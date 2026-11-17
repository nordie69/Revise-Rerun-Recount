# Review report: Quantifying Southern Hemisphere dust sources during the Last Glacial-Interglacial Transition using rare earth elements in the EPICA Dome C ice core

| Field | Value |
|---|---|
| Manuscript | Boxho, S., Vanderstraeten, A., Mattielli, N., Laruelle, G. G., Bory, A., Gabrielli, P., Bonneville, S. (2025), Quantifying Southern Hemisphere dust sources during the Last Glacial-Interglacial Transition using rare earth elements in the EPICA Dome C ice core, EGUsphere preprint, doi:10.5194/egusphere-2025-5046, with supplement |
| Checked version | egusphere-2025-5046.pdf, 29 pages, SHA-256 f598b53d01e375844cfb549eb05b9a3407bb30cae553e603c125d5f14886c722; supplement egusphere-2025-5046-supplement.pdf, 22 pages, SHA-256 759cfa14195948f5772d3d6d696081932424f4296e51c812415527ed3b108ea6 |
| Date | 2026-10-18 |
| Language | English |
| Review instances | Segments 1 to 4, Figures, Study design; nacheinander geprüft, nicht kontextgetrennt (all six instances ran sequentially in one context); no instance omitted |
| Note | The review instances ran sequentially in one context, not as separate agents. Line numbers follow the printed margin numbers (every fifth line), counted between them and confirmed on the page images where the count was uncertain. Supplement locations are given as "Supplement p." with the PDF page of the supplement. |

## Summary

The manuscript is a modelling study of a published dataset: it applies the authors' constrained least-squares unmixing algorithm DEPOT (non-negative least squares, MATLAB lsqnonneg) to the UCC-normalised rare earth element (REE) patterns of the EPICA Dome C (EDC) ice core published by Gabrielli et al. (2010), using a database of 217 REE patterns from potential source areas (PSA: Patagonia, Central Western Argentina, Puna-Altiplano, Southern Africa, Australia, New Zealand, Antarctica). Of 294 samples, 279 had complete patterns (13 REE after removal of Gd), and 241 passed a fit-quality threshold of R = 0.67 between measured and modelled pattern; uncertainties are propagated with 2000 Monte Carlo runs per sample. The record spans 2852 to 33699 yr BP. Patagonia supplies 65.7 to 74.8 % of dust in MIS3, LGM and HS1 and 49.0 % in the Holocene, while Australia rises from about 10 % to 23.1 % (Table S5). The reconstruction is compared with Sr and Nd isotope compositions computed from the modelled contributions (Eq. 3 and 4) and with the earlier EDML record of the same algorithm; the shift after about 14.5 kyr BP is attributed to shelf submergence and Patagonian drainage reorganisation.

## Strengths

1. The supplement gives the median contribution of every PSA for every retained sample (Table S1, 241 rows), so that every interval average in Table S5 can be recomputed; the recomputation reproduces all 56 EDC values of Table S5 to 0.1 percentage points, and most numbers in the Results follow from it within rounding (PP-07, PP-08).
2. The isotope cross-check is fully specified by Eq. 3 and 4 and Tables S1 and S3: recomputing it per sample reproduces the extreme modelled points of Figure 2 and gives an LGM mean of 0.7084 and eNd -2.39, close to the two measured EDC LGM values in Table S4 (PP-14); the comparison for the Holocene is limited by the reference data used (GB-20).
3. Analytical and correction-factor uncertainties are propagated sample by sample with 2000 Monte Carlo runs, and the authors state that 5000 runs do not change the results, which makes the per-sample medians less dependent on a single fit (PP-04, PP-05).
4. The PSA end-member database is published with sample names, references, sample types, coordinates and normalised values (Table S2), and Figure 1 is drawn on period boundaries that match the stated chronozones to within 48 yr on the axis, so that the source matrix and the period assignment can be inspected (PP-06, PP-10).

## Weaknesses

1. Whether the unmixing identifies sources is not tested: 13 equations face 217 unknowns, the acceptance criterion is the correlation between the fitted and the measured pattern, its significance level is miscalculated, and three accepted samples fail the stated threshold; the rejection removes only samples younger than 14 kyr. A recovery test with synthetic mixtures of the database patterns, a correct threshold and a sensitivity analysis of the Holocene averages to the rejection would show how far the contributions are determined (GB-09, GB-11, GB-13).
2. The isotope validation, aim (2), compares modelled EDC values with measured Holocene values from Taylor Glacier and Berkner Island, not from EDC, and gives no measure of agreement; the measured EDC Holocene values quoted in the text are not plotted. The comparison should use EDC or Dome C interglacial data and a quantitative misfit (GB-20, GB-03, GB-31).
3. Several result statements do not match the manuscript's own tables and figures: Puna-Altiplano subregion values and onset, the box plots labelled Holocene and Early Holocene, Figure S3 against Table S1, the LGM New Zealand share, derived sums and the EDC minus EDML differences, including a Holocene comparison of different time windows. Each statement should be recomputed from Table S1 and the figures relabelled (GB-15, GB-17, GB-18, GB-23, GB-22, GB-26, GB-28).
4. Reproducibility and traceability are incomplete in several moderate points: code and per-sample model outputs are not available, the conversion of coefficients to percent is not specified, six new source samples have no method, counts and duplicates in the source database disagree with the text, chronologies are mixed, supplementary references are missing, and the attribution of the shift to sea-level rise is stated as demonstrated. A data and code repository, a short methods paragraph per point and a weaker verb in the conclusion would resolve them (GB-30, GB-08, GB-12, GB-07, GB-05, GB-25, GB-29).

## Findings by segment

### Segment 1: Abstract, introduction (p. 1 to 3)

#### Substantive findings

**GB-01 The time span of the record is given in four different ways**

| Field | Content |
|---|---|
| Check | P2 |
| Location | p. 1, l. 18; p. 3, l. 90 to 91; p. 4, l. 109 to 110; p. 6, l. 182; p. 9, l. 304 |
| Quotation | "from 33.6 kyr to 2.8 kyr BP" |
| Concern | The same span appears as 33.7 to 2.9 kyr BP (l. 18, l. 182), 33.6 to 2.8 kyr BP (l. 90 to 91), 2852 to 33699 yr BP (l. 109 to 110) and "until 2.7 kyr BP" (l. 304). Table S1 runs from 2852 to 33699 yr BP, so 33.7 to 2.9 kyr is the rounded form; 33.6 and 2.7 kyr agree with neither. |
| Suggestion | Use 33.7 to 2.9 kyr BP (or 2852 to 33699 yr BP) at l. 90 to 91 and l. 304. |
| Status | verified |
| Severity | minor |
| Source | S3 |

**GB-02 Priority claims are made without a stated literature search**

| Field | Content |
|---|---|
| Check | P28 |
| Location | p. 1, l. 19; p. 3, l. 74 to 76; p. 7, l. 220; p. 14, l. 472 |
| Quotation | "we quantify for the first-time contributions from key Southern Hemisphere dust sources" |
| Concern | The manuscript claims the first quantification (l. 19), the first REE pattern-fitting algorithm (l. 74 to 76), the first continuous quantitative EDC record (l. 220) and the first high-resolution reconstruction (l. 472). No databases, search terms or dates are given. Three own searches found no earlier continuous quantitative EDC record (PP-02), so the claim is not refuted, but it is not documented; earlier qualitative EDC provenance work exists (GB-03). "first-time" in l. 19 is also not an adjective here. |
| Suggestion | Qualify as "to our knowledge" and state the search, or name the precursors and say what is new relative to them; in l. 19 write "for the first time". |
| Status | verified (no search stated); inferred (no counterexample found) |
| Severity | moderate |
| Source | S1 |

