# Review report: Quantifying Southern Hemisphere dust sources during the Last Glacial-Interglacial Transition using rare earth elements in the EPICA Dome C ice core

| Field | Value |
|---|---|
| Manuscript | Boxho, S., Vanderstraeten, A., Mattielli, N., Laruelle, G.G., Bory, A., Gabrielli, P., Bonneville, S. (2025): Quantifying Southern Hemisphere dust sources during the Last Glacial-Interglacial Transition using rare earth elements in the EPICA Dome C ice core. EGUsphere preprint egusphere-2025-5046, https://doi.org/10.5194/egusphere-2025-5046 |
| Version reviewed | egusphere-2025-5046.pdf, 29 pages, SHA-256 f598b53d01e375844cfb549eb05b9a3407bb30cae553e603c125d5f14886c722; supplement egusphere-2025-5046-supplement.pdf, 22 pages, SHA-256 759cfa14195948f5772d3d6d696081932424f4296e51c812415527ed3b108ea6 |
| Date | 2026-10-18 |
| Language | English |
| Review instances | Segments 1 to 4, figures, study design. The six review instances ran as separate agents without shared context; the consolidation (steps 4 to 7) ran as a further agent and re-checked quotations and locations against the page images. |

Line numbers follow the printed margin numbers of the manuscript (every fifth line printed, lines in between counted). The supplement has no line numbers; locations there are given by page, table, row, column, figure and panel.

## Summary

The manuscript is a method application with a descriptive palaeo reconstruction. The authors apply their DEPOT unmixing model (constrained non-negative least squares in MATLAB, 2000 Monte Carlo runs per sample, median as estimate) to a published EPICA Dome C (EDC) rare earth element (REE) data set of 294 dust samples (Gabrielli et al., 2010). After removing 15 incomplete patterns and gadolinium, 279 UCC-normalised 13-REE patterns are fitted against a database of 217 source patterns in seven potential source areas (PSA: PAT, CWA, PAP, SAF, AUS, NZ, ANT); 241 samples with a fit correlation of R of at least 0.67 form the record from 33.7 to 2.9 kyr BP. Patagonia supplies about 65 to 75 % of the dust during MIS3, the LGM and HS1 and 49 % in the Holocene, while Australia rises from 10.2 % (LGM) to 23.1 % (Holocene) and Puna-Altiplano from 3.6 % to 11.0 % (Table S5). The record is checked against Sr and Nd isotope values back-calculated from the modelled contributions (Eq. 3 and 4) and published ice core isotope data (Table S4), compared with the EDML provenance record of Vanderstraeten et al. (2023), and the shift near 14.5 kyr BP is attributed to Patagonian shelf submersion and river reorganisation.

## Strengths

1. The derived tables close arithmetically: the sample balance 294 minus 15 minus 38 = 241 matches Table S1 row for row, Table S5 is reproduced from Table S1 to within 0.05 points for every period, and the values in Section 3 match Table S5 to within 0.5 points, so a reader can recompute every period mean from the supplement (PP-20, PP-21, PP-22, PP-23).
2. The Sr and Nd back-calculation (Eq. 3 and 4) is an independent check on the REE apportionment; recomputed from Tables S1, S3 and S5 it reproduces the stated direction of change from glacial to Holocene isotope signatures, although the measured comparison data are mostly not from EDC (PP-28, GB-38).
3. The methods section discloses the main limits of the data where the method is introduced (sampling gap 21.7 to 27.3 kyr BP, removal of Gd, incomplete acid leaching, 38 excluded samples, tentative ACR and YD results), so the reader can see where the record is thin (PP-09, PP-20).
4. The EDC and EDML contrast for the LGM and HS1 (NZ plus 8.0, PAT minus 8.0 points in the LGM; HS1 differences up to 5.3 points) agrees between text, Table S5 and Figure 4 and holds when the EDC LGM window is restricted to the stated overlap (PP-31, PP-32, PP-33, PP-34).

## Weaknesses

1. The accuracy of the unmixing is not established: the isotope validation uses mostly non-EDC data, there is no recovery test with known mixtures, the Monte Carlo spread is computed but not reported, and the stated significance of the fit threshold cannot be reproduced; the authors should add a synthetic-mixture recovery test, report per-sample uncertainty, restrict the validation to EDC data and derive the threshold from a null distribution that respects the fit (GB-38, GB-11, GB-19, GB-21).
2. Several interpretations go beyond what relative shares can show: rising low-latitude shares are read as increased input without the announced absolute fluxes, a mechanism is said to be demonstrated by a timing coincidence, larger Holocene variability is not separated from sampling and fit effects or from the exclusion of 38 Holocene samples, and the dated Altiplano onset conflicts with Table S1; the authors should report PSA fluxes, phrase causal links as consistent with, and test variability and exclusion effects before interpreting them (GB-20, GB-52, GB-41, GB-25, GB-45).
3. The end-member database and the comparison record are not documented well enough to trust differences between sources and sites: the Antarctic patterns in Table S2 are not UCC-normalised and number 4 instead of 5, two Australian patterns are duplicated under different basins, one SAF value looks like an entry error, and the EDML values used differ from the published EDML record and come from another model configuration; the authors should correct Table S2, run sensitivity tests on the database, and recompute EDML with the present configuration (GB-16, GB-15, GB-24, GB-09).
4. Many statements in the text do not match the authors' own tables and figures, and the inputs needed to repeat the analysis are missing; the authors should reconcile the numbers with Tables S1 and S5 (sub-regional peaks, NZ share, combined shares, swapped ACR and YD values, Holocene comparison window, YD sample count, figure labels) and deposit code, correction factors, input data and full references (GB-31, GB-30, GB-40, GB-39, GB-49, GB-50, GB-48, GB-33, GB-57, GB-35, GB-17, GB-14, GB-54, GB-46).

## Findings by segment

### Segment 1: Abstract, introduction, state of research (pp. 1 to 3)

#### Substantive findings

**GB-01 The time span of the record is given with three different young limits and two different old limits.**

| Field | Content |
|---|---|
| Check | P2 |
| Location | p. 1, l. 18; p. 3, l. 90 to 91; p. 6, l. 182 and l. 187; p. 9, l. 303 to 304; supplement p. 11 and p. 15, Table S1, first and last row |
| Quotation | "from 33.7 to 2.9 kyr BP" (l. 18); "during the LGIT from 33.6 kyr to 2.8 kyr BP" (l. 90 to 91); "(from 14.5 kyr BP until 2.7 kyr BP)" |
| Concern | Table S1 runs from 2852 to 33699 yr. Rounded, that is 2.9 to 33.7 kyr BP (Abstract, l. 182); truncated, it is 2.8 to 33.6 kyr BP (l. 90 to 91 and the Holocene bound in l. 187). The value 2.7 kyr BP in l. 304 fits neither convention. The minor correction proposed by instance S4 for l. 303 to 304 is included here. |
| Suggestion | Use one convention throughout (2.9 to 33.7 kyr BP, as in the Abstract) in l. 90 to 91, l. 187, l. 304 and the row labels of Table S5. |
| Status | verified |
| Severity | minor |
| Source | S3, S4 |

**GB-02 The Abstract claims a first quantification of Southern Hemisphere source contributions without qualification and without any account of a literature search, while the manuscript itself cites an earlier quantitative estimate.**

| Field | Content |
|---|---|
| Check | P28 |
| Location | p. 1, l. 19 to 20; p. 3, l. 74 to 76; p. 7, l. 220 to 221; p. 12, l. 403; p. 14, l. 472 to 473; counter-evidence p. 9, l. 277 to 279 |
| Quotation | "we quantify for the first-time contributions from key Southern Hemisphere dust sources" |
| Concern | The priority claims in l. 220, l. 403 and l. 472 are qualified (continuous, at EDC, REE-based) and are plausible in that form; two own searches found no earlier continuous quantitative provenance record at EDC (PP-01). The Abstract claim in l. 19 to 20 is not qualified. The manuscript itself reports a quantification for East Antarctica: "Coppo et al. (2022) estimated LGM dust composition over EA as 64% from SSA" with shares for Antarctica, AUS, SAF and NZ (l. 277 to 279), and a Holocene estimate (l. 324 to 328). Outside ice cores, Longman et al. (2022) quantified Southern Hemisphere source shares for the LGM and the Holocene with mixing models (GB-07). No database, search terms, period or search date are given for any of the five priority claims. |
| Suggestion | Qualify the Abstract sentence in l. 19 to 20 as in l. 220, for example "we provide the first continuous, REE-based quantification of Southern Hemisphere dust source contributions at EDC", and name in the Introduction the earlier quantitative estimates (Coppo et al., 2022; Longman et al., 2022) that the new record improves on. |
| Status | verified (absence of a search description; Coppo et al. as quoted in the manuscript; Longman et al., 2022, in the source); inferred for the Coppo et al. (2022) shares in the source, full text not readable |
| Severity | moderate |
| Source | S1 |

**GB-03 The range of 20 to 40 ppmv for the CO2 drawdown by dust iron fertilisation is not found in the two cited sources.**

| Field | Content |
|---|---|
| Check | P13 |
| Location | p. 2, l. 40 to 42 |
| Quotation | "are modelled to have lowered the atmospheric pCO2 by ~20 to 40 ppmv, accounting for a significant portion of the glacial-interglacial pCO2 difference (Lambert et al., 2015; Lambert et al., 2021)" |
| Concern | Lambert et al. (2015) give "a weak reduction of <10 ppm" on centennial timescales followed by a further about 10 ppm over millennial timescales, 20 ppm in the Key Points. Lambert et al. (2021) give "between 12 and 29 ppmv" for global-scale iron fertilisation, 18.5 ppmv for the four HNLC regions and a model spread of 8.9 to 33.1 ppmv (their Table 2). The upper bound of 40 ppmv appears in neither source and exceeds the largest value in them by 40 minus 33.1 = 6.9 ppmv; the lower bound of 20 ppmv lies at the upper end of the 2021 central range. The statement cannot be traced to the cited sources; this concerns traceability, not a result of the study. |
| Suggestion | Replace the range in l. 41 by the values of the cited sources, for example "by about 10 to 30 ppmv (Lambert et al., 2015, 2021)", or cite the study that gives 40 ppmv. |
| Status | verified (Lambert et al., 2015, abstract and Key Points; Lambert et al., 2021, full text of the open repository copy) |
| Severity | moderate |
| Source | S1 |

**GB-04 The statement on the role of the Southern Hemisphere westerlies is supported by a regional downscaling study whose abstract does not address the westerlies.**

| Field | Content |
|---|---|
| Check | P13 |
| Location | p. 2, l. 51 to 52 |
| Quotation | "advancing our understanding of changes in Southern Hemisphere westerly winds, which play a crucial role in atmospheric and oceanic circulation (Engelbrecht et al., 2019)" |
| Concern | Engelbrecht et al. (2019) downscale LGM climate over southern Africa; their abstract mentions an extension in the northward reach of frontal rainfall but makes no statement on the westerlies or their role in atmospheric and oceanic circulation. The full text was not readable. The claim itself is uncontested; the reference does not appear to carry it as cited. Is there a passage in Engelbrecht et al. (2019) that makes this statement? |
| Suggestion | Support the sentence in l. 51 to 52 with a review of Southern Hemisphere westerly dynamics, for example Fletcher and Moreno (2012), already in the reference list, or give the page of Engelbrecht et al. (2019) that makes the statement. |
| Status | inferred (abstract only) |
| Severity | minor |
| Source | S1 |

**GB-05 Aarons et al. (2017), an East Antarctic REE and Sr-Nd dust record across the same transition, supplies most of the measured validation data but is not discussed in the state of research.**

| Field | Content |
|---|---|
| Check | P14 |
| Location | p. 2 to 3, l. 53 to 98 (state of research and aims); p. 3, l. 93 to 94 (aim 2); supplement p. 21, Table S4, column "Reference", 18 rows "Taylor Glacier" |
| Quotation | "(2) confronting and validating the EDC results from our REE pattern-based model against Sr-Nd isotopic data published in the literature" |
| Concern | Aarons et al. (2017) characterise dust from the Taylor Glacier horizontal ice core across the last glacial-interglacial transition with Sr and Nd isotopes, grain size, trace element and REE concentrations and attribute the glacial dust mainly to southern South America (dataset record abstract). It is the nearest earlier East Antarctic LGIT record with the same element group, and 18 of the 35 measured isotope rows of Table S4 come from it (supplement page image p. 21), including all ACR and YD values. The Introduction does not say what the REE data of Aarons et al. (2017) showed about provenance and how the present record goes beyond it. The missing reference entry itself is part of GB-46. |
| Suggestion | Discuss Aarons et al. (2017) in the Introduction after l. 74 as an earlier REE and isotope record of the LGIT in East Antarctica: Aarons, S.M., Aciego, S.M., Arendt, C.A., Blakowski, M.A., et al., 2017. Dust composition changes from Taylor Glacier (East Antarctica) during the last glacial-interglacial transition: A multi-proxy approach. Quaternary Science Reviews 162, 60 to 71. https://doi.org/10.1016/j.quascirev.2017.03.011 |
| Status | verified (use in Table S4 on the page image; absence from the reference list); inferred for the content and the full author list, taken from the dataset record and a partial author listing |
| Severity | moderate |
| Source | S1 |

**GB-06 The factor of up to 25 between glacial and interglacial dust flux is cited to two papers whose readable text does not contain it.**

| Field | Content |
|---|---|
| Check | P13 |
| Location | p. 2, l. 62 to 63 |
| Quotation | "dust fluxes are up to 25 times lower than LGM fluxes (e.g. Delmonte et al., 2008; Delmonte et al., 2017)" |
| Concern | The abstracts of Delmonte et al. (2008), on Sr and Nd provenance of glacial dust at EDC and Vostok, and Delmonte et al. (2017), on dust size at Dome B, contain no flux ratio; their full texts were not readable. Lambert et al. (2008), already cited in l. 36 and l. 46, gives "the observed approximately 25-fold increase in glacial dust flux over all eight glacial periods" at EDC. The number is consistent with the literature; the citation probably points to the wrong papers. |
| Suggestion | Cite Lambert et al. (2008) for the factor in l. 63, or give the page of Delmonte et al. (2008) or (2017) where the factor is stated. |
| Status | inferred (full texts of Delmonte et al., 2008, 2017, not readable; Lambert et al., 2008, abstract verified) |
| Severity | minor |
| Source | S1 |

**GB-07 Longman et al. (2022) quantified the shift from South American to Australian dust between the LGM and the Holocene with mixing models and is not cited.**

| Field | Content |
|---|---|
| Check | P14 |
| Location | p. 2, l. 67 to 68; p. 1, l. 19 to 20; p. 3, l. 69 to 76; p. 10, l. 315 to 328 |
| Quotation | "All of the above-mentioned factors render the quantification of dust source contribution complex to achieve using isotopic fingerprinting." |
| Concern | Longman et al. (2022) applied Bayesian mixing models to Pb and Nd isotope data of South Pacific sediments and report that "During the LGM, a higher proportion (mean 53%) of dust entering the South Pacific was South American in origin", with Australian contributions "lower during the LGM (mean 38%) than Holocene (mean 55%)". This is a quantitative isotope-based apportionment of the same sources across the same change, on the oceanic pathway upwind of East Antarctica. It qualifies the statement in l. 67 to 68, bears on the priority claim in l. 19 to 20 (GB-02) and offers a further comparison for the Holocene rise of AUS from 10 to 23 % at EDC (l. 316 to 318). Not in the reference list. |
| Suggestion | Cite and discuss in the Introduction after l. 68 and in Section 4.3 after l. 328: Longman, J., Struve, T., Pahnke, K., 2022. Spatial and temporal trends in mineral dust provenance in the South Pacific: Evidence from mixing models. Paleoceanography and Paleoclimatology 37, e2021PA004356. https://doi.org/10.1029/2021PA004356 |
| Status | verified (open access full text read) |
| Severity | moderate |
| Source | S1 |

**GB-08 The Introduction describes earlier REE records as multi-decadal, while one cited source says decadal to centennial and the manuscript gives about 100 years for the reused EDC data set.**

| Field | Content |
|---|---|
| Check | P13 |
| Location | p. 3, l. 72 to 74; p. 4, l. 109 to 111 |
| Quotation | "Previous studies using REE patterns in Antarctic ice cores (e.g., Gabrielli et al., 2010; Wegner et al., 2012) achieved multi-decadal resolution but could not fully resolve dust provenance." |
| Concern | Wegner et al. (2012) describe their EDML record as "at decadal to centennial resolution". For the Gabrielli et al. (2010) EDC data set, which this study reuses, the manuscript gives an average spacing of about 100 years with a range of 60 to 140 years (l. 110 to 111), which is centennial on average. "Multi-decadal" overstates the resolution that the new record, built on the same data, can offer. |
| Suggestion | Replace "achieved multi-decadal resolution" in l. 73 by "achieved decadal to centennial resolution". |
| Status | verified (Wegner et al., 2012, abstract; manuscript l. 110 to 111) |
| Severity | minor |
| Source | S1 |

**GB-09 The EDML values used for the EDC and EDML comparison differ from the published EDML record cited in the Introduction, and the two records were unmixed with different model configurations.**

| Field | Content |
|---|---|
| Check | P13, P7 |
| Location | p. 3, l. 77 to 82; p. 5, l. 144 to 145; p. 9, l. 288; p. 12 to 13, l. 403 to 424; p. 13 to 14, l. 444 to 450; p. 1, l. 28 to 29; Figure 4 (p. 28); supplement p. 22, Table S5, EDML block; Figure S5 |
| Quotation | "up until ~14.5 kyr BP when a sudden drop in Patagonian contribution (below 50% on average) was evidenced" (l. 79 to 80); "In Vanderstraeten et al. (2023), n was equal to 14 but is only 13 in the present study because of the exclusion of Gd." |
| Concern | The Introduction reproduces Vanderstraeten et al. (2023) correctly (PP-07): Patagonia about 68 % before 14.5 kyr BP and below 50 % on average after it, Southern Africa 21 to 23 % after 14.5 kyr BP, New Zealand 3 to 4 % before, Patagonia about 50 % in the Early Holocene, from 207 source patterns. The EDML values actually compared (Table S5, checked on the page image) do not match: PAT is 62.5 (ACR), 58.4 (YD) and 62.7 (Early Holocene), so no period after 14.5 kyr BP is below 50 %; SAF after 14.5 kyr BP is 12.4, 8.2 and 11.2 %; NZ in the LGM is 6.2 %, which l. 288 repeats as the published result. The comparison depends on this: with Table S5, EDC Holocene PAT minus EDML Early Holocene PAT is 49.0 minus 62.7 = minus 13.7 (the "-14%" of l. 424); with the published value of about 50 % it would be about minus 1. With published SAF values of 21 to 23 %, EDC minus EDML for SAF after 14.5 kyr BP would be about minus 6.4 to minus 15.0 points instead of minus 4.4, plus 6.4 and minus 1.4. At the same time the manuscript states that EDML was unmixed with 14 REE and EDC with 13 (l. 144 to 145), the published EDML work used 207 source patterns against 217 here, and the EDML chronology is not named although l. 444 to 446 compare the timing of changes in both cores (EDC on EDC3, l. 111). Two readings remain, and both need action: (a) EDML was recomputed for this study; then the manuscript does not say so, and l. 77 to 82 and l. 288 cite values that are not the ones used; (b) the EDML values were taken over; then Table S5 does not match their source, and the differences in l. 417 to 424, Figure 4 and the Abstract statement on EDML and Southern Africa (l. 28 to 29) mix site effects with differences in REE set and database. Which reading applies? Aim (4) of the study rests on this comparison, hence the grade. |
| Suggestion | State in Section 2 and in the caption of Table S5 whether and how the EDML contributions were recomputed (REE set, database, Monte Carlo settings). Base Table S5, Figure 4 and Figure S5 on one configuration for both cores, report recomputed EDML values in l. 77 to 82 and l. 288 next to the published ones, name the EDML age scale and put both records on one chronology before comparing timing. |
| Status | verified (published values in the abstract of Vanderstraeten et al., 2023; Table S5 on the page image; l. 144 to 145; absence of the EDML chronology); inferred (differences computed); assumption (which reading applies, asked as a question) |
| Severity | major |
| Source | S1, SD |

