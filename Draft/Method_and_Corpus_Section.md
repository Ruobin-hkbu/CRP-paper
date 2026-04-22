# IV. Method and Corpus

## IV.1 Dataset and Study Boundary

This study is a qualitative examination of poetry writing sessions conducted in a university creative writing seminar for advanced L2 English learners. The data were generated through a purpose-built AI co-creation platform that logs chat transcripts, final poem outputs, and reflective commentary. The workshop operated in two modes—Structured Studio (guided prompting templates) and Exploratory Atelier (open-ended dialogue)—though the study does not use mode as a causal variable but rather as context for understanding how different interaction structures enabled or constrained critical engagement.

The primary dataset consists of human-AI dialogue records from 8–12 representative writing sessions. Sessions were selected for inclusion if they contained at least one complete interaction cycle (prompt → AI response → human revision) and yielded sufficient transcript quality to reconstruct stylistic decision points and moments of participant reasoning. Excluded sessions were those with incomplete logs, one-shot outputs without subsequent human revision, or corrupted records.

The analysis focuses exclusively on turn-level qualitative evidence: the linguistic and functional character of AI suggestions, the form and timing of human responses, the specific language of revisions and rejections, and the textual features present or absent in participants' final work. Rather than aggregating patterns across all turns, the study traces how particular features recur across sessions and identifies moments when writers recognize and contest recurring defaults.

This is an explicitly bounded study. Claims are limited to observed patterns within this corpus and explicitly do not constitute proof of what AI systems cannot generate in principle, only what remained difficult to elicit within the conditions and interaction styles documented here. By design, the study makes no attempt to generalize across different models, datasets, or pedagogical contexts; rather, it uses this contained setting to examine the relationship between model output tendencies, user interaction, and the emergence of critical awareness in one concrete case.

## IV.2 Interaction Categories

To analyze how writers navigate AI suggestions, the study employs three primary coding categories that map interaction functions rather than participant intentions. The category structure builds in part on McQuire et al. (2024), who show that learner engagement tends to decline when participants are given an AI-generated poem and asked merely to edit it, whereas creativity and self-efficacy increase when participants co-create with AI through iterative exchange. That distinction is especially useful here because it helps separate turns in which the AI output functions primarily as a pre-formed exemplar from turns in which meaning and form are negotiated across interaction. The framework is further refined through scholarship on collaborative writing and iterative prompt interaction.

**Exemplar-led turns.** The AI provides polished, coherent, stylistically recognizable text presented as a self-contained option. The human's response is typically acceptance with minimal modification, or acceptance followed by a separate new prompt rather than revision of the offered text. In these turns, the AI proposal functions as an exemplar — a form ready to be adopted or set aside rather than negotiated. McQuire et al. (2024) are especially relevant here because they suggest that when learners are positioned mainly as editors of pre-generated AI poems, engagement can diminish. This dynamic also draws on a well-established tradition in writing pedagogy in which model texts organize imitation before critique (Swales, 1990); what changes in the AI context is that the exemplar is generated on demand and presented without explicit acknowledgment of its role as a stylistic template. Research on automated text suggestion acceptance similarly shows that users tend toward low-effort selection when output quality is locally plausible, even when the suggestion forecloses alternatives (Buschek et al., 2021).

**Negotiation-oriented turns.** The human explicitly requests revision, specifies dissatisfaction with output, or iteratively reshapes AI suggestions. These turns involve back-and-forth interaction in which the human introduces constraints, alternative phrasings, or formal requests that the AI then attempts to accommodate. While negotiation creates friction and may prompt the model to generate alternatives, it often remains within the field of possibilities that the model itself pre-curates. Negotiation becomes visible as a distinct interaction mode, but the option space itself remains bounded. McQuire et al. (2024) are also important here because they indicate that creativity can re-emerge when learners move from editing a finished AI text to co-creating through interaction, suggesting that iterative exchange matters even if it does not by itself guarantee critical resistance. This category is consistent with collaborative writing research that distinguishes sequential from dialogic co-authorship (Lowry et al., 2004), and with conversation analytic accounts of how interlocutors establish and repair common ground across turns (Clark & Schaefer, 1989); in the human-AI case, however, the AI does not hold prior intentions or shared knowledge in the same sense, which means negotiation is asymmetric in ways that prior dyadic models do not fully capture.

**Critical-relational turns.** The human explicitly identifies and names a recurrent AI pattern, rejects it on grounds of recognizing its typicality, or introduces stylistic features absent from the model's suggestions. In these moments, the human moves from selecting within offered options to questioning the logic that organizes the option set itself. This category marks the threshold at which participants begin to recognize and contest administered defaults, and corresponds to the critical-relational stance theorized through Haraway's situated engagement with the machine.

Each turn is coded by its dominant function. Ambiguous or mixed turns are flagged and recorded with supporting rationale.

## IV.3 Stylistic Features and Coding Strategy

