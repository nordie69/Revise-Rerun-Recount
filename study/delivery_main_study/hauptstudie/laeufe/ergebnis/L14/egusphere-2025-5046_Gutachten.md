# Review report: Quantifying Southern Hemisphere dust sources during the Last Glacial-Interglacial Transition using rare earth elements in the EPICA Dome C ice core

| Field | Value |
|---|---|
| Manuscript | Boxho, S., Vanderstraeten, A., Mattielli, N., Laruelle, G.G., Bory, A., Gabrielli, P., Bonneville, S., 2025. Quantifying Southern Hemisphere dust sources during the Last Glacial-Interglacial Transition using rare earth elements in the EPICA Dome C ice core. EGUsphere preprint egusphere-2025-5046, https://doi.org/10.5194/egusphere-2025-5046 |
| Checked version | egusphere-2025-5046.pdf, 29 pages, SHA-256 f598b53d01e375844cfb549eb05b9a3407bb30cae553e603c125d5f14886c722; supplement egusphere-2025-5046-supplement.pdf, 22 pages, SHA-256 759cfa14195948f5772d3d6d696081932424f4296e51c812415527ed3b108ea6 |
| Date | 2026-10-17 |
| Language | English |
| Review instances | Segments 1 to 4, figures, study design; the six review instances ran as separate agents; no instance omitted |

## Summary

The manuscript is a modelling study that applies a statistical unmixing algorithm (DEPOT, non-negative least squares with MATLAB lsqnonneg) to published rare earth element (REE) concentrations of the EPICA Dome C (EDC) ice core (Gabrielli et al., 2010) in order to quantify the contributions of seven Southern Hemisphere potential source areas (PSA: Patagonia, central western Argentina, Puna-Altiplano, southern Africa, Australia, New Zealand, Antarctica) between 33.7 and 2.9 kyr BP. Of 294 samples, 279 were unmixed against a database of 217 UCC-normalised source patterns using 13 REE (Gd removed), with 2000 Monte Carlo runs per sample; 241 samples with a correlation R of at least 0.67 form the record (Table S1), and period means are given in Table S5. Patagonia supplies 65.7 to 74.8 % of the dust in MIS3, LGM and HS1 and 49.0 % in the Holocene, while Australia rises from 10.2 % (LGM) to 23.1 % (Holocene). The authors place a provenance shift at about 14.5 kyr BP and attribute it to the flooding of the Patagonian shelf and the reorganisation of Patagonian rivers. The results are checked by forward calculation of Sr and Nd isotopes against measured ice core values (Fig. 2, Table S4) and compared with the earlier EDML record of the same group (Fig. 4, Fig. S5).

## Strengths

1. The supplement publishes the per-sample median contributions of all 241 retained samples (Table S1) and the full source database with 13 element values per pattern (Table S2), so every period mean of Table S5 can be recomputed from Table S1 to within 0.05 percentage points and the database can be counted row by row; this transparency is what allowed the arithmetic checks in PP-11, PP-28 and PP-30.
2. The fit criterion and the sample bookkeeping are stated explicitly and applied uniformly (294 minus 15 equals 279, minus 38 equals 241; mean R 0.852 reproduced), and the exclusions and the sampling gap between 21.7 and 27.3 kyr BP are disclosed with their cause, so the path from dataset to record is traceable (PP-09, PP-26, PP-27).
3. The validation design confronts the REE-based contributions with a second tracer by forward calculation of 87Sr/86Sr and εNd (Eq. 3 and 4); recomputed from Table S3 and the period means, the modelled values (Holocene 0.7101 and -4.99, LGM 0.7083 and -2.61) lie close to the EDC values quoted in the text, so the check is feasible in principle, although the comparison actually shown has the limits set out in GB-34 (PP-45).
4. Figures 1, 3 (LGM panel) and 4 are drawn from the tabulated data: measured box statistics, bar heights, smoothed extremes and the shaded period boundaries agree with Table S1 and Table S5 within the measurement uncertainty, so the plotted values of these panels can be relied on (PP-38, PP-39, PP-41, PP-55).

## Weaknesses

1. The record is compositional, but several central statements read it as absolute or as demonstrated mechanism: the rise of low-latitude shares is interpreted as amplified emissions although the total flux falls by up to a factor of 25 and the announced PSA fluxes are not shown, the shift is placed as a step at about 14.5 kyr BP although Table S1 shows a progressive change, and shelf flooding is said to be demonstrated and confirmed although no mechanism is tested; the authors should report PSA fluxes with uncertainties, word the low-latitude change in relative terms where fluxes do not rise, date the change from Table S1 with an uncertainty and present the mechanism as consistent rather than demonstrated (GB-17, GB-33, GB-47, GB-50).
2. The robustness of the unmixing itself is not shown: there is no recovery test for 217 unknowns and 13 equations, the Monte Carlo spread is never reported although the Holocene variability is interpreted as a signal, the 38 excluded samples all fall after 14 kyr BP (22.8 % of that part of the record), the R threshold does not follow from the stated test and three samples below it are retained, and the conversion of coefficients into percent of dust is not described; the authors should add a synthetic recovery test, percentiles of the Monte Carlo distributions and a sensitivity analysis of the threshold and the exclusions (GB-14, GB-15, GB-16, GB-18, GB-20).
3. The two external checks are not made on the basis the text claims: the isotopic agreement "measured in EDC" rests for the Holocene on Taylor Glacier and Berkner Island values, the EDML values in Table S5 differ from those published in the cited 2023 study and come from a different model configuration, the Holocene differences of Section 4.4 use mismatched windows and the ACR and YD differences are reversed, and the Puna and Altiplano statements contradict Table S1; the authors should plot EDC Holocene isotopes, rerun EDML with the present configuration, recompute Fig. 4 on matched windows and rewrite the subregional statements from Table S1 (GB-24, GB-34, GB-44, GB-45).
4. Reproducibility and the reporting of sources need repair: the code and several inputs (EDC REE data, correction factors, excluded samples, sub-basin results) are not available despite the data statement, six works that supply 117 of the 217 source patterns and 32 of 35 ice core isotope values are missing from the reference list, Table S2 differs from the Methods in its counts and holds two duplicated patterns, six new source samples are undescribed, and several cited studies are reported inaccurately; the authors should deposit code and inputs, complete the reference list, correct Table S2 and check each literature value against its source (GB-03, GB-06, GB-07, GB-10, GB-12, GB-38).

## Findings by segment

### Segment 1: Title, Abstract, Introduction (p. 1 to 3)

#### Substantive findings

**GB-01 The priority claims are not backed by a described literature search, and the manuscript itself cites earlier quantitative source apportionments for East Antarctic dust.**

