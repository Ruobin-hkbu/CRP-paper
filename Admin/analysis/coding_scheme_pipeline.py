"""Coding scheme pipeline for CRP qualitative transcript analysis.

This script supports a three-stage workflow:
1) convert: transform speaker-by-speaker platform logs into paired turn CSVs.
2) prepare: convert raw transcript CSV into a coding sheet with provisional labels.
3) analyze: summarize completed coding and extract case candidates.

Usage examples (speaker-by-speaker platform log):
  python Admin/analysis/coding_scheme_pipeline.py convert \
    --input Admin/analysis/templates/speaker_log_template.csv \
    --output Admin/analysis/raw_transcript.csv

  python Admin/analysis/coding_scheme_pipeline.py prepare \
    --input Admin/analysis/raw_transcript.csv \
    --output Admin/analysis/coding_sheet.csv

  python Admin/analysis/coding_scheme_pipeline.py analyze \
    --input Admin/analysis/coding_sheet.csv \
    --outdir Admin/analysis/results

Expected speaker-log CSV columns:
  session_id      - e.g. S01
  utterance_id    - e.g. S01_U01 (used for ordering within session)
  speaker         - exactly 'human' or 'ai' (case-insensitive)
  text            - the utterance text
  final_poem_excerpt - optional; non-empty on the last human turn that carries the final poem
"""

from __future__ import annotations

import argparse
import csv
import json
import re
from collections import Counter, defaultdict
from pathlib import Path
from typing import Dict, Iterable, List, Tuple

FEATURES: List[Tuple[str, str]] = [
    ("syntax_compression", "Syntax compression"),
    ("semantic_opacity", "Semantic opacity"),
    ("anti_lyric_fragmentation", "Anti-lyric fragmentation"),
    ("non_standard_register_or_dialect", "Non-standard register or dialect"),
    ("meter_irregularity", "Meter irregularity"),
    ("unusual_line_break_logic", "Unusual line-break logic"),
    ("figurative_novelty", "Figurative novelty"),
]

ALLOWED_RATINGS = {"present", "partial", "absent", ""}

NEGOTIATION_MARKERS = {
    "revise",
    "rewrite",
    "change",
    "make it",
    "more",
    "less",
    "instead",
    "not",
    "again",
    "try",
    "different",
    "remove",
    "replace",
    "edit",
    "adjust",
    "fix",
    "shorter",
    "longer",
    "stronger",
}

CRITICAL_RELATIONAL_MARKERS = {
    "too generic",
    "generic",
    "predictable",
    "formulaic",
    "typical ai",
    "sounds ai",
    "ai-like",
    "cliche",
    "overly polished",
    "not my voice",
    "not my style",
    "stereotyped",
}


def normalize_space(text: str) -> str:
    return re.sub(r"\s+", " ", (text or "").strip())


def to_lower(text: str) -> str:
    return normalize_space(text).lower()


def detect_interaction_category(human_prompt: str) -> Tuple[str, str]:
    lowered = to_lower(human_prompt)
    if any(marker in lowered for marker in NEGOTIATION_MARKERS):
        return (
            "Negotiation-oriented",
            "Prompt contains revision/constraint markers suggesting iterative reshaping.",
        )
    return (
        "Exemplar-led",
        "No clear revision markers; turn appears oriented to receiving a ready-made output.",
    )


def detect_critical_relational_marker(*texts: str) -> Tuple[str, str]:
    merged = " ".join(to_lower(t) for t in texts if t)
    for marker in sorted(CRITICAL_RELATIONAL_MARKERS):
        if marker in merged:
            return "yes", marker
    return "", ""