#### Minor corrections

| Code | Location | Quotation | Replacement | Source |
|---|---|---|---|---|
| KK-01 | p. 1, l. 15 | "Dust deposits in ice cores provides a valuable archive" | "Dust deposits in ice cores provide a valuable archive" | S1 |
| KK-02 | p. 1, l. 19 | "we quantify for the first-time contributions" | "we quantify for the first time the contributions" (wording of the claim itself see GB-02) | S1 |
| KK-03 | p. 1, l. 20 | "During the Marine isotope 3 (MIS3)" | "During Marine Isotope Stage 3 (MIS3)" | S1 |
| KK-04 | p. 1, l. 23 to 24 | "sources - Australia, Southern Africa, and the Puna-Altiplano - culminating" | "sources (Australia, Southern Africa and the Puna-Altiplano), culminating" | S1 |
| KK-05 | p. 1, l. 27; p. 3, l. 77 (EDML is never expanded in the text) | "Comparison with the EDML ice core" | "Comparison with the EPICA Dronning Maud Land (EDML) ice core" | ZF |
| KK-06 | p. 2, l. 39 | "High Nutrients Low Chlorophyll (HNLC)" | "High-Nutrient, Low-Chlorophyll (HNLC)" | S1 |
| KK-07 | p. 2, l. 40 to 41 | "Enhanced iron delivery by atmospheric dust during glacial periods are modelled" | "Enhanced iron delivery by atmospheric dust during glacial periods is modelled" | S1 |
| KK-08 | p. 2, l. 48 to 49 | "(Qu, 2016; Shi et al., 2009, Shi et al. 2011, Shi et al. 2015)" | "(Qu, 2016; Shi et al., 2009, 2011, 2015)" | S1 |
| KK-09 | p. 2, l. 49 | "the contributions of individual PSA is essential" | "the contributions of individual PSAs is essential" | S1 |
| KK-10 | p. 2, l. 55 to 56 | "essential to the process of source identification, these PSAs serve as end-members" | "essential to the process of source identification; these PSAs serve as end-members" | S1 |
| KK-11 | p. 2, l. 62 | "high altitude site such as EDC where dust fluxes is low" | "high-altitude sites such as EDC, where dust fluxes are low" | S1 |
| KK-12 | p. 3, l. 70 to 71 | "the 14 concentrations/observations contain a lot more discriminative information than REE ratio" | "the 14 REE concentrations contain considerably more discriminative information than REE ratios" | S1 |
| KK-13 | p. 3, l. 88 | "we applied our ‘DEPOT’ model - to the REE pattern dataset measured - in the EPICA Dome C" | "we applied our DEPOT model to the REE pattern dataset measured in the EPICA Dome C" | S1 |
| KK-14 | p. 3, l. 90 | "in the Indian Ocean sector of the East Antarctica" | "in the Indian Ocean sector of East Antarctica" | S1 |

#### Verification log

| Code | Check | Checked | Values | Result |
|---|---|---|---|---|
| PP-01 | P28 | Priority and gap claims l. 19 to 20, l. 74 to 76, l. 220 to 221, l. 403, l. 472 to 473 (S1); Gili et al. (2022), cited l. 236 and l. 381, as possible quantitative precedent | No search description anywhere in text, supplement or statements. Two own searches (EDC quantitative apportionment; Holocene EDC Sr-Nd mixing proportions), publisher and follow-up journal pages excluded: no earlier continuous quantitative record at EDC. Gili et al. (2022): Namibian source characterisation, mixing discussed qualitatively, no own shares, quotes DustCOMM (about 70 % SSA, 20 % AUS, 10 % SAF). Disclosed limit: ACR and YD tentative (l. 407 to 409), not relevant here | qualified claims stand; unqualified Abstract claim in GB-02 |
| PP-02 | P13 | l. 36 and l. 46 (Lambert et al., 2008) and the 25-fold flux factor (S1) | Lambert et al. (2008), abstract: approximately 25-fold increase in glacial dust flux over all eight glacial periods at EDC; dust flux related to source conditions and transport | no finding for l. 36 and l. 46; l. 63 see GB-06 |
| PP-03 | P14 | Positioning of the contribution against work on quantitative dust provenance in East Antarctica across the LGIT (S1) | Four searches; candidates: Aarons et al. (2017), not in the list (GB-05); Longman et al. (2022), not in the list (GB-07); Vallelonga et al. (2010), Quaternary Science Reviews 29, 247 to 255, https://doi.org/10.1016/j.quascirev.2009.06.019, Pb isotopes at EDC, supports the motivation in l. 60 to 68 without limiting the contribution (optional citation); Vanderstraeten et al. (2023), Gabrielli et al. (2010), Wegner et al. (2012), Koffman et al. (2021), Paleari et al. (2019), Delmonte et al. (2020) in the list; an earlier presentation of the same work found and not used | two findings (GB-05, GB-07) |
| PP-04 | P10 | Mapping of named gaps (l. 59 to 93) to research questions RQ1 to RQ4 (l. 91 to 98) (SD) | Isotope limitations (l. 59 to 68) to RQ1 and RQ2; unresolved REE provenance (l. 73 to 74) to RQ1; Holocene without consensus (l. 92 to 93) to RQ1; spatial variability to RQ4; RQ3 follows from the EDML hypothesis (l. 83 to 87); each question has a gap and each gap a question | no finding; design capacity see GB-38, GB-52, GB-09, GB-50 |
| PP-05 | P18 | Principles the manuscript states for others, applied to itself (SD) | l. 64 to 67 argue that isotopes cannot discern multiple sources when fields overlap; Section 4.1 validates with isotopes of PSA whose fields overlap in Figure 2 (PAT, NZ, CWA, S-Puna), used qualitatively; data availability principle covered by GB-54; disclosed: overlap of SAF and AUS domains (caption l. 863) | no separate finding (covered by GB-38) |
| PP-06 | P13 | "could not fully resolve dust provenance" (l. 73 to 74) against Wegner et al. (2012), abstract (S1) | Record 26600 to 7500 yr BP; uniform composition before 15000 yr BP, dominated by a South American source; after 15000 yr BP Australia and New Zealand relatively more important; qualitative attribution without shares | statement fair; resolution wording in GB-08 |
| PP-07 | P13 | Statements on the authors' EDML record, l. 77 to 87, against the abstract of Vanderstraeten et al. (2023) (S1; re-read in the consolidation) | Source: Patagonia about 68 %, Australia 14 to 15 %, Southern Africa about 9 %, New Zealand 3 to 4 %, Puna-Altiplano 2 to 3 % before 14.5 kyr BP; after it Patagonia below 50 % on average, Southern Africa 21 to 23 %, Australia 13 to 21 %, Puna-Altiplano 4 to 10 %; Early Holocene highly variable, Patagonia about 50 %; 207 source patterns, 386 of 398 samples unmixed | Introduction reproduces the source correctly; conflict with the EDML values used in GB-09 |
| PP-08 | P13 | "the Holocene for which there is no consensus (e.g. Paleari et al., 2019; Coppo et al., 2022; Delmonte et al., 2007)" (l. 92 to 93) (S1) | Paleari et al. (2019): Holocene dust compatible with Pampean and Patagonian provenance plus subtropical South American contribution; Coppo et al. (2022): combined southern South America and Australia, no percentages in the abstract, full text not readable; Delmonte et al. (2007) not read | statement holds |

### Segment 2: Materials and methods, supplement Table S2, Figures S1 and S2 (pp. 3 to 5; supplement pp. 1 to 4, 16 to 19)

#### Substantive findings

**GB-10 Six new SAF source samples marked "this study" enter a database described as literature-based without any description, and their location data contradict their names and coordinates.**

| Field | Content |
|---|---|
| Check | P19, P38 |
| Location | p. 4, l. 105; p. 4, l. 126 to 131; supplement p. 17, Table S2, Southern Africa block, rows EtoshaL1 to EtoshaL4, SuksesL and Sossusvlei, columns "Reference", "Location", "Lattitude", "Longitude"; supplement p. 17, Table S2, row Darling12, column "Longitude"; p. 12, l. 385 to 398 |
| Quotation | "and literature reported patterns from known potential source areas (PSA) across the Southern" |
| Concern | Six of 23 SAF patterns (26 %) are marked "this study". Their sampling, size separation (below 5 µm), digestion and measurement are not described, so they are primary data of unknown method inside a database the text calls literature-based. Their metadata are inconsistent (supplement page image p. 17): all six carry the location "Etosha Pan", including "Sossusvlei" at 24.76 S and "SuksesL" at 21.059 S, while the Etosha Pan rows of Li et al. (2020) in the same block lie at 18°53' to 19°02' S. All six give western longitudes, while every other SAF row gives eastern longitudes (13°29' E to 25°59' E). In the AUS block, Darling12 gives 138°17'6.00" E, while Darling11 at the same latitude lies at 144°17'6.00" E and the other Darling rows between 141.8° E and 148.6° E. Section 4.3 (l. 385 to 398) assigns SAF contributions to the Etosha, Makgadikgadi and Namibian coast systems; to which system Sossusvlei and SuksesL were counted cannot be determined. |
| Suggestion | Add to Section 2 a paragraph on the six new SAF samples (sites, sampling, size fraction, digestion, instrument, blanks, reference materials) or cite where they are described; correct names and longitude hemispheres of the six rows and the longitude of Darling12 in Table S2; state to which sub-system each SAF sample is assigned in Section 4.3. |
| Status | verified (Table S2 on the page image; Methods text) |
| Severity | moderate |
| Source | S2, SD |

**GB-11 No test estimates how well the unmixing recovers known source mixtures in the present configuration.**

| Field | Content |
|---|---|
| Check | P32 |
| Location | p. 4, l. 106 to 107; p. 3, l. 93 to 94; p. 5, l. 171 to 172; p. 8, l. 258 to 260 |
| Quotation | "A detailed description of the methodology is available in Vanderstraeten et al. (2023)." (l. 106 to 107); "supports the robustness of our DEPOT algorithm" |
| Concern | The manuscript calls its results validated and robust, but the only check is the qualitative isotope comparison (GB-38). There is no recovery test with mixtures of known composition for the present setting (13 REE, 217 source patterns, Holocene noise levels), no estimate of missed sources (a real source returned as zero) or spurious sources, and no leave-one-out test. Whether Vanderstraeten et al. (2023) hold such a test is not stated, and their settings differ (14 REE, 207 patterns; GB-09). |
| Suggestion | Add to Section 2 a recovery test: build synthetic mixtures from source patterns with known proportions (including ANT, CWA and NZ), add noise at the 2 to 10 % analytical level and at the Holocene concentration level, run DEPOT with 2000 Monte Carlo simulations, and report per PSA the mean bias and the rates of missed and spurious sources; alternatively leave each source pattern out, use it as target and report how often its own PSA is recovered. |
| Status | verified (absence of such a test in the manuscript and supplement) |
| Severity | major |
| Source | SD |

**GB-12 The stated spacing of 60 to 140 years between adjacent samples is contradicted by the ages in Table S1.**

| Field | Content |
|---|---|
| Check | P23, P2 |
| Location | p. 4, l. 109 to 111; supplement pp. 11 to 15, Table S1, column "Time [yr]" |
| Quotation | "with an average temporal resolution of approximately 100 years, ranging from 60 to 140 years between adjacent samples" |
| Concern | The average spacing matches: (33699 minus 2852)/293 = 105.3 yr. The 241 samples of Table S1 are a subset of the 294 described, and removing samples can only widen gaps, so every gap in Table S1 should be at least 60 years. Table S1 has 77 adjacent gaps below 60 years, for example 16 yr (10495 to 10511), 17 yr (10205 to 10222) and 18 yr (10029 to 10047), and four duplicated ages with different compositions (3559, 10511, 12841, 28709 yr). At the other end, 60 of 236 spacings between distinct ages exceed 140 years, the largest 2280 yr (23104 to 25384). Possible resolutions: (a) "60 to 140" describes typical, not extreme spacing; (b) the ages in Table S1 come from another age model or rounding; (c) the duplicated ages are replicates of one depth interval, which would then not be independent samples in the period means (two fall in the YD, GB-48). Which applies? |
| Suggestion | Add sample depths (top and bottom) to Table S1, correct the spacing statement in l. 110 to 111 so that it describes the retained record, and state how samples with the same age are treated in Table S5. |
| Status | verified (ages in Table S1); inferred (gap counts computed); assumption (resolutions, asked as a question) |
| Severity | moderate |
| Source | S3, SD |

**GB-13 Period boundaries are taken from the AICC2012 chronology paper while the sample ages are on EDC3, and the transfer is not stated.**

| Field | Content |
|---|---|
| Check | P9 |
| Location | p. 4, l. 111; p. 6, l. 183 to 188 |
| Quotation | "The age model follows the EDC3 chronology (Parrenin et al., 2007)." |
| Concern | The period means (Table S5, Figures 3 and 4) depend on where the boundaries fall. With samples every 60 to 300 years near the ACR and YD, a shift of a boundary by a few centuries moves samples between periods. The manuscript does not say whether the boundaries from Veres et al. (2013) (l. 188) were transferred to EDC3 or applied as AICC2012 ages to an EDC3 record. Were the boundaries converted? |
| Suggestion | State in Section 3 on which age scale the boundaries are applied; if they are AICC2012 ages, transfer them to EDC3 (or the data to AICC2012) and report whether any sample changes period. |
| Status | verified (both citations); assumption (size of the offset, asked as a question) |
| Severity | moderate |
| Source | SD |

**GB-14 The element-specific correction factors are neither given nor traced to their samples, and the cited source does not obviously supply them.**

| Field | Content |
|---|---|
| Check | P7, P12 |
| Location | p. 4, l. 118 to 124; p. 5, l. 157 to 158 |
| Quotation | "we applied cfi derived from parallel measurements of fully digested EDC samples to obtain total REE concentrations" |
| Concern | One set of cf_i corrects the leaching data of all 279 samples from 2.9 to 33.7 kyr BP and enters every Monte Carlo run with its variability (l. 157 to 158), but no value, spread or number of digested samples is given, and their ages are not stated. Partial dissolution depends on the minerals present, and the mineral assemblage is what changes with provenance; factors derived from glacial samples may not hold for Holocene dust of different provenance, so the correction could interact with the result. According to an open copy read by instance S2, Gabrielli et al. (2010), cited for the factors in l. 119, give recovery fractions only for element groups (about 0.55 LREE, 0.50 MREE, 0.40 HREE) and state that no correction was applied. Do the cf_i differ between glacial and Holocene samples? |
| Suggestion | Add a supplement table with the 13 cf_i (mean, standard deviation, number and ages of the fully digested samples) and state their source in l. 119 to 124; if Holocene samples are absent from the digestion set, test the sensitivity of the Holocene results to period-specific factors. |
| Status | verified (absence of values and sample description); inferred (content of Gabrielli et al., 2010, from a partial reading); assumption (effect on the Holocene results, asked as a question) |
| Severity | moderate |
| Source | SD, S2 |

**GB-15 The end-member database is unbalanced in number and size fraction between PSA and contains two duplicated patterns, and the sensitivity of the apportionment to this is not tested.**

| Field | Content |
|---|---|
| Check | P9, P38 |
| Location | p. 4, l. 126 to 133; p. 11, l. 366; supplement p. 17, Table S2, rows Darling26 and Darling29; supplement p. 18, Table S2, rows Murray24 and Murray29; Table S2, column "Type of sample" |
| Quotation | "we compiled a comprehensive database of 217 REE patterns from" (l. 126); "our model identifies the Darling sub-basin as the dominant source region during the Holocene" |
| Concern | AUS supplies 107 of 217 patterns (49.3 %), ANT 4 (1.8 %), CWA 5. The size fractions differ between PSA: 100 patterns are below 90 µm (all AUS patterns from Marx and Kamber), 57 below 5 µm, 8 below 63 µm, 42 aeolian dust, 6 surface sediment, 4 bulk loess. Two pairs of AUS rows have identical coordinates and identical values for all 13 REE (confirmed on the page images): Murray24 ("Murray 10", Murray Basin) equals Darling29 ("DR 3", Darling Basin), and Murray29 ("Murray 15") equals Darling26. So the database holds 215 distinct patterns, the two columns of each pair are identical in Eq. 2, and the split of a contribution between them, and hence the Darling or Murray label, is arbitrary. With 13 equations and 217 candidates the solution is not unique among similar patterns, and a PSA with many candidates has more chances to supply the best-fitting combination. Neither the number of patterns per PSA nor the size fraction is discussed as a possible influence on the AUS increase, a central Holocene result, or on the sub-basin statement in l. 366. Did the authors test whether the AUS share depends on the number of AUS patterns, and do the Holocene contributions assigned to the Darling sub-basin include Darling26 or Darling29? |
| Suggestion | Remove the duplicates and give the size fraction rule in Section 2 and Table S2, state the number of distinct patterns in l. 126, and add sensitivity tests: random subsampling of AUS to the size of PAT (39) repeated many times; runs restricted to fine fractions (below 5 µm and aeolian dust); leave-one-PSA-out. Report the change of the Holocene and LGM means in Table S5 and rerun the sub-basin attribution behind l. 366. |
| Status | verified (counts, size fractions and duplicates in Table S2, page images); assumption (effect on the apportionment, asked as a question) |
| Severity | major |
| Source | SD, S2 |

**GB-16 The Antarctic end-members in Table S2 are not UCC-normalised as stated, and the numbers of Antarctic and Australian patterns differ from the Methods.**

| Field | Content |
|---|---|
| Check | P5, P2 |
| Location | p. 4, l. 131 to 135; p. 10, l. 327 to 334; supplement p. 19, Table S2, rows ELB, Expcove, Miers, Vict; supplement pp. 17 to 19, Table S2, AUS block; supplement p. 11, Table S1, row 3654 yr, column ANT; supplement p. 1 to 2, Figure S1, ANT panel |
| Quotation | "and Antarctica (ANT; 5 DS from the McMurdo Dry Valleys, representing ice-free sources). As with the EDC ice core samples, all PSA REE patterns were normalized to the UCC composition of Rudnick and Gao (2003)" |
| Concern | Table S2 lists 4 ANT patterns, not 5, and 107 AUS patterns (6 plus 45 Darling plus 36 Murray plus 20 aust), not 106; the total of 217 agrees either way. Figure S1 shows 5 ANT pins (PP-19), which fits a missing ANT row. The four ANT rows (page image p. 19) do not look normalised: their values fall from about 0.7 to 2.4 for La and Ce to about 0.01 for Lu with the odd-even zigzag of absolute crustal abundances (for ELB, Ce/Pr = 9.0 against 8.87 in the UCC), while every other PSA is near 1; divided by the UCC values of Rudnick and Gao (2003, Table 3) the first six values of the ELB row become flat at 0.022 to 0.031, and instance SD found ratios between 0.012 and 0.054 for all four rows. If these numbers entered Eq. 2, an ANT pattern could hardly match a UCC-normalised ice sample, and the near-absence of Antarctic dust and the contrast with the 24 % of Coppo et al. (2022) (l. 327 to 330) could be an artefact. Against this, Table S1 reports 33.1 % ANT at 3654 yr and 1.7 % at 13412 yr, so ANT patterns did enter some solutions; the consolidation therefore states the artefact only as a question. Which ANT values were used in the model, and is one Antarctic sample missing from Table S2? |
| Suggestion | Correct the counts in l. 131 to 133 or Table S2 and add the missing ANT row if there is one; state in Section 2 and Table S2 whether the ANT rows used in the model are the listed values or normalised ones; if the model used the listed values, rerun with normalised ANT patterns and report the ANT contribution before discussing l. 327 to 334, including the 3654 yr sample. |
| Status | verified (counts and ANT values on the page images; ANT values in Table S1); inferred (ratios against the UCC values); assumption (which values entered the model and the effect on the ANT contribution, asked as a question) |
| Severity | major |
| Source | SD, S3 |