**GB-03 A direct precursor on interglacial EDC dust provenance is missing**

| Field | Content |
|---|---|
| Check | P14 |
| Location | p. 3, l. 92 to 93; p. 7, l. 238 to 242 |
| Quotation | "particularly during the Holocene for which there is no consensus" |
| Concern | Delmonte et al. (2010) report the isotopic field of interglacial dust in East Antarctica (Sr about 0.7100, eNd about -6.7 with 2.3 spread, against glacial -1.5 with 2.2 spread) and name East Australia or low-latitude Andean plateaus as possible additional interglacial sources. This anticipates the main Holocene result (more AUS and PAP) and supplies interglacial reference values for the validation in 4.1 (GB-20). The reference list contains Delmonte et al. (2010) in J. Quaternary Sci., not this paper. |
| Suggestion | Cite Delmonte, B., Andersson, P. S., Schöberg, H., Hansson, M., Petit, J. R., Delmas, R., Gaiero, D. M., Maggi, V., Frezzotti, M. (2010) Geographic provenance of aeolian dust in East Antarctica during Pleistocene glaciations: preliminary results from Talos Dome and comparison with East Antarctic and new Andean ice core data, Quaternary Science Reviews 29, 256 to 264, doi:10.1016/j.quascirev.2009.05.010, in l. 92 to 93 and compare its interglacial field with the modelled Holocene values in 4.1. |
| Status | verified |
| Severity | moderate |
| Source | S1 |

#### Minor corrections

| ID | Location | Quotation | Replacement | Source |
|---|---|---|---|---|
| KK-01 | p. 1, l. 15 | "Dust deposits in ice cores provides" | "Dust deposits in ice cores provide" | S4 |
| KK-02 | p. 1, l. 20 | "the Marine isotope 3 (MIS3)" | "Marine Isotope Stage 3 (MIS3)" | S4 |

#### Verification log

| ID | Check | Checked | Values | Result |
|---|---|---|---|---|
| PP-01 | P13 | Sentences with numbers from cited sources and readability of the sources | l. 41 (20 to 40 ppmv, Lambert 2015, 2021), l. 63 (25 times, Delmonte 2008, 2017), l. 238 to 240 (Delmonte 2004 isotopes), l. 267 to 269 (Davies 2020), l. 278 to 279 (Coppo 2022 LGM 64, 15, 11, 5, 5 %), l. 287 (Neff and Bertler 2015, 14 to 32 %), l. 320 to 323 (Kok 2021), l. 325 to 328 (Coppo 2022 Holocene 33, 23, 14, 24 %). Read: Kok 2021 (repository copy), Davies 2020 (abstract), Delmonte 2004 (abstract: Sr and Nd signature of EDC dust used for provenance; individual numbers not in abstract). Not readable: Coppo 2022, Neff and Bertler 2015 (abstract without percentages). | Findings GB-21, GB-24; no finding for the readable remainder; unreadable sources listed under Limits |
| PP-02 | P14, P28 | Searches for work on quantitative EDC dust provenance | Queries: "quantitative dust provenance EPICA Dome C ice core source apportionment mixing model deglaciation Holocene"; "Holocene dust provenance Dome C Australia South America quantitative contribution Sr Nd mixing East Antarctica"; Delmonte 2004 isotope query. Candidates against reference list: Paleari 2019 and Revel-Rolland 2006 listed; Delmonte 2010 QSR not listed; Marino 2008 (G3) not readable. Hits on this manuscript's own pages were not opened. | Finding GB-03; no counterexample to the priority claims |

### Segment 2: Materials and methods, source database (p. 3 to 5, Supplement Figure S1, Table S2)

#### Substantive findings

**GB-04 The stated sample spacing does not match the ages in Table S1**

| Field | Content |
|---|---|
| Check | P6 |
| Location | p. 4, l. 110 to 111; Supplement p. 11 to 15, Table S1 |
| Quotation | "ranging from 60 to 140 years between adjacent samples" |
| Concern | Among the 240 spacings between the 241 ages of Table S1, 77 are shorter than 60 yr and four are 0 yr, because the ages 3559, 10511, 12841 and 28709 each occur twice (confirmed for 3559 on the supplement page image p. 11). Rejected samples can only lengthen spacings, so the shorter ones contradict the statement for the original dataset as well. The longest spacing is 2280 yr (23104 to 25384), which l. 113 explains. Two samples with the same age are either two depth intervals with the same assigned age or a transcription error. |
| Suggestion | Correct the range in l. 110 to 111 and explain the four duplicate ages (depth intervals or errors) in Section 2 and the Table S1 caption. |
| Status | verified |
| Severity | moderate |
| Source | SD |

**GB-05 Two chronologies are combined without comment**

| Field | Content |
|---|---|
| Check | P7, P35 |
| Location | p. 4, l. 111; p. 6, l. 185 to 188; p. 12, l. 404 to 407; Figure 5 |
| Quotation | "The age model follows the EDC3 chronology (Parrenin et al., 2007)." |
| Concern | Sample ages are on EDC3 (l. 111), the period boundaries are taken from Veres et al. (2013), the AICC2012 chronology (l. 188), and the age models of the EDML record (Section 4.4) and of the Potrok Aike record (Figure 5) are not stated. Synchronous changes between cores (l. 444 to 446) and the assignment of samples near 14.7, 12.9 and 11.7 kyr to periods depend on a common time scale. Whether the difference matters here is not shown. |
| Suggestion | State the chronology of every record in Section 2, transfer all records to one chronology (AICC2012) or quantify the offset at the period boundaries, and mark samples that change period. |
| Status | verified (chronologies named); inferred (effect on period assignment) |
| Severity | moderate |
| Source | SD |

**GB-06 Several cross-references point to the wrong table, figure, equation or section**

| Field | Content |
|---|---|
| Check | P4 |
| Location | p. 4, l. 127; p. 5, l. 159; p. 6, l. 183; p. 7, l. 215; p. 10, l. 329 to 330; p. 12, l. 382; p. 13, l. 449 to 450; p. 26, l. 857 to 858; p. 26, l. 865; p. 28, l. 876 |
| Quotation | "(Figure S1, and Table S1)" |
| Concern | The database is in Table S2, not Table S1 (l. 127); "by minimizing Eq. (1)" (l. 159) should cite Eq. (2), since Eq. (1) defines the correction factor; interval averages are in Table S5, Table S1 is per sample (l. 183); South Puna is shown separately only in Figure S3, not Figure 1 (l. 215); the McMurdo sites are described in Section 2, not 4.2 (l. 329 to 330); the SAF subregion trend is in Figure S3, Figure S4 is box plots (l. 382); Figure S5 shows no total deposition and EDML deposition is not shown anywhere, although l. 449 to 450 cite "Figures S2 and S5" for a decline "in both cores"; the Figure 2 caption cites Table S1 for ice core data (Table S4) and Table S4 for PSA isotopes (Table S3); the Figure 4 caption cites Table S4 (Table S5). |
| Suggestion | Correct each reference; for l. 449 to 450 add the EDML deposition record or cite its source. |
| Status | verified |
| Severity | minor |
| Source | S4, AB |

