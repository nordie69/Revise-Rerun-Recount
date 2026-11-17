# Review report: From XRD signal to erosion rate maps

| Field | Value |
|---|---|
| Manuscript | De Doncker, F., Herman, F., Belotti, B. and Adatte, T. (2025) From XRD signal to erosion rate maps, EGUsphere preprint egusphere-2025-4695, https://doi.org/10.5194/egusphere-2025-4695 |
| Checked version | egusphere-2025-4695.pdf, 37 pages, SHA-256 9c80676054f96ecd6f00f4d2a8b5ba568e03c6949e3856d363ac1c4abb42e7bd |
| Date | 2026-10-22 |
| Language | English |
| Review instances | Segments 1 to 4, figures, study design; the six review instances ran as separate agents; no instance omitted |

## Summary

The manuscript is a method-development study. It proposes a Bayesian maximum a posteriori inversion that converts binned X-ray diffraction (XRD) peak-area fingerprints of source lithologies and of detrital suspended sediment into a spatially explicit erosion rate map, with erosion rates cast in log space for positivity, Gaussian model and data covariances, and three posterior metrics (posterior covariance, resolution, normalised posterior uncertainty). Two update schemes, steepest descent and quasi-Newton, are compared. The synthetic forward-inverse tests use one true erosion map with a localised hotspot: a quasi-Newton run of 100 iterations, a steepest descent run, three data-degradation scenarios (three geological maps, 20 levels of fingerprint blending, 1 to 21 tracers) and five hyperparameter sweeps (smoothing distance, model and data standard deviation, step size, iteration cap). The natural application concerns the Gornergletscher catchment (Swiss Alps) with seven lithological units and 21 target minerals: a natural known-mixture analogue with samples from the Gorner-Grenz confluence subcatchment, and a comparison with zircon U-Pb fingerprints for a detrital sample of 28 June 2019. Key numbers: errors and uncertainty rise sharply below an average Jensen-Shannon (JS) distance of 0.55; seven tracers give approximately the same solution as 21; normalised posterior uncertainty 0.87 for zircon, 0.82 for XRD and 0.86 for the combined data, with average JS distance 0.48 for zircon and 0.57 combined.

## Strengths

1. One reference configuration (original map, unblended fingerprints, all 21 tracers, L = 1200 m, σm = 3, σd = 0.01 mm/y, µ = 0.1, 25 iterations) recurs in Figures 7 to 10 with the same summed error of about 197.4 to 197.6 and a normalised uncertainty of about 0.740; the degradation scenarios and the parameter sweeps are thereby anchored to one baseline, and their effects can be read as departures from it (PP-18).
2. Testing against a known true map yields operating conditions that the figures bear out: the posterior uncertainty in Figure 8 jumps from 0.747 to 0.842 between average JS distances of 0.561 and 0.541, and the summed error in Figure 9 stays at 197.4 from 7 to 21 tracers, as the text states (PP-27, PP-28); how far these thresholds hold beyond the single hotspot geometry is not shown (GB-26).
3. The uncertainty maps follow the stated formula: over 159 cells, Figure 5(f) equals the square root of Figure 5(e) divided by σm² = 9 with a median deviation of minus 0.016 and a correlation of 0.984, so the per-pixel normalised uncertainty is computed as Eq. (22) defines it (PP-19).
4. The manuscript discloses its own failures and substitutions where they occur (steepest descent instability and gradient normalisation, non-convergent blended runs, missing zircon data for two units and the copied MR g-g fingerprint), its synthetic test data and code sit in a resolving Zenodo record, and all 64 citation keys match the reference list in both directions; this makes the scope of the synthetic results traceable (PP-22, PP-34, PP-41, PP-45).

## Weaknesses

1. The validation does not test the method independently of its own assumptions: all synthetic tests use one true map, the same forward model, no stated noise and a prior equal to the true mean, and the iteration cap was chosen at the error minimum against that same truth (GB-26, GB-17); the natural known-mixture analogue checks one of seven units with pooled KDEs and no drawn subcatchment boundary (GB-42), and the zircon benchmark is confounded by missing and copied zircon data (GB-45). Suggestion: several truth maps with noise and an independent prior, tuning on held-out truth maps, a laboratory known-mixture test with source powders, and a benchmark restricted to units with both data types.
2. Several headline statements are stronger than the reported results: the combined zircon and XRD inversion is presented as a further improvement although its normalised uncertainty (0.86) exceeds that of XRD alone (0.82) (GB-47), cost and time effectiveness is called validated without any measurement (GB-01), convergence and robustness are stated without the failure conditions the Results report (GB-02), the hotspot magnitude is said to match although the posterior overshoots it (GB-29), quasi-Newton is called more accurate although its error curve ends higher (GB-30), and the novelty claim credits earlier work and linear mixing as new (GB-56). Suggestion: restate each claim to what the numbers show or add the missing measurement.
3. The inversion as described cannot be reproduced and partly contradicts its own assumptions: normalising each sample by its maximum breaks the linear mixing of Eq. (1) (GB-20), σd is assumed and far from the achieved misfit (GB-28), the prior and the export estimate of the natural runs are undefined (GB-44), Eq. (9) and Eq. (19) cannot be implemented as printed (GB-14, GB-15), and the normalised uncertainty has two definitions (GB-16). Suggestion: state the implemented equations, the normalisation, the prior, the export value and the derivation of σd, and add sensitivity runs for prior and σd.
4. Moderate gaps in reporting and in the agreement of text and figures: the laboratory chain and the data statement do not allow a rebuild (GB-18, GB-62), descriptions of Figures 6, 8 and 10 are not what the plotted points show (GB-31, GB-34, GB-35, GB-38, GB-39, GB-53), and unit and mineral names change between text and figures (GB-22, GB-40). Suggestion: align the text with the measured figure values, list omitted runs, and add a methods table and an item-by-item data statement.

## Findings by segment

### Segment 1: Abstract, Introduction (p. 1 to 5)

#### Substantive findings

**GB-01 Time and cost effectiveness is stated as validated, but no time or cost is measured or reported.**

| Field | Content |
|---|---|
| Check | P33, P11, P15 |
| Location | p. 1, l. 3 to 4; p. 2, l. 40 to 41; p. 3, l. 74 to 75; twins p. 4, l. 107 to 108 and p. 5, l. 141 to 142 |
| Quotation | "In this study, we validate a time- and cost-effective fingerprinting approach based on X-ray diffraction (XRD) data." (l. 3 to 4); "we investigate the potential of binned XRD data as a cost-effective fingerprinting method" (l. 40 to 41); l. 74 to 75: "To conclude, we show and validate the potential of binned XRD peak-area data as a cost- and time-efficient approach for constructing erosion rate maps." |
| Concern | The motivation that many tracers are "expensive and time-consuming" (l. 35) is attributed to Das et al. (2023) and is a legitimate reason to study XRD. The Abstract and l. 74 to 75 go further and present cost and time effectiveness as validated by this study. A text search finds "cost" only in l. 3, 4, 40 and 74 and in their twins in the duplicated Section 2; no passage in Sections 3 to 6 reports preparation time, instrument time, throughput or cost per sample, neither for XRD nor for the zircon U-Pb dating run on a sample of the same date (l. 423 to 424), and Discussion and Conclusions do not return to the claim. The grade is major because cost and time effectiveness is the first claim of the Abstract and part of the stated aim (l. 40 to 42): if the finding holds, the manuscript cannot show what it announces in l. 3 to 4 and l. 74 to 75. |
| Suggestion | Add to Section 4.2.2 or Section 5 a table of preparation time, instrument time and cost per sample for XRD and for zircon U-Pb dating as used here, and take it up in Section 6; otherwise replace "we validate" (l. 3) and "we show and validate" (l. 74) by wording that cites cost effectiveness as motivation (Das et al., 2023). |
| Status | verified (absence in Sections 3 to 6; text search) |
| Severity | major |
| Source | S3, S4, SD |

**GB-02 Abstract and Conclusions state consistent convergence, robustness and validation without the failure conditions the Results report.**

| Field | Content |
|---|---|
| Check | P2, P6, P15 |
| Location | p. 1, l. 7 to 8; p. 15, l. 451; p. 16, l. 482 to 483 |
| Quotation | "Forward-inverse tests with synthetic data demonstrate consistent convergence of the posterior solution. The application to real-world datasets further validates the practical utility and robustness of the model." (l. 7 to 8); l. 482 to 483: "we show that the true erosion pattern can be reliably recovered, and that the method is robust across a range of parameters" |
| Concern | The Results disclose the non-convergent cases themselves: "In initial experiments, the steepest descent approach proved unstable" (l. 312), "In many of these cases, the inversion fails to converge to a stable posterior solution" (l. 353) and "the most blended example did not have a stable solution and is therefore not plotted" (Figure 8 caption). Error and uncertainty "rise sharply" below an average JS distance of 0.55 (l. 352), the error "increases rapidly" below 7 tracers (l. 361), step sizes below 0.1 prevent convergence (l. 385 to 386), and fewer than 25 iterations fail (l. 387). Across the smoothing sweep the summed error falls from 257.1 to 76.1, a factor of 3.38 (Python, values measured by AB on Figure 10, row 1), so the result depends strongly on L within the tested range. All synthetic tests use one true map with one hotspot (l. 288 to 289; GB-26), and the natural tests rest on one negative-control unit (GB-42) and one sample date (GB-45). Abstract and Conclusions report convergence, robustness and validation without these conditions, and "a range of parameters" is not specified. |
| Suggestion | In the Abstract (l. 7 to 8) and the Conclusions (l. 482 to 483) name the conditions under which recovery was reliable (average JS distance above about 0.55, at least 7 informative tracers, µ = 0.1, at least 25 iterations, one hotspot geometry) and that L changes the error by a factor of about 3.4 within the tested range; in l. 8 and l. 451 replace "validates" and "validated" by "tests" and "tested". |
| Status | verified (quotations at the page images); inferred (factor from values measured on Figure 10) |
| Severity | moderate |
| Source | S3, S4, SD |

**GB-03 Section 2 "Introduction" repeats Section 1 "Introduction" word for word.**

| Field | Content |
|---|---|
| Check | P4, P16 |
| Location | p. 1, l. 9 (heading of Section 1, body to l. 75); p. 3, l. 76 (heading of Section 2, body to l. 142) |
| Quotation | "1 Introduction" (l. 9) and "2 Introduction" (l. 76), both followed by "As rivers face increasingly frequent and intense hydrological events, understanding the spatio-temporal dynamics of suspended" |
| Concern | The 66 text lines under heading 1 and the 66 text lines under heading 2 are identical: 1153 words each, difflib ratio 1.0 (Python); the page images p. 1 and p. 3 confirm both headings. One section carries two numbers, and every citation of the Introduction appears twice. Locations in this review give the Section 1 lines; each has a twin 67 lines later. |
| Suggestion | Delete Section 2 (l. 76 to 142) and renumber Methods, Validation, Discussion and Conclusions as Sections 2 to 5. |
| Status | verified |
| Severity | minor |
| Source | S4 |

**GB-04 The citation "E., 2009" and its entry "E., W. D." carry an initial in place of the surname.**

| Field | Content |
|---|---|
| Check | P4 |
| Location | p. 1, l. 11 to 12; p. 18, l. 567 to 568; twin p. 3, l. 78 to 79 |
| Quotation | "(Gergel et al., 2002; Allan, 2004; E., 2009; Hamel et al., 2015)"; "E., W. D.: The Impact of global change on erosion and sediment transport by rivers, UNESCO 2009, ISBN 9789231041358, oCLC:" |
| Concern | The author field consists of initials only, so the entry sorts under "E" and the in-text citation names no author; "oCLC" is set in lower case on the page image. The UNESCO report of 2009 with this title is attributed to D. E. Walling, which suggests that the name was parsed with the second initial as surname; the report itself could not be read. |
| Suggestion | After checking the title page, change the citation in l. 11 to 12 to "Walling, 2009" and the entry in l. 567 to 568 to "Walling, D. E.: The impact of global change on erosion and sediment transport by rivers, UNESCO, Paris, ISBN 9789231041358, 2009", move it to its alphabetical position and write "OCLC". |
| Status | verified (malformed author field, page images p. 1 and p. 18); inferred (author identification, report not readable) |
| Severity | minor |
| Source | S4, S1 |

**GB-05 Two of the three citations for sediment traps on dams do not concern sediment traps or dams.**

| Field | Content |
|---|---|
| Check | P13 |
| Location | p. 1, l. 18 to 19; twin p. 3, l. 85 to 86 |
| Quotation | "Direct measurements, such as sediment traps installed on dams, provide valuable information on sediment fluxes but do not reveal the origin of the transported material (Wilson et al., 1993; Barker et al., 1997; Davis and Fox, 2009)." |
| Concern | The sentence is plausible as general knowledge; what is missing is a source that documents it. Barker et al. (1997) is "Use of terrestrial photogrammetry for monitoring and measuring bank erosion" (reference list, p. 17), and its abstract (University of Portsmouth research portal, read by S1) mentions neither sediment traps, dams nor sediment flux. Wilson et al. (1993), "Soil erosion in the Falkland Islands: an assessment" (p. 21), is by its title a regional soil erosion assessment; its abstract could not be read. Davis and Fox (2009), a review of sediment fingerprinting, could not be read either. |
| Suggestion | In l. 18 to 19 replace Barker et al. (1997) and Wilson et al. (1993) by a study that reports sediment trapping in reservoirs or at dams, or give the page of Davis and Fox (2009) that supports the sentence. |
| Status | verified (Barker et al.: title in the reference list and abstract); inferred (Wilson et al.: title only; Davis and Fox: not read) |
| Severity | minor |
| Source | S1 |

**GB-06 Four citations in the list of fingerprinting tools do not report the tracer they are cited for; one of them is a theology article.**

| Field | Content |
|---|---|
| Check | P13, P4 |
| Location | p. 1, l. 26; p. 2, l. 28 to 31; p. 19, l. 597 to 598; twins p. 3, l. 93 and p. 4, l. 95 to 98 |
| Quotation | "geochemistry (Olley et al., 1993; Gholami et al., 2019; Lipp et al., 2021; Domingo et al., 2023)"; "nutrients (Blaen et al., 2016; Asadi et al., 2025)"; "mineralogy (Walden et al., 1997; Nukazawa et al., 2021)"; "plant pollen content (Brown, 1985; Kobe, 2021)" |
| Concern | The list is a useful overview of tracer families, and most entries match their sources. Four do not, by the titles in the manuscript's own reference list. (1) Kobe (2021), cited for plant pollen content, is "Ubuntu as a spirituality of liberation for black theology of liberation", HTS Teologiese Studies / Theological Studies (p. 19, l. 597 to 598); citation and entry match by name and year, but the source cannot support the claim. (2) Walden et al. (1997), cited for mineralogy, is "Use of mineral magnetic measurements to fingerprint suspended sediment sources" (p. 20, l. 641), which belongs to magnetic susceptibility, listed separately in l. 29. (3) Olley et al. (1993), cited for geochemistry, is "Identifying sediment sources in a gullied catchment using natural and anthropogenic radioactivity" (p. 20, l. 621 to 622), which belongs to radionuclides (l. 27). (4) Blaen et al. (2016), cited for nutrients as fingerprints, is "Real-time monitoring of nutrients and dissolved organic matter in rivers" (p. 17, l. 528 to 529); its abstract (read by S1) does not mention source apportionment. Each tracer is still carried by at least one other citation, so the statements stand. The grade is moderate because a reader following the second pollen reference reaches an unrelated source and cannot trace the claim beyond Brown (1985). |
| Suggestion | In l. 26 to 31 remove Kobe (2021) or replace it by a pollen fingerprinting study and correct the entry in l. 597 to 598; move Walden et al. (1997) to magnetic susceptibility and Olley et al. (1993) to radionuclides; replace Blaen et al. (2016) by a study that uses nutrients as source tracers. |
| Status | verified (titles in the reference list, page images p. 2 and p. 17 to 20; Blaen et al. abstract) |
| Severity | moderate |
| Source | S1, S4 |

**GB-07 The claim that XRD has only recently gained attention and remains underutilised rests on one source and overlooks earlier XRD-based provenance unmixing.**

| Field | Content |
|---|---|
| Check | P28 |
| Location | p. 2, l. 36 to 37; twin p. 4, l. 103 to 104 |
| Quotation | "X-ray diffraction (XRD) has recently gained attention as a proxy for mineral abundance in provenance analysis but remains underutilized (Das et al., 2023)." |
| Concern | The sentence is the gap that motivates the study. The manuscript documents no literature search: no databases, search terms, period or date (text search for "search" and "database" finds only the RRUFF database, l. 257). A single search finds a counterexample: Andrews and Eberl (2012) unmixed source-area sediment mineralogy measured by quantitative XRD with the SedUnMix program and tested it on eleven artificial mixtures of four end members (abstract, USGS publication page). The manuscript's own references Klages and Hsieh (1975, "Using Mineralogy for Inferring Sources") and Wall and Wilding (1976, "Mineralogy and Related Parameters of Fluvial Suspended Sediments") indicate a mineralogical provenance tradition of five decades; whether they used XRD could not be checked. The abstract of Das et al. (2023) describes XRD spectra with partial least squares regression and does not state that XRD is underutilised; its full text could not be read. |
| Suggestion | In l. 36 to 37 either document the search (databases, terms, period, date) or rephrase to "XRD-based fingerprinting has been applied less often than geochemical tracers", and cite Andrews and Eberl (2012) as earlier XRD-based unmixing (GB-08). |
| Status | verified (no search documented; Andrews and Eberl abstract); inferred (Das et al. 2023 full text not read; Klages and Hsieh, Wall and Wilding: titles only) |
| Severity | moderate |
| Source | S1 |

**GB-08 Three works that anticipate or qualify the contribution are missing from the reference list.**

