# Review report: Quantifying Southern Hemisphere dust sources during the Last Glacial-Interglacial Transition using rare earth elements in the EPICA Dome C ice core

| Field | Value |
|---|---|
| Manuscript | Boxho, S., Vanderstraeten, A., Mattielli, N., Laruelle, G. G., Bory, A., Gabrielli, P. and Bonneville, S. (2025) Quantifying Southern Hemisphere dust sources during the Last Glacial-Interglacial Transition using rare earth elements in the EPICA Dome C ice core. EGUsphere preprint egusphere-2025-5046, https://doi.org/10.5194/egusphere-2025-5046 |
| Checked version | egusphere-2025-5046.pdf, 29 pages, SHA-256 f598b53d01e375844cfb549eb05b9a3407bb30cae553e603c125d5f14886c722; supplement egusphere-2025-5046-supplement.pdf, 22 pages, SHA-256 759cfa14195948f5772d3d6d696081932424f4296e51c812415527ed3b108ea6 |
| Date | 2026-10-18 |
| Language | English |
| Review instances | Segments 1 to 4 (S1 to S4), Figures (AB), Study design (SD); the six review instances ran as separate agents; no instance omitted |
| Note | Line numbers are the printed margin numbers of the manuscript. The supplement has no line numbers; locations there are given as "Suppl. p." with table, row, column or panel. |

## Summary

The manuscript re-analyses a published rare earth element (REE) dataset of the EPICA Dome C (EDC) ice core (Gabrielli et al., 2010) with the authors' non-negative least-squares unmixing model DEPOT to quantify the contributions of Southern Hemisphere potential source areas (PSA) to EDC dust between 33.7 and 2.9 kyr BP. Of 294 samples, 15 are excluded for missing data and 279 are fitted against a database of 217 UCC-normalised dust source patterns (DS) grouped into seven PSA (Patagonia, Central Western Argentina, Puna-Altiplano, Southern Africa, Australia, New Zealand, Antarctica), using 13 REE after removal of Gd, element-specific correction factors for acid leaching and 2000 Monte Carlo runs per sample; 241 samples with a median fit correlation R ≥ 0.67 form the record. Patagonia supplies 70.3, 65.7 and 74.8 % on average in MIS3, the LGM and HS1 and 49.0 % in the Holocene, while Australia rises from about 10 % to 23.1 % (Table S5). The apportionment is checked against Sr and Nd isotope data by back-calculation (Eq. 3 and 4), compared with the authors' EDML record, and the shift after about 14.5 kyr BP is attributed to Patagonian shelf submersion and river reorganisation.

## Strengths

1. The unmixing is specified as an explicit numerical procedure (Eq. 1 and 2, 217 DS, 13 REE, Monte Carlo, R per sample) and the supplement gives per-sample PSA medians, so the record can be recomputed: all EDC period means of Table S5 are reproduced from the 241 rows of Table S1 to within 0.1 points, the mean R of 0.852 and the sample balance 294, 279, 241 close (PP-11, PP-25, PP-29).
2. The isotope back-calculation (Eq. 3 and 4) adds an independent geochemical check: period means of Table S1 with the end-members of Table S3 give 0.7083 and εNd -2.62 for the LGM and 0.7101 and -4.99 for the Holocene, close to the EDC values the authors cite, and individual modelled points of Figure 2 are reproduced to 0.0001 (PP-37); what this check can establish is limited by GB-37.
3. The manuscript discloses its main data limitations where they arise (sampling gap of 21.7 to 27.3 kyr BP with four samples, 15 incomplete patterns, Gd removal, 38 samples below the fit threshold with their cause, tentative ACR and YD results), which lets a reader verify them: the four gap samples and the exclusion counts are confirmed in Table S1 (PP-11, PP-21).
4. Several figures are drawn exactly from the tabulated values, which makes them checkable: the 25 bars of Figure 4 reproduce the Table S5 differences to within 0.3 points, the LGM panel of Figure 3 matches the Table S1 statistics, and the period shading of Figure 1 matches the stated boundaries (PP-26, PP-33, PP-39).

## Weaknesses

1. The accuracy of the apportionment itself is not established: DEPOT is not tested on mixtures of known composition with 13 equations and 217 end-members, the Antarctic end-members appear not to be UCC-normalised, two Australian end-members are duplicated, the significance attached to the R threshold does not hold, and the Holocene record is selected by fit quality at the lowest concentrations (GB-13, GB-15, GB-19, GB-20, GB-23). Suggestion: add a recovery test with synthetic mixtures and noise at Holocene levels, correct the database, and report Monte Carlo intervals per sample.
2. The timing and the cause of the provenance shift are stated more strongly than the analysis supports: the shift at the ACR onset rests on 8 and 9 samples without a test, the Conclusion "demonstrate" and "confirm" a mechanism that is shown only by temporal coincidence, the Conclusion names another cause of inter-core differences than Section 4.4, and the isotope validation for interglacials uses measurements from other ice cores (GB-36, GB-37, GB-46, GB-48). Suggestion: add a change-point analysis with uncertainty, rephrase the causal verbs, and show the EDC Holocene isotope data with their own symbol.
3. The EDC versus EDML comparison (aim 4) is not reproducible as written: the EDML averages of Table S5 disagree with the cited EDML record and with Figure S5, the Holocene bars compare unequal intervals, the ACR and YD values are swapped, and no difference carries an uncertainty (GB-06, GB-44, GB-45). Suggestion: document one EDML series, compare matching intervals and give intervals for each difference.
4. Many numbers and references cannot be traced: code, input concentrations, correction factors and excluded samples are not available, several text values disagree with Table S1 and Table S5, Figure S3 and the sub-regional statements disagree with Table S1, absolute fluxes and Monte Carlo spreads are announced but not shown, and several cited works lack reference entries (GB-09, GB-16, GB-18, GB-28, GB-38, GB-42). Suggestion: deposit code and inputs, reconcile every text value with the tables, and complete the reference list.

## Findings by segment

### Segment 1: Abstract, Introduction, State of research (p. 1 to 3)

#### Substantive findings

**GB-01 The time span of the record is given with three different end points.**

| Field | Content |
|---|---|
| Check | P2 |
| Location | p. 1, l. 18; p. 3, l. 90 to 91; p. 6, l. 182; p. 9, l. 303 to 304 |
| Quotation | "the EPICA Dome C (EDC) ice core from 33.7 to 2.9 kyr BP" (p. 1, l. 18); (p. 3, l. 90 to 91) "during the LGIT from 33.6 kyr to 2.8 kyr BP"; (p. 9, l. 303 to 304) "from 14.5 kyr BP until 2.7 kyr BP" |
| Concern | The Abstract and the Results (p. 6, l. 182) agree with Table S1, whose first and last retained samples are 2852 and 33699 yr BP, and with the dataset span in p. 4, l. 109 to 110 (first and last row of Table S1, Suppl. p. 11 and 15). The Introduction gives 33.6 and 2.8 kyr BP, Section 4.2 gives 2.7 kyr BP; 33.699 and 2.852 round to 33.7 and 2.9 at one decimal, so neither value matches. If 2.8 kyr BP in p. 3, l. 91 is meant as the period limit used for the Holocene in p. 6, l. 187 and Table S5, the text does not say so. |
| Suggestion | Use "33.7 to 2.9 kyr BP" in p. 3, l. 90 to 91 and p. 9, l. 304, or state that 2.8 kyr BP is the period limit of Table S5. |
| Status | verified |
| Severity | minor |
| Source | S3, SD |

**GB-02 The priority claim of the Abstract is broader than the restricted claims of the Discussion and Conclusion and is contradicted by quantifications the manuscript itself cites.**

