# Review report: Talk, Check, Decide: A Skill-Based Workflow for Writing and Verifying Geological Excursion Reports with an AI Assistant

| Field | Value |
|---|---|
| Manuscript | Stefan Mohr, Talk, Check, Decide: A Skill-Based Workflow for Writing and Verifying Geological Excursion Reports with an AI Assistant; manuscript without DOI or journal identifier in the file |
| Checked version | Talk_Check_Decide_A_Skill-Based_Workflow.pdf, 25 pages, SHA-256 f8190be6c06586eb5068aee0c70760a5413a6378ea291cf7e89bed2cf10b415e |
| Date | 2026-10-16 |
| Language | English |
| Review instances | Segments 1 to 4, figures, study design; the six review instances ran as separate agents, each without context from the session or from the other instances; merge, overall assessment and format check by a further separate agent; no instance omitted |
| Note | Manuscript and review were produced with the same model family: the manuscript names Claude (Claude Opus 5, later Claude Opus 5.5) as the assistant that drafted and checked it (p. 11, l. 203 to 206), and this review was produced with Claude Opus 5.5. The review is therefore a check by the same model family. |

## Summary

The manuscript is a retrospective case report, written by the developer of the method, on a workflow in which an AI assistant (Claude, first Claude Opus 5 and later Claude Opus 5.5) writes and checks geological excursion reports under 20 written procedures ("skills") and two project templates, while the author works largely by voice and confirms the assistant's proposals before they are inserted. The workflow is shown on two reports by one author: a post-trip report on 20 localities in Germany (about 55,000 words, 226 references in version v15) and a pre-trip field guide on 21 localities in southern Norway and Denmark (about 42,000 words, version v100). Six review axes are kept apart: genre, fact support, internal consistency, reference accuracy, locality evidence and usefulness. The key counts are seven consistency runs on the Norway report with 18, 4, 6, 4, 0, 2 and 71 findings; 13 errors among 211 reference entries of the Germany report (about 6 %); 26 proposals from a check of 55 Mindat citations, carried out in 22 changes; 36 sourced statements in a chapter fact check (18 verified, 14 partly verified, 3 not checkable, 1 misattributed); 43 template rules, each naming the incident it came from; 75 wording proposals for the paper itself; and three documented cases in which one axis alone found an error. Three research questions ask where the assistant helps and falls short, which errors AI assistance introduces and which checks catch them, and whether an iterative approach supports building the skills and improves the reports. The study has no comparison condition, which it states for RQ3.

## Strengths

1. Repeated quantities are kept consistent across the paper: the run sequence, 13 of 211, 31 + 12 = 43, 68 + 6 + 1 = 75, 32 of 117, "one entry in eight" and 20 skills with two templates agree between Abstract, text, tables and figures, and all sums close within rounding (PP-32, PP-33, PP-48, PP-27). This is what the paper's rules of recounting after every write and of a register of repeated statements aim at; the checks show the consistency, not that these rules produced it.
2. The figures carry exactly the values the text states: the bars of Figure 5 measure within 0.2 of their labels and of the text, every colour matches its legend field except the arrows of Figure 1, and the eight steps of Figure 2 and the roles in Figures 3 and 4 follow the method text in wording and order (PP-41, PP-05, PP-07, PP-26). A reader can take the numbers from either place.
3. The reference apparatus is complete in both directions: each of the 74 entries is cited and each citation has an entry, with years, spellings and the suffixes 2026a and 2026b consistent, and most numerical values taken from the literature agree with their sources (PP-45, PP-47, PP-09, PP-14, PP-18). This matters for a paper whose first named risk is fabricated and wrong references; the exceptions are the cited statements in GB-08 and GB-09.
4. Limits are disclosed at the claim they limit in most places, with hedged verbs: "the share was not measured" (l. 156), "indicated ... but not shown" (l. 284), "how often each type occurred or was missed was not counted" (l. 286 to 287), the 32 of 117 statements resting on a summary only (l. 199 to 200), and unrecorded dates and versions (l. 232, l. 255) (PP-53, PP-51). A reader can see which statements rest on counts and which on the author's view; the findings concern the places where the consequences of these limits are not drawn (GB-26, GB-43).

## Weaknesses

1. The answers to RQ1 and RQ2 go beyond what was measured: the ranking of checking "above all" has no measure of help in research, elicitation or writing, the errors are neither traced to their origin nor shown to have escaped axes that ran over the same text, and dictation is named as a gap without a question or measure (GB-42, GB-43, GB-01). Suggestion: report the outcomes of the 75 wording proposals and a table of axis by error class with origin on one fixed text, or restate both answers as the author's experience.
2. The evidence for RQ3 does not test the effect it is offered for: that all 43 template rules name their incident follows from the template convention, and the falling consistency counts are confounded by changing scope, by suppression through carried-forward non-findings and by a changing checker, with "large change" undefined (GB-44, GB-26, GB-27, GB-29). Suggestion: count recurrences of each rule's error class before and after the rule was written, and give per run the scope, size, skill version, model and carried-forward non-findings, or rerun one check on archived versions.
3. The workflow described as the method largely postdates the results it is credited with: the wording proposal began on 26 September 2026 and the skills are fixed at 27 and 28 September, while seven of eight dated results lie before 26 September, and no run is tied to a skill version or model (GB-17, GB-51, GB-21, GB-18). Suggestion: add a table of every reported run with date, report version, skill version or commit and model, and state the scope of the confirmation in the Abstract and Conclusions.
4. Many reported counts cannot be checked or rebuilt: the records behind them are not published and not fully listed, each axis ran on one report only, and breakdowns and units are incomplete in the reference, museum, Mindat, usefulness and genre results; several values cited in Related work differ from their sources (GB-54, GB-25, GB-23, GB-32, GB-31, GB-35, GB-38, GB-37, GB-13, GB-08, GB-09, GB-11). Suggestion: publish the check reports and log extracts behind each count, mark each count with its record class, give complete breakdowns per check, and correct the cited values against their sources.

## Findings by segment

### Segment 1: Abstract, introduction, related work (p. 1 to 4)

#### Substantive findings

**GB-01 Dictation is named as a research gap and carries the title, but no research question, instrument or result follows it.**

| Field | Content |
|---|---|
| Check | P10 |
| Location | p. 1, l. 1 and l. 10; p. 4, l. 83 to 85; p. 8, l. 155 to 156; p. 15, l. 300 to 304 |
| Quotation | "found no study ... on dictation as a way of writing them"; "the share was not measured" |
| Concern | The Gap paragraph names two gaps; RQ1 to RQ3 take up only the first. For dictation the chain stops after the gap: no question asks about it, no instrument measures it, Section 4 has no result on it, and the discussion rests on the author's experience (l. 300). The paper discloses that the share and the effect were not measured; the consequence for the frame (title "Talk", abstract l. 10) is not drawn. |
| Suggestion | Either add a research question on dictation and a measure (share of dictated inputs from the chat record; corrections after read-back per input), or remove dictation from the Gap paragraph (l. 84 to 85) and describe it in 3.2 as a working condition, not a subject of the study. |
| Status | verified |
| Severity | moderate |
| Source | SD |

**GB-02 The orange return arrow in the graphical abstract is not explained in its legend.**

| Field | Content |
|---|---|
| Check | P29 |
| Location | Graphical abstract, top edge between box 3 (AUTHOR, "confirms, changes or rejects") and box 2 (AI, "researches, proposes full wording"); caption p. 2, l. 21 to 24 |
| Quotation | "the author confirms, changes or rejects it; the assistant inserts it unchanged, logs the change and recounts"; "Orange marks the author, blue the assistant." |
| Concern | The caption explains the five boxes in reading order and the colour of the boxes. The figure also contains a sixth element: an arrow that leaves the top of the AUTHOR box "confirms, changes or rejects" and points back to the top of the AI box "researches, proposes full wording" (arrowhead at the AI box). Its colour measures #dc5c2c, identical to the AUTHOR header (#dc5c2c). The caption describes only the straight path to "inserts unchanged", so a reader of the abstract alone does not learn that a change or rejection sends the proposal back for a new proposal. Section 3.2 describes exactly this path ("when the author added to a proposal, the extended version was proposed again rather than worked in silently", l. 141 to 142), so the arrow is correct but unexplained where it is shown. |
| Suggestion | Add to the graphical abstract caption (p. 2, l. 22) a clause such as "a change or rejection returns the proposal to the assistant for a new proposal (upper arrow)", or label the arrow in the figure. |
| Status | verified (arrow and colour measured on the page image; absence of an explanation in the caption checked in l. 21 to 24) |
| Severity | minor |
| Source | AB |

**GB-03 The graphical abstract is not referred to anywhere in the text.**

| Field | Content |
|---|---|
| Check | P29 |
| Location | Graphical abstract, p. 2, l. 21 to 24; whole text |
| Quotation | "Graphical abstract. The workflow in brief: the author dictates raw input; the assistant, working under 20 written skills, researches and proposes the full wording" |
| Concern | Figures 1 to 6 are each cited in the text of their section (l. 108, 122, 158, 161, 214 and 331, 261). A case-insensitive search of text.json for "graphical" finds the caption itself (p. 2) and the journal name "International Journal of Geographical Information Science" in the references (p. 24), nothing else; no section points the reader to it, although section 3.2 describes the same cycle in more steps (Figure 2). Many journals treat a graphical abstract as standing outside the text; if that applies here, it is a matter of the journal's convention, which the manuscript does not state. |
| Suggestion | Either cite the graphical abstract once, for example at the end of the first paragraph of section 3.2 (l. 104) or in the Introduction (l. 38, "It describes the workflow"), or confirm that the target journal does not cite graphical abstracts in the text. |
| Status | verified (absence of a citation searched in text.json and confirmed on pages 2, 5 to 9); convention of the target journal: assumption |
| Severity | minor |
| Source | AB |

**GB-04 The guidebook guidelines do not ask for coordinates for each stop; they list them as one of several ways to make a trip repeatable.**

| Field | Content |
|---|---|
| Check | P13 |
| Location | p. 2, l. 27 to 28 |
| Quotation | "Guidance for field trip guidebooks therefore asks for enough information to repeat the trip, including coordinates for each stop (Geoscience Information Society, 2018)" |
| Concern | The first half is supported: "Sufficient information necessary to replicate the trip should be included." The second half overstates it: the guideline continues "This may be in the form of a road log with mileage between stops, GPS coordinates at each stop, or any other method that enables trip replication." Coordinates are an option, not a requirement. Graded minor: wording of a cited statement. |
| Suggestion | In p. 2, l. 28, replace "including coordinates for each stop" with "for example a road log or GPS coordinates for each stop". |
| Status | verified (geoinfo.org PDF) |
| Severity | minor |
| Source | S1 |

**GB-05 A benchmark on whether agent skills help, and whether models can write their own, is missing, although RQ3 and the method rest on skills drafted by the assistant.**

| Field | Content |
|---|---|
| Check | P14 |
| Location | p. 2, l. 36 to 38 (RQ3); p. 5, l. 103 to 106; p. 16, l. 323 to 331 |
| Quotation | "In this sense, AI was used to set up the use of AI: the assistant that did the work also analysed its records and revised the skills that steer it, and the author approved or edited them." |
| Concern | The manuscript states openly that whether the skills improved the reports is "indicated ... but not shown" (p. 15, l. 283 to 285). Related work has no section on skills as a technique. Li et al. (2026) test exactly this kind of written procedure (Agent Skills) on 86 tasks in 11 domains with 7,308 trajectories: curated skills raised the average pass rate from 24.3 % to 40.6 % (+16.2 percentage points), while self-generated skills gave no average benefit (about -1.3 points), and the authors conclude that effective skills need human-curated domain expertise. This both supports the manuscript's design choice (author approval of every skill change) and limits it: skills drafted by the assistant are not beneficial by default, so the author's control is the factor that RQ3 would have to isolate. Graded moderate: positioning of RQ3 against directly relevant evidence; the answer to RQ3 as stated stays, since the manuscript already calls the effect unshown. |
| Suggestion | Add a paragraph "Skills and procedural knowledge" to section 2 (after p. 4, l. 82) citing: Li, X., Chen, W., Liu, Y. et al. (2026) 'SkillsBench: Benchmarking how well agent skills work across diverse tasks', arXiv, 2602.12670. https://doi.org/10.48550/arXiv.2602.12670; and refer to it in the discussion of RQ3 (p. 15, l. 281 to 285) and of iterative skill development (p. 16, l. 323 to 331). |
| Status | verified (arXiv HTML full text, abstract and results); DOI form inferred from the arXiv identifier |
| Severity | moderate |
| Source | S1 |

**GB-06 For Güneş, Cesur and Çamur (2026), only the fully accurate rate of the weaker Claude model is given, without the values that place it.**

| Field | Content |
|---|---|
| Check | P13 |
| Location | p. 3, l. 44 to 46 |
| Quotation | "and only 59.6 % of the references from Claude 3 Opus were fully accurate (Güneş, Cesur and Çamur, 2026)" |
| Concern | The fabrication values are reproduced correctly (Claude 3.5 Sonnet 3.1 %, Claude 3 Opus 18.3 %, ChatGPT o1-preview, ChatGPT-4o, ChatGPT-4o with canvas and Gemini 1.5 Pro 27.7 to 60.6 %). For full accuracy, however, the study reports 80.8 % for Claude 3.5 Sonnet and below 8 % for the four OpenAI and Google models (5.6 to 7.3 % for ChatGPT, 2.7 % for Gemini). "Only 59.6 %" picks the middle value and leaves out both ends, so the reader cannot see how widely the models differ, which is the point of the preceding sentence ("they differ widely"). Graded minor: presentation of a cited result. |
| Suggestion | In p. 3, l. 45 to 46, give the full range, e.g. "and fully accurate references ranged from 80.8 % (Claude 3.5 Sonnet) and 59.6 % (Claude 3 Opus) to below 8 % for the other four models". |
| Status | verified (dirjournal.org article page) |
| Severity | minor |
| Source | S1 |

**GB-07 The fabrication rate of Claude Opus 4.8 is given over all prompts, including the 52.1 % it declined, and so reads lower than the rate of Opus 4.6.**

| Field | Content |
|---|---|
| Check | P13 |
| Location | p. 3, l. 46 to 48 |
| Quotation | "Claude Opus 4.6 fabricated 18.5 % and gave fully correct references in 54.6 %, while Claude Opus 4.8 fabricated 10.2 % but declined about half of the requests (Topaz et al., 2026a, preprint)" |
| Concern | The manuscript does name the declines, which is to its credit. The abstract of Topaz et al. (2026a) gives "Fabrication ranged from 10.2% (Claude Opus 4.8, which declined 52.1% of prompts)", so 10.2 % is unconditional. Over the prompts Opus 4.8 actually answered, the rate is 10.2 / (1 - 0.521) = 21.3 %, higher than the 18.5 % given for Opus 4.6. The sentence, built on "while ... fabricated 10.2 %", invites the reading that the later model fabricates less. The value 18.5 % for Opus 4.6 is not in the abstract (it gives 77.6 % verifiable references and 54.6 % fully correct responses); the full text could not be read. Whether Opus 4.6 declined prompts, which would change its conditional rate too, could not be checked. Graded minor: presentation of a cited value; the argument that models still fabricate is unaffected. |
| Suggestion | In p. 3, l. 47 to 48, give both rates, e.g. "Claude Opus 4.8 fabricated 10.2 % of all responses but declined 52.1 % of the prompts, so that about one in five of its answered prompts was fabricated", and check 18.5 % against the full text. |
| Status | verified (10.2 % and 52.1 %, 54.6 %, 55.4 % in the abstract via chatpaper.com); inferred (21.3 %, Python); inferred (18.5 %, full text not readable) |
| Severity | minor |
| Source | S1 |

**GB-08 The figure of about 30 % unsupported statements for GPT-4o is attributed jointly to Gao et al. (2023), which does not evaluate GPT-4o.**

