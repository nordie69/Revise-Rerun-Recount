# Review report: Quantifying Southern Hemisphere dust sources during the Last Glacial-Interglacial Transition using rare earth elements in the EPICA Dome C ice core

| Field | Value |
|---|---|
| Manuscript | Boxho, S., Vanderstraeten, A., Mattielli, N., Laruelle, G. G., Bory, A., Gabrielli, P. and Bonneville, S. (2025) Quantifying Southern Hemisphere dust sources during the Last Glacial-Interglacial Transition using rare earth elements in the EPICA Dome C ice core. EGUsphere preprint egusphere-2025-5046, https://doi.org/10.5194/egusphere-2025-5046 |
| Checked version | egusphere-2025-5046.pdf, 29 pages, SHA-256 f598b53d01e375844cfb549eb05b9a3407bb30cae553e603c125d5f14886c722; supplement egusphere-2025-5046-supplement.pdf, 22 pages, SHA-256 759cfa14195948f5772d3d6d696081932424f4296e51c812415527ed3b108ea6 |
| Date | 2026-10-18 |
| Language | English |
| Review instances | Segments 1 to 4, figures, study design; the six review instances ran as separate agents; no instance dropped |
| Note | The review instances ran as separate agents. Line numbers are the printed margin numbers of the main manuscript; the supplement has no line numbers and is cited by page, table, row and column. All calculations were run in Python on the values of Supplementary Tables S1, S2, S4 and S5. |

## Summary

The manuscript is a modelling study that applies an existing statistical unmixing algorithm (DEPOT, Vanderstraeten et al., 2023; non-negative least squares with the MATLAB function lsqnonneg) to a published rare earth element (REE) dataset of the EPICA Dome C (EDC) ice core (Gabrielli et al., 2010). Of 294 dust samples, 279 with complete data are described by 13 REE (Gd removed), corrected for partial acid leaching and normalised to the upper continental crust; each is fitted as a non-negative combination of 217 REE patterns from seven potential source areas (Patagonia PAT, Central Western Argentina CWA, Puna-Altiplano PAP, southern Africa SAF, Australia AUS, New Zealand NZ, Antarctica ANT). 2000 Monte Carlo runs per sample give median contributions, and a fit threshold of R ≥ 0.67 retains 241 samples from 33.7 to 2.9 kyr BP. Patagonia supplies about 65 to 75 % of the dust in MIS3, the LGM and HS1 and 49 % in the Holocene, when Australia (23 %), the Puna-Altiplano (11 %) and southern Africa (11 %) gain weight. The model output is compared with published Sr-Nd isotope data through a concentration-weighted mixing calculation (Eq. 3 and 4) and, period by period, with the authors' EDML record; the shift is attributed to the submersion of the Patagonian shelf and the reorganisation of Patagonian rivers around 14.5 kyr BP.

## Strengths

1. Per-sample results are published: Table S1 lists the PSA medians and R for all 241 retained samples, and recomputing from it reproduces every EDC period mean of Table S5 to 0.1 percentage points and the mean R of 0.852 given in the text (PP-26, PP-27). A reader can therefore check and recompute every period statistic of the paper, which is how most numerical findings of this review could be verified (for example GB-25, GB-56, GB-57).
2. Sample selection is documented as a closed balance: 294 published patterns, 15 removed for missing elements, 279 modelled, 38 below the fit threshold, 241 retained, together with the sampling gap from 21.7 to 27.3 kyr BP with four samples (PP-15, PP-16). The data basis of each period mean is thus known, and the limits of the record are disclosed by the authors themselves.
3. The REE apportionment is confronted with an independent tracer through explicit mixing equations (Eq. 3 and 4) and tabulated end-member values (Table S3), and the measured glacial isotope values, including the two EDC LGM values, are plotted at the positions of Table S4 (PP-38). The glacial part of this comparison is reproducible; its reach for the Holocene is limited (GB-43).
4. The same algorithm family is applied to a second core, and the differences are given per period and source area (Figure 4, Table S5); the bars for LGM, HS1, ACR and YD agree with Table S5 within about 0.5 points (PP-43). Site differences are therefore quantified rather than only described, which makes the discrepancies in GB-07, GB-56 and GB-57 detectable at all.

## Weaknesses

1. Timing and cause of the provenance shift are not established by the EDC data: the high-latitude share stays at glacial values until about 13.2 kyr BP, the shift "at ~14.5 kyr BP" appears to be taken from EDML, absolute fluxes per source area are announced but not shown, and Discussion and Conclusion turn a temporal coincidence into a demonstrated cause (GB-02, GB-03, GB-59). Suggestion: determine the onset in EDC by a change-point analysis with Monte Carlo uncertainty, report absolute PSA fluxes, and phrase the shelf and river mechanism as a hypothesis unless the fluxes discriminate it.
2. The validation against Sr-Nd isotopes (aim 2) uses two EDC values, all from the LGM, and for the Holocene only Taylor Glacier and Berkner Island data, with no measure of agreement; the cited EDC Holocene values have no traceable source (GB-43, GB-41, GB-42). Suggestion: compare per sample with EDC or Dome C measurements of matching age, define a residual measure against measurement uncertainty, and show that an alternative mixture would fail it.
3. Whether the unmixing identifies source areas is untested and, with the material provided, untestable: 13 equations against 217 end-members, Antarctic end-member patterns unlike all others, a fit filter that removes noisy Holocene samples while the remaining Holocene scatter is read as climate, a threshold that does not match its stated significance, no reported Monte Carlo spread, and neither inputs nor code (GB-18, GB-28, GB-29, GB-25, GB-23, GB-13, GB-11). Suggestion: add a recovery test with synthetic mixtures, per-sample uncertainty, the corrected threshold, the input concentrations and correction factors, and the code with a persistent identifier.
4. The EDC and EDML comparison (aim 4) rests on EDML values that contradict the manuscript's own summary of the published record and were produced with an earlier model configuration, and several of its numbers compare different time windows or are swapped (GB-07, GB-22, GB-57, GB-56). Suggestion: recompute EDML with the present configuration, state the origin of the EDML values in Table S5, and base all differences on the common window 7.5 to 27 kyr BP.

## Findings by segment

### Segment 1: Abstract, introduction, state of research (pp. 1 to 3)

#### Substantive findings

**GB-01 The priority claims rest on no documented search and are not qualified by the gaps that the manuscript itself discloses.**

| Field | Content |
|---|---|
| Check | P28, P15 |
| Location | p. 1, l. 17 to 20; p. 3, l. 74 to 75; p. 7, l. 220; p. 12, l. 403; p. 14, l. 472 to 473; compare p. 4, l. 110 to 113 and p. 6, l. 174 to 175 |
| Quotation | "Using a statistical unmixing algorithm on 241 samples, we quantify for the first-time"; "This study presents the first high-resolution, continuous and quantitative reconstruction of dust" |
| Concern | The narrower claim, a first continuous REE-based apportionment at EDC, is plausible, and the manuscript discloses its sampling limits in the Methods. Two points are not carried through. (a) No database, search terms or date of a literature search are given for any of the five priority statements (l. 19 to 20, l. 74 to 75, l. 220, l. 403, l. 472). The abstract version is the broadest: it claims to quantify "for the first-time" the contributions of key Southern Hemisphere sources, without "continuous" or "at EDC", although the manuscript itself reports earlier quantitative estimates for East Antarctic dust, by Coppo et al. (2022) for the LGM (64 % SSA, 15 % Antarctica, 11 % AUS, 5 % SAF, 5 % NZ; l. 278 to 279) and for the Holocene (l. 324 to 328), and model apportionments by Kok et al. (2021) and Krätschmer et al. (2022) (l. 275 to 277, l. 319 to 323). (b) "Continuous" and "high-resolution" are repeated in the Conclusion without the limits disclosed in Methods and Results: a sampling gap from 21.7 to 27.3 kyr BP with four samples (l. 113) and 38 excluded samples, all younger than 14 kyr BP (l. 174 to 175). Computed from Table S1, the largest spacings between retained samples are 2280 yr (23104 to 25384 yr BP) and 1785 yr (25640 to 27425 yr BP), and the mean spacing is 128.5 yr, against "approximately 100 years" in l. 110, which refers to the 294 original samples. |
| Suggestion | In l. 19 to 20 write "we provide the first continuous, quantitative REE-based record of dust source contributions at EDC" ("first time" without hyphen). In l. 74 to 75, l. 220 and l. 403 either name the search (databases, terms, date) or write "to our knowledge". After l. 76 cite the earlier quantitative estimates and state what the continuous REE record adds. In l. 17, l. 220 and l. 472 qualify "continuous", for example "quasi-continuous (mean sample spacing about 130 yr, with a sampling gap between 21.7 and 27.3 kyr BP)". |
| Status | verified (absence of a search description; wording; disclosures in l. 113 and l. 174 to 175; values in l. 278 to 279); inferred (spacings computed from Table S1) |
| Severity | moderate |
| Source | S1, S4 |

**GB-02 The EDC data do not show the provenance shift at about 14.5 kyr BP that Abstract, Section 4.1 and Conclusion report; the high-latitude share stays at glacial values until about 13.2 kyr BP.**

| Field | Content |
|---|---|
| Check | P15, P17, P2 |
| Location | p. 1, l. 23 to 24; p. 6, l. 203 to 204; p. 7, l. 225 and l. 233 to 236; p. 13, l. 445 to 447; p. 14, l. 477 to 480; compare p. 12, l. 407 to 409; Supplement Table S1 (page 13), rows 13032 to 14601; Supplement Table S5 (page 22), rows MIS3 to ACR |
| Quotation | "Our calculations highlight a major shift in dust provenance occurred at the onset of the ACR, marking a"; "onward, a marked reorganization in dust provenance occurred, characterized by a relative decline in" |
| Concern | The manuscript rightly calls the ACR and YD results "tentative" because they rest on few samples (l. 407 to 409), but this caveat stands only in the EDML comparison and is not carried to the timing statements. The samples that exist do not show a shift at 14.5 kyr BP. High-latitude share (PAT plus NZ) as the mean of the Table S1 rows: MIS3 79.4 %, LGM 79.9 %, HS1 81.9 %, ACR 75.5 %. The six ACR samples from 13412 to 14601 yr BP average 80.1 % (PAT 76.0 %), the glacial level; the ACR mean is lowered only by the two youngest ACR samples, 13143 yr BP (68.7 %) and 13032 yr BP (54.8 %). A Mann-Whitney test of the per-sample high-latitude shares gives p = 0.14 for ACR against HS1 and p = 0.27 for ACR against the LGM; "significantly increased contributions" (l. 235) is not backed by a test. AUS, named among the sources that rise at the onset of the ACR (l. 235) and said to have "rose after 14.7 kyr BP, reaching 11% during the ACR" (l. 203 to 204), is 11.3 % in HS1 and 11.1 % in the ACR (Table S5); the low-latitude increase from HS1 to ACR (AUS plus SAF plus PAP, 18.2 to 24.3 %) comes from SAF (4.9 to 8.0) and PAP (2.0 to 5.2) only. The EDC decline between 15 and 14 kyr BP cited in l. 445 to 446 exists (PAT 83.2 % for 15 to 16 kyr BP, 72.0 % for 14 to 15 kyr BP), but it returns PAT from a late HS1 maximum to the LGM and HS1 level (65.7 %, 74.8 %), not below it. The finding is major because the attribution to Meltwater Pulse 1A and shelf submersion in Abstract and Conclusion (l. 29 to 31, l. 450 to 454, l. 477 to 482) rests on this timing. Does the 14.5 kyr BP date come from the EDML record (Vanderstraeten et al., 2023) or from the moving average over 9 samples in Figure 1 and Figure S5, which at the mean spacing of 128.5 yr spans about 1.2 kyr? |
| Suggestion | Determine the onset of the change in EDC from the unsmoothed samples with the Monte Carlo uncertainty of each sample, for example by a change-point analysis, and report it separately from the EDML timing in Section 4.1 (l. 233 to 236) and Section 4.4 (l. 445 to 452). Move the sample-number caveat to Section 3, where the interval means are introduced. In l. 203 to 204 write that AUS stays at about 11 % in the ACR and rises in the YD (14.5 %) and the Holocene (23.1 %), and remove AUS from the sources that increase at the ACR onset in l. 235. Align Abstract l. 23 to 24 and Conclusion l. 477 to 480 with the result, and if the EDC onset is later than 14.5 kyr BP, discuss what this means for the link to Meltwater Pulse 1A. |
| Status | verified (wording and location of the caveat; Table S1 and Table S5 values on the page images); inferred (means, test results and onset computed from Table S1); assumption (origin of the 14.5 kyr BP date, asked as a question) |
| Severity | major |
| Source | S4, SD, S3 |

**GB-03 Absolute dust fluxes per source area are announced but not shown, so the attribution of the shift to shelf submersion cannot separate a Patagonian decline from a low-latitude increase.**

| Field | Content |
|---|---|
| Check | P10, P11, P4, P3 |
| Location | p. 1, l. 29 to 31; p. 5, l. 165 to 167; p. 6, l. 183 to 184; p. 13, l. 448 to 450; p. 13, l. 450 to p. 14, l. 470; Figure 1 (page 24); Supplement Figure S2 (page 4); Supplement Figure S5 (page 10) |
| Quotation | "to convert PSA contributions into absolute dust fluxes (Figure S2)."; "Figure 1 and Table S1 summarize the relative contributions (in % of total"; "We attribute the shift in provenance" |
| Concern | Shelf flooding and drainage reversal predict a fall of the absolute Patagonian flux, whereas a relative fall of PAT can also arise from rising low-latitude inputs, which l. 462 to 466 itself allows ("relative increase in dust input from lower-latitude source regions"). The Methods announce the conversion of PSA contributions into absolute fluxes with the nssCa2+ flux (l. 165 to 167), and l. 183 to 184 says that Figure 1 and Table S1 give contributions "in % of total deposition and flux". No absolute flux per PSA appears anywhere: Figure 1 (all five y axes "Total Contribution (%)"), Table S1 and Table S5 give percentages only, and Figure S2 shows the total nssCa2+ flux (A), δ18O (B) and deuterium excess (C) of EDC. The statement in l. 448 to 450 that total deposition declined "in both cores (Figures S2 and S5)" is shown for EDC only: Figure S5 shows relative contributions in EDC and EDML, and no figure or table shows the EDML dust flux. The shift also coincides with several events that the manuscript lists itself (AID6, onset of the Bølling, Meltwater Pulse 1A; l. 450 to 452), so timing alone cannot single out sea level, and the iron fertilisation framework that motivates PSA-specific emissions (l. 37 to 52) is not taken up with any flux result (see GB-62). The design therefore answers aim (1) descriptively but cannot carry the causal attribution in the Abstract (l. 29 to 31); the finding is major because this attribution is one of the main conclusions. |
| Suggestion | Add the absolute flux per PSA with Monte Carlo uncertainty, per sample and per period (a panel in Figure 1 or a supplement table), test whether the PAT flux falls at the time of shelf submersion while the other fluxes stay constant, and derive for each candidate cause (sea level, river reorganisation, transport change) a prediction that differs in absolute fluxes or timing. Cite the EDML dust flux record used in l. 449 to 450 or restrict the statement to EDC. Otherwise delete "and flux" in l. 184 and the conversion in l. 166 to 167, and reword l. 29 to 31 and Section 4.4 as a hypothesis consistent with the data. |
| Status | verified (content of Figure 1, Figure S2, Figure S5, Table S1 and Table S5 on the page images); inferred (that the design cannot carry the causal statement) |
| Severity | major |
| Source | SD, S3, S4, AB |

**GB-04 Two attributions in the introduction do not match the cited sources: an ice-core finding is credited to a marine sediment study, and the upper half of the CO2 range is not in the cited model studies.**

| Field | Content |
|---|---|
| Check | P13 |
| Location | p. 2, l. 36 to 42 |
| Quotation | "Over recent decades, studies on these ice cores have"; "modelled to have lowered the atmospheric pCO2 by ~20 to 40 ppmv, accounting for a significant portion" |
| Concern | The paragraph frames dust as a driver of iron fertilisation correctly, but two attributions do not hold. (a) Martínez-García et al. (2014), cited for what "studies on these ice cores have revealed", is a marine sediment study: its abstract describes foraminifera-bound nitrogen isotopes, iron burial and productivity proxies from a Subantarctic Atlantic sediment core. (b) Neither cited model study gives values up to 40 ppmv. Lambert et al. (2015) give less than 10 ppm on centennial and a further about 10 ppm on millennial timescales, and about 20 ppm for the LGM in their conclusions; Lambert et al. (2021) give "between 12 and 29 ppmv" for global-scale iron fertilisation, and their only 40 ppmv figure refers to ocean stratification. The cited range is therefore about 12 to 29 ppmv. The value does not change the results, but a reader who checks the cited sources cannot find it, which makes the finding a matter of traceability (moderate). |
| Suggestion | In l. 36 to 40 attribute the link between dust, export productivity and fertilisation to marine sediment records (Martínez-García et al., 2014) together with the ice-core dust records, or cite an ice-core study for the ice-core part. In l. 41 replace "~20 to 40 ppmv" by "~10 to 30 ppmv (about 20 ppm in Lambert et al., 2015; 12 to 29 ppmv in Lambert et al., 2021)", or cite the source of the 40 ppmv value. |
| Status | verified (abstract of Martínez-García et al., 2014; full text of Lambert et al., 2015; author version of Lambert et al., 2021; read by instance S1) |
| Severity | moderate |
| Source | S1 |

**GB-05 The role of the Southern Hemisphere westerlies is referenced to a regional downscaling study of southern African LGM climate.**

| Field | Content |
|---|---|
| Check | P13 |
| Location | p. 2, l. 51 to 52 |
| Quotation | "winds, which play a crucial role in atmospheric and oceanic circulation (Engelbrecht et al., 2019)." |
| Concern | Engelbrecht et al. (2019) downscale eight LGM climate simulations over southern Africa to 8 km and report regional temperature and rainfall changes. Their abstract mentions frontal rainfall reaching farther north, but not the Southern Hemisphere westerlies or their role in atmospheric and oceanic circulation. The general statement in l. 51 to 52 is therefore at most indirectly supported by this source. |
| Suggestion | In l. 52 cite a work that addresses the westerlies and their role in atmospheric and oceanic circulation (for example a review of Southern Hemisphere westerly wind changes), or restrict the reference to Engelbrecht et al. (2019) to a statement about southern African LGM climate. |
| Status | verified (abstract, asu.elsevierpure.com record, read by instance S1 and again in the merge); inferred (full text not readable) |
| Severity | minor |
| Source | S1 |

**GB-06 The study that produced the dataset already reported the deglacial change in EDC dust composition, but the manuscript credits the shift to later work.**

| Field | Content |
|---|---|
| Check | P13 |
| Location | p. 3, l. 72 to 74; p. 7, l. 236; compare p. 18, l. 615 to 618 |
| Quotation | "Gabrielli et al., 2010; Wegner et al., 2012) achieved multi-decadal resolution but could not fully resolve"; "This shift already describes by Gili et al. (2022) and Vanderstraeten et al. (2023), appears" |
| Concern | The description of Gabrielli et al. (2010) in l. 72 to 74 is accurate for the source attribution: the authors write that their REE results do not allow the exclusion of any major Southern Hemisphere source. It leaves out that the same paper, on the same samples, already reported the change that the manuscript presents as its main result; its title in the reference list reads "A major glacial-interglacial change in aeolian dust composition inferred from Rare Earth Elements in Antarctic ice" (l. 616 to 617), and its text dates the change to about 15 kyr BP with a variable Holocene composition. In l. 236 the shift is credited only to Gili et al. (2022) and Vanderstraeten et al. (2023), and the sentence is ungrammatical ("already describes by"). |
| Suggestion | In l. 72 to 74 and l. 236 state that Gabrielli et al. (2010) identified the change in REE composition from about 15 kyr BP and the variable Holocene composition in this dataset, and that the present study adds the quantitative attribution; write "This shift, already described by Gabrielli et al. (2010), Gili et al. (2022) and Vanderstraeten et al. (2023), appears". |
| Status | verified (title in the reference list; author copy of Gabrielli et al., 2010, read by instance S1) |
| Severity | minor |
| Source | S1, S4 |

