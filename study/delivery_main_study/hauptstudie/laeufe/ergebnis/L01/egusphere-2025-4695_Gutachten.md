# Review report: From XRD signal to erosion rate maps

| Field | Value |
|---|---|
| Manuscript | De Doncker, F., Herman, F., Belotti, B. and Adatte, T. (2025) From XRD signal to erosion rate maps, EGUsphere preprint, https://doi.org/10.5194/egusphere-2025-4695 |
| Checked version | egusphere-2025-4695.pdf, 37 pages, SHA-256 9c80676054f96ecd6f00f4d2a8b5ba568e03c6949e3856d363ac1c4abb42e7bd |
| Date | 2026-10-17 |
| Language | English |
| Review instances | Segments 1 to 4 (S1 to S4), figures (AB), study design (SD); run sequentially in one context, not context-separated (nacheinander geprüft, nicht kontextgetrennt); no instance omitted |
| Note | The six review instances ran one after another in a single context, without separate agents. |

## Summary

The manuscript is a method development study. It inverts binned X-ray diffraction (XRD) peak areas of 21 minerals, measured on suspended sediment and on bedrock of seven lithological units, into a pixel-scale erosion rate map of the Gornergletscher catchment (Pennine Alps), using a Bayesian maximum a posteriori inversion with log-space erosion rates, a Gaussian smoothing prior (L = 1200 m, pixel size 300 m) and two update schemes (steepest descent and quasi-Newton). Posterior covariance, a resolution diagonal and a normalised posterior uncertainty serve as uncertainty metrics. Synthetic forward-inverse tests on one true map with a single erosion hotspot cover three degradation scenarios (map mismatch, blended fingerprints, tracer number) and five hyperparameter sweeps; the inversion fails for an average Jensen-Shannon distance below about 0.44 and needs at least 7 tracers. Natural tests compare the fingerprints with the known lithology, check whether samples from the Gorner-Grenz confluence are attributed only to units in that subcatchment, and compare and combine XRD with zircon U-Pb fingerprints of one sample (28 June 2019), with normalised posterior uncertainties of 0.87 (zircon), 0.82 (XRD) and 0.86 (combined).

## Strengths

1. The forward model, the misfit, its gradient, both update rules and the uncertainty metrics are written out step by step (Sect. 3.1 to 3.3), with consistent equation references (PP-29); this makes each step checkable, which is how the printed errors in Eq. 9, 12, 14 and 19 could be located (GB-09).
2. The synthetic tests vary map geometry, fingerprint distinctiveness, tracer number and five hyperparameters and report error, uncertainty and both misfits for every run; in the map and tracer scenarios the plotted values agree with the text, including the unexpected result for the slightly modified map (PP-16, PP-17).
3. The natural part adds a subcatchment exclusion test as a field analogue of a known-mixture experiment and a second, independent tracer; concatenating zircon and XRD matrices shows that the framework takes several tracer types in one inversion, and the reported summary values match the figure labels (PP-18, PP-21).
4. The scholarly apparatus is complete in both directions: all 64 short citations have an entry and all 16 figures are referenced in the text (PP-27, PP-28), and the inversion code and test data are deposited under a DOI (GB-32).

## Weaknesses

1. What the data can resolve is not separated from what the prior supplies: all pixels of a unit share one fingerprint, so the data fix at most seven unit contributions, and the plotted resolution values near 1 are incompatible with the definition of R (GB-07, GB-10, GB-09). The authors should state this limit in Sect. 3.2, give the formula of R, and report the natural results as unit erosion rates with uncertainties.
2. The XRD fingerprints themselves are not validated: per-sample normalisation by the maximum peak area biases the mixing model, several minerals carry identical values, and diagnostic minerals of garnet-bearing and eclogitic units are nearly absent (GB-13, GB-21, GB-12). A laboratory known-mixture experiment through the full processing chain and a table of 2θ windows would test the fingerprints directly.
3. The natural-data tests have no reference against which accuracy could be judged: the unit that should be absent is indistinguishable from present units, the zircon benchmark is confounded by missing and copied source data, and the combined inversion is more uncertain than XRD alone although the discussion claims a further improvement (GB-22, GB-24, GB-29). Several confluence samples whose subcatchments lack different units, and a zircon comparison restricted to units with own data, would give the needed contrast.
4. Several reported results disagree with the figures or lack the inputs needed to reproduce them: the data standard deviation sweep, the smoothing distance claim beyond 3000 m, the choice of quasi-Newton, the blending counts, missing inversion inputs and processing settings, a data statement limited to the tests, and a duplicated introduction (GB-20, GB-19, GB-16, GB-17, GB-25, GB-12, GB-32, GB-05). Each figure statement should be rechecked against the plotted values, and the inputs listed in Sect. 4.2.

## Findings by segment

### Segment 1: Abstract, introduction, state of research (p. 1 to 5)

#### Substantive findings

**GB-01 Cost- and time-effectiveness is claimed but not measured**

| Field | Content |
|---|---|
| Check | P33 |
| Location | p. 1, l. 3 to 4; p. 2, l. 40 to 42; p. 3, l. 74 to 75 |
| Quotation | "To conclude, we show and validate the potential of binned XRD peak-area data as a cost- and time-efficient approach for constructing erosion rate maps." |
| Concern | The abstract and the aims present cost- and time-effectiveness as a result ("we validate a time- and cost-effective fingerprinting approach", l. 3 to 4). No cost, analysis time or sample throughput is given for XRD or for the zircon method it is compared with, and Sect. 5 and 6 do not return to the claim. |
| Suggestion | Add cost and time per sample for XRD and U-Pb dating, with source, in Sect. 4.2.2, or remove the claim from l. 3 to 4 and l. 74 to 75. |
| Status | verified |
| Severity | moderate |
| Source | SD |

**GB-02 The propagated uncertainty covers data noise and prior only**

| Field | Content |
|---|---|
| Check | P26, P31 |
| Location | p. 1, l. 6 to 7; p. 6, l. 185 to p. 7, l. 187 (Eq. 8) |
| Quotation | "in order to invert detrital mineralogical data into erosion rate maps while quantifying posterior uncertainty and" |
| Concern | The data covariance Cd = σd² I, with one σd for all tracers, is the only data-side uncertainty. Variability of the fingerprints within a unit (the number of source samples is not given), uncertainty of the map inferred under ice, and uncertainty of the XRD processing are not propagated. The "error propagation" of the abstract therefore holds only on the path where fingerprints and map are exact. |
| Suggestion | State this scope in Sect. 3.3, or add a fingerprint variance term to Cd. |
| Status | verified |
| Severity | moderate |
| Source | SD |

**GB-03 Three cited sources do not support the statements they are cited for**

| Field | Content |
|---|---|
| Check | P13 |
| Location | p. 1, l. 19; p. 2, l. 28; p. 2, l. 31; p. 19, l. 597 |
| Quotation | "plant pollen content (Brown, 1985; Kobe, 2021)" |
| Concern | Kobe (2021), HTS Teologiese Studies 77, is a theology article ("Ubuntu as a spirituality of liberation for black theology of liberation"); its article page contains nothing on pollen, sediment or fingerprinting. Two further attributions do not match the titles in the reference list: Barker et al. (1997) concerns terrestrial photogrammetry of bank erosion but is cited for "sediment traps installed on dams" (l. 18 to 19), and Blaen et al. (2016) concerns real-time sensor monitoring of nutrients and dissolved organic matter but is cited for nutrients as a sediment fingerprint (l. 28). All three citations recur in the duplicated Sect. 2 (GB-05). |
| Suggestion | Replace Kobe (2021) at p. 2, l. 31 and p. 19, l. 597 by a pollen fingerprinting study or delete it; check Barker et al. (1997) and Blaen et al. (2016) against the statements at l. 18 to 19 and l. 28. |
| Status | verified (Kobe 2021, source read); inferred (Barker 1997, Blaen 2016, from the titles in the reference list) |
| Severity | moderate |
| Source | S1 |