| Field | Content |
|---|---|
| Check | P13 |
| Location | p. 3, l. 50 to 51 |
| Quotation | "even with retrieval, about 30 % of the statements made by GPT-4o were not supported by the sources it cited (Gao et al., 2023; Wu et al., 2025)" |
| Concern | The value is correctly taken from Wu et al. (2025), whose abstract states "Even for GPT-4o with Web Search, approximately 30% of individual statements are unsupported". Gao et al. (2023), the ALCE benchmark (EMNLP 2023, arXiv 2305.14627 of May 2023), does not mention GPT-4o on its landing page; its headline result is that "even the best models lack complete citation support 50% of the time" on ELI5. A reader who looks up Gao et al. for the GPT-4o figure will not find it. The manuscript uses Gao et al. correctly later, for the general point that retrieval leaves citation support incomplete (p. 15, l. 290 to 291). Graded moderate: the reader cannot trace the number to one of the two cited sources. |
| Suggestion | In p. 3, l. 51, cite only Wu et al. (2025) for the GPT-4o figure; if Gao et al. is kept here, give its own result in its own clause, e.g. "and on the ALCE benchmark even the best models lacked complete citation support about half of the time (Gao et al., 2023)". |
| Status | verified (Wu et al. 2025 abstract, Nature Communications page; Gao et al. 2023, ACL Anthology page) |
| Severity | moderate |
| Source | S1 |

**GB-09 The rates for Wolniewicz (2024) compare two different categories, and the editing judgement did not rest on field checks.**

| Field | Content |
|---|---|
| Check | P13 |
| Location | p. 3, l. 65 to 67 |
| Quotation | "found that 44.8 % of the Polish and 1.3 % of the English texts needed editing after manual and field checks (Wolniewicz, 2024)" |
| Concern | The manuscript calls this "The closest work to the present one", so its result matters for positioning. In the source (299 short introductions generated with Llama 3), 44.8 % is the share of Polish texts "marked as requiring additional editing effort" (134/299), whereas 1.3 % is the share of English texts "marked as demanding a significant improvement" (4/299). The like-for-like category, texts with incorrect or easily misread content, is 3.3 % Polish (10/299) and 3.0 % English (9/299). The source gives no English figure for "additional editing effort". Read as the manuscript gives it, the ratio is 44.8 / 1.3 = 34.5; on the comparable category the two languages are almost equal. The text quality was judged by manual scanning of the LLM output (section 3.3 of the source); field work was used to filter sites (123 of 299 removed), not to grade the wording. Graded moderate: misstates the result of the work the manuscript names as closest, so the reader cannot judge the positioning; the paper's own results are not affected. |
| Suggestion | Rewrite p. 3, l. 66 to 67, e.g. "found that 3.3 % of the Polish and 3.0 % of the English short descriptions contained incorrect or misleading content, and that 44.8 % of the Polish ones needed further editing, after a manual check of the output (Wolniewicz, 2024)". |
| Status | verified (MDPI full text, section 3.3 and results); ratio inferred (Python: 134/299 = 0.448, 4/299 = 0.013, 10/299 = 0.033, 9/299 = 0.030) |
| Severity | moderate |
| Source | S1 |

**GB-10 Work on LLM-assisted writing with speech is missing from the section on speech and from the gap statement.**