**GB-17 The code and the computational settings needed to repeat the apportionment are not given.**

| Field | Content |
|---|---|
| Check | P35, P12 |
| Location | p. 5, l. 139 to 140; p. 5, l. 153 to 167; p. 16, l. 494 to 496 |
| Quotation | "This was implemented using the lsqnonneg function in MATLAB." |
| Concern | The method is described clearly in words and with Eq. 2. The results in Tables S1 and S5 and Figures 1 to 5 depend on steps for which no code is cited: building the 13 by 217 matrix after Gd removal and UCC normalisation, sampling cf_i and Dust_i over 2000 Monte Carlo runs, aggregating per PSA and sub-region, taking medians, computing R per run, converting to fluxes. Missing are also the MATLAB version and lsqnonneg tolerance, the random number generator and seed, and the per-element analytical uncertainties (only the range 2 to 10 %, l. 155 to 156). The CODE/DATA AVAILABILITY statement names code in its heading but covers only data, and it gives no link. |
| Suggestion | Deposit the DEPOT scripts with the input matrices in a public repository with a DOI and name it in the statement on p. 16, l. 494; state MATLAB version, solver options and seed in Section 2 and add the per-element RSD to the supplement. |
| Status | verified (absence in text, supplement and statement); inferred (that no public code exists elsewhere, not searched beyond the manuscript) |
| Severity | moderate |
| Source | S2, SD |

**GB-18 Is a zero contribution evidence of absence, given that the solver returns only a small subset of non-zero sources by construction?**

| Field | Content |
|---|---|
| Check | P31 |
| Location | p. 5, l. 149 to 152; p. 7, l. 217; p. 10, l. 330; p. 11, l. 355 to 357 |
| Quotation | "Sources with CDS equal to 0 are excluded from the fit, indicating no detectable contribution to that specific DIC sample." |
| Concern | The system has 13 equations and 217 non-negative unknowns. An active-set non-negative least-squares solution typically has no more positive coefficients than equations, so most source patterns are zero by construction, and among similar patterns which one is zero may depend on small differences. A zero would then reflect the solver and the database rather than a test of absence. This reading supports statements such as "North Puna does not contribute" (l. 356) and negligible CWA and ANT (l. 217, l. 330). The argument rests on the general behaviour of the solver, not on evidence in the manuscript, hence the question. |
| Suggestion | In l. 151 to 152 replace "indicating no detectable contribution" by a statement on non-uniqueness, and support absence statements by the Monte Carlo frequency with which a source or PSA is non-zero and by the recovery test of GB-11 with mixtures that contain that PSA. |
| Status | assumption (solver property from general knowledge); verified (wording and the absence statements at the cited lines) |
| Severity | moderate |
| Source | SD |

**GB-19 The Monte Carlo uncertainties are computed but not reported, so differences of 3 to 14 points between periods and cores cannot be judged.**

| Field | Content |
|---|---|
| Check | P11, P31 |
| Location | p. 5, l. 153 to 165; p. 4, l. 115 to 117; p. 6, l. 179 to 181; p. 13, l. 417 to 424; p. 1, l. 27 to 29; supplement Table S1 and Table S5; Figure 1 (caption l. 851 to 854) |
| Quotation | "Each DIC sample was subjected to 2000 simulations and the ensuing CDS results (in % of total deposition) generate a probability density function (PDF) for every DS" |
| Concern | The Methods build a PDF for each sample and source and keep only its median (l. 164 to 165). Table S1 holds medians only, Table S5 period means without standard deviation or standard error, Figure 1 medians and a moving average; Section 3 states only that the mixes "were considered meaningful compared to the uncertainties" (l. 180 to 181). The comparison of EDC and EDML interprets differences of 4, 6.5, 8, 12 and 14 points (l. 418 to 424), the Abstract reports "regional variations in the secondary contributions" (l. 28), and period contrasts such as ACR 68.9 % against YD 63.1 % PAT are discussed. Without the per-sample spread and an uncertainty for the period means, the reader cannot tell whether these differences exceed model uncertainty. The claims that 5000 simulations "does not significantly affect the results" (l. 163 to 164) and that Gd adds "more noise than discriminatory power" (l. 116 to 117) come without numbers. RQ1 claims a quantitative record, hence the grade. |
| Suggestion | Add the 25th and 75th (or 2.5th and 97.5th) percentiles of each PSA PDF to Table S1 and as a band to Figure 1; give standard errors or bootstrap intervals for Table S5 and Figures 3 and 4; state in Section 4.4 for each EDC minus EDML difference whether it exceeds the combined uncertainty; report the 2000 against 5000 run comparison and a run with Gd included. |
| Status | verified (absence in Tables S1 and S5, Figure 1 and Section 3) |
| Severity | major |
| Source | S3, SD, S2 |

**GB-20 The absolute PSA fluxes announced in the Methods are not reported, and the rise in low-latitude shares is interpreted as increased input although the manuscript's own flux figures imply lower absolute low-latitude deposition.**

| Field | Content |
|---|---|
| Check | P8, P11, P15 |
| Location | p. 5, l. 165 to 167; p. 6, l. 183 to 184; p. 1, l. 23 to 24; p. 10, l. 315 to 317; p. 13, l. 440 to 443; p. 14, l. 463 to 466 and l. 478 to 480; Figure 1; supplement Table S1; supplement pp. 3 to 4, Figure S2, panel A |
| Quotation | "to convert PSA contributions into absolute dust fluxes (Figure S2)" (l. 167); "the dust assemblage shifted toward greater inputs from low-latitude sources" (l. 23); "which likely amplified dust emissions and transport from these sources." |
| Concern | The conversion factor from nssCa2+ to dust, the matching of nssCa samples to REE samples and the resulting PSA fluxes are not given. Figure S2 shows only nssCa2+ flux, δ18O and deuterium excess; Figure 1 and Table S1 show only percentages, although l. 183 to 184 say they give contributions "in % of total deposition and flux" (page images). This matters for the main interpretation. Contributions sum to 100 %, so a fall in PAT deposition alone raises all other shares even if their emissions do not change. The Introduction states that interglacial dust fluxes are "up to 25 times lower than LGM fluxes" (l. 63), and Figure S2A shows the nssCa flux falling from several hundred to near zero after about 15 kyr BP. With Table S5, the AUS share rises from 10.2 % (LGM) to 23.1 % (Holocene), a factor of 2.26; the absolute AUS deposition ratio Holocene to LGM is 2.26/f, where f is the LGM to Holocene total flux ratio. For f = 5, 10 and 25 it is 0.45, 0.23 and 0.09, so for any f above 2.26 absolute AUS deposition at EDC fell; the same holds for SAF (factor 1.70) and PAP (factor 3.06). The Conclusion uses relative wording correctly (l. 478 to 479), but the Abstract (l. 23 to 24), l. 316 ("increased contributions") and the Discussion (l. 441 to 443, l. 463 to 466) read the shares as increased emission or transport. If the concern holds, the manuscript cannot claim increased low-latitude input. |
| Suggestion | State the conversion (factor or regression and source) and the age matching in Section 2, and report the PSA fluxes per sample and per period (columns in Tables S1 and S5, a panel in Figure S2 or Figure 1). Rewrite l. 23 to 24, l. 316, l. 441 to 443 and l. 463 to 466 on that basis: if absolute low-latitude fluxes fell, attribute the relative rise to the PAT decline and keep aridity and transport arguments only for differences that remain in absolute terms; otherwise delete the flux statements in l. 166 to 167 and l. 183 to 184. |
| Status | verified (absence of flux values in Table S1, Figure 1 and Figure S2 on the page images; shares in Table S5; statement in l. 63); inferred (ratios computed from Table S5) |
| Severity | major |
| Source | S2, S3, S4, AB, SD |

**GB-21 The stated significance of the fit threshold R of at least 0.67 cannot be reproduced, and a parametric test does not apply to a fitted pattern.**

| Field | Content |
|---|---|
| Check | P1, P8 |
| Location | p. 5, l. 170 to 172; p. 5, l. 145; p. 6, l. 174; supplement Table S1, column R |
| Quotation | "We determined that R ≥ 0.67 corresponds to a statistically significant match (p < 0.01, two-tailed test, degrees of freedom = 10)" |
| Concern | For a Pearson correlation the critical value is r = t/sqrt(t² + df). Computed with scipy: two-tailed p of 0.01 gives r_crit = 0.708 at df = 10 and 0.684 at df = 11, the degrees of freedom implied by 13 REE (l. 145); R = 0.67 corresponds to p = 0.017 (df = 10) or 0.012 (df = 11). R = 0.67 reaches p of 0.01 only one-tailed at df = 10 (0.658) or two-tailed at df = 12 (0.661). Beyond the arithmetic, the modelled pattern is fitted to the measured one with many free coefficients, so the two are not independent and the t-test null distribution does not hold; R between a fit and its target is raised by construction. The choice decides which samples enter the record: in Table S1, 19 retained samples have R of 0.70 or less (below 0.708) and 9 have R of 0.68 or less (below 0.684), 17 of the 19 in the Holocene. |
| Suggestion | In l. 170 to 172 state n, df and the tail and correct p or df; replace the parametric test by a null distribution that respects the fitting, for example by fitting permuted or synthetic patterns with the same 217 sources and taking the 99th percentile of their R as threshold. Report the resulting threshold and how many samples it retains, and update l. 174 to 182, Table S1 and Table S5 if the retained set changes. |
| Status | inferred (critical values and p computed with scipy; dependence of fit and target from the method description); verified (counts in Table S1) |
| Severity | moderate |
| Source | S3, SD |

**GB-22 Figure S2 lacks units, and its three panels are not on a common time axis.**

| Field | Content |
|---|---|
| Check | P29 |
| Location | supplement pp. 3 to 4, Figure S2, panels A to C and caption |
| Quotation | "(A) Non Sea Salt Calcium (nssCa2+) flux in EDC ice core" |
| Concern | The axes "nssCa2+ flux", "δ18O" and "deuterium excess" have no units (l. 166 gives µg m⁻² yr⁻¹; δ18O and deuterium excess are in ‰). The δ18O axis has tick values such as -49.05 and -51.05. Panel B has no period bands. The tick 0.4 (×10⁴ yr) lies at 761 px in A, 771.5 px in B and 752 px in C, and the tick 3.2 at 2521, 2516 and 2502.5 px (300 dpi rendering); at about 63 px per kyr the panels are offset by up to 0.3 kyr, while the text reads timing across them (l. 296 to 299, l. 449). |
| Suggestion | Add units, use round tick values, add the period bands to panel B and align the panels on one time axis. |
| Status | verified (measured on the page image) |
| Severity | minor |
| Source | AB |

**GB-23 "PSA" names both the seven source regions and the 217 individual source patterns.**

| Field | Content |
|---|---|
| Check | P38 |
| Location | supplement p. 16, Table S2, title; supplement p. 11, Table S1, caption; p. 4, l. 129; p. 10, l. 329 |
| Quotation | "Median of PSA's contribution (in percents) based on th DEPOT model results - using 217 PSAs and 279 DIC from EDC ice core REE patterns." |
| Concern | The main text uses PSA for a region (PAT, CWA, PAP, SAF, AUS, NZ, ANT) and DS for one of the 217 patterns (l. 129, l. 144, l. 161, l. 329; Figure S1). The supplement captions call the 217 patterns "PSAs" ("Table of PSAs database", Table S2). A reader of Table S1 meets "217 PSAs" next to column headers that are seven PSAs. The same caption also announces 279 samples while the table has the 241 retained ones (page image p. 11). The minor correction proposed by instance S3 for this caption is included here. |
| Suggestion | Replace the Table S1 caption by "Median of PSA contributions (in percent) based on the DEPOT model results, using 217 dust sources (DS) and the 241 DIC samples from the EDC ice core with R ≥ 0.67." and title Table S2 "Dust source (DS) database". |
| Status | verified (page images) |
| Severity | minor |
| Source | S2, S3 |

**GB-24 One value of the source pattern Kuiseb2inf5 in Table S2 is more than twice its neighbours and looks like an entry error.**

| Field | Content |
|---|---|
| Check | P5 |
| Location | supplement p. 17, Table S2, Southern Africa block, row Kuiseb2inf5, eighth REE column (Dy) |
| Quotation | "6,200013" |
| Concern | In the UCC-normalised pattern of Kuiseb2inf5 the eighth value (Dy, Gd removed) is 6.200013, while the other twelve values of the row lie between 1.805 and 3.344 and the neighbouring Tb and Ho values are 2.692922 and 2.149792; the twin sample Kuiseb1inf5 from the same river bed has 2.376464 in that column (page image p. 17). A single spike of this size is not expected in a normalised crustal pattern and changes the shape that Eq. 2 fits. Instances S2 and SD noted the value outside their checklists; no instance treated it, and the consolidation confirmed it on the page image. Is the value a transcription error in the table, or did it also enter the model? |
| Suggestion | Check the value against the source (Vanderstraeten et al., 2023), correct Table S2 on supplement p. 17, and if the model used it, rerun and report whether SAF contributions change. |
| Status | verified (value on the page image); assumption (entry error and use in the model, asked as a question) |
| Severity | moderate |
| Source | ZF |

#### Minor corrections

| Code | Location | Quotation | Replacement | Source |
|---|---|---|---|---|
| KK-15 | p. 3, l. 101 | "ice core camples" | "ice core samples" | SD |
| KK-16 | p. 4, l. 109; p. 6, l. 190 (10 occurrences of "MIS3" against 2 of "MIS 3") | "the end of MIS 3" | "the end of MIS3" | S2 |
| KK-17 | p. 4, l. 127 (the database is Table S2, as l. 128 says) | "(Figure S1, and Table S1)" | "(Figure S1 and Table S2)" | S2, SD |
| KK-18 | p. 4, l. 128 | "subdivised into Patagonia" | "subdivided into Patagonia" | SD |
| KK-19 | p. 5, l. 145 to 146 | "For any given time step. The vector of 217 components" | "For any given time step, the vector of 217 components" | SD |
| KK-20 | p. 5, l. 159 (Eq. 1 defines cf_i; the minimised norm is Eq. 2) | "by minimizing Eq. (1)" | "by minimizing Eq. (2)" | S2, SD |
| KK-21 | supplement p. 16, Table S2, block header | "Puna AltiPlano (PAP)" | "Puna-Altiplano Plateau (PAP)" (as on p. 4, l. 129) | S2 |
| KK-22 | supplement p. 16, Table S2, header and rows PataGa6, PataGa7, Npuna1; supplement p. 18, rows aust8 to aust13, column "Location" | "Lattitude"; "Ingienero white"; "Laguna Guayatayoe"; "Murrumbigdee basin" | "Latitude"; "Ingeniero White"; "Laguna Guayatayoc"; "Murrumbidgee basin" | S2 |
| KK-23 | supplement p. 17, Table S2, Southern Africa block, second column | "Omarur1inf5", "Omarur2inf5" | "Omaruru1inf5", "Omaruru2inf5" (as "Omaruru3inf5") | S2 |
| KK-24 | supplement p. 19, Table S2, block header; supplement p. 20, Table S3, row 4 | "New-Zealand (NZ)" | "New Zealand (NZ)" (as on p. 4, l. 132) | S2 |

#### Verification log

| Code | Check | Checked | Values | Result |
|---|---|---|---|---|
| PP-09 | P9, P10 | Design sketch of the study, Sections 1 and 2 and the supplement (SD) | Type: method application of DEPOT to a published REE data set plus descriptive reconstruction and literature comparison. RQ1 to RQ4 at l. 91 to 98. Cases: EDC, 294 patterns, 15 removed, 279 modelled, 38 excluded by R, 241 reported, 2852 to 33699 yr BP, 13 REE, 217 source patterns in 7 PSA. Controls: literature Sr-Nd data (Table S4) for RQ2, EDML record for RQ4, no known-mixture control. Data sources: EDC REE (secondary), cf_i (values not given), Table S2 (secondary plus 6 primary rows), nssCa flux (secondary), Tables S3, S4 (secondary), EDML (model output). Software MATLAB lsqnonneg, no version or seed. Guarantees: non-negativity, UCC normalisation, R threshold, exclusion, zero meaning, data statement. Disclosed limits at the method: sampling gap (l. 113), 15 incomplete patterns (l. 114 to 115), Gd (l. 115 to 117), incomplete leaching (l. 121 to 122); 38 exclusions in Results (l. 174 to 179); ACR and YD tentative only in 4.4 (l. 407 to 409) | basis for GB-11, GB-14, GB-17 to GB-21, GB-25, GB-38, GB-41, GB-47, GB-52 |
| PP-10 | P12 | Every data source named in Section 2 (l. 99 to 172) against the CODE/DATA AVAILABILITY statement (l. 494 to 496) and the supplement (S2) | EDC REE data (Gabrielli et al., 2010): cited, not in supplement, no archive; EDC3 age model, UCC composition, nssCa flux (Fischer et al., 2007), δ18O and deuterium excess: cited and published; cf_i: not given; analytical uncertainties: range only; source database: Table S2, 117 of 217 rows (53.9 %) cite sources missing from the reference list; site map: Figure S1; code: not mentioned; Monte Carlo outputs: medians only (Table S1); absolute PSA fluxes: not given; R per sample: Table S1; excluded samples: not identified; EDML contributions: Table S5; isotope data: Tables S3, S4. Disclosed limits: sampling gap 21.7 to 27.3 kyr BP with four samples (22150, 23104, 25384, 25640 yr), Gd exclusion | gaps reported in GB-14, GB-17, GB-19, GB-20, GB-25, GB-46, GB-54 |
| PP-11 | P38 | Identifiers of model, data sets, samples, regions and periods across text, captions and supplement (S2) | Model: "'DEPOT' model" (l. 88), "DEPOT algorithm" (l. 100, l. 259), "statistical unmixing algorithm" (l. 19), "unmixing model" (l. 306), one procedure, expanded at l. 100. Sample counts 294, 279, 241 explained. DIC, CDS, cf_i, DS used consistently; Dust_i (measured) and DIC_La to DIC_Lu (corrected, normalised) are two objects. PSA codes consistent; Table S1 splits PAP into Puna and Altiplano (explained l. 130, l. 355 to 358); "SCWA" in Table S3 is a subset of CWA. EDC3 and AICC2012 are two objects (GB-13). Period labels consistent apart from KK-16, KK-27, KK-32 | no further finding; GB-23, GB-43 |
| PP-12 | P26 | Non-negativity guarantee in single fit, each Monte Carlo run and aggregation (SD) | lsqnonneg used for every fit (l. 140, l. 159); aggregation of non-negative values preserves sign; all 1928 PSA values in Table S1 are at least 0.0 | guarantee holds in all described paths |
| PP-13 | P37 | Whether figures or tables show corrected values without saying so (SD) | cf_i correction stated (l. 117 to 124) and applied to all results; Table S5 equals the recomputation from Table S1 (PP-23); Figure 4 bars equal Table S5 differences apart from the window question (GB-50) | no undeclared change found |
| PP-14 | P35 | Analytical method of the reused REE data (SD) | Data from Gabrielli et al. (2010) with the method of Gabrielli et al. (2006) cited (l. 156); acid leaching with ultrapure HNO3 (l. 120); partial dissolution disclosed (l. 121 to 122) | citation sufficient for reused data; missing inputs in GB-14 and GB-17 |
| PP-15 | P30 | Reported errors, corrections and order of runs (SD) | No error, bug fix or model correction reported; one modelling run plus an unreported 5000-run test (l. 163 to 164) | no finding |
| PP-16 | P33 | Statements on effort or cost (SD) | Only "a tradeoff between computation cost and representativity" (l. 162 to 163), used to justify 2000 runs | no finding beyond GB-19 |
| PP-17 | P27 | Downstream use of untested components (SD) | R threshold (GB-21) selects the record (GB-25); PSA medians feed Table S5, Figures 2 to 5 and the isotope back-calculation; the zero reading (GB-18) feeds absence statements; exclusion of 38 samples disclosed (l. 174 to 179) | covered by the findings named |
| PP-18 | P25 | Whether each step had the information it uses (SD) | Eq. 3 and 4 need Sr and Nd concentration and isotope values per PSA: Table S3 gives them for PAT, AUS, SAF, NZ, S-Puna, S-Altiplano, SCWA, none for ANT; Monte Carlo needs cf_i variability, present in the authors' data but not reported; flux conversion needs nssCa at the REE sample ages, matching not reported | no step uses unavailable information; reporting gaps in GB-14, GB-20 |
| PP-19 | P3, P29 | Figure S1, counts and legibility (AB) | ANT: 5 pins against 5 source patterns in l. 132 to 133 (Table S2 has 4, GB-16); PAT 19 pins against 39 patterns, co-located samples share a pin; each panel labelled by region and colour; scale bars illegible at print size in NZ, SAF, CWA, AUS and ANT panels, none in the Puna-Altiplano panel and the globe; map source credited | no finding (positions inferred, map without grid) |

