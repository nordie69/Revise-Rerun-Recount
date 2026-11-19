# Review report: Listen. Answer. Memorize. Building and Running Verified Learning Paths for Geoscience Self-Study with an AI Assistant

| Field | Value |
|---|---|
| Manuscript | Mohr, S. (2026) Listen. Answer. Memorize. Building and Running Verified Learning Paths for Geoscience Self-Study with an AI Assistant; manuscript prepared for a Copernicus journal, no DOI or manuscript number in the file |
| Checked version | Listen_Answer_Memorize_Copernicus.pdf, 26 pages, SHA-256 9065d593cbc95029707b6936346f193d31cfedcd4e11382fbbd43629428595aa |
| Date | 2026-10-16 |
| Language | English |
| Review instances | Segments 1 to 4, figures (science-review-abbildungen 1.2.0), study design (science-review-studiendesign 1.2.0); the six review instances ran as separate agents, and the merge ran in a further separate agent; no instance omitted |
| Note | Manuscript and review were produced with the same language model (Claude Opus 5.5, Sect. 3.7 of the manuscript); this review is a check by the same model family |

## Summary

The manuscript reports a single-case self-experiment, placed by its author closest to autoethnography, in which one adult learner, who is also the developer, built with an AI assistant (Claude Opus 5.5) the skill lernpfad-sitzungen and learned with it. The skill cuts a learner-supplied fact document into sessions of whole paragraphs, aimed at up to about 550 words, with three questions each, whose expected answers of 5 to 30 words a check script finds word for word in the excerpt; in a voice call the assistant reads the excerpt aloud, asks the questions, grades the spoken answers tolerantly and keeps a learning record, from whose list To review review sessions are built on request. The study covers five cases (fact documents on southern Norway, the geological eras, the geology of Germany and volcanology, and a narrative version of the eras document), six learning paths in seven check runs, all passed, three only after exclusions; 25 sessions on two cases with 75 graded answers, 23 sessions entirely in the voice call, and two completed review sessions, between 27 September and 13 October 2026. Rules for the assistant were revised from incidents across skill versions 2.1.0 to 2.6.6, though no session ran under 2.6.5 or 2.6.6. Success is judged by the learner's own account against three criteria; there is no control condition and no claim about retention.

## Strengths

1. The check script makes the binding of every learning path to its fact document countable, and the counts hold across the paper: anchors are two per session and expected answers three per session in all seven runs, and words, sessions and questions per path are identical in Table 1, Table 4 and Fig. 1 (PP-52, PP-29, PP-55). A reader can therefore check for each of the six paths that every expected answer occurs word for word in its excerpt; what lies before this link, the check of the fact document, is a separate matter (GB-19).
2. The manuscript discloses its own limits and incidents where it reports the results: the grades are declared process data, comparisons of modes, paths and rule versions are explicitly not drawn, the self-analysis of the chats and the compacted transcript are named, and the skill version of sessions 4 to 11 is marked as inferred (PP-70, PP-56, PP-59, PP-61). This keeps most verbs of the Discussion within the evidence; the exceptions are listed as findings (GB-41, GB-39).
3. The figures are drawn from the same data as the tables: measured at 300 dpi, the stacked bars of Fig. 4 reproduce Table 5 answer by answer, the bars of Fig. 1 are proportional to the session counts of Table 1, the dates in Fig. 4 and Fig. 5 match Sect. 4.1 and Table A2 where they are drawn, and no label is smaller than 6.3 pt (PP-02, PP-30, PP-60, PP-62). A reader can take counts and dates from the figures; the gaps are omitted versions, not wrong values (GB-26, GB-31).
4. The related work is reported close to its sources: the values and statements on retrieval practice, spacing, tutoring with supplied solutions, hallucination types, reading while listening, self-regulated learning and narrative were found in the sources themselves, and every citation has an entry and every entry a citation, with matching years and spellings (PP-09, PP-10, PP-13, PP-20, PP-81). Sect. 2 can be checked by a reader, with two omitted moderators and two missing works as exceptions (GB-04, GB-05, GB-06).

## Weaknesses

1. The attribute verified is not shown for the material that was learned: Sect. 4.1 reports no check of the fact documents on southern Norway and the geological eras, no reported check has an estimate of the errors it left, and the completeness of the narrative version rests on one unspecified AI check (GB-19, GB-30). Report the checks of all fact documents with a sample checked against the sources independently of the building chat, or restrict verified to the binding of learning path to fact document.
2. What happens in the call is not audited, and the scope of the verbatim binding is stated wider than the procedure: reading and asking in the 25 sessions were not compared with excerpt and learning path, answers to deviating questions and answers after hints are counted in Table 5 without a mark, review sessions admit general knowledge, and the Methods describe version 2.6.6, under which no session ran (GB-35, GB-24, GB-36, GB-12). Audit the calls where the chats hold the spoken output, mark deviating answers, restrict the claims to regular sessions and describe the procedure as it ran.
3. The answers to RQ2 and RQ3 are not traced to their evidence: two rules are said to come from incidents that the Results do not report and Table 6 has no selection rule, RQ3 asks about mastery that the design does not measure, the third and fourth respects of the gap are not taken up again, and the proposed retention test inherits these weaknesses (GB-34, GB-02, GB-33, GB-40). Report the incidents or drop the claims, reword RQ3 to what the design answers, return to the literature of Sect. 2 in the Discussion, and give the retention test a design that can answer its question.
4. Several counts and data cannot be reproduced from the paper: the data statement covers only the skill package, the model-based analysis chain is not documented, Table 4 lacks dates, script and fact document versions, the To review balance for version 6 does not close without an unstated reading, and the crediting of sessions is not described (GB-42, GB-15, GB-23, GB-28, GB-14). Publish the data that concern no persons, add the missing columns and state the rules behind the counts.

## Findings by segment

### Segment 1: Abstract, introduction, related work (p. 1 to 4)

#### Substantive findings

**GB-01 Five works with three authors are cited with all three names, where the check rule requires "et al." for more than two authors.**

| Field | Content |
|---|---|
| Check | P4 |
| Location | p. 2, l. 36 (Cheek, LaDue and Shipley, 2017); p. 2, l. 37 to 38 (Landy, Silbert and Goldin, 2013); p. 3, l. 57 (Agarwal, Nunes and Blunt, 2021); p. 3, l. 59 to 60 and p. 20, l. 436 (Latimier, Peyre and Ramus, 2021); p. 12, l. 252 (Ellis, Adams and Bochner, 2011) |
| Quotation | "(Cheek, LaDue and Shipley, 2017)"; "(Landy, Silbert and Goldin, 2013)"; "(Agarwal, Nunes and Blunt, 2021)"; "(Latimier, Peyre and Ramus, 2021)"; "(Ellis, Adams and Bochner, 2011)" |
| Concern | All short citations otherwise match their entries in year and spelling (PP-81). The manuscript applies one convention consistently: up to three authors in full, "et al." from four on (Dunlosky et al., Ji et al., Bastani et al., Kestin et al., Li et al., Mar et al., Nückles et al., Zhang et al., Wilson et al., Denojean-Mairet et al.). The check rule for short citations used here calls for "et al." for more than two authors, which these six citations do not follow. Whether the journal's house style or the author's Harvard convention applies is for the authors and the editor to decide. |
| Suggestion | Check the target journal's rule for in-text citations; if it uses "et al." from three authors on, change the six citations to "Cheek et al., 2017", "Landy et al., 2013", "Agarwal et al., 2021", "Latimier et al., 2021" (twice) and "Ellis et al., 2011". |
| Status | verified (occurrences on the page images); the journal rule is not checked here (citation style is an optional check). |
| Severity | minor |
| Source | S4 |

**GB-02 RQ3 asks how the record tracks what the learner has not yet mastered, while the design declares the grades that fill the record not to be a measure of learning.**

| Field | Content |
|---|---|
| Check | P10 |
| Location | p. 3 l. 47 to 48; p. 12 l. 256 to 257; p. 18 l. 391 to 393; p. 20 l. 424 to 425 |
| Quotation | "How does a learning record kept by the AI assistant track what the learner has not yet mastered"; "are not used as a measure of learning success"; "the data show how the record is kept, not what it achieves" |
| Concern | The manuscript is consistent in treating grades as process data, and the discussion of RQ3 says so. RQ3 itself, however, asks for a relation between the record and mastery. The To review list is filled from grades given by the model in the call, without a second grader, so the design can describe what the list contains (35 and 14 entries) but not whether it tracks what is not mastered. The question is causal or validating in type; the design is descriptive. Moderate: the answer actually given to RQ3 stands, but the question as posed is not answerable with this design. |
| Suggestion | Reword RQ3 in Sect. 1 (p. 3 l. 47 to 48) to what the design answers, for instance "How does a learning record kept by the AI assistant collect the questions answered incorrectly or partially correctly, and how are review sessions built from it?" If the original wording is kept, add a design that can answer it: a delayed retest of all 75 asked questions, comparing entries in To review with correctly answered questions, graded by a second grader blind to the original grade. |
| Status | verified (wording and disclaimers); inferred (that the design cannot answer the question as worded) |
| Severity | moderate |
| Source | SD |

**GB-03 The gap of Sect. 2 is stated without any account of how the literature was searched, and Sect. 4.3 relies on it to set aside a comparison.**

| Field | Content |
|---|---|
| Check | P28 |
| Location | p. 4, l. 97 to 108; p. 14, l. 319 to 320 |
| Quotation | "Taken together, this work leaves a gap that the present paper addresses, in five respects." (l. 97); l. 103 to 104: "none of the studies reviewed here, however, combines listening alone with spoken answers in self-study, as the voice sessions studied here do"; l. 319 to 320: "Since none of the studies reviewed in Sect. 2 combines listening alone with spoken answers in self-study, these requests cannot be set against them" |
| Concern | The manuscript words its gap carefully as "none of the studies reviewed here", which limits the claim to its own selection. It does not say how that selection was made: no databases, search terms, period or date of search are given anywhere in Sect. 2 or Sect. 3.6. The restriction to "the studies reviewed here" therefore does not make the gap checkable, because a reader cannot tell whether the absence of a study reflects the literature or the selection. The gap is also used as an argument: in Sect. 4.3 the learner's requests to hear the excerpt again "cannot be set against" the literature because no reviewed study combines listening with spoken answers. Three own searches (queries in PP-26) found work on spoken computer tutoring that does combine listening to a tutor with spoken answers (GB-05), so the gap in its third respect is at least narrower than stated. |
| Suggestion | Add to Sect. 2 (or Sect. 3.6) a short statement of the literature search: databases or search engines used, search terms for each of the five respects, period covered and date of search; then reword the five respects at l. 97 to 108 and l. 319 to 320 so that each states what the search found, and revise the third respect in the light of GB-05. |
| Status | verified (absence of a search description checked in Sect. 2, Sect. 3.6 and Sect. 3.7 of the manuscript) |
| Severity | moderate |
| Source | S1 |

**GB-04 The summary of Clinton-Lisell (2022) leaves out the two moderators under which reading beat listening, and both match the design of the voice sessions.**

| Field | Content |
|---|---|
| Check | P13 |
| Location | p. 4, l. 101 to 102; consequence at p. 14, l. 319 to 320 |
| Quotation | "listening alone has been compared with reading in many studies, with no reliable overall difference in comprehension (Clinton-Lisell, 2022)" |
| Concern | The overall result is reported correctly: the meta-analysis (46 studies, N = 4,687) found that "the overall difference between reading and listening comprehension was not reliably different (g = 0.07, p = .23)". The same abstract, however, reports that "Reading was beneficial over listening when the reading condition was self-paced" (g = 0.13, p = .049) and that "Reading also had a benefit when inferential and general comprehension rather than literal comprehension was assessed". Both conditions describe this study: the learner could work through a learning path "either on screen or interactively by voice" (p. 6, l. 131) and listened in 23 of 25 sessions (l. 322 to 323), and from version 2.5.0 on the questions aim at "relations and events instead of numbers, dates and names" (l. 40 to 41), which is closer to inferential than to literal comprehension. Reported without these moderators, the source reads as if listening cost nothing in comprehension; for the conditions of this study the source points the other way. The manuscript handles the parallel moderator correctly for Clinton-Lisell (2023), where it reports that the benefit of reading while listening was limited to experimenter-paced reading (l. 74 to 76); the same care is missing for the 2022 paper. Severity moderate, not major: the manuscript makes no claim about comprehension or retention, so its results stand, but a reader cannot judge from Sect. 2 what the literature says about the trade-off of the listening mode that RQ2 studies. |
| Suggestion | In Sect. 2, l. 101 to 102, add the two moderators of Clinton-Lisell (2022) (reading advantage when reading is self-paced, g = 0.13, and for inferential and general comprehension), and in Sect. 5 state that the voice mode trades a known small comprehension advantage of self-paced reading for the possibility of learning on the move. |
| Status | verified (abstract of the source, read by instance S1 through the publisher record on x-mol; full text not read; the record could not be reopened during the merge) |
| Severity | moderate |
| Source | S1 |

**GB-05 Work on spoken dialogue tutoring, in which a computer tutor and a learner talk by voice and learning gains are compared with typed tutoring, is missing from the third respect of the gap.**