| Field | Content |
|---|---|
| Check | P14 |
| Location | p. 2, l. 42 to 44; p. 13, l. 404 to 406 |
| Quotation | "Building on the work of Das et al. (2023, 2024), we investigate the potential of binned XRD data as a cost-effective fingerprinting method." |
| Concern | Contribution in one sentence: spatially explicit erosion rate maps from binned XRD peak-area fingerprints, obtained by a Bayesian MAP inversion with log-space erosion rates and posterior uncertainty metrics, tested synthetically and at Gornergletscher. The Introduction positions it against Das et al. (2023, 2024) and De Doncker et al. (2020). Three works not in the reference list (checked against p. 17 to 21) bear directly on it. (1) Andrews, J. T. and Eberl, D. D. (2012) 'Determination of sediment provenance by unmixing the mineralogy of source-area sediments: The "SedUnMix" program', Marine Geology, 291-294, pp. 24-33, https://doi.org/10.1016/j.margeo.2011.10.007: XRD-based source unmixing with a test on eleven artificial mixtures, the kind of test that l. 404 to 406 invokes without citation. (2) Braun, J., Gemignani, L. and van der Beek, P. (2018) 'Extracting information on the spatial variability in erosion rate stored in detrital cooling age distributions in river sands', Earth Surface Dynamics, 6, pp. 257-270, https://doi.org/10.5194/esurf-6-257-2018: an inversion of detrital mineral data into the relative distribution of erosion rates in a catchment, tested on synthetic age distributions; it qualifies the gap in l. 58 to 59. (3) Cooper, R. J., Krueger, T., Hiscock, K. M. and Rawlins, B. G. (2014) 'Sensitivity of fluvial sediment source apportionment to mixing model assumptions: A Bayesian model comparison', Water Resources Research, 50(11), pp. 9031-9047, https://doi.org/10.1002/2014WR016194: 13 versions of a mixing model, with a Bayesian and a frequentist optimisation compared, shift median source contributions by up to 21 %; it bears on the classification in l. 44 to 57 and on the prior and covariance choices of Section 4.1.4. |
| Suggestion | Discuss the three works in Section 1 (l. 36 to 61) and state how the method differs (spatial erosion rates instead of source proportions; binned XRD instead of cooling ages; sensitivity to prior and covariance), and cite Andrews and Eberl (2012) in l. 404 to 406. |
| Status | verified (abstracts on the USGS publication page, the VU research portal and the UEA repository; absence from the reference list) |
| Severity | moderate |
| Source | S1 |

**GB-09 The classification and ranking of unmixing methods cannot be traced to the cited sources as written.**

| Field | Content |
|---|---|
| Check | P13 |
| Location | p. 2, l. 45 to 48 and l. 52; twin p. 4, l. 112 to 115 and l. 119 |
| Quotation | "Where frequentist methods estimate the uncertainty on the resulting source contributions by sampling the different possible sets of source contributions, Bayesian methods use priors, model and data uncertainty to allow error propagation so the a posteriori uncertainty can be inferred from different posterior metrics (Niu et al., 2020). In the frequentist category, the most common methods are" |
| Concern | The paragraph gives a helpful frame for placing the method. Two attributions could not be confirmed: the abstract of Niu et al. (2020) describes a linear mixing model with uncertainty from a first-order approximation and does not use the words Bayesian, frequentist, prior or posterior; the abstract of Haddadchi et al. (2013) names modified Collins and Hughes models among seven commonly used mixing models and local versus global optimisation, not NLLS, Monte Carlo, GLUE or MLE as the most common frequentist methods. The full texts of Niu et al. (2020), Haddadchi et al. (2013), Yang et al. (2025) and Fathabadi and Jansen (2022) could not be read, so the classification may appear in their body text. |
| Suggestion | Could the authors give the page of the source for the contrast of frequentist and Bayesian methods (l. 45 to 48) and for the ranking "most common" (l. 48 to 52)? If the classification is the authors' own synthesis, mark it as such and cite Niu et al. (2020) only for the linear mixing statement in l. 59. |
| Status | inferred (abstracts only) |
| Severity | minor |
| Source | S1 |

**GB-10 The list of frequentist methods introduces "NLLS" but refers back to "NNLS" and gives two method names in a non-standard form.**

| Field | Content |
|---|---|
| Check | P38 |
| Location | p. 2, l. 48 to 51; twin p. 4, l. 115 to 118 |
| Quotation | "the Non-Linear Least Squares (NLLS) (a constrained linear regression)" (l. 48 to 49); "Generalist Likelihood Uncertainty Estimation (GLUE)" (l. 50); l. 51 to 52: "Maximal Likelihood Estimation (MLE) (similar to the NNLS approach, but with a probabilistic error model)" |
| Concern | NNLS is defined nowhere in the manuscript and can only refer back to the method introduced as NLLS; the description "a constrained linear regression" fits a non-negative least squares method better than a non-linear one, so the reader cannot tell which method is meant. GLUE is usually expanded as Generalized Likelihood Uncertainty Estimation and MLE as Maximum Likelihood Estimation; the cited sources were not checked for these names. |
| Suggestion | Could the authors state which method is meant and use one name and abbreviation in l. 48 to 51 and in the twin l. 115 to 118, for example "Non-Negative Least Squares (NNLS)"? Write "Generalized Likelihood Uncertainty Estimation" and "Maximum Likelihood Estimation" if the standard methods are meant. |
| Status | verified (abbreviation mismatch, page image p. 2); assumption (which method is meant; standard names not checked in the cited sources), hence posed as a question |
| Severity | minor |
| Source | S2, S1, S4 |

#### Minor corrections

| ID | Location | Quotation | Replacement | Source |
|---|---|---|---|---|
| KK-01 | p. 1, l. 5 | "(steepest descent and Quasi-Newtonian)" | "(steepest descent and quasi-Newton)" (as in l. 211 and l. 296) | S1, S2 |
| KK-02 | p. 1, l. 24 to 25; twin p. 3, l. 91 to 92 | "An ideal fingerprint is 1) capable of distinguishing among sources and 2) remains stable" | "An ideal fingerprint 1) is capable of distinguishing among sources and 2) remains stable" | S4 |
| KK-03 | p. 2, l. 55 to 56; twin p. 4, l. 122 to 123 | "a hybrid between Bayesian linear mixed models and hierarchical Bayesian models" | "a hybrid between Bayesian Linear Mixing Models (BLMM) and Hierarchical Bayesian Models" (as named in l. 53 to 54) | S1, S4 |
| KK-04 | p. 2, l. 61; twin p. 4, l. 128 | "the inversion framework validated in (De Doncker et al., 2020)" | "the inversion framework validated in De Doncker et al. (2020)" | S1, S4 |

#### Verification log

| ID | Check | Checked | Values | Result |
|---|---|---|---|---|
| PP-01 | P13 | Inventory of statements with numbers, rankings or evaluations taken from cited works in the Abstract and Sections 1 and 2 | numbers from cited works: 0; rankings or evaluations: 11 statements (l. 10 to 13, 15 to 16, 18 to 19, 20 to 23, 24 to 25, 26 to 35, 35, 36 to 37, 43 to 55, 58 to 59, 60 to 61; twins in l. 77 to 128) | findings GB-05, GB-06, GB-07, GB-09; no finding for the other statements (PP-02 to PP-04, PP-07) |
| PP-02 | P13 | Further citations in l. 10 to 35 against the titles in the reference list | 32 citations (Gergel et al. 2002, Allan 2004, Walling 2009, Hamel et al. 2015, Issaka and Ashraf 2017, Poesen 2018, Borrelli et al. 2021, Wall and Wilding 1976, Walling et al. 1979, Gholami et al. 2019, Lipp et al. 2021, Domingo et al. 2023, Bezuidenhout 2023, Abere et al. 2025, Papanicolaou et al. 2003, Blake et al. 2012, Abbas et al. 2024, Asadi et al. 2025, Poulenard et al. 2009, Nibourel et al. 2015, Hatfield and Maher 2009, Torres Astorga et al. 2020, Nukazawa et al. 2021, Saylor et al. 2019, Brown 1985, Li et al. 2019, Brito et al. 2018, Astakhov et al. 2019, Evrard et al. 2019, Grimshaw and Lewin 1980, Martínez-Carreras et al. 2010, Collins et al. 2020); titles consistent with the stated topic; Gergel et al. 2002 has no title in the list (KK-37) | no finding |
| PP-03 | P13 | Klages and Hsieh (1975) for the two criteria of an ideal fingerprint (l. 24 to 25) | title "Suspended Solids Carried by the Gallatin River of Southwestern Montana: II. Using Mineralogy for Inferring Sources"; abstract and publisher page not readable | no finding; source not readable (Limits) |
| PP-04 | P13 | Das et al. (2023) for "many of these methods are expensive and time-consuming" (l. 35) | full text not retrievable; abstract: XRD spectra with partial least squares regression, no statement on cost or time; abstract of Das et al. (2024): MIR and XRD with MixSIAR, no statement on cost or time | no finding; source not readable in full (Limits) |
| PP-05 | P10 | Gaps in the Introduction against questions and results | gap cost (l. 35) without question or measurement (GB-01); XRD underused (l. 36 to 37) answered by the objective in l. 63 to 64; no spatially explicit maps (l. 58 to 59) answered by Section 4; linear mixing (l. 59) not answered (GB-56); glacierized catchments (l. 62 to 63) addressed by the site (GB-59) | no finding for the two answered gaps |
| PP-06 | P14 | Search for works on the contribution; candidates held against the reference list (p. 17 to 21) | five queries on XRD mineralogy unmixing, inversion of detrital data into spatial erosion rates, Gornergletscher provenance, Bayesian mixing model assumptions, mineralogical fingerprints with geological maps; candidates: Andrews and Eberl 2012, Braun et al. 2018, Cooper et al. 2014 (not in the list), De Doncker et al. 2020 and Das et al. 2024 (in the list), a conference abstract EGU21-6207 by the same authors (not peer reviewed, not proposed); search results leading to this manuscript, its discussion or later versions were not opened | finding GB-08 for the three missing works; no finding for the others |
| PP-07 | P13 | De Doncker et al. (2020) for "the inversion framework validated in" (l. 61) | abstract (serval.unil.ch): least-squares inversion with prior and model covariance; synthetic and natural examples recover erosion rate patterns | no finding for the citation; the novelty consequence is GB-56 |

### Segment 2: Methods, study area and validation design (p. 5 to 10)

#### Substantive findings

**GB-11 Two central assumptions, immediate export without storage and XRD grain-size and orientation effects, appear only in the Discussion, not where the forward model and the XRD method are introduced.**

| Field | Content |
|---|---|
| Check | P17 |
| Location | p. 5, l. 147 to 148; p. 15, l. 467 to 470 |
| Quotation | "These sediments are then transported or stored." (l. 147 to 148); "We caution against using this method in catchments with significant sediment storage, as the inversion directly links sediment provenance to erosion rates and assumes immediate sediment export" (l. 466 to 468); l. 469 to 470: "Grain-size effects may influence peak intensities" |
| Concern | The manuscript discloses both assumptions, which is to its credit; their place in the method and their consequence are not drawn through. Section 3.1 mentions storage without saying that the forward model ignores it; the assumption of immediate export is first stated in l. 467 to 468. Section 3.4 does not mention grain-size or preferred-orientation effects, which first appear in l. 469 to 473. A reader of the Methods therefore does not see that one instantaneous suspended sample (28 June 2019, 13:30; l. 423 to 424) is equated with an erosion rate map scaled by an annual export estimate; the temporal representativeness of that sample is not addressed anywhere. |
| Suggestion | Add the immediate-export assumption to Section 3.1 after Eq. (1) and the grain-size and orientation caveats to Section 3.4; state in Section 4.2.2 what period the sample of 28 June 2019 represents. |
| Status | verified |
| Severity | moderate |
| Source | SD |

**GB-12 Iteration, tracer and pixel indices and two posterior symbols change within the method equations.**

| Field | Content |
|---|---|
| Check | P38 |
| Location | p. 5, l. 154 to 156; p. 6, l. 176; p. 7, l. 208 to 209; p. 8, l. 215 to 216 and l. 219; p. 9, l. 262 to 263; p. 14, l. 436; Figure 3 (p. 24), panel (d) |
| Quotation | "εk+1 the posterior model after k + 1 non-linear iteration steps" (l. 209); "where Gn is the Jacobian at iteration n" (l. 216); l. 262 to 263: "We can thereby derive the abundance of a given tracer t at pixel xy in At,xy as well as in the detrital data dt (eq. 1-4)" |
| Concern | (a) The iteration index is k in Eq. (17) and l. 209 but n in Eqs. (18) and (19) and l. 216, while the prior term inside Eqs. (18) and (19) is written with εk; n is also the number of pixels in Eqs. (1) and (4). (b) The tracer index is i in Eq. (1) and l. 155, t in l. 262, and n in Figure 3(d), where i denotes a detrital sample instead. (c) The pixel index is j in Eq. (1) and xy in l. 262 to 263. (d) The posterior is p(εm∣dobs) in Eq. (5) and p(ε∣dobs) in l. 176; the posterior covariance is C̃m in Eq. (20) and Cm,post in l. 436. Each pair denotes the same object; no passage states the equivalence. |
| Suggestion | Use one iteration index (for example k) in Eqs. (17) to (19) and l. 216, including the prior term, reserve n for the number of pixels, use i for tracers and j for pixels throughout (l. 262 to 263 and Figure 3(d), with a separate index for detrital samples), and keep one symbol for the posterior and one for the posterior covariance (Eq. 5, l. 176, l. 436). |
| Status | verified (page images p. 5 to 9, 14 and 24) |
| Severity | minor |
| Source | S2, SD |

**GB-13 The prior term of the misfit is called "prior misfit" once and "model misfit" afterwards, and σm² is called "prior variance" while σm is called "model standard deviation".**

| Field | Content |
|---|---|
| Check | P38 |
| Location | p. 6, l. 184; p. 7, l. 190 and l. 202 |
| Quotation | "and the prior misfit" (l. 184); "and the gradient of the model misfit can be written as" (l. 202); "The model misfit (eq. 7) measures the deviation from the prior" (l. 245); "the prior variance" (l. 190); l. 294: "a model standard deviation of 3" |
| Concern | ϕprior is introduced as "prior misfit" in l. 184 and then appears as "model misfit" in 13 text lines (Python count) and on all misfit axes of Figures 5 to 10, while the symbol ϕprior is kept in Eqs. (10) and (15). Likewise σm² is "the prior variance" in l. 190, while all hyperparameter passages and Figure 10 use "model standard deviation" σm. The pairs denote the same objects, which can be inferred but is not stated. |
| Suggestion | In l. 183 to 184 write "the prior (model) misfit ϕprior, hereafter model misfit", and in l. 190 "with σm² the prior (model) variance; σm is hereafter called model standard deviation". |
| Status | verified (page images p. 6 to 10) |
| Severity | minor |
| Source | S2 |

**GB-14 The model covariance in Eq. (9) lacks the minus sign in the exponent and, as printed, is not a valid covariance.**

| Field | Content |
|---|---|
| Check | P8 |
| Location | p. 7, l. 189 |
| Quotation | "Cm(i,j) = σm² exp(si,j²/L²)" |
| Concern | Eq. (9) is printed as quoted (page image p. 7). With exp(+s²/L²) the covariance grows with distance instead of decaying. Python check on 30 pixels at 300 m spacing with L = 1200 m and σm = 3: the printed kernel gives 9 at zero distance and about 2.4e25 at 9000 m, and the matrix has a smallest eigenvalue of minus 6.1e23, so it is not positive definite and not a covariance; with the minus sign the smallest eigenvalue is non-negative (6.8e-13). A reader rebuilding the smoothing prior from the text cannot reproduce it. |
| Suggestion | Correct Eq. (9) to Cm(i,j) = σm² exp(-s_ij²/L²) and state whether the code uses this form. |
| Status | verified (equation on the page image p. 7); inferred (consequence, Python) |
| Severity | moderate |
| Source | SD |

**GB-15 The Jacobian and the update equations cannot be implemented as printed: Eq. (12) gives a vector, Eq. (14) lacks a transpose, Eq. (19) inverts a singular matrix, and Eq. (18) omits the gradient normalisation that was used.**

| Field | Content |
|---|---|
| Check | P8, P25 |
| Location | p. 7, l. 197 and l. 201; p. 8, l. 215 and l. 219 |
| Quotation | "the number of tracers, representing the data we have, is smaller than the number of pixels" (l. 170 to 171); l. 312: "In initial experiments, the steepest descent approach proved unstable, requiring the normalization of the gradient." |
| Concern | (1) Eq. (12) writes the Jacobian of dε = A·exp(ε) as G = A·exp(ε), a matrix-vector product that gives a vector of length m; the Jacobian is A·diag(exp(ε)), an m by n matrix (raised as a hint by S1 and confirmed at the page image p. 7). (2) Eq. (14) writes G C_d^-1 without transpose, whereas Eq. (16) writes G^T C_d^-1. (3) Eq. (19) inverts G_n^T C_d^-1 G_n. With m tracers and n pixels, m smaller than n (l. 170 to 172), this n by n matrix has rank at most m; Python with m = 21 and n = 500 or 900 gives rank 21. The inverse does not exist, so the update cannot have been computed as printed; the usual Gauss-Newton form includes C_m^-1 inside the inverse, as Eq. (20) does for the posterior covariance. (4) Eq. (18) contains no gradient normalisation, although Section 4.1.2 states that the reported steepest descent run used one (l. 312). A reader cannot rebuild either update scheme from Section 3.2. |
| Suggestion | In Section 3.2 write the Jacobian as A·diag(exp(ε)), add the transpose in Eq. (14), replace Eq. (19) by the update actually implemented (for example with (G^T C_d^-1 G + C_m^-1)^-1 or a damping term), and add the normalisation to Eq. (18). |
| Status | verified (equations on the page images p. 7 and p. 8); inferred (rank argument, Python) |
| Severity | moderate |
| Source | SD, ZF |

**GB-16 The normalised posterior uncertainty has two definitions and many names, its axis label names another quantity, and the resolution has no computable formula.**

