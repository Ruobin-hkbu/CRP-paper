# Corpus Analysis Plan

Date: April 13, 2026
Project: AI Poetry Co-Creation Study

## 1. Purpose and Scope

This plan operationalizes the paper's revised claims by focusing on bounded, answerable corpus analysis rather than universal statements about AI creativity. The analysis is designed to answer three questions:

1. How AI co-creation may shape stylistic selection.
2. When participants stay within defaults versus resist them.
3. Which style features are repeatedly suggested, rarely suggested, or difficult to elicit.

Unit of generalization: this dataset only.

## 2. Corpus Definition

Primary corpus components:

1. Human-AI chat transcripts from poetry writing sessions.
2. AI suggestions at each turn.
3. Human revisions and final poem outputs.
4. Interaction metadata where available (timestamps, room mode, parameter settings).

Minimum recommended analytic subset:

1. 8-12 representative sessions for deep coding.
2. Include both Structured Studio and Exploratory Atelier conditions if available.
3. Include sessions with different participant confidence levels or writing goals.

Session inclusion criteria:

1. Session has at least one full interaction cycle (prompt -> AI response -> human revision).
2. Final text or near-final draft exists.
3. Log quality is sufficient to trace stylistic decision points.

Session exclusion criteria:

1. Incomplete logs where turn sequence cannot be reconstructed.
2. Sessions with only one-shot output and no participant revision.
3. Corrupted or duplicate records.

## 3. Data Preparation Workflow

### 3.1 File Inventory and Naming

Create a consistent folder schema:

1. `data/raw/` for original exports.
2. `data/clean/` for normalized transcripts.
3. `coding/` for coding sheets and codebook versions.
4. `outputs/` for tables, figures, excerpts.

Use a session ID format:

1. `S01`, `S02`, and so on.
2. Turn IDs within each session: `S01_T01`, `S01_T02`.

### 3.2 Transcript Normalization

For each session:

1. Separate speaker turns into `HUMAN` and `AI`.
2. Mark the interaction phase: prompt, suggestion, revision, reflection.
3. Preserve original wording.
4. Remove personally identifying information.

### 3.3 Analysis Table Template

Build a row-per-turn table with these columns:

1. `session_id`
2. `turn_id`
3. `mode` (structured or exploratory)
4. `speaker`
5. `turn_text`
6. `interaction_type`
7. `target_style_feature`
8. `feature_presence` (present, partial, absent)
9. `elicitation_attempt_number`
10. `human_action` (accept, modify, reject, redirect)
11. `default_pattern_flag` (yes or no)
12. `resistance_flag` (yes or no)
13. `evidence_note`

## 4. Codebook and Operational Definitions

### 4.1 Interaction Type Codes

Use three primary categories:

1. Exemplar-led: AI provides polished, ready-to-use text with low human transformation.
2. Negotiation-oriented: human requests revision and iteratively reshapes AI output.
3. Critical-relational resistance: human explicitly identifies and contests recurring AI tendencies or missing stylistic options.

Decision rule:

1. Code each turn by dominant function.
2. If ambiguous, mark as mixed and record rationale in memo.

### 4.2 Style Feature List

Pre-register a bounded feature set before full coding. Suggested starter set:

1. Syntax compression.
2. Semantic opacity.
3. Anti-lyric fragmentation.
4. Dialect or non-standard register.
5. Meter irregularity.
6. Unusual line break logic.
7. Figurative novelty outside corpus-typical lyric diction.

You can refine the list after pilot coding of 2 sessions, but freeze it before full analysis.

### 4.3 Difficult-to-Elicit Definition

A feature is coded as difficult to elicit when:

1. The feature is explicitly requested.
2. At least 3 prompt variants are attempted.
3. At least 2 explicit revision requests are made.
4. Output remains absent or only partial.

This is a bounded empirical category, not proof of absolute impossibility.

### 4.4 Default Pattern and Resistance

Default pattern indicators:

1. Recurrent smoothing toward generic coherence.
2. Repetition of familiar lyric diction.
3. Preference for high-probability figurative patterns.

Resistance indicators:

1. Participant explicitly names AI recurrence or limitation.
2. Participant rejects default output and introduces alternative form.
3. Participant requests style beyond model's recurrent tendencies.

## 5. Coding Procedure

### 5.1 Pilot Round

1. Code 2 sessions fully.
2. Record ambiguities.
3. Tighten definitions.
4. Freeze codebook version `v1.0`.

### 5.2 Main Coding Round