### Segment 3: Results (pp. 6 to 7, 24 to 25, 27; supplement pp. 5 to 8, 11 to 15, 22)

#### Substantive findings

**GB-25 Samples were excluded by their fit quality, the exclusion falls entirely on the part of the record younger than 14 kyr BP, and the excluded samples are not identified.**

| Field | Content |
|---|---|
| Check | P9, P22 |
| Location | p. 6, l. 174 to 179; p. 4, l. 114; p. 12, l. 408; supplement Table S1; supplement p. 22, Table S5, Holocene rows; p. 1, l. 25 |
| Quotation | "Out of the 279 DIC samples treated by our algorithm, 38 did not meet the R threshold (R≥0.67) and were excluded from the provenance record. These excluded samples are all younger than 14 kyr BP" |
| Concern | The manuscript discloses the exclusion but does not draw its consequence. The criterion is a model output (fit quality), and it is linked to concentration (l. 176 to 177). Table S1 holds 129 retained samples younger than 14 kyr BP, so 38 of 167 such samples were removed (22.8 %); before 14 kyr BP none. The Holocene averages (Table S5, Figure 3, Abstract l. 25: "~49% on average") rest on the survivors. If low-concentration samples come from times of weak or different supply, the retained set over-represents samples with more dust, and the period means are biased in an unknown direction. Only the ACR and YD counts are stated (l. 408, one of them wrong, GB-48); counting Table S1 gives Late Holocene 60, Early Holocene 56, YD 9, ACR 8, HS1 27, LGM 40, MIS3 41, but how the 38 exclusions split between the ACR, YD, Early and Late Holocene is not stated, and neither they nor the 15 incomplete samples (l. 114) are listed. Holocene means are a result for RQ1, hence the grade. Do the excluded samples cluster in particular periods? |
| Suggestion | List the 38 excluded and the 15 incomplete samples in the supplement (age, concentrations, R); add to Table S5 the numbers of retained and excluded samples per period and refer to it in l. 174 to 176; report the Holocene means with a relaxed threshold (for example R of at least 0.6) or with excluded samples set to the mix of their neighbours; state in the Abstract that the Holocene means rest on retained samples only. |
| Status | verified (exclusion and counts, l. 174 to 175, Table S1); inferred (share 38/167 computed); assumption (direction of bias, asked as a question) |
| Severity | major |
| Source | SD, S3, S2 |

**GB-26 Table S1 contains three retained samples below the stated threshold and one row whose contributions add up to 93.5 %.**

| Field | Content |
|---|---|
| Check | P2, P5, P23 |
| Location | supplement p. 11, Table S1, rows 2888 yr and 3267 yr, column R; supplement p. 13, Table S1, first row 10511 yr, columns PAT to ANT and R; p. 6, l. 174 to 175 |
| Quotation | "38 did not meet the R threshold (R≥0.67) and were excluded from the provenance record" |
| Concern | Rows 2888 yr, 3267 yr and the first 10511 yr row give R = 0,66 (page images p. 11 and p. 13). A value printed as 0.66 is below 0.665 if rounded and cannot meet R of at least 0.67; four further rows give exactly 0,67. The first 10511 yr row sums to 0.0 + 0.0 + 3.1 + 6.7 + 49.2 + 29.5 + 5.0 + 0.0 = 93.5, while all other 240 rows sum to 100.0 within 0.1. Resolution A: R was truncated, not rounded; then the column should say so. Resolution B: the three samples were retained by mistake; then the record has 238 samples and 41 exclusions, and the Holocene means change. For the row sum, either a value of 6.5 points is missing or the row was not normalised like the others; the same sample has one of the lowest R values. Which resolution applies? |
| Suggestion | Give R with three decimals in Table S1, or remove the three samples and update l. 174 to 182, Table S5 and Figure 1; correct or explain the row sum of the first 10511 yr row. |
| Status | verified (values on the page images); inferred (row sums computed); assumption (resolutions, asked as a question) |
| Severity | moderate |
| Source | S3, SD |

**GB-27 The period values reported as percentages of total dust deposition are unweighted means of per-sample medians, and weighting by time changes some of them by several points.**

| Field | Content |
|---|---|
| Check | P20, P21 |
| Location | p. 6, l. 189 to 191; p. 6, l. 183 to 188; supplement p. 22, Table S5, caption; p. 10, l. 319 to 327 |
| Quotation | "It contributes for 65-70% (average contributions) of the total dust deposition during the end of MIS 3 and the LGM" |
| Concern | Table S5 is reproduced exactly as the arithmetic mean of the Table S1 rows in each period (PP-23), so every sample has equal weight whatever its time span and dust flux. Sample spacing is very uneven (16 yr to 2280 yr between adjacent retained samples). Weighting each sample by half the distance to its neighbours, clipped to the period bounds, gives YD SAF 22.4 instead of 14.6, YD PAP 2.0 instead of 4.5, Holocene PAT 51.6 instead of 49.0, ACR AUS 8.5 instead of 11.1 and LGM NZ 15.3 instead of 14.2. A flux weighting cannot be computed because PSA fluxes are not given (GB-20). The literature values compared in l. 319 to 327 (DustCOMM, Coppo et al., 2022) are fractions of deposited mass, so the quantities differ. |
| Suggestion | State in the caption of Table S5 and in l. 189 to 191 that the values are unweighted means of per-sample medians; add time-weighted and, once fluxes are reported, flux-weighted means as a sensitivity check, and use flux-weighted shares for the comparison with DustCOMM and Coppo et al. (2022). |
| Status | verified (Table S5 reproduced from Table S1); inferred (weighted means computed) |
| Severity | moderate |
| Source | S3 |

**GB-28 Results at the level of single source patterns and sub-basins are stated without data in the manuscript or the supplement.**

| Field | Content |
|---|---|
| Check | P11, P34 |
| Location | p. 6, l. 196 to 197; p. 5, l. 161 to 162; p. 11, l. 366; p. 12, l. 385 to 387 and l. 392 to 398; supplement Table S1; supplement pp. 5 to 6, Figure S3 |
| Quotation | "Among the 39 DS from PAT, our algorithm highlights three specific REE patterns collected in or near the Valdes Peninsula." |
| Concern | The Methods announce aggregation "by PSA or specific sub-regions within PSA" (l. 161 to 162). Sub-regional results are shown only for Puna, Altiplano, Etosha, Namibia and Sua (Figure S3). There are no numbers for the three Valdes Peninsula sources, for Australian sub-basins ("our model identifies the Darling sub-basin as the dominant source region during the Holocene", l. 366), or for detection frequencies ("the Namibian coast and ephemeral riverbeds were detected most frequently", l. 385 to 386, "relatively frequent" for Makgadikgadi). The denominator of "detected most frequently" is not stated, and no rule says how the highlighted patterns were chosen among 217. |
| Suggestion | Add a supplementary table that gives, for each source pattern or at least each sub-region (and the three Valdes sources), the number of samples with a contribution above zero out of the samples in each period and the mean contribution; cite it at l. 196 to 197, l. 366 and l. 385 to 387. |
| Status | verified (absence in Tables S1, S5 and Figures 1, S3) |
| Severity | moderate |
| Source | S3, SD |

**GB-29 The overall ranking of the secondary sources does not follow from Table S1 or Table S5 under any aggregation.**

| Field | Content |
|---|---|
| Check | P2 |
| Location | p. 6, l. 201 to 202; supplement Table S1; supplement p. 22, Table S5; p. 7, l. 223 |
| Quotation | "Overall, other Southern Hemisphere PSAs contribute to EDC dust deposition with sources from: AUS, SAF, PAP and NZ, in decreasing order of importance." |
| Concern | The mean over all 241 samples of Table S1 is AUS 16.51 %, SAF 9.17 %, NZ 7.85 %, PAP 6.85 %, so NZ ranks above PAP. The unweighted mean of the six period means in Table S5 also puts NZ above PAP: AUS 13.22, SAF 8.97, NZ 7.70, PAP 4.75. Among single periods only the YD ranks PAP above NZ, and there SAF (14.6) precedes AUS (14.5). The Discussion gives a different order for the LGM (l. 223: NZ, AUS, SAF, PAP), which does match Table S5. The high- against low-latitude conclusion does not depend on this ranking. |
| Suggestion | In l. 201 to 202 give the ranking per period or state the aggregation on which the overall ranking rests (for example mean over all samples: AUS, SAF, NZ, PAP). |
| Status | inferred (means computed from Tables S1 and S5) |
| Severity | moderate |
| Source | S3 |

**GB-30 Two bounds in Section 3, SAF at about 2 % between 9.5 and 12 kyr BP and South Puna consistently below 20 % in the Holocene, do not match Table S1 or the cited figure.**

| Field | Content |
|---|---|
| Check | P2, P3, P20 |
| Location | p. 6 to 7, l. 207 to 208; p. 7, l. 214 to 215; Figure 1 (p. 24), SAF and PAP panels; supplement Table S1, columns SAF and Puna; supplement pp. 5 to 6, Figure S3, Puna panel |
| Quotation | "Although SAF input drops to minimal levels (~2%) between 9.5 and 12 kyr BP" (l. 207 to 208); "contributions of South Puna remained consistently below 20% during this interval (Figure 1)" |
| Concern | SAF: the 33 samples between 9.5 and 12 kyr BP give a mean of 4.32 % and a median of 0.3 %, with two samples at 40.3 % (10278 yr) and 49.2 % (10511 yr). The smoothed SAF curve of Figure 1 (measured, 300 dpi) reaches 12.3 % between 10.3 and 10.5 kyr and 11 to 12.7 % from 11.5 kyr on, and is near 1 % only around 9.9 kyr and 10.9 to 11.4 kyr; a centred 9-point moving mean of Table S1 gives the same. The "~2%" fits neither the mean, the median nor the plotted curve. South Puna (the only Puna contributor, l. 356): eight Holocene samples of Table S1 reach 20 % or more (3503 yr 25.0; 4387 yr 20.6; 5657 yr 23.4; 5850 yr 29.1; 6775 yr 20.7; 7833 yr 25.6; 10205 yr 25.7; 11117 yr 20.2), and the Puna panel of Figure S3 has seven raw peaks above 20 %. Figure 1, which is cited, shows PAP only and no South Puna series. |
| Suggestion | In l. 207 to 208 name the statistic and the interval, for example "SAF input is mostly below 2 % between 9.5 and 12 kyr BP (median 0.3 %), apart from two samples at 10.3 and 10.5 kyr BP (40 and 49 %)"; in l. 215 write "mostly below 20 % (maximum 29 %)" and cite Figure S3. |
| Status | verified (Table S1 values; Figure 1 measured; Figure 1 panels on the page image); inferred (mean and median computed) |
| Severity | moderate |
| Source | S3, AB |

**GB-31 Southern Altiplano contributions above 90 % are claimed for five ages, but Table S1 supports two, and the cited Figure 1 does not show the sub-region.**

| Field | Content |
|---|---|
| Check | P2, P3, P20, P36 |
| Location | p. 7, l. 213 to 216; Figure 1 (p. 24), PAP panel; supplement pp. 11 to 13, Table S1, column Altiplano; supplement pp. 5 to 6, Figure S3 |
| Quotation | "which even becomes dominant in several samples, contributing over 90% at 11.2, 10, 8.6, 6, and 3.5 kyr BP" |
| Concern | The Holocene rise of PAP dust is well documented (PAP from 3.6 % in the LGM to 11.0 % in the Holocene, Table S5). The Altiplano column of Table S1 exceeds 90 % only at 8629 yr (100.0) and 11228 yr (97.0); near the other three ages the highest values are 75.7 (9957 yr), 58.5 (5967 yr) and 62.7 (3465 yr). The raw PAP curve of Figure 1 measures 99.2 % (8.6 kyr) and 97.7 % (11.2 kyr) but 76.7 %, 58.2 % and 60.8 % at 10.0, 6.0 and 3.5 kyr. All five exceed 50 %, so "dominant" holds; the threshold does not. If "over 90%" meant the Altiplano share of PAP, the five ages would not be special, since Altiplano makes up all of PAP in further samples (for example 3267, 5453, 6367, 6449 yr). Figure 1, the figure cited, has no Altiplano series; the sub-regions are shown only in Figure S3 (which itself disagrees with Table S1, GB-35). |
| Suggestion | In l. 213 to 216 state the denominator and write, for example, "over 90 % at 11.2 and 8.6 kyr BP and between 58 and 76 % at 10, 6 and 3.5 kyr BP"; cite Figure S3 instead of Figure 1 for the sub-regional statement. |
| Status | verified (Table S1 values; Figure 1 measured); inferred (alternative reading) |
| Severity | moderate |
| Source | S3, AB, SD |

**GB-32 Figure 1 cannot be read without the text: abbreviations, time unit and the meaning of the thin line are not explained, and the panels are not aligned.**

| Field | Content |
|---|---|
| Check | P29 |
| Location | Figure 1 (p. 24), all panels; caption p. 25, l. 851 to 854 |
| Quotation | "Bold lines denote the mobile average over 9 steps." |
| Concern | The gray bands match the period boundaries of l. 185 to 188 to within about 50 yr (PP-25). However: (1) PAT, AUS, SAF, NZ, PAP and the period labels YD, ACR, HS1, LGM, MIS3 are not expanded in the caption; (2) the time axis reads "Time (yr BP)" with a factor ×10⁴ only in the bottom right corner, while the text uses kyr BP, and the four upper panels have no axis title; (3) the legend ("Raw data", "smoothed") appears only in the bottom panel, and the caption does not say that the raw data are the medians of the Monte Carlo distributions; (4) the five panels are separate images whose x axes are offset by up to 7 px (tick 0.4 at 681 px in the top panel and 688 px in the fourth, about 170 yr), so the bands do not line up exactly. |
| Suggestion | Expand all abbreviations and give the period limits in the caption; label the axis "Age (kyr BP)"; state that the thin line shows the median of 2000 Monte Carlo runs per sample; align the five panels on one time axis. |
| Status | verified (page image, measured) |
| Severity | minor |
| Source | AB |

**GB-33 The Holocene box plot of Figure 3 shows only the Early Holocene, the Early Holocene panel of Figure S4 shows the Late Holocene, and the Late Holocene appears nowhere under its name.**

| Field | Content |
|---|---|
| Check | P3, P11 |
| Location | Figure 3 (p. 27), left panel "Holocene"; caption l. 869 to 873; supplement pp. 7 to 8, Figure S4, panel (1) "Early Holocene"; p. 9 to 10, l. 315 to 319; supplement p. 22, Table S5, row Late Holocene |
| Quotation | "Box plots of provenance contributions (in %) of Holocene, and Last Glacial Maximum (LGM) dust depositions in EDC ice core." |
| Concern | Box edges, medians and mean crosses were measured on the page images (300 dpi; ±0.22 points) and compared with Table S1 quartiles; the method reproduces the LGM panel to within 0.13 points (PP-26). Figure 3 "Holocene" panel, Q1/median/Q3 measured against Early Holocene (n = 56) and whole Holocene (n = 116): PAT 12.20/55.24/72.96 against 12.3/55.2/73.0 and 18.4/58.6/73.8; NZ 0/1.08/7.46 against 0/1.1/7.5 and 0/0/5.5; PAP 0/0/12.48 against 0/0/12.5 and 0/0/17.6; mean crosses PAT 47.3, AUS 25.0, NZ 8.4 against Early Holocene 47.1, 24.9, 8.1 and whole Holocene 49.0, 23.1, 5.9. Figure S4 panel (1) "Early Holocene" matches the Late Holocene (n = 60): PAT 18.94/61.70/80.67 against 18.9/61.7/80.7, upper whisker 97.93 against the Late Holocene maximum 97.9. So the panel labelled Holocene differs from the Holocene values of the text (l. 315 to 319) and of Figure 4, and the Late Holocene, reported separately in Table S5 and discussed in l. 195 and l. 352, has no box plot under its name. The caption of Figure 3 names only HS1, ACR and YD of the five panels of Figure S4. The same exchange of labels appears in Figure 2 (GB-57). |
| Suggestion | Relabel the left panel of Figure 3 "Early Holocene (7.5 to 11.7 kyr BP)" or replot it with all 116 Holocene samples; relabel panel (1) of Figure S4 "Late Holocene (2.8 to 7.5 kyr BP)"; list all panels of Figure S4 in the caption of Figure 3 and give n per box in both captions. |
| Status | verified (measured on the page images; quartiles from Table S1) |
| Severity | moderate |
| Source | AB, S3 |

**GB-34 The captions of Figure 3 and Figure S4 describe the whiskers as extremes, but they end at 1.5 times the interquartile range, and Figure S4 panels are drawn at a different scale.**

| Field | Content |
|---|---|
| Check | P3, P29 |
| Location | Figure 3 (p. 27) and supplement p. 8, Figure S4, all boxes; caption l. 871 to 872; supplement p. 7, Figure S4 caption |
| Quotation | "and the whiskers indicate the lower and upper extremes" |
| Concern | Measured upper whisker ends in the Holocene panel of Figure 3 against Q3 plus 1.5 IQR from the Early Holocene data: AUS 79.84 against 79.8 (3 points above, maximum 98.1); SAF 25.54 against 25.5 (10 above); NZ 16.43 against 16.4 (9 above); PAP 27.98 against 28.0 (4 above, maximum 100). In the LGM panel the PAT whisker ends at 84.36 with a point at 93.5. The whiskers follow the Tukey rule and the dots are single samples; the caption explains neither. In Figure S4, panels (2) to (5) have no y axis of their own and are drawn about 1.5 % taller than panel (1): read against the axis of panel (1), the ratio of measured to Table S1 values is 1.015 for the ACR, HS1 and MIS3 PAT boxes, and the YD whisker top of 98.7 % lies above the 100 % tick. |
| Suggestion | Write "whiskers extend to the most extreme value within 1.5 times the interquartile range; dots show individual samples"; give each panel of Figure S4 its own axis or a common scale. |
| Status | verified (measured) |
| Severity | minor |
| Source | AB |