**GB-04 Two works that bear on the contribution are missing**

| Field | Content |
|---|---|
| Check | P14 |
| Location | p. 3, l. 62 to 63 |
| Quotation | "particularly valuable in glacierized catchments, where ice cover limits direct observations and contributes to large uncertainties" |
| Concern | Ehlers, T. A., Szameitat, A., Enkelmann, E., Yanites, B. J. and Woodsworth, G. J. (2015) Identifying spatial variations in glacial catchment erosion with detrital thermochronology, Journal of Geophysical Research: Earth Surface, 120(6), pp. 1023 to 1039, https://doi.org/10.1002/2014JF003432, infer where erosion occurs beneath a glacier from detrital data, the aim named at l. 62 to 63. Madella, A., Glotzbach, C. and Ehlers, T. A. (2022) How many grains are needed for quantifying catchment erosion from tracer thermochronology?, Geochronology, 4, pp. 177 to 190, https://doi.org/10.5194/gchron-4-177-2022, show that detrital samples of about 100 grains often cannot separate erosion scenarios, which limits the zircon benchmark of Sect. 4.2.2, for which no grain counts are given. Neither work is in the reference list. |
| Suggestion | Cite Ehlers et al. (2015) at l. 62 to 63, and Madella et al. (2022) in Sect. 4.2.2 together with the number of dated zircon grains. |
| Status | verified |
| Severity | minor |
| Source | S1 |

**GB-05 Section 2 repeats Section 1 word for word**

| Field | Content |
|---|---|
| Check | P16, P4 |
| Location | p. 3, l. 76 to p. 5, l. 142 |
| Quotation | "2    Introduction" |
| Concern | Section 2 has the same heading as Section 1 and repeats it completely: 66 lines (l. 77 to 142 against l. 10 to 75) and 1153 words, identical word by word (difflib ratio 1.0). The repetition takes 66 of the 489 numbered lines of the main text (13.5 %) and shifts all later section numbers by one. |
| Suggestion | Delete p. 3, l. 76 to p. 5, l. 142 and renumber Sect. 3 to 6 as 2 to 5. |
| Status | verified |
| Severity | minor |
| Source | S4, S1 |

#### Minor corrections

| ID | Location | Quotation | Replacement | Source |
|---|---|---|---|---|
| KK-01 | p. 1, l. 5 | "Quasi-Newtonian" | "quasi-Newton" (as in l. 211) | S1 |
| KK-02 | p. 1, l. 11 to 12; p. 18, l. 567 | "E., 2009"; "E., W. D.: The Impact of global change" | "Walling, 2009"; "Walling, D. E.: The Impact of global change"; likewise the repetition at l. 78 to 79 | S4 |
| KK-03 | p. 2, l. 50 | "Generalist Likelihood Uncertainty Estimation" | "Generalised Likelihood Uncertainty Estimation"; likewise l. 117 | S4 |
| KK-04 | p. 2, l. 51 | "similar to the NNLS" | "similar to the NLLS"; likewise l. 118 | S4 |

#### Verification log

| ID | Check | Checked | Values | Result |
|---|---|---|---|---|
| PP-01 | P13 | statements with evaluations from sources in Sect. 1 | Kobe 2021 read (mismatch, GB-03); De Doncker et al. 2020 abstract read, supports "inversion framework" (l. 61); Gergel et al. 2002 record read, title "Landscape indicators of human impacts to riverine systems", fits l. 11; Das et al. 2023 for "remains underutilized" and "expensive and time-consuming" (l. 35 to 37) and Walling 2009 not readable | no finding beyond GB-03; unreadable sources listed under limits |
| PP-02 | P14 | searches for precursors of "binned XRD peak areas in a spatial non-linear inversion to erosion rate maps in a glacierized catchment" | five queries: XRD mineralogical fingerprinting of suspended sediment in glacier catchments; spatially explicit sediment unmixing into erosion maps; detrital zircon or thermochronology and spatial glacial erosion; two title queries (Ehlers et al. 2015, Sharman and Johnstone 2017). Candidates: Lipp et al. 2021 (already cited, dropped), Sharman and Johnstone 2017 (same field only), Ehlers et al. 2015, Madella et al. 2022 | two proposals, GB-04 |
| PP-03 | P28 | statements of the form "no study", "first", "not yet" | none; the gap statements at l. 36 to 37 and l. 58 to 59 are attributed to Das et al. (2023) and Niu et al. (2020) | no finding apart from the novelty claim (GB-27) |

### Segment 2: Methods, study area, figures 1 to 4 (p. 5 to 10, figures p. 22 to 25)

#### Substantive findings

**GB-06 Symbols of the forward model change between equations**

| Field | Content |
|---|---|
| Check | P38 |
| Location | p. 5, l. 154 to 155; p. 6, l. 161; p. 7, l. 208 to 209; p. 8, l. 215 to 219; p. 9, l. 262 to 263; p. 10, l. 295 |
| Quotation | "We can thereby derive the abundance of a given tracer t at pixel" |
| Concern | Eq. 1 to 4 index tracers by i and pixels by j (A_ij, d_i); l. 262 to 263 switch to t and xy. Eq. 17 counts iterations with k, Eq. 18 and 19 with n but keep εk inside the bracket. Eq. 3 is called a "dimensionless form" (l. 161), while d is scaled by the total erosion rate (Eq. 2) and σd is given in mm/y (l. 295). |
| Suggestion | Use i and j throughout (l. 262 to 263), one iteration index in Eq. 17 to 19, and state the unit of d after Eq. 2. |
| Status | verified |
| Severity | minor |
| Source | S2 |

**GB-07 The data constrain at most seven unit contributions; the pattern within a unit comes from the prior**

| Field | Content |
|---|---|
| Check | P31, P9 |
| Location | p. 6, l. 166 to 169; Fig. 2c; Fig. 5a |
| Quotation | "By using the spatial distribution of the source areas (geological map) (Figure 2C), we obtain an erosion rate map from the detrital data" |
| Concern | A_ij is the fingerprint of the unit that contains pixel j (Fig. 2c and Sect. 3.4), so all pixels of one unit have identical columns and rank(A) is at most 7 for 7 units (Python, 21 tracers and 818 pixels: rank 7). The data therefore fix at most seven unit sums; where inside a unit erosion is placed is decided by the prior mean and the Gaussian kernel of Eq. 9 with L. The synthetic true map is a single smooth bump (Fig. 5a, l. 288 to 289), the shape this kernel favours, and the error in Fig. 10 falls as L grows (GB-19). The manuscript discloses part of this (l. 297 to 298), but abstract and conclusions present pixel-scale "erosion rate maps". |
| Suggestion | State in Sect. 3.2 that the structure within a unit is set by the prior, and report the natural results as seven unit erosion rates with uncertainties. Counter-design: synthetic true maps that the prior does not favour (uniform rate per unit, a sharp hotspot inside one unit, two hotspots in one unit), evaluating recovered unit sums and within-unit patterns separately. |
| Status | inferred |
| Severity | major |
| Source | SD |

