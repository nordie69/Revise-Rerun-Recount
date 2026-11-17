# Review report: From XRD signal to erosion rate maps

| Field | Value |
|---|---|
| Manuscript | De Doncker, F., Herman, F., Belotti, B. and Adatte, T. (2025) From XRD signal to erosion rate maps. EGUsphere preprint egusphere-2025-4695, https://doi.org/10.5194/egusphere-2025-4695 |
| Checked version | egusphere-2025-4695.pdf, 37 pages, SHA-256 9c80676054f96ecd6f00f4d2a8b5ba568e03c6949e3856d363ac1c4abb42e7bd |
| Date | 2026-10-18 |
| Language | English |
| Review instances | Segments 1 to 4 (S1 to S4), figures (AB), study design (SD); the six review instances ran as separate agents without shared context; no instance omitted; merging, overall assessment and format check by a further separate agent (ZF) |

## Summary

The manuscript is a method-development and validation study. It builds a spatially explicit Bayesian (maximum a posteriori) inversion that converts tracer abundances in suspended sediment into erosion rate maps, using binned XRD peak areas in mineral-specific 2θ windows as source fingerprints and a geological map as the spatial distribution of sources; erosion rates are parametrised in log-space, and a steepest-descent and a quasi-Newton update are compared. Posterior covariance, a resolution diagonal and a normalised posterior uncertainty serve as reliability metrics. Synthetic forward-inverse tests on a seven-unit map with one erosion hotspot compare the two schemes (100 and up to 200 iterations), test three degradation scenarios (three geological maps, 20 levels of fingerprint blending, 1 to 21 tracers) and sweep five hyperparameters (adopted values L = 1200 m, σm = 3, σd = 0.01 mm/y, step size 0.1, 25 iterations). Natural-data tests in the glacierized Gornergletscher catchment (Pennine Alps) use 21 tracer minerals for seven lithological units, a subcatchment test with one absent unit at the Gorner-Grenz confluence, and a comparison of zircon U-Pb ages (13 age bins), XRD and their combination for one detrital sample of 28 June 2019, with total normalised posterior uncertainties of 0.87, 0.82 and 0.86 and an average Jensen-Shannon distance rising from 0.48 (zircon) to 0.57 (combined).

## Strengths

1. The log-space parametrisation of the erosion rates enters every forward and update equation (eqs. 3, 17, 18 and 19), so no inversion scheme can return a negative erosion rate (PP-15); this is the property that the novelty statement should name (GB-11).
2. The synthetic tests vary three degradation factors and five hyperparameters against a known map and report each case with summed error, normalised uncertainty and the data and model misfit trade-off (PP-31, PP-36); this exposes operating limits that the figures confirm, such as the steep rise of error below 7 tracers and the optimum step size of 0.1 (PP-35, PP-37).
3. Numbers agree between text and figures: the natural-data uncertainties 0.87, 0.82 and 0.86, the 21 tracer minerals, the 13 zircon age bins and the baseline error of Figures 7 to 10 match within measurement uncertainty (PP-32, PP-39, PP-43, PP-44); this consistency is what makes the comparisons in GB-33 and GB-44 checkable at all.
4. Data gaps and limitations are disclosed where they arise: missing zircon ages and the copied Monte Rosa fingerprint (l. 430 to 434, confirmed in Figure 14, PP-42), the lithology inferred under ice and labelled "Inferred geology" in Figure 4 (PP-18), and storage, grain-size and orientation effects (l. 466 to 476); a reader can thereby trace the instability of the zircon-only run to missing source data (GB-41).

## Weaknesses

1. The uncertainty metrics that carry the natural-data comparison cannot be interpreted as reported: the resolution maps show values near 1 that diag(R) cannot reach (GB-17), the normalised uncertainty has two definitions and eight names (GB-16), the main XRD erosion peak is hatched as low confidence without a stated rule (GB-45), and the combined zircon and XRD run is less certain than XRD alone while the text reports an improvement (GB-44). Define R, the normalised uncertainty and the low-confidence rule in Section 3.3, recompute the maps, and report all three natural runs against both single-data baselines.
2. The natural-data tests do not yet validate the fingerprints: research question 1 is answered qualitatively while three mineral pairs have identical fingerprints (GB-39), research question 2 rests on one negative control whose criterion present units also meet (GB-40), and the zircon comparison mixes method and data availability (GB-41), so "validated" overstates the evidence (GB-55). Add laboratory known mixtures, a quantitative comparison with the expected mineralogy per unit, and a comparison restricted to units with both fingerprints.
3. The synthetic validation runs under the most favourable conditions (noise-free data from the same operator, one true map, a prior equal to the true mean; GB-25), and several statements in Section 4.1 are not supported by the manuscript's own figures: the accuracy argument for quasi-Newton (GB-27), the ranking of degradation factors (GB-33), and the smoothing-distance, data-uncertainty and iteration statements (GB-35, GB-36, GB-37), carried into the Abstract as "consistent convergence" (GB-03). Add noise, an independent grid, several true maps and a prior independent of the truth, compare the scenarios on a common scale, and rewrite the sweep statements to the measured behaviour.
4. Reproducibility and positioning have gaps of moderate weight: the export estimate and the prior of the natural runs are not reported (GB-13), several equations differ from what was computed or is defined (GB-12, GB-14, GB-15), sample metadata, XRD settings and data availability are incomplete (GB-19, GB-20), and the novelty claim and the cost argument are not delimited against the cited predecessor and earlier XRD unmixing (GB-01, GB-07, GB-09, GB-11). Add the missing inputs, settings and sample tables, correct the equations, itemise the data statement, and delimit the contribution against De Doncker et al. (2020), Eberl (2004) and Andrews and Eberl (2012).

## Findings by segment

### Segment 1: Abstract, Introduction, state of research (p. 1 to 5)

#### Substantive findings

**GB-01 The Abstract and Introduction present the time and cost efficiency of XRD fingerprinting as validated, but the study contains no measure of time or cost, and Discussion and Conclusions do not return to it.**

| Field | Content |
|---|---|
| Check | P33, P15 |
| Location | p. 1, l. 3 to 4; p. 2, l. 35 and l. 40 to 42; p. 3, l. 74 to 75 (repeated p. 4, l. 102 and l. 107 to 109; p. 5, l. 141 to 142); Sections 5 and 6 (p. 15, l. 450 to p. 16, l. 489) |
| Quotation | "In this study, we validate a time- and cost-effective fingerprinting approach based on X-ray diffraction (XRD) data." and "To conclude, we show and validate the potential of binned XRD peak-area data as a cost- and time-efficient approach for constructing erosion rate maps." |
| Concern | The motivation is stated clearly: other methods are "expensive and time-consuming (Das et al., 2023)" (l. 35). A text search finds "cost", "time-consuming" and "efficien" only in l. 3 to 4, l. 35, l. 40 to 42 and l. 74 to 75 and their duplicates. None of the synthetic tests and none of the three natural-data questions (p. 10, l. 282 to 285) addresses time or cost; no sample mass, preparation or measurement time, or cost per sample is reported for XRD or for the zircon U-Pb benchmark, and Sections 5 and 6 do not mention efficiency. The efficiency therefore rests on the citation of Das et al. (2023) alone, which could not be read for this review (PP-07), while l. 3 to 4 presents it as validated by this study. The inversion results are unaffected, hence moderate. |
| Suggestion | Either report in Section 4.2.2 the per-sample effort of XRD and of zircon U-Pb dating (sample mass, preparation and measurement time, approximate cost) and take it up in Sections 5 and 6, or rephrase l. 3 to 4 and l. 74 to 75 (and l. 141 to 142) so that the efficiency is attributed to Das et al. (2023), e.g. "a potentially time- and cost-effective approach". |
| Status | verified (absence of any time or cost measure; wording) |
| Severity | moderate |
| Source | S4, SD |

**GB-02 Posterior uncertainty and "error propagation" rest on a single data standard deviation that is swept as a hyperparameter, not estimated from measurements, and the variability of the source fingerprints enters no covariance.**

| Field | Content |
|---|---|
| Check | P31 |
| Location | p. 1, l. 6 to 7; p. 6, l. 185 to 186 (eq. 8); p. 10, l. 295; p. 13, l. 380 to 384; p. 14, l. 427 to 428; p. 15, l. 444 to 445 |
| Quotation | "in order to invert detrital mineralogical data into erosion rate maps while quantifying posterior uncertainty and error propagation" |
| Concern | The data covariance is Cd = σd² I with one σd (eq. 8); σd is swept in Figure 10 (third row) and fixed at 0.01 mm/y. No replicate XRD measurements are reported from which σd could be estimated, and the tracer matrix A is treated as exact, so the within-unit spread of the source fingerprints is not propagated. The same σd is used for XRD peak-area fractions and for zircon age-bin fractions ("with the same inversion parameters", l. 444 to 445), two data types with different error structures. The values 0.87, 0.82 and 0.86 that carry the zircon, XRD and combined comparison therefore depend on a chosen σd. What the manuscript measures is the sensitivity of the posterior to an assumed σd, not the propagation of measured error; GB-36 shows that, within the tested range, this sensitivity is negligible on the reported synthetic metrics. |
| Suggestion | In Section 3.4 report replicate XRD measurements (repeated preparation of the same powder) and the spread of source samples within each unit, derive σd and an uncertainty on A from them, and use data-type specific σd in Section 4.2.2; otherwise replace "error propagation" in l. 7 by "sensitivity to the assumed data uncertainty". |
| Status | verified (σd swept and fixed; no replicates reported; A without uncertainty); inferred (dependence of 0.82, 0.86 and 0.87 on the chosen σd) |
| Severity | moderate |
| Source | SD |

**GB-03 The Abstract and Conclusions state consistent convergence and robustness without the non-converging settings that the Results report.**

| Field | Content |
|---|---|
| Check | P2, P6 |
| Location | p. 1, l. 7; p. 16, l. 482 to 483; p. 11, l. 312; p. 12, l. 353; p. 13, l. 387 to 388; Figure 8 caption (p. 29) |
| Quotation | "Forward-inverse tests with synthetic data demonstrate consistent convergence of the posterior solution." and "we show that the true erosion pattern can be reliably recovered, and that the method is robust across a range of parameters" |
| Concern | The Results disclose the limits: the steepest-descent scheme "proved unstable, requiring the normalization of the gradient" (l. 312); for blended fingerprints "In many of these cases, the inversion fails to converge to a stable posterior solution." (l. 353); the most blended case "did not have a stable solution" (Figure 8 caption); below 25 iterations the posterior is said to "fail to converge" (l. 387 to 388; see GB-37). Figure 8 plots 14 of 20 blending runs (GB-31), so at least one and possibly six blending runs did not converge. The Abstract and Conclusions carry none of these conditions. Instance S4 mapped l. 482 to 483 to the sweeps, where the limits are reported, without a finding; the finding here concerns only that the limits are not carried into l. 7 and l. 482 to 483. The results themselves stand, hence moderate. |
| Suggestion | Qualify l. 7 and l. 482 to 483 with the conditions under which convergence was obtained (quasi-Newton scheme, average JS distance above about 0.55, noise-free synthetic data) and state the number of non-converging runs. |
| Status | verified |
| Severity | moderate |
| Source | S3, SD |

**GB-04 The Introduction is printed twice, as Section 1 and again as Section 2, with identical wording.**

| Field | Content |
|---|---|
| Check | P4 |
| Location | p. 1, l. 9 to p. 3, l. 75; p. 3, l. 76 to p. 5, l. 142 |
| Quotation | "1 Introduction" and "2 Introduction" |
| Concern | The section numbering gives two numbers to the same section. A word-by-word comparison (Python, difflib, page headers excluded) of l. 10 to 75 against l. 77 to 142 gives 1153 words in each block and a similarity ratio of 1.0; both headings were confirmed on page images 1 and 3. Methods therefore start as Section 3, all later section numbers are shifted by one, and every citation of the Introduction is counted twice. |
| Suggestion | Delete p. 3, l. 76 to p. 5, l. 142 and renumber Sections 3 to 6 as 2 to 5; where this review cites both copies, the first copy is meant. |
| Status | verified |
| Severity | minor |
| Source | S4 |

**GB-05 A single instantaneous detrital sample is converted into an erosion rate map in mm/y scaled by an annual export, while the temporal question named in the Introduction is not addressed.**

| Field | Content |
|---|---|
| Check | P9, P10 |
| Location | p. 1, l. 10 to 14; p. 14, l. 423 to 424 and l. 437 to 438; p. 16, l. 479 to 480; p. 5, l. 160 (eq. 2) |
| Quotation | "the detrital sample collected on June 28, 2019, at 13:30" and "The approach integrates prior erosion estimates, a yearly sediment export estimate, and spatial information on source areas." |
| Concern | The Introduction frames the problem as "spatio-temporal dynamics of suspended sediment" and "the timing of their activation" (l. 10 to 13), but no research question addresses time. The natural tests use one sample at one moment (Section 4.2.2) or an unstated number of samples at unstated dates (Section 4.2.1). The composition of a single sample taken at 13:30 on one summer day reflects the sources active at that time, while eq. 2 scales the data by a total erosion rate and the maps are given in mm/y; within-day and seasonal changes of source activation, named as the motivation, are thus confounded with the spatial pattern. The manuscript does not discuss this. |
| Suggestion | In Section 4.2 state sampling dates and times of all detrital samples, invert them separately and report the spread; state in Section 3.1 or 4.2 whether a single sample is treated as representative of the annual export. A design that answers the temporal question would invert a time series of samples (diurnal and seasonal) with discharge-weighted aggregation. |
| Status | verified (single sample; scaling by the total erosion rate); inferred (confounding of temporal and spatial variation) |
| Severity | moderate |
| Source | SD |

**GB-06 The in-text citation "E., 2009" and its reference entry use initials instead of the author's surname.**

| Field | Content |
|---|---|
| Check | P4 |
| Location | p. 1, l. 11 to 12; p. 3, l. 78 to 79; p. 18, l. 567 to 568 |
| Quotation | "(Gergel et al., 2002; Allan, 2004; E., 2009; Hamel et al., 2015)" and "E., W. D.: The Impact of global change on erosion and sediment transport by rivers" |
| Concern | Short citation and entry agree with each other, but the name field consists of initials only, so the entry is sorted under "E" and the citation cannot be resolved to an author. The pattern matches an inverted parse of "Walling, D. E."; the UNESCO report of 2009 with this title and ISBN is attributed to D. E. Walling (the UNESDOC copy could not be opened by instance S4). The entry also contains the residue "oCLC: 1402659188" and the year twice. |
| Suggestion | Replace "E., 2009" by "Walling, 2009" in l. 11 to 12 (and l. 78 to 79 if the duplicate remains) and the entry by "Walling, D. E.: The impact of global change on erosion and sediment transport by rivers, UNESCO, Paris, ISBN 9789231041358, 2009.", sorted before the Walling et al. (1979) entry, after confirming the author on the title page. |
| Status | verified (malformed name field, page images 1 and 18); inferred (author D. E. Walling) |
| Severity | minor |
| Source | S4, S1 |

**GB-07 The argument that the spatially informed approach is particularly valuable in glacierized catchments omits an earlier detrital study of spatial erosion variation in a glacial catchment.**

| Field | Content |
|---|---|
| Check | P14 |
| Location | p. 1, l. 16 to 17; p. 2, l. 61 to p. 3, l. 63; p. 3, l. 83 to 84; p. 4, l. 128 to p. 5, l. 130 |
| Quotation | "This spatially informed approach to sediment provenance is particularly valuable in glacierized catchments, where ice cover limits direct observations" |
| Concern | The glacier setting motivates the study clearly. The same motivation, the inaccessibility of the glacier bed, has already been addressed with detrital provenance data by Ehlers, T. A., Szameitat, A., Enkelmann, E., Yanites, B. J. and Woodsworth, G. J. (2015) Identifying spatial variations in glacial catchment erosion with detrital thermochronology, Journal of Geophysical Research: Earth Surface, 120(6), 1023 to 1039, https://doi.org/10.1002/2014JF003432. According to its abstract (read by instance S1), 106 apatite (U-Th)/He and 100 apatite fission-track ages from glacial outwash were treated as a mixture of source signals and compared with a bedrock age-elevation transect to locate the sediment-supplying elevations. The work is not in the reference list (search for "Ehlers": 0 hits). It does not produce pixel-wise erosion rate maps; the manuscript, however, does not say what it adds over such elevation-based approaches. |
| Suggestion | Cite Ehlers et al. (2015) in l. 61 to 63 (and l. 128 to 130) and state what the pixel-wise inversion with posterior covariance and resolution adds over the elevation-band approach. |
| Status | verified (abstract read by instance S1; reference list checked); the landing page could not be re-read during merging |
| Severity | moderate |
| Source | S1 |

**GB-08 The citation "Kobe, 2021" for plant pollen as a fingerprint points to an article on black theology of liberation.**

| Field | Content |
|---|---|
| Check | P13, P4 |
| Location | p. 2, l. 31; p. 4, l. 98; p. 19, l. 597 to 598 |
| Quotation | "plant pollen content (Brown, 1985; Kobe, 2021)" and "Kobe, S. L.: Ubuntu as a spirituality of liberation for black theology of liberation" |
| Concern | The list of fingerprinting tools in l. 26 to 33 gives one or more examples per tracer type. For pollen, the second example does not fit: the entry is Kobe, S. L. (2021) Ubuntu as a spirituality of liberation for black theology of liberation, HTS Teologiese Studies / Theological Studies, 77(3), https://doi.org/10.4102/hts.v77i3.6176. Its abstract (journal page hts.org.za, article 6176, read by instances S1 and S4 and again during merging) argues for Ubuntu as a liberative partner of black theology of liberation and contains no reference to pollen, sediment or fingerprinting. The statement on pollen remains supported by Brown (1985) alone, so the content of l. 31 stands; the citation points to a wrong work. Is a reference-manager mismatch the cause? The entry also lacks the article number. |
| Suggestion | Replace "Kobe, 2021" in l. 31 (and l. 98) by a study that uses pollen as a sediment source fingerprint, or delete it, and correct or remove the entry in l. 597 to 598. |
| Status | verified (source read) |
| Severity | minor |
| Source | S1, S4 |