**GB-35 Figure S3 does not reproduce the Altiplano and Puna values of Table S1 and Figure 1.**

| Field | Content |
|---|---|
| Check | P3 |
| Location | supplement pp. 5 to 6, Figure S3, panels "Altiplano", "Puna" and "Sua"; supplement Table S1; Figure 1 (p. 24), PAP panel; p. 11, l. 355 to 360 |
| Quotation | "Evolution of contribution to EDC from subregions of the Puna-Altiplano and Southern Africa PSA" |
| Concern | Raw maxima measured on Figure S3 (300 dpi; faded line tips may read up to about 3 points low) against Table S1: Altiplano at 8.6 kyr 5.7 % or less against 100.0 % (8629 yr; Figure 1 PAP 99.2 %); Altiplano at 11.2 kyr 14.6 % against 97.0 % (11228 yr; Figure 1 97.7 %); highest raw Altiplano value 66.1 % at 6.4 kyr against 53.5 % (6367 yr); Puna at 11.1 kyr 42.9 % against 20.2 % (11117 yr); Puna at 11.8 kyr 54.9 % against 0.5 % and 0 % (11779 and 11993 yr). At 3.5, 5.6, 5.8, 6.7, 7.8 and 10.2 kyr the Puna panel agrees with Table S1 within 1.4 points. Figure S3 is the only figure for the Southern Altiplano onset and the South Puna trend discussed in l. 355 to 360, and it disagrees with the table at the dates that matter. Panel 5 is named "Sua", while the text speaks of the "Makgadikgadi Complex (including Sua Pan)" (l. 380). Does Figure S3 come from another model run or another aggregation? |
| Suggestion | Replot Figure S3 from the data of Table S1 or state which run it shows; name panel 5 "Makgadikgadi (Sua Pan)". |
| Status | verified (measured; Table S1); assumption (cause, asked as a question) |
| Severity | moderate |
| Source | AB |

#### Minor corrections

| Code | Location | Quotation | Replacement | Source |
|---|---|---|---|---|
| KK-25 | p. 6, l. 189 | "It contributes for 65-70% (average" | "It contributes 65-70% (average" | S3 |
| KK-26 | p. 6, l. 191 | "the PSA dust assemblage during HSI is marked" | "the PSA dust assemblage during HS1 is marked" | S2, S3 |
| KK-27 | p. 6, l. 193 | "(averages contributions), respectively" | "(average contributions), respectively" | S3 |
| KK-28 | p. 6, l. 198 | "and therefore reflects regional mixed input" | "and therefore reflect regional mixed input" | S3 |
| KK-29 | p. 6, l. 199 | "reflected by LREE (low rare earth elements) depletions" | "reflected by LREE (light rare earth elements) depletions" | S3 |
| KK-30 | p. 7, l. 213; p. 9, l. 290 (against "Southern Altiplano" in l. 130, l. 358, l. 362) | "the emergence of South Altiplano dust" and "conditions in the South Altiplano" | "the emergence of Southern Altiplano dust" and "conditions in the Southern Altiplano" | S2 |
| KK-31 | p. 25, Figure 1 caption, l. 851 | "between 2852 to 33699 yr BP" | "between 2852 and 33699 yr BP" | AB |
| KK-32 | p. 25, Figure 1 caption, l. 853 | "as their dust emissions contribution are very low" | "as their contributions are very low" | AB |
| KK-33 | supplement p. 7, Figure S4 caption | "Antarctica Cold Reveal (ACR), (4) Heindrich Stadial 1 (HS1), and (5) Marine Isotope 3 (MIS3)" | "Antarctic Cold Reversal (ACR), (4) Heinrich Stadial 1 (HS1), and (5) Marine Isotope Stage 3 (MIS3)" (as on p. 6, l. 184 to 186) | S2, S3, AB, SD |

#### Verification log

| Code | Check | Checked | Values | Result |
|---|---|---|---|---|
| PP-20 | P23, P36 | Sample balance from the data set to the record and per period (S3, SD) | 294 minus 15 = 279 (l. 108, l. 114, l. 117); 279 minus 38 = 241 (l. 174 to 179); 241/279 = 0.864, stated 86 % (l. 179); Table S1 has 241 rows; per period 60 + 56 + 9 + 8 + 27 + 40 + 41 = 241; four samples between 21.7 and 27.3 kyr BP as stated (l. 113); source patterns 39 + 5 + 14 + 23 + 106 + 25 + 5 = 217 = rows of Table S2 (split see GB-16). Disclosed: sampling gap (l. 113), small ACR and YD numbers (l. 407 to 408) | balance closes; YD count in GB-48 |
| PP-21 | P1 | Mean correlation coefficient and further arithmetic statements (S3) | Mean R over 241 samples 0.8523, stated 0.852 (l. 181), median 0.89; Coppo et al. LGM split 64 + 15 + 11 + 5 + 5 = 100 (l. 278 to 279); PAT mean below 5 kyr BP (25 samples) 52.0, stated 50 to 55 % (l. 352); PAT minima (l. 194) at 9957, 10029, 10222 yr (0.0), 8629 yr (0.0), 6245 and 6367 yr (0.0) and 6306 yr (6.5); AUS maxima (l. 205) 98.1 (9772 yr), 95.3 (9976 yr), 84.0 (6306 yr) | consistent |
| PP-22 | P2 | Values in Section 3 and the Abstract against Table S5 (S3) | PAT MIS3/LGM 65-70 against 70.3/65.7; HS1 75 against 74.8; ACR/YD 69 and 63 against 68.9/63.1; Holocene 47-51 against 47.1/50.7; AUS 9, 10, 11, 11, about 15, 23 against 9.1, 10.2, 11.3, 11.1, 14.5, 23.1; SAF MIS3 to ACR about 5 and 9 against 9.3/6.3/4.9/8.0, YD 15 against 14.6, Holocene about 11 against 10.7; NZ 14, 7, 6.5, 3, 6 against 14.2, 7.1, 6.6, 3.3, 5.9; PAP below 4 against 2.2/3.6/2.0, about 5 against 5.2/4.5, 11 against 11.0; Abstract 241 samples, PAT about 65 to 75 % and 49 % | all within 0.5 points; exceptions in GB-30, GB-31 |
| PP-23 | P1, P2 | Table S5 (EDC block) recomputed as period means of Table S1 with the bounds of l. 184 to 188 (S3, AB, SD, S4) | Largest deviation per period 0.03 to 0.05 points; for example Late Holocene (60) 50.7/0.0/12.0/11.6/21.4/3.8/0.6, Early Holocene (56) 47.1/0.0/10.0/9.8/24.9/8.1/0.0, Holocene (116) 49.0/0.0/11.0/10.7/23.1/5.9/0.3, YD (9) 63.1/0/4.5/14.6/14.5/3.3/0, ACR (8) 68.9/0/5.2/8.0/11.1/6.6/0.2, HS1 (27) 74.8/0/2.0/4.9/11.3/7.1/0, LGM (40) 65.7/0/3.6/6.3/10.2/14.2/0, MIS3 (41) 70.3/0/2.2/9.3/9.1/9.1/0 (PAT/CWA/PAP/SAF/AUS/NZ/ANT); Holocene as weighted mean (60 × 50.7 + 56 × 47.1)/116 = 48.96; row sums 99.9 to 100.1 (EDML 99.9 to 100.0) | Table S5 equals the unweighted means of Table S1 |
| PP-24 | P11 | Coverage of periods against the outputs announced in Methods and Discussion (S3) | Table S5 EDC: 8 periods; EDML: Early Holocene, YD, ACR, HS1, LGM (EDML 7 to 27 kyr, stated); box plots: Holocene, LGM (Figure 3), Early Holocene, YD, ACR, HS1, MIS3 (Figure S4); modelled isotopes for MIS3/LGM, HS1, ACR, YD, Holocene; per-sample R present; per-sample uncertainty missing; PSA fluxes missing; sub-regions present for PAP and SAF only | gaps in GB-19, GB-20, GB-28, GB-33 |
| PP-25 | P24, P3 | Figure 1: period bands, labels, smoothing, text values (AB) | Band edges per panel (ticks 0.4 and 3.0, ±48 yr): YD 11.69 to 12.91 kyr, HS1 14.68 to 18.01 kyr, MIS3 from 28.99 kyr against 11.7 to 12.9, 14.7 to 18, 29; ACR label overruns its interval by 2 px; smoothed curve equals a centred 9-point moving mean of Table S1 (SAF 12.3 measured against 12.6 at 10.4 kyr; 0.9 against 0.8 at 11.4 kyr); PAT minima of l. 194 at 10117 yr (20.4 %), 8508 yr (29.2 %), 6306 yr (26.4 %); AUS maxima of l. 205 at 9902 yr (45.7 %), 10511 yr (45.4 %), 6306 yr (41.8 %). Disclosed: the sampling gap explains the straight LGM segments | consistent; exceptions in GB-30, GB-31, GB-32 |
| PP-26 | P3 | Figure 3, LGM panel (AB) | Q1/median/Q3 measured against Table S1 (n = 40, exclusive quartiles, ±0.22): PAT 58.82/65.71/71.74 against 58.8/65.8/71.7; AUS 5.74/10.19/13.92 against 5.8/10.2/14.0; SAF 1.72/4.59/7.60 against 1.8/4.6/7.6; NZ 10.83/15.49/18.87 against 10.8/15.5/18.9; PAP 0/1.87/6.39 against 0/1.8/6.4; whiskers PAT 46.84 and 84.36 against 46.8 and 84.4; text l. 280 to 281 (SSA about 70 %, AUS about 10 %) against 69.3 and 10.2 | consistent |
| PP-27 | P3 | Figure S4, panels (2) to (5) (AB) | ACR (n = 8) PAT box 57.98/74.28/81.39 against 57.18/73.2/80.2; HS1 (n = 27) 67.99/76.04/80.56 against 67.0/75.0/79.4; MIS3 (n = 41) 63.41/71.57/78.41 against 62.45/70.5/77.25; ratio 1.014 to 1.015 throughout | sample sets agree, drawing scale differs (GB-34); YD in GB-48 |

### Segment 4: Discussion, conclusion, statements, references (pp. 7 to 22, 26, 28 to 29; supplement pp. 9 to 10, 20 to 21)

#### Substantive findings

**GB-36 "Continuous" and "high-resolution" are claimed for the whole record, although it has a sampling gap of 5.6 kyr in the LGM.**

| Field | Content |
|---|---|
| Check | P15, P6 |
| Location | p. 7, l. 220 to 221; p. 14, l. 472 to 473; p. 12, l. 403; p. 1, l. 17; p. 3, l. 89 to 90; p. 4, l. 113; supplement Table S1, rows 23104 and 25384 yr |
| Quotation | "we present the first continuous and quantitative record of dust provenance in the Epica Dome C ice core spanning the entire LGIT" (l. 220 to 221); "This study presents the first high-resolution, continuous and quantitative reconstruction of dust provenance in the EDC ice core over the Last Glacial-Interglacial Transition (LGIT)." |
| Concern | The Methods disclose "A sampling gap exists between 21.7 and 27.3 kyr BP, where only four samples were available" (l. 113), and 38 samples younger than 14 kyr BP were excluded (l. 174 to 175). Abstract, Discussion and Conclusion repeat "continuous" without qualification. In Table S1 the largest gaps between retained samples are 2280 yr (23104 to 25384 yr BP), 1785 yr (25640 to 27425 yr BP) and 954 yr (22150 to 23104 yr BP), against an average resolution of about 100 years (l. 110). The LGM means are not distorted by the gap (21 samples from 18 to 21.7 kyr BP give PAT 65.8 and NZ 13.6 against 65.7 and 14.2 for all 40; PP-34), but millennial changes between 21.7 and 27.3 kyr BP cannot be resolved. The grade is moderate rather than minor because the claim is repeated as the novelty of the study. |
| Suggestion | Qualify "continuous" in l. 17, l. 220 and l. 472 (for example "continuous except for a sampling gap between 21.7 and 27.3 kyr BP") and state the gap in the Conclusion. |
| Status | verified (l. 113, l. 174 to 175, wording); inferred (gap lengths and subset means computed from Table S1) |
| Severity | moderate |
| Source | S4, SD |

**GB-37 The Discussion and Conclusion place a major, significant shift at the onset of the ACR, but the ACR means do not differ from HS1, and no test is reported.**

| Field | Content |
|---|---|
| Check | P15 |
| Location | p. 7, l. 233 to 236; p. 7, l. 225 to 226; p. 14, l. 477 to 480; supplement p. 22, Table S5, rows HS1 and ACR; p. 12, l. 407 to 409 |
| Quotation | "Our calculations highlight a major shift in dust provenance occurred at the onset of the ACR" |
| Concern | Table S5 for EDC, HS1 then ACR: PAT 74.8 then 68.9; AUS 11.3 then 11.1; SAF 4.9 then 8.0; PAP 2.0 then 5.2; NZ 7.1 then 6.6. AUS does not rise, and PAT in the ACR (68.9) is higher than in the LGM (65.7). Mann-Whitney tests on Table S1 samples (HS1 n = 27, ACR n = 8) give p = 0.75 (PAT), 0.86 (AUS), 0.84 (SAF), 0.49 (PAP) and 0.15 for the sum of low-latitude sources; between HS1 and the Holocene PAT differs with p below 0.001. In 1 kyr windows of Table S1, PAT falls from 83.2 % (15 to 16 kyr BP, n = 8) to 72.0 % (14 to 15 kyr BP, n = 7) and the low-latitude sum rises from 11.4 % to 26.5 %, so a change near 15 kyr BP is visible but falls in late HS1, not at the ACR onset, and rests on 7 to 8 samples per window. "Significantly" (l. 235) and "marked" (l. 478) have no reported statistic, and the tentativeness stated in l. 407 to 409 does not reach the Conclusion. |
| Suggestion | In Section 4.1 (l. 233 to 236) and the Conclusion (l. 477 to 480) give the timing of the shift from the sample series (for example a change-point analysis on Table S1) instead of from period means; report a test with sample numbers for "significantly" or remove the word; carry the caveat of l. 407 to 409 into the Conclusion. |
| Status | verified (Table S5 values); inferred (tests and window means computed from Table S1) |
| Severity | moderate |
| Source | S4 |

**GB-38 The isotopic validation is described as agreement with values measured in EDC, but apart from three glacial values the measured data are from other ice cores.**

| Field | Content |
|---|---|
| Check | P15, P10, P3 |
| Location | p. 8, l. 258 to 260; p. 8, l. 254 to 257; p. 7, l. 238 to 240; p. 3, l. 93 to 94; p. 1, l. 25 to 27; Figure 2 (p. 26), open symbols; caption l. 857 to 866; supplement p. 21, Table S4, all rows |
| Quotation | "Overall, the close agreement between our modeled isotopic compositions and those measured in EDC for both glacial and interglacial intervals supports the robustness of our DEPOT algorithm" |
| Concern | Recalculating the bulk Sr and Nd signature from the modelled contributions (Eq. 3 and 4) is a sound independent test and the only validation in the manuscript (aim 2, l. 93 to 94). The measured values it is tested against do not support "measured in EDC" for the interglacial. Table S4 (page image p. 21) holds 35 measured pairs: 2 from EPICA Dome C (LGM), 1 from "Old Dome C" (HS1), 18 from Taylor Glacier and 14 from Berkner Island, so the Dome C share is 3/35 = 8.6 %. All 22 Holocene values come from Taylor Glacier (8) and Berkner Island (14), and the ACR and YD values from Taylor Glacier. The open circles of Figure 2 sit at the Table S4 positions (ring centres within 4 px; PP-28). The EDC Holocene values quoted in l. 240 (87Sr/86Sr about 0.710, εNd from -4.51 to -5.68) are neither in Table S4 nor in Figure 2, although the modelled Holocene value (87Sr/86Sr 0.7101, εNd -4.98, recomputed from Tables S3 and S5) lies close to them, so the supporting comparison exists in the text but is not shown. The manuscript itself argues that dust delivery differs between sectors (l. 415 to 416, l. 425 to 428), so agreement with sites in other sectors does not validate a site-specific EDC record. "Close agreement" is also not quantified: no misfit, no uncertainty on modelled or measured values, no matching of ages. The Abstract presents the same comparison as support ("aligns with changes observed in other East Antarctic ice cores", l. 26 to 27) without saying which cores; this location was added in the consolidation. |
| Suggestion | Add the EDC Holocene values quoted in l. 240 with their source to Table S4 and Figure 2; separate EDC from non-EDC comparison data by symbol and in l. 254 to 260; report for each measured EDC sample the modelled value at the matching depth or age window with Monte Carlo uncertainty and the residual, and test whether the measured values fall inside the modelled 95 % range; keep Taylor Glacier and Berkner Island as a separate regional comparison and name the cores in the Abstract; reword the conclusion of Section 4.1 according to the result. |
| Status | verified (composition of Table S4 on the page image; open symbol positions measured; values of l. 240 absent from Table S4 and Figure 2); inferred (share 3/35 and modelled Holocene value computed) |
| Severity | major |
| Source | S4, AB, SD, ZF |

**GB-39 Two combined shares in Section 4.2 differ from the sums of Table S5 by more than rounding, and one combines the wrong sources.**

| Field | Content |
|---|---|
| Check | P1, P15 |
| Location | p. 9, l. 276; p. 9, l. 295; supplement p. 22, Table S5, rows LGM and HS1 |
| Quotation | "(here, PAT+AUS is ~77%)" (l. 276); "This dominance persisted into HS1, with high-latitude sources totaling 84 %" |
| Concern | From Table S5: LGM PAT plus AUS = 65.7 + 10.2 = 75.9 (stated about 77); the models cited compare SSA and AUS, and SSA plus AUS = 65.7 + 0.0 + 3.6 + 10.2 = 79.5, which does not give 77 either. HS1 PAT plus NZ = 74.8 + 7.1 = 81.9 (stated 84; difference 2.1). Instance S3 also raised the LGM values "~79 %" and "~21 %" in l. 293 to 294, against 79.9 and 20.1 from Table S5, while instance S4 logged them as within rounding. On re-check the consolidation follows S4: approximate values within one point of the table are not raised; that part is not taken over. The qualitative statement (dominance of high-latitude sources) is not affected, but readers cannot reproduce the two numbers. |
| Suggestion | Replace "PAT+AUS is ~77%" in l. 276 by "SSA+AUS is ~80%" (or "PAT+AUS is ~76%") and "84 %" in l. 295 by "82 %", or name the subset the values come from. |
| Status | inferred (sums computed from Table S5) |
| Severity | moderate |
| Source | S3, S4 |

**GB-40 The average LGM contribution of New Zealand is given as about 11 % in Section 4.2 but as 14 % in Section 3 and 14.2 % in Table S5.**

| Field | Content |
|---|---|
| Check | P2, P3 |
| Location | p. 9, l. 281 to 282; p. 7, l. 209; Figure 3 (p. 27), LGM panel, NZ box; supplement p. 22, Table S5, row LGM, column NZ |
| Quotation | "However, we find a higher average NZ contribution (~11%), making it the second-largest dust source to EDC during the LGM." |
| Concern | Table S5 gives 14.2 % for NZ in the LGM, recomputed from Table S1 as 14.17 % (40 samples, median 15.5 %). The NZ LGM box of Figure 3 measures Q1 10.83, median 15.49, Q3 18.87. The sum in l. 293 to 294 (PAT plus NZ about 79 %) works only with 14.2 (65.7 + 14.2 = 79.9; with 11 it would be 76.7). A value near 11 results from pooling MIS3 and LGM: (9.1 × 41 + 14.2 × 40)/81 = 11.6, but l. 281 refers to the LGM only. The comparison with the 5 % of Coppo et al. (2022) and the ranking (AUS 10.2 %) hold either way. |
| Suggestion | Replace "(~11%)" in l. 282 by "(~14%)", or state which interval the 11 % refers to. |
| Status | verified (text, Table S5, Figure 3 measured); inferred (pooled value computed) |
| Severity | moderate |
| Source | S3, S4, AB |