**GB-08 Pixel size and pixel number must be derived by the reader**

| Field | Content |
|---|---|
| Check | P22 |
| Location | p. 6, l. 170 to 172; p. 10, l. 294 |
| Quotation | "Our inverse problem is underdetermined: the number of tracers, representing the data we have, is smaller than the number" |
| Concern | The pixel size appears only implicitly: 1200 m / 4 = 300 m (l. 294) and 3000 m / 10 = 300 m (l. 373). The number of pixels n, which fixes the degree of underdetermination and the scale of the resolution trace, is not given; from the catchment area of Fig. 4 (about 73.6 km², estimated from the 1 km scale bar) it would be about 73.6 / 0.09 = 818. |
| Suggestion | State pixel size and n in Sect. 3.2 or 4. |
| Status | inferred |
| Severity | minor |
| Source | S3 |

**GB-09 Several printed equations cannot be implemented as written**

| Field | Content |
|---|---|
| Check | P8 |
| Location | p. 7, l. 189 (Eq. 9); p. 7, l. 197 (Eq. 12); p. 7, l. 201 (Eq. 14); p. 8, l. 219 (Eq. 19); p. 8, l. 225 (Eq. 20) |
| Quotation | "Cm (i, j) = σm 2 exp(" |
| Concern | Eq. 9 has a positive exponent, exp(s²/L²), so the covariance grows with distance and is not positive definite (Python, 50 random points at L = 1200 m: smallest eigenvalue −4.4e36). Eq. 12 writes the Jacobian as the vector A·exp(ε) instead of A·diag(exp(ε)). Eq. 14 lacks the transpose used in Eq. 16. Eq. 19 inverts GᵀCd⁻¹G alone; with rank(G) at most 7 this matrix of order n is singular (Python: rank 7 of 818), whereas Eq. 20 contains the term Cm⁻¹. |
| Suggestion | Write Eq. 9 with exp(−s²/L²), Eq. 12 as A·diag(exp(ε)), add the transpose in Eq. 14, and write the Hessian in Eq. 19 as GᵀCd⁻¹G + Cm⁻¹ or state how the code regularises it. |
| Status | verified (equations at the page image); inferred (singularity, from the rank bound) |
| Severity | moderate |
| Source | SD, S2 |

**GB-10 The plotted resolution values cannot be the diagonal of R as defined, and text and colour bars disagree**

| Field | Content |
|---|---|
| Check | P8, P3 |
| Location | p. 8, l. 230 to 236; Fig. 5d; Fig. 6d; Fig. 14, resolution diagonal; Fig. 15; p. 10, l. 299 to 300; p. 14, l. 436 |
| Quotation | "Where the diagonal of R is close to 1, data have improved our knowledge considerately relative to the prior." |
| Concern | No formula for R is given. For the usual R = I − C̃m Cm⁻¹ = C̃m GᵀCd⁻¹G the trace is at most rank(G), at most 7 (GB-07), so the mean diagonal over about 818 pixels (GB-08) is at most 7/818 = 0.0086 (Python: trace 7.00). Fig. 5d and 6d show 0.88 to 1.00 in every pixel, a trace of at least 0.88 × 818 = 720. In Fig. 14 the colour bar runs from 0.5 (light) to 1.0 (black) and the map is black except a few pixels, which by l. 235 to 236 means well resolved, yet the text reports "low resolution" (l. 436). The plotted quantity is probably something else, for instance C̃m Cm⁻¹, for which values near 1 mean that the data have not reduced the prior; read that way, l. 235 to 236, l. 299 to 300 and the use of resolution to "assess the reliability" (l. 483 to 484) are inverted. |
| Suggestion | Give the formula of R in Sect. 3.3, recompute Fig. 5d, 6d and 14 to 16 with it, state the pixel number and the trace of R, make l. 436 agree with Fig. 14, and correct "considerately" to "considerably" in l. 236. |
| Status | verified (colour scales and maps at the page image); inferred (which quantity is plotted, pixel number) |
| Severity | major |
| Source | SD, AB |

**GB-11 The posterior uncertainty metric has six names and two definitions**

| Field | Content |
|---|---|
| Check | P38 |
| Location | p. 8, l. 237 to 239 (Eq. 22); p. 10, l. 303; p. 14, l. 436; Fig. 5f, 5h; Fig. 7 to 10; Fig. 14 to 16 |
| Quotation | "The third metric is the ratio between the posterior model covariance and the “prior” model covariance." |
| Concern | Eq. 22 defines an element-wise ratio of square roots. Sect. 4.2.2 uses a ratio of traces without square roots, tr(Cm,post)/tr(Cm) (l. 436). The quantity is called "normalised posterior variance" (l. 303), "Normalised posterior covariance" (Fig. 5f), "Normalised covariance trace" (Fig. 5h, 6h), "Trace(post. cov.)" (Fig. 7 to 9), "Normalised posterior uncertainty" with axis "Trace(post.covar.)" (Fig. 10) and "Total normalised posterior uncertainty" (Fig. 14 to 16). A trace ratio and a mean of square-root ratios differ in value, so the reader cannot tell which number 0.74, 0.82 or 0.87 is. |
| Suggestion | Define the scalar summary once in Sect. 3.3 next to Eq. 22 and use one name in text and all figure labels. |
| Status | verified |
| Severity | moderate |
| Source | S2 |

**GB-12 The XRD processing and the tracer selection cannot be rebuilt from the text**

| Field | Content |
|---|---|
| Check | P8, P35 |
| Location | p. 9, l. 251 to 259; p. 11, l. 312; p. 12, l. 355 to 357; p. 13, l. 396 to 398 |
| Quotation | "In a fifth step, diagnostic 2θ windows for each mineral are selected from RRUFF database reference" |
| Concern | Missing for rebuilding: diffractometer, radiation, scan range and step; grain size fraction and powder preparation of source and detrital samples; version, thresholds and fitting settings of the WinXRD Peak Finder; the 2θ window of each of the 21 minerals; what "average the total peak area" (l. 260) means; the number of source samples per unit; how a PCA can "retain the subset of tracers" (l. 356), since it yields components rather than tracers; how the steepest descent gradient was normalised (l. 312); how the synthetic fingerprints of Fig. 5k were generated. |
| Suggestion | Add a table of 2θ windows and instrument settings to Sect. 3.4, sample numbers per unit to Sect. 4.2 and the PCA ranking rule to Sect. 4.1.3. |
| Status | verified |
| Severity | moderate |
| Source | SD |

**GB-13 Per-sample normalisation by the maximum peak area biases the unmixing, and the synthetic tests cannot detect it**

