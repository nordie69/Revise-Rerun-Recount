# Review report: Quantifying Southern Hemisphere dust sources during the Last Glacial-Interglacial Transition using rare earth elements in the EPICA Dome C ice core

| Field | Value |
|---|---|
| Manuscript | Boxho, S., Vanderstraeten, A., Mattielli, N., Laruelle, G. G., Bory, A., Gabrielli, P., Bonneville, S. (2025): Quantifying Southern Hemisphere dust sources during the Last Glacial-Interglacial Transition using rare earth elements in the EPICA Dome C ice core. EGUsphere preprint, https://doi.org/10.5194/egusphere-2025-5046, with supplement |
| Checked version | egusphere-2025-5046.pdf, 29 pages, SHA-256 f598b53d01e375844cfb549eb05b9a3407bb30cae553e603c125d5f14886c722; supplement egusphere-2025-5046-supplement.pdf, 22 pages, SHA-256 759cfa14195948f5772d3d6d696081932424f4296e51c812415527ed3b108ea6 |
| Date | 2026-10-18 |
| Language | English |
| Review instances | Segments 1 to 4, figures (AB), study design (SD); nacheinander geprüft, nicht kontextgetrennt: all six instances ran one after another in one context, not as separate agents; no instance omitted |
| Note | Line numbers are the printed margin numbers; the reading script did not detect them, so they were reconstructed from the numbered lines and confirmed at the page images. Figures were measured at 300 dpi. |

## Summary

The manuscript applies an existing constrained least-squares unmixing model (DEPOT, MATLAB lsqnonneg) to a published set of rare earth element (REE) patterns of dust in the EPICA Dome C (EDC) ice core (Gabrielli et al., 2010) to quantify the contributions of seven Southern Hemisphere potential source areas (PSA) between 33.7 and 2.9 kyr BP. Each of 279 UCC-normalised 13-element patterns (Gd removed) is fitted as a non-negative combination of 217 dust source patterns (Table S2); 2000 Monte Carlo runs per sample propagate analytical and correction-factor uncertainty, and 241 samples with median correlation R ≥ 0.67 are retained. Patagonia dominates during MIS3, LGM and HS1 (65.7 to 74.8 %), and after about 14.5 kyr BP the shares of Australia, Southern Africa and the Puna-Altiplano rise, giving Holocene averages of 49.0 % (PAT), 23.1 % (AUS), 11.0 % (PAP) and 10.7 % (SAF). Modelled Sr and Nd mixtures are compared with literature isotope data, and the EDC record is compared with the EDML record of Vanderstraeten et al. (2023); the shift is attributed to shelf submergence and drainage reorganisation in Patagonia.

## Strengths

1. The per-sample results are published (Table S1, 241 rows), and the period averages of Table S5 can be recomputed from them exactly, so every period statement in the Results can be checked by a reader (PP-13, PP-14).
2. The full source database of 217 UCC-normalised patterns with locations and references is given (Table S2), which makes the end-member basis of the unmixing inspectable and allowed this review to test the fit criterion with the authors' own matrix (PP-05, GB-08).
3. The REE shares are translated into Sr and Nd mixtures with explicit equations (Eq. 3 and 4) and tabulated end members (Table S3); recomputing them gives LGM and Holocene values close to the EDC isotope values cited in the text, which offers an independent check of the apportionment at least for these two periods (PP-08, GB-17).
4. Exclusions and gaps are disclosed with numbers (15 incomplete patterns, 38 samples below the R threshold, all younger than 14 kyr, a gap of four samples between 21.7 and 27.3 kyr BP), and the figures place periods and dated extremes where the data and definitions put them (PP-07, PP-15, PP-19, PP-20).

## Weaknesses

1. The quality criterion and the uncertainty of the record are not established: R ≥ 0.67 is derived with wrong degrees of freedom, ignores that the pattern is fitted with up to 217 coefficients (random patterns pass in 24 to 40 % of cases), and is not applied consistently; the Monte Carlo spread is never reported, and the larger Holocene variability is not separated from noise at low concentrations. Suggestion: derive the threshold from a null distribution with the actual database, report per-sample percentiles, and test with synthetic degraded mixtures (GB-08, GB-07, GB-24).
2. The EDC to EDML comparison rests on an undocumented basis: the EDML values in Table S5 differ from the published record, the two cores were fitted with different configurations, the Holocene compares unequal windows, and the ACR and YD differences are misreported. Suggestion: rerun EDML with the present configuration and recompute Section 4.4 and Figure 4 on identical windows (GB-22, GB-29, GB-28, GB-09).
3. Several interpretations do not follow from the data shown: the isotope validation uses mostly non-EDC data and no misfit, relative shares are read as increased emissions although the total flux fell, and the Puna and Altiplano statements, including the onset date linked to the Coipasa desiccation, contradict Table S1 and Figure S3. Suggestion: report absolute PSA fluxes, quantify the isotope misfit per period with EDC data, and rebuild the subregion record from one consistent series (GB-17, GB-30, GB-11).
4. Traceability is limited in many places of moderate weight: the data and code statement covers few of the data sources, steps of the normalisation and the new source patterns are not described, eight cited works lack entries, and several literature statements differ from their sources; conclusions overstate what the data demonstrate. Suggestion: deposit code and intermediate data, complete Section 2 and the reference list, and align the cited statements and the conclusion with the evidence (GB-34, GB-04, GB-02, GB-27, GB-15, GB-19, GB-32, GB-33).

## Findings by segment

### Segment 1: Abstract, introduction (p. 1 to 3, l. 1 to 98)

#### Substantive findings

**GB-01 The priority claims are not backed by a described literature search**

| Field | Content |
|---|---|
| Check | P28 |
| Location | p. 1, l. 19; p. 7, l. 220; p. 12, l. 403; p. 14, l. 472 |
| Quotation | "we quantify for the first-time contributions from key Southern Hemisphere dust sources" |
| Concern | The manuscript claims the first quantification (p. 1, l. 19 to 20), the "first continuous and quantitative record" at EDC (p. 7, l. 220), that the EDML record is "The only continuous and quantitative dust provenance record in EA" (p. 12, l. 403) and the "first high-resolution, continuous and quantitative reconstruction" (p. 14, l. 472). No databases, search terms or date of search are given. The manuscript itself reports quantitative source shares for East Antarctic LGM dust from Coppo et al. (2022) (p. 9, l. 277 to 279), so "for the first-time" in the abstract is at least ambiguous. Three searches of this review found no other continuous quantitative EDC record (PP-02). |
| Suggestion | Restrict the claims to what they cover, for example "the first continuous, sample-resolved, REE-based quantitative record at EDC" at p. 1, l. 19 (written "for the first time"), and either describe the search basis in Section 1 or drop "only" at p. 12, l. 403. |
| Status | verified |
| Severity | moderate |
| Source | S1 |

#### Minor corrections

| ID | Location | Quotation | Replacement | Source |
|---|---|---|---|---|
| KK-01 | p. 1, l. 15 | "Dust deposits in ice cores provides" | "Dust deposits in ice cores provide" | S1 |
| KK-02 | p. 1, l. 20 | "Marine isotope 3 (MIS3)" | "Marine Isotope Stage 3 (MIS3)" | S1 |
| KK-03 | p. 3, l. 90 to 91 | "from 33.6 kyr to 2.8 kyr BP" | "from 33.7 to 2.9 kyr BP" (as in the abstract, p. 1, l. 18, and p. 6, l. 182) | S3 |

#### Verification log

| ID | Check | Checked | Values | Result |
|---|---|---|---|---|
| PP-01 | P13 | Reproduction of Vanderstraeten et al. (2023) in the introduction (p. 3, l. 77 to 87) | source abstract (marineinfo.org/doc/publication/382930): Patagonian share below 50 % on average after about 14.5 kyr BP, early Holocene variable with about 50 % | no finding for the introduction; for Table S5 see GB-22 |
| PP-02 | P14 | Searches for work preceding or contradicting the contribution (3 queries) | "quantitative dust provenance EPICA Dome C Holocene source apportionment mixing model contributions Australia Patagonia ice core"; "Aarons Taylor Glacier dust provenance last glacial-interglacial transition Sr Nd isotopes East Antarctica"; "Vallelonga 2010 lead isotopic compositions EPICA Dome C ice core Southern Hemisphere potential source areas"; candidates: Aarons et al. (2017), cited in Table S4 without entry (GB-27); Vallelonga et al. (2010), absent (GB-25) | one proposal (GB-25) |
| PP-03 | P28 | Gap statement for the Holocene (p. 3, l. 91 to 93) | backed by three citations (Paleari et al., 2019; Coppo et al., 2022; Delmonte et al., 2007) | no finding |
| PP-04 | P18 | Principles stated in the introduction applied to the manuscript | REE are said to allow "higher temporal resolution and precision" (p. 3, l. 71 to 72); precision is not reported (GB-07) | covered by GB-07 |

### Segment 2: Materials and methods (p. 3 to 5, l. 99 to 172; Figures S1, S2; Table S2)

#### Substantive findings

**GB-02 Six source patterns labelled "this study" have no method, and Table S2 contains apparent transcription errors**

