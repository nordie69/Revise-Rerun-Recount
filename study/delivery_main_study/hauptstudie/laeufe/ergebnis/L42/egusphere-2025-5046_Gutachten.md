# Review report: Quantifying Southern Hemisphere dust sources during the Last Glacial-Interglacial Transition using rare earth elements in the EPICA Dome C ice core

| Field | Value |
|---|---|
| Manuscript | Boxho, S., Vanderstraeten, A., Mattielli, N., Laruelle, G. G., Bory, A., Gabrielli, P., Bonneville, S. (2025): Quantifying Southern Hemisphere dust sources during the Last Glacial-Interglacial Transition using rare earth elements in the EPICA Dome C ice core. EGUsphere preprint egusphere-2025-5046, https://doi.org/10.5194/egusphere-2025-5046 |
| Reviewed version | egusphere-2025-5046.pdf, 29 pages, SHA-256 f598b53d01e375844cfb549eb05b9a3407bb30cae553e603c125d5f14886c722; supplement egusphere-2025-5046-supplement.pdf, 22 pages, SHA-256 759cfa14195948f5772d3d6d696081932424f4296e51c812415527ed3b108ea6 |
| Date | 2026-10-18 |
| Language | English |
| Check instances | Segments 1 to 4, figures, study design; the six check instances ran as separate agents, each without context of the others; merging, overall assessment and format check in a further separate agent |

## Summary

The manuscript is a modelling study on a published geochemical dataset. It applies a constrained least-squares unmixing algorithm (DEPOT; MATLAB lsqnonneg with non-negativity, 2000 Monte Carlo runs per sample, median as estimate) to 13 UCC-normalised rare earth elements (Gd removed) of the EPICA Dome C dust record of Gabrielli et al. (2010), fitted against a database of 217 dust source patterns from seven potential source areas (Patagonia PAT, Central Western Argentina CWA, Puna-Altiplano PAP, Southern Africa SAF, Australia AUS, New Zealand NZ, Antarctica ANT). Of 294 samples, 15 were removed for missing data and 38 at a fit threshold R ≥ 0.67, leaving 241 samples from 33.7 to 2.9 kyr BP on the EDC3 chronology (mean R 0.852). Period means give PAT 70.3, 65.7 and 74.8 % for MIS3, LGM and HS1 and 49.0 % for the Holocene, while AUS rises from 10.2 % (LGM) to 23.1 % (Holocene) and PAP from 3.6 to 11.0 %. The record is checked by a forward Sr-Nd isotope calculation against literature values, related to regional climate proxies, and compared with the authors' earlier EDML record; the provenance shift around 14.5 kyr BP is attributed to submersion of the Patagonian shelf and reorganisation of Patagonian rivers.

## Strengths

1. The supplement publishes the per-sample median contributions (Table S1) and the period means (Table S5) in a form that lets a reader recompute every quoted percentage: all 56 EDC cells of Table S5 are reproduced to 0.1 percentage points as means of Table S1 with the period bounds of l. 185 to 188, and the sample balance 294, 279, 241 closes (PP-18, PP-19). This transparency is what makes the numerical checks of this review possible at all.
2. The dust source database is fully disclosed: Table S2 lists all 217 patterns with reference, sample type, location and coordinates, and Tables S3 to S5 hold the isotope end-members, the ice-core isotope values and the period averages (PP-08). The end-member side of the unmixing can therefore be inspected row by row, which is how the duplicated and anomalous rows were found (GB-14, GB-26).
3. The forward calculation of 87Sr/86Sr and εNd from the REE-based contributions (Eq. 3 and 4) tests the unmixing against an independent tracer; recomputed from Tables S1, S3 and S5 it reproduces the per-sample spread plotted in Figure 2 and a single YD sample at the SAF end-member, and the modelled LGM mixture (0.7083, εNd minus 2.62) lies close to the measured EDC LGM values (PP-29, PP-30). The test is sound in design; what it is compared with is the subject of GB-39.
4. The manuscript discloses its main sampling limits itself (the 21.7 to 27.3 kyr gap with four samples, the exclusion of 38 low-concentration samples, the tentative ACR and YD results, the 9-step smoothing in Figure 1), and its period definitions are applied consistently: the period zones of Figure 1 match the stated bounds within 0.02 kyr, and the Figure 4 bars for YD, ACR, HS1 and LGM match the Table S5 differences within 0.31 points (PP-07, PP-25, PP-32).

## Weaknesses

1. The EDC data establish a glacial to Holocene contrast but not the timing or the cause of the shift that the abstract and conclusion state: per-sample PAT stays at HS1 level until about 13.4 kyr BP, the ACR means lie within the glacial range for every PSA except PAP, the attribution to shelf submersion and river reorganisation rests on temporal coincidence and on the EDML record, and the conclusion adds a cause for the between-site differences that the discussion does not develop (GB-37, GB-55, GB-56, GB-58). A change-point analysis with the Monte Carlo spread on one chronology, and wording that matches a coincidence ("is consistent with"), would align the claims with what the data show.
2. Both external checks of the record rest on mismatched comparands: the interglacial "agreement with values measured in EDC" uses Taylor Glacier and Berkner Island values, the EDC to EDML Holocene differences compare the whole EDC Holocene with the EDML Early Holocene and a 13-element with a 14-element configuration, and the ACR and YD differences are swapped in the text (GB-17, GB-39, GB-51, GB-53). Comparing like with like (EDC values, identical windows, identical configuration) and stating the uncertainty of each difference would make research aims (2) and (4) testable.
3. Several inputs and choices that shape every contribution are untested or unreported: the recovery accuracy of an underdetermined unmixing with 13 equations and 217 coefficients, Antarctic end-members that appear not to be UCC-normalised, the correction factors, an analytical uncertainty below the published total for Holocene samples, and a selection of samples by their own fit quality with a threshold that does not match the stated test (GB-11, GB-13, GB-15, GB-18, GB-21, GB-22, GB-29). Leave-one-out and synthetic-mixture tests, the published element-specific uncertainties and a reported Monte Carlo spread per sample would show which Holocene features exceed noise.
4. Several literature statements do not match their sources (model support attributed to Krätschmer et al., the reading of Coppo et al., the pCO2 range, a missing EDC lead isotope study that reports local Antarctic dust), several quoted values differ from Tables S1 and S5, and the input REE data, the code and the announced PSA fluxes are not available (GB-04, GB-20, GB-34, GB-41, GB-42, GB-44, GB-45, GB-59). Checking each cited number against its source with page, taking all quoted values from the tables, and depositing data and code in a repository would close these gaps.

## Findings by segment

### Segment 1: Abstract, introduction (pp. 1 to 3)

#### Substantive findings

**GB-01 The study period and the term LGIT are given with inconsistent bounds.**

| Field | Content |
|---|---|
| Check | P2, P38 |
| Location | p. 1, l. 18; p. 2, l. 44; p. 3, l. 90 to 91; p. 4, l. 109 to 110; p. 6, l. 182 and l. 187; p. 7, l. 220 to 221; p. 9, l. 300 to 304; p. 14, l. 473; supplement p. 9, Figure S5 caption; supplement p. 11, Table S1, first and last row |
| Quotation | "from 33.7 to 2.9 kyr BP" and "during the LGIT from 33.6 kyr to 2.8 kyr BP" and "a remarkably stable provenance pattern until the onset of the LGIT" and "from 14.5 kyr BP until 2.7 kyr BP" |
| Concern | Table S1 runs from 2852 to 33699 yr BP, which rounds to 2.9 and 33.7 kyr as in the abstract (l. 18) and l. 182; the introduction gives 33.6 and 2.8 kyr (l. 90 to 91), the Holocene is defined to end at 2.8 kyr (l. 187) and l. 304 gives 2.7 kyr. The abbreviation LGIT is defined in l. 44 without bounds; l. 90 to 91, l. 221 and l. 473 use it for the whole record including MIS3, l. 302 places its onset at about 14.5 kyr BP, and the Figure S5 caption applies it to 7 to 27 kyr BP. The central statement of Section 4.2, stability "until the onset of the LGIT", therefore has no defined reference point. |
| Suggestion | Define the LGIT with explicit bounds at l. 44; use "the study period (33.7 to 2.9 kyr BP)" in l. 90 to 91, l. 221 and l. 473; use 2.9 kyr in l. 91, l. 187 and l. 304; in l. 302 name the event meant (for example "until about 14.5 kyr BP"). |
| Status | verified |
| Severity | minor |
| Source | S2, S3, S4 |

**GB-02 The abstract claims a first quantification of Southern Hemisphere dust source contributions, while cited and uncited works already quantify such contributions.**

| Field | Content |
|---|---|
| Check | P28, P14 |
| Location | p. 1, l. 19 to 20; p. 3, l. 74 to 81; p. 9, l. 277 to 279; p. 10, l. 319 to 323 |
| Quotation | "Using a statistical unmixing algorithm on 241 samples, we quantify for the first-time contributions from key Southern Hemisphere dust sources." |
| Concern | The manuscript names no databases, terms, period or date of a literature search. The claim is not restricted to EDC or to REE, and works cited by the manuscript contradict it in this general form: Vanderstraeten et al. (2023) quantified the same sources for EDML (l. 74 to 81), Coppo et al. (2022) give LGM percentages for East Antarctica (l. 277 to 279), and Kok et al. (2021) give present-day shares (l. 319 to 323). Not in the reference list: Longman, J., Struve, T., Pahnke, K. (2022) Spatial and temporal trends in mineral dust provenance in the South Pacific: evidence from mixing models. Paleoceanography and Paleoclimatology 37, e2021PA004356, https://doi.org/10.1029/2021PA004356. With Bayesian mixing models of Pb and Nd isotopes they report a South American share of South Pacific dust of 53 % in the LGM and 31 % in the Holocene and an Australian share of 38 % and 55 %, the same direction of change for a neighbouring sink. This narrows the novelty to the continuous REE-based record at EDC; it does not contradict the result. |
| Suggestion | Restrict l. 19 to 20 to what is new, for example "we provide the first continuous, quantitative REE-based record of Southern Hemisphere dust source contributions at EDC"; cite Longman et al. (2022) in Section 1 after l. 76. |
| Status | verified |
| Severity | moderate |
| Source | S1 |

**GB-03 The link between dust flux, export productivity and iron fertilisation is credited to ice-core studies, but the cited work is a marine sediment record.**

| Field | Content |
|---|---|
| Check | P13 |
| Location | p. 2, l. 36 to 40 |
| Quotation | "Over recent decades, studies on these ice cores have revealed the connection between dust fluxes, ocean export productivity, and the development of deep glaciations" |
| Concern | The statement on iron fertilisation matches the source, the archive does not: Martínez-García et al. (2014, Science 343, 1347 to 1350) measured foraminifera-bound nitrogen isotopes "in a sediment core from the Subantarctic Atlantic"; dust flux, productivity and nitrate consumption come from that marine core. |
| Suggestion | In l. 36 to 37 write "studies of ice-core and marine sediment records have revealed ...", keep Martínez-García et al. (2014) for the marine evidence and add an ice-core reference already in the list, for example Lambert et al. (2008). |
| Status | verified |
| Severity | minor |
| Source | S1 |

**GB-04 The pCO2 lowering attributed to dust-borne iron fertilisation exceeds the values given in both cited studies.**

| Field | Content |
|---|---|
| Check | P13 |
| Location | p. 2, l. 40 to 42 |
| Quotation | "Enhanced iron delivery by atmospheric dust during glacial periods are modelled to have lowered the atmospheric pCO2 by ~20 to 40 ppmv" |
| Concern | The second half of the sentence is faithful: Lambert et al. (2021) attribute about one quarter of the LGM to Holocene rise to a stronger biological pump. The range is not. Lambert et al. (2015, Geophys. Res. Lett. 42, 6014 to 6023) conclude that LGM pCO2 "was reduced by ~20 ppm due to enhanced dust loads"; Lambert et al. (2021, Earth Planet. Sci. Lett. 554, 116675, author repository version) give 12 to 29 ppmv for global iron fertilisation (Table 2 up to 33.1 ppmv). One quarter of the 180 to 260 ppmv rise is (260 minus 180) / 4 = 20 ppmv. The upper bound of 40 ppmv exceeds the largest value in the text of Lambert et al. (2021) by 11 ppmv (40 / 29 = 1.38), the largest table value by 6.9 ppmv and the estimate of Lambert et al. (2015) by a factor of 2. Graded moderate because it misstates the content of the sources; it does not touch the results. |
| Suggestion | In l. 41 replace "~20 to 40 ppmv" by "~20 ppmv (12 to 29 ppmv across model experiments)", or cite the source that gives 40 ppmv. |
| Status | verified |
| Severity | moderate |
| Source | S1 |

**GB-05 The introduction understates what the earlier REE studies of the same EDC dataset found, and the deglacial shift is credited only to later works.**

| Field | Content |
|---|---|
| Check | P13 |
| Location | p. 3, l. 72 to 74; p. 7, l. 236 |
| Quotation | "Previous studies using REE patterns in Antarctic ice cores (e.g., Gabrielli et al., 2010; Wegner et al., 2012) achieved multi-decadal resolution but could not fully resolve dust provenance." and "This shift already describes by Gili et al. (2022) and Vanderstraeten et al. (2023)" |
| Concern | The manuscript rightly states that the earlier studies did not quantify contributions. But both identified the shift that the manuscript presents as a main result (l. 23 to 25, l. 225 to 226, l. 233 to 236). Gabrielli et al. (2010, Quat. Sci. Rev. 29, 265 to 273), on the dataset reused here (l. 108): "Starting at ~15 kyr BP, there was a major change in dust composition, the variable character of which persisted throughout the Holocene." Wegner et al. (2012, Clim. Past 8, 135 to 147), abstract: "After 15 000 yr BP, multiple sources such as Australia and New Zealand become relatively more important". A reader of l. 72 to 74 and l. 236 cannot tell that direction and timing of the shift at EDC were known from the same REE data and that the new contribution is its quantification by source. |
| Suggestion | In l. 72 to 74 state what the two studies found (a change near 15 kyr BP towards a more variable composition with relatively more Australian and New Zealand dust) and what they could not do; in l. 236 add Gabrielli et al. (2010) and Wegner et al. (2012). |
| Status | verified |
| Severity | moderate |
| Source | S1 |

**GB-06 Further priority and uniqueness claims are made without a description of the literature search.**

| Field | Content |
|---|---|
| Check | P28 |
| Location | p. 3, l. 74 to 76; p. 1, l. 17; p. 7, l. 220 to 221; p. 12, l. 403 to 404; p. 14, l. 472 to 473 |
| Quotation | "we presented the first quantitative apportionment algorithm based on REE pattern fitting" and "The only continuous and quantitative dust provenance record in EA available for direct comparison with our EDC data" |
| Concern | None of the claims (also l. 17 "a novel continuous, high-resolution reconstruction", l. 220 "the first continuous and quantitative record", l. 472 "the first high-resolution, continuous and quantitative reconstruction") is backed by named databases, search terms, period or date. Searches for this review found no earlier continuous quantitative provenance record at EDC; Vallelonga et al. (2010) and Coppo et al. (2022) give quantitative or semi-quantitative but discontinuous information (GB-45). The claim in l. 74 to 76 is broad: it is not restricted to ice cores, and REE-based mixing approaches for sediment provenance exist in other settings. |
| Suggestion | Add to Section 1 one sentence naming the databases searched, the search terms, the period and the date, or restrict the wording, for example in l. 74 "the first quantitative apportionment algorithm for Antarctic ice-core dust based on REE pattern fitting, to our knowledge". |
| Status | verified (absence of a search description); inferred (absence of earlier work, few queries) |
| Severity | moderate |
| Source | S1 |

#### Minor corrections

| ID | Location | Quotation | Replacement | Source |
|---|---|---|---|---|
| KK-01 | p. 1, l. 20 | "During the Marine isotope 3 (MIS3)" | "During Marine Isotope Stage 3 (MIS3)" | S2 |
| KK-02 | p. 1, l. 27; p. 3, l. 77 | "Comparison with the EDML ice core"; "Our results for EDML ice core" | "Comparison with the EPICA Dronning Maud Land (EDML) ice core"; "Our results for the EPICA Dronning Maud Land (EDML) ice core" | S2 |
| KK-03 | p. 2, l. 44 to 46 | "dust deposition rates are primarily influenced by both the geographic location of dust sources and the residence time of dust in the atmosphere (Lambert et al., 2008)" | "dust deposition rates are primarily influenced by the strength of the dust sources and the lifetime of dust in the atmosphere (Lambert et al., 2008)"; the abstract of Lambert et al. (2008) names sources and lifetime, not location | S1 |
| KK-04 | p. 2, l. 63 | "dust fluxes are up to 25 times lower than LGM fluxes (e.g. Delmonte et al., 2008; Delmonte et al., 2017)" | "dust fluxes are about 25 times lower than LGM fluxes (Lambert et al., 2008)"; the ratio is in Lambert et al. (2008), not in the abstracts of the two Delmonte papers | S1 |
| KK-05 | p. 3, l. 73 | "achieved multi-decadal resolution" | "achieved decadal to centennial resolution (sample spacing ~60 years in the Holocene and ~140 years in the last glacial at EDC; Gabrielli et al., 2010)" | S1 |

#### Verification log

