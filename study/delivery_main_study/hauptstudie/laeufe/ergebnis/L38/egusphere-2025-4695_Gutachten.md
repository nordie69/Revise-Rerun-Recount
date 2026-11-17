# Review report: From XRD signal to erosion rate maps

| Field | Value |
|---|---|
| Manuscript | De Doncker, F., Herman, F., Belotti, B. and Adatte, T. (2025) From XRD signal to erosion rate maps, EGUsphere preprint, https://doi.org/10.5194/egusphere-2025-4695 |
| Checked version | egusphere-2025-4695.pdf, 37 pages, SHA-256 9c80676054f96ecd6f00f4d2a8b5ba568e03c6949e3856d363ac1c4abb42e7bd |
| Date | 2026-10-18 |
| Language | English |
| Review instances | Segments 1 to 4, Figures, Study design; sequentially checked, not context-separated; no instance omitted |
| Note | The six review instances ran one after another in a single context, not as separate agents. |

## Summary

The manuscript is a method-development study with one case study. It inverts binned X-ray diffraction (XRD) peak areas of suspended sediment, together with XRD fingerprints of source lithologies, a map of source areas and an estimate of annual sediment export, into a map of erosion rates per pixel. The forward model is linear mixing in erosion rates, parametrised in log space; the inverse uses a Gaussian maximum a posteriori formulation solved by steepest descent (SD) or a quasi-Newton (QN) scheme, with posterior covariance, resolution and a normalised posterior uncertainty as diagnostics. Synthetic forward-inverse tests on the Gornergletscher geometry (seven units, 21 tracer minerals, pixel size 300 m inferred from L = 1200 m = 4 pixels) compare SD and QN, degrade the geological map, the fingerprint distinctness (20 Jensen-Shannon levels) and the tracer number (1 to 21), and sweep five hyper-parameters. Natural tests use XRD fingerprints of seven units, a natural known-mixture test with samples from the Gorner-Grenz subcatchment, and a comparison with zircon U-Pb fingerprints for one detrital sample of 28 June 2019. Reported normalised posterior uncertainties are 0.87 (zircon), 0.82 (XRD) and 0.86 (combined); average JS distances 0.48 (zircon) and 0.57 (combined).

## Strengths

1. Every inversion is reported with posterior covariance, normalised uncertainty and the data-model misfit trade-off (eq. 20 to 22, Fig. 5 to 10, 14 to 16). This lets a reader see from the manuscript itself how weakly the natural data constrain the solution, with variance reductions of 0.13 to 0.18 (GB-08, GB-11).
2. The synthetic programme varies three degradation sources and five hyper-parameters on the real catchment geometry, with all sweep points plotted (Fig. 7 to 10). It isolates fingerprint distinctness as the condition under which the inversion fails, so the recommendations on p. 15, l. 463 to 466 have a tested basis (PP-15, PP-16, PP-21, GB-21).
3. The natural known-mixture test leaves the inversion free to attribute sediment anywhere in the catchment while sampling a subcatchment that lacks one unit (p. 14, l. 407 to 412). This is a falsifiable check of attribution with field data; extended to all units it would test the method directly (GB-28).
4. Gaps are disclosed where they arise: missing zircon data for two units and the substitute fingerprint are stated at the zircon run and are visible in Fig. 14, and code and synthetic data are deposited (PP-08, GB-36).

## Weaknesses

1. The evidence for accuracy rests on synthetic tests that share forward model and tracer matrix with the inversion, add no stated noise and use a prior equal to the true mean; even then the QN posterior exceeds the true peak by about 2.3 (75 %), and Fig. 5g and 6g do not show QN to be more accurate than SD. Repeat the tests with noise, a prior independent of the truth, perturbed fingerprints and several true maps, and report peak and summed errors (GB-16, GB-19, GB-20).
2. The natural tests do not support the claims drawn from them: the combination with zircon raises the normalised uncertainty relative to XRD alone (0.86 against 0.82), the zircon benchmark is confounded by missing fingerprints and has no accuracy metric, and the known-mixture test checks one small unit while units outside the subcatchment receive erosion. Define stability, compare tracers on the same source set and report attribution for every unit (GB-08, GB-15, GB-28).
3. Core steps of the method are either not reproducible or inconsistent with the model: per-sample maximum normalisation does not preserve linear mixing, the resolution operator is undefined and its plotted values exceed what the problem size allows, several equations are wrong as printed, and XRD processing, export estimate and prior are not specified. Give the formulas and settings, and test mixing preservation with laboratory mixtures (GB-07, GB-09, GB-10, GB-12, GB-13, GB-30).
4. Several statements do not follow from the figures or are not measured: the text of the sweeps contradicts Fig. 10, Fig. 8 shows 14 of 20 cases, the hyper-parameters used are not those the sweeps favour, cost-effectiveness and novelty of non-linear mixing are asserted, and the Introduction appears twice. Rewrite these passages from the plotted values and remove the duplicated section (GB-01, GB-03, GB-06, GB-17, GB-23, GB-25).

## Findings by segment

### Segment 1: Abstract, introduction (p. 1 to 5)

#### Substantive findings

**GB-01 Time- and cost-effectiveness is claimed as a result but not measured**

| Field | Content |
|---|---|
| Check | P33 |
| Location | p. 1, l. 3 to 4; p. 2, l. 40 to 42; p. 3, l. 74 to 75 |
| Quotation | "In this study, we validate a time- and cost-effective fingerprinting approach based on X-ray diffraction (XRD) data." |
| Concern | The motivation for XRD is clear and plausible. However, no cost per sample, analysis time or comparison with zircon U-Pb dating is reported anywhere; the only support is the citation that other methods are "expensive and time-consuming" (p. 2, l. 35). "We validate" (abstract) and "we show and validate the potential ... as a cost- and time-efficient approach" (p. 3, l. 74 to 75) present it as an outcome of this study. |
| Suggestion | Report cost and time per sample for XRD and for zircon dating in Sect. 3.4 or 4.2.2, or reword the abstract and p. 3, l. 74 to 75 as motivation supported by literature. |
| Status | verified |
| Severity | moderate |
| Source | SD |

**GB-02 The abstract states consistent convergence; the results report non-convergence**

| Field | Content |
|---|---|
| Check | P6 |
| Location | p. 1, l. 7; p. 12, l. 353; Fig. 8 |
| Quotation | "Forward-inverse tests with synthetic data demonstrate consistent convergence of the posterior solution." |
| Concern | Sect. 4.1.3 reports "In many of these cases, the inversion fails to converge to a stable posterior solution" (p. 12, l. 353), and the caption of Fig. 8 says the most blended example "did not have a stable solution". The abstract omits this limit. |
| Suggestion | Qualify the abstract sentence with the range of fingerprint distinctness (JS distance) in which convergence was obtained. |
| Status | verified |
| Severity | moderate |
| Source | SD |

