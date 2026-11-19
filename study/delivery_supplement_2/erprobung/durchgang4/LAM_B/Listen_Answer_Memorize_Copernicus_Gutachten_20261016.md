# Review report: Listen. Answer. Memorize. Building and Running Verified Learning Paths for Geoscience Self-Study with an AI Assistant

| Field | Value |
|---|---|
| Manuscript | Mohr, S. (2026) Listen. Answer. Memorize. Building and Running Verified Learning Paths for Geoscience Self-Study with an AI Assistant; manuscript in Copernicus layout, no DOI or submission identifier on the PDF |
| Checked version | Listen_Answer_Memorize_Copernicus.pdf, 26 pages, SHA-256 9065d593cbc95029707b6936346f193d31cfedcd4e11382fbbd43629428595aa |
| Date | 2026-10-16 |
| Language | English |
| Review instances | Segments 1 to 4, figures, study design; the six review instances ran as separate agents; none dropped |
| Note | According to Sect. 3.7 (l. 273 to 279), all work on the manuscript was done with Claude Opus 5.5; this review was produced with the same language model, so it is a check by the same model family |

## Summary

The manuscript reports a self-experiment, described as a descriptive multiple case study closest to autoethnography, in which a single adult learner, who is also the developer of the learning environment, built and used learning paths for geoscience self-study with an AI assistant (Claude Opus 5.5). The artefact is the skill lernpfad-sitzungen (versions 2.1.0 to 2.6.6). It cuts a fact document in Markdown, supplied by the learner, into sessions of whole paragraphs of up to about 550 words with three questions each, whose expected answers of 5 to 30 words must occur verbatim in the excerpt of the session; a check script verifies anchors, coverage, expected answers, image blocks and exclusions. A session runs in two channels: the text chat prepares it and keeps a learning record, and a voice call reads the excerpt aloud and grades the spoken answers on three grades; incorrect and partially correct answers enter a list To review, from which review sessions are built on request. Five cases (southern Norway, Earth's geological eras, a narrative version of the eras document, the geology of Germany, volcanology) yielded six learning paths in seven check runs, all passed, three only after exclusions. Between 27 September and 13 October 2026, 25 sessions were run on two cases (15 on southern Norway, 10 on the narrative version), 23 of them entirely in the voice call, with 12, 8 and 13 (southern Norway, version 6), 1, 5 and 6 (version 7) and 16, 6 and 8 (narrative version) answers graded correct, partially correct and not correct; two review sessions were completed, and 32 and 13 entries of To review were open on 8 October. Nine stumbling points and the rules they produced are listed in Table 6. Success is judged by the learner's own account on three criteria, and no claim on retention is made.

## Strengths

1. The check script binds each learning path to its fact document by anchors, coverage and verbatim expected answers, and its counts are internally consistent in all seven runs: anchors equal twice the sessions, answers three times the sessions, and the word counts agree between Table 1 and Table 4, with the script change behind the 31-word difference disclosed (PP-25, PP-30, PP-36, PP-45). A reader can therefore verify the one link of the chain that is checked by script, from fact document to learning path; the scope of this check ends at the fact document (GB-26).
2. The manuscript dates the skill versions in Table A2, assigns each group of sessions to a version, marks the inferred assignment of sessions 4 to 11 as such, and ties nine stumbling points to their rules and versions; Table 6, Table A2, the triangles and shading of Fig. 4 and the text agree (PP-24, PP-40, PP-49, PP-60). This lets a reader follow which rule existed when, which is what makes the version-related findings checkable at all (GB-18, GB-28).
3. Session, question and grade counts agree across the Abstract, the text, Table 1, Table 5, Fig. 1 and Fig. 4: the measured bars of Fig. 4 sum to the grades of Table 5, the bars of Fig. 1 to the session counts of Table 1, and the totals 25 = 15 + 10 and 23 + 1 + 1 hold (PP-27, PP-35, PP-38, PP-48). The reported figures can be reproduced from the paper itself, with the exception of the To review balance of version 6 (GB-33).
4. The manuscript declares the grades as process data, makes no claim on retention, draws no comparison between modes, learning paths or skill versions that its design cannot carry, and lists five limitations whose count holds (PP-43, PP-55, PP-61, PP-62). This keeps most claims within what a single-learner self-experiment can show; where a statement goes further, the findings name it (GB-01, GB-44).

## Weaknesses

1. The qualifier "verified" is not supported for the two fact documents behind all 25 sessions: Sect. 4.1 reports no check against the sources for southern Norway and the geological eras and gives no estimate of errors that all checks missed, and the eras paths were cut anew after version 10 without a check run (GB-26, GB-11). Report, for each fact document, which check was run, when and with what result, or a sample check of expected answers against the sources, and otherwise replace "verified" with wording that names what was checked.
2. The answer to the second part of RQ2 claims more than the data show: two of the four named rules have no documented incident, Table 6 omits incidents named in the text, the effect of showing the questions before the call rests on 2 of 7 against 0 of 3 sessions in time order, reading the excerpt verbatim in the call was not measured, and Sect. 3.2 and 3.5 describe version 2.6.6, under which no session ran (GB-35, GB-01, GB-20, GB-18). Report counts instead of causal wording, state a selection rule for Table 6, and give for each rule the first version that contained it and the sessions in which it applied.
3. Several data and procedures cannot be checked or rebuilt: the data availability statement covers two of four kinds of source, one of six learning paths and only skill version 2.6.6, and the script version of each check run, the model and context of the voice call, the procedure of the method analyses and the source of each statement are not given (GB-21, GB-10, GB-24, GB-28, GB-15, GB-17, GB-22, GB-23). Extend the statement source by source, add the script version to Table 4, and describe the voice call and the method analyses in Sect. 3.2 and 3.6.
4. Related work, interpretation and outlook have gaps of moderate weight: the literature search is not described, three close studies and a moderator of Clinton-Lisell (2022) are missing, the gaps are not carried through to the Discussion, the questions on relations are classed as elaborative interrogation against the verbatim design, the claim that the skill works with any fact document that can be checked goes beyond the five conditions of Sect. 3.4, and the proposed retention test confounds review with selection and grading (GB-06, GB-04, GB-05, GB-09, GB-08, GB-07, GB-42, GB-44, GB-43). Describe the search, add the studies, align the classification and the reuse claim with the manuscript's own design, and specify a randomised retest.

## Findings by segment

### Segment 1: Abstract, Introduction, Related work (p. 1 to 4)

#### Substantive findings

**GB-01 The statement that all questions were asked as worded only once they were shown before the call rests on three sessions without comparison and without a stated detection procedure.**

| Field | Content |
|---|---|
| Check | P9, P32 |
| Location | p. 1, l. 18 to 20; p. 19, l. 399 to 401; Table 6, row 6, column Rule or remedy (p. 16); Table 6, rows 7 and 8; Fig. 4 (p. 15), triangles over narrative sessions 6, 7 and 10; Fig. 7 (p. 19), lower annotation |
| Quotation | "in the narrative version, for example, all questions were asked as worded only once they were shown in the text chat before each call"; "only after the excerpt and the questions were shown in the text chat before each call were all questions asked as worded" |
| Concern | The manuscript documents deviations openly in Table 6, which is valuable. The causal reading ("only once") is not supported by the design. (1) Comparison: deviations occurred in 2 of 7 narrative sessions before the change (sessions 6 and 7, Fig. 4) and in 0 of 3 after it, with 9 questions after the change. With a deviation rate of 2/7 per session, three sessions without deviation have a probability of (5/7)^3 = 0.36; Fisher's exact test on 2/7 vs 0/3 gives p = 1.0. (2) Confounding: the change coincides with session order; sessions 8 to 10 are the last three, and the two deviating sessions are the two sessions directly before the change. (3) Detection: how a deviation was found (comparison of the call transcript with the learning path for every question, or only noticed incidents) is not described. Without it, the counts in Table 6 rows 6 to 8 are a lower bound (at least 4 of 25 sessions with a deviating question, 16 %), and the statement that all questions were asked as worded is a claim of zero errors without an independent check. (4) In session 10, after the change, a content hint was still given (Table 6 row 8; Fig. 7), so the rule of 2.5.0 that questions are asked "without hints" did not hold there. Severity major: the statement is the Abstract's example of the effect of a rule and part of the RQ2 answer (l. 399 to 401); if the finding holds, the manuscript can show that the rule arose, not that it worked. |
| Suggestion | In the Abstract and in Sect. 5 (l. 399 to 401) report the counts (2 of 7 sessions before, 0 of 3 after) and drop "only once" and "only after", or support them by a design that can: compare, for every one of the 25 sessions, each question asked in the call with the learning path (if the call text is kept) and report the deviation rate per condition; for future sessions, alternate showing and not showing the questions before the call in a fixed or random order, so that the condition is not confounded with time. State in Sect. 3.6 how deviations in Table 6 were detected. |
| Status | verified (counts, location of deviations); inferred (probability and test, from manuscript counts); assumption (whether call text is kept) |
| Severity | major |
| Source | SD |

**GB-02 In the Graphical Abstract one of three line styles is not explained: what does the dotted arrow from "Learning path" down to "AI assistant rules" mean?**

| Field | Content |
|---|---|
| Check | P29 |
| Location | Graphical Abstract, p. 2, dotted arrow between the boxes "Learning path script-checked" and "AI assistant rules" |
| Quotation | "on request"; "incidents led to new rules" |
| Concern | The Graphical Abstract has no caption, so it must be read from its labels. It uses solid, dashed and dotted arrows. The dashed arrow is labelled "on request" and the long dotted line "incidents led to new rules". The short dotted arrow pointing from "Learning path" to "AI assistant rules" carries no label; it may stand for incidents in building learning paths (Table 6, nos. 3, 4, 9), but the figure does not say so, and the solid arrow in the opposite direction makes the pair hard to read. |
| Suggestion | Label the short dotted arrow in the Graphical Abstract, for example "incidents in building", or join it to the label "incidents led to new rules". |
| Status | verified (line styles at the page image); assumption (intended meaning) |
| Severity | minor |
| Source | AB |

**GB-03 The binding of every session to the fact document does not hold in the explanation mode of reviews and for the map booklet, and Sect. 3.5.3 does not say so.**

| Field | Content |
|---|---|
| Check | P26, P17 |
| Location | p. 2, l. 32; p. 11, l. 224 to 227; p. 20, l. 432 to 433; p. 21, l. 448 to 449; p. 10, l. 202 to 203; p. 20, l. 426 to 428 |
| Quotation | "The learning environment studied here therefore binds every session to a fact document that the learner supplies"; "An explanation mode in which general knowledge is allowed was later introduced for review sessions at the learner's request."; "for the narrative version a separate booklet of 15 maps served to show the cited maps and to answer follow-up questions" |
| Concern | The guarantee is stated for every session. It is suspended in at least two paths: the review mode "explain", where general knowledge is allowed (disclosed only in the Discussion, l. 432 and l. 449), and follow-up questions on the narrative version answered with the map booklet, which is not part of the fact document and not covered by the check script. Sect. 3.5.3, where the review modes are introduced, does not say that the explanation mode leaves the fact document, and it is not stated whether the introduction and summary in the default mode "both" may use general knowledge. This also stands against the open-question rule (l. 426 to 428). |
| Suggestion | In Sect. 3.5.3, l. 226 to 227, state for each review mode whether content outside the fact document may be used; in Sect. 3.5.1, l. 202 to 203, state whether the booklet was checked against its sources and how follow-up questions on it were answered; qualify l. 32 to "every learning session". |
| Status | verified |
| Severity | moderate |
| Source | SD |

**GB-04 Ruan et al. (2019), a dialogue-based quizzing system for factual knowledge that grades free-text answers and schedules reviews, is missing from Sect. 2.**

| Field | Content |
|---|---|
| Check | P14 |
| Location | p. 3, l. 52 to 61 (retrieval practice and spacing); p. 4, l. 97 to 108 (gap statement, respects relating to RQ2 and RQ3) |
| Quotation | "none of the studies reviewed here, however, combines listening alone with spoken answers in self-study, as the voice sessions studied here do" |
| Concern | Ruan, S., Jiang, L., Xu, J., Tham, B.J.-K., Qiu, Z., Zhu, Y., Murnane, E.L., Brunskill, E. and Landay, J.A. (2019) 'QuizBot: a dialogue-based adaptive learning system for factual knowledge', in Proceedings of the 2019 CHI Conference on Human Factors in Computing Systems (CHI 2019). New York: ACM. Available at: https://doi.org/10.1145/3290605.3300587. The system asks factual questions in a conversation, grades the learner's free-text answer by similarity to the correct answer (threshold 0.9), schedules reviews with a memory model, and was compared against a flashcard app; the abstract reports that students recognised and recalled over 20% more correct answers with QuizBot (study 1: recall 66.3% against 45.2%). It is the closest predecessor of the "Answer" and "Memorize" parts: conversational retrieval practice of facts with tolerant grading of free answers and a record that drives review. It is not in the reference list (Pflichtabgleich against p. 24, l. 509 to p. 26, l. 575). It differs in that answers are typed, the content is not bound to a learner's own fact document, and reviews are scheduled rather than on request, which the manuscript could use to sharpen its own contribution. |
| Suggestion | Cite Ruan et al. (2019) in Sect. 2 after the paragraph on retrieval and spacing (p. 3, l. 61) and state in the gap statement (p. 4, l. 101 to 104) how the voice sessions and the on-request review differ from conversational quizzing with scheduled review. |
| Status | verified (contents read in the full text at https://cs.stanford.edu/~ebrun/papers/QuizBot.pdf; absence from the reference list checked) |
| Severity | moderate |
| Source | S1 |

**GB-05 Schmucker et al. (2024), an LLM tutor whose questions and expected answers are generated from a supplied lesson text and which did not outperform reading, is missing from Sect. 2.**

| Field | Content |
|---|---|
| Check | P14 |
| Location | p. 3, l. 62 to 72 (AI tutors and supplied material); p. 4, l. 97 to 99 (gap statement, first respect) |
| Quotation | "First, the AI tutors in the studies rely on solutions supplied by teachers or researchers, whereas here the learner supplies a fact document of his own" |
| Concern | Schmucker, R., Xia, M., Azaria, A. and Mitchell, T. (2024) 'Ruffle&Riley: insights from designing and evaluating a large language model-based conversational tutoring system', arXiv [Preprint], arXiv:2404.17460. Available at: https://arxiv.org/abs/2404.17460. The system induces an editable tutoring script "automatically from a lesson text": review questions are generated first, then for each question "a solution is generated based on question and lesson texts", and expectations are derived from it. In two online evaluations (100 participants recruited each, 58 and 72 retained) against reading the 640-word lesson text, no significant differences in post-test scores were found, while the tutor took about 20.8 minutes against 5.5 minutes for reading (ratio 20.8 / 5.5 = 3.78). The work anticipates the first respect in part: a tutor whose questions and answers are derived from a supplied text rather than from teacher-written solutions or the model's own knowledge. Its null result against reading is the nearest evidence on what a text-bound conversational tutor adds over reading the same text. It is not in the reference list. |
| Suggestion | Cite Schmucker et al. (2024) in Sect. 2 after l. 72 as a tutor bound to a supplied lesson text, and narrow the first respect (p. 4, l. 97 to 99) to what remains specific here: the learner's own checked fact document and the script check that every expected answer occurs verbatim in the excerpt. |
| Status | verified (abstract and evaluation section read at https://arxiv.org/abs/2404.17460 and https://arxiv.org/html/2404.17460v1; absence from the reference list checked); a later peer-reviewed venue could not be confirmed from the pages read |
| Severity | moderate |
| Source | S1 |

**GB-06 The gap argument rests on "none of the studies reviewed here" without any account of how the reviewed studies were found.**

| Field | Content |
|---|---|
| Check | P28 |
| Location | p. 4, l. 97 to 108 (five respects); p. 14, l. 319 to 320; p. 12, l. 276 (Sect. 3.7) |
| Quotation | "Taken together, this work leaves a gap that the present paper addresses, in five respects."; "none of the studies reviewed here examines a narrative version built from the same verified fact document, without losing or adding a fact, as a second way into the same material"; "none of the studies reviewed here, however, combines listening alone with spoken answers in self-study, as the voice sessions studied here do"; "Since none of the studies reviewed in Sect. 2 combines listening alone with spoken answers in self-study, these requests cannot be set against them" |
| Concern | The hedge "reviewed here" is careful, but it makes the gap depend entirely on what was reviewed, and the manuscript says nowhere how the literature was searched: Sect. 2 names no databases, search terms, period or search date, and Sect. 3.7 says only that Claude "searched and checked the literature" (p. 12, l. 276). The Results then use the gap as a reason not to relate the learner's requests to any prior work (p. 14, l. 319 to 320). Three own searches show that the neighbouring work is not empty: dialogue-based quizzing of factual knowledge with graded free-text answers and scheduled review (Ruan et al., 2019; GB-04), an LLM tutor whose questions and expected answers are generated from a supplied lesson text (Schmucker et al., 2024; GB-05), an autoethnography of a single adult learning with an LLM tutor (Gandhi and Muldner, 2025; GB-09), and a voice-assistant quiz in which questions are spoken and answered by voice (Todericiu et al., 2024, CSEDU 2024, pp. 589 to 596, https://doi.org/10.5220/0012722400003693; multiple-choice answers given as option letters, preliminary survey of six participants, no excerpt listening). None of these combines all elements of the present design, so the narrow gap may well hold, but a reader cannot tell whether it holds because such work does not exist or because it was not searched for. |
| Suggestion | At the start of Sect. 2 (p. 3, l. 52) or in Sect. 3.7 (p. 12, l. 276), state the databases or search engines used, the search terms, the period covered and the date of the search; then either cite the neighbouring work in Sect. 2 and narrow the five respects accordingly, or rephrase "leaves a gap" (l. 97) as "the studies reviewed here do not address". |
| Status | verified (absence of a search description in Sect. 2 and 3.7 checked in the full text); inferred (that the neighbouring work bears on the gap, from the abstracts and full texts read for GB-04, GB-05 and GB-09) |
| Severity | moderate |
| Source | S1 |

**GB-07 The chain from the five gaps to the Discussion is incomplete: gap 5 has no research question, gaps 3 and 4 and the retrieval-augmented approach are not taken up again, and the Conclusions take up no core term of RQ2 or RQ3.**

| Field | Content |
|---|---|
| Check | P10, P15 |
| Location | p. 4, l. 101 to 108; p. 3, l. 43 to 48; p. 3, l. 69 to 72; p. 4, l. 83 to 90; p. 18, l. 381 to p. 21, l. 465; p. 22, l. 467 to 482 |
| Quotation | "Fifth, the studies concern school classes, courses and samples of many learners; this paper describes the self-study of a single adult learner in the geosciences, who is also the developer of the learning environment."; "The first two respects correspond to RQ1, the third to RQ2 and the fourth to RQ3." |
| Concern | The manuscript maps four of its five gaps to research questions, which makes the chain easy to follow. Gap 5 maps to none, yet the Discussion builds a result on it (the learner "regulated not only his learning but also the tool he learned with", l. 449 to 450, Fig. 8), and the Conclusions repeat it (l. 469 to 470), so this result answers no stated question. Gap 3, listening alone combined with spoken answers (Clinton-Lisell, 2022; Putnam and Roediger, 2013), returns only in Sect. 4.3 (l. 319 to 320), not in the Discussion. Gap 4 rests on the journal studies, in which the learner's own writing is the learning activity ("written text relieves the learner as an external representation and memory aid", l. 85); the design hands the writing to the assistant, but the RQ3 paragraph (l. 391 to 393) does not say what follows from this against Nückles et al. (2020) and Zhang et al. (2022). Retrieval-augmented generation (Li et al., 2025) is introduced as the third approach in which accuracy rests on supplied material (l. 69 to 72), but the comparison in l. 394 to 396 and Fig. 7 covers only the tutoring studies. The Conclusions take up the success criteria of Sect. 3.6 but neither the rules from incidents (RQ2) nor how the record tracks what is not yet mastered (RQ3). The Discussion answers all three research questions (l. 381 to 393), so no result changes; severity moderate rather than minor because a reader cannot trace two of the five stated gaps to an answer and one result to a question. |
| Suggestion | In Sect. 1, either add a research question for gap 5 (for example how the learner, as developer, changed the tool during use, answered by Table 6, Table A2 and Fig. 8) or state after l. 108 that gap 5 describes the setting and is not a question. In Sect. 5, add one paragraph each on gap 3 (what the requests for re-reading in Sect. 4.3 mean against the listening literature) and on gap 4 (what is lost or gained when the assistant, not the learner, writes the record), and set the verbatim principle against retrieval-augmented generation in l. 394 to 396. In Sect. 6, add one sentence each on RQ2 and RQ3. |
| Status | verified |
| Severity | moderate |
| Source | S4, SD |

**GB-08 The related work reports only the null overall result of Clinton-Lisell (2022) and omits the moderator that favours self-paced reading over listening, which is the comparison this study's design faces.**

| Field | Content |
|---|---|
| Check | P13 |
| Location | p. 4, l. 101 to 102 (gap statement, third respect); taken up again p. 14, l. 319 to 320 |
| Quotation | "listening alone has been compared with reading in many studies, with no reliable overall difference in comprehension (Clinton-Lisell, 2022)" |
| Concern | The overall figure is reproduced correctly: the abstract of Clinton-Lisell (2022) reports, from 46 studies (N = 4,687), that "the overall difference between reading and listening comprehension was not reliably different (g = 0.07, p = .23)". The same abstract continues that "Reading was beneficial over listening when the reading condition was self-paced (g = 0.13, p = .049)", and that the reading advantage held when inferential and general rather than literal comprehension was assessed. Both moderators bear directly on this study: the learner could study each learning path either on screen, at his own pace, or by listening to the excerpt read aloud (p. 6, l. 131: "From the start, the learner wanted to work through a learning path either on screen or interactively by voice"), and the voice sessions replace self-paced reading with listening. Reported without the moderator, the sentence suggests that listening costs nothing against reading; the source says that it costs a small but reliable amount against self-paced reading. The manuscript reports the moderators of the companion meta-analysis on reading while listening (Clinton-Lisell, 2023, p. 3, l. 73 to p. 4, l. 76) in full, so the omission is specific to the 2022 study. The effect is small (g = 0.13), and the manuscript draws no comparison of modes (p. 14, l. 323: "the modes therefore allow no comparison, and none is drawn"), so no result changes. Severity moderate rather than minor because the sentence is part of the gap argument for RQ2 and a reader cannot judge the trade-off of the voice-only design without the moderator. |
| Suggestion | In Sect. 2, p. 4, l. 101 to 102, add the moderator, for example: "with no reliable overall difference in comprehension, although reading had a small advantage when it was self-paced (g = 0.13) and when inferential comprehension was assessed (Clinton-Lisell, 2022)"; and in Sect. 5, where the voice mode is discussed, state that listening trades a small comprehension advantage of self-paced reading for availability on the move. |
| Status | verified (wording in the manuscript at the printed line numbers; moderator values in the abstract of Clinton-Lisell, 2022, read via the publisher page https://journals.sagepub.com/doi/10.3102/00346543211060871) |
| Severity | moderate |
| Source | S1 |

**GB-09 Gandhi and Muldner (2025), an autoethnography of a single adult learning with an LLM tutor in sessions, is missing and bears on the fifth respect and on the method.**

| Field | Content |
|---|---|
| Check | P14 |
| Location | p. 4, l. 106 to 107 (gap statement, fifth respect); method framing p. 11, l. 250 to p. 12, l. 252 |
| Quotation | "Fifth, the studies concern school classes, courses and samples of many learners; this paper describes the self-study of a single adult learner in the geosciences, who is also the developer of the learning environment." |
| Concern | Gandhi, A. and Muldner, K. (2025) '"That's not the way I would explain it": a teacher-researcher's autoethnography of learning to program with ChatGPT', in Proceedings of the 21st ACM Conference on International Computing Education Research (ICER 2025), Charlottesville, VA. Available at: https://icer2025.acm.org/details/icer-2025-papers/27/-That-s-Not-the-Way-I-Would-Explain-It-A-Teacher-Researcher-s-Autoethnography-of-Le. An experienced educator and novice programmer worked through course materials with ChatGPT-4o over five learning sessions, as both learner and evaluator, and reports that ChatGPT "lacked the ability to autonomously assess my understanding", so that she "had to rely on self-monitoring". The study is a single adult learner, self-study with an LLM tutor, autoethnographic method, and a learner who also shapes the use of the tool: it weakens the fifth respect as stated, and its finding on assessment is the counterpart of this manuscript's AI-kept learning record and grading (RQ3). It is not in the reference list. |
| Suggestion | Cite Gandhi and Muldner (2025) in Sect. 2 and in the method framing at p. 11, l. 251, and rephrase the fifth respect (p. 4, l. 106 to 107) so that it names what differs: the learner as developer of the tool and the assistant keeping the learning record. |
| Status | verified (abstract read on the conference page; absence from the reference list checked); DOI not shown on the page read |
| Severity | moderate |
| Source | S1 |

#### Minor corrections

| ID | Location | Quotation | Replacement | Source |
|---|---|---|---|---|
| KK-01 | Graphical Abstract, p. 2, box Review | "missed questions" | "questions not answered fully correctly" (the list To review also holds partially correct answers, p. 11, l. 221) | AB |

#### Verification log

| ID | Check | Checked | Values | Result |
|---|---|---|---|---|
| PP-01 | P13 | Dunlosky et al. (2013), p. 3, l. 52 to 55 and 60 to 61 | ten techniques; practice testing and distributed practice high utility, benefit "learners of different ages and abilities"; rereading low; elaborative interrogation moderate because "not been adequately evaluated in educational contexts"; abstract recommends other techniques such as practice testing instead of rereading (publisher abstract) | no finding |
| PP-02 | P13 | Agarwal, Nunes and Blunt (2021), p. 3, l. 55 to 57 | 50 experiments, 49 effect sizes, n = 5374; "the majority of which (57%) revealed medium or large benefits"; "only 6% of experiments were conducted in non-WEIRD countries" (publisher abstract) | no finding |
| PP-03 | P13 | Latimier, Peyre and Ramus (2021), p. 3, l. 57 to 60 | 29 studies; spaced vs massed retrieval g = 0.74; expanding vs uniform no significant difference, g = 0.034 (publisher abstract) | no finding |
| PP-04 | P13 | Ji et al. (2023), p. 2, l. 30 to 31; p. 3, l. 62 to 64 | intrinsic: "output that contradicts the source content"; extrinsic: "output that can neither be supported nor contradicted by the source" (arXiv full text 2202.03629, Sect. 2.1) | no finding |
| PP-05 | P13 | Bastani et al. (2025), p. 3, l. 64 to 67 | "nearly a thousand" students; "17% reduction in grades for GPT Base" once access was removed; harm "largely mitigated by the safeguards included in GPT Tutor" (abstract via RePEc, SSRN, Stanford SCALE). The figure "only 51% of the time" could not be checked: the PNAS full text was not reachable and none of the abstracts read contains it. The abstract also reports 48% (GPT Base) and 127% (GPT Tutor) better grades while access was available; omitting them does not change the cited statement | no finding; 51% unverified (Limits of this review) |
| PP-06 | P13 | Kestin et al. (2025), p. 3, l. 67 to 69 | "we enriched our prompts with comprehensive, step-by-step answers"; "we avoided relying solely on GPT-4"; "students learn significantly more in less time when using the AI tutor, compared with the in-class active learning" (PMC12179260) | no finding |
| PP-07 | P13 | Li et al. (2025), p. 3, l. 69 to 71 | RAG retrieves "relevant information from an external knowledge base"; hallucination named as a challenge and "mitigating hallucinations" listed among future directions (abstract, Lingnan University repository) | no finding |
| PP-08 | P13 | Clinton-Lisell (2023), p. 3, l. 73 to p. 4, l. 76 | 30 studies, N = 1945, 62 effect sizes; overall g = .18 called "trivial"; experimenter-paced g = 0.41; self-paced g = 0.06, p = .34 (ERIC full text EJ1403866) | no finding |
| PP-09 | P13 | Terzopoulos and Satratzemi (2020), p. 4, l. 76 to 78 | "have just started to be used in schools and universities" (abstract); "still at an early stage of research", "results are limited, incomplete and unorganized", "the lack of many languages" (Conclusion, full text PDF) | no finding |
| PP-10 | P13 | Denojean-Mairet et al. (2024), p. 4, l. 79 to 81 | review cites 30 s to 5 min (Jahnke et al.) and "less than 10 min" (Torgerson and Iannone); also cites up to 15 min (Díaz Redondo et al.; Garcia et al.) and notes no consensus. The 15 min definitions are left out; the cut does not change the statement in l. 79 to 81 | no finding; the use of these definitions in l. 418 is GB-40 |
| PP-11 | P13 | Traxler (2007), p. 4, l. 81 to 82 | "learning whilst traveling, driving, sitting, or walking"; "exploit small amounts of time and space for learning" (IRRODL full text) | no finding |
| PP-12 | P13 | Panadero (2017), Nückles et al. (2020), Zhang et al. (2022), p. 4, l. 83 to 88 | SRL "a core conceptual framework to understand the cognitive, motivational, and emotional" aspects; written text as "an external representation and memory aid", journal writing "needs to be instructionally supported"; 38 Chinese EFL students, journaling "raised students' awareness" and "may have contributed" to strategy use (hedge "suggest" for awareness dropped; statement unchanged) | no finding |
| PP-13 | P13 | Achuthan (2025), p. 4, l. 88 to 90 | 32 studies, 92 effect sizes; SRL g = 1.613 (11 studies); SDL g = 1.111 (8 studies); cognitive/metacognitive g = 0.377, "moderate" in the abstract, "small-to-moderate" in the results; forethought g = 0.4739, p = 0.0009, called most effective; performance phase g = 0.78 not significant (p = 0.0782) | no finding |
| PP-14 | P13 | Mar et al. (2021), Dahlstrom (2014), p. 4, l. 91 to 96 | "over 75 unique samples", "more than 33,000 participants", "stories were more easily understood and better recalled than essays", "robust", "not moderated by various study characteristics" (PMC8219577); narrative structure "describes the cause-and-effect relationships between events", "Narratives offer increased comprehension, interest, and engagement", "intrinsically persuasive", "raises ethical considerations" (full text PDF) | no finding |
| PP-15 | P13 | Cheek, LaDue and Shipley (2017), Landy, Silbert and Goldin (2013), p. 2, l. 36 to 38 | Cheek et al.: estimates "can be off by several orders of magnitude" (citing Trend, Catley and Novick, Delgado); Landy et al.: "about half of people did estimate numbers linearly", "nearly all the remaining participants placed 1 million approximately halfway between 1 thousand and 1 billion"; share at most 1 - 0.5 = 0.5, so "many adults" holds | no finding |
| PP-16 | P13 | Putnam and Roediger (2013), p. 4, l. 102 to 103 | publisher page, PubMed and two secondary pages tried; abstract not readable | not checked (Limits of this review) |
| PP-17 | P14 | Contribution in one sentence: a single adult learner builds with an LLM assistant learning paths whose expected answers are script-checked to occur verbatim in his own checked fact documents, runs them as voice-call sessions with an AI-kept learning record, and reports this as a self-experiment. Searches (5 of 6 allowed): (1) "LLM generated quiz questions grounded in source document answer verification extractive answers educational question generation evaluation 2024"; (2) "voice-based LLM tutor spoken answers retrieval practice study conversational agent quiz learners evaluation"; (3) "autoethnography self-study learning with large language model ChatGPT personal learning tutor single learner"; (4) "LLM tutor grounded in instructor-provided source material hallucination verbatim answers voice mode study 2025"; plus (5) the P28 search below | candidates: Ruan et al. 2019 (QuizBot), Schmucker et al. 2024 (Ruffle&Riley), Gandhi and Muldner 2025, Breuer and Meyer 2024 (bachelor thesis on grounded question generation, arXiv 2506.12066), Todericiu et al. 2024. Pflichtabgleich against p. 24, l. 509 to p. 26, l. 575: none is in the reference list. Proposed: three (GB-04, GB-05 and GB-09); Breuer and Meyer not proposed (thesis, same field only); Todericiu et al. used under P28 | three findings |
| PP-18 | P28 | Lack claims: p. 4, l. 97, 100, 103 to 104; p. 14, l. 319 to 320. Search description sought in Sect. 2 and 3.7. One own search: "voice assistant Alexa quiz spoken answers retrieval practice learning study audio-only" (plus searches 1 to 3 above) | no databases, terms, period or date given; p. 12, l. 276 says only "searched and checked the literature". Voice quiz with spoken answers exists (Todericiu et al., 2024, multiple choice, N = 6 survey); no study found that combines listening to a source excerpt with spoken free answers in self-study, so the narrow gap is not refuted | one finding (GB-06) |
| PP-19 | P29, P3 (7) | Inventory of figures | Graphical Abstract, p. 2, schema, raster 1328 x 531 px at 194 ppi, no caption, not referenced (none expected). Fig. 1, p. 6, schema with bars, JPEG 1365 x 633 px, caption l. 121 to 124, cited l. 112 (Sect. 3.1). Fig. 2, p. 7, flow schema, caption l. 151 to 155, cited l. 141 (3.2). Fig. 3, p. 9, schema declared schematic, caption l. 185 to 188, cited l. 173, 182 (3.4), 302 (4.2). Fig. 4, p. 15, stacked bar chart with date axis, caption l. 331 to 334, cited l. 322 (4.4). Fig. 5, p. 17, timeline, caption l. 359 to 363, cited l. 354 (4.7). Fig. 6, p. 18, three-column schema, caption l. 377 to 379, cited l. 365 (4.8). Fig. 7, p. 19, chain schema, caption l. 406 to 411, cited l. 387, 394, 402 to 403, 425 (5). Fig. 8, p. 21, loop schema, caption l. 456 to 461, cited l. 450 (5). All figures raster, 200 ppi. | no finding: numbering 1 to 8 consecutive in order of first citation (l. 112, 141, 173, 322, 354, 365, 387, 450); every figure cited in its own section |
| PP-20 | P10 | RQ1 and RQ2 first part against design | descriptive "how" questions, answered by case descriptions, Table 4, Sect. 3.2; no comparison needed for descriptive questions; Sect. 1, l. 49 to 50, limits "Memorize" to the record | no finding except GB-07 and GB-35 |

### Segment 2: Materials, methods, appendix (p. 5 to 12, 22 to 24)

#### Substantive findings

**GB-10 Of the five fact documents and six learning paths checked in Table 4, the data availability statement covers one fact document and one learning path; the others are not mentioned.**

| Field | Content |
|---|---|
| Check | P12 |
| Location | p. 5, l. 113 and Table 1 (column Learning path); p. 14, Table 4 (l. 310 to 314, column Learning path); p. 7, l. 157 to 158; p. 8, l. 166 to 167; p. 10, l. 202 to 203; p. 24, l. 496 to 498 |
| Quotation | "Each case has a fact document and a learning path that passed the check script"; "an example pair: a fact document in German on the geology of southern Norway and its learning path in version 5 with 30 sessions, which can be reused under the same licence." |
| Concern | The example pair is published under a licence, which makes one complete pair reusable. Table 4 lists seven check runs of six learning paths (l. 301). The statement covers the path of southern Norway in version 5, which Table 4 and l. 301 to 302 identify with version 6, but says nothing about the paths southern Norway version 7, Geological eras version 7, narrative version 8, Geology of Germany version 1 and Volcanology version 4, or about the fact documents on the geological eras, the narrative version, the geology of Germany and volcanology. Count: 1 of 6 learning paths and 1 of 5 fact documents addressed. These materials concern no person; the fact document on Germany "was based on open-access sources" and the one on volcanology "was taken word for word from openly licensed textbooks" (l. 166 to 167), so the statement gives no reason for withholding them. Also not mentioned: the version of the published example fact document, which version of the fact document on southern Norway the paths 5 to 7 belong to, the two paths of 15 and 14 sessions cut after version 10 of the fact document on the geological eras (Table 1 caption, l. 117 to 119), the workplans, decision logs and change records of the document projects (l. 157 to 158), and the "separate booklet of 15 maps" (l. 203). Third-party rights may explain some of this (textbook text, maps); the statement should then say so. |
| Suggestion | In Code and data availability (p. 24, l. 494 to 500), state for each fact document and learning path in Table 4 whether it is published, where, or why not (for example licence of third-party material); give the version of the published example fact document; and add that the example pair's version 5 is the learning path used as version 6 in sessions 1 to 11 (Table 4). |
| Status | verified (absence in the statement, Table 1 and Table 4 at the page images p. 5, p. 14, p. 24); inferred (that the materials concern no person, from l. 166 to 167 and Sect. 3.3) |
| Severity | moderate |
| Source | S2 |

**GB-11 After version 10 of the fact document on the geological eras, both of its learning paths were cut anew without a documented check run; this stands only in the caption of Table 1, and the dates are not given.**

| Field | Content |
|---|---|
| Check | P2, P30, P17 |
| Location | p. 5, Table 1 caption, l. 117 to 119; p. 5, l. 113; p. 6, Fig. 1 caption, l. 121 to 122; p. 7, l. 159; p. 8, l. 168 to 170; p. 13, l. 297 to 298 and l. 306; p. 1, l. 14 to 15 |
| Quotation | "after version 10 of the fact document on the geological eras, both of its learning paths were cut anew, into 15 and 14 sessions, without a documented full check run"; "Each case has a fact document and a learning path that passed the check script"; "All six paths passed." |
| Concern | The caption discloses the recut, Table 1 defines its column as "the latest version with a documented check run", and the reported sessions (Table 5) ran on the checked version 8, so the results stand. The manuscript requires a fact document that "has been checked against its sources before a learning path is built" (l. 168 to 169) and a skill that "presupposes a finished fact document and never changes it" (l. 159). For the eras case, the fact document reached version 10 after the checked paths existed (the narrative path was checked on 5 October, l. 297 to 298), and the current paths of 15 and 14 sessions have no reported check. The statements in l. 113, in the Fig. 1 caption and in the Abstract (l. 14 to 15) therefore hold only for the earlier versions, and Sect. 3.4, Sect. 4.2 and Table 4 do not mention the recut. When version 10 arose relative to the narrative sessions (5 to 7 October) is not given, so it is open whether any session ran after the fact document had changed and whether the version-mismatch report of the learning record (l. 227 to 228) applied. Severity moderate, the higher of the two merged grades: the disclosure stands only in a table caption, and a reader cannot tell whether the current paths still meet the check. |
| Suggestion | In Sect. 4.1 or 4.2, give the dates of version 10 and of the recut paths and state whether any session ran after the fact document changed; either run the check script on the two recut paths and add the runs to Table 4, or mark them in Table 4 as not checked and write in l. 113 and in the Fig. 1 caption "a learning path whose latest checked version passed the check script". |
| Status | verified (recut after the check, place of disclosure); assumption (timing relative to the sessions, put as a question) |
| Severity | moderate |
| Source | S3, SD |

**GB-12 The learning paths on the geology of Germany and on volcanology carry their version in Table 1 and Fig. 1 but not in Table 4, and the second number of the Germany path is not explained.**

| Field | Content |
|---|---|
| Check | P38 |
| Location | p. 5, Table 1, row Geology of Germany, column Learning path; p. 6, Fig. 1, row Geology of Germany, column Learning path; p. 14, Table 4, rows Geology of Germany and Volcanology, stage 1, column Learning path |
| Quotation | "version 1 (file name: version 6)"; "version 1: passed after exclusions"; "Geology of Germany"; "Volcanology, stage 1" |
| Concern | Table 1 names both numbers, so the double name is disclosed, but it does not say what the number 6 in the file name counts (earlier cuts, the fact document version, or a numbering shared with another path), so a reader holding the files cannot tell which one is meant. Table 4 gives a version in five of its seven rows but none in this row nor in the row "Volcanology, stage 1", although Table 1 and Fig. 1 give version 4, so these two runs in Table 4 cannot be tied to the versions in Table 1 by name. Confirmed at the page images p. 5, p. 6 and p. 14. |
| Suggestion | In the Table 1 caption (p. 5, l. 115 to 119), explain why file name and version differ; in Table 4 (p. 14), name the rows "Geology of Germany, version 1" and "Volcanology, stage 1, version 4". |
| Status | verified |
| Severity | minor |
| Source | S2 |

**GB-13 The volcanology case is called "Volcanology, stage 1" in Table 1, Table 4 and Fig. 1, but "Volcanology" in Table 6 and "volcanology" in the text, and "stage 1" is not explained.**

| Field | Content |
|---|---|
| Check | P38 |
| Location | p. 5, Table 1, row 5, column Case; p. 6, Fig. 1, row 5, column Case; p. 14, Table 4, row 7, column Learning path; p. 16, Table 6, row 9, column Case; text p. 1, l. 14; p. 5, l. 112 to 113; p. 8, l. 167; p. 13, l. 284 and 299 |
| Quotation | "Volcanology, stage 1"; "Volcanology"; "the fact document on volcanology is in English" |
| Concern | The word "stage" occurs only in the two table rows (Table 1 and Table 4, confirmed at the page images p. 5 and p. 14) and in Fig. 1, apart from an unrelated use in l. 77. The qualifier suggests that the case covers only part of a larger fact document, but the text never says so, and it is unclear whether "the fact document on volcanology" (l. 113, l. 284) and the 19,519 words in Table 1 refer to stage 1 or to the whole document. Same object, two names, no explanation. |
| Suggestion | Explain "stage 1" where the case is introduced (Sect. 3.1, p. 5, l. 111 to 114, or Sect. 3.3, p. 8, l. 167), and use one name in Table 1, Table 4, Table 6 and Fig. 1. |
| Status | verified |
| Severity | minor |
| Source | S2 |

**GB-14 Fig. 1 labels the narrative version as an own document project, while the text says it was written within the project on the geological eras.**

| Field | Content |
|---|---|
| Check | P3 |
| Location | Fig. 1, row "Geological eras, narrative version", column "Fact document", p. 6; caption p. 6, l. 121; compare p. 7, l. 157 to 159, p. 18, l. 381 to 383, and Fig. 5, row "Building fact documents and learning paths", p. 17 |
| Quotation | "own document project (German)"; "Each fact document was built in a document project of its own"; "Each of the four source fact documents was built in a document project of its own before any learning path existed, with a workplan, a decision log and a record of all changes, and the narrative version was written within the project on the geological eras (Sect. 4.6)" |
| Concern | Fig. 1 gives all five rows the same box "own document project", and the caption extends this to "Each fact document". The text restricts it to the four source fact documents and places the narrative version inside the project on the geological eras; Fig. 5 agrees with the text, with one bar "geological eras and narrative version" (measured 2 October + 0.06 d to 5 October + 0.93 d). Fig. 1 thus contradicts the methods text and Fig. 5 on how the fifth case arose. The overview figure is otherwise correct against Table 1 and Table 4 (PP-27). |
| Suggestion | In Fig. 1, row "Geological eras, narrative version", replace "own document project (German)" with, for example, "within the project on the geological eras (German)", and in the caption, l. 121, write "Each of the four source fact documents was built in a document project of its own". |
| Status | verified (figure label and caption at the page image; text at l. 157 to 159) |
| Severity | minor |
| Source | AB |

**GB-15 For the voice call, model, setting, speech recognition, speech output and app version are not given.**

| Field | Content |
|---|---|
| Check | P35 |
| Location | p. 6, l. 126 to 127; p. 6, l. 138 to 139; Table 6, row 8, column Trigger; p. 11, l. 245; p. 20, l. 422 to 424 |
| Quotation | "The assistant was Claude (Anthropic), model Claude Opus 5.5 at the effort setting medium."; "the voice gave a hint on question 4.3" |
| Concern | The manuscript names model and effort setting, which many studies omit. The voice call, however, has capabilities different from the text chat (l. 138 to 139: it can neither update the record nor read the excerpt from its file), and Table 6 refers to "the voice" as the agent that gave a hint. Whether the call ran with the same model and effort setting is therefore a question for the authors, as are the speech recognition and speech output in use and the app version; the grades and deviations of the call depend on them. The model of the "separate agent of the same model family" that checked the method analyses (l. 245) is also not named. |
| Suggestion | In Sect. 3.2 state the model and setting used in the voice call (or that they could not be determined), the app version and date range, and the speech recognition and output; in Sect. 3.6 name the model of the checking agent. |
| Status | verified (not given); assumption (whether the call model differs) |
| Severity | moderate |
| Source | SD |

**GB-16 The count of short inputs is given for one chat without saying which chat or why that one.**

| Field | Content |
|---|---|
| Check | P34 |
| Location | p. 6, l. 133 to 134 |
| Quotation | "in the chats in which learning paths were built, he steered mainly with short instructions, in one of them with 22 of 41 inputs of three words or fewer" |
| Concern | The general statement "mainly with short instructions" covers all building chats, but a count is given only for one of them (22 of 41, 53.7 %), without naming the chat or the rule by which it was chosen. |
| Suggestion | Give the count for each building chat (or the total), or name the chat and say why it was chosen. |
| Status | verified; inferred (53.7 %) |
| Severity | minor |
| Source | SD |

**GB-17 How the expected answers reached the voice call is not described, although the call could not read session files and the text chat shows the questions without answers.**

| Field | Content |
|---|---|
| Check | P25 |
| Location | p. 6, l. 138 to 139; p. 7, l. 145, l. 148; Table 6, row 6, column Trigger; Table 3, row Session blocks (p. 10) |
| Quotation | "During a voice call, the assistant could neither update the learning record nor read the excerpt of a session from its file"; "In the text chat, the assistant shows the excerpt and the three questions without their answers." |
| Concern | Step 5 grades each answer, and the grading rule asks whether "the core of the answer" is given. According to l. 138 to 139 and l. 145, the call had the excerpt and (from 2.6.5, by hand in narrative sessions 8 to 10) the questions, but not the expected answers. In narrative sessions 1 to 7 only the excerpt was shown (Table 6 row 6), so the questions themselves had to come from elsewhere. It is therefore open whether the call graded against the stored expected answer or against its own reading of the excerpt, and where the questions came from in sessions without prior display. The manuscript itself suggests the second: deviating questions occurred exactly where questions were not shown. |
| Suggestion | In Sect. 3.2 state which content of the learning path (questions, expected answers) was in the context of the call in each version, and how; in Sect. 3.5.2 state whether grading compared the answer with the expected answer or with the excerpt. |
| Status | inferred (from l. 138 to 139, 145 and Table 6 row 6); assumption (actual context of the call) |
| Severity | moderate |
| Source | SD |

**GB-18 Sections 3.2 and 3.5 describe version 2.6.6, under which none of the 25 sessions ran, and the note on this stands only in Sect. 3.6.**

| Field | Content |
|---|---|
| Check | P7, P17 |
| Location | p. 7, l. 142 to 149; Fig. 2 caption, p. 7, l. 151; p. 9, l. 194 to 201; p. 12, l. 262 to 272; Fig. 4 (p. 15); Table 5 (p. 15); Table A2, rows 2.2.0 and 2.3.1 |
| Quotation | "Sections 3.2 and 3.5 describe the current version 2.6.6 (Appendix A), which brings together the rules that arose from these sessions; no session in the data ran under it or under its predecessor 2.6.5." |
| Concern | The manuscript discloses the version history with unusual care and shades Fig. 4 by version. The described method, however, did not apply to any reported session: 3 sessions ran under 2.3.1 (12 %), 8 presumably under 2.4.0 (32 %), 14 under 2.5.0 (56 %), 0 under 2.6.5 or 2.6.6. Step 2 of the six-step cycle (questions shown before the call, l. 145) applied in at most 3 of 25 sessions (12 %, narrative sessions 8 to 10); for "no hint, even when asked" and "decimal digits spoken one by one" the sessions in which they applied are not stated. A reader of Sect. 3.2 and 3.5 reads the steps in the present tense as the procedure behind Tables 5 and 6. Table 5 groups SN version 6 across 2.3.1 and 2.4.0. In addition, Table A2 says the order of 2.3.1 relative to 2.2.0 (learning record file) "could not be determined", so it is open whether sessions 1 to 3 ran under a version with the record function. |
| Suggestion | In Sect. 3.2, before l. 142, state that the six steps describe 2.6.6 and that the sessions ran under 2.3.1 to 2.5.0; add to Sect. 3.6 a table with one row per rule of Sect. 3.2 and 3.5, the first version containing it and the sessions in which it applied (installed, applied by hand, or not yet); in Table 5 split SN version 6 into sessions 1 to 3 and 4 to 11. State whether 2.3.1 contained the learning record function. |
| Status | verified (version assignment and shares from l. 262 to 272 and Fig. 4); inferred (shares) |
| Severity | moderate |
| Source | SD |

**GB-19 In Fig. 2 the transfer of questions into the list To review is drawn as a regular step, while the text says it happens at the learner's request; which is meant?**

| Field | Content |
|---|---|
| Check | P3 |
| Location | Fig. 2, arrow from "Update learning record, hand it over as a file" to "To review: questions answered incorrectly or only partially correctly", p. 7; caption p. 7, l. 152 to 155; text p. 11, l. 221 |
| Quotation | "Questions answered incorrectly or only partially correctly are collected in the list To review [...] dashed arrows mark steps that follow only on request or with the next session"; "At the learner's request, questions answered incorrectly or only partially correctly are collected in the list To review and later taken up in review sessions." |
| Concern | The caption defines dashed arrows as steps "only on request". The arrow into To review is solid (profile at y = 984 px of the 300 dpi render: one pink run of 66 px, #cc7aa7, no gap), while the following arrow to the review session is dashed (profile: four pink runs of 7 to 20 px separated by gaps). Read with the caption, the figure says every incorrect or partially correct answer goes into the list automatically. Line 221 can be read in two ways: the list was introduced at the learner's request, or entries are made only when the learner asks. In the second reading the arrow should be dashed. Since the text is ambiguous, this is put as a question. |
| Suggestion | Clarify in l. 221 whether "At the learner's request" refers to the introduction of the list or to each entry; if each entry needs a request, draw the arrow into To review in Fig. 2 dashed. |
| Status | verified (line style at the page image); inferred (the reading of l. 221) |
| Severity | minor |
| Source | AB |

**GB-20 That the excerpt was read verbatim in the call is not measured, and this is disclosed only in the Discussion, not where verbatim reading is introduced.**

| Field | Content |
|---|---|
| Check | P31, P17 |
| Location | p. 9, l. 194 to 201; p. 1, l. 11 to 12; p. 18, l. 387 to 389; p. 19, l. 401 to 403; Fig. 7 caption, p. 19, l. 409 to 411; p. 11, l. 232 to 233 |
| Quotation | "In voice mode, only the form of the text may change, never its content"; "the call, in which the excerpt is read in full and the three questions are asked and graded"; "Reading the excerpt, asking the questions and grading in the call rest only on rules or procedure (dashed lines), and Table 6 shows that these rules did not always hold." |
| Concern | Fig. 7 shows clearly which links are checked. The consequence is not carried back: Sect. 3.5.1 and the RQ2 answer (l. 388) state as fact that the excerpt "is read in full", while no session was checked for whether the spoken text matched the excerpt. The verbatim principle is the central safeguard of the design (l. 32 to 33), and its effect in the call, where the learner hears the material, is the link that was not measured. Sect. 3.6 says only that voice input is available as speech recognition text; whether the assistant's spoken output is kept is not stated. |
| Suggestion | In Sect. 3.5.1, after l. 194, add one sentence that adherence to these rules was not measured (Fig. 7); in the RQ2 answer write "is to be read in full". If the call text of the assistant is kept, compare it word by word with the excerpt for the 23 voice sessions (for example with a diff) and report deviations per session in Sect. 4.3; if it is not kept, say so in Sect. 3.6. |
| Status | verified (not measured, location of disclosure); assumption (availability of call text) |
| Severity | moderate |
| Source | SD |

**GB-21 The data availability statement says nothing about two of the four kinds of data source named in Sect. 3.6, the chats and the output of the check script, nor about the checks of the method analyses and the further sources named in the Results.**

| Field | Content |
|---|---|
| Check | P12 |
| Location | p. 11, l. 232 to 233, l. 237 to 238, l. 245 to 249; p. 13, l. 284 and l. 292; p. 15, l. 344 to 345; p. 24, l. 494 to 500 |
| Quotation | "The data come from four kinds of source. First, the chats in which the fact documents and learning paths were built and the sessions were held"; "Third, the output of the check script for every learning path in Table 4 (Sect. 3.4)."; "Three of them were checked by a separate agent of the same model family"; "The first analysis was examined only by a later meta-analysis."; "the complete learning records and the method analyses of the chats are not published." |
| Concern | Sect. 3.6 lists its sources clearly and states that every statement rests on a chat passage or a checked file (l. 240 to 242). The statement in l. 494 to 500 addresses two of these four kinds (learning records and method analyses: "not published") and is silent on the other two. (a) The check script output for the seven runs of Table 4 is the basis of every value in Table 4 (anchors, words, answers, "first run 577 findings") and of Table 6 no. 3; it concerns no person, and no reason is given for not making it available. (b) The chats are the first data source and the basis of the quotations and counts in Sect. 3.2 (for example "22 of 41 inputs", l. 134) and Sect. 4; they concern the learner, so withholding them would be justified, but the statement does not say whether they are withheld or why. (c) The reports of the separate agent that checked three method analyses (18 deviations; 85 and 93 statements, 30 and 37 deviating; 31 and 34 findings, l. 245 to 247), the later meta-analysis (l. 247) and the chat log that replaces the transcript for 74 of 86 inputs of one chat (l. 248) are data sources named in the Methods and are not mentioned. Count: 4 kinds of source in Sect. 3.6, 2 addressed in the statement. (d) Sources named only in the Results are not mentioned either: the project script that compared the volcanology fact document with the raw text (l. 284), the inventory of 144 sentences (l. 292) and the check of the narrative version by a second AI agent (l. 344 to 345). Whether the linked repository holds any of this was not checked in this review. |
| Suggestion | Extend Code and data availability (p. 24, l. 494 to 500) with one sentence per source of Sect. 3.6: the check script output of the seven runs in Table 4 (publish it in the repository or as a supplement, since it contains no personal data, or give the reason it is withheld); the chats and the assistant's chat log (state that they are not published and why, for example because they contain the learner's spoken inputs); the agent reports on the method analyses and the meta-analysis, the project script, the sentence inventory and the agent check of the narrative version (state their status). |
| Status | verified (content of Sect. 3.6, of the Results and of the statement, at the page images p. 11, p. 13, p. 15 and p. 24); repository contents not checked |
| Severity | moderate |
| Source | S2 |

**GB-22 The method analyses, the crediting of sessions and the hand-set anchor are not described so that a reader could repeat them.**

| Field | Content |
|---|---|
| Check | P8 |
| Location | p. 11, l. 238 to 239, l. 244 to 247; p. 11, l. 228 to 230; p. 14, l. 325 to 327; Table 4, row Geology of Germany, column Exclusions and corrections until passed; p. 24, l. 499 to 500 |
| Quotation | "four method analyses of the chats in which the skill was developed and used, written between 1 and 9 October 2026; they are cited as a data basis and are not published"; "eight new sessions whose material lay entirely in completed sessions were credited"; "opening anchor of session 20 set by hand" |
| Concern | The method analyses are a data basis for Table 6 (l. 353), but how they were produced (instructions, skill, scope), what the checking agent counted as a deviation, and what happened to the 18, 30 and 37 deviations (corrected, discarded, kept) is not stated; a "later meta-analysis" is mentioned without description. The counts also switch unit without explanation: 18 deviations in one analysis without a denominator, then 30 of 85 and 37 of 93 statements deviating (35.3 % and 39.8 %) and 31 and 34 findings, so that 31 findings arise from 30 deviating statements. Crediting decides that 8 of the 17 sessions counted as done in v7 were done (only 4 of 17, 23.5 %, were asked), but whether the overlap was determined by script or by the assistant's judgment is not stated. For the hand-set anchor of session 20, the reason and the rule are not given, and whether it meets condition 2 of Sect. 3.4 is not visible. |
| Suggestion | In Sect. 3.6 describe the procedure of the method analyses and of their check in two or three sentences and say how deviations were resolved; in Sect. 3.5.3 state how "material lay entirely in completed sessions" was determined; in Table 4 or Sect. 4.2 give the reason for the hand-set anchor. |
| Status | verified (not described); inferred (23.5 %) |
| Severity | moderate |
| Source | SD, S3 |

**GB-23 The statement that every statement rests on an original chat passage or a checked file is contradicted by the data limits in the same section.**

| Field | Content |
|---|---|
| Check | P6, P19 |
| Location | p. 11, l. 240 to 242; p. 11, l. 244 to 249; p. 12, l. 262 to 263, l. 268; p. 16, l. 353 |
| Quotation | "Every statement in this paper rests either on a chat passage read in its original wording or on a file checked with a measured value."; "so that the wording of 74 of its 86 inputs rests only on the chat log the assistant kept during the work" |
| Concern | The manuscript names its data limits openly. The absolute statement in l. 240 does not hold against them: for one chat, 74 of 86 inputs (86.0 %) are known only from the assistant's own log, which is model generated, not an original wording; the version of sessions 4 to 11 is "presumably" assigned (l. 263) and later versions "as far as the chats show" (l. 268); Table 6 rests partly on method analyses in which the checking agent found 30 of 85 (35.3 %) and 37 of 93 (39.8 %) statements deviating. Which statements of the paper, in particular which rows of Table 6, rest on which class is not stated. |
| Suggestion | Replace l. 240 to 242 with a statement that names the exceptions, and add to Table 6 a column "source" (chat passage, learning record, method analysis, assistant log) per row; name which chat is affected by the context compaction and which reported statements come from it. |
| Status | verified (contradiction); inferred (shares) |
| Severity | moderate |
| Source | SD |

**GB-24 The statement makes available only skill version 2.6.6, under which no session ran; the rule files of the versions that produced the session data are not mentioned.**

| Field | Content |
|---|---|
| Check | P12 |
| Location | p. 12, l. 262 to 272; p. 23, Table A2 (l. 490 ff.); p. 24, l. 495 |
| Quotation | "Sections 3.2 and 3.5 describe the current version 2.6.6 (Appendix A), which brings together the rules that arose from these sessions; no session in the data ran under it or under its predecessor 2.6.5."; "The skill lernpfad-sitzungen, version 2.6.6, is available under the MIT License" |
| Concern | The manuscript discloses openly which skill version each group of sessions ran under (2.3.1, presumably 2.4.0, 2.5.0, l. 262 to 268) and that 2.6.6 ran no session. The statement, however, offers only 2.6.6 and says nothing about the rule files of 2.3.1, 2.4.0 and 2.5.0, under which all 25 sessions ran. The script versions of the check runs are taken up in GB-28. Table A2 summarises the changes per version but is not the files. The skill versions concern no person. |
| Suggestion | Add to Code and data availability (p. 24, l. 495) whether the versions 2.3.1, 2.4.0 and 2.5.0 are archived (for example as tagged releases in the repository) or no longer available; the script version of each check run belongs in Table 4 (GB-28). |
| Status | verified |
| Severity | moderate |
| Source | S2 |

**GB-25 The example pair shipped with version 2.6.6 asks for numbers and dates, which the skill's own rule since 2.5.0 avoids.**

| Field | Content |
|---|---|
| Check | P5, P18 |
| Location | Table A3 (p. 23 to 24), rows Question 3.1 and 3.3; p. 2, l. 40 to 41; Table A2, row 2.5.0; p. 24, l. 497 to 498; p. 9, l. 189 to 190 |
| Quotation | "From version 2.5.0 on, the skill aims its questions at relations and events instead of numbers, dates and names."; "How long is the Transscandinavian Igneous Belt according to the two sources cited?" |
| Concern | The example session meets the formal rules (496 words, at most 550; expected answers of 24, 21 and 22 words in the translation, within 5 to 30). The expected answer of question 3.1 is a length in kilometres, and that of question 3.3 a list of named periods ending with an age of 55 Ma, so two of the three example questions ask for numbers, dates or names. The package distributed with 2.6.6 contains this pair as learning path version 5 (l. 497 to 498), built before 2.5.0. A reader who builds on the example will reproduce the question type the paper has moved away from, and the shipped example does not show the rule it describes. |
| Suggestion | In Code and data availability and in the Table A3 caption state that the example pair predates 2.5.0 and does not follow its question rule, or replace the example by a session of SN version 7 or a path built under 2.6.6. |
| Status | verified (rule, questions); inferred (word counts of the translation) |
| Severity | moderate |
| Source | SD |

#### Minor corrections

| ID | Location | Quotation | Replacement | Source |
|---|---|---|---|---|
| KK-02 | p. 5, Table 1 caption, l. 115 to 116 | "Sessions run: sessions in the learning records;" | "Sessions run: sessions in the learning records; Review sessions: completed review sessions, not counting a review of the narrative version broken off before any answer (Table 6, No. 5);" | S3 |
| KK-03 | p. 6, Fig. 1, row 2, column Case | "Geological eras" | "Geological eras, fact document" (as in Table 1, row 2) | S2 |
| KK-04 | p. 23, Table A1, row review session, column Command | "‘Wiederholung" / "ssitzung’" (cell break without hyphen) | "‘Wiederholungs-" / "sitzung’" or the unbroken "‘Wiederholungssitzung’" | S4 |

#### Verification log

| ID | Check | Checked | Values | Result |
|---|---|---|---|---|
| PP-21 | P12 | Learning records and method analyses against the statement | Statement l. 499 to 500: "the complete learning records and the method analyses of the chats are not published", no reason given. Both contain the learner's answers or inputs (Table 3: "the learner’s answer, the grade and the verbatim answer"; analyses of the learner's chats, l. 238 to 239). The manuscript discloses non-publication itself (l. 218 to 219, l. 239) and replaces the records with invented examples (Table 3). | no finding: the data concern a person, so withholding without a stated reason is not a finding under P12 |
| PP-22 | P12 | Contents of the skill package and the appendix against Sect. 3.2 and Table A2 | Statement l. 496 to 497: SKILL.md, lernpfad.py with tests, licence file, example pair; Sect. 3.2 l. 128 to 130: rule file, check script with tests, example pair; Table A2, 2.6.6: "licence file". Appendix A (Tables A1 to A3) stands in the manuscript and counts as accessible. Per case summary figures in Table 1, Table 4 and Table 5 as stated in l. 498 to 499; per session values in Fig. 4 are integer stacked bars (0 to 3), per day counts in Fig. 5 are printed in the circles (3, 4, 4, 4 = 15; 5, 4, 1 = 10). Link to GitHub present; reachability not checked. | no finding |
| PP-23 | P38 | Versions 5, 6, 7 of the learning path on southern Norway | v5 and v6 named as one path in l. 301 to 302 and Table 4, row 2 ("same learning path as version 5, renamed"); v6: 11 sessions (Table 1, Table 5, Fig. 4 sessions 1 to 11); v7: 31 sessions, 8 credited + 5 closed + 4 asked = 17 done, 31 minus 17 = 14 open (l. 325 to 327, Python); asked sessions 14 to 17 in Fig. 4; Table 6 no. 7 "session 9 of version 6 and session 17 of version 7". | no finding |
| PP-24 | P38 | Skill version identifiers in Sect. 3.6, Table 6, Table A2, Fig. 4, Fig. 5 | 2.1.0, 2.2.0, 2.3.1, 2.4.0, 2.5.0, 2.6.0 first line, 2.6.0 second line, 2.6.1, 2.6.5, 2.6.6. The double number 2.6.0 is explained in the Table A2 caption (l. 490 to 491) and used as "first line" (7 text lines) and "second line" (Table 6 no. 9, Table A2) throughout; "version 2.6.6" in Fig. 2 caption, Table A1 title and l. 271 consistent. | no finding |
| PP-25 | P38 | Rows of Table 1 against Table 4 (names and numbers), with Python | Words 14,267; 3,595; 4,692; 9,682; 19,519 equal in both tables; sessions 31, 11, 10, 25, 38 equal; questions = 3 x sessions in all five rows; anchors = 2 x sessions in all five rows; sessions run 11 + 4 + 10 = 25 = 23 voice + 1 screen + 1 partly (l. 322 to 323). Name differences: see GB-12, GB-13, KK-03, GB-12. | no further finding |
| PP-26 | P38 | Further identifiers across the manuscript | Skill name lernpfad-sitzungen (all occurrences identical); "check script" (21 text lines) and lernpfad.py (l. 497) one object; list "To review" (8 text lines, no variant); grades correct, partially correct, not correct (Table 2, Table 3, Table 5, l. 256); review modes verbatim, explain, both (Table A1, Table A2) and "explanation mode" (l. 432, l. 449) for the explain mode; model "Claude Opus 5.5" (l. 126, l. 274); "Claude app for Android" (l. 127, l. 274); commands in l. 143 and l. 222 to 223 match the glosses of Table A1. Different objects with similar names checked and kept apart: "a later meta-analysis" (l. 247, internal) and the literature meta-analyses; "a separate agent" (l. 245, checks of method analyses) and "a second AI agent" (l. 344, check of the narrative version); "project script" (l. 284) and the check script. | no finding |
| PP-27 | P3 | Fig. 1 bars and labels against Table 1, Table 4 and l. 113 to 114 | Grey bars (fill #e4e4e4, start 1395 px): 31 sessions 421 px, 11: 147 px, 10: 134 px, 25: 338 px, 38: 516 px, that is 13.36 to 13.58 px per session; orange bars (#e89c04): 15: 202 px, 10: 133 px (13.47 and 13.30 px per session); deviation below one session for every bar. Labels: versions 7, 7, 8, 1, 4 and sessions 31, 11, 10, 25, 38 as in Table 1; sessions run 15 (11 on version 6, 4 on version 7) and 10; review sessions 1, 0, 1, 0, 0 as in Table 1 and l. 340 to 341; "passed after exclusions" for narrative version, Germany and volcanology as in Table 4; "(English)" only for volcanology as in l. 113 to 114. The caption itself discloses that the southern Norway bar of sessions run mixes versions 6 and 7. | no finding beyond GB-14 |
| PP-28 | P3, P29 | Figs. 2 and 3: labels and colours against captions and l. 142 to 149, 173 to 182, 205 to 207, 302 to 306 | Fig. 2: chat background #ecf4fc, call background #fcf4e4, chat boxes #0474b4, call boxes #e49c04, review boxes #cc7ca4 to #cc84ac ("Pink marks the review part"); dashed arrows "next session" and "on request"; boxes match steps 2 to 6 of l. 145 to 149. Fig. 3: paragraphs #0474b4, image block #5cb4ec (light blue), excluded chapters #9c9c9c dashed (grey), sessions and questions #e49c04 (orange), check script #049c74 (green), each as in l. 186 to 188; checks a to e match the five checks of l. 181 to 182 and l. 302 to 306; "up to about 550 words" and "5 to 30 words" as in l. 205 to 207. Fig. 3 declares itself schematic (l. 188); no proportions checked. | no finding beyond GB-19 |
| PP-29 | P5 to P38 (design sketch) | whole manuscript, all captions, Appendix A: questions, type, data sources, time line, environment, principles, disclosed limits, chain from framework to result, proposals | self-experiment, descriptive multiple case study, closest to autoethnography (l. 250 to 251); one learner, five cases, six learning paths in seven check runs, 25 sessions on two cases (11 + 4 + 10), two reviews; no control condition; data window 27 September to 13 October 2026 (l. 258 to 259); data sources: chats, four learning records, check script output, four method analyses, learner's account; skill versions 2.1.0 to 2.6.6, sessions under 2.3.1 (3), 2.4.0 presumed (8), 2.5.0 (14); model Claude Opus 5.5, effort medium (l. 126) | basis for the design checks; no finding of its own |
| PP-30 | P5 | formal rules against own tables: anchors = 2 x sessions, answers = 3 x sessions, Table 1 against Table 4, Table 5 sums, words per session | anchors 60/60, 60/60, 62/62, 22/22, 20/20, 50/50, 76/76; answers 90, 90, 93, 33, 30, 75, 114; Table 1 words and questions equal Table 4; Table 5 sums 33, 12, 30; mean words per session 463, 460, 327, 469, 387, 514 (limit about 550); example pair 28 of 30 within 550 (93.3 %), longest 659, disclosed; Table A3 session 496 words, answers 24, 21, 22 words | no finding except GB-25 |
| PP-31 | P17 | location of other disclosed limits | no control, no retention claim, records by assistant, self-analyses, 74 of 86 inputs, check binds only to fact document, sessions on two cases: each stated in Sect. 1, 3.1, 3.3 or 3.6 where the method is introduced | no finding except GB-20, GB-18, GB-11, GB-03 |
| PP-32 | P26 | version mismatch guarantee (l. 227 to 228); exclusions and default (Table 6 row 4) | mismatch report: no counterexample in the manuscript, timing of eras v10 open (GB-11); exclusions replacing default disclosed as not fixed in 2.6.6 | no finding |
| PP-33 | P32 | speech recognition errors "interpreted correctly by the assistant in the recorded cases" (l. 215 to 216) | qualified by "in the recorded cases"; two examples named | no finding; unrecorded misrecognitions cannot be counted, wording already restricts the claim |
| PP-34 | P19 | provenance of core statements | Table 4: primary (script output); Table 5, Fig. 4, modes, To review: model generated records, disclosed (l. 243); Sect. 4.8: self-report, disclosed (l. 375); Table 6: mixed, not stated per row (GB-23) | no finding except GB-23 |

### Segment 3: Results (p. 13 to 18)

#### Substantive findings

**GB-26 The fact documents are called verified, but Sect. 4.1 reports a check against the sources for neither of the two fact documents behind the 25 sessions, and no estimate is given of errors that all checks missed.**

| Field | Content |
|---|---|
| Check | P11, P15, P32 |
| Location | p. 13, l. 282 to 293; p. 7, l. 157 to 166; p. 1, l. 7; p. 3, l. 43; p. 18, l. 385 to 387; p. 19, Fig. 7, annotation above Sources and Fact document; p. 22, l. 467 |
| Quotation | "How the fact documents were checked therefore matters."; "learning paths from his own verified fact documents"; "checked in each document project, by different procedures; errors found late (Sect. 4.1)"; "the learner assembled learning content from his own verified fact documents with an AI assistant" |
| Concern | The manuscript states the dependency itself: the check script compares a learning path only with its fact document, so errors in the fact document "pass into the learning path unnoticed" (l. 282 to 283; also l. 385 to 387 and Fig. 7). Sect. 4.1 then reports how the fact document on volcanology was checked (word comparison against the raw text, two serious errors found later, l. 283 to 287), how the one on the geology of Germany was checked (source cycle and a final consistency check, l. 287 to 292), and that the narrative version was built from an inventory of 144 sentences and checked for completeness against its source (l. 292 to 293, l. 343 to 345). For southern Norway and the geological eras, Sect. 4.1 and Sect. 3.3 (l. 157 to 166) give the brief, the sources and the project structure, but no check procedure and no result. These are the two fact documents behind all 25 sessions: 15 on southern Norway and 10 on the narrative version derived from the eras document. Fig. 7 nevertheless says "checked in each document project, by different procedures", and the Abstract (l. 7), RQ1 (l. 43) and the Conclusions (l. 467) use "verified" without restriction. Where checks are reported, each later check found errors the earlier one missed (volcanology: two serious errors after a word-by-word comparison; Germany: 49 first mentions without the English term after the template checks, l. 290 to 291), so the residual error rate is unknown, and no independent sample of statements or expected answers was checked against the sources. For volcanology, the text also does not say whether the two errors were corrected before the check run of 9 October. Severity moderate: the binding of learning path to fact document stands (Table 4), but a reader cannot verify the qualifier "verified" for the fact documents behind the reported sessions; the Discussion names the dependency (l. 385 to 387), the Conclusions do not draw the consequence. |
| Suggestion | In Sect. 4.1, add one or two sentences each for southern Norway and the geological eras: which check was run, against which sources, when, and what it found; state for volcanology whether the two errors were corrected before the check run in Table 4. Optionally report an independent check of a random sample of expected answers per learning path against the cited sources (for example 60 per path; with zero errors the 95 % upper bound by the rule of three is 3/60 = 5 %). If no such checks were made, replace "verified" in the Abstract (l. 7), RQ1 (l. 43), the Fig. 7 annotation and l. 467 with wording that names what was checked, and state that the residual error rate is unknown. |
| Status | verified (no check reported for the two documents in Sect. 3.3 and 4.1; errors found late); inferred (rule-of-three bound) |
| Severity | moderate |
| Source | S3, S4, SD |

**GB-27 "Seven check runs" counts only the passing run per learning path (plus one re-measurement), while at least three paths needed earlier runs whose outcome is reported for one only.**

| Field | Content |
|---|---|
| Check | P20, P11 |
| Location | p. 13, l. 301 and l. 306 to 309; p. 14, Table 4, caption (l. 310 to 314) and column "Exclusions and corrections until passed", rows "Geological eras (narrative version), version 8", "Geology of Germany", "Volcanology, stage 1" |
| Quotation | "Table 4 lists seven check runs of six learning paths"; "Three of them passed only after chapters that the learning path itself marks as no learning material had been named as exclusions"; "first run 577 findings"; "Southern Norway, version 5, is the example pair of the skill and was re-measured on 13 October 2026 with the script of version 2.6.6; the original run had counted 13,859 words" |
| Concern | The arithmetic of Table 4 holds (anchors = 2 × sessions and answers = 3 × sessions in all seven rows; words identical to Table 1; 13,890 minus 13,859 = 31 words explained by the script change). The unit "check run", however, changes within the table: six rows are the final, passing run of a path, and the row for version 5 is a re-measurement of 13 October that replaces the original run. The Germany row itself names a "first run", so that path had at least two runs, and "passed only after" (l. 306) implies the same for the narrative version and volcanology. So at least ten runs took place (7 listed + at least 3 earlier failing runs, plus the original run of version 5), of which the table lists seven. For the earlier runs, a count of findings is given for Germany (577) only; for the narrative version and volcanology the cell gives only a description. The column heading "until passed" signals the intent, but the sentence in l. 301 reads as a full count. |
| Suggestion | In l. 301 write "the passing check run of each of six learning paths (seven rows; versions 5 and 6 ...)", and in Table 4 give for every path with exclusions the number of runs and the findings of the first run, as for Germany. |
| Status | verified (wording and table cells); inferred (minimum number of runs, calculated) |
| Severity | minor |
| Source | S3 |

**GB-28 The version of the check script is not given for most runs in Table 4, and the checks listed in Sect. 4.2 did not exist for four of the seven runs.**

| Field | Content |
|---|---|
| Check | P35, P30, P7 |
| Location | Table 4 caption, p. 14, l. 310 to 314; Table 4, row Volcanology, column Exclusions and corrections until passed; p. 13, l. 302 to 306; Fig. 3 (p. 9), check box items d and e; Table A2, rows 2.6.0 second line and 2.6.1; Table 6, row 9 |
| Quotation | "in addition, every image block must be assigned to exactly one session, and excluded chapters must not be covered. All six paths passed."; "Version 6 was checked on 30 September 2026 with the script then in use, which already counted 13,890 words." |
| Concern | The manuscript reports the changed word count of the v5 re-measurement, which shows that the script changed. For the other runs the script version is not given: only the re-measurement of version 5 names its script (2.6.6), version 6 used "the script then in use", and the original run of version 5 counted 13,859 words against 13,890 with the script of 2.6.6, a difference of 31 words (l. 311 to 314). Image blocks enter the skill only with 2.6.0 second line on 9 Oct (Table A2), so the runs for SN v6 (30 Sep), SN v7 (before 8 Oct), and the two eras paths (5 Oct) cannot have included check d of Fig. 3: 4 of 7 runs (57 %). The volcanology run is listed with exclusions only, although Table 6 row 9 reports that 2.6.0 second line skipped an image block in that case and 2.6.1 fixed it; whether the passing run came after the fix is not stated. |
| Suggestion | Add a column "script version and date" to Table 4; in the Volcanology row add the image-block fix of Table 6 row 9 to "corrections until passed"; or re-run all six paths with the 2.6.6 script, as done for v5, and report both runs. |
| Status | verified (missing versions, dates of image-block function); inferred (4 of 7) |
| Severity | moderate |
| Source | S2, SD |

**GB-29 Counts of check findings are given without unit or base: 577 findings exceed the 125 items the check verifies, and 49 first mentions have no total.**

| Field | Content |
|---|---|
| Check | P20 |
| Location | p. 14, Table 4, row "Geology of Germany", last column; p. 16, Table 6, row 3, column "Stumbling point"; p. 13, l. 290 to 291 |
| Quotation | "first run 577 findings"; "577 findings in the first check"; "Only the consistency check at the end found 49 first mentions without the English term in brackets" |
| Concern | The learning path on the geology of Germany has 25 sessions with 50 anchors and 75 expected answers, so 50 + 75 = 125 items of those types; 577 findings must therefore be counted on another unit (for example words, paragraphs or passages covered outside the learning material), which neither table names. The number signals the size of the problem caused by the replaced default (Table 6, No. 3 and 4), but cannot be read without the unit. Likewise, 49 first mentions without the English term cannot be placed without the number of first mentions checked. |
| Suggestion | In the Table 4 caption, define what one finding of the check script is; in l. 291, give the base ("49 of n first mentions"). |
| Status | verified (values); inferred (the comparison with 125 items, calculated) |
| Severity | minor |
| Source | S3 |

**GB-30 In Fig. 4 the sessions of versions 6 and 7 of the southern Norway path cannot be told apart, so the numbers 14 to 17 read as a continuation of 1 to 11.**

| Field | Content |
|---|---|
| Check | P29 |
| Location | Fig. 4, legend entry "Southern Norway (versions 6, 7)" and session numbers below the bars on 8 October, p. 15; caption p. 15, l. 331; text p. 14, l. 325 to 327 |
| Quotation | "Southern Norway (versions 6, 7)"; "numbers below the bars are session numbers"; "17 of the 31 sessions of version 7 on southern Norway were done: 8 credited from version 6, 5 closed at the learner's request without being asked and 4 asked" |
| Concern | Both learning paths share one colour line (measured #0474b4 under all 15 southern Norway bars) and one legend entry. The bars on 30 September to 2 October carry the numbers 1 to 11, the bars on 8 October the numbers 14 to 17. Without the text a reader takes these as sessions 14 to 17 of the same path and looks for sessions 12 and 13. That 14 to 17 belong to version 7 and that sessions 1 to 13 of version 7 were credited or closed is said only in l. 325 to 327. The text itself warns that the two paths are not to be compared (l. 324), which the shared encoding invites. The text is consistent (the numbering 14 to 17 follows from 8 credited and 5 closed sessions, PP-37); the finding concerns the figure alone. |
| Suggestion | In Fig. 4 mark the 8 October bars as version 7, for example with "v7: 14 to 17" below them or a separate legend entry, and add to the caption: "on southern Norway, sessions 1 to 11 belong to version 6 and sessions 14 to 17 to version 7 (Sect. 4.4)". |
| Status | verified (colours measured, numbers read at a 300 dpi render of p. 15) |
| Severity | minor |
| Source | AB |

**GB-31 Fig. 4 shows the grades after regrading, but its caption does not say so, while the shading suggests the grades of the version in use.**

| Field | Content |
|---|---|
| Check | P37 |
| Location | Fig. 4 (p. 15), sessions 1 to 3 on southern Norway; Fig. 4 caption, p. 15, l. 331 to 334; Table 5 caption, p. 15, l. 328 to 329; p. 10, l. 213 to 214 |
| Quotation | "Shading marks the skill version in use"; "Grades after the regrading of three answers of version 6 under the tolerance rule" |
| Concern | Table 5 labels the regrading correctly. The bars of Fig. 4, measured on the page image, sum to the values of Table 5 (SN v6: 12 correct, 8 partially correct, 13 not correct; v7: 1, 5, 6; narrative: 16, 6, 8), so Fig. 4 also shows regraded values. Sessions 1 to 3 are shaded 2.3.1, but their grades follow the tolerance rule of 2.4.0. Which bars changed is not marked. |
| Suggestion | Add to the Fig. 4 caption: "Grades after the regrading of three answers of version 6 under the tolerance rule (Table 5)", and mark the three regraded answers in the bars or name their sessions. |
| Status | verified (bar values measured at the page image) |
| Severity | minor |
| Source | SD |

**GB-32 Fig. 4 shows four dashed version lines, while the caption promises all versions of Table A2 dated to the day, which are six.**

| Field | Content |
|---|---|
| Check | P24 |
| Location | Fig. 4, dashed lines and their labels above the plot, p. 15; caption p. 15, l. 332 to 333; Table A2, p. 23, rows 2.6.0 second line and 2.6.1 |
| Quotation | "dashed lines the build dates of the versions dated to the day in Table A2"; "2.6.0, second line"; "9 October 2026" |
| Concern | Table A2 dates six versions to the day: 2.2.0 (29 September), 2.4.0 (30 September), 2.6.0 second line (9 October), 2.6.1 (9 October), 2.6.5 (12 October), 2.6.6 (13 October). Fig. 4 has four dashed lines, measured at 586.5, 744.0, 1946.5 and 2051.5 px, which convert to 29 September, 30 September + 0.50 d, 12 October and 13 October (calibration on the ticks 29 September at 587 px and 13 October at 2052 px, ±0.01 d). The 9 October tick (measured at 1633.5 px) carries no line, although two versions were built that day. Count: 4 lines against 6 dated versions. |
| Suggestion | Add a dashed line at 9 October labelled "2.6.0 (2nd line), 2.6.1" in Fig. 4, or restrict the caption, l. 332 to 333, to the versions actually drawn. |
| Status | verified (lines measured, Table A2 at the page image) |
| Severity | minor |
| Source | AB |

**GB-33 The To review balance for version 6 on southern Norway does not close against Table 5: 24 entries against 21 answers that are not correct.**

| Field | Content |
|---|---|
| Check | P23, P2 |
| Location | p. 15, l. 338 to 340; p. 15, Table 5, row "Southern Norway, version 6", columns "Partially correct" and "Not correct", and caption; p. 11, l. 221 |
| Quotation | "held 35 entries for that case: 24 from version 6, of which two had been closed by regrading and one in a review session, and 11 from version 7; 32 were open"; "Grades after the regrading of three answers of version 6 under the tolerance rule"; "questions answered incorrectly or only partially correctly are collected in the list To review" |
| Concern | The balances for the other two learning paths close exactly: version 7 has 5 + 6 = 11 answers that are not correct and 11 entries; the narrative version has 6 + 8 = 14 and 14 entries, of which 13 are open. For version 6, Table 5 gives 8 + 13 = 21 answers that are not correct after regrading, but the list holds 24 entries. The total of open entries itself is consistent (35 minus 2 minus 1 = 32), which is why the check of the same totals in the Discussion found nothing (PP-61); the balance per version does not close. The gap of three equals the number of regraded answers, but the text names only two entries closed by regrading. With r regraded answers moving from not or partially correct to correct, the number of answers that were not correct before regrading is 21 + r: r = 0 gives 21 (gap 3), r = 1 gives 22 (gap 2), r = 2 gives 23 (gap 1), r = 3 gives 24 (gap 0). Resolution A: all three regraded answers moved to correct, but only two of their entries were closed by regrading; the third stayed in the list, and either it is the entry later closed in the review session (then the 21 open entries for version 6 equal the 21 answers that are not correct) or it is still open while one answer that is not correct was closed in review. Resolution B: two answers moved to correct (matching "two had been closed by regrading"), and the list holds one entry that does not come from an answer graded not correct or partially correct, for example the hinted answer to question 4.3 that was graded correct (Table 6, No. 8). Under neither resolution does the manuscript state the missing step. The question is decided by two statements: how many of the three regraded answers became correct, and which entry was closed in the review session. Severity moderate: the RQ3 statement on how the record tracks what is not mastered stands, but a reader cannot reconcile the record with the grades. |
| Suggestion | In Sect. 4.5 (l. 338 to 341), state the direction of the three regradings and which entry the review closed, or add a short balance (entries from answers not correct before regrading, closed by regrading, closed in review, open) per learning path, possibly as two columns added to Table 5. |
| Status | verified (the values 24, 2, 1, 32, 21, 11, 14 and the three regraded answers stand in the manuscript); inferred (the gap of three and the resolutions, calculated) |
| Severity | moderate |
| Source | S3 |

**GB-34 The two completed review sessions are reported only as a count; their mode, topic and outcome, which the learning record keeps, are not reported, and the closure of one entry per case must be derived.**

| Field | Content |
|---|---|
| Check | P11, P22 |
| Location | p. 15, l. 338 to 341; p. 10 to 11, Table 3, row "Reviews"; p. 11, l. 224 to 227; p. 18, l. 391 to 393 |
| Quotation | "Two review sessions were completed, one for each case, each with one topic."; "per review: date, mode, topics, then each question with the learner's answer, the grade and whether the entry is done" |
| Concern | Sect. 3.5.3 announces three review modes and a structure per topic (introduction, verbatim core passage, summary, original question), and Table 3 shows that the record keeps date, mode, topics, answer, grade and state per review. RQ3 asks how review sessions are built from the record. Sect. 4.5 reports neither the date, nor the mode, nor the topic, nor the answer and grade of either review. That each review closed exactly one entry follows only by calculation: 35 minus 32 minus 2 = 1 for southern Norway and 14 minus 13 = 1 for the narrative version; l. 339 states it for southern Norway, but for the narrative version the reader must infer it. Since the review modes changed between versions 2.4.0 and 2.6.0 (Table A2), the version under which each review ran is also needed. |
| Suggestion | Add to Sect. 4.5 one sentence per review: date, skill version, mode, topic, grade of the reviewed question and whether its entry was closed. |
| Status | verified (the missing cells); inferred (one closed entry per review, calculated) |
| Severity | minor |
| Source | S3 |

**GB-35 Table 6, the instrument for the second part of RQ2, is not the complete list of incidents, and the RQ2 answer names two rules for which no incident is documented.**

| Field | Content |
|---|---|
| Check | P10, P15, P34 |
| Location | p. 16, l. 353 to 354 and Table 6; p. 18, l. 387 to 391; p. 10, l. 209 to 211; p. 14, l. 318; p. 2, l. 38 to 41; p. 20, l. 428 to 432; p. 9, l. 198; p. 12, l. 268 to 272; p. 17, Fig. 5, diamond do not interrupt the learner; p. 23, Table A2, rows 2.6.0 first line and 2.6.5 |
| Quotation | "Table 6 lists the stumbling points documented in the learning records and in the analyses of the chats"; "The rules for the call came from incidents and requests in real sessions: questions shown before the call and asked as worded, decimal digits spoken one by one, the end of the excerpt announced and, in version 2.6.5, rules against interrupting the learner." |
| Concern | The manuscript traces the split between text chat and call to a documented limitation (l. 137 to 141), and two of the four rules named in the RQ2 answer to results: the announced end of the excerpt to the third narrative session (l. 318) and the questions shown before the call to Table 6, no. 6. (a) The other two have no such passage. Decimal digits spoken one by one appear as a rule (l. 198), as a change of the first line of 2.6.0 in Table A2 and in the RQ2 answer (l. 390), but neither Sect. 4.3 nor Table 6 names the incident or request behind them. The rules against interrupting appear only in Table A2 (2.6.5, 12 October 2026), in Fig. 5 and in l. 390; the last session took place on 8 October (l. 338; Fig. 5, "no sessions after 8 October"), and no session ran under 2.6.5 (l. 271 to 272). (b) Table 6 is presented as the list of documented stumbling points, but at least four incidents with consequences described elsewhere are not in it: a spoken 'not quite right' entered as 'not correct', which led to the fixed scale (l. 209 to 211); the third narrative session, which led to the announced end of the excerpt (l. 318); the open question on the Mesozoic that is missing from the record and whose wording was shortened (l. 428 to 432, GB-41); and the confusion of orders of magnitude and "too many numbers" before 2.5.0 (l. 38 to 41). No selection rule for Table 6 is stated. (c) The first clause of the RQ2 answer describes the procedure of version 2.6.6 (Fig. 2; l. 270 to 271): showing the questions before the call is documented only for sessions 8 to 10 of the narrative version (l. 269 to 270), 3 of 25 sessions; in sessions 1 to 7 of that version only the excerpt was shown (Table 6, no. 6), and what was shown for southern Norway is not stated (GB-18). Severity moderate: the core of the answer, the division between the two channels, held for all sessions (l. 137 to 141), but a reader cannot trace two of the four named rules to an incident, and Table 6 cannot serve as the complete answer to which rules arose from incidents. |
| Suggestion | In Sect. 4.7, either extend Table 6 to all incidents named in the text, with the rule each produced, or state the selection rule in l. 353 to 354; for the decimal-digit rule and the rules against interrupting, name the incident or request with case, session and date, or limit l. 389 to 391 to the rules that the results document. In l. 387 to 389, add that the questions were shown before the call only in sessions 8 to 10 of the narrative version. |
| Status | verified |
| Severity | moderate |
| Source | S4, SD |

**GB-36 Fig. 5 omits version 2.3.1, under which the first three sessions ran, and the second line of 2.6.0, although its caption takes the versions from Table A2.**

| Field | Content |
|---|---|
| Check | P24 |
| Location | Fig. 5, row "Versions of the skill", p. 17; caption p. 17, l. 359; Table A2, p. 23; text p. 12, l. 262 |
| Quotation | "when versions of the skill appeared (Table A2; a version dated by a range is placed at its middle)"; "Sessions 1 to 3 on southern Norway, version 6, ran under version 2.3.1"; "by 30 September 2026" |
| Concern | Table A2 lists ten versions. Fig. 5 labels eight: 2.1.0 and 2.2.0 (one tick, measured 29 September + 0.21 d), 2.4.0 (30 September + 0.20 d), 2.5.0 (4 October + 0.20 d), 2.6.0 first line (dotted, 8 October + 0.20 d), 2.6.1 (9 October + 0.20 d), 2.6.5 (12 October + 0.20 d), 2.6.6 (13 October + 0.20 d); calibration on the gridlines 27 September at 615 px and 8 October at 1655.5 px, ±0.02 d. Missing are 2.3.1 and 2.6.0 second line. 2.1.0, dated "by 29 September", is drawn, while 2.3.1, dated "by 30 September", is not; it is the version of sessions 1 to 3, which Fig. 4 shades as "skill 2.3.1". |
| Suggestion | Add 2.3.1 at 30 September and "2.6.0, 2nd line" at 9 October to Fig. 5, or say in the caption, l. 359, which versions are left out and why. |
| Status | verified (ticks measured, labels read at the page image) |
| Severity | minor |
| Source | AB |

**GB-37 Fig. 5 places the first line of version 2.6.0 on 8 October, not at the middle of its date range as the caption states.**

| Field | Content |
|---|---|
| Check | P24 |
| Location | Fig. 5, dotted tick "2.6.0, first line (never installed)", p. 17; caption p. 17, l. 359 to 360; Table A2, p. 23, row 2.6.0 first line |
| Quotation | "a version dated by a range is placed at its middle"; "rules proposed from 5 October, package 7 to 8 October 2026" |
| Concern | All ticks for versions dated to the day lie at day + 0.20 (six ticks, 0.20 to 0.21 d), and 2.5.0, dated "3 to 5 October", lies at 4 October + 0.20 d, the middle of its range, as stated. The dotted tick of 2.6.0 first line measures at 1674.1 px, that is 8 October + 0.20 d (calibration as in GB-36, ±0.02 d). The middle of the package range 7 to 8 October would lie at 7 October + 0.70 d (1627.1 px), the middle of 5 to 8 October at 6 October + 0.70 d (1532.5 px). The tick lies 0.50 d or 1.50 d later, which exceeds the uncertainty; it marks the end of the range. The placement matters for the reading of the figure, because the rules of this line were proposed from 5 October, during the narrative sessions on 5 to 7 October, which sit before the tick. |
| Suggestion | Move the dotted tick in Fig. 5 to the middle of the range used for the other ranges, or change the caption, l. 359 to 360, to say that the line is placed at its packaging date. |
| Status | verified (measured) |
| Severity | minor |
| Source | AB |

**GB-38 The learner's account of three or four screen sessions differs from the records, which show one full and one partial screen session, and the manuscript calls the two a similar picture.**

| Field | Content |
|---|---|
| Check | P36 |
| Location | p. 17, l. 369 to 372; p. 14, l. 322 to 323; Fig. 6 (p. 18), row 1, column Learner's account |
| Quotation | "He used voice mode in almost all sessions and the screen in only three or four cases, because he learned mostly on the move"; "The learning records show a similar picture: 23 of the 25 sessions took place entirely in the voice call, one on screen and one partly on screen" |
| Concern | The manuscript sets the account against the records, which is good practice. The two numbers differ: 3 or 4 screen cases in the account against 1 screen and 1 partly screen session in the records. Possible resolutions are named nowhere: the two review sessions (mode not given), trial runs, which are not entered (l. 226), the uncounted first voice session, or the building chats. The Results check recorded no finding here because account and records may count different things (PP-44); rechecked at p. 17, l. 369 to 372, the manuscript does not say what the account counts, so the difference stands. It concerns the wording "a similar picture" rather than a result, which is why the severity is minor. |
| Suggestion | In Sect. 4.8 give the modes of the two review sessions and of any trial runs, and either resolve the difference with counts or state it as a difference between account and record instead of "a similar picture". |
| Status | verified (difference); assumption (resolutions) |
| Severity | minor |
| Source | SD |

#### Minor corrections

| ID | Location | Quotation | Replacement | Source |
|---|---|---|---|---|
| KK-05 | p. 13, l. 297 to 298 | "the narrative version dated 3 October, and its learning path was checked on 5 October" | "the narrative version dated 3 October; the learning path of the narrative version was checked on 5 October, that of the fact document on [date]" (the check date of the learning path on the fact document on the geological eras, Table 4 row 4, is otherwise not given, and "its" can refer to either document) | S3 |
| KK-06 | p. 15, l. 331, Fig. 4 caption; date axis without year | "Answers per session by date, for the two cases with sessions" | "Answers per session by date, 28 September to 13 October 2026, for the two cases with sessions" | AB |
| KK-07 | p. 15, l. 336 | "which the assistant updated after every session and review" | "which the assistant updated after every session and every completed review (a review broken off before any answer left it unchanged, Table 6)" | SD |
| KK-08 | p. 17, l. 359, Fig. 5 caption | "how many sessions were run per day (Table 1)" | "how many sessions were run per day (Fig. 4)" (Table 1 gives totals per case only; the counts per day are those of the bar groups in Fig. 4) | S4, AB |
| KK-09 | p. 17, l. 360 to 361, Fig. 5 caption | "were set (Sect. 3.4, 4.3, Table 6)" | "were set (Sect. 3.4, 4.3, Table 6, Table A2)" (the diamond "do not interrupt the learner" is documented in Table A2 and l. 390, not in Sect. 3.4, 4.3 or Table 6) | S4 |

#### Verification log

| ID | Check | Checked | Values | Result |
|---|---|---|---|---|
| PP-35 | P1 | Row sums of Table 5 (p. 15) and questions per session | version 6: 12 + 8 + 13 = 33 = 3 × 11; version 7: 1 + 5 + 6 = 12 = 3 × 4; narrative: 16 + 6 + 8 = 30 = 3 × 10; shares correct 36.4 %, 8.3 %, 53.3 % (not stated in the manuscript) | no finding |
| PP-36 | P1, P2 | Table 1 (p. 5) against Table 4 (p. 14) and Fig. 1 labels (page image p. 6) | questions = 3 × sessions in all five Table 1 rows (93, 33, 30, 75, 114); anchors = 2 × sessions and answers = 3 × sessions in all seven Table 4 rows; words 14,267, 3,595, 4,692, 9,682, 19,519 identical in Table 1 and Table 4; sessions run 15 = 11 + 4; mean words per session 460.2, 326.8, 469.2, 387.3, 513.7, all below the aim of about 550 (l. 205); Fig. 1 labels 31, 15 (11 + 4), 11, 10, 10, 25, 38 and review sessions 1, 0, 1, 0, 0 match Table 1 | no finding |
| PP-37 | P1, P23, P22 | Sessions of version 7 on southern Norway, l. 325 to 327, against l. 228 to 230 and the session numbers in Fig. 4 (page image p. 15) | 8 + 5 + 4 = 17 done; 31 minus 17 = 14 open; 8 credited and 5 closed in l. 229 to 230 equal the figures in l. 326; asked sessions therefore numbered 14 to 17 (8 + 5 = 13), as labelled in Fig. 4; Table 6, No. 7 names session 17 of version 7 | no finding; the numbering 14 to 17 is derivable but not needed for a result |
| PP-38 | P2, P1 | Number and mode of sessions across Abstract (p. 1, l. 16 to 17), Sect. 4.4 (l. 322 to 323), Sect. 4.6 (l. 349 to 350), Sect. 4.8 (l. 371 to 372), Fig. 6, Table 1, Fig. 5 labels | 25 sessions = 15 + 10; 23 + 1 + 1 = 25; two review sessions = 1 + 1; Fig. 5 sessions per day southern Norway 3 + 4 + 4 + 4 = 15, narrative 5 + 4 + 1 = 10; narrative sessions 5 to 7 October in l. 349 and Fig. 4 and 5; the two sessions not entirely in voice belong to southern Norway (10 narrative sessions all in voice, l. 349) | no finding |
| PP-39 | P2 | "Three of them only after exclusions" across Abstract (l. 15 to 16), Sect. 4.2 (l. 306 to 307), Table 4 last column, Fig. 1 caption and labels, Discussion (l. 384 to 385) | three paths with exclusions: narrative version 8, Geology of Germany, Volcanology stage 1; six paths, seven rows (versions 5 and 6 identical) | no finding (unit of "check run": GB-27) |
| PP-40 | P2 | Versions and rules: Table 6 (p. 16), Table A2 (p. 23), Sect. 3.6 (l. 262 to 272), Discussion (l. 389 to 391), triangles in Fig. 4 | Table 6 No. 2 rule since 2.4.0 = Table A2 2.4.0; No. 5, 7, 8 since 2.6.6 = Table A2 2.6.6; No. 6 first line 2.6.0 and 2.6.5 = Table A2; No. 9 2.6.1 = Table A2; rules against interrupting in 2.6.5 (l. 390) = Table A2; triangles 8 (session 4), 7 (sessions 9 and 17), 6 (narrative sessions 6 and 7), 8 (narrative session 10) match Table 6 No. 6 to 8 and l. 399 to 400 ("in two sessions") | no finding |
| PP-41 | P2 | Narrative version: Sect. 4.6 (l. 350) against Table 5; 144 sentences in l. 292, l. 344, l. 383 | 16, 6, 8 of 30 in both; 144 in all three places | no finding |
| PP-42 | P23 | To review balances, Sect. 4.5 (l. 338 to 341) and Discussion (l. 438 to 439) | southern Norway 24 + 11 = 35, 35 minus 2 minus 1 = 32 open; version 7 entries 11 = 5 + 6; narrative 14 = 6 + 8, 13 open; Discussion repeats 32 and 13 | no finding for version 7, narrative version and totals; version 6: GB-33 |
| PP-43 | P21 | Comparisons of absolute counts between learning paths of different size (Table 5, Sect. 4.4, 4.6, Discussion l. 441 to 444) | 33, 12 and 30 questions; shares correct 36.4 %, 8.3 %, 53.3 % | no finding: the manuscript explicitly draws no comparison between modes or paths (l. 323 to 325) or before and after version 2.5.0 (l. 442 to 444) |
| PP-44 | P2 | Screen use: learner's account (l. 369) against learning records (l. 371 to 372) | "three or four cases" against 1 + 1 = 2 sessions | no finding: two different quantities (account, which may include sessions outside the records, against record count), both labelled as such; the manuscript itself marks the account as the learner's statement (l. 375) |
| PP-45 | P2 | Word counts of southern Norway version 5 and 6, Table 4 caption and rows | 13,890 (re-measured 2.6.6) and 13,890 (version 6, 30 September) against 13,859 (original run); difference 31 words, attributed to the script | no finding; the manuscript discloses the change of script |
| PP-46 | P20 | Units "sessions run", "done", "credited", "asked" (Table 1, l. 325 to 327); "entries" and "open" (l. 338 to 341); "sessions in the learning records" against the uncounted first voice session (Table 1 caption, l. 336 to 337, Table 6 No. 2) | 15 run on southern Norway, 17 of 31 done on version 7 including 8 credited and 5 closed without being asked; first voice session of 29 September excluded | no finding: each unit is defined at its place; the exclusion of the first voice session is disclosed |
| PP-47 | P11 | Matrix of cases against reported results (building period, check run, sessions, grades, reading requests, To review, reviews) | building period reported for all four chats (l. 294 to 299); check run for all six paths (Table 4); sessions and grades for both cases with sessions (Table 5); reading requests for both (l. 316 to 318); To review for both (l. 338 to 340); reviews for both (count only) | gaps: fact document check (GB-26), runs before passing (GB-27), review details (GB-34), recut paths (GB-11), check date of the eras fact document path (KK-05); the manuscript itself limits sessions to two of five cases (l. 114, l. 464 to 465) |
| PP-48 | P3 (2, 3) | Fig. 4: segments per bar against Table 5 and l. 349 to 350 | 25 bars found (row y = 990 px of a 300 dpi render); one answer = 115 to 117 px (axis 0 to 3). Southern Norway version 6, sessions 1 to 11: correct 1, 3, 1, 1, 0, 1, 2, 2, 1, 0, 0 = 12; partially correct 2, 0, 2, 1, 0, 1, 0, 0, 2, 0, 0 = 8; not correct 0, 0, 0, 1, 3, 1, 1, 1, 0, 3, 3 = 13. Narrative version, sessions 1 to 10: correct 2, 3, 2, 2, 2, 1, 0, 1, 2, 1 = 16; partially 0, 0, 0, 0, 0, 2, 0, 1, 1, 2 = 6; not correct 1, 0, 1, 1, 1, 0, 3, 1, 0, 0 = 8. Southern Norway version 7, sessions 14 to 17: correct 0, 1, 0, 0 = 1; partially 1, 1, 1, 2 = 5; not correct 2, 1, 2, 1 = 6. Table 5: 12/8/13, 1/5/6, 16/6/8. Colours: bars #049c74, #e49c04, #d45c04 equal legend fields (deviation 0). | no finding: every count equals Table 5 |
| PP-49 | P24 | Fig. 4: dates of bars, triangles, star and shading against l. 116, 262 to 268, 295 to 299, 338, 349 to 350, 399 to 400, Table 6 | Calibration: ticks 29 September 587 px, 13 October 2052 px, 104.6 px per day; bar groups centred on the ticks: 30 September (3 bars), 1 October (4), 2 October (4), 5 October (5), 6 October (4), 7 October (1), 8 October (4). Triangles at 762.9, 889.6, 1286.1, 1308.6, 1423.8, 1561.7 px = southern Norway session 4 (no. 8, question 4.3), session 9 (no. 7), narrative sessions 6 and 7 (no. 6, two of the first seven sessions, l. 399 to 400), narrative session 10 (no. 8, question 10.3), southern Norway session 17 (no. 7); Table 6 grades "correct" for 4.3 and "partially correct" for 10.3 are compatible with the bars (session 4: one correct; session 10: two partially correct). Star at 29 September as in l. 116. Shading: #e8f1f8 over sessions 1 to 3 (legend 2.3.1 #ecf4fc, deviation 11), #d2e4f2 over sessions 4 to 11 (legend 2.4.0 #d4e4f4, deviation 4), #f6e3ee over all narrative sessions and sessions 14 to 17 (legend 2.5.0 #f4e4ec, deviation 6), as in l. 262 to 268. The caption itself discloses that the shading of sessions 4 to 11 is inferred. Line 2.4.0 at 30 September + 0.50 d, between the groups of 30 September and 1 October, consistent with "after sessions 1 to 3" (l. 264). Shades 2.3.1 and 2.4.0 differ by 41 in RGB sum, just above the limit of 40. | no finding beyond GB-32, GB-30 |
| PP-50 | P24 | Fig. 5: bars, circles and diamonds against l. 294 to 299, 318, 349, 390, Table A2, Fig. 4 | Calibration: gridlines 27 September 615 px and 8 October 1655.5 px (94.6 px per day, label 27 September starts at the gridline), ±0.02 d. Bars: southern Norway 27 September + 0.06 to 30 September + 0.93; geological eras and narrative version 2 October + 0.06 to 5 October + 0.93; Germany 2 October + 0.06 to 9 October + 0.92; volcanology 8 October + 0.07 to 9 October + 0.92, each as in l. 294 to 299. Circles (#0474b4 and #6c3c9c, equal to the case lines of Fig. 4): 30 September 3, 1 October 4, 2 October 4, 8 October 4 (sum 15), 5 October 5, 6 October 4, 7 October 1 (sum 10), equal to the bar groups of Fig. 4 and to Table 1. Diamonds at day + 0.49: 4 October (questions on relations; 2.5.0 dated 3 to 5 October), 5 October (end of excerpt; third narrative session, l. 318, on 5 October in Fig. 4), 6 October (questions shown before the call; from session 8, on 6 October in Fig. 4), 12 October (do not interrupt; 2.6.5, l. 390). Grey region from 9 October + 0.0, "no sessions after 8 October", agrees with Fig. 4. Year given in the caption. | no finding beyond GB-36, GB-37 |
| PP-51 | P29 (7) | Font size in print size, cap or ascender height in 300 dpi renders, pt = px x 72 / 300 / 0.72 | Smallest per figure: Graphical Abstract "session" x-height 20 px (cap about 9 pt); Fig. 1 "31" 20 px = 6.7 pt, legend 20 to 22 px = 6.7 to 7.3 pt, "none" x-height 16 px (about 7 pt); Fig. 2 "next session", "on request" x-height 16 to 17 px (about 7 pt); Fig. 3 "compared with the fact document" 20 to 21 px = 6.7 to 7.0 pt, "Conventions (excluded)" C 22 px = 7.3 pt; Fig. 4 session numbers 19 to 21 px = 6.3 to 7.0 pt, legend "Southern" 20 px = 6.7 pt, axis numbers 22 px = 7.3 pt, date labels 20 px = 6.7 pt, version labels 20 px = 6.7 pt; Fig. 5 date labels 21 to 22 px = 7.0 to 7.3 pt, grey note 21 to 22 px; Fig. 6 footer 21 to 22 px; Fig. 7 "in this study" 22 px, legend 21 to 22 px; Fig. 8 footer 21 px, "here of learning" 21 px = 7.0 pt. Method error up to 0.6 pt. | no finding: smallest text 6.3 pt (Fig. 4 session numbers), above 6 pt |
| PP-52 | P29 (1 to 4) | Legends, axes, abbreviations | Fig. 4: y axis "answers per session" (count), x axis dates without year (KK-06), all colours and symbols in the legend (correct, partially correct, not correct, two case lines, three shades, triangle, dashed line); star explained in the caption. Fig. 5: rows labelled, circles, diamonds and dotted tick explained in the caption. Abbreviations in figures: none undefined (version numbers, "Sect."). No subpanels a, b, c in any figure. | no finding beyond GB-30, GB-02, KK-06 |
| PP-53 | P37 | corrected values in tables | Table 4 v5 row is the 13 Oct re-measurement, labelled in caption (13,859 vs 13,890); Table 5 labelled as regraded; Fig. 4 bars equal Table 5 | no finding except GB-31 |
| PP-54 | P33 | effort and duration statements | working hours not recorded, disclosed (l. 294); building given in chat days (l. 294 to 299); session length 5 to 10 min by learner's account, disclosed (l. 190, l. 372); mean reading time from manuscript word counts at an assumed 130 to 160 words per minute: 2.0 to 4.0 min, longest example session 4.1 to 5.1 min, plausible with three questions | no finding |
| PP-55 | P9 | comparisons that the design cannot carry | modes (23/1/1) not compared (l. 322 to 324); SN v6 vs v7 not compared (l. 324 to 325); narrative vs source not compared (l. 351); before vs after 2.5.0 not compared (l. 442 to 444); motivation causal wording marked as learner's statement (l. 375, l. 471) | no finding except GB-01 and GB-43 |
| PP-56 | P31 | narrative version: "a second AI agent checked that every sentence was contained" (l. 344 to 345) | check described, outcome not quantified (number of sentences found missing or changed not given) | no finding as P31, the check is reported as performed; an outcome count would help |

### Segment 4: Discussion, conclusions, references, declarations (p. 12, 18 to 26)

#### Substantive findings

**GB-39 "Works as a safeguard" is stronger than what the manuscript shows about the links checked by rules only.**

| Field | Content |
|---|---|
| Check | P15 |
| Location | p. 18, l. 394 |
| Quotation | "The verbatim principle works as a safeguard of the kind that the tutoring studies built into their prompts (Fig. 7)." |
| Concern | The same paragraph says that the principle "does not enforce itself" (l. 398 to 401), and the Fig. 7 caption says the rules for the call "did not always hold" (l. 410 to 411). Only the link from fact document to learning path is checked (l. 401 to 402). Of the tutoring studies cited, Bastani et al. (2025) are reported with a measured accuracy of the tutor without safeguards (51 %, l. 64 to 66); for Kestin et al. (2025) the manuscript reports learning gains (l. 67 to 69). No accuracy of the assistant in the call was measured here, and Table 6, no. 6 to 8 record deviations. The verb asserts an effect that the manuscript shows only for one link of the chain. |
| Suggestion | Replace with "The verbatim principle is designed as a safeguard of the kind that the tutoring studies built into their prompts; the check script secures it only for the link from the fact document to the learning path (Fig. 7)." |
| Status | verified |
| Severity | minor |
| Source | S4 |

**GB-40 "Fall within the range given for microlearning" puts an unmeasured session length at the upper bound of the cited definitions without saying so.**

| Field | Content |
|---|---|
| Check | P15 |
| Location | p. 20, l. 418 |
| Quotation | "The sessions of five to ten minutes fall within the range given for microlearning" |
| Concern | The length of five to ten minutes is the learner's account (l. 190 to 191, l. 372) and was not measured: the manuscript states that working hours were not recorded (l. 294). The definitions cited in Sect. 2 range from "lessons of 30 seconds to five minutes" to "any content that can be taken in within less than ten minutes" (l. 80 to 81). Five minutes is the upper end of the first, and ten minutes is not "less than ten minutes". |
| Suggestion | Replace with "By the learner's account, the sessions took five to ten minutes, which lies at the upper end of the range given for microlearning". |
| Status | verified |
| Severity | minor |
| Source | S4 |

**GB-41 The Discussion introduces observations that appear nowhere in the methods or results: the rule for open questions, its single case, the empty open-question lists and the learner's description of the environment.**

| Field | Content |
|---|---|
| Check | P15 |
| Location | p. 20, l. 426 to 433; p. 20, l. 445 to 447 |
| Quotation | "This happened once, in the first session in voice mode, when the learner asked for the time span of the Mesozoic. The question is not in the learning record kept for that case today, and the open-question lists of all four learning records are empty."; "which he describes as a complete system of its own. The purpose and criteria of its parts came from him, for instance that the learning record should be portable and show progress first" |
| Concern | Sect. 3.5.3 and Table 3 name an "Open questions" part of the record but do not describe the rule (do not answer from general knowledge, record the question, return to the quiz). The single case, the empty lists of all four records, and the two limits of the rule (checked only against the excerpt; wording shortened despite quotation marks) appear for the first time in the Discussion. The case also comes from the first voice session, which went into the second record and is excluded from the data elsewhere (Table 1 caption, l. 116 to 117; l. 235 to 236). Likewise, neither Sect. 4.8 nor any other section reports the learner's statement that the environment is "a complete system of its own", or the requirements "portable" and "show progress first". A reader cannot trace these statements to a data source of Sect. 3.6. Severity is moderate: the conclusions do not depend on them, but they cannot be checked. |
| Suggestion | Describe the open-question rule in Sect. 3.5.3. Report the case in Sect. 4.5 or as a row in Table 6 (stumbling point: open question checked only against the excerpt, wording shortened), with date and record. Say that it comes from the uncounted second record. Report the learner's account of the environment in Sect. 4.8, with a translated quotation and its source. |
| Status | verified; inferred (that the case belongs to the uncounted second record, from l. 428 and the Table 1 caption) |
| Severity | moderate |
| Source | S4 |

**GB-42 The Discussion classes the questions on relations and events as elaborative interrogation, but the manuscript's own design makes them retrieval of stated content, which is practice testing.**

| Field | Content |
|---|---|
| Check | P15 |
| Location | p. 20, l. 441 to 442 |
| Quotation | "Directing the questions at relations and events comes close to what Dunlosky et al. (2013) call elaborative interrogation, a technique they rated of only moderate utility (Sect. 2)." |
| Concern | Dunlosky et al. (2013, p. 6, Table 1) define elaborative interrogation as "Generating an explanation for why an explicitly stated fact or concept is true" (p. 8: "prompting learners to generate an explanation for an explicitly stated fact"). In this skill, every expected answer is 5 to 30 words taken verbatim from the excerpt that has just been read (l. 205 to 207, l. 304 to 305; Table A3, e.g. answer 3.2). So the learner retrieves a relation the excerpt states and does not generate an explanation. That matches practice testing, "Self-testing or taking practice tests over to-be-learned material" (Dunlosky et al., 2013, p. 6), which the manuscript itself reports as rated of high utility (l. 53 to 54). The classification thus places the change under the lower-rated technique, against the manuscript's own verbatim principle. Severity is moderate rather than minor, because the classification frames the interpretation of the 2.5.0 change, not merely the wording. |
| Suggestion | Replace l. 441 to 442 with, e.g.: "Directing the questions at relations and events keeps them within practice testing, since every expected answer stands in the excerpt; it differs from elaborative interrogation, in which learners generate the explanation themselves (Dunlosky et al., 2013)." |
| Status | verified (source read: Dunlosky et al., 2013, Psychological Science in the Public Interest, 14(1), pp. 4 to 58, pp. 6 and 8) |
| Severity | moderate |
| Source | S4 |

**GB-43 The proposed retention test compares reviewed with not reviewed questions, but the manuscript's own findings show that review status depends on the first grade, on the learner's requests and on unchecked grading, and that most done sessions of version 7 were never asked.**

| Field | Content |
|---|---|
| Check | P9, P15, P27 |
| Location | p. 22, l. 473 to 475; p. 11, l. 221 to 224 and l. 229 to 230; p. 14, l. 326; p. 12, l. 256 to 257; p. 20, l. 422 to 425, l. 434 to 437 and l. 443 to 444; p. 5, l. 117 to 119; p. 15, l. 338 to 341; p. 16, Table 6, nos. 6 to 8 |
| Quotation | "Retention could be tested next by asking the questions of completed sessions again after fixed intervals and comparing questions that were taken up in review sessions with questions that were not; the list To review already records which entries were reviewed and when." |
| Concern | Naming a concrete next study follows from the open question in l. 472 and is useful. As written, it cannot isolate the effect of reviews. (a) Not asked: of the 17 done sessions of version 7 on southern Norway, 8 were credited and 5 closed without being asked (l. 229 to 230, l. 326), so 13 of 17 (76.5 %) were never asked, and asking them again would be a first test. (b) Selection by outcome: only incorrectly or partially answered questions enter To review (l. 221), so the not-reviewed group mixes questions answered correctly at first with open entries, and the groups differ in prior knowledge before any review. (c) Selection by request and age: reviews start only on request and take the oldest entries first, at most four topics (l. 222 to 224, l. 434 to 435), so review status also depends on when the learner chose to review and on the interval. (d) Grading: entry into the list and any retest rest on grades given by the language model in the call, with no second grader (l. 424 to 425), and the grades are declared process data (l. 256 to 257). (e) Deviations and versions: calls asked other questions than those of the learning path and gave hints (Table 6, nos. 6 to 8); noting the question actually asked is a rule only from 2.6.6, under which no session ran (l. 271 to 272); and the eras paths were cut anew after version 10 (l. 117 to 119), so the questions of completed sessions must be tied to a version. (f) Volume: two completed reviews of one topic each against 32 + 13 = 45 open entries on 8 October (l. 338 to 341, l. 438 to 439). (g) The same verbatim questions asked again measure recall of the item, not of the material. Severity moderate: the proposal answers no research question, but as written it would not separate the effect of review from selection and grading. |
| Suggestion | In Sect. 6, l. 473 to 475, describe a design that can answer the question: retest only questions that were actually asked, against a fixed learning-path version; among To-review entries of equal first grade and age, assign each at random to review or no review (or to early or late review); test all entries and a random sample of correctly answered questions after the same fixed intervals; have a second grader (person or separate model run) grade the retest answers blind to condition, or score them against the expected verbatim answer; log the question actually asked; where possible, use a rephrased question with the same expected answer. |
| Status | verified (a, d, e, f and the selection rules); inferred (b, c and g, consequences for the design) |
| Severity | moderate |
| Source | S4, SD |

**GB-44 The claim that the skill "works with any fact document that can be checked" goes beyond the manuscript's own conditions and check runs.**

| Field | Content |
|---|---|
| Check | P15 |
| Location | p. 22, l. 476 to 477; similar p. 1, l. 20 to 21 |
| Quotation | "the rules of the skill contain no subject content, and the skill works with any fact document that can be checked." |
| Concern | Sect. 3.4 (l. 173 to 180) gives five conditions a fact document must meet before it can be cut, and l. 168 to 170 repeats that a document must meet them. The results show that meeting them was not automatic. Three of six paths passed only after exclusions (Table 4). The geology of Germany had 577 findings in the first run and needed an opening anchor set by hand (Table 4; Table 6, no. 3 and 4). An image block was assigned to no session (Table 6, no. 9). Two proposals to the check script are still open in 2.6.6 (Table 6, no. 3 and 4). "can be checked" is a weaker condition than "meets the five conditions". The claim of no subject content is open to question too: the grading rule and its example in Table 2 ("Ma given instead of Ga") and the reading rule in l. 197 ("425 Ma") address geological time units, and Table A2 says earlier versions "were specific to southern Norway". Does the rule file of 2.6.6 contain such geoscience examples? Severity is moderate: other learners will base reuse on this sentence. |
| Suggestion | In l. 476 to 477 (and l. 20 to 21), replace with "the skill works with any fact document in Markdown that meets the five conditions of Sect. 3.4 and has been checked against its sources". State whether the rule file contains subject-specific examples. |
| Status | verified (conditions and check runs); assumption (content of the rule file, put as a question) |
| Severity | moderate |
| Source | S4, SD |

#### Minor corrections

| ID | Location | Quotation | Replacement | Source |
|---|---|---|---|---|
| KK-10 | p. 18, l. 391 | "The learning record keeps every answer with its grade" | "The learning record keeps every answer of the counted sessions with its grade (trial runs are not entered, Sect. 3.5.3)" | SD |
| KK-11 | p. 19, Fig. 7, annotation above Grade in the learning record | "graded by the language model, no second grader (Sect. 3.6)" | "graded by the language model, no second grader (Sect. 5)" (Sect. 3.6, l. 243 to 244, says only that the records are as accurate as the grading; that no second grader checked the grades stands in l. 424 to 425) | ZF |
| KK-12 | p. 26, l. 548, reference Latimier, Peyre and Ramus (2021) | "Educational Psychology Review, 33, pp. 959-987" | add the issue number after the volume, "Educational Psychology Review, 33(n), pp. 959-987", as in the other entries with issue numbers (Agarwal, Nunes and Blunt, 33(4); Mar et al., 28(3)); the issue number was not confirmed in this review | S4 |
| KK-13 | p. 26, l. 559, reference Nückles et al. (2020) | "Educational Psychology Review, 32, pp. 1089-" | add the issue number after the volume, "Educational Psychology Review, 32(n), pp. 1089-1126", as in the other entries with issue numbers; the issue number was not confirmed in this review | S4 |

#### Verification log

| ID | Check | Checked | Values | Result |
|---|---|---|---|---|
| PP-57 | P4 | Citations against the reference list in both directions; short citation against entry (year, spelling, "et al.") | 25 entries, 25 cited works, one to one. Citation counts: Mohr 2026 (5), Dunlosky et al. 2013 (3), Ji et al. 2023 (3, plus Fig. 7), Achuthan 2025, Bastani et al. 2025, Dahlstrom 2014, Kestin et al. 2025, Latimier, Peyre and Ramus 2021, Mar et al. 2021 (2 each), all others 1. Panadero 2017 and Wilson et al. 2007 also appear in Fig. 8. Author forms: one author (7 entries), two authors named (Putnam and Roediger; Terzopoulos and Satratzemi), three authors named in full (Agarwal, Cheek, Ellis, Landy, Latimier), four or more as "et al." (11). Years and spellings (Nückles, Denojean-Mairet, LaDue, Clinton-Lisell) agree. | no finding. The convention (three names in full, "et al." from four) is consistent; the checklist rule "et al. for more than two" and the journal style are a matter for the optional citation-style check. |
| PP-58 | P4 | Numbering of sections, tables, figures, appendix tables | Sections 1 to 6; 3.1 to 3.7; 3.5.1 to 3.5.3; 4.1 to 4.8; Sect. 5 without subsections. Tables 1 to 6, A1 to A3; Figures 1 to 8. Each number assigned once, none skipped, each element cited in the text. | no finding; order of first citation of the tables: PP-68 |
| PP-59 | P4 | Every reference to a section, table, figure or appendix and its target | Sect. refs: 4.1 (l. 30, 170, 359, 387, Fig. 7), 3.5.1 to 3.5.3 (l. 49), 4.7 (l. 117, 135), 4.2 (l. 117, 182, 186, 282), 3.6 (l. 151, 325, 361, 365, 377, 424, 470, Fig. 7, Fig. 8), 3.5.3 (l. 154, 237, Fig. 8), 4.6 (l. 159, 293, 383, 416), 3.4 (l. 169, 238, 361), 3.5.2 (l. 186, 329, Fig. 6), 1 (l. 190, 215), 4.5 (l. 236), 2 (l. 319, 419, 442, 449), 3.3 (l. 346), 5 (l. 351), 4.3 (l. 361, Fig. 8), 4.4 (l. 372, Fig. 6), 4.8 (l. 378, 419), 3.7 (l. 503), "Sections 3.2 and 3.5" (l. 270), "Code and data availability" (l. 489). Table and figure refs as listed by script; Table 6 nos. 6, 7, 8 in Fig. 7 match the rows. | Every target exists and contains what is referred to, except KK-08 and KK-09. |
| PP-60 | P4 | Triangle numbers in Fig. 4 against Table 6; "in two sessions" (l. 399 to 400) | Fig. 4: no. 8 at southern Norway session 4 (Table 6: question 4.3) and narrative session 10 (question 10.3); no. 7 at southern Norway sessions 9 and 17 (Table 6: session 9 of version 6, session 17 of version 7); no. 6 at narrative sessions 6 and 7 | no finding; the two narrative sessions match l. 399 to 400. |
| PP-61 | P15 | RQ1 and RQ3 answers (l. 381 to 387, 391 to 393) against results | Six paths passed, three after exclusions (Table 4: narrative, Germany, volcanology); 144 sentences (l. 344). To review: southern Norway 35 entries = 24 + 11, open 35 minus 3 = 32; narrative 14 entries = 6 + 8 partially/not correct (Table 5), 13 open; version 7: 11 entries = 5 + 6 (Table 5); two reviews of one topic each (l. 340 to 341). Sessions by version: 3 + 8 + 4 + 10 = 25 (l. 262 to 268) = 25 (Table 5: 11 + 4 + 10). Computed with Python. | no finding except GB-26 for "verified". Disclosed: self-experiment, no control condition, no claim on retention (l. 20, 440), grades as process data (l. 256 to 257). |
| PP-62 | P15 | Limitation counts and other statements in the Discussion | "five limitations" (l. 462): single learner who is developer, short period, no control condition, own account, two of five cases = 5. "Three limits" (l. 243): records by assistant, self-analyses, transcript after compaction = 3. Narrative version (l. 412 to 417) against Sect. 4.6: no session on the source document, comparison declared impossible. Grading (l. 422 to 425) against Sect. 3.6. Spacing (l. 434 to 440): 32 and 13 open entries, two reviews, a broken-off review (Table 6, no. 5). | no finding |
| PP-63 | P15 | Each proposal in Sect. 6, held against the manuscript's own findings | (1) Retention test (l. 473 to 475) against l. 221, 224, 229 to 230, 256 to 257, 271 to 272, 326, 422 to 425, 443 to 444, Table 6 no. 6 to 8: GB-43. (2) "works with any fact document that can be checked" (l. 476 to 477) against Sect. 3.4, Table 4, Table 6 no. 3, 4, 9: GB-44. (3) Other subjects (biology, history, law, l. 478 to 480) against the 2.5.0 rule of asking about relations and events instead of numbers, dates and names (l. 40 to 41): the manuscript itself marks it as untested, so no finding. (4) Requirements for other learners (code execution, voice mode, provider processing, l. 481 to 482) against l. 137 to 139: consistent. (5) Open question whether the approach serves other learners (l. 472 to 473) against the limitation in l. 462: consistent. | no further finding beyond GB-43, GB-44 |
| PP-64 | P15 | Frameworks and core terms from the introduction and RQs in Discussion and conclusions | Retrieval practice and spacing (l. 434 to 440), hallucination types (l. 397), tutoring studies (l. 394 to 396), narrative (l. 412 to 417), microlearning and mobile learning (l. 418 to 421), self-regulated learning (l. 449 to 454), grading (l. 422 to 425) are taken up. Not taken up: listening literature, learning journals, retrieval-augmented generation. "Memorize" stands for the record, not retention (l. 49 to 50), as in l. 391 to 393. | GB-07 |
| PP-65 | P16 | Language and setting of Sect. 3.7, 5, 6, declarations and references on the page images (pp. 12, 18 to 26) | No grammatical errors found. The line breaks in the URL l. 495 to 496 ("Listen-" / "Answer-Memorize") and in the DOIs l. 530 to 531, 548 to 549, 554 to 555 break at hyphens that belong to the identifiers; the compound "self-" / "directed" (l. 452 to 453) is correctly hyphenated. The reference list is uniform in "Available at:", italic journal titles, hyphen in page ranges, and access dates only for URLs without a DOI (Clinton-Lisell 2023, Wilson et al. 2007), except for the issue numbers in KK-12 and KK-13. The wide word spacing in justified entries (e.g. l. 521, 527, 538, 568) is typesetting, not an error. | no finding beyond KK-04, KK-12 and KK-13 |
| PP-66 | P3, P29 | Figs. 6, 7, 8 against l. 252 to 256, 365 to 375, 394 to 403, 422 to 425, 445 to 452, Table 6 | Fig. 6: three criteria match l. 253 to 256; "23 of 25 sessions entirely in the voice call" as in l. 371; "often two sessions on a 30-minute drive" as in l. 372 to 373; "five to ten minutes" as in l. 372. Fig. 7: solid green (check script), dotted yellow (document project), dashed orange (rules) explained in the legend and the caption; references Table 6 nos. 6, 7, 8 and question 10.3 agree with Table 6. Fig. 8: line styles explained in the footer and the caption; Wilson et al. (2007) and Panadero (2017) as in l. 449 to 452. The caption of Fig. 6 itself discloses that its right-hand column is not a measured outcome. | no finding |
| PP-67 | P9 step 4 | outlook proposals | retention test checked against selection, comparison and grading (GB-43); other learners and other subjects named as untested, no design proposed; Table 6 rule proposals checked under PP-63 | no finding beyond GB-43 |
| PP-68 | P2, P3, P5 | Hints outside the checklists that no instance had raised as a finding, rechecked at the page images | (1) Table A3, question 3.1, "according to the two sources cited", against l. 196: in voice mode a source that is the subject of a sentence becomes 'a source', and expected answer 3.1 itself names 'a second source', so the question stays answerable; (2) Table 1 caption, "both of its learning paths", against l. 343: the narrative path derives from the eras document, consistent with l. 157 to 159; (3) Table A1, 'weiter' as next and as end of a pause: both effects are documented in the table; (4) Fig. 4 shows no review sessions: its caption and Table 5 concern learning sessions; (5) Fig. 7 names three of the five checks of Fig. 3: a shortened label, no contradiction; (6) second learning record referred to Sect. 4.7 in Table 1 and to Sect. 4.5 in l. 236: both sections mention it; (7) Kortemeyer (2024) only in Sect. 5: no defect; (8) number 2.6.0 assigned twice: explained in the Table A2 caption (l. 490 to 491); (9) order of first citation of the tables (Table 4 in the Fig. 1 caption before Tables 2 and 3, Table 6 before Table 5, Table A2 before Table A1): a matter for the journal requirements, not run; (10) Fig. 7 label "no second grader (Sect. 3.6)": confirmed | no finding except KK-11 |

## Optional checks

| Area | What it needs | Responsible | Run |
|---|---|---|---|
| DOI resolution | one retrieval per reference entry with a DOI | `science-quellenapparat-pruefung` | no |
| Citation style | the name of the style | `science-zitierstil-harvard-ctr` or the style rules of the journal | no |
| AI statement against publisher policy | the AI policy of the target publisher | this review, on request | no |
| Relation to the authors' prior work | the prior work of the author, as files or DOIs | this review, on request | no |
| Journal requirements | the author guidelines of the target journal | this review, on request | no |
| Subject-matter accuracy | access to the sources of the checked statements and a selection of sections | `science-faktenbeleg-pruefung`, `geo-frage-belegbasiert-klaeren` | no |

## Limits of this review

- Checked version: Listen_Answer_Memorize_Copernicus.pdf, 26 pages, SHA-256 9065d593cbc95029707b6936346f193d31cfedcd4e11382fbbd43629428595aa.
- Sources not readable: the full text of Bastani et al. (2025), so the figure of 51 % in l. 65 is unverified (PP-05); Putnam and Roediger (2013) (PP-16); the publisher records for the issue numbers of Latimier, Peyre and Ramus (2021) and Nückles et al. (2020) (KK-12, KK-13). The repository named in the data availability statement was not opened (GB-21).
- Literature not checked against its source: Ellis, Adams and Bochner (2011) in l. 251 to 252, Wilson et al. (2007) in l. 450 to 452, and the statement in l. 394 to 396 that Kestin et al. (2025) achieved accuracy by supplying solutions; Kortemeyer (2024) was checked only in passing.
- Findings with status assumption: 8 of 44 (GB-01, GB-02, GB-11, GB-15, GB-17, GB-20, GB-38, GB-44), in each for a part claim on the authors' environment or intent, put as a question; in GB-02 the intended meaning of the arrow is itself the question.
- Optional checks run: 0 of 6.
- Dropped instances: none.
- Discarded findings: 0. All 50 findings and 15 minor corrections of the six instances had their mandatory fields, and none was discarded on rechecking at the manuscript. Merging joined 50 findings into 44 and 15 minor corrections into 13: two minor corrections went into findings (GB-12, GB-44), two were joined into one (KK-08), and one minor correction was added from a hint (KK-11, source ZF).
- Merging: `formatpruefung.py --paare` listed 117 pairs on the instance findings; 9 were merged, 0 were resolved as a contradiction and 108 were kept separate because they concern a different subject at the same place. On this report the list holds 85 pairs, all kept separate after rechecking. Three contradictions between a finding and the verification log of another instance were rechecked at the manuscript and decided in the concern (GB-30, GB-33, GB-38).
- Line numbers were confirmed at the printed margin numbers of the page images; rows of tables without their own line number are given as table, row and column.
- Manuscript and review were produced with the same language model family (see Note in the header).
