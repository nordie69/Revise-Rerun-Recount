# Review report: From XRD signal to erosion rate maps

| Field | Value |
|---|---|
| Manuscript | De Doncker, F., Herman, F., Belotti, B. and Adatte, T. (2025) From XRD signal to erosion rate maps, EGUsphere preprint, https://doi.org/10.5194/egusphere-2025-4695 |
| Checked version | egusphere-2025-4695.pdf, 37 pages, SHA-256 9c80676054f96ecd6f00f4d2a8b5ba568e03c6949e3856d363ac1c4abb42e7bd |
| Date | 2026-10-18 |
| Language | English |
| Review instances | Segments 1 to 4, figures, study design; checked sequentially, not context-separated: the six review instances ran one after another in a single context; no instance omitted |
| Note | Review instances ran sequentially in one context, not as separate agents. |

## Summary

The manuscript is a method-development study. It proposes to use binned X-ray diffraction (XRD) peak areas of 21 minerals as sediment fingerprints in a spatially explicit Bayesian inversion that turns detrital fingerprint concentrations, a map of source units and an annual sediment export estimate into erosion rate maps. The forward model is a weighted average of source fingerprints with erosion rates in log space; the inversion is solved by steepest descent and quasi-Newton iterations, and uncertainty is expressed by posterior covariance, resolution and a normalised covariance ratio. Synthetic forward-inverse tests on the Gornergletscher catchment (seven units, 300 m pixels) compare both solvers, three degradation scenarios (map mismatch with three maps, 20 levels of fingerprint blending, 1 to 21 tracers) and five hyperparameter sweeps. Natural data tests compare XRD source fingerprints with the known lithology, check that samples from the Gorner-Grenz subcatchment do not attribute erosion to the one unit absent there, and compare zircon U-Pb, XRD and combined fingerprints for one detrital sample of 28 June 2019, with total normalised posterior uncertainties of 0.87, 0.82 and 0.86.

## Strengths

1. The synthetic programme varies one factor at a time (solver, map geometry, fingerprint blending, tracer count, five hyperparameters) and reports for each the error, the posterior uncertainty and the misfit trade-off; this lets a reader locate where the inversion degrades, for example the jump of the posterior uncertainty near a JS distance of 0.55 and the plateau of the error from seven tracers on (PP-17, PP-21, PP-22).
2. The manuscript discloses its own adverse outcomes where they occur: the instability of steepest descent and its fix, non-converged blended runs, the missing zircon fingerprints of two units and the borrowed fingerprint of the Monte Rosa gneiss, and the inferred geology under the ice; a reader can therefore see which inputs are measured and which are substituted (PP-08, PP-10).
3. XRD is benchmarked against an independent tracer, zircon U-Pb ages, on the same detrital sample with identical inversion parameters, and all three solutions are reported with the same uncertainty metric, which makes the comparison like for like (PP-16, PP-17).
4. The formal apparatus is complete in both directions: all 64 references are cited and all citations are listed, figures 1 to 16 and equations 1 to 22 are consecutive and every figure is cited in the text, and code and data are deposited under a DOI (PP-29, PP-30, PP-34).

## Weaknesses

1. The synthetic tests cannot fail in the ways the natural application can: data are generated with the same forward model and normalised space, without stated noise, with a smooth single-hotspot truth and a prior equal to the true mean, and hyperparameters are tuned on the truth; the per-sample maximum normalisation of real diffractograms breaks the weighted-average forward model (GB-12, GB-10, GB-28). Proposal: add noisy synthetic cases mixed in raw peak-area space with several and non-smooth hotspots, a laboratory known-mixture test, and a hyperparameter criterion available for natural data.
2. The natural tests do not carry the claim that they "validate" the method: the subcatchment test discriminates on a single unit and cannot separate the absent from a present unit, the agreement of fingerprints with the lithology is asserted without comparison, the zircon hotspot lies in a unit without zircon signal, and the combination with zircon is less certain than XRD alone (GB-24, GB-23, GB-29, GB-30, GB-31). Proposal: compare unit contributions with area shares, quantify fingerprint agreement against independent mineralogy, and restate the abstract, aim 3 and the discussion as consistency rather than validation.
3. Several reported results disagree with the manuscript's own figures or definitions: resolution maps exceed the trace bound of the resolution operator, the posterior overshoots the synthetic hotspot by about 2 mm/y, the data standard deviation has almost no effect in Fig. 10, the 700 mm/yr threshold does not fit the plotted error, and 5 of 20 blending runs are missing (GB-14, GB-13, GB-22, GB-17, GB-16). Proposal: recompute and replot the resolution, report peak values and the dropped runs, and rewrite the result sentences from the measured figures.
4. Reproducibility and form fall short in several places of moderate weight: equations with sign, transpose and rank problems, missing processing settings and the annual export value, a data statement that does not itemise its sources, three metrics under one name, a duplicated introduction and a theology paper cited for pollen fingerprinting (GB-07, GB-09, GB-36, GB-08, GB-06, GB-04). Proposal: correct the equations, add a settings table and an itemised data statement, define one metric, delete Section 2 and fix the citations.

## Findings by segment

### Segment 1: Abstract, introduction, state of research (p. 1 to 5)

#### Substantive findings

**GB-01 "Time- and cost-effective" is claimed as a validated property but never measured**

| Field | Content |
|---|---|
| Check | P33 |
| Location | p. 1, l. 3 to 4; p. 2, l. 40 to 42; p. 3, l. 74 to 75 |
| Quotation | "we validate a time- and cost-effective fingerprinting approach" |
| Concern | The comparison with zircon in Section 4.2.2 sets up the right pair for such a claim, but no cost, analysis time or sample throughput is reported for XRD or for zircon U-Pb dating; the only support is a citation that other methods "are expensive and time-consuming" (p. 2, l. 35). The discussion and the conclusion do not return to cost. The efficiency is part of what the manuscript says it shows (p. 3, l. 74 to 75) but rests on no measurement. |
| Suggestion | Report cost and analyst time per sample for XRD and for zircon U-Pb dating in Section 4.2.2, or remove "validate" and "cost- and time-efficient" from p. 1, l. 3 to 4 and p. 3, l. 74 to 75. |
| Status | verified |
| Severity | moderate |
| Source | SD |

**GB-02 The abstract reports consistent convergence, while the results report failed and unstable runs**

| Field | Content |
|---|---|
| Check | P6 |
| Location | p. 1, l. 7; p. 11, l. 312; p. 12, l. 353; Fig. 8 caption |
| Quotation | "Forward-inverse tests with synthetic data demonstrate consistent convergence of the posterior solution." |
| Concern | The results disclose the exceptions: steepest descent "proved unstable, requiring the normalization of the gradient" (p. 11, l. 312); in scenario 2 "In many of these cases, the inversion fails to converge to a stable posterior solution" (p. 12, l. 353); Fig. 8 drops the most blended run for lack of a stable solution. The absolute statement in the abstract does not carry these conditions. |
| Suggestion | Qualify the sentence at p. 1, l. 7 by the conditions under which convergence was observed (quasi-Newton solver, JS distance above about 0.55). |
| Status | verified |
| Severity | moderate |
| Source | SD |

**GB-03 The citation "E., 2009" uses an initial as the author name**

| Field | Content |
|---|---|
| Check | P4 |
| Location | p. 1, l. 11 to 12; p. 3, l. 78 to 79; p. 18, l. 567 to 568 |
| Quotation | "E., W. D.: The Impact of global change on erosion and sediment transport by rivers" |
| Concern | The in-text citations ("E., 2009") and the entry are keyed on "E.", which is an initial; the surname of the author is missing from the entry. |
| Suggestion | Correct the entry at p. 18, l. 567 to the author's surname and initials and change the citations at p. 1, l. 11 to 12 and p. 3, l. 78 to 79 accordingly. |
| Status | verified (wrong key); inferred (that the surname is missing) |
| Severity | minor |
| Source | S4 |

**GB-04 Three citations do not support the statements they are attached to**

| Field | Content |
|---|---|
| Check | P13 |
| Location | p. 2, l. 31; p. 4, l. 98; p. 19, l. 597 to 598; p. 1, l. 18 to 19; p. 3, l. 85 to 86; p. 15, l. 470 to 471 |
| Quotation | "plant pollen content (Brown, 1985; Kobe, 2021)" |
| Concern | The reference list itself gives Kobe (2021) as "Ubuntu as a spirituality of liberation for black theology of liberation", HTS Teologiese Studies (p. 19, l. 597 to 598), and a search for its DOI 10.4102/hts.v77i3.6176 returns the same theology article; it cannot support pollen as a sediment fingerprint. Two more attributions are doubtful from the titles in the manuscript's own list: "sediment traps installed on dams" (p. 1, l. 18) is supported by Wilson et al. (1993), a soil erosion assessment of the Falkland Islands, and Barker et al. (1997), terrestrial photogrammetry of bank erosion; depth-integrated suspended sediment sampling to average out sorting (p. 15, l. 470 to 471) is attributed to Butler et al. (2019), a paper on pre-treatment of soil XRD data for cluster analysis. The full texts of Wilson, Barker and Butler could not be read. |
| Suggestion | Replace Kobe (2021) at p. 2, l. 31 and p. 4, l. 98 by a pollen fingerprinting study or delete it, and remove the entry at p. 19, l. 597; check that Wilson et al. (1993) and Barker et al. (1997) report sediment traps on dams and that Butler et al. (2019) discusses depth-integrated sampling, otherwise cite sources that do. |
| Status | verified (Kobe 2021, from the reference list and the DOI search); inferred (Wilson, Barker, Butler, from titles only) |
| Severity | moderate |
| Source | S1 |