**GB-03 The Introduction appears twice**

| Field | Content |
|---|---|
| Check | P16, P4 |
| Location | p. 1, l. 9; p. 3, l. 76 |
| Quotation | "2 Introduction" |
| Concern | Section 2 (p. 3, l. 76 to p. 5, l. 142) repeats Section 1 (p. 1, l. 9 to p. 3, l. 75) word for word: 1153 words each, difflib ratio 1.0 (arbeit_S1/dup.py). Confirmed at the page images of p. 1, 3 and 5. All later sections are numbered one too high (Methods is Section 3). |
| Suggestion | Delete Section 2 and renumber Sections 3 to 6. |
| Status | verified |
| Severity | minor |
| Source | S4 |

**GB-04 A reference cited for pollen fingerprinting is a theology article**

| Field | Content |
|---|---|
| Check | P13 |
| Location | p. 2, l. 31; p. 19, l. 597 to 598 |
| Quotation | "plant pollen content (Brown, 1985; Kobe, 2021)" |
| Concern | The entry is "Kobe, S. L.: Ubuntu as a spirituality of liberation for black theology of liberation, HTS Teologiese Studies / Theological Studies, 77". Its landing page (hts.org.za, article 6176) gives the keywords black, liberation, theology, spirituality, Ubuntu and does not mention pollen or sediment. Brown (1985) supports the statement; Kobe (2021) does not. |
| Suggestion | Replace Kobe (2021) at p. 2, l. 31 by a study on pollen as a sediment tracer, or delete it, and remove the entry on p. 19. |
| Status | verified |
| Severity | minor |
| Source | S1 |

**GB-05 Earlier XRD-based mineralogical unmixing for sediment provenance is not cited**

| Field | Content |
|---|---|
| Check | P14, P28 |
| Location | p. 2, l. 36 to 42; p. 13, l. 403 to 406 |
| Quotation | "X-ray diffraction (XRD) has recently gained attention as a proxy for mineral abundance in provenance analysis but remains underutilized (Das et al., 2023)." |
| Concern | The manuscript builds on Das et al. (2023, 2024). Quantitative XRD mineralogy was unmixed into source proportions earlier: Eberl (2004) for bed and suspended sediment of the Yukon River system, and Andrews and Eberl (2012), who tested the SedUnMix program with eleven artificial mixtures of four source sediments and recommend testing with known artificial mixtures before application. Neither is among the 64 entries of the reference list. The second bears directly on p. 13, l. 403 to 406, where a laboratory known-mixture test is replaced by a natural analogue. The claim that XRD is underutilized is made without a stated search. |
| Suggestion | Cite and discuss Eberl, D. D. (2004) Quantitative mineralogy of the Yukon River system: changes with reach and season, and determining sediment provenance, American Mineralogist 89, 1784 to 1794; and Andrews, J. T. and Eberl, D. D. (2012) Determination of sediment provenance by unmixing the mineralogy of source-area sediments: the "SedUnMix" program, Marine Geology 291 to 294, 24 to 33, https://doi.org/10.1016/j.margeo.2011.10.007; place them at p. 2, l. 36 to 42 and in Sect. 4.2.1, and state what this study adds. |
| Status | verified |
| Severity | moderate |
| Source | S1 |

**GB-06 The claimed novelty of a non-linear mixing model does not match the forward model**

| Field | Content |
|---|---|
| Check | P15 |
| Location | p. 2, l. 58 to 60; p. 5, l. 157 to 158; p. 15, l. 454 to 455 |
| Quotation | "The novelty of our method lies in the spatially informed approach of this underdetermined inversion problem, and in the incorporation of non-linear mixing model." |
| Concern | Eq. 3 reads d = A exp(epsilon) with exp(epsilon_j) the erosion rate of pixel j, so mixing is linear in the erosion rates; the non-linearity comes from the log parametrisation that imposes positivity (p. 5, l. 157 to 158). The introduction contrasts the method with approaches that "implicitly rely on a linear mixing scheme" (p. 2, l. 59). The spatially informed inversion is that of De Doncker et al. (2020), as p. 2, l. 60 to 61 states. |
| Suggestion | Describe the model at p. 2, l. 58 to 60 and p. 15, l. 454 to 455 as linear mixing with a log-parametrised inversion, and state what is new relative to De Doncker et al. (2020). |
| Status | verified |
| Severity | moderate |
| Source | S4 |

**GB-07 The total sediment export estimate is an input without value or source**

| Field | Content |
|---|---|
| Check | P8 |
| Location | p. 3, l. 65 to 66; p. 5, l. 159 to 160; p. 15, l. 452 to 454 |
| Quotation | "an estimate of the total annual suspended sediment export from the catchment" |
| Concern | Eq. 2 scales d by the total erosion rate. For the natural runs neither the export value, its source (the "multi-year suspended sediment datasets" named at p. 9, l. 267 to 268), nor the conversion to an erosion rate (catchment area, density) is given, while the absolute rates in Fig. 13 to 16 depend on it. |
| Suggestion | Give value, years, data source and conversion in Sect. 4, and show where eq. 2 uses it. |
| Status | verified |
| Severity | moderate |
| Source | SD |

**GB-08 Statements that combining XRD with zircon improves the solution contradict the reported uncertainties**

| Field | Content |
|---|---|
| Check | P2, P15 |
| Location | p. 3, l. 72 to 73; p. 5, l. 139 to 140; p. 15, l. 446 to 449; p. 15, l. 461 to 463 |
| Quotation | "showing that integrating XRD with zircon data improves the stability and sharpness of the posterior solution" |
| Concern | Normalised posterior uncertainty: zircon 0.87, XRD 0.82, combined 0.86 (p. 14, l. 436; p. 15, l. 442; p. 15, l. 447). Relative to XRD alone the combination raises it by 0.04 (4.9 %); relative to zircon alone it lowers it by 0.01. Variance reductions, 1 minus the value: 0.13, 0.18, 0.14. Neither "stability" nor "sharpness" is measured. The discussion states that combination "proves to further stabilize and improve the posterior solution" (p. 15, l. 462). |
| Suggestion | Report the combination against XRD alone and against zircon alone separately, with defined metrics for stability and sharpness, and restate p. 3, l. 72 to 73, p. 15, l. 446 and p. 15, l. 461 to 463 to what these metrics show. |
| Status | verified |
| Severity | major |
| Source | S3 |

#### Minor corrections

