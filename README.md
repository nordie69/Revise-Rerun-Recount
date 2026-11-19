# Revise, Rerun, Recount: data and code

Data, skill packages and scripts for the paper "Revise, Rerun, Recount: Measuring whether revising AI review skills helps them find the issues human referees raise in geoscience preprints" (Stefan Mohr, independent researcher, Hamburg; ORCID 0000-0003-4657-3501).

![Graphical abstract: an AI review and human referees assess one preprint, shared issues count as hits; revising the AI's review instructions gave no gain (29.1 % vs 28.7 % of substantive referee issues hit); further comparisons: separate agents hit more issues; new rules about halved the sum of the seven targeted error classes, but wrong counts rose.](figures/ga.png)

The study ran three review skills for an AI assistant in four conditions on four EGUsphere preprints, three times each (48 reviews), and measured the reviews against the objections in the public referee reports. Most files are in German, the working language of the study; the paper is in English.

## Contents

| Folder | Content | In the paper |
|---|---|---|
| `skills/` | the skill packages (`.skill`, zip archives) of the four version sets: eleven distinct packages, science-review-studiendesign 1.2.0 appears in two sets | Table 2, Appendix A, Table A1 |
| `protocol/final_with_amendments/` | study protocol as frozen on 17 October 2026 with its three amendments, checksum file, note on freezing, origin of the rules; the amendments were entered after the first run had finished and before any review was matched or rated (the times come from the working log of the study, which is not part of this repository) | Sect. 3.6, Appendix B |
| `protocol/first_frozen_version_superseded/` | first frozen version of the same day, before the first run and before the amendments, its checksum file and note on freezing, with the file comparison of the packages D against B | Sect. 3.3, 3.6 |
| `study/delivery_main_study/` | run register, the 48 reviews with their check reports, the access logs of the verification (`laeufe/`), reference issues and their confirmation (`soll/`, `soll_vorstudie/`), grouping and rating (`einstufung/`), rule proposals of R and R2 (`rq3/`), assessment of AI assistance in referee reports (`spinoff_ki_herkunft/`), recount of the pilot (`vorstudie/`), measures (`auswertung/`), scripts (`tools/`) | Sects. 3.3 to 3.8, 4.1 to 4.6, Appendix B |
| `study/delivery_supplement_1/` | study handbook, analysis of the rise of F3, note on the line numbers of two manuscripts, scripts | Sects. 4.4, 4.6 |
| `study/delivery_supplement_2/` | the four reviews of pilot round V4 with their check reports, the only input of R and R2 (`erprobung/`); the second extraction of the reference issues with its instructions and access logs and its comparison with the first (`hauptstudie/soll/<M>/extraktion2/`, `hauptstudie/soll/<M>/abgleich/`); the acceptance criteria AK-01 to AK-14 of V4, the check of the access logs of R and R2 and the search for wording of the AI peer-review service (`hauptstudie/freigabe_e42/`); scripts (`hauptstudie/tools/`); the instructions and access logs of R and R2 are copies of those in `delivery_main_study/` | Sects. 3.4, 3.7, Table B1 |
| `recalculation/` | independent recalculation of every measure from the raw data (report, scripts, results) and the list of corrections to the delivery | the measures in Sect. 4; where the delivery and the recalculation differ in rounding or in K9, the paper follows the recalculation |
| `recalculation/supplement_8-1/` | recalculation of the values added in later versions of the paper, among them Appendices C and D with Table C2, the waves and early runs, all assignments of reviews to repetitions and the power of the effect rule (`gutachten3.py`; scripts and results); the scripts read `study/delivery_main_study/hauptstudie/` and `recalculation/ergebnis.json` under the absolute paths of the working copy | Sects. 3.3, 3.5, 4.2 to 4.5, 5.1, Appendices C and D |
| `figures/` | scripts and output (PNG, PDF, SVG) of Figs. 1 to 5; script and output (PNG, SVG) of the graphical abstract (`ga`) | Figs. 1 to 5, graphical abstract |

Figure files: `fig_ablauf_skill` is Fig. 1, `fig01_methods` Fig. 2, `fig02_pilot` Fig. 3, `fig03_k1_conditions` Fig. 4, `fig04_error_classes` Fig. 5.

Skill packages by use:

| Folder in `skills/` | Use |
|---|---|
| `A_and_pilot_V1_V2_1.0.0/` | condition A; pilot V1 and V2 |
| `pilot_V3_1.1.0/` | pilot V3 |
| `B_C_and_pilot_V4_1.3.0_1.2.0_1.2.0/` | conditions B and C; pilot V4 |
| `D_1.4.0_1.3.0_1.2.0/` | condition D (science-review-studiendesign unchanged from B) |

## What is not included

- The four preprints of the test material and their referee reports. They are public on the EGUsphere discussion pages (https://egusphere.copernicus.org/preprints/2025/egusphere-2025-4506/, -4695/, -4733/, -5046/). The same holds for egusphere-2025-2248 of the pilot.
- The individual verdicts of the human rater on the blinded sample of 60 findings and on the finding groups without an AI majority. The repository gives the counts (57 of 60, per condition) and the final verdict of every finding group; where a final verdict was not set by the AI majority, its source is given as "set under the protocol, not by AI majority". Three files of the delivery and two files of the recalculation differ from their originals for this reason; they are listed in `REDACTIONS.md`, the three delivery files with the checksums of the originals. The final verdicts themselves are part of the data, so for the finding groups that were not decided by the AI majority the final verdict is the one set by the human rater.
- The objections extracted from the reports of an AI peer-review service on the author's two earlier papers, with their verbatim quotations (pilot study, `soll_vorstudie/LAM` and `soll_vorstudie/TCD`). The lists of these reference issues with identifier, kind and confirmation are included; their wording is not.
- The instructions and access logs of the agents that wrote the 48 reviews, which were not kept; the access logs of the runs were checked after each run (Sect. 4.6 of the paper). Not archived are also the access logs of the matching and of the counters, and the instructions and access logs of the first extraction and of the confirmation of the reference issues and of the assessment of AI assistance in referee reports. Table B1 of the paper states for each kind of agent what is included.
- The 11 reviews of pilot rounds V1 to V3 with their check reports, because the pilot is not compared with the main study. The matching of all pilot reviews is included, and the four reviews of V4 with their check reports are in `study/delivery_supplement_2/`. These four were searched for wording of the AI peer-review service: nine passages of six to ten words that they share with it and that the reviewed manuscripts do not contain are left unchanged and listed by location, without their wording, in `hauptstudie/freigabe_e42/`.
- The material of the author's timed trial rating, because it contains the author's own ratings; the protocol states its result.
- A later version of the main skill that was built after the study.

Because the rating sheet and the pilot extraction files are withheld (second and third item), the scripts in `recalculation/` and `study/.../tools/` that read the rating sheet of the human rater or the extraction files of the pilot do not run to the end on this repository; all other steps can be recomputed from the files given here.

## Checksums

`SHA256SUMS.txt` lists the SHA-256 checksum of every other file in this repository. The checksum files inside `study/` are those of the delivery and refer to the originals; they differ for the redacted and withheld files.

## Licence

Skill packages, scripts and the author's own data and texts in this repository are released under the MIT License (`LICENSE`). Quotations from public referee reports and preprints remain under their own licence, see `NOTICE.md`.