**GB-05 Claim that unmixing approaches do not yield spatially explicit erosion maps is made without a search and has counterexamples**

| Field | Content |
|---|---|
| Check | P28, P14 |
| Location | p. 2, l. 58 to 59; p. 4, l. 125 to 126; p. 15, l. 454 to 455 |
| Quotation | "these approaches typically yield relative source contributions without translating them into spatially explicit erosion rate maps" |
| Concern | The introduction surveys the fingerprinting unmixing literature well, but this statement and the novelty claim "The novelty of our method lies in the spatially informed approach" (p. 15, l. 454) rest on no stated search (databases, terms, dates). Methods that turn detrital tracer distributions into spatial patterns of erosion exist and are absent from the reference list: Braun et al. (2018) invert detrital cooling-age distributions along a river into the spatial variability of erosion rates and test the method on synthetic data first, as this manuscript does; Ehlers et al. (2015) identify spatial variations of erosion in a glacial catchment from detrital thermochronology, the setting the manuscript names as its main field of use (p. 3, l. 62 to 63). The authors' own earlier inversion (De Doncker et al., 2020) is already spatial. |
| Suggestion | Restrict the claim at p. 2, l. 58 to 59 to sediment-fingerprinting unmixing models, or state the search behind it; position the contribution against Braun, J., Gemignani, L. and van der Beek, P. (2018) Extracting information on the spatial variability in erosion rate stored in detrital cooling age distributions in river sands, Earth Surface Dynamics, 6, 257 to 270, https://doi.org/10.5194/esurf-6-257-2018, and Ehlers, T. A., Szameitat, A., Enkelmann, E., Yanites, B. J. and Woodsworth, G. J. (2015) Identifying spatial variations in glacial catchment erosion with detrital thermochronology, Journal of Geophysical Research: Earth Surface, 120(6), 1023 to 1039, https://doi.org/10.1002/2014JF003432; restate the novelty at p. 15, l. 454 as the use of binned XRD peak areas within the spatial inversion of De Doncker et al. (2020). |
| Status | verified (no search stated; both works absent from the reference list; both landing pages read) |
| Severity | moderate |
| Source | S1 |

**GB-06 Section 2 repeats Section 1 word for word**

| Field | Content |
|---|---|
| Check | P4, P16 |
| Location | p. 3, l. 76 to p. 5, l. 142; p. 1, l. 9 to p. 3, l. 75 |
| Quotation | "2 Introduction" |
| Concern | Section 1 (p. 1, l. 9 to p. 3, l. 75) and Section 2 (p. 3, l. 76 to p. 5, l. 142) carry the same heading and the same text: a word-by-word comparison with difflib gives 1153 words in each and a match ratio of 1.0. 67 printed lines are duplicated, and all later sections are numbered one higher than intended. |
| Suggestion | Delete Section 2 (p. 3, l. 76 to p. 5, l. 142) and renumber Sections 3 to 6 as 2 to 5. |
| Status | verified |
| Severity | minor |
| Source | S4 |

#### Minor corrections

| ID | Location | Quotation | Replacement | Source |
|---|---|---|---|---|
| KK-01 | p. 1, l. 5 | "Quasi-Newtonian" | "quasi-Newton (QN)", as at p. 7, l. 211 | S2 |
| KK-02 | p. 2, l. 48 to 49 and l. 51; p. 4, l. 115 to 116 and l. 118 | "Non-Linear Least Squares (NLLS)" and "similar to the NNLS approach" | one acronym for the same method in both places | S2 |
| KK-03 | p. 2, l. 50; p. 4, l. 117 | "Generalist Likelihood Uncertainty Estimation (GLUE)" | "Generalised Likelihood Uncertainty Estimation (GLUE)" | S1 |
| KK-04 | p. 2, l. 51; p. 4, l. 118 | "Maximal Likelihood Estimation (MLE)" | "Maximum Likelihood Estimation (MLE)" | S1 |
| KK-05 | p. 2, l. 55 to 56; p. 4, l. 122 to 123 | "Bayesian linear mixed models" | "Bayesian linear mixing models (BLMM)", as defined at p. 2, l. 53 | S2 |
| KK-06 | p. 2, l. 61; p. 11, l. 333; p. 14, l. 424 | "validated in (De Doncker et al., 2020)" | narrative citations: "validated by De Doncker et al. (2020)", "proposed by Steck et al. (2015)", "described by Belotti (2021)", "outlined by De Doncker et al. (2020)" | S4 |

#### Verification log

| ID | Check | Checked | Values | Result |
|---|---|---|---|---|
| PP-01 | P13 | Statements with rankings or judgements from cited works in Segment 1 | 9 statements collected: p. 1, l. 16 (Poesen 2018; Borrelli 2021), l. 18 to 19 (Wilson 1993; Barker 1997; Davis and Fox 2009), l. 21 (Klages and Hsieh 1975), l. 24 to 25 (ideal fingerprint), p. 2, l. 35 and l. 36 to 37 (Das et al. 2023, "expensive and time-consuming", "underutilized"), l. 40 (Das et al. 2023, 2024), l. 43 to 57 (Haddadchi 2013; Yang 2025; Fathabadi and Jansen 2022), l. 59 (Niu 2020); Das et al. (2024) landing page read: XRD mineralogy unmixed with MixSIAR, contribution ranges broadly comparable with MIR spectroscopy, consistent with l. 40; Das et al. (2023) not readable | no finding beyond GB-04; Das et al. (2023) unverified |
| PP-02 | P14 | Contribution: binned XRD peak areas as fingerprints in a spatially explicit Bayesian inversion of detrital data into erosion rate maps for a glacierised catchment. Searches (4 of 6): "X-ray diffraction mineralogy fingerprinting suspended sediment sources glacier catchment unmixing"; "Gornergletscher suspended sediment provenance erosion source detrital"; "spatially resolved erosion rates from detrital provenance data inversion map glacier detrital thermochronology Enkelmann Ehlers"; "SedUnMix Andrews Eberl 2012 Marine Geology" | Candidates: Braun et al. 2018 (absent from list), Ehlers et al. 2015 (absent), SedUnMix program for quantitative XRD unmixing, Marine Geology 291 to 294, 24 to 33 (authors not shown on the record read, not proposed), EGU21 abstract of the authors on erosion rate maps of the Gornergletscher (own prior work, left to the optional check on prior work); hits on the publisher page, discussion and later versions of this manuscript were not opened | two proposals in GB-05 |
| PP-03 | P28 | Gap and first-time statements | p. 2, l. 36 to 37 ("remains underutilized", attributed to Das et al. 2023); p. 2, l. 58 to 59; p. 15, l. 454 to 455 ("novelty"); no search method stated for any; 1 own search for the spatial claim (third query of PP-02) | finding GB-05; the attributed "underutilized" statement no finding |

### Segment 2: Material, methods, appendix (p. 5 to 9, Figs. 1 to 3)

#### Substantive findings

**GB-07 Several equations cannot be implemented as printed**

| Field | Content |
|---|---|
| Check | P8 |
| Location | p. 6, l. 175 (eq. 5); p. 7, l. 189 (eq. 9); p. 7, l. 197 (eq. 12); p. 7, l. 201 (eq. 14); p. 8, l. 215 (eq. 18); p. 8, l. 219 (eq. 19); p. 8, l. 230 to 234 |
| Quotation | "with σm 2 the prior variance, si,j the Euclidean distance between point i and j, and L the smoothing distance" |
| Concern | The derivation is laid out step by step, which makes the errors visible. At the page image: eq. 5 has no relation sign between posterior and likelihood times prior and writes the prior as p(εprior) instead of p(εm); eq. 9 has a positive exponent, exp(s²/L²), so the prior covariance grows with distance, whereas a smoothing kernel needs exp(−s²/L²); eq. 12 writes the Jacobian as A · exp(ε), a vector, instead of A · diag(exp(ε)); eq. 14 lacks the transpose of G that eq. 16 has; eqs. 18 and 19 mix the iteration indices n and k, and n is also the number of pixels in eq. 1; eq. 19 inverts G^T Cd^−1 G, which has rank at most m = 21 for about 818 parameters (p. 6, l. 170 to 172) and is singular as printed, and it omits the Cm^−1 term that eq. 20 contains; the resolution matrix R is used in eq. 21 but never given as a formula. The code may be correct, but the text does not let a reader rebuild it. |
| Suggestion | Correct eqs. 5, 9, 12, 14, 18 and 19, add the formula for R after eq. 21, and state the damping or the Hessian actually used in the quasi-Newton step. |
| Status | verified (equations at the page image); inferred (singularity of eq. 19, pixel count) |
| Severity | moderate |
| Source | SD |