| ID | Location | Quotation | Replacement | Source |
|---|---|---|---|---|
| KK-01 | p. 1, l. 5 | "Quasi-Newtonian" | "quasi-Newton" | S4 |
| KK-02 | p. 1, l. 11; p. 18, l. 567 to 568 | "E., 2009" | "Walling, 2009", with the entry author "Walling, D. E." and "oCLC" corrected to "OCLC" | S4 |
| KK-03 | p. 2, l. 48 to 49 | "the Non-Linear Least Squares (NLLS) (a constrained linear regression)" | "the Non-Negative Least Squares (NNLS) (a constrained linear regression)" | S1 |
| KK-04 | p. 2, l. 50 | "Generalist Likelihood Uncertainty Estimation (GLUE)" | "Generalized Likelihood Uncertainty Estimation (GLUE)" | S1 |
| KK-05 | p. 2, l. 51 | "Maximal Likelihood Estimation (MLE)" | "Maximum Likelihood Estimation (MLE)" | S1 |
| KK-06 | p. 2, l. 61; p. 11, l. 333 | "the inversion framework validated in (De Doncker et al., 2020)" | "the inversion framework validated by De Doncker et al. (2020)"; likewise "the map proposed by Steck et al. (2015)" | S4 |

#### Verification log

| ID | Check | Checked | Values | Result |
|---|---|---|---|---|
| PP-01 | P13 | Statements from cited works with numbers, rankings or judgements in Sect. 1 | Kobe 2021 read (GB-04); Gergel et al. 2002 identified as "Landscape indicators of human impacts to riverine systems", Aquatic Sciences 64, 118 to 128 (KK-17); Das et al. 2023 for "expensive and time-consuming" and "underutilized" not readable | no further finding; Das et al. 2023 unverified |
| PP-02 | P14 | Four searches: "SedUnMix unmixing mineralogy XRD sediment provenance Andrews Eberl"; "inversion detrital zircon provenance erosion rate map glacier catchment spatially variable erosion suspended sediment"; "X-ray diffraction mineralogical fingerprinting glacial meltwater suspended sediment sources unmixing"; "Das Remesan Gupta 2023 X-Ray Diffraction Spectral Fingerprinting" | Candidates Eberl 2004 and Andrews and Eberl 2012, both absent from the list; hits on this manuscript and its later versions not opened | finding GB-05 |
| PP-03 | P28 | Gap and novelty claims | "remains underutilized" (p. 2, l. 36 to 37); "The novelty of our method lies in" (p. 15, l. 454) | covered by GB-05 and GB-06 |

### Segment 2: Methods, study area (p. 5 to 10)

#### Substantive findings

**GB-09 Several equations are incorrect as printed; eq. 19 cannot be evaluated as written**

| Field | Content |
|---|---|
| Check | P8, P25 |
| Location | p. 6, l. 175; p. 7, l. 189; p. 7, l. 197; p. 7, l. 201; p. 8, l. 215; p. 8, l. 219 |
| Quotation | "Combining eq. 14 and eq. 15 in eq. 10 so the total misfit gradient becomes:" |
| Concern | Confirmed at the page images: eq. 5 has no relation sign between posterior and likelihood; eq. 9 reads sigma_m^2 exp(s^2/L^2) without a minus sign, which grows with distance and is not a valid covariance; eq. 12 writes the Jacobian as A exp(epsilon), a vector, instead of A diag(exp(epsilon)); eq. 14 has G where eq. 16 has G^T; eq. 18 and 19 mix the iteration indices n and k. Eq. 19 inverts G^T Cd^-1 G alone. With m = 21 tracers and n pixels, n much larger than m (p. 6, l. 170 to 172), this n by n matrix has rank at most 21 and is singular; eq. 20 includes Cm^-1, eq. 19 does not. |
| Suggestion | Correct eq. 5, 9, 12, 14, 18 and 19 (for eq. 19 presumably (G^T Cd^-1 G + Cm^-1)^-1) and state which form the deposited code implements. |
| Status | verified for the printed forms; inferred for the singularity |
| Severity | moderate |
| Source | SD |

**GB-10 Resolution values close to 1 are not possible for the stated problem size under the cited definition**

| Field | Content |
|---|---|
| Check | P8, P3 |
| Location | p. 8, l. 230 to 235; p. 16, l. 483 to 484; Fig. 5d; Fig. 14; Fig. 15; Fig. 16 |
| Quotation | "So R is close to the identity operator I if we have perfectly resolved the" |
| Concern | R is defined only through eq. 21; its formula is not given. For the linearised Gaussian problem of Tarantola (2005), which the manuscript cites, R equals C̃m G^T Cd^-1 G, so its rank and trace are at most m = 21. Measured in Fig. 5d: 91.8 % of colour-matched pixels lie at or above 0.98, median 0.994 (colour bar 1.00 at 1064 px, 0.90 at 1344 px; 23490 of 121526 pixels matched within tolerance 40), over a raster of about 43 by 25 cells (cell edge about 12 px at 300 dpi). The trace would then be several hundred. Fig. 5h gives a normalised covariance trace of 0.742, about 26 % variance reduction, which also does not fit diagonal values near 1. Is R computed differently, for example normalised per row, and with which formula? |
| Suggestion | Give the formula for R in Sect. 3.3, check its trace against m, and redraw Fig. 5d, 6d and 14 to 16 if needed; until then do not use the resolution maps to assess reliability (p. 16, l. 483 to 484). |
| Status | inferred |
| Severity | major |
| Source | SD |

**GB-11 Normalised posterior uncertainty has two definitions**

| Field | Content |
|---|---|
| Check | P38 |
| Location | p. 8, l. 237 to 239; p. 14, l. 436; Fig. 7; Fig. 8; Fig. 9; Fig. 10 |
| Quotation | "values closer to zero indicate a maximal variance reduction after the inversion" |
| Concern | Eq. 22 defines a ratio of square roots of the posterior and prior covariance, per pixel. p. 14, l. 436 defines the total value as tr(Cm,post)/tr(Cm) without square roots. Fig. 7 to 10 label the axis "Trace(post. cov.)" or "Trace(post.covar.)" under the titles "Posterior uncertainty" and "Normalised posterior uncertainty". It cannot be determined which quantity the values 0.74, 0.82, 0.86 and 0.87 are. |
| Suggestion | Define one quantity with its formula in Sect. 3.3 and use the same name and formula in Sect. 4 and on the figure axes. |
| Status | verified |
| Severity | moderate |
| Source | S2 |

**GB-12 XRD processing is not specified enough to reproduce the fingerprints**

| Field | Content |
|---|---|
| Check | P8, P35 |
| Location | p. 9, l. 250 to 259; p. 13, l. 396 to 398 |
| Quotation | "diagnostic 2θ windows for each mineral are selected from RRUFF database reference spectra" |
| Concern | Not given: number of source samples per unit; size fraction and preparation of the suspended sediment; instrument, radiation, scan range and step; version and thresholds of the WinXRD Peak Finder; the 2θ window and RRUFF entry for each of the 21 minerals. "We average the total peak area within the 2θ windows" (l. 259 to 260) is undefined where windows of two minerals overlap. |
| Suggestion | Add a table of the 21 minerals with RRUFF identifiers and 2θ windows and a paragraph on instrument settings and sample numbers in Sect. 3.4. |
| Status | verified |
| Severity | moderate |
| Source | SD |