**GB-07 The EDML values used for the EDC and EDML comparison contradict the manuscript's own summary of the EDML record and are not labelled as recalculated.**

| Field | Content |
|---|---|
| Check | P13, P37 |
| Location | p. 3, l. 78 to 81; p. 1, l. 27 to 29; p. 9, l. 288; p. 13, l. 417 to 424; Supplement Table S5 (page 22), EDML block, rows LGM to Early Holocene, columns PAT, SAF, AUS, NZ; Figure 4 (page 28); Supplement Figure S5 (page 10) |
| Quotation | "of Patagonian dust, up until ~14.5 kyr BP when a sudden drop in Patagonian contribution (below 50%"; "PAT dust (-14%) but higher contributions of Australian dust (+12%) than EDML." |
| Concern | The introduction summarises the EDML record as a drop of the Patagonian contribution below 50 % on average after about 14.5 kyr BP (l. 79 to 81). Table S5, whose EDML block feeds Figure 4, Figure S5 and the differences in l. 417 to 424, gives EDML PAT after 14.5 kyr BP as 62.5 % (ACR), 58.4 % (YD) and 62.7 % (Early Holocene), none below 50 %. The abstract of Vanderstraeten et al. (2023), read by instances S1 and SD, also differs from Table S5 in the other sources: after 14.5 kyr BP SAF 21 to 23 % and AUS 13 to 21 % (Table S5: SAF 12.4, 8.2, 11.2), Patagonia still "at ~50 % on average" in the Early Holocene; before 14.5 kyr BP Patagonia about 68 %, Australia 14 to 15 % and New Zealand about 3 to 4 % (Table S5: PAT 73.7 and 71.6, AUS 9.7 and 9.4, NZ 6.2 and 6.5; l. 288 cites the 6 % as the result of the "previous EDML ice core work"). The comparison depends on these values: the Holocene PAT difference of l. 424 ("-14%") follows from 49.0 minus 62.7 = minus 13.7; with an EDML Early Holocene PAT of about 50 % it becomes about minus 1 (whole EDC Holocene) or about minus 3 (EDC Early Holocene, 47.1 %). The abstract statement that EDML shows more consistent inputs from southern Africa (l. 28 to 29) agrees with Table S5 in four of five periods but not in the YD (EDC 14.6 %, EDML 8.2 %). A possible explanation is that EDML was recalculated with the present configuration (13 REE, 217 patterns; see GB-22); the manuscript does not say so. The finding is major because aim (4) (l. 95 to 98) and the abstract statement on regional differences rest on these differences. |
| Suggestion | State in Section 2 and in the captions of Table S5, Figure 4 and Figure S5 how the EDML values were obtained (source, model version, recalculation). If EDML was recalculated, report the recalculated EDML record as a new result, give its differences to Vanderstraeten et al. (2023), and revise l. 78 to 81 and l. 288 accordingly. If not, replace the EDML block of Table S5 by the published values and recompute Figure 4, l. 417 to 424 and the abstract sentence in l. 27 to 29. |
| Status | verified (l. 79 to 81 against Table S5 on the page image; abstract of Vanderstraeten et al., 2023, read by instances S1 and SD); inferred (differences computed from Table S5); assumption (recalculation as explanation) |
| Severity | major |
| Source | S1, SD |

**GB-08 Three works that precede or qualify the EDC provenance result are not cited.**

| Field | Content |
|---|---|
| Check | P14 |
| Location | p. 3, l. 88 to 98; p. 10, l. 329 to 334; Supplement Table S4 (page 21), column Reference |
| Quotation | "ice core (Gabrielli et al., 2010) to provide a high-resolution quantitative and continuous reconstruction"; "4.2), our results do not indicate significant Antarctic contributions to EDC. This is consistent with the" |
| Concern | Contribution in one sentence: a continuous, quantitative REE-based apportionment of EDC dust provenance from 33.7 to 2.9 kyr BP, checked against Sr-Nd data and compared with EDML. Three works that bear directly on it are not in the reference list. (1) Aarons, S.M., Aciego, S.M., Arendt, C.A., Blakowski, M.A., Steigmeyer, A., Gabrielli, P., Sierra-Hernandez, M.R., Beaudon, E., Delmonte, B., Baccolo, G., May, N.W., Pratt, K.A., 2017. Dust composition changes from Taylor Glacier (East Antarctica) during the last glacial-interglacial transition: A multi-proxy approach. Quaternary Science Reviews 162, 60-71. https://doi.org/10.1016/j.quascirev.2017.03.011. It combines REE patterns with Sr-Nd isotopes across the same transition, places the shift between 15.3 and 14.5 kyr BP and attributes early Holocene dust to South American and local Ross Sea sector sources, which qualifies the statement that Antarctic sources are insignificant (l. 330); its isotope data are used in Table S4 but the work is neither discussed nor listed (see also GB-54). (2) Vallelonga, P., Gabrielli, P., Balliana, E., Wegner, A., Delmonte, B., Turetta, C., Burton, G., Vanhaecke, F., Rosman, K.J.R., Hong, S., Boutron, C.F., Cescon, P., Barbante, C., 2010. Lead isotopic compositions in the EPICA Dome C ice core and Southern Hemisphere Potential Source Areas. Quaternary Science Reviews 29, 247-255. https://doi.org/10.1016/j.quascirev.2009.06.019. A provenance study on EDC itself; it finds Australian dust not to be the main component (66 of 74 samples away from the Australian field) and samples with more than 50 % local Antarctic dust, mostly in interglacials; both points bear on the Holocene AUS share and the zero ANT share here. (3) Marino, F., Castellano, E., Ceccato, D., De Deckker, P., Delmonte, B., Ghermandi, G., Maggi, V., Petit, J.R., Revel-Rolland, M., Udisti, R., 2008. Defining the geochemical composition of the EPICA Dome C ice core dust during the last glacial-interglacial cycle. Geochemistry, Geophysics, Geosystems 9, Q10018. https://doi.org/10.1029/2008GC002023. It found at EDC a homogeneous glacial composition matching southern South America and a more variable Holocene composition with an additional, likely Australian, source: the qualitative form of the present result at the same site. Only Marino et al. (2009) is cited. |
| Suggestion | Cite and discuss the three works in the introduction (after l. 87) and in Sections 4.1 and 4.3 (l. 236 to 242, l. 329 to 334), and add Aarons et al. (2017) to the reference list in any case, since Table S4 uses its data. |
| Status | verified (author copies of Aarons et al., 2017, and Vallelonga et al., 2010, abstract of Marino et al., 2008, read by instance S1; reference list pp. 16 to 22 checked) |
| Severity | moderate |
| Source | S1 |

**GB-09 The time span of the record is given with three end points and two start points.**

| Field | Content |
|---|---|
| Check | P2 |
| Location | p. 3, l. 90 to 91; p. 9, l. 303 to 304; compare p. 1, l. 18; p. 4, l. 109 to 110; p. 6, l. 182 and l. 187; p. 25, l. 851 |
| Quotation | "during the LGIT from 33.6 kyr to"; "BP until 2.7 kyr BP)." |
| Concern | Table S1 runs from 2852 to 33699 yr BP, which the Abstract (l. 18) and l. 182 render as 33.7 to 2.9 kyr BP and the Methods (l. 109 to 110) and the caption of Figure 1 (l. 851) as 2852 to 33699 yr BP. The introduction gives 33.6 to 2.8 kyr BP (l. 90 to 91; 33699 yr does not round to 33.6 kyr), and Section 4.2 gives 2.7 kyr BP as the end of the record (l. 304; 2852 yr does not round to 2.7 kyr). The Holocene is defined as ending at 2.8 kyr BP (l. 187). Three end values and two start values are thus in use for one record. |
| Suggestion | Use one rounding throughout: in l. 90 to 91 write "from 33.7 to 2.9 kyr BP", in l. 304 "until 2.9 kyr BP", and state in l. 187 that the Holocene average ends at the youngest sample (2852 yr BP). |
| Status | verified |
| Severity | minor |
| Source | S3, S1, SD |

**GB-10 The core term LGIT is used for three different time spans.**

| Field | Content |
|---|---|
| Check | P15 |
| Location | p. 3, l. 90 to 91; p. 7, l. 221; p. 9, l. 301 to 302; p. 12, l. 397; title, p. 1 |
| Quotation | "during the LGIT from 33.6 kyr to"; "provenance pattern until the onset of the LGIT"; "coinciding roughly with dry periods of the lake during the LGIT" |
| Concern | In l. 90 to 91 and l. 221 ("spanning the entire LGIT") the LGIT covers the whole record from MIS3 to the late Holocene. In l. 302 it begins after the stable glacial period, at about 14.5 kyr BP. In l. 397 it includes a dry period at 5.5 to 4.0 kyr BP. The term of the title and of three of the four aims therefore has no fixed meaning, and "until the onset of the LGIT" contradicts the definition in l. 90. |
| Suggestion | Define the LGIT once in Section 1 with its age limits and use it only in that sense; for the whole record use "the last 34 kyr" or "MIS3 to the late Holocene", and rephrase l. 302 as "until ~14.5 kyr BP". |
| Status | verified |
| Severity | minor |
| Source | S4 |

#### Minor corrections

| ID | Location | Quotation | Replacement | Source |
|---|---|---|---|---|
| KK-01 | p. 1, l. 15 | "Dust deposits in ice cores provides" | "Dust deposits in ice cores provide" | S1 |
| KK-02 | p. 1, l. 20 | "During the Marine isotope 3 (MIS3)" | "During Marine Isotope Stage 3 (MIS3)" | S1, S2 |
| KK-03 | p. 1, l. 27 | "Comparison with the EDML ice core" | "Comparison with the EPICA Dronning Maud Land (EDML) ice core" (first use; the abbreviation is not expanded elsewhere) | S2 |
| KK-04 | p. 2, l. 39 | "High Nutrients Low Chlorophyll (HNLC)" | "High-Nutrient, Low-Chlorophyll (HNLC)" | S1 |
| KK-05 | p. 2, l. 40 | "Enhanced iron delivery by atmospheric dust during glacial periods are" | "Enhanced iron delivery by atmospheric dust during glacial periods is" | S1 |
| KK-06 | p. 2, l. 48 to 49 | "Shi et al., 2009, Shi et al. 2011, Shi et al." | "Shi et al., 2009, 2011, 2015" | S1 |
| KK-07 | p. 2, l. 55 to 56 | "essential to the process of source identification, these PSAs serve as end-" | "essential to the process of source identification; these PSAs serve as end-" | S1 |
| KK-08 | p. 2, l. 62 | "high altitude site such as EDC where dust fluxes is low" | "high-altitude sites such as EDC, where dust fluxes are low" | S1 |
| KK-09 | p. 3, l. 71 | "information than REE ratio." | "information than REE ratios." | S1 |
| KK-10 | p. 3, l. 88 | "Here, we applied our ‘DEPOT’ model - to the REE pattern dataset measured - in the EPICA Dome C" | "Here, we apply our DEPOT model to the REE pattern dataset measured in the EPICA Dome C" | S1 |
| KK-11 | p. 3, l. 90 | "in the Indian Ocean sector of the East Antarctica" | "in the Indian Ocean sector of East Antarctica" | S1 |

#### Verification log

| ID | Check | Checked | Values | Result |
|---|---|---|---|---|
| PP-01 | P2 | Abstract against Results and tables | 241 samples (l. 19, l. 179, rows of Table S1); 33.7 to 2.9 kyr BP (l. 18, l. 182); PAT about 65 to 75 % in MIS3, LGM, HS1 (Table S5: 70.3, 65.7, 74.8); Holocene PAT about 49 % (49.0) | no finding; the introduction values see GB-09 |
| PP-02 | P28 | Gap and priority claims: l. 19 to 20 ("first-time"), l. 74 to 75 ("first quantitative apportionment algorithm"), l. 91 to 93 ("no consensus"), l. 220, l. 403 ("The only"), l. 472 | No database, search terms, period or date anywhere in the manuscript. "No consensus" on Holocene sources (l. 92 to 93) is consistent with Gabrielli et al. (2010), Marino et al. (2008) and Aarons et al. (2017), as read by instance S1 | GB-01 for l. 19 to 20, 74 to 75, 220, 403, 472; no finding for l. 91 to 93 |
| PP-03 | P13 | p. 2, l. 34 to 36 and l. 44 to 46: Lambert et al. (2008) as source for ice-core dust records and for source location and residence time as controls of deposition | Lambert et al. (2008): sources and lifetime of dust are the main factors of the high glacial dust input; average glacial increase of dust flux by a factor of about 25 | no finding |
| PP-04 | P10 | Gaps named in the introduction against the aims | Gap "limited knowledge of dust emissions from specific Potential Source Areas" (l. 43 to 44): no aim on fluxes; limits of isotopes (l. 59 to 68): basis of the method choice; Holocene without consensus (l. 92): aim (1); spatial variability implied by EDML: aim (4) | GB-03 for the flux gap; otherwise no finding |
| PP-05 | P13 | p. 2, l. 62 to 63: "up to 25 times lower than LGM fluxes" with Delmonte et al. (2008, 2017) | Abstracts of both Delmonte papers contain no flux factor; full texts not openly accessible. Lambert et al. (2008), already in the list, gives an average glacial to interglacial factor of about 25 | no finding; limit: the two Delmonte full texts were not read |
| PP-06 | P18 | Principles the manuscript states for other methods, applied to itself (l. 64 to 71) | Argument that overlapping isotopic fields hamper discrimination (l. 64 to 65) and that REE patterns carry more discriminative information (l. 70 to 71) is not applied to the REE end-members; the data completeness statement (l. 494 to 495) | covered by GB-18 and GB-30 |
| PP-07 | P13 | p. 3, l. 72 to 73; p. 4, l. 108 to 124: description of the Gabrielli et al. (2010) data and correction basis | 294 samples; 2.9 to 33.7 kyr BP; spacing about 60 years (Holocene) and 140 years (glacial); gap 21.7 to 27.3 kyr BP with four samples; dissolved mass fractions about 0.55 (LREE), 0.50 (MREE), 0.40 (HREE), no correction applied in that paper | no finding beyond GB-06; the correction factors come from Vanderstraeten et al. (2023), as l. 119 and l. 124 state |
| PP-08 | P13 | p. 3, l. 77 to 87: summary of Vanderstraeten et al. (2023) | Abstract: Patagonia about 68 % before 14.5 kyr BP, below 50 % on average afterwards; SAF 21 to 23 %, AUS 13 to 21 %, PAP 4 to 10 % after 14.5 kyr BP; highly variable early Holocene; link to shelf submergence and river hydrology | no finding for l. 77 to 87; the mismatch with Table S5 is GB-07 |
| PP-09 | P14 | Search for works that precede, qualify or contradict the contribution | Five queries on Aarons et al. (2017), Vallelonga et al. (2010), REE source apportionment in Antarctic ice, Marino et al. (2008), Davies et al. (2020). Check against the reference list: Gili et al. (2022), Revel-Rolland et al. (2006), Coppo et al. (2022), Paleari et al. (2019), Delmonte et al. (2020), Marino et al. (2009), Vallelonga et al. (2002) are listed and drop out; Aarons et al. (2017), Vallelonga et al. (2010), Marino et al. (2008) are not listed. Results pointing to this manuscript or its later versions were not opened | three proposals, GB-08 |
| PP-10 | P10 | Design of the study (whole manuscript) | Type: modelling, application of an existing algorithm with modified settings (13 instead of 14 REE, 217 patterns). Data: 294 EDC samples (Gabrielli et al., 2010), 15 removed, 279 modelled, 241 retained; PSA database of 217 patterns, 6 of them new. Comparison: Sr-Nd isotopes measured in ice (Table S4); EDML record (Vanderstraeten et al., 2023); model studies. Aims (1) to (4) in l. 91 to 98; no separate hypotheses; the shelf and river hypothesis of the EDML study is carried into Section 4.4 | basis for GB-18, GB-22, GB-29, GB-43; no finding of its own |
| PP-11 | P15 | Aims and core terms of the introduction in Discussion and Conclusion | Aim (1) record: Conclusion l. 472. Aim (2) Sr-Nd validation: Section 4.1, not in the Conclusion. Aim (3) climatic changes: Sections 4.2, 4.3, Conclusion l. 477 to 482 and l. 488 to 490. Aim (4) EDML: Section 4.4, Conclusion l. 484 to 487. Iron fertilisation (l. 37 to 51) not resumed; Southern Hemisphere westerlies (l. 51 to 52) resumed in Sections 4.3 and 4.4 | GB-60, GB-62, GB-10; no finding for aims (1), (3) and (4) |

### Segment 2: Material, methods, appendix (pp. 3 to 5)

#### Substantive findings

**GB-11 Neither the code of the DEPOT algorithm and its Monte Carlo propagation nor the software settings are available, although the statement carries "CODE" in its heading.**

| Field | Content |
|---|---|
| Check | P12, P35 |
| Location | p. 3, l. 100; p. 5, l. 139 to 140 and l. 153 to 165; p. 16, l. 494 to 496 |
| Quotation | "implemented using the lsqnonneg function in MATLAB."; "CODE/DATA AVAILABILITY. All data needed to evaluate the conclusions in the paper are present" |
| Concern | The methods name a self-developed algorithm (l. 100), its MATLAB implementation (l. 140) and a Monte Carlo routine with 2000 runs per sample, normal sampling of the correction factors and concentrations and aggregation of the resulting distributions by PSA (l. 153 to 165). The availability statement addresses only data; it gives no repository for the code, no reason for withholding it and no pointer to a release with Vanderstraeten et al. (2023). MATLAB version, solver tolerance, random number generator and seed are also not given; in a system with 13 equations and 217 unknowns (GB-18) they can influence which dust sources enter the solution and how reproducible the medians are. |
| Suggestion | State in l. 494 to 496 where the DEPOT and Monte Carlo code in the version used here (13 REE, 217 patterns) can be obtained, with a persistent identifier, or why it is withheld; add MATLAB version, solver options and seed to Section 2. |
| Status | verified (absence in the statement, the main text and the supplement); whether the code was released with Vanderstraeten et al. (2023) was not checked (repository record not reachable) |
| Severity | moderate |
| Source | S2, SD |

**GB-12 Six end-member patterns are new data without a methods description, and the size fractions of the database differ strongly between source areas.**

| Field | Content |
|---|---|
| Check | P12, P19 |
| Location | p. 4, l. 104 to 105 and l. 126 to 135; p. 16, l. 494 to 497; Supplement Table S2 (page 17), rows EtoshaL1 to EtoshaL4, SuksesL, Sossusvlei, column Reference; Supplement Table S2 (pages 16 to 19), column Type of sample |
| Quotation | "and literature reported patterns from known potential source areas (PSA) across the Southern"; "this study" |
| Concern | The methods describe the PSA database as a compilation from the literature (l. 105, l. 126). Table S2 assigns six SAF patterns to "this study". Sampling, size separation, digestion and analysis of these samples are not described anywhere, only UCC-normalised values are given, and the data statement does not distinguish new from compiled data, so the origin of a new data source cannot be traced. The size fractions also differ between regions (counted in Table S2): AUS 100 of 107 entries finer than 90 µm, CWA 5 of 5 and NZ 19 of 25 finer than 5 µm, PAT a mix of fractions and sample types (finer than 63 µm, finer than 5 µm, top soil, aeolian dust). Whether this heterogeneity shifts the attribution towards one region is a question to the authors. |
| Suggestion | After l. 131 identify the six new samples and describe their collection, size separation and analysis, give their concentrations in Table S2 or a repository, and name them in the data statement (l. 494 to 496). Add a column with the size fraction to Table S2 and test the sensitivity of the results to restricting the database to fine fractions (for example finer than 10 µm). |
| Status | verified (labels and fractions in Table S2; absence of a methods description); assumption (effect of the size fractions, asked as a question) |
| Severity | moderate |
| Source | S2, SD |

