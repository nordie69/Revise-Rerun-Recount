# Review report: Quantifying Southern Hemisphere dust sources during the Last Glacial-Interglacial Transition using rare earth elements in the EPICA Dome C ice core

| Field | Value |
|---|---|
| Manuscript | Boxho, S., Vanderstraeten, A., Mattielli, N., Laruelle, G. G., Bory, A., Gabrielli, P., Bonneville, S., 2025, Quantifying Southern Hemisphere dust sources during the Last Glacial-Interglacial Transition using rare earth elements in the EPICA Dome C ice core, EGUsphere preprint, https://doi.org/10.5194/egusphere-2025-5046, with supplement |
| Checked version | egusphere-2025-5046.pdf, 29 pages, SHA-256 f598b53d01e375844cfb549eb05b9a3407bb30cae553e603c125d5f14886c722; supplement egusphere-2025-5046-supplement.pdf, 22 pages, SHA-256 759cfa14195948f5772d3d6d696081932424f4296e51c812415527ed3b108ea6 |
| Date | 2026-10-17 |
| Language | English |
| Review instances | Segments 1 to 4, figures (AB), study design (SD); review instances ran sequentially in one context (checked sequentially, not context-separated); no instance omitted |

## Summary

The manuscript is a method-application study in ice-core dust provenance. It applies the authors' rare earth element unmixing model DEPOT, a non-negative least-squares fit (MATLAB lsqnonneg) of 13 UCC-normalised REE concentrations per sample against a database of 217 potential source area (PSA) patterns, to the published EPICA Dome C REE record of Gabrielli et al. (2010). Of 294 samples, 279 were fitted and 241 retained after a fit criterion of R at least 0.67, covering 33.7 to 2.9 kyr BP. Uncertainty is propagated with 2000 Monte Carlo runs per sample. Patagonia (PAT) supplies 65.7 to 74.8 % of the dust on average in MIS3, LGM and HS1 and 49.0 % in the Holocene, while Australia (AUS) rises from 10.2 % (LGM) to 23.1 % (Holocene) and the Puna-Altiplano (PAP) from 3.6 % to 11.0 % (Table S5). The model output is checked against Sr-Nd isotope data through a concentration-weighted mixing calculation and compared with the EDML record of the same method; the shift after about 14.5 kyr BP is attributed to Patagonian shelf flooding and drainage reorganisation.

## Strengths

1. The supplement gives the result for every retained sample (Table S1, 241 rows with R); the period averages in Table S5 can be recomputed from it and agree to 0.1 percentage points for all eight EDC intervals, so the central numbers of the paper are traceable (PP-08, PP-09).
2. Uncertainty in the analytical REE concentrations and in the element-specific correction factors is propagated by 2000 Monte Carlo runs per sample with a stated check at 5000 runs, and the median of the resulting distribution is used, which makes the per-sample estimates less sensitive to single noisy elements (PP-05).
3. The PSA database is documented sample by sample in Table S2 with reference, sample type, location, coordinates and all 13 normalised values, so the end-member set can be reused and audited; the audit in this review was only possible because of it (PP-04, GB-05, GB-06).
4. The EDC record is compared with the EDML record produced by the same algorithm, so differences between the two sites are not caused by a change of method; for LGM and HS1 the reported differences agree with Table S5 (PP-14, GB-24).

## Weaknesses

1. Identifiability of the unmixing is not demonstrated: 13 equations are solved for 217 non-negative unknowns, and the four Antarctic end-members appear not to be normalised like the rest of the database. The authors should test non-uniqueness and recovery on synthetic mixtures and correct or re-examine the ANT patterns (GB-08, GB-05).
2. The Holocene results, which carry the main new statements, rest on the samples with the lowest concentrations and the weakest fits, and the fit threshold is less strict than stated. The authors should show that the Holocene shift and its variability survive a stricter, correctly derived threshold and a concentration-dependent noise test (GB-10, GB-09).
3. Several claims are stronger than their evidence: the isotope check does not use measured Holocene EDC data, the feedback mechanisms are said to be demonstrated by the data, the record is called the first quantitative one, and one modelling study is cited for the opposite of its result. The authors should rephrase these statements and, where possible, compare with measured EDC isotopes (GB-18, GB-25, GB-01, GB-19).
4. Text, tables and figures disagree at several places of moderate weight: PAP sub-region statements against Table S1 and Figure S3, the Holocene box plots, the EDC minus EDML comparison window, and the missing code and correction factors. The authors should regenerate the affected statements and figures from Table S1 and release code and inputs (GB-13, GB-15, GB-24, GB-07, GB-03).

## Findings by segment

### Segment 1: Abstract, introduction (p. 1 to 3)

#### Substantive findings

**GB-01 The claim of a first quantitative provenance record for EDC is not backed by a described search and is weakened by quantitative work the manuscript itself cites**

| Field | Content |
|---|---|
| Check | P28 |
| Location | p. 1, l. 19; p. 7, l. 220; p. 12, l. 403; p. 14, l. 472 |
| Quotation | "we quantify for the first-time contributions from key Southern Hemisphere dust sources" |
| Concern | The priority claim is repeated four times ("first continuous and quantitative record" l. 220, "The only continuous and quantitative dust provenance record in EA" l. 403, "the first high-resolution, continuous and quantitative reconstruction" l. 472), but no search (databases, terms, date) is described. The manuscript itself reports quantitative source shares from Coppo et al. (2022) for East Antarctica in the LGM (64 % SSA, 15 % Antarctica, 11 % AUS, 5 % SAF, 5 % NZ; p. 9, l. 277 to 279) and for the Holocene (SSA 33 %, AUS 23 %, SAF 14 %, Antarctica 24 %; p. 10, l. 324 to 328). Delmonte et al. (2010, QSR 29, 256 to 264), not in the reference list, give mixing estimates of roughly 70 to 100 % Patagonian dust for glacial East Antarctic dust. The defensible novelty is the combination "continuous, sample-resolved, REE-based record at EDC", not quantification as such. |
| Suggestion | Restrict the claim in the abstract (l. 19), l. 220, l. 403 and l. 472 to what is new, e.g. "the first continuous, sample-resolved REE-based quantification at EDC", and position it explicitly against the isotope-based quantifications of Coppo et al. (2022) and Delmonte et al. (2010) in the introduction (p. 3, l. 88 to 98). |
| Status | verified (claim and cited quantifications in the manuscript); inferred (Delmonte et al. 2010 content, read from the full text) |
| Severity | moderate |
| Source | S1 |

**GB-02 Directly relevant EDC provenance studies are missing from the positioning**

