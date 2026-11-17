# Review report: From XRD signal to erosion rate maps

| Field | Value |
|---|---|
| Manuscript | De Doncker, F., Herman, F., Belotti, B. and Adatte, T. (2025), From XRD signal to erosion rate maps, EGUsphere preprint egusphere-2025-4695, https://doi.org/10.5194/egusphere-2025-4695 |
| Checked version | egusphere-2025-4695.pdf, 37 pages, SHA-256 9c80676054f96ecd6f00f4d2a8b5ba568e03c6949e3856d363ac1c4abb42e7bd |
| Date | 2026-10-17 |
| Language | English |
| Review instances | Segments 1 to 4 (S1 to S4), figures (AB), study design and method (SD); the six review instances ran as separate agents without shared context; no instance omitted; merging, overall assessment and format check in a separate step (ZF) |

## Summary

The manuscript is a method study with a synthetic validation and a natural case study. It builds a Bayesian maximum a posteriori inversion that turns binned X-ray diffraction (XRD) peak-area data of 21 tracer minerals, measured on source rocks and on suspended sediment, into an erosion rate map on a raster of source pixels (pixel size 300 m), using a geological map of 7 lithological units as spatial information and a log-space parameterisation of the erosion rates. Two iterative schemes, steepest descent (SD) and quasi-Newton (QN), are compared, and posterior covariance, resolution and a normalised posterior uncertainty are reported per pixel. Synthetic forward-inverse tests use one "true" map with a single hotspot, three degradation scenarios (3 geological maps, 20 levels of fingerprint blending, 1 to 21 tracers) and five hyperparameter sweeps. The natural tests in the Gornergletscher catchment (Swiss Alps) check the XRD fingerprints qualitatively, invert detrital samples from the Gorner-Grenz subcatchment while the tracer matrix covers the whole catchment, and compare zircon U-Pb, XRD and combined fingerprints on one detrital sampling time (28 June 2019). Key numbers: errors and uncertainty rise below an average Jensen-Shannon (JS) distance of 0.55; 7 tracers give about the same solution as 21; total normalised posterior uncertainty 0.87 (zircon), 0.82 (XRD) and 0.86 (combined); average JS distance 0.48 (zircon) and 0.57 (combined).

## Strengths

1. The synthetic forward-inverse design scores every run against a known map and varies one factor at a time, so the manuscript can show where the method degrades: the error plateau from 7 tracers on and the rise below 7 (PP-27), monotonically increasing misfits with growing map mismatch (PP-28), and the onset of higher uncertainty below an average JS distance of about 0.55 (PP-32). Limits of what this design covers are in GB-24 and GB-30.
2. The numbers that link text and figures agree: hyperparameters and the implied pixel size (PP-22), the three total normalised uncertainties 0.87, 0.82 and 0.86 in text and figure labels (PP-23), the 21 tracers in the text list and in Figures 5k, 9, 11, 15 and 16 (PP-24), and the 13 zircon age bins with the assigned Monte Rosa fingerprint (PP-26). A reader can match each reported value to its figure; the one name mismatch is GB-35.
3. The citation apparatus resolves in both directions: 64 author-year keys in the text against 64 reference entries with no missing and no uncited entry, and consistent short forms (PP-40, PP-41); figures and equations are numbered consecutively and every figure is cited in order (PP-18, PP-12). Wrong targets remain at single places (GB-07, GB-29).
4. Code and data for the inversion tests are deposited under a resolving DOI with an open licence (PP-09), and the framework accepts a second, independent tracer type by concatenating the tracer matrices and data vectors, which the zircon comparison demonstrates technically (PP-26). What the comparison shows in substance is limited by GB-41 and GB-42.

## Weaknesses

1. The mineralogical fingerprints, the core of the method, are not shown to be valid tracers: their stability between bedrock powder and suspended load is not tested (GB-06), research question 1 is answered by one qualitative sentence while several values in Figure 11 do not fit the stated lithologies (GB-36), several of the 21 "minerals" have identical columns (GB-20), and one tracer name does not match the figures (GB-35). Suggested: a range test per tracer, size-matched source preparation, a table of expected minerals per unit with a stated agreement criterion, and a table of 2θ windows with merged group tracers.
2. The natural-data tests do not yet support "validated": the subcatchment test checks one excluded unit, while a second unit without area in the subcatchment receives substantial erosion (GB-37); the zircon comparison confounds tracer type with an incomplete zircon matrix (GB-41); the claim that combining zircon with XRD further improves the solution is contradicted by the reported uncertainties (GB-42); and the Conclusions do not answer the three natural-data questions (GB-51). Suggested: area shares and per-unit results for the subcatchment, a comparison on a common source set and on several samples, the same metrics for all three runs, and conclusions stated per question.
3. The synthetic tests are a best case and their reading is partly not borne out by the figures: the prior equals the true mean and the hyperparameters are tuned against the true map of a single hotspot (GB-24); the stated accuracy advantage of QN over SD and three stated sweep trends are not visible in Figures 5, 6 and 10 (GB-28, GB-34); and the resolution and normalised uncertainty maps pair in the opposite way to their definitions, under names that change between text and figures (GB-26, GB-18). Suggested: an ensemble of true maps with data-only priors and tuning, equal iteration budgets, sweeps that cover the claimed ranges, and a formula and check of the plotted resolution.
4. Several inputs and steps cannot be rebuilt from the manuscript: the XRD processing settings and sample metadata (GB-19), the zircon protocol (GB-39), the prior and export estimate of the natural runs (GB-40), the sources and identity of the geological maps (GB-21, GB-22), and four equations as printed (GB-15, GB-17); in addition the Introduction is printed twice and some references are wrong (GB-04, GB-05, GB-07). Suggested: a methods table with instrument and processing settings, the export value and prior per run, named map files in the data statement, corrected equations, and a single checked Introduction.

## Findings by segment

### Segment 1: Abstract, Introduction (p. 1 to 5)

#### Substantive findings

**GB-01 The spatio-temporal motivation and the Bayesian positioning of the Introduction have no research question, test or discussion, and the natural comparison rests on one instantaneous sample scaled by an annual export.**

| Field | Content |
|---|---|
| Check | P10, P15 |
| Location | p. 1, l. 1; p. 1, l. 10; p. 1, l. 13; p. 2, l. 55 to 57; p. 4, l. 122 to 124 |
| Quotation | "Understanding the spatio-temporal dynamics of suspended sediment source activation is essential" and "Identifying sediment source hotspots and the timing of their activation" and "Our approach can be seen as a hybrid between Bayesian linear mixed models and hierarchical Bayesian models" |
| Concern | Abstract and Introduction motivate the study with temporal dynamics and the timing of source activation, and place the method between frequentist and Bayesian unmixing models (p. 2, l. 43 to 57, repeated p. 4, l. 110 to 124). Search of `text.json`, p. 1 to 16, for "temporal" gives 3 hits (p. 1, l. 1 and l. 10; p. 3, l. 77), "season" 0 and "timing" 2 (p. 1, l. 13; p. 3, l. 80), all in this motivation; in Discussion and Conclusions (p. 15, l. 450 to p. 16, l. 489) "Bayes", "frequentist", "temporal" and "timing" give 0 hits each. No research question, instrument or result addresses time. The comparison runs use "the detrital sample collected on June 28, 2019, at 13:30" (p. 14, l. 423 to 424), while the data are scaled by an annual export estimate (p. 3, l. 65 to 66; eq. 2, p. 5, l. 159 to 160), although "multi-year suspended sediment datasets" are said to exist (p. 9, l. 268); how representative one moment is for the year is not discussed. The Discussion also does not say how the posterior covariance and resolution relate to the uncertainty outputs of the unmixing families named in Section 1. Graded moderate rather than minor because the maps are read as annual erosion rates without this discussion. |
| Suggestion | Either analyse a time series (for instance samples across a melt season, weighted by suspended load) or remove the temporal framing from the Abstract (p. 1, l. 1) and the Introduction (p. 1, l. 10 to 14) and state in Section 4.2 that the maps express instantaneous source contributions scaled by an annual export; add to Section 5 two or three sentences relating posterior covariance and resolution to the uncertainty outputs of the unmixing models of Section 1. |
| Status | verified (searches in `text.json`, wording on page images p. 1, 2, 14) |
| Severity | moderate |
| Source | S4, SD |

**GB-02 Time and cost efficiency is claimed as validated in the Abstract and Introduction, but no time, cost or throughput is reported and the Discussion does not take it up.**

| Field | Content |
|---|---|
| Check | P15, P33 |
| Location | p. 1, l. 3 to 4; p. 2, l. 40 to 42; p. 3, l. 74 to 75; p. 4, l. 107 to 109; p. 5, l. 141 to 142 |
| Quotation | "In this study, we validate a time- and cost-effective fingerprinting approach based on X-ray diffraction (XRD) data." and "To conclude, we show and validate the potential of binned XRD peak-area data as a cost- and time-efficient approach for constructing erosion rate maps." |
| Concern | Search of `text.json`, p. 1 to 16: "cost" 6 hits (p. 1, l. 3 and 4; p. 2, l. 40; p. 3, l. 74; p. 4, l. 107; p. 5, l. 141), "efficien" 4 hits (p. 2, l. 42; p. 3, l. 75; p. 4, l. 109; p. 5, l. 142), all in Abstract and Introduction; in Discussion and Conclusions "cost", "time-" and "efficien" give 0 hits. The manuscript reports no cost per sample, no preparation or instrument time and no comparison with the zircon U-Pb workflow that the study itself runs (p. 14, l. 423 to 425). The only support is the literature statement that other methods "are expensive and time-consuming (Das et al., 2023)" (p. 2, l. 35), whose source could not be read (PP-02). "validate" thus presents as a result what is a motivation. The inversion results are unaffected, hence moderate. |
| Suggestion | Report per-sample preparation and measurement time and cost for the XRD and the zircon workflows used here and discuss them in Section 5, or reword p. 1, l. 3 to 4 and p. 3, l. 74 to 75 as a sourced motivation, for example "XRD is considered a time- and cost-effective technique (Das et al., 2023)". |
| Status | verified (searches; page images p. 1 to 5) |
| Severity | moderate |
| Source | S4, SD |

**GB-03 The Abstract reports "consistent convergence" for the synthetic tests, while the Results report three conditions without convergence and call poorly distinguishable fingerprints a major limitation.**

| Field | Content |
|---|---|
| Check | P2 |
| Location | p. 1, l. 7; p. 11, l. 312; p. 12, l. 353 to 354; p. 13, l. 387 to 388 |
| Quotation | "Forward-inverse tests with synthetic data demonstrate consistent convergence of the posterior solution." and "In many of these cases, the inversion fails to converge to a stable posterior solution." and "Only when the maximum number of non-linear steps is reduced below 25 does the posterior fail to converge to the true erosion map." |
| Concern | The Results document three conditions without convergence: steepest descent without gradient normalisation ("In initial experiments, the steepest descent approach proved unstable, requiring the normalization of the gradient.", p. 11, l. 312), blended fingerprints (p. 12, l. 353) and too few iterations (p. 13, l. 387 to 388). They conclude that "poorly distinguishable fingerprints are a major limitation in source attribution" (p. 12, l. 353 to 354). The Abstract states convergence without condition and does not mention this limitation. GB-34 shows that the iteration threshold itself is not as stated in Figure 10; this finding concerns the Abstract. |
| Suggestion | In the Abstract (p. 1, l. 7) qualify the convergence statement by the conditions found (sufficiently distinct fingerprints, QN scheme, enough iterations) and add one sentence on the limitation from poorly distinguishable fingerprints. |
| Status | verified |
| Severity | moderate |
| Source | S3 |

**GB-04 The Introduction is printed twice, as Section 1 and Section 2, with identical wording.**

| Field | Content |
|---|---|
| Check | P4 |
| Location | p. 1, l. 9; p. 3, l. 76 |
| Quotation | "1 Introduction" and "2 Introduction" |
| Concern | The text of Section 1 (p. 1, l. 10 to p. 3, l. 75) and of Section 2 (p. 3, l. 77 to p. 5, l. 142) are the same: word comparison with Python difflib on `text.json`, running headers removed, gives 1153 words each and a ratio of 1.0 (PP-06; headings confirmed on page images p. 1 and 3). As a consequence "3 Methods" is numbered one higher than it would be, and every citation and every small error of the Introduction occurs twice (GB-07, GB-10, KK-02). All six instances noted the duplication. |
| Suggestion | Delete Section 2 (p. 3, l. 76 to p. 5, l. 142) and renumber Methods, Validation, Discussion and Conclusions as Sections 2 to 5. |
| Status | verified (page images p. 1, 3, 5; Python comparison) |
| Severity | minor |
| Source | S4 |

**GB-05 Four cited sources in the Introduction do not deal with the subject they are cited for, and a fifth is doubtful by its title.**