**GB-07 Counts of dust sources per region differ from Table S2, which contains duplicates**

| Field | Content |
|---|---|
| Check | P38, P2 |
| Location | p. 4, l. 131 to 132; Supplement p. 16 to 19, Table S2; Supplement p. 2, Figure S1 |
| Quotation | "Australia (AUS; 106 DS" and "Antarctica (ANT; 5" |
| Concern | Table S2 lists PAT 39, CWA 5, PAP 14, SAF 23, AUS 107, NZ 25, ANT 4 (sum 217); the text gives AUS 106 and ANT 5. Two AUS rows are identical in all 13 values and in their coordinates: Darling26 and Murray29, Darling29 and Murray24, so AUS has 105 distinct patterns. The ANT inset of Figure S1 shows 5 markers (counted at enlargement), Table S2 has 4 ANT rows. Duplicated columns do not change an NNLS fit, but they change "106 DS" and frequency statements per region. The Table S1 caption also calls the 217 dust sources "PSAs". |
| Suggestion | Reconcile the counts in l. 131 to 132 with Table S2, remove or explain the duplicate rows, add the missing ANT sample, and write "217 dust sources (DS)" in the Table S1 caption. |
| Status | verified |
| Severity | moderate |
| Source | S2, S3 |

**GB-08 How the coefficients become percent of total deposition is not specified**

| Field | Content |
|---|---|
| Check | P8 |
| Location | p. 4, l. 137 to 138; p. 5, l. 160 to 165; Supplement p. 13, Table S1, row 10511 |
| Quotation | "The median of each PSA-specific PDF was taken as the best estimate of its contribution" |
| Concern | Eq. 2 imposes non-negativity but no sum-to-one constraint, and the input patterns are UCC-normalised concentrations in ice and in sediment, so the coefficients are not fractions by construction. The text does not say how CDS are normalised to percent, whether PSA medians are re-normalised, and how DS are aggregated to PSA before or after taking medians. In Table S1, 240 of 241 rows sum to 100 within 0.2, but row 10511 sums to 93.5 (0.0 + 0.0 + 3.1 + 6.7 + 49.2 + 29.5 + 5.0 + 0.0). The cfi values and the per-element analytical uncertainties used in the MC runs are not listed. |
| Suggestion | Add to Section 2 the normalisation step, the order of aggregation and median, the cfi values and per-element uncertainties (table), and explain row 10511. |
| Status | verified |
| Severity | moderate |
| Source | SD |

**GB-09 The fit criterion does not show that the unmixing identifies the sources**

| Field | Content |
|---|---|
| Check | P9, P31 |
| Location | p. 5, l. 143 to 144; p. 5, l. 150 to 152; p. 5, l. 168 to 172 |
| Quotation | "a vector of 217 components" |
| Concern | The system has 13 equations and 217 unknowns, so it is underdetermined; non-negativity selects a sparse solution, and different source combinations may fit equally well, particularly among PSA with similar UCC-normalised patterns. Fit quality is measured as the correlation between the measured pattern and the pattern fitted to it, which is not independent of the fit and does not test whether the selected sources are the right ones. The MC spread per PSA, which would show the non-uniqueness, is not reported. The manuscript offers no recovery test. Question to the authors: how often does DEPOT recover known contributions from synthetic mixtures of Table S2 patterns? |
| Suggestion | Add to Section 2 a recovery test: synthetic mixtures of database patterns with 2 to 10 % noise per element (the stated analytical range), reconstructed with the same pipeline, reporting bias and spread per PSA; a leave-one-source-out test; and the interquartile range of each PSA from the MC runs per period in Table S5. |
| Status | verified (dimensions of the system, absence of a recovery test); assumption (how strongly R is inflated by the fit) |
| Severity | major |
| Source | SD |

**GB-10 The announced absolute dust fluxes per source are not reported**

| Field | Content |
|---|---|
| Check | P11 |
| Location | p. 5, l. 166 to 167; p. 6, l. 183 to 184; Supplement p. 4, Figure S2 |
| Quotation | "to convert PSA contributions into absolute dust fluxes (Figure S2)" |
| Concern | Methods announce absolute fluxes per PSA and l. 183 to 184 say contributions are summarised "in % of total deposition and flux". Figure S2 shows only nssCa2+ flux, d18O and deuterium excess; Table S1 and Table S5 give percent only. Absolute fluxes would separate a relative rise of low-latitude sources from a fall of Patagonian flux, which matters for the attribution in 4.4. |
| Suggestion | Add the absolute PSA fluxes as a figure and a column in Table S5, or remove the announcement in l. 166 to 167 and l. 183 to 184. |
| Status | verified |
| Severity | moderate |
| Source | S3 |

**GB-11 The significance threshold for R is miscalculated and not applied consistently**

| Field | Content |
|---|---|
| Check | P1, P5 |
| Location | p. 5, l. 170 to 172; p. 6, l. 174; Supplement p. 11 and 13, Table S1 |
| Quotation | "R ≥ 0.67 corresponds to a statistically significant match" |
| Concern | With 13 REE the correlation has 11 degrees of freedom, not 10. Critical values (scipy, t distribution): two-tailed p = 0.01 requires R of 0.708 at df 10 and 0.684 at df 11; R = 0.67 corresponds to two-tailed p = 0.017 (df 10) or 0.012 (df 11). Under the stated criterion, 19 retained samples with R of 0.70 or less (17 of them Holocene) would fail at df 10, and 9 Holocene samples with R of 0.68 or less at df 11. In addition, Table S1 contains three samples with R = 0.66 (2888, 3267, 10511; page image p. 11), below the threshold of l. 174. |
| Suggestion | Correct the degrees of freedom and the p value in l. 170 to 172 (or the threshold), remove or justify the three R = 0.66 samples, and report how the Holocene averages in Table S5 change. |
| Status | verified (calculation, Table S1) |
| Severity | moderate |
| Source | S3, SD |

**GB-12 Six source samples labelled "this study" have no method description and inconsistent metadata**

| Field | Content |
|---|---|
| Check | P8 |
| Location | Supplement p. 17, Table S2, rows EtoshaL1 to EtoshaL4, SuksesL, Sossusvlei |
| Quotation | "this study" |
| Concern | Six SAF end-members are new measurements, but Section 2 does not describe sampling, size separation, digestion or analysis, and the author contribution names no one for them. Their metadata are inconsistent: all six have location "Etosha Pan", including Sossusvlei (24.76 S) and SuksesL (21.059 S), and all six longitudes are given as W (15.29 to 16.836 W) although the sites are in Namibia (east longitude, as in the neighbouring rows). |
| Suggestion | Describe sampling and analysis of the six samples in Section 2, and correct locations and longitudes in Table S2. |
| Status | verified |
| Severity | moderate |
| Source | SD, S2 |

#### Minor corrections