| Field | Content |
|---|---|
| Check | P20, P38, P8 |
| Location | p. 8, l. 236 to 239; p. 10, l. 303; p. 14, l. 436; Figure 5 (p. 26), panels (d), (f), (h) and caption; Figures 7 to 10 (p. 28 to 31), uncertainty axes; Figure 14 (p. 35), resolution panel |
| Quotation | "The third metric is the ratio between the posterior model covariance and the “prior” model covariance." (l. 236 to 237); "a high total normalized uncertainty (tr(Cm,post)/tr(Cm)) value of 0.87" (l. 436, fraction as printed); l. 303: "The same pattern is visible in the normalised posterior variance" |
| Concern | Eq. (22) defines a per-pixel ratio of square roots, sqrt(C̃m)/sqrt(Cm), a standard-deviation ratio; l. 436 defines a scalar ratio of traces without square root, a variance ratio, and changes the symbol from C̃m (Eq. 20) to Cm,post. The two give different numbers for one inversion: if 0.87 is a variance ratio, the standard-deviation ratio is sqrt(0.87) = 0.933 (0.82 gives 0.906, 0.86 gives 0.927; Python). The quantity carries at least seven names: "ratio between the posterior model covariance and the “prior” model covariance" (l. 236 to 237), "normalised posterior variance" (l. 303), "normalised posterior covariance" (captions of Figures 5 and 6), "Normalised covariance trace" (Figure 5(h)), "normalized posterior uncertainty" (l. 335, 441, 446), "total normalized uncertainty" (l. 436) and "Posterior uncertainty" (Figures 7 to 9), and l. 306 calls the curve of Figure 5(h) "posterior covariance". The axis labels "Trace(post. cov.)" (Figures 7 to 9) and "Trace(post.covar.)" (Figure 10) name the unnormalised trace, but the plotted values lie between about 0.3 and 1.0, the range of a ratio, while Figure 5(e) shows posterior covariance diagonals from 2 to 8. Whether the traces are taken in ε space or in erosion-rate space is not stated. Eq. (21) defines the resolution operator R only implicitly, and no formula for the non-linear case is given, although "Resolution diagonal" is mapped in Figures 5, 6 and 14 to 16. In Figure 14, 96 % of the resolution map pixels are closest in colour to scale values of 0.9 or more (median 0.95; colour distance 66 because of the hillshade overlay; Python on the page image), while l. 436 calls the zircon resolution "low"; is the panel drawn on the scale shown? The grade is moderate: the values 0.87, 0.82 and 0.86 cannot be recomputed without the definition, but their comparison stands if one definition was used throughout. |
| Suggestion | In Section 3.3 define one metric for maps (Eq. 22) and one scalar summary (state whether it is tr(C̃m)/tr(Cm) or the mean of Eq. 22, and in which space), give each one name and symbol, and use them in l. 303, 306, 335, 436, 441 and 446 and in all captions and axis labels of Figures 5 to 10 and 14 to 16; add the formula for R at the final iterate (for example R = I - C̃m Cm^-1) and check the colour scale of the resolution panel of Figure 14 against l. 436. |
| Status | verified (definitions, names, axis labels and values on the page images); inferred (numerical consequence, Python; colour reading of Figure 14, posed as a question) |
| Severity | moderate |
| Source | S2, S3, SD, AB, ZF |

**GB-17 The stated stopping rule did not govern the reported runs, which ended at fixed caps that coincide with the error minimum against the true map, and the description of the iteration sweep does not match Figure 10.**

| Field | Content |
|---|---|
| Check | P5, P3 |
| Location | p. 9, l. 243 to 244; p. 13, l. 387 to 388; Figure 10 (p. 31), row 5 |
| Quotation | "We stop the non-linear iterations when the data-misfit stops decreasing, or when it exceeds the user-defined maximal allowed number of iterations." (l. 243 to 244); l. 387 to 388: "Only when the maximum number of non-linear steps is reduced below 25 does the posterior fail to converge to the true erosion map." |
| Concern | By the manuscript's own record the data misfit still changes until iteration 115 (l. 388 to 389). The degradation tests and all natural runs used 25 iterations, 21.7 % of 115, and the first quasi-Newton test 100 iterations, 87.0 % (Python), so the reported runs were ended by the cap, not by the stated condition. The cap of 25 coincides with the minimum of the error against the known truth: in Figure 5(g) the lower envelope is lowest at iterations 20.4 to 23.5 and then rises by 5.1 to iteration 100, and in Figure 10, row 5, the minimum is 197.6 at n = 25, lower than every larger n (199.6 at n = 35, 200.6 to 201.1 for n of 45 and more; AB measurement). This amounts to early stopping chosen on the true map, which does not exist for natural data; the rise after iteration 25 may indicate over-fitting. The sentence in l. 387 to 388 is also not what row 5 shows: below 25 there are two points, n = 5 (268.7) and n = 15 (200.9), and the value at n = 15 lies within the plateau, so only the shortest run fails. The iteration numbers are compatible with each other (PP-31); this finding concerns whether the rule governed the runs. |
| Suggestion | In Section 3.2 state the convergence threshold and that 25 iterations is an early-stopping choice; in Section 4.1.4 justify it without the true map (for example by a discrepancy criterion on the data misfit), rephrase l. 387 to 388 to what row 5 shows, and report for the natural runs whether the stopping condition or the cap ended the iterations. |
| Status | verified (text; values measured on Figures 5(g) and 10); inferred (shares, Python) |
| Severity | moderate |
| Source | SD, AB |

**GB-18 The XRD and zircon laboratory chains cannot be rebuilt from the text: instrument, scan settings, 2θ windows, Peak Finder settings, sample numbers and the zircon protocol are missing.**

| Field | Content |
|---|---|
| Check | P8, P35 |
| Location | p. 9, l. 251 to 258; p. 13, l. 393 to 394; p. 14, l. 424 |
| Quotation | "In a fifth step, diagnostic 2θ windows for each mineral are selected from RRUFF database reference spectra" (l. 257 to 258); "we focused on a set of 21 minerals expected to be characteristic of the main lithologies in the catchment" (l. 393 to 394); l. 424: "following the methodology described in (Belotti, 2021)" |
| Concern | Missing are: diffractometer model, radiation, 2θ range, step size and counting time; sample preparation (grinding, target grain size, mount); the WinXRD version and the Peak Finder thresholds and fit settings; the RRUFF access date and the 2θ windows of the 21 minerals; the number of source samples per unit and the rule that combines several samples into one fingerprint per unit; the criterion for selecting the 21 minerals beyond "expected to be characteristic"; and whether "we average the total peak area" (l. 260) means summing or averaging. The lithology description names "calcareous mica schists" and "marbles" (l. 275, 278), but calcite is not among the 21 minerals; was it excluded deliberately? The zircon method is documented only in an unpublished master's thesis (reference list, Belotti, 2021). These settings determine A and d, so neither the natural fingerprints nor the inversions of Section 4.2 can be rebuilt. |
| Suggestion | Add to Section 3.4 or a supplement the instrument and scan settings, the preparation, the software versions, a table of the 21 windows with RRUFF reference IDs, the Peak Finder settings, the number of source samples per unit and the aggregation rule, the mineral selection criterion with a statement on calcite, and a summary of the zircon separation and dating protocol with instrument and standards. |
| Status | verified (missing items); assumption (relevance of calcite, from the lithology description), posed as a question |
| Severity | moderate |
| Source | SD |

**GB-19 Several mineral tracers carry identical fingerprints, and the claim that window averaging reduces peak overlap is not tested.**

| Field | Content |
|---|---|
| Check | P3, P26 |
| Location | p. 9, l. 259 to 260; p. 16, l. 475 to 476; Figure 11 (p. 32), rows Annite, Phlogopite, Muscovite, Anorthite, Pyroxene, Ankerite, Dolomite, Albite, Paragonite, Omphacite; Figure 15 (p. 36) |
| Quotation | "Sixth, to mitigate peak overlap, we average the total peak area within the 2θ windows corresponding to each mineral, rather than relying on individual peaks." (l. 259 to 260); l. 475 to 476: "Averaging peak areas across multiple 2θ values for the same mineral also reduces the possible impact of peak overlap between minerals with similar diffraction angles" |
| Concern | Bar lengths measured row by row in Figure 11 (AB; full width 244 px, about ±0.004) show two exact duplicates across all seven units: Annite and Phlogopite (0.000, 0.541, 0.311, 0.566, 0.213, 0.660, 0.541 in caption order) and Anorthite and Pyroxene (0.000, 0.143, 1.004, 0.381, 0.996, 0.029, 0.426). Muscovite equals Annite except in one column, Ankerite and Dolomite differ only in one column (0.020 against 0.029), and Albite and Paragonite differ by at most 0.029; the same identities recur in the stacked bars of Figure 15. The 21 named tracers therefore carry between 16 and 19 distinct patterns. The list also contains the group "Pyroxene" beside its members "Omphacite" and "Diopside" (l. 394 to 395), and the eclogite-bearing unit shows a high Pyroxene bar with a very small Omphacite bar. Identical values across all lithologies suggest that the windows of these pairs coincide or contain the same peaks; averaging within a window cannot separate them, and the overlap lowers the distinctiveness that the manuscript identifies as the most influential factor (l. 363 to 364). Do the windows overlap, and how are shared peaks assigned? |
| Suggestion | List the 2θ windows per mineral in Section 3.4 or a supplement, merge or drop duplicated tracers, state the number of independent tracers used in Section 4.2, check whether the JS distances in l. 447 to 448 change, and test the averaging on RRUFF reference spectra or pure mineral standards. |
| Status | verified (identical bar lengths by measurement; mineral list); assumption (cause: shared windows), posed as a question |
| Severity | moderate |
| Source | AB, SD |

**GB-20 Normalising each sample by its own maximum peak area breaks the linear mixing of Eq. (1), and Figures 11 and 15 show two different normalisations of the source fingerprints.**

| Field | Content |
|---|---|
| Check | P25, P3 |
| Location | p. 9, l. 261 to 264; Figure 11 (p. 32); Figure 15 (p. 36), stacked bars; Figure 5 (p. 26), panel (k) |
| Quotation | "these are normalized within each sample by dividing by the maximum observed peak area, yielding relative mineral concentrations on a scale from 0 to 1" (l. 261 to 262); l. 151 to 152: "Hence, the detrital data are a weighted average of the tracer mineral concentrations, with the weights being the erosion rates." |
| Concern | Even if raw peak areas mixed linearly, the normalised mixture equals Σ w_k a_k divided by max(Σ w_k a_k), while Eq. (1) fits Σ w'_k (a_k / max a_k). Matching the two gives w'_k proportional to w_k · max(a_k): each source's weight is scaled by its own maximum peak area. Python example with three sources of equal true weight and maxima 100, 80 and 300: recovered relative weights 0.208, 0.167 and 0.625, the ratio of the maxima. The synthetic tests cannot detect this, because their data are generated with Eq. (1) on already normalised fingerprints, and the purpose stated in l. 263 to 264 ("minimizing the influence of absolute intensity differences") is asserted, not measured. In addition, Figure 11 follows the stated normalisation (longest bar per unit 0.996 to 1.004), whereas Figure 15 ("Normalised abundance per mineral or age") and Figure 5(k) normalise per mineral across units; Figure 15 does not equal the rows of Figure 11 divided by their sums (largest per-mineral deviation: median 0.135, maximum 0.216, for example Antigorite, serpentinite share 0.639 against 0.425), and only a separate scale factor per lithology (0.20 to 1.00) brings the deviation down to a median of 0.012 (AB measurement and fit). Which version enters A in Section 4.2 is not stated. The grade is major: if the normalisation is as described, erosion rates attributed to sources of high or low absolute intensity are biased, which changes the natural results of Sections 4.2.1 and 4.2.2. |
| Suggestion | State in Section 3.4 which normalisation enters A and d and show that it preserves linear mixing (for example normalisation by an internal standard or a common reference mineral), make Figures 11 and 15 consistent with it, and test the chain with laboratory mixtures of the source powders in known proportions, the test the manuscript names in l. 404 to 406. |
| Status | inferred (derivation from the described normalisation, Python); verified (difference between Figures 11 and 15 by measurement); assumption (which normalisation the code uses), posed as a question |
| Severity | major |
| Source | SD, AB |

**GB-21 The lithology inferred under the ice enters the tracer matrix of all natural runs without a test against an alternative map.**

| Field | Content |
|---|---|
| Check | P27 |
| Location | p. 9, l. 270 to 271 |
| Quotation | "In ice-covered regions, where direct geological mapping is not possible, we infer the lithology based on regional geological knowledge." (l. 270 to 271); l. 364: "Geological map uncertainty follows as the second most influential factor." |
| Concern | The manuscript discloses the inference, and its own scenario 1 shows that map mismatch raises the summed error from about 197.5 to 274.8 (Figure 7, AB measurement). The share of the catchment whose lithology is inferred is not given, and the natural inversions (Sections 4.2.1 and 4.2.2) are not rerun with an alternative map, although the Steck et al. (2015) map used in scenario 1 is at hand. No step propagates map uncertainty, so the stated aim of "quantifying posterior uncertainty and error propagation" (l. 6 to 7) does not cover this input. |
| Suggestion | State in Section 4 the percentage of the catchment area with inferred lithology, rerun the natural inversions with the Steck et al. (2015) map and report the change in Section 4.2. |
| Status | verified |
| Severity | moderate |
| Source | SD |

**GB-22 The seven lithological units carry different names and spellings in the text and in Figures 4, 5, 11 to 13, 15 and 16, so two units cannot be traced from the text to the figures.**

| Field | Content |
|---|---|
| Check | P38 |
| Location | p. 10, l. 274 to 276; p. 10, l. 299; p. 12, l. 340; p. 14, l. 411, l. 414 and l. 432; Figure 4 (p. 25), legend; Figure 11 (p. 32), caption; Figure 12 (p. 33), caption; Figure 13 (p. 34), labels; Figures 5(j), 15 and 16 (p. 26, 36, 37), legends |
| Quotation | "Penninic Mesozoic sedimentary units (Bündnerschiefer)" (l. 274 to 275); "the Zermatt - Saas Fee unit (ZSF sediments)" (l. 414); "the Monte Rosa garnet-gneiss (MR g-g) unit" (l. 432); "Stockhorn-Turftgrat-Gornergrat" and "ZSF ophiolites (metabasites, ecologites)" (Figure 11 caption); Figure 4 and Figure 12 legend: "Stockhorn basement, Tuftgrat Mesozoic and GornergratPermo-Mesozoic" |
| Concern | Counted variants per unit. (a) Sedimentary unit: "Penninic Mesozoic sedimentary units (Bündnerschiefer)" (l. 274 to 275), "Zermatt Saas-Fee sediments" (l. 299), "Zermatt - Saas Fee sediment unit" (l. 411), "Zermatt - Saas Fee unit (ZSF sediments)" (l. 414), "Zermatt - Saas Fee sediments" (Figures 4 and 12), "Zermatt- Saas Fee sediments unit" (Figure 12 caption) and "ZSF sediments" (Figures 5(j), 11, 13, 15, 16); only the outcrop legend of Figure 4 links it to the Bündnerschiefer, and "Zermatt - Saas Fee unit" in l. 414 could equally be read as the ophiolites. (b) Monte Rosa gneiss unit: "Monte Rosa (garnet gneiss and micaschist)" (Figure 4), "Monte Rosa (gneiss, micaschist)" (Figures 11, 13), "MR gneiss, mica" (Figures 5, 15, 16) and "Monte Rosa garnet-gneiss (MR g-g)" (l. 432); l. 275 to 276 describes one "Monte Rosa nappe" without splitting it into the two mapped units. (c) Stockhorn unit: "Stockhorn basement, Tuftgrat Mesozoic and GornergratPermo-Mesozoic" (Figure 4), "The Stockhorn, Tuftgrat, and Gornergrat units" (l. 276), "Stockhorn, Tuftgrat, Gornergrat" (Figure 13), "S.,T.,G." (legends) and the misspelling "Turftgrat" (Figure 11 caption). (d) Metabasite unit: "Zermatt - Saas Fee ophiolites (metabasites and eclogites)" (Figure 4), "ZSF ophiolites (metabasites, ecologites)" (Figure 11 caption, misspelt), "ZSF ophiolites (metabasites, eclogites)" (Figure 13) and "ZSF metabasites" (Figures 15, 16); l. 340 spells "Zermatt-Saas-Fee ophiolites". The identity matters for two results: which unit received the substituted zircon fingerprint (l. 433 to 434; Figure 14 has no lithology legend) and which unit is the control without outcrops in Section 4.2.1. The unit count itself is consistent (PP-13). The grade is moderate because the unit identity carries the interpretation of Section 4.2. |
| Suggestion | Introduce one name and one abbreviation per unit in Section 4 (l. 273 to 279), matching the legend of Figure 4, for example "ZSF sediments (Bündnerschiefer)", "MR gneiss and micaschist (MR g-m)", "Stockhorn, Tuftgrat and Gornergrat (STG)" and "ZSF metabasites and eclogites", with "Zermatt-Saas Fee" spelled the same throughout; use them in l. 299, 340, 411, 414 and 431 to 434, in all captions and legends (correcting "Turftgrat", "ecologites" and "GornergratPermo-Mesozoic"), and in a lithology legend for Figure 14. |
| Status | verified (page images p. 10, 12, 14, 25, 26, 32, 33, 34, 36, 37) |
| Severity | moderate |
| Source | S2, S3, S4, AB |

**GB-23 Third-party data shown in Figure 4 are covered neither by the data statement nor by the reference list.**

| Field | Content |
|---|---|
| Check | P12 |
| Location | Figure 4 (p. 25), credit line and legend; reference list p. 17 to 21 |
| Quotation | "Land cover data: SwissTopo 2018 Geological data: data from Steck et al., 2015, personal communication by L. Baumgartner, outcrops by GeoCover" (Figure 4, credit line); l. 270: "Figure 4 shows the study area, with the inferred geology, outcrops and land cover." |
| Concern | The geological map builds the tracer matrix A (l. 408), so its origin is a data source of the method. Figure 4 credits four origins: SwissTopo 2018 (land cover), GeoCover (outcrops), Steck et al. (2015) and a personal communication by L. Baumgartner (geological data); glacier outlines and an "ELA estimation" are drawn without credit. Only Steck et al. (2015) is in the reference list; there is no entry for SwissTopo or GeoCover, and Baumgartner appears otherwise only in the Acknowledgements (l. 499). The data statement (l. 490) covers "data and codes used for the inversion tests" and says nothing about these layers, their versions or their licences; the part of the inferred map that rests on the personal communication cannot be traced to a citable source. |
| Suggestion | Add reference entries with product name, version and access date for the SwissTopo land cover and the GeoCover outcrop data, name the source of the glacier outlines and the ELA estimate in the caption of Figure 4, and state in the data statement (l. 490) whether the inferred geological map, including the parts based on the personal communication, is part of the Zenodo record. |
| Status | verified (credit line and legend on the page image p. 25; absence in the reference list and in l. 490) |
| Severity | moderate |
| Source | S2 |

**GB-24 Three red-orange swatches in the legend of Figures 4 and 12 cannot be told apart.**