| Field | Content |
|---|---|
| Check | P14 |
| Location | p. 3 to 4, l. 72 to 78; p. 4, l. 84 to 85; p. 15, l. 300 to 304 |
| Quotation | "Speech input is about three times faster than typing on a phone (Ruan et al., 2018)."; "or on dictation as a way of writing them" |
| Concern | The speech paragraph draws on text entry speed, survey answers, clinical dictation and knowledge elicitation, but not on the setting the manuscript actually uses: speaking to a language model that turns speech into text. Yang et al. (2025) report a ten-day diary study in which twelve academic and creative writers wrote with Rambler, an LLM-assisted dictation tool; they describe strategies (dictating an outline and expanding it, or speaking freely and restructuring), benefits (speed, reduced overthinking, self-efficacy, language learning) and problems (precise editing, multitasking with research, noisy environments). This is the closest evidence for the manuscript's own observations on speaking (p. 8, l. 155 to 161; p. 15, l. 300 to 307) and for the role of the language barrier (p. 15, l. 308 to 316). It does not concern excursion reports, so it does not refute the gap, but it narrows the novelty of the dictation half. Graded moderate: positioning of a central element of the workflow; results unaffected. |
| Suggestion | In p. 4 after l. 76, add: Yang, X., Li, W., Lee, M.G., Li, Z., Zamfirescu-Pereira, J.D. and Liu, C. (2025) 'Rambler in the wild: a diary study of LLM-assisted writing with speech', in Extended Abstracts of the CHI Conference on Human Factors in Computing Systems (CHI EA '25). New York: ACM. https://doi.org/10.1145/3706599.3706676; optionally also the system paper it builds on, Lin, S. et al. (2024) 'Rambler: supporting writing with speech via LLM-assisted gist manipulation', CHI '24. https://doi.org/10.1145/3613904.3642217; and set the discussion in p. 15, l. 300 to 304 against both. |
| Status | verified (Yang et al. 2025, arXiv HTML full text); inferred (Lin et al. 2024, bibliographic data taken from Yang et al.'s reference list, not read) |
| Severity | moderate |
| Source | S1 |

**GB-11 Revilla et al. (2020) is reported only against recorded speech, although its abstract places dictation below typed text as well.**

| Field | Content |
|---|---|
| Check | P13 |
| Location | p. 4, l. 74 to 75; also p. 15, l. 301 to 304 |
| Quotation | "although plain dictation into text gave less detail than recorded speech (Revilla et al., 2020; Revilla and Couper, 2026)"; p. 15: "Whether this closes the gap between dictation and recorded speech was not measured." |
| Concern | The manuscript openly states that plain dictation underperformed recorded speech, which is a fair point to make. The source abstract says more: "Among those who provided an answer, when dictation was used, we found fewer valid answers and less information provided", with control groups that used "standard text entry" and with nonresponse given "relative to text input". The comparison omitted is the one most relevant to a workflow built on dictation: dictation gave less than typing, not only less than recording. The discussion therefore frames the open question only as the gap to recorded speech (p. 15, l. 303 to 304), not as the gap to typed input. For Revilla and Couper (2026) the fetched abstract does not separate dictation from recording. Graded moderate: the omitted comparison changes how the cited evidence bears on the manuscript's dictation claims; the results of the paper stand. |
| Suggestion | In p. 4, l. 74 to 75, add the comparison with typed answers, e.g. "although dictation into text gave fewer valid answers and less information than typed text, while recorded speech gave longer answers (Revilla et al., 2020)", and in p. 15, l. 303 to 304 name both gaps (to typed and to recorded answers) as unmeasured. Check whether Revilla and Couper (2026) supports the clause on its own, or move it. |
| Status | verified ("fewer valid answers and less information" for dictation, ISR Michigan abstract page); inferred (that typed text is the baseline, from the abstract's control design and the nonresponse sentence); assumption for Revilla and Couper (2026), full text not read |
| Severity | moderate |
| Source | S1 |

**GB-12 The gap statement names the number of queries and tools, but not the search terms, the date of the search or the subject database of the geosciences.**

| Field | Content |
|---|---|
| Check | P28 |
| Location | p. 4, l. 83 to 85 |
| Quotation | "A search of 24 queries in English and German, by web search and a partial Crossref search, without Scopus or Web of Science, found no study on using a language model to write or check geological excursion reports, or on dictation as a way of writing them." |
| Concern | The manuscript is more open than many about its search: it gives the number of queries, the languages, the tools and the databases it did not use. Still missing are (a) the search terms, (b) the date or period of the search, (c) what "partial" Crossref search means (which fields, which subset), and (d) any mention of GeoRef, the bibliographic database of the geosciences, or of Google Scholar; the omission of Scopus and Web of Science is stated but not justified. Without the terms, a reader cannot repeat the search. Three own queries (Verification log PP-20) found no peer-reviewed study on LLM-written or LLM-checked excursion reports, so the claim is not refuted; but work on LLM-assisted writing by speech exists outside geology (GB-10), and the manuscript itself cites speech recognition for geological field data (Zhang et al., 2020, p. 4, l. 76 to 77), which borders on the dictation half of the claim. Graded moderate: the gap claim cannot be checked or repeated; it is not shown to be false. |
| Suggestion | In p. 4, l. 83 to 85, or in a supplement referenced there, list the 24 queries, the date of the search, the Crossref fields searched, and either add GeoRef (and Google Scholar) or state why they were not used; narrow the dictation half of the claim to "dictation as a way of writing them with a language model" and set it against Zhang et al. (2020). |
| Status | verified (wording on the page image); inferred (no counterexample in three queries) |
| Severity | moderate |
| Source | S1 |

#### Minor corrections

| ID | Location | Quotation | Replacement | Source |
|---|---|---|---|---|
| KK-01 | p. 2, Graphical abstract, title line inside the figure | "Talk, Check, Decide: AI-assisted scientific geological excursion reports" | "Talk, Check, Decide: a skill-based workflow for geological excursion reports with an AI assistant", matching the title on p. 1, l. 1 to 2 | AB |
| KK-02 | p. 3, l. 44 to 45 | "Claude 3 Opus 18.3" at the end of l. 44 and "%, against" at the start of l. 45 (page image) | "Claude 3 Opus 18.3 %, against", with a non-breaking space between number and percent sign | S1, S3, S4 |

#### Verification log

| ID | Check | Checked | Values | Result |
|---|---|---|---|---|
| PP-01 | P6 | "In three documented cases, an error was caught by one axis only" (l. 15) against l. 286 to 290 | misplaced age (consistency), writer's conclusion (fact support), neighbouring DOI (reference accuracy): 3 | no finding on the count; inference "invisible to both" see GB-43 |
| PP-02 | P3, P29 | List of figures with page, type, caption and every citation in the text, confirmed at the printed margin numbers | Graphical abstract: p. 2, schema with icons, caption l. 21 to 24, no citation in the text. Figure 1 "Iterative skill development": p. 6, flow diagram, caption l. 118 to 121, cited l. 108. Figure 2 "Human in the loop": p. 8, cycle diagram, caption l. 151 to 154, cited l. 122. Figure 3 "Division of labour between author and AI assistant": p. 9, two-box schema, caption l. 163 to 165, cited l. 158. Figure 4 "Speaking with read-back": p. 9, flow diagram, caption two lines between margin numbers 165 and 170 (exact lines uncertain), cited l. 161. Figure 5 "Findings and documented non-findings in the seven consistency runs of the Norway report": p. 12, grouped bar chart with axis, caption l. 220 to 223, cited l. 214 and l. 331. Figure 6 "Failures and the rules they produced": p. 14, table-like schema, caption l. 267 to 269, cited l. 261. Embedded images (pdfimages): 7, all raster, 200 ppi (graphical abstract 211 ppi), Figure 2 JPEG. Tables 1, 2 and A1 are set as text, not as images. | no finding for numbering: Figures 1 to 6 are numbered consecutively and first cited in that order (l. 108, 122, 158, 161, 214, 261); every citation hits the figure it describes. Graphical abstract without citation: GB-03. |
| PP-03 | P29 | Legends, axes, abbreviations and panels of every figure | Graphical abstract: box colours explained in caption ("Orange marks the author, blue the assistant"), axes none, panels none, "AI" in the boxes is the "assistant" of the caption. Figure 1: in-figure legend Author and AI assistant; arrow colours not explained (GB-15). Figure 2: in-figure legend Author, AI assistant, Either; dashed arrow labelled "next task". Figure 3: box colours in caption, arrow labels in the figure. Figure 4: in-figure legend Author, AI assistant, Tool; dashed arrow labelled "correction: speak again". Figure 5: legend Findings and Documented non-findings, y-axis "Count per run" (unit counts), x-axis categories Run 1 to Run 7 with versions; no axis title on the x-axis, which needs none as categories are labelled. Figure 6: no legend, grey and white boxes explained in caption l. 267 to 268. No figure has panels a, b, c. Abbreviations "v17" to "v100" are versions, explained in caption l. 221 to 222. | no finding apart from GB-02, GB-15 and GB-30 |
| PP-04 | P29 | Type size in print size, smallest word of each kind, cap height at half intensity in the 300 dpi render | Graphical abstract "20 skills" digits 25 px = 8.3 pt (other labels larger). Figure 1 in-figure note "Structural analogy ...", letter N of "No": 19.3 px = 6.4 pt (component at threshold 167: 20 px = 6.7 pt; at threshold 128: 17 to 18 px = 5.7 to 6.0 pt). Figure 2 note "Exception: ...", letter E: 20 px = 6.7 pt; legend "Either" larger. Figure 3 box text larger than 8 pt (x-height 20 px). Figure 4 legend "Tool", letter T: 21 px = 7.0 pt; box text A: 23 px = 7.7 pt. Figure 5 tick label "80": 23 px = 7.7 pt; "Run 1": 23 px = 7.7 pt; row "Change before run", letter C and digits "21": 20 px = 6.7 pt. Figure 6 monospace skill names (lowercase only): ascender of l 19 px, scaled to cap height by 0.729/0.76 gives 18.2 px = 6.1 pt; x-height 14 px × 1.33 gives 18.6 px = 6.2 pt; box text A: 22 px = 7.3 pt. Method uncertainty ±0.6 pt (messverfahren, section 8); the figures are upsampled from 200 ppi to 300 dpi. | no finding: no measured size below 6 pt; the in-figure note of Figure 1 and the skill names in Figure 6 lie at the limit (about 6.1 to 6.4 pt) |
| PP-05 | P3 | Colours against legend fields, `messen.py farben` and mean RGB of 80 px samples | Figure 5: legend Findings #2c7cd4, all six blue bars #2c7cd4; legend non-findings #1cac7c, all seven green bars #1cac7c (difference 0). Figure 2: legend Author 254, 233, 226 against step 5 252, 235, 227 (difference 5); legend AI assistant 231, 239, 254 against steps 2, 3, 4, 6, 7 each 233, 239, 251 (difference 5); legend Either 242, 242, 240 against steps 1 and 8 242, 242, 240 (difference 0). Figure 1: three author boxes and legend 252, 235, 226; five assistant boxes and legend 232, 241, 251. Figure 3: author box 252, 235, 226, assistant box 232, 241, 251. Figure 4: Author speaks and Author confirms 252, 235, 226 (legend same); Assistant restates and Written record 232, 241, 251 (legend same); Speech recognition 255, 255, 255 (legend Tool same). Graphical abstract: AUTHOR headers and return arrow #dc5c2c. | no finding apart from the arrow colours of Figure 1 (GB-15) |
| PP-06 | P3 | Counts of elements against caption and text, counted on enlarged crops | Graphical abstract: 5 workflow boxes (3 AUTHOR, 2 AI) and 6 review axes, against six axes in caption l. 23, l. 11 to 12 and Table 2 (6 rows). Figure 2: 8 steps against "eight steps" (l. 122, caption l. 151); colours 5 blue (2, 3, 4, 6, 7), 1 orange (5), 2 grey (1, 8) against caption l. 152 to 154 ("the assistant enters, researches, proposes, applies and verifies; locating a task and presenting the result fall to either"). Figure 5: 6 blue bars plus a label 0, 7 green bars (flecken: 6 and 7 bars plus legend field each). Figure 6: 6 rows; carrying skills template-dokumentprojekt 2, science-quellenapparat-pruefung 3, science-arbeitsplan-erstellen 1, against caption l. 269 and text l. 262 to 263 ("two ... by the document template, three by the reference check and one by the work plan skill"). | no finding |
| PP-07 | P3 | Content of each figure against its caption and the text | Graphical abstract against abstract l. 16 to 17 and l. 8 to 9 ("20 written procedures"; "20 skills" in the figure). Figure 1 against l. 105 to 108: analyse actions, draft step by step, consistency checks and critique, judged by next review round; in-figure note on the analogy agrees with l. 121 and l. 325 to 327. Figure 2 against l. 122 to 126: eight steps in the same order and wording, exception for mechanical corrections and released classes in figure and l. 125 to 126. Figure 3 against l. 155 to 158 and the caption. Figure 4 against l. 158 to 161: "slips, misrecognised words, late corrections, pauses and revocations" against "Slips of the tongue, misrecognised words, corrections several sentences later, pauses and even revoking a statement"; sorting into "observation, estimate, interpretation, hearsay" against l. 303. Figure 6 against l. 261 to 265: rows 1 and 3 are the two error classes named there. Satz and residues: no placeholder, watermark, template remnant or cut-off label found on pp. 2, 6, 8, 9, 12, 14. | no finding apart from GB-16 and GB-47 |
| PP-08 | P14 | Contribution in one sentence: a human-in-the-loop, voice-driven workflow in which an AI assistant works under written skills and separate review axes to write and check geological excursion reports. Six queries: (1) large language model geological field trip guide writing evaluation; (2) ChatGPT geoheritage geosite descriptions generated accuracy evaluation; (3) human-in-the-loop LLM scientific writing workflow citation verification agents hallucinated references pipeline; (4) Agent Skills procedural knowledge files LLM agents SKILL.md study evaluation; (5) voice dictation large language model assistant writing scientific paper workflow case study author confirms; (6) generative AI field guide geotourism virtual guide geology accuracy errors locality | Kept: Li et al. 2026 (GB-05), Yang et al. 2025 (GB-10). Rejected as same field only: GeoGalactica (arXiv 2401.00434), CiteAudit (arXiv 2602.23452). Already in the list: Deng et al. 2024 (K2), Wolniewicz 2024, Baucon and Neto de Carvalho 2024. All kept candidates checked against the reference list (p. 19 to 25): absent | two findings |
| PP-09 | P13 | Walters and Wilder (2023), p. 3, l. 42 to 43 | Source: 55 % GPT-3.5 and 18 % GPT-4 citations fabricated; 43 % and 24 % of real citations with substantive errors | no finding |
| PP-10 | P13 | Bhattacharyya et al. (2023); Chelli et al. (2024), p. 3, l. 48 to 49 ("similar or higher rates") | Chelli: hallucination 39.6 % (GPT-3.5), 28.6 % (GPT-4), 91.4 % (Bard); Bhattacharyya: 28 of 178 references (15.7 %) neither found nor with DOI, 69 of 178 without DOI | no finding; the reference point of "similar or higher" is left open, since the values just given range from 10.2 % to 55.4 % |
| PP-11 | P13 | Wu et al. (2025), p. 3, l. 50 to 51 | "approximately 30% of individual statements are unsupported" for GPT-4o with Web Search; nearly half of responses not fully supported | no finding for Wu; attribution to Gao see GB-08 |
| PP-12 | P13 | Rao, Wong and Callison-Burch (2026), p. 3, l. 51 to 52 | Deep research agents: openai-deepresearch 3.5 %, gemini-2.5-pro-deepresearch 13.3 % hallucinated URLs; over all ten models and agents 3 to 13 % | no finding |
| PP-13 | P13 | Topaz et al. (2026b), p. 3, l. 53 to 55 | Secondary reports (Retraction Watch, CASRAI): about 2.5 million PMC open-access papers, January 2023 to February 2026; papers with fabricated references 1 in 2,828 (2023), 1 in 458 (2025), 1 in 277 (first seven weeks of 2026). The Lancet letter itself not read | no finding; source read only through secondary reports |
| PP-14 | P13 | Todd et al. (2010), p. 3, l. 55 to 56 | Clearly supported 75.8 %, ambiguous 10.6 %, no support 6.0 %, empty 7.6 % | no finding |
| PP-15 | P28 | Other gap or novelty sentences in segment 1 ("no study", "first", "closest", "not been") | Only p. 3, l. 65 ("The closest work") and p. 4, l. 83 to 85; the first is covered by GB-09, the second by GB-12 | no further finding |
| PP-16 | P13 | Baucon and Neto de Carvalho (2024), p. 3, l. 67 to 68 | 152 questions; 79.6 % of answers at or above the passing mark of 5 of 10 | no finding |
| PP-17 | P13 | Peters and McClennen (2016), p. 3, l. 69 to 70 | Paper notes that collections vary in scope, about 75 % at outcrop scale or finer; sampling biases not discussed. Ralph et al. (2025) not read | no finding (joint citation, the bias part presumably rests on Ralph et al.) |
| PP-18 | P13 | Ruan et al. (2018), p. 3, l. 72 | English 2.93 times faster (153 vs 52 WPM), Mandarin 2.87 times (123 vs 43 WPM), transcription of given phrases | no finding |
| PP-19 | P13 | Höhne, Gavras and Claassen (2024); Lenzner, Höhne and Gavras (2024), p. 3 to 4, l. 73 to 74 | Lenzner: oral answers "about three times as many words" (43.82 vs 14.18; 41.19 vs 12.08), about 0.3 more themes in the first probe only; Höhne: more words and more topics, no multiplier given | no finding (shortening that does not change the statement) |
| PP-20 | P28 | Gap claim p. 4, l. 83 to 85; three own queries: (1) "excursion guide" OR "field trip guide" ChatGPT geology students generated evaluation; (2) Exkursionsbericht Geologie KI ChatGPT Sprachmodell Erstellung Studie; (3) GeoRef "large language model" fieldwork report writing geoscience education field course AI-generated report | No peer-reviewed study on LLM-written or LLM-checked geological excursion reports found; results were general geoscience LLMs, course pages, an EGU 2026 session on generative AI in geosciences and a non-peer-reviewed GitHub essay | gap not refuted; missing search details see GB-12 |

### Segment 2: Materials, methods, Appendix A (p. 4 to 11 and 18 to 19)

#### Substantive findings

**GB-13 Table 1 gives counts for the Norway project files but only file kinds for Germany, and the Germany files carry other names in the Data availability statement and Figure 6; did the Germany project keep a log, and is the "Germany organisation file" one of the files in Table 1?**

| Field | Content |
|---|---|
| Check | P11, P38 |
| Location | p. 4, Table 1, rows Size and Project files, columns Germany and Norway; p. 19, l. 390; p. 10, l. 194; p. 14, Figure 6, row 6, column "Failure"; p. 17, l. 363 to 364 |
| Quotation | "report, appendices, register of repeated statements, work plan, base data, locality table" and "27 files, among them a decision log with 130 entries, a log with 243 entries and a work plan with 132 steps in 21 blocks" |
| Concern | Table 1 compares the two cases, but in the row Project files the Germany column lists file kinds without any count, while the Norway column gives the number of files, of log and decision log entries and of work plan steps. In the row Size, Germany gives references but not appendices, Norway appendices but not references. The effort statement in the Limits ("243 log entries for a pre-trip field guide", l. 363 to 364) can therefore not be set against the post-trip case. The Germany column names neither a log nor a decision log, while the Data availability statement speaks of "logs" for both reports (l. 390) and section 3.4 of "the decision log" (l. 194) without naming the project. Figure 6 names a "Germany organisation file", which appears nowhere else in the manuscript; it may be one of the files in Table 1 under another name or a further file. |
| Suggestion | In Table 1 (p. 4), give the same quantities for both cases: number of files, log entries, decision log entries, work plan steps and blocks, references and appendices, each with version and date, or state per cell why a count does not exist. Use the same file names in Table 1, Figure 6 (p. 14, row 6) and the Data availability statement (p. 19, l. 390), and say in section 3.4 (l. 194) which project's decision log is meant. |
| Status | verified (page image of p. 4; the differing lists at the cited places); assumption (whether the organisation file is one of the Table 1 files, asked as a question) |
| Severity | moderate |
| Source | S2, S3 |

**GB-14 Several components are named by number but not described, so the checks cannot be rebuilt from the text.**

| Field | Content |
|---|---|
| Check | P8 |
| Location | p. 5, l. 100 to 101; p. 6, l. 124; p. 13, l. 249 to 252; p. 18, Table A1, rows science-interne-konsistenz-pruefung, geo-exkursionsbericht-erstellen, science-dokumentkritik-drei-sichten |
| Quotation | "the document against itself in six dimensions"; "met 9 of 11 obligations of an excursion report"; "the 15 types of the genre selection skill" |
| Concern | Named but not listed: the six dimensions of the consistency check, the 11 obligations of an excursion report and which 2 were missed, the 15 genre types and the four candidate genres (only the chosen one is named, l. 253), the 15 measures per perspective, the 12 groups of working patterns, and the full set of "metrics of the skills" (l. 124 gives three examples). All checks are judgement steps of a model; how a judgement is reached (for instance what counts as "partly verified", l. 230) is not stated. The skills are said to be published (p. 19, l. 387); the manuscript does not point to the place where each of these lists is found. The counts for the four candidate genres and the two unmet obligations are taken up in GB-37; this finding concerns the missing lists and definitions. |
| Suggestion | In 3.4 or Appendix A, list the six dimensions, the 11 obligations with the two not met, the four candidate genres, and the grading categories of fact support with their definitions; or give for each the file and section in the repository. |
| Status | verified (absence in the manuscript); whether the repository contains them was not checked |
| Severity | moderate |
| Source | SD |

**GB-15 Figure 1 uses three arrow colours, but its legend explains only the box colours.**

| Field | Content |
|---|---|
| Check | P29 |
| Location | Figure 1, all arrows; legend below the diagram; caption p. 6, l. 120 to 121 |
| Quotation | "Orange marks the author, blue the assistant."; legend fields "Author", "AI assistant" |
| Concern | Measured with `messen.py farben`: two arrows are orange (#dc5c2c), "AI runs consistency checks and critique" to "Author approves or edits the skill" and the arrow "what fails goes back into the skill"; one arrow is black (#1c1c1c), "apply"; the remaining four arrows are dark grey (#4c4c4c). The orange arrows match the author border colour (#dc6434; difference 0 + 8 + 8 = 16, below the threshold 40), so a reader will take them to mean "author", but the coding is not consistent with that: the arrow out of the author box "Author approves or edits the skill" ("apply") is black, the arrow out of "Author carries out the work himself" is grey, and the arrow into "Counted findings; author judges the result" is grey while the arrow into "Author approves or edits the skill" is orange. Caption and legend explain box fills only. Box fills measure 252, 235, 226 for all three author boxes and 232, 241, 251 for all five assistant boxes, identical to the legend fields. |
| Suggestion | Either draw all arrows in one colour, or state in the legend of Figure 1 what orange and black arrows mean (for example "orange: transition that needs the author's decision"), and apply that meaning to every arrow. |
| Status | verified (colours measured; meaning intended by the author: assumption, therefore offered as a question of which coding is meant) |
| Severity | minor |
| Source | AB |

**GB-16 The caption of Figure 1 says the feedback "closes the loop", while section 3.2 says the loop does not close.**

| Field | Content |
|---|---|
| Check | P3 |
| Location | Figure 1 caption, p. 6, l. 120; section 3.2, p. 5, l. 107 to 108 |
| Quotation | "What fails feeds back into the skill, which closes the loop."; "The loop does not close: every report is a practical test of the skills, and every change to a skill passes the author's control (Figure 1)." |
| Concern | The two sentences describe the same figure; the second ends with the citation of Figure 1. They use "close" in two senses: the caption means that the arrow "what fails goes back into the skill" completes a cycle, the text means that the process never ends. A reader comparing caption and text reads a contradiction. The figure itself agrees with both readings: the orange arrow from "Counted findings; author judges the result" back to "AI drafts or revises the skill step by step" completes the cycle, and nothing in the figure marks an end. |
| Suggestion | Change one of the two wordings, for example in the caption (l. 120) "What fails feeds back into the skill, so that the cycle starts again", or in the text (l. 107) "The loop does not end:". |
| Status | verified (both passages confirmed on the page images of pp. 5 and 6) |
| Severity | minor |
| Source | AB |

**GB-17 The workflow described as the method, with wording proposals, chat record and the skills in their state of 27 September, postdates nearly all dated results.**

| Field | Content |
|---|---|
| Check | P7, P30 |
| Location | p. 7, l. 136 to 138; p. 10, l. 181; p. 10, l. 198; p. 11, l. 215 to 217; p. 12, l. 229; p. 13, l. 237 and 249; p. 14, Fig. 6; p. 19, l. 383 to 386 |
| Quotation | "Since this procedure was introduced on 26 September 2026"; "the others are identified by name, in their state of 27 September 2026" |
| Concern | Appendix A fixes the skills at 27 and 28 September; the wording proposal procedure began on 26 September; the data window ends on 28 September. Of the eight dated results (Germany runs 13, 15, 19, 21 September, reference check 18 September, genre analysis 19 September, fact check 24 September, Norway second critique 26 September), seven lie before 26 September and all eight before 27 September (recalculated). For Norway, the records cover 19 days, of which 3 (15.8 %) fall from 26 September on. The seven Norway runs and the Mindat check are undated. The skills were revised after each round (l. 105 to 108), and the rules of Fig. 6 were written back after failures that are not dated, so it cannot be told which reported run ran under which rule; for example, whether the reference check of 18 September already compared first authors on the landing page (Fig. 6, row 3). The results are not separated by skill version. |
| Suggestion | In 3.5, add a table with every reported run: date, report version, skill and template version (or commit), model; in 4.6 and Fig. 6, date each failure and rule. State in 3.2 that the results in Section 4 arose under earlier forms of the skills and before the wording proposal procedure, and which of its elements (eight steps, confirmation) were in force then. |
| Status | verified (dates); inferred (share of days); assumption (skill content at the time of each run, not given) |
| Severity | major |
| Source | SD |

**GB-18 Does the traceability of each inserted sentence to the input that released it hold for proposals released among the 30 inputs whose wording was lost?**

| Field | Content |
|---|---|
| Check | P26, P17 |
| Location | p. 7, l. 142 to 147; p. 17, l. 352 to 353; p. 19, l. 384 to 385 |
| Quotation | "every sentence inserted in this way can be traced to its proposal and, from the tenth proposal on, also to the input that released it"; "of the first 30 inputs in the chat in which this paper was revised, only their order survived, because the chat had been summarised" |
| Concern | The chat record was added with template 1.5.0 on 27 September (l. 384 to 385), the wording proposal began on 26 September, and in the revision chat the wording of the first 30 inputs is lost. The guarantee says the release can be traced; for a release given among those inputs only its position survives, not whether it was "yes", "all" or "yes, unless" (l. 148 to 149). The loss is disclosed only in the discussion, not in 3.2 where the guarantee is made. |
| Suggestion | In 3.2 (l. 142 to 147), state how many of the 75 proposals were released by inputs whose wording survives, and move the note on the 30 lost inputs there. |
| Status | inferred (overlap of the two periods); assumption (whether any proposal from the tenth on falls among the lost inputs) |
| Severity | moderate |
| Source | SD |

**GB-19 A working note on the state of the proposals stands in the paper, against its own rule to keep working notes out of the deliverable.**

| Field | Content |
|---|---|
| Check | P18 |
| Location | p. 7, l. 144 to 145; against p. 10, l. 180 |
| Quotation | "75 by 28 September 2026, this one included" |
| Concern | "This one included" refers to the proposal that inserted the sentence, which a reader cannot see; the count is a running state. One of the eleven rules is "keep working notes out of the deliverable" (l. 180). |
| Suggestion | In p. 7, l. 144, replace "75 by 28 September 2026, this one included, of which" with "75 by 28 September 2026, of which". |
| Status | verified |
| Severity | minor |
| Source | SD |

**GB-20 The assistant is also called "the system" in eight places, without saying whether the term means the same object.**

| Field | Content |
|---|---|
| Check | P38 |
| Location | p. 8, l. 156, 158 (twice) and 160; p. 15, l. 300, 302 and 306; p. 17, l. 369; compare Figure 3 (p. 9, panel header "AI assistant") and its legend, p. 9, l. 163 to 165. |
| Quotation | "the system asked one question at a time, stated why it asked, and wrote the result into the files"; "the system kept the written record (Figure 3)"; "and the system writing, counting, checking and keeping the records" |
| Concern | Elsewhere the manuscript says "assistant" (40 occurrences in title, text and legends, counted with Python) or "AI assistant" (in the figures, the title and 5 places in the text). Line 158 points to Figure 3, whose panel is headed "AI assistant" and whose legend says "the assistant writes, counts, checks and keeps the records" (l. 164); l. 369 repeats the same four verbs for "the system". The roles are therefore the same. Figure 4, however, separates a speech recognition tool (white box) from the assistant, so "the system" could also be read as assistant plus speech recognition plus skills. The manuscript does not say which reading is meant. The phrase "A GPT-based geology system" (l. 67) is a different object and not part of this finding. |
| Suggestion | Replace "the system" with "the assistant" at the eight places, or define "the system" once in Section 3.2 (p. 8, l. 156) if it is meant to include speech recognition and skills. |
| Status | verified |
| Severity | minor |
| Source | S2 |

**GB-21 The working environment is incomplete: the speech recognition tool is not named, the model change is not dated, and 19 of 22 skills carry no version.**

| Field | Content |
|---|---|
| Check | P35 |
| Location | p. 9, Fig. 4, box "Speech recognition"; p. 11, l. 203 to 204; p. 19, l. 383 to 386 |
| Quotation | "first as Claude Opus 5 and later as Claude Opus 5.5"; "the others are identified by name, in their state of 27 September 2026" |
| Concern | The voice path, presented as central (title, abstract l. 10), passes through a speech recognition tool that is neither named nor described (device, language setting). The model change has no date, so runs cannot be assigned to a model. Which interface (chat or agent) ran which check is not said, though the Mindat second pass used "separate instances" (l. 246). Model settings that affect output are not given. Skills identified "by name, in their state" of a date after the results cannot be restored to the state of any earlier run. |
| Suggestion | In 3.5, name the speech recognition tool and its settings, the date of the model change, the interface per axis, and give a repository commit for the skill state of each run. |
| Status | verified |
| Severity | moderate |
| Source | SD |

**GB-22 The read-back of dictated input is said to catch slips, corrections and revocations, but its effect was not measured.**

| Field | Content |
|---|---|
| Check | P31 |
| Location | p. 9, Fig. 4 caption; p. 8, l. 158 to 160 |
| Quotation | "slips, corrections and revocations are caught because the assistant restates what it understood and the author confirms or corrects it" |
| Concern | The text limits the claim to "the author's experience" (l. 160); the figure caption states it as an effect. No count of read-backs, corrections after read-back or slips that passed is given, though the chat record would hold them. |
| Suggestion | In the caption of Fig. 4, write "are meant to be caught", or report from the chat record how many read-backs led to a correction. |
| Status | verified |
| Severity | minor |
| Source | SD |

**GB-23 Each review axis except consistency is reported for one report only; five of twelve cells of case and axis are empty without a reason, and the prescribed order of axes is reported as broken for the Germany report only.**

| Field | Content |
|---|---|
| Check | P11, P5 |
| Location | p. 10, l. 185 to 189; p. 1, l. 10 to 13; p. 11 to 13, sections 4.1 to 4.5; p. 12, Figure 5; p. 17, l. 362 to 363 |
| Quotation | "Six checks were kept separate because an axis can find errors the others miss (Table 2). Section 4 reports a counted result for each of them. The skills prescribe the order: genre first, then fact support and consistency, then usefulness, then a new consistency run" |
| Concern | The claim of l. 185 to 186 holds per axis. Built as a table of the two cases against the six axes, section 4 reports for Germany consistency (4.1), fact support (4.2), reference accuracy (4.3) and genre (4.5), and for Norway consistency (4.1), locality evidence (4.4) and usefulness (4.5). Empty are Germany locality evidence and usefulness, and Norway fact support, reference accuracy and genre: 5 of 12 cells. The method prescribes an order and says that reference accuracy and locality evidence "run at the latest before submission" (l. 188 to 189), which reads as if every axis was applied to each report. The deviation is disclosed for Germany ("the genre analysis came only after the first two consistency runs", l. 187 to 188). For Norway, no genre analysis and no fact check are reported, and the change before run 1 reads "first run, report only" (Figure 5). The Limits explain the genre cells only in part (l. 363). For the other empty cells it is not said whether the check was not run, was run without countable result, or was run after 28 September. The claim that an axis "can find errors the others miss" can be weighed only where axes ran on the same report (see GB-43). |
| Suggestion | Add to section 4 (or to Table 2) a table of case by axis giving per cell the date, version and counted result, or the reason the check was not run. In section 3.4, state for the Norway report which axes ran and in which order, and that the prescribed order was not followed there either. |
| Status | verified (sections 3.4 and 4.1 to 4.5; order for Germany); inferred (order for Norway, from the absence of reports and l. 362 to 363) |
| Severity | moderate |
| Source | S3, SD |

**GB-24 The six review axes appear under several names, and the Figure 6 legend names a skill only by a short form that Table 2 does not define.**

| Field | Content |
|---|---|
| Check | P38 |
| Location | Table 2, p. 10, column "Axis"; Abstract, p. 1, l. 12 and 14; Graphical abstract, p. 2, graphic (axis boxes) and legend l. 23; Section 3.4, p. 10, l. 187; Section 4.5, p. 13, l. 254; Section 4.6, p. 13, l. 262; Figure 6 legend, p. 14, l. 269 (by count) and column "Skill that carries the rule"; Section 5, p. 15, l. 287 to 289; Limits, p. 17, l. 363 to 365. |
| Quotation | "Fact support", "Internal consistency", "Reference accuracy", "Locality evidence", "Usefulness". Section 5: "The misplaced age was invisible to the fact check"; "only the consistency check found". Section 4.6: "three by the reference check and one by the work plan skill" |
| Concern | Table 2 fixes six axis names, and Sections 4.2 to 4.5 use them as headings. The same axes are also called: "fact check" (l. 287, l. 364 to 365) for fact support; "consistency check" (l. 288, 289) and "consistency run" (7 occurrences) for internal consistency; "reference check" (l. 14, 262, 269) for reference accuracy; "three-perspective critique" (l. 254) for usefulness; "genre analysis" (l. 187, 363) for genre; and in the graphical abstract "facts", "consistency", "references", "locality". In Section 4.6 and the Figure 6 legend, "reference check" stands for the skill science-quellenapparat-pruefung, which the figure itself names in its third column; the mapping can only be made through Table 2. Most short forms can be worked out, but none is introduced. In Section 3.2 "consistency checks" (l. 106, 119) also means checks applied to a skill, not to a report, so the same expression names two activities. |
| Suggestion | Add a column "Short name" to Table 2 (p. 10) or one sentence in Section 3.4 (l. 185) that fixes the short forms, and use the identifier from Figure 6 in its legend (p. 14, l. 269): "three by science-quellenapparat-pruefung and one by science-arbeitsplan-erstellen". |
| Status | verified |
| Severity | minor |
| Source | S2 |

**GB-25 The results rest largely on the assistant's own check reports and on a summary, but the paper does not say which result rests on which class of record.**

| Field | Content |
|---|---|
| Check | P19 |
| Location | p. 10, l. 196 to 200; p. 17, l. 350 to 352; p. 17, l. 361 to 362 |
| Quotation | "check reports as quoted in the working chats, a summary document compiled from the chats, and the chats themselves"; "32 of the 117 statements about the two projects checked for this paper rest on the summary document only" |
| Concern | The paper names the classes globally, which is to its credit. But the counts of Section 4 are outputs of the assistant (check reports), passed on as quotations in chats, so they are model-generated data reported secondhand; 32 of 117 statements (27.4 %, recalculated) rest only on a summary whose compiler is not named. Which of the results in Section 4 and in the abstract are among the 32 is not identified, so a reader cannot tell how much of any given count is backed by a saved check report. The run dates of Norway and the date and version of the museum check are missing (l. 232), which fits a secondary record. |
| Suggestion | In 3.5 or a table in 4, mark each reported count with its record class: saved check report, log entry, chat quotation, summary only. Say who compiled the summary document (author or assistant). Where possible, re-derive the 32 summary-only statements from primary records or mark them in the text. Say also whether the author or the assistant checked the 117 statements (l. 199). |
| Status | verified (classes and count); assumption (that the summary was compiled by the assistant; to be stated by the author) |
| Severity | moderate |
| Source | SD |

#### Minor corrections

| ID | Location | Quotation | Replacement | Source |
|---|---|---|---|---|
| KK-03 | p. 10, l. 198 | "the Norway records begin on 10 September" | "the Norway records begin on 10 September 2026" | SD |
| KK-04 | p. 10, l. 201 to 202 | "for the Germany report to its version v15, so numbered since 21 September 2026" | "for the Germany report to its version v15, the version current from 21 September 2026" | SD |

#### Verification log

| ID | Check | Checked | Values | Result |
|---|---|---|---|---|
| PP-21 | design sketch | Design sketch of the study from the whole manuscript, including captions, Table A1 and declarations: questions and type, data sources, time axis, environment, principles and components, disclosed limits, chain from frame to result, proposals in the outlook | study type: retrospective case report of a method development by its developer, two cases, one author; hypotheses: none stated; comparison condition: none (stated for RQ3, l. 284 to 285); data sources: logs, work plans, decision logs, check reports as quoted in the chats, a summary document, the chats; data window to 28 September 2026, Norway records from 10 September; model change Claude Opus 5 to Claude Opus 5.5 undated; 12 disclosed limits, 5 at the claim they limit, 1 in part, 6 only in results, discussion, Limits or Data availability; RQ1 writing help, RQ2 origin of errors and the dictation gap have no instrument | no finding; basis for the design findings |
| PP-22 | P9 (selection) | selection of the two cases and of the examples in 4.1 | two reports of the author, disclosed (l. 361); examples marked as examples (l. 224) | no finding |
| PP-23 | P38 | Names of the two reports | Norway: "Norway report", "planning report" (4), "dossier" (6), "pre-excursion dossier" (1), "field guide", "pre-trip field guide" (l. 11); Germany: "Germany report", "post-trip report" (l. 10), "excursion report after the trip", "research excursion written up as a project report" (l. 253) | no finding. Section 3.1 (l. 91 to 93) explains that both forms of the Norway report are called the Norway report; l. 253 to 254 explains the Germany genre. The "separate results report" (l. 91, 373) is a different, future object. |
| PP-24 | P10 (frame) | RLHF analogy | introduced in Fig. 1 caption and taken up in 5 (l. 323 to 331) and 6 (l. 377 to 379), limited as "structural, not formal" | no finding |
| PP-25 | P6 | "Every task followed the same eight steps" (l. 122) against exceptions | exceptions named in l. 125 to 126 and Fig. 2; still pass steps 7 and 8 | no finding; scope of the abstract see GB-51 |
| PP-26 | P38 | Step and role names in text against Figures 1 to 4 | eight steps l. 122 to 125 against the eight boxes of Figure 2 ("Locate the task" to "Present the result for acceptance"); roles of Figure 3 against l. 163 to 165; Figure 1 boxes against l. 105 to 108 and legend l. 118 to 121 | no finding on names. The step names agree; the only naming issue (assistant and system) is GB-20. |
| PP-27 | P5 | wording proposal arithmetic; template rule count; fact support and museum sums; Mindat sums | 68 + 6 + 1 = 75; 31 + 12 = 43; 18 + 14 + 3 + 1 = 36; 12 + 4 + 3 = 19 rows; 21 + 4 + 1 = 26; Table A1 rows: 4 research, 1 elicitation, 4 writing, 1 rules, 2 clarification, 6 checking, 1 steering, 1 maintenance = 20, plus 2 framework = 22 | no finding; order rule see GB-23 |
| PP-28 | P38 | Skill identifiers in text, Table 2, Figure 6 and Table A1 | 22 identifiers in Table A1; in the body text template-dokumentprojekt (2), template-skill-projekt (2), science-entscheidungspunkt-klaeren (1), six identifiers in Table 2, three in Figure 6 (template-dokumentprojekt, science-quellenapparat-pruefung, science-arbeitsplan-erstellen); line breaks inside identifiers in Table 2 and at l. 193 to 194 checked on the page images | no finding. Every identifier matches Table A1 letter for letter. "Framework skills", "templates", "document template" and "skill template" are introduced at l. 109 to 110 and l. 171 to 172. "Genre selection skill" (l. 251) and "genre analysis" (l. 187) are two skills (geo-exkursionsbericht-erstellen, geo-exkursionsbericht-typenanalyse), as Limits l. 363 confirms. |
| PP-29 | P38 | Model names and markers | own tool: Claude Opus 5, Claude Opus 5.5 (l. 203 to 204); cited studies: Claude 3.5 Sonnet, Claude 3 Opus, Claude Opus 4.6, Claude Opus 4.8 (l. 44 to 47); markers OPEN/OFFEN and UNCLEAR/UNKLAR (l. 177 to 178) | no finding. The cited models and the own tool are different objects; the German marker names are explained. |
| PP-30 | P12 | Skills and templates against Appendix A and the Data availability statement | Table A1 on pp. 18 to 19 lists 22 entries: 4 Research, 1 Elicitation, 4 Writing, 1 Rules, 2 Clarification, 6 Checking, 1 Steering, 1 Maintenance (20 skills, 10 geo-, 10 science-) and 2 Framework; link https://github.com/nordie69/Talk-Check-Decide at l. 387 and l. 389, MIT licence named at both places | no finding. The appendix is in the manuscript and counts as accessible. Reachability not checked: the WebFetch request for the repository was not sent (permission request not answered), so neither the content nor the state "of 27 September 2026" (l. 386) could be compared. |
| PP-31 | P38 | Version identifiers of skills and templates | science-arbeitsplan-erstellen 5.0.0, template-skill-projekt 1.5.0, template-dokumentprojekt 1.6.0 (l. 383 to 384); 1.5.0 of 27 September added chat record and wording proposals to both templates, 1.6.0 of 28 September the running-chat rule (l. 384 to 386); "Since 28 September 2026, the document template extends the rule" (l. 181); rule counts 31 + 12 = 43 (l. 114, 261, 282, 371) | no finding. Dates and numbers agree; the shared number 1.5.0 is explained by "both templates". |

### Segment 3: Results (p. 11 to 14)

#### Substantive findings

**GB-26 The fall in consistency findings offered as indication for the second part of RQ3 compares absolute counts on changing bases and has causes that the manuscript itself names but does not separate.**

| Field | Content |
|---|---|
| Check | P21, P15, P9 |
| Location | p. 11, l. 211 to 218; p. 12, Figure 5; p. 15, l. 283 to 285; p. 17, l. 372; p. 11, l. 203 to 204; p. 5, l. 105 to 108; p. 4, Table 1, row Size |
| Quotation | "That it also improved the reports is indicated by findings that fell over successive runs between large changes, but not shown" |
| Concern | The manuscript states that with two cases and no comparison group the improvement is "not shown" and names one confound, that "better skills cannot be separated from reports that simply matured" (l. 284 to 285). What is not drawn to its end is that the indication itself rests on absolute counts with three further possible causes. (1) Scope and base: the Norway runs checked v17 to v100; run 1 is labelled "report only", run 7 "two-part run" (Figure 5), and run 7 "was also made in two separate parts and then merged" (l. 213), with no merge rule given. Only the final size is given (about 42,000 words, Table 1), so findings per unit of text cannot be formed. In Germany, three runs over chapter 1 produced 10, 9 and 7 findings (sum 26), three later runs over the whole report 3, 5 and 4 (sum 12); the chapter 1 runs are undated. (2) Suppression: documented non-findings "stopped later runs from raising them again" (l. 215). The Figure 5 values, measured on the raster (PP-41), are findings 18, 4, 6, 4, 0, 2, 71 and non-findings 9, 6, 10, 12, 12, 10, 42; the non-findings accumulated before runs 2 to 7 are 9, 15, 25, 37, 49, 59, and the suspicions raised per run (findings plus non-findings) are 27, 10, 16, 16, 12, 12, 113 (Python). Falling findings therefore partly measure suspicions set aside, not errors absent. (3) Change of checker: the checking skills were revised after each review round (l. 105 to 108), and the model changed from Claude Opus 5 to Claude Opus 5.5 at an undated point (l. 203 to 204). A falling count is compatible with an improving report, with suppression, with a narrower run and with a changed checker; normalised by size and scope, the sequence could flatten or reverse. Graded major because the indication answers part of RQ3. |
| Suggestion | In section 4.1 and Figure 5, give for each run the version, the checked scope (chapters, appendices) and its size in words, findings per 1,000 words, the skill version, the model, and the number of carried-forward non-findings; for run 7, the counts of each part and the merge rule. A design that separates the causes: rerun the current skill and model once over two archived versions (for example v17 and v67), with and without the carried-forward non-findings. In section 5 (l. 283 to 285) and section 6 (l. 372), name suppression, scope and change of checker next to maturation, and weaken "indicated" accordingly. |
| Status | verified (counts, versions, scope labels, mechanism l. 215, model change; Figure 5 values by measurement); inferred (accumulated non-findings and suspicions per run, Python; that normalisation could flatten or reverse the sequence) |
| Severity | major |
| Source | S3, S4, SD |

**GB-27 That the Norway findings "fell over the first six runs and rose only after large changes" does not describe the sequence 18, 4, 6, 4, 0, 2, and Figure 5 gives no measure of which changes count as large.**

| Field | Content |
|---|---|
| Check | P2, P3 |
| Location | p. 11, l. 211; p. 12, Figure 5, bars and row "Change before run", caption l. 222 to 223; p. 1, l. 13; p. 15, l. 284 |
| Quotation | "In the Norway report, findings fell over the first six runs and rose only after large changes." |
| Concern | Text, Abstract (l. 13) and Figure 5 agree on the numbers; the bar heights match the labels within 0.2 (PP-41). The run to run differences are minus 14, plus 2, minus 2, minus 4, plus 2: findings rose twice within the first six runs, at run 3 after "localities renumbered, literature added" and at run 6 after "measures of the three-perspective critique". They fell after "route direction reversed, one locality added" (run 2, 18 to 4) and stayed at 0 after "locality 21 added" (run 5). The figure names every change in words but gives no size for any of them, so the reader cannot tell why reversing the route and adding a locality is not a large change while renumbering localities is. Two readings are possible: the size of each change was recorded, and can be added; or "large" was judged afterwards, and the sentence describes an interpretation. The design instance logged no finding on l. 211, noting that both rises follow named changes (PP-39); checked at the page images of pages 11 and 12, the changes are named but not graded, so "large" stays undefined and the finding stands. Graded moderate: the counts stay, but the reader cannot check the claim on which the indication for RQ3 (l. 284) rests (GB-26). |
| Suggestion | Add to Figure 5 a measure of the size of each change (words or sections changed between v17, v47, v59, v63, v64, v67 and v100), or state in section 4.1 (l. 211) and in the caption (l. 222) by which criterion a change counts as large. Otherwise write in l. 211 "findings fell from 18 to 2 over the first six runs, with small rises in runs 3 and 6 after the renumbering of localities and after the measures of the three-perspective critique", and replace "rose only after large changes" in the caption by a description of the two rises. |
| Status | verified (bar values by measurement; rises and falls computed from them; absence of a size measure on the page image); assumption (whether a size was recorded, asked as a question) |
| Severity | moderate |
| Source | S3, AB |

**GB-28 Unverified judgements of the assistant steer later selection: carried-forward non-findings, the clustering of working patterns, and the preselection of the Germany localities.**

| Field | Content |
|---|---|
| Check | P27 |
| Location | p. 11, l. 214 to 215; p. 5, l. 100 to 101; p. 10, l. 202 to p. 11, l. 203 |
| Quotation | "they stopped later runs from raising them again"; "268 working patterns were written down and clustered into 12 groups; the gaps between groups became new skills"; "The localities of the Germany tour were selected before it with ChatGPT and Claude" |
| Concern | (1) A documented non-finding is a judgement that a suspicion is unfounded; if it is wrong, the carried-forward record removes the error from every later run. 101 non-findings were recorded in the seven Norway runs (recalculated); none is reported as rechecked. (2) The clustering, which decided which skills were built, is not described and not checked. (3) The model-assisted preselection of localities fixed the Germany case; whether its output was checked is not said. |
| Suggestion | In 4.1, report a recheck of a sample of carried-forward non-findings (for instance 15 of the 42 of run 7) and state whether non-findings expire with a version change. In 3.2, say who clustered the patterns and by which criterion, and whether the author checked it. In 3.5, say whether the locality preselection was checked and against what. |
| Status | verified (components and their downstream use); inferred (risk of hidden errors) |
| Severity | moderate |
| Source | SD |

**GB-29 For the Germany consistency runs non-findings are given for one run only, and three runs are dated with two dates.**

| Field | Content |
|---|---|
| Check | P11, P22 |
| Location | p. 11, l. 215 to 218 |
| Quotation | "three later runs, on 19 and 21 September, produced 3, 5 and 4; three runs over chapter 1 produced 10, 9 and 7 findings; the first of them also recorded 16 non-findings." |
| Concern | For Norway, findings and documented non-findings are reported for every run (Figure 5: 9, 6, 10, 12, 12, 10, 42). For Germany, non-findings are given for one of eight runs (16, first chapter-1 run); for the other seven runs it is not said whether none were recorded or they were not counted. Because l. 215 attributes to non-findings the effect of stopping later runs from raising suspicions again, the missing values matter for reading the Germany sequence 29, 8, 3, 5, 4. In addition, the reader has to infer that one of the two dates, 19 or 21 September, carried two runs, and the chapter-1 runs carry no date at all. |
| Suggestion | In l. 215 to 218, give per Germany run the date, scope, findings and non-findings (or "not recorded"), for instance as a short table parallel to Figure 5. |
| Status | verified (p. 11, Figure 5 labels on p. 12) |
| Severity | moderate |
| Source | S3 |

**GB-30 Two labels in the row "Change before run" of Figure 5 describe the run itself, not a change before it.**

| Field | Content |
|---|---|
| Check | P29 |
| Location | Figure 5, row "Change before run", Run 1 and Run 7, p. 12; caption l. 221 to 222 |
| Quotation | "first run, report only" and "target format now dossier; two-part run"; "below each run stand the version of the report it checked and the change made before it" |
| Concern | The caption announces one change per run. Under Run 1 there is no change but a scope ("report only"), and under Run 7 the change ("target format now dossier") is joined to a property of the run ("two-part run", described in l. 213 as "made in two separate parts and then merged"). "report only" is not explained anywhere: the reader cannot tell whether it means without the 7 appendices listed in Table 1 or something else, and whether later runs included the appendices, which would affect the comparison of counts across runs. |
| Suggestion | In Figure 5 write "none (first run)" under Run 1 and move scope and mode of a run ("report only", "two-part run") into the run label or the caption (p. 12, l. 221), and say in section 4.1 (l. 211 to 214) which parts of the report each run covered. |
| Status | labels verified on the page image; meaning of "report only": assumption, asked as a question |
| Severity | minor |
| Source | AB |

**GB-31 The museum fact check switches its unit from statements to rows.**

| Field | Content |
|---|---|
| Check | P20 |
| Location | p. 12, l. 229 to 232 |
| Quotation | "A check of statements about museums, 20 statements in 19 rows, found 12 rows verified, 4 partly verified and 3 misattributed" |
| Concern | The chapter-1 check is reported in statements (18 + 14 + 3 + 1 = 36 statements, l. 229 to 231). The museum check announces 20 statements and then reports rows: 12 + 4 + 3 = 19 rows. The sum closes on rows, but the verdict for the 20 statements cannot be derived: one row holds two statements, and whether both share the row's verdict is not said. The misattribution share is 3/19 = 15.8 % per row or 3/20 = 15.0 % per statement, and the chapter-1 share is 1/36 = 2.8 % per statement; the manuscript does not compare them, but a reader who does cannot use the same unit. |
| Suggestion | In l. 231 to 232, give the result per statement (verified, partly verified, misattributed, not checkable, summing to 20), or state how the row with two statements was graded. |
| Status | verified (p. 12); quoted shares inferred: 3/19 = 15.8 %, 3/20 = 15.0 %, 1/36 = 2.8 % |
| Severity | moderate |
| Source | S3 |

**GB-32 The sub-counts of the 13 reference errors do not form a partition, and the reader has to compute the missing ones.**

| Field | Content |
|---|---|
| Check | P22, P20 |
| Location | p. 13, l. 237 to 242; p. 14, l. 273 to 274; p. 17, l. 362 |
| Quotation | "found 13 errors, about 6 %. Five were found by checks that needed no search, among them comparisons of an entry with the document's own practice. Four of the six errors among entries with a DOI sat among the 11 most cited works. Three DOIs pointed to a real but different paper"; "About one entry in eight could only be checked in part." |
| Concern | The rate is correct: 13/211 = 6.16 %, "about 6 %". The four sub-counts use different splits (how found: 5; DOI or not: 6; most cited: 4 of 6; type: 3 wrong DOIs) and none is completed: the reader has to infer that 13 minus 6 = 7 errors sat in entries without DOI and that 2 of the 6 DOI errors were outside the 11 most cited works; whether the 3 wrong DOIs are among the 6 is not said; the number of entries with a DOI is not given, so an error rate per DOI entry cannot be formed; "one entry in eight" corresponds to about 211/8 = 26.4 entries, but the count is not stated. RQ2 (l. 274 to 278) lists "wrong DOIs or authors" as an error class, yet section 4.3 gives no breakdown of the 13 errors by class. |
| Suggestion | In section 4.3, give the 13 errors in one table by error class and by with or without DOI, the number of entries with a DOI, and the number of entries checked only in part. |
| Status | verified (p. 13, p. 14, p. 17); derived values inferred: 13/211 = 6.16 %, 13 minus 6 = 7, 6 minus 4 = 2, 211/8 = 26.4 |
| Severity | moderate |
| Source | S3 |

**GB-33 The reference accuracy result refers to 211 entries, while the version the paper reports has 226; 15 entries were not covered by the full check.**

| Field | Content |
|---|---|
| Check | P7 |
| Location | p. 13, l. 237; p. 4, Table 1, row Size, column Germany; p. 10, l. 200 to 202; p. 14, l. 273 to 274; p. 15, l. 311; p. 17, l. 362 |
| Quotation | "about 55,000 words, 226 references in version v15"; "covered the 211 entries it held on 18 September 2026" |
| Concern | 226 minus 211 = 15 entries (6.6 % of 226, recalculated) were added after the full check. Whether they were checked is not said; the rule that reference accuracy runs "at the latest before submission" (l. 188 to 189) suggests a later check that is not reported. In l. 273 to 274 and l. 362 the ratio "one in eight" is given for "the Germany list", whose denominator is the 211 entries of 18 September, not the 226 of v15 (taken over from S3). |
| Suggestion | In 4.3, state whether the 15 later entries were checked and with what result, or give the error figure for v15. In l. 274 and l. 362, write "about one in eight of the 211 entries checked on 18 September". |
| Status | verified (numbers); inferred (gap) |
| Severity | moderate |
| Source | SD, S3 |

**GB-34 No axis has an estimate of the errors it missed; the second Mindat pass reviewed the first pass's proposals, not the citations it passed.**

| Field | Content |
|---|---|
| Check | P32 |
| Location | p. 13, l. 237 to 242; p. 13, l. 244 to 247; p. 12, l. 229 to 231; p. 1, l. 14 |
| Quotation | "A full check of the Germany reference list covered the 211 entries ... and found 13 errors, about 6 %"; "confirmed 21 of them, 4 in part and 1 with a condition" |
| Concern | The 13 errors (6.16 % of 211, recalculated) are a lower bound: the 198 entries passed as correct, and the about 26 entries (one in eight of 211) checked only in part, were not resampled independently. In the Mindat check, 26 of 55 citations (47.3 %) were flagged; the second pass confirmed flagged ones, and nothing is said about the 29 unflagged citations. The fact check reports verified and partly verified statements without an independent recheck. RQ2 asks which checks catch errors "before publication"; without a miss rate this cannot be answered beyond "some". |
| Suggestion | In 4.3 and 4.4, report an independent recheck of a random sample of the items passed as correct (for example 30 of the 198 reference entries and 10 of the 29 unflagged Mindat citations, checked by the author or a second person against the source) with the error rate found and its confidence interval. |
| Status | verified (no such sample reported); inferred (shares) |
| Severity | moderate |
| Source | SD |

**GB-35 The locality evidence check passes from 55 citations to 26 proposals to 22 changes without stating how the units map.**

| Field | Content |
|---|---|
| Check | P20, P23 |
| Location | p. 13, l. 244 to 247 |
| Quotation | "all 55 citations of Mindat were checked, in version v67, for whether the cited page supports the statement for that very site ... A first pass produced 26 proposals for change. A second pass ... confirmed 21 of them, 4 in part and 1 with a condition; all 26 were carried out, in 22 changes to the text." |
| Concern | The second-pass sum closes: 21 + 4 + 1 = 26. The question the check asks (does the cited page support the statement for the site) is however answered in proposals, not in citations: how many of the 55 citations failed is not stated. If each proposal concerns one citation, 55 minus 26 = 29 citations passed; if a proposal can cover several citations, more than 26 failed. The balance from 26 proposals to 22 changes (26 minus 22 = 4) is not resolved in the text. Resolution A: four pairs of proposals were merged into one change each (8 proposals into 4 changes). Resolution B: five proposals were merged into one change. Resolution C: some proposals were carried out outside the text proper, for instance in reference entries, and are not counted as changes to the text. It is also not said what was carried out for the 4 proposals confirmed only in part and the 1 with a condition, given that "all 26 were carried out". The datum that decides is the mapping of citations to proposals and of proposals to changes. |
| Suggestion | In l. 245 to 247, give the number of the 55 citations that did not support the site statement, state whether a proposal covers one citation, explain the reduction from 26 proposals to 22 changes, and say in what form the 5 not fully confirmed proposals were carried out. In l. 246 to 247, write "confirmed 21 of them fully, 4 in part and 1 with a condition". |
| Status | counts verified (p. 13); the three resolutions inferred |
| Severity | moderate |
| Source | S3, SD |

**GB-36 How could the second Mindat pass confirm the first pass's proposals without having seen its results?**

| Field | Content |
|---|---|
| Check | P25 |
| Location | p. 13, l. 245 to 247 |
| Quotation | "A second pass by separate instances of the assistant, which had not seen the results of the first pass, confirmed 21 of them, 4 in part and 1 with a condition" |
| Concern | To confirm 21 of 26 proposals, the second pass needed the proposals, which are results of the first pass. Two readings are possible: it saw the proposals but not the first pass's reasoning, or it checked all 55 citations independently and agreement was matched afterwards. In the first reading the pass is not blind to which citations were flagged; in the second, its own findings on the 29 unflagged citations should be reported (GB-34). |
| Suggestion | In 4.4, say what the second pass received as input (all 55 citations, or the 26 proposals) and, in the second case, how many of the 29 unflagged citations it flagged. |
| Status | inferred |
| Severity | moderate |
| Source | SD |

**GB-37 The genre analysis measured the Germany report against four candidate genres but reports a result for one.**

| Field | Content |
|---|---|
| Check | P11 |
| Location | p. 13, l. 249 to 254 |
| Quotation | "Measured against four candidate genres in its version v13 of 19 September 2026, the Germany report met 9 of 11 obligations of an excursion report"; "The author chose as target genre the research excursion written up as a project report, one of the four candidates; in this paper, it counts as an excursion report after the trip." |
| Concern | The analysis was announced for four candidates, and Table A1 describes the skill as checking "a finished report against every candidate genre". Section 4.5 gives the obligations met for one genre only (9 of 11), and it remains for the reader to combine l. 250 and l. 253 to 254 to conclude that "an excursion report" in l. 250 is the chosen target genre. For the other three candidates no counts are given, although the comparison across candidates is what the analysis produces and what justified the choice. The two obligations not met are not named. |
| Suggestion | In section 4.5, give for each of the four candidates the number of obligations and the number met, name the two unmet obligations of the target genre, and write in l. 250 "of the target genre, the research excursion written up as a project report". |
| Status | verified (p. 13, p. 18) |
| Severity | moderate |
| Source | S3 |

**GB-38 The usefulness result of 45 measures per critique is fixed by the procedure, so it carries no information about the report.**

| Field | Content |
|---|---|
| Check | P20, P21 |
| Location | p. 13, l. 254 to 256; Table A1, p. 18, row science-dokumentkritik-drei-sichten, column Task |
| Quotation | "produced 45 measures, of which the author struck 9; a second critique on 26 September produced 45 more."; "usefulness from three reader perspectives, with 15 measures each" |
| Concern | Section 3.4 promises a counted result for each axis (l. 185 to 186), and section 4.5 gives the usefulness counts. By Table A1 the skill produces 15 measures for each of three perspectives: 3 × 15 = 45. Both critiques therefore produced exactly the number the procedure prescribes; the count 45 is a quota, not a measurement, and the equality of the two critiques ("45 more") says nothing about whether usefulness improved between them. The informative numbers are those the reader has to look for: for the first critique, 45 minus 9 = 36 measures were kept, but how many were carried out is not given; for the second critique, neither struck nor carried out measures are given. The two qualitative gaps named (daily plan, radioactive minerals) are a strength of the passage and show that the axis finds what other checks do not. |
| Suggestion | In section 4.5, state that the skill prescribes 15 measures per perspective, and report for both critiques the measures struck, kept and carried out, with version and date. |
| Status | 3 × 15 = 45 and the wording verified (p. 13, p. 18); that the count is fixed by the procedure inferred from Table A1 |
| Severity | moderate |
| Source | S3 |

**GB-39 Figure 6 shows six failures next to the 43 template rules, but the 43 are not listed and no criterion for choosing the six is given.**

| Field | Content |
|---|---|
| Check | P34 |
| Location | p. 13, l. 261 to 263; p. 14, Fig. 6, column "Skill that carries the rule", and caption l. 268 to 269 |
| Quotation | "Every rule of the two templates names the incident it came from, 43 in all; Figure 6 shows six failures and the rules they produced" |
| Concern | The sentence and the caption state openly that of the six rules two are carried by the document template, three by the reference check and one by the work plan skill (l. 262 to 263; caption, l. 269), so four of the six are not among the 43 template rules; at the page image, rows 1 and 6 name template-dokumentprojekt, rows 2 to 4 science-quellenapparat-pruefung and row 5 science-arbeitsplan-erstellen. What remains open: the 43 rules are not listed, the rules of the other skills "were not counted" (l. 283), and how the six examples were chosen is not said ("The six rows are examples", l. 269). A reader can therefore not check any of the 43 rules or judge whether the six are typical of them. |
| Suggestion | In 4.6, state how the six examples were chosen, separate the sentence on the 43 from the figure, and give the full list of 43 rules with incident and date in an appendix or supplement (needed for GB-44 as well). |
| Status | verified |
| Severity | moderate |
| Source | SD |

#### Minor corrections

| ID | Location | Quotation | Replacement | Source |
|---|---|---|---|---|
| KK-05 | p. 13, l. 237 to 238 | "found 13 errors, about 6" at the end of l. 237 and "%." at the start of l. 238 (page image) | "found 13 errors (6.2 %)", with a non-breaking space between number and percent sign; if the rounded form is kept, "about 6 %" with the same space | S3, S4, SD |

#### Verification log

| ID | Check | Checked | Values | Result |
|---|---|---|---|---|
| PP-32 | P1 | Sums and differences in sections 3 and 4 | Chapter-1 fact check 18 + 14 + 3 + 1 = 36; museum check 12 + 4 + 3 = 19 rows; reference errors 13/211 = 6.16 % ("about 6 %"); Mindat second pass 21 + 4 + 1 = 26; template rules 31 + 12 = 43 (l. 114, 261, 282, 371); Figure 6 rules 2 + 3 + 1 = 6 (l. 262, l. 269 and figure column); proposals 68 + 6 + 1 = 75 (l. 144 to 145); version rule 38 + 1 = 39 (l. 115 to 116); tour 2 to 9 August = 8 days (Table 1); usefulness 3 × 15 = 45 (Table A1, l. 255); summary-only share 32/117 = 27.4 % | no finding; all within rounding. The manuscript discloses that the museum check's date and version were not recorded (l. 232) and that the first critique's version and date were not recorded (l. 255) |
| PP-33 | P2 | Quantities stated in more than one place, abstract included | Norway findings 18, 4, 6, 4, 0, 2, 71: abstract l. 13 = Figure 5 labels; 71: l. 13, l. 211, l. 222; non-findings 6 to 12 and 42 (l. 214 to 215) = Figure 5 labels 9, 6, 10, 12, 12, 10, 42 (min 6, max 12); 211 entries and 18 September: l. 14 = l. 237; 226 references: Table 1 = l. 311; 20 skills and two templates: l. 8, l. 20, l. 170, Table A1 (22 entries, l. 383); localities 20 and 21: l. 10 to 11 = Table 1; 268 patterns: l. 100, l. 198, l. 350; 32 of 117: l. 199 = l. 350; three single-axis cases: l. 15, l. 280, l. 286 with three cases named in l. 287 to 290; 243 log entries: Table 1 = l. 363; one in eight: l. 240, l. 274, l. 362; 15 genre types: l. 250 = Table A1; v67: l. 244, l. 255, Figure 5 run 6; v100: l. 92, l. 201, Figure 5 run 7 | no finding beyond GB-27, GB-33 (denominator wording, taken over from S3) and GB-48; the 211 and 226 references are different dates, not a contradiction (l. 201, l. 237) |
| PP-34 | P2 | Version chronology Germany and Norway | Germany runs 13 and 15 September before genre analysis on v13 of 19 September (l. 187 to 188, l. 216, l. 249); v15 numbered since 21 September (l. 201); fact check 24 September (l. 229); first Norway critique before v67 (l. 255) and Figure 5 run 6 at v67 "measures of the three-perspective critique"; dossier since 26 September as v100 (l. 91 to 92, l. 201) | no finding |
| PP-35 | P23 | Lists whose announced count can be recounted | "Eleven rules" (l. 176 to 181): 11 listed; "eight steps" (l. 122 to 125): 8 listed, step 5 is the confirmation; Table A1 rows by role: 4 + 1 + 4 + 1 + 2 + 6 + 1 + 1 = 20, plus 2 framework = 22; checking role 6 skills = 6 axes of Table 2; three named misattributions of the museum check = 3 (l. 232 to 235) | no finding |
| PP-36 | P20 | Denominators of the chapter-1 fact check and the reference check | Chapter-1: 36 statements carrying a source, all four categories in statements; reference check: 13 of 211 entries, unit entries | no finding for these two; see GB-31 and GB-32 for the other quotas |
| PP-37 | P21 | Comparisons between checks of different size | The manuscript does not compare the misattribution rates of the chapter-1 check (1/36 = 2.8 %) and the museum check (3/19 = 15.8 %), nor findings across the two reports | no finding; only the run sequences are compared (GB-26) |
| PP-38 | P11 | Claim "Section 4 reports a counted result for each of them" per axis | Genre 9 of 11 (4.5); fact support 36 and 19 (4.2); consistency both cases (4.1); reference accuracy 13 of 211 (4.3); locality evidence 26 proposals (4.4); usefulness 45 measures (4.5) | no finding per axis; per case see GB-23 |
| PP-39 | P6 | "findings fell over the first six runs and rose only after large changes" (l. 211) against Fig. 5 | 18, 4, 6, 4, 0, 2; rises at run 3 (after renumbering, literature added) and run 6 (after critique measures), both after named changes; non-findings 6 to 12 in runs 1 to 6 (9, 6, 10, 12, 12, 10) | no finding in this instance; S3 and AB read the same sentence as a finding. Checked at the page images of pages 11 and 12: the changes before runs 3 and 6 are named but not graded, so "large" stays undefined; decided as finding GB-27 |
| PP-40 | P36 | memory statements against the paper's own records | "about one entry in eight" l. 240, l. 274, l. 362 consistent with each other; "two or three points" l. 252 not checkable; Germany runs 29, 8, 3, 5, 4 and 10, 9, 7 consistent between l. 216 to 217 and abstract (abstract gives Norway only) | no finding; the author's view is marked as such where used (l. 224, 296, 300) |
| PP-41 | P3 | Bar heights of Figure 5 against the bar labels, the abstract (l. 13) and section 4.1 (l. 211 to 215) | Calibration on gridlines: 0 at y = 934.0 px (axis line, 3 px), 80 at y = 150.5 px; intermediate gridlines 20, 40, 60 at 738.5, 542.5, 346.0 px measure 19.96, 39.97, 60.04 (spacing 195.5, 196.0, 196.5, 195.5 px, linear). Slope 0.1021 per px, uncertainty ±0.2 with calibration error 1 px. Blue bars (findings), top edges: Run 1 758 px = 17.97; Run 2 896 px = 3.88; Run 3 877 px = 5.82; Run 4 896 px = 3.88; Run 5 no blue bar = 0; Run 6 916 px = 1.84; Run 7 240 px = 70.86. Green bars (non-findings): Run 1 847 px = 8.88; Run 2 877 px = 5.82; Run 3 837 px = 9.90; Run 4 818 px = 11.84; Run 5 818 px = 11.84; Run 6 837 px = 9.90; Run 7 524 px = 41.86. Bars end at y = 932 px, 2 px above the axis centre, which explains the common offset of about -0.15. Text: findings 18, 4, 6, 4, 0, 2, 71 (l. 13, bar labels); non-findings "from 6 to 12 in the first six runs" and "42 in the seventh" (l. 214 to 215), measured 6 to 12 and 42. | no finding: every bar agrees with its label and the text within ±0.2; the interpretation of the run sequence is in GB-27 |
| PP-42 | P24 | Order of versions and dated events in Figure 5 against the text | Versions under the runs: v17, v47, v59, v63, v64, v67, v100, strictly increasing. Text: Mindat check "in version v67" (l. 244) and Run 6 at v67 after "measures of the three-perspective critique", whose first critique was "made on a version before v67" (l. 255); Run 7 at v100 after "target format now dossier", and the report "was a planning report until 26 September 2026 and has since been a pre-excursion dossier (version v100)" (l. 91 to 92), version v100 "of 26 September 2026" (l. 201); Norway records begin on 10 September (l. 198); the version rule starting at v39 (l. 115 to 116) lies between Run 1 (v17) and Run 2 (v47). Number of runs 7 against "seven consistency runs" (l. 13, caption l. 220). The figure has no date axis; dates of the runs are not given. | no finding; the manuscript itself discloses that counts refer to v100 of 26 September 2026 (l. 200 to 201) |
| PP-43 | P37 | figures and tables with later changed values | Fig. 5 run 7 shows the merged count 71; the label "two-part run" stands under the bar; no recalculation of other values is reported | no finding; merge rule see GB-26 |
| PP-44 | P30 | corrections against runs | no reported correction of a check method is dated; failures in Fig. 6 undated | not testable; see GB-17 |

### Segment 4: Discussion, conclusions, references, declarations (p. 11, 14 to 25)

#### Substantive findings

**GB-40 The AI declaration does not say what "verified" covers, who verified, or which model drafted the paper, and the author contributions name the author alone as writer.**

| Field | Content |
|---|---|
| Check | P2 |
| Location | p. 11, l. 205 to 208; p. 19, l. 394 to 395; p. 11, l. 203 to 204 |
| Quotation | "This paper was drafted with Claude from the author's dictated instructions, the skills listed in Appendix A and the project records of both reports. The literature was searched and every reference verified against a publisher, society or institutional page, a DOI landing page or a Crossref record." |
| Concern | The declaration names the tool and states that "The author is responsible for all content" (l. 208), in line with the guidance the paper cites (l. 58 to 60). Three points are open. (1) "verified against a publisher, society or institutional page, a DOI landing page or a Crossref record" names targets that confirm existence and bibliographic data; it does not say whether each cited source was checked for the statement it is cited for. Six findings in segment 1 (GB-04, GB-06, GB-07, GB-08, GB-09, GB-11) concern cited statements that differ from, or select from, what the sources report, for example the 1.3 % for English texts from Wolniewicz (2024), which in the source is the share "demanding a significant improvement" (verified in the source, see GB-09). A reader may take "verified" to cover the content. (2) It does not say whether the assistant or the author verified, which matters because the same assistant drafted the text. (3) It names "Claude" without a version, while section 3.5 names Claude Opus 5 and Claude Opus 5.5 for the reports only (l. 203 to 204). In addition, Author contributions say that SM "wrote, reviewed and edited the manuscript" (l. 395), while section 3.6 says "This paper was drafted with Claude" (l. 206); the two declarations should give the same division of labour. Raised as a hint by S1 and S4 and not handled as a finding by the responsible instance; confirmed at the page images of pages 11 and 19. |
| Suggestion | In section 3.6 (p. 11, l. 207 to 208), state what the verification covered, for example "every reference was checked for existence and bibliographic data against ...; whether each cited source supports the statement was checked for ...", say who verified, and name the model version and interface used for this paper. In Author contributions (p. 19, l. 394 to 395), write for example "wrote the manuscript with the AI assistant described in section 3.6, and reviewed and edited it". |
| Status | verified (wording at p. 11 and p. 19); inferred (that the named targets describe a bibliographic check) |
| Severity | minor |
| Source | ZF |

**GB-41 The closest prior work and the error-rate studies from Related work are not taken up in the Discussion, and the Conclusions do not return to the gap.**

| Field | Content |
|---|---|
| Check | P15 |
| Location | p. 14 to 17, l. 270 to 379; p. 3, l. 42 to 57 and 65 to 67; p. 4, l. 83 to 85 |
| Quotation | "The closest work to the present one used a language model to write geosite descriptions and found that 44.8 % of the Polish and 1.3 % of the English texts needed editing after manual and field checks (Wolniewicz, 2024)." |
| Concern | Wolniewicz (2024) is cited once only, at l. 67 (counted with Python over the whole text). Walters and Wilder (2023), Güneş, Cesur and Çamur (2026) and Topaz et al. (2026a, 2026b) do not appear in section 5. The reference error rate of section 4.3 (13 of 211, 6.2 %, computed) is not set against these rates. A comparison would need to say that the Germany list does not separate references proposed by the assistant from others. Section 6 does not state what the paper adds to the gap in l. 83 to 85. Graded minor because no result changes; the concern is how the results are placed in the literature. Such a comparison should use the corrected values of Wolniewicz (2024), see GB-09. |
| Suggestion | In section 5 add a short paragraph that sets section 4.3, and the editing need, against Wolniewicz (2024) and the error-rate studies already cited, with the caveat on the denominator. In section 6 add one sentence on the gap. |
| Status | verified (citation counts with Python) |
| Severity | minor |
| Source | S4 |

**GB-42 The answer to RQ1 ranks checking "above all" and the Conclusions state the ranking as a finding, but no result in section 4 measures the assistant's help in research, elicitation or writing.**

| Field | Content |
|---|---|
| Check | P15, P10, P31 |
| Location | p. 14, l. 271 to 274; p. 17, l. 367 to 368; p. 1, l. 15 to 16; p. 2, l. 34 to 35; p. 7, l. 140 and 144 to 145; p. 8, l. 155 to 156 |
| Quotation | "RQ1: The assistant helped in research, provided that every reference it proposed was verified; in drawing out the author's observations one question at a time; and above all in counted checking along separate axes." and "its main value in these two cases lay in systematic, counted checking along separate axes" |
| Concern | RQ1 is comparative: where the assistant helps and where it falls short. One part of the answer has a result behind it: the shortfall "where sources were out of reach" rests on section 4.3 ("About one entry in eight could only be checked in part", l. 240 to 241). The other parts do not. Sections 4.1 to 4.6 report only counts from checks. No result covers help in research (how many references the assistant proposed and how many failed verification), help in elicitation (the only passage is in the methods, p. 8, l. 155 to 156: "By his own account ... the share was not measured"), help in writing, or the shortfall in field observation. The paper holds the data for one such measure: it counts 75 wording proposals (68 + 6 + 1 = 75, recalculated) and names the author's three answers, "The author confirmed, changed or rejected it" (l. 140), but does not report how many proposals were confirmed unchanged, changed or rejected. "Above all" and "main value" rank the areas of help against each other, which the design cannot do without such a measure. The Abstract hedges the claim ("The results suggest that the value of AI assistance lies above all in systematic, counted checking", l. 15 to 16); the Conclusions state it as a finding ("lay in"). Graded major because it concerns the answer to RQ1: if the concern holds, what the manuscript can say about RQ1 drops from a ranking to a hypothesis. |
| Suggestion | In a new subsection of section 4, report the outcome of the 75 proposals (confirmed unchanged, changed, rejected, and for changed ones the kind of change), and for research help the number of references proposed by the assistant and how many failed verification. A design that would answer RQ1: for a defined set of passages, record whether the assistant drafted it, how much of the draft survived (character comparison against the inserted text) and which axis later found errors in it. Until then, mark the help in research and elicitation in section 5 (l. 271 to 274) as the author's experience with a pointer to p. 8, l. 155 to 161, and in section 6 (l. 367) write "the results suggest that its main value in these two cases lay in", matching the Abstract. |
| Status | verified (no result in section 4 for help in research, elicitation or writing, or for field observation; proposal counts, l. 144 to 145); inferred (that the ranking is not carried by the design; that outcome data exist in the logs, from l. 140 to 143) |
| Severity | major |
| Source | S4, SD |

**GB-43 The answer to RQ2 does not trace the errors to their origin, leaves out the errors of the checks themselves, and argues from the type of error, not from recorded coverage, that the other axes could not see the three single-axis errors.**

| Field | Content |
|---|---|
| Check | P15, P10 |
| Location | p. 14, l. 274 to 280; p. 15, l. 281 and 286 to 290; p. 2, l. 35 to 36; p. 1, l. 15; p. 12, l. 232 to 233; p. 14, Figure 6, rows 1, 2 and 4; p. 17, l. 367 to 379 |
| Quotation | "The errors that arose in AI-assisted writing, not all of them introduced by the assistant, were misattributions, misplaced attributions, wrong DOIs or authors, regional statements transferred to single sites, stale numbers and cross-references, and editing accidents" and "The DOI pointing to a neighbouring paper was invisible to both." |
| Concern | The manuscript says that not all of these errors were introduced by the assistant and discloses that "how often each type occurred or was missed was not counted" (l. 286 to 287); that limit is not raised again here. Three consequences are not drawn. (1) Origin: none of the six classes is traced to where it came from, the assistant while writing, the author, a source or an inherited bibliography; one museum misattribution was "taken over from an unchecked bibliography" (l. 233). The core term of RQ2, "introduce", is therefore not answered. (2) Errors of the checks: Figure 6 documents failures in the assistant's own checking, row 2 "A search pattern flagged all 20 map sheets because of a grid shifted by one line" and row 4 "Checked, no finding" without a source (page image). Only the editing accident of row 1 appears in the answer, as "editing accidents"; false positives of a check and "no finding" reports without a source are missing, though they are the errors most clearly introduced by the assistant. (3) Which checks catch them: each axis is reported for one report only, and only consistency for both (GB-23). The text does not say whether the chapter 1 fact check covered the Steinheim passage, whether a consistency run covered the writer's conclusion inside a citation, or whether a fact or consistency check covered the entry with the neighbouring DOI; for the museum check "its date and the version it checked were not recorded" (l. 232). Two readings follow. If the other axis ran over the passage and missed the error, the cases show that separate axes are needed. If it never covered the passage, they show only which axis found the error. The wording "was invisible to ..., because ..." argues the second reading from the type of error. Section 6 names no error class. Graded major because it concerns the answer to RQ2 and the result the Discussion calls central (l. 286). |
| Suggestion | In section 5, answer to RQ2 (l. 274 to 281), trace each of the six classes and each failure in Figure 6 to its origin: the assistant while writing, the assistant while checking, the author, or a source; where the origin was not recorded, say so and phrase the answer as errors that arose rather than as an answer to "introduce". Add errors of the checks themselves as a class. In "Separate axes" (l. 286 to 290), state for each of the three cases which other axes had run over the passage (run, date, version) and whether they reported it; where this is not documented, write "would not be visible to, by its type", and in the Abstract (l. 15) and l. 280 to 281 "was found by one axis". A design that answers RQ2: run all six axes over one fixed text (for instance chapter 1 of the Germany report in one version), record every finding with the axis that found it and its origin, and report the table of axis by error class with the overlaps. Add one sentence on RQ2 to section 6. |
| Status | verified (no origin given for the classes; failures in Figure 6 on the page image; no record of coverage by the other axes); inferred ("invisible to both" is not an observation that the other axes ran over that entry); assumption (which of the two readings applies, asked as a question) |
| Severity | major |
| Source | S4, SD |

**GB-44 The evidence for the first part of RQ3, that all 43 template rules name their incident, follows from the template convention and shows where the rules came from, not that the loops supported building the skills.**

| Field | Content |
|---|---|
| Check | P15, P31, P10 |
| Location | p. 15, l. 281 to 283; p. 17, l. 370 to 372; p. 5, l. 113 to 114 and 116; p. 13, l. 261; p. 2, l. 36 to 38 |
| Quotation | "Building skills in loops supported the building of skills, as far as the two templates show: all 43 of their rules name the incident they came from, and they carry these rules into every new project" |
| Concern | The method section sets as a convention that each template rule names its incident (l. 113 to 114: "Each of their rules names the incident it came from"). That all 43 rules (31 + 12 = 43, recalculated) do so therefore holds by construction, whatever the rules achieved. It shows that the loop produced rules and documented their origin, not that the skills got better. The qualifier "as far as the two templates show" narrows the scope, not the inference. What a rule is meant to do, prevent its incident from recurring, is not measured: no rule is followed to see whether its error class recurred after it was written, and Figure 6 shows six failures and their rules but not whether a failure recurred. That the templates "carry these rules into every new project" is stated as an effect; the only later project reported is this paper ("The present paper was itself set up with the document template", l. 116). Graded major because it concerns the answer to RQ3. |
| Suggestion | In section 4.6, date each of the 43 template rules and count from the logs the occurrences of the error class it addresses before and after that date (per report and per run); list the 43 rules with incident and date in an appendix or supplement (see also GB-39). Without such data, rephrase section 5 (l. 281 to 283) and section 6 (l. 371 to 372) as: "the loops produced 43 rules, each traced to an incident; whether they improved the skills was not measured". |
| Status | verified (convention l. 113 to 114 against l. 282 and l. 371 to 372; no recurrence data in the manuscript); inferred (that the measure does not test the effect) |
| Severity | major |
| Source | S4, SD |

**GB-45 "Counting instead of assuring" is stated without exception, but the manuscript's own incidents contradict it.**

| Field | Content |
|---|---|
| Check | P15 |
| Location | p. 15, l. 292; p. 13, l. 264 to 265; p. 14, Figure 6, rows 1 and 4; p. 12, l. 232; p. 13, l. 255 |
| Quotation | "Every finding carried a count or a location, and success was reported as measured values." |
| Concern | The manuscript reports a restoration "whose first reported restoration was itself unchecked and missed a second error" (l. 265), and Figure 6, row 4 shows the failure "Checked, no finding" without a source. In two results the date and version of the check "were not recorded" (l. 232, l. 255). The rules in Figure 6 came out of these incidents, so the sentence can hold at most for the period after those rules were written. Graded moderate because it bears on how far a reader can rely on the reported counts. |
| Suggestion | In section 5, "Counting instead of assuring", replace with: "After the rules in Figure 6 were written, every finding carried a count or a location, and success was reported as measured values; before that, a restoration was reported without a check (section 4.6)." |
| Status | verified (text; Figure 6 on the page image) |
| Severity | moderate |
| Source | S4 |

**GB-46 The Discussion recommends the file as master copy for counted checks, yet the paper itself switched to the online document alone, and it does not say how its own checks were made after that.**

| Field | Content |
|---|---|
| Check | P15 |
| Location | p. 16, l. 338 to 343; p. 7, l. 142 to 145 |
| Quotation | "For work built on counted checks, the file is the better master copy, and the online document the place where the author reads, comments and confirms. This paper itself left that setup on 27 September: to end the double work, only the online document has been kept since then, and the Markdown copy was frozen." |
| Concern | After 27 September the paper's own checks (75 proposals by 28 September, l. 144; each insertion "compared with the proposal in every copy of the text", l. 143) ran on the medium the same paragraph calls less suited. In that medium "a word count reported differences where the text was the same" (l. 338 to 339). A reader cannot tell how the counted checks after 27 September were made, or whether the recommendation was tested on this paper or set aside. |
| Suggestion | In section 5, "Documents or files", say how insertions were checked after 27 September (for example the character comparison of l. 339, or an export). Then either qualify the recommendation or explain why the paper departed from it. |
| Status | contradiction verified; method after 27 September not stated: verified |
| Severity | moderate |
| Source | S4 |

**GB-47 "The six figures of this paper" leaves out the graphical abstract; was it made by the same route?**

| Field | Content |
|---|---|
| Check | P4, P3 |
| Location | p. 16, l. 345 to 346; p. 2, Graphical abstract; p. 6, 8, 9, 12 and 14, Figures 1 to 6; p. 19, l. 391 |
| Quotation | "The six figures of this paper took the second route: each was redrawn from a script, and the scripts are kept with the figures in the project files." |
| Concern | Counted in the PDF, the paper holds seven embedded images: the graphical abstract on page 2 and Figures 1 to 6 on pages 6, 8, 9 (two), 12 and 14 (PP-02). The sentence covers Figures 1 to 6 and leaves open by which route the graphical abstract was made. On the page image it differs from Figures 1 to 6 in typeface, icon set and resolution (211 ppi against 200 ppi), which suggests a different origin but does not prove it. The Data availability statement refers to "the scripts that drew the figures" (l. 391). Since the sentence is offered as an example of the fixed order of routes, a reader cannot tell whether the graphical abstract followed it. |
| Suggestion | In l. 345, write "The six numbered figures and the graphical abstract of this paper took the second route" if it was also drawn by script; otherwise say how the graphical abstract was made and by which of the five routes. |
| Status | verified (count on the page images and in the PDF); assumption (different origin of the graphical abstract, asked as a question) |
| Severity | minor |
| Source | S4, AB |

**GB-48 The Limits say the genre selection and genre analysis skills were "each tested once or not at all", while section 4.5 reports a use of both. Which of the two was not tested?**

| Field | Content |
|---|---|
| Check | P2, P15 |
| Location | p. 17, l. 362 to 363; p. 13, l. 249 to 253; p. 18, Table A1, rows geo-exkursionsbericht-erstellen and geo-exkursionsbericht-typenanalyse |
| Quotation | "Two skills, for genre selection and genre analysis, were each tested once or not at all." |
| Concern | Section 4.5 reports that the Germany report v13 was measured against four candidate genres (genre analysis) and that the four "were chosen from the 15 types of the genre selection skill in a discussion" (l. 250 to 251). Each skill thus appears once, on the Germany report, and the reader cannot tell which one was tested "not at all". Two resolutions are possible: only the type list of the selection skill was consulted in a discussion, not its procedure; or, since Table A1 says the selection skill "chooses the genre among 15 types before writing", it was used in the Germany case only after writing and so never as designed. Graded moderate (the higher of the two instance grades): the statement bounds how far the two skills are tested, which matters for their transfer (l. 376). |
| Suggestion | In l. 362 to 363, state for each of the two skills how often it was run, on which report, and whether before or after writing; in l. 250 to 251, say whether the selection skill was run or only its type list consulted. |
| Status | verified (both uses in section 4.5; wording at p. 13 and p. 17); assumption (the resolution, asked as a question) |
| Severity | moderate |
| Source | S3, S4 |

**GB-49 The effort of the workflow is used as a limit and for a lighter version, but is given only in log entries, not in working time.**

| Field | Content |
|---|---|
| Check | P33 |
| Location | p. 17, l. 363 to 365; p. 16, l. 336 to 337 |
| Quotation | "The effort was large: 243 log entries for a pre-trip field guide."; "Keeping both doubled the work" |
| Concern | Log entries count events, not effort; "doubled" is not measured in time. The transfer question (l. 376) and the lighter version (l. 364 to 365) depend on effort; for the Germany report no effort figure is given at all. |
| Suggestion | In Limits, give working sessions or hours per report (from chat timestamps or the chat record), and the share spent on checking. |
| Status | verified |
| Severity | moderate |
| Source | SD |

**GB-50 The "lighter version" in Limits drops the axes and records that the manuscript shows to be necessary, and keeps the one element for which section 4 has no result.**

| Field | Content |
|---|---|
| Check | P15 |
| Location | p. 17, l. 364 to 365; set against p. 15, l. 286 to 290; p. 13, l. 244 to 247 and 256 to 258; p. 14, l. 279 to 280; p. 10, l. 186 to 187; p. 16 to 17, l. 347 to 353; p. 17, l. 374 to 376 |
| Quotation | "A lighter version would keep the register of repeated statements, one consistency run per chapter and one fact check per chapter, and drop most of the project files." |
| Concern | Each part of the proposal contradicts a result or a statement elsewhere in the manuscript. (1) It drops reference accuracy, yet "The DOI pointing to a neighbouring paper was invisible to both" (l. 289 to 290), that is, to the very fact and consistency checks the lighter version keeps; section 4.3 reports 13 errors. (2) It drops locality evidence, which in section 4.4 produced 26 proposals and 22 changes, and which the answer to RQ2 names as the check for regional statements transferred to single sites (l. 279 to 280). (3) It drops usefulness, although "The first critique found gaps that no correctness check could" (l. 256 to 257). (4) The clause "one consistency run per chapter" contradicts the order the skills prescribe, "then a new consistency run, because every improvement shifts numbers and cross-references" (l. 186 to 187), and Figure 5, where findings rose after large changes. (5) The clause "drop most of the project files" contradicts "everything that matters has to leave the chat and be kept in documents" (l. 347 to 348) and the 32 of 117 statements that could be traced only to a summary document (l. 350 to 351). (6) The one element kept by name, the register of repeated statements, is the one whose effect section 4 does not measure; the outlook proposes measuring it only later (l. 375 to 376). Graded moderate in the merge (the instance graded it major): the lighter version is a recommendation in the Limits; if the concern holds, no result and no answer to a research question changes, but the recommendation contradicts the results and the answer to RQ2 on which checks catch which errors, so a reader cannot trace it from them. |
| Suggestion | In Limits, either derive the lighter version from the results, keeping at least one pass of each axis that found errors only it could find, one consistency run after the last change, and the log and decision log, or mark it as an untested proposal and name the documented error classes it would leave uncaught. |
| Status | verified (each contrast in the text) |
| Severity | moderate |
| Source | S4 |

**GB-51 The Conclusions and the Abstract present the confirmation of the complete wording of every change as the setting of the results, but the manuscript limits it to this paper from 26 September 2026 and to tasks outside two exceptions.**

| Field | Content |
|---|---|
| Check | P15, P6 |
| Location | p. 17, l. 367 to 370; p. 1, l. 16 to 17; p. 7, l. 136 to 138 and 144 to 145; p. 6, l. 125 to 126; p. 10, l. 200 to 202 |
| Quotation | "with the author speaking, deciding, observing and confirming the complete wording of every proposed change before it was inserted" |
| Concern | The manuscript itself states that mechanical corrections and corrections released as a class skipped confirmation (l. 125 to 126), that the wording proposal was introduced on 26 September 2026 and that for the two reports its use "was not counted" (l. 137 to 138), and that the 75 counted proposals concern this paper (l. 144 to 145). The counts for the reports refer to Norway v100 of 26 September 2026 and Germany v15 (l. 200 to 202), and most dated results lie between 13 and 26 September (sections 4.1, 4.2, 4.3 and 4.5; see GB-17). "Every proposed change" and "complete wording" in section 6, and the sequence "the assistant proposes the complete wording, the author confirms it, and only then is it inserted unchanged" in the Abstract (l. 16 to 17), therefore describe more than the manuscript documents for the two cases. Graded moderate: the counts stay, but the conditions under which they arose are stated more broadly than shown. |
| Suggestion | In section 6 (l. 368 to 369) and the Abstract (l. 16 to 17), state the scope, for example "with the author confirming every change (step 5 in Figure 2) and, from 26 September 2026, the complete wording of every proposal", or name the 75 proposals for this paper as the counted evidence. |
| Status | verified |
| Severity | moderate |
| Source | S4, SD |

**GB-52 The two studies proposed for the Norway tour have no comparison condition.**

| Field | Content |
|---|---|
| Check | P9 |
| Location | p. 17, l. 373 to 376 |
| Quotation | "whether guided dictation yields as much content as recorded speech, and how the share of follow-up corrections changes with the register of repeated statements" |
| Concern | (1) The tour plans field notes "filled by dictation on site" (l. 374); a comparison with recorded speech needs recorded speech for the same observations, which the plan does not include. (2) The phrase "changes with the register" needs runs with and without the register; the register is part of the workflow throughout (Table A1, maintenance) and of the lighter version (l. 364). As planned, neither study can answer its question. |
| Suggestion | In 6, specify the designs: for (1), at alternating stops, or for the same stops, record free speech and guided dictation, and compare content by the measures of the cited surveys (word count, themes; Lenzner, Höhne and Gavras, 2024); for (2), compare follow-up corrections per change in comparable chapters edited with and without consulting the register. |
| Status | verified |
| Severity | moderate |
| Source | SD |

**GB-53 The outlook's self-improving skill removes the human role the Discussion calls necessary, and it assumes incidents are visible at the end of their task, which the manuscript's own incidents contradict.**

| Field | Content |
|---|---|
| Check | P15 |
| Location | p. 17, l. 376 to 379; p. 16, l. 328 to 330; p. 13, l. 264 to 265; p. 6 to 7, l. 128 to 133; p. 5, l. 114 to 116 |
| Quotation | "whether it could end each task by proposing, from the incidents of that task, the rule it lacked, so that the loop described in section 5 would run with the author's confirmation as its only human step." |
| Concern | The outlook is phrased as a question, which is appropriate. Two of the manuscript's own findings weaken it, and section 6 does not take them up. (1) The Discussion assigns the human "control and the test against real use, not the engine of the loop" (l. 328 to 329), and says the loop "still needs a human prompt" (l. 329 to 330). The proposal keeps confirmation but removes the test against real use. (2) Several documented incidents were not visible in the task where they arose. They surfaced later or by another route: wrong authors "caught only by comparing the first author on the DOI landing page" (l. 264); a restoration reported before it was checked (l. 265); a rule not carried by any skill, found "While this paper was revised" (l. 131 to 133); one missing log entry, two missing chat-record inputs and seven contradictions, found only at the chat change (l. 128 to 130); six different version counts across 10 files (l. 114 to 116). A skill that proposes rules "from the incidents of that task" would not have seen these. Graded moderate: no answer to a research question changes, but the outlook cannot be traced from the results. |
| Suggestion | In section 6, add the condition: rules proposed at the end of a task cover only incidents visible in that task. Incidents found in later review rounds still need the review round and the author's test against real use. Name the late-found incidents above as the cases the proposed study must be tested against. |
| Status | contrasts verified; whether such a skill would work: not claimed |
| Severity | moderate |
| Source | S4 |

**GB-54 The Data availability statement does not cover several records that the methods name as the basis of the results, gives no reason for withholding logs, work plans, check reports and figure scripts, and so leaves every count unverifiable for readers, against the paper's own rule.**

| Field | Content |
|---|---|
| Check | P12, P18 |
| Location | p. 19, l. 389 to 392; p. 10, l. 194 and 196 to 200; p. 5, l. 99 to 100; p. 6 to 7, l. 128 to 130 and 142 to 145; p. 4, Table 1, row "Project files"; p. 16, l. 345 to 348; p. 17, l. 350 to 353 and 361 to 362 |
| Quotation | "The project records of the two reports, namely logs, work plans, check reports and chat records, and the scripts that drew the figures are not published." |
| Concern | Section 3.5 names its sources with unusual openness, including that "32 of the 117 statements about the two projects checked for this paper rest on the summary document only" (l. 199 to 200). The Data availability statement does not follow this list. Of the eight source types in the parenthesis of l. 196 to 198, three are not mentioned (critiques, the summary document compiled from the chats, the chats themselves), and check reports are listed although Section 5 says that 32 statements could not be traced to "a saved check report" (l. 351 to 352). Not mentioned either are the list of 268 working patterns in 12 groups (l. 100), the check of the 117 statements (l. 199), the decision log (Table 1; l. 194; l. 353), the register of repeated statements, base data and locality table (Table 1), and the records of this paper's own project behind the counts of section 3.2 (75 proposals; one missing log entry, two missing inputs and seven contradicting statements, l. 128 to 130 and 142 to 145). "Chat records" is ambiguous: the manuscript uses "chat record" for a document introduced with template version 1.5.0 on 27 September 2026 (p. 19, l. 384 to 385), while the Norway records begin on 10 September (l. 198). The statement gives a reason for the reports ("not yet published; the author intends to make them publicly available", l. 391 to 392) but none for the other items, although logs, work plans, check reports and scripts describe documents, not persons, and the scripts "are kept with the figures in the project files" (l. 346). Every count in section 4 rests on these records ("Counts are those stated in the reports, logs and work plans", l. 200). The Limits name that "the counts are taken from the author's own records" (l. 361 to 362) but not the consequence that a reader cannot check any of them, which the paper's own principle asks for: "everything that matters has to leave the chat and be kept in documents that can be read, checked and exported" (l. 347 to 348). Graded moderate: the counts stay as reported, but a reader cannot verify them or tell which records exist. |
| Suggestion | Rewrite the Data availability statement (p. 19, l. 389 to 392) as a list that takes up every source of section 3.5, section 3.2 and Table 1 and gives for each: published with link (for example in the repository named at l. 389 or in an archive with a DOI), available on request, or not published with the reason. State whether "chat records" means the chat record documents since 27 September or the chats themselves, and name the summary document and the check of the 117 statements. Publish at least the check reports and log extracts behind each count of section 4, redacted where they hold personal content, or state in section 6 that the counts cannot be verified externally. |
| Status | verified (absence of each source from the statement at the cited lines; no reason stated; scripts kept, l. 346); inferred (that "chat records" cannot cover the chats before 27 September, from l. 198 and l. 384 to 385; that the withheld items do not concern persons, from their description in Table 1, section 3.2 and l. 345 to 346) |
| Severity | moderate |
| Source | S2, SD |

**GB-55 Conference and book entries in the reference list are not given in one form.**

| Field | Content |
|---|---|
| Check | P16 |
| Location | p. 20, l. 406 to 407 (Amershi), l. 429 to 431 (Christiano), l. 432 (Coe), l. 433 (Compton); p. 21, l. 440 to 443 (Deng), l. 444 to 446 (Dhuliawala), l. 455 to 457 (Gao); p. 22, l. 484 to 485 (Jansen), l. 499 to 500 (Lisle), l. 501 to 502 (Madaan), l. 503 to 505 (Manakul); p. 23, l. 515 to 518 (Ouyang), l. 535 to 537 (Rohanian); p. 24, l. 545 to 546 (Schön), l. 549 to 550 (Sutton) |
| Quotation | "New York: ACM, pp. 1-13." and "IEEE, pp. 109-120." and "in Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing, pp. 6465-6488." and "ISBN 0471829021." |
| Concern | Proceedings appear with publisher and place (Amershi, Deng), with publisher but no place (Jansen), and with no publisher (Gao, Manakul, Dhuliawala, Rohanian). Of the three NeurIPS papers, Ouyang and Madaan give pages and Christiano does not. Books give ISBN-13 (Coe, Lisle, Sutton) or ISBN-10 (Compton, Schön). Only uniformity was checked; conformity with a citation style is an optional check. |
| Suggestion | In the references, use one form for proceedings (publisher and place for all, or for none), add the page range to Christiano et al. (2017), and give ISBN-13 for Compton (1985) and Schön (1983). |
| Status | verified on the page images |
| Severity | minor |
| Source | S4 |

#### Minor corrections

| ID | Location | Quotation | Replacement | Source |
|---|---|---|---|---|
| KK-06 | p. 16, l. 317 to 318 | "The workflow keeps a human in the loop for every change, with the two exceptions named in section 3.2 (Mosqueira-Rey et al., 2023):" | "The workflow keeps a human in the loop (Mosqueira-Rey et al., 2023) for every change, with the two exceptions named in section 3.2:" | S4 |
| KK-07 | p. 16, l. 323 | "the permanent feedback between skill, report and review" | "the continuous feedback between skill, report and review" | S4 |
| KK-08 | p. 17, l. 374 | "Two questions should be measured then:" | "Two questions should then be answered by measurement:" | S4 |
| KK-09 | p. 19, l. 394 | "carried out the fieldwork and both excursion reports" | "carried out the fieldwork of the Germany tour, wrote the Germany excursion report and the Norway field guide" | S4 |

#### Verification log

| ID | Check | Checked | Values | Result |
|---|---|---|---|---|
| PP-45 | P4 | Citations against reference list in both directions, by Python over text.json, with the joins at line breaks checked by hand (Berdejo-Espinola at l. 314 to 315) | 74 entries (pp. 19 to 25, l. 401 to 578); each has at least one citation; each citation has an entry. Years and spelling match, including Güneş, Cesur and Çamur; Höhne; Neto de Carvalho; Mosqueira-Rey; Schön; González-Varo. "2026a" and "2026b" are distinguished for Topaz in the text (l. 48, l. 55); the preprints are marked "preprint" in the text (l. 48, l. 52) and as arXiv in the list | no finding |
| PP-46 | P4 | "et al." in short citations | Works with three authors are cited with all three names (12 works: Amano 2016, Güneş, Hadid, Hatvani, Höhne, Hosseini, Lenzner, Lisle, Manakul, Rao, Schegloff, Wieczorek); works with four or more as "et al." (for example Bhattacharyya 4, Gao 4, Hoffman 4, Revilla 2020 4, Sandve 4, Todd 4). The rule is applied without exception. The checklist's rule ("et al." above two authors) would differ for the 12 three-author works; the manuscript follows a consistent threshold of four. Whether this matches the target style is an optional check | no finding |
| PP-47 | P4 | Numbering and cross-references | Sections 1 to 6, 3.1 to 3.6, 4.1 to 4.6 without gaps; Figures 1 to 6 first cited at l. 108, 122, 158, 161, 214, 261 in order; Tables 1, 2, A1; Appendix A. References checked against their targets: section 3.3 (l. 132 to l. 181 to 183), section 5 (l. 183 to l. 349; l. 200 to l. 350 to 351; l. 263 to l. 274; l. 378 to l. 323 to 331), section 3.2 (l. 318 to l. 125 to 126; l. 358 to l. 126 to 130), section 4.2 (l. 279 to l. 233 to 234), section 4.6 (l. 279 to l. 264 to 265), section 4.4 (l. 280), section 3.6 (l. 395), Appendix A (l. 206, l. 390), Figure 5 (l. 331), Figure 6 rule carriers 2/3/1 (l. 262, legend l. 268 to 269, page image) | no finding |
| PP-48 | P4 | Repeated counts in segment 4 against their other occurrences, by Python | 31 + 12 = 43 (l. 114, 261, 282, 371); 68 + 6 + 1 = 75 (l. 144 to 145); Table A1 rows Research 4, Elicitation 1, Writing 4, Rules 1, Clarification 2, Checking 6, Steering 1, Maintenance 1 = 20, plus Framework 2 = 22 (l. 381, 383); eleven recurring rules counted 11 (l. 176 to 181); 243 log entries (Table 1, l. 363); 226 references (Table 1, l. 311); 32 of 117 (l. 199, l. 350); one in eight (l. 240, 274, 362); 13/211 = 6.16 % (l. 237) | no finding; the count of figures in GB-47 |
| PP-49 | P15 | Each proposal in the outlook, held against the manuscript's own findings | (1) results report after the Norway tour, field notes by dictation: against l. 89 to 91 and l. 302 to 304, consistent. (2) whether guided dictation yields as much content as recorded speech: against l. 155 to 156 (share not measured) and l. 303 to 304 (not measured), consistent; design see GB-52. (3) share of follow-up corrections with the register: no result in section 4 on the register, consistent as a proposed study, but in conflict with Limits (GB-50). (4) transfer to other authors and sciences: against Limits l. 361 to 362, consistent. (5) self-improving skill: against l. 128 to 133, 264 to 265, 328 to 330, see GB-53. Lighter version in Limits: see GB-50 | no finding for (1), (2), (4); limits already disclosed: two reports, one author, one assistant, counts from the author's records (l. 361 to 362) |
| PP-50 | P15 | Frameworks and core terms from Introduction and research questions in Discussion and Conclusions | Human in the loop: l. 317 to 322. RLHF analogy (Figure 1 legend l. 121): l. 323 to 331. Separating observation from interpretation (l. 29): l. 303. Regional statement transferred to a point (l. 32): l. 296 to 299. RQ1 "help", "fall short": l. 271 to 274, l. 367. RQ3 "iterative", "building of skills", "quality of the reports": l. 281 to 285, l. 371 to 372. RQ2 "introduce": see GB-43. Related work and gap: see GB-41 | no finding beyond GB-43 and GB-41 |
| PP-51 | P15 | Verbs in Discussion and Conclusions against what the evidence supports | Hedged and in line with the results: "indicated ... but not shown" (l. 284), "remains to be shown" (l. 372), "In the author's view ... not counted" (l. 296 to 297), "was not measured" (l. 304). Stronger than the evidence: "lay in" (l. 367, GB-42), "was invisible to" (l. 287 to 290, GB-43), "Every finding carried" (l. 292, GB-45) | no finding beyond the ones named |
| PP-52 | P16 | Language of segment 4 and uniformity of the reference list on the page images of pp. 14 to 25 | British spelling used throughout (formalise, summarised, practised, colour, judgement, licence, analysed); no American -ize spelling outside titles of cited works. Reference list: italics for journal and book titles uniform; page ranges with hyphen throughout; "Accessed: 26 September 2026" uniform for the 7 entries with URL; DOI as https://doi.org/ throughout. Splits in the extracted text inside Table 2 and Table A1 are artefacts of extraction (confirmed on the page images) and not findings. Line breaks in URLs fall at hyphens that belong to the URL or DOI (l. 447 to 448, 482 to 483, 495 to 496, 577 to 578). In entries, 8 works are truncated with "et al." after three names (Amershi, Binz, Casper, Haynes, Liang, Madaan, Ouyang, Zizka), while others list up to 12 names (Deng). Whether a consistent threshold lies behind this cannot be judged without the full author lists, which is an optional check | no finding beyond GB-55 and the minor corrections KK-02, KK-05 and KK-07 to KK-09 |
| PP-53 | P17 | location of disclosed limits | RQ3 comparison and axis frequencies only in the discussion; 30 lost inputs only in the discussion; genre skills only in Limits | findings only where consequences are not drawn: GB-43, GB-18, GB-23; the others are placed at the claim they limit |
| PP-54 | P9 (outlook) | transfer to other authors and field sciences; self-improving skill | l. 376 and l. 377 to 379: no design given; both stated as open questions | no finding here; the proposal of a self-improving skill is taken up in GB-53 |
| PP-55 | P12 | The two reports against the Data availability statement | Germany report v13 (l. 249), v15 (Table 1, l. 201), 211 entries on 18 September (l. 237); Norway report v17, v47, v59, v63, v64, v67, v100 (Figure 5), v67 (l. 244), v100 (l. 92, 201); statement: "not yet published; the author intends to make them publicly available" (l. 391 to 392) | no finding under P12: a reason is given. The statement does not say which version will be published; whether the counts can be reproduced on v13, v67 and earlier versions is taken up in GB-17 and GB-54 |

## Optional checks

| Area | What it needs | Responsible | Run |
|---|---|---|---|
| DOI resolution | one fetch per reference entry with a DOI | `science-quellenapparat-pruefung` | no |
| Citation style | the name of the style | `science-zitierstil-harvard-ctr` or the style rules of the journal | no |
| AI declaration against publisher policy | the target publisher's policy on AI use | this review, on request | no |
| Relation to the authors' own prior work | the authors' prior work | this review, on request | no |
| Journal requirements | the author guidelines of the target journal | this review, on request | no |
| Subject accuracy | access to the sources of the checked statements and a choice of sections | `science-faktenbeleg-pruefung`, `geo-frage-belegbasiert-klaeren` | no |

## Limits of this review

- Checked version: Talk_Check_Decide_A_Skill-Based_Workflow.pdf, 25 pages, SHA-256 f8190be6c06586eb5068aee0c70760a5413a6378ea291cf7e89bed2cf10b415e.
- Sources not readable: full text of Topaz et al. (2026a), abstract only; the letter Topaz et al. (2026b), read through secondary reports only; Hatvani, Mudelsee and Kern (2024), fetch error; Ralph et al. (2025); full texts of Revilla et al. (2020) and Revilla and Couper (2026), abstracts only; the books Compton (1985), Coe (2010) and Lisle, Brabham and Barnes (2011). The repository https://github.com/nordie69/Talk-Check-Decide was not opened by any instance, so the published skills and their state were not compared with Appendix A. Value claims in the Discussion that rest on literature (Rohanian et al., 2023; Parasuraman and Manzey, 2010; Amano et al., 2023; Ralph et al., 2025) were not checked against their sources, since the checklist of segment 4 has no fact check.
- Findings with status assumption: 12 of 55, each for a partial statement; these parts are put as questions to the author.
- Optional checks run: 0 of 6.
- Instances omitted: none.
- Discarded findings: 0. All 68 substantive findings, 14 minor corrections and 55 verification log entries of the six instances had their mandatory fields; none was returned or discarded.
- Merge: the 68 instance findings became 54 findings, plus 1 finding from the merge (Source ZF), 55 in all; 14 minor corrections became 9, two of them absorbed by findings that name the same place and subject. One finding was regraded from major to moderate by the counter-test for major findings (GB-50). Of 35 hints outside the checklists, 3 led to the finding with Source ZF, 18 were already covered by findings, corrections or log entries, 6 were not adopted after checking the manuscript, 7 concern optional checks or the limits above, and 1 was a statement without a claim.
- Pairs with overlapping location: `formatpruefung.py --paare` listed 226 pairs before the merge; 22 were merged, 3 were resolved as differing readings, and 201 were left separate as different subjects at the same place. After the merge it lists 129 pairs, all left separate as different subjects.
- Lines between the printed margin numbers 165 and 170 on page 9 (end of the Figure 4 caption, heading 3.3) cannot be counted with certainty; locations there are given by element. All other locations were confirmed at the printed margin numbers.