**GB-13 Maximum normalisation per sample is incompatible with the linear mixing model, and a second normalisation is undocumented**

| Field | Content |
|---|---|
| Check | P9, P8 |
| Location | p. 9, l. 260 to 264; p. 5, l. 150 to 152; Fig. 5k; Fig. 11; Fig. 15; Fig. 16 |
| Quotation | "these are normalized within each sample by dividing by the maximum observed peak area" |
| Concern | Eq. 1 assumes that the detrital value of each tracer is the erosion-weighted mean of the source values. If raw peak areas mix linearly, a mixture divided by its own maximum is not the weighted mean of sources each divided by their own maxima, because the divisor differs per sample and comes from different minerals. The synthetic tests generate data with eq. 1 directly and cannot reveal this. Fig. 15, 16 and 5k show bars that sum to one per tracer across units, a second normalisation not described in the methods (Fig. 11, by contrast, shows per-unit bars with the longest bar of each unit at full length). |
| Suggestion | State which normalised quantities enter A and d, and show that mixing is preserved, for example with laboratory mixtures of two or three source powders in known proportions as in Andrews and Eberl (2012), or use a normalisation that preserves linearity (internal standard, total peak area). |
| Status | verified for the described normalisations; inferred for the incompatibility |
| Severity | major |
| Source | SD |

**GB-14 Names of the catchment, the units and the eclogites vary**

| Field | Content |
|---|---|
| Check | P38 |
| Location | p. 9, l. 267; p. 9, l. 272; p. 10, l. 299; p. 12, l. 340; p. 13, l. 392; p. 14, l. 411; p. 14, l. 432; p. 15, l. 463; Fig. 11; Fig. 12; Fig. 15 |
| Quotation | "on the Gorner-gletscher catchment" |
| Concern | Catchment: "Gorner-gletscher" (l. 267, Fig. 11), "Gornergletscher" (l. 272, l. 282), "Gorner Glacier" (l. 392, l. 400), "Gorner gletscher" (l. 463). Unit: "Zermatt Saas-Fee" (l. 299), "Zermatt-Saas-Fee" (l. 340), "Zermatt - Saas Fee" (l. 411, l. 414), "Zermatt-Saas Fee" (l. 431), "Zermatt- Saas Fee" (Fig. 12 caption). Monte Rosa gneiss unit: "garnet-gneiss (MR g-g)" (l. 432), "gneiss, micaschist" (Fig. 11, 13), "MR gneiss, mica" (Fig. 15, 16), "garnet gneiss and micaschist" (Fig. 4). The Fig. 11 caption has "Turftgrat" and "ecologites". These denote the same objects. |
| Suggestion | Fix one name per object (for example "Gornergletscher", "Zermatt-Saas Fee", "Monte Rosa gneiss and micaschist") and use it in text, captions and legends; correct "Tuftgrat" and "eclogites" in the Fig. 11 caption. |
| Status | verified |
| Severity | minor |
| Source | S2 |

**GB-15 Research question 3 asks for accuracy, which the zircon comparison cannot measure, and the comparison is confounded**

| Field | Content |
|---|---|
| Check | P10, P9 |
| Location | p. 10, l. 284 to 285; p. 14, l. 420 to 422; p. 14, l. 430 to 435 |
| Quotation | "to assess how the incorporation of XRD-based fingerprints alongside zircon data improves the stability and accuracy of the posterior solution" |
| Concern | The manuscript discloses the zircon gaps where the run is described. Still, natural data have no reference map, so accuracy is not measurable, and "stability" has no metric. Zircon fingerprints are missing for the ZSF metabasites and replaced by the Monte Rosa granite fingerprint for MR g-g (l. 430 to 434), so the instability of the zircon run (l. 435) may come from these gaps rather than from the tracer type; the benchmark conclusion at l. 439 does not separate the two causes. |
| Suggestion | Define stability (for example the spread over repeated inversions with resampled data), run the XRD inversion with the same two units removed or merged so both tracers face the same source set, and confine accuracy statements to the synthetic tests. |
| Status | verified |
| Severity | major |
| Source | SD |

#### Minor corrections

| ID | Location | Quotation | Replacement | Source |
|---|---|---|---|---|
| KK-07 | p. 6, l. 180 | "becomes Tarantola (2005):" | "becomes (Tarantola, 2005):" | S4 |
| KK-08 | p. 8, l. 236 | "considerately" | "considerably" | S4 |
| KK-09 | p. 9, l. 245 | "weighed by the model covariance" | "weighted by the model covariance" | S4 |
| KK-10 | Fig. 3c | "quarz pattern alignment" | "quartz pattern alignment" | AB |
| KK-11 | Fig. 4 legend; Fig. 12 legend | "caclcite-zoisite amphibolites" | "calcite-zoisite amphibolites"; also "silimanite" to "sillimanite", "biotite schits" to "biotite schist", "GornergratPermo-Mesozoic" to "Gornergrat Permo-Mesozoic" | AB |

#### Verification log

| ID | Check | Checked | Values | Result |
|---|---|---|---|---|
| PP-04 | P10 | Design sketch (instanz_SD.md): aims, three natural-data questions, chain from frame to result | Q1 alignment (Fig. 11), Q2 subcatchment (Fig. 13), Q3 zircon (Fig. 14 to 16); Q1 and Q2 not taken up in Sect. 5 or 6; cost-effectiveness has no question and no instrument | findings GB-01, GB-15, GB-26, GB-28 |
| PP-05 | P29 | Figure register (instanz_AB.md) and references in the text | 16 figures, numbered 1 to 16 without gap, each referenced in its section (first references p. 5, l. 146 to p. 15, l. 445); no tables | no finding |
| PP-06 | P38 | Method names and abbreviations | QN and "quasi-Newton" (l. 211) against "Quasi-Newtonian" (l. 5); SD used only for steepest descent; 21 minerals in l. 393 to 396 counted with Python | KK-01; names in GB-14 |
| PP-07 | P7, P30 | Method versions and corrections over time | one method version; SD gradient normalisation from "initial experiments" (p. 11, l. 312) is part of the described method | no finding |
| PP-08 | P37 | Values changed after the fact | MR g-g zircon fingerprint replaced by MR granite, disclosed at p. 14, l. 433 to 434 and visible as identical shares in Fig. 14 | no finding |
| PP-09 | P17 | Location of disclosed limits | grain size, preferred orientation, peak overlap and storage only in Sect. 5 (p. 15, l. 466 to 476), not in Sect. 3.4 | covered by GB-35 |
| PP-10 | P19 | Provenance class of the key statements | robustness and hyper-parameter choices rest on model-generated data only; the manuscript says so ("fully synthetic", p. 10, l. 280) | no separate finding |
| PP-11 | P26, P27 | Guarantees and unchecked components | "should help cancel out such effects" (p. 15, l. 473) untested; unchecked maximum normalisation feeds A and d | covered by GB-13 |
| PP-12 | P5, P32, P34, P36 | Rules, error estimates, selections, recollections | no formal rule with thresholds; no claim of error-free results; three of 20 blending cases shown as examples with a selection rule (most, half, none); no recollection statements | no finding |