**GB-41 The larger Holocene variability is interpreted as source and transport dynamics, but it coincides with shorter sample integration, lower concentrations and weaker fits, and samples of the same age differ strongly.**

| Field | Content |
|---|---|
| Check | P9 |
| Location | p. 9 to 10, l. 306 to 314; p. 4, l. 112 to 113; p. 6, l. 174 to 179; Figure 1; supplement p. 11, Table S1, rows 3559 yr (two rows); supplement p. 13, rows 10511 yr and 12841 yr (two rows each) |
| Quotation | "During YD and throughout the Holocene, our unmixing model reveals a significantly larger variability in the dust assemblages reaching EDC" |
| Concern | Three properties of the design change with the period and can produce the same pattern: (a) each Holocene sample integrates 2 to 3 years instead of 4 to 5 in the LGM (l. 112 to 113), so a single dust event weighs more; (b) Holocene concentrations are near the detection limit (l. 176 to 177); (c) the fit is weaker: in Table S1, 51 of 116 Holocene samples have R below 0.80 against 0 of 108 samples older than 14.7 kyr BP; the mean number of PSA with a non-zero contribution is 3.3 against 4.4, and single-PSA solutions above 90 % occur in 13 of 116 against 5 of 108. The standard deviation of PAT is 32.0 points in the Holocene against 9.8 (LGM), 10.6 (HS1) and 10.1 (MIS3). Four pairs of samples have identical ages; the Holocene and YD pairs differ strongly (3559 yr: PAT 86.7 against 0.0 %; 10511 yr: 38.2 points PAT and 36.9 SAF; 12841 yr: 32.4 PAT and 31.7 AUS), the LGM pair at 28709 yr by at most 10.2 points. If these pairs are replicates or adjacent samples, the scatter at one age in the Holocene is as large as the signal discussed in Section 4.3. "Significantly" (l. 306) is not backed by a test. The Holocene variability is a stated result for RQ1 and RQ3, hence the grade. What are the same-age pairs? |
| Suggestion | Before interpreting variability in Sections 3 and 4.3: report per sample the Monte Carlo interquartile range of each PSA and test whether differences between consecutive Holocene samples exceed it; state what the same-age pairs are and use them as an empirical reproducibility estimate; compare variability at equal integration time where possible; show variability against concentration and R. A design that separates the causes: unmix synthetic mixtures with fixed proportions after adding noise at Holocene and at LGM concentration levels and compare the recovered spread; attribute to source dynamics only the spread above that noise floor. Remove "significantly" or add the test. |
| Status | verified (integration times, concentrations, Table S1 values); inferred (counts, standard deviations, pair differences computed); assumption (nature of the same-age pairs, asked as a question) |
| Severity | major |
| Source | SD |

**GB-42 The agreement between the PAT record and the Potrok Aike wind proxy is asserted without a measure, and the drop at 6 to 6.5 kyr BP said to appear in both is not visible in the wind record.**

| Field | Content |
|---|---|
| Check | P15, P24 |
| Location | p. 10, l. 338 to 340; p. 11, l. 350 to 352; Figure 5 (p. 29), panels A and B |
| Quotation | "Overall, our Holocene provenance record for PAT contributions is matching well with the SWW intensity proxies in Potrok Aike bog (see Figure 5)." (l. 338 to 340); "Apart from a well-marked drop in PAT contributions between 6-6.5 kyr BP (also present in Potrok Aike wind intensity record)" |
| Concern | Neither text nor caption gives a correlation, a common time step or a lag analysis, and the Holocene PAT series is sparse and noisy (raw values from 0 to about 100 %). Measured on Figure 5 (300 dpi; panel B ±0.4 mT): the bold MDF line stays at 14.1 to 20.5 mT (5.0 to 6.0 kyr), 16.9 to 18.0 mT (6.0 to 6.5 kyr) and 15.3 to 17.2 mT (6.5 to 7.5 kyr), while the smoothed PAT of panel A has its minimum of 28.6 % at 6.0 to 6.5 kyr. Excursions elsewhere in panel B reach 42 mT (8 to 9 kyr); on the inverted axis a weaker wind would appear as a downward excursion, and there is none at 6 to 6.5 kyr. Panel B is almost flat from 3 to 8 kyr, while PAT varies between 27 and 72 %. "Matching well" is therefore a visual judgement the reader cannot check, and the stated common feature is not shown. |
| Suggestion | Remove "(also present in Potrok Aike wind intensity record)" in l. 351 or name the feature in Lisé-Pronovost et al. (2015) that is meant; give for the Holocene a measure of agreement (for example a correlation of the 9-step moving average with the MDF record resampled to the EDC ages, with sample number and significance), or weaken l. 338 to "shows similar features at". |
| Status | verified (wording, absence of a measure, Figure 5 measured) |
| Severity | moderate |
| Source | S4, AB |

**GB-43 The Potrok Aike record is called a bog in the text but lacustrine sediments of a lake in the caption and the cited reference.**

| Field | Content |
|---|---|
| Check | P38 |
| Location | p. 10, l. 339 to 340; p. 11, l. 348 to 349; p. 29, Figure 5 caption, l. 880 to 882; p. 19, l. 690 to 693 (Lisé-Pronovost et al., 2015) |
| Quotation | "the SWW intensity proxies in Potrok Aike bog (see Figure 5)" |
| Concern | The same record (MDF from Lisé-Pronovost et al., 2015) appears as "Potrok Aike bog" (l. 340, l. 349), "Potrok Aike wind intensity record" (l. 351) and as "lacustrine sediments in Laguna Potrok Aike" (Figure 5 caption, reference title). A bog is a peat archive, a laguna a lake archive, so the text names a different archive type from the one cited. The minor correction proposed by instance S4 for the same lines is included here. |
| Suggestion | Replace "Potrok Aike bog" in l. 340 and l. 349 by "Laguna Potrok Aike (lacustrine sediments)". |
| Status | verified (page images) |
| Severity | minor |
| Source | S2, S4, AB |

**GB-44 Figure 5 is cited before Figure 4.**

| Field | Content |
|---|---|
| Check | P3, P4 |
| Location | p. 10, l. 340 (first citation of Figure 5); p. 12, l. 405 (first citation of Figure 4) |
| Quotation | "Aike bog (see Figure 5)." |
| Concern | The first citations run Figure 1 (l. 183), Figure 2 (l. 244), Figure 3 (l. 281), Figure 5 (l. 340), Figure 4 (l. 405). Figures should be numbered in the order of their first citation. |
| Suggestion | Swap the numbers of Figures 4 and 5 (figures, captions and citations in l. 340, l. 405, l. 419), or move the comparison with Potrok Aike after Section 4.4. |
| Status | verified |
| Severity | minor |
| Source | S4, AB |

**GB-45 The Discussion dates the first Southern Altiplano contribution to after 11.2 kyr BP and links it to the desiccation of paleolake Coipasa, but Table S1 and Figure S3 show Altiplano contributions in the YD.**

| Field | Content |
|---|---|
| Check | P2, P6, P15, P24 |
| Location | p. 11, l. 357 to 360; p. 7, l. 211 to 212; supplement p. 13, Table S1, both rows 12841 yr, columns Puna and Altiplano; supplement pp. 5 to 6, Figure S3, Altiplano panel |
| Quotation | "the Southern Altiplano begins contributing dust only after approximately 11.2 kyr BP, a timing that coincides with the final desiccation of paleolake Coipasa" |
| Concern | Table S1 gives Altiplano contributions of 16.6 % and 12.8 % in the two YD samples dated 12841 yr, about 1.6 kyr before the stated onset; no other sample older than 11228 yr has Altiplano above zero. In Figure S3 the smoothed Altiplano curve is above zero from about 11.5 to 12.9 kyr (about 5 %, inside the YD band) and the raw line peaks at about 39 % near 11.9 kyr. The YD mean of PAP in Table S5 (4.5 %) consists of 3.3 % Altiplano and 1.3 % Puna (Table S1 means), so the YD input is not "primarily from the South Puna region" (l. 212); that holds for the ACR only (Puna 5.2 %, Altiplano 0.0 %). Since the argument in l. 358 to 360 is a timing coincidence, the earlier onset weakens the link to the Coipasa desiccation, which supports RQ3, hence the grade. Are the 12841 yr samples discounted, for example as replicates (GB-12)? |
| Suggestion | In l. 358 replace "only after approximately 11.2 kyr BP" by the first age with Altiplano contributions in Table S1 (12.8 kyr BP) or explain why those samples are discounted; reassess the coincidence with the Coipasa desiccation and the Tauca and Coipasa lake phases (Blard et al., 2011; Placzek et al., 2006) against that date; restrict "primarily from the South Puna region" in l. 212 to the ACR. |
| Status | verified (Table S1 on the page image; Figure S3 on the page image); inferred (YD and ACR means computed) |
| Severity | major |
| Source | S3, S4, AB, SD |

**GB-46 Several cited sources have no entry in the reference list, among them the data sources of the source database and of the measured isotopes.**

| Field | Content |
|---|---|
| Check | P4 |
| Location | p. 11, l. 365; p. 7, l. 238; p. 12, l. 416; supplement pp. 16 to 19, Table S2, column "Reference"; supplement p. 21, Table S4, column "Reference"; reference list pp. 16 to 22 |
| Quotation | "with the previous Pb isotopic study (Gili et al., 2016) ." |
| Concern | (a) Gili et al. (2016), l. 365, has no entry; the list has Gili et al. 2017 and 2022 only. The work is Gili, S., Gaiero, D.M., Goldstein, S.L., Chemale, F., Koester, E., Jweda, J., Vallelonga, P., Kaplan, M.R., 2016. Provenance of dust to Antarctica: A lead isotopic perspective. Geophysical Research Letters 43, 2291 to 2298, https://doi.org/10.1002/2016GL068244 (bibliographic record read). (b) The only Delmonte 2004 entry is a dust size paper (Climate Dynamics 23), but l. 238 cites Delmonte et al. (2004) for EDC 87Sr/86Sr and εNd values and Table S4 cites "Delmonte et al., 2004a", which implies a second 2004 work; the isotope data fit Delmonte, B., Basile-Doelsch, I., Petit, J.R., Maggi, V., Revel-Rolland, M., Michard, A., Jagoutz, E., Grousset, F., 2004. Comparing the Epica and Vostok dust records during the last 220,000 years: stratigraphical correlation and provenance in glacial periods. Earth-Science Reviews 66, 63 to 87, https://doi.org/10.1016/j.earscirev.2003.10.004 (abstract read); l. 416 fits the listed Climate Dynamics paper. (c) The supplement has no reference list, and sources cited there have no entry in the main list: Marx and Kamber, 2010 (101 rows of Table S2), Marx et al., 2005 (10), McGowan et al., 2005 (2), Diaz et al., 2018 (4), Aarons et al., 2017 (18 rows of Table S4), Bory et al., 2010 (14 rows of Table S4). So 117 of 217 database rows (53.9 %) and 32 of 35 measured isotope values cannot be traced to a full reference. |
| Suggestion | Add entries for Gili et al. (2016) and the isotope paper of Delmonte et al. (2004), and label the two Delmonte 2004 works 2004a and 2004b in l. 238, l. 416, the Figure 2 caption and Table S4. Add a reference list to the supplement, or add the supplement sources (Aarons et al., 2017; Bory et al., 2010; Diaz et al., 2018; Marx and Kamber, 2010; Marx et al., 2005; McGowan et al., 2005) to the main list. |
| Status | verified (absence of entries; counts in Tables S2 and S4 on the page images; existence of Gili et al., 2016); inferred (that the Earth-Science Reviews paper is the intended source for l. 238; values not checked in its full text) |
| Severity | moderate |
| Source | S4, S2, S1 |

**GB-47 The small number of ACR and YD samples is disclosed only in Section 4.4, not where the ACR and YD results are first reported.**

| Field | Content |
|---|---|
| Check | P17 |
| Location | p. 12, l. 407 to 409; p. 6 to 7, l. 192 to 193 and l. 203 to 212; p. 7, l. 233 to 236; Figure 2; Figure S4 |
| Quotation | "It is important however to note that results for ACR and YD are tentative due to the limited number samples covering those periods in EDC" |
| Concern | The caveat is given only for the EDML comparison. Section 3 reports ACR and YD means (PAT 69 % and 63 %, AUS about 15 %, SAF 15 %, NZ 6.5 % and 3 %) without sample numbers or caveat, and Section 4.1 places the "major shift" at the onset of the ACR (l. 233, GB-37). A reader of Section 3 does not see that these means rest on 8 and 9 samples (GB-48). |
| Suggestion | Give n per period next to every period mean in Section 3, Table S5, Figure 3 and Figure S4, and move the caveat from Section 4.4 to the first report of ACR and YD values. |
| Status | verified |
| Severity | moderate |
| Source | SD |

**GB-48 The number of EDC samples in the YD is given as 7, but Table S1, Table S5 and Figure S4 rest on 9.**

| Field | Content |
|---|---|
| Check | P2, P3, P36 |
| Location | p. 12, l. 407 to 409; supplement p. 13, Table S1, YD block; supplement p. 8, Figure S4, panel (2) YD |
| Quotation | "(8 and 7 samples in ACR and YD, respectively, compared to 47 and 27 in EDML)" |
| Concern | The YD block of Table S1 (page image p. 13) has nine rows: 11779, 11993, 12227, 12477, 12588, 12754, 12841, 12841, 12867 yr. The YD means of Table S5 are reproduced only with these nine (largest deviation 0.04 points; PAT 63.1), and the YD boxes of Figure S4 match them (PAT Q1/median/Q3 47.07/70.17/84.83 measured against 47.1/70.2/84.85 for n = 9). Counting the duplicated age 12841 once still gives 8. The ACR count of 8 is correct. The count matters for how tentative the ACR and YD comparison is (GB-47, GB-49). |
| Suggestion | Replace "8 and 7 samples" by "8 and 9 samples" in l. 408, or state which samples are excluded from the count and why, and explain the duplicate age. |
| Status | verified (rows counted on the page image; Table S5 reproduced; Figure S4 measured) |
| Severity | moderate |
| Source | S3, S4, AB, SD |

**GB-49 For the ACR and YD, the EDC minus EDML differences in PAT are swapped, and in the YD the SAF difference has the opposite sign to the one stated.**

| Field | Content |
|---|---|
| Check | P2, P3, P15 |
| Location | p. 13, l. 421 to 422; Figure 4 (p. 28), panels PAT, SAF, AUS, NZ, PAP, bars YD and ACR; supplement p. 22, Table S5, rows ACR and YD |
| Quotation | "the ACR and YD intervals exhibit a slight enrichment of Patagonian dust (+4 and +6.5%) in EDC, primarily at the expense of Southern African and Australian contributions." |
| Concern | Table S5: PAT ACR 68.9 minus 62.5 = plus 6.4; PAT YD 63.1 minus 58.4 = plus 4.7; the order of the sentence assigns them the other way round. SAF: ACR 8.0 minus 12.4 = minus 4.4, YD 14.6 minus 8.2 = plus 6.4, so in the YD EDC receives more SAF dust than EDML, which contradicts "at the expense of Southern African" for that period. AUS is minus 7.4 (ACR) and minus 4.5 (YD) as stated; in the YD, NZ (minus 3.9) and PAP (minus 2.4) also decrease. Figure 4 measured: PAT YD plus 5.06, ACR plus 6.58; SAF YD plus 6.58, ACR minus 4.68. The authors call the ACR and YD results tentative (l. 407 to 408); that caveat covers small sample numbers, not a reversal of sign. The minor correction proposed by instance SD for l. 422 is included here. |
| Suggestion | Write "(+6.4 and +4.7%, respectively) in EDC, at the expense of Southern African and Australian contributions in the ACR and of Australian, New Zealand and Puna-Altiplano contributions in the YD, while SAF is higher at EDC in the YD (+6.4%)". |
| Status | verified (Table S5; Figure 4 measured); inferred (differences computed) |
| Severity | moderate |
| Source | S3, S4, AB, SD |

**GB-50 The Holocene comparison of EDC and EDML sets the full EDC Holocene against the EDML Early Holocene only, although the text restricts the comparison to the overlapping interval.**

| Field | Content |
|---|---|
| Check | P21, P2, P3, P9 |
| Location | p. 13, l. 423 to 424; p. 12, l. 405 to 407; Figure 4 (p. 28), bar "Holo" in all five panels and bar "LGM"; caption l. 875 to 876; supplement p. 22, Table S5 |
| Quotation | "over their overlapping interval shared by both datasets, i.e., between 7.5 and 27 kyr BP" (l. 406 to 407); "EDC appears to receive substantially less PAT dust (-14%) but higher contributions of Australian dust (+12%) than EDML." |
| Concern | Table S5 gives EDML only for the Early Holocene (7.5 to 11.7 kyr). The stated values and the "Holo" bars of Figure 4 (measured: PAT minus 13.95, AUS plus 12.51, NZ plus 0.53) match EDC Holocene 2.8 to 11.7 kyr minus EDML Early Holocene: PAT 49.0 minus 62.7 = minus 13.7, AUS 23.1 minus 10.8 = plus 12.3, NZ plus 0.4, SAF minus 0.5. With the matched interval (EDC Early Holocene) the differences are PAT minus 15.6, AUS plus 14.1, NZ plus 2.6, SAF minus 1.4. The direction holds, but text and figure mix in 60 Late Holocene samples (4.7 kyr) outside the overlap the text defines. For the LGM the EDC mean covers 18 to 29 kyr, and 15 of its 40 samples lie beyond 27 kyr; restricted to 18 to 27 kyr (n = 25), EDC gives PAT 65.2 and NZ 14.3, a change below 1 point (PP-31). The caption gives no period limits. |
| Suggestion | Compute the Holocene bar of Figure 4 and the values in l. 423 to 424 from EDC 7.5 to 11.7 kyr BP (Table S5, "Early Holocene") and label it "Early Holocene"; compute the LGM bar from EDC 18 to 27 kyr; state the period limits and n of both cores in the caption. |
| Status | verified (Table S5 values; bars measured on the page image); inferred (matched differences computed) |
| Severity | moderate |
| Source | S3, S4, AB, SD |

**GB-51 The explanation of the low-latitude increase conflicts with statements on aridity and transport efficiency made earlier in the same Discussion.**

| Field | Content |
|---|---|
| Check | P15 |
| Location | p. 14, l. 463 to 466; p. 13, l. 440 to 443; p. 11, l. 368 to 374; p. 10, l. 310 to 311; p. 12, l. 400 to 401 |
| Quotation | "further enhanced by the long-term trend of increasing aridity in these regions and the greater efficiency of long-range atmospheric transport from low-latitude to Antarctica (see above)" |
| Concern | Section 4.3 states that central Australia had prolonged wet conditions between 14.5 and 4 kyr BP (l. 369) and that the Darling Basin had humid phases from about 13.5 to 11.5 and 9.5 to 7.5 kyr BP, possibly to 5.5 kyr BP (l. 372 to 374). AUS has the largest Holocene rise (10.2 % to 23.1 %, Table S5), so a long-term trend of increasing aridity does not hold for AUS by the manuscript's own account. On transport, Section 4.3 names "a reduced transport efficiency associated with enhanced «wet scavenging»" for the deglaciation and Holocene (l. 310 to 311) and explains the intermittent SAF signal by "reduced atmospheric transport efficiency during the Holocene" (l. 400 to 401); l. 465 to 466 then claims greater efficiency from low latitudes. A reconciliation is possible (reduced efficiency on mid-latitude routes, enhanced subtropical jet routes from elevated low-latitude sources, l. 429 to 435), but the text does not draw it. Together with GB-20, the closure effect alone may explain the AUS rise. |
| Suggestion | In the last paragraph of Section 4.4 state for which of AUS, SAF and PAP the cited records show increasing aridity, say which transport pathway is meant in l. 465 and how it relates to l. 310 to 311 and l. 400 to 401, and consider the closure effect (GB-20) before invoking emission changes. |
| Status | verified (all statements at the cited lines) |
| Severity | moderate |
| Source | S4 |