| Field | Content |
|---|---|
| Check | P3 |
| Location | Figure 4 (p. 25), legend; Figure 12 (p. 33), legend |
| Quotation | "Stockhorn basement, Tuftgrat Mesozoic and GornergratPermo-Mesozoic"; "Outcrops: garnet mica & muscovite schist, calcareous micaschist, carbonate-bearing muscovite quartzite, amphibolite-garnet micaschist, pennine sediments"; "Outcrops: garnet-bearing silimanite-biotite gneiss" |
| Concern | Measured swatch colours (Figure 12, AB): Stockhorn #fc7434, its outcrops #fc3434, Monte Rosa garnet gneiss outcrops #fc5c34. The last differs by 24 from the first and by 40 from the second (sum of absolute RGB differences), so all three are equal by the colour criterion, and on the map outcrops of the Monte Rosa gneiss and of the Stockhorn unit cannot be distinguished by colour. |
| Suggestion | Give the Monte Rosa gneiss outcrops a clearly different colour or a pattern. |
| Status | verified (colours measured on the page image) |
| Severity | minor |
| Source | AB |

**GB-25 Several figures lack colour keys, labels or resolved abbreviations.**

| Field | Content |
|---|---|
| Check | P29 |
| Location | Figure 4 (p. 25), caption and insets; Figure 5 (p. 26), panel (k); Figures 8 and 9 (p. 29, 30), top rows; Figure 11 (p. 32); Figure 14 (p. 35); captions of Figures 5, 11, 13, 15 and 16 |
| Quotation | "Figure 4. Study area: location, land cover and geology."; Figure 14 caption: "the geological map and the source fingerprints." |
| Concern | Figure 14 has no lithology legend for its map or its stacked bars, although the text sends the reader to "the source signatures in Figure 14" (l. 430). The top rows of Figures 8 and 9 show coloured stacked bars without legend or tracer labels. Figure 11 has no column labels and no value axis; the column order is given only in the caption. Panel (k) of Figure 5 labels the tracers A to U without saying that they are the 21 synthetic tracers. The abbreviations "S.,T.,G.", "ZSF" and "MR" are not resolved in the captions of Figures 5, 11, 13, 15 and 16 ("ZSF" is first resolved in l. 431). Figure 4 leaves "ELA estimation" unresolved, and its caption explains neither the insets nor the difference between inferred units and outcrops. |
| Suggestion | Add a lithology legend to Figure 14 and to the top rows of Figures 8 and 9, column labels and a value axis to Figure 11, resolve the abbreviations in each caption, and expand the caption of Figure 4. |
| Status | verified (page images) |
| Severity | minor |
| Source | AB |

#### Minor corrections

| ID | Location | Quotation | Replacement | Source |
|---|---|---|---|---|
| KK-05 | p. 5, l. 146 | "it undergoes erosion (Figure 1A) and thereby produces sediments" | "undergoes erosion (Figure 1A) and thereby produces sediments" | S4 |
| KK-06 | p. 5, l. 146; p. 6, l. 166 to 167; p. 9, l. 258; all panel citations in Sections 3 and 4 | "(Figure 1B)"; "(Figure 3D and 3E)"; "(Figure 5K)" | lower-case panel letters as printed in the figures: "(Figure 1b)", "(Figure 3d and e)", "(Figure 5k)" | S4 |
| KK-07 | p. 5, l. 154 (Eq. 1) | "f or i = 1, . . . m" (set in math italic) | upright text "for i = 1, ..., m" | S4 |
| KK-08 | p. 6, l. 174 | "given the observed detrital data and a prior knowledge" | "given the observed detrital data and prior knowledge" | S4 |
| KK-09 | p. 6, l. 175 (Eq. 5) | "p (εm ∣dobs ) p (dobs ∣εm ) ·" (no relation sign between the two terms, page image p. 6) | "p(εm∣dobs) ∝ p(dobs∣εm) · p(εprior)/p(dobs)" | S4, SD |
| KK-10 | p. 6, l. 181 | "becomes Tarantola (2005):" | "becomes (Tarantola, 2005):" | S4 |
| KK-11 | p. 8, l. 236 | "data have improved our knowledge considerately relative to the prior" | "data have improved our knowledge considerably relative to the prior" | S4, SD |
| KK-12 | p. 8, l. 240 to 241 | "The data misfit explains how well the model - here: our a posteriori erosion rate map - explains the observed data." (italics extend over "erosion") | "The data misfit describes how well the model, here our *a posteriori* erosion rate map, explains the observed data." | S4 |
| KK-13 | p. 9, l. 244 | "or when it exceeds the user-defined maximal allowed number of iterations" | "or when the number of iterations reaches the user-defined maximum" | S4 |
| KK-14 | p. 9, l. 245 | "weighed by the model covariance" | "weighted by the model covariance" | S4 |
| KK-15 | p. 9, l. 267 and l. 272; p. 10, l. 282; p. 15, l. 463; Figure 11 (p. 32), caption | "Gorner-gletscher catchment"; "Gornergletscher"; "the Gorner gletscher catchment" | one name throughout, for example "Gorner Glacier" as in l. 392, l. 400 and the Acknowledgements | S2, S4, AB |
| KK-16 | Figure 3 (p. 24), panel (c), legend | "quarz pattern alignment" | "quartz pattern alignment" | S2, AB |
| KK-17 | Figure 4 (p. 25) and Figure 12 (p. 33), legend | "biotite schits"; "caclcite-zoisite amphibolites"; "silimanite-biotite gneiss"; "metamorphic bündnerschiefer, calcarious mica schist" | "biotite schist"; "calcite-zoisite amphibolites"; "sillimanite-biotite gneiss"; "metamorphic Bündnerschiefer, calcareous mica schist" | AB |

#### Verification log

| ID | Check | Checked | Values | Result |
|---|---|---|---|---|
| PP-08 | P5 to P38 (design sketch) | Design sketch from the whole manuscript, including captions and declarations | 7 units and 21 minerals (Python counts); no explicit research questions; 3 synthetic aims (l. 280 to 281) and 3 natural aims (l. 282 to 285); hypothesis l. 410 to 411; 8 disclosed limitations (ice-covered lithology l. 270 to 272; small units l. 299 to 300; steepest descent instability l. 312; indistinct fingerprints l. 353 to 354; zircon gaps l. 430 to 434; storage l. 466 to 468; grain size and orientation l. 469 to 473; weak non-linearity l. 177 to 178) | no finding as such; basis of GB-11, GB-21, GB-26, GB-42, GB-45 |
| PP-09 | P26 | Positivity guarantee across all paths | log-space parameterisation (l. 157 to 158) enters Eq. (3) for quasi-Newton and steepest descent, synthetic and natural runs | no finding |
| PP-10 | P19 | Provenance class of each core claim | 7 core claims: 3 on model-generated data, declared synthetic (l. 280); 3 with secondary or substituted inputs, disclosed (l. 270 to 272, l. 433 to 434); 1 on primary XRD data against literature | no separate finding; consequences in GB-21, GB-44, GB-45 |
| PP-11 | P4 | Section and equation numbering and equation references | Sections 1 to 6 without gap (Section 2 duplicates Section 1, GB-03); Eqs. (1) to (22) without gap or double number; references "eq. 1-4" (l. 263), "eq. 7" (l. 191, 240, 245), "eq. 16" (l. 213, 217), "eq. 12 and eq. 13 into eq. 11" (l. 200), "eq. 14 and eq. 15 in eq. 10" (l. 204): each target exists and contains the quantity referred to; no tables or appendices | no finding |
| PP-12 | P38 | Method and dataset abbreviations | QN 7, SD 3, JS 13 (defined l. 345), PCA 1, MAP 2, KDE 3, RRUFF 3, XRD 67, GLUE 2, MLE 2, BLMM 2, TOC 2 occurrences; "WinXRD Peak Finder" (l. 254, 473) and "Peak Finder algorithm" (l. 396) denote one tool | no finding apart from GB-10 and KK-01 |
| PP-13 | P38 | Unit count and site names across the figures | seven units in Figures 4, 11, 12, 13 and in the legends of Figures 5(j), 15 and 16, plus the class "Gorner glacier"; "Gorner-Grenzgletscher confluence" (l. 406, Figure 12), "Gorner-Grenz subcatchment" (l. 411) and "Gorner-Grenz catchment" (Figure 13) denote one site | no finding on count and site names; unit names GB-22, glacier name KK-15 |
| PP-14 | P29 | Schematic Figures 1 to 3 | every colour and symbol explained (erosion types, lithologies 1 to 4, pump sampler, glacier, source sample location, diffractogram types, instrument parts); the figures declare themselves schematic and carry no values | no finding apart from KK-16 |

### Segment 3: Results of the synthetic and natural tests (p. 10 to 15)

#### Substantive findings

**GB-26 The synthetic validation uses one true map, the same forward model for generating and inverting data, no stated noise and a prior equal to the true mean, and tunes and evaluates on the same configuration.**

| Field | Content |
|---|---|
| Check | P10 |
| Location | p. 10, l. 288 to 289; p. 11, l. 325 to 326; p. 16, l. 482 to 483 |
| Quotation | "we generate synthetic detrital data using the forward model applied to a “true” erosion rate map featuring a localised hotspot" (l. 288 to 289); l. 295: "a prior equal to the average true erosion rate" |
| Concern | All synthetic tests use a single true map with one hotspot, and the data are generated by the same forward model and, except in scenario 1, with the same map used in the inversion. This configuration is known as the inverse crime: "The inverse crime occurs when the same (or very nearly the same) theoretical ingredients are employed to synthesize as well as to invert data in an inverse problem." (Wirgin, A. (2004) 'The inverse crime', arXiv:math-ph/0401050, abstract). No noise added to the synthetic detrital data is stated (the only occurrence of "noise" is the background noise of diffractograms, l. 255). The prior equals the mean of the truth, so the inversion starts at the correct overall level, and the iteration cap and step size were chosen by the error against this same truth (GB-17, GB-53) and then evaluated on it. The scenario 1 result that a modified map beats the correct one because it moves a unit "closer to the centre of the true erosion-rate bump" (l. 341) shows how strongly the evaluation depends on the single hotspot position. The grade is major because the validation of the inversion, the main result of Section 4.1 and the basis of l. 482 to 483, rests on this configuration. |
| Suggestion | Counter-design for Section 4.1: generate several truth maps (hotspots in each unit, several hotspots, uniform erosion), add noise at a level derived from replicate XRD measurements, generate the data on a finer grid or with a perturbed forward operator, set the prior independently of the truth (for example from the export estimate), tune the hyperparameters on one subset of truth maps and report the error on the others. |
| Status | verified (design as described; quoted source read at arxiv.org) |
| Severity | major |
| Source | SD |

**GB-27 How the synthetic fingerprints, the modified maps, the blended fingerprints and the PCA tracer subsets were produced is not described.**

| Field | Content |
|---|---|
| Check | P8 |
| Location | p. 10, l. 293 to 294; p. 11, l. 332 to 333; p. 12, l. 343 to 344 and l. 355 to 357 |
| Quotation | "the full tracer mineral information from synthetic source fingerprints (Figure 5K)" (l. 293 to 294); "using a geological map with minimal difference from the one used to generate the detrital data" (l. 332 to 333); l. 355 to 356: "We perform a Principal Component Analysis (PCA) to retain the subset of tracers that explain the maximum variance in the mineralogical fingerprints." |
| Concern | The generator of the synthetic fingerprints (random, derived from the measured XRD fingerprints, or other) is not given. Nor is it stated how the minimal-changes map was made and which map is the reference: Section 4 attributes the inferred geology to Bearth (1953) and Steck et al. (2015) (l. 271 to 272), Figure 4 credits Steck et al. (2015) and a personal communication, and scenario 1 uses "the map proposed by (Steck et al., 2015)" as the map with the largest mismatch (l. 333 to 334). The blending rule ("approaching each lithology’s mineral concentration to its mean", l. 343 to 344) gives no formula and no blending factors for the 20 levels. PCA yields components, not tracers, so the rule that turns components into "the top 11 tracers" (l. 357) is missing. Grid dimensions and the number of pixels are not stated (GB-35). None of the four degradation steps can be rebuilt. |
| Suggestion | Add to Section 4.1 the generator of the synthetic fingerprints, which map is the reference and how the modified map was made, the blending formula with the 20 factors, the tracer ranking rule derived from the PCA, and the grid dimensions. |
| Status | verified |
| Severity | moderate |
| Source | SD |

**GB-28 The posterior uncertainties rest on an assumed data standard deviation that is not derived from measurements and is far from the achieved data misfit.**

| Field | Content |
|---|---|
| Check | P31 |
| Location | p. 10, l. 295; p. 1, l. 6 to 7 |
| Quotation | "a data standard deviation of 0.01 mm/y and a prior equal to the average true erosion rate" (l. 295); l. 6 to 7: "while quantifying posterior uncertainty and error propagation" |
| Concern | σd = 0.01 mm/y is a tuning value, not an estimate of XRD measurement error; no replicate measurement is reported (no occurrence of "replicate"). The synthetic runs end with a data misfit of 3.254e6 (Figure 7, forward geology, AB measurement) to about 3.45e6 (Figure 10, row 1) for 21 data. With Eq. (7) this gives a misfit per datum of about 1.6e5 and an RMS residual of 3.9 to 4.1 mm/y, about 400 times σd (Python). The assumed data error is far from the achieved misfit, and the posterior covariance (Eq. 20), which scales with Cd, inherits this choice; the normalised uncertainty also depends strongly on the prior settings (about 1.0 to 0.27 across L, Figure 10, row 1). The same σd is transferred to the natural data (l. 427 to 428), so 0.87, 0.82 and 0.86 are relative numbers under an assumed σd, not quantified uncertainties. The grade is major because the stated aim of quantifying posterior uncertainty and error propagation (l. 6 to 7) is not met while σd is not calibrated. |
| Suggestion | Counter-design: measure replicate diffractograms (repeat scans and split powders of source and detrital samples, several detrital samples taken at the same time) to estimate σd per tracer, check that the misfit per datum at the final iterate is near 1, and report the natural uncertainties with this σd in Section 4.2.2 and in the Abstract. |
| Status | verified (no replicates; σd setting); inferred (misfit per datum and RMS residual from values measured on Figures 7 and 10, Python) |
| Severity | major |
| Source | SD |

**GB-29 Figure 5(b) clips the overshoot at the hotspot that Figure 5(c) contains, and the text describes the match in magnitude as close.**

| Field | Content |
|---|---|
| Check | P3 |
| Location | p. 10, l. 296 to 297; Figure 5 (p. 26), panels (a), (b) and (c); Figure 6 (p. 27), panel (b) |
| Quotation | "The quasi-Newton (QN) approach generates a posterior erosion rate map that closely matches the true erosion pattern, both in spatial distribution and magnitude (Figure 5B)." |
| Concern | The spatial pattern is recovered well: the posterior hotspot in (b) sits where the true hotspot in (a) sits. The magnitude is not shown to match. Measured against the colour scale of (c) (AB, scale minus 2.22 to 2.27), the cell at the hotspot centre reads minus 2.11 and its neighbours minus 2.04 and minus 1.99; with the difference defined as true minus posterior (panel title), the posterior exceeds the true rate by about 2.0 to 2.1 at the centre. The true peak in (a) reads 2.97 to 2.98, so the overshoot is about 70 % of the true peak (2.1 / 3.0, Python). Panel (b) cannot show this, because its colour scale ends at 3.0: the cells at the centre read the top of the scale, and pixels within 40 of the top colour cover 592 px in (a) but 1670 px in (b), 2.8 times more, as a clipped overshoot would. A hatched "Low-confidence areas" spot sits on the hotspot centre in (b), where (c) has its minimum; the text mentions neither. The grade is major because this sentence is the result statement of the forward-inverse test that underpins l. 482 ("the true erosion pattern can be reliably recovered"): if the peak magnitude is off by about 70 %, that claim holds for the pattern, not for the rates. |
| Suggestion | Extend the colour scale of Figure 5(b) and 6(b) to the posterior maximum or mark clipped cells, give the true and posterior peak values in Section 4.1.1, and revise l. 296 to 297 so that it separates spatial pattern from magnitude. |
| Status | verified (colour readings of (a), (b), (c) and the saturated areas by measurement); inferred (overshoot ratio of about 70 %, Python) |
| Severity | major |
| Source | AB |

**GB-30 The comparison of the two inversion schemes is confounded, and the reported error curves do not show that quasi-Newton is more accurate.**

| Field | Content |
|---|---|
| Check | P31, P11 |
| Location | p. 11, l. 320 to 321; Figure 6 (p. 27), panel (g); Figure 5 (p. 26), panel (g) |
| Quotation | "We implement and compare two non-linear inversion schemes (steepest descent and Quasi-Newtonian)" (l. 4 to 5); l. 320 to 321: "Based on these findings, we adopt the Quasi-Newton (QN) approach for all subsequent tests, as it provides a more stable and accurate reconstruction of the erosion rate patterns." |
| Concern | The two schemes differ in more than the update direction: steepest descent uses a normalised gradient that Eq. (18) does not contain (GB-15); it ran 200 iterations (axis of Figure 6), quasi-Newton 100 (l. 293); no step size, iteration number or normalisation is given for steepest descent (parameter sets stated: Section 4.1.1 5 of 6, Section 4.1.2 0 of 6, PP-23); and the step-size sweep (Figure 10, row 4) was run only for quasi-Newton. The text gives no final error, misfit or uncertainty for either scheme. Read on Figures 5(g) and 6(g), the steepest descent error at iteration 200 is about 193.0, while quasi-Newton ends at about 201.0 at iteration 100 with its minimum of about 197.3 near iteration 22; steepest descent is 4.0 % below the quasi-Newton end value and 2.2 % below its minimum (Python). The curves support faster convergence of quasi-Newton, not the claimed greater accuracy; the stability argument (steepest descent needed normalisation) remains. Discussion and Conclusions do not return to the comparison. The grade is major because the comparison of the two schemes is a stated aim of the Abstract and its stated outcome is not supported by the reported curves. |
| Suggestion | Counter-design for Section 4.1.2: run both schemes with the same settings, each with its own tuned step size or a line search, the same stopping rule and the same iteration budget, report error, misfits, normalised uncertainty and run time for each scheme, and rephrase l. 320 to 321 to what the curves show. |
| Status | verified (settings as reported); inferred (end values read on Figures 5(g) and 6(g), Python) |
| Severity | major |
| Source | S3, SD |

**GB-31 The oscillations said to be visible after 125 iterations are not visible in Figure 6, and the comparison is cited as "Figure 6G versus Figure 6G".**