| Field | Content |
|---|---|
| Check | P14 |
| Location | p. 2, l. 54 to 59; p. 3, l. 72 to 74 |
| Quotation | "Antarctic ice cores, especially those collected from high-altitude, inland drill sites, provide continuous" |
| Concern | Three studies that address EDC dust provenance with independent tracers are absent from the reference list (checked against all entries on p. 16 to 22): (1) Delmonte, B., Andersson, P.S., Schöberg, H., Hansson, M., Petit, J.R., Delmas, R., Gaiero, D.M., Maggi, V., Frezzotti, M., 2010. Geographic provenance of aeolian dust in East Antarctica during Pleistocene glaciations: preliminary results from Talos Dome and comparison with East Antarctic and new Andean ice core data. Quaternary Science Reviews 29, 256 to 264, https://doi.org/10.1016/j.quascirev.2009.05.010; it quantifies a 70 to 100 % Patagonian share for glacial dust and reports interglacial EDC and Vostok dust at 87Sr/86Sr about 0.7100 and eNd about minus 6.7 ± 2.3, a direct benchmark for Section 4.1. (2) Vallelonga, P., Gabrielli, P., Balliana, E., et al., 2010. Lead isotopic compositions in the EPICA Dome C ice core and Southern Hemisphere Potential Source Areas. Quaternary Science Reviews 29, 247 to 255, https://doi.org/10.1016/j.quascirev.2009.06.019; it states that 66 of 74 EDC samples fall outside the Australian Pb field and that Australia cannot be confirmed as a major source, which bears on the Holocene AUS share of 23 %. (3) Delmonte, B., Basile-Doelsch, I., Petit, J.R., et al., 2004. Comparing the Epica and Vostok dust records during the last 220,000 years: stratigraphical correlation and provenance in glacial periods. Earth-Science Reviews 66, 63 to 87, https://doi.org/10.1016/j.earscirev.2003.10.004; it excludes South Africa and Australia as dominant glacial sources (see also GB-17). The listed Delmonte et al. (2004) entry is a different paper (Climate Dynamics, dust size). |
| Suggestion | Add the three studies to the introduction (p. 2, l. 54 to 67) and to the discussion of Sections 4.1 and 4.3, and discuss the Pb result of Vallelonga et al. (2010) against the Holocene AUS share. |
| Status | verified (absence from reference list; content of items 1 to 3 read in full text or abstract) |
| Severity | moderate |
| Source | S1 |

#### Minor corrections

| ID | Location | Quotation | Replacement | Source |
|---|---|---|---|---|
| KK-01 | p. 1, l. 15 | "Dust deposits in ice cores provides" | "Dust deposits in ice cores provide" | S4 |
| KK-02 | p. 1, l. 20 | "During the Marine isotope 3 (MIS3)" | "During Marine Isotope Stage 3 (MIS3)" | S4 |
| KK-03 | p. 3, l. 101 | "dust source contributions to ice core camples" | "dust source contributions to ice core samples" | S4 |

#### Verification log

| ID | Check | Checked | Values | Result |
|---|---|---|---|---|
| PP-01 | P13 | DustCOMM shares for Antarctica (p. 10, l. 319 to 323) against Kok et al. (2021), Table 2, column Antarctica | Source: South America 71 % (50 to 90), Australia 18 % (6 to 36), Southern Africa 8 % (3 to 13); text of Kok et al.: about 70, 20, 10 %. Manuscript: SSA 70 ± 20 %, AUS 18 % (6 to 36), SAF 10 % (3 to 13). SAF central value follows the rounded text value, range follows the table | no finding |
| PP-02 | P13 | EDML results cited p. 3, l. 77 to 81 and p. 9, l. 288 against the abstract of Vanderstraeten et al. (2023) | Abstract: Patagonia about 68 % before 14.5 kyr BP, below 50 % after; NZ 3 to 4 %. Manuscript: below 50 % after 14.5 kyr (l. 79 to 80); NZ "~6 %" over the LGM (l. 288), which matches Table S5, EDML LGM NZ 6.2 % | no finding |
| PP-03 | P14, P28 | Searches for prior and contradicting work (WebSearch, 6 queries plus one targeted): Coppo 2022 provenance percentages; Delmonte 2004 Dome C Sr Nd; Neff and Bertler 2015 trajectories; Vanderstraeten 2023 EDML; quantitative dust source apportionment East Antarctic Holocene; REE apportionment Talos Dome RICE; Vallelonga 2010 Pb EDC | Candidates retained: Delmonte et al. 2010, Vallelonga et al. 2010, Delmonte et al. 2004 (Earth-Sci. Rev.); all absent from the list (GB-02). Gili et al. (2022), Coppo et al. (2022), Krätschmer et al. (2022) are cited | no finding beyond GB-02 |

### Segment 2: Materials, methods, data (p. 3 to 5, supplement Tables S2)

#### Substantive findings

**GB-03 Ages on the EDC3 chronology are binned with period boundaries from the AICC2012 chronology**

| Field | Content |
|---|---|
| Check | P7 |
| Location | p. 4, l. 111; p. 6, l. 184 to 188 |
| Quotation | "The age model follows the EDC3 chronology (Parrenin et al., 2007)." |
| Concern | Sample ages are on EDC3 (l. 111), while the interval boundaries MIS3, LGM, HS1, ACR, YD and Holocene are taken from Veres et al. (2013) (l. 188), the AICC2012 chronology. Samples near a boundary may fall into a different interval depending on the chronology; the ACR has 8 and the YD 9 samples in Table S1, so a shift of one or two samples changes the period averages and the EDC minus EDML differences of Figure 4. It is not stated whether EDML ages were put on the same chronology. The size of the EDC3 to AICC2012 offset over the deglaciation is not given in the manuscript; that it matters here is an assumption of this review. |
| Suggestion | Could the authors state, in Section 2 (p. 4, l. 111), whether the ages were transferred to AICC2012 before binning, which chronology the EDML record uses, and how many samples change interval when one chronology is used throughout? |
| Status | verified (two chronologies named); assumption (size of the effect) |
| Severity | moderate |
| Source | SD |

**GB-04 Numbers of dust sources per region in the text differ from Table S2**

| Field | Content |
|---|---|
| Check | P2 |
| Location | p. 4, l. 131 |
| Quotation | "Australia (AUS; 106 DS, predominantly from the central" |
| Concern | Counting the data rows per block in Table S2 (supplement p. 16 to 19) gives PAT 39, CWA 5, PAP 14, SAF 23, AUS 107, NZ 25, ANT 4, total 217. The text gives AUS 106 (l. 131) and ANT 5 (l. 132 to 133); 39 + 5 + 14 + 23 + 106 + 25 + 5 = 217 as well, so both lists add up and one of them is wrong. Rows were counted by Python as lines with 13 normalised values and confirmed on the page image of supplement p. 19 (four ANT rows: ELB, Expcove, Miers, Vict). This finding is separate from GB-05 and GB-06, which concern values, not counts. |
| Suggestion | Correct the counts on p. 4, l. 131 to 133 to AUS 107 and ANT 4, or add the missing ANT pattern to Table S2. |
| Status | verified |
| Severity | minor |
| Source | S3 |

**GB-05 The Antarctic end-member patterns in Table S2 do not look UCC-normalised, which could explain the absence of Antarctic contributions**

| Field | Content |
|---|---|
| Check | P5 |
| Location | p. 4, l. 132 to 134; p. 10, l. 329 to 331 |
| Quotation | "all PSA REE patterns were normalized to the UCC composition of Rudnick and Gao (2003)" |
| Concern | The rule on l. 133 to 134 is that all PSA patterns are UCC-normalised. In Table S2 (supplement p. 19), the four ANT rows have values such as 1.415, 0.157, 0.605, 0.120, 0.031, 0.015 (ELB, La to Tb), i.e. an odd-even zigzag with the light REE about 100 times above the heavy REE. Computed over all rows: ratio of maximum to minimum within one pattern is 209 to 252 for ANT, but at most 4.1 for any other region (median 1.3 to 1.9); mean absolute log step between neighbouring elements is 1.53 for ANT against 0.07 to 0.12 elsewhere. This pattern is typical of unnormalised or chondrite-type values, not of UCC-normalised dust. A pattern of this shape cannot fit any EDC sample, so the result "our results do not indicate significant Antarctic contributions to EDC" (l. 330) and the contrast with the 15 % (LGM) and 24 % (Holocene) Antarctic shares of Coppo et al. (2022) may be an artefact of the input. The explanation via katabatic winds (l. 330 to 334) would then not be needed. |
| Suggestion | Check the normalisation of the ANT rows in Table S2, rerun the unmixing with correctly normalised Antarctic patterns, and report in Section 4.3 (p. 10, l. 328 to 334) whether ANT contributions change. |
| Status | verified (values in Table S2, computed ratios); inferred (that the rows are unnormalised) |
| Severity | major |
| Source | SD |