| Field | Content |
|---|---|
| Check | P6, P8 |
| Location | p. 4, l. 104 to 105; Table S2 (rows EtoshaL1 to EtoshaL4, SuksesL, Sossusvlei, Darling12, Kuiseb2inf5) |
| Quotation | "the REE patterns measured in the EDC ice core and literature reported patterns from known potential source areas (PSA)" |
| Concern | Six SAF patterns in Table S2 are labelled "this study"; no sampling, size separation (5 µm fraction), digestion or analysis is described anywhere. Their coordinates are given as west longitudes (for example "15,97 W") although the sites are in Namibia, and Sossusvlei (24.76 S) is listed under location "Etosha Pan". Darling12 is at 31°2'49.20"S 138°17'6.00"E, while Darling11 has the same latitude at 144°17'6.00"E. Kuiseb2inf5 has Dy = 6.200013 against Tb 2.692922 and Ho 2.149792 in the same row (Kuiseb1inf5: Dy 2.376464), a spike of about 2.3 times its neighbours that the least-squares fit can use to match Dy. |
| Suggestion | Describe sampling and analysis of the six new patterns in Section 2 or the supplement, correct the coordinates in Table S2, check the Dy value of Kuiseb2inf5 against the original data and refit if it is an error. |
| Status | verified (table entries); inferred (that the Dy value is an error) |
| Severity | moderate |
| Source | SD |

**GB-03 The stated sample spacing of 60 to 140 years is contradicted by Table S1**

| Field | Content |
|---|---|
| Check | P6 |
| Location | p. 4, l. 110 to 111; Table S1 |
| Quotation | "with an average temporal resolution of approximately 100 years, ranging from 60 to 140 years between adjacent samples" |
| Concern | Among the 241 retained samples, 77 of 240 adjacent intervals are shorter than 60 yr (for example 2852 to 2888 yr: 36 yr; duplicated ages, GB-14, give 0 yr). Table S1 is a subset of the 294 samples, so the spacing in the full set is at most as large. |
| Suggestion | Replace at p. 4, l. 110 to 111 by the actual minimum and maximum spacing of the 294 samples. |
| Status | verified |
| Severity | minor |
| Source | SD |

**GB-04 Key steps of the apportionment cannot be rebuilt from the text**

| Field | Content |
|---|---|
| Check | P8 |
| Location | p. 4, l. 119 to 124; p. 5, l. 160 to 161; Table S1 |
| Quotation | "the ensuing CDS results (in % of total deposition) generate a probability density function (PDF) for every DS which were subsequently aggregated by PSA" |
| Concern | (1) lsqnonneg does not constrain the coefficients to sum to one, and DIC concentrations and UCC-normalised source patterns differ in scale; how CDS become "% of total deposition" is not stated. (2) Medians of PSA distributions need not sum to 100 %, yet 240 of 241 rows of Table S1 sum to 100 ± 0.1 %, which implies an undisclosed renormalisation. (3) The correction factors cf_i, their "variability" and the distributions sampled in the Monte Carlo runs are not given. (4) The statement that 5000 runs "does not significantly affect the results" (p. 5, l. 163 to 164) is not documented; the computation cost argument has no measure. |
| Suggestion | State in Section 2 the normalisation of CDS, the order of aggregation, medians and renormalisation, list cf_i with uncertainties in a supplement table, and give the comparison of 2000 and 5000 runs in numbers. |
| Status | verified |
| Severity | moderate |
| Source | SD |

**GB-05 The number of dust sources per PSA in the text differs from Table S2**

| Field | Content |
|---|---|
| Check | P2 |
| Location | p. 4, l. 131 to 133; Table S2 |
| Quotation | "Australia (AUS; 106 DS, predominantly from the central and southeastern regions)" |
| Concern | Counting the rows of Table S2 with 13 REE values gives PAT 39, CWA 5, PAP 14, SAF 23, AUS 107, NZ 25, ANT 4, total 217. The text gives AUS 106 and ANT 5 (p. 4, l. 131 to 133). The totals agree, so either one source is assigned to the wrong PSA or an ANT row is missing. |
| Suggestion | Correct the counts at p. 4, l. 131 to 133 to AUS 107 and ANT 4, or add the missing ANT row to Table S2. |
| Status | verified |
| Severity | minor |
| Source | S3 |

**GB-06 Several objects carry different names across text, figures and supplement**

| Field | Content |
|---|---|
| Check | P38 |
| Location | p. 4, l. 137; Table S1 caption (supplement p. 11); p. 6, l. 191; p. 6, l. 199; p. 7, l. 213; p. 11, l. 358; p. 10, l. 338; p. 11, l. 374; Figure S3 panel labels; Figure S4 caption |
| Quotation | "using 217 PSAs and 279 DIC from EDC ice core REE patterns" |
| Concern | (1) The 217 columns of the model are "dust sources (DS)" in the text (p. 4, l. 137; p. 5, l. 143 to 144) but "217 PSAs" in the Table S1 caption, where PSA otherwise means one of seven regions; the caption also names 279 DIC although the table lists the 241 retained samples. (2) Heinrich Stadial 1 appears as "HS1", "HSI" (p. 6, l. 191) and "Heindrich Stadial 1" (Figure S4 caption, which also has "Antarctica Cold Reveal" and "Marine Isotope 3"). (3) The South Altiplano is "South Altiplano" (p. 7, l. 213), "Southern Altiplano" (p. 11, l. 358), "S-Altiplano" (Figure 2, Table S3) and "Altiplano" (Table S1, Figure S3); South Puna is "Puna" in Table S1 and Figure S3. (4) The SAF subregions are "Makgadikgadi Complex (including Sua Pan)" and the "Namibian coast" in the text (p. 11, l. 379 to 381) but "Sua" and "Namibia" in Figure S3. (5) "LREE (low rare earth elements)" (p. 6, l. 199) for light REE. (6) "kyr", "kyrs" (p. 10, l. 338) and "kry" (p. 11, l. 374). |
| Suggestion | Use one name per object: in the Table S1 caption "based on the DEPOT model results, using 217 dust sources (DS), for the 241 of 279 DIC samples that passed the R threshold"; "HS1" at p. 6, l. 191; in the Figure S4 caption "Antarctic Cold Reversal (ACR), Heinrich Stadial 1 (HS1), Marine Isotope Stage 3 (MIS3)"; one subregion name matching Table S1 and Figure S3; "light rare earth elements"; "kyr". |
| Status | verified |
| Severity | minor |
| Source | S2, S4, S3, AB |

**GB-07 Announced uncertainty propagation and absolute fluxes are not reported**

| Field | Content |
|---|---|
| Check | P11 |
| Location | p. 5, l. 153 to 156; p. 5, l. 166 to 167; p. 6, l. 183 to 184; Table S1; Table S5; Figure 1 |
| Quotation | "to convert PSA contributions into absolute dust fluxes (Figure S2)" |
| Concern | Section 2 announces 2000 Monte Carlo runs per sample to "evaluate the impact of uncertainties" and a conversion of PSA shares into absolute fluxes, and p. 6, l. 183 to 184 says that Figure 1 and Table S1 give contributions "in % of total deposition and flux". Table S1, Table S5 and Figures 1, 3 and 4 show medians or averages only; no spread, percentile or interval appears for any sample or period, and no PSA flux appears anywhere (Figure S2 shows nssCa flux, δ18O and deuterium excess only). Statements such as "significantly increased contributions" (p. 7, l. 235) and "significantly larger variability" (p. 9, l. 306) cannot be checked. The sentence at p. 6, l. 183 also refers to Table S1 for interval values, which are in Table S5. |
| Suggestion | Add Monte Carlo percentiles (for example 16th and 84th) per sample to Table S1 and per period to Table S5, show them as bands in Figure 1, add PSA fluxes as table and figure, and change p. 6, l. 183 to 184 to "Figure 1 and Table S5 summarize the relative contributions (in % of total deposition)" unless fluxes are shown. |
| Status | verified |
| Severity | moderate |
| Source | S3, S4 |

**GB-08 The R threshold is not a significance test of the fit and is not applied consistently**

| Field | Content |
|---|---|
| Check | P8, P5, P27 |
| Location | p. 5, l. 170 to 172; p. 6, l. 174; Table S1 (column R) |
| Quotation | "We determined that R ≥ 0.67 corresponds to a statistically significant match" |
| Concern | (1) With 13 REE per pattern (p. 4, l. 117) a Pearson test has 11 degrees of freedom, not the stated 10. Critical r, two-tailed, p 0.01: 0.708 (df 10), 0.684 (df 11); for r = 0.67 the p value is 0.017 (df 10) or 0.012 (df 11). (2) The test assumes two independent series, but the modelled pattern is fitted to the observed one with up to 217 non-negative coefficients, which inflates R. Fitting 2000 structureless random 13-element patterns with the 217 patterns of Table S2 by non-negative least squares gives a median R of 0.627; 40 % reach R ≥ 0.67 and 31 % reach R ≥ 0.708 (lognormal, sd 0.3; with sd 0.5: 32 % and 25 %; uniform 0.2 to 2: 24 % and 16 %). R ≥ 0.67 therefore does not separate a provenance match from chance. (3) Table S1 retains three samples with R = 0.66 (2888, 3267, 10511 yr), below the stated rule. Nineteen retained samples have R below 0.708, all younger than 14 kyr, so the threshold decides which Holocene samples enter the record. |
| Suggestion | Derive the acceptance threshold from a null distribution generated with the actual database (random or permuted patterns fitted by the same procedure), or use cross-validation (fit 12 REE, predict the 13th); report residuals per sample; apply the corrected rule to Table S1 and recompute the Holocene results with the samples that remain. |
| Status | verified (degrees of freedom, critical values, Table S1); inferred (simulation with the supplement data) |
| Severity | major |
| Source | SD |