**GB-09 Earlier quantitative XRD unmixing for sediment provenance is not cited, so the positioning of XRD and the known-mixture design lack their direct precedents.**

| Field | Content |
|---|---|
| Check | P14 |
| Location | p. 2, l. 36 to 42; p. 4, l. 103 to 109; p. 13, l. 404 to 406 |
| Quotation | "X-ray diffraction (XRD) has recently gained attention as a proxy for mineral abundance in provenance analysis but remains underutilized (Das et al., 2023)." and "Typically, the reliability of a given fingerprinting method is tested using known mixture experiments" |
| Concern | The manuscript builds explicitly on Das et al. (2023, 2024). Quantitative XRD mineralogy has, however, been unmixed for sediment source apportionment before. (1) Eberl, D. D. (2004) Quantitative mineralogy of the Yukon River system: changes with reach and season, and determining sediment provenance, American Mineralogist, 89(11 to 12), 1784 to 1794, develops a calculation of source proportions in mixed sediment from quantitative XRD and reports that "at least three sediment sources can be identified quantitatively with good accuracy" (abstract on the USGS publication page https://pubs.usgs.gov/publication/70026557, read during merging). (2) Andrews, J. T. and Eberl, D. D. (2012) Determination of sediment provenance by unmixing the mineralogy of source-area sediments: the 'SedUnMix' program, Marine Geology, 291 to 294, 24 to 33, https://doi.org/10.1016/j.margeo.2011.10.007, tested XRD-based unmixing on eleven artificial mixtures of four end-member sediments according to its abstract (read by instance S1), which is the known-mixture test that l. 404 to 406 describes without a citation. Neither work is in the reference list (search for "Eberl" and "Andrews": 0 hits). The wording "recently gained attention" may still describe the recent literature, but what binned peak-area fingerprints and the spatial inversion add over quantitative XRD unmixing is not delimited. |
| Suggestion | Cite both works in l. 36 to 42 (and l. 103 to 109) and in l. 404 to 405, and state in one or two sentences what binned peak-area fingerprints add over quantitative XRD unmixing (no full phase quantification, cost, spatial inversion). |
| Status | verified (Eberl, 2004, abstract read; Andrews and Eberl, 2012, abstract read by instance S1; reference list checked) |
| Severity | moderate |
| Source | S1 |

**GB-10 The method overview uses two abbreviations for the frequentist least-squares method, two names for the Bayesian mixing-model class and non-standard names for GLUE and MLE.**

| Field | Content |
|---|---|
| Check | P38 |
| Location | p. 2, l. 48 to 56; p. 4, l. 115 to 123 |
| Quotation | "the Non-Linear Least Squares (NLLS) (a constrained linear regression)" and "similar to the NNLS approach" and "Our approach can be seen as a hybrid between Bayesian linear mixed models and hierarchical Bayesian models" |
| Concern | The overview of unmixing techniques helps to place the method. Within it, the least-squares method is introduced as "NLLS" (l. 48 to 49) and referred back to as "NNLS" (l. 51 to 52); the expansion "Non-Linear Least Squares" does not match the gloss "a constrained linear regression", so the reader cannot tell whether a non-linear or a non-negative least-squares scheme is meant. The class introduced as "Bayesian Linear Mixing Models (BLMM)" (l. 53) is later called "Bayesian linear mixed models" (l. 55 to 56), the usual name of a different model family. The method names "Generalist Likelihood Uncertainty Estimation (GLUE)" (l. 50) and "Maximal Likelihood Estimation (MLE)" (l. 51) differ from the usual generalised likelihood uncertainty estimation and maximum likelihood estimation. Is the hybrid statement in l. 55 meant to refer to BLMM? |
| Suggestion | In l. 48 to 52 (and l. 115 to 119) use "Non-Negative Least Squares (NNLS)" in both places if a constrained linear regression is meant, otherwise "NLLS" in both and drop "linear regression"; write "Generalised Likelihood Uncertainty Estimation (GLUE)" and "Maximum Likelihood Estimation (MLE)"; in l. 55 to 56 (and l. 122 to 123) write "Bayesian linear mixing models (BLMM)". |
| Status | verified (all variants on page images 2 and 4); assumption (which least-squares method is intended) |
| Severity | minor |
| Source | S2, S1 |

**GB-11 The novelty claim of a "spatially informed approach" and a "non-linear mixing model" is not delimited against the cited spatial inversion of De Doncker et al. (2020), the mixing in the forward model is linear, and no comparison with a linear scheme is made.**

| Field | Content |
|---|---|
| Check | P28, P15, P10 |
| Location | p. 2, l. 58 to 61; p. 4, l. 125 to 128; p. 15, l. 454 to 455; p. 5, l. 151 to 152 and l. 157 to 158 |
| Quotation | "The novelty of our method lies in the spatially informed approach of this underdetermined inversion problem, and in the incorporation of non-linear mixing model." and "implicitly rely on a linear mixing scheme (Niu et al., 2020)" |
| Concern | The Introduction openly names De Doncker et al. (2020) as the framework that is adapted (l. 60 to 61). According to its abstracts (Serval, University of Lausanne, and EGU2020-2176, read by instance S1), that work already inverts provenance data into an erosion rate map by least squares with a priori information and a model covariance to handle non-uniqueness, and it notes that other tracers such as mineral content can be used. The first part of the claim in l. 454 is therefore not new relative to the cited predecessor. For the second part, the forward model states that "the detrital data are a weighted average of the tracer mineral concentrations, with the weights being the erosion rates" (l. 151 to 152), and after rescaling eq. 3 (d = A · exp(ε)) is linear in the erosion rates; the non-linearity comes from the parametrisation: "We cast the erosion rates in log-space to impose a positivity constraint, hence making this non-linear." (l. 157 to 158). The contrast with approaches that rely on a linear mixing scheme (l. 59) thus describes a reparametrisation, not a different mixing model, and no test compares the log-space scheme with the linear framework of De Doncker et al. (2020) on the same data. The general gap statement in l. 58 to 59 rests on Niu et al. (2020) alone, whose abstract reports one case study with a linear mixing model (full text not read); no literature search behind either statement is described. |
| Suggestion | Rephrase l. 454 to 455, e.g. "Building on the spatial inversion of De Doncker et al. (2020), the novelty lies in the log-space (positivity-preserving) non-linear parametrisation and in the use of binned XRD peak areas as fingerprints", correcting the grammar of the sentence ("approach to this", "a non-linear"); add in Section 4.1 a run of the linear framework of De Doncker et al. (2020) on the same synthetic data; in l. 58 to 59 cite a review for the general statement or limit it to the cited case. |
| Status | verified (l. 151 to 152, l. 157 to 158, eq. 3 on page images 5 and 6; absence of a comparison and of a search description; content of De Doncker et al., 2020, from abstracts read by instance S1); inferred (Niu et al., 2020, full text not read) |
| Severity | moderate |
| Source | S1, S4, SD |

#### Minor corrections

| ID | Location | Quotation | Replacement | Source |
|---|---|---|---|---|
| KK-01 | p. 1, l. 5 | "(steepest descent and Quasi-Newtonian)" | "(steepest descent and quasi-Newton)", as in l. 211 and l. 296 | S1, S2 |
| KK-02 | p. 2, l. 61; p. 4, l. 128; p. 6, l. 180; p. 11, l. 333 to 334; p. 14, l. 424 to 425 | "validated in (De Doncker et al., 2020)", "becomes Tarantola (2005):", "proposed by (Steck et al., 2015)", "described in (Belotti, 2021)" and "outlined in (De Doncker et al., 2020)" | "validated by De Doncker et al. (2020)", "becomes (Tarantola, 2005):", "proposed by Steck et al. (2015)", "described by Belotti (2021)" and "outlined by De Doncker et al. (2020)" | ZF |

#### Verification log

| ID | Check | Checked | Values | Result |
|---|---|---|---|---|
| PP-01 | P1, P2 | Wording of every quotation and embedded quotation in the Quotation and Concern fields, the minor corrections and the verification log against `text.json` | Script `zf/zitate2.py` (whitespace and hyphenation normalised): 286 quotations of at least 12 characters checked, 262 found in `text.json`; of the 24 others, 19 are figure labels in raster graphics, confirmed on page images 24, 25, 26 and 28; 3 are from external sources (Eberl, 2004, and Wirgin, 2004, read during merging; Collins et al., 2020, read by instance S1); 2 are descriptive terms, not quotations | no finding; line numbers confirmed at the printed margin numbers on page images 1, 3, 5 to 8, 11, 24 to 26, 28, 31, 32, 34 and 36 |
| PP-02 | P13 | Numbers taken from cited works in the Introduction | Numbers in l. 1 to 75 other than years: only the enumerations 1 to 4 (Python count). Klages and Hsieh (1975) for the two criteria of an ideal fingerprint (l. 24 to 25) not readable | no finding; Klages and Hsieh (1975) listed under Limits |
| PP-03 | P32 | Results described as "validated" or "confirmed" against independent checks | "validat" in l. 3, 8, 61, 69, 74, 266 to 267, 288, 451 (plus duplicates); "confirms" in l. 415; no independent erosion estimate, no laboratory known mixture, no independent mineral quantification | covered by GB-39, GB-40 and GB-55; no separate finding |
| PP-04 | P4 | Numbering of sections, equations, figures, tables, appendices | Sections 1, 2, 3, 3.1 to 3.4, 4, 4.1, 4.1.1 to 4.1.4, 4.2, 4.2.1, 4.2.2, 5, 6; equations (1) to (22) without gap or double number; equation references eq. 1 to 4 (l. 263), eq. 7 (l. 190, 240), eq. 10 to 16 (l. 200, 204, 213, 217) resolve; figure captions 1 to 16 each once; no tables, no appendices | double section "Introduction" (GB-04); otherwise no finding |
| PP-05 | P9, P10 | Design sketch from the whole manuscript (questions, cases, data sources, timeline, environment, components, disclosed limits, chain from aims to results) | Study type method development with synthetic tests and two natural-data tests in one catchment; 7 units, 21 tracer minerals, 13 zircon age bins; pixel size 300 m only implied; catchment area about 76.4 km² estimated from the Figure 4 scale bar (about 849 pixels); number of source samples not stated; one detrital sample for Section 4.2.2; data sources: synthetic, inferred geology, binned source and detrital XRD, zircon ages from Belotti (2021), export estimate without source; hyperparameter sweeps, fingerprint validity and source attribution not taken up in the Discussion | design sketch complete; gaps marked "not stated" and treated in GB-05, GB-13, GB-20, GB-22 |
| PP-06 | P13 | Collins et al. (2020) for multi-proxy combinations (l. 33 to 35), tracer patterns (l. 151) and storage caution (l. 467 to 468) | Read (100000 of 103352 characters): storage lasts "days or weeks to millennia", fingerprinting cannot determine residence time; colour, elemental geochemistry, radionuclides and mineral magnetics listed as tracers; the term "spectrocolourmetrics" not located in the part read | no finding |
| PP-07 | P13 | Statements attributed to Das et al. (2023) on cost and use of XRD | l. 35 "expensive and time-consuming"; l. 36 to 37 "remains underutilized". Source not readable (publisher page and DOI refused); Collins et al. (2020) call biomarker analyses expensive relative to conventional tracers | no finding; statements unverified, listed under Limits |
| PP-08 | P28 | Gap and novelty statements and the search behind them | l. 36 to 37 "remains underutilized"; l. 58 to 59 "typically yield relative source contributions without translating them into spatially explicit erosion rate maps"; l. 454 to 455 novelty; no other "first" or "not yet studied" statement; search description (databases, terms, period, date): none | GB-11, GB-09 |
| PP-09 | P14 | Contribution and missing preceding or contradicting work | Five queries on quantitative XRD unmixing, detrital thermochronology in glacial catchments, spatially explicit inversion of tracer data, zircon mixing and SedUnMix. Candidates against the reference list: Eberl (2004) absent, Andrews and Eberl (2012) absent, Ehlers et al. (2015) absent, Braun et al. (2018, Earth Surface Dynamics 6, 257 to 270) absent but not proposed; Lipp et al. (2021), Saylor et al. (2019), Das et al. (2024) already cited | GB-09, GB-07 |
| PP-10 | P13 | Niu et al. (2020) for the frequentist and Bayesian characterisation and composite fingerprints | Abstract: linear mixing model, multiple composite fingerprints, contributions 49.0 %, 26.5 %, 24.5 % from three source areas; no frequentist against Bayesian discussion in the abstract; l. 459 "optimising composite fingerprints" matches | no finding for l. 459; l. 45 to 48 not verifiable beyond the abstract (Limits); l. 58 to 59 in GB-11 |
| PP-11 | P13 | Ranking "most common methods" and Bayesian categories (l. 48 to 55) | Haddadchi et al. (2013), Yang et al. (2025), Fathabadi and Jansen (2022): publisher refused automated access, no open version found | no finding; listed under Limits |
| PP-12 | P13 | "the inversion framework validated in (De Doncker et al., 2020)" (l. 61) | Serval and EGU2020-2176 abstracts: least-squares inversion of detrital zircon ages with a priori information and model covariance, tested on synthetic and natural examples | no finding for P13; novelty aspect in GB-11 |

### Segment 2: Material, methods, data (p. 5 to 10)

#### Substantive findings

**GB-12 The same index letters denote different objects across the equations, and the iteration index has two names inside one update rule.**

| Field | Content |
|---|---|
| Check | P38 |
| Location | p. 5, l. 154 (eq. 1); p. 6, l. 164 (eq. 4); p. 7, l. 208 to 209 (eq. 17); p. 8, l. 215 to 216 (eq. 18); p. 8, l. 219 (eq. 19); p. 9, l. 262 to 263; Figure 3 (p. 24) panel (d) |
| Quotation | "We can thereby derive the abundance of a given tracer t at pixel xy in At,xy as well as in the detrital data dt (eq. 1-4)." |
| Concern | The derivation from forward model to update rules is complete and readable. The symbols, however, change meaning: (1) The iteration index is k in eq. 17 and l. 209 but n in eqs. 18 and 19 and in l. 216 (Gn as "the Jacobian at iteration n"); eqs. 18 and 19 contain both εn and εk in the same update, so the prior term can be read as using another iterate than the data term (confirmed on page image 8). (2) n is also the number of pixels (upper summation limit in eq. 1; A1,n and εn in eq. 4). (3) The tracer index is i in eq. 1, t in l. 262 to 263 and n in Figure 3d ("tracer mineral n"), where i denotes the detrital sample ("detrital sample i"). (4) m is the number of tracers (eq. 1, Am,n in eq. 4) and at the same time the subscript for "model" (εm, Cm, σm). Because eqs. 18 and 19 are the update rules that all tests rely on, the mixed indices affect whether a reader can re-implement them. |
| Suggestion | Use one iteration index (k) in eqs. 17 to 19 and l. 216, reserve n for the number of pixels and m for the number of tracers, use one tracer index (i) in eqs. 1 to 4, l. 262 to 263 and Figure 3d, give the detrital sample a separate index, and add a short notation table after eq. 4. |
| Status | verified (page images 5 to 9 and 24) |
| Severity | moderate |
| Source | S2 |

**GB-13 The inputs that set the absolute erosion rates of the natural-data inversions are not reported: the annual sediment export estimate has no value, source or availability, and the stated prior refers to a "true" erosion rate that does not exist for natural data.**

| Field | Content |
|---|---|
| Check | P12, P11, P15, P8 |
| Location | p. 5, l. 160 (eq. 2); p. 3, l. 65 to 66; p. 5, l. 132 to 133; p. 9, l. 267 to 268; p. 14, l. 426 to 428; p. 15, l. 452 to 454; p. 16, l. 479 to 480 and l. 490 |
| Quotation | "d) an estimate of the total annual suspended sediment export from the catchment" and "a prior equal to the average true erosion rate, and a step size µ of 0.1" |
| Concern | The export estimate is named as one of four required inputs three times (l. 65 to 66, l. 452 to 454, l. 479 to 480), and eq. 2 rescales the data vector by the total erosion rate, which sets the erosion rates in mm/y. The site is chosen for "the availability of multi-year suspended sediment datasets" (l. 267 to 268). A text search finds "export" only in l. 66, 133, 454, 468 and 479, and "multi-year" only in l. 268; none of these gives the origin of the datasets (station, operator, period), the export value used in Sections 4.2.1 and 4.2.2, or its conversion to the total erosion rate of eq. 2. The parameter list of the zircon inversion repeats the synthetic-test wording "a prior equal to the average true erosion rate" (l. 428; compare l. 295 and l. 325 to 326), but for natural data the true erosion rate is unknown; for the known-mixture inversions of Section 4.2.1 no parameters are stated at all. The reported magnitudes (above 8000 mm/y in l. 435; colour bars up to 8 and 12 mm/y in Figures 15 and 16; KDE axes 0 to 3 mm/y in Figure 13) therefore cannot be traced to their inputs, and the availability statement (l. 490) covers "data and codes used for the inversion tests" without these datasets. Is the total erosion rate of eq. 2 the export estimate, and which value was used as the prior? |
| Suggestion | In Section 3.1 at eq. 2 state that the total erosion rate is derived from the annual export estimate; in Section 4.2 give the export value with source and period, its conversion to an average erosion rate (catchment area, rock density), the prior used for each natural inversion, and the full parameter set of the Section 4.2.1 inversions; correct l. 428; list the suspended sediment datasets, or their owner and access conditions, in l. 490. |
| Status | verified (absence in Sections 3 and 4; wording of l. 428 on page image 14); inferred (role of the export estimate in eq. 2) |
| Severity | moderate |
| Source | S2, S3, S4, SD |

**GB-14 The update equations do not describe the computations that produced the results: the steepest-descent runs use a normalised gradient that eq. 18 does not contain, and eq. 19 inverts a matrix that is singular by the manuscript's own statement.**

| Field | Content |
|---|---|
| Check | P7, P25 |
| Location | p. 6, l. 170 to 172; p. 8, l. 213 to 219 (eqs. 18 and 19); p. 11, l. 312 to 314; Figure 6 caption (p. 27) |
| Quotation | "In initial experiments, the steepest descent approach proved unstable, requiring the normalization of the gradient." and "the number of tracers, representing the data we have, is smaller than the number of pixels for which we want to infer the erosion rates" |
| Concern | (1) Eq. 18 gives the steepest-descent update without normalisation; the results in Figure 6 come from the normalised version (l. 312 to 314), and neither eq. 18 nor the Figure 6 caption states the normalisation or the norm used. (2) Eq. 19 contains the inverse of Gnᵀ Cd⁻¹ Gn (confirmed on page image 8). G is m by n with m (21 tracers) smaller than n (pixels), as l. 170 to 172 state, so Gnᵀ Cd⁻¹ Gn is n by n with rank at most m and is not invertible; moreover every pixel of one unit has the same column pattern in A, so the rank is at most 7. As written, eq. 19 cannot be computed; the code must use another operator, for example one including Cm⁻¹ or a pseudo-inverse. Which matrix was inverted in the quasi-Newton step? |
| Suggestion | Rewrite eq. 18 with the normalisation actually used and state it in the Figure 6 caption; rewrite eq. 19 with the Hessian approximation actually computed (e.g. the inverse of Gnᵀ Cd⁻¹ Gn + Cm⁻¹) and confirm that the archived code implements it. |
| Status | verified (eq. 18 without normalisation and eq. 19 as printed, page image 8; m smaller than n stated in l. 170 to 172); inferred (singularity of the matrix in eq. 19) |
| Severity | moderate |
| Source | SD |

**GB-15 Four further equations as printed differ from the operators the method requires: eq. 5 lacks its relation sign, eq. 9 lacks the minus sign in the exponent, eq. 12 writes the Jacobian as a vector, and eq. 14 lacks the transpose that eq. 16 has.**

| Field | Content |
|---|---|
| Check | P8 |
| Location | p. 6, l. 175 (eq. 5); p. 7, l. 189 (eq. 9); p. 7, l. 197 (eq. 12); p. 7, l. 201 (eq. 14); p. 7, l. 205 (eq. 16) |
| Quotation | "with σm 2 the prior variance, si,j the Euclidean distance between point i and j, and L the smoothing distance" |
| Concern | The equations were checked on page images 6 and 7 during merging, following hints of instances S2 and SD that no instance had raised as a finding. (1) Eq. 5 prints p(εm given dobs) and p(dobs given εm) · p(εprior)/p(dobs) side by side, without an equality or proportionality sign. (2) Eq. 9 prints Cm(i, j) = σm² exp(si,j²/L²); without a minus sign in the exponent the prior covariance grows with distance and is not a valid squared-exponential covariance, which contradicts the role of L as "the smoothing distance" (l. 190). (3) Eq. 12 writes the Jacobian as G = A · exp(ε), the same expression as the modelled data in l. 195; the Jacobian of d = A · exp(ε) is A · diag(exp(ε)), a matrix of the size of A. (4) Eq. 14 writes the data-misfit gradient as G Cd⁻¹ (dε minus dobs), whereas eq. 16, which combines eqs. 14 and 15, has Gᵀ; with G of size m by n only the transposed form is defined. A reader re-implementing the inversion from Section 3.2 starts from these equations; whether the archived code (l. 490) uses the correct forms is not stated. |
| Suggestion | Insert the proportionality sign in eq. 5, write eq. 9 as Cm(i, j) = σm² exp(-si,j²/L²) (or the form actually implemented), write eq. 12 as G = A · diag(exp(ε)), and use Gᵀ in eq. 14. |
| Status | verified (page images 6 and 7) |
| Severity | moderate |
| Source | ZF |

**GB-16 The normalised posterior uncertainty is defined per pixel as a standard-deviation ratio in eq. 22 and as a ratio of traces of variances in the results, and it appears under eight names, with figure axes naming an unnormalised trace.**

| Field | Content |
|---|---|
| Check | P38, P2 |
| Location | p. 8, l. 225 (eq. 20); p. 8, l. 236 to 239 (eq. 22); p. 10, l. 303; p. 11, l. 335; p. 14, l. 435 to 436; p. 15, l. 441 to 442 and l. 446 to 447; Figure 5 (p. 26) panels (f), (h) and caption; Figures 7 to 9 (p. 28 to 30) middle panels; Figure 10 (p. 31) second column; Figures 14 to 16 (p. 35 to 37) |
| Quotation | "The third metric is the ratio between the posterior model covariance and the “prior” model covariance." and "low resolution, and a high total normalized uncertainty" |
| Concern | Eq. 22 defines the per-pixel quantity as the square root of the posterior covariance over the square root of the prior covariance, a standard-deviation ratio, with the posterior covariance written C̃m (eq. 20). The scalar that carries the natural-data comparison (0.87, 0.82, 0.86) is defined only in l. 436, as tr(Cm,post)/tr(Cm), a ratio of traces of variances without square root and with another symbol. The quantity is then named "normalised posterior variance" (l. 303), "normalised posterior covariance" (Figure 5f and caption items f and h), "Normalised covariance trace" (Figure 5h), "normalized posterior uncertainty" (l. 335, 441, 446), "total normalized uncertainty" (l. 436), "Posterior uncertainty" with the axis "Trace(post. cov.)" (Figures 7 to 9), "Normalised posterior uncertainty" with the axis "Trace(post.covar.)" (Figure 10) and "Total normalised posterior uncertainty" (Figures 14 to 16). The plotted values lie between about 0.27 and 0.98, which fits a ratio, not an unnormalised trace. The difference matters: a variance ratio of 0.82 corresponds to a standard-deviation ratio of √0.82 = 0.906, so the differences between the three natural runs (GB-44) shrink accordingly. |
| Suggestion | Define the scalar metric in Section 3.3 next to eq. 22, with one symbol for the posterior covariance, state whether 0.87, 0.82 and 0.86 are variance or standard-deviation ratios, and use one name for the quantity in l. 303, 335, 436, 441 and 446, in the captions of Figures 5 and 10, and on the panel titles and y-axes of Figures 5h and 7 to 10. |
| Status | verified (definitions on page images 8 and 14; names and labels on page images 10, 11, 14, 15, 26, 28 to 31, 35 to 37); inferred (that the plotted values are trace ratios, from their range; √0.82 = 0.906) |
| Severity | moderate |
| Source | S2, S3, SD |

**GB-17 The resolution maps show values close to 1 almost everywhere, which the diagonal of R as defined cannot reach and which contradicts both the text ("low resolution") and the high normalised uncertainty shown beside them.**

| Field | Content |
|---|---|
| Check | P8, P31, P3 |
| Location | p. 8, l. 230 to 239 (eq. 21); p. 10, l. 299 to 300; p. 14, l. 435 to 436; Figure 5 (p. 26) panel (d); Figure 6 (p. 27) panel (d); Figures 14 to 16 (p. 35 to 37) panel "Resolution diagonal" |
| Quotation | "Where the diagonal of R is close to 1, data have improved our knowledge considerately relative to the prior." |
| Concern | (1) Map pixels matched to the colour bar (instance AB) give median values of 0.994 (Figure 5d, bar 0.90 to 1.00), 0.987 (Figure 14), 0.992 (Figure 15) and 0.984 (Figure 16). By l. 235 to 236 this means a strong gain over the prior almost everywhere, whereas the normalised uncertainty in the same figures is 0.82 to 0.87 and l. 436 calls the zircon solution "low resolution". In Figure 15 the resolution panel is darkest (1.00) almost everywhere and lighter only at the erosion peak, where the normalised uncertainty is lowest (page image 36), the opposite of what the definitions imply. (2) R is given only implicitly by eq. 21. For the linearised Gaussian problem of eq. 20, R = I minus C̃m Cm⁻¹ has eigenvalues between 0 and 1 and rank at most rank(G); with all pixels of one unit sharing one column pattern of A (eq. 3, Figure 2c), rank(G) is at most 7, so trace(R) is at most 7. With a catchment of about 76.4 km² (Figure 4 scale bar) and 300 m pixels (GB-32) there are about 849 pixels, so the mean diagonal of R is at most 7/849 = 0.008 (21/849 = 0.025 without the unit argument), while maps near 0.9 imply a trace near 764. (3) The weak-nonlinearity assumption that justifies eq. 20 (p. 6, l. 177 to 178) is not checked, although the zircon posterior exceeds 8000 mm/y. Either the colour scale is reversed, the plotted quantity is not diag(R), or the text misreads the maps. Resolution is one of the three reliability metrics (p. 16, l. 483 to 484) and is used to judge the zircon result, so this bears on the comparison in Section 4.2.2, hence major. How was R computed? |
| Suggestion | Give in Section 3.3 the formula used for R (e.g. C̃m Gᵀ Cd⁻¹ G at the final iterate), check trace(R) against the number of independent data, recompute the resolution maps of Figures 5, 6 and 14 to 16, state in the captions what values near 1 mean, reconcile l. 299 to 300 and l. 436 with the maps, and write "considerably" in l. 236. |
| Status | inferred (map values by colour matching through transparency; bound on trace(R) from eqs. 3, 20 and 21 and the pixel count estimated from Figure 4); verified (pattern of Figure 15 on page image 36) |
| Severity | major |
| Source | AB, SD |

**GB-18 The storage assumption and the XRD limitations are disclosed only in the Discussion, not where the forward model and the XRD processing are introduced.**

| Field | Content |
|---|---|
| Check | P17 |
| Location | p. 9, l. 249 to 265 (Section 3.4); p. 5, l. 145 to 152 (Section 3.1); p. 15, l. 466 to p. 16, l. 476 |
| Quotation | "We caution against using this method in catchments with significant sediment storage, as the inversion directly links sediment provenance to erosion rates and assumes immediate sediment export" |
| Concern | The Introduction notes that the approach links sediment to its origin "without modelling storage or transport" (l. 23), and Section 3.1 says that sediments "are then transported or stored" (l. 147 to 148), but neither states the consequence that the inversion assumes immediate export; this appears first in l. 467 to 468. Grain-size effects, preferred orientation of micas and peak overlap (l. 469 to 476) bear directly on the binning in Section 3.4, which presents the max-normalised peak areas as "relative mineral concentrations" (l. 261 to 262) without these caveats. A reader of the Methods does not see them. |
| Suggestion | Move the storage and export assumption to the end of Section 3.1 and the three XRD caveats with their mitigations to the end of Section 3.4; keep the Discussion for their consequences. |
| Status | verified |
| Severity | moderate |
| Source | SD |

**GB-19 The XRD measurement and processing settings are not specified, and the availability statement covers only "the inversion tests" without naming raw diffractograms, zircon ages, the 2θ windows or sample metadata.**

| Field | Content |
|---|---|
| Check | P12, P35 |
| Location | p. 9, l. 250 to 262; p. 13, l. 396 to 398; p. 14, l. 423 to 425; p. 16, l. 490; p. 17, l. 522 to 523 |
| Quotation | "In a third step, the WinXRD Peak Finder algorithm corrects for baseline drift and removes the background noise" and "The data and codes used for the inversion tests in the study are available at https://doi.org/10.5281/zenodo.17120374" |
| Concern | A persistent DOI for data and code is given. Section 3.4 does not give the diffractometer, radiation, 2θ range, step size and counting time, the WinXRD version, threshold and peak-fitting settings, the quartz reference used for alignment, or the 2θ window per mineral selected from RRUFF (l. 257 to 258), a derived table that is not printed and directly sets A and d. The statement in l. 490 names only "data and codes used for the inversion tests", which covers synthetic data and code and possibly the binned fingerprints of Figure 11, but says nothing explicit about the raw diffractograms of source and detrital samples, the zircon U-Pb ages (whose method is described only in an unpublished master's thesis, Belotti, 2021, l. 522 to 523), the window table or the sample metadata. The manuscript has no appendix that would supply them. Whether the repository contains them could not be checked (record not readable by instance S2, HTTP 429). The statement also lacks a final full stop. |
| Suggestion | Add to Section 3.4 the instrument and scan parameters, the WinXRD version and settings, and a table of 2θ windows per mineral (supplement or repository); replace l. 490 by an itemised statement that lists raw and binned XRD data, zircon ages, the window table, sample metadata, synthetic data and code with their location in the repository or the reason they are withheld, ending with a full stop. |
| Status | verified (content of Section 3.4 and of l. 490 on page images 9 and 16); repository contents not checked |
| Severity | moderate |
| Source | S2, SD, S4 |

**GB-20 The numbers, dates and locations of source and detrital samples, the aggregation of source samples into unit fingerprints, and the identity of the benchmark sample are not reported.**

| Field | Content |
|---|---|
| Check | P8, P34, P20, P38 |
| Location | p. 9, l. 251 to 252; p. 13, l. 391 to 398; p. 14, l. 406 to 407, l. 413 to 414, l. 420 to 421, l. 423 to 424 and l. 437 to 438; Figure 13 caption (p. 34) |
| Quotation | "In a first step, in-situ source samples are collected from every lithological unit across the study area" and "Merging the inversion results from multiple detrital samples collected at the sink of this sub-catchment" and "a detrital sample taken at the same date and time" |
| Concern | Identifying the benchmark sample by date and hour (l. 423 to 424) is helpful. Not stated are: how many rock samples per unit were measured, where they were taken relative to the inferred contacts, and whether a unit fingerprint is a single sample or a mean (with what spread). For Section 4.2.1 the number, dates and times of the "multiple" detrital samples, the number of inversions entering the kernel density estimates of Figure 13 and the KDE bandwidth are not given, although the caption reads peak height as "greater consistency across inversions". For Section 4.2.2 the benchmark is "the same detrital sample" (l. 421) without antecedent, since Section 4.2.1 speaks of several samples; "the detrital sample collected on June 28, 2019, at 13:30" (l. 423 to 424, zircon); and "a detrital sample taken at the same date and time" (l. 437 to 438, XRD), which reads as a second sample. No sample identifiers are given, and the sampling location of the benchmark sample is not stated. Are the zircon and XRD data from one physical sample (split) or from two samples, and was it taken at the Gorner-Grenz confluence? The answer determines whether the two fingerprints see the same sediment. |
| Suggestion | Add to Section 3.4 or 4.2 a table of source samples (unit, number, location) and of detrital samples (identifier, date, time, location, discharge if available), state the aggregation rule for unit fingerprints, give the number of inversions and the KDE bandwidth in the Figure 13 caption, and state in l. 420 to 424 and l. 437 to 438 whether the zircon and XRD aliquots come from the same sample. |
| Status | verified (absence in the manuscript; wording on page image 14); assumption (whether zircon and XRD data come from one sample), asked as a question |
| Severity | moderate |
| Source | SD, S3, S2 |

**GB-21 The text cites Figure 3A for source sampling, but panel (a) shows detrital sampling.**

| Field | Content |
|---|---|
| Check | P3 |
| Location | p. 9, l. 251 to 252; Figure 3 (p. 24) panels (a) and (b) |
| Quotation | "In a first step, in-situ source samples are collected from every lithological unit across the study area (Figure 3A and 3B)." |
| Concern | Panel (a) is titled "detrital sampling: pump sampler", panel (b) "in-situ source sampling"; only (b) shows what the sentence describes (confirmed on page image 24 during merging). Instance S4 had listed the references to Figure 3 without a finding; the page image decides for the finding. The caption itself pairs (a) and (b) correctly as sampling of sediments and of rock samples. |
| Suggestion | Cite "(Figure 3B)" in l. 252 and Figure 3A where the detrital sampling is described. |
| Status | verified |
| Severity | minor |
| Source | AB |

**GB-22 The study site does not meet the manuscript's own recommendation of well-constrained lithology, the share of inferred lithology is not quantified, and the depth-integrated sampling recommended against grain-size effects is not shown for the pump samples.**

| Field | Content |
|---|---|
| Check | P18, P27, P26 |
| Location | p. 9, l. 270 to 272; p. 15, l. 463 to 464 and l. 469 to 471; p. 12, l. 364; Figure 3 (p. 24) panel (a); Figure 4 (p. 25) legend |
| Quotation | "In ice-covered regions, where direct geological mapping is not possible, we infer the lithology based on regional geological knowledge." and "we recommend applying this method in catchments where: a) the spatial distribution of source lithologies is well constrained" |
| Concern | (1) The manuscript recommends application only where lithology is well constrained, and its own Scenario 1 ranks map uncertainty as "the second most influential factor" (l. 364); yet the test site is a glacierized catchment whose lithology under ice is inferred (Figure 4 legend "Inferred geology and outcrops"), and the share of inferred against observed area is not quantified. The inferred map defines every column of A and thereby all posterior maps and the subcatchment test. (2) The mitigation of grain-size effects relies on "depth-integrated suspended sediment samples" (l. 470), while Figure 3a shows "detrital sampling: pump sampler", and no statement says that the samples were depth-integrated. (3) Whether sediment storage is significant at the Gorner-Grenz confluence (l. 466 to 468) is not discussed for the own site. Were the detrital samples depth-integrated? |
| Suggestion | Quantify in Section 4 the ice-covered and inferred share of the catchment and of each unit, discuss in Section 5 how the own site relates to recommendation a) and to the storage caveat, and state the sampling method of the detrital samples in Section 3.4. |
| Status | verified (inferred lithology, recommendation, pump sampler on page images 9, 15, 24, 25); assumption (whether the pump samples are depth-integrated; storage at the site) |
| Severity | moderate |
| Source | SD |

**GB-23 Lithological units carry different names and spellings in text, legends and captions, and the abbreviations used in the figures are not resolved.**

| Field | Content |
|---|---|
| Check | P38, P29 |
| Location | p. 10, l. 274 to 277 and l. 299; p. 12, l. 340; p. 14, l. 411, l. 414 and l. 431 to 434; Figure 4 (p. 25) and Figure 12 (p. 33) legends; Figure 5 (p. 26) panel (j); Figure 11 caption (p. 32); Figure 12 caption (p. 33); Figure 13 (p. 34) labels; Figures 14 to 16 (p. 35 to 37) legends |
| Quotation | "while Penninic Mesozoic sedimentary units (Bündnerschiefer) consist mainly of calcareous mica schists and quartzites" and "Stockhorn-Turftgrat-Gornergrat" and "ZSF ophiolites (metabasites, ecologites)" |
| Concern | The seven units are named identically in the legends of Figures 4 and 12; elsewhere names vary. (1) The "Penninic Mesozoic sedimentary units (Bündnerschiefer)" (l. 274 to 275) are later "Zermatt Saas-Fee sediments" (l. 299), "ZSF sediments" (l. 414) or "Zermatt - Saas Fee sediment unit" (l. 411); the identity is visible only through the outcrop entry "metamorphic bündnerschiefer" in the Figure 4 legend. The complex is spelled "Zermatt Saas-Fee" (l. 299), "Zermatt-Saas-Fee" (l. 340), "Zermatt - Saas Fee" (l. 411, 414), "Zermatt-Saas Fee" (l. 431, 432) and "Zermatt- Saas Fee" (Figure 12 caption). (2) The Monte Rosa non-granite unit is "Monte Rosa garnet-gneiss (MR g-g)" (l. 432), "Monte Rosa (garnet gneiss and micaschist)" (Figures 4, 12), "Monte Rosa (gneiss, micaschist)" (Figures 11, 13) and "MR gneiss, mica" (Figures 5, 15, 16); MR g-g occurs in no figure. (3) The Stockhorn, Tuftgrat and Gornergrat unit is "S.,T.,G." in Figures 5, 15 and 16 without explanation and "Stockhorn-Turftgrat-Gornergrat" in the Figure 11 caption, against "Tuftgrat" in l. 276; the same caption has "ecologites". (4) ZSF and MR are introduced only in the text (l. 414, 431, 432); "ELA estimation" in the Figure 4 legend is not resolved; Figure 14 has no legend for its lithology colours and the age-bin unit "Ma" only on the last bar; the black outlines are explained only through the "Gorner glacier" entry of Figures 5, 15 and 16; the Figure 4 caption does not explain the two insets. This matters in l. 433 to 434, where the reader must infer which figure column carries the copied MR g-g fingerprint. |
| Suggestion | Introduce each unit in l. 274 to 279 with the name and abbreviation used in Figures 4 and 11 to 16 (e.g. "Zermatt-Saas Fee sediments (ZSF sediments; Bündnerschiefer)", "Monte Rosa garnet gneiss and micaschist (MR g-g)", "Stockhorn, Tuftgrat and Gornergrat units (S.,T.,G.)"), use one spelling ("Zermatt-Saas Fee") and these names in l. 299, 340, 411, 414, 431 to 434 and in all legends and captions; write "Stockhorn-Tuftgrat-Gornergrat" and "eclogites" in the Figure 11 caption; resolve ELA, ZSF, MR and S.,T.,G. in the captions, add a lithology legend to Figure 14, and describe insets and outlines in the captions. |
| Status | verified (page images 10, 14, 25, 26, 32 to 37) |
| Severity | minor |
| Source | S2, AB |

**GB-24 Third-party data underlying the geological map and land cover of Figure 4 are credited only inside the figure and are neither referenced nor covered by the availability statement.**

| Field | Content |
|---|---|
| Check | P12 |
| Location | Figure 4 (p. 25) credit block at lower right; p. 9, l. 270 to 272; p. 16, l. 490; reference list (p. 17 to 21) |
| Quotation | "Land cover data: SwissTopo 2018 Geological data: data from Steck et al., 2015, personal communication by L. Baumgartner, outcrops by GeoCover" |
| Concern | The map of potential source areas is input c) of the method (l. 65) and the basis of the tracer matrix A. The text (l. 270 to 272) says that the lithology was inferred from regional geological knowledge and outcrop observations, citing Bearth (1953) and Steck et al. (2015). Only the figure credit discloses three further sources: SwissTopo land cover of 2018, GeoCover outcrops and a personal communication; the glacier outline and the "ELA estimation" in the Figure 4 legend have no source. A text search of the reference list finds neither SwissTopo nor GeoCover. The availability statement (l. 490) does not say whether the resulting raster of source areas, which rests partly on unpublished information, is deposited. |
| Suggestion | Cite SwissTopo and GeoCover (product, version, year, licence) in the References and in l. 270 to 272, state the source of the glacier outline and of the ELA, and state in l. 490 whether the source-area raster used for A is deposited. |
| Status | verified (page image 25; text search of the reference list) |
| Severity | moderate |
| Source | S2 |