def read_rows(path: Path) -> List[Dict[str, str]]:
    with path.open("r", encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        return [dict(r) for r in reader]


def write_rows(path: Path, rows: List[Dict[str, str]], fieldnames: List[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def ensure_base_columns(rows: Iterable[Dict[str, str]]) -> None:
    required = {"session_id", "turn_id", "human_prompt", "ai_response"}
    if not rows:
        raise ValueError("Input CSV is empty.")
    header = set(next(iter(rows)).keys())
    missing = required - header
    if missing:
        raise ValueError(f"Input CSV missing required column(s): {', '.join(sorted(missing))}")


# ---------------------------------------------------------------------------
# Speaker-by-speaker → turn-pair conversion
# ---------------------------------------------------------------------------

def convert_speaker_log(input_path: Path, output_path: Path) -> None:
    """Group speaker-row logs into human/AI turn pairs.

    Pairing rules:
    - Each block of consecutive human utterances (before the next AI turn)
      is concatenated as one human_prompt.
    - The following AI utterance(s) are concatenated as ai_response.
    - If human utterances follow an AI response before a new AI response,
      they begin a new turn pair.
    - The final_poem_excerpt is carried from the last human row in the session
      that contains a non-empty value.
    - Skipped/empty utterances are ignored.
    """
    rows = read_rows(input_path)
    required = {"session_id", "utterance_id", "speaker", "text"}
    if not rows:
        raise ValueError("Speaker log CSV is empty.")
    header = set(rows[0].keys())
    missing = required - header
    if missing:
        raise ValueError(
            f"Speaker log CSV missing required column(s): {', '.join(sorted(missing))}"
        )

    # Group by session, preserving utterance_id order.
    sessions: Dict[str, List[Dict[str, str]]] = defaultdict(list)
    for row in rows:
        sessions[normalize_space(row["session_id"])].append(row)

    turn_rows: List[Dict[str, str]] = []

    for session_id, utterances in sessions.items():
        # Sort by utterance_id lexicographically (works for zero-padded IDs like U01, U02...).
        utterances = sorted(utterances, key=lambda r: normalize_space(r["utterance_id"]))

        # Walk utterances and pair human blocks with following AI blocks.
        i = 0
        turn_counter = 0

        while i < len(utterances):
            row = utterances[i]
            speaker = normalize_space(row["speaker"]).lower()

            if speaker != "human":
                # Orphan AI utterance at start of session - skip.
                i += 1
                continue

            # Collect consecutive human utterances.
            human_parts: List[str] = []
            human_poem: str = ""
            while i < len(utterances) and normalize_space(utterances[i]["speaker"]).lower() == "human":
                text = normalize_space(utterances[i]["text"])
                if text:
                    human_parts.append(text)
                poem_fragment = normalize_space(utterances[i].get("final_poem_excerpt", ""))
                if poem_fragment:
                    human_poem = poem_fragment
                i += 1

            # Collect immediately following consecutive AI utterances.
            ai_parts: List[str] = []
            while i < len(utterances) and normalize_space(utterances[i]["speaker"]).lower() == "ai":
                text = normalize_space(utterances[i]["text"])
                if text:
                    ai_parts.append(text)
                i += 1

            if not human_parts:
                continue

            turn_counter += 1
            turn_id = f"{session_id}_T{turn_counter:02d}"

            turn_rows.append(
                {
                    "session_id": session_id,
                    "turn_id": turn_id,
                    "human_prompt": " / ".join(human_parts),
                    "ai_response": " / ".join(ai_parts) if ai_parts else "",
                    "human_revision": "",
                    "final_poem_excerpt": human_poem,
                }
            )

    if not turn_rows:
        raise ValueError("No valid human→AI turn pairs found in the speaker log.")

    write_rows(
        output_path,
        turn_rows,
        ["session_id", "turn_id", "human_prompt", "ai_response", "human_revision", "final_poem_excerpt"],
    )
    print(f"Converted {len(turn_rows)} turn pair(s) from {len(rows)} speaker rows.")


def prepare_sheet(input_path: Path, output_path: Path) -> None:
    rows = read_rows(input_path)
    ensure_base_columns(rows)

    prepared: List[Dict[str, str]] = []
    for row in rows:
        prompt = row.get("human_prompt", "")
        revision = row.get("human_revision", "")
        category, rationale = detect_interaction_category(prompt)
        critical_flag, marker = detect_critical_relational_marker(prompt, revision)

        out = dict(row)
        out["interaction_category_provisional"] = category
        out["interaction_category_final"] = ""
        out["interaction_rationale"] = rationale

        for feature_key, _feature_label in FEATURES:
            out[f"{feature_key}_ai"] = ""
            out[f"{feature_key}_human"] = ""
            out[f"{feature_key}_evidence"] = ""

        out["difficult_target_feature"] = ""
        out["difficult_attempt_type"] = ""
        out["difficult_case_note"] = ""
        out["critical_relational_flag"] = critical_flag
        out["critical_marker_detected"] = marker
        out["critical_relational_note"] = ""

        prepared.append(out)

    base_fields = list(prepared[0].keys())
    write_rows(output_path, prepared, base_fields)


def normalize_rating(value: str) -> str:
    return to_lower(value)


def get_interaction_label(row: Dict[str, str]) -> str:
    final_label = normalize_space(row.get("interaction_category_final", ""))
    if final_label:
        return final_label
    return normalize_space(row.get("interaction_category_provisional", ""))


def analyze_sheet(input_path: Path, outdir: Path) -> None:
    rows = read_rows(input_path)
    ensure_base_columns(rows)

    outdir.mkdir(parents=True, exist_ok=True)

    interaction_counts: Counter[str] = Counter()
    feature_by_interaction_ai: Dict[str, Counter[str]] = defaultdict(Counter)
    feature_by_interaction_human: Dict[str, Counter[str]] = defaultdict(Counter)
    rating_warnings: List[str] = []

    difficult_candidates: List[Dict[str, str]] = []
    by_session_feature: Dict[Tuple[str, str], List[Dict[str, str]]] = defaultdict(list)

    critical_cases: List[Dict[str, str]] = []

    for row in rows:
        interaction = get_interaction_label(row) or "Unlabeled"
        interaction_counts[interaction] += 1

        for feature_key, feature_label in FEATURES:
            ai_col = f"{feature_key}_ai"
            human_col = f"{feature_key}_human"

            ai_rating = normalize_rating(row.get(ai_col, ""))
            human_rating = normalize_rating(row.get(human_col, ""))

            if ai_rating not in ALLOWED_RATINGS:
                rating_warnings.append(
                    f"{row.get('turn_id', '')}: invalid AI rating in {ai_col} -> {row.get(ai_col, '')}"
                )
            if human_rating not in ALLOWED_RATINGS:
                rating_warnings.append(
                    f"{row.get('turn_id', '')}: invalid human rating in {human_col} -> {row.get(human_col, '')}"
                )

            if ai_rating:
                feature_by_interaction_ai[f"{feature_label} | {interaction}"][ai_rating] += 1
            if human_rating:
                feature_by_interaction_human[f"{feature_label} | {interaction}"][human_rating] += 1

        target_feature = normalize_space(row.get("difficult_target_feature", ""))
        if target_feature:
            key = (normalize_space(row.get("session_id", "")), target_feature)
            by_session_feature[key].append(row)

        crit_flag = to_lower(row.get("critical_relational_flag", ""))
        if crit_flag in {"yes", "true", "1"} or row.get("critical_marker_detected", ""):
            critical_cases.append(
                {
                    "session_id": row.get("session_id", ""),
                    "turn_id": row.get("turn_id", ""),
                    "human_prompt": row.get("human_prompt", ""),
                    "critical_marker_detected": row.get("critical_marker_detected", ""),
                    "critical_relational_note": row.get("critical_relational_note", ""),
                }
            )

    for (session_id, feature), episode_rows in by_session_feature.items():
        distinct_prompts = {
            to_lower(r.get("human_prompt", ""))
            for r in episode_rows
            if normalize_space(r.get("human_prompt", ""))
        }
        attempt_count = len(episode_rows)

        # Treat as candidate when at least two substantively different prompt attempts exist.
        if attempt_count >= 2 and len(distinct_prompts) >= 2:
            difficult_candidates.append(
                {
                    "session_id": session_id,
                    "feature": feature,
                    "attempt_count": str(attempt_count),
                    "distinct_prompt_count": str(len(distinct_prompts)),
                    "turn_ids": ", ".join(r.get("turn_id", "") for r in episode_rows),
                }
            )

    summary = {
        "total_turns": len(rows),
        "interaction_counts": dict(interaction_counts),
        "feature_by_interaction_ai": {
            k: dict(v) for k, v in sorted(feature_by_interaction_ai.items())
        },
        "feature_by_interaction_human": {
            k: dict(v) for k, v in sorted(feature_by_interaction_human.items())
        },
        "rating_warnings": rating_warnings,
        "difficult_to_elicit_candidate_count": len(difficult_candidates),
        "critical_relational_case_count": len(critical_cases),
    }

    (outdir / "summary.json").write_text(
        json.dumps(summary, indent=2, ensure_ascii=True), encoding="utf-8"
    )

    write_rows(
        outdir / "difficult_to_elicit_candidates.csv",
        difficult_candidates,
        ["session_id", "feature", "attempt_count", "distinct_prompt_count", "turn_ids"],
    )

    write_rows(
        outdir / "critical_relational_cases.csv",
        critical_cases,
        [
            "session_id",
            "turn_id",
            "human_prompt",
            "critical_marker_detected",
            "critical_relational_note",
        ],
    )

    md_lines = [
        "# Coding Analysis Summary",
        "",
        f"Total turns: {len(rows)}",
        "",
        "## Interaction Counts",
    ]
    for label, count in interaction_counts.most_common():
        md_lines.append(f"- {label}: {count}")

    md_lines.extend([
        "",
        "## Difficult-to-Elicit Candidates",
        f"- Candidate episodes: {len(difficult_candidates)}",
        "",
        "## Critical-Relational Cases",
        f"- Flagged cases: {len(critical_cases)}",
    ])

    if rating_warnings:
        md_lines.extend(["", "## Rating Warnings"])
        for warning in rating_warnings:
            md_lines.append(f"- {warning}")

    (outdir / "summary.md").write_text("\n".join(md_lines) + "\n", encoding="utf-8")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="CRP coding scheme analysis pipeline")
    sub = parser.add_subparsers(dest="command", required=True)

    convert_cmd = sub.add_parser(
        "convert", help="Convert speaker-by-speaker platform log into turn-pair CSV"
    )
    convert_cmd.add_argument("--input", required=True, help="Path to speaker log CSV")
    convert_cmd.add_argument("--output", required=True, help="Path for generated turn-pair CSV")

    prepare_cmd = sub.add_parser(
        "prepare", help="Generate coding sheet from turn-pair transcript CSV"
    )
    prepare_cmd.add_argument("--input", required=True, help="Path to turn-pair transcript CSV")
    prepare_cmd.add_argument("--output", required=True, help="Path to generated coding sheet CSV")

    analyze_cmd = sub.add_parser(
        "analyze", help="Analyze completed coding sheet and export summaries"
    )
    analyze_cmd.add_argument("--input", required=True, help="Path to coding sheet CSV")
    analyze_cmd.add_argument("--outdir", required=True, help="Directory for analysis outputs")

    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()

    if args.command == "convert":
        convert_speaker_log(Path(args.input), Path(args.output))
        print(f"Turn-pair CSV written to: {args.output}")
    elif args.command == "prepare":
        prepare_sheet(Path(args.input), Path(args.output))
        print(f"Prepared coding sheet: {args.output}")
    elif args.command == "analyze":
        analyze_sheet(Path(args.input), Path(args.outdir))
        print(f"Analysis written to: {args.outdir}")


if __name__ == "__main__":
    main()