| Field | Content |
|---|---|
| Check | P14 |
| Location | p. 4, l. 101 to 104; p. 14, l. 319 to 320 |
| Quotation | "answering aloud during retrieval practice has been compared with typing, with few differences (Putnam and Roediger, 2013); none of the studies reviewed here, however, combines listening alone with spoken answers in self-study, as the voice sessions studied here do" |
| Concern | The manuscript compares its voice sessions with laboratory studies of reading versus listening and of typed versus spoken recall. It does not cite the line of work on spoken dialogue tutoring, which studied one learner at a time working with a computer tutor by voice. Litman et al. (2006) ran two experiments comparing typed and spoken tutoring dialogues, one human-human and one human-computer, and measured learning gains and time on task; according to their abstract, changing from text to speech "caused changes in the learning gains" in human tutoring, while for computer tutoring the change "made less difference". This work anticipates the combination that the third respect claims as unstudied (a learner hears a tutor and answers aloud, one to one) and gives a result on it for computer tutors, which bears on how RQ2 is framed. It differs from the present study in that the tutor did not read a fixed excerpt and the setting was a laboratory, not self-study on the move; these differences are what the gap could then name. Whether the computer tutor in the spoken condition delivered its turns by synthesized speech was not read in the source; the authors could clarify this when they place their study against it. Check against the reference list: Litman et al. (2006) is not in the reference list (p. 24 to 26). |
| Suggestion | In Sect. 2 (third respect, l. 101 to 104), add Litman, D., Rosé, C.P., Forbes-Riley, K., VanLehn, K., Bhembe, D. and Silliman, S. (2006) 'Spoken versus typed human and computer dialogue tutoring', International Journal of Artificial Intelligence in Education, 16, pp. 145-170 (report version: https://www.inf.ed.ac.uk/publications/report/1105.html), and restate the gap as the difference between spoken dialogue tutoring and verbatim reading of a learner-supplied excerpt in self-study; adjust l. 319 to 320 accordingly. |
| Status | verified (content of the source abstract; title, authors, journal, volume and pages confirmed again during the merge on the report page of the University of Edinburgh); inferred (that the computer tutor spoke its turns, not read) |
| Severity | moderate |
| Source | S1 |

**GB-06 An autoethnography of a single adult learner who learned with ChatGPT as tutor precedes the fifth respect of the gap and the methodological framing, and is not cited.**

| Field | Content |
|---|---|
| Check | P14 |
| Location | p. 4, l. 106 to 108; p. 11, l. 250 to p. 12, l. 252 |
| Quotation | "Fifth, the studies concern school classes, courses and samples of many learners; this paper describes the self-study of a single adult learner in the geosciences, who is also the developer of the learning environment." (l. 106 to 107); l. 250 to 251: "Methodologically, it comes closest to autoethnography" |
| Concern | The fifth respect contrasts the present single-learner study with studies of classes and samples, and Sect. 3.6 places it close to autoethnography, citing only the general overview by Ellis, Adams and Bochner (2011). Gandhi and Muldner (2025) report an autoethnography in which one experienced educator, a novice programmer, learned Python with ChatGPT-4o as tutor over five sessions. They found that ChatGPT could not reliably assess the learner's understanding or adapt sessions to it, so that the learner had to monitor himself to decide when to advance or seek review, and they describe ChatGPT as a "learning-mediating tool rather than a more knowledgeable other". The study thus anticipates the design (a single adult learner, autoethnographic, an LLM tutor in self-study) and reports on the very function that the present learning record and review queue take over from the learner (RQ3) and on assessment by the model (Sect. 5, l. 422 to 425). It differs in that the learner did not build the tool or bind it to a verified source. Check against the reference list: not in the reference list (p. 24 to 26). |
| Suggestion | In Sect. 2 (fifth respect, l. 106 to 107) and in Sect. 3.6 (l. 250 to 252), cite Gandhi, A. and Muldner, K. (2025) '"That's not the way I would explain it": a teacher-researcher's autoethnography of learning to program with ChatGPT', ICER 2025, 21st ACM Conference on International Computing Education Research, Charlottesville, VA (https://icer2025.acm.org/details/icer-2025-papers/27/-That-s-Not-the-Way-I-Would-Explain-It-A-Teacher-Researcher-s-Autoethnography-of-Le), and restate the fifth respect as the difference to it: the learner as builder of the tool and the binding to a verified fact document. |
| Status | verified (content of the conference abstract page, read by instance S1; title confirmed again during the merge on the ICER 2025 profile page of the first author; full paper and DOI not read) |
| Severity | moderate |
| Source | S1 |

#### Minor corrections

| ID | Location | Quotation | Replacement | Source |
|---|---|---|---|---|
| KK-01 | p. 2, l. 36 | "Learners often misjudge the ages of geological events by orders of magnitude" | "Learners and teachers can misjudge the ages of geological events by several orders of magnitude"; the source says they "can be off by several orders of magnitude" | S1 |
| KK-02 | p. 3, l. 58 to 59 | "across 29 studies, spaced retrieval practice showed a strong benefit for retention over massed retrieval practice (g = 0.74)" | "in a meta-analysis of 29 studies, spaced retrieval practice showed a strong benefit for retention over massed retrieval practice (g = 0.74, 39 effect sizes), whereas expanding intervals were not superior to uniform ones (g = 0.034, 54 effect sizes)"; the 29 studies are the total over both subsets, the g = 0.74 refers to the first subset only | S1 |
| KK-03 | p. 4, l. 76 to 77 | "Voice assistants and smart speakers have only recently begun to be used in schools and universities" | "In 2020, voice assistants and smart speakers had only just begun to be used in schools and universities"; the source is six years older than the manuscript and states the situation of 2020 ("have just started to be used") | S1 |

#### Verification log

| ID | Check | Checked | Values | Result |
|---|---|---|---|---|
| PP-01 | P29 | Inventory of all figures, with references in the text (margin numbers confirmed on the page images) | Graphical Abstract, p. 2, schema, no caption, no reference in the text. Fig. 1, p. 6, overview schema with bars, caption l. 121 to 124, cited l. 112. Fig. 2, p. 7, flow diagram, caption l. 151 to 155, cited l. 141. Fig. 3, p. 9, schema declared schematic, caption l. 185 to 188, cited l. 173, 182, 302. Fig. 4, p. 15, stacked bar chart over a date axis, caption l. 331 to 334, cited l. 322 and in the Fig. 5 caption. Fig. 5, p. 17, timeline, caption l. 358 to 363, cited l. 354. Fig. 6, p. 18, three-column schema, caption l. 377 to 379, cited l. 365. Fig. 7, p. 19, chain diagram, caption l. 406 to 411, cited l. 387, 394, 402 to 403, 425. Fig. 8, p. 21, two-loop schema, caption l. 456 to 461, cited l. 450 | no finding; numbering 1 to 8 continuous, first citations in ascending order, every numbered figure cited in the text of its own section |
| PP-02 | P29 | Font size of the smallest labels in print size (cap height or ascender height in the 300 dpi image) | GA: 21 px = 7.0 pt ("session", "script-checked"). Fig. 1: digits "31" 21 to 22 px = 7.0 to 7.3 pt, "Southern" 22 px = 7.3 pt, "none" 23 px = 7.7 pt. Fig. 2: lowercase "next session" x-height 17 px, ascender 19 px = 6.3 pt. Fig. 3: "compared" ascender 21 px = 7.0 pt. Fig. 4: y-axis digits 21 to 22 px = 7.0 to 7.3 pt, x-axis "28 Sep" 20 px = 6.7 pt, legend "Southern" 21 px = 7.0 pt, session numbers (rotated) 21 px width = 7.0 pt, version labels and triangle numbers 20 px = 6.7 pt. Fig. 5: axis "27 Sep" 21 px = 7.0 pt, version labels 21 to 22 px = 7.0 to 7.3 pt, grey italic note ascender 22 px = 7.3 pt, rule labels 22 px = 7.3 pt. Fig. 6: italic note ascender 21 px = 7.0 pt, box text 23 px = 7.7 pt. Fig. 7: grey italic note ascender 22 px = 7.3 pt, annotations 22 to 23 px = 7.3 to 7.7 pt. Fig. 8: note 22 px = 7.3 pt | no finding; smallest measured 6.3 to 6.7 pt, all above 6 pt (method error at most 0.6 pt) |
| PP-03 | P29, P3 | Graphical Abstract against the text | Five stages fact document, learning path, listen, answer, memorize = l. 49 to 50 and Sect. 3.5; "expected answers verbatim in the session excerpt" = l. 33; dashed "on request" for review = l. 222; dotted arrows from learning path and from the session to the rules box, labelled "incidents led to new rules" = l. 18 to 19 (incidents in building and in sessions) | no finding |
| PP-04 | P13 | Ji et al. (2023), p. 2, l. 31; p. 3, l. 62 to 64 | Source Sect. 2.1: intrinsic, "output that contradicts the source content"; extrinsic, "output that cannot be verified from the source content", "can neither be supported nor contradicted by the source" | no finding |
| PP-05 | P17 | location of limitations | single learner p. 2 l. 33; period p. 12 l. 258; no control p. 1 l. 20; process data p. 12 l. 256 | no finding apart from GB-12 and GB-07 |
| PP-06 | P13 | Cheek, LaDue and Shipley (2017), p. 2, l. 36; Landy, Silbert and Goldin (2013), p. 2, l. 37 to 38 | Cheek: learners and teachers "can be off by several orders of magnitude" (ERIC full text). Landy abstract: about half estimated linearly; "nearly all the remaining participants placed 1 million approximately halfway between 1 thousand and 1 billion"; "many adults" is covered | no finding; wording of Cheek in KK-01 |
| PP-07 | P13 | Dunlosky et al. (2013), p. 3, l. 52 to 55 and 60 to 61: ratings and reasons | Source abstract (APS page): practice testing and distributed practice high utility because "they benefit learners of different ages and abilities" and boost performance "across many criterion tasks and even in educational contexts"; rereading among techniques that "do not consistently boost students' performance"; recommends "practice testing instead of rereading"; elaborative interrogation short of high utility because evidence is limited and it has "not been adequately evaluated in educational contexts" | no finding |
| PP-08 | P13 | Agarwal, Nunes and Blunt (2021), p. 3, l. 55 to 57 | Source: 50 experiments; "the majority of which (57%) revealed medium or large benefits"; "only 6% of experiments were conducted in non-WEIRD countries" | no finding |
| PP-09 | P13 | Latimier, Peyre and Ramus (2021), p. 3, l. 57 to 60 | Source: 29 studies; subset 1, 39 effect sizes, g = 0.74 spaced vs massed; subset 2, 54 effect sizes, g = 0.034, no significant difference expanding vs uniform | no finding on the values; denominator wording in KK-02 |
| PP-10 | P13 | Bastani et al. (2025), p. 3, l. 64 to 67 | Source (PDF copy, version label not shown): "nearly 1000 students"; GPT Base correct "only 51% of the time" under repeated queries; exam 17% lower than control for GPT Base; GPT Tutor prompt contained teacher-written solutions and common mistakes, with incremental hints; harm "largely mitigated". Not reported in the manuscript: practice gains of 48% (GPT Base) and 127% (GPT Tutor) while access lasted; the omission does not change the cited statement on harm after removal | no finding |
| PP-11 | P13 | Kestin et al. (2025), p. 3, l. 67 to 69 | Source (PMC full text and PDF copy): "avoided relying solely on GPT-4"; "enriched our prompts with comprehensive, step-by-step answers"; "students learn more than twice as much in less time" than in the active learning class; median time on task 49 min vs 60 min assumed | no finding |
| PP-12 | P13 | Li et al. (2025), p. 3, l. 69 to 71 | Source abstract: RAG retrieves "relevant information from an external knowledge base"; challenges include hallucination; future directions include "mitigating hallucinations" | no finding |
| PP-13 | P13 | Clinton-Lisell (2023), p. 3, l. 73 to p. 4, l. 76 | Source (ERIC PDF): 30 studies, N = 1945, 62 effect sizes; overall g = .18 ("trivial"); experimenter-paced g = 0.41; self-paced g = 0.06, p = .34, "no reliable effects" | no finding |
| PP-14 | P13 | Terzopoulos and Satratzemi (2020), p. 4, l. 76 to 78 | Source: abstract "have just started to be used in schools and universities"; Sect. 7 "still at an early stage of research", "results are limited, incomplete and unorganized", "the lack of many languages" | no finding on content; tense in KK-03 |
| PP-15 | P13 | Denojean-Mairet et al. (2024), p. 4, l. 79 to 81 | Source: 30 s to 5 min (Jahnke et al., 2020); less than 10 min (Torgerson and Iannone, 2019); also up to 15 min (Díaz Redondo et al., 2021; Garcia et al., 2022); no consensus on duration. The 15-minute definitions are not reported; the omission does not change the reading in Sect. 5, l. 418, since 5 to 10 min lies within either range | no finding |
| PP-16 | P13 | Traxler (2007), p. 4, l. 81 to 82 | Source: "It may mean learning whilst traveling, driving, sitting, or walking"; "Mobile learning allows these students to exploit small amounts of time and space for learning" (second passage from a later section) | no finding |
| PP-17 | P13 | Panadero (2017), p. 4, l. 83 to 84 | Source introduction: "Self-regulated learning (SRL) is a core conceptual framework to understand the cognitive, motivational, [and emotional aspects of learning]" | no finding |
| PP-18 | P13 | Nückles et al. (2020), p. 4, l. 84 to 86 | Source: written text as "external representation and memory aid"; "the journal writing needs to be instructionally supported" | no finding |
| PP-19 | P13 | Zhang et al. (2022), p. 4, l. 86 to 88 | Source abstract: 38 Chinese EFL students, 112 journal entries; journaling "raised students' awareness" and "may have contributed to an increase in their use" of strategies | no finding |
| PP-20 | P13 | Achuthan (2025), p. 4, l. 88 to 90 | Source: 32 studies, 92 effect sizes, 3,029 participants; SRL g = 1.613 (11 studies, p = 0.032); SDL g = 1.111 (8 studies, p = 0.043); cognitive/metacognitive regulation combined g = 0.377, "moderate"; forethought g = 0.474, the largest significant phase effect (performance g = 0.781, p = 0.078, not significant) | no finding |
| PP-21 | P13 | Mar et al. (2021), p. 4, l. 91 to 93 | Source abstract: "over 75 unique samples and data from more than 33,000 participants"; stories "more easily understood and better recalled"; "robust"; "not moderated by various study characteristics" | no finding |
| PP-22 | P13 | Dahlstrom (2014), p. 4, l. 93 to 96 | Source: narratives describe "the cause-and-effect relationships between events" over "a particular time period that impact particular characters"; "increased comprehension, interest, and engagement"; "intrinsically persuasive"; "raises ethical considerations" | no finding |
| PP-23 | P28 | Gap and novelty sentences in Segment 1: "this work leaves a gap" (l. 97), "none of the studies reviewed here examines a narrative version" (l. 100), "none of the studies reviewed here, however, combines" (l. 103 to 104); abstract (l. 6 to 22) and introduction (l. 25 to 50) contain no "first" or "not yet studied" claim | Search description in manuscript: none (no databases, terms, period, date). Own searches: 3 (searches 1, 2, 3 of PP-26); counterexample for the third respect (GB-05), none for the first and second respects | finding GB-03 |
| PP-24 | P13 | Putnam and Roediger (2013), p. 4, l. 103 | Source not readable (publisher page blocked). Secondary summary (Frontiers in Psychology 2017, 8, 1018): overt retrieval better in "only one of three experiments"; formats typing and saying aloud. Compatible with "few differences" | no finding; status inferred; source listed under limits |
| PP-25 | P10 | gaps against RQs, chain from frame to results | 5 gaps; gaps 1 and 2 to RQ1, 3 to RQ2, 4 to RQ3 (p. 4 l. 106 to 108); gap 5 describes the sample, not a question; RQ1 and RQ2 descriptive and answerable with case data; reading while listening frame declined explicitly (p. 14 l. 319 to 320) | no finding beyond GB-02; disclosed: no comparison with the literature on listening |
| PP-26 | P14 | Contribution in one sentence: a single learner builds with an AI assistant learning paths whose expected answers must occur verbatim in his own verified fact document, checked by a script, and learns them by voice with a learning record kept by the assistant. Searches (6): (1) voice assistant retrieval practice quiz spoken answers smart speaker; (2) LLM quiz questions grounded in source text, verbatim answer verification; (3) spoken dialogue tutoring ITSPOKE spoken vs typed; (4) Litman et al. 2006 citation; (5) LLM rewriting expository text into narrative, same content; (6) autoethnography of learning with ChatGPT | Candidates: Litman et al. (2006) not in list, finding GB-05; Gandhi and Muldner (2025) not in list, finding GB-06; Ruan et al. (2019) QuizBot, CHI 2019, doi:10.1145/3290605.3300587, not in list, text chat retrieval practice of factual knowledge with stored answers and spaced scheduling, same field, no finding; search 5 gave no study of a narrative version built from the same verified content; search 2 gave no study with verbatim answer checking | two findings |

### Segment 2: Materials, methods, Appendix A (p. 5 to 12; p. 22 to 24)

#### Substantive findings

**GB-07 The statement that each case has a learning path that passed the check script holds only for earlier paths; the current paths of two cases were cut anew without a documented full check, which is said only in the caption of Table 1.**

| Field | Content |
|---|---|
| Check | P6, P17 |
| Location | p. 5 l. 113; Fig. 1 caption p. 6 l. 121 to 122; Table 1 caption p. 5 l. 117 to 119; p. 1 l. 14 to 15; p. 8 l. 168 to 170 |
| Quotation | "Each case has a fact document and a learning path that passed the check script"; "after version 10 of the fact document on the geological eras, both of its learning paths were cut anew, into 15 and 14 sessions, without a documented full check run" |
| Concern | For two of five cases (geological eras fact document and narrative version), the learning paths in use at the cut-off date (15 and 14 sessions) differ from the checked ones in Table 4 (11 and 10 sessions) and have no documented full check run; the fact document itself moved to version 10 (for the fact document version of each run see GB-23). The manuscript's own advice to users is that a learning path rests on a checked basis (p. 8, l. 168 to 170). The 10 narrative sessions ran on the checked path, so Table 5 is unaffected. |
| Suggestion | Move the disclosure into Sect. 3.1 and 4.2 and the caption of Fig. 1; reword p. 5 l. 113 to "Each case has a fact document and a learning path that passed the check script in the version listed in Table 4"; run and report the check of the two new paths, or state that they are outside the study. |
| Status | verified |
| Severity | moderate |
| Source | SD |

**GB-08 The learning path on the geology of Germany is named version 1 in Table 1 and Fig. 1 but version 6 in its file name, without explanation, and Table 4 gives it no version.**

| Field | Content |
|---|---|
| Check | P38 |
| Location | Table 1, p. 5, row Geology of Germany, column Learning path; Fig. 1, p. 6, row Geology of Germany, box "Learning path, checked by script"; Table 4, p. 14, row Geology of Germany, column Learning path |
| Quotation | "version 1 (file name: version 6)" (Table 1); Fig. 1: "version 1: passed after exclusions"; Table 4: "Geology of Germany" |
| Concern | The manuscript discloses the two names in Table 1, which is to its credit, but does not say why the file carries version 6, whether versions 2 to 5 exist, or which name the learning record and the check run refer to. Table 3 says that a learning record header holds the learning path "with version and date", and Sect. 3.5.3 (l. 227 to 228) says the assistant reports a version mismatch; with two version names for one file, a reader cannot tell which one such a check would compare. In Table 4, every other row carries a version except this row and Volcanology (see GB-09). |
| Suggestion | Add one sentence to the caption of Table 1 (p. 5, l. 115 to 119) or to Sect. 4.1 (l. 298 to 299) explaining the file name version 6, and add "version 1" to the Table 4 row Geology of Germany. |
| Status | verified (names at the page images 5, 6, 14); inferred (consequence for the version check in Sect. 3.5.3) |
| Severity | minor |
| Source | S2 |

**GB-09 The volcanology case is labelled "Volcanology, stage 1" in Table 1, Table 4 and Fig. 1, but the text never uses or explains "stage 1".**

| Field | Content |
|---|---|
| Check | P38 |
| Location | Table 1, p. 5, row Volcanology, stage 1, column Case; Fig. 1, p. 6, row label; Table 4, p. 14, row Volcanology, stage 1, column Learning path; text mentions of the case in l. 13 to 14, l. 111 to 114, l. 167, l. 235, l. 259, l. 283 to 287, l. 299 |
| Quotation | "Volcanology, stage 1" (Table 1, Table 4, Fig. 1); l. 167: "the one on volcanology was taken word for word from openly licensed textbooks" |
| Concern | Counted over text.json, "stage 1" occurs twice (Table 1, Table 4), and at the page image a third time in Fig. 1; "volcanology" or "Volcanology" occurs 11 times, never with a stage. A reader cannot tell whether the fact document covers only part of the textbooks, whether further stages exist, or whether "stage 1" is part of the name of the fact document. Table 4 also gives no learning path version for this row, while Table 1 and Fig. 1 give "version 4". |
| Suggestion | Explain "stage 1" in Sect. 3.3 (p. 8, l. 166 to 167), for instance which chapters or textbooks the stage covers, or drop the qualifier from Table 1, Table 4 and Fig. 1; add "version 4" to the Table 4 row. |
| Status | verified (counts and labels at page images 5, 6, 14); assumption (that "stage 1" denotes a partial coverage) |
| Severity | minor |
| Source | S2 |

**GB-10 For the geological eras, it is unclear whether "version 7" and "version 8" name versions of the learning paths or of the fact documents, and which fact document version each learning path was built on.**

| Field | Content |
|---|---|
| Check | P38 |
| Location | Table 1, p. 5, caption l. 117 to 119 and rows Geological eras, fact document and Geological eras, narrative version, column Learning path; Table 4, p. 14, rows Geological eras (fact document), version 7 and Geological eras (narrative version), version 8, column Learning path; Sect. 4.6, p. 15, l. 343 |
| Quotation | "after version 10 of the fact document on the geological eras, both of its learning paths were cut anew, into 15 and 14 sessions, without a documented full check run." (l. 117 to 119); Table 4: "Geological eras (fact document), version 7"; l. 343: "The narrative version of the geological eras was written at the learner's request as a fact document of its own" |
| Concern | The caption of Table 1 defines the column as the learning path version, but the Table 4 label "Geological eras (fact document), version 7" can be read as version 7 of the fact document, and the same caption counts versions of the fact document as well ("version 10"). The caption also speaks of "both of its learning paths", which treats the learning path of the narrative version as a learning path of the eras fact document, while Sect. 4.6 calls the narrative version "a fact document of its own" with "a learning path of its own" (l. 343, l. 346). Is the narrative version versioned together with the eras fact document, so that version 10 applies to both? The missing fact document version per check run is raised in GB-23. |
| Suggestion | In Table 4, write "Geological eras, fact document: learning path version 7" (and correspondingly for the narrative version), and in the caption of Table 1 (l. 115 to 119) say whether the narrative version shares the version numbering of the eras fact document. |
| Status | verified (wording at page images 5, 14, 15); inferred (the double reading); assumption (shared versioning of the two documents), therefore asked as a question |
| Severity | minor |
| Source | S2 |

**GB-11 Fig. 1 and its caption present the narrative version as built in a document project of its own, whereas Sect. 3.3 and Sect. 5 say it was written within the project on the geological eras.**

| Field | Content |
|---|---|
| Check | P3 |
| Location | Fig. 1, row "Geological eras, narrative version", column "Fact document" (p. 6); Fig. 1 caption, l. 121; compare p. 7, l. 157 to 159 and p. 18, l. 381 to 382 |
| Quotation | "own document project (German)" (box text); caption l. 121: "Each fact document was built in a document project of its own"; Sect. 3.3 l. 157 to 159: "Each of the four source fact documents was built in a document project of its own before any learning path existed, with a workplan, a decision log and a record of all changes, and the narrative version was written within the project on the geological eras (Sect. 4.6)" |
| Concern | Fig. 1 is a clear overview: its counts agree with Table 1 (see PP-30). But the third row gives the narrative version the same box, "own document project (German)", as the four source documents (box text confirmed on the 300 dpi page image), and the caption says the same for every fact document. The text separates the two on purpose: four source documents each in their own project, and a fifth written "within the project on the geological eras" (l. 158 to 159) and "from one of them" (l. 382). The difference matters for how the narrative version was checked: it was checked against the inventory of its source (l. 344 to 345), not against sources of its own. A reader who only sees Fig. 1 takes it to be a fifth independent project. |
| Suggestion | In Fig. 1, row 3, column "Fact document", replace "own document project (German)" with, for example, "written from the fact document on the geological eras (German)". In the caption, l. 121, write "Each of the four source fact documents was built in a document project of its own, the narrative version within the project on the geological eras". |
| Status | verified (box text at the page image, caption and Sect. 3.3 in the text) |
| Severity | minor |
| Source | AB |

**GB-12 Sections 3.2 and 3.5 describe version 2.6.6 as the way sessions run, but none of the 25 sessions ran under it, and several of the described rules applied to no or few sessions; this is said only later in Sect. 3.6.**

| Field | Content |
|---|---|
| Check | P7, P17 |
| Location | p. 7 l. 142 to 149; Fig. 2 caption p. 7 l. 151; p. 9 l. 194 to 200; p. 12 l. 262 to 272; p. 18 l. 387 to 391 |
| Quotation | "A session in voice mode runs in six steps"; "In the text chat, the assistant shows the excerpt and the three questions without their answers"; "Sections 3.2 and 3.5 describe the current version 2.6.6 (Appendix A) ... no session in the data ran under it or under its predecessor 2.6.5" |
| Concern | The manuscript is open about this in Sect. 3.6 and in the caption of Fig. 2. Computed from Sect. 3.6 and Fig. 4: 3 of 25 sessions (12 %) ran under 2.3.1, 8 (32 %) presumably under 2.4.0, 14 (56 %) under 2.5.0, 0 under 2.6.5 or 2.6.6. Step 2 of the six steps (questions shown before the call) is documented for 3 of 25 sessions (narrative 8 to 10, 12 %); "asked as worded, without hints" was a rule for 14 of 25; digits spoken one by one, rephrasing only on request and no hint even when asked were rules for none. Sect. 3.2 and 3.5 use the present tense ("runs", "is read", "are asked") without saying so where the steps are introduced, and the discussion answers RQ2 with the 2.6.6 division of work. Moderate: the results sections report the runs correctly, but a reader of the methods takes the specification for the procedure behind the data. |
| Suggestion | At the start of Sect. 3.2 and 3.5, state that the description is the 2.6.6 specification and that no session ran under it; add a table to Sect. 3.6 listing for each rule in Sect. 3.5 the sessions to which it applied (with the counts above); in Sect. 5 (p. 18 l. 387 to 391), answer the first half of RQ2 with the sessions as they ran. |
| Status | verified (versions and rules); inferred (shares) |
| Severity | moderate |
| Source | SD |

**GB-13 The statement that speech recognition errors were interpreted correctly cannot be checked from the data, because only the recognized text of voice input exists.**

| Field | Content |
|---|---|
| Check | P25 |
| Location | p. 10 l. 214 to 216; p. 11 l. 232 to 233 |
| Quotation | "Speech recognition errors ... were interpreted correctly by the assistant in the recorded cases"; "inputs given by voice are available only as the text produced by the speech recognition" |
| Concern | To judge an interpretation correct, one needs what the learner said. The data hold only the recognized text, so only those errors are visible that produced implausible text ("55 times"); errors that produced plausible but wrong text cannot be found and may have changed grades. The number of recorded cases is not given. How was correctness established, by the learner's memory or by context? |
| Suggestion | In Sect. 3.5.2, give the number of recorded cases and how correctness was judged, and add that misrecognitions yielding plausible text are not detectable in these data; if audio exists for some calls, compare it for a sample. |
| Status | inferred (from l. 233); the method of judging is a question |
| Severity | moderate |
| Source | SD |

**GB-14 How eight sessions of version 7 were credited from version 6 is not described, and which sessions were credited, closed and asked can only be derived by calculation.**

| Field | Content |
|---|---|
| Check | P8, P22 |
| Location | p. 11, l. 228 to 230 (Sect. 3.5.3); p. 14, l. 325 to 327 (Sect. 4.4); Fig. 4, session labels 14 to 17; Table 6, row 7 |
| Quotation | "eight new sessions whose material lay entirely in completed sessions were credited, and five with new material were closed at the learner's request without being asked"; l. 325 to 326: "17 of the 31 sessions of version 7 on southern Norway were done: 8 credited from version 6, 5 closed at the learner's request without being asked and 4 asked" |
| Concern | 13 of the 17 sessions counted as done on version 7 (76.5 %, Python) were not asked. How "lay entirely in completed sessions" was decided, by anchors compared by script or by the judgement of the assistant, and against which version of the fact document, is not stated. The text gives 4 asked sessions; Fig. 4 labels them 14, 15, 16 and 17, and Table 6, no. 7 refers to session 17. A reader has to compute 8 + 5 = 13 sessions credited or closed and assume that these were sessions 1 to 13 to see why the asked sessions start at 14. |
| Suggestion | In Sect. 3.5.3 (l. 228 to 230), state the procedure for crediting (input, rule, output) and whether the check script was used; in Sect. 4.4 (l. 326), write "and 4 asked (sessions 14 to 17)" and name the sessions that were credited and those that were closed. |
| Status | verified (text, Fig. 4 labels at the page image, Table 6); inferred (76.5 %; assignment of sessions 1 to 13) |
| Severity | moderate |
| Source | S3, SD |

**GB-15 The analysis chain from chats to Table 6, Table 5 and the counts in Sect. 4 is carried out by the same model at every step, with procedures that are not described and data that are not published.**

| Field | Content |
|---|---|
| Check | P8 |
| Location | p. 11 l. 238 to 239, 244 to 247; p. 12 l. 275 to 277; p. 16 l. 353; p. 24 l. 499 to 500; p. 10 l. 218 to 219 |
| Quotation | "four method analyses of the chats ... they are cited as a data basis and are not published"; "Three of them were checked by a separate agent of the same model family"; "Claude analysed the chats and learning records, collected the facts and checked them against their sources" |
| Concern | The steps grading (model in the call), recording (model), method analysis (model), check of the analyses (agent of the same model family), extraction of counts and checking of statements (Claude, Sect. 3.7) all depend on judgement by models. For none of them are the instruction, the criteria or the output format given, and the records and analyses are not published, so Table 5, Table 6 and Sect. 4.5 cannot be rebuilt. The report of the check itself is hard to read: for the first checked analysis only "18 deviations" are given, without the number of statements assessed, and for the other two "30 and 37" deviating statements stand beside "31 and 34 findings", one more finding than deviations in one case and three fewer in the other, without saying how the two units relate (l. 245 to 247). The deviation rates (30 of 85 = 35.3 %, 37 of 93 = 39.8 %, Python) are reported, but not what was done with the deviations, nor whether the first analysis, examined "only by a later meta-analysis", feeds Table 6. |
| Suggestion | Add to Sect. 3.6 a short description of each judgement step (who, instruction, output), state for each checked analysis the number of statements, deviations and findings and how the deviations were resolved, and publish a per-session table (date, path, version, mode, questions asked, grade, deviation flag, To review entry) as a supplement; the records concern only the author, so such a table could be released even if the records are not. |
| Status | verified; inferred (rates computed: 30/85, 37/93) |
| Severity | moderate |
| Source | S3, SD |

**GB-16 The paper says every statement rests on a chat passage in original wording or a checked file, but for one chat 74 of 86 inputs rest only on the assistant's own chat log, and the statements drawn from that chat are not identified.**

| Field | Content |
|---|---|
| Check | P6, P19 |
| Location | p. 11 l. 240 to 242; p. 11 l. 247 to 249; p. 6 l. 133 to 134 |
| Quotation | "Every statement in this paper rests either on a chat passage read in its original wording or on a file checked with a measured value"; "the wording of 74 of its 86 inputs rests only on the chat log the assistant kept during the work" |
| Concern | 74 of 86 inputs is 86.0 % of that chat. The chat log is a machine-kept record, i.e. the kind of source the paper says was checked or not used. Which chat this is, and which statements (for instance the 22 of 41 short inputs on p. 6 l. 134, or rows of Table 6) rest on it, is not stated. The voice inputs of all chats are in addition only speech recognition text (l. 233). |
| Suggestion | In Sect. 3.6, name the compacted chat and list the statements that rest on its log, or qualify l. 240 to 242 ("except for the chat described below"); mark the affected rows in Table 6. |
| Status | verified; inferred (86.0 %) |
| Severity | moderate |
| Source | SD |

**GB-17 When the three success criteria were set is not stated; if they were set after the sessions, the self-assessment in Sect. 4.8 is judged against criteria shaped by the experience.**

| Field | Content |
|---|---|
| Check | P9 |
| Location | p. 12 l. 252 to 256; p. 17 l. 365; Fig. 6 |
| Quotation | "Success is therefore judged by the learner's own account, not by a test, and on three counts" |
| Concern | The data window starts on 27 September, when the format was set (p. 12 l. 258), and the criteria appear in the methods. Were they written down before the first session, for instance in the chat of 27 September, or formulated when the paper was written? The manuscript does not say; this is a question. |
| Suggestion | In Sect. 3.6, give the date and source of the criteria (chat passage), or state that they were formulated afterwards. |
| Status | assumption (formulated as a question) |
| Severity | moderate |
| Source | SD |

**GB-18 The example pair shipped with version 2.6.6 is learning path version 5, whose questions ask for lengths, dates and ages, contrary to the rule in force since 2.5.0.**

| Field | Content |
|---|---|
| Check | P5, P18 |
| Location | Table A3, p. 23 to 24, rows Question 3.1 to Expected answer 3.3; p. 24, l. 497 to 498; p. 2, l. 40 to 41; p. 9, l. 189 to 190 |
| Quotation | "From version 2.5.0 on, the skill aims its questions at relations and events instead of numbers, dates and names"; "How long is the Transscandinavian Igneous Belt according to the two sources cited?"; "with seafloor spreading at about 55 Ma" |
| Concern | Of the three questions shown, 3.1 asks for a length (1400 km, 1500 km) and 3.3 for rift phases with ages ending in "55 Ma", the very value the speech recognition turned into "55 times" (p. 2 l. 40). The manuscript knows that version 7 of the path already followed the newer style (p. 9 l. 189). Users who take the published example pair as the model of a learning path learn the pre 2.5.0 style. The expected answers have 24, 21 and 22 words in the English translation and meet the 5 to 30 word rule. |
| Suggestion | Ship version 7 of the path, or a path built under 2.6.6, as the example pair; or state in Appendix A and in Code and data availability that the example pair predates the 2.5.0 rule. |
| Status | verified; inferred (word counts in translation) |
| Severity | moderate |
| Source | SD |

#### Minor corrections

| ID | Location | Quotation | Replacement | Source |
|---|---|---|---|---|
| KK-04 | Fig. 1, p. 6, row label of the second row (column Case) | "Geological eras" | "Geological eras, fact document" (as in Table 1, row 2, column Case) | S2 |
| KK-05 | p. 12 l. 265 | "and the first line of version 2.6.0 after the ten sessions of the narrative version" | "and the first line of version 2.6.0 during and after the ten sessions of the narrative version (rules proposed from 5 October, Table A2)" | SD |
| KK-06 | Table A1, p. 23, row review session, column Command | "‘Wiederholung ssitzung’" (word broken across the cell line after Wiederholung, without a hyphen, page image 23) | ‘Wiederholungssitzung’ on one line (wider Command column), or broken with a hyphen as ‘Wiederholungs-’ and ‘sitzung’ | S2, S4, SD |

#### Verification log

| ID | Check | Checked | Values | Result |
|---|---|---|---|---|
| PP-27 | P5 to P38 (design sketch) | design sketch of the study from the manuscript, each entry with location | aim l. 28 to 30; RQ1 to RQ3 l. 43 to 48; no hypotheses, three success criteria by own account l. 252 to 256; type self-experiment, single case, closest to autoethnography l. 250 to 252; 1 learner who is also developer, 5 cases, 6 learning paths, 7 check runs, 25 sessions on 2 cases, 75 graded answers, 2 completed reviews (Table 1, Table 5, l. 301); no control condition l. 20, l. 463 to 464; sources: chats, four learning records, check script output, four method analyses, learner's account (l. 232 to 249); data window 27 September to 13 October 2026 (l. 258 to 259); sessions under 2.3.1: 3, under 2.4.0: 8, under 2.5.0: 14, under 2.6.5 or 2.6.6: 0 (l. 262 to 272) | no finding on the sketch itself; findings derived from it are listed in their segments |
| PP-28 | P9 | selection of cases with sessions | 2 of 5 cases with sessions; Germany and volcanology paths finished 9 October, 4 days before cut-off | no finding; reason for the choice not stated |
| PP-29 | P38 | Case figures in Table 1, Table 4 and Fig. 1 (Python) | words, sessions, questions per case identical in Table 1 and Table 4: 14,267/31/93; 3,595/11/33; 4,692/10/30; 9,682/25/75; 19,519/38/114; questions = 3 x sessions in all five rows; Fig. 1 session bars 31, 11, 10, 25, 38; sessions run 11 + 4 + 10 = 25 | no finding |
| PP-30 | P3 | Fig. 1 against Table 1 and Table 4; bar lengths | Versions 7, 7, 8, 1, 4; sessions in the path 31, 11, 10, 25, 38; sessions run 15 (11 on version 6, 4 on version 7), none, 10, none, none; review sessions 1, 0, 1, 0, 0: all as in Table 1. "after exclusions" for narrative version, Germany, volcanology = 3, as in Table 4 and caption. Bar interiors (flecken #e4e4e4 and #e49c04): 420, 146, 133, 337, 515 px grey and 202, 134 px orange, that is 13.55, 13.27, 13.30, 13.48, 13.55, 13.47, 13.40 px per session (spread 0.28 px per session, within the 2 px border error divided by the bar count). Colours of bars equal legend fields (#e4e4e4, #e49c04) | no finding on values; for the project box of the narrative version see GB-11 |
| PP-31 | P26 | version binding of the record; division of channels | record and version check only in the text chat, call cannot read the record (p. 6 l. 138 to 139) | no finding; the path without record access is disclosed |
| PP-32 | P3 | Fig. 2 against the six steps (l. 142 to 149) and Sect. 3.5.3 | Boxes: build and check (code execution), prepare (excerpt and three questions), listen (read in full, announce end), answer (three questions, graded tolerantly), update record and hand over as file, To review (incorrect or partially correct), review on request on screen or in the call; dashed arrows "next session" and "on request" as the caption says; pink only on review part. Steps 2 to 6 each have a box; step 1 (naming the session) is part of "Prepare session" | no finding |
| PP-33 | P18 | self-application of stated principles | fact document checked before the path (p. 8 l. 168 to 170): see GB-07; question style rule: see GB-18; process data treated as such in all result sections | no finding beyond those |
| PP-34 | P3 | Fig. 3 against Sect. 3.4, 3.5.2 and 4.2 | Checks a to e (anchor exactly once, coverage without gaps or overlaps, answers word for word, image block in exactly one session, excluded chapters not covered) = the five checks of l. 181 to 182 and l. 302 to 306; "up to about 550 words" = l. 205; "5 to 30 words" = l. 206 to 207; colours as in the caption (paragraph blue, image block light blue, excluded grey dashed, orange sessions, green check script). The manuscript declares the figure schematic (l. 188) | no finding |
| PP-35 | P6 | absolute statements | "read in full in every call" (p. 9 l. 195): no counter case; "All 10 sessions of the narrative version were asked" (p. 14 l. 327): Fig. 4 shows 10 bars; "open-question lists of all four learning records are empty" (p. 20 l. 429 to 430): consistent with the one open question in the uncounted record; "updated after every session and review" (p. 15 l. 336): broken off review had no answers (Table 6 row 5) | no finding apart from GB-07 and GB-16 |
| PP-36 | P38 | Grade names, list names and commands in Sect. 3.5, Table 2, Table 3, Table A1 | grades "correct", "partially correct" (7), "not correct" (4) identical in Table 2, Table 3, l. 256 and Table 5; list "To review" (8) and part "Open questions" (2) consistent; commands 'review session', 'start review', 'repeat' (l. 222 to 223) match Table A1 glosses; review modes verbatim, explain, both match Table A1 and Table A2 | no finding |
| PP-37 | P12 | Each data source in Sect. 3 and Appendix A against Code and data availability (l. 495 to 500) | skill 2.6.6 with SKILL.md, lernpfad.py, tests, licence file: published (GitHub link present, reachability not checked); example pair, fact document on southern Norway and learning path version 5 with 30 sessions: published; Tables A1 to A3: in the manuscript, accessible; learning records: not published, no reason; method analyses: not published, no reason; chats, check script outputs, fact documents and learning paths of five cases, skill versions 2.3.1, 2.4.0, 2.5.0, ICS chart file, textbooks and open-access sources, map booklet, agent check reports, per-session data of Fig. 4: not mentioned; machine-generated chat summaries and project notes (l. 241 to 242): used only as pointers, not as evidence | findings GB-42; disclosed by the manuscript: records and analyses not published (l. 218 to 219, l. 239, l. 499 to 500), self-analysis limits (l. 243 to 249) |
| PP-38 | P19 | provenance class of result blocks | 7 result blocks: Table 4 primary; Table 1 sessions, Table 5, Fig. 4, Sect. 4.5, Table 6 model generated (records, analyses); Sect. 4.8 self report; 5 of 7 (71 %) on model generated data | no finding beyond GB-16; disclosed in Sect. 3.6 l. 243 to 249 |
| PP-39 | P38 | Skill version numbers across Sect. 1, 3.2, 3.4, 3.6, Table 6, Fig. 2, Fig. 4, Fig. 5, Table A1, Table A2 | occurrences in text.json: 2.1.0: 1, 2.2.0: 2, 2.3.1: 2, 2.4.0: 4, 2.5.0: 7, 2.6.0: 10, 2.6.1: 4, 2.6.5: 6, 2.6.6: 13; "first line" 7, "second line" 1; every version named in the text appears in Table A2; the double number 2.6.0 is explained in the caption of Table A2 (l. 490 to 492); Table 6 remedies (2.4.0, 2.6.1, 2.6.5, 2.6.6) match the Change column of Table A2 | no finding |
| PP-40 | P38 | Learning path versions of southern Norway and the example pair | version 5 and version 6: same learning path, explained in l. 301 to 302 and Table 4, row version 6; example pair = version 5 with 30 sessions in Sect. 3.5.2 (l. 205 to 206), Table 4, Table A3 caption and l. 497 to 498; version 7: 31 sessions in Table 1, Table 4, Fig. 1, l. 325 | no finding |
| PP-41 | P38 | Assistant, model and platform names | "Claude Opus 5.5" 2 occurrences (l. 126, l. 274), "claude.ai website in a web browser" and "Claude app for Android" in l. 126 to 127 and l. 274; skill name "lernpfad-sitzungen" 8 occurrences plus one hyphenated line break (l. 128 to 129, page image 6), "template-dokumentprojekt" 1; "check script" 22, "lernpfad.py" 1 (l. 497); package parts in l. 128 to 129 (rule file, check script with tests, example pair) and l. 496 to 498 (adds licence file, introduced in 2.6.6 according to Table A2) | no finding |
| PP-42 | P38 | Counts of learning records and method analyses | learning records: five cases minus the eras fact document = 4 files (l. 234), "all four learning records" (l. 429 to 430); second record for southern Norway excluded in l. 116 to 117, l. 235 to 236, l. 337; method analyses: four (l. 238), three checked by an agent plus one examined by a meta-analysis (l. 245 to 247) = 4 | no finding |

### Segment 3: Results (p. 13 to 18)

#### Substantive findings

**GB-19 The fact documents are called verified, but Sect. 4.1 reports no check for the two source documents on which sessions were run, and no reported check has an estimate of the errors it left.**

| Field | Content |
|---|---|
| Check | P15, P11, P32 |
| Location | p. 13, l. 282 to 299 (Sect. 4.1); p. 1, l. 2 and l. 7; p. 2, l. 30; p. 3, l. 43 (RQ1); p. 18, l. 385 to 387; p. 19, l. 409 and l. 412; Fig. 6, middle column, third box; p. 22, l. 467 |
| Quotation | "How the fact documents were checked therefore matters." (l. 283); title: "Building and Running Verified Learning Paths"; l. 467: "the learner assembled learning content from his own verified fact documents with an AI assistant" |
| Concern | The manuscript states its premise clearly: the check script binds the learning path only to the fact document, so "how good that content is depends on how the fact document itself was checked (Sect. 4.1)" (l. 30) and "its correctness rests on how the fact document itself was checked" (l. 386). Sect. 4.1 then reports the check and its findings for volcanology (word comparison, two serious errors found by later steps, l. 283 to 287), for the geology of Germany (source cycle, 49 first mentions and mixed spelling found only by the final consistency check, l. 287 to 292) and for the narrative version (inventory of 144 sentences, l. 292 to 293). For the fact document on southern Norway, on which 15 of the 25 sessions ran, and for the fact document on the geological eras, the source of the narrative version, whose names and boundary ages were to come only from the ICS chart v2026/06 (l. 164 to 165), Sect. 4.1 gives only the chat dates (l. 294 to 298). The only statements are that each was built in a document project with workplan, decision log and record of changes (l. 157 to 158) and that it "was checked in its document project, by different procedures" (Fig. 7 caption, l. 409). The attribute "verified" in the title, the Abstract (l. 7), RQ1 (l. 43), l. 412, Fig. 6 and the conclusion (l. 467) therefore has no location in the Results for exactly the two cases that were learned. Where checks are reported, each stage missed errors that a later one found (volcanology, geology of Germany), and no fact document was checked against its sources by a sample independent of the building chat, so the remaining error of the material read aloud and asked is unknown. RQ1 asks how verified fact documents can be built; the Results report procedures for three of five documents and no measure of their outcome. Major rather than moderate: if the checks of the two learned documents cannot be reported, "verified" no longer holds for the material on which the sessions ran, and the answer to RQ1 changes. |
| Suggestion | Add to Sect. 4.1 how the fact documents on southern Norway and on the geological eras were checked against their sources (procedure, what was found, when), at the level of detail given for volcanology and the geology of Germany, preferably as a table with one row per fact document (procedure, errors found, stage at which they were found); report for each fact document a random sample of paragraphs checked against the cited sources by a person or procedure independent of the building chat, with the number of deviations. If this cannot be done, restrict "verified" in the title, l. 7, l. 43, l. 412, l. 467 and Fig. 6 to the binding of path to fact document and say so in Sect. 5. |
| Status | verified (absence of a check description for southern Norway and the geological eras in Sect. 4.1; wording at l. 2, 7, 30, 43, 283, 386, 409, 412, 467 and in Fig. 6 at the page images); inferred (remaining error unknown); whether such checks took place is asked as a question |
| Severity | major |
| Source | S3, S4, SD |

**GB-20 "Seven check runs" counts only the passing runs; the runs that failed before them are not counted and the number of runs until a pass is not reported.**

| Field | Content |
|---|---|
| Check | P20 |
| Location | p. 13, l. 301 and l. 306 to 307 (Sect. 4.2); Table 4, column Exclusions and corrections until passed, row Geology of Germany; Table 6, row 3 |
| Quotation | "Table 4 lists seven check runs of six learning paths"; Table 4: "first run 577 findings; chapters the path itself marks as no learning material excluded; reference chapter added to the exclusions; opening anchor of session 20 set by hand" |
| Concern | The unit "check run" changes within the section. l. 301 counts seven runs, one row each; the row for the geology of Germany itself names a first run with 577 findings and three later corrections, so at least one further run took place for that path (at least 8 runs in all). For the narrative version and volcanology, "passed only after chapters ... had been named as exclusions" (l. 306 to 307, also Abstract l. 15 to 16) suggests earlier failing runs, but the text does not say so. Instance SD proposed to reword l. 306 to 307 as if only the geology of Germany had failed before its exclusions were named; the manuscript does not support that reading, because both l. 306 to 307 and the Abstract say that all three passed "only after" the exclusions had been named, so the question is asked here instead of a correction. The number of runs needed to reach a pass is part of how a learner builds a learning path (RQ1) and cannot be derived. |
| Suggestion | Rephrase l. 301 as "Table 4 lists the final check run of each of the six learning paths, seven in all", add a column "Runs until passed" to Table 4, and state in l. 306 to 307 for each of the three paths whether a run failed before the exclusions were named. |
| Status | verified (additional run for the geology of Germany); assumption (earlier failing runs for the narrative version and volcanology), put as a question to the author |
| Severity | moderate |
| Source | S3, SD |

**GB-21 Two of the checks that the script performs, image blocks and overlaps, are announced but not reported per learning path.**

| Field | Content |
|---|---|
| Check | P11 |
| Location | p. 13, l. 302 to 306 (Sect. 4.2); Table 4, all columns; p. 8, l. 180 to 182 (Sect. 3.4); Table 6, row 9 |
| Quotation | "in addition, every image block must be assigned to exactly one session, and excluded chapters must not be covered"; Table 6, no. 9: "version 2.6.0, second line, skipped an image block that followed a heading" |
| Concern | Sect. 3.4 and 4.2 list five checks: anchors, coverage, expected answers, image blocks and exclusions. Table 4 reports anchors and answers as counts and exclusions as text, but has no column for image blocks and none for overlaps. Table 6, no. 9 shows that the image block check failed at least once, for volcanology, and was fixed in version 2.6.1 (Table A2, 9 October 2026); how many image blocks each path has and whether each was assigned exactly once is not shown (for the timing of the volcanology run relative to that fix see GB-23). |
| Suggestion | Add to Table 4 a column "Image blocks: assigned exactly once, of all" (with "none" where a fact document has no image blocks) and, if the script counts them, a column for overlapping words. |
| Status | verified (absence in Table 4) |
| Severity | moderate |
| Source | S3 |

**GB-22 The column Words in Table 4 has no denominator, so the coverage "without gaps or overlaps" that the check verifies is not shown.**

| Field | Content |
|---|---|
| Check | P20 |
| Location | Table 4, column Words, all rows, with caption p. 14, l. 310 to 311; p. 13, l. 303 to 304; cross-reference Table 1, caption p. 5, l. 115 and column Words |
| Quotation | "Words: words of learning material covered by the sessions"; "the sessions together must cover the learning material without gaps or overlaps"; Table 1: "Words: words of learning material in the learning path" |
| Concern | Anchors and Answers are given as found of all (60/60, 90/90 and so on), so the pass is visible. Words is given as a single number (13,890; 14,267; 3,595; 4,692; 9,682; 19,519) without the number of words of learning material in the fact document, so a reader cannot see that coverage was complete or that excluded chapters were not counted. Table 1 defines the same numbers differently, as words "in the learning path" rather than words "covered by the sessions"; both definitions only give the same value if coverage is complete, which is what the column should show. |
| Suggestion | In Table 4, give Words as covered of all words of learning material in the fact document (for example 14,267/14,267), and add overlapping words if the script counts them; align the definition in the caption of Table 1 with that of Table 4. |
| Status | verified |
| Severity | moderate |
| Source | S3 |

**GB-23 Table 4 gives date and script version of the check run for two of seven rows and the fact document version for none, although the word count depends on the script version; for volcanology the order of run and corrections is open.**

| Field | Content |
|---|---|
| Check | P11, P35, P30 |
| Location | Table 4, caption p. 14, l. 310 to 314, all rows, column Words; p. 13, l. 284 to 287 and l. 295 to 299 (Sect. 4.1); Table 6, row 9; Table A2, rows 2.6.0, second line, and 2.6.1; p. 6, l. 126 to 127 |
| Quotation | "Southern Norway, version 5, is the example pair of the skill and was re-measured on 13 October 2026 with the script of version 2.6.6; the original run had counted 13,859 words. Version 6 was checked on 30 September 2026 with the script then in use, which already counted 13,890 words."; l. 299: "each path was checked in a chat of its own on 9 October" |
| Concern | The caption itself shows that the same learning path was counted as 13,859 and as 13,890 words by different script versions (difference 31 words, 0.22 %, Python), so the counting rule changed between runs. For the other five rows neither the script version nor in every case the date is given. Sect. 4.1 gives check dates for version 6 (30 September), version 7 ("later in that chat"), the geology of Germany and volcanology (9 October); "its learning path was checked on 5 October" (l. 297 to 298) can refer to the fact document on the geological eras or to its narrative version, so the date of the run "Geological eras (fact document), version 7" is not stated. No row gives the version of the fact document it was run on, although the caption of Table 1 notes that one fact document reached version 10. The runs for the geology of Germany and volcanology fall on 9 October, the day on which version 2.6.0, second line, and its correction 2.6.1 for image blocks appeared (Table A2; Table 6, no. 9). For volcanology, the two serious errors that "later steps" found (l. 285 to 287), a chapter with three instead of eight paragraphs and 14 words of a figure description in the running text, concern paragraph boundaries and learning material, which is what the check script compares; whether the run in Table 4 (38 sessions, 19,519 words, passed) was made on the corrected fact document and under 2.6.1 is not stated. The values of the column Words are therefore not known to rest on the same counting rule or on the final documents. For the voice calls, the manuscript states model and effort setting once (l. 126), but not whether the call used the same model and setting, nor the app version or the speech recognition; this part is a question. |
| Suggestion | Add to Table 4 the columns Date, Script version and Fact document version; in l. 297 to 298, name the learning path checked on 5 October and give the check date of the path on the fact document on the geological eras; in Sect. 4.1 and Table 4, state the dates of the volcanology corrections relative to its check run; in Sect. 3.2, state the app version and whether model and effort setting applied to the voice calls. |
| Status | verified (caption, Sect. 4.1, missing fields, change of count); inferred (0.22 %); assumption (order of the volcanology corrections and the run; model in the voice call), asked as questions |
| Severity | moderate |
| Source | S3, SD |

**GB-24 Table 5 and Fig. 4 count answers to questions that were not in the learning path and answers given after a hint, without marking them, and these answers feed the To review list.**

| Field | Content |
|---|---|
| Check | P26 |
| Location | Table 5, p. 15 l. 328 to 329; Fig. 4, p. 15 l. 331 to 334; Table 6 rows 6, 7, 8, p. 16; p. 15 l. 338 to 340 |
| Quotation | "in session 9 of version 6 and session 17 of version 7, the call asked other questions than the learning path"; "the voice gave a hint on question 4.3 of version 6 on southern Norway, then graded correct" |
| Concern | The guarantee that every expected answer occurs word for word in the excerpt holds for the learning path, not for questions improvised in the call. Fig. 4 marks the deviating sessions with triangles, which is helpful, but Table 5 sums them with the others: up to 12 of the 75 graded answers (16 %) belong to sessions with deviating questions, and 2 more were graded after a hint, together up to 14 of 75 (18.7 %). In narrative sessions 6 and 7 the six answers were 1 correct, 2 partially correct and 3 not correct (measured in Fig. 4), and the incorrect ones went into To review as questions of the path although they may not be. How many questions per session deviated is not given. Moderate: the grades are process data, but the tables cannot be read as answers to verified questions. |
| Suggestion | In Table 5, add a column or a footnote with the number of answers to deviating questions and answers after hints per path, and give the totals without them; in Sect. 4.5, state whether To review entries from these sessions refer to the question asked or the question in the path. |
| Status | verified (deviations, hints, Fig. 4 values by measurement); inferred (shares 12/75, 14/75 as upper bounds) |
| Severity | moderate |
| Source | SD |

**GB-25 Table 5 and Sect. 4.4 do not say that the counted session 1 on southern Norway was the second run of that session, which only Table 6 states.**

| Field | Content |
|---|---|
| Check | P9 |
| Location | Table 5, row Southern Norway, version 6, with p. 14, l. 322 to 327; Table 6, row 2, column Trigger; Table 1 caption, p. 5, l. 115 to 117; Fig. 4, session 1 on 30 September |
| Quotation | "session 1 ran twice" (Table 6, no. 2); Table 1 caption: "the first voice session on southern Norway, on 29 September 2026, is not counted" |
| Concern | Table 6, no. 2 states that session 1 ran twice, and the caption of Table 1 that the first voice session of 29 September is not counted. Taken together, the answers counted for session 1 of version 6 on 30 September (1 correct, 2 partially correct, measured in Fig. 4) were given at the second hearing of the same excerpt and questions. Table 5 and Sect. 4.4, where the answers are reported, do not say so. That the uncounted session was session 1 is inferred from both statements. |
| Suggestion | Note in Table 5 or in Sect. 4.4 (l. 322 to 327) that the counted session 1 of version 6 was a repeat. |
| Status | inferred |
| Severity | minor |
| Source | SD |

**GB-26 Fig. 4 leaves out the dashed lines for the two skill versions dated 9 October 2026, although the caption promises lines for every version that Table A2 dates to the day.**

| Field | Content |
|---|---|
| Check | P24 |
| Location | Fig. 4, upper edge and plot area between the ticks "8 Oct" and "10 Oct" (p. 15); caption l. 332 to 333; Table A2, rows "2.6.0, second line" and "2.6.1", column Date (p. 23) |
| Quotation | "dashed lines the build dates of the versions dated to the day in Table A2" (l. 332 to 333); Table A2, column Date, rows 2.6.0, second line, and 2.6.1: "9 October 2026" |
| Concern | Fig. 4 maps each session to its date and skill version, and the dates of the dashed lines agree with Table A2 where they appear. Calibrated on the x-axis ticks (28 Sep at 482.5 px, 13 Oct at 2052.0 px, 16 ticks evenly spaced at 104.6 px), the dashed lines lie at 586.5 px = 29 Sep (2.2.0), 744.0 px = 30 Sep + 0.50 day (2.4.0), 1946.5 px = 12 Oct (2.6.5) and 2051.5 px = 13 Oct (2.6.6), each ± 0.01 day. Table A2 dates six versions to the day: 2.2.0 (29 Sep), 2.4.0 (30 Sep), 2.6.0 second line (9 Oct), 2.6.1 (9 Oct), 2.6.5 (12 Oct) and 2.6.6 (13 Oct). The search for vertical lines between x = 1580 and 1900 px (the 9 Oct tick is at 1633.5 px) finds none: 4 of the 6 lines are drawn. The figure gives no reason for leaving out the two 9 October versions. The tool loop is a main point of the paper, so the omission counts. |
| Suggestion | Add a dashed line at 9 Oct labelled "2.6.0 (second line), 2.6.1" to Fig. 4. If the lines are meant to show only the versions relevant to sessions, change the caption, l. 332 to 333, to say which versions are drawn. |
| Status | verified (measured) |
| Severity | minor |
| Source | AB |

**GB-27 Fig. 4 shows the grades after regrading without saying so in its caption.**

| Field | Content |
|---|---|
| Check | P37 |
| Location | Fig. 4 caption p. 15 l. 331 to 334; Table 5 caption p. 15 l. 328 to 329 |
| Quotation | "Answers per session by date, for the two cases with sessions" |
| Concern | Measured in the bars of Fig. 4 (page rendered at 300 dpi): version 6 sums to 12 correct, 8 partially correct, 13 not correct, version 7 to 1, 5, 6, narrative version to 16, 6, 8, which equals Table 5, whose caption states that three answers of version 6 were regraded. The caption of Fig. 4 does not. |
| Suggestion | Add to the caption of Fig. 4: "Grades after the regrading of three answers of version 6 (Sect. 3.5.2)." |
| Status | verified (by measurement) |
| Severity | minor |
| Source | SD |

**GB-28 The To review balance for version 6 on southern Norway does not close against Table 5 and Fig. 4 without a reading of the three regradings that the text does not state.**

| Field | Content |
|---|---|
| Check | P23, P3, P5 |
| Location | p. 15, l. 338 to 340 (Sect. 4.5); Table 5, row Southern Norway, version 6, columns Partially correct and Not correct, caption l. 328 to 329; Fig. 4, sessions 1 to 11 of southern Norway; p. 10, l. 213 to 214; p. 11, l. 221 |
| Quotation | "the list To review held 35 entries for that case: 24 from version 6, of which two had been closed by regrading and one in a review session, and 11 from version 7; 32 were open"; Table 5 caption: "Grades after the regrading of three answers of version 6 under the tolerance rule" |
| Concern | The rule that incorrect and partially correct answers go into To review (l. 221) matches the counts exactly for two of the three learning paths: version 7 has 11 entries and 5 + 6 = 11 answers not fully correct, the narrative version 14 entries and 6 + 8 = 14 answers, of which one entry was closed in a review while the answer keeps its session grade in Table 5. The stacked bars of Fig. 4, measured at 300 dpi, agree with Table 5 in every row (version 6: 12 correct, 8 partially correct, 13 not correct). For version 6, however, Table 5 gives 8 + 13 = 21 answers not fully correct against 24 entries, a difference of 3. Case analysis (Python), with k the number of the three regraded answers raised to correct: before the regrading there were 21 + k answers not fully correct, so k = 0, 1, 2, 3 give 21, 22, 23 and 24 entries, and only k = 3 yields one entry per answer. In that case three entries could have been closed by regrading, while the text names two closed by regrading and one in a review session. The balance then closes only if the entry closed in the review session is the third regraded answer, which would treat the review differently from the narrative version, or if one entry whose answer was raised to correct is still open while the review closed another. With k = 2, one of the 24 entries does not stem from a grade below correct, for example question 4.3, graded correct after a hint (Table 6, no. 8). The open count (24 minus 3, plus 11, = 32) agrees in every reading, so the difference concerns which entries are open and how the closings are attributed. Which reading applies is not stated and is asked here as a question. |
| Suggestion | In Sect. 4.5 (l. 338 to 340) or in the caption of Table 5, give the grade before and after for each of the three regraded answers, say whether the entry closed in the review session is one of them, and name any entry that does not stem from a grade below correct, so that entries, closings and Table 5 balance. |
| Status | verified (counts in Sect. 4.5 and Table 5; Fig. 4 by measurement); inferred (difference and case analysis); assumption (which reading applies), therefore asked as a question |
| Severity | moderate |
| Source | S3, AB, SD |

**GB-29 For the review sessions, Results report only the number of completed reviews and their topics, not the third review that broke off, nor the mode and outcome that the learning record keeps per review.**

| Field | Content |
|---|---|
| Check | P11, P20 |
| Location | p. 15, l. 340 to 341 (Sect. 4.5); Table 1, column Review sessions; Table 6, row 5; p. 20, l. 439; p. 11, l. 224 to 227 (Sect. 3.5.3); Table 3, row Reviews |
| Quotation | "Two review sessions were completed, one for each case, each with one topic."; Table 6, no. 5: "Call broken off before any answer"; l. 439: "A further review of the narrative version broke off before any answer was given." |
| Concern | Three reviews were started (one on southern Norway, two on the narrative version) and two completed. Sect. 4.5, the results section on review sessions, and the column Review sessions of Table 1 count only the completed ones without saying so; the broken-off review appears only in Table 6 and in the Discussion. Sect. 3.5.3 announces three review modes, and Table 3 shows that the record keeps date, mode, topics, the answer and the grade per review; Sect. 4.5 reports the topics, but not the mode, the skill version or the grade of the two completed reviews, although RQ3 asks how review sessions are built from the record. The closing of one entry per case implies a successful answer, but this is not stated. |
| Suggestion | In Sect. 4.5 (l. 340 to 341), report all three review attempts with date, mode, skill version, number of topics and grade, and name the column in Table 1 "Review sessions completed". |
| Status | verified |
| Severity | moderate |
| Source | S3, SD |

**GB-30 That the narrative version keeps all 144 sentences and adds no fact rests on one unspecified AI agent check, without an independent sample or a false negative estimate.**

| Field | Content |
|---|---|
| Check | P32 |
| Location | p. 15 l. 343 to 345; p. 18 l. 382 to 383; p. 4 l. 99 to 101; p. 19 l. 412 to 413; p. 11 l. 245 to 247 |
| Quotation | "a second AI agent checked that every sentence was contained with its full content and that no fact had been added"; "so that every one of the 144 sentences of its source was kept" |
| Concern | The inventory of 144 sentences is a sound basis. The completeness claim is, however, carried into the answer to RQ1 and into the second gap ("without losing or adding a fact") as an established result, and it rests on one check by a model of unstated identity, prompt and output; no count of deviations found, no correction, no human or scripted verification is reported. The manuscript's own data show that checks by a separate agent of the same model family found 30 of 85 (35.3 %) and 37 of 93 (39.8 %) statements deviating in the method analyses (p. 11 l. 246), so model output in this workflow is not error free, and nothing is said about how many deviations the checking agent itself would miss. The check script then binds the narrative learning path to the narrative version only, not to its source (Fig. 7). Major: if sentences were lost or facts added, the answer to RQ1 for the narrative case and the second gap claim (p. 4 l. 99 to 101) would not hold. |
| Suggestion | In Sect. 4.6, report the check: model, instruction, number of sentences flagged, corrections made. Counter design: publish the sentence to passage mapping as a supplement; check a random sample of the 144 sentences (or all) by a second, independent method, either the learner or a script that matches key terms and numbers of each source sentence in the narrative text, and report the agreement with its interval. Until then, state in Sect. 5 (p. 18 l. 382 to 383) that the completeness rests on one AI check. |
| Status | verified (only one AI check reported, deviation rates in Sect. 3.6); inferred (rates computed: 30/85, 37/93) |
| Severity | major |
| Source | SD |

**GB-31 Fig. 5 is said to show when the versions of Table A2 appeared, but it has no mark for version 2.3.1 or for the second line of 2.6.0.**

| Field | Content |
|---|---|
| Check | P24 |
| Location | Fig. 5, row "Versions of the skill" (p. 17); caption l. 359 to 360; Table A2, rows "2.3.1" and "2.6.0, second line" (p. 23); Sect. 3.6, l. 262 |
| Quotation | "when versions of the skill appeared (Table A2; a version dated by a range is placed at its middle)" (l. 359 to 360); Table A2, row 2.3.1: "revision; its order relative to 2.2.0 could not be determined"; l. 262: "Sessions 1 to 3 on southern Norway, version 6, ran under version 2.3.1" |
| Concern | The version ticks that are drawn match Table A2. Calibrated on the gridlines (27 Sep 00:00 at 615.0 px, 8 Oct 00:00 at 1655.0 px, spacing 94.5 px), the solid ticks lie at 29 Sep + 0.21 (labels 2.1.0 and 2.2.0 on one tick), 30 Sep + 0.20 (2.4.0), 4 Oct + 0.20 (2.5.0, the middle of "3 to 5 October"), 9 Oct + 0.21 (2.6.1), 12 Oct + 0.21 (2.6.5) and 13 Oct + 0.20 (2.6.6), and the dotted tick at 8 Oct + 0.20 (2.6.0 first line), each ± 0.02 day. Table A2 lists ten versions or lines, of which Fig. 5 labels eight; 2.3.1 and the second line of 2.6.0 have no tick and no label. 2.3.1 is the version under which sessions 1 to 3 ran (l. 262), and Fig. 4 shades those sessions as "skill 2.3.1". So Fig. 5 is the only timeline of the versions, yet a reader cannot place the version of the first three sessions on it. Its order relative to 2.2.0 is uncertain (Table A2), but a version "dated by a range" is placed at its middle under the caption's own rule. |
| Suggestion | In Fig. 5, add a tick for 2.3.1 marked as dated only "by 30 September" (for example open or hatched) and a tick or shared label "2.6.0, second line" with 2.6.1 at 9 Oct. Or change the caption, l. 359, to "when selected versions of the skill appeared" and name the versions left out. |
| Status | verified (measured; missing ticks confirmed at the page image) |
| Severity | minor |
| Source | AB |

**GB-32 The learner's account of three or four screen sessions differs from the two in the learning records, the text calls this a similar picture, and the unit of the count is not clear.**

| Field | Content |
|---|---|
| Check | P20, P36 |
| Location | p. 17, l. 369 to 372 (Sect. 4.8); p. 14, l. 322 to 323 (Sect. 4.4) |
| Quotation | "He used voice mode in almost all sessions and the screen in only three or four cases"; "The learning records show a similar picture: 23 of the 25 sessions took place entirely in the voice call, one on screen and one partly on screen" |
| Concern | The records give at most 1 + 1 = 2 sessions with screen use, the learner's account 3 or 4. The text calls this "a similar picture" without resolving the difference. One possible resolution is that the learner also counts the two review sessions, which can run on screen (Fig. 2 caption, l. 153), giving 2 + 2 = 4; the manuscript does not say in which mode the reviews ran. Another is that trial runs, which are not entered in the learning record (l. 226), are counted. In addition, "cases" is the paper's term for its five study cases (Sect. 3.1) and is used here for sessions. |
| Suggestion | In Sect. 4.8 (l. 369 to 372), state what the learner's count includes (sessions, reviews, trial runs) or name the difference to the records explicitly, and give the mode of the reviews if they explain it; replace "in only three or four cases" with "in only three or four sessions". |
| Status | verified (counts); assumption (resolution via review sessions or trial runs), put as a question |
| Severity | minor |
| Source | S3, SD |

#### Minor corrections

| ID | Location | Quotation | Replacement | Source |
|---|---|---|---|---|
| KK-07 | p. 13, l. 306 to 307; Table 6 (p. 16), row 3, column Trigger | "chapters that the learning path itself marks as no learning material"; "chapters that the learning path marks as no learning material" | "chapters that the learning path itself marks as not being learning material"; "chapters that the learning path marks as not being learning material" | S4 |
| KK-08 | Fig. 4 caption, l. 331 (p. 15); the x-axis labels "28 Sep" to "13 Oct" show no year | "Fig. 4. Answers per session by date, for the two cases with sessions" | "Fig. 4. Answers per session by date, 28 September to 13 October 2026, for the two cases with sessions" | AB |
| KK-09 | Table 6 (p. 16), row 4, column Trigger | "an own list of exclusions replaced the default" | "a list of exclusions of its own replaced the default" | S4 |
| KK-10 | Table 6 (p. 16), row 4, column Rule or remedy | "proposal that own exclusions supplement the default" | "proposal that exclusions named in the learning path supplement the default" | S4 |
| KK-11 | Table 6 (p. 16), row 8, column Trigger | "the voice gave a hint on question 4.3" | "the assistant gave a hint in the call on question 4.3" | S4 |
| KK-12 | Fig. 5 caption, p. 17, l. 359 | "how many sessions were run per day (Table 1)" | how many sessions were run per day (Fig. 4; totals per case in Table 1); Table 1 gives only totals per case, the sessions by date are in Fig. 4 | S3, S4, AB |

#### Verification log

| ID | Check | Checked | Values | Result |
|---|---|---|---|---|
| PP-43 | P2, P22 | Count of learning paths, runs and paths with exclusions: Abstract l. 13 to 16, l. 301, l. 306, Table 4, Fig. 1, Discussion l. 384 to 385 | 7 rows, version 5 = version 6, so 6 paths; "two versions of the path on southern Norway" in the Abstract = versions 5/6 and 7; three paths with exclusions (narrative, Germany, volcanology) in all five places | no finding |
| PP-44 | P2 | Number of sessions and modes across Abstract l. 16 to 17, Table 1, Sect. 4.4, Sect. 4.8, Fig. 6 | 15 (11 + 4) + 10 = 25; 23 + 1 + 1 = 25; "23 of the 25" in Abstract, l. 322, l. 371, Fig. 6 | no finding; the first voice session of 29 September is excluded by the caption of Table 1 and in l. 336 to 337, disclosed |
| PP-45 | P2 | Skill versions per session and per rule: Sect. 3.6 l. 262 to 272, Fig. 4 shading, Table 6, Table A2, Discussion l. 390 | 3 sessions under 2.3.1, 8 under 2.4.0, 4 + 10 = 14 under 2.5.0, total 25; Table 6 versions 2.4.0, 2.6.0 first line, 2.6.1, 2.6.5, 2.6.6 match Table A2; deviations in Table 6 nos. 6, 7, 8 match the triangles over narrative sessions 6 and 7, southern Norway sessions 4, 9 and 17, narrative session 10 in Fig. 4 | no finding |
| PP-46 | P2 | Narrative version: 144 sentences (l. 292 to 293, l. 344, l. 383); dates 5 to 7 October (l. 349 to 350) against Fig. 5 circles 5 + 4 + 1 = 10; southern Norway 3 + 4 + 4 + 4 = 15, last session 8 October (l. 338) | values identical | no finding |
| PP-47 | P2 | "first seven sessions" (l. 399) against Table 6, no. 6 "sessions 1 to 7" and Abstract l. 19 to 20 | two deviating sessions (6 and 7) within sessions 1 to 7; sessions 8 to 10 asked as worded | no finding |
| PP-48 | P1 | Table 1: questions as three per session; mean words per session against the target of about 550 words (Sect. 3.5.2) | 31 x 3 = 93, 11 x 3 = 33, 10 x 3 = 30, 25 x 3 = 75, 38 x 3 = 114; mean words per session 460.2, 326.8, 469.2, 387.3, 513.7 | no finding |
| PP-49 | P2 | Table 1 against Table 4 and Fig. 1, per learning path: words, sessions, questions | 14,267/31/93; 3,595/11/33; 4,692/10/30; 9,682/25/75; 19,519/38/114 identical in both tables; Fig. 1 bars 31, 11, 10, 25, 38 and sessions run 15 and 10 | no finding; definitions of Words differ (see GB-22) |
| PP-50 | P2 | Table 1 "latest version with documented check run" against later learning paths on the geological eras | 11 and 10 sessions in Tables 1 and 4; later cut into 15 and 14 sessions without full check run | disclosed in the caption of Table 1; no finding |
| PP-51 | P33 | effort statements | working hours not recorded (p. 13 l. 294); building in chat days (27 to 30 Sep, 2 to 9 Oct, 8 to 9 Oct); session length 5 to 10 min by account (p. 9 l. 190; p. 17 l. 375) | no finding; effort not used as a result, session length marked as own account |
| PP-52 | P1 | Table 4: anchors two per session, answers three per session, all seven rows | 60 = 2 x 30, 62 = 2 x 31, 22 = 2 x 11, 20 = 2 x 10, 50 = 2 x 25, 76 = 2 x 38; 90, 93, 33, 30, 75, 114 = 3 x sessions | no finding |
| PP-53 | P11 | Matrix cases x reported results: build period (Sect. 4.1), check run (Table 4), answers (Table 5), To review (Sect. 4.5), stumbling points (Table 6) | build period given for all five cases; check run for all six paths; answers and To review for the two cases with sessions, the other three disclosed as without sessions (l. 114, l. 464 to 465); Table 5 has the same columns for each row | no finding apart from GB-19, GB-21, GB-23, GB-29 |
| PP-54 | P30, P37 | regrading and re-measurement | Table 5 caption names regrading; SN v5 re-measurement named in Table 4 caption (13,859 to 13,890) | no finding apart from GB-27 and GB-23 |
| PP-55 | P5 | numeric rules against own tables | anchors 2 per session in all rows (60, 60, 62, 22, 20, 50, 76); questions 3 per session (93, 33, 30, 75, 114); Table 5 row sums 33, 12, 30; Fig. 4 bars equal Table 5; version 7: 8 + 5 + 4 = 17, 31 to 17 = 14 open; narrative To review 14, 13 open; example pair 28 of 30 sessions within 550 words (93.3 %); Table A3 session 496 words; expected answers 24, 21, 22 words | no finding apart from GB-28 and GB-18 |
| PP-56 | P9 | confounding of path, skill version, question style and case | no comparisons drawn: modes (p. 14 l. 323), paths (l. 324), before and after 2.5.0 (p. 20 l. 442 to 444), narrative and source (p. 16 l. 350 to 351) | no finding; disclosed |
| PP-57 | P1, P2 | Table 5 row sums; sessions x 3; text of Sect. 4.6; integer stacks of Fig. 4 counted at the page image (exact measurement is with AB) | version 6: 12 + 8 + 13 = 33 = 3 x 11; version 7: 1 + 5 + 6 = 12 = 3 x 4; narrative: 16 + 6 + 8 = 30 = 3 x 10, as in l. 350; Fig. 4 counts 12/8/13, 1/5/6, 16/6/8 | no finding |
| PP-58 | P23 | To review totals and their match to Table 5 for version 7 and the narrative version | 24 + 11 = 35; 35 minus 2 minus 1 = 32 open; version 7: 11 entries = 5 + 6; narrative: 14 entries = 6 + 8, 14 minus 1 = 13 open; Discussion l. 438 repeats 32 and 13 | no finding (version 6: see GB-28) |
| PP-59 | P21 | Comparisons of absolute counts in Results and Discussion: Table 5 rows, reread requests (l. 316 to 318), open entries 32 and 13 (l. 438) | shares correct computed for reference only: 12/33 = 36.4 %, 1/12 = 8.3 %, 16/30 = 53.3 %; no comparison is drawn in the text | no finding; the manuscript itself excludes comparison of modes and of the two paths (l. 323 to 325) and before and after 2.5.0 (l. 442 to 444) |
| PP-60 | P3 | Fig. 4 segments counted per bar against Table 5 and l. 349 to 350 (`f4_balken.py`, colours #049c74 correct, #e49c04 partially correct, #d45c04 not correct, measured on legend fields and bars, deviation 0) | One answer = 115 to 116 px (y = 3 at 646 px, y = 0 at 993 px). Southern Norway version 6, sessions 1 to 11: 12 correct, 8 partially correct, 13 not correct, 33 answers. Version 7, sessions 14 to 17: 1, 5, 6, 12. Narrative version, sessions 1 to 10: 16, 6, 8, 30. Number of bars 11, 4, 10 = Table 5 sessions. Shading colours equal legend fields: 2.3.1 #ecf4fc, 2.4.0 #d4e4f4, 2.5.0 #f4e4ec; case lines #0474b4 and #6c3c9c equal legend lines | no finding; all three rows of Table 5 and the narrative counts of l. 350 confirmed. The manuscript says itself that the grades are process data, not a measure of learning success (caption l. 334, l. 256 to 257) |
| PP-61 | P24 | Fig. 4 date axis: sessions per day, versions in use, triangles, star (x calibrated on 16 ticks, 28 Sep 482.5 px to 13 Oct 2052.0 px; ticks mark the day, bars centred on them) | Southern Norway 1 to 3 on 30 Sep, 4 to 7 on 1 Oct, 8 to 11 on 2 Oct, 14 to 17 on 8 Oct (last session 8 Oct, l. 338); narrative 1 to 5 on 5 Oct, 6 to 9 on 6 Oct, 10 on 7 Oct (between 5 and 7 Oct, l. 349 to 350); star on 29 Sep (l. 337). Shading 2.3.1 for 1 to 3, 2.4.0 for 4 to 11, 2.5.0 for narrative and 14 to 17 (l. 262 to 268). Triangles: 8 over session 4 and narrative session 10, 7 over session 9 and session 17, 6 over narrative sessions 6 and 7 (Table 6 nos. 6 to 8; "in two sessions", l. 399 to 400). 2.4.0 line at 30 Sep + 0.50 day, after sessions 1 to 3 (l. 264) | no finding on sessions and triangles; for the missing 9 Oct lines see GB-26. The manuscript states itself that the version for sessions 4 to 11 is inferred (caption l. 332, l. 263) |
| PP-62 | P24 | Fig. 5 dates against Sect. 4.1, Fig. 4, Table A2, Sect. 4.3 and 3.6 (x calibrated on gridlines at day start, 27 Sep 615.0 px, 8 Oct 1655.0 px; labels left-aligned at their gridline) | Build bars: southern Norway 27 Sep + 0.06 to 30 Sep + 0.93 (27 to 30 Sep, l. 295); eras and narrative 2 Oct + 0.07 to 5 Oct + 0.94 (from 2 Oct, path checked 5 Oct, l. 297 to 298); Germany 2 Oct + 0.07 to 9 Oct + 0.93 (l. 298 to 299); volcanology 8 Oct + 0.07 to 9 Oct + 0.93 (l. 299). Circles at day + 0.60: southern Norway 3, 4, 4, 4 on 30 Sep, 1 Oct, 2 Oct, 8 Oct = 15; narrative 5, 4, 1 on 5, 6, 7 Oct = 10, same as Fig. 4; circle colours #0474b4 and #6c3c9c = Fig. 4. Diamonds at day + 0.50: questions on relations 4 Oct (2.5.0, 3 to 5 Oct), end of excerpt 5 Oct (third narrative session, l. 318), questions shown before the call 6 Oct (narrative sessions 8 to 10, l. 269), do not interrupt 12 Oct (2.6.5, l. 390). Shaded area from 9 Oct, "no sessions after 8 October" | no finding on these values; for the missing versions see GB-31 |
| PP-63 | P36 | "often ran two sessions" on 30 minute drives | sessions per day measured in Fig. 4 and Fig. 5: 3, 4, 4, 5, 4, 1, 4 | no finding; records allow two or more sessions on 6 of 7 days |
| PP-64 | P3 | Fig. 6 against Sect. 3.6 (l. 252 to 256) and Sect. 4.8 | Three criteria as in l. 253 to 256; "23 of 25 sessions entirely in the voice call" = l. 322 to 323 and 371; "often two sessions on a 30-minute drive" = l. 372 to 373; "up to about 550 words, three questions" = l. 205 to 207 | no finding; the manuscript states itself that the right-hand column is not a measured outcome (caption l. 378 to 379) |
| PP-65 | P1, P23 | Progress of version 7 on southern Norway, Sect. 4.4 against Sect. 3.5.3 | 8 + 5 + 4 = 17 done, 31 minus 17 = 14 open; l. 229 to 230 eight credited, five closed | no finding |
| PP-66 | P20 | Denominators of quotas in Segment 3 | Anchors and Answers defined as "of all" (Table 4 caption); "of 30 questions" (l. 350); "17 of the 31 sessions ... done" with "done" defined by its three parts (l. 325 to 326); "23 of the 25 sessions" (l. 322) | no finding (exceptions: GB-22, GB-20, GB-32) |
| PP-67 | P2, P21 | Word count of the same path (versions 5 and 6) under different scripts | 13,890 (2.6.6 and script of 30 September) against 13,859 (original run), difference 31 | disclosed in the caption of Table 4; consequence for the other rows in GB-23 |

### Segment 4: Discussion, conclusions, declarations, references (p. 12; p. 18 to 26)

#### Substantive findings

**GB-33 The two gaps of Sect. 2 that correspond to RQ2 and RQ3 are not taken up again in the Discussion or the Conclusions.**

| Field | Content |
|---|---|
| Check | P15 |
| Location | p. 18, l. 387 to 393 (answers to RQ2 and RQ3); p. 4, l. 101 to 108 (third and fourth respects); p. 4, l. 73 to 78 and l. 83 to 90 (literature); p. 14, l. 319 to 320 |
| Quotation | "Third, listening alone has been compared with reading in many studies, ... none of the studies reviewed here, however, combines listening alone with spoken answers in self-study ... Fourth, in the journal studies the learners write the journals themselves, whereas here the AI assistant keeps the learning record on the learner's behalf. ... the third to RQ2 and the fourth to RQ3." |
| Concern | Sect. 2 introduces five respects of the gap and assigns the third to RQ2 and the fourth to RQ3 (l. 107 to 108). The first and second respects (learner-supplied fact document; narrative version) are taken up in the Discussion (l. 394 to 397, l. 412 to 417), as are spacing, microlearning, mobile learning, self-regulated learning and elaborative interrogation. The literature behind the third respect (Clinton-Lisell, 2022 and 2023; Putnam and Roediger, 2013; Terzopoulos and Satratzemi, 2020) and behind the fourth (Nückles et al., 2020; Zhang et al., 2022) does not occur in Sect. 5 or 6 (full-text search of l. 380 to 482). For RQ2, only the Results say that the listening requests "cannot be set against them" (l. 319 to 320). For RQ3 the omission matters for the argument: Nückles et al. (2020), as cited in l. 84 to 86, locate the benefit of journals in the learner's own writing, and the design here moves the writing to the assistant; the Discussion of RQ3 (l. 391 to 393) does not say what this means for the record as a learning aid. The moderators of Clinton-Lisell (2022) are raised in GB-04. Moderate: the answers to RQ2 and RQ3 stand, but the contribution claimed for them in Sect. 2 is not traced to the end, so the reader cannot follow how the results fill the stated gap. |
| Suggestion | Add to Sect. 5, after the answers to RQ2 and RQ3, one paragraph each that returns to the third and fourth respects: what the voice sessions add to or cannot say about listening with spoken answers, and what is gained or lost when the assistant, not the learner, writes the learning record, in the light of Nückles et al. (2020). |
| Status | verified (full-text search of Sect. 5 and 6, l. 380 to 482, for the cited authors and for "journal" and "listen") |
| Severity | moderate |
| Source | S4 |

**GB-34 The answer to RQ2 lists rules as arising from incidents in real sessions for which the Results contain no incident, one of them set after the last session, and Table 6 does not say by which rule it selects its stumbling points.**

| Field | Content |
|---|---|
| Check | P15, P34 |
| Location | p. 18, l. 389 to 391; Table 6; Fig. 5, row Rules from incidents and requests, diamond do not interrupt the learner; Table A2, rows 2.6.0, first line, and 2.6.5; p. 16, l. 353 to 355; p. 14, l. 315 to 320; p. 10, l. 209 to 211; p. 20, l. 430 to 432; p. 6, l. 138 to 139 |
| Quotation | "The rules for the call came from incidents and requests in real sessions: questions shown before the call and asked as worded, decimal digits spoken one by one, the end of the excerpt announced and, in version 2.6.5, rules against interrupting the learner." (l. 389 to 391); l. 353: "Table 6 lists the stumbling points documented in the learning records and in the analyses of the chats" |
| Concern | Two of the four rules have a location in the Results: the end of the excerpt announced (l. 318) and questions shown before the call (Table 6, no. 6; l. 399 to 401). For "decimal digits spoken one by one" and "rules against interrupting the learner" no incident or request is reported in Sect. 4.3, 4.4, 4.7 or Table 6 (full-text search for "decimal" and "interrupt"); the two rules appear only as changes in Table A2 and, for decimal digits, as a rule in Sect. 3.5.1 (l. 198). Fig. 5 places the diamond "do not interrupt the learner" at about 12 October, inside its own shaded area "no sessions after 8 October", and Sect. 3.6 states that no session ran under 2.6.5 or 2.6.6 (l. 271 to 272). An incident in a session of the data can therefore have produced this rule only before 8 October, and the manuscript does not name it. Table 6 is introduced as the list of documented stumbling points, but of the four rules only the first has a row there, and further incidents named elsewhere in the paper have none: the spoken "not quite right" entered as "not correct" (l. 209 to 211), the end of excerpt rule from the third narrative session (l. 318), the two limits of the open question rule (l. 430 to 432) and the refusal to recite the excerpt in the call that produced the division into two channels (l. 138 to 139). Fig. 5 shows "some of these rules" (l. 354) without a selection rule. RQ2 asks explicitly "which rules for the assistant arose from incidents in real sessions" (l. 46), so this part of the answer is stated without a result, and a reader cannot tell whether Table 6 is complete or a selection. The rules themselves are documented in Table A2; what is missing is the traceability of their origin, hence moderate. |
| Suggestion | Report in Sect. 4.3 or as rows of Table 6 the incidents or requests from which the rules on decimal digits and on not interrupting the learner arose (case, session, date), or remove them from the list in l. 389 to 391 and say that they were added without a documented incident; either add the further incidents to Table 6 or state in Sect. 4.7 (l. 353 to 355) the rule by which Table 6 and Fig. 5 select. |
| Status | verified (full-text search for "decimal" and "interrupt"; Fig. 5 and Table A2 at the page images) |
| Severity | moderate |
| Source | S4, SD |

**GB-35 The verbatim principle is said to work as a safeguard, but of its four links only the first was measured; reading and asking in the call were not audited across the 25 sessions.**

| Field | Content |
|---|---|
| Check | P31 |
| Location | p. 18 l. 394; p. 19 l. 396 to 403; Fig. 7 caption p. 19 l. 408 to 411; p. 9 l. 194 to 200; p. 11 l. 232 to 233 |
| Quotation | "The verbatim principle works as a safeguard of the kind that the tutoring studies built into their prompts"; "The design is meant to leave no room for either kind of hallucination"; "Reading the excerpt, asking the questions and grading in the call rest only on rules or procedure" |
| Concern | The discussion itself concedes that the principle does not enforce itself and that the links after the learning path rest on rules. The sentence at l. 394, though, states an effect. What was measured is that expected answers occur in the excerpts (Table 4). Whether the excerpt was read verbatim was not measured in any session, and whether the questions were asked as worded is known only from deviations that surfaced in records and analyses (Table 6 rows 6 to 8: 4 of 25 sessions, 16 %, with questions other than in the path, plus 2 hints). Without an audit of all sessions, these four are a lower bound. Whether the chats hold the assistant's spoken output in text form, which would allow such an audit, is not stated (only voice input is described, l. 233); this part is a question. Major: the effect of the safeguard is the core contribution, and the answer to RQ2 on how sessions run depends on what happened in the call. |
| Suggestion | Counter design: for each of the 25 sessions, compare the text the assistant spoke in the call (if the chat holds it) with the excerpt by a word level diff, and each asked question with the path; report per session the share of words changed and the number of questions asked as worded, in a new table in Sect. 4.3 and 4.4. If the spoken output is not available, say so in Sect. 3.6 and change l. 394 to "is meant to work as a safeguard". |
| Status | verified (only the first link measured; effect sentence); inferred (16 % lower bound, 4/25); assumption (availability of spoken output) |
| Severity | major |
| Source | SD |

**GB-36 The design is said to bind every session to the fact document and to leave no room for either kind of hallucination, while review sessions add an introduction, a summary and an explanation mode that allows general knowledge.**

| Field | Content |
|---|---|
| Check | P15, P26 |
| Location | p. 19, l. 397 to 398; p. 2, l. 31 to 33; p. 11, l. 224 to 227; p. 20, l. 432 to 433 and l. 448 to 449; Table A2, rows 2.4.0 and 2.6.0, first line; Fig. 7 |
| Quotation | "The design is meant to leave no room for either kind of hallucination distinguished by Ji et al. (2023), statements that contradict the source and statements that the source can neither support nor contradict." (l. 397 to 398); l. 32: "binds every session to a fact document that the learner supplies"; l. 432 to 433: "An explanation mode in which general knowledge is allowed was later introduced for review sessions" |
| Concern | The manuscript separates well what the check script secures and what rests on rules (l. 401 to 403, Fig. 7). The sentence in l. 397 to 398 and the binding of "every session" in l. 32, however, are made for the design as a whole. By the manuscript's own description, the default review mode ('both', Table A2, 2.6.0 first line) has each topic begin "with an introduction" and continue with "the core passage read verbatim from the fact document and a closing summary" (l. 224 to 225), and the explanation mode, offered for reviews since version 2.4.0 (Table A2), allows general knowledge (l. 432 to 433, l. 448 to 449). Statements from general knowledge are by definition statements the fact document can neither support nor contradict, the extrinsic kind named in l. 63 to 64. The design thus opens room for this kind in review sessions on purpose; the two sentences hold only for regular sessions, and Fig. 7 shows no link for the review path. The verbatim binding of regular sessions stays; what the reader cannot see from the Discussion is that one part of the design is not covered by it. |
| Suggestion | Restrict the sentences in l. 32 and l. 397 to 398 to regular sessions; state in Sect. 3.5.3 (l. 224 to 227) that introduction, summary and the explanation mode lie outside the verbatim binding, with the consequence for what the learner hears in them; add the review path to Fig. 7. |
| Status | verified (explanation mode with general knowledge, l. 432 to 433 and l. 448 to 449; Table A2); inferred (that introduction and summary of the default mode are generated by the model, which the manuscript does not state explicitly, though it distinguishes them from the passage read verbatim, l. 225) |
| Severity | moderate |
| Source | S4, SD |

**GB-37 In Fig. 7, the arrow from "Sources" to "Fact document" is dashed, while the legend and caption call it dotted.**

| Field | Content |
|---|---|
| Check | P3 |
| Location | Fig. 7, lower panel, arrow between the boxes "Sources" and "Fact document (supplied by the learner)", and legend entry "checked in the document project" (p. 19); caption l. 409 |
| Quotation | "How the fact document matches its sources was checked in its document project, by different procedures (dotted line, Sect. 4.1)" (caption l. 408 to 409); legend: "checked in the document project" |
| Concern | Fig. 7 tells three kinds of link apart by colour and line style, and that is how it makes the point of Sect. 5 visible. The colour of the arrow matches its legend entry (#e69f02 against #e6a107, deviation below 40). But a horizontal profile at y = 1458 px through the arrow gives yellow runs of 10 and 11 px with a gap of 6 px before the arrowhead. The same profile through the legend entry at y = 1770 px gives square dots of 5 to 6 px with gaps of 10 to 11 px. The "secured only by rules or procedure" legend entry has dashes of 19 to 21 px. Measured this way, the arrow is a short-dashed line, matching neither the dotted legend sample nor the caption's "dotted line". At print size, the arrow reads as one of the "dashed lines" that the caption reserves for links secured only by rules (l. 410), and colour alone carries the difference. |
| Suggestion | Draw the arrow "Sources" to "Fact document" in Fig. 7 with the same dotted style as the legend sample. |
| Status | verified (measured) |
| Severity | minor |
| Source | AB |

**GB-38 The Discussion dates the count of 13 open entries for the narrative version to 8 October 2026, whereas Sect. 4.5 gives that date only for southern Norway.**

| Field | Content |
|---|---|
| Check | P2 |
| Location | p. 20, l. 438 to 439 (Sect. 5); p. 15, l. 338 to 340 (Sect. 4.5) |
| Quotation | "on 8 October 2026 the list To review held 32 open entries for southern Norway and 13 for the narrative version" (l. 438 to 439); l. 338 to 340: "On 8 October 2026, the day of the last session on southern Norway, and unchanged until the cut-off date, the list To review held 35 entries for that case ... For the narrative version, it held 14 entries, of which 13 were open." |
| Concern | In Sect. 4.5 the date and the remark "unchanged until the cut-off date" apply to southern Norway ("for that case"); the count for the narrative version has no date. Whether it was 13 on 8 October depends on when its review was completed, which the manuscript does not state; if that review took place after 8 October, the count on that day was 14. |
| Suggestion | Give the date of the narrative version's count in Sect. 4.5, and in l. 438 either use the cut-off date 13 October 2026 for both counts or give one date per case. |
| Status | dates and counts verified; the possible difference is an assumption, put as a question |
| Severity | minor |
| Source | S3 |

**GB-39 The conclusion attributes the building of the learning environment to the learner alone, while Sect. 3.7, Sect. 5 and Fig. 8 assign the drafting and building of the skill versions to the assistant.**

| Field | Content |
|---|---|
| Check | P15 |
| Location | p. 22, l. 469; held against p. 12, l. 277 to 278; p. 20, l. 446 to 447; Fig. 8 caption (p. 21), l. 459 to 460; p. 24, l. 502 to 503 |
| Quotation | "He built the learning environment himself and adapted it while using it, instead of receiving a finished system that cannot be changed." |
| Concern | The manuscript describes the division of work carefully elsewhere: "Claude also drafted the wording of the rules of the skill lernpfad-sitzungen and built its versions, which the author installed and used" (l. 277 to 278); "The purpose and criteria of its parts came from him, ..., while the assistant proposed their structure" (l. 446 to 447); "the AI assistant ... proposed the structure and wording of the rules" (l. 459 to 460); the author contributions say "with the AI assistance described in Sect. 3.7" (l. 502 to 503). "Himself" in the conclusion is stronger than these statements, and the contrast "instead of receiving a finished system" has no counterpart in the Results. Minor: the division of work is disclosed correctly in Sect. 3.7, Sect. 5 and Fig. 8; only the wording of the conclusion deviates. |
| Suggestion | Replace l. 469 to 470 with, for example: "He set the purpose and criteria of the learning environment, had the assistant draft and build the skill, and adapted it while using it." |
| Status | verified |
| Severity | minor |
| Source | S4 |

**GB-40 The proposed retention test relies on parts of the environment that the manuscript itself shows to be unsuited for it, and its comparison of reviewed with non-reviewed questions would confound the review with the selection into review.**

| Field | Content |
|---|---|
| Check | P15, P9 |
| Location | p. 22, l. 473 to 475; held against p. 14, l. 325 to 327; p. 11, l. 221 to 224 and l. 228 to 230; p. 20, l. 434 to 439; p. 12, l. 256 to 257; p. 20, l. 422 to 425 and l. 428 to 431; Table 6, rows 6, 7 and 8; p. 12, l. 270 to 272 |
| Quotation | "Retention could be tested next by asking the questions of completed sessions again after fixed intervals and comparing questions that were taken up in review sessions with questions that were not; the list To review already records which entries were reviewed and when." |
| Concern | The outlook is the only proposed study, and it asks the right next question. Held against the manuscript's own findings, four parts of it are weakened. (1) "questions of completed sessions": of the 17 completed sessions of version 7 on southern Norway, 8 were credited from version 6 and 5 closed without being asked (l. 325 to 327), so 13 of 17 = 76.5 % of these completed sessions have no answered questions to repeat (Python). (2) "after fixed intervals": review sessions "follow no schedule" and draw on a queue on demand, which "allows spacing but does not ensure it" (l. 434 to 437); the skill has no mechanism for fixed intervals. (3) The outcome would again be a grade given by the language model in the call, which the manuscript defines as process data "not used as a measure of learning success" (l. 256 to 257), checked by no second grader (l. 424 to 425); Table 6 shows questions asked other than those in the learning path (rows 6 and 7) and hints given in the call (row 8), and the remedies (noting deviations and hints) entered the skill only with 2.6.6, under which no session ran (l. 271 to 272). (4) "comparing questions that were taken up in review sessions with questions that were not": only questions answered incorrectly or partially correctly enter To review (l. 221), reviews start on request and serve the oldest entries first (l. 222 to 224), so non-reviewed questions are mostly those answered correctly at first, or newer entries. A difference at retest would mix the effect of the review with the first grade, including regression towards the mean, with the time since first exposure and with the learner's choice of when to review; asking the same verbatim questions again also measures recall of the expected wording rather than of the content. In addition, 32 of 35 and 13 of 14 entries were still open and only two reviews with one topic each took place (l. 340 to 341, l. 437 to 439). The statement that the list "already records which entries were reviewed and when" is correct (Table 3), but the one open question recorded so far is not in the record kept for that case today, and its wording had been shortened (l. 428 to 431). Moderate: the proposal does not change a result, but as written it could not be carried out with the environment described and would not answer its question. |
| Suggestion | Rewrite the outlook in l. 473 to 475 so that it names what the test needs beyond the present environment: a schedule for the repeated questions; only sessions whose questions were actually asked; assignment of the entries of the list To review at random to review or to no review (waiting list); a retest of all entries and of a sample of correctly answered questions after fixed intervals, with for each item a second question with a different verbatim answer from the same excerpt; a grading that does not rest on the call alone, for example recorded answers graded by a second grader blind to the condition; and the 2.6.6 logging of deviations and hints. |
| Status | verified (all passages held against confirmed in the text and in Table 3); inferred (share 13 of 17; the confounding) |
| Severity | moderate |
| Source | S4, SD |

**GB-41 The conclusion that the skill "works with any fact document that can be checked" contradicts the five conditions and the corrections the manuscript reports.**

| Field | Content |
|---|---|
| Check | P15 |
| Location | p. 22, l. 476 to 477; held against p. 8, l. 168 to 180 (Sect. 3.3 and 3.4); p. 13, l. 306 to 307; Table 4 (p. 14), column "Exclusions and corrections until passed"; p. 13, l. 285 to 287 |
| Quotation | "The method is not tied to the geosciences: the rules of the skill contain no subject content, and the skill works with any fact document that can be checked." |
| Concern | Sect. 3.3 says that a user needs "a document in Markdown that meets the five conditions in Sect. 3.4 and has been checked against its sources" (l. 168 to 169), and Sect. 3.4 lists conditions on paragraphs, minimum length of opening paragraphs, first table cells, exclusions and image blocks (l. 173 to 180). Three of six paths passed only after exclusions, one needed an anchor set by hand (l. 306 to 307, Table 4), and the volcanology document had a paragraph error the comparison could not detect (l. 285 to 287). "Any fact document that can be checked" is therefore wider than the manuscript's own conditions. The first clause, "is not tied to the geosciences", is stated as a fact, while the same paragraph and the abstract say that use in other subjects "has not been tested" (l. 479 to 480; l. 21 to 22); all four cases are geoscience topics (l. 477). Moderate: the statement concerns what a reader can expect when reusing the published skill (Code and data availability), not a result of the study; it misleads a reader who wants to reproduce the approach with another document. |
| Suggestion | Replace l. 476 to 477 with a sentence bound to the conditions, for example: "The rules of the skill contain no subject content, and the skill can cut any fact document that meets the five conditions of Sect. 3.4 and has been checked against its sources; whether the method serves subjects outside the geosciences has not been tested." |
| Status | verified |
| Severity | moderate |
| Source | S4 |

**GB-42 The Code and data availability statement covers only the skill package, withholds two data sources without a reason and does not mention several data sources named in Sect. 3 and 4.**

| Field | Content |
|---|---|
| Check | P12 |
| Location | Code and data availability, p. 24, l. 495 to 500; Sect. 3.1, p. 5, l. 111 to 114; Sect. 3.3, p. 7, l. 157 to 158 and p. 8, l. 164 to 167; Sect. 3.5.1, p. 10, l. 202 to 203; Sect. 3.5.3, p. 10, l. 218 to 219; Sect. 3.6, p. 11, l. 232 to 239 and l. 245 to 249; p. 12, l. 262 to 272; Sect. 4.1, p. 13, l. 284 and l. 292 to 293; Sect. 4.6, p. 15, l. 344 to 345 |
| Quotation | "The summary figures per case on which this paper is based are reported in the paper itself; the complete learning records and the method analyses of the chats are not published." (l. 498 to 500); l. 232 to 233: "The data come from four kinds of source. First, the chats in which the fact documents and learning paths were built and the sessions were held"; l. 218 to 219: "The example entries are invented, because the records themselves are not published." |
| Concern | Sect. 3.6 names four kinds of source, and the statement addresses two of them (learning records, method analyses: "not published"), three times without a reason (l. 218 to 219, l. 239, l. 499 to 500). The learning records concern the learner as a person, so withholding them needs no further justification under P12, although a reason would help. The method analyses are the basis of Table 6 and of several counts in the Methods ("22 of 41 inputs of three words or fewer", l. 134; "18 deviations", "85 and 93 statements, of which 30 and 37 deviated", l. 245 to 246); whether they contain personal data is not stated. The statement says nothing about these sources named in the paper: (1) the chats themselves, including the speech recognition text of voice inputs, the saved transcripts and the chat log kept by the assistant (l. 232 to 233, l. 247 to 249); (2) the output of the check script for the seven runs of Table 4 (l. 237 to 238), of which only the run on the example pair can be repeated from the package; (3) the fact documents and learning paths of the five cases (l. 113), while the package holds only the example pair, the fact document on southern Norway with its learning path in version 5 (l. 497 to 498), and the sessions ran on versions 6 and 7 of that path and on version 8 of the narrative path (Table 1); (4) the skill versions 2.3.1, 2.4.0 and 2.5.0 under which the sessions ran (l. 262 to 268), while the statement offers only 2.6.6 (l. 495), under which "no session in the data ran" (l. 271 to 272); (5) the source material of the fact documents: the ICS chart "edition v2026/06, in the file he supplied" (l. 164 to 165), the open-access sources and the openly licensed textbooks (l. 166 to 167), none of which is named or cited; (6) the booklet of 15 maps used for the narrative version (l. 203); (7) the reports of the separate agent that checked three method analyses and the later meta-analysis of the first (l. 245 to 247); (8) the per-session grades, shown only graphically in Fig. 4 and given in the tables only as totals per learning path (Table 5); (9) the project script used to extract the volcanology text (l. 284), the inventory of the 144 sentences (l. 292 to 293, l. 344) and the output of the second AI agent that checked the narrative version (l. 344 to 345). For items 2, 3, 5, 6 and 9 the data do not concern persons, and the fact documents on Germany and volcanology rest on openly available or openly licensed sources (l. 166 to 167), so no obstacle to publication follows from the manuscript itself. The repository is given by a GitHub address without a persistent identifier or release tag; its reachability was not checked. For comparison, the data policy of Copernicus journals, as published for Biogeosciences and read by instance S2, asks for a statement "on how their underlying research data can be accessed" and requires "a detailed explanation" where data cannot be deposited (https://www.biogeosciences.net/about/data_policy.html, accessed 16 October 2026); the target journal is not named in the manuscript, so the applicability of this policy is inferred. |
| Suggestion | In Code and data availability (p. 24, l. 495 to 500), address each of the nine sources: publish the fact documents and learning paths of all five cases (at least those under open licences), the outputs of the check runs in Table 4, the skill versions 2.3.1, 2.4.0 and 2.5.0, the sentence inventory and the per-session grades in a repository with a persistent identifier and a release for 2.6.6; name and cite the ICS chart edition, the textbooks and the open-access sources in Sect. 3.3 and in the reference list; for the chats, the agent reports, the method analyses and the map booklet, state whether they are available and, if not, why; if no personal data stand in the way, publish the method analyses or the passages on which Table 6 and the counts in Sect. 3.2 and 3.6 rest. |
| Status | verified (absence of the nine items from the statement, l. 495 to 500; absence of a reason at l. 218 to 219, l. 239 and l. 499 to 500); inferred (applicability of the Copernicus policy; that items 2, 3, 5, 6 and 9 concern no persons); assumption (whether the method analyses contain personal data), asked as a question; reachability of the repository not checked |
| Severity | moderate |
| Source | S2, S4 |

#### Minor corrections

| ID | Location | Quotation | Replacement | Source |
|---|---|---|---|---|
| KK-13 | Fig. 7, annotation above "Grade in the learning record" (p. 19); "no second grader" appears in Sect. 5, l. 424 to 425, not in Sect. 3.6 | "graded by the language model, no second grader (Sect. 3.6)" | "graded by the language model, no second grader (Sect. 3.6, 5)" | AB |
| KK-14 | p. 24, l. 495 to 496 | "https://github.com/nordie69/Listen-" / "Answer-Memorize" | URL unbroken, or broken after a slash: "https://github.com/nordie69/" / "Listen-Answer-Memorize"; a line break at the URL's own hyphen leaves open whether the hyphen belongs to it | S4 |
| KK-15 | p. 25, l. 530 to 531; p. 26, l. 548 to 549; p. 26, l. 554 to 555 | "https://doi.org/10.1186/s40561-024-" / "00334-5"; "https://doi.org/10.1007/s10648-020-" / "09572-8"; "https://doi.org/10.3758/s13423-020-" / "01853-1" | break after the slash: "https://doi.org/10.1186/" / "s40561-024-00334-5"; "https://doi.org/10.1007/" / "s10648-020-09572-8"; "https://doi.org/10.3758/" / "s13423-020-01853-1" | S4 |
| KK-16 | p. 26, l. 548 (Latimier, Peyre and Ramus); p. 26, l. 559 (Nückles et al.); compare p. 25, l. 512 (Agarwal, Nunes and Blunt) | "Educational Psychology Review, 33, pp. 959-987"; "Educational Psychology Review, 32, pp. 1089-1126"; against "Educational Psychology Review, 33(4), pp. 1409-1453" | "Educational Psychology Review, 33(n), pp. 959-987" with n the issue number of the article (not confirmed in this review); "Educational Psychology Review, 32(4), pp. 1089-1126" (issue 4 confirmed in the record of the Fachportal Pädagogik) | S4 |

#### Verification log

| ID | Check | Checked | Values | Result |
|---|---|---|---|---|
| PP-68 | P4 | every reference to a section, figure, table and appendix, target looked up | Sect. 1 (l. 190, 215: version 2.5.0 and '55 Ma' in l. 40), Sect. 2 (l. 319, 419, 442, 449), Sect. 3.3 (l. 346: l. 159), Sect. 3.4 (l. 169, 238), Sect. 3.5.1 to 3.5.3 (l. 49), Sect. 3.5.2 (l. 186, 329: l. 205, 213), Sect. 3.5.3 (l. 154, 237), Sect. 3.6 (l. 151, 325, 361, 365, 377, 424, 470: versions l. 262 to 272, criteria l. 252 to 256), Sect. 3.7 (l. 503), Sect. 4.1 (l. 30, 170, 359, 387, 409), Sect. 4.2 (l. 117, 182, 186, 282), Sect. 4.3 (l. 361), Sect. 4.4 (l. 372), Sect. 4.5 (l. 236: l. 337), Sect. 4.6 (l. 159, 293, 383, 416), Sect. 4.7 (l. 117, 135: Table 6 row 2), Sect. 4.8 (l. 378, 419), Sect. 5 (l. 351: l. 415 to 417), Fig. 1 to 8, Table 1 to 6, Table A1 to A3, Appendix A, "Code and data availability" (l. 489); in-figure references of Fig. 5, 6, 7, 8 on the page images; Fig. 4 triangles "6 6" over narrative sessions 6 and 7 support "in two sessions" (l. 400) | all targets exist and hold what they are cited for, except Fig. 5 caption "(Table 1)" for sessions per day (KK-12) and the annotation "(Sect. 3.6)" for "no second grader" in Fig. 7, which instance AB found to point to a section that does not mention a second grader (KK-13); decided in the merge at l. 243 to 257 and l. 424 to 425: Sect. 3.6 treats grades as process data but names no second grader, so KK-13 stands |
| PP-69 | P4 | numbering of sections, figures, tables and order of first citation | sections 1 to 6; 3.1 to 3.7; 3.5.1 to 3.5.3; 4.1 to 4.8; Fig. 1 to 8, first cited l. 112, 141, 173, 322, 354, 365, 387, 450; Table 1 to 6, first cited l. 112, 209, 218, 238, 322, 308; Table A1 to A3 cited l. 484 | no gaps, no double numbers; Table 6 is first cited (l. 308) before Table 5 (l. 322); no finding |
| PP-70 | P15 | verbs of Discussion and Conclusions against the evidence | "can be answered as far as the data of a single learner allow" (l. 381); "the data show how the record is kept, not what it achieves" (l. 392 to 393); "works as a safeguard" (l. 394), qualified in l. 398 to 403; "shows that, in this study" (l. 412); "cannot test that expectation" (l. 416); "therefore process data" (l. 424); "allows spacing but does not ensure it", "cannot settle" (l. 437); "makes no claim about retention" (l. 440); "do not show" (l. 442); "cannot be judged from a single case" (l. 453 to 454); "should also suit ... this has not been tested" (l. 478 to 480) | verbs match the evidence, except l. 397 to 398 (GB-36), l. 469 (GB-39) and l. 476 to 477 (GB-41). The manuscript discloses its limits itself (single learner who is also developer, short period, no control condition, own account, sessions on two of five cases, l. 462 to 465; grades as process data, l. 256 to 257; self-analyses, l. 243 to 249); these are not raised again |
| PP-71 | P15 | frameworks and core terms from Sect. 1 and 2 and the research questions, searched in Sect. 5 and 6 | retrieval practice and spacing (l. 52 to 61) taken up l. 434 to 437; hallucination types (l. 62 to 64) l. 397; tutoring studies (l. 64 to 69) l. 394 to 396; microlearning and mobile learning (l. 79 to 82) l. 418 to 419; self-regulated learning and AI interventions (l. 83, 88 to 90) l. 449 to 454; narrative (l. 91 to 96) l. 412 to 417; elaborative interrogation (l. 60) l. 441 to 442; listening and spoken answers (l. 73 to 78, 101 to 104) and learner journals (l. 84 to 88, 104 to 106) not taken up; RQ1 core terms "verified fact documents", "verbatim" in l. 381 to 387 and l. 467; RQ2 "voice call", "rules ... from incidents" in l. 387 to 391 and l. 468 to 469; RQ3 "learning record", "review sessions" in l. 391 to 393 and l. 475 | taken up, except the third and fourth respects of the gap (GB-33); autoethnography (l. 251) as method frame is not taken up in Sect. 5 |
| PP-72 | P15 | numbers in Sect. 5 and 6 against the Results, with Python | 25 sessions = 11 + 4 + 10 (Table 5); 23 in the voice call (l. 322, 371); two reviews with one topic each (l. 341, 392, 437 to 438); open entries southern Norway (24 minus 2 minus 1) + 11 = 32 of 35, narrative 14 minus 1 = 13 (l. 340, 438 to 439); 144 sentences (l. 344, 383); six paths, three after exclusions (Table 4, l. 384 to 385); five limitations counted in l. 462 to 465 | consistent; no finding |
| PP-73 | P3 | Fig. 7 against Sect. 5, Table 6 and Sect. 4.2 | Solid green only fact document to learning path (l. 401 to 402); dashed orange for excerpt, questions, grade (l. 402, 410); annotations "Table 6, no. 6", "hint on question 10.3 (no. 8)", "deviations in southern Norway (no. 7)" match Table 6 rows 6 to 8; legend colours: solid #049c74 type green, dotted #e6a107, dashed #d55e00 | no finding apart from GB-37 and KK-13 |
| PP-74 | P27 | unchecked grades feeding To review and review selection | grades without second grader (p. 20 l. 424 to 425) decide To review entries, which decide review topics (p. 11 l. 221 to 224) | no separate finding; disclosed, consequence drawn for RQ3 (p. 18 l. 392 to 393); deviating questions in GB-24 |
| PP-75 | P31 | effect of the 2.5.0 question rule; tolerant grading; version binding of the record | not compared (p. 20 l. 442 to 444); one instance of version change (p. 11 l. 228 to 230) | no finding; disclosed |
| PP-76 | P3 | Fig. 8 against Sect. 5 (l. 445 to 454), Table 6 and caption | Learning loop: session, record and To review, review on request; tool loop: incident or request, rule, skill version; example "questions asked other than those in the learning path → questions shown before the call" = Table 6 no. 6; dotted lines from "AI assistant" = caption "dotted lines" (l. 460); dashed return lines = l. 461 | no finding; the manuscript states itself that not every incident led to a rule (l. 458) |
| PP-77 | P15 | each statement of Sect. 6 assigned to a location in the Results | "read aloud in a voice call, on screen, and as a narrative version" (l. 468): l. 322 to 323, l. 349 to 350; "adapted it while using it" (l. 469): Sect. 4.7, Table 6, Table A2; "judges the experiment positively ... motivation ... grew" (l. 470 to 471): Sect. 4.8, l. 365 to 375, marked as own account; "Two questions remain open" (l. 471 to 473): l. 20 to 21, l. 440, l. 462 to 465; "four geoscience topics, with fact documents in German and in English" (l. 477 to 478): l. 113 to 114; requirements for other learners (l. 481 to 482): l. 137 to 141 | stated with a location, except "verified" (GB-19), "himself" (GB-39) and "works with any fact document" (GB-41) |
| PP-78 | P9 | other outlook proposals | other learners (p. 22 l. 472 to 473) and other subjects (l. 476 to 480): no study design proposed, untested status stated | no finding |
| PP-79 | P15 | each proposal of the outlook and each rule proposal held against a finding of the manuscript | (1) retention test, l. 473 to 475, against l. 221, 256 to 257, 325 to 327, 424 to 425, 434 to 439, Table 6 rows 6 to 8: GB-40; (2) use in other subjects, l. 476 to 480, against l. 168 to 180 and Table 4: GB-41; (3) requirements for other learners, l. 481 to 482, against l. 137 to 141 (code execution, two channels) and l. 127: consistent; (4) Table 6 row 3, proposal that the check reads exclusions from the learning path, against l. 306 to 307 and Table 4 row Geology of Germany (577 findings caused by chapters the path already marks): consistent; (5) Table 6 row 4, proposal that own exclusions supplement the default, against l. 308 and Table 4 row Geology of Germany (reference chapter had to be added by hand): consistent | proposals (3) to (5) consistent with the manuscript's findings; (1) and (2) are findings |
| PP-80 | P34 | selections from counted sets | example pair: full pair published (p. 24 l. 497 to 498); Table A3 one of 30 sessions, pair available | no finding apart from GB-34 |
| PP-81 | P4 | citations against the reference list in both directions, year and spelling | 25 distinct works cited in the text, 25 entries: Achuthan 2025, Agarwal 2021, Bastani 2025, Cheek 2017, Clinton-Lisell 2022 and 2023, Dahlstrom 2014, Denojean-Mairet 2024, Dunlosky 2013, Ellis 2011, Ji 2023, Kestin 2025, Kortemeyer 2024, Landy 2013, Latimier 2021, Li 2025, Mar 2021, Mohr 2026, Nückles 2020, Panadero 2017, Putnam 2013, Terzopoulos 2020, Traxler 2007, Wilson 2007, Zhang 2022; both Clinton-Lisell citations point to the matching year (l. 76: 2023, reading while listening; l. 102: 2022, listening versus reading) | every citation has an entry and every entry a citation; years and spellings agree (Nückles, Kabakcı, Denojean-Mairet, López-Pernas checked on the page images); "et al." see GB-01; no further finding |
| PP-82 | P16 | language and form of Sect. 3.7, 5, 6, the declarations and the reference list on the page images (p. 12, 18 to 26); uniformity of the reference list | page ranges uniformly with hyphen; access dates only for the two entries without DOI (Clinton-Lisell 2023, l. 525; Wilson et al. 2007, l. 572); "Available at:" in every entry; volume(issue) given except Latimier and Nückles in a journal for which Agarwal gives the issue (KK-16); Frontiers and Computers and Education: AI entries without issue, uniformly; italics of "Talk, Check, Decide" uniform at l. 26, 160, 266; table cells of Table 6, A1, A2, A3 checked | no grammar error in the running text of Sect. 5 and 6; findings KK-07 to KK-16. Limits: the issue numbers of Latimier et al. (2021) and Nückles et al. (2020) could not be confirmed, because https://api.crossref.org/works/10.1007/s10648-020-09572-8 and https://api.crossref.org/works/10.1007/s10648-020-09541-1 were blocked and the pages fetched instead (link.springer.com, lscp.dec.ens.fr) did not show them |

## Optional checks

| Area | What it needs | Responsible | Run |
|---|---|---|---|
| DOI resolution | one retrieval per reference entry with a DOI | `science-quellenapparat-pruefung` | no |
| Citation style | the name of the style | `science-zitierstil-harvard-ctr` or the style rules of the journal | no |
| AI statement against publisher policy | the policy of the target publisher | this review, on request | no |
| Relation to the authors' own prior work | the prior work of the authors | this review, on request | no |
| Journal requirements | the author guidelines of the target journal | this review, on request | no |
| Subject accuracy | access to the sources of the checked statements and a selection of sections | `science-faktenbeleg-pruefung`, `geo-frage-belegbasiert-klaeren` | no |

## Limits of this review

- Checked version: Listen_Answer_Memorize_Copernicus.pdf, 26 pages, SHA-256 9065d593cbc95029707b6936346f193d31cfedcd4e11382fbbd43629428595aa
- Sources not readable or read only in part: Putnam and Roediger (2013), publisher page blocked, only a secondary summary read; Clinton-Lisell (2022), Litman et al. (2006) and Dunlosky et al. (2013), abstract only; Gandhi and Muldner (2025), conference page only; Bastani et al. (2025), a PDF copy of unclear version; the issue number of Latimier, Peyre and Ramus (2021) could not be confirmed (Crossref blocked); Kortemeyer (2024), Wilson et al. (2007) and Ellis, Adams and Bochner (2011) were not checked against their sources; the repository named in Code and data availability was not opened; the Copernicus data policy cited in GB-42 was read by instance S2 only
- Findings with status assumption: 1 of 42 for the central statement (GB-17); 9 further findings have the status assumption for a partial statement, and these parts are put as questions
- Optional checks run: 0 of 6
- Omitted instances: none; when instances AB and SD ran, the folder of page images was not yet complete, and both rendered the missing pages themselves; at the merge all 26 page images were present
- Discarded findings: 0. All 54 substantive findings, 21 minor corrections and 82 verification log entries of the six instances had their mandatory fields, and no finding was dropped after checking it at the manuscript. Merged: 54 substantive findings into 42, by nine merges of two or three findings each; 21 minor corrections into 16, by two merges of three corrections each and one correction of instance SD taken into a finding (GB-20) after its contradiction was resolved. Four partial statements were struck or corrected because the manuscript does not support them: that the version 6 balance is off by one in every reading (GB-28), that the record shortened a second open question (GB-40), that the tables do not mention the repeated session 1 (GB-25), and the replacement wording that instance SD proposed for l. 306 to 307 (GB-20)
- Hints outside the checklists: 38 hints of the six instances were checked; none became a finding of origin ZF, because each concerned a location that a responsible instance had already treated, duplicated a finding, or was not confirmed as a deficiency at the manuscript; confirmed details of three hints were taken into two existing findings (GB-42, GB-15)