### Segment 3: Results (p. 10 to 15)

#### Substantive findings

**GB-16 The synthetic tests are built in a way that favours the inversion**

| Field | Content |
|---|---|
| Check | P9 |
| Location | p. 10, l. 288 to 292; p. 10, l. 295; p. 16, l. 482 to 483 |
| Quotation | "Using synthetic forward-inverse experiments, we show that the true erosion pattern can be reliably recovered" |
| Concern | Data are generated with the same forward model and, except in scenario 1, the same tracer matrix as the inversion; adding noise is not mentioned (the word occurs only for XRD background, p. 9, l. 255); the prior equals the average true erosion rate (l. 295, p. 11, l. 326), which uses the answer; one true map with one hotspot is tested. Larger smoothing lowers the error because it pulls the posterior towards that prior (p. 13, l. 374 to 376). |
| Suggestion | Repeat the tests with noise at the stated sigma_d, a prior not derived from the truth, perturbed fingerprints in the forward model and several true maps (two hotspots, a hotspot in a small unit), and report errors relative to a prior-only solution. |
| Status | inferred |
| Severity | major |
| Source | SD |

**GB-17 The hyper-parameters used are not those the sweeps favour, and the Fig. 10 annotations are unexplained**

| Field | Content |
|---|---|
| Check | P29, P3 |
| Location | p. 10, l. 293 to 294; p. 11, l. 324 to 326; p. 14, l. 426 to 428; Fig. 10 |
| Quotation | "a smoothing distance of 4 times the pixel size (L = 1200 m), a model standard deviation of 3" |
| Concern | The trade-off panels of Fig. 10 mark "L = 3000 m", "σm = 6.2", "σd = 0.003 mm/y", "μ = 0.1" and "n_m = 25"; three of five differ from the values used throughout (1200 m, 3, 0.01 mm/y), and the caption does not say what the marked points are. In the smoothing sweep (x ticks 500 at 657.5 px, 3000 at 963.0 px; y ticks 250 at 674.0 px, 75 at 905.5 px) the error is 214.8 ± 0.8 at 1230 m and 76.4 ± 0.8 at 3002 m, so the value used is not the one the sweep favours, while p. 3, l. 70 says the hyper-parameters are optimised. |
| Suggestion | Explain the marked points in the Fig. 10 caption and state for each hyper-parameter in Sect. 4.1.4 why the value used was chosen. |
| Status | verified |
| Severity | moderate |
| Source | AB |

**GB-18 Pixel size and number of pixels must be inferred**

| Field | Content |
|---|---|
| Check | P22 |
| Location | p. 10, l. 294; p. 12, l. 372 |
| Quotation | "(L = 1200 m)" |
| Concern | The pixel size follows only from 1200/4 = 300 m and 3000/10 = 300 m. The number of pixels n, needed to judge how underdetermined the problem is with m = 21 tracers, is not stated. |
| Suggestion | State pixel size and n in Sect. 3.2 or 4.1. |
| Status | inferred |
| Severity | minor |
| Source | S3 |

**GB-19 Fig. 5c shows the QN posterior exceeding the true peak by about 2.3, three quarters of the peak value**

| Field | Content |
|---|---|
| Check | P3 |
| Location | p. 10, l. 296 to 297; Fig. 5a; Fig. 5c |
| Quotation | "closely matches the true erosion pattern, both in spatial distribution and magnitude (Figure 5B)" |
| Concern | Measured by matching pixel colours to the colour bars at 300 dpi: the true maximum is 3.03 (colour bar 0.5 at 886.0 px, 3.0 at 637.5 px); the difference true minus posterior at the same cell is minus 2.26 (colour bar 2 at 657.5 px, minus 2 at 903.0 px; about ±0.02 calibration plus colour tolerance), with plus 1.37 on the adjacent cells. The posterior is about 5.3 where the truth is 3.0, an excess of 75 %; Fig. 5b saturates at 3.0 and hides this. |
| Suggestion | Extend the colour scale of Fig. 5b to the posterior maximum and replace "closely matches ... magnitude" at p. 10, l. 296 to 297 by the measured peak error. |
| Status | verified |
| Severity | major |
| Source | AB |

**GB-20 Fig. 5g and 6g do not show QN to be more accurate than SD**

| Field | Content |
|---|---|
| Check | P3, P11 |
| Location | p. 11, l. 312 to 317; p. 11, l. 320 to 321; Fig. 5g; Fig. 6g; Fig. 6c |
| Quotation | "as it provides a more stable and accurate reconstruction of the erosion rate patterns" |
| Concern | Sum of absolute differences measured: QN 200.9 ± 0.6 after 100 iterations, minimum 197.3 ± 0.6 near iteration 22 (y ticks 340 at 1510.5 px, 200 at 1946.5 px); SD 193.1 ± 0.8 after 200 iterations (y ticks 375 at 1488.0 px, 200 at 1936.5 px), 7.8 lower than QN. The peak difference in Fig. 6c is about minus 1.58 against minus 2.26 in Fig. 5c. The SD iteration count of 200 appears only in Fig. 6. The reference "(Figure 6G versus Figure 6G)" (l. 317) compares a panel with itself. |
| Suggestion | State the SD iteration count, compare both schemes at equal iterations and at convergence with numbers, restrict the claim at l. 320 to 321 to what these show (for example speed of convergence), and correct l. 317 to the intended panels (for example "Figure 6H versus Figure 5H"). |
| Status | verified |
| Severity | moderate |
| Source | AB |

**GB-21 The ranking of degradation factors depends on the chosen degradation ranges**

| Field | Content |
|---|---|
| Check | P21 |
| Location | p. 11, l. 336 to 337; p. 12, l. 363 to 365; Fig. 7; Fig. 8; Fig. 9 |
| Quotation | "Geological map uncertainty follows as the second most influential factor." |
| Concern | Maximum absolute error measured in the figures: scenario 1 (map) 274.8 ± 0.2, scenario 3 (one tracer) 347.1 ± 0.3, scenario 2 (blending) about 676 400. By these values tracer reduction exceeds map uncertainty. The ranges are not comparable (area mismatch up to about 1.1e7 m², JS down to 0.25, tracers down to 1). Scenario 1 has three maps, and the map with minimal changes gives a lower error (193.4 ± 0.2) than the identical map, so "the greater the mismatch ... the larger the discrepancy" (l. 336 to 337) rests on two of three points. |
| Suggestion | Express each degradation on a common scale or state the ranking as conditional on the ranges tested, and add more maps to scenario 1. |
| Status | verified |
| Severity | moderate |
| Source | S3 |