#### Minor corrections

| ID | Location | Quotation | Replacement | Source |
|---|---|---|---|---|
| KK-04 | p. 3, l. 101 | "ice core camples" | "ice core samples" | S2 |
| KK-05 | p. 4, l. 127 | "(Figure S1, and Table S1)" | "(Figure S1 and Table S2)" | S4 |
| KK-06 | p. 4, l. 128 | "subdivised into Patagonia" | "subdivided into Patagonia" | S2 |
| KK-07 | p. 5, l. 140 | "implemented using the lsqnonneg function in MATLAB" | "implemented using the lsqnonneg function in MATLAB (release stated)" | SD |
| KK-08 | p. 5, l. 145 to 146 | "For any given time step. The vector of 217 components represents" | "For any given time step, the vector of 217 components represents" | S2 |
| KK-09 | p. 5, l. 159 | "by minimizing Eq. (1)" | "by minimizing Eq. (2)" | S4 |

#### Verification log

| ID | Check | Checked | Values | Result |
|---|---|---|---|---|
| PP-05 | P12 | Table S2 parsed | 217 rows with 13 UCC-normalised values each; references per row: Gili et al. 2017 (44), Gaiero et al. 2004 (14), Li et al. 2020 (6), Vanderstraeten et al. 2023 (11), this study (6), Koffman et al. 2021 (19), Marx et al. 2005 (10), McGowan et al. 2005 (2), Marx and Kamber 2010 (101), Diaz et al. 2018 (4) | available; entries see GB-02, GB-27 |
| PP-06 | P38 | Model and core names | "DEPOT" p. 3, l. 88, 100, p. 8, l. 259, Table S1; "EDC", "EPICA Dome C", "Epica Dome C" (p. 7, l. 220) | no finding |
| PP-07 | P22 | Sampling gap (p. 4, l. 113) | Table S1 ages between 21.7 and 27.3 kyr: 22150, 23104, 25384, 25640 (four) | no finding |
| PP-08 | P9 | Sr Nd mixture recomputed with Eq. 3 and 4, Table S3 and the period means of Table S1 | LGM 0.7083 and εNd minus 2.61; HS1 0.7076, minus 1.56; ACR 0.7082, minus 2.92; YD 0.7094, minus 5.38; Holocene 0.7101, minus 4.98; text EDC LGM 0.708, minus 1.66 to minus 2.46, Holocene 0.710, minus 4.51 to minus 5.68 | LGM and Holocene close; YD see GB-17 |
| PP-09 | P10 | Design sketch (instanz_SD.md) | four aims (p. 3, l. 91 to 98), no separate research questions; modelling study; comparison with EDML and literature isotopes; iron fertilization frame without instrument, used as motivation only (p. 2, l. 37 to 52; p. 15, l. 491) | filled; no separate finding |
| PP-10 | P7, P30, P37 | One method for all data; corrections after runs | single configuration for all 279 EDC samples (n 13); no corrections reported | no finding (EDML configuration see GB-22) |
| PP-11 | P26 | Non-negativity guarantee (p. 4, l. 138 to p. 5, l. 139) | holds by construction in all fits | no finding |
| PP-12 | P32, P33, P36 | False negatives, effort, recollection statements | no error-free claim; effort only as computation cost (GB-04); no recollection statements | no finding |

### Segment 3: Results (p. 6 to 7, l. 173 to 218; Figures 1, 3, S3, S4; Tables S1, S5)

#### Substantive findings

**GB-09 The tentative status of the ACR and YD results is stated only in Section 4.4, with a YD sample count that differs from Table S1**

| Field | Content |
|---|---|
| Check | P17, P2 |
| Location | p. 6, l. 192 to 193; p. 6, l. 203 to 207; p. 7, l. 233; p. 12, l. 407 to 409 |
| Quotation | "It is important however to note that results for ACR and YD are tentative due to the limited number samples covering those periods in EDC" |
| Concern | The ACR and YD means are reported in the Results (p. 6, l. 192 to 193, 203 to 207) and the main shift is placed "at the onset of the ACR" (p. 7, l. 233) without this caveat, which appears only in the EDML comparison (p. 12, l. 407 to 409). The caveat gives "8 and 7 samples in ACR and YD"; with the limits of p. 6, l. 186 to 187 Table S1 has 8 ACR samples (13032 to 14601 yr) and 9 YD samples (11779 to 12867 yr, including 12841 yr twice), and the Table S5 YD mean (PAT 63.1) is reproduced only with all 9. |
| Suggestion | Move the caveat to Section 3 after p. 6, l. 188 and to p. 7, l. 233, give the number of samples per period in Table S5, correct "8 and 7" to "8 and 9" at p. 12, l. 408, and attach Monte Carlo ranges to the ACR and YD means. |
| Status | verified |
| Severity | moderate |
| Source | SD, S3 |

**GB-10 Statements about individual sources and subregions are made from data that are not shown**

| Field | Content |
|---|---|
| Check | P34 |
| Location | p. 6, l. 196 to 197; p. 11, l. 366 to 367; p. 12, l. 385 to 387 |
| Quotation | "Among the 39 DS from PAT, our algorithm highlights three specific REE patterns collected in or near the Valdes Peninsula." |
| Concern | The three patterns are not named (Table S2 has PataGi5 at Peninsula de Valdes and several Puerto Madryn and Trelew samples nearby), the criterion for "highlights" is not given, and per-source results are not reported. "our model identifies the Darling sub-basin as the dominant source region during the Holocene" (p. 11, l. 366 to 367) rests on Australian subregion results shown nowhere (Figure S3 covers PAP and SAF only). The ranking of SAF subregions by detection frequency (p. 12, l. 385 to 387) has no counts. |
| Suggestion | Name the three sources and the selection criterion, add Australian subregion shares and detection frequencies per subregion to the supplement, and refer to them at p. 6, l. 196, p. 11, l. 366 and p. 12, l. 385. |
| Status | verified |
| Severity | moderate |
| Source | SD |

**GB-11 The Puna and Altiplano statements disagree with Table S1, and Table S1 disagrees with Figure S3**

| Field | Content |
|---|---|
| Check | P2, P3 |
| Location | p. 7, l. 211 to 215; p. 11, l. 355 to 359; Figure S3 (Altiplano panel); Table S1 (columns Puna, Altiplano) |
| Quotation | "which even becomes dominant in several samples, contributing over 90% at 11.2, 10, 8.6, 6, and 3.5 kyr BP. In contrast, contributions of South Puna remained consistently below 20% during this interval" |
| Concern | (1) Table S1 has Altiplano above 90 % only at 8629 yr (100.0) and 11228 yr (97.0); the highest values near the other three ages are 75.7 (9957 yr), 58.5 (5967 yr) and 62.7 (3465 yr). (2) South Puna is at or above 20 % in eight Holocene samples: 3503 (25.0), 4387 (20.6), 5657 (23.4), 5850 (29.1), 6775 (20.7), 7833 (25.6), 10205 (25.7), 11117 (20.2). (3) The ACR and YD increase of PAP is "primarily from the South Puna region" (l. 212), but for the YD Table S1 gives Puna 1.3 % and Altiplano 3.3 % (mean of 9 samples). (4) "the Southern Altiplano begins contributing dust only after approximately 11.2 kyr BP" (p. 11, l. 358): Table S1 has Altiplano 16.6 % and 12.8 % at 12841 yr. (5) Figure S3, measured at 300 dpi (y: 0 % at 792.0 px, 100 % at 67.5 px; x: 14 kyr at 1381.5 px, 30 kyr at 2378.5 px; ±0.14 % and ±16 yr), shows at most 5.5 % at 8.63 kyr and 14.5 % at 11.23 kyr (Table S1: 100.0 and 97.0), a maximum of 66.1 % at about 6.37 kyr (Table S1 at 6367 yr: 53.5), and 38.8 % at about 11.86 kyr, also before 11.2 kyr. Figure 3 (Holocene PAP points near 100, 97 and 76 %) agrees with Table S1, so Figure S3 is the deviating element. The text refers to Figure 1 for South Puna (l. 215), which shows only total PAP. The link of the Altiplano onset to the final desiccation of paleolake Coipasa (p. 11, l. 358 to 359) rests on an onset date that both Table S1 and Figure S3 contradict. |
| Suggestion | Recheck which series Figure S3 shows and make Table S1, Figure 3 and Figure S3 consistent; rewrite p. 7, l. 211 to 215 (with "(Figure S3)" instead of "(Figure 1)") and p. 11, l. 355 to 360 from the corrected series, including the onset of Altiplano contributions and its comparison with the Coipasa desiccation. |
| Status | verified |
| Severity | major |
| Source | S3, AB, S4 |

**GB-12 Legends and axis numbers of Figures 1, 2, 3 and 5 are below 6 pt at print size**