| Field | Content |
|---|---|
| Check | P28 |
| Location | p. 1, l. 19 to 20; p. 3, l. 74 to 76; p. 7, l. 220 to 221; p. 12, l. 403 to 404; p. 14, l. 472 to 473 |
| Quotation | "Using a statistical unmixing algorithm on 241 samples, we quantify for the first-time contributions from key Southern Hemisphere dust sources." (p. 1, l. 19 to 20); (p. 7, l. 220 to 221) "we present the first continuous and quantitative record of dust provenance in the Epica Dome C ice core"; (p. 14, l. 472 to 473) "This study presents the first high-resolution, continuous and quantitative reconstruction of dust provenance in the EDC ice core" |
| Concern | The Discussion and Conclusion restrict the priority claim to a continuous, quantitative record at EDC, which is a defensible scope; two searches by S1 found no earlier continuous quantitative record for EDC (PP-02). The Abstract sentence carries no such restriction, although the manuscript itself reports earlier quantifications of these contributions: the authors' EDML record (p. 3, l. 77 to 81), the Sr-Nd based LGM estimate of Coppo et al. (2022) with "64% from SSA, 15% from Antarctica, 11% from AUS, 5% from SAF, and 5% from NZ" (p. 9, l. 277 to 279), its Holocene estimate (p. 10, l. 324 to 328) and the DustCOMM estimate (p. 10, l. 319 to 323). None of the five claims states how the literature was searched: search of text.json, p. 1 to 22, for "search", "database", "Web of Science", "Scopus", "Google Scholar", "literature review" gives no statement of a literature search ("database" 2 hits, both the dust source database, p. 4, l. 126 and p. 10, l. 329; "search" only inside "Research" in journal titles). In the same sentence "first-time" is hyphenated as an adjective. |
| Suggestion | Restrict the Abstract sentence (p. 1, l. 19 to 20) to the scope of p. 7, l. 220 to 221, for example "we provide the first continuous, quantitative record of source contributions at EDC", write "for the first time" without hyphen, and either state the basis of the priority claims in the Introduction (after p. 3, l. 87) or soften them to "to our knowledge". |
| Status | verified (wording at page images p. 1, 3, 7, 12, 14; earlier quantifications as reported in the manuscript; absence of a search statement by the search above); inferred for the content of Coppo et al. (2022), whose full text was not accessible (abstract only, https://boa.unimib.it/handle/10281/393168) |
| Severity | moderate |
| Source | S1, ZF |

**GB-03 Two background statements of the Introduction are attributed to sources on a different archive or region.**

| Field | Content |
|---|---|
| Check | P13 |
| Location | p. 2, l. 36 to 40; p. 2, l. 51 to 52 |
| Quotation | "Over recent decades, studies on these ice cores have revealed the connection between dust fluxes, ocean export productivity, and the development of deep glaciations" (p. 2, l. 36 to 38); (p. 2, l. 51 to 52) "changes in Southern Hemisphere westerly winds, which play a crucial role in atmospheric and oceanic circulation (Engelbrecht et al., 2019)." |
| Concern | (1) The connection is attributed to "studies on these ice cores" but supported only by Martínez-García et al. (2014), whose abstract reads "In a sediment core from the Subantarctic Atlantic, we measured foraminifera-bound nitrogen isotopes"; the ice core side is not cited. (2) Engelbrecht et al. (2019) is a regional downscaling of LGM climate over southern Africa; its abstract does not mention the Southern Hemisphere westerlies. Whether its full text supports the general statement could not be checked: is a different source intended? |
| Suggestion | In p. 2, l. 36 to 40 write "studies on marine sediment cores" for Martínez-García et al. (2014) or add the ice core studies meant; in p. 2, l. 52 cite a source on the westerlies and their role in circulation, or restrict the sentence to what Engelbrecht et al. (2019) show. |
| Status | (1) verified (abstract, published version, via https://collaborate.princeton.edu/en/publications/iron-fertilization-of-the-subantarctic-ocean-during-the-last-ice-/); (2) inferred (abstract only, via https://asu.elsevierpure.com/en/publications/downscaling-last-glacial-maximum-climate-over-southern-africa/), formulated as a question |
| Severity | minor |
| Source | S1 |

**GB-04 The upper bound of "~20 to 40 ppmv" for the dust-driven pCO2 reduction is not found in the two cited studies.**

| Field | Content |
|---|---|
| Check | P13 |
| Location | p. 2, l. 40 to 42 |
| Quotation | "Enhanced iron delivery by atmospheric dust during glacial periods are modelled to have lowered the atmospheric pCO2 by ~20 to 40 ppmv, accounting for a significant portion of the glacial-interglacial pCO2 difference (Lambert et al., 2015; Lambert et al., 2021)." |
| Concern | The sentence rightly states that the effect is modelled and accounts for part of the difference. The numbers do not match the sources: Lambert et al. (2015) give a centennial reduction below 10 ppm "followed by a further ~10 ppm reduction over millennial timescales" and in the Key Points "Iron fertilization reduced LGM atmospheric CO2 levels by 20 ppm"; Lambert et al. (2021) give "between 12 and 29 ppmv" for global-scale fertilisation and "a total atmospheric CO2 reduction of 18.5 ppmv" for the four HNLC regions. The largest value in the two sources is 29 ppmv, 11 ppmv below the stated bound (Python: 40 - 29 = 11). Is 40 ppmv taken from a further study? GB-03 concerns the attribution of the preceding sentence; here the numbers. The grade is moderate because a reader cannot trace the motivating value to the cited sources; the results are not affected. |
| Suggestion | In p. 2, l. 41 replace "~20 to 40 ppmv" by the range of the cited sources ("~10 to 30 ppmv" or "~20 ppmv"), or add the source of the upper bound. |
| Status | verified (Lambert et al., 2015, full text, published version, https://agupubs.onlinelibrary.wiley.com/doi/full/10.1002/2015GL064250; Lambert et al., 2021, full text, published version PDF, https://boa.unimib.it/retrieve/e39773b7-1d77-35a3-e053-3a05fe0aac26/Lambert_2021_EPSL_Dust-iron-CO2.pdf) |
| Severity | moderate |
| Source | S1 |

**GB-05 The factor "up to 25 times" is cited from Delmonte et al. (2008, 2017), but it stems from Lambert et al. (2008), where it is an average factor.**

| Field | Content |
|---|---|
| Check | P13 |
| Location | p. 2, l. 62 to 63 |
| Quotation | "during interglacial periods where dust fluxes are up to 25 times lower than LGM fluxes (e.g. Delmonte et al., 2008; Delmonte et al., 2017)." |
| Concern | Lambert et al. (2008), cited in p. 2, l. 36 and l. 46, report "an average increase in dust flux by a factor of about 25" and "the observed 25-fold increase in glacial dust flux over all eight glacial periods". The abstracts of the two cited works contain no such factor (Sr-Nd provenance at EPICA Dome C and Vostok; dust size sorting at Dome B). "Up to" also turns an average into a maximum. Do the full texts of Delmonte et al. (2008, 2017) contain the factor? |
| Suggestion | In p. 2, l. 63 write "about 25 times lower on average than glacial fluxes" and cite Lambert et al. (2008), or give the page in Delmonte et al. (2008, 2017) where the factor appears. |
| Status | verified for Lambert et al. (2008) (full text, published version, https://epic2-clone.awi.de/18052/1/Lam2007b.pdf); inferred for the absence in Delmonte et al. (2008, 2017) (abstracts only, https://boa.unimib.it/handle/10281/6594 and https://boa.unimib.it/handle/10281/156340) |
| Severity | minor |
| Source | S1 |

**GB-06 The EDML averages of Table S5, on which the EDC versus EDML comparison rests, do not match the EDML record as summarised in the Introduction, as reported in the cited source and as plotted in Figure S5.**

| Field | Content |
|---|---|
| Check | P13 |
| Location | p. 3, l. 77 to 83; p. 1, l. 27 to 29; p. 13, l. 417 to 424; Suppl. p. 22, Table S5, EDML block, rows Early Holocene, YD, ACR, column PAT; Figure 4 (p. 28), panel PAT; Suppl. p. 10, Figure S5, panel PAT |
| Quotation | "being predominantly composed of Patagonian dust, up until ~14.5 kyr BP when a sudden drop in Patagonian contribution (below 50% on average) was evidenced" (p. 3, l. 78 to 80); (p. 13, l. 423 to 424) "EDC appears to receive substantially less PAT dust (-14%) but higher contributions of Australian dust (+12%) than EDML" |
| Concern | The Introduction renders Vanderstraeten et al. (2023) faithfully: its abstract states that Patagonia "dropped below 50 % on average" at about 14.5 kyr BP and that the early Holocene Patagonian contribution was "still prevalent, at ~50 % on average". The EDML block of Table S5 gives PAT 62.5 % (ACR), 58.4 % (YD) and 62.7 % (Early Holocene), all above 50 %. Figure S5, whose caption cites Vanderstraeten et al. (2023), agrees with the source, not with Table S5: tracing the EDML curve in the PAT panel gives about 51.0 % (Early Holocene), 43.8 % (YD) and 49.6 % (ACR), while the same procedure reproduces the EDC rows of Table S5 within 6 points. The comparison in p. 13, l. 417 to 424 and Figure 4 uses the Table S5 values. With EDML values as reported in the source the picture changes: Early Holocene 47.1 - 50 = -2.9 instead of about -15, ACR at least 68.9 - 50 = +18.9 and YD at least 63.1 - 50 = +13.1 instead of a "slight enrichment" (Python). Possible resolutions: (a) EDML was recalculated with the present setup (217 DS, 13 REE, p. 5, l. 143 to 145), which the text does not say and which would make the Introduction describe a different record; (b) the values were transcribed from the source and then contradict it; (c) a different averaging was used for EDML. Which applies? The grade is major because aim (4) and the Abstract statement on regional variations (p. 1, l. 27 to 29) depend on these differences. GB-44 and GB-45 concern how the comparison is computed from Table S5; this finding concerns the EDML values themselves. |
| Suggestion | State in Section 2 (after p. 5, l. 172) how the EDML averages of Table S5 were obtained, use one EDML series in Table S5, Figure S5 and Figure 4, recompute p. 13, l. 417 to 424, and adapt p. 3, l. 77 to 83 and p. 1, l. 27 to 29 to that series. |
| Status | verified for the source statements (abstract of Vanderstraeten et al., 2023, via https://marineinfo.org/doc/publication/382930; full text not accessible), the manuscript text (page images p. 3 and 13) and the Table S5 values (Suppl. p. 22); inferred for the Figure S5 values (pixel tracing by S1); assumption for the cause (cases a to c), formulated as a question |
| Severity | major |
| Source | S1 |

**GB-07 Two studies that bear on the Holocene provenance at EDC and on the dismissal of Antarctic sources are missing from the reference list.**

| Field | Content |
|---|---|
| Check | P14 |
| Location | p. 3, l. 91 to 93; p. 10, l. 330 to 334; p. 13, l. 438 to 440; Suppl. p. 21, Table S4, column Reference |
| Quotation | "throughout the LGIT and particularly during the Holocene for which there is no consensus" (p. 3, l. 92); (p. 10, l. 330) "our results do not indicate significant Antarctic contributions to EDC." |
| Concern | The manuscript frames the Holocene provenance as unsettled. Two studies that constrain this result are not in the reference list (p. 16, l. 502 to p. 22, l. 846; "Vallelonga" only as Vallelonga et al. 2002 and as co-author; "Aarons" 0 hits in main text and list): (1) Vallelonga, P. et al. (2010) Lead isotopic compositions in the EPICA Dome C ice core and Southern Hemisphere Potential Source Areas. Quaternary Science Reviews 29, 247-255, https://doi.org/10.1016/j.quascirev.2009.06.019: on the same core (74 samples, 2 to 217 kyr BP), the samples that indicate more than 50 % input from a local Antarctic dust source correspond to interglacial periods, against negligible Antarctic input here (p. 10, l. 330). (2) Aarons, S.M. et al. (2017) Dust composition changes from Taylor Glacier (East Antarctica) during the last glacial-interglacial transition: A multi-proxy approach. Quaternary Science Reviews 162, 60-71, https://doi.org/10.1016/j.quascirev.2017.03.011: REE and Sr-Nd over the same transition, concluding on a change to a local Ross Sea source in the early Holocene; its isotope data are used in Table S4 without a reference entry. GB-15 concerns a possible artefact behind the same Antarctic result; GB-01 the time span stated in p. 3, l. 90 to 91, next to the aims. |
| Suggestion | Add both studies to the reference list and discuss them in p. 3, l. 91 to 93 and p. 10, l. 330 to 334, stating why the REE model result differs from the Pb isotope evidence of Vallelonga et al. (2010) for the same core. |
| Status | verified (Vallelonga et al., 2010, full text, published version PDF, https://bpcrc.osu.edu/sites/default/files/2020-12/QSR%20Vallelonga%202010.pdf; Aarons et al., 2017, full text, published version PDF, https://byrd.osu.edu/sites/default/files/2020-12/Aarons_et_al_QSR_2017.pdf; absence from the reference list by search in text.json) |
| Severity | moderate |
| Source | S1 |

#### Minor corrections

| ID | Location | Quotation | Replacement | Source |
|---|---|---|---|---|
| KK-01 | p. 1, l. 15 | "Dust deposits in ice cores provides a valuable archive" | "Dust deposits in ice cores provide a valuable archive" | ZF |
| KK-02 | p. 1, l. 20 | "During the Marine isotope 3 (MIS3)" | "During Marine Isotope Stage 3 (MIS3)" (form of p. 6, l. 184); GB-02 concerns the priority claim of the preceding sentence | S2, ZF |
| KK-03 | p. 1, l. 27; p. 3, l. 77 | "Comparison with the EDML ice core"; "Our results for EDML ice core" | define at first use: "Comparison with the EPICA Dronning Maud Land (EDML) ice core" (search "Dronning", p. 1 to 15 and 23 to 29: 0 hits); GB-06 concerns the EDML values at the same places | S2 |
| KK-04 | p. 2, l. 40 to 41 | "Enhanced iron delivery by atmospheric dust during glacial periods are modelled" | "Enhanced iron delivery by atmospheric dust during glacial periods is modelled"; GB-03 and GB-04 concern the sources and numbers of the same passage | ZF |
| KK-05 | p. 2, l. 62 | "high altitude site such as EDC where dust fluxes is low" | "high-altitude sites such as EDC, where dust fluxes are low"; GB-05 concerns the factor in the following line, GB-23 uses the same passage as context | ZF |
| KK-06 | p. 3, l. 88 | "our ‘DEPOT’ model - to the REE pattern dataset measured - in the EPICA Dome C" | "our ‘DEPOT’ model to the REE pattern dataset measured in the EPICA Dome C" | ZF |
| KK-07 | p. 3, l. 90 | "in the Indian Ocean sector of the East Antarctica" | "in the Indian Ocean sector of East Antarctica"; GB-01 concerns the time span of the same sentence | ZF |

#### Verification log

| ID | Check | Checked | Values | Result |
|---|---|---|---|---|
| PP-01 | P28 | Gap and controversy statements, p. 1 to 3 and their repetitions on p. 7, 12, 14; search of text.json p. 1 to 22 for "first", "novel", "only", "no consensus", "not been", "no study", "never", "unprecedented" | "novel" p. 1, l. 17; "first-time" p. 1, l. 19; "first" p. 3, l. 74, p. 7, l. 220, p. 14, l. 472; "only continuous" p. 12, l. 403; "no consensus" p. 3, l. 92; "not been", "no study", "unprecedented", "never": 0 | priority claims see GB-02; "no consensus" is a controversy statement backed by three citations: no finding under P28 (missing literature see GB-07) |
| PP-02 | P28 | Own searches whether the priority claim is evidently false (three searches by S1) | Revel-Rolland et al. (2006): abstract qualitative; Coppo et al. (2022): abstract without percentages; Gili et al. (2022) via DOI: no EDC-specific percentages | no earlier continuous quantitative record for EDC found; restricted claims of p. 7 and p. 14 stand; no finding beyond GB-02 |
| PP-03 | P13 | Lambert et al. (2008) for p. 2, l. 34 to 36 and l. 44 to 46 | source (full text, https://epic2-clone.awi.de/18052/1/Lam2007b.pdf): "the sources and lifetime of dust are the main factors controlling the high glacial dust input"; manuscript: "the geographic location of dust sources and the residence time of dust in the atmosphere" | no finding; the paraphrase narrows "sources" to their location without changing the role assigned |
| PP-04 | P13 | Remaining citation statements of Segment 1 without numbers or rankings: p. 2, l. 47 to 49; p. 2, l. 53 to 55; p. 2, l. 64 to 67 | not opened (no number, ranking or valuation taken from the sources) | no finding; not checked against the sources |
| PP-05 | P13 | Gabrielli et al. (2010) and Wegner et al. (2012) for p. 3, l. 72 to 74 | Gabrielli et al. (2010), full text: 294 samples, 2.9 to 33.7 kyr BP, spacing about 60 yr (Holocene) to 140 yr (glacial), no quantitative apportionment; Wegner et al. (2012), abstract https://cp.copernicus.org/articles/8/135/2012/: "at decadal to centennial resolution" | no finding |
| PP-06 | P10 | Gaps of research against the four aims (p. 3, l. 91 to 98) | gap "could not fully resolve dust provenance" (p. 3, l. 73 to 74) and "no consensus" (p. 3, l. 92) lead to aim 1; isotope limits (p. 2, l. 60 to 68) to aims 1 and 2; spatial variability to aim 4; aim 3 without a stated gap beyond the EDML hypothesis (p. 3, l. 83 to 87) | no finding beyond GB-39 and GB-47 |
| PP-07 | P13 | Vanderstraeten et al. (2023) for p. 3, l. 77 to 87 | abstract (https://marineinfo.org/doc/publication/382930): "relatively uniform up until 14.5 kyr BP", "dropped below 50 % on average", "Early Holocene dust composition is highly variable" | Introduction consistent with the source abstract; conflict with Table S5 see GB-06 |
| PP-08 | P14 | Contribution in one sentence and six literature searches for missing work (S1) | candidates: Vallelonga et al. (2010) and Aarons et al. (2017), not in the list: proposed; Delmonte et al. (2013), full text read, no conclusion for inner sites: rejected; Gili et al. (2022), Revel-Rolland et al. (2006), Coppo et al. (2022), Paleari et al. (2019), Delmonte et al. (2020): in the list, no proposal | see GB-07 |

### Segment 2: Material, Methods, Appendix (p. 3 to 5, Supplement Table S2, Figure S1)

#### Substantive findings

**GB-08 Six PSA end-members are labelled "this study" without any description of sampling or analysis.**

| Field | Content |
|---|---|
| Check | P19 |
| Location | p. 4, l. 104 to 105; p. 4, l. 126; Suppl. p. 17, Table S2, rows EtoshaL1, EtoshaL2, EtoshaL3, EtoshaL4, SuksesL, Sossusvlei, column Reference |
| Quotation | "literature reported patterns from known potential source areas (PSA)" (p. 4, l. 105); "this study" |
| Concern | The text presents the database as compiled literature data (p. 4, l. 105 and 126). Table S2 (page image Suppl. p. 17) lists 6 of the 23 SAF end-members as "this study", "< 5 µm", i.e. primary data. Sampling, size separation, digestion and measurement of these samples are described nowhere: search of p. 1 to 15 and 23 to 29 for "this study" gives 2 hits (p. 7, l. 220; p. 14, l. 472), neither about PSA samples. SAF contributions (YD 14.6 %, Holocene 10.7 %) and the Etosha interpretation (p. 12, l. 395 to 398) may rest on them. |
| Suggestion | In Section 2 (p. 4, l. 126 to 133) state that six SAF end-members are new and describe sampling, size fraction, digestion, instrument and quality control, or cite where they are published. |
| Status | verified |
| Severity | moderate |
| Source | SD |

**GB-09 The data availability statement covers neither the DEPOT code nor the input data, correction factors, excluded samples and DS-level results that the Methods and Discussion use.**

| Field | Content |
|---|---|
| Check | P12, P8, P34 |
| Location | p. 4, l. 107 to 109; p. 4, l. 114; p. 4, l. 118 to 125; p. 5, l. 140; p. 5, l. 155 to 158; p. 6, l. 174 to 175; p. 6, l. 196 to 197; p. 11, l. 366 to 367; p. 12, l. 386 to 387; p. 16, l. 494 to 496 |
| Quotation | "All data needed to evaluate the conclusions in the paper are present in the paper and/or the Supplementary Materials. Additional data related to the paper may be requested from the authors." (p. 16, l. 494 to 496); (p. 5, l. 139 to 140) "This was implemented using the lsqnonneg function in MATLAB." |
| Concern | The supplement gives the PSA database (Table S2), the isotope end-members (Table S3), ice-core isotope values (Table S4), period averages (Table S5) and per-sample PSA medians (Table S1), which covers the PSA side of the fit. Held against the Methods, the following are neither in paper nor supplement (supplement read in full, 22 pages) nor accounted for in the statement: (1) the DEPOT code (MATLAB lsqnonneg plus Monte Carlo wrapper, version, tolerances, seed); the heading says "CODE/DATA" but the text has no sentence on code; (2) the EDC REE input concentrations of the 294 samples (p. 4, l. 107 to 109), cited only to Gabrielli et al. (2010), which names no repository; (3) the cf_i values and their spread used in the Monte Carlo runs (p. 4, l. 118 to 125; p. 5, l. 157 to 158; supplement search for "correction", "cfi", "leach", "digest": 0 hits), and the element-specific analytical uncertainties, given only as "between 2% and 10%" (p. 5, l. 155 to 156); Gabrielli et al. (2010) report recovery fractions of acid leaching but, as read, no correction factors, so the origin of the cf_i is unclear; (4) the identity of the 15 incomplete and 38 below-threshold samples (Table S1 lists only the 241 retained ones); (5) DS-level results, so that the three Valdes Peninsula patterns (p. 6, l. 196 to 197), "the Darling sub-basin as the dominant source region" (p. 11, l. 366 to 367) and the Namibian coast DS "detected most frequently" (p. 12, l. 386 to 387) cannot be checked. "Additional data ... may be requested" is offered without a reason; none of these data concern persons. The normalisation of the medians is treated in GB-34, the Monte Carlo spread in GB-16, absolute fluxes in GB-18. |
| Suggestion | In the CODE/DATA AVAILABILITY section (p. 16, l. 494 to 496) state for each item where it is published (repository with DOI) or why not; deposit the MATLAB code with Monte Carlo settings, the 279 input patterns with the cf_i and element uncertainties and their origin, the list of the 15 plus 38 excluded samples with ages and R, and a table of DS-level selection frequency and median contribution per period; name the three Valdes DS in p. 6, l. 196 to 197. |
| Status | verified (statement, absence from paper and supplement, Table S1 row count 241); inferred (absence of a repository and of correction factors in Gabrielli et al. (2010), full text read through fetch and summary tools by S2 and SD at https://bpcrc.osu.edu/sites/default/files/2020-12/QSR%20Gabrielli%202010.pdf) |
| Severity | moderate |
| Source | S2, SD |

**GB-10 The stated sample spacing of 60 to 140 years is contradicted by the ages in Table S1, which also contains four duplicated ages.**

| Field | Content |
|---|---|
| Check | P36 |
| Location | p. 4, l. 110 to 111; Suppl. p. 11 to 15, Table S1, column "Time [yr]", rows 3559, 10511, 12841, 28709 |
| Quotation | "with an average temporal resolution of approximately 100 years, ranging from 60 to 140 years between adjacent samples" |
| Concern | Table S1 holds 241 of the 294 samples, so spacings in the full set can only be smaller. Of the 240 adjacent spacings in Table S1, 77 are below 60 yr and 60 above 140 yr (Python), also outside the disclosed gap of 21.7 to 27.3 kyr BP. The mean (33699 - 2852)/293 = 105 yr agrees with "approximately 100 years". Gabrielli et al. (2010) give about 60 yr in the Holocene and about 140 yr in the glacial, two typical values rather than a range. Four ages occur twice with different compositions (3559, 10511, 12841, 28709 yr): are these replicates, adjacent depths with equal ages or transcription errors? Timing statements and the 9-step moving averages depend on these ages. |
| Suggestion | In p. 4, l. 110 to 111 give the spacing distribution per period, and explain the four duplicated ages in the caption of Table S1. |
| Status | verified (ages in Table S1, page images Suppl. p. 11 and 13); inferred (spacing counts, Python; content of Gabrielli et al. (2010) via summary of the full text) |
| Severity | moderate |
| Source | SD |

**GB-11 Samples are dated on EDC3, the period boundaries come from the AICC2012 paper, and the other series have no stated timescale.**

| Field | Content |
|---|---|
| Check | P7 |
| Location | p. 4, l. 111; p. 6, l. 187 to 188; p. 21, l. 817 to p. 22, l. 821; p. 13, l. 444 to 445 |
| Quotation | "The age model follows the EDC3 chronology (Parrenin et al., 2007)." (p. 4, l. 111); (p. 6, l. 188) "(Veres et al., 2013)" |
| Concern | The data are on EDC3; the period boundaries are cited from Veres et al. (2013), whose title in the reference list names "The Antarctic ice core chronology (AICC2012)" and whose abstract recommends AICC2012 for EDC. Whether the boundaries were transferred to EDC3 is not said. The EDML record, nssCa2+, δ18O, deuterium excess and the Potrok Aike series (p. 10, l. 338 to 340) have no stated timescale, although synchronous changes are claimed (p. 13, l. 444 to 445). 29 of 241 samples lie within ±300 yr of the boundaries 11.7, 12.9, 14.7, 18 and 29 kyr BP, among them 6 of the 9 YD and 3 of the 8 ACR samples (Python); their assignment depends on the timescale. GB-10 concerns the sample spacing on the same line; here the timescale. How large is the EDC3 to AICC2012 offset in this interval? |
| Suggestion | In Section 2 state the timescale of every series; either transfer all to AICC2012 or justify EDC3 and convert the boundaries; report how many samples change period and recompute Table S5. |
| Status | verified (citations, timescale statements; Veres et al. (2013) abstract read by SD at https://cp.copernicus.org/articles/9/1733/2013/); inferred (counts near boundaries); assumption (size of the effect), formulated as a question |
| Severity | moderate |
| Source | SD |

**GB-12 The measured REE concentration carries three symbols, and the Monte Carlo step cites Eq. (1) as the minimised function although Eq. (2) is the objective.**

| Field | Content |
|---|---|
| Check | P38 |
| Location | p. 4, l. 125; p. 4, l. 137 to 138; p. 5, l. 141; p. 5, l. 147; p. 5, l. 155 to 159 |
| Quotation | "by solving the system of matrixes (Eq.2) with non-negativity constraints" (p. 4, l. 137 to 138); (p. 5, l. 157) "In each MC simulation, cfi and Dusti values were randomly selected following normal distributions"; (p. 5, l. 159) "by minimizing Eq. (1)" |
| Concern | The order of operations is stated (Gd removal, cf_i correction, UCC normalisation, fit). The symbols do not follow it: the measured concentration is the acid-leaching REE_i in Eq. 1 (l. 125), DIC_La to DIC_Lu in Eq. 2 (l. 141), the "dust ice core (DIC) sample" pattern in l. 147 and Dust_i in l. 156 to 157. A reader cannot tell whether Dust_i is the leached concentration or the corrected, normalised value entering Eq. 2, which decides how the Monte Carlo perturbation acts. Eq. (1) defines cf_i as a ratio and contains nothing to minimise. GB-09 concerns the missing cf_i values; here the notation. |
| Suggestion | Use one symbol for the measured leached concentration and one for the corrected, normalised vector (for example DIC_i = cf_i Dust_i / UCC_i), write this relation as an equation near p. 4, l. 125, and change "minimizing Eq. (1)" in p. 5, l. 159 to "minimizing Eq. (2)". |
| Status | verified (page images p. 4 and 5) |
| Severity | minor |
| Source | S2, S4, SD |

**GB-13 DEPOT is not shown to recover known contributions with 13 equations and 217 end-members.**

| Field | Content |
|---|---|
| Check | P31 |
| Location | p. 4, l. 126 to 133; p. 5, l. 142 to 152; p. 2, l. 64 to 65; Suppl. p. 16 to 19, Table S2, columns Type of sample and Location |
| Quotation | "the input matrix- comprising “n” rows (one for each UCC-normalized REE) and 217 columns (one for each dust source sample, DS)- is multiplied by a vector of 217 components" (p. 5, l. 142 to 144); (p. 5, l. 151 to 152) "Sources with CDS equal to 0 are excluded from the fit, indicating no detectable contribution to that specific DIC sample." |
| Concern | The method is specified as a non-negative least-squares problem, which makes the issue visible. With 13 equations and 217 unknowns the columns are necessarily linearly dependent, so different CDS vectors can produce the same fitted pattern; a zero coefficient marks a DS the solver did not pick, not "no detectable contribution". The Introduction criticises isotopes for overlapping fields (p. 2, l. 64 to 65), but overlap of the REE fields of the seven PSA is not tested. Search of p. 1 to 15 and 23 to 29 and of the supplement for "synthetic", "artificial", "unique", "recover": 0 hits; "known" 1 hit (p. 4, l. 105, "known potential source areas"), not a test. The method refers to Vanderstraeten et al. (2023), which used 14 elements; the change to 13 is not tested. Two design features could bias the apportionment (questions): (a) the database is unbalanced, AUS has 107 of 217 DS and ANT 4 (page images Suppl. p. 17 to 19), while the text gives "106 DS" and "5" (p. 4, l. 131 to 133); (b) size fractions differ, with all 100 "< 90µm" entries from AUS next to "< 5µm" and "Aeolian dust" entries elsewhere; search of p. 1 to 15 for "grain", "size fraction", "µm", "micron": no hit concerning PSA material. GB-08 concerns the undocumented new SAF rows of the same table; here the design of the fit. The grade is major because every provenance number rests on DEPOT. |
| Suggestion | Add to Section 2 a recovery test: synthetic mixtures from Table S2 with known proportions, the DS used removed from the matrix, noise at glacial and Holocene analytical levels, refit and error per PSA; repeat with a database balanced by subsampling AUS; report the range of PSA totals among near-optimal solutions. Correct the counts in p. 4, l. 131 to 133 to "AUS; 107 DS" and "ANT; 4 DS". Is a size criterion applied to the "< 90µm" AUS material? |
| Status | verified (matrix dimensions, absence of a recovery test by search, database counts on page images); inferred (non-uniqueness, a consequence of 13 equations and 217 unknowns); assumption (bias from imbalance and size fraction), formulated as questions |
| Severity | major |
| Source | SD |

**GB-14 Supplement tables are cited under the wrong number in four places.**

| Field | Content |
|---|---|
| Check | P38, P4 |
| Location | p. 4, l. 127; p. 26, l. 858; p. 26, l. 865; p. 28, l. 876 |
| Quotation | "(Figure S1, and Table S1). This" (p. 4, l. 127); (p. 26, l. 858) "(refs. Table S1, - open symbols)"; (p. 26, l. 865) "the isotopic fingerprint (Table S4)"; (p. 28, l. 876) "between EDC and EDML ice cores (Table S4)." |
| Concern | Each supplement table has one content: Table S1 per-sample results, Table S2 PSA database, Table S3 Sr and Nd values of the PSA end-members, Table S4 measured ice-core isotopes, Table S5 period averages. Search of p. 1 to 15 and 23 to 29 for "Table S1" to "Table S5": 16 lines; the four above name the wrong table: the PSA database is cited as Table S1 and one sentence later as Table S2; the ice-core isotopes of Figure 2 as Table S1 instead of S4; the PSA isotopic fingerprints as Table S4 instead of S3; the EDC minus EDML differences of Figure 4 as Table S4 instead of S5. With Table S3 the modelled values of Figure 2 are reproduced (PP-37). The grade is moderate because a reader following these references finds other data than those plotted or used. GB-13 concerns the database design described in the same paragraph as the first citation. |
| Suggestion | p. 4, l. 127: "(Figure S1 and Table S2)"; p. 26, l. 858: "(refs. Table S4; open symbols)"; p. 26, l. 865 to 866: "the isotopic fingerprint and elemental concentration of the PSA end-members (Table S3)"; p. 28, l. 876: "(Table S5)". |
| Status | verified (page images p. 4, 26, 28; Suppl. p. 11, 16, 20, 21, 22) |
| Severity | moderate |
| Source | S2, S4, SD, AB |

**GB-15 The Antarctic end-members of Table S2 are not UCC-normalised, although the table header and the Methods state that all PSA patterns are.**

| Field | Content |
|---|---|
| Check | P2 |
| Location | p. 4, l. 132 to 135; Suppl. p. 19, Table S2, Antarctica rows ELB, Expcove, Miers, Vict, columns La to Lu; p. 7, l. 217; p. 10, l. 329 to 334 |
| Quotation | "all PSA REE patterns were normalized to the UCC composition of Rudnick and Gao (2003)" (p. 4, l. 134); "REE normalised on the Upper Continental Crust (Rudnick and Gao, 2003)"; (p. 10, l. 330) "our results do not indicate significant Antarctic contributions to EDC." |
| Concern | In the 213 non-Antarctic rows of Table S2 the 13 values of a row lie close together (ratio of largest to smallest value 1.20 to 4.13, Ce/Pr 0.80 to 2.77). The four Antarctic rows differ by orders of magnitude within a row (ratio 78 to 252) with Ce/Pr 8.35 to 9.16, for example ELB La 0,720323, Ce 1,414516, Pr 0,157226, Lu 0,008290 (page image Suppl. p. 19; Python on all 217 rows). Ce/Pr near 9 is the ratio of raw crustal concentrations, not of UCC-normalised values: divided by the UCC values of Rudnick and Gao (2003) the four rows become flat (coefficient of variation 0.12 to 0.36, at 0.023 to 0.036 of UCC). If these values entered Eq. 2 as listed, the ANT columns could hardly fit a normalised EDC pattern, and the finding of negligible Antarctic input (p. 7, l. 217; p. 10, l. 329 to 334), which the authors explain by katabatic winds and transport, could be an artefact of the database. Table S1 nevertheless gives ANT 33.1 % at 3654 yr (R 0.69) and 1.7 % at 13412 yr, the only two of 241 samples with ANT above 0. Were the ANT patterns normalised before fitting, and is only the table wrong? The grade is major because the absence of Antarctic dust is a stated result that differs from Coppo et al. (2022) and from the Pb isotope study discussed in GB-07; GB-13 concerns the design of the same database as a whole, GB-08 the undocumented SAF rows of the same table. |
| Suggestion | State in Section 2 (p. 4, l. 132 to 135) whether the ANT rows were normalised; correct Table S2 (Suppl. p. 19); if the fit used the listed values, rerun DEPOT with normalised ANT end-members and revise p. 10, l. 329 to 334 and Table S5. |
| Status | verified (values and header on page images Suppl. p. 16 and 19; row statistics, Python); inferred (flatness after division by UCC values of Rudnick and Gao (2003), values taken as reference, the source not read); assumption (that the listed values entered the fit), formulated as a question |
| Severity | major |
| Source | ZF |

**GB-16 The Monte Carlo uncertainty of the source contributions is computed but never reported.**

| Field | Content |
|---|---|
| Check | P11 |
| Location | p. 5, l. 153 to 165; p. 6, l. 179 to 181; Suppl. p. 11 to 15, Table S1; Suppl. p. 22, Table S5 |
| Quotation | "To evaluate the impact of uncertainties in REE concentrations in DIC samples and their associated correction factors (cfi) on our model outputs, we performed Monte Carlo (MC) simulations for each DIC sample" |
| Concern | The Monte Carlo design (2000 runs, a PDF per DS, aggregation by PSA, median as best estimate) is described in detail. The Results report medians only: Table S1 gives one median per PSA and sample, Table S5 period means without dispersion, Figures 1 and 3 show sample-to-sample variation. The Results call the PSA mixes "meaningful compared to the uncertainties" (p. 6, l. 180) without a number; "±" occurs only in literature values (p. 10, l. 320; p. 12, l. 394). The reader cannot judge whether the ACR and YD differences or the EDC versus EDML differences of 4 to 8 points (p. 13, l. 418 to 424) exceed the model uncertainty; GB-23 and GB-44 depend on this. GB-12 concerns the notation of the same Monte Carlo passage; GB-10 the ages of the same table. |
| Suggestion | Add to Table S1 the 16th to 84th percentile (or interquartile range) of each PSA PDF per sample, to Table S5 the mean Monte Carlo spread per period, and refer to it in p. 6, l. 180 and in Section 4.4. |
| Status | verified (search) |
| Severity | moderate |
| Source | S3 |

**GB-17 The choice of 2000 Monte Carlo runs is justified by cost and an unquantified comparison.**

| Field | Content |
|---|---|
| Check | P33 |
| Location | p. 5, l. 162 to 164 |
| Quotation | "The choice of 2000 MC simulations is a tradeoff between computation cost and representativity of the uncertainty propagation in the PDFs" |
| Concern | Computation cost is used as a limit, but no run time or resource is given, and "does not significantly affect the results" (l. 164) has no measure. GB-16 asks for the spread itself; here the sufficiency of the run number. |
| Suggestion | Give the run time per sample and the largest change of a PSA median between 2000 and 5000 runs in p. 5, l. 162 to 164. |
| Status | verified |
| Severity | minor |
| Source | SD |

**GB-18 Absolute PSA dust fluxes and an EDML deposition record are announced but shown nowhere.**

| Field | Content |
|---|---|
| Check | P11, P4, P31, P3 |
| Location | p. 5, l. 165 to 167; p. 6, l. 183 to 184; p. 13, l. 448 to 450; Figure S2 (Suppl. p. 3 to 4); Figure 1 (p. 24); Figure S5 (Suppl. p. 9 to 10); Suppl. p. 11, Table S1 |
| Quotation | "to convert PSA contributions into absolute dust fluxes (Figure S2)" (p. 5, l. 167); (p. 6, l. 183 to 184) "summarize the relative contributions (in % of total deposition and flux)"; (p. 13, l. 449 to 450) "and continued until ~15 kyr BP in both cores (Figures S2 and S5)" |
| Concern | Figure S2 shows (A) EDC nssCa2+ flux, (B) δ18O and (C) deuterium excess, all for EDC; no PSA flux. Table S1 and Table S5 give percentages only; all five panels of Figure 1 are labelled "Total Contribution (%)"; Figure S5 shows contributions, not deposition. Search of all figure captions for "flux": one hit (Figure S2, nssCa2+). The conversion factor from nssCa2+ to dust mass is not given. No figure shows the EDML deposition decline that p. 13, l. 449 to 450 attribute to "both cores". The decoupling argument of p. 13, l. 447 to 450 would be directly testable with PSA fluxes. S4 also proposed citing Table S5 instead of Table S1 in p. 6, l. 183; since Table S1 groups the samples by period, that reference is not counted as wrong. GB-16 concerns the Monte Carlo output on the same page; here the flux conversion. |
| Suggestion | Either add PSA fluxes (figure panel and table columns) with the conversion and its uncertainty and an EDML flux record with source, or delete the conversion sentence in p. 5, l. 165 to 167 and "and flux" in p. 6, l. 184, and cite a source for the EDML deposition in p. 13, l. 449 to 450. |
| Status | verified (page images and captions Suppl. p. 3, 4, 9, 10, 11; p. 24) |
| Severity | moderate |
| Source | S3, S4, SD, AB |

**GB-19 The threshold R ≥ 0.67 does not correspond to the stated test, and three retained samples fall below it.**

| Field | Content |
|---|---|
| Check | P1, P5, P2 |
| Location | p. 5, l. 170 to 172; p. 6, l. 174 to 175; p. 5, l. 145; Suppl. p. 11, Table S1, rows 2888 and 3267, column R; Suppl. p. 13, Table S1, first row 10511, column R |
| Quotation | "We determined that R ≥ 0.67 corresponds to a statistically significant match (p < 0.01, two-tailed test, degrees of freedom = 10)" (p. 5, l. 170 to 172); (p. 6, l. 174 to 175) "38 did not meet the R threshold (R≥0.67) and were excluded from the provenance record" |
| Concern | The criterion is numeric and R is reported per sample, which makes it checkable. (a) Each pattern has 13 values (p. 5, l. 145), so a Pearson test has df = 11, not 10. (b) With r = t/sqrt(df + t²) and the two-tailed Student quantile (Python, scipy): p below 0.01 needs R ≥ 0.708 at df = 10 and R ≥ 0.684 at df = 11; R = 0.67 gives p = 0.017 (df 10) and 0.012 (df 11). R of about 0.66 is the 1 % value for df = 12, i.e. for 14 elements, the setting of Vanderstraeten et al. (2023). (c) Table S1 retains three samples with R = 0,66 (2888, 3267 and the first row 10511 yr), below the threshold under any rounding. Effect on the record (Table S1): 9 of 241 retained samples have R below 0.685 and 19 below 0.71 (17 Holocene, 2 YD); without them the Holocene means change by at most 1.0 point (PAT 49.0 to 49.8 or 48.4). (d) R is computed between a pattern and its own least-squares fit with up to 217 free coefficients, so the textbook null distribution does not apply; whether 0.67 separates meaningful from arbitrary fits is untested. The consequences for the Holocene record are treated in GB-23; GB-16 concerns the missing Monte Carlo spread, GB-10 the ages of the same table. |
| Suggestion | In p. 5, l. 170 to 172 state df = 11 and either apply the critical value of the intended test (0.684) and report the change of Table S5, or state 0.67 as an empirical choice with its p value; explain or remove the three rows with R = 0,66. Could the threshold be calibrated empirically, for example as the 99th percentile of R from fits of shuffled REE patterns with the same 217 DS? |
| Status | verified (wording, Table S1 values on page images Suppl. p. 11 and 13); inferred (critical values and recomputed means, Python; that 0.67 stems from the 14-element setting); assumption (that the standard null distribution does not hold for a fitted model), formulated as a question |
| Severity | moderate |
| Source | S3, SD |

**GB-20 Two Australian dust source samples appear twice in Table S2 under different names and basins, with identical coordinates and 13 identical values.**

| Field | Content |
|---|---|
| Check | P38 |
| Location | Suppl. p. 17, Table S2, rows Darling26 and Darling29; Suppl. p. 18, Table S2, rows Murray24 and Murray29; p. 4, l. 126; p. 4, l. 131; p. 11, l. 366 to 367 |
| Quotation | "1,031323 1,021984 1,065352 1,017556 1,072553" (rows Darling29 and Murray24); "1,150581 1,134873 1,250986 1,247889 1,436383" |
| Concern | Table S2 gives sample code, reference, size fraction, location and coordinates for all 217 DS, which makes this check possible. A comparison of all 217 value vectors (Python) finds exactly two pairs with identical 13-element vectors, Darling26 = Murray29 and Darling29 = Murray24 (the second quotation is Darling26 and Murray29), each also with identical coordinates (page images Suppl. p. 17 and 18). The same sample carries two names and basin assignments; the database has 215 distinct patterns, not 217; two columns of Eq. 2 are identical, so the split between the copies is not identifiable (inferred); and the Darling versus Murray attribution behind "the Darling sub-basin as the dominant source region" (p. 11, l. 366 to 367) can depend on it. PSA-level results are unaffected because all four rows are AUS. GB-13 concerns the size and balance of the database, GB-08 and GB-15 other rows of the same table; here two duplicated entries. |
| Suggestion | Remove or replace the duplicate rows in Table S2 (Suppl. p. 17 to 18), state the number of distinct patterns in p. 4, l. 126 and 131, and confirm the Darling attribution in p. 11, l. 366 to 367. How did lsqnonneg distribute contributions between the identical columns? |
| Status | verified (names, coordinates and values on page images, Python comparison); inferred (non-identifiability); assumption (effect on the Darling attribution), formulated as a question |
| Severity | moderate |
| Source | S2 |

**GB-21 Two of the six Southern African "this study" samples are labelled "Etosha Pan" although their names and latitudes point elsewhere, and all six carry western longitudes.**

| Field | Content |
|---|---|
| Check | P38 |
| Location | Suppl. p. 17, Table S2, rows EtoshaL1 to EtoshaL4, SuksesL and Sossusvlei, columns Location, Lattitude and Longitude; p. 11, l. 379 to 381; p. 12, l. 385 to 387; p. 12, l. 395 to 396 |
| Quotation | "Etosha Pan" (Location of rows SuksesL and Sossusvlei); "21,059 S"; "24,76 S"; "15,29 W" |
| Concern | The three Etosha samples of Li et al. (2020) lie at 18°53' to 19°03' S and the four EtoshaL samples at 18.557 to 19.125 S; SuksesL (21.059 S) and Sossusvlei (24.76 S) lie 2 to 6 degrees further south, and "Sossusvlei" names a pan in the Namib. The Li et al. (2020) rows give eastern longitudes (15° 50' to 15° 53' E), the six "this study" rows western ones (15,29 W to 16,836 W). Section 4.3 aggregates SAF contributions into Etosha, Makgadikgadi and Namibian coast systems (p. 12, l. 385 to 387 and 392 to 398); if the Location column was used for this grouping, SuksesL and Sossusvlei were counted as Etosha. GB-08 concerns the missing method description of the same rows, GB-13, GB-15 and GB-20 other aspects of the same table; here labels and coordinates. |
| Suggestion | Correct the Location of SuksesL and Sossusvlei and the hemisphere of all six rows in Table S2 (Suppl. p. 17), and add the sub-region used in Section 4.3 for each DS. To which system were SuksesL and Sossusvlei assigned in p. 12, l. 395 to 396? |
| Status | verified (page image Suppl. p. 17); inferred (location of Sossusvlei from name and coordinates); assumption (use of the label in the aggregation), formulated as a question |
| Severity | moderate |
| Source | S2 |

**GB-22 Two entries of Table S2 break the pattern of the table: a Darling Basin longitude 6 degrees west of all other Darling rows and a Dy value 2.6 times its neighbours.**

| Field | Content |
|---|---|
| Check | P2 |
| Location | Suppl. p. 17, Table S2, row Darling12, column Longitude; Suppl. p. 17, Table S2, row Kuiseb2inf5, column Dy |
| Quotation | "138°17'6.00" (Darling12, Longitude); "6,200013" |
| Concern | Darling12 has the same latitude as Darling11 (31° 2'49.20"S) but 138°17' E instead of 144°17' E; all other 44 Darling rows lie between 141 and 148° E (Python, Suppl. p. 17 to 18). In Kuiseb2inf5 Dy is 6,200013 between Tb 2,692922 and Ho 2,149792 (second quotation); the ratio of Dy to the mean of Tb and Ho is 2.56, against at most 1.27 in the other 212 non-Antarctic rows (Python). Both values are confirmed on the page image Suppl. p. 17. Are these transcription errors? A Dy spike of this size would shape the fit of any EDC pattern to which this DS contributes. GB-20 concerns two duplicated rows of the same table; GB-15 the Antarctic rows; GB-08, GB-13 and GB-21 other aspects of the same table. |
| Suggestion | Check the two values against Marx and Kamber (2010) and Vanderstraeten et al. (2023) and correct Table S2; if Kuiseb2inf5 was used with the listed Dy, state whether results change. |
| Status | verified (values on page image; ratios, Python); assumption (that the values are errors), formulated as a question |
| Severity | minor |
| Source | ZF |

#### Minor corrections

| ID | Location | Quotation | Replacement | Source |
|---|---|---|---|---|
| KK-08 | p. 3, l. 101 | "to ice core camples" | "to ice core samples" | SD |
| KK-09 | p. 4, l. 128 | "subdivised into Patagonia" | "subdivided into Patagonia"; GB-13 concerns the counts of the same sentence | ZF |
| KK-10 | p. 4, l. 138 | "solving the system of matrixes (Eq.2)" | "solving the system of equations (Eq. 2)"; GB-12 concerns the equation reference of the same passage | ZF |
| KK-11 | Suppl. p. 16, Table S2, column header | "Lattitude" | "Latitude"; spelling only, GB-08, GB-13, GB-15, GB-20, GB-21 and GB-22 concern contents of the same table | ZF |
| KK-12 | Suppl. p. 19, Table S2, section header; Suppl. p. 20, Table S3, row 4 | "New-Zealand (NZ)" | "New Zealand (NZ)" (form of the main text); spelling only, KK-11 corrects the header of the same table, GB-08, GB-13, GB-15, GB-20, GB-21 and GB-22 concern its contents | S2 |

#### Verification log

| ID | Check | Checked | Values | Result |
|---|---|---|---|---|
| PP-09 | Design sketch (SD) | Questions, type, data sources, time axis, environment, principles, components, disclosed limitations and chain from framework to result, whole manuscript and supplement | four aims (p. 3, l. 91 to 98), no hypotheses; re-analysis of a published dataset with a numerical unmixing model; 294, 279, 241 samples; 217 DS in 7 PSA; MATLAB lsqnonneg without version; disclosed: gap, 15 exclusions, Gd removal, 38 exclusions, tentative ACR and YD | basis for the design checks; no finding of its own |
| PP-10 | P12 | Data sources of Methods and Discussion covered by paper or supplement | Table S2 217 rows (39 PAT, 5 CWA, 14 PAP, 23 SAF, 107 AUS, 25 NZ, 4 ANT; sum 217); Table S3 7 rows; Table S4 35 rows; Table S5; Table S1 241 rows; external and cited: nssCa2+ (Fischer et al., 2007), δ18O (EPICA Community Members, 2006), deuterium excess (Stenni et al., 2010), EDML (Vanderstraeten et al., 2023), Potrok Aike (Lisé-Pronovost et al., 2015), DustCOMM (Kok et al., 2021) | no finding for these sources; the others see GB-09; reachability not checked (no links) |
| PP-11 | P23, P36 | Sample and source balance from dataset to record | 294 - 15 = 279 (p. 4, l. 108, 114, 117); 279 - 38 = 241 (p. 6, l. 174, 179); Table S1 241 rows (48 + 51 + 51 + 51 + 40 on Suppl. p. 11 to 15); per period 60 + 56 + 9 + 8 + 27 + 40 + 41 = 241; 241/279 = 86.38 % (text 86 %); gap 21.7 to 27.3 kyr BP: 22150, 23104, 25384, 25640 yr = four (p. 4, l. 113); DS in text 39 + 5 + 14 + 23 + 106 + 25 + 5 = 217 | no finding; balance closes; DS split by region see GB-13, Table S1 caption see GB-33 |
| PP-12 | P38 | Names of model, samples and coefficients, p. 1 to 15, 23 to 29 and supplement | "DEPOT" with expansion at p. 3, l. 100; "model", "algorithm" for the same procedure; PSA abbreviations defined at p. 2, l. 58 to 59 and p. 4, l. 128 to 133 and then used consistently | no finding beyond GB-12, KK-03, KK-21 |
| PP-13 | P38 | Period labels | HS1 on 15 lines of the main text, HSI once (KK-14); MIS3 and "MIS 3" (spacing only); LGM, ACR, YD, Early and Late Holocene defined at p. 6, l. 184 to 188 and used consistently in Table S5 | no finding beyond KK-02, KK-14, KK-20 |
| PP-14 | P38 | Pairs of similar names tested for identity | SCWA (Table S3) as southern subset of CWA (rows SCWA1 to SCWA3, MCWA, NCWA); "Darling sub-basin" and "Darling Basin": same object; "S-Puna" and "South Puna": abbreviation; "Puna-Altiplano" with hyphen or dash and "Puna AltiPlano" (Table S2) | no finding; typographic variants only |
| PP-15 | P25 | Information availability per step | cf_i from parallel full digestion (p. 4, l. 122 to 124) available before fitting; end-members from Table S3; nssCa2+ from Fischer et al. (2007) | no finding |
| PP-16 | P37 | Post-hoc corrected values in figures and tables | cf_i correction applied to all samples and stated (p. 4, l. 118 to 124); no other recalculation | no finding |
| PP-17 | P26 | Guarantees across paths | non-negativity holds in every fit and Monte Carlo run (p. 5, l. 139); no alternative mode | no finding; normalisation of medians see GB-34 |
| PP-18 | P27 | Flow of untested values | R threshold steers sample selection; Monte Carlo medians steer Tables S1, S5 and Figures 1, 3, 4 without spread | no finding beyond GB-16, GB-19, GB-23 |
| PP-19 | P18 | Self-application of stated principles | critique of overlapping isotope fields (p. 2, l. 64 to 65) not applied to REE fields; data statement (p. 16, l. 494 to 495) not met | no finding beyond GB-09 and GB-13 |
| PP-20 | P32 | Statements of confirmation and independent checks | "confirming a robust linear agreement" (p. 5, l. 172); "supports the robustness" (p. 8, l. 259); no synthetic or independent sample check | no finding beyond GB-13, GB-19, GB-37 |
| PP-21 | P17 | Location of disclosed limitations | gap, 15 exclusions and Gd removal in Methods (p. 4, l. 113 to 117); 38 exclusions in Results (p. 6, l. 174 to 179); ACR and YD caveat only in Section 4.4 (p. 12, l. 407 to 409); isotope domain note in the Figure 2 caption (p. 26, l. 863) | no finding except for the ACR and YD caveat (GB-36) |
| PP-22 | P35 | Environment fields | MATLAB without version; lsqnonneg options and seed absent; instrument named only through the cited dataset | no finding beyond GB-09 |
| PP-23 | P19 | Provenance class of core statements | all provenance shares (Tables S1, S5, Figures 1, 3, 4, S3 to S5) are model output from secondary REE data, as the manuscript says (p. 3, l. 88 to 89; p. 4, l. 107 to 108) | no finding for the main record; new end-members see GB-08; Table S4 sites see GB-37 |
| PP-24 | P29 | Figure S1 map collage (Suppl. p. 1 to 2) | panels PAT, NZ, SAF, AUS, Puna-Alti, CWA, ANT and overview with EDC and EDML; north arrows in 3 panels, scale bars in 5; names written out in the caption; pins not compared with DS counts (overlapping pins) | no finding |

### Segment 3: Results (p. 6 to 7, Figures 1 and 3, Tables S1 and S5, Figures S3 and S4)

#### Substantive findings

**GB-23 The Holocene record is selected by fit quality, and its larger variability is confounded with low dust concentrations.**

| Field | Content |
|---|---|
| Check | P9, P11, P20, P22 |
| Location | p. 6, l. 174 to 182; p. 9, l. 306 to p. 10, l. 314; p. 2, l. 62 to 63 |
| Quotation | "These excluded samples are all younger than 14 kyr BP and have very low REE concentrations near the detection limit." (p. 6, l. 175 to 176); (p. 9, l. 306 to 307) "During YD and throughout the Holocene, our unmixing model reveals a significantly larger variability in the dust assemblages reaching EDC" |
| Concern | The manuscript discloses the exclusion and its cause. Its consequences are not drawn. (a) Selection by outcome: exclusion uses R and acts only after 14 kyr BP. The 86 % refer to all 279 samples; Table S1 has 129 retained samples younger than 14 kyr BP, so the exclusion rate there is 38/(129 + 38) = 22.8 %, against 0 % before (Python); the 38 are not listed, so "all younger than 14 kyr BP" cannot be checked (GB-09). (b) Fit quality covaries with composition among the 116 retained Holocene samples: mean R 0.799 against 0.916 in the 108 samples of HS1 to MIS3; 51 Holocene samples have R below 0.80, none of the glacial ones; Holocene samples with R below 0.80 have mean PAT 41.5 % (SD 34.6), those with R ≥ 0.80 54.8 % (SD 29.0) (Welch p = 0.03 by SD). (c) The manuscript states that at low concentrations analytical noise "distorts the REE patterns" (p. 6, l. 179) and that interglacial fluxes are much lower (p. 2, l. 62 to 63). The larger Holocene variability, read as source dynamics in Section 4.3, coincides with the lowest concentrations; noise propagated through the fit would also produce scattered single-source solutions (13 Holocene samples with one PSA at 90 % or more against 5 of 108 glacial ones). No test is reported for "significantly larger variability". The Monte Carlo spread that could separate both causes is not reported (GB-16). GB-19 concerns the threshold rule itself; GB-09 the missing list of excluded samples; GB-05 the flux factor of p. 2, l. 63 used here as context; GB-01 the end of the time span in p. 6, l. 182. The grade is major because aim 1 singles out the Holocene and Section 4.3 interprets its variability as regional source dynamics. |
| Suggestion | Report per-sample Monte Carlo intervals in Table S1 and as bands in Figure 1; give the exclusion rate per period next to "86%" in p. 6, l. 179; give Holocene averages for R thresholds 0.67, 0.71 and 0.80. Counter-design: scale glacial samples to Holocene concentrations, add noise at the Holocene analytical level, refit with DEPOT and compare the resulting spread with the observed Holocene spread; only the excess can be read as source change. |
| Status | verified (exclusion counts and statements in the text, Table S1 rows); inferred (rates, means and tests computed from Table S1, Python); assumption (that noise produces part of the spread), formulated as a test |
| Severity | major |
| Source | SD, S3 |

**GB-24 The ranking of the secondary sources "AUS, SAF, PAP and NZ" is not supported by Table S1 or Table S5: NZ ranks above PAP.**

| Field | Content |
|---|---|
| Check | P2, P21 |
| Location | p. 6, l. 201 to 202 |
| Quotation | "AUS, SAF, PAP and NZ, in decreasing order of importance" |
| Concern | The basis of "overall" is not stated, so both plausible bases were computed (Python): mean over all 241 samples of Table S1, AUS 16.5, SAF 9.2, NZ 7.9, PAP 6.8 %; mean of the six period means of Table S5 (Holocene, YD, ACR, HS1, LGM, MIS3), AUS 13.2, SAF 9.0, NZ 7.7, PAP 4.8 %. On both bases NZ is third and PAP fourth. |
| Suggestion | In p. 6, l. 201 to 202 name the basis and change the order to "AUS, SAF, NZ and PAP", or restrict the order to a named interval. |
| Status | verified (Table S1, Table S5 values); inferred (means, Python) |
| Severity | moderate |
| Source | S3 |

**GB-25 Two trend statements of the Results do not follow from the period means of Table S5.**

| Field | Content |
|---|---|
| Check | P1, P2 |
| Location | p. 6, l. 203 to 204; p. 7, l. 209 to 210 |
| Quotation | "Its average contributions rose after 14.7 kyr BP, reaching 11% during the ACR" (p. 6, l. 203 to 204); (p. 7, l. 209 to 210) "its influence steadily declines over time: 7% during HS1, and only 6.5%, 3%, and 6% during the ACR, YD, and Holocene" |
| Concern | AUS is 11.3 % in HS1 and 11.1 % in the ACR, so there is no rise from HS1 to ACR; the rise begins with the YD (14.5 %). NZ rises from 3.3 % in the YD to 5.9 % in the Holocene, so the decline is not steady. The single values are correct (PP-27); only the trend words do not follow. |
| Suggestion | In p. 6, l. 203 to 204 write "remained at 11 % during the ACR and rose to ~15 % during the YD"; in p. 7, l. 209 write "declines after the LGM" or name the YD minimum. |
| Status | verified |
| Severity | minor |
| Source | S3 |

**GB-26 The "sharp increase" of SAF during the YD rests on one of nine samples.**

| Field | Content |
|---|---|
| Check | P21, P20 |
| Location | p. 6, l. 207 |
| Quotation | "followed by a sharp increase during the YD with 15%" |
| Concern | The YD mean of 14.6 % is reproduced from the nine YD rows of Table S1: 0.0, 1.3, 94.7, 8.8, 5.5, 5.0, 6.2, 2.4, 7.8. Without the sample at 12227 yr (94.7 %) the mean is 4.6 %; the median of all nine is 5.5 % (Python). The comparison with MIS3 to ACR (4.9 to 9.3 %) reverses once this sample is removed or the median is used. The small YD sample number is disclosed only in Section 4.4 (p. 12, l. 407 to 409). The same sample drives the YD SAF difference to EDML (GB-45). |
| Suggestion | Give the number of samples and the median per period in Table S5, and qualify p. 6, l. 207 ("driven by one sample at 12.2 kyr BP"). |
| Status | verified (values); inferred (mean and median, Python) |
| Severity | moderate |
| Source | S3 |

**GB-27 The SAF minimum "~2%" between 9.5 and 12 kyr BP matches neither the mean nor the median of Table S1 in that window.**

| Field | Content |
|---|---|
| Check | P2, P20 |
| Location | p. 6, l. 207 to p. 7, l. 208 |
| Quotation | "Although SAF input drops to minimal levels (~2%) between 9.5 and 12 kyr BP" |
| Concern | Table S1 has 33 samples between 9500 and 12000 yr BP; their SAF mean is 4.32 % and their median 0.3 %, with single values of 40.3 % (10278 yr) and 49.2 % (10511 yr) (Python). The text does not say which statistic or smoothing gives ~2 %; the smoothed curve of Figure 1 runs between 1.2 and 12.6 % in this window (PP-28). The window also overlaps the YD, for which the preceding sentence gives 15 %. GB-26 concerns the YD value of the same sentence. |
| Suggestion | Name the statistic and its source in p. 7, l. 208 (mean, median or smoothed curve, with Figure 1 or Table S1), and avoid overlap with the YD. |
| Status | verified (values); inferred (mean and median, Python) |
| Severity | minor |
| Source | S3 |

**GB-28 The statements on South Puna and South Altiplano contributions contradict Table S1, and Figure S3 shows neither the values of Table S1 nor those of Figure 1.**

| Field | Content |
|---|---|
| Check | P2, P3, P6, P20, P24 |
| Location | p. 7, l. 211 to 215; p. 11, l. 355 to 360; p. 9, l. 290; Figure S3, panels Altiplano and Puna (Suppl. p. 6); Figure 1, panel PAP (p. 24); Suppl. p. 11 to 13, Table S1, columns Puna and Altiplano |
| Quotation | "increasing to ~5% during the ACR and YD, primarily from the South Puna region" (p. 7, l. 212); (p. 7, l. 214) "contributing over 90% at 11.2, 10, 8.6, 6, and 3.5 kyr BP"; (p. 7, l. 215) "contributions of South Puna remained consistently below 20% during this interval (Figure 1)"; (p. 11, l. 358) "Southern Altiplano begins contributing dust only after approximately 11.2 kyr BP" |
| Concern | The sub-regional split is a useful addition. Against Table S1 (241 rows, Python, page images Suppl. p. 11 to 13): (1) in the ACR the PAP contribution is indeed from Puna (mean 5.23 %, Altiplano 0.0 %), but in the YD Altiplano averages 3.27 % and Puna 1.26 %; (2) Altiplano exceeds 90 % in two samples only, 8629 yr (100.0) and 11228 yr (97.0); near 10, 6 and 3.5 kyr BP the maxima are 75.7 (9957 yr), 58.5 (5967 yr) and 62.7 (3465 yr); read as share of PAP, 22 samples reach 100 %, so the denominator is not named either; (3) eight Holocene samples have Puna ≥ 20 %: 3503 (25.0), 4387 (20.6), 5657 (23.4), 5850 (29.1), 6775 (20.7), 7833 (25.6), 10205 (25.7), 11117 (20.2); (4) Altiplano is non-zero before 11.2 kyr BP in the two YD rows at 12841 yr (16.6 and 12.8 %), so the onset precedes the stated date by about 1.6 kyr, which bears on the coincidence with the desiccation of paleolake Coipasa (p. 11, l. 358 to 360). Against the figures (measured by AB): Figure 1, cited in l. 215, shows only the PAP total; its raw PAP line exceeds 85 % only at 8.64 kyr (98.0 %) and 11.23 kyr (95.4 %). Figure S3 shows the Altiplano raw line at most at 66.1 % (6.37 kyr), at or below 5.2 % around 8.629 kyr and at or below 14.6 % at 11.228 kyr, and Puna at or below 2.1 % at 8.629 kyr; so at 8.63 kyr Figure 1 shows PAP 98.0 % but Figure S3 at most 7.3 %. In Figure S3 the Puna line exceeds 20 % at 8 Holocene peaks (maximum 42.8 % at 11.11 kyr) and the Altiplano line has a raw peak of 38.8 % at 11.85 kyr inside the YD. The sub-region is also named "South Altiplano" (p. 7, l. 213; p. 9, l. 290) and "Southern Altiplano" (p. 4, l. 130; p. 11, l. 358). The grade is major because p. 7, l. 213 to 215 and p. 11, l. 357 to 360 report a result on Holocene source change used in aim 3. GB-35 concerns the panel names of Figure S3. |
| Suggestion | Check which series Figure S3 plots and make it consistent with Table S1 or state the difference in its caption; correct p. 7, l. 212 to 215 and p. 11, l. 357 to 360 to the dates and values the data support, name the denominator, give the onset of Altiplano input from the data and revise the Coipasa comparison; cite Figure S3 instead of Figure 1 in l. 215; use "Southern Altiplano" throughout. |
| Status | verified (Table S1 values; Figure 1 and Figure S3 measured by AB on 300-dpi renderings); inferred (shares and onset, Python; effect on the Coipasa argument) |
| Severity | major |
| Source | S3, SD, AB, S2 |

**GB-29 Labels in Figures 1 and 5 are printed below 6 pt; in Figures 2 and 3 they are at the limit.**

| Field | Content |
|---|---|
| Check | P29 |
| Location | Figure 1, tick numbers and legend (p. 24); Figure 5, tick numbers and legend (p. 29); Figure 2, legend (p. 26); Figure 3, tick numbers (p. 27) |
| Quotation | "Raw data"; "smoothed" |
| Concern | Capital or digit heights measured at 300 dpi (px × 72 / 300 / 0.72, tolerance ±0.6 pt): Figure 1 tick "100" 5.7 pt, legend 5.0 pt; Figure 5 legend 4.7 pt, ticks 4.7 to 5.0 pt; Figure 2 legend 5.7 pt; Figure 3 ticks 5.7 to 6.0 pt; Figure 4 6.3 to 6.7 pt; supplement figures 8.7 pt or more. Figures 1 and 5 lie below 6 pt even with the tolerance. |
| Suggestion | Enlarge tick numbers and legends of Figures 1 and 5 (and 2 and 3) to at least 7 pt at print size. |
| Status | verified (measured) |
| Severity | minor |
| Source | AB |

**GB-30 Source and period abbreviations in Figures 1, 3 and 4 are not resolved in their captions, and Figure 1 does not mark the sampling gap.**

| Field | Content |
|---|---|
| Check | P29 |
| Location | Figure 1 and caption, p. 25, l. 851 to 854; Figure 3 and caption, p. 27, l. 869 to 873; Figure 4 and caption, p. 28, l. 875 to 876 |
| Quotation | "Figure 1: Evolution of dust PSA contributions to EDC ice core" |
| Concern | Figure 1 labels its panels PAT, AUS, SAF, NZ and PAP and the periods YD, ACR, HS1, LGM and MIS3; Figure 3 uses PAT to PAP; Figure 4 PAT to PAP and Holo to LGM. The captions resolve none of these (Figure 3 only LGM; Figure 1 writes out only CWA and ANT, which are not shown). Across the sampling gap of 21.7 to 27.3 kyr BP (four samples, PP-11) the smoothed lines of Figure 1 run as straight segments without marking. GB-29 concerns the label sizes of the same figure. |
| Suggestion | Resolve PSA, EDC, EDML and all source and period abbreviations in each caption, state the period limits, and mark the gap in Figure 1. |
| Status | verified |
| Severity | minor |
| Source | AB |

**GB-31 The "Holocene" panel of Figure 3 shows the Early Holocene samples, and the "Early Holocene" panel of Figure S4 shows the Late Holocene samples.**

| Field | Content |
|---|---|
| Check | P3 |
| Location | Figure 3, left panel "Holocene" (p. 27); Figure 3 caption, p. 27, l. 869 to 870; Figure S4, panel "Early Holocene" (Suppl. p. 8) |
| Quotation | "Figure 3: Box plots of provenance contributions (in %) of Holocene, and Last Glacial Maximum (LGM)" |
| Concern | The LGM panel agrees with Table S1 (PP-33). The left panel (measured, ±0.22) gives PAT upper whisker 98.48, Q3 72.95, median 55.17, Q1 12.29; AUS 79.84, 34.23, 18.17, 2.83. This matches the Early Holocene of Table S1 (7.5 to 11.7 kyr, 56 samples: PAT 98.5, 73.0, 55.2, 12.3; AUS 79.8, 34.2, 18.1, 2.8), not the whole Holocene (116 samples: PAT median 58.6, Q1 18.4; AUS whisker 77.7), which differs by 3 to 12 points. The "Early Holocene" panel of Figure S4 gives PAT 18.91, 61.65, 80.65, 98.06, which matches the Late Holocene (60 samples: 18.9, 61.7, 80.7, 97.9). In the other Figure S4 panels the PAT boxes lie 0.6 to 1.4 points above the Table S1 statistics. Could the authors say whether these panels were drawn from renormalised values? GB-30 concerns the abbreviations of the same caption. |
| Suggestion | Relabel the Figure 3 panel and caption "Early Holocene (7.5 to 11.7 kyr BP)" or replot it with all Holocene samples; relabel the Figure S4 panel "Late Holocene (2.8 to 7.5 kyr BP)" or replot it; give period limits and sample numbers in both captions and explain the offset of the other Figure S4 panels. |
| Status | verified (box elements measured; Table S1 statistics computed); assumption (cause of the offset in Figure S4), formulated as a question |
| Severity | moderate |
| Source | AB |

**GB-32 The captions of Figure 3 and Figure S4 call the whiskers "extremes", but points are plotted beyond them.**

| Field | Content |
|---|---|
| Check | P3 |
| Location | Figure 3 caption, p. 27, l. 872; Figure S4 caption (Suppl. p. 7); Figure 3, both panels |
| Quotation | "and the whiskers indicate the lower and upper extremes" |
| Concern | In the LGM panel 1 PAT point (93.5) lies above the whisker (84.35) and 3 SAF points above 14.51; in the left panel points lie beyond the whiskers for AUS (3), PAP (4), SAF and NZ. All whisker ends agree with 1.5 times the interquartile range (for example LGM SAF Q1 1.8, Q3 7.6, whisker 14.5 from Table S1 against 14.51 measured). GB-30 and GB-31 concern other parts of the same caption and figure. |
| Suggestion | Replace in both captions by "the whiskers extend to the most extreme values within 1.5 times the interquartile range; points beyond them are shown individually". |
| Status | verified (measured) |
| Severity | minor |
| Source | AB |

**GB-33 The caption of Table S1 gives 279 DIC samples and 217 PSAs; the table lists 241 samples, and 217 is the number of dust source samples.**

| Field | Content |
|---|---|
| Check | P20, P2 |
| Location | Suppl. p. 11, Table S1, caption; p. 6, l. 179 |
| Quotation | "Table S1: Median of PSA's contribution (in percents) based on th DEPOT model results - using 217 PSAs and 279" |
| Concern | Table S1 has 241 data rows (48 + 51 + 51 + 51 + 40 on Suppl. p. 11 to 15), equal to the retained samples in p. 6, l. 179, not the 279 fitted. The 217 units are DS (p. 4, l. 126 to 133), grouped into seven PSA. The caption mixes DS and PSA and names a count the table does not contain; "th" is a typo. GB-10, GB-16, GB-19 and GB-23 concern the ages, the missing spread, the R column and the selection behind the same table and the same sentence of p. 6, l. 179. |
| Suggestion | Caption: "Median contribution of each PSA (in %) from the DEPOT model, using 217 dust source samples (DS) grouped into seven PSA, for the 241 DIC samples with R ≥ 0.67 (of 279 fitted)". |
| Status | verified |
| Severity | minor |
| Source | S3, S2, SD |

**GB-34 One row of Table S1 sums to 93.5 %, and how the PSA medians are brought to percent of total deposition is not described.**

| Field | Content |
|---|---|
| Check | P1, P8 |
| Location | p. 5, l. 160; Suppl. p. 13, Table S1, first row 10511, columns PAT to ANT |
| Quotation | "Median of PSA's contribution (in percents)"; (p. 5, l. 160) "the ensuing CDS results (in % of total deposition)" |
| Concern | Summing the eight contribution columns gives 99.85 to 100.15 for 240 rows; the first row at 10511 yr gives 0.0 + 0.0 + 3.1 + 6.7 + 49.2 + 29.5 + 5.0 + 0.0 = 93.5 (page image Suppl. p. 13; Python). Medians of separate PDFs need not add to 100, but the other 240 rows show that the published values are effectively closed. CDS scale with dust concentration; how they become "% of total deposition", and whether the PSA medians were renormalised to 100 %, is not described. The same row is one of the three with R = 0,66 (GB-19). GB-16 concerns the Monte Carlo spread of the same output; GB-10 and GB-33 the ages and the caption of the same table. |
| Suggestion | Describe in Section 2 (p. 5, l. 160 to 165) the normalisation of CDS and the aggregation of medians, and check and correct the row 10511 of Table S1. |
| Status | verified (values); inferred (sums, Python) |
| Severity | moderate |
| Source | S3, SD |

**GB-35 The panel names of Figure S3 differ from the sub-region names of the text.**

| Field | Content |
|---|---|
| Check | P3 |
| Location | Figure S3, y-axis titles of the five panels (Suppl. p. 6); p. 7, l. 212 to 215; p. 11, l. 356 to 359; p. 11, l. 379 to p. 12, l. 392 |
| Quotation | "Altiplano Total Contribution (%)"; "Puna Total Contribution (%)"; "Sua Total Contribution (%)" |
| Concern | The text uses "South Puna", "South Altiplano" or "Southern Altiplano", "Makgadikgadi Complex (including Sua Pan)", "the Namibian coast and ephemeral riverbeds" and "Etosha Pan"; the panels are titled "Altiplano", "Puna", "Etosha", "Namibia" and "Sua". "Puna" does not show that North Puna is excluded (p. 11, l. 356), "Sua" not whether the whole Makgadikgadi Complex is meant. GB-28 concerns the values of the same panels; GB-21 the SAF sub-region labels of Table S2. |
| Suggestion | Use the text names in the axis titles of Figure S3 or define the panel names in its caption. |
| Status | verified |
| Severity | minor |
| Source | AB |

#### Minor corrections

| ID | Location | Quotation | Replacement | Source |
|---|---|---|---|---|
| KK-13 | p. 6, l. 189 | "It contributes for 65-70% (average" | "It contributes 65-70% (average" | S3 |
| KK-14 | p. 6, l. 191 | "the PSA dust assemblage during HSI is marked" | "the PSA dust assemblage during HS1 is marked" (HS1 on 15 other lines of the main text) | S2, S3 |
| KK-15 | p. 6, l. 193 | "(averages contributions)" | "(average contributions)" | S3 |
| KK-16 | p. 6, l. 198 | "and therefore reflects regional mixed input" | "and therefore reflect regional mixed input" (subject "The samples", l. 197) | S3 |
| KK-17 | p. 6, l. 199 | "LREE (low rare earth elements)" | "LREE (light rare earth elements)" | S2, S3 |
| KK-18 | Figure 1 caption, p. 25, l. 851; Figure S3 caption (Suppl. p. 5) | "between 2852 to 33699 yr BP"; "between 2.852 to 33.699 kyr BP" | "between 2852 and 33699 yr BP"; "between 2.852 and 33.699 kyr BP"; GB-29 and GB-30 concern other aspects of Figure 1 | AB |
| KK-19 | Figure 1 caption, p. 25, l. 852; Figure 5 caption, p. 29, l. 882; Figure S5 caption | "mobile average over 9 steps" | "moving average over 9 samples" (compared at all three captions, identical wording); KK-18, GB-29, GB-30 and GB-55 concern other aspects of Figure 1, GB-53 of Figure 5 | AB |
| KK-20 | Figure S4 caption (Suppl. p. 7) | "Antarctica Cold Reveal (ACR), (4) Heindrich Stadial 1 (HS1), and (5) Marine Isotope 3 (MIS3)" | "Antarctic Cold Reversal (ACR), (4) Heinrich Stadial 1 (HS1), and (5) Marine Isotope Stage 3 (MIS3)"; GB-31, GB-32 and GB-43 concern the content of Figure S4 | S2, S3, AB |

#### Verification log

| ID | Check | Checked | Values | Result |
|---|---|---|---|---|
| PP-25 | P1 | Average R of the retained samples (p. 6, l. 181) | mean of 241 R values in Table S1 = 0.8523 (text 0.852); median 0.89 | no finding |
| PP-26 | P2, P24 | Period boundaries (p. 6, l. 185 to 188) against the period bars of Table S1 and the gray zones of Figure 1 | Table S1: MIS3 from 29004, LGM 18128 to 28908, HS1 14716 to 17993, ACR 13032 to 14601, YD 11779 to 12867, Early Holocene 7676 to 11593, Late Holocene 2852 to 7478 yr; Figure 1 zone edges per panel 11.67 to 11.71, 12.89 to 12.91, 14.68 to 14.70, 17.98 to 18.02, 28.97 to 29.00 kyr (±0.036) | no finding |
| PP-27 | P2 | Abstract and Results values against Table S5 | PAT 65 to 75 % in MIS3, LGM, HS1 = 70.3, 65.7, 74.8; ACR 69 (68.9), YD 63 (63.1), Holocene 49 (49.0), 47 to 51 (47.1, 50.7); AUS 9, 10, 11, 11, ~15, 23 (9.1, 10.2, 11.3, 11.1, 14.5, 23.1); SAF ~5 to 9 (9.3, 6.3, 4.9, 8.0), YD 15 (14.6), Holocene ~11 (10.7); NZ 14, 7, 6.5, 3, 6 (14.2, 7.1, 6.6, 3.3, 5.9); PAP below 4, ~5, 11 | no finding for the values; ranking and trends see GB-24, GB-25 |
| PP-28 | P2, P3 | Minima and maxima named in the text against Table S1 (centred 9-step moving average) and Figure 1 (measured) | PAT minima: Table S1 at 10117, 8508, 6306 yr; Figure 1 at 10.13, 8.54, 6.33 kyr; text 10, 8.6, 6.3 kyr BP (p. 6, l. 194); AUS maxima: Table S1 9902, 10511, 6306 yr; Figure 1 plateau 9.86 to 10.57 kyr and 6.30 kyr; text 9.5 to 10 and ~6.3 kyr BP (p. 6, l. 205); PAT mean of 25 samples at or below 5000 yr 52.0 % against 50 to 55 % (p. 11, l. 352); SAF smoothed 9.5 to 12 kyr 1.2 to 12.6 % | no finding beyond GB-27 and GB-55; the smoothing alignment is not stated, so the comparison is inferred |
| PP-29 | P1, P3 | Table S5 (EDC) recomputed from Table S1 per period, PAP = Puna + Altiplano | all EDC cells reproduced within 0.1 (for example LGM 65.7, 0.0, 3.6, 6.3, 10.2, 14.2, 0.0; Holocene 49.0, 11.0, 10.7, 23.1, 5.9); Holocene row = sample-weighted mean of Late (60) and Early (56) Holocene; row sums 99.9 to 100.1 | no finding |
| PP-30 | P29, P3 | Inventory of all figures with type, caption and citations | Figures 1 to 5 (p. 24 to 29), one caption each; Figures S1 to S5 (Suppl. p. 1 to 10); all raster images; every figure cited in the text of its section; no graphical abstract | no finding; numbering order see GB-41 |
| PP-31 | P3 | Figure citations in the text | search "Fig", "Figure", "Figures", p. 1 to 15: 25 citations; first citations Figure 1 p. 6, l. 183, Figure 2 p. 8, l. 244, Figure 3 p. 9, l. 281, Figure 5 p. 10, l. 340, Figure 4 p. 12, l. 405; supplement order S1 to S5 | see GB-41 |
| PP-32 | P29 | Font sizes, all figures | Figure 1 5.0 to 6.3 pt; Figure 2 5.7 to 7.3 pt; Figure 3 5.7 to 6.0 pt; Figure 4 6.3 to 6.7 pt; Figure 5 4.7 to 5.0 pt; Figures S2 to S5 8.7 to 10.7 pt | see GB-29; supplement no finding |
| PP-33 | P3 | Figure 3, LGM panel, box elements against Table S1 (18 to 29 kyr, 40 samples) | measured / computed (±0.22): PAT 84.35/84.4, 71.73/71.7, 65.78/65.8, 58.90/58.9, 46.85/46.8; NZ 25.27/25.3, 18.89/18.9, 15.52/15.5, 10.86/10.8; SAF 14.51/14.5, 7.63/7.6, 4.62/4.6, 1.75/1.8 | no finding for the LGM panel |
| PP-34 | P3 | Figure S4, box elements against Table S1 | YD PAT 48.0, 71.4, 86.3, whiskers 100.3 and 0.2 against Table S1 (9 samples) 47.1, 70.2, 84.8, 98.7, 0.0; at least 8 YD positions visible in the PAT column; ACR count not possible (hidden points) | see GB-31 and GB-45 |

### Segment 4: Discussion, Conclusion, References, Declarations (p. 7 to 22, Figures 2, 4, 5, Tables S3, S4, Figures S2, S5)

#### Substantive findings

**GB-36 The Discussion and Conclusion place a "major" shift at the onset of the ACR, but the ACR averages lie inside the glacial range, no test is reported, and the caveat on 8 and 9 samples does not reach the timing claims.**

| Field | Content |
|---|---|
| Check | P15, P17 |
| Location | p. 7, l. 233 to 236; p. 7, l. 225; p. 1, l. 23; p. 8, l. 251 to 253; p. 9, l. 305 to 307; p. 12, l. 407 to 409; p. 13, l. 444 to 447; p. 14, l. 477 to 480 |
| Quotation | "Our calculations highlight a major shift in dust provenance occurred at the onset of the ACR" (p. 7, l. 233); (p. 7, l. 235) "with significantly increased contributions from low-latitude sources"; (p. 14, l. 477 to 478) "From ~14.5 kyr BP onward, a marked reorganization in dust provenance occurred"; (p. 12, l. 407) "It is important however to note that results for ACR and YD are tentative" |
| Concern | The glacial and Holocene assemblages differ clearly in Table S5. The timing rests on the ACR, where the averages do not show a "major" change: PAT 68.9 % lies between LGM (65.7) and MIS3 (70.3); the high-latitude share PAT + NZ is 79.4, 79.9, 81.9, 75.5, 66.4 and 54.9 % for MIS3, LGM, HS1, ACR, YD and Holocene, the low-latitude share AUS + SAF + PAP 20.6, 20.1, 18.2, 24.3, 33.6 and 44.8 % (Python, Table S5), a gradual rise rather than a step; AUS is 11.3 % in HS1 and 11.1 % in the ACR. The ACR differs from the LGM by 4.4 points in high-latitude share, the Holocene by 25.0. Welch tests by SD on Table S1 give HS1 against ACR PAT p = 0.32 and PAT + NZ p = 0.22, HS1 against Holocene p below 0.001 (autocorrelation ignored, indicative); in 1-kyr bins PAT is 83.2 % at 15 to 16 kyr and 68.5 % at 17 to 18 kyr, so part of the decline after 15 kyr BP is a return from a maximum within HS1. "Significantly increased" (p. 7, l. 235) is not backed by a test. Section 4.4 discloses that ACR and YD rest on 8 and 9 samples (Table S1: 13032 to 14601 and 11779 to 12867 yr) and are tentative, but the caveat is not carried into the Abstract (p. 1, l. 23), Section 4.1, the heading of 4.2 or the Conclusion. The YD is grouped with the glacial isotope cluster in 4.1 (p. 8, l. 251 to 253) but with the Holocene in 4.3 (p. 9, l. 306); the per-period back-calculation gives εNd -5.39 for the YD against -4.99 for the Holocene and -2.62 for the LGM (PP-37). The grade is major because the timing at ~14.5 kyr BP links the record to shelf submersion and Meltwater Pulse 1A (p. 13, l. 450 to p. 14, l. 455). Is the shift meant to begin at the ACR or to be fully expressed from the YD onward? In the same sentence "highlight ... occurred" lacks "that". |
| Suggestion | In p. 7, l. 233 to 236, p. 1, l. 23 and p. 14, l. 477 to 480 state the shift in terms the data support (for example a gradual change from the ACR, fully expressed in the YD and Holocene), give per-period values with sample numbers, move the caveat on ACR and YD to Section 3, and add a change-point or piecewise regression on the 241 samples (or on Monte Carlo realisations) with a confidence interval for the break, for PAT, PAT + NZ and the low-latitude sum, and the same for EDML; replace "significantly" by the test used and "major" accordingly ("highlight that a shift in dust provenance occurred"); decide to which group the YD belongs. |
| Status | verified (Table S5 values, Table S1 ages, quotations); inferred (group sums, bins, tests and recomputed εNd, Python) |
| Severity | major |
| Source | S4, SD |

**GB-37 The isotope validation claims agreement with values "measured in EDC" for interglacials, but the measured Holocene values of Table S4 and Figure 2 come from Taylor Glacier and Berkner Island, the calculation is described per interval but plotted per sample, and no measure of agreement is given.**

| Field | Content |
|---|---|
| Check | P31, P15, P3, P2, P11, P20 |
| Location | Figure 2, open and filled symbols and legend (p. 26); p. 8, l. 243 to 260; p. 7, l. 238 to 240; p. 3, l. 93 to 94; Suppl. p. 21, Table S4; Suppl. p. 20, Table S3 |
| Quotation | "For each time interval of the LGIT, the relative contribution of each PSA (CONTR) was multiplied by its average Sr and Nd concentrations" (p. 8, l. 244 to 245); (p. 8, l. 254 to 255) "the modeled and measured Holocene isotopic compositions (red filled and open symbols, respectively)"; (p. 8, l. 258 to 259) "Overall, the close agreement between our modeled isotopic compositions and those measured in EDC for both glacial and interglacial intervals supports the robustness of our DEPOT algorithm" |
| Concern | The back-calculation is reproducible: with Eq. 3 and 4, Table S3 and the period means of Table S1 one obtains 0.7083 and εNd -2.62 (LGM) and 0.7101 and -4.99 (Holocene), close to the EDC values cited in p. 7, l. 238 to 240 (PP-37). Three points do not hold. (a) Table S4 (page image Suppl. p. 21, 35 rows) lists EDC only for the LGM (2 rows, Delmonte et al., 2004a) and "Old Dome C" for HS1 (1 row); ACR and YD only Taylor Glacier (2 rows each); all 22 Holocene rows are Taylor Glacier (8) and Berkner Island (14). Seven Holocene open circles found in Figure 2 match Table S4 rows of Taylor Glacier (1) and Berkner Island (6) to within 0.0001 and 0.02 (measured by AB). The EDC Holocene values cited in p. 7, l. 239 to 240 (~0.710, εNd -4.51 to -5.68) appear neither in Table S4 nor among the detected symbols. So "measured in EDC for both glacial and interglacial intervals" is not what Figure 2 shows, and aim (2) (p. 3, l. 93 to 94) rests for the Holocene on cores of the Ross Sea and Weddell Sea sectors. (b) The text describes the calculation per time interval, but Figure 2 shows one point per sample: applied per row of Table S1, the Holocene spreads from 0.7060 to 0.7236 and εNd 2.20 to -16.52, and the YD sample at 12227 yr gives 0.7274 and -17.87, matching the isolated YD point; no table gives the modelled values. (c) No residual or uncertainty quantifies the agreement, and whether other mixtures would agree equally well is not tested. The grade is major because the stated support for the algorithm (p. 8, l. 258 to 260) would read differently if the comparison is with other cores. GB-36 concerns the grouping of the YD in the same section, GB-07 the literature on the Holocene question of the same aims. |
| Suggestion | Add the EDC Holocene measurements (Delmonte et al., 2004) to Table S4 and Figure 2 with their own symbol and label Taylor Glacier and Berkner Island as other sites; change "For each time interval" in p. 8, l. 244 to "For each DIC sample" and tabulate the modelled values per sample and per period; rephrase p. 8, l. 258 to 259 so that each comparison names its site; report residuals with Monte Carlo uncertainty and a discrimination test (for example Holocene isotopes computed with glacial, DustCOMM or Coppo et al. (2022) proportions). |
| Status | verified (Table S4 sites on page image, Figure 2 symbols measured, quotations); inferred (recomputed values, Python) |
| Severity | major |
| Source | S3, S4, AB, SD |

**GB-38 Several percentages of Sections 4.2 and 4.3 do not match Table S5 or the Results.**

| Field | Content |
|---|---|
| Check | P1, P2, P15, P36 |
| Location | p. 9, l. 276; p. 9, l. 281 to 282; p. 9, l. 293 to 295; p. 10, l. 321; p. 10, l. 326 |
| Quotation | "(here, PAT+AUS is ~77%)" (p. 9, l. 276); (p. 9, l. 281 to 282) "However, we find a higher average NZ contribution (~11%), making it the second-largest dust source to EDC during the LGM."; (p. 9, l. 294) "~79 % of total deposition. Lower-latitude PSAs (AUS, SAF, PAP) supplied the remaining ~21 %"; (p. 9, l. 295) "with high-latitude sources totaling 84 %"; (p. 10, l. 321) "compared to 61% in our record when combining PAT, CWA, and PAP" |
| Concern | From Table S5 (Python): LGM PAT + AUS = 65.7 + 10.2 = 75.9 (text ~77); LGM NZ = 14.2, and the Results say "an average of 14%" (p. 7, l. 209), while ~11 % matches only the first quartile of the NZ box in Figure 3 (10.86 measured; mean cross 13.8, median 15.52); LGM PAT + NZ = 79.9 (text ~79) and AUS + SAF + PAP = 20.1 (text ~21); HS1 PAT + NZ = 74.8 + 7.1 = 81.9 (text 84); Holocene PAT + CWA + PAP = 49.0 + 0.0 + 11.0 = 60.0, given as 61 % in l. 321 and as 60 % in l. 326. All deviations exceed rounding (0.9 to 3.2 points). The qualitative statements hold (NZ remains second at 14.2 %). |
| Suggestion | Replace ~77 % by ~76 % (p. 9, l. 276), ~11 % by ~14 % (p. 9, l. 282), ~79 % and ~21 % by ~80 % and ~20 % (p. 9, l. 294), 84 % by 82 % (p. 9, l. 295) and 61 % by 60 % (p. 10, l. 321), or state which other averaging was used. |
| Status | verified (table values, quotations); inferred (sums, Python; Figure 3 positions measured by AB) |
| Severity | moderate |
| Source | S3, S4, AB, SD |

**GB-39 Aim 3 is answered by visual coincidence with proxy records, without a measure of agreement.**

| Field | Content |
|---|---|
| Check | P10 |
| Location | p. 10, l. 338 to 340; p. 3, l. 94 to 95; Figure 5 (p. 29) |
| Quotation | "Overall, our Holocene provenance record for PAT contributions is matching well with the SWW intensity proxies in Potrok Aike bog (see Figure 5)." |
| Concern | Aim 3 asks for shifts "in relation to regional climatic changes". The comparisons with Potrok Aike (Figure 5), the Darling Basin (p. 11, l. 366 to 372), Makgadikgadi and Etosha (p. 12, l. 392 to 398) and Coipasa are made by eye; search of p. 9 to 14 for "correlat", "significan", "statistic", "uncertaint", "±" finds no measure applied to them. The timescales of the proxy records and of EDC3 are not reconciled (GB-11). With a per-sample standard deviation of 32.1 points for Holocene PAT (Table S1, Python), visual coincidence of single minima is weak evidence. |
| Suggestion | In Section 4.3 put PAT and the Potrok Aike MDF on a common age grid and report a correlation with age-uncertainty-aware significance, or state that the comparison is qualitative. |
| Status | verified (absence of a measure by search); inferred (standard deviation, Python) |
| Severity | moderate |
| Source | SD |

**GB-40 The Potrok Aike record is called a bog, while Figure 5 and the cited source describe lake sediments, and SWW is defined only after first use.**

| Field | Content |
|---|---|
| Check | P38, P3 |
| Location | p. 10, l. 339 to 341; p. 11, l. 348 to 349; p. 29, l. 881 to 882 |
| Quotation | "the SWW intensity proxies in Potrok Aike bog (see Figure 5)" (p. 10, l. 339 to 340); (p. 11, l. 348 to 349) "(Potrok Aike bog 52°S; Lago Cardiel 48.9°S"; (p. 29, l. 881 to 882) "lacustrine sediments in Laguna Potrok Aike"; (p. 10, l. 340 to 341) "a weakening of South Westerlies Winds (SWW)" |
| Concern | Search "Potrok", p. 1 to 15 and 23 to 29: 4 lines; the archive is "Potrok Aike bog" twice, "Potrok Aike wind intensity record" once (p. 11, l. 351) and "Laguna Potrok Aike" in the Figure 5 caption and the cited title (Lisé-Pronovost et al., 2015). A bog is a peat archive, a different record type. SWW is used in l. 339 and defined in l. 340 to 341 as "South Westerlies Winds". GB-39 concerns how the same record is compared; here its name. |
| Suggestion | Replace "Potrok Aike bog" by "Laguna Potrok Aike" in p. 10, l. 339 to 340 and p. 11, l. 348 to 349; define at first use in l. 339 "the Southern Westerly Winds (SWW) intensity proxies" and write "a weakening of the SWW" in l. 340 to 341. |
| Status | verified (page images p. 10, 11, 29; reference list) |
| Severity | minor |
| Source | S2, AB, S4 |

**GB-41 Figure 5 is cited before Figure 4.**

| Field | Content |
|---|---|
| Check | P3, P4 |
| Location | p. 10, l. 340; p. 12, l. 405 |
| Quotation | "(see Figure 5)" (p. 10, l. 340); (p. 12, l. 405) "Figures 4 and S5" |
| Concern | First citations: Figure 1 p. 6, l. 183; Figure 2 p. 8, l. 244; Figure 3 p. 9, l. 281; Figure 5 p. 10, l. 340; Figure 4 p. 12, l. 405 (PP-31). Likewise Table S5 (first cited p. 6, l. 191) precedes Table S3 (p. 8, l. 246). GB-39 and GB-40 concern the content of the sentence that cites Figure 5. |
| Suggestion | Renumber Figures 4 and 5 and their citations (p. 10, l. 340; p. 12, l. 405; p. 13, l. 419) so that numbering follows first citation. |
| Status | verified |
| Severity | minor |
| Source | AB, S4 |

**GB-42 Several cited works have no reference entry, including the sources of most Australian end-members, and one entry is cited nowhere.**

| Field | Content |
|---|---|
| Check | P4 |
| Location | p. 11, l. 365; Suppl. p. 21, Table S4, column Reference; Suppl. p. 16 to 19, Table S2, column Reference; p. 18, l. 630 to 632; p. 17, l. 594 to 595 |
| Quotation | "with the previous Pb isotopic study (Gili et al., 2016) ." |
| Concern | The reference list (p. 16, l. 503 to p. 22, l. 846; 91 entries) has no entry for Gili et al. (2016) (p. 11, l. 365) and, for the supplement, which has no list of its own, none for Marx and Kamber (2010), Marx et al. (2005), McGowan et al. (2005) (Table S2, Australia), Diaz et al. (2018) (Table S2, Antarctica), Aarons et al. (2017) and Bory et al. (2010) (Table S4). Table S4 cites "Delmonte et al., 2004a", but the list has one Delmonte 2004 entry. The Marx works supply the Darling Basin patterns behind the dominant Holocene Australian source (p. 11, l. 366), which affects traceability; this is why the grade is moderate. Conversely, Gaiero, Brunet, Probst and Depetris (2007), Chemical Geology (p. 18, l. 630 to 632), is not cited ("Gaiero, 2007" in p. 8, l. 274 and p. 26, l. 862 refers to the single-author entry), and EPICA Community Members (2006) (p. 17, l. 594 to 595) is cited only in the caption of Figure S2. The citation of Gili et al. (2016) also has a space before the period. GB-07 concerns Aarons et al. (2017) as missing literature in the discussion; here the missing entries. |
| Suggestion | Add entries for Gili et al. (2016), Marx and Kamber (2010), Marx et al. (2005), McGowan et al. (2005), Diaz et al. (2018), Aarons et al. (2017) and Bory et al. (2010); resolve "2004a"; cite or delete Gaiero et al. (2007, Chemical Geology); write "(Gili et al., 2016)." in p. 11, l. 365. |
| Status | verified (absence in the reference list, p. 16 to 22; supplement text and page images) |
| Severity | moderate |
| Source | S4 |

**GB-43 The text cites Figure S4 for a Holocene trend that Figure S4 cannot show.**

| Field | Content |
|---|---|
| Check | P3 |
| Location | p. 12, l. 382; Figure S4 (Suppl. p. 8) |
| Quotation | "results show an increasing trend in SAF dust contribution to EDC ice core (Figure S4)" |
| Concern | Figure S4 shows one box plot per period (Early Holocene, YD, ACR, HS1, MIS3), with a single Holocene panel and no time axis, so it cannot show a trend within the Holocene; Table S5 supports the trend (Early 9.8, Late 11.6 %). A time series of SAF sub-regions is in Figure S3. GB-35 concerns the names of the SAF panels in Figure S3. |
| Suggestion | Cite Figure S3 or Figure 1 (panel SAF) and Table S5 in p. 12, l. 382, or add a Late Holocene panel to Figure S4. |
| Status | verified |
| Severity | minor |
| Source | AB, S4 |

**GB-44 The Holocene EDC versus EDML comparison uses the whole EDC Holocene against the EDML Early Holocene, outside the stated overlap, and no difference carries an uncertainty.**

| Field | Content |
|---|---|
| Check | P2, P3, P9, P15, P21 |
| Location | p. 12, l. 405 to 407; p. 13, l. 423 to 424; Figure 4, bars "Holo" in all five panels (p. 28); Suppl. p. 22, Table S5 |
| Quotation | "over their overlapping interval shared by both datasets, i.e., between 7.5 and 27 kyr BP" (p. 12, l. 406 to 407); (p. 13, l. 423 to 424) "EDC appears to receive substantially less PAT dust (-14%) but higher contributions of Australian dust (+12%) than EDML" |
| Concern | Table S5 gives EDML only for the Early Holocene (7.5 to 11.7 kyr). The stated -14 and +12 and the measured Holo bars of Figure 4 (PAT -13.97, AUS +12.44, SAF -0.53, NZ about 0, PAP +1.53) equal EDC "Holocene (2.8-11.7 kyr)" minus EDML Early Holocene (-13.7, +12.3, -0.5, +0.4, +1.6). With the like-for-like EDC Early Holocene they are -15.6, +14.1, -1.4, +2.6, +0.6 (Python). The bar therefore includes 60 EDC samples from 2.8 to 7.5 kyr BP that lie outside the overlap stated in p. 12, l. 407. The direction of PAT and AUS survives; NZ changes from +0.4 to +2.6. No difference carries an uncertainty: the standard errors of the EDC period means of PAT are 5.1 (ACR) and 9.8 points (YD) (Table S1, Python), larger than the ACR and YD differences, and the Monte Carlo spread is not reported (GB-16). The timescale of the EDML record is not stated, although synchronous changes are claimed (p. 13, l. 444 to 445; GB-11). GB-06 concerns the EDML values themselves; GB-41 the figure numbering of the same sentence; GB-36 the tentative status of the ACR and YD stated next to it. |
| Suggestion | Recompute the Holo bars and p. 13, l. 423 to 424 with the EDC Early Holocene (-15.6 % PAT, +14.1 % AUS) and label the bar "Early Holocene"; give bootstrap or Monte Carlo intervals for each difference; state the timescale of both records. |
| Status | verified (Table S5; Figure 4 bars measured by AB); inferred (differences and standard errors, Python) |
| Severity | moderate |
| Source | S3, S4, AB, SD |

**GB-45 For the ACR and YD the text swaps the PAT differences, attributes the YD enrichment to lower Southern African input and gives 7 instead of 9 YD samples.**

| Field | Content |
|---|---|
| Check | P2, P3, P15, P36 |
| Location | p. 12, l. 408 to 409; p. 13, l. 421 to 422; Figure 4, panels PAT, AUS and SAF, bars YD and ACR (p. 28); Suppl. p. 22, Table S5; Suppl. p. 13, Table S1, YD rows |
| Quotation | "(8 and 7 samples in ACR and YD, respectively, compared to 47 and 27 in EDML)" (p. 12, l. 408 to 409); (p. 13, l. 421 to 422) "the ACR and YD intervals exhibit a slight enrichment of Patagonian dust (+4 and +6.5%) in EDC, primarily at the expense of Southern African and Australian contributions" |
| Concern | From Table S5 (Python): PAT ACR 68.9 - 62.5 = +6.4, YD 63.1 - 58.4 = +4.7; the text gives the reverse order, and the measured bars of Figure 4 agree with Table S5 (PAT YD +4.81, ACR +6.49). For the ACR the compensation is as stated (SAF -4.4, AUS -7.4); in the YD SAF is +6.4 points higher in EDC (14.6 against 8.2), and the PAT gain is offset by AUS (-4.5), NZ (-3.9) and PAP (-2.4). The EDC YD SAF value rests on one sample (GB-26). Table S1 has 9 YD samples (11779, 11993, 12227, 12477, 12588, 12754, 12841, 12841, 12867 yr), and only these 9 reproduce the YD means of Table S5; Figure S4 shows at least 8 YD positions. The ACR count of 8 is correct. S4 proposed "+4.5 %" for the YD; Table S5 gives +4.7, which is used here. GB-36 concerns the tentative status of the same two periods; GB-44 the Holocene bar of the same figure. |
| Suggestion | In p. 13, l. 421 to 422 write "(+6.4 and +4.7 % in the ACR and YD, respectively)" and name the compensating sources per interval (ACR: AUS and SAF; YD: AUS, NZ and PAP, with SAF higher in EDC); in p. 12, l. 408 write "8 and 9 samples"; give n per period in Table S5 and in the captions of Figure 3 and Figure S4. |
| Status | verified (Table S5, Table S1 ages, quotations; Figure 4 bars measured by AB); inferred (differences, Python) |
| Severity | moderate |
| Source | S3, S4, AB, SD |

**GB-46 Discussion and Conclusion state the cause of the shift with stronger verbs than the evidence of temporal coincidence allows.**

| Field | Content |
|---|---|
| Check | P15 |
| Location | p. 14, l. 466 to 470; p. 14, l. 480 to 484; p. 9, l. 296; p. 13, l. 450; p. 1, l. 29 to 31 |
| Quotation | "Importantly, our data demonstrate that these feedback mechanisms influenced dust deposition not only in EDML" (p. 14, l. 466 to 467); (p. 14, l. 480 to 481) "As such those results confirm our previous study"; (p. 14, l. 483 to 484) "the massive decline in dust deposition that occurred between 18 and 15 kyr BP due to changing atmospheric transport dynamics" |
| Concern | The manuscript documents that the shift "coincides with" shelf submersion, Meltwater Pulse 1A and drainage reversals (p. 13, l. 450). Coincidence in time is the evidence; no analysis relates PAT contributions quantitatively to shelf area, sea level or drainage (search of the Results, p. 6, l. 173 to p. 7, l. 218, for "shelf", "sea level", "sea-level", "drainage": 0 hits). "Demonstrate" and "confirm" therefore claim more than shown, and sea-level rise and drainage reversal are called "feedback mechanisms" although no feedback is shown. The Discussion hedges the earlier flux decline ("The latter likely reflects intensified", p. 9, l. 296), the Conclusion drops the hedge ("due to"); the flux itself is taken from Fischer et al. (2007) (p. 5, l. 167). The Abstract attributes the shift in the same way (p. 1, l. 29 to 31). GB-36 concerns the timing basis of the shift; here the verbs. |
| Suggestion | Replace "demonstrate" (p. 14, l. 466) by "are consistent with the hypothesis that", "these feedback mechanisms" (l. 467) by "these mechanisms", "confirm" (l. 480) by "are consistent with", "due to" (l. 484) by "most likely due to", and adapt p. 1, l. 29 to 31; name in Section 4.4 an observation that would distinguish the shelf and drainage hypothesis from the climatic explanations of Section 4.3. |
| Status | verified (quotations; absence of a quantitative test by search) |
| Severity | major |
| Source | S4 |

**GB-47 The Conclusion does not return to aim 2, to the Holocene consensus question of aim 1, or to the iron fertilisation framing of the Introduction.**

| Field | Content |
|---|---|
| Check | P15, P10 |
| Location | p. 14, l. 471 to p. 15, l. 492 |
| Quotation | "(2) confronting and validating the EDC results from our REE pattern-based model against Sr-Nd isotopic data published in the literature" (p. 3, l. 93 to 94); (p. 15, l. 491) "with implications for biogeochemical fluxes" |
| Concern | Section 4.1 addresses aim 2, but the Conclusion has no statement on it (search of p. 14, l. 471 to p. 15, l. 492 for "isotop", "Sr", "Nd", "validat": 0 hits). The Holocene debate cited in p. 3, l. 92 to 93 is not resolved in words ("consensus": 1 hit in the manuscript, p. 3, l. 92). The Introduction motivates the study with dust-borne iron fertilisation and pCO2 (p. 2, l. 37 to 52), but "iron", "fertiliz" and "pCO2" occur only on p. 2 (4, 2 and 2 lines), none of the four aims addresses them, and the Conclusion ends with "implications for biogeochemical fluxes" without naming any. The absolute fluxes that could link to iron supply are not shown (GB-18). GB-02 concerns the priority claim and GB-36 the timing claim, GB-46 the verbs of the same Conclusion; here what it omits. |
| Suggestion | Add one sentence each to the Conclusion on the outcome of the Sr and Nd comparison, on what the record says about the Holocene debate, and on what the shift implies for iron supply to the Southern Ocean, or reduce the iron framing in p. 2, l. 37 to 52 to what the study delivers. |
| Status | verified (searches in text.json and page images p. 7 to 15) |
| Severity | minor |
| Source | S4, SD |

**GB-48 The Conclusion explains the inter-core differences by climate in the source areas, whereas Section 4.4 explains them by the position of the two drill sites.**

| Field | Content |
|---|---|
| Check | P15 |
| Location | p. 14, l. 486 to 487; p. 13, l. 424 to 428 |
| Quotation | "the relative contributions of PAT, SAF, NZ and AUS differed reflecting regional climatic dynamics in their respective source areas" (p. 14, l. 486 to 487); (p. 13, l. 424 to 425) "These differences are consistent with the geographic positioning of the two sites" |
| Concern | Both cores sample the same source areas, so climate in those areas cannot by itself produce differences between EDC and EDML. Section 4.4 attributes the differences to exposure of EDML to the Atlantic storm track and of EDC to polar vortex intrusions, i.e. to transport to the sites. The existence of spatial differences (aim 4) is unaffected, which is why the grade is not major; the reader cannot tell which explanation the authors hold. GB-47 concerns what the same Conclusion omits. |
| Suggestion | Rewrite p. 14, l. 486 to 487 to match Section 4.4, for example "differed, reflecting the different exposure of the two sites to mid-latitude and low-latitude air masses". |
| Status | verified |
| Severity | moderate |
| Source | S4 |

**GB-49 The author contribution statement names "P.B", which matches no author, and leaves two authors without a stated contribution.**

| Field | Content |
|---|---|
| Check | P4 |
| Location | p. 16, l. 497 to 499; p. 1, l. 4 to 5 |
| Quotation | "P.B performed the measurements; A.V., St. B and G.L. developed together the model; Si.B and St.B. analyzed the data" |
| Concern | The authors are Sibylle Boxho, Aubry Vanderstraeten, Nadine Mattielli, Goulven G. Laruelle, Aloys Bory, Paolo Gabrielli and Steeve Bonneville (p. 1, l. 4 to 5); "P.B" matches none. N.M. and A.B. are covered only by "All authors reviewed the manuscript". Is "P.G." meant (Paolo Gabrielli, who published the REE dataset, p. 4, l. 108)? Initials are written with and without periods ("St. B", "St.B."). |
| Suggestion | Correct the initials in p. 16, l. 497, state the contributions of N.M. and A.B., and use one form of initials (Si.B., St.B., P.G.). |
| Status | verified (initials against the author list); assumption (that P.G. is meant), formulated as a question |
| Severity | minor |
| Source | S4, S2 |

**GB-50 Eighteen reference entries print RTF control codes instead of dashes, accented letters and symbols.**

| Field | Content |
|---|---|
| Check | P16 |
| Location | p. 16, l. 528; p. 17, l. 553; p. 18, l. 606; p. 19, l. 693 to 694; p. 19, l. 703 to 707; p. 20, l. 714; p. 21, l. 795; p. 22, l. 821 |
| Quotation | "471\uc0\u8211{}501. https://doi.org/10.1191/0309133303pp386ra\" (p. 16, l. 528); (p. 19, l. 703) "Mall\uc0\u237{}n Pollux, Coyhaique, Province Ais\uc0\u233{}n" |
| Concern | Visible on the page images. Search of p. 16 to 22 for RTF codes or a trailing backslash: 35 printed lines (p. 16: 528; p. 17: 553, 556, 588, 590, 593; p. 18: 606, 632, 645 to 648, 653, 654; p. 19: 693, 694, 703 to 707, 710; p. 20: 714, 716, 742, 746, 747, 757, 758; p. 21: 795, 799, 817; p. 22: 821, 826, 828) in 18 entries: Bullard and McTainsh 2003; De Deckker et al. 2014; Dukes et al. 2018; Engelbrecht et al. 2019; Fletcher and Moreno 2012; Gaiero et al. 2007; Gingele and De Deckker 2005; Grousset and Biscaye 2005; Lisé-Pronovost et al. 2015; Markgraf et al. 2007; Markle et al. 2018; Moreno et al. 2010; Power et al. 2008; Quade and Kaplan 2017; Stone et al. 2010; Stuut et al. 2002; Veres et al. 2013; Wagner et al. 2021. |
| Suggestion | Re-export these entries from the reference manager as plain text (\u8211 as the page-range dash, \u8217 as apostrophe, \u237 í, \u233 é, \u241 ñ, \u176 °) and delete the trailing backslashes. |
| Status | verified (page images p. 16 to 22; line count in text.json) |
| Severity | minor |
| Source | S4 |

**GB-51 The reference list mixes citation styles and contains incomplete entries.**

| Field | Content |
|---|---|
| Check | P16 |
| Location | p. 16, l. 536 to 537; p. 17, l. 584 to 585; p. 18, l. 633 to 636; p. 20, l. 726 to 729; p. 20, l. 730 to 732; p. 20, l. 762 to 763; p. 22, l. 844 to 846 |
| Quotation | "Ding, Q., Steig, E., Battisti, D. et al. Winter warming in West Antarctica caused by central tropical Pacific warming. Nature Geosci 4, 398" (p. 17, l. 584 to 585); (p. 20, l. 729) "chronology for the EPICA Dome C ice core. Clim. Past." |
| Concern | Most entries follow "Name, Initials, Year. Title. Journal Volume, pages. DOI". Deviating: Ding et al. 2011 (year at the end, "et al." in the list); Gaiero et al. 2013 (initials first for co-authors, year in parentheses, "doi:" prefix); Yang et al. 2024 ("&", year in parentheses); Placzek et al. 2006 ("doi: https://"); Rudnick and Gao 2003 ("Holland HD, Turkian KK", the second editor being Turekian); Delmonte et al. 2007 (chapter number before the title); Caldenius 1932 ("pp."). Parrenin et al. 2007 lacks volume, pages and DOI. Journal names are partly abbreviated, partly in full. Within De Deckker et al., 2014 precedes 2010. Conformity with the journal style is an optional check (not run). |
| Suggestion | Bring the listed entries into the format of the majority, complete Parrenin et al. (2007), correct "Turkian" to "Turekian", use one form of journal names and order De Deckker et al. 2010 before 2014. |
| Status | verified (page images p. 16 to 22) |
| Severity | minor |
| Source | S4 |

**GB-52 The Figure 2 legend uses classes that neither the caption nor Table S4 defines.**

| Field | Content |
|---|---|
| Check | P29 |
| Location | Figure 2, legend and labels (p. 26); p. 8, l. 251 to 252 |
| Quotation | "The modeled isotopic signatures for the end of MIS3/LGM, HS1, ACR, and the YD (represented on Figure 2 by blue, cyan, green, and yellow filled symbols)" |
| Concern | (a) The legend label "Iso" is not explained. (b) The legend has "Iso Early Holocene" and "EDC Early Holocene" next to "Iso Holocene" and "EDC Holocene"; Table S4 has no Early Holocene group, and six Berkner Island rings are drawn in the lighter red of the "Early Holocene" class; whether "Holocene" means the whole or the late Holocene is not stated. (c) The text assigns blue to "the end of MIS3/LGM", the legend says "EDC LGM". (d) The domain label "Southern Central Western Argentina" differs from "Central Western Argentina (CWA)" (p. 4, l. 129). The figure cannot be read without text and supplement, which is why the grade is moderate. GB-37 concerns which data the symbols show; GB-14 the wrong table numbers of the caption; GB-36 the grouping of the YD in the quoted sentence. |
| Suggestion | Explain "Iso" (measured ice-core values) and the period limits of each legend class in the caption; give Table S4 an Early Holocene group or drop the class; state whether MIS3 samples are in the blue class; use one name for CWA. |
| Status | verified (caption, legend and Tables S3, S4 at the page images) |
| Severity | moderate |
| Source | AB |

**GB-53 Figure 5 cannot be read on its own: the time axis has no title or unit, and the blue band, dashed lines and gray zones are not explained.**

| Field | Content |
|---|---|
| Check | P29, P24 |
| Location | Figure 5, panels A and B (p. 29); Figure 5 caption, p. 29, l. 880 to 882 |
| Quotation | "Figure 5: Comparison of the contribution of Patagonian dust (PAT) to EDC ice core (A) and (B) the Median Destructive Field of isothermal remanent magnetization (MDF)" |
| Concern | (a) The x-axis carries only the numbers 0.5 to 3, with no title and no factor, unlike Figure 1. (b) A blue band bounded by dashed lines lies at 7.95 to 11.44 kyr (measured, ±0.034 kyr), and gray zones are drawn; the caption explains neither, and the band does not match "The 11 to 8 kyr BP period" (p. 10, l. 340). (c) The gray zones have no labels, and the YD zone ends at 12.89 kyr in panel A and 13.00 kyr in panel B. GB-39 concerns the comparison the figure supports; GB-41 its number; GB-40 the name of the lake in the same caption. |
| Suggestion | Add the axis title "Time (kyr BP)" or the factor, explain the band (with limits) and the zones in the caption, align the band with p. 10, l. 340 and draw the shading from the same limits in both panels. |
| Status | verified (measured) |
| Severity | minor |
| Source | AB |

**GB-54 The three y-axes of Figure S2 give no units, and panel B lacks the period shading of panels A and C.**

| Field | Content |
|---|---|
| Check | P29 |
| Location | Figure S2, panels A, B and C (Suppl. p. 4) |
| Quotation | "nssCa2+ flux"; "δ18O"; "deuterium excess" |
| Concern | The text gives the flux unit (µg m⁻² yr⁻¹, p. 5, l. 166), the axis does not; δ18O and deuterium excess have no ‰. Panels A and C show the period zones, panel B not, although the text uses panel B for the 18 to 15 kyr warming (p. 9, l. 299). GB-18 concerns what Figure S2 is cited for. |
| Suggestion | Add units to the three axis titles and the same period shading in panel B. |
| Status | verified |
| Severity | minor |
| Source | AB |

**GB-55 Figure S5 and Figure 1 show different EDC curves, although both are described as 9-step moving averages of the same record.**

| Field | Content |
|---|---|
| Check | P3 |
| Location | Figure S5, panels PAT and AUS, EDC line (Suppl. p. 10); Figure 1, panels PAT and AUS (p. 24); p. 6, l. 194 |
| Quotation | "Bold lines denote the mobile average over 9 steps." |
| Concern | Both curves were extracted column by column with axis calibration from the tick marks (AB). PAT: Figure S5 has its deepest early-Holocene minimum at 18 to 22 % around 8.85 to 8.9 kyr; there Figure 1 shows 39 to 45 %, with its minimum at 8.54 kyr (30.8 %); at 9.0 kyr Figure S5 gives 41.4 % against 54.2 %. AUS: the Figure S5 maximum near 10.1 kyr is 50.7 %, the Figure 1 maximum about 41 to 45 %. The minima "at 10, 8.6, and 6.3 kyr BP" (p. 6, l. 194) agree with Figure 1 but not with Figure S5 for the 8.6 kyr event. The quotation is the Figure 1 caption, p. 25, l. 852; KK-19 concerns its wording. |
| Suggestion | Plot both figures from the same smoothed series, or state in the Figure S5 caption how its smoothing differs (window, interpolation, sample set). |
| Status | verified (curves measured); assumption (cause), formulated as a question |
| Severity | moderate |
| Source | AB |

**GB-56 The period shading of Figure S5 is offset from the time axes of the panels.**

| Field | Content |
|---|---|
| Check | P24 |
| Location | Figure S5, all five panels (Suppl. p. 10); p. 6, l. 185 to 187 |
| Quotation | "Comparison between EDC and EDML ice cores in terms of dust provenance contributions (mobile average over 9 steps)" |
| Concern | The gray zones run through all panels at the same image position, but the PAT panel has another time scale than the four lower panels. The YD zone reads 11.56 to 12.88 kyr in the PAT panel and 11.67 to 12.98 kyr below, HS1 14.68 to 17.89 and 14.77 to 17.97 kyr (±0.011 kyr), against the limits 11.7, 12.9, 14.7 and 18 kyr (p. 6, l. 185 to 187). The offset (up to 0.14 kyr) exceeds the measurement uncertainty and matters for the 15 to 14 kyr comparison (p. 13, l. 445 to 446). GB-55 concerns the curves of the same figure; GB-11 the timescale behind the period limits. |
| Suggestion | Give all panels the same time axis, or draw the shading per panel from the period limits. |
| Status | verified (measured) |
| Severity | minor |
| Source | AB |

#### Minor corrections

| ID | Location | Quotation | Replacement | Source |
|---|---|---|---|---|
| KK-21 | p. 7, l. 220 to 221 | "in the Epica Dome C ice core" | "in the EPICA Dome C ice core" (title; p. 1, l. 18; p. 3, l. 88); GB-02 concerns the priority claim of the same sentence | S2 |
| KK-22 | p. 7, l. 229 | "in conjunction with regional climatic evolution (3)" | "in conjunction with regional climatic evolution; and (3)" | S4 |
| KK-23 | p. 7, l. 236 | "This shift already describes by Gili et al. (2022) and Vanderstraeten et al. (2023), appears" | "This shift, already described by Gili et al. (2022) and Vanderstraeten et al. (2023), appears"; GB-36 concerns the claim of the preceding sentence | S4 |
| KK-24 | p. 8, l. 246 | "(Table S3, e.i. Eq.3)" | "(Table S3; Eq. 3)"; GB-37 concerns the calculation of the same paragraph | S4 |
| KK-25 | p. 8, l. 249 | "where the mean isotopic signatures is represents by CIR PSA" | "where CIR_PSA represents the mean isotopic signature of each PSA"; see GB-37 | S4 |
| KK-26 | p. 8, l. 261 | "Persistance of high-latitude dust source to EDC" | "Persistence of high-latitude dust sources to EDC" | S4 |
| KK-27 | p. 8, l. 270 | "~763.10³ km²" | "~763 × 10³ km²" | S4 |
| KK-28 | p. 8, l. 272 | "those from SSA- to EDC" | "those from SSA to EDC" | S4 |
| KK-29 | p. 9, l. 300 | "before 14.5 kyr BP reflect a transport regime" | "before 14.5 kyr BP reflects a transport regime" | S4 |
| KK-30 | p. 9, l. 301 | "strong westerlies -a system" | "strong westerlies, a system" | S4 |
| KK-31 | p. 10, l. 311 | "«wet scavenging»" | "“wet scavenging”" (as "rainout" in p. 9, l. 297); GB-23 concerns the interpretation of the same passage | S4 |
| KK-32 | p. 10, l. 325 to 326 | "SSA input -down to 33%- compared" | "SSA input (down to 33%) compared"; GB-38 concerns the SSA value of the same sentence | S4 |
| KK-33 | p. 10, l. 327 | "vs. 23% and 11%, here - and a larger" | "comparable contributions from AUS and SAF (i.e., 23% and 14%, respectively, vs. 23% and 11% here) and a larger" | S4 |
| KK-34 | p. 10, l. 329 to 330 | "includes several McMurdo region sites (Section 4.2)" | "includes several McMurdo region sites (Section 2)"; the database is described in p. 4, l. 132 to 133; GB-07 and GB-15 concern the Antarctic result of the same passage | S4 |
| KK-35 | p. 10, l. 331; p. 13, l. 427 | "over the East Antarctic Plateau"; "located at the interior of EAP" | p. 10, l. 331: "over the East Antarctic Plateau (EAP)"; p. 13, l. 427: "located in the interior of the EAP" ("EAP" otherwise undefined); GB-07, GB-15 and GB-48 concern the content of these passages | S2, S4 |
| KK-36 | p. 10, l. 334 | "(Speirs et al., 2001)" | "(Speirs et al., 2010)" if the only Speirs entry (p. 21, l. 781) is meant; otherwise add the 2001 work; GB-07 and GB-15 concern the content of the same passage | S2, S4 |
| KK-37 | p. 10, l. 335 to 336 | "after 14.5 kyr BP during the ACR, YD reaching minimum values" | "after 14.5 kyr BP during the ACR and YD, reaching minimum values" | S4 |
| KK-38 | p. 10, l. 338 | "centered ~9 kyrs BP" | "centered at ~9 kyr BP"; GB-39 concerns the comparison of the same sentence group | S4 |
| KK-39 | p. 10, l. 339 | "is matching well with" | "matches well with"; GB-39, GB-40 and GB-41 concern the same sentence | S4 |
| KK-40 | p. 10, l. 341 | "Moreno et al. (2010);" | "Moreno et al., 2010;"; GB-40 concerns the SWW definition of the same line | S4 |
| KK-41 | p. 10, l. 342 to 343 | "(Quake and Kaplan, 2017)" | "(Quade and Kaplan, 2017)" (p. 11, l. 349; reference p. 20, l. 755) | S2, S4 |
| KK-42 | p. 10, l. 346 | "Fires co-emit mineral soil-dust particle" | "Fires co-emit mineral soil-dust particles" | S4 |
| KK-43 | p. 11, l. 354 | "Dust emission from PAP are primarily linked" | "Dust emissions from PAP are primarily linked" | S4 |
| KK-44 | p. 11, l. 366 | "As far as Australian dust contribution," | "Regarding the Australian dust contribution,"; GB-09 and GB-20 concern the Darling attribution of the same sentence | S4 |
| KK-45 | p. 11, l. 367 | "De Deccker et al. (2010)" | "De Deckker et al. (2010)" (reference p. 17, l. 557); see GB-09 and GB-20 for the same sentence | S2, S4 |
| KK-46 | p. 11, l. 374 | "(post-7.5 kry" | "(post-7.5 kyr" | S4 |
| KK-47 | p. 11, l. 376 | "El-Nino-Southern Oscillation (ENSO)" | "El Niño-Southern Oscillation (ENSO)" | S4 |
| KK-48 | p. 12, l. 384 to 385 | "suggesting strengthened dust transport from southern Africa suggesting strengthened dust transport from southern Africa (Stuut et al., 2002)" | "suggesting strengthened dust transport from southern Africa (Stuut et al., 2002)"; the phrase is printed twice; GB-21, GB-35 and GB-43 concern the SAF content of the same passage | S4 |
| KK-49 | p. 12, l. 396 | "include few substantial inputs" | "include a few substantial inputs"; GB-21 concerns the Etosha assignment of the same sentence | S4 |
| KK-50 | p. 12, l. 398 | "BP (Brook et al., 2011). The intermittent" | "BP; Brook et al., 2011). The intermittent" (the parenthesis opened in l. 397 is otherwise not closed) | S4 |
| KK-51 | p. 12, l. 399 | "likely reflect their low-frequency, high-magnitude nature of their dust emissions" | "likely reflect the low-frequency, high-magnitude nature of their dust emissions" | S4 |
| KK-52 | p. 12, l. 408 | "due to the limited number samples" | "due to the limited number of samples"; GB-36 and GB-45 concern the content of the same sentence | S4 |
| KK-53 | p. 13, l. 426 | "to receive dust from Patagonia dust brought in" | "to receive Patagonian dust brought in"; GB-48 concerns the explanation of the same passage | S4 |
| KK-54 | p. 13, l. 428 | "from such mid-latitude air masses incursions" | "from such incursions of mid-latitude air masses"; see GB-48 and KK-35 | S4 |
| KK-55 | p. 13, l. 439 | "(De Deccker et al., 2019" | "(De Deckker, 2019" (single author, reference p. 17, l. 551); GB-07 concerns the literature of the same passage | S2, S4 |
| KK-56 | p. 13, l. 441 to 442 | "favoring poleward STJ trajectories and interactions with PFJ (Ding et al., 2011) - and increased aridity" | "climate circulation patterns, favoring poleward STJ trajectories and interactions with PFJ (Ding et al., 2011), and increased aridity" (replaces the unpaired dashes of l. 441 and 442 by commas) | S4 |
| KK-57 | p. 14, l. 457 | "redirecting large portion of river catchment" | "redirecting a large portion of the river catchments" | S4 |
| KK-58 | p. 14, l. 466 | "transport from low-latitude to Antarctica" | "transport from low latitudes to Antarctica"; GB-46 concerns the verbs of the following sentence | S4 |
| KK-59 | p. 14, l. 481 | "showing similar shift that we ascribed" | "showing a similar shift that we ascribed"; GB-46 and GB-47 concern the same passage | S4 |
| KK-60 | p. 14, l. 488 | "glacial-eustatic and hydrological feedbacks" | "glacial-eustatic and hydrological changes"; GB-46 explains why no feedback is shown, GB-47 concerns the same Conclusion | S4 |
| KK-61 | p. 16, l. 501 | "APPENDIX S. SUPPLENTARY DATA. Supplementary data to this article" | "APPENDIX S. SUPPLEMENTARY DATA. Supplementary data to this article are available online." | S4 |
| KK-62 | p. 20, l. 748 | "Environùental characterization" | "Environmental characterization" | S4 |
| KK-63 | p. 21, l. 800 | "Sudgen, D. E., McCulloch, R. D." | "Sugden, D. E., McCulloch, R. D." (text p. 8, l. 266; author spelling on https://nora.nerc.ac.uk/id/eprint/11307), and move the entry to its alphabetical place | S2, S4 |
| KK-64 | Figure 2 caption, p. 26, l. 863 | "Note that the SAF and AUS domain is more extended than showed in the Figure." | "Note that the SAF and AUS domains extend beyond the area shown in the figure."; GB-14, GB-37 and GB-52 concern other parts of Figure 2 | S4, AB |
| KK-65 | Figure 2, x-axis tick labels (p. 26); Figure 3, y-axis tick labels (p. 27); Figure S4, y-axis tick labels (Suppl. p. 8) | "0,700" to "0,730"; "0,00" to "100,00" | "0.700" to "0.730"; "0" to "100" (decimal point as in the text; compared: Figure 2 x-axis 7 labels, Figure 3 both panels 11 labels each, Figure S4 11 labels); GB-37, GB-52 and KK-64 concern other parts of Figure 2 | AB |
| KK-66 | Figure 4 caption, p. 28, l. 875 | "Histograms representing the contribution percentage difference" | "Bar charts of the difference in contribution (percentage points)"; GB-14 corrects the table number of the same caption, GB-30 its abbreviations, GB-44 and GB-45 concern the bars | AB |
| KK-67 | Figure S5, y-axis title (Suppl. p. 10) | "PAS EDC Contribution and PSA EDML Contribution ( in %)" | "PSA EDC contribution and PSA EDML contribution (%)"; GB-55 and GB-56 concern the same figure | AB |
| KK-68 | Suppl. p. 21, Table S4, rows 1 and 2, column Localisation | "Epica dome C" | "EPICA Dome C"; GB-07, GB-37 and GB-42 concern the content of the same table | S2 |

#### Verification log

| ID | Check | Checked | Values | Result |
|---|---|---|---|---|
| PP-35 | P4 | Numbering of sections, figures, equations and supplement elements | Sections 1 to 5 with 4.1 to 4.4; Figures 1 to 5, one caption each (p. 25 to 29); Equations (1) to (4) (p. 4, l. 125; p. 5, l. 141; p. 8, l. 247 and 250); Figures S1 to S5 and Tables S1 to S5 once each | no finding on gaps or duplicates; order see GB-41 |
| PP-36 | P4 | Targets of the remaining cross-references | Eq. 1 (p. 4, l. 120), Eq. 2 (p. 4, l. 138), Table S2 (p. 4, l. 128), Table S5 (p. 6, l. 191; p. 7, l. 216 to 218; p. 9, l. 281 and 295; p. 10, l. 318 and 326), Figure 1, Figure 2, Figure 3, Figure S2, Figure S3, Figures 4 and S5, Section 4.2 (p. 9, l. 310) | each target exists and shows what is referred to; no finding |
| PP-37 | P1, P3, P15, P31 | Eq. 3 and 4 with Table S3 end-members, per period from Table S1 means and per sample | per period (87Sr/86Sr, εNd): Late Holocene 0.7101, -5.22; Early Holocene 0.7102, -4.76; Holocene 0.7101, -4.99; YD 0.7094, -5.39; ACR 0.7082, -2.91; HS1 0.7076, -1.55; LGM 0.7083, -2.62; MIS3 0.7083, -3.37; cited EDC LGM 0.708, -1.66 to -2.46, Holocene ~0.710, -4.51 to -5.68 (p. 7, l. 238 to 240); per sample YD and ACR points of Figure 2 reproduced to 0.0001 and 0.04 (for example 0.7274, -17.87 computed against 0.7274, -17.89 measured) | reproducible; agreement with the cited EDC values for period means; limits see GB-37, YD grouping see GB-36 |
| PP-38 | P2 | Discussion values against Table S5 | Holocene AUS, PAP, SAF 23.1, 11.0, 10.7 (text 23, 11, 11); LGM 10.2, 3.6, 6.3 (text 10, 4, 6); Holocene PAT, NZ 49.0, 5.9 (text 49, 6); LGM SSA 65.7 + 3.6 + 0.0 = 69.3 (text ~70); EDML LGM NZ 6.2 (text ~6) | no finding; other values see GB-38, GB-44, GB-45 |
| PP-39 | P2, P3 | EDC minus EDML for LGM and HS1 (p. 13, l. 417 to 421) and all 25 bars of Figure 4 against Table S5 | LGM NZ +8.0, PAT -8.0 (text +8 and equivalent reduction); HS1 PAT +3.2, PAP -0.2, SAF -5.3, AUS +1.9, NZ +0.6, maximum 5.3 (text "not exceeding ~5%"); Figure 4 bars within 0.3 of Table S5 (±0.23) | no finding for LGM and HS1; Holocene, ACR and YD see GB-44, GB-45 |
| PP-40 | P3, P24 | Figure S5, EDC PAT decline 15 to 14 kyr (p. 13, l. 445 to 446) | EDC PAT 71.4 % at 15.0 kyr, 73.9 % at 14.5 kyr, 61.9 % at 14.0 kyr; EDML from about 60 % to 35 to 45 % between 14.5 and 14 kyr | no finding; curve differences see GB-55, shading see GB-56 |
| PP-41 | P24 | Figure 5, band and zone edges | blue band 7.95 to 11.44 kyr; YD zone A 11.71 to 12.89, B 11.71 to 13.00 kyr; HS1 A 14.68 to 17.99, B 14.75 to 18.03 kyr; axis 2.85 to 33.69 kyr (±0.034) | see GB-53 |
| PP-42 | P15 | Each Conclusion statement against a Results or Discussion locus | first record (p. 14, l. 472 to 473): p. 6, l. 182 to 183; glacial dominance (l. 474 to 476): Table S5, PAT 65.7 to 74.8 %, PAT + NZ 79.4 to 81.9 %; rise of AUS, PAP, SAF (l. 478 to 480): 23.1, 11.0, 10.7 against 10.2, 3.6, 6.3 %; decoupling (l. 482 to 484): p. 13, l. 445 to 450; synchronous changes (l. 486): p. 13, l. 444 to 447; paleolake desiccation (p. 15, l. 489): p. 11, l. 358 to 360 | supported apart from timing (GB-36), verbs (GB-46), omissions (GB-47) and cause of differences (GB-48) |
| PP-43 | P15, P9 | Proposals and future work in Discussion and Conclusion | search p. 7, l. 219 to p. 16, l. 501 for "future", "further stud", "further work", "further research", "should", "recommend", "outlook", "perspective", "we suggest", "need to", "will be": one hit, p. 16, l. 496 ("should be addressed to Si.B."), not a proposal | no outlook proposals; no finding |
| PP-44 | P4 | Citations against the reference list in both directions | 91 entries (p. 16, l. 503 to p. 22, l. 846); in-text citations from text.json p. 1 to 15 and 23 to 29; years agree except Speirs | deviations see GB-42, KK-36, KK-41, KK-45, KK-55, KK-63; DOIs not resolved (optional check) |
| PP-45 | P16 | Language and setting of Discussion, Conclusion, declarations, references and captions of Figures 2, 4, 5 at page images p. 7 to 22, 26, 28 | extraction artefacts not raised: "c Author(s)" (page shows ©), layout of Eq. 4 in text.json (typeset correctly), "Lisé-/Pronovost" (word hyphen), superscripts in 87Sr/86Sr | language see KK-21 to KK-68, setting see GB-50, GB-51 |
| PP-46 | P30 | Reported errors and corrections | none in text, captions or supplement | no finding |
| PP-47 | Merging (ZF) | Locations of all findings and minor corrections against the printed margin numbers | The location listing of `formatpruefung.py` gives 405 location ends (398 "without entry", 7 "on another page"), all because `text.json` numbers lines per page, not by margin number; 173 printed margin numbers in the text layer agree with the mapping page line plus offset of the segment table; pages 1, 4, 5 and 8 (superscripts and formula lines) counted from margin numbers 15 and 20, 120, 125 and 130, 140 and 145, 245, 250 and 255 at the page images; all 557 line references of this report exist in that mapping, and 133 quotations with a stated line range were found within it, first word on the first and last word on the last line | no finding; S4 gave the author list as lines 6 to 7 of p. 1, corrected to p. 1, l. 4 to 5 (GB-49); AB's range "l. 380 to 392" crosses a page and is written p. 11, l. 379 to p. 12, l. 392 (GB-35) |
| PP-48 | Merging (ZF) | Wording of quotations and embedded values | every quotation searched verbatim in `text.json` or `supplement/text.json` (normalised for line breaks, ligatures and superscripts); figure-internal labels (GB-29, GB-35, GB-52, GB-54, KK-65, KK-67) checked by AB at the page images; sums, differences, counts and test values of the merged findings recomputed with Python from Table S1 (241 rows) and Table S5 | corrected during merging: SD's search for "known" (1 hit, p. 4, l. 105, not a test; GB-13); S4's "+4.5 %" for the YD replaced by +4.7 from Table S5 (GB-45) |
| PP-49 | Merging (ZF) | Hints outside the checklists of all six instances, classified | 53 hints: covered by a responsible instance and merged; three not covered and confirmed at the page images became findings or corrections with source ZF: Antarctic rows of Table S2 not normalised (GB-15), Darling12 longitude and Kuiseb2inf5 Dy (GB-22), language of Segment 1 and of p. 4 (KK-01, KK-04 to KK-07, KK-09 to KK-11, part of GB-02); not raised: Figure 3 caption naming only HS1, ACR and YD for Figure S4 (treated by AB at the same caption), one Late Holocene sample with ANT 33.1 % (period means support the text), εNd of the Table S3 end-members and the content of Delmonte et al. (2004) (factual checks, optional) | no further finding |
| PP-50 | Merging (ZF) | Conflicting readings between instances, decided at the manuscript | S4 proposed Table S5 instead of Table S1 in p. 6, l. 183; S2 counted the citation as correct; Table S1 groups samples by period, so no correction (GB-18); YD PAT difference +4.5 (S4), +4.7 (S3, SD), +4.8 (AB, measured): Table S5 gives +4.7 (GB-45); AB graded the Holocene isotope comparison major, S4 and SD moderate: major retained (GB-37); AB-GB-04 split: wrong table numbers into GB-14, legend classes in GB-52 | decisions stated in the findings named |

## Optional checks

| Area | What it needs | Responsible | Run |
|---|---|---|---|
| DOI resolution | one fetch per reference entry with DOI | `science-quellenapparat-pruefung` | no |
| Citation style | the name of the style | `science-zitierstil-harvard-ctr` or the style rules of the journal | no |
| AI statement against publisher policy | the policy of the target publisher | this review, on request | no |
| Relation to the authors' own prior work | the authors' prior work | this review, on request | no |
| Journal requirements | the author guidelines of the target journal | this review, on request | no |
| Factual accuracy | access to the sources of the checked statements and a selection of sections | `science-faktenbeleg-pruefung`, `geo-frage-belegbasiert-klaeren` | no |

## Limits of this review

- Checked version: egusphere-2025-5046.pdf, 29 pages, SHA-256 f598b53d01e375844cfb549eb05b9a3407bb30cae553e603c125d5f14886c722, with supplement egusphere-2025-5046-supplement.pdf, 22 pages, SHA-256 759cfa14195948f5772d3d6d696081932424f4296e51c812415527ed3b108ea6.
- Unreadable sources (full text not accessible, abstract or record only): Vanderstraeten et al. (2023); Coppo et al. (2022); Delmonte et al. (2008); Delmonte et al. (2017); Engelbrecht et al. (2019); Martínez-García et al. (2014); Veres et al. (2013); Delmonte et al. (2004). Gabrielli et al. (2010) was read through fetch and summary tools, not page by page. The merging step did not reopen literature; statements about sources rest on the access logged by the instances and are marked inferred where only an abstract was read.
- Findings with status assumption: 12 of 56 contain a sub-statement with status assumption; in each case it is formulated as a question.
- Optional checks run: 0 of 6.
- Omitted instances: none.
- Discarded findings: 0. No instance finding lacked a mandatory field or was refuted at the manuscript; two sub-statements were corrected (PP-48) and one proposed correction was not adopted (PP-50).
- Merged findings: the six instances delivered 84 substantive findings and 96 minor corrections (180 entries); merging combined them into 54 substantive findings and 60 minor corrections (114 entries), so 66 entries were merged into others. The merging step added 2 substantive findings (GB-15, GB-22) and 8 minor corrections, and contributed to GB-02 and KK-02. 142 pairs with overlapping locations remained separate, each with a cross-reference.
- Language: the quotations contain no dash characters other than the hyphen; the figures were measured by instance AB on 300-dpi renderings, the other page images are 150 dpi.