**GB-22 The Jensen-Shannon distance is not reported for the XRD-only case**

| Field | Content |
|---|---|
| Check | P11 |
| Location | p. 12, l. 345 to 347; p. 15, l. 447 to 448 |
| Quotation | "the average Jensen-Shannon distance between source fingerprints increases from 0.48 to 0.57" |
| Concern | JS distance is reported for zircon (0.48) and combined (0.57), not for XRD alone. In the synthetic tests errors rise below 0.55 (p. 12, l. 352), so 0.48 lies in that range. JS is defined for probability distributions; the fingerprints are maximum-normalised to 0 to 1 (p. 9, l. 261 to 262), and the normalisation used for JS is not stated. |
| Suggestion | Report the JS distance for all three natural cases and state how fingerprint vectors are normalised before JS is computed. |
| Status | verified |
| Severity | moderate |
| Source | S3 |

**GB-23 Fig. 8 shows 14 of 20 blending cases, and the text value "700 mm/yr" does not match the plotted metric**

| Field | Content |
|---|---|
| Check | P3, P20 |
| Location | p. 12, l. 348 to 353; Fig. 8 |
| Quotation | "with errors exceeding 700 mm/yr" |
| Concern | Counted at the enlarged middle panel: 14 markers, at JS 0.249, 0.272, 0.338, 0.359, 0.441, 0.461, 0.481, 0.501, 0.521, 0.541, 0.561, 0.581, 0.602 and 0.624 (x ticks 0.25 at 986.5 px, 0.60 at 1440.5 px). l. 348 says 20 values were tested; the caption excludes only the most blended one, so five are missing without explanation. Absolute error (y ticks 0 at 1395.5 px, 700000 at 891.5 px, ±1400): 6100, 322 100 and 676 400 below JS 0.44; 1250 to 19 600 between 0.44 and 0.54, four of them above 700 beyond the uncertainty. The axis is a sum over pixels without unit, so "mm/yr" does not apply. |
| Suggestion | Show or list all 20 cases with a symbol for non-converged runs, give the unit of the summed error or report a mean per pixel, and restate the thresholds at l. 352 to 353 with the measured values. |
| Status | verified |
| Severity | moderate |
| Source | AB |

**GB-24 The x axes of Fig. 9 are labelled as JS distance but show the number of tracers**

| Field | Content |
|---|---|
| Check | P29 |
| Location | p. 12, l. 356 to 358; Fig. 9 |
| Quotation | "Avg. JS distance between lithologies" |
| Concern | The lower row has ticks 0.0 to 20.0 and a colour bar "Number of tracrs", so the axes show tracer counts; the axis label is copied from Fig. 8. The y-axis label of the left panel carries a stray second sum sign (page image p. 30). |
| Suggestion | Label the x axes "Number of tracers", correct "tracrs" and remove the stray sign. |
| Status | verified |
| Severity | minor |
| Source | AB |

**GB-25 Text descriptions of the parameter sweeps contradict Fig. 10**

| Field | Content |
|---|---|
| Check | P3 |
| Location | p. 12, l. 371 to 374; p. 13, l. 380 to 389; Fig. 10 |
| Quotation | "Very low data standard deviation values lead to large differences between the posterior and true erosion rate maps" |
| Concern | Row 3: the left panel has the offset +1.974e2; measured values run from 197.420 (sigma_d up to about 0.1 mm/y) to 197.440 (about 0.9 mm/y), a range of 0.0101 %, with no maximum at low sigma_d and no minimum followed by a plateau; model misfit varies from 1.5614 to 1.5622 (0.05 %), not "rapidly" (l. 384). Row 1: the error falls monotonically from 266.3 at about 640 m to 76.4 at 3002 m, and no value beyond 3000 m is shown, so oversmoothing beyond 3000 m (l. 372 to 374) has no plotted support. Row 5: 15 iterations give 200.8 ± 0.25 and 195 iterations 200.9 ± 0.25; only the run at about 5 iterations (about 269) fails, against "Only when the maximum number of non-linear steps is reduced below 25" (l. 387). "10-2" at l. 384 lacks the superscript. |
| Suggestion | Rewrite p. 12, l. 371 to p. 13, l. 389 from the plotted values, extend the smoothing sweep beyond 3000 m if the oversmoothing claim is kept, show the offset of row 3 in the panel, and set "10^-2" as a superscript. |
| Status | verified |
| Severity | moderate |
| Source | AB |

**GB-26 Agreement of the XRD fingerprints with known lithology is asserted, not tested**

| Field | Content |
|---|---|
| Check | P31 |
| Location | p. 13, l. 393 to 394; p. 13, l. 399 to 401; p. 10, l. 275; p. 10, l. 278; Fig. 11 |
| Quotation | "The mineralogical fingerprints derived from processed and binned XRD data align well with established knowledge of the" |
| Concern | No expected composition per unit and no comparison measure are given. Calcite is not among the 21 minerals although the units include "calcareous mica schists" (p. 10, l. 275) and "marbles" (p. 10, l. 278); dolomite and ankerite are near zero for ZSF sediments in Fig. 11. The sentence continues "supporting the 1) the robustness" (l. 400), with a doubled article. |
| Suggestion | Tabulate the expected main minerals per unit from Bearth (1953) and Steck et al. (2015) against the measured ranks, explain the choice of the 21 minerals including the absence of calcite, and correct l. 400 to "supporting 1) the robustness". |
| Status | verified for the absence of calcite; inferred for its relevance |
| Severity | moderate |
| Source | SD |

**GB-27 The mineral called "Chrysolite" in the text is "Chrysotile" in all fingerprint figures**

| Field | Content |
|---|---|
| Check | P38 |
| Location | p. 13, l. 395; Fig. 11; Fig. 15; Fig. 16 |
| Quotation | "Dolomite, Diopside, Chrysolite, Antigorite" |
| Concern | Fig. 11, 15 and 16 label the tracer "Chrysotile" (page images p. 32, 36, 37), and p. 10, l. 274 names chrysotile. Chrysolite is a name used for olivine, chrysotile a serpentine mineral; the RRUFF reference window depends on which was used. |
| Suggestion | Write "Chrysotile" at p. 13, l. 395 if that is the reference pattern used, and give its RRUFF entry. |
| Status | verified |
| Severity | moderate |
| Source | S2 |

**GB-28 The natural known-mixture test checks one unit, while units outside the subcatchment receive erosion**