| Field | Content |
|---|---|
| Check | P29 |
| Location | Figure 1 legend (p. 24); Figure 2 legend (p. 26); Figure 3 axis numbers (p. 27); Figure 5 axis numbers (p. 29) |
| Quotation | "Bold lines denote the mobile average over 9 steps." |
| Concern | Measured at 300 dpi as cap or digit height, px × 72 / 300 / 0.72: Figure 1 legend ("Raw data", "smoothed") 11 to 12 px = 3.7 to 4.0 pt; Figure 2 legend ("EDC LGM") 16 px = 5.3 pt; Figure 3 digits of "100,00" 15 px = 5.0 pt; Figure 5 axis digits 14 px = 4.7 pt (both axes of panel A). Figure 4 axis digits are 18 px = 6.0 pt, at the limit. Method uncertainty about 0.6 pt. |
| Suggestion | Enlarge the legends of Figures 1, 2 and 5 and the axis numbers of Figures 3 and 5 to at least 7 pt at final print size. |
| Status | verified |
| Severity | minor |
| Source | AB |

**GB-13 The smoothed curves run unbroken across the sampling gap of 21.7 to 27.3 kyr BP**

| Field | Content |
|---|---|
| Check | P29 |
| Location | Figure 1, all panels (p. 24); Figure 5 A; Figure S3; Figure S5; p. 4, l. 113 |
| Quotation | "A sampling gap exists between 21.7 and 27.3 kyr BP, where only four samples were available." |
| Concern | In all panels of Figure 1 the bold 9-point mobile average is drawn as a continuous, nearly straight line between about 22 and 28 kyr, where Table S1 has four samples. The 9-sample window spans a few hundred years in the Holocene and several thousand years across the gap; neither the gap nor the varying window is marked in the figures or captions. |
| Suggestion | Interrupt the smoothed curves or shade the gap in Figures 1, 5 A, S3 and S5, and state in the captions that the mobile average is over 9 samples of irregular spacing. |
| Status | verified |
| Severity | minor |
| Source | AB |

**GB-14 Table S1 contains four duplicated ages with different compositions and one row that does not sum to 100 %**

| Field | Content |
|---|---|
| Check | P23 |
| Location | Table S1 (rows 3559, 10511, 12841, 28709 yr) |
| Quotation | "Table S1: Median of PSA's contribution (in percents) based on th DEPOT model results" |
| Concern | Four ages occur twice with different results, for example 3559 yr: PAT 86.7, AUS 12.8 (R 0.88) and PAT 0.0, Altiplano 32.9, AUS 49.8, NZ 17.3 (R 0.73); 12841 yr: PAT 39.5 and 71.9. The first row at 10511 yr sums to 93.5 % (all other 240 rows sum to 100 ± 0.1 %) and has R = 0.66. Possible resolutions: (A) two subsamples of one depth were measured separately; (B) an age was copied wrongly; (C) at 10511 yr a share of 6.5 % is missing from a column. The table cannot decide between them; the Table S5 means include all eight rows. |
| Suggestion | Give sample identifiers and depths in Table S1, correct or explain the duplicated ages and the row at 10511 yr, and recompute Table S5 if rows change. |
| Status | verified |
| Severity | moderate |
| Source | S3 |

#### Minor corrections

| ID | Location | Quotation | Replacement | Source |
|---|---|---|---|---|
| KK-10 | Figure 3, y axes (p. 27) | "100,00" | "100" (decimal point, no decimals) | AB |

#### Verification log

| ID | Check | Checked | Values | Result |
|---|---|---|---|---|
| PP-13 | P2 | Table S5 (EDC) recomputed from the 241 rows of Table S1 with the limits of p. 6, l. 184 to 188 | Late Holocene n 60: PAT 50.7, PAP 12.0, SAF 11.6, AUS 21.4, NZ 3.8, ANT 0.6; Early Holocene n 56: 47.1, 10.0, 9.8, 24.9, 8.1, 0.0; Holocene n 116: 49.0, 11.0, 10.7, 23.1, 5.9, 0.3; YD n 9: 63.1, 4.5, 14.6, 14.5, 3.3, 0.0; ACR n 8: 68.9, 5.2, 8.0, 11.1, 6.6, 0.2; HS1 n 27: 74.8, 2.0, 4.9, 11.3, 7.1; LGM n 40: 65.7, 3.6, 6.3, 10.2, 14.2; MIS3 n 41: 70.3, 2.2, 9.3, 9.1, 9.1 | no finding; identical to Table S5 |
| PP-14 | P1, P2 | Sample bookkeeping and Results text against Table S5 (p. 6, l. 174 to p. 7, l. 216) | 294 minus 15 = 279; 279 minus 38 = 241; 241 / 279 = 86.4 % (text 86 %); mean R of Table S1 0.8523 (text 0.852); PAT 65 to 70, 75, 69, 63, 47 to 51; AUS 9, 10, 11, 11, ~15, 23; SAF ~5 to 9, 15; NZ 14, 7, 6.5, 3, 6; PAP below 4, ~5, 11 (Table S5 values above) | no finding |
| PP-15 | P20 | Exclusions (p. 6, l. 174 to 176) | retained samples younger than 14 kyr: 129; excluded 38, all younger than 14 kyr; excluded share of samples younger than 14 kyr 38 / 167 = 22.8 % | no finding; disclosed |
| PP-16 | P2 | SAF minimum "~2%" between 9.5 and 12 kyr (p. 7, l. 207 to 208) | 9-point moving average of Table S1 0.8 to 12.8 % (mean 6.2 %), sample median 0.3 % | no finding |
| PP-17 | P38 | Period limits: text, Table S5, Figure 1 | MIS3 57 to 29, LGM 29 to 18, HS1 18 to 14.7, ACR 14.7 to 12.9, YD 12.9 to 11.7, Holocene 11.7 to 2.8 kyr BP; Table S5 Late Holocene 2.8 to 7.5, Early Holocene 7.5 to 11.7 | no finding |
| PP-18 | P29 | Register of figures | Fig. 1 p. 24 (caption p. 25, l. 851 to 854), cited p. 6, l. 183, 205, 215, p. 7, l. 221, p. 9, l. 307, p. 10, l. 338; Fig. 2 p. 26, cited p. 8, l. 244, 252, 257; Fig. 3 p. 27, cited p. 9, l. 281, 294; Fig. 4 p. 28, cited p. 12, l. 405, p. 13, l. 419; Fig. 5 p. 29, cited p. 10, l. 340; Figures S1 to S5 cited p. 4, l. 127, p. 5, l. 167, p. 11, l. 355, p. 12, l. 382, l. 405 | numbering continuous; every figure cited |
| PP-19 | P24 | Period shading in Figure 1, NZ panel (x: 4 kyr at 688.0 px, 32 kyr at 1865.5 px; ±24 yr) | grey 11.70 to 12.89 kyr (YD), 14.70 to 18.01 kyr (HS1), from 28.99 kyr (MIS3) | no finding |
| PP-20 | P24 | Dated extremes in the text against the 9-point moving average of Table S1 | PAT minima at 10117, 8508, 6306 yr (text 10, 8.6, 6.3 kyr); AUS maxima at 9902 and 10511 yr and 6306 yr (text 9.5 to 10 and ~6.3 kyr) | no finding |
| PP-21 | P3 | Figure 3 points against Table S1; residues and placeholders | Holocene PAP points near 100, 97, 76 % (Table S1 100.0, 97.0, 75.7); NZ point near 90 % (10222 yr: 90.4); no placeholders on pages 24 to 29 or supplement figure pages | no finding |
| PP-22 | P19 | Provenance class of core statements | Table S1 and Table S5 labelled as model results (medians, averages) | no finding |

### Segment 4: Discussion, conclusion, declarations, references (p. 7 to 29, l. 219 to 882; Figures 2, 4, 5, S5; Tables S3 to S5)

#### Substantive findings

**GB-15 The isotope values attributed to Delmonte et al. (2004) are referenced to the dust size paper**

| Field | Content |
|---|---|
| Check | P4 |
| Location | p. 7, l. 238 to 240; p. 17, l. 561 to 564; Table S4 |
| Quotation | "Delmonte et al. (2004) reported 87Sr/86Sr ratios of ~0.708 and ε(Nd) values ranging from -1.66 to -2.46 for LGM dust at EDC" |
| Concern | The only Delmonte 2004 entry is "Dust size evidence for opposite regional atmospheric circulation changes over east Antarctica during the last climatic transition", Climate Dynamics 23 (p. 17, l. 561 to 564). Sr and Nd isotopes of EDC glacial dust are reported in Delmonte, B., Basile-Doelsch, I., Petit, J.R., Maggi, V., Revel-Rolland, M., Michard, A., Jagoutz, E., Grousset, F. (2004) Comparing the Epica and Vostok dust records during the last 220,000 years: stratigraphical correlation and provenance in glacial periods. Earth-Science Reviews 66, 63 to 87, https://doi.org/10.1016/j.earscirev.2003.10.004 (abstract read at boa.unimib.it/handle/10281/553), which is not in the list; Table S4 cites "Delmonte et al., 2004a". The source of the Holocene EDC values (minus 4.51 to minus 5.68, l. 240) is not given. |
| Suggestion | Cite the Earth-Science Reviews paper for the glacial values at p. 7, l. 238 and in Table S4, add it to the reference list, and give the source of the Holocene values at p. 7, l. 239 to 240. |
| Status | verified (reference list, source abstract); inferred (whether the Climate Dynamics paper also lists isotopes, full text not read) |
| Severity | moderate |
| Source | S4 |