**GB-08 Three different quantities are reported under near-identical names for normalised posterior uncertainty**

| Field | Content |
|---|---|
| Check | P38 |
| Location | p. 8, l. 236 to 239 (eq. 22); p. 10, l. 303; p. 14, l. 435 to 436; p. 15, l. 441 to 442 and l. 446 to 447; Fig. 5f; Fig. 5h and caption; Fig. 10 (second column); Figs. 14 to 16 |
| Quotation | "a high total normalized uncertainty" |
| Concern | Eq. 22 defines a per-pixel ratio of square roots, the "ratio between the posterior model covariance and the prior model covariance" (p. 8, l. 236 to 237). At p. 14, l. 436 the scalar 0.87 is defined as tr(Cm,post)/tr(Cm), a ratio of summed variances without square roots. Fig. 5h is titled "Normalised covariance trace" while its caption says "(h) normalised posterior covariance"; Fig. 10 is titled "Normalised posterior uncertainty" with the axis "Trace(post.covar.)"; the text at p. 10, l. 303 says "normalised posterior variance". Counted spellings: "Normalised posterior uncertainty" 8, "normalized posterior uncertainty" 5, "normalised posterior uncertainty" 4, "normalised posterior covariance" 4, "normalised posterior variance" 1, "total normalized uncertainty" 1. A square-root ratio and a trace ratio differ numerically, so a reader cannot tell which definition produced 0.74 (Fig. 5h), 0.82, 0.86 and 0.87. |
| Suggestion | Define the scalar metric once in Section 3.3 next to eq. 22, give it one name, and use that name at p. 10, l. 303, p. 14, l. 436, p. 15, l. 441 to 447, in the caption of Fig. 5h and in the axis titles of Figs. 5, 10 and 14 to 16. |
| Status | verified |
| Severity | moderate |
| Source | S2, AB |

**GB-09 Inputs and settings needed to rebuild the processing and the runs are not given**

| Field | Content |
|---|---|
| Check | P8, P35 |
| Location | p. 9, l. 251 to 262; p. 10, l. 293 to 295; p. 11, l. 312 to 313 and l. 327 to 331; p. 12, l. 343 to 344 and l. 355 to 357; p. 15, l. 453 to 454 |
| Quotation | "the WinXRD Peak Finder algorithm corrects for baseline drift and removes the background noise" |
| Concern | The six processing steps of Section 3.4 are named in order, but the following are missing: XRD instrument, radiation, scan range and step; WinXRD version, threshold and fitting settings; the 2θ window of each of the 21 minerals; the number of source samples per unit and how they were combined; the pixel size (only implicit, "4 times the pixel size (L = 1200 m)") and the number of pixels; the value of the annual export estimate, one of the four required inputs; whether noise was added to the synthetic data; the step size of the first quasi-Newton test and the iterations and step size of the steepest descent run (Fig. 6 runs to 200); how the gradient was normalised; how the maps of scenario 1 were modified; how the blending of scenario 2 was parametrised; how the principal component analysis selected the "top" tracers. Peak finding and window choice depend on judgement and have no stated rule. |
| Suggestion | Add a table of processing settings and run parameters to Sections 3.4 and 4.1, including the 2θ windows per mineral, the number of samples per unit, the pixel size and count, and the export estimate with its source. |
| Status | verified |
| Severity | moderate |
| Source | SD |

**GB-10 Normalising each sample by its maximum peak area breaks the weighted-average forward model for natural data**

| Field | Content |
|---|---|
| Check | P25, P9 |
| Location | p. 9, l. 260 to 262; p. 5, l. 151 to 152 (eq. 1); Fig. 5k; Fig. 11; Figs. 15 and 16 (source fingerprints) |
| Quotation | "these are normalized within each sample by dividing by the maximum observed peak area" |
| Concern | Eq. 1 treats the detrital value of each tracer as a weighted average of the source values. If each source and the detrital sample are divided by their own maximum peak area, the detrital value equals the weighted average of the normalised source values only when all sources share the same maximum, because the maximum of a mixture is not the weighted average of the sources' maxima. The synthetic data are generated in the normalised space, so no synthetic test can detect this; it affects the natural runs. Figs. 5k, 15 and 16 show a second normalisation, in which each tracer sums to one across the lithologies, while Fig. 11 shows per-sample normalisation. Which of the two enters A and d? |
| Suggestion | State in Section 3.4 which normalisation enters A and d; show with a synthetic mixture in raw peak-area space that the chosen normalisation preserves eq. 1, or normalise in a way that does, for example by a common internal standard. |
| Status | inferred (from eq. 1 and p. 9, l. 261); verified (two normalisations shown in the figures) |
| Severity | major |
| Source | SD |

#### Minor corrections

| ID | Location | Quotation | Replacement | Source |
|---|---|---|---|---|
| KK-07 | p. 5, l. 146 to 149; p. 6, l. 166 to 167; p. 9, l. 251 to 262; p. 10 to 11 | "(Figure 1B)" | lower-case panel letters as in the captions, "(Figure 1b)" | S4 |
| KK-08 | p. 5, l. 154 (eq. 1) | "f or i = 1, . . . m" | "for i = 1, ..., m" in roman type | S4 |
| KK-09 | p. 6, l. 174 | "and a prior knowledge" | "and prior knowledge" | S4 |
| KK-10 | p. 6, l. 181 | "becomes Tarantola (2005):" | "becomes (Tarantola, 2005):" | S4 |
| KK-11 | p. 8, l. 236 | "considerately" | "considerably" | S4 |
| KK-12 | p. 8, l. 240 to 241 | "the model - here: our a posteriori erosion rate map - explains" | "the model, here our a posteriori erosion rate map, explains", with italics only on "a posteriori" | S4 |
| KK-13 | p. 9, l. 245 | "weighed by the model covariance" | "weighted by the model covariance" | S4 |
| KK-14 | Fig. 3c legend | "quarz pattern alignment" | "quartz pattern alignment" | AB |

#### Verification log

| ID | Check | Checked | Values | Result |
|---|---|---|---|---|
| PP-04 | P38 | Identifiers: unit names, mineral names, method acronyms, metric names, site names | Tuftgrat 2, Turftgrat 1 (Fig. 11 caption); Chrysotile 3, Chrysolite 1; NLLS 2, NNLS 2; quasi-Newton 2, Quasi-Newton 3, Quasi-Newtonian 1; Gorner site 5 variants; Zermatt-Saas Fee 5 variants; Monte Rosa gneiss unit 4 variants; the Steck et al. map of scenario 1 and the Fig. 4 map credited to Steck et al. are different objects (p. 11, l. 333: the Steck map has "the biggest area mismatch"), no conflict | findings GB-08, KK-01, KK-02, KK-05, KK-15, KK-16, KK-20, KK-24 |
| PP-05 | P10, P9, P19 | Design sketch (full table in instanz_SD.md) | framework: Bayesian inverse theory after Tarantola (2005); aim at p. 3, l. 63 to 64; three research aims at p. 10, l. 282 to 285; type: method development with synthetic tests and one field application; 7 units, 21 minerals, pixel 300 m (implicit), about 818 pixels (estimated, not stated); source samples per unit not stated; detrital samples "multiple" (number not stated) and one of 28 June 2019 (site not stated); controls: synthetic truth, zircon, absent unit; data classes: synthetic model-generated, XRD and zircon primary, geology secondary and inferred under ice, export estimate not given | basis for GB-01, 02, 07, 09, 10, 12, 23, 24, 27, 28, 34, 35 |
| PP-06 | P10 | Fit of the three research aims to the design | aim 1 descriptive, answered qualitatively; aim 2 comparative with one discriminating unit; aim 3 comparative, compared against zircon only | findings GB-23, GB-24, GB-30 |
| PP-07 | P32 | Results called confirmed or validated without an independent sample | "validate" p. 1, l. 3 and l. 8; p. 3, l. 69 and l. 74; p. 15, l. 451; "confirms" p. 14, l. 415; no independent check of fingerprints or erosion rates | covered by GB-23, GB-24 |
| PP-08 | P7, P30, P37 | Method versions and corrections against reported runs | only change: steepest descent gradient normalised after initial experiments (p. 11, l. 312 to 313), all reported steepest descent results after it; no corrected data shown in figures | no finding |
| PP-09 | P34 | Shown selection from a counted set | "multiple detrital samples" (p. 14, l. 413) pooled, not listed; Fig. 8 shows 14 of 20 runs | findings GB-16, GB-26 |
| PP-10 | P19 | Provenance class of key statements | Monte Rosa gneiss zircon fingerprint copied from the granite (disclosed p. 14, l. 433 to 434); geology under ice inferred (disclosed p. 9, l. 270 to 272); synthetic results model-generated (stated) | no finding |
| PP-11 | P36, P5 | Recollection against records; rules against own examples | no recollection statements; rule "below 25 ... fail to converge" (p. 13, l. 387) against runs with 25 iterations (p. 11, l. 324; p. 14, l. 426): rule met at its limit | no finding |
| PP-12 | P26, P27 | Guarantees and unchecked components | "should help cancel out such effects" (p. 15, l. 472 to 473) is hedged, no guarantee; unchecked geology under ice feeds A in every natural run (disclosed) | covered by GB-34, GB-35 |
| PP-13 | P9 | Proposed future studies in the outlook | land-use source maps and other tracers (p. 15, l. 466; p. 16, l. 487 to 489) proposed as possibilities without a study design | no finding |