| ID | Location | Quotation | Replacement | Source |
|---|---|---|---|---|
| KK-03 | p. 3, l. 101 | "ice core camples" | "ice core samples" | S4 |
| KK-04 | p. 4, l. 128 | "subdivised into Patagonia" | "subdivided into Patagonia" | S4 |
| KK-05 | p. 5, l. 145 to 146 | "For any given time step." | delete, or "For any given time step, the vector of 217 components represents" | S4 |

#### Verification log

| ID | Check | Checked | Values | Result |
|---|---|---|---|---|
| PP-03 | P38 | Identifiers across text, tables and figures | DEPOT (l. 88, 100, 259), DIC (l. 108 ff.), PSA abbreviations PAT, CWA, PAP, SAF, AUS, NZ, ANT in text, Tables S1 to S5 and Figures 1 to 4; SSA = PAT + PAP + CWA (l. 280); Figure S3 panels "Sua" and "Namibia" against "Makgadikgadi Complex (including Sua Pan)" and "Namibian coast" (l. 379 to 381) | no finding except GB-07 |
| PP-04 | P10, P19 | Design sketch: aims, design, data classes | Aims (1) to (4) at l. 91 to 98, no separate research questions or hypotheses; study type modelling of a published dataset; 294, 279, 241 samples; 217 DS; contributions are model-generated, PSA patterns and EDC REE primary, isotope reference data secondary; the manuscript states the classes | aim (2) see GB-20, aim (3) see GB-29; otherwise no finding |
| PP-05 | P26, P27, P32, P33, P34, P36, P18, P30, P37 | Remaining design checks | Non-negativity holds in all MC runs (l. 139); MC 2000 runs, 5000 checked (l. 160 to 164); no claim of error-free results; no recollection statements; no reported errors or corrections; three Valdes DS highlighted out of 39 (l. 196 to 197) without list | no finding; the unchecked threshold controlling selection is GB-11 and GB-13 |
| PP-06 | P3 | Figure S1 against Table S2 | ANT inset: 5 markers counted at enlargement; AUS markers overlap and could not be counted; regional labels match Table S2 | see GB-07 |

### Segment 3: Results (p. 6 to 7, Figures 1 and 3, Supplement Table S1, Table S5, Figures S3 and S4)

#### Substantive findings

**GB-13 Rejection by fit quality removes only young samples, and the consequence is not followed through**

| Field | Content |
|---|---|
| Check | P9, P17 |
| Location | p. 6, l. 174 to 179 |
| Quotation | "These excluded samples are all younger than 14 kyr BP" |
| Concern | The authors disclose that the 38 rejected samples are younger than 14 kyr and have low concentrations. Table S1 retains 129 samples younger than 14 kyr, so at least 38 of 167, 22.8 %, of that part of the record were removed, against none older than 14 kyr. The Holocene averages and the variability discussed in 4.3 therefore rest on the dustier samples. The disclosure stands in the Results, not where the threshold is introduced (l. 168 to 172), and its effect on the Holocene averages is not discussed. |
| Suggestion | Move the disclosure to Section 2, give ages and concentrations of the rejected samples, and show in 4.3 whether retained and rejected Holocene samples differ in dust concentration or flux, for example by comparing Holocene averages weighted by flux. |
| Status | verified (counts); inferred (possible bias) |
| Severity | moderate |
| Source | SD |

**GB-14 The SAF level between 9.5 and 12 kyr BP is neither the mean nor the median of Table S1**

| Field | Content |
|---|---|
| Check | P20 |
| Location | p. 6, l. 207 to p. 7, l. 208 |
| Quotation | "drops to minimal levels (~2%) between 9.5 and 12 kyr BP" |
| Concern | Table S1 has 33 samples between 9500 and 12000 yr BP; their SAF mean is 4.32 %, the median 0.3 %, the maximum 49.2 %. Elsewhere the Results use averages (l. 189 to 216), so the reader cannot tell which statistic "~2%" is. |
| Suggestion | State the statistic and its value (mean 4.3 %, median 0.3 %). |
| Status | verified |
| Severity | minor |
| Source | S3 |

**GB-15 Statements on Puna and Altiplano contributions contradict Table S1**

| Field | Content |
|---|---|
| Check | P2 |
| Location | p. 7, l. 212 to 215; p. 11, l. 356 to 360; Supplement p. 11 to 13, Table S1; Supplement p. 6, Figure S3 |
| Quotation | "contributing over 90% at 11.2, 10, 8.6, 6, and 3.5 kyr BP" |
| Concern | Table S1: Altiplano exceeds 90 % only at 8629 (100.0) and 11228 (97.0); the highest values near the other three ages are 75.7 (9957), 58.5 (5967) and 58.0 (6166), and 62.7 (3465). South Puna "remained consistently below 20%" in the Holocene (l. 215), but 8 Holocene samples exceed 20 % (20.2 to 29.1). The YD PAP share is said to come "primarily from the South Puna region" (l. 212), but the YD means are Puna 1.3 % and Altiplano 3.3 % (n = 9). The Altiplano is said to contribute "only after approximately 11.2 kyr BP" and this is tied to the final desiccation of paleolake Coipasa (l. 358 to 360), but Table S1 gives Altiplano 16.6 % and 12.8 % at 12841 yr BP, and the smoothed Altiplano curve in Figure S3 is above zero inside the YD band. The Coipasa argument for aim (3) rests on this onset. |
| Suggestion | Recompute the statements in l. 212 to 215 and l. 356 to 360 from Table S1 and revise the onset and the Coipasa link in 4.3, or explain which quantity (for example MC means instead of medians) the statements use. |
| Status | verified |
| Severity | major |
| Source | S3, AB |

**GB-16 Labels in Figures 1, 2, 4 and 5 are below 6 pt in print size**

| Field | Content |
|---|---|
| Check | P29 |
| Location | Figure 1 (p. 24); Figure 2 (p. 26); Figure 4 (p. 28); Figure 5 (p. 29) |
| Quotation | "0.4" |
| Concern | The quotation is the first tick label of Figure 1. Glyph heights measured on 300 dpi renders (pt = px x 72/300/0.72, about 0.6 pt uncertainty): Figure 1 tick label "0.4" 15 px, 5.0 pt; Figure 5 tick label "0.5" 13 px, 4.3 pt; Figure 2 legend "EDC" 17 px, 5.7 pt; Figure 4 tick label "Holo" 17 px, 5.7 pt. Figures 1 and 5 are clearly below 6 pt. |
| Suggestion | Enlarge tick labels and legends to at least 7 pt at print size. |
| Status | verified |
| Severity | minor |
| Source | AB |

**GB-17 Figure 3 "Holocene" shows the Early Holocene, Figure S4 "Early Holocene" the Late Holocene, and the whiskers are not extremes**