| Field | Content |
|---|---|
| Check | P3, P4 |
| Location | p. 11, l. 316 to 317; Figure 6 (p. 27), panels (g) and (h); Figure 5 (p. 26), panel (h) |
| Quotation | "This limited sensitivity to strong gradients also leads to oscillations in the posterior covariance, visible after 125 iterations, as the Jacobian fluctuates between iterations (Figure 6G versus Figure 6G)." |
| Concern | A panel cannot be compared with itself, and the posterior covariance during the iterations is panel 6(h), not 6(g), which shows the summed difference between true and posterior map. In 6(h) the upper envelope of the markers still rises at iteration 125, reaches its maximum of 0.74259 between iterations 137.8 and 143.3 and then declines monotonically to 0.74249 at iteration 199; within the resolution of 2.0e-5 no oscillation is resolved (AB measurement). Panel 6(g) changes regime at the same place. The figure shows a kink at about 140 iterations, not oscillations from 125 on. The grade is moderate because the statement is used to justify adopting quasi-Newton (l. 320), and the reader cannot check it in the figure. |
| Suggestion | Replace the reference by the intended pair (presumably "Figure 6H versus Figure 5H"), give the iteration of the regime change as it appears in the figure, and if oscillations are meant, show them, for example as an inset of 6(h) after iteration 120. |
| Status | verified (identical targets; panel content and values by measurement); assumption (the intended pair) |
| Severity | moderate |
| Source | AB, S4, S3, SD |

**GB-32 The quantity and the maps of scenario 1 carry different names in the text and in Figure 7.**

| Field | Content |
|---|---|
| Check | P38 |
| Location | p. 11, l. 330, l. 333 to 335 and l. 338 to 339; Figure 7 (p. 28), caption, x-axes, colour bar, map titles and point labels |
| Quotation | "quantified by area mismatch (expressed in m2 )" (l. 330); "the colour on the scatterplot indicates area difference (m2)" (Figure 7 caption); "Geology misalignment (m²)" (Figure 7 colour bar); Figure 7 map title: "Originial geology (same as forward)" |
| Concern | One quantity has three names: area mismatch (three times in the text), area difference (caption and two x-axes) and geology misalignment (colour bar). For the maps the text uses "same geological map", "geological map with minimal difference" and "a simplified geological map with minimal changes" (l. 338 to 339), the figure "Originial geology (same as forward)" (misspelt), "Forward geology", "Geology with minimal changes" and "Minimal changes"; "simplified" adds an attribute that l. 333 and Figure 7 do not give. The citation in l. 333 to 334 is set in parentheses although Steck et al. (2015) is the subject. |
| Suggestion | Use "area mismatch" in the caption, the x-axes and the colour bar; name the three maps identically in l. 332 to 334, l. 338 and Figure 7 (for example "reference map", "modified map", "Steck et al. (2015) map"), correct "Originial", state in l. 333 whether the modified map is simplified, and write "the map proposed by Steck et al. (2015)" in l. 333 to 334. |
| Status | verified (page images p. 11 and p. 28) |
| Severity | minor |
| Source | S2, AB, S3, S4 |

**GB-33 The three blending levels of scenario 2 are named differently in the text, the caption and the panels of Figure 8.**

| Field | Content |
|---|---|
| Check | P38 |
| Location | p. 12, l. 347 to 348; Figure 8 (p. 29), panel titles, point labels and caption |
| Quotation | "1) highly blended, 2) intermediate, and 3) the original synthetic fingerprints" (l. 348); "first the most blended source signatures, then the half-way in between source signatures, and then the original synthetic fingerprints" (Figure 8 caption); Figure 8 panel title: "Almost fully blended (avg. JS = 0.225)" |
| Concern | Each level carries three names: highly blended, most blended, almost fully blended; intermediate, half-way in between, medium blended; original synthetic, unblended. The JS values that identify the levels appear only in the panel titles, not in the text. |
| Suggestion | Use one set of names in l. 348, the caption and the panels of Figure 8, and give the average JS distance of the three examples in l. 347 to 349. |
| Status | verified (page images p. 12 and p. 29) |
| Severity | minor |
| Source | S2 |

**GB-34 Twenty blending levels are reported as tested, but Figure 8 shows fourteen, and the caption accounts for one missing run.**

| Field | Content |
|---|---|
| Check | P23, P9, P3 |
| Location | p. 12, l. 348 to 349 and l. 353; Figure 8 (p. 29), all three scatterplots and caption |
| Quotation | "In total, 20 values between the highly blended and the original synthetic fingerprints are tested" (l. 348 to 349); Figure 8 caption: "Note that the most blended example did not have a stable solution and is therefore not plotted." |
| Concern | Fourteen markers were counted in the error panel and in the uncertainty panel (AB with a marker script; S3 and SD at enlarged page images), at JS 0.249, 0.272, 0.338, 0.359 and ten values from 0.440 to 0.624 in steps of about 0.020 (±0.001); values near 0.29 to 0.32 and 0.38 to 0.42 are missing. Balance: 20 tested minus 14 plotted is 6 missing (30 %), of which the caption explains one (avg. JS 0.225), so 5 are unaccounted for. Resolutions: (A) five further runs did not converge, which fits "In many of these cases, the inversion fails to converge" (l. 353) but contradicts a caption that names one; (B) points overlap, unlikely because all 14 positions are distinct in both panels; (C) the runs were omitted for another reason. If the missing runs failed, the plotted curve shows only converged runs and understates the failure rate below 0.55. |
| Suggestion | Plot all 20 levels with non-converged runs marked by a distinct symbol, and state in l. 353 or the caption how many and which levels failed, with their JS values. |
| Status | verified (count on the page image); inferred (resolutions) |
| Severity | moderate |
| Source | S3, AB, SD |

**GB-35 The threshold "errors exceeding 700 mm/yr" does not match the error axis of Figure 8, and the error is a sum over an unstated number of pixels reported in the unit of a single rate.**

| Field | Content |
|---|---|
| Check | P3, P20 |
| Location | p. 12, l. 351 to 353; Figure 8 (p. 29), left scatterplot; Figure 5 (p. 26), panel (g); Figures 7, 9 and 10 (p. 28, 30, 31), error axes |
| Quotation | "As the JS distance decreases below 0.55, both absolute error and posterior uncertainty rise sharply, with errors exceeding 700 mm/yr" |
| Concern | The axis of the absolute-error panel runs to 700000. Measured values (AB, each ±1400): JS 0.249: 47500; 0.272: 676400; 0.338: 5970; 0.359: 322100; 0.461: 1390; 0.481: 1250; 0.501: 9030; 0.521: 4170; 0.541: 19580; 0.561: 690; 0.581 and 0.602: 560; 0.624: 280. The errors below JS 0.44 exceed 700 by one to three orders of magnitude, and values above 700 already occur at JS 0.50 and 0.54, so 700 does not mark the transition at 0.44; the number coincides with the top tick label 700000. Does "700 mm/yr" refer to 700000 on the axis? The plotted quantity is a sum over pixels of absolute differences between true and posterior rates (axis labels of Figures 5(g) and 7 to 10). A sum scales with the number of pixels, which the manuscript never states (only the pixel size of 300 m is derivable, PP-16), and it does not carry the unit of a single rate, whereas the "extreme erosion rate values" of l. 435 are single-pixel maxima. The true map of Figure 5(a) peaks at about 3 on a colour bar without unit. The unit "mm/yr" also differs from "mm/y" used elsewhere. The threshold at 0.55 is borne out for the uncertainty (PP-27). |
| Suggestion | State the number of pixels and the mean true erosion rate in Section 4.1.1; give quantity and unit on the error axes of Figures 5(g) and 7 to 10, preferably as mean absolute error per pixel; correct l. 352 to 353 to the measured values or explain what 700 refers to; write "mm/y". |
| Status | verified (values by measurement; missing pixel count); assumption (that 700 was read from the tick label 700000), posed as a question |
| Severity | moderate |
| Source | AB, S3, S2, S4 |

**GB-36 Data misfits are compared across runs with different numbers of tracers without normalisation, so the drop in data misfit with fewer tracers may only reflect fewer summed terms.**

| Field | Content |
|---|---|
| Check | P21 |
| Location | p. 12, l. 360 to 362; Figure 9 (p. 30), third panel |
| Quotation | "However, when the number of tracers drops below 7, the absolute error increases rapidly, as does the posterior uncertainty, while the data misfit and model misfit drop." |
| Concern | The data misfit of Eq. (7) is a sum over the m data weighted by 1/σd². With fewer tracers there are fewer terms, so the absolute data misfit falls even if the fit per datum is unchanged. Read from the axis ticks of Figure 9, the data misfit is about 3.25e6 for 21 tracers and about 1.55e6 for 11 tracers, a ratio of 2.1, close to the tracer ratio 21/11 = 1.91. The same issue applies to any comparison of the combined natural dataset (34 tracers) with the single datasets (13 or 21 tracers). |
| Suggestion | Report the data misfit per datum (divided by m) or as a reduced chi-square in Section 4.1.3 and Figure 9, and use the same normalisation for natural datasets of different size. |
| Status | verified (absence of normalisation in Eq. 7); inferred (proportionality from axis tick reading, Python) |
| Severity | moderate |
| Source | S3 |

**GB-37 The ranking of the three degradation factors is stated without numbers and compares perturbations of non-commensurate size.**

| Field | Content |
|---|---|
| Check | P21, P10 |
| Location | p. 12, l. 363 to 365 |
| Quotation | "To summarize, among the three tested scenarios, the strongest impact on the posterior solution arises from reduced fingerprint distinctiveness. Geological map uncertainty follows as the second most influential factor." |
| Concern | The scenarios differ in number and range of perturbations: 3 maps (Figure 7), 20 blending levels (Figure 8, reaching almost fully blended fingerprints with non-convergent runs) and 21 tracer counts (Figure 9). On the error scale measured by AB, the largest increase over the reference case is 77.3 (39.1 %) for the map scenario (197.5 to 274.8) and 151.0 (76.5 %) for the tracer scenario (197.4 to 348.4 at 2 tracers), and up to 676400 for blending, driven by unstable runs (Python). Tracer reduction thus ranks above map uncertainty at its extreme; the ranking holds only under the condition of l. 365 that the informative tracers are retained, a condition not applied to the map scenario. With three maps no trend with mismatch can be established, and the minimal-changes map breaks the trend stated in l. 337 to 338 (disclosed, PP-24). The ranking therefore reflects the chosen perturbation ranges and the inclusion of non-converged runs rather than the effect per comparable perturbation. |
| Suggestion | Express each perturbation on a common scale in Section 4.1.3 (for example change in average JS distance or fraction of a plausible range), separate converged from non-converged runs, test more than three maps, and restrict the ranking in l. 363 to 365 and the recommendations in l. 456 to 461 to what these numbers support. |
| Status | verified (absence of numbers; run counts); inferred (increases from values measured on Figures 7 to 9, Python) |
| Severity | moderate |
| Source | S3, SD |

**GB-38 The statement on smoothing distances beyond 3000 m has no plotted case, and the two sentences on long smoothing distances contradict each other.**

| Field | Content |
|---|---|
| Check | P11, P3 |
| Location | p. 12, l. 372 to p. 13, l. 376; Figure 10 (p. 31), row 1 |
| Quotation | "However, beyond approximately 10 times the pixel size (3000 m), the solution becomes overly smooth, causing the posterior to deviate from the true erosion rates." (l. 373 to 374); l. 374 to 375: "A longer smoothing distance effectively constrains the posterior closer to the prior (set here as the average true erosion rate) resulting in a reduced difference between posterior and true values" |
| Concern | Row 1 of Figure 10 has 20 points from 200 m to 3000 m; the summed difference falls monotonically from 257.1 to 76.1, with the lowest value at the last tested point, 3000 m, and axis and colour bar end at 3000 (AB measurement). No case beyond 3000 m is shown, so the figure cannot show the deviation that l. 373 to 374 reports. The next sentence states that a longer smoothing distance reduces the difference between posterior and true values, the opposite of the preceding claim for the same range. At the L used in all tests (1200 m) the error is about 195, 155 % above the value at 3000 m (SD reading, Python); the choice of 1200 m is not explained (GB-53). |
| Suggestion | Extend the smoothing sweep beyond 3000 m or remove the claim in l. 373 to 374, and reconcile it with l. 374 to 376. |
| Status | verified (point positions and values by measurement; contradiction between the sentences) |
| Severity | moderate |
| Source | S3, AB, SD |

**GB-39 The text describes the data standard deviation sweep with large effects, a minimum and a plateau that Figure 10 does not show.**

| Field | Content |
|---|---|
| Check | P3, P21 |
| Location | p. 13, l. 380 to 384; Figure 10 (p. 31), row 3 |
| Quotation | "Very low data standard deviation values lead to large differences between the posterior and true erosion rate maps, likely due to overfitting or unstable gradients. As data standard deviation increases, the absolute difference first decreases to a minimum, then rises to a plateau at higher values." (l. 380 to 382); l. 383 to 384: "Beyond a data standard deviation of approximately 10-2 mm/y, model misfit begins to decrease rapidly while data misfit stabilizes." |
| Concern | In row 3, column 1 (axis offset +1.974e2) the summed difference rises monotonically from 197.4197 at the smallest σd to 197.4431 at σd = 0.89 mm/y (±0.0001, AB measurement): there are no large values at low σd, no minimum and no plateau, and the whole range is 0.0234, or 0.0119 % of the value (Python). In column 3 the model misfit spans 1.56141 to 1.56232, a change of 0.06 %, which the text calls "begins to decrease rapidly"; the normalised uncertainty spans 0.74015 to 0.74040. Lines 380 to 384 may describe another run or another axis range. "10-2" is set without superscript. The grade is moderate because the choice of σd = 0.01 mm/y for all later tests is justified by this sweep. |
| Suggestion | Replace the description in l. 380 to 384 by what row 3 shows (σd has practically no effect on the error in the tested range) or show the run the text describes, for example on a logarithmic σd axis down to 1e-3 mm/y; give absolute and relative changes; set 10⁻² with a superscript. |
| Status | verified (values by measurement on the page image p. 31) |
| Severity | moderate |
| Source | AB, S3, S4, SD |

**GB-40 The mineral list names "Chrysolite", while line 274 and Figures 11, 15 and 16 name "Chrysotile"; the two names denote different minerals.**

