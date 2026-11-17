# Review report: From XRD signal to erosion rate maps

| Field | Value |
|---|---|
| Manuscript | De Doncker, F., Herman, F., Belotti, B. and Adatte, T. (2025) From XRD signal to erosion rate maps. EGUsphere preprint egusphere-2025-4695, https://doi.org/10.5194/egusphere-2025-4695 |
| Version reviewed | egusphere-2025-4695.pdf, 37 pages, SHA-256 9c80676054f96ecd6f00f4d2a8b5ba568e03c6949e3856d363ac1c4abb42e7bd |
| Date | 2026-10-18 |
| Language | English |
| Review instances | Segments 1 to 4, figures, study design; the six review instances ran as separate agents, each without the context of the others; consolidation, overall assessment and format check by a seventh agent |

## Summary

The manuscript is a method development study. It builds a non-linear Bayesian inversion that turns binned X-ray diffraction (XRD) peak areas of suspended sediment and of source rocks into spatially explicit erosion rate maps, with erosion rates cast in log-space to keep them positive, a smoothing prior covariance, and two iterative schemes (steepest descent and quasi-Newton). Posterior covariance, resolution and a normalised posterior uncertainty are reported as reliability metrics. Validation has two parts. Synthetic forward-inverse tests use one "true" map with one hotspot, three data degradation scenarios (three geological maps, 20 levels of fingerprint blending, 1 to 21 tracers) and one-at-a-time sweeps of five hyperparameters. Natural tests in the Gornergletscher catchment use 21 tracer minerals for seven lithological units, a subcatchment as natural analogue of a known mixture test, and a comparison of zircon U-Pb, XRD and combined inversions of one detrital sample of 28 June 2019. Key numbers: degradation sets in below an average Jensen-Shannon (JS) distance of 0.55; 7 tracers give about the same solution as 21; the normalised posterior uncertainty is 0.87 (zircon), 0.82 (XRD) and 0.86 (combined); the average JS distance rises from 0.48 to 0.57 when XRD is added to zircon.

## Strengths

1. The reference apparatus is complete in both directions: 64 distinct citations match 64 entries one to one, with identical years and alphabetical order, so every cited claim can be traced to an entry (PP-34); the exceptions are single entries (GB-04, GB-07).
2. The inversion code is archived under a resolving DOI with a public licence, so the synthetic tests can in principle be rerun from the archive (PP-07); what the archive covers for the natural data is open (GB-21).
3. The synthetic part follows a stated test matrix: both schemes, all three degradation scenarios and all five hyperparameters announced are reported, and the reference run gives the same error, uncertainty and misfit values across Fig. 7, 9 and 10, which lets a reader attribute changes to the varied parameter (PP-16, PP-20).
4. The authors disclose the gaps in their own inputs at the point where they arise: missing zircon data for two units and the substituted fingerprint, the inferred subglacial geology, and the storage assumption; the zircon balance closes with the information given (PP-06, PP-13, PP-30).

## Weaknesses

1. The headline claims go beyond the results. Combining XRD with zircon data is said to stabilise and improve the solution, but on the only reported metric it is worse than XRD alone; abstract and conclusions state convergence and robustness without the failure ranges of Sect. 4.1, and recommend zircon data and effects of tracer and source counts that were not shown (GB-02, GB-51, GB-52, GB-54, GB-56). Suggestion: restate each claim with its reference case, metric and tested range.
2. The validation design cannot separate accuracy from self-consistency. Synthetic data come from the same forward model with a prior equal to the true mean and one true map; the natural known-mixture test can fail only through one small unit; the prior of the natural runs is not stated; and the zircon hotspot may reflect a near-zero fingerprint (GB-30, GB-45, GB-47, GB-50). Suggestion: add noisy data, an independent prior and several true maps to the synthetic tests, and a laboratory known-mixture test with source powders.
3. The construction of the XRD fingerprints is not shown to be compatible with the mixing model. Per-sample maximum normalisation breaks the weighted-average forward model, several tracer rows are identical, the fingerprints plotted in Fig. 15 follow a different normalisation from Fig. 11, the fingerprints are not compared with the expected mineralogy, and the uncertainty rests on one fixed data standard deviation (GB-12, GB-15, GB-22, GB-23, GB-29, GB-43). Suggestion: justify or replace the normalisation, merge identical tracers, and propagate within-unit and measurement variability.
4. Several result statements are not borne out by the figures, and inputs needed to reproduce the natural runs are missing: the sensitivity sweeps and the chosen hyperparameters, the resolution maps, the colour scale of the posterior map, the accuracy of quasi-Newton against steepest descent, the scenario ranking, and the sediment export, sample data, spatial inputs and processing settings (GB-14, GB-17, GB-19, GB-21, GB-24, GB-27, GB-31, GB-33, GB-36, GB-40, GB-41, GB-42). Suggestion: align each sentence with the plotted values and add a table of inputs, samples and settings with their archive location.

## Findings by segment

### Segment 1: Title, abstract, introduction (p. 1 to 5)

#### Substantive findings

**GB-01 Time and cost efficiency is stated as a result in abstract, introduction and aims but is not measured.**

| Field | Content |
|---|---|
| Check | P33 |
| Location | p. 1, l. 3 to 4; p. 2, l. 35 and l. 40 to 42; p. 3, l. 74 to 75; duplicate p. 5, l. 141 to 142 |
| Quotation | "we validate a time- and cost-effective fingerprinting approach"; "offering an efficient alternative to conventional approaches" |
| Concern | The manuscript gives no analysis time or cost per sample for XRD, none for the zircon U-Pb dating it compares with, and no throughput. The only support is the statement that many other methods are expensive and time-consuming (Das et al., 2023, l. 35), which does not quantify XRD. |
| Suggestion | Add in Sect. 4.2.2 or 5 a short comparison of preparation and measurement time and cost per sample for XRD and zircon U-Pb in this study, or reduce the claim in l. 3 to 4 and l. 74 to 75 to a reference to Das et al. (2023). |
| Status | verified |
| Severity | moderate |
| Source | SD |

**GB-02 Abstract and conclusions state consistent convergence, reliable recovery and robustness without the conditions and failure ranges that Sect. 4.1 reports.**

| Field | Content |
|---|---|
| Check | P2, P15 |
| Location | p. 1, l. 7 to 8; p. 16, l. 482 to 483; p. 3, l. 74 to 75; results p. 10, l. 288 to 289; p. 11, l. 312; p. 12, l. 351 to 354 and l. 360 to 362; p. 12, l. 373 to p. 13, l. 374; p. 13, l. 380 and l. 387; p. 14, l. 435; Fig. 8 caption |
| Quotation | "Forward-inverse tests with synthetic data demonstrate consistent convergence of the posterior solution. The application to real-world datasets further validates the practical utility and robustness of the model."; "Using synthetic forward-inverse experiments, we show that the true erosion pattern can be reliably recovered, and that the method is robust across a range of parameters." |
| Concern | Sect. 4.1 defines the conditions under which the inversion converges, which is a useful result in itself: quasi-Newton scheme, average JS distance above about 0.55, at least 7 tracers, enough iterations; steepest descent needed gradient normalisation (l. 312), and "In many of these cases, the inversion fails to converge" below JS 0.44 (l. 353). All synthetic tests use one true map with one localised hotspot (l. 288 to 289). Of the two natural tracer sets, zircon alone gives a "highly unstable" solution above 8000 mm/y (l. 435). The abstract and l. 482 to 483 state convergence and robustness without these bounds, and "show" generalises from one test configuration. Major, because these sentences report the outcome of the validation, which is the research aim. |
| Suggestion | In the abstract (l. 7 to 8) and in l. 482 to 483, name the conditions of convergence (scheme, JS distance, tracer count, iterations), the single synthetic hotspot scenario, and the instability of the zircon-only inversion; or add synthetic tests with further true maps before generalising. |
| Status | verified |
| Severity | major |
| Source | S3, S4 |

**GB-03 The introduction is printed twice, as Section 1 and verbatim as Section 2, so all later section numbers are shifted by one.**

| Field | Content |
|---|---|
| Check | P4 |
| Location | p. 1, l. 9 to p. 3, l. 75 (Section 1); p. 3, l. 76 to p. 5, l. 142 (Section 2); Sections 3 to 6 from p. 5, l. 143 |
| Quotation | "1 Introduction"; "2 Introduction" |
| Concern | A word-level comparison with difflib of l. 10 to 75 against l. 77 to 142 gives 1153 words each and a similarity ratio of 1.0 with no differing token. Every citation of the introduction is printed twice and Sections 3 to 6 carry numbers one higher than intended. The content is not changed, hence minor. |
| Suggestion | Delete Section 2 (p. 3, l. 76 to p. 5, l. 142) and renumber "3 Methods" to "6 Conclusions" as 2 to 5, including all subsections. |
| Status | verified |
| Severity | minor |
| Source | S4 |

**GB-04 The short citation "E., 2009" and its entry carry a garbled author name.**

| Field | Content |
|---|---|
| Check | P4 |
| Location | p. 1, l. 11 to 12; duplicate p. 3, l. 78 to 79; reference list p. 18, l. 567 to 568 |
| Quotation | "(Gergel et al., 2002; Allan, 2004; E., 2009; Hamel et al., 2015)"; "E., W. D.: The Impact of global change on erosion and sediment transport by rivers, UNESCO 2009, ISBN 9789231041358, oCLC: 1402659188, 2009." |
| Concern | "E." is an initial, not a surname; the entry inverts surname and initials. Title and ISBN point to the 2009 UNESCO report by D. E. Walling, so the citation should read "Walling, 2009" and the entry would sort under W. The UNESCO page could not be read, so the attribution rests on title, ISBN and initials. "oCLC" is a case artefact. |
| Suggestion | Correct the citation in l. 11 to 12 (and l. 78 to 79) to "Walling, 2009" and rewrite and re-sort the entry on p. 18, l. 567 to 568 as "Walling, D. E.: The impact of global change on erosion and sediment transport by rivers, UNESCO, ISBN 9789231041358, 2009." |
| Status | verified (garbled form); inferred (author Walling) |
| Severity | minor |
| Source | S4 |

**GB-05 The sources cited for direct sediment flux measurements with traps on dams are, by their titles, about bank erosion photogrammetry and a soil erosion survey.**

| Field | Content |
|---|---|
| Check | P13 |
| Location | p. 1, l. 18 to 19; duplicate p. 3, l. 85 to 86; reference list p. 17, l. 519 to 520; p. 21, l. 649 to 650 |
| Quotation | "Direct measurements, such as sediment traps installed on dams, provide valuable information on sediment fluxes but do not reveal the origin of the transported material (Wilson et al., 1993; Barker et al., 1997; Davis and Fox, 2009)." |
| Concern | Barker et al. (1997) is titled "Use of terrestrial photogrammetry for monitoring and measuring bank erosion" and Wilson et al. (1993) "Soil erosion in the Falkland Islands: an assessment". Neither title points to sediment traps, dams or flux measurements. Abstracts and full texts could not be read, so such measurements inside the studies cannot be ruled out. Do the authors mean these studies as examples of direct erosion measurement in general? |
| Suggestion | In l. 18 to 19 (and l. 85 to 86), cite studies that measure sediment flux with traps or reservoir deposits, or rephrase to "direct erosion and flux measurements, such as bank erosion monitoring or sediment traps". |
| Status | verified (titles); inferred (content, full texts not readable) |
| Severity | minor |
| Source | S1 |

**GB-06 Two cited studies are filed under the wrong fingerprint category, judging by their titles in the reference list.**

| Field | Content |
|---|---|
| Check | P13 |
| Location | p. 1, l. 26; p. 2, l. 30; duplicates p. 3, l. 93 and p. 4, l. 97; reference list p. 20, l. 621 to 622 and l. 641 to 642 |
| Quotation | "geochemistry (Olley et al., 1993; Gholami et al., 2019; Lipp et al., 2021; Domingo et al., 2023)"; "mineralogy (Walden et al., 1997; Nukazawa et al., 2021)" |
| Concern | Olley et al. (1993) is titled "Identifying sediment sources in a gullied catchment using natural and anthropogenic radioactivity", a radionuclide study. Walden et al. (1997) is titled "Use of mineral magnetic measurements to fingerprint suspended sediment sources", which belongs to magnetic properties. The misfiled example weakens the mineralogy entry, the category the manuscript builds on. |
| Suggestion | In l. 26 and l. 30 (and l. 93, l. 97), move Olley et al. (1993) to radionuclides and Walden et al. (1997) to magnetic susceptibility, and give a mineralogical example under mineralogy (see GB-09). |
| Status | verified |
| Severity | minor |
| Source | S1 |

**GB-07 The citation "Kobe, 2021" for plant pollen as a sediment fingerprint points to a theology article.**

| Field | Content |
|---|---|
| Check | P4, P13 |
| Location | p. 2, l. 31; duplicate p. 4, l. 98; reference list p. 19, l. 597 to 598 |
| Quotation | "plant pollen content (Brown, 1985; Kobe, 2021)"; "Kobe, S. L.: Ubuntu as a spirituality of liberation for black theology of liberation, HTS Teologiese Studies / Theological Studies, 77, https://doi.org/10.4102/hts.v77i3.6176, 2021." |
| Concern | Citation and entry match formally, but by its title the entry has no connection to pollen, sediment or fingerprinting; instance S1 read the publisher's abstract and metadata, which mention none of these. The statement rests on Brown (1985) alone. A reference manager mix-up is a plausible cause: is a different pollen study intended? Moderate, because the reference cannot back the statement. |
| Suggestion | Replace the entry on p. 19, l. 597 to 598 with the intended pollen fingerprinting study and adjust l. 31 (and l. 98), or delete "Kobe, 2021" and the entry. |
| Status | verified (mismatch, source read on the publisher page); assumption (identity of the intended source) |
| Severity | moderate |
| Source | S1, S4 |

**GB-08 The statement that XRD has only recently gained attention in provenance analysis has no stated basis, and XRD unmixing for sediment provenance was published in 2004 and 2012.**

| Field | Content |
|---|---|
| Check | P28 |
| Location | p. 2, l. 36 to 37; duplicate p. 4, l. 103 to 104; abstract p. 1, l. 3 to 4 |
| Quotation | "X-ray diffraction (XRD) has recently gained attention as a proxy for mineral abundance in provenance analysis but remains underutilized (Das et al., 2023)." |
| Concern | The sentence describes the state of research with one citation and no search basis. Eberl (2004) used quantitative XRD to unmix Yukon River sediment into tributary contributions, and Andrews and Eberl (2012) unmixed quantitative XRD mineralogy in eleven artificial mixtures (USGS Publications Warehouse records, read by instance S1); that is 19 and 11 years before the source cited for "recently" (Python). "Underutilized" may hold as a statement on frequency of use; "recently gained attention" does not. Das et al. (2023) could only be read as an abstract summary. |
| Suggestion | In l. 36 to 37 (and l. 103 to 104), drop "recently", cite the earlier XRD unmixing studies (GB-09), and give the basis for "underutilized" or phrase it as the authors' assessment. |
| Status | verified (counterexamples read); inferred (content of Das et al., 2023, full text not readable) |
| Severity | moderate |
| Source | S1 |

**GB-09 Direct predecessors of XRD-based sediment unmixing and of spatially resolved glacial erosion from detrital data are missing from the reference list.**