**GB-06 Table S2, Southern Africa block: location entries and one outlying value**

| Field | Content |
|---|---|
| Check | P38, P27 |
| Location | Table S2 (supplement p. 17), rows EtoshaL1 to EtoshaL4, SuksesL, Sossusvlei, columns Location and Longitude; row Kuiseb2inf5, column Dy |
| Quotation | "Sossusvlei               /                   this study                < 5 µm                     Etosha Pan" |
| Concern | Confirmed on the rendered page: the six samples marked "this study" all carry the location "Etosha Pan", including Sossusvlei at 24.76 S, which is about 600 km south of Etosha Pan, and SuksesL at 21.06 S; their longitudes are given as W (15.29 W to 16.836 W), which places them in the Atlantic Ocean, while all other SAF rows are E. In row Kuiseb2inf5 the Dy value is 6.200013 while the neighbouring elements are 2.69 (Tb) and 2.15 (Ho) and the same element in Kuiseb1inf5 is 2.38. This value enters the 217 by 13 design matrix and may steer which SAF sources are selected (Section 4.3, l. 385 to 387). This finding is separate from GB-04 (counts). |
| Suggestion | Correct location names and the E/W sign for the six "this study" rows, check the Kuiseb2inf5 Dy value against the source, and state in Section 2 (p. 4, l. 130 to 131) which SAF samples are new. |
| Status | verified |
| Severity | minor |
| Source | S2, SD |

**GB-07 Code, correction factors and intermediate data are not available, so the unmixing cannot be reproduced**

| Field | Content |
|---|---|
| Check | P12, P35 |
| Location | p. 5, l. 140; p. 16, l. 493 to 496 |
| Quotation | "Additional data related to the paper may be requested from the authors." |
| Concern | The data statement covers what is "present in the paper and/or the Supplementary Materials" (l. 494 to 495). Not covered: the DEPOT code (only "the lsqnonneg function in MATLAB", l. 140, without version, tolerance or options); the element-specific correction factors cfi and their variability used in the Monte Carlo runs (l. 153 to 159); the element-wise analytical uncertainties Dusti (stated only as 2 % to 10 %, l. 155 to 156); the REE data of the 15 incomplete and 38 rejected samples and their R values; the absolute fluxes derived from nssCa (l. 166 to 167). The data concern no persons, so restriction to "on request" has no stated reason. The EDC REE data themselves are published (Gabrielli et al., 2010) and the end-members are in Table S2. Reachability of external repositories was not checked because none is given. |
| Suggestion | Deposit the DEPOT code with version and solver settings, the cfi table with uncertainties, Dusti per element, and the full per-sample output including rejected samples in a public repository, and cite it in the data statement on p. 16, l. 493 to 496 and in Section 2 (p. 5, l. 140). |
| Status | verified |
| Severity | moderate |
| Source | S2, SD |

**GB-08 Uniqueness of a 217-source solution from 13 elements is not tested**

| Field | Content |
|---|---|
| Check | P9 |
| Location | p. 5, l. 143 to 144; p. 5, l. 150 to 152 |
| Quotation | "is multiplied by a vector of 217 components" |
| Concern | Each sample is fitted with 13 UCC-normalised REE values against 217 unknown non-negative contributions (l. 143 to 145). Non-negative least squares returns at most as many non-zero terms as there are equations, but many different subsets of 217 strongly collinear patterns (AUS alone has 107, mostly flat patterns with ratios of maximum to minimum near 1.4) can fit almost equally well. The Monte Carlo runs (l. 153 to 165) propagate measurement noise but do not show whether a different selection of sources, with different regional shares, fits equally well; R is computed against the same 13 values that were fitted, with "degrees of freedom = 10" (l. 171 to 172), which ignores that the fitted model has up to 13 free parameters. Regional shares also depend on how many patterns each region contributes to the database (AUS 49 % of all patterns). The result that PAT dominates and AUS rises therefore needs a test of identifiability before it can be read as a source apportionment. Alternative design: synthetic mixtures of known composition drawn from Table S2, with noise as in the Monte Carlo runs, unmixed by DEPOT to give recovery rates per region; a leave-one-region-out or regional-mean end-member variant; and the spread of regional shares over all solutions within the noise level. |
| Suggestion | Add a recovery test on synthetic mixtures and a sensitivity test with regional mean end-members to Section 2 (after p. 5, l. 152), and report regional shares with the resulting uncertainty in Table S5. |
| Status | verified (13 equations, 217 unknowns, R definition); inferred (non-uniqueness and database weighting effect) |
| Severity | major |
| Source | SD |

**GB-09 The fit threshold R 0.67 does not correspond to p below 0.01 for 10 degrees of freedom, and three retained samples fall below it**

| Field | Content |
|---|---|
| Check | P1, P5 |
| Location | p. 5, l. 170 to 172; Table S1, column R, rows 2888, 3267, 10511 |
| Quotation | "We determined that R" |
| Concern | For a two-tailed test with 10 degrees of freedom the critical correlation at p = 0.01 is 0.708 (Python, scipy t distribution: t crit 3.169, r = t / sqrt(t squared + 10)); R = 0.67 gives p = 0.017, and 0.67 corresponds to p = 0.02 (r crit 0.658) or to 11 degrees of freedom at p = 0.01 (0.684). Table S1 contains three retained samples with R = 0.66 (2888 and 3267 yr, and the first 10511 yr row), contrary to the rule that only samples with R at least 0.67 are kept (l. 174 to 175). With R at least 0.708, 19 of 241 samples would drop out, 17 of them Holocene; recomputed Holocene means change only slightly (PAT 49.0 to 48.4 %, AUS 23.1 to 23.6 %, PAP 11.0 to 11.8 %), so the period averages hold, but the stated significance level does not. |
| Suggestion | Correct the threshold or the stated p value and degrees of freedom on p. 5, l. 170 to 172, remove or justify the three rows with R 0.66 in Table S1, and report the Holocene averages for the corrected threshold in Table S5. |
| Status | verified (calculation, Table S1 values) |
| Severity | moderate |
| Source | S3, SD |

#### Minor corrections

| ID | Location | Quotation | Replacement | Source |
|---|---|---|---|---|
| KK-04 | p. 4, l. 127 | "(Figure S1, and Table S1)" | "(Figure S1 and Table S2)" | S4 |
| KK-05 | p. 4, l. 128 | "subdivised into Patagonia" | "subdivided into Patagonia" | S4 |
| KK-06 | p. 5, l. 145 to 146 | "For any given time" | "For any given time step, the vector of 217 components" (merge the sentence fragment) | S4 |
| KK-07 | p. 5, l. 159 | "minimizing Eq. (1)" | "minimizing Eq. (2)" | S4 |

#### Verification log

| ID | Check | Checked | Values | Result |
|---|---|---|---|---|
| PP-04 | P12 | Data sources in Section 2 against data statement and supplement | EDC REE: Gabrielli et al. (2010), published; PSA patterns: Table S2, 217 rows with coordinates and references; Sr-Nd end-members: Table S3, 7 rows; ice-core isotopes: Table S4, 37 rows; nssCa flux: Fischer et al. (2007), Figure S2; per-sample results: Table S1; period averages: Table S5. Not covered: see GB-07 | no finding beyond GB-07 |
| PP-05 | P8 | Monte Carlo design (p. 5, l. 153 to 167) | 2000 runs per sample, cfi and Dusti drawn from normal distributions, check with 5000 runs, median of PDF as estimate, aggregation per PSA; method nachvollziehbar apart from missing input values (GB-07) | no finding beyond GB-07 |
| PP-06 | P38 | Identifiers for regions and sub-regions in text, tables and figures | PAP: "Puna-Altiplano Plateau" (text), "Puna AltiPlano" (Table S2), "Puna" and "Altiplano" columns (Table S1), "S-Puna" and "S-Altiplano" (Figure 2, Table S3); CWA vs SCWA (Table S3, Figure 2) with explained subdivision; EDC, EDML, DIC, DS, CDS consistent | no finding |
| PP-07 | P10 | Design sketch: aims and instruments | Aims (1) to (4), p. 3, l. 91 to 98: (1) record by DEPOT (Section 3, Table S1, S5); (2) validation against Sr-Nd (Section 4.1, Figure 2); (3) links to regional climate (Sections 4.2, 4.3); (4) comparison with EDML (Section 4.4, Figure 4, S5). Each aim has an instrument and a results section; no outlook proposals in Section 5. Disclosed limits: ACR and YD sample numbers (p. 12, l. 407 to 409), sampling gap 21.7 to 27.3 kyr (p. 4, l. 113) | no finding |