| Field | Content |
|---|---|
| Check | P9 |
| Location | p. 9, l. 260 to 261; Fig. 5k |
| Quotation | "these are normalized within each sample by dividing by the maximum observed peak area, yielding relative mineral" |
| Concern | Eq. 1 treats the detrital signal as a weighted average of source signals. If raw peak areas mix linearly, d_raw = Σ w_j M_j c̃_j, where M_j is the maximum peak area of source j and c̃_j its normalised fingerprint; after dividing d_raw by its own maximum the inversion recovers w_j M_j / M_mix instead of w_j (Python, two sources with maxima 10 and 8 and true shares 0.5 and 0.5: recovered ratio 1.25 = 10/8). Sources with one strong reflection, such as quartz-rich units, are over-weighted. The synthetic tests draw fingerprints and data from the same forward model (l. 287 to 288), and Fig. 5k even normalises each tracer to a sum of 1 over the units rather than each sample to its maximum, so they cannot reveal the bias. Is, in addition, the mineral composition of fine suspended sediment comparable to that of bulk rock powder? The discussion names grain size effects (l. 469 to 471), but only as measurement effects. |
| Suggestion | Counter-design: laboratory mixtures of the source powders in known proportions, processed with the full pipeline of Sect. 3.4 and inverted; normalise by an internal standard instead of the sample maximum, or include the maxima M_j in A. |
| Status | inferred (normalisation effect); assumption (sorting effect) |
| Severity | major |
| Source | SD |

#### Minor corrections

| ID | Location | Quotation | Replacement | Source |
|---|---|---|---|---|
| KK-05 | p. 6, l. 175 | Eq. 5 without relation symbol between "p (εm ∣dobs )" and "p (dobs ∣εm )" | "p (εm ∣dobs ) = p (dobs ∣εm ) · p(εprior) / p(dobs)" | S4 |
| KK-06 | p. 6, l. 181; p. 8, l. 223 to 224; p. 11, l. 333 | "becomes Tarantola (2005):"; "estimated by (Tarantola, 2005):"; "proposed by (Steck et al.," | "becomes (Tarantola, 2005):"; "estimated by Tarantola (2005):"; "proposed by Steck et al. (2015)"; likewise "validated in De Doncker et al. (2020)" (l. 61) and "described in Belotti (2021)" (l. 424) | S4 |
| KK-07 | p. 9, l. 245 | "weighed by the model covariance" | "weighted by the model covariance" | S4 |
| KK-08 | p. 9, l. 267; p. 9, l. 272; p. 13, l. 392 | "Gorner-gletscher"; "Gornergletscher"; "Gorner Glacier" | one form throughout, e.g. "Gornergletscher"; likewise "Gorner gletscher" (l. 463) and the caption of Fig. 11 | S2 |
| KK-09 | Fig. 3c, legend | "quarz pattern" | "quartz pattern" | AB |
| KK-10 | Fig. 4, legend (repeated in Fig. 12) | "schits", "calcarious mica schist", "caclcite-zoisite amphibolites", "silimanite-biotite gneiss", "GornergratPermo-Mesozoic" | "schists", "calcareous mica schist", "calcite-zoisite amphibolites", "sillimanite-biotite gneiss", "Gornergrat Permo-Mesozoic" | AB |

#### Verification log

| ID | Check | Checked | Values | Result |
|---|---|---|---|---|
| PP-04 | P10 | design sketch: aims, questions, cases, comparison, chain to results | aims l. 63 to 64 and l. 40 to 42; three natural-data questions l. 282 to 285 (alignment, subcatchment attribution, gain from zircon); 7 units, 21 tracers, 300 m pixels; comparisons: synthetic truth, zircon; question 1 instrument Fig. 11 qualitative, question 2 Fig. 13, question 3 Fig. 14 to 16; cost aim without instrument; only question 3 taken up in Sect. 5 (l. 461 to 463) | findings GB-01, GB-07, GB-21, GB-22, GB-24, GB-29 |
| PP-05 | P38 | identifiers of methods, units, minerals, metrics | SD and QN used consistently after l. 211; 7 units with the same names in Fig. 4, 11, 13, 15 apart from KK-08, KK-13 and the caption of Fig. 11 (GB-21); 21 minerals at l. 394 to 396 against 21 labels in Fig. 11, one spelling deviation (KK-14) | no finding beyond GB-06, GB-11 |
| PP-06 | P12 | appendices and supplements | the manuscript has neither appendix nor supplement | no finding; data statement in GB-32 |
| PP-07 | P29, P3 | inventory of figures | Fig. 1 to 3 schematics p. 22 to 24 (l. 146 to 149, 166 to 167, 251 to 262); Fig. 4 map p. 25 (l. 269 to 270); Fig. 5, 6 maps and diagrams p. 26, 27 (l. 288 to 319); Fig. 7 to 9 scenario plots p. 28 to 30 (l. 334, 347, 356); Fig. 10 fifteen sweep plots p. 31 (l. 371); Fig. 11 bar chart p. 32 (l. 398); Fig. 12 map p. 33 (l. 412); Fig. 13 KDE plots p. 34 (l. 414); Fig. 14 to 16 maps and bars p. 35 to 37 (l. 429, 438, 445); no graphical abstract | 16 figures, numbered without gap, all referenced; no finding |
| PP-08 | P29 | schematic figures 1 to 3 | legends explain all colours and symbols; panels a to e explained in the captions | no finding apart from KK-09 |
| PP-09 | P7, P30 | method versions and corrections over time | one correction, the gradient normalisation of steepest descent (l. 312), applied before the reported run; no dated protocol change; only one sample date given (28 June 2019) | no finding |
| PP-10 | P5 | own recommendations a) to c) (l. 463 to 466) against own site | a) "well constrained" lithology against lithology inferred under ice (l. 270 to 272), which the manuscript discloses | no finding |
| PP-11 | P27 | unchecked components feeding later steps | inferred map feeds A, tested by scenario 1 (Fig. 7); normalisation feeds all natural results | covered by GB-13 |
| PP-12 | P19 | provenance class of the data | Sect. 4.1 entirely model-generated and declared synthetic; geological map partly interpretation, declared (l. 270 to 272) | no finding |
| PP-13 | P17 | place of disclosure | inferred lithology stated at the method (l. 270 to 272); storage and grain size only in the discussion (l. 466 to 473) | covered by GB-13, GB-31 |

### Segment 3: Results, figures 5 to 16 (p. 10 to 15, figures p. 26 to 37)

#### Substantive findings

**GB-14 All synthetic tests rest on one true map and on data from the inversion model itself**

| Field | Content |
|---|---|
| Check | P9 |
| Location | p. 10, l. 287 to 292 |
| Quotation | "To validate our inversion model, we generate synthetic detrital data using the forward model applied to a “true” erosion rate" |
| Concern | One true map with one hotspot is used throughout (Fig. 5a, 6a, Sect. 4.1.3 and 4.1.4); no noise added to the synthetic data is mentioned, and data, fingerprints and map come from the model used for the inversion, except in scenario 1. The general statements of the conclusions (GB-31) rest on this single configuration. |
| Suggestion | State whether noise at the level of σd was added. Counter-design: an ensemble of true maps (location and size of hotspots, rates uniform per unit) with several noise realisations, reporting the spread of the error. |
| Status | verified |
| Severity | moderate |
| Source | SD |

**GB-15 The steepest descent test and the natural cases are reported with different sets of metrics**

| Field | Content |
|---|---|
| Check | P11 |
| Location | p. 11, l. 310 to 311; p. 15, l. 448 |
| Quotation | "In the next test, we use the synthetic data as input for the inversion model, this time using the steepest descent approach in the" |
| Concern | The steepest descent test gives none of the five inversion parameters stated for the quasi-Newton test (l. 293 to 295), although comparing the two schemes is an aim (abstract, l. 4 to 5). Among the natural cases (Sect. 4.2.2), the Jensen-Shannon distance is given for zircon (0.48) and combined data (0.57) but not for XRD alone (l. 448); maximum erosion rate and resolution are given for zircon only; the data misfit is given for none. |
| Suggestion | Add the steepest descent parameters to Sect. 4.1.2 and a table to Sect. 4.2.2 with JS distance, normalised uncertainty, mean resolution, data misfit and maximum erosion rate for the three natural cases. |
| Status | verified |
| Severity | moderate |
| Source | S3 |