### Segment 3: Results (p. 9 to 15, Figs. 4 to 16)

#### Substantive findings

**GB-11 Abbreviations and symbols in several legends are not resolved in the captions**

| Field | Content |
|---|---|
| Check | P29 |
| Location | Fig. 4 (legend "ELA estimation"); Fig. 5j, Fig. 15, Fig. 16 (legend "S.,T.,G."); Figs. 11, 13 to 16 ("ZSF", "MR"); Fig. 6b (hatched swatch without label); Fig. 6g (x axis without title) |
| Quotation | "Study area: location, land cover and geology." |
| Concern | "ELA", "S.,T.,G.", "ZSF" and "MR" are not spelled out in any caption; ZSF and MR are first expanded in the text at p. 14, l. 431 to 432, after Figs. 4, 5 and 11 are cited. In Fig. 6 the hatch symbol for low-confidence areas appears without its label, and panel g has no axis title. |
| Suggestion | Expand ELA, S.,T.,G., ZSF and MR in the captions of Figs. 4, 5, 11 and 13 to 16; add the missing label in Fig. 6b and the axis title "Iteration" in Fig. 6g. |
| Status | verified |
| Severity | minor |
| Source | AB |

**GB-12 The synthetic tests cannot fail in the ways the natural application can**

| Field | Content |
|---|---|
| Check | P9, P10, P3 |
| Location | p. 10, l. 288 to 295; p. 11, l. 324 to 326; p. 12, l. 372 to p. 13, l. 376; Fig. 5a; Fig. 10 (first row) |
| Quotation | "we generate synthetic detrital data using the forward model applied to a “true” erosion rate map featuring a localised hotspot" |
| Concern | The synthetic programme is systematic, but data are generated with the same forward model, tracer matrix and (except scenario 1) map as used for the inversion, with no stated noise, and the prior is "equal to the average true erosion rate" (p. 10, l. 295), known only because the truth is. The true map is a single smooth bump. Measured in Fig. 10, first row (calibration points 250 at 635.5 px and 75 at 905.5 px, ±0.65): the error falls monotonically over 20 markers from about 257 to 76.0 at the largest tested L = 3000 m, against 194.9 near the L = 1200 m used in all tests; this reflects the smooth truth rather than a general optimum. The text says the solution deviates "beyond approximately 10 times the pixel size (3000 m)", outside the tested range. The hyperparameters (25 iterations, μ = 0.1) were chosen by error against the truth and then transferred to the natural data. |
| Suggestion | Add synthetic cases with noise drawn from replicate XRD measurements, several and non-smooth hotspots, a prior that differs from the true mean, and fingerprints mixed in raw peak-area space; choose hyperparameters by a criterion available for natural data (trade-off curve, cross-validation on tracers); extend the L sweep beyond 3000 m or delete the claim at p. 12, l. 373 to p. 13, l. 374, and explain why L = 1200 m was used. |
| Status | verified (design statements, measured sweep); inferred (consequences) |
| Severity | major |
| Source | SD, AB |

**GB-13 Fig. 5c shows the posterior overshooting the hotspot by about 2 mm/y, which the text describes as a close match**

| Field | Content |
|---|---|
| Check | P3 |
| Location | p. 10, l. 296 to 298; Fig. 5c; Fig. 5a; Fig. 5b; p. 16, l. 482 |
| Quotation | "The primary differences occur within larger lithological units" |
| Concern | The text says the quasi-Newton map "closely matches the true erosion pattern, both in spatial distribution and magnitude" (p. 10, l. 296 to 297). In Fig. 5c (true minus posterior) the cells at the centre of the hotspot measure −2.2 (closest colour-bar match, calibration points 2 at 657.5 px and −2 at 903 px, colour distance 38 because of the hillshade, so the value lies between −2.2 and the bar end −2.38). The true map tops out at 3.0 (colour bar of Fig. 5a). The posterior therefore exceeds the true peak by about 2.2 mm/y, about 73 % of the peak (2.2/3.0), and the largest difference sits at the hotspot inside the small elliptical unit, not within the larger units. Fig. 5b cannot show this because its colour bar saturates at 3.0. |
| Suggestion | Report the true and posterior peak values and the maximum absolute difference at p. 10, l. 296 to 298; extend the colour bar of Fig. 5b to the posterior maximum; restate the claim of reliable recovery at p. 16, l. 482. |
| Status | verified (measured colour); inferred (posterior peak and ratio) |
| Severity | major |
| Source | AB |

**GB-14 The resolution maps show values the stated resolution operator cannot take**

| Field | Content |
|---|---|
| Check | P3 |
| Location | p. 10, l. 300; Fig. 5d; Figs. 14, 15 and 16 (resolution diagonal); p. 8, l. 230 to 236; p. 16, l. 483 to 484 |
| Quotation | "Where the diagonal of R is close to 1, data have improved our knowledge considerately relative to the prior." |
| Concern | The colour bar of Fig. 5d runs from 0.90 to 1.00, so every pixel has a resolution diagonal of at least 0.90; Figs. 14 to 16 use 0.5 to 1.0 and 0.80 to 1.00 with most of the map at the dark end. R maps the true model onto the estimate through the data (eq. 21); for a linearised problem its trace cannot exceed the number of independent data, here 21 tracers (13 age bins for zircon, 34 combined), because A has "more columns than rows" (p. 6, l. 172). The catchment in Fig. 4 measures about 73.6 km² (890750 coloured pixels at 110 ± 2 pixels per km on the scale bar), that is about 818 pixels of 300 m. A diagonal of at least 0.90 everywhere gives a trace of at least 736 against a bound of 21; the mean diagonal could be at most 21/818 = 0.026. The maps also disagree with the normalised posterior covariance of the same run (Fig. 5f 0.4 to 0.9, trace ratio 0.74 in Fig. 5h). The conclusion uses these maps "to assess the reliability of inferred erosion patterns" (p. 16, l. 483 to 484). |
| Suggestion | Give the formula used for R in Section 3.3, check the computation against the trace bound, and replot Figs. 5d, 14, 15 and 16; if a different quantity is shown, rename it in the figures and at p. 10, l. 300. |
| Status | verified (colour bar ranges, map extent measured); inferred (trace bound and pixel count) |
| Severity | major |
| Source | AB |

**GB-15 The stated monotonic effect of map mismatch is contradicted by the next sentence**

| Field | Content |
|---|---|
| Check | P15 |
| Location | p. 11, l. 337 to 339; p. 12, l. 340 to 342; Fig. 7 |
| Quotation | "the greater the mismatch between the geological map used in the inversion and the one used to generate the synthetic data, the larger the discrepancy between the posterior and true erosion rate maps" |
| Concern | The next sentence reports that the map "with minimal changes from the truth results in a more accurate posterior erosion map than the original geological map itself"; measured in Fig. 7 (calibration points 270 at 1070.5 px and 220 at 1370.5 px, ±0.17): 193.6 for the minimal changes against 197.5 for the original and 274.8 for the Steck et al. map. With three maps and one non-monotonic step the general statement is not supported. |
| Suggestion | Replace the sentence at p. 11, l. 337 to 338 by the observed result for the three maps, or test more maps with graded mismatch. |
| Status | verified |
| Severity | minor |
| Source | S4 |

**GB-16 Fig. 8 shows 14 of the 20 tested blending levels, but the caption accounts for one missing**

| Field | Content |
|---|---|
| Check | P3, P23 |
| Location | p. 12, l. 348 to 349; p. 12, l. 353; Fig. 8 (left and middle scatterplots, caption) |
| Quotation | "Note that the most blended example did not have a stable solution and is therefore not plotted." |
| Concern | Counted at the enlarged 300 dpi crop: 14 markers in the left scatterplot (4 between JS 0.25 and 0.36, 10 between 0.44 and 0.62) and 14 in the middle one. The text tests "20 values" (p. 12, l. 348); minus the one excluded in the caption this leaves 19, so 5 are missing without explanation (20 − 1 − 14 = 5). The text adds "In many of these cases, the inversion fails to converge" (p. 12, l. 353), which suggests further non-converged runs were dropped; there are no markers between JS 0.36 and 0.44. |
| Suggestion | State in the caption of Fig. 8 how many of the 20 runs converged, which were dropped and why, and show the dropped runs as open symbols at their JS value. |
| Status | verified (counted) |
| Severity | moderate |
| Source | AB, S3 |

**GB-17 The text states an error threshold in mm/yr that does not match the scale or the unit of the plotted error**