### Segment 3: Results (p. 6 to 7, Figures 1 and 3, supplement Tables S1, S5, Figures S3, S4)

#### Substantive findings

**GB-10 Holocene variability coincides with the lowest concentrations and weakest fits, and is not separated from noise**

| Field | Content |
|---|---|
| Check | P9 |
| Location | p. 6, l. 175 to 179; p. 9, l. 306 to 307 |
| Quotation | "These excluded samples are all younger than 14 kyr BP and" |
| Concern | The manuscript discloses that all 38 rejected samples are younger than 14 kyr BP and that near the detection limit "element-specific analytical noise" distorts REE patterns (l. 175 to 179). The retained Holocene samples come from the same low-concentration regime: mean R is 0.799 for the 116 Holocene samples against 0.916 for the samples older than 14.7 kyr (Table S1, Python). The "significantly larger variability" of the Holocene (l. 306 to 307), with single samples switching between 0 and over 90 % for one region (e.g. AUS 98.1 % at 9772 yr next to PAT 92.7 % at 9847 yr), is then interpreted as source changes. Each sample integrates only 2 to 3 years (l. 112) at about 100-year spacing, so sample-to-sample switching may reflect single-year events or noise. The consequence of the disclosed noise is not carried through to the retained Holocene samples. Alternative design: inflate the Monte Carlo noise for low-concentration samples to the level implied by blanks and detection limits, report per-sample credible intervals of regional shares in Table S1, and test whether the Holocene variance exceeds the variance expected from noise alone. |
| Suggestion | Add a concentration-dependent noise test to Section 3 (after p. 6, l. 179), show per-sample uncertainties in Figure 1, and restrict the interpretation of Holocene variability in Section 4.3 (p. 9, l. 306 to 314) to features that exceed this noise. |
| Status | verified (disclosed noise, R statistics); inferred (that variability is partly noise) |
| Severity | major |
| Source | SD |

**GB-11 The stated order of importance of the secondary sources does not match the averages**

| Field | Content |
|---|---|
| Check | P2 |
| Location | p. 6, l. 201 to 202 |
| Quotation | "SAF, PAP and NZ, in decreasing order of importance" |
| Concern | Over all 241 samples (Table S1, unweighted mean) the order is AUS 16.5 %, SAF 9.2 %, NZ 7.9 %, PAP 6.9 % (Puna 3.1 + Altiplano 3.8), so NZ ranks above PAP. In the glacial periods NZ is second after PAT (LGM 14.2 %, l. 209), and l. 223 gives "NZ, AUS, SAF and PAP" for the LGM. The statement on l. 201 to 202 holds for none of the periods in Table S5 in full. |
| Suggestion | State the reference period on p. 6, l. 201 to 202 or change the order to "AUS, SAF, NZ and PAP". |
| Status | verified |
| Severity | minor |
| Source | S3 |

**GB-12 SAF minimum between 9.5 and 12 kyr BP is given as about 2 % but averages 4.3 %**

| Field | Content |
|---|---|
| Check | P2 |
| Location | p. 7, l. 208 |
| Quotation | "levels (~2%) between 9.5 and 12 kyr BP" |
| Concern | Table S1 has 33 samples between 9500 and 12000 yr; their SAF mean is 4.32 % and the median 0.3 %. The sample at 12227 yr has SAF 94.7 %. Neither statistic gives about 2 %. The smoothed curve in Figure 1 is not quantified. |
| Suggestion | Give the statistic used and its value on p. 7, l. 208, e.g. "median 0.3 %, mean 4.3 %". |
| Status | verified |
| Severity | minor |
| Source | S3 |

**GB-13 Statements on South Altiplano and South Puna contributions contradict Table S1, and Figure S3 does not reproduce Table S1**

| Field | Content |
|---|---|
| Check | P2, P3 |
| Location | p. 7, l. 212 to 215; p. 11, l. 358; Figure S3, panels Altiplano and Puna |
| Quotation | "dominant in several samples, contributing over 90% at 11.2, 10, 8.6, 6, and 3.5 kyr BP" |
| Concern | Table S1, column Altiplano: values over 90 % occur at 8629 yr (100.0) and 11228 yr (97.0) only; near 10 kyr the maximum is 75.7 (9957), near 6 kyr 58.5 (5967) and 58.0 (6166), near 3.5 kyr 62.7 (3465). Two of five stated cases hold. "contributions of South Puna remained consistently below 20%" (l. 215): eight Holocene samples have Puna at least 20 %, maximum 29.1 % (5850 yr). "begins contributing dust only after approximately 11.2 kyr BP" (l. 358): Table S1 has Altiplano 16.6 and 12.8 % at 12841 yr (two rows, YD). Figure S3 does not agree with Table S1 either: measured raw-data maximum in the Altiplano panel 66.2 ± 0.14 % at 6365 ± 16 yr (y ticks 100 at 67.5 px and 10 at 720.5 px, x ticks 4000 at 758.5 px and 12000 at 1257.5 px, 300 dpi), while Table S1 has 100.0 % at 8629 yr; Puna raw maximum 54.8 ± 0.14 % at about 11.8 kyr, while Table S1 Puna never exceeds 29.1 %. The PAP discussion (p. 11, l. 353 to 365) links the 11.2 kyr onset to the desiccation of paleolake Coipasa. |
| Suggestion | Recompute the statements on p. 7, l. 212 to 215 and p. 11, l. 357 to 359 from Table S1, and regenerate Figure S3 from the same data as Table S1 or explain the difference (e.g. whether Figure S3 shows medians or a different run). |
| Status | verified (table values; figure values measured) |
| Severity | moderate |
| Source | S3, AB |

**GB-14 Labels and legends in Figures 1 to 5 are below 6 pt in print size**

| Field | Content |
|---|---|
| Check | P29 |
| Location | Figure 1 (p. 24), legend and tick labels; Figure 2 (p. 26), legend; Figure 3 (p. 27), tick labels; Figure 4 (p. 28), tick labels; Figure 5 (p. 29), legend and tick labels |
| Quotation | "Bold lines denote the mobile average over 9 steps." |
| Concern | Cap heights measured on 300 dpi renders (pt = px × 72 / 300 / 0.72): Figure 1 legend "R" 14 px, 4.7 pt; tick digits 12 px, 4.0 pt; Figure 2 legend "E" 13 px, 4.3 pt; Figure 3 tick digits 14 px, 4.7 pt; Figure 4 tick digits 17 px, 5.7 pt; Figure 5 legend "R" 12 px, 4.0 pt, tick digits 11 to 16 px, 3.7 to 5.3 pt. All are below 6 pt in the page size of the preprint. |
| Suggestion | Enlarge legend, axis and tick label fonts in Figures 1 to 5 to at least 6 pt at final print size. |
| Status | verified (measured) |
| Severity | minor |
| Source | AB |