| Field | Content |
|---|---|
| Check | P13 |
| Location | p. 1, l. 18 to 19; p. 1, l. 26; p. 2, l. 28; p. 2, l. 30; p. 3, l. 85 to 86; p. 3, l. 93; p. 4, l. 95; p. 4, l. 97 |
| Quotation | "Direct measurements, such as sediment traps installed on dams, provide valuable information on sediment fluxes but do not reveal the origin of the transported material (Wilson et al., 1993; Barker et al., 1997; Davis and Fox, 2009)." and "geochemistry (Olley et al., 1993; Gholami et al., 2019; Lipp et al., 2021; Domingo et al., 2023)" and "nutrients (Blaen et al., 2016; Asadi et al., 2025)" and "mineralogy (Walden et al., 1997; Nukazawa et al., 2021)" |
| Concern | The tracer overview is useful, but (a) Barker et al. (1997) test terrestrial photogrammetry of a river bank for bank erosion volumes; its abstract mentions neither sediment traps, dams nor sediment flux. Wilson et al. (1993) is titled "Soil erosion in the Falkland Islands: an assessment" (p. 21, l. 649); its publisher page could not be read. Only Davis and Fox (2009) plausibly supports the sentence. (b) Olley et al. (1993), listed under geochemistry, is titled "Identifying sediment sources in a gullied catchment using natural and anthropogenic radioactivity" (p. 20, l. 621 to 622), that is radionuclides, the next category of the same sentence. (c) Walden et al. (1997), listed under mineralogy, is titled "Use of mineral magnetic measurements to fingerprint suspended sediment sources" (p. 20, l. 641), that is magnetic tracers; for a paper on mineralogical fingerprinting this suggests a mineralogical precedent that is magnetic. (d) Blaen et al. (2016), listed as a nutrient fingerprinting study, reviews real-time monitoring of nutrients and dissolved organic matter in rivers; its abstract does not mention sediment sources or fingerprinting. All occur twice because of GB-04. |
| Suggestion | At p. 1, l. 19 and p. 3, l. 86 replace Wilson et al. (1993) and Barker et al. (1997) by studies that measure sediment flux with traps, reservoir surveys or turbidity records, or reword the sentence; move Olley et al. (1993) to "radionuclides" and Walden et al. (1997) to "magnetic susceptibility" (p. 1, l. 26 and p. 2, l. 30, and their duplicates), and replace Blaen et al. (2016) by a study that uses nutrients as source tracers; for "mineralogy" cite XRD fingerprinting studies, for example Klages and Hsieh (1975) and Wall and Wilding (1976), already in the reference list. |
| Status | (a) Barker: verified (abstract, https://researchportal.port.ac.uk/en/publications/use-of-terrestrial-photogrammetry-for-monitoring-and-measuring-ba/); Wilson: inferred (title only, https://doi.org/10.1016/0143-6228(93)90036-Z not readable). (b), (c): verified at title level (reference list on page image p. 20; Semantic Scholar records for DOI 10.1029/92WR02710 and 10.1016/S0022-1694(97)00078-4; full texts not read). (d): verified (abstract, Semantic Scholar record for DOI 10.1016/j.scitotenv.2016.06.116) |
| Severity | minor |
| Source | S1 |

**GB-06 The manuscript states that an ideal fingerprint must stay stable during erosion, transport and storage, but tests only distinctness, and the grain-size mitigation it names does not match its own sampling.**

| Field | Content |
|---|---|
| Check | P18 |
| Location | p. 1, l. 24 to 25; p. 3, l. 91 to 92; p. 15, l. 469 to 473; Fig. 3a (p. 24) |
| Quotation | "An ideal fingerprint is 1) capable of distinguishing among sources and 2) remains stable during erosion, transport, and storage" and "This can be diminished by powdering samples and using depth-integrated suspended sediment samples" |
| Concern | Criterion 1 is tested (JS distance, scenario 2), criterion 2 is not: there is no range test of detrital values against source values, and no size fraction is given for either material (search of `text.json`, p. 1 to 16, for "sieve", "µm", "grain size", "grain-size", "size fraction", "clay", "silt": 1 hit, p. 15, l. 469, in the Discussion). Sources are powdered bulk rock (p. 9, l. 252; p. 13, l. 396); the detrital material is suspended sediment, shown in Fig. 3a as "detrital sampling: pump sampler", while the text does not name the sampling method (search "pump" in p. 1 to 16: 0 hits). The mitigation at p. 15, l. 470 names depth-integrated samples; whether the pump sampler integrates over depth is not said. Applying the same preparation protocol to both materials (p. 15, l. 472 to 473) addresses preparation effects, not differences in mineral make-up between bulk rock and suspended load. If the tracers are not conservative, the attributions of Section 4.2 change, hence major. Does the pump sampler integrate over depth, and which size fraction was analysed? |
| Suggestion | State in Section 3.4 the size fraction and sampling depth of the detrital samples; apply a range test per tracer to all detrital samples; prepare source material at the size of the suspended load (crushed and sieved) or sample fine sediment from monolithologic tributaries, and report the effect on the fingerprints. |
| Status | verified (absence by search; Fig. 3a on page image); assumption (depth integration of the pump sampler, size of sorting effects), asked as a question |
| Severity | major |
| Source | SD |

**GB-07 The citation "Kobe, 2021" for plant pollen as a sediment fingerprint points to an article on black theology of liberation.**

| Field | Content |
|---|---|
| Check | P13, P4 |
| Location | p. 2, l. 31; p. 4, l. 98; p. 19, l. 597 to 598 |
| Quotation | "plant pollen content (Brown, 1985; Kobe, 2021)" and "Kobe, S. L.: Ubuntu as a spirituality of liberation for black theology of liberation, HTS Teologiese Studies / Theological Studies, 77," |
| Concern | Brown (1985) supports pollen as a sediment tracer; the second source does not deal with sediment. The journal landing page reached from DOI 10.4102/hts.v77i3.6176 shows an article in Christian spirituality whose abstract mentions neither pollen, sediment nor fingerprinting. The statement of the state of research thus loses one of its two sources, which a reader cannot trace; because of GB-04 the wrong citation occurs twice. Graded moderate (S4) rather than minor (S1) because the source of a state-of-research statement is not traceable. |
| Suggestion | Delete "Kobe, 2021" at p. 2, l. 31 and p. 4, l. 98 and remove the entry at p. 19, l. 597 to 598, or replace it by the intended pollen-tracing publication; check the reference import for further mismatches (GB-05, KK-02, KK-26). |
| Status | verified (journal landing page with abstract, https://hts.org.za/index.php/hts/article/view/6176; citation and entry on page images p. 2, 4, 19) |
| Severity | moderate |
| Source | S1, S4 |

**GB-08 Three works that anticipate parts of the contribution are missing: XRD-based mineralogical unmixing tested on known mixtures, a formal inversion of detrital data into spatially varying erosion rates, and a log-ratio parameterisation of source proportions.**

| Field | Content |
|---|---|
| Check | P14 |
| Location | p. 2, l. 36 to 42; p. 4, l. 103 to 109; p. 2, l. 58 to 61; p. 4, l. 125 to 128; p. 13, l. 404 to 406 |
| Quotation | "X-ray diffraction (XRD) has recently gained attention as a proxy for mineral abundance in provenance analysis but remains underutilized (Das et al., 2023)." and "Building on the work of Das et al. (2023, 2024), we investigate the potential of binned XRD data as a cost-effective fingerprinting method." |
| Concern | The contribution in one sentence: binned XRD peak-area data serve as mineralogical fingerprints in a log-space Bayesian inversion that turns detrital data into spatially explicit erosion rate maps with posterior uncertainty. Each of the following works anticipates one element and is absent from the reference list (search of p. 17 to 21 for the author names "Andrews", "Eberl", "Braun", "Stock", "Ehlers": 0 hits as author). (1) Andrews, J. T. and Eberl, D. D. (2012) Determination of sediment provenance by unmixing the mineralogy of source-area sediments: The "SedUnMix" program, Marine Geology, 291 to 294, 24 to 33, https://doi.org/10.1016/j.margeo.2011.10.007: quantitative XRD mineralogy of four end members unmixed in eleven artificial mixtures; precedent for XRD unmixing and for the known-mixture test that p. 13, l. 404 to 406 describe as typical without a citation. (2) Braun, J., Gemignani, L. and van der Beek, P. (2018) Extracting information on the spatial variability in erosion rate stored in detrital cooling age distributions in river sands, Earth Surface Dynamics, 6, 257 to 270, https://doi.org/10.5194/esurf-6-257-2018: inversion of detrital cooling ages into present-day erosion rates for an underdetermined problem; it limits the claim at p. 2, l. 58 to 59 (GB-11). (3) Stock, B. C., Jackson, A. L., Ward, E. J., Parnell, A. C., Phillips, D. L. and Semmens, B. X. (2018) Analyzing mixing systems using a new generation of Bayesian tracer mixing models, PeerJ, 6, e5096, https://doi.org/10.7717/peerj.5096: MixSIAR transforms source proportions into isometric log-ratio space, the device the manuscript introduces as its "non-linear adaptation" (GB-11); Das et al. (2024), cited by the manuscript, already used MixSIAR for XRD mineralogical tracers. GB-02 cites p. 2, l. 40 to 42 for the cost claim; this finding concerns missing literature. |
| Suggestion | Cite Andrews and Eberl (2012) at p. 2, l. 36 to 42 and p. 13, l. 404 to 406, Braun et al. (2018) and Stock et al. (2018) at p. 2, l. 58 to 61, and state what the present study adds beyond each. |
| Status | Andrews and Eberl (2012): verified (abstract, https://pubs.usgs.gov/publication/70032707); Braun et al. (2018): verified (article page, https://esurf.copernicus.org/articles/6/257/2018/); Stock et al. (2018): verified (full text, https://pmc.ncbi.nlm.nih.gov/articles/PMC6015753); Das et al. (2024) use of MixSIAR: verified (abstract, Rothamsted repository record); absence from the reference list: verified on page images p. 17 to 21 |
| Severity | moderate |
| Source | S1 |

**GB-09 The split of uncertainty methods into sampling-based frequentist and Bayesian methods is attributed to Niu et al. (2020), whose abstract reports a third route, analytical first-order error propagation without sampling, which the manuscript later claims for its own approach.**

| Field | Content |
|---|---|
| Check | P13 |
| Location | p. 2, l. 45 to 48; p. 4, l. 112 to 115; p. 2, l. 55 to 57; p. 4, l. 122 to 124; p. 6, l. 177 to 178 |
| Quotation | "Where frequentist methods estimate the uncertainty on the resulting source contributions by sampling the different possible sets of source contributions, Bayesian methods use priors, model and data uncertainty to allow error propagation so the a posteriori uncertainty can be inferred from different posterior metrics (Niu et al., 2020)." and "without requiring the generation and sampling of multiple posterior solutions" |
| Concern | The overview of unmixing families helps the reader place the method. In the publisher abstract of Niu et al. (2020), however, "the uncertainty of sediment source contributions was quantified using the Gaussian first-order approximation", that is analytical, linearised error propagation without sampling and without priors. The manuscript's own posterior covariance rests on the same principle ("We assume weak nonlinearity, where our forward model can be linearized around the prior", p. 6, l. 177 to 178; eq. 20). By attributing a two-way split to Niu et al. (2020), the text leaves out the category of the cited study that anticipates the property presented as distinctive at p. 2, l. 56 to 57. Whether the full text of Niu et al. (2020) contains the split elsewhere could not be checked. |
| Suggestion | At p. 2, l. 45 to 48 cite a source that sets out the frequentist and Bayesian split (the manuscript already cites Fathabadi and Jansen, 2022, whose title names both), or add linearised analytical error propagation as a third family with Niu et al. (2020) as example; at p. 2, l. 55 to 57 state how the linearised Gaussian posterior covariance of eq. 20 differs from the first-order approximation of Niu et al. (2020). |
| Status | wording of Niu et al. (2020): verified (abstract on publisher page, https://link.springer.com/article/10.1007/s11368-019-02424-1; full text not readable); absence of the split in the full text: inferred; manuscript passages: verified on page images p. 2, 4, 6 |
| Severity | moderate |
| Source | S1 |

**GB-10 The overview of unmixing methods gives one method two abbreviations and a contradictory name, uses non-standard expansions for GLUE and MLE, and calls the Bayesian category by two different model names.**

| Field | Content |
|---|---|
| Check | P38 |
| Location | p. 2, l. 48 to 56; p. 4, l. 115 to 123 |
| Quotation | "1) the Non-Linear Least Squares (NLLS) (a constrained linear regression)" and "3) Generalist Likelihood Uncertainty Estimation (GLUE)" and "4) Maximal Likelihood Estimation (MLE) (similar to the NNLS approach, but with a probabilistic error model)" and "Bayesian Linear Mixing Models (BLMM)" |
| Concern | Method 1 is introduced as "NLLS", but MLE is then compared with "the NNLS approach"; NNLS is not introduced anywhere (search of `text.json`, p. 1 to 21: "NLLS" 2 hits, p. 2, l. 49 and p. 4, l. 116; "NNLS" 2 hits, p. 2, l. 51 and p. 4, l. 118; no expansion of NNLS). "Non-Linear Least Squares" also contradicts the gloss "a constrained linear regression". GLUE is usually expanded as "Generalized (Generalised) Likelihood Uncertainty Estimation", and "Maximal" should read "Maximum". The Bayesian category is introduced as "Bayesian Linear Mixing Models (BLMM)" and two lines later called "Bayesian linear mixed models" (p. 2, l. 55 to 56); mixing models (source apportionment) and mixed models (random effects) are different model classes. Is method 1 non-negative least squares, and is BLMM meant at p. 2, l. 55 to 56? GB-09 cites the same paragraph for the source of the frequentist and Bayesian split, and GB-01 cites p. 2, l. 55 to 57 for the Bayesian positioning that is not taken up later; this finding concerns the method names. |
| Suggestion | At p. 2, l. 48 to 56 (and the duplicate, or after deleting it, GB-04) write "Non-Negative Least Squares (NNLS)" if meant, "Generalised Likelihood Uncertainty Estimation (GLUE)", "Maximum Likelihood Estimation (MLE)" and "Bayesian linear mixing models (BLMM)" in the hybrid sentence. |
| Status | wording and counts: verified (page images p. 2 and 4); identity of NLLS and NNLS: inferred from the back reference; GLUE expansion: inferred (abstract of Beven and Binley, 1992, Hydrological Processes, 6, 279 to 298, read on https://eprints.lancs.ac.uk/id/eprint/22741, names the GLUE procedure without spelling out the acronym) |
| Severity | minor |
| Source | S1, S2, S4 |

**GB-11 The contrast with approaches that "implicitly rely on a linear mixing scheme" and the novelty of a "non-linear mixing model" do not hold for the manuscript's own forward model, which is a linear mixture with a log-space parameterisation, and the spatially informed approach is taken from De Doncker et al. (2020).**

| Field | Content |
|---|---|
| Check | P28, P15 |
| Location | p. 2, l. 58 to 61; p. 4, l. 125 to 128; p. 15, l. 454 to 455 |
| Quotation | "However, these approaches typically yield relative source contributions without translating them into spatially explicit erosion rate maps and implicitly rely on a linear mixing scheme (Niu et al., 2020)." and "Hence, the detrital data are a weighted average of the tracer mineral concentrations, with the weights being the erosion rates." and "The novelty of our method lies in the spatially informed approach of this underdetermined inversion problem, and in the incorporation of non-linear mixing model." |
| Concern | The manuscript credits the spatial inversion to De Doncker et al. (2020), which is good practice. (1) No literature search is reported for what "these approaches typically" do; the only support is Niu et al. (2020), a single case study whose abstract reports "a linear mixing model". (2) The spatially informed approach is not new here: the repository abstract of De Doncker et al. (2020) describes converting zircon age data into an erosion rate map from the spatial distribution of source signatures, and Braun et al. (2018) invert detrital data into spatially varying erosion rates (GB-08). (3) The forward model is a linear mixture: eq. 1 (p. 5, l. 151 to 154) reads d_i = sum_j A_ij exp(ε_j) / sum_j exp(ε_j), which the text calls a weighted average (p. 5, l. 151 to 152). A Python check with random A (21 × 7) and random ε confirms that eq. 1 equals A·p with p = exp(ε)/sum(exp(ε)), that is linear mixing with softmax proportions (np.allclose True), and that it is unchanged when all rates are scaled by 2 (True). The non-linearity lies in the parameterisation ("We cast the erosion rates in log-space to impose a positivity constraint, hence making this non-linear.", p. 5, l. 157 to 158), not in the mixing; log-ratio parameterisations of proportions are standard in Bayesian mixing models (Stock et al., 2018, GB-08). (4) An article is missing in "of non-linear mixing model". The duplicate passage p. 4, l. 125 to 128 carries the same text, including the citation form "validated in (De Doncker et al., 2020)" (p. 2, l. 61; p. 4, l. 128). GB-08 cites the same lines for the missing literature; this finding concerns the contrast and the novelty claim. |
| Suggestion | At p. 2, l. 58 to 61 report the search behind "typically" or narrow the sentence to the cited study; describe the method as linear mixing with a log-space (softmax) parameterisation of erosion rates for positivity and relate it to log-ratio parameterisations; rewrite p. 15, l. 454 to 455 so that the novelty is what the manuscript adds to De Doncker et al. (2020), for example binned XRD fingerprints, the QN and SD schemes and the posterior metrics, with "a non-linear inversion of a linear mixing model"; write "validated by De Doncker et al. (2020)". |
| Status | manuscript passages and eq. 1: verified (page images p. 2, 4, 5, 15); equivalence to linear mixing: verified (Python); Niu et al. (2020) linear mixing model: verified (abstract, https://link.springer.com/article/10.1007/s11368-019-02424-1); De Doncker et al. (2020): verified at abstract level (https://serval.unil.ch/notice/serval:BIB_1A4D2FF81D64, full text not read) |
| Severity | moderate |
| Source | S1, S4 |

#### Minor corrections

| ID | Location | Quotation | Replacement | Source |
|---|---|---|---|---|
| KK-01 | p. 1, l. 5 | "(steepest descent and Quasi-Newtonian)" | "(steepest descent and quasi-Newton)"; the text uses "quasi-Newton" (p. 7, l. 211; p. 10, l. 296) and "Quasi-Newton" (p. 10, l. 287; p. 11, l. 320); "Quasi-Newtonian" occurs only here. The comparison announced in this sentence is treated in GB-28; this correction concerns the name only. | S1, S2 |
| KK-02 | p. 1, l. 11 to 12; p. 3, l. 78 to 79; p. 18, l. 567 to 568 | "(Gergel et al., 2002; Allan, 2004; E., 2009; Hamel et al., 2015)" and entry "E., W. D.: The Impact of global change on erosion and sediment transport by rivers, UNESCO 2009, ISBN 9789231041358, oCLC:" | In the text "(Gergel et al., 2002; Allan, 2004; Walling, 2009; Hamel et al., 2015)"; entry "Walling, D. E.: The impact of global change on erosion and sediment transport by rivers, UNESCO, Paris, ISBN 9789231041358, OCLC 1402659188, 2009." The surname is inferred from the inverted initials "E., W. D."; the report itself could not be read (Limits). | S1, S4 |
| KK-03 | p. 3, l. 70; p. 5, l. 137 | "we optimize the hyper-parameters" | "we optimize the hyperparameters", as in p. 10, l. 281 and p. 12, l. 370 (hyphen inside the line, confirmed on page images p. 3 and 5) | S2 |

#### Verification log

| ID | Check | Checked | Values | Result |
|---|---|---|---|---|
| PP-01 | P13 | Inventory of statements in Segment 1 that report findings or evaluations of cited works, each once for both copies of the Introduction | Importance of suspended sediment (Gergel 2002, Allan 2004, Walling 2009, Hamel 2015); fine fractions carry nutrients (Issaka and Ashraf 2017); model performance (Poesen 2018, Borrelli 2021); sediment traps (GB-05); fingerprinting principle (Klages and Hsieh 1975, Wall and Wilding 1976, Walling et al. 1979); ideal fingerprint criteria; tracer list with 29 citations (GB-05, GB-07); cost statement (Das 2023, PP-02); unmixing families (Yang 2025, Niu 2020, Haddadchi 2013, Fathabadi and Jansen 2022; GB-09); gap statement (GB-11). No statement quotes a number from a cited work. | Findings GB-05, GB-07, GB-09, GB-11; not checked at source: Klages and Hsieh (1975), Wall and Wilding (1976), Walling et al. (1979), Gergel et al. (2002), Allan (2004), Hamel et al. (2015), Issaka and Ashraf (2017), Poesen (2018), Borrelli et al. (2021), Yang et al. (2025) |
| PP-02 | P13 | Das et al. (2023) as source for "expensive and time-consuming" (p. 2, l. 35) and "remains underutilized" (p. 2, l. 36 to 37) | Publisher page (DOI 10.1029/2023WR034500) not readable; Semantic Scholar summary reports XRD spectra with PLS regression and source shares, no statement on cost, time or underuse | no finding; source not readable (Limits) |
| PP-03 | P13 | Cited statements found consistent with their source | Torres Astorga et al. (2020) for total organic carbon (DOAJ abstract); De Doncker et al. (2020) for the inversion framework (repository abstract: least-squares inversion of detrital zircon ages into an erosion rate map, other tracers such as mineral content possible); Das et al. (2024) for "Building on" (Rothamsted abstract: XRD mineralogical tracers with MixSIAR); Niu et al. (2020) for its own linear mixing (abstract) | no finding |
| PP-04 | P14 | Literature search for the contribution, four queries | Q1 XRD unmixing (Andrews and Eberl 2012, proposed); Q2 detrital thermochronology inversion (Ehlers et al. 2015, JGR Earth Surface 120, 1023 to 1039, abstract read, not proposed because it uses a forward Monte Carlo model; Braun et al. 2018, proposed); Q3 XRD fingerprinting in glacierized catchments (no candidate; hits on later versions of this manuscript were not opened); Q4 Stock et al. 2018 (proposed). Lipp et al. (2021), Saylor et al. (2019), Das et al. (2024) already cited. | Finding GB-08 |
| PP-05 | P28 | Gap statements and their basis, p. 1 to 16 | Search for "first time", "for the first", "novel", "no stud", "not been", "never", "underutili", "unexplored", "gap", "to our knowledge", "rarely", "few stud", "typically", "has not", "have not", "lack": gap statements "underutilized" (p. 2, l. 37), "typically" (p. 2, l. 58; also p. 13, l. 404), "novel" (p. 15, l. 454); no database, search terms or period named | "typically ... linear mixing" and the novelty statement: GB-11; "underutilized" rests on Das et al. (2023), not readable (PP-02), no separate finding |
| PP-06 | P4 | Word comparison of the two Introductions | Python difflib on `text.json`, p. 1, l. 10 to p. 3, l. 75 against p. 3, l. 77 to p. 5, l. 142: 1153 and 1153 words, ratio 1.0, no differing word; headings on page images p. 1 and 3 | Finding GB-04 |
| PP-07 | P10 | Gaps named in the Introduction against research questions | Costly methods (p. 2, l. 35) to the cost aim without question (GB-02); no spatially explicit maps (p. 2, l. 58 to 60) to the objective p. 3, l. 63 to 64, served by Sections 3 and 4; uncertainty (p. 2, l. 45 to 48) to Section 3.3; temporal dynamics without question (GB-01) | Findings GB-01, GB-02; otherwise no finding |

### Segment 2: Methods, data, study area (p. 5 to 10, Figures 1 to 4)

#### Substantive findings

**GB-12 Two limits that condition the reading of all maps appear only in the Discussion, not where the methods are introduced.**

| Field | Content |
|---|---|
| Check | P17 |
| Location | p. 5, l. 145 to 152; p. 9, l. 249 to 265; p. 15, l. 466 to 468; p. 15, l. 469 to 473 |
| Quotation | "These sediments are then transported or stored." and "as the inversion directly links sediment provenance to erosion rates and assumes immediate sediment export" |
| Concern | The forward model names storage as part of the process (p. 5, l. 147 to 148) but contains no storage term; the assumption of immediate export, under which every map is read as erosion rates, appears only in the Discussion (p. 15, l. 467 to 468). Grain-size, orientation and peak-overlap effects (p. 15, l. 469 to p. 16, l. 476) are likewise discussed only after the results, not in Section 3.4. Both limits are disclosed and are not raised again as such; the finding concerns their place. GB-06 treats the untested stability of the fingerprints. |
| Suggestion | State the immediate-export assumption at eq. 1 in Section 3.1 and the XRD limits in Section 3.4, with a forward reference to Section 5. |
| Status | verified |
| Severity | moderate |
| Source | SD |

**GB-13 The model vector, the iteration index and the tracer indices change their symbols between equations without explanation.**

| Field | Content |
|---|---|
| Check | P38 |
| Location | p. 5, l. 155 to 156; p. 6, l. 175 to 176; p. 6, l. 183 to 184; p. 7, l. 208 to 209; p. 8, l. 215 to 219; p. 9, l. 262 to 263 |
| Quotation | "with µ being the step size, and εk+1 the posterior model after k + 1 non-linear iteration steps" and "where Gn is the Jacobian at iteration n" and "We can thereby derive the abundance of a given tracer t at pixel xy in At,xy as well as in the detrital data dt (eq. 1-4)" |
| Concern | The derivation in Sections 3.1 and 3.2 follows Tarantola (2005) step by step, which makes the notation the main access to the method. Three objects carry two names each (page images p. 5 to 9): (1) iteration index: eq. 17 (p. 7, l. 208) updates ε_k to ε_(k+1); eqs. 18 and 19 (p. 8, l. 215 and 219) update ε_n to ε_(n+1) with G_n, d_n and µ_n but contain the prior term with ε_k, so the current iterate appears as ε_n and ε_k within one equation; (2) model vector: eq. 5 writes the posterior as p(ε_m given d_obs) (p. 6, l. 175), the next line as p(ε given d_obs) (l. 176), and the misfit definitions at l. 183 to 184 mix ε_m on the left with d_ε and ε on the right; (3) tracer matrix: eq. 1 and p. 5, l. 155 to 156 index tracer abundances as A_ij and d_i (tracer i, pixel j), p. 9, l. 262 to 263 as A_t,xy and d_t, with a back reference to "eq. 1-4". In addition the letter n denotes both the number of pixels (eqs. 1 and 4) and the iteration index. |
| Suggestion | In Sections 3.1 to 3.4 fix one symbol per object (for example ε for the model vector, k for the iteration index, A_ij and d_i for tracer i at pixel j), write ε_n instead of ε_k in the prior terms of eqs. 18 and 19, and use the symbols in eqs. 5 to 7, 17 to 19 and at p. 6, l. 176 and 183 to 184, p. 8, l. 216 and p. 9, l. 262 to 263. |
| Status | verified (page images p. 5 to 9) |
| Severity | minor |
| Source | S2, SD |

**GB-14 Figure 2c is cited as the geological map but shows tracer concentration maps, and the black bars of Figure 2b are not explained.**

| Field | Content |
|---|---|
| Check | P3 |
| Location | p. 6, l. 166 to 167; Fig. 2b and 2c (p. 23) |
| Quotation | "By using the spatial distribution of the source areas (geological map) (Figure 2C)" and caption "(c) tracer concentration maps based on geology and lithological fingerprints." |
| Concern | Panel (c) shows stacked maps labelled "tracer 1" to "tracer n" with a colour scale "tracer concentration low high"; no geological map is shown. In panel (b) some detrital bars are drawn in the colours of the tracer maps of (c), others in black; the black bars are not explained in the caption. |
| Suggestion | Cite Fig. 2c at p. 6, l. 167 as tracer concentration maps derived from the geological map, or add the geological map; explain the black bars in the caption. |
| Status | verified (page image p. 23) |
| Severity | minor |
| Source | AB |

**GB-15 Four equations of the inversion are incomplete or inconsistent as printed: eq. 5 lacks its relation sign, eq. 9 lacks the minus sign of the exponent, eq. 12 writes the Jacobian as a vector, and eq. 14 lacks the transpose that eq. 16 has.**

| Field | Content |
|---|---|
| Check | P25 |
| Location | p. 6, l. 175; p. 7, l. 189; p. 7, l. 197; p. 7, l. 201 |
| Quotation | "following Bayes’ theorem" and "the Euclidean distance between point i and j, and L the smoothing distance" and "plugging eq. 12 and eq. 13 into eq. 11, the gradient of the data misfit therefore is" |
| Concern | Checked on page images p. 6 and 7. (1) Eq. 5 (p. 6, l. 175) prints the posterior p(ε_m given d_obs) and the product of likelihood and prior over the evidence side by side with no relation sign; Bayes' theorem needs "=" (with the evidence term, as printed) or "∝". (2) Eq. 9 (p. 7, l. 189) reads C_m(i,j) = σ_m² exp(s_ij²/L²). Without a minus sign the prior covariance grows without bound with distance; for L = 1200 m and s = 3000 m the factor is exp(6.25) = 518, against exp(−6.25) = 0.0019 for a decaying kernel (Python), so the printed form cannot act as the smoothing kernel described at p. 7, l. 190. (3) Eq. 12 (p. 7, l. 197) writes G = A · exp(ε), which is a vector of length m, while G is used as a matrix in G^T C_d^-1 (eq. 16) and in eqs. 19 and 20; the Jacobian of eq. 3 is A · diag(exp(ε)). (4) Eq. 14 (p. 7, l. 201) writes G C_d^-1 (d_ε − d_obs), whereas eq. 16 (p. 7, l. 205), which combines eqs. 14 and 15, has G^T C_d^-1 (d_ε − d_obs); with G of size m × n only the transposed product is defined. The code is released (p. 16, l. 490), so the computed results may be unaffected; a reader implementing the equations as printed cannot reproduce them, hence moderate. These points were noted outside their checklists by S1, S2, S4 and SD and raised by no instance; GB-13 cites eq. 5 for the symbol ε_m, and GB-17 treats the inverse in eq. 19; this finding concerns the relation sign, the kernel sign, the Jacobian and the transpose. |
| Suggestion | In Section 3.2 write eq. 5 with "=" or "∝" between posterior and likelihood times prior, eq. 9 as C_m(i,j) = σ_m² exp(−s_ij²/L²), eq. 12 as G = A · diag(exp(ε)) and eq. 14 as G^T C_d^-1 (d_ε − d_obs), and check that the code uses these forms. |
| Status | printed forms: verified (page images p. 6 and 7); consequences: inferred (dimension argument and Python) |
| Severity | moderate |
| Source | ZF |

**GB-16 The Gaussian and weak non-linearity assumption is not checked, yet its uncertainty outputs decide the ranking of the data sets and the marking of low-confidence areas.**

| Field | Content |
|---|---|
| Check | P27 |
| Location | p. 6, l. 177 to 178; p. 8, l. 220 to 225 |
| Quotation | "We assume weak nonlinearity, where our forward model can be linearized around the prior, hence, the a posteriori probability density remains approximately Gaussian." |
| Concern | Posterior covariance, resolution and normalised uncertainty all rest on this assumption, and they steer later steps: the ranking of zircon, XRD and combined data (0.87, 0.82, 0.86; p. 14, l. 436; p. 15, l. 442 and 447), the hatched low-confidence areas (Figs. 5b and 14 to 16) and the uncertainty column of Figure 10. With σ_m = 3 in log space, the prior one-standard-deviation range spans a factor e^3 = 20.1 in erosion rate and two standard deviations e^6 = 403 (Python), a range over which the exponential forward model (eq. 3) is strongly non-linear. Search of p. 1 to 16 for "MCMC", "Markov", "sampling of": 4 hits (p. 2, l. 53 and 57; p. 4, l. 120 and 124), all in the Introduction, where the approach is contrasted with sampling methods; no comparison is made. GB-09 cites p. 6, l. 177 to 178 for the positioning against Niu et al. (2020); this finding concerns the unchecked assumption. |
| Suggestion | Check the linearised posterior covariance against a sampling estimate (MCMC on the synthetic case, or an ensemble of inversions with perturbed data and prior) in Section 3.3 or 4.1, at least for the natural runs where the uncertainty values decide the comparison. |
| Status | verified (assumption stated, no check found); inferred (degree of non-linearity) |
| Severity | moderate |
| Source | SD |

**GB-17 The quasi-Newton update in eq. 19 inverts a matrix that is singular for the manuscript's own underdetermined problem.**

| Field | Content |
|---|---|
| Check | P25 |
| Location | p. 8, l. 219; p. 6, l. 170 to 172 |
| Quotation | "Our inverse problem is underdetermined: the number of tracers, representing the data we have, is smaller than the number of pixels for which we want to infer the erosion rates." |
| Concern | G has m rows (tracers, 21) and n columns (pixels), with m smaller than n by the manuscript's own statement. G^T C_d^-1 G is then an n × n matrix of rank at most m and has no inverse; eq. 19 (page image p. 8) inverts exactly this term, while eq. 20 (p. 8, l. 225) adds C_m^-1 inside the inverse. As printed, the update cannot be computed; the results suggest that a different Hessian or a pseudo-inverse was used. Which one? GB-13 cites eq. 19 for the iteration index ε_k; this finding concerns the inverse. |
| Suggestion | Give in Section 3.2 the Hessian actually used (for instance G^T C_d^-1 G + C_m^-1, as in eq. 20, or a damped or pseudo-inverse) and state the number of pixels n. |
| Status | inferred (rank argument from the dimensions stated in the manuscript), asked as a question |
| Severity | moderate |
| Source | SD |

**GB-18 The posterior uncertainty metric appears under at least six names and two symbols, and two different quantities, a per-pixel ratio of square roots and a scalar ratio of traces, share the name "normalised posterior uncertainty".**

| Field | Content |
|---|---|
| Check | P38, P2, P3 |
| Location | p. 8, l. 236 to 239; p. 10, l. 303; p. 10, l. 306; p. 11, l. 335; p. 14, l. 436; Fig. 5f and 5h (p. 26); Figs. 7 to 9, middle panels (p. 28 to 30); Fig. 10, column 2 (p. 31); Figs. 14 to 16 (p. 35 to 37) |
| Quotation | "The third metric is the ratio between the posterior model covariance and the “prior” model covariance." and "The same pattern is visible in the normalised posterior variance" and "The posterior covariance follows a similar trend" |
| Concern | Offering three complementary posterior metrics is a strength of Section 3.3. The third is named inconsistently (all forms read on page images): a ratio of posterior to prior model covariance (p. 8, l. 236 to 237, wording in the Quotation field), defined in eq. 22 (p. 8, l. 239) as a ratio of square roots, that is of standard deviations per pixel; "normalised posterior variance" (p. 10, l. 303); "Normalised posterior covariance" (Fig. 5f); "Normalised covariance trace" (Fig. 5h); "The posterior covariance" (p. 10, l. 306, citing Fig. 5H); "Posterior uncertainty" with axis "Trace(post. cov.)" (Figs. 7 to 9); "Normalised posterior uncertainty" with axis "Trace(post.covar.)" (Fig. 10); "normalized posterior uncertainty" (p. 11, l. 335; p. 15, l. 441 and 446 to 447); and "total normalized uncertainty" defined as tr(C_m,post)/tr(C_m) without square root (p. 14, l. 436). Two quantities result: a per-pixel square-root ratio (eq. 22; map panels of Figs. 5f and 14 to 16) and a scalar trace ratio (p. 14, l. 436; labels 0.87, 0.82 and 0.86 in Figs. 14 to 16). For values below 1 they differ: the square root of 0.87 is 0.93 (Python). The values plotted as "Trace(post. cov.)" lie between 0.7376 and 0.96 (measured, Figs. 7 to 9), the same range as the normalised trace in Fig. 5h (0.733 to 0.7425), while the posterior covariance diagonal in Fig. 5e spans about 2 to 8 per pixel; the axes therefore show normalised traces, not traces. The scalar used in all comparisons of Section 4 is defined only in the zircon paragraph. GB-26 cites p. 8, l. 235 to 238 for the pairing of resolution and normalised uncertainty in the maps; this finding concerns the names and definitions. |
| Suggestion | In Section 3.3 (p. 8, l. 236 to 239) define two named quantities, for example "normalised posterior standard deviation" per pixel (eq. 22) and "total normalised posterior variance" tr(C̃_m)/tr(C_m) as a numbered equation, use one symbol for the posterior covariance, and relabel p. 10, l. 303 and 306, p. 11, l. 335, p. 14, l. 436, p. 15, l. 441 and 446, and the titles and axes of Figs. 5, 7 to 10 and 14 to 16 accordingly. |
| Status | names and symbols: verified (page images); plotted values: verified (measured by AB); identification of the axes with the trace ratio: inferred |
| Severity | moderate |
| Source | S2, S3, AB |

**GB-19 The XRD acquisition and processing chain cannot be rebuilt from the text, and the data availability statement does not say which stages of it and which sample metadata are released.**

| Field | Content |
|---|---|
| Check | P12, P35, P8 |
| Location | p. 9, l. 250 to 257; p. 13, l. 396 to 398; p. 16, l. 490 |
| Quotation | "In a third step, the WinXRD Peak Finder algorithm corrects for baseline drift and removes the background noise, facilitating the identification of local maxima through thresholding and peak fitting" and "the diffractograms are aligned to a pure quartz pattern (Butler et al., 2019)" and "The data and codes used for the inversion tests in the study are available at https://doi.org/10.5281/zenodo.17120374" |
| Concern | Section 3.4 describes the path from diffractogram to fingerprint in six numbered steps and Figure 3 illustrates it, which makes the chain easy to follow. Not stated: diffractometer, radiation, 2θ range, step and counting time, sample mount and grinding size (search of p. 1 to 16 for "diffractomet", "Bruker", "kV", "Cu K", "scan": 0 hits); WinXRD version, threshold and peak-fit settings (search "WinXRD" or "Peak Finder": 3 hits, p. 9, l. 254, p. 13, l. 396, p. 15, l. 473; "threshold": 3 hits, p. 2, l. 51, p. 4, l. 118, p. 9, l. 255, none with a value); the origin of the pure quartz pattern (1 hit, p. 9, l. 256); the diagnostic 2θ windows of the 21 minerals; the number of rock samples per unit ("collected from every lithological unit", p. 9, l. 251) and how they are combined into one fingerprint; and the number, dates and sites of the detrital samples (p. 13, l. 406 to p. 14, l. 407; p. 14, l. 413). The availability statement names only "data and codes used for the inversion tests". The Zenodo record (version 1.0.0, CC BY 4.0, one zip archive) could be opened but not its archive; the repository README of the GitHub main branch lists "Raw XRD data and RRUFF files" without saying whether these are instrument output or WinXRD peak lists. None of the data concern persons. GB-12 cites p. 9, l. 249 to 265 for the place of the XRD limits; this finding concerns the settings and their availability. |
| Suggestion | Add to Section 3.4 a table of instrument settings, processing parameters (WinXRD version, thresholds, peak function, quartz reference) and window definitions, and the number of samples per unit; in "Code and data availability" (p. 16, l. 490) list the released items by stage (raw diffractograms, WinXRD output, aligned and binned peak areas, sample table with IDs, coordinates and dates). |
| Status | wording and searches: verified (`text.json` and page images p. 9, 13, 14, 16); repository content: inferred from the GitHub README (main branch), not from the Zenodo archive |
| Severity | moderate |
| Source | S2, SD |

**GB-20 The averaging that is meant to mitigate peak overlap leaves several of the 21 "minerals" with identical values, so the tracers are fewer and less mineral-specific than stated.**

| Field | Content |
|---|---|
| Check | P31 |
| Location | p. 9, l. 259 to 260; p. 16, l. 475 to 476; Fig. 11 (p. 32) |
| Quotation | "Sixth, to mitigate peak overlap, we average the total peak area within the 2θ windows corresponding to each mineral, rather than relying on individual peaks." and "Averaging peak areas across multiple 2θ values for the same mineral also reduces the possible impact of peak overlap" |
| Concern | The effect of this step is stated, not measured. Bar widths in Fig. 11, measured at three heights per bar with identical results (units in caption order): annite and phlogopite 0, 66, 38, 69, 26, 80, 66 px in both; muscovite equal to them in 6 of 7 units; anorthite and pyroxene 0, 17, 123, 47, 122, 3, 52 px in both; ankerite and dolomite equal in 6 of 7; antigorite and chrysotile close (121 and 110, 63 and 60, 70 and 71 px). These pairs act as one tracer: the 21 minerals (p. 13, l. 393) give at most 21 − 2 − 1 − 1 = 17 distinct tracer columns (Python), 16 if the serpentine pair is merged. The mineral labels of Figs. 11, 15 and 16 suggest mineral-specific abundances that the windows do not separate, and the tracer count and JS distances refer to partly duplicated columns. The synthetic result that 7 tracers suffice (p. 12, l. 360) suggests that the maps may hold, hence moderate. GB-12 cites p. 9, l. 249 to 265 for the place of the XRD limits, GB-36 uses Fig. 11 for research question 1, and GB-48 compares Fig. 11 with Fig. 15; this finding concerns duplicated columns. Do the windows of these pairs overlap? |
| Suggestion | List each diagnostic window (2θ range and RRUFF reference) in Section 3.4 or a supplement, state which windows overlap, merge overlapping minerals into group tracers (micas, carbonates, serpentine, and the shared anorthite and pyroxene window), relabel Figs. 11, 15 and 16, and recompute the JS values and tracer counts. |
| Status | widths: verified (measured on page image p. 32); shared windows as cause: inferred, asked as a question |
| Severity | moderate |
| Source | SD |

**GB-21 The sources of the geological map, the outcrop layer and the land cover are named only inside Figure 4 and are neither referenced nor covered by the availability statement.**

| Field | Content |
|---|---|
| Check | P12 |
| Location | p. 9, l. 270 to 272; Fig. 4 (p. 25), credits below the inset maps; p. 16, l. 490 |
| Quotation | "Figure 4 shows the study area, with the inferred geology, outcrops and land cover." and Figure 4 credit "Land cover data: SwissTopo 2018" |
| Concern | Figure 4 credits its data sources, which is good practice: "Land cover data: SwissTopo 2018" and "Geological data: data from Steck et al., 2015, personal communication by L. Baumgartner, outcrops by GeoCover" (page image p. 25). These sources are named nowhere else: SwissTopo and GeoCover are not in the reference list (search of `text.json`, all pages, for "topo", "geocover", "geo cover", "personal comm": 0 hits), and a personal communication is not accessible. The geological map is one of the four inputs (matrix A, p. 6, l. 167; p. 14, l. 408) and enters all tests; scenario 1 additionally uses a modified map and the map of Steck et al. (2015) (p. 11, l. 327 to 334). The availability statement does not say whether the inferred raster, the modified map and the Steck map are released; the README names "a geological map" without file name. GB-22 concerns the identity of these maps, GB-23 the names of their units, and KK-11 the spelling in the legend; this finding concerns their sources. |
| Suggestion | Add SwissTopo (product, version, year) and GeoCover (sheet, version) to the reference list and cite them at p. 9, l. 270 to 272; state which parts of the inferred map rest on the personal communication; name the three geological rasters of the tests and their files in "Code and data availability" (p. 16, l. 490). |
| Status | verified (page images p. 9, 11, 16, 25; searches); repository content: inferred from the README (main branch) |
| Severity | moderate |
| Source | S2 |

**GB-22 It is not stated whether the "original geological map", the "inferred geology" of Figure 4 and the maps of the natural tests are the same map, and Figure 4 credits Steck et al. (2015) while scenario 1 treats their map as the most different one.**

| Field | Content |
|---|---|
| Check | P38, P8 |
| Location | p. 9, l. 270; p. 11, l. 327 to 334; p. 11, l. 339; Fig. 7 (p. 28), map titles and left scatterplot; Fig. 4 (p. 25), legend heading and credits |
| Quotation | "the lithological unit boundaries of the original geological map and those of the modified map" and "3) the map proposed by (Steck et al., 2015) with the biggest area mismatch" |
| Concern | The map that generated the synthetic data is called "original geological map" (p. 11, l. 331 and 339), "Originial geology (same as forward)" and "Forward geology" (Fig. 7); the study area map is "inferred geology" (p. 9, l. 270; Fig. 4 legend heading "Inferred geology and outcrops"); the natural tests use "the geological map of the entire catchment" (p. 14, l. 408) and "Geology" panels (Figs. 14 to 16). The manuscript never states that these are one map. Figure 4 credits "data from Steck et al., 2015" as its geological source, while scenario 1 uses "the map proposed by (Steck et al., 2015)" as the map with the largest mismatch to the original; how the "minimal changes" map was made is not stated either. Is the original map of scenario 1 the inferred map of Figure 4, and is it also used in the natural tests? What distinguishes it from the map of Steck et al.? GB-21 cites the same lines for the sources of the maps; this finding concerns their identity. |
| Suggestion | At p. 9, l. 270 to 272 give the inferred map one name (for example "reference geological map") and state that it is used in the forward model of all synthetic tests and in all natural tests; in Section 4.1.3 (p. 11, l. 327 to 334) describe how the Steck et al. (2015) map and the minimal-change map differ from it (source figure, scale, unit merging). |
| Status | names: verified (page images p. 9, 11, 14, 25, 28); identity of the maps: assumption, asked as a question |
| Severity | moderate |
| Source | S2, SD |

**GB-23 The seven lithological source units carry different names and unresolved abbreviations in the geology text, Section 4.2, and the legends and captions of Figures 4, 5 and 11 to 16.**

| Field | Content |
|---|---|
| Check | P38, P29 |
| Location | p. 9, l. 273 to p. 10, l. 279; p. 10, l. 299; p. 14, l. 411; p. 14, l. 414; p. 14, l. 431 to 434; Fig. 5 (p. 26), legend of panel j; Figs. 4 and 12, legends; Fig. 11, caption; Fig. 13, curve labels; Figs. 14 to 16, legends and titles |
| Quotation | "while Penninic Mesozoic sedimentary units (Bündnerschiefer) consist mainly of calcareous mica schists and quartzites" and "the Monte Rosa garnet-gneiss (MR g-g) unit" |
| Concern | The units are well described petrographically (p. 10, l. 274 to 279). Their names change (all read on page images): (1) the sedimentary unit is "Penninic Mesozoic sedimentary units (Bündnerschiefer)" in the geology text but "Zermatt Saas-Fee sediments" (p. 10, l. 299), "Zermatt - Saas Fee sediment unit" (p. 14, l. 411), "ZSF sediments" (p. 14, l. 414; Figs. 5, 11, 13, 15, 16) and "Zermatt - Saas Fee sediments" (Figs. 4, 12); only the Figure 4 outcrop entry ("metamorphic bündnerschiefer") shows that these are the same unit. (2) The second Monte Rosa unit has five names: "garnet-mica schists" (p. 10, l. 276), "Monte Rosa (garnet gneiss and micaschist)" (Figs. 4, 12), "Monte Rosa (gneiss, micaschist)" (Figs. 11, 13), "MR gneiss, mica" (Figs. 5, 15, 16) and "Monte Rosa garnet-gneiss (MR g-g)" (p. 14, l. 432). (3) The Stockhorn unit appears as "The Stockhorn, Tuftgrat, and Gornergrat units" (p. 10, l. 276), "Stockhorn basement, Tuftgrat Mesozoic and GornergratPermo-Mesozoic" (Figs. 4, 12), "Stockhorn-Turftgrat-Gornergrat" (Fig. 11), "Stockhorn, Tuftgrat, Gornergrat" (Fig. 13) and "S.,T.,G." (Figs. 5, 15, 16). (4) The geology paragraph describes five groups, the figures use seven units (Figure 4 legend: 7 unit entries besides the outcrop lines); the mapping is not given. (5) Abbreviations: search of `text.json`, p. 1 to 16, case-sensitive: "ZSF" 2 hits (p. 14, l. 414 and 431), "MR" 2 hits (p. 14, l. 432 and 433), "S.,T.,G" 0, "ELA" 0, "Zr" 0; "S.,T.,G." (legends) and "ELA estimation" (Fig. 4 legend) are resolved nowhere, "ZSF" and "MR" only late in the text and in no caption, and "Zr" (Fig. 14 caption "using Zr fingerprint data", Fig. 14 axis "Normalised abundance per Zr age bin", Fig. 16 title "combined XRD and Zr data") is the element symbol where the text says "zircon". KK-09 treats hyphenation of "Zermatt-Saas Fee" and KK-19 the spellings "Turftgrat" and "ecologites"; GB-26 (resolution, p. 10, l. 299 to 301), GB-36 (fingerprints, p. 10, l. 274 to 278), GB-37 (subcatchment test, p. 14, l. 410 to 416), GB-41 (zircon matrix, p. 14, l. 430 to 434) and GB-54 (Fig. 5) cite the same places for other matters; this finding concerns the names and abbreviations. |
| Suggestion | At p. 10, after l. 279, introduce the seven units once with a fixed name and abbreviation (for example in a short table linking each unit to the geology text and the Figure 4 legend), use exactly these names at p. 10, l. 299, p. 12, l. 340 and p. 14, l. 411 to 434 and in Figs. 4, 5 and 11 to 16, resolve "S.,T.,G." and "ELA" (equilibrium line altitude, if meant) in the captions, and write "zircon" instead of "Zr" in Figs. 14 and 16. |
| Status | verified (page images p. 9, 10, 14, 25, 26, 32 to 37; abbreviation counts in `text.json`) |
| Severity | minor |
| Source | S2, AB |

#### Minor corrections

| ID | Location | Quotation | Replacement | Source |
|---|---|---|---|---|
| KK-04 | p. 5, l. 146 (first of 28 panel references with 33 panel letters); p. 11, l. 319 (last) | "Figure 1B" and "(Figure 6D, 6E and 6F )" | "Figure 1b" and accordingly for all panel references, as the panels are labelled "(a)" to "(k)"; at p. 11, l. 319 "(Figure 6d, 6e and 6f)" without the space before the parenthesis (page image p. 11). Count: Python on `text.json` plus the line-broken references "Figure 3C" and "Figure 6C". GB-12 cites p. 5, l. 145 to 152 for the storage assumption; this correction concerns letter case and spacing. | AB, S4 |
| KK-05 | p. 6, l. 181 | "becomes Tarantola (2005):" | "becomes (Tarantola, 2005):" | S4 |
| KK-06 | p. 8, l. 236 | "considerately" | "considerably". GB-18 and GB-26 cite this line for the uncertainty metrics; this correction concerns the word only. | S4, SD |
| KK-07 | p. 9, l. 245 | "weighed by the model covariance" | "weighted by the model covariance" | S4 |
| KK-08 | p. 9, l. 267; p. 9, l. 272; p. 10, l. 282; p. 13, l. 392; p. 13, l. 400; p. 15, l. 463; p. 16, l. 498; p. 16, l. 499; Fig. 11 caption; legends of Figs. 5, 15 and 16 | "Gorner-gletscher catchment" and "Gornergletscher" and "Gorner Glacier" and "Gorner gletscher catchment" and "Gorner glacier" | One form throughout, for example "Gorner Glacier"; 5 forms in 12 places, each read on the page image. GB-21 cites p. 9, l. 270 to 272 for the map sources, GB-20, GB-35, GB-36 and GB-48 cite Figure 11, KK-14 and GB-36 cite p. 13, l. 400, and GB-42 cites p. 15, l. 463 for other matters; this correction concerns the glacier name only. | S2, S4 |
| KK-09 | p. 9, l. 273 to p. 10, l. 274; p. 10, l. 299; p. 12, l. 340; p. 14, l. 411; p. 14, l. 414; Figs. 4 and 12, legends; Fig. 12 caption | "Zermatt Saas-Fee" and "Zermatt-Saas-Fee" and "Zermatt - Saas Fee" and "Zermatt- Saas Fee" | "Zermatt-Saas Fee" in all places, as at p. 9, l. 273 to p. 10, l. 274 and p. 14, l. 431 and 432; compared on the page images: all 7 occurrences of "Zermatt" on p. 1 to 16 plus the Figure 4 and 12 legends and the Figure 12 caption. The unit names themselves are treated in GB-23; GB-21 and KK-11 cite Figure 4 for its sources and legend spelling, and GB-26, GB-36 and GB-37 cite p. 10, l. 299 to 301, p. 10, l. 274 to 278 and p. 14, l. 410 to 416 for other matters; this correction concerns hyphens and spaces only. | S2, S4 |
| KK-10 | Fig. 3c (p. 24), legend | "quarz pattern alignment" | "quartz pattern alignment" (text "quartz": p. 9, l. 256; p. 13, l. 397; p. 15, l. 473) | S2, AB |
| KK-11 | Fig. 4 (p. 25) and Fig. 12 (p. 33), legends | "GornergratPermo-Mesozoic" and "biotite schits" and "caclcite-zoisite amphibolites" and "silimanite-biotite gneiss" and "calcarious mica schist" | "Gornergrat Permo-Mesozoic"; "biotite schists"; "calcite-zoisite amphibolites"; "sillimanite-biotite gneiss"; "calcareous mica schist" (both legends read on the page images, same wording). GB-21 and GB-23 cite Figure 4 for its sources and unit names, and KK-09 the hyphenation of the unit name in the same legends; this correction concerns spelling. | AB |

#### Verification log

| ID | Check | Checked | Values | Result |
|---|---|---|---|---|
| PP-08 | P10, P9, P31, P7, P35, P19, P17 | Design sketch from the whole manuscript, including captions and figure pages | Type: method development with synthetic forward-inverse tests and a natural case study; aim p. 3, l. 63 to 64; research questions p. 10, l. 280 to 285; cases: 7 units, 21 tracers, pixel size 300 m, number of pixels not stated; data sources: synthetic fingerprints and map, geological map partly inferred, XRD of source rocks and suspended sediment, zircon ages (measured for 4 of 7 units, assigned for 1, absent or near absent for 2), export estimate (origin not given), prior "average true erosion rate"; declared principles: ideal fingerprint criteria, window averaging, same protocol for source and detritus, positivity by log space, stopping rule p. 9, l. 243 to 244 | Basis of GB-01, GB-06, GB-12, GB-16, GB-17, GB-20, GB-24, GB-30, GB-36, GB-37, GB-40 to GB-42; disclosed limits listed there |
| PP-09 | P12, P35 | Presence and reachability of the availability statement | Statement p. 16, l. 490 with DOI 10.5281/zenodo.17120374; DOI resolves to the Zenodo record, version 1.0.0, published 15 September 2025, CC BY 4.0, open access, one file Non-Linear-XRD-Inversion-v1.0.0.zip (49.3 MB), description "This release contains the code and data to reproduce the results in the article"; archive preview not readable, GitHub README (main branch) read instead | no finding for presence and reachability; coverage of single sources in GB-19, GB-21, GB-39, GB-40 |
| PP-10 | P12 | Sources covered by manuscript or repository | RRUFF reference spectra cited (Lafuente et al., 2015) and listed in the README; synthetic fingerprints, true map and inversion code listed in the README; raw XRD and raw zircon data listed in the README; Bearth (1953) and Steck et al. (2015) in the reference list | no finding for these sources; limit: README of the main branch, not the archived version |
| PP-11 | P38 | Abbreviations of methods and measures | SD defined p. 7, l. 210 to 211; QN defined p. 7, l. 211 and used 6 further times; MAP defined p. 6, l. 173; JS defined p. 12, l. 345; PCA p. 12, l. 356; KDE defined in the Figure 13 caption | no finding |
| PP-12 | P4 | Equation numbering and references | Equations 1 to 22 consecutive; references to eq. 7 (p. 7, l. 191; p. 8, l. 240; p. 9, l. 245), eqs. 10 to 15 (p. 7, l. 200 and 204), eq. 16 (p. 8, l. 213 and 217), eqs. 1 to 4 (p. 9, l. 263); each target holds the quantity named | no finding (content of single equations in GB-15, GB-17) |
| PP-13 | P7, P30 | Validity of the described method over all runs and reported errors | SD gradient normalisation introduced after "initial experiments" (p. 11, l. 312), reported SD run is the normalised one; QN for all later tests (p. 11, l. 320); 100 iterations in the first QN test, 25 in later runs; one reported error (SD instability), corrected before the reported run | no finding |
| PP-14 | P19 | Provenance class per core statement | Results subsections: 4 of 6 synthetic, 2 of 6 natural; zircon fingerprints measured for 4 of 7 units (57.1 %), assigned for 1 (14.3 %), empty for 2 (28.6 %) (Python); XRD fingerprints measured for 7 of 7; geology under ice inferred (area share not stated) | Classes named in the text; assigned zircon values unmarked in figures (GB-49); export estimate of unknown class (GB-40) |
| PP-15 | P26, P31 | Guarantees and intent statements across all paths | Positivity by log space holds in every run; normalisation to the sample maximum (p. 9, l. 261 to 264) applies to all samples; "should help cancel out such effects" (p. 15, l. 472 to 473) in GB-06; overlap mitigation in GB-20; quartz alignment and Peak Finder "helps normalize" (p. 16, l. 474) not measured, no stated result depends on it beyond GB-36 | no finding beyond GB-06, GB-20, GB-42 |
| PP-16 | P17 | Further disclosed limits at their place | Inferred geology under ice at the map introduction (p. 9, l. 270 to 272); lower resolution of small units at the result (p. 10, l. 299 to 300); prior equal to the true mean disclosed at p. 13, l. 375, consequence in GB-24 | no finding |
| PP-17 | P14 | Collins et al. (2020), already in the reference list (p. 18, l. 548 to 551), as support for the steps proposed in GB-06 and GB-37 | Full-text HTML at https://link.springer.com/article/10.1007/s11368-020-02755-4 read through a fetch summary: conservativeness tests, comparison of source and target particle size and mixture tests named as key steps | Not new literature; may be cited in Sections 3.4 and 4.2.1 (wording of the source not verified) |
| PP-18 | P3, P29, P4 | Inventory, numbering and first citation of all figures; panel references against captions | 16 figures on p. 22 to 37, numbered without gap, all cited in order from p. 5, l. 146 (Fig. 1) to p. 15, l. 445 (Fig. 16); no graphical abstract, tables or appendix figures; panel references 1A to 1D, 2A to 2C, 3A to 3E, 5A to 5K, 6C to 6G checked against captions and page images | All targets exist and show what is referred to, except p. 11, l. 317 (GB-29) and p. 6, l. 167 (GB-14); letter case in KK-04 |
| PP-19 | P3 | Scale bars of the catchment maps against each other | East-west extent divided by scale bar: Fig. 4 13.2 km, Fig. 12 13.1 km, Fig. 14 13.3 km, Fig. 15 13.2 km, Fig. 16 13.2 km | no finding |
| PP-20 | P29 | Font size of the remaining figures | Cap or digit height in the 300 dpi page image: Fig. 4 legend 6.3 pt; Fig. 5g ticks 6.0 pt; Fig. 5j legend 5.7 pt; Fig. 7 ticks 5.7 pt; Fig. 8 5.7 pt; Fig. 9 5.7 pt; Fig. 11 6.7 pt; Fig. 13 8.0 pt; Figs. 1 to 3 larger | no finding (within the tolerance of 0.6 pt below 6 pt); Figs. 4 (inset), 10 and 14 to 16 in GB-47 |
| PP-21 | P24 | Dated events against figures | Only dated event: the detrital sample of 28 June 2019, 13:30 (p. 14, l. 423 to 424); no figure has a time axis or dated markers | no finding (P24 not applicable) |

### Segment 3: Results (p. 10 to 15, Figures 5 to 16)

#### Substantive findings

**GB-24 The synthetic tests behind the recovery and robustness claims give the inversion the true mean erosion rate as prior, tune the hyperparameters against the true map, and use a single true map with one hotspot.**

| Field | Content |
|---|---|
| Check | P9 |
| Location | p. 10, l. 288 to 289; p. 10, l. 295; p. 11, l. 325 to 326; p. 13, l. 374 to 376; p. 16, l. 482 to 483 |
| Quotation | "a prior equal to the average true erosion rate" and "Through forward-inverse testing, we optimize the hyper-parameters" and "we show that the true erosion pattern can be reliably recovered, and that the method is robust across a range of parameters" |
| Concern | The forward-inverse design with a known truth is the right instrument for a new inversion, and the manuscript itself notes that a long smoothing distance pulls the solution "closer to the prior (set here as the average true erosion rate)" (p. 13, l. 375). The consequence is not drawn. (1) The prior mean carries information about the truth that no field application has; the closer the solution stays to it, the better the score: in Fig. 10, row 1, the total absolute difference falls from 256.8 at the smallest L to 76.2 at L = 3000 m, a factor of 3.37 (measured, Python). (2) The hyperparameters were chosen by comparison with the true map (p. 5, l. 137; Fig. 10) and transferred unchanged to the natural runs (p. 14, l. 426 to 428). (3) Every synthetic test uses one true map "featuring a localised hotspot" (p. 10, l. 288 to 289); scenario 1 shows that the score depends on where unit boundaries lie relative to this hotspot (p. 11, l. 338 to p. 12, l. 341). The reported errors are thus a best case for one pattern under a truth-informed prior, and the general claims at p. 16, l. 482 to 483 and p. 1, l. 7 go beyond this design. GB-25 treats the missing settings and construction rules of the same tests, and GB-30 the missing noise scenario. |
| Suggestion | Repeat Section 4.1 with a prior derived only from information available in a field case (for instance the export estimate divided by catchment area, also deliberately biased by factors 0.5 and 2), with hyperparameters fixed before comparison with the truth or chosen by a data-only criterion, and over an ensemble of true maps (several hotspot positions and sizes, a lithology-controlled pattern, a uniform map); report the distribution of errors and restrict p. 16, l. 482 to 483 and p. 1, l. 7 to what the ensemble shows. |
| Status | verified (prior, tuning and single map stated; Fig. 10 values measured by AB); inferred (that the errors are optimistic for field use) |
| Severity | major |
| Source | SD |

**GB-25 The settings and construction rules of the synthetic tests are given completely only for the degradation tests; the QN test, the SD test, the parameter sweeps and the construction of the synthetic data, the blended fingerprints and the PCA subsets are incompletely specified.**

| Field | Content |
|---|---|
| Check | P11, P8 |
| Location | p. 10, l. 290; p. 10, l. 293 to 294; p. 11, l. 310 to 311; p. 12, l. 343 to 349; p. 12, l. 355 to 357; p. 12, l. 367 to 371 |
| Quotation | "After several iterations, the inversion yields an a posteriori erosion rate map (Figure 5B)" and "In a first test, we use the QN approach with 100 iterations" and "this time using the steepest descent approach in the inversion method." and "We perform a Principal Component Analysis (PCA) to retain the subset of tracers that explain the maximum variance in the mineralogical fingerprints." |
| Concern | Matrix of tests against settings (iterations, L, σ_m, σ_d, prior, step size µ): Section 4.1.3 (p. 11, l. 324 to 326) and Section 4.2.2 (p. 14, l. 426 to 428) give all six. Section 4.1.1 gives five, without step size, and says "After several iterations" (p. 10, l. 290) next to "100 iterations" (l. 293). Section 4.1.2 (SD) gives none; the iteration axes of Fig. 6g to 6i run to 200 while the text mentions only "after 125 iterations" (p. 11, l. 316), and the gradient normalisation (p. 11, l. 312) is not specified. Section 4.1.4 does not state the values held fixed while one parameter is swept; they can only be inferred from the baseline error of about 197.4 in Fig. 10, rows 2 and 3. Section 4.2.1 gives no settings (GB-37). Not specified either: how the 21 synthetic fingerprints (Fig. 5k) were generated, position, amplitude and width of the true hotspot, whether noise was added (GB-30), the blending weights of the 20 steps (p. 12, l. 343 to 349), and the rule that turns a PCA, which yields components, into a ranked subset of tracers (p. 12, l. 355 to 357). The reproducibility of Figs. 6, 8 to 10 therefore depends on the code archive. GB-24 treats the prior and tuning of the same tests; the formula of R is asked in GB-26 and the hatching criterion in GB-44; this finding concerns the settings and construction rules. |
| Suggestion | Add to Section 4 (after p. 10, l. 285) a parameter table with one row per test (4.1.1, 4.1.2, 4.1.3, 4.1.4 baseline, 4.2.1, 4.2.2) and columns iterations, L, σ_m, σ_d, prior, µ and gradient normalisation, and a short subsection or appendix with the construction rules of the synthetic fingerprints, the true map, the blending and the PCA ranking; replace "After several iterations" at p. 10, l. 290 by the number used. |
| Status | missing settings and rules: verified (p. 10, l. 286 to p. 14, l. 429); baseline value in Fig. 10: verified (measured by AB) |
| Severity | moderate |
| Source | S3, SD |

**GB-26 In Figures 5, 6 and 14 to 16 the resolution diagonal is lowest where the normalised posterior uncertainty is lowest, the reverse of the pairing that the definitions on p. 8 imply.**

| Field | Content |
|---|---|
| Check | P3 |
| Location | p. 10, l. 299 to 301; p. 8, l. 235 to 238; p. 14, l. 436; Fig. 5d and 5f (p. 26); Fig. 6d and 6f (p. 27); Figs. 14 to 16, panels "Resolution diagonal" and "Normalised posterior uncertainty" (p. 35 to 37) |
| Quotation | "Where the diagonal of R is close to 1, data have improved our knowledge considerately relative to the prior." and "values closer to zero indicate a maximal variance reduction after the inversion" and "low resolution, and a high total normalized uncertainty" |
| Concern | By these definitions a pixel well constrained by the data should show a resolution diagonal near 1 and a normalised uncertainty near 0. Map colours matched to the colour bars (block means of 20 × 20 px, colour bars calibrated on ticks): Fig. 5, hotspot resolution 0.950 and normalised uncertainty 0.399, eastern block 0.985 and 0.821; Fig. 15, hotspot 0.80 and 0.255, bulk of the domain 0.97 and 0.89; Fig. 14, lowest resolution 0.48, lowest normalised uncertainty 0.19, bulk 0.93 and 0.90; Fig. 6 shows the same pattern. Where the data reduce the variance most, the resolution is lowest; where the variance is hardly reduced, it is close to 1. Consequences: the zircon solution is called "low resolution" (p. 14, l. 436), yet Fig. 14 shows about 0.93 or more over most of the domain; the statement that small units have "lower resolution (Figure 5D)" (p. 10, l. 300) rests on the same panels; and the Conclusions recommend these metrics (GB-54). Is the plotted quantity 1 − diag(R), or is the text on p. 8 inverted? The manuscript gives no formula for R. GB-18 cites p. 8, l. 236 to 239 for the names of the uncertainty metric, and KK-06 the spelling at p. 8, l. 236; this finding concerns the pairing in the maps. |
| Suggestion | Give the formula for R in Section 3.3 (for instance R = C̃_m G^T C_d^-1 G); check whether the panels show diag(R) or 1 − diag(R) and correct titles and colour bars or the text at p. 8, l. 235 to 238, p. 10, l. 299 to 301 and p. 14, l. 436; report trace(R) next to the total normalised uncertainty. |
| Status | ordering of values between the paired panels: verified (measured); numeric values: inferred (colour matching through semi-transparent maps over hillshade); cause: assumption, asked as a question |
| Severity | major |
| Source | AB |

**GB-27 The error metric and the map mismatch measure of the synthetic tests are named differently in text, captions, panel titles and axes, and the symbol e is not defined.**

| Field | Content |
|---|---|
| Check | P38 |
| Location | p. 10, l. 305; p. 11, l. 330; p. 11, l. 334 to 336; p. 12, l. 352; p. 12, l. 361; p. 13, l. 381; Fig. 5g (p. 26); Fig. 7 (p. 28), caption, axes and colour bar; Figs. 8 and 9, left scatterplots; Fig. 10, first column (p. 31) |
| Quotation | "the difference between the true and posterior erosion rates initially decreases" and "quantified by area mismatch (expressed in m2 ) between the lithological unit" |
| Concern | (1) The summed deviation between true and posterior maps is "the difference between the true and posterior erosion rates" (p. 10, l. 305), the sum of difference between the true and the posterior erosion map (Fig. 5 caption, panel g), "absolute error" (p. 11, l. 335; p. 12, l. 352 and 361; panel titles of Figs. 7 to 9), "the absolute difference" (p. 13, l. 381) and "Total absolute difference etrue - epost" (Fig. 10 titles), with axis labels "Σ|etrue - epost|" (Figs. 5g, 7 to 9) and "sum|etrue - epost|" (Fig. 10). The symbol e does not occur in Section 3, which uses ė (erosion rate) and ε (log erosion rate), so the reader cannot tell in which of the two the error is computed. (2) The map mismatch is "area mismatch" (p. 11, l. 330, 334, 335), "area difference" (Fig. 7 caption and axes) and "Geology misalignment" (Fig. 7 colour bar). GB-18 treats the uncertainty metric at p. 11, l. 335 and GB-32 the size of the error at p. 12, l. 352; this finding concerns the names. |
| Suggestion | At p. 10, l. 305 define the error metric once with a formula in the symbols of Section 3 and one name, and use it at p. 11, l. 335, p. 12, l. 352 and 361, p. 13, l. 381 and in Figs. 5 and 7 to 10; use "area mismatch" also in the Figure 7 caption, axes and colour bar. |
| Status | verified (page images p. 10 to 13, 26, 28 to 31) |
| Severity | minor |
| Source | S2 |

**GB-28 Quasi-Newton is adopted as "more stable and accurate", but no number compares the two schemes, the runs used different iteration budgets, and the error curves of Figures 5g and 6g end lower for steepest descent.**

| Field | Content |
|---|---|
| Check | P3, P11, P9 |
| Location | p. 11, l. 314 to 316; p. 11, l. 320 to 321; Fig. 5g (p. 26); Fig. 6g (p. 27) |
| Quotation | "more iterations are needed to converge to a posterior result as close to the true erosion rate map as the QN posterior" and "we adopt the Quasi-Newton (QN) approach for all subsequent tests, as it provides a more stable and accurate reconstruction of the erosion rate patterns." |
| Concern | The comparison is an announced aim ("We implement and compare two non-linear inversion schemes", p. 1, l. 4 to 5), but Section 4.1.2 reports it in words only. Both panels show the same metric. Measured: Fig. 5g (QN) ends at 201.0 ± 0.5 after iteration 100, with its minimum of 197.3 ± 0.5 near iteration 22; Fig. 6g (SD) ends at 193.0 ± 0.6 after iteration 200. SD thus ends 8.0 below QN (4.0 %, Python) and 4.3 below the QN minimum, both above the combined uncertainty (at most 1.1). The colour bar of the difference map spans about −2 to 2 for QN (Fig. 5c) and about −1.5 to 1.5 for SD (Fig. 6c). The figures support that QN is faster (minimum near iteration 22; SD plateau from iteration 137 ± 3) and that SD needed gradient normalisation (p. 11, l. 312), not that QN is more accurate; the QN curve also rises again after its minimum, while p. 10, l. 305 to 306 describe a plateau. QN ran 100 iterations (p. 10, l. 293), SD 200 according to the axis of Fig. 6, which the text does not state; step sizes are not given. Which quantity shows QN to be more accurate? GB-27 cites Fig. 5g for the name of the error metric; this finding concerns the comparison of the schemes. |
| Suggestion | In Section 4.1.2 report for both schemes, at an equal iteration budget and under the stopping rule of p. 9, l. 243 to 244, the final summed absolute difference, the normalised uncertainty, the misfits, the number of iterations to convergence and the run time; reword p. 11, l. 320 to 321 accordingly (for example "converges in fewer iterations"). |
| Status | curve values: verified (measured by AB, read consistently by S3 and SD); that QN is not more accurate: inferred; whether another quantity shows it: assumption, asked as a question |
| Severity | major |
| Source | AB, S3, SD |

**GB-29 The reference "(Figure 6G versus Figure 6G)" compares a panel with itself, and the onset of the oscillations is later than stated.**

| Field | Content |
|---|---|
| Check | P4 |
| Location | p. 11, l. 316 to 317 |
| Quotation | "This limited sensitivity to strong gradients also leads to oscillations in the posterior covariance, visible after 125 iterations, as the Jacobian fluctuates between iterations (Figure 6G versus Figure 6G)." |
| Concern | Panel (g) of Figure 6 is the sum of differences between true and posterior map; the covariance evolution is panel (h), "normalised posterior covariance during non-linear iterations" (caption p. 27), which rises and flattens. The comparison partner is not named; presumably Fig. 5h, the same quantity for the QN run. The plateau onset in Fig. 6h measures at iteration 136.6 ± 3 (AB), so "after 125 iterations" is earlier than shown. GB-28 cites p. 11, l. 314 to 316 for the scheme comparison; this finding concerns the panel reference. |
| Suggestion | At p. 11, l. 316 to 317 write the intended pair, presumably "(Figure 6h versus Figure 5h)", and "after about 135 iterations". |
| Status | verified (page images p. 11, 26, 27; onset measured by AB); intended target: assumption |
| Severity | minor |
| Source | S4, S3, AB, SD |

**GB-30 The data degradation scenarios leave out analytical noise in the detrital data and variability within source units, and the data standard deviation is a set value, not a measured one.**

| Field | Content |
|---|---|
| Check | P10 |
| Location | p. 11, l. 323 to 324; p. 9, l. 251; p. 6, l. 185 to 186 |
| Quotation | "We assess the sensitivity of the inversion model to data degradation through three scenarios, each designed to reflect a common source of uncertainty in sediment provenance studies." |
| Concern | The three scenarios are map mismatch, blended fingerprints and fewer tracers. Search of p. 1 to 16 for "noise": 1 hit (p. 9, l. 255, background removal in diffractograms); for "replicat", "repeat", "duplicate", "triplicate": 0 hits. No scenario perturbs the detrital data with measurement error, none resamples the source fingerprints, and no replicate XRD measurement is reported. The number of source samples per unit is not stated (p. 9, l. 251), and A enters as exact, since the data covariance contains only the data variance (eq. 8, p. 6, l. 185 to 186). σ_d = 0.01 mm/y is a setting (Fig. 10 marks 0.003 mm/y instead, GB-34). Whether the synthetic detrital data contained noise is not stated; if not, "consistent convergence" (p. 1, l. 7) was shown on noise-free data. The tested scenarios remain valid; the most common degradation of field data is missing, so the robustness statement is limited rather than wrong, hence moderate. GB-24 treats prior, tuning and single map of the same tests, and GB-19 cites p. 9, l. 251 for the missing sample metadata; this finding concerns the missing noise scenario. |
| Suggestion | Add to Section 4.1.3 a fourth scenario with noise on d at the level of measured XRD repeatability (replicate preparations of at least one detrital and one source sample) and with source fingerprints resampled from several rock samples per unit; state in Section 3.4 the number of source samples per unit and how their spread enters C_d or A; state in Section 4.1.1 whether the synthetic data contain noise. |
| Status | verified (searches, eq. 8, Fig. 10); assumption (noise-free synthetic data), asked as a question |
| Severity | moderate |
| Source | SD |

**GB-31 Scenario 2 tests 20 blended fingerprint sets, Figure 8 plots 14, and the caption accounts for one; five runs are unaccounted for, and "many of these cases" has no count.**

| Field | Content |
|---|---|
| Check | P23, P20, P9 |
| Location | p. 12, l. 348 to 349; p. 12, l. 353; Fig. 8 (p. 29), panels "Absolute error" and "Posterior uncertainty", caption |
| Quotation | "In total, 20 values between the highly blended and the original synthetic fingerprints are tested" and "In many of these cases, the inversion fails to converge to a stable posterior solution." and caption "Note that the most blended example did not have a stable solution and is therefore not plotted." |
| Concern | Counted independently by three instances on enlarged page images (AB at 600 dpi as connected marker fills): 14 markers in the left and 14 in the middle panel (the right panel has overlapping markers near zero, 9 separable), at average JS of 0.249, 0.272, 0.338, 0.359 and then 0.441 to 0.624 in steps of 0.020; 4 of them below 0.44, none between 0.36 and 0.44. Balance (Python): 20 tested − 14 plotted = 6 not plotted; − 1 explained in the caption = 5 unexplained. Resolution A: the 5 further runs did not converge and were omitted like the most blended one; then the panels exclude runs by their outcome. Resolution B: fewer than 20 sets were run or saved. Resolution C: markers overlap; the gaps between 0.27 and 0.34 and between 0.36 and 0.44 make this unlikely. The caption also announces three labelled examples, but only "Medium" and "Unblended" are labelled. Deciding information: the list of the 20 JS values with a convergence flag. GB-32 treats the error threshold of the same scenario, and GB-25 cites p. 12, l. 343 to 349 for the missing blending weights; this finding concerns the number of runs. |
| Suggestion | In Section 4.1.3 after p. 12, l. 353 state how many of the 20 runs did not converge, at which JS values and by which criterion; mark or list the failed runs in Fig. 8 and extend its caption to all omitted runs. |
| Status | counts: verified (page image, measured); balance: inferred (calculated); reason for the missing runs: assumption, asked as a question |
| Severity | moderate |
| Source | S3, AB, SD |

**GB-32 The "absolute error" is a sum over all pixels, but the text reports a threshold of "700 mm/yr" that matches the plotted values in no unit reading and gives neither the number of pixels nor the scale of the true map.**

| Field | Content |
|---|---|
| Check | P20, P3 |
| Location | p. 12, l. 352 to 353; Fig. 8 (p. 29), left scatterplot and y axis; Fig. 5g (p. 26); Figs. 7 and 9, left scatterplots |
| Quotation | "distance decreases below 0.55, both absolute error and posterior uncertainty rise sharply, with errors exceeding 700 mm/yr for JS < 0.44." |
| Concern | All error axes are labelled as sums over pixels ("Σ|etrue - epost|", "sum|etrue - epost|"), without unit, while "mm/y" is also used for single-pixel values (p. 14, l. 435). The baseline of the sum for the unperturbed synthetic case is about 197 (Figs. 7, 9, 10); the true map ranges from about 0.5 to 3 (Fig. 5a colour bar, no unit). Neither the number of pixels nor the summed true rate is given, so neither 197 nor 700 can be related to erosion rates (700/197 = 3.55, Python). Measured absolute errors in Fig. 8 (ticks 0 and 700000): below JS 0.44: 47,270; 677,100; 5,561; 321,800; at JS 0.44 and above: 0 to 19,460 (0.501: 8,342; 0.521: 3,476; 0.541: 19,460). If the axis is in mm/y, 700 is also exceeded at JS 0.50 to 0.54; if "700 mm/yr" corresponds to 700,000 axis units, no marker exceeds it. The unit "mm/yr" occurs only here (search of p. 1 to 21: "mm/yr" 1 hit; "mm/y" elsewhere, p. 10, l. 295; p. 11, l. 325; p. 13, l. 384; p. 14, l. 428 and 435). GB-27 cites p. 12, l. 352 for the name of the error metric, GB-31 treats the number of runs and GB-03 cites p. 12, l. 353 to 354 for the convergence statement of the Abstract; this finding concerns the size and unit of the threshold. |
| Suggestion | In Section 3.3 or 4.1.1 define the absolute error as the sum over N pixels, give N and the summed true erosion rate, and report the error as mean absolute error per pixel or relative to the summed true rate; restate p. 12, l. 352 to 353 in the unit of Figure 8 ("mm/y") with the actual range of the non-converging cases, and give the unit on the y axes. |
| Status | axis labels and text: verified; plotted values: verified (measured by AB); unit readings: inferred |
| Severity | moderate |
| Source | S3, AB |

**GB-33 The ranking of the three degradation scenarios compares perturbations with arbitrary ranges; at the extremes of the tested ranges, tracer reduction degrades the solution more than map uncertainty, contrary to the stated order.**

| Field | Content |
|---|---|
| Check | P21 |
| Location | p. 12, l. 363 to 365; Fig. 7 (p. 28), Fig. 8 (p. 29), Fig. 9 (p. 30), panels "Absolute error" and "Posterior uncertainty" |
| Quotation | "To summarize, among the three tested scenarios, the strongest impact on the posterior solution arises from reduced fingerprint distinctiveness. Geological map uncertainty follows as the second most influential factor." |
| Concern | Each scenario spans a range chosen by the authors: three maps up to an area difference of about 1.15e7 m² (Fig. 7), blending from JS 0.624 to 0.225 (Fig. 8), 1 to 21 tracers (Fig. 9); the effects are not put on a common scale. At the maxima the summed error is 274.8 for the Steck et al. map (Fig. 7), 347.0 for one tracer (Fig. 9) and 677,100 for blending (Fig. 8); the maximum normalised uncertainty is 0.7460, 0.9613 and 0.8926. Tracer reduction thus exceeds map uncertainty in both metrics (347/275 = 1.26, Python) and exceeds blending in uncertainty. The stated order holds only under the qualification "provided that the most informative ones are retained" (p. 12, l. 365), which compares tracer reduction at 7 or more tracers with the full range of the other two scenarios. The Discussion builds on this order (p. 15, l. 456 to 461). GB-22 cites Figure 7 for the identity of the maps and KK-17 corrects a title in it; this finding concerns the ranking. |
| Suggestion | At p. 12, l. 363 to 365 state the order for a defined, comparable perturbation (for example per unit of JS distance lost), or give the maximum error and uncertainty per scenario and restrict the ranking to the tested ranges. |
| Status | text: verified; maxima: verified (measured by AB, read consistently by S3) |
| Severity | moderate |
| Source | S3 |

**GB-34 Three trends described for the parameter sweeps are not shown by Figure 10, its highlighted values differ from the settings used, and "robust across a range of parameters" is not qualified.**

| Field | Content |
|---|---|
| Check | P3, P5, P21 |
| Location | p. 12, l. 372 to 373; p. 13, l. 374; p. 13, l. 380 to 384; p. 13, l. 387 to 388; Fig. 10 (p. 31) |
| Quotation | "However, beyond approximately 10 times the pixel size (3000 m), the solution becomes overly smooth, causing the posterior to deviate from the true erosion rates." and "As data standard deviation increases, the absolute difference first decreases to a minimum, then rises to a plateau at higher values." |
| Concern | Measured at 600 dpi (AB), consistent with the readings of S3 and SD. (1) Smoothing distance (row 1): 20 markers from 199 ± 4 m to 3002 ± 4 m; the total difference falls monotonically from 256.8 to 76.2 ± 0.3 and the uncertainty from about 0.99 to 0.27; the marker at 3000 m is the minimum and no value above 3000 m is plotted, so the stated deterioration is not in the figure; at the value used elsewhere, 1200 m, the error is about 197, and how 1200 m follows from the sweep is not stated. (2) Data standard deviation (row 3): the y axis carries the offset "+1.974e2"; the markers from σ_d = 0.032 to 0.892 mm/y rise monotonically from 197.4198 to 197.4432, a spread of 0.023 or 0.012 %; the normalised uncertainty spans 0.74015 to 0.74040 (0.034 %) and the model misfit 1.5614 to 1.5623 (0.058 %) (Python); there is no minimum, no plateau and no "large" difference at low σ_d, and "decrease rapidly" (p. 13, l. 384) is invisible at the scale of the other rows. (3) Iterations (row 5): values 268.7 (n = 5), 200.8 (n = 15), 197.6 (n = 25) and 200.8 to 201.1 (n of 35 and more), so within the tested grid only n = 5 fails, not every n below 25. (4) The highlighted labels "L = 3000 m", "σm = 6.2", "σd = 0.003 mm/y", "μ = 0.1" and "n_m = 25" (column 3) are not explained in the caption; the last two agree with the settings at p. 11, l. 324 to 326, the first three do not (1200 m, 3, 0.01 mm/y). (5) The colour bars of rows 3 and 4 end below the plotted maxima (σ_d 0.89 mm/y, step size 0.316). (6) The score varies by a factor of 3.37 over L and from about 330 to 197 over µ, which does not support an unqualified "the method is robust across a range of parameters" (p. 16, l. 482 to 483). KK-13 treats the exponent at p. 13, l. 384, KK-18 a spelling in the same figure and GB-47 its font size; this finding concerns the content of the sweeps. |
| Suggestion | Extend the smoothing sweep beyond 3000 m or delete the sentence at p. 12, l. 373 to p. 13, l. 374; state in Section 4.1.4 the values held fixed per sweep and why L = 1200 m was chosen; rewrite p. 13, l. 380 to 384 to the plotted ranges (or plot σ_d on a logarithmic axis that resolves values below 0.03 mm/y); restate the iteration threshold in terms of the tested values; explain or align the highlighted values; extend the colour bars; and replace "robust across a range of parameters" by ranges within which the score stays within a stated tolerance. |
| Status | values: verified (measured); contradictions with the text: inferred |
| Severity | moderate |
| Source | S3, AB, SD |

**GB-35 One of the 21 tracer minerals is called "Chrysolite" in the text and "Chrysotile" in Figures 11, 15 and 16.**

| Field | Content |
|---|---|
| Check | P38 |
| Location | p. 13, l. 395; Fig. 11 (p. 32), row labels; Fig. 15 (p. 36) and Fig. 16 (p. 37), fingerprint panels |
| Quotation | "Fayalite, Dolomite, Diopside, Chrysolite, Antigorite, Anorthite" |
| Concern | The tracer list matches the figures in number: the text list has 21 names, Fig. 11 has 21 row labels, Figs. 15 and 16 have 21 mineral labels each (Python set comparison; page images); the sets are identical except "Chrysolite" (text) against "Chrysotile" (all three figures). The manuscript itself names chrysotile as a serpentine mineral of the serpentinites ("serpentinites (predominantly antigorite and chrysotile)", p. 10, l. 274). Chrysolite is a name for a yellowish green olivine, a different mineral, and the olivine end member fayalite is already in the list. Since the 2θ windows are taken per mineral from RRUFF reference spectra (p. 9, l. 257 to 258), the name decides which reference pattern defines the window; the reader cannot tell which one was used. GB-20 treats duplicated tracer columns, including the antigorite and chrysotile pair. |
| Suggestion | Correct "Chrysolite" to "Chrysotile" at p. 13, l. 395 if chrysotile is meant, and list the RRUFF reference (ID) and the 2θ window of each of the 21 minerals in Section 3.4 or a supplement. |
| Status | verified (text and figure labels on page images; set comparison with Python); identity of chrysolite: verified on the minerals.net variety page (https://minerals.net/variety/chrysolite, not a primary mineralogical reference) |
| Severity | moderate |
| Source | S2, S3, S4, AB, SD |

**GB-36 Research question 1 is answered by one qualitative sentence, and several fingerprint values in Figure 11 sit uneasily with the manuscript's own description of the lithologies.**

| Field | Content |
|---|---|
| Check | P10, P11 |
| Location | p. 13, l. 399 to 401; p. 10, l. 282 to 283; p. 10, l. 274 to 278; Fig. 11 (p. 32) |
| Quotation | "to investigate whether the inferred XRD source fingerprints align with the expected mineralogical compositions of the lithologies" and "The mineralogical fingerprints derived from processed and binned XRD data align well with established knowledge of the lithology in the Gorner Glacier catchment" |
| Concern | No expected composition per unit is listed and no agreement measure is used; the sentence also serves as evidence for "the robustness of the cleaning and binning approach" (p. 13, l. 400 to 401). Measured bar widths in Fig. 11 (full scale 122 px, normalised to the sample maximum): almandine 4 px (0.03) in Monte Rosa gneiss and micaschist and 11 px (0.09) in Stockhorn, Tuftgrat, Gornergrat, both described as garnet-mica schists (p. 10, l. 276 to 277); omphacite 7 px (0.06) in the ZSF metabasites and eclogites (eclogites named at p. 10, l. 274); tremolite 109 px (0.89) in the Monte Rosa granite (p. 10, l. 276); antigorite and chrysotile 70 and 71 px (0.57, 0.58) in Stockhorn, Tuftgrat, Gornergrat and 63 and 60 px (0.52, 0.49) in the ZSF sediments, while the manuscript names these minerals for the serpentinites (p. 10, l. 274). Whether these values are mineralogically wrong is not decided here; the claim "align well" is untested. If the fingerprints do not reflect the lithologies, the attribution to units changes, hence major. KK-14 corrects a duplicated article at p. 13, l. 400; GB-20 explains part of the pattern by shared windows, and GB-35 treats the name of one mineral in Fig. 11. Which minerals were expected per unit? |
| Suggestion | In Section 4.2 tabulate expected major minerals per unit (from Bearth, 1953 and Steck et al., 2015, already cited, or own thin sections) and compare with Fig. 11 by a stated criterion (presence and absence agreement, rank correlation), or quantify the same source powders independently (for instance by Rietveld refinement); discuss the cases above. |
| Status | absence of a measure: verified; bar widths: verified (measured on page image p. 32); mineralogical expectation: assumption, asked as a question |
| Severity | major |
| Source | SD, S3 |

**GB-37 The natural known-mixture test checks the exclusion of one small unit, while a second unit without area in the subcatchment, the ZSF metabasites, receives erosion rates comparable to units inside it; sample number, parameters and spillover are not reported.**

| Field | Content |
|---|---|
| Check | P3, P10, P11 |
| Location | p. 14, l. 410 to 416; Fig. 12 (p. 33), map and caption; Fig. 13 (p. 34), inset map and KDE panels |
| Quotation | "If the XRD fingerprinting method is robust, the inversion should attribute erosion only to lithologies present within the sub-catchment. Only the Zermatt - Saas Fee sediment unit does not have outcrops in the Gorner-Grenz subcatchment" and "the overall pattern confirms that the inversion respects geological boundaries" |
| Concern | Letting A cover the whole domain while the samples drain a subcatchment is an informative natural analogue of a known-mixture test, and Fig. 13 draws the subcatchment boundary. (1) Measured on the inset of Fig. 13 (600 dpi, polygon traced along the dashed boundary, 269,512 coloured pixels assigned to the nearest unit colour): MR granite 68.27 %, S.,T.,G. 17.00 %, Furgg series 9.26 %, ZSF serpentinites 3.18 %, MR gneiss 2.06 %, ZSF sediments 0.23 % (misassigned boundary pixels), ZSF metabasites 0 px; a strict green test gives 0 px inside the boundary and 100 % on a reference patch of the metabasite unit outside it. In the unit map of Fig. 13, which is also the map of the KDEs ("for all pixels within each lithological unit"), the ZSF metabasites thus lie entirely outside the subcatchment, like the ZSF sediments. Fig. 12 shows one small outline in the north-east whose colour matches the metabasite swatch, so metabasite outcrops may exist there, but not as unit area. (2) KDEs (x axis calibrated, ± 0.007 mm/y): ZSF metabasites peak at 0.28 mm/y, area median 0.50 mm/y, 75 % of the plotted area above 0.25 mm/y; ZSF sediments median 0.09 mm/y, 11 % above 0.25 mm/y; MR gneiss, with 2.06 % of the subcatchment area, has the narrowest KDE, peak 0.60 mm/y, no mass near zero. Under the criterion of p. 14, l. 410 to 411 the metabasite KDE is a failure of the kind the ZSF sediment KDE was meant to detect, so the conclusion of p. 14, l. 415 to 416 does not follow from Fig. 13 as drawn. (3) The criterion is applied to 1 of 7 units, which is also one of the small units with "lower resolution" (p. 10, l. 299 to 300); resolution, uncertainty and prior of these runs are not shown. (4) "multiple detrital samples" (p. 14, l. 413) and "multiple inversions" (Fig. 13 caption) are the only statements on sample number; dates and parameters are not given; "close to zero" and "Some spillover" (p. 14, l. 414) are not quantified. (5) The test works at unit level, so erosion assigned to outside pixels of units that also crop out inside cannot be detected. (6) Fig. 12 is announced as showing the subcatchment, but its boundary is not drawn there. Is the metabasite unit counted as present because of outcrop polygons, and were the KDEs computed on unit polygons or outcrops? KK-15 treats the spelling of "sub-catchment" in these lines. |
| Suggestion | Draw the subcatchment boundary in Fig. 12 and give the area share of each unit inside it; evaluate the test for every unit without area in the subcatchment (at least ZSF sediments and ZSF metabasites) and comment on units with very small shares; report the number and dates of the samples, the inversion parameters, the fraction of posterior flux assigned to pixels outside the subcatchment and per-unit mean rates; add a control run with A masked to the subcatchment and, ideally, laboratory known mixtures of the source powders (as described at p. 13, l. 404 to 406); revise p. 14, l. 411 to 416 and the caption of Fig. 12 accordingly. |
| Status | unit shares and KDE values: verified (measured by AB); missing numbers: verified (search); that the test is not passed for ZSF metabasites: inferred; regularisation as alternative explanation: inferred; how unit membership was defined: assumption, asked as a question |
| Severity | major |
| Source | AB, SD, S3 |

**GB-38 The zircon and XRD comparison is said to use "the same detrital sample" in one place and "a detrital sample taken at the same date and time" in another, and the sample has no ID or site.**

| Field | Content |
|---|---|
| Check | P38, P2 |
| Location | p. 14, l. 420 to 421; p. 14, l. 437 to 438 |
| Quotation | "we compare it against a zircon-based fingerprinting approach applied to the same detrital sample" and "We then applied the same nonlinear inversion technique to the XRD-derived dataset acquired from a detrital sample taken at the same date and time" |
| Concern | Pairing zircon and XRD data from one sampling time is a good basis for the comparison. The first wording means one sample split for both analyses, the second two samples collected at the same time. The sample has no ID, and its site is not given (whether it was taken at the Gorner-Grenz confluence of Section 4.2.1 or elsewhere). With two samples, part of the difference between Figs. 14 and 15 may come from sample-to-sample variability. Were zircon and XRD measured on splits of one sample or on two samples? GB-39 treats the zircon protocol and GB-41 the design of the comparison; this finding concerns the identity of the sample. |
| Suggestion | In Section 4.2.2 (p. 14, l. 420 to 424 and 437 to 438) give the sample an ID and its site, state whether zircon and XRD data come from splits of one sample, and use the ID in the captions of Figs. 14 to 16. |
| Status | wording: verified (page image p. 14); interpretation as two samples: assumption, asked as a question |
| Severity | moderate |
| Source | S2, S3 |

**GB-39 The zircon extraction and dating protocol rests on a thesis cited as unpublished, and the availability statement does not mention the zircon data.**

| Field | Content |
|---|---|
| Check | P12, P35 |
| Location | p. 14, l. 423 to 425; p. 17, l. 522 to 523; p. 16, l. 490 |
| Quotation | "Zircon grains were extracted and U-Pb dated from both the source lithologies and the detrital sample collected on June 28, 2019, at 13:30, following the methodology described in (Belotti, 2021)." |
| Concern | The zircon comparison is the only test with an independent tracer, and its data source is clearly attributed. The manuscript itself gives no protocol: no separation method, dating technique or laboratory, number of grains per sample, discordance filter, or rationale for the 13 age bins of Fig. 14 (search of p. 1 to 21 for "LA-ICP", "ICP-MS", "U-Pb", "SHRIMP", "grains": 3 hits, p. 14, l. 423 and 430, p. 16, l. 489, none naming a technique or count). The reference marks the thesis as unpublished and gives no locator; a catalogue record exists in the UNIL repository of master's theses (https://igd.unil.ch/memoires/memoires/1856, title, author, June 2021, link to a PDF that was not opened). The availability statement does not mention the zircon data; the README lists "Zircon_Data_to_Generate_fingerprints/ # Raw zircon data", so they are probably released, but the manuscript does not say so. KK-16 treats the citation form at p. 14, l. 424 to 425 and KK-24 the wording of the thesis entry; this finding concerns protocol and availability. |
| Suggestion | Summarise the zircon protocol in Section 4.2.2 (after p. 14, l. 425) or an appendix (separation, dating method and laboratory, standards, grains per sample, filters, age bins), add the repository locator to the reference (p. 17, l. 522 to 523), and name the zircon data in "Code and data availability" (p. 16, l. 490). |
| Status | verified (page images p. 14, 16, 17; search; UNIL catalogue page read); repository content: inferred from the README; accessibility of the thesis PDF: not checked |
| Severity | moderate |
| Source | S2, SD |

**GB-40 For the natural runs the prior is described as the "average true erosion rate", which does not exist for field data, and the annual export estimate that scales the data is never given.**

| Field | Content |
|---|---|
| Check | P25, P12, P2 |
| Location | p. 14, l. 426 to 428; p. 15, l. 444 to 445; p. 5, l. 159 to 160; p. 15, l. 452 to 454; p. 16, l. 479 to 480 |
| Quotation | "a prior equal to the average true erosion rate, and a step size µ of 0.1" and "4) an estimate of the total annual suspended sediment export from the catchment" and "For simplicity, we redefine the data vector d as scaled by the total erosion rate" |
| Concern | The parameter list of the natural zircon run repeats the synthetic list word for word, including the prior (p. 14, l. 426 to 428), and the XRD and combined runs use the same settings (p. 14, l. 437 to 438; p. 15, l. 444 to 445). For the Gornergletscher no true map exists; which prior was used? The Gorner-Grenz runs have no parameters at all. The export estimate is named as one of four key inputs (p. 3, l. 65 to 66; p. 15, l. 452 to 454; "a yearly sediment export estimate", p. 16, l. 479 to 480) and enters through eq. 2, which scales d by the total erosion rate. Search of p. 1 to 16 for "export", "annual", "yearly": 6 lines (p. 3, l. 66; p. 5, l. 133; p. 15, l. 453, 454 and 468; p. 16, l. 479), all naming it as an input, none giving value, source, period, conversion from mass to erosion rate or uncertainty; the "multi-year suspended sediment datasets" (p. 9, l. 267 to 268) have no operator, years or access, and the availability statement does not mention them. The absolute rates in mm/y of Figs. 13 to 16 can therefore not be reproduced; the spatial pattern and the method comparison are not affected, hence moderate. Is the export estimate also used in the synthetic tests, or is the scaling taken there from the true map? |
| Suggestion | In Section 4.2 state the prior value used for each natural run and its derivation, and the export estimate with source, period, density, area and uncertainty and how it enters eq. 2; correct the wording at p. 14, l. 428; add the suspended sediment data, or their public source, to "Code and data availability" (p. 16, l. 490). |
| Status | wording and absence: verified (page images p. 5, 9, 14, 15, 16; searches); what was actually used: assumption, asked as a question |
| Severity | moderate |
| Source | S2, S3, SD |

**GB-41 The zircon comparison confounds the tracer type with an incomplete zircon fingerprint matrix, does not state how the unit without zircon enters the matrix, and rests on one sample.**

| Field | Content |
|---|---|
| Check | P9, P11, P20 |
| Location | p. 14, l. 430 to 434; p. 14, l. 435; p. 15, l. 447 to 448; Fig. 14 (p. 35), source fingerprint panel |
| Quotation | "zircon data were not available for two lithological units: no zircon grains were recovered from the Zermatt-Saas Fee (ZSF) ophiolites (metabasites and eclogites), and no age data were available for the Monte Rosa garnet-gneiss (MR g-g) unit" and "we assigned the MR g-g unit the same zircon-age fingerprint as the Monte Rosa granite unit" |
| Concern | The zircon run differs from the XRD run not only in tracer type but in completeness. Measured in Fig. 14 at three columns per bar: no serpentinite (yellow) and no metabasite (green) segment in any of the 13 age bins; MR gneiss and MR granite segments are equal within 1 px in all 11 bins where they occur (for instance 140 to 200 Ma: 113 and 113 px). Measured zircon fingerprints thus exist for 4 of 7 units (57.1 %), one is a copy and two are empty (Python). Two units are identical by construction, which the manuscript's own scenario 2 names as the main cause of failure (p. 12, l. 351 to 354); the instability of the zircon solution (">8000 mm/y", p. 14, l. 435) can therefore not be attributed to the zircon method. Whether the metabasite column of the zircon matrix is zero, removed or filled otherwise is not stated; with an empty column the pixels of that unit act only through the normalisation of eq. 1. The average JS distance is defined over "all pairs of source XRD signatures" (p. 12, l. 347): 7 units give 21 pairs, 6 give 15 (Python); the identical Monte Rosa fingerprints contribute a JS distance of 0, and whether 0.48 (zircon) and 0.57 (combined) are averaged over the same pairs is not stated. The comparison uses one sample, although "multi-year suspended sediment datasets" exist (p. 9, l. 268), and the choice is not explained. GB-49 treats the labelling of the copied fingerprint in the figures and GB-42 the claims drawn from the comparison. |
| Suggestion | In Section 4.2.2 (after p. 14, l. 434) state how the units without zircon enter the zircon and combined matrices and the pairs behind the JS values; compare on a common source set (merge the two Monte Rosa units and merge or drop units without zircon in both data sets) or run a synthetic test with the zircon matrix as given; repeat the comparison on all paired samples available and report the spread. |
| Status | text: verified; segment lengths: verified (measured on page image p. 35); mechanism through eq. 1 and effect on 0.87: inferred and assumption, asked as a question |
| Severity | major |
| Source | SD, S3 |

**GB-42 The claim that combining zircon with XRD "further" stabilises and improves the solution is contradicted by the reported uncertainties, the three runs are compared on different metrics, and stability, sharpness and accuracy are not measured.**

| Field | Content |
|---|---|
| Check | P2, P11, P15, P31 |
| Location | p. 15, l. 446 to 449; p. 15, l. 461 to 463; p. 3, l. 72 to 73; p. 5, l. 139 to 140; p. 10, l. 284 to 285 |
| Quotation | "Adding XRD data to the zircon dataset stabilizes the inversion and improves the posterior solution. The normalized posterior uncertainty decreases slightly to 0.86 (from 0.87 in the zircon-only case)" and "combining XRD data with other fingerprint data such as zircon data, proves to further stabilize and improve the posterior solution" |
| Concern | The three natural runs report one common metric each, consistently in text and figure labels (PP-23): zircon 0.87 (p. 14, l. 436), XRD 0.82 (p. 15, l. 442), combined 0.86 (p. 15, l. 447). Section 4.2.2 correctly reports the change relative to zircon: 0.87 − 0.86 = 0.01 (1.1 %). Relative to XRD alone, however, the combination raises the uncertainty: 0.86 − 0.82 = 0.04 (4.9 %, Python), four times the gain over zircon. The colour bars of the posterior maps point the same way: maximum 8 mm/y for XRD (Fig. 15) and 12 mm/y for the combination (Fig. 16). The Discussion takes XRD as the base ("combining XRD data with other fingerprint data such as zircon data") and claims a further improvement, and the Introduction states that integrating XRD with zircon "improves the stability and sharpness of the posterior solution" (p. 3, l. 72 to 73; p. 5, l. 139 to 140); by the manuscript's own metric neither has support. The other metrics are reported per case only in part: average JS distance for zircon (0.48) and combined (0.57) but not for XRD alone, although the synthetic tests place the onset of degraded solutions below 0.55 (p. 12, l. 352); maximum erosion rate and resolution only for zircon, in words; no measure of stability or sharpness (search "sharp" in p. 1 to 16: 5 hits, none defines a measure); and "accuracy", announced in research question 3 (p. 10, l. 285), cannot be assessed on natural data without a reference. The differences of 0.01 to 0.05 come from one sample without uncertainty, and "proves" is stronger than one sample allows. Severity major because the answer to research question 3, as written in Introduction and Discussion, changes if the reference case is XRD alone; the claim that XRD fingerprints work is not affected. Wording in the same sentence: comma between subject and verb ("zircon data, proves"). GB-18 treats the definition of the uncertainty metric. |
| Suggestion | In Section 4.2.2 add the XRD-only case to the comparison (p. 15, l. 446 to 449), give normalised uncertainty, JS distance, maximum and mean posterior rate and mean resolution for all three runs in one table, and state that the combined uncertainty (0.86) is higher than the XRD-only value (0.82); rephrase p. 3, l. 72 to 73, p. 5, l. 139 to 140 and p. 15, l. 461 to 463 so that any improvement is stated relative to zircon and "for one detrital sample", replace "proves" by "suggests" and delete the comma; replace "accuracy" at p. 10, l. 285 by a property that can be assessed with natural data. |
| Status | values in text and figure labels: verified; differences and percentages: inferred (calculated); colour bar maxima: verified (page images p. 36, 37) |
| Severity | major |
| Source | S3, S4, SD |

**GB-43 Several panels lack units, axis titles or value scales.**

| Field | Content |
|---|---|
| Check | P29 |
| Location | Fig. 5a to 5c and Fig. 6a to 6c, colour bars (p. 26 to 27); Fig. 6g to 6i, x axes, multiplier and colour bar (p. 27); Figs. 7 to 9, y axes of the absolute error (p. 28 to 30); Fig. 11, value axis and column headings (p. 32); Fig. 13, upper panel density axis (p. 34) |
| Quotation | "(a) True erosion map" and "(g) ∑|etrue - epost|" and caption "a taller peak indicates greater consistency across inversions" |
| Concern | (1) The erosion and difference maps of Figs. 5 and 6 have colour bars without quantity or unit, while Figs. 14 to 16 give "(mm/y)". (2) Fig. 6g and 6h have no x-axis title ("Iteration" in Fig. 5); Fig. 6i has no x-axis title, no multiplier (Fig. 5i: "Data misfit" and "1e8") and an unlabelled colour bar. (3) The absolute error axes of Figs. 7 to 9 give no unit (GB-32). (4) Fig. 11 has no value axis and no column headings; the lithologies are identified only by their order in the caption. (5) The upper panel of Fig. 13 has a density axis without ticks, while the lower panel has a scale from 0 to 2; the caption interprets peak heights, which cannot be compared between the panels. |
| Suggestion | Add quantities and units to all colour bars and axes, the missing axis titles and multiplier in Fig. 6, column headings and a value axis in Fig. 11, and a common density scale in Fig. 13. |
| Status | verified (page images) |
| Severity | minor |
| Source | AB |

**GB-44 The hatched "low-confidence areas" are not defined anywhere, and the legend label is missing in Figure 6.**

| Field | Content |
|---|---|
| Check | P29 |
| Location | Fig. 5b, legend below the panel (p. 26); Fig. 6, legend below panel b (p. 27); Figs. 14 to 16, legend below the erosion map (p. 35 to 37) |
| Quotation | "Low-confidence areas" |
| Concern | Search of the text pages (p. 1 to 16, `text.json`, case-insensitive) for "confiden", "hatch" and "low con": 0 hits; the captions of Figs. 5, 6 and 14 to 16 do not define the criterion either. In Fig. 6 the hatch swatch appears without any label (page image). A reader cannot tell which threshold or metric produces the hatching. KK-21 treats the lost ligature in the legend of Figs. 14 to 16 and GB-50 the position of the XRD peak relative to the hatching. |
| Suggestion | Define the criterion in Section 3.3 and in the captions; add the label in Fig. 6. |
| Status | verified |
| Severity | minor |
| Source | AB, SD |

**GB-45 Bar colours in Figures 5k, 15 and 16 match the wrong legend swatches, and Figure 14 has no legend.**

| Field | Content |
|---|---|
| Check | P3 |
| Location | Fig. 5j legend and Fig. 5k (p. 26); Fig. 15, legend and bar panel (p. 36); Fig. 16, legend and bar panel (p. 37); Fig. 14 (p. 35) |
| Quotation | "S.,T.,G." and "MR gneiss, mica" and "MR granite" |
| Concern | Legend swatches measured in Fig. 15: S.,T.,G. #fc5404, MR gneiss #fc7c44, MR granite #fc9c9c (identical in Figs. 5j and 16). The bars use lighter colours, consistent with about 70 % opacity (ZSF metabasites #34a42c becomes #74bc6c). The bar colour #fc844c (S.,T.,G.) differs from the MR gneiss swatch by 16 and from its own swatch by 120; the bar colour #fca47c (MR gneiss) differs from the MR granite swatch by 40 and from its own by 96 (sums of RGB differences). A reader using the legend thus assigns the S.,T.,G. bars to MR gneiss and the MR gneiss bars to MR granite; the same bar colours occur in Figs. 5k and 16. Fig. 14 shows a geological map and stacked bars in the same colours without any legend. The fingerprints are an input of the inversion and cannot be attributed correctly from the figure, hence moderate rather than minor. |
| Suggestion | Draw the bars opaque or use legend swatches with the same opacity; add a legend to Fig. 14. |
| Status | verified (measured) |
| Severity | moderate |
| Source | AB |

**GB-46 The x axes of the scatterplots in Figure 9 are labelled as Jensen-Shannon distance but show the number of tracers, and the colour bar title is misspelt.**

| Field | Content |
|---|---|
| Check | P3 |
| Location | Fig. 9 (p. 30), left and middle scatterplots, x axes; colour bar of the third panel |
| Quotation | "Avg. JS distance between lithologies" and "Number of tracrs" |
| Concern | 21 markers counted at 600 dpi at x = 1 to 21 (equal spacing; label "1 tracer" at the first, "All" at the last), matching "the full range between 1 and 21 tracers" (p. 12, l. 358). The axis title is that of Fig. 8. |
| Suggestion | Replace the x-axis titles by "Number of tracer minerals" and the colour bar title by "Number of tracers". |
| Status | verified (page image p. 30) |
| Severity | minor |
| Source | AB, S3, SD |

**GB-47 Text in Figure 10 is 2 to 4 pt in print size, and tick labels in Figures 4 and 14 to 16 are about 5 pt.**

| Field | Content |
|---|---|
| Check | P29 |
| Location | Fig. 10 (p. 31), all panels; Figs. 14 to 16, tick labels (p. 35 to 37); Fig. 4, inset coordinate labels (p. 25) |
| Quotation | "+1.974e2" and "0.74040" |
| Concern | Cap or digit height measured in the 300 dpi page image (pt = px × 72 / 300 / 0.72): Fig. 10 tick labels "250" and "3000" 2.3 pt, "0.74040", "+1.974e2" and "1e6" 3.3 pt, axis titles 4.0 pt; Figs. 14 to 16 "40-140", "Talc", "8000" 5.0 to 5.3 pt; Fig. 4 inset "46°N" 5.3 pt. Fig. 10 is far below 6 pt, the others 0.7 to 1.0 pt below, more than the tolerance of 0.6 pt. GB-34 treats the content of Fig. 10 and KK-18 a spelling in it; this finding concerns legibility. |
| Suggestion | Enlarge Fig. 10 (for example split it over two pages or reduce the panels) and raise the tick labels of Figs. 4 and 14 to 16 to at least 6 pt. |
| Status | verified (measured) |
| Severity | minor |
| Source | AB |

**GB-48 The source fingerprints in the bar panel of Figure 15 are not the per-mineral normalisation of the fingerprints in Figure 11.**

| Field | Content |
|---|---|
| Check | P3 |
| Location | Fig. 11 (p. 32); Fig. 15 (p. 36), bar panel; Fig. 16 (p. 37), XRD part of the bar panel; p. 13, l. 397 to 398 |
| Quotation | "we obtained the mineral concentrations characterizing each lithological unit (Figure 11)" and y axis of Fig. 15 "Normalised abundance per mineral or age" |
| Concern | If the stacked bars of Fig. 15 normalise the values of Fig. 11 per mineral, each lithology's share equals its bar length in Fig. 11 divided by the row sum. Measured by colour profiles (Fig. 11 rows, full width 243 px; Fig. 15 bars, height 451 to 455 px): all 21 minerals differ; the largest share difference per mineral ranges from 0.081 to 0.217, median 0.144. Examples: quartz is at full width for ZSF sediments, MR granite, MR gneiss and Furgg in Fig. 11, giving 0.209 each, but 0.177, 0.227, 0.325 and 0.214 in Fig. 15; fayalite, ZSF serpentinites 0.543 against 0.734; antigorite 0.430 against 0.641. The deviation is systematic. By contrast the zircon bars of Fig. 14 follow plain normalisation (PP-26). Is a lithology-specific weighting (for example by area) applied in Fig. 15, or do Figs. 11 and 15 come from different samples? GB-20 uses Fig. 11 for duplicated columns, GB-35 for the name of one mineral, GB-36 for research question 1, GB-19 cites p. 13, l. 396 to 398 for the processing chain, and KK-08 and KK-19 correct its caption; this finding concerns the relation between the two figures. |
| Suggestion | State in the captions of Figs. 15 and 16 how the bars are normalised or weighted; derive Figs. 11 and 15 from the same matrix A or explain the difference; provide A as a table in the repository or a supplement. |
| Status | shares: verified (measured); cause: assumption, asked as a question |
| Severity | moderate |
| Source | AB |

**GB-49 Figures 14 and 16 show the assigned Monte Rosa gneiss zircon fingerprint as if it were measured.**

| Field | Content |
|---|---|
| Check | P37 |
| Location | Fig. 14 (p. 35), source fingerprint panel and caption; Fig. 16 (p. 37), age-bin part of the fingerprint panel; p. 14, l. 430 |
| Quotation | "As shown in the source signatures in Figure 14, zircon data were not available for two lithological units" |
| Concern | Measured on the page images, the MR gneiss segments equal the MR granite segments within 1 px in all 11 age bins where they occur, in Fig. 14 and in Fig. 16 (for instance Fig. 16, 140 to 200 Ma: 109 and 109 px). Neither caption nor legend marks these values as assigned; the figures show missing data only for the metabasites, while the text says the figure shows missing data for two units. GB-41 uses the same measurement for the design of the comparison, and KK-21 corrects a legend label of the same figures; this finding concerns the labelling. |
| Suggestion | Mark the assigned fingerprint in Figs. 14 and 16 (hatching or a note in the caption) and adjust p. 14, l. 430. |
| Status | verified (measured on page images p. 35 and 37) |
| Severity | moderate |
| Source | SD |

**GB-50 The main erosion peak attributed to the XRD solution borders on and partly lies under the hatched low-confidence area of Figure 15.**

| Field | Content |
|---|---|
| Check | P3 |
| Location | Fig. 15 (p. 36), posterior erosion map; Fig. 16 (p. 37), posterior erosion map; p. 14, l. 440 to p. 15, l. 441; p. 15, l. 448 to 449 |
| Quotation | "the XRD solution identifies the main erosion peak in the center of the domain and a secondary peak in the Monte Rosa granite area" and "The resulting erosion pattern more closely resembles the XRD-only solution" |
| Concern | In Fig. 15 all pixels at the top of the colour scale form 7 patches within a box of 36 × 49 px of the 300 dpi page image, inside the bounding box of the hatched patch; the hatching covers the centre of the peak. In Fig. 16 the top-of-scale cells surround a hatched patch in the same way. The text uses this peak as the main result of the XRD and combined inversions without mentioning the flag. Since the criterion of the hatching is not given (GB-44), it is open whether the peak is robust. KK-22 corrects the legend of the same figures, and GB-42 cites p. 15, l. 446 to 449 for the comparison of the three runs; this finding concerns the peak. |
| Suggestion | Explain whether the peak lies in a low-confidence area and what that means; give peak values with their posterior uncertainty; qualify p. 14, l. 440 to p. 15, l. 441 and p. 15, l. 448 to 449 if the peak is not robust. |
| Status | coincidence of peak and hatching: verified (measured); meaning of the hatching: assumption, asked as a question |
| Severity | moderate |
| Source | AB |

#### Minor corrections

| ID | Location | Quotation | Replacement | Source |
|---|---|---|---|---|
| KK-12 | p. 11, l. 333 to 334 | "the map proposed by (Steck et al., 2015)" | "the map proposed by Steck et al. (2015)". GB-22 cites these lines for the identity of the maps and GB-27 p. 11, l. 334 to 336 for the name of the mismatch measure; this correction concerns the citation form. | S4 |
| KK-13 | p. 13, l. 384 | "approximately 10-2 mm/y" | "approximately 10⁻² mm/y", exponent as superscript, as "10⁻⁵" at p. 13, l. 388 (page image). GB-34 cites this line for the σ_d sweep; this correction concerns typesetting. | S3, S4, SD |
| KK-14 | p. 13, l. 400 | "supporting the 1) the robustness" | "supporting 1) the robustness". KK-08 and GB-36 cite this line for the glacier name and research question 1. | S3, S4 |
| KK-15 | p. 14, l. 409; p. 14, l. 411; p. 14, l. 413; p. 16, l. 488 | "sub-catchment" | "subcatchment", as at p. 10, l. 283 and 284, p. 14, l. 411 and in the captions of Figs. 12 and 13 (hyphens confirmed on the page images). GB-37 cites these lines for the known-mixture test and GB-55 p. 16, l. 487 to 489 for the outlook; this correction concerns spelling. | S2 |
| KK-16 | p. 14, l. 424 to 425 | "described in (Belotti, 2021)" and "outlined in (De Doncker et al., 2020)" | "described in Belotti (2021)" and "outlined in De Doncker et al. (2020)" (two narrative citations in consecutive sentences). GB-39 cites these lines for the zircon protocol. | S4 |
| KK-17 | Fig. 7 (p. 28), title of the left map | "Originial geology (same as forward)" | "Original geology (same as forward)". GB-22 quotes this title for the identity of the maps and GB-33 uses Figure 7 for the ranking of scenarios; this correction concerns spelling. | S3, AB |
| KK-18 | Fig. 10 (p. 31), row 1, x axis of column 2 and colour bar of column 3 | "Smooting distance (m)" | "Smoothing distance (m)", as in column 1. GB-34 and GB-47 treat content and legibility of Fig. 10. | S3, AB |
| KK-19 | Fig. 11 (p. 32), caption | "Stockhorn-Turftgrat-Gornergrat" and "ZSF ophiolites (metabasites, ecologites)" | "Stockhorn-Tuftgrat-Gornergrat" (as p. 10, l. 276 and Fig. 13) and "ZSF ophiolites (metabasites, eclogites)" (as p. 10, l. 274; p. 12, l. 341; p. 14, l. 431; Fig. 13). GB-20, GB-23, GB-35, GB-36, GB-48 and KK-08 cite this figure for other matters. | S2, S3, S4, AB |
| KK-20 | Fig. 13 (p. 34), KDE labels | "Monte R osa" and "ZS F ophiolites" and "S tockhorn, Tuftgrat, Gornergrat" | "Monte Rosa", "ZSF ophiolites", "Stockhorn, Tuftgrat, Gornergrat" (letter spacing visible on the page image) | AB |
| KK-21 | Fig. 14 (p. 35), Fig. 15 (p. 36) and Fig. 16 (p. 37), legend below the erosion map | "Low-con dence area" | "Low-confidence area" (the "fi" ligature is missing on the page images; Fig. 5 reads "Low-confidence areas"). GB-41, GB-44, GB-49 and GB-50 cite these figures for the zircon matrix, the hatching criterion, the assigned fingerprint and the XRD peak. | S3, AB |
| KK-22 | Fig. 15 (p. 36) and Fig. 16 (p. 37), legend | "ZSF serpentinite" | "ZSF serpentinites" with full text, swatches moved apart (in Fig. 15 the last letter is covered by the next swatch); place the legend of Fig. 16 so that its top row is complete. GB-45 and GB-50 cite these figures for bar colours and the XRD peak. | AB |

#### Verification log

| ID | Check | Checked | Values | Result |
|---|---|---|---|---|
| PP-22 | P1, P2 | Pixel size and hyperparameters wherever stated | L = 1200 m = 4 pixels (p. 10, l. 294; p. 11, l. 325; p. 14, l. 427) and 3000 m = 10 pixels (p. 12, l. 373); 1200/4 = 300 m, 3000/10 = 300 m (Python); σ_m = 3, σ_d = 0.01 mm/y, µ = 0.1 and 25 iterations identical at p. 10, l. 294 to 295, p. 11, l. 324 to 326 and p. 14, l. 426 to 428; 100 iterations in the first QN test (p. 10, l. 293; Fig. 5g axis) | no finding among text values; figure labels in GB-34 |
| PP-23 | P1, P2 | Total normalised posterior uncertainty, text against figure labels | 0.87 (p. 14, l. 436; Fig. 14), 0.82 (p. 15, l. 442; Fig. 15), 0.86 (p. 15, l. 447; Fig. 16); JS 0.48 to 0.57 | no finding on values and arithmetic; direction of the comparison in GB-42, definition in GB-18 |
| PP-24 | P2, P38 | Number of tracer minerals in text and figures | Text list p. 13, l. 394 to 396: 21 names, 21 unique (Python); "21" at p. 12, l. 358 and p. 13, l. 393 and 397; Fig. 5k letters A to U = 21; Fig. 11 21 rows; Fig. 15 21 bars; Fig. 16 21 + 13 age bins = 34 bars; Fig. 9 21 points per panel; "top 11 tracers": 11 bars in Fig. 9 | no finding on the count; name mismatch in GB-35 |
| PP-25 | P2 | Number of source units | 7 units in Fig. 5j legend, Fig. 11 caption, Fig. 12 legend, Fig. 13 (7 KDEs), Figs. 15 and 16 legends | no finding on the count; names in GB-23 |
| PP-26 | P1, P3 | Zircon age bins and assigned fingerprint in Figs. 14 and 16 | Fig. 14: 13 bins from 40-140 Ma to 750-800 Ma; Fig. 16: same 13 bins in the same order; MR gneiss and MR granite segments equal within 1 px in all bins, as p. 14, l. 433 to 434 imply; no yellow and no green segments; top of the zircon colour bar 8598 ± 87 mm/y, consistent with ">8000 mm/y" | no finding; labelling of the copy in GB-49 |
| PP-27 | P23, P3 | Scenario 3 against p. 12, l. 357 to 362 | 21 tracer counts tested, 21 markers per panel; absolute error 347.0 (1 tracer), 348.4 (2), 293.3 (3), 296.3 (4), 223.9 (5), 205.0 (6), 197.2 for 7 to 21 (measured, ± 0.5) | no finding: plateau from 7 tracers and rise below 7, as stated |
| PP-28 | P21, P3 | Scenario 1 against p. 11, l. 336 to p. 12, l. 342 | Absolute error 197.6 (forward geology), 193.8 (minimal changes), 274.8 (Steck et al.); posterior uncertainty 0.7401, 0.7376, 0.7460; data misfit 3.254, 3.491, 3.687 × 10^6; model misfit 1.574, 1.929, 2.463 (measured); the lower error of the modified map is disclosed and explained (p. 11, l. 338 to p. 12, l. 341) | no finding |
| PP-29 | P23 | Balance of source units in the known-mixture test | 7 units; 1 without outcrops in the subcatchment by the text (p. 14, l. 411; Fig. 12 caption); 6 expected to contribute | no finding on the balance as stated; measured area shares in GB-37 |
| PP-30 | P22 | Distance unit of the average JS distance in the synthetic tests | Average over "all pairs of source XRD signatures" (p. 12, l. 347); 7 units give 21 pairs (Python) | no finding for the synthetic case; natural case in GB-41 |
| PP-31 | P1, P3 | Iteration counts and plateau of the SD and QN runs | Text: "after 125 iterations" (p. 11, l. 316); Fig. 6g to 6i axes 0 to 200 (not stated in the text); plateau onset in Fig. 6h at iteration 136.6 ± 3, kink in Fig. 6g at 134 ± 3; Figs. 5g to 5i to 100, as p. 10, l. 293; Fig. 5e light (low) colours at the hotspot, as p. 10, l. 301 | no finding beyond GB-25, GB-28 and GB-29 |
| PP-32 | P3 | Fig. 8, middle panel, against "As the JS distance decreases below 0.55, both absolute error and posterior uncertainty rise sharply" (p. 12, l. 351 to 352) | Posterior uncertainty: JS 0.561 to 0.624: 0.7397 to 0.7467; JS 0.541: 0.8416; JS 0.441 to 0.521: 0.8318 to 0.8388; JS below 0.36: 0.8797 to 0.8926 (measured) | no finding for the threshold 0.55 |
| PP-33 | P3 | Fig. 10, row 4, against p. 13, l. 385 to 386 | Minimum 197.5 at step size 0.0991; 328.3 at the smallest and 201.3 at the largest step (measured) | no finding: minimum at 0.1 as stated |
| PP-34 | P3 | Fig. 13 axis range | x axis ends at 3.27 mm/y; KDEs of Furgg series, ZSF serpentinites, ZSF metabasites and S.,T.,G. are above their baselines at the right edge | no finding as such; medians in GB-37 refer to the plotted range |
| PP-35 | P36 | Statements from impression against the manuscript's own records | "In many of these cases" (p. 12, l. 353) against Fig. 8 (GB-31); "approximately 10-2 mm/y" (p. 13, l. 384) against Fig. 10 marked 0.003 mm/y (GB-34); "approximately the same posterior solution" with 7 tracers (p. 12, l. 360) against Fig. 9: about 197 for 7 to 21 tracers | consistent for tracers; others in GB-31 and GB-34 |
| PP-36 | P34 | Shown selections from counted sets | Fig. 8 top row: 3 of 20 with rule stated; Fig. 9 top row: 3 of 21 with rule stated; Fig. 13: "multiple" samples without number (GB-37); zircon comparison: 1 sample from multi-year data without selection rule (GB-41) | no further finding |
| PP-37 | P5 | Own rules against own examples | Stopping rule (p. 9, l. 243 to 244) against runs with fixed counts 25 and 100; threshold 10⁻⁵ after 115 iterations (p. 13, l. 388) against natural runs with 25 iterations; recommended conditions against the own case (PP-43); marked against used hyperparameters (GB-34) | finding GB-34; otherwise no finding |
| PP-38 | P38 | Name of the confluence site | "Gorner-Grenzgletscher confluence" (p. 13, l. 406 to p. 14, l. 407; Fig. 12), "Gorner-Grenz subcatchment" (p. 14, l. 411), "Gorner-Grenz confluence subcatchment" (captions of Figs. 12 and 13), "Gorner-Grenz catchment" (Fig. 13 inset): same site, consistent core name | no finding (spelling of "subcatchment" in KK-15) |

### Segment 4: Discussion, Conclusions, statements, references (p. 15 to 21)

#### Substantive findings

**GB-51 Discussion and Abstract call the method "validated" with real data, but the Conclusions do not take up the three natural-data questions, and the natural tests support a weaker verb.**

| Field | Content |
|---|---|
| Check | P15, P32 |
| Location | p. 15, l. 451; p. 1, l. 8; p. 16, l. 477 to 489 |
| Quotation | "We explained and validated the use of binned XRD peak-area data as mineralogical fingerprints within a non-linear inversion scheme to infer erosion rate maps." and "The application to real-world datasets further validates the practical utility and robustness of the model." |
| Concern | The manuscript states three natural-data questions (p. 10, l. 282 to 285): fingerprints match the lithologies; subcatchment samples are attributed only to lithologies inside it; adding XRD to zircon improves stability and accuracy. The Conclusions (p. 16, l. 477 to 489) answer none of them: in p. 15, l. 450 to p. 16, l. 489 "natural" and "Gorner" occur once each (p. 15, l. 463, Discussion), and in the Conclusions 0 times; the Conclusions summarise only the synthetic experiments (p. 16, l. 482). Question 1 is answered qualitatively (GB-36), question 2 rests on one excluded unit while a second unit fails the criterion (GB-37), question 3 on one sample with a result that runs against the claim (GB-42). The manuscript itself uses the weaker "supports the reliability" for the natural case (p. 14, l. 417). Search of `text.json`, p. 1 to 16, for "validat": 12 hits (p. 1, l. 3 and 8; p. 2, l. 61; p. 3, l. 69 and 74; p. 4, l. 128; p. 5, l. 136 and 141; p. 9, l. 266 and 267; p. 10, l. 288; p. 15, l. 451), for "confirm": 1 hit (p. 14, l. 415); no independent check sample is reported anywhere. The method result stands; what the natural tests show is not traceable from Discussion and Conclusions, hence moderate. |
| Suggestion | Add to the Conclusions (p. 16, after l. 486) one sentence per natural-data question with its answer and its limits (qualitative fingerprint check, one excluded unit, one sample for the zircon comparison); replace "validated" at p. 15, l. 451 and "further validates" at p. 1, l. 8 by "tested" or "supported". |
| Status | searches and wording: verified; judgement on verb strength: inferred |
| Severity | moderate |
| Source | S4 |

**GB-52 Three statements in Discussion and Conclusions have no result behind them: the benefit of a broad tracer set for stability and resolution, the effect of the number of source areas, and minimal sediment storage as a result.**

| Field | Content |
|---|---|
| Check | P15, P10 |
| Location | p. 15, l. 457 to 458; p. 15, l. 460 to 461; p. 16, l. 484 to 485 |
| Quotation | "Including a broad set of tracer minerals further improves model stability and resolution." and "A higher number of distinct source areas leads to higher posterior resolution and lower uncertainty." and "Our results suggest that the method is best applied in catchments with minimal sediment storage" |
| Concern | (a) The tracer test found a threshold, not a monotone benefit: "The inversion with 7 tracers results in approximately the same posterior solution as with the full tracer set." (p. 12, l. 360) and "reducing the number of tracers has a comparatively limited effect" (p. 12, l. 364 to 365); "resol" gives 0 hits in p. 11, l. 322 to p. 12, l. 365, so neither "more resolvable" (p. 15, l. 457) nor "resolution" (p. 15, l. 458) has a result. (b) No test varies the number of source areas; it stays at 7 throughout (search "number of": 7 hits, p. 6, l. 170; p. 9, l. 244; p. 12, l. 355, 361 and 364; p. 13, l. 387; p. 15, l. 461, none in the Results about source areas; "source area" 0 hits in p. 11, l. 322 to p. 12, l. 365). (c) Storage is a model assumption ("assumes immediate sediment export", p. 15, l. 467 to 468), not a result: "storage" occurs 6 times, all in the Introduction and in p. 15, l. 467 and p. 16, l. 485, never in Sections 4.1 or 4.2. GB-53 cites the neighbouring lines for the application domain; this finding concerns statements without results. |
| Suggestion | Replace p. 15, l. 457 to 458 by a statement matching Section 4.1.3 (for example "retaining at least the 7 most informative tracers gave about the same posterior as all 21; fewer tracers increased error and uncertainty"); add a synthetic test that merges or splits units at constant tracers, or reword p. 15, l. 460 to 461 as an expectation with a source; at p. 16, l. 484 separate storage as a model assumption from the results on source distinctness and map knowledge. |
| Status | verified (searches) |
| Severity | moderate |
| Source | S4, SD |

**GB-53 The recommended application domain, a well constrained source lithology, conflicts with the claim that the approach is particularly valuable in glacierized catchments, where the lithology under ice is inferred.**

| Field | Content |
|---|---|
| Check | P15 |
| Location | p. 15, l. 459 to 460; p. 15, l. 464; p. 2, l. 61 to p. 3, l. 62 |
| Quotation | "accurate spatial delineation of source areas is crucial, which can be challenging in glaciated catchments with limited outcrop exposure." and "a) the spatial distribution of source lithologies is well constrained" |
| Concern | The Introduction motivates the method by glacierized catchments: "This spatially informed approach to sediment provenance is particularly valuable in glacierized catchments, where ice cover limits direct observations" (p. 2, l. 61 to p. 3, l. 62). In the study catchment the lithology under ice is inferred ("In ice-covered regions, where direct geological mapping is not possible, we infer the lithology based on regional geological knowledge.", p. 9, l. 270 to 271), and map uncertainty is the second most influential degradation factor (p. 12, l. 363 to 364). The Discussion then recommends the method only where source lithology is well constrained, without saying whether the Gornergletscher meets this condition or how large its map uncertainty is compared with the area mismatches of Fig. 7. Wording: "glaciated" (p. 15, l. 460) occurs only here; elsewhere "glacierized" (5 hits on p. 1 to 16). GB-52 cites p. 15, l. 460 to 461 for the number of source areas, and GB-11 cites p. 2, l. 58 to 61 for the novelty claim; this finding concerns the application domain. |
| Suggestion | Add to the Discussion (p. 15, after l. 466) a paragraph stating for the Gornergletscher how much of the source map is inferred under ice and how this compares with the tested area mismatch, and qualify p. 2, l. 61 to p. 3, l. 62 accordingly; write "glacierized" at p. 15, l. 460. |
| Status | wording and counts: verified; the conflict as such: inferred |
| Severity | moderate |
| Source | S4 |

**GB-54 The Conclusions say that resolution and posterior covariance can be used to assess reliability, but in Figure 5 the lowest posterior covariance lies where the difference to the true map is largest.**

| Field | Content |
|---|---|
| Check | P15 |
| Location | p. 16, l. 483 to 484; Fig. 5 (p. 26), panels c, d and e |
| Quotation | "We highlight how model resolution and posterior covariance can be used to assess the reliability of inferred erosion patterns." |
| Concern | The only test with known truth (Fig. 5) is not used to compare the metrics with the actual error. Measured on page image p. 26 (150 dpi, colour matching to the colour bars): the most negative difference in panel c (about −1.8 on the bar from −2 to 2) lies inside the hotspot ellipse; the lightest pixel of the posterior covariance diagonal in panel e, the low end of its bar, lies at the same map position within about 5 px (offset between the two extremes equal to the offset between the panels). The text reads this as "Posterior covariance is lowest in regions of high erosion, where the signal is strongest and most easily inferred (Figure 5E)." (p. 10, l. 300 to 301). The resolution diagonal (d) lies between about 0.90 and 1.00 over the whole map, with its lowest values in the west. If low covariance coincides with the largest error, the metrics indicate the least reliable area as the most reliable. Do the authors read Fig. 5 the same way? GB-24 cites p. 16, l. 482 to 483 for the claims of the synthetic tests, GB-26 the pairing of resolution and normalised uncertainty, GB-23 the legend of Fig. 5j, GB-51 the Conclusions as a whole and GB-52 p. 16, l. 484 to 485 for the storage statement; this finding concerns covariance against error. |
| Suggestion | Add to Section 4.1.1 a pixel-wise comparison of absolute error with posterior covariance and resolution for Fig. 5 (scatter plot or rank correlation), and word p. 16, l. 483 to 484 according to that result. |
| Status | inferred (colour-scale measurement at 150 dpi, approximate values), asked as a question |
| Severity | moderate |
| Source | S4 |

**GB-55 Two outlook proposals are weakened by the manuscript's own results: the method is offered for zircon U-Pb data alone, although the zircon-only inversion was "highly unstable", and for land-use maps, although indistinct fingerprints are its main limitation.**

| Field | Content |
|---|---|
| Check | P15 |
| Location | p. 16, l. 487 to 489; p. 15, l. 466 |
| Quotation | "Similarly, the method is not limited to XRD-derived fingerprints and can be applied to other types of tracer data, including zircon U-Pb age distributions or geochemical compositions." and "Other types of source area maps, such as those based on land use, can also be incorporated." |
| Concern | (a) The zircon-only inversion gave "the resulting posterior solution is highly unstable, with extreme erosion rate values" (p. 14, l. 435), with normalised uncertainty 0.87; the manuscript names a possible cause, the missing and replaced fingerprints (p. 14, l. 430 to 434; GB-41). The Conclusions offer zircon U-Pb data without this condition. (b) The forward model assumes that "each source area has its unique lithological fingerprint" (p. 5, l. 146), and the synthetic tests conclude that "poorly distinguishable fingerprints are a major limitation in source attribution" (p. 12, l. 353 to 354). Land-use classes would need mineralogically distinct XRD fingerprints; no result shows that, and the proposal does not name the condition. Neither proposal is tested. Is the zircon instability attributed to the missing fingerprints? KK-15 corrects "sub-catchments" at p. 16, l. 488, and GB-51 cites the Conclusions as a whole for the missing natural-data answers; this finding concerns the outlook. |
| Suggestion | At p. 16, l. 488 to 489 add the condition shown by the own results, for example "provided that fingerprints are available for all source units and are sufficiently distinct (average JS distance above about 0.55 in our synthetic tests)", and mention the zircon-only instability; at p. 15, l. 466 and p. 16, l. 488 state that land-use classes would have to differ in mineralogy. |
| Status | (a) verified; (b) inferred |
| Severity | moderate |
| Source | S4 |

**GB-56 Three reference entries lack the publisher or source information that comparable entries give.**

| Field | Content |
|---|---|
| Check | P16 |
| Location | p. 17, l. 521; p. 19, l. 583; p. 19, l. 599 to 600 |
| Quotation | "Bearth, P.: Blatt 535 Zermatt - Geologischer Atlas der Schweiz 1:25 000, 1953." and "Gjems, O.: Studies on clay minerals and clay-mineral formation in soil profiles in Scandinavia, 1967." |
| Concern | The map sheet has no publisher, the Gjems entry has neither series, journal nor publisher, and the Lafuente et al. chapter ("The power of databases: the RRUFF project, Highlights in Mineralogical Crystallography", p. 19, l. 599 to 600) has no editors and no publisher, while comparable book and chapter entries name them (Aster et al., p. 17, l. 514 to 516; Menke, p. 19, l. 610 to 611; Tarantola, p. 20, l. 634 to 635). A reader cannot locate the Gjems work from the entry. The Gergel entry lacks its title (KK-26). |
| Suggestion | Complete the three entries with publisher (Bearth), series or journal and publisher (Gjems), and editors, publisher and place (Lafuente et al.). |
| Status | verified (page images p. 17 and 19) |
| Severity | minor |
| Source | S4 |

#### Minor corrections

| ID | Location | Quotation | Replacement | Source |
|---|---|---|---|---|
| KK-23 | p. 16, l. 491 | "All authors (FDD, FH, BB, TA)" | "All authors (F.D.D., F.H., B.B., T.A.)", as at p. 16, l. 491 to 494 | S4 |
| KK-24 | p. 17, l. 522 to 523 | "Master’s thesis, University of Lausanne, unpublished master’s thesis, 2021." | "unpublished Master’s thesis, University of Lausanne, 2021." GB-39 asks for a locator in the same entry; this correction concerns the duplicated wording. | S4 |
| KK-25 | p. 17, l. 526 | "Mineralogical society of America" | "Mineralogical Society of America" | S4 |
| KK-26 | p. 19, l. 578 | "[No title found]" | "Landscape indicators of human impacts to riverine systems" (same authors, Aquatic Sciences 64, 118 to 128, 2002, same DOI; verified on https://experts.illinois.edu/en/publications/landscape-indicators-of-human-impacts-to-riverine-systems/) | S4 |
| KK-27 | p. 20, l. 612 | "New-York" | "New York" | S4 |
| KK-28 | p. 20, l. 635 | "ISBN 9780898715729 9780898717921" | "ISBN 9780898715729" (or both numbers separated by a comma) | S4 |
| KK-29 | p. 20, l. 639 | "Bomb-fallout137 Cs" | "Bomb-fallout ¹³⁷Cs" (superscript 137 directly after "fallout" and a space before "Cs" on the page image) | S4 |

#### Verification log

| ID | Check | Checked | Values | Result |
|---|---|---|---|---|
| PP-39 | P4 | Section numbering and headings, p. 1 to 16 | 1 Introduction (p. 1, l. 9); 2 Introduction (p. 3, l. 76); 3 Methods (p. 5, l. 143) with 3.1 to 3.4; 4 Validation (p. 9, l. 266) with 4.1, 4.1.1 to 4.1.4, 4.2, 4.2.1, 4.2.2; 5 Discussion (p. 15, l. 450); 6 Conclusions (p. 16, l. 477); no cross-references to sections, tables, appendices or supplements | Subsections consecutive; duplicate Introduction in GB-04; otherwise no finding |
| PP-40 | P4 | Citations against the reference list in both directions | Reference list p. 17, l. 501 to p. 21, l. 653: 64 entries; in-text citations p. 1 to 16 extracted with Python (line breaks joined): 64 distinct author-year keys, 161 year tokens; citations without entry 0; entries without citation 0 | no missing and no uncited entry; wrong target in GB-07 |
| PP-41 | P4 | Short citation against entry: year, spelling, "et al." | 64 keys: year equal in 64; 11 two-author entries cited with "and"; all 41 entries with more than two authors cited with "et al."; single authors by name | form mismatches 0; author name "E." in KK-02 |
| PP-42 | P15 | Every statement of Discussion and Conclusions mapped to a Results location | p. 15, l. 451 "validated" (GB-51); l. 452 to 454 four inputs (export estimate in GB-40); l. 454 to 455 novelty (GB-11); l. 456 to 457 distinct signatures essential: p. 12, l. 351 to 354, supported; l. 457 to 458 tracer breadth (GB-52); l. 459 to 460 map delineation crucial: p. 12, l. 363 to 364, supported; l. 460 to 461 source areas (GB-52); l. 461 to 463 zircon combination (GB-42); l. 467 to 468 storage caution: consistent with the model assumption; p. 16, l. 478 to 481 description of the method: consistent with Section 3; l. 482 reliable recovery: under ideal conditions (GB-24); l. 482 to 483 robustness (GB-34); l. 483 to 484 metrics for reliability (GB-54); l. 484 to 486 best applied (GB-52) | findings as listed; the remaining statements follow from the Results |
| PP-43 | P15, P9 | Every outlook proposal against the own findings | (1) well constrained lithology (p. 15, l. 464) against the glacierized motivation (GB-53); (2) strong mineralogical contrasts (l. 464 to 465) against p. 12, l. 351 to 354: consistent; (3) multiple tracers or combinable data (l. 465 to 466) against GB-52 and GB-42; (4) land-use maps (l. 466; p. 16, l. 488) (GB-55); (5) caution against storage: consistent; (6) best applied conditions (p. 16, l. 484 to 486) (GB-52); (7) sub-catchments as classification (p. 16, l. 488): no own result against it; (8) zircon or geochemical tracers (p. 16, l. 488 to 489) against p. 14, l. 435 (GB-55); zircon JS 0.48 below the own 0.55 threshold | findings GB-42, GB-52, GB-53, GB-55; proposals 2, 5 and 7 no finding |
| PP-44 | P15 | XRD limitation paragraph p. 15, l. 469 to p. 16, l. 476 | Grain size (Gjems, 1967), mitigation by powdering and depth-integrated samples (Butler et al., 2019); preferred orientation (Weir et al., 1975); Peak Finder and quartz alignment; averaging of peak areas, consistent with p. 9, l. 259 to 260 | hedged and sourced; disclosed by the manuscript; place in GB-12, sampling in GB-06 |
| PP-45 | P15 | Theory frame and core terms of the Introduction in Discussion and Conclusions (p. 15, l. 450 to p. 16, l. 489, Python) | Taken up: posterior uncertainty, resolution, erosion rate maps, source areas, storage, zircon, glacier only as "glaciated"; not taken up: "cost" 0, "time-" 0, "efficien" 0, "Bayes" 0, "frequentist" 0, "temporal" 0, "timing" 0; "natural" 1 and "Gorner" 1 (both p. 15, l. 463) | findings GB-01, GB-02, GB-51 |
| PP-46 | P32 | Results called confirmed or validated | "validat" 12 hits in `text.json`, p. 1 to 16 (Abstract p. 1, l. 3 and 8; Introduction, both copies; heading and first sentence of Section 4, p. 9, l. 266 and 267; p. 10, l. 288; Discussion p. 15, l. 451); "confirms" 1 hit (p. 14, l. 415); no independent check sample | covered by GB-24, GB-37 and GB-51 |
| PP-47 | P16 | Language and typesetting of p. 15, l. 450 to p. 16, l. 499 on the page images | Grammar, word choice, punctuation, line-end hyphenation ("inten-/sities", p. 15, l. 469 to 470, correct), URL at p. 16, l. 490 unbroken | errors at p. 15, l. 455, 460, 462 and 463 in GB-11, GB-53, GB-42 and KK-08; initials in KK-23; no further finding |
| PP-48 | P16 | Uniformity of the reference list, p. 17 to 21, on the page images (style conformity is an optional check) | Element order author, title, source, volume, pages, DOI, year kept in all 64 entries; DOI present in 55 of 64 (missing: Bearth, Belotti, Bish and Post, E., Gjems, Lafuente, Moore and Reynolds, Papanicolaou, Tarantola; books, thesis and map allowed without DOI); article numbers with thin space consistent | findings GB-56, KK-24 to KK-29 |
| PP-49 | P16 | Statements: code and data availability, author contributions, competing interests, acknowledgements (p. 16, l. 490 to 499) | Zenodo DOI given; roles named for all four authors; competing interests declared none; no statement on the use of AI tools | initials in KK-23; coverage of the data statement in GB-19, GB-21, GB-39, GB-40; otherwise no finding |
| PP-50 | Locations (merging step 5) | Locations at page boundaries, on lines that `text.json` places on another page, and on unsafe lines, listed by `formatpruefung.py --fundorte` | Counted on the page images from the printed margin number in brackets: p. 1, l. 1, 3, 4, 25 and 26 (5, 25); p. 2, l. 28 (30); p. 2, l. 61 and p. 3, l. 62 (60 and 65); p. 3, l. 91, 92 and 93 (90, 95); p. 4, l. 128 (125); p. 5, l. 152, 155, 156, 159 and 160 (150, 155, 160); p. 6, l. 172, 175, 176, 177, 178, 181, 183, 184, 185 and 186 (170, 175, 180, 185; eq. 8 is the line after 185); p. 7, l. 189, 197 and 201 (190, 195, 200); p. 8, l. 219, 220, 225, 236, 238 and 239 (215, 220, 225, 235, 240); p. 9, l. 272 and 273 (270); p. 10, l. 274, 305 and 306 (275, 305); p. 11, l. 336 and 339 (335); p. 12, l. 371, 372 and 373 (370); p. 13, l. 374 and 406 (375, 405); p. 14, l. 409, 435 to 438 and 440 (410, 435, 440); p. 15, l. 441, 444 and 473 (445, 470); p. 16, l. 498 and 499 (495, continued by 500 on p. 17); p. 20, l. 612 (615). `text.json` is shifted against the page image at p. 3 after l. 90, p. 5, l. 151 to 159, p. 6, l. 186, p. 11, l. 337 to 339 and p. 12, l. 371 to 373 | all confirmed; corrected during merging: GB-22 (p. 11, l. 339 instead of 338 to 339), GB-30 (p. 6, l. 185 to 186), GB-32 (quotation starts at p. 12, l. 352), PP-22 (p. 12, l. 373) |
| PP-51 | Wording (merging step 5) | Every quotation in the Quotation fields and every quoted fragment in Concern and Replacement, searched literally in `text.json` (line breaks joined, hyphenation at line ends removed, whitespace normalised) | Fragments not in `text.json` are figure-internal labels (legends, panel titles, axis labels, credits) and were read on the page images p. 23 to 37 | all found or confirmed on the page image |

## Optional checks

| Area | What it needs | Responsible | Run |
|---|---|---|---|
| DOI resolution | one request per reference entry with a DOI | `science-quellenapparat-pruefung` | no |
| Citation style | the name of the style | `science-zitierstil-harvard-ctr` or the style rules of the journal | no |
| AI statement against publisher policy | the policy of the target publisher | this review, on request | no |
| Relation to the authors' own prior work | the authors' prior work | this review, on request | no |
| Journal requirements | the author guidelines of the target journal | this review, on request | no |
| Subject accuracy | access to the sources of the checked statements and a selection of sections | `science-faktenbeleg-pruefung`, `geo-frage-belegbasiert-klaeren` | no |

## Limits of this review

- Checked version: egusphere-2025-4695.pdf, 37 pages, SHA-256 9c80676054f96ecd6f00f4d2a8b5ba568e03c6949e3856d363ac1c4abb42e7bd.
- Sources not readable or read only in part: Das et al. (2023), https://doi.org/10.1029/2023WR034500 (publisher page not readable, only a summary record); Niu et al. (2020), https://doi.org/10.1007/s11368-019-02424-1 (abstract only); Wilson et al. (1993), https://doi.org/10.1016/0143-6228(93)90036-Z (title only); Haddadchi et al. (2013), https://doi.org/10.1016/S1001-6279(14)60013-5 (not reachable, the list of frequentist methods could not be checked against it); Olley et al. (1993) and Walden et al. (1997) (title level only); De Doncker et al. (2020), https://doi.org/10.1002/esp.5008 (abstract only); the UNESCO 2009 report behind "E., W. D." (not readable, surname inferred); the Zenodo archive of the code and data (record read, archive not readable; content inferred from the GitHub README of the main branch); the thesis of Belotti (2021) (catalogue record read, PDF not opened).
- Measurements in figures were taken by the instance AB at 300 and 600 dpi and by S4 at 150 dpi (GB-54); colour matching through semi-transparent maps over hillshade gives approximate values, stated with their status.
- `text.json` is shifted by one line or more on several pages (p. 3 after margin number 90, p. 5, 6, 8, 11 to 15); all locations were taken from the printed margin numbers on the page images.
- Findings with status assumption for at least one sub-statement: 15 of 56; each such sub-statement is put as a question, and no finding rests on an assumption alone.
- Optional checks run: 0 of 6.
- Omitted instances: none.
- Discarded findings: 0 of 84 instance findings; every instance finding had all required fields and was confirmed at the manuscript in its core. 29 instance findings were merged into others (84 instance findings became 55 findings; S3-GB-13, AB-GB-06, SD-GB-11 and SD-GB-12 were each split between two findings by subject); 1 finding (GB-15) was added in the merging step from hints outside the checklists. Of 69 instance minor corrections, 29 remain after merging; the others were merged with each other or absorbed into findings that name the same place and subject. Hints outside the checklists that were not taken up: the unit of the data standard deviation (resolved by eq. 2, which scales d to an erosion rate), the omitted normalising denominator between eqs. 1 and 3, the rising normalised covariance trace in Fig. 5h, the title of the Zenodo record, and scale bars of Figs. 12 to 16 (checked in PP-19).