#### Minor corrections

| ID | Location | Quotation | Replacement | Source |
|---|---|---|---|---|
| KK-03 | p. 9, l. 267; p. 15, l. 463; Figure 11 caption (p. 32) | "Gorner-gletscher catchment" (l. 267, Figure 11) and "Gorner gletscher catchment" (l. 463) | "Gornergletscher catchment", as in l. 272 and l. 282 (l. 392, 400, 498 and 499 use "Gorner Glacier") | S2, S4 |
| KK-04 | Figure 3 (p. 24) panel (c) legend | "quarz pattern alignment" | "quartz pattern alignment" | S2, AB |
| KK-05 | Figure 4 (p. 25) and Figure 12 (p. 33) legends | "biotite schits" | "biotite schists" | AB |
| KK-06 | Figure 4 (p. 25) and Figure 12 (p. 33) legends | "caclcite-zoisite amphibolites" | "calcite-zoisite amphibolites" | AB |
| KK-07 | Figure 4 (p. 25) and Figure 12 (p. 33) legends | "silimanite-biotite gneiss" | "sillimanite-biotite gneiss" | AB |
| KK-08 | Figure 4 (p. 25) and Figure 12 (p. 33) legends | "calcarious mica schist" | "calcareous mica schist" | AB |
| KK-09 | Figure 4 (p. 25) and Figure 12 (p. 33) legends | "GornergratPermo-Mesozoic" | "Gornergrat Permo-Mesozoic" | AB |