**GB-16 After its 200 iterations the steepest descent run is closer to the truth than the quasi-Newton run**

| Field | Content |
|---|---|
| Check | P3 |
| Location | p. 11, l. 313 to 316, l. 320 to 321; Fig. 5g; Fig. 6g |
| Quotation | "we adopt the Quasi-Newton (QN) approach for all subsequent tests, as it provides a more stable" |
| Concern | Measured at 300 dpi: quasi-Newton ends at Σ∣e_true − e_post∣ = 200.8 ± 0.6 after 100 iterations, with a minimum of 197.2 ± 0.6 near iteration 20 (y ticks 340 at 93.5 px, 200 at 529.5 px); steepest descent ends at 192.8 ± 0.8 after 200 iterations (ticks 375 at 71.0 px, 200 at 519.5 px), 4.0 % lower. At equal 100 iterations quasi-Newton is better (200.8 against 211.3 ± 1.6). "more stable and accurate" thus holds for accuracy per iteration only, "stable" is not quantified, and the rise of the quasi-Newton error after iteration 20 is not mentioned. |
| Suggestion | State in l. 320 to 321 the measured final errors and the iteration budget on which the choice rests, and mention the rise after iteration 20 in Sect. 4.1.1. |
| Status | verified |
| Severity | moderate |
| Source | AB |

**GB-17 Fig. 8 shows 14 of the 20 tested blending levels, and its error axis does not match the text**

| Field | Content |
|---|---|
| Check | P3 |
| Location | p. 12, l. 348 to 353; Fig. 8, scatter plots |
| Quotation | "In total, 20 values between the highly blended and the original synthetic fingerprints are tested" |
| Concern | Each scatter plot has 14 points (counted at the enlarged section, JS 0.25 to 0.62); the caption explains one missing case, five remain unexplained. The text gives "errors exceeding 700 mm/yr" for JS below 0.44; the axis Σ∣e_true − e_post∣ has no unit, and the four points below JS 0.44 measure 4.72e4, 6.76e5, about 6.3e3 and 3.22e5 (±1.4e3; ticks 700000 at 37.5 px, 0 at 541.5 px). They exceed 700 by a factor of 9 to 966, and the error is not monotonic in JS. |
| Suggestion | State in l. 348 how many of the 20 runs converged and are plotted, give the unit of the error axis, and correct "700 mm/yr" in l. 352 to the plotted quantity. |
| Status | verified |
| Severity | moderate |
| Source | AB, S3 |

**GB-18 Misfits and errors are compared across settings with different numbers of data and different degradation ranges**

| Field | Content |
|---|---|
| Check | P21 |
| Location | p. 12, l. 360 to 365 |
| Quotation | "To summarize, among the three tested scenarios, the strongest impact on the posterior solution arises from reduced fingerprint" |
| Concern | (1) The data misfit is a sum over the m tracers; with 1 instead of 21 tracers it falls because there are fewer terms, so "the data misfit and model misfit drop" (l. 361 to 362) does not show a better fit. (2) The ranking compares absolute errors whose size depends on how far each degradation was pushed: 6.76e5 at JS 0.27 (Fig. 8, GB-17), 347.2 ± 0.6 for one tracer (Fig. 9) and 274.8 ± 0.2 for the map of Steck et al. (Fig. 7), with an "Almost fully blended" extreme (Fig. 8) set against a single alternative map. A narrower blending range or a map with larger mismatch could change the order. |
| Suggestion | Report the data misfit per datum (divided by m) in Fig. 9 and l. 361 to 362, and rank the scenarios at matched degradation levels, or state in l. 363 to 365 that the order holds only for the tested ranges. |
| Status | verified (values, measured); inferred (effect of normalisation) |
| Severity | moderate |
| Source | S3 |

**GB-19 The smoothing distance sweep has its smallest error at the largest tested L, while all tests use L = 1200 m**

| Field | Content |
|---|---|
| Check | P3 |
| Location | p. 12, l. 372 to p. 13, l. 376; Fig. 10, first row; p. 10, l. 294; p. 11, l. 325 |
| Quotation | "However, beyond approximately 10 times the pixel size (3000 m), the solution becomes overly smooth," |
| Concern | The x axis of row 1 ends at 3000 m (last marker at 2998 ± 4 m), so no value beyond 3000 m is shown. The error falls monotonically from 256.9 ± 0.3 at L = 203 m to 194.8 ± 0.3 at L = 1230 m and 76.3 ± 0.3 at L = 2998 m (600 dpi; ticks 250 at 146.0 px, 75 at 687.0 px; 500 m at 273.5 px, 3000 m at 884.5 px); at the L = 1200 m used everywhere else the error is 194.8 / 76.3 = 2.55 times larger. The annotations "L = 3000 m", "σm = 6.2", "σd = 0.003 mm/y", "μ = 0.1" and "n_m = 25" in the third column are not explained and partly differ from the values used (1200 m, 3, 0.01 mm/y). |
| Suggestion | Extend row 1 beyond 3000 m or delete the claim in l. 373 to 374; explain the annotations in the caption of Fig. 10 and justify L = 1200 m, σm = 3 and σd = 0.01 mm/y against them; correct "Smooting distance (m)" to "Smoothing distance (m)" in row 1. |
| Status | verified |
| Severity | moderate |
| Source | AB |

**GB-20 The data standard deviation sweep changes the error by 0.012 %, but the text describes large and non-monotonic effects**

| Field | Content |
|---|---|
| Check | P3 |
| Location | p. 13, l. 380 to 384; Fig. 10, third row |
| Quotation | "Very low data standard deviation values lead to large differences between the posterior and true erosion rate maps" |
| Concern | Measured in row 3, first panel (axis offset +1.974e2, ticks 0.040 at 177.0 px and 0.020 at 653.0 px, 600 dpi): Σ∣e_true − e_post∣ = 197.4197 at the smallest σd and 197.4432 at σd = 0.89 mm/y, ±4e-5 per value; the span is 0.012 %, and the values rise monotonically. There are no "large differences", no minimum and no plateau (l. 381 to 382). The normalised uncertainty spans 0.74015 to 0.74040 and the model misfit 1.5614 to 1.5623, so "model misfit begins to decrease rapidly" (l. 384) describes a change of 0.06 %. |
| Suggestion | Rewrite l. 380 to 384 to report that σd has almost no effect in the tested range, with the measured spans, or replace the panel if it shows another run; write "10⁻² mm/y" for "10-2 mm/y" in l. 384. |
| Status | verified |
| Severity | moderate |
| Source | AB |

**GB-21 The measured XRD fingerprints repeat values across minerals and lack the diagnostic minerals of several units**

