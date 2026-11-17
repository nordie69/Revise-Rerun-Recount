# Review report: Quantifying Southern Hemisphere dust sources during the Last Glacial-Interglacial Transition using rare earth elements in the EPICA Dome C ice core

| Field | Value |
|---|---|
| Manuscript | Boxho, S., Vanderstraeten, A., Mattielli, N., Laruelle, G. G., Bory, A., Gabrielli, P. and Bonneville, S. (2025) Quantifying Southern Hemisphere dust sources during the Last Glacial-Interglacial Transition using rare earth elements in the EPICA Dome C ice core, preprint egusphere-2025-5046, https://doi.org/10.5194/egusphere-2025-5046 |
| Checked version | egusphere-2025-5046.pdf, 29 pages, SHA-256 f598b53d01e375844cfb549eb05b9a3407bb30cae553e603c125d5f14886c722; supplement egusphere-2025-5046-supplement.pdf, 22 pages, SHA-256 759cfa14195948f5772d3d6d696081932424f4296e51c812415527ed3b108ea6 |
| Date | 2026-10-22 |
| Language | English |
| Review instances | Segments 1 to 4 (S1 to S4), figures (AB), study design and method (SD); the six review instances ran as separate agents; no instance omitted |
| Note | Line numbers are the printed margin numbers, confirmed on the page images; the supplement has no margin numbers, so supplement locations give table or figure, row or panel and supplement page ("Suppl. page"). Calculations in Python. |

## Summary

The manuscript is a modelling study that applies the authors' constrained least-squares unmixing algorithm DEPOT (MATLAB lsqnonneg, non-negativity constraint, 2000 Monte Carlo runs per sample, median as estimate) to a published rare earth element (REE) record of the EPICA Dome C (EDC) ice core (Gabrielli et al., 2010). Of 294 dust samples, 279 with complete patterns were fitted with 13 UCC-normalised REE (Gd removed) against a database of 217 source patterns from seven potential source areas (Patagonia, Central Western Argentina, Puna-Altiplano, Southern Africa, Australia, New Zealand, Antarctica), and 241 samples with a fit correlation R ≥ 0.67 were retained (2852 to 33699 yr BP, EDC3 chronology). Patagonia supplies 65.7 to 74.8 % of the dust on average in MIS3, the LGM and HS1 and 49.0 % in the Holocene, while Australian, Southern African and Puna-Altiplano shares rise after about 14.5 kyr BP (Holocene 23.1, 10.7 and 11.0 %). The record is checked against Sr-Nd literature data with an isotope mass balance (Eq. 3 and 4, Fig. 2) and compared with the authors' EDML provenance record; the shift is attributed to Patagonian shelf submergence during Meltwater Pulse 1A and to drainage reorganisation in Patagonia.

## Strengths

1. The supplement gives the per-sample medians (Table S1) from which every period mean in Table S5 can be recomputed; all EDC entries of Table S5 follow from Table S1 to 0.1 percentage points, and the sample bookkeeping closes (294, 279, 241, 86 %, mean R 0.852) (PP-08, PP-20). Every period statistic in the text can therefore be checked by a reader, which is what made the checks in GB-36 and GB-50 possible.
2. The main figures are drawn from the tabulated output: raw peaks and the 9-point moving averages of Fig. 1 agree with Table S1, the LGM panel of Fig. 3 with Table S1, the LGM and HS1 bars of Fig. 4 with Table S5 within 0.4 points, and the modelled points of Fig. 2 with Eq. 3 and 4 applied to Tables S1 and S3 (PP-28, PP-30, PP-46, PP-56).
3. The input data of the comparison are published row by row: 217 source patterns with location, sample type and reference (Table S2), end-member isotope values (Table S3) and 35 measured ice-core isotope values (Table S4) (PP-11, PP-14). The source matrix can thus be audited, which is how the duplicate and the apparently non-normalised rows were found (GB-09, GB-10).
4. The manuscript discloses its data limits where the data are introduced (sampling gap 21.7 to 27.3 kyr BP with four samples, 15 incomplete patterns, removal of Gd) and states that the ACR and YD results are tentative (PP-09, PP-44); the EDC and EDML comparison is restricted to the common interval, and for the LGM this restriction does not change the result (PP-45).

## Weaknesses

1. The uncertainty and the identifiability of the unmixing are not shown: the Monte Carlo spreads are not reported and the input uncertainty is set below the analytical uncertainty reported for Holocene samples (GB-13), no test shows that 217 candidate patterns can be resolved from 13 values (GB-12), the Antarctic end-members appear not to be UCC-normalised (GB-10), and the R threshold does not correspond to the stated significance level (GB-15). Report percentiles per sample and period, rerun the Monte Carlo with period-specific analytical uncertainties, add a recovery test with synthetic mixtures, and correct and rerun the Antarctic rows.
2. Several central statements go beyond what the design shows: the Holocene validation against EDC rests on measurements from other sites (GB-33), the shift dated to the ACR onset lies within the glacial per-sample spread (GB-22), the larger Holocene variability is not separated from sampling density, integration time and analytical noise (GB-38), the attribution to shelf submergence is stated as demonstrated (GB-03), and the Conclusion explains the EDC and EDML differences by a mechanism the Discussion does not develop (GB-54). Test the timing and the variability quantitatively and phrase the mechanisms as hypotheses consistent with the record.
3. The EDC and EDML comparison of aim 4 cannot be reproduced as stated: the EDML values differ from the published record and come from a different method configuration (GB-49), and the reported differences swap the ACR and YD values and use unequal Holocene windows (GB-50). Rerun EDML with the identical configuration and recompute all differences over matched windows.
4. Many reported values, figure references and cited statements do not match the tables, figures or sources: values in the Discussion (GB-36), the South Altiplano and South Puna statements (GB-24, GB-44), Figure S3 (GB-31), the panel labels of Fig. 3 (GB-28), sub-regional attributions without data (GB-20), the documentation of Table S1 and of the inputs (GB-08, GB-18), and reproductions of the literature (GB-04, GB-35, GB-40, GB-46, GB-48, GB-51). Regenerate all figures and text values from one model output, deposit data and code, and check each cited statement against its source.

## Findings by segment

### Segment 1: Title, abstract, introduction (p. 1 to 3)

#### Substantive findings

**GB-01 The record span and the term LGIT are given with different limits.**

| Field | Content |
|---|---|
| Check | P2, P15 |
| Location | p. 1, l. 18; p. 3, l. 90 to 91; p. 6, l. 182 and l. 187; p. 9, l. 302 to 304; p. 12, l. 407 and l. 411; Supplement Table S1 |
| Quotation | "from 33.7 to 2.9 kyr BP"; "during the LGIT from 33.6 kyr to"; "provenance pattern until the onset of the LGIT"; "BP until 2.7 kyr BP)." |
| Concern | Table S1 runs from 2852 to 33699 yr BP, which rounds to 2.9 and 33.7 kyr BP as in l. 18 and l. 182. Lines 90 to 91 give 33.6 to 2.8 kyr BP, l. 187 ends the Holocene at 2.8 kyr BP, and l. 304 gives 2.7 kyr BP. The term LGIT covers the whole record at l. 90 to 91, begins at about 14.5 kyr BP at l. 302, and refers to the EDC and EDML overlap of 7.5 to 27 kyr BP at l. 407 to 411. A reader cannot tell which interval a statement "during the LGIT" refers to. |
| Suggestion | Define the LGIT once in Section 1 (for example as the deglacial interval) and write "the record (33.7 to 2.9 kyr BP)" elsewhere; replace 33.6 and 2.8 at l. 90 to 91 and 2.7 at l. 304 by 33.7 and 2.9; state at l. 187 whether 2.8 kyr BP is a period limit or the end of the record; replace "until the onset of the LGIT" at l. 302 by "until ~14.5 kyr BP". |
| Status | verified |
| Severity | minor |
| Source | S3, S4 |

**GB-02 The first-time quantification claim of the abstract is not qualified and has no search basis, although the manuscript itself cites earlier quantitative source estimates.**

| Field | Content |
|---|---|
| Check | P28 |
| Location | p. 1, l. 19; p. 3, l. 74 to 76; p. 7, l. 220; p. 12, l. 403; p. 14, l. 472 |
| Quotation | "Using a statistical unmixing algorithm on 241 samples, we quantify for the first-time"; "we presented the first" |
| Concern | The record is new in its temporal continuity, and l. 220, 403 and 472 qualify the claim with "continuous". The abstract does not: it claims a first-time quantification of contributions as such, and the manuscript names no databases, search terms or search date for any priority claim. It reports earlier quantitative estimates itself: Coppo et al. (2022) "estimated LGM dust composition over EA as 64% from SSA, 15% from Antarctica, 11% from AUS," (l. 277 to 278) and give Holocene shares (l. 324 to 328). According to Vallelonga et al. (2010, see GB-39), Revel-Rolland et al. (2006), cited at l. 439 to 440, estimated an Australian contribution of 10 to 20 % in glacial and up to 50 % in interglacial EDC dust. The claim at l. 74 to 75 ("the first quantitative apportionment algorithm based on REE pattern fitting") is likewise given without a search basis. |
| Suggestion | In the abstract (l. 19) replace "for the first-time" by the specific novelty, for example "a continuous, sample-by-sample quantification", acknowledge the earlier discrete estimates (Revel-Rolland et al., 2006; Coppo et al., 2022) near l. 72 to 76, and qualify l. 74 or state the literature search behind it. |
| Status | verified (wording and the estimates cited in the manuscript); inferred (Revel-Rolland et al. 2006 percentages, reported in Vallelonga et al. 2010, not read in the original) |
| Severity | moderate |
| Source | S1 |

**GB-03 The attribution of the provenance shift to shelf submergence and Patagonian drainage reorganisation is stated as shown by the data, although the design establishes only a coincidence in time.**

| Field | Content |
|---|---|
| Check | P10, P15, P25 |
| Location | p. 1, l. 29 to 31; p. 13, l. 450 to 452; p. 14, l. 466 to 468; p. 14, l. 480 to 484; p. 14, l. 488; Supplement Table S2, column "Type of sample" |
| Quotation | "We attribute the shift in provenance"; "Importantly, our data demonstrate"; "that these feedback mechanisms influenced dust deposition not only in EDML"; "As such those results confirm our"; "18 and 15 kyr BP due to changing atmospheric transport dynamics." |
| Concern | The data show a change in modelled provenance and its synchrony with EDML (l. 444 to 447), and the Discussion is cautious at l. 296 ("likely reflects") and l. 450 ("coincides"). The mechanisms (shelf flooding during Meltwater Pulse 1A, drainage reversals, transport efficiency) come from cited studies (l. 450 to 460); no EDC data set tests them, and the manuscript gives no change-point estimate, age uncertainty or comparison with competing drivers. It names competing drivers itself: rainout and wet scavenging, moisture-source shifts and transport efficiency (l. 296 to 299, l. 310 to 314, l. 465 to 466). The database cannot fingerprint the shelf: no Table S2 entry is a shelf or marine sediment, the Patagonian entries are aeolian dust, topsoil and ephemeral-lake samples, so a lower Patagonian share is compatible with less shelf dust, less onshore dust or more low-latitude dust. Yet the Abstract attributes the shift (l. 29 to 31), Section 4.4 writes "our data demonstrate" (l. 466), the Conclusion writes "confirm" (l. 480) and attributes the deposition decline with "due to" (l. 484) where l. 296 says "likely reflects". Sea-level rise and drainage reversal act as forcings, not as feedbacks (l. 467, l. 488). GB-22 shows in addition that the EDC timing of the shift is less sharp than ~14.5 kyr BP. Graded major: the attribution is a conclusion of the Abstract and the answer to aim 3. |
| Suggestion | Phrase the attribution as a hypothesis consistent with the record in the Abstract (l. 29 to 31), Section 4.4 (l. 466 to 470) and the Conclusion (l. 480 to 484): "our data are consistent with" for "our data demonstrate", "support the timing reported in" for "confirm", "likely reflecting" for "due to"; write "these mechanisms" at l. 467 and "hydrological processes" at l. 488. Alternatively test it: estimate the timing of the Patagonian decline with a change-point method that includes EDC3 age uncertainty, compare it with the timing of the competing drivers (δ18O, deuterium excess, nssCa flux, sea level), and add shelf or coastal sediments as a separate end-member group. |
| Status | verified (wording, the competing drivers named in the manuscript, sample types in Table S2); inferred (that the design cannot separate the drivers) |
| Severity | major |
| Source | S4, SD |

**GB-04 The upper bound of the iron-fertilisation CO2 drawdown (~40 ppmv) is not found in either cited source.**

| Field | Content |
|---|---|
| Check | P13 |
| Location | p. 2, l. 40 to 42 |
| Quotation | "Enhanced iron delivery by atmospheric dust during glacial periods are modelled to have lowered the atmospheric pCO2 by ~20 to 40 ppmv" |
| Concern | Framing provenance as a constraint on dust-driven iron fertilisation is apt, but the range is wider than the sources report. Lambert et al. (2015, Geophysical Research Letters 42, 6014 to 6023) state in the Key Points "Iron fertilization reduced LGM atmospheric CO2 levels by 20 ppm"; Lambert et al. (2021, Earth and Planetary Science Letters 554, 116675) give "The model-calculated range of CO2 change for global-scale IF is between 12 and 29 ppmv" with a median of 18.5 ppmv. The upper bound of 40 ppmv exceeds the highest cited value by 11 ppmv (40 minus 29 = 11; 11 / 29 = 0.38, about 38 %). Graded moderate rather than minor: the number is not a matter of form, and a reader who follows the citations cannot find it. |
| Suggestion | At l. 41 replace "~20 to 40 ppmv" by the range the sources give (about 12 to 29 ppmv, central estimates near 20 ppmv), or add the source that reports up to 40 ppmv. |
| Status | verified (both sources read by instance S1 in author copies) |
| Severity | moderate |
| Source | S1 |

**GB-05 Aarons et al. (2017), a provenance study of East Antarctic dust across the same transition with REE and Sr-Nd, supplies most measured late glacial and Holocene values of Fig. 2 but is neither discussed nor in the reference list.**

| Field | Content |
|---|---|
| Check | P14 |
| Location | p. 3, l. 72 to 74; p. 8, l. 254 to 259; Supplement Table S4, column "Reference" (Suppl. page 21); Fig. 2 caption (p. 26, l. 857 to 866); reference list (p. 16 to 22) |
| Quotation | "Previous studies using REE patterns in Antarctic ice cores (e.g.," |
| Concern | Table S4 lists 18 rows "Aarons et al. (2017)" from Taylor Glacier (confirmed on the page image). The study is Aarons, S.M., Aciego, S.M., Arendt, C.A. et al. (2017) Dust composition changes from Taylor Glacier (East Antarctica) during the last glacial-interglacial transition: a multi-proxy approach. Quaternary Science Reviews 162, 60 to 71, https://doi.org/10.1016/j.quascirev.2017.03.011. It reports that "The increased isotopic variability during the early Holocene suggests a shift in dust provenance" and attributes early Holocene dust to "a combination of both local Ross Sea Sector dust sources and SSA". This precedes the manuscript's central finding (a provenance shift with a more variable Holocene) and offers a local Antarctic interpretation that the manuscript rejects for EDC. Section 4.1 uses these Taylor Glacier values as "measured" evidence (GB-33), but does not say that the site lies in the Ross Sea sector near the McMurdo sources. The missing reference list entries for the supplement sources are GB-57. |
| Suggestion | In the introduction (l. 72 to 74) and in Section 4.1 state what Aarons et al. (2017) found and how its local-source interpretation relates to the negligible Antarctic contribution at EDC; name the sites of the measured values in the caption of Fig. 2. |
| Status | verified (Table S4 on the page image; study read by instance S1 in an author copy; absence from the reference list) |
| Severity | moderate |
| Source | S1 |

#### Minor corrections

| ID | Location | Quotation | Replacement | Source |
|---|---|---|---|---|
| KK-01 | p. 1, l. 20 | "During the Marine isotope 3 (MIS3)" | "During Marine Isotope Stage 3 (MIS3)" | S2 |
| KK-02 | p. 1, l. 27 | "Comparison with the EDML ice core" | "Comparison with the EPICA Dronning Maud Land (EDML) ice core" | S2 |

#### Verification log

| ID | Check | Checked | Values | Result |
|---|---|---|---|---|
| PP-01 | P13 | p. 2, l. 41 to 42, second clause "a significant portion of the glacial-interglacial pCO2 difference" | Lambert et al. (2021) abstract: "About one quarter of that difference is thought to be due to a stronger biological pump" | no finding for this clause; the number is GB-04 |
| PP-02 | P13 | p. 2, l. 62 to 63, factor between LGM and interglacial dust flux at EDC ("up to 25 times lower") | Lambert et al. (2008) abstract: "approximately 25-fold increase in glacial dust flux"; Delmonte et al. (2008) abstract gives no factor; Delmonte et al. (2017) not readable | no finding; Lambert et al. (2008), already in the reference list, would be the more direct citation |
| PP-03 | P13 | p. 3, l. 77 to 87, summary of the EDML study | Vanderstraeten et al. (2023) abstract: "~68 %" Patagonian before 14.5 kyr BP, "dropped below 50 % on average", early Holocene "~50 % on average" | no finding for the introduction; the values used later disagree (GB-49) |
| PP-04 | P28 | Gap and priority claims at p. 1, l. 19; p. 3, l. 74; p. 7, l. 220; p. 12, l. 403; p. 14, l. 472; p. 3, l. 92 ("for which there is no consensus") | no search method stated anywhere; l. 92 is an assessment backed by three citations (Paleari et al., 2019; Coppo et al., 2022; Delmonte et al., 2007) | one finding (GB-02); no finding for l. 92 |
| PP-05 | P14 | Search for work that precedes or contradicts the contribution (continuous quantitative REE provenance of EDC across the LGIT, checked against Sr-Nd and EDML) | four queries by instance S1 (EDC quantitative provenance with REE; Aarons 2017 Taylor Glacier; Gili et al. 2016 lead isotopes; REE unmixing Talos Dome); candidates dropped because already cited: Revel-Rolland et al. (2006), Delmonte et al. (2020), Gili et al. (2022), Paleari et al. (2019), Gabrielli et al. (2010), Wegner et al. (2012); the publisher page, discussion page and later versions of this manuscript were not opened | two findings (GB-05, GB-39) |

### Segment 2: Materials and methods (p. 3 to 5)

#### Substantive findings

**GB-06 The stated temporal resolution contradicts Table S1 and its own source.**