| Field | Content |
|---|---|
| Check | P14 |
| Location | p. 2, l. 36 to 42 and l. 58 to 61; duplicates p. 4, l. 103 to 109 and l. 125 to 128; p. 13, l. 404 to 406; reference list p. 17 to 21 |
| Quotation | "Building on the work of Das et al. (2023, 2024), we investigate the potential of binned XRD data as a cost-effective fingerprinting method." |
| Concern | The contribution: binned XRD peak areas of source rocks and suspended sediment turned into erosion rate maps of a glacierized catchment by non-linear Bayesian inversion. Three studies absent from the reference list (checked by text search of p. 17 to 21) anticipate parts of it: Eberl, D. D. (2004) Quantitative mineralogy of the Yukon River system: changes with reach and season, and determining sediment provenance. American Mineralogist, 89(11 to 12), pp. 1784 to 1794; Andrews, J. T. and Eberl, D. D. (2012) Determination of sediment provenance by unmixing the mineralogy of source-area sediments: the SedUnMix program. Marine Geology, 291 to 294, pp. 24 to 33, https://doi.org/10.1016/j.margeo.2011.10.007, which tests XRD unmixing with known artificial mixtures, the test the manuscript replaces by a natural analogue (l. 404 to 406); Ehlers, T. A., Szameitat, A., Enkelmann, E., Yanites, B. J. and Woodsworth, G. J. (2015) Identifying spatial variations in glacial catchment erosion with detrital thermochronology. Journal of Geophysical Research: Earth Surface, 120(6), pp. 1023 to 1039, https://doi.org/10.1002/2014JF003432. |
| Suggestion | In l. 36 to 42 add Eberl (2004) and Andrews and Eberl (2012) and say how binned peak areas differ from their quantitative mineral percentages; in l. 58 to 63 add Ehlers et al. (2015); in Sect. 4.2.1 relate the natural test to the artificial mixtures of Andrews and Eberl (2012). |
| Status | verified (records read by instance S1; reference list checked) |
| Severity | moderate |
| Source | S1 |

**GB-10 Niu et al. (2020) is cited for Bayesian error propagation, but its abstract describes a linear mixing model with Gaussian first-order uncertainty.**

| Field | Content |
|---|---|
| Check | P13 |
| Location | p. 2, l. 45 to 48; duplicate p. 4, l. 112 to 115 |
| Quotation | "Where frequentist methods estimate the uncertainty on the resulting source contributions by sampling the different possible sets of source contributions, Bayesian methods use priors, model and data uncertainty to allow error propagation so the a posteriori uncertainty can be inferred from different posterior metrics (Niu et al., 2020)." |
| Concern | The abstract of Niu et al. (2020), Journal of Soils and Sediments 20, pp. 1097 to 1111, reports "a linear mixing model" and uncertainty quantified "using the Gaussian first-order approximation"; it does not mention Bayesian or frequentist frameworks. Only the abstract was readable, so the body may still contain the comparison. Is Fathabadi and Jansen (2022), cited three lines later, the intended source? |
| Suggestion | Check the citation in l. 48 (and l. 115) and, if Niu et al. (2020) does not discuss Bayesian error propagation, cite a source that does, such as Fathabadi and Jansen (2022). |
| Status | inferred (only the abstract was readable) |
| Severity | minor |
| Source | S1 |

#### Minor corrections

| ID | Location | Quotation | Replacement | Source |
|---|---|---|---|---|
| KK-01 | p. 1, l. 5; p. 7, l. 211; p. 10, l. 287 and l. 296; p. 11, l. 320 | "(steepest descent and Quasi-Newtonian)"; "Quasi-Newton approach" | "(steepest descent and quasi-Newton)", and one capitalisation of quasi-Newton throughout the running text | S1, S2, S4 |
| KK-02 | p. 2, l. 48 to 49 and l. 51; p. 4, l. 115 to 116 and l. 118 | "the Non-Linear Least Squares (NLLS) (a constrained linear regression)"; "similar to the NNLS approach" | "the Non-Negative Least Squares (NNLS) (a constrained linear regression)", or NLLS in both places if non-linear least squares is meant | S1, S2, S4 |
| KK-03 | p. 2, l. 50; p. 4, l. 117 | "Generalist Likelihood Uncertainty Estimation (GLUE)" | "Generalized Likelihood Uncertainty Estimation (GLUE)" | S1, S4 |
| KK-04 | p. 2, l. 51; p. 4, l. 118 | "Maximal Likelihood Estimation (MLE)" | "Maximum Likelihood Estimation (MLE)" | S1, S4 |
| KK-05 | p. 2, l. 53 and l. 55 to 56; p. 4, l. 120 and l. 122 to 123 | "Bayesian Linear Mixing Models (BLMM)"; "a hybrid between Bayesian linear mixed models and hierarchical Bayesian models" | "a hybrid between Bayesian linear mixing models (BLMM) and hierarchical Bayesian models" | S1, S2 |
| KK-06 | p. 2, l. 61 (and p. 4, l. 128); p. 11, l. 333 to 334; p. 14, l. 424; p. 14, l. 424 to 425 | "validated in (De Doncker et al., 2020)"; "the map proposed by (Steck et al., 2015)"; "described in (Belotti, 2021)"; "outlined in (De Doncker et al., 2020)" | "validated by De Doncker et al. (2020)"; "the map proposed by Steck et al. (2015)"; "described in Belotti (2021)"; "outlined in De Doncker et al. (2020)" | S1, S4, SD |

#### Verification log

| ID | Check | Checked | Values | Result |
|---|---|---|---|---|
| PP-01 | P13 | All evaluative statements on cited work in abstract and introduction (l. 1 to 75; duplicate identical): 14 statements with citations, sources opened where possible | Collins et al. (2020), full text: composite signatures "increased during 2018 to 2019" and "adoption of frequentist and, more latterly, Bayesian un-mixing models" support l. 33 to 35 and l. 44 to 45; Das et al. (2024), repository record: XRD with MixSIAR, consistent with l. 40; De Doncker et al. (2020), abstract: least-squares inversion into erosion rate maps from zircon ages, consistent with l. 60 to 61; Lipp et al. (2021), abstract: 67 samples, 22 elements, consistent with l. 26. No external numbers in Segment 1. Limits disclosed: none | no finding beyond GB-05 to GB-10 |
| PP-02 | P28 | Gap and novelty statements of the type "no study", "not yet", "novel", "underutilized" in the whole manuscript | Four found: l. 36 to 37 (GB-08); l. 58 to 59, hedged with "typically" and limited to unmixing models, no separate finding; l. 454 to 455 (GB-53); abstract l. 3 to 4, a comparative claim (GB-01). No statement gives databases, search terms or dates of a literature search | no further finding |
| PP-03 | P13 | Sources that could not be read and statements left unverified | Das et al. (2023): abstract summary only, so l. 35 and l. 36 to 37 stay unverified; Klages and Hsieh (1975), cited at l. 21 and l. 24 to 25: not readable; Torres Astorga et al. (2020), cited for TOC at l. 30: not readable, the title names geochemical fingerprints; Haddadchi et al. (2013), Yang et al. (2025), Fathabadi and Jansen (2022), l. 48 to 55: not opened. Limits disclosed: none | no finding |
| PP-04 | P14 | Search for work that anticipates or contradicts the contribution, and mandatory check against the reference list | 4 queries (SedUnMix; detrital thermochronology of glacial erosion; XRD fingerprinting of glacial suspended sediment; Das et al. 2023). Candidates not in the list: Eberl (2004), Andrews and Eberl (2012), Ehlers et al. (2015), reported in GB-09. Dropped because already cited: Lipp et al. (2021), De Doncker et al. (2020), Saylor et al. (2019) | no further finding |
| PP-05 | P16 | Observations in the extracted text that are not errors on the page image | Line-end hyphenations "fin-gerprinting" (l. 40 to 41), "min-eralogical" (l. 68 to 69), "conver-gence" (l. 385 to 386) correct on the page images; the DOI of Steck et al. (2015) breaks at a hyphen that belongs to it (p. 20, l. 632 to 633); wide spacing in the Grimshaw and Lewin entry is justification; symbols lost in extraction in eq. 1 to 22 are typeset correctly on p. 6 and 8 | no finding |
| PP-06 | Design sketch | Research questions, study type, cases, comparisons, data sources, timeline, environment, components and disclosed limitations | Objective l. 63 to 64; natural aims 1 to 3 l. 282 to 285; study type method development with synthetic tests and one natural case; 7 units, pixel size 300 m (1200 m divided by 4), 21 tracers; scenarios: 3 maps, 20 blending levels, 1 to 21 tracers, 5 hyperparameters; natural: "multiple" samples (number not given) and one dated sample of 28 June 2019, 13:30; sediment export not given; XRD instrument settings and WinXRD version not given; inversion code on Zenodo; disclosed limitations: inferred subglacial geology (l. 270 to 272), small units (l. 299 to 300), indistinct fingerprints (l. 353 to 354), zircon gaps (l. 430 to 434), storage (l. 466 to 468), grain size and orientation (l. 469 to 476) | basis for GB-01, GB-12 to GB-24, GB-30, GB-45, GB-47, GB-55 |

### Segment 2: Methods, data, study area (p. 5 to 10; Fig. 1 to 4, 11, 12)

#### Substantive findings

**GB-11 Symbols in the schematic Fig. 1 and Fig. 2 are not explained.**

| Field | Content |
|---|---|
| Check | P29 |
| Location | Fig. 1, panel (b), p. 22; Fig. 2, panels (b) and (c), p. 23; referenced p. 5, l. 146 and p. 6, l. 166 |
| Quotation | "(b) tracer concentrations in suspended sediments, (c) tracer concentration maps based on geology and lithological fingerprints." |
| Concern | The arrow symbol on the plates of Fig. 1b and 2b is not explained. In Fig. 2b the bars of tracers 1, 2, 3 and n are coloured like the layers of Fig. 2c, the other seven are black without explanation. Fig. 2c shows four tracer layers in four colour ramps, but only the green ramp has a "tracer concentration low high" bar. |
| Suggestion | Explain the arrow symbol and the black bars in the captions of Fig. 1 and 2, and state that the colour ramp applies to all tracer layers of Fig. 2c or give one ramp per layer. |
| Status | verified |
| Severity | minor |
| Source | AB |

**GB-12 Per-sample maximum normalisation of peak areas is not compatible with the weighted-average forward model, and the synthetic tests cannot detect this.**

| Field | Content |
|---|---|
| Check | P9 |
| Location | p. 5, l. 151 to 152 and l. 154 (eq. 1); p. 9, l. 260 to 265 |
| Quotation | "Hence, the detrital data are a weighted average of the tracer mineral concentrations, with the weights being the erosion rates."; "these are normalized within each sample by dividing by the maximum observed peak area, yielding relative mineral concentrations on a scale from 0 to 1" |
| Concern | Eq. 1 assumes that each detrital tracer value is the erosion-weighted mean of the source values. After maximum normalisation each sample is divided by its own maximum, so a physical mixture is no longer the weighted mean of the normalised sources. Worked case (Python): source 1 with peak areas (100, 20), source 2 with (10, 10), mixed 1:1; normalised sources (1, 0.2) and (1, 1); weighted mean (1, 0.6); normalised mixture (1, 0.273); read through eq. 1, tracer 2 implies a share of 0.909 for source 1 instead of 0.5. The bias grows with differences in total diffracted intensity between lithologies. Because the synthetic data are generated with eq. 1 itself, Sect. 4.1 cannot reveal it. The manuscript introduces the normalisation to remove intensity differences (l. 263 to 265) but does not discuss its effect on mixing. Major, because every natural result rests on the mixing of normalised values. |
| Suggestion | In Sect. 3.4, state why maximum-normalised values may be mixed linearly, or replace the normalisation by one compatible with eq. 1 (for instance an internal standard or absolute peak areas per mass), and test it with a laboratory known-mixture experiment from the source powders, the usual test named in l. 404 to 406. |
| Status | verified (wording); inferred (incompatibility, worked numerically) |
| Severity | major |
| Source | SD |

**GB-13 The iteration index changes from k to n between eq. 17 and eqs. 18 and 19, both indices appear in one update rule, and n and m already denote the numbers of pixels and tracers.**

| Field | Content |
|---|---|
| Check | P38 |
| Location | p. 5, l. 154 (eq. 1); p. 6, l. 164 (eq. 4), l. 175 to 180 (eqs. 5 and 6); p. 7, l. 208 to 209 (eq. 17); p. 8, l. 215 to 216 (eq. 18) and l. 219 (eq. 19); Fig. 10 caption, p. 31 |
| Quotation | "with µ being the step size, and εk+1 the posterior model after k + 1 non-linear iteration steps."; "where Gn is the Jacobian at iteration n, Cm is the model covariance and µn is the step size." |
| Concern | Eq. 17 counts iterations with k. Eqs. 18 and 19 count them with n, but the prior term inside both is written with the index k (confirmed on page image 8). In eqs. 1 and 4, n is the number of pixels, and Fig. 10 uses n with subscript m for the maximal number of iterations. The MAP model is written with subscript m in eqs. 5 to 7, although m is the number of tracers, and the posterior has no subscript at l. 176. Read literally, eqs. 18 and 19 evaluate the data term at the current iterate and the prior term at another one. The code is archived, but the printed update rule is ambiguous. |
| Suggestion | Use one iteration index in eqs. 17 to 19 and l. 216 (replacing the k in the prior terms of eqs. 18 and 19), reserve n and m for pixel and tracer counts, and write the MAP model with a symbol not used for a count. |
| Status | verified |
| Severity | moderate |
| Source | S2, SD |

**GB-14 The total annual suspended sediment export, named four times as a required input, has no value, source, period or availability statement.**

| Field | Content |
|---|---|
| Check | P8, P12, P15 |
| Location | p. 5, l. 160 (eq. 2); p. 3, l. 65 to 66; duplicate p. 5, l. 132 to 133; p. 9, l. 267 to 268; p. 15, l. 452 to 454; p. 16, l. 479 to 480; p. 16, l. 490 |
| Quotation | "For simplicity, we redefine the data vector d as scaled by the total erosion rate:"; "d) an estimate of the total annual suspended sediment export from the catchment"; "due to the availability of multi-year suspended sediment datasets" |
| Concern | Eq. 2 scales the data by the total erosion rate, which converts relative contributions into rates in mm/y. A text search finds "export", "annual" and "yearly" only in the statements quoted above and in l. 468; no value, unit, source, year or conversion (catchment area, sediment density) is given, and the multi-year datasets that justify the choice of site (l. 267 to 268) have no reference. The data statement (l. 490) mentions neither. The absolute erosion rates of Fig. 13 to 16 and the "extreme erosion rate values" of l. 435 can therefore not be reproduced, even with the code. The prior of the natural runs is treated in GB-47. |
| Suggestion | In Sect. 3.1 state how the export estimate enters eq. 2, and in Sect. 4 give for each natural run the export value, its source and period and the conversion to the summed erosion rate; cite the multi-year datasets and add both to the statement at l. 490. |
| Status | verified (absence by text search, wording); inferred (consequence for Fig. 13 to 16) |
| Severity | moderate |
| Source | S2, S4, SD |

**GB-15 The posterior uncertainty, a headline output, rests on one fixed data standard deviation and ignores variability within source units.**