**GB-16 Figure 2 shows one point per sample while the text describes one calculation per interval, and the MIS3 class of the text is not in the legend**

| Field | Content |
|---|---|
| Check | P3 |
| Location | p. 8, l. 244 to 246; p. 8, l. 251 to 252; Figure 2 (p. 26) |
| Quotation | "For each time interval of the LGIT, the relative contribution of each PSA (CONTR) was multiplied by its average Sr and Nd concentrations" |
| Concern | Figure 2 shows dozens of filled points per colour (for example EDC YD points from εNd about +1 to minus 18 at 87Sr/86Sr 0.7275), so the calculation was done per sample, not per interval. The legend lists EDC Early Holocene, EDC Holocene, EDC YD, EDC ACR, EDC HS1 and EDC LGM; the text (p. 8, l. 251 to 252) speaks of "the end of MIS3/LGM" in blue, but MIS3 is not in the legend. "Iso" in the legend is not explained. |
| Suggestion | State at p. 8, l. 244 that the mixture was computed per sample (and per interval, if both), add MIS3 to the legend or remove it from l. 251, and explain "Iso" (measured ice core values, Table S4) in the caption. |
| Status | verified |
| Severity | moderate |
| Source | AB |

**GB-17 The isotopic agreement is claimed for EDC, but the measured comparison data are almost entirely from other sites, and robustness is stated rather than measured**

| Field | Content |
|---|---|
| Check | P15, P31 |
| Location | p. 8, l. 258 to 260; p. 8, l. 251 to 255; Table S4; Figure 2 |
| Quotation | "Overall, the close agreement between our modeled isotopic compositions and those measured in EDC for both glacial and interglacial intervals supports the robustness of our DEPOT algorithm" |
| Concern | Table S4, the source of the measured values (open symbols in Figure 2), lists two EDC values (LGM, Delmonte et al., 2004a), one "Old Dome C" value (Basile et al., 1997), 18 Taylor Glacier values (Aarons et al., 2017; LGM and deglacial) and 14 Berkner Island values (Bory et al., 2010), which are all the Holocene values. No measured EDC value for deglacial or Holocene intervals is in Table S4, although Holocene EDC values are cited at p. 7, l. 239 to 240. Aarons et al. (2017) attribute part of the deglacial and early Holocene Taylor Glacier dust to local Ross Sea sources (read at byrd.osu.edu), and Berkner Island lies outside East Antarctica, so these points test other deposition settings. No misfit and no recovery test with known mixtures is given; robustness is stated, not measured. Recomputing Eq. 3 and 4 with Table S3 and the YD means gives 0.7094 and εNd minus 5.38, more negative than the Holocene (0.7101, minus 4.98), whereas l. 251 to 252 places the YD in the glacial cluster of "higher ε(Nd)". Aim (2) of the study (p. 3, l. 93 to 94) is this validation. |
| Suggestion | Restrict the agreement at p. 8, l. 258 to 260 to what is compared (EDC for the LGM, other Antarctic sites later), add the cited EDC Holocene values to Table S4 and Figure 2, give a quantitative misfit per period, add a recovery test with synthetic mixtures of database patterns plus noise, and correct the YD statement at p. 8, l. 251 to 252. |
| Status | verified (Table S4, text, source); inferred (YD recomputation) |
| Severity | major |
| Source | S4, SD |

**GB-18 The timing and dimensions attributed to Davies et al. (2020) differ from the source**

| Field | Content |
|---|---|
| Check | P13 |
| Location | p. 8, l. 267 to 269 |
| Quotation | "the Patagonian Ice Sheet reached its maximum spatial extent between ~34 and 29.4 kyr BP, covering much of the Andes with an ice mass 2090 km long and 350 km wide (Davies et al., 2020)" |
| Concern | The abstract of Davies et al. (2020) (read at researchportal.port.ac.uk) gives the maximum extent by 33 to 28 ka between 38° S and 48° S, and an earlier maximum around 47 ka south of 48° S; the dimensions 2090 km by 350 km refer to the ice sheet at 35 ka, not to its maximum. |
| Suggestion | Replace by "reached its maximum extent between 38° S and 48° S by 33 to 28 ka (earlier, around 47 ka, further south); at 35 ka it was 2090 km long and 350 km wide (Davies et al., 2020)". |
| Status | verified |
| Severity | minor |
| Source | S1 |

**GB-19 The model study cited as support for South American dominance reports Australian dominance over Antarctica in the LGM**

| Field | Content |
|---|---|
| Check | P13 |
| Location | p. 8, l. 275 to p. 9, l. 276 |
| Quotation | "Model simulations also support this view, estimating that SSA and AUS sources together supplied 70-90% (here, PAT+AUS is ~77%) of the dust reaching EA during the LGM" |
| Concern | "this view" (l. 275) is the significance of Patagonian sources (p. 8, l. 273 to 275). Krätschmer et al. (2022), read at cp.copernicus.org/articles/18/67/2022/, report that in their LGM simulation Australia is the predominant source of dust deposited over Antarctica, that South American dust contributes up to 40 % only in a smaller region of East Antarctica, and that Australia and South America together contribute slightly more than 90 % over 60 to 90° S. The cited model does not support Patagonian dominance, and its combined share lies above the stated range. Albani et al. (2012) was not checked. |
| Suggestion | Rewrite p. 8, l. 275 to p. 9, l. 277 to state that model simulations attribute most Antarctic LGM dust to Australia and South America together, that Krätschmer et al. (2022) find Australia dominant, and discuss this disagreement with the REE result. |
| Status | verified |
| Severity | moderate |
| Source | S1 |

**GB-20 The LGM share of New Zealand is given as 14 % and as 11 %**

| Field | Content |
|---|---|
| Check | P2 |
| Location | p. 9, l. 281 to 282; p. 7, l. 208 to 209; Table S5 |
| Quotation | "However, we find a higher average NZ contribution (~11%), making it the second-largest dust source to EDC during the LGM." |
| Concern | Results (p. 7, l. 209) and Table S5 give NZ 14 % (14.2) for the LGM. The mean NZ share over all samples older than 18 kyr (LGM and MIS3, n 81) is 11.6 %, which may be the origin of "~11%", but the sentence refers to the LGM. |
| Suggestion | Replace "(~11%)" by "(~14%)" at p. 9, l. 282, or name the interval if another one is meant. |
| Status | verified (14.2 %); inferred (origin of 11 %) |
| Severity | minor |
| Source | S3 |

**GB-21 Is the New Zealand share attributed to Neff and Bertler (2015) a value for inland East Antarctica?**

| Field | Content |
|---|---|
| Check | P13 |
| Location | p. 9, l. 286 to 287 |
| Quotation | "Present-day forward air-mass trajectories indicate NZ dust could contribute" |
| Concern | The sentence continues with a range of 14 to 32 % "to inland Antarctic deposition (Neff and Bertler, 2015)". The abstract of Neff and Bertler (2015) (read at adam.antarcticanz.govt.nz/nodes/view/63689) says that New Zealand and Patagonia "rapidly contribute a high proportion of trajectories to West Antarctica" and that "in interior East Antarctica, source contributions are limited and highly mixed". The full text could not be read, so the range could not be located. If it refers to West Antarctica, it does not support New Zealand as second source at Dome C (p. 9, l. 282). |
| Suggestion | Please give the table or figure of Neff and Bertler (2015) from which the range is taken and the region it refers to; if it is West Antarctica, qualify the sentence at p. 9, l. 286 to 287. |
| Status | inferred (full text not readable) |
| Severity | moderate |
| Source | S1 |

**GB-22 The EDML values used for the EDC to EDML comparison differ from the published EDML record and were obtained with another configuration**

| Field | Content |
|---|---|
| Check | P13, P9 |
| Location | p. 9, l. 287 to 288; p. 5, l. 144; Table S5 (EDML rows); Figure 4; Figure S5 |
| Quotation | "our previous EDML ice core work detected NZ dust at ~6 % on average over the entire LGM" |
| Concern | The introduction (p. 3, l. 78 to 81) reproduces Vanderstraeten et al. (2023) correctly: after about 14.5 kyr BP the Patagonian share in EDML fell "below 50% on average". The abstract of that study (read at marineinfo.org/doc/publication/382930) states this drop, an early Holocene Patagonian share of about 50 % and New Zealand at about 3 to 4 % before 14.5 kyr BP. Table S5, titled as EDC and EDML averages, gives for EDML PAT 62.5 % (ACR), 58.4 % (YD) and 62.7 % (Early Holocene), and NZ 6.2 % (LGM) and 6.5 % (HS1): no post 14.5 kyr PAT value is below 50 %, and the NZ values are about twice the published ones. In addition, EDML was fitted with 14 REE and EDC with 13 (p. 5, l. 144 to 145); whether database, threshold and Monte Carlo set-up were the same is not stated. All EDC minus EDML differences in Section 4.4, Figure 4 and the abstract (p. 1, l. 27 to 29), for example NZ LGM +8 = 14.2 minus 6.2, rest on these values, and part of them may come from the configuration rather than from atmospheric circulation. |
| Suggestion | State in Section 2 and in the caption of Table S5 how the EDML values were obtained; rerun EDML with the present configuration (13 REE, same 217 sources, same threshold), report both versions, and base Section 4.4, Figure 4 and the abstract on identical configurations. |
| Status | verified (Table S5, text, source abstract, configuration difference); inferred (cause and effect size of the deviation) |
| Severity | major |
| Source | S1, SD |