| Field | Content |
|---|---|
| Check | P2, P20 |
| Location | p. 12, l. 351 to 353; Fig. 8 (left scatterplot); Fig. 5g; Figs. 7, 9 and 10 (first column) |
| Quotation | "with errors exceeding 700 mm/yr for JS < 0.44" |
| Concern | The plotted error is the sum over all pixels of the absolute difference between true and posterior rate, with no unit on any axis. Its baseline is about 197 (Figs. 7 and 9) for a true map with values up to 3 mm/y (Fig. 5a), so it is not a rate in mm/yr. Fig. 8 runs to 700000 on this axis; measured (calibration points 0 at 1395.5 px and 700000 at 891.5 px, ±1400): the points between JS 0.44 and 0.54 reach up to about 19700, already far above 700 in the axis unit, and the point at JS 0.34 lies at about 6100, below that at 0.54. The number of pixels that would convert the sum into a mean rate is not given; it has to be estimated from the map (about 818 pixels of 300 m). |
| Suggestion | Define the error metric in Section 4.1 with its unit and the number of pixels, or report the mean absolute error per pixel in mm/y; correct the threshold at p. 12, l. 352 to 353 to a value read from Fig. 8 in the same unit. |
| Status | verified (wording, axis labels, measured values); inferred (pixel count) |
| Severity | moderate |
| Source | S3, AB |

**GB-18 Fig. 9 labels the tracer-count axis as JS distance**

| Field | Content |
|---|---|
| Check | P29 |
| Location | Fig. 9 (left and middle scatterplots, colour bar); p. 12, l. 357 |
| Quotation | "Avg. JS distance between lithologies" |
| Concern | The x axes run from 0.0 to 20.0, the number of tracers (labels "1 tracer", "11 tracers", "All"), but carry the JS label copied from Fig. 8. The colour bar reads "Number of tracrs". |
| Suggestion | Relabel both x axes of Fig. 9 "Number of tracers" and correct the colour bar label. |
| Status | verified |
| Severity | minor |
| Source | AB |

**GB-19 The ranking of the three degradation scenarios does not follow from the plotted errors**

| Field | Content |
|---|---|
| Check | P21 |
| Location | p. 12, l. 363 to 365; Fig. 7; Fig. 9 |
| Quotation | "Geological map uncertainty follows as the second most influential factor." |
| Concern | Measured on the same error axis: the largest map mismatch (Steck et al. map) gives 274.8 against 197.5 for the original map (Fig. 7), an increase of 77. Reducing the tracers gives 293.5 and 296.5 with 3 and 4 tracers and 347.3 with 1 tracer against 197.4 with 7 or more (Fig. 9, calibration points 340 at 948.5 px and 200 at 1399.5 px, ±0.31), increases of 96 to 150. Tracer reduction below 5 therefore has a larger effect than any tested map error. The ranking depends on how far each scenario was pushed (three maps, 21 tracer counts, 20 blending levels), with no common scale of degradation. |
| Suggestion | Rank the scenarios at p. 12, l. 363 to 365 only for stated, comparable degradation levels, or drop the ranking and report the error range of each scenario. |
| Status | verified (measured values); inferred (differences) |
| Severity | moderate |
| Source | S3, AB |

**GB-20 Markers in Fig. 10 name parameter values that differ from those used and are not explained**

| Field | Content |
|---|---|
| Check | P29, P3 |
| Location | Fig. 10 (third column, rows 1 to 5); p. 12, l. 371; p. 10, l. 294 to 295; p. 11, l. 324 to 326 |
| Quotation | "σm = 6.2" |
| Concern | The trade-off panels highlight one point per row with the labels "L = 3000 m", "σm = 6.2", "σd = 0.003 mm/y", "μ = 0.1" and "n_m = 25" (vector text read from the PDF). The tests use L = 1200 m, σm = 3 and σd = 0.01 mm/y (p. 11, l. 324 to 326). The caption does not say what the highlighted points mean (optimum, corner of the trade-off curve, chosen value). |
| Suggestion | Explain the highlighted points in the caption of Fig. 10 and either mark the values actually used or explain why they differ from the highlighted ones. |
| Status | verified |
| Severity | moderate |
| Source | AB |

**GB-21 Text in Fig. 10 is set at about 3.5 to 4 pt**

| Field | Content |
|---|---|
| Check | P29 |
| Location | Fig. 10 (all 15 panels) |
| Quotation | "Data standard deviation (mm/y)" |
| Concern | Measured at 600 dpi: cap height of "D" in the axis title "Data" 24 px, giving 24 × 72/600/0.72 = 4.0 pt; height of the tick label digits "0.040" 21 px, giving 3.5 pt. Both are below 6 pt at print size. |
| Suggestion | Split Fig. 10 over two pages or enlarge the fonts to at least 6 pt. |
| Status | verified (measured) |
| Severity | minor |
| Source | AB |

**GB-22 Fig. 10 shows almost no effect of the data standard deviation, whereas the text describes large differences, a minimum and a plateau**

| Field | Content |
|---|---|
| Check | P3 |
| Location | p. 13, l. 380 to 384; Fig. 10 (third row, first and second column) |
| Quotation | "Very low data standard deviation values lead to large differences between the posterior and true erosion rate maps" |
| Concern | The y axis carries the offset "+1.974e2". Measured (calibration points 0.020 at 1680.0 px and 0.040 at 1442.0 px, ±0.00008): the total absolute difference rises monotonically from 197.4201 at the smallest σd to 197.4431 at σd of about 0.89 mm/y, a change of 0.023, or 0.012 % of the value. There is no large difference at low σd, no minimum and no plateau. The normalised uncertainty in the same row varies only between 0.74015 and 0.74040. |
| Suggestion | Rewrite p. 13, l. 380 to 384 to state that σd has no material effect over the tested range, or extend the sweep to the range where the described behaviour occurs and show it. |
| Status | verified (measured) |
| Severity | moderate |
| Source | AB |

**GB-23 The agreement of the XRD fingerprints with the known lithology is asserted, not tested**

| Field | Content |
|---|---|
| Check | P31, P3 |
| Location | p. 13, l. 399 to 401; Fig. 11; p. 10, l. 274 to 276; p. 10, l. 282 to 283 |
| Quotation | "The mineralogical fingerprints derived from processed and binned XRD data align well with established knowledge of the lithology" |
| Concern | Aim 1 (p. 10, l. 282 to 283) is answered by this one sentence without a comparison. Measured bars in Fig. 11 (relative to the longest bar per column, 244 px = 1, ±0.004): almandine reaches 0.037 in "Monte Rosa (gneiss, micaschist)", a unit the manuscript describes with "garnet-mica schists" (p. 10, l. 276) and labels "garnet gneiss and micaschist" in Fig. 4; in the "ZSF ophiolites (metabasites, eclogites)" almandine is 0.098 and omphacite 0.053, while the generic "Pyroxene" window reaches 1.000. Is the omphacite signal absorbed by the pyroxene window, and why is garnet nearly absent from the garnet-bearing units? The robustness of "the cleaning and binning approach" (p. 13, l. 400 to 401) does not follow from a qualitative look. |
| Suggestion | Compare the binned XRD values at p. 13, l. 399 to 401 with an independent estimate (point counting of thin sections, Rietveld quantification of a subset, or published modal compositions) and report the agreement per mineral and unit; discuss the garnet and omphacite values of Fig. 11. |
| Status | verified (measured bars, wording); assumption (which values are to be expected) |
| Severity | major |
| Source | SD, AB |

**GB-24 The known mixture test rests on one absent unit, and an absent and a present unit look the same**

| Field | Content |
|---|---|
| Check | P10, P31 |
| Location | p. 14, l. 410 to 418; Fig. 13; p. 1, l. 8; p. 15, l. 451 |
| Quotation | "the overall pattern confirms that the inversion respects geological boundaries when the XRD fingerprints provide sufficiently distinct signals" |
| Concern | Using a subcatchment as a natural analogue of a known mixture is a sensible idea, but six of the seven units crop out in it (p. 14, l. 411), so the test can fail only on one unit, the ZSF sediments, which the synthetic tests already identify as a small unit with low resolution (p. 10, l. 299 to 300). Measured in Fig. 13 (x axis from label centres 0.0 at 545.8 px and 3.0 at 1876.7 px, ±0.007): the KDE peak of the absent ZSF sediments lies at −0.002 mm/y and that of the present Furgg series at 0.000 mm/y; the test does not separate absence from presence. Erosion attributed to pixels outside the subcatchment is not evaluated, and the area share of each unit inside the subcatchment is not given. On this basis the abstract says the application "further validates the practical utility and robustness of the model" (p. 1, l. 8). |
| Suggestion | Compare, per unit, the posterior sediment contribution with the unit's area share inside the subcatchment, report the posterior erosion outside the subcatchment, and add a laboratory known-mixture test with source powders mixed in set proportions; tone down p. 1, l. 8 and p. 15, l. 451 to "is consistent with". |
| Status | verified (measured peaks, wording); inferred (discriminating power) |
| Severity | major |
| Source | SD, AB, S4 |

**GB-25 Fig. 12 does not show the subcatchment boundary that the test depends on, and Fig. 13 has no density scale for six units**