| Field | Content |
|---|---|
| Check | P9 |
| Location | p. 6, l. 186 (eq. 8); p. 1, l. 6 to 7; p. 10, l. 295; p. 14, l. 427 to 428; Fig. 3 caption, p. 24 |
| Quotation | "Cd = σd 2 I"; "invert detrital mineralogical data into erosion rate maps while quantifying posterior uncertainty and error propagation"; "a data standard deviation of 0.01 mm/y" |
| Concern | Cd is the identity times one variance, with 0.01 mm/y for synthetic and natural data alike; its derivation from measured XRD scatter (replicates, counting statistics) is not given. The unit mm/y is attached to data that are maximum-normalised to 0 to 1 and then scaled by the summed erosion rate (eq. 2); the unit chain is not stated. Matrix A holds one fingerprint per unit, so within-unit variability of mineralogy enters neither A nor Cd. The posterior covariance (eq. 20), resolution and the normalised uncertainties 0.82, 0.86 and 0.87 are therefore conditional on these choices. Fig. 10, row 3, shows that the data standard deviation changes the summed error by 0.012 % in the synthetic case; its effect on natural data is unknown. Major, because uncertainty quantification is one of the stated outputs of the method. |
| Suggestion | In Sect. 3.2 and 4.2, derive the data standard deviation for natural data from replicate diffractograms and state its unit chain; quantify within-unit variability from several source samples per unit and propagate it (added to Cd or by Monte Carlo over source fingerprints); state in Sect. 3.3 that the reported uncertainties are conditional on these choices. |
| Status | verified (fixed value, single fingerprints); inferred (consequence for the uncertainty) |
| Severity | major |
| Source | SD, ZF |

**GB-16 Equations 9, 12, 14 and 19 as printed differ from the forms that the text and eqs. 16 and 20 imply.**

| Field | Content |
|---|---|
| Check | P38 |
| Location | p. 7, l. 189 (eq. 9) and l. 190; p. 7, l. 197 (eq. 12); p. 7, l. 201 (eq. 14) against l. 205 (eq. 16); p. 8, l. 219 (eq. 19) against l. 225 (eq. 20) |
| Quotation | "with σm 2 the prior variance, si,j the Euclidean distance between point i and j, and L the smoothing distance." |
| Concern | Checked on page images 7 and 8. (1) Eq. 9 gives Cm(i,j) as the prior variance times exp(s squared over L squared), without a minus sign in the exponent. A covariance that grows with distance contradicts the role of L as a smoothing distance, and it is not a valid covariance: for two pixels at s = 300 m and s = 1200 m with σm = 3 and L = 1200 m the 2 by 2 matrix has eigenvalues of minus 0.58 and minus 15.47; with a minus sign they are 0.55 and 5.69 (Python). (2) Eq. 12 writes the Jacobian as A times exp(ε), which is a vector; eq. 16 uses its transpose as a matrix, which requires A times diag(exp(ε)). (3) Eq. 14 has no transpose on G, eq. 16 has. (4) Eq. 19 inverts the data term of the Hessian only, while eq. 20 adds the inverse prior covariance to it. Do the archived code and the reported runs use the standard forms? |
| Suggestion | Correct eq. 9 (minus sign), eq. 12 (diag), eq. 14 (transpose) and eq. 19 (prior term in the Hessian), or state in Sect. 3.2 why the printed forms are intended. |
| Status | verified (printed forms, eigenvalues computed); assumption (which forms the code uses), asked as a question |
| Severity | moderate |
| Source | ZF |

**GB-17 Several steps of the inversion and of its display cannot be rebuilt from the text: gradient normalisation, step sizes, PCA selection, the low-confidence hatching and the synthetic fingerprints.**

| Field | Content |
|---|---|
| Check | P8, P11, P29 |
| Location | p. 8, l. 215 (eq. 18); p. 10, l. 293 to 295; p. 11, l. 310 to 319; p. 12, l. 355 to 357; Fig. 5b (p. 26), Fig. 6 legend (p. 27), Fig. 14 to 16 legends (p. 35 to 37); Fig. 5k |
| Quotation | "In initial experiments, the steepest descent approach proved unstable, requiring the normalization of the gradient."; "We perform a Principal Component Analysis (PCA) to retain the subset of tracers that explain the maximum variance in the mineralogical fingerprints."; "Low-confidence areas" |
| Concern | (1) The gradient normalisation used for steepest descent is not in eq. 18 and its form is not given. (2) The step size of the first quasi-Newton test (l. 293 to 295) and the number of iterations and step size of the steepest descent run are not stated; Fig. 6g runs to 200 iterations. The choice of quasi-Newton for all later tests (l. 320 to 321) rests on this comparison. (3) PCA yields components, not tracers; the rule that ranks tracers from loadings is not given. (4) Hatched "low-confidence" pixels appear in Fig. 5b, 6b and 14 to 16, but no text or caption names the metric and threshold, and in Fig. 6 the hatch symbol has no label; in Fig. 15 the main XRD erosion peak lies in such an area. (5) How the 21 synthetic tracers A to U of Fig. 5k were generated is not described. |
| Suggestion | Give the normalised update in Sect. 3.2, the step sizes and iteration numbers of both runs in Sect. 4.1.1 and 4.1.2, the PCA selection rule in Sect. 4.1.3, the hatching criterion in Sect. 3.3 and the captions of Fig. 5, 6 and 14 to 16 (with a label in Fig. 6), and the construction of the synthetic fingerprints in Sect. 4.1.1. |
| Status | verified (text, captions and hatching on page images 26, 27, 35 to 37) |
| Severity | moderate |
| Source | SD, AB, S3 |

**GB-18 The normalised posterior uncertainty is defined in two ways and appears under six names and axis labels.**

| Field | Content |
|---|---|
| Check | P2, P38 |
| Location | p. 8, l. 225 (eq. 20) and l. 236 to 239 (eq. 22); p. 10, l. 303 and l. 306; p. 12, l. 352 and l. 361; p. 14, l. 436; p. 15, l. 441 to 442 and l. 446 to 447; Fig. 5 panels (f) and (h) and caption, p. 26; Fig. 6 caption, p. 27; Fig. 7 to 9, middle panels; Fig. 10, second column, p. 31; Fig. 14 to 16 |
| Quotation | "The third metric is the ratio between the posterior model covariance and the “prior” model covariance."; "The same pattern is visible in the normalised posterior variance, with lower values indicating better constraint (Figure 5F)." |
| Concern | Eq. 22 defines a per-pixel ratio of square roots of the posterior and prior covariances. Sect. 4.2.2 (l. 436) instead uses the ratio of traces without square roots and writes the posterior covariance with the subscript "m,post", while eq. 20 uses a tilde. The quantity then appears as normalised posterior covariance (Fig. 5f, 5h, Fig. 6 captions), normalised posterior variance (l. 303), posterior covariance (l. 306), posterior uncertainty (l. 352, l. 361), normalised posterior uncertainty (Fig. 10, 14 to 16), normalised covariance trace (Fig. 5h) and "Trace(post. cov.)" as axis label (Fig. 7 to 10). With a prior standard deviation of 3, an unnormalised trace would be 9 times the number of pixels, so the plotted values of about 0.74 must be normalised; the reader cannot tell whether the synthetic values (about 0.74) and the natural ones (0.82 to 0.87) are computed with or without the square root. Moderate, because these values carry the comparison of Sect. 4.2.2. |
| Suggestion | Define after eq. 22 both the per-pixel map and the scalar summary with distinct symbols, use one symbol for the posterior covariance, and relabel l. 303, 306, 352, 361, 436 and Fig. 5 to 10 and 14 to 16 accordingly. |
| Status | verified (definitions and labels on page images); inferred (that the trace axes show the normalised ratio) |
| Severity | moderate |
| Source | S2, S3 |

**GB-19 XRD acquisition and processing settings are not given in a form that allows the fingerprints to be reproduced.**

| Field | Content |
|---|---|
| Check | P35 |
| Location | p. 9, l. 250 to 265; p. 13, l. 393 to 398; p. 16, l. 490 |
| Quotation | "the WinXRD Peak Finder algorithm corrects for baseline drift and removes the background noise, facilitating the identification of local maxima through thresholding and peak fitting"; "diagnostic 2θ windows for each mineral are selected from RRUFF database reference spectra" |
| Concern | The six-step chain is clearly ordered and illustrated in Fig. 3. Missing for reproduction: diffractometer, radiation, 2θ range, step width and counting time; grain size after powdering and mount type; WinXRD version and thresholds; the 2θ windows per mineral; whether "average the total peak area within the 2θ windows" (l. 260) means the average of window sums or the sum of averages; the number of source samples per unit and how a unit fingerprint is formed from several samples. |
| Suggestion | Add to Sect. 3.4 a table of instrument and scan settings, software version and thresholds, and the 2θ windows of the 21 minerals; state the samples per unit and the aggregation rule. |
| Status | verified (absences searched in the full text) |
| Severity | moderate |
| Source | SD |

**GB-20 XRD limitations and the storage assumption appear only in the Discussion, and the recommended depth-integrated sampling is not related to the own pump samples.**

| Field | Content |
|---|---|
| Check | P17 |
| Location | p. 9, l. 250 to 265 (Sect. 3.4); p. 15, l. 466 to 476; Fig. 3a, p. 24 |
| Quotation | "This can be diminished by powdering samples and using depth-integrated suspended sediment samples to average out sorting effects during transport (Butler et al., 2019)." |
| Concern | Grain-size effects, preferred orientation and peak overlap concern step 3.4, and immediate export concerns the forward model of Sect. 3.1; a reader of Sect. 3 does not see them. Fig. 3a shows a pump sampler; whether the Gornergletscher samples are depth-integrated, and how rock powders and fine suspended sediment were brought to comparable grain size, is not stated, nor whether the catchment meets the no-storage condition. Are the pump samples point samples, and if so, how are sorting effects handled? |
| Suggestion | Repeat the grain-size, orientation and storage limitations in Sect. 3.1 and 3.4, and state there the sampling device, whether samples are depth-integrated, and the grain size of source and detrital powders. |
| Status | verified (placement); assumption (sampling type), asked as a question |
| Severity | moderate |
| Source | SD |

**GB-21 The data availability statement covers only "the inversion tests" and names none of the natural XRD, zircon, sample or processing data.**