To operationalize the paper's claim that AI suggestions shape stylistic possibility, the study tracks a set of poetic features identified through two converging sources: pilot reading of the corpus, in which these features were rarely or only partially present in AI suggestions across early sessions; and existing scholarship in computational poetics and AI text generation, which has documented related tendencies. Research on high-probability token selection in neural language models (Holtzman et al., 2020) explains why outputs tend toward coherent, smooth, and contextually expected sequences rather than syntactically deviant or semantically unstable ones. Work in computational poetics (Gervás, 2001; Oliveira, 2017) has noted the persistent difficulty of generating metrically irregular or structurally disruptive verse. Studies on training data bias have documented the underrepresentation of non-prestige registers and dialect forms in large language model corpora (Bender et al., 2021). No single source establishes all seven features as a unified list; rather, the feature set is assembled from these converging lines of evidence and then grounded in what the pilot reading of this corpus specifically showed. The features tracked are:

1. **Syntax compression.** Extreme reduction of grammatical elaboration; elliptical or paratactic structures that omit expected grammatical elements.
2. **Semantic opacity.** Imagery or figurative language resistant to paraphrase; intentional obscurity or semantic instability.
3. **Anti-lyric fragmentation.** Disruption of expected lyric coherence; abrupt shifts in register, reference, or address.
4. **Non-standard register or dialect.** Deviation from prestige or corpus-typical language norms; use of dialect, slang, or register incongruent with dominant training corpora.
5. **Meter irregularity.** Unpredictable stress patterns; deliberate metrical disturbance in poems employing metrical frameworks.
6. **Unusual line-break logic.** Line breaks that cut across grammatical or semantic units in unexpected ways.
7. **Figurative novelty.** Metaphor or simile outside recognizable patterns in training data; imaginative constructions that resist corpus-typical lyric diction.

For each stylistic feature, human and AI contributions are coded on a three-point scale:

- **Present:** The feature appears clearly in the output.
- **Partial:** The feature appears in limited form, only after explicit pressure, or only in isolated sections.
- **Absent:** The feature does not appear despite requests or attempts.

The coding process involves close reading of AI suggestions at each turn, human revisions, and the final poem, with side-by-side comparison to identify which formal possibilities humans added that the model did not supply, and which features remained inaccessible despite human effort.

## IV.4 Operationalizing "Difficult to Elicit"

To avoid overclaiming machine incapacity, the study defines *difficult to elicit* as a qualitative threshold of sustained effort, assessed through close reading of the transcript rather than by counting turns or attempts.

The justification for requiring sustained, varied effort before applying this category comes from two bodies of research. Jiang et al. (2020) demonstrate that language model outputs are highly sensitive to prompt formulation, such that rephrasing alone can substantially change what a model produces; this means that single-attempt failures are not reliable evidence of model limitation and that substantively varied attempts are methodologically necessary before any difficulty claim can be made. Zamfirescu-Pereira et al. (2023) show that even users making repeated, genuine efforts to refine their prompts frequently fail to elicit desired outputs — and frame this pattern as a structural feature of human-AI interaction rather than individual user error, which supports treating sustained unsuccessful effort as an index of elicitation difficulty rather than inexperience.

Informed by this rationale, a stylistic feature in this study is operationalized as difficult to elicit when the transcript shows a participant making sustained, substantively varied attempts — rephrasing requests, shifting framing, or supplying examples — without obtaining the desired output, and when the researcher's close reading confirms that the attempts were genuinely distinct in their approach rather than minor rewordings. The category does not prove that the model cannot generate such features in other contexts; rather, it documents what occurred in this dataset when writers sought specific forms under these interaction conditions. Difficulty, in this sense, is a situated and relational finding: a property of the encounter between a particular participant, a particular stylistic goal, and a particular model in a particular session — not a claim about the model's absolute capacity.

## IV.5 Analytic Approach

Analysis proceeds through close qualitative reading of transcript records assigned session IDs (`S01`, `S02`, etc.) and turn IDs (`S01_T01`, `S01_T02`, etc.). For each session, the study traces when and how participants encounter recurring AI patterns, how they respond to those patterns (accepting, modifying, rejecting, or redirecting), and whether they develop explicit awareness of the model's stylistic tendencies.

Findings are presented through detailed analysis of 3–5 representative session trajectories that illustrate (1) how AI defaults shape the option space before explicit evaluation, (2) how negotiation-oriented interaction may or may not generate critical recognition, and (3) moments when writers explicitly identify and contest administered patterns. By grounding claims in specific dialogue sequences and comparing patterns across sessions, the analysis demonstrates how AI co-creation structures stylistic choice without overextending claims beyond the corpus itself.

## IV.6 Specific Coding Plan for Data Analysis

To implement the analytic framework above in a replicable way, coding will proceed in four linked parts. The workflow is sequential, but coders may return to earlier parts when later evidence requires refinement.