| Field | Content |
|---|---|
| Check | P38 |
| Location | p. 13, l. 395; Figure 11 (p. 32), row label; Figure 15 (p. 36) and Figure 16 (p. 37), axis labels |
| Quotation | "Dolomite, Diopside, Chrysolite, Antigorite, Anorthite" (l. 395); l. 274: "serpentinites (predominantly antigorite and chrysotile)" |
| Concern | The 21 target minerals in l. 393 to 396 and the labels of Figure 11 agree in 20 of 21 names (Python set comparison: text minus Figure 11 is Chrysolite, Figure 11 minus text is Chrysotile; Figures 11 and 15 carry identical sets). Chrysotile is a serpentine mineral, as l. 274 states for the serpentinites; chrysolite denotes gem-quality olivine (Wikipedia contributors, 'Chrysolite', https://en.wikipedia.org/wiki/Chrysolite, read by S2). Because the diagnostic windows are taken from RRUFF reference spectra per mineral (l. 257 to 258), the name decides which reference spectrum a reader would use to rebuild the fingerprint. The grade is moderate (reproducibility); the result is unchanged if the figures are right. |
| Suggestion | Replace "Chrysolite" by "Chrysotile" in l. 395, or, if the olivine variety was meant, correct the figure labels and explain the choice; in either case name the RRUFF reference spectrum used for this tracer. |
| Status | verified (page images p. 10, 13, 32, 36, 37; meaning of chrysolite in the cited source) |
| Severity | moderate |
| Source | S2, S3, S4, AB, SD |

**GB-41 The natural XRD fingerprints are declared robust and valid on a qualitative agreement with the literature, without a criterion or an independent check.**

| Field | Content |
|---|---|
| Check | P32 |
| Location | p. 13, l. 399 to 401; Figure 11 (p. 32) |
| Quotation | "The mineralogical fingerprints derived from processed and binned XRD data align well with established knowledge of the lithology in the Gorner Glacier catchment (Bearth, 1953; Steck et al., 2015)" |
| Concern | The terms "robustness" and "validity" (l. 400 to 401) are inferred from a visual comparison: no criterion for "align well" is given, no replicate measurement, and no comparison with an independent mineral quantification (for example Rietveld analysis or modal counts) of a subset of samples. Figure 11 raises questions that such a criterion would answer: the Monte Rosa granite column shows Tremolite at 0.893 and the Furgg series at 1.000, and the serpentinite column shows no quartz (AB measurement), while l. 276 describes the Monte Rosa nappe as granites, granite gneisses and garnet-mica schists. Is tremolite expected in the Monte Rosa granite? The rate at which the processing chain mis-assigns minerals is unknown (see also GB-19). |
| Suggestion | In Section 4.2 give expected and observed dominant minerals per unit in a table with an explicit agreement criterion, or quantify the agreement for a subset of source samples against an independent method. |
| Status | verified (qualitative basis in the text; bar values by measurement); assumption (expected tremolite content), posed as a question |
| Severity | moderate |
| Source | SD, AB |

**GB-42 The natural known-mixture analogue tests one of seven units, does not show which units lie inside the subcatchment, and pools an unstated number of samples, so it cannot show that erosion is attributed only to units present.**

| Field | Content |
|---|---|
| Check | P10, P20, P3, P4, P24 |
| Location | p. 14, l. 410 to 418; Figure 12 (p. 33), map and caption; Figure 13 (p. 34), inset, ridges and caption |
| Quotation | "If the XRD fingerprinting method is robust, the inversion should attribute erosion only to lithologies present within the sub-catchment." (l. 410 to 411); "Merging the inversion results from multiple detrital samples collected at the sink of this sub-catchment" (l. 413); l. 414 to 415: "Some spillover occurs from adjacent lithologies, but the overall pattern confirms that the inversion respects geological boundaries" |
| Concern | The design is a sensible natural analogue of a known-mixture test, and the ZSF sediments curve does what the text says (peak at 0.00 mm/y, half height at 0.13 mm/y; AB measurement). The comparison that would make it a test is missing. (1) Only 1 of 7 units (14 %) is absent from the subcatchment, and the manuscript names this unit as small and poorly resolved (l. 299 to 300); the KDEs of the Furgg series and the serpentinites, both present, also peak near 0 mm/y, so a near-zero peak does not separate an absent unit from a weakly resolved one. (2) Figure 12, cited for the outcrop argument (l. 411 to 412), draws no subcatchment boundary; the subcatchment is shown only by stronger colours without legend. Inside the dashed boundary of the inset of Figure 13 (filled polygon, 53927 px) the green of the metabasite unit covers 0.00 % (pink 65.3 %, orange 20.3 %, light green 10.6 %, yellow 3.8 %), and in Figure 12 the metabasite outcrop colour occurs inside the subcatchment in three specks of together about 0.002 km²; yet the metabasite ridge peaks at 0.28 mm/y and stays above half height up to 1.05 mm/y (AB measurement). (3) Each KDE pools "all pixels within each lithological unit" (Figure 13 caption), inside and outside the subcatchment, so attribution inside and spillover outside cannot be separated; the caption also reads peak height as consistency across inversions, although the spread is over pixels and inversions together. (4) The expectation is phrased for lithologies "present within the sub-catchment", but the excluded unit is defined by outcrops (l. 411), while A uses the inferred map of the whole catchment (l. 408). (5) The number, dates and times of the "multiple detrital samples", the number of inversions and the inversion parameters (0 of 6 settings, PP-23) are not given, and "close to zero" and "Some spillover" are not quantified. Question to the authors: is the metabasite unit counted as present because of the outcrop specks? The grade is major because the test answers the second natural-data aim (l. 283 to 284); as designed and shown it cannot separate the two readings, so the conclusion of l. 415 to 418 is not shown. |
| Suggestion | Counter-design for Section 4.2.1: draw the subcatchment boundary in Figure 12 and give the area of each mapped unit inside it; give number, dates and times of the samples and inversions and the parameter set; report per unit the median posterior rate and the fraction of total posterior sediment flux attributed to pixels outside the subcatchment, with KDEs split into pixels inside and outside; compare with a prior-only run to show that the near-zero values are data-driven; define "close to zero" numerically; and add a laboratory known-mixture test with source powders (l. 404 to 406). |
| Status | verified (text; shares, areas and KDE positions by measurement on the page images p. 33 and p. 34); inferred (pooled KDEs cannot separate spillover from attribution inside); assumption (why the metabasite unit counts as present), posed as a question |
| Severity | major |
| Source | S3, S4, AB, SD |

**GB-43 The zircon comparison is introduced as applied "to the same detrital sample", but the XRD data are later said to come from "a detrital sample taken at the same date and time".**

| Field | Content |
|---|---|
| Check | P38, P2 |
| Location | p. 14, l. 420 to 421 and l. 437 to 438 |
| Quotation | "we compare it against a zircon-based fingerprinting approach applied to the same detrital sample" (l. 420 to 421); l. 437 to 438: "the XRD-derived dataset acquired from a detrital sample taken at the same date and time" |
| Concern | l. 421 indicates one sample analysed with both methods; l. 437 to 438 ("a detrital sample", "at the same date and time") indicates a second sample taken simultaneously, possibly with a different volume or grain-size fraction for zircon separation and XRD powder. If two samples were used, differences between the zircon and XRD solutions can arise from sampling as well as from the method, and the benchmark of Section 4.2.2 cannot separate the two causes; the two readings also differ in how the concatenated detrital vector (l. 443 to 444) is formed. |
| Suggestion | Could the authors state in l. 420 to 424 whether the zircon and XRD data come from splits of one sample or from two samples, and if two, identify both and give mass and grain-size fraction? |
| Status | verified (wording, page image p. 14); assumption (which reading is correct), posed as a question |
| Severity | moderate |
| Source | S2, S3 |

**GB-44 For the natural inversions the prior is "the average true erosion rate", which does not exist for natural data, and the sediment export estimate that scales all rates is never given.**

| Field | Content |
|---|---|
| Check | P25, P12, P22 |
| Location | p. 14, l. 428; p. 3, l. 65 to 66; p. 15, l. 453 |
| Quotation | "a data standard deviation of 0.01 mm/y, a prior equal to the average true erosion rate, and a step size µ of 0.1" (l. 427 to 428); "For simplicity, we redefine the data vector d as scaled by the total erosion rate" (l. 159); l. 453 to 454: "an estimate of the total annual suspended sediment export from the catchment" |
| Concern | The prior definition is carried over from the synthetic tests, where a true map exists; for the zircon, XRD and combined runs (l. 426 to 428, l. 445) the stated prior cannot have been computed. Eq. (2) scales d by the sum of the pixel erosion rates, which is the unknown. The manuscript lists "an estimate of the total annual suspended sediment export" as one of four key inputs (l. 65 to 66, l. 452 to 454), as integrated in the Conclusions (l. 479 to 480), and names "multi-year suspended sediment datasets" as the reason for choosing the site (l. 267 to 268). A search of p. 1 to 21 for "export", "annual", "yearly" and "multi-year" returns only these passages: none gives a value, period, method, operator or reference, the data statement (l. 490) does not mention them, and the conversion from export to the sum in Eq. (2) is not stated. With a normalised posterior uncertainty of 0.82 to 0.87 the posterior stays close to the prior, so prior and scaling largely set the natural rate magnitudes (more than 8000 mm/y in Figure 14). The grade is major: the natural erosion rate maps can be neither read as data-driven nor reproduced while prior and scaling are undefined. |
| Suggestion | In Section 4.2 state the prior used for each natural run and how it was obtained, the export value with period, derivation and source, and its conversion to Eq. (2); state in the data statement (l. 490) whether these data are in the Zenodo record or are third-party data with a reference; add a sensitivity run of the natural inversions with the prior changed by factors of 0.1 and 10. |
| Status | verified (text; absence on p. 1 to 21 and in l. 490) |
| Severity | major |
| Source | S2, S3, SD |

**GB-45 The zircon benchmark is confounded by missing and copied zircon source data and rests on one sample date without ground truth, so it cannot assess the "accuracy" named in the aim; the copied fingerprint is not marked in the figures.**

| Field | Content |
|---|---|
| Check | P9, P27, P37 |
| Location | p. 14, l. 430 to 434; p. 10, l. 285; Figure 14 (p. 35) and Figure 16 (p. 37), fingerprint panels and captions |
| Quotation | "zircon data were not available for two lithological units" (l. 430); "we assigned the MR g-g unit the same zircon-age fingerprint as the Monte Rosa granite unit" (l. 433 to 434); l. 284 to 285: "to assess how the incorporation of XRD-based fingerprints alongside zircon data improves the stability and accuracy of the posterior solution" |
| Concern | The manuscript discloses the gaps and the substitution, which is to its credit; their consequence for the benchmark is not drawn. The zircon matrix lacks one unit (no zircon in the ZSF metabasites and eclogites), has a copied column for MR g-g, and has very low zircon contents in the serpentinites (l. 430 to 434); the MR gneiss and MR granite segments are equal in all 11 shared age bins (PP-34). Two identical columns prevent the zircon and combined inversions from separating MR granite and MR g-g by construction. The instability of the zircon-only run (more than 8000 mm/y, l. 435) can follow from these data gaps rather than from the zircon method, so the comparison does not isolate method performance. How a unit without zircon enters A (zero column or omitted) is not stated. One sample date is compared (sample identity: GB-43). Without a known truth, accuracy cannot be assessed; only stability is measured. The captions of Figures 14 and 16 present all fingerprints as data, so a reader of the figures cannot see that one column is copied. The grade is major because the test answers the third natural-data aim. |
| Suggestion | Counter-design for Section 4.2.2: compare the two methods on the units for which both have data (restricting A accordingly) and on several detrital samples, judge accuracy against an independent constraint (the subcatchment test or laboratory mixtures) or remove "accuracy" from l. 285; state how units without zircon enter A; add to the captions of Figures 14 and 16 that the MR g-g zircon fingerprint is copied from MR granite. |
| Status | verified |
| Severity | major |
| Source | SD |

**GB-46 For the natural inversions the announced evaluation metrics are reported unevenly, and data and model misfits are reported for none of them.**

| Field | Content |
|---|---|
| Check | P11 |
| Location | p. 14, l. 435 to 436; p. 15, l. 442 and l. 447 to 448 |
| Quotation | "Furthermore, one must evaluate the data- and model misfit (eq. 7)." (l. 240); l. 447 to 448: "the average Jensen-Shannon distance between source fingerprints increases from 0.48 to 0.57" |
| Concern | Reported quantities per natural case: zircon only, normalised uncertainty 0.87, resolution "low" (qualitative), maximum rate above 8000 mm/y, JS 0.48 (given only in the paragraph on the combined run), no misfits; XRD only, 0.82, resolution and maximum only in the figure, no JS, no misfits; combined, 0.86, resolution and maximum only in the figure, JS 0.57, no misfits; Gorner-Grenz subcatchment, KDEs only. Section 3.3 introduces data and model misfit as required evaluation and as the stopping criterion (l. 240, l. 243 to 244), yet no natural inversion reports them, so the fit of the XRD solution to the observed detrital data cannot be judged. The first natural aim (l. 282 to 283) is answered only qualitatively (GB-41). The grade is moderate; it would become major if the missing misfits showed a poor fit. |
| Suggestion | Add a table to Section 4.2 with one row per natural inversion (subcatchment samples, zircon, XRD, combined) and the columns normalised posterior uncertainty, mean resolution, maximum erosion rate, average JS distance, final data misfit, final model misfit and iterations reached. |
| Status | verified (gaps; Section 4.2 read in full) |
| Severity | moderate |
| Source | S3 |

**GB-47 The combined zircon and XRD inversion is presented as a further improvement, but its normalised posterior uncertainty (0.86) is higher than that of the XRD-only inversion (0.82).**

| Field | Content |
|---|---|
| Check | P2, P15, P31 |
| Location | p. 15, l. 446 to 447; p. 15, l. 461 to 462; p. 3, l. 72 to 73; twin p. 5, l. 139 to 140 |
| Quotation | "Adding XRD data to the zircon dataset stabilizes the inversion and improves the posterior solution. The normalized posterior uncertainty decreases slightly to 0.86 (from 0.87 in the zircon-only case)" (l. 446 to 447); "The normalized posterior uncertainty is slightly lower at 0.82." (l. 441 to 442); "combining XRD data with other fingerprint data such as zircon data, proves to further stabilize and improve the posterior solution" (l. 461 to 462); l. 72 to 73: "showing that integrating XRD with zircon data improves the stability and sharpness of the posterior solution" |
| Concern | The Results compare the combined run only with zircon-only, and against that reference the statement holds: (0.86 minus 0.87) / 0.87 = minus 1.15 %. Against XRD-only the combined run is worse on the same metric: (0.86 minus 0.82) / 0.82 = plus 4.88 %, an absolute increase of 0.04, four times the improvement over zircon (Python). The three values agree between text and figure labels (PP-35), so this is not a transcription error but a framing that depends on the reference. The colour bar of the posterior rate ends at about 8 mm/y for XRD-only (Figure 15) and about 12 mm/y for the combination (Figure 16). "further stabilize" (l. 462) and "integrating XRD with zircon data improves" (l. 72 to 73) read as improvements over XRD alone, which the numbers do not show; "proves" rests on one sample date; "sharpness" (l. 73) is measured nowhere; only the JS distance (0.48 to 0.57) favours the combination, without an XRD-only value (GB-48). The grade is major because the comparison is the third natural-data aim (l. 284 to 285); on the reported metric the combination is not better than XRD alone, so the claim must be restricted to the zircon-only reference. |
| Suggestion | In l. 446 to 449 state that the combined run improves on zircon-only but not on XRD-only in normalised uncertainty; revise l. 72 to 73, l. 139 to 140 and l. 461 to 463 accordingly, replace "proves" by "suggests", and either define and report a stability measure for all three runs or remove "sharpness". |
| Status | verified (values and quotations at the page images and figure labels); inferred (relative changes, Python) |
| Severity | major |
| Source | S3, S4, SD |

**GB-48 The average Jensen-Shannon distances of the natural datasets are given without their base, without the XRD-only value and without the normalisation that makes fingerprints probability distributions.**

| Field | Content |
|---|---|
| Check | P20 |
| Location | p. 15, l. 447 to 448; p. 12, l. 346 to 347 |
| Quotation | "We compute the JS distance between all pairs of source XRD signatures and use the average across all combinations." (l. 346 to 347); l. 345 to 346: "which measures the similarity between two probability distributions" |
| Concern | With seven units the average runs over 21 pairs. For zircon one unit has no fingerprint, and one pair (MR g-g, MR granite) has distance zero by construction; if the metabasite unit is excluded, there are 15 pairs, and the other 14 must average 0.48 × 15 / 14 = 0.514 to give 0.48 (Python). How the unit without zircon enters the zircon average and the concatenated matrix (34 tracers: 21 minerals and 13 age bins, Figure 16) is not stated. The XRD-only value is missing, so the reader cannot tell whether concatenation raises or lowers distinguishability relative to XRD alone, nor whether the natural XRD case lies above the threshold of 0.55 that the manuscript defines (l. 352; GB-59). The zircon value 0.48 lies in the range where the synthetic tests report sharply rising errors, and the natural values are not related to the synthetic thresholds or to the unblended synthetic value 0.624 (Figure 8). The JS distance requires probability distributions, but the fingerprints are normalised by their maximum (l. 261), not to unit sum; the normalisation used for the JS computation and the comparability of vectors with 13, 21 and 34 bins are not stated. |
| Suggestion | State in Section 4.2.2 the number of units and pairs behind each average, how the metabasite unit and the duplicated MR fingerprint were treated, the normalisation used for the JS computation and the XRD-only value, and relate the natural values to the thresholds of Section 4.1.3. |
| Status | verified (missing base, missing value, normalisation in l. 261); inferred (pair counts and 0.514, Python) |
| Severity | moderate |
| Source | S3 |

**GB-49 Units and axis labels are missing in Figures 5, 6 and 13.**

| Field | Content |
|---|---|
| Check | P29 |
| Location | Figure 5 (p. 26), colour bars (a) to (f) and panels (g), (h); Figure 6 (p. 27), colour bars and panels (g), (h), (i); Figure 13 (p. 34), upper panel |
| Quotation | "(e) Posterior covariance diagonal" |
| Concern | The colour bars of Figures 5(a) to (f) and 6(a) to (f) carry numbers without units (erosion rates, differences, covariance), whereas the maps of Figures 14 to 16 give "(mm/y)". The y-axis of 5(g) has no unit and 5(h) no axis label. In Figure 6 the panels (g), (h) and (i) have no x-axis labels, the colour bar of (i) has no label, and the data-misfit axis of (i) (0.0 to 2.0) has no scale factor, whereas Figure 5(i) shows "1e8". In Figure 13 the upper ridges have a density axis without numbers, and the x-axis ends at 3.3 mm/y although the Stockhorn ridge still stands above its baseline there (AB measurement). Quantity and unit of the error axes and of the uncertainty axes are treated in GB-35 and GB-16. |
| Suggestion | Add units and labels to all colour bars and axes of Figures 5 and 6, give the scale factor in Figure 6(i), add a density scale to the upper panel of Figure 13 and extend its x-axis or note the truncation. |
| Status | verified (page images p. 26, 27, 34) |
| Severity | minor |
| Source | AB |

**GB-50 The hatched "Low-confidence area" in five figures is defined nowhere, and in Figures 14 and 15 it covers the erosion maxima that the text interprets.**

| Field | Content |
|---|---|
| Check | P29, P8 |
| Location | Figure 5 (p. 26), panel (b); Figure 6 (p. 27), panel (b) and hatch swatch; Figures 14 to 16 (p. 35 to 37), map panels and legend |
| Quotation | "Low-confidence areas" (Figure 5 legend); l. 440 to 441: "the XRD solution identifies the main erosion peak in the center of the domain" |
| Concern | The word "confidence" does not occur in the text (search of p. 1 to 16); neither Section 3.3 nor the captions say which criterion marks a cell as low-confidence. In Figure 6 the hatch swatch has no label, and in Figures 14 to 16 the legend reads "Low-con dence area" with the fi ligature lost (page image p. 35). In Figure 15 the hatch lies on the cells of highest colour, the peak that l. 440 to 441 calls the main erosion peak; in Figure 14 it covers the hotspot whose cells read 8360 to 8510 mm/y; in Figure 5(b) it sits on the hotspot centre where 5(c) shows the largest difference (GB-29; AB measurement). The flag apparently marks the cells the text relies on, without the text saying so. |
| Suggestion | Define the low-confidence criterion (metric and threshold) in Section 3.3 and in the captions, label the swatch in Figure 6, set "Low-confidence area" in full in Figures 14 to 16, and discuss in l. 439 to 449 that the interpreted peaks are flagged. |
| Status | verified (absence of a definition; position of the hatch by measurement); assumption (what the flag means) |
| Severity | moderate |
| Source | AB, SD |

**GB-51 The bar colours in Figures 5(k), 15 and 16 do not match their legend swatches, and two of them match the swatch of another lithology.**

| Field | Content |
|---|---|
| Check | P3 |
| Location | Figure 5 (p. 26), panels (j) and (k); Figure 15 (p. 36), legend and stacked bars; Figure 16 (p. 37), legend and stacked bars; Figures 8 and 9 (p. 29, 30), top rows |
| Quotation | "S.,T.,G."; "MR gneiss, mica"; "MR granite" |
| Concern | Measured legend swatches (AB): serpentinites #e4dc1c, ZSF sediments #849c44, S.,T.,G. #fc5404, MR granite #fc9c9c, metabasites #34a42c, MR gneiss #fc7c44, Furgg #bcdc6c (Figures 5 and 15 identical). The bars use lighter colours (#ece45c, #a4b47c, #fc844c, #fcbcbc, #74bc6c, #fca47c, #cce494 in Figure 15; Figure 5(k) agrees within 8), with differences from their own swatches of 64 to 152. The Stockhorn bar colour #fc844c lies 16 from the "MR gneiss, mica" swatch, and the MR gneiss bar colour #fca47c lies 40 from the "MR granite" swatch. Which bar colour belongs to which unit follows only from Figure 14 and Figure 11, not from the legend; a reader matching colours to the legend assigns Stockhorn segments to MR gneiss and MR gneiss segments to MR granite. The grade is moderate because the source fingerprints are a result of Section 4.2 and cannot be read correctly from the legend. |
| Suggestion | Draw legend swatches and bars in the same colours and transparency, or add a legend that shows the bar colours. |
| Status | verified (colours measured on the page images) |
| Severity | moderate |
| Source | AB |

**GB-52 The x-axis of the tracer-count scatterplots in Figure 9 is labelled with the JS distance, and two further labels of the figure are faulty.**

| Field | Content |
|---|---|
| Check | P29, P38 |
| Location | Figure 9 (p. 30), x-axes of the left and middle scatterplots, colour bar and y-axis label of the left scatterplot |
| Quotation | "Avg. JS distance between lithologies" (Figure 9, x-axes); Figure 9, colour bar: "Number of tracrs" |
| Concern | The axis runs from 0.0 to 20.0; the 21 markers sit at 1.02, 2.02 and so on to 21.02 (spacing 1.00), and the labels "1 tracer", "11 tracers" and "All" sit at 1.02, 11.02 and 21.02 (AB measurement). The plotted variable is therefore the tracer count described in l. 355 to 359 and named on the colour bar; the label repeats that of Figure 8. The colour bar label is misspelt, and the y-axis label of the left scatterplot carries a second, clipped Σ. |
| Suggestion | Relabel the x-axes of both panels "Number of tracers", correct the colour bar label to "Number of tracers", and delete the stray Σ. |
| Status | verified (page image p. 30; positions by measurement) |
| Severity | minor |
| Source | S2, AB |

**GB-53 The highlighted points in Figure 10 are not explained, three of them differ from the parameters used, and the selection rule for the "optimized" hyperparameters is not stated.**

| Field | Content |
|---|---|
| Check | P2, P29, P5 |
| Location | Figure 10 (p. 31), third column, rows 1 to 5, and row 1; p. 3, l. 70 |
| Quotation | "Through forward-inverse testing, we optimize the hyper-parameters" (l. 70); l. 427 to 428: "smoothing distance of 4 times the pixel size (L = 1200 m), a model standard deviation of 3 (dimensionless), a data standard deviation of 0.01 mm/y" |
| Concern | Each trade-off panel highlights one point with a thick circle and a label: "L = 3000 m", "σm = 6.2", "σd = 0.003 mm/y", "µ = 0.1" and "n_m = 25". The caption does not say what the highlighted point denotes. Two labels agree with the settings of Sections 4.1.3 and 4.2.2 (µ = 0.1, 25 iterations); three do not (L 3000 m against 1200 m, ratio 2.5; σm 6.2 against 3, ratio 2.07; σd 0.003 against 0.01 mm/y, ratio 0.3; Python). The text calls µ = 0.1 optimal (l. 385), which suggests that the labels mark selected or optimal values. The L used in the tests (1200 m) is not a point of the sweep in row 1, whose points lie at 200 m plus multiples of 147.4 m, among them 1084 m and 1232 m (AB measurement). The Introduction announces an optimisation (l. 70), but no selection rule is stated; "n_m" is unrendered notation. A reader reproducing the tests cannot tell which parameter set the authors consider optimal. |
| Suggestion | State in the caption of Figure 10 and in Section 4.1.4 (l. 370 to 371) what the highlighted points are and the selection rule for each hyperparameter, mark the values actually used in each row, include L = 1200 m in the sweep, and either use the marked values in Sections 4.1.1 to 4.2.2 or justify L = 1200 m, σm = 3 and σd = 0.01 mm/y. |
| Status | verified (labels, sweep positions and text values); assumption (meaning of the labels), posed as a question |
| Severity | moderate |
| Source | S3, AB, SD |

**GB-54 The lettering of Figure 10 is below 6 pt in print size.**

| Field | Content |
|---|---|
| Check | P29 |
| Location | Figure 10 (p. 31), all panels; for comparison Figures 11, 14, 15 and 16 (p. 32, 35 to 37) |
| Quotation | "Data standard deviation (mm/y)" |
| Concern | Cap heights measured at 300 dpi (AB): axis numbers 11 px = 3.7 pt, axis titles 12 px = 4.0 pt, panel titles 14 px = 4.7 pt, all below 6 pt by more than the measuring uncertainty of about 0.6 pt. Labels in Figures 11, 14 and 15 measure 5.3 pt, just below the limit. |
| Suggestion | Enlarge the lettering in Figure 10 to at least 6 pt, for example by splitting it into two figures, and raise the labels in Figures 11, 14, 15 and 16 slightly. |
| Status | verified (measurement on the page images) |
| Severity | minor |
| Source | AB |

#### Minor corrections

| ID | Location | Quotation | Replacement | Source |
|---|---|---|---|---|
| KK-18 | p. 10, l. 295 | "as epsilon is dimensionless" | "as ε is dimensionless" | S3 |
| KK-19 | p. 11, l. 307; Figure 5 (p. 26) and Figure 6 (p. 27), captions | "the model’s "greedy" optimisation strategy"; "(a) "true" erosion map" (straight quotation marks) | typographic quotation marks as elsewhere in the text: “greedy”, “true” | S4 |
| KK-20 | p. 11, l. 319 | "(Figure 6D, 6E and 6F )" | "(Figure 6D, 6E and 6F)" | S4 |
| KK-21 | p. 12, l. 343 to 344 | "by approaching each lithology’s mineral concentration to its mean across all lithologies" | "by moving each lithology’s mineral concentration towards its mean across all lithologies" | S4 |
| KK-22 | p. 12, l. 351 | "The more resemblant the source fingerprints are" | "The more similar the source fingerprints are" | S4 |
| KK-23 | p. 12, l. 370 | "the maximal amount of non-linear iterations" | "the maximum number of non-linear iterations" | S4 |
| KK-24 | p. 13, l. 394 to 396 | "Tremolite, Talc, Quartz, Pyroxene, Phlogopite, Paragonite, Omphacite, Muscovite" | mineral names in lower case: "tremolite, talc, quartz, pyroxene, phlogopite, paragonite, omphacite, muscovite" and so on to "albite" | S4 |
| KK-25 | p. 13, l. 400 | "supporting the 1) the robustness of the cleaning and binning approach" | "supporting 1) the robustness of the cleaning and binning approach" | S3, S4 |
| KK-26 | p. 14, l. 409, l. 411 and l. 413; p. 16, l. 488 | "sub-catchment" | "subcatchment" (form of l. 283, 284, 411 and Figures 12 and 13) | S2 |
| KK-27 | p. 14, l. 424 to 425 | "following the methodology described in (Belotti, 2021). Using the approach outlined in (De Doncker et al., 2020)" | "following the methodology described in Belotti (2021). Using the approach outlined in De Doncker et al. (2020)" | S3, S4 |
| KK-28 | p. 14, l. 437 | "the same nonlinear inversion technique" | "the same non-linear inversion technique" (spelling as elsewhere) | S3, S4 |
| KK-29 | p. 15, l. 441; p. 9, l. 261; p. 10, l. 303; p. 12, l. 340 | "center of the domain"; "normalized"; "normalised"; "centre" | one spelling variety throughout, for example British: "centre of the domain", "normalised" | S4 |
| KK-30 | Figure 10 (p. 31), row 1, x-axis of the second column and colour bar label | "Smooting distance (m)" | "Smoothing distance (m)" | AB |
| KK-31 | Figure 14 (p. 35), caption and y-axis; Figure 16 (p. 37), panel title | "using Zr fingerprint data"; "Normalised abundance per Zr age bin"; "combined XRD and Zr data" | "using zircon fingerprint data"; "Normalised abundance per zircon age bin"; "combined XRD and zircon data" (Zr is the element symbol; the text uses "zircon") | S2 |
| KK-32 | Figure 15 (p. 36) and Figure 16 (p. 37), legend | "ZSF serpentinites" (overlapped by the next swatch; in Figure 16 the top row is also clipped) | "ZSF serpentinites" set in full, with the swatch of "ZSF metabasites" moved right and the top row not clipped | AB |

#### Verification log

| ID | Check | Checked | Values | Result |
|---|---|---|---|---|
| PP-15 | P4, P3 | Numbering, first citations and panel targets of all figures | Figures 1 to 16 on p. 22 to 37 without gap, each cited; first citations in ascending order (l. 146, 166, 251, 268, 289, 314, 334, 347, 356, 371, 398, 412, 414, 429, 438, 445); panel targets 1a to 1d, 2a to 2c, 3a to 3e, 5a to 5k, 6c to 6g, 7, 8, 9, 10, 13 to 16 match the cited content | no finding apart from GB-31 (6G) and GB-42 (Figure 12); panel letter case KK-06 |
| PP-16 | P1, P3 | Pixel size from the text and map scales | 1200 m / 4 = 300 m (l. 294, 325, 427); 3000 m / 10 = 300 m (l. 373); Figure 5(a) raster 44.0 cells over 532 px = 13.2 km at 300 m; catchment width at the scale bar: Figure 4 13.18 km, Figure 12 13.14 km, Figures 14 to 16 13.32 to 13.39 km (±2 %) | no finding |
| PP-17 | P2, P38 | Hyperparameters across the tests | L = 1200 m (l. 294, 325, 427); σm = 3 (l. 294, 325, 427); σd = 0.01 mm/y (l. 295, 325, 428); µ = 0.1 (l. 326, 385, 428); iterations 100 (l. 293) and 25 (l. 324, 426); symbols identical in the caption of Figure 10; counts "smoothing distance" 7, "model standard deviation" 9, "data standard deviation" 12, "step size" 10 | no finding on naming and consistency within the text; Figure 10 labels GB-53, prior GB-44 |
| PP-18 | P5, P3 | Reference configuration across Figures 7 to 10 | summed difference: Figure 7 forward geology about 197.5, Figure 9 all tracers 197.4, Figure 10 row 3 197.42 to 197.44, row 4 at µ = 0.100 197.5, row 5 at n = 25 197.6; normalised trace 0.7402 (Figure 7) and 0.7403 (Figure 8, unblended); model misfit 1.562 (Figure 7) and 1.5614 to 1.5623 (Figure 10, row 3) | no finding; the baseline is consistent across the figures |
| PP-19 | P3 | Figure 5(e) and 5(f) against Eq. (22) with σm = 3 | 159 cells read on both colour scales: (e) 2.13 to 7.89, (f) 0.449 to 0.941; (f) minus sqrt((e)/9): median minus 0.016, quartiles minus 0.023 and minus 0.005; correlation 0.984 | no finding |
| PP-20 | P3 | Figure 5(e) against l. 301 (covariance lowest at high erosion) | colour scale of (e) from 8 (dark) to 2 (light); the light cells lie at and west of the hotspot of (a) | no finding |
| PP-21 | P3 | Figure 5(g) and 5(h) against l. 305 to 307 | (g) lower envelope lowest at iterations 20.4 to 23.5, then rises by 5.1 to iteration 100; (h) rises from 0.7330 to 0.7426 and levels off | no finding on the description; the rise after iteration 23 enters GB-17 |
| PP-22 | P30 | Order of reported error correction and runs | steepest descent instability corrected by gradient normalisation before the reported steepest descent run (l. 312 to 313); no other reported error with correction | no finding; disclosed by the authors |
| PP-23 | P7 | Whether the described method held for all reported runs | one undated method change (steepest descent normalisation); parameter sets stated per run: Section 4.1.1 5 of 6, 4.1.2 0 of 6, 4.1.3 6 of 6, 4.2.1 0 of 6, 4.2.2 6 of 6 | no finding beyond GB-15, GB-30, GB-42, GB-44 |
| PP-24 | P2, P3 | Scenario 1 against l. 337 to 342 | summed difference: minimal changes 193.6, forward about 197.5, Steck et al. 274.8; area difference 0.694e7 and 1.144e7 m²; data misfit 3.254e6, 3.490e6, 3.687e6; model misfit 1.562, 1.921, 2.460 | no finding; the non-monotonic error is disclosed ("Surprisingly", l. 338) and both misfits increase as stated; ranking GB-37 |
| PP-25 | P2 | Example labels in Figures 8 and 9 against the text | Figure 8: avg. JS 0.225, 0.441, 0.624; threshold 0.44 (l. 353); Figure 9: 1, 11 and 21 tracers against "a single tracer", "the top 11 tracers", "the full tracer set" (l. 357) | no finding on the values; names GB-33 |
| PP-26 | P20 | Base of the synthetic JS average | "between all pairs of source XRD signatures" (l. 347); 7 units in Figure 5(j), hence 21 pairs | no finding for the synthetic case; natural base GB-48 |
| PP-27 | P3 | Posterior uncertainty in Figure 8 | 0.880 to 0.893 for JS 0.249 to 0.359; 0.832 to 0.842 for JS 0.440 to 0.541; 0.747 (0.561), 0.741 (0.581), 0.740 (0.602, 0.624) | no finding; the threshold at 0.55 (l. 352) is borne out for the uncertainty |
| PP-28 | P23, P34, P3 | Figure 9 counts and the statement on 7 tracers (l. 357 to 362) | 21 markers at 1 to 21 tracers in each scatterplot; summed difference 348.4 (2 tracers), 347.2 (1), 296.5 (4), 293.5 (3), 224.1 (5), 205.2 (6), 197.4 (7 to 21); top rows with 1, 11 and 21 bars; trade-off panel: few-tracer points at lower data and model misfit (l. 361 to 362) | no finding apart from GB-52 |
| PP-29 | P21 | Comparability of the synthetic error sums | all synthetic tests share domain and pixel grid (Figures 5 to 10), so the sums are comparable within Section 4.1 | no finding within Section 4.1; base across contexts GB-35 |
| PP-30 | P3 | Figure 10 rows 2 and 4 against l. 377 to 379 and l. 385 to 386 | row 4: 328.3 at µ = 0.010 falling to a minimum of 197.5 at 0.100, then 199.0 to 201.3 up to 0.316; row 2: 209.1, 204.1, 200.9 and 198.9 at the smallest σm, 197.4 to 197.6 for all others; the annotated σm = 6.2 is the point at 6.16 | no finding |
| PP-31 | P2, P22 | Iteration statements | minimum of 25 iterations (l. 387); 25 used (l. 324, 426); change in data misfit below 10^-5 after 115 iterations (l. 388 to 389); 100 in the first quasi-Newton test (l. 293) | no finding on the compatibility of the numbers (25 a lower bound, 115 a stricter criterion); whether the stopping rule governed the runs is GB-17 |
| PP-32 | P1, P2, P38 | Names and number of the tracer minerals | 21 stated (l. 393, 397); 21 names listed (l. 394 to 396), all distinct; 21 rows in Figure 11, 21 bars in Figures 15 and 16; synthetic tracers A to U in Figure 5(k) = 21; "between 1 and 21 tracers" (l. 358); text against Figure 11 differs only in Chrysolite and Chrysotile | no finding apart from GB-40 |
| PP-33 | P3 | Figure 11 normalisation and serpentinite composition (l. 261 to 262, l. 274) | longest bar per column 0.996 to 1.004; serpentinites: Antigorite 0.996, Chrysotile 0.906, Fayalite 0.615, Diopside 0.143, all others at most 0.016 | no finding apart from GB-19 and GB-20 |
| PP-34 | P23, P3 | Lithological units in the zircon dataset; Figure 14 against l. 430 to 436 | 7 units = 5 with own zircon fingerprint + 1 copied (MR g-g from MR granite) + 1 without zircon (ZSF metabasites and eclogites); MR gneiss and MR granite segments equal in all 11 shared age bins; no metabasite segment; hotspot cells 8360 to 8510 mm/y | no finding for the balance; consequences in GB-45 and GB-48 |
| PP-35 | P2 | Normalised posterior uncertainty, text against figure labels | zircon 0.87 (l. 436, l. 447; Figure 14), XRD 0.82 (l. 442; Figure 15), combined 0.86 (l. 447; Figure 16) | no finding on the values; interpretation GB-47, definition GB-16 |
| PP-36 | P1 | Relative changes between the natural runs | zircon to XRD minus 5.75 %; zircon to combined minus 1.15 %; XRD to combined plus 4.88 %; JS 0.48 to 0.57 plus 18.75 % (Python) | no finding; "slightly" (l. 441, l. 447) matches the size of the changes |
| PP-37 | P2 | Sampling date and time | 28 June 2019, 13:30 (l. 423 to 424); "the same date and time" (l. 438) | no finding for date and time; sample identity GB-43 |
| PP-38 | P36 | Statements from impression against the manuscript's own records | "After several iterations" (l. 290) against 100 iterations (l. 293): consistent; "In initial experiments" (l. 312): no record, not contradicted; "In many of these cases" (l. 353): unquantified (GB-34); "Some spillover" (l. 414 to 415): unquantified (GB-42) | no separate finding |
| PP-39 | P29 | Font size in print size, smallest lettering of each figure with values | Figure 5 6.3 pt; Figure 7 5.7 pt; Figures 8 and 9 6.0 to 6.3 pt; Figure 10 3.7 to 4.7 pt; Figures 11, 14 and 15 5.3 pt; Figure 13 7.7 to 8.3 pt | finding GB-54 for Figure 10; Figures 7, 11, 14 and 15 within or just outside the measuring uncertainty, no finding |
| PP-40 | P24 | Dated events in the figures | no figure has a time axis or dated markers; dated sample in the text: 28 June 2019, 13:30 (Figures 14 to 16) | no finding apart from the undated samples of Figure 13 (GB-42) |

### Segment 4: Discussion, Conclusions, declarations, references (p. 15 to 21)

#### Substantive findings

**GB-55 Discussion and Conclusions do not take up two of the three natural-data aims, the comparison of the inversion schemes, or the unmixing framework of the Introduction.**

| Field | Content |
|---|---|
| Check | P15 |
| Location | Sections 5 and 6 (p. 15, l. 450 and p. 16, l. 477); aims p. 10, l. 282 to 284; p. 2, l. 59 |
| Quotation | "1) to investigate whether the inferred XRD source fingerprints align with the expected mineralogical compositions of the lithologies, 2) to test if sediment samples from a subcatchment are attributed only to lithologies present within the subcatchment boundaries" (l. 282 to 284); l. 55 to 56: "Our approach can be seen as a hybrid between Bayesian linear mixed models and hierarchical Bayesian models" |
| Concern | Aims 1 and 2 are answered in the Results (l. 399 to 401, l. 402 to 418), but neither appears in the Discussion or the Conclusions; the Conclusions cite only "synthetic forward-inverse experiments" (l. 482). The comparison of the two inversion schemes, announced in the Abstract (l. 4 to 5), is not taken up either (design sketch, PP-08). The Introduction places the method among frequentist and Bayesian unmixing models (l. 43 to 57) and states that these "implicitly rely on a linear mixing scheme" (l. 59); the Discussion neither returns to this classification nor compares the results with any of these models. |
| Suggestion | Add to Section 6 one sentence each on the outcome of aims 1 and 2 and of the scheme comparison, and to Section 5 a paragraph that places the results against the unmixing models of l. 48 to 57 (what the spatial, log-parameterised inversion gains or loses compared with BLMM or NNLS). |
| Status | verified |
| Severity | moderate |
| Source | S4 |

**GB-56 The novelty statement claims a spatially informed approach and a non-linear mixing model, whereas the Introduction attributes the spatial framework to earlier work and the forward model mixes linearly.**

| Field | Content |
|---|---|
| Check | P28, P15, P10 |
| Location | p. 15, l. 454 to 455; p. 2, l. 58 to 59 |
| Quotation | "The novelty of our method lies in the spatially informed approach of this underdetermined inversion problem, and in the incorporation of non-linear mixing model." (l. 454 to 455); "these approaches typically yield relative source contributions without translating them into spatially explicit erosion rate maps and implicitly rely on a linear mixing scheme" (l. 58 to 59); l. 157 to 158: "We cast the erosion rates in log-space to impose a positivity constraint, hence making this non-linear." |
| Concern | The Introduction states correctly that the method is "a non-linear adaptation of the inversion framework validated in (De Doncker et al., 2020)" (l. 60 to 61), whose title in the reference list is "Inversion of provenance data and sediment load into spatially varying erosion rates" (p. 18, l. 559). Its abstract (serval.unil.ch record, read by S1) already describes a formal inversion that converts detrital data into an erosion rate map from the spatial distribution of source signatures, with a priori information and model covariance, and states that mineral content can serve as tracer. The spatially informed inversion is therefore not new in this manuscript. The second element is stated more strongly than the model supports: the detrital data are "a weighted average of the tracer mineral concentrations, with the weights being the erosion rates" (l. 151 to 152), so the mixing is linear in the erosion rates, and the non-linearity arises only from the log parameterisation (l. 157 to 158). The gap "rely on a linear mixing scheme" (l. 59) thus has no matching answer, and no result compares linear with non-linear mixing. Das et al. (2023), also cited, combine fingerprinting with sediment yield into an erosion susceptibility index (abstract), which qualifies "typically" in l. 58. The phrase in l. 455 also lacks an article ("of non-linear mixing model"). |
| Suggestion | Rewrite l. 454 to 455 to name what is new relative to De Doncker et al. (2020), for example "The novelty lies in the use of binned XRD peak-area data as fingerprints within the spatially informed inversion of De Doncker et al. (2020), and in a log-space parameterisation that enforces positive erosion rates"; replace "non-linear mixing model" by "linear mixing with a non-linear (log-space) parameterisation", and state in l. 58 to 61 what the 2020 framework already provided. |
| Status | verified (manuscript text; De Doncker et al. 2020 abstract) |
| Severity | moderate |
| Source | S1, S4, SD |

**GB-57 The Discussion states that a broad tracer set further improves stability and resolution, whereas the tracer-reduction test found no change above 7 tracers and did not evaluate resolution.**

| Field | Content |
|---|---|
| Check | P15 |
| Location | p. 15, l. 457 to 458 |
| Quotation | "Including a broad set of tracer minerals further improves model stability and resolution." |
| Concern | The Results state that "The inversion with 7 tracers results in approximately the same posterior solution as with the full tracer set" (l. 360) and that reducing the number of tracers "has a comparatively limited effect" provided the informative ones are retained (l. 365). In Figure 9 the summed error is 197.4 for every count from 7 to 21 tracers (PP-28). The scenario reports absolute error, posterior uncertainty and misfits, not resolution. The Discussion sentence thus reverses the reported result and adds a metric that was not tested. |
| Suggestion | Replace l. 457 to 458 by a statement that matches l. 360 to 365, for example "Retaining at least the seven most informative tracers is sufficient; adding further tracers did not change the posterior solution in our tests." |
| Status | verified |
| Severity | moderate |
| Source | S4 |

**GB-58 Two conditions are presented as results although no test varies them: the number of distinct source areas and sediment storage.**

| Field | Content |
|---|---|
| Check | P15 |
| Location | p. 15, l. 460 to 461; p. 16, l. 484 to 486 |
| Quotation | "A higher number of distinct source areas leads to higher posterior resolution and lower uncertainty." (l. 460 to 461); l. 484 to 486: "Our results suggest that the method is best applied in catchments with minimal sediment storage, multiple mineralogically distinct source areas, and good prior knowledge of the spatial distribution of source areas." |
| Concern | The synthetic tests vary map geometry (scenario 1), fingerprint blending (scenario 2), tracer count (scenario 3) and five hyperparameters (Section 4.1.4); none varies the number of source areas. Sediment storage is not tested at all: the Discussion presents it as an assumption of the model with a literature citation (l. 466 to 468), and the Introduction says that the approach works "without modelling storage or transport" (l. 23). "Our results suggest" in l. 484 is therefore correct only for distinctness (scenario 2) and spatial knowledge (scenario 1). |
| Suggestion | Delete l. 460 to 461 or support it with a test that varies the number of source units; in l. 484 to 486 separate the conditions supported by results from the model assumption, for example "Our results indicate that the method requires mineralogically distinct sources and a well-constrained source map; by construction, it also assumes minimal sediment storage." |
| Status | verified |
| Severity | moderate |
| Source | S4 |

**GB-59 The study site does not meet the application criteria the manuscript itself recommends, and the criterion on fingerprint contrast is not reported for the natural XRD data.**

| Field | Content |
|---|---|
| Check | P18 |
| Location | p. 15, l. 463 to 465; p. 3, l. 62 |
| Quotation | "we recommend applying this method in catchments where: a) the spatial distribution of source lithologies is well constrained, b) the source units show strong mineralogical contrasts, and c) multiple XRD tracers are available" (l. 463 to 465); l. 61 to 62: "This spatially informed approach to sediment provenance is particularly valuable in glacierized catchments, where ice cover limits direct observations" |
| Concern | Criterion a) conflicts with the site, where "In ice-covered regions, where direct geological mapping is not possible, we infer the lithology" (l. 270 to 271), and with the Introduction, which names glacierized catchments as the setting where the approach is particularly valuable. For criterion b) the manuscript defines a measurable threshold (error and uncertainty rise sharply below an average JS distance of 0.55, l. 351 to 352) and reports JS for zircon (0.48) and the combination (0.57), but not for the natural XRD fingerprints alone (GB-48), so it cannot be checked whether the natural XRD case lies above or below the manuscript's own threshold. The caution against significant sediment storage (l. 467) is not assessed for the glacial site. |
| Suggestion | Report the average JS distance of the natural XRD fingerprints in Section 4.2; state in Section 5 how far the Gornergletscher site meets criteria a) to c) and the storage condition; reconcile l. 61 to 63 with criterion a). |
| Status | verified |
| Severity | moderate |
| Source | SD |