**GB-23 Three composite shares in the discussion do not follow from Table S5**

| Field | Content |
|---|---|
| Check | P1 |
| Location | p. 9, l. 295; p. 9, l. 276; p. 10, l. 321; p. 10, l. 326 |
| Quotation | "This dominance persisted into HS1, with high-latitude sources totaling 84 %" |
| Concern | Table S5 (EDC): HS1 PAT 74.8 + NZ 7.1 = 81.9 %, not 84 % (difference 2.1 points). LGM PAT 65.7 + AUS 10.2 = 75.9 %, not "~77%" (p. 9, l. 276; 1.1 points). Holocene PAT 49.0 + CWA 0.0 + PAP 11.0 = 60.0 %, given as 61 % at p. 10, l. 321 and as 60 % at p. 10, l. 326 for the same quantity. LGM PAT + NZ = 79.9 % and AUS + SAF + PAP = 20.1 % (p. 9, l. 294 to 295, "~79 %" and "~21 %") are within rounding. |
| Suggestion | Replace "84 %" by "82 %" at p. 9, l. 295, "~77%" by "~76%" at p. 9, l. 276 and "61%" by "60%" at p. 10, l. 321. |
| Status | verified |
| Severity | minor |
| Source | S3 |

**GB-24 The higher Holocene variability is not separated from analytical noise at low dust concentrations**

| Field | Content |
|---|---|
| Check | P9 |
| Location | p. 9, l. 306 to p. 10, l. 314; p. 6, l. 175 to 179; Table S1 |
| Quotation | "During YD and throughout the Holocene, our unmixing model reveals a significantly larger variability in the dust assemblages reaching EDC as shown in Figure 1." |
| Concern | The manuscript states that at low concentrations element-specific analytical noise "distorts the REE patterns" (p. 6, l. 178 to 179) and excluded 38 samples, all younger than 14 kyr (22.8 % of the samples younger than 14 kyr). The retained Holocene samples also fit worse: mean R 0.799 (Holocene, n 116) against 0.924 (LGM, n 40) and 0.912 (HS1, n 27). Large jumps between neighbouring samples (3559 yr listed twice with PAT 86.7 and 0.0) are consistent with noise as well as with climate. Section 4.3 explains the variability by climatic processes only, and the Monte Carlo spread that would show the noise level is not reported (GB-07). |
| Suggestion | Report the Monte Carlo interquartile range per sample, compare the sample-to-sample variability of PSA shares with it, and test synthetic mixtures: LGM patterns degraded to Holocene concentration and noise and refitted; discuss the noise explanation at p. 9, l. 306 to 308. |
| Status | verified (R means, exclusions); inferred (noise as cause) |
| Severity | major |
| Source | SD |

**GB-25 A Pb isotope study of the EDC core itself that bears on the Australian and Antarctic shares is not discussed**

| Field | Content |
|---|---|
| Check | P14 |
| Location | p. 10, l. 329 to 334; p. 13, l. 438 to 440 |
| Quotation | "our results do not indicate significant Antarctic contributions to EDC" |
| Concern | Vallelonga, P., Gabrielli, P., Balliana, E., Wegner, A., Delmonte, B., Turetta, C., Burton, G., Vanhaecke, F., Rosman, K.J.R., Hong, S., Boutron, C.F., Cescon, P., Barbante, C. (2010) Lead isotopic compositions in the EPICA Dome C ice core and Southern Hemisphere Potential Source Areas. Quaternary Science Reviews 29, 247 to 255, https://doi.org/10.1016/j.quascirev.2009.06.019 (read at bpcrc.osu.edu). On EDC samples it finds that Australian dust is not the main component, that several interglacial and low-dust samples show more than 50 % local Antarctic dust input, and that volcanic Pb obscures interglacial provenance. This bears directly on the Holocene AUS share of 23 % and the negligible ANT share claimed here. The reference list contains only Vallelonga et al. (2002), a Law Dome pollution study. |
| Suggestion | Discuss Vallelonga et al. (2010) in Section 4.3 at p. 10, l. 329 to 334 (Antarctic sources) and at p. 13, l. 438 to 440 (Australian sources), and add it to the reference list. |
| Status | verified |
| Severity | moderate |
| Source | S1 |

**GB-26 Aim 3 is examined only by visual comparison with literature records**

| Field | Content |
|---|---|
| Check | P10 |
| Location | p. 10, l. 338 to 340; p. 3, l. 94 to 95; Figure 5 |
| Quotation | "Overall, our Holocene provenance record for PAT contributions is matching well with the SWW intensity proxies in Potrok" |
| Concern | Aim (3) asks to relate shifts to regional climatic changes. No instrument quantifies the relation: Figure 5 places two series side by side without correlation, lag or age uncertainty, and the other comparisons (Australian lakes, Namibian rivers, Coipasa) are verbal. "matching well" has no measure. |
| Suggestion | Resample both series of Figure 5 to a common time step and give a correlation with its uncertainty under the age models, or define events (onsets, minima) and compare their dates with uncertainties; report the result at p. 10, l. 338 to 340. |
| Status | verified |
| Severity | moderate |
| Source | SD |

**GB-27 Eight cited works have no entry in the reference list, and one entry is not cited**

| Field | Content |
|---|---|
| Check | P4 |
| Location | p. 11, l. 365; Table S2; Table S4; p. 18, l. 630 to 632 |
| Quotation | "with the previous Pb isotopic study (Gili et al., 2016)" |
| Concern | Not in the reference list: Gili et al., 2016 (main text); Marx et al., 2005, McGowan et al., 2005, Marx and Kamber, 2010 and Diaz et al., 2018 (Table S2, together the source of 117 of the 217 patterns: all 107 AUS, 6 of 25 NZ and all 4 ANT rows); Aarons et al. (2017) and Bory et al. (2010) (Table S4, measured isotopes in Figure 2); "Delmonte et al., 2004a" (Table S4) implies two 2004 entries, the list has one. The supplement has no reference list. Without these entries the origin of more than half of the source patterns and of most validation data cannot be traced. Conversely, Gaiero, Brunet, Probst and Depetris (2007) (p. 18, l. 630 to 632) is listed but not cited; the text cites only "Gaiero, 2007", which matches the single-author entry. |
| Suggestion | Add full entries for the eight works to the reference list or a supplement reference list, check whether "Gili et al., 2016" means Gili et al. (2017), and cite or remove Gaiero et al. (2007). |
| Status | verified |
| Severity | moderate |
| Source | S4 |

**GB-28 The ACR and YD differences between EDC and EDML are swapped, and the YD is not at the expense of Southern Africa**

| Field | Content |
|---|---|
| Check | P2 |
| Location | p. 13, l. 421 to 422; Figure 4; Table S5 |
| Quotation | "the ACR and YD intervals exhibit a slight enrichment of Patagonian dust (+4 and +6.5%) in EDC, primarily at the expense of Southern African and Australian contributions" |
| Concern | From Table S5: PAT ACR 68.9 minus 62.5 = +6.4, YD 63.1 minus 58.4 = +4.7; the order in the text is reversed. SAF: ACR 8.0 minus 12.4 = minus 4.4, but YD 14.6 minus 8.2 = +6.4, so in the YD EDC receives more SAF dust; the YD deficit is in AUS (minus 4.5), NZ (minus 3.9) and PAP (minus 2.4). Figure 4 agrees with Table S5 (measured: PAT ACR +6.4, YD +4.8; SAF YD +6.4; ±0.15). |
| Suggestion | Replace at p. 13, l. 421 to 422 by "(+6.4 and +4.7 %) in EDC, at the expense of Australian and Southern African contributions in the ACR and of Australian, New Zealand and PAP contributions in the YD". |
| Status | verified |
| Severity | moderate |
| Source | S3 |

**GB-29 The Holocene comparison sets the whole EDC Holocene against the EDML Early Holocene**

| Field | Content |
|---|---|
| Check | P20 |
| Location | p. 13, l. 423 to 424; Figure 4 (bars "Holo"); Table S5; p. 1, l. 27 to 29 |
| Quotation | "EDC appears to receive substantially less PAT dust (-14%) but higher contributions of Australian dust (+12%) than EDML" |
| Concern | The comparison is announced for the shared interval 7.5 to 27 kyr BP (p. 12, l. 406 to 407), and Table S5 gives EDML only for the Early Holocene (7.5 to 11.7 kyr). The values follow from EDC Holocene 2.8 to 11.7 kyr (PAT 49.0, AUS 23.1) minus EDML Early Holocene (62.7, 10.8): minus 13.7 and +12.3; Figure 4 measures minus 13.7 and +12.3. On the shared window (EDC Early Holocene 47.1 and 24.9) the differences are minus 15.6 and +14.1. The direction holds, but the analysis unit differs between the two cores without notice. |
| Suggestion | Compute the Holocene differences in Section 4.4 and Figure 4 for the Early Holocene of both cores, label the bar "Early Holocene" and state the window in the caption of Figure 4. |
| Status | verified |
| Severity | moderate |
| Source | S3 |

