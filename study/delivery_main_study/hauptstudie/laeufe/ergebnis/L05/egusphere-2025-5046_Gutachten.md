# Review report: Quantifying Southern Hemisphere dust sources during the Last Glacial-Interglacial Transition using rare earth elements in the EPICA Dome C ice core

| Field | Value |
|---|---|
| Manuscript | Boxho, S., Vanderstraeten, A., Mattielli, N., Laruelle, G. G., Bory, A., Gabrielli, P., Bonneville, S. (2025), Quantifying Southern Hemisphere dust sources during the Last Glacial-Interglacial Transition using rare earth elements in the EPICA Dome C ice core, EGUsphere preprint egusphere-2025-5046, https://doi.org/10.5194/egusphere-2025-5046 |
| Version reviewed | egusphere-2025-5046.pdf, 29 pages, SHA-256 f598b53d01e375844cfb549eb05b9a3407bb30cae553e603c125d5f14886c722; supplement egusphere-2025-5046-supplement.pdf, 22 pages, SHA-256 759cfa14195948f5772d3d6d696081932424f4296e51c812415527ed3b108ea6 |
| Date | 2026-10-18 |
| Language | English |
| Check instances | Segments 1 to 4, figures, study design |
| Note | The six check instances ran as separate agents, each without the context of the others; merging, overall assessment and format check were done afterwards in one further agent. Line numbers are the printed margin numbers of the page images. Supplement locations are given as "Supp. p.". |

## Summary

The manuscript is a modelling study on an existing data set. It applies the DEPOT algorithm, a non-negative least-squares unmixing (MATLAB lsqnonneg) with a Monte Carlo propagation of 2000 draws per sample, to the published rare earth element (REE) patterns of the EPICA Dome C (EDC) ice core (Gabrielli et al., 2010): 294 patterns, 279 fitted after removing incomplete ones, 241 retained with R ≥ 0.67, spanning 33.7 to 2.9 kyr BP on the EDC3 chronology. The end-member library holds 217 REE patterns from seven potential source areas (PSA: Patagonia, Central Western Argentina, Puna-Altiplano, Southern Africa, Australia, New Zealand, Antarctica). Patagonia supplies about 65 to 75 % of the dust in MIS3, LGM and HS1; after about 14.5 kyr BP the shares of low-latitude sources rise, and in the Holocene Patagonia averages 49 % and Australia 23 % (Table S5). The REE result is checked against Sr-Nd isotopes by a forward mixing calculation (Eq. 3 and 4) and compared with the EDML record of the same group (Vanderstraeten et al., 2023); the shift is attributed to Patagonian shelf submergence and drainage reorganisation at about 14.5 kyr BP.

## Strengths

1. Every per-sample result is published (Table S1, 241 rows with R), and the period means of Table S5 follow from it exactly (48 EDC values recomputed within 0.1 percentage point); Figure 1, the LGM panel of Figure 3 and Figure 4 were measured and reproduce these tables. A reader can therefore check nearly every number in the text against the tables, which is how most of the deviations listed below were found (PP-14, PP-20, PP-21, PP-26).
2. The source library is published as Table S2 with location, grain size and reference per pattern, and the Sr-Nd end-members as Table S3; region counts match the text for five of seven PSA, and Eq. 3 and 4 can be rerun from the supplement. This makes the input side of the unmixing open to inspection, although the inputs on the ice-core side are missing (PP-08, PP-23, GB-10).
3. The sample balance is stated and consistent (294, 279, 241; mean R 0.852; four samples in the 21.7 to 27.3 kyr gap), and the manuscript discloses its main limits itself: the sampling gap, the exclusion of low-concentration samples younger than 14 kyr, and the tentative status of ACR and YD. This lets the reader see where the record is thin (PP-07, PP-05).
4. For the glacial periods the forward isotope calculation lands near the two measured EDC LGM values (computed about 0.7083 and εNd minus 2.6 against 0.7086 to 0.7088 and minus 1.66 to minus 2.46), so the REE-based glacial apportionment is consistent with independent Sr-Nd data; the literature search found no earlier continuous quantitative provenance record for EDC, which supports the qualified priority claim (PP-23, PP-04).

## Weaknesses

1. The main result is stated more strongly than the data show. The shift is expressed as greater inputs although only shares are reported while total flux falls sharply, the announced absolute PSA fluxes are missing, the sea-level mechanism is said to be demonstrated although only a timing coincidence is shown (and the New Zealand decline precedes it), and the conclusion explains the EDC and EDML differences differently from Section 4.4. Suggestion: report PSA fluxes or speak of relative contributions throughout, and phrase the mechanism as consistent with the data (GB-03, GB-20, GB-54, GB-55).
2. Signal and noise are not separated. The Monte Carlo spread is computed but not reported, fit quality drops in the Holocene exactly where variability rises, the R threshold does not correspond to the stated significance level, and the library may favour Australia by its size while the Antarctic end-members appear not to be normalised. Suggestion: report per-sample and per-period uncertainty, add a synthetic noise test and a library-size sensitivity test, and restate the threshold (GB-19, GB-43, GB-21, GB-13, GB-16).
3. The tests behind aims 2 to 4 do not compare like with like. The Holocene isotope validation uses Taylor Glacier and Berkner Island data instead of EDC, the EDC and EDML comparison mixes time windows and method versions and uses EDML values that differ from the published record, the agreement with the Potrok Aike record is not quantified, and the Altiplano onset tied to paleolake Coipasa contradicts Table S1. Suggestion: compare on matching windows, sites and method versions and quantify each agreement (GB-37, GB-50, GB-08, GB-45, GB-29).
4. Reproducibility and traceability suffer from several moderate issues: the ice-core inputs, correction factors and code are not available despite the data statement, more than half of the source patterns cite works missing from the reference list, counts and duplicates in Table S2 do not match the text, figure labels and legends exchange periods, and several numbers in Sections 3 and 4 differ from the tables. Suggestion: deposit inputs and code, complete the references, and reconcile labels and numbers with Tables S1 and S5 (GB-10, GB-22, GB-15, GB-23, GB-31, GB-58, GB-41, GB-53).

## Findings by segment

### Segment 1: Title, abstract, introduction (p. 1 to 3)

#### Substantive findings

**GB-01 The priority claims are made without an account of the literature search, and the claim in the abstract is not qualified.**

| Field | Content |
|---|---|
| Check | P28 |
| Location | p. 1, l. 17 to 20; p. 3, l. 74 to 76; p. 7, l. 220 to 221; p. 12, l. 403 to 404; p. 14, l. 472 to 473 |
| Quotation | "Using a statistical unmixing algorithm on 241 samples, we quantify for the first-time contributions from key Southern Hemisphere dust sources." |
| Concern | No database, search terms or date are given for any of these statements. Searches of the reviewer (see PP-04) found no earlier REE pattern-fitting apportionment for an Antarctic ice core and no earlier continuous quantitative provenance record for EDC, so the qualified claims in l. 74 to 76, l. 220 and l. 472 hold as far as checked. The abstract claim is unqualified and does not hold as worded: Southern Hemisphere contributions to East Antarctic dust were already quantified by Vanderstraeten et al. (2023) for EDML with the same algorithm (l. 74 to 76) and by Coppo et al. (2022) from Sr-Nd isotopes (l. 277 to 279), both cited in the manuscript. |
| Suggestion | In l. 19 to 20 write, for example, "we provide the first continuous quantification at EDC of contributions from key Southern Hemisphere dust sources", and add one sentence in the introduction on how novelty was established, or write "to our knowledge". |
| Status | verified (contradiction with l. 74 to 76 and l. 277 to 279; search queries in the verification log) |
| Severity | moderate |
| Source | S1 |

**GB-02 The end points of the record are given with three different values.**

| Field | Content |
|---|---|
| Check | P2 |
| Location | p. 1, l. 18; p. 3, l. 90 to 91; p. 6, l. 182; p. 9, l. 303 to 304; Supp. p. 11 and 15 (Table S1, first and last row) |
| Quotation | "from 33.7 to 2.9 kyr BP"; "during the LGIT from 33.6 kyr to 2.8 kyr BP"; "(from 14.5 kyr BP until 2.7 kyr BP)" |
| Concern | Table S1 runs from 2852 to 33699 yr, which rounds to 2.9 and 33.7 kyr, as in l. 18 and l. 182. The values 33.6 (l. 90) and 2.7 (l. 304) match neither the table nor rounding; 2.8 kyr (l. 91) is the Holocene boundary of l. 187, not the youngest sample. |
| Suggestion | In l. 90 to 91 and l. 304 write 33.7 and 2.9 kyr BP, as in the abstract. |
| Status | verified |
| Severity | minor |
| Source | S3, SD, S4 |

**GB-03 The shift towards low-latitude sources is stated as greater inputs, but it is a change in shares while the total flux falls sharply.**

| Field | Content |
|---|---|
| Check | P21 |
| Location | p. 1, l. 23 to 24; p. 10, l. 315 to 318; p. 2, l. 63; Table S5 (Supp. p. 22) |
| Quotation | "After ~14.5 kyr BP, the dust assemblage shifted toward greater inputs from low-latitude" |
| Concern | All period comparisons use percentages of a total that changes greatly; the manuscript itself gives interglacial fluxes up to 25 times lower than LGM fluxes (l. 63) and shows the decline in Figure S2. With that ratio, the Holocene AUS flux would be 23.1 / 25 = 0.92 in LGM-equivalent units against 10.2 in the LGM, a drop of about 91 % although the AUS share more than doubles. Section 4.4 speaks correctly of a "relative increase" (l. 463). The abstract and l. 315 to 316 ("increased contributions") can be read as an absolute increase that the data do not show. The factor 25 is a literature value, not measured for these samples (see also GB-06), so the size of the drop is approximate. The finding is major because it concerns how the main result is stated. |
| Suggestion | In the abstract (l. 23) and l. 315 to 316 write "greater relative contributions", and report per-PSA fluxes (GB-20) so that relative and absolute changes can be told apart. |
| Status | verified (wording); inferred (flux estimate computed with the ratio from l. 63) |
| Severity | major |
| Source | S3 |

**GB-04 The pCO2 range credited to Lambert et al. (2015, 2021) is wider than either source reports.**