**GB-13 The model inputs, namely the EDC REE concentrations, the correction factors and the per-element uncertainties, are neither provided nor addressed by the data statement.**

| Field | Content |
|---|---|
| Check | P12, P8 |
| Location | p. 4, l. 107 to 124; p. 5, l. 155 to 158; p. 16, l. 494 to 496; Supplement Tables S1 to S5 |
| Quotation | "this method does not fully dissolve all mineral particles, we applied cfi derived from parallel"; "All data needed to evaluate the conclusions in the paper are present" |
| Concern | The supplement contains model outputs (Table S1, Table S5), the PSA database (Table S2) and isotope tables (Tables S3, S4). It contains no EDC REE concentrations, no list of the 15 patterns removed for missing data (l. 114), no values of the correction factors cf_i with their number of samples, ages and variability (needed for the Monte Carlo runs, l. 157 to 158), and no values of the per-element uncertainties of "2% and 10%" (l. 155 to 156). The statement neither points to Gabrielli et al. (2010) or a repository for the input concentrations nor says that they are available on request. "All data needed" therefore does not hold for the inputs of the central calculation. Whether correction factors obtained on some samples hold for glacial and Holocene dust alike, whose mineralogy the manuscript considers different (l. 253 to 257), is a question to the authors. |
| Suggestion | Add a supplementary table with, per sample, age, depth or sample code and the 13 corrected, UCC-normalised REE values, and a table of cf_i with its standard deviation and sample basis and of the analytical uncertainty per element; or cite the repository with identifier in l. 494 to 496. |
| Status | verified (absence in the supplement and the statement); assumption (validity of constant correction factors, asked as a question) |
| Severity | moderate |
| Source | S2, SD |

**GB-14 The abbreviations PSA, DS and DIC each carry two meanings, and the caption of Table S1 names 217 PSAs and 279 samples, while the table lists the 241 retained samples.**

| Field | Content |
|---|---|
| Check | P38, P23 |
| Location | p. 4, l. 109 and l. 129; p. 5, l. 144 and l. 147; Supplement Table S1 caption (page 11); Supplement Table S2 title (page 16) |
| Quotation | "samples from Ice Cores (DIC)"; "(PAT; 39 dust sources, DS)"; "sample, DS)- is multiplied by a vector of 217 components"; "approximate the REE signature of a given dust ice core"; "based on th DEPOT model results - using 217 PSAs and 279"; "Table of PSAs database" |
| Concern | The methods separate the seven source areas (PSA) from the 217 individual REE patterns (DS), on which the aggregation in l. 160 to 162 relies. The supplement does not keep this separation: the caption of Table S1 calls the 217 patterns "PSAs", and Table S2 is titled a "PSAs database". DS is expanded once as "dust sources" (l. 129) and once as "dust source sample" (l. 143 to 144); DIC once as "Dust samples from Ice Cores" (l. 108 to 109) and once as "dust ice core" (l. 147). The caption of Table S1 also names "279 DIC", while the table has 241 rows (Late Holocene 60, Early Holocene 56, YD 9, ACR 8, HS1 27, LGM 40, MIS3 41); the 38 excluded samples are not listed, so a reader cannot see the ages and R values of the samples that l. 175 describes. |
| Suggestion | Use PSA only for the seven regions and DS only for the 217 patterns, and expand DS and DIC once, identically. Change the caption of Table S1 to "Median PSA contributions (in %) based on the DEPOT model results, using 217 dust source (DS) patterns from 7 PSAs, for the 241 DIC samples retained (R ≥ 0.67) out of 279 processed", the title of Table S2 to "Database of the 217 dust source (DS) REE patterns", and add the 38 excluded samples with age and R in a separate block. |
| Status | verified (wording on the page images; row count of Table S1) |
| Severity | minor |
| Source | S2, S3, SD |

**GB-15 Four ages occur twice in Table S1 with different results, and the stated sample spacing of 60 to 140 years does not hold.**

| Field | Content |
|---|---|
| Check | P38, P20, P6 |
| Location | p. 4, l. 110 to 111; p. 6, l. 179; p. 12, l. 408; Supplement Table S1, rows 3559 (page 11), 10511 and 12841 (page 13), 28709 (page 14), column Time |
| Quotation | "with an average temporal resolution of approximately 100 years, ranging from 60 to 140" |
| Concern | Table S1 is the only per-sample output and uses the age as identifier. The ages 3559, 10511, 12841 and 28709 each appear in two rows with different compositions: 3559 (PAT 86.7 and 0.0; AUS 12.8 and 49.8), 10511 (PAT 0.0 and 38.2; SAF 49.2 and 12.3), 12841 (PAT 39.5 and 71.9), 28709 (PAT 68.8 and 72.5). Of the 240 spacings between adjacent retained samples, 77 are below 60 years, four of them 0; the median is 98 and the mean 128.5 years. Removing samples can only enlarge spacings, so spacings below 60 years were present in the original 294 samples as well. Without depth or sample code, the rows cannot be linked to the samples of Gabrielli et al. (2010). If the duplicates are replicate analyses of one depth interval, n = 241 counts four intervals twice, the period means weight them double, and the YD count of 9 (GB-55) contains one duplicate. Are these different depths with identical rounded ages, or replicates of the same sample? |
| Suggestion | Add a sample code or depth column to Table S1 and explain the four pairs in its caption; if they are replicates, average or flag them and recompute Table S5 and the counts in l. 179 and l. 408; give the actual spacing range and median in l. 110 to 111. |
| Status | verified (four duplicate ages on the page images); inferred (spacings computed from Table S1); assumption (nature of the duplicates, asked as a question) |
| Severity | moderate |
| Source | S2, S3, SD |

**GB-16 Sample ages on EDC3 and period limits after an AICC2012 paper are combined without a statement on the chronology, and the chronologies of EDML and of the Figure S2 records are not given.**

| Field | Content |
|---|---|
| Check | P35 |
| Location | p. 4, l. 111; p. 6, l. 184 to 188; p. 12, l. 403 to 409; Supplement Figure S2 caption (page 3) |
| Quotation | "The age model follows the EDC3 chronology (Parrenin et al., 2007)." |
| Concern | The period limits cite Veres et al. (2013), whose title names the AICC2012 chronology (l. 817 to 821), while the sample ages follow EDC3. The assignment of samples near 14.7, 12.9 and 11.7 kyr BP and the comparison of timing with EDML (l. 444 to 446) depend on a common chronology; the EDML record and the nssCa2+, δ18O and deuterium excess series of Figure S2 carry no chronology statement. The size of the offset between EDC3 and AICC2012 in this interval could not be checked from the manuscript, so its effect is put as a question. |
| Suggestion | State in Section 2 the chronology of every record (EDC REE, EDML, Figure S2 series) and of the period limits, and either transfer all to one chronology or quantify the offset at the period limits. |
| Status | verified (citations in l. 111 and l. 188); assumption (effect of the offset, asked as a question) |
| Severity | moderate |
| Source | SD |

**GB-17 The ice-core REE vector carries different symbols in Eq. 1, Eq. 2 and the Monte Carlo description, and l. 159 refers to the wrong equation.**

| Field | Content |
|---|---|
| Check | P38 |
| Location | p. 4, l. 119 and l. 125; p. 5, l. 141, l. 147 and l. 156 to 159 |
| Quotation | "by minimizing Eq. (1)."; "depending on the specific REE - Dusti" |
| Concern | The REE concentration of an ice-core sample appears as the acid-leaching concentration in Eq. 1, as DIC_La to DIC_Lu in Eq. 2, with lower-case subscripts in l. 147 and as Dust_i in l. 156 to 157. Eq. 1 defines the correction factor and contains nothing to minimise; the minimised norm is Eq. 2. A reader rebuilding the Monte Carlo step cannot tell which vector is perturbed (leached or corrected values) and which equation is solved. |
| Suggestion | Introduce one symbol for the corrected, UCC-normalised ice-core REE vector and use it in Eq. 2, l. 147 and l. 156 to 157; state whether cf_i is applied before or after the perturbation; change "Eq. (1)" in l. 159 to "Eq. (2)". |
| Status | verified (page images pp. 4 and 5) |
| Severity | minor |
| Source | S2, S4, SD |

**GB-18 With 217 candidate end-members and 13 equations per sample the unmixing is underdetermined, and the manuscript does not show that source-area contributions are identifiable.**

| Field | Content |
|---|---|
| Check | P9 |
| Location | p. 4, l. 126 to 138; p. 5, l. 142 to 152; p. 3, l. 70 to 71; p. 2, l. 64 to 65; Supplement Table S2 |
| Quotation | "Sources with CDS equal to 0 are excluded from the fit, indicating"; "no detectable contribution to that specific DIC sample." |
| Concern | The system has 13 rows (UCC-normalised REE without Gd, l. 145) and 217 columns (l. 143 to 144), so many combinations of patterns can reproduce one sample equally well; a zero coefficient then marks a pattern not chosen, not a source absent. The manuscript criticises isotopes for overlapping fields (l. 64 to 65) and states that REE patterns carry more discriminative information (l. 70 to 71), but it does not test whether the PSA patterns are distinguishable after normalisation; the Monte Carlo runs perturb only the sample values and the correction factors (l. 157), not the choice among similar end-members. The database is also unbalanced: AUS holds 107 of 217 entries (49.3 %), PAT 39 (18.0 %), ANT 4. Whether a region with more candidate patterns is selected more often for noisy samples is not examined: could the Holocene rise of AUS (23.1 % against 10.2 % in the LGM, Table S5) be partly a selection effect? The method paper is cited for details (l. 107), but the present configuration differs from it (l. 145; GB-22). The finding is major because the source-area shares, the main result, depend on identifiability. |
| Suggestion | Add to Section 2 a recovery test for the present configuration: synthetic mixtures of database patterns with known shares and noise at the EDC level (2 to 10 %, l. 155 to 156), unmixed with DEPOT, with recovered against true shares per PSA, repeated with each pattern left out in turn. Report the number of non-zero patterns per sample and, as a check, a fit with seven mean PSA end-members (13 equations, 7 unknowns). Reword l. 151 to 152 to "not selected in the best fit". |
| Status | verified (dimensions in l. 143 to 145; counts in Table S2); inferred (identifiability problem); assumption (selection effect of database size, asked as a question) |
| Severity | major |
| Source | SD |

**GB-19 Supplementary tables are cited under wrong numbers in five places.**

| Field | Content |
|---|---|
| Check | P38, P4 |
| Location | p. 4, l. 127 to 128; p. 6, l. 183; p. 26, l. 858 and l. 865 to 866; p. 28, l. 876 |
| Quotation | "(Figure S1, and Table S1). This"; "(refs. Table S1, - open symbols)"; "the isotopic fingerprint (Table S4) and elemental concentration"; "between EDC and EDML ice cores (Table S4)." |
| Concern | By their titles, Table S1 holds per-sample model results, Table S2 the PSA database, Table S3 isotopic and elemental values of the PSA end-members, Table S4 measured ice-core isotope values and Table S5 the period means of EDC and EDML. The manuscript calls the PSA database "Table S1" (l. 127) and "Table S2" in the next sentence (l. 128), the ice-core isotope data "Table S1" (l. 858), the end-member isotopic fingerprints "Table S4" (l. 865) and the EDC and EDML period means "Table S4" (l. 876). In l. 183 to 184 the interval summaries are attributed to Table S1, which lists per-sample medians; the interval means are in Table S5. Table S4 is never cited correctly in the text. |
| Suggestion | Change "Table S1" in l. 127 to "Table S2", "Table S1" in l. 858 to "Table S4", "(Table S4) and elemental concentration of the PSAs end-members (Table S3)" in l. 865 to 866 to "and elemental concentration of the PSA end-members (Table S3)", "(Table S4)" in l. 876 to "(Table S5)", and "Table S1" in l. 183 to "Table S5" (or describe Table S1 as per-sample results). |
| Status | verified (page images pp. 4, 6, 26, 28; table titles on supplement pages 11, 16, 20, 21, 22) |
| Severity | minor |
| Source | S2, S4, AB, SD |

**GB-20 The Puna-Altiplano sub-regions are named in up to four ways, and the column "Puna" of Table S1 does not say which Puna it contains.**

| Field | Content |
|---|---|
| Check | P38 |
| Location | p. 4, l. 129 to 130; p. 7, l. 212 to 215; p. 11, l. 353 and l. 355 to 362; Supplement Table S1 header (page 11); Supplement Table S2 section header (page 16); Supplement Table S3 (page 20) |
| Quotation | "(PAP; 14 DS from North and South Puna and Southern Altiplano)"; "the emergence of South Altiplano dust"; "S-Altiplano" |
| Concern | The southern Altiplano appears as "Southern Altiplano", "South Altiplano", "S-Altiplano" and "Altiplano"; the southern Puna as "South Puna", "S-Puna" and, in Table S1, "Puna". The PSA itself is "Puna-Altiplano Plateau" (l. 129 to 130, l. 353) and "Puna AltiPlano" (Table S2). The objects are the same, but Table S1 does not state whether "Puna" includes the North Puna patterns, which according to l. 356 do not contribute. |
| Suggestion | Fix one name per sub-region (South Puna, North Puna, Southern Altiplano) and use it in l. 213, Table S1, Table S2 and Table S3; label the Table S1 column "South Puna" or "Puna (North and South)". |
| Status | verified |
| Severity | minor |
| Source | S2 |

**GB-21 Two Australian patterns appear twice in Table S2 under different names and basins, and the counts per source area in the text and in Figure S1 differ from the table.**