#### Verification log

| ID | Check | Checked | Values | Result |
|---|---|---|---|---|
| PP-13 | P4, P29, P3 | Every figure reference in the text against the figure and its panels; inventory of figures and captions | Fig. 1A to 1D (l. 146 to 149), Fig. 2A to 2C (l. 166 to 167), Fig. 3A to 3E (l. 251 to 262), Fig. 4 (l. 268 to 270, 299), Fig. 5A to 5K (l. 289 to 308, 316), Fig. 6C to 6G (l. 314 to 319), Fig. 7 (l. 334), Fig. 8 (l. 347), Fig. 9 (l. 356 to 357), Fig. 10 (l. 371), Fig. 11 (l. 398), Fig. 12 (l. 412), Fig. 13 (l. 414), Fig. 14 (l. 429, 430), Fig. 15 (l. 438), Fig. 16 (l. 445); 16 figures on p. 22 to 37, no graphical abstract, tables or appendix figures | all 16 figures referenced in their own section, first references in ascending order; wrong references in GB-21 and GB-28; no finding otherwise |
| PP-14 | P8 | Equations 1 to 22 at page images 5 to 8 | eq. 1 weighted average with normalisation by the sum of exp(εj); eq. 2 rescaling by the total erosion rate; eq. 3 d = A · exp(ε); eqs. 6, 7, 10, 11, 13, 15, 16, 17, 20, 21 consistent with the text | no finding for these; eqs. 5, 9, 12, 14 in GB-15; eqs. 18, 19 in GB-12 and GB-14; eq. 22 in GB-16 |
| PP-15 | P26 | Positivity guarantee by the log-space parametrisation | ėj = ė0 exp(εj) in eqs. 3, 17, 18 and 19; exp is positive for every path | no finding |
| PP-16 | P5 | Stopping rule (l. 243 to 244) against reported runs; JS threshold against the natural data | Figure 5i data misfit still decreasing at iteration 100, run stopped at the maximum; threshold 0.55 (l. 352): zircon 0.48 below and unstable, combined 0.57 above | no finding; iteration rule in GB-37 |
| PP-17 | P12 | Data sources that are published or covered by the statement | Synthetic data and inversion code named in l. 490; geological maps Bearth (1953, l. 521) and Steck et al. (2015, l. 631 to 633); RRUFF reference spectra cited as Lafuente et al. (2015, l. 599 to 600) for l. 257 to 258; no appendix; repository DOI 10.5281/zenodo.17120374, reachability not checked (HTTP 429) | no finding for these sources; others in GB-13, GB-19, GB-24 |
| PP-18 | P19 | Provenance class of each data source and of the core claims | Synthetic (model-generated): Section 4.1, l. 287 to 389, 103 lines; natural (primary, processed): Section 4.2, l. 390 to 449, 60 lines; synthetic share 103/163 = 63.2 %; synthetic data labelled as such throughout; inferred geology labelled "Inferred geology" in Figure 4 | no finding on labelling; consequences in GB-22 and GB-25 |
| PP-19 | P29 | Font sizes in print size (cap or figure height at 300 dpi) | Figure 1 7.0 to 12.0 pt; Figure 2 6.7 to 12.0 pt; Figure 3 8.3 pt; Figures 5 to 7 5.7 to 6.3 pt; Figures 8, 9 5.7 pt; Figure 10 3.3 to 3.7 pt; Figure 11 6.3 to 6.7 pt; Figure 13 7.7 to 8.3 pt; Figures 14 to 16 colour bar labels 5.0 to 5.3 pt, legends 6.0 pt; calibration caption capital 8.3 pt | below 6 pt in GB-49; Figures 5 to 9 within the 0.6 pt tolerance, no finding |
| PP-20 | P3 | Counts in the schematics of Figures 1 to 3 | Figure 3d: 11 2θ windows and 11 concentration bars; Figure 3e: 11 windows and 11 bars per source sample; Figures 1 and 2: 11 bars per tracer row | windows and bars correspond; no finding |
| PP-21 | P38 | Unit legends of the two map figures | Figure 4 and Figure 12 legends: seven units and their outcrop entries identical in wording (page images 25 and 33) | no finding; text and other figures in GB-23 |
| PP-22 | P3 | Map colours of Figures 4 and 12 against their legends | Eastern Monte Rosa granite: Figure 4 #ecacac and #f4acac, Figure 12 #f4acac, swatch #fcacac (difference 8) | no finding; fading in Figure 12 in GB-51 |
| PP-23 | P3 | Scale bars of the catchment maps | Catchment width: Figure 4 13.18 km, Figure 12 13.36 km, Figure 14 13.44 km, Figure 15 13.39 km, Figure 16 13.32 km | consistent within 2 %; no finding |

### Segment 3: Results (p. 10 to 15)

#### Substantive findings

**GB-25 The synthetic validation uses noise-free data generated with the same forward operator and source matrix as the inversion, a single true pattern, and a prior equal to the true mean, so convergence and robustness are tested under the most favourable conditions.**

| Field | Content |
|---|---|
| Check | P9 |
| Location | p. 10, l. 288 to 295; p. 11, l. 324 to 326; p. 13, l. 374 to 376; p. 16, l. 482 to 484; Figure 5 (p. 26) panel (a) |
| Quotation | "we generate synthetic detrital data using the forward model applied to a “true” erosion rate map featuring a localised hotspot with elevated erosion intensities" and "A longer smoothing distance effectively constrains the posterior closer to the prior (set here as the average true erosion rate)" |
| Concern | (1) No noise is added to the synthetic detrital data (the word "noise" occurs only for the XRD background, l. 255, and in the Figure 3 legend), and except in Scenario 1 the same A and the same grid generate and invert the data. Using the same ingredients to synthesise and invert data is known as the inverse crime: Wirgin, A. (2004) The inverse crime. arXiv: math-ph/0401050. Available at: https://arxiv.org/abs/math-ph/0401050 (abstract read during merging: "The inverse crime occurs when the same (or very nearly the same) theoretical ingredients are employed"), not in the reference list; it makes recovery look better than with real data. (2) Only one true map (one hotspot, Figure 5a) is tested; recovery of hotspots in small units, which the manuscript itself flags as poorly resolved (l. 299 to 300), or of several hotspots is not tested. (3) The prior equals the average true erosion rate in all synthetic runs; the manuscript itself notes that this pulls the posterior towards the truth for long L (l. 374 to 376). (4) Hyperparameters are tuned against the same truth (GB-34, GB-35). The conclusion that "the true erosion pattern can be reliably recovered" (l. 482) therefore holds only for this configuration, and 103 of 163 lines of the validation (63.2 %) rest on these synthetic data (PP-18). Convergence and robustness are central results of the Abstract and Conclusions, hence major. |
| Suggestion | Counter-design: generate synthetic data with a forward model independent of the inversion grid (finer grid, or A perturbed by the within-unit spread of source samples), add noise with the replicate XRD variance (GB-02), test several true maps (hotspots in each unit including ZSF sediments and Furgg, several hotspots, a uniform field), set the prior independently of the truth (e.g. from a perturbed export estimate), select hyperparameters on one set of maps and evaluate on another, and report error distributions across maps in Section 4.1. |
| Status | verified (no noise, one map, prior; source read); inferred (consequence for the robustness claim) |
| Severity | major |
| Source | SD |

**GB-26 The synthetic set-up cannot be rebuilt from the text: how the synthetic fingerprints, the true map, the modified geological map, the blending and the PCA tracer subset were constructed is not stated.**

| Field | Content |
|---|---|
| Check | P8 |
| Location | p. 10, l. 288 to 294; p. 11, l. 327 to 333; p. 12, l. 343 to 347 and l. 355 to 357; Figure 5 (p. 26) panel (k) |
| Quotation | "We perform a Principal Component Analysis (PCA) to retain the subset of tracers that explain the maximum variance in the mineralogical fingerprints." |
| Concern | Not given: how the 21 by 7 synthetic fingerprints of Figure 5k were generated (random, derived from Figure 11, other); shape, amplitude and position of the true hotspot; pixel size (only implied as 300 m, GB-32) and number of pixels; how the "geological map with minimal difference" was constructed; the blending formula and step for "approaching each lithology’s mineral concentration to its mean across all lithologies" (l. 343 to 344); and how a subset of original tracers is selected from a PCA, which yields linear combinations, not tracers. The archived code (l. 490) may contain these, but the text should let the reader follow them. |
| Suggestion | Add to Sections 4.1.1 and 4.1.3 the generating rule for fingerprints and true map, the grid (pixel size, number of pixels), the construction of the modified map, the blending equation and the tracer selection rule (e.g. ranking tracers by their loading on the first k components). |
| Status | verified |
| Severity | moderate |
| Source | SD |

**GB-27 The steepest-descent run ends closer to the true map than the quasi-Newton run, at a different iteration budget, while the text adopts quasi-Newton as the more accurate scheme.**

| Field | Content |
|---|---|
| Check | P21, P3 |
| Location | p. 11, l. 314 to 316 and l. 320 to 321; p. 10, l. 293; Figure 5 (p. 26) panels (c), (g); Figure 6 (p. 27) panels (c), (g) |
| Quotation | "Based on these findings, we adopt the Quasi-Newton (QN) approach for all subsequent tests, as it provides a more stable and accurate reconstruction of the erosion rate patterns." |
| Concern | The figures support that QN converges faster (l. 315 to 316). Measured in panel (g), the summed absolute difference between true and posterior rates is: QN (Figure 5g, 100 iterations, l. 293) minimum 197.3 ± 0.6 near iteration 20, final 201.0 ± 0.6 at iteration 100; SD (Figure 6g, axis to 200 iterations) 330.7 at iteration 25, 211.3 at 100, 194.1 at 150, final 193.0 ± 0.8 at 200 (instance AB; instance S3 measured 201.2 and 192.8 independently). The SD end state is 8.0 lower than the QN end state (8.0/201.0 = 4.0 %) and 4.3 lower than the QN minimum, beyond the combined uncertainty. Panel (c) points the same way: the most negative difference at the hotspot is about -2.36 for QN and -1.72 for SD (colour matching), so the features "smoothed out or missed" in SD (l. 314) appear as a smaller overshoot, not a larger error. The SD parameters (iterations, step size, L, σm, σd) are not stated in Section 4.1.2. "Faster" is supported, "more accurate" is not; at equal iterations or at convergence the accuracy comparison reverses or becomes a tie. The choice of QN for all later tests rests on this comparison of the two schemes named in the Abstract (l. 4 to 5); instance AB graded it major and S3 moderate, and the higher grade applies. |
| Suggestion | In Section 4.1.2 state the SD parameters and iteration count, report the final errors and uncertainties of both schemes at convergence and at equal iteration counts, and state the criterion for choosing QN; rephrase l. 320 to 321 to "faster and more stable" unless a metric shows higher accuracy for QN. |
| Status | verified (panel (g) values measured by instances AB and S3; iteration axes on page images 26 and 27); inferred (panel (c) extremes by colour matching on semi-transparent maps; percentages) |
| Severity | major |
| Source | S3, AB |