| Field | Content |
|---|---|
| Check | P3 |
| Location | Figure 3 (p. 27), Holocene panel and caption l. 869 to 872; Supplement p. 8, Figure S4, Early Holocene panel; caption Supplement p. 7 |
| Quotation | "Box plots of provenance contributions (in %) of Holocene, and Last Glacial Maximum (LGM)" |
| Concern | Measured Figure 3 Holocene panel (0 at 1432.5 px, 100 at 735.5 px, 0.29 uncertainty): PAT Q1 12.27, median 55.16, Q3 72.96; AUS 2.80, 18.15, 34.22; NZ median 1.08, Q3 7.46. Table S1 Early Holocene (n = 56, exclusive quartiles): PAT 12.3, 55.2, 73.0; AUS 2.8, 18.1, 34.2; NZ 1.1, 7.5; whole Holocene (n = 116): PAT 18.4, 58.6, 73.8. Measured Figure S4 Early Holocene panel (20 at 1618.5 px, 100 at 167.5 px, 0.17 uncertainty): PAT 18.92, 61.65, 80.65; AUS 2.66, 14.62, 29.73, which is the Late Holocene (n = 60: 18.9, 61.7, 80.7; 2.7, 14.6, 29.8). The LGM panel of Figure 3 matches Table S1 (PP-11). The caption says the whiskers "indicate the lower and upper extremes", but points lie beyond them (Holocene NZ 90.4, PAP 100.0). The Figure S4 caption has "Antarctica Cold Reveal", "Heindrich Stadial 1" and "Marine Isotope 3". |
| Suggestion | Relabel Figure 3 as Early Holocene (or replot with 2.8 to 11.7 kyr) and Figure S4 as Late Holocene; state in both captions the whisker rule (1.5 times the interquartile range) and that points beyond it are shown; write "Antarctic Cold Reversal", "Heinrich Stadial 1", "Marine Isotope Stage 3". |
| Status | verified (measurement) |
| Severity | moderate |
| Source | AB |

**GB-18 Figure S3 subregion values do not match Table S1**

| Field | Content |
|---|---|
| Check | P3 |
| Location | Supplement p. 6, Figure S3, Altiplano and Puna panels |
| Quotation | "Evolution of contribution to EDC from subregions of the Puna-Altiplano and Southern Africa PSA" |
| Concern | Measured raw maximum of the Altiplano panel: 66.1 % with about 1 % uncertainty (0 at 792 px, 100 at 67.5 px), near 6.3 kyr; Table S1 gives Altiplano 100.0 % at 8629 and 97.0 % at 11228, and Figure 1 shows PAP spikes near 100 % at these ages. Raw maximum of the Puna panel: 54.9 % near 11.8 kyr; Table S1 Puna maximum is 29.1 % (5850), and between 11 and 12.5 kyr at most 20.2 %. Both figures claim to show the same per-sample contributions. |
| Suggestion | Replot Figure S3 from the values in Table S1, or state what Figure S3 shows (for example MC means of subregions) and why it differs. |
| Status | verified (measurement) |
| Severity | moderate |
| Source | AB |

**GB-19 Table S1 caption gives 279 samples, the table lists 241**

| Field | Content |
|---|---|
| Check | P2 |
| Location | Supplement p. 11, Table S1, caption |
| Quotation | "using 217 PSAs and 279" |
| Concern | Table S1 has 241 rows (2852 to 33699 yr BP), the samples retained after the R threshold (l. 179). The caption also calls the 217 dust sources "PSAs" and has "th DEPOT". |
| Suggestion | Write "Median contribution of each PSA (in %) from the DEPOT model, using 217 dust sources (DS), for the 241 retained DIC samples of the EDC ice core". |
| Status | verified |
| Severity | minor |
| Source | S3, S2, AB |

#### Minor corrections

| ID | Location | Quotation | Replacement | Source |
|---|---|---|---|---|
| KK-06 | p. 6, l. 189 | "It contributes for 65-70%" | "It contributes 65 to 70 %" | S3 |
| KK-07 | p. 6, l. 191 | "during HSI is marked" | "during HS1 is marked" | S3 |

#### Verification log

| ID | Check | Checked | Values | Result |
|---|---|---|---|---|
| PP-07 | P1 | Counts and quotas in Methods and Results | 294 - 15 = 279; 279 - 38 = 241; 241/279 = 86.4 % (text 86 %); mean R in Table S1 = 0.8523 (text 0.852); four samples between 21.7 and 27.3 kyr (22150, 23104, 25384, 25640) | no finding |
| PP-08 | P2 | Table S5 against Table S1, text against Table S5 | Table S5 EDC reproduced to 0.1 from Table S1 means for all 8 periods and 7 PSA (n: Late Holocene 60, Early 56, Holocene 116, YD 9, ACR 8, HS1 27, LGM 40, MIS3 41); l. 189 to 216: PAT 65 to 70 and 75 (70.3, 65.7, 74.8), 69 and 63 (68.9, 63.1), 47 to 51 (47.1, 50.7); AUS 9, 10, 11, 11, about 15, 23 (9.1, 10.2, 11.3, 11.1, 14.5, 23.1); SAF about 5 to 9, 15, about 11 (9.3, 6.3, 4.9, 8.0; 14.6; 10.7); NZ 14, 7, 6.5, 3, 6 (14.2, 7.1, 6.6, 3.3, 5.9); PAP below 4, about 5, 11 (2.2, 3.6, 2.0; 5.2, 4.5; 11.0); l. 307 to 309 and abstract (about 49 %, 65 to 75 %) | no finding except GB-14, GB-15 |
| PP-09 | P11, P21, P22, P23 | Coverage, normalisation, implicit counts, balances | Every PSA in Table S5 for every interval; CWA and ANT omitted from Figure 1 with reason (l. 216 to 218); comparisons between periods use means; row sums of Table S1 (see GB-08) | no finding except GB-10 |
| PP-10 | P3, P24 | Figure 1 axis, period shading and extremes | x ticks 0.4 at 681 px and 3.2 at 1859.5 px (x 10^4 yr BP); gray zones 11710 to 12900, 14700 to 18010 and from 29010 yr (48 yr uncertainty) against 11.7, 12.9, 14.7, 18 and 29 kyr (l. 185 to 188); plotted span 2871 to 33660 yr; 9-point moving average of Table S1: PAT minima 26.4 % (6306), 29.2 % (8508), 20.4 % (10117) against "10, 8.6, and 6.3 kyr BP" (l. 194); AUS maxima 41.8 % (6306), 45.7 % (9902) against l. 205 | no finding |
| PP-11 | P3 | Figure 3 LGM panel against Table S1 | measured PAT 58.90, 65.78, 71.74 and NZ 10.83, 15.49, 18.87 (0.29 uncertainty); Table S1 LGM (n = 40) PAT 58.8, 65.8, 71.7 and NZ 10.8, 15.5, 18.9 | no finding |

### Segment 4: Discussion, conclusion, statements, references (p. 7 to 22, Figures 2, 4, 5, Supplement Figures S2, S5, Tables S3, S4)

#### Substantive findings

**GB-20 The isotope validation compares EDC model values with Holocene measurements from other cores and gives no measure of agreement**