| Field | Content |
|---|---|
| Check | P3 |
| Location | p. 13, l. 399 to 401; Fig. 11; p. 9, l. 273 to p. 10, l. 279; p. 15, l. 475 to 476 |
| Quotation | "The mineralogical fingerprints derived from processed and binned XRD data align well with established knowledge of the" |
| Concern | Bar lengths measured in Fig. 11 (300 dpi, full bar 241 to 243 px, ±0.004): Anorthite and Pyroxene have identical values in all seven units (0.00, 0.14, 1.00, 0.38, 1.00, 0.02, 0.42), as do Ankerite and Dolomite, and Annite and Phlogopite; Muscovite differs from these two in one unit only (0.17 against 0.21), and Albite and Paragonite agree within 0.03. Only 18 of 21 rows differ at a tolerance of 0.01, 15 at 0.05. Against the lithologies of l. 273 to 279: Almandine (garnet) is at most 0.09 in every unit, also in the garnet-mica schists (Stockhorn, Tuftgrat, Gornergrat 0.08; Monte Rosa garnet gneiss 0.02) and in the eclogite unit (0.09); Omphacite is 0.05 in the eclogite unit; Tremolite is 0.89 in the Monte Rosa granite; the serpentine minerals reach 0.57 in the Stockhorn, Tuftgrat, Gornergrat unit. "align well" is stated without any comparison. Do identical values come from shared 2θ windows, despite the averaging said to reduce peak overlap (l. 475 to 476)? |
| Suggestion | Replace l. 399 to 401 by a table of expected and measured main minerals per unit, list the 2θ window of each mineral, merge minerals with identical windows into one tracer before counting tracers, correct "supporting the 1) the robustness" to "supporting 1) the robustness" (l. 400), and in the caption of Fig. 11 "Stockhorn-Turftgrat-Gornergrat" to "Stockhorn-Tuftgrat-Gornergrat" and "ecologites" to "eclogites". |
| Status | verified (measured values); inferred (expectation from the lithology descriptions in the manuscript) |
| Severity | major |
| Source | AB |

**GB-22 In Fig. 13 the unit that should be absent cannot be told apart from three units that are present**

| Field | Content |
|---|---|
| Check | P3 |
| Location | p. 14, l. 414 to 415; p. 14, l. 411; Fig. 13; Fig. 12 |
| Quotation | "predicted erosion rates for pixels within the Zermatt - Saas Fee unit (ZSF sediments) are close to zero (Figure 13)" |
| Concern | KDE peak positions measured (300 dpi, ticks 0.0 at 542.5 px, 3.0 at 1876.5 px, ±0.002 mm/y): ZSF sediments 0.006, Furgg series 0.008, ZSF serpentinites 0.035, Monte Rosa granite 0.042, ZSF metabasites 0.24 and Monte Rosa gneiss 0.61 mm/y. Three units present in the subcatchment peak as close to zero as the absent unit, so "close to zero" does not show that the inversion "respects geological boundaries" (l. 415). Fig. 12, whose caption claims to show the subcatchment, draws no boundary; the inset of Fig. 13 does, and its dashed line encloses mainly the granite, Stockhorn and Furgg areas, while the ZSF metabasite area lies outside. Is the metabasite unit present in the subcatchment, as l. 411 implies? |
| Suggestion | Draw the subcatchment boundary in Fig. 12, give the area of each unit inside it in Sect. 4.2.1, and compare each unit's posterior with its prior rather than with zero. |
| Status | verified (peak positions); inferred (units inside the boundary, map without grid) |
| Severity | major |
| Source | AB |

**GB-23 The number of detrital samples and inversions behind Fig. 13 is not given**

| Field | Content |
|---|---|
| Check | P20 |
| Location | p. 14, l. 413 |
| Quotation | "Merging the inversion results from multiple detrital samples collected at the sink of this sub-catchment" |
| Concern | The KDEs pool "all pixels within each lithological unit" over "multiple inversions" (caption of Fig. 13). Neither the number of samples nor their dates nor the number of pixels per unit is given, so the reader cannot judge whether a peak reflects many samples or many correlated pixels of a few samples. |
| Suggestion | State in Sect. 4.2.1 the number and dates of the Gorner-Grenz samples and the number of pixels per unit inside the subcatchment. |
| Status | verified |
| Severity | moderate |
| Source | S3 |

**GB-24 The zircon benchmark is confounded by missing and copied source data and has no reference**

| Field | Content |
|---|---|
| Check | P9, P37 |
| Location | p. 14, l. 420 to 425; p. 14, l. 430 to 435; p. 10, l. 284 to 285; Fig. 14; Fig. 16 |
| Quotation | "To compensate for the lack of age data for the MR g-g unit, we assigned the MR g-g unit the same" |
| Concern | In the zircon inversion one unit has no zircon at all (ZSF metabasites), one carries the fingerprint of another (MR g-g copied from the granite), so two units are indistinguishable by construction, and one has "very low concentrations" (l. 432 to 433). The instability of the zircon solution (more than 8000 mm/y) can therefore come from these gaps, from an unreported and possibly small number of dated grains (GB-04), or from the method; the comparison does not separate these causes, and "accuracy" (l. 285) cannot be assessed without a reference. The captions of Fig. 14 and 16 show the copied fingerprint as a source fingerprint without a note. |
| Suggestion | Report the grain numbers per sample; repeat the comparison on the units with own zircon data, merging MR granite and MR g-g in both data sets; mark the substituted unit in the captions of Fig. 14 and 16 and name it as in Fig. 4 ("Monte Rosa (garnet gneiss and micaschist)", l. 432). Counter-design for accuracy: laboratory known mixtures, or several confluence samples whose subcatchments lack different units. |
| Status | verified (data gaps and captions); inferred (causes) |
| Severity | major |
| Source | SD |

**GB-25 Inputs of the natural inversions are not given or do not apply to natural data**

| Field | Content |
|---|---|
| Check | P25, P8 |
| Location | p. 14, l. 426 to 428; p. 15, l. 443 to 445; p. 3, l. 65 to 66; p. 15, l. 452 to 453 |
| Quotation | "deviation of 0.01 mm/y, a prior equal to the average true erosion rate, and a step size µ of 0.1" |
| Concern | For the natural zircon, XRD and combined inversions the prior is "equal to the average true erosion rate" (l. 428), which exists only in the synthetic tests. The estimate of the total annual suspended sediment export, one of the four required inputs (l. 452 to 453) and the scale of d in Eq. 2, is given neither as value nor with source. The same σd = 0.01 mm/y is applied to the concatenated zircon age bins and XRD tracers (l. 443 to 445), which are normalised differently (Fig. 14, 15). No sample location, source or detrital, is given in text or figures. |
| Suggestion | State in Sect. 4.2 the prior, the sediment export value with source, the σd used for each data type, and the coordinates of all samples (table, or markers in Fig. 4). |
| Status | verified |
| Severity | moderate |
| Source | SD |

**GB-26 Several figures cannot be read without the text: missing units, wrong axis titles, font below 6 pt**

| Field | Content |
|---|---|
| Check | P29 |
| Location | Fig. 5a to 5c, 5e, 5g; Fig. 6g to 6i; Fig. 9, scatter plots; Fig. 10, all panels; Fig. 11; Fig. 13; Fig. 14 to 16 |
| Quotation | "Avg. JS distance between lithologies" |
| Concern | Fig. 10: tick labels 3.7 pt (digit height 11 px at 300 dpi), axis titles 4.0 pt (cap height 12 px), below 6 pt. Fig. 9: the x axes are titled "Avg. JS distance between lithologies" but run from 0 to 21 tracers. The colour bars of Fig. 5a, 5b, 5c, 5e and the error axes of Fig. 5g, 6g, 7 and 8 have no unit. Fig. 6g and 6h lack the x title, Fig. 6i lacks x title and scale factor (Fig. 5i shows "1e8"). Fig. 11 has no scale and no column labels. The upper panel of Fig. 13 has no density values. The hatched low-confidence areas (Fig. 5b, 14 to 16) are defined neither in a caption nor in the text. |
| Suggestion | Enlarge the fonts of Fig. 10 to at least 6 pt, correct the x titles of Fig. 9, add units and missing axis titles, label the columns of Fig. 11, and define low-confidence areas in Sect. 3.3 and in the captions. |
| Status | verified |
| Severity | minor |
| Source | AB |