**GB-15 The Holocene box plots in Figure 3 show only the Early Holocene, and the Early Holocene box plots in Figure S4 show the Late Holocene**

| Field | Content |
|---|---|
| Check | P3 |
| Location | Figure 3, panel Holocene; Figure S4, panel Early Holocene; p. 9, l. 281 |
| Quotation | "Box plots of provenance contributions (in %) of Holocene, and Last Glacial Maximum (LGM)" |
| Concern | Measured on 300 dpi renders (Figure 3: ticks 100 at 735.5 px, 10 at 1363 px, ± 0.14 %; Figure S4: ticks 100 at 167.5 px, 0 at 1981 px, ± 0.06 %) and compared with Table S1 quartiles (Python, Weibull plotting positions). Figure 3 Holocene, PAT box: Q1 12.29, median 55.18, Q3 72.96; Table S1 Early Holocene (7.5 to 11.7 kyr, n 56): 12.30, 55.20, 72.97; full Holocene (n 116): 18.38, 58.60, 73.75. Figure 3 Holocene, AUS box: 2.83, 18.18, 34.24; Early Holocene: 2.85, 18.15, 34.17. Figure S4 Early Holocene, PAT box: 18.91, 61.65, 80.65; Table S1 Late Holocene (n 60): 18.92, 61.70, 80.70. The LGM panel of Figure 3 agrees with Table S1 LGM (58.84, 65.79, 71.75 against 58.85, 65.75, 71.68). Thus the panel labelled "Holocene" in Figure 3 and cited for Holocene statements is the Early Holocene, and the panel labelled "Early Holocene" in Figure S4 is the Late Holocene. The caption of Figure S4 lists five panels including Early Holocene but no Late Holocene. |
| Suggestion | Relabel or regenerate Figure 3 and Figure S4 so that the panels show the stated intervals, add the missing interval, and check the statements that cite Figure 3 (p. 9, l. 281 and l. 294 to 295). |
| Status | verified (measured, recomputed) |
| Severity | moderate |
| Source | AB |

**GB-16 Table S1 caption, duplicate ages and one row that does not sum to 100 %**

| Field | Content |
|---|---|
| Check | P2, P1 |
| Location | Table S1 (supplement p. 11 to 15), caption; rows 3559, 10511, 12841, 28709 |
| Quotation | "using 217 PSAs and 279 DIC from EDC ice core REE patterns" |
| Concern | The caption says 279 DIC, but the table lists 241 rows (the retained samples, l. 179). Four ages occur twice with different results: 3559, 10511, 12841, 28709 yr; it is not stated whether these are replicate samples or rounding of different depths. Row sums over the eight PSA columns are 99.9 to 100.1 % for 240 rows; the first 10511 yr row sums to 93.5 % (0.0 + 0.0 + 3.1 + 6.7 + 49.2 + 29.5 + 5.0 + 0.0) and has R 0.66 (see GB-09). |
| Suggestion | Change the caption of Table S1 to 241 retained samples (and "th DEPOT" to "the DEPOT"), add depth or sample identifiers to distinguish the duplicate ages, and correct or explain the row at 10511 yr. |
| Status | verified |
| Severity | minor |
| Source | S3 |

#### Minor corrections

| ID | Location | Quotation | Replacement | Source |
|---|---|---|---|---|
| KK-08 | p. 6, l. 183 | "Figure 1 and Table S1 summarize" | "Figure 1 and Table S5 summarize" (Table S1 gives per-sample values; period averages are in Table S5) | S4 |
| KK-09 | p. 6, l. 191 | "during HSI is marked" | "during HS1 is marked" | S4 |
| KK-10 | p. 25, l. 851 | "between 2852 to 33699 yr BP" | "between 2852 and 33699 yr BP" | S4 |
| KK-11 | p. 25, l. 853 | "contribution are very low" | "contributions are very low" | S4 |
| KK-12 | Figure S4, caption | "Antarctica Cold Reveal" | "Antarctic Cold Reversal", and "Heindrich Stadial 1" to "Heinrich Stadial 1", "Marine Isotope 3" to "Marine Isotope Stage 3" | AB |

#### Verification log

| ID | Check | Checked | Values | Result |
|---|---|---|---|---|
| PP-08 | P1 | Table S5, EDC, recomputed as unweighted means of Table S1 per interval (Python) | MIS3 n 41: PAT 70.3, PAP 2.2, SAF 9.3, AUS 9.1, NZ 9.1; LGM n 40: 65.7, 3.6, 6.3, 10.2, 14.2; HS1 n 27: 74.8, 2.0, 4.9, 11.3, 7.1; ACR n 8: 68.9, 5.2, 8.0, 11.1, 6.6; YD n 9: 63.1, 4.6, 14.6, 14.5, 3.3; Early Holocene n 56: 47.1, 10.0, 9.8, 24.9, 8.1; Late Holocene n 60: 50.7, 12.0, 11.6, 21.4, 3.8; Holocene n 116: 49.0, 11.1, 10.7, 23.1, 5.9. All within 0.1 of Table S5 | no finding |
| PP-09 | P2 | Abstract and Section 3 values against Table S5 | Abstract PAT 65 to 75 % for MIS3, LGM, HS1 (70.3, 65.7, 74.8); Holocene 49 % (49.0). l. 189 to 195: 65 to 70, 75, 69, 63, 47 to 51 (47.1, 50.7). l. 203 to 204: AUS 9, 10, 11, 11, about 15, 23 (9.1, 10.2, 11.3, 11.1, 14.5, 23.1). l. 206 to 209: SAF 5 to 9, 15, about 11 (9.3, 6.3, 4.9, 8.0, 14.6, 10.7). l. 209 to 210: NZ 14, 7, 6.5, 3, 6 (14.2, 7.1, 6.6, 3.3, 5.9). l. 211 to 216: PAP below 4, about 5, 11 (2.2, 3.6, 2.0, 5.2, 4.6, 11.0). l. 317 to 319: 23, 11, 11 against 10, 4, 6; 49, 6 | no finding |
| PP-10 | P23 | Sample balance | 294 samples, 15 incomplete, 279 fitted (l. 108, 114, 117); 38 rejected, 241 retained (l. 174, 179); 294 minus 15 = 279; 279 minus 38 = 241; 241 / 279 = 86.4 %, text 86 %; Table S1 rows 241; mean R 0.8523, text 0.852 | no finding |
| PP-11 | P11, P20 | Coverage and denominators | Table S5 EDC: 8 intervals by 7 PSA, no empty cell; EDML: 5 intervals (no MIS3, no Late Holocene), consistent with EDML span 7 to 27 kyr; averages are unweighted means of sample medians (denominator samples, not time) | no finding |
| PP-12 | P3, P29 | Figure list and Figure 1 against Table S1 | Figure 1 (p. 24, 5 panels, cited l. 183, 205, 215, 217, 221, 307, 338), Figure 2 (p. 26, cited l. 244, 252, 257), Figure 3 (p. 27, cited l. 281, 295), Figure 4 (p. 28, cited l. 405, 419), Figure 5 (p. 29, cited l. 339); Figures S1 to S5 cited. Figure 1 PAP raw peaks near 8.6 and 11.2 kyr consistent with Table S1 Altiplano 100.0 and 97.0 | no finding |

### Segment 4: Discussion, conclusion, declarations, references (p. 7 to 22, Figures 2, 4, 5, supplement Tables S3, S4, Figures S2, S5)

#### Substantive findings

**GB-17 Sr-Nd values attributed to Delmonte et al. (2004) are cited from a paper whose listed entry is a dust size study**