**GB-60 The outlook proposes zircon data, land use and sub-catchments as available extensions, although the zircon-only inversion was highly unstable and the other extensions are untested and outside the sampling protocol.**

| Field | Content |
|---|---|
| Check | P15, P9 |
| Location | p. 15, l. 466; p. 16, l. 487 to 489 |
| Quotation | "While we focus on geological units as source areas, the approach is flexible and can be extended to alternative classifications such as land use or sub-catchments. Similarly, the method is not limited to XRD-derived fingerprints and can be applied to other types of tracer data, including zircon U-Pb age distributions or geochemical compositions." |
| Concern | The zircon-only inversion gave "extreme erosion rate values" above 8000 mm/y, "low resolution" and a normalised uncertainty of 0.87 (l. 435 to 436), which the manuscript attributes to missing zircon data for two units (l. 430 to 434); the proposal may hold where zircon fingerprints are complete, but the Conclusions state it without that condition. No geochemical tracer was tested. Section 3.4 defines source sampling "from every lithological unit" (l. 251); no protocol exists for sampling a land-use class or a sub-catchment, whose mineralogy is not homogeneous where lithology varies within it. The manuscript holds distinct source signatures to be essential (l. 457) and finds reduced distinctiveness to be the strongest factor (l. 363 to 364); a land-use class that mixes lithologies lowers distinctiveness. Do the authors expect land-use classes on the same lithology to give fingerprints distinct enough for the inversion? |
| Suggestion | In Section 6 rephrase the extensions as proposed studies, add the condition shown by Section 4.2.2 ("provided that fingerprints are available for all source units"), state the sampling design for non-lithological source classes and the distinctiveness (average JS distance) they would have to reach, and say in l. 466 that the land-use extension has not been tested. |
| Status | verified (text and zircon result); assumption (fingerprint contrast between land-use classes), posed as a question |
| Severity | moderate |
| Source | S4, SD |