**GB-28 The text dates the onset of oscillations in the steepest-descent posterior covariance to 125 iterations and cites panel 6G against itself; panel (h) shows a single kink at about 138 iterations and no resolvable oscillation.**

| Field | Content |
|---|---|
| Check | P3, P4 |
| Location | p. 11, l. 316 to 317; Figure 6 (p. 27) panels (g), (h); Figure 5 (p. 26) panel (h) |
| Quotation | "This limited sensitivity to strong gradients also leads to oscillations in the posterior covariance, visible after 125 iterations, as the Jacobian fluctuates between iterations (Figure 6G versus Figure 6G)." |
| Concern | The normalised posterior covariance during the iterations is panel (h) in the captions of Figures 5 and 6, not (g), and the reference compares 6G with itself. Measured in Figure 6h (instance AB): the curve rises monotonically to its maximum at iteration 137.9 ± 0.8 and then decreases monotonically from 0.7425 to 0.7424; the upper envelope between these points changes by at most 1 px per 8 px step without reversal. An oscillation is not visible at print resolution, and 125 iterations lies 12.9 iterations before the kink. |
| Suggestion | Correct the reference, probably to "(Figure 6H versus Figure 5H)", give the iteration of the kink as read from the data, and either show the oscillation (inset or difference plot) or describe the behaviour as a kink followed by a slow decrease. |
| Status | verified |
| Severity | minor |
| Source | AB, S4, SD |

**GB-29 The geological-map scenario and the blending scenario use different names for the same maps, examples and mismatch metric in text, figure titles, labels and captions.**

| Field | Content |
|---|---|
| Check | P38 |
| Location | p. 11, l. 330 to 339; Figure 7 (p. 28) map titles, scatter labels, x-axes, colour bar and caption; p. 12, l. 347 to 348; Figure 8 (p. 29) titles and caption |
| Quotation | "In the left scatterplot, the labels correspond to the maps above." |
| Concern | Scenario 1: the map-difference metric is "area mismatch" in the text (l. 330, 335), "area difference (m2 )" in the Figure 7 caption, "Area difference" on its x-axes, and "Geology misalignment (m²)" on the Figure 7 colour bar. The reference map is "the same geological map" (l. 332), "the original geological map" (l. 331, 339), "Originial geology (same as forward)" (map title, with a typo) and "Forward geology" (scatter label); the second map is "a geological map with minimal difference" (l. 333), "a simplified geological map with minimal changes" (l. 338 to 339), "Geology with minimal changes" and "Minimal changes"; "simplified" also suggests another operation than minimal changes. The caption states that the scatter labels correspond to the map titles, but the wording differs. Scenario 2: the three examples are "highly blended", "intermediate" and "the original synthetic fingerprints" (l. 348), "Almost fully blended", "Medium blended" and "Unblended" (Figure 8 titles), and "the most blended", "the half-way in between" and "the original synthetic fingerprints" (Figure 8 caption). |
| Suggestion | Use one term for the metric ("area mismatch (m²)") in l. 330 to 336 and on the axes, colour bar and caption of Figure 7; use the Figure 7 map titles as scatter labels and in l. 331 to 339, correcting "Originial" to "Original"; name the three Figure 8 examples identically in l. 348, the panel titles and the caption. |
| Status | verified (page images 11, 12, 28, 29) |
| Severity | minor |
| Source | S2, AB |

**GB-30 The Jensen-Shannon distance is defined for probability distributions, but the fingerprints are normalised by their maximum, and the conversion used before computing the distance is not stated.**

| Field | Content |
|---|---|
| Check | P8 |
| Location | p. 12, l. 345 to 347; p. 9, l. 261 to 262; p. 12, l. 352; p. 15, l. 447 to 448 |
| Quotation | "the average Jensen-Shannon (JS) distance, which measures the similarity between two probability distributions" |
| Concern | Section 4.1.3 measures distinctiveness by the average JS distance over all source pairs (l. 345 to 347), and the threshold of 0.55 (l. 352) and the natural values 0.48 and 0.57 (l. 448) rest on it. The JS distance requires vectors that sum to one, whereas the fingerprints are "normalized within each sample by dividing by the maximum observed peak area" (l. 261); for the combined data set the vector mixes 21 mineral peak areas and 13 zircon age-bin abundances. Whether the fingerprints were renormalised to unit sum, and with which logarithm base the distance was computed, is not stated; both change the values and thus the position of the natural runs relative to the 0.55 threshold. The point was a hint of instance S3 that no instance treated; a text search of Sections 3.4 and 4.1.3 confirms the absence. |
| Suggestion | State in l. 345 to 347 how fingerprints are converted to distributions before the JS distance is computed (renormalisation, logarithm base) and how the combined vector is treated, so that 0.48, 0.57 and the threshold of 0.55 can be reproduced. |
| Status | verified (absence of the conversion in the text); inferred (effect on the values) |
| Severity | moderate |
| Source | ZF |

**GB-31 Twenty blending levels are said to be tested, but Figure 8 plots 14; the caption accounts for one, and the number of non-converging runs is not given.**

| Field | Content |
|---|---|
| Check | P23, P34, P36, P3 |
| Location | p. 12, l. 348 to 349 and l. 352 to 354; Figure 8 (p. 29) scatterplots and caption |
| Quotation | "In total, 20 values between the highly blended and the original synthetic fingerprints are tested" and "In many of these cases, the inversion fails to converge to a stable posterior solution." and "Note that the most blended example did not have a stable solution and is therefore not plotted." |
| Concern | Three instances counted independently (S3, SD, AB): 14 markers in the absolute-error and posterior-uncertainty panels, at average JS 0.249, 0.272, 0.338 and 0.359, then 0.441 to 0.624 in ten steps of about 0.02, with no point between 0.36 and 0.44. Balance: tested 20, excluded by the caption 1, expected plotted 19, plotted 14, unexplained 5 (6 if the 20 do not include the original set). Resolution A: five further runs did not converge and were dropped without mention; then "many of these cases" means at least 6 of 20, and the plotted error curve is censored where failure is most frequent. Resolution B: fewer than 20 levels were run. Resolution C: overlapping markers; the spacing of about 0.02 in JS makes this unlikely. Which applies? |
| Suggestion | State in l. 348 to 354 and the Figure 8 caption how many of the 20 runs converged and at which JS values the others failed, and mark them in Figure 8 (e.g. open symbols on the x-axis). |
| Status | verified (count on page image 29 by three instances); assumption (that the missing runs are non-converging ones), asked as a question |
| Severity | moderate |
| Source | S3, SD, AB |

**GB-32 The error plotted in Figures 5 to 10 is a sum over pixels without unit, the text reports it as a rate in mm/yr, and the number of pixels and the pixel size are not stated.**

| Field | Content |
|---|---|
| Check | P20, P29, P3 |
| Location | p. 12, l. 351 to 353; Figure 8 (p. 29) y-axis; Figure 5 (p. 26) and Figure 6 (p. 27) panels (a), (b), (c), (g); Figures 7, 9 and 10 (p. 28, 30, 31) error axes |
| Quotation | "As the JS distance decreases below 0.55, both absolute error and posterior uncertainty rise sharply, with errors exceeding 700 mm/yr" |
| Concern | All error axes are labelled as a sum of absolute differences between true and posterior rates, with a baseline of about 197 and values up to about 676,000 in Figure 8; the colour bars of the erosion maps in Figures 5 and 6 (0.5 to 3.0 and -2 to 2) and the error axes carry no unit, while Figures 13 to 16 state mm/y. The text turns the Figure 8 sum into "700 mm/yr", which reads as a per-pixel or catchment-mean rate; for JS below 0.44 the four plotted values are about 47,400, 676,400, 6,000 and 322,100 (instance AB), so neither reading of "700" can be checked against the figure. The denominator is not stated anywhere; the pixel size of 300 m follows only from "4 times the pixel size (L = 1200 m)" (1200/4 = 300) and "10 times the pixel size (3000 m)" (3000/10 = 300). Comparisons between synthetic tests on the same grid remain valid; absolute magnitudes cannot be interpreted. The unit form "mm/yr" also differs from "mm/y" used in l. 295, 325, 384, 428 and 435. |
| Suggestion | State pixel size and number of pixels in Section 4.1.1; report errors as mean absolute error per pixel in mm/y or as a sum with unit and pixel count; add "(mm/y)" to the colour bars and axes of Figures 5 to 10; correct l. 352 to 353 accordingly, writing "mm/y". |
| Status | verified (axis labels, missing units and missing pixel count on page images 26 to 31); inferred (pixel size of 300 m) |
| Severity | moderate |
| Source | S3, AB |

**GB-33 The ranking of the three degradation factors compares perturbations of arbitrary size, and the general statement on map mismatch is contradicted by two of the three maps; over the tested ranges, tracer reduction changes error and uncertainty more than map uncertainty.**

| Field | Content |
|---|---|
| Check | P21, P9, P6, P3 |
| Location | p. 12, l. 363 to 365; p. 11, l. 332 to 339; p. 12, l. 340 to 342 and l. 348 to 358; Figure 7 (p. 28); Figure 8 (p. 29); Figure 9 (p. 30) |
| Quotation | "To summarize, among the three tested scenarios, the strongest impact on the posterior solution arises from reduced fingerprint distinctiveness. Geological map uncertainty follows as the second most influential factor." and "We observe that the greater the mismatch between the geological map used in the inversion and the one used to generate the synthetic data, the larger the discrepancy between the posterior and true erosion rate maps." |
| Concern | The scenarios differ in the number of cases (3 maps, 20 blending levels, 21 tracer counts) and in how far each degradation is pushed. Measured on the figures by instances S3 and AB: Scenario 1, summed error 197.4 (same map), 193.5 (minimal changes) and 274.9 (map of Steck et al.), largest increase 77.5 (77.5/197.4 = +39.3 %); normalised uncertainty 0.7402, 0.7376 and 0.7460, range 0.0084. Scenario 3, summed error 197.2 (7 to 21 tracers) up to 347.9 (2 tracers), increase 150.7 (+76.4 %); uncertainty 0.740 up to 0.961 (+29.9 %). Over its tested range the tracer scenario has the larger effect on both metrics; the ranking holds only if the tracer scenario is cut at 7 tracers, while the map scenario is taken at its largest mismatch of about 1.13e7 m² (about 15 % of the catchment area of about 76.4 km² estimated from Figure 4) and the blending scenario down to JS = 0.225, far below the natural values 0.48 and 0.57 (l. 448). In Scenario 1 the minimal-changes map gives both a lower error (193.5 against 197.4) and a lower uncertainty (0.7376 against 0.7402) than the same map; the text explains the lower error ("Surprisingly", l. 338 to 341) but keeps the general monotonic statement and does not mention the lower uncertainty; data and model misfit do rise monotonically, as l. 341 to 342 say. The ranking is the stated result of the degradation tests and feeds the recommendations (l. 456 to 466), hence major. |
| Suggestion | Express each scenario on a common scale in Section 4.1.3 (e.g. relative change of error and uncertainty against the undegraded baseline at degradation levels realistic for the Gornergletscher case), report the numbers in a table, extend Scenario 1 by more maps with graded mismatch (e.g. 10 to 20 random boundary shifts of increasing amplitude), and rephrase l. 337 to 338 and l. 363 to 365 accordingly, or remove the ranking. |
| Status | verified (marker positions measured by instances S3 and AB; quotations); inferred (percentages, area share and the possible reversal) |
| Severity | major |
| Source | S3, SD, AB |

**GB-34 The parameter values marked in Figure 10 differ from those used in all tests for three of five parameters, and the values held fixed during each sweep are not stated.**

| Field | Content |
|---|---|
| Check | P2, P22, P7 |
| Location | p. 12, l. 367 to 371; Figure 10 (p. 31) third column; p. 10, l. 294 to 295; p. 11, l. 324 to 326; p. 14, l. 426 to 428; p. 13, l. 385 |
| Quotation | "a smoothing distance of 4 times the pixel size (L = 1200 m), a model standard deviation of 3, a data standard deviation of 0.01 mm/y" and "The results of the hyperparameter sweeps are shown in Figure 10." |
| Concern | Values side by side (figure label against text): L 3000 m against 1200 m; σm 6.2 against 3; σd 0.003 mm/y against 0.01 mm/y; μ 0.1 against 0.1; nm 25 against 25 (100 in the first QN test, l. 293); two of five agree. Possible readings: (A) the labels mark the optimum of each sweep; then the tests use non-optimal values for L, σm and σd without explanation, and the text names only the step size as optimal (l. 385); (B) the labels mark the base values held fixed in the other sweeps; then the sweeps ran at other settings than the tests. The summed error at the baseline is about 197 in Figure 7 (same map), Figure 9 (7 to 21 tracers) and Figure 10, rows 2 to 5, and about 195 at L of about 1230 m in row 1 (instances S3, AB, SD), which points to (A) and suggests that L = 1200 m, σm = 3, σd = 0.01 mm/y, μ = 0.1 and 25 iterations were held fixed; a reader can derive this only by comparing baselines across figures. |
| Suggestion | State in the Figure 10 caption what the labelled values mean; in Section 4.1.4 name the fixed values of the other parameters in each sweep and the reason for the adopted values L = 1200 m, σm = 3 and σd = 0.01 mm/y. |
| Status | verified (labels on page image 31; text values); inferred (reading A and the fixed values from the measured baselines) |
| Severity | moderate |
| Source | S3, SD |

**GB-35 The smoothing-distance sweep ends at 3000 m, so the stated deterioration beyond 3000 m is not shown, and within the tested range the error falls monotonically to its lowest value at 3000 m, 2.6 times below the value at the adopted L = 1200 m.**

| Field | Content |
|---|---|
| Check | P11, P3, P5 |
| Location | p. 12, l. 373 to p. 13, l. 374; Figure 10 (p. 31) first row; p. 10, l. 294; p. 11, l. 325; p. 14, l. 427 |
| Quotation | "However, beyond approximately 10 times the pixel size (3000 m), the solution becomes overly smooth, causing the posterior to deviate from the true erosion rates." |
| Concern | Measured by three instances: 20 values of L from about 200 m to 3001 m; the summed error falls monotonically from about 257 to about 76 (AB 257.1 to 76.1, S3 257.2 to 76.9, SD 256.6 to 75.9), and the normalised uncertainty falls likewise (confirmed on page image 31). No tested case lies beyond 3000 m, so the deviation claimed there has no reported result. At L of about 1230 m the error is about 195, i.e. 195.0/76.1 = 2.56 times the value at 3000 m; the adopted L = 1200 m is not the best value of the sweep, and the text does not say why it is kept. The manuscript itself notes that a longer L pulls the posterior towards the prior, which equals the true mean (l. 374 to 376), which links the sweep to GB-25. |
| Suggestion | Extend the sweep of Figure 10, first row, beyond 3000 m, or delete the sentence in l. 373 to 374; state in Section 4.1.4 why L = 1200 m is used although the sweep favours larger L. |
| Status | verified (axis range and values measured by instances S3, AB and SD); inferred (ratio) |
| Severity | moderate |
| Source | S3, AB, SD |

**GB-36 The described effect of the data standard deviation is not visible in Figure 10: error, uncertainty and model misfit vary by less than 0.06 %, and the error rises monotonically.**

| Field | Content |
|---|---|
| Check | P21, P3 |
| Location | p. 13, l. 380 to 384; Figure 10 (p. 31) third row |
| Quotation | "Very low data standard deviation values lead to large differences between the posterior and true erosion rate maps" and "Beyond a data standard deviation of approximately 10-2 mm/y, model misfit begins to decrease rapidly while data misfit stabilizes." |
| Concern | The left panel uses an axis offset of 197.4 (printed "+1.974e2"). Measured by instances AB and S3, the summed error rises monotonically from 197.4197 to 197.4431, a range of 0.023, i.e. 0.012 % of the value, without large differences at low σd, without a minimum and without a plateau. The normalised uncertainty spans 0.74015 to 0.74040 (0.034 %) and the model misfit 1.5614 to 1.5623 (0.06 %), which the text calls a rapid decrease. Within the tested range of 0 to 0.9 mm/y the posterior is practically insensitive to σd, the opposite of l. 380 to 384. The exponent in l. 384 is set as "10-2" instead of 10⁻². |
| Suggestion | Rewrite l. 380 to 384 to match Figure 10 (or replace the panel if another run was intended), state the insensitivity explicitly since it bears on σd = 0.01 mm/y (l. 295, 325, 428), and write "10⁻² mm/y". |
| Status | verified (axis offset, tick labels and monotonic course measured by instances AB and S3; page image 31); inferred (percentages) |
| Severity | moderate |
| Source | S3, AB |

**GB-37 The statement that the posterior fails to converge below 25 iterations does not match Figure 10, where only the run with about 5 iterations deviates, and the 25 iterations used in all later runs are not related to the convergence criterion of 115 iterations.**