| Field | Content |
|---|---|
| Check | P6, P36 |
| Location | p. 4, l. 110 to 111; Supplement Table S1 |
| Quotation | "with an average temporal resolution of approximately 100 years, ranging from 60 to 140" |
| Concern | In Table S1 the spacing between adjacent retained samples ranges from 0 to 2280 yr (median 98 yr); 77 of 240 intervals are below 60 yr and 60 are above 140 yr; the Holocene median is 43 yr and the LGM median 134 yr (Python). The data source gives a spacing of about 60 years in the Holocene and about 140 years in the last glacial (Gabrielli et al., 2010, p. 266), so 60 and 140 are period values, not the bounds of a range. Four ages occur twice (spacing 0, GB-18). The spacing difference also bears on the variability argument (GB-38). |
| Suggestion | Replace l. 110 to 111 by the period-specific spacing of the retained samples (Holocene and glacial medians and ranges). |
| Status | verified (Table S1 ages; Gabrielli et al. 2010 as read by instance SD); inferred (spacing statistics) |
| Severity | moderate |
| Source | SD |

**GB-07 Are the EDC samples, the period limits, the EDML record and the Potrok Aike record on one chronology?**

| Field | Content |
|---|---|
| Check | P35, P7 |
| Location | p. 4, l. 111; p. 6, l. 184 to 188; p. 13, l. 444 to 447; p. 11, l. 350 to 352 |
| Quotation | "The age model follows the EDC3 chronology (Parrenin et al., 2007)."; "7.5-2.8 kyr BP) (Veres et al., 2013)." |
| Concern | EDC ages are on EDC3, while the period limits are taken from Veres et al. (2013), which defines AICC2012; the chronologies of EDML and of the Potrok Aike record are not stated. The manuscript argues with synchronous changes between 15 and 14 kyr BP in both cores (l. 444 to 447) and with centennial matches to Potrok Aike (l. 350 to 352). Whether the timescales differ in these intervals cannot be judged from the manuscript. |
| Suggestion | Please state the chronology of each record in Section 2 and, if they differ, place EDC on AICC2012 or give the offsets for the intervals used in Sections 4.3 and 4.4. |
| Status | assumption (that the timescales differ materially is not shown in the manuscript; therefore a question) |
| Severity | moderate |
| Source | SD |

**GB-08 The Code/Data availability statement does not hold for the inputs and steps of the unmixing: measured REE data, correction factors, per-element uncertainties, normalisation, code and the six new source samples are not available.**

| Field | Content |
|---|---|
| Check | P12, P8, P35 |
| Location | p. 4, l. 118 to 124; p. 4, l. 107 to 109; p. 4, l. 135 to p. 5, l. 140; p. 5, l. 155 to 160; p. 16, l. 494 to 496; Supplement Table S2, rows EtoshaL1 to EtoshaL4, SuksesL, Sossusvlei (Suppl. page 17) |
| Quotation | "using element-specific factors (cfi) as described in Gabrielli et al. (2010) and Vanderstraeten et al. (2023)"; "All data needed to evaluate the conclusions in the paper are present" |
| Concern | The supplement carries the source database (Table S2), the end-member and ice-core isotope values (Tables S3, S4) and the per-sample medians (Table S1). The statement at l. 494 to 496 names no source, and it does not hold for: (1) the EDC REE concentrations of the 294 samples (l. 108), which are not in paper or supplement; instance S2 found no repository named in Gabrielli et al. (2010), and the EDC REE data sets on PANGAEA (doi:10.1594/PANGAEA.696111 and 696113) belong to an analytical intercomparison at other depths; (2) the element-specific correction factors cf_i and their uncertainties, which appear nowhere; the cited source reports only group recoveries of about 0.55 (LREE), 0.50 (MREE) and 0.40 (HREE) (Gabrielli et al., 2010, p. 267); (3) the per-element analytical uncertainties "between 2% and 10%" (l. 155 to 156); (4) the step from lsqnonneg coefficients, which carry no sum constraint, to "% of total deposition" (l. 160), which is not described; (5) the MATLAB version, random seed and code, although the heading reads "CODE/DATA"; (6) six Southern African patterns marked "this study" in Table S2, whose sampling, size separation, digestion and analysis are not described, while l. 105 describes the database as literature patterns; (7) the third-party series (nssCa flux, δ18O, deuterium excess, EDML per-sample contributions, Potrok Aike MDF), which are cited but not located. The second sentence offers data on request without a reason. Monte Carlo spreads, absolute fluxes and DS-level results are GB-13, GB-14 and GB-20. |
| Suggestion | Replace the statement at l. 494 to 496 by a source list giving for items 1 to 7 a repository with DOI, the supplement table that holds it, or the reason for withholding it; add the cf_i and per-element uncertainties as a supplement table; state in Section 2 how the contributions are normalised to 100 %; deposit the MATLAB code (DEPOT and Monte Carlo) with version and seed under a persistent identifier; describe the six new samples in Section 2 or cite their source. |
| Status | verified (absence of items 1 to 7 in paper and supplement; wording of the statement); inferred (no repository and no element-specific factors in Gabrielli et al. 2010, read by instances S2 and SD) |
| Severity | moderate |
| Source | S2, SD |

**GB-09 Table S2 holds 107 Australian and 4 Antarctic patterns instead of the stated 106 and 5, two Australian patterns appear twice under different basin names, and Figure S1 shows 5 Antarctic markers.**