| Field | Content |
|---|---|
| Check | P31, P15 |
| Location | p. 7, l. 227 to 228; p. 7, l. 238 to 240; p. 8, l. 254 to 260; Figure 2; Supplement p. 21, Table S4 |
| Quotation | "the close agreement between our modeled isotopic compositions and those measured in EDC" |
| Concern | Aim (2) is to validate DEPOT against Sr and Nd data. Table S4 (page image) contains measured EDC values only for the LGM (0.7086 and -1.66; 0.7088 and -2.46); all measured Holocene values plotted as open red symbols are from Taylor Glacier (8 values) and Berkner Island (14 values: 0.7090 to 0.7228, eNd -7.33 to -14.71). The EDC Holocene values quoted in l. 238 to 240 (about 0.710, eNd -4.51 to -5.68) are not in Table S4 or Figure 2. Recomputed from Tables S1 and S3 with Eq. 3 and 4, the modelled means are 0.7099 and -4.06 (Late Holocene), 0.7098 and -3.92 (Early Holocene) and 0.7084 and -2.39 (LGM): the LGM agrees with the EDC measurements, the Holocene lies far from the plotted Berkner Island values. "Close agreement" is asserted without a metric, and the agreement "measured in EDC" for interglacials is not shown. |
| Suggestion | Plot and tabulate measured EDC or Dome C interglacial data (l. 238 to 240; Delmonte et al. 2010, see GB-03) as the reference, keep other cores as a separate symbol class, and give a misfit per period (difference of means in 87Sr/86Sr and eNd with their spread). |
| Status | verified |
| Severity | major |
| Source | SD, S4 |

**GB-21 The timing of the maximum of the Patagonian Ice Sheet is not as in Davies et al. (2020)**

| Field | Content |
|---|---|
| Check | P13 |
| Location | p. 8, l. 267 to 269 |
| Quotation | "between ~34 and 29.4 kyr BP" |
| Concern | The abstract of Davies et al. (2020) states that the ice sheet reached its maximum extent by 33 to 28 ka from 38°S to 48°S, and earlier, around 47 ka, south of 48°S; the dimensions 2090 km by 350 km refer to 35 ka. The manuscript gives a different interval and applies the dimensions to the maximum. |
| Suggestion | Write "reached its maximum extent by 33 to 28 ka between 38°S and 48°S and around 47 ka further south; at 35 ka it was 2090 km long and 350 km wide (Davies et al., 2020)". |
| Status | verified |
| Severity | moderate |
| Source | S1 |

**GB-22 Derived sums in Sections 4.2 and 4.3 deviate from Table S5**

| Field | Content |
|---|---|
| Check | P1 |
| Location | p. 9, l. 276; p. 9, l. 293 to 295; p. 10, l. 321; p. 10, l. 326 |
| Quotation | "(here, PAT+AUS is ~77%)" |
| Concern | From Table S5: LGM PAT + AUS = 65.7 + 10.2 = 75.9 (text about 77); LGM PAT + NZ = 65.7 + 14.2 = 79.9 (about 79) and AUS + SAF + PAP = 10.2 + 6.3 + 3.6 = 20.1 (about 21); HS1 PAT + NZ = 74.8 + 7.1 = 81.9 (text 84); Holocene PAT + CWA + PAP = 49.0 + 0.0 + 11.0 = 60.0 (61 in l. 321, 60 in l. 326). Four of the five exceed the rounding tolerance of 0.5 points. |
| Suggestion | Replace by 76, 80, 20, 82 and 60 %. |
| Status | inferred (calculation from Table S5) |
| Severity | minor |
| Source | S3 |

**GB-23 The LGM New Zealand share is given as 11 % against 14 % elsewhere**

| Field | Content |
|---|---|
| Check | P2 |
| Location | p. 9, l. 281 to 282; p. 7, l. 209; Figure 3, LGM panel |
| Quotation | "average NZ contribution (~11%), making it the second-largest dust source to EDC during the LGM" |
| Concern | Table S5 gives an LGM NZ average of 14.2 %, l. 209 says 14 %, and the LGM box in Figure 3 has a measured median of 15.49 %. With 11 %, NZ would be close to AUS (10.2 %), which weakens the "second-largest" statement; with 14.2 % the statement holds. A possible origin is the MIS3 and LGM mean, (9.1 + 14.2)/2 = 11.7 %. |
| Suggestion | Write 14 % in l. 282, or state the interval the 11 % refers to. |
| Status | verified |
| Severity | moderate |
| Source | S3, AB |

**GB-24 The DustCOMM value for Southern Africa combines a central value and a range from different places**

| Field | Content |
|---|---|
| Check | P13 |
| Location | p. 10, l. 312 to 313 |
| Quotation | "10% (ranging from 3% to 13%)" |
| Concern | Kok et al. (2021), Table 2, gives southern Africa 8 % with 3 to 13 %; the abstract says about 10 %. Australia 18 % (6 to 36 %) and South America 71 % (50 to 90 %, here "70 ± 20%") agree with the source. |
| Suggestion | Write "8 % (3 to 13 %)" or "about 10 %" without the range. |
| Status | verified |
| Severity | minor |
| Source | S1 |

**GB-25 Citations without reference entries and entries without citations**

| Field | Content |
|---|---|
| Check | P4 |
| Location | p. 11, l. 365; Supplement p. 16 to 21, Tables S2, S3, S4; p. 18, l. 630 to 632 |
| Quotation | "with the previous Pb isotopic study (Gili et al., 2016)" |
| Concern | Gili et al. (2016) is not in the reference list. The supplement cites Marx et al. (2005), McGowan et al. (2005), Marx and Kamber (2010), Diaz et al. (2018) for most source patterns in Table S2, and Aarons et al. (2017), Bory et al. (2010) and Delmonte et al. (2004a) for the measured isotopes in Table S4; none is in the reference list and the supplement has none of its own. The entry Gaiero, Brunet, Probst and Depetris (2007) is not cited; EPICA Community Members (2006) is cited only in the Figure S2 caption. The sources of 107 AUS, 6 NZ and 4 ANT end-members and of the validation data are therefore not traceable. |
| Suggestion | Add the eight missing references, remove or cite Gaiero et al. (2007), and replace "2004a" by an unambiguous citation. |
| Status | verified |
| Severity | moderate |
| Source | S4 |

**GB-26 The Holocene comparison of EDC and EDML uses different time windows**

| Field | Content |
|---|---|
| Check | P2, P20, P3 |
| Location | p. 12, l. 405 to 407; p. 13, l. 423 to 424; Figure 4, Holo bars; Supplement p. 22, Table S5 |
| Quotation | "PAT dust (-14%) but higher contributions of Australian dust (+12%) than EDML" |
| Concern | The comparison is announced for the overlap 7.5 to 27 kyr BP (l. 406 to 407), and EDML has only an Early Holocene value in Table S5. Measured Holo bars in Figure 4 (10 at 791 px, -10 at 922 px, 0.31 uncertainty): PAT -13.89, AUS 12.21, SAF -0.46. These equal EDC whole Holocene (2.8 to 11.7 kyr) minus EDML Early Holocene: PAT 49.0 - 62.7 = -13.7, AUS 23.1 - 10.8 = 12.3, SAF 10.7 - 11.2 = -0.5. Over the common window (Early Holocene) the differences are PAT -15.6, AUS +14.1, SAF -1.4, NZ +2.6 instead of +0.4. The direction holds, the values and the "Holo" label do not. |
| Suggestion | Use the EDC Early Holocene (7.5 to 11.7 kyr) in Figure 4 and l. 423 to 424, or state in the caption that EDC 2.8 to 11.7 kyr is compared with EDML 7.5 to 11.7 kyr. |
| Status | verified (measurement and calculation) |
| Severity | moderate |
| Source | S3, AB |

**GB-27 The number of EDC samples in the YD is 9, not 7**