#### Minor corrections

| ID | Location | Quotation | Replacement | Source |
|---|---|---|---|---|
| KK-11 | p. 11, l. 317 | "(Figure 6G versus Figure 6G)" | "(Figure 6H)" (the posterior covariance during the iterations is panel h) | S4 |
| KK-12 | p. 11, l. 319 | "(Figure 6D, 6E and 6F )" | "(Figure 6D, 6E and 6F)" | S4 |
| KK-13 | p. 12, l. 340 | "Zermatt-Saas-Fee ophiolites" | "Zermatt-Saas Fee ophiolites"; one form also at l. 299, l. 411, l. 431 and in the caption of Fig. 12 | S2, AB |
| KK-14 | p. 13, l. 395 | "Chrysolite" | "Chrysotile" (as in l. 274 and Fig. 11; chrysolite is an olivine) | S2 |
| KK-15 | Fig. 7, title of the left map | "Originial geology" | "Original geology" | AB |
| KK-16 | Fig. 9, colour bar | "Number of tracrs" | "Number of tracers" | AB |
| KK-17 | Fig. 15, legend (likewise Fig. 14 and 16) | "Low-con dence area" | "Low-confidence area" | AB |

#### Verification log

| ID | Check | Checked | Values | Result |
|---|---|---|---|---|
| PP-14 | P3 | Fig. 5g and 6g, error against iteration | quasi-Newton: 197.2 ± 0.6 near iteration 20, 200.8 ± 0.6 at 100; steepest descent: 211.3 ± 1.6 at 100, 192.8 ± 0.8 at 200; x axes end at 100 and 200, matching l. 293 | values used in GB-16 |
| PP-15 | P3 | Fig. 6h against l. 316 ("visible after 125 iterations") | kink of the trace curve at iteration 136 (600 dpi, ticks 0 at 68 px, 200 at 1012 px), afterwards a slowly falling, slightly thickened band | no finding |
| PP-16 | P3 | Fig. 7 against l. 337 to 342 | error: same map 197.2, minimal changes 193.6 ± 0.2, Steck et al. 274.8 ± 0.2 (ticks 270 at 70.5 px, 190 at 550.5 px); data misfit 3.26e6, 3.49e6, 3.68e6 and model misfit 1.57, 1.92, 2.46 rise in this order | no finding: agrees with l. 338 to 342 |
| PP-17 | P3 | Fig. 9 against l. 357 to 362 | 21 points per scatter plot (counted at the enlarged section); 1 tracer 347.2 ± 0.6, 7 to 21 tracers 197.4 ± 0.3 (ticks 340 at 73.5 px, 200 at 524.5 px) | no finding: agrees with "7 tracers" (l. 360) |
| PP-18 | P2, P3 | labels of Fig. 14 to 16 against text | total normalised uncertainty 0.87, 0.82, 0.86 equal to l. 436, 442, 447; colour scale of Fig. 14 up to 8000 mm/y, text "more than 8000" (l. 435) | no finding |
| PP-19 | P29 | font size of Fig. 8 tick labels | digit height 17 px at 300 dpi, 5.7 pt (±0.6 pt) | no finding: not below 6 pt beyond the uncertainty |
| PP-20 | P24 | dated events in figures | no figure shows dates or a time axis; the sample date (l. 423 to 424) is not plotted | no finding, not applicable |
| PP-21 | P1 | derived numbers | 1200/4 = 300 m, 3000/10 = 300 m; 21 minerals listed at l. 394 to 396 and 21 tracers at l. 358; 0.87 to 0.86 "decreases slightly" (l. 447), 0.87 to 0.82 "slightly lower" (l. 441 to 442) | no finding |
| PP-22 | P2 | same quantities at several places | QN with 100 iterations (l. 293) and Fig. 5g to 5i; example JS 0.441 (Fig. 8) at the boundary of l. 353; JS 0.48 and 0.57 (l. 448) stated once only; abstract contains no numbers | no finding |
| PP-23 | P23 | balances | none in the manuscript | no finding, not applicable |
| PP-24 | P20 | quotas | JS distance averaged over all pairs (l. 347): 7 units give 21 pairs | no finding beyond GB-23 |
| PP-25 | P34 | selections from counted sets | Fig. 8 shows 3 of 20 fingerprint sets and Fig. 9 3 of 21, each with a stated rule (most, half, not blended; 1, 11, 21 tracers) | no finding; plotted count in GB-17 |
| PP-26 | P32, P36 | claims of error-free results, recollections | none | no finding, not applicable |

### Segment 4: Discussion, conclusions, statements, references (p. 15 to 21)

#### Substantive findings

**GB-27 The stated novelty is already contained in the cited predecessor**

| Field | Content |
|---|---|
| Check | P28, P14 |
| Location | p. 15, l. 454 to 455; p. 2, l. 58 to 61 |
| Quotation | "The novelty of our method lies in the spatially informed approach of this underdetermined" |
| Concern | The introduction itself calls the method "a non-linear adaptation of the inversion framework validated in (De Doncker et al., 2020)" (l. 60 to 61). De Doncker et al. (2020) already invert detrital zircon ages, with prior and covariance information, into an erosion rate map of a catchment and name mineral content as a possible tracer (abstract read). The spatially informed inversion is therefore not new; new are the log-space parametrisation and the binned XRD tracer set. |
| Suggestion | Rewrite l. 454 to 455 to state the novelty against De Doncker et al. (2020): log-space (non-linear) parametrisation, XRD tracer set and its processing. |
| Status | verified |
| Severity | moderate |
| Source | S1 |

**GB-28 The discussion states an effect of the number of source areas that was never tested**

| Field | Content |
|---|---|
| Check | P15 |
| Location | p. 15, l. 460 to 461 |
| Quotation | "higher number of distinct source areas leads to higher posterior resolution and lower uncertainty" |
| Concern | The synthetic tests vary the geological map (three maps), fingerprint blending, tracer number and five hyperparameters (Sect. 4.1.3, 4.1.4); none varies the number of source areas. The statement has no result behind it, yet it supports the recommendation of "multiple mineralogically distinct source areas" (l. 485). |
| Suggestion | Delete the sentence, or add a test with merged or split units and cite it in l. 460 to 461 and l. 485. |
| Status | verified |
| Severity | moderate |
| Source | S4 |

**GB-29 The combined zircon and XRD inversion is more uncertain than XRD alone, but the discussion claims a further improvement**