**GB-52 The Discussion says the data demonstrate a mechanism that the record can only show to coincide in time, and the timing of the shift is not determined with an uncertainty.**

| Field | Content |
|---|---|
| Check | P15, P10 |
| Location | p. 14, l. 466 to 470; p. 1, l. 29 to 31; p. 1, l. 23; p. 7, l. 225 and l. 233; p. 10, l. 315; p. 13 to 14, l. 445 to 453; p. 14, l. 477 to 482; p. 15, l. 488 to 490 |
| Quotation | "Importantly, our data demonstrate that these feedback mechanisms influenced dust deposition not only in EDML (in the Atlantic sector of East Antarctica) but also in EDC" |
| Concern | The joint use of the EDC and EDML records is a strength: a provenance shift seen in both cores (l. 444 to 447) is a stronger observation than either alone. What the EDC data show is a change in relative provenance near 15 to 14 kyr BP. The mechanisms (Meltwater Pulse 1A shelf submergence, drainage reversal, river planform change, l. 450 to 462) are not measured in this study; they are taken from the literature and linked by timing (l. 450, "coincides with"). The Abstract (l. 29, "We attribute") and the Conclusion (l. 481 to 482, "that we ascribed to") use fitting verbs; l. 466 raises the attribution to "demonstrate", and l. 469 to 470 state "spatially extensive and long-lasting effects" as established. The timing itself is given as about 14.5 kyr BP (l. 23, l. 225), "the onset of the ACR" (l. 233, 14.7 kyr), "after ~14.7 kyr BP" (l. 315) and "between 15 and 14 kyr BP" (l. 445); around 14.6 kyr the record has spacings of 260 and 115 years (14341, 14601, 14716 yr), and age-scale uncertainty is not considered (GB-13). No result separates the sea-level and drainage explanation from the alternatives the Discussion itself names: wet scavenging and transport efficiency (l. 310 to 314), SWW position (l. 340 to 343), low-latitude aridity (l. 441 to 443), AIM and Bølling onset and temperature (l. 298 to 299, l. 450 to 452). Aim (3) and the main conclusion of Abstract and Conclusion rest on this, hence the grade. |
| Suggestion | In l. 466 replace "our data demonstrate that" by "the synchronous shift in both cores is consistent with" and qualify l. 469 accordingly. Estimate the shift time with a change-point analysis on the sample series including Monte Carlo and age uncertainty, and compare it with Meltwater Pulse 1A on a common chronology. A design that tests the cause: compare the PAT contribution with the exposed shelf area derived from a sea-level curve across the whole record, not only at one step, and against the deuterium excess and nssCa records (Figure S2) at sample resolution. |
| Status | verified (wording, timing values and absence of own sea-level or hydrological data); inferred (sample spacing from Table S1; limits of causal inference from the design) |
| Severity | major |
| Source | S4, SD |

**GB-53 The Conclusion states as fact a cause that the Discussion gives as likely.**

| Field | Content |
|---|---|
| Check | P15 |
| Location | p. 14, l. 482 to 484; p. 9, l. 296 to 298 |
| Quotation | "This shift in provenance is effectively decoupled from the massive decline in dust deposition that occurred between 18 and 15 kyr BP due to changing atmospheric transport dynamics." |
| Concern | Section 4.2 says the decline "likely reflects intensified 'rainout' during long-range transport" (l. 296 to 297, with Markle et al., 2018). The manuscript does not test this cause; in the Conclusion the hedge is gone. |
| Suggestion | In l. 484 replace "due to changing atmospheric transport dynamics" by "which likely reflects changing atmospheric transport dynamics". |
| Status | verified |
| Severity | minor |
| Source | S4 |

**GB-54 The data availability statement says all data needed are present, but key inputs and outputs are missing, and further data are offered only on request without a reason.**

| Field | Content |
|---|---|
| Check | P12, P6 |
| Location | p. 16, l. 494 to 496; p. 4, l. 107 to 109; p. 4, l. 114; p. 6, l. 174; supplement p. 11, Table S1 |
| Quotation | "CODE/DATA AVAILABILITY. All data needed to evaluate the conclusions in the paper are present in the paper and/or the Supplementary Materials. Additional data related to the paper may be requested from the authors." |
| Concern | The supplement makes the source database (Table S2) and the per-sample median contributions (Table S1) accessible, which covers the two central derived tables. Missing are: the EDC REE input data of the 294 samples (Gabrielli et al., 2010), which are not in the supplement and for which no archive is named (an open copy of Gabrielli et al., 2010, read by instance S2, reports summary statistics and figures but no per-sample table); the cf_i (GB-14); the Monte Carlo spread (GB-19); the absolute PSA fluxes (GB-20); the identities of the 15 incomplete and 38 excluded samples (GB-25); source-level results (GB-28); code (GB-17); full references for most of Table S2 (GB-46). The data are geochemical and do not concern persons, and no reason is given for holding them back. |
| Suggestion | Extend the statement in l. 494 to list each source with its location: an archive DOI for the 294 EDC REE patterns (or a supplement table), the supplement tables proposed in GB-14, GB-19, GB-20, GB-25 and GB-28, and the code repository of GB-17; replace "may be requested" by a deposit or give a reason. |
| Status | verified (statement and contents of the supplement); inferred (contents of Gabrielli et al., 2010, from a partial reading) |
| Severity | moderate |
| Source | S2, SD |

**GB-55 The author contribution statement credits the measurements to "P.B", whose initials match no author.**

| Field | Content |
|---|---|
| Check | P38 |
| Location | p. 16, l. 497; p. 1, l. 4 to 5 (author list) |
| Quotation | "P.B performed the measurements; A.V., St. B and G.L. developed together the model" |
| Concern | The authors are Sibylle Boxho, Aubry Vanderstraeten, Nadine Mattielli, Goulven G. Laruelle, Aloys Bory, Paolo Gabrielli and Steeve Bonneville. No author has the initials P.B.; the other initials (A.V., St.B., G.L., Si.B.) resolve. Possible readings are P.G. (Paolo Gabrielli, who published the REE data set) or A.B. (Aloys Bory). It is also unclear which measurements are meant: the EDC REE data were published in 2010, and the six "this study" source samples of Table S2 are new (GB-10). Which author is meant? The minor correction proposed by instance S4 for the same line is included here. |
| Suggestion | Correct the initials in l. 497 and name the measurements, for example "P.G. measured the EDC REE concentrations (Gabrielli et al., 2010); X.Y. measured the new dust source samples in Table S2". |
| Status | verified (mismatch of initials on the page image); assumption (which author is meant, asked as a question) |
| Severity | minor |
| Source | S2, S4 |

**GB-56 One reference entry is not cited anywhere, and one is cited only in the supplement.**

| Field | Content |
|---|---|
| Check | P4 |
| Location | p. 18, l. 630 to 632 (Gaiero et al., 2007, Chemical Geology); p. 17, l. 594 to 595 (EPICA Community Members, 2006) |
| Quotation | "Gaiero, D.M., Brunet, F., Probst, J.-L., Depetris, P.J., 2007. A uniform isotopic and chemical signature" |
| Concern | The text cites "Gaiero, 2007" twice (l. 274, Figure 2 caption l. 862), which is the single-author entry; "Gaiero et al., 2007" appears nowhere in text or captions. EPICA Community Members (2006) is cited only in the caption of Figure S2. That is acceptable if the main list serves the supplement, but then the supplement sources of GB-46 (c) are missing by the same rule. |
| Suggestion | Cite Gaiero et al. (2007) where it was intended (perhaps in the Figure 2 caption as a source of PAT isotope domains) or delete the entry; state in the supplement that its references are in the main list, and apply that consistently. |
| Status | verified |
| Severity | minor |
| Source | S4 |

**GB-57 In Figure 2 the legend labels "Early Holocene" and "Holocene" do not match the plotted points: the light red points are Late Holocene samples and the dark red points Early Holocene samples.**