| Field | Content |
|---|---|
| Check | P4, P13 |
| Location | p. 7, l. 238 to 240; p. 26, l. 861 |
| Quotation | "Delmonte et al. (2004) reported" |
| Concern | The only Delmonte 2004 entry in the list is "Dust size evidence for opposite regional atmospheric circulation changes over east Antarctica during the last climatic transition", Climate Dynamics 23 (p. 17, l. 561 to 564). The Sr-Nd values for LGM EDC dust (0.708, eNd minus 1.66 and minus 2.46) agree with Table S4, labelled "Delmonte et al., 2004a", and with the isotope paper Delmonte et al. (2004), Earth-Science Reviews 66, 63 to 87 (abstract: glacial dust at 0.708 to 0.711, eNd minus 5 to plus 5), which is not listed. The Holocene values "-4.51 to -5.68" (l. 240) cannot be traced: Table S4 contains no Holocene EDC value, and Delmonte et al. (2010, QSR 29) report interglacial EDC and Vostok dust at eNd about minus 6.7 ± 2.3. The "2004a" label implies a "2004b" that does not exist in the list. |
| Suggestion | Add the Earth-Science Reviews paper to the reference list, distinguish 2004a and 2004b, and give the source of the Holocene EDC values on p. 7, l. 239 to 240 or remove them. |
| Status | verified (reference list, Table S4); inferred (attribution to Earth-Sci. Rev. paper from its abstract) |
| Severity | moderate |
| Source | S1, S4 |

**GB-18 The isotope validation does not use measured Holocene EDC data and is not quantified**

| Field | Content |
|---|---|
| Check | P31, P10 |
| Location | p. 8, l. 251 to 260; Figure 2; Table S4 |
| Quotation | "the close agreement between our modeled isotopic compositions and those measured in EDC" |
| Concern | Aim (2) is "confronting and validating the EDC results ... against Sr-Nd isotopic data" (p. 3, l. 93 to 94), and the conclusion is "close agreement ... measured in EDC for both glacial and interglacial intervals" (l. 258 to 259). Table S4, which supplies the measured values of Figure 2, contains 22 Holocene values: 8 from Taylor Glacier and 14 from Berkner Island, none from EDC; EDC values exist only for the LGM (2 values). Berkner Island lies in the Weddell Sea sector, not at EDC. Recomputing Eq. 3 and 4 with Table S3 end-members and Table S5 Holocene shares gives 87Sr/86Sr 0.7101 and eNd minus 4.98 for the Holocene mixture and 0.7083, minus 2.61 for the LGM; the Table S4 Holocene mean is 0.7125, minus 9.01, i.e. 4 eNd units apart, so "close agreement" for the interglacial is not shown. No misfit statistic is given. Figure 2 also shows one filled dot per sample, while Section 4.1 (p. 8, l. 244 to 246) describes the calculation "For each time interval of the LGIT". Agreement with isotopes would not discriminate between solutions either, since several end-members (S-Puna, NZ, AUS) overlap in Sr-Nd space (Figure 2). Alternative design: compare modelled and measured isotopes for the same EDC depth intervals (e.g. the Holocene EDC data of Delmonte et al., 2010), with a misfit measure and a null comparison using random or regional-mean mixtures. |
| Suggestion | Restrict the validation claim on p. 8, l. 258 to 260 and in the abstract (l. 25 to 27) to the LGM, add measured Holocene EDC isotope data if available, report a quantitative misfit in Section 4.1, and state in the caption of Figure 2 whether dots are per sample or per interval. |
| Status | verified (Table S4 content, recomputation); inferred (weak discrimination) |
| Severity | major |
| Source | SD |

**GB-19 Krätschmer et al. (2022) is cited as supporting Patagonian dominance, but the cited model attributes most LGM Antarctic deposition to Australia**

| Field | Content |
|---|---|
| Check | P13 |
| Location | p. 8, l. 275 |
| Quotation | "Model simulations also support this view, estimating that SSA and AUS" |
| Concern | The sentence continues "sources together supplied 70-90% (here, PAT+AUS is ~77%) of the dust reaching EA during the LGM (i.e., Albani et al., 2012; Krätschmer et al., 2022)". In Krätschmer et al. (2022, Clim. Past 18, 67 to 87), Table 5, the LGM deposition to Antarctica is 68 % Australian, 24 % South American, 7 % southern African; the text states that "the dust deposition over Antarctica is dominated by the Australian contribution during the LGM", with South American dust reaching up to 40 % only in a smaller region of East Antarctica. "This view" (l. 275) is the predominance of Patagonian dust (l. 271 to 274), which the cited model contradicts; the combined SSA plus AUS figure hides this. Albani et al. (2012) could only be read as abstract, which gives no source shares. |
| Suggestion | Report the split given by Krätschmer et al. (2022) on p. 8, l. 275 to p. 9, l. 277 and discuss the contrast between their model and the REE result, or remove the citation as support. |
| Status | verified (Krätschmer et al. 2022 full text); inferred (Albani et al. 2012, not readable beyond abstract) |
| Severity | moderate |
| Source | S1 |

**GB-20 Three numbers in Section 4.2 do not match Table S5**

| Field | Content |
|---|---|
| Check | P1 |
| Location | p. 9, l. 276; p. 9, l. 282; p. 9, l. 295 |
| Quotation | "(here, PAT+AUS is ~77%)" |
| Concern | Table S5, EDC, LGM: PAT 65.7 + AUS 10.2 = 75.9 %, not about 77 %. NZ LGM is 14.2 % (Table S5, and l. 209 "an average of 14%"), not "~11%" (l. 282). HS1 high-latitude share PAT 74.8 + NZ 7.1 = 81.9 %, not "84 %" (l. 295). The LGM sums on l. 293 to 294 hold (79.9 and 20.1 %). |
| Suggestion | Correct the values on p. 9, l. 276 (76 %), l. 282 (14 %) and l. 295 (82 %). |
| Status | verified |
| Severity | minor |
| Source | S3 |

**GB-21 Citations without matching entry or with an unrelated entry**

| Field | Content |
|---|---|
| Check | P4 |
| Location | p. 11, l. 365; p. 13, l. 440; Table S2, column Reference; Table S4, column Reference |
| Quotation | "with the previous Pb isotopic study (Gili et al., 2016)" |
| Concern | "Gili et al., 2016" (l. 365) has no entry; the list has Gili et al. 2017 and 2022 only. "Vallelonga et al., 2002" is cited as identifying Australia as a dust contributor to Antarctica (l. 438 to 440), but the entry is "The lead pollution history of Law Dome, Antarctica, from isotopic measurements on ice cores: 1500 AD to 1989 AD" (p. 21, l. 807 to 810); could the authors check whether Vallelonga et al. (2010, QSR 29, 247 to 255) was meant (see GB-02)? References used only in the supplement have no list: Marx et al. 2005, McGowan et al. 2005, Marx and Kamber 2010, Diaz et al. 2018 (Table S2), Aarons et al. 2017, Bory et al. 2010 (Table S4). Conversely, Gaiero et al. (2007, Chemical Geology, p. 18, l. 630 to 632) is listed but cited nowhere; the citations "Gaiero, 2007" (l. 274, Figure 2 caption) match the GRL entry. |
| Suggestion | Add Gili et al. (2016) to the list or correct the citation on p. 11, l. 365; check the Vallelonga citation on p. 13, l. 440; add a reference list to the supplement; remove or cite Gaiero et al. (2007, Chem. Geol.). |
| Status | verified (list); assumption (intended Vallelonga paper) |
| Severity | minor |
| Source | S4, S2, S1 |

**GB-22 Sub-regional attributions in Section 4.3 are not supported by data shown in the paper**