| Field | Content |
|---|---|
| Check | P13 |
| Location | p. 2, l. 40 to 42 |
| Quotation | "Enhanced iron delivery by atmospheric dust during glacial periods are modelled to have lowered the atmospheric pCO2 by ~20 to 40 ppmv" |
| Concern | The qualitative summary of iron fertilization is fair, but the upper bound does not come from the cited works. Lambert et al. (2015, Geophys. Res. Lett. 42, 6014 to 6023, https://doi.org/10.1002/2015GL064250) state that iron fertilization reduced LGM CO2 by 20 ppm (less than 10 ppm on centennial plus about 10 ppm on millennial timescales). Lambert et al. (2021, Earth Planet. Sci. Lett. 554, 116675, https://doi.org/10.1016/j.epsl.2020.116675) give 12 to 29 ppmv in the results and 8.9 to 33.1 ppmv across six dust reconstructions in Table 2. The highest value in either source is 33.1 ppmv, 6.9 ppmv below the 40 ppmv quoted. |
| Suggestion | In l. 41 replace "~20 to 40 ppmv" by the range the sources give, for example "~10 to 30 ppmv (about 20 ppmv in most estimates)", or cite the source of the 40 ppmv bound. |
| Status | verified (both sources read in repository copies) |
| Severity | moderate |
| Source | S1 |

**GB-05 Engelbrecht et al. (2019) is cited for the role of the Southern Hemisphere westerlies, but it is a regional downscaling of LGM climate over southern Africa.**

| Field | Content |
|---|---|
| Check | P13 |
| Location | p. 2, l. 51 to 52 |
| Quotation | "which play a crucial role in atmospheric and oceanic circulation (Engelbrecht et al., 2019)." |
| Concern | The abstract of Engelbrecht et al. (2019, Quat. Sci. Rev. 226, 105879) describes the first dynamic downscaling of LGM climate over southern Africa with the main result that southern Africa was generally wetter; it does not address the hemispheric role of the westerlies. The statement itself is uncontroversial, but the citation does not support it. |
| Suggestion | In l. 52 cite a work on the role of the Southern Hemisphere westerlies, or move Engelbrecht et al. (2019) to the discussion of southern African sources. |
| Status | inferred (only the abstract was readable) |
| Severity | minor |
| Source | S1 |

**GB-06 The factor of 25 between LGM and interglacial dust fluxes is credited to Delmonte et al. (2008, 2017), but it comes from Lambert et al. (2008) and is a typical ratio, not an upper limit.**

| Field | Content |
|---|---|
| Check | P13 |
| Location | p. 2, l. 62 to 63 |
| Quotation | "dust fluxes are up to 25 times lower than LGM fluxes (e.g. Delmonte et al., 2008; Delmonte et al., 2017)" |
| Concern | The abstracts of Delmonte et al. (2008, 2017) do not give a glacial to interglacial flux ratio. Lambert et al. (2008, Nature 452, 616 to 619), already in the reference list (l. 676 to 678), report an approximately 25-fold increase in glacial dust flux over all eight glacial periods, and Gabrielli et al. (2010) cite the ratio from there. An approximate factor over all glacials is not a maximum, so "up to" changes the meaning. |
| Suggestion | In l. 63 write "about 25 times lower than glacial fluxes (Lambert et al., 2008)" and keep the Delmonte citations only for what they show. |
| Status | verified for Lambert et al. (2008) and Gabrielli et al. (2010); inferred for the absence of the factor in Delmonte et al. (2008, 2017), abstracts only |
| Severity | minor |
| Source | S1 |

**GB-07 Three earlier EDC studies that already show the glacial to Holocene change in dust provenance and its timing are not cited.**

| Field | Content |
|---|---|
| Check | P14 |
| Location | p. 3, l. 72 to 74 and l. 91 to 93; p. 1, l. 16 to 19 |
| Quotation | "Previous studies using REE patterns in Antarctic ice cores (e.g., Gabrielli et al., 2010; Wegner et al., 2012) achieved multi-decadal resolution but could not fully resolve dust provenance." |
| Concern | The introduction places the study against Sr-Nd work and two REE studies. Contribution in one sentence: a continuous quantitative REE-based provenance record at EDC from 33.7 to 2.9 kyr BP with a shift from high- to low-latitude sources at about 14.5 kyr BP. Three EDC studies anticipate or limit this and are not in the reference list (checked p. 16 to 22): (1) Siggaard-Andersen, M.-L. et al. (2007) Soluble and insoluble lithium dust in the EPICA DomeC ice core: implications for changes of the East Antarctic dust provenance during the recent glacial-interglacial transition. Earth Planet. Sci. Lett. 258, 32 to 43, https://doi.org/10.1016/j.epsl.2007.03.013, which reports a change of the major source areas with the Holocene dust type appearing after about 16 ka BP; (2) Marino, F. et al. (2008) Defining the geochemical composition of the EPICA Dome C ice core dust during the last glacial-interglacial cycle. Geochem. Geophys. Geosyst. 9, Q10018, https://doi.org/10.1029/2008GC002023, which finds uniform glacial dust consistent with southern South America and a likely Australian contribution in warm times; (3) Vallelonga, P. et al. (2010) Lead isotopic compositions in the EPICA Dome C ice core and Southern Hemisphere Potential Source Areas. Quat. Sci. Rev. 29, 247 to 255, https://doi.org/10.1016/j.quascirev.2009.06.019, which states that volcanic Pb prevents evaluating Australia as an interglacial source, a limit relevant to the Pb-based support in l. 365 to 367. Only Vallelonga et al. (2002, Law Dome) and Marino et al. (2009) are listed. The stated gap (l. 92, "no consensus") remains, but the reader cannot see that direction and timing were known before and that the new contribution is the quantification. |
| Suggestion | Cite works 1 and 2 in the introduction (after l. 74 and in l. 92 to 93) and work 3 in Section 4.3 next to De Deckker et al. (2010); state the new contribution as the quantification of what these studies show qualitatively. |
| Status | verified (abstracts and bibliographic records read; reference list checked p. 16 to 22) |
| Severity | moderate |
| Source | S1 |

**GB-08 The introduction misstates the EDML result for Australia, and the EDML values in Table S5 differ from the published record.**

| Field | Content |
|---|---|
| Check | P13 |
| Location | p. 3, l. 77 to 81; Supp. p. 22 (Table S5, block EDML, columns PAT, SAF, AUS, NZ); p. 9, l. 287 to 288; p. 13, l. 417 to 424; p. 14, l. 480 to 481; Figure 4 |
| Quotation | "a sudden drop in Patagonian contribution (below 50% on average) was evidenced while the dust contributions from low-latitude PSA, particularly from Australia and Southern Africa, sharply increased (Vanderstraeten et al., 2023)." |
| Concern | The Patagonian part reproduces the abstract of Vanderstraeten et al. (2023, Sci. Total Environ. 881, 163450): about 68 % before 14.5 kyr BP and below 50 % afterwards. The low-latitude part does not: the same abstract gives Australia 14 to 15 % before and 13 to 21 % after 14.5 kyr BP (midpoints plus 2.5 percentage points); only Southern Africa rises sharply, from about 9 % to 21 to 23 %. Second, the EDML values used for the comparison in this manuscript do not match the published record: PAT 71.6 to 73.7 % in HS1 and LGM (published about 68 %) and 58.4 to 62.7 % in ACR, YD and Early Holocene (published below 50 %); SAF 8.2 to 12.4 % after 14.5 kyr BP (published 21 to 23 %); AUS 9.4 to 9.7 % before 14.5 kyr BP (published 14 to 15 %). Read against Table S5, the claim of l. 79 to 80 does not hold for EDML at all. A likely explanation is a recalculation of EDML with 13 instead of 14 REE (l. 144 to 145) and the present library; the manuscript does not say so. Aim (4) (l. 95 to 98) and the statement that the results confirm the earlier study (l. 480 to 481) rest on this comparison, hence major. |
| Suggestion | In l. 80 to 81 replace "particularly from Australia and Southern Africa, sharply increased" by "particularly from Southern Africa (to 21 to 23 %), increased". Question to the authors: was EDML recalculated for this study? If so, say so in Section 2 and the caption of Table S5, give published and recalculated values side by side, and adjust l. 288 and l. 480 to 481. |
| Status | verified for the published values (abstract) and for Table S5 (page image); assumption for the cause, hence put as a question |
| Severity | major |
| Source | S1 |

#### Minor corrections

| Kennung | Location | Quotation | Replacement | Source |
|---|---|---|---|---|
| KK-01 | p. 1, l. 15 | "Dust deposits in ice cores provides a valuable archive" | "Dust deposits in ice cores provide a valuable archive" | S1 |
| KK-02 | p. 1, l. 19 | "we quantify for the first-time contributions" | "we quantify for the first time contributions" | S1 |
| KK-03 | p. 1, l. 20 | "During the Marine isotope 3 (MIS3)" | "During Marine Isotope Stage 3 (MIS3)" | S1, S2 |
| KK-04 | p. 2, l. 39 | "High Nutrients Low Chlorophyll (HNLC)" | "High-Nutrient, Low-Chlorophyll (HNLC)" | S1 |
| KK-05 | p. 2, l. 40 to 41 | "during glacial periods are modelled" | "during glacial periods is modelled" | S1 |
| KK-06 | p. 2, l. 48 to 49 | "(Qu, 2016; Shi et al., 2009, Shi et al. 2011, Shi et al. 2015)" | "(Qu, 2016; Shi et al., 2009, 2011, 2015)" | S1 |
| KK-07 | p. 2, l. 62 | "high altitude site such as EDC where dust fluxes is low" | "high-altitude sites such as EDC where dust fluxes are low" | S1 |
| KK-08 | p. 3, l. 70 to 71 | "contain a lot more discriminative information than REE ratio" | "contain much more discriminative information than REE ratios" | S1 |
| KK-09 | p. 3, l. 88 | "Here, we applied our ‘DEPOT’ model - to the REE pattern dataset measured - in the EPICA Dome C" | "Here, we apply our DEPOT model to the REE pattern dataset measured in the EPICA Dome C" | S1 |
| KK-10 | p. 3, l. 90 | "in the Indian Ocean sector of the East Antarctica" | "in the Indian Ocean sector of East Antarctica" | S1 |

#### Verification log

| Kennung | Check | Checked | Values | Result |
|---|---|---|---|---|
| PP-01 | P13 | p. 2, l. 34 to 36 and l. 44 to 46 against Lambert et al. (2008) | Abstract: sources and lifetime of dust are the main factors controlling the high glacial dust input; manuscript: deposition rates influenced by location of sources and residence time | no finding |
| PP-02 | P13 | p. 2, l. 37 to 40 against Martínez-García et al. (2014) | Abstract: dust-borne iron fertilization caused the ice age CO2 reduction; dust flux from a Subantarctic Atlantic sediment core, loosely but not distortingly attributed to "studies on these ice cores" | no finding |
| PP-03 | P13 | p. 3, l. 72 to 74 and p. 4, l. 108 to 110 against Gabrielli et al. (2010) and Wegner et al. (2012) | Gabrielli: 294 samples, about 2.9 to 33.7 kyr BP, about 60 yr (Holocene) and 140 yr (glacial) spacing, tentative provenance; Wegner: decadal to centennial resolution, 26.6 to 7.5 kyr BP | no finding |
| PP-04 | P14, P28 | positioning and priority claims (l. 19, 74 to 76, 220, 403, 472) | Six WebSearch queries on REE unmixing, Sr-Nd provenance at Dome C, Bayesian unmixing, Taylor Glacier, Pb isotopes at EDC, REE mixing models; candidates already listed (Vanderstraeten 2023, Gabrielli 2010, Wegner 2012, Gili 2022, Delmonte 2004 and 2020, Koffman 2021, Krätschmer 2022, Kok 2021); Aarons 2017 and Neff 2021 concern other sites; three unlisted EDC studies found | findings GB-07 and GB-01; no counterexample to the qualified claims |

### Segment 2: Materials and methods (p. 3 to 5)

#### Substantive findings

**GB-09 The 217 source samples are called DS in the text but PSAs in Tables S1 and S2, while PSA otherwise denotes the seven regions.**

| Field | Content |
|---|---|
| Check | P38 |
| Location | p. 4, l. 105, l. 127 to 133, l. 137; p. 5, l. 143 to 144; Supp. p. 11 (caption Table S1); Supp. p. 16 (caption Table S2) |
| Quotation | "Median of PSA's contribution (in percents) based on th DEPOT model results - using 217 PSAs and 279"; "Table S2: Table of PSAs database" |
| Concern | The method section defines PSA for the seven regions and DS for the 217 patterns (l. 105, l. 158 to 162). Table S1 uses "217 PSAs" for the patterns, so one word names two objects, and a reader of the supplement cannot tell whether 217 regions or 217 samples were used. The same caption gives "279 DIC" although the table lists the 241 samples that passed the R threshold. |
| Suggestion | Supp. p. 11: "based on the DEPOT model results, using 217 dust sources (DS) and the 241 DIC samples with R ≥ 0.67"; Supp. p. 16: "Table S2: Database of dust-source (DS) REE patterns, grouped by PSA". |
| Status | verified (page images) |
| Severity | minor |
| Source | S2, S3, SD |

**GB-10 The ice-core inputs, correction factors, exclusion lists and code needed to rebuild DEPOT are not available, although the data statement says all data are present.**

| Field | Content |
|---|---|
| Check | P12, P8, P18 |
| Location | p. 4, l. 107 to 124; p. 5, l. 139 to 140, l. 153 to 165; p. 6, l. 174 to 175; p. 16, l. 494 to 496 |
| Quotation | "All data needed to evaluate the conclusions in the paper are present in the paper and/or the Supplementary Materials. Additional data related to the paper may be requested from the authors." |
| Concern | The supplement gives the outputs per sample (Table S1) and the source end-members (Table S2), which is a good basis. Missing are: (1) the 294 measured REE patterns with depth and age, or a repository identifier (Gabrielli et al., 2010 is cited only as a paper); (2) the lists of the 15 incomplete and the 38 excluded samples with their R; (3) the 13 correction factors cf_i and their variability used in the Monte Carlo draws; (4) the per-element uncertainties (only the range 2 % to 10 % is given); (5) the DEPOT implementation and the Monte Carlo wrapper. Without (1), (3) and (4), Table S1 cannot be recomputed even with the code. The statement covers these items only by "may be requested", without naming them or giving a reason, although no personal data are involved; its absolute claim is therefore not met. Two PANGAEA REE data sets for EDC exist (doi:10.1594/PANGAEA.696109 and 10.1594/PANGAEA.696111); whether either is the one used cannot be decided from the manuscript. |
| Suggestion | Add to the supplement the EDC REE patterns (raw, UCC-normalised and cf_i-corrected) with sample identifiers, a flag and reason for each excluded sample, and a table of cf_i and relative uncertainty per element, or cite the repository DOI in l. 108 and l. 494; deposit the DEPOT and Monte Carlo scripts in the version used (13 REE, 217 DS) with a persistent identifier and revise l. 494 to 496. |
| Status | verified (absence in supplement p. 1 to 22 and in the statement); assumption (identity of the PANGAEA data sets), hence put as a question |
| Severity | moderate |
| Source | S2, SD |

**GB-11 The spacing between samples in Table S1 falls outside the stated 60 to 140 years, and the 15 excluded samples cannot account for the gaps.**

| Field | Content |
|---|---|
| Check | P23 |
| Location | p. 4, l. 110 to 114; Table S1 (Supp. p. 11 to 15), column Time |
| Quotation | "with an average temporal resolution of approximately 100 years, ranging from 60 to 140 years between adjacent samples." |
| Concern | No sample older than 14 kyr was removed by the R filter (l. 175), so the 112 older samples should keep the original spacing apart from the 15 incomplete ones. Outside the stated 21.7 to 27.3 kyr gap there are 29 gaps longer than 140 years in that part (for example 20257 to 20731 yr, 474 yr), which would need at least 33 additional samples, more than 15. In the Holocene many spacings are below 60 years (2852 to 2888 yr, 36 yr), and four ages appear twice. Mean spacing of the retained record 128.5 yr, median 98 yr; overall range 0 to 2280 yr. Possible explanations: the range describes typical spacing, refers to depth rather than EDC3 age, or more samples were removed than reported. The resolution underpins the high-resolution claim. |
| Suggestion | In l. 110 to 113 give minimum, median and maximum spacing of the 241 retained samples, say where the 15 excluded samples lie, and explain the repeated ages. |
| Status | inferred (computed from Table S1) |
| Severity | moderate |
| Source | S3 |

**GB-12 Period boundaries are cited from the AICC2012 chronology while the sample ages follow EDC3.**

| Field | Content |
|---|---|
| Check | P7, P35 |
| Location | p. 4, l. 111; p. 6, l. 184 to 188 |
| Quotation | "The age model follows the EDC3 chronology (Parrenin et al., 2007)." |
| Concern | The period limits (14.7, 12.9, 11.7 kyr BP) are cited from Veres et al. (2013), the AICC2012 chronology (reference list p. 21, l. 817 to 820). If the two age scales differ in the deglaciation, samples near the boundaries fall into the wrong period, which matters for ACR and YD with 8 and 9 samples. The size of the offset is not given; this is asked. |
| Suggestion | State in Section 2 on which chronology the period limits are applied, and transfer either the sample ages to AICC2012 or the boundaries to EDC3. |
| Status | verified (citations); assumption (that an offset changes the assignment), hence put as a question |
| Severity | moderate |
| Source | SD |

**GB-13 The source library is unbalanced (Australia 107 of 217 patterns, mixed grain sizes); could the dominance of Australia and of the Darling Basin partly follow from library size?**

| Field | Content |
|---|---|
| Check | P9, P27 |
| Location | p. 4, l. 126 to 133; p. 11, l. 366 to 367; Table S2 (Supp. p. 16 to 19) |
| Quotation | "our model identifies the Darling sub-basin as the dominant source region during the Holocene" |
| Concern | Counted from Table S2: PAT 39, CWA 5, PAP 14, SAF 23, AUS 107, NZ 25, ANT 4; Australia holds 49.3 % of the library, 101 Australian patterns come from one study and 45 from the Darling Basin; sample types mix below 5 µm, below 63 µm, below 90 µm, bulk loess, topsoil and aeolian dust. In a non-negative fit over 217 columns, a region with more candidate patterns may absorb noisy patterns more easily, which would enlarge Australia exactly where noise is high (Holocene, GB-43). The manuscript neither tests nor discusses this. The mechanism is an assumption from general knowledge of least-squares fitting and is therefore asked. It would change the Holocene result, hence major. |
| Suggestion | In Section 2 add a sensitivity test with equal library size per region (repeated random subsets) or one mean pattern per region and grain-size class, and report in Section 3 whether the Australian and Darling Basin shares persist. |
| Status | verified (counts); assumption (library-size effect), hence put as a question |
| Severity | major |
| Source | SD |

**GB-14 The Puna-Altiplano and Central Western Argentina sub-units carry different names in text, Tables S1 to S3 and Figure 2, and the PAP end-member assignment in Eq. 3 and 4 is not stated.**

| Field | Content |
|---|---|
| Check | P38 |
| Location | p. 4, l. 129 to 130; p. 8, l. 245 to 250; p. 11, l. 355 to 358; Supp. p. 11 (Table S1 header); Supp. p. 16 (Table S2 block heading); Supp. p. 20 (Table S3); Figure 2 (p. 26) |
| Quotation | "the Puna-Altiplano Plateau (PAP; 14 DS from North and South Puna and Southern Altiplano)"; "Puna AltiPlano (PAP)"; "Southern Central Western Argentina (SCWA)" |
| Concern | Table S1 has columns "Puna" and "Altiplano", Table S2 the heading "Puna AltiPlano (PAP)", Table S3 the end-members "S-Puna", "S-Altiplano" and "SCWA", Figure 2 a domain "Southern Central Western Argentina". Table S2 holds SCWA1 to SCWA3, MCWA and NCWA, so it is not said whether SCWA in Table S3 stands for the whole CWA end-member. Eq. 3 and 4 do not say how PAP enters: recomputed with Table S3 and the Table S5 Holocene means, assigning all PAP to S-Puna gives 0.7094 and εNd minus 4.13, all to S-Altiplano 0.7104 and minus 5.33, so the assignment moves the Holocene result by 0.0010 and 1.2 εNd units. |
| Suggestion | Use one set of names (PAP with North Puna, South Puna, South Altiplano; CWA with North, Middle, South) in text, Tables S1 to S3 and Figure 2; in l. 245 to 250 state how PAP is split into S-Puna and S-Altiplano (presumably by the Table S1 columns) and whether SCWA represents CWA. |
| Status | verified (spellings on page images); inferred (recomputed isotope values); assumption (meaning of SCWA), hence put as a question |
| Severity | minor |
| Source | S2, ZF |

**GB-15 The source counts for Australia and Antarctica differ between text, Table S2 and Figure S1.**

| Field | Content |
|---|---|
| Check | P12, P3 |
| Location | p. 4, l. 131 to 133; Supp. p. 17 to 19 (Table S2, blocks AUS and ANT); Supp. p. 2 (Figure S1, panel ANT) |
| Quotation | "Australia (AUS; 106 DS, predominantly from the central and southeastern regions), New Zealand (NZ; 25 DS, from the South Island), and Antarctica (ANT; 5" |
| Concern | Rows counted in Table S2 (script, confirmed on page images): PAT 39, CWA 5, PAP 14, SAF 23, AUS 107, NZ 25, ANT 4, total 217; the text gives AUS 106 and ANT 5, also 217. Figure S1 shows five Antarctic markers; its PAT panel shows 22 markers for 22 distinct PAT coordinates, so markers stand for sites. Two resolutions: (a) the text is right and one Antarctic pattern is missing from Table S2, so the published library is not the one used; (b) Table S2 is right and the text miscounts. Under (a) the matrix of Eq. 2 cannot be rebuilt; Antarctica reaches 33.1 % in one sample (Table S1, 3654 yr). |
| Suggestion | Reconcile l. 131 to 133, Table S2 and Figure S1; if a fifth Antarctic pattern was used, add it to Table S2 with reference, and say in the caption of Figure S1 that one marker can stand for several samples. |
| Status | verified (counts on page images and by script); inferred (which resolution applies) |
| Severity | moderate |
| Source | S2, AB, SD |

**GB-16 The Antarctic end-members in Table S2 do not appear UCC-normalised, contrary to the stated rule; does this cause the absent Antarctic contribution?**

| Field | Content |
|---|---|
| Check | P5, P27 |
| Location | p. 4, l. 133 to 135; Supp. p. 19 (Table S2, rows ELB, Expcove, Miers, Vict); p. 10, l. 329 to 334 |
| Quotation | "all PSA REE patterns were normalized to the UCC composition of Rudnick and Gao (2003) and Gd values were removed" |
| Concern | Table S2 is headed "REE normalised on the Upper Continental Crust". For the other 213 patterns La/Lu lies between 0.26 and 2.48; for the four Antarctic patterns it is 35.8 to 129.3, with Lu 0.008 to 0.010 against values near 1 elsewhere (page image Supp. p. 19, for example ELB La 0,720323, Lu 0,008290). Dividing these values by UCC gives near-flat patterns at 0.01 to 0.05, which suggests the table holds unnormalised values for Antarctica. If the fit used them, Antarctic patterns could hardly match any normalised ice-core pattern, and the conclusion of l. 329 to 334 that Antarctica contributes nothing (against 24 % in Coppo et al., 2022) would follow from the input. Table S1 row 3654 yr (ANT 33.1 %) shows that the model can select Antarctica, so the question is open; it concerns a result, hence major. |
| Suggestion | State in Section 2 whether the Antarctic patterns were normalised in the fit, correct Table S2, and if the fit used unnormalised values, rerun it and revise l. 324 to 334. |
| Status | verified (table values on page image); inferred (normalisation test); assumption (values used unnormalised in the fit), hence put as a question |
| Severity | major |
| Source | SD |

**GB-17 How do medians of separate PSA distributions sum to 100 %, and is the fit closed to 100 %?**

| Field | Content |
|---|---|
| Check | P26, P8 |
| Location | p. 5, l. 137 to 139, l. 164 to 165; Supp. p. 13 (Table S1, first row 10511) |
| Quotation | "The median of each PSA-specific PDF was taken as the best estimate of its contribution to the DIC sample’s total dust load." |
| Concern | The text states non-negativity but no sum-to-one constraint. Medians of separate marginal distributions do not in general add up to 100 %; in Table S1, 240 of 241 rows sum to 100 ± 0.15 %, one (first row 10511 yr) to 0.0 + 0.0 + 3.1 + 6.7 + 49.2 + 29.5 + 5.0 + 0.0 = 93.5 %. Either a normalisation step after the medians is applied and not described, or the values are not marginal medians. |
| Suggestion | Describe in Section 2 whether contributions are constrained or rescaled to 100 % per simulation and per sample, and correct or explain the row at 10511 yr. |
| Status | verified (row sums on Table S1); assumption (cause), hence put as a question |
| Severity | moderate |
| Source | SD |

**GB-18 Result-relevant settings of the computing environment are missing.**

| Field | Content |
|---|---|
| Check | P35 |
| Location | p. 5, l. 140, l. 157 to 162 |
| Quotation | "This was implemented using the lsqnonneg function in MATLAB." |
| Concern | No MATLAB version, solver tolerance, random seed or generator is given, and no rule for drawing normal values of cf_i and Dust_i that cannot be negative (truncation or rejection). In a 217-column non-negative fit such settings can decide which columns receive non-zero weight; whether they change the results here is asked, not claimed. |
| Suggestion | Give in Section 2 the MATLAB version, lsqnonneg options, seed and the handling of negative draws. |
| Status | verified (absence); assumption (effect on results), hence put as a question |
| Severity | moderate |
| Source | SD |

**GB-19 The Monte Carlo uncertainty is computed but not reported, so no shift or core difference can be judged against it.**

| Field | Content |
|---|---|
| Check | P11, P31 |
| Location | p. 5, l. 153 to 165; p. 7, l. 233 to 235; p. 13, l. 420 to 424; Supp. p. 11 (Table S1 title); Supp. p. 22 (Table S5) |
| Quotation | "To evaluate the impact of uncertainties in REE concentrations in DIC samples and their associated correction factors (cfi) on our model outputs, we performed Monte Carlo (MC) simulations" |
| Concern | A PDF from 2000 simulations is formed for every sample, but Table S1 gives only medians and Table S5 period means without spread or sample counts. The text interprets differences of 4 to 14 percentage points between periods and cores and speaks of "significantly increased" contributions (l. 235) without a test; that 5000 simulations "does not significantly affect the results" (l. 163 to 164) has no numbers. Without spread, single-sample peaks (SAF 94.7 % at 12227 yr, Altiplano 100 % at 8629 yr) and core differences cannot be judged against model uncertainty. The finding concerns the robustness of the main comparisons, hence major. |
| Suggestion | Report per sample the 16th and 84th (or 5th and 95th) percentiles of each PSA in Table S1, per period mean, standard error or bootstrap interval and n in Table S5 and Figure 4, test the period and core differences used in Sections 4.1 and 4.4, and give the 2000 against 5000 comparison as numbers. |
| Status | verified |
| Severity | major |
| Source | S3, SD |

**GB-20 Absolute PSA fluxes are announced as an output, but no flux values are reported.**

| Field | Content |
|---|---|
| Check | P12, P11, P31, P3 |
| Location | p. 5, l. 165 to 167; p. 6, l. 183 to 184; Figure 1 (p. 24); Supp. p. 3 to 4 (Figure S2); Supp. p. 11 to 15 (Table S1); Supp. p. 22 (Table S5) |
| Quotation | "to convert PSA contributions into absolute dust fluxes (Figure S2)"; "Figure 1 and Table S1 summarize the relative contributions (in % of total deposition and flux) from each PSA" |
| Concern | Table S1, Table S5 and all y axes of Figure 1 ("Total Contribution (%)") give percentages only; Figure S2 shows total nssCa2+ flux, δ18O and deuterium excess, not PSA fluxes. The derived data set announced in the method section (PSA fluxes per sample, conversion from nssCa2+ to dust, interpolation to sample ages) is neither published nor covered by the data statement. The fluxes would also address the iron fertilisation motivation of l. 43 to 52 and the distinction between relative and absolute change (GB-03). |
| Suggestion | Add PSA fluxes per sample to Table S1 and per period to Table S5 (or a flux panel in Figure 1), with the nssCa2+ value and conversion factor used; otherwise remove l. 165 to 167 and write "(in % of total deposition)" in l. 183 to 184. |
| Status | verified (page images) |
| Severity | moderate |
| Source | S2, S3, SD, AB |

**GB-21 The R threshold of 0.67 does not correspond to p below 0.01 with the stated degrees of freedom, and three retained samples fall below it.**

| Field | Content |
|---|---|
| Check | P1, P5, P25, P23 |
| Location | p. 5, l. 170 to 172; p. 6, l. 174 to 175; Supp. p. 11 (Table S1, rows 2888 and 3267); Supp. p. 13 (first row 10511), column R |
| Quotation | "We determined that R ≥ 0.67 corresponds to a statistically significant match (p < 0.01, two-tailed test, degrees of freedom = 10)" |
| Concern | Critical r for p = 0.01 two-tailed (Student t, scipy): 0.708 at df = 10 and 0.684 at df = 11, which 13 REE give (n minus 2); r = 0.67 corresponds to p = 0.017 (df 10) or 0.012 (df 11), significant at p below 0.05 but not 0.01. Table S1 also retains three rows with R = 0,66 (2888, 3267, first 10511), below the threshold. Two resolutions: R values truncated in print (then 241 holds), or the three were kept by mistake (then 238 retained and 41 excluded). With the threshold at 0.708, 221 samples would remain, all additional exclusions younger than 14 kyr; Holocene means change little (PAT 49.0 to 48.4 %, AUS 23.1 to 23.6 %), so the period means are robust, but the significance statement and the selection are not. |
| Suggestion | In l. 170 to 172 give the correct df and the significance level 0.67 actually corresponds to, or raise the threshold; print R with three decimals in Table S1 and explain or remove the rows with R = 0,66; report the sensitivity of Table S5 to the threshold. |
| Status | inferred (critical values and counts computed); verified (wording and Table S1 values on page images) |
| Severity | moderate |
| Source | S3, SD |

**GB-22 For 117 of the 217 source patterns, and for the ice-core isotope data of Figure 2, the original source is not in the reference list.**

| Field | Content |
|---|---|
| Check | P12, P4 |
| Location | Supp. p. 17 to 19 (Table S2, column Reference); Supp. p. 21 (Table S4, column Reference); reference list p. 16 to 22 |
| Quotation | "Marx and Kamber, 2010"; "McGowan et al ., 2005"; "Diaz et al. , 2018"; "[Aarons et al. (2017)]"; "[Bory et al. (2010)]" |
| Concern | Table S2 is the published form of the end-member data, which is welcome. Its reference column points to works absent from the reference list (checked for Marx, McGowan, Diaz, Aarons, Bory): Marx and Kamber 2010 (101 AUS rows), Marx et al. 2005 (4 AUS and 6 NZ rows), McGowan et al. 2005 (2 AUS rows), Diaz et al. 2018 (4 ANT rows), together 117 of 217 patterns (54 %); the supplement has no reference list. The same holds for Aarons et al. (2017) and Bory et al. (2010) in Table S4, which supply all Holocene measurements of Figure 2. A reader cannot check whether normalisation and Gd removal were applied to the original values. |
| Suggestion | Add full entries for Marx et al. (2005), Marx and Kamber (2010), McGowan et al. (2005), Diaz et al. (2018), Aarons et al. (2017) and Bory et al. (2010) to the reference list or a supplement reference list, and state in the caption of Table S2 that values are recalculated from these sources. |
| Status | verified (absence in the reference list and page images); inferred (share 54 %) |
| Severity | moderate |
| Source | S2, S4 |

**GB-23 Two pairs of rows in Table S2 are the same sample under two names and basins (Darling and Murray), so the library holds 215 distinct patterns.**

| Field | Content |
|---|---|
| Check | P38 |
| Location | Supp. p. 17 (rows Darling26, Darling29); Supp. p. 18 (rows Murray29, Murray24); p. 11, l. 366 |
| Quotation | "Darling26"; "Murray29"; "Darling29"; "DR 3"; "Murray24"; "Murray 10" |
| Concern | A script compared all 13 normalised values of the 217 rows: exactly two pairs are identical in all values and coordinates (Darling26 and Murray29 at 34° 3'0.00"S 142° 3'10.80"E, La 1,150581; Darling29 and Murray24 at 34°28'48.00"S 142°49'48.00"E, La 1,031323), confirmed in the text layer and page images. Each pair is one object with two names and two basin labels. In Eq. 2 the two columns of each pair are identical, so their combined share can go to either name; at PSA level (both AUS) this has no effect, but the Darling statement in l. 366 depends on it. |
| Suggestion | Resolve the duplicates in Table S2, correct the count in l. 127 and l. 143 to 146 if a row is removed, and state for l. 366 whether these patterns contributed to the Darling result. |
| Status | verified (identity by script and on page images); inferred (effect on the sub-basin attribution) |
| Severity | moderate |
| Source | S2 |

**GB-24 Two "this study" samples in Table S2 carry the location Etosha Pan although they lie elsewhere, and all six "this study" rows give western longitudes.**

| Field | Content |
|---|---|
| Check | P38 |
| Location | Supp. p. 17 (Table S2, rows EtoshaL1 to EtoshaL4, SuksesL, Sossusvlei, columns Location, Lattitude, Longitude) |
| Quotation | "Sossusvlei"; "Etosha Pan"; "24,76 S"; "15,29 W" |
| Concern | These six rows are the only patterns published for the first time, so Table S2 is their only record. Sossusvlei (24.76 S) lies about 5.8 degrees south of the Etosha rows of Li et al. (2020) (18.9 to 19.0 S), and SuksesL (21.059 S) also carries "Etosha Pan". All six rows give longitudes in W, while the other SAF rows and Namibia are E. The text groups SAF sources into Makgadikgadi, Etosha and the Namibian coast (l. 379 to 381, l. 386 to 387), so with the label Sossusvlei would be counted under Etosha. |
| Suggestion | Correct the Location entries of Sossusvlei and SuksesL and the hemisphere of the longitudes, and state in l. 386 to 398 under which system each "this study" sample was aggregated. |
| Status | verified (page image Supp. p. 17); inferred (latitude difference); assumption (that aggregation used the Location column) |
| Severity | minor |
| Source | S2 |

#### Minor corrections

| Kennung | Location | Quotation | Replacement | Source |
|---|---|---|---|---|
| KK-11 | p. 3, l. 101 | "dust source contributions to ice core camples" | "dust source contributions to ice core samples" | ZF |
| KK-12 | p. 4, l. 127 | "(Figure S1, and Table S1)" | "(Figure S1 and Table S2)" | S4, AB, SD |
| KK-13 | p. 4, l. 128 | "subdivised into Patagonia" | "subdivided into Patagonia" | ZF |
| KK-14 | p. 5, l. 147 | "a given dust ice core (DICₗₐ₋ₗᵤ) sample" | "a given DIC sample (DIC_La to DIC_Lu)" | S2 |
| KK-15 | p. 5, l. 159 | "by minimizing Eq. (1)" | "by minimizing Eq. (2)" | S4, SD |
| KK-16 | Supp. p. 16 (Table S2, column header) | "Lattitude" | "Latitude" | ZF |
| KK-17 | Supp. p. 17 (Table S2, row Darling12, column Longitude) | "138°17'6.00"E" | check against the source; probably "144°17'6.00"E" as in Darling11 at the same latitude (138° E lies outside the Darling Basin) | ZF |

#### Verification log

| Kennung | Check | Checked | Values | Result |
|---|---|---|---|---|
| PP-05 | design sketch | questions, study type, data sources, time axis, environment, stated principles and disclosed limits (p. 3 to 6, p. 16, supplement) | Four aims l. 91 to 98; modelling on a re-used data set; 211 of 217 patterns from literature, 6 "this study"; EDC3 ages, period limits after Veres et al. (2013); lsqnonneg without version; disclosed: gap 21.7 to 27.3 kyr, low-concentration samples younger than 14 kyr, 13 instead of 14 REE, ACR and YD tentative, isotope domains cut in Figure 2 | basis for the design findings; no separate finding |
| PP-06 | P12 | every data source named in Section 2 and its coverage by the statement and supplement | EDC REE patterns, exclusion lists, cf_i, per-element uncertainties, code: missing (GB-10); library: Table S2 (GB-15, GB-22); MC medians and R: Table S1, 241 rows; nssCa2+, δ18O, d-excess: external with references (Figure S2); PSA fluxes: missing (GB-20); EDML: Table S5; isotopes: Tables S3, S4; statement without link, so no reachability check needed | findings as listed |
| PP-07 | P1, P23, P38 | sample balance and names of the ice-core sample set | 294 minus 15 = 279; 279 minus 38 = 241; 241 rows in Table S1; 241 / 279 = 86.4 % (text 86 %); mean R 0.8523 (text 0.852); ages 2852 to 33699 yr; four samples in the gap (22150, 23104, 25384, 25640); DEPOT named as algorithm, model and unmixing model for the same method | no finding beyond GB-21 and GB-11 |
| PP-08 | P38, P1 | region counts and names of the library against text and Figure S1 | PAT 39 (Gili 2017: 25, Gaiero 2004: 14), CWA 5, PAP 14 (South Puna 7, North Puna 2, South Altiplano 5), SAF 23 (Li 2020: 6, this study: 6, Vanderstraeten 2023: 11), NZ 25 (Marx 2005: 6, Koffman 2021: 19) equal to l. 128 to 132; text sum 39 + 5 + 14 + 23 + 106 + 25 + 5 = 217; Figure S1 panel labels match the block headings | mismatch only AUS and ANT (GB-15) |
| PP-09 | P30 | reported errors, corrections or reprocessing in text, captions and supplement | none found | no finding |
| PP-10 | P33 | effort statements | "tradeoff between computation cost and representativity" (l. 162 to 163), not used as a result or limitation | no finding |
| PP-11 | P34 | counted sets against published lists | 294, 279, 241 samples; 217 patterns; all 241 contributions in Table S1, all 217 patterns in Table S2 | no finding beyond GB-26 |
| PP-12 | P19 | provenance class of the data | 211 of 217 patterns from literature (97.2 %); all contributions model-generated; isotope end-members are means; 33 of 35 ice-core isotope values not from EDC | no separate finding; the naming "measured in EDC" is GB-37 |
| PP-13 | P25 | information flow between steps | flux conversion needs nssCa2+ at sample ages (Fischer et al., 2007); forward isotope calculation needs [Sr], [Nd] and isotope means per PSA (Table S3; no ANT, CWA only as SCWA) | no further finding |

### Segment 3: Results (p. 6 to 7; Figures 1 and 3; Tables S1 and S5)

#### Substantive findings

**GB-25 The exclusion rate is given for the whole record only, although all excluded samples are younger than 14 kyr.**

| Field | Content |
|---|---|
| Check | P20 |
| Location | p. 6, l. 174 to 179; Supp. p. 22 (Table S5) |
| Quotation | "These excluded samples are all younger than 14 kyr BP and have very low REE concentrations near the detection limit." |
| Concern | The 86 % (241 / 279) is a rate over the whole record. Table S1 keeps 129 samples younger than 14 kyr, so 38 of 167 (22.8 %) were excluded there, against none before 14 kyr. The Holocene, YD and ACR means of Table S5 therefore rest on a selection of the samples with higher concentrations, and how the 38 split between these periods is not given. |
| Suggestion | In Section 3 state the exclusion rate per period and add the number of retained samples per period to Table S5. |
| Status | inferred (computed from Table S1 and l. 174 to 179) |
| Severity | moderate |
| Source | S3 |

**GB-26 The three Valdes Peninsula patterns highlighted in the results are not identified, and Table S2 names only one pattern at that location.**

| Field | Content |
|---|---|
| Check | P34 |
| Location | p. 6, l. 196 to 198; Supp. p. 16 (Table S2, row PataGi5) |
| Quotation | "our algorithm highlights three specific REE patterns collected in or near the Valdes Peninsula. The samples represent aeolian materials" |
| Concern | Table S2 lists one row with location "Peninsula de Valdes" (PataGi5, Gili et al., 2017), and its sample type is topsoil below 5 µm, not aeolian material. The other two patterns are not named, so the reader cannot find the three end-members that dominate the Patagonian contribution. |
| Suggestion | Name the three patterns in l. 196 (sample names of Table S2) and correct the sample type or the description. |
| Status | verified (text and Table S2); inferred (that no other row qualifies as "near") |
| Severity | minor |
| Source | ZF |

**GB-27 The ranking of secondary sources over the whole record places PAP above NZ, but no averaging basis supports that order.**

| Field | Content |
|---|---|
| Check | P21 |
| Location | p. 6, l. 201 to 202; Table S1; Table S5 |
| Quotation | "other Southern Hemisphere PSAs contribute to EDC dust deposition with sources from: AUS, SAF, PAP and NZ, in decreasing order of importance." |
| Concern | Mean over all 241 samples: AUS 16.5, SAF 9.2, NZ 7.9, PAP 6.9; time-weighted mean: AUS 12.9, NZ 9.4, SAF 9.0, PAP 5.0; mean of the six period means of Table S5: AUS 13.2, SAF 9.0, NZ 7.7, PAP 4.8. NZ ranks above PAP on all three bases. The sample mean is weighted towards the Holocene (116 of 241 samples). |
| Suggestion | In l. 201 to 202 state the basis and correct the order (AUS, SAF, NZ, PAP for sample means), or restrict the sentence to the Holocene, where AUS 23.1, PAP 11.0, SAF 10.7, NZ 5.9 holds. |
| Status | inferred (computed from Tables S1 and S5) |
| Severity | minor |
| Source | S3 |

**GB-28 The SAF minimum of "~2%" between 9.5 and 12 kyr BP matches neither Table S1 nor Figure 1, and overlaps with the YD value.**

| Field | Content |
|---|---|
| Check | P20, P3, P36 |
| Location | p. 6, l. 207 to p. 7, l. 208; Figure 1 (p. 24, panel SAF); Table S1; Table S5 |
| Quotation | "Although SAF input drops to minimal levels (~2%) between 9.5 and 12 kyr BP, it rebounds in the subsequent Holocene, averaging ~11%." |
| Concern | Over the 33 samples between 9.5 and 12 kyr BP, SAF has mean 4.3 % and median 0.3 % (15 samples at 0.0, maximum 49.2 %); the smoothed curve of Figure 1 measures a mean of 6.1 % in that window. The window includes the youngest part of the YD, for which the text gives 15 %; that YD mean (14.6, 9 samples) is driven by one sample (12227 yr, 94.7 %), without which it is (14.6 × 9 minus 94.7) / 8 = 4.6. "~11%" equals the full Holocene mean (10.7), which includes the minimum window; the 85 samples between 2.8 and 9.5 kyr average 13.0 %. |
| Suggestion | In l. 207 to 208 state the statistic and sample count for each value, note that the YD mean rests on one sample, and give the mean for 2.8 to 9.5 kyr if "subsequent Holocene" is meant. |
| Status | inferred (computed from Tables S1 and S5); verified (12227 yr value and Figure 1 measurement on page images) |
| Severity | minor |
| Source | S3, AB, SD |

**GB-29 The statements on South Altiplano peaks, South Puna levels and the Altiplano onset contradict Table S1, which weakens the link to the desiccation of paleolake Coipasa.**

| Field | Content |
|---|---|
| Check | P2, P3, P15, P24, P6, P36 |
| Location | p. 7, l. 212 to 215; p. 11, l. 355 to 360; Supp. p. 11 to 13 (Table S1, columns Puna and Altiplano, rows 3465, 5967, 6166, 8629, 9957, 11117, 11228, both rows 12841); Figure 1 (panel PAP); Supp. p. 6 (Figure S3, panel Altiplano) |
| Quotation | "contributing over 90% at 11.2, 10, 8.6, 6, and 3.5 kyr BP. In contrast, contributions of South Puna remained consistently below 20% during this interval (Figure 1)"; "the Southern Altiplano begins contributing dust only after approximately 11.2 kyr BP, a timing that coincides with the final desiccation of paleolake Coipasa" |
| Concern | The sub-regional split in Table S1 is a useful addition, but: (a) Altiplano exceeds 90 % in two samples only, 8629 yr (100.0) and 11228 yr (97.0); near the other ages the values are 75.7 (9957), 58.5 and 58.0 (5967, 6166) and 62.7 (3465); the raw PAP curve of Figure 1 shows the same peaks (measured 97.1, 99.0, 74.9, 57.8, 60.0). (b) South Puna is at or above 20 % in eight Holocene samples (3503: 25.0; 4387: 20.6; 5657: 23.4; 5850: 29.1; 6775: 20.7; 7833: 25.6; 10205: 25.7; 11117: 20.2). (c) Altiplano is non-zero before 11.2 kyr BP in both YD rows at 12841 yr (16.6 and 12.8 %, R 0.69 and 0.77), and Figure S3 shows a raw Altiplano peak at 11.86 kyr. The YD PAP signal (Puna 1.3 %, Altiplano 3.3 % as means of nine rows) therefore comes mostly from the Altiplano, not from South Puna as l. 212 says. Figure 1 shows only PAP combined, so it cannot support the sub-regional statements. The onset date is the basis of the Coipasa link under aim (3), hence major. |
| Suggestion | In l. 212 to 215 write "over 90% at 11.2 and 8.6 kyr BP and over 55% at 10, 6 and 3.5 kyr BP", replace "consistently below 20%" by "mostly below 20% (maximum 29%)", and cite Table S1 and Figure S3 instead of Figure 1; in l. 357 to 360 give the first Altiplano contribution (12.8 kyr BP, YD) and either explain why these values are disregarded or revise the comparison with the lake record. |
| Status | verified (Table S1 values on page images; Figure 1 and Figure S3 measured); inferred (YD sub-means) |
| Severity | major |
| Source | S3, AB, SD, S4 |

**GB-30 The panels of Figure 1 use abbreviations that the caption does not resolve.**

| Field | Content |
|---|---|
| Check | P29 |
| Location | Figure 1 (p. 24, y axes of all panels); caption p. 25 |
| Quotation | "Evolution of dust PSA contributions to EDC ice core between 2852 to 33699 yr BP" |
| Concern | The caption spells out Central Western Argentina and Antarctica, which are not shown, but not PAT, AUS, SAF, NZ, PAP, PSA or EDC on the axes. Image (p. 24) and caption (p. 25) stand on different pages. |
| Suggestion | Add "PAT, Patagonia; AUS, Australia; SAF, Southern Africa; NZ, New Zealand; PAP, Puna-Altiplano Plateau; PSA, potential source area" to the caption and set caption and image on one page. |
| Status | verified |
| Severity | minor |
| Source | AB |

**GB-31 The panel labelled "Holocene" in Figure 3 shows the Early Holocene, and the panel labelled "Early Holocene" in Figure S4 shows the Late Holocene.**

| Field | Content |
|---|---|
| Check | P3 |
| Location | Figure 3 (p. 27, panel Holocene; caption l. 869 to 873); Supp. p. 8 (Figure S4, panel Early Holocene; caption Supp. p. 7); p. 9, l. 281 |
| Quotation | "Box plots of provenance contributions (in %) of Holocene, and Last Glacial Maximum (LGM)" |
| Concern | The LGM panel of Figure 3 reproduces Table S1, so the plots are drawn from it. Figure 3, Holocene panel, measured: PAT Q3 73.1, median 55.3, Q1 12.4; AUS 34.4, 18.3, 2.9. Table S1, Early Holocene (n = 56): PAT 73.0, 55.2, 12.3; AUS 34.2, 18.1, 2.8; whole Holocene (n = 116): PAT 73.8, 58.6, 18.4; AUS 33.0, 16.1, 2.7. The merging step remeasured the PAT box on the page image (73 / 55 / 12 %) and confirmed the Early Holocene. Figure S4, "Early Holocene" panel: PAT 80.6, 61.6, 18.9 against Late Holocene 80.7, 61.7, 18.9. The glacial to interglacial contrast of Figure 3 therefore compares the LGM with the Early Holocene only, while l. 281 and Table S5 speak of the Holocene, and the Late Holocene appears nowhere under its own name. |
| Suggestion | Relabel the Figure 3 panel "Early Holocene (7.5 to 11.7 kyr BP)" or redraw it from all 116 Holocene samples, relabel the Figure S4 panel "Late Holocene (2.8 to 7.5 kyr BP)", and state n for each box. |
| Status | verified (measured on page images); inferred (quartiles computed from Table S1) |
| Severity | moderate |
| Source | AB |

**GB-32 Figures 3 and S4 draw whiskers at 1.5 interquartile ranges with outliers beyond, while both captions say the whiskers mark the extremes.**

| Field | Content |
|---|---|
| Check | P29, P3 |
| Location | Figure 3 (p. 27, caption l. 872); Supp. p. 7 (caption Figure S4) |
| Quotation | "and the whiskers indicate the lower and upper extremes." |
| Concern | Measured whisker ends against Tukey fences and extremes of Table S1: Early Holocene AUS 80.0 (fence 79.8, maximum 98.1), NZ 16.6 (16.4, maximum 90.4), PAP 28.2 (28.0, maximum 100.0); LGM PAT 84.5 (84.4, maximum 93.5). The points beyond the whiskers are outliers. |
| Suggestion | Write in both captions "whiskers extend to the most extreme values within 1.5 times the interquartile range; points beyond are shown individually". |
| Status | verified (Figure 3); inferred (Figure S4, read without separate calculation) |
| Severity | minor |
| Source | AB |

**GB-33 Panels 2 to 5 of Figure S4 are drawn about 2 % taller than the only y axis, so their boxes read about 1 % too high.**

| Field | Content |
|---|---|
| Check | P3 |
| Location | Supp. p. 8 (Figure S4, panels YD, ACR, HS1, MIS3) |
| Quotation | "Box plots of provenance contributions of (1) Early Holocene, (2) Younger Dryas (YD)" |
| Concern | Only the first panel has a y axis. Read on it, the PAT boxes give YD 86.3 / 71.3 / 48.0, ACR 81.3 / 74.3 / 58.0, HS1 80.5 / 76.0 / 68.0, MIS3 78.5 / 71.5 / 63.4 (Q3 / median / Q1); Table S1 gives 84.8 / 70.2 / 47.1, 80.2 / 73.2 / 57.2, 79.4 / 75.0 / 67.0, 77.2 / 70.5 / 62.5, a difference of 0.9 to 1.5 % against a reading uncertainty of 0.06 %. Scaling each panel on its own whisker caps reproduces Table S1 within 0.3 %. |
| Suggestion | Draw all five panels on one common axis, or give each panel its own y axis. |
| Status | verified (measured); inferred (separate scaling) |
| Severity | minor |
| Source | AB |

**GB-34 Ice-core samples in Table S1 are identified only by age, and four ages occur twice with different results.**

| Field | Content |
|---|---|
| Check | P38 |
| Location | Supp. p. 11 (rows 3559); Supp. p. 13 (rows 10511, 12841); Supp. p. 14 (rows 28709) |
| Quotation | "Time [yr]" |
| Concern | Table S1 lists 241 samples, but its only identifier is the age. Four ages occur twice with different results (for example 3559 yr: PAT 86.7 and 0.0), so eight samples cannot be told apart or traced to depth or bag number; this also blocks matching Table S1 to any input table added under GB-10. |
| Suggestion | Add depth or bag number as first column of Table S1 and give ages with enough digits to separate the four pairs. |
| Status | verified (page images) |
| Severity | minor |
| Source | S2 |

**GB-35 The number of samples behind each period mean in Table S5 must be counted from Table S1, and the means are sample means, not time-weighted.**

| Field | Content |
|---|---|
| Check | P22 |
| Location | Supp. p. 22 (Table S5); p. 6, l. 183 to 188; Figure 3; Figure S4 |
| Quotation | "Table S5: Average contributions for each PSA (in percents) based on dust samples from EDC and EDML ice core through time (by period)" |
| Concern | Counted from Table S1: MIS3 41, LGM 40, HS1 27, ACR 8, YD 9, Early Holocene 56, Late Holocene 60 (total 241); the text gives counts only for ACR and YD. Time-weighted, the Holocene PAT mean is 51.6 instead of 49.0 and AUS 21.7 instead of 23.1, because the Late Holocene is sampled more densely. |
| Suggestion | Add a column n to Table S5 for EDC and EDML and state in the caption that the means are sample means. |
| Status | inferred (counted and computed from Table S1) |
| Severity | minor |
| Source | S3 |

#### Minor corrections

| Kennung | Location | Quotation | Replacement | Source |
|---|---|---|---|---|
| KK-18 | p. 6, l. 189 | "It contributes for 65-70% (average" | "It contributes 65 to 70% (average" | S3 |
| KK-19 | p. 6, l. 191 | "the PSA dust assemblage during HSI is marked" | "the PSA dust assemblage during HS1 is marked" | S2, S3 |
| KK-20 | p. 6, l. 193 | "(averages contributions)" | "(average contributions)" | S3 |
| KK-21 | p. 6, l. 198 | "and therefore reflects regional mixed input" | "and therefore reflect regional mixed input" | S3 |
| KK-22 | p. 6, l. 199 | "LREE (low rare earth elements)" | "LREE (light rare earth elements)" | S3 |
| KK-23 | p. 25, caption Figure 1 | "between 2852 to 33699 yr BP"; "as their dust emissions contribution are very low" | "between 2852 and 33699 yr BP"; "as their contributions are very low" | AB |
| KK-24 | p. 27, l. 872 to 873 (caption Figure 3) | "Box plots for HS1, ACR and YD are illustrated in Figure S4." | "Box plots for the Early Holocene, YD, ACR, HS1 and MIS3 are shown in Figure S4." | ZF |
| KK-25 | Supp. p. 7 (caption Figure S4) | "(3) Antarctica Cold Reveal (ACR), (4) Heindrich Stadial 1 (HS1), and (5) Marine Isotope 3 (MIS3)" | "(3) Antarctic Cold Reversal (ACR), (4) Heinrich Stadial 1 (HS1), and (5) Marine Isotope Stage 3 (MIS3)" | S2, S3, AB |

#### Verification log

| Kennung | Check | Checked | Values | Result |
|---|---|---|---|---|
| PP-14 | P1, P2, P37 | Table S5 (EDC) recomputed as sample means from the 241 rows of Table S1 with the period limits of l. 185 to 188 (PAP = Puna + Altiplano) | PAT, PAP, SAF, AUS, NZ, ANT: Late Holocene (60) 50.7, 12.0, 11.6, 21.4, 3.8, 0.6; Early Holocene (56) 47.1, 10.0, 9.8, 24.9, 8.1, 0.0; Holocene (116) 49.0, 11.0, 10.7, 23.1, 5.9, 0.3; YD (9) 63.1, 4.5, 14.6, 14.5, 3.3, 0.0; ACR (8) 68.9, 5.2, 8.0, 11.1, 6.6, 0.2; HS1 (27) 74.8, 2.0, 4.9, 11.3, 7.1, 0.0; LGM (40) 65.7, 3.6, 6.3, 10.2, 14.2, 0.0; MIS3 (41) 70.3, 2.2, 9.3, 9.1, 9.1, 0.0; all 48 equal to Table S5 within 0.1; row sums of Table S5 99.9 to 100.1 | no finding |
| PP-15 | P2, P36, P5 | values in the abstract and Section 3 against Table S5 | abstract PAT ~65 to 75 % (70.3, 65.7, 74.8), Holocene ~49 % (49.0); l. 189 to 193 PAT 65 to 70, 75, 69, 63 (70.3 and 65.7, 74.8, 68.9, 63.1); l. 195 47 to 51 (47.1, 50.7); l. 203 to 204 AUS 9, 10, 11, 11, ~15, 23 (9.1, 10.2, 11.3, 11.1, 14.5, 23.1); l. 206 SAF ~5 to 9 (9.3, 6.3, 4.9, 8.0); l. 209 to 210 NZ 14, 7, 6.5, 3, 6 (14.2, 7.1, 6.6, 3.3, 5.9); l. 211 to 212 PAP below 4 and ~5 (2.2, 3.6, 2.0; 5.2, 4.5); l. 216 PAP 11 (11.0); l. 223 LGM order NZ, AUS, SAF, PAP (14.2, 10.2, 6.3, 3.6) | deviations only in GB-27, GB-28, GB-29 |
| PP-16 | P38 | names of PSA, cores and periods across text, Tables S1 to S5, Figures 1 to 5 and S1 to S5 | PAT, AUS, SAF, NZ, ANT, SSA, EDC, EDML used identically; variants only for PAP, CWA and DS against PSA; period names consistent apart from the corrections listed | findings GB-09, GB-14 |
| PP-17 | P21 | whether sample means and time-weighted means lead to different statements | Holocene PAT 49.0 / 51.6, AUS 23.1 / 21.7, SAF 10.7 / 10.8, NZ 5.9 / 4.8; LGM PAT 65.7 / 65.8, AUS 10.2 / 9.0, SAF 6.3 / 7.1, NZ 14.2 / 15.3 (sample / time-weighted) | no change of direction; ranking see GB-27 |
| PP-18 | P11 | matrix of periods against announced outputs | relative contributions per sample: all periods (Table S1, Figure 1); period means: eight EDC and five EDML periods (Table S5), EDML Late Holocene and MIS3 absent, justified by the EDML record length (l. 406 to 407); box plots: all periods in Figure 3 and Figure S4; isotopes: six periods (Figure 2) | fluxes and MC spread missing (GB-20, GB-19) |
| PP-19 | P29, P3 | list of all figures with type, caption and citations | Figures 1 to 5 and S1 to S5 present and cited; first citations Figure 1 l. 183, 2 l. 244, 3 l. 281, 5 l. 340, 4 l. 405; no graphical abstract; p. 23 holds only the heading | order see GB-47 |
| PP-20 | P3, P24 | Figure 1 against Table S1 and text: period zones, smoothing, named values | zones match l. 185 to 188 within 0.05 kyr; bold curves equal a centred 9-point moving average (mean absolute deviation 0.6 % PAT, 0.3 % AUS before 14.7 kyr); smoothed PAT minima 10.13, 8.54, 6.33 kyr (text 10, 8.6, 6.3); AUS raw values above 90 % at 9772 and 9976 yr (text maxima 9.5 to 10 kyr); PAT 3 to 5 kyr mean 52.8 % (text 50 to 55 %) | no finding beyond GB-28, GB-29, GB-20, GB-30 |
| PP-21 | P3 | Figure 3, panel LGM, against Table S1 | PAT Q3 71.9 (71.7), median 65.9 (65.8), Q1 59.0 (58.9); AUS 14.1 (14.0), 10.3 (10.2), 6.0 (5.8); NZ 19.0 (18.9), 15.6 (15.5), 11.0 (10.8); PAP 6.5 (6.5), 1.9 (1.9) | no finding |
| PP-22 | P3 | Figure S4, panels YD to MIS3, each scaled on its own whisker caps, against Table S1 | YD PAT 84.8 / 70.0 / 47.1 (84.8 / 70.2 / 47.1); ACR 79.9 / 73.1 / 57.2 (80.2 / 73.2 / 57.2); HS1 79.3 / 74.9 / 67.1 (79.4 / 75.0 / 67.0); MIS3 77.3 / 70.4 / 62.5 (77.2 / 70.5 / 62.5) | no finding beyond GB-33 |

### Segment 4: Discussion, conclusion, declarations, references (p. 7 to 22; Figures 2, 4, 5; Figures S2, S3, S5; Tables S3, S4)

#### Substantive findings

**GB-36 The shift is dated to the onset of the ACR in Section 4.1 but to about 14.5 kyr BP elsewhere.**

| Field | Content |
|---|---|
| Check | P2 |
| Location | p. 7, l. 233; p. 7, l. 225; p. 6, l. 186; p. 1, l. 23; p. 14, l. 477 |
| Quotation | "Our calculations highlight a major shift in dust provenance occurred at the onset of the ACR" |
| Concern | The ACR is defined as 14.7 to 12.9 kyr BP (l. 186), while l. 225, the abstract (l. 23) and the conclusion (l. 477) place the shift at about 14.5 kyr BP, the date tied to shelf submergence. With a sample spacing of about 100 to 200 years in this part of the record, the two dates are distinguishable in principle, and the mechanism argument depends on which one holds. |
| Suggestion | Give one date for the shift in l. 233 and state how it was determined (for example a change-point on Table S1). |
| Status | verified |
| Severity | minor |
| Source | ZF |

**GB-37 The isotopic validation claims agreement with Holocene dust "measured in EDC", but no measured EDC Holocene value is shown or tabulated.**

| Field | Content |
|---|---|
| Check | P15, P3, P10, P19, P32 |
| Location | p. 7, l. 238 to 240; p. 8, l. 254 to 260; p. 3, l. 93 to 94; Figure 2 (p. 26) with caption l. 857 to 866; Supp. p. 21 (Table S4) |
| Quotation | "Overall, the close agreement between our modeled isotopic compositions and those measured in EDC for both glacial and interglacial intervals supports the robustness of our DEPOT algorithm" |
| Concern | Comparing the REE apportionment with independent Sr and Nd data (aim 2) is a useful test. Table S4, the source of the open symbols, holds 35 values: 2 from EPICA Dome C (LGM: 0.7086 and minus 1.66; 0.7088 and minus 2.46), 1 from Old Dome C (HS1), 18 from Taylor Glacier and 14 from Berkner Island; all 22 Holocene values come from Taylor Glacier (8, mean 0.7111 and minus 4.64) and Berkner Island (14, mean 0.7132 and minus 11.50), and the open Holocene symbols sit at Berkner Island coordinates. The EDC Holocene values quoted in l. 240 (about 0.710, εNd minus 4.51 to minus 5.68) are neither in Table S4 nor in Figure 2. Recomputed with Eq. 3 and 4, Table S3 and the Table S5 means, the Holocene mix is about 0.7094 to 0.7104 and minus 4.1 to minus 5.3 (depending on the PAP assignment, GB-14), close to the quoted EDC range, and the LGM mix 0.7083 and minus 2.61, close to the EDC LGM values. Agreement is thus plausible but neither shown nor quantified; Berkner Island lies in the Weddell Sea sector, which l. 425 to 428 themselves describe as receiving different dust. No counter-test shows that a mixture without a provenance shift would fit worse. The verb "supports the robustness" is stronger than Figure 2 allows; aim (2) is affected, hence major. |
| Suggestion | Add the EDC Holocene Sr and Nd values (Delmonte et al., l. 238 to 240) to Table S4 and Figure 2 with their own symbol, distinguish symbols by core, give the misfit per period in 87Sr/86Sr and εNd, add the counter-test of applying the glacial mixture to the Holocene, and rephrase l. 258 to 260 accordingly. |
| Status | verified (Table S4 and page images); inferred (recomputed mixtures) |
| Severity | major |
| Source | S4, AB, SD |

**GB-38 Delmonte et al. (2004) is cited for Sr and Nd values of EDC dust, but the only 2004 entry is a dust size study.**

| Field | Content |
|---|---|
| Check | P4 |
| Location | p. 7, l. 238 to 240; p. 26, l. 861 (caption Figure 2); p. 17, l. 561 to 564 (reference list); Supp. p. 21 (Table S4) |
| Quotation | "For instance, Delmonte et al. (2004) reported 87Sr/86Sr ratios of ~0.708 and ε(Nd) values ranging from -1.66 to -2.46 for LGM dust at EDC" |
| Concern | The listed entry is "Dust size evidence for opposite regional atmospheric circulation changes over east Antarctica during the last climatic transition", Climate Dynamics 23, 427 to 438, which fits the circulation citation in l. 416, not isotope values. Table S4 cites "Delmonte et al., 2004a", implying a second 2004 paper. Sr and Nd data for EPICA Dome C dust were published by Delmonte et al. (2004) in Earth-Science Reviews 66, 63 to 87 ("Comparing the Epica and Vostok dust records during the last 220,000 years: stratigraphical correlation and provenance in glacial periods"), which is not in the list. |
| Suggestion | Add Delmonte et al. (2004a), Earth-Science Reviews 66, 63 to 87, to the reference list, cite it as 2004a in l. 238, the Figure 2 caption and Table S4, and the Climate Dynamics paper as 2004b in l. 416. |
| Status | verified (entry content); inferred (that the values come from the Earth-Science Reviews paper, bibliographic record only) |
| Severity | minor |
| Source | S4 |

**GB-39 The timing and dimensions of the Patagonian Ice Sheet maximum are attributed to Davies et al. (2020) in a form the source does not give.**

| Field | Content |
|---|---|
| Check | P13 |
| Location | p. 8, l. 267 to 269 |
| Quotation | "the Patagonian Ice Sheet reached its maximum spatial extent between ~34 and 29.4 kyr BP, covering much of the Andes with an ice mass 2090 km long and 350 km wide (Davies et al., 2020)" |
| Concern | The abstract of Davies et al. (2020, Earth-Science Reviews 204, 103152, read in the Exeter repository record) states that the ice sheet reached its maximum extent by 33 to 28 ka from 38°S to 48°S and earlier, around 47 ka, south of 48°S, and that at 35 ka it was 350 km wide and 2090 km long. The interval "~34 and 29.4 kyr BP" does not appear, and the dimensions refer to 35 ka, not to the maximum. The argument of the paragraph (extensive glaciation during the LGM and MIS3) is unaffected. |
| Suggestion | In l. 267 to 269 write "reached its maximum extent by 33 to 28 ka north of 48°S (earlier, around 47 ka, further south), and at 35 ka measured about 2090 km by 350 km (Davies et al., 2020)". |
| Status | verified (source abstract read) |
| Severity | minor |
| Source | ZF |

**GB-40 Krätschmer et al. (2022) is cited for a 70 to 90 % share of South American and Australian dust, but the source gives over 90 % and a larger Australian share in the LGM.**

| Field | Content |
|---|---|
| Check | P13 |
| Location | p. 8, l. 275 to p. 9, l. 277 |
| Quotation | "Model simulations also support this view, estimating that SSA and AUS sources together supplied 70-90% (here, PAT+AUS is ~77%) of the dust reaching EA during the LGM (i.e., Albani et al., 2012; Krätschmer et al., 2022)." |
| Concern | The sentence is used as support for Patagonian dominance ("this view", l. 273 to 275). The abstract of Krätschmer et al. (2022, Clim. Past 18, 67 to 87, read in the AWI repository record) states that over 90 % of the dust deposited over Antarctica is of Australian or South American origin in both the pre-industrial and the LGM, and that Australia contributes a higher proportion during the LGM. Instance S1 reported from the full text (Table 5) Australia 68 % and South America 24 % for Antarctica in the LGM and the conclusion that Australia was the predominant source; Albani et al. (2012), cited alongside, gives no percentage (full text read by S1). The model result thus contradicts rather than supports Patagonian dominance, and the range 70 to 90 % is not in either source. The comparison value "PAT+AUS" also differs from "SSA and AUS" in the same sentence. |
| Suggestion | In l. 275 to 277 report the model result as it stands (over 90 % from South America and Australia, with Australia dominant in the LGM according to Krätschmer et al., 2022), discuss the contrast with the REE result, and compare with SSA plus AUS (69.3 + 10.2 = 79.5 %). |
| Status | verified (abstract statements); inferred (Table 5 values, reported by instance S1; full text not reachable during merging) |
| Severity | moderate |
| Source | ZF |

**GB-41 The LGM values in l. 276 and l. 282 differ from Table S5 and from the results section.**

| Field | Content |
|---|---|
| Check | P2, P3, P15, P36 |
| Location | p. 9, l. 276 and l. 281 to 282; p. 7, l. 209; Figure 3 (panel LGM, box NZ); Supp. p. 22 (Table S5, row LGM) |
| Quotation | "However, we find a higher average NZ contribution (~11%), making it the second-largest dust source to EDC during the LGM." |
| Concern | Table S5 gives NZ 14.2 % in the LGM, l. 209 says 14 %, and the NZ box of Figure 3 measures median 15.6 (Table S1: 15.5); for PAT plus AUS Table S5 gives 65.7 + 10.2 = 75.9 %, the text "~77%". Both values in the text match the pooled MIS3 and LGM samples (NZ 11.6, PAT plus AUS 77.7), while l. 280 to 281 and l. 293 to 294 (65.7 + 14.2 = 79.9) use the LGM alone. The comparison with Coppo et al. (2022, NZ 5 %) depends on which value is meant. |
| Suggestion | In l. 276 and l. 282 use the LGM values of Table S5 (PAT plus AUS ~76 %, NZ ~14 %), or label the pooled values as MIS3 plus LGM. |
| Status | verified (text, Table S5, Figure 3 measured); inferred (pooled values) |
| Severity | minor |
| Source | S3, AB, S4, SD |

**GB-42 The high-latitude share for HS1 (84 %) does not follow from Table S5.**

| Field | Content |
|---|---|
| Check | P1, P15, P36 |
| Location | p. 9, l. 295; Supp. p. 22 (Table S5, row HS1) |
| Quotation | "This dominance persisted into HS1, with high-latitude sources totaling 84 %" |
| Concern | High-latitude sources are PAT and NZ (l. 293). Table S5 gives 74.8 + 7.1 = 81.9 %, 2.1 points below 84. The median of per-sample PAT plus NZ over the 27 HS1 samples is 83.2; adding PAP gives 83.9, but PAP is classed as low-latitude (l. 294). Neither basis is stated. |
| Suggestion | In l. 295 write "~82 %", or state the basis used. |
| Status | inferred (computed from Tables S5 and S1) |
| Severity | minor |
| Source | S3, S4, SD |

**GB-43 The higher Holocene variability is attributed to source and transport processes, although fit quality drops at the same time and noise is not separated from signal.**

| Field | Content |
|---|---|
| Check | P15, P9, P32 |
| Location | p. 9, l. 306 to 314; p. 6, l. 174 to 179; p. 4, l. 112 to 113; Supp. p. 11 to 15 (Table S1, including same-age rows 3559, 10511, 12841, 28709) |
| Quotation | "During YD and throughout the Holocene, our unmixing model reveals a significantly larger variability in the dust assemblages reaching EDC as shown in Figure 1. This increased variability, seemingly higher frequency changes in sources, likely reflects several interrelated processes" |
| Concern | The manuscript states openly that all 38 excluded samples are younger than 14 kyr with concentrations near detection, where noise "distorts the REE patterns" (l. 175 to 179), and that Holocene samples integrate 2 to 3 years against 4 to 5 years in the LGM (l. 112 to 113). Table S1 shows the consequence for retained samples: mean R 0.799 in the Holocene (116 samples, minimum 0.66) against 0.924 in the LGM (40 samples, minimum 0.88); the standard deviation of PAT is 32.1 percentage points in the Holocene against 9.9 in the LGM; 23 Holocene samples have PAT = 0 against one older sample. The four same-age pairs differ by half the sum of absolute differences of 87.2 (3559 yr), 52.9 (10511) and 39.4 (12841) points against 10.2 at 28709 (LGM); if they are replicates or adjacent samples, their spread equals the Holocene variability interpreted in Section 4.3, which is asked. Three causes can produce the variability: real changes in source and transport (discussed), analytical noise at low concentration (documented but not carried through), and shorter integration time per sample. The disclosed limitation is not taken to the interpretation, which concerns a main result, hence major. |
| Suggestion | In Section 4.3 separate the three causes: fit synthetic ice-core patterns from a fixed glacial mixture perturbed with the analytical uncertainty at Holocene concentrations and report the variability this alone produces; show the Monte Carlo spread per sample against age; test whether contribution variance correlates with R or concentration; explain the same-age rows; state which Holocene features exceed the noise level, and weaken "significantly larger variability" (l. 306) if needed. |
| Status | verified (R statistics, standard deviations, pair values from Table S1); inferred (relative share of the causes); assumption (pairs are replicates), hence put as a question |
| Severity | major |
| Source | S4, SD |

**GB-44 The Holocene SSA share is given as 61 % and as 60 % five lines apart.**

| Field | Content |
|---|---|
| Check | P2 |
| Location | p. 10, l. 321 and l. 326; Supp. p. 22 (Table S5, row Holocene) |
| Quotation | "compared to 61% in our record when combining PAT, CWA, and PAP" |
| Concern | Table S5 gives 49.0 + 0.0 + 11.0 = 60.0 %, as l. 326 states; 61 % has no basis in the tables (Late Holocene 62.7, Early Holocene 57.1). |
| Suggestion | In l. 321 write "60%". |
| Status | verified |
| Severity | minor |
| Source | S3, S4 |

**GB-45 The agreement with the Potrok Aike wind record is asserted by eye: a feature named in the text is not visible in Figure 5, and no common time axis or test is used.**

| Field | Content |
|---|---|
| Check | P3, P24, P10 |
| Location | p. 10, l. 338 to 341; p. 11, l. 348 to 352, l. 371 to 374; p. 3, l. 94 to 95; Figure 5 (p. 29, panels A and B) |
| Quotation | "Overall, our Holocene provenance record for PAT contributions is matching well with the SWW intensity proxies in Potrok Aike bog (see Figure 5)."; "(also present in Potrok Aike wind intensity record)" |
| Concern | Aim (3) asks whether provenance shifts relate to regional climate. Panel B, measured (MDF 6.01 px per mT, axis inverted): the MDF curve stays at 17.0 to 18.1 mT between 6.0 and 6.5 kyr, within the 14.1 to 20.6 mT range of 4.75 to 8.0 kyr; a weakening of the wind would be an excursion to higher MDF, and none occurs at 6 to 6.5 kyr, while panel A shows the PAT drop (27.3 % at 6.33 kyr). As a rough measure of "matching well", the correlation of the digitised PAT curve and the inverted MDF curve from 5.0 to 11.4 kyr is r = 0.29 (n = 264 columns), from 8.0 to 11.4 kyr r = 0.14. The weakening is dated "11 to 8 kyr BP" (l. 340), while the blue band in Figure 5 spans 7.96 to 11.42 kyr. No resampling to a common time step, no treatment of the age uncertainty between EDC3 and the lake chronology, and no test against the noise of GB-43 are reported; single peaks are attributed to regional dry phases (l. 350, l. 371 to 372). Aim (3) is affected, hence major. |
| Suggestion | Remove "also present in Potrok Aike wind intensity record" or mark the feature in panel B; resample both series to a common step, compute a correlation with lag or age-uncertainty analysis and significance against a red-noise null; restrict interpretations of single peaks to those outside the noise band; make the band match l. 340 or explain it. |
| Status | verified (curves measured); inferred (correlations from digitised curves) |
| Severity | major |
| Source | AB, SD |

**GB-46 The wind-intensity record compared in Figure 5 comes from lake sediments of Laguna Potrok Aike, but the text calls it a bog.**

| Field | Content |
|---|---|
| Check | P38 |
| Location | p. 10, l. 339 to 340; p. 11, l. 348 to 349; p. 29, l. 880 to 882 (caption Figure 5); p. 19, l. 690 (reference) |
| Quotation | "the SWW intensity proxies in Potrok Aike bog (see Figure 5)"; "(Potrok Aike bog 52°S; Lago Cardiel 48.9°S" |
| Concern | The caption and the cited reference name lacustrine sediments of Laguna Potrok Aike, a maar lake; "bog" denotes a different archive type (peat), so a reader looking for the data would search the wrong archive. |
| Suggestion | Replace "Potrok Aike bog" by "Laguna Potrok Aike" in l. 339 to 340 and l. 348 to 349. |
| Status | verified (page images p. 10, 11, 29 and reference) |
| Severity | minor |
| Source | S2 |

**GB-47 Figure 5 is cited before Figure 4, so figures are not numbered in order of first citation.**

| Field | Content |
|---|---|
| Check | P3 |
| Location | p. 10, l. 340 (first citation of Figure 5); p. 12, l. 405 (first citation of Figure 4) |
| Quotation | "Aike bog (see Figure 5)." |
| Concern | First citations: Figure 1 l. 183, Figure 2 l. 244, Figure 3 l. 281, Figure 5 l. 340, Figure 4 l. 405; the supplementary figures are cited in order. |
| Suggestion | Swap the numbers of Figures 4 and 5 (captions, l. 340, l. 405, l. 419). |
| Status | verified |
| Severity | minor |
| Source | AB, S4 |

**GB-48 Gili et al. (2016) is cited without an entry in the reference list.**

| Field | Content |
|---|---|
| Check | P4 |
| Location | p. 11, l. 365 |
| Quotation | "with the previous Pb isotopic study (Gili et al., 2016) ." |
| Concern | The reference list holds Gili et al. 2017 and 2022 only (p. 18, l. 637 and l. 641). The Pb study supports the statement on interglacial PAP contributions, but the reader cannot find it. |
| Suggestion | Add the entry for Gili et al. (2016), or correct the year if Gili et al. (2017) is meant. |
| Status | verified |
| Severity | minor |
| Source | S4 |

**GB-49 Figure S4 cannot show the Holocene SAF trend that l. 381 to 382 attribute to it.**

| Field | Content |
|---|---|
| Check | P3, P4 |
| Location | p. 11, l. 381 to p. 12, l. 382; Supp. p. 8 (Figure S4) |
| Quotation | "an increasing trend in SAF dust contribution to EDC ice core (Figure S4)" |
| Concern | Figure S4 holds one Holocene box per source (labelled Early Holocene, in fact the Late Holocene, GB-31), so it contains no time series within the Holocene. A trend can be seen only in Figure 1 (panel SAF) or Figure S3 (SAF subregions); is Figure S3 meant? |
| Suggestion | Cite Figure S3 or Figure 1, or compare Early and Late Holocene SAF means in the text (Table S5: 9.8 and 11.6 %). |
| Status | verified (content of Figure S4); assumption (intended figure), hence put as a question |
| Severity | minor |
| Source | AB, S4 |

**GB-50 The EDC and EDML records compared in Section 4.4 differ in time window, method version and possibly chronology.**

| Field | Content |
|---|---|
| Check | P2, P21, P15, P3, P7, P9 |
| Location | p. 12, l. 405 to 407; p. 13, l. 423 to 424, l. 444 to 446; Figure 4 (p. 28, all panels, bar Holo); Supp. p. 22 (Table S5); p. 5, l. 144 to 145; Supp. p. 17 (Table S2, SAF rows "this study") |
| Quotation | "over their overlapping interval shared by both datasets, i.e., between 7.5 and 27 kyr BP"; "EDC appears to receive substantially less PAT dust (-14%) but higher contributions of Australian dust (+12%) than EDML." |
| Concern | (a) Window: EDML has only an Early Holocene row (7.5 to 11.7 kyr). The stated differences are reproduced only with the full EDC Holocene: 49.0 minus 62.7 = minus 13.7 (PAT) and 23.1 minus 10.8 = +12.3 (AUS); with the matching EDC Early Holocene they are minus 15.6 and +14.1. The Figure 4 bars (measured PAT minus 13.9, AUS +12.4) also use the full EDC Holocene, so 8.9 kyr of EDC are compared with 4.2 kyr of EDML. EDC "LGM" covers 18 to 29 kyr, of which 15 of 40 samples lie outside the stated overlap; restricting to 18 to 27 kyr changes little (PAT minus 8.5, NZ +8.1). (b) Method version: EDML was unmixed with 14 REE, EDC with 13 (disclosed, l. 144 to 145), and the library contains six SAF patterns marked "this study", so it is not the library of the EDML fit; differences of 5 to 14 points can come from the method as well as from circulation (see also GB-08). (c) Chronology: EDC ages are on EDC3; the EDML chronology is not given, yet "synchronous millennial-scale changes" are claimed (l. 445). The direction of the Holocene result holds, but aim (4) rests on this comparison, hence major. |
| Suggestion | Compare both records on the same windows (EDC 7.5 to 11.7 kyr for the Holocene bar, labelled "Early Holocene"; 18 to 27 kyr for the LGM) in Section 4.4, Figure 4 and Table S5; refit EDML with the present 13-REE set and library, or EDC with the EDML set, and report both; state the EDML chronology and place both records on a common one before claiming synchrony. |
| Status | verified (windows, Figure 4 measurements, method versions); inferred (computed differences); assumption (that the method difference changes the results), hence put as a question |
| Severity | major |
| Source | S3, S4, AB, SD |

**GB-51 The tentative status of the ACR and YD results is disclosed only in Section 4.4, not where the period results and the timing of the shift are stated.**

| Field | Content |
|---|---|
| Check | P17 |
| Location | p. 12, l. 407 to 409; p. 6, l. 183 to 193; p. 7, l. 233; p. 6, l. 174 to 179 |
| Quotation | "It is important however to note that results for ACR and YD are tentative" |
| Concern | Section 3 reports ACR and YD means (l. 192, 204, 207, 212) and Section 4.1 places the shift at the onset of the ACR (l. 233) without the caveat, although ACR rests on 8 and YD on 9 samples. The low concentrations of young samples (l. 175 to 179) are likewise stated in the Results, not in the Methods where the threshold is introduced. |
| Suggestion | Move the caveat and the sample counts per period to Section 3 (l. 183 to 188) and l. 233, and state the low-concentration limitation in Section 2 next to the threshold. |
| Status | verified |
| Severity | moderate |
| Source | SD |

**GB-52 The YD sample count in Section 4.4 is 7, but Table S1 and Figure S4 have 9.**

| Field | Content |
|---|---|
| Check | P2, P3, P15, P36 |
| Location | p. 12, l. 408 to 409; Supp. p. 13 (Table S1, YD block); Supp. p. 8 (Figure S4, panel YD) |
| Quotation | "due to the limited number samples covering those periods in EDC (8 and 7 samples in ACR and YD," |
| Concern | Table S1 has nine YD rows (11779, 11993, 12227, 12477, 12588, 12754, 12841 twice, 12867), and the Table S5 mean and the YD box of Figure S4 (PAT 84.8 / 70.0 / 47.1 measured, nine samples 84.8 / 70.2 / 47.1, seven samples 83.6 / 70.2 / 39.5) are reproduced from all nine. The ACR count of 8 is correct. Treating the two 12841 rows as one would give 8, not 7. |
| Suggestion | In l. 408 write "8 and 9 samples in ACR and YD", or explain the count. |
| Status | verified (page images) |
| Severity | minor |
| Source | S3, AB, S4, SD |

**GB-53 The EDC minus EDML differences for PAT in the ACR and YD are given in reversed order, and the YD excess is not at the expense of Southern African dust.**

| Field | Content |
|---|---|
| Check | P2, P3, P15, P36 |
| Location | p. 13, l. 421 to 422; Supp. p. 22 (Table S5, rows ACR and YD); Figure 4 (panels PAT, SAF, AUS, NZ) |
| Quotation | "the ACR and YD intervals exhibit a slight enrichment of Patagonian dust (+4 and +6.5%) in EDC, primarily at the expense of Southern African and Australian contributions." |
| Concern | Table S5: ACR PAT 68.9 minus 62.5 = +6.4; YD 63.1 minus 58.4 = +4.7; Figure 4 measures +6.5 and +4.9. The order of the text is reversed. In the YD, SAF is +6.4 (measured +6.5), so EDC has more SAF than EDML; the YD PAT excess is offset by AUS (minus 4.5), NZ (minus 3.9) and PAP (minus 2.4). The phrase holds only for the ACR (SAF minus 4.4, AUS minus 7.4). |
| Suggestion | In l. 422 write "(+6.4 and +4.7%, respectively)" and name the compensating sources for each interval separately. |
| Status | verified (Table S5 and Figure 4 on page images); inferred (differences computed) |
| Severity | minor |
| Source | S3, AB, S4, SD |

**GB-54 Section 4.4 and the conclusion state the sea-level and drainage mechanism as demonstrated, although the data show a timing coincidence, and the New Zealand part contradicts the timing in Table S5.**

| Field | Content |
|---|---|
| Check | P15 |
| Location | p. 14, l. 461 to 470, l. 480 to 484; p. 1, l. 29 to 31; p. 9, l. 296 to 297 |
| Quotation | "Importantly, our data demonstrate that these feedback mechanisms influenced dust deposition not only in EDML (in the Atlantic sector of East Antarctica) but also in EDC" |
| Concern | The EDC record shows a decline of PAT and a rise of low-latitude shares around 15 to 14 kyr BP (binned means from Table S1: PAT 83.2 % at 15 to 16 kyr, 72.0 % at 14 to 15 kyr, 64.3 % at 13 to 14 kyr). That shelf submergence and drainage reversal cause it is an interpretation through coincidence with Meltwater Pulse 1A (l. 450 to 453); no analysis tests it against the other named drivers (warming, wet scavenging, trajectory change, l. 308 to 314). Section 4.2 still writes "likely" (l. 296), while l. 466 says "demonstrate" and l. 483 to 484 "due to". Moreover, l. 461 to 462 include the submergence of the New Zealand shelf, but Table S5 shows NZ halving long before 14.5 kyr BP (LGM 14.2 %, HS1 7.1 %, ACR 6.6 %), so the mechanism cannot explain the NZ decline in its stated timing. The main interpretation is affected, hence major. |
| Suggestion | In l. 466 replace "demonstrate" by "are consistent with", in l. 480 "confirm" by "are consistent with", and in l. 484 "due to" by "most likely due to"; in l. 461 to 462 remove "(and New Zealand)" or discuss the earlier NZ decline separately in Section 4.2. |
| Status | verified (wording); verified (binned PAT values and NZ means from Tables S1 and S5) |
| Severity | major |
| Source | S4 |

**GB-55 The conclusion attributes the EDC and EDML differences to source-area climate, whereas Section 4.4 attributes them to the position of the two sites and atmospheric circulation.**

| Field | Content |
|---|---|
| Check | P15 |
| Location | p. 14, l. 484 to 487; p. 13, l. 424 to 443 |
| Quotation | "the relative contributions of PAT, SAF, NZ and AUS differed reflecting regional climatic dynamics in their respective source areas." |
| Concern | Source-area climate acts on both cores alike; by itself it cannot explain why two receptor sites differ at the same time. Section 4.4 accordingly explains the differences by "the geographic positioning of the two sites" (l. 425), the storm track, the polar vortex, Rossby waves and jet transport (l. 425 to 440). The conclusion replaces this receptor-side explanation with a source-side one and so contradicts the section it summarises for aim (4), hence major. |
| Suggestion | Rewrite l. 486 to 487 in line with Section 4.4, for example "differed, consistent with the different exposure of the two sites to mid- and low-latitude air masses". |
| Status | verified |
| Severity | major |
| Source | S4 |

**GB-56 The last sentence of the conclusion claims implications for biogeochemical fluxes and climate feedbacks for which no result is reported.**

| Field | Content |
|---|---|
| Check | P15 |
| Location | p. 15, l. 490 to 492 |
| Quotation | "with implications for biogeochemical fluxes, atmospheric circulation (chemistry and physics), and climate feedbacks on glacial-interglacial timescales." |
| Concern | The introduction motivates the study with iron fertilization (l. 37 to 52), and l. 166 to 167 announce absolute PSA fluxes, but no fluxes, iron estimates or chemistry results appear in Sections 3 and 4 (GB-20). |
| Suggestion | Show the announced fluxes and discuss their relevance, or rephrase l. 490 to 492 as an outlook ("may have implications ..., which future work could quantify"). |
| Status | verified |
| Severity | minor |
| Source | S4 |

**GB-57 The author contribution statement names "P.B", but no author has these initials.**

| Field | Content |
|---|---|
| Check | P38 |
| Location | p. 16, l. 497; p. 1, l. 4 to 5 (author list) |
| Quotation | "P.B performed the measurements" |
| Concern | The authors are S. Boxho, A. Vanderstraeten, N. Mattielli, G. G. Laruelle, A. Bory, P. Gabrielli and S. Bonneville; none has the initials P.B. Since the REE data are those of Gabrielli et al. (2010), P.G. may be meant; this is a question to the authors. |
| Suggestion | In l. 497 give the correct initials of the author who performed the measurements. |
| Status | verified (author list); assumption (intended author), hence put as a question |
| Severity | minor |
| Source | ZF |

**GB-58 In the legend of Figure 2, "EDC Early Holocene" marks the Late Holocene samples and "EDC Holocene" the Early Holocene samples; MIS3 samples are drawn in the LGM colour without a legend entry.**

| Field | Content |
|---|---|
| Check | P3, P29 |
| Location | Figure 2 (p. 26, legend); caption l. 857 to 866; p. 8, l. 252 to 255 |
| Quotation | "EDC Early Holocene"; "EDC Holocene"; "EDC LGM" |
| Concern | Legend colours measured at 600 dpi: EDC Early Holocene light red, EDC Holocene dark red, LGM blue. The modelled values of every Table S1 sample were recomputed with Eq. 3 and 4 and Table S3 and located on the calibrated axes: of the isolated positions, all 14 Late Holocene samples carry the light red of "EDC Early Holocene" and 10 of 11 Early Holocene samples the dark red of "EDC Holocene" (for example 6570 yr BP at 0.7236 and minus 13.17 on a light red dot; 8629 yr BP at 0.7128 and minus 10.90 on a dark red dot); 38 of 41 MIS3 positions show the LGM blue. The text (l. 252) names the blue group "end of MIS3/LGM". |
| Suggestion | Rename the legend entries "EDC Late Holocene" and "EDC Early Holocene" (or change the colours), rename "EDC LGM" to "EDC MIS3/LGM", and state in the caption which windows the colours cover. |
| Status | verified (colours measured); inferred (assignment of dots to samples by recomputation) |
| Severity | moderate |
| Source | AB |

**GB-59 Figure 5 has no title, unit or multiplier on the time axis and leaves the band, dashed lines and grey zones unexplained.**

| Field | Content |
|---|---|
| Check | P29 |
| Location | Figure 5 (p. 29, x axes of panels A and B, blue band, grey zones); caption l. 880 to 882 |
| Quotation | "Bold lines denote the mobile average over 9 steps." |
| Concern | The ticks read 0.5, 1, 1.5, 2, 2.5, 3 without the multiplier that Figure 1 carries, and the text layer contains no axis title or unit. The blue band with dashed edges (7.96 to 11.42 kyr) and the grey zones (11.72 to 12.88, 14.69 to 18.00 and from 28.99 kyr in panel A) are not explained, the period names are missing, and the raw MDF curve has no legend entry. |
| Suggestion | Add "Time (kyr BP)" to the x axis, label the periods as in Figure 1, and explain band and zones in the caption. |
| Status | verified |
| Severity | minor |
| Source | AB |

**GB-60 The y axes of Figure S2 carry no units.**

| Field | Content |
|---|---|
| Check | P29 |
| Location | Supp. p. 4 (Figure S2, panels A, B, C) |
| Quotation | "nssCa2+ flux"; "δ18O"; "deuterium excess" |
| Concern | The unit of the flux is given only in the main text (l. 166), δ18O and deuterium excess have none; panel B uses tick values such as minus 49.05 and minus 51.05, which suggests an offset axis. |
| Suggestion | Add "(µg m⁻² yr⁻¹)", "(‰)" and "(‰)" to the axis labels and use round tick values in panel B. |
| Status | verified |
| Severity | minor |
| Source | AB |

**GB-61 Figure S3 does not show the subregion values of Table S1: the largest Altiplano peaks are missing, and several Puna and Etosha peaks have no counterpart in the table.**

| Field | Content |
|---|---|
| Check | P3 |
| Location | Supp. p. 6 (Figure S3, panels Altiplano, Puna, Etosha); Supp. p. 11 to 15 (Table S1); p. 11, l. 355 to 358; p. 12, l. 395 to 396 |
| Quotation | "Evolution of contribution to EDC from subregions of the Puna-Altiplano and Southern Africa PSA" |
| Concern | Calibrated on the ticks: Table S1 gives Altiplano 100.0 at 8629, 97.0 at 11228 and 75.7 at 9957 yr BP; the Altiplano curve of Figure S3 reaches only 5.7, 14.6 and 2.3 % at these ages, and its highest peak is 66.1 % at 6.37 kyr against 53.5 in Table S1. Six Puna peaks match Table S1, but peaks of 42.9 % at 11.07 kyr and 54.9 % at 11.82 kyr have no counterpart (Table S1 maximum 29.1). The largest Etosha peak, 88.5 % at 11.89 kyr, falls between samples with SAF 0.0 and 1.3, while the large SAF value of Table S1 is at 12227 yr (94.7), which l. 396 also names. Figure 1 by contrast reproduces Table S1. Either Figure S3 shows another model run or shifted ages, or Table S1 does not hold the subregion values used in the discussion; this is asked. |
| Suggestion | Redraw Figure S3 from the data behind Table S1 and Figure 1, or state which run it shows, and add the Etosha, Sua and Namibian coast columns to Table S1 so that l. 379 to 400 can be checked. |
| Status | verified (measured on page image against Table S1); assumption (the two explanations), hence put as a question |
| Severity | moderate |
| Source | AB |

**GB-62 In Figure S5 the EDML entries of the legends are almost invisible.**

| Field | Content |
|---|---|
| Check | P29 |
| Location | Supp. p. 10 (Figure S5, legends of all five panels) |
| Quotation | "EDC"; "EDML" |
| Concern | Measured colour of the EDML legend text in the PAT panel: #dcecf4 on white, contrast ratio 1.3 : 1; the EDC entry has 2.9 : 1. The legend that tells the curves apart is not legible in print. |
| Suggestion | Write the legend entries in black and mark the cores by line style (for example EDML dashed). |
| Status | verified |
| Severity | minor |
| Source | AB |

#### Minor corrections

| Kennung | Location | Quotation | Replacement | Source |
|---|---|---|---|---|
| KK-26 | p. 7, l. 220 to 221 | "in the Epica Dome C ice core" | "in the EPICA Dome C (EDC) ice core" | S2, S4 |
| KK-27 | p. 7, l. 233 | "Our calculations highlight a major shift in dust provenance occurred" | "Our calculations highlight that a major shift in dust provenance occurred" | S4 |
| KK-28 | p. 7, l. 236 | "This shift already describes by Gili et al. (2022) and Vanderstraeten et al. (2023), appears" | "This shift, already described by Gili et al. (2022) and Vanderstraeten et al. (2023), appears" | S4 |
| KK-29 | p. 8, l. 246 | "(Table S3, e.i. Eq.3)" | "(Table S3, i.e. Eq. 3)" | S4, SD |
| KK-30 | p. 8, l. 248 | "where the mean isotopic signatures is represents by CIR PSA." | "where CIR_PSA represents the mean isotopic signature of each PSA." | S4 |
| KK-31 | p. 8, l. 261 (heading 4.2) | "4.2 Persistance of high-latitude dust source to EDC before 14.5 kyr BP" | "4.2 Persistence of high-latitude dust sources to EDC before 14.5 kyr BP" | S4 |
| KK-32 | p. 8, l. 270 | "by ~763.10" | "by ~763 × 10³ km²" (superscripts as printed) | S4 |
| KK-33 | p. 9, l. 300 | "before 14.5 kyr BP reflect a transport regime" | "before 14.5 kyr BP reflects a transport regime" | S4 |
| KK-34 | p. 10, l. 329 to 330 | "includes several McMurdo region sites (Section 4.2)" | "includes several McMurdo region sites (Section 2)" | S4 |
| KK-35 | p. 10, l. 334 | "(Speirs et al., 2001)" | "(Speirs et al., 2010)", or add the 2001 entry if a different paper is meant | S4 |
| KK-36 | p. 10, l. 338 | "centered ~9 kyrs BP" | "centered at ~9 kyr BP" | S4 |
| KK-37 | p. 10, l. 340 to 341 | "a weakening of South Westerlies Winds (SWW)" | "a weakening of the Southern Westerly Winds (SWW)" | S4 |
| KK-38 | p. 10, l. 341 | "Moreno et al. (2010); Lisé-" | "Moreno et al., 2010; Lisé-" | S4 |
| KK-39 | p. 10, l. 342 to 343 | "(Quake and Kaplan, 2017)" | "(Quade and Kaplan, 2017)" | S2, S4, SD |
| KK-40 | p. 10, l. 346 | "Fires co-emit mineral soil-dust particle" | "Fires co-emit mineral soil-dust particles" | S4 |
| KK-41 | p. 11, l. 354 | "Dust emission from PAP are primarily linked" | "Dust emissions from PAP are primarily linked" | S4 |
| KK-42 | p. 11, l. 365 | "(Gili et al., 2016) ." | "(Gili et al., 2016)." | S4 |
| KK-43 | p. 11, l. 366 | "the Darling sub-basin as the dominant source region" | "the Darling Basin (Table S2) as the dominant source region" | S2 |
| KK-44 | p. 11, l. 367 | "De Deccker et al. (2010)" | "De Deckker et al. (2010)" | S2, S4 |
| KK-45 | p. 11, l. 374 | "(post-7.5 kry BP)" | "(post-7.5 kyr BP)" | S4 |
| KK-46 | p. 12, l. 384 to 385 | "suggesting strengthened dust transport from southern Africa suggesting strengthened dust transport from southern Africa (Stuut et al., 2002)" | "suggesting strengthened dust transport from southern Africa (Stuut et al., 2002)" | S4, SD |
| KK-47 | p. 12, l. 396 | "but include few substantial inputs" | "but include a few substantial inputs" | S4 |
| KK-48 | p. 12, l. 399 | "likely reflect their low-frequency, high-magnitude nature of their dust emissions" | "likely reflect the low-frequency, high-magnitude nature of their dust emissions" | S4 |
| KK-49 | p. 12, l. 408 | "due to the limited number samples covering those periods" | "due to the limited number of samples covering those periods" | S4 |
| KK-50 | p. 13, l. 426 | "to receive dust from Patagonia dust brought in the mid-" | "to receive dust from Patagonia brought into the mid-" | S4 |
| KK-51 | p. 13, l. 427 | "located at the interior of EAP and the Indian Ocean sector" | "located in the interior of the East Antarctic Plateau (EAP) and the Indian Ocean sector" (EAP is not defined elsewhere) | ZF |
| KK-52 | p. 13, l. 428 | "from such mid-latitude air masses incursions" | "from such incursions of mid-latitude air masses" | S4 |
| KK-53 | p. 13, l. 439 | "(De Deccker et al., 2019;" | "(De Deckker, 2019;" (single-author entry, p. 17, l. 551) | S2, S4 |
| KK-54 | p. 14, l. 457 | "redirecting large portion of river catchment" | "redirecting a large portion of river catchments" | S4 |
| KK-55 | p. 14, l. 481 | "study on the EDML dust record showing similar shift" | "study on the EDML dust record showing a similar shift" | S4 |
| KK-56 | p. 16, l. 501 | "APPENDIX S. SUPPLENTARY DATA. Supplementary data to this article" | "APPENDIX S. SUPPLEMENTARY DATA. Supplementary data to this article are available online." | S4 |
| KK-57 | reference list, 18 entries with RTF codes printed on p. 16 to 22, first at p. 16, l. 528 (Bryant 2003), further at l. 553 to 556, 588, 590, 593, 606, 632, 645 to 648, 653 to 654, 693 to 694, 702 to 707, 710, 714 to 716, 742 to 747, 757 to 758, 795, 799, 817, 821, 826 to 828 | "471\uc0舑{}501. https://doi.org/10.1191/0309133303pp386ra\" | replace each code by its character (\uc0舑{} by an en dash, \uc0舗{} by a right single quote, \uc0\u237{} by í, \uc0\u233{} by é, \uc0\u241{} by ñ, \uc0\u176{} by °, other codes likewise) and delete the trailing backslash after each DOI; example "471 to 501" with an en dash in place of "to", followed by the DOI without backslash | S4 |
| KK-58 | p. 18, l. 630 to 632 | "Gaiero, D.M., Brunet, F., Probst, J.-L., Depetris, P.J., 2007." | delete the entry (not cited; "Gaiero, 2007" in l. 274 and l. 862 refers to the single-author entry), or cite it where intended | S4 |
| KK-59 | p. 20, l. 728 | "The EDC3 chronology for the EPICA Dome C ice core. Clim. Past." | "The EDC3 chronology for the EPICA Dome C ice core. Clim. Past 3, 485-497. https://doi.org/10.5194/cp-3-485-2007" | S4 |
| KK-60 | p. 20, l. 748 | "Environùental characterization" | "Environmental characterization" | S4 |
| KK-61 | p. 20, l. 763 | "Holland HD, Turkian KK (eds)" | "Holland HD, Turekian KK (eds)" (editor name confirmed in the EarthRef record of Rudnick and Gao, 2003) | ZF |
| KK-62 | p. 21, l. 800 (cited as "Sugden et al., 2009" in l. 266) | "Sudgen, D. E., McCulloch, R. D., Bory, A. J.-M., Hein, A. S., 2009." | "Sugden, D. E., McCulloch, R. D., Bory, A. J.-M., Hein, A. S., 2009." | S2, S4 |
| KK-63 | p. 22, l. 844 to 846 | "Yang, Y., Carey-Smith, T., & Turner, R. (2024)." | "Yang, Y., Carey-Smith, T., Turner, R., 2024." followed by title and "Atmospheric Science Letters 25, e1203. https://doi.org/10.1002/asl.1203"; bring Ding et al. 2011 (l. 584 to 585) and Gaiero et al. 2013 (l. 633 to 636) into the same style | S4 |
| KK-64 | p. 26, l. 857 to 858 (caption Figure 2) | "dust in ice cores (refs. Table S1, - open symbols)" | "dust in ice cores (open symbols; references in Table S4)" | S4, AB, SD |
| KK-65 | p. 26, l. 863 (caption Figure 2) | "Note that the SAF and AUS domain is more extended than showed in the Figure." | "Note that the SAF and AUS domains extend beyond the plotted area." | AB |
| KK-66 | p. 26, l. 865 to 866 (caption Figure 2) | "(ii) the isotopic fingerprint (Table S4) and elemental concentration of the PSAs end-members (Table S3)." | "(ii) the isotopic fingerprint and elemental concentration of the PSA end-members (Table S3)." | S4, AB, SD |
| KK-67 | p. 28, l. 875 (caption Figure 4) | "Histograms representing the contribution percentage difference" | "Bar charts of the difference in contribution (percentage points)" | AB |
| KK-68 | p. 28, l. 876 (caption Figure 4) | "periods for each PSA between EDC and EDML ice cores (Table S4)." | "periods for each PSA between EDC and EDML ice cores (Table S5)." | S4, AB, SD |
| KK-69 | Supp. p. 5 (caption Figure S3) | "between 2.852 to 33.699 kyr BP" | "between 2.852 and 33.699 kyr BP" | AB |
| KK-70 | Supp. p. 10 (Figure S5, y axis label) | "PAS EDC Contribution and PSA EDML Contribution ( in %)" | "PSA contribution to EDC and EDML (%)" | AB |
| KK-71 | Supp. p. 10 (Figure S5, panel AUS, lower right) | "x 1000" | delete the stray label (the axis is already in kyr) | AB |

#### Verification log

| Kennung | Check | Checked | Values | Result |
|---|---|---|---|---|
| PP-23 | P1 | Eq. 3 and 4 recomputed with Table S3 end-members and period means (PAP split by the Table S1 columns) | 87Sr/86Sr and εNd: Holocene 0.7101 and minus 4.99; YD 0.7094 and minus 5.39; ACR 0.7082 and minus 2.92; HS1 0.7076 and minus 1.56; LGM 0.7083 and minus 2.61; MIS3 0.7083 and minus 3.36; glacial values near the EDC LGM measurements of Table S4 | consistent with the pattern stated in l. 252 to 257; limits in GB-37, GB-14; disclosed: SAF and AUS domains cut (l. 863) |
| PP-24 | P3, P29 | Figure 2, axes and modelled points | x ticks every 0.001 (0.705 at 835.5 px, 0.710 at 1057.5 px), y ticks every 1; recomputed values fall on filled dots, for example 12227 yr BP (0.7274, minus 17.87) on the isolated yellow YD dot; all recomputed values inside the plotted range | no finding beyond GB-58 |
| PP-25 | P15 | quantitative statements in abstract, Section 4 and Section 5 against Tables S5 and S1 | Holocene AUS, PAP, SAF 23, 11, 11 (23.1, 11.0, 10.7) and LGM 10, 4, 6 (10.2, 3.6, 6.3); Holocene PAT and NZ 49 and 6 (49.0, 5.9); LGM SSA ~70 (69.3), AUS ~10; LGM PAT plus NZ ~79 (79.9), low latitude ~21 (20.1); EDML LGM NZ ~6 (6.2); PAT minimum near 10 kyr (binned 35.4 % at 10.0 to 10.5 kyr); PAT peaks about 9, 7 to 8 and after 6 kyr (69.8, 71.8, 61.7 % in 500-yr bins); PAT 50 to 55 % after 5 kyr (52.0); South Puna Early 2.3, Late 4.6 %; SAF Early 9.8, Late 11.6 % | deviations only in the findings listed for l. 276, 282, 295, 321, 357, 408, 421; disclosed limits not raised again except in GB-43 |
| PP-26 | P2, P3 | EDC minus EDML differences in Section 4.4 and Figure 4 against Table S5 | bars measured (Table S5 difference): PAT minus 13.9 (minus 13.7), +4.9 (+4.7), +6.5 (+6.4), +3.2 (+3.2), minus 8.1 (minus 8.0); AUS +12.4 (+12.3), minus 4.4 (minus 4.5), minus 7.3 (minus 7.4), +2.2 (+1.9); SAF minus 0.4, +6.5, minus 4.4, minus 5.2, minus 2.7; NZ LGM +7.8 (+8.0); HS1 largest difference 5.3 (text "not exceeding ~5%") | Figure 4 drawn from Table S5; deviations in GB-53 and GB-50 |
| PP-27 | P3, P24 | Figure S5, period zones and the shift between 15 and 14 kyr BP | smoothed EDC PAT 74.1 % at 14.3 kyr, 61.9 % at 14.0 kyr; EDML 60.1 % at 14.8 kyr, 49.4 % at 14.5 kyr, 36.6 % at 13.8 kyr | consistent with l. 445 to 446 |
| PP-28 | P3 | Figure S3 Puna peaks and Figure S1 markers | Puna raw peaks against Table S1: 29.8 (29.1 at 5850), 25.9 (25.7 at 10205), 26.0 (25.6 at 7833), 24.4 (25.0 at 3503), 24.7 (23.4 at 5657), 21.5 (20.7 at 6775); Figure S1 PAT panel 22 markers for 22 distinct coordinates | no finding beyond GB-61, GB-15 |
| PP-29 | P24 | Figure S2, timing of the flux decline | smoothed nssCa2+ flux falls from about 600 to below 50 between 18 and 14.7 kyr; δ18O rises from about 16 kyr; text l. 296 and l. 449 | consistent within reading at the page image |
| PP-30 | P4 | all cross-references to sections, figures, tables, equations and supplement items | sections 1 to 5 without gaps; Eq. 1 to 4 numbered and referenced; Figures 1 to 5 and S1 to S5, Tables S1 to S5 present and cited; correct targets for Figure S2 (l. 167, 296, 299, 312, 449), S3 (l. 355), S5 (l. 405, 409, 446, 450), Table S5 (l. 191, 216, 281, 295, 318, 326) | faulty targets in the minor corrections; order in GB-47 |
| PP-31 | P4 | 86 reference entries against all short citations in text, captions and supplement, both directions | all entries cited except Gaiero et al. 2007 (Chemical Geology); EPICA Community Members 2006 cited only in the caption of Figure S2; citations without entry: Gili et al. 2016, supplement sources; deviating year or spelling: Speirs 2001, Sudgen, Quake, De Deccker | findings GB-48, GB-22 and minor corrections |
| PP-32 | P4 | form of short citations ("et al." and "and" against author counts) | two-author citations correct (Grousset and Biscaye 2005, Fletcher and Moreno 2012, Neff and Bertler 2015, Quade and Kaplan 2017, Rudnick and Gao 2003 and others); single-author citations correct (Qu 2016, Gaiero 2007, Bryant 2003, Caldenius 1932); only De Deckker 2019 with "et al." | minor correction only; missing commas before years left to the optional citation style check |
| PP-33 | P15 | recommendations and outlook in Section 5 | Section 5 contains no recommendation for follow-up work | no finding beyond GB-56 |
| PP-34 | P16 | language and typesetting of p. 7 to 22 and captions p. 25 to 29 on page images | superscripts and subscripts in Eq. 3 and 4 and in 87Sr/86Sr printed correctly; "Lisé-/Pronovost" is a line-break hyphen; RTF codes in the reference list are printed, not extraction artefacts; mixed quotation marks («wet scavenging», "rainout") left as a style question | minor corrections as listed |

## Optional checks

| Area | What it needs | Responsible | Run |
|---|---|---|---|
| DOI resolution | one request per reference entry | `science-quellenapparat-pruefung` | no |
| Citation style | the name of the style | `science-zitierstil-harvard-ctr` or the journal's style rules | no |
| AI statement against publisher policy | the target publisher's policy | this review, on request | no |
| Relation to the authors' own prior work | the authors' prior work | this review, on request | no |
| Journal requirements | the target journal's author guidelines | this review, on request | no |
| Scientific accuracy | access to the sources of every checked statement | `science-faktenbeleg-pruefung`, `geo-frage-belegbasiert-klaeren` | no |

## Limits of this review

- Version reviewed: egusphere-2025-5046.pdf, 29 pages, SHA-256 f598b53d01e375844cfb549eb05b9a3407bb30cae553e603c125d5f14886c722; supplement egusphere-2025-5046-supplement.pdf, 22 pages, SHA-256 759cfa14195948f5772d3d6d696081932424f4296e51c812415527ed3b108ea6.
- Sources not readable in full: Vanderstraeten et al. (2023), Delmonte et al. (2008, 2017), Engelbrecht et al. (2019), Siggaard-Andersen et al. (2007), Marino et al. (2008), Vallelonga et al. (2010), Coppo et al. (2022), Neff and Bertler (2015), Delmonte et al. (2004, Earth-Science Reviews), Davies et al. (2020) and Krätschmer et al. (2022) were read as abstract or bibliographic record only; Koffman et al. (2021) was not reachable. The Table 5 values of Krätschmer et al. (2022) rest on the reading of instance S1.
- Findings with status assumption (at least for one partial statement): 14 of 62.
- Optional checks run: 0 of 6.
- Merging: the six instances delivered 84 substantive findings, 93 minor corrections and 42 verification logs. No finding lacked a mandatory field, so none was returned or discarded on that ground (0 discarded findings). Duplicates were merged: the 84 findings became 57 findings of this report (two bundled findings of S4 and SD were split over the single number findings they contain), 10 minor corrections were absorbed into findings, the remaining 83 minor corrections became 64, and the 42 verification logs became 34 (six merged, two folded into findings). Of the notes outside the checklists, 5 became findings and 7 became minor corrections with source ZF after checking against the manuscript; 7 notes were not adopted (verworfen): the "14 concentrations" in l. 70 (correct as a general statement on REE patterns), the rounding of Kok et al. (2021) in l. 322 to 323 (the source rounds to about 10 % itself), the list of partly readable sources (a limit, not a finding), the missing graphic on Supp. p. 5 (the panels follow on p. 6), the single Antarctic sample at 3654 yr (the statement in l. 330 holds for the mean), the end of the HS1 zone in Figure S5 at 17.88 kyr (within reading tolerance of the purpose), and the 9-sample moving average across the sampling gap (the caption states the method correctly).
- Line numbers were taken from the printed margin numbers; the extracted text counts lines per page, so figure captions on p. 25 have no margin number and are located by page. Quotations containing dashes were shortened to fragments without them.