| Field | Content |
|---|---|
| Check | P12 |
| Location | p. 16, l. 490; p. 9, l. 251 to 253 and l. 257; p. 13, l. 391 to 398; p. 13, l. 406 to p. 14, l. 408; p. 14, l. 413, l. 423 to 425, l. 437 to 438; p. 17, l. 522 to 523 |
| Quotation | "The data and codes used for the inversion tests in the study are available at https://doi.org/10.5281/zenodo.17120374"; "following the methodology described in (Belotti, 2021)" |
| Concern | The DOI resolves (Zenodo record 17120374, v1.0.0, 15 September 2025, CC BY 4.0, one zip file of 49.3 MB). Sect. 4 separates synthetic tests (4.1) from natural data tests (4.2), and the statement is worded for "the inversion tests". Not named: raw diffractograms of source and detrital samples, zircon U-Pb ages (described only in an unpublished master's thesis), sample metadata (number, coordinates, dates, device), the 2θ windows, and figure scripts. The repository README lists folders for raw XRD, RRUFF files and raw zircon data, so part of this is probably archived, but the manuscript does not tell the reader, and the archive listing could not be opened. None of these data concern persons. |
| Suggestion | Rewrite the statement at l. 490 to list each dataset (source XRD, detrital XRD, zircon ages, sample locations and dates, 2θ windows, figure scripts) with its location in the archive, and state that the zircon data are archived, since Belotti (2021) is unpublished. |
| Status | verified (wording, missing items, DOI reachable); inferred (archive contents, read from the README) |
| Severity | moderate |
| Source | S2 |

**GB-22 Several minerals in Fig. 11 have identical fingerprints in all seven lithologies, so the 21 tracers are not 21 independent mineral concentrations.**

| Field | Content |
|---|---|
| Check | P3 |
| Location | Fig. 11, p. 32, rows Anorthite and Pyroxene, Annite, Muscovite and Phlogopite, Ankerite and Dolomite; p. 9, l. 259 to 261; p. 13, l. 393 to 398; p. 16, l. 475 to 476 |
| Quotation | "By extracting the relative peak areas within diagnostic 2θ windows for each of the 21 target minerals, we obtained the mineral concentrations characterizing each lithological unit (Figure 11)." |
| Concern | Bar lengths measured on the 300 dpi page image (full width 244 px = 1.0, plus or minus 0.004), in caption order of the columns: Anorthite and Pyroxene both 0, 0.143, 1.000, 0.381, 0.996, 0.029, 0.426; Annite and Phlogopite both 0, 0.541, 0.307, 0.566, 0.213, 0.660, 0.541, Muscovite the same except 0.176 in the metabasites; Ankerite and Dolomite equal within 0.009. Albite and Paragonite (largest difference 0.029) and Antigorite and Chrysotile (0.090) are close. Identical rows mean that the diagnostic windows of these minerals coincide, so plagioclase and pyroxene, or three micas, cannot be told apart. The effective number of distinct tracers is at most 17 of 21, which bears on the tracer-count test (Fig. 9, l. 360 to 362) and on the averaging claim of l. 475 to 476. Major, because it changes the information content behind every natural result. |
| Suggestion | List the 2θ windows of the 21 minerals in Sect. 3.4, state which minerals share windows, merge identical tracers or show that they differ, and repeat the inversions of Sect. 4.2 with the merged set or state the number of independent tracers. |
| Status | verified (bar lengths measured) |
| Severity | major |
| Source | AB |

**GB-23 The XRD source fingerprints in Fig. 15 and Fig. 16 are not the column-normalised values of Fig. 11; they differ by a lithology-specific factor of up to 5.**

| Field | Content |
|---|---|
| Check | P3 |
| Location | p. 9, l. 260 to 263; Fig. 11, p. 32; Fig. 15 source fingerprints, p. 36; Fig. 16 source fingerprints, p. 37 |
| Quotation | "At the end, these are normalized within each sample by dividing by the maximum observed peak area, yielding relative mineral concentrations on a scale from 0 to 1 (Figure 3D and 3E)." |
| Concern | Fig. 11 is consistent with l. 261: the largest bar of each column measures 0.996 to 1.000. If Fig. 15 were built from Fig. 11, each stacked segment would equal the Fig. 11 value divided by the row sum. Measured shares differ by up to 0.215 (Chrysotile in the serpentinites: 0.64 against 0.42 from Fig. 11). The deviations follow one factor per lithology relative to the Furgg series: 0.37 (Stockhorn, Tuftgrat, Gornergrat; 14 minerals), 0.28 (metabasites; 10 minerals), 1.49 (Monte Rosa gneiss; 7 minerals), 0.80 (ZSF sediments), 1.05 (Monte Rosa granite); between gneiss and metabasites 1.49 divided by 0.28 gives 5.3. Fig. 15 is therefore built from values not normalised by the sample maximum. Only one of the two figures can show the matrix A that entered the inversion. |
| Suggestion | State in Sect. 3.4 and in the captions of Fig. 11 and 15 which normalisation each figure shows and which was used for A and for d in Fig. 13, 15 and 16. |
| Status | verified (shares and factors measured); inferred (that Fig. 15 uses non-normalised peak areas) |
| Severity | moderate |
| Source | AB |

**GB-24 The samples used are not identified, their selection from a multi-year record is not explained, and it is unclear whether zircon and XRD were measured on one sample or on two.**

| Field | Content |
|---|---|
| Check | P2, P34, P38 |
| Location | p. 9, l. 267 to 268; p. 13, l. 406 to p. 14, l. 407; p. 14, l. 413, l. 420 to 421, l. 423 to 424, l. 437 to 438 |
| Quotation | "applied to the same detrital sample"; "the detrital sample collected on June 28, 2019, at 13:30"; "We then applied the same nonlinear inversion technique to the XRD-derived dataset acquired from a detrital sample taken at the same date and time." |
| Concern | The site is chosen for its multi-year suspended sediment record, but Sect. 4.2.2 uses one sample of 28 June 2019, 13:30, and Sect. 4.2.1 uses "multiple" samples without number, dates or discharge. No sample has an identifier, and source sampling dates are not given. Sect. 4.2.2 first speaks of "the same detrital sample", then of a sample "taken at the same date and time"; the sampling site of the 28 June sample is not stated either. If two samples or a split were analysed, differences between Fig. 14 and Fig. 15 also contain sample-to-sample variability. Is it one physical sample, split for both analyses, or two? |
| Suggestion | Add in Sect. 4 a table of all samples with identifier, date, time, location, discharge if available and analyses (XRD, zircon); state the selection rule; state at l. 420 and l. 437 whether one or two samples were analysed. |
| Status | verified (wordings, absences); assumption (that two physical samples may be involved), asked as a question |
| Severity | moderate |
| Source | SD, S2, S3 |

**GB-25 Three red-orange legend colours of Fig. 4 and Fig. 12 are indistinguishable, and the subcatchment in Fig. 12 is shown only by saturation.**

| Field | Content |
|---|---|
| Check | P3 |
| Location | Fig. 4 legend, p. 25; Fig. 12 legend and map, p. 33; referenced p. 9, l. 268 and p. 14, l. 412 |
| Quotation | "Lithology and outcrops in the Gorner-Grenz confluence subcatchment." |
| Concern | Median legend colours: Stockhorn unit #ff7333, its outcrops #fd3333, Monte Rosa gneiss outcrops #ff5933; sums of RGB differences 26 and 40, within the criterion of 40 for the same colour, so these classes cannot be told apart on the map. The subcatchment in Fig. 12 has no boundary line and no legend entry for the faded area; the inset of Fig. 13 draws it as a dashed line. |
| Suggestion | Choose clearly different colours for the three entries in Fig. 4 and 12, and draw the subcatchment boundary in Fig. 12 with a legend entry. |
| Status | verified |
| Severity | minor |
| Source | AB |

**GB-26 Several captions only list the panels and do not say how to read the figure; Fig. 11 has no value axis.**

| Field | Content |
|---|---|
| Check | P29 |
| Location | captions of Fig. 4 (p. 25), Fig. 11 (p. 32), Fig. 14 to 16 (p. 35 to 37); Fig. 11 bars |
| Quotation | "Figure 4. Study area: location, land cover and geology."; "Figure 11. XRD-based mineralogical fingerprints of the different source areas of the Gorner-gletscher catchment." |
| Concern | The caption of Fig. 4 does not explain the insets (glacier outline, ELA, land cover), the difference between inferred geology and outcrops, or the sources given in small italic text. Fig. 11 has no x axis, scale or column headers; the column order is given only in the caption. The captions of Fig. 14 to 16 name the panels but not the normalisation of the stacked bars, the sample used or the parameters. |
| Suggestion | Extend the captions of Fig. 4, 11 and 14 to 16 by one or two sentences on what is shown and how it is read, and add a value axis (0 to 1) and column headers to Fig. 11. |
| Status | verified |
| Severity | minor |
| Source | AB |

**GB-27 The spatial inputs (inferred geological map, outcrops, land cover, glacier outline, ELA) are credited only inside Fig. 4, are missing from the reference list and are not covered by the data statement.**

| Field | Content |
|---|---|
| Check | P12 |
| Location | p. 9, l. 270 to 272; p. 6, l. 167; p. 11, l. 327 to 334; p. 16, l. 490; Fig. 4 credit block, p. 25; Fig. 7, p. 28; Fig. 12, p. 33 |
| Quotation | "In ice-covered regions, where direct geological mapping is not possible, we infer the lithology based on regional geological knowledge." |
| Concern | The geological map is the spatial basis of matrix A ("the spatial distribution of the source areas (geological map)", l. 167). Its subglacial part is the authors' interpretation (l. 270 to 272), informed by a personal communication named in the Fig. 4 credits. Those credits name SwissTopo 2018 and GeoCover, neither of which is in the reference list (p. 17 to 21, searched); glacier outline and ELA have no source. Scenario 1 uses further modified maps (Fig. 7). The data statement mentions none of these maps; of the four Fig. 4 sources only Steck et al. (2015) is traceable. |
| Suggestion | Add SwissTopo (product, version) and GeoCover as references, give the sources of glacier outline and ELA, describe the inferred subglacial geology as an author-produced dataset, and list the final and modified maps in the statement at l. 490. |
| Status | verified (credits on the page image, absence from the reference list and from l. 490) |
| Severity | moderate |
| Source | S2 |

**GB-28 The seven lithological units carry different names in the text, the maps, the fingerprint figures and the zircon section.**

| Field | Content |
|---|---|
| Check | P38 |
| Location | p. 10, l. 274 to 277 and l. 299; p. 14, l. 411 to 414 and l. 431 to 434; Fig. 4 and 12 legends; Fig. 5j, 15, 16 legends; Fig. 11 caption; Fig. 13 labels |
| Quotation | "Penninic Mesozoic sedimentary units (Bündnerschiefer)"; "Zermatt Saas-Fee sediments"; "the Monte Rosa garnet-gneiss (MR g-g) unit" |
| Concern | The sedimentary unit appears once as Bündnerschiefer (l. 274 to 275) and eight times as Zermatt Saas-Fee sediments or ZSF sediments; only the Fig. 4 legend links the two. The Monte Rosa non-granite unit appears as "Monte Rosa (garnet gneiss and micaschist)", "Monte Rosa (gneiss, micaschist)", "MR gneiss, mica" and "MR g-g", while the text introduces one Monte Rosa nappe (l. 275 to 276). The Stockhorn unit appears in four forms. ZSF is used at l. 414 and defined at l. 431. The unit count is consistent (seven), so the objects are the same, but at l. 433 a fingerprint is transferred to "MR g-g", a label that appears in no figure. |
| Suggestion | Introduce the seven units once after l. 279 with full name and abbreviation (for example in a short table), state that the Bündnerschiefer are the ZSF sediments unit and that the Monte Rosa nappe is split into two map units, and use these names in all figures and in l. 431 to 434. |
| Status | verified |
| Severity | minor |
| Source | S2 |

**GB-29 The agreement of the XRD fingerprints with known lithology is asserted without a comparison, and several fingerprints differ from the mineralogy the manuscript itself gives for the units.**

| Field | Content |
|---|---|
| Check | P3, P31 |
| Location | Fig. 11, p. 32; Fig. 4 legend, p. 25; p. 10, l. 274 to 279; p. 13, l. 399 to 401 |
| Quotation | "The mineralogical fingerprints derived from processed and binned XRD data align well with established knowledge of the lithology in the Gorner Glacier catchment (Bearth, 1953; Steck et al., 2015), supporting the 1) the robustness of the cleaning and binning approach, and 2) the validity of the input data for the inversion method." |
| Concern | No expected composition and no criterion of agreement are given. Measured bar values set against the manuscript's own unit descriptions: Monte Rosa gneiss and micaschist (garnet, sillimanite, biotite, andesine, muscovite, albite in the Fig. 4 legend) has Almandine 0.037, Albite 0.029, Anorthite 0.029, but Tremolite 0.504; ZSF sediments, "calcareous mica schists and quartzites" (l. 275), have Dolomite and Ankerite 0.020 but Antigorite 0.520 and Chrysotile 0.496, the serpentine minerals named for the serpentinites (l. 274); Monte Rosa granite has Tremolite 0.893; Stockhorn, Tuftgrat, Gornergrat, "dominated by amphibolite-bearing garnet-mica schists" (l. 276 to 277), has Anorthite and Pyroxene 1.000 and Almandine 0.086. The comparison rests on the manuscript's descriptions only; whether these values are mineralogically implausible is a question for the authors. The sentence is used as evidence for the processing chain and the input data, hence major. |
| Suggestion | Add to Sect. 4.2 a table that sets the expected main minerals per unit (Bearth, 1953; Steck et al., 2015) against the fingerprint values of Fig. 11, discuss the deviations named above, or add a quantitative check (for instance Rietveld or reference-mixture quantification on a subset of source samples). |
| Status | verified (bar values, absence of a comparison); inferred (deviation from the unit descriptions) |
| Severity | major |
| Source | AB, SD |

#### Minor corrections

| ID | Location | Quotation | Replacement | Source |
|---|---|---|---|---|
| KK-07 | p. 5, l. 146 to 149; p. 6, l. 166 to 167; p. 9, l. 251 to 262; p. 10 to 11, l. 289 to 319 | "(Figure 1B)", "(Figure 5A)", "(Figure 6C)" and similar | "(Figure 1b)", "(Figure 5a)", "(Figure 6c)" and similar, matching the lower-case panel letters in figures and captions | AB |
| KK-08 | p. 6, l. 174 | "given the observed detrital data and a prior knowledge" | "given the observed detrital data and prior knowledge" | S4 |
| KK-09 | p. 6, l. 175 (eq. 5), confirmed on page image 6 | "following Bayes’ theorem:" followed by eq. 5, which has no sign between the posterior and the likelihood | insert the proportionality or equality sign after the posterior | ZF |
| KK-10 | p. 6, l. 181 | "Which, in an approximately Gaussian setting, becomes Tarantola (2005):" | "which, in an approximately Gaussian setting, becomes (Tarantola, 2005):" | S4 |
| KK-11 | p. 8, l. 236 | "data have improved our knowledge considerately relative to the prior" | "data have improved our knowledge considerably relative to the prior" | S4 |
| KK-12 | p. 8, l. 240 to 241 | "our a posteriori erosion rate map" with "a posteriori erosion" in italics | italics on "a posteriori" only | S4 |
| KK-13 | p. 9, l. 244; p. 12, l. 370 | "the user-defined maximal allowed number of iterations"; "the maximal amount of non-linear iterations" | "the user-defined maximum number of iterations"; "the maximum number of non-linear iterations" | S4 |
| KK-14 | p. 9, l. 245 | "weighed by the model covariance" | "weighted by the model covariance" | S4 |
| KK-15 | p. 9, l. 251 to 252 | "in-situ source samples are collected from every lithological unit across the study area (Figure 3A and 3B)" | "(Figure 3B)", since Fig. 3a shows detrital sampling with the pump sampler | AB |
| KK-16 | Fig. 3, panel (c), legend, p. 24 | "quarz pattern alignment" | "quartz pattern alignment" | S2, AB |
| KK-17 | p. 9, l. 257 | "selected from RRUFF database reference spectra" | "selected from the RRUFF database reference spectra" | S4 |
| KK-18 | p. 9, l. 267; p. 9, l. 272; p. 10, l. 282; p. 13, l. 392 and l. 400; p. 15, l. 463; Acknowledgements, p. 16 | "Gorner-gletscher catchment"; "Gornergletscher catchment"; "Gorner Glacier catchment"; "Gorner gletscher catchment" | one form throughout, for example "Gornergletscher catchment" | S2, S3, S4 |
| KK-19 | Fig. 4 legend, p. 25, and Fig. 12 legend, p. 33 | "GornergratPermo-Mesozoic"; "calcarious mica schist"; "biotite schits"; "epidotamphibolites"; "garnetamphibolites"; "caclcite-zoisite amphibolites"; "silimanite-biotite gneiss" | "Gornergrat Permo-Mesozoic"; "calcareous mica schist"; "biotite schists"; "epidote amphibolites"; "garnet amphibolites"; "calcite-zoisite amphibolites"; "sillimanite-biotite gneiss" | S2, AB |
| KK-20 | p. 9, l. 273 to p. 10, l. 274; p. 10, l. 299; p. 12, l. 340; p. 14, l. 411, 414, 431, 432; Fig. 12 caption | "Zermatt- Saas Fee"; "Zermatt Saas-Fee"; "Zermatt-Saas-Fee"; "Zermatt - Saas Fee" | "Zermatt-Saas Fee (ZSF)" at the first occurrence, "ZSF" thereafter | S2, S4, AB |
| KK-21 | Fig. 11 caption, p. 32 | "Gorner-gletscher catchment"; "Stockhorn-Turftgrat-Gornergrat"; "ZSF ophiolites (metabasites, ecologites)" | "Gornergletscher catchment"; "Stockhorn, Tuftgrat, Gornergrat"; "ZSF ophiolites (metabasites, eclogites)" | S2, AB |

#### Verification log

| ID | Check | Checked | Values | Result |
|---|---|---|---|---|
| PP-07 | P12 | Every data source of Sect. 3 and of the study area part of Sect. 4, plus the inputs of Sect. 4.2, against the statement at l. 490; no appendix exists | Synthetic maps, fingerprints and data: covered by "inversion tests"; code: covered; source and detrital diffractograms, zircon ages, sample metadata, 2θ windows, figure scripts: not named (GB-21); maps, outcrops, land cover, glacier outline, ELA: not named (GB-27); sediment export and multi-year datasets: not named (GB-14); RRUFF: public, cited as Lafuente et al. (2015). DOI resolves to Zenodo record 17120374, v1.0.0, 15 September 2025, CC BY 4.0, one file of 49.3 MB; URL complete on the page image. No data concern persons. Limits disclosed: inferred subglacial geology (l. 270 to 272), missing zircon data (l. 430 to 434) | no further finding |
| PP-08 | P29, P3 | Inventory of all figures with page, type, caption opening and text references | 16 figures on p. 22 to 37: schemas Fig. 1 to 3; map Fig. 4; result panels Fig. 5 to 10 (raster); fingerprint bars Fig. 11; map Fig. 12; KDE ridges Fig. 13; maps and stacked bars Fig. 14 to 16 (13, 21 and 34 columns). No graphical abstract, no tables, no appendix figures | basis for GB-11, GB-22, GB-23, GB-25, GB-26 and the figure findings of Segment 3 |
| PP-09 | P4, P3, P22 | Numbering and targets of sections, figures, panels and equations | Figures 1 to 16 without gap or duplicate; first references in numerical order at l. 146, 166, 251, 268, 289, 314, 334, 347, 356, 371, 398, 412, 414, 429, 439, 445; panels Fig. 1A to 1D, 2A to 2C, 3A to 3E, 5A to 5K, 6C to 6G exist; equations 1 to 22 continuous, references "eq. 1-4", "eq. 7", "eq. 11" to "eq. 16" resolve; subsections continuous; no tables or appendices referenced. Exceptions: duplicate introduction (GB-03), Fig. 3A at l. 251 (KK-15), Fig. 6G versus 6G (GB-35) | no further finding |
| PP-10 | P7 | Whether the described method applied to all reported data | One XRD processing version; one modification, the gradient normalisation of steepest descent (l. 312), which precedes all reported steepest descent results ("In initial experiments"). Collection dates are missing except 28 June 2019, so the share of data per version cannot be computed (GB-24) | no finding |
| PP-11 | P3 | Fig. 3 and Fig. 11 against the normalisation of l. 257 to 262 | Fig. 3d: 11 windows and 11 concentration bars; Fig. 11 column maxima 0.996, 1.000, 1.000, 1.000, 0.996, 1.000, 1.000, consistent with normalisation by the sample maximum | no finding beyond GB-23 |
| PP-12 | P3 | Catchment width from each scale bar | Fig. 4: 110 px per km, width 13.18 km, height 7.89 km, area 73.7 km2; Fig. 12: 13.13 km; Fig. 14: 13.32 km; Fig. 15: 13.38 km; Fig. 16: 13.43 km; spread 2.3 %, within reading accuracy of the shortest bar plus edge effects | no finding |
| PP-13 | P27 | Downstream effect of untested components | Inferred subglacial geology (disclosed) enters A of every natural run; its effect is tested in scenario 1 with 3 maps (summed error about 197, 193 and 275); maximum normalisation enters every A and d (GB-12); hatching enters the reading of Fig. 14 to 16 (GB-17) | no separate finding |
| PP-14 | P19 | Provenance class named for each core statement | Synthetic data labelled as synthetic throughout Sect. 4.1; inferred geology disclosed; zircon method rests on an unpublished master's thesis, named as such; core results resting on model-generated data: 4 of 6 result subsections (66.7 %), labelled | no finding |
| PP-15 | P38 | Identifiers of minerals, units, hyperparameters, methods and metrics across text and figures | Tracers: 21 in the text, 21 row labels in Fig. 11, 21 axis labels in Fig. 15, sets identical except Chrysolite and Chrysotile (GB-44); count 21 also at l. 358, 397 and Fig. 9. Pixel size 1200 m divided by 4 and 3000 m divided by 10 both 300 m. Hyperparameter names in Fig. 10 match l. 367 to 371 and eqs. 8, 9, 17. SD and QN defined at l. 210 to 211, JS at l. 345. Seven units in Fig. 11, 13 and 15, plus the glacier as map class | no further finding |
| PP-16 | P11 | Test matrix announced (l. 280 to 285, l. 323, l. 367 to 370) against reported results | Schemes QN and SD reported; three degradation scenarios reported (Fig. 7 to 9); five hyperparameters in Fig. 10 and l. 372 to 389; natural aims 1 to 3 reported in l. 399 to 401, Sect. 4.2.1 and 4.2.2; normalised uncertainty given for all three natural runs (0.87, 0.82, 0.86), JS distance for two, maximum erosion rate for zircon only (GB-51, GB-52). Limits disclosed: zircon gaps and substitution (l. 430 to 434) | no further finding |
| PP-17 | P3 | Which units lie within the subcatchment, Fig. 12 against the inset of Fig. 13 | Within the saturated area and the dashed boundary: Stockhorn, Tuftgrat, Gornergrat, Furgg series, Monte Rosa granite with outcrops, the tip of Monte Rosa gneiss, small outcrop patches; no ZSF sediments, consistent with l. 411 to 412. Status inferred: maps without grid | no finding |

### Segment 3: Results of the validation (p. 10 to 15; Fig. 5 to 10, 13 to 16)

#### Substantive findings

**GB-30 The synthetic validation uses the same forward model, apparently noise-free data and a prior equal to the mean of the true map, so it measures self-consistency rather than accuracy.**

| Field | Content |
|---|---|
| Check | P9 |
| Location | p. 10, l. 288 to 295; p. 11, l. 324 to 326; p. 12, l. 372 to p. 13, l. 376; p. 16, l. 482 to 483; Fig. 10, row 1, p. 31 |
| Quotation | "we generate synthetic detrital data using the forward model applied to a “true” erosion rate map"; "A longer smoothing distance effectively constrains the posterior closer to the prior (set here as the average true erosion rate) resulting in a reduced difference between posterior and true values," |
| Concern | The forward-inverse design of Sect. 4.1 is clearly laid out. Three features favour the result. (1) Data are generated with the same forward operator (eq. 3) and, in Sect. 4.1.1, 4.1.2 and 4.1.4, the same geological map as the inversion; no noise addition is described, although a data standard deviation is used. (2) The prior equals the mean of the true map, so every pull toward the prior is a pull toward the truth; the manuscript states this effect for L (l. 374 to 375), and in Fig. 10, row 1, the summed error falls from about 257 to about 76 at L = 3000 m, 61.5 % below the baseline of 197.4 (Python, values read from the figure). (3) One true map with one hotspot is tested. Under these conditions agreement between posterior and truth does not show that the inversion recovers unknown patterns. Major, because Sect. 4.1 is the validation the conclusions rest on. |
| Suggestion | In Sect. 4.1 add noise at the level of measured XRD replicate scatter, set the prior from information available in a real application (for instance the catchment mean from sediment export), use at least three true maps (hotspot at a unit boundary, in a small unit, two hotspots), and where possible a perturbed A; report the summed error for each and revise l. 482 to 483 to the scope then shown. |
| Status | verified (design features in the text; no noise addition described); inferred (that the design favours the result; values read from the figure) |
| Severity | major |
| Source | SD |

**GB-31 The colour scale of Fig. 5b ends at 3.0, while Fig. 5c implies posterior values of about 4.3 to 5.2 at the hotspot; the claimed close match in magnitude cannot be checked from the figure.**

| Field | Content |
|---|---|
| Check | P3 |
| Location | p. 10, l. 296 to 297; Fig. 5, panels (a), (b), (c), p. 26 |
| Quotation | "The quasi-Newton (QN) approach generates a posterior erosion rate map that closely matches the true erosion pattern, both in spatial distribution and magnitude (Figure 5B)." |
| Concern | The maps of panels (a) to (c) are aligned (offsets 698 and 1397 px on the 300 dpi page). At the strongest blue pixel of panel (c) the colour of (a) reads 2.81 and that of (b) 3.02, the top of its scale; panel (c) shows its darkest blue there, between minus 1.5 and the lower end of its scale at minus 2.36. With "Difference (true - posterior)" this implies a posterior of 4.3 to 5.2, above the range of panel (b), whose colour bar has no extension mark. At a red control point the panels agree (2.35 minus 1.14 = 1.21 against about 1.1 in panel c). If the reading holds, the posterior overshoots the true maximum of about 3.0 by 40 % to 70 % on the western flank of the hotspot and the hotspot is displaced westwards. Colour reading over a hillshade is approximate, hence inferred. Could the authors state the maxima of the posterior map and the difference map? |
| Suggestion | Use a common colour range for panels (a) and (b) of Fig. 5 and 6 that covers both maxima or mark clipped values, and give peak values and location shift in Sect. 4.1.1, l. 296 to 298. |
| Status | verified (colour bar limits, absence of an extension mark); inferred (values read from colours) |
| Severity | major |
| Source | AB |

**GB-32 Abbreviations in the figures are not resolved in captions or legends.**

| Field | Content |
|---|---|
| Check | P29 |
| Location | Fig. 5, panel (j) legend, p. 26; Fig. 15 and 16 legends; Fig. 11 caption; Fig. 13; Fig. 14 caption; Fig. 4 inset legend; Fig. 8 and 9 titles and axes; Fig. 10, fifth row |
| Quotation | "S.,T.,G."; "MR gneiss, mica"; "ELA estimation"; "Avg. JS distance"; "using Zr fingerprint data" |
| Concern | ZSF, MR, S.,T.,G., ELA, JS and Zr are not expanded in any caption or legend; ZSF is expanded in the text (l. 431), JS at l. 345, ELA nowhere. The iteration symbol in Fig. 10 is typeset as code text while the caption uses math. |
| Suggestion | Expand the abbreviations in the captions of Fig. 4, 5, 8, 11, 13, 14, 15 and 16 (for example "ZSF: Zermatt-Saas Fee; MR: Monte Rosa; S.,T.,G.: Stockhorn, Tuftgrat, Gornergrat; ELA: equilibrium line altitude; JS: Jensen-Shannon") and typeset the iteration symbol consistently. |
| Status | verified |
| Severity | minor |
| Source | AB |

**GB-33 The resolution diagonal maps show values between 0.5 and 1.0 almost everywhere, which the resolution operator of eq. 21 cannot reach with 13 to 34 data.**

| Field | Content |
|---|---|
| Check | P3 |
| Location | Fig. 5, panel (d), p. 26; Fig. 6, panel (d), p. 27; Fig. 14 to 16, "Resolution diagonal", p. 35 to 37; p. 8, l. 230 to 236; p. 10, l. 299 to 300; p. 14, l. 436; p. 16, l. 483 to 484 |
| Quotation | "So R is close to the identity operator I if we have perfectly resolved the “exact model”."; "Where the diagonal of R is close to 1, data have improved our knowledge considerately relative to the prior." |
| Concern | In the linearised Gaussian framework of eq. 20 the resolution operator has rank at most the number of data m, so its trace is at most m. With 21 XRD tracers, 13 zircon age bins (Fig. 14, 13 columns counted) and 34 combined tracers (Fig. 16), and with about 819 pixels (catchment area 73.7 km2 from the Fig. 4 scale bar, pixel size 300 m from l. 294), the mean diagonal element is at most 21/819 = 0.026, 13/819 = 0.016 and 34/819 = 0.042. The colour bars run from 0.90 (Fig. 5d), 0.88 (Fig. 6d), 0.5 (Fig. 14), 0.80 (Fig. 15) and 0.5 (Fig. 16) to 1.0, and almost all pixels carry the top colour; a diagonal of at least 0.90 on 819 pixels implies a trace of at least 737, 35 times 21. The panels also disagree with Fig. 5e and 5f, which imply a variance reduction of 11 % to 78 %. In Fig. 14 the text calls the resolution "low" (l. 436) while the map is at the top of its scale. Possible readings: the panels show 1 minus the diagonal, another operator, or an inverted scale; each changes the reading at l. 299 to 300 and l. 436 and the claim at l. 483 to 484. |
| Suggestion | State after eq. 21 the formula used to compute R, report its trace for the runs of Fig. 5 and 14 to 16, redraw the resolution panels with that quantity and a caption that says how to read it, and revise l. 299 to 300 and l. 436. |
| Status | verified (colour bar ranges, column counts, scale bar, area measured); inferred (rank bound and pixel count, derived from eqs. 20 and 21, l. 294 and Fig. 4) |
| Severity | major |
| Source | AB |

**GB-34 Axis labels, exponents and colour-bar labels are missing in Fig. 6, and units are missing for erosion rates and errors in Fig. 5 to 10.**

| Field | Content |
|---|---|
| Check | P29 |
| Location | Fig. 6, panels (g), (h), (i), p. 27; Fig. 5, panels (a), (b), (c), (e), (g), p. 26; Fig. 7 left and middle scatterplots, p. 28; Fig. 8 and 9 left scatterplots; Fig. 10 first column, p. 31 |
| Quotation | "(i) Trade-off data- vs model-misfit" |
| Concern | In Fig. 6 the x axes of (g) and (h) have no label (Fig. 5 shows "Iteration"), the x axis of (i) has neither the label "Data misfit" nor the exponent (Fig. 5i has "1e8"), and the colour bar of (i) has no label. The colour bars of the erosion maps in Fig. 5 and 6 and of the posterior covariance carry no unit; the error axes of Fig. 5 to 10 carry no unit, although l. 352 quotes errors in mm/yr; the x axis "Area difference" of Fig. 7 has no unit. Fig. 14 to 16 give "(mm/y)", so the units are known. |
| Suggestion | Add the missing labels, exponent and colour-bar label to Fig. 6g to 6i, and units (mm/y for erosion rates and errors, m2 for area difference) to all axes and colour bars named above. |
| Status | verified |
| Severity | minor |
| Source | AB |

**GB-35 The oscillations of the steepest descent posterior covariance "visible after 125 iterations" are not visible in Fig. 6h, and the cited comparison refers to the same panel twice.**

| Field | Content |
|---|---|
| Check | P3, P4 |
| Location | p. 11, l. 316 to 317; Fig. 6, panels (g) and (h), p. 27 |
| Quotation | "This limited sensitivity to strong gradients also leads to oscillations in the posterior covariance, visible after 125 iterations, as the Jacobian fluctuates between iterations (Figure 6G versus Figure 6G)." |
| Concern | "Figure 6G versus Figure 6G" compares a panel with itself, and panel (g) shows the summed absolute difference, not the covariance. Tracing the upper edge of the marker band in Fig. 6h column by column on the 300 dpi page, the curve rises to a kink at iteration 138.3 plus or minus 0.4 and then decreases monotonically from 0.7426 to 0.7423 at iteration 200; after the kink there are 14 one-pixel steps down and 3 steps up of 1 px, within the reading uncertainty. No oscillation is resolved. |
| Suggestion | In l. 317 name the intended panels (presumably Fig. 6h versus Fig. 5h), and either show the oscillation (zoomed inset of Fig. 6h after iteration 125, or the change between iterations) or describe the curve as a kink near iteration 138 followed by a slow decrease. |
| Status | verified (self-reference, panel content, curve traced); assumption (intended target) |
| Severity | moderate |
| Source | AB, S4 |

**GB-36 Fig. 5g and Fig. 6g show the steepest descent run ending closer to the true map than the quasi-Newton run, contrary to the stated reason for adopting quasi-Newton.**

| Field | Content |
|---|---|
| Check | P3 |
| Location | p. 11, l. 320 to 321 and l. 314 to 316; p. 10, l. 305 to 306; Fig. 5, panel (g), p. 26; Fig. 6, panel (g), p. 27 |
| Quotation | "Based on these findings, we adopt the Quasi-Newton (QN) approach for all subsequent tests, as it provides a more stable and accurate reconstruction of the erosion rate patterns." |
| Concern | Calibrated on the tick marks, the quasi-Newton curve reaches its minimum summed absolute difference of 197.1 plus or minus 0.3 at iteration 24.8 and rises to 201.0 at iteration 100; the steepest descent curve ends at 192.9 plus or minus 0.4 after 200 iterations, 8.1 (4.0 %) closer to the true map. The text says steepest descent needs more iterations "to converge to a posterior result as close to the true erosion rate map as the QN posterior" (l. 315 to 316), which the figures support as to speed, but "more accurate" is not shown. The rise after iteration 25 also differs from "initially decreases rapidly, then plateaus" (l. 305 to 306). The comparison of the two schemes is a stated aim (l. 4 to 5), hence major. |
| Suggestion | Restate the choice in l. 320 to 321 by the criteria the figures show (speed, stability), give final and minimum errors of both runs, and describe the rise after iteration 25 in l. 305 to 306. |
| Status | verified (measured) |
| Severity | major |
| Source | AB |

**GB-37 In the blended-fingerprint scenario 20 cases are tested and one is said not to be plotted, but Fig. 8 shows 14 points.**

| Field | Content |
|---|---|
| Check | P3, P23, P34 |
| Location | p. 12, l. 347 to 349 and l. 353; Fig. 8, caption and left and middle panels, p. 29 |
| Quotation | "In total, 20 values between the highly blended and the original synthetic fingerprints are tested"; "Note that the most blended example did not have a stable solution and is therefore not plotted." |
| Concern | Three instances counted 14 markers in both panels, at JS distances of 0.249, 0.272, 0.338, 0.359, 0.440, 0.461, 0.481, 0.501, 0.521, 0.541, 0.561, 0.581, 0.602 and 0.624. 20 tested minus 1 stated as not plotted gives 19 expected; 5 are unaccounted for, 6 of 20 (30 %) absent (Python). Twenty values in equal steps from 0.225 to 0.624 would lie about 0.021 apart; the gaps between 0.272 and 0.338 and between 0.359 and 0.440 match the missing runs. "In many of these cases, the inversion fails to converge" (l. 353) suggests the reason but does not count. The plotted errors are a selection by outcome and understate the failure rate at low JS. Overlapping markers are not visible at the marker size. |
| Suggestion | In Sect. 4.1.3 and the caption of Fig. 8 give the number of runs plotted (14) and not plotted (6) with their JS distances and the convergence criterion, and mark the failed runs in the plot. |
| Status | verified (counts and positions); inferred (missing grid values, from equal spacing) |
| Severity | moderate |
| Source | S3, AB, SD |

**GB-38 The threshold of "errors exceeding 700 mm/yr" below JS 0.44 does not match the absolute errors plotted in Fig. 8, which are sums over pixels.**

| Field | Content |
|---|---|
| Check | P3, P20, P22 |
| Location | p. 12, l. 351 to 353; Fig. 8, left scatterplot, p. 29; Fig. 5g, 7, 9, 10, first column; p. 10, l. 294 |
| Quotation | "As the JS distance decreases below 0.55, both absolute error and posterior uncertainty rise sharply, with errors exceeding 700 mm/yr for JS" |
| Concern | All error axes show the sum of absolute differences over the pixels, which is not a rate and depends on the number of pixels; the manuscript does not state that number, and the pixel size must be derived from L = 1200 m = 4 pixel sizes. Calibrated values in Fig. 8: JS 0.249: 46,800; 0.272: 677,000; 0.338: 5,300; 0.359: 322,000; 0.461: 700; 0.501: 8,400; 0.521: 3,500; 0.541: 18,900; 0.561 to 0.624: 0 within plus or minus 1,400. If 700 refers to the plotted sum, values above 700 also occur at JS 0.501 to 0.541, so 0.44 is not the threshold; if 700,000 was meant (the top tick), no run exceeds it. The rise of the uncertainty below 0.55 is confirmed (0.842 at 0.541 against 0.747 at 0.561). Is 700 a typing error, or a per-pixel mean in other units? |
| Suggestion | Define the error metric in Sect. 3.3 or 4.1.1 (sum or mean, unit), give number and size of pixels, and correct value and threshold in l. 352 to 353 to what Fig. 8 shows; add the unit to the y axis. |
| Status | verified (axis labels, measured values); assumption (cause of the discrepancy), asked as a question |
| Severity | moderate |
| Source | S3, AB |

**GB-39 The x axis of the left and middle scatterplots of Fig. 9 is labelled as JS distance but shows the number of tracers.**

| Field | Content |
|---|---|
| Check | P3 |
| Location | Fig. 9, left and middle scatterplots, p. 30; referenced p. 12, l. 356 to 357 |
| Quotation | "Avg. JS distance between lithologies" |
| Concern | The 21 markers of the left scatterplot lie at the integers 1 to 21 (plus or minus 0.04), the tracer counts tested (l. 357 to 358), coloured by tracer number. An average JS distance cannot exceed 1. The label was presumably copied from Fig. 8. |
| Suggestion | Relabel the x axes of the left and middle scatterplots of Fig. 9 as "Number of tracer minerals". |
| Status | verified |
| Severity | minor |
| Source | AB, S3, SD |

**GB-40 The ranking of the three degradation scenarios compares perturbations of non-commensurate size, and the map-uncertainty trend rests on three maps.**

| Field | Content |
|---|---|
| Check | P6, P20, P21 |
| Location | p. 12, l. 363 to 365; p. 11, l. 332 to 339; p. 12, l. 340 to 342; Fig. 7 to 9, left panels, p. 28 to 30; p. 15, l. 456 to 460 |
| Quotation | "To summarize, among the three tested scenarios, the strongest impact on the posterior solution arises from reduced fingerprint distinctiveness. Geological map uncertainty follows as the second most influential factor."; "We observe that the greater the mismatch between the geological map used in the inversion and the one used to generate the synthetic data, the larger the discrepancy between the posterior and true erosion rate maps." |
| Concern | The scenarios vary quantities on different scales (area mismatch in m2, JS distance, number of tracers), and the size of each perturbation is set by the authors. The largest summed errors are about 275 (Steck et al. map, plus 39.6 % over the baseline of about 197), about 348 (one tracer, plus 76.6 %) and about 677,000 (JS about 0.27) (Python, values from the figures). Over the tested ranges, reducing tracers produced a larger maximum error than map uncertainty; the stated order holds only under the proviso "provided that the most informative ones are retained". Scenario 1 has three points, and the minimally changed map (about 193) lies below the identical map (about 197); the authors disclose this exception (l. 338 to 340), and instance AB therefore raised no finding on the non-monotonic error; the trend sentence of l. 337 to 338 and the ranking, which the Discussion reuses (l. 456 to 460), do not follow from three maps with one exception. Major, because the ranking is a stated result that grounds the recommendations of Sect. 5. |
| Suggestion | Express each scenario on a common, normalised perturbation scale (for instance the change in A or in JS distance each causes) or restrict the ranking to stated ranges; test more than three maps or replace l. 337 to 338 by a description of the three cases. |
| Status | verified (three maps, ranking sentences); inferred (values read from the figures, percentages computed) |
| Severity | major |
| Source | S3, SD |

**GB-41 Fig. 10 marks hyperparameter values that differ from those used in all runs, and the over-smoothing beyond 3000 m stated in the text lies outside the tested sweep, whose lowest error is at 3000 m.**

| Field | Content |
|---|---|
| Check | P2, P3, P5, P11, P29 |
| Location | p. 12, l. 372 to p. 13, l. 375; p. 3, l. 70 and p. 5, l. 137; p. 10, l. 294 to 295; p. 11, l. 324 to 326; p. 14, l. 426 to 428; Fig. 10, rows 1 to 5, third column annotations, p. 31 |
| Quotation | "However, beyond approximately 10 times the pixel size (3000 m), the solution becomes overly smooth, causing the posterior to deviate from the true erosion rates."; "Through forward-inverse testing, we optimize the hyper-parameters and demonstrate the convergence of the inversion." |
| Concern | The sweeps follow a clear one-at-a-time plan. The 20 markers of row 1 run from L = 205 to 3001 m (plus or minus 8 m); the summed error falls monotonically from 256.7 to 76.4 at the last point and the uncertainty from about 0.99 to 0.27. No L above 3000 m is plotted, so the stated deterioration is not shown, and l. 375 itself reports a reduced difference at longer L. The annotations (confirmed on the page image) mark L = 3000 m, σm = 6.2 and σd = 0.003 mm/y, while every reported run uses L = 1200 m, σm = 3 and σd = 0.01 mm/y; only µ = 0.1 and 25 iterations agree, and the caption does not say what the marked values are. At L = 1200 m the error is about 199 (interpolated between 206.5 at 1087 m and 194.9 at 1234 m), 2.6 times that at 3000 m; why 1200 m was kept if the aim is to optimise is not said. Major, because the parameter choice enters all later results. |
| Suggestion | State in the caption of Fig. 10 what the marked points are; extend the L sweep beyond 3000 m or delete l. 373 to 374; give in Sect. 4.1.4 the rule by which L = 1200 m, σm = 3 and σd = 0.01 mm/y were chosen and why the marked values were not adopted. |
| Status | verified (labels, parameter values, measured markers) |
| Severity | major |
| Source | S3, AB, SD |

**GB-42 The described effects of the data standard deviation and of the iteration limit are not present in Fig. 10, rows 3 and 5.**

| Field | Content |
|---|---|
| Check | P2, P3, P21 |
| Location | p. 13, l. 380 to 384 and l. 387 to 389; Fig. 10, rows 3 and 5, p. 31; Fig. 7 and 9 right scatterplots; p. 11, l. 324 to 326 |
| Quotation | "Very low data standard deviation values lead to large differences between the posterior and true erosion rate maps, likely due to overfitting or unstable gradients."; "Only when the maximum number of non-linear steps is reduced below 25 does the posterior fail to converge to the true erosion map." |
| Concern | Row 3, left panel, carries the offset "+1.974e2" (confirmed on the page image); calibrated, the summed error runs from 197.4197 at the lowest values to 197.4431 at σd = 0.891 mm/y, a range of 0.012 %, rising monotonically, with no large difference at low σd, no minimum and no plateau. Model misfit spans 1.5614 to 1.5623 (0.06 %), uncertainty 0.74015 to 0.74040. The linear x axis puts 0.01 mm/y within 4 px of the origin. Row 5, left: 5 iterations give 268.8, 15 give 200.7, 25 give 197.5 and 45 to 195 give 199.5 to 200.8 (plus or minus 0.3), so 15 iterations are as close to the truth as 195; only 5 deviate. Instances S3 and SD had read the row-5 statement as consistent because the lowest point deviates; the calibrated values of instance AB and a check of the page image show that the next point, at 15 iterations, already lies at about 200, so the decision is for the finding. The marked 25-iteration point of row 5 also lies at a model misfit of 1.77, against 1.56 for the reference run in Fig. 7 and 9, so this sweep used a different setting, which the text does not state. Major, because the sentences report results of the sensitivity analysis that justify the parameters of all later runs. |
| Suggestion | Rewrite l. 380 to 384 and l. 387 to 388 to what rows 3 and 5 show (or state that the inversion is insensitive to σd over the tested range), plot σd on a logarithmic axis without offset, and state the fixed parameters of each sweep and why the 25-iteration run of row 5 differs from the reference run. |
| Status | verified (offset, measured values, page image) |
| Severity | major |
| Source | S3, AB |

**GB-43 Calcite is not among the 21 tracer minerals, although the manuscript describes calcareous and marble-bearing units, including the unit that decides the known-mixture test.**

| Field | Content |
|---|---|
| Check | P9 |
| Location | p. 13, l. 393 to 396; p. 10, l. 275 and l. 278; Fig. 4 legend, p. 25; Fig. 11, p. 32; Fig. 15 axis labels, p. 36; p. 14, l. 411 to 412 |
| Quotation | "we focused on a set of 21 minerals expected to be characteristic of the main lithologies in the catchment, including: Tremolite, Talc, Quartz, Pyroxene, Phlogopite, Paragonite, Omphacite, Muscovite, Microcline, Magnesite, Glaucophane, Fayalite, Dolomite, Diopside, Chrysolite, Antigorite, Anorthite, Annite, Ankerite, Almandine, and Albite." |
| Concern | The Bündnerschiefer (ZSF sediments) "consist mainly of calcareous mica schists and quartzites" (l. 275), the Furgg series contains marbles (l. 278), and the Fig. 4 legend lists calcareous mica schist and calcite-zoisite amphibolites. The tracer list and the axes of Fig. 11 and 15 contain dolomite, ankerite and magnesite, but no calcite (checked on page images 13 and 36). The ZSF sediments are the only unit absent from the subcatchment (l. 411 to 412), so their distinction carries the test of Sect. 4.2.1. Was calcite excluded deliberately, for instance because of dissolution during transport or window overlap? |
| Suggestion | State in Sect. 4.2, l. 393 to 396, how the 21 minerals were chosen and why calcite is not among them, or add calcite and report its effect on the fingerprints and on Fig. 13. |
| Status | verified (absence in list and figure axes); inferred (relevance for the ZSF distinction) |
| Severity | moderate |
| Source | ZF |

**GB-44 The tracer list names "Chrysolite", while all figures and the lithology description name "Chrysotile".**

| Field | Content |
|---|---|
| Check | P38 |
| Location | p. 13, l. 395; p. 10, l. 274; Fig. 11, row label, p. 32; Fig. 15, axis label, p. 36; Fig. 16, p. 37 |
| Quotation | "Dolomite, Diopside, Chrysolite, Antigorite, Anorthite"; "serpentinites (predominantly antigorite and chrysotile)" |
| Concern | The text list (l. 393 to 396) and the row labels of Fig. 11 contain 21 minerals each; a set comparison in Python gives identical sets except "Chrysolite" in the text and "Chrysotile" in Fig. 11; Fig. 15 has the same 21 labels as Fig. 11. Chrysotile is the serpentine mineral named for the serpentinites at l. 274. If l. 395 is a typo the correction is trivial; if a chrysolite reference spectrum (an olivine name) was used to select the 2θ window (l. 257), the fingerprint row differs in substance. Which RRUFF reference was used? |
| Suggestion | Confirm the reference used for this tracer and use one name at l. 395 and in Fig. 11, 15 and 16. |
| Status | verified (both spellings on the page images, set comparison); assumption (that the olivine spectrum may have been used), asked as a question |
| Severity | moderate |
| Source | S2, S3, S4, AB, SD |

**GB-45 The natural known-mixture test can fail only through one small unit, gives no quantitative criterion, and Fig. 13 does not separate the absent unit from present ones.**

| Field | Content |
|---|---|
| Check | P3, P10, P11, P20 |
| Location | p. 14, l. 410 to 418; p. 13, l. 404 to 406; p. 10, l. 299 to 300; p. 9, l. 262 to 263; Fig. 12 caption, p. 33; Fig. 13, p. 34 |
| Quotation | "Only the Zermatt - Saas Fee sediment unit does not have outcrops in the Gorner-Grenz subcatchment (Steck et al., 2015), as shown in Figure 12."; "Some spillover occurs from adjacent lithologies, but the overall pattern confirms that the inversion respects geological boundaries when the XRD fingerprints provide sufficiently distinct signals." |
| Concern | Using a subcatchment as natural analogue of a known mixture is a sound idea. As designed, the test has one possible failure, erosion in the ZSF sediments, one of 7 units and one the manuscript names as small and poorly resolved (l. 299 to 300), so a posterior near zero can also follow from low resolution; the causes are not separated. Because A depends only on lithology, pixels of one unit inside and outside the subcatchment are indistinguishable by the data. The number of samples and inversions is given only as "multiple" (l. 413), and "close to zero" and "some spillover" have no numbers. Measured on the calibrated x axis of Fig. 13: ZSF sediments (absent) mode 0.007 mm/y, 66 % of the curve area at or below 0.25 mm/y; Furgg series (present, Fig. 12) mode 0.007 mm/y, 71 %; Monte Rosa granite (present) 0.016 mm/y, 21 %; Stockhorn, Tuftgrat, Gornergrat (present) 0.007 mm/y, 13 %. The absent unit and the present Furgg series are indistinguishable. Major, because Sect. 4.2.1 is one of three stated validation aims (l. 283 to 284). |
| Suggestion | In Sect. 4.2.1 give the number and dates of samples and inversions; report per unit the share of the total predicted flux with its spread across inversions against its outcrop area inside the subcatchment, with a criterion fixed in advance; give the resolution of the ZSF sediment pixels; restrict l. 415 to 418 to what one absent unit can show; and add a laboratory known-mixture experiment or a second subcatchment that excludes a large, distinct unit. |
| Status | verified (design statements, measured densities); inferred (that low resolution may explain the result) |
| Severity | major |
| Source | S3, AB, SD |

**GB-46 Fig. 13 gives no density scale for the six upper ridges and no number of samples or inversions, although the caption asks the reader to compare peak heights.**

| Field | Content |
|---|---|
| Check | P29 |
| Location | Fig. 13 and caption, p. 34; p. 14, l. 413 |
| Quotation | "a taller peak indicates greater consistency across inversions." |
| Concern | The upper panel has the axis label "Density" but no ticks or values; only the lower panel (ZSF sediments) has a scale (0 to 2). The six ridges overlap, so their heights cannot be compared with each other or with the lower panel. Each KDE pools all pixels of a unit over all inversions, so a tall peak also reflects a narrow spread across pixels within one inversion, not only consistency across inversions. |
| Suggestion | Give the number of samples and inversions in the caption of Fig. 13 and in l. 413, add a common density scale or normalise each ridge and say so, and reword the last sentence of the caption to what the pooled KDE measures. |
| Status | verified |
| Severity | moderate |
| Source | AB |

**GB-47 The natural-data inversions use "a prior equal to the average true erosion rate", which does not exist for natural data, so the prior of Fig. 13 to 16 is unknown.**

| Field | Content |
|---|---|
| Check | P11, P25 |
| Location | p. 14, l. 426 to 428; p. 14, l. 437 to 438; p. 15, l. 444 to 445; p. 10, l. 284 to 285 |
| Quotation | "a data standard deviation of 0.01 mm/y, a prior equal to the average true erosion rate, and a step size µ of 0.1." |
| Concern | The parameter list of Sect. 4.2.2 repeats the wording of the synthetic tests (l. 295, l. 325 to 326), and the XRD and combined runs use "the same inversion parameters" (l. 444 to 445). For the Gornergletscher no true map exists, so the prior used is not stated; the prior of the Gorner-Grenz runs (Sect. 4.2.1) is not given at all. Fig. 10 shows that the posterior is pulled toward the prior (l. 374 to 375), and the posterior maxima differ by three orders of magnitude between zircon (above 8000 mm/y, l. 435) and XRD (colour scale to about 8 mm/y, Fig. 15). The aim in l. 285 includes "accuracy", which cannot be assessed without a reference map. Is the prior derived from the sediment export divided by catchment area (GB-14), or from another source? Major, because the prior sets the level of every natural result. |
| Suggestion | State in Sect. 4.2.1 and 4.2.2 the prior value in mm/y and its derivation, confirm that the three runs of Sect. 4.2.2 share it, and replace "accuracy" in l. 285 by the quantity actually assessed. |
| Status | verified (wording, absence of the value); assumption (what was used), asked as a question |
| Severity | major |
| Source | SD, S3 |

**GB-48 Fig. 14 has no lithology legend, and the legends of Fig. 15 and Fig. 16 are partly overlapped or clipped.**

| Field | Content |
|---|---|
| Check | P29 |
| Location | Fig. 14, "Geology" panel and source fingerprints, p. 35; Fig. 15 legend, p. 36; Fig. 16 legend, p. 37; referenced p. 14, l. 429 |
| Quotation | "the geological map and the source fingerprints." |
| Concern | In Fig. 14 neither the geology panel nor the stacked bars have a legend, so the colours can only be assigned by comparison with Fig. 15. In Fig. 15 the label "ZSF serpentinites" is overlapped by the swatch of "ZSF metabasites"; in Fig. 16 the top line of the legend is cut at its upper edge. |
| Suggestion | Add the lithology legend of Fig. 15 to Fig. 14 and reposition the legends of Fig. 15 and 16 so that all labels are complete. |
| Status | verified |
| Severity | minor |
| Source | AB |

**GB-49 Fig. 14 and Fig. 16 show the substituted Monte Rosa garnet-gneiss zircon fingerprint without marking it.**

| Field | Content |
|---|---|
| Check | P37 |
| Location | p. 14, l. 432 to 434; Fig. 14 caption and fingerprint panel, p. 35; Fig. 16 caption, p. 37 |
| Quotation | "To compensate for the lack of age data for the MR g-g unit, we assigned the MR g-g unit the same zircon-age fingerprint as the Monte Rosa granite unit." |
| Concern | The substitution is disclosed in the text. The captions present all fingerprints as data, and in the Fig. 14 bars the two Monte Rosa units carry identical shares in each age bin, which a reader of the figure alone takes as measured. |
| Suggestion | Add to the captions of Fig. 14 and 16 that the Monte Rosa garnet-gneiss carries the zircon fingerprint of the Monte Rosa granite (no age data), and mark the bars. |
| Status | verified |
| Severity | minor |
| Source | SD |

**GB-50 The zircon-only hotspot above 8000 mm/y lies in the serpentinites, whose zircon fingerprint is nearly zero, so its agreement with the XRD solution may reflect the fingerprint rather than erosion.**

| Field | Content |
|---|---|
| Check | P21 |
| Location | p. 14, l. 439 to 440; p. 14, l. 432 to 433 and l. 435; Fig. 14, erosion map, geology panel and fingerprint bars, p. 35; p. 6, l. 153 (eq. 3) |
| Quotation | "While both datasets indicate sediment source activation in the serpentinite-rich region in the southwest"; "Moreover, the Zermatt-Saas Fee ophiolites (serpentinites) contain only very low concentrations of zircons." |
| Concern | On page image 35 the hotspot of the zircon map sits in the south-west, where the geology panel shows the ZSF serpentinites; in the stacked zircon bars the serpentinite colour appears only as lines of one pixel (at most 0.002 of a column, instance AB). In the forward model d = A times exp(ε) (eq. 3), a unit whose column of A is near zero can contribute to the predicted detrital signal only through very large erosion rates, which matches the extreme values of l. 435. The south-western activation of the zircon run may then express the near-zero fingerprint, and l. 439 to 440 counts it as agreement between the two tracer sets. Is the zircon hotspot driven by the small serpentinite entries of A, and how does it change if the serpentinite column is removed or floored? Major, because the agreement statement is part of the comparison that answers aim 3 (l. 284 to 285). |
| Suggestion | In Sect. 4.2.2 discuss the mechanism of the zircon hotspot, report the zircon run with the serpentinite entries treated explicitly, and restate l. 439 to 440 accordingly. |
| Status | verified (hotspot location, near-zero fingerprint, text l. 432 to 433); inferred (mechanism, from eq. 3) |
| Severity | major |
| Source | ZF |

**GB-51 Adding zircon data to the XRD data raises the normalised posterior uncertainty and the peak erosion rate, while introduction and Discussion state that the combination further stabilises and improves the solution.**

| Field | Content |
|---|---|
| Check | P2, P3, P6, P15, P21 |
| Location | p. 15, l. 446 to 449; p. 14, l. 436; p. 15, l. 441 to 442; p. 15, l. 461 to 463; p. 3, l. 72 to 73 and p. 5, l. 139 to 140; p. 10, l. 284 to 285; Fig. 14 to 16, "Total normalised posterior uncertainty" and colour bars, p. 35 to 37 |
| Quotation | "Adding XRD data to the zircon dataset stabilizes the inversion and improves the posterior solution. The normalized posterior uncertainty decreases slightly to 0.86 (from 0.87 in the zircon-only case)"; "Furthermore, combining XRD data with other fingerprint data such as zircon data, proves to further stabilize and improve the posterior solution, as shown with natural data for the Gorner gletscher catchment." |
| Concern | The three natural runs are reported with one common metric, which allows a direct comparison: 0.87 (zircon, l. 436), 0.82 (XRD, l. 442), 0.86 (combined, l. 447), confirmed as printed totals in Fig. 14 to 16. Against zircon the combination lowers the value by 0.01 (1.1 %); against XRD it raises it by 0.04 (4.9 %) (Python). The colour bars end at about 8,620 (Fig. 14), 8.3 to 8.5 (Fig. 15) and 12.06 mm/y (Fig. 16), so the peak rises by 43 % against XRD alone. Sect. 4.2.2 compares the combination only with zircon, which the numbers support; l. 461 to 463 turns the direction ("combining XRD data with other fingerprint data") and l. 72 to 73 and l. 139 to 140 claim improved "stability and sharpness", which are neither defined nor measured. The colour scale of the resolution maps changes between Fig. 15 and 16, and the comparison rests on one sample. Two readings: adding XRD rescues an unstable zircon inversion, which the results support; or zircon adds value to XRD, which they contradict on the only reported metric. Major, because this is the answer to aim 3. |
| Suggestion | In Sect. 4.2.2 report combined against XRD-only with the same metrics (normalised uncertainty, resolution, JS distance, maximum rate), define stability (for instance spread across bootstrap resamples or several samples), restate l. 72 to 73, l. 139 to 140, l. 284 to 285 and l. 461 to 463 so that each claimed improvement names its reference case and metric, and replace "proves" by "suggests" for a single sample. |
| Status | verified (values in text and figures); inferred (differences and percentages, computed) |
| Severity | major |
| Source | S3, S4, AB, SD |

**GB-52 The JS distances of the natural datasets have no stated set of units and pairs, are missing for the XRD-only case, and are compared across fingerprint vectors of different length and with synthetic thresholds.**

| Field | Content |
|---|---|
| Check | P9, P11, P20, P21 |
| Location | p. 15, l. 447 to 448; p. 14, l. 430 to 434; p. 12, l. 346 to 347 and l. 351 to 353; Fig. 8 "Unblended", p. 29; Fig. 14 and 16 source fingerprints, p. 35 and 37 |
| Quotation | "the average Jensen-Shannon distance between source fingerprints increases from 0.48 to 0.57, indicating improved distinguishability." |
| Concern | The disclosure of the zircon gaps is useful; its consequence for the JS average is not drawn: with 7 units there are 21 pairs, without the unit lacking zircon 15 (Python); the copied Monte Rosa fingerprint makes one pair identical (JS = 0), so 5 independent zircon fingerprints remain. The text does not say over which units and pairs 0.48 was averaged, nor how a unit without zircon enters the combined vector. The XRD-only value is not given, although XRD is the method validated. JS distances between vectors of 13, 21 and 34 bins are not directly comparable with each other or with the synthetic thresholds 0.55 and 0.44 obtained with 21 tracers. The synthetic fingerprints have 0.624 ("Unblended", Fig. 8), the zircon set 0.48 lies below the onset of degradation, and it remains open whether the natural XRD fingerprints lie in the range where Sect. 4.1 shows recovery. Major, because the transfer of the synthetic results to the natural case rests on this comparison. |
| Suggestion | In Sect. 4.2.2 give the JS distance of the XRD-only fingerprints (Fig. 11) and place it in Fig. 8; state the units and pairs entering each average and the handling of missing and copied fingerprints; compare JS only within one tracer set or explain the comparability; repeat at least the test of Sect. 4.1.1 with the natural fingerprints of Fig. 11. |
| Status | verified (gaps, values, bin counts); inferred (pair counts, transfer gap) |
| Severity | major |
| Source | S3, SD |

#### Minor corrections

| ID | Location | Quotation | Replacement | Source |
|---|---|---|---|---|
| KK-22 | p. 10, l. 299 | "(such as Zermatt Saas-Fee sediments and Furgg series (Figure 4) and Figure 5J)" | "(such as the Zermatt-Saas Fee sediments and the Furgg series; Figures 4 and 5J)" | S4 |
| KK-23 | p. 10, l. 303 | "normalised posterior variance" | "normalized posterior variance", and one spelling variety throughout (also "optimisation" l. 307 against "optimize" l. 70, "characterise" l. 250 against "characterizing" l. 398) | S4 |
| KK-24 | p. 11, l. 319 | "(Figure 6D, 6E and 6F )" | "(Figure 6D, 6E and 6F)" | S4 |
| KK-25 | Fig. 7, title of the left map, p. 28 | "Originial geology (same as forward)" | "Original geology (same as forward)" | S3, AB |
| KK-26 | p. 12, l. 343 to 344 | "by approaching each lithology’s mineral concentration to its mean across all lithologies" | "by moving each lithology's mineral concentration towards its mean across all lithologies" | S4 |
| KK-27 | p. 12, l. 351 | "The more resemblant the source fingerprints are" | "The more similar the source fingerprints are" | S4 |
| KK-28 | p. 12, l. 352 | "errors exceeding 700 mm/yr" | unit "mm/y" as elsewhere (14 times "mm/y", once "mm/yr"); value per GB-38 | S2, S3, S4 |
| KK-29 | Fig. 9, colour bar label and y-axis label of the left scatterplot, p. 30 | "Number of tracrs"; a second summation sign below the y-axis label | "Number of tracers"; the label without the second summation sign | S2, S3, AB |
| KK-30 | Fig. 10, row 1, x-axis label and colour bar label, p. 31 | "Smooting distance (m)" | "Smoothing distance (m)" | S2, AB |
| KK-31 | p. 13, l. 384, confirmed on page image 13 | "approximately 10-2 mm/y" | "approximately 10^−2 mm/y" with superscript exponent, as in l. 388 | S3, S4 |
| KK-32 | p. 13, l. 400 | "supporting the 1) the robustness of the cleaning" | "supporting 1) the robustness of the cleaning" | S3, S4 |
| KK-33 | Fig. 14, 15 and 16, legend of the erosion map, p. 35 to 37 | "Low-con dence area" | "Low-confidence area" | AB |

#### Verification log

| ID | Check | Checked | Values | Result |
|---|---|---|---|---|
| PP-18 | P3, P29 | Fig. 5 settings and consistency of panels (e) and (f) | Panels (g) to (i) run to 100 iterations, as l. 293; panel (k) has 21 tracers A to U; panel (e) colour bar 2 to 8 with prior variance 9 (l. 294), panel (f) 0.4 to 0.9; the square roots of 2/9 and 8/9 (0.47 and 0.94) agree with (f) under eq. 22; posterior covariance lowest at the hotspot, as l. 301; pixel grid consistent with 300 m pixels | no finding beyond GB-31 and GB-33 |
| PP-19 | P1 | Derived numbers in Sect. 4.1 and 4.2 | Pixel size 1200/4 = 300 m and 3000/10 = 300 m (l. 294, l. 373); 21 minerals listed, matching l. 393 and l. 397 and 21 bars in Fig. 15; 21 synthetic tracers in Fig. 5k, matching l. 358; 13 zircon bins (Fig. 14), 13 plus 21 = 34 combined (Fig. 16); zircon to XRD minus 0.05, zircon to combined minus 0.01, consistent with "decreases slightly" (l. 447); Fig. 5g summed error from about 345 to about 200 (42.0 %, read) | no finding |
| PP-20 | P2, P3 | Reference run (25 iterations, L = 1200 m, σm = 3, σd = 0.01 mm/y, µ = 0.1, full tracer set) across text and figures | Parameter sets identical in l. 294 to 295, l. 324 to 326, l. 426 to 428; summed error 198.2 (Fig. 7), 197.5 (Fig. 9, 7 to 21 tracers), about 197.4 (Fig. 10 row 3); normalised uncertainty 0.7402 (Fig. 7), 0.740 (Fig. 8 unblended, Fig. 9 "All"), 0.74015 (Fig. 10 row 3); model misfit 1.562 (Fig. 7), about 1.56 (Fig. 9), 1.557 (Fig. 10 row 4). Exception: Fig. 10 row 5 (GB-42) | no further finding |
| PP-21 | P30 | Order of correction and measurement | The only reported error is the instability of steepest descent (l. 312 to 313); quasi-Newton, used for all later tests (l. 320 to 321), is unaffected | no finding |
| PP-22 | P3 | Fig. 7 against l. 332 to 342 | Area difference 0.0005, 0.693 and 1.143 times 10^7 m2; summed error 198.2, 193.5 and 274.9; uncertainty 0.7402, 0.7376, 0.7460; data misfit 3.254, 3.490, 3.687 times 10^6; model misfit 1.562, 1.922, 2.461; data and model misfit rise with area difference (l. 341 to 342). Limits disclosed: the smaller error of the minimally changed map (l. 338 to 340) | no finding beyond GB-40 |
| PP-23 | P3 | Fig. 8 labels and uncertainty threshold | "Medium" at JS 0.440 to 0.441, "Unblended" at 0.624, no marker at 0.225 (omitted example); uncertainty 0.880 to 0.893 below JS 0.36, 0.832 to 0.842 at 0.44 to 0.54, 0.747 at 0.561, 0.740 to 0.741 at 0.581 to 0.624; threshold 0.55 of l. 351 to 352 confirmed for the uncertainty. Limits disclosed: non-convergence (l. 353) | no finding beyond GB-37 and GB-38 |
| PP-24 | P3 | Fig. 9 against l. 355 to 362 | Top row bars 1, 11 and 21; 21 markers; summed error 1 tracer 347.2, 2: 348.4, 3: 293.5, 4: 296.5, 5: 224.1, 6: 205.2, 7 to 21: 197.4 to 197.5, consistent with l. 360 to 361; lower data and model misfit below 7 tracers, as l. 361 to 362 | no finding beyond GB-39 |
| PP-25 | P36 | Approximate statements against the plotted values | "approximately the same posterior solution" with 7 tracers (l. 360) against Fig. 9: about 197 from 7 tracers on, consistent; "approximately 10-2 mm/y" (l. 384) and "below 25" (l. 387) against Fig. 10: see GB-42 | no separate finding |
| PP-26 | P3 | Direction of trends in Fig. 10, rows 1, 2 and 4, against l. 372 to 379 and l. 385 to 386 | Row 1: error 256.7 to 76.4, uncertainty about 0.99 to 0.27, data misfit up from about 3.23 to 3.45 times 10^6, model misfit down from about 26 to 1.4; row 2: error 209.1 at the smallest σm, 197.4 for larger values, high misfits at low σm; row 4: error minimum at µ = 0.1 (about 197), 328.6 at µ = 0.010. Consistent, apart from GB-41 | no further finding |
| PP-27 | P20 | Iteration counts in Fig. 5g and convergence of the tracer scenario | Fig. 5g plateaus after about 20 iterations, consistent with the use of 25 iterations; the statement on 115 iterations (l. 388 to 389) refers to the change in data misfit, which no figure shows numerically, not checkable; scenario 3 consistent with l. 360 to 362. The reading of Fig. 10 row 5 by this check is superseded by GB-42 | no further finding |
| PP-28 | P32 | Statements labelling results as confirmed | "the overall pattern confirms that the inversion respects geological boundaries" (l. 415 to 416) and "align well with established knowledge" (l. 399 to 400): neither rests on a check whose error rate could be estimated; treated as design questions in GB-29 and GB-45; no statement of error freedom found | no further finding |
| PP-29 | P24 | Datings in the text and time axes in the figures | Only dated event: the detrital sample of 28 June 2019, 13:30 (l. 423 to 424, again l. 437 to 438); no figure has a date axis; iteration axes are not time axes | P24 does not apply |
| PP-30 | P23 | Balance of lithological units in the zircon dataset | 7 units; 1 without zircon grains (ZSF metabasites and eclogites); 1 without ages, filled with the Monte Rosa granite fingerprint; 5 independent zircon fingerprints (7 minus 1 minus 1). Limits disclosed: gaps and substitution (l. 430 to 434) | no finding beyond GB-52 |
| PP-31 | P3 | Fig. 14 to 16 against l. 430 to 449 | Printed totals 0.87, 0.82, 0.86 as in l. 436, 442 and 447; Fig. 14 colour bar top 8,620 plus or minus 30 mm/y, consistent with l. 435; 13, 21 and 34 columns; Monte Rosa gneiss and granite have equal shares in each zircon bin, as l. 433 to 434; serpentinite colour only in lines of one pixel, no metabasite colour, consistent with l. 430 to 432 | no finding beyond GB-49 to GB-51 |

### Segment 4: Discussion, conclusions, statements, references (p. 15 to 21)

#### Substantive findings

**GB-53 The novelty claim for a spatially informed approach and a non-linear mixing model conflicts with the cited predecessor and with the manuscript's own forward model.**

| Field | Content |
|---|---|
| Check | P28 |
| Location | p. 15, l. 454 to 455; p. 2, l. 58 to 61 and duplicate p. 4, l. 125 to 128; p. 5, l. 151 to 152 and l. 158 to 159 (eq. 1); p. 6, l. 153 (eq. 3) |
| Quotation | "The novelty of our method lies in the spatially informed approach of this underdetermined inversion problem, and in the incorporation of non-linear mixing model." |
| Concern | The introduction states correctly that the method is "a non-linear adaptation of the inversion framework validated in (De Doncker et al., 2020)" (l. 60 to 61). The abstract of De Doncker et al. (2020), read by instance S1, already converts detrital information "into an erosion rate map starting from the spatial distribution of zircon age signatures" and notes that "other tracers such as mineral content can be used"; the spatially informed, underdetermined inversion is therefore the predecessor's contribution. The mixing itself stays linear: l. 151 to 152 calls the detrital data "a weighted average", and l. 158 to 159 attributes the non-linearity to the log-space parameterisation. A Python check of eq. 3 with a random 5 by 8 matrix confirms that the model is linear in the erosion rates and non-linear only in their logarithm. The contrast with methods that "implicitly rely on a linear mixing scheme" (l. 59) therefore does not hold for the mixing model. |
| Suggestion | Rewrite l. 454 to 455 to name what is new against De Doncker et al. (2020), for example binned XRD peak areas as tracers, a log-space parameterisation that enforces positive rates, and their combination with zircon data; change l. 59 (and l. 126) so that the contrast is with the parameterisation. |
| Status | verified (page images, source abstract read, calculation run) |
| Severity | moderate |
| Source | S1 |

**GB-54 Discussion and conclusions attribute effects of tracer count, number of source areas and sediment storage to the results, which the results do not show or show weaker.**

| Field | Content |
|---|---|
| Check | P15 |
| Location | p. 15, l. 458 and l. 460 to 461; p. 16, l. 484 to 486; results p. 12, l. 355 to 365; p. 15, l. 467 to 468 |
| Quotation | "Including a broad set of tracer minerals further improves model stability and resolution."; "higher number of distinct source areas leads to higher posterior resolution and lower uncertainty."; "Our results suggest that the method is best applied in catchments with minimal sediment storage, multiple mineralogically distinct source areas, and good prior knowledge of the spatial distribution of source areas." |
| Concern | (1) Sect. 4.1.3 found that 7 tracers give "approximately the same posterior solution as with the full tracer set" (l. 360); 14 of 21 tracers (two thirds) can be dropped without loss, so a broad set is not shown to improve stability beyond 7. (2) No test varies the number of source areas; the related observation that small units are resolved worse (l. 299 to 300) concerns unit size. (3) No test involves storage; l. 467 to 468 correctly present it as a model assumption, but l. 484 recasts it as a result. Major, because these sentences state what the study found. |
| Suggestion | In l. 458 state the tested result (at least 7 of the most informative tracers were needed; more did not further improve the solution); delete l. 460 to 461 or add a test that varies the number of source units; in l. 484 to 486 separate tested conditions from model assumptions. |
| Status | verified (wording, absence of the tests); inferred (share 14 of 21) |
| Severity | major |
| Source | S4 |

**GB-55 The study site does not meet the manuscript's own first application condition, and the consequence for the natural results is not drawn.**

| Field | Content |
|---|---|
| Check | P18 |
| Location | p. 15, l. 463 to 466; p. 9, l. 270 to 272; p. 12, l. 363 to 364; Fig. 4, p. 25 |
| Quotation | "Based on these findings, we recommend applying this method in catchments where: a) the spatial distribution of source lithologies is well constrained" |
| Concern | The manuscript discloses that the geology under ice is inferred (l. 270 to 272) and finds map uncertainty to be the second strongest factor in the synthetic tests (summed error 275 against 197.4, plus 39.3 %, Python). The Gornergletscher is largely ice-covered (Fig. 4), so condition a) is not met by the case used for natural validation, and the results of Sect. 4.2 are not qualified for this. |
| Suggestion | In Sect. 4.2 or 5 state the share of the catchment area with inferred geology, and repeat the natural inversions with the alternative map of Steck et al. (2015) already used in scenario 1, reporting how Fig. 13 and 15 change. |
| Status | verified (wording, ice cover in Fig. 4); inferred (non-fulfilment) |
| Severity | moderate |
| Source | SD |