| Field | Content |
|---|---|
| Check | P28 |
| Location | p. 1, l. 17 to 20; p. 3, l. 74 to 76; p. 7, l. 220 to 221; p. 12, l. 403 to 404; p. 14, l. 472 to 473 |
| Quotation | "Using a statistical unmixing algorithm on 241 samples, we quantify for the first-time contributions from key Southern Hemisphere dust sources." |
| Concern | Further claims read "we presented the first quantitative apportionment algorithm based on REE pattern fitting" (p. 3, l. 74 to 75), "we present the first continuous and quantitative record of dust provenance" (p. 7, l. 220) and "The only continuous and quantitative dust provenance record in EA available for direct comparison" (p. 12, l. 403). No databases, search terms or search dates are given. The abstract claim is broader than the evidence: the manuscript itself reports that Coppo et al. (2022) "estimated LGM dust composition over EA as 64% from SSA, 15% from Antarctica, 11% from AUS, 5% from SAF, and 5% from NZ" (p. 9, l. 277 to 279), and the abstract of Coppo et al. (2022) confirms an unmixing of Nd, Sr and Pb isotope signals. Longman et al. (2022) quantified Southern Hemisphere dust source shares with Bayesian mixing models for the LGM and the Holocene. Contributions from key Southern Hemisphere sources have thus been quantified before with other tracers and archives; what is new is narrower, a continuous, sample-resolved, REE-based apportionment at EDC. Two searches found no earlier REE-pattern apportionment in ice cores (PP-06), but the claim still lacks a stated search basis. The overstatement concerns the positioning of the contribution, not the results. |
| Suggestion | Rephrase p. 1, l. 19 to 20 to the narrower claim (for example "we provide the first continuous, sample-resolved REE-based quantification of Southern Hemisphere dust source contributions at EDC") and qualify p. 7, l. 220 and p. 14, l. 472 accordingly; after p. 3, l. 76, name the earlier isotope-based apportionments (Coppo et al., 2022; Longman, J., Struve, T., Pahnke, K., 2022. Spatial and temporal trends in mineral dust provenance in the South Pacific: evidence from mixing models. Paleoceanography and Paleoclimatology 37, e2021PA004356, https://doi.org/10.1029/2021PA004356) and state how the present record differs. |
| Status | verified (no search described; Coppo et al. 2022 cited with quantitative shares; abstracts of Coppo et al. 2022 and Longman et al. 2022 read) |
| Severity | moderate |
| Source | S1 |

**GB-02 The age span of the record is given with four different end points.**

| Field | Content |
|---|---|
| Check | P2 |
| Location | p. 1, l. 18; p. 3, l. 90 to 91; p. 4, l. 109 to 110; p. 6, l. 182; p. 6, l. 187; p. 9, l. 303 to 304 |
| Quotation | "from 33.6 kyr to 2.8 kyr BP" |
| Concern | The Abstract (l. 18) and l. 182 give "33.7 to 2.9 kyr BP", which matches the first and last rows of Table S1 (33699 and 2852 yr BP, as stated in l. 109 to 110). The Introduction gives "from 33.6 kyr to 2.8 kyr BP" (l. 90 to 91), the Holocene is defined as ending at 2.8 kyr BP (l. 187, Table S5), which is a period limit, not the youngest sample, and l. 304 has "until 2.7 kyr BP", which matches neither. |
| Suggestion | Use "33.7 to 2.9 kyr BP" for the record in p. 3, l. 90 to 91 and "2.9 kyr BP" (or 2.8 kyr BP as the period limit) in p. 9, l. 304. |
| Status | verified |
| Severity | minor |
| Source | S3, SD |

**GB-03 The modelled CO2 drawdown of "~20 to 40 ppmv" is not supported by the two cited studies, which give about 20 ppm and 12 to 29 ppmv.**

| Field | Content |
|---|---|
| Check | P13 |
| Location | p. 2, l. 40 to 42 |
| Quotation | "Enhanced iron delivery by atmospheric dust during glacial periods are modelled to have lowered the atmospheric pCO2 by ~20 to 40 ppmv, accounting for a significant portion of the glacial-interglacial pCO2 difference (Lambert et al., 2015; Lambert et al., 2021)." |
| Concern | Lambert et al. (2015) conclude that iron fertilization reduced LGM atmospheric CO2 by about 20 ppm (less than 10 ppm on centennial and a further about 10 ppm on millennial time scales); the 40 % figure in that paper is the share earlier studies assigned to iron fertilization, not its own result. Lambert et al. (2021) give "between 12 and 29 ppmv" for global iron fertilization and speak of about one quarter of the glacial-interglacial difference. The upper bound of 40 ppmv exceeds the highest value in either source by 11 ppmv (40 minus 29). As shares of the 80 ppmv glacial-interglacial rise: 20 ppmv is 25 %, 29 ppmv is 36 %, 40 ppmv is 50 % (Python). The cited range doubles the share that the sources attribute to dust. |
| Suggestion | Replace "~20 to 40 ppmv" in p. 2, l. 41 by "~12 to 29 ppmv (about one quarter of the glacial-interglacial difference)" or cite a source for the upper bound. |
| Status | verified (both sources read: Lambert et al. 2015 full text, Lambert et al. 2021 open access); inferred (shares) |
| Severity | moderate |
| Source | S1 |

**GB-04 The factor "up to 25 times lower" is attributed to Delmonte et al. (2008, 2017), whose abstracts do not give it; the 25-fold figure appears in Lambert et al. (2008).**

| Field | Content |
|---|---|
| Check | P13 |
| Location | p. 2, l. 62 to 63 |
| Quotation | "dust fluxes are up to 25 times lower than LGM fluxes (e.g. Delmonte et al., 2008; Delmonte et al., 2017)." |
| Concern | The abstract of Lambert et al. (2008), cited in p. 2, l. 36 and l. 46, reports a 25-fold increase in glacial dust flux at EDC. The abstracts of Delmonte et al. (2008) (Sr and Nd provenance in glacial stages) and Delmonte et al. (2017) (dust size at Dome B in MIS 2) contain no glacial to interglacial flux ratio. Their full texts were not accessible, so they may repeat the figure. Do the authors mean Lambert et al. (2008)? |
| Suggestion | Cite Lambert et al. (2008) for the 25-fold figure in p. 2, l. 63, or give the page in Delmonte et al. (2008, 2017) where it appears. |
| Status | verified (abstracts of Lambert et al. 2008 and Delmonte et al. 2008, 2017); inferred (absence in the Delmonte full texts) |
| Severity | minor |
| Source | S1 |

**GB-05 The key term LGIT denotes two different time spans.**

| Field | Content |
|---|---|
| Check | P38, P15 |
| Location | p. 3, l. 90 to 91; p. 7, l. 220 to 221; p. 9, l. 300 to 302; p. 14, l. 472 to 473 |
| Quotation | "a system that maintained a remarkably stable provenance pattern until the onset of the LGIT" |
| Concern | The title, the four aims and l. 90 to 91 ("during the LGIT from 33.6 kyr to 2.8 kyr BP") and l. 221 ("spanning the entire LGIT") equate the LGIT with the whole record from the end of MIS3 to the late Holocene. In l. 301 to 302 the same abbreviation marks a point in time after the stable glacial regime, about 14.5 kyr BP, so that MIS3, LGM and HS1 lie before "the onset of the LGIT". A reader cannot tell whether statements such as "atmospheric dust deposition across East Antarctica during the LGIT was relatively uniform" (p. 12, l. 410 to 411) include the LGM. |
| Suggestion | Define LGIT once with explicit age limits (Section 1 or 2) and rephrase p. 9, l. 302 as "until ~14.5 kyr BP" or "until the onset of the ACR"; use "the study interval" where the whole record is meant. |
| Status | verified |
| Severity | minor |
| Source | S2, S4 |

#### Minor corrections

| ID | Location | Quotation | Replacement | Source |
|---|---|---|---|---|
| KK-01 | p. 1, l. 15 | "Dust deposits in ice cores provides a valuable archive" | "Dust deposits in ice cores provide a valuable archive" | ZF |
| KK-02 | p. 1, l. 20 | "During the Marine isotope 3 (MIS3)" | "During Marine Isotope Stage 3 (MIS3)" | S2 |
| KK-03 | p. 3, l. 73 | "achieved multi-decadal resolution" | "achieved decadal to centennial resolution" (Gabrielli et al., 2010: sample spacing about 60 years in the Holocene and 140 years in the last glacial; Wegner et al., 2012: decadal to centennial resolution) | S1 |

#### Verification log

| ID | Check | Checked | Values | Result |
|---|---|---|---|---|
| PP-01 | P13 | p. 2, l. 34 to 36 and l. 44 to 46, Lambert et al. (2008): dust records, control of deposition by source location and residence time | Abstract: 25-fold increase in glacial dust flux; causes stated tentatively ("may reflect" a strengthening of South American sources and longer particle lifetimes) | no finding; the source is tentative, the manuscript affirmative ("primarily influenced"), which does not change the statement |
| PP-02 | P13 | p. 3, l. 72 to 74, Gabrielli et al. (2010) and Wegner et al. (2012) "could not fully resolve dust provenance" | Gabrielli 2010: 294 samples, 2.9 to 33.7 kyr BP, no major PSA excluded; Wegner 2012: South America dominant before 15 kyr BP, Australia and New Zealand relatively more important after | no finding on provenance; resolution wording in KK-03 |
| PP-03 | P13 | p. 3, l. 76 to 87, summary of Vanderstraeten et al. (2023) | Abstract: PAT about 68 % before 14.5 kyr BP, below 50 % on average after, SAF 21 to 23 %, AUS 13 to 21 %; Early Holocene PAT about 50 %; shift linked to Patagonian river hydrology and shelf submersion | no finding for the Introduction text; conflict with Table S5 in GB-44; full text not accessible |
| PP-04 | P13 | p. 3, l. 92 to 93, "no consensus" on Holocene provenance (Paleari et al., 2019; Coppo et al., 2022; Delmonte et al., 2007) | Coppo 2022 abstract: Holocene East Antarctic Plateau records suggest a combined contribution from southern South America and Australia; Paleari 2019 (via Lanci et al., 2020): South America primary in glacial and interglacial stages | no finding; Paleari 2019 and Delmonte 2007 not read directly |
| PP-05 | P10 | Research gaps against aims, chain from framework to result | gaps: PSA emissions (p. 2, l. 43 to 44), Holocene without consensus (l. 92), isotope limits (l. 60 to 67); aims 1 to 4 each with instrument (DEPOT, forward isotope calculation, comparison with proxies, period means) and result topic (Fig. 1, Fig. 2, Fig. 5, Fig. 4) | aims 1 to 4 have instruments and result topics; iron fertilization framing without successor in GB-53; design limits in GB-34, GB-44, GB-47 |
| PP-06 | P14, P28 | Literature searches for work preceding or contradicting the contribution (six P14 queries on Taylor Glacier, Holocene EDC provenance, Patagonian shelf flooding, Talos Dome, isotope unmixing, South Pacific mixing models; two P28 queries on REE mixing models in ice cores) | Candidates: Aarons et al. 2017 (not in list, GB-10); Longman et al. 2022 (not in list, GB-01); Lanci et al. 2020 (no quantitative provenance); Delmonte et al. 2020, Revel-Rolland et al. 2006, Sugden et al. 2009, Gili et al. 2022, Koffman et al. 2021 (in list); no earlier REE-pattern apportionment in ice cores found | findings GB-01 and GB-10; no further proposal |

### Segment 2: Materials and methods (p. 3 to 5)

#### Substantive findings

**GB-06 Six source patterns are attributed to "this study", although the Methods describe the database as literature data and describe no sampling or analysis; their location labels and coordinates are inconsistent.**

| Field | Content |
|---|---|
| Check | P12, P8, P38 |
| Location | p. 4, l. 104 to 105 and l. 126 to 128; Supplement p. 17, Table S2, rows EtoshaL1, EtoshaL2, EtoshaL3, EtoshaL4, SuksesL, Sossusvlei, columns Reference, Location, Lattitude, Longitude |
| Quotation | "The fit between the REE patterns measured in the EDC ice core and literature reported patterns from known potential source areas (PSA)" |
| Concern | The values of the six patterns are in Table S2, so the data as such are available. Their origin is not described: Section 2 speaks only of literature patterns and of a compiled database and nowhere states that new source samples were collected, sieved to the fraction "< 5 µm" given in Table S2, digested and measured, with which instrument, blank correction or uncertainty. Six of the 23 SAF patterns are concerned, four of them representing Etosha Pan, one of the three SAF systems discussed in Section 4.3 (p. 11, l. 379 to 381). The location entries are inconsistent: all six are labelled "Etosha Pan", but SuksesL lies at 21.059 S and Sossusvlei at 24.76 S, while the three Etosha samples of Li et al. (2020) lie near 18.9 to 19.0 S; the sample name "Sossusvlei" and the location "Etosha Pan" name two places. All six rows give western longitudes ("W"), whereas the Li et al. Etosha rows at nearly the same longitude give "E". Because the SAF subregion contributions (Fig. S3) depend on how each pattern is assigned, the labels matter for Section 4.3. Who made the measurements is addressed in GB-54. |
| Suggestion | Add a paragraph after p. 4, l. 133 that identifies the six patterns as new data and describes sampling sites, size separation, digestion, instrument and quality control, or cite their first publication; correct the Location column for SuksesL and Sossusvlei, change "W" to "E" for the six rows, and state in the caption of Fig. S3 to which subregion each was assigned. |
| Status | verified (Methods wording; labels and coordinates on the page image, Supplement p. 17); whether the samples were published elsewhere could not be established from the manuscript |
| Severity | moderate |
| Source | S2, SD |

**GB-07 The code and data statement claims that all data are in the paper or supplement, but the DEPOT code and several inputs and intermediate results named in the Methods are not provided.**

| Field | Content |
|---|---|
| Check | P12, P34, P35 |
| Location | p. 4, l. 107 to 109, l. 113 to 114, l. 118 to 124; p. 5, l. 139 to 140, l. 155 to 164; p. 6, l. 174 to 175, l. 196 to 197; p. 11, l. 366; p. 16, l. 494 to 496 |
| Quotation | "All data needed to evaluate the conclusions in the paper are present in the paper and/or the Supplementary Materials. Additional data related to the paper may be requested from the authors." |
| Concern | The supplement gives the source database (Table S2), the median contributions of the retained samples (Table S1) and period means (Table S5), which allows a partial check. Not provided and not addressed are: (1) the REE concentrations of the 294 EDC samples "originally published by Gabrielli et al. (2010)" (l. 108), with no repository named; (2) the element specific correction factors cfi and their variability (l. 118 to 124, l. 157 to 158), which enter every fit and every Monte Carlo run; (3) the element specific analytical uncertainties, given only as a range of 2 to 10 % (l. 155 to 156); (4) the identity of the 15 samples excluded for missing data (l. 113 to 114) and of the 38 samples excluded by the R threshold (l. 174 to 175); (5) contributions below PSA level on which statements rest: the three Valdes Peninsula patterns are not named (l. 196 to 197) and "our model identifies the Darling sub-basin as the dominant source region" (l. 366) has no table or figure (Fig. S3 covers only Puna-Altiplano and SAF subregions); (6) the MATLAB code of the fit, the Monte Carlo propagation and the aggregation, the MATLAB version, solver tolerance and random seed (l. 139 to 140); (7) a number for the statement that 5000 runs "does not significantly affect the results" (l. 163 to 164). The section is headed "CODE/DATA AVAILABILITY" but says nothing on code. No reason is given why the remaining data are available only on request. The Monte Carlo spread is treated in GB-16, the PSA fluxes in GB-17. |
| Suggestion | Revise p. 16, l. 494 to 496 to list each input with its location; deposit in a public repository with DOI the EDC REE concentrations used (or cite the existing archive), cfi with uncertainties, per-element analytical uncertainties, the list of excluded samples with reason, per-sample DS-level contributions for all fitted samples, and the DEPOT code with version and solver settings; report the 2000 versus 5000 comparison numerically in p. 5, l. 164. |
| Status | verified (absence in manuscript and supplement); inferred (that no public archive of the 294 EDC REE patterns exists; the search was inconclusive) |
| Severity | moderate |
| Source | S2, SD |

**GB-08 The stated sample spacing of 60 to 140 years contradicts Table S1, in which four ages occur twice with different compositions.**

| Field | Content |
|---|---|
| Check | P6, P2, P38 |
| Location | p. 4, l. 110 to 113; Supplement p. 11, Table S1, rows 3559 (two rows); Supplement p. 13, rows 10511 and 12841 (two rows each); Supplement p. 14, rows 28709 (two rows) |
| Quotation | "with an average temporal resolution of approximately 100 years, ranging from 60 to 140 years between adjacent samples" |
| Concern | Two lines later the paragraph states a gap from 21.7 to 27.3 kyr BP with four samples. In Table S1 the spacings between retained samples run from 0 to 2280 years (23104 to 25384 yr). Exclusion can only widen spacings, yet in the part older than 14 kyr BP, where no sample was excluded, eight spacings lie below 60 years (31 to 58 yr) and one is 0 years. The cited source gives a typical spacing of about 60 years in the Holocene and about 140 years in the glacial (Gabrielli et al., 2010, p. 265), not a range. Table S1 identifies each sample only by its age, and four ages (3559, 10511, 12841, 28709 yr) occur twice with different contributions, for example 3559 yr with PAT 86.7 and AUS 12.8 in one row and PAT 0.0, Altiplano 32.9, AUS 49.8 and NZ 17.3 in the other (Python). Either an age is mistyped, two samples share one age, or one sample appears twice. The rows cannot be matched to the dataset of Gabrielli et al. (2010), and the 9-step moving average of Fig. 1 and Fig. 5 averages over very different time spans. If the pairs are replicates, they measure the single-sample reproducibility (GB-16). |
| Suggestion | Replace p. 4, l. 110 to 111 by the spacing statistics of the retained samples (median and range) with the period-typical values of the source; add sample depth or the original sample code as a column of Table S1; check and correct the eight duplicated rows and state what they are. |
| Status | verified (wording, Table S1 values on the page images, source wording); inferred (spacing statistics by Python) |
| Severity | moderate |
| Source | S2, S3, SD |

**GB-09 Samples are dated on EDC3, the period limits come from another chronology, and the assignment of samples near the limits is not tested.**

| Field | Content |
|---|---|
| Check | P9 |
| Location | p. 4, l. 111; p. 6, l. 184 to 188; p. 13, l. 445 to p. 14, l. 453 |
| Quotation | "The age model follows the EDC3 chronology (Parrenin et al., 2007)." |
| Concern | The period limits are taken from Veres et al. (2013) (l. 188), whose title names the AICC2012 chronology, while the samples are on EDC3. Within 200 years of the limits lie 2 samples (11.7 kyr), 5 (12.9 kyr), 3 (14.7 kyr) and 4 (18 kyr) (Python, Table S1); with 8 ACR and 9 YD samples, a shift of a few samples changes those means. The synchrony with Meltwater Pulse 1A and the Bølling onset (l. 450 to 453) is also stated across chronologies without uncertainty. Question to the authors: were the limits transferred to EDC3, and how large is the offset between the chronologies in this interval? |
| Suggestion | State in p. 4, l. 111 and p. 6, l. 184 to 188 the chronology of the limits, place limits and samples on one chronology, report the period means with limits shifted by the chronological uncertainty, and give an age uncertainty for the shift at about 14.5 kyr BP. |
| Status | verified (two chronologies named); inferred (counts by Python); assumption (size of the offset), posed as a question |
| Severity | moderate |
| Source | SD |

**GB-10 Six works that supply 117 of the 217 source patterns and 32 of the 35 measured ice core isotope values are missing from the reference list; one of them, Aarons et al. (2017), is also directly relevant to the Holocene provenance argument.**

| Field | Content |
|---|---|
| Check | P12, P4, P14 |
| Location | p. 4, l. 126 to 128; Supplement pp. 17 to 19, Table S2, column Reference; Supplement p. 21, Table S4, column Reference; p. 10, l. 329 to 334; reference list p. 16, l. 502 to p. 22, l. 846 |
| Quotation | "Marx and Kamber, 2010" |
| Concern | Section 2 states that the PSA patterns are literature data, so their publications are data sources. Table S2 cites "Marx and Kamber, 2010" (101 patterns), "Marx et al. , 2005" (10 patterns), "McGowan et al ., 2005" (2) and "Diaz et al. , 2018" (4), together 117 of 217 patterns including all Australian ones; Table S4 cites "[Aarons et al. (2017)]" (18 values) and "[Bory et al. (2010)]" (14 values), which form the open symbols of Fig. 2 (counts by Python from the extracted tables). None of these six works is in the reference list, and the supplement has no list of its own. Aarons et al. (2017) also present a Sr, Nd and REE record of Taylor Glacier dust across the deglaciation and attribute early Holocene dust to a combination of local Ross Sea sources and southern South America; this bears on the statement "our results do not indicate significant Antarctic contributions to EDC" (p. 10, l. 330), even though Taylor Glacier is a coastal site. A search found the McMurdo aeolian REE data published as Diaz et al. (2020); the year 2018 should be checked. |
| Suggestion | Add full entries with DOI for Aarons et al. (2017), Bory et al. (2010), Diaz et al. (2018 or 2020), Marx et al. (2005), Marx and Kamber (2010) and McGowan et al. (2005) to the reference list (or a list to the supplement); name Aarons et al. (2017) and Bory et al. (2010) in the caption of Fig. 2; after p. 10, l. 334 discuss the Holocene attribution of Aarons, S.M. et al., 2017. Dust composition changes from Taylor Glacier (East Antarctica) during the last glacial-interglacial transition: a multi-proxy approach. Quaternary Science Reviews 162, 60-71, https://doi.org/10.1016/j.quascirev.2017.03.011, and why EDC differs. |
| Status | verified (absence from the list on pp. 16 to 22; Aarons et al. 2017 read as open access PDF); inferred (row counts from the extracted tables) |
| Severity | moderate |
| Source | S1, S2, S4 |

**GB-11 "PSA" is used both for the seven source regions and for the 217 individual source patterns.**

| Field | Content |
|---|---|
| Check | P38 |
| Location | p. 4, l. 129 and l. 136 to 137; p. 2, l. 44; p. 5, l. 143 to 144; Supplement p. 11, Table S1 caption; Supplement p. 16, Table S2 title |
| Quotation | "modeled as a linear combination of PSA end-members" |
| Concern | The text defines PSA as a source area ("Potential Source Areas (PSAs)", l. 44) and DS as one of the 217 source patterns ("PAT; 39 dust sources, DS", l. 129), and results are aggregated by PSA. Table S1 nevertheless speaks of "217 PSAs", Table S2 of a "PSAs database", and l. 136 to 137 calls the columns of Eq. (2) PSA end-members, whereas Eq. (2) has one column per DS. Since contributions are computed per DS and summed per PSA, the two levels must be kept apart. |
| Suggestion | Use "DS" for the 217 patterns throughout: "a linear combination of DS end-members" (p. 4, l. 136 to 137), "using 217 DS" (Table S1 caption), "Table of the DS database" (Table S2 title). |
| Status | verified |
| Severity | minor |
| Source | S2 |

**GB-12 Table S2 does not reproduce the database as described: it holds 107 Australian and 4 Antarctic patterns instead of 106 and 5, and two Australian patterns appear twice under a Darling Basin and a Murray Basin name.**

| Field | Content |
|---|---|
| Check | P12, P23, P38 |
| Location | p. 4, l. 131 to 133; p. 11, l. 366 to 367; Supplement p. 17, Table S2, rows Darling26 and Darling29; Supplement p. 18, rows Murray24 and Murray29; Supplement p. 19, section Antarctica (ANT) |
| Quotation | "Australia (AUS; 106 DS, predominantly from the central and southeastern regions)" |
| Concern | Counting the rows of Table S2 gives PAT 39, CWA 5, PAP 14, SAF 23, AUS 107, NZ 25, ANT 4, total 217 (Python); the Methods give AUS 106 and "ANT; 5 DS from the McMurdo Dry Valleys", also 217. The totals agree only because one row too many and one too few cancel. The ANT block holds four rows (ELB, Expcove, Miers, Vict, page image), while the ANT inset of Fig. S1 shows five markers. In addition, Darling26 and Murray29 have identical coordinates (34° 3'0.00"S 142° 3'10.80"E) and identical values in all 13 element columns, and so do Darling29 and Murray24 (34°28'48.00"S 142°49'48.00"E), so Table S2 holds 215 distinct patterns. Eq. (2) thus contains two pairs of identical columns, the split between the members of each pair is not determined by the data, and contributions can be assigned to the Darling or the Murray Basin arbitrarily, which bears on "our model identifies the Darling sub-basin as the dominant source region during the Holocene" (l. 366 to 367). PSA-level results are not affected, since both members of each pair are AUS. |
| Suggestion | Reconcile Table S2 with p. 4, l. 131 to 133 (add the missing ANT pattern or correct the counts), remove the duplicated rows, assign each sample to its basin, rerun the fits, state the number of distinct patterns used, and check whether the Darling attribution in p. 11, l. 366 survives. |
| Status | verified (rows and coordinates on the page images, Supplement pp. 17 to 19; counts and identity of values by Python) |
| Severity | moderate |
| Source | S2, S3, SD |

**GB-13 Source patterns enter the unmixing without a described quality check, and two cases in Table S2 look anomalous.**

| Field | Content |
|---|---|
| Check | P27 |
| Location | p. 4, l. 133 to 135; Supplement p. 17, Table S2, row Kuiseb2inf5, column Dy; Supplement p. 19, Table S2, rows ELB, Expcove, Miers, Vict; p. 10, l. 329 to 331 |
| Quotation | "our results do not indicate significant Antarctic contributions to EDC" |
| Concern | In Kuiseb2inf5 Dy is 6.200013 while Tb is 2.692922 and Ho 2.149792, and the sister sample Kuiseb1inf5 has Dy 2.376464. The four ANT patterns span a factor of about 100 to 170 within one pattern (ELB: Ce 1.414516, Tm 0.008484), unlike all other groups, which are smooth after UCC normalisation (l. 133 to 134). Such patterns can either never fit or fit spuriously, and the ANT result (negligible, against 15 % for Antarctica in Coppo et al. (2022), l. 278) depends on them. Question to the authors: were the values checked against the original publications for units and normalisation? |
| Suggestion | Describe after p. 4, l. 135 a quality check of the PSA database (comparison with source tables, outlier screening), correct or remove anomalous entries, and report whether the ANT and SAF results change. |
| Status | verified (values on the page images, Supplement pp. 17 and 19); assumption (that the values are erroneous), posed as a question |
| Severity | moderate |
| Source | SD |

**GB-14 The ability of the 217-pattern, 13-element configuration to recover known mixtures is asserted, not tested.**

| Field | Content |
|---|---|
| Check | P31 |
| Location | p. 5, l. 142 to 149; p. 3, l. 75 to 76; p. 5, l. 171 to 172; p. 8, l. 258 to 259 |
| Quotation | "capable of disentangling contributions from multiple dust sources across the Southern Hemisphere (Vanderstraeten et al., 2023)" |
| Concern | The system has 13 equations (UCC-normalised REE without Gd) and 217 unknowns (l. 142 to 145). The evidence offered for discrimination is the R of the fit (l. 171 to 172) and the qualitative isotope agreement (l. 258 to 259); neither shows that the algorithm returns the right PSA proportions. The 2023 configuration differed (14 REE; 207 patterns according to the abstract of Vanderstraeten et al., 2023), so a test there does not carry over. The Introduction criticises isotopes for failing "when the isotopic fields overlap" (p. 2, l. 64 to 65); the equivalent overlap of REE patterns between PSAs is not assessed. Question to the authors: with more unknowns than equations, is the minimiser unique, or can different PSA combinations give the same residual, so that the returned solution depends on the solver? The severity is major because every reported contribution depends on this ability. |
| Suggestion | Add after p. 5, l. 152 a recovery test: synthetic mixtures of held-out patterns with known proportions and noise at Holocene and glacial concentration levels, unmixed with the exact configuration used here; report the recovery error per PSA and the false attribution rate, and how often the Monte Carlo runs change the set of non-zero sources. |
| Status | verified (absence of a recovery test; dimensions; database size in the source abstract); assumption (non-uniqueness), posed as a question |
| Severity | major |
| Source | SD |

**GB-15 How the 217 coefficients become percent of dust mass is not stated, and one row of Table S1 sums to 93.5 %.**

| Field | Content |
|---|---|
| Check | P8, P1 |
| Location | p. 5, l. 146 to 147; p. 5, l. 160; Supplement p. 16, Table S2, rows PataGi7 and PataGi10, column La; Supplement p. 13, Table S1, first row 10511 |
| Quotation | "The vector of 217 components represents the proportional contribution of each DS required to best approximate the REE signature" |
| Concern | Eq. (2) fits UCC-normalised patterns with free non-negative coefficients; no sum-to-one constraint is stated, and the units of the DIC vector are not given. The source patterns differ in level (La 0.073 for PataGi7, 1.103 for PataGi10, factor 15), so a coefficient equals a mass share only if the DIC pattern is expressed per mass of dust and the coefficients are normalised accordingly. In Table S1 all rows but one sum to 100.0 plus or minus 0.1; the first row 10511 reads 0.0, 0.0, 3.1, 6.7, 49.2, 29.5, 5.0, 0.0, which sums to 93.5 (Python). If medians are taken per PSA separately (l. 164 to 165), they need not sum to 100, which would explain the row but is not stated. The effect on the Early Holocene and Holocene means is at most 0.12 and 0.06 percentage points. Question to the authors: are the reported percentages normalised coefficients, concentration-weighted shares, or mass fractions? |
| Suggestion | State in p. 5, l. 142 to 152 the units of the DIC and DS vectors, whether a sum constraint or normalisation is applied, and the formula from CDS to percent of total deposition; note in the caption of Table S1 that per-PSA medians need not sum to 100 %, or correct the row. |
| Status | verified (missing description; Table S1 and S2 values on the page images); inferred (sum); assumption (effect on shares), posed as a question |
| Severity | moderate |
| Source | SD, S3 |

**GB-16 The Monte Carlo uncertainty is announced but not reported, while the larger Holocene variability is interpreted as an environmental signal.**

| Field | Content |
|---|---|
| Check | P11, P9 |
| Location | p. 5, l. 153 to 165; p. 9, l. 306 to 308; p. 6, l. 193 to 194; Fig. 1; Supplement pp. 11 to 15, Table S1; Supplement p. 22, Table S5 |
| Quotation | "During YD and throughout the Holocene, our unmixing model reveals a significantly larger variability in the dust assemblages reaching EDC as shown in Figure 1." |
| Concern | The propagation design (2000 runs per sample, cfi and Dusti drawn from normal distributions) is apt to separate signal from noise, but its spread is shown nowhere: Table S1 gives medians, Table S5 means of medians, and Fig. 1 has no uncertainty bands. Fit quality and variability change together: mean R is 0.799 in the Holocene against 0.912 to 0.924 in HS1, LGM and MIS3, the standard deviation of PAT across samples is 32.1 percentage points in the Holocene against 9.9 to 10.8, and 23 Holocene samples have PAT 0.0, none before 12.9 kyr BP (Python, Table S1). The duplicated ages of Table S1 (GB-08) give PAT 86.7 and 0.0 at 3559 yr and 0.0 and 38.2 at 10511 yr; if these are samples from the same depth, the single-sample reproducibility is of the size of the variability interpreted. The three explanations offered (l. 308 to 314) are all environmental; analytical noise at near-detection-limit concentrations (l. 176 to 177) and non-unique fits (GB-14) are not considered, although single-sample features (PAT minima, Altiplano peaks) carry the climate interpretation of Section 4.3. Without the spread, the reader also cannot judge whether period differences of a few percentage points, such as those in Section 4.4, exceed the model uncertainty. The severity is major because the Holocene interpretation of Section 4.3 (aim 3) would read differently if the variability lay within the model uncertainty. |
| Suggestion | Add the 16th and 84th percentiles of each PSA distribution to Table S1 and show them as bands in Fig. 1, give the propagated uncertainty of the period means in Table S5, test in Section 4.3 whether the between-sample variance exceeds the mean within-sample Monte Carlo variance per period, and interpret only features whose interval excludes the neighbouring values. |
| Status | verified (missing uncertainties; Table S1 values); inferred (mean R, standard deviations, counts by Python); assumption (that the duplicates are same-depth samples), posed as a question |
| Severity | major |
| Source | S3, SD |

**GB-17 Absolute PSA dust fluxes are announced in the Methods and Results but shown in no figure or table, and Table S1 is cited for interval summaries it does not contain.**

| Field | Content |
|---|---|
| Check | P11, P4, P3 |
| Location | p. 5, l. 165 to 167; p. 6, l. 183 to 184; Supplement p. 4, Fig. S2; Supplement p. 11, Table S1; Fig. 1 |
| Quotation | "to convert PSA contributions into absolute dust fluxes (Figure S2)" |
| Concern | Section 3 continues: "Figure 1 and Table S1 summarize the relative contributions (in % of total deposition and flux) from each PSA across major climatic intervals" (l. 183 to 184). Fig. S2 has three panels, total nssCa2+ flux, δ18O and deuterium excess; no panel shows fluxes per PSA. The five y axes of Fig. 1 read "Total Contribution (%)", and Table S1 lists per-sample median percentages, without fluxes and without interval means; the interval means are in Table S5. The conversion factor from nssCa2+ flux to total dust flux is not given. No reason is given for omitting the PSA fluxes, so a reader cannot check any statement that depends on them (see GB-47). |
| Suggestion | Add PSA fluxes (nssCa2+-based dust flux times contribution) per sample to Table S1 and per period to Table S5, or a panel to Fig. 1 or Fig. S2, with the conversion factor; correct p. 6, l. 183 to 184 to "Figure 1, Table S1 (per sample) and Table S5 (per interval)"; otherwise delete the flux statement in p. 5, l. 165 to 167 and "and flux" in p. 6, l. 184. |
| Status | verified (page images p. 5, 6, 24; Supplement p. 4, 11) |
| Severity | moderate |
| Source | S2, S3, S4, AB, SD |

**GB-18 The correlation threshold R ≥ 0.67 does not correspond to p below 0.01 for the stated or the correct degrees of freedom, and Table S1 retains three samples with R = 0.66.**

| Field | Content |
|---|---|
| Check | P1, P5, P2 |
| Location | p. 5, l. 170 to 172; p. 6, l. 174 to 175; Supplement p. 11, Table S1, rows 2888 and 3267, column R; Supplement p. 13, Table S1, first row 10511, column R |
| Quotation | "We determined that R ≥ 0.67 corresponds to a statistically significant match (p < 0.01, two-tailed test, degrees of freedom = 10)" |
| Concern | The criterion is clearly defined and applied uniformly. With 13 REE per pattern (l. 145) a Pearson correlation has 13 minus 2 = 11 degrees of freedom, not 10. Critical r for p = 0.01, two-tailed (scipy, t distribution): 0.708 for df 10, 0.684 for df 11, 0.661 for df 12; R = 0.67 gives p = 0.017 (df 10) or 0.012 (df 11). The value 0.67 matches p = 0.01 only for df 12, that is for 14 elements as in Vanderstraeten et al. (2023), which suggests the threshold was carried over. Of the 241 retained samples, 9 have R below 0.684 and 19 below 0.708, all in the part younger than 14 kyr. Table S1 also lists three samples with a printed R of 0.66 (2888 yr, 3267 yr, first row 10511 yr), below the threshold by which 38 samples "were excluded" (l. 174 to 175); a printed 0.66 lies below 0.665 under rounding and below 0.67 under truncation. Question to the authors: since the modelled pattern is fitted to the observed one and REE patterns are smooth across elements, is a significance test for independent pairs applicable at all? |
| Suggestion | Correct the derivation in p. 5, l. 170 to 172 (df 11, critical value), state whether the threshold applies to the median R and how rounding is treated, give R with three decimals in Table S1, remove or flag the three rows with R = 0.66, and report how the results change under the corrected threshold (see GB-20). |
| Status | verified (wording, df, Table S1 values on the page images); inferred (critical values and counts by Python); assumption (applicability of the test), posed as a question |
| Severity | moderate |
| Source | S3, SD |

**GB-19 Figure S1 is a low-resolution screenshot with unreadable labels in French.**

| Field | Content |
|---|---|
| Check | P3 |
| Location | Figure S1, Supplement p. 2 |
| Quotation | "(see Table S2 for details), © Google Earth Pro." |
| Concern | The main map image has 78 ppi; place names and scale bars are blurred, and the readable labels are French Google Earth labels ("Nouvelle-Zélande", "Argentine", "Territoire de la capitale australienne"). Marker positions cannot be checked against the coordinates of Table S2, which matters given the inconsistent coordinates in GB-06 and the marker count in GB-12. |
| Suggestion | Replace Fig. S1 by a map of at least 300 ppi with English labels, a coordinate grid and legible scale bars. |
| Status | verified |
| Severity | minor |
| Source | AB |

#### Minor corrections

| ID | Location | Quotation | Replacement | Source |
|---|---|---|---|---|
| KK-04 | p. 3, l. 101 | "ice core camples" | "ice core samples" | SD |
| KK-05 | p. 4, l. 127 | "(Figure S1, and Table S1)" | "(Figure S1 and Table S2)" | S2, S4 |
| KK-06 | p. 4, l. 128 | "subdivised into Patagonia" | "subdivided into Patagonia" | ZF |
| KK-07 | p. 5, l. 145 to 146 | "For any given time step. The vector of 217 components represents" | "For any given time step, the vector of 217 components represents" | ZF |
| KK-08 | p. 5, l. 159 | "by minimizing Eq. (1)" | "by minimizing Eq. (2)" | S2, S4, SD |
| KK-09 | Supplement p. 16, Table S2, group heading | "Puna AltiPlano (PAP)" | "Puna-Altiplano Plateau (PAP)" | S2 |
| KK-10 | Supplement p. 17, Table S2, rows Omarur1inf5 and Omarur2inf5 | "Omarur1inf5", "Omarur2inf5" | "Omaruru1inf5", "Omaruru2inf5" (as "Omaruru3inf5") | S2 |
| KK-11 | Supplement p. 17, Table S2, row Darling12, column Longitude | "138°17'6.00"E" | the longitude of the source sample; Darling11 at the same latitude (31° 2'49.20"S) has 144°17'6.00"E, and 138° E lies far west of all other Darling Basin rows | ZF |
| KK-12 | Supplement p. 18, Table S2, rows aust8 to aust13, column Location | "Murrumbigdee basin" | "Murrumbidgee basin" | S2 |

#### Verification log

| ID | Check | Checked | Values | Result |
|---|---|---|---|---|
| PP-07 | P12 | Inventory of the data sources named in Section 2 and their coverage by the statement in p. 16, l. 494 to 496, the supplement and the reference list | EDC REE concentrations (Gabrielli et al., 2010): cited, not provided; EDC3 age model (Parrenin et al., 2007): in list; UCC (Rudnick and Gao, 2003): in list; cfi: not provided; analytical uncertainties: range only; source database: Table S2; nssCa2+ flux (Fischer et al., 2007): in list, Fig. S2 A; code: not addressed; per-sample medians and R: Table S1 (241 rows); period means: Table S5 | findings GB-06, GB-07, GB-10, GB-12 |
| PP-08 | design sketch | Questions, study type, data sources, timeline, environment, principles, disclosed limits and the chain from framework to result over the whole manuscript and supplement | study type: modelling (NNLS) on a published observational dataset; 294 samples, 279 unmixed, 241 retained; 217 patterns; comparison data: Table S4, EDML record, DustCOMM, Coppo et al. (2022); no synthetic recovery test; one run configuration (2000 runs, check with 5000) | disclosed limits: sampling gap (p. 4, l. 113), 38 exclusions (p. 6, l. 174 to 179), ACR and YD tentative (p. 12, l. 407 to 409), SAF and AUS domains larger than shown (p. 26, l. 863) |
| PP-09 | P2 | Sampling gap and mean resolution | rows between 21.7 and 27.3 kyr: 22150, 23104, 25384, 25640 yr (l. 113: four samples); mean spacing of the 294 samples (33699 minus 2852) / 293 = 105.3 yr (l. 110: about 100) | no finding; range of spacings in GB-08 |
| PP-10 | P13 | p. 4, l. 118 to 124, correction factors cfi "as described in Gabrielli et al. (2010)" | Gabrielli 2010, Sect. 2.4 and Fig. 1a: acid-leached versus full-digestion mass fractions, LREE slightly overestimated; no correction factor defined or applied there | no finding under P13; availability of cfi in GB-07 |
| PP-11 | P12 | Completeness of Table S2 against p. 4, l. 128 to 133 for the regions without discrepancy; element columns against the removal of Gd | PAT 39 (TDFGi 3, PataGa 14, PataGi 22), CWA 5, PAP 14 (South Puna 7, North Puna 2, Southern Altiplano 5), SAF 23, NZ 25 (Marx et al. 6, Koffman et al. 19); 13 element columns (La to Lu without Gd), all 217 rows with 13 values | no finding for these regions and the element set |
| PP-12 | P23 | Dust source totals | text 39 + 5 + 14 + 23 + 106 + 25 + 5 = 217; Table S2 PAT, CWA, PAP, SAF and NZ match; REE 14 minus Gd = 13 (l. 145) | no finding for the totals; group sizes in GB-12 |
| PP-13 | P12 | Records used in Section 2 and in method figures: citation and presence in the reference list | Fischer et al. 2007, EPICA Community Members 2006, Stenni et al. 2010, Lisé-Pronovost et al. 2015, Vanderstraeten et al. 2023, Gili et al. 2017, Gaiero et al. 2004, Koffman et al. 2021, Li et al. 2020: all have entries | no finding |
| PP-14 | P38 | Names of ice cores | "EPICA Dome C" 6 lines, "EDC" 63 lines in the main text and 14 in the supplement, "EDML" consistent; "Old Dome C" (Basile et al., 1997) denotes the earlier Dome C core | no finding beyond KK-24 and KK-76 |
| PP-15 | P38 | Name of the algorithm | "DEPOT" defined l. 100, used l. 88, l. 259, captions of Fig. S1 and Table S1; descriptive variants (l. 19, l. 94, l. 142, l. 306) refer to the same algorithm; the difference to the 2023 version (n = 14 versus 13) is disclosed (l. 144 to 145) | no finding |
| PP-16 | P38 | Abbreviations of source regions | SSA, PAT, CWA, PAP, SAF, AUS, NZ, ANT consistent in text, Tables S1, S2, S5 and Fig. S1; "SCWA" in Table S3 denotes the southern part of CWA (rows SCWA1 to SCWA3) | no finding |
| PP-17 | P38 | Uniqueness of DS identifiers in Table S2 | 217 sample names, 217 distinct (Python) | no finding; duplicated content under different names in GB-12 |
| PP-18 | P32 | Claims "validating", "robust", "confirming" (l. 93, l. 172, l. 259) against an independent check of results | no recovery test, no replicate; Sr and Nd check qualitative | no separate finding; covered by GB-14 and GB-34 |
| PP-19 | P30 | Reported errors and corrections against reported runs | no error or correction reported | no finding |
| PP-20 | P37 | Transformed data in tables and figures: Gd removal, cfi correction, UCC normalisation, medians, 9-step moving average | Table S2 header "REE normalised on the Upper Continental Crust"; Table S1 caption "Median"; Fig. 1 caption "mobile average over 9 steps" | transformations are labelled; caption count in GB-21 |
| PP-21 | P33 | Effort statements | "tradeoff between computation cost and representativity" (l. 162 to 163); cost not used as result or limit | no finding; missing number for the 5000-run check in GB-07 |
| PP-22 | P18 | Principles declared by the manuscript applied to itself | data statement (l. 494 to 495); critique of isotopes for overlapping fields (l. 64 to 65) | not applied to itself; in GB-07 and GB-14 |
| PP-23 | P26 | Guarantee "physically meaningful (i.e., no negative values)" (l. 139) across single fit, Monte Carlo runs and PSA medians | no negative value in Table S1 (241 rows, 9 columns) | guarantee holds; closure question in GB-15 |
| PP-24 | P17 | Sampling gap and exclusions at the point of introduction | gap stated in Methods l. 113 where the dataset is introduced; exclusion stated in Results l. 174 to 179 directly after the threshold | no finding for these two; ACR and YD caveat in GB-46 |
| PP-25 | P25 | Information flow of each step: flux conversion, isotope calculation, period assignment | nssCa2+ flux available (l. 166); Table S3 end-members without ANT | missing ANT end-member in GB-36; otherwise no finding |

### Segment 3: Results (p. 6 to 7)

#### Substantive findings

**GB-20 All 38 samples removed for poor fit are younger than 14 kyr BP, so the Holocene and deglacial composition rests on an outcome-based selection whose effect is not assessed.**

| Field | Content |
|---|---|
| Check | P20, P9 |
| Location | p. 6, l. 174 to 182; p. 5, l. 168 to 172; Supplement pp. 11 to 13, Table S1 |
| Quotation | "These excluded samples are all younger than 14 kyr BP and have very low REE concentrations near the detection limit." |
| Concern | The exclusion and its cause are disclosed; the consequence is not drawn. The retention rate "For the remaining 241 DIC samples (86%)" (l. 179) is given against the whole record, in which no sample older than 14 kyr is excluded. Table S1 has 129 retained samples younger than 14 kyr, so 38 of 167 = 22.8 % of the post-14 kyr samples were excluded, against 0 % before (overall 38 of 279 = 13.6 %; Python). R measures how well the 217 patterns reproduce a sample, so the rule removes exactly the samples the database cannot explain, which can be noise or a source missing from the database. The Holocene means of Table S5 (PAT 49.0, AUS 23.1 %) and the Holocene record of aim 1 are computed from fit-able samples only, and if low-dust intervals have a different provenance, they are biased towards higher-dust intervals. The ages of the excluded samples are not listed, so clustering in particular intervals cannot be seen. Question to the authors: could the excluded patterns reflect sources not represented in the database? The severity is major because the Holocene composition, the core of aim 1, could change with the selection. |
| Suggestion | In p. 6, l. 174 to 179, report the exclusion rate per period, list the ages of the 38 excluded samples in the supplement, and add a sensitivity analysis: period means and Fig. 1 recomputed with all 279 samples, with the stated threshold and with the correctly derived threshold (GB-18). |
| Status | verified (statements, absence of exclusions before 14 kyr); inferred (rates by Python); assumption (missing sources), posed as a question |
| Severity | major |
| Source | S3, SD |

**GB-21 Table S1 is captioned as based on "279 DIC" but lists only the 241 retained samples.**

| Field | Content |
|---|---|
| Check | P2 |
| Location | p. 6, l. 179; Supplement p. 11, Table S1 caption |
| Quotation | "using 217 PSAs and 279 DIC from EDC ice core REE patterns." |
| Concern | Table S1 contains 241 data rows (first row 2852 yr, last 33699 yr), that is only the samples that passed the R threshold ("the remaining 241 DIC samples", l. 179), not the 279 treated samples; the 38 excluded samples appear nowhere. The use of "PSAs" for the 217 patterns is addressed in GB-11. |
| Suggestion | Change the caption of Table S1 to "using 217 dust sources (DS) and the 241 DIC samples with R ≥ 0.67 (of 279 treated)", and add the 38 excluded samples with their R values as a separate block. |
| Status | verified |
| Severity | minor |
| Source | S3, SD |

**GB-22 The stated order of the secondary PSAs (AUS, SAF, PAP, NZ) does not match the averages, in which NZ exceeds PAP.**

| Field | Content |
|---|---|
| Check | P2 |
| Location | p. 6, l. 201 to 202; Supplement pp. 11 to 15, Table S1; Supplement p. 22, Table S5 |
| Quotation | "Overall, other Southern Hemisphere PSAs contribute to EDC dust deposition with sources from: AUS, SAF, PAP and NZ, in decreasing order of importance." |
| Concern | Mean over all 241 samples (Table S1): AUS 16.51, SAF 9.17, NZ 7.85, PAP 6.85. Unweighted mean of the six periods of Table S5: NZ (9.1 + 14.2 + 7.1 + 6.6 + 3.3 + 5.9) / 6 = 7.7; PAP (2.2 + 3.6 + 2.0 + 5.2 + 4.5 + 11.0) / 6 = 4.75 (Python). Under both bases the order is AUS, SAF, NZ, PAP; only the Holocene alone gives PAP above NZ. |
| Suggestion | Write "AUS, SAF, NZ and PAP" in p. 6, l. 202, or restrict the statement to the Holocene. |
| Status | inferred (means by Python) |
| Severity | minor |
| Source | S3 |

**GB-23 The SAF level of "~2%" between 9.5 and 12 kyr BP has no stated basis and matches neither the mean, the median nor the moving average.**

| Field | Content |
|---|---|
| Check | P20 |
| Location | p. 6, l. 207 to p. 7, l. 208; Supplement pp. 12 to 13, Table S1, rows 9772 to 11993 |
| Quotation | "Although SAF input drops to minimal levels (~2%) between 9.5 and 12 kyr BP" |
| Concern | For the 33 rows from 9772 to 11993 yr: mean SAF 4.32 %, median 0.3 %; the centred 9-step moving average (as in Fig. 1) ranges from 0.8 to 12.8 % with a mean of 6.2 % (Python). Two samples (10278 yr: 40.3; 10511 yr: 49.2) carry most of the mean. |
| Suggestion | State in p. 7, l. 208 whether the value is a median, a mean or read from the moving average, and give the matching number. |
| Status | inferred (statistics by Python) |
| Severity | minor |
| Source | S3 |

**GB-24 The statements on Puna and Altiplano timing and magnitude contradict Table S1, Fig. 1 and Fig. S3, and the Altiplano onset tied to paleolake Coipasa is earlier than stated.**

| Field | Content |
|---|---|
| Check | P2, P3, P6 |
| Location | p. 7, l. 211 to 215; p. 11, l. 357 to 360; Fig. 1, panel PAP; Supplement p. 6, Fig. S3, panels Puna and Altiplano; Supplement pp. 11 to 13, Table S1, columns Puna and Altiplano |
| Quotation | "which even becomes dominant in several samples, contributing over 90% at 11.2, 10, 8.6, 6, and 3.5 kyr BP. In contrast, contributions of South Puna remained consistently below 20% during this interval (Figure 1)." |
| Concern | (a) "increasing to ~5% during the ACR and YD, primarily from the South Puna region" (l. 212): over the 9 YD rows mean Puna is 1.26 and mean Altiplano 3.27, so the YD input is mainly Altiplano (the ACR holds: Puna 5.23, Altiplano 0.0). (b) Altiplano exceeds 90 % in only two rows of Table S1, 8629 yr (100.0) and 11228 yr (97.0); at the other three ages the values are 75.7 (9957 yr), 58.5 (5967 yr) and 62.7 (3465 yr). The PAP panel of Fig. 1 shows exactly two raw-data peaks above 90 % (97.6 % at 8627 yr, 95.4 % at 11243 yr, measured). (c) Puna reaches 20 % or more in 8 Holocene rows (20.2 to 29.1 %, maximum 5850 yr), and the Puna panel of Fig. S3 shows 8 Holocene peaks above 20 %; Fig. 1 shows PAP as a whole and cannot show South Puna. (d) l. 357 to 358 state "the Southern Altiplano begins contributing dust only after approximately 11.2 kyr BP", but Table S1 gives Altiplano 16.6 and 12.8 % in the two YD rows at 12841 yr and 7.8 % at 11117 yr, and Fig. S3 shows 38.8 % at 11873 yr; the link to the final desiccation of paleolake Coipasa (l. 358 to 360), part of aim 3, rests on this onset. The severity is major because the Coipasa interpretation changes if the onset lies in the YD. |
| Suggestion | Rewrite p. 7, l. 211 to 215 and p. 11, l. 357 to 360 from Table S1 (Altiplano first in the YD, above 90 % only at 11.2 and 8.6 kyr BP, Puna up to 29 %), cite Fig. S3 instead of Fig. 1 for the subregions, state whether values refer to total deposition or to the PAP share, and discuss whether the Coipasa argument holds for a YD onset or treat the two YD samples (R 0.69 and 0.77) as uncertain with their Monte Carlo intervals. |
| Status | verified (Table S1 values on the page images; measured peaks in Fig. 1 and Fig. S3); inferred (period means by Python) |
| Severity | major |
| Source | S3, AB, SD |

**GB-25 Abbreviations and graphical elements in Figures 1, 2, 4 and 5 are not explained in the captions or legends.**

| Field | Content |
|---|---|
| Check | P29 |
| Location | Figure 1, p. 24 and caption p. 25, l. 851 to 854; Figure 2, legend and SAF frame, p. 26; Figure 4, x axes, p. 28; Figure 5, blue band, dashed lines and grey zones, p. 29 |
| Quotation | "Gray vertical zones delineate the various periods of the transition from end of MIS3 to Holocene." |
| Concern | Fig. 1 uses PAT, AUS, SAF, NZ, PAP, YD, ACR, HS1, LGM, MIS3, EDC and PSA without expansion in the caption. Fig. 2 uses "Iso" in six legend entries without explanation, and the SAF domain is closed by an unexplained dashed line. Fig. 4 uses "Holo" and the period abbreviations without expansion and does not say which Holocene interval is used (see GB-45). Fig. 5 shows a blue band bounded by dashed lines at 7958 and 11430 yr (measured) and grey zones that are not labelled or explained; the reader has to infer from l. 340 that the band marks the weakening of the westerlies. |
| Suggestion | Expand all abbreviations in the captions of Fig. 1, 2 and 4; explain "Iso" (measured ice core values) and the dashed SAF boundary in the caption of Fig. 2; explain the blue band and label the grey zones in the caption of Fig. 5. |
| Status | verified |
| Severity | minor |
| Source | AB |

**GB-26 Tick labels, legends and axis titles in Figures 1, 2, 3 and 5 are below 6 pt at print size.**

| Field | Content |
|---|---|
| Check | P29 |
| Location | Figure 1, p. 24; Figure 2, legend, p. 26; Figure 3, p. 27; Figure 5, p. 29 |
| Quotation | "Bold lines denote the mobile average over 9 steps." |
| Concern | Cap or digit heights measured at 300 dpi and converted to points: Fig. 1 tick digits and legend 5.0 pt, axis titles 5.7 pt; Fig. 2 legend 5.7 pt; Fig. 3 tick labels 5.0 to 5.3 pt, y axis title 5.7 pt; Fig. 5 tick labels 4.3 pt, legend 4.7 pt, axis title of panel B about 5.0 pt. Fig. 4 (6.0 pt) is at the limit. In Fig. 5 the tick labels are also pale grey. |
| Suggestion | Enlarge tick labels, legends and axis titles in Fig. 1, 2, 3 and 5 to at least 7 pt at final print width. |
| Status | verified (measured) |
| Severity | minor |
| Source | AB |

**GB-27 The sampling gap between 21.7 and 27.3 kyr BP is bridged by continuous smoothed lines in Figures 1, 5, S3 and S5 without being marked.**

| Field | Content |
|---|---|
| Check | P29 |
| Location | Figure 1, all panels, p. 24; Figure 5A, p. 29; Fig. S3 and Fig. S5, Supplement pp. 6 and 10; p. 4, l. 113 |
| Quotation | "A sampling gap exists between 21.7 and 27.3 kyr BP, where only four samples were available." |
| Concern | The gap is disclosed in l. 113, but the figures do not show its consequence: Table S1 has four samples in the interval (22150, 23104, 25384, 25640 yr), and a 9-step mean around them spans more than 5 kyr. The smoothed curves run as straight, nearly flat lines over this interval, which reads as a stable signal, and no caption mentions it. |
| Suggestion | Mark the interval 21.7 to 27.3 kyr BP (hatching or a break in the smoothed line) in Fig. 1, 5, S3 and S5 and mention it in the captions. |
| Status | verified |
| Severity | minor |
| Source | AB |

**GB-28 The "Holocene" panel of Figure 3 shows the Early Holocene, and the "Early Holocene" panel of Figure S4 shows the Late Holocene.**

| Field | Content |
|---|---|
| Check | P3 |
| Location | Figure 3, left panel, p. 27, caption l. 869; Fig. S4, first panel, Supplement p. 8, and caption, Supplement p. 7 |
| Quotation | "Figure 3: Box plots of provenance contributions (in %) of Holocene, and Last Glacial Maximum (LGM)" |
| Concern | Measured box elements (Fig. 3 plus or minus 0.14 %, Fig. S4 plus or minus 0.06 %) compared with quartiles computed from Table S1: the Fig. 3 "Holocene" panel gives PAT Q3 72.88, median 55.09, Q1 12.12, upper whisker 98.35, against Early Holocene (n = 56) 73.0, 55.2, 12.3, 98.5 and full Holocene (n = 116) 73.8, 58.6, 18.4; the PAP whisker deviates from the full Holocene by 12.1. The first panel of Fig. S4 gives PAT 80.65, 61.65, 18.89 against Late Holocene (n = 60) 80.7, 61.7, 18.9. All deviations from the Early or Late Holocene values lie within 0.15. The main text figure labelled "Holocene" thus contrasts LGM with the Early Holocene only, and the full Holocene to which the averages of l. 316 to 319 refer is shown nowhere. |
| Suggestion | Relabel the left panel of Fig. 3 and its caption "Early Holocene (7.5 to 11.7 kyr BP)" or replot it with all Holocene samples; relabel the first panel of Fig. S4 and its caption "Late Holocene (2.8 to 7.5 kyr BP)"; give n per box in both captions. |
| Status | verified (measured) |
| Severity | moderate |
| Source | AB |

**GB-29 The captions of Figures 3 and S4 define the whiskers as extremes, but the whiskers end at 1.5 interquartile ranges with further points beyond them.**

| Field | Content |
|---|---|
| Check | P29 |
| Location | Figure 3, caption p. 27, l. 872; Fig. S4, caption, Supplement p. 7 |
| Quotation | "and the whiskers indicate the lower and upper extremes" |
| Concern | In the left panel of Fig. 3 the AUS whisker ends at 79.70 % while three AUS points lie above it (maximum 98.1 % in Table S1 for the plotted interval), and the SAF whisker ends at 25.47 % with points up to 54.3 %. The whisker ends equal the last value within Q3 plus 1.5 times the interquartile range (AUS: 34.2 + 1.5 x 31.4 = 81.3; last value below 79.8). The plotted points are not explained. |
| Suggestion | Replace in both captions by "whiskers extend to the most extreme values within 1.5 times the interquartile range; dots show individual samples". |
| Status | verified (measured) |
| Severity | minor |
| Source | AB |

**GB-30 The Altiplano panel of Figure S3 does not show the largest Altiplano contributions of Table S1 and Figure 1, so it is unclear which data set Figure S3 shows.**

| Field | Content |
|---|---|
| Check | P3 |
| Location | Fig. S3, panel "Altiplano Total Contribution (%)", Supplement p. 6; p. 11, l. 355 |
| Quotation | "Altiplano Total Contribution (%)" |
| Concern | Raw-data peaks above 15 % in the Altiplano panel (measured, plus or minus 0.14 % and 16 yr) reach at most 66.1 % (6367 yr). Table S1 lists Altiplano 100.0 % (8629 yr), 97.0 % (11228 yr), 75.7 % (9957 yr), 62.7 % (3465 yr) and 58.5 % (5967 yr); none of these appears in the panel, while Fig. 1 shows the first two. Since South Puna is 0 % in these samples, Fig. S3 should show them in the Altiplano panel. The timing statement based on this panel is treated in GB-24. |
| Suggestion | Replot Fig. S3 from the data of Table S1, or state in its caption which model run it shows. |
| Status | verified (measured peaks and their absence; values in Table S1); inferred (that Fig. S3 stems from another data set) |
| Severity | moderate |
| Source | AB |

**GB-31 Subregions carry different names in Figure S3, Table S2 and the text, and the Figure S3 panel "Namibia" is ambiguous.**

| Field | Content |
|---|---|
| Check | P38 |
| Location | Fig. S3, panel labels, Supplement p. 6; p. 11, l. 355 to 358; p. 11, l. 379 to 381; p. 12, l. 392; p. 7, l. 213; p. 9, l. 290; Supplement p. 17, Table S2, SAF rows, column Location |
| Quotation | "the Makgadikgadi Complex (including Sua Pan), the Etosha Pan, and ephemeral river valleys along the Namibian coast" |
| Concern | The text discusses the Makgadikgadi Complex, while Fig. S3 shows a panel "Sua", and Table S2 contains only Sua Pan samples for that system (Sua1 to Sua3); the two names presumably denote one object. The panel "Namibia" is ambiguous, because Etosha Pan also lies in Namibia (l. 131: "23 DS from Namibia and Botswana") and Table S2 labels the coastal samples by river ("Huab river bed, Namibian coast"). Likewise the PAP subregions appear as "South Puna" and "Southern Altiplano" in the text, "Puna" and "Altiplano" in Fig. S3 and Table S1, and "S-Puna" and "S-Altiplano" in Table S3; the text itself varies between "Southern Altiplano" (p. 11, l. 357) and "South Altiplano" (p. 7, l. 213: "emergence of South Altiplano dust"; p. 9, l. 290: "in the South Altiplano linked to"). |
| Suggestion | Use one name per subregion in text, figures and tables, for example "Makgadikgadi (Sua Pan)" and "Namibian coastal rivers" in Fig. S3 and "South Puna" and "Southern Altiplano" throughout (in p. 7, l. 213 "emergence of Southern Altiplano dust", in p. 9, l. 290 "in the Southern Altiplano linked to"), and state in the caption of Fig. S3 which DS each panel aggregates. |
| Status | verified |
| Severity | minor |
| Source | S2 |

**GB-32 Panels 2 to 5 of Figure S4 are drawn about 1.3 to 1.8 % taller than the shared y axis, so their values read up to 1.4 percentage points too high.**

| Field | Content |
|---|---|
| Check | P3 |
| Location | Fig. S4, panels YD, ACR, HS1, MIS3, Supplement p. 8 |
| Quotation | "Box plots of provenance contributions of (1) Early Holocene, (2) Younger Dryas (YD)" |
| Concern | Only the first panel carries the y axis; the five panels are separate images (heights 1356 px for the first, 1336 to 1338 px for the others). Measured against the axis (plus or minus 0.06 %): HS1 PAT Q3, median, Q1 80.51, 76.01, 67.96 against Table S1 79.4, 75.0, 67.0; MIS3 78.38, 71.55, 63.39 against 77.2, 70.5, 62.5; ACR 81.33, 74.25, 57.95 against 80.2, 73.2, 57.2; YD 86.24, 71.38, 47.95 against 84.8, 70.2, 47.1. The ratios are 1.013 to 1.018, while the first panel matches within 0.05. |
| Suggestion | Align the scale of panels 2 to 5 with the y axis of Fig. S4 or give each panel its own axis. |
| Status | verified (measured) |
| Severity | minor |
| Source | AB |

#### Minor corrections

| ID | Location | Quotation | Replacement | Source |
|---|---|---|---|---|
| KK-13 | p. 6, l. 189 | "It contributes for 65-70%" | "It contributes 65 to 70 %" | S3 |
| KK-14 | p. 6, l. 191 | "the PSA dust assemblage during HSI is marked" | "the PSA dust assemblage during HS1 is marked" | S2, S3 |
| KK-15 | p. 6, l. 193 | "(averages contributions)" | "(average contributions)" | S3 |
| KK-16 | p. 6, l. 194 | "Three distinct minima in PAT contributions occur at 10, 8.6, and 6.3 kyr BP." | "Three distinct minima in PAT contributions occur at 10.1, 8.5, and 6.3 kyr BP." (smoothed minima measured in Fig. 1 at 10132, 8492 and 6329 yr; 9-step mean of Table S1 at 10117, 8508 and 6306 yr) | AB |
| KK-17 | p. 6, l. 195 | "contributing to 47-51% of the total mix" | "contributing 47 to 51 % of the total mix" | S3 |
| KK-18 | p. 6, l. 198 | "and therefore reflects regional mixed input" | "and therefore reflect regional mixed input" | S3 |
| KK-19 | p. 6, l. 199 | "LREE (low rare earth elements)" | "LREE (light rare earth elements)" | S3 |
| KK-20 | p. 25, l. 851 | "between 2852 to 33699 yr BP" | "between 2852 and 33699 yr BP" | AB |
| KK-21 | Fig. S4, caption, Supplement p. 7 | "Antarctica Cold Reveal (ACR), (4) Heindrich Stadial 1 (HS1), and (5) Marine Isotope 3 (MIS3)" | "Antarctic Cold Reversal (ACR), (4) Heinrich Stadial 1 (HS1), and (5) Marine Isotope Stage 3 (MIS3)" | S2, AB |
| KK-22 | Table S1, caption, Supplement p. 11 | "based on th DEPOT model results" | "based on the DEPOT model results" | S3 |
| KK-23 | Table S5, caption, Supplement p. 22 | "based on dust samples from EDC and EDML ice core through time" | "based on dust samples from the EDC and EDML ice cores through time" | S3 |

#### Verification log

| ID | Check | Checked | Values | Result |
|---|---|---|---|---|
| PP-26 | P23 | Sample balance from dataset to record | 294 minus 15 = 279 (l. 114, l. 117); 279 minus 38 = 241 (l. 174, l. 179); Table S1 rows 241; per period 60 + 56 + 9 + 8 + 27 + 40 + 41 = 241 | no finding |
| PP-27 | P1 | Percentages of the sample balance | 241 / 279 = 86.4 % (text 86 %); mean R of Table S1 0.8523 (text 0.852) | no finding |
| PP-28 | P12 | Table S1 as the published record of retained samples | 241 rows, ages 2852 to 33699 yr, R column present; agrees with "241 DIC samples" (l. 179) and the span in l. 109 to 110; exclusion of low-concentration samples younger than 14 kyr disclosed (l. 175 to 179) | no finding beyond GB-08 and GB-21 |
| PP-29 | P38 | Period names in text, Table S1 row labels, Table S5 and Fig. S2 to S4 | MIS3, LGM, HS1, ACR, YD, Early and Late Holocene defined l. 184 to 188 and used consistently; Table S1 label "HS" on Supplement p. 14 continues the rotated label "HS1" across the page break | no finding beyond KK-02, KK-14, KK-21 and GB-05 |
| PP-30 | P1, P5 | Table S5 (EDC) recomputed from Table S1 with the limits of l. 185 to 188 | Holocene PAT 48.96, PAP 11.04, SAF 10.74, AUS 23.06, NZ 5.86, ANT 0.29; LGM PAT 65.72, PAP 3.58, SAF 6.33, AUS 10.19, NZ 14.17; MIS3 PAT 70.34, SAF 9.34, AUS 9.09, NZ 9.06; all 56 cells within 0.05 of Table S5; Holocene equals the n-weighted mean of Late (60) and Early (56) Holocene | no finding; Table S5 is the arithmetic mean of the per-sample medians |
| PP-31 | P1 | Row sums of Table S5 | EDC rows 99.9 to 100.1; EDML rows 99.9 to 100.0 | no finding |
| PP-32 | P1 | Row sums of Table S1 | 240 of 241 rows sum to 100.0 plus or minus 0.1 | one row in GB-15 |
| PP-33 | P2 | Results text and Abstract against Table S5 | PAT MIS3 and LGM 70.3 and 65.7 (text 65 to 70), HS1 74.8 (75), ACR 68.9 (69), YD 63.1 (63), Holocene 49.0 (~49), Early and Late 47.1 and 50.7 (47 to 51); AUS 9.1, 10.2, 11.3, 11.1, 14.5, 23.1 (9, 10, 11, 11, ~15, 23); SAF YD 14.6 (15), Holocene 10.7 (~11); NZ LGM 14.2 (14), HS1 7.1, ACR 6.6, YD 3.3, Holocene 5.9 (7, 6.5, 3, 6); PAP Holocene 11.0 (11) | no finding |
| PP-34 | P2 | Time series features of l. 194 and l. 205 against a centred 9-step moving average of Table S1 | PAT minima at 10117 (20.4), 8508 (29.2), 6306 yr (26.4); AUS maxima at 9902 to 10511 (45.4 to 45.7) and 6306 yr (41.8) | no finding for l. 205; l. 194 in KK-16 |
| PP-35 | P11 | Coverage of periods by outputs | Table S5 EDC 8 periods, EDML 5 (EDML 7 to 27 kyr, disclosed l. 406 to 407); box plots Fig. 3 and Fig. S4; isotope calculation for MIS3 and LGM, HS1, ACR, YD, Holocene (l. 251 to 255) | no finding for periods; fluxes and uncertainty in GB-16 and GB-17 |
| PP-36 | P36 | Statements against the manuscript's own records | YD n 7 against 9 (GB-46); above 90 % at five ages against two (GB-24); NZ LGM ~11 % against 14 % and 14.2 (GB-40) | in findings |
| PP-37 | P29, P3 | Inventory of figures and their citations | Fig. 1 to 5 (pp. 24 to 29) cited first in l. 183, 244, 281, 405, 340; Fig. S1 to S5 cited (l. 127, 167, 355, 382, 405); unnumbered Sr and Nd diagram on Supplement p. 20 not cited; no graphical abstract | all figures cited except the diagram in GB-59; order in GB-42 |
| PP-38 | P24 | Grey period zones in Fig. 1 and Fig. 5 against the boundaries of l. 185 to 188 | Fig. 1: YD 11.70 to 12.88, HS1 14.73 to 17.96, MIS3 from 29.02 kyr; Fig. 5B: 11.75 to 12.91, 14.77 to 17.96, from 29.05 kyr (measured) | no finding; all edges within 0.06 kyr |
| PP-39 | P3 | Extremes of the smoothed curves in Fig. 1 against l. 194 and l. 205 | PAT minima 6329, 8492, 10132 yr; AUS maxima 9883 and 10524 yr (measured); 9-step mean of Table S1 at 6306, 8508, 10117 yr and 9902, 10205, 10511 yr | Fig. 1 agrees with Table S1 within line width; 8.6 kyr in KK-16 |
| PP-40 | P3 | Sample lines and labels in Fig. 1 against caption and text | panels PAT, AUS, SAF, NZ, PAP; CWA and ANT omitted as stated (CWA 0.0 in all rows, ANT mean 0.3 % in the Holocene, single value 33.1 % at 3654 yr); legend explains raw and smoothed lines | no finding |
| PP-41 | P3 | Fig. 3, LGM panel, against the 40 LGM samples of Table S1 | measured Q3, median, Q1, whiskers: PAT 71.59, 65.71, 58.75, 84.29, 46.77 (Table S1 71.7, 65.8, 58.9, 84.4, 46.8); AUS 13.85, 10.11, 5.67, 22.60 (14.0, 10.2, 5.8, 22.7); NZ 18.79, 15.35, 10.76, 25.18 (18.9, 15.5, 10.8, 25.3) | no finding |
| PP-42 | P29 | Font sizes in all main figures | Fig. 1 5.0 to 5.7 pt; Fig. 2 legend 5.7 pt, ticks 7.3 pt; Fig. 3 5.0 to 6.0 pt; Fig. 4 6.0 to 6.7 pt; Fig. 5 4.3 to 5.0 pt (accuracy about 0.6 pt); supplement figures not measured (mixed page sizes, no print size defined) | Fig. 4 meets 6 pt; Fig. 1, 2, 3 and 5 in GB-26 |

### Segment 4: Discussion, Conclusion, Declarations, References (p. 7 to 22)

#### Substantive findings

**GB-33 The Discussion and Conclusion place a marked provenance shift at about 14.5 kyr BP (onset of the ACR), but the EDC per-sample results show a progressive change in which the early ACR samples remain glacial in composition.**

| Field | Content |
|---|---|
| Check | P15 |
| Location | p. 7, l. 225 to 226; p. 7, l. 233 to 236; p. 13, l. 445 to 447; p. 14, l. 477 to 480; p. 1, l. 23 to 25 and l. 29 to 31; Supplement p. 22, Table S5, EDC rows HS1 and ACR; Supplement p. 13, Table S1, rows 13032 to 14601 |
| Quotation | "Our calculations highlight a major shift in dust provenance occurred at the onset of the ACR" |
| Concern | The manuscript notes that the ACR and YD results are tentative because few samples cover them (p. 12, l. 407 to 409), but the caveat is not carried into the Conclusion, and the manuscript's own numbers show no step. (1) Table S5: AUS is 11.3 % in HS1 and 11.1 % in the ACR, so the "significantly increased contributions from low-latitude sources, including AUS, SAF and PAP" (l. 235 to 236) are not present for AUS, and no test is reported for any period difference. (2) PAT in the ACR (68.9 %) is higher than in the LGM (65.7 %) and lies within the glacial range 65.7 to 74.8 %; PAT plus NZ is 81.9 (HS1), 75.5 (ACR), 66.4 (YD) and 54.9 % (Holocene), PAP plus SAF plus AUS 18.2, 24.3, 33.6 and 44.8 %, a progressive change through ACR, YD and Holocene. (3) From Table S1, the six ACR samples between 13.41 and 14.60 kyr BP average PAT 76.0, NZ 4.1, AUS 9.8 and SAF 2.8 %, HS1-like values (HS1: 74.8, 7.1, 11.3, 4.9 %); the low ACR mean comes from the two samples at 13.03 and 13.14 kyr BP (PAT 41.9 and 53.7 %). (4) A 9-point running mean of PAT falls from 83.4 % at 15.46 kyr BP to 75.5 % at 14.60, 68.3 % at 13.96 and 63.3 % at 13.03 kyr BP, so the decline begins within HS1 and continues into the YD (Python). The attribution in the Abstract to a "rapid submersion of the Patagonian shelf around 14.5 kyr BP" (p. 1, l. 29 to 31) and the link to Meltwater Pulse 1A (p. 13, l. 450 to 453) rest on this timing, which bears on aims 3 and 4. Question to the authors: was the 14.5 kyr BP timing carried over from the EDML record (p. 3, l. 79 to 84)? The severity is major because, if the concern holds, the statement of when the shift occurred at EDC changes. |
| Suggestion | In p. 7, l. 225 to 236, p. 13, l. 445 to 447 and p. 14, l. 477 to 480, describe the EDC change as Table S1 shows it (progressive decline from about 15.5 to 11.7 kyr BP, main drop after about 13.2 kyr BP), quantify the timing with uncertainty (for example a change-point analysis on the Monte Carlo ensembles), report a test or the Monte Carlo spread before using "significantly", remove AUS from the sources said to increase at the onset of the ACR, and repeat the ACR and YD caveat in the Abstract and Conclusion. |
| Status | verified (Table S5 values and quoted wording); inferred (window and running means from Table S1 by Python); assumption (origin of the 14.5 kyr BP timing from EDML) |
| Severity | major |
| Source | S4 |

**GB-34 The isotopic validation claims close agreement with values measured in EDC for glacial and interglacial intervals, but the measured Holocene values in Table S4 and Figure 2 come from Taylor Glacier and Berkner Island, and no agreement measure is given.**

| Field | Content |
|---|---|
| Check | P31, P15, P11, P3 |
| Location | p. 7, l. 238 to 240; p. 8, l. 252 to 260; p. 3, l. 93 to 94; Figure 2, open symbols, p. 26, caption l. 857 to 858; Supplement p. 21, Table S4 |
| Quotation | "Overall, the close agreement between our modeled isotopic compositions and those measured in EDC for both glacial and interglacial intervals supports the robustness of our DEPOT algorithm" |
| Concern | Confronting the REE result with Sr and Nd data is the right independent check for aim 2. Table S4 lists 35 measured values: 2 from EDC (LGM, "Delmonte et al., 2004a"), 1 from "Old Dome C" (HS1), 18 from Taylor Glacier (Aarons et al., 2017) and 14 from Berkner Island (Bory et al., 2010); 3 of 35 = 8.6 % are from Dome C. The 35 positions computed from Table S4 coincide with the centres of the open circles of Fig. 2 (overlay, measured), and all Holocene open symbols are Taylor Glacier and Berkner Island values, the latter reaching 0.7228 and εNd -14.71. The EDC Holocene values cited in l. 239 to 240 ("~0.710" and εNd "-4.51 to -5.68") appear neither in Table S4 nor in Fig. 2. At the same time, 16 filled Holocene symbols lie at 87Sr/86Sr 0.7113 to 0.7236 and εNd -10.3 to -16.5 (measured), 4.6 to 10.8 εNd units below the quoted EDC Holocene range. Recomputed with Eq. 3 and 4 from Table S3 and the period means, the modelled values are 0.7101 and -4.99 (Holocene), inside the cited EDC range, and 0.7083 and -2.61 (LGM) against -1.66 and -2.46 measured (PP-45). The agreement may therefore hold at period-mean level, but the comparison shown is with a Ross Sea and a Weddell Sea site, and "close agreement" is not quantified. The caption cites "refs. Table S1" for the ice core data, which are in Table S4. Since the figure is the evidence for aim 2, the validation reads differently if the EDC Holocene values lie far from the modelled cloud. |
| Suggestion | Add the EDC Holocene measurements cited in p. 7, l. 239 to 240 to Table S4 and plot them in Fig. 2 as a separate symbol, label other sites by name in the legend, report per period the modelled value with its interval next to the measured EDC value and their difference in Section 4.1, restrict "measured in EDC" in p. 8, l. 258 to periods with EDC data, and replace "refs. Table S1" by "references in Table S4" in the caption (p. 26, l. 858). |
| Status | verified (Table S4 content on the page image, positions of the open symbols against Table S4, filled symbols measured, wording); inferred (recomputed modelled values) |
| Severity | major |
| Source | S3, S4, AB, SD |

**GB-35 The Sr and Nd values for EDC are attributed to "Delmonte et al. (2004)" and "Delmonte et al., 2004a", but the reference list has one Delmonte 2004 entry, a dust size study.**

| Field | Content |
|---|---|
| Check | P4 |
| Location | p. 7, l. 238 to 239; p. 12, l. 416; p. 26, l. 861; Supplement p. 21, Table S4, rows 1 and 2, column Reference; p. 17, l. 561 to 564 |
| Quotation | "For instance, Delmonte et al. (2004) reported 87Sr/86Sr ratios of ~0.708 and ε(Nd) values ranging from -1.66 to -2.46 for LGM dust at EDC" |
| Concern | The suffix in "[Delmonte et al., 2004a]" (Table S4) implies two 2004 entries; the list contains only Delmonte, Petit, Andersen et al. (2004), Climate Dynamics 23, 427 to 438, "Dust size evidence for opposite regional atmospheric circulation changes", whose abstract gives no isotope values. Delmonte, B., Basile-Doelsch, I., Petit, J.R., Maggi, V., Revel-Rolland, M., Michard, A., Jagoutz, E., Grousset, F., 2004. Comparing the Epica and Vostok dust records during the last 220,000 years: stratigraphical correlation and provenance in glacial periods. Earth-Science Reviews 66, 63 to 87, https://doi.org/10.1016/j.earscirev.2003.10.004, reports Sr and Nd data for EDC dust. Is this the intended "2004a"? The citation in l. 416 (atmospheric circulation) fits the Climate Dynamics paper. |
| Suggestion | Clarify which work each citation refers to; if two 2004 papers are used, add the second entry and label them 2004a and 2004b consistently in p. 7, l. 238, p. 12, l. 416, p. 26, l. 861 and Table S4. |
| Status | verified (list content; abstracts of both 2004 papers); assumption (which paper the authors meant), posed as a question |
| Severity | minor |
| Source | S4 |

**GB-36 The isotope calculation is described per time interval, but Figure 2 shows one value per sample, the aggregation is not stated, and samples with an ANT share have no end-member.**

| Field | Content |
|---|---|
| Check | P3, P8, P22 |
| Location | p. 8, l. 244 to 253; Figure 2, filled symbols, p. 26, caption l. 864 to 866; Supplement p. 20, Table S3; Supplement p. 11, Table S1, row 3654, column ANT |
| Quotation | "For each time interval of the LGIT, the relative contribution of each PSA (CONTR) was multiplied by its average Sr and Nd concentrations" |
| Concern | Read literally, l. 244 to 246 yields one point per interval. Fig. 2 shows many filled symbols per period: below εNd -10 alone there are 8 symbols in the colour of "EDC Early Holocene" and 8 in that of "EDC Holocene" (counted), so the figure plots per-sample results, which is not described. The modelled values are not tabulated, and the result depends on the aggregation: recomputed from the period means of Table S1 the YD lies at 0.7094 and -5.39, nearer the Holocene (0.7101 and -4.99) than the glacial cluster, whereas applying Eq. 3 and 4 per sample gives YD 0.7101 and -3.65 (mean) or 0.7077 and -2.52 (median) (Python); l. 251 to 253 place the YD with the glacial cluster. For sample 3654 yr, ANT is 33.1 %, but Table S3 has no ANT end-member, so the calculation as described cannot be carried out for it. The caption assigns the isotopic fingerprint to "Table S4", while Table S3 holds both isotope ratios and concentrations of the end-members. Question to the authors: which aggregation underlies the YD symbols in Fig. 2, and how were ANT and CWA handled? |
| Suggestion | State in p. 8, l. 244 to 250 that Eq. 3 and 4 were applied per sample (or show the interval values as larger symbols), state how ANT and CWA were handled, add a table of the modelled 87Sr/86Sr and εNd per period, revise l. 251 to 253 if the YD does not fall in the glacial cluster, and in the caption (p. 26, l. 865) replace "(ii) the isotopic fingerprint (Table S4) and elemental concentration of the PSAs end-members (Table S3)" by "(ii) the isotopic fingerprint and elemental concentration of the PSA end-members (Table S3)". |
| Status | verified (figure symbols counted on the page image; Table S1 and S3); inferred (recalculated values); assumption (aggregation used by the authors), posed as a question |
| Severity | moderate |
| Source | S3, AB, SD |

**GB-37 The timing and dimensions of the Patagonian Ice Sheet maximum are not reported as in Davies et al. (2020).**

| Field | Content |
|---|---|
| Check | P13 |
| Location | p. 8, l. 267 to 269 |
| Quotation | "the Patagonian Ice Sheet reached its maximum spatial extent between ~34 and 29.4 kyr BP, covering much of the Andes with an ice mass 2090 km long and 350 km wide (Davies et al., 2020)." |
| Concern | Davies et al. (2020) state that the ice sheet reached its maximum extent by 33 to 28 ka from 38°S to 48°S and earlier, around 47 ka, from 48°S southwards, and give the dimensions (350 km wide, 2090 km long) for 35 ka. The values "~34" and "29.4" were not found in the public access text of Davies et al. (2020). The manuscript narrows a latitude-dependent timing to one interval and ties dimensions from 35 ka to it. |
| Suggestion | Replace in p. 8, l. 267 to 269 by "reached its maximum extent by 33 to 28 ka between 38°S and 48°S (around 47 ka farther south); at 35 ka it was 2090 km long and 350 km wide (Davies et al., 2020)", or cite the source of "29.4". |
| Status | verified (abstract and public access full text of Davies et al. 2020) |
| Severity | moderate |
| Source | S1 |

**GB-38 The model studies cited as support for Patagonian dominance give another picture: Krätschmer et al. (2022) simulate Australia as the dominant LGM source for Antarctica, and Albani et al. (2012) give no source percentages.**

| Field | Content |
|---|---|
| Check | P13 |
| Location | p. 8, l. 275 to p. 9, l. 277 |
| Quotation | "Model simulations also support this view, estimating that SSA and AUS sources together supplied 70-90% (here, PAT+AUS is ~77%) of the dust reaching EA during the LGM (i.e., Albani et al., 2012; Krätschmer et al., 2022)." |
| Concern | The phrase "this view" (l. 273 to 275) is the significance of Patagonian sources in glacial dust. Krätschmer et al. (2022) state that Australian and South American sources contribute in sum slightly more than 90 % over the Southern Ocean and Antarctica, and their Table 5 gives for Antarctica in the LGM Australia 68 %, South America 24 %, southern Africa 7 %; they conclude that Australia was the predominant source of dust deposited over Antarctica in the LGM. The ratio AUS to South America in that simulation is 68 / 24 = 2.83, against AUS to PAT 10.2 / 65.7 = 0.16 at EDC in the LGM (Table S5; Python). The combined share hides the split, and the cited simulation contradicts Patagonian dominance instead of supporting it. Albani et al. (2012) contain no source percentages; they identify southern South America as the primary and Australia as a possible secondary source at Talos Dome. The parenthesis "~77%" is treated in GB-39. The REE result itself stands, but the claimed independent support turns into a disagreement with one model that the Discussion does not address. |
| Suggestion | In p. 8, l. 275 to p. 9, l. 277, report the split of Krätschmer et al. (2022) for LGM Antarctica (AUS 68 %, South America 24 %), discuss why the REE apportionment differs from this simulation, and remove Albani et al. (2012) as a source of percentages. |
| Status | verified (both sources read as open access PDFs; ratios by Python) |
| Severity | moderate |
| Source | S1 |

**GB-39 Four sums of period means in the Discussion deviate from Table S5 by more than rounding.**

| Field | Content |
|---|---|
| Check | P1 |
| Location | p. 9, l. 276; p. 9, l. 293 to 294; p. 9, l. 295; p. 10, l. 321 and l. 326; Supplement p. 22, Table S5, EDC |
| Quotation | "with high-latitude sources totaling 84 %" |
| Concern | From Table S5 (EDC): LGM PAT plus AUS 65.7 + 10.2 = 75.9 (text "~77%", l. 276, deviation 1.1); HS1 PAT plus NZ 74.8 + 7.1 = 81.9 (text "84 %", l. 295, deviation 2.1); Holocene PAT plus CWA plus PAP 49.0 + 0.0 + 11.0 = 60.0 (text "61%" in l. 321, while l. 326 gives "60%" for the same quantity); LGM PAT plus NZ 65.7 + 14.2 = 79.9 and AUS plus SAF plus PAP 10.2 + 6.3 + 3.6 = 20.1 (text "~79 %" and "~21 %", l. 294, the smallest deviation, 0.9). Possible bases checked with Table S1: the mean over MIS3 and LGM gives PAT plus AUS 77.7; medians give HS1 PAT plus NZ 81.0; none reproduces 84 % for HS1. |
| Suggestion | Replace the values in p. 9, l. 276 (76 %), l. 294 (80 % and 20 %), l. 295 (82 %) and p. 10, l. 321 (60 %) with the sums of Table S5, or state the basis used. |
| Status | verified (quoted values); inferred (sums by Python) |
| Severity | minor |
| Source | S3 |

**GB-40 The NZ contribution in the LGM is given as ~11 % in Section 4.2 but as 14 % in the Results and Table S5.**

| Field | Content |
|---|---|
| Check | P2 |
| Location | p. 9, l. 281 to 282; p. 7, l. 209; Supplement p. 22, Table S5, row LGM, column NZ |
| Quotation | "However, we find a higher average NZ contribution (~11%), making it the second-largest dust source to EDC during the LGM." |
| Concern | Table S5 gives LGM NZ 14.2, and l. 209 says "an average of 14%". 11 % matches the mean over MIS3 and LGM (11.6) or LGM and HS1 (11.3) (Table S1, Python), not the LGM. The ranking claim holds with either value (AUS 10.2), but the contrast with the 5 % of Coppo et al. (2022) is understated. |
| Suggestion | Write "(~14%)" in p. 9, l. 282 or name the interval to which 11 % refers. |
| Status | verified; inferred (alternative interval means) |
| Severity | minor |
| Source | S3 |

**GB-41 In-text citations and reference list do not match in four cases: a citation without entry, a year mismatch, an entry without citation and a single-author entry cited as "et al.".**

| Field | Content |
|---|---|
| Check | P4 |
| Location | p. 10, l. 334 and p. 21, l. 781 to 783; p. 11, l. 365; p. 13, l. 439 and p. 17, l. 551 to 552; p. 18, l. 630 to 632 |
| Quotation | "(Speirs et al., 2001)" |
| Concern | (1) "(Gili et al., 2016)" (l. 365) has no entry; the previous Pb isotopic study meant is presumably Gili, S., Gaiero, D.M., Goldstein, S.L., Chemale, F., Koester, E., Jweda, J., Vallelonga, P., Kaplan, M.R., 2016. Provenance of dust to Antarctica: a lead isotopic perspective. Geophysical Research Letters 43, 2291 to 2298, https://doi.org/10.1002/2016GL068244, whose abstract states a more prominent Puna-Altiplano contribution during interglacials. (2) Speirs et al. are cited as 2001 (l. 334) but listed as 2010. (3) Gaiero et al. (2007, Chemical Geology; l. 630 to 632) is not cited anywhere; "Gaiero, 2007" (l. 274, l. 861) matches the single-author entry. (4) De Deckker (2019) is a single-author entry but cited as "De Deccker et al., 2019" (l. 439). Bidirectional count: 91 entries, 89 cited in the main text, EPICA Community Members (2006) only in the supplement, Gaiero et al. (2007) nowhere, one cited work without entry. |
| Suggestion | Add the Gili et al. (2016) entry, correct the Speirs year in text or list, cite or delete Gaiero et al. (2007), and change p. 13, l. 439 to "(De Deckker, 2019;". |
| Status | verified (mismatches on the page images pp. 10, 11, 13, 17, 18, 21; Gili et al. 2016 abstract); assumption (intended Speirs year) |
| Severity | minor |
| Source | S4 |

**GB-42 Figure 5 is cited before Figure 4.**

| Field | Content |
|---|---|
| Check | P3 |
| Location | p. 10, l. 340; p. 12, l. 405 |
| Quotation | "Aike bog (see Figure 5)" |
| Concern | Order of first citation: Fig. 1 (l. 183), 2 (l. 244), 3 (l. 281), 5 (l. 340), 4 (l. 405). The numbering does not follow the order of citation. |
| Suggestion | Swap the numbers of Fig. 4 and Fig. 5 so that the Potrok Aike comparison becomes Fig. 4 and the EDC and EDML differences Fig. 5, and adapt the citations in p. 10, l. 340, p. 12, l. 405, p. 13, l. 419 and the captions. |
| Status | verified |
| Severity | minor |
| Source | AB, S4 |

**GB-43 The drop in Patagonian dust at 6 to 6.5 kyr BP is said to be present in the Potrok Aike wind record, but the MDF curve in Figure 5B shows no distinct feature at that time.**

| Field | Content |
|---|---|
| Check | P24 |
| Location | p. 11, l. 350 to 352; Figure 5, panel B, p. 29 |
| Quotation | "Apart from a well-marked drop in PAT contributions between 6-6.5 kyr BP (also present in Potrok Aike wind intensity record)" |
| Concern | Bold MDF curve in Fig. 5B, minimum and maximum per half millennium (measured, plus or minus 0.17 mT): 5.0 to 5.5 kyr 15.1 to 20.6 mT; 5.5 to 6.0 kyr 16.8 to 19.5; 6.0 to 6.5 kyr 16.9 to 18.0; 6.5 to 7.0 kyr 15.8 to 17.2; 7.0 to 7.5 kyr 15.3 to 17.1. The highest MDF (weakest wind) between 5 and 7.5 kyr lies at 5442 yr (20.6 mT); the values in 6.0 to 6.5 kyr lie inside the range of the neighbouring intervals, and the total amplitude of 5.5 mT is small against the axis range of 60 mT. The asserted correspondence is not visible, and the strongest weakening in this segment differs in age by about 0.6 to 1.0 kyr. |
| Suggestion | Mark the interval 6 to 6.5 kyr BP in Fig. 5 and show the MDF feature meant (for example a zoomed inset), or delete "also present in Potrok Aike wind intensity record" in p. 11, l. 351. |
| Status | verified (measured curve); inferred (that no feature is visible at the scale of the figure) |
| Severity | moderate |
| Source | AB |

**GB-44 The EDML values used for the EDC and EDML comparison differ from those published in the cited 2023 study, and the manuscript does not say whether they were recomputed; either way, the comparison mixes or hides a change of model configuration.**

| Field | Content |
|---|---|
| Check | P13, P7 |
| Location | p. 12, l. 403 to 407; Supplement p. 22, Table S5, EDML block; p. 3, l. 79 to 81; p. 5, l. 144 to 145; p. 9, l. 287 to 288; p. 13, l. 417 to 424; Figure 4, p. 28; Fig. S5, Supplement pp. 9 to 10; p. 1, l. 27 to 29; p. 14, l. 484 to 487 |
| Quotation | "In the Holocene, the discrepancies become more pronounced: EDC appears to receive substantially less PAT dust (-14%) but higher contributions of Australian dust (+12%) than EDML." |
| Concern | The text attributes the EDML record to "our recent study on the EDML ice core (Vanderstraeten et al., 2023)" (l. 404), and the Introduction reports it as published: Patagonia "below 50% on average" after about 14.5 kyr BP (l. 79 to 80). The abstract of Vanderstraeten et al. (2023) gives, before 14.5 kyr BP, Patagonia about 68 %, Australia 14 to 15 %, New Zealand about 3 to 4 %; after 14.5 kyr BP Patagonia below 50 %, southern Africa 21 to 23 %, Australia 13 to 21 %; and in the Early Holocene Patagonia about 50 %; it used 207 source patterns, 14 REE, and retained 386 of 398 samples. The EDML block of Table S5 gives other values: PAT 62.5 (ACR), 58.4 (YD) and 62.7 (Early Holocene), all above 50 %; SAF 12.4, 8.2 and 11.2 after 14.5 kyr BP instead of 21 to 23 %; AUS 9.7 (LGM) and 9.4 (HS1) instead of 14 to 15 %; NZ 6.2 (LGM) instead of 3 to 4 %. The manuscript thus contradicts itself between l. 79 to 80 and Table S5. The differences of Section 4.4 follow from Table S5 (Holocene PAT 49.0 minus 62.7 = -13.7, AUS 23.1 minus 10.8 = +12.3, LGM NZ 14.2 minus 6.2 = +8.0); with the published values they change (Early Holocene PAT 47.1 minus about 50 = about -3; SAF after 14.5 kyr BP 10.7 minus 21 to 23 = -10.3 to -12.3; LGM NZ 14.2 minus 3 to 4 = +10.2 to +11.2; Python), so the pronounced Holocene PAT contrast would largely disappear and a large SAF contrast would appear. Two readings exist. If the EDML values are taken from the 2023 study, site differences are confounded with element set (14 against 13 REE, l. 144 to 145), database (207 against 217 patterns), selection (97 % against 86 % retained) and raw data source (Wegner et al., 2012 against Gabrielli et al., 2010). If they were recomputed with the present configuration, this is not stated and the published and new EDML values are not compared. No uncertainty accompanies any difference. Aim 4 (p. 3, l. 95 to 98), the Abstract (p. 1, l. 27 to 29) and the Conclusion (p. 14, l. 484 to 487) rest on these differences. |
| Suggestion | State in Section 2 and in the caption of Table S5 whether the EDML values were recomputed with 13 REE and 217 patterns or taken from Vanderstraeten et al. (2023). Best: rerun the EDML REE data with the present configuration (same threshold and Monte Carlo), give published and recomputed EDML means side by side in Table S5, report each difference with its Monte Carlo interval, and correct p. 3, l. 79 to 81, p. 9, l. 288, p. 13, l. 417 to 424, Fig. 4 and the Abstract accordingly. |
| Status | verified (Table S5 against the published abstract of Vanderstraeten et al. 2023, Science of the Total Environment 881, 163450, read at marineinfo.org; contradiction between p. 3, l. 79 to 80 and Table S5; differences by Python); assumption (whether the EDML data were recomputed) |
| Severity | major |
| Source | S1, SD |

**GB-45 The EDC minus EDML differences in Section 4.4 and Figure 4 do not follow from Table S5 as stated: the Holocene bars compare different windows, and the ACR and YD values are swapped and wrongly compensated.**

| Field | Content |
|---|---|
| Check | P2, P3, P5, P21 |
| Location | p. 12, l. 405 to 407; p. 13, l. 421 to 424; Figure 4, all panels, p. 28, caption l. 875 to 876; Supplement p. 22, Table S5 |
| Quotation | "the ACR and YD intervals exhibit a slight enrichment of Patagonian dust (+4 and +6.5%) in EDC, primarily at the expense of Southern African and Australian contributions." |
| Concern | (1) The comparison is announced "over their overlapping interval shared by both datasets, i.e., between 7.5 and 27 kyr BP" (l. 406 to 407), and EDML has only an Early Holocene row. The Holocene values "(-14%)" and "(+12%)" (l. 424) and the "Holo" bars of Fig. 4 (measured PAT -13.97, AUS +12.44, SAF -0.69, NZ +0.42, PAP +1.79) reproduce only the full EDC Holocene (2.8 to 11.7 kyr) minus the EDML Early Holocene: -13.7, +12.3, -0.5, +0.4, +1.6. On the shared window (EDC Early Holocene) the differences are PAT -15.6, AUS +14.1, SAF -1.4, NZ +2.6, PAP +0.6 (Python). The direction stands, but the numbers and the NZ difference change. (2) From Table S5: ACR PAT 68.9 minus 62.5 = +6.4, YD PAT 63.1 minus 58.4 = +4.7; the text assigns +4 to the ACR and +6.5 to the YD, the reverse; Fig. 4 agrees with Table S5 (measured ACR +6.49, YD +4.96). (3) Compensation: ACR SAF -4.4 and AUS -7.4 (the statement holds), but YD SAF +6.4, AUS -4.5, NZ -3.9, PAP -2.4: in the YD EDC receives more southern African dust than EDML, and the YD bar of the SAF panel lies above zero. The caption cites "(Table S4)" for the period averages, which are in Table S5, and calls the bars "Histograms", though they show differences of means. |
| Suggestion | Recompute the "Holo" bars of Fig. 4 and p. 13, l. 423 to 424 from the EDC Early Holocene (or label them "EDC Holocene minus EDML Early Holocene" and justify it); write "(+6.4 and +4.7%)" in p. 13, l. 422 and name the compensation per interval (ACR: AUS and SAF; YD: AUS, NZ and PAP, with more SAF at EDC); in the caption (p. 28, l. 875 to 876) replace "Histograms" by "Bar charts" and "(Table S4)" by "(Table S5)". |
| Status | verified (text and table values; bars measured); inferred (differences by Python) |
| Severity | moderate |
| Source | S3, AB, SD |

**GB-46 The YD sample count is misstated, the number of samples per period is not given, and the caveat that ACR and YD are tentative appears only in Section 4.4.**

| Field | Content |
|---|---|
| Check | P2, P17, P22 |
| Location | p. 12, l. 407 to 409; p. 6, l. 192 to 193; p. 6, l. 203 to p. 7, l. 212; p. 7, l. 233; Supplement p. 22, Table S5; Supplement p. 13, Table S1, YD block |
| Quotation | "(8 and 7 samples in ACR and YD, respectively, compared to 47 and 27 in EDML)" |
| Concern | The manuscript openly flags the ACR and YD results as tentative. The YD block of Table S1 (rows 11779, 11993, 12227, 12477, 12588, 12754, 12841, 12841, 12867 yr) has 9 rows, also with the limits 12.9 to 11.7 kyr BP of l. 186 to 187, and the YD means of Table S5 (PAT 63.1, PAP 4.5, SAF 14.6, AUS 14.5, NZ 3.3) are reproduced only with all 9 (63.06, 4.52, 14.63, 14.50, 3.28; Python). The ACR count of 8 is correct. The other counts must be derived from Table S1: Late Holocene 60, Early Holocene 56, HS1 27, LGM 40, MIS3 41. The Results report ACR and YD means (l. 192 to 193, l. 207) and Section 4.1 places the "major shift" at the onset of the ACR (l. 233) without the caveat, and Table S5 gives no n, although the reliability of each mean depends on it, as l. 407 to 409 argue. |
| Suggestion | Correct "8 and 7 samples" to "8 and 9 samples" in p. 12, l. 408 (or state which two YD samples are excluded and recompute Table S5), add a column n to Table S5 for EDC and EDML, and repeat the caveat in Section 3 (p. 6, l. 192 and l. 207) and Section 4.1 (p. 7, l. 233). |
| Status | verified (page image, count, wording); inferred (recalculated means and counts by Python) |
| Severity | moderate |
| Source | S3, SD |

**GB-47 The record is compositional, yet the manuscript infers amplified or greater low-latitude dust inputs; normalised by the total flux, which falls by up to a factor of 25, the absolute low-latitude input decreases.**

| Field | Content |
|---|---|
| Check | P21, P10 |
| Location | p. 13, l. 440 to 443; p. 1, l. 23 to 24; p. 10, l. 315 to 318; p. 14, l. 462 to 465; p. 2, l. 62 to 63; Supplement p. 4, Fig. S2 A; Supplement p. 22, Table S5 |
| Quotation | "The enhanced contributions of low-latitude sources to EDC during the Holocene reflect both warmer climate circulation patterns" |
| Concern | The manuscript itself speaks of "a relative increase in dust input from lower-latitude source regions" (p. 14, l. 463), which is correct for percentages, but the same paragraph and the Abstract go further: "which likely amplified dust emissions and transport from these sources" (l. 443) and "the dust assemblage shifted toward greater inputs from low-latitude sources" (p. 1, l. 23 to 24). Percentages are closed: a fall in PAT raises all other shares without any change in their emissions. AUS rises from 10.2 % (LGM) to 23.1 % (Holocene), a factor of 2.26; with the interglacial total flux "up to 25 times lower than LGM fluxes" (p. 2, l. 63), the Holocene AUS flux is 23.1 / (10.2 x 25) = 0.09 of the LGM value, for a factor of 10 it is 0.23 and for a factor of 5 it is 0.45 (Python). An absolute AUS increase would require the total flux to fall by less than a factor of 2.26; Fig. S2 A shows a far larger decline of the smoothed nssCa2+ flux (868 at 22 kyr against 22 at 14 kyr, measured). The same holds for SAF (6.3 to 10.7 %) and PAP (3.6 to 11.0 %). The aridity argument therefore claims a mechanism the compositional design cannot separate from a pure PAT decline. The PSA fluxes announced in p. 5, l. 166 to 167 would decide the question (GB-17). The causal wording "demonstrate" is treated in GB-50. |
| Suggestion | Report absolute PSA fluxes per period with Monte Carlo intervals (GB-17), test per PSA whether the absolute flux rose, stayed or fell across 14.5 kyr BP, and rewrite p. 1, l. 23 to 24, p. 10, l. 316 and p. 13, l. 440 to 443 in relative terms ("a larger share of") unless the fluxes show an increase. |
| Status | verified (wording; absence of fluxes); inferred (ratios from Table S5 and p. 2, l. 63; flux values measured in Fig. S2 A) |
| Severity | major |
| Source | S3, SD |

**GB-48 The decline in total dust deposition "in both cores" is referred to Figures S2 and S5, but neither figure shows total deposition for EDML, and Figure S5 shows no deposition at all.**

| Field | Content |
|---|---|
| Check | P4 |
| Location | p. 13, l. 448 to 450; Supplement p. 4, Fig. S2; Supplement p. 10, Fig. S5 |
| Quotation | "continued until ~15 kyr BP in both cores (Figures S2 and S5)" |
| Concern | Fig. S2 shows EDC nssCa2+ flux, δ18O and deuterium excess; Fig. S5 shows relative PSA contributions (%) for EDC and EDML. The EDML part of the statement has no target in the manuscript. |
| Suggestion | Add an EDML dust flux record with its source to Fig. S2, or cite the EDML flux source in p. 13, l. 450 and refer only to Fig. S2 for EDC. |
| Status | verified (page images) |
| Severity | minor |
| Source | S4 |

**GB-49 The NZ contribution already halves between the LGM and HS1, before 14.5 kyr BP, yet its decline is attributed to later shelf submergence, and the Conclusion groups NZ with Patagonia as a dominant source in MIS3 and HS1, where NZ ranks below AUS and SAF.**

| Field | Content |
|---|---|
| Check | P15 |
| Location | p. 14, l. 461 to 463; p. 14, l. 474 to 476; p. 7, l. 209 to 210; Supplement p. 22, Table S5, EDC, column NZ |
| Quotation | "The combined effects of continental shelf submergence in Patagonia (and New Zealand), along with drainage reversals and reorganized river networks, led to a persistent decline in high-latitude dust contributions" |
| Concern | Table S5 gives NZ 9.1 (MIS3), 14.2 (LGM), 7.1 (HS1), 6.6 (ACR), 3.3 (YD) and 5.9 % (Holocene). The main decline (14.2 to 7.1 %, a factor of 2.0) occurs between LGM and HS1, before the submergence invoked in l. 461 to 463; from HS1 to the Holocene NZ changes only from 7.1 to 5.9 %, and the Results' "its influence steadily declines over time" (l. 209 to 210) does not describe MIS3 to LGM. In MIS3 NZ (9.1 %) equals AUS (9.1 %) and lies below SAF (9.3 %); in HS1 NZ (7.1 %) lies below AUS (11.3 %). NZ is the second source only in the LGM, so "particularly Patagonia (and New Zealand)" (l. 476) holds for the LGM only. The Patagonian result stands. |
| Suggestion | In p. 14, l. 461 to 463 restrict the shelf argument to the timing the data show for NZ or give a separate explanation for the LGM to HS1 decline; in p. 14, l. 475 to 476 write "particularly Patagonia, and New Zealand during the LGM". |
| Status | verified (Table S5 values on the page image); inferred (factor 14.2 / 7.1) |
| Severity | moderate |
| Source | S4 |

**GB-50 The attribution of the shift to shelf submergence and drainage reorganisation is stated as demonstrated and confirmed, although no mechanism is tested and the manuscript itself names transport changes as alternative causes.**

| Field | Content |
|---|---|
| Check | P15 |
| Location | p. 14, l. 466 to 470; p. 14, l. 480 to 482; p. 14, l. 488 to p. 15, l. 490; p. 1, l. 29 to 31 |
| Quotation | "Importantly, our data demonstrate that these feedback mechanisms influenced dust deposition not only in EDML" |
| Concern | The results are relative contributions per sample. The mechanisms (Meltwater Pulse 1A shelf flooding, drainage reversals, paleolake desiccation) come from the literature (l. 450 to 460) and are linked to the record by temporal coincidence only; no shelf area or drainage time series is compared with the EDC record. The manuscript itself lists other causes of the post-14.5 kyr change: reduced transport efficiency by wet scavenging and longer trajectories (p. 10, l. 308 to 313), circulation changes and low-latitude aridity (p. 13, l. 440 to 443), and it attributes the HS1 flux decline to transport (p. 9, l. 296 to 298). With several candidate causes and no test that separates them, the data are consistent with the proposed mechanism but neither "demonstrate" it nor, as l. 480 to 481 say, "confirm our previous study"; GB-33 further weakens the temporal argument. The provenance result stands; the strength of the causal claim changes. |
| Suggestion | Replace "demonstrate" (p. 14, l. 466), "confirm" (l. 480, for example "As such, these results are consistent with our previous study on the EDML dust record, which showed a similar shift") and "emphasize the role" (l. 488) by wording such as "are consistent with"; in Section 4.4 name the competing explanations (source area against transport) and state which observation would separate them, for example the timing of the PAT decline against a dated record of Patagonian shelf exposure. |
| Status | verified (wording and alternative causes with locations) |
| Severity | moderate |
| Source | S4 |

**GB-51 Two research aims are not taken up in the Conclusion: the validation against Sr and Nd data (aim 2) and the Holocene provenance for which there is "no consensus" (aim 1).**

| Field | Content |
|---|---|
| Check | P15 |
| Location | p. 14, l. 472 to p. 15, l. 492; p. 3, l. 91 to 94 |
| Quotation | "(2) confronting and validating the EDC results from our REE pattern-based model against Sr-Nd isotopic data published in the literature" |
| Concern | Section 4.1 addresses aim 2 and Section 4.3 compares the Holocene results with Coppo et al. (2022) and Kok et al. (2021), but the Conclusion neither mentions the isotopic check nor states how the EDC Holocene record bears on the lack of consensus named in aim 1 ("particularly during the Holocene for which there is no consensus", l. 92). The Abstract mentions the Sr and Nd check (l. 25 to 26). |
| Suggestion | Add one sentence each to Section 5: the outcome of the Sr and Nd comparison (with the qualification of GB-34) and the Holocene composition relative to the earlier estimates (for example SSA 60 % here against 33 % in Coppo et al., 2022, p. 10, l. 325 to 326). |
| Status | verified |
| Severity | minor |
| Source | S4 |

**GB-52 The Conclusion explains the EDC and EDML differences by climate in the source areas, whereas the Discussion explains them by the positions of the two sites; source-area climate alone cannot produce differences between two cores fed by the same sources.**

| Field | Content |
|---|---|
| Check | P15 |
| Location | p. 14, l. 485 to 487; p. 13, l. 424 to 428; p. 13, l. 440 to 443 |
| Quotation | "the relative contributions of PAT, SAF, NZ and AUS differed reflecting regional climatic dynamics in their respective source areas" |
| Concern | Section 4.4 attributes the differences to transport ("These differences are consistent with the geographic positioning of the two sites", l. 424 to 425; storm track, polar vortex, Rossby waves, jet entrainment, l. 425 to 440). Both cores are unmixed against the same PSA, so changes in emission strength would alter both records in the same direction; a difference between EDC and EDML requires a difference in transport or deposition. The Conclusion sentence does not follow from the Discussion and conflates aim 3 (temporal shifts related to PSA climate) with aim 4 (spatial variability). |
| Suggestion | Rewrite p. 14, l. 486 to 487 in line with Section 4.4, for example "the relative contributions of PAT, SAF, NZ and AUS differed, consistent with the different exposure of the two sites to mid-latitude and subtropical air masses". |
| Status | verified (both passages); inferred (logical point from the shared PSA database, p. 12, l. 403 to 407) |
| Severity | moderate |
| Source | S4 |

**GB-53 The iron fertilization framework that motivates the study is not taken up in the Discussion, and the closing statement on biogeochemical and atmospheric implications has no basis in the results.**

| Field | Content |
|---|---|
| Check | P15, P10 |
| Location | p. 15, l. 490 to 492; p. 2, l. 37 to 51 |
| Quotation | "with implications for biogeochemical fluxes, atmospheric circulation (chemistry and physics), and climate feedbacks on glacial-interglacial timescales" |
| Concern | The Introduction motivates the study with dust-borne iron fertilization, pCO2 drawdown and source-specific iron content and solubility, ending "identifying and quantifying the contributions of individual PSA is essential to help better constrain models of dust-driven iron fertilization" (p. 2, l. 49 to 50). This framing needs PSA-specific fluxes, which are not shown (GB-17), so it has no instrument and no result topic. None of Sections 4.1 to 4.4 returns to iron, solubility or biogeochemical consequences of the source shift, and atmospheric chemistry is discussed nowhere. The severity follows the S4 assessment; the major severity of the SD finding from which part of this point comes attaches to its core, merged in GB-47. |
| Suggestion | Either add a short paragraph to Section 4 on what the shift from PAT to AUS, SAF and PAP sources implies for iron supply (citing the iron solubility references already in the list), or reduce p. 15, l. 490 to 492 to what the manuscript shows and shorten the motivation in p. 2, l. 37 to 51. |
| Status | verified |
| Severity | minor |
| Source | S4, SD |

**GB-54 The author contribution statement assigns the measurements to "P.B", but no author has these initials, and two authors have no stated role.**

| Field | Content |
|---|---|
| Check | P4 |
| Location | p. 16, l. 497 to 499 |
| Quotation | "P.B performed the measurements; A.V., St. B and G.L. developed together the model" |
| Concern | The authors are S. Boxho, A. Vanderstraeten, N. Mattielli, G.G. Laruelle, A. Bory, P. Gabrielli and S. Bonneville (p. 1, l. 4 to 5). "P.B" matches none; the REE dataset was published by Gabrielli et al. (2010) (l. 108). Is P. Gabrielli (P.G.) meant, and do the measurements include the six new SAF samples (GB-06)? N. Mattielli and A. Bory appear only under "All authors reviewed". |
| Suggestion | Correct the initials in p. 16, l. 497, state which measurements were made in this study, write "A.V., St.B. and G.L. developed the model together", and state the contributions of N.M. and A.B. |
| Status | verified (mismatch); assumption (P.G. as intended author), posed as a question |
| Severity | minor |
| Source | S4, S2 |

**GB-55 Eighteen reference entries contain visible RTF escape codes and trailing backslashes instead of dashes and accented letters.**

| Field | Content |
|---|---|
| Check | P16 |
| Location | p. 16, l. 528; p. 17, l. 553 to 556, l. 588, l. 590, l. 593; p. 18, l. 606, l. 632, l. 645 to 648, l. 653 to 654; p. 19, l. 693 to 694, l. 703 to 707, l. 710; p. 20, l. 714 to 716, l. 742, l. 746 to 747, l. 757 to 758; p. 21, l. 795, l. 799, l. 817; p. 22, l. 821, l. 826 to 828 |
| Quotation | "Mall\uc0\u237{}n Pollux, Coyhaique, Province Ais\uc0\u233{}n" |
| Concern | The codes are printed on the page images (pp. 16 to 22). Affected entries: Bullard and McTainsh (2003), De Deckker et al. (2014), Dukes et al. (2018), Engelbrecht et al. (2019), Fletcher and Moreno (2012), Gaiero et al. (2007), Gingele and De Deckker (2005), Grousset and Biscaye (2005), Lisé-Pronovost et al. (2015), Markgraf et al. (2007), Markle et al. (2018), Moreno et al. (2010), Power et al. (2008), Quade and Kaplan (2017), Stone et al. (2010), Stuut et al. (2002), Veres et al. (2013), Wagner et al. (2021). Page ranges, several author names and the coordinates in Markgraf et al. are unreadable as printed, and the trailing backslash after several DOIs breaks the links. |
| Suggestion | Replace each code by its character (page range dash, apostrophe, í, é, ñ, degree sign, prime and double prime, hyphen) and delete the trailing backslashes in all eighteen entries. |
| Status | verified (page images) |
| Severity | minor |
| Source | S4 |

**GB-56 The reference list mixes several citation styles and journal name conventions.**

| Field | Content |
|---|---|
| Check | P16 |
| Location | p. 17, l. 584 to 585; p. 18, l. 633 to 636; p. 20, l. 732; p. 22, l. 844 to 846; journal names throughout (for example p. 16, l. 505 and l. 509) |
| Quotation | "Yang, Y., Carey-Smith, T., & Turner, R. (2024)." |
| Concern | Most entries follow the pattern surname, initials, year, title, journal, volume, pages, DOI. Ding et al. (2011) uses "et al." in the list and puts the year at the end, Gaiero et al. (2013) uses inverted initials for co-authors, the year in parentheses and "doi:", Yang et al. (2024) uses APA with "&", Placzek et al. prefixes "doi:" to a DOI link, and journal names are abbreviated in some entries ("Clim. Past", "Nature Geosci", "Clim Dyn") and spelled out in others ("Earth and Planetary Science Letters"). Only uniformity is checked here. |
| Suggestion | Bring all entries to the majority style (or the journal's style) and use abbreviated or full journal names throughout; in particular p. 17, l. 584 to 585: full author list, then "2011. Winter warming in West Antarctica caused by central tropical Pacific warming. Nature Geosci. 4, 398-403. https://doi.org/10.1038/ngeo1129"; p. 18, l. 633 to 636: "Gaiero, D.M., Simonella, L., Gassó, S., Gili, S., Stein, A.F., Sosa, P., Becchio, R., Arce, J., Marelli, H., 2013." with "J. Geophys. Res. Atmos. 118, 3817-3831. https://doi.org/10.1002/jgrd.50036"; p. 20, l. 732: "https://doi.org/10.1130/B25770.1" without "doi:"; p. 22, l. 844 to 846: "Yang, Y., Carey-Smith, T., Turner, R., 2024." with "Atmospheric Science Letters 25, e1203. https://doi.org/10.1002/asl.1203". |
| Status | verified (page images) |
| Severity | minor |
| Source | S4 |

**GB-57 Several axes lack a quantity or unit: the time axis of Figure 5 has neither title, unit nor multiplier, and the three y axes of Figure S2 have no units.**

| Field | Content |
|---|---|
| Check | P29 |
| Location | Figure 5, x axes of panels A and B, p. 29; Fig. S2, y axes of panels A, B, C, Supplement p. 4 |
| Quotation | "(A) Non Sea Salt Calcium (nssCa2+) flux in EDC ice core (Fischer et al., 2007) (B) δ18O in EDC ice core" |
| Concern | Fig. 5 labels the time axis only with "0.5, 1, 1.5, 2, 2.5, 3"; unlike Fig. 1 there is no "Time (yr BP)" and no "x10^4", so the axis reads as 0.5 to 3 without unit. In Fig. S2 the axis titles read "nssCa2+ flux", "δ18O" and "deuterium excess" without units (the text gives µg m-2 yr-1 for the flux in p. 5, l. 166), and the δ18O ticks carry no per mil sign. |
| Suggestion | Add "Time (kyr BP)" or "Time (yr BP) x10^4" to both axes of Fig. 5; add units to the y axes of Fig. S2 (µg m-2 yr-1, per mil, per mil). |
| Status | verified |
| Severity | minor |
| Source | AB |

**GB-58 The EDC curves in Figure S5 differ in timing and amplitude from those in Figure 1 and from a 9-step mean of Table S1, although both captions state the same smoothing.**

| Field | Content |
|---|---|
| Check | P3 |
| Location | Fig. S5, panels PAT and AUS, EDC curve, Supplement p. 10; Figure 1, panels PAT and AUS, p. 24; p. 13, l. 444 to 447 |
| Quotation | "(mobile average over 9 steps)" |
| Concern | Measured extremes of the bold EDC curves between 7.5 and 11.5 kyr: Fig. S5 PAT minima 22.9 % at 8.85 kyr and 22.4 % at 10.08 kyr, AUS maxima 50.8 % at 10.08 kyr and 50.6 % at 10.65 kyr; Fig. 1 PAT minima 30.0 % at 8.49 kyr and 23.4 % at 10.13 kyr, AUS maxima 42.7 % at 9.88 kyr and 43.5 % at 10.52 kyr. A centred 9-point mean of Table S1 gives PAT 29.2 % at 8508 yr and AUS 45.7 % at 9902 yr and 45.4 % at 10511 yr. Fig. 1 agrees with Table S1 within line width; Fig. S5 deviates by about 0.35 kyr and 17 percentage points at 8.85 kyr and by about 7 percentage points at the AUS maxima. Fig. S5 is the basis for the synchrony of millennial changes in EDC and EDML (l. 444 to 447). Question to the authors: was EDC placed on a common age scale with EDML for Fig. S5? |
| Suggestion | State in the caption of Fig. S5 which EDC series, chronology and smoothing it shows; if EDC was placed on a common age scale with EDML, give the scale; otherwise replot the EDC curves from Table S1. |
| Status | verified (measured deviations); assumption (cause, for example another age model), posed as a question |
| Severity | moderate |
| Source | AB |

**GB-59 The supplement contains an unnumbered figure without caption on the Table S3 page.**

| Field | Content |
|---|---|
| Check | P29 |
| Location | Table S3, Supplement p. 20, figure below the table |
| Quotation | "Table S3: Selected values of Sr and Nd isotopic and elemental compositions for the PSA end-members used for the Figure 2" |
| Concern | Below Table S3 a Sr and Nd diagram with PSA domains, end-member stars and its own legend is placed (800 x 450 px). It has no number, no caption and is not cited, so its relation to Fig. 2 (domains without stars) is not stated. |
| Suggestion | Number the diagram (for example Fig. S6), add a caption ("Position of the PSA end-members of Table S3 in Sr and Nd space") and cite it in Section 4.1. |
| Status | verified |
| Severity | minor |
| Source | AB |

#### Minor corrections

| ID | Location | Quotation | Replacement | Source |
|---|---|---|---|---|
| KK-24 | p. 7, l. 220 | "in the Epica" | "in the EPICA" | S2 |
| KK-25 | p. 7, l. 229 | "regional climatic evolution (3) compare" | "regional climatic evolution; and (3) compare" | S4 |
| KK-26 | p. 7, l. 233 | "Our calculations highlight a major shift in dust provenance occurred" | "Our calculations highlight that a major shift in dust provenance occurred" | S4 |
| KK-27 | p. 7, l. 236 | "This shift already describes by Gili et al. (2022) and Vanderstraeten et al. (2023), appears" | "This shift, already described by Gili et al. (2022) and Vanderstraeten et al. (2023), appears" | S4 |
| KK-28 | p. 8, l. 246 | "(Table S3, e.i. Eq.3)" | "(Table S3, i.e., Eq. 3)" | S4, SD |
| KK-29 | p. 8, l. 249 | "where the mean isotopic signatures is represents by CIR PSA" | "where CIR PSA represents the mean isotopic signature of each PSA" | S4 |
| KK-30 | p. 8, l. 261 | "4.2 Persistance of high-latitude dust source to EDC" | "4.2 Persistence of high-latitude dust sources to EDC" | S4 |
| KK-31 | p. 8, l. 270 | "by ~763.103 km2" (superscripts as printed) | "by ~763 × 10³ km²" | S4 |
| KK-32 | p. 8, l. 272 | "those from SSA- to EDC" | "those from SSA to EDC" | S4 |
| KK-33 | p. 9, l. 300 | "high-latitude dominance before 14.5 kyr BP reflect a transport regime" | "high-latitude dominance before 14.5 kyr BP reflects a transport regime" | S4 |
| KK-34 | p. 9, l. 301 | "and strong westerlies -a system that" | "and strong westerlies, a system that" | S4 |
| KK-35 | p. 10, l. 311 | "enhanced «wet scavenging»" | "enhanced “wet scavenging”" | S4 |
| KK-36 | p. 10, l. 313 | "from the mid-latitudes of Indian Ocean" | "from the mid-latitudes of the Indian Ocean" | S4 |
| KK-37 | p. 10, l. 322 to 323 | "18% (ranging from 6% to 36%) and 10% (ranging from 3% to 13%)" | "18% (6% to 36%) and 8% (3% to 13%)" (Kok et al., 2021, Table 2, Antarctica: Australia 18 (6 to 36) %, southern Africa 8 (3 to 13) %) | S1 |
| KK-38 | p. 10, l. 329 to 330 | "includes several McMurdo region sites (Section 4.2)" | "includes several McMurdo region sites (Section 2, Table S2)"; also "Dust Source (DS)" to "DS", the term being defined in Section 2 | S4, SD |
| KK-39 | p. 10, l. 336 | "ACR, YD reaching minimum values" | "ACR and YD, reaching minimum values" | S4 |
| KK-40 | p. 10, l. 336 to 337 | "in the mid Holocene, PAT contributions fluctuated widely between 10 and 6 kyr BP" | "in the Early to mid Holocene, PAT contributions fluctuated widely between 10 and 6 kyr BP" (the Early Holocene is defined as 11.7 to 7.5 kyr BP in p. 6, l. 187) | ZF |
| KK-41 | p. 10, l. 338 | "centered ~9 kyrs BP" | "centered at ~9 kyr BP" | S4 |
| KK-42 | p. 10, l. 339 | "is matching well with the SWW intensity proxies" | "matches well with the Southern Westerly Winds (SWW) intensity proxies" | S4 |
| KK-43 | p. 10, l. 339 to 340; p. 11, l. 348 to 349 | "Potrok Aike bog (see Figure 5)"; "(Potrok Aike bog 52°S" | "Laguna Potrok Aike (see Figure 5)"; "(Laguna Potrok Aike, 52°S" (as in the caption and y axis of Fig. 5) | AB |
| KK-44 | p. 10, l. 340 to 341 | "a weakening of South Westerlies Winds (SWW)" | "a weakening of the SWW" | S4 |
| KK-45 | p. 10, l. 341 | "Moreno et al. (2010);" | "Moreno et al., 2010;" | S4 |
| KK-46 | p. 10, l. 342 to 343 | "(Quake and Kaplan, 2017)" | "(Quade and Kaplan, 2017)" | S4 |
| KK-47 | p. 10, l. 346 | "Fires co-emit mineral soil-dust particle" | "Fires co-emit mineral soil-dust particles" | S4 |
| KK-48 | p. 11, l. 354 | "Dust emission from PAP are primarily linked" | "Dust emissions from PAP are primarily linked" | S4 |
| KK-49 | p. 11, l. 365 | "(Gili et al., 2016) ." | "(Gili et al., 2016)." | S4 |
| KK-50 | p. 11, l. 366 | "As far as Australian dust contribution, our model" | "As far as the Australian dust contribution is concerned, our model" | S4 |
| KK-51 | p. 11, l. 367 | "De Deccker et al. (2010)" | "De Deckker et al. (2010)" | S4 |
| KK-52 | p. 11, l. 374 | "(post-7.5 kry" | "(post-7.5 kyr" | S4 |
| KK-53 | p. 11, l. 376 | "the El-Nino-Southern Oscillation (ENSO)" | "the El Niño Southern Oscillation (ENSO)" | S4 |
| KK-54 | p. 12, l. 382 | "an increasing trend in SAF dust contribution to EDC ice core (Figure S4)" | "an increasing trend in SAF dust contribution to the EDC ice core (Figure S3)" | S4, AB |
| KK-55 | p. 12, l. 384 to 385 | "suggesting strengthened dust transport from southern Africa suggesting strengthened dust transport from southern Africa (Stuut et al., 2002)" | "suggesting strengthened dust transport from southern Africa (Stuut et al., 2002)" | S4 |
| KK-56 | p. 12, l. 396 | "but include few substantial inputs" | "but include a few substantial inputs" | S4 |
| KK-57 | p. 12, l. 397 to 398 | "kyr BP (Brook et al., 2011). The intermittent" (opening parenthesis before "~15.4" not closed) | "kyr BP; Brook et al., 2011). The intermittent" | S4 |
| KK-58 | p. 12, l. 399 | "likely reflect their low-frequency, high-magnitude nature of their dust emissions" | "likely reflect the low-frequency, high-magnitude nature of their dust emissions" | S4 |
| KK-59 | p. 12, l. 408 | "due to the limited number samples" | "due to the limited number of samples" | S4 |
| KK-60 | p. 13, l. 426 | "to receive dust from Patagonia dust brought in the mid-" | "to receive Patagonian dust brought in the mid-" | S4 |
| KK-61 | p. 13, l. 427 | "located at the interior of EAP" | "located in the interior of the East Antarctic Plateau (EAP)" | S4 |
| KK-62 | p. 13, l. 428 | "from such mid-latitude air masses incursions" | "from such incursions of mid-latitude air masses" | S4 |
| KK-63 | p. 14, l. 457 | "redirecting large portion of river catchment" | "redirecting a large portion of the river catchments" | S4 |
| KK-64 | p. 16, l. 496 | "Correspondence and requests should be addressed to Si.B." | "Correspondence and requests should be addressed to S. Boxho." | S4 |
| KK-65 | p. 16, l. 501 | "APPENDIX S. SUPPLENTARY DATA. Supplementary data to this article" | "APPENDIX S. SUPPLEMENTARY DATA. Supplementary data to this article are available in the Supplement." | S2, S4 |
| KK-66 | p. 16, l. 536 | "Las glaciaciones cuaternarios en la Patagonia" | "Las glaciaciones cuaternarias en la Patagonia" | S4 |
| KK-67 | p. 17, l. 553 to 560 | De Deckker et al. (2014) listed before De Deckker et al. (2010) | list De Deckker et al. (2010) before De Deckker et al. (2014) | S4 |
| KK-68 | p. 17, l. 565 | "2007. 6. Late quaternary interglacials" | "2007. Late Quaternary interglacials" | S4 |
| KK-69 | p. 20, l. 726 to 729 | "The EDC3 chronology for the EPICA Dome C ice core. Clim. Past." | "The EDC3 chronology for the EPICA Dome C ice core. Clim. Past 3, 485-497." and check the author list against the article | S4 |
| KK-70 | p. 20, l. 748 | "Environùental characterization" | "Environmental characterization" | S4 |
| KK-71 | p. 20, l. 763 | "Holland HD, Turkian KK (eds)" | "Holland, H.D., Turekian, K.K. (Eds.)" | S4 |
| KK-72 | p. 21, l. 770 | "Global Biogeochem. Cycles 25, n/a-n/a." | "Global Biogeochem. Cycles 25" followed by the article number | S4 |
| KK-73 | p. 21, l. 800 | "Sudgen, D. E., McCulloch, R. D." | "Sugden, D.E., McCulloch, R.D." | S4 |
| KK-74 | Figure 2, x axis, p. 26; Figure 3 and Fig. S4, y axes | "0,700 0,705"; "100,00" | "0.700 0.705"; "100" (decimal points, no superfluous decimals) | AB |
| KK-75 | Fig. S5, y axis title, Supplement p. 10 | "PAS EDC Contribution and PSA EDML Contribution ( in %)" | "PSA EDC contribution and PSA EDML contribution (%)" | AB |
| KK-76 | Table S4, rows 1 and 2, Supplement p. 21 | "Epica dome C" | "EPICA Dome C" | S2 |

#### Verification log

| ID | Check | Checked | Values | Result |
|---|---|---|---|---|
| PP-43 | P13 | p. 7, l. 236, "This shift already describes by Gili et al. (2022)" | Gili 2022 abstract: southern African dust signature during warm periods in Southern Hemisphere archives including the margins of the East Antarctic plateau; DustCOMM shares quoted there: SSA 70 %, AUS 20 %, SAF 10 % | no finding |
| PP-44 | P13 | p. 7, l. 238 to 239, Delmonte et al. (2004), LGM isotopes at EDC | abstract reports Sr and Nd of LGM to Holocene transition dust from Dome B, EDC and Komsomolskaia with common South American provenance; Table S4 values 0.7086 and -1.66, 0.7088 and -2.46 | no finding for the LGM values; numbers not checkable in the full text; attribution of the entry in GB-35; Holocene values without source in GB-34 |
| PP-45 | P1 | Modelled Sr and Nd recalculated with Eq. 3 and 4 from Table S3 and the period means, against the EDC values of l. 238 to 240 | Holocene 0.7101 and -4.99 against ~0.710 and -4.51 to -5.68; LGM 0.7083 and -2.61 against ~0.708 and -1.66 to -2.46 | no finding at period-mean level; YD and aggregation in GB-36 |
| PP-46 | P3 | Fig. 2 legend colours against l. 251 to 255; open symbols against Table S4 | filled symbols: Early Holocene, Holocene, YD, ACR, HS1, LGM in red, dark red, yellow, green, cyan, blue as the text describes; all 35 Table S4 positions fall on open circles (overlay) | colours consistent; MIS3 has no own legend entry, covered by "MIS3/LGM" in the text; data origin in GB-34 |
| PP-47 | P13 | p. 9, l. 277 to 279 and p. 10, l. 324 to 328, percentages from Coppo et al. (2022) | abstract confirms unmixing of Nd, Sr and Pb signals for LGM East Antarctic Plateau dust, mostly from southern South America; preprint without unmixing results; journal full text restricted | not checkable; listed under limits |
| PP-48 | P13 | p. 9, l. 283, Koffman et al. (2021) against significant NZ input; p. 8, l. 269 to 271 and p. 9, l. 284 to 285, shelf areas from Vanderstraeten et al. (2023) (~763 x 10³ km², ~62,000 km²) | publisher and repository pages not accessible; Vanderstraeten full text restricted | not checkable; listed under limits |
| PP-49 | P13 | p. 9, l. 286 to 287, Neff and Bertler (2015) "14-32 %" | abstract: New Zealand emissions can contribute significantly; interior East Antarctica limited and highly mixed; no percentages in the abstract; full text not accessible | not checkable; listed under limits |
| PP-50 | P2 | Discussion values against Table S5 | l. 280 to 281 SSA LGM 65.7 + 3.6 + 0.0 = 69.3 (~70), AUS 10.2 (~10); l. 288 EDML NZ 6.2 (~6); l. 289 PAP 3.6 (~4); l. 317 to 319 Holocene 23.1, 11.0, 10.7 and LGM 10.2, 3.6, 6.3; l. 326 60.0 (60); l. 327 23.1 and 10.7 (23, 11); l. 417 to 419 LGM NZ +8.0, PAT -8.0; l. 420 to 421 HS1 differences at most 5.3 | no finding for these values; deviating values in GB-39, GB-40, GB-45 |
| PP-51 | P15 | Discussion figures against Table S5 | l. 222 to 223 LGM order NZ 14.2, AUS 10.2, SAF 6.3, PAP 3.6; l. 294 PAT plus NZ 79.9, lower latitudes 20.1; l. 418 LGM NZ +8.0; l. 420 to 421 HS1 differences at most 5.3 | agree within rounding except as listed in GB-39 |
| PP-52 | P20 | Bases of quoted literature shares | Coppo et al. LGM 64 + 15 + 11 + 5 + 5 = 100; DustCOMM SSA 70 plus or minus 20, AUS 18 (6 to 36) compared with Holocene shares | no finding; SAF value in KK-37 |
| PP-53 | P13 | p. 10, l. 319 to 323, Kok et al. (2021) | Table 2, Antarctica: South America 71 (50 to 90) %, Australia 18 (6 to 36) %, southern Africa 8 (3 to 13) % | SSA and AUS agree; SAF in KK-37. Kok et al. refer to present-day deposition over the whole continent, the comparison value is the EDC Holocene mean (60.0 %), a different spatial and temporal denominator that the text does not mention |
| PP-54 | P21 | Sample size of the ACR and YD comparison with EDML | EDC 8 (ACR) and 9 (YD) against EDML 47 and 27; results disclosed as tentative (l. 407 to 409) | disclosed limitation, not raised again; count in GB-46 |
| PP-55 | P3 | Fig. 4, all 25 bars, against the differences of Table S5 | measured against Table S5: PAT YD +4.96 and +4.7, ACR +6.49 and +6.4, HS1 +3.28 and +3.2, LGM -8.17 and -8.0; AUS LGM +0.53 and +0.5; SAF HS1 -5.27 and -5.3; NZ LGM +8.17 and +8.0; PAP LGM +2.24 and +2.2 (plus or minus 0.15) | no finding for these bars; "Holo" bars and the ACR and YD text in GB-45 |
| PP-56 | P24 | Fig. S2 A, timing of the dust flux decline, against l. 296 and l. 448 to 449 | smoothed nssCa2+ flux: 868 (22 kyr), 463 (20), 556 (19), 583 (18.5), 528 (18), 287 (17), 179 (16), 41 (15), 32 (14.7), 22 (14) (measured) | no finding |
| PP-57 | P15 | Each Conclusion statement assigned to a result | "first high-resolution, continuous and quantitative reconstruction" (l. 472 to 473): Table S1, gap disclosed (l. 113); glacial to interglacial shift (l. 473 to 474): PAT 65.7 to 74.8 % against 49.0 %; PAT dominance in MIS3, LGM, HS1 (l. 474 to 476): 70.3, 65.7, 74.8 %; decoupling from the 18 to 15 kyr flux decline (l. 483 to 484): Fig. S2 A; broad similarity with EDML (l. 484 to 486): HS1 differences at most 5.3 | supported; statements stronger than their basis in GB-33, GB-49, GB-50, GB-52, GB-53 |
| PP-58 | P15, P9 | Outlook proposals | Section 5 (p. 14, l. 472 to p. 15, l. 492) contains no outlook, no proposed studies and no recommendations; no limitations section, the only stated limitation in Section 4 is the small ACR and YD sample size (l. 407 to 409) | no proposal to test; the limitation not carried into Section 5 is part of GB-33 and GB-46 |
| PP-59 | P15 | Core terms and frames of the Introduction in Discussion and Conclusion | aim 1: Sections 3, 4, 5; aim 2: Section 4.1 only; aim 3: Section 4.3; aim 4: Sections 4.4 and 5; westerlies (l. 51 to 52): Section 4.3; isotopic limits (l. 59 to 68): Section 4.1; iron fertilization (l. 37 to 50): not taken up | taken up except as listed in GB-05, GB-51, GB-53 |
| PP-60 | P19 | Provenance class of each core claim | contributions model-generated and named as model output (l. 220 "record", l. 306 "unmixing model"); isotope end-members are secondary means (Table S3); Holocene "measured" isotopes from other cores | model output named; misattribution of the Holocene isotope basis in GB-34; "our data demonstrate" in GB-50 |
| PP-61 | P4 | Numbering of sections, equations, figures and supplementary elements | Sections 1, 2 (one unnumbered subsection), 3, 4, 4.1 to 4.4, 5; Eq. 1 (l. 125), 2 (l. 141), 3 (l. 247), 4 (l. 250); Fig. 1 to 5; Fig. S1 to S5; Tables S1 to S5; no main text tables | no gaps or duplicates; order of Fig. 4 and 5 in GB-42 |
| PP-62 | P4 | Every remaining cross-reference opened at its target | l. 167 Fig. S2 A; l. 183, 205, 215, 217, 221, 307, 338 Fig. 1; l. 191, 216, 218, 281, 295, 318, 326 Table S5; l. 217 to 218 Table S1; l. 244, 252, 257 Fig. 2; l. 246 Table S3; l. 281, 295 Fig. 3; l. 296, 299, 312 Fig. S2; l. 340 Fig. 5; l. 355 Fig. S3; l. 405, 409, 446 Fig. S5; l. 419 Fig. 4; l. 852 Table S1; l. 866 Table S3; l. 873 Fig. S4 | no finding for these; wrong targets in GB-17, GB-34, GB-36, GB-45, GB-48, KK-05, KK-54 |
| PP-63 | P4 | Citations against the reference list in both directions; short forms against entries | 91 entries (pp. 16 to 22); 90 distinct citation strings in main text and captions; 89 entries cited in the main text; 18 distinct sources cited in the supplement; Li et al. (2020) present (p. 19, l. 686 to 689) | mismatches in GB-10, GB-35, GB-41, KK-46, KK-51, KK-73; all other short forms agree |
| PP-64 | P16 | Anomalies in the extracted text checked on the page images | header copyright sign; Eq. 1, 2 and 4 split over several extracted lines but printed as single equations; "763.103 km2" (l. 270) printed with superscripts; wide gaps in reference entries are justified typesetting; isotope superscripts in l. 238 to 240 correct | no finding beyond KK-31 |

## Optional checks

| Area | What it needs | Responsible | Run |
|---|---|---|---|
| DOI resolution | one retrieval per reference entry with DOI | `science-quellenapparat-pruefung` | no |
| Citation style | the name of the style | `science-zitierstil-harvard-ctr` or the style rules of the journal | no |
| AI statement against publisher policy | the target publisher's policy on AI use | this review, on request | no |
| Relation to the authors' own previous work | the authors' previous work | this review, on request | no |
| Journal requirements | the author guidelines of the target journal | this review, on request | no |
| Scientific accuracy | access to the sources of the checked statements and a selection of sections | `science-faktenbeleg-pruefung`, `geo-frage-belegbasiert-klaeren` | no |

## Limits of this review

- Checked version: egusphere-2025-5046.pdf, 29 pages, SHA-256 f598b53d01e375844cfb549eb05b9a3407bb30cae553e603c125d5f14886c722; supplement egusphere-2025-5046-supplement.pdf, 22 pages, SHA-256 759cfa14195948f5772d3d6d696081932424f4296e51c812415527ed3b108ea6.
- Sources not readable in full: Vanderstraeten et al. (2023), Coppo et al. (2022), Delmonte et al. (2004, 2008, 2017) and Neff and Bertler (2015) (abstracts only); Paleari et al. (2019), Koffman et al. (2021) and Delmonte et al. (2007) (not accessible). Statements about these sources beyond their abstracts carry the status inferred or are recorded as not checkable (PP-04, PP-47, PP-48, PP-49).
- Findings with status assumption: 0 of 59 rest on an assumption as their central statement; 14 of 59 contain a partial statement with status assumption, posed as a question to the authors or left open as an alternative.
- Optional checks run: 0 of 6.
- Omitted instances: none.
- Discarded findings: 0. All 94 findings delivered by the six instances had all mandatory fields; none was refuted on re-checking. 35 instance findings were merged into others (94 instance findings became 59), 15 minor corrections were absorbed into findings and 9 duplicated minor corrections merged; 3 verification log entries were merged into others (67 became 64); 5 minor corrections were added from hints outside the checklists after confirmation on the page images (origin ZF).
- The supplement has no line numbers; locations there are given as page, table or figure, row and column. Line numbers in the main text follow the printed margin numbers; values in figures were measured by the figure instance at 300 dpi.