| ID | Check | Checked | Values | Result |
|---|---|---|---|---|
| PP-01 | P28 | Novelty and gap claims, l. 17, 19 to 20, 74 to 76, 92, 220 to 221, 403 to 404, 472 to 473, against a search description and own queries (S1) | No databases, terms, period or date named; four own queries targeting EDC claims found no earlier continuous quantitative record at EDC; l. 92 "no consensus" is evaluative, not a gap claim | no finding beyond GB-02 and GB-06 |
| PP-02 | P2 | Abstract figures against Results and Table S5 (S3) | 241 samples (l. 19; Table S1); Patagonia ~65 to 75 % in MIS3, LGM, HS1 (70.3, 65.7, 74.8); Holocene ~49 % (49.0); span 33.7 to 2.9 kyr (Table S1 33699 and 2852 yr BP) | no finding |
| PP-03 | P13 | Every sentence of l. 1 to 98 with numbers, rankings or evaluations from cited works (S1) | l. 34 to 36 Lambert et al. (2008) consistent; l. 46 to 49 Qu (2016), Shi et al. qualitative, titles match; l. 64 to 67 Delmonte et al. (2020) "great mixture from multiple sources", consistent; l. 74 to 87 Vanderstraeten et al. (2023) abstract: Patagonia ~68 %, below 50 % after 14.5 kyr consistent within rounding; l. 88 to 91 Gabrielli et al. (2010): 294 sections, 2.9 to 33.7 kyr, gap 21.7 to 27.3 kyr with four samples, consistent | no finding beyond GB-03, GB-04, GB-05, KK-03 to KK-05 |
| PP-04 | P10 | Stated gaps against research questions 1 to 4, l. 43 to 44, l. 59 to 68, l. 91 to 98 (SD) | RQ1 (descriptive, gap l. 43 to 44 and l. 92): design adequate; RQ2 from limits of isotopes (l. 59 to 68); RQ3 without explicit gap; RQ4 implied by l. 403 to 404 | no finding beyond GB-37, GB-39, GB-51 |
| PP-05 | P18 | Principles the manuscript states for other methods, applied to its own (SD) | Overlapping isotope fields hamper source discrimination (l. 64 to 65); the same argument is not applied to similar REE patterns in the database; no other stated principle | no finding beyond GB-13 |
| PP-06 | P14 | Positioning: contribution in one sentence, six queries, candidates checked against the reference list (S1) | Candidates: Vallelonga et al. (2010) absent (GB-45); Longman et al. (2022) absent (GB-02); Aarons et al. (2017) cited only in Table S4 (GB-66); Delmonte et al. (2020), Revel-Rolland et al. (2006), De Deckker et al. (2010), Paleari et al. (2019), Koffman et al. (2021) in the list | no finding beyond GB-02, GB-45 |

### Segment 2: Materials and methods, supplement Figures S1 and S2, Table S2 (pp. 3 to 5)

#### Substantive findings

**GB-07 The data class and grain size of the source patterns are not stated in the main text, although most of them are coarser fractions than ice-core dust.**

| Field | Content |
|---|---|
| Check | P19 |
| Location | p. 4, l. 104 to 106, l. 126 to 133; p. 6, l. 197 to 198; supplement pp. 16 to 19, Table S2, column "Type of sample" |
| Quotation | "literature reported patterns from known potential source areas (PSA) across the Southern Hemisphere" |
| Concern | Table S2 (count of the sample type column) holds 100 DS of the fraction below 90 µm, 8 below 63 µm, 44 below 5 µm, 41 aeolian dust, 12 soil, 6 surface sediment, 4 bulk loess, 1 bulk and 1 dust trap. All 100 AUS samples below 90 µm come from one source (Marx and Kamber, 2010). The main text calls the database "well-established dust source regions" (l. 127) and does not mention that the end-members are a heterogeneous compilation of different size fractions. Do the REE patterns of the coarser fractions represent the fine dust that reaches EDC? |
| Suggestion | In Section 2 describe sample types and size fractions per PSA and test whether contributions change when only fine fractions or aeolian dust are used. |
| Status | verified (counts in Table S2); assumption (effect of grain size on the patterns, asked as a question) |
| Severity | moderate |
| Source | SD |

**GB-08 "PSA" names both the seven source regions and the 217 individual dust sources, and "end-member" names both the 217 samples and the regional means.**

| Field | Content |
|---|---|
| Check | P38 |
| Location | p. 4, l. 105 to 106, l. 128 to 129, l. 136 to 137; supplement p. 11, Table S1 caption; supplement p. 16, Table S2 title; supplement p. 20, Table S3; p. 26, l. 865 to 866 |
| Quotation | "the REE pattern of each EDC sample was modeled as a linear combination of PSA end-members" |
| Concern | The text separates the two levels clearly in l. 128 to 133 and l. 143 to 146: seven PSAs and 217 dust sources (DS). Elsewhere the 217 samples are called "PSAs" (Table S1 caption "using 217 PSAs", Table S2 title "Table of PSAs database") and "PSA end-members" (l. 137), while "PSA end-members" in Table S3 and in the Figure 2 caption denotes seven regional means. A reader of l. 137 cannot tell whether the model mixes 217 patterns or seven regional end-members. |
| Suggestion | Use "dust source (DS)" for the 217 samples throughout (l. 137 "a linear combination of the 217 DS patterns", Table S2 title "Dust source (DS) database") and reserve "PSA end-member" for the regional means of Table S3. |
| Status | verified |
| Severity | minor |
| Source | S2 |

**GB-09 The stated sample spacing is not met by Table S1, which also contains four duplicated ages and one row that sums to 93.5 %.**

| Field | Content |
|---|---|
| Check | P2, P6 |
| Location | p. 4, l. 109 to 111; supplement p. 11, Table S1, rows 3559 (twice); supplement p. 13, rows 10511 (twice) and 12841 (twice); supplement p. 14, rows 28709 (twice) |
| Quotation | "with an average temporal resolution of approximately 100 years, ranging from 60 to 140 years between adjacent samples" |
| Concern | The mean spacing of the full set, (33699 minus 2852) / 293 = 105 years, agrees with l. 110. The range does not: of the 240 spacings between adjacent retained samples in Table S1, 77 are below 60 years (4 of them 0 years, others 18 or 19 years, for example 9957 to 9976 yr BP) and 60 exceed 140 years (maximum 2280 years); the Holocene median is 43 years. Removing samples can only lengthen spacings, so spacings below 60 years contradict the range stated for the full set. Ages 3559, 10511, 12841 and 28709 yr BP each appear twice with different contributions (see GB-29), and the first row at 10511 yr BP sums to 0.0 + 0.0 + 3.1 + 6.7 + 49.2 + 29.5 + 5.0 + 0.0 = 93.5, while all other rows sum to 99.9 to 100.1. |
| Suggestion | Check the ages of the duplicated rows, restate the spacing in l. 110 to 111 as the actual distribution, and correct or explain the row sum of the first sample at 10511 yr BP. |
| Status | verified (Table S1 values); inferred (spacings and sums computed) |
| Severity | moderate |
| Source | S3, SD |

**GB-10 Sample ages and period boundaries come from two chronologies, and the EDML chronology is not stated.**

| Field | Content |
|---|---|
| Check | P7 |
| Location | p. 4, l. 111; p. 6, l. 184 to 188; p. 12, l. 405 to 409; p. 13, l. 444 to 452; p. 29, Figure 5 |
| Quotation | "The age model follows the EDC3 chronology (Parrenin et al., 2007)." |
| Concern | Samples are dated on EDC3, while the period boundaries are taken from Veres et al. (2013), which defines AICC2012. Table S5 is reproduced exactly from Table S1 with these boundaries applied to EDC3 ages. With 8 ACR and 9 YD samples a shift of a boundary moves samples between periods; the rows at 14601 yr (ACR) and 14716 yr (HS1) lie within 0.1 kyr of the 14.7 kyr boundary. The comparisons with EDML and with events dated elsewhere (MWP-1A, AID6, Bølling; l. 445 to 452) need a common time scale. How large is the EDC3 to AICC2012 offset in this interval? |
| Suggestion | State the chronology of the EDML record in Section 2, transfer the EDC sample ages to AICC2012 (or state the offset), and recompute Table S5 and Figure 4 on one chronology. |
| Status | verified (two chronologies); inferred (boundary sensitivity); assumption (size of the offset, asked as a question) |
| Severity | moderate |
| Source | SD |

**GB-11 The correction factors that convert leached to total REE are not given, and their validity across the glacial to Holocene change in mineralogy is not shown.**

| Field | Content |
|---|---|
| Check | P7 |
| Location | p. 4, l. 118 to 126 (Eq. 1); p. 5, l. 153 to 158; p. 8, l. 251 to 257 |
| Quotation | "Since this method does not fully dissolve all mineral particles, we applied cfi derived from parallel measurements of fully digested EDC samples to obtain total REE concentrations" |
| Concern | The manuscript states that leaching dissolves minerals only partially (l. 121 to 122) and that the dust changed from "less weathered, mafic lithologies" to a "more heterogeneous and weathered source assemblage" (l. 254 to 257). The values of cf_i, their variability used in the Monte Carlo runs (l. 157 to 158), and the number and ages of the fully digested samples are not given. If the factors come from glacial samples and are applied to Holocene samples, part of the glacial to Holocene change in pattern may come from the correction. From which samples and periods are the cf_i derived, and do they differ between glacial and Holocene samples? Graded major because the correction enters every fitted pattern and the shift is the main result. |
| Suggestion | In Section 2 add a table of cf_i with their spread and the number and ages of the digested samples, test whether cf_i differ between periods, and use period-specific factors or show that the result is insensitive to them. |
| Status | verified (missing information); assumption (effect on the shift, asked as a question) |
| Severity | major |
| Source | SD |

**GB-12 The measured REE concentration of an ice-core sample appears under four notations in Eq. 1, Eq. 2 and the text, two of them undefined.**

| Field | Content |
|---|---|
| Check | P38 |
| Location | p. 4, l. 125 (Eq. 1); p. 5, Eq. 2 (between l. 140 and 142); p. 5, l. 147; p. 5, l. 156 to 157 |
| Quotation | "depending on the specific REE - Dusti (Gabrielli et al., 2006). In each MC simulation, cfi and Dusti values were randomly selected" |
| Concern | Eq. 1 defines the correction factor from two bracketed concentrations, Eq. 2 uses the vector DIC with element subscripts La to Lu, l. 147 writes the subscripts in lower case, and l. 156 to 157 introduce "Dust_i" without definition. It is not stated whether Dust_i is the leached, the corrected or the UCC-normalised value, nor in which order correction and normalisation produce the vector of Eq. 2. The range La to Lu in Eq. 2 implies 14 rows, while l. 145 states n = 13. |
| Suggestion | Define one symbol for the measured concentration per element, state in l. 117 to 124 the order of correction and normalisation, replace "Dusti" in l. 156 to 157 by that symbol, and note under Eq. 2 that the Gd row is omitted. |
| Status | verified |
| Severity | minor |
| Source | S2 |

**GB-13 No test shows that the unmixing recovers correct proportions; the problem is underdetermined and the database is dominated by Australian samples.**

| Field | Content |
|---|---|
| Check | P32 |
| Location | p. 4 to 5, l. 126 to 152; p. 3, l. 64 to 71; p. 5, l. 172; p. 8, l. 258 to 260; p. 11, l. 366 to 367; supplement pp. 16 to 19, Table S2 |
| Quotation | "confirming a robust linear agreement between the reconstructed and observed REE signatures" and "our model identifies the Darling sub-basin as the dominant source region during the Holocene" |
| Concern | Each sample is fitted with 13 equations and 217 non-negative coefficients (l. 143 to 145). Many dust sources within and across PSAs have similar patterns, so several mixtures can fit equally well; the manuscript reports fit quality (R) but no test of whether the recovered proportions are right. The introduction rejects isotopes because overlapping fields make sources hard to discern (l. 64 to 65) and credits REE patterns with more discriminative information (l. 70 to 71), but this is not tested for the database used. The database is unbalanced (Table S2): AUS 107 of 217 DS (49.3 %), the Darling sub-basin alone 45 DS (20.7 % of all, 42.1 % of AUS), against 4 ANT and 5 CWA. How sensitive are the PSA contributions to the number of dust sources per PSA? Graded major because every PSA and sub-region result rests on the unmixing. |
| Suggestion | In Section 2 add (1) a leave-one-out test (unmix each DS with the remaining 216 and report the share attributed to its own PSA); (2) synthetic mixtures with known proportions and noise at Holocene concentration levels, reporting recovered against true proportions; (3) a rerun with equal numbers of DS per PSA by repeated subsampling, reporting the change in Table S5; restrict DS-level claims (Darling, Valdes, Namibian rivers) to what these tests support. |
| Status | verified (equation size, DS counts); inferred (imbalance shares computed); assumption (effect on the contributions, asked as a question) |
| Severity | major |
| Source | SD |

**GB-14 The per-region counts of the dust source database do not match Table S2, and Table S2 contains two Australian patterns twice under different basin names.**