**GB-56 The conclusions recommend the method for zircon U-Pb age data, although the manuscript's own zircon-only inversion was highly unstable.**

| Field | Content |
|---|---|
| Check | P15 |
| Location | p. 16, l. 488 to 489; p. 14, l. 430 to 436; Fig. 14, p. 35 |
| Quotation | "Similarly, the method is not limited to XRD-derived fingerprints and can be applied to other types of tracer data, including zircon U-Pb age distributions or geochemical compositions." |
| Concern | The only zircon application in the manuscript failed: two units had no zircon data, one received a borrowed fingerprint (l. 430 to 434), and the posterior reached more than 8000 mm/y (l. 435), against a synthetic range of about 0 to 3 mm/y (Fig. 5). The manuscript does say why (missing source fingerprints), and De Doncker et al. (2020) is cited for the zircon approach (l. 424 to 425), so the statement may rest on that study; the conclusions do not say so. Geochemical compositions were not tested. Major, because the sentence states a scope of application as a conclusion. |
| Suggestion | Rewrite l. 488 to 489 to say that zircon U-Pb data can be used when all source units yield zircon fingerprints, citing De Doncker et al. (2020), that zircon data alone gave an unstable solution in the Gornergletscher case, and that geochemical tracers are untested. |
| Status | verified |
| Severity | major |
| Source | S4 |