| Field | Content |
|---|---|
| Check | P38, P3 |
| Location | p. 4, l. 131 to 133; p. 11, l. 366; Supplement Table S2 (page 17), rows Darling26 and Darling29; Supplement Table S2 (page 18), rows Murray24 and Murray29; Supplement Table S2 (page 19), block Antarctica; Supplement Figure S1 (page 2), Antarctica inset |
| Quotation | "Australia (AUS; 106 DS, predominantly from the central"; "and Antarctica (ANT; 5" |
| Concern | Darling29 (Darling Basin) and Murray24 (Murray Basin) have identical coordinates (34°28'48.00"S 142°49'48.00"E) and all 13 values identical; the same holds for Darling26 and Murray29 (34°3'0.00"S 142°3'10.80"E). One pattern thus carries two names and two basins. Table S2 has 107 AUS rows (105 distinct patterns) and 4 ANT rows (ELB, Expcove, Miers, Vict), while l. 131 to 133 give 106 and 5; both versions sum to 217. The Antarctica inset of Figure S1 shows five markers, as the text, so the fifth mapped site cannot be identified in Table S2. Identical columns make the split between the two copies non-unique: the aggregated AUS share is unaffected, but the attribution to the Darling sub-basin in l. 366 is. |
| Suggestion | Remove or justify the duplicate rows and assign each pattern to one basin; reconcile Table S2, Figure S1 and l. 131 to 133 (add the fifth Antarctic sample to Table S2 or remove it from Figure S1 and correct l. 133, and correct the AUS count); state whether the sub-basin attribution in l. 366 changes after deduplication. |
| Status | verified (duplicate values and coordinates in Table S2; counts; marker count on the page image by instance AB); inferred (effect on the sub-basin attribution) |
| Severity | moderate |
| Source | S2, AB, SD |

**GB-22 The EDC record (13 REE, 217 patterns) is compared with an EDML record computed with an earlier model configuration (14 REE including Gd), so the differences between the cores may be partly methodological.**

| Field | Content |
|---|---|
| Check | P7 |
| Location | p. 5, l. 144 to 145; p. 4, l. 115 to 117; p. 12, l. 403 to p. 13, l. 428; Figure 4 (page 28); Supplement Table S5 (page 22), EDML block; Supplement Figure S5 (page 10) |
| Quotation | "n was equal to 14 but is only 13 in the present study because of the exclusion of Gd." |
| Concern | Aim (4) rests on differences between the two cores (for example NZ plus 8 points in the LGM, PAT minus 14 points in the Holocene, l. 417 to 424). The manuscript states that the EDML model used 14 REE including Gd (l. 144 to 145), an element it now regards as "low and often unreliable" and adding noise (l. 115 to 117). The abstract of Vanderstraeten et al. (2023), read by instance SD, reports a database of 207 REE patterns, against 217 here. The manuscript does not say whether the EDML values in Table S5, Figure 4 and Figure S5 were recalculated with the present configuration (see GB-07). If they were not, every difference between EDC and EDML mixes site and method, and the Gd correction was applied to one record only. The finding is major because the answer to aim (4) would change. |
| Suggestion | Rerun the EDML REE data (Wegner et al., 2012) with the present configuration (13 REE, 217 patterns, same correction and threshold) and base Table S5, Figure 4, Figure S5 and Section 4.4 on it; if this has been done, say so in Section 2 and the captions; report EDC with 14 REE as a check of the effect of removing Gd. |
| Status | verified (l. 144 to 145; 207 patterns in the abstract of Vanderstraeten et al., 2023, marineinfo.org record); inferred (effect on the differences) |
| Severity | major |
| Source | SD |

**GB-23 The Monte Carlo uncertainty of the source contributions is described but not reported for any sample or period.**

| Field | Content |
|---|---|
| Check | P11, P31 |
| Location | p. 5, l. 153 to 165; p. 6, l. 179 to 181; Supplement Table S1 (pages 11 to 15); Supplement Table S5 (page 22); Figure 1 (page 24); Figure 3 (page 27) |
| Quotation | "the PSA mixes calculated by the model were considered meaningful compared to the uncertainties" |
| Concern | The Monte Carlo set-up yields a distribution per pattern and PSA (l. 160 to 165), which is the right tool. The paper reports only medians (Table S1, captioned "Median of PSA's contribution"), interval means (Table S5) and box plots of medians across samples (Figure 3, Figure S4); no spread, interquartile range or credible interval is given per sample, per period or in the text. The statement in l. 180 to 181 that the mixes are meaningful compared to the uncertainties therefore cannot be checked, and neither can period differences of a few points (l. 189 to 216) or single-sample features such as minima and values over 90 % (GB-34). The comparison of 2000 and 5000 runs (l. 163 to 164) is reported only as a verdict. |
| Suggestion | Add the 16th and 84th percentiles (or the interquartile range) of each PSA distribution per sample to Table S1, a dispersion measure to Table S5, and an uncertainty band to Figure 1; report the difference between 2000 and 5000 runs as numbers in the supplement. |
| Status | verified |
| Severity | moderate |
| Source | S3, SD |

**GB-24 How the fitted coefficients become percentages of total deposition is not described, and one row of Table S1 sums to 93.5 %.**

| Field | Content |
|---|---|
| Check | P23, P8 |
| Location | p. 5, l. 160 to 165; p. 5, l. 139; Supplement Table S1 (page 13), first row 10511 |
| Quotation | "the ensuing CDS results (in % of total deposition)"; "10511 0,0 0,0 3,1 6,7 49,2 29,5 5,0 0,0 0,66" |
| Concern | The constrained least-squares fit on UCC-normalised concentrations gives coefficients with a non-negativity constraint only (l. 139), not a sum constraint; how they become "% of total deposition" (l. 160) is not described. The values in Table S1 are separate medians of PSA distributions (l. 164 to 165), which need not sum to 100 %, yet 240 of the 241 rows sum to 100 within 0.1, which suggests an undescribed renormalisation. The first row at 10511 yr BP sums to 0.0 + 0.0 + 3.1 + 6.7 + 49.2 + 29.5 + 5.0 + 0.0 = 93.5. Either a value of 6.5 is missing or mistyped in one column, or this row was not renormalised. The row is also one of the duplicates (GB-15) and one of the three rows with R = 0.66 (GB-25), and it enters the Early Holocene means of Table S5. |
| Suggestion | Describe in Section 2 the normalisation from coefficients to percent, whether medians are renormalised to 100 %, and whether patterns are aggregated to PSA per simulation or per median; check the row at 10511 yr BP against the model output and correct it. |
| Status | verified (row sum on the page image; absence of a description); inferred (renormalisation inferred from the row sums) |
| Severity | moderate |
| Source | S3, SD |

**GB-25 The fit threshold R ≥ 0.67 does not correspond to p below 0.01 with the stated or the correct degrees of freedom, and three retained samples fall below it.**

| Field | Content |
|---|---|
| Check | P1, P23, P5 |
| Location | p. 5, l. 170 to 172; p. 6, l. 174 to 179; Supplement Table S1, rows 2888 and 3267 (page 11) and first row 10511 (page 13), column R |
| Quotation | "two-tailed test, degrees of freedom ="; "38 did not meet the R threshold (R≥0.67) and" |
| Concern | With 13 REE per pattern a Pearson correlation has 11 degrees of freedom, not 10. Computed with scipy, a two-tailed p below 0.01 requires R ≥ 0.708 for df = 10 and R ≥ 0.684 for df = 11; R = 0.67 corresponds to p = 0.017 (df = 10) or p = 0.012 (df = 11). The p-value further assumes independent elements, while the R tested is the median over 2000 fits of a modelled pattern to the observed one; whether the test is then meaningful is a question to the authors. Table S1 contains three retained rows with R = 0,66 (2888, 3267 and the first row at 10511 yr BP), against the stated rule; a printed 0,66 is below 0.665, so rounding does not explain it. Either the threshold was applied to a different R than the tabulated median (then l. 169 to 170 describe the wrong statistic), or the three samples should have been excluded (then 41 are excluded and 238, or 85.3 %, retained, and the Late Holocene means change to PAT 50.3 % and AUS 21.8 %, n = 58), or the threshold was 0.66. The threshold decides which samples form the record: with R ≥ 0.71, 19 rows drop out, all younger than 12.9 kyr BP (17 Holocene, 2 YD); the YD set shrinks from 9 to 7 rows and its AUS mean from 14.5 to 9.1 %, while the Holocene means change by less than 1 point (PAT 49.0 to 48.4 %, AUS 23.1 to 23.6 %) and the glacial means not at all. |
| Suggestion | In l. 170 to 172 give the n and degrees of freedom used and either the threshold that matches p below 0.01 or the p that matches 0.67; state which R statistic was tested and how the dependence between fitted and observed patterns is handled, or replace the test by a criterion calibrated with synthetic mixtures (GB-18); remove or flag the three rows with R = 0.66 and correct the counts in l. 174, l. 179 and the Abstract (l. 19), and report which period means change under the corrected threshold. |
| Status | verified (wording; three rows on the page images); inferred (critical values and sensitivity computed with Python from Table S1); assumption (which R was tested; dependence of the elements, asked as questions) |
| Severity | moderate |
| Source | S3, SD |

**GB-26 Figure S1 is a low-resolution composite in which region labels, place names and scale values cannot be read.**

| Field | Content |
|---|---|
| Check | P29 |
| Location | Supplement Figure S1 (page 2), all map panels; caption (page 1) |
| Quotation | "Localization of dust sources (DS) used in our DEPOT algorithm" |
| Concern | The map composite is embedded as a raster of 800 x 450 pixels at 78 ppi, with two insets at 146 and 170 ppi. At this resolution the region label of the CWA panel (pink on pink) is illegible, and the place names in all panels and the values of the scale bars, except "900 km" in PAT and "80 km" in ANT, cannot be read. The figure is the only place where a reader sees the spatial distribution of the 217 dust sources (l. 127). |
| Suggestion | Re-export Figure S1 at a resolution of at least 300 dpi at print size, enlarge the region labels and scale values, and give each panel a scale bar with a readable value. |
| Status | verified |
| Severity | minor |
| Source | AB |

**GB-27 Two new end-member samples labelled "Etosha Pan" lie 262 and 655 km from the Etosha samples, and all six new samples carry west longitudes.**

| Field | Content |
|---|---|
| Check | P38 |
| Location | Supplement Table S2 (page 17), rows SuksesL and Sossusvlei, columns Location, Lattitude, Longitude; rows EtoshaL1 to EtoshaL4, column Longitude; p. 12, l. 386 to 398 |
| Quotation | "21,059 S 16,836 W"; "24,76 S 15,29 W"; "Dust contributions from the Etosha Pan were more sporadic" |
| Concern | The sample named Sossusvlei is located at "Etosha Pan" in the location column, as is SuksesL. With the coordinates of the table (east longitude assumed), SuksesL lies 262 km and Sossusvlei 655 km from Etosha1 (18°53'26.6"S 15°50'35.5"E), whereas EtoshaL1 to EtoshaL4 lie 29 to 108 km from it (haversine distances). One label thus names two different places. All six new rows give "W" longitudes, which would place them in the Atlantic; the other SAF rows give "E". The discussion attributes SAF contributions to Etosha, Makgadikgadi and the Namibian coast (l. 386 to 398); if this grouping followed the location column, contributions of SuksesL or Sossusvlei would be counted as Etosha. How were the patterns grouped into the SAF sub-systems? |
| Suggestion | Correct the location of SuksesL and Sossusvlei in Table S2 (for example "Sossusvlei, Namib"), change "W" to "E" in the six rows, and state in the methods how patterns were grouped into the SAF sub-systems used in l. 386 to 398. |
| Status | verified (labels, coordinates, distances); assumption (grouping by the location column, asked as a question) |
| Severity | moderate |
| Source | S2, SD |

**GB-28 The four Antarctic end-member patterns alternate between neighbouring elements unlike every other database entry, so the absence of Antarctic contributions may be caused by the input rather than by transport.**

| Field | Content |
|---|---|
| Check | P27 |
| Location | Supplement Table S2 (page 19), rows ELB, Expcove, Miers, Vict; Supplement Table S2 (page 17), row Kuiseb2inf5, column Dy; p. 10, l. 329 to 334; p. 7, l. 217 to 218 |
| Quotation | "0,720323 1,414516 0,157226"; "our results do not indicate significant Antarctic contributions to EDC" |
| Concern | The ANT rows alternate strongly between neighbouring elements (ELB: La 0,720323, Ce 1,414516, Pr 0,157226, Nd 0,604516, Sm 0,120000, Eu 0,030516, Tb 0,014774). The largest step between neighbouring elements, in log10, is 0.92 to 0.96 for the four ANT rows and at most 0.49 for all 213 other rows. Such odd-even alternation is typical of concentrations that are not normalised; patterns of this shape cannot be combined to fit a smooth ice pattern, so ANT may be excluded by the input, not by transport. The manuscript explains the absence by katabatic winds and wind directions (l. 331 to 334) and contrasts it with 24 % in Coppo et al. (2022) (l. 327 to 328). Kuiseb2inf5 also has Dy = 6,200013 between Tb = 2,692922 and Ho = 2,149792. Are the ANT values mis-normalised or in another unit? The finding is major because the result on Antarctic sources (l. 329 to 334) could change. |
| Suggestion | Check normalisation and units of the ANT rows and of Kuiseb2inf5 against Diaz et al. (2018) and Vanderstraeten et al. (2023); add a screening rule for end-member patterns to Section 2; rerun with corrected ANT patterns and revise l. 329 to 334 accordingly. |
| Status | verified (values in Table S2 on the page images); inferred (step sizes computed with Python); assumption (mis-normalisation as cause, asked as a question) |
| Severity | major |
| Source | SD |

#### Minor corrections

| ID | Location | Quotation | Replacement | Source |
|---|---|---|---|---|
| KK-12 | p. 3, l. 101 | "to ice core camples" | "to ice core samples" | SD |
| KK-13 | p. 4, l. 128 | "subdivised into Patagonia" | "subdivided into Patagonia" | ZF |
| KK-14 | Supplement Table S2 header (page 16) | "Lattitude" | "Latitude" | ZF |

#### Verification log

| ID | Check | Checked | Values | Result |
|---|---|---|---|---|
| PP-12 | P12 | Inventory of all data sources named in the methods (l. 99 to 172) and figures, held against the data statement (l. 494 to 496) and the supplement | EDC REE patterns (294 samples): not in the supplement; correction factors and per-element uncertainties: absent; PSA database: Table S2; code: absent; per-sample PSA medians: Table S1 (241 rows); pattern-level results, excluded samples, absolute fluxes: absent; nssCa2+ flux, δ18O, deuterium excess: Figure S2, cited by publication; isotope end-members and ice-core isotopes: Tables S3, S4; EDML period means: Table S5. The statement gives no link, DOI or repository | GB-11, GB-12, GB-13, GB-30, GB-54; third-party records used for figures count as published through the cited source |
| PP-13 | P38 | Names of ice cores and of the algorithm | EDC and EPICA Dome C, "Epica Dome C" (KK-26), "Epica dome C" (Table S4); Vostok, Taylor Glacier, Berkner Island, "Old Dome C" are distinct cores; "DEPOT" algorithm and model, "statistical unmixing algorithm", "unmixing model", "source apportionment model" | one object each; no finding |
| PP-14 | P8 | Tool chain from data to result | Data: Gabrielli et al. (2010), published; normalisation: Rudnick and Gao (2003); correction factors: values missing; fit: MATLAB lsqnonneg, settings missing; Monte Carlo: distributions named, variability of cf_i missing; conversion to percent and aggregation: not described; isotope calculation: Eq. 3 and 4 with Table S3 | GB-11, GB-13, GB-24 |
| PP-15 | P12, P23 | Sample balance from raw data to record | 294 minus 15 = 279 (l. 108, l. 114, l. 117); 279 minus 38 = 241 (l. 174, l. 179); 241 / 279 = 86.4 % (text 86 %); rows of Table S1 = 241; periods 60 + 56 + 9 + 8 + 27 + 40 + 41 = 241; first and last age 2852 and 33699 yr BP; four samples between 21.7 and 27.3 kyr BP (22150, 23104, 25384, 25640) as in l. 113 | no finding on the balance itself; content of the rows see GB-14, GB-15, GB-25 |
| PP-16 | P1 | PSA database total and mean resolution | 39 + 5 + 14 + 23 + 106 + 25 + 5 = 217 (l. 129 to 133); (33699 minus 2852) / 293 = 105.3 yr for the original samples (text "approximately 100 years") | no finding; sampling gap disclosed (l. 113); counts per region see GB-21 |
| PP-17 | P38 | Names of climatic periods and chronologies | MIS3, LGM, HS1, ACR, YD, Holocene, Early and Late Holocene with limits in l. 184 to 188 and Table S5; sample ages on EDC3 (l. 111), period limits from Veres et al. (2013, AICC2012) | names consistent apart from KK-02, KK-17, KK-25; the chronologies see GB-16 |
| PP-18 | P17 | Place of the disclosed limitations | Sampling gap in the Methods (l. 113, correct place); Gd removal in the Methods (l. 115 to 117); exclusion of 38 samples only in the Results (l. 174 to 179); ACR and YD caveat only in Section 4.4 (l. 407 to 409); extended SAF and AUS isotope domains only in the Figure 2 caption (l. 863) | GB-29, GB-02 |
| PP-19 | P30 | Reported corrections against reported runs | Gd removed from EDC and PSA patterns (l. 115 to 117, l. 134 to 135); EDML record computed with Gd (l. 145) | GB-22 |
| PP-20 | P38 | Names of the source areas and end-members | SSA = PAT + CWA + PAP (l. 128 to 130, l. 280); CWA "Central Western Argentina" (l. 129), "Central-Western-Argentina" (l. 852 to 853), "Southern Central Western Argentina (SCWA)" in Table S3 is the southern subset (rows SCWA1 to SCWA3 of Table S2); "New-Zealand" in Tables S2 and S3 | no finding; PAP variants see GB-20 |
| PP-21 | P26 | Non-negativity guarantee across all paths | lsqnonneg in every Monte Carlo run, guarantee holds; a sum of 100 % is not guaranteed (row at 10511 yr BP sums to 93.5) | GB-24 |
| PP-22 | P33 | Effort statements | Only the computation cost of the Monte Carlo runs (l. 162 to 164), not used as result or limitation | no finding |
| PP-23 | P1 | Sensitivity of the record to the R threshold, from Table S1 | R ≥ 0.67: 238 rows (3 dropped); R ≥ 0.68: 234; R ≥ 0.71: 222, all dropped rows younger than 12.9 kyr BP; Late Holocene PAT 50.3, 50.9, 49.4 %; YD AUS 14.5, 14.5, 9.1 % | basis for GB-25 |
| PP-24 | P32 | Claims of checked or robust results | No claim of error-free results; "robust" (l. 172, l. 259) rests on R and on the isotope comparison; no independent recovery test exists | GB-18, GB-25, GB-43 |
| PP-25 | P3 | Count of CWA markers in Figure S1 against l. 129 and Table S2 | 5 markers (counted on an enlarged crop), 5 rows | no finding |

### Segment 3: Results (pp. 6 to 7, Figures 1 and 3)

#### Substantive findings

**GB-29 The record is filtered by fit quality, and the larger Holocene variability coincides with lower fit quality, so analytical noise and climate signal are not separated.**

| Field | Content |
|---|---|
| Check | P9 |
| Location | p. 6, l. 174 to 182; p. 4, l. 112; p. 9, l. 306 to p. 10, l. 314; p. 6, l. 194; Supplement Table S1 |
| Quotation | "These excluded samples are all younger than 14 kyr BP and"; "have very low REE concentrations near the detection limit." |
| Concern | The manuscript states that low concentrations after HS1 let analytical noise distort the patterns (l. 176 to 179) and removes these samples. The same conditions apply to the retained Holocene samples, yet their scatter is read as climate (l. 306 to 314; minima at 10, 8.6 and 6.3 kyr BP, l. 194), and "significantly larger variability" (l. 306) is not tested. Computed from Table S1: the 38 exclusions are 22.8 % of all samples younger than 14 kyr BP (38 of 38 + 129); the mean R is 0.799 in the Holocene (116 samples) against 0.916 before 14.7 kyr BP (108 samples); the standard deviation of PAT is about 32 points in the Holocene against about 11 before 14.7 kyr BP; 23 of the 116 Holocene samples have PAT = 0. Each Holocene sample integrates 2 to 3 years (l. 112), so sample-to-sample scatter also contains interannual variability. Selecting by R keeps only samples that the database can fit, a selection on the outcome, and ages, concentrations and patterns of the 38 excluded samples are not given. The finding is major because the Holocene variability and its climatic interpretation (Section 4.3) are among the results. |
| Suggestion | List the 38 excluded samples with age, total REE concentration and R in the supplement; plot R and REE concentration against time beside Figure 1; test whether Holocene sample-to-sample differences exceed the Monte Carlo spread of each sample (GB-23); report Holocene means for alternative thresholds and for samples above a concentration limit; in Section 4.3 separate analytical noise and the 2 to 3 year integration from climatic causes before interpreting single-sample minima. |
| Status | verified (l. 112, l. 174 to 179); inferred (figures computed with Python from Table S1) |
| Severity | major |
| Source | SD |

**GB-30 Results at the level of single patterns and sub-regions, on which the discussion relies, are stated without numbers and are not in the supplement, although the data statement claims completeness.**

| Field | Content |
|---|---|
| Check | P12, P6, P11 |
| Location | p. 6, l. 196 to 197; p. 5, l. 160 to 162; p. 10, l. 329 to 330; p. 11, l. 366 to 367; p. 12, l. 385 to 398; p. 16, l. 494 to 496; Supplement Table S1; Supplement Figure S3 (page 6) |
| Quotation | "our algorithm highlights three specific REE patterns collected in"; "our model identifies the Darling sub-basin as the dominant source"; "Additional data related to the paper may be requested" |
| Concern | The Monte Carlo step produces a distribution "for every DS" (l. 161), aggregated "by PSA or specific sub-regions within PSA" (l. 161 to 162), and the discussion uses pattern-level and sub-region results: three Valdes Peninsula patterns (l. 196 to 197; which three of the 39 PAT patterns is not said), the Darling sub-basin as dominant Holocene AUS source (l. 366), the Namibian coast and ephemeral riverbeds as most frequently detected SAF sources and Etosha and Makgadikgadi as larger contributors (l. 385 to 398), and the absence of McMurdo contributions (l. 329 to 330). For PAP the sub-regions have numbers (Puna and Altiplano columns of Table S1), and Figure S3 shows SAF sub-region curves without frequencies; for the Valdes patterns, the Darling sub-basin and the SAF detection frequencies neither shares nor counts with a denominator are given. The data statement claims that all data needed are present and offers additional data on request without saying which. |
| Suggestion | Add a supplement table per sub-region (Valdes patterns, Darling, other AUS basins, Namibian coast, Etosha, Makgadikgadi) and, where used, per pattern, with the number of samples with a contribution above zero out of 241 (and out of the 116 Holocene samples) and the mean contribution per period; name the three Valdes patterns; reword l. 494 to 496 to what is actually provided, with a repository identifier. |
| Status | verified (absence in the text and the supplement; Figure S3 on the page image) |
| Severity | moderate |
| Source | S2, SD, S3 |

**GB-31 The ranking of the secondary sources "in decreasing order of importance" holds for no stated basis.**

| Field | Content |
|---|---|
| Check | P20 |
| Location | p. 6, l. 201 to 202 |
| Quotation | "Overall, other Southern Hemisphere PSAs contribute to EDC dust deposition with sources from: AUS,"; "SAF, PAP and NZ, in decreasing order of importance" |
| Concern | "Overall" suggests the whole record. Mean of the 241 rows of Table S1: AUS 16.5, SAF 9.2, NZ 7.9, PAP 6.85 (Puna 3.09 plus Altiplano 3.76), so NZ ranks above PAP. Mean of the seven period means of Table S5 (Late and Early Holocene, YD, ACR, HS1, LGM, MIS3): AUS 14.6, SAF 9.2, NZ 7.5, PAP 5.6, again NZ above PAP. Only the samples younger than 14.7 kyr BP give the stated order (AUS 21.8, SAF 10.8, PAP 10.3, NZ 5.7). |
| Suggestion | Name the basis in l. 201 to 202, for example "over the whole record: AUS (16.5 %), SAF (9.2 %), NZ (7.9 %) and PAP (6.9 %)", or restrict the statement to the period after 14.7 kyr BP. |
| Status | inferred (means computed from Table S1 and Table S5) |
| Severity | minor |
| Source | S3 |

**GB-32 Two dated maxima cited to Figure 1 lie outside the stated time windows of the smoothed curves.**

| Field | Content |
|---|---|
| Check | P24 |
| Location | p. 6, l. 204 to 205; p. 10, l. 337 to 338; Figure 1 (page 24), panels PAT and AUS |
| Quotation | "with two prominent maxima centered around 9.5"; "centered ~9 kyrs BP, between 7-8 kyr BP and after 6 kyr BP (Figure 1)." |
| Concern | The dated minima are well placed: the bold PAT curve has minima at 10.13, 8.54 and 6.33 kyr BP (l. 194: 10, 8.6, 6.3). The maxima are not. Between the minima the bold PAT curve has its maxima at 9.73 kyr (64.6 %) and 7.71 kyr (71.4 %); there is no maximum near 9 kyr, and between 8.54 and 9.73 kyr the curve rises monotonically; "~9" does not cover 9.73 kyr. The bold AUS curve, for which l. 205 gives a maximum at 9.5 to 10 kyr BP, peaks at 10.14 kyr (40.9 %) and 10.50 kyr (40.8 %), with a local minimum of 22.9 % at 9.79 kyr inside the stated window; the second maximum at 6.30 kyr matches. Calibration of the time axis: 0.4 at 681.0 px and 3.2 at 1859.5 px in the PAT panel (23.8 yr per px). |
| Suggestion | In l. 338 replace "~9 kyrs BP" by "~9.7 kyr BP"; in l. 205 replace the window 9.5 to 10 kyr BP by "10 to 10.5 kyr BP"; or state which curve (raw or smoothed) the dates refer to. |
| Status | verified (positions measured on the page image by instance AB) |
| Severity | minor |
| Source | AB, S2, S4 |

**GB-33 The SAF values of about 2 % between 9.5 and 12 kyr BP and about 11 % in the subsequent Holocene do not follow from Table S1 with a named statistic.**

| Field | Content |
|---|---|
| Check | P20 |
| Location | p. 6, l. 207 to p. 7, l. 208; Supplement Table S1, column SAF, rows 9484 to 11993 |
| Quotation | "levels (~2%) between 9.5 and 12 kyr BP, it rebounds in the subsequent Holocene, averaging ~11%" |
| Concern | Table S1 has 33 rows between 9500 and 12000 yr BP; their SAF mean is 4.3 % and their median 0.3 %, and two rows exceed 40 % (10278: 40.3; 10511: 49.2). "~2%" matches neither and may refer to the moving average of Figure 1, which the text does not say. For the "subsequent Holocene" (samples younger than 9.5 kyr BP) the SAF mean is 13.0 %; "~11%" matches instead the whole Holocene in Table S5 (10.7 %), which includes the low interval. |
| Suggestion | Name statistic and interval in l. 207 to 208, for example "the moving average falls to about 2 % between 9.5 and 12 kyr BP (sample mean 4.3 %), and SAF averages 13.0 % after 9.5 kyr BP (10.7 % over the whole Holocene, Table S5)". |
| Status | inferred (computed from Table S1) |
| Severity | minor |
| Source | S3 |

**GB-34 South Altiplano dust exceeds 90 % at two of the five ages the text lists, not at all five.**

| Field | Content |
|---|---|
| Check | P20, P3, P36 |
| Location | p. 7, l. 213 to 214; Supplement Table S1, column Altiplano, rows 11228, 9957, 8629, 5967, 6166, 3465; Figure 1 (page 24), panel PAP; Supplement Figure S3 (page 6) |
| Quotation | "contributing over 90% at 11.2, 10, 8.6, 6, and 3.5 kyr BP" |
| Concern | Table S1 gives Altiplano as % of total deposition: 97.0 (11228 yr BP) and 100.0 (8629), but 75.7 (9957), 58.5 (5967) or 58.0 (6166), and 62.7 (3465). Since total PAP is an upper bound for its Altiplano part, Figure 1 confirms this: the raw PAP line measures 96.4 % at 11.24 kyr and 97.9 % at 8.62 kyr, but 72.5 % at 9.97 kyr, 56.5 % at 6.17 kyr and 56.1 % at 3.45 kyr. If the 90 % referred to the share of Altiplano within PAP, all five samples would qualify, but so would 20 of the 32 Holocene samples with Altiplano above zero, so the five ages would not be distinguished. Neither reading reproduces the sentence. The qualitative statement that Altiplano dust dominates (above 50 %) in these samples holds for all five. The finding is moderate because a reader cannot reproduce the values on which the compositional shift of PAP (l. 212 to 214) rests. |
| Suggestion | State the denominator in l. 214 and give the values from Table S1, for example "contributing over 90 % at 11.2 and 8.6 kyr BP and 58 to 76 % at 10, 6 and 3.5 kyr BP", and cite Table S1. |
| Status | verified (Table S1 values; Figure 1 measured by instance AB); assumption (the intended denominator) |
| Severity | moderate |
| Source | S3, AB, SD |

**GB-35 South Puna is said to stay below 20 % in the Holocene, but Table S1 lists eight Holocene samples with 20.2 to 29.1 %, and the figure cited shows only the PAP sum.**

| Field | Content |
|---|---|
| Check | P2, P36 |
| Location | p. 7, l. 215; Supplement Table S1, column Puna, rows 3503, 4387, 5657, 5850, 6775, 7833, 10205, 11117 |
| Quotation | "contributions of South Puna remained consistently below 20% during this interval (Figure 1)" |
| Concern | The Puna column (North Puna does not contribute, l. 356) gives in the Holocene 25.0 (3503 yr BP), 20.6 (4387), 23.4 (5657), 29.1 (5850), 20.7 (6775), 25.6 (7833), 25.7 (10205) and 20.2 (11117). The sentence holds neither for the samples nor as a maximum. Figure 1, cited for it, shows only the PAP sum; the sub-region is in Figure S3. The finding is moderate because the cited figure cannot confirm the statement and the table contradicts it. |
| Suggestion | Replace in l. 215 by "remained below 30 % (maximum 29.1 % at 5.85 kyr BP)" or give the Holocene mean of the Puna column, and cite Figure S3 and Table S1 instead of Figure 1. |
| Status | verified |
| Severity | moderate |
| Source | S3, AB, SD |

**GB-36 Tick labels and legends in Figures 1, 2, 3 and 5 are printed below 6 pt.**

| Field | Content |
|---|---|
| Check | P29 |
| Location | Figure 1 (page 24); Figure 2 legend (page 26); Figure 3 (page 27); Figure 5 (page 29) |
| Quotation | "Bold lines denote the mobile average over 9 steps." |
| Concern | Cap or digit heights measured on the 300 dpi page (size in pt = px x 72 / 300 / 0.72; method deviation up to 0.6 pt): Figure 1 tick labels and legend 15 px = 5.0 pt, axis titles 17 px = 5.7 pt; Figure 2 legend 16 px = 5.3 pt; Figure 3 tick labels 16 px = 5.3 pt, category labels 18 px = 6.0 pt; Figure 5 tick labels 13 px = 4.3 pt, legend 14 px = 4.7 pt. Figure 5 and the tick labels and legend of Figure 1 stay below 6 pt even with the method deviation added. |
| Suggestion | Enlarge tick labels, axis titles and legends of Figures 1, 2, 3 and 5 to at least 7 pt at final print size. |
| Status | verified |
| Severity | minor |
| Source | AB |

**GB-37 Abbreviations and period labels in the figures are not resolved in the captions.**

| Field | Content |
|---|---|
| Check | P29 |
| Location | p. 25, l. 851 to 854; p. 27, l. 869 to 873; p. 28, l. 875 to 876; p. 29, l. 880 to 882; Supplement Figure S3 caption (page 5) |
| Quotation | "vertical zones delineate the various periods of the transition from end of MIS3 to Holocene." |
| Concern | The panel labels PAT, AUS, SAF, NZ, PAP (Figures 1, 3, 4), the period labels YD, ACR, HS1, LGM, MIS3 (Figure 1) and "Holo" (Figure 4) are explained only in the main text (l. 128 to 133, l. 184 to 188). Figure S3 shows panels "Etosha", "Namibia" and "Sua" without saying that they are sub-regions of SAF and that Sua belongs to the Makgadikgadi complex (l. 380). The caption of Figure 1 does not give the age limits of the grey zones (measured: YD 11.71 to 12.90, HS1 14.70 to 17.98, MIS3 from 29.01 kyr BP, consistent with l. 184 to 188). |
| Suggestion | Add to each caption the full names of the PSA abbreviations and of the periods with their age limits, and in Figure S3 name the PSA to which each sub-region belongs. |
| Status | verified |
| Severity | minor |
| Source | AB |

**GB-38 The "Holocene" panel of Figure 3 shows the Early Holocene, and the "Early Holocene" panel of Figure S4 shows the Late Holocene.**

| Field | Content |
|---|---|
| Check | P3 |
| Location | p. 27, l. 869 to 870; Figure 3 (page 27), Holocene panel; Supplement Figure S4 (page 8), panel 1, caption (page 7) |
| Quotation | "Figure 3: Box plots of provenance contributions (in %) of Holocene, and Last Glacial Maximum (LGM)"; "Box plots of provenance contributions of (1) Early Holocene" |
| Concern | Measured in the Holocene panel of Figure 3: PAT first quartile 12.27, median 55.16, third quartile 72.96, upper whisker 98.49; AUS 2.80, 18.15, 34.22; NZ median 1.08, third quartile 7.46; highest SAF point 54.29. From Table S1, the Early Holocene (n = 56) gives PAT 12.3, 55.2, 73.0, maximum 98.5; AUS 2.8, 18.1, 34.2; NZ 1.1, 7.5; SAF maximum 54.3, whereas the whole Holocene (n = 116) gives PAT 18.4, 58.6, 73.8, NZ median 0.0 and SAF maximum 73.5. The five SAF values above 55 % of the Holocene (73.5, 71.0, 63.3, 58.2, 56.7) are absent from Figure 3 and appear in the "Early Holocene" panel of Figure S4, whose PAT, AUS and PAP boxes match the Late Holocene of Table S1 (n = 60: PAT 18.9, 61.7, 80.7). The two labels are swapped, and the whole Holocene, which the text discusses (l. 317 to 319), appears in no box plot. |
| Suggestion | Relabel the Holocene panel of Figure 3 as "Early Holocene (7.5 to 11.7 kyr BP)" and the first panel of Figure S4 as "Late Holocene (2.8 to 7.5 kyr BP)" and correct both captions, or replace the Figure 3 panel by the whole Holocene if that is what the caption intends. |
| Status | verified (box positions measured by instance AB; quartiles recomputed from Table S1) |
| Severity | moderate |
| Source | AB |

**GB-39 The captions of Figures 3 and S4 say that the whiskers show the extremes, but points are drawn beyond them.**

| Field | Content |
|---|---|
| Check | P29 |
| Location | p. 27, l. 872; Figure 3 (page 27), LGM panel; Supplement Figure S4 caption (page 7) |
| Quotation | "and the whiskers indicate the lower and upper extremes" |
| Concern | In the LGM panel of Figure 3 the PAT whisker ends at 84.36 % while a point lies above it (Table S1 maximum 93.5 %); the SAF whisker ends at 14.49 % with three points above it (Table S1: 17.2, 28.4 and 34.7 %). The whiskers end at the last value within 1.5 times the interquartile range (PAT: 71.7 + 1.5 x 12.8 = 90.9; highest value below is 84.4). Points beyond the whiskers are outliers, not extremes. |
| Suggestion | Replace the phrase in both captions by "whiskers extend to the most extreme values within 1.5 times the interquartile range; points beyond are shown individually". |
| Status | verified |
| Severity | minor |
| Source | AB |

**GB-40 The sub-regional series of Figure S3 do not reproduce Table S1 or the PAP panel of Figure 1.**

| Field | Content |
|---|---|
| Check | P3 |
| Location | Supplement Figure S3 (page 6), panels Altiplano and Puna; Figure 1 (page 24), panel PAP; Supplement Table S1, columns Puna and Altiplano; p. 11, l. 355 |
| Quotation | "As illustrated in Figure S3, South"; "Puna (i.e., North Puna does not contribute) consistently provides dust throughout the entire record," |
| Concern | Line tops in Figure S3 against Table S1: at 8629 yr BP Altiplano at most 5.8 % (Table S1: 100.0) and Puna at most 2.3 %; at 11228 yr BP Altiplano 14.8 % (97.0); at 9957 yr BP 2.4 % (75.7); at 3465 yr BP 10.1 % (62.7). The highest Altiplano value in the panel is 66.1 % at 6.37 kyr (Table S1, 6367 yr BP: 53.5). Several Puna peaks match Table S1 (3503 yr BP 24.4 against 25.0; 5850 yr BP 29.8 against 29.1), but peaks of 54.9 % at 11.87 kyr and 42.9 % at 11.11 kyr have no counterpart (Table S1 maximum 29.1). Figure 1 shows PAP at 97.9 % at 8.62 kyr, which cannot be the sum of the two Figure S3 panels (at most 8.1 %). A median of 100 % implies that at least half of the Monte Carlo runs gave 100 %, so a different summary statistic cannot explain values below 50 %. The text uses Figure S3 for the timing argument of l. 355 to 360. |
| Suggestion | Regenerate Figure S3 from the same data as Table S1 and Figure 1, state in its caption which statistic is plotted, and check the timing statements of l. 355 to 360 against the corrected figure. |
| Status | verified (values measured on the page image by instance AB); inferred (that a change of statistic cannot explain the difference) |
| Severity | moderate |
| Source | AB |

#### Minor corrections

| ID | Location | Quotation | Replacement | Source |
|---|---|---|---|---|
| KK-15 | p. 6, l. 178 to 179 | "element-specific analytical noise exacerbated by varying ionization efficiencies and UCC normalization" | "element-specific analytical noise, exacerbated by varying ionization efficiencies and UCC normalization, distorts the REE patterns" (removing the unpaired dash at the start of l. 179) | S3 |
| KK-16 | p. 6, l. 189 | "It contributes for 65-70% (average" | "It contributes 65 to 70% (average" | S3 |
| KK-17 | p. 6, l. 191 | "the PSA dust assemblage during HSI is marked" | "the PSA dust assemblage during HS1 is marked" | S3, S2 |
| KK-18 | p. 6, l. 193 | "(averages contributions)" | "(average contributions)" | S3 |
| KK-19 | p. 6, l. 198 | "campaigns and therefore reflects regional mixed input" | "campaigns and therefore reflect regional mixed input" | S3 |
| KK-20 | p. 6, l. 199 | "LREE (low rare earth elements)" | "LREE (light rare earth elements)" | S2 |
| KK-21 | p. 25, l. 851 | "between 2852 to 33699 yr BP" | "from 2852 to 33699 yr BP" | S3, AB |
| KK-22 | p. 25, l. 852; p. 29, l. 882; Supplement Figure S5 caption (page 9) | "Bold lines denote the mobile average over 9 steps." | "Bold lines denote the moving average over 9 samples." (in the Figure S5 caption "moving average over 9 samples") | S3, AB |
| KK-23 | p. 25, l. 853 | "their dust emissions contribution are very low" | "their dust contributions are very low" | ZF |
| KK-24 | p. 27, l. 873 | "for HS1, ACR and YD are illustrated in Figure S4." | "for the other periods (YD, ACR, HS1, MIS3 and the second Holocene interval) are shown in Figure S4." (Figure S4 has five panels) | ZF |
| KK-25 | Supplement Figure S4 caption (page 7) | "(3) Antarctica Cold Reveal (ACR), (4) Heindrich Stadial 1 (HS1), and (5) Marine Isotope 3 (MIS3)" | "(3) Antarctic Cold Reversal (ACR), (4) Heinrich Stadial 1 (HS1), and (5) Marine Isotope Stage 3 (MIS3)" | S2, S3, AB |

#### Verification log

| ID | Check | Checked | Values | Result |
|---|---|---|---|---|
| PP-26 | P1 | Mean correlation coefficient (l. 181) | Mean of the R column of Table S1 = 0.8523 (text 0.852); without the three rows with R = 0.66: 0.8547 | no finding |
| PP-27 | P2, P3, P7 | Table S5 (EDC) recomputed from the 241 rows of Table S1 for 8 periods and 7 PSA, using the printed period brackets | All 56 cells agree within 0.1 (for example Holocene PAT 49.0, AUS 23.1, PAP 11.0; LGM NZ 14.2); the Holocene row is the sample-weighted mean of Late (n = 60) and Early Holocene (n = 56); row sums of Table S5 between 99.9 and 100.1; ACR n = 8 as in l. 408 | no finding for the EDC part |
| PP-28 | P24 | Grey period zones of Figure 1 against l. 184 to 188, and the sampling gap of l. 113 | Zone limits measured in all five panels (23.8 yr per px): YD 11.70 to 12.90, HS1 14.69 to 18.01, MIS3 from 29.00 to 29.01 kyr BP; Figure 1 bridges the gap 21.7 to 27.3 kyr BP with straight segments | no finding |
| PP-29 | P2 | Results text (l. 189 to 216) against Table S5 | PAT MIS3 70.3, LGM 65.7 ("65-70"), HS1 74.8 ("75"), ACR 68.9 ("69"), YD 63.1 ("63"), Late and Early Holocene 50.7 and 47.1 ("47-51"); AUS MIS3 9.1, LGM 10.2, HS1 11.3 ("9, 10 and 11"), YD 14.5 ("~15"), Holocene 23.1 ("23"); SAF 9.3, 6.3, 4.9, 8.0 ("~5 and 9"), YD 14.6 ("15"); NZ LGM 14.2, HS1 7.1, ACR 6.6, YD 3.3, Holocene 5.9; PAP MIS3 2.2, LGM 3.6, HS1 2.0 ("below 4"), ACR 5.2, YD 4.5 ("~5"), Holocene 11.0; CWA 0.0 in all periods, ANT at most 0.6 | no finding for these values; deviations see GB-02, GB-33, GB-34, GB-35 |
| PP-30 | P24 | Minima of PAT in Figure 1 against l. 194 and l. 336 | Bold PAT curve minima at 10.13 kyr (23.6 %), 8.54 kyr (30.9 %), 6.33 kyr (28.5 %); text 10, 8.6, 6.3 kyr BP | no finding; maxima see GB-32 |
| PP-31 | P21 | Period means as unweighted sample means against time-weighted means, because sample density varies within periods | LGM PAT 65.7 and 65.8, NZ 14.2 and 15.3, AUS 10.2 and 9.0; HS1 all within 0.4; MIS3 all within 0.6; Holocene PAT 49.0 and 51.6, AUS 23.1 and 21.7, NZ 5.9 and 4.8 | no finding: no ranking or direction changes; sampling gap and small ACR and YD samples are disclosed |
| PP-32 | P11 | Matrix of periods, PSA and outputs: Table S5, box plots (Figure 3, Figure S4), time series (Figure 1, Figure S3), isotope calculation (Figure 2, Table S3) | EDC and EDML rows have the same 7 PSA columns; EDML lacks Late Holocene and MIS3, consistent with its 7 to 27 kyr BP record | no finding beyond GB-03, GB-23, GB-30, GB-38 |
| PP-33 | P22 | Derived quantities the reader must compute: high- and low-latitude sums, SSA sums, EDC minus EDML differences | Sums and differences stated in the text are listed in PP-40 and PP-43; the composition of a sum is named except in GB-46 | no further finding |
| PP-34 | P34 | Shown selection from counted sets | Table S1 complete for the 241 retained samples; the 38 excluded samples not listed; "three specific REE patterns" out of 39 not named | GB-14, GB-29, GB-30 |
| PP-35 | P29, P3 | Inventory of figures and their citations | Figure 1 cited l. 183, 205, 215, 217, 221, 307, 338; Figure 2 l. 244, 252, 257; Figure 3 l. 281, 295; Figure 4 l. 405, 419; Figure 5 l. 340; Figures S1 to S5 cited l. 127, 167, 355, 382, 405 and further; no graphical abstract | every figure is cited; order see GB-51; wrong targets see GB-35, KK-47 |
| PP-36 | P3 | LGM panel of Figure 3 against Table S1 (n = 40, exclusive quartiles) | PAT 58.90, 65.78, 71.66 (table 58.9, 65.8, 71.7); AUS 5.81, 10.11, 13.99 (5.8, 10.2, 14.0); SAF 1.72, 4.59, 7.60 (1.8, 4.6, 7.6); NZ 10.83, 15.49, 18.87 (10.8, 15.5, 18.9); measurement uncertainty 0.22 | no finding; caption see GB-39, NZ value in the text see GB-47 |

### Segment 4: Discussion, conclusion, references, declarations (pp. 7 to 29)

#### Substantive findings

**GB-41 The EDC Sr-Nd values cited as Delmonte et al. (2004) cannot be traced to the listed reference, and the Holocene values have no source.**

| Field | Content |
|---|---|
| Check | P13 |
| Location | p. 7, l. 238 to 240; p. 17, l. 561 to 564; Supplement Table S4 (page 21), rows Epica dome C, column Reference |
| Quotation | "For instance, Delmonte et al. (2004) reported 87Sr/86Sr ratios of ~0.708 and ε(Nd)"; "more radiogenic 87Sr/86Sr ratios (~0.710) and more negative ε(Nd) values (-4.51 to -5.68). Similar shifts" |
| Concern | The only Delmonte et al. (2004) in the reference list is the Climate Dynamics paper on dust size evidence at Dome B, EDC and Komsomolskaia (l. 561 to 564); its abstract mentions Sr-Nd only qualitatively and gives no values. Table S4 cites the EDC values as "[Delmonte et al., 2004a]", a reference that does not exist in the list. The Holocene values in l. 239 to 240 carry no citation, and Table S4 contains no Holocene EDC values; its Holocene block lists Taylor Glacier and Berkner Island. Since aim (2) (l. 93 to 94) validates the model against Sr-Nd data "published in the literature", the reader must be able to find these data; the consequence for the validation is GB-43. |
| Suggestion | In l. 238 and Table S4 cite the paper that reports the EDC LGM values, with a full entry in the reference list, and in l. 239 to 240 give the source and the core of the Holocene values; if they are not from EDC, say so. |
| Status | verified (reference list p. 17; Table S4 on the page image); inferred (that the Climate Dynamics paper contains no such values, since only its abstract was readable) |
| Severity | moderate |
| Source | S1 |

**GB-42 Figure 2 shows one modelled point per sample, while Section 4.1 describes one calculation per time interval, and its legend uses classes that neither the text nor Table S4 defines.**

| Field | Content |
|---|---|
| Check | P29, P8 |
| Location | p. 8, l. 244 to 246; p. 8, l. 252 to 253; Figure 2 (page 26), legend and solid dots; p. 26, l. 864 |
| Quotation | "For each time interval of the LGIT, the"; "relative contribution of each PSA (CONTR) was multiplied by its average Sr and Nd concentrations,"; "The modeled isotopic signatures for the end of MIS3/LGM, HS1, ACR, and the YD (represented on" |
| Concern | The method in l. 244 to 246 reads as one mixture per interval, which would give six solid points. Figure 2 shows many: isolated dot-shaped spots number at least 23 light red, 25 dark red, 7 cyan, 26 blue and 3 green (lower bounds, since a dense cluster near 0.707 and minus 1 hides further dots), so points are computed per sample. The legend has six solid classes from "EDC Early Holocene" to "EDC LGM"; there is no MIS3 class although l. 252 includes MIS3 in the blue symbols, and "Holocene" next to "Early Holocene" leaves open whether the dark red dots are the Late Holocene or the whole Holocene. The open class "Iso Early Holocene" does not exist in Table S4, which has only "Iso Holocene"; the split into light and dark red open rings (Berkner Island and Taylor Glacier, see GB-43) is not explained. |
| Suggestion | State in l. 244 to 246 that the mixture is calculated for each sample (and, if so, averaged per interval), and define each legend class of Figure 2 in the caption with its age limits and, for the open symbols, its site. |
| Status | verified (legend; counts as lower bounds, by instance AB); inferred (per-sample calculation) |
| Severity | moderate |
| Source | AB, SD |

**GB-43 The validation against Sr-Nd isotopes (aim 2) uses two EDC values, both from the LGM, and for the Holocene only measurements from other sectors of Antarctica, without a measure of agreement.**

| Field | Content |
|---|---|
| Check | P10, P15, P3 |
| Location | p. 8, l. 254 to 260; p. 3, l. 93 to 94; p. 1, l. 25 to 26; p. 7, l. 238 to 240; Figure 2 (page 26), open symbols; p. 26, l. 857 to 858; Supplement Table S4 (page 21) |
| Quotation | "Overall, the close agreement between our modeled isotopic compositions and those measured in EDC"; "for both glacial and interglacial intervals supports the robustness of our DEPOT algorithm and reinforces" |
| Concern | Comparing the model output with an independent tracer is the right idea, and the glacial comparison is plotted correctly (PP-38). Table S4, the source of the open symbols, lists 35 measured values: 2 from EDC (LGM, "Delmonte et al., 2004a"), 1 from "Old Dome C" (HS1), 18 from Taylor Glacier and 14 from Berkner Island. The "Iso Holocene" group holds 22 values, none from EDC (8 Taylor Glacier, 14 Berkner Island); for each Berkner Island value an open ring was found in Figure 2 within 3 px of its tabulated position, while no ring lies at the EDC Holocene values of l. 239 to 240 (about 0.710 with minus 4.51 to minus 5.68). The interglacial agreement is therefore an agreement with Ross Sea and Weddell Sea sector sites, while Section 4.4 argues that the Holocene provenance differs between the Atlantic and Indian Ocean sectors (l. 423 to 428), and the manuscript does not discuss why Berkner Island is a suitable reference for EDC. No agreement measure is defined: the measured Holocene values span εNd minus 2.30 to minus 14.71, so almost any mixture falls within them, and the comparison as designed cannot fail. The finding is major because it changes what the manuscript can show for aim (2) and for the Abstract statement that the transition "is supported by Sr-Nd isotopic calculations" (l. 25 to 26). |
| Suggestion | In Section 4.1 and Figure 2 restrict the validation to measurements on EDC or Dome C dust, including the Holocene values of l. 239 to 240 in Table S4 with their own symbol; calculate isotopes per sample with the Monte Carlo spread for the age intervals of those measurements; define a quantitative agreement measure (residuals in εNd and 87Sr/86Sr against measurement uncertainty) and show that an alternative mixture, for example a constant glacial composition, would fail it. Report Taylor Glacier and Berkner Island separately as regional context, label them by site in the legend, and rephrase l. 258 to 260, for example "those measured in EDC (LGM) and in other Antarctic ice cores (Holocene)". |
| Status | verified (Table S4 on the page image; symbol positions in Figure 2 measured by instance AB; wording); inferred (counts; that the comparison cannot discriminate) |
| Severity | major |
| Source | AB, S4, SD |

**GB-44 The timing of the Patagonian Ice Sheet maximum differs from the cited synthesis.**

| Field | Content |
|---|---|
| Check | P13 |
| Location | p. 8, l. 267 to 269 |
| Quotation | "between ~34 and 29.4 kyr BP, covering much of the Andes with an ice mass 2090 km long and 350 km" |
| Concern | Davies et al. (2020) write that the ice sheet reached its maximum extent by 33 to 28 ka between 38°S and 48°S, and earlier, around 47 ka, south of 48°S; the dimensions 350 km wide and 2090 km long refer to the ice sheet at 35 ka. The values 34 and 29.4 kyr BP were not found in the readable text, and the earlier maximum of the southern sector, closest to the outwash plains discussed in l. 262 to 272, is omitted. |
| Suggestion | In l. 268 write "by 33 to 28 ka between 38°S and 48°S and around 47 ka south of 48°S" and give 2090 km and 350 km as the extent at 35 ka, or cite the source of 34 to 29.4 kyr BP. |
| Status | verified (abstract of Davies et al., 2020, read by instance S1); inferred (that 34 and 29.4 kyr BP are absent from the full text) |
| Severity | minor |
| Source | S1 |

**GB-45 The model studies cited as support for Patagonian dominance attribute most LGM Antarctic dust to Australia, and one of them gives no such estimate.**

| Field | Content |
|---|---|
| Check | P13 |
| Location | p. 8, l. 275 to p. 9, l. 277 |
| Quotation | "Model simulations also support this view, estimating that SSA and AUS"; "(i.e., Albani et al., 2012; Krätschmer et al., 2022)." |
| Concern | "This view" is the significance of Patagonian sources (l. 273). Krätschmer et al. (2022) state that over 90 % of the dust deposited over Antarctica is of Australian or South American origin, but their Table 5 gives for Antarctica at the LGM Australia 1.96 Tg per year (68 %) and South America 0.69 Tg per year (24 %), and their conclusions call Australia the predominant source at the LGM; South American dust reaches up to 40 % only in a smaller region of East Antarctica. The combined share is 92 %, not 70 to 90 %, and the split reverses the ranking found here. Albani et al. (2012) give no model percentage for South American or Australian dust at EDC, Talos Dome or East Antarctica. The claimed independent support is therefore a contradiction that the discussion has to address; the composition of the comparison value "PAT+AUS" is GB-46. |
| Suggestion | Rewrite l. 275 to 277: report the model split (Australia 68 %, South America 24 % of LGM deposition over Antarctica in Krätschmer et al., 2022), state that it contradicts the REE result, and discuss the reasons, for example the source parameterisation of the model or the absence of shelf and outwash sources; remove Albani et al. (2012) from this sentence or cite the passage that gives the value. |
| Status | verified (open-access full texts of Krätschmer et al., 2022, and Albani et al., 2012, read by instance S1); inferred (combined share computed) |
| Severity | moderate |
| Source | S1 |

**GB-46 The sums of high-latitude and "PAT+AUS" contributions use different compositions and do not match Table S5.**

| Field | Content |
|---|---|
| Check | P20, P36 |
| Location | p. 9, l. 276; p. 9, l. 293 to 295; Supplement Table S5 (page 22), rows LGM and HS1 |
| Quotation | "(here, PAT+AUS is ~77%)"; "~79 % of total deposition. Lower-latitude PSAs (AUS, SAF, PAP) supplied the remaining ~21 % (Figure"; "with high-latitude sources totaling 84 %" |
| Concern | From Table S5: LGM PAT plus NZ = 65.7 + 14.2 = 79.9 (text ~79); AUS plus SAF plus PAP = 10.2 + 6.3 + 3.6 = 20.1 (text ~21); HS1 PAT plus NZ = 74.8 + 7.1 = 81.9 (text 84). The HS1 value of 84 is reproduced only by SSA plus NZ (74.8 + 2.0 + 7.1 = 83.9), that is with PAP counted as high latitude, which contradicts l. 294, where PAP is a lower-latitude source. LGM PAT plus AUS = 65.7 + 10.2 = 75.9 (text ~77), while the model estimate it is compared with refers to SSA plus AUS, here 69.3 + 10.2 = 79.5. The deviations of 0.9, 0.9, 2.1 and 1.1 points exceed rounding. The finding is moderate because a reader cannot reproduce the stated sums from the table that is cited for them. |
| Suggestion | Use one composition (PAT plus NZ for high latitude, AUS plus SAF plus PAP for low latitude) and the Table S5 values: LGM 79.9 and 20.1 %, HS1 81.9 %; in l. 276 compare SSA plus AUS (79.5 %) with the 70 to 90 % of the models. |
| Status | inferred (sums computed from Table S5) |
| Severity | moderate |
| Source | S3, SD, S1 |

**GB-47 The average New Zealand contribution in the LGM is given as about 11 % in the Discussion, while Results, Table S5 and Figure 3 give about 14 %.**

| Field | Content |
|---|---|
| Check | P2, P3, P36 |
| Location | p. 9, l. 281 to 282; compare p. 7, l. 208 to 209; Figure 3 (page 27), LGM panel, NZ box; Supplement Table S5 (page 22), row LGM |
| Quotation | "average NZ contribution (~11%), making it the second-largest dust source to EDC during the LGM." |
| Concern | Table S5 gives 14.2 % for the LGM and l. 209 says "an average of 14%". In Figure 3, cited in l. 281, the LGM NZ box measures first quartile 10.83 %, median 15.49 %, third quartile 18.87 %, and the mean cross lies at about 14.0 %. The value of 11 is reproduced only by pooling periods: LGM and HS1 weighted by sample numbers (14.2 x 40 + 7.1 x 27) / 67 = 11.3, or MIS3 and LGM (9.1 x 41 + 14.2 x 40) / 81 = 11.6. With about 11 % the margin to AUS (10.2 %) that carries "second-largest" shrinks to under one point; with 14.2 % it is 4.0. The finding is moderate because the text contradicts the figure and table it cites. |
| Suggestion | Replace "~11%" in l. 282 by "~14%" (Table S5), or name the pooled interval if a pooled value was meant and cite Table S5 instead of Figure 3. |
| Status | verified (values; Figure 3 measured by instance AB); assumption (pooled interpretation) |
| Severity | moderate |
| Source | S3, AB, SD |

**GB-48 Is the New Zealand range of 14 to 32 % a share of trajectories rather than of deposition?**

| Field | Content |
|---|---|
| Check | P13 |
| Location | p. 9, l. 286 to 288 |
| Quotation | "Present-day forward air-mass"; "to inland Antarctic deposition (Neff and Bertler," |
| Concern | The abstract of Neff and Bertler (2015) describes forward trajectories that are independent of deposition processes and states that sources reaching the East Antarctic interior are limited and mixed, while New Zealand and Patagonia supply a high proportion of trajectories to West Antarctica. A share of trajectories has a different denominator from a share of deposition. The values 14 and 32 % could not be located because the full text was not readable. |
| Suggestion | Could the authors give the page or table of Neff and Bertler (2015) with the 14 to 32 %, state the denominator (trajectories or deposition) and the target region (East Antarctic interior or West Antarctica), and rephrase l. 287 accordingly? |
| Status | verified (that the study is independent of deposition, abstract read by instance S1); inferred (meaning of the 14 to 32 %) |
| Severity | moderate |
| Source | S1 |

**GB-49 The Holocene SSA contribution is given as 61 % and five lines later as 60 %.**

| Field | Content |
|---|---|
| Check | P2 |
| Location | p. 10, l. 321 and l. 326; Supplement Table S5 (page 22), row Holocene |
| Quotation | "compared to 61% in our record when combining PAT, CWA, and PAP"; "compared to our SSA estimate of 60% (Table S5)" |
| Concern | Table S5, Holocene: PAT 49.0 + CWA 0.0 + PAP 11.0 = 60.0. The value 61 does not follow from Table S5 (Late Holocene alone gives 62.7, Early Holocene 57.1). |
| Suggestion | Write 60 % in l. 321. |
| Status | verified |
| Severity | minor |
| Source | S3 |

**GB-50 The Potrok Aike record is called a bog in the text but a lake record in Figure 5 and in the cited source.**

| Field | Content |
|---|---|
| Check | P38 |
| Location | p. 10, l. 339 to 340; p. 11, l. 348 to 349; p. 29, l. 881 to 882 |
| Quotation | "Potrok Aike bog (see Figure 5)"; "(Potrok Aike bog 52°S"; "of lacustrine sediments in Laguna Potrok Aike (Lisé-Pronovost et al., 2015)" |
| Concern | The proxy in Figure 5 and the title of the cited reference ("lacustrine sediments of Laguna Potrok Aike", l. 691 to 692) refer to a lake record. The text names the same archive "Potrok Aike bog" twice, which designates a different archive type (peat). |
| Suggestion | Replace "Potrok Aike bog" in l. 339 to 340 by "Laguna Potrok Aike" and "(Potrok Aike bog 52°S" in l. 348 to 349 by "(Laguna Potrok Aike, 52°S". |
| Status | verified (page images pp. 10, 11, 29) |
| Severity | minor |
| Source | S2, S4, AB |

**GB-51 Figure 5 is cited before Figure 4, so the figure numbers do not follow the order of first citation.**

| Field | Content |
|---|---|
| Check | P3 |
| Location | p. 10, l. 340; p. 12, l. 405 |
| Quotation | "Aike bog (see Figure 5)"; "Figures 4 and S5 (for millennial trends)" |
| Concern | First citations: Figure 1 l. 183, Figure 2 l. 244, Figure 3 l. 281, Figure 5 l. 340, Figure 4 l. 405. Figure 5 belongs to Section 4.3, Figure 4 to Section 4.4. The supplementary figures are cited in order. Instance S4 recorded the same order without a finding and left it to the journal style (PP-46); since numbering in order of first citation is the common rule and the swap costs nothing, it is kept as a minor finding. |
| Suggestion | Swap the numbers of Figures 4 and 5 in figures, captions and all citations. |
| Status | verified |
| Severity | minor |
| Source | AB |

**GB-52 Is the drop of PAT between 6 and 6.5 kyr BP really present in the Potrok Aike wind record, as the text says? Panel B of Figure 5 shows no excursion there.**

| Field | Content |
|---|---|
| Check | P3 |
| Location | p. 11, l. 350 to 351; p. 10, l. 339 to 340; Figure 5 (page 29), panel B |
| Quotation | "Apart from a well-marked drop in"; "PAT contributions between 6-6.5 kyr BP (also present in Potrok Aike wind intensity record), strong" |
| Concern | In panel B the bold MDF curve averages 18.2 mT (5.5 to 6.0 kyr), 17.4 mT (6.0 to 6.5 kyr), 16.4 mT (6.5 to 7.0 kyr) and 16.2 mT (7.0 to 7.5 kyr), with a maximum of 18.4 mT within 6.0 to 6.5 kyr, while the whole panel spans about 10 to 55 mT. A change of at most 1.8 mT is not a well-marked counterpart of the PAT drop to 28.5 % at 6.33 kyr in panel A. The original record may resolve a weaker wind phase at finer scale; the figure as printed does not show it. |
| Suggestion | Could the authors give the MDF values of Lisé-Pronovost et al. (2015) for 6 to 6.5 kyr BP that support l. 351 and mark the interval in Figure 5B, or remove the parenthesis if the record does not show it? |
| Status | verified (measurement by instance AB); assumption (that the original record could contain a finer signal) |
| Severity | moderate |
| Source | AB |

**GB-53 South Altiplano dust appears in Table S1 and Figure S3 from 12.84 kyr BP, not only after 11.2 kyr BP as the text states.**

| Field | Content |
|---|---|
| Check | P24 |
| Location | p. 11, l. 358 to 360; Supplement Table S1 (page 13), rows 12841; Supplement Figure S3 (page 6), panel Altiplano |
| Quotation | "Southern Altiplano begins contributing dust only after approximately 11.2 kyr BP, a timing that" |
| Concern | Table S1 has two YD samples at 12841 yr BP with Altiplano 16.6 % and 12.8 %, and the YD mean of PAP in Table S5 (4.5 %) is partly Altiplano (Table S1 YD means: Puna 1.3 %, Altiplano 3.3 %). In Figure S3 the oldest point where the Altiplano line exceeds 2 % lies at 12.85 kyr BP, followed by a raw peak of 38.8 % at 11.85 kyr. The onset thus precedes the date that the text links to the final desiccation of paleolake Coipasa by about 1.6 kyr. The interpretation in l. 358 to 360 rests on this timing, which is why the finding is moderate; the main shift is not affected. |
| Suggestion | Correct l. 358 to "after approximately 12.9 kyr BP (YD), with major contributions after 11.2 kyr BP" and revise the link to the Coipasa desiccation accordingly, or explain why the YD samples are not counted. |
| Status | verified (Table S1; Figure S3 measured by instance AB) |
| Severity | moderate |
| Source | AB |

**GB-54 Seven cited works have no entry in the reference list, among them the sources of more than half of the end-member database and of most measured isotope values, and one entry is never cited.**

| Field | Content |
|---|---|
| Check | P4, P12 |
| Location | p. 11, l. 365; p. 18, l. 630 to 632; Supplement Table S2 (pages 16 to 19), column Reference; Supplement Table S4 (page 21), column Reference |
| Quotation | "with the previous Pb isotopic study (Gili et al., 2016) ."; "Marx and Kamber, 2010"; "[Delmonte et al., 2004a]" |
| Concern | The authors use the main reference list for supplementary citations ("EPICA Community Members, 2006", l. 594, is cited only in the caption of Figure S2), and the supplement has no list of its own. The list has no entry for Gili et al. (2016) (l. 365; only Gili et al., 2017 and 2022), for Marx and Kamber (2010), Marx et al. (2005), McGowan et al. (2005) and Diaz et al. (2018), cited in Table S2, or for Aarons et al. (2017) and Bory et al. (2010), cited in Table S4. Counted in Table S2, these four works supply 101, 10, 2 and 4 patterns, together 117 of 217 (53.9 %); Aarons et al. (2017) and Bory et al. (2010) supply 32 of the 35 measured isotope values of Table S4, the reference values of Section 4.1. "Delmonte et al., 2004a" implies a 2004b; the list has one Delmonte et al. (2004) entry (l. 561), see GB-41. In the other direction, the entry Gaiero, Brunet, Probst and Depetris (2007) (l. 630 to 632) is cited nowhere; the text cites "Gaiero, 2007" (l. 274, l. 862), the single-author entry of l. 619. |
| Suggestion | Add full entries for Gili et al. (2016), Marx and Kamber (2010), Marx et al. (2005), McGowan et al. (2005), Diaz et al. (2018), Aarons et al. (2017) and Bory et al. (2010), or give the supplement its own reference list; change "Delmonte et al., 2004a" in Table S4 to the correct reference; cite Gaiero et al. (2007) where it is meant or delete the entry. |
| Status | verified (citations and entries; rows of Table S2 and Table S4); inferred (share of 53.9 % computed) |
| Severity | moderate |
| Source | S4, S2, SD |

**GB-55 The number of YD samples is given as 7, but Table S1 lists 9 samples in the YD bracket.**

| Field | Content |
|---|---|
| Check | P2, P36 |
| Location | p. 12, l. 407 to 409; Supplement Table S1 (page 13), YD block, rows 11779 to 12867 |
| Quotation | "(8 and 7 samples in ACR and YD," |
| Concern | The YD bracket of Table S1 contains 11779, 11993, 12227, 12477, 12588, 12754, 12841, 12841 and 12867, that is 9 rows; the ACR bracket contains 8 (13032 to 14601), which matches. The YD means of Table S5 are reproduced exactly from these 9 rows, so the means and the stated n disagree. Possible resolutions: the two rows at 12841 yr BP count as one sample (GB-15) and one further row is excluded, or 7 is the count under a stricter threshold (with R ≥ 0.71 exactly 7 YD rows remain, GB-25). The EDML counts (47 and 27) cannot be checked from the manuscript. The finding is moderate because the stated n and the means it qualifies cannot both be right. |
| Suggestion | Correct l. 408 to 9 YD samples, or explain which two rows are not counted and recompute the YD row of Table S5. |
| Status | verified (count on the page image); inferred (resolutions) |
| Severity | moderate |
| Source | S3, SD |

**GB-56 The PAT differences between EDC and EDML for ACR and YD are swapped, and in the YD the SAF difference is positive, not a loss.**

| Field | Content |
|---|---|
| Check | P2, P3 |
| Location | p. 13, l. 421 to 422; Figure 4 (page 28), panels PAT and SAF, bars ACR and YD; Supplement Table S5 (page 22), rows ACR and YD |
| Quotation | "dust (+4 and +6.5%) in EDC, primarily at the expense of Southern African and Australian contributions." |
| Concern | From Table S5, PAT ACR 68.9 minus 62.5 = plus 6.4 and YD 63.1 minus 58.4 = plus 4.7; the bars of Figure 4 measure plus 6.49 (ACR) and plus 4.81 (YD), uncertainty 0.31. The text assigns plus 4 to the ACR and plus 6.5 to the YD. For the compensation: ACR SAF 8.0 minus 12.4 = minus 4.4 and AUS 11.1 minus 18.5 = minus 7.4, consistent with the text; YD SAF 14.6 minus 8.2 = plus 6.4 (bar plus 6.34) and AUS 14.5 minus 19.0 = minus 4.5. In the YD the PAT surplus is balanced by AUS (minus 4.5), NZ (minus 3.9) and PAP (minus 2.4), while SAF is higher in EDC. The finding is moderate because the paragraph explains the regional difference by displaced SAF and AUS dust, which does not hold for SAF in the YD. |
| Suggestion | Correct l. 422 to "(+6.4 and +4.7%)" and state that in the YD the PAT surplus is balanced by AUS, NZ and PAP, while SAF is 6.4 points higher in EDC. |
| Status | verified (differences from Table S5; bars measured by instance AB) |
| Severity | moderate |
| Source | S3, AB, SD |

**GB-57 The Holocene comparison of EDC and EDML subtracts the EDML Early Holocene from the whole EDC Holocene, although the comparison is declared for the common window.**

| Field | Content |
|---|---|
| Check | P21, P3, P5 |
| Location | p. 13, l. 423 to 424; p. 12, l. 405 to 407; Figure 4 (page 28), bars "Holo"; Supplement Table S5 (page 22), rows EDC Holocene, EDC Early Holocene, EDML Early Holocene |
| Quotation | "PAT dust (-14%) but higher contributions of Australian dust (+12%) than EDML."; "between 7.5 and 27 kyr BP." |
| Concern | EDML has only an Early Holocene row in Table S5. The stated differences and all five "Holo" bars of Figure 4 (measured PAT minus 13.97, AUS plus 12.44, SAF minus 0.53, PAP plus 1.48, NZ about plus 0.4) are reproduced by the whole EDC Holocene (2.8 to 11.7 kyr BP) minus the EDML Early Holocene: minus 13.7, plus 12.3, minus 0.5, plus 1.6, plus 0.4. Within the window the text declares (7.5 to 27 kyr BP, l. 406 to 407), that is EDC Early Holocene minus EDML Early Holocene, the differences are PAT minus 15.6, AUS plus 14.1, SAF minus 1.4, PAP plus 0.6, NZ plus 2.6; the measured bars exclude this variant (difference 1.6 to 2.2 points, uncertainty 0.31). The comparison thus includes 60 EDC samples from 2.8 to 7.5 kyr BP without EDML counterpart. The direction of the PAT and AUS differences stays, their size and the NZ difference change. |
| Suggestion | Compute the Holocene differences in l. 423 to 424 and in Figure 4 from the EDC Early Holocene, label the bars "Early Holocene (7.5 to 11.7 kyr BP)" and state the window in the caption of Figure 4; or state that the whole EDC Holocene is compared and why. |
| Status | verified (differences from Table S5; bars measured by instance AB) |
| Severity | moderate |
| Source | S3, AB, SD |

**GB-58 A Law Dome lead pollution study is cited as evidence for Australian mineral dust reaching Antarctica.**

| Field | Content |
|---|---|
| Check | P13 |
| Location | p. 13, l. 438 to 440 |
| Quotation | "significant contributors to both western and eastern Antarctica (De Deccker et al., 2019; Revel-Rolland"; "et al., 2006; Vallelonga et al., 2002)." |
| Concern | Vallelonga et al. (2002), by its title in the list "The lead pollution history of Law Dome, Antarctica, from isotopic measurements on ice cores: 1500 AD to 1989 AD" (l. 807 to 809), reports anthropogenic lead: the 1884 to 1908 pollution event was attributed to lead mined at Broken Hill and smelted at Broken Hill and Port Pirie, while rock and soil dust supplied only about 8 to 12 % of background lead. The paper does not identify Australian regions as mineral dust sources. The lead study of EDC dust by Vallelonga et al. (2010), which is not cited (GB-08), found 66 of 74 EDC samples away from the Australian field. |
| Suggestion | Remove Vallelonga et al. (2002) from l. 440; if the lead evidence is to be used, cite Vallelonga et al. (2010) and discuss its result against the Holocene AUS share of 23 % (Table S5). |
| Status | verified (title in the reference list; abstract of Vallelonga et al., 2002, read by instance S1) |
| Severity | moderate |
| Source | S1 |

**GB-59 Discussion and Conclusion state a causal mechanism with "demonstrate", "confirm" and "due to", where the results show a temporal coincidence and Section 4.2 itself says "likely".**

| Field | Content |
|---|---|
| Check | P15 |
| Location | p. 14, l. 466 to 468; p. 14, l. 480 to 484; compare p. 9, l. 296 to 298 |
| Quotation | "Importantly, our data demonstrate"; "As such those results confirm our previous"; "18 and 15 kyr BP due to changing atmospheric transport dynamics." |
| Concern | The manuscript links the provenance shift to shelf submersion and drainage reversal through coincidence in time with literature records (l. 450 to 462). It does not test the mechanism: neither the exposed shelf area nor river sediment supply enters the model (l. 100 to 172). "Demonstrate" and "confirm" are therefore stronger than the evidence. In Section 4.2 the cause of the flux decline is given as "likely" (l. 296, Markle et al., 2018); the Conclusion turns it into a fact ("due to"). The timing itself is uncertain in EDC (GB-02), and the fluxes that could discriminate the mechanism are not reported (GB-03). The answer to aim (3), a provenance shift coinciding with hydrological and sea-level changes, stands; only the strength of the causal claim changes, hence moderate. |
| Suggestion | In l. 466 replace "our data demonstrate" by "our data are consistent with the hypothesis"; in l. 480 replace "confirm" by "are consistent with"; in l. 484 replace "due to" by "likely due to". |
| Status | verified (wording); inferred (that the mechanism is not tested, from the Methods) |
| Severity | moderate |
| Source | S4 |

**GB-60 The outcome of aim (2), the validation against Sr-Nd isotopes, does not appear in the Conclusion.**

| Field | Content |
|---|---|
| Check | P15 |
| Location | p. 14, l. 472 to p. 15, l. 492; compare p. 3, l. 93 to 94 |
| Quotation | "(2) confronting and validating the EDC results from our REE pattern-based model against Sr-Nd isotopic data published in the literature" |
| Concern | The Abstract cites the isotope check as support (l. 25 to 26), and Section 4.1 is devoted to it, but the Conclusion (l. 472 to 492) contains no statement on isotopes or validation; of the four aims it takes up (1), (3) and (4). |
| Suggestion | Add one sentence to the Conclusion on the outcome of the isotope comparison, phrased within the limits named in GB-43. |
| Status | verified (search for isotope terms in l. 471 to 492) |
| Severity | minor |
| Source | S4 |

**GB-61 The Conclusion explains the EDC and EDML differences by source-area climate, while Section 4.4 explains them by the position of the two sites in the atmospheric circulation.**

| Field | Content |
|---|---|
| Check | P15 |
| Location | p. 14, l. 484 to 487; compare p. 13, l. 424 to 428 and l. 440 to 443 |
| Quotation | "SAF, NZ and AUS differed reflecting regional climatic dynamics in their respective source areas."; "consistent with the geographic positioning of the two sites" |
| Concern | Both cores draw on the same source regions, so a climate change in a source area changes emissions for both and cannot by itself explain why the cores differ. Section 4.4 attributes the differences to EDML lying in the Atlantic storm track and EDC being shielded by the polar vortex (l. 425 to 428), that is to transport. Section 4.4 also invokes increased low-latitude aridity (l. 442 to 443), but as a cause of the larger low-latitude contributions at EDC, not of the difference between the cores. The Conclusion does not take up the transport explanation and states a cause that does not follow from the Discussion. The answer to aim (4), that differences exist, stands, hence moderate. |
| Suggestion | In l. 486 to 487 write, for example, "differed, reflecting the different exposure of the two sites to mid-latitude air masses (storm track versus polar vortex)", in line with l. 424 to 428; if source-area climate is meant to contribute, add the argument to Section 4.4. |
| Status | verified (wording at both places); inferred (that a source-area signal affects both cores) |
| Severity | moderate |
| Source | S4 |

**GB-62 The iron fertilisation framework of the introduction does not return in the Discussion, and the Conclusion claims implications for biogeochemical fluxes without a supporting result.**

| Field | Content |
|---|---|
| Check | P15 |
| Location | p. 15, l. 490 to 492; compare p. 2, l. 37 to 51 |
| Quotation | "Hemisphere dust cycle during the LGIT, with implications for biogeochemical fluxes, atmospheric" |
| Concern | The introduction motivates the study with iron fertilisation, pCO2 and the inter-source variability of iron content and solubility (l. 37 to 51; Qu, 2016; Shi et al., 2009, 2011, 2015). The Discussion (l. 219 to 470) does not mention iron, solubility or biogeochemical fluxes again. The closing sentence of the Conclusion therefore has no basis in the results or the discussion, and the motivation set out in the introduction is not answered. |
| Suggestion | Add a paragraph to Section 4 that states what the reconstructed change in the PSA mix implies for iron delivery or solubility, at least qualitatively and with the cited iron studies, or shorten l. 491 to 492 and the motivation in l. 49 to 51 accordingly. |
| Status | verified (search for "iron", "solubility" and "biogeochem" in l. 219 to 492, repeated in the merge, finds only l. 491) |
| Severity | moderate |
| Source | S4 |

**GB-63 The author contribution statement names "P.B", which matches none of the authors.**

| Field | Content |
|---|---|
| Check | P38 |
| Location | p. 16, l. 497; compare p. 1, l. 4 to 5 |
| Quotation | "P.B performed the measurements; A.V., St. B and G.L. developed" |
| Concern | The authors are S. Boxho, A. Vanderstraeten, N. Mattielli, G. G. Laruelle, A. Bory, P. Gabrielli and S. Bonneville; no author has the initials P.B. The statement also uses "Si.B", "St. B" and "St.B." for two authors. Because it does not say which measurements are meant (the EDC REE data of 2010 or the six new SAF samples, GB-12), the person responsible for new data cannot be identified. P.G. (Paolo Gabrielli) is a plausible reading. |
| Suggestion | Correct the initials in l. 497 (please check whether "P.G." is meant), use one form per author ("Si.B.", "St.B."), and name the measurements concerned. |
| Status | verified (no author with the initials P.B); assumption (intended author) |
| Severity | minor |
| Source | S2, S4 |

**GB-64 The reference list prints raw RTF escape sequences in 18 entries and mixes several entry formats.**

| Field | Content |
|---|---|
| Check | P16 |
| Location | p. 16, l. 528; p. 17, l. 553 to 556, l. 584 to 588, l. 590 to 593; p. 18, l. 606, l. 632 to 636, l. 645 to 648, l. 653 to 654; p. 19, l. 693 to 694, l. 703 to 710; p. 20, l. 714 to 716, l. 732, l. 742 to 747, l. 757 to 758; p. 21, l. 795 to 799; p. 21, l. 817 to p. 22, l. 828; p. 22, l. 844 to 846 |
| Quotation | "Mall\uc0\u237{}n Pollux, Coyhaique, Province Ais\uc0\u233{}n"; "Ding, Q., Steig, E., Battisti, D. et al. Winter warming in West Antarctica caused by central tropical" |
| Concern | The page images show the escape codes as printed text: "\uc0舑{}" in place of an en dash in page ranges, "\uc0舗{}" for an apostrophe, codes for í, é, ñ, for degree, minute and second signs, and a trailing backslash after many DOIs. Counted in the merge, 18 of the 91 entries are affected (Bullard and McTainsh 2003; De Deckker et al. 2014; Dukes et al. 2018; Engelbrecht et al. 2019; Fletcher and Moreno 2012; Gaiero et al. 2007; Gingele and De Deckker 2005; Grousset and Biscaye 2005; Lisé-Pronovost et al. 2015; Markgraf et al. 2007; Markle et al. 2018; Moreno et al. 2010; Power et al. 2008; Quade and Kaplan 2017; Stone et al. 2010; Stuut et al. 2002; Veres et al. 2013; Wagner et al. 2021). The formats also differ: year at the end and "et al." in the author list (Ding, l. 584 to 585); year in parentheses and initials before the surname (Gaiero et al. 2013, l. 633 to 636); "&" and "(2024)" (Yang, l. 844); a chapter number "6." in the title (Delmonte et al. 2007, l. 565); "doi: https://" (Placzek, l. 732); the Gaiero entries are not in chronological order. |
| Suggestion | Regenerate the reference list from the reference manager in one style (authors with initials, year, title, journal, volume, pages, DOI), replace each escape sequence by its character, remove the trailing backslashes and order the Gaiero entries. |
| Status | verified (page images pp. 16 to 22; count of entries with escape codes rechecked in the merge) |
| Severity | minor |
| Source | S4 |

**GB-65 Figure 5 has no x-axis title, unit or scale factor, and its blue band, dashed lines and grey zones are not explained.**

| Field | Content |
|---|---|
| Check | P29 |
| Location | p. 29, l. 880 to 882; Figure 5 (page 29), panels A and B |
| Quotation | "Figure 5: Comparison of the contribution of Patagonian dust (PAT) to EDC ice core (A) and (B) the" |
| Concern | The x axes carry the numbers 0.5 to 3 only; unlike Figure 1 there is neither "Time (yr BP)" nor "x10^4". The blue band bounded by dashed lines spans 7.95 to 11.45 kyr BP, which corresponds to the weakening of the westerlies from 11 to 8 kyr BP in l. 340, but neither caption nor legend says so. The grey zones are not explained, and in panel B the YD zone ends at 13.03 kyr against 12.88 kyr in panel A. The legend entries "Raw data" and "smoothed" exist only in panel A. |
| Suggestion | Add "Time (yr BP)" and the scale factor to the x axes, explain the blue band, the dashed lines and the grey zones in the caption, and align the grey zones of both panels. |
| Status | verified |
| Severity | minor |
| Source | AB |

**GB-66 The y axes of Figure S2 carry no units, and panel B has no period zones.**

| Field | Content |
|---|---|
| Check | P29 |
| Location | Supplement Figure S2 (page 4), panels A, B and C; caption (page 3) |
| Quotation | "(A) Non Sea Salt Calcium (nssCa2+) flux in EDC ice core (Fischer et al., 2007)" |
| Concern | The axis titles read "nssCa2+ flux", "δ18O" and "deuterium excess" without units; l. 166 gives the flux unit (µg m⁻² yr⁻¹), and the per mil unit of the isotope panels is not given anywhere in the figure. Panel B has no grey period zones, unlike panels A and C. |
| Suggestion | Add the units (µg m⁻² yr⁻¹; ‰ VSMOW) to the three axis titles and the period zones to panel B. |
| Status | verified |
| Severity | minor |
| Source | AB |

#### Minor corrections

| ID | Location | Quotation | Replacement | Source |
|---|---|---|---|---|
| KK-26 | p. 7, l. 220 | "provenance in the Epica" | "provenance in the EPICA" | S2 |
| KK-27 | p. 8, l. 246 | "(Table S3, e.i. Eq.3)" | "(Table S3; Eq. 3)" | S4, SD |
| KK-28 | p. 8, l. 249 | "where the mean isotopic signatures is represents by CIR PSA" | "where CIR PSA represents the mean isotopic signature of each PSA" | S4 |
| KK-29 | p. 8, l. 261 | "Persistance of high-latitude dust source to EDC before 14.5 kyr BP" | "Persistence of high-latitude dust sources to EDC before 14.5 kyr BP" | S4 |
| KK-30 | p. 8, l. 270 | "expanding Patagonian outwash plains by ~763.10" | "expanding Patagonian outwash plains by ~763 × 10³ km²" (printed as "~763.10³ km²") | S4 |
| KK-31 | p. 8, l. 272 | "those from SSA- to EDC" | "those from SSA, to EDC" | S4 |
| KK-32 | p. 9, l. 300 | "before 14.5 kyr BP reflect a transport regime" | "before 14.5 kyr BP reflects a transport regime" | S4 |
| KK-33 | p. 9, l. 301 | "strong westerlies -a system that" | "strong westerlies, a system that" | S4 |
| KK-34 | p. 10, l. 311 | "«wet scavenging»" | "“wet scavenging”" (as "rainout" in l. 297) | S4 |
| KK-35 | p. 10, l. 325 to 326 | "reduction in SSA input -down to 33%-" | "reduction in SSA input (down to 33%)" | S4 |
| KK-36 | p. 10, l. 329 to 330 | "includes several McMurdo region sites (Section" | "includes several McMurdo region sites (Section 2; Table S2)" (Section 4.2 does not treat the McMurdo sites) | S4 |
| KK-37 | p. 10, l. 334 | "(Speirs et al., 2001)" | "(Speirs et al., 2010)" (entry in l. 781) | S4 |
| KK-38 | p. 10, l. 339 to 341 | "The 11 to 8 kyr BP period corresponds to a weakening of South Westerlies" | define at first use in l. 339 ("the Southern Westerly Winds (SWW) intensity proxies") and write "a weakening of the SWW" in l. 340 to 341 | S2, S4 |
| KK-39 | p. 10, l. 341 | "Moreno et al. (2010);" | "Moreno et al., 2010;" | S4 |
| KK-40 | p. 10, l. 342 | "(Quake and" | "(Quade and" (entry in l. 755; correct in l. 349) | S4 |
| KK-41 | p. 10, l. 346 | "Fires co-emit mineral soil-dust particle" | "Fires co-emit mineral soil-dust particles" | S4 |
| KK-42 | p. 11, l. 354 | "Dust emission from PAP are primarily linked" | "Dust emissions from PAP are primarily linked" | S4 |
| KK-43 | p. 11, l. 366 | "As far as Australian dust contribution, our model" | "As for the Australian dust contribution, our model" | S4 |
| KK-44 | p. 11, l. 367 | "De Deccker et al. (2010)" | "De Deckker et al. (2010)" | S4 |
| KK-45 | p. 11, l. 374 | "(post-7.5 kry" | "(post-7.5 kyr" | S2, S4 |
| KK-46 | p. 11, l. 376 | "El-Nino-Southern Oscillation (ENSO)" | "El Niño Southern Oscillation (ENSO)" | S4 |
| KK-47 | p. 12, l. 382 | "(Figure S4), which is" | "(Figure S3; Table S5), which is" (Figure S4 has no Holocene time series; the SAF sub-region series are in Figure S3) | S4, AB |
| KK-48 | p. 12, l. 384 to 385 | "suggesting strengthened dust transport from southern Africa suggesting strengthened dust transport from southern Africa (Stuut et al., 2002)" | "suggesting strengthened dust transport from southern Africa (Stuut et al., 2002)" | S4 |
| KK-49 | p. 12, l. 396 | "but include few substantial inputs" | "but include a few substantial inputs" | S4 |
| KK-50 | p. 12, l. 397 to 398 | "during the LGIT (~15.4"; "BP (Brook et al., 2011)." | "during the LGIT (~15.4 to 13.6, ~11.5 to 8.4 and ~5.5 to 4.0 kyr BP; Brook et al., 2011)." (the first parenthesis is never closed) | S4 |
| KK-51 | p. 12, l. 399 | "likely reflect their low-frequency, high-magnitude nature of their dust emissions" | "likely reflect the low-frequency, high-magnitude nature of their dust emissions" | S4 |
| KK-52 | p. 12, l. 408 | "due to the limited number samples" | "due to the limited number of samples" | S4 |
| KK-53 | p. 13, l. 426 | "well positioned to receive dust from Patagonia dust brought in the mid-" | "well positioned to receive Patagonian dust brought in the mid-" | S4 |
| KK-54 | p. 13, l. 427; p. 10, l. 331 | "located at the interior of EAP" | "located in the interior of the EAP" in l. 427, and "over the East Antarctic Plateau (EAP)" at first use in l. 331 | S2, S4 |
| KK-55 | p. 13, l. 428 | "from such mid-latitude air masses incursions" | "from such incursions of mid-latitude air masses" | S4 |
| KK-56 | p. 13, l. 439 | "(De Deccker et al., 2019;" | "(De Deckker, 2019;" (single-author entry in l. 551) | S4 |
| KK-57 | p. 13, l. 442 | "(Ding et al., 2011) - and increased aridity" | "(Ding et al., 2011), and increased aridity" | S4 |
| KK-58 | p. 14, l. 457 | "redirecting large portion of river catchment from the Atlantic" | "redirecting a large portion of the river catchments from the Atlantic" | S4 |
| KK-59 | p. 14, l. 466 | "atmospheric transport from low-latitude to Antarctica" | "atmospheric transport from low latitudes to Antarctica" | S4 |
| KK-60 | p. 14, l. 481 | "study on the EDML dust record showing similar shift" | "study on the EDML dust record showing a similar shift" | S4 |
| KK-61 | p. 16, l. 501 | "APPENDIX S. SUPPLENTARY DATA. Supplementary data to this article" | "APPENDIX S. SUPPLEMENTARY DATA. Supplementary data to this article are provided in the Supplement." | S4 |
| KK-62 | p. 16, l. 536 | "Las glaciaciones cuaternarios en la Patagonia" | "Las glaciaciones cuaternarias en la Patagonia" (agreement with "glaciaciones"; please check against the original title) | S4 |
| KK-63 | p. 20, l. 726 to 729 | "chronology for the EPICA Dome C ice core. Clim. Past." | "chronology for the EPICA Dome C ice core. Clim. Past 3, 485-497." with the author order of the source (Parrenin, Barnola, Chappellaz and others) | S4 |
| KK-64 | p. 20, l. 748 | "Environùental characterization" | "Environmental characterization" | S4 |
| KK-65 | p. 20, l. 762 to 763 | "Rudnick, R.L., Gao, S., 2003. 01 Composition of the Continental Crust. In Treatise on Geochemistry" | "Rudnick, R.L., Gao, S., 2003. Composition of the continental crust. In: Rudnick, R.L. (Ed.), The Crust, Treatise on Geochemistry, Vol. 3, Holland, H.D., Turekian, K.K. (Eds.). Elsevier-Pergamon, Oxford, 1-64." | S4 |
| KK-66 | p. 21, l. 800; compare p. 8, l. 266 | "Sudgen, D. E., McCulloch, R. D." | "Sugden, D. E., McCulloch, R. D." (the text cites "Sugden et al., 2009") | S4 |
| KK-67 | p. 26, l. 863 | "Note that the SAF and AUS domain is more extended than showed in the Figure." | "Note that the SAF and AUS domains extend beyond the plotted range." | S4, AB |
| KK-68 | Figure 2 (page 26), x axis; Figure 3 (page 27) and Supplement Figure S4 (page 8), y axes | "0,700"; "100,00" | "0.700"; "100" (decimal point as in the text, no superfluous decimals) | AB |
| KK-69 | p. 28, l. 875 | "Histograms representing the contribution percentage difference" | "Bar charts of the difference in contribution percentage" (the panels show one bar per period, not a frequency distribution) | S4, AB |
| KK-70 | Supplement Figure S5 (page 10), y-axis title | "PAS EDC Contribution and PSA EDML Contribution ( in %)" | "PSA EDC contribution and PSA EDML contribution (%)" | AB |

#### Verification log

| ID | Check | Checked | Values | Result |
|---|---|---|---|---|
| PP-37 | P15 | Verbs of the Discussion against the evidence | l. 237 "appears to be consistent"; l. 259 "supports"; l. 296 and l. 308 "likely reflects"; l. 339 "is matching well" (Figure 5, qualitative); l. 350 "probably explaining"; l. 399 "likely reflect"; l. 424 "are consistent with" | no finding beyond GB-43 and GB-59 |
| PP-38 | P3 | Open symbols of Figure 2 against Table S4 for LGM, HS1, ACR and YD | Rings found within 5 px of all 13 calculated positions; blue rings at the two EDC LGM values (0.7086 and minus 1.66; 0.7088 and minus 2.46) | no finding for the glacial groups; Holocene see GB-43 |
| PP-39 | P13 | p. 9, l. 277 to 279 and l. 291 to 292; p. 10, l. 324 to 328: Coppo et al. (2022) | Published version not openly accessible; its abstract names the Puna-Altiplano as main source of fine Pampean loess and minimum loess accumulation in the early LGM; 64 + 15 + 11 + 5 + 5 = 100 (l. 278 to 279) | no finding; limit: the percentages for LGM and Holocene could not be checked in the source |
| PP-40 | P1 | Discussion values derived from Table S5 | Holocene AUS, PAP, SAF 23.1, 11.0, 10.7 ("23%, 11% and 11 %", l. 317); LGM 10.2, 3.6, 6.3 ("10%, 4% and 6%"); Holocene PAT, NZ 49.0, 5.9 ("49% and 6%", l. 319); LGM SSA 69.3 ("~70%"), AUS 10.2 ("~10%", l. 281); LGM PAP 3.6 ("~4 %", l. 289); LGM order NZ 14.2, AUS 10.2, SAF 6.3, PAP 3.6 (l. 222 to 223) | no finding; deviations see GB-46, GB-47, GB-49 |
| PP-41 | P24 | Figure S2 against l. 296, l. 299 and l. 312 | Smoothed nssCa2+ flux 601 (18.5 to 19 kyr), 578 (18 to 18.5), 444 (17.5 to 18), 158 (15.5 to 16), 40 (14.5 to 15) in the unlabelled axis unit; δ18O rises between about 18 and 14.5 kyr; deuterium excess binned means 7.32 (12 to 13 kyr), 7.41 (11 to 12), 8.51 (10 to 11), 9.03 to 9.59 (3 to 10 kyr) | no finding; units see GB-66 |
| PP-42 | P13 | p. 10, l. 319 to 323: DustCOMM values from Kok et al. (2021) | Kok et al. (2021), Table 2, Antarctica: South America 71 (50 to 90) %, Australia 18 (6 to 36) %, southern Africa 8 (3 to 13) %; text about 70, 20, 10 % | no finding; "10% (ranging from 3% to 13%)" combines the rounded text value with the table range |
| PP-43 | P1, P15, P3 | Differences between EDC and EDML for LGM, HS1, ACR and YD (l. 417 to 422, Figure 4) against Table S5 | LGM NZ 14.2 minus 6.2 = plus 8.0 ("+8%"), PAT 65.7 minus 73.7 = minus 8.0 ("equivalent reduction"); HS1 largest difference SAF 4.9 minus 10.2 = minus 5.3 ("not exceeding ~5%"); bars measured PAT plus 4.81, plus 6.49, plus 3.13, minus 8.17 for YD, ACR, HS1, LGM (table plus 4.7, plus 6.4, plus 3.2, minus 8.0); NZ minus 3.99, plus 3.16, about plus 0.5, plus 7.72 (minus 3.9, plus 3.4, plus 0.6, plus 8.0); uncertainty 0.31; EDML rows of Table S5 sum to 99.9 to 100.0 | no finding for LGM and HS1; ACR, YD and Holocene see GB-56, GB-57; origin of the EDML values see GB-07 |
| PP-44 | P15 | Every statement of the Conclusion assigned to a result | (1) first continuous record, l. 472 to 473: GB-01. (2) MIS3, LGM, HS1 dominated by PAT and NZ, l. 474 to 477: PAT plus NZ 79.4, 79.9, 81.9 %, consistent. (3) shift from about 14.5 kyr BP, l. 477 to 480: GB-02. (4) "confirm" EDML, l. 480 to 482: GB-59. (5) decoupling from the flux decline 18 to 15 kyr BP, l. 482 to 484: Figure S2A shows the flux falling before the provenance change, consistent; cause GB-59. (6) EDML comparison, l. 484 to 487: GB-61. (7) sea level, drainage reversals, paleolake desiccation, l. 488 to 490: Sections 4.3 and 4.4. (8) implications, l. 490 to 492: GB-62 | statements (2), (5) and (7) no finding |
| PP-45 | P15, P9 | Outlook: proposals, recommendations, planned follow-up work | Conclusion (l. 471 to 492) and Discussion searched for "future", "should", "need": no proposal, recommendation or planned work | no finding (nothing to test) |
| PP-46 | P4 | Numbering of sections, equations, figures and tables, and the first citation of each | Sections 1 to 5 with 4.1 to 4.4 (l. 33, 99, 173, 219, 232, 261, 305, 402, 471): no gap; Equations 1 to 4: no gap; Figures 1 to 5 all cited, Figure 5 before Figure 4; Tables S1 to S5 all cited, Table S4 only in figure captions and there wrongly | GB-19, GB-51 |
| PP-47 | P4 | Content of the targets of the remaining cross-references | l. 192 Table S5 (PAT 70.3, 65.7, 74.8); l. 216 PAP Holocene 11.0; l. 281 and l. 294 Figure 3 and Table S5; l. 296, l. 299, l. 312 Figure S2 panels A to C; l. 340 Figure 5; l. 355 Figure S3; l. 310 Section 4.2; l. 405 Figures 4 and S5; l. 873 Figure S4 (HS1, ACR, YD boxes present) | no finding beyond GB-19, KK-24, KK-36, KK-47 |
| PP-48 | P4 | Citations against the reference list in both directions, and short forms against entries | 91 entries; two-author entries all cited with "and"; single-author entries Bryant 2003, Caldenius 1932, De Deckker 2019, EPICA 2006, Gaiero 2007, Qu 2016, of which only De Deckker 2019 is cited with "et al."; year mismatch Speirs 2001 and 2010; spellings Sugden and Sudgen, Quake and Quade, De Deccker and De Deckker (twice); citations without entry: 1 in the main text, 6 in the supplement; entries without citation: 1 | GB-54, KK-37, KK-40, KK-44, KK-56, KK-66 |
| PP-49 | P16 | Uniformity of the reference list | Author format "Surname, Initials" except Ding 2011, Gaiero et al. 2013 and Yang 2024; DOI present except Parrenin 2007, Rudnick and Gao 2003, Qu 2016 (thesis); alphabetical order kept except the Gaiero entries (2007, 2003, 2004, 2007, 2013) | GB-64, KK-63, KK-65 |
| PP-50 | P16 | Language and typesetting of pp. 7 to 22 and 24 to 29 on the page images; extraction artefacts excluded | Every minor correction confirmed on the page image. Not raised because they appear only in the extracted text: subscripts in Eq. 3 and 4 (p. 8) and the superscripts of 87Sr/86Sr, set correctly on the image. The RTF codes of GB-64 are visible on the image | KK-26 to KK-70, GB-64 |
| PP-51 | P29 | Font size of Figure 4 | Tick labels 18 to 19 px = 6.0 to 6.3 pt, category labels 19 px = 6.3 pt | no finding |
| PP-52 | P13 | Literature statements collected but not checked against their sources | Koffman et al. (2021) (l. 283), Williams et al. (2015) (l. 286), NZ shelf about 62,000 km² and outwash area from Vanderstraeten et al. (2023) (l. 270, l. 284), Blard et al. (2011), Placzek et al. (2006), Markle et al. (2018), Stenni et al. (2010), Fletcher and Moreno (2012), Lisé-Pronovost et al. (2015), Quade and Kaplan (2017), Magee et al. (2004), Brook et al. (2007, 2011), Burrough et al. (2009), Franchi et al. (2022), Speirs et al. (l. 333 to 334), Nguyen et al. (2019), Weber et al. (2014) | not checked; limit of this review |
| PP-53 | P1 | Merge: mandatory fields and discards (ZF) | 94 substantive findings, 112 minor corrections and 58 verification log entries from six instances; every finding had all mandatory fields, an allowed check, status, severity and source; 0 findings discarded. 94 findings became 66: 24 findings combine two or more instance findings; SD-GB-11 and SD-GB-14 were split by subject into 4 and 5 parts. 32 minor corrections went into findings, 80 into 66 rows, plus 4 from notes (ZF). Severity of merged findings is the highest of the merged ones; where a part of a bundled finding raised a numerical mismatch to moderate, the concern says why | no finding |
| PP-54 | P2 | Merge: pairs with overlapping location (ZF) | The pair list of the format check (281 pairs: 89 sharing Table S1 as first element, 18 Table S2, 4 Tables S4 or S5, 14 a figure, 156 overlapping lines) was worked through before and after numbering, and each pair was decided. Merged into one finding before numbering: findings on the same statement or cell, for example the time span with the corrections of l. 90 to 91 and l. 304 (GB-09), Potrok Aike bog (GB-50), table numbering (GB-19), Eq. (1) (GB-17), author initials (GB-63), the Table S1 caption (GB-14). Kept separate because the subject differs at the same place: GB-09 and GB-10 with KK-11 (l. 90); GB-45 and GB-46 (l. 276); GB-07 with GB-56 and GB-57 (EDML origin against arithmetic and windows); GB-12 and GB-27 (documentation against location data of the six new rows of Table S2); GB-15 and GB-55 (duplicate ages against the YD count); GB-25 and GB-29 (significance of the threshold against selection on the outcome); GB-34 and GB-53 (Altiplano values against onset); GB-41, GB-42 and GB-43 (source of values, description of Figure 2, validation design); GB-50, GB-51, GB-52 and KK-38 (l. 339 to 351); GB-59, GB-60, GB-61, KK-59 and KK-60 (l. 466 to 487); GB-01 and GB-60 (l. 472); GB-08, GB-28, GB-30 and KK-36 (l. 329 to 334); GB-21, GB-30 and KK-43 (l. 366); GB-27, GB-30 and KK-49 (l. 386 to 398); GB-58 and KK-56 (l. 439); GB-61 and KK-57 (l. 442); GB-55 and KK-52 (l. 408); GB-37 with KK-21 to KK-24 and KK-69 (captions). All other pairs concern different statements that share a large table, a figure or a cited range | 0 further merges; decisions as listed |
| PP-55 | P1, P2 | Merge: wording and numbers rechecked against the manuscript (ZF) | Every quotation searched in the extracted text of manuscript and supplement (values in figures and the decimal commas of KK-68 on the page images); line numbers checked against the printed margin numbers, page image p. 11 viewed; Table S1 re-parsed (241 rows) and Table S5, R statistics, spacings, duplicates, threshold sensitivity, ACR shares, Mann-Whitney tests, SAF, Altiplano and Puna values recomputed; Table S2 re-parsed (217 rows: PAT 39, CWA 5, PAP 14, SAF 23, AUS 107, NZ 25, ANT 4), duplicates, references, size fractions, ANT step sizes and distances recomputed. Corrected on the way: count of reference entries with escape codes 19 to 18 (GB-64); line of KK-42 353 to 354; in GB-07 the clause that Table S5 contradicts the abstract on southern Africa, restricted to the YD; in GB-61 the clause that the Discussion does not develop source-area climate, restricted (l. 442 to 443 invoke aridity); in GB-02 the statement on the first values below the glacial range, replaced by the per-sample values | no finding of its own; corrections as listed |
| PP-56 | P1 | Merge: notes outside the checklists (ZF) | 61 notes from the six instances (S1 11, S2 11, S3 8, S4 15, AB 10, SD 6). 54 match findings or corrections already raised by a responsible instance (S2 note 9 only in part). 3 notes gave 4 new minor corrections after checking the page or text: KK-13 (l. 128) and KK-14 (Table S2 header) from S2 note 11, KK-23 (l. 853) from AB note 9, KK-24 (l. 873) from S3 note 7. 4 notes not taken up: panel alignment in Figures 1, S2 and S5 and the missing y axes in panels 2 to 5 of Figure S4 (AB notes 7 and 8; the responsible instance AB reviewed the figures and kept them as notes); the exclusion rates of EDML and EDC (SD note 6; the comparison relies on a source abstract); the 6-point difference to Coppo et al. (2022) called a close match (S3 note 5; no tolerance is defined, a matter of wording). Also not taken up: Darling12 at 138°17'6.00"E, 572 km west of Darling11 (part of S2 note 9; a possible entry error that cannot be confirmed without the source) | as listed |
| PP-57 | P13 | Engelbrecht et al. (2019) abstract, rechecked in the merge for GB-05 | Abstract (asu.elsevierpure.com): downscaling of eight LGM simulations to 8 km over southern Africa, cooler temperatures, frontal rainfall reaching farther north, altered rainfall seasonality; no mention of the westerlies | GB-05 kept, severity minor, wording softened |

## Optional checks

| Area | What it needs | Responsible | Run |
|---|---|---|---|
| DOI resolution | one retrieval per reference entry with DOI | `science-quellenapparat-pruefung` | no |
| Citation style | the name of the style | `science-zitierstil-harvard-ctr` or the style rules of the journal | no |
| AI statement against publisher policy | the policy of the target publisher | this review, on request | no |
| Relation to the authors' own earlier work | the earlier work of the authors | this review, on request | no |
| Journal requirements | the author guidelines of the target journal | this review, on request | no |
| Technical correctness | access to the sources of the checked statements and a selection of sections | `science-faktenbeleg-pruefung`, `geo-frage-belegbasiert-klaeren` | no |

## Limits of this review

- Checked version: egusphere-2025-5046.pdf, 29 pages, SHA-256 f598b53d01e375844cfb549eb05b9a3407bb30cae553e603c125d5f14886c722, with egusphere-2025-5046-supplement.pdf, 22 pages, SHA-256 759cfa14195948f5772d3d6d696081932424f4296e51c812415527ed3b108ea6
- Unreadable sources: full texts of Delmonte et al. (2004, 2008, 2017), Coppo et al. (2022), Neff and Bertler (2015), Engelbrecht et al. (2019), Davies et al. (2020), Marino et al. (2008) and Vanderstraeten et al. (2023), of which only abstracts or records were read; the percentages of Revel-Rolland et al. (2006); the code repository record of Vanderstraeten et al. (2023); the literature statements listed in PP-52 were not checked
- Findings with status assumption: 0 of 66 with assumption as the central status; 14 of 66 contain a sub-statement with status assumption, each posed as a question or offered as one of several readings
- Optional checks run: 0 of 6
- Dropped instances: none
- Discarded findings: 0 (of 94 instance findings; all had the mandatory fields and survived the recheck; four clauses and one line number were corrected, see PP-55, and one wording softened, see PP-57)