| Field | Content |
|---|---|
| Check | P29 |
| Location | Fig. 12; Fig. 13 (upper panel); p. 14, l. 412 |
| Quotation | "Lithology and outcrops in the Gorner-Grenz confluence subcatchment." |
| Concern | Fig. 12 shows the whole catchment with some areas in saturated and others in faded colours; neither the subcatchment boundary nor the meaning of the fading is given in legend or caption. Fig. 13 draws the boundary as a dashed line in its inset. The upper panel of Fig. 13 stacks six KDEs on a "Density" axis without values; only the lower panel has a scale (0 to 2). |
| Suggestion | Draw the subcatchment boundary in Fig. 12 and explain the faded colours; give each KDE in Fig. 13 a density scale or state that all curves share one. |
| Status | verified |
| Severity | minor |
| Source | AB |

**GB-26 The number of detrital samples behind the known mixture test is not given, and Fig. 13 pools pixels and inversions**

| Field | Content |
|---|---|
| Check | P20, P11, P34 |
| Location | p. 14, l. 413 to 414; Fig. 13 caption |
| Quotation | "Merging the inversion results from multiple detrital samples collected at the sink of this sub-catchment" |
| Concern | Neither text nor caption says how many samples were inverted, on which dates, or with which parameters. The KDE "integrates results from all inversions" over "all pixels within each lithological unit", so the unit of analysis is pixel times inversion; "a taller peak indicates greater consistency across inversions" cannot be separated from spatial variation within a unit. |
| Suggestion | State at p. 14, l. 413 the number of samples, their dates and the inversion parameters; show the per-sample mean erosion rate per unit next to the pooled KDE in Fig. 13. |
| Status | verified |
| Severity | moderate |
| Source | S3, SD |

**GB-27 Erosion rates in mm/y are derived from one instantaneous sample whose site is not given**

| Field | Content |
|---|---|
| Check | P9 |
| Location | p. 14, l. 423 to 424 and l. 437 to 438; p. 9, l. 267 to 268; p. 3, l. 65 to 66 |
| Quotation | "the detrital sample collected on June 28, 2019, at 13:30" |
| Concern | The zircon, XRD and combined maps (Figs. 14 to 16) come from a single sample taken at one moment, scaled with an annual export estimate into mm/y. The site is chosen for its "multi-year suspended sediment datasets" (p. 9, l. 268), but only one date is used, and it is not said whether the sample comes from the catchment outlet or from the Gorner-Grenz confluence; the hotspots in the south-west (Figs. 14 and 15) lie outside the Gorner-Grenz subcatchment drawn in Fig. 13. |
| Suggestion | State the sampling site of the 28 June 2019 sample at p. 14, l. 423; either label Figs. 14 to 16 as instantaneous source contributions or derive annual maps from samples spread over the melt season. |
| Status | verified (single sample, missing site); inferred (temporal mismatch) |
| Severity | moderate |
| Source | SD |

**GB-28 The prior for the natural inversion is set to a "true" rate that does not exist**

| Field | Content |
|---|---|
| Check | P25 |
| Location | p. 14, l. 426 to 428 |
| Quotation | "a prior equal to the average true erosion rate" |
| Concern | For natural data there is no true map; the parameter list of the synthetic tests (p. 11, l. 325 to 326) appears to have been carried over. The prior used for Figs. 13 to 16 is therefore unknown, although it controls the posterior where the data are weak (Fig. 5d to f). |
| Suggestion | State at p. 14, l. 428 the prior actually used, with its value and derivation (for example the annual export estimate divided by catchment area). |
| Status | verified |
| Severity | moderate |
| Source | SD, S3 |

**GB-29 The zircon fingerprints contain no serpentinite signal, yet the zircon hotspot in the serpentinites is read as source activation**

| Field | Content |
|---|---|
| Check | P3, P15 |
| Location | p. 14, l. 439 to 440; Fig. 14 (source fingerprints and posterior map); p. 14, l. 432 to 433 |
| Quotation | "While both datasets indicate sediment source activation in the serpentinite-rich region in the southwest" |
| Concern | The text discloses the low zircon content of the serpentinites (p. 14, l. 432 to 433). Colour count over the bar panel of Fig. 14: orange 27.9 %, light orange 25.4 %, pink 25.4 %, light green 10.9 %, olive 8.0 %; pixels within colour distance 40 of the serpentinite yellow of Fig. 15: 290 of 558000 (0.05 %, edge pixels). No age bin carries a serpentinite or metabasite share. With a zero column in A the zircon data cannot inform erosion in that unit, so the extreme value above 8000 mm/y there is not evidence of activation; it is the part of the solution the zircon data do not constrain. |
| Suggestion | Remove the zircon solution as support at p. 14, l. 439 to 440, or show that the serpentinite unit has a non-zero zircon fingerprint; mark units without fingerprint signal as unconstrained in Fig. 14. |
| Status | verified (colour count); inferred (consequence for the inversion) |
| Severity | moderate |
| Source | AB, SD |

**GB-30 Combining zircon with XRD is presented as an improvement, but the combined solution is less certain than XRD alone**

| Field | Content |
|---|---|
| Check | P15 |
| Location | p. 15, l. 446 to 449; p. 3, l. 72 to 73; p. 5, l. 139 to 140; p. 10, l. 284 to 285; p. 15, l. 461 to 463 |
| Quotation | "Adding XRD data to the zircon dataset stabilizes the inversion and improves the posterior solution." |
| Concern | The comparison is made against zircon alone (0.87 to 0.86, a change of 1.1 %). Against XRD alone, the method the paper proposes, the combination raises the normalised posterior uncertainty from 0.82 to 0.86 (plus 4.9 %; Figs. 15 and 16), and the colour bar maximum of the erosion map rises from 8 to 12 mm/y. The introduction says integrating XRD with zircon "improves the stability and sharpness of the posterior solution" (p. 3, l. 72 to 73), the discussion that combining "proves to further stabilize and improve the posterior solution" (p. 15, l. 461 to 463). By the manuscript's own metric, aim 3 (p. 10, l. 284 to 285) is answered for adding XRD to zircon, not for adding zircon to XRD; stability and sharpness are not quantified. |
| Suggestion | Report the comparison against XRD alone at p. 15, l. 446 to 449, state that the combination does not reduce the normalised uncertainty relative to XRD alone, and rephrase p. 3, l. 72 to 73 and p. 15, l. 461 to 463 accordingly; if stability is meant, define and report a measure of it, for example the spread of posteriors over repeated detrital samples. |
| Status | verified (values); inferred (percentages) |
| Severity | major |
| Source | S4, S3 |

**GB-31 The JS distance is reported for the zircon and the combined fingerprints but not for the XRD fingerprints**

| Field | Content |
|---|---|
| Check | P11 |
| Location | p. 15, l. 446 to 448; p. 15, l. 441 to 442; p. 12, l. 351 to 353 |
| Quotation | "the average Jensen-Shannon distance between source fingerprints increases from 0.48 to 0.57" |
| Concern | The synthetic tests place the change in behaviour near JS 0.55 (p. 12, l. 352). For the three natural cases the manuscript gives the normalised uncertainty for each (0.87, 0.82, 0.86) but the JS distance only for zircon (0.48) and for the combination (0.57). Without the XRD value the reader cannot place the XRD-only case, the method of the paper, on the synthetic curve of Fig. 8. |
| Suggestion | Add the average JS distance of the XRD fingerprints at p. 15, l. 441 to 442 and mark the three natural cases on the x axis of Fig. 8. |
| Status | verified |
| Severity | moderate |
| Source | S3 |

#### Minor corrections

| ID | Location | Quotation | Replacement | Source |
|---|---|---|---|---|
| KK-15 | p. 9, l. 267; p. 13, l. 392; p. 15, l. 463; Fig. 11 caption | "Gorner-gletscher catchment" | one name throughout, for example "Gornergletscher catchment" (counted: Gorner-gletscher 2, Gornergletscher 2, Gorner Glacier 4, Gorner gletscher 1, Gorner glacier 2) | S2 |
| KK-16 | Fig. 4 and Fig. 12 legends | "biotite schits" | "biotite schists"; also "calcarious" to "calcareous", "caclcite-zoisite" to "calcite-zoisite", "silimanite" to "sillimanite", "GornergratPermo-Mesozoic" to "Gornergrat Permo-Mesozoic" | AB |
| KK-17 | p. 10, l. 299; p. 12, l. 340; p. 14, l. 411 and l. 414; Fig. 12 caption | "Zermatt Saas-Fee sediments" | one spelling throughout, for example "Zermatt-Saas Fee" (counted: 5 variants, 8 occurrences, including "Zermatt- Saas Fee" in the caption of Fig. 12) | S2, AB |
| KK-18 | p. 11, l. 317 | "(Figure 6G versus Figure 6G)" | "(Figure 6H versus Figure 6G)", or the intended pair | S4 |
| KK-19 | Fig. 7, title of the left map | "Originial geology (same as forward)" | "Original geology (same as forward)" | AB |
| KK-20 | Fig. 10, first row, second panel x axis and colour bar | "Smooting distance (m)" | "Smoothing distance (m)" | AB |
| KK-21 | p. 13, l. 384 | "approximately 10-2 mm/y" | "approximately 10^−2 mm/y" with superscript exponent, as at l. 388 | S3 |
| KK-22 | p. 13, l. 395 | "Chrysolite" | "Chrysotile", as at p. 10, l. 274 and in Figs. 11, 15 and 16 | S2 |
| KK-23 | Fig. 11 caption | "Stockhorn-Turftgrat-Gornergrat" and "ecologites" | "Stockhorn-Tuftgrat-Gornergrat" and "eclogites" | AB |
| KK-24 | p. 13, l. 400 | "supporting the 1) the robustness" | "supporting 1) the robustness" | S4 |
| KK-25 | p. 14, l. 420 to 421 and l. 437 to 438 | "applied to the same detrital sample" | one formulation: either the same sample was split for zircon and XRD, or two samples were taken at the same time | SD |
| KK-26 | Figs. 14, 15 and 16 legends | "Low-con dence area" | "Low-confidence area" (the ligature fi is missing in the rendered text) | AB |
| KK-27 | p. 14, l. 432; Figs. 11, 13, 15 and 16 | "Monte Rosa garnet-gneiss (MR g-g)" | one unit name matching the legend of Fig. 4, "Monte Rosa (garnet gneiss and micaschist)", with one abbreviation | S2 |
| KK-28 | Fig. 15 and Fig. 16 legends | "ZSF serpentinites" | move the swatch of "ZSF metabasites" so that it does not overlap the label (Fig. 15), and keep the first legend row inside the figure (Fig. 16, top row cut by the map) | AB |