| Field | Content |
|---|---|
| Check | P8 |
| Location | p. 11, l. 366; p. 12, l. 386 to 387; p. 12, l. 392 to 396 |
| Quotation | "our model identifies the Darling sub-basin as the dominant source" |
| Concern | The discussion attributes Holocene AUS dust to the Darling sub-basin (l. 366), states that Namibian coast and riverbeds "were detected most frequently" but contribute less than Etosha and Makgadikgadi (l. 386 to 387), and dates Makgadikgadi inputs to 8.2 to 2.8 kyr and Etosha inputs to 12.2 to 5.1 kyr (l. 392 to 396). Table S1 reports only regional totals; Figure S3 shows SAF sub-regions (Etosha, Namibia, Sua) but no AUS sub-regions, and no table gives detection frequencies or per-source contributions. These statements cannot be checked. Given GB-08, the selection of individual dust sources out of 217 is also the least robust part of the output. |
| Suggestion | Add a supplementary table with per-sample contributions by sub-region (Darling, Murray, Lake Eyre, Namibian coast, Etosha, Makgadikgadi and others) and detection frequencies, and qualify the sub-regional statements on p. 11, l. 366 to 373 and p. 12, l. 385 to 398 with the identifiability test of GB-08. |
| Status | verified |
| Severity | moderate |
| Source | SD |

**GB-23 The number of YD samples given in Section 4.4 differs from Table S1**

| Field | Content |
|---|---|
| Check | P2 |
| Location | p. 12, l. 408 |
| Quotation | "8 and 7 samples in ACR and YD" |
| Concern | Table S1 lists 8 ACR rows (13032 to 14716 yr) and 9 YD rows (11779 to 12867 yr; the block label YD on supplement p. 13 spans these nine). The ACR count holds, the YD count does not. |
| Suggestion | Correct "7" to "9" on p. 12, l. 408, or state which two YD samples were excluded from the comparison. |
| Status | verified |
| Severity | minor |
| Source | S3 |

**GB-24 EDC minus EDML differences: the Holocene compares different windows, and ACR and YD values are swapped**

| Field | Content |
|---|---|
| Check | P21, P2 |
| Location | p. 13, l. 418 to 424; Figure 4 |
| Quotation | "the ACR and YD intervals exhibit a slight enrichment of Patagonian" |
| Concern | Section 4.4 compares both cores "between 7.5 and 27 kyr BP" (p. 12, l. 407). Table S5 gives EDML only for the Early Holocene (7.5 to 11.7 kyr), but Figure 4 "Holo" uses EDC Holocene 2.8 to 11.7 kyr: measured bars PAT minus 13.3 to minus 13.8, AUS plus 12.1 (zero at 856.5 px, 10 at 791 px, ± 0.15); EDC Holocene minus EDML Early Holocene gives PAT 49.0 minus 62.7 = minus 13.7 and AUS 23.1 minus 10.8 = plus 12.3, matching the text "-14%" and "+12%" (l. 424); on the stated common window (EDC Early Holocene) the values are minus 15.6 and plus 14.1. The comparison mixes a 9-kyr and a 4-kyr window. For ACR and YD the text gives PAT "+4 and +6.5%" (l. 422), but Table S5 gives ACR 68.9 minus 62.5 = plus 6.4 and YD 63.1 minus 58.4 = plus 4.7, and Figure 4 shows YD plus 4.8, ACR plus 6.3 (measured): the values are swapped. "primarily at the expense of Southern African and Australian contributions" (l. 422) holds for the ACR (SAF minus 4.4, AUS minus 7.4) but not for the YD, where SAF is plus 6.4. The LGM (NZ plus 8.0, PAT minus 8.0) and HS1 (largest difference SAF minus 5.3) statements hold. |
| Suggestion | Use EDC Early Holocene for the comparison with EDML in Figure 4 and on p. 13, l. 423 to 424, and correct the ACR and YD values and the YD statement on l. 421 to 422. |
| Status | verified (Table S5 arithmetic; bars measured) |
| Severity | moderate |
| Source | S3, AB |

**GB-25 The data are said to demonstrate the sea-level and drainage mechanisms at EDC, but the EDC record shows a gradual decline and the mechanism is inferred**

| Field | Content |
|---|---|
| Check | P15 |
| Location | p. 14, l. 466 to 467; p. 14, l. 483 to 484 |
| Quotation | "Importantly, our data demonstrate" |
| Concern | The sentence continues "that these feedback mechanisms influenced dust deposition not only in EDML ... but also in EDC". The EDC data show a provenance change; they do not test the mechanisms. The mechanisms (Meltwater Pulse 1A, shelf submergence, drainage reversal) are taken from Vanderstraeten et al. (2023) and the literature (l. 450 to 460) and supported by timing only. The EDC PAT decline is gradual rather than abrupt: Table S1 means 83.1 % (15 to 16 kyr, n 8), 72.0 % (14 to 15 kyr, n 7), 68.9 % (ACR), 63.1 % (YD), 47.1 % (Early Holocene), while the EDML abstract describes a "sudden drop" at about 14.5 kyr (cited l. 79). A gradual decline over 7 kyr is also consistent with the other explanations the manuscript itself lists (reduced transport efficiency, wet scavenging, changed trajectories, l. 308 to 314; increasing low-latitude aridity, l. 465). The conclusion attributes the decoupled flux decline to "changing atmospheric transport dynamics" (l. 484) with "due to", although transport is inferred from Markle et al. (2018), not shown. No change-point or timing analysis with age uncertainty is given. Alternative design: a change-point analysis of PAT share against MWP-1A timing with chronological uncertainty, and a comparison of the expected size of shelf-area loss with the observed share change. |
| Suggestion | Replace "demonstrate" on p. 14, l. 466 by "are consistent with", state the alternative explanations in Section 4.4, and replace "due to" on p. 14, l. 484 by "probably reflecting"; add a timing analysis if the claim is kept. |
| Status | verified (wording, Table S1 means); inferred (that timing alone cannot separate the explanations) |
| Severity | major |
| Source | S4, SD |

**GB-26 Formatting code remains in the reference list**

| Field | Content |
|---|---|
| Check | P16 |
| Location | p. 16, l. 528; p. 18, l. 606; p. 20, l. 742 |
| Quotation | "471\uc0\u8211{}501. https://doi.org/10.1191/0309133303pp386ra\" |
| Concern | Confirmed on page images 16, 18 and 20: RTF control words appear in print, 33 times "\uc0\u" (page ranges, apostrophes, accented letters such as "Go\uc0\u241{}i" for Goñi) and 18 entries ending in a backslash. Entries are otherwise readable; consistency of the list is affected. |
| Suggestion | Regenerate the reference list from the reference manager without RTF codes (p. 16 to 22). |
| Status | verified |
| Severity | minor |
| Source | S4 |

**GB-27 Figure 5 and Figure S2 lack axis titles, units and an explanation of shaded bands**

| Field | Content |
|---|---|
| Check | P29 |
| Location | Figure 5, panels A and B; Figure S2, panels A to C |
| Quotation | "Comparison of the contribution of Patagonian dust (PAT) to EDC ice core (A) and (B) the" |
| Concern | Figure 5 has no x-axis title or unit (tick labels 0.5 to 3, presumably 10^4 yr BP as in Figure 1, but no multiplier is printed), and the blue band with dashed limits between about 0.8 and 1.15 as well as the grey bands are not explained in the caption. Figure S2 gives y axes "nssCa2+ flux", "δ18O" and "deuterium excess" without units (µg m⁻² yr⁻¹ is stated only in the main text, p. 5, l. 166; per mil missing). |
| Suggestion | Add x-axis title and unit to Figure 5, explain the blue and grey bands in its caption, and add units to the y axes of Figure S2. |
| Status | verified |
| Severity | minor |
| Source | AB |

#### Minor corrections