**GB-57 Several reference entries lack the publication details that comparable entries carry.**

| Field | Content |
|---|---|
| Check | P16 |
| Location | p. 17, l. 521 (Bearth, 1953); p. 19, l. 583 (Gjems, 1967); p. 19, l. 599 to 600 (Lafuente et al., 2015); p. 20, l. 612 to 613 (Moore and Reynolds, 1990) |
| Quotation | "Gjems, O.: Studies on clay minerals and clay-mineral formation in soil profiles in Scandinavia, 1967." |
| Concern | Other book and map entries give publisher and place (for example Bish and Post, Tarantola, Menke). Bearth (1953) has no publisher for the atlas sheet, Gjems (1967) has neither series nor publisher and cannot be located, Lafuente et al. (2015) gives a book title without editors or publisher, and Moore and Reynolds (1990) gives a page range for a whole book and the place as "New-York". |
| Suggestion | Complete the four entries on p. 17, 19 and 20 with series, publisher, place and editors, and replace the page range in Moore and Reynolds by the chapter or pages cited. |
| Status | verified |
| Severity | minor |
| Source | S4 |

#### Minor corrections

| ID | Location | Quotation | Replacement | Source |
|---|---|---|---|---|
| KK-34 | p. 15, l. 455 | "and in the incorporation of non-linear mixing model." | "and in the incorporation of a non-linear mixing model." | S4 |
| KK-35 | p. 15, l. 461 to 462 | "combining XRD data with other fingerprint data such as zircon data, proves" | no comma between subject and verb; content per GB-51 | S4 |
| KK-36 | p. 16, l. 491 to 494 | "All authors (FDD, FH, BB, TA)" | "All authors (F.D.D., F.H., B.B., T.A.)", as in the following sentences | S4 |
| KK-37 | p. 17, l. 522 to 523 | "Master’s thesis, University of Lausanne, unpublished master’s thesis, 2021." | "unpublished Master's thesis, University of Lausanne, 2021." | S4 |
| KK-38 | p. 17, l. 526 | "Mineralogical society of America" | "Mineralogical Society of America" | S4 |
| KK-39 | p. 19, l. 578 | "[No title found], Aquatic Sciences, 64" | "Landscape indicators of human impacts to riverine systems, Aquatic Sciences, 64" (title confirmed by instance S4 at experts.illinois.edu) | S4 |