**GB-30 Higher relative shares of low-latitude sources are read as greater inputs although the total flux fell**

| Field | Content |
|---|---|
| Check | P21 |
| Location | p. 13, l. 440 to 443; p. 1, l. 23 to 24; p. 10, l. 315 to 317; p. 14, l. 479 to 480 |
| Quotation | "and increased aridity in low-latitude regions (see above), which likely amplified dust emissions and transport from these sources." |
| Concern | All shares are fractions of the total deposition. AUS rises from 10.2 % (LGM) to 23.1 % (Holocene), a factor of 2.26, so the absolute AUS input rises only if the total dust flux fell by less than this factor. The manuscript states that interglacial fluxes are "up to 25 times lower than LGM fluxes" (p. 2, l. 63); with a factor of 25 the Holocene AUS input is 23.1 / 25 = 0.92 against 10.2 (units of the LGM total flux), about 11 times lower. "greater inputs from low-latitude sources" (p. 1, l. 23) and "amplified dust emissions" (p. 13, l. 443) therefore cannot be read from relative data; a stronger decline of high-latitude emissions alone produces the same relative rise. The absolute fluxes announced in Section 2 (GB-07) would decide this. |
| Suggestion | Report absolute PSA fluxes for LGM and Holocene, and at p. 1, l. 23, p. 13, l. 440 to 443 and p. 14, l. 479 to 480 speak of relative shares unless the fluxes show an increase. |
| Status | inferred (computed from manuscript values) |
| Severity | major |
| Source | S3 |

**GB-31 The decline in total dust deposition at EDML is referred to figures that do not show it**

| Field | Content |
|---|---|
| Check | P4 |
| Location | p. 13, l. 448 to 450 |
| Quotation | "deposition that began around 19-18 kyr BP and continued until ~15 kyr BP in both cores (Figures S2" |
| Concern | Figure S2 shows EDC records only (nssCa flux, δ18O, deuterium excess); Figure S5 shows relative provenance contributions, not deposition. No figure or table shows EDML deposition. |
| Suggestion | Add an EDML dust flux record with its source to Figure S2, or cite the publication that shows it at p. 13, l. 449 to 450. |
| Status | verified |
| Severity | minor |
| Source | S4 |

**GB-32 "Our data demonstrate" overstates what a synchronous provenance shift can show about mechanisms**

| Field | Content |
|---|---|
| Check | P15 |
| Location | p. 14, l. 466 to 470; p. 14, l. 480 to 482 |
| Quotation | "Importantly, our data demonstrate that these feedback mechanisms influenced dust deposition not only in EDML" |
| Concern | The data show a synchronous decline of the PAT share in both cores (p. 13, l. 445 to 447). The mechanisms (shelf submergence, drainage reversal) are taken from Vanderstraeten et al. (2023) and the cited literature; no test in this manuscript separates them from the alternatives it discusses itself (transport efficiency, wet scavenging, p. 9, l. 308 to p. 10, l. 314). |
| Suggestion | Replace "our data demonstrate" by "our data are consistent with the hypothesis" at p. 14, l. 466, and "confirm" by "are consistent with" at p. 14, l. 480. |
| Status | verified |
| Severity | moderate |
| Source | S4 |

**GB-33 The conclusion attributes the EDC to EDML differences to source-area climate, the discussion to site position and circulation**

| Field | Content |
|---|---|
| Check | P15 |
| Location | p. 14, l. 485 to 487; p. 13, l. 424 to 425 |
| Quotation | "the relative contributions of PAT, SAF, NZ and AUS differed reflecting regional climatic dynamics in their respective source areas" |
| Concern | Section 4.4 explains the differences by "the geographic positioning of the two sites" (p. 13, l. 425), the storm track, the polar vortex and jet pathways (l. 425 to 435). Climate in a source area changes its emissions for both cores alike and cannot by itself make the two cores differ, so the conclusion names a cause the discussion does not develop. |
| Suggestion | Replace at p. 14, l. 487 by "differed, which we attribute to the different exposure of the two sites to mid- and low-latitude air masses (Section 4.4)". |
| Status | verified |
| Severity | moderate |
| Source | S4 |

**GB-34 The data availability statement does not cover the model code, the correction factors, the uncertainty outputs or the derived series**

| Field | Content |
|---|---|
| Check | P12 |
| Location | p. 16, l. 494 to 496; p. 5, l. 140 |
| Quotation | "All data needed to evaluate the conclusions in the paper are present in the paper and/or the Supplementary Materials." |
| Concern | Data sources named in Section 2 and their status: (1) DIC REE concentrations of 294 samples (Gabrielli et al., 2010): published elsewhere, neither in the supplement nor linked; (2) cf_i and their variability (p. 4, l. 119 to 124; p. 5, l. 157 to 158): not given; (3) source database: Table S2, available; (4) DEPOT code (p. 5, l. 140): not mentioned; (5) Monte Carlo outputs per source and PSA (p. 5, l. 160 to 165): not given, Table S1 has medians only; (6) absolute PSA fluxes (p. 5, l. 166 to 167): not given; (7) subregion series (Figure S3; Darling sub-basin, p. 11, l. 366): only as figure, AUS subregions not at all; (8) identities of the 38 excluded samples (p. 6, l. 174 to 175): not given; (9) EDML series (Table S5, Figure S5): source and configuration not stated. Seven of nine sources are not covered. The data concern no persons, and "may be requested from the authors" (l. 495 to 496) gives no reason for withholding. No link is given, so reachability could not be checked. |
| Suggestion | Replace the statement at p. 16, l. 494 to 496 by a list per data source with repository and DOI; deposit the DEPOT code, the cf_i values with uncertainties, per-sample Monte Carlo percentiles and absolute fluxes; name the excluded samples. |
| Status | verified |
| Severity | moderate |
| Source | S2 |

**GB-35 Eighteen reference entries contain RTF control codes in the typeset text**