| Field | Content |
|---|---|
| Check | P15 |
| Location | p. 15, l. 462 to 463; p. 15, l. 441 to 442, l. 446 to 447; p. 3, l. 72 to 73; p. 10, l. 284 to 285 |
| Quotation | "XRD data with other fingerprint data such as zircon data, proves to further stabilize and improve the posterior solution" |
| Concern | The normalised posterior uncertainty is 0.82 for XRD alone (l. 441 to 442), 0.86 combined and 0.87 for zircon alone (l. 447). Combining improves on zircon alone but is worse than XRD alone, so "further" is not supported; "sharpness" (l. 73) and "accuracy" (l. 285) are not measured, and for natural data no truth is available. In a linear Gaussian setting with the same prior and linearisation point, adding data cannot raise the trace of the posterior covariance (Python: trace ratio 0.650 with 21 data rows, 0.433 with 34); the rise to 0.86 shows that the metric is evaluated at different non-linear solutions and does not compare the data sets on equal terms. |
| Suggestion | Rewrite l. 462 to 463 and l. 72 to 73: combining improves on zircon alone (0.87 to 0.86), not on XRD alone (0.82); report the uncertainty of all three cases linearised at the same model, or drop "further". |
| Status | verified (values); inferred (cause of the rise) |
| Severity | major |
| Source | S4 |

**GB-30 The own detrital sampling is not described against the own recommendation**

| Field | Content |
|---|---|
| Check | P18 |
| Location | p. 15, l. 470 to 471; Fig. 1c; Fig. 3a |
| Quotation | "This can be diminished by powdering samples and using depth-integrated suspended sediment samples" |
| Concern | The discussion recommends depth-integrated samples; the only trace of the own detrital sampling is the "pump sampler" drawn in Fig. 1 and 3. Were the own samples depth-integrated? |
| Suggestion | Describe the detrital sampling (device, depth, volume, time) in Sect. 4.2. |
| Status | assumption |
| Severity | moderate |
| Source | SD |

**GB-31 The conclusions call the method reliable and robust beyond what the tests show**

| Field | Content |
|---|---|
| Check | P15 |
| Location | p. 16, l. 482 to 486; p. 15, l. 466 to 468 |
| Quotation | "we show that the true erosion pattern can be reliably recovered, and that" |
| Concern | The own results restrict this: for JS below about 0.44 the inversion "fails to converge to a stable posterior solution" in many cases (l. 353), fewer than 7 tracers raise the error (l. 360 to 361), and all synthetic tests use one true map (GB-14). "minimal sediment storage" (l. 485) appears as a result ("Our results suggest"), although storage was not tested and Sect. 5 introduces it as an assumption of the method (l. 466 to 468). |
| Suggestion | Qualify l. 482 to 483 with the tested ranges (JS above 0.55, at least 7 tracers, one true map), and present storage in l. 484 to 485 as an assumption, not a result. |
| Status | verified |
| Severity | moderate |
| Source | S4 |

**GB-32 The data availability statement covers only the inversion tests, not the natural data**

| Field | Content |
|---|---|
| Check | P12 |
| Location | p. 16, l. 490 |
| Quotation | "The data and codes used for the inversion tests in the study are available at https://doi.org/10.5281/zenodo.17120374" |
| Concern | The methods name eight data sources: inversion code and test data, raw diffractograms of source and of detrital samples, processing settings with 2θ windows, zircon U-Pb ages (method only in an unpublished thesis, l. 424), the geological map with parts inferred under ice and credited to "personal communication" in Fig. 4, sample locations, and the sediment export estimate. The statement names only the first. None of the others concerns persons, so no reason for withholding applies. Whether the Zenodo record holds them could not be checked (record not reachable): accessibility not checked. |
| Suggestion | Extend the statement at l. 490 to list each data set with its place in the repository, or state where each one is held. |
| Status | verified (wording of the statement); inferred (content of the repository) |
| Severity | moderate |
| Source | S2 |

#### Minor corrections

| ID | Location | Quotation | Replacement | Source |
|---|---|---|---|---|
| KK-18 | p. 17, l. 522 to 523 | "Master’s thesis, University of Lausanne," and "unpublished master’s thesis" | "Master’s thesis, University of Lausanne (unpublished)" | S4 |
| KK-19 | p. 19, l. 578 | "[No title found]" | "Landscape indicators of human impacts to riverine systems" | S4 |

#### Verification log

| ID | Check | Checked | Values | Result |
|---|---|---|---|---|
| PP-27 | P4 | figure numbers and references | Fig. 1 to 16 each referenced, first at l. 146, 166, 251, 269, 288, 314, 334, 347, 356, 371, 398, 412, 414, 429, 438, 445; all panel letters cited in the text exist in the captions, except "6G versus 6G" (KK-11) | no finding |
| PP-28 | P4 | citations against reference list, both directions | 64 short citations, 64 entries, all matched; names and years agree except "E." (KK-02) | no finding |
| PP-29 | P4 | equation references | "eq. 1-4" (l. 263), eq. 7 (l. 191, 240, 245), eq. 10 to 16 (l. 200, 204, 213, 217) point to the right equations | no finding |
| PP-30 | P15 | each proposal of Sect. 5 and 6 against own results | a) well constrained lithology: scenario 1 (Fig. 7); b) strong contrasts: scenario 2 (Fig. 8); c) several tracers: scenario 3 (Fig. 9); land use maps and sub-catchments as source areas (l. 466, l. 487 to 488) stated as possible, not as shown, and limited by GB-07; caution against storage (l. 466 to 468) an assumption; other tracers (l. 488 to 489) shown with zircon | no finding beyond GB-28, GB-31 |
| PP-31 | P15 | key terms of the aims in Sect. 5 and 6 | "erosion rate maps" and "posterior uncertainty" taken up; "cost-effective" (l. 3, l. 74) not taken up | handled in GB-01 |
| PP-32 | P16 | uniformity of the reference list | DOIs missing for Papanicolaou et al. 2003, Gjems 1967, Bearth 1953, Lafuente et al. 2015, Moore and Reynolds 1990; Gjems 1967 and Bearth 1953 without publisher; Tarantola 2005 with two ISBNs; "oCLC" in the Walling entry | no finding: non-uniform entries; the citation style is an optional check |

## Optional checks

| Area | What it needs | Responsible | Run |
|---|---|---|---|
| DOI resolution | one fetch per reference with a DOI | `science-quellenapparat-pruefung` | no |
| Citation style | the name of the style | `science-zitierstil-harvard-ctr` or the style rules of the journal | no |
| AI statement against publisher policy | the policy of the target publisher | this review, on request | no |
| Relation to own prior work | the authors' prior work | this review, on request | no |
| Journal requirements | the author guidelines of the target journal | this review, on request | no |
| Subject accuracy | access to the sources of the checked statements and a selection of sections | `science-faktenbeleg-pruefung`, `geo-frage-belegbasiert-klaeren` | no |

## Limits of this review

- Checked version: egusphere-2025-4695.pdf, 37 pages, SHA-256 9c80676054f96ecd6f00f4d2a8b5ba568e03c6949e3856d363ac1c4abb42e7bd.
- The six review instances ran sequentially in one context, not context-separated; separate agents usually find more.
- Unreadable sources: Das et al. (2023), Water Resources Research (fetch failed); Walling (2009), UNESCO report (archive rate-limited); Zenodo record https://doi.org/10.5281/zenodo.17120374 (HTTP 429); Barker et al. (1997) and Blaen et al. (2016) were judged from their titles only.
- The pixel number (about 818) is estimated from the catchment area in Fig. 4 and the 300 m pixel size; it is not stated in the manuscript.
- Findings with status assumption: 1 of 32 (GB-30); GB-13 has one partial statement with this status.
- Optional checks run: 0 of 6.
- Omitted instances: none.
- Discarded findings: 0.