#### Verification log

| ID | Check | Checked | Values | Result |
|---|---|---|---|---|
| PP-32 | P15 | Every sentence of Sect. 5 (l. 451 to 476) and Sect. 6 (l. 478 to 489) against the results | Supported: distinct signatures essential (l. 457 to 458) by l. 351 to 354; delineation crucial (l. 459 to 460) by l. 337 to 342; recommendations a) to c) by scenarios 1 to 3; resolution and covariance as indicators (l. 483 to 484) by Sect. 4.1.1 (but see GB-33); XRD limitations argued from literature and declared; storage stated as assumption at l. 467 to 468. Not supported or overstated: GB-02, GB-51, GB-54, GB-56. Limits disclosed: storage, limited outcrop exposure (l. 460), spillover (l. 414 to 415) | no further finding |
| PP-33 | P26 | Statements of the type "ensures", "prevents", "should help cancel out" | "applying the same sample preparation and analysis protocol to both detrital and source material should help cancel out such effects" (l. 472 to 473): hedged, scope stated, physical equivalence of rock powder and suspended sediment raised in GB-20; "This stabilization prevents divergence" (l. 312 to 313) applies to steepest descent only, not used afterwards | no finding |
| PP-34 | P4 | Citations against the reference list in both directions, short citations against entries | 64 distinct citations and 64 entries, one to one; years identical in all 64 pairs; two-author citations use "and" in all 11 cases; 12 single-author citations; alphabetical order checked by script, no inversion. Exceptions: GB-04, GB-07. DOIs not resolved (optional check) | no further finding |