| Field | Content |
|---|---|
| Check | P2 |
| Location | p. 12, l. 408 |
| Quotation | "(8 and 7 samples in ACR and YD" |
| Concern | Table S1 has 8 samples in the ACR (12.9 to 14.7 kyr) and 9 in the YD (11.7 to 12.9 kyr: 11779, 11993, 12227, 12477, 12588, 12754, 12841 twice, 12867), the number from which the YD averages in Table S5 are computed. The sentence also lacks "of" ("number samples"). |
| Suggestion | Write "due to the limited number of samples covering those periods in EDC (8 and 9 samples in ACR and YD". |
| Status | verified |
| Severity | minor |
| Source | S3, S4 |

**GB-28 The EDC minus EDML differences for ACR and YD are swapped and the SAF statement fails for the YD**

| Field | Content |
|---|---|
| Check | P2 |
| Location | p. 13, l. 421 to 422; Figure 4, ACR and YD bars |
| Quotation | "dust (+4 and +6.5%) in EDC, primarily at the expense of Southern African and Australian contributions" |
| Concern | Table S5: PAT ACR 68.9 - 62.5 = +6.4, YD 63.1 - 58.4 = +4.7; Figure 4 measured ACR 6.26 and YD 4.73. The order in the text (ACR, YD) gives +4 and +6.5, the reverse. SAF is lower at EDC in the ACR (-4.4; measured -4.43) but higher in the YD (+6.4; measured 6.26), so the YD enrichment in PAT is not at the expense of SAF; AUS is lower in both (-7.4 and -4.5). |
| Suggestion | Write "(+6.5 and +5 %, respectively)" and "primarily at the expense of Australian contributions, and in the ACR also of Southern African ones". |
| Status | verified |
| Severity | moderate |
| Source | S3, AB |

**GB-29 The attribution of the shift to sea-level rise and drainage change is stated as demonstrated**

| Field | Content |
|---|---|
| Check | P15 |
| Location | p. 14, l. 466 to 468; p. 14, l. 480 to 484; p. 1, l. 29 to 31 |
| Quotation | "our data demonstrate that these feedback mechanisms influenced dust deposition" |
| Concern | The results show that the provenance shift at EDC falls in the same interval as at EDML and as the events listed in l. 450 to 452; no record of shelf area, sea level or river reorganisation is compared with the EDC series, and no lag or timing uncertainty is quantified, with 8 and 9 samples in ACR and YD (GB-27) and mixed chronologies (GB-05). The conclusion also states the deposition decline as "due to changing atmospheric transport dynamics" (l. 484), which 4.2 calls "likely" (l. 296). Timing coincidence supports consistency with the mechanism, not a demonstration. |
| Suggestion | Replace "demonstrate" by "are consistent with" in l. 466 and "due to" by "probably due to" in l. 484; to test the attribution, compare the PAT fraction with a time series of exposed Patagonian shelf area on a common chronology, with timing uncertainties of the shift from the MC runs. |
| Status | verified (wording); inferred (strength of evidence) |
| Severity | major |
| Source | S4 |

**GB-30 The code and data statement does not cover the code and several data sources**

| Field | Content |
|---|---|
| Check | P12 |
| Location | p. 16, l. 494 to 496 |
| Quotation | "Additional data related to the paper may be requested from the authors." |
| Concern | Data sources named in Methods and their availability: EDC REE dataset (published, Gabrielli et al. 2010); source database (Table S2); per-sample medians (Table S1); not available: the DEPOT MATLAB code (the heading says CODE/DATA, the text says nothing about code), the list and ages of the 15 incomplete and 38 rejected samples, the cfi values and per-element uncertainties, the MC distributions per sample and PSA, the absolute fluxes (l. 167), the EDML per-sample values behind Table S5 and Figures 4 and S5. The data concern no persons, so availability on request needs a reason. |
| Suggestion | Deposit code and per-sample outputs (all 279 samples with R, MC quantiles per PSA) in a public repository with a DOI and cite it in l. 494 to 496. |
| Status | verified |
| Severity | moderate |
| Source | S2 |

**GB-31 Figure 2 shows one modelled point per sample, the text describes one per interval, and the legend is ambiguous**

| Field | Content |
|---|---|
| Check | P3, P29 |
| Location | Figure 2 (p. 26); p. 8, l. 244 to 245; p. 8, l. 251 to 253 |
| Quotation | "For each time interval of the LGIT, the" |
| Concern | The text describes the calculation per time interval, but Figure 2 shows many filled points per period; recomputation per sample from Tables S1 and S3 reproduces the extremes (YD 0.7274 and eNd -17.87, the single yellow point near 0.7275 and -18). The legend has "EDC Early Holocene" and "EDC Holocene" (presumably Late Holocene) and no MIS3 entry, although l. 251 includes "end of MIS3/LGM" in the blue symbols. |
| Suggestion | Write "For each sample" in l. 244 to 245 (or plot interval means), and label the legend "Late Holocene" and "MIS3 and LGM". |
| Status | verified |
| Severity | minor |
| Source | AB |

**GB-32 Figure 5 has no x axis title and an unexplained shaded band, and the shading of panel B is offset**

| Field | Content |
|---|---|
| Check | P29, P3 |
| Location | Figure 5 (p. 29), caption l. 880 to 882 |
| Quotation | "Comparison of the contribution of Patagonian dust (PAT) to EDC ice core (A) and (B) the" |
| Concern | The x axis carries neither quantity nor unit nor the factor 10^4 shown in Figure 1. A blue band with dashed edges at 7968 and 11430 yr (45 yr uncertainty; ticks 0.5 at 685 px and 3.0 at 1788.5 px) is not explained; l. 340 mentions 11 to 8 kyr. The gray zones of panel B are offset from those of panel A: YD upper edge 13030 against 12895 yr, HS1 lower edge 14780 against 14707 yr. The chronology of the Potrok Aike record is not stated. |
| Suggestion | Add "Time (yr BP)" with the factor, explain the blue band in the caption, align the zones of panel B and name the age model of the Potrok Aike record. |
| Status | verified (measurement) |
| Severity | minor |
| Source | AB |

**GB-33 Figure S2 axes lack units**

| Field | Content |
|---|---|
| Check | P29 |
| Location | Supplement p. 4, Figure S2, panels A and B |
| Quotation | "Non Sea Salt Calcium (nssCa2+) flux in EDC ice core" |
| Concern | Panel A is labelled "nssCa2+ flux" without unit (l. 166 gives µg m⁻² yr⁻¹), panel B "δ18O" without per mil, and panel B has no period shading although panels A and C have it. |
| Suggestion | Add units to both axes and the period shading to panel B. |
| Status | verified |
| Severity | minor |
| Source | AB |

#### Minor corrections