| Field | Content |
|---|---|
| Check | P3 |
| Location | Figure 2 (p. 26), legend and solid red symbols; open light red symbols; caption l. 863 to 866; supplement p. 22, Table S5, period definitions |
| Quotation | "REE-based calculated isotopic composition (blue to red dots corresponding to periods of LGIT)" |
| Concern | Modelled values were recomputed with Eq. 3 and Eq. 4 from the Table S1 medians and Table S3 end-members, and isolated points were measured on the page (300 dpi; ±0.00002 in 87Sr/86Sr, ±0.04 εNd). Light red (#fc5454, legend "EDC Early Holocene"): (0.72361, -13.17) is the 6570 yr sample (computed 0.7236, -13.17); (0.72000, -16.51) 3425 yr; (0.71972, -15.30) 7013 yr; (0.71587, -14.60) 5580 yr; (0.71582, -15.18) 4863 yr; all younger than 7.5 kyr, which Table S5 defines as Late Holocene. Dark red (#c40404, "EDC Holocene"): (0.71844, -12.36) is 10511 yr and (0.71731, -12.91) 8790 yr, both Early Holocene. Control: the yellow point (0.72745, -17.88) is the YD sample 12227 yr (0.7274, -17.87). The open Berkner Island rings carry the colour of "Iso Early Holocene", while Table S4 has no Early Holocene group, only "Iso Holocene". A reader therefore assigns the most radiogenic modelled values to the wrong half of the Holocene. The same exchange of labels appears in Figure 3 and Figure S4 (GB-33). |
| Suggestion | Relabel the light red solid symbols "EDC Late Holocene (2.8 to 7.5 kyr)" and the dark red ones "EDC Early Holocene (7.5 to 11.7 kyr)", give the age limits in the caption, and give the open symbols the grouping of Table S4 or add an Early and Late split to Table S4. |
| Status | verified (positions and colours measured; recomputation from Tables S1 and S3) |
| Severity | moderate |
| Source | AB |

**GB-58 Figure 2 cannot be read without the text: "Iso", MIS3 and a PSA domain name are not explained or do not match the text.**

| Field | Content |
|---|---|
| Check | P29 |
| Location | Figure 2 (p. 26), legend and domain labels; caption l. 857 to 866; p. 8, l. 251 to 252 |
| Quotation | "The modeled isotopic signatures for the end of MIS3/LGM, HS1, ACR, and the YD (represented on" |
| Concern | The legend colours match the text (LGM #0404fc, HS1 #34ccfc, ACR #34cc34, YD #fcc404). However: (1) the legend prefix "Iso" (open symbols) is not explained, the caption only says "open symbols"; (2) the legend has "EDC LGM" but no MIS3 entry, while l. 251 says blue stands for "end of MIS3/LGM", so the reader cannot tell whether the 41 MIS3 samples are plotted; (3) the domain label "Southern Central Western Argentina" differs from "Central Western Argentina (CWA)" in l. 129 and "CWA" in Table S1; (4) the caption does not say what the dashed lines on the Southern Africa domain mean. |
| Suggestion | Explain "Iso" (measured in ice cores, Table S4) in the caption; add MIS3 to the legend or state in l. 251 that MIS3 is not plotted; use one name for CWA throughout; explain the dashed domain border. |
| Status | verified (page image; colours measured) |
| Severity | minor |
| Source | AB |

**GB-59 Figure 5 has no time axis title, and its shaded bands and dashed lines are not explained.**

| Field | Content |
|---|---|
| Check | P29 |
| Location | Figure 5 (p. 29), panels A and B; caption l. 880 to 882; p. 10, l. 340 |
| Quotation | "Median Destructive Field of isothermal remanent magnetization (MDF) of lacustrine sediments in Laguna Potrok Aike" |
| Concern | (1) The x axis has values 0.5 to 3 but no title, unit or multiplier. (2) A blue band bounded by dashed lines and three gray bands are unexplained; the blue band measures 8.0 to 11.4 kyr (±45 yr), close to but not the "11 to 8 kyr BP" period of l. 340, and the gray bands of panel B are drawn 6 to 7 px to the right of those of panel A (YD end 12.85 kyr in A, 13.02 kyr in B). (3) The caption says that bold lines are 9-step moving averages; for panel B it is not stated whether the authors smoothed the MDF data or took them as published. The archive name is treated in GB-43. |
| Suggestion | Add "Age (kyr BP)" to both panels; explain the blue band (period and source) and the gray bands in the caption; align the bands; state the origin of the smoothing in panel B. |
| Status | verified (page image; band edges measured) |
| Severity | minor |
| Source | AB |

**GB-60 In Figure S5 the PAT panel has its own time axis, offset from the bands and the other panels.**

| Field | Content |
|---|---|
| Check | P3, P29 |
| Location | supplement pp. 9 to 10, Figure S5, top panel (PAT) and period bands; caption |
| Quotation | "Comparison between EDC and EDML ice cores in terms of dust provenance contributions (mobile average over 9 steps) through the LGIT" |
| Concern | The plot frame of the PAT panel runs from 391 px (7 kyr) to 3044 px (27 kyr), the four other panels from 374 to 3040 px (vector labels). The gray bands are one rectangle across all panels and match the lower panels (YD 11.70 to 12.97 kyr, HS1 14.77 to 17.96 kyr), but in the PAT panel they read 11.57 to 12.87 and 14.68 to 17.89 kyr, an offset of about 0.13 kyr. That is small, but l. 445 to 446 reads the decline between 15 and 14 kyr from this panel. The caption explains neither the bands nor the arrows for Holocene and LGM. |
| Suggestion | Put all panels on one axis and explain bands and arrows in the caption. |
| Status | verified (measured) |
| Severity | minor |
| Source | AB |

#### Minor corrections

| Code | Location | Quotation | Replacement | Source |
|---|---|---|---|---|
| KK-34 | p. 7, l. 220; supplement p. 21, Table S4, column "Localisation" | "in the Epica Dome C ice core"; "Epica dome C" | "in the EPICA Dome C ice core"; "EPICA Dome C" | S2 |
| KK-35 | p. 7, l. 236 | "This shift already describes by Gili et al. (2022) and Vanderstraeten et al. (2023), appears" | "This shift, already described by Gili et al. (2022) and Vanderstraeten et al. (2023), appears" | S4 |
| KK-36 | p. 8, l. 246 | "(Table S3, e.i. Eq.3)" | "(Table S3; Eq. 3)" | S4, SD |
| KK-37 | p. 8, l. 249 | "where the mean isotopic signatures is represents by CIR" | "where CIR_PSA represents the mean isotopic signature of each PSA" | S4 |
| KK-38 | p. 8, l. 261 (heading 4.2) | "4.2 Persistance of high-latitude dust source to EDC before 14.5 kyr BP" | "4.2 Persistence of high-latitude dust sources to EDC before 14.5 kyr BP" | S4 |
| KK-39 | p. 8, l. 270 (page image: "~763.10³ km²") | "expanding Patagonian outwash plains by ~763.10" | "expanding Patagonian outwash plains by ~763 × 10³ km²" | S4 |
| KK-40 | p. 8, l. 272 | "those from SSA- to EDC during the LGM and MIS3" | "those from SSA to EDC during the LGM and MIS3" | S4 |
| KK-41 | p. 9, l. 277 | "(i.e., Albani et al., 2012; Krätschmer et al., 2022)" | "(e.g., Albani et al., 2012; Krätschmer et al., 2022)" | S4 |
| KK-42 | p. 9, l. 300 | "high-latitude dominance before 14.5 kyr BP reflect a transport regime" | "high-latitude dominance before 14.5 kyr BP reflects a transport regime" | S4 |
| KK-43 | p. 9, l. 301; p. 10, l. 325; p. 13, l. 442 (parenthetical dashes set as spaced or unspaced hyphens, while l. 234, l. 291 and l. 431 use a long dash) | "strong westerlies -a system" and "reduction in SSA input -down to 33%-" and "(Ding et al., 2011) - and increased aridity" | set all parenthetical dashes in one form, the long dash without spaces as in l. 291 | S4 |
| KK-44 | p. 9, l. 302 (the LGIT is defined as the whole record in l. 90 and l. 221) | "provenance pattern until the onset of the LGIT" | "provenance pattern until ~14.5 kyr BP" | S4 |
| KK-45 | p. 10, l. 311 (guillemets; l. 297 uses English quotation marks) | "enhanced «wet scavenging» due to rising temperatures" | "enhanced “wet scavenging” due to rising temperatures" | S4 |
| KK-46 | p. 10, l. 312 to 313 | "trajectories inferred by increased deuterium-excess values" and "from the mid-latitudes of Indian Ocean" | "trajectories inferred from increased deuterium-excess values" and "from the mid-latitudes of the Indian Ocean" | S4 |
| KK-47 | p. 10, l. 321 (l. 326 and Table S5: 49.0 + 0.0 + 11.0 = 60.0) | "compared to 61% in our record when combining PAT, CWA, and PAP" | "compared to 60% in our record when combining PAT, CWA, and PAP" | S3, S4 |
| KK-48 | p. 10, l. 329 (abbreviation defined in l. 129) | "Although our Dust Source (DS) database" | "Although our DS database" | S4 |
| KK-49 | p. 10, l. 329 to 330 (the McMurdo sources are introduced in Section 2, l. 132 to 133) | "includes several McMurdo region sites (Section 4.2)" | "includes several McMurdo region sites (Section 2)" | S4 |
| KK-50 | p. 10, l. 334 (reference list: Speirs et al., 2010, p. 21, l. 781) | "(Speirs et al., 2001)" | "(Speirs et al., 2010)" | S4 |
| KK-51 | p. 10, l. 335 to 336 and l. 338 | "during the ACR, YD reaching minimum values" and "centered ~9 kyrs BP" | "during the ACR and YD, reaching minimum values" and "centered at ~9 kyr BP" | S4 |
| KK-52 | p. 10, l. 339 to 341 (SWW used in l. 339, defined in l. 340 to 341) | "a weakening of South Westerlies Winds (SWW)" and "Moreno et al. (2010);" | define at first use in l. 339 ("Southern Westerly Winds (SWW) intensity proxies"), then "a weakening of the SWW" and "Moreno et al., 2010;" | S4 |
| KK-53 | p. 10, l. 342 to 343 (reference list and l. 349: Quade and Kaplan, 2017) | "(Quake and Kaplan, 2017)" | "(Quade and Kaplan, 2017)" | S4 |
| KK-54 | p. 10, l. 346 | "Fires co-emit mineral soil-dust particle" | "Fires co-emit mineral soil-dust particles" | S4 |
| KK-55 | p. 11, l. 353 to 354 | "had its prime time in terms of contribution to EDC. Dust emission from PAP are primarily linked" | "made its largest contribution to EDC. Dust emissions from PAP are primarily linked" | S4 |
| KK-56 | p. 11, l. 365 (space before the full stop, page image) | "(Gili et al., 2016) ." | "(Gili et al., 2016)." (entry to be added, GB-46) | S4 |
| KK-57 | p. 11, l. 366 to 367 | "As far as Australian dust contribution, our model" and "De Deccker et al. (2010)" | "Regarding the Australian dust contribution, our model" and "De Deckker et al. (2010)" | S4 |
| KK-58 | p. 11, l. 374 and l. 376 | "(post-7.5 kry" and "El-Nino-Southern Oscillation (ENSO)" | "(post-7.5 kyr" and "El Niño Southern Oscillation (ENSO)" | S4 |
| KK-59 | p. 11 to 12, l. 381 to 382 (Figure S4 shows period box plots and no trend) | "results show an increasing trend in SAF dust contribution to EDC ice core (Figure S4)" | "results show an increasing trend in SAF dust contribution to EDC ice core (Figure 1; Table S5)" | S4 |
| KK-60 | p. 12, l. 384 to 385 (repetition, page image) | "suggesting strengthened dust transport from southern Africa suggesting strengthened dust transport from southern Africa (Stuut et al., 2002)" | "suggesting strengthened dust transport from southern Africa (Stuut et al., 2002)" | S4 |
| KK-61 | p. 12, l. 396 to 398 (the parenthesis before "~15.4" is not closed, page image) | "include few substantial inputs" and "kyr BP (Brook et al., 2011)." | "include a few substantial inputs" and "kyr BP; Brook et al., 2011)." | S4 |
| KK-62 | p. 12, l. 399 | "likely reflect their low-frequency, high-magnitude nature of their dust emissions" | "likely reflect the low-frequency, high-magnitude nature of their dust emissions" | S4 |
| KK-63 | p. 12, l. 406 to 408 (sample count see GB-48) | "over their overlapping interval shared by both datasets" and "limited number samples" | "over their overlapping interval" and "limited number of samples" | S4 |
| KK-64 | p. 13, l. 426 to 428 | "receive dust from Patagonia dust brought in the mid-" and "located at the interior of EAP" and "mid-latitude air masses incursions" | "receive Patagonian dust brought into the mid-troposphere", "located in the interior of the East Antarctic Plateau (EAP)" and "incursions of mid-latitude air masses" | S4 |
| KK-65 | p. 13, l. 439 (entry p. 17, l. 551: single author) | "(De Deccker et al., 2019;" | "(De Deckker, 2019;" | S4 |
| KK-66 | p. 14, l. 457 | "redirecting large portion of river catchment" | "redirecting a large portion of the river catchments" | S4 |
| KK-67 | p. 16, l. 496 (p. 1, l. 14 names two corresponding authors) | "Correspondence and requests should be addressed to Si.B." | "Correspondence and requests should be addressed to Si.B. and St.B." | ZF |
| KK-68 | p. 16, l. 497 | "St. B" | "St.B." (as in l. 498) | S2 |
| KK-69 | p. 16, l. 501 | "APPENDIX S. SUPPLENTARY DATA. Supplementary data to this article" | "SUPPLEMENT. The supplement related to this article is available online." | S4 |
| KK-70 | reference list pp. 16 to 22, 18 entries with printed RTF control codes (page images p. 16, 19, 20, 21): Bullard and McTainsh 2003; De Deckker et al. 2014; Dukes et al. 2018; Engelbrecht et al. 2019; Fletcher and Moreno 2012; Gaiero et al. 2007; Gingele and De Deckker 2005; Grousset and Biscaye 2005; Lisé-Pronovost et al. 2015; Markgraf et al. 2007; Markle et al. 2018; Moreno et al. 2010; Power et al. 2008; Quade and Kaplan 2017; Stone et al. 2010; Stuut et al. 2002; Veres et al. 2013; Wagner et al. 2021 | "471\uc0\u8211{}501. https://doi.org/10.1191/0309133303pp386ra\" | replace each code of the form \uc0\uNNNN{} by the character it encodes (8211 page range sign, 8217 apostrophe, 233 é, 237 í, 241 ñ, 176 °, 8242 prime, 8243 double prime, 8208 hyphen, 8212 long dash) and delete the trailing backslash after the DOI, for example "471 to 501" with the page range sign and "https://doi.org/10.1191/0309133303pp386ra" | S4 |
| KK-71 | reference list p. 20, l. 726 to 729 (no volume, pages or DOI) | "The EDC3 chronology for the EPICA Dome C ice core. Clim. Past." | "The EDC3 chronology for the EPICA Dome C ice core. Clim. Past [volume], [pages]. https://doi.org/[DOI]" (to be completed from the article) | S4 |
| KK-72 | reference list p. 20, l. 748 | "Environùental characterization" | "Environmental characterization" | S4 |
| KK-73 | reference list p. 20, l. 762 to 763 | "Holland HD, Turkian KK (eds). Pergamon:Oxford 1-64." | "Holland, H.D., Turekian, K.K. (Eds.). Pergamon, Oxford, 1-64." | S4 |
| KK-74 | reference list p. 21, l. 800 (text l. 266 cites "Sugden et al., 2009") | "Sudgen, D. E., McCulloch, R. D., Bory, A. J.-M., Hein, A. S., 2009." | "Sugden, D.E., McCulloch, R.D., Bory, A.J.-M., Hein, A.S., 2009." | S4 |
| KK-75 | p. 26, Figure 2 caption, l. 857 to 858 (measured ice core values are in Table S4) | "dust in ice cores (refs. Table S1" | "dust in ice cores (open symbols; values and references in Table S4" | S4, AB, SD |
| KK-76 | p. 26, Figure 2 caption, l. 863 | "Note that the SAF and AUS domain is more extended than showed in the Figure." | "Note that the SAF and AUS domains extend beyond the plotted area." | AB |
| KK-77 | p. 26, Figure 2 caption, l. 865 to 866 (end-member fingerprints and concentrations are in Table S3) | "(ii) the isotopic fingerprint (Table S4) and elemental concentration of the PSAs end-members (Table S3)." | "(ii) the isotopic fingerprint and elemental concentration of the PSA end-members (Table S3)." | S4, AB, SD |
| KK-78 | Figure 2 (p. 26), x axis tick labels; Figure 3 (p. 27) and supplement p. 8, Figure S4, y axis tick labels | "0,700" and "0,730"; "100,00" and "0,00" | "0.700" and "0.730"; "100" and "0" (decimal point, no superfluous decimals) | AB |
| KK-79 | p. 28, Figure 4 caption, l. 875 | "Histograms representing the contribution percentage difference" | "Bar charts of the difference in contribution (percentage points)" | AB |
| KK-80 | p. 28, Figure 4 caption, l. 876 (period averages of both cores are in Table S5) | "between EDC and EDML ice cores (Table S4)." | "between EDC and EDML ice cores (Table S5)." | S4, AB, SD |
| KK-81 | supplement p. 10, Figure S5, y axis title | "PAS EDC Contribution and PSA EDML Contribution ( in %)" | "PSA contribution, EDC and EDML (%)" | AB |

#### Verification log

| Code | Check | Checked | Values | Result |
|---|---|---|---|---|
| PP-28 | P15, P3 | Sr and Nd mixing with Eq. 3 and 4 from Table S3 end-members and Table S1 or S5 contributions; Figure 2 calibration and modelled points (S4, AB) | Period means: MIS3 0.7083 and -3.36; LGM 0.7083 and -2.61; HS1 0.7076 and -1.56; ACR 0.7082 and -2.92; YD 0.7094 and -5.38; Holocene 0.7101 and -4.98 (87Sr/86Sr and εNd). Figure 2 axes: 0.700 at 613.5 px, 0.730 at 1946.5 px; εNd +5 at 694.0 px, -25 at 1455.5 px. Per-sample ranges LGM 0.7065 to 0.7122 and -10.48 to +1.02; HS1 0.7063 to 0.7107 and -8.68 to +1.75; ACR 0.7066 to 0.7116 and -9.79 to +0.92; YD 0.7062 to 0.7274 and -17.87 to +1.59; ANT has no end-member and is omitted (largest ANT share among the checked samples 0.6 %); 8 isolated points matched to single samples; open symbols at the Table S4 positions | direction described in l. 251 to 257 reproduced; validation data in GB-38; legend in GB-57 |
| PP-29 | P15 | Each percentage in Section 4 against Table S5 (S4) | Agree: LGM SSA 69.3 against about 70 % (l. 282); LGM AUS 10.2 against about 10 % (l. 281); LGM PAP 3.6 against about 4 % (l. 289); EDML LGM NZ 6.2 against about 6 % (l. 288); LGM PAT + NZ 79.9 and AUS + SAF + PAP 20.1 against about 79 and 21 % (l. 293 to 294, approximate); Holocene AUS, PAP, SAF 23.1, 11.0, 10.7 and LGM 10.2, 3.6, 6.3 against 23, 11, 11 and 10, 4, 6 % (l. 317 to 318); Holocene PAT and NZ 49.0 and 5.9 (l. 319); Holocene SSA 60.0 (l. 326); LGM differences NZ plus 8.0, PAT minus 8.0 (l. 418 to 419); HS1 differences up to 5.3 (l. 420 to 421). Disclosed: ACR and YD tentative (l. 407 to 409) | consistent; disagreements in GB-39, GB-40, GB-49, GB-50, KK-47 |
| PP-30 | P24 | Figures S5 and S2 against text (AB) | l. 445 to 446 (PAT decline in both cores between 15 and 14 kyr): visible in Figure S5, EDC smoothed PAT from about 75 % near 14.3 kyr to about 52 % at 13.2 kyr, EDML to about 35 % at 14.2 to 14.5 kyr (read without calibration); l. 448 to 449 (decline of total dust from 19 to 18 kyr until about 15 kyr): Figure S2A nssCa flux from about 600 to near 0 between 18 and 14.6 kyr; l. 312 (deuterium excess higher after 10 kyr): Figure S2C about 7.5 before and 9 to 10 after 10.5 kyr | consistent; timing limited by GB-22, GB-60 |
| PP-31 | P9 | LGM window of the EDC and EDML comparison (EDC 18 to 29 kyr against stated overlap ending at 27 kyr) (SD) | EDC 18 to 27 kyr, n = 25: PAT 65.2, NZ 14.3, AUS 9.8, SAF 7.1, PAP 3.5; 18 to 29 kyr, n = 40: 65.7, 14.2, 10.2, 6.3, 3.6; differences at most 0.8 points. Disclosed: sampling gap holds 4 of the 25 samples (l. 113) | LGM differences of Figure 4 stand |
| PP-32 | P2 | EDC minus EDML differences for LGM and HS1 (l. 417 to 421) and the Abstract statement on secondary sources (l. 28 to 29) (S3) | LGM NZ 14.2 minus 6.2 = plus 8.0, PAT 65.7 minus 73.7 = minus 8.0; HS1 PAT plus 3.2, PAP minus 0.2, SAF minus 5.3, AUS plus 1.9, NZ plus 0.6. SAF higher in EDML in 4 of 5 shared periods (LGM -2.7, HS1 -5.3, ACR -4.4, Early Holocene -1.4; YD +6.4); AUS higher in EDC in 3 of 5 (LGM +0.5, HS1 +1.9, Early Holocene +14.1), lower in 2 (ACR -7.4, YD -4.5). Disclosed: ACR and YD tentative (l. 407 to 408) | consistent if "more consistent inputs" (l. 29) means more often higher; the phrase is not defined |
| PP-33 | P3 | Figure 4, all 25 bars measured against EDC minus EDML from Table S5 (AB) | PAT: Holo -13.95 (-13.7), YD 5.06 (4.7), ACR 6.58 (6.4), HS1 3.38 (3.2), LGM -8.17 (-8.0); AUS: 12.51 (12.3), -4.68 (-4.5), -7.57 (-7.4), 2.32 (1.9), 0.65 (0.5); SAF: -0.72 (-0.5), 6.58 (6.4), -4.68 (-4.4), -5.29 (-5.3), -3.0 (-2.7); NZ: 0.53 (0.4), -4.17 (-3.9), 3.56 (3.4), 0.68 (0.6), 8.26 (8.0); PAP: 1.89 (1.6), -2.35 (-2.4), 2.05 (1.8), below 0.3 (-0.2), 2.35 (2.2); bars read on average 0.2 high, about the outline thickness | bars equal Table S5 differences; window and order questions in GB-49, GB-50 |
| PP-34 | P15 | Synchronous PAT decline between 15 and 14 kyr BP (l. 445 to 447) and effect of the LGM sampling gap (S4) | 1 kyr windows from Table S1: PAT 83.2 % (15 to 16 kyr BP, n = 8), 72.0 % (14 to 15, n = 7), 64.3 % (13 to 14, n = 4); low-latitude sum 11.4, 26.5, 24.2 %. LGM 18 to 21.7 kyr BP (n = 21): PAT 65.8, NZ 13.6, AUS 10.1, SAF 6.7, PAP 3.8 against 65.7, 14.2, 10.2, 6.3, 3.6 for all 40. Disclosed: sampling gap (l. 113) | EDC part of l. 445 to 447 supported in direction; gap does not bias the LGM comparison |
| PP-35 | P4 | Numbering and cross-references in l. 219 to 501 and the captions of Figures 2, 4 and 5 (S4) | Sections 1 to 5 and 4.1 to 4.4 complete; Eq. 3 (l. 247) and Eq. 4 (l. 250) follow Eq. 1 and 2; Figures 1 to 5 each cited (first at l. 183, 244, 281, 405, 340); Figures S1 to S5 and Tables S1 to S5 each cited at least once (Figure S3 at l. 355); correct targets at l. 221, l. 244, l. 257, l. 281, l. 294 to 296, l. 299, l. 310, l. 312, l. 355, l. 405, l. 419, l. 446, l. 449 to 450 | wrong targets in KK-49, KK-59, KK-75, KK-77, KK-80; order in GB-44 |
| PP-36 | P4 | Citations in text and captions against the 91 reference entries, both ways; supplement citations against the main list (S4) | 89 distinct author and year strings; mismatches: Gili et al. 2016 (no entry), Speirs et al. 2001 (entry 2010), Quake (Quade), De Deccker 2010 and 2019 (De Deckker; 2019 single author), Sugden (Sudgen), Delmonte 2004 isotope paper (entry is another work); uncited entry Gaiero et al. 2007; EPICA Community Members 2006 only in the supplement; line-break artefacts checked by hand (Caldenius 1932, Magee et al. 2004, Stone et al. 2010, Weber et al. 2014, Lisé-Pronovost et al. 2015 are cited); "et al." and two-author forms correct | findings GB-46, GB-56, KK-50, KK-53, KK-57, KK-65, KK-74 |
| PP-37 | P16 | Language and typesetting in Segment 4 on pages 7 to 22, 26, 28, 29 and supplement pages 6, 8 and 21 (S4) | every minor correction of instance S4 confirmed on the page images; not counted: wide word spacing in justified reference lines with long DOIs (l. 521, l. 549, l. 559), the line-end split of "Lisé-Pronovost" (l. 341 to 342), sub- and superscripts that the extracted text flattens; journal names mixed between abbreviated and full forms (for example l. 505 against l. 509), a citation style check is an optional check | no further finding |
| PP-38 | P29, P3 | Figure inventory (AB) | Figure 1 (p. 24, caption p. 25, l. 851 to 854), five time series, cited l. 183, 205, 215, 217, 221, 307, 338; Figure 2 (p. 26, l. 857 to 866), scatter plot, cited l. 244, 252, 257; Figure 3 (p. 27, l. 869 to 873), box plots, cited l. 281, 294 to 295; Figure 4 (p. 28, l. 875 to 876), bar charts, cited l. 405, 419; Figure 5 (p. 29, l. 880 to 882), two time series, cited l. 340; Figures S1 to S5 in the supplement, cited l. 128, l. 167 and others, l. 355, l. 382, l. 405; no graphical abstract, no appendix figure; all figures raster except period labels of Figures 1, S2, S3 and the whole of Figure S5 | every figure cited; main figures out of order (GB-44) |
| PP-39 | P24 | Figure 5, axes and bands (AB) | x ticks in panel A at 685.5, 905.5, 1126.5, 1348, 1568 and 1788.5 px (0.5 to 3.0), evenly spaced at 220.6 px per 0.5; gray bands in A: HS1 14.71 to 18.00 kyr, MIS3 from 28.99 kyr; in B: HS1 14.77 to 17.99 kyr, MIS3 from 29.05 kyr; YD band in B 11.75 to 13.02 kyr; dashed lines at 7.96 and 11.44 kyr; panel A repeats the PAT series of Figure 1; text values for 7 to 8 kyr and since 5 kyr (l. 349 to 352) agree with panel A (smoothed PAT 61.1 to 71.6 % in 7.5 to 8.1 kyr, 46.3 to 54.2 % in 5 to 6 kyr) | consistent with l. 185 to 188; band offset and labels in GB-59 |

## Optional checks

| Area | What it needs | Responsible | Run |
|---|---|---|---|
| DOI resolution | one retrieval per reference entry with DOI | `science-quellenapparat-pruefung` | no |
| Citation style | the name of the style or the style rules of the target journal | `science-zitierstil-harvard-ctr` or the journal's style rules | no |
| AI statement against publisher policy | the AI policy of the target publisher | this review, on request | no |
| Relation to the authors' own prior work | the authors' prior work as files or DOIs; relevant here because the EDML record and the DEPOT method come from Vanderstraeten et al. (2023) | this review, on request | no |
| Journal requirements | the author guidelines of the target journal | this review, on request | no |
| Scientific accuracy | access to the sources of each checked statement; relevant here for the literature values in Segment 4 | `science-faktenbeleg-pruefung`, `geo-frage-belegbasiert-klaeren` | no |

## Limits of this review

- Version reviewed: egusphere-2025-5046.pdf, 29 pages, SHA-256 f598b53d01e375844cfb549eb05b9a3407bb30cae553e603c125d5f14886c722, with supplement egusphere-2025-5046-supplement.pdf, 22 pages, SHA-256 759cfa14195948f5772d3d6d696081932424f4296e51c812415527ed3b108ea6.
- Procedure: the six review instances (S1 to S4, AB, SD) ran as separate agents without shared context; the consolidation ran as a further agent, re-checked the quotations of all findings and minor corrections against the extracted text and the locations against the printed margin numbers of the page images, and recomputed the central numbers with Python.
- Unreadable sources: full texts of Coppo et al. (2022), Delmonte et al. (2007, 2008, 2017), Engelbrecht et al. (2019), Vanderstraeten et al. (2023), Delmonte et al. (2004, Earth-Science Reviews) and Aarons et al. (2017); Gabrielli et al. (2010) only partly read. Statements resting on them are marked inferred.
- Findings with status assumption: 1 of 60 (GB-18); a further 12 findings contain assumption sub-statements, which are put as questions to the authors.
- Optional checks run: 0 of 6.
- Discarded findings: 0 of 94 instance findings (all had the mandatory fields). One sub-statement was not taken over after re-check (l. 293 to 294, "~79 %" and "~21 %", GB-39).
- Merged findings: the 94 instance findings were consolidated into 59 findings, 33 of which combine findings or minor corrections of two or more instances; 6 instance findings covering several subjects (S2-GB-02, S4-GB-08, SD-GB-15, SD-GB-16, SD-GB-19, SD-GB-22) were split across the findings concerned. One finding was added by the consolidation (GB-24); 5 minor corrections were absorbed into findings, and the remaining 95 became 79 minor corrections (16 duplicates merged), plus 2 from the consolidation (KK-05, KK-67); 43 verification logs became 39.
- Hints outside the checklists: 63 from the six instances; 3 were taken up as items with source ZF (GB-24, KK-05, KK-67) and 1 as an added location (GB-38, Abstract l. 26 to 27); the others were already covered by findings or logs or would need the optional check of scientific accuracy, among them the literature values in l. 276 (70 to 90 %), l. 277 to 279 and l. 324 to 328 (Coppo et al., 2022), l. 287 (Neff and Bertler, 2015), l. 319 to 323 (DustCOMM), l. 238 to 240 (Delmonte et al., 2004), the transport direction in l. 431 to 432 and the use of Vallelonga et al. (2002) in l. 440.
- Line numbers on pages with equations (pp. 4, 5, 8) and in tables were set from the page images; supplement locations are given by page and element.