## Optional checks

| Check | What it needs | Responsible | Run |
|---|---|---|---|
| DOI resolution | one request per reference entry with a DOI | `science-quellenapparat-pruefung` | no |
| Citation style | the name of the style or the style rules of the journal | `science-zitierstil-harvard-ctr` or the journal's style rules | no |
| AI statement against publisher policy | the policy of the target publisher | this review, on request | no |
| Relation to the authors' own previous work | the authors' previous work as files or DOIs | this review, on request | no |
| Journal requirements | the author guidelines of the target journal | this review, on request | no |
| Factual accuracy | access to the sources of each checked statement | `science-faktenbeleg-pruefung`, `geo-frage-belegbasiert-klaeren` | no |

## Limits of this review

- Version reviewed: egusphere-2025-4695.pdf, 37 pages, SHA-256 9c80676054f96ecd6f00f4d2a8b5ba568e03c6949e3856d363ac1c4abb42e7bd.
- The six review instances ran as separate agents; the consolidation re-checked quotations and locations at the printed margin numbers of the page images. On p. 14 the extracted text is shifted by one line from l. 436 on; the locations follow the page image.
- Sources not readable: Das et al. (2023) beyond its abstract; Klages and Hsieh (1975); Torres Astorga et al. (2020); Barker et al. (1997) and Wilson et al. (1993) beyond metadata; Niu et al. (2020) beyond its abstract; the UNESCO page of Walling (2009); the file listing of the Zenodo archive. Haddadchi et al. (2013), Yang et al. (2025) and Fathabadi and Jansen (2022) were not opened. The consolidation did not re-open web sources; literature findings rest on the reading of the instances.
- Discarded findings: 0 of 81 instance findings lacked a mandatory field. 27 instance findings were merged into 17 combined findings; 10 instance minor corrections were absorbed into substantive findings. Of 58 notes outside the checklists, 2 were rejected after checking the manuscript (the preconditioning of eq. 18 is consistent with the stated preconditioning by Cm; the storage caution is attributed and treated as an assumption in GB-54), 4 led to new items with source ZF (GB-16, GB-43, GB-50, KK-09), and 1 was added to GB-15; the others were already covered by instance findings or concern material outside the manuscript.
- Findings with status assumption for at least one partial statement: 8 of 57; findings whose central statement has status assumption: 0 of 57.
- Optional checks run: 0 of 6.