| ID | Location | Quotation | Replacement | Source |
|---|---|---|---|---|
| KK-08 | p. 7, l. 236 | "This shift already describes by" | "This shift, already described by" | S4 |
| KK-09 | p. 8, l. 246 | "(Table S3, e.i. Eq.3)" | "(Table S3, i.e. Eq. 3)" | S4 |
| KK-10 | p. 8, l. 249 | "the mean isotopic signatures is represents by" | "the mean isotopic signature is represented by" | S4 |
| KK-11 | p. 8, l. 261 | "Persistance of high-latitude dust source" | "Persistence of high-latitude dust sources" | S4 |
| KK-12 | p. 8, l. 270 | "by ~763.10" (with superscript 3, km²) | "by about 763 × 10³ km²" | S4 |
| KK-13 | p. 9, l. 302 | "until the onset of the LGIT" | "until about 14.5 kyr BP" (LGIT denotes the whole record in l. 90) | S4 |
| KK-14 | p. 10, l. 334 | "(Speirs et al., 2001)" | "(Speirs et al., 2010)" | S4 |
| KK-15 | p. 10, l. 342 | "(Quake and" | "(Quade and" | S4 |
| KK-16 | p. 11, l. 367 | "De Deccker et al. (2010)" | "De Deckker et al. (2010)" | S4 |
| KK-17 | p. 11, l. 374 | "(post-7.5 kry" | "(post-7.5 kyr" | S4 |
| KK-18 | p. 12, l. 384 to 385 | "suggesting strengthened dust transport from southern Africa suggesting strengthened dust transport from southern Africa" | "suggesting strengthened dust transport from southern Africa" (repetition confirmed on page image p. 12) | S4 |
| KK-19 | p. 12, l. 397 to 398 | "(~15.4" | close the parenthesis: "(about 15.4 to 13.6, 11.5 to 8.4, 5.5 to 4.0 kyr BP; Brook et al., 2011)" | S4 |
| KK-20 | p. 12, l. 399 | "likely reflect their low-frequency, high-magnitude nature of their dust emissions" | "likely reflect the low-frequency, high-magnitude nature of their dust emissions" | S4 |
| KK-21 | p. 13, l. 439 | "(De Deccker et al., 2019;" | "(De Deckker, 2019;" | S4 |
| KK-22 | p. 16, l. 497 | "P.B performed the measurements" | name the author with initials matching the author list (no author has the initials P.B.) | S4 |
| KK-23 | p. 16, l. 501 | "APPENDIX S. SUPPLENTARY DATA. Supplementary data to this article" | "SUPPLEMENT. The supplement related to this article is available online." | S4 |
| KK-24 | p. 16, l. 528 | "471\uc0\u8211{}501" | "471 to 501" with an en rule; the same RTF codes are visible in 17 further entries on p. 17 to 22 (page image p. 16) | S4 |
| KK-25 | p. 20, l. 729 | "chronology for the EPICA Dome C ice core. Clim. Past." | add volume, pages and DOI of the entry | S4 |
| KK-26 | p. 20, l. 748 | "Environùental characterization" | "Environmental characterization" | S4 |
| KK-27 | p. 20, l. 763 | "Turkian KK (eds)" | "Turekian KK (eds)" | S4 |
| KK-28 | p. 21, l. 800 | "Sudgen, D. E." | "Sugden, D. E." | S4 |
| KK-29 | Supplement p. 10, Figure S5, y axis | "PAS EDC Contribution and PSA EDML Contribution ( in %)" | "PSA contribution at EDC and EDML (%)" | AB |

#### Verification log

| ID | Check | Checked | Values | Result |
|---|---|---|---|---|
| PP-12 | P4 | Numbering and citation lists | Sections 1 to 5 and 4.1 to 4.4 without gaps; Eq. 1 to 4; Figures 1 to 5 each cited (first at l. 183, 244, 281, 405, 340); Figures S1 to S5 and Tables S1 to S5 cited; 94 author and year pairs from text and captions held against the list | no finding except GB-06, GB-25, KK-14 to KK-16, KK-21, KK-28 |
| PP-13 | P15 | Conclusion and aims against results | l. 474 to 477 against Table S5 (PAT 65.7 to 74.8 in MIS3 to HS1); l. 477 to 480 (AUS, PAP, SAF rise: 10.2 to 23.1, 3.6 to 11.0, 6.3 to 10.7); l. 485 to 487 against Table S5 and Figure 4; l. 488 to 490 against GB-15; aims (1) to (4) taken up in the conclusion, 4.1, 4.2 and 4.3, 4.4; no outlook proposals (no proposed studies or rules) | no finding except GB-15, GB-29 |
| PP-14 | P31 | Recomputation of Eq. 3 and 4 per sample from Tables S1 and S3 | means per period: Late Holocene 0.7099 and -4.06, Early Holocene 0.7098 and -3.92, YD 0.7101 and -3.65, ACR 0.7083 and -2.28, HS1 0.7076 and -1.32, LGM 0.7084 and -2.39, MIS3 0.7083 and -3.17; LGM measured at EDC 0.7086 and -1.66, 0.7088 and -2.46 | method reproducible; see GB-20 |
| PP-15 | P3 | Figure 4 bars for HS1 and LGM against Table S5 | PAT HS1 3.05 and LGM -8.09 (Table S5: 3.2, -8.0); AUS HS1 1.99 (1.9); SAF HS1 -5.19 and LGM -2.75 (-5.3, -2.7) | no finding |
| PP-16 | P29, P24 | Register of figures and dated features | Fig. 1 p. 24 (caption p. 25, l. 851 to 854), Fig. 2 p. 26 (l. 857 to 866), Fig. 3 p. 27 (l. 869 to 873), Fig. 4 p. 28 (l. 875 to 876), Fig. 5 p. 29 (l. 880 to 882), Figures S1 to S5; all raster images; period boundaries in Figures 1, 5, S2, S3, S5 compared; Figure 3 is a results figure cited only in the Discussion | no finding except GB-16 to GB-18, GB-31 to GB-33 |
| PP-17 | P16 | Uniformity of reference list | mixed formats, for example Ding et al. (l. 584 to 585), Gaiero et al. 2013 (l. 633 to 636), Yang et al. (l. 844 to 846); citation style itself is an optional check | no finding |

## Optional checks

| Area | What it needs | Responsible | Run |
|---|---|---|---|
| DOI resolution | one retrieval per reference with DOI | `science-quellenapparat-pruefung` | no |
| Citation style | the name of the style | `science-zitierstil-harvard-ctr` or style rules of the journal | no |
| AI statement against publisher policy | the AI policy of the target publisher | this review, on request | no |
| Relation to own earlier work | the authors' earlier work (for example Vanderstraeten et al. 2023) | this review, on request | no |
| Journal requirements | the author guidelines of the target journal | this review, on request | no |
| Scientific accuracy | access to the sources of the checked statements and a choice of sections | `science-faktenbeleg-pruefung`, `geo-frage-belegbasiert-klaeren` | no |

## Limits of this review

- Checked version: egusphere-2025-5046.pdf, 29 pages, SHA-256 f598b53d01e375844cfb549eb05b9a3407bb30cae553e603c125d5f14886c722, with supplement (22 pages, SHA-256 759cfa14195948f5772d3d6d696081932424f4296e51c812415527ed3b108ea6)
- Sources not readable: Coppo et al. (2022), final paper (preprint page without numbers); Neff and Bertler (2015), full text (abstract without percentages); Delmonte et al. (2004), full text (abstract only); Marino et al. (2008); Kok et al. (2021) publisher page (rate limited; read in a repository copy)
- Findings with status assumption: 0 of 33 (GB-09 has one sub-statement with status assumption)
- Optional checks run: 0 of 6
- Omitted instances: none; all six instances ran sequentially in one context
- Discarded findings: 0