#### Verification log

| ID | Check | Checked | Values | Result |
|---|---|---|---|---|
| PP-14 | P29, P3 | Inventory of figures | Fig. 1 p. 22 schema, 4 panels, first cited p. 5, l. 146; Fig. 2 p. 23 schema, 3 panels, p. 6, l. 166; Fig. 3 p. 24 schema, 5 panels, p. 9, l. 251; Fig. 4 p. 25 map with insets, p. 9, l. 268; Fig. 5 p. 26, 11 panels, p. 10, l. 289; Fig. 6 p. 27, 9 panels, p. 11, l. 315; Fig. 7 p. 28, p. 11, l. 334; Fig. 8 p. 29, p. 12, l. 347; Fig. 9 p. 30, p. 12, l. 357; Fig. 10 p. 31, 15 panels, p. 12, l. 371; Fig. 11 p. 32, 7 columns × 21 minerals, p. 13, l. 398; Fig. 12 p. 33, p. 14, l. 412; Fig. 13 p. 34, p. 14, l. 414; Fig. 14 p. 35, 13 age bins, p. 14, l. 429; Fig. 15 p. 36, 21 minerals, p. 14, l. 438; Fig. 16 p. 37, 34 bars, p. 15, l. 445; numbers 1 to 16 consecutive, all cited; no graphical abstract, no appendix figures | inventory complete |
| PP-15 | P1 | Derived numbers | 21 minerals listed at p. 13, l. 394 to 396: counted 21; tracer range 1 to 21 (p. 12, l. 358) matches; L = 4 × pixel = 1200 m and 10 × pixel = 3000 m give a pixel of 300 m in both places; 0.87 to 0.86 is a decrease of 1.1 %; 0.82 to 0.86 an increase of 4.9 %; JS 0.48 to 0.57 an increase of 0.09 | no finding |
| PP-16 | P2 | Quantities stated more than once | normalised uncertainty 0.87 (p. 14, l. 436; Fig. 14), 0.82 (p. 15, l. 442; Fig. 15), 0.86 (p. 15, l. 447; Fig. 16): equal; extreme erosion "above 8000 mm/y" (p. 14, l. 435) against the Fig. 14 colour bar top 8000: consistent; parameter sets at p. 10, l. 293 to 295, p. 11, l. 324 to 326 and p. 14, l. 426 to 428: equal except iterations (100, 25, 25) and step size (stated only from l. 326); the abstract states no numbers | finding GB-17 only |
| PP-17 | P11 | Cases against announced analyses | synthetic: quasi-Newton and steepest descent each with maps and iteration curves (Figs. 5, 6): complete; scenarios 1 to 3 each with error, uncertainty and trade-off (Figs. 7 to 9): complete; sweeps of 5 parameters × 3 metrics (Fig. 10): complete; natural aims 1 to 3: aim 1 qualitative (Fig. 11), aim 2 (Fig. 13), aim 3 with uncertainty for three cases and JS for two of three | findings GB-23, GB-31 |
| PP-18 | P22 | Implicit counts | pixel size only implicit (p. 10, l. 294); pixel count not stated; number of detrital samples in Section 4.2.1 not stated | findings GB-17, GB-26 |
| PP-19 | P23 | Balances | scenario 2: 20 values tested, 1 not plotted, 14 plotted; no other balances | finding GB-16 |
| PP-20 | P3 | Fig. 7 against p. 11, l. 337 to p. 12, l. 342 | error: original 197.5, minimal changes 193.6, Steck et al. 274.8 (±0.17); trace: 0.7401, 0.7376, 0.746; data misfit 3.26, 3.49, 3.68 × 10^6; model misfit 1.56, 1.92, 2.46: both misfits rise with mismatch as stated | consistent except the monotonic claim (GB-15) |
| PP-21 | P3 | Fig. 8 against p. 12, l. 351 to 353 | error: JS 0.44 to 0.54 from about 0 to 19700, JS 0.34 about 6100, JS 0.36 about 321900 (±1400); posterior uncertainty jumps from about 0.84 at JS 0.54 to about 0.75 at JS 0.56 | finding GB-17; the uncertainty jump below 0.55 confirmed |
| PP-22 | P3 | Fig. 9 against p. 12, l. 360 to 362 | 1 tracer 347.3, 2 tracers 348.5, 3 and 4 tracers 293.5 and 296.5, 5 tracers 224.1, 6 tracers 205.2, 7 and more about 197.4 (±0.31) | text consistent ("7 tracers ... approximately the same") |
| PP-23 | P3 | Fig. 10, first row against p. 12, l. 372 to p. 13, l. 376 | 20 markers; 206.6 and 194.9 near L = 1100 to 1250 m, 76.0 at L = 3000 m (±0.65); monotonic decrease to the end of the tested range | finding GB-12 |
| PP-24 | P3 | Fig. 13 KDE peaks | Furgg series 0.000 ± 0.007 mm/y; ZSF sediments −0.002 ± 0.007 mm/y | finding GB-24 |
| PP-25 | P3 | Fig. 11 bar lengths, normalised to the longest bar per column (±0.004) | almandine: ZSF serpentinites 0.004, ZSF sediments 0.029, S-T-G 0.090, MR granite 0.037, ZSF metabasites 0.098, MR gneiss 0.037, Furgg 0.041; omphacite in ZSF metabasites 0.053; pyroxene in ZSF metabasites 1.000; quartz in MR gneiss 1.000; tremolite in MR granite 0.893 | finding GB-23 |
| PP-26 | P3 | Fig. 6h against p. 11, l. 316 | after about 135 iterations the markers form a doubled band, consistent with an oscillation between two values | no finding |
| PP-27 | P24 | Dated events in figures | the only dated event is the detrital sample of 28 June 2019, 13:30 (p. 14, l. 423 to 424); no figure has a time axis or date | not applicable |
| PP-28 | P29 | Font sizes outside Fig. 10 | Figs. 14 to 16 "Geology" 7.0 to 7.3 pt; Fig. 11 "Albite" 6.3 pt; Figs. 1 to 9 and 11 to 16 checked at 300 dpi, no text smaller than in Fig. 10 | only Fig. 10 below 6 pt (GB-21) |

### Segment 4: Discussion, conclusion, references, statements (p. 15 to 21)

#### Substantive findings

**GB-32 The novelty claim of a non-linear mixing model conflicts with the forward model**

| Field | Content |
|---|---|
| Check | P15 |
| Location | p. 15, l. 454 to 455; p. 5, l. 157 to 158; p. 6, eq. 3; p. 2, l. 58 to 60 |
| Quotation | "and in the incorporation of non-linear mixing model" |
| Concern | Eq. 3 writes the data as d = A · exp(ε), linear in the erosion rates ė = ė0 exp(ε); the text says log space is chosen "to impose a positivity constraint, hence making this non-linear" (p. 5, l. 157 to 158). The mixing stays linear, a weighted average of source concentrations (p. 5, l. 151 to 152); only the parametrisation is non-linear. The introduction contrasts the method with approaches that "implicitly rely on a linear mixing scheme" (p. 2, l. 59). One of the two stated novelties therefore describes the inversion, not the mixing. |
| Suggestion | Rephrase p. 15, l. 455 and p. 2, l. 59 to 60 as "a linear mixing model inverted in log space to enforce positive erosion rates", or state which non-linear mixing effect the model represents. |
| Status | verified |
| Severity | moderate |
| Source | S4, S1 |

**GB-33 Two factors in the discussion are stated as results although no test varied them**