### Part 1. Identify Interaction Types and Sort Turns Into Categories

**Unit of coding.** The primary unit is the turn pair (human request plus immediate AI response), with follow-up human revision notes attached as contextual evidence.

**Step 1: Prepare transcript units.**

1. Segment each session into turn pairs and assign IDs (`S01_T01`, `S01_T02`, etc.).
2. Preserve the original wording of prompts, AI outputs, and visible human edits.
3. Add a short memo (1-2 lines) describing what the human appears to be doing in that turn.

**Step 2: Apply interaction-category decision rules.**

- Code as **Exemplar-led** when the AI output is treated as a ready-made option and the human accepts it with minimal local adjustment, or moves to a new prompt without substantial revision dialogue.
- Code as **Negotiation-oriented** when the human requests revision, specifies dissatisfaction, imposes new constraints, or iteratively reshapes the same output trajectory across turns.
- If a turn contains both functions, assign the **dominant** function and add an ambiguity memo explaining why.

**Step 3: Record coding evidence.**

For each coded turn, record:

1. Category label (`Exemplar-led` or `Negotiation-oriented`).
2. Evidence quote from the human prompt and/or AI response.
3. Brief rationale (one sentence) tied to the operational definition.

### Part 2. Track Stylistic Features Within Categories (Present/Partial/Absent)

After interaction coding, each turn is coded for the seven stylistic features listed in IV.3.

**Step 1: Feature-by-turn coding matrix.**

Build a matrix where rows are turn IDs and columns include:

1. Interaction category (from Part 1).
2. Seven stylistic features.
3. Rating for each feature: `Present`, `Partial`, or `Absent`.
4. Evidence note (short quote or description).

**Step 2: Apply consistent rating rules.**

- **Present:** clear and sustained realization of the feature in the AI output or revised human text.
- **Partial:** feature appears weakly, locally, or only after explicit prompting pressure.
- **Absent:** feature not realized despite request, attempt, or opportunity.

**Step 3: Compare by interaction category.**

Within each session, compare feature profiles across `Exemplar-led` and `Negotiation-oriented` turns to identify:

1. Features frequently stabilized by AI defaults.
2. Features that improve only under negotiation.
3. Features that remain mostly absent in both categories.

### Part 3. Case Analysis of "Difficult to Elicit"

This part focuses on failed or only partially successful attempts to obtain target stylistic features despite sustained effort.

**Step 1: Select candidate episodes.**

Mark an episode as a candidate when all of the following are visible:

1. The human explicitly names a stylistic goal.
2. The human makes substantively varied attempts (rephrasing, reframing, examples, or stronger constraints).
3. The output remains absent or only partial for the target feature.

**Step 2: Reconstruct conversation flow in detail.**

For each selected episode, produce a micro-timeline:

1. Initial request and target feature.
2. Sequence of prompt adjustments by the human.
3. AI response pattern at each step.
4. Final outcome in the poem draft.

**Step 3: Interpret why elicitation remained difficult.**

Use close reading to identify whether difficulty appears linked to:

1. AI drift back to fluent/default lyric form.
2. Weak compliance with unconventional constraints.
3. Local compliance without global structural change.

Each case write-up should include direct transcript excerpts and a short analytic claim limited to that episode.

### Part 4. Case Analysis of Possible Critical-Relational Stance

This part identifies moments where participants move beyond revision toward explicit critique of model defaults.

**Step 1: Identify critical-relational indicators.**

Flag episodes where the human does one or more of the following:

1. Names a recurring AI pattern as formulaic, generic, or predictable.
2. Rejects an output because it reflects "typical AI" style rather than the writer's intent.
3. Introduces an alternative stylistic principle not offered by the AI.

**Step 2: Conduct focused case reading.**

For each flagged case, analyze:

1. Trigger: what prompted recognition of the pattern.
2. Articulation: how the participant verbally frames the critique.
3. Action: whether the participant redirects prompts, rewrites independently, or sets anti-default constraints.
4. Consequence: how final text choices differ from prior AI-led trajectories.

**Step 3: Classify stance strength (possible, developing, explicit).**

- **Possible:** implicit resistance with limited metalinguistic naming.
- **Developing:** intermittent naming of AI defaults and partial strategic redirection.
- **Explicit:** clear, sustained critique of AI patterning plus deliberate stylistic counter-moves.

This classification is interpretive and should be justified with transcript evidence rather than inferred from final poem quality alone.

### Coding Outputs and Audit Trail

To ensure transparency, each session will produce four linked outputs:

1. Turn-category sheet (Part 1).
2. Feature matrix with `Present/Partial/Absent` ratings (Part 2).
3. Difficult-to-elicit case memo(s) with conversation timelines (Part 3).
4. Critical-relational case memo(s) with stance-strength classification (Part 4).

All coding changes should be logged with date, coder initials, and a one-line reason for recoding decisions.