| Field | Content |
|---|---|
| Check | P38, P3, P2 |
| Location | p. 4, l. 131 to 133; p. 4, l. 126; p. 5, l. 143; Supplement Table S2, rows Darling26 and Darling29 (Suppl. page 17), Murray24 and Murray29 (Suppl. page 18), block Antarctica (Suppl. page 19); Figure S1, panel ANT (Suppl. page 2); p. 11, l. 366 |
| Quotation | "Australia (AUS; 106 DS, predominantly from the central"; "Antarctica (ANT; 5" |
| Concern | The total of 217 holds either way (39 + 5 + 14 + 23 + 106 + 25 + 5 = 217; 39 + 5 + 14 + 23 + 107 + 25 + 4 = 217), so the totals do not reveal the shift. Counted in Table S2 (Python): AUS 107, ANT 4 (ELB, Expcove, Miers, Vict, confirmed on the page image). Figure S1, which refers to Table S2, shows 5 markers in the ANT panel. Darling26 and Murray29 ("Murray 15") carry the same coordinates (34°3'0.00"S, 142°3'10.80"E) and identical values in all 13 REE columns; Darling29 ("DR 3") and Murray24 ("Murray 10") likewise (34°28'48.00"S, 142°49'48.00"E). The database thus holds 215 distinct patterns, two of them twice; in Eq. 2 duplicate columns cannot be told apart, so how a fitted contribution is split between the two basin names is not determined by the data. This bears on the Darling sub-basin attribution at l. 366 (GB-20). Could the authors say whether the two patterns belong to the Darling or the Murray Basin, and which composition of the 217-column matrix was used? |
| Suggestion | Reconcile l. 131 to 133, Table S2 and the ANT panel of Figure S1 (write "AUS; 107 DS" and "ANT; 4 DS", or add the missing Antarctic row to Table S2); remove or justify the duplicate rows, correct l. 126 and l. 143 if the matrix changes, rerun the fit and report at l. 366 to 367 whether the Darling dominance holds. |
| Status | verified (row counts and duplicates by script and on the page images Suppl. pages 17 to 19; marker count on the page image); assumption (effect on the Darling attribution, asked as a question) |
| Severity | moderate |
| Source | S2, S3, AB |

**GB-10 The four Antarctic patterns in Table S2 show the zigzag of raw concentrations, contrary to the stated UCC normalisation; if they entered the model, the negligible Antarctic share follows from the input.**

| Field | Content |
|---|---|
| Check | P5, P27 |
| Location | p. 4, l. 133 to 135; Supplement Table S2, header (Suppl. page 16) and rows ELB, Expcove, Miers, Vict (Suppl. page 19); p. 10, l. 329 to 330; p. 10, l. 325 to 328 |
| Quotation | "all PSA REE patterns were normalized to the UCC composition of Rudnick and Gao (2003)"; "REE normalised on the Upper Continental Crust (Rudnick and Gao, 2003)"; "our results do not indicate significant Antarctic contributions to EDC" |
| Concern | The four ANT rows have Ce/Pr = 9.00, 9.01, 9.16 and 8.35, against a median of 0.96 and a maximum of 2.77 for the other 213 patterns (Python on Table S2; values confirmed on the page image). Instance SD found the odd-even zigzag removed when the ANT values are divided by crustal abundances (Ce/Pr 0.93 to 1.02). If these values entered the model, ANT shapes cannot match a smooth UCC-normalised ice-core pattern, so the absence of Antarctic dust (l. 330) and the contrast with the 24 % Antarctic component of Coppo et al. (2022) (l. 327 to 328) would follow from the input, not from the data, and the meteorological explanation at l. 330 to 334 would not be needed for the result. Table S1 nonetheless assigns 33.1 % ANT to the sample at 3654 yr, which a non-normalised column could also produce through scaling. |
| Suggestion | State whether the model used the ANT values printed in Table S2; if so, normalise them, rerun DEPOT and report the ANT contributions per period in Table S5 and in Section 4.3 (l. 329 to 334); in any case correct Table S2. |
| Status | verified (table values on the page image Suppl. page 19); inferred (non-normalisation, from the element ratios); assumption (use of these values in the model, asked as a question) |
| Severity | major |
| Source | SD |

**GB-11 "PSA" names both the seven source regions and the 217 individual source patterns, and "end-member" both the patterns and the regional averages.**

| Field | Content |
|---|---|
| Check | P38 |
| Location | p. 4, l. 136 to 137; p. 2, l. 44; p. 5, l. 144; p. 10, l. 329; Supplement Table S1 caption (Suppl. page 11), Table S2 title (Suppl. page 16), Table S3 header (Suppl. page 20) |
| Quotation | "the REE pattern of each EDC sample was modeled as a linear combination of PSA"; "Table S2: Table of PSAs database" |
| Concern | The text defines PSA as Potential Source Areas (l. 44) and uses PAT, CWA, PAP, SAF, AUS, NZ and ANT as the PSAs; the 217 individual patterns are "dust source sample, DS" (l. 144). The Table S1 caption counts "217 PSAs", the Table S2 title calls the DS collection a "PSAs database", l. 136 to 137 calls the 217 columns "PSA end-members", while Table S3 uses "PSA end-members" for seven regional averages. One word thus names two objects that the method keeps apart (CDS per DS, then aggregation by PSA, l. 161). |
| Suggestion | Use "DS" for the 217 patterns throughout: Table S2 title "Dust source (DS) database", l. 136 to 137 "a linear combination of the 217 DS patterns"; keep "PSA end-member" for the regional averages of Table S3 (the Table S1 caption is corrected in GB-18). |
| Status | verified (page images Suppl. pages 11, 16, 20; main text p. 4 and 5) |
| Severity | minor |
| Source | S2 |

**GB-12 No test shows that the unmixing recovers known mixtures, although 217 unevenly distributed candidate patterns are fitted to 13 values.**

| Field | Content |
|---|---|
| Check | P9, P32, P8 |
| Location | p. 5, l. 143 to 152; p. 4, l. 126 to 133; Supplement Table S2; p. 6, l. 180; p. 5, l. 172; p. 8, l. 259; p. 6, l. 196 to 197; p. 7, l. 212 to 215; p. 11, l. 366 to 367 |
| Quotation | "comprising “n” rows (one for each UCC-normalized REE) and 217 columns" |
| Concern | The system has 13 equations and 217 non-negative unknowns, so many combinations of similar patterns can fit equally well, and the Monte Carlo spreads that would show this are not reported (GB-13). The database is uneven: AUS 107 of 217 patterns (49.3 %), ANT 4 (1.8 %), CWA 5 (2.3 %); within AUS, 45 of 107 patterns are from the Darling Basin (42.1 %) (Python on Table S2). Whether a densely sampled region is selected more often because it covers more of the pattern space, not because it contributed more, is not tested. The manuscript calls its results "meaningful" (l. 180) and "robust" (l. 172, l. 259) without a recovery rate. Sub-regional attributions (Valdes Peninsula, Darling sub-basin, South Altiplano above 90 % in single samples) depend most on this. If Vanderstraeten et al. (2023) contains such tests, their outcome for 13 REE and 217 patterns is not stated. |
| Suggestion | Add a recovery test to Section 2: synthetic mixtures of known composition from held-out patterns, perturbed with period-specific analytical noise, unmixed with DEPOT, with the recovery error per PSA and sub-region; repeat the EDC unmixing with a database balanced by random subsampling to equal numbers per PSA and report the spread of the period means. |
| Status | verified (counts in Table S2; absence of a recovery test); assumption (selection bias toward densely sampled groups, asked as a question) |
| Severity | major |
| Source | SD |

**GB-13 The Monte Carlo propagation uses an input uncertainty far below the analytical uncertainty reported for Holocene samples, and its results are not reported.**

| Field | Content |
|---|---|
| Check | P31, P7, P8, P11 |
| Location | p. 5, l. 153 to 165; p. 6, l. 180 to 181; Supplement Table S1; Supplement Table S5; Fig. 1 (p. 24); p. 13, l. 420 to 424 |
| Quotation | "Analytical uncertainties associated with REE concentrations in EDC dust range between 2%"; "the PSA mixes calculated by the model were considered meaningful compared to the uncertainties" |
| Concern | The method draws 2000 runs per sample and builds a PDF per PSA, but only medians are reported: Table S1 lists medians, Fig. 1 has no uncertainty bands, Table S5 gives means without dispersion, and the check with 5000 runs ("does not significantly affect the results", l. 164) has no numbers. The 2 to 10 % at l. 155 to 156 correspond to replicate precision; the data source gives 25 to 35 % for MREE and HREE in Holocene samples and 5 to 8 % in glacial samples (Gabrielli et al., 2010, p. 266, as read by instance SD), so the Holocene MREE and HREE input uncertainty is underestimated by a factor between 2.5 (25 against 10 %) and 17.5 (35 against 2 %). The variability of cf_i used in the draws is not given. The claim at l. 180 to 181 is therefore not shown, and differences of a few points, such as HS1 differences "not exceeding ~5%" (l. 420 to 421) or ACR and YD differences (l. 421 to 422), cannot be judged. |
| Suggestion | Rerun the Monte Carlo with period-specific analytical uncertainties and the cf_i uncertainty stated in Section 2; add 16th and 84th percentiles per sample and PSA to Table S1, uncertainty bands to Fig. 1 and intervals for the period means to Table S5; give the 2000 against 5000 comparison as numbers at l. 162 to 164. |
| Status | verified (absence of spreads; wording); verified (analytical uncertainty in Gabrielli et al. 2010, read by instance SD); inferred (underestimation factor) |
| Severity | major |
| Source | S3, SD |

**GB-14 Absolute PSA dust fluxes are announced in the method and results sections but are shown in no figure or table.**

| Field | Content |
|---|---|
| Check | P12, P11, P3 |
| Location | p. 5, l. 166 to 167; p. 6, l. 183 to 184; Fig. 1 (p. 24); Supplement Figure S2, panel A (Suppl. page 4); Supplement Table S1 |
| Quotation | "to convert PSA contributions into absolute dust fluxes (Figure S2)."; "Figure 1 and Table S1 summarize the relative contributions (in % of total" |
| Concern | Fig. 1 shows percentages only (all five panels "Total Contribution (%)"), Table S1 gives percentage medians only, and Figure S2 shows the total nssCa2+ flux, δ18O and deuterium excess, but no flux per PSA. The derived quantity is therefore neither shown nor tabulated, and l. 494 to 496 do not mention it. Absolute fluxes would show whether the rise of the low-latitude shares after 14.5 kyr BP is an absolute increase or only a relative one against a falling Patagonian flux, which the Discussion addresses only in words (l. 463, "a relative increase"). The iron-fertilisation frame of the introduction depends on such fluxes (GB-55). |
| Suggestion | Add the PSA fluxes (µg m⁻² yr⁻¹) per sample or per period to Table S1 or Table S5 and a flux panel to Fig. 1 or Figure S2, and cite them at l. 167 and l. 183 to 184; otherwise delete the conversion sentence at l. 166 to 167 and "and flux" at l. 184. |
| Status | verified (page images p. 24, Suppl. pages 4 and 11 to 15) |
| Severity | moderate |
| Source | S2, S3, AB, SD |

**GB-15 The fit criterion R ≥ 0.67 does not correspond to the stated significance level, is not applied consistently, and removes samples only from the young part of the record.**

| Field | Content |
|---|---|
| Check | P1, P5, P9, P27 |
| Location | p. 5, l. 168 to 172; p. 6, l. 174 to 179; Supplement Table S1, rows 2888 and 3267 (Suppl. page 11) and first row 10511 (Suppl. page 13) |
| Quotation | "≥ 0.67 corresponds to a statistically significant match"; "These excluded samples are all younger than 14 kyr BP and" |
| Concern | (1) For a Pearson correlation the two-tailed critical value at p = 0.01 is r = 0.708 for 10 degrees of freedom and 0.684 for 11 (13 REE, n minus 2); r = 0.67 corresponds to p = 0.017 (df 10) or 0.012 (df 11) (scipy). R ≥ 0.67 thus meets p below 0.05, not p below 0.01; with r = 0.708, 16 retained samples with printed R from 0.67 to 0.70 would drop out in addition. (2) R is computed between the data and a model fitted with up to 13 non-zero coefficients chosen from 217 columns, so the classical test for independent variables does not apply and overstates significance. (3) Table S1 retains three samples with R = 0,66 (2888, 3267 and the first row 10511), below the threshold. (4) The 38 excluded samples are 22.8 % of the 167 samples younger than 14 kyr BP (129 retained plus 38) and 0 % of the 112 older ones; exclusion depends on the fit itself. If poorly fitted Holocene samples carry a source that the database does not represent well, the Holocene means would be biased toward represented sources; could the authors check this? The excluded samples are not listed (GB-18). |
| Suggestion | Correct the derivation at l. 170 to 172 (significance level and degrees of freedom actually met) or replace it by a criterion validated on synthetic mixtures (GB-12); apply it consistently to Table S1 or give R with three decimals; show in Section 3 how the Holocene means of Table S5 change for thresholds of 0.6, 0.7 and 0.8. |
| Status | inferred (critical values, p values and shares computed); verified (R values in Table S1 on the page images); assumption (direction of a bias, asked as a question) |
| Severity | moderate |
| Source | S3, SD |

**GB-16 Figure S1 is embedded at low resolution: most scale bars and place names are illegible, and the place names are in French.**

| Field | Content |
|---|---|
| Check | P29 |
| Location | Supplement Figure S1, panels NZ, AUS, SAF, Puna Alti, CWA (Suppl. page 2) |
| Quotation | "Localization of dust sources (DS) used in our DEPOT algorithm" |
| Concern | The map image is embedded at 800 × 450 px, about 78 ppi at print size. At 300 dpi the scale-bar labels of the NZ and AUS panels cannot be read; only "900 km" (PAT) and "80 km" (ANT) are legible. The Google Earth labels are French ("Argentine", "Nouvelle-Zélande", "TERRITOIRE DE LA CAPITALE AUSTRALIENNE") in an English manuscript. |
| Suggestion | Export Figure S1 at 300 ppi or more with English map labels and a legible scale bar in every panel. |
| Status | verified (page image; embedded image size) |
| Severity | minor |
| Source | AB |

**GB-17 Two Southern African samples are filed under the location "Etosha Pan" although their names and coordinates point elsewhere, and the six samples of "this study" have western instead of eastern longitudes.**

| Field | Content |
|---|---|
| Check | P38 |
| Location | Supplement Table S2, rows EtoshaL1 to EtoshaL4, SuksesL, Sossusvlei, columns "Location", "Lattitude", "Longitude" (Suppl. page 17); p. 12, l. 385 to 387; p. 12, l. 395 to 397 |
| Quotation | "Etosha Pan 24,76 S 15,29 W" |
| Concern | The sample "Sossusvlei" (24.76 S) and the sample "SuksesL" (21.059 S) are filed under "Etosha Pan", whose other rows lie at about 18.6 to 19.1 S; one object thus carries two place names. All six "this study" rows give longitudes with "W" (15,97 W to 16,836 W), whereas the Etosha rows of Li et al. (2020) give about 15°50' to 15°53' E. The Discussion compares the Etosha, Makgadikgadi and Namibian coast systems (l. 385 to 387, l. 395 to 397); which location column was used to group the Southern African sources? |
| Suggestion | Correct the "Location" entries of Sossusvlei and SuksesL and the hemisphere of the six longitudes in Table S2, and state at l. 385 to 387 how the Southern African patterns were grouped into systems. |
| Status | verified (table entries on the page image Suppl. page 17); assumption (effect on the system attribution, asked as a question) |
| Severity | minor |
| Source | S2 |

#### Minor corrections

| ID | Location | Quotation | Replacement | Source |
|---|---|---|---|---|
| KK-03 | p. 3, l. 101 | "to ice core camples" | "to ice core samples" | ZF |
| KK-04 | p. 4, l. 127 | "(Figure S1, and Table S1)" | "(Figure S1 and Table S2)" | S4 |
| KK-05 | p. 5, l. 159 | "by minimizing Eq. (1)" | "by minimizing Eq. (2)" | SD |
| KK-06 | Supplement Table S2, rows Omarur1inf5 and Omarur2inf5 (Suppl. page 17) | "Omarur1inf5", "Omarur2inf5" | "Omaruru1inf5", "Omaruru2inf5" | S2 |
| KK-07 | Supplement Table S2, rows aust8 to aust13, column Location (Suppl. page 18) | "Murrumbigdee basin" | "Murrumbidgee basin" | S2 |
| KK-08 | Supplement Table S2, block heading (Suppl. page 16) | "Puna AltiPlano (PAP)" | "Puna-Altiplano Plateau (PAP)" | S2 |
| KK-09 | Supplement Table S2, block heading (Suppl. page 19); Table S3, row NZ (Suppl. page 20) | "New-Zealand (NZ)" | "New Zealand (NZ)" | S2 |

#### Verification log

| ID | Check | Checked | Values | Result |
|---|---|---|---|---|
| PP-06 | P10, P9, P19, P7, P35, P17 | Design sketch from the whole manuscript and supplement (aims, data sources, timeline, environment, principles, disclosed limitations, chain from frame to result) | four aims (l. 91 to 98), no separate research questions or hypotheses; secondary use of the Gabrielli et al. (2010) data; 217 patterns, 211 from the literature and 6 "this study"; MATLAB lsqnonneg without version; chronology EDC3, period limits Veres et al. (2013); no outlook proposals | basis for GB-03, GB-07, GB-12, GB-13, GB-33, GB-55 |
| PP-07 | P26 | Non-negativity guarantee (l. 103 to 104, l. 138 to 139) over all reported values | minimum of all 1928 contribution cells of Table S1: 0.0 | no finding |
| PP-08 | P38, P1, P6 | Sample and database balance and fit statistics | 294 (l. 108, l. 114) minus 15 = 279 (l. 117, l. 174); 279 minus 38 = 241 (l. 179, l. 19); 241 / 279 = 86.4 % ("86%", l. 179); mean R of the 241 rows of Table S1 = 0.8523 ("0.852", l. 181); ages 2852 to 33699 yr; four samples in the gap 21.7 to 27.3 kyr BP (22150, 23104, 25384, 25640; l. 113) | no finding; Table S1 caption is GB-18, region counts GB-09 |
| PP-09 | P17 | Disclosure location of the sampling gap, the 15 incomplete patterns and the removal of Gd | p. 4, l. 113, l. 114 and l. 115 to 117, all in Section 2 where the data are introduced | no finding |
| PP-10 | P38 | Names of the method objects | "DEPOT" algorithm or model (l. 88, l. 100, l. 259, Table S1, Figure S1); DIC (l. 108 to 109, Eq. 2); CDS (l. 137, Eq. 2, l. 159); cf_i (l. 119, Eq. 1, l. 154); R (l. 168 to 174, Table S1); period names and limits (l. 184 to 188) equal the row labels of Tables S1 and S5 | no finding; spelling variants are KK-01, KK-15 and KK-21 |
| PP-11 | P5 | Pattern counts per PSA (l. 128 to 133) against Table S2; Gd column | PAT 39, CWA 5, PAP 14, SAF 23, NZ 25 match; AUS 107 against 106, ANT 4 against 5; total 217 matches l. 126; 13 REE columns without Gd, as l. 134 to 135 | no further finding beyond GB-09 and GB-10 |
| PP-12 | P38 | Sub-region names of PAP | South Puna (l. 212, l. 215, l. 355), S-Puna (Table S3), Spuna1 to 7 (Table S2), column "Puna" (Table S1); South or Southern Altiplano (l. 213, l. 290, l. 358), S-Altiplano, Salti1 to 5, column "Altiplano"; North Puna (l. 130, l. 356), Npuna1 to 2 | no finding |
| PP-13 | P38 | Two chronologies named in the manuscript | EDC3 (Parrenin et al., 2007) for sample ages, l. 111; Veres et al. (2013), AICC2012, for the period limits, l. 188 | no finding under P38 (two different objects); the question of a common timescale is GB-07 |
| PP-14 | P12 | Data sources of the method that the supplement does hold | Table S2: 217 rows, 13 REE columns; Table S1: 241 rows of ages, medians and R; Table S3: 7 end-member rows; Table S4: 35 measured rows; Table S5: period means for EDC and EDML; Figure S1: source locations; UCC composition: Rudnick and Gao (2003) | no finding for these sources; gaps are GB-08, GB-13, GB-14 |
| PP-15 | P33 | Statements on effort | only "computation cost" as the reason for 2000 runs (l. 162 to 163) | no finding; the missing numbers for the 5000-run check are part of GB-13 |
| PP-16 | P30 | Reported errors and corrections against the dates of runs | none reported in manuscript or supplement | no finding |
| PP-17 | P19 | Provenance class of the core statements | 211 of 217 patterns from the literature (97.2 %); ice-core REE data secondary; contributions model-generated and labelled so in the Table S1 caption; 3 of 35 measured isotope rows from Dome C (8.6 %) | no separate finding; see GB-08, GB-33, KK-32 |
| PP-18 | P25 | Availability of each input at the step that uses it (ice-core REE, cf_i, source patterns, isotope means, measured isotopes, nssCa flux) | all named sources exist; EDC Holocene isotopes not in Table S4; the reference at l. 159 points to Eq. 1 | no further finding beyond GB-08, GB-33 and KK-05 |
| PP-19 | P3 | Figure S1 marker counts against Table S2 | PAT 19 markers for 39 samples at 22 distinct coordinates; NZ 21 markers for 25 samples at 23 distinct coordinates; ANT 5 markers for 4 samples | PAT and NZ: no finding (shared or overlapping locations at map scale); ANT is GB-09 |

### Segment 3: Results (p. 6 to 7; Fig. 1, Fig. 3, Tables S1 and S5, Figures S3 and S4)

#### Substantive findings

**GB-18 Table S1 is captioned for 279 samples but lists the 241 retained ones, the 15 dropped and 38 excluded samples are listed nowhere, and samples are identified only by age, with four ages occurring twice.**

| Field | Content |
|---|---|
| Check | P12, P23, P38, P2 |
| Location | p. 6, l. 174 to 176; Supplement Table S1 caption (Suppl. page 11); Supplement Table S1, rows 3559 (Suppl. page 11), 10511 and 12841 (Suppl. page 13), 28709 (Suppl. page 14); p. 4, l. 114 to 117 |
| Quotation | "Table S1: Median of PSA's contribution (in percents) based on th DEPOT model results - using 217 PSAs and 279"; "These excluded samples are all younger than 14 kyr BP and have very low REE concentrations near the detection limit." |
| Concern | The balance in the text closes (PP-08), but Table S1 has 241 rows (2852 to 33699 yr), not 279. The 15 samples dropped for missing REE (l. 114) and the 38 samples below the threshold (l. 174) are not identified, so the statements that all 38 are younger than 14 kyr BP and near the detection limit cannot be checked, nor the effect of the exclusion on the periods younger than 14 kyr BP. Rows are keyed only by "Time [yr]", without depth or sample number linking them to the Gabrielli et al. (2010) data set, and four ages occur twice with different compositions (Python, confirmed on the page images): 3559 yr PAT 86.7 and 0.0; 10511 yr PAT 0.0 and 38.2; 12841 yr AUS 31.7 and 0.0; 28709 yr PAT 68.8 and 72.5. These pairs enter the period means and the moving average of Fig. 1 as independent samples. What distinguishes the two rows of each pair: two samples of one depth interval, replicates, or a transcription error? |
| Suggestion | Correct the caption of Table S1 to "Median PSA contributions (in percent) from the DEPOT model, using 217 dust sources (DS), for the 241 DIC samples retained (R ≥ 0.67) out of 279"; add depth or the original sample ID as key column; list all 279 fitted samples with median R and a flag for the 38 excluded ones (age, R, total REE concentration) and the 15 samples dropped for missing data; explain the duplicate ages in the caption or in Section 2. |
| Status | verified (row count and duplicates on the page images Suppl. pages 11 to 15); assumption (nature of the duplicates, asked as a question) |
| Severity | moderate |
| Source | S2, S3 |

**GB-19 Period means and box plots are reported without the number of samples, which ranges from 8 to 60, and the disclosed caveat for ACR and YD appears only in Section 4.4.**

| Field | Content |
|---|---|
| Check | P20, P22, P17, P36 |
| Location | p. 6, l. 183 to 188; p. 12, l. 407 to 409; Supplement Table S5 (Suppl. page 22); Fig. 3 caption (p. 27, l. 869 to 873); Supplement Figure S4 caption (Suppl. page 7); p. 6, l. 192 to 193; p. 6, l. 204 and l. 206 to 207; p. 7, l. 210 to 212; p. 7, l. 233 to 236 |
| Quotation | "It is important however to note that results for ACR and YD are tentative"; "due to the limited number samples covering those periods in EDC" |
| Concern | Counted from Table S1: Late Holocene 60, Early Holocene 56, YD 9, ACR 8, HS1 27, LGM 40, MIS3 41 samples (sum 241). Table S5 and the captions of Fig. 3 and Figure S4 give no numbers; only the ACR and YD counts appear, in Section 4.4 (with an error for the YD, GB-36). The manuscript discloses that ACR and YD results are tentative, which is not raised again here; the consequence is not drawn where these values are introduced: the Results give ACR and YD means without caveat (l. 192 to 193, l. 204, l. 206 to 207, l. 210 to 212), and Section 4.1 places "a major shift" at the onset of the ACR (l. 233) on 8 samples (GB-22). EDML sample numbers are missing for the Early Holocene, HS1 and LGM rows. |
| Suggestion | Add a column "n" to both parts of Table S5 and state n in the captions of Fig. 3 and Figure S4; move the caveat to Section 3, where ACR and YD means are first given, and to Section 4.1; at l. 408 write "due to the limited number of samples". |
| Status | verified (absence of n; text locations); inferred (counts from Table S1) |
| Severity | moderate |
| Source | S3, SD |

**GB-20 Sub-regional source attributions (Valdes Peninsula, Darling sub-basin, Southern African systems) have no reported numbers.**

| Field | Content |
|---|---|
| Check | P11, P15, P20, P6 |
| Location | p. 6, l. 196 to 197; p. 11, l. 366 to 367 and l. 371 to 372; p. 12, l. 385 to 387 and l. 392 to 397; p. 5, l. 161 to 162; Supplement Table S1; Supplement Figure S3 |
| Quotation | "Among the 39 DS from PAT, our algorithm highlights three specific REE patterns collected in"; "our model identifies the Darling sub-basin as the dominant"; "the Namibian coast and ephemeral riverbeds were detected most frequently, though their overall" |
| Concern | The method aggregates the PDFs "by PSA or specific sub-regions within PSA" (l. 161 to 162), but sub-regional results are reported only for Puna and Altiplano (Table S1) and as curves for Etosha, Namibia and Sua (Figure S3). No table or figure gives values for the Darling sub-basin, on which the argument at l. 371 to 372 builds (dry phase of the Darling Basin coinciding with the AUS peak), for the three Valdes Peninsula patterns, or for the detection frequency of the Southern African systems; "detected most frequently" has neither a count nor a base. Figure S3 is cited only for PAP (l. 355), not for the Southern African statements at l. 386 to 398, and it does not agree with Table S1 (GB-31). The Darling share may also reflect database density (45 of 107 Australian patterns, GB-12) and duplicate patterns (GB-09). |
| Suggestion | Add a supplementary table with the mean contribution and the detection count (samples with CDS above 0, out of n) per sub-region and period for PAT, AUS and SAF, or the DS-level contributions per sample, and cite it at l. 197, l. 366 and l. 386 to 398. |
| Status | verified (absence in Tables S1 and S5 and in Figure S3; text) |
| Severity | moderate |
| Source | S3, S4, SD |

**GB-21 The stated order of the secondary sources ranks PAP above NZ, while Tables S1 and S5 rank NZ above PAP.**

| Field | Content |
|---|---|
| Check | P2 |
| Location | p. 6, l. 201 to 202 |
| Quotation | "Overall, other Southern Hemisphere PSAs contribute to EDC dust deposition with sources from: AUS,"; "SAF, PAP and NZ, in decreasing order of importance." |
| Concern | Mean over all 241 samples of Table S1: AUS 16.51, SAF 9.17, NZ 7.85, PAP 6.85 %. Mean of the seven period means of Table S5: AUS 14.64, SAF 9.21, NZ 7.46, PAP 5.64 %. On both bases NZ ranks above PAP. |
| Suggestion | At l. 202 write "AUS, SAF, NZ and PAP" or state the basis on which PAP ranks above NZ. |
| Status | inferred (means computed from Tables S1 and S5) |
| Severity | minor |
| Source | S3 |

**GB-22 The provenance shift is dated to the onset of the ACR, but the Australian share does not rise there and the ACR composition lies within the glacial per-sample spread; the departure appears from the YD.**

| Field | Content |
|---|---|
| Check | P2, P15 |
| Location | p. 6, l. 202 to 204; p. 7, l. 225 to 226; p. 7, l. 233 to 236; p. 13, l. 445 to 447; p. 14, l. 477 to 480; Supplement Table S5; Supplement Table S1, rows 13032 to 14601 (Suppl. page 13); p. 12, l. 407 to 409 |
| Quotation | "Its average contributions rose after 14.7"; "Our calculations highlight a major shift in dust provenance occurred at the onset of the ACR"; "diverse mixture with significantly increased contributions from low-latitude sources, including AUS,"; "onward, a marked reorganization in dust provenance occurred" |
| Concern | Table S5: AUS is 11.3 % in HS1 and 11.1 % in the ACR (10.2 % in the LGM), so it does not rise at the ACR onset; the rise begins in the YD (14.5 %). The low-latitude total does rise (PAP + SAF + AUS: MIS3 20.6, LGM 20.1, HS1 18.2, ACR 24.3, YD 33.6, Holocene 44.8 %), carried by SAF (4.9 to 8.0) and PAP (2.0 to 5.2). The high-latitude share (PAT + NZ) is 79.4 (MIS3), 79.9 (LGM), 81.9 (HS1), 75.5 (ACR), 66.4 (YD) and 54.9 % (Holocene), and PAT in the ACR (68.9 %) exceeds the LGM value (65.7 %). Per sample (Table S1, Python), PAT + NZ is 79.9 ± 8.9 % in the LGM (n = 40), 81.9 ± 10.0 % in HS1 (n = 27) and 75.5 ± 12.6 % in the ACR (n = 8), so the ACR lies within one standard deviation of the glacial distributions. The smoothed curve of Figure S5 falls between 14.4 and 14.0 kyr BP (PP-48), but the per-sample PAT values from 13412 to 14601 yr are 67.6 to 81.7 % (mean 76.0 %), and the first values below 60 % appear at 13143 and 13032 yr (53.7, 41.9 %); with 8 ACR samples, a 9-step moving average mixes in YD values. "significantly" (l. 235) is not backed by a test. The manuscript discloses the ACR results as tentative (GB-19), but Section 4.1 and the Conclusion still date a "major" shift to the ACR onset, and the attribution to Meltwater Pulse 1A (l. 450 to 455) rests on the coincidence with ~14.5 kyr BP. Graded major: the timing underpins one of the main conclusions. |
| Suggestion | In Section 3 (l. 203 to 204), Section 4.1 (l. 233 to 236, writing "highlight that a major shift"), Section 4.4 (l. 445 to 447) and the Conclusion (l. 477 to 480) state that AUS rises from the YD onward, that the ACR rise of the low-latitude share is carried by SAF and PAP and lies within the glacial per-sample spread, or test the ACR distribution against LGM and HS1 (for example a rank test or bootstrap on Table S1) before dating the shift to ~14.5 kyr BP; remove "significantly" or give the test. |
| Status | verified (Tables S5 and S1, wording); inferred (sums and standard deviations computed from Tables S5 and S1) |
| Severity | major |
| Source | S3, S4 |

**GB-23 The Southern African minimum of "~2%" between 9.5 and 12 kyr BP matches neither the mean nor the median of Table S1, and no statistic is named.**

| Field | Content |
|---|---|
| Check | P2, P20 |
| Location | p. 6, l. 207 to p. 7, l. 208; Supplement Table S1, column SAF (Suppl. pages 12 and 13) |
| Quotation | "Although SAF input drops to minimal"; "levels (~2%) between 9.5 and 12 kyr BP" |
| Concern | For the 33 samples between 9.5 and 12 kyr BP (9772 to 11993 yr), SAF has a mean of 4.32 % and a median of 0.3 % (Python); two samples carry 40.3 % (10278 yr) and 49.2 % (first row 10511 yr). Instance AB measured a smoothed mean of 5.2 % (9.5 to 11.7 kyr) with a local maximum of 12.3 % and judged the wording loose but within the spread of the data; since no named statistic gives about 2 %, the statement is kept as a minor finding. |
| Suggestion | At l. 208 give the statistic and its value from Table S1 (for example "median 0.3 %, mean 4.3 %"). |
| Status | inferred (mean and median computed from Table S1) |
| Severity | minor |
| Source | S3 |

**GB-24 The South Altiplano peaks "over 90%" and the South Puna limit "below 20%" do not match Table S1, and the cited Fig. 1 does not show the sub-regions.**

| Field | Content |
|---|---|
| Check | P2, P3, P20 |
| Location | p. 7, l. 212 to 216; Fig. 1, panel PAP (p. 24); Supplement Figure S3, panels Puna and Altiplano (Suppl. page 6); Supplement Table S1, columns Puna and Altiplano |
| Quotation | "dominant in several samples, contributing over 90% at 11.2, 10, 8.6, 6, and 3.5 kyr BP. In contrast,"; "contributions of South Puna remained consistently below 20% during this interval (Figure 1)." |
| Concern | Separating PAP into its two sub-regions supports the later argument on paleolake Coipasa, and the positions of the five peaks are right. Their values are not: in Table S1 the Altiplano exceeds 90 % only at 8629 yr (100.0) and 11228 yr (97.0); at the other three ages the highest values are 75.7 (9957 yr), 58.5 and 58.0 (5967 and 6166 yr) and 62.7 % (3465 yr), with Puna 0.0 in all these samples; instance AB measured the raw tips in Fig. 1 consistently (95.8, 60.0, 97.9, 55.9 and 55.6 %, lower bounds). South Puna reaches 20 % or more in eight Holocene samples: 3503 (25.0), 4387 (20.6), 5657 (23.4), 5850 (29.1), 6775 (20.7), 7833 (25.6), 10205 (25.7) and 11117 yr (20.2 %). Fig. 1 has a single PAP panel; the split appears only in Figure S3, where the raw Puna curve also exceeds 20 % at eight Holocene ages and only the smoothed curve stays below 20 % (maximum 11.7 % at 11,449 yr, measured by AB). If "over 90%" meant the Altiplano share of PAP, 22 samples would qualify (all at 100 %), and the Puna statement could not hold. Figure S3 itself disagrees with Table S1 (GB-31). |
| Suggestion | At l. 213 to 215 state the basis (% of total deposition or of PAP, single samples or moving average), give the values from Table S1 (for example "over 90 % at 11.2 and 8.6 kyr BP and 58 to 76 % at 10, 6 and 3.5 kyr BP"), correct the Puna statement or restrict it to the moving average, and cite Figure S3 instead of Fig. 1. |
| Status | verified (Table S1 on the page images; Fig. 1 and Figure S3 measured by instance AB) |
| Severity | moderate |
| Source | S3, AB |

**GB-25 Antarctic dust is called negligible, which holds for the period means but not for one sample with 33.1 % ANT.**

| Field | Content |
|---|---|
| Check | P20 |
| Location | p. 7, l. 216 to 218; p. 10, l. 329 to 330; Supplement Table S1, row 3654 (Suppl. page 11), column ANT |
| Quotation | "only contributed negligibly (data not shown on Figure 1, see Table S1, Table" |
| Concern | Table S5 gives ANT means of 0.0 to 0.6 %, but Table S1 lists 33.1 % ANT at 3654 yr (and 1.7 % at 13412 yr). The statement refers to means without saying so, and the Discussion contrasts it with the 24 % Antarctic component of Coppo et al. (2022). Whether the ANT input patterns are usable at all is GB-10. |
| Suggestion | At l. 217 to 218 add "on average" and mention the single sample with 33 % ANT. |
| Status | verified (page image Suppl. page 11) |
| Severity | minor |
| Source | S3 |

**GB-26 Axis numbers and legends of Figures 1, 3 and 5 are below 6 pt at print size.**

| Field | Content |
|---|---|
| Check | P29 |
| Location | Fig. 1 (p. 24), all panels; Fig. 3 (p. 27), y axes; Fig. 5 (p. 29), both panels |
| Quotation | "Figure 1: Evolution of dust PSA contributions to EDC ice core" |
| Concern | Cap heights measured at 300 dpi (pt = px × 72 / 300 / 0.72): Fig. 1 axis numbers 5.0 to 5.7 pt, legend 5.0 pt, axis titles 5.7 pt; Fig. 3 axis numbers 5.3 pt; Fig. 5 axis numbers 4.3 to 4.7 pt, legend 4.7 pt. All are below 6 pt, the smallest by more than the measurement tolerance of 0.6 pt; Fig. 4 measures 6.3 to 6.7 pt and the supplementary figures 6.0 to 13 pt. |
| Suggestion | Enlarge axis numbers, axis titles and legends in Figures 1, 3 and 5 to at least 7 pt at final size. |
| Status | verified (measured by instance AB) |
| Severity | minor |
| Source | AB |

**GB-27 The abbreviations used inside the figures are not resolved in the captions.**

| Field | Content |
|---|---|
| Check | P29 |
| Location | Figures 1 to 5, captions p. 25, l. 851 to 854; p. 26, l. 857 to 866; p. 27, l. 869 to 873; p. 28, l. 875 to 876; p. 29, l. 880 to 882; Supplement Figures S3 to S5 |
| Quotation | "Western-Argentina and Antarctica are not shown as their dust emissions contribution are very low." |
| Concern | The figures are labelled with PAT, AUS, SAF, NZ, PAP, YD, ACR, HS1, LGM, MIS3, "Holo", EDC, EDML and PSA, Fig. 2 also with "Iso". No caption expands them; the caption of Fig. 1 names only Central-Western-Argentina and Antarctica, the two regions that are not shown. A reader who opens the figure pages at the end of the preprint must look the labels up in the text. |
| Suggestion | Add one sentence to the caption of Fig. 1 that expands the PSA and period abbreviations, refer to it from the captions of Figures 2 to 5 and S3 to S5, and expand "Holo" and "Iso" in Figures 4 and 2. |
| Status | verified (labels on the page images; caption text) |
| Severity | minor |
| Source | AB |

**GB-28 The "Holocene" panel of Fig. 3 shows the Early Holocene, and the "Early Holocene" panel of Figure S4 shows the Late Holocene.**

| Field | Content |
|---|---|
| Check | P3 |
| Location | Fig. 3, left panel "Holocene" (p. 27), caption p. 27, l. 869; Supplement Figure S4, panel "Early Holocene" (Suppl. page 8); Supplement Table S1; Supplement Table S5 |
| Quotation | "Figure 3: Box plots of provenance contributions (in %) of Holocene, and Last Glacial Maximum (LGM)" |
| Concern | Measured box lines of the Fig. 3 "Holocene" panel (Q1, median, Q3): PAT 12.3, 55.2, 72.9; AUS 2.9, 18.1, 34.2; SAF 0.1, 2.2, 11.4; mean crosses PAT 47.2, AUS 24.9, SAF 9.9. Table S1 for the Early Holocene (7.5 to 11.7 kyr, n = 56) gives PAT 12.3, 55.2, 73.0, AUS 2.8, 18.1, 34.2, SAF 0.0, 2.1, 11.3 and means 47.1, 24.9, 9.8 (match); the full Holocene (n = 116) gives PAT 18.4, 58.6, 73.8 and means 49.0, 23.1, 10.7 (no match). The Figure S4 "Early Holocene" panel (PAT 18.9, 61.7, 80.6; AUS 2.6, 14.6, 29.7) matches the Late Holocene of Table S1 (n = 60: 18.9, 61.7, 80.7; 2.7, 14.6, 29.8), not the Early Holocene. The full Holocene, whose means the text uses (Table S5, l. 216, l. 317 to 319), appears in no box plot. |
| Suggestion | Relabel the left panel of Fig. 3 "Early Holocene (7.5 to 11.7 kyr BP)" and the first panel of Figure S4 "Late Holocene (2.8 to 7.5 kyr BP)", or recompute the Fig. 3 panel for the full Holocene, and adapt both captions. |
| Status | verified (measured by instance AB; statistics computed from Table S1) |
| Severity | moderate |
| Source | AB |

**GB-29 The captions of Fig. 3 and Figure S4 call the whisker ends extremes, but values are plotted beyond them.**

| Field | Content |
|---|---|
| Check | P29 |
| Location | Fig. 3 caption, p. 27, l. 872; Supplement Figure S4 caption (Suppl. page 7); Fig. 3, left panel, AUS and PAP |
| Quotation | "the whiskers indicate the lower and upper extremes" |
| Concern | In the left panel of Fig. 3 the upper AUS whisker ends at 79.7 % (measured), while Table S1 gives Early Holocene AUS values of 84.3, 95.3 and 98.1 % beyond it, drawn as dots; the whisker equals the largest value within Q3 + 1.5 × IQR (fence 81.2, largest value below it 79.8). The PAP whisker ends at 28.0 % with values of 39.6, 75.7, 97.0 and 100.0 % beyond it. The whiskers thus follow the 1.5 × IQR rule, and the dots, which are individual samples, are not explained in either caption. |
| Suggestion | At l. 872 and in the caption of Figure S4 write "the whiskers extend to the most extreme values within 1.5 times the interquartile range; dots are individual samples". |
| Status | verified (measured by instance AB; values in Table S1) |
| Severity | minor |
| Source | AB |

**GB-30 One row of Table S1 sums to 93.5 %, while all other rows sum to 100 %.**

| Field | Content |
|---|---|
| Check | P23 |
| Location | Supplement Table S1, first row 10511 (Suppl. page 13) |
| Quotation | "10511 0,0 0,0 3,1 6,7 49,2 29,5 5,0 0,0 0,66" |
| Concern | 0.0 + 0.0 + 3.1 + 6.7 + 49.2 + 29.5 + 5.0 + 0.0 = 93.5; the other 240 rows sum to 99.9 to 100.1 (Python). The page image shows this row first of the two rows dated 10511 yr (instance SD had named the second row; the decision follows the page image). Either one value is mistyped, or the medians of the separate PSA PDFs were not renormalised for this sample, in which case the method (l. 164 to 165, "median of each PSA-specific PDF") should say whether the other rows were renormalised (GB-08, item 4). The same row has R = 0,66 (GB-15). |
| Suggestion | Check and correct the first row 10511 of Table S1 and state in Section 2 whether the PSA medians are renormalised to 100 %. |
| Status | verified (page image Suppl. page 13); inferred (sums) |
| Severity | minor |
| Source | S3 |

**GB-31 Figure S3 cannot be reconciled with Table S1 and Fig. 1: sub-regional values exceed the PSA totals, and the largest Altiplano samples are missing.**

| Field | Content |
|---|---|
| Check | P3 |
| Location | Supplement Figure S3, all panels (Suppl. page 6); Supplement Table S1; Fig. 1, panels SAF and PAP (p. 24); p. 11, l. 355 to 358; p. 12, l. 395 to 396 |
| Quotation | "Evolution of contribution to EDC from subregions of the Puna-Altiplano and Southern Africa PSA between 2.852" |
| Concern | Raw peaks measured by instance AB (calibrated axes, ±16 yr) against Table S1 and Fig. 1: (1) at about 11.86 kyr the panels show Etosha 88.5 %, Puna 54.9 % and Altiplano 38.8 %, together 182 % for one age, while Table S1 has no sample between 11779 and 11993 yr and Fig. 1 shows at most 7.7 % PAP and 13.6 % SAF there; the SAF spike of Table S1 (94.7 % at 12227 yr) thus appears 360 yr younger. (2) Sua exceeds the total SAF of the same sample: 25.7 % at 12,868 yr (Table S1 SAF 7.8 at 12867), 28.3 % at 19,368 yr (SAF 0.0 at 19365), 34.4 % at 28,710 yr (SAF 0.8 and 1.7 at 28709). (3) The Altiplano panel does not show the samples that Table S1 and Fig. 1 give as Altiplano-dominated: 5.2 % at 8629 yr (Table S1 100.0), 14.6 % at 11228 yr (97.0), 1.0 % at 9957 yr (75.7), 9.9 % at 3465 yr (62.7). Other peaks agree (Puna 29.8 % at 5,852 yr against 29.1 at 5850). Figure S3 thus appears to come from a different data set or time vector, and the sub-regional statements that cite it (l. 355 to 358; Etosha from "~12.2" kyr BP at l. 396) cannot be checked against it. Could the authors say whether Figure S3 was produced from a different run or from the 279-sample set before the R filter? |
| Suggestion | Regenerate Figure S3 from the same model output and time vector as Table S1 and Fig. 1, add the Southern African sub-region columns (Etosha, Namibia, Sua) to Table S1, and recheck l. 355 to 360 and l. 392 to 398 against the corrected figure. |
| Status | verified (values measured by instance AB and compared with Table S1); assumption (cause, asked as a question) |
| Severity | major |
| Source | AB |

**GB-32 Panels 2 to 5 of Figure S4 have no y axis of their own and are drawn on a scale about 1.4 % taller than the axis of panel 1.**

| Field | Content |
|---|---|
| Check | P29 |
| Location | Supplement Figure S4, panels YD, ACR, HS1, MIS3 (Suppl. page 8) |
| Quotation | "Box plots of provenance contributions of (1) Early Holocene, (2) Younger Dryas (YD)," |
| Concern | Only the first panel has a y axis. Read against it, the PAT boxes of the other panels lie above the Table S1 statistics by a constant factor: HS1 68.0, 76.0, 80.5 measured against 67.0, 75.0, 79.4 (ratios 1.015, 1.013, 1.014); MIS3 63.4, 71.5, 78.4 against 62.5, 70.5, 77.2. Divided by 1.014, all values agree within 0.3 points. A reader using the only axis reads values about one point too high near 75 %. |
| Suggestion | Draw all five panels on one plotting area with a common y scale, or give each panel its own y axis. |
| Status | verified (measured by instance AB; ratios computed) |
| Severity | minor |
| Source | AB |

#### Minor corrections

| ID | Location | Quotation | Replacement | Source |
|---|---|---|---|---|
| KK-10 | p. 6, l. 189 | "It contributes for 65-70%" | "It contributes 65 to 70%" | S3 |
| KK-11 | p. 6, l. 191 | "during HSI is marked" | "during HS1 is marked" | S2, S3 |
| KK-12 | p. 6, l. 193 | "(averages contributions)" | "(average contributions)" | S3 |
| KK-13 | p. 6, l. 195 | "contributing to 47-51% of the total mix" | "contributing 47 to 51% of the total mix" | S3 |
| KK-14 | p. 6, l. 197 to 198 | "and therefore reflects regional mixed input" | "and therefore reflect regional mixed input" | S3 |
| KK-15 | p. 6, l. 199 | "LREE (low rare earth elements)" | "LREE (light rare earth elements)" | ZF |
| KK-16 | Fig. 1 caption, p. 25, l. 851 | "between 2852 to 33699 yr BP" | "between 2852 and 33699 yr BP" | AB |
| KK-17 | Fig. 1 caption, p. 25, l. 852; Fig. 5 caption, p. 29, l. 882; Supplement Figure S5 caption (Suppl. page 9) | "mobile average over 9 steps" | "moving average over 9 samples" | S4, AB |
| KK-18 | Fig. 1 legend, PAP panel (p. 24) | "Raw data" | "Sample medians (DEPOT)" | SD |
| KK-19 | Fig. 3 caption, p. 27, l. 873 | "for HS1, ACR and YD are illustrated in Figure S4." | "for YD, ACR, HS1 and MIS3 are shown in Figure S4." | AB |
| KK-20 | Supplement Figure S4 caption (Suppl. page 7) | "Antarctica Cold Reveal (ACR), (4) Heindrich Stadial 1 (HS1), and (5) Marine Isotope 3 (MIS3)" | "Antarctic Cold Reversal (ACR), (4) Heinrich Stadial 1 (HS1), and (5) Marine Isotope Stage 3 (MIS3)" | S2, S3, AB |

#### Verification log

| ID | Check | Checked | Values | Result |
|---|---|---|---|---|
| PP-20 | P2, P37, P5 | Table S5 (EDC) recomputed as means of Table S1 rows per period, limits of l. 185 to 188 (PAP = Puna + Altiplano) | n: LH 60, EH 56, Holocene 116, YD 9, ACR 8, HS1 27, LGM 40, MIS3 41 (sum 241); means PAT, PAP, SAF, AUS, NZ, ANT: LH 50.70, 11.99, 11.62, 21.39, 3.77, 0.55; EH 47.09, 10.03, 9.81, 24.85, 8.10, 0.00; Holocene 48.96, 11.04, 10.74, 23.06, 5.86, 0.29; YD 63.06, 4.52, 14.63, 14.50, 3.28, 0.00; ACR 68.94, 5.23, 7.97, 11.07, 6.58, 0.21; HS1 74.76, 1.98, 4.86, 11.27, 7.13, 0.00; LGM 65.72, 3.58, 6.33, 10.19, 14.17, 0.00; MIS3 70.34, 2.19, 9.34, 9.09, 9.06, 0.00 | no finding: all EDC entries of Table S5 reproduced to 0.1 |
| PP-21 | P2, P36 | Values of the Abstract and Results against Table S5 (EDC) | Abstract PAT ~65 to 75 % (70.3, 65.7, 74.8) and ~49 % (49.0); l. 189 to 191 65 to 70 % and 75 %; l. 192 69 and 63 % (68.9, 63.1); l. 195 47 to 51 % (47.1, 50.7); l. 203 to 204 AUS 9, 10, 11, 15, 23 (9.1, 10.2, 11.3, 14.5, 23.1); l. 206 to 208 SAF ~5 to 9 (9.3, 6.3, 4.9, 8.0), 15 (14.6), ~11 (10.7); l. 209 to 210 NZ 14, 7, 6.5, 3, 6 (14.2, 7.1, 6.6, 3.3, 5.9); l. 211 to 212 PAP below 4 and ~5 (2.2, 3.6, 2.0; 5.2, 4.5); l. 216 PAP 11 (11.0) | no finding for these values; deviations are GB-21, GB-22, GB-23, GB-24 |
| PP-22 | P23 | Row sums of Tables S5 and S1 | Table S5 EDC rows 99.9 to 100.1, EDML rows 99.9 to 100.0; Table S1: 240 of 241 rows between 99.9 and 100.1 | no finding except the first row 10511 (GB-30) |
| PP-23 | P11 | Periods against reported outputs | Table S5 EDC for all eight periods; EDML only for the overlap 7.5 to 27 kyr BP (disclosed, l. 406 to 407); box plots for LGM (Fig. 3) and five further panels (Fig. 3, Figure S4); R per sample (Table S1); modelled isotope values per sample (Fig. 2) | no finding beyond GB-13, GB-14, GB-20 and GB-28 |
| PP-24 | P21 | Comparisons of contributions across periods and cores | all comparisons use percentages of total deposition, normalised within each sample; the small ACR and YD samples are disclosed (l. 407 to 409) | no finding beyond GB-19, GB-38 and GB-50 |
| PP-25 | P22 | Quantities the reader must compute | sample numbers per period (only by counting Table S1), SSA totals (PAT + CWA + PAP, not in Table S5), PAP sub-region split (Table S1 only), high- and low-latitude totals | sample numbers are GB-19; SSA and latitude totals are stated in the text, no separate finding |
| PP-26 | P29, P3 | Inventory of figures with page, type, caption and citations | Fig. 1 image p. 24, caption l. 851 to 854, cited l. 183, 205, 215, 217, 221, 307, 338; Fig. 2 p. 26, cited l. 244, 252, 257; Fig. 3 p. 27, cited l. 281, 294 to 295; Fig. 4 p. 28, cited l. 405, 419; Fig. 5 p. 29, cited l. 340; Figures S1 to S5 cited at l. 127, 167, 355, 382, 405; no graphical abstract | no finding beyond GB-42 (order of Fig. 4 and 5) |
| PP-27 | P24 | Period shading against the limits of l. 185 to 188 | Fig. 1: 11,720, 12,900, 14,700, 17,990, 29,020 yr (±24); Figure S2: 11,720, 12,890, 14,720, 18,000, 28,980 yr (±16); Fig. 5: 11,740, 12,980, 14,760, 17,980, 29,030 yr (±23); Figure S5: YD 11,570 to 12,870 yr, HS1 14,680 to 17,890 yr | no finding |
| PP-28 | P3 | Fig. 1 raw curves and moving average against Table S1 | raw peaks of 50 % or more found at the Table S1 ages within ±60 yr: AUS 15 of 15, SAF 7 of 7, NZ 3 of 3, PAP 7 of 7; tips up to 10 points low (once 16) because the thin line fades; centred 9-point moving average of Table S1 against the bold line: median difference SAF minus 0.21, AUS minus 0.31, NZ minus 0.17, PAT minus 1.48 points | no finding |
| PP-29 | P3, P24 | Dated statements on Fig. 1 at l. 194, l. 204 to 205, l. 336 to 338, l. 350 to 352 | smoothed PAT minima 10,131 yr (23.5 %), 8,539 yr (30.9 %), 6,329 yr (28.5 %) against 10, 8.6, 6.3 kyr; maxima 9,276 to 9,727 yr and 7,588 to 7,707 yr against "~9" and "7-8" kyr; smoothed PAT 3 to 5 kyr mean 53.0 % against 50 to 55 %; smoothed AUS maxima 10,167 and 6,277 yr against 9.5 to 10 and 6.3 kyr | no finding; the SAF statement at l. 207 to 208 is GB-23 |
| PP-30 | P3 | Fig. 3 LGM panel against Table S1 (n = 40) and l. 281, 289, 294 | measured Q1, median, Q3: PAT 58.9, 65.8, 71.6; AUS 5.8, 10.2, 14.0; NZ 10.9, 15.5, 18.9; Table S1: PAT 58.9, 65.8, 71.7; AUS 5.8, 10.2, 14.0; NZ 10.8, 15.5, 18.9; SSA 69.3 % (text ~70 %), AUS 10.2 % (~10 %), PAP 3.6 % (~4 %) | no finding |
| PP-31 | P29 | Font sizes of the remaining figures at print size | Fig. 2 axis numbers 7.3 pt, legend 5.7 pt (within the 0.6 pt tolerance), domain labels 7.3 pt; Fig. 3 x labels 6.0 pt, panel titles 7.0 pt; Fig. 4 6.3 to 6.7 pt; Figures S2 to S5 axis numbers 8.3 to 13.0 pt | no finding for these figures; Figures 1, 3 (y axes) and 5 are GB-26 |
| PP-32 | P3 | Figure S4 panels YD, ACR, HS1, MIS3 against Table S1 after the scale factor of GB-32 | after division by 1.014: YD PAT 47.3, 70.4, 85.1 against 47.1, 70.2, 84.8; HS1 AUS 5.7, 10.3, 14.8 against 5.7, 10.3, 14.8; MIS3 SAF 4.7, 8.5, 13.3 against 4.6, 8.3, 13.2; YD panel shows 9 PAT values | no finding beyond GB-32 |
| PP-33 | P2 | Merge: quotations and embedded values of all findings re-checked against the extracted text and the page images; Table S1 recomputed from the supplement text | 241 rows, 4 duplicate ages, one row sum 93.5 %, three rows with R = 0,66, Altiplano above 90 % in two samples, Altiplano onset 12841 yr, ANT above 0 in two samples, Table S2 counts AUS 107 and ANT 4 with two duplicate patterns | corrections made in the merge: Aarons et al. (2017) rows in Table S4 counted as 18 (not 22); sum row 10511 is the first row (page image); the statement that Altiplano values between 12841 and 11228 yr are non-zero at 11117 and 10708 yr was dropped (both ages are younger); the LGM sums ~79 % and ~21 % (l. 294) differ from 79.9 and 20.1 by less than one point and are not raised |

### Segment 4: Discussion, conclusion, declarations, references (p. 7 to 22; Fig. 2, 4, 5; Tables S3, S4; Figures S2, S5)

#### Substantive findings

**GB-33 The agreement with isotopic compositions "measured in EDC for both glacial and interglacial intervals" is not shown: the measured Holocene values come from other sites, and the per-sample values plotted in Fig. 2 do not agree with the EDC Holocene range.**

| Field | Content |
|---|---|
| Check | P15, P3, P31, P18, P10 |
| Location | p. 8, l. 254 to 259; p. 8, l. 244 to 246; p. 7, l. 228; p. 7, l. 238 to 240; p. 3, l. 93 to 94; Fig. 2 and caption (p. 26, l. 857 to 866); Supplement Table S3 (Suppl. page 20); Supplement Table S4 (Suppl. page 21) |
| Quotation | "Overall, the close agreement between our modeled isotopic compositions and those measured in EDC"; "for both glacial and interglacial intervals supports the robustness of our DEPOT algorithm"; "For each time interval of the LGIT, the" |
| Concern | Plotting all measured values is useful: each of the 35 rows of Table S4 coincides with an open symbol in Fig. 2 (overlay by instance AB). But Table S4 contains EDC values only for the LGM (two rows, "Delmonte et al., 2004a") and one "Old Dome C" value for HS1; all 22 Holocene rows come from Taylor Glacier (8, Aarons et al., 2017) and Berkner Island (14, Bory et al., 2010), and Berkner Island lies in the Weddell Sea sector, not among the "other East Antarctic ice cores" announced at l. 228. The EDC Holocene values quoted at l. 239 to 240 (87Sr/86Sr ~0.710, ε(Nd) -4.51 to -5.68) carry no citation and appear neither in Table S4 nor in Fig. 2. Fig. 2 plots one value per sample (sample 12227 recomputed with Eq. 3 and 4 and Table S3: 0.72745 and -17.87; measured position 0.72745 and -17.89), while l. 244 describes the calculation "For each time interval". Recomputed per sample (Python, contributions renormalised without ANT, which has no end-member in Table S3), the 116 Holocene samples span ε(Nd) -16.52 to 2.20 (median -2.44), and only 8 fall within -5.68 to -4.51; from period-mean contributions the Holocene gives 0.7101 and -4.99, inside the EDC range, and the LGM 0.7083 and -2.62, slightly outside -1.66 to -2.46. Agreement thus holds for period means, which the manuscript does not show, not for the plotted per-sample values. It is asserted from overlapping point clouds without a metric, and with one mean value per PSA (Table S3) every modelled mixture lies inside the hull of the end-members by construction, so overlap has little discriminating power, which the manuscript names itself: "the difficulty to discern multiple source contributions, especially when the isotopic fields overlap" (l. 64 to 65). Instance S4 graded moderate because the period-mean check succeeds; instances AB and SD graded major; merged as major because the Holocene validation of aim 2 against EDC is not shown. |
| Suggestion | Compare modelled and measured Sr-Nd at the ages of the measured EDC samples (Delmonte et al., 2004, glacial and Holocene) with Monte Carlo uncertainty of the modelled values and a residual measure; add a null comparison (for example a constant glacial mixture applied to the Holocene) to show that the test can fail; add the EDC Holocene values with their source to Table S4 and Fig. 2, mark Taylor Glacier and Berkner Island separately, write "For each sample" at l. 244 or plot period means, and revise l. 228 and l. 258 to 260 accordingly. |
| Status | verified (Table S4 on the page image Suppl. page 21; Fig. 2 positions measured by instance AB; wording); inferred (recomputation with Eq. 3 and 4; weak discrimination) |
| Severity | major |
| Source | S4, AB, SD |

**GB-34 The timing of the Patagonian Ice Sheet maximum differs from the cited source, and the dimensions given refer to 35 ka.**

| Field | Content |
|---|---|
| Check | P13 |
| Location | p. 8, l. 267 to 269 |
| Quotation | "between ~34 and 29.4 kyr BP, covering much of the Andes with an ice mass 2090 km long and 350 km" |
| Concern | The abstract of Davies et al. (2020, Earth-Science Reviews 204, 103152) dates the maximum extent to 33 to 28 ka between 38° S and 48° S "and earlier, around 47 ka from 48°S southwards", and gives the dimensions for 35 ka ("At 35 ka ... was 350 km wide and 2090 km long"). The interval 34 to 29.4 kyr BP is not in the abstract, the earlier maximum south of 48° S is left out, and the dimensions are attached to another time. The effect on the argument is small. |
| Suggestion | At l. 267 to 269 give the timing as in Davies et al. (2020), including the earlier maximum south of 48° S, and state that the dimensions refer to 35 ka; if 34 to 29.4 ka comes from a specific section or figure, cite it. |
| Status | verified (abstract, read by instance S1); inferred (that the full text contains no interval 34 to 29.4 ka) |
| Severity | minor |
| Source | S1 |

**GB-35 The model estimate "70-90%" for southern South American and Australian dust is not in the cited model studies, and one of them points to Australian, not Patagonian, dominance.**

| Field | Content |
|---|---|
| Check | P13 |
| Location | p. 8, l. 275; p. 9, l. 276 to 277 |
| Quotation | "Model simulations also support this view, estimating that SSA and AUS" |
| Concern | Krätschmer et al. (2022, Climate of the Past 18, 67 to 87) state in the abstract that "over 90 % of the mineral dust deposited over Antarctica are of Australian or South American origin during both PI and LGM"; in the discussion preprint (cp-2021-73), Table 4 attributes LGM deposition over Antarctica to Australia 68 %, South America 24 % and South Africa 7 %. Albani et al. (2012, Climate of the Past 8, 741 to 750) give no source percentages and describe Australia as "a possible contribution of Australia as a secondary, but significant dust source". The sentence thus gives a range below the cited value (more than 90 %) and presents as support for Patagonian predominance a simulation in which Australia supplies most of the Antarctic deposition. If the range comes from another study, which one? The internal sum in the same sentence is GB-36. |
| Suggestion | At l. 275 to 277 quote Krätschmer et al. (2022) as "over 90 %" for Australia and South America over all of Antarctica, state the model's split, replace "also support this view" by a sentence that discusses the disagreement with the present 10 % AUS share at the LGM, and remove Albani et al. (2012) as a source of the percentage. |
| Status | verified (abstract of Krätschmer et al. 2022 and full text of Albani et al. 2012, read by instance S1); inferred (Table 4 split, read in the discussion preprint) |
| Severity | moderate |
| Source | S1 |

**GB-36 Several values in the Discussion deviate from Tables S5 and S1: the LGM New Zealand share, the HS1 high-latitude total, the LGM PAT + AUS sum, the Holocene SSA share and the number of YD samples.**

| Field | Content |
|---|---|
| Check | P1, P2, P15, P3 |
| Location | p. 9, l. 276; p. 9, l. 282; p. 9, l. 295; p. 10, l. 321 and l. 326; p. 12, l. 408; p. 7, l. 209; Supplement Table S5; Supplement Table S1, block YD (Suppl. page 13); Supplement Figure S4, panel YD |
| Quotation | "(here, PAT+AUS is ~77%)"; "average NZ contribution (~11%), making it the second-largest dust source to EDC during the LGM."; "with high-latitude sources totaling 84 %"; "compared to 61% in our record when combining PAT, CWA, and PAP"; "(8 and 7 samples in ACR and YD," |
| Concern | (1) NZ in the LGM is 14.2 % in Table S5 and "14%" at l. 209; the LGM mean of Table S1 is 14.17 % and the median 15.5 %; MIS3 and LGM together give 11.6 % (Python). No LGM statistic gives ~11 %, and the ~79 % for PAT + NZ at l. 293 to 294 itself implies 14.2 %. The value matters because it is the argument against Koffman et al. (2021) in the next sentence. (2) HS1: PAT + NZ = 74.8 + 7.1 = 81.9 %, not 84 %; the sum of the medians gives 81.0 %. (3) LGM: PAT + AUS = 65.7 + 10.2 = 75.9 %, not ~77 %; MIS3 and LGM together give 77.7 %; the model estimate cited in the same sentence concerns SSA and AUS, which is 69.3 + 10.2 = 79.5 %. (4) Holocene SSA = 49.0 + 0.0 + 11.0 = 60.0 %; l. 321 gives 61 %, l. 326 gives 60 %. (5) Table S1 has 9 YD rows (11779 to 12867 yr, 8 distinct ages); their mean reproduces the YD row of Table S5 (PAT 63.06, SAF 14.63, AUS 14.50 %), and the YD panel of Figure S4 shows 9 values; the ACR count of 8 is confirmed. The qualitative statements stand (NZ remains second in the LGM either way). |
| Suggestion | Replace the values at l. 276, 282, 295, 321 and 408 by those of Tables S5 and S1 (14 %, 82 %, 76 %, 60 %, 9 samples) or state how they were derived, and compare the model estimate at l. 275 to 276 with SSA + AUS. |
| Status | verified (text, Table S5, Table S1 count on the page image Suppl. page 13); inferred (sums and alternative statistics computed) |
| Severity | moderate |
| Source | S3, S4, AB |

**GB-37 Does Neff and Bertler (2015) give 14 to 32 % for New Zealand dust in inland East Antarctic deposition, given that their abstract calls the source contributions to interior East Antarctica "limited and highly mixed"?**

| Field | Content |
|---|---|
| Check | P13 |
| Location | p. 9, l. 286 to 288 |
| Quotation | "Present-day forward air-mass"; "to inland Antarctic deposition (Neff and Bertler," |
| Concern | The sentence makes a substantial NZ contribution to EDC (14.2 % in the LGM) plausible with 14 to 32 % (l. 287). The abstract of Neff and Bertler (2015, Journal of Geophysical Research: Atmospheres 120, 9303 to 9322) gives no percentages; it says "New Zealand and Patagonia rapidly contribute a high proportion of trajectories to West Antarctica" and "in interior East Antarctica, source contributions are limited and highly mixed". If the 14 to 32 % refers to trajectories reaching West Antarctica or Antarctica as a whole, it does not support NZ dust at Dome C. The full text could not be read, so this is a question. |
| Suggestion | At l. 287 state the region and quantity (trajectory fraction or deposition fraction) to which 14 to 32 % refers, with page or table of Neff and Bertler (2015); if it refers to West Antarctica, change "inland Antarctic deposition" and add the abstract's qualification for interior East Antarctica. |
| Status | verified (wording of the abstract, read by instance S1); inferred (what the full text reports) |
| Severity | moderate |
| Source | S1 |

**GB-38 The larger Holocene variability is interpreted climatically, but sampling density, integration time, analytical noise and fit quality change with it, and "significantly" is not backed by a test.**

| Field | Content |
|---|---|
| Check | P9, P15, P21 |
| Location | p. 9, l. 306 to 308; p. 1, l. 24 to 25; p. 4, l. 110 to 112; p. 6, l. 175 to 179; Fig. 1 caption, p. 25, l. 852; Supplement Table S1 |
| Quotation | "our unmixing model reveals a significantly larger variability"; "This increased variability, seemingly higher"; "culminating during the Holocene with" |
| Concern | The increase is clear in Table S1: the standard deviation of the PAT share is 9.9 (LGM), 10.8 (HS1), 14.5 (ACR), 29.5 (YD) and 32.1 percentage points (Holocene) (Python). Four design properties differ between Holocene and glacial samples, and each alone raises apparent variability: (1) spacing: median 43 yr between retained Holocene samples against 134 yr in the LGM, so the 9-step moving average of Fig. 1 spans about 8 × 43 = 340 yr against 8 × 134 = 1070 yr; (2) integration: 2 to 3 yr per Holocene sample against 4 to 5 yr in the LGM (l. 112); (3) analytical noise: MREE and HREE uncertainties of 25 to 35 % in Holocene against 5 to 8 % in glacial samples (Gabrielli et al., 2010, p. 266, as read by instance SD), and the manuscript itself describes post-14 kyr samples "near the detection limit" (l. 176); (4) fit quality: median R 0.80 in the Holocene against 0.925 in the LGM. At the same nominal age, Table S1 gives PAT 86.7 and 0.0 % (3559 yr), 0.0 and 38.2 % (10511 yr), 39.5 and 71.9 % (12841 yr), against 68.8 and 72.5 % for the glacial pair (28709 yr); such pairs suggest that sample-to-sample scatter in the Holocene is of the size of the signal. No test supports "significantly". Does the contrast persist after aggregating Holocene samples to the glacial integration length and after accounting for the per-sample Monte Carlo uncertainty? Graded major: the Holocene variability is a stated result in the Abstract (l. 24 to 25) and Section 4.3, and aim 1 targets the Holocene. |
| Suggestion | In Section 4.3 report a variability measure per period, test whether between-sample variance exceeds the within-sample Monte Carlo variance (with period-specific analytical uncertainty, GB-13), compare variability at equal temporal resolution by binning the Holocene to the glacial spacing and by smoothing over a fixed time span (for example 1 kyr) instead of 9 steps in Fig. 1, use the duplicate ages as replicates, and revise l. 306 to 310 and the Abstract (l. 24 to 25) according to the outcome. |
| Status | verified (integration times, noise statements and Table S1 values); inferred (spacing, standard deviations and R medians computed from Table S1); assumption (the share of the variability that is an artefact, asked as a question) |
| Severity | major |
| Source | S3, S4, SD |

**GB-39 A lead-isotope provenance study on the same EDC core, which reports interglacial samples with more than 50 % local Antarctic dust and finds Australia not a major source, is neither cited nor discussed.**

| Field | Content |
|---|---|
| Check | P14 |
| Location | p. 10, l. 324 to 334; p. 13, l. 438 to 443; p. 8, l. 258 to 260; reference list (p. 16 to 22) |
| Quotation | "our results do not indicate significant Antarctic contributions to EDC" |
| Concern | The manuscript validates its model only against Sr-Nd data (Section 4.1) and finds negligible Antarctic input (ANT 0.0 to 0.6 % in Table S5). Vallelonga, P., Gabrielli, P., Balliana, E. et al. (2010) Lead isotopic compositions in the EPICA Dome C ice core and Southern Hemisphere Potential Source Areas. Quaternary Science Reviews 29, 247 to 255, https://doi.org/10.1016/j.quascirev.2009.06.019, studied the same core and state: "The EDC samples which indicate a >50% input from such a local Antarctic dust source correspond to interglacial periods", concluding that Australian source areas are not a major component of Antarctic dust. This contradicts two Holocene results of the manuscript (negligible ANT, 23 % AUS). The reference list contains only Vallelonga et al. (2002), on the pollution history at Law Dome; other Pb studies are cited (l. 365, l. 367), so the omission concerns the Pb study closest to the data set. Graded moderate: the record stands, but its validation and the rejection of Antarctic sources cannot be assessed without this comparison. |
| Suggestion | In Section 4.1 (after l. 258) or at l. 329 to 334 cite Vallelonga et al. (2010) and discuss its interglacial local-Antarctic and Australian findings against the present Holocene contributions, including the limits of Pb that the study itself names. |
| Status | verified (study read by instance S1 in an author copy; absence from the reference list) |
| Severity | moderate |
| Source | S1 |

**GB-40 The wind argument against McMurdo dust at Dome C cites a source that names another wind direction, and a wind "from the east-southeast" blows toward Dome C, not away from it.**

| Field | Content |
|---|---|
| Check | P13 |
| Location | p. 10, l. 333 to 334 |
| Quotation | "Furthermore, dominant winds in the McMurdo"; "opposite to the direction toward Dome C (Speirs et al., 2001)." |
| Concern | The argument is used to reject the 24 % Antarctic component of Coppo et al. (2022) (l. 327 to 334). The abstract of the listed Speirs et al. (2010, Journal of Climate 23, 3577 to 3598) states that "foehn winds in the MDVs are caused by topographic modification of south-southwesterly airflow"; it does not describe east-southeasterly winds as dominant. Geometry (Python, approximate coordinates): the initial bearing from the McMurdo Dry Valleys (77.5° S, 162.0° E) to Dome C (75.1° S, 123.35° E) is about 265°, that is west; a wind from the east-southeast (112.5°) blows toward 292.5°, 27° from that bearing, so broadly toward Dome C. The sentence would hold only for a wind toward the east-southeast. The citation year is GB-45. |
| Suggestion | At l. 333 to 334 state the wind direction that the cited study reports and rewrite the sentence so that the direction relative to Dome C follows from it; if the down-valley foehn is meant, say so. |
| Status | verified (abstract wording, read by instance S1); inferred (bearing calculation) |
| Severity | moderate |
| Source | S1 |

**GB-41 The agreement between the Patagonian record and the Potrok Aike wind proxy is asserted as "matching well" without a measure, while the text needs a separate explanation for 11 to 8 kyr BP.**

| Field | Content |
|---|---|
| Check | P15 |
| Location | p. 10, l. 339 to 341 and l. 343 to 348; p. 11, l. 348 to 349; Fig. 5, panels A and B (p. 29) |
| Quotation | "provenance record for PAT contributions is matching well with the SWW intensity proxies in Potrok"; "At first glance, this seems unfavorable for PAT dust emissions" |
| Concern | No correlation or other measure is given, although the authors use correlation coefficients elsewhere (l. 168 to 172). The 11 to 8 kyr BP interval is explained by fires (l. 343 to 348), which shows that the match is not uniform; the 6 to 6.5 kyr BP feature is GB-43, the missing time axis of Fig. 5 GB-61. In the same passage "SWW" is used at l. 339 before its definition at l. 340 to 341, and the record is called "Potrok Aike bog" (l. 339 to 340, l. 348 to 349), while the caption of Fig. 5 describes "lacustrine sediments in Laguna Potrok Aike". |
| Suggestion | Report a correlation between the PAT series and the MDF series for the Holocene after resampling to common ages (with the number of points) in Section 4.3, or replace "matching well" by a description of the intervals of agreement and disagreement; write "Southern Westerly Winds (SWW) intensity proxies from Laguna Potrok Aike" at l. 339 to 340, "a weakening of the SWW" at l. 340 to 341 and "Laguna Potrok Aike, 52°S" at l. 348 to 349. |
| Status | verified |
| Severity | moderate |
| Source | S4, S2, AB |

**GB-42 Fig. 5 is cited before Fig. 4.**

| Field | Content |
|---|---|
| Check | P3, P4 |
| Location | p. 10, l. 340; p. 12, l. 405 |
| Quotation | "Aike bog (see Figure 5)" |
| Concern | The first citations of the main figures are Fig. 1 (l. 183), Fig. 2 (l. 244), Fig. 3 (l. 281), Fig. 5 (l. 340) and Fig. 4 (l. 405), so the figures are not numbered in the order of first citation. |
| Suggestion | Swap the numbers of Figures 4 and 5 (Laguna Potrok Aike comparison as Fig. 4, EDC minus EDML bars as Fig. 5) and update l. 340, l. 405, l. 419 and the captions. |
| Status | verified (citations confirmed on the page images) |
| Severity | minor |
| Source | AB, S4 |

**GB-43 The drop of the Patagonian contribution at 6 to 6.5 kyr BP that the text finds also in the Potrok Aike wind record is not visible in Fig. 5B.**

| Field | Content |
|---|---|
| Check | P3 |
| Location | p. 11, l. 350 to 351; Fig. 5, panel B (p. 29) |
| Quotation | "PAT contributions between 6-6.5 kyr BP (also present in Potrok Aike wind intensity record)" |
| Concern | The PAT drop is present in Fig. 5A and Fig. 1 (smoothed minimum 28.5 % at 6,329 yr, measured by instance AB). In panel B (calibrated: 10 mT at 1267 px, 60 mT at 1566.5 px), all line pixels between 6.0 and 6.5 kyr lie between 16.2 and 18.5 mT, those between 6.5 and 7.5 kyr between 14.7 and 18.5 mT and those between 5.0 and 6.0 kyr between 14.2 and 23.9 mT. A weakening of the wind would appear as higher MDF; the 6 to 6.5 kyr window differs from its neighbours by less than 2 mT, whereas excursions between 8 and 11.4 kyr reach above 40 mT. |
| Suggestion | Mark the 6 to 6.5 kyr feature in Fig. 5B and give its MDF amplitude, or delete the parenthesis at l. 351. |
| Status | verified (measured by instance AB) |
| Severity | moderate |
| Source | AB |

**GB-44 The statement that the Southern Altiplano contributes only after ~11.2 kyr BP contradicts Table S1, which carries the timing link to paleolake Coipasa.**

| Field | Content |
|---|---|
| Check | P2, P15, P24 |
| Location | p. 11, l. 357 to 360; p. 7, l. 211 to 212; Supplement Table S1, two rows 12841 (Suppl. page 13); Supplement Figure S3, panel Altiplano (Suppl. page 6) |
| Quotation | "Southern Altiplano begins contributing dust only after approximately 11.2 kyr BP, a timing that"; "4%, increasing to ~5% during the ACR and YD, primarily from the South Puna region." |
| Concern | Table S1 lists Altiplano contributions of 16.6 % and 12.8 % in the two YD rows dated 12841 yr (R 0.69 and 0.77); all other Altiplano values between 11228 and 12841 yr are 0.0 (Python, confirmed on the page image). The earliest Altiplano contribution is therefore at 12.8 kyr BP, within the YD. Figure S3, cited for this paragraph at l. 355, also shows Altiplano values before 11.2 kyr BP (raw peak 38.8 % at 11,857 yr; smoothed curve above 1 % up to 12,772 yr, measured by instance AB), although Figure S3 itself disagrees with Table S1 (GB-31). In the YD, the mean Altiplano share is 3.27 % against 1.26 % for Puna (n = 9), so l. 211 to 212 holds for the ACR (Puna 5.23 %, Altiplano 0.00 %, n = 8) but not for the YD. The coincidence with the final desiccation of paleolake Coipasa rests on the 11.2 kyr BP onset. Instances S3 and S4 graded moderate, AB major; merged as major because the timing link is part of the answer to aim 3 and the table contradicts its premise. |
| Suggestion | State the earliest Altiplano contribution from Table S1 (12.8 kyr BP) at l. 358 and at l. 211 to 212, and either reassess the link to the Coipasa desiccation at l. 359 to 360 or explain why the two YD values are disregarded. |
| Status | verified (Table S1 on the page image; Figure S3 measured by instance AB); inferred (YD and ACR sub-region means) |
| Severity | major |
| Source | S3, S4, AB |

**GB-45 Three citations in the text do not match the reference list, and one entry is not cited.**

| Field | Content |
|---|---|
| Check | P4 |
| Location | p. 11, l. 365; p. 10, l. 334; p. 13, l. 439; reference list p. 17, l. 551 to 552; p. 18, l. 630 to 632; p. 21, l. 781 to 783 |
| Quotation | "with the previous Pb isotopic study (Gili et al., 2016)"; "(Speirs et al., 2001)."; "(De Deccker et al., 2019; Revel-Rolland" |
| Concern | (1) Gili et al., 2016 has no entry; the list has Gili et al. 2017 and 2022 only. (2) Speirs et al., 2001 has no entry; the list has Speirs et al., 2010 (Journal of Climate 23, l. 781 to 783). (3) "De Deccker et al., 2019" corresponds to the single-author entry "De Deckker, P., 2019" (l. 551), so spelling and "et al." deviate. (4) The entry Gaiero, Brunet, Probst and Depetris (2007, Chemical Geology 238; l. 630 to 632) is not cited; "Gaiero, 2007" (l. 274, l. 862) refers to the single-author entry. The EPICA Community Members (2006) entry is cited only in the caption of Figure S2. |
| Suggestion | Add the Gili et al. (2016) entry; write "Speirs et al., 2010" at l. 334 and "De Deckker, 2019" at l. 439; cite or delete the Gaiero et al. (2007) entry. |
| Status | verified |
| Severity | minor |
| Source | S4 |

**GB-46 The hydrological sources cited for Australia report a later and weaker Lake Eyre wet phase than stated, and the cited lead-isotope study links Australian dust supply to wet phases, the opposite of the mechanism invoked.**

| Field | Content |
|---|---|
| Check | P13 |
| Location | p. 11, l. 366 to 374 |
| Quotation | "As far as Australian dust contribution, our model identifies the Darling sub-basin as the dominant"; "which was also suggested by De Deccker et al. (2010) using Pb isotopes."; "These humid intervals would have lowered dust emissions from central Australia." |
| Concern | The identification of the Darling sub-basin agrees with De Deckker et al. (2010), whose abstract states that the data "supports the Darling sub-basin as a potential source of aeolian material to Antarctica". Two parts of the paragraph are not reproduced as the sources state them. (a) Magee et al. (2004, Geology 32, 885 to 888) date the abrupt dry-to-wet transitions to "ca. 125 and 12 ka" and describe a "low intensity of the early Holocene Australian monsoon", which does not support "prolonged wet conditions" at Lake Eyre from 14.5 to 4 kyr BP (l. 368 to 370). (b) De Deckker et al. (2010) place the Australian supply "more particularly during wet phases in Australia", whereas l. 370 to 374 argue that humid phases lowered emissions. Citing the same study for the source region while leaving out its opposite mechanism is a selective reproduction. Graded moderate: the main conclusion on the Patagonian shift does not depend on it, but the claimed hydrological support for the Australian record (aim 3) does. Singh and Luly (1991) were not read. The missing numbers for the Darling result are GB-20. |
| Suggestion | At l. 368 to 370 give the timing and character of the Lake Eyre wet phase as Magee et al. (2004) report it and state which interval Singh and Luly (1991) cover; at l. 366 to 374 discuss that De Deckker et al. (2010) associate Australian dust supply with wet phases and explain why the present record supports the opposite relation; write "As far as the Australian dust contribution is concerned" at l. 366 and "De Deckker et al. (2010)" at l. 367. |
| Status | verified (abstracts of Magee et al. 2004 and De Deckker et al. 2010, read by instance S1) |
| Severity | moderate |
| Source | S1, S4 |

**GB-47 Figure S4 is cited for a Holocene trend in the Southern African contribution, but it contains one Holocene panel and cannot show a trend.**

| Field | Content |
|---|---|
| Check | P3 |
| Location | p. 12, l. 382; Supplement Figure S4 (Suppl. page 8) |
| Quotation | "results show an increasing trend in SAF dust contribution to EDC ice core (Figure S4), which is" |
| Concern | Figure S4 shows box plots for five periods, of which one is a Holocene period (labelled "Early Holocene", showing the Late Holocene, GB-28). A trend within the Holocene is visible only in a time series (Fig. 1, panel SAF). Table S5 gives a slight increase from the Early Holocene (9.8 %) to the Late Holocene (11.6 %). |
| Suggestion | At l. 382 cite "(Figure 1; Table S5)" instead of "(Figure S4)", or give the Early and Late Holocene means. |
| Status | verified (panels on the page image; Table S5) |
| Severity | minor |
| Source | AB, S4 |

**GB-48 Vickery et al. (2013) attribute most present-day southern African dust plumes to pans, not to ephemeral riverbeds.**

| Field | Content |
|---|---|
| Check | P13 |
| Location | p. 12, l. 391 |
| Quotation | "Notably, ephemeral riverbeds represent the majority of present-day dust plumes (Vickery et al., 2013" |
| Concern | The sentence supports the explanation why Namibian riverbeds were detected most frequently (l. 385 to 390). Vickery et al. (2013, Geophysical Research Letters 40, 5274 to 5279) state: "Pans dominate in terms of sources count (57%) and number of detectable plumes (64%)"; their Table 1 gives 208 of 328 plumes from pans and 113 of 328 from rivers (208 / 328 = 63.4 %; 113 / 328 = 34.5 %). Their statement that "Ephemeral rivers accounted for more than half of all plume sources in this region" refers to sources in the Namib region, not to plumes across southern Africa. The manuscript changes both the region and the counted quantity. |
| Suggestion | At l. 391 write that ephemeral rivers account for more than half of the plume sources in the Namib region, while across southern Africa pans produce about 64 % and rivers about 34 % of plumes. |
| Status | verified (source read by instance S1 in an author copy; shares recomputed) |
| Severity | moderate |
| Source | S1 |

**GB-49 The EDML values used for the EDC and EDML comparison differ from the published values of the cited EDML study and come from a different method configuration, and the manuscript does not say whether EDML was recalculated.**

| Field | Content |
|---|---|
| Check | P13, P7, P9 |
| Location | p. 12, l. 403 to 409; p. 5, l. 144 to 145; p. 9, l. 288; p. 13, l. 417 to 424; p. 1, l. 27 to 29; p. 3, l. 77 to 82; Supplement Table S5, block EDML (Suppl. page 22); Fig. 4 (p. 28); Supplement Figure S5 |
| Quotation | "The only continuous and quantitative dust provenance record in EA available for direct comparison with"; "n was equal to 14 but is only 13 in the present study because of the exclusion of Gd"; "our previous EDML ice core work detected NZ dust at ~6 % on average over the entire LGM." |
| Concern | Building aim 4 on an existing record from the same algorithm is a strength, but the numbers do not match the abstract of Vanderstraeten et al. (2023, Science of the Total Environment 881, 163450): before 14.5 kyr BP Patagonia "~68 %", Australia 14 to 15 %, Southern Africa ~9 %, New Zealand ~3 to 4 %; after 14.5 kyr BP Patagonia "below 50 % on average", Southern Africa 21 to 23 %, Australia 13 to 21 %; early Holocene Patagonia "~50 % on average". The introduction (l. 79 to 80) repeats "below 50% on average". Table S5 (EDML), checked on the page image, gives PAT 73.7 (LGM) and 71.6 (HS1), NZ 6.2 and 6.5, AUS 9.7 and 9.4, and after 14.5 kyr BP PAT 62.5 (ACR), 58.4 (YD) and 62.7 (Early Holocene) and SAF 12.4, 8.2 and 11.2; no weighting of 58.4 to 62.7 falls below 50 %. The comparison changes with the source values: Holocene PAT difference 49.0 minus 62.7 = minus 13.7 with Table S5 (stated "-14%"), but about minus 1 with ~50 %; LGM NZ 14.2 minus 6.2 = plus 8.0 (stated "+8%"), but plus 10.2 to 11.2 with 3 to 4 %; LGM AUS plus 0.5 with Table S5, but about minus 4 to minus 5 with 14 to 15 %. The abstract's "EDML from Southern Africa" (l. 29) agrees with the published 21 to 23 % but not with Table S5, where EDML AUS exceeds SAF in the ACR (18.5 against 12.4) and YD (19.0 against 8.2). In addition the configurations differ: the EDML study used 14 REE (l. 144 to 145) and, according to its abstract, "a new database of 207 Rare Earth Element (REE) patterns", while EDC uses 13 REE and 217 patterns, and the EDML samples come from another measurement campaign (Wegner et al., 2012), so the reported core differences (l. 417 to 428) may include method effects. One explanation would be that EDML was rerun with the present configuration; the manuscript does not say so, and Figure S5 and l. 404 attribute the record to the 2023 publication. Graded major: aim 4, the differences at l. 417 to 424, the abstract sentence at l. 27 to 29 and the Conclusion at l. 484 to 487 depend on these values. |
| Suggestion | State in Section 2 and in the captions of Table S5, Fig. 4 and Figure S5 whether the EDML contributions were recalculated (database, number of REE, sample selection, Monte Carlo settings, R threshold) or taken from Vanderstraeten et al. (2023). Preferably rerun EDML with the identical configuration (13 REE, the same 217 patterns, the same settings), report both versions and their differences with uncertainties, recompute l. 288, l. 417 to 424 and Fig. 4, and align l. 79 to 80 and the Abstract (l. 27 to 29) with the version used. |
| Status | verified (published abstract values, read by instances S1 and SD; Table S5 on the page image; l. 144 to 145); inferred (recomputed differences; size of the method effect) |
| Severity | major |
| Source | S1, SD |

**GB-50 The EDC minus EDML differences for ACR and YD are swapped and misattributed in the text, and the Holocene difference compares unequal windows, contrary to the stated common interval.**

| Field | Content |
|---|---|
| Check | P2, P3, P5, P9, P15, P21 |
| Location | p. 13, l. 421 to 424; p. 12, l. 405 to 407; Fig. 4, bars ACR, YD and "Holo" (p. 28); Supplement Table S5 |
| Quotation | "the ACR and YD intervals exhibit a slight enrichment of Patagonian"; "dust (+4 and +6.5%) in EDC, primarily at the expense of Southern African and Australian contributions."; "PAT dust (-14%) but higher contributions of Australian dust (+12%) than EDML."; "between 7.5 and 27 kyr BP." |
| Concern | From Table S5: PAT ACR 68.9 minus 62.5 = plus 6.4, YD 63.1 minus 58.4 = plus 4.7; the text assigns +4 to the ACR and +6.5 to the YD, while Fig. 4 shows the ACR bar higher (measured plus 6.56 and plus 5.04). In the YD, SAF is 14.6 minus 8.2 = plus 6.4 (bar plus 6.56), so the YD enrichment of PAT is not at the expense of Southern African dust; it is balanced by AUS (minus 4.5), NZ (minus 3.9) and PAP (minus 2.4). Only in the ACR do SAF (minus 4.4) and AUS (minus 7.4) both decrease. The Holocene values result from EDC Holocene 2.8 to 11.7 kyr (49.0, 23.1) against EDML Early Holocene 7.5 to 11.7 kyr (62.7, 10.8): minus 13.7 and plus 12.3; the measured "Holo" bars (PAT minus 13.89, AUS plus 12.52, NZ plus 0.46) match this variant. With the common window named at l. 406 to 407 (Early Holocene in both cores) the differences are PAT minus 15.6, AUS plus 14.1 and NZ plus 2.6, which the NZ bar does not show. The direction holds, but the numbers rest on unequal windows and cannot be reproduced from the stated rule. |
| Suggestion | At l. 421 to 422 write "(+6.4 and +4.7%)" for ACR and YD and state that the YD enrichment is at the expense of AUS, NZ and PAP while SAF is higher in EDC; compute the Holocene bars of Fig. 4 and the values at l. 423 to 424 from the EDC Early Holocene (7.5 to 11.7 kyr) and label the bars "Early Holocene". |
| Status | verified (Table S5; Fig. 4 bars measured by instance AB); inferred (differences computed) |
| Severity | moderate |
| Source | S3, S4, AB, SD |

**GB-51 Two sources cited for Australian dust transport to Antarctica concern other subjects: a jet-stream case study without dust, and anthropogenic lead at Law Dome.**

| Field | Content |
|---|---|
| Check | P13 |
| Location | p. 13, l. 434 to 435; p. 13, l. 438 to 440 |
| Quotation | "southeast Australia can inject dust into the STJ"; "Other studies have similarly identified regions in Australia as"; "significant contributors to both western and eastern Antarctica" |
| Concern | (a) The abstract of Yang et al. (2024, Atmospheric Science Letters 25, e1203) analyses the superposition of the subtropical and polar-front jets over the southwest Pacific and does not mention dust, aerosol or Antarctica; the full text was not read. (b) Vallelonga et al. (2002, Earth and Planetary Science Letters 204, 291 to 306) attribute the Law Dome lead event of 1884 to 1908 to "Pb mined at Broken Hill and smelted at Broken Hill and Port Pirie, Australia", that is anthropogenic lead, and report a natural "rock and soil dust Pb contribution of 8-12%" without assigning it to Australia. Neither source shows Australian mineral dust reaching Antarctica. The citation form "De Deccker et al., 2019" is GB-45. |
| Suggestion | At l. 435 cite a study that documents dust injection into the jet system over southeast Australia, or phrase the sentence as a meteorological possibility; at l. 439 to 440 remove Vallelonga et al. (2002) or restrict it to anthropogenic lead, and write "both West and East Antarctica". |
| Status | verified (Vallelonga et al. 2002 abstract, read by instance S1); inferred (Yang et al. 2024, only the abstract was readable) |
| Severity | moderate |
| Source | S1, S4 |

**GB-52 The cited Figures S2 and S5 do not show the decline of total dust deposition "in both cores".**

| Field | Content |
|---|---|
| Check | P4, P3 |
| Location | p. 13, l. 448 to 450; Supplement Figure S2, panel A (Suppl. page 4); Supplement Figure S5 (Suppl. page 10) |
| Quotation | "deposition that began around 19-18 kyr BP and continued until ~15 kyr BP in both cores (Figures S2" |
| Concern | Figure S2 shows the nssCa flux of EDC only; Figure S5 shows relative contributions (in %) of EDC and EDML, no deposition flux. The EDML part of the statement has no target in the manuscript. |
| Suggestion | Add the EDML dust flux to Figure S2 or cite its source (for example Fischer et al., 2007) at l. 449, and remove "S5" from the reference. |
| Status | verified (panel contents on the page images) |
| Severity | minor |
| Source | S4, AB |

**GB-53 Research aims 1 and 2 are not taken up in the Conclusion: neither the Sr-Nd validation nor the Holocene provenance question "for which there is no consensus".**

| Field | Content |
|---|---|
| Check | P15 |
| Location | p. 14, l. 472 to p. 15, l. 492; p. 3, l. 91 to 94; p. 10, l. 324 to 326 |
| Quotation | "throughout the LGIT and particularly during the Holocene for which there is no consensus (e.g. Paleari"; "from our REE pattern-based model against Sr-Nd isotopic data published in the literature" |
| Concern | The Conclusion (l. 472 to 492) contains no statement on the isotopic validation (aim 2), although Section 4.1 is devoted to it, and none on how the record resolves the Holocene disagreement (aim 1). The Discussion notes the difference to Coppo et al. (2022) (SSA 33 % against 60 %, l. 325 to 326) but does not explain it, and Paleari et al. (2019), cited for the lack of consensus, is not discussed again. |
| Suggestion | Add to the Conclusion one sentence on the Sr-Nd comparison (with the restriction of GB-33) and one on the Holocene provenance, including how the difference to Coppo et al. (2022) and Paleari et al. (2019) is explained, and add that explanation to Section 4.3. |
| Status | verified |
| Severity | moderate |
| Source | S4 |

**GB-54 The Conclusion explains the EDC and EDML differences by climate in the source areas, while Section 4.4 explains them by the position of the sites relative to atmospheric pathways.**

| Field | Content |
|---|---|
| Check | P15 |
| Location | p. 14, l. 485 to 487; p. 13, l. 424 to 435; p. 13, l. 440 to 443 |
| Quotation | "SAF, NZ and AUS differed reflecting regional climatic dynamics in their respective source areas."; "consistent with the geographic positioning of the two sites: EDML is exposed to the storm track in the" |
| Concern | Source-area climate acts on the same source for both cores; by itself it cannot produce different contributions of the same PSA at EDC and EDML. Section 4.4 accordingly attributes the differences to exposure to the storm track, the polar vortex and jet pathways (l. 425 to 435), with low-latitude aridity as an additional factor for the common Holocene increase (l. 440 to 443). The Conclusion thus answers aim 4 (spatial variability, l. 96 to 98) with a mechanism the Discussion does not develop. Graded major: the Conclusion's answer to aim 4 changes. |
| Suggestion | Rewrite l. 486 to 487 so that the Conclusion attributes the between-core differences to atmospheric transport and site position as in Section 4.4, and source-area climate to the changes common to both cores. |
| Status | verified |
| Severity | major |
| Source | S4 |

**GB-55 The iron-fertilisation frame of the introduction is not revisited, and the Conclusion's "implications for biogeochemical fluxes" has no basis in the Discussion.**

| Field | Content |
|---|---|
| Check | P15, P10 |
| Location | p. 15, l. 490 to 492; p. 2, l. 37 to 52; Discussion, Sections 4.1 to 4.4 |
| Quotation | "Hemisphere dust cycle during the LGIT, with implications for biogeochemical fluxes, atmospheric" |
| Concern | The introduction motivates the study by dust-borne iron fertilisation, pCO2 and inter-source differences in iron content and solubility (l. 37 to 52). A search of l. 219 to 492 finds no occurrence of "iron", "fertili" or "CO2" (Python); no aim addresses iron, the announced PSA fluxes are not shown (GB-14), and the closing implication at l. 491 remains unsupported. |
| Suggestion | Add a short paragraph to Section 4.3 or 4.4 that relates the change in source shares to the iron frame of l. 37 to 52 (for example in terms of source-specific iron content), or remove "biogeochemical fluxes" from l. 491 and shorten the iron-fertilisation motivation to what the study delivers. |
| Status | verified |
| Severity | moderate |
| Source | S4, SD |

**GB-56 The author contribution statement names a "P.B" who matches no author, and gives no role for two authors.**

| Field | Content |
|---|---|
| Check | P38, P4 |
| Location | p. 16, l. 497 to 499; byline p. 1, l. 4 to 5 |
| Quotation | "P.B performed the measurements; A.V., St. B and G.L. developed" |
| Concern | The byline lists Sibylle Boxho, Aubry Vanderstraeten, Nadine Mattielli, Goulven G. Laruelle, Aloys Bory, Paolo Gabrielli and Steeve Bonneville; no author has the initials P.B. The statement otherwise distinguishes "Si.B" and "St.B". N.M. and A.B. appear only under "All authors reviewed the manuscript". Is P.G. (Paolo Gabrielli, author of the REE data set, l. 108) meant? |
| Suggestion | Correct the initials at l. 497, state the contributions of N.M. and A.B., and write "St.B. and G.L. jointly developed the model" at l. 497 to 498. |
| Status | verified (initials mismatch, page images p. 1 and 16); assumption (intended author, asked as a question) |
| Severity | minor |
| Source | S2, S4 |

**GB-57 The supplement cites seven sources that appear in no reference list, among them the sources of the measured ice-core isotopes in Table S4 and of most Australian patterns in Table S2.**

| Field | Content |
|---|---|
| Check | P4 |
| Location | reference list (p. 16 to 22); Supplement Table S2, column "Reference" (Suppl. pages 16 to 19); Supplement Table S4, column "Reference" (Suppl. page 21) |
| Quotation | "Marx and Kamber, 2010"; "[Aarons et al. (2017)]"; "[Bory et al. (2010)]"; "[Delmonte et al., 2004a]" |
| Concern | Counted in the supplement (Python, confirmed on Suppl. pages 17 and 21): Marx and Kamber, 2010 (101 rows), Aarons et al. 2017 (18), Bory et al. 2010 (14), Marx et al. 2005 (10), Diaz et al. 2018 (4), McGowan et al. 2005 (2) and Delmonte et al. 2004a (2). None is in the main reference list, and the supplement has no reference list of its own; "2004a" implies a second Delmonte 2004 entry that does not exist. These sources supply the source database and the measured values plotted in Fig. 2, whose provenance cannot be traced without them. The discussion of Aarons et al. (2017) is GB-05. |
| Suggestion | Add the six missing works to the reference list (or a supplement reference list) and change "2004a" to "2004" in Table S4. |
| Status | verified |
| Severity | moderate |
| Source | S4 |

**GB-58 The reference list prints RTF control codes in 18 entries and mixes several citation formats.**

| Field | Content |
|---|---|
| Check | P16 |
| Location | p. 16, l. 528; p. 17, l. 553, l. 556 and l. 584 to 593; p. 18, l. 606, l. 632 to 636 and l. 645 to 654; p. 19, l. 693 to 694 and l. 703 to 710; p. 20, l. 714 to 716, l. 726 to 729, l. 742 and l. 746 to 758; p. 21, l. 795, l. 799 and l. 817; p. 22, l. 821 to 828 and l. 844 to 846 |
| Quotation | "471\uc0\u8211{}501. https://doi.org/10.1191/0309133303pp386ra\"; "Agricultural\uc0\u8208{}Like" |
| Concern | Confirmed on the page images: control codes for dashes, apostrophes and accented letters and trailing backslashes after DOIs appear in the entries Bullard and McTainsh 2003, De Deckker et al. 2014, Dukes et al. 2018, Engelbrecht et al. 2019, Fletcher and Moreno 2012, Gaiero et al. 2007, Gingele and De Deckker 2005, Grousset and Biscaye 2005, Lisé-Pronovost et al. 2015, Markgraf et al. 2007, Markle et al. 2018, Moreno et al. 2010, Power et al. 2008, Quade and Kaplan 2017, Stone et al. 2010, Stuut et al. 2002, Veres et al. 2013 and Wagner et al. 2021. Format deviations: Ding et al. 2011 (year at the end, "et al." in the author list), Gaiero et al. 2013 (initials before surnames, year in parentheses), Yang et al. 2024 (APA style), Parrenin et al. 2007 (no volume, pages or DOI, and nine co-authors missing: Barnola, Beer, Blunier, Castellano, Chappellaz, Dreyfus, Fischer, Fujita and Petit). |
| Suggestion | Regenerate the reference list from the reference manager in one style, remove the control codes and backslashes, and complete the entry at l. 726 to 729 as "... chronology for the EPICA Dome C ice core. Clim. Past 3, 485-497. https://doi.org/10.5194/cp-3-485-2007" with the full author list. |
| Status | verified (page images p. 16 to 22; Parrenin et al. 2007 record checked by instance S4) |
| Severity | minor |
| Source | S4 |

**GB-59 The captions of Fig. 2 and Fig. 4 cite the wrong supplementary tables.**

| Field | Content |
|---|---|
| Check | P3, P4 |
| Location | Fig. 2 caption, p. 26, l. 858 and l. 865; Fig. 4 caption, p. 28, l. 876 |
| Quotation | "cores (refs. Table S1, - open symbols)"; "the isotopic fingerprint (Table S4) and elemental"; "periods for each PSA between EDC and EDML ice cores (Table S4)." |
| Concern | Table S1 holds the PSA contributions per sample, not ice-core isotope data, which are in Table S4. The isotopic fingerprints of the end-members are in Table S3, not in Table S4. The averages from which Fig. 4 is computed are in Table S5 (bar values match Table S5 within 0.4 points, PP-46), whereas Table S4 holds measured isotope ratios. |
| Suggestion | At l. 858 write "(refs. Table S4; open symbols)", at l. 865 "the isotopic fingerprint (Table S3)", and at l. 876 "(Table S5)". |
| Status | verified (table contents on the page images Suppl. pages 20 to 22) |
| Severity | minor |
| Source | AB, S3, S4, SD |

**GB-60 The legend of Fig. 2 uses period classes that Table S4 does not have, and one domain outline has the same colour as a period symbol.**

| Field | Content |
|---|---|
| Check | P29 |
| Location | Fig. 2, legend and domain outlines (p. 26); caption p. 26, l. 858 to 859; Supplement Table S4 |
| Quotation | "calculated isotopic values using REE contributions from" |
| Concern | (1) The legend separates "Early Holocene" and "Holocene"; since the Early Holocene is part of the Holocene, "Holocene" presumably means the Late Holocene, which the caption does not say. (2) Table S4 has one class "Iso Holocene" (22 rows); in the figure the 8 Taylor Glacier values carry the "Iso Holocene" colour and the 14 Berkner Island values the "Iso Early Holocene" colour (measured by instance AB), so the legend class is a site class. (3) The Australia outline (#fcc404) has the same colour as the "EDC YD" symbol (#fcc404), so a yellow dot can be read as either. |
| Suggestion | Rename the legend entry "EDC Late Holocene", give Table S4 the same classes as the legend (or the sites), and draw the PSA domains in colours distinct from the period symbols, for example grey outlines with labels. |
| Status | verified (colours measured by instance AB at the plotted positions) |
| Severity | minor |
| Source | AB |

**GB-61 Fig. 5 has no x-axis title or unit, and its blue band and grey zones are not explained.**

| Field | Content |
|---|---|
| Check | P29 |
| Location | Fig. 5, both panels (p. 29); caption p. 29, l. 880 to 882; p. 10, l. 340 |
| Quotation | "Figure 5: Comparison of the contribution of Patagonian dust (PAT) to EDC ice core (A) and (B)" |
| Concern | The x axis shows 0.5 to 3 without quantity, unit or the ×10^4 factor that Fig. 1 gives, so the alignment of the two panels cannot be read off. The figure has a blue band between dashed lines and three grey zones, but no labels or legend entry, and the caption mentions neither. Measured, the band spans 7,958 to 11,430 yr (±23 yr), while the text relates Fig. 5 to "The 11 to 8 kyr BP period" (l. 340); the grey zones lie at 11,740 to 12,980, 14,760 to 17,980 and from 29,030 yr, that is YD, HS1 and MIS3 as in Fig. 1. |
| Suggestion | Add "Time (yr BP) ×10^4" to the x axis of Fig. 5, label the grey zones as in Fig. 1, and explain the blue band in the caption with its limits (or set it to 8 to 11 kyr BP as at l. 340). |
| Status | verified (measured by instance AB) |
| Severity | minor |
| Source | AB, S4 |

**GB-62 The end-members of Table S3 do not carry the PSA names of the model: "SCWA" stands where the text has CWA, PAP is split, and ANT is missing.**

| Field | Content |
|---|---|
| Check | P38 |
| Location | Supplement Table S3, column "PSA end-members", rows "S-Puna", "S-Altiplano", "Southern Central Western Argentina (SCWA)" (Suppl. page 20); p. 8, l. 245 to 247 |
| Quotation | "Southern Central Western Argentina (SCWA)" |
| Concern | The model and Table S5 use the PSA set PAT, CWA, PAP, SAF, AUS, NZ, ANT. Table S3 lists "SCWA" instead of CWA, and Table S2 uses SCWA1 to SCWA3 for three of the five CWA patterns, so SCWA reads as a subset of CWA. PAP appears as "S-Puna" and "S-Altiplano", and ANT has no row, although Table S5 gives ANT 0.3 % (Holocene) and 0.6 % (Late Holocene). It is not stated which end-member stands for CWA and how ANT enters Eq. 3. Is SCWA meant as the end-member for the whole CWA region? |
| Suggestion | Rename the Table S3 row to the PSA it represents (or explain that the southern CWA patterns stand for CWA), state at l. 245 to 246 that PAP enters as two sub-region end-members, and say how ANT is treated in Eq. 3. |
| Status | verified (labels on the page image Suppl. page 20); assumption (intended mapping, asked as a question) |
| Severity | minor |
| Source | S2 |

**GB-63 The y axes of Figure S2 have no units.**

| Field | Content |
|---|---|
| Check | P29 |
| Location | Supplement Figure S2, panels A to C (Suppl. page 4) |
| Quotation | "(A) Non Sea Salt Calcium (nssCa2+) flux in EDC ice core (Fischer et al., 2007) (B) δ18O in EDC ice core" |
| Concern | The axis titles read "nssCa2+ flux", "δ18O" and "deuterium excess" without unit, although the text gives the flux unit (l. 166, µg m⁻² yr⁻¹); δ18O and deuterium excess are conventionally given in per mil. Panel B also lacks the period shading of panels A and C. |
| Suggestion | Label the axes "nssCa²⁺ flux (µg m⁻² yr⁻¹)", "δ¹⁸O (‰)" and "Deuterium excess (‰)" and add the period shading to panel B. |
| Status | verified (page image) |
| Severity | minor |
| Source | AB |

#### Minor corrections

| ID | Location | Quotation | Replacement | Source |
|---|---|---|---|---|
| KK-21 | p. 7, l. 220 | "in the Epica" | "in the EPICA" | S2, S4 |
| KK-22 | p. 7, l. 229 | "in conjunction with regional climatic evolution (3)" | "in conjunction with regional climatic evolution; and (3)" | S4 |
| KK-23 | p. 7, l. 236 | "This shift already describes by Gili et al. (2022)" | "This shift, already described by Gili et al. (2022)," | S4 |
| KK-24 | p. 8, l. 246 | "e.i. Eq.3" | "i.e. Eq. 3" | S4 |
| KK-25 | p. 8, l. 249 | "where the mean isotopic signatures is represents by CIR PSA" | "where CIR_PSA represents the mean isotopic signature of each PSA" | S4 |
| KK-26 | p. 8, l. 261 | "Persistance of high-latitude dust source" | "Persistence of high-latitude dust sources" | S4 |
| KK-27 | p. 8, l. 270 | "~763.10³ km²" (superscripts on the page image) | "~763 × 10³ km²" | S4 |
| KK-28 | p. 8, l. 272 | "those from SSA- to EDC" | "those from SSA to EDC" | S4 |
| KK-29 | p. 9, l. 300 | "before 14.5 kyr BP reflect a transport regime" | "before 14.5 kyr BP reflects a transport regime" | S4 |
| KK-30 | p. 9, l. 301 | "strong westerlies -a system" | "strong westerlies, a system" | S4 |
| KK-31 | p. 9, l. 305 | "4.3 Holocene Variability in Dust Provenance and Importance of Regional Source Dynamics" | "4.3 Holocene variability in dust provenance and importance of regional source dynamics" (sentence case as in 4.1, 4.2, 4.4) | S4 |
| KK-32 | p. 10, l. 311 | "«wet scavenging»" | "“wet scavenging”" | S4 |
| KK-33 | p. 10, l. 312 | "trajectories inferred by increased" | "trajectories inferred from increased" | S4 |
| KK-34 | p. 10, l. 325 to 326 | "reduction in SSA input -down to" | "reduction in SSA input (down to 33%)" | S4 |
| KK-35 | p. 10, l. 327 | "i.e., 23% and 14%, respectively vs. 23% and 11%, here -" | "(23% and 14%, respectively, vs. 23% and 11% here)" | S4 |
| KK-36 | p. 10, l. 329 | "our Dust Source (DS) database" | "our DS database" | S4 |
| KK-37 | p. 10, l. 329 to 330 | "(Section" ... "4.2)" | "(Section 2; Table S2)" | S4 |
| KK-38 | p. 10, l. 331; p. 13, l. 427 | "over the East Antarctic Plateau"; "located at the interior of EAP" | "over the East Antarctic Plateau (EAP)"; "located in the interior of the EAP" | S2, S4 |
| KK-39 | p. 10, l. 338 | "centered ~9 kyrs BP" | "centered ~9 kyr BP" | S4 |
| KK-40 | p. 10, l. 341 | "Moreno et al. (2010);" | "Moreno et al., 2010;" | S1, S4 |
| KK-41 | p. 10, l. 342 to 343 | "(Quake and" | "(Quade and" | S1, S4 |
| KK-42 | p. 10, l. 346 | "Fires co-emit mineral soil-dust particle" | "Fires co-emit mineral soil-dust particles" | S4 |
| KK-43 | p. 11, l. 353 | "had its prime time" | "reached its largest contribution" | S4 |
| KK-44 | p. 11, l. 354 | "Dust emission from PAP are" | "Dust emissions from PAP are" | S4 |
| KK-45 | p. 11, l. 374 to 375 | "(post-7.5 kry" | "(post-7.5 kyr" | S2, S4 |
| KK-46 | p. 11, l. 376 | "El-Nino-Southern Oscillation" | "El Niño Southern Oscillation" | S4 |
| KK-47 | p. 12, l. 384 to 385 | "suggesting strengthened dust transport from southern Africa suggesting strengthened dust transport from southern Africa" | "suggesting strengthened dust transport from southern Africa" | S4 |
| KK-48 | p. 12, l. 396 | "include few substantial inputs" | "include a few substantial inputs" | S4 |
| KK-49 | p. 12, l. 397 to 398 | "kyr" ... "BP (Brook et al., 2011)." (parenthesis opened before "~15.4" not closed) | "(~15.4 to 13.6, ~11.5 to 8.4 and ~5.5 to 4.0 kyr BP; Brook et al., 2011)." | S4 |
| KK-50 | p. 12, l. 399 | "likely reflect their low-frequency, high-magnitude nature of their dust emissions" | "likely reflect the low-frequency, high-magnitude nature of their dust emissions" | S4 |
| KK-51 | p. 13, l. 426 | "receive dust from Patagonia dust brought" | "receive Patagonian dust brought" | S4 |
| KK-52 | p. 13, l. 428 | "mid-latitude air masses incursions" | "incursions of mid-latitude air masses" | S4 |
| KK-53 | p. 13, l. 441 to 442 | "interactions with PFJ (Ding et al., 2011) - and increased aridity" (opened with a dash after "patterns") | "warmer climate circulation patterns (favoring poleward STJ trajectories and interactions with the PFJ; Ding et al., 2011) and increased aridity" | S4 |
| KK-54 | p. 14, l. 457 | "redirecting large portion of river catchment" | "redirecting a large portion of the river catchments" | S4 |
| KK-55 | p. 16, l. 501 | "APPENDIX S. SUPPLENTARY DATA. Supplementary data to this article" | "APPENDIX S. SUPPLEMENTARY DATA. Supplementary data to this article are available in the Supplement (Tables S1 to S5, Figures S1 to S5)." | S2, S4 |
| KK-56 | p. 20, l. 748 | "Environùental characterization" | "Environmental characterization" | S4 |
| KK-57 | p. 20, l. 763 | "Holland HD, Turkian KK (eds)" | "Holland HD, Turekian KK (eds)" | S4 |
| KK-58 | p. 21, l. 800 | "Sudgen, D. E." | "Sugden, D. E." | S4 |
| KK-59 | Fig. 2 caption, p. 26, l. 863 | "Note that the SAF and AUS domain is more extended than showed in the Figure." | "Note that the SAF and AUS domains extend beyond the plotted area." | S4, AB |
| KK-60 | Fig. 2, x-axis numbers (p. 26); Fig. 3, y-axis numbers (p. 27); Supplement Figure S4, y-axis numbers | "0,700" and "100,00" | "0.700" and "100" | S4, AB |
| KK-61 | Fig. 4 caption, p. 28, l. 875 | "Histograms representing" | "Bar charts showing" | AB |
| KK-62 | Supplement Figure S5, y-axis title (Suppl. page 10) | "PAS EDC Contribution and PSA EDML Contribution ( in %)" | "PSA contribution in EDC and EDML (%)" | S2, S4, AB |

#### Verification log

| ID | Check | Checked | Values | Result |
|---|---|---|---|---|
| PP-34 | P13 | p. 7, l. 238 to 240, LGM isotope values of EDC dust attributed to Delmonte et al. (2004) | Table S4: 0.7086 and -1.66, 0.7088 and -2.46, labelled "Delmonte et al., 2004a"; abstract of Delmonte et al. (2004, Climate Dynamics 23, 427 to 438) confirms Sr-Nd data for the LGM to Holocene transition, numbers not shown | no finding for the LGM values; the uncited Holocene values are part of GB-33 |
| PP-35 | P13 | p. 8, l. 269 to 271 and p. 9, l. 284 to 285, shelf areas from Vanderstraeten et al. (2023): ~763 × 10³ km² (Patagonia), ~62,000 km² (NZ) | not in the 2023 abstract; full text not readable | no finding (limit) |
| PP-36 | P13 | p. 9, l. 277 to 279, l. 291 to 292; p. 10, l. 324 to 328; p. 11, l. 362 to 363: Coppo et al. (2022) | percentages not in the abstract; full text restricted; abstract confirms "Minimum MARs in each section were identified for the Last Glacial Maximum" | no finding (limit) |
| PP-37 | P15 | Discussion values against Table S5 | Holocene AUS, PAP, SAF 23.1, 11.0, 10.7 against "23%, 11% and 11 %" (l. 317); LGM 10.2, 3.6, 6.3 against "10%, 4% and 6%" (l. 317 to 318); Holocene PAT, NZ 49.0, 5.9 against "49% and 6%" (l. 319); LGM SSA 69.3 against "~70%" and AUS 10.2 against "~10%" (l. 281); LGM PAP 3.6 against "~4 %" (l. 289); EDML LGM NZ 6.2 against "~6 %" (l. 288); Coppo comparison 23.1 and 10.7 against "23% and 11%" (l. 327) | consistent; deviations are GB-36 and GB-50 |
| PP-38 | P13 | p. 9, l. 283, Koffman et al. (2021) "argued against significant NZ dust input to EA" | abstract and full text not readable; a different Koffman et al. (2021) paper on Siple Dome excludes Australia and New Zealand for West Antarctica | no finding (limit) |
| PP-39 | P3 | Figure S2 against l. 296, l. 299 and l. 312 | smoothed deuterium excess (panel C): 3 to 10 kyr mean 9.20, 10 to 11.7 kyr 7.87, 11.7 to 14.7 kyr 7.17, 14.7 to 18 kyr 6.01, 18 to 29 kyr 6.34; decline of the nssCa flux from about 18 kyr BP and rise of δ18O from 18 to 15 kyr BP visible in panels A and B | no finding |
| PP-40 | P13 | p. 10, l. 319 to 323, DustCOMM shares for Antarctica (Kok et al., 2021) | Kok et al. (2021), Section 3.4.1: South America "∼ 70 %", Australia "∼ 20 %", southern Africa "∼ 10 %" | no finding |
| PP-41 | P15 | Absence of Antarctic contributions (l. 329 to 330) against Table S5 | ANT 0.0 to 0.6 % in all EDC periods | no finding for internal consistency; the input patterns are GB-10, the single sample GB-25 |
| PP-42 | P2 | Holocene PAT statements against Table S1 | PAT since 5 kyr BP: 25 samples, mean 52.04 % (l. 352, "50-55%"); PAT 7 to 8 kyr: 12 samples, mean 60.83 %, above the Holocene mean of 49.0 % (l. 350, "elevated"); SAF Late against Early Holocene 11.6 against 9.8 % | no finding |
| PP-43 | P13 | p. 11, l. 366 to 367, Darling sub-basin as Australian source (De Deckker et al., 2010) | abstract: "supports the Darling sub-basin as a potential source of aeolian material to Antarctica"; method Pb with Nd and Sr | no finding on the source region; the mechanism is GB-46 |
| PP-44 | P17, P9 | EDC minus EDML in ACR and YD against the standard error of the EDC period mean (l. 407 to 409) | YD PAT plus 4.7 (SE 9.8), SAF plus 6.4 (SE 10.1); ACR PAT plus 6.4 (SE 5.1), AUS minus 7.4 (SE 4.2) | disclosed as tentative by the authors; not raised again; the location of the caveat is GB-19 |
| PP-45 | P15, P7 | LGM window of the EDC and EDML comparison: EDC 18 to 29 kyr BP against the EDML coverage up to 27 kyr BP (l. 406 to 407) | restricted to 18 to 27 kyr BP (n = 25): NZ 14.3 %, PAT 65.2 % against 14.2 and 65.7 % for the full LGM; differences NZ plus 8.1, PAT minus 8.5, AUS plus 0.1 against plus 8.0, minus 8.0, plus 0.5 | no finding |
| PP-46 | P2, P3 | Fig. 4 bars and l. 418 to 421 against Table S5 differences for LGM and HS1 | measured against Table S5: LGM PAT minus 8.09 and minus 8.0, AUS plus 0.61 and plus 0.5, SAF minus 2.90 and minus 2.7, NZ plus 8.21 and plus 8.0, PAP plus 2.28 and plus 2.2; HS1 PAT plus 3.36 and plus 3.2, AUS plus 2.29 and plus 1.9, SAF minus 5.19 and minus 5.3, NZ plus 0.61 and plus 0.6; text "+8%" with equivalent PAT reduction and HS1 "not exceeding ~5%" agree | no finding; ACR, YD and Holocene are GB-50 |
| PP-47 | P13 | p. 13, l. 435 to 438, Nguyen et al. (2019): uplift to 4 to 6 km, transport to the Indian Ocean sector | preprint abstract: dust "located above Antarctica", transport "to Antarctica in the south east"; altitude not in the abstract; journal article not reachable | no finding; altitude and sector not verified |
| PP-48 | P3 | Figure S5 against l. 445 to 447 (decline of PAT between 15 and 14 kyr BP in both cores) | EDC smoothed PAT 71.5 % at 15.0 kyr, 75.0 % at 14.4 kyr, 61.9 % at 14.0 kyr, 55.9 % at 13.0 kyr; EDML from 64.6 % at 14.6 kyr to 38.9 % at 14.4 kyr | no finding for the smoothed curves; the per-sample timing in EDC is GB-22 |
| PP-49 | P15 | Decoupling of provenance shift and flux decline (l. 447 to 450, l. 483 to 484) | Figure S2 panel A: nssCa flux falls from about 600 at 18 kyr BP to near zero at about 14.7 kyr BP (read from the figure); high-latitude share HS1 81.9 % during the decline | the decoupling follows from the data; the causal wording is GB-03 |
| PP-50 | P15, P9 | Outlook and proposed studies | no outlook section, no recommendations, no proposed follow-up studies; the Conclusion ends with implications (l. 490 to 492) | no proposals to check; the closing implication is GB-55 |
| PP-51 | P15 | Theory frame and key terms of introduction and aims in Discussion and Conclusion | aim 3 taken up in Sections 4.2 and 4.3 and in the Conclusion (l. 474 to 477, l. 488 to 490); aim 4 in Section 4.4 and l. 484 to 487; westerly-wind frame (l. 51 to 52) at l. 338 to 352; aims 1 and 2 and the iron frame not taken up | findings GB-53, GB-54, GB-55, GB-01 |
| PP-52 | P4 | Numbering of sections, figures, tables and equations; existence of each target | Sections 1 to 5 with 4.1 to 4.4 without gaps; Figures 1 to 5 each cited; Figures S1 to S5 and Tables S1 to S5 cited; Eq. 3 and 4 referenced at l. 246 and l. 249; supplement tables first cited in the order S1, S2, S5, S3, S4 | no finding beyond GB-42, GB-47, GB-52, GB-59, KK-04, KK-37 |
| PP-53 | P4 | Citations in text and captions against the 91 reference entries, both directions | 89 entries cited in main text or captions; EPICA Community Members 2006 cited only in Figure S2; Gaiero et al. 2007 uncited; citations without entry: Gili et al. 2016, Speirs et al. 2001, De Deccker et al. 2019; spelling deviations Quake (l. 342), Sudgen (l. 800), De Deccker (l. 367) | findings GB-45, GB-46, KK-41, KK-58 |
| PP-54 | P4 | Short citations against entries: year, spelling, "et al." for more than two authors | two-author citations Bullard and McTainsh 2003, Fletcher and Moreno 2012, Gingele and De Deckker 2005, Grousset and Biscaye 2005, Neff and Bertler 2015, Quade and Kaplan 2017, Rudnick and Gao 2003, Singh and Luly 1991, Stanley and De Deckker 2002 match two-author entries; single-author Qu 2016, Gaiero 2007, Caldenius 1932, Bryant 2003 match | no finding beyond GB-45 |
| PP-55 | P16 | Language, characters and layout of l. 219 to 501, the captions of Fig. 2, 4, 5, the reference list and supplement pages 6, 8, 10, 17, 21 on the page images | every minor correction confirmed on the page image; the extracted text of table rows and tick labels was not used for character findings | findings GB-58, KK-21 to KK-62 |
| PP-56 | P3 | Fig. 2 positions of Table S3 and Table S4 values and Eq. 3 and 4 | calibration x 0.700 at 613.5 px, 0.730 at 1946.5 px; y +5 at 693.5 px, -25 at 1455.5 px; all 35 Table S4 values fall on open symbols; sample 12227 recomputed 0.72745 and -17.87, measured 0.7275 and -17.89; text colours at l. 252 to 253 (blue, cyan, green, yellow) match the legend | no finding beyond GB-33 and GB-60 |

## Optional checks

| Area | What it needs | Responsible | Run |
|---|---|---|---|
| DOI resolution | one retrieval per reference entry with a DOI | `science-quellenapparat-pruefung` | no |
| Citation style | the name of the style | `science-zitierstil-harvard-ctr` or the style rules of the journal | no |
| AI declaration against publisher policy | the policy of the target publisher | this review, on request | no |
| Relation to the authors' own prior work | the authors' prior work | this review, on request | no |
| Journal requirements | the author guidelines of the target journal | this review, on request | no |
| Factual accuracy | access to the sources of the checked statements and a selection of sections | `science-faktenbeleg-pruefung`, `geo-frage-belegbasiert-klaeren` | no |

## Limits of this review

- Checked version: egusphere-2025-5046.pdf, 29 pages, SHA-256 f598b53d01e375844cfb549eb05b9a3407bb30cae553e603c125d5f14886c722; supplement egusphere-2025-5046-supplement.pdf, 22 pages, SHA-256 759cfa14195948f5772d3d6d696081932424f4296e51c812415527ed3b108ea6.
- Sources not readable, statements therefore not verified: full texts of Coppo et al. (2022), Koffman et al. (2021), Neff and Bertler (2015), Vanderstraeten et al. (2023), Delmonte et al. (2004, 2008, 2017), Davies et al. (2020), Yang et al. (2024) and Nguyen et al. (2019, journal version); final tables of Krätschmer et al. (2022) (preprint used); Singh and Luly (1991), Brook et al. (2011), Moreno et al. (2010), Fletcher and Moreno (2012). Qualitative citations in Sections 4.2 to 4.4 were not opened. The literature statements in this report rest on the reading of the review instances; the merge re-checked the manuscript side (quotations, table values, counts) but did not reopen the sources.
- Findings with status assumption: 11 of 63 (for at least one part of the finding); the central statement is an assumption in 1 of 63 (GB-07), formulated as a question, as is GB-37, whose core is inferred.
- Optional checks run: 0 of 6.
- Omitted instances: none.
- Discarded findings: 0. All instance findings had the mandatory fields. In the merge, 100 instance findings became 63 findings (37 merged into others); of 101 instance minor corrections, 25 were absorbed into findings and 16 merged as duplicates, leaving 60, plus 2 from the merge; 63 instance verification log entries became 56 (8 merged, 1 added by the merge); individual sub-statements were corrected or dropped as stated in PP-33.