**GB-61 The Discussion cites depth-integrated sampling as a remedy for grain-size effects, but the manuscript does not say that its detrital samples were depth-integrated.**

| Field | Content |
|---|---|
| Check | P15 |
| Location | p. 15, l. 469 to 471 |
| Quotation | "This can be diminished by powdering samples and using depth-integrated suspended sediment samples to average out sorting effects during transport (Butler et al., 2019)." |
| Concern | "depth-integrated" occurs only in l. 470. The figures label the detrital sampling "pump sampler" (Figure 3(a): "detrital sampling: pump sampler"), and the Methods give no sampling depth or integration procedure. If the samples were taken at a fixed intake, the mitigation named in l. 470 does not apply to the data of this study, and grain-size sorting remains an uncontrolled influence on the detrital fingerprints. Were the detrital samples depth-integrated? |
| Suggestion | State in Section 3.4 or Section 4.2 how and at which depth the detrital samples were taken, and say in l. 469 to 471 whether the mitigation applies to the present data. |
| Status | verified (absence of the information; figure labels); assumption (that a pump sampler takes point samples), posed as a question |
| Severity | moderate |
| Source | S4 |

**GB-62 The one-sentence data statement does not say which natural datasets it covers.**

| Field | Content |
|---|---|
| Check | P12 |
| Location | p. 16, l. 490 |
| Quotation | "The data and codes used for the inversion tests in the study are available at https://doi.org/10.5281/zenodo.17120374" |
| Concern | The statement gives a working DOI (PP-45), which is a strength. It does not list what the record contains, and "for the inversion tests" leaves open whether the following sources named in the methods are included: (1) raw diffractograms of source and detrital samples (l. 252 to 253); (2) the WinXRD Peak Finder settings (l. 254 to 255), a step done in commercial software and therefore not reproducible from the authors' code; (3) the zircon U-Pb ages of sources and detrital sample (l. 423 to 425), whose only reference is an unpublished master's thesis (Belotti, 2021); (4) the three geological maps of scenario 1 (l. 332 to 334); (5) sample metadata: number and coordinates of the source samples (l. 251) and number, dates and location of the "multiple detrital samples" (l. 413); (6) the export estimate and the multi-year sediment datasets (GB-44); (7) the third-party layers of Figure 4 (GB-23). The README of the authors' public code repository lists raw XRD data, RRUFF files and raw zircon data (read by S2 on the current repository page, not in the archived v1.0.0); the manuscript itself does not say so. |
| Suggestion | Expand the statement in l. 490 into an item list (raw diffractograms, processed fingerprints, zircon U-Pb ages with a note that Belotti (2021) is unpublished, geological map variants, sample metadata, Peak Finder settings, export estimate), each marked as included, available on request, or withheld with a reason. |
| Status | verified (wording of l. 490 and the sources named in the methods); inferred (contents of the record, from the repository README, not from the archived v1.0.0) |
| Severity | moderate |
| Source | S2 |

**GB-63 Several reference entries are incomplete or inconsistent in form.**

| Field | Content |
|---|---|
| Check | P16 |
| Location | p. 17, l. 521; p. 19, l. 583 and l. 599 to 600; p. 20, l. 612 to 613 and l. 634 to 635 |
| Quotation | "Gjems, O.: Studies on clay minerals and clay-mineral formation in soil profiles in Scandinavia, 1967."; "The power of databases: the RRUFF project, Highlights in Mineralogical Crystallography,"; "Bearth, P.: Blatt 535 Zermatt - Geologischer Atlas der Schweiz 1:25 000, 1953."; "ISBN 9780898715729 9780898717921"; "Oxford University Press, New-York," |
| Concern | Compared with the other entries, Gjems (1967) lacks report series or publisher, Lafuente et al. (2015) lack the editors and publisher of the book, Bearth (1953) lacks the publishing body, Tarantola (2005) lists two ISBNs without separator, and Moore and Reynolds (1990) give a page range for a book and write "New-York" with a hyphen. The entries cannot all be located in the same way. |
| Suggestion | Complete the entries in l. 521, l. 583 and l. 599 to 600 with publisher or series and place, keep one ISBN in l. 635, and in l. 612 to 613 write "New York" and move the page range to the in-text citation if a specific passage is meant. |
| Status | verified (page images p. 17, p. 19, p. 20) |
| Severity | minor |
| Source | S4 |

#### Minor corrections

| ID | Location | Quotation | Replacement | Source |
|---|---|---|---|---|
| KK-33 | p. 16, l. 490 | "available at https://doi.org/10.5281/zenodo.17120374" (the line runs into the right margin; no final period) | "available at https://doi.org/10.5281/zenodo.17120374." with a permitted break in the URL | S4 |
| KK-34 | p. 16, l. 491 to 494 | "All authors (FDD, FH, BB, TA)" | "All authors (F.D.D., F.H., B.B., T.A.)" (form used in l. 491 to 494) | S2, S4 |
| KK-35 | p. 17, l. 522 to 523 | "Master’s thesis, University of Lausanne, unpublished master’s thesis, 2021." | "unpublished Master’s thesis, University of Lausanne, 2021." | S4 |
| KK-36 | p. 17, l. 526 to 527 | "Mineralogical society of America" | "Mineralogical Society of America" | S4 |
| KK-37 | p. 19, l. 578 | "[No title found]" | "Landscape indicators of human impacts to riverine systems" | S4 |
| KK-38 | p. 20, l. 639 | "Bomb-fallout137 Cs as a marker" | "Bomb-fallout ¹³⁷Cs as a marker" | S4 |

#### Verification log

| ID | Check | Checked | Values | Result |
|---|---|---|---|---|
| PP-41 | P4 | Citations against the reference list in both directions | 64 distinct citation keys in the text (Python extraction of p. 1 to 16) and 64 entries (l. 501 to 653); every key has an entry and every entry is cited; years agree for all 64; "et al." for all entries with three or more authors, "X and Y" for the 11 two-author entries; name spellings agree | no finding apart from GB-04 and GB-06 |
| PP-42 | P15, P9 | Outlook proposals held against the findings | (a) well-constrained lithology (l. 464): scenario 1 error 193.6 to 274.8, supported; (b) strong mineralogical contrasts (l. 464 to 465): sharp rise below JS 0.55, supported; (c) multiple XRD tracers (l. 465): at least 7 tracers, supported; combination part GB-47; (d) land use (l. 466, l. 487 to 488) untested, GB-60; (e) storage (l. 466 to 468) as result, GB-58; (f) zircon and geochemistry (l. 488 to 489), GB-60 | no finding for (a) to (c) |
| PP-43 | P15 | Conclusion statements mapped to results | "We present a non-linear inversion method" (l. 478): Sections 3 and 4.1; "integrates prior erosion estimates, a yearly sediment export estimate, and spatial information" (l. 479 to 480): Eq. (2), l. 159 to 160 (value missing, GB-44); "We highlight how model resolution and posterior covariance can be used" (l. 483 to 484): Section 4.1.1, l. 299 to 304, and Section 4.2.2, l. 435 to 436, verb matches the qualitative evidence | no finding for the mapped statements |
| PP-44 | P15 | Discussion of XRD limitations (l. 469 to 476) | grain size (Gjems, 1967), preferred orientation (Weir et al., 1975), shielding and peak alignment (Butler et al., 2019; Das et al., 2023, 2024), window averaging (matches l. 259 to 260); all hedged or literature-based, not claimed as own results | no finding beyond GB-11, GB-19 and GB-61 |
| PP-45 | P12 | Reachability of the data link; published sources of the method | DOI 10.5281/zenodo.17120374 resolves to "Non-Linear-XRD-Inversion: First public release", v1.0.0, 15 September 2025, CC BY 4.0, one file of 49.3 MB; RRUFF spectra cited as Lafuente et al. (2015); Bearth (1953) and Steck et al. (2015) in the reference list | no finding for the synthetic test data and the published geological sources; coverage of the natural data GB-62 |
| PP-46 | P16 | Extraction artefacts not raised as findings | checked at the page images: ligature in "fluvial" only in text.json; copyright sign rendered as "c"; displaced equation fragments on p. 5 to 8 (layout correct apart from KK-07 and KK-09); justified spacing in the entry Grimshaw and Lewin (l. 584) | no finding |

## Optional checks

| Area | What it needs | Responsible | Run |
|---|---|---|---|
| DOI resolution | one retrieval per reference entry with a DOI | `science-quellenapparat-pruefung` | no |
| Citation style | the name of the style | `science-zitierstil-harvard-ctr` or the style rules of the journal | no |
| AI statement against publisher policy | the policy of the target publisher | this review, on request | no |
| Relation to the authors' earlier work | the earlier work of the authors | this review, on request | no |
| Journal requirements | the author guidelines of the target journal | this review, on request | no |
| Subject accuracy | access to the sources of the checked statements and a selection of sections | `science-faktenbeleg-pruefung`, `geo-frage-belegbasiert-klaeren` | no |

## Limits of this review

- Checked version: egusphere-2025-4695.pdf, 37 pages, SHA-256 9c80676054f96ecd6f00f4d2a8b5ba568e03c6949e3856d363ac1c4abb42e7bd.
- Review instances: the six instances (segments 1 to 4, figures, study design) ran as separate agents; the merge, the overall assessment and the format check ran in a further separate agent.
- Sources not readable: full texts of Das et al. (2023), Niu et al. (2020), Haddadchi et al. (2013), Yang et al. (2025), Fathabadi and Jansen (2022) and Davis and Fox (2009); abstracts of Klages and Hsieh (1975), Wilson et al. (1993), Walden et al. (1997) and Olley et al. (1993), judged by their titles; the UNESCO report of 2009 attributed to Walling; the content of the archived Zenodo file v1.0.0 (only the record page and the current repository README were read).
- Values read from diagrams come from measurements of the figures instance on page images at 300 dpi; where a value was read from tick labels only, the finding says so.
- Findings with status assumption: 13 of 63.
- Optional checks run: 0 of 6.
- Omitted instances: none.
- Discarded findings: 0. One partial statement was dropped during the merge: the part of an instance finding that called the rise in Figure 5(h) steep relative to a truncated axis, after the figures instance had measured the description of l. 305 to 307 as consistent with the plot (PP-21).