| Field | Content |
|---|---|
| Check | P23 |
| Location | p. 4, l. 131 to 133; supplement pp. 17 to 19, Table S2, blocks Australia (AUS) and Antarctica (ANT); rows Darling26 and Darling29 (p. 17), Murray24 and Murray29 (p. 18) |
| Quotation | "Australia (AUS; 106 DS, predominantly from the central and southeastern regions)" |
| Concern | Rows counted in Table S2: PAT 39, CWA 5, PAP 14, SAF 23, AUS 107, NZ 25, ANT 4, total 217. The text gives AUS 106 and ANT 5 (l. 131 to 133); both sums are 217, but two region counts differ by one in opposite directions. Darling26 and Murray29 have identical coordinates (34°3'0.00"S 142°3'10.80"E) and identical values for all 13 REE (La 1.150581 ...), and so do Darling29 and Murray24. Resolution A: the text counts are wrong and Table S2 is the matrix used; then the matrix holds 215 distinct patterns in 217 columns. Resolution B: one ANT pattern is missing from Table S2 and one AUS row is superfluous; then the published table does not reproduce the model input. Identical columns leave the split of a contribution between the two copies undetermined, which matters for the Darling attribution in l. 366, because each duplicated pattern is labelled once Darling and once Murray. |
| Suggestion | Correct the counts in l. 131 to 133 to the matrix used; remove or flag the duplicate rows in Table S2; state how contributions of identical columns were assigned before claiming Darling dominance in l. 366. |
| Status | verified (row counts and identical rows on the page images); inferred (consequence for the sub-basin attribution) |
| Severity | moderate |
| Source | S3 |

**GB-15 The Antarctic end-members in Table S2 do not look UCC-normalised, contrary to the stated rule, and the absence of Antarctic dust is then interpreted climatically.**

| Field | Content |
|---|---|
| Check | P5 |
| Location | p. 4, l. 133 to 135; p. 10, l. 328 to 334; supplement p. 19, Table S2, rows ELB, Expcove, Miers, Vict; supplement p. 11, Table S1, row 3654 |
| Quotation | "all PSA REE patterns were normalized to the UCC composition of Rudnick and Gao (2003) and Gd values were removed" |
| Concern | The four ANT rows range from 0.0083 (Lu) to 2.39 (Ce) and follow the zigzag of crustal REE abundances (for Expcove Ce 2.394624 against Pr 0.265656, ratio 9.0, close to the UCC ratio Ce/Pr 63 / 7.1 = 8.9); the correlation of their log values with log UCC abundances is 0.987 to 0.998, and value divided by UCC is nearly constant (0.012 to 0.054). For all other PSAs median row values lie near 1 (0.76 to 1.18), as expected for normalised patterns. The ANT rows therefore look like concentrations or doubly normalised values. The verification log of instance S2 described Table S2 as UCC-normalised as a whole; the row-level check above decides this point. If the model used these rows, ANT cannot fit a normalised ice pattern, and the near-zero ANT contribution (0.0 to 0.6 % in Table S5; one sample with 33.1 % at 3654 yr BP) is a property of the input rather than of katabatic winds (l. 330 to 334); the contrast with the 24 % of Coppo et al. (2022, l. 326 to 328) would remain unexplained. Which ANT values entered the model? Graded major because the ANT result and its interpretation depend on it. |
| Suggestion | State in Section 2 which ANT values entered the model; correct Table S2; if unnormalised ANT patterns were used, rerun with normalised ones and revise l. 328 to 334. |
| Status | verified (table values on the page image); inferred (non-normalisation, computed); assumption (use in the model, asked as a question) |
| Severity | major |
| Source | SD |

**GB-16 Several steps of the algorithm and the computing settings cannot be rebuilt from text and supplement.**

| Field | Content |
|---|---|
| Check | P8, P35 |
| Location | p. 5, l. 135 to 165 (Eq. 2); p. 5, l. 140; p. 6, l. 196 to 197; p. 11 to 12, l. 385 to 392; supplement p. 17, Table S2, rows EtoshaL1 to EtoshaL4, SuksesL, Sossusvlei |
| Quotation | "This was implemented using the lsqnonneg function in MATLAB." |
| Concern | (1) Eq. 2 minimises the residual with non-negativity only; how the CDS are converted to "% of total deposition" (l. 160) is not stated (normalisation by the sum, or a sum constraint); Table S1 rows sum to 99.9 to 100.1 except one row with 93.5 (GB-09). (2) How DS-level distributions are aggregated to PSA (sum of medians or median of sums) is not stated. (3) Six SAF dust sources are labelled "this study" in Table S2 without sampling, size separation or analytical method. (4) The "three specific REE patterns" near the Valdes Peninsula (l. 196 to 197) are not named. (5) MATLAB version, lsqnonneg tolerance, random number generator and seed, and whether the normal distributions for cf_i and Dust_i were truncated at zero are not given; these settings affect the Monte Carlo output. |
| Suggestion | In Section 2 give normalisation and aggregation as formulas, describe the six new SAF samples (collection, size fraction, digestion, instrument), name the three Valdes dust sources, and state MATLAB version, solver options, seed and distribution settings (or deposit them with the code, GB-59). |
| Status | verified; inferred (row sums computed) |
| Severity | moderate |
| Source | SD |

**GB-17 The EDML values compared in Section 4.4 come from a differently configured model run under the same name, and the manuscript does not say whether they were recomputed.**

| Field | Content |
|---|---|
| Check | P38, P9 |
| Location | p. 5, l. 144 to 145; p. 3, l. 88; p. 3, l. 100; p. 4, l. 106 to 107; p. 12, l. 403 to 404; supplement p. 22, Table S5 (EDML block) |
| Quotation | "In Vanderstraeten et al. (2023), n was equal to 14 but is only 13 in the present study because of the exclusion of Gd." |
| Concern | The manuscript openly states the difference between the two versions, which is good practice, but uses one name ("our 'DEPOT' model", l. 88; "DEPOT algorithm", l. 100) for both. Section 4.4 and Table S5 then place EDC results (13 elements, Gd removed, 217 DS) next to EDML results attributed to the 2023 study; whether database, correction factors and chronology were the same, and whether the EDML values were recomputed with the present variant, is not stated. If not, differences such as the Holocene PAT difference (l. 423 to 424) could partly reflect the configuration rather than the sites. Were the EDML values in Table S5 produced with the 14-element run? |
| Suggestion | Give the present variant a version label (for example "DEPOT v2, 13 REE, 217 DS") in l. 100 and in the Table S1 and S5 captions; state in l. 403 to 404 and in the Table S5 caption whether the EDML contributions were recomputed with this version, or rerun them with it. |
| Status | verified (shared name, stated element difference, missing statement for EDML values); assumption (that the EDML values stem from the 14-element run, asked as a question) |
| Severity | moderate |
| Source | S2, SD |

**GB-18 The Monte Carlo input uncertainty of 2 to 10 % is the replicate precision; the publication of the reused dataset gives a total analytical uncertainty up to 35 % for Holocene MREE and HREE.**

| Field | Content |
|---|---|
| Check | P13 |
| Location | p. 5, l. 153 to 158 |
| Quotation | "Analytical uncertainties associated with REE concentrations in EDC dust range between 2% and 10% (1 relative standard deviation), depending on the specific REE" |
| Concern | Gabrielli et al. (2010, Sect. 2.2), the publication of the dataset used (l. 108), distinguishes the precision on ten replicates, 2 % (La, Ce, Pr, Lu) to 10 % (Er, Tm, Yb), which is the range quoted here, from the relative instrumental standard deviation that "essentially represents the whole analytical uncertainty": 8 % (Holocene) and 3 % (glacial) for LREE, 25 to 35 % (Holocene) and 5 to 8 % (glacial) for MREE and HREE. For Holocene MREE and HREE the total uncertainty is 25 / 10 = 2.5 to 35 / 10 = 3.5 times the largest value used. With these values the Monte Carlo distributions of Holocene contributions would widen, so part of the Holocene variability (l. 25, l. 194, l. 306 to 307) and single-sample extremes such as Altiplano contributions above 90 % (l. 214) could reflect analytical noise. The manuscript discloses that 38 young samples were excluded for concentrations near the detection limit (l. 174 to 179), but does not carry this over to the uncertainty of the retained Holocene samples. Gabrielli et al. (2006) could not be read. Graded major because the Holocene record is research aim (1). |
| Suggestion | In Section 2 (l. 155 to 158) use the element- and period-specific total uncertainties of Gabrielli et al. (2010, Sect. 2.2), report the resulting spread of each Holocene contribution per sample, and state in Section 3 whether the minima at 10, 8.6 and 6.3 kyr BP (l. 194) and the Altiplano maxima (l. 214) exceed it. |
| Status | verified (content of Gabrielli et al., 2010); inferred (content of Gabrielli et al., 2006; effect on the Holocene distributions, not recomputed) |
| Severity | major |
| Source | S1 |

**GB-19 The Monte Carlo propagation is run, but its result, the uncertainty of the contributions, is never reported.**

| Field | Content |
|---|---|
| Check | P31 |
| Location | p. 5, l. 153 to 167; p. 24, Figure 1; p. 27, Figure 3; p. 28, Figure 4; supplement pp. 11 to 15, Table S1; supplement p. 22, Table S5 |
| Quotation | "the use of a larger number of simulations (5000) does not significantly affect the results" |
| Concern | The Monte Carlo runs are introduced "To evaluate the impact of uncertainties" (l. 153), but only medians are shown (Table S1, Figure 1); no interquartile range or interval per sample or per period appears anywhere, so the reader cannot judge whether differences of 3 to 8 points (Section 3, 4.2, 4.4) exceed the uncertainty. The comparison of 2000 and 5000 runs is stated without a measure. Standard errors of period means computed from Table S1 are, for PAT, 5.1 (ACR, n = 8), 9.8 (YD, n = 9) and 2.1 (HS1, n = 27) points, which is the size of the differences interpreted in l. 417 to 422. |
| Suggestion | Add to Table S1 the 16th and 84th percentiles of each PSA per sample, show bands in Figure 1, give period means with uncertainty in Table S5, quantify the 2000 against 5000 comparison, and state the input uncertainty used for low-concentration samples. |
| Status | verified; inferred (standard errors computed) |
| Severity | moderate |
| Source | SD |

**GB-20 The conversion of PSA contributions into absolute dust fluxes is announced and cited as a result, but no PSA flux is reported.**

| Field | Content |
|---|---|
| Check | P11, P12, P31 |
| Location | p. 5, l. 166 to 167; p. 6, l. 183 to 184; p. 24, Figure 1; supplement pp. 3 to 4, Figure S2; supplement p. 11, Table S1 |
| Quotation | "to convert PSA contributions into absolute dust fluxes (Figure S2)" and "Figure 1 and Table S1 summarize the relative contributions (in % of total deposition and flux) from each PSA" |
| Concern | Figure S2 shows only the nssCa2+ flux, δ18O and deuterium excess (page image); Table S1 gives medians in percent; all five y axes of Figure 1 read "Total Contribution (%)". No PSA flux appears anywhere, the conversion from nssCa2+ to total dust (factor, matching of the nssCa2+ series to the sample ages) is not described, and the data statement does not mention the derived fluxes. The discussion uses flux arguments (l. 224 to 225, l. 295 to 296, l. 447 to 450) that PSA fluxes would make testable, for example whether the absolute PAT flux falls before or after 14.5 kyr BP. The nssCa2+ input is openly available (Fischer et al., 2007, PANGAEA, https://doi.org/10.1594/PANGAEA.683641), but only the paper is cited. |
| Suggestion | Add per-sample PSA fluxes with the conversion factor and matching procedure (Section 2, a column set in Table S1 and a flux panel in Figure 1 or S2), or delete the announcement in l. 166 to 167 and "and flux" in l. 184; cite the PANGAEA dataset at l. 167. |
| Status | verified (page images of Figure 1 and Figure S2, Table S1) |
| Severity | moderate |
| Source | S2, S3, SD, AB |

**GB-21 The record is filtered by the quality of its own fit, which removes about a quarter of the samples younger than 14 kyr BP and can bias the Holocene composition.**

| Field | Content |
|---|---|
| Check | P9 |
| Location | p. 5, l. 168 to 172; p. 6, l. 174 to 182; p. 1, l. 19 and l. 24 to 25; supplement p. 22, Table S5 |
| Quotation | "Out of the 279 DIC samples treated by our algorithm, 38 did not meet the R threshold (R≥0.67) and were excluded from the provenance record." |
| Concern | The selection criterion is an outcome of the model: samples whose pattern no database mixture matches are removed, so the retained Holocene record over-represents compositions that the database can express. With 129 retained rows younger than 14 kyr in Table S1 and the 38 excluded samples stated to be younger than 14 kyr (l. 175), 38 / 167 = 22.8 % of that part of the record is removed, against 0 % before 14 kyr. The Holocene averages (PAT 49 %, AUS 23 %; l. 25, l. 317 to 319) and the EDC to EDML differences refer to this selected subset. The manuscript explains the exclusion by low concentrations, but does not show that the excluded samples differ from the retained ones only in concentration. Graded major because the Holocene composition is research aim (1). |
| Suggestion | List the excluded samples with age, concentration and R in the supplement (GB-27), report the Holocene averages also with all 279 samples or weighted by R, and, if concentration is the reason, use a concentration criterion fixed before the fit instead of R. |
| Status | inferred (count and share computed from l. 174 to 175 and Table S1; bias direction from the selection rule) |
| Severity | major |
| Source | SD |

**GB-22 The R threshold does not correspond to p below 0.01 for the stated or the correct degrees of freedom, and Table S1 retains three samples below it.**

| Field | Content |
|---|---|
| Check | P1, P5, P23 |
| Location | p. 5, l. 170 to 172; p. 6, l. 174 and l. 179; supplement p. 11, Table S1, title and rows 2888 and 3267, column R; supplement p. 13, first row 10511, column R |
| Quotation | "We determined that R ≥ 0.67 corresponds to a statistically significant match (p < 0.01, two-tailed test, degrees of freedom = 10)" |
| Concern | (a) The two-tailed critical Pearson r at p = 0.01 is 0.7079 for df = 10, 0.6835 for df = 11 (13 REE, n minus 2) and 0.6614 for df = 12; R = 0.67 corresponds to p = 0.017 (df = 10) or p = 0.012 (df = 11). The value 0.67 matches only df = 12, that is 14 elements, the setup before Gd was removed. Was the threshold carried over from the 14-element setup? (b) With the threshold of the stated test, 19 of the 241 retained samples fall below 0.708, with df = 11 nine fall below 0.684; all are Holocene or YD samples. (c) Table S1 itself retains three rows with R = 0.66 (2888, 3267 and the first row at 10511 yr BP), so the stated rule is broken in its own table; with them excluded, 238 of 279 = 85.3 % remain instead of 86 % (l. 179). Which statistic was compared with the threshold? (d) The modelled pattern is fitted to the same 13 values with up to 217 coefficients, so the null hypothesis of zero correlation is not the relevant one. The balance 294 minus 15 = 279 and 279 minus 38 = 241 closes, and the mean R of Table S1 (0.8523) matches l. 181. |
| Suggestion | In l. 170 to 172 correct the degrees of freedom and the critical value, or justify the threshold otherwise (for example by the R distribution obtained when random database mixtures plus noise are fitted); give R to three decimals in Table S1, state which statistic is compared, and remove or flag the three rows below the threshold and state whether they enter Table S5 and Figure 1. |
| Status | verified (wording, Table S1 values on the page images); inferred (critical values, p values and counts computed); assumption (origin of the threshold, asked as a question) |
| Severity | moderate |
| Source | S3, SD |

**GB-23 Figure S1 shows 19 sampling pins for Patagonia, while the database holds 39 Patagonian dust sources.**

| Field | Content |
|---|---|
| Check | P3 |
| Location | supplement p. 2, Figure S1, panel PAT; p. 4, l. 128 to 129 |
| Quotation | "(PAT; 39 dust sources, DS)" |
| Concern | On the enlarged panel 19 pins are counted; the Antarctic inset shows 5 pins for 5 DS, which agree. Do several Patagonian samples share one site, and are the other panels complete? |
| Suggestion | State in the caption of Figure S1 that one pin can stand for several samples, or give the number per pin; alternatively refer to the coordinates in Table S2. |
| Status | verified (count); assumption (explanation, asked as a question) |
| Severity | minor |
| Source | AB |

**GB-24 The axes of Figure S2 have no units, and panel B lacks the period zones of panels A and C and is offset in time.**

| Field | Content |
|---|---|
| Check | P29 |
| Location | supplement p. 4, Figure S2, panels A, B and C; supplement p. 3, caption |
| Quotation | "(A) Non Sea Salt Calcium (nssCa2+) flux in EDC ice core (Fischer et al., 2007) (B) δ18O in EDC ice core" |
| Concern | The y axes read "nssCa2+ flux", "δ18O" and "deuterium excess" without unit; the main text gives µg m⁻² yr⁻¹ for the flux (l. 166) but no per mil scale for the isotopes. Panel B has no grey period zones, and its tick marks do not line up with A and C: the 0.4 tick lies at 761 px (A), 771.5 px (B) and 752 px (C) at 300 dpi, so a vertical comparison across panels is off by up to 19.5 px, about 300 years. |
| Suggestion | Add units to all three y axes, add the period zones to panel B, and align the three time axes. |
| Status | verified |
| Severity | minor |
| Source | AB |

**GB-25 The Southern African sub-regions carry different names in Table S2, Figure S3 and Section 4.3, and two samples far from Etosha Pan are labelled "Etosha Pan".**

| Field | Content |
|---|---|
| Check | P38 |
| Location | supplement p. 17, Table S2, rows SuksesL and Sossusvlei, column Location; supplement p. 6, Figure S3, panels "Etosha", "Namibia", "Sua"; p. 11, l. 380; p. 12, l. 385 to 386, l. 392, l. 395 to 396 |
| Quotation | "the Makgadikgadi Complex (including Sua Pan), the Etosha Pan, and ephemeral river valleys along the Namibian coast" |
| Concern | The text discusses three systems (Makgadikgadi Complex, Etosha Pan, Namibian coast and riverbeds), Figure S3 plots "Sua", "Etosha" and "Namibia", and Table S2 has no location "Makgadikgadi" (the Botswana samples are "Sua Pan"). The Location column assigns "Etosha Pan" to SuksesL (21.059 S) and Sossusvlei (24.76 S), whereas the other Etosha samples lie between 18.5 and 19.1 S; Sossusvlei is a name in the Namib. If the sub-region series of Figure S3 were built from the Location column, these two samples feed the "Etosha" series on which l. 395 to 398 rest. Which dust sources were aggregated into that series? |
| Suggestion | Add to Table S2 a column "sub-region as used in Figure S3 and Section 4.3", correct the Location entries of SuksesL and Sossusvlei, and use one name per sub-region in l. 380 to 398 and in the Figure S3 axis labels. |
| Status | verified (labels, coordinates, panel names); assumption (aggregation by the Location column, asked as a question) |
| Severity | moderate |
| Source | S2 |

**GB-26 Two rows of Table S2 carry values that are implausible next to their neighbours and enter the fitting matrix.**

| Field | Content |
|---|---|
| Check | P23 |
| Location | supplement p. 17, Table S2, row Kuiseb2inf5, column Dy; supplement p. 17, Table S2, rows Darling11 and Darling12, column Longitude |
| Quotation | "6,200013" and "31° 2'49.20"S 138°17'6.00"E" |
| Concern | Kuiseb2inf5 has a normalised Dy value of 6.200013, while its other twelve values lie between 1.81 and 3.34 (Tb 2.69, Ho 2.15) and the paired sample Kuiseb1inf5 has Dy 2.376; a single positive Dy anomaly of this size is unusual for a normalised dust pattern. Darling12 has longitude 138°17'6.00"E at exactly the latitude of Darling11 (31° 2'49.20"S, 144°17'6.00"E); 138° E at 31° S lies west of the Darling Basin. Both rows were confirmed on the page image. A transcription error in the Dy value would distort the fitted pattern of this end-member in every model run. Are both entries correct? |
| Suggestion | Check both rows against the original sources (Vanderstraeten et al., 2023; Marx and Kamber, 2010), correct Table S2 and, if the Dy value was wrong in the model input, rerun the unmixing. |
| Status | verified (values on the page image); assumption (that they are transcription errors, asked as a question) |
| Severity | minor |
| Source | ZF |

#### Minor corrections

| ID | Location | Quotation | Replacement | Source |
|---|---|---|---|---|
| KK-06 | p. 3, l. 101 | "ice core camples" | "ice core samples" | SD |
| KK-07 | p. 4, l. 127 | "(Figure S1, and Table S1)" | "(Figure S1 and Table S2)" | S2 |
| KK-08 | p. 5, l. 145 to 146 | "because of the exclusion of Gd. For any given time step. The vector of 217 components" | "because of the exclusion of Gd. For any given time step, the vector of 217 components" | SD |
| KK-09 | p. 5, l. 159 | "by minimizing Eq. (1)" | "by minimizing Eq. (2)" | S2, SD |
| KK-10 | supplement p. 16, Table S2, region heading | "Puna AltiPlano (PAP)" | "Puna-Altiplano Plateau (PAP)" | S2 |
| KK-11 | supplement p. 17, Table S2, rows EtoshaL1 to EtoshaL4, SuksesL, Sossusvlei, column Longitude | "15,97 W", "16,487 W", "16,701 W", "16,803 W", "16,836 W", "15,29 W" | "15,97 E", "16,487 E", "16,701 E", "16,803 E", "16,836 E", "15,29 E" | S2 |

#### Verification log

| ID | Check | Checked | Values | Result |
|---|---|---|---|---|
| PP-07 | Design sketch | Research questions, study type, data sources, time axis, environment, principles, components and disclosed limitations over the whole manuscript and supplement (SD) | Modelling on a published dataset; 294, 279, 241 samples; 217 DS; 13 REE; 2000 MC runs; R ≥ 0.67; mean R 0.852 (recomputed 0.8523); disclosed: gap 21.7 to 27.3 kyr (l. 113), low concentrations of excluded samples (l. 175 to 179), ACR and YD tentative (l. 407 to 409), truncated SAF and AUS domains (l. 863), 2000 runs as trade-off (l. 162 to 164) | no finding beyond GB-11, GB-13, GB-21, GB-37 |
| PP-08 | P12 | Every data source named in l. 99 to 172 against the data statement (l. 494 to 496), the appendix line (l. 501) and the supplement (S2) | UCC composition published; Table S2 with 217 rows, 13 value columns, reference per row, six rows "this study"; nssCa2+ flux open at PANGAEA; ages per sample in Table S1 (2852 to 33699 yr BP); Tables S3, S4, S5 present | no finding beyond GB-20, GB-59 |
| PP-09 | P38 | Identifiers across text, captions and supplement (S2) | EDC, DIC, UCC, cf_i, CDS, MC, R and 0.67, 13 elements after Gd removal, PSA abbreviations identical in text, Tables S1 and S5, Figures 1, 3, 4; SSA = PAT + CWA + PAP identical in l. 128 to 130, l. 280, l. 321; period names and bounds identical between l. 185 to 188 and Table S5 | no finding beyond GB-01, GB-08, GB-12, GB-17 |
| PP-10 | P2, P22 | Sampling statements of Section 2 used by the results (S3) | Mean spacing (33699 minus 2852) / 293 = 105.3 years against "approximately 100 years" (l. 110); samples between 21.7 and 27.3 kyr BP in Table S1: 22150, 23104, 25384, 25640, that is four, as in l. 113 | no finding beyond GB-09 |
| PP-11 | P3 | Pins of Figure S1 against the database numbers of l. 128 to 133 (AB) | ANT 5 pins for 5 DS; other panels not counted where pins overlap | no finding beyond GB-23 |
| PP-12 | P26 | Non-negativity "ensuring that all contributions are physically meaningful" (l. 138 to 139) across all paths (SD) | Minimum of all 241 × 8 entries in Table S1 is 0.0; lsqnonneg used for every fit (l. 140, l. 159) | no finding |
| PP-13 | P33 | Statements about effort or cost (SD) | Only "computation cost" as reason for 2000 MC runs (l. 162 to 163); not used as a result or limitation | no finding beyond GB-19 |
| PP-14 | P25 | Whether each step had the information it uses (SD) | REE data (Gabrielli et al., 2010), cf_i from digested samples, Table S2 patterns, nssCa2+ flux, Table S3 end-members, EDML results: all published or tabulated before the analysis | no finding beyond GB-20 |
| PP-15 | P27 | Downstream use of untested components (SD) | cf_i to every fit (GB-11); R threshold to selection of 241 of 279 (GB-21, GB-22); ANT end-members to ANT share (GB-15); unmixing accuracy to all PSA and DS statements (GB-13) | no finding beyond these |
| PP-16 | P30 | Reported errors, corrections, reruns (SD) | The manuscript reports no error or correction | no finding |
| PP-17 | P12 | Reachability of links in the data statement and the appendix line (S2) | l. 494 to 496 and l. 501 contain no link, DOI or repository; the supplement was supplied as a file | no finding beyond GB-59 |

### Segment 3: Results, Figure 1, Tables S1 and S5 (pp. 6 to 7, 24 to 25)

#### Substantive findings

**GB-27 The excluded samples and the number of samples per period are not reported.**

| Field | Content |
|---|---|
| Check | P22, P34 |
| Location | p. 6, l. 174 to 176; p. 4, l. 114 to 115; p. 6, l. 182 to 188; supplement p. 22, Table S5 |
| Quotation | "These excluded samples are all younger than 14 kyr BP and have very low REE concentrations near the detection limit." |
| Concern | The 15 samples with missing data and the 38 samples below the R threshold are listed nowhere, so the statement that all excluded samples are younger than 14 kyr BP cannot be checked, nor how they distribute over the Holocene periods. The number of samples per period, needed to read every period average, must be counted from Table S1: Late Holocene 60, Early Holocene 56 (Holocene 116), YD 9, ACR 8, HS1 27, LGM 40, MIS3 41, sum 241. Only ACR and YD are mentioned, the YD count incorrectly (GB-42). |
| Suggestion | Add a column n to Table S5 and list the 53 excluded samples with age, concentration and reason in the supplement. |
| Status | verified (absence; Table S1); inferred (counts) |
| Severity | moderate |
| Source | S3, SD |

**GB-28 Period averages are unweighted means of per-sample percentages but are described as shares of total deposition.**

| Field | Content |
|---|---|
| Check | P20 |
| Location | p. 6, l. 189 to 190; p. 7, l. 216; p. 9, l. 293 to 294; supplement p. 22, Table S5, title |
| Quotation | "It contributes for 65-70% (average contributions) of the total dust deposition during the end of MIS 3 and the LGM" |
| Concern | Table S5 is reproduced exactly as the arithmetic mean of the per-sample medians of Table S1 (PP-19); the unit is the sample, each weighted equally. A share of total deposition would weight each sample by the dust flux and the time it represents. Sample spacing in Table S1 varies from 0 to 2280 years, so equal weighting already changes the values: time-weighted Holocene means are PAT 51.8 instead of 49.0, AUS 21.4 instead of 23.1, NZ 4.8 instead of 5.9. Within HS1 the nssCa2+ flux falls from about 600 to below 50 (Figure S2A), so equal weights over-represent the low-flux end. Flux weighting cannot be checked because PSA fluxes are not reported (GB-20). |
| Suggestion | Rename the quantity in l. 189 to 190, l. 216, l. 294 and in the title of Table S5 as "mean relative contribution per sample", or add flux-weighted period shares from the conversion announced in l. 166 to 167. |
| Status | verified (reproduction of Table S5, wording); inferred (time-weighted means) |
| Severity | moderate |
| Source | S3 |

**GB-29 The Holocene variability interpreted as climate signal may reflect sampling of 2 to 3 year windows and analytical noise; the duplicated ages in Table S1 show scatter of this size.**

| Field | Content |
|---|---|
| Check | P9 |
| Location | p. 6, l. 194; p. 4, l. 112; p. 6, l. 175 to 179; p. 9 to 11, l. 306 to 352, l. 372 to 378; p. 29, Figure 5; supplement p. 11, Table S1, rows 3559; supplement p. 13, rows 10511 and 12841; supplement p. 14, rows 28709 |
| Quotation | "Three distinct minima in PAT contributions occur at 10, 8.6, and 6.3 kyr BP." and "Overall, our Holocene provenance record for PAT contributions is matching well with the SWW intensity proxies in Potrok Aike bog" |
| Concern | Holocene samples integrate 2 to 3 years (l. 112), have very low concentrations (l. 175 to 176), and SAF sources emit in a "low-frequency, high-magnitude" way (l. 399). A 2 to 3 year sample every ~100 years can catch or miss single dust events, so sample-to-sample scatter is expected from sampling alone. At the duplicated age 3559 yr BP the two rows give PAT 86.7 % and 0.0 % (half the sum of absolute differences across PSAs: 87.2 points); at 10511 yr 52.9 points, at 12841 yr 39.4 points, at 28709 yr (LGM) 10.2 points. Neighbour-to-neighbour change in PAT has a Holocene median of 26.4 points (31 of 115 steps above 50 points) against 8.4 points for samples older than 14.7 kyr (0 of 107 above 50). Mean R falls from 0.916 to 0.799. 23 Holocene samples have PAT = 0 and 13 have one PSA at or above 90 %, against none with PAT = 0 before 14.7 kyr. None of this separates source change from sampling and noise, yet single minima and peaks are tied to fires, westerlies and lake phases (l. 335 to 352, l. 370 to 378, l. 392 to 398). What are the duplicated ages: replicates, adjacent depths or typing errors? Graded major because the Holocene interpretation is research aims (1) and (3). |
| Suggestion | State in Section 2 what the duplicated ages are; report the Monte Carlo spread per sample and the difference between duplicate rows; test whether the Holocene sample-to-sample variance exceeds the variance expected from analytical uncertainty (GB-18) plus event sampling; base the comparisons in Section 4.3 and Figure 5 on multi-centennial bins with uncertainty and a stated correlation statistic. |
| Status | verified (duplicate rows and values); inferred (variability figures computed); assumption (interpretation of the pairs, asked as a question) |
| Severity | major |
| Source | SD |

**GB-30 Results at sub-region and dust source level are stated without being reported anywhere.**

| Field | Content |
|---|---|
| Check | P11, P34 |
| Location | p. 6, l. 196 to 197; p. 5, l. 161 to 162; p. 11, l. 366; p. 12, l. 385 to 397 |
| Quotation | "our algorithm highlights three specific REE patterns collected in or near the Valdes Peninsula" and "the Namibian coast and ephemeral riverbeds were detected most frequently" |
| Concern | The methods announce aggregation "by PSA or specific sub-regions within PSA" (l. 161 to 162). Reported are PSA medians (Table S1, PAP split into Puna and Altiplano) and the PAP and SAF sub-regions as curves (Figure S3). There is no table or figure for Australian sub-basins (Darling, Murray and others), for the dust source level within PAT, or for detection frequencies within SAF, so the Valdes, Darling (l. 366) and Namibian river results cannot be checked; for Darling see also the duplicated patterns in GB-14. |
| Suggestion | Add a supplementary table with median contributions per sub-region for all PSAs and the number of samples in which each sub-region or dust source has CDS above zero, and cite it in l. 196, l. 366 and l. 386. |
| Status | verified |
| Severity | moderate |
| Source | S3, SD |

**GB-31 The stated overall ranking of the secondary sources does not follow from Table S1.**

| Field | Content |
|---|---|
| Check | P2 |
| Location | p. 6, l. 201 to 202; supplement pp. 11 to 15, Table S1 |
| Quotation | "Overall, other Southern Hemisphere PSAs contribute to EDC dust deposition with sources from: AUS, SAF, PAP and NZ, in decreasing order of importance." |
| Concern | Means over all 241 samples of Table S1: AUS 16.5, SAF 9.2, NZ 7.9, PAP 6.8 (Puna 3.1 + Altiplano 3.8); NZ ranks third and PAP fourth. For the Holocene the order is AUS 23.1, PAP 11.0, SAF 10.7, NZ 5.9; for the LGM the manuscript itself gives NZ, AUS, SAF, PAP (l. 223). |
| Suggestion | State the period to which the ranking applies, or correct it to "AUS, SAF, NZ and PAP". |
| Status | verified (Table S1); inferred (means) |
| Severity | minor |
| Source | S3 |

**GB-32 The "sharp increase" of Southern African dust in the YD rests on a single sample.**

| Field | Content |
|---|---|
| Check | P21 |
| Location | p. 6, l. 207; p. 13, l. 421 to 422; supplement p. 13, Table S1, row 12227, column SAF; supplement p. 22, Table S5, row YD, column SAF |
| Quotation | "followed by a sharp increase during the YD with 15%" |
| Concern | The nine YD values of SAF in Table S1 are 0.0, 1.3, 94.7, 8.8, 5.5, 5.0, 6.2, 2.4 and 7.8; their mean is 14.6 (Table S5), their median 5.5. The sample at 12227 yr BP alone contributes 94.7 of the sum 131.7, that is 71.9 %; without it the YD mean is 4.6, below the ACR mean of 8.0. The same sample drives the YD difference SAF EDC minus EDML of +6.4 (GB-53). |
| Suggestion | Report median and range next to the mean in Table S5 and qualify l. 207: the YD increase reflects one sample at 12.2 kyr BP. |
| Status | verified (Table S1 values); inferred (mean, median, share) |
| Severity | moderate |
| Source | S3 |

**GB-33 SAF contributions of about 2 % are stated for 9.5 to 12 kyr BP, but neither Table S1 nor Figure 1 shows this value for the window.**

| Field | Content |
|---|---|
| Check | P3, P24 |
| Location | p. 6 to 7, l. 207 to 208; p. 24, Figure 1, panel SAF; supplement pp. 13 to 14, Table S1, column SAF |
| Quotation | "Although SAF input drops to minimal levels (~2%) between 9.5 and 12 kyr BP" |
| Concern | Instance AB measured the smoothed SAF curve of Figure 1 between 9.5 and 12 kyr BP at 1.0 to 12.7 % (mean 6.0 %), with values near 2 % only from 10.6 to 11.3 kyr and around 9.8 kyr, and 12.2 to 12.6 % from 11.6 to 12.0 kyr. Instance S3 recorded the statement as consistent with Table S1 because the median of the 33 samples in the window is 0.3 %. Rechecked for this report on Table S1: n = 33, median 0.3 %, mean 4.3 %, raised by 40.3 % at 10278 and 49.2 % at 10511 yr BP. Decision: "minimal levels" holds for the typical sample, but the value ~2 % matches neither the median (0.3) nor the mean (4.3) nor the smoothed curve that the sentence refers to, and the window ends inside the YD, the period with the highest SAF mean (14.6 %). |
| Suggestion | Give in l. 208 the statistic meant (for example "median below 1 %, with two samples above 40 % at 10.3 and 10.5 kyr BP") or narrow the window to about 10.6 to 11.3 kyr BP. |
| Status | verified (Figure 1 measured, Table S1 values); inferred (median and mean computed) |
| Severity | moderate |
| Source | AB, S3 |

**GB-34 The statements on Southern Altiplano contributions above 90 %, South Puna below 20 % and an Altiplano onset after 11.2 kyr BP do not match Table S1 and Figure S3.**

| Field | Content |
|---|---|
| Check | P2, P3, P6, P24 |
| Location | p. 7, l. 212 to 215; p. 11, l. 355 to 360; p. 24, Figure 1, panel PAP; supplement p. 6, Figure S3, panels Altiplano and Puna; supplement pp. 11 to 13, Table S1, columns Puna and Altiplano |
| Quotation | "contributing over 90% at 11.2, 10, 8.6, 6, and 3.5 kyr BP. In contrast, contributions of South Puna remained consistently below 20% during this interval (Figure 1)." and "the Southern Altiplano begins contributing dust only after approximately 11.2 kyr BP" |
| Concern | The five dates match raw PAP peaks in Figure 1 (measured at 11230, 9947, 8639, 5927 and 3453 yr BP). But Table S1 shows Altiplano values of 90 % or more in two samples only, 11228 yr BP (97.0) and 8629 yr BP (100.0); near the other dates the highest values are 75.7 (9957), 58.5 (5967), 58.0 (6166) and 62.7 (3465), and the Figure 1 PAP peaks there reach only 60.0, 55.9 and 55.6 %, so three of the five values above 90 % are impossible if Figure 1 is correct, because the Altiplano is part of PAP. South Puna (column "Puna"; North Puna does not contribute, l. 356) is at or above 20 % in eight Holocene samples: 3503 (25.0), 4387 (20.6), 5657 (23.4), 5850 (29.1), 6775 (20.7), 7833 (25.6), 10205 (25.7), 11117 (20.2). Figure 1 cited in l. 215 does not separate South Puna. The Altiplano contributes 16.6 and 12.8 % at 12841 yr BP (Table S1) and 38.8 % at 11.86 kyr BP in Figure S3, before 11.2 kyr BP, which weakens the link to the final desiccation of paleolake Coipasa (l. 358 to 360). Graded major because the emergence and timing of Altiplano dust is a result used for the Holocene interpretation. |
| Suggestion | Bring l. 213 to 215 and l. 357 to 359 into line with Table S1 (two samples above 90 %; South Puna up to 29 %; Altiplano present at 12.8 kyr BP), or state the quantity from which the values are taken; cite Figure S3 instead of Figure 1 in l. 215; revise the Coipasa link in l. 358 to 360 if the onset moves. |
| Status | verified (Table S1 values; Figure 1 and Figure S3 measured on the page images); inferred (impossibility argument from the nesting of Altiplano in PAP) |
| Severity | major |
| Source | AB, S3, SD |

**GB-35 Figure 1 (PAP total) and Figure S3 (PAP sub-regions) do not add up at the two highest PAP samples.**

| Field | Content |
|---|---|
| Check | P3 |
| Location | p. 24, Figure 1, panel PAP; supplement p. 6, Figure S3, panels Altiplano and Puna; supplement p. 5, Figure S3 caption |
| Quotation | "Evolution of contribution to EDC from subregions of the Puna-Altiplano and Southern Africa PSA between 2.852 to 33.699 kyr BP (% of total dust deposition for each PSA)" |
| Concern | With North Puna not contributing (l. 356), PAP should equal South Puna plus Altiplano. At 8.64 kyr BP Figure 1 shows PAP at 97.9 % (Table S1: Altiplano 100.0), while Figure S3 shows at most 5.7 % Altiplano and 2.4 % Puna within ±130 yr; at 11.23 kyr BP Figure 1 shows 95.8 % (Table S1: 97.0), Figure S3 at most 14.6 % plus 42.9 %. Figure S3 thus disagrees with both Figure 1 and Table S1. Two readings: (a) medians of sub-regions need not add to the median of their sum, for example when the solver alternates between sub-regions with similar patterns; (b) Figure S3 was produced from a different data set or normalisation; the caption phrase "% of total dust deposition for each PSA" can be read as percent of total dust or as percent within the PSA. Which applies? |
| Suggestion | State in the captions of Figure 1 and Figure S3 whether the curves are medians and of which quantity; under (a) add the per-run sum or an interquartile range; under (b) correct the figure that is wrong. |
| Status | verified (mismatch measured and in Table S1); assumption (cause, asked as a question) |
| Severity | moderate |
| Source | AB |

**GB-36 Abbreviations in the figure captions are not resolved, and the region names in Figure 2 differ from the text.**

| Field | Content |
|---|---|
| Check | P29 |
| Location | p. 25, l. 851 to 854 (Figure 1 caption); p. 26, Figure 2, region labels and legend; p. 27, l. 869 to 873; p. 28, l. 875 to 876; p. 29, l. 880 to 882; supplement captions of Figures S3 and S4 |
| Quotation | "Evolution of dust PSA contributions to EDC ice core between 2852 to 33699 yr BP" |
| Concern | PSA, PAT, AUS, SAF, NZ, PAP, YD, ACR, HS1, LGM and MIS3 appear in the figures but are defined only in the text (Figure 3 defines LGM only). Figure 2 labels a domain "Southern Central Western Argentina", while the text uses "Central Western Argentina (CWA)" (l. 129) and Table S3 "SCWA"; the legend has no entry for MIS3 although l. 252 assigns "the end of MIS3/LGM" to the blue symbols, and the caption does not say that "Iso" denotes measured ice-core values. |
| Suggestion | Add the abbreviations to each caption (or one key under Figure 1 that later captions refer to), use one name for CWA, write "EDC MIS3/LGM" in the legend, and explain "Iso" in the Figure 2 caption. |
| Status | verified |
| Severity | minor |
| Source | AB |

#### Minor corrections

| ID | Location | Quotation | Replacement | Source |
|---|---|---|---|---|
| KK-12 | p. 6, l. 189 | "It contributes for 65-70%" | "It contributes 65-70%" | S3 |
| KK-13 | p. 6, l. 191 | "during HSI is marked" | "during HS1 is marked" | S2, S3 |
| KK-14 | p. 6, l. 193 | "(averages contributions)" | "(average contributions)" | S3 |
| KK-15 | p. 6, l. 195 | "contributing to 47-51% of the total mix" | "contributing 47-51% of the total mix" | S3 |
| KK-16 | p. 6, l. 197 to 198 | "therefore reflects regional mixed input" | "therefore reflect regional mixed input" | S3 |
| KK-17 | p. 6, l. 199 | "LREE (low rare earth elements)" | "LREE (light rare earth elements)" | S3 |
| KK-18 | p. 7, l. 213; p. 9, l. 290 | "the emergence of South Altiplano dust"; "in the South Altiplano linked to" | "the emergence of Southern Altiplano dust"; "in the Southern Altiplano linked to" (as in l. 130, l. 358, l. 362) | S2 |
| KK-19 | p. 25, l. 851 (Figure 1 caption) | "between 2852 to 33699 yr BP" | "between 2852 and 33699 yr BP" | AB |
| KK-20 | p. 25, l. 852 (Figure 1 caption); p. 29, l. 882 (Figure 5 caption); supplement p. 9 (Figure S5 caption) | "mobile average over 9 steps" | "moving average over 9 samples" | AB |
| KK-21 | p. 25, l. 852 to 853 (Figure 1 caption) | "Central-Western-Argentina and Antarctica are not shown" | "Central Western Argentina (CWA) and Antarctica (ANT) are not shown" | S2 |
| KK-22 | p. 25, l. 853 (Figure 1 caption) | "as their dust emissions contribution are very low" | "as their contributions are very low" | AB |
| KK-23 | supplement p. 11, Table S1 title | "based on th DEPOT model results - using 217 PSAs and 279 DIC from EDC ice core REE patterns." | "based on the DEPOT model results, using 217 dust sources (DS) and the 241 retained DIC samples from EDC ice core REE patterns." | S3, SD |

#### Verification log

| ID | Check | Checked | Values | Result |
|---|---|---|---|---|
| PP-18 | P1, P23 | Sample balance and fit quality, l. 108 to 181 (S3) | 294 minus 15 = 279 (l. 108, l. 114); 279 minus 38 = 241 (l. 174, l. 179); Table S1 has 241 rows; 241 / 279 = 86.4 %, printed 86 %; mean R of Table S1 0.8523, printed 0.852 | no finding beyond GB-22 |
| PP-19 | P2, P1, P7 | Table S5 (EDC) against means of Table S1 per period with the bounds of l. 185 to 188, PAP = Puna + Altiplano; one configuration for all EDC samples (S3, S4, SD) | All 56 EDC cells reproduced within 0.05; n = 60, 56, 116, 9, 8, 27, 40, 41; for example LGM PAT 65.7, NZ 14.2; Holocene PAT 49.0, AUS 23.1; row sums 99.9 to 100.1; 13 REE and Gd removal for all EDC samples, no protocol change | no finding beyond GB-28 |
| PP-20 | P2 | Values in the Results text, l. 189 to 218, and l. 315 to 319, l. 327, against Table S5 (S3) | PAT 65 to 70 % MIS3 and LGM (70.3, 65.7), 75 % HS1 (74.8), 69 % ACR, 63 % YD, 49 % Holocene; AUS 9, 10, 11 % (9.1, 10.2, 11.3), 23 % Holocene; NZ 14 % LGM, 7 % HS1, 6.5 % ACR, 3 % YD, 6 % Holocene; PAP below 4 % before ACR, 11 % Holocene; all within rounding | no finding beyond GB-31, GB-32, GB-33 |
| PP-21 | P1 | Further derived values against Tables S1 and S5 (S3) | SSA LGM 65.7 + 0 + 3.6 = 69.3, text about 70 % (l. 281); PAP LGM 3.6, text about 4 % (l. 289); PAT younger than 5 kyr: mean of 25 samples 52.0, text 50 to 55 % (l. 352); PAT minima at 10, 8.6, 6.3 kyr BP (l. 194): Table S1 PAT 0.0 at 9957, 10029, 10222 and 8629, 6.5 at 6306 | no finding beyond GB-33 |
| PP-22 | P20 | Quotes and their denominators (S3) | 86 % refers to 279 treated samples (stated); Table S5 refers to per-sample medians with equal weight; "three specific REE patterns" among the 39 PAT DS, consistent with Table S2 | no finding beyond GB-28 |
| PP-23 | P11 | Matrix of periods against announced outputs (S3) | Table S5 EDC covers all 8 periods, EDML Early Holocene, YD, ACR, HS1, LGM, matching the overlap 7.5 to 27 kyr (l. 407); box plots: Holocene and LGM in Figure 3, five periods in Figure S4; isotopes per sample in Figure 2; CWA and ANT omitted from Figure 1 as disclosed (Table S5: CWA 0.0, ANT at most 0.6) | no finding beyond GB-19, GB-20, GB-30 |
| PP-24 | P29, P3 | Inventory of all figures, captions and text references (AB) | Five main figures (pp. 24, 26 to 29), five supplementary figures; every figure cited at least once; no graphical abstract, placeholder or watermark; first citations 1 (l. 183), 2 (l. 244), 3 (l. 281), 5 (l. 340), 4 (l. 405) | no finding beyond GB-46 |
| PP-25 | P24 | Grey period zones of Figure 1 against l. 185 to 188 (AB) | Panel PAT: YD 11690 to 12900, HS1 14710 to 18010, MIS3 from 28990 yr BP; panel PAP within 0.01 kyr of these; text 11.7 to 12.9, 14.7 to 18, older than 29 kyr; agreement within 0.02 kyr | no finding |
| PP-26 | P24 | Dated features of Figure 1 (PAT, AUS) against l. 194, l. 205, l. 336 to 338 (AB) | PAT minima at 10132 (23.3 %), 8539 (31.1 %), 6329 yr BP (28.8 %) against 10, 8.6, 6.3 kyr; PAT maxima 9.2 to 9.7 and 7.66 kyr against "~9 kyrs BP, between 7-8 kyr BP"; AUS high 9.8 to 10.7 kyr against 9.5 to 10 kyr, within the shift of a 9-step average | no finding |
| PP-27 | P37 | Labelling of smoothed or changed data in figures (SD) | Figure 1 shows medians as thin lines and a 9-step moving average as bold lines, both stated in the caption (l. 852 to 853); Figure S2 shows cited source data; plotted range 2852 to 33699 equals the retained record | no finding |

### Segment 4: Discussion, conclusion, declarations, references, Figures 2 to 5, supplement Figures S3 to S5 and Tables S3, S4 (pp. 7 to 29)

#### Substantive findings

**GB-37 The EDC record does not resolve the shift at about 14.5 kyr BP: per-sample PAT stays at HS1 level until about 13.4 kyr BP, and the ACR means lie within the glacial range.**

| Field | Content |
|---|---|
| Check | P10, P15, P2 |
| Location | p. 7, l. 233 to 236; p. 1, l. 23; p. 6, l. 203 to 204; p. 10, l. 335; p. 13, l. 444 to 447; p. 14, l. 477 to 480 and l. 486; supplement p. 13, Table S1, rows 13032 to 15153 yr BP; supplement p. 10, Figure S5, panel PAT; supplement p. 22, Table S5 |
| Quotation | "Our calculations highlight a major shift in dust provenance occurred at the onset of the ACR" and "From ~14.5 kyr BP onward, a marked reorganization in dust provenance occurred" and "while millennial-scale changes were broadly synchronous" |
| Concern | The glacial to Holocene contrast is clear in the record; the timing is not. Per-sample PAT in Table S1 between 13.4 and 14.7 kyr BP is 81.7, 79.9, 67.8, 80.3, 78.6 and 67.6 % (HS1 mean 74.8 %); the first low values are 53.7 % (13143 yr) and 41.9 % (13032 yr), so the ACR mean of 68.9 % is driven by its two youngest samples. AUS is 11.3 % in HS1 and 11.1 % in the ACR (Table S5), contrary to "rose after 14.7 kyr BP" (l. 203 to 204) and "significantly increased contributions from low-latitude sources, including AUS" (l. 235); the low-latitude sum does rise (18.2 to 24.3 %), driven by SAF and PAP. ACR means lie inside the glacial range for every PSA except PAP; Mann-Whitney tests on Table S1 give PAT ACR against HS1 p = 0.753, against LGM p = 0.263, PAT + NZ ACR against HS1 p = 0.143; only the Holocene differs from the LGM (PAT p = 0.018). Contradiction between instances: S4 read the EDC PAT curve of Figure S5 as flat between 15 and 14 kyr, AB as falling. Rechecked on the page image: the smoothed EDC curve stays near 73 to 76 % from 15 to about 14.4 kyr and falls to about 62 % by 14.0 kyr, while the EDML curve drops to about 35 to 40 %. Decision: the smoothed EDC decline appears near 14 kyr, but with a 9-sample window spanning roughly 1 kyr at ACR sample density it can be carried by the 13.0 and 13.1 kyr samples; the per-sample values do not show a decline before 13.4 kyr BP. If this holds, the EDC shift lags the EDML shift and MWP-1A (l. 452) by roughly 1 kyr, which bears on "synchronous" (l. 486) and on research aims (3) and (4). The tentative status of ACR and YD (l. 407 to 409) is not carried into these statements. |
| Suggestion | In Sections 3, 4.1, 4.4 and 5 either restrict the EDC claim to the glacial to Holocene contrast, or date the change by a change-point analysis on the per-sample medians with the Monte Carlo spread, reporting date and uncertainty on a stated chronology (GB-10), and state whether it is distinguishable from the EDML timing; qualify "synchronous" and "From ~14.5 kyr BP onward"; correct l. 203 to 204 (AUS stays at about 11 % through the ACR) and name SAF and PAP in l. 235. |
| Status | verified (Table S1 values; Figure S5 on the page image); inferred (interval means and tests computed) |
| Severity | major |
| Source | S4, SD, S3 |

**GB-38 Section 4.1 describes one isotope calculation per time interval, while Figure 2 plots one calculated point per sample.**

| Field | Content |
|---|---|
| Check | P3 |
| Location | p. 8, l. 244 to 247 and l. 251 to 253; p. 26, Figure 2 |
| Quotation | "For each time interval of the LGIT, the relative contribution of each PSA (CONTR) was multiplied by its average Sr and Nd concentrations" |
| Concern | Read literally, the text yields six calculated points. Figure 2 shows dozens of filled symbols per colour (26 separate light red, 26 dark red and 27 blue dots counted at 300 dpi, besides merged clusters), and recomputation per sample reproduces the spread and the single YD point at 0.7275 and εNd minus 17.9 (PP-29). The figure therefore uses per-sample contributions; because points overlap, the number per period cannot be counted, so a reader cannot check whether all 241 samples are plotted. |
| Suggestion | In l. 244 write "For each sample" (or state both if period means are also plotted) and give in the caption of Figure 2 the number of calculated points per period. |
| Status | verified (dot counts on the page image) |
| Severity | moderate |
| Source | AB, SD |

**GB-39 The isotopic validation claims agreement with values "measured in EDC" for glacial and interglacial intervals, but the interglacial measurements in Table S4 and Figure 2 come from Taylor Glacier and Berkner Island, and no measure of agreement is given.**

| Field | Content |
|---|---|
| Check | P31, P15, P2, P3 |
| Location | p. 8, l. 254 to 260; p. 3, l. 93 to 94; p. 7, l. 238 to 240; p. 8, l. 251 to 253; p. 26, Figure 2 and caption l. 857 to 858; supplement p. 21, Table S4; supplement p. 20, Table S3 |
| Quotation | "Overall, the close agreement between our modeled isotopic compositions and those measured in EDC for both glacial and interglacial intervals supports the robustness of our DEPOT algorithm" |
| Concern | The forward calculation is a sound independent check. Table S4 (page image) lists 35 measured values: Iso LGM 6 (2 EDC, Delmonte et al. 2004a; 4 Taylor Glacier), Iso HS1 3 (1 Old Dome C, 2 Taylor Glacier), Iso ACR 2 and Iso YD 2 (Taylor Glacier), Iso Holocene 22 (8 Taylor Glacier, 14 Berkner Island); none of the Holocene values is from EDC. Berkner Island lies in the Atlantic sector, where the manuscript expects more Patagonian dust than at EDC (l. 425 to 427); its values average εNd minus 11.50 (minus 7.33 to minus 14.71), far from the modelled Holocene minus 4.99. The EDC Holocene values the text quotes (l. 239 to 240: 87Sr/86Sr ~0.710, εNd minus 4.51 to minus 5.68) are in neither Table S4 nor Figure 2; recomputed from Tables S1, S3 and S5 the modelled Holocene mixture (0.7101, minus 4.99) lies inside them and the LGM mixture (0.7083, minus 2.62) is close to the measured EDC LGM values (0.7086 to 0.7088, minus 1.66 to minus 2.46). Adding these values would support the claim directly. For ACR the measured Taylor Glacier values (0.7110, 0.7112) differ from the modelled 0.7082. The legend distinguishes "Iso Early Holocene" and "Iso Holocene", while Table S4 has one group. The recomputed YD mean (εNd minus 5.39) is more negative than the Holocene mean, while l. 251 to 253 group the YD with the glacial cluster. Graded major because this validation is research aim (2). |
| Suggestion | In l. 254 to 260 name for each period the core the measured values come from; add the EDC Holocene values of l. 239 to 240 to Table S4 and Figure 2 and mark sites by symbol; restrict "measured in EDC" to the periods with EDC data; report per period the difference between modelled and measured EDC values with the Monte Carlo spread; align the legend with Table S4. |
| Status | verified (Table S4 and Figure 2 on the page images); inferred (recomputed mixtures and Berkner mean) |
| Severity | major |
| Source | S3, S4, AB, SD |

**GB-40 The timing of the Patagonian Ice Sheet maximum differs from the cited synthesis.**

| Field | Content |
|---|---|
| Check | P13 |
| Location | p. 8, l. 267 to 269 |
| Quotation | "the Patagonian Ice Sheet reached its maximum spatial extent between ~34 and 29.4 kyr BP, covering much of the Andes with an ice mass 2090 km long and 350 km wide (Davies et al., 2020)." |
| Concern | The dimensions are reproduced correctly. The abstract of Davies et al. (2020, Earth-Sci. Rev. 204, 103152) dates the maximum extent to 33 to 28 ka between 38 and 48° S and "earlier, around 47 ka from 48°S southwards"; the dimensions refer to 35 ka. The range 34 to 29.4 kyr BP is not in the abstract, and the earlier maximum south of 48° S is omitted. The full text was not read. |
| Suggestion | In l. 267 to 269 write "reached its maximum extent by 33 to 28 ka between 38 and 48° S and around 47 ka south of 48° S; at 35 ka it was 2090 km long and 350 km wide (Davies et al., 2020)", or give the page for 34 and 29.4 kyr BP. |
| Status | verified (abstract); inferred (whether the full text gives 29.4 kyr BP) |
| Severity | minor |
| Source | S1 |

**GB-41 The model studies cited in support of Patagonian dominance report the opposite, and one of them contains no model apportionment.**

| Field | Content |
|---|---|
| Check | P13 |
| Location | p. 8, l. 275 to p. 9, l. 277 |
| Quotation | "Model simulations also support this view, estimating that SSA and AUS sources together supplied 70-90% (here, PAT+AUS is ~77%) of the dust reaching EA during the LGM (i.e., Albani et al., 2012; Krätschmer et al., 2022)." |
| Concern | Krätschmer et al. (2022, Clim. Past 18, 67 to 87) state that "over 90 % of the mineral dust deposited over Antarctica are of Australian or South American origin during both PI and LGM"; in their LGM simulation Australian dust dominates, and "Only in a smaller region of East Antarctica does dust of South American origin contribute up to 40 %". Their Sect. 3.2.3 calls this "inconsistent with observational data from Antarctic ice cores" and a "shortcoming on the modeling side". The study therefore does not support the significance of Patagonian sources (l. 273 to 275), and the range 70 to 90 % is not in it. Albani et al. (2012, Clim. Past 8, 741 to 750) is an observational TALDICE study without a percentage apportionment by a transport model. Is a different Albani et al. (2012) paper intended? Graded major because the passage offers independent model support for the LGM provenance result and the cited model contradicts it. |
| Suggestion | Rewrite l. 275 to 277: state that Krätschmer et al. (2022) simulate more than 90 % South American plus Australian dust with Australian dominance over most of Antarctica and identify this as a model to data mismatch; correct or replace the Albani et al. (2012) citation and "i.e." by "e.g."; remove the comparison "(here, PAT+AUS is ~77%)" or base it on a source that gives the range (see also GB-42). |
| Status | verified |
| Severity | major |
| Source | S1 |

**GB-42 Several quoted values and sample counts in Sections 4.2 to 4.4 differ from Tables S1 and S5.**

| Field | Content |
|---|---|
| Check | P1, P2, P36 |
| Location | p. 9, l. 276; p. 9, l. 281 to 282; p. 9, l. 293 to 295; p. 10, l. 321 and l. 326; p. 12, l. 408; p. 7, l. 209; p. 27, Figure 3, panel LGM, box NZ; supplement p. 13, Table S1, block YD; supplement p. 22, Table S5 |
| Quotation | "we find a higher average NZ contribution (~11%), making it the second-largest dust source to EDC during the LGM" and "(8 and 7 samples in ACR and YD" |
| Concern | Against Table S5 and its recomputation from Table S1: (1) NZ in the LGM is 14.2 % (also "14%" in l. 209; Figure 3 median 15.5 %, quartiles 10.8 and 18.9 %), not ~11 %; 11.6 % would be the mean of MIS3 and LGM together. (2) "PAT+AUS is ~77%" (l. 276): 65.7 + 10.2 = 75.9. (3) "~79 %" and "~21 %" (l. 294): PAT + NZ = 65.7 + 14.2 = 79.9, AUS + SAF + PAP = 10.2 + 6.3 + 3.6 = 20.1, so 80 and 20. (4) "high-latitude sources totaling 84 %" in HS1 (l. 295): 74.8 + 7.1 = 81.9; l. 294 to 295 cite Figure 3, which has no HS1 panel. (5) Holocene SSA "61%" (l. 321) and "60%" (l. 326): 49.0 + 0.0 + 11.0 = 60.0. (6) YD samples: Table S1 brackets nine rows as YD (11779 to 12867 yr BP, two of them at 12841), consistent with 12.9 to 11.7 kyr BP, and their mean reproduces the YD row of Table S5 exactly; no stated boundary yields seven. The ACR count of 8 is correct. Directions of the arguments are unaffected; graded moderate because a reader cannot reproduce the quoted values. |
| Suggestion | Take all quoted values from Table S5 and counts from Table S1: l. 282 "~14%", l. 276 "~76%", l. 294 "~80 %" and "~20 %", l. 295 "82 %" with Table S5 instead of Figure 3, l. 321 "60%", l. 408 "8 and 9 samples". |
| Status | verified (text, Tables S1 and S5, Figure 3); inferred (sums and means computed) |
| Severity | moderate |
| Source | SD, S3, AB |

**GB-43 The cited trajectory study models transport independent of deposition and reports New Zealand trajectories mainly to West Antarctica; the manuscript presents its figure as a share of inland Antarctic deposition.**

| Field | Content |
|---|---|
| Check | P13 |
| Location | p. 9, l. 286 to 288 |
| Quotation | "Present-day forward air-mass trajectories indicate NZ dust could contribute" and "to inland Antarctic deposition (Neff and Bertler, 2015)" |
| Concern | The abstract of Neff and Bertler (2015, J. Geophys. Res. Atmos. 120, 9303 to 9322) explores "atmospheric transport, independent of deposition processes", states that "New Zealand and Patagonia rapidly contribute a high proportion of trajectories to West Antarctica" and that "in interior East Antarctica, source contributions are limited and highly mixed". The quantity in the source is a share of trajectories, not of deposition, and the region of high New Zealand share is West Antarctica. Whether the quoted 14 to 32 % appears in the full text and for which region could not be checked. The sentence supports New Zealand as second largest LGM source at EDC (l. 282). |
| Suggestion | In l. 286 to 288 name the quantity (share of forward trajectories), the region and the period, give page or figure of the range, and add the caveat of the source that deposition is not modelled. |
| Status | verified (abstract statements); inferred (value and its region) |
| Severity | moderate |
| Source | S1 |

**GB-44 Coppo et al. (2022) read low LGM Pampean loess accumulation as aridity favouring long-range transport of southern Puna dust; the manuscript cites the same observation as support for a minimal PAP contribution under wet conditions.**

| Field | Content |
|---|---|
| Check | P13 |
| Location | p. 9, l. 289 to 292; p. 9, l. 280 to 281 |
| Quotation | "In contrast, PAP contributions during the LGM were minimal (~4 %), likely due to persistent wet conditions in the South Altiplano" and "low during both the LGM and HS1 (Coppo et al., 2022)" |
| Concern | The abstract of Coppo et al. (2022, Quat. Sci. Rev. 295, 107768) reports minimum dust accumulation "during the early part of the Last Glacial Maximum (LGM)" and states that LGM dust on the East Antarctic Plateau came either from southern central-western Argentina or from Patagonia/Tierra del Fuego plus southern Puna; "Our results favor this second scenario", linked to "more local arid conditions and less frequent rainfall, allowing more vigorous long-range transport of southern Puna dust". The manuscript uses the low accumulation in the opposite sense and omits that the favoured scenario includes southern Puna dust, which contrasts with the ~4 % PAP of this study (Table S5, LGM 3.6 %). The agreement claimed in l. 280 holds for the SSA total only. The HS1 part and the numbers in l. 278 to 279 and l. 325 to 328 could not be checked (full text restricted). Do Coppo et al. split SSA into Patagonia and southern Puna? Graded major because it concerns research aim (2) and the LGM PAP result. |
| Suggestion | In l. 289 to 292 report the interpretation of Coppo et al. (2022) as published and discuss its conflict with the ~4 % PAP; in l. 280 to 281 compare PAT and PAP separately if the paper provides the split; restrict "low during both the LGM and HS1" to what the source states, with page. |
| Status | verified (abstract of Coppo et al., 2022); inferred (HS1 statement and percentages) |
| Severity | major |
| Source | S1 |

**GB-45 A lead isotope study of the EDC core that reports local Antarctic dust in interglacial samples within the studied period is missing.**

| Field | Content |
|---|---|
| Check | P14 |
| Location | p. 10, l. 329 to 330; p. 7, l. 216 to 218 |
| Quotation | "our results do not indicate significant Antarctic contributions to EDC" |
| Concern | Vallelonga, P., Gabrielli, P., Balliana, E., Wegner, A., Delmonte, B., Turetta, C., Burton, G., Vanhaecke, F., Rosman, K. J. R., Hong, S., Boutron, C. F., Cescon, P., Barbante, C. (2010) Lead isotopic compositions in the EPICA Dome C ice core and Southern Hemisphere Potential Source Areas. Quaternary Science Reviews 29, 247 to 255, https://doi.org/10.1016/j.quascirev.2009.06.019. The abstract suggests "occasional dust contributions from local Antarctic sources"; Sect. 5.5 states that EDC samples with more than 50 % input from such a source "correspond to interglacial periods", at 10.27, 12.82, 114.12 and 122.81 kyr BP. Two of these lie within the period of this study. Sect. 5.4 further concludes that "Australian dust is not the main component". The reference list contains only Vallelonga et al. (2002, Law Dome). Offered resolution: Delmonte et al. (2020, in the list) describe local dispersal to the interior as negligible, Pb isotopes at EDC carry a volcanic component, and the excluded young samples (l. 174 to 177) may be those in which a local signal would appear. Which DEPOT result do the samples nearest to 10.27 and 12.82 kyr BP give for ANT (see also GB-15), and were they excluded? Graded major because the work contradicts a stated result on the same core. |
| Suggestion | Cite and discuss Vallelonga et al. (2010) in Section 4.3 (l. 328 to 334); report the ANT contribution of the samples nearest to 10.27 and 12.82 kyr BP, or state that they were excluded. |
| Status | verified (content of Vallelonga et al., 2010; absence from the reference list); inferred (correspondence of their samples with the DEPOT sample set) |
| Severity | major |
| Source | S1 |

**GB-46 Figure 5 is cited before Figure 4, and Table S4 is not cited in the main text.**

| Field | Content |
|---|---|
| Check | P4, P3 |
| Location | p. 10, l. 340; p. 12, l. 405; p. 26, l. 865; p. 28, l. 876 |
| Quotation | "Aike bog (see Figure 5)" and "Figures 4 and S5 (for millennial trends)" |
| Concern | Figures 1 to 5 exist once each without gap, but Figure 5 is first cited at l. 340 and Figure 4 at l. 405. Supplement tables are first cited in the order S1 (l. 127), S2 (l. 128), S5 (l. 191), S3 (l. 246); Table S4 appears only in two figure captions, both pointing to the wrong table (KK-76, KK-80). |
| Suggestion | Swap the numbers of Figures 4 and 5, and cite Table S4 in Section 4.1 (l. 254 to 255) where the measured values are discussed. |
| Status | verified |
| Severity | minor |
| Source | S4, AB |

**GB-47 The drop in Patagonian contribution between 6 and 6.5 kyr BP is said to be present in the Potrok Aike wind record, but Figure 5B shows no excursion there.**

| Field | Content |
|---|---|
| Check | P3, P24 |
| Location | p. 11, l. 350 to 352; p. 29, Figure 5, panels A and B |
| Quotation | "Apart from a well-marked drop in PAT contributions between 6-6.5 kyr BP (also present in Potrok Aike wind intensity record)" |
| Concern | The PAT drop is real: the smoothed PAT curve of Figure 1 has a minimum of 28.8 % at 6.33 kyr BP. In Figure 5B the MDF curve lies between 16.5 and 18.3 mT from 6.0 to 6.5 kyr, 13.8 to 21.5 mT from 5 to 6 kyr and 15.3 to 17.5 mT from 6.5 to 7 kyr, on an axis from 10 to 70 mT; within the blue band (7.96 to 11.43 kyr) it swings from 14.3 to 49.2 mT. A comparable excursion at 6 to 6.5 kyr is not visible. Do the authors refer to the original record at higher resolution? |
| Suggestion | Mark the excursion in Figure 5B and give the MDF change, or delete the parenthesis in l. 351. |
| Status | verified (Figure 5B measured); assumption (content of the original record, asked as a question) |
| Severity | moderate |
| Source | AB |

**GB-48 One citation has no reference entry, and one reference entry is not cited.**

| Field | Content |
|---|---|
| Check | P4 |
| Location | p. 11, l. 365; references p. 18, l. 630 to 632 |
| Quotation | "consistent with the previous Pb isotopic study (Gili et al., 2016)" |
| Concern | The reference list has Gili et al. 2017 and 2022 but no 2016 item. The text cites "Gaiero, 2007" (l. 274; l. 862), which matches the single-author entry; the four-author Chemical Geology entry of the same year (Gaiero, Brunet, Probst, Depetris, 2007) is cited nowhere. |
| Suggestion | Add the entry Gili, S., Gaiero, D. M., Goldstein, S. L., Chemale, F., Koester, E., Jweda, J., Vallelonga, P., Kaplan, M. R. (2016) Provenance of dust to Antarctica: a lead isotopic perspective. Geophysical Research Letters 43, 2291 to 2298, https://doi.org/10.1002/2016GL068244; cite or delete the Gaiero et al. (2007) Chemical Geology entry. |
| Status | verified (manuscript; bibliographic data from the CONICET repository record) |
| Severity | minor |
| Source | S4 |

**GB-49 The cited Lake Eyre record describes a weak early Holocene monsoon and a dry to wet transition near 12 ka, not prolonged wet conditions from 14.5 kyr BP.**

| Field | Content |
|---|---|
| Check | P13 |
| Location | p. 11, l. 367 to 371 |
| Quotation | "experienced prolonged wet conditions between 14.5" and "These humid intervals would have lowered dust emissions from central Australia." |
| Concern | Magee et al. (2004, Geology 32, 885 to 888), titled with "unexpected Holocene failure", report in the abstract "Abrupt transitions from dry phases to wet phases (ca. 125 and 12 ka)" and "the low intensity of the early Holocene Australian monsoon". Neither the onset at 14.5 kyr BP nor prolonged wet conditions until 4 kyr BP appear in the abstract; the full text and Singh and Luly (1991) were not read. The sentence carries the argument that central Australia emitted less dust and the Darling sub-basin dominated (l. 366 to 372). |
| Suggestion | In l. 368 to 370 assign each wet interval to the record that shows it, with page, and reconcile the statement with the weak early Holocene monsoon reported by Magee et al. (2004). |
| Status | verified (abstract of Magee et al., 2004); inferred (full text; Singh and Luly, 1991) |
| Severity | moderate |
| Source | S1 |

**GB-50 The Holocene increase in SAF contributions is referenced to Figure S4, which shows box plots for the Early Holocene only and no time trend.**

| Field | Content |
|---|---|
| Check | P4, P3 |
| Location | p. 11 to 12, l. 381 to 382; supplement pp. 7 to 8, Figure S4 |
| Quotation | "results show an increasing trend in SAF dust contribution to EDC ice core (Figure S4)" |
| Concern | Figure S4 shows box plots for the Early Holocene, YD, ACR, HS1 and MIS3; a trend within the Holocene cannot be read from it. The SAF time series is in Figure 1 and, for sub-regions, Figure S3. The trend is weak in Table S1: a linear fit of SAF against age over the 116 Holocene samples gives 0.54 % per kyr towards the present with r = minus 0.08; Late Holocene mean 11.6 %, Early Holocene 9.8 % (Table S5). |
| Suggestion | Refer to Figure 1 or Figure S3 in l. 382, and give the trend with a statistic or describe it as a small difference between the Early and Late Holocene means. |
| Status | verified (Figure S4 on the page image); inferred (trend statistic computed) |
| Severity | minor |
| Source | S4, AB |

**GB-51 The Holocene comparison of EDC and EDML uses the whole EDC Holocene against the EDML Early Holocene, outside the stated overlap, and reports differences without uncertainty.**

| Field | Content |
|---|---|
| Check | P38, P21, P3, P9 |
| Location | p. 12, l. 405 to 407; p. 13, l. 423 to 424; p. 28, Figure 4, bars "Holo" and caption l. 875 to 876; supplement p. 22, Table S5, rows "Holocene (2.8-11.7 kyr)" (EDC) and "Early Holocene (7.5-11.7 kyr)" (EDML); p. 1, l. 27 to 29 |
| Quotation | "over their overlapping interval shared by both datasets, i.e., between 7.5 and 27 kyr BP" and "In the Holocene, the discrepancies become more pronounced: EDC appears to receive substantially less PAT dust (-14%) but higher contributions of Australian dust (+12%) than EDML." |
| Concern | Table S5 gives EDML only for the Early Holocene. The quoted differences follow only from the EDC whole Holocene minus the EDML Early Holocene: PAT 49.0 minus 62.7 = minus 13.7, AUS 23.1 minus 10.8 = +12.3; the measured Holo bars of Figure 4 (PAT minus 13.97, AUS 12.44) match this pair within 0.27 points and not the matched pair. On the shared window (EDC Early Holocene) the differences are PAT 47.1 minus 62.7 = minus 15.6 and AUS 24.9 minus 10.8 = +14.1. 60 of the 116 EDC samples entering the quoted value (Late Holocene) lie outside the overlap stated in l. 406 to 407. The direction stands, but the magnitude and the time window change, and the abstract statement that EDC shows "more consistent inputs from Australia" (l. 28 to 29) rests on this Holocene difference: in ACR and YD the AUS difference is negative (minus 7.4 and minus 4.5, Table S5). The same issue may apply to the LGM bar if EDC LGM samples older than 27 kyr enter it. Differences of a few points are interpreted without the Monte Carlo spread (GB-19), and the EDML values come from another model configuration (GB-17). Graded major because the comparison answers research aim (4) and feeds the abstract. |
| Suggestion | Compute the Holocene (and if needed LGM) differences in l. 423 to 424, Figure 4 and Table S5 from identical windows, label the bars "Early Holocene (7.5 to 11.7 kyr BP)", state the period limits of both cores in the Figure 4 caption, give each difference with its uncertainty, and revise l. 28 to 29 accordingly. |
| Status | verified (Table S5, text, Figure 4 bars measured); inferred (differences computed; LGM part) |
| Severity | major |
| Source | S2, S3, AB, SD |

**GB-52 The limitation that ACR and YD rest on few samples is stated only in Section 4.4, after ACR and YD values have been interpreted.**

| Field | Content |
|---|---|
| Check | P17 |
| Location | p. 12, l. 407 to 409; p. 6, l. 192 to 193, l. 203 to 212; p. 7, l. 233 to 236; p. 8, l. 251 to 253 |
| Quotation | "It is important however to note that results for ACR and YD are tentative due to the limited number samples covering those periods in EDC" |
| Concern | The manuscript discloses the limitation, but a reader of Section 3 sees ACR and YD averages ("sharp increase during the YD with 15%", l. 207) and the "major shift [...] at the onset of the ACR" (l. 233) without it. The consequence for the timing argument (GB-37) is not drawn. |
| Suggestion | Give the number of samples per period in Section 3 and Table S5 (GB-27) and move the caveat to l. 184 to 188. |
| Status | verified |
| Severity | moderate |
| Source | SD |

**GB-53 For ACR and YD the text swaps the two Patagonian differences and says the YD enrichment comes at the expense of Southern Africa, while Table S5 and Figure 4 show a positive SAF difference for the YD.**

| Field | Content |
|---|---|
| Check | P2, P3 |
| Location | p. 13, l. 421 to 422; p. 28, Figure 4, panels PAT, SAF, AUS, bars YD and ACR; supplement p. 22, Table S5, rows ACR and YD |
| Quotation | "the ACR and YD intervals exhibit a slight enrichment of Patagonian dust (+4 and +6.5%) in EDC, primarily at the expense of Southern African and Australian contributions." |
| Concern | From Table S5: PAT ACR 68.9 minus 62.5 = +6.4, PAT YD 63.1 minus 58.4 = +4.7 (Figure 4 measured: +6.49 and +4.96), so the text assigns the values in reverse order. SAF ACR 8.0 minus 12.4 = minus 4.4, but SAF YD 14.6 minus 8.2 = +6.4: in the YD EDC receives more SAF dust than EDML, driven by one sample (GB-32); the YD PAT excess is balanced by AUS (minus 4.5), NZ (minus 3.9) and PAP (minus 2.4). The authors rightly call these results tentative (l. 407 to 409), and their size is comparable to the standard errors of the EDC means (PAT ACR 5.1, YD 9.8). |
| Suggestion | Rewrite l. 421 to 422 as "+6.4 % in the ACR and +4.7 % in the YD", name AUS and SAF as the compensating sources for the ACR and AUS, NZ and PAP for the YD, and give standard errors in Table S5. |
| Status | verified (text, Table S5, Figure 4 measured); inferred (differences and standard errors computed) |
| Severity | moderate |
| Source | S3, AB, SD |

**GB-54 The decline in total dust deposition "in both cores" is referenced to Figures S2 and S5, but neither shows deposition at EDML.**

| Field | Content |
|---|---|
| Check | P4, P3 |
| Location | p. 13, l. 447 to 450; supplement pp. 3 to 4, Figure S2; supplement pp. 9 to 10, Figure S5 |
| Quotation | "the earlier, more gradual yet massive decline in total dust deposition that began around 19-18 kyr BP and continued until ~15 kyr BP in both cores (Figures S2 and S5)" |
| Concern | Figure S2 shows nssCa2+ flux, δ18O and deuterium excess for EDC only; Figure S5 shows relative contributions in percent for EDC and EDML, no deposition or flux. The EDML half of the statement has no target in the manuscript, and the decoupling claim of the conclusion (l. 483 to 484) rests on it. |
| Suggestion | Add an EDML dust flux series to Figure S2 (or a panel to Figure S5), or cite the EDML flux source in l. 449 to 450 and cite only Figure S2 for EDC. |
| Status | verified (page images of supplement pp. 4 and 10) |
| Severity | moderate |
| Source | S4, AB |

**GB-55 The attribution of the provenance shift to shelf submersion and drainage reorganisation is stated as demonstrated, although the manuscript shows a temporal coincidence and some of its own results do not fit the mechanism.**

| Field | Content |
|---|---|
| Check | P15, P10 |
| Location | p. 14, l. 461 to 470; p. 14, l. 480 to 482; p. 14 to 15, l. 488 to 490; p. 1, l. 29 to 31 |
| Quotation | "led to a persistent decline in high-latitude dust contributions" and "Importantly, our data demonstrate that these feedback mechanisms influenced dust deposition not only in EDML" |
| Concern | The data establish a change in relative contributions; the mechanism is inferred from coincidence with sea-level and drainage events taken from the literature (l. 450 to 460), and no analysis tests it against alternatives. Three of the manuscript's own results limit the claim. (a) The NZ contribution halves before 14.5 kyr BP, from 14.2 % in the LGM to 7.1 % in HS1 (Table S5; l. 209 to 210), so the NZ shelf submergence invoked in l. 461 to 462 cannot account for most of the NZ decline. (b) At EDC the PAT decline is not dated to 14.5 kyr BP (GB-37). (c) PAT is higher in the Late Holocene (50.7 %) than in the Early Holocene (47.1 %), and Section 4.3 explains Holocene PAT by westerlies and fire (l. 339 to 352), so "persistent decline" is not supported for the Holocene part. The discussion itself names transport changes as co-driver (l. 308 to 314, l. 440 to 443). Graded major because the attribution is the main interpretive claim of abstract and conclusion. |
| Suggestion | In l. 466 to 470, the abstract (l. 29 to 31) and the conclusion (l. 480 to 482, l. 488 to 490) replace "demonstrate" and "led to" with wording that matches a coincidence ("is consistent with"), discuss the NZ decline before 14.5 kyr BP separately, and name an observation that would separate shelf submersion from transport changes (for example the relative timing at EDC and EDML with uncertainties, or the size of the PAT drop predicted from the lost shelf area). |
| Status | verified (wording and Table S5 values); inferred (that the NZ decline predates the invoked mechanism) |
| Severity | major |
| Source | S4, SD |

**GB-56 The conclusion and discussion call the record "continuous" and "high-resolution" without carrying through the sampling gaps the manuscript discloses.**

| Field | Content |
|---|---|
| Check | P15 |
| Location | p. 14, l. 472 to 473; p. 7, l. 220 and l. 230; p. 12, l. 403; p. 4, l. 113; p. 6, l. 174 to 176; supplement p. 14, Table S1 |
| Quotation | "This study presents the first high-resolution, continuous and quantitative reconstruction of dust provenance in the EDC ice core" |
| Concern | The manuscript discloses a sampling gap between 21.7 and 27.3 kyr BP (l. 113), the exclusion of 38 samples younger than 14 kyr BP (l. 174 to 176) and tentative ACR and YD results (l. 407 to 409). The retained samples in Table S1 have intervals of 2280 years (23104 to 25384 yr BP) and 1785 years (25640 to 27425 yr BP); ACR holds 8 and YD 9 samples. The conclusion keeps "continuous" and "high-resolution" without qualification. Graded moderate: the statement overstates coverage; the results themselves stand. |
| Suggestion | In l. 472 and l. 220 qualify "continuous" (for example "near-continuous, with a gap between 23.1 and 27.4 kyr BP") and give the resolution of the retained record per period. |
| Status | verified (disclosures, Table S1 ages); inferred (interval lengths) |
| Severity | moderate |
| Source | S4 |

**GB-57 Two conclusion statements go beyond what the results show: a cause for the 18 to 15 kyr flux decline and implications for the hemispheric dust cycle and biogeochemical fluxes.**

| Field | Content |
|---|---|
| Check | P15 |
| Location | p. 14, l. 483 to 484; p. 15, l. 490 to 492; p. 9, l. 296 to 298 |
| Quotation | "the massive decline in dust deposition that occurred between 18 and 15 kyr BP due to changing atmospheric transport dynamics" and "These processes, in turn, contributed to the persistent reorganization of the Southern Hemisphere dust cycle during the LGIT, with implications for biogeochemical fluxes" |
| Concern | The discussion presents the transport cause as likely ("The latter likely reflects intensified", l. 296 to 297); the conclusion states it as established. The flux record is taken from Fischer et al. (2007) and is not a result of this study, and no PSA-specific flux is reported (GB-20). The results are relative proportions at one site, so a reorganisation of the hemispheric dust cycle and implications for biogeochemical fluxes, the motivation of l. 37 to 52, are not shown. |
| Suggestion | Write "likely due to" in l. 484, and either add the PSA flux series announced in l. 166 to 167 or limit l. 490 to 492 to the relative composition of dust reaching East Antarctica. |
| Status | verified (wording; content of Figure S2 on the page image) |
| Severity | moderate |
| Source | S4 |

**GB-58 The conclusion explains the EDC and EDML differences by climate in the source areas, while the discussion explains them by the position of the two sites in the circulation.**

| Field | Content |
|---|---|
| Check | P15 |
| Location | p. 14, l. 484 to 487; p. 13, l. 424 to 443 |
| Quotation | "the relative contributions of PAT, SAF, NZ and AUS differed reflecting regional climatic dynamics in their respective source areas" |
| Concern | Section 4.4 builds a transport argument: EDML lies under the Atlantic storm track, EDC is shielded by the polar vortex and receives low-latitude dust via Rossby-wave intrusions and the subtropical jet (l. 424 to 440). Climate in a source area changes what that source emits and acts on both cores alike, so it cannot by itself produce a difference between two cores fed by the same sources. The conclusion therefore states a cause the discussion does not develop. Graded major because it concerns the answer to research aim (4). |
| Suggestion | Rewrite l. 486 to 487 so that the between-site differences are attributed to transport pathways and site position as argued in Section 4.4, and keep source-area climate for the common temporal changes. |
| Status | verified |
| Severity | major |
| Source | S4 |

**GB-59 The data and code statement does not cover the input REE dataset, the excluded samples, the correction factors, the uncertainties or the DEPOT code.**

| Field | Content |
|---|---|
| Check | P12, P8 |
| Location | p. 16, l. 494 to 496; p. 4, l. 107 to 109, l. 114, l. 117 to 124; p. 5, l. 139 to 140, l. 155 to 165; p. 6, l. 174; supplement p. 11, Table S1 caption |
| Quotation | "All data needed to evaluate the conclusions in the paper are present in the paper and/or the Supplementary Materials. Additional data related to the paper may be requested from the authors." |
| Concern | The supplement makes the source side transparent (Tables S2 to S5). The ice-core side is not: (1) the 294 measured REE patterns of Gabrielli et al. (2010) that enter Eq. 2; (2) the identities of the 15 samples with missing data and the 38 below the R threshold (Table S1 holds 241 rows although its caption names 279, so the excluded samples are not there either); (3) the cf_i and their variability; (4) the element-specific analytical uncertainties, given only as 2 to 10 %. None of these appears in manuscript or supplement, and a search of PANGAEA found the EDML REE series of Wegner et al. (2012) but no deposit of the EDC series. The heading announces code, but the text addresses only data; the scripted procedure (matrix construction, sampling, 2000 runs, aggregation, R per run, flux conversion, 9-step smoothing) has no repository, version or licence, and the present variant differs from the 2023 version (13 instead of 14 elements), so a pointer to that paper would not cover it. None of these data concern persons, so "may be requested" withholds them without a reason. |
| Suggestion | In l. 494 to 496 name the repository or supplement table for the 294 input patterns; add a table of all 294 samples (age, REE as used, inclusion flag and reason) and of cf_i and per-element uncertainties; deposit the MATLAB scripts with version and input files, or give the reason if they are not released. |
| Status | verified (statement wording, absence of the four inputs and of code); inferred (that the EDC series is not in a public repository, one search); assumption (that the code exists in releasable form) |
| Severity | moderate |
| Source | S2, SD |

**GB-60 The author contribution statement assigns the measurements to "P.B", initials that match no author.**

| Field | Content |
|---|---|
| Check | P38, P4 |
| Location | p. 16, l. 497 to 499; p. 1, l. 4 to 5; supplement p. 17, Table S2, six rows with reference "this study" |
| Quotation | "P.B performed the measurements; A.V., St. B and G.L. developed together the model" |
| Concern | The authors are S. Boxho, A. Vanderstraeten, N. Mattielli, G. G. Laruelle, A. Bory, P. Gabrielli and S. Bonneville; none has the initials P.B. The statement does not say which measurements are meant: the EDC REE data come from Gabrielli et al. (2010, l. 108), and the only new data are six SAF dust source samples marked "this study" in Table S2. N.M. and A.B. are covered only by "All authors reviewed the manuscript", and the same author appears as "St. B" and "St.B." in consecutive lines. Is P.G. meant? |
| Suggestion | Correct the initials in l. 497, state which measurements were made for this study and by whom, state the contributions of N.M. and A.B., and unify the initials as "Si.B." and "St.B.". |
| Status | verified (initials, author list); assumption (that P.G. is meant, asked as a question) |
| Severity | minor |
| Source | S2, S4 |

**GB-61 The reference list prints RTF control codes in 18 entries and mixes several citation formats.**

| Field | Content |
|---|---|
| Check | P16 |
| Location | references pp. 16 to 22, for example p. 16, l. 528 and p. 19, l. 703; entries Ding et al. (l. 584 to 585), Gaiero et al. 2013 (l. 633 to 636), Parrenin et al. (l. 726 to 729), Placzek et al. (l. 732), Rudnick and Gao (l. 762 to 763), Yang et al. (l. 844 to 846) |
| Quotation | "471\uc0\u8211{}501. https://doi.org/10.1191/0309133303pp386ra\" |
| Concern | On the page images escape sequences such as "\uc0\u8211{}" (en dash), "\uc0\u237{}" (i acute) and a trailing backslash after the DOI are printed in 18 entries (Bullard and McTainsh 2003, De Deckker et al. 2014, Dukes et al. 2018, Engelbrecht et al. 2019, Fletcher and Moreno 2012, Gaiero et al. 2007, Gingele and De Deckker 2005, Grousset and Biscaye 2005, Lisé-Pronovost et al. 2015, Markgraf et al. 2007, Markle et al. 2018, Moreno et al. 2010, Power et al. 2008, Quade and Kaplan 2017, Stone et al. 2010, Stuut et al. 2002, Veres et al. 2013, Wagner et al. 2021). The entries follow different styles: Ding et al. with "et al." in the author list, Gaiero et al. 2013 in AGU style, Yang et al. in APA style, Placzek et al. with "doi: https://", Rudnick and Gao with "Vol. 03", Delmonte et al. 2007 (l. 565) with a stray "6."; Parrenin et al. (2007) lacks volume, pages and DOI. |
| Suggestion | Regenerate the reference list from the reference manager as plain text in one style, and complete the Parrenin et al. (2007) entry. |
| Status | verified (page images pp. 16 to 22) |
| Severity | minor |
| Source | S4 |

**GB-62 The box plot labelled "Holocene" in Figure 3 shows the Early Holocene means of Table S5, the box plot labelled "Early Holocene" in Figure S4 shows the Late Holocene means, and the YD and ACR means of Figure S4 lie about 1 point above Table S5.**

| Field | Content |
|---|---|
| Check | P3 |
| Location | p. 27, Figure 3, panel Holocene, caption l. 869 to 873; supplement pp. 7 to 8, Figure S4, panels (1) Early Holocene, (2) YD, (3) ACR; supplement p. 22, Table S5 |
| Quotation | "Box plots of provenance contributions (in %) of Holocene, and Last Glacial Maximum (LGM) dust depositions in EDC ice core." |
| Concern | Mean crosses measured in Figure 3: PAT 47.2, PAP 10.0, SAF 9.8, AUS 24.9, NZ 8.3 % (±0.36); Table S5 Early Holocene 47.1, 10.0, 9.8, 24.9, 8.1, Holocene 49.0, 11.0, 10.7, 23.1, 5.9; differences to Early Holocene at most 0.22, to Holocene up to 2.42 points. Figure S4 panel (1): PAT 50.7, PAP 12.0, SAF 12.0, AUS 21.7, NZ 3.8 % (±0.17), equal to Table S5 Late Holocene (50.7, 12.0, 11.6, 21.4, 3.8). Either both figures are mislabelled (the full Holocene is then shown nowhere) or the Early and Late rows of Table S5 are swapped; in both cases Figure 3 does not show the "Holocene" its caption names. In Figure S4 the PAT means measure 64.2 % (YD) and 70.0 % (ACR) against 63.1 and 68.9 in Table S5, beyond the measurement uncertainty, which suggests different sample sets. |
| Suggestion | Check which period each box plot shows and relabel Figure 3, Figure S4 or Table S5; add a full or Late Holocene panel; state the number of samples per panel in both captions and use the same samples in Figure S4 and Table S5. |
| Status | verified (means measured); inferred (which reading applies) |
| Severity | moderate |
| Source | AB |

**GB-63 The captions of Figure 3 and Figure S4 say the whiskers mark the extremes, but both figures plot points beyond the whiskers, and the points are not explained.**

| Field | Content |
|---|---|
| Check | P29, P3 |
| Location | p. 27, l. 871 to 872; p. 27, Figure 3, panels Holocene AUS and LGM PAT; supplement pp. 7 to 8, Figure S4 |
| Quotation | "the whiskers indicate the lower and upper extremes" |
| Concern | Figure 3, Holocene AUS: upper whisker at 79.8 %, three points above at 84.4, 95.3 and 98.1 %; LGM PAT: whisker at 84.4 %, one point at 93.5 %. Figure S4, Early Holocene AUS: whisker at 56.1 %, highest point 94.0 %. The whiskers follow another rule (perhaps 1.5 times the interquartile range), and the dots, the individual samples, are not mentioned. |
| Suggestion | State the whisker rule in both captions and add "dots: individual samples; points beyond the whiskers: outliers". |
| Status | verified |
| Severity | minor |
| Source | AB |

**GB-64 Figure 5 has no time axis title or unit in panel B, and its blue band, dashed lines and grey zones are not explained.**

| Field | Content |
|---|---|
| Check | P29 |
| Location | p. 29, Figure 5, panels A and B; caption l. 880 to 882; p. 10, l. 340 |
| Quotation | "Comparison of the contribution of Patagonian dust (PAT) to EDC ice core (A) and (B) the Median Destructive Field" |
| Concern | The x axis of panel B carries only the numbers 0.5 to 3, without title, unit or the factor ×10^4 of Figure 1. The blue band between dashed lines measures 7.96 to 11.43 kyr BP in both panels; the text speaks of "The 11 to 8 kyr BP period" (l. 340), but the caption does not say so and the upper edge lies 0.43 kyr above 11 kyr. The grey zones and the arrow "Wind intensity" are not explained; in panel B the YD zone ends at 13.02 kyr, 0.13 kyr later than in panel A. |
| Suggestion | Add "Time (yr BP) ×10^4" to panel B, explain band, dashed lines, grey zones and the direction of the MDF axis in the caption, and align the band edges with l. 340 or give the reason for 11.4 kyr. |
| Status | verified |
| Severity | minor |
| Source | AB |

**GB-65 The EDML legend entries and curves in Figure S5 are printed in very pale colours.**

| Field | Content |
|---|---|
| Check | P3 |
| Location | supplement p. 10, Figure S5, legend boxes of all five panels |
| Quotation | "Comparison between EDC and EDML ice cores in terms of dust provenance contributions (mobile average over 9 steps) through the LGIT" |
| Concern | The EDML text colours measure #fcecbc (AUS), #fcbcbc (SAF), #bcecd4 (NZ) and #bcecfc (PAP); their contrast against white is 1.18, 1.61, 1.31 and 1.27, far below the 4.5 usually required for text. The pale EDML curves have the same problem, so the two cores are hard to tell apart in print. |
| Suggestion | Use darker colours or different line styles for EDML and name the line styles in the caption. |
| Status | verified |
| Severity | minor |
| Source | AB |

**GB-66 Seven sources cited in the supplement for the dust source database and the ice-core isotope data have no entry in any reference list.**

| Field | Content |
|---|---|
| Check | P4 |
| Location | supplement pp. 16 to 19, Table S2, column "Reference"; supplement p. 21, Table S4, column "Reference"; references pp. 16 to 22 |
| Quotation | "Marx and Kamber, 2010" and "Diaz et al. , 2018" |
| Concern | The supplement has no reference list, and none of Marx et al. (2005), McGowan et al. (2005), Marx and Kamber (2010), Diaz et al. (2018), Aarons et al. (2017), Bory et al. (2010) and "Delmonte et al., 2004a" appears among the 91 entries of the main list. They supply 117 of the 217 rows of Table S2 (Marx et al. 2005: 10; McGowan et al. 2005: 2; Marx and Kamber 2010: 101; Diaz et al. 2018: 4) and 34 of the 35 measured values in Table S4. The suffix "2004a" implies a second Delmonte et al. (2004) item; the list holds one, a dust size study. A reader cannot trace the end-member database or the validation data to their sources. |
| Suggestion | Add full entries for the seven sources to the reference list (or a reference list to the supplement) and resolve "Delmonte et al., 2004a" to one entry. |
| Status | verified |
| Severity | moderate |
| Source | S4 |

#### Minor corrections

| ID | Location | Quotation | Replacement | Source |
|---|---|---|---|---|
| KK-24 | p. 7, l. 220; supplement p. 21, Table S4, column Localisation | "in the Epica Dome C ice core"; "Epica dome C" | "in the EPICA Dome C (EDC) ice core"; "EPICA Dome C" | S2, S4 |
| KK-25 | p. 7, l. 233 | "Our calculations highlight a major shift in dust provenance occurred" | "Our calculations highlight that a major shift in dust provenance occurred" | S4 |
| KK-26 | p. 7, l. 236 | "This shift already describes by Gili et al. (2022) and Vanderstraeten et al. (2023), appears" | "This shift, already described by Gili et al. (2022) and Vanderstraeten et al. (2023), appears" | S4 |
| KK-27 | p. 7, l. 242 | "(Basile et al. 1997; Delmonte et al. 2007)" | "(Basile et al., 1997; Delmonte et al., 2007)" | S4 |
| KK-28 | p. 8, l. 246 | "(Table S3, e.i. Eq.3)" | "(Table S3; Eq. 3)" | S4, SD |
| KK-29 | p. 8, l. 249 | "where the mean isotopic signatures is represents by CIR PSA" | "where CIR_PSA is the mean isotopic signature of each PSA" | S4 |
| KK-30 | p. 8, l. 261 | "4.2 Persistance of high-latitude dust source to EDC" | "4.2 Persistence of high-latitude dust sources to EDC" | S4 |
| KK-31 | p. 8, l. 270 | "by ~763.10³ km²" | "by ~763 × 10³ km²" | S4 |
| KK-32 | p. 8, l. 272 | "those from SSA- to EDC" | "those from SSA to EDC" | S4 |
| KK-33 | p. 9, l. 288 | "detected NZ dust at ~6 % on average over the entire LGM" | "detected NZ dust at ~6 % on average over the entire LGM (Vanderstraeten et al., 2023)" | S4 |
| KK-34 | p. 9, l. 300 | "before 14.5 kyr BP reflect a transport regime" | "before 14.5 kyr BP reflects a transport regime" | S4 |
| KK-35 | p. 9, l. 301 | "strong westerlies -a system" | "strong westerlies, a system" | S4 |
| KK-36 | p. 9, l. 306 | "reveals a significantly larger variability" | "reveals a markedly larger variability" (no significance test is reported) | S4 |
| KK-37 | p. 10, l. 311 | "«wet scavenging»" | "“wet scavenging”" (as "rainout" in l. 297) | S4 |
| KK-38 | p. 10, l. 312 | "trajectories inferred by increased deuterium-excess values" | "trajectories inferred from increased deuterium-excess values" | S4 |
| KK-39 | p. 10, l. 313 | "from the mid-latitudes of Indian Ocean" | "from the mid-latitudes of the Indian Ocean" | S4 |
| KK-40 | p. 10, l. 320 | "at 70 ± 20% (Kok" | "at ~70 % (Kok et al., 2021, Sect. 3.4.1)"; Sect. 3.4.1 of Kok et al. gives ~70 % without the ± 20 % | S1 |
| KK-41 | p. 10, l. 325 | "reduction in SSA input -down to 33%-" | "reduction in SSA input (down to 33 %)" | S4 |
| KK-42 | p. 10, l. 329 to 330 | "includes several McMurdo region sites (Section 4.2)" | "includes several McMurdo region sites (Section 2)"; the sites are listed in l. 132 to 133 | S4 |
| KK-43 | p. 10, l. 334 | "(Speirs et al., 2001)" | "(Speirs et al., 2010)" (only entry in the list) | S4 |
| KK-44 | p. 10, l. 336 | "during the ACR, YD reaching minimum values" | "during the ACR and YD, reaching minimum values" | S4 |
| KK-45 | p. 10, l. 338 | "centered ~9 kyrs BP" | "centered at ~9 kyr BP" | S4 |
| KK-46 | p. 10, l. 339 to 341 | "is matching well with the SWW intensity proxies in Potrok Aike bog" and "a weakening of South Westerlies Winds (SWW)" | "matches the intensity proxies of the Southern Hemisphere westerly winds (SWW) in Laguna Potrok Aike" and "a weakening of the SWW" | S2, S4 |
| KK-47 | p. 10, l. 341 | "Moreno et al. (2010);" | "Moreno et al., 2010;" | S4 |
| KK-48 | p. 10, l. 342 to 343 | "(Quake and Kaplan, 2017)" | "(Quade and Kaplan, 2017)" | S4 |
| KK-49 | p. 10, l. 346 | "Fires co-emit mineral soil-dust particle" | "Fires co-emit mineral soil-dust particles" | S4 |
| KK-50 | p. 11, l. 348 | "in S-E Patagonia" | "in southeastern Patagonia" | S4 |
| KK-51 | p. 11, l. 348 to 349 | "(Potrok Aike bog 52°S" | "(Laguna Potrok Aike, 52°S" (a lake record, as in the Figure 5 caption, l. 882) | S2, S4 |
| KK-52 | p. 11, l. 354 | "Dust emission from PAP are primarily linked" | "Dust emissions from PAP are primarily linked" | S4 |
| KK-53 | p. 11, l. 356 | "(i.e., North Puna does not contribute)" | "(North Puna does not contribute)" | S4 |
| KK-54 | p. 11, l. 365 | "(Gili et al., 2016) ." | "(Gili et al., 2016)." | S4 |
| KK-55 | p. 11, l. 366 | "As far as Australian dust contribution," | "As far as the Australian dust contribution is concerned," | S4 |
| KK-56 | p. 11, l. 367 | "De Deccker et al. (2010)" | "De Deckker et al. (2010)" | S4 |
| KK-57 | p. 11, l. 374 | "(post-7.5 kry" | "(post-7.5 kyr" | S4 |
| KK-58 | p. 11, l. 376 | "El-Nino-Southern Oscillation" | "El Niño-Southern Oscillation" | S4 |
| KK-59 | p. 12, l. 384 to 385 | "suggesting strengthened dust transport from southern Africa suggesting strengthened dust transport from southern Africa" | "suggesting strengthened dust transport from southern Africa" | S4 |
| KK-60 | p. 12, l. 396 | "include few substantial inputs" | "include a few substantial inputs" | S4 |
| KK-61 | p. 12, l. 397 to 398 | "kyr BP (Brook et al., 2011)." (parenthesis opened in l. 397 not closed) | "kyr BP; Brook et al., 2011)." | S4 |
| KK-62 | p. 12, l. 399 | "likely reflect their low-frequency, high-magnitude nature of their dust emissions" | "likely reflect the low-frequency, high-magnitude nature of their dust emissions" | S4 |
| KK-63 | p. 12, l. 408 | "due to the limited number samples" | "due to the limited number of samples" | S3, S4 |
| KK-64 | p. 13, l. 426 | "to receive dust from Patagonia dust brought in" | "to receive Patagonian dust brought in" | S4 |
| KK-65 | p. 13, l. 427 | "located at the interior of EAP" | "located in the interior of the East Antarctic Plateau" (EAP is not defined) | S2, S4 |
| KK-66 | p. 13, l. 428 | "mid-latitude air masses incursions" | "mid-latitude air-mass incursions" | S4 |
| KK-67 | p. 13, l. 439 | "De Deccker et al., 2019" | "De Deckker, 2019" (single-author entry, l. 551) | S4 |
| KK-68 | p. 14, l. 457 | "redirecting large portion of river catchment" | "redirecting a large portion of the river catchments" | S4 |
| KK-69 | p. 14, l. 480 to 481 | "As such those results confirm our previous study on the EDML dust record showing similar shift" | "As such, these results confirm our previous study on the EDML dust record, which showed a similar shift" | S4 |
| KK-70 | p. 16, l. 501 | "APPENDIX S. SUPPLENTARY DATA. Supplementary data to this article" | "SUPPLEMENT. The supplement related to this article is available online." | S4 |
| KK-71 | p. 20, l. 748 | "Environùental characterization" | "Environmental characterization" | S4 |
| KK-72 | p. 20, l. 763 | "Holland HD, Turkian KK (eds)" | "Holland HD, Turekian KK (eds)" | S4 |
| KK-73 | p. 21, l. 800 | "Sudgen, D. E., McCulloch" | "Sugden, D. E., McCulloch" (cited as "Sugden et al., 2009", l. 266) | S4 |
| KK-74 | p. 26, l. 858 (Figure 2 caption) | "refs. Table S1" | "references in Table S4" | S2, S4, AB |
| KK-75 | p. 26, l. 863 (Figure 2 caption) | "the SAF and AUS domain is more extended than showed in the Figure" | "the SAF and AUS domains are more extended than shown in the figure" | S4, AB |
| KK-76 | p. 26, l. 865 (Figure 2 caption) | "the isotopic fingerprint (Table S4)" | "the isotopic fingerprint (Table S3)" (end-member isotopes are in Table S3) | S2, S4, AB |
| KK-77 | p. 26, Figure 2, x axis tick labels | "0,700" (and 0,705 to 0,730) | "0.700" (decimal point throughout) | AB |
| KK-78 | p. 27, Figure 3, y axis tick labels of both panels; supplement p. 8, Figure S4 | "100,00" (and 0,00 to 90,00) | "100" (and 0 to 90) | AB |
| KK-79 | p. 28, l. 875 (Figure 4 caption) | "Figure 4: Histograms representing" | "Figure 4: Bar charts representing" | S4, AB |
| KK-80 | p. 28, l. 876 (Figure 4 caption) | "between EDC and EDML ice cores (Table S4)." | "between EDC and EDML ice cores (Table S5)." | S2, S4, AB, SD |
| KK-81 | supplement p. 5, Figure S3 caption | "between 2.852 to 33.699 kyr BP" | "between 2.852 and 33.699 kyr BP" | AB |
| KK-82 | supplement p. 7, Figure S4 caption | "(3) Antarctica Cold Reveal (ACR), (4) Heindrich Stadial 1 (HS1), and (5) Marine Isotope 3 (MIS3)" | "(3) Antarctic Cold Reversal (ACR), (4) Heinrich Stadial 1 (HS1), and (5) Marine Isotope Stage 3 (MIS3)" | S2, S4, AB |
| KK-83 | supplement p. 10, Figure S5, y axis title | "PAS EDC Contribution and PSA EDML Contribution ( in %)" | "PSA contribution, EDC and EDML (%)" | S4, AB |

#### Verification log

| ID | Check | Checked | Values | Result |
|---|---|---|---|---|
| PP-28 | P13 | Numerical literature statements outside segment 1, l. 238 to 240, l. 288, l. 319 to 323, l. 269 to 271 (S1) | Kok et al. (2021) central values South America ~70 %, Australia ~20 %, southern Africa ~10 % against 70, 18 and 10 %, consistent within rounding (the ± 20 % see KK-40); Delmonte et al. LGM values appear in Table S4; EDML NZ ~6 % matches Table S5 (6.2); shelf areas not checkable (full text not readable) | no finding beyond GB-39, GB-40, GB-43, KK-40 |
| PP-29 | P1 | Eq. 3 and 4 recomputed with Table S3 end-members and Table S1 contributions, per period and per sample (S3) | Modelled 87Sr/86Sr and εNd: Late Holocene 0.7101 / minus 5.22; Early Holocene 0.7102 / minus 4.76; YD 0.7094 / minus 5.39; ACR 0.7082 / minus 2.91; HS1 0.7076 / minus 1.55; LGM 0.7083 / minus 2.62; MIS3 0.7083 / minus 3.37; per-sample Holocene range 0.7060 to 0.7236; the YD sample at 12227 yr BP gives 0.7274 / minus 17.9, matching the yellow point in Figure 2 | no finding beyond GB-38, GB-39 |
| PP-30 | P3 | Figure 2 legend colours against symbols, counts and an outlying point (AB) | Six legend colours match plotted symbols; separate dots 26, 26, 27, 9, 9, 4 per colour, dense field merged; axes 0.700 to 0.730 and εNd 5 to minus 25 calibrated; one YD point at 0.7275 / minus 17.88 next to the SAF end-member (0.7280 / minus 18.61) | no finding beyond GB-38 |
| PP-31 | P3 | Figure 3 medians and quartiles against l. 280 to 295 (AB) | LGM PAT median 65.8 (58.9, 71.7), AUS 10.1 (5.8, 14.0), SAF 4.6, NZ 15.5 (10.8, 18.9), PAP 1.8; SSA ~70 % and AUS ~10 % (l. 281) agree with medians and Table S5 (69.3, 10.2) | no finding beyond GB-42, GB-62 |
| PP-32 | P1, P2, P3 | EDC minus EDML differences for LGM and HS1 (l. 417 to 421) against Table S5, and all 25 bars of Figure 4 measured (S3, AB) | LGM NZ 14.2 minus 6.2 = +8.0, PAT 65.7 minus 73.7 = minus 8.0 (text +8 and "equivalent reduction"); HS1 largest difference 5.3 (SAF; text "not exceeding ~5%"); bars for YD, ACR, HS1, LGM within 0.31 points of Table S5 | no finding beyond GB-51, GB-53 |
| PP-33 | P15 | Each sentence of Section 5 against Section 3 and Table S5 (S4) | Glacial to interglacial shift (PAT 65.7 to 49.0 %, AUS 10.2 to 23.1 %, PAP 3.6 to 11.0 %, SAF 6.3 to 10.7 %) supported; MIS3, LGM, HS1 high-latitude (PAT + NZ 79.4, 79.9, 81.9 %) supported; broad similarity with EDML in HS1 supported | no finding beyond GB-37, GB-55 to GB-58 |
| PP-34 | P4 | Cross-references to figures, sections, equations and supplement items (S4) | Figures 1 to 5 each once; Sections 1 to 5 and 4.1 to 4.4, Eq. 1 to 4 without gaps; "section 4.2" (l. 310) correct; Figure S1, S2, S3, S5, Table S3 and S5 references lead to the stated content | no finding beyond GB-46, GB-50, GB-54, KK-09, KK-74, KK-76, KK-80 |
| PP-35 | P4 | 91 reference entries against all in-text citations (88 author-year keys) in both directions (S4) | 82 keys match exactly; mismatches Gili et al. 2016, Speirs 2001, Quake, Sugden, De Deccker 2010 and 2019; uncited entry Gaiero et al. 2007 (Chemical Geology); two-author and single-author citations correct throughout | no finding beyond GB-48, KK-43, KK-48, KK-56, KK-67, KK-73 |
| PP-36 | P16 | Character and typesetting observations of Sections 4 and 5, declarations, references and captions at the page images (S4) | Confirmed: duplicated phrase l. 384 to 385, RTF codes in 18 entries, "Environùental", "Sudgen", "SUPPLENTARY"; not reported because correct on the page image: Eq. 3 and 4, δ¹⁸O, isotope superscripts, the name hyphen in Lisé-Pronovost, margin numbers inside extracted lines | no finding beyond GB-61 |
| PP-37 | P3 | Whether the YD and ACR sample numbers can be counted in Figure S4 (AB) | YD PAT box 6 separate dots plus whisker ends, ACR 5 dots plus whisker ends; dots on whisker caps and box lines cannot be separated | no finding beyond GB-62 |
| PP-38 | P24 | Zone and band edges in both panels of Figure 5 (AB) | Band 7958 to 11430 yr BP; panel A zones 11710 to 12890, 14680 to 18010, from 28980; panel B 11730 to 13020, 14750 to 17990, from 29000 (±34 yr) | no finding beyond GB-64 |
| PP-39 | P24 | Dated Etosha and Makgadikgadi (Sua) inputs in Figure S3 against l. 392 to 397 (AB) | Etosha raw peaks 5166, 6243, 8703, 10488, 11854 yr BP against "between ~12.2 and ~5.1 kyr BP" (youngest agrees, oldest 0.35 kyr younger); Sua peaks 3462 to 8293 yr BP against "between ~8.2 and 2.8 kyr BP", agreement | no finding |
| PP-40 | P24 | Qualitative statements on Figure S2 (l. 296, 299, 312) and Figure S5 (l. 445 to 447) (AB) | Figure S2A: nssCa2+ flux falls from about 620 at 18.8 kyr to near zero by about 14.7 kyr; S2B: δ18O rises from about 17.5 to 14.5 kyr; S2C: deuterium excess rises from about 10 kyr; Figure S5: both smoothed PAT curves fall between 15 and 14 kyr, EDC only from about 14.4 kyr (rechecked, see GB-37) | no finding beyond GB-24, GB-37 |

## Optional checks

| Area | What it needs | Responsible | Run |
|---|---|---|---|
| DOI resolution | one fetch per reference entry with DOI | `science-quellenapparat-pruefung` | no |
| Citation style | the name of the style | `science-zitierstil-harvard-ctr` or the style rules of the journal | no |
| AI statement against publisher policy | the AI policy of the target publisher | this review, on request | no |
| Relation to the authors' own prior work | the prior works of the authors | this review, on request | no |
| Journal requirements | the author guidelines of the target journal | this review, on request | no |
| Factual accuracy | access to the source of each checked statement | `science-faktenbeleg-pruefung`, `geo-frage-belegbasiert-klaeren` | no |

## Limits of this review

- Reviewed version: egusphere-2025-5046.pdf, 29 pages, SHA-256 f598b53d01e375844cfb549eb05b9a3407bb30cae553e603c125d5f14886c722; supplement egusphere-2025-5046-supplement.pdf, 22 pages, SHA-256 759cfa14195948f5772d3d6d696081932424f4296e51c812415527ed3b108ea6.
- Check instances: the six instances (S1 to S4, AB, SD) ran as separate agents without context of each other; merging, overall assessment and format check ran in a further separate agent. Line numbers follow the printed margin numbers (every fifth line printed), interpolated between them; the supplement has no line numbers and is cited by page and element.
- Sources not readable: Gabrielli et al. (2006) (no abstract found); Delmonte et al. (2008) and Delmonte et al. (2017) (abstracts only); Vanderstraeten et al. (2023) (abstract only; full text blocked); Coppo et al. (2022) (abstract only); Neff and Bertler (2015), Davies et al. (2020), Magee et al. (2004), Delmonte et al. (2004) (abstracts only); Singh and Luly (1991) (not read); Kok et al. (2021), Table 2 (image only); Lambert et al. (2021) (author repository version instead of the publisher version); the original title of the Caldenius (1932) entry. A Zenodo record bearing the manuscript title was not opened because it may belong to a later version.
- Findings with status assumption: 15 of 66.
- Discarded findings: 1 of 294 instance items (92 substantive findings, 110 minor corrections, 44 verification log entries). Discarded was the minor correction AB-KK-15 ("x 1000" in Figure S5): the string exists only in the text layer of supplement p. 10 and is not visible on the page image, so by the rules of this review it is not a finding. No substantive finding lacked a mandatory field or was refuted at verification.
- Merged findings: 27 of 92 substantive findings were merged into others (66 substantive findings result, one of them from a note outside the checklists, origin ZF, GB-26); 26 of 110 minor corrections were merged into others or into a substantive finding (83 minor corrections result, after one discard); 4 of 44 verification log entries were merged (3 into other entries, 1 into this list of unreadable sources), 40 result.
- Contradictions between instances decided at the manuscript: three (GB-15, GB-33, GB-37).
- Measurements in figures were made by instance AB at 300 dpi and are not repeated here; this report rechecked Figure S5 (GB-37), Table S2 rows (GB-26) and Figure S5 labels (discarded item) on the page images and recomputed Table S1 statistics.
- Optional checks run: 0 of 6.