| Field | Content |
|---|---|
| Check | P3, P5 |
| Location | p. 13, l. 387 to 389; Figure 10 (p. 31) fifth row; p. 9, l. 243 to 244; p. 11, l. 324; p. 14, l. 426 |
| Quotation | "Only when the maximum number of non-linear steps is reduced below 25 does the posterior fail to converge to the true erosion map." |
| Concern | Measured by instance AB (summed error at the maximum number of iterations): 4.9 iterations 268.7; 14.9 iterations 200.9; 24.9 iterations 197.6; 34.9 iterations 199.6; 44.9 iterations 200.6; from 55 iterations on 200.9 to 201.1. Only the first run fails; at about 15 iterations the value equals the plateau, and 25 iterations give the minimum, after which the error rises again by about 3.3. The text states that the change in data misfit per step falls below 10⁻⁵ only beyond 115 iterations (l. 388 to 389), while the degradation and natural runs stop at 25 iterations, 25/115 = 21.7 % of that, Figure 5 uses 100 and Figure 6 up to 200; the stopping rule of l. 243 to 244 is related to neither number. |
| Suggestion | Revise l. 387 to 388 to the measured behaviour, mention that the error rises again after 25 iterations, and justify 25 iterations against the criterion of l. 388 to 389, or use one iteration rule for all reported runs. |
| Status | verified (values measured by instance AB on page image 31); inferred (percentage) |
| Severity | moderate |
| Source | AB, SD |

**GB-38 One of the 21 tracer minerals is "Chrysolite" in the text but "Chrysotile" in all figures, two different minerals.**