1. Code all selected sessions turn by turn.
2. Tag interaction type per turn.
3. Tag requested style feature where applicable.
4. Mark feature outcome as present, partial, or absent.
5. Mark human action and resistance signal.

### 5.3 Reliability Check

If you have a second coder:

1. Double-code 20-25% of sessions.
2. Compute agreement for interaction type and feature outcome.
3. Resolve disagreements and update decision memo.

If solo coding:

1. Re-code a 15% subset after 5-7 days.
2. Compare your own first and second pass.
3. Document reconciliation rules.

## 6. Analysis Strategy by Research Question

### RQ1: Effect on Stylistic Selection

Quantitative checks:

1. Count frequency of feature types in AI suggestions.
2. Compare feature diversity across modes.
3. Count how often human final drafts diverge from AI defaults.

Qualitative checks:

1. Extract excerpts showing narrowed option space.
2. Identify moments where alternatives were not surfaced by AI until human pressure.

Expected evidence product:

1. Table of recurrent AI features versus human-added features.
2. Short excerpt set illustrating pre-curation.

### RQ2: Conditions of Compliance versus Resistance

Quantitative checks:

1. Proportion of turns coded exemplar-led, negotiation-oriented, critical-relational.
2. Resistance rate by mode.
3. Acceptance versus modification versus rejection rates.

Qualitative checks:

1. Process-trace 3-5 sessions from initial prompt to final poem.
2. Identify turning points where negotiation became explicit critique.

Expected evidence product:

1. Transition map from negotiation to resistance.
2. Comparative mini-case narratives.

### RQ3: Repeated, Rare, and Difficult-to-Elicit Features

Quantitative checks:

1. Frequency rank of style features in AI outputs.
2. Difficult-to- elicit rate by feature.
3. Average attempts needed per feature.

Qualitative checks:

1. Close reading of failed elicitation attempts.
2. Compare AI outputs with participant revisions that achieve target effects.

Expected evidence product:

1. Feature matrix with repeated, rare, difficult-to-elicit labels.
2. Appendix-ready coding examples.

## 7. Output Templates

Prepare these tables for the paper:

1. Corpus summary table: sessions, turns, modes, participant profile basics.
2. Interaction distribution table by mode.
3. Style feature frequency table.
4. Difficult-to-elicit matrix by feature and session.
5. Human action table: accept, modify, reject, redirect.

Prepare these figures:

1. Sankey or flow chart from interaction type to outcome.
2. Bar chart of repeated versus difficult-to-elicit features.

Prepare these qualitative artifacts:

1. Three representative annotated transcript excerpts.
2. One full process-trace case in appendix.

## 8. Claim Calibration Rules for Writing

Use calibrated language:

1. Use "in this sample," "suggests," "indicates," "tends to."
2. Avoid "proves," "always," "cannot in principle."
3. Distinguish observed tendency from theoretical interpretation.

Link evidence to theory explicitly:

1. Marcuse: narrowing of thinkable options and language forms.
2. Adorno: administered standardization effects.
3. Feenberg: possibility of redesign and democratizing intervention.
4. Haraway: critical-relational engagement rather than passive use.

## 9. Risks and Mitigation

Risk: Over-interpretation from small sample.
Mitigation: Keep claims bounded and show transparent coding criteria.

Risk: Ambiguous coding boundaries.
Mitigation: Decision memo plus pilot refinement and reliability check.

Risk: Confirmation bias toward critical theory.
Mitigation: Include disconfirming cases where AI did produce unexpected stylistic variation.

Risk: Drift in feature definitions.
Mitigation: Freeze codebook after pilot and track any later deviations.

## 10. 7-Day Execution Schedule

Day 1:

1. Finalize session subset.
2. Build data table and codebook draft.

Day 2:

1. Pilot coding on 2 sessions.
2. Refine and freeze codebook.

Day 3:

1. Code first half of corpus.
2. Write analytic memos.

Day 4:

1. Code second half.
2. Run reliability check or self-check.

Day 5:

1. Produce frequency tables and feature matrix.
2. Select representative excerpts.

Day 6:

1. Draft findings sections aligned to RQ1-RQ3.
2. Add theory linkage paragraphs.

Day 7:

1. Calibrate claims and limitations.
2. Finalize visuals, appendix materials, and method transparency notes.

## 11. Minimum Viable Deliverables Checklist

1. Clean corpus table with turn-level coding.
2. Frozen codebook with definitions and examples.
3. Feature matrix marking repeated, rare, difficult-to-elicit.
4. At least 3 evidence excerpts tied to each RQ.
5. One limitations paragraph and one future-work paragraph.