| Field | Content |
|---|---|
| Check | P15 |
| Location | p. 15, l. 457 to 458; p. 15, l. 460 to 461; p. 16, l. 484 to 485 |
| Quotation | "A higher number of distinct source areas leads to higher posterior resolution and lower uncertainty." |
| Concern | None of the synthetic tests changes the number of source areas: scenario 1 varies map geometry with the same seven units, scenario 2 blending, scenario 3 the number of tracers (p. 11, l. 327 to p. 12, l. 362). The conclusion repeats it as a condition for use, "multiple mineralogically distinct source areas" (p. 16, l. 485). The preceding sentence, "Including a broad set of tracer minerals further improves model stability and resolution" (p. 15, l. 457 to 458), conflicts with scenario 3, where 7 tracers give "approximately the same posterior solution as with the full tracer set" (p. 12, l. 360); resolution was not reported for any scenario. |
| Suggestion | Either add a synthetic test that varies the number of source units at constant JS distance, or mark the statement at p. 15, l. 460 to 461 as an expectation; restate p. 15, l. 457 to 458 as "at least about seven informative tracers", in line with p. 12, l. 360. |
| Status | verified |
| Severity | moderate |
| Source | S4 |

**GB-34 The field site does not meet the manuscript's own first condition for use**

| Field | Content |
|---|---|
| Check | P18 |
| Location | p. 15, l. 463 to 466; p. 9, l. 270 to 272; p. 12, l. 363 to 364 |
| Quotation | "we recommend applying this method in catchments where: a) the spatial distribution of source lithologies is well constrained" |
| Concern | In the Gornergletscher catchment the lithology under the ice is inferred "based on regional geological knowledge" (p. 9, l. 270 to 272), and map uncertainty is called the second most influential factor (p. 12, l. 363 to 364). The natural results are not discussed in the light of condition a), nor of condition b), the zircon JS of 0.48 lying below the 0.55 at which the synthetic uncertainty rises (p. 12, l. 352). |
| Suggestion | Discuss in Section 5 how far the Gornergletscher meets conditions a) and b), and what the scenario 1 results imply for the natural maps. |
| Status | verified |
| Severity | moderate |
| Source | SD |

**GB-35 The XRD limitations are disclosed only in the discussion**

| Field | Content |
|---|---|
| Check | P17 |
| Location | p. 15, l. 469 to 476; p. 9, l. 250 to 265 |
| Quotation | "Several limitations associated with raw XRD data should also be considered." |
| Concern | The limitations are named and referenced, but grain-size effects, preferred orientation of micas and peak overlap bear on every fingerprint and appear only at the end of the discussion, not in Section 3.4 where the XRD processing is introduced. The detrital samples are suspended fine sediment and the sources powdered rock, so equal preparation does not by itself remove grain-size differences between them; this is not discussed. |
| Suggestion | Move the limitations to Section 3.4 and state there how the grain size of detrital and source powders was controlled. |
| Status | verified |
| Severity | moderate |
| Source | SD |

**GB-36 The data availability statement covers "the inversion tests" but not several data sources the methods rely on**

| Field | Content |
|---|---|
| Check | P12 |
| Location | p. 16, l. 490; p. 14, l. 423 to 424; p. 17, l. 522 to 523; Fig. 4 (credit line); p. 9, l. 251 to 258; p. 15, l. 452 to 454 |
| Quotation | "The data and codes used for the inversion tests in the study are available at https://doi.org/10.5281/zenodo.17120374" |
| Concern | A DOI-based deposit is provided. The methods, however, use at least eight data sources: source rock diffractograms; detrital diffractograms of the Gorner-Grenz samples and of the sample of 28 June 2019; zircon U-Pb ages produced "following the methodology described in (Belotti, 2021)", an "unpublished master's thesis" (p. 17, l. 522 to 523); the inferred geological map, credited in Fig. 4 to "data from Steck et al., 2015, personal communication by L. Baumgartner"; the modified maps of scenario 1; the 2θ windows per mineral from RRUFF (p. 9, l. 257); the annual export estimate, a required input whose value is not given; the synthetic fingerprints and true map. The statement names none of these items, and "inversion tests" may or may not include raw diffractograms, zircon ages, the map and the export estimate. The Zenodo record could not be opened (rate limited), so its reachability and content were not checked. |
| Suggestion | List each item above in the statement at p. 16, l. 490 with its location (repository file or reason for withholding); deposit the zircon ages and the geological map raster, or cite where they are published; give the annual export value and its source in Section 3 or 4.2. |
| Status | verified (statement wording, missing value, unpublished thesis, credit line); content of the Zenodo record not checked |
| Severity | moderate |
| Source | S2 |

#### Minor corrections

| ID | Location | Quotation | Replacement | Source |
|---|---|---|---|---|
| KK-29 | p. 18, l. 567 | "oCLC: 1402659188" | "OCLC: 1402659188" | S4 |
| KK-30 | p. 19, l. 578 | "[No title found]" | the title of the article in Aquatic Sciences 64, 118 to 128 | S4 |

#### Verification log

| ID | Check | Checked | Values | Result |
|---|---|---|---|---|
| PP-29 | P4 | Numbering and cross-references | Sections 1, 2 (duplicate), 3 to 6; subsections 3.1 to 3.4, 4.1.1 to 4.1.4, 4.2, 4.2.1 to 4.2.2 without gaps; equations 1 to 22 consecutive; references to eq. 7 (p. 7, l. 191; p. 8, l. 240; p. 9, l. 245), eq. 16 (p. 8, l. 213 and l. 217), eqs. 11 to 13 (p. 7, l. 200), eqs. 1 to 4 (p. 9, l. 263) reach the right equation; figures 1 to 16 consecutive and cited; panel letters cited (1A to 1D, 2A to 2C, 3A to 3E, 5A to 5K, 6C to 6G) all exist | findings GB-06, KK-18 |
| PP-30 | P4 | Citations against reference list, both directions (Python) | 64 entries, 64 cited keys; every entry cited, every citation listed; "et al." used for entries with more than two authors, "and" for two | findings GB-03, KK-30 |
| PP-31 | P15 | Conclusion and outlook statements against results | p. 16, l. 482 to 483 reliable recovery (held against Fig. 5c, GB-13); l. 483 to 484 resolution and covariance as reliability measures (held against Fig. 5d, GB-14); l. 484 to 486 conditions for use: minimal storage (assumption stated at p. 15, l. 466 to 468), distinct sources (scenario 2, supported), good spatial knowledge (scenario 1, supported), multiple source areas (GB-33); l. 487 to 489 extension to land use and other tracers (stated as possible, no finding) | findings GB-30, GB-32, GB-33 |
| PP-32 | P15 | Framework and key terms of the introduction in discussion and conclusion | Bayesian framing (p. 2, l. 55 to 57) used in Section 3.2, not in the discussion; glacierised catchments (p. 3, l. 62) taken up at p. 14, l. 418 and p. 15, l. 460; cost-effectiveness (p. 2, l. 40) taken up at p. 3, l. 74, not in discussion or conclusion | finding GB-01 |
| PP-33 | P16 | Language and typesetting at the page image | 30 minor corrections; reference list checked for uniformity only: DOI given for most entries, absent for Bearth 1953, Belotti 2021, Bish and Post 1989, E. 2009, Gjems 1967, Lafuente et al. 2015, Moore and Reynolds 1990, Papanicolaou et al. 2003, Tarantola 2005 (books, theses, maps) | KK-01 to KK-30 |
| PP-34 | P12 | Data sources of Sections 3 and 4 against the statement at p. 16, l. 490 | 8 sources listed in GB-36; 1 statement; Zenodo DOI present; WebFetch of the DOI returned HTTP 429 | finding GB-36 |

## Optional checks

| Area | What it needs | Responsible | Run |
|---|---|---|---|
| DOI resolution | one retrieval per reference entry with DOI | `science-quellenapparat-pruefung` | no |
| Citation style | the name of the style | `science-zitierstil-harvard-ctr` or the journal's style rules | no |
| AI statement against publisher policy | the target publisher's policy | this review, on request | no |
| Relation to own prior work | the authors' prior work | this review, on request | no |
| Journal requirements | the author guidelines of the target journal | this review, on request | no |
| Subject-matter accuracy | access to the sources of the checked statements and a selection of sections | `science-faktenbeleg-pruefung`, `geo-frage-belegbasiert-klaeren` | no |

## Limits of this review

- Checked version: egusphere-2025-4695.pdf, 37 pages, SHA-256 9c80676054f96ecd6f00f4d2a8b5ba568e03c6949e3856d363ac1c4abb42e7bd
- Unreadable sources: Zenodo record https://doi.org/10.5281/zenodo.17120374 (rate limited); Butler et al. (2019) full text (PMC browser check, Europe PMC rate limited); Das et al. (2023) full text; Das et al. (2024) full text (only the landing page read); Wilson et al. (1993) and Barker et al. (1997) (judged from titles); authors of the SedUnMix paper (record without author list)
- Findings with status assumption: 1 of 36 (one sub-statement of GB-23)
- Optional checks run: 0 of 6
- Omitted instances: none
- Discarded findings: 0
- The six review instances ran sequentially in one context, not as separate agents, so the double coverage of figure numbering, outlook proposals, framework and figures against methods was not independent.