| Field | Content |
|---|---|
| Check | P9, P11 |
| Location | p. 13, l. 403 to p. 14, l. 418; Fig. 12; Fig. 13 |
| Quotation | "Only the Zermatt - Saas Fee sediment unit does not have outcrops in the Gorner-Grenz subcatchment" |
| Concern | The design leaves the inversion free to attribute sediment to any unit, which is a good test. In the Fig. 13 inset the dashed Gorner-Grenz catchment encloses Stockhorn-Tuftgrat-Gornergrat, Furgg series, Monte Rosa granite and a strip of serpentinite colour; no metabasite colour and only the tip of the MR gneiss unit lie inside. Yet MR gneiss has the highest and most peaked distribution (about 0.4 to 0.9 mm/y) and ZSF metabasites a broad one up to about 1.5 mm/y. The test counts only ZSF sediments, a small unit for which p. 10, l. 299 to 300 reports low resolution, so near-zero rates there may reflect the prior and low data sensitivity; the prior for natural data is not stated (GB-30). Number of samples, dates and share of sediment attributed to units outside are not given. Does "outcrops" refer to the outcrop layer rather than to the inferred units used to build A? |
| Suggestion | Report for every unit its area inside and outside the subcatchment in the map used for A, the attributed share of sediment, the prior value and the resolution, and repeat the test with samples from a second subcatchment. |
| Status | inferred |
| Severity | major |
| Source | SD |

**GB-29 The zircon method is documented only in an unpublished thesis**

| Field | Content |
|---|---|
| Check | P8 |
| Location | p. 14, l. 423 to 425; p. 17, l. 522 to 523; Fig. 14 |
| Quotation | "following the methodology described in (Belotti, 2021)" |
| Concern | Dating method, standards, number of grains per sample and the edges of the 13 age bins in Fig. 14 are not given; the cited source is an unpublished master's thesis. |
| Suggestion | Summarise the U-Pb method, grain counts and bin edges in Sect. 4.2.2 or an appendix, and cite as "described in Belotti (2021)". |
| Status | verified |
| Severity | moderate |
| Source | SD |

**GB-30 Natural runs use a prior "equal to the average true erosion rate"**

| Field | Content |
|---|---|
| Check | P25 |
| Location | p. 14, l. 428; p. 15, l. 444 to 445 |
| Quotation | "a prior equal to the average true erosion rate" |
| Concern | For natural data there is no true erosion rate, yet the zircon run (and by "the same inversion parameters" the XRD and combined runs) uses this prior. Which value was used, and was it derived from the export estimate? |
| Suggestion | State the prior value and its derivation for Sect. 4.2. |
| Status | verified |
| Severity | moderate |
| Source | SD |

**GB-31 Several figures lack units, scales or legends**

| Field | Content |
|---|---|
| Check | P29 |
| Location | Fig. 5a to 5c; Fig. 5e; Fig. 5j; Fig. 5k; Fig. 6a to 6c; Fig. 11; Fig. 13; Fig. 14 |
| Quotation | "(k) synthetic source tracer concentrations" |
| Concern | Colour bars of Fig. 5 and 6 a to c and e have no unit; Fig. 5j, 15 and 16 use "S.,T.,G.", "MR" and "ZSF" without expansion in the caption; the tracers in Fig. 5k are letters A to U without key; Fig. 11 has no value axis and identifies its seven columns only by caption order; the upper panel of Fig. 13 has no density scale; the geology panel of Fig. 14 has no legend although its fingerprint bars are coloured by unit. |
| Suggestion | Add units, value axes, density scale and legend, and expand the abbreviations in each caption. |
| Status | verified |
| Severity | minor |
| Source | AB |

**GB-32 "Low-confidence areas" are drawn but not defined**

| Field | Content |
|---|---|
| Check | P29 |
| Location | Fig. 5b; Fig. 6b; Fig. 14; Fig. 15; Fig. 16 |
| Quotation | "Low-confidence areas" |
| Concern | Hatched cells are labelled in the legend; neither captions nor text give the criterion (the word "confidence" does not occur in the text). In Fig. 15 the hatching covers the main erosion peak named at p. 14, l. 440 to p. 15, l. 441. In Fig. 14 to 16 the legend reads "Low-con dence area" (missing ligature, page images p. 35 to 37). |
| Suggestion | Define the criterion (metric and threshold) in Sect. 3.3 and in the captions, and correct the legend to "Low-confidence area". |
| Status | verified |
| Severity | moderate |
| Source | AB |

**GB-33 Labels in Fig. 10 and Fig. 14 to 16 are below 6 pt**

| Field | Content |
|---|---|
| Check | P29 |
| Location | Fig. 10; Fig. 14; Fig. 15; Fig. 16 |
| Quotation | "Results of parameter sweeps" |
| Concern | Digit height measured at 300 dpi: Fig. 10 tick labels 11 px (3.7 pt), axis labels about 14 px (4.7 pt); Fig. 14 to 16 colour-bar ticks 16 px (5.3 pt). For comparison Fig. 8 and 9 ticks 18 px (6.0 pt), Fig. 5 and 6 18 to 19 px (6.0 to 6.3 pt). |
| Suggestion | Enlarge the labels of Fig. 10 and Fig. 14 to 16 to at least 6 pt at print size, for Fig. 10 by splitting it into two figures. |
| Status | verified |
| Severity | minor |
| Source | AB |

#### Minor corrections

| ID | Location | Quotation | Replacement | Source |
|---|---|---|---|---|
| KK-12 | p. 11, l. 319 | "(Figure 6D, 6E and 6F )" | "(Figure 6D, 6E and 6F)" | S4 |
| KK-13 | Fig. 7 | "Originial geology (same as forward)" | "Original geology (same as forward)" | AB |
| KK-14 | Fig. 10 | "Smooting distance (m)" | "Smoothing distance (m)" | AB |
| KK-15 | Fig. 15 legend; Fig. 16 legend | "ZSF serpentinite" | "ZSF serpentinites", with the legend columns spaced so the next patch does not cover the text and the clipped top row of Fig. 16 restored | AB |

#### Verification log

| ID | Check | Checked | Values | Result |
|---|---|---|---|---|
| PP-13 | P1 | Arithmetic in Sect. 4 | L = 4 x 300 = 1200 m; 10 x 300 = 3000 m; 0.87 to 0.86 "decreases slightly" (0.01); 0.48 to 0.57 "increases" (0.09); 21 minerals listed (counted) | no finding |
| PP-14 | P2 | Parameters across sections | 25 iterations, L = 1200 m, sigma_m = 3, sigma_d = 0.01 mm/y, mu = 0.1 identical at p. 11, l. 324 to 326 and p. 14, l. 426 to 428; QN test 100 iterations (p. 10, l. 293) | consistent in the text; figure annotations in GB-17 |
| PP-15 | P3 | Fig. 9 marker count | 21 markers for 1 to 21 tracers (19 counted automatically from x 980 px, two at the axis counted at the enlarged crop); one-tracer error 347.1 ± 0.3 (y ticks 340 at 948.5 px, 200 at 1399.5 px) | no finding on the count |
| PP-16 | P3 | Fig. 7 values | identical map about 197.5, minimal changes 193.4 ± 0.2, Steck et al. map 274.8 ± 0.2 (y ticks 270 at 1070.5 px, 190 at 1550.5 px); data misfit 3.27e6 to 3.69e6 and model misfit 1.57 to 2.46 increase with mismatch | consistent with p. 12, l. 341 to 342; generalisation in GB-21 |
| PP-17 | P24 | Time axes and dated events | no figure has a date axis; the dated detrital sample (p. 14, l. 423 to 424) is not shown in a figure | not applicable |
| PP-18 | P3 | Oscillations of Fig. 6h after 125 iterations (p. 11, l. 316) | marker band after about iteration 135 doubles in thickness at the enlarged crop, consistent with small alternation | no finding |