| ID | Location | Quotation | Replacement | Source |
|---|---|---|---|---|
| KK-13 | p. 7, l. 236 | "This shift already describes by" | "This shift, already described by" | S4 |
| KK-14 | p. 8, l. 246 | "e.i. Eq.3" | "i.e. Eq. 3" | S4 |
| KK-15 | p. 8, l. 249 | "is represents by" | "is represented by" | S4 |
| KK-16 | p. 8, l. 261 | "Persistance of high-latitude dust source" | "Persistence of high-latitude dust sources" | S4 |
| KK-17 | p. 8, l. 270 | "expanding Patagonian outwash plains by ~763.10" | "expanding Patagonian outwash plains by ~763 × 10³ km²" | S4 |
| KK-18 | p. 9, l. 304 | "BP until 2.7 kyr BP" | "BP until 2.9 kyr BP" (youngest retained sample 2852 yr) | S3 |
| KK-19 | p. 10, l. 321 | "compared to 61% in our record" | "compared to 60% in our record" (49.0 + 0.0 + 11.0, Table S5; as on l. 326) | S3 |
| KK-20 | p. 10, l. 329 to 330 | "several McMurdo region sites (Section" | "several McMurdo region sites (Section 2)" | S4 |
| KK-21 | p. 10, l. 334 | "(Speirs et al., 2001)" | "(Speirs et al., 2010)" | S4 |
| KK-22 | p. 10, l. 339 to 340; p. 11, l. 348 to 349 | "Aike bog 52°S" | "Laguna Potrok Aike, 52°S" (lake sediments, as in the caption of Figure 5) | S4 |
| KK-23 | p. 10, l. 341 | "Moreno et al. (2010);" | "Moreno et al., 2010;" | S4 |
| KK-24 | p. 10, l. 342 | "(Quake and" | "(Quade and" | S4 |
| KK-25 | p. 11, l. 367; p. 13, l. 439 | "De Deccker et al. (2010)" | "De Deckker et al. (2010)", and "De Deccker et al., 2019" to "De Deckker, 2019" | S4 |
| KK-26 | p. 11, l. 374 | "(post-7.5 kry" | "(post-7.5 kyr" | S4 |
| KK-27 | p. 12, l. 382 | "(Figure S4), which is" | "(Figure S3), which is" | S4 |
| KK-28 | p. 12, l. 384 to 385 | "suggesting strengthened dust transport from southern Africa" | delete the repeated clause on l. 385 | S4 |
| KK-29 | p. 16, l. 497 | "P.B performed the measurements" | "P.G. performed the measurements" | S4 |
| KK-30 | p. 16, l. 501 | "SUPPLENTARY DATA" | "SUPPLEMENTARY DATA" | S4 |
| KK-31 | p. 20, l. 729 | "chronology for the EPICA Dome C ice core. Clim. Past." | complete the entry with volume, pages and DOI | S4 |
| KK-32 | p. 20, l. 748 | "Environùental characterization" | "Environmental characterization" | S4 |
| KK-33 | p. 20, l. 763 | "Turkian KK (eds)" | "Turekian KK (eds)" | S4 |
| KK-34 | p. 21, l. 800 | "Sudgen, D. E." | "Sugden, D. E." | S4 |
| KK-35 | p. 26, l. 858 and l. 865 | "(refs. Table S1, - open symbols)" | "(refs. Table S4, open symbols)", and on l. 865 "isotopic fingerprint (Table S4)" to "isotopic fingerprint (Table S3)" | S4 |
| KK-36 | p. 28, l. 876 | "ice cores (Table S4)." | "ice cores (Table S5)." | S4 |
| KK-37 | Figure S5, y-axis title | "PAS EDC Contribution" | "PSA EDC Contribution" | AB |

#### Verification log

| ID | Check | Checked | Values | Result |
|---|---|---|---|---|
| PP-13 | P4 | Numbering and cross-references of sections, equations, figures and tables | Sections 1 to 5 and 4.1 to 4.4 continuous; Equations 1 to 4 present; Figures 1 to 5 present and cited (Figure 5 first cited l. 339, before Figure 4 at l. 405); Figures S1 to S5 and Tables S1 to S5 present and cited; wrong targets listed as KK-04, KK-08, KK-20, KK-27, KK-35, KK-36 | no finding beyond KK |
| PP-14 | P2 | Figure 4 bars and l. 418 to 421 against Table S5 for LGM and HS1 | LGM: NZ 14.2 minus 6.2 = plus 8.0, PAT 65.7 minus 73.7 = minus 8.0 (text plus 8 %, equivalent reduction in PAT); HS1: PAT plus 3.2, PAP minus 0.2, SAF minus 5.3, AUS plus 1.9, NZ plus 0.6 (text not exceeding about 5 %); Figure 4 bars measured LGM PAT minus 7.6 to minus 8.0, NZ about plus 8 | no finding |
| PP-15 | P15 | Conclusion statements mapped to results | l. 473 to 477 to Table S5 (MIS3, LGM, HS1 PAT 65.7 to 74.8 %); l. 477 to 480 to Table S5 (Holocene AUS 23.1, PAP 11.0, SAF 10.7); l. 483 to 484 to Figure S2 (flux decline, data of Fischer et al., 2007; see GB-25); l. 485 to 487 to Figure 4 (see GB-24); no outlook or proposals for future studies in Section 5 | no finding beyond GB-24, GB-25 |
| PP-16 | P3 | Figure 2 colours against legend and text | Filled and open symbols for EDC LGM (blue), HS1 (cyan), ACR (green), YD (yellow), Holocene (dark red), Early Holocene (light red) as in legend and l. 252 to 255; domains labelled Patagonia, New Zealand, Southern Central Western Argentina, S-Puna, S-Altiplano, Australia, Southern Africa | no finding |
| PP-17 | P16 | Language and typesetting pass over p. 1 to 29 on page images | Errors listed as KK-01 to KK-37; equation layout on p. 4 and 5 differs in extracted text only and was not raised (Grundregel 4) | no finding beyond KK |

## Optional checks

| Area | What it needs | Responsible | Run |
|---|---|---|---|
| DOI resolution | one request per reference with DOI | `science-quellenapparat-pruefung` | no |
| Citation style | the name of the style | `science-zitierstil-harvard-ctr` or style rules of the journal | no |
| AI statement against publisher policy | the policy of the target publisher | this review, on request | no |
| Relation to the authors' own prior work | the authors' prior publications | this review, on request | no |
| Journal requirements | the author guidelines of the target journal | this review, on request | no |
| Scientific accuracy | access to the sources of the checked statements and a selection of sections | `science-faktenbeleg-pruefung`, `geo-frage-belegbasiert-klaeren` | no |

## Limits of this review

- Checked version: egusphere-2025-5046.pdf, 29 pages, SHA-256 f598b53d01e375844cfb549eb05b9a3407bb30cae553e603c125d5f14886c722; supplement, 22 pages, SHA-256 759cfa14195948f5772d3d6d696081932424f4296e51c812415527ed3b108ea6
- Review instances: all six ran sequentially in one context, not context-separated; this is the fallback mode of the skill and likely finds less than separate instances.
- Sources not readable: Coppo et al. (2022) full text (publisher blocked, preprint page without numbers); Neff and Bertler (2015), Albani et al. (2012) and Vanderstraeten et al. (2023) readable only as abstracts; Delmonte et al. (2004, Earth-Sci. Rev.) readable only as abstract.
- Findings with status assumption as central statement: 1 of 27 (GB-03); partial assumptions in GB-21.
- Optional checks run: 0 of 6
- Omitted instances: none
- Discarded findings: 0
- Overlap hints of the format check: the minor correction to the caption of Table S1 was merged into GB-16; GB-05 and KK-20, GB-06 and GB-21, GB-09 and GB-16 concern different subjects at the same location and were kept separate.