| Field | Content |
|---|---|
| Check | P38 |
| Location | p. 13, l. 395; Figure 11 (p. 32) row 7; Figure 15 (p. 36) and Figure 16 (p. 37) bar labels; p. 10, l. 274 |
| Quotation | "Fayalite, Dolomite, Diopside, Chrysolite, Antigorite, Anorthite" |
| Concern | The mineral list in l. 393 to 396 and the rows of Figure 11 agree in number (21 each) and in 20 of 21 names (set comparison in Python by instance S2: text minus Figure 11 = Chrysolite, Figure 11 minus text = Chrysotile; Figures 11, 15 and 16 identical). Chrysolite is a name for a yellowish green variety of olivine (minerals.net, "Chrysolite", https://minerals.net/variety/chrysolite), whereas chrysotile is a member of the serpentine group (minerals.net, "Chrysotile", https://minerals.net/variety/chrysotile), and the serpentinites of the study area are described as "predominantly antigorite and chrysotile" (l. 274). The two names denote different minerals with different RRUFF reference spectra; since the 2θ windows are selected per mineral from RRUFF (l. 257 to 258), the reader cannot tell which window was used for this tracer. The list also contains fayalite, another olivine. |
| Suggestion | Correct l. 395 to the mineral actually used (presumably "Chrysotile") and state the RRUFF reference used for it. |
| Status | verified (page images 10, 13, 32, 36, 37; definitions in the web sources read by instance S2); assumption (which mineral's window was used) |
| Severity | moderate |
| Source | S2, S3, AB, SD |

**GB-39 Research question 1 is answered by a qualitative statement only, and Figure 11 gives identical fingerprints for three pairs of minerals, so the 21 tracers do not denote separate abundances.**

| Field | Content |
|---|---|
| Check | P3, P10, P31, P32 |
| Location | p. 13, l. 399 to 401; p. 10, l. 282 to 283; p. 9, l. 259 to 262; Figure 11 (p. 32) |
| Quotation | "The mineralogical fingerprints derived from processed and binned XRD data align well with established knowledge of the lithology in the Gorner Glacier catchment (Bearth, 1953; Steck et al., 2015), supporting the 1) the robustness of the cleaning and binning approach, and 2) the validity of the input data for the inversion method." |
| Concern | (1) The question asks whether the fingerprints "align with the expected mineralogical compositions" (l. 282 to 283), but the expected compositions are not tabulated, no agreement measure is given, and no independent check (e.g. Rietveld quantification or thin sections of the same samples) is reported; two conclusions are nonetheless drawn. (2) Measured bar lengths (instance AB, 300 dpi; column maxima 243 to 245 px, consistent with normalisation to the maximum): anorthite and pyroxene are identical in all seven units (1, 35, 245, 93, 243, 7, 104 px), annite and phlogopite are identical (1, 132, 76, 138, 52, 161, 132 px), ankerite and dolomite differ by at most 2 px, and muscovite equals annite in six of seven columns (pairs confirmed by eye on page image 32). Identical vectors mean that these mineral names denote the same binned signal, so the tracer set has fewer independent columns than 21; are 2θ windows shared? (3) Further readings raise questions: tremolite reaches 218/244 = 0.89 of the column maximum in the Monte Rosa granite, close to quartz; antigorite and chrysotile reach high values in the Stockhorn-Tuftgrat-Gornergrat unit (garnet-mica schists, quartzites); in the unit named metabasites and eclogites omphacite reaches 13/243 = 0.05 and almandine 24/243 = 0.10, although an eclogite consists mainly of garnet and omphacite (British Geological Survey, Rock Classification Scheme, entry Eclogite, read by instance AB). Because the values are max-normalised peak areas, not abundances (l. 261 to 262), these readings are questions, not contradictions: mineral signals or window overlap? Checking the fingerprints against the expected mineralogy is the first aim of the natural-data tests, hence major. The sentence also contains a doubled article ("supporting the 1) the robustness"). |
| Suggestion | State the 2θ windows per mineral and explain the identical fingerprints; merge tracers that share windows or report the number of independent tracers; tabulate the expected mineral assemblage per unit from Bearth (1953) and Steck et al. (2015) and score each of the 21 minerals against Figure 11 (e.g. a presence and absence table); verify a subset of source samples by an independent quantitative method; discuss the tremolite, serpentine and garnet and omphacite signals in Section 4.2; delete the second "the" in l. 400. |
| Status | verified (identical bar lengths measured by instance AB and seen on page image 32; absence of expected compositions and of an agreement measure); inferred (loss of independent tracers); assumption (mineralogical plausibility of individual signals) |
| Severity | major |
| Source | AB, SD |

**GB-40 The natural known-mixture test has a single negative control, a small unit already flagged as poorly resolved, and its criterion "close to zero" is also met by units present in the subcatchment.**

| Field | Content |
|---|---|
| Check | P3, P10, P9, P32 |
| Location | p. 14, l. 410 to 418; p. 13, l. 403 to 406; p. 10, l. 299 to 300; Figure 12 (p. 33); Figure 13 (p. 34) |
| Quotation | "Only the Zermatt - Saas Fee sediment unit does not have outcrops in the Gorner-Grenz subcatchment" and "the overall pattern confirms that the inversion respects geological boundaries when the XRD fingerprints provide sufficiently distinct signals" |
| Concern | (1) One of seven units serves as negative control (1/7 = 14.3 %), so the test has a single chance to fail. (2) That unit is named in the synthetic tests as a small unit that may be "under-represented in the mixing process" (l. 299 to 300), so a near-zero rate is expected even without discriminating power. (3) Measured KDE modes (instance AB): ZSF sediments 0.00, Furgg series 0.00, Monte Rosa granite 0.01 (second maximum 0.46), ZSF serpentinites 0.03, Stockhorn-Tuftgrat-Gornergrat 0.07, ZSF metabasites 0.29, Monte Rosa gneiss 0.60 mm/y. The Furgg series and the Monte Rosa granite, both inside the subcatchment according to Figure 12 and the inset of Figure 13, also peak at zero (page image 34). "Close to zero" therefore does not separate an absent from a present unit. (4) Because all pixels of a unit share one fingerprint, the test checks unit totals and cannot show that erosion is placed inside the subcatchment boundary, yet the conclusion speaks of respecting geological boundaries. (5) "Close to zero" and "some spillover" are not quantified; for the number of samples see GB-20. The manuscript names laboratory known mixtures as the usual test (l. 404 to 406) but does not perform one. Research question 2 is one of three natural-data aims, hence major. |
| Suggestion | Counter-design: (a) laboratory known mixtures of the source powders in predefined proportions, measured by XRD and inverted, with recovered against true proportions reported (Collins et al., 2020, already cited, can be cited in l. 404 to 406 for the procedure); (b) several subcatchment samples chosen so that different units are absent; (c) a quantitative criterion, e.g. the share of modelled flux assigned to absent units against their area share and against present units of similar size, with spread across inversions; (d) the share of modelled flux originating outside the subcatchment boundary. |
| Status | verified (one absent unit; KDE modes measured by instance AB and seen on page image 34); inferred (consequence for the discriminating power) |
| Severity | major |
| Source | AB, SD |

**GB-41 The zircon and XRD comparison is confounded: three of seven units lack usable zircon fingerprints, one fingerprint is copied, and the comparison rests on one sample.**

| Field | Content |
|---|---|
| Check | P9 |
| Location | p. 14, l. 420 to 421 and l. 430 to 440; p. 15, l. 441 to 442; Figure 14 (p. 35) |
| Quotation | "no zircon grains were recovered from the Zermatt-Saas Fee (ZSF) ophiolites (metabasites and eclogites), and no age data were available for the Monte Rosa garnet-gneiss (MR g-g) unit" and "Compared to the zircon-only results, the XRD-based posterior shows greater stability." |
| Concern | The manuscript discloses the missing data (l. 430 to 434); its effect on the comparison is not drawn to the end. With no zircon fingerprint for the ZSF metabasites, a copied fingerprint for MR g-g (identical to the Monte Rosa granite, largest difference 0.004 across the 13 bins of Figure 14, instance AB), and "only very low concentrations of zircons" in the ZSF serpentinites, 3 of 7 units (42.9 %) are poorly or not constrained by zircon. Instability and higher uncertainty of the zircon inversion are thus expected from missing information, not from the method, and "the XRD-based posterior shows greater stability" mixes method and data availability. The comparison rests on one detrital sample without replicate (GB-20) and uses the same σd for both data types (GB-02). Research question 3 depends on this comparison, hence major. |
| Suggestion | Counter-design: compare XRD and zircon on the subset of units that have both fingerprints (merge or drop the others in both runs), on several detrital samples, and on synthetic data with the zircon availability pattern imposed on XRD. |
| Status | verified (missing fingerprints, single sample, wording); inferred (confounding) |
| Severity | major |
| Source | SD |

**GB-42 How the units without measured zircon ages enter the zircon and combined tracer matrices is not stated, and Figures 14 and 16 show the copied fingerprint without marking it.**

| Field | Content |
|---|---|
| Check | P23, P37 |
| Location | p. 14, l. 430 to 434; Figure 14 (p. 35) source fingerprint panel; Figure 16 (p. 37) age bins |
| Quotation | "To compensate for the lack of age data for the MR g-g unit, we assigned the MR g-g unit the same zircon-age fingerprint as the Monte Rosa granite unit." |
| Concern | Balance of source units: 7; without zircon data 2; with a stated compensation 1 (MR g-g); the ZSF metabasites and eclogites unit is not accounted for. Possible resolutions: (A) a zero zircon fingerprint, so its erosion only dilutes the zircon signal; (B) removal from the zircon inversion, its pixels not inverted; (C) another unit's fingerprint, as for MR g-g. Each gives a different posterior in the southwest and centre of the domain. The fingerprint bars of Figure 14 show no ZSF metabasites segment and no ZSF serpentinites segment in any of the 13 age bins (instance AB), which fits (A) or (B), but Figure 14 has no legend. In Figures 14 and 16 the MR gneiss bars appear beside the MR granite bars as an independent signature, and the captions ("the source fingerprints") do not say that one is a copy. The same question carries over to the combined inversion. |
| Suggestion | State in l. 430 to 434 how the ZSF metabasites and eclogites unit enters the zircon and the combined matrices; add a legend to the fingerprint panel of Figure 14; add to the captions of Figures 14 and 16 that the MR gneiss zircon fingerprint is copied from the MR granite and that no zircons were recovered from the ZSF metabasites, and mark the copied bars (e.g. by hatching). |
| Status | verified (text; absence of the segments in Figure 14 measured by instance AB; captions on page images 35 and 37); inferred (colour assignment from the legends of Figures 15 and 16) |
| Severity | moderate |
| Source | S3, SD |

**GB-43 The three natural-data inversions are not reported with the same metrics: the Jensen-Shannon distance, resolution and misfits are missing for some or all runs.**

| Field | Content |
|---|---|
| Check | P11 |
| Location | p. 14, l. 435 to 436; p. 15, l. 441 to 442 and l. 446 to 449; p. 8, l. 240 to p. 9, l. 244; p. 10, l. 284 to 285 |
| Quotation | "Furthermore, one must evaluate the data- and model misfit (eq. 7)." and "the average Jensen-Shannon distance between source fingerprints increases from 0.48 to 0.57, indicating improved distinguishability" |
| Concern | Matrix of runs (zircon only, XRD only, combined) against reported quantities: normalised uncertainty 0.87, 0.82, 0.86 (complete); average JS distance 0.48, missing, 0.57; resolution "low resolution" in words only, not described, not described; data and model misfit missing in all three; maximum erosion rate above 8000 mm/y, not stated in the text, not stated in the text; no accuracy metric in any run. The JS distance is introduced in Section 4.1.3 as the measure of distinguishability, and the synthetic results tie the error growth to JS below 0.55 (l. 352); without the XRD-only value the reader cannot place the XRD solution on that scale or judge whether 0.57 is an improvement over XRD alone (GB-44). The misfits are announced as a required evaluation (l. 240) but are reported for no natural inversion. |
| Suggestion | Add to Section 4.2.2 a table with one row per run (zircon, XRD, combined) and columns for average JS distance, normalised posterior uncertainty, mean resolution diagonal, data misfit, model misfit, maximum posterior erosion rate and number of iterations; state that accuracy cannot be assessed for natural data without a reference, or name the reference used. |
| Status | verified (presence and absence of values in l. 435 to 449 and on the figure labels of page images 35 to 37) |
| Severity | moderate |
| Source | S3 |

**GB-44 The claim that combining zircon and XRD data improves the posterior holds only against the zircon-only run; against the XRD-only run the reported normalised uncertainty is higher, and "stability" and "accuracy" are not measured.**

| Field | Content |
|---|---|
| Check | P21, P15, P3, P10, P31, P6 |
| Location | p. 15, l. 446 to 449; p. 14, l. 439 to p. 15, l. 442; p. 3, l. 72 to 73; p. 5, l. 139 to 140; p. 10, l. 284 to 285; p. 15, l. 461 to 463; Figures 14 to 16 (p. 35 to 37) |
| Quotation | "Adding XRD data to the zircon dataset stabilizes the inversion and improves the posterior solution." and "showing that integrating XRD with zircon data improves the stability and sharpness of the posterior solution" and "combining XRD data with other fingerprint data such as zircon data, proves to further stabilize and improve the posterior solution" |
| Concern | Text and figure labels report all three values consistently (PP-43), which makes the comparison possible. Case 1, reference zircon only: 0.86 minus 0.87 = minus 0.01 (minus 1.1 %), supported but small. Case 2, reference XRD only: 0.86 minus 0.82 = plus 0.04 (plus 4.9 %), i.e. the combination is less certain than XRD alone. l. 72 to 73 and l. 461 to 463, with XRD as the base and zircon as "other fingerprint data", read as improvements over the XRD solution, which the reported metric does not show; the top of the erosion colour bar is 12 mm/y for the combined map against 8 mm/y for XRD only. Under the linearised posterior covariance of eq. 20, adding data rows adds a positive semidefinite term to the inverse, so at the same linearisation point the trace cannot increase; a numerical check with 500 random configurations (21 XRD plus 13 zircon rows, σd = 0.01; instance S3) gave no case in which the combined ratio exceeded the XRD-only one. The higher combined value must come from another linearisation point, from the scaling of the concatenated data, or from another number of iterations, which the text does not discuss. Further: the JS distance of XRD alone is not reported (GB-43); "stability" (l. 73, 285, 439, 446, 462) and "sharpness" (l. 73) have no defined metric; "accuracy" (l. 285) cannot be measured for natural data without a reference; the three runs use one detrital sample, which does not carry the verb "proves". Research question 3 (l. 284 to 285) is one of three natural-data aims, hence major. |
| Suggestion | In Section 4.2.2 report the combined result against both single-data baselines, state that its normalised uncertainty (0.86) exceeds that of the XRD-only run (0.82) and explain why; report the JS distance of XRD alone; define stability operationally (e.g. coefficient of variation of pixel rates across bootstrap resamples of the detrital data and across several detrital samples) for all three runs; for accuracy, run the three configurations on synthetic data with realistic noise for both data types; rephrase l. 72 to 73, l. 139 to 140, l. 284 to 285 and l. 461 to 463 so that the improvement is attributed to the zircon baseline only (e.g. "adding XRD data to zircon data improved the zircon-only solution"), and remove the comma before "proves". |
| Status | verified (values in text and on the figure labels of page images 35 to 37; wording); inferred (direction reversal, percentages, eq. 20 argument and numerical check) |
| Severity | major |
| Source | S3, S4, AB, SD |

**GB-45 The hatched "low-confidence" areas are defined nowhere, and in Figures 15 and 16 they cover the main erosion peak that the text reports as the result of the XRD inversion.**

| Field | Content |
|---|---|
| Check | P29 |
| Location | Figure 5 (p. 26) panel (b); Figure 6 (p. 27) panel (b); Figures 14 to 16 (p. 35 to 37) erosion maps and hatch legend; p. 14, l. 440 to p. 15, l. 441 |
| Quotation | "the XRD solution identifies the main erosion peak in the center of the domain and a secondary peak in the Monte Rosa granite area" |
| Concern | Neither the captions nor the text say how low confidence is determined (text search for "confiden" and "hatch": 0 hits). In Figure 15 the central cells of the peak are hatched and their colour is hidden; only cells at the edge of the hatching are visible (instance AB at 300 dpi; seen on page image 36 during merging); in Figure 16 the centre of the peak block is hatched as well. The peak that l. 440 presents as the main result is thus flagged by the figure itself as low confidence, and its value cannot be read. The hatch legend of Figures 14 to 16 reads "Low-con dence area" (missing "fi" ligature). Because the main result of the XRD run lies in these cells, the finding is graded major. |
| Suggestion | Define the criterion for low confidence in Section 3.3 and in the captions; draw the hatching so that the cell colour stays visible (outline or transparent hatch); discuss in Section 4.2.2 that the main XRD peak lies in such cells; write "Low-confidence area" in the legends. |
| Status | verified (overlap on page image 36; absence of a definition); inferred (consequence for l. 440), asked |
| Severity | major |
| Source | AB, SD |

**GB-46 The lithology legends are drawn opaque while bars and map colours are semi-transparent, so colours match the wrong legend entries.**

| Field | Content |
|---|---|
| Check | P3 |
| Location | Figure 5 (p. 26) panels (j), (k); Figure 15 (p. 36) and Figure 16 (p. 37) legends and fingerprint bars |
| Quotation | "S.,T.,G." and "MR gneiss, mica" and "MR granite" |
| Concern | Measured legend swatches in Figure 15 (instance AB): S.,T.,G. #fc5404, MR gneiss #fc7c44, MR granite #fc9c9c, ZSF metabasites #34a42c, Furgg #bcdc6c; bar colours #fc844c, #fca47c, #fcbcbc, #74bc6c, #cce494, i.e. the swatches blended with white at an opacity of about 0.72. Compared directly (sum of RGB differences), the S.,T.,G. bar colour lies 16 from the "MR gneiss, mica" swatch and 120 from its own, and the MR gneiss bar colour lies 40 from the "MR granite" swatch and 96 from its own. A reader matching colours assigns these two units wrongly. Figure 5 behaves the same. |
| Suggestion | Draw the legend swatches with the same opacity as the bars and maps. |
| Status | verified (colour measurement) |
| Severity | minor |
| Source | AB |

**GB-47 Figure 6 lacks the axis titles, the axis multiplier and the hatch label that Figure 5 has.**

| Field | Content |
|---|---|
| Check | P29 |
| Location | Figure 6 (p. 27) panels (b), (g), (h), (i) |
| Quotation | "Low-confidence areas" and "Data misfit" |
| Concern | Figure 5 shows the axis titles "Iteration" and "Data misfit", the multiplier "1e8" and the hatch label "Low-confidence areas". In Figure 6, panels (g) and (h) have no x-axis title, panel (i) has no x-axis title, no multiplier for the data misfit (ticks 0.0 to 2.0) and no colour bar title, and the hatch swatch below panel (b) has no text. Read alone, the data misfit of Figure 6i appears 10⁸ times smaller than in Figure 5i. |
| Suggestion | Add the missing titles, the multiplier and the legend text in Figure 6. |
| Status | verified |
| Severity | minor |
| Source | AB |

**GB-48 The x-axes of the two left scatterplots of Figure 9 are labelled as JS distance but show the number of tracers.**

| Field | Content |
|---|---|
| Check | P29 |
| Location | Figure 9 (p. 30) left and middle scatterplots, x-axis titles, left y-axis title and colour bar |
| Quotation | "Avg. JS distance between lithologies" and "Number of tracrs" |
| Concern | The tick labels run from 0.0 to 20.0, and the 21 markers lie at 1.02 to 21.0 (instance AB, 24.3 px per unit), i.e. at the tracer counts 1 to 21 that l. 358 names; the axis title was carried over from Figure 8. A second, stray summation sign stands below the y-axis title of the left plot, and the colour bar title reads "Number of tracrs". |
| Suggestion | Retitle both x-axes "Number of tracer minerals", remove the stray symbol, and write "Number of tracers" on the colour bar. |
| Status | verified |
| Severity | minor |
| Source | AB |

**GB-49 The text of Figure 10 is set at 3.3 to 3.7 pt in print size, and the colour bar labels of Figures 14 to 16 at 5.0 to 5.3 pt.**

| Field | Content |
|---|---|
| Check | P29 |
| Location | Figure 10 (p. 31) all panels; Figures 14 to 16 (p. 35 to 37) colour bars |
| Quotation | "250" and "0.040" and "1e6" |
| Concern | Height of digits at 300 dpi (instance AB): tick labels of Figure 10 10 to 11 px, i.e. 3.3 to 3.7 pt (229 digit labels, median 3.7 pt); colour bar labels of Figures 14 to 16 15 to 16 px, i.e. 5.0 to 5.3 pt. The measuring procedure deviates by at most 0.6 pt, so both stay below 6 pt (PP-19). |
| Suggestion | Re-export Figure 10 at full page width with axis text of at least 7 pt (e.g. split into two figures), and enlarge the colour bar labels of Figures 14 to 16. |
| Status | verified |
| Severity | minor |
| Source | AB |

**GB-50 Figure 11 has no value axis and no column labels.**

| Field | Content |
|---|---|
| Check | P29 |
| Location | Figure 11 (p. 32) |
| Quotation | "From left to right: ZSF ophiolites (serpentinites), ZSF sediments, Stockhorn-Turftgrat-Gornergrat" |
| Concern | The seven columns are identified only by the order in the caption and by colour; the bars have no scale, so the reader cannot read the normalisation from 0 to 1 of l. 261 to 262 off the figure (measured column maxima 243 to 245 px confirm it, GB-39). |
| Suggestion | Add column headers and a scale from 0 to 1 under each column. |
| Status | verified |
| Severity | minor |
| Source | AB |

**GB-51 Figure 12 does not delimit the subcatchment it is about and does not explain why some units are drawn faded.**

| Field | Content |
|---|---|
| Check | P29 |
| Location | Figure 12 (p. 33) and caption; p. 14, l. 411 to 412 |
| Quotation | "Lithology and outcrops in the Gorner-Grenz confluence subcatchment." |
| Concern | The map shows the whole catchment. The eastern Monte Rosa granite is drawn in the legend colour, the central granite area faded; the fading is not explained, and the boundary drawn as a dashed line in the inset of Figure 13 is missing. Counting map pixels within a colour difference of 30 of the opaque legend colours (instance AB) gives 207,667 for Monte Rosa granite, 20,351 for Furgg, 8,063 for S.,T.,G. and 8,014 for MR gneiss, but only 83 for ZSF metabasites and 31 for their outcrops. Does the subcatchment contain ZSF metabasites, as the caption implies? |
| Suggestion | Draw the subcatchment boundary, explain the faded rendering in the caption, and list the units with outcrops inside it. |
| Status | verified (missing boundary; pixel counts); assumption (whether ZSF metabasites lie inside, because of hillshade blending), asked |
| Severity | minor |
| Source | AB |

**GB-52 The upper panel of Figure 13 has no density scale, although the caption reads peak heights as consistency.**

| Field | Content |
|---|---|
| Check | P29 |
| Location | Figure 13 (p. 34) upper panel and caption |
| Quotation | "a taller peak indicates greater consistency across inversions" |
| Concern | The ridgeline panel has the axis title "Density" but no tick values; only the separate lower panel (ZSF sediments) has a scale from 0 to 2 (page image 34). Peak heights of the seven units cannot be compared with each other or with the lower panel; the Furgg curve also rises into the band of the unit above. |
| Suggestion | Add a common density scale (or state that all ridges share the scale of the lower panel) and draw the ZSF sediments on the same scale. |
| Status | verified |
| Severity | minor |
| Source | AB |

**GB-53 The source fingerprints in Figure 15 cannot be derived from Figure 11 under the stated normalisation; a different weight per lithology is needed.**

| Field | Content |
|---|---|
| Check | P3 |
| Location | Figure 15 (p. 36) fingerprint bars; Figure 11 (p. 32); p. 9, l. 260 to 262 |
| Quotation | "At the end, these are normalized within each sample by dividing by the maximum observed peak area, yielding relative mineral concentrations on a scale from 0 to 1" and "Normalised abundance per mineral or age" |
| Concern | If Figure 15 shows the matrix of Figure 11 normalised per mineral, the segment share of unit j in mineral i must equal the bar length of unit j divided by the sum over units. Measured segment shares (instance AB, 21 bars) deviate from this prediction by up to 0.21 (median of per-mineral maxima 0.13); normalising each unit by its column sum gives up to 0.17. A free weight per unit fits (median deviation 0.026, maximum 0.048 without magnesite), with weights relative to the ZSF serpentinites of 0.66 (ZSF sediments), 0.35 (S.,T.,G.), 0.97 (MR granite), 0.31 (ZSF metabasites), 1.36 (MR gneiss) and 0.92 (Furgg). In the forward model (eq. 1) a column scale changes the erosion rate attributed to that unit, so the reader cannot tell which matrix entered the natural-data inversions. |
| Suggestion | State in the captions of Figures 15 and 16 how the bars are normalised and confirm that the matrix A of Section 4.2.2 is the one in Figure 11; if a per-unit weighting (e.g. by area or sample number) was applied, describe it in Section 3.4. |
| Status | inferred (fit to measured bar lengths) |
| Severity | moderate |
| Source | AB |

**GB-54 Legend labels are clipped or overlap swatches in Figures 15 and 16.**

| Field | Content |
|---|---|
| Check | P3 |
| Location | Figure 15 (p. 36) legend; Figure 16 (p. 37) legend |
| Quotation | "ZSF serpentinites" and "ZSF metabasites" |
| Concern | In Figure 16 the top legend row is cut off at the top; in Figures 15 and 16 the label "ZSF serpentinites" runs into the swatch of "ZSF metabasites" (instance AB; seen on page image 36). |
| Suggestion | Re-export the legends with sufficient margin and column spacing. |
| Status | verified |
| Severity | minor |
| Source | AB |

#### Minor corrections

| ID | Location | Quotation | Replacement | Source |
|---|---|---|---|---|
| KK-10 | p. 10, l. 306 to p. 11, l. 307 | "The posterior covariance follows a similar trend: it rises steeply in early iterations" | "The normalised posterior covariance follows the opposite trend: it rises steeply in early iterations" | SD |
| KK-11 | p. 11, l. 319 | "(Figure 6D, 6E and 6F )" | "(Figure 6D, 6E and 6F)" | ZF |
| KK-12 | Figure 10 (p. 31) first row, middle panel, x-axis title | "Smooting distance (m)" | "Smoothing distance (m)" | AB |
| KK-13 | Figure 10 (p. 31) fifth row, right panel, annotation | "n_m = 25" | "nₘ = 25" with subscript m, as in the caption | AB |
| KK-14 | Figure 14 (p. 35) caption and y-axis; Figure 16 (p. 37) panel title | "using Zr fingerprint data", "Normalised abundance per Zr age bin" and "combined XRD and Zr data" | "using zircon fingerprint data", "Normalised abundance per zircon age bin" and "combined XRD and zircon data" | S2 |

#### Verification log

| ID | Check | Checked | Values | Result |
|---|---|---|---|---|
| PP-24 | P36 | Statements of the form "approximately", "several", "many" against the records | "After several iterations" (l. 290) against 100 iterations (l. 293): vague, not contradictory; "7 tracers ... approximately the same" (l. 360) against Figure 9: error flat from 7 tracers on; "many of these cases" (l. 353) against Figure 8 | GB-31; others consistent, no finding |
| PP-25 | P38 | Hyperparameter names, symbols and method abbreviations | L, σm, σd, µ, nm in l. 293 to 295, 324 to 326, 367 to 370, 426 to 428 and in the Figure 10 caption; QN and SD defined in l. 211, JS in l. 345, PCA in l. 355 to 356, MAP in l. 173, KDE in the Figure 13 caption, all used consistently after definition | no finding |
| PP-26 | P1 | Pixel size implied by two statements of the smoothing distance | 1200 m / 4 = 300 m (l. 294, 325, 427); 3000 m / 10 = 300 m (l. 373) | no finding; pixel size not stated (GB-32) |
| PP-27 | P2 | Synthetic parameter set across tests | L = 1200 m, σm = 3, σd = 0.01 mm/y, prior equal to the average true erosion rate in l. 294 to 295, 324 to 326 and 426 to 428; µ = 0.1 in l. 326, 385, 428; iterations 100 (l. 293) and 25 (l. 324, 426) | no finding within the text; against Figure 10 in GB-34 |
| PP-28 | P3 | Figure 5e against l. 301 and iteration count of l. 293 | Hotspot cells median 1.6 (1.06 to 2.64), eastern area median 6.7 (6.0 to 8.8); panels (g), (h), (i) end at 100 iterations | no finding |
| PP-29 | P30, P7 | Reported errors and corrections; method version per reported run | No error with correction date reported; one method change (gradient normalisation of SD after initial experiments, l. 312) without date; QN for Figure 5 and all later runs (l. 320); SD normalised for Figure 6; base values of the sweeps not stated | no separate finding; treated in GB-14 and GB-34 |
| PP-30 | P3 | Figure 6g against Figure 5g at equal iteration numbers | SD 330.7 (iteration 25), 211.3 (100), 194.1 (150), 193.0 (200); QN 197.3 (20.2), 201.0 (100) | QN converges faster, as l. 315 says; accuracy in GB-27 |
| PP-31 | P11 | Degradation scenarios announced against reported | Announced 3 (l. 323); reported 3 (Figures 7, 8, 9), each with absolute error, posterior uncertainty and misfit trade-off | no finding for coverage; scale in GB-33 |
| PP-32 | P3 | Same baseline configuration across Figures 7 to 10 | Summed error: Figure 7 same map 197.4; Figure 9 7 to 21 tracers 197.4; Figure 10 row 3 197.42; row 4 at µ = 0.100 197.5; row 5 at 24.9 iterations 197.6; row 1 at 1232 m 195.0. Normalised uncertainty: Figure 7 0.74015; Figure 8 unblended 0.7401 to 0.7403; Figure 10 row 3 0.74015 | consistent within measurement uncertainty; no finding |
| PP-33 | P2 | Scenario 1 misfits against l. 341 to 342 | Data misfit about 3.254e6, 3.490e6, 3.687e6; model misfit about 1.563, 1.921, 2.461 (Figure 7) | no finding; both rise with mismatch as stated |
| PP-34 | P1, P2 | Pairs for the average JS distance; JS values in Figure 8 against thresholds | 7 units, 7 · 6 / 2 = 21 pairs ("all pairs", l. 347); labels 0.225, 0.441 and 0.624; text thresholds 0.55 and 0.44 (l. 352 to 353) | no finding |
| PP-35 | P1, P3 | Scenario 3 threshold of 7 tracers against Figure 9 | Summed error (S3; AB): 1 tracer 347.0; 347.2, 2: 347.9; 348.4, 3: 293.3; 293.6, 4: 296.3; 296.6, 5: 223.9; 224.3, 6: 205.0; 205.4, 7 to 21: 197.2; 197.4; uncertainty 0.961 at 1 tracer to 0.740 from 7 tracers | statements in l. 360 to 361 supported; no finding (axis label in GB-48) |
| PP-36 | P11 | Parameter sweeps announced against reported | Announced 5 (l. 367 to 370: σm, L, σd, µ, nm); Figure 10 rows 5; text paragraphs l. 372 to 389: 5 | no finding for coverage; content in GB-34 to GB-37 |
| PP-37 | P3 | Figure 10 row 4 against l. 385 | Step sizes 0.010 to 0.316 (10 values); summed error 328.3, 308.0, 283.3, 254.6, 225.1, 203.8, 197.5, 199.0, 200.8, 201.3; minimum at µ = 0.100 | minimum at 0.1 as stated; no finding |
| PP-38 | P20 | Basis of the iteration statements | "Beyond 115 iterations" (l. 388) within the tested range 0 to 200 of Figure 10, row 5; first QN test uses 100 iterations | no finding; iteration rule in GB-37 |
| PP-39 | P1, P2, P38 | Tracer mineral names and counts in text and figures | List l. 394 to 396: 21 names (Python count); l. 393 "21 minerals", l. 397 "21 target minerals", l. 358 "between 1 and 21 tracers"; Figure 9 "All tracers (21)"; Figure 11 21 rows; Figures 15 and 16 21 bars; set comparison 20 of 21 names identical; Figure 11 columns in caption order, maxima 243 to 245 px | no finding beyond GB-38; normalisation to the maximum per sample confirmed |
| PP-40 | P38 | Name of the subcatchment and of the glacier outline | "Gorner-Grenzgletscher confluence" (l. 406, Figure 12 label), "Gorner-Grenz subcatchment" (l. 411), "Gorner-Grenz confluence subcatchment" (Figure 12 caption), "Gorner-Grenz samples" and "Gorner-Grenz catchment" (Figure 13): one object, one root name; "Gorner glacier" in legends marks the glacier outline, another object | no finding |
| PP-41 | P24 | Dated events in figures | No figure has a time axis or shows dated events; the sample of 28 June 2019, 13:30 (l. 423 to 424) appears in no figure; x-axes of Figures 5, 6 and 10 count iterations | P24 not applicable; no finding |
| PP-42 | P3 | Figure 14 against l. 430 to 436 | MR gneiss and MR granite segments equal in all 13 age bins (largest difference 0.004); no ZSF serpentinites or ZSF metabasites segment in any bin; colour bar top 8623 ± 29 mm/y; printed total normalised posterior uncertainty 0.87 | assignment of the MR granite fingerprint, missing zircon data and values above 8000 mm/y as stated; no finding |
| PP-43 | P2, P3 | Normalised uncertainty of the natural runs, text against figure labels | Zircon 0.87 (l. 436; Figure 14), XRD 0.82 (l. 442; Figure 15), combined 0.86 (l. 447; Figure 16); XRD minus zircon = minus 0.05, combined minus zircon = minus 0.01 ("decreases slightly", l. 447) | no finding for the values; interpretation in GB-44 |
| PP-44 | P23 | Tracer count of the combined inversion | 21 XRD minerals plus 13 zircon age bins (Figure 14: 40 to 140 up to 750 to 800 Ma) = 34; Figure 16 shows 34 bars; 13 age bins with identical labels in Figures 14 and 16 | no finding |

### Segment 4: Discussion, Conclusions, references, declarations (p. 15 to 21)

#### Substantive findings

**GB-55 The Discussion says the method was "validated", while the natural-data results use "supports" and rest on one subcatchment and one detrital sample.**

| Field | Content |
|---|---|
| Check | P15 |
| Location | p. 15, l. 451; p. 1, l. 8; p. 13, l. 399 to 401; p. 14, l. 413 to 418 and l. 420 to 449 |
| Quotation | "We explained and validated the use of binned XRD peak-area data as mineralogical fingerprints within a non-linear inversion scheme to infer erosion rate maps." |
| Concern | The natural-data sections choose weaker verbs: "supporting the 1) the robustness of the cleaning and binning approach" (l. 400) and "This natural case study supports the reliability of our XRD fingerprinting approach" (l. 417). The natural known-mixture test checks one unit without outcrops and notes "Some spillover occurs from adjacent lithologies" (l. 414 to 415), and the zircon comparison has no reference map against which a solution could be validated (GB-39, GB-40, GB-41). The synthetic tests validate the recovery of a known map. "Validated" in l. 451 and "further validates the practical utility and robustness" in l. 8 are therefore stronger than the natural-data evidence; the main statement stands, hence moderate. |
| Suggestion | Rephrase l. 451, e.g. "We explained the use ... and validated it with synthetic tests; tests with natural data support it.", and l. 8 accordingly. |
| Status | verified |
| Severity | moderate |
| Source | S4 |

**GB-56 Two statements in the Discussion that feed the recommendations rest on effects that were not tested or that the results contradict.**

| Field | Content |
|---|---|
| Check | P15, P31 |
| Location | p. 15, l. 458 and l. 460 to 461; p. 16, l. 484 to 485; p. 12, l. 360 and l. 364 to 365; Figure 9 (p. 30) |
| Quotation | "Including a broad set of tracer minerals further improves model stability and resolution." and "A higher number of distinct source areas leads to higher posterior resolution and lower uncertainty." |
| Concern | (1) The degradation test reports that "The inversion with 7 tracers results in approximately the same posterior solution as with the full tracer set." (l. 360) and that reducing tracers "has a comparatively limited effect" provided the most informative ones are retained (l. 364 to 365). With 7 of 21 tracers (33.3 %) the solution is approximately unchanged, so the result supports a minimum number of informative tracers, not a further improvement by a broad set; Scenario 3 reports error, uncertainty and the misfit trade-off but not resolution, so "resolution" in l. 458 has no counterpart. Recommendation c), "multiple XRD tracers" (l. 465), agrees with the result; only l. 458 overstates it. (2) No synthetic test varies the number of source areas; all runs use the same seven units (Scenario 1 changes boundaries, not their number). The nearest results concern small units (l. 299 to 300) and boundaries (l. 302). "Our results suggest" in l. 484 nevertheless extends to "multiple mineralogically distinct source areas". Is the statement in l. 460 to 461 taken from De Doncker et al. (2020) or from tests not shown? |
| Suggestion | Rephrase l. 458, e.g. "A minimum number of informative tracer minerals (here about 7 of 21) is required; beyond that, additional tracers changed the posterior solution little.", and delete "and resolution" or add resolution values to Section 4.1.3; add a synthetic test with merged or split units (e.g. 3, 5, 7 and 10 source areas) reporting resolution and normalised uncertainty, or cite the source of l. 460 to 461 and remove "multiple ... source areas" from "Our results suggest" in l. 484 to 485. |
| Status | verified (no test varies the number of source areas; l. 360 and l. 364 to 365); inferred (7/21 = 33.3 %); assumption (origin of the statement in l. 460 to 461), asked |
| Severity | moderate |
| Source | S4, SD |

**GB-57 Butler et al. (2019), a study on pre-treatment of soil XRD data for cluster analysis, is cited for depth-integrated suspended sediment sampling against sorting effects and for shielding and peak-overlap corrections; its abstract does not cover these.**

| Field | Content |
|---|---|
| Check | P13 |
| Location | p. 15, l. 469 to 471; p. 15, l. 473 to p. 16, l. 474; p. 16, l. 475 to 476 |
| Quotation | "This can be diminished by powdering samples and using depth-integrated suspended sediment samples to average out sorting effects during transport (Butler et al., 2019)." |
| Concern | The Discussion names grain-size effects as a limitation of raw XRD data, which is appropriate; the mitigation rests on a single citation. According to its abstract (SLU research portal, read by instance S1), Butler et al. (2019) test peak alignment, binning, scaling and square-root transformation on 12 African soils measured by five operators (60 measurements) to improve cluster analysis. The abstract mentions neither suspended sediment, depth-integrated sampling, sorting during transport, shielding effects nor peak overlap. The full text could not be read. Where in Butler et al. (2019) is the recommendation on depth-integrated suspended sediment samples, and on which page are shielding effects and peak overlap treated? If it is not there, the mitigation has no source. |
| Suggestion | In l. 470 to 471 cite a source on depth-integrated suspended sediment sampling and grain-size sorting, or give the page in Butler et al. (2019); check the same for l. 474 and l. 476. |
| Status | verified (content of the abstract, read by instance S1); inferred (full text not readable) |
| Severity | moderate |
| Source | S1 |

**GB-58 The Conclusions do not take up the natural-data aims, the Bayesian framing of the Introduction or the stated error propagation.**

| Field | Content |
|---|---|
| Check | P15 |
| Location | p. 16, l. 477 to 489; p. 10, l. 281 to 285; p. 2, l. 55 to 57; p. 1, l. 6 to 7 |
| Quotation | "Using synthetic forward-inverse experiments, we show that the true erosion pattern can be reliably recovered, and that the method is robust across a range of parameters." |
| Concern | Section 4 announces three natural-data aims: alignment of XRD fingerprints with expected mineralogy, attribution of subcatchment samples only to present lithologies, and the effect of combining XRD with zircon (l. 282 to 285). Section 6 names only synthetic experiments; none of the three aims is answered there, and the Discussion takes up only the third. The Introduction positions the approach as "a hybrid between Bayesian linear mixed models and hierarchical Bayesian models" (l. 55 to 56), and the Abstract promises "quantifying posterior uncertainty and error propagation" (l. 6 to 7); Sections 5 and 6 return neither to the frequentist and Bayesian methods introduced in l. 43 to 57 nor to error propagation (see also GB-02). The reader cannot see from the Conclusions what the natural-data tests established or how the approach compares with the unmixing methods introduced. |
| Suggestion | Add to Section 6 one sentence per natural-data aim with its result (Figure 11, Figure 13, values 0.87, 0.82, 0.86) and to Section 5 a paragraph comparing the approach with the unmixing methods of l. 48 to 57, or delete "error propagation" from l. 7 if it is not shown. |
| Status | verified |
| Severity | moderate |
| Source | S4 |

**GB-59 The extension to land-use classes and to zircon data in the Conclusions is not qualified by the manuscript's own results.**

| Field | Content |
|---|---|
| Check | P15 |
| Location | p. 16, l. 487 to 489; p. 15, l. 464 to 466; p. 14, l. 435; p. 12, l. 351 to 354 and l. 363 to 364 |
| Quotation | "the approach is flexible and can be extended to alternative classifications such as land use or sub-catchments" and "can be applied to other types of tracer data, including zircon U-Pb age distributions or geochemical compositions" |
| Concern | The Discussion places the land-use proposal (l. 466) directly after recommendation b), "the source units show strong mineralogical contrasts" (l. 464 to 465), so there the condition is stated; instance SD therefore recorded no finding for it, and this finding is limited to the Conclusions. There the extension to land use (l. 487 to 488) carries no condition, although the manuscript's own results make fingerprint distinctiveness the strongest control (l. 363 to 364), with error and uncertainty rising sharply below an average JS distance of 0.55 (l. 351 to 354). Will land-use classes on the same lithology have distinguishable XRD fingerprints? For zircon, the own zircon-only run is "highly unstable, with extreme erosion rate values" (l. 435), which the Conclusions do not mention when listing zircon U-Pb age distributions as applicable tracer data (l. 488 to 489). |
| Suggestion | Add to l. 487 to 488 the condition "provided the source classes have sufficiently distinct fingerprints (average Jensen-Shannon distance above about 0.55 in our tests)", and to l. 489 that zircon data alone gave an unstable solution in this catchment (Section 4.2.2) because of missing source data. |
| Status | verified (own results and wording); assumption (fingerprint similarity of land-use classes), asked |
| Severity | moderate |
| Source | S4 |

