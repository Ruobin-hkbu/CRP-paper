# Coding Scheme Pipeline (Python)

This folder provides a practical coding workflow aligned with your four-part method:

1. Identify interaction categories (`Exemplar-led`, `Negotiation-oriented`).
2. Track stylistic features with `Present/Partial/Absent` ratings.
3. Extract difficult-to-elicit case candidates.
4. Extract possible critical-relational case candidates.

## Files

- `coding_scheme_pipeline.py`: main script.
- `templates/speaker_log_template.csv`: input template for speaker-by-speaker platform logs.
- `templates/raw_transcript_template.csv`: alternative input if you already have turn-pair data.

## Input: Speaker-by-Speaker Platform Log

Your platform log CSV must have these columns:

| Column | Description |
|--------|-------------|
| `session_id` | e.g. `S01` |
| `utterance_id` | e.g. `S01_U01` — determines row order within a session |
| `speaker` | exactly `human` or `ai` (case-insensitive) |
| `text` | the utterance text |
| `final_poem_excerpt` | optional; fill in only on the last human turn containing the final poem |

See [templates/speaker_log_template.csv](templates/speaker_log_template.csv) for an example.

## Step 1: Convert Speaker Log → Turn-Pair CSV

```powershell
python Admin/analysis/coding_scheme_pipeline.py convert --input Admin/analysis/templates/speaker_log_template.csv --output Admin/analysis/raw_transcript.csv
```

The converter groups consecutive human utterances (before each AI response) into one `human_prompt` and the following AI utterance(s) into one `ai_response`. Multiple consecutive utterances from the same speaker are joined with ` / `.

## Step 2: Prepare Coding Sheet

```powershell
python Admin/analysis/coding_scheme_pipeline.py prepare --input Admin/analysis/raw_transcript.csv --output Admin/analysis/coding_sheet.csv
```

Open `Admin/analysis/coding_sheet.csv` and complete/verify:

- `interaction_category_final` — confirm or override provisional label
- Feature ratings (`*_ai`, `*_human`) — use `present`, `partial`, or `absent`
- Difficult-to-elicit notes (`difficult_target_feature`, `difficult_attempt_type`, `difficult_case_note`)
- Critical-relational notes (`critical_relational_note`)

## Step 3: Run Analysis

```powershell
python Admin/analysis/coding_scheme_pipeline.py analyze --input Admin/analysis/coding_sheet.csv --outdir Admin/analysis/results
```

Outputs in `Admin/analysis/results/`:

| File | Contents |
|------|----------|
| `summary.md` | Interaction counts, case totals, rating warnings |
| `summary.json` | Same data in machine-readable form |
| `difficult_to_elicit_candidates.csv` | Episodes with 2+ distinct prompt attempts for a target feature |
| `critical_relational_cases.csv` | Turns flagged for critical-relational markers or manual notes |

## Notes

- Provisional interaction labels are heuristic and should be human-checked.
- Case outputs are candidate lists designed to support close qualitative reading, not replace it.
- If your platform uses different speaker labels (e.g. `User`/`Assistant`), update them to `human`/`ai` before running `convert`.