### Segment 4: Discussion, conclusions, statements, references (p. 15 to 21)

#### Substantive findings

**GB-34 Two discussion statements have no support in the results**

| Field | Content |
|---|---|
| Check | P15 |
| Location | p. 15, l. 457 to 461; p. 12, l. 360 to 365 |
| Quotation | "Including a broad set of tracer minerals further improves model stability and resolution." |
| Concern | The results say that 7 tracers give "approximately the same posterior solution as with the full tracer set" and that tracer reduction "has a comparatively limited effect" (p. 12, l. 360, l. 364 to 365). "A higher number of distinct source areas leads to higher posterior resolution and lower uncertainty" (p. 15, l. 460 to 461) has no test; no experiment varies the number of source areas. |
| Suggestion | Reword p. 15, l. 457 to 458 to the tested statement (at least 7 informative tracers) and remove or test the statement on the number of source areas. |
| Status | verified |
| Severity | moderate |
| Source | S4 |

**GB-35 Depth-integrated sampling is recommended; the study shows a pump sampler**

| Field | Content |
|---|---|
| Check | P18 |
| Location | p. 15, l. 469 to 473; Fig. 1c; Fig. 3a |
| Quotation | "using depth-integrated suspended sediment samples to average out sorting effects during transport" |
| Concern | Fig. 1 and 3 show a pump sampler; whether its samples were depth-integrated is not stated. Source rocks are powdered whole, while suspended sediment is a transported fine fraction; whether sorting shifts mineral proportions between the two is not tested, and the limit appears only in the discussion. Were the detrital samples depth-integrated, and was a size fraction matched between source and detrital material? |
| Suggestion | State sampling depth and size fraction in Sect. 3.4 and discuss the grain-size effect there. |
| Status | assumption |
| Severity | moderate |
| Source | SD |

**GB-36 The data statement covers "inversion tests" and does not name the measured data**

| Field | Content |
|---|---|
| Check | P12 |
| Location | p. 16, l. 490 |
| Quotation | "The data and codes used for the inversion tests in the study are available at https://doi.org/10.5281/zenodo.17120374" |
| Concern | The methods and study area name seven data sources (PP-23); the statement names one, the synthetic tests. Not named: raw and processed diffractograms, sample locations and numbers, detrital sample metadata, U-Pb ages, the inferred geological map, and the export estimate. Whether the Zenodo record contains them was not checked (WebFetch refused with HTTP 429; reachability not checked). |
| Suggestion | List each data set with its location in the statement, or state why one is withheld. |
| Status | inferred |
| Severity | moderate |
| Source | S2 |

#### Minor corrections

| ID | Location | Quotation | Replacement | Source |
|---|---|---|---|---|
| KK-16 | p. 16, l. 491 | "All authors (FDD, FH, BB, TA)" | "All authors (F.D.D., F.H., B.B., T.A.)" | S4 |
| KK-17 | p. 19, l. 578 | "[No title found]" | "Landscape indicators of human impacts to riverine systems" | S4 |

#### Verification log

| ID | Check | Checked | Values | Result |
|---|---|---|---|---|
| PP-19 | P4 | Citations against the reference list in both directions (arbeit_S4/refs2.py) | 64 entries, 64 cited, 0 citations without entry; "et al." for three or more authors in the checked cases (Steck, Lafuente, Fox, Walling 1979) | no finding beyond KK-02 and KK-06 |
| PP-20 | P4 | Section, figure and cross references | Figures 1 to 16 consecutive; Section 2 duplicates Section 1 (GB-03); "Figure 6G versus Figure 6G" (GB-20) | no further finding |
| PP-21 | P15 | Outlook proposals held against results | (a) well constrained source map: Fig. 7; (b) strong mineralogical contrast: Fig. 8; (c) multiple XRD tracers: 7 suffice (p. 12, l. 360); land-use maps "can also be incorporated" (p. 15, l. 466): untested, stated as possibility; caution on storage (p. 15, l. 466 to 468): stated assumption; other tracers (p. 16, l. 488 to 489): shown for zircon | finding GB-34; others no finding |
| PP-22 | P16 | Uniformity of the reference list | Gjems 1967, Bearth 1953 and Lafuente et al. 2015 without publisher; Belotti 2021 with "Master's thesis" and "unpublished master's thesis" in one entry | style check is an optional area; no finding |
| PP-23 | P12 | Data sources from methods and study area against the statement | synthetic data and code (named); diffractograms; source sample locations and numbers; detrital samples and dates; U-Pb ages; inferred map, outcrops, land cover; export estimate: 1 of 7 named | finding GB-36 |

## Optional checks

| Area | What it needs | Responsible | Run |
|---|---|---|---|
| DOI resolution | one fetch per reference entry with DOI | `science-quellenapparat-pruefung` | no |
| Citation style | the name of the style | `science-zitierstil-harvard-ctr` or the journal's style rules | no |
| AI statement against publisher policy | the target publisher's policy | this review, on request | no |
| Relation to own prior work | the authors' prior work | this review, on request | no |
| Journal requirements | the author guidelines of the target journal | this review, on request | no |
| Subject-matter accuracy | access to the sources of the checked statements and a selection of sections | `science-faktenbeleg-pruefung`, `geo-frage-belegbasiert-klaeren` | no |

## Limits of this review

- Checked version: egusphere-2025-4695.pdf, 37 pages, SHA-256 9c80676054f96ecd6f00f4d2a8b5ba568e03c6949e3856d363ac1c4abb42e7bd
- Sources not readable: Das et al. (2023), https://doi.org/10.1029/2023WR034500 (fetch error); Zenodo record https://doi.org/10.5281/zenodo.17120374 (HTTP 429); UNESCO 2009 report behind "E., 2009" (rate limit, author Walling inferred); Belotti (2021), unpublished
- Findings with status assumption: 1 of 36
- Optional checks run: 0 of 6
- Omitted instances: none; all six instances ran sequentially in one context
- Discarded findings: 0