#### Minor corrections

| ID | Location | Quotation | Replacement | Source |
|---|---|---|---|---|
| KK-15 | p. 15, l. 460 | "glaciated catchments" | "glacierized catchments", as in l. 16, l. 62 and l. 329 | S4 |
| KK-16 | p. 16, l. 480 | "identify the mineralogical contributions of different source areas" | "identify the contributions of different source areas" | S4 |
| KK-17 | p. 16, l. 491 | "All authors (FDD, FH, BB, TA)" | "All authors (F.D.D., F.H., B.B., T.A.)", the form used in l. 491 to 494 | S2, S4 |
| KK-18 | p. 17, l. 514; p. 19, l. 610 | "Chapter Ten - Nonlinear Inverse Problems" and "Chapter 9 - Nonlinear Inverse Problems" | one form in both entries, e.g. "Chapter 10: Nonlinear Inverse Problems" and "Chapter 9: Nonlinear Inverse Problems" | S4 |
| KK-19 | p. 17, l. 522 to 523 | "Master’s thesis, University of Lausanne, unpublished master’s thesis, 2021." | "Master’s thesis, University of Lausanne, 2021." | S4 |
| KK-20 | p. 17, l. 526 | "Reviews in mineralogy, Mineralogical society of America" | "Reviews in Mineralogy, Mineralogical Society of America" | S4 |
| KK-21 | p. 19, l. 578 | "[No title found]" | "Landscape indicators of human impacts to riverine systems" | S4 |
| KK-22 | p. 20, l. 612 to 613 | "Oxford University Press, New-York," | "Oxford University Press, New York, 1990." without page range; if specific pages are meant, give them at the citation in l. 265 | S4 |
| KK-23 | p. 20, l. 635 | "ISBN 9780898715729 9780898717921" | "ISBN 9780898715729" | S4 |
| KK-24 | p. 20, l. 639 | "Bomb-fallout137 Cs" | "Bomb-fallout ¹³⁷Cs" | S4 |

#### Verification log

| ID | Check | Checked | Values | Result |
|---|---|---|---|---|
| PP-45 | P16 | Language and typesetting of p. 15, l. 450 to p. 21, l. 653 at the page images; uniformity of the reference list | Sentences of l. 451 to 499 read at page images 15 and 16; reference list p. 17 to 21: author format "Surname, Initials" and "and" before the last author consistent, DOIs as https links consistent, article numbers with thin space consistent; wide spacing in the Grimshaw and Lewin entry (l. 584) is justification; the line break in the Steck et al. DOI (l. 632 to 633) falls on a hyphen that belongs to the DOI | KK-15 to KK-24; grammar in l. 454 to 455 and l. 461 to 462 in GB-11 and GB-44; no further finding |
| PP-46 | P15 | Frameworks and core terms of Introduction and aims in Sections 5 and 6 | Spatially informed inversion (l. 58 to 61) taken up in l. 454; posterior uncertainty metrics (l. 67, Section 3.3) in l. 483 to 484; non-linear inversion in l. 451 and l. 478; Bayesian hybrid framing (l. 55 to 57) and error propagation (l. 7) not taken up; cost and time efficiency (l. 3 to 4, l. 74 to 75) not taken up; natural-data aims 1 to 3 (l. 282 to 285): only aim 3 in Section 5 | GB-01, GB-58; no finding for the terms taken up |
| PP-47 | P15 | Each statement of Sections 5 and 6 mapped to a place in the results | l. 457 to 458 distinct signatures to l. 351 to 354 and l. 363 to 364; l. 459 to 460 spatial delineation to l. 336 to 342; l. 466 to 468 storage caution to the assumption in l. 23; l. 469 to 476 XRD limitations to citations with hedged verbs; l. 482 to 483 "reliably recovered" to l. 296 to 298; "robust across a range of parameters" to l. 371 to 389 with reported limits; l. 483 to 484 resolution and covariance to l. 299 to 304 | unsupported or overstated: GB-03, GB-11, GB-13, GB-44, GB-55, GB-56; all other statements have a place in the results, no finding for those |
| PP-48 | P15, P9 | Each proposal in the outlook held against own findings | a) well-constrained source lithology (l. 464) against Scenario 1: consistent, own site in GB-22; b) strong mineralogical contrasts (l. 464 to 465) against Scenario 2: consistent; c) multiple XRD tracers (l. 465) against Scenario 3: consistent; c) other fingerprint data combined (l. 465 to 466) against l. 442 and l. 447: GB-44; land use (l. 466) covered by b), (l. 487 to 488) in GB-59; storage caution against the assumption of l. 23: consistent; best applied with minimal storage, distinct source areas, prior spatial knowledge (l. 484 to 486): number of areas in GB-56; other tracers (l. 488 to 489): GB-59 | proposals a), b), c) with tracers and storage caution: no finding |
| PP-49 | P4 | In-text citations against the reference list in both directions; years, name spelling, "et al." | 64 distinct citation keys (160 occurrences, most of l. 10 to 75 doubled by the duplicate Introduction) against 64 entries; every key has an entry and every entry a citation; all years agree; works with more than two authors cited with "et al.", two-author works with "and" | malformed name "E." (GB-06) and wrong work behind "Kobe, 2021" (GB-08); otherwise no finding; DOIs not resolved (optional check) |

## Optional checks

| Area | What it needs | Responsible | Run |
|---|---|---|---|
| DOI resolution | one retrieval per reference entry with a DOI | `science-quellenapparat-pruefung` | no |
| Citation style | the name of the style or the style rules of the journal | `science-zitierstil-harvard-ctr` or the journal's style rules | no |
| AI statement against publisher policy | the target publisher's policy on AI use | this review, on request | no |
| Relation to the authors' own prior work | the authors' prior work as files or DOIs | this review, on request | no |
| Journal requirements | the author guidelines of the target journal | this review, on request | no |
| Factual correctness | access to the sources of the checked statements and a selection of sections | `science-faktenbeleg-pruefung`, `geo-frage-belegbasiert-klaeren` | no |

## Limits of this review

- Checked version: egusphere-2025-4695.pdf, 37 pages, SHA-256 9c80676054f96ecd6f00f4d2a8b5ba568e03c6949e3856d363ac1c4abb42e7bd.
- Sources not readable: Das et al. (2023), Haddadchi et al. (2013), Yang et al. (2025), Fathabadi and Jansen (2022), Klages and Hsieh (1975), the full texts of Butler et al. (2019) and Niu et al. (2020), the UNESDOC copy of the UNESCO 2009 report (GB-06) and the Zenodo record 10.5281/zenodo.17120374 (repository contents not checked). During merging the landing pages of Andrews and Eberl (2012) and Ehlers et al. (2015) could not be re-read (HTTP 429); GB-07 and GB-09 rest for these works on the abstracts read by instance S1.
- Findings with status assumption: 0 of 59 for the central statement; 9 of 59 (GB-10, GB-20, GB-22, GB-31, GB-38, GB-39, GB-51, GB-56, GB-59) carry a sub-statement with status assumption, each asked as a question.
- Optional checks run: 0 of 6.
- Omitted instances: none.
- Discarded findings: 0. All 89 instance findings had their mandatory fields, and none was rejected after checking at the manuscript. The 89 instance findings became 57 findings: 24 merged findings combine 56 instance findings (three instance findings were split across two or three findings by subject), and 33 come from one instance. 25 of the 51 instance minor corrections were absorbed into findings, the other 26 merged into 22 minor corrections; the 55 instance verification entries were merged into 47. Two findings (GB-15, GB-30) and two minor corrections (KK-02, KK-11) were raised during merging from hints outside the checklists that no instance had treated. The format check lists 191 pairs with overlapping locations; after merging, each was decided as a different subject (list in the working folder, `zf/paare_entscheidungen.txt`).
- Hints outside the checklists not raised as findings because they could not be confirmed: possible loose fit of citations judged only from entry titles (Walden et al., 1997; Olley et al., 1993; Wilson et al., 1993; Barker et al., 1997; Blaen et al., 2016), the missing financial support statement although l. 492 mentions funding, incomplete reference entries without publisher or series (Bearth, 1953; Gjems, 1967; Lafuente et al., 2015), the unit of σd against the dimensionless data of eq. 3, and the capital panel letters in text references against lower-case panel labels.
- Figure values rest on measurements by instances AB, S3 and SD; during merging they were spot-checked by eye on page images 24, 25, 31, 32, 34 and 36, not re-measured.