| Field | Content |
|---|---|
| Check | P16 |
| Location | p. 16, l. 528 to p. 22, l. 828 |
| Quotation | "471\uc0\u8211{}501. https://doi.org/10.1191/0309133303pp386ra\" |
| Concern | The codes are visible on the page images (p. 16, l. 528; p. 20, l. 746 to 747). In the extracted text 27 lines carry such sequences or a trailing backslash, in 18 entries: Bullard and McTainsh 2003, De Deckker et al. 2014, Dukes et al. 2018, Engelbrecht et al. 2019, Fletcher and Moreno 2012, Gaiero et al. 2007, Gingele and De Deckker 2005, Grousset and Biscaye 2005, Lisé-Pronovost et al. 2015, Markgraf et al. 2007, Markle et al. 2018, Moreno et al. 2010, Power et al. 2008, Quade and Kaplan 2017, Stone et al. 2010, Stuut et al. 2002, Veres et al. 2013, Wagner et al. 2021; names (O'Loingsigh, Villa-Martínez, Goñi), page ranges and coordinates are garbled. |
| Suggestion | Replace the codes by the characters they encode (en dash, apostrophe, accented letters, degree and prime signs) and remove the trailing backslashes in the reference list. |
| Status | verified |
| Severity | minor |
| Source | S4 |

**GB-36 Figure 5 has no time axis title, and its shaded band and dashed lines are not explained**

| Field | Content |
|---|---|
| Check | P29 |
| Location | Figure 5 (p. 29), panels A and B; p. 29, l. 880 to 882 |
| Quotation | "Figure 5: Comparison of the contribution of Patagonian dust (PAT) to EDC ice core (A) and (B) the Median Destructive Field of isothermal remanent magnetization (MDF)" |
| Concern | The x axes carry only numbers (0.5 to 3) without quantity, unit or the ×10⁴ factor used in Figure 1. A blue band (about 0.8 to 1.15) between dashed lines and grey bands appear in both panels; the caption explains neither. Panel B uses an inverted MDF axis whose meaning is given only by an arrow "Wind intensity". The age model of the Potrok Aike record is not stated. |
| Suggestion | Add "Time (kyr BP)" to both axes, explain the blue band, dashed lines and grey bands in the caption, and name the Potrok Aike chronology. |
| Status | verified |
| Severity | minor |
| Source | AB |

#### Minor corrections

| ID | Location | Quotation | Replacement | Source |
|---|---|---|---|---|
| KK-11 | p. 7, l. 236 | "This shift already describes by Gili et al. (2022)" | "This shift, already described by Gili et al. (2022)" | S4 |
| KK-12 | p. 8, l. 246 | "(Table S3, e.i. Eq.3)" | "(Table S3, i.e. Eq. 3)" | S4 |
| KK-13 | p. 8, l. 249 | "where the mean isotopic signatures is represents by" | "where the mean isotopic signatures are represented by" | S4 |
| KK-14 | p. 8, l. 261 | "4.2 Persistance of high-latitude" | "4.2 Persistence of high-latitude" | S4 |
| KK-15 | p. 8, l. 266; p. 21, l. 800 | "(Sugden et al., 2009)" with entry "Sudgen, D. E." | entry "Sugden, D. E." | S4 |
| KK-16 | p. 9, l. 303 to 304 | "(from 14.5 kyr BP until 2.7 kyr BP)" | "(from 14.5 kyr BP until 2.8 kyr BP)" | S3 |
| KK-17 | p. 10, l. 329 to 330 | "includes several McMurdo region sites (Section 4.2)" | "includes several McMurdo region sites (Section 2, Table S2)" | S4 |
| KK-18 | p. 10, l. 334 | "(Speirs et al., 2001)" | "(Speirs et al., 2010)" | S4 |
| KK-19 | p. 10, l. 341 | "Moreno et al. (2010);" | "Moreno et al., 2010;" | S4 |
| KK-20 | p. 10, l. 342 to 343 | "(Quake and Kaplan, 2017)" | "(Quade and Kaplan, 2017)" | S4 |
| KK-21 | p. 11, l. 367 | "De Deccker et al. (2010)" | "De Deckker et al. (2010)" | S4 |
| KK-22 | p. 12, l. 382 | "SAF dust contribution to EDC ice core (Figure S4)" | "SAF dust contribution to EDC ice core (Figure S3)" | S4 |
| KK-23 | p. 12, l. 384 to 385 | "suggesting strengthened dust transport from southern Africa suggesting strengthened dust transport from southern Africa" | "suggesting strengthened dust transport from southern Africa" | S4 |
| KK-24 | p. 12, l. 398 | "kyr BP (Brook et al., 2011)" | "kyr BP; Brook et al., 2011)" | S4 |
| KK-25 | p. 12, l. 398 to 399 | "likely reflect their low-frequency, high-magnitude nature of their dust emissions" | "likely reflect the low-frequency, high-magnitude nature of their dust emissions" | S4 |
| KK-26 | p. 13, l. 426 | "to receive dust from Patagonia dust brought" | "to receive dust from Patagonia brought" | S4 |
| KK-27 | p. 13, l. 427 | "located at the interior of EAP" | "located in the interior of the East Antarctic Plateau (EAP)" | S4 |
| KK-28 | p. 13, l. 439 | "(De Deccker et al., 2019" | "(De Deckker, 2019" | S4 |
| KK-29 | p. 16, l. 501 | "APPENDIX S. SUPPLENTARY DATA. Supplementary data to this article" | "APPENDIX S. SUPPLEMENTARY DATA. Supplementary data to this article are available online." | S4 |
| KK-30 | p. 20, l. 729 | "chronology for the EPICA Dome C ice core. Clim. Past." | "chronology for the EPICA Dome C ice core. Clim. Past 3, 485 to 497, https://doi.org/10.5194/cp-3-485-2007" (page range with an en dash in the final version) | S4 |
| KK-31 | p. 20, l. 748 | "Environùental characterization" | "Environmental characterization" | S4 |
| KK-32 | p. 26, l. 857 to 858 | "dust in ice cores (refs. Table S1, - open symbols)" | "dust in ice cores (refs. Table S4, open symbols)" | S4 |
| KK-33 | p. 26, l. 865 | "the isotopic fingerprint (Table S4)" | "the isotopic fingerprint (Table S3)" | S4 |
| KK-34 | p. 28, l. 875 to 876 | "Histograms representing the contribution percentage difference" and "(Table S4)" | "Bar charts representing the contribution percentage difference" and "(Table S5)" | S4, AB |
| KK-35 | Figure S5, y axis title (supplement p. 10) | "PAS EDC Contribution and PSA EDML Contribution ( in %)" | "PSA contribution, EDC and EDML (%)" | AB |

#### Verification log

| ID | Check | Checked | Values | Result |
|---|---|---|---|---|
| PP-23 | P13 | Kok et al. (2021) shares for Antarctica (p. 10, l. 319 to 323) | source text, Sect. 3.4.1 (acp.copernicus.org): South America about 70 %, Australia about 20 %, Southern Africa about 10 %; manuscript 70 ± 20 %, 18 % (6 to 36 %), 10 % (3 to 13 %); Table 2 of the source is an image | no finding; central values consistent, ranges not verified |
| PP-24 | P13 | Coppo et al. (2022) shares 64, 15, 11, 5, 5 % (LGM) and 33, 23, 14, 24 % (Holocene) (p. 9, l. 277 to 279; p. 10, l. 324 to 328) | published article not open; ESS Open Archive preprint essoar.10508915.1 has no percentages | no finding; source not readable |
| PP-25 | P2 | Discussion values against Table S5 (p. 10, l. 315 to 319; p. 13, l. 417 to 421) | Holocene AUS, PAP, SAF 23, 11, 11 against LGM 10, 4, 6; PAT, NZ 49, 6; NZ LGM EDC minus EDML 14.2 minus 6.2 = 8.0, PAT minus 8.0; HS1 differences 3.2, minus 0.2, minus 5.3, 1.9, 0.6 (maximum about 5) | no finding |
| PP-26 | P2 | PAT decline between 15 and 14 kyr in EDC (p. 13, l. 445 to 446) | Table S1 bin means PAT 83.2 (15 to 16 kyr, n 8), 72.0 (14 to 15 kyr, n 7), 64.3 (13 to 14 kyr, n 4) | no finding |
| PP-27 | P3 | Figure 4 bars measured (y: +10 at 791.0 px, minus 10 at 922.5 px; ±0.15) | PAT Holo minus 13.7, YD +4.8, ACR +6.4, HS1 +3.2, LGM minus 8.0; AUS Holo +12.3, YD minus 4.5, ACR minus 7.3, HS1 +2.1, LGM +0.3; SAF Holo minus 0.5, YD +6.4, ACR minus 4.5, HS1 minus 5.1, LGM minus 2.6 | consistent with Table S5; text deviations GB-28, GB-29 |
| PP-28 | P4 | Numbering of sections, equations, figures and tables | Sections 1 to 5 (4.1 to 4.4); Eq. 1 to 4; Figures 1 to 5 and S1 to S5; Tables S1 to S5 | no finding beyond the minor corrections listed |
| PP-29 | P4 | Citations against reference list in both directions | 90 distinct in-text citations; mismatches: Gili 2016 (no entry), Speirs 2001 and 2010, Quake and Quade, Sugden and Sudgen, De Deccker 2010 and 2019, Gaiero et al. 2007 uncited; EPICA Community Members 2006 cited only in the Figure S2 caption | GB-27, KK-15, KK-18, KK-20, KK-21, KK-28 |
| PP-30 | P15 | Statements of Section 5 against own results | glacial dominance (p. 14, l. 474 to 477; Table S5), shift after 14.5 kyr (l. 477 to 480; Table S5), decoupling from the flux decline (l. 483 to 484; Figure S2), differences between cores (l. 485 to 487; GB-33), role of sea level and hydrology (l. 488 to 492; literature); no proposals for future studies | GB-32, GB-33; rest no finding |
| PP-31 | P15 | Aims (1) to (4) (p. 3, l. 91 to 98) taken up in discussion and conclusion | (1) Sect. 3, 4; (2) Sect. 4.1 (GB-17); (3) Sect. 4.2, 4.3 (GB-26); (4) Sect. 4.4, 5 | no finding for coverage |
| PP-32 | P16 | "763.103 km2" in the extracted text (p. 8, l. 270) | page image shows "~763.10³ km²" | no finding (extraction artefact) |
| PP-33 | P16 | Uniformity of the reference list | journal names abbreviated and in full side by side (for example "Clim. Past" and "Earth and Planetary Science Letters") | noted, no further finding |

## Optional checks

| Area | What it needs | Responsible | Run |
|---|---|---|---|
| DOI resolution | one request per reference with DOI | `science-quellenapparat-pruefung` | no |
| Citation style | the name of the style | `science-zitierstil-harvard-ctr` or the journal's style rules | no |
| AI statement against publisher policy | the target publisher's policy | this review, on request | no |
| Relation to the authors' own prior work | the authors' prior publications | this review, on request | no |
| Journal requirements | the target journal's author guidelines | this review, on request | no |
| Subject-matter accuracy | access to the sources of the checked statements and a choice of sections | `science-faktenbeleg-pruefung`, `geo-frage-belegbasiert-klaeren` | no |

## Limits of this review

- Checked version: egusphere-2025-5046.pdf, 29 pages, SHA-256 f598b53d01e375844cfb549eb05b9a3407bb30cae553e603c125d5f14886c722, with supplement (22 pages, SHA-256 759cfa14195948f5772d3d6d696081932424f4296e51c812415527ed3b108ea6)
- Sources not readable: Coppo et al. (2022), published version; Vanderstraeten et al. (2023), full text (abstract read); Neff and Bertler (2015), full text (abstract read); Delmonte et al. (2004, Earth-Science Reviews), full text (abstract read); Davies et al. (2020), full text (abstract read); Kok et al. (2021), Table 2 (image); Albani et al. (2012) not checked
- Findings with status assumption: 0 of 36 (GB-21 is phrased as a question because its source could not be read)
- Optional checks run: 0 of 6
- Omitted instances: none; all six instances ran one after another in one context, not as separate agents
- Discarded findings: 0
