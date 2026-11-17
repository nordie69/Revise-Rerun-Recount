# Review report: From XRD signal to erosion rate maps

| Field | Value |
|---|---|
| Manuscript | De Doncker, F., Herman, F., Belotti, B., and Adatte, T. (2025): From XRD signal to erosion rate maps, EGUsphere preprint egusphere-2025-4695, https://doi.org/10.5194/egusphere-2025-4695 |
| Checked version | egusphere-2025-4695.pdf, 37 pages, SHA-256 9c80676054f96ecd6f00f4d2a8b5ba568e03c6949e3856d363ac1c4abb42e7bd |
| Date | 2026-10-17 |
| Language | English |
| Review instances | Segments 1 to 4, figures, study design; the six review instances ran as separate agents, each without context from the others; no instance omitted |

## Summary

The manuscript is a method development study. It builds a spatially explicit inversion that converts binned X-ray diffraction (XRD) peak-area fingerprints of suspended sediment into erosion rate maps: a linear mixing forward model with log-parameterised erosion rates, inverted as a Bayesian maximum a posteriori problem with a Gaussian model covariance, and solved with a steepest descent and a quasi-Newton scheme. Posterior covariance, resolution and a normalised posterior uncertainty serve as reliability metrics. Synthetic forward-inverse tests use one "true" map with one hotspot, three degradation scenarios (three geological maps, 20 levels of fingerprint blending, 1 to 21 tracers) and five hyperparameter sweeps. The natural case is the Gornergletscher catchment with seven lithological units and 21 tracer minerals: a natural known-mixture analogue at the Gorner-Grenz confluence, and a comparison of zircon U-Pb, XRD and combined fingerprints from one detrital sample, with normalised posterior uncertainty of 0.87, 0.82 and 0.86 and average Jensen-Shannon distance of 0.48 (zircon) and 0.57 (combined).

## Strengths

1. The synthetic tests vary one factor at a time against a known truth on the same grid (three degradation scenarios, five sweeps), so changes in error, uncertainty and misfit can be traced to their cause; the reported baselines agree across scenarios and sweeps, and thresholds such as seven tracers and an average JS distance of about 0.55 can be read from the plotted values (PP-37, PP-40, PP-45, PP-51).
2. The natural known-mixture test states its expected outcome before the result (only lithologies inside the subcatchment should receive erosion) and uses a unit without outcrops in the subcatchment as a negative control, so the test is set up so that it can fail (PP-13; its present limits in GB-39).
3. The same normalised uncertainty metric is reported for all three natural cases and agrees between text and figure labels (0.87, 0.82, 0.86), which makes the cases directly comparable; it is this consistency that lets the reader check the combined case against the XRD-only case (PP-32, PP-48; GB-42).
4. Code and data are archived under a DOI that resolves, the citations and the reference list correspond in both directions, and the underdetermination, the Gaussian approximation and the inferred geology under ice are disclosed where the method is introduced, so a reader can obtain the code and knows these limits from the start (PP-09, PP-56, PP-24).

## Weaknesses

1. Several comparative statements are not supported by the manuscript's own numbers: the combined zircon and XRD inversion is less certain than XRD alone (GB-42), steepest descent ends with the lower error than the adopted quasi-Newton scheme (GB-26), the posterior hotspot in Figure 5 is shifted and overshoots (GB-25), and the smoothing distance used in all runs is not the one the sweep favours (GB-33). The statements should be restated with the numbers for every case compared, and the choices of scheme and hyperparameters justified on stated criteria.
2. The three natural tests have no quantitative criterion: the fingerprints are judged to align with the lithology by eye, although several minerals carry identical fingerprints and key minerals are near zero (GB-38, GB-36); the known-mixture analogue cannot separate discrimination from low resolution (GB-39); the normalisation entering A and d is not the one described (GB-18); and the resolution panels contradict the reading of low resolution (GB-48). Expected-against-measured tables, flux shares inside and outside the subcatchment, a laboratory known-mixture test and an explicit normalisation formula would make these tests decisive.
3. The Abstract and Conclusions claim more than the Results show: time and cost efficiency is not measured (GB-02), convergence and robustness are stated without their conditions (GB-03), the novelty of a non-linear mixing model does not match a linear forward model (GB-09), the synthetic tests take the prior mean from the truth (GB-23), and the natural-data aims are not answered in the Conclusions (GB-52). Each claim should be qualified to the conditions and evidence reported.
4. Inputs and settings needed to rebuild the results are missing or inconsistent: the export estimate and the natural prior (GB-11), the unit of the data standard deviation (GB-12), the printed quasi-Newton update (GB-14), the uncertainty metric (GB-15), the XRD processing and zircon methods (GB-17, GB-19), the construction of the synthetic test sets (GB-29) and the scope of the data statement (GB-56). These should be stated in Sections 3 and 4 and in an itemised data availability statement.

## Findings by segment

### Segment 1: Abstract, Introduction (p. 1 to 5, l. 1 to 142)

#### Substantive findings

**GB-01 The temporal framing of the Abstract and Introduction is not carried into any question, test or result, and the assumptions that link one instantaneous sample to annual erosion are not stated where the forward model is introduced**

| Field | Content |
|---|---|
| Check | P10, P15, P17 |
| Location | p. 1, l. 1 and l. 13 (repeated p. 3, l. 80); p. 1, l. 23; p. 5, l. 147 to 148; p. 9, l. 267 to 268; p. 14, l. 413 and l. 423 to 424; p. 15, l. 466 to 468; Figure 13 (p. 34) |
| Quotation | "Understanding the spatio-temporal dynamics of suspended sediment source activation is essential"; "Identifying sediment source hotspots and the timing of their activation"; "We caution against using this method in catchments with significant sediment storage, as the inversion directly links sediment provenance to erosion rates and assumes immediate sediment export" |
| Concern | Temporal dynamics and the timing of source activation motivate the study (l. 1, l. 10, l. 13), and the site was chosen for its "multi-year suspended sediment datasets" (l. 268). No test aim (l. 280 to 285), instrument or result addresses time: "temporal" and "timing" occur only in l. 1, 10, 13, 77 and 80 (Python search of the text). Section 4.2.2 uses one sample "collected on June 28, 2019, at 13:30" (l. 423 to 424), and Section 4.2.1 pools all samples of the subcatchment into one KDE per unit (Figure 13), which removes any temporal information. Combining one instantaneous composition with an annual export estimate into an erosion rate map in mm/y assumes that the composition of the sample stands for the annual mean; this is not stated. The Introduction notes that fingerprinting links sediment to its origin "without modelling storage or transport" (l. 23), and the Discussion states the assumption of immediate export (l. 466 to 468); Section 3.1, where the forward model is introduced, says only that sediments "are then transported or stored" (l. 147 to 148). |
| Suggestion | Either narrow the framing in the Abstract (l. 1) and the Introduction (l. 10 to 13) to spatial attribution and state in Section 5 that temporal dynamics were not addressed, or add per-sample inversions with dates and discharge from the multi-year data set to Section 4.2.1; state in Section 3.1 the assumptions of immediate export and of a representative sample composition. |
| Status | verified (absence of a temporal question, test or result; wording at l. 1, 13, 23, 147 to 148, 466 to 468); inferred (the representativeness assumption) |
| Severity | moderate |
| Source | SD, S4 |

**GB-02 Time and cost efficiency of the XRD approach is stated as validated, but no measure of time or cost appears in the manuscript**

| Field | Content |
|---|---|
| Check | P10, P15, P33 |
| Location | p. 1, l. 3 to 4; p. 2, l. 35 and l. 40 to 42; p. 3, l. 74 to 75 (repeated p. 4, l. 102 and l. 107 to 109; p. 5, l. 141 to 142); p. 16, l. 477 to 489 |
| Quotation | "In this study, we validate a time- and cost-effective fingerprinting approach based on X-ray diffraction (XRD) data."; "To conclude, we show and validate the potential of binned XRD peak-area data as a cost- and time-efficient approach for constructing erosion rate maps." |
| Concern | The manuscript ran two fingerprinting methods on material of the same sampling date (zircon U-Pb and XRD, l. 423 to 438), which would allow a comparison of effort. No measure of effort is reported for either method: no cost per sample, no instrument or analyst time, no throughput. "cost" occurs only in l. 3, 4, 40, 74, 107 and 141 (Python search). The efficiency claim rests on the citation "many of these methods are expensive and time-consuming (Das et al., 2023)" (l. 35). Efficiency is not among the three natural test aims (l. 282 to 285), and the Conclusions (l. 477 to 489) do not mention cost or time, although the Introduction announces that the study will "show and validate" it (l. 74 to 75). The grade is major because the Abstract names efficiency as part of what was validated; if the finding holds, the manuscript cannot show that part. |
| Suggestion | Either add a per-sample comparison of XRD and zircon U-Pb to Section 4.2.2 (preparation, instrument and processing time, consumables, cost) and take it up in Section 6, or remove the words "validate a time- and cost-effective" from l. 3 to 4 and "as a cost- and time-efficient approach" from l. 74 to 75 (and l. 141 to 142), and present efficiency as a motivation with its citation (Das et al., 2023). |
| Status | verified (absence of any measure of time or cost in text and figures; word search) |
| Severity | major |
| Source | SD, S4 |

**GB-03 The Abstract and Conclusions state convergence and robustness without the conditions that the Results show**

| Field | Content |
|---|---|
| Check | P2, P6 |
| Location | p. 1, l. 7 to 8; p. 16, l. 482 to 483; p. 11, l. 312; p. 12, l. 353; p. 13, l. 380 and l. 387 to 388; p. 14, l. 435; Figure 8, caption (p. 29) |
| Quotation | "Forward-inverse tests with synthetic data demonstrate consistent convergence of the posterior solution."; "the method is robust across a range of parameters" |
| Concern | The Results name non-convergence or failure under several conditions: steepest descent "proved unstable, requiring the normalization of the gradient" (l. 312); for blended fingerprints "In many of these cases, the inversion fails to converge to a stable posterior solution" (l. 353), and six of 20 runs are missing from Figure 8 (GB-30); the posterior fails to converge below 25 iterations (l. 387 to 388); very low data standard deviation is said to "lead to large differences" (l. 380; see GB-34); the natural zircon-only run is "highly unstable" (l. 435). Convergence was therefore shown for the quasi-Newton scheme with sufficiently distinct fingerprints and at least 25 iterations. "consistent convergence" in l. 7 states it without these conditions. "a range of parameters" in l. 483 is hedged, but the range is not named. The Abstract adds that "The application to real-world datasets further validates the practical utility and robustness of the model" (l. 8), which rests on one subcatchment test and one dated sample (GB-39, GB-42). |
| Suggestion | Qualify l. 7 and l. 482 to 483 with the conditions found (quasi-Newton scheme, average JS distance above about 0.55, at least 7 tracers, at least 25 iterations) and name the tested parameter ranges; restrict l. 8 to what Sections 4.2.1 and 4.2.2 show. |
| Status | verified |
| Severity | moderate |
| Source | S3, SD |

**GB-04 The Introduction is printed twice, as Section 1 and as Section 2, so every later section number is shifted by one**

| Field | Content |
|---|---|
| Check | P4 |
| Location | p. 1, l. 9 and p. 3, l. 76 (section headings; Sections 1 and 2 in full, p. 1 to 5) |
| Quotation | "1 Introduction"; "2 Introduction" |
| Concern | A word-by-word comparison (Python, difflib, page headers removed) of l. 10 to 75 against l. 77 to 142 gives 1153 words in each block and a similarity ratio of 1.0; the two sections are identical (66 printed lines each). Because of the duplicate, Methods is Section 3 and Validation Section 4, every citation of the Introduction appears twice, and a reference to "Section 2" would be ambiguous. |
| Suggestion | Delete Section 2 (l. 76 to 142) and renumber Methods to 2, Validation to 3, Discussion to 4 and Conclusions to 5, including all subsection numbers. |
| Status | verified (page images 1, 3 and 5; word comparison) |
| Severity | minor |
| Source | S4 |

**GB-05 The author of the UNESCO 2009 report appears as "E., W. D." in the entry and as "E., 2009" in the citation; surname and initials are inverted**

| Field | Content |
|---|---|
| Check | P4 |
| Location | p. 1, l. 11 to 12 and p. 3, l. 78 to 79 (citation); p. 18, l. 567 to 568 (entry) |
| Quotation | "(Gergel et al., 2002; Allan, 2004; E., 2009; Hamel et al., 2015)"; "E., W. D.: The Impact of global change on erosion and sediment transport by rivers, UNESCO 2009, ISBN 9789231041358, oCLC: 1402659188, 2009." |
| Concern | "E." is not a surname. The UNESCO report with this title is listed under D. E. Walling, so surname and initials have been swapped. The entry also repeats the year ("UNESCO 2009" and "2009"), contains the misprint "oCLC", and is filed under "E", out of alphabetical place. |
| Suggestion | In l. 11 (and l. 78) write "Walling, 2009"; rewrite the entry in l. 567 to 568 as "Walling, D. E.: The impact of global change on erosion and sediment transport by rivers: current progress and future challenges, UNESCO, Paris, ISBN 9789231041358, 2009." after checking the full title against the title page, and move it before "Walling, D. E., Peart, M. R." (l. 645). |
| Status | verified (inversion of the name in citation and entry, page images 1, 3 and 18); inferred (attribution to D. E. Walling and the full title, from a search listing; the report itself was not readable) |
| Severity | minor |
| Source | S4, S1 |

**GB-06 Two of the three works cited for sediment traps on dams do not deal with sediment traps**

| Field | Content |
|---|---|
| Check | P13 |
| Location | p. 1, l. 18 to 19 (repeated p. 3, l. 85 to 86); p. 17, l. 519 to 520 (Barker et al., 1997); p. 21, l. 649 to 650 (Wilson et al., 1993) |
| Quotation | "Direct measurements, such as sediment traps installed on dams, provide valuable information on sediment fluxes but do not reveal the origin of the transported material (Wilson et al., 1993; Barker et al., 1997; Davis and Fox, 2009)." |
| Concern | According to its abstract, Barker et al. (1997) use terrestrial photogrammetry to measure river bank erosion; sediment traps or dams do not appear, and the entry title reads "Use of terrestrial photogrammetry for monitoring and measuring bank erosion" (l. 519). Wilson et al. (1993) assess soil erosion in the Falkland Islands (l. 649); the bibliographic record lists grazing, stocking rate and pasture burning as keywords. Davis and Fox (2009) was not checked. The statement is plausible, but two of its three citations do not document the example "sediment traps installed on dams". |
| Suggestion | In l. 19 and l. 86 cite a study that measures sediment flux with traps or reservoir surveys at dams, or rephrase the example so that it matches the cited works. |
| Status | verified (Barker et al., 1997, abstract); inferred (Wilson et al., 1993, metadata only) |
| Severity | minor |
| Source | S1 |

**GB-07 Four of the 29 citations in the list of fingerprinting tools do not report the tracer they are cited for; one of them is a theology article**

| Field | Content |
|---|---|
| Check | P13, P4 |
| Location | p. 1, l. 26 and p. 2, l. 28 to 31 (repeated p. 3, l. 93 and p. 4, l. 95 to 98); p. 17, l. 528 to 530 (Blaen et al., 2016); p. 19, l. 597 to 598 (Kobe, 2021); p. 20, l. 621 to 622 (Olley et al., 1993); p. 20, l. 641 to 642 (Walden et al., 1997) |
| Quotation | "Common fingerprinting tools include geochemistry (Olley et al., 1993; Gholami et al., 2019; Lipp et al., 2021; Domingo et al., 2023)"; "nutrients (Blaen et al., 2016; Asadi et al., 2025)"; "mineralogy (Walden et al., 1997; Nukazawa et al., 2021)"; "plant pollen content (Brown, 1985; Kobe, 2021)"; "Kobe, S. L.: Ubuntu as a spirituality of liberation for black theology of liberation, HTS Teologiese Studies / Theological Studies" |
| Concern | The paragraph gives a broad overview of tracer types with 29 citations (counted with Python in l. 26 to 33). Four do not show the use they are cited for. (1) Kobe (2021) is an article on liberation theology (entry l. 597 to 598, confirmed at the publisher's page) and does not deal with pollen, sediment or fingerprinting; Brown (1985), in the same bracket, does cover pollen. (2) Olley et al. (1993) trace sources with lithogenic and fallout radionuclides according to their abstract; the study is cited under "geochemistry", while the radionuclide category follows in l. 27. (3) Walden et al. (1997) is titled "Use of mineral magnetic measurements to fingerprint suspended sediment sources" (l. 641) and belongs to the magnetic category (l. 29), not to "mineralogy". (4) Blaen et al. (2016) is titled "Real-time monitoring of nutrients and dissolved organic matter in rivers" (l. 528 to 529); title and keywords give no indication that nutrients are used as source tracers. Share: 4 / 29 = 13.8 % (Python). Each category keeps at least one fitting citation, so the overview stands; but a reader who follows these four citations does not find the claimed use, and an off-topic theology article suggests a reference manager error that may affect further entries. The grade is moderate rather than minor because four statements cannot be checked from their sources. |
| Suggestion | In l. 31 and l. 98 delete "Kobe, 2021" and the entry in l. 597 to 598; move Olley et al. (1993) to the radionuclide group (l. 27, l. 94) and Walden et al. (1997) to the magnetic group (l. 29, l. 96); replace Blaen et al. (2016) in l. 28 and l. 95 by a study that uses nutrients as source tracers, or delete it; check every entry of the reference list against the statement it supports. |
| Status | verified (Kobe, 2021, entry on page image 19 and source; Olley et al., 1993, abstract); inferred (Walden et al., 1997, and Blaen et al., 2016, title and metadata only) |
| Severity | moderate |
| Source | S1, S4 |

**GB-08 Earlier XRD-based unmixing of sediment provenance, including a known-mixture test, and a Bayesian comparison of mixing model structures are missing from the positioning**

| Field | Content |
|---|---|
| Check | P14 |
| Location | p. 2, l. 36 to 42 (repeated p. 4, l. 103 to 109); p. 2, l. 43 to 57 (repeated p. 4, l. 110 to 124); p. 13, l. 404 to 406 |
| Quotation | "X-ray diffraction (XRD) has recently gained attention as a proxy for mineral abundance in provenance analysis but remains underutilized (Das et al., 2023)."; "Building on the work of Das et al. (2023, 2024), we investigate the potential of binned XRD data as a cost-effective fingerprinting method."; "Our approach can be seen as a hybrid between Bayesian linear mixed models and hierarchical Bayesian models" |
| Concern | The contribution in one sentence: binned XRD peak-area fingerprints used as tracers in a spatially explicit Bayesian inversion that yields erosion rate maps with posterior uncertainty. The Introduction traces XRD-based fingerprinting to Das et al. (2023, 2024) and reviews mixing models. Three works that precede or constrain this contribution are not in the reference list (Python search: "Eberl" and "Andrews" absent; "Cooper" occurs only as E. A. Cooper, co-author of Wilson et al., 1993, l. 649). (1) Eberl, D. D.: Quantitative mineralogy of the Yukon River system: Changes with reach and season, and determining sediment provenance, American Mineralogist, 89, 1784 to 1794, https://doi.org/10.2138/am-2004-11-1225, 2004: quantitative XRD of river sediments with a calculation of the proportions of sediment sources in a mixed sediment, at least three sources identified quantitatively. (2) Andrews, J. T. and Eberl, D. D.: Determination of sediment provenance by unmixing the mineralogy of source-area sediments: The "SedUnMix" program, Marine Geology, 291 to 294, 24 to 33, https://doi.org/10.1016/j.margeo.2011.10.007, 2012: four end members mixed into eleven artificial mixtures, measured by quantitative XRD and unmixed; this is the known-mixture test the manuscript names as the usual test (l. 404 to 406) and replaces by a natural analogue. (3) Cooper, R. J., Krueger, T., Hiscock, K. M., and Rawlins, B. G.: Sensitivity of fluvial sediment source apportionment to mixing model assumptions: A Bayesian model comparison, Water Resources Research, 50, 9031 to 9047, https://doi.org/10.1002/2014WR016194, 2014: thirteen versions of a mixing model differing in error and structural assumptions; median source contributions varied by up to 21 % between versions. The manuscript uses one model structure with a fixed Gaussian data error and tests hyperparameters only (Section 4.1.4). |
| Suggestion | In l. 36 to 42 cite Eberl (2004) and Andrews and Eberl (2012) as earlier XRD-based provenance unmixing and state what binned peak areas add to quantitative XRD mineralogy; in l. 404 to 406 cite Andrews and Eberl (2012) for the known-mixture design and explain why an artificial mixture test was not run; in l. 43 to 57 cite Cooper et al. (2014) and discuss how the choice of error model affects the posterior. |
| Status | verified (summaries read at the USGS Publications Warehouse and the UEA repository; absence from the reference list by Python search) |
| Severity | moderate |
| Source | S1 |

**GB-09 The novelty claims for the spatially informed approach and for a "non-linear mixing model" are not supported: the forward model mixes linearly, and the spatial inversion is adapted from earlier work**

| Field | Content |
|---|---|
| Check | P28, P15, P18, P6 |
| Location | p. 2, l. 58 to 61 (repeated p. 4, l. 125 to 128); p. 15, l. 454 to 455; p. 5, l. 151 to 152, l. 154 (eq. 1) and l. 157 to 158; p. 6, l. 162 (eq. 3) |
| Quotation | "However, these approaches typically yield relative source contributions without translating them into spatially explicit erosion rate maps and implicitly rely on a linear mixing scheme (Niu et al., 2020)."; "The novelty of our method lies in the spatially informed approach of this underdetermined inversion problem, and in the incorporation of non-linear mixing model."; "Hence, the detrital data are a weighted average of the tracer mineral concentrations, with the weights being the erosion rates."; "We cast the erosion rates in log-space to impose a positivity constraint, hence making this non-linear." |
| Concern | The Introduction credits the earlier framework (l. 60 to 61). (1) Eq. 1 gives d_i = sum_j A_ij exp(ε_j) / sum_j exp(ε_j), with exp(ε_j) proportional to the erosion rate of pixel j: a weighted average of source concentrations, as l. 151 to 152 state; eq. 3, d = A · exp(ε), is linear in the erosion rates. The non-linearity lies in the log parameterisation (l. 156 to 158), not in the mixing. The gap named in l. 59 ("implicitly rely on a linear mixing scheme") is therefore not closed by this method, and "non-linear mixing model" in l. 455 describes the model incorrectly. (2) The spatially informed inversion is "a non-linear adaptation of the inversion framework validated in (De Doncker et al., 2020)" (l. 60 to 61); according to the abstracts of De Doncker et al. (2020) and EGU2020-2176, that framework already converts detrital provenance data into erosion rate maps by an inversion with a priori information and model covariance, and names mineral content as a possible tracer. (3) The gap and novelty statements name no literature search (databases, terms, date). The results stand; what changes is the stated contribution. |
| Suggestion | In l. 58 to 61 (l. 125 to 128) and l. 454 to 455 state the contribution as binned XRD peak-area fingerprints used within the spatial inversion of De Doncker et al. (2020), with a log-space parameterisation of the erosion rates that enforces positivity and makes the inverse problem non-linear while the mixing stays linear; replace "the incorporation of non-linear mixing model" by "a non-linear (log-space) parameterisation of the erosion rates within a linear mixing model"; if a wider novelty is claimed, report the literature search. |
| Status | verified (equations and wording on page images 2, 4, 5, 6 and 15); verified for point (2) on the abstracts of De Doncker et al. (2020) and EGU2020-2176 (full text not readable) |
| Severity | moderate |
| Source | S1, S4, SD |

#### Minor corrections

| ID | Location | Quotation | Replacement | Source |
|---|---|---|---|---|
| KK-01 | p. 1, l. 5 | "(steepest descent and Quasi-Newtonian)" | "(steepest descent and quasi-Newton)", as in l. 211 | S1, S2 |
| KK-02 | p. 2, l. 32; p. 4, l. 99 | "E-DNA information (Evrard et al., 2019)" | "environmental DNA (eDNA) (Evrard et al., 2019)" | S1 |
| KK-03 | p. 2, l. 50; p. 4, l. 117 | "Generalist Likelihood Uncertainty Estimation (GLUE)" | "Generalized Likelihood Uncertainty Estimation (GLUE)" | S1 |
| KK-04 | p. 2, l. 51; p. 4, l. 118 | "Maximal Likelihood Estimation (MLE) (similar to the NNLS" | "Maximum Likelihood Estimation (MLE) (similar to the NLLS", abbreviation as introduced in l. 48 to 49 | S1 |
| KK-05 | p. 2, l. 55 to 56; p. 4, l. 122 to 123 | "Bayesian linear mixed models" | "Bayesian linear mixing models (BLMM)", as introduced in l. 53 | S1 |
| KK-06 | p. 2, l. 61; p. 4, l. 128 | "validated in (De Doncker et al., 2020)" | "validated by De Doncker et al. (2020)" | S1 |
| KK-07 | p. 3, l. 70; p. 5, l. 137 | "hyper-parameters" | "hyperparameters", as in l. 281 and l. 370 | S2 |

#### Verification log

| ID | Check | Checked | Values | Result |
|---|---|---|---|---|
| PP-01 | P13 | Statements attributed to Das et al. (2023, 2024), l. 35 to 42 (l. 102 to 109) | Das et al. (2023), Crossref record: XRD spectra with partial least squares regression, Konar reservoir catchment, agricultural share 28 to 43 % of suspended sediment. Das et al. (2024), repository record: MIR with PLS and XRD with MixSIAR, agriculture 36 to 61 %. Full texts not readable. | no finding; "Building on the work of Das et al." is consistent with both abstracts; "expensive and time-consuming" (l. 35) and "remains underutilized" (l. 37) could not be checked in the full text (see Limits) |
| PP-02 | P13 | Statements attributed to Niu et al. (2020), l. 46 to 48 and l. 58 to 59 | Abstract: linear mixing model, multiple composite fingerprints, uncertainty by Gaussian first-order approximation, 66 samples, three sources, mean shares 49.0, 26.5 and 24.5 %; no mention of Bayesian methods. Full text behind paywall. | no finding; "implicitly rely on a linear mixing scheme" is supported by the abstract; whether Niu et al. is the intended source for the description of Bayesian methods (l. 46 to 48) remains open |
| PP-03 | P13 | De Doncker et al. (2020) as the "inversion framework validated" (l. 61, l. 128) | OpenAlex abstract and EGU2020-2176 abstract: least-squares inversion with a priori information and model covariance, detrital zircon ages as fingerprints, synthetic and natural tests, mineral content named as possible tracer | no finding for the citation itself; content used in GB-09 |
| PP-04 | P13 | Further cited claims with ranking or rating: Klages and Hsieh (1975), l. 24 to 25; Haddadchi et al. (2013), Yang et al. (2025), Fathabadi and Jansen (2022), l. 48 to 55; Collins et al. (2020), l. 33 to 35; Torres Astorga et al. (2020), l. 30 | Sources not readable (publisher pages blocked, rate limits; one record without abstract). The segment contains no numbers taken from other works. | no finding; not checked (see Limits) |
| PP-05 | P14 | Search for works preceding or contradicting the contribution | Five queries on XRD provenance unmixing, Bayesian inversion of detrital data for erosion maps, Avdeev et al. (2011), XRD fingerprinting in glacial catchments, Gornergletscher provenance. Reference list check (Python): Eberl 2004 absent, Andrews and Eberl 2012 absent, Cooper et al. 2014 absent, Avdeev et al. 2011 absent, Lipp et al. 2021 present (l. 604 to 606), Belotti 2021 present (l. 522 to 523) | three proposals in GB-08; Avdeev et al. (2011) not proposed (abstract not readable); Lipp et al. (2021) already cited |
| PP-06 | P28 | Inventory of gap and novelty statements | Python on the text: "no study" 0, "not yet" 0, "novel" 2 (l. 454; title of Das et al. 2023, l. 552), "underutil" 2 (l. 37, l. 104, attributed to Das et al. 2023), "first" 14 (enumerations, none a priority claim), "lack" 3 in the body (l. 17, l. 84, l. 433, none a literature gap) | one finding (GB-09); the statement on XRD being underutilized is attributed and treated in PP-01 |
| PP-07 | P14 | Bibliographic details and content of the three proposals of GB-08, checked again during merging | Eberl (2004): American Mineralogist 89, 1784 to 1794, calculation of the proportion of sediment sources in a mixed sediment (USGS Publications Warehouse). Andrews and Eberl (2012): Marine Geology 291 to 294, 24 to 33, four end members, eleven artificial mixtures, quantitative XRD (USGS). Cooper et al. (2014): Water Resources Research 50, 9031 to 9047, 13 model versions, median contributions varying by up to 21 % (UEA repository) | no finding; proposals confirmed |

### Segment 2: Methods, data, study area (p. 5 to 10, l. 143 to 285; Figures 1 to 4)

#### Substantive findings

**GB-10 In the Methods, the iteration index, the tracer index, the pixel index, the erosion rate and the prior misfit each carry two symbols or names, and n stands for three different things**

| Field | Content |
|---|---|
| Check | P38 |
| Location | p. 5, l. 154 to 156 (eq. 1); p. 6, l. 164 (eq. 4); p. 6, l. 175 to 176 (eq. 5); p. 6, l. 183 to 184; p. 7, l. 189 to 190 (eq. 9); p. 7, l. 208 to 209 (eq. 17); p. 8, l. 215 to 216 (eq. 18) and l. 219 (eq. 19); p. 9, l. 245; p. 9, l. 262 to 263; Figures 1b, 2b, 2c, 3d, 3e (p. 22 to 24); Figures 5g, 6g, 7 to 10 (p. 26 to 31) |
| Quotation | "with µ being the step size, and εk+1 the posterior model after k + 1 non-linear iteration steps"; "where Gn is the Jacobian at iteration n"; "Aij is the tracer abundance of tracer mineral i at source position j (pixel j)"; "the abundance of a given tracer t at pixel xy in At,xy as well as in the detrital data dt"; "the prior misfit"; "The model misfit (eq. 7) measures the deviation from the prior" |
| Concern | (a) Iteration index: eq. 17 writes the update with k; eq. 18 and eq. 19 write it with n but keep ε_k in the prior term (page image 8). (b) n has three meanings: number of pixels (eq. 1 sums to n; eq. 4, A_m,n and ε_n), iteration counter (eq. 18, eq. 19, l. 216), and number of tracers in the schematic figures ("tracer n", Figures 1b, 2b, 2c, 3d, 3e), where the equations use m for the number of tracers (eq. 1, eq. 4). (c) Tracer index: i in eq. 1 and l. 155, t in l. 262 to 263; pixel index: j in eq. 1, xy in l. 263; in eq. 9, i and j denote pixels, and in Figure 3d "detrital sample i" denotes a sample. (d) Erosion rate: ė (l. 156, eq. 2), but e in the axis labels of Figures 5g, 6g, 7 to 9 and in "Total absolute difference etrue - epost" (Figure 10). (e) Posterior: p(ε_m&#124;d_obs) in eq. 5, p(ε&#124;d_obs) in l. 176. (f) The term ϕ_prior is called "prior misfit" (l. 184) and "model misfit" (l. 202, l. 245 and further places in Sections 3 and 4, captions of Figures 5 and 6). |
| Suggestion | In Sections 3.1 and 3.2 use k for the iteration counter in eq. 17 to 19 and l. 216, which also replaces the mixed ε_k and ε_n in the prior term of eq. 18 and eq. 19; keep n for the number of pixels and m for the number of tracers and write "tracer m" in Figures 1 to 3; use one pair of indices for tracer and pixel throughout; rename the pixel indices of eq. 9 (for example j and j′); write ė in the figure axes; choose one name for ϕ_prior. |
| Status | verified (page images 5 to 9, 22 to 24, 26 to 31) |
| Severity | minor |
| Source | S2, SD |

**GB-11 The annual suspended sediment export estimate, named as a required input, is given nowhere, and the natural-data runs use a prior defined by a true erosion rate that does not exist for natural data**

| Field | Content |
|---|---|
| Check | P12, P15, P2, P25, P8 |
| Location | p. 5, l. 159 to 160 (eq. 2); p. 3, l. 65 to 66 (repeated p. 5, l. 132 to 133); p. 9, l. 267 to 268; p. 14, l. 426 to 428 and l. 444 to 445; p. 15, l. 452 to 454; p. 16, l. 479 to 480 and l. 490 |
| Quotation | "For simplicity, we redefine the data vector d as scaled by the total erosion rate"; "4) an estimate of the total annual suspended sediment export from the catchment"; "a data standard deviation of 0.01 mm/y, a prior equal to the average true erosion rate, and a step size µ of 0.1" |
| Concern | The manuscript names the export estimate as input d) (l. 132 to 133) and input 4) (l. 453 to 454), and justifies the choice of the Gornergletscher by the "availability of multi-year suspended sediment datasets" (l. 268). "export" occurs only in l. 66, 133, 454, 468 and 479 (Python search), never in Sections 3 and 4; no value, period, gauging station, operator, uncertainty or conversion to an erosion rate (density, area) is given. Eq. 2 scales the data by the total erosion rate, so the absolute scale of the natural posterior maps in mm/y (Figures 13 to 16; "(>8000 mm/y)" in l. 435) depends on how this total was set. The zircon run, whose parameters the XRD and combined runs share ("the same inversion parameters", l. 444 to 445), uses "a prior equal to the average true erosion rate" (l. 428), word for word as in the synthetic tests (l. 325 to 326), although no true map exists for the Gornergletscher; the prior value and its origin are not stated, and the parameters of the known-mixture runs (Section 4.2.1) are not stated at all. The statement in l. 490 covers "The data and codes used for the inversion tests" and does not mention the discharge or sediment record. Question to the authors: does the export estimate define the prior, the scaling of eq. 2, or both, for the natural data? |
| Suggestion | In Section 4.2 (after l. 269 and at l. 428) state the export value used, its period, site, method, source and uncertainty, the conversion constants, the prior value of each natural run and how it was obtained without a true map, and the parameter set of Section 4.2.1; describe the multi-year datasets of l. 268; propagate the export uncertainty or state that the maps are relative; name these data in the statement at l. 490. |
| Status | verified (absence of value, source and prior derivation, by full-text search and on page images); inferred (dependence of the mm/y scale on the total used in eq. 2); assumption (role of the estimate in the natural runs, posed as question) |
| Severity | moderate |
| Source | S2, S3, S4, SD |

**GB-12 The data standard deviation is given in mm/y, while the forward model is called dimensionless and the data are normalised from 0 to 1, so the data covariance cannot be rebuilt**

| Field | Content |
|---|---|
| Check | P8, P20 |
| Location | p. 6, l. 161; p. 5, l. 157 and l. 159 to 160 (eq. 2); p. 6, l. 186 (eq. 8); p. 9, l. 261 to 262; p. 10, l. 294 to 295; p. 11, l. 325; p. 13, l. 384; p. 14, l. 427 to 428; Figure 10, third row (p. 31) |
| Quotation | "This allows us to rewrite the forward model in a simplified, dimensionless form"; "yielding relative mineral concentrations on a scale from 0 to 1"; "a model standard deviation of 3 (dimensionless, as epsilon is dimensionless), a data standard deviation of 0.01 mm/y" |
| Concern | The tracer data are normalised concentrations from 0 to 1 (l. 261 to 262), the reference erosion rate is "set to 1" (l. 157), and the forward model is called dimensionless (l. 161). The model standard deviation is labelled dimensionless (l. 294 to 295), but the data standard deviation carries mm/y in every run (l. 295, l. 325, l. 384, l. 428) and on the axis "Data standard deviation (mm/y)" of Figure 10, third row. After eq. 2 the data are multiplied by the sum of the erosion rates over all pixels, so their magnitude depends on the number of pixels (not stated, GB-24) and on the unit of ė. A reader cannot tell whether σd = 0.01 refers to normalised concentrations, to scaled data, or to a rate per pixel, and therefore cannot rebuild C_d = σd² I (eq. 8). |
| Suggestion | In Section 3.1 state the unit and scale of d after eq. 2 and the unit of σd, and use it consistently in l. 295, l. 325, l. 384, l. 428 and Figure 10. |
| Status | verified (wording and units on page images 5, 6, 9, 10 and 31); inferred (that C_d cannot be rebuilt) |
| Severity | moderate |
| Source | ZF |

**GB-13 All posterior uncertainty metrics rest on a linearised Gaussian approximation that is not checked in any run, including runs far from the prior**

| Field | Content |
|---|---|
| Check | P26 |
| Location | p. 6, l. 177 to 178; p. 2, l. 55 to 57; p. 8, l. 220 to 225 (eq. 20); p. 10, l. 294; p. 14, l. 435; Figure 10, second row (p. 31); Figure 15 (p. 36) |
| Quotation | "We assume weak nonlinearity, where our forward model can be linearized around the prior, hence, the a posteriori probability density remains approximately Gaussian." |
| Concern | The assumption is stated where the method is introduced, and the manuscript presents the absence of posterior sampling as an advantage (l. 56 to 57). The guarantee that eq. 20 to 22 quantify uncertainty holds only within the assumption, which no run tests. With σm = 3 in log space, plus or minus one standard deviation of the prior spans a factor of 0.05 to 20.1, a ratio of about 403 (Python); Figure 10 marks σm = 6.2. The zircon run reaches "(>8000 mm/y)" (l. 435), against at most about 8 mm/y in the XRD run (colour bar of Figure 15). At which ε the Jacobian in eq. 20 is evaluated is not stated. Whether the linearisation holds in such runs is asked as a question; the doubt rests on general inverse theory. |
| Suggestion | For the synthetic case of Figure 5 and the natural XRD case, compare the covariance of eq. 20 with a sampled posterior (for example MCMC or randomise-then-optimise); state in Section 3.3 at which ε G is evaluated, and give the scope of the metrics. |
| Status | assumption (central claim, posed as question); verified (values and wording) |
| Severity | moderate |
| Source | SD |

**GB-14 The quasi-Newton update of eq. 19 inverts a matrix that, by the manuscript's own description of the problem, is singular**

| Field | Content |
|---|---|
| Check | P25, P8 |
| Location | p. 8, l. 217 to 219 (eq. 19); p. 6, l. 170 to 172; p. 8, l. 225 (eq. 20) |
| Quotation | "mathematically, this means that our tracer matrix A is not invertible (it has more columns than rows)."; "the misfit gradient (eq. 16) is preconditioned using curvature information, with the Hessian (i.e. the second derivative of the misfit)" |
| Concern | Eq. 19, checked on page image 8, inverts (G_n^T C_d^-1 G_n) without the term C_m^-1. G has as many rows as tracers (21 for XRD) and as many columns as pixels, more than rows (l. 170 to 172). The n by n matrix G^T C_d^-1 G therefore has rank at most 21 and cannot be inverted. The Hessian of the misfit of eq. 7 contains C_m^-1, as eq. 20 does. The printed update cannot be computed, so the implementation must differ (damping, pseudo-inverse or added C_m^-1). |
| Suggestion | Print in Section 3.2 the update that the code uses, for example ε_n+1 = ε_n - µ_n (G_n^T C_d^-1 G_n + C_m^-1)^-1 ∇ϕ(ε_n), and refer to the corresponding function in the archived code (l. 490). |
| Status | verified (printed form on page image 8); inferred (singularity, from l. 170 to 172) |
| Severity | moderate |
| Source | SD |

**GB-15 The normalised posterior uncertainty, the main comparison metric, carries at least nine names and is defined in two incompatible ways**

| Field | Content |
|---|---|
| Check | P38, P20, P8 |
| Location | p. 8, l. 236 to 239 (eq. 22); p. 8, l. 225 (eq. 20); p. 10, l. 303; p. 10, l. 306 to p. 11, l. 307; p. 11, l. 335; p. 14, l. 436; p. 15, l. 441 to 442 and l. 446 to 447; Figures 5 and 6, panels f and h and captions (p. 26, 27); Figures 7 to 9, middle scatterplots (p. 28 to 30); Figure 10, second column (p. 31); Figures 14 to 16, right panel and annotation (p. 35 to 37) |
| Quotation | "The third metric is the ratio between the posterior model covariance and the “prior” model covariance"; "normalised posterior variance"; "low resolution, and a high total normalized uncertainty"; "The normalized posterior uncertainty is slightly lower at 0.82." |
| Concern | Section 3.3 defines the third metric as eq. 22, the element-wise ratio of the square roots of posterior and prior covariance, a map of standard-deviation ratios. Section 4.2.2 reports a scalar, written in l. 436 as tr(C_m,post) / tr(C_m), a ratio of traces of variances without square root, and calls it "normalized posterior uncertainty" in l. 441 and l. 446 to 447. The posterior covariance is written with a tilde in eq. 20 and eq. 22 but as C_m,post in l. 436. Across text and figures the measure appears as "ratio between the posterior model covariance and the “prior” model covariance" (l. 236 to 237), "normalised posterior variance" (l. 303), "normalised posterior covariance" (captions of Figures 5 and 6), "Normalised covariance trace" (Figures 5h, 6h), "posterior covariance" (l. 306, for Figure 5H), "Posterior uncertainty" with axis "Trace(post. cov.)" (Figures 7 to 9), "Normalised posterior uncertainty" with axis "Trace(post.covar.)" (Figure 10), "Total normalised posterior uncertainty" (Figures 14 to 16) and "total normalized uncertainty" (l. 436). The axis label "Trace(post. cov.)" has no denominator, although its values (about 0.73 to 0.96) can only be ratios. A standard-deviation ratio of 0.87 corresponds to a variance ratio of 0.757 (0.82 to 0.672, 0.86 to 0.740; Python), so which quantity the reported 0.87, 0.82 and 0.86 are matters for their reading and for recomputing them. The comparison between the three natural cases stays valid as long as one quantity is used throughout. |
| Suggestion | In Section 3.3 after eq. 22 define two named quantities with symbols, a per-pixel normalised posterior standard deviation (eq. 22) and a scalar normalised trace tr(C̃_m) / tr(C_m) as a new equation; use one symbol for the posterior covariance, including l. 436; label every panel, axis and caption of Figures 5 to 10 and 14 to 16 and every mention in Section 4 with one of these two names. |
| Status | verified (name forms in the text and on page images 8, 10, 11, 14, 15, 26 to 31, 35 to 37); inferred (that Figures 7 to 9 show the normalised trace, from the value range) |
| Severity | moderate |
| Source | S2, S3, SD |

**GB-16 The measurement and computing environment is not specified**

| Field | Content |
|---|---|
| Check | P35 |
| Location | p. 9, l. 252 to 255; p. 14, l. 423 to 424; p. 16, l. 490 |
| Quotation | "Secondly, these samples are then powdered and analysed using XRD producing one diffractogram per sample" |
| Concern | Making the code and data available (l. 490) helps reproducibility. Missing are the diffractometer, radiation, 2θ range, step size, counting time, sample mount and grinding size, the WinXRD version, the U-Pb instrument, and the programming language and dependencies of the code. These settings affect peak areas and therefore the fingerprints. The detrital sampling (sampler, intake, integration) is treated in GB-51. |
| Suggestion | Add an instrument and software paragraph to Section 3.4, and for U-Pb to Section 4.2.2. |
| Status | verified (absence) |
| Severity | moderate |
| Source | SD |

**GB-17 The XRD processing chain and the concatenation of the zircon and XRD data cannot be rebuilt from the text**

| Field | Content |
|---|---|
| Check | P8 |
| Location | p. 9, l. 254 to 262; p. 13, l. 396 to 398; p. 15, l. 443 to 445 |
| Quotation | "In a fifth step, diagnostic 2θ windows for each mineral are selected from RRUFF database reference spectra"; "we combine both zircon and XRD data by concatenating the tracer concentration matrices A of the zircon and XRD approaches, as well as both corresponding detrital data vectors." |
| Concern | Not given: the 2θ windows per mineral (position, width, number), the rule for choosing them from RRUFF, the Peak Finder thresholds and fitting function, and whether "average the total peak area" (l. 260) means a mean or a sum. For the concatenation, the relative weighting of the two blocks (variances, normalisation across blocks) is not stated, although both use the same σd (l. 444 to 445). If these are in the archive (l. 490), the text does not say so. The zircon method is treated in GB-19. |
| Suggestion | Add a table of 2θ windows per mineral and the Peak Finder settings (Section 3.4 or a supplement), state the weighting used in the concatenation (Section 4.2.2), and point to the files in the archive. |
| Status | verified (absence) |
| Severity | moderate |
| Source | SD |

**GB-18 The described normalisation by each sample's maximum peak area does not keep the linear mixing relation of eq. 1, and Figures 11 and 15 show fingerprints that no stated normalisation links**

| Field | Content |
|---|---|
| Check | P25, P8, P3 |
| Location | p. 9, l. 260 to 264; p. 5, l. 151 to 152 and l. 154 (eq. 1); Figure 11 (p. 32); Figure 15, fingerprint panel (p. 36); Figure 16, fingerprint panel (p. 37) |
| Quotation | "At the end, these are normalized within each sample by dividing by the maximum observed peak area, yielding relative mineral concentrations on a scale from 0 to 1"; "Normalised abundance per mineral or age"; "geological map, and the source fingerprints." |
| Concern | Eq. 1 needs detrital values that are erosion-weighted averages of the source values. Dividing each sample by its own maximum breaks this unless all sources share the same absolute maximum. Two-source example (peak areas 10, 5, 1 and 2, 8, 4, mixed 50:50): the normalised mixture is (0.923, 1.0, 0.385), whereas the mixture of the normalised sources is (0.625, 0.75, 0.3); unconstrained least squares on the normalised values, rescaled to a sum of one, recovers 0.556 and 0.444 instead of 0.5 and 0.5 (Python). Figure 11 shows per-unit fingerprints with the longest bar of each column at the same length (243 to 245 px), consistent with normalisation by the maximum. Figure 15 stacks, for each mineral, the shares of the seven units, which sum to one per mineral: a normalisation across sources, not within a sample. Normalising the measured Figure 11 values of each mineral to a sum of one gives shares that differ from Figure 15 by up to 0.21 (mean 0.054), for example Antigorite in ZSF serpentinites 0.43 against 0.64, Fayalite 0.54 against 0.73, Anorthite in ZSF metabasites 0.33 against 0.17; normalising each unit first (maximum difference 0.17) or to unit length (0.18) does not remove the difference. Which normalisation enters A and d, and whether Figures 11 and 15 are drawn from the same matrix, is not stated. The grade is major because, if the described normalisation enters the inversion, the unmixing behind Figures 13 to 16 is biased. |
| Suggestion | State in Section 3.4 as a formula the normalisation that enters A and d, and in the captions of Figures 15 and 16 how the stacked shares are computed; check that Figures 11 and 15 are drawn from the same matrix. If the per-sample maximum is used, show with mixtures of measured raw source diffractograms in known proportions, processed through the full chain, that the inversion recovers the proportions; otherwise use a mixing-consistent quantity (peak areas against an internal standard, or the normalisation included in the forward model). |
| Status | verified (wording, figure labels, measured bar lengths and share differences); inferred (loss of linear mixing, by calculation); assumption (which normalisation the code uses and why Figures 11 and 15 differ, posed as question) |
| Severity | major |
| Source | SD, AB |

**GB-19 Two inputs rest on sources a reader cannot access: the zircon method in an unpublished master's thesis and a geological map built partly from a personal communication**

| Field | Content |
|---|---|
| Check | P12, P8 |
| Location | p. 9, l. 270 to 272; p. 14, l. 423 to 425; p. 17, l. 522 to 523; Figure 4, credit line (p. 25); Figure 12 (p. 33); Figure 14, age bins (p. 35); p. 16, l. 490 |
| Quotation | "we infer the lithology based on regional geological knowledge"; "following the methodology described in (Belotti, 2021)"; "unpublished master’s thesis, 2021." |
| Concern | The manuscript names where the zircon method and the map come from. Both sources are not accessible. The zircon extraction and U-Pb dating protocol is given only by reference to an unpublished thesis (l. 522 to 523); the manuscript gives no laboratory, instrument, number of grains per sample, or rule for the 13 age bins shown in Figure 14. The geological map that defines matrix A combines a published map, a personal communication and an interpretation under ice based on regional knowledge (l. 270 to 272); the credit line of Figure 4 reads "Geological data: data from Steck et al., 2015, personal communication by L. Baumgartner, outcrops by GeoCover" and "Land cover data: SwissTopo 2018" (page image 25). GeoCover and swisstopo appear only in the figure, not in the reference list. The statement in l. 490 says nothing about either source. |
| Suggestion | Add a short supplement on the zircon method (sample preparation, instrument, standards, number of grains, age binning) or deposit the thesis in an open repository and cite it with a persistent identifier; deposit the inferred geological map as a raster or vector file with the rules used under ice; add GeoCover and the swisstopo land cover dataset with version to the reference list; name all of these in the statement at l. 490. |
| Status | verified |
| Severity | moderate |
| Source | S2, SD |

**GB-20 The lithological units carry different names in the study area description, the legends, the captions and the results, and the abbreviations ZSF, MR and S.,T.,G. are used before or without definition**

| Field | Content |
|---|---|
| Check | P38, P3 |
| Location | p. 10, l. 274 to 277; p. 10, l. 299; p. 14, l. 411, l. 414 and l. 431 to 434; Figure 4, legend (p. 25); Figure 5j, legend (p. 26); Figure 11, caption (p. 32); Figure 12, legend and caption (p. 33); Figure 13, labels (p. 34); Figures 15 and 16, legends (p. 36, 37) |
| Quotation | "Penninic Mesozoic sedimentary units (Bündnerschiefer) consist mainly of calcareous mica schists and quartzites"; "Zermatt - Saas Fee unit (ZSF sediments)"; "Zermatt-Saas Fee (ZSF) ophiolites"; "Monte Rosa garnet-gneiss (MR g-g) unit"; "The Stockhorn, Tuftgrat, and Gornergrat units"; "Stockhorn-Turftgrat-Gornergrat" |
| Concern | Figure 4 defines seven units, and the results use them consistently in number. Their names change from place to place, and the study area paragraph (l. 273 to 279) describes five groups that do not map one to one onto the seven units. (a) The unit that carries the natural known-mixture test is "Penninic Mesozoic sedimentary units (Bündnerschiefer)" in the study area text (l. 274 to 275, the only occurrence of "Bündnerschiefer" in the text), "Zermatt - Saas Fee sediments" in the Figure 4 legend, "Zermatt Saas-Fee sediments" (l. 299), "Zermatt - Saas Fee sediment unit" (l. 411), "Zermatt- Saas Fee sediments unit" (Figure 12 caption) and "ZSF sediments" (l. 414, Figures 5, 11, 13, 15, 16). The link between the first two rests on the outcrop line "metamorphic bündnerschiefer, calcarious mica schist" in the Figure 4 legend. (b) The Monte Rosa gneiss unit appears as "Monte Rosa (garnet gneiss and micaschist)" (Figure 4), "Monte Rosa (gneiss, micaschist)" (Figures 11, 13), "Monte Rosa garnet-gneiss (MR g-g) unit" (l. 432) and "MR gneiss, mica" (Figures 5, 15, 16). (c) The Stockhorn unit appears as "Stockhorn basement, Tuftgrat Mesozoic and GornergratPermo-Mesozoic" (Figure 4, also Figure 12), "The Stockhorn, Tuftgrat, and Gornergrat units" (l. 276), "Stockhorn-Turftgrat-Gornergrat" (Figure 11, with a misspelt "Tuftgrat"), "Stockhorn, Tuftgrat, Gornergrat" (Figure 13) and "S.,T.,G." (Figures 5, 15, 16). (d) "ZSF" is first used at l. 414, in the Figure 5 legend and in the Figure 11 caption, but defined only at l. 431; "MR" is defined only as "MR g-g" (l. 432), while "MR granite" (Figures 5, 15, 16) is not defined; "S.,T.,G." is not defined. Question to the authors: is the unit "Zermatt - Saas Fee sediments" the same as the "Penninic Mesozoic sedimentary units (Bündnerschiefer)" of l. 274 to 275? |
| Suggestion | Introduce in Section 4 (l. 273 to 279) one name and one abbreviation for each of the seven units of Figure 4, in the form used later (for example "Zermatt-Saas Fee sediments (ZSF sediments; Bündnerschiefer)", "Monte Rosa garnet gneiss and micaschist (MR gneiss)", "Stockhorn, Tuftgrat and Gornergrat units (STG)"), and use exactly these names in l. 299, l. 411, l. 414, l. 431 to 434 and in all legends and captions; this also corrects "Turftgrat" (Figure 11 caption), "GornergratPermo-Mesozoic" (Figures 4 and 12) and the spacing in "Zermatt- Saas Fee" (Figure 12 caption). |
| Status | verified (name forms and counts on page images 10, 14, 25, 26, 32 to 37); assumption (identity of "Bündnerschiefer" and "Zermatt - Saas Fee sediments", posed as question) |
| Severity | minor |
| Source | S2, AB, S3, SD |

**GB-21 Figures 1 to 3 use symbols and colours that no legend or caption explains**

| Field | Content |
|---|---|
| Check | P29 |
| Location | Figure 1b, Figure 2b, Figure 3b (arrow symbol); Figure 2b (black bars); Figure 2c (colour ramps) (p. 22 to 24) |
| Quotation | "(b) tracer concentrations in suspended sediments, (c) tracer concentration maps based on geology and lithological fingerprints." |
| Concern | The black arrowhead beside the maps in Figures 1b, 2b and 3b (presumably a north arrow) is not explained. In Figure 2b four bars are coloured like the tracer maps in Figure 2c and seven are black; the meaning of black is not given. In Figure 2c only the lowest layer has a colour ramp. |
| Suggestion | Explain the arrow and the black bars in the captions of Figures 1 to 3, or remove them. |
| Status | verified |
| Severity | minor |
| Source | AB |

**GB-22 The caption of Figure 4 lists nouns only and does not explain the insets, the ELA line or the outcrop overlays**

| Field | Content |
|---|---|
| Check | P29 |
| Location | Figure 4, caption, inset legend and source note (p. 25) |
| Quotation | "Study area: location, land cover and geology." |
| Concern | The figure combines a geological map with outcrops, a land cover inset with "ELA estimation", a location map and a globe; the caption names none of these, "ELA" is not resolved in figure, caption or text, and the main map carries no coordinates (only a 1 km scale bar). |
| Suggestion | Extend the caption to say what each part shows, resolve ELA, and state the data sources and the date of the land cover data there. |
| Status | verified |
| Severity | minor |
| Source | AB |

#### Minor corrections

| ID | Location | Quotation | Replacement | Source |
|---|---|---|---|---|
| KK-08 | p. 6, l. 175 (eq. 5) | "p(εm&#124;dobs)   p(dobs&#124;εm)" (no relation sign between the two terms, page image 6) | "p(εm&#124;dobs) ∝ p(dobs&#124;εm)", or "=" if the denominator p(dobs) is kept | ZF |
| KK-09 | p. 6, l. 181 | "becomes Tarantola (2005):" | "becomes (Tarantola, 2005):" | ZF |
| KK-10 | p. 7, l. 189 (eq. 9) | "Cm(i, j) = σm² exp(s_ij²/L²)" (no minus sign in the exponent, page image 7) | "Cm(i, j) = σm² exp(-s_ij²/L²)" | SD |
| KK-11 | p. 7, l. 197 (eq. 12) | "G = A · exp(ε)" | "G = A · diag(exp(ε))" | ZF |
| KK-12 | p. 7, l. 201 (eq. 14) | "G C_d^-1 (dε - dobs)" (no transpose, page image 7) | "G^T C_d^-1 (dε - dobs)", as in eq. 16 | ZF |
| KK-13 | p. 8, l. 236 | "considerately" | "considerably" | ZF |
| KK-14 | p. 9, l. 245 | "weighed by the model covariance" | "weighted by the model covariance" | ZF |
| KK-15 | p. 9, l. 267; Figure 11, caption (p. 32) | "Gorner-gletscher catchment" | "Gornergletscher catchment", as in l. 272 and l. 282 | S2, AB |
| KK-16 | Figure 3c, legend (p. 24) | "quarz pattern alignment" | "quartz pattern alignment" | S2, AB |
| KK-17 | Figure 4 and Figure 12, legends (p. 25, 33) | "calcarious mica schist"; "caclcite-zoisite amphibolites"; "silimanite-biotite gneiss"; "biotite schits"; "metamorphic bündnerschiefer"; "epidotamphibolites, garnetamphibolites" | "calcareous mica schist"; "calcite-zoisite amphibolites"; "sillimanite-biotite gneiss"; "biotite schists"; "metamorphic Bündnerschiefer"; "epidote amphibolites, garnet amphibolites" | S2, AB |

#### Verification log

| ID | Check | Checked | Values | Result |
|---|---|---|---|---|
| PP-08 | P12 | Inventory of data sources in Methods and Section 4 against the statement in l. 490 | (1) synthetic true map, fingerprints, maps, blended and reduced sets (l. 288 to 289, 327 to 358): covered by "inversion tests"; (2) raw source and detrital diffractograms (l. 250 to 253): not mentioned; (3) Peak Finder output (l. 254): not mentioned; (4) RRUFF reference spectra (l. 257): public, cited; (5) inferred geological map (l. 270 to 272): not mentioned; (6) GeoCover outcrops, SwissTopo 2018 land cover: figure credit only; (7) zircon U-Pb ages (l. 423 to 425): not mentioned; (8) sample metadata (l. 251, 391 to 392, 406, 413, 423 to 424): not mentioned; (9) export estimate and multi-year datasets (l. 133, 268, 453, 479): no value anywhere; (10) code: DOI given. No appendices or supplements. | findings GB-11, GB-19, GB-56 |
| PP-09 | P12 | Reachability of the DOI in l. 490 and repository description | https://doi.org/10.5281/zenodo.17120374 redirects to the Zenodo record "fdedonck/Non-Linear-XRD-Inversion: First public release", v1.0.0, 15 September 2025, CC BY 4.0, one zip file of 49.3 MB; repository README lists folders "Forward-Inverse testing", "Generating XRD fingerprints", "INPUT", "OUTPUT", "Zircon testing" and mentions raw XRD, RRUFF and raw zircon data; the zip file was not opened | link reachable, no finding on reachability; content of the statement in GB-56 |
| PP-10 | P38 | Identifiers that are consistent | QN and SD defined at l. 210 to 211 and used consistently; JS defined at l. 345; RRUFF uniform; "Furgg series" uniform; hyperparameter symbols of the Figure 10 caption match l. 367 to 370; pixel size from l. 294 and l. 373: 1200 / 4 = 300.0 m and 3000 / 10 = 300.0 m (Python); 21 tracer minerals in l. 358, l. 393, l. 397, Figure 9, Figure 11, Figure 15; "WinXRD Peak Finder" and "Peak Finder" denote one tool | no finding |
| PP-11 | P38 | Glacier and catchment name | "Gornergletscher" 2 (l. 272, 282), "Gorner Glacier" 4 (l. 392, 400, 498, 499), "Gorner-gletscher" 2 (l. 267, Figure 11), "Gorner gletscher" 1 (l. 463), "Gorner glacier" 2 (legends of Figures 15, 16); one glacier, spelling only | KK-15; the form in l. 463 is corrected within GB-42 |
| PP-12 | P38 | Names of the two schemes and of hyperparameters | "quasi-Newton" 2 (l. 211, 296), "Quasi-Newton" 3 (l. 287, 320, Figure 5 caption), "Quasi-Newtonian" 1 (l. 5); "hyper-parameters" 2 (l. 70, 137), "hyperparameter(s)" 2 (l. 281, 370) | KK-01, KK-07 |
| PP-13 | P10 | Design sketch from the whole manuscript | Type: method development, synthetic forward-inverse tests plus one natural catchment. No explicit research questions; synthetic aims l. 280 to 281, natural aims 1 to 3 l. 282 to 285; stated expectations l. 410 to 411 and l. 72 to 73. Cases: one true map with one hotspot; scenario 1 three maps, scenario 2 20 blending levels, scenario 3 1 to 21 tracers; five sweeps; natural: seven units, 21 minerals, multiple detrital samples at the Gorner-Grenz confluence (number not stated), one dated sample (28 June 2019, 13:30). Controls: synthetic truth; QN against SD; one unit without outcrops as negative control; zircon, XRD and combined. Data sources: synthetic (model-generated), XRD of bedrock and suspended sediment (primary, processed), zircon U-Pb (primary, method in a thesis, one unit imputed), geological map (secondary plus inference under ice), export estimate (not specified), prior (from the truth in synthetic runs, same wording in natural runs). | no finding by itself; basis for GB-01 to GB-03, GB-11, GB-13, GB-14, GB-16 to GB-19, GB-23, GB-26, GB-29, GB-30, GB-32, GB-33, GB-38, GB-39, GB-41, GB-42, GB-50, GB-51, GB-55 |
| PP-14 | P10 | Research gaps named against test aims | gaps: costly methods (l. 35), XRD underused (l. 36 to 37), no spatial maps and linear mixing (l. 58 to 59), glacierized catchments (l. 62 to 63); aims l. 280 to 285 | gaps "costly" and "linear mixing" lead to GB-02 and GB-09; the other two are answered by the design |
| PP-15 | P32 | Claims "validate", "confirms", "supports the reliability" against any independent check of results | "validat" in l. 3, 8, 69, 74, 415, 451; no independent re-check of attributions or fingerprints | covered by GB-38 and GB-39 |
| PP-16 | P30 | Reported corrections against reported runs | SD gradient normalisation introduced before the runs of Figure 6 (l. 312); MR g-g substitution before the zircon run (l. 433 to 434); no dated corrections | no finding; both disclosed |
| PP-17 | P19 | Provenance class of each data source and share of result figures on model-generated data | Figures 5 to 10 synthetic: 6 of 12 result figures, 50.0 % (Python), named "fully synthetic" (l. 280); map under ice named as inferred (l. 270 to 272) | classes named in the text, except the imputed fingerprint in the figures (GB-41) and the prior and export (GB-11) |
| PP-18 | P27 | Unchecked components and where their output flows | inferred lithology under ice to A (all natural runs); export estimate to the scaling of d; per-sample normalisation to A and d; SD gradient normalisation to Figure 6 | traced in GB-11, GB-18, GB-26, GB-39, GB-50 |
| PP-19 | P36 | Statements from impression against the records | "In many of these cases" (l. 353) against 6 of 20 missing points; "approximately the same posterior solution" with 7 tracers (l. 360) against 197.6 for 7 and more tracers (Figure 9); "Some spillover" (l. 414 to 415) not quantified | first in GB-30; second consistent; third in GB-39 |
| PP-20 | P6 | Further absolute statements against counter-evidence | "in all cases, both data misfit and model misfit increase as map uncertainty grows" (l. 341 to 342) against Figure 7: data misfit about 3.25, 3.49, 3.69 × 10^6, model misfit about 1.56, 1.92, 2.46; "The only unit not having outcrops" (Figure 12 caption) against l. 411 | consistent; no finding |
| PP-21 | P5 | Stopping rule and scheme rule against the runs | stopping rule l. 243 to 244 permits fixed maxima (25, 100); QN named for Section 4.2.2 (l. 426), implied for 4.1.3 and 4.2.1 by l. 320 | no finding |
| PP-22 | P33 | Statements on effort | "more iterations are needed" (l. 315) quantified by the axes of Figures 5 and 6 (100 against 200); "expensive and time-consuming" (l. 35) | first: no finding; second: GB-02 |
| PP-23 | P9 | Each outlook proposal against own results | recommendations a) to c) (l. 463 to 466); land use (l. 466, 487 to 488); other tracers (l. 488 to 489); storage caution (l. 466 to 468) | GB-50, GB-55; storage caution consistent with the model, its placement in GB-01 |
| PP-24 | P17 | Place of each disclosed limitation | underdetermination (l. 170 to 172), weak non-linearity (l. 177 to 178), inferred geology (l. 270 to 272), zircon gaps (l. 430 to 434): at the method; SD normalisation, storage, grain size: Results or Discussion only | GB-01, GB-26, GB-41, GB-51; the rest no finding |
| PP-25 | P31 | Intended effect of each processing component against measurement | Peak Finder, quartz alignment, window averaging, per-sample normalisation, identical protocol for source and detrital samples: none measured (Section 3.4; l. 471 to 476) | covered by GB-18 and GB-38 |
| PP-26 | P7 | Collection window and method versions against reported data | one dated sample (28 June 2019); other dates not given; one method change (SD normalisation) applying to all reported SD runs; QN unchanged | GB-26; missing dates in GB-29 and GB-39 |
| PP-27 | P37 | Figures showing changed values | Figure 6 shows the normalised SD variant (GB-26); Figures 14 and 16 show the imputed fingerprint (GB-41); no other recalculated values | no further finding |
| PP-28 | P3 | Figure 3d: windows against bars | 11 grey 2θ windows and 11 concentration bars; Figures 1b, 2b, 3e: 11 tracer bars each | no finding; Figures 1 to 3 are conceptual by content |

### Segment 3: Results (p. 10 to 15, l. 286 to 449; Figures 5 to 16)

#### Substantive findings

**GB-23 The synthetic tests on which the recovery and robustness claims rest favour recovery: the prior mean is taken from the truth, adding noise is not stated, and there is only one true map**

| Field | Content |
|---|---|
| Check | P9, P10 |
| Location | p. 10, l. 288 to 295; p. 11, l. 325 to 326; p. 13, l. 374 to 376; p. 16, l. 482 to 483; Figure 5a (p. 26); Figure 10, first row (p. 31) |
| Quotation | "a prior equal to the average true erosion rate"; "Using synthetic forward-inverse experiments, we show that the true erosion pattern can be reliably recovered, and that the method is robust across a range of parameters." |
| Concern | (1) Every synthetic run sets the prior mean to the mean of the true map (l. 295, l. 325 to 326). The manuscript shows the effect itself: "A longer smoothing distance effectively constrains the posterior closer to the prior (set here as the average true erosion rate) resulting in a reduced difference between posterior and true values" (l. 374 to 375). In Figure 10, first row, the summed error falls from about 197.6 at L = 1200 m (interpolated) to 76.6 at L = 3000 m, 61 % lower (GB-33): a smoother solution scores better because the prior already holds the true mean. (2) The text never states that noise was added to the synthetic detrital data; the only mention of noise concerns XRD background (l. 255). The data come from the same forward model on the same grid and map that the inversion uses (l. 288 to 290). (3) There is one true map with a single hotspot (Figure 5a); other patterns (several hotspots, a hotspot in a small unit, uniform erosion) are not tested. Whether (2) makes the recovery look better than with real data is a question to the authors; it rests on general inverse theory. The grade is major because the Conclusions' "reliably recovered" and "robust" rest on these tests. |
| Suggestion | Counter-design for Section 4.1: add noise at the stated σd and at the replicate variance of real XRD peak areas; set the prior mean from an independent estimate (for example the export-based mean with a bias of plus or minus 50 %); test several true maps (two hotspots, a hotspot in ZSF sediments, uniform, gradient); perturb the fingerprints between forward and inverse runs by within-unit variability; report error distributions over realisations. State in Section 4.1.1 whether noise was added, and qualify l. 482 to 483 accordingly. |
| Status | verified (points 1 and 3; absence of a noise statement in point 2); assumption (effect of missing noise, posed as question) |
| Severity | major |
| Source | SD |

**GB-24 The grid size and several counts are stated nowhere, and the summed error over all pixels is quoted in mm/yr as if it were a rate**

| Field | Content |
|---|---|
| Check | P20, P22 |
| Location | p. 10, l. 294; p. 12, l. 352 to 353; p. 15, l. 443 to 445; Figure 5, caption panel g and Figure 5k (p. 26); Figure 7, x-axis and colour bar (p. 28); Figure 8, left scatterplot (p. 29); Figure 9 (p. 30); Figure 10, first column (p. 31); Figure 11, caption (p. 32); Figure 14, age bins (p. 35) |
| Quotation | "a smoothing distance of 4 times the pixel size (L = 1200 m)"; "with errors exceeding 700 mm/yr for JS"; "(g) sum of difference between "true" and posterior erosion map during non-linear iterations" |
| Concern | The figures label the error as a sum over pixels ("Σ&#124;etrue - epost&#124;", Figure 8; "sum&#124;etrue - epost&#124;", Figure 10), while l. 352 to 353 gives it in "mm/yr" without saying it is a sum, and in a unit spelt "mm/y" everywhere else (l. 295, l. 325, l. 384, l. 428, all figures). Neither the number of pixels nor the catchment area is stated; the pixel size follows only from l. 294 (1200 m / 4 = 300 m). Without the pixel count, a reader cannot convert the summed error into a mean error per pixel and compare it with the erosion rates of 0 to 3 mm/y in Figure 5a. The same applies to the area mismatch of scenario 1 (Figure 7, up to about 1.14 × 10^7 m², which is 1.14 × 10^7 / 300² = 127 pixels; its share of the catchment cannot be computed). Further counts must be derived by the reader: 21 synthetic tracers (Figure 5k, bars A to U; Figure 9 "All tracers (21)"), 7 units (Figure 11 caption), 13 zircon age bins (Figure 14) and thus 13 + 21 = 34 tracers in the combined inversion, and 21 pairs for the average JS distance (C(7,2), Python). |
| Suggestion | In Section 4.1.1 state the pixel size, the number of pixels and the catchment area; in l. 352 write the error as a sum (or give the mean per pixel) with the unit "mm/y"; express the area mismatch of scenario 1 also as a share of the catchment area; state the number of units, synthetic tracers, zircon age bins and the size of the combined tracer matrix in Sections 4.1.1 and 4.2.2. |
| Status | verified (labels and wording on page images 10, 12, 26 to 31, 32, 35); inferred (pixel size, pixel equivalent and derived counts) |
| Severity | moderate |
| Source | S3, S2 |

**GB-25 Figure 5b does not show the westward shift and the overshoot of the posterior hotspot that Figure 5c reveals, so the text overstates the agreement between true and posterior maps**

| Field | Content |
|---|---|
| Check | P3 |
| Location | p. 10, l. 296 to 298; Figure 5a, 5b, 5c (p. 26) |
| Quotation | "The quasi-Newton (QN) approach generates a posterior erosion rate map that closely matches the true erosion pattern, both in spatial distribution and magnitude (Figure 5B). The primary differences occur within larger lithological units" |
| Concern | The difference map (Figure 5c) is a useful addition, and read by eye panels a and b agree. Measured against panel c, the agreement is weaker than the text says. (1) Location: the centroid of the hotspot cells lies at x = 491.1 px in panel a and at 1168.6 px in panel b; with the panel offset of 698 px (registered on the black outlines), the posterior hotspot is shifted 20.5 px west. One raster cell measures 12 px, so the shift is 1.7 cells, about 510 m at the 300 m pixel size implied by l. 294. (2) Magnitude: inverting the colour bar of panel c gives a minimum of minus 2.26 at the hotspot; the true value at the same place in panel a is 2.65. Since panel c shows true minus posterior, the posterior there is 2.65 + 2.26 = 4.91, a factor of 1.85 above the true value (Python); because hillshade blending lightens the colours, 2.26 is a lower bound. (3) Display: the colour bar of panels a and b ends at 3.0, so a posterior of about 4.9 is drawn as 3.0 and the overshoot is invisible in panel b. (4) The largest difference sits in and next to the small outlined unit in the centre, not "within larger lithological units". The grade is major because this forward-inverse test is the manuscript's validation of the method (Abstract, l. 7; Conclusions, l. 482). |
| Suggestion | In Section 4.1.1 (l. 296 to 298) state the hotspot offset and the peak overshoot taken from the model output; set the colour scale of Figure 5b (and 6b) to the posterior maximum or mark clipped cells; add the true and posterior peak values to the caption of Figure 5. |
| Status | verified (shift, colour bar limit, minimum of panel c, measured at 300 dpi); inferred (posterior value 4.91 and factor 1.85, computed from two measured values; lower bound) |
| Severity | major |
| Source | AB |

**GB-26 The choice of the quasi-Newton scheme rests on a comparison under unequal conditions, and the error curves of Figures 5g and 6g show the steepest descent run ending with the lower error**

| Field | Content |
|---|---|
| Check | P3, P9, P10, P11, P7, P17 |
| Location | p. 11, l. 310 to 321; p. 10, l. 293 to 295 and l. 305 to 306; p. 8, l. 213 to 216 (eq. 18); p. 1, l. 4 to 5; Figure 5c, 5g (p. 26); Figure 6c, 6g and caption (p. 27) |
| Quotation | "Based on these findings, we adopt the Quasi-Newton (QN) approach for all subsequent tests, as it provides a more stable and accurate reconstruction of the erosion rate patterns."; "In initial experiments, the steepest descent approach proved unstable, requiring the normalization of the gradient." |
| Concern | Comparing the two schemes is an aim stated in the Abstract (l. 4 to 5), and the text explains the steepest descent behaviour with care. The runs, however, differ in more than the scheme: QN ran 100 iterations (l. 293), SD 200 (axes of Figure 6, not stated in the text); SD used a normalised gradient that eq. 18 does not show and that is disclosed only in the Results (l. 312); for SD no parameter set is given, for QN no step size. Measured on Figures 5g and 6g at 300 dpi, the summed difference between true and posterior map reaches its minimum of 197.3 at iteration 22 for QN and ends at 201.0 at iteration 100; SD is at 211.7 at iteration 100 and ends at 193.0 at iteration 200, 4.0 % below the QN end value (measurements at 150 dpi agree within 0.4). The largest absolute difference (colour inversion of panel c) is at least 2.26 for QN and at least 1.58 for SD; the colour bars of 5c and 6c end at plus or minus 2.36 and 1.72, which also makes the visual comparison misleading. By the manuscript's own accuracy metric, SD is not less accurate at the end of its run; the advantage of QN is speed. The QN curve also does not simply plateau (l. 305 to 306): it rises by 3.7 after iteration 22. Stability is not quantified, and the comparison uses one true map and one data set. The grade is major because the scheme adopted for all later tests and a stated aim depend on this comparison. |
| Suggestion | In Section 3.2 add the normalised SD update rule with its step length after eq. 18 and name the variant in the caption of Figure 6; in Section 4.1.2 run both schemes from the same start with the same stopping rule (l. 243 to 244) or the same computing budget, report final and minimum summed error, peak difference, data misfit, iterations and run time in a table, plot panels c of Figures 5 and 6 on the same colour range, and rephrase l. 320 to 321 to what the table shows (for example "converges in fewer iterations"). |
| Status | verified (iteration counts from text and axes; curve values and colour bar limits measured); inferred (peak differences as lower bounds from colour inversion) |
| Severity | major |
| Source | S3, AB, SD |

**GB-27 The oscillations in the posterior covariance that the text places after 125 iterations are not visible in Figure 6, and the cited panel pair names the same panel twice**

| Field | Content |
|---|---|
| Check | P3, P4 |
| Location | p. 11, l. 316 to 317; Figure 6g, 6h (p. 27) |
| Quotation | "This limited sensitivity to strong gradients also leads to oscillations in the posterior covariance, visible after 125 iterations, as the Jacobian fluctuates between iterations (Figure 6G versus Figure 6G)." |
| Concern | "(Figure 6G versus Figure 6G)" compares a panel with itself, and by the caption of Figure 6 panel g shows the summed difference, while the posterior covariance during the iterations is panel h. Panel h (measured at 300 dpi) shows a smooth rise to a kink at iteration 137 (plus or minus about 3) and then a monotonic decline from 0.7424 to 0.7423; the vertical extent of the marker band stays 13 to 17 px over the whole curve, so no oscillation is resolvable at print resolution (1 px corresponds to 2 × 10^-5). Panel g shows the same kink. A natural reading is a comparison of the SD run with the QN run (Figure 6H against Figure 5H); is that what is meant? The grade is moderate because a described behaviour of the method cannot be checked in the cited figure. |
| Suggestion | In l. 317 replace "(Figure 6G versus Figure 6G)" by the intended pair, for example "(Figure 6H; compare Figure 5H)"; give the iteration of the kink as read from the output (about 137), and either show the oscillation in an inset with a narrower y range or delete the statement in l. 316 to 317. |
| Status | verified (self-reference, panel content and curve shape on page images 11 and 27); assumption (intended target, posed as question) |
| Severity | moderate |
| Source | S4, AB, SD |

**GB-28 The three geological maps of scenario 1 and the area measure between them carry changing names, and "Steck et al. 2015" names both the source of the base map and the most different alternative map**

| Field | Content |
|---|---|
| Check | P38 |
| Location | p. 11, l. 330 to 336 and l. 338 to 339; p. 12, l. 347 to 348; Figure 4, credit line (p. 25); Figure 7, map titles, labels, x-axis and colour bar (p. 28); Figure 8, panel titles and caption (p. 29) |
| Quotation | "quantified by area mismatch"; "1) using the same geological map in the forward and inverse method, 2) using a geological map with minimal difference from the one used to generate the detrital data, 3) the map proposed by (Steck et al., 2015) with the biggest area mismatch"; "a simplified geological map with minimal changes from the truth"; "Originial geology (same as forward)" |
| Concern | Section 4.1.3 sets up scenario 1 with three cases, but the names vary. Case 1 is "the same geological map" (l. 332), "the original geological map" (l. 331, l. 339), "Originial geology (same as forward)" (with a misspelling) and "Forward geology" (Figure 7); case 2 is "a geological map with minimal difference" (l. 333), "a simplified geological map with minimal changes" (l. 338 to 339), "Geology with minimal changes" and "Minimal changes" (Figure 7); case 3 is "the map proposed by (Steck et al., 2015)" (l. 333 to 334) and "Geology by Steck et al. 2015" (Figure 7). The measure between maps is "area mismatch" (l. 330, l. 334, l. 335), "area difference (m2 )" (Figure 7 caption, x-axis "Area difference") and "Geology misalignment (m²)" (Figure 7 colour bar). The base map of Figure 4 uses, by its credit line, "data from Steck et al., 2015" and is case 1; case 3 is also named after Steck et al. (2015). A reader cannot tell what distinguishes the two maps that carry the same source name, nor whether "simplified" (l. 338) and "minimal difference" (l. 333) describe the same operation, so the source of the map difference in scenario 1 cannot be reconstructed. The same pattern occurs in scenario 2: "1) highly blended, 2) intermediate, and 3) the original synthetic fingerprints" (l. 348), "Almost fully blended", "Medium blended", "Unblended" (Figure 8 titles), "the most blended", "the half-way in between" (Figure 8 caption). Question to the authors: is the case 3 map the published map of Steck et al. (2015) without the personal communication and outcrop corrections that went into the Figure 4 map? |
| Suggestion | Name the three maps once in l. 332 to 334 with short labels (for example "reference map", "modified map", "Steck et al. (2015) map", with the narrative citation "proposed by Steck et al. (2015)" instead of "proposed by (Steck et al., 2015)"), say what was changed in the modified map and how the reference map differs from the published map, use one term for the area measure with its definition, and carry these labels into Figure 7 (which also corrects "Originial"); do the same for the three fingerprint sets of Figure 8. |
| Status | verified (name forms on page images 11, 12, 25, 28, 29); assumption (relation between the case 1 and case 3 maps, posed as question) |
| Severity | moderate |
| Source | S2, AB, ZF |

**GB-29 How the synthetic test sets were built, and how many source samples and zircon grains enter the natural fingerprints, is not stated**

| Field | Content |
|---|---|
| Check | P8, P34 |
| Location | p. 12, l. 343 to 344 and l. 355 to 357; p. 10, l. 288 to 289; Figure 5k (p. 26); p. 13, l. 391 to 392; p. 14, l. 423 to 424 |
| Quotation | "We perform a Principal Component Analysis (PCA) to retain the subset of tracers that explain the maximum variance in the mineralogical fingerprints."; "we progressively homogenize the source fingerprints by approaching each lithology’s mineral concentration to its mean across all lithologies" |
| Concern | Not described: how the 21 synthetic fingerprints of Figure 5k were generated; how individual tracers are ranked from principal components (a PCA yields components, not tracers); the blending coefficients of the 20 levels (l. 343 to 349). For the natural data, the number of source samples per unit (l. 391 to 392) and the number of zircon grains per sample (l. 423 to 424) are not given. The grid size is treated in GB-24, the construction of the modified map in GB-28, the number of detrital samples behind Figure 13 in GB-39. |
| Suggestion | Add to Section 4.1 the construction of the synthetic fingerprints, the blending levels and the PCA ranking rule; add to Section 4.2 a table of source samples per unit and the number of zircon grains per sample. |
| Status | verified (absence) |
| Severity | moderate |
| Source | SD |

**GB-30 Figure 8 shows 14 of the 20 tested blending levels while the caption accounts for one, and the error threshold in the text does not separate the plotted values**

| Field | Content |
|---|---|
| Check | P3, P23, P9, P36, P34 |
| Location | p. 12, l. 348 to 354; Figure 8, left and middle scatterplots and caption (p. 29) |
| Quotation | "In total, 20 values between the highly blended and the original synthetic fingerprints are tested"; "In many of these cases, the inversion fails to converge to a stable posterior solution."; "Note that the most blended example did not have a stable solution and is therefore not plotted." |
| Concern | Counted on the page image (connected components, 300 dpi): 14 markers in the left and 14 in the middle scatterplot, at JS 0.249, 0.272, 0.338, 0.359, 0.441, 0.461, 0.481, 0.501, 0.521, 0.541, 0.561, 0.581, 0.602, 0.624. Balance: 20 tested minus 14 plotted = 6 missing (30 %); the caption explains one (the most blended set, JS 0.225), five remain unexplained. Given the regular spacing of about 0.02, the missing sets lie in the gaps 0.29 to 0.31 and 0.38 to 0.42, among the poorly separated sets the text discusses. "In many of these cases" (l. 353) is not backed by a count, no convergence criterion is defined, and the thresholds of 0.55 and 0.44 come from converged runs only, a selection by outcome. Values of the left panel (unlabelled axis up to 700000): 46600, 677000, 5600 and 322200 for JS below 0.44, and 8400, 3500 and 18800 at JS 0.501, 0.521 and 0.541. Every plotted value from JS 0.501 downward exceeds 700, so "errors exceeding 700 mm/yr for JS" below 0.44 (l. 352 to 353) does not separate these runs from the rest; read as 700000, no point exceeds it (maximum 677000 plus or minus 1400). The middle panel supports the 0.55 threshold for the uncertainty (0.842 at JS 0.541, 0.747 at 0.561). |
| Suggestion | In l. 353 and in the caption of Figure 8 give the number of non-converged runs out of 20 and their JS values, mark them in the scatterplots (for example as crosses on the x-axis), define the convergence criterion, report the failure rate as a result, and state in l. 352 to 353 a threshold that separates the plotted values, with the unit of the summed error (see GB-24). |
| Status | verified (marker counts and values measured); inferred (balance and position of the missing runs, from the regular spacing) |
| Severity | moderate |
| Source | S3, AB, SD |

**GB-31 The drop in data misfit with fewer tracers is reported as an absolute sum, although the data misfit sums over the number of tracers**

| Field | Content |
|---|---|
| Check | P21 |
| Location | p. 12, l. 360 to 362; p. 6, l. 182 to 186 (eq. 7 and eq. 8); Figure 9, right scatterplot (p. 30) |
| Quotation | "when the number of tracers drops below 7, the absolute error increases rapidly, as does the posterior uncertainty, while the data misfit and model misfit drop" |
| Concern | By eq. 7 and eq. 8 (C_d = σd² I), the data misfit is a sum over the m tracers, so it falls with m even at unchanged fit quality. Read from Figure 9 (right): about 3.3 × 10^6 for 21 tracers and about 0.12 × 10^6 for one tracer. Per tracer: 3.3 × 10^6 / 21 = 1.57 × 10^5 and 0.12 × 10^6 / 1 = 1.2 × 10^5 (Python). After normalisation the drop shrinks from a factor of about 27 to a factor of about 1.3; most of the reported drop follows from the number of terms. In addition, fewer data make the underdetermined problem easier to fit. The text presents the drop without this explanation. |
| Suggestion | In l. 361 to 362 report the data misfit per tracer (or as reduced chi-square) when comparing different tracer counts, and state that the absolute sum falls with m. |
| Status | verified (equations and wording); inferred (values read from the figure, normalisation calculated) |
| Severity | moderate |
| Source | S3 |

**GB-32 The ranking of the three degradation factors depends on the ranges chosen for each scenario; over the tested ranges, removing tracers raises the error more than the largest map mismatch, and error is not monotonic in map mismatch**

| Field | Content |
|---|---|
| Check | P3, P21, P9, P10 |
| Location | p. 12, l. 363 to 365; p. 11, l. 337 to 338; p. 15, l. 456 to 461; Figure 7, left and middle scatterplots (p. 28); Figure 9, left and middle scatterplots (p. 30) |
| Quotation | "To summarize, among the three tested scenarios, the strongest impact on the posterior solution arises from reduced fingerprint distinctiveness. Geological map uncertainty follows as the second most influential factor."; "We observe that the greater the mismatch between the geological map used in the inversion and the one used to generate the synthetic data, the larger the discrepancy between the posterior and true erosion rate maps." |
| Concern | The text itself flags the minimal-change case as surprising (l. 338 to 339). Measured at 300 dpi: scenario 1 gives summed errors of about 198 (same map), 193.5 (minimal changes, 0.69 × 10^7 m²) and 274.8 (Steck et al. 2015, 1.14 × 10^7 m²), and posterior uncertainty of 0.7402, 0.7376 and 0.7460; neither quantity is monotonic in the mismatch, so the general sentence in l. 337 to 338 holds only for the largest mismatch. Scenario 3 reaches 347.3 and 348.3 (1 and 2 tracers) and an uncertainty of 0.962, against 197.6 with 7 or more tracers. Increase over the unperturbed case: map mismatch plus 39 % (274.8 against 198), tracer reduction plus 76 % (347.3 against 197.6); uncertainty plus 0.006 against plus 0.22 (Python; 150 dpi readings agree within 1). Over the tested ranges, tracer reduction therefore has the larger effect; the ranking in l. 363 to 365 holds only under the proviso "provided that the most informative ones are retained" read as at least 7 tracers, while map mismatch is judged over its full range. The three scenarios have no common scale (m², JS distance, count), scenario 1 has only two perturbed maps against 20 and 21 levels, and the "minimal changes" map differs by 61 % of the Steck mismatch (0.69 / 1.14), so "minimal" is not small. The Discussion builds on this ranking (l. 456 to 461). |
| Suggestion | Put the scenarios on a common scale (for example the resulting change in average JS distance, or realistic ranges stated in advance), test several random map perturbations at controlled area mismatch, and state the ranking in l. 363 to 365 with the ranges for which it holds (for example "with at least 7 tracers") and with the error and uncertainty increases per scenario as numbers; replace l. 337 to 338 by a statement for the three cases with their values. |
| Status | verified (values measured on page images 28 and 30; wording); inferred (dependence of the ranking on the ranges, percentages calculated) |
| Severity | moderate |
| Source | S3, AB, SD |

**GB-33 The hyperparameter sweep of Figure 10 does not support the values used in all tests: the error falls up to the largest smoothing distance tested, the over-smoothing beyond 3000 m is not shown, and the marked values differ from those used**

| Field | Content |
|---|---|
| Check | P3, P11, P2, P5, P10, P29 |
| Location | p. 12, l. 372 to p. 13, l. 376; Figure 10, all rows and caption (p. 31); p. 10, l. 294 to 295; p. 11, l. 324 to 326; p. 14, l. 426 to 428; p. 3, l. 70; p. 12, l. 367 to 371 |
| Quotation | "However, beyond approximately 10 times the pixel size (3000 m), the solution becomes overly smooth, causing the posterior to deviate from the true erosion rates."; "Through forward-inverse testing, we optimize the hyper-parameters"; "L = 3000 m" |
| Concern | Measured at 300 dpi: the 20 markers of the first row lie at L = 206 to 3000 m; the summed difference falls monotonically from 256.8 to 76.6 at 3000 m, and the normalised uncertainty from 0.98 to 0.27. No run beyond 3000 m is plotted, so the over-smoothing stated in l. 373 to 374 is not shown. Interpolated at L = 1200 m, the value used in all tests (l. 294, l. 325, l. 427): 197.6 and 0.741; the setting used thus has a summed error 158 % above the best tested value ((197.6 - 76.6) / 76.6, Python). Part of this decrease reflects the prior taken from the truth (GB-23). The third column marks L = 3000 m, σm = 6.2, σd = 0.003 mm/y, µ = 0.1 and n_m = 25; two of five agree with the test settings (µ = 0.1, 25 iterations, l. 324 and l. 326), three do not (1200 m, σm = 3, σd = 0.01 mm/y). Neither text nor caption says what the marked values are (optimum, recommendation or default), at which values the other parameters were held in each sweep (l. 367 to 371), why the sweep (Section 4.1.4) follows tests that already use fixed values, or how hyperparameters are chosen for natural data without a truth. The figure is set in about 3.6 pt (digit height at 600 dpi), below 6 pt. The grade is major because the manuscript states that the tests optimise the hyperparameters (l. 70), and the smoothing distance enters every result in Sections 4.1.3 and 4.2. |
| Suggestion | In Section 4.1.4 or the caption of Figure 10 state the fixed values of each sweep and the meaning of the marked values; justify L = 1200 m against Figure 10 or rerun the tests with the selected value; extend the sweep beyond 3000 m or delete the statement in l. 373 to 374; describe a truth-free selection rule for natural data (for example L-curve or discrepancy principle); enlarge Figure 10 to at least 6 pt, for example by splitting it. |
| Status | verified (axis ranges, marks and font size measured on page image 31; wording) |
| Severity | major |
| Source | S3, AB, SD |

**GB-34 The text describes a strong and non-monotonic effect of the data standard deviation that Figure 10 does not show; the plotted changes are about 0.01 % and 0.06 %**

| Field | Content |
|---|---|
| Check | P3, P21 |
| Location | p. 13, l. 380 to 384; Figure 10, third row (p. 31) |
| Quotation | "Very low data standard deviation values lead to large differences between the posterior and true erosion rate maps, likely due to overfitting or unstable gradients. As data standard deviation increases, the absolute difference first decreases to a minimum, then rises to a plateau at higher values."; "with increasing data standard deviation, model misfit remains high while data misfit decreases sharply" |
| Concern | The first panel of the third row carries the axis offset "+1.974e2". Measured at 600 dpi, the summed difference rises monotonically from 197.4198 at the smallest σd to 197.4432 at σd = 0.89 mm/y: there is no high value at low σd, no minimum and no plateau, and the whole range is 0.0234 on 197.42, a relative change of 1.2 × 10^-4 (Python). The normalised uncertainty spans 0.74015 to 0.74040 (3.4 × 10^-4), the model misfit 1.5614 to 1.5623 (5.8 × 10^-4), which l. 383 to 384 describe as high and then decreasing rapidly. Compared with the first row (about 257 to 77) and the fourth row (about 329 to 197), the inversion is practically insensitive to σd over the tested range. The linear x-axis (0 to 0.9 mm/y) does not resolve the value "10-2 mm/y" named in l. 384. |
| Suggestion | Rewrite l. 380 to 384 to the plotted behaviour and give the size of the changes relative to the baseline, or show the range in which σd matters; use a logarithmic x-axis for σd in Figure 10 and avoid the axis offset or state it in the caption. |
| Status | verified (axis offset, tick labels and values measured on page image 31); inferred (relative changes calculated) |
| Severity | moderate |
| Source | S3, AB |

**GB-35 It is not stated whether the convergence threshold of 10^-5 refers to an absolute or a relative change in data misfit**

| Field | Content |
|---|---|
| Check | P20 |
| Location | p. 13, l. 388 to 389; Figure 10, fifth row, third panel (p. 31) |
| Quotation | "Beyond 115 iterations, the change in data misfit between successive steps falls below 10" |
| Concern | The data misfit in this sweep is of the order of 10^7 (axis multiplier "1e7" on page image 31). If 10^-5 is absolute, it corresponds to a relative change of 10^-5 / 10^7 = 10^-12; if relative, the absolute change is about 10^2 (Python). The reader cannot tell which applies. |
| Suggestion | In l. 388 state whether the threshold is absolute or relative to the current misfit. |
| Status | verified (wording, axis label); inferred (relative value calculated) |
| Severity | minor |
| Source | S3 |

**GB-36 Figure 11 gives identical fingerprints for several mineral pairs and triples, so the 21 tracers are not 21 independent mineral signals**

| Field | Content |
|---|---|
| Check | P3 |
| Location | p. 13, l. 393 to 398; p. 9, l. 259 to 260; Figure 11, rows Annite, Muscovite, Phlogopite; Anorthite, Pyroxene; Ankerite, Dolomite; Albite, Paragonite (p. 32); Figures 15 and 16, fingerprint bars (p. 36, 37) |
| Quotation | "Sixth, to mitigate peak overlap, we average the total peak area within the 2θ windows corresponding to each mineral, rather than relying on individual peaks." |
| Concern | Bar lengths measured on the row centres of all 21 minerals in the seven columns (maximum bar 243 to 245 px = 1.0): Annite and Phlogopite 0, 132, 76, 138, 52, 162, 132 px in every column; Muscovite identical except column 5 (43 instead of 52 px); Anorthite and Pyroxene 0, 35, 245, 93, 243, 7, 104 px, identical in all columns; Ankerite and Dolomite differ by at most 2 px (0.008), Albite and Paragonite by at most 7 px (0.03). Figure 15 repeats this: the stacked bars of Anorthite and Pyroxene, and of Annite and Phlogopite, have identical shares in all units. Identical values across seven different lithologies indicate shared 2θ windows or peaks rather than separate minerals. Counting groups with differences of at most 2 px as one, Figure 11 carries 16 or 17 distinct tracers, not 21. This affects the mineralogical reading of the fingerprints (l. 399 to 401) and the tracer count compared with scenario 3. The grade is major because the validity of the XRD fingerprints as mineral abundances is the first aim of the natural data tests (l. 282 to 283). |
| Suggestion | In Section 3.4 list the 2θ windows per mineral and state which minerals share windows; in Figure 11 and in l. 393 to 398 either merge the identical tracers into named groups or explain why they coincide; report the number of independent tracers. |
| Status | verified (identity of the bar lengths, measured); inferred (shared windows as the cause) |
| Severity | major |
| Source | AB |

**GB-37 The tracer list in the text names "Chrysolite", while all figures and the study area description name "Chrysotile"; the two are different minerals**

| Field | Content |
|---|---|
| Check | P38, P2 |
| Location | p. 13, l. 395; p. 10, l. 274; p. 9, l. 257; Figure 11, row labels (p. 32); Figure 15 and Figure 16, x-axis of the fingerprint panel (p. 36, 37) |
| Quotation | "Dolomite, Diopside, Chrysolite, Antigorite, Anorthite"; "serpentinites (predominantly antigorite and chrysotile)" |
| Concern | The list of 21 minerals in l. 393 to 396 and the row labels of Figure 11 agree in 20 of 21 names; the only difference is "Chrysolite" in the text against "Chrysotile" in the figures (Python set difference). The text list follows the order of the x-axis of Figure 15, with "Chrysolite" in the slot where the figure has "Chrysotile", so the same tracer carries two names. Chrysolite is a yellowish green form of olivine, chrysotile a serpentine mineral, Mg3Si2O5(OH)4 (minerals.net). The 2θ windows are selected per mineral from RRUFF reference spectra (l. 257), so a reader who rebuilds the windows from the text list would take an olivine reference instead of a serpentine one. The study area text (l. 274) and the serpentinite fingerprint of Figure 11 point to chrysotile as the intended mineral. |
| Suggestion | Replace "Chrysolite" by "Chrysotile" in l. 395, and state in Section 3.4 or a supplement which RRUFF reference spectrum and which 2θ window was used for each of the 21 tracers. |
| Status | verified (both spellings on page images 13, 32, 36, 37; mineral identities in the cited source) |
| Severity | moderate |
| Source | S2, S3, AB, SD |

**GB-38 Natural test 1 is answered by a qualitative statement without criterion, while the minerals that define the garnet-bearing, eclogitic and calcareous units are low or absent in Figure 11**

| Field | Content |
|---|---|
| Check | P3, P31, P10 |
| Location | p. 13, l. 399 to 401; p. 10, l. 274 to 279 and l. 282 to 283; p. 13, l. 393 to 396; Figure 11, rows Almandine, Omphacite, Microcline, Tremolite, Fayalite (p. 32) |
| Quotation | "The mineralogical fingerprints derived from processed and binned XRD data align well with established knowledge of the lithology in the Gorner Glacier catchment (Bearth, 1953; Steck et al., 2015), supporting the 1) the robustness of the cleaning and binning approach, and 2) the validity of the input data for the inversion method." |
| Concern | The robustness of the processing chain is inferred from an unstated visual match. There is no table of expected against measured minerals, no pass criterion, no number of source samples per unit, no within-unit spread, no replicate measurement, and no check of the binned quantification against prepared mixtures. Points that a criterion would have to address, from the manuscript: the units are described with "garnet-mica schists" (l. 276 to 277), "eclogites" (l. 274) and "coarse-grained granites" (l. 276). Measured normalised values in Figure 11 (bar length / 244 px): Almandine 0.01, 0.03, 0.09, 0.04, 0.10, 0.04, 0.04 in the seven columns, that is at most 0.04 in Monte Rosa (gneiss, micaschist) and 0.09 in Stockhorn-Tuftgrat-Gornergrat; Omphacite 0.05 in the ZSF metabasites and eclogites; Microcline 0.29 but Tremolite 0.89 in Monte Rosa granite; Fayalite 0.62 in ZSF serpentinites. The units are also described with "calcareous mica schists" and "marbles" (l. 275, l. 278), but calcite is not among the 21 minerals (l. 394 to 396), while the list contains the group name "Pyroxene" next to diopside and omphacite. Is the low garnet and omphacite signal a property of the normalisation by the maximum peak area (l. 261; GB-18), of the window choice (GB-36), or of the samples? The grade is major because test 1 is the first aim of the natural data tests and the validity of all natural inputs is derived from it. |
| Suggestion | Add to Section 4.2 a table of expected major minerals per unit (from Bearth, 1953, and Steck et al., 2015) against the measured binned values, with a stated criterion, and discuss the units where they differ; report the number of source samples per unit and the spread; validate the binning on mixtures of known proportions; justify the mineral list (calcite, group names); rephrase l. 399 to 401 to what this shows, and delete the doubled article in "supporting the 1) the robustness". |
| Status | verified (measured values; absence of criterion and validation; calcite absence); inferred (mismatch with the expected composition, from the manuscript's own unit descriptions); assumption (cause of the low signals, posed as question) |
| Severity | major |
| Source | AB, SD, S3 |

**GB-39 The natural known-mixture test cannot separate discrimination from low resolution: units inside the subcatchment also peak at zero, the unit with the highest predicted rate covers a small part of the subcatchment, and the number of samples is not given**

| Field | Content |
|---|---|
| Check | P3, P10, P9, P20, P27, P29, P32 |
| Location | p. 14, l. 410 to 418; p. 13, l. 403 to 406; p. 10, l. 283 to 284 and l. 299 to 300; p. 9, l. 270 to 272; Figure 12 (p. 33); Figure 13, KDE panels, inset and caption (p. 34) |
| Quotation | "Merging the inversion results from multiple detrital samples collected at the sink of this sub-catchment shows that the predicted erosion rates for pixels within the Zermatt - Saas Fee unit (ZSF sediments) are close to zero (Figure 13)."; "the overall pattern confirms that the inversion respects geological boundaries when the XRD fingerprints provide sufficiently distinct signals."; "a taller peak indicates greater consistency across inversions." |
| Concern | Using a subcatchment as a natural analogue of a known mixture is a sound idea, and the prediction is stated before the result (l. 410 to 411). The design has these limits. (1) Only one of seven units (14.3 %) is expected to be absent (l. 411), and it is one of the "Small lithological units" with "lower resolution" (l. 299 to 300); a posterior near zero may then reflect low resolution and the prior rather than discrimination, and the natural prior is not stated (GB-11). (2) Measured KDE modes (x-axis 0.0 to 3.0 mm/y, plus or minus 0.002): ZSF sediments 0.007, Furgg series 0.007, Monte Rosa granite 0.020, ZSF serpentinites 0.034, ZSF metabasites 0.234, Monte Rosa gneiss and micaschist 0.603, Stockhorn-Tuftgrat-Gornergrat 0.772 (nearly flat); a mode near zero is not specific to the unit without outcrops. (3) Composition of the dashed Gorner-Grenz catchment in the inset (colours by chromaticity, convex hull of the dashes): Monte Rosa granite 0.69, Stockhorn-Tuftgrat-Gornergrat 0.16, Furgg 0.08, Monte Rosa gneiss 0.03, ZSF serpentinites 0.03, ZSF metabasites 0.00; the unit with the highest predicted rate covers about 3 % of the subcatchment, the unit covering about 69 % peaks at 0.02 mm/y, and ZSF metabasites, counted in l. 411 among the units with outcrops, does not appear inside the dashed line (small outcrops below the map scale may explain part of this). (4) The KDEs pool "all pixels within each lithological unit" over the whole catchment (caption), so whether erosion is assigned to pixels outside the subcatchment is not reported. (5) Absence is judged from outcrops (l. 411), while lithology under ice is inferred (l. 270 to 272). (6) The number and dates of the "multiple detrital samples" and inversions are given neither in the text nor in the caption; the upper panel has the axis title "Density" but no tick values, so peak heights (9 to 435 px) cannot be compared on a scale and the reading rule of the caption cannot be applied across units. "Some spillover" (l. 414 to 415) is not quantified. The grade is major because the test answers natural aim 2 (l. 283 to 284). |
| Suggestion | Counter-design for Section 4.2.1: (i) a laboratory known-mixture experiment with the authors' own source powders in predefined proportions, processed through the same XRD chain, the test the manuscript names as standard (l. 404 to 406); (ii) report per unit the area share inside the subcatchment and the median predicted rate, and the share of posterior erosion flux assigned to pixels outside against inside the subcatchment, with A built for the full catchment and for the subcatchment only; (iii) a sampling point whose catchment excludes several units, giving more than one negative control. Give the number, dates and individual results of the detrital samples, add a density scale to Figure 13 or state that ridges are scaled individually, draw the outcrops inside the subcatchment, and state the inferred lithology under ice there. |
| Status | verified (KDE modes measured; absence of sample numbers and scale; wording); inferred (area shares, from map colours with a convex hull; the conclusion that the test cannot separate discrimination from resolution) |
| Severity | major |
| Source | S3, AB, SD |

**GB-40 The detrital sample of the zircon comparison is called "the same detrital sample" and also "a detrital sample taken at the same date and time"; whether XRD and zircon data come from one sample is unclear**

| Field | Content |
|---|---|
| Check | P38, P2 |
| Location | p. 14, l. 420 to 421, l. 423 to 424 and l. 437 to 438 |
| Quotation | "we compare it against a zircon-based fingerprinting approach applied to the same detrital sample"; "the detrital sample collected on June 28, 2019, at 13:30"; "the XRD-derived dataset acquired from a detrital sample taken at the same date and time" |
| Concern | The manuscript fixes the sample by date and time. l. 420 to 421 speak of "the same detrital sample", l. 437 to 438 of "a detrital sample taken at the same date and time", which reads as a second sample. The sampling site (main outlet or the Gorner-Grenz confluence of Section 4.2.1) is not named. For the comparison and for concatenating both data vectors (l. 443 to 444), a split of one sample and two parallel samples are different designs. Question to the authors: are the XRD and zircon data from aliquots of one sample, and where was it taken? |
| Suggestion | In l. 423 to 424 and l. 437 to 438 give the sample one identifier, state whether XRD and zircon data come from aliquots of the same sample, and name the sampling site. |
| Status | verified (both descriptions on page image 14); assumption (whether they denote one or two samples, posed as question) |
| Severity | minor |
| Source | S2, S3 |

**GB-41 The zircon tracer matrix is incomplete: the treatment of the ZSF metabasites and eclogites is not stated, and Figures 14 and 16 show the imputed Monte Rosa gneiss fingerprint as if it were measured**

| Field | Content |
|---|---|
| Check | P23, P37 |
| Location | p. 14, l. 430 to 434; Figure 14, source fingerprints and caption (p. 35); Figure 16, age-bin bars and caption (p. 37); Figure 11, caption (p. 32) |
| Quotation | "zircon data were not available for two lithological units: no zircon grains were recovered from the Zermatt-Saas Fee (ZSF) ophiolites (metabasites and eclogites), and no age data were available for the Monte Rosa garnet-gneiss (MR g-g) unit"; "To compensate for the lack of age data for the MR g-g unit, we assigned the MR g-g unit the same zircon-age fingerprint as the Monte Rosa granite unit." |
| Concern | The gaps are disclosed in the text. Balance: 7 units (Figure 11 caption) minus 2 without zircon data = 5 with own fingerprints, plus 1 substituted (MR g-g) = 6; one unit, the ZSF metabasites and eclogites, has no stated treatment. In Figures 14 and 16 the ZSF metabasites have no segment in any of the 13 age bins, which fits a zero column in A, with pixels that then do not affect the zircon data and stay at the prior; whether the unit was instead removed or merged is not stated. The same applies to the zircon rows of the concatenated matrix (l. 443 to 445). In Figure 14 the MR granite and MR gneiss segments have equal heights in all 11 bins where they occur (pixel heights 113/114, 107/107, 113/114, 112/113, 104/105, 32/32, 18/19, 13/13, 13/13, 93/94, 48/49); the captions of Figures 14 and 16 say only "the source fingerprints" and do not note the substitution. The "low resolution" of the zircon run (l. 436) may partly be an effect of this design. |
| Suggestion | In l. 430 to 434 state how the ZSF metabasites and eclogites were represented in the zircon and in the combined tracer matrix and discuss the effect on resolution and uncertainty; add to the captions of Figures 14 and 16 that the MR g-g zircon fingerprint is copied from MR granite, and mark the imputed segments (for example by hatching). |
| Status | verified (text; segment heights measured on page image 35); inferred (balance; zero column as the likely treatment) |
| Severity | moderate |
| Source | S3, SD |

**GB-42 The combined zircon and XRD inversion has a higher normalised posterior uncertainty than the XRD-only inversion, while the Discussion and Introduction say that combining the data further stabilises and improves the solution**

| Field | Content |
|---|---|
| Check | P2, P15, P11, P9, P31, P6 |
| Location | p. 14, l. 435 to 436; p. 15, l. 441 to 449; p. 15, l. 461 to 463; p. 3, l. 72 to 73 (repeated p. 5, l. 139 to 140); p. 10, l. 284 to 285; Figures 14, 15 and 16, label "Total normalised posterior uncertainty" (p. 35 to 37) |
| Quotation | "Adding XRD data to the zircon dataset stabilizes the inversion and improves the posterior solution. The normalized posterior uncertainty decreases slightly to 0.86 (from 0.87 in the zircon-only case)"; "Furthermore, combining XRD data with other fingerprint data such as zircon data, proves to further stabilize and improve the posterior solution, as shown with natural data for the Gorner gletscher catchment."; "showing that integrating XRD with zircon data improves the stability and sharpness of the posterior solution" |
| Concern | The three cases are reported with the same metric, and text and figure labels agree (0.87, 0.82, 0.86). Computed: zircon to XRD only minus 0.05 (minus 5.7 %); zircon to combined minus 0.01 (minus 1.1 %); XRD only to combined plus 0.04 (plus 4.9 %) (Python). Section 4.2.2 compares the combined case only with the zircon case (l. 447); the Discussion turns this into an improvement "further" than XRD alone and uses "proves" for one sample (l. 461 to 463). By the manuscript's own metric, adding zircon to XRD worsens the posterior uncertainty. The colour scale of the combined map extends to 12.2 mm/y against 8.4 mm/y for XRD only (Figures 15 and 16), and the hatched low-confidence area is larger in Figure 16. The other quantities are not reported for all cases: average JS distance 0.48 (zircon) and 0.57 (combined) but none for XRD only, although that value decides whether XRD alone lies above the synthetic threshold of 0.55 (l. 352); maximum erosion rate only for zircon ("(>8000 mm/y)", l. 435); resolution only as "low" for zircon; "stability", "sharpness" (l. 73) and "accuracy" (l. 285) are not defined, and accuracy cannot be measured for natural data without a reference. The comparison is also confounded: the zircon matrix lacks one unit and duplicates another (GB-41), and the same σd = 0.01 mm/y is used for both data types (l. 427 to 428, l. 444 to 445), so the metrics reflect A and the assumed variance rather than measured uncertainties; the differences (0.05) are small next to the change of the same metric across the smoothing sweep (0.98 to 0.27, Figure 10) and carry no uncertainty. Question to the authors: does the increase from 0.82 to 0.86 come from a different linearisation point, a different normalisation (tr(C_m) of the concatenated problem) or different parameters? The grade is major because natural aim 3 (l. 284 to 285) rests on this comparison; with the finding, the manuscript can show only that XRD improves a zircon-only inversion, not that zircon improves an XRD inversion. |
| Suggestion | In Section 4.2.2 add a table with the same quantities for all three cases (normalised uncertainty, average JS distance, maximum and median posterior erosion rate, mean resolution diagonal, number of tracers), state the comparison with each single data set, and explain why the combined value (0.86) exceeds the XRD-only value (0.82); define stability (for example the spread of the posterior across samples or hyperparameter settings); compare the methods on the units with complete fingerprints and with measured data variances per data type; remove "accuracy" from l. 285; in l. 461 to 463 restrict the statement to what Section 4.2.2 shows, replace "proves" by "suggests", add the commas around "such as zircon data", delete the comma before "proves", and write "Gornergletscher"; adjust l. 72 to 73 and l. 139 to 140 accordingly. |
| Status | verified (values and wording in text and figure labels; colour bar maxima measured); inferred (differences calculated; confounding); assumption (possible causes, posed as question) |
| Severity | major |
| Source | S3, S4, SD, S2 |

**GB-43 Figures 5 and 6 lack units and axis titles, Figure 6 has an unlabelled legend symbol, and the abbreviations and tracer letters of Figure 5 are not resolved**

| Field | Content |
|---|---|
| Check | P29 |
| Location | Figure 5a to 5k (p. 26); Figure 6a to 6i (p. 27); captions p. 26, 27 |
| Quotation | "(a) "true" erosion map, (b) posterior erosion map, (c) difference between "true" and posterior erosion map" |
| Concern | No colour bar in panels a, b, c and e of Figures 5 and 6 carries a unit (Figures 14 to 16 give "(mm/y)"). Panels g and h have no y-axis title; in Figure 6 panels g, h and i have no x-axis title and panel i has no colour bar title. Figure 6 shows the hatched legend symbol without the label "Low-confidence areas" that Figure 5 carries, and neither caption nor text defines when an area counts as low-confidence. The legend in 5j uses ZSF, MR and "S.,T.,G.", introduced in the text only at l. 414 and l. 432, and the tracers in 5k are labelled A to U without explanation. |
| Suggestion | Add units and axis titles to Figures 5 and 6, label the hatched symbol in Figure 6 and define low-confidence areas in Section 3.3 or the captions, resolve ZSF, MR and S.,T.,G. in the caption of Figure 5, and say that A to U are the 21 synthetic tracers. |
| Status | verified |
| Severity | minor |
| Source | AB |

**GB-44 The legend fields in Figures 5, 15 and 16 do not match the colours of the bars and maps, so the Stockhorn-Tuftgrat-Gornergrat bars match the legend field of Monte Rosa gneiss; in Figures 4 and 12 three red legend fields are hardly distinguishable**

| Field | Content |
|---|---|
| Check | P3 |
| Location | Figure 5j, 5k (p. 26); Figures 15 and 16, legend and fingerprint bars (p. 36, 37); Figures 4 and 12, legends (p. 25, 33) |
| Quotation | "S.,T.,G." and "MR gneiss, mica" |
| Concern | The legend fields (Figure 15, same in Figures 5 and 16) are saturated: S.,T.,G. #ff5001, MR gneiss #ff7f41, ZSF metabasites #32a02d; the bars use lighter colours: S.,T.,G. #ff844c, MR gneiss #ffa579, metabasites #6fbc6b (differences 60 to 151, above the limit of 40). The S.,T.,G. bars (#ff844c) differ from the MR gneiss legend field (#ff7f41) by only 21 (Figure 5k: 19), so a reader matching colours assigns S.,T.,G. bars to MR gneiss. In Figures 4 and 12 the field "Stockhorn basement, Tuftgrat Mesozoic and GornergratPermo-Mesozoic" (#fc7434) and two outcrop fields (#fc3434, #fc5c34) differ pairwise by 64, 24 and 40. In Figure 15 the legend text "ZSF serpentinites" is cut by the next legend field, and in Figure 16 the top row of the legend is cropped. The grade is moderate because the source fingerprints, on which the natural data interpretation rests, are misread with the current legends. |
| Suggestion | Draw the legend fields with the same transparency as bars and maps in Figures 5, 15 and 16; choose distinguishable colours for the three red fields in Figures 4 and 12; fix the legend layout in Figures 15 and 16. |
| Status | verified (colours measured at 300 dpi) |
| Severity | moderate |
| Source | AB |

**GB-45 The x-axis of the two left scatterplots in Figure 9 is labelled with the JS distance although it shows the number of tracers**

| Field | Content |
|---|---|
| Check | P29 |
| Location | Figure 9, left and middle scatterplots, x-axis title (p. 30) |
| Quotation | "Avg. JS distance between lithologies" |
| Concern | The axis runs from 0.0 to 20.0, and the 21 markers lie at 1.0 to 21.0, matching "the full range between 1 and 21 tracers" in l. 358. The label was evidently taken over from Figure 8. |
| Suggestion | Relabel both x-axes "Number of tracer minerals". |
| Status | verified |
| Severity | minor |
| Source | AB |

**GB-46 Figure 12 does not draw the subcatchment boundary and does not explain why part of the map is faded**

| Field | Content |
|---|---|
| Check | P29 |
| Location | Figure 12, map, legend and caption (p. 33) |
| Quotation | "Lithology and outcrops in the Gorner-Grenz confluence subcatchment." |
| Concern | The subcatchment appears only as the saturated north-eastern part. Measured: Monte Rosa granite inside it #f4acac against the legend field #fcacac (difference 8); outside #fcdcdc (difference 48, matching no legend field). Legend and caption do not explain the fading, and the map has no boundary line, while Figure 13 draws a dashed one. The reader cannot check from Figure 12 which units drain to the sampling point, which is the basis of the known-mixture test (GB-39). |
| Suggestion | Draw the subcatchment boundary in Figure 12 (as in the inset of Figure 13) and state in the caption that units outside it are faded. |
| Status | verified |
| Severity | moderate |
| Source | AB |

**GB-47 Figure 14 has no legend for the colours of its geological map and its stacked fingerprint bars**

| Field | Content |
|---|---|
| Check | P29 |
| Location | Figure 14, panel "Geology" and fingerprint bars (p. 35) |
| Quotation | "the geological map and the source fingerprints." |
| Concern | Figures 15 and 16 carry a legend with eight entries; Figure 14 carries none, so the colours in the zircon bars (ZSF sediments, Monte Rosa granite and gneiss, S.,T.,G., Furgg; ZSF metabasites absent) can only be read via the later figures. |
| Suggestion | Add the legend of Figure 15 to Figure 14. |
| Status | verified |
| Severity | minor |
| Source | AB |

**GB-48 The resolution panels of Figures 14 to 16 show values near 1 over most of the map, which by Section 3.3 means well resolved, while the text calls the zircon result low in resolution and the normalised uncertainty stays high**

| Field | Content |
|---|---|
| Check | P3 |
| Location | Figures 14, 15 and 16, panels "Resolution diagonal" and "Normalised posterior uncertainty" (p. 35 to 37); p. 8, l. 234 to 238; p. 14, l. 435 to 436; Figures 5d and 6d (p. 26, 27) |
| Quotation | "Where the diagonal of R is close to 1, data have improved our knowledge considerately relative to the prior."; "low resolution, and a high total normalized uncertainty" |
| Concern | Colour bars measured at 300 dpi: on these bars, achromatic dark grey occurs only for values from 0.97 (Figure 14), 0.99 (Figure 15) and 0.965 (Figure 16) upward. Of the map pixels, 84.2 %, 82.5 % and 85.7 % are achromatic dark grey and only 2.1 %, 4.1 % and 0.4 % are coloured. Taken at face value, the diagonal of R is close to 1 almost everywhere, that is well resolved by l. 235 to 236, while the total normalised uncertainty is 0.87, 0.82 and 0.86 (values close to 1 mean little variance reduction, l. 237 to 238) and the zircon case is called "low resolution" in l. 436. Lower resolution values appear only in a few cells, where the normalised uncertainty is lowest (Figure 15, hotspot). Are the panels showing diag(R), 1 - diag(R), or another quantity? The grade is major because resolution and posterior covariance are the metrics the manuscript offers to assess reliability (l. 483 to 484). |
| Suggestion | State in Section 3.3 and in the captions which quantity the resolution panels show and its expected range; if diag(R) is plotted, explain why it is near 1 where the variance reduction is small, and revise l. 436. |
| Status | verified (colour shares measured); inferred (value range, since hillshade blending lowers chroma); assumption (the cause, posed as question) |
| Severity | major |
| Source | AB |

#### Minor corrections

| ID | Location | Quotation | Replacement | Source |
|---|---|---|---|---|
| KK-18 | p. 10, l. 299 | "(such as Zermatt Saas-Fee sediments and Furgg series (Figure 4) and Figure 5J)" | "(such as Zermatt Saas-Fee sediments and Furgg series; Figures 4 and 5J)", with the unit name as fixed in GB-20 | ZF |
| KK-19 | p. 11, l. 319 | "(Figure 6D, 6E and 6F )" | "(Figure 6D, 6E and 6F)" | S3 |
| KK-20 | p. 12, l. 340 | "Zermatt-Saas-Fee ophiolites" | "Zermatt-Saas Fee ophiolites", as in l. 431 | S2 |
| KK-21 | p. 13, l. 384 | "approximately 10-2 mm/y" | "approximately 10⁻² mm/y" | S3, SD |
| KK-22 | p. 14, l. 409, l. 411 and l. 413 | "sub-catchment" | "subcatchment", as in l. 283, l. 284, l. 411 and Figures 12 and 13 (l. 411 has both forms in one sentence) | S2 |
| KK-23 | p. 14, l. 424 | "described in (Belotti, 2021)"; "outlined in (De Doncker et al.," | "described by Belotti (2021)"; "outlined by De Doncker et al. (2020)" | ZF |
| KK-24 | Figure 6, caption (p. 27) | "Steepest-Descent (SD)" | "steepest descent (SD)", as in l. 210 | S2 |
| KK-25 | Figure 9, colour bar title (p. 30) | "Number of tracrs" | "Number of tracers" | AB |
| KK-26 | Figure 9, left scatterplot, below the y-axis title (p. 30) | "Σ" (second, isolated sign) | delete | AB |
| KK-27 | Figure 10, first row, x-axis of the second column and colour bar title (p. 31) | "Smooting distance (m)" | "Smoothing distance (m)" | AB |
| KK-28 | Figure 11, caption (p. 32) | "(metabasites, ecologites)" | "(metabasites, eclogites)" | S2, S3, AB, SD |
| KK-29 | Figure 13, inset label (p. 34) | "Gorner-Grenz catchment" | "Gorner-Grenz subcatchment", as in l. 411 and the Figure 13 caption | S2 |
| KK-30 | Figures 14, 15 and 16, legend (p. 35 to 37) | "Low-con dence area" | "Low-confidence area" (missing "fi" ligature, page images) | AB |
| KK-31 | Figure 14, caption and axis (p. 35); Figure 16, panel title (p. 37) | "using Zr fingerprint data"; "Normalised abundance per Zr age bin"; "combined XRD and Zr data" | "using zircon fingerprint data"; "Normalised abundance per zircon age bin"; "combined XRD and zircon data", as in the text | S2, AB |

#### Verification log

| ID | Check | Checked | Values | Result |
|---|---|---|---|---|
| PP-29 | P1 | Pixel size and smoothing distances | 1200 m / 4 = 300 m (l. 294, l. 325, l. 427); 10 × 300 m = 3000 m (l. 373) | no finding |
| PP-30 | P1 | Tracer counts | text list l. 394 to 396: 21 names; "21 target minerals" l. 397; Figure 11: 21; Figure 9 "All tracers (21)"; Figure 5k bars A to U: 21; scenario 3 range 1 to 21 (l. 358) | no finding (name difference in GB-37) |
| PP-31 | P1 | Differences of the natural-data metrics and their wording | 0.87 to 0.86: minus 0.01, "decreases slightly" (l. 447); 0.87 to 0.82: minus 0.05, "slightly lower" (l. 441 to 442); JS 0.48 to 0.57: plus 0.09 (plus 18.75 %), "increases" (l. 448) | no finding on direction; comparison XRD to combined in GB-42 |
| PP-32 | P2 | Uncertainty values in text against figure labels | 0.87 (l. 436, Figure 14), 0.82 (l. 442, Figure 15), 0.86 (l. 447, Figure 16) | no finding |
| PP-33 | P2 | Parameter sets across sections | L = 1200 m, σm = 3, σd = 0.01 mm/y in l. 294 to 295, l. 325, l. 427 to 428; iterations 100 (l. 293) and 25 (l. 324, l. 426); µ = 0.1 in l. 326 and l. 428 | no finding beyond GB-11, GB-26, GB-33 |
| PP-34 | P2 | Baseline of the synthetic tests in Figures 7, 9, 10 | summed error about 197 to 198 in Figure 7 (forward geology), Figure 9 (all tracers), Figure 10 rows 2 and 3; uncertainty about 0.740 in Figures 7, 9 and Figure 10 rows 3 to 5; data misfit about 3.3 × 10^6 in Figures 7 and 9 | no finding |
| PP-35 | P2 | Scenario 3 runs against Figure 9 | 21 counts tested (l. 358); 21 markers counted; examples 1, 11 and 21 tracers in l. 357 and Figure 9 | no finding |
| PP-36 | P2 | Scenario 2 examples against Figure 8 | text "highly blended, intermediate, original" (l. 348); Figure 8 JS 0.225, 0.441, 0.624; midpoint (0.225 + 0.624) / 2 = 0.4245, close to 0.441 ("half-way", caption) | no finding (run count in GB-30) |
| PP-37 | P11 | Announced tests against reported results | synthetic: schemes, data degradation, hyperparameters (l. 280 to 281) to Sections 4.1.1 to 4.1.4; three scenarios (l. 323) to three paragraphs and Figures 7 to 9; five hyperparameters (l. 367 to 370) to five rows of Figure 10 and l. 372 to 389; natural aims 1 to 3 (l. 282 to 285) to Sections 4.2, 4.2.1, 4.2.2; the fingerprints of aim 1 are judged qualitatively against Bearth (1953) and Steck et al. (2015), as disclosed (l. 399 to 401) | no finding beyond GB-26, GB-38, GB-42, GB-49 |
| PP-38 | P23 | Lithological units in the subcatchment test | 7 units (Figure 11); 1 without outcrops in the subcatchment (l. 411, Figure 12 caption); Figure 13: 6 KDEs plus ZSF sediments = 7 | no finding |
| PP-39 | P20 | Denominator of the average JS distance | "between all pairs of source XRD signatures and use the average across all combinations" (l. 347); 7 units give C(7,2) = 21 pairs | no finding (count not stated, GB-24) |
| PP-40 | P21 | Comparability within scenarios | scenarios 1 to 3 and the sweeps use the same synthetic domain and pixel grid, so summed errors are comparable within each scenario | no finding; across tracer counts GB-31, across scenarios GB-32 |
| PP-41 | P29, P3 | Inventory of figures: number, page, type, caption, text references | Figures 1 to 3 (p. 22 to 24) schematic; Figure 4 (p. 25) map with insets; Figures 5 and 6 (p. 26, 27) maps, line plots, bars; Figures 7 to 10 (p. 28 to 31) maps, bars, scatterplots; Figure 11 (p. 32) bar chart; Figure 12 (p. 33) map; Figure 13 (p. 34) ridge plot with inset; Figures 14 to 16 (p. 35 to 37) maps and stacked bars; first text references l. 146, 166, 251, 268, 289, 314, 334, 347, 356, 371, 398, 412, 414, 429, 438, 445; no graphical abstract, no appendix figures, no tables | no finding |
| PP-42 | P29 | Reference of every figure in the text of its own section | Figures 1 to 3 in Section 3, Figure 4 in Section 4, Figures 5 to 10 in Section 4.1, Figures 11 to 16 in Section 4.2; panel references in the text upper case ("Figure 5B"), panel labels lower case | no finding (wrong panel pair in GB-27) |
| PP-43 | P3 | Scale bars and raster size across maps | Figure 12: 1 km = 147 px, catchment 13.07 × 7.57 km; Figures 14 to 16: 2 km = 85, 85, 82 px, catchment 13.39 × 7.79, 13.34 × 7.76, 13.37 × 7.78 km; Figure 5a raster 44.3 × 26.2 cells = 13.3 × 7.9 km at 300 m | no finding (differences 2.5 %, within 1 px on the scale bars) |
| PP-44 | P3 | Figure 7 values against l. 332 to 342 | 3 markers per panel; summed error 198 ± 2, 193.5, 274.8; trace 0.7402, 0.7376, 0.7460; data misfit 3.254, 3.490, 3.687 × 10^6; model misfit 1.562, 1.922, 2.461; area difference 0, 0.69 × 10^7, 1.14 × 10^7 m² | no finding for l. 338 to 342 (both misfits increase; the minimal-change map gives the smaller error, as disclosed); general sentence in GB-32 |
| PP-45 | P3 | Figure 9 against l. 357 to 362 | 21 markers at 1 to 21 tracers; summed error 347.3 (1), 348.3 (2), 293.5 (3), 296.6 (4), 224.4 (5), 205.6 (6), 197.6 (7 and more); trace 0.962, 0.917, 0.878, 0.833, 0.796, 0.769, 0.740 (7 and more) | no finding for the threshold of 7 tracers |
| PP-46 | P3 | Figure 10: baseline across rows and statements in l. 377 to 379 and l. 385 to 389 | row 1 at 1200 m (interpolated) 197.6 and 0.741; row 2 for σm of 1.4 and more: 197.4, falling from 209.1 near zero; row 4 at µ = 0.1: 197.2 (minimum; 328.7 at 0.010, 201.2 at 0.316); row 5 at 25 iterations: 197.4 (268.9 at 5, 200.8 at 15, 199.5 at 35, 200.8 to 200.9 from 45) | no finding for rows 2, 4, 5; rows 1 and 3 in GB-33 and GB-34 |
| PP-47 | P3 | Figure 11: normalisation by the maximum (l. 261 to 262) | longest bar per column 245, 244, 245, 244, 243, 244, 244 px; 7 columns in caption order, colours equal to Figure 5j | no finding |
| PP-48 | P3 | Figures 14 to 16 against l. 430 to 447 | zircon stacks: MR granite and MR gneiss shares equal in every age bin; ZSF metabasites 0 in all 13 bins; ZSF serpentinites at most 0.002; uncertainty labels 0.87, 0.82, 0.86 equal to l. 436, 442, 447; colour bar maxima 8620 mm/y (Figure 14), 8.4 mm/y (Figure 15), 12.2 mm/y (Figure 16) | no finding beyond GB-41, GB-42 |
| PP-49 | P29 | Font size in print size | Figure 5 colour bar digits 6.0 pt, 5g ticks 6.2 pt; Figure 6 6.3 pt; Figure 7 6.0 pt; Figures 8 and 9 5.8 pt; Figures 14 and 15 ticks 5.5 pt; Figure 16 legend 5.5 to 5.8 pt; calibration on a 9 pt caption capital: 8.2 pt | no finding (within 0.6 pt of 6 pt), except Figure 10 (GB-33) |
| PP-50 | P24 | Dated events in figures | no figure has a time axis or dated markers; the only date is the detrital sample of 28 June 2019, 13:30 (l. 423 to 424, 437 to 438), not shown in Figures 14 to 16 | no finding |
| PP-51 | P3 | Figure 8, middle panel, against "As the JS distance decreases below 0.55, both absolute error and posterior uncertainty rise sharply" (l. 351 to 352) | trace 0.740 to 0.747 for JS 0.561 to 0.624; 0.838 to 0.842 for JS 0.501 to 0.541; 0.832 to 0.833 for 0.441 to 0.481; 0.880 to 0.893 for JS up to 0.36 | no finding for the uncertainty threshold |
| PP-52 | P3 | Figure 5 statements on resolution and covariance patterns (l. 300 to 304) and iterations (l. 293) | iteration axes of 5g to 5i end at 100; hotspot cells light in 5e and 5f (low covariance); low resolution cells in 5d west of the hotspot | no finding beyond GB-25, GB-48, GB-53 |

### Segment 4: Discussion, Conclusions, declarations, references (p. 15 to 21, l. 450 to 653)

#### Substantive findings

**GB-49 The Discussion states effects of the tracer number and of the number of source areas that the Results either qualify or do not test, and the second feeds the application conditions of the Conclusions**

| Field | Content |
|---|---|
| Check | P15, P2, P11 |
| Location | p. 15, l. 458 and l. 460 to 461; p. 16, l. 484 to 485; p. 12, l. 360 to 365; Figure 9 (p. 30) |
| Quotation | "Including a broad set of tracer minerals further improves model stability and resolution."; "A higher number of distinct source areas leads to higher posterior resolution and lower uncertainty."; "Our results suggest that the method is best applied in catchments with minimal sediment storage, multiple mineralogically distinct source areas" |
| Concern | Section 4.1.3 reports "The inversion with 7 tracers results in approximately the same posterior solution as with the full tracer set" (l. 360) and that reducing the number of tracers "has a comparatively limited effect" (l. 365) provided the most informative are retained; 7 of 21 tracers are 33.3 % of the set (Python), and above that number no further improvement is reported. Resolution was not evaluated in scenario 3; Figure 9 shows summed error, posterior uncertainty and the misfit trade-off only. "further improves" is therefore stronger than the result and in part contrary to it. No test in Sections 4.1 or 4.2 varies the number of source areas: the scenarios vary map mismatch, fingerprint blending and tracer number (l. 323 to 365), the sweeps five hyperparameters (l. 367 to 389). The only related observation, lower resolution of small units (l. 299 to 300), concerns unit size, not unit number. Yet the statement enters the conditions introduced by "Our results suggest" (l. 484 to 485). |
| Suggestion | Rewrite l. 458, for example "A minimum number of informative tracer minerals (here about seven of 21, selected by PCA) is needed; beyond this, additional tracers change the posterior little (Section 4.1.3)."; either add a synthetic test with different numbers of source units to Section 4.1.3, or mark l. 460 to 461 as an expectation with a reference and remove it from the list in l. 484 to 485. |
| Status | verified (pages 12, 15, 16; absence of a source-number test); inferred (ratio) |
| Severity | moderate |
| Source | S3, S4 |

**GB-50 The manuscript's own application rules are not checked against its own natural case: the lithology is partly inferred under ice, and the XRD-only JS distance needed for comparison with the 0.55 threshold is not reported**

| Field | Content |
|---|---|
| Check | P5, P18, P19 |
| Location | p. 15, l. 463 to 466; p. 9, l. 270 to 272; p. 12, l. 351 to 354; p. 15, l. 447 to 448; Figure 7 (p. 28) |
| Quotation | "we recommend applying this method in catchments where: a) the spatial distribution of source lithologies is well constrained, b) the source units show strong mineralogical contrasts" |
| Concern | For a): in the Gorner catchment the lithology under ice is inferred (l. 270 to 272), and the Steck et al. (2015) map differs from the map used by about 1.14 × 10^7 m² (Figure 7, measured); the ice-covered share of the catchment is not quantified. For b): the only natural JS values reported are 0.48 for zircon, below the synthetic threshold of 0.55 (l. 352) and consistent with the unstable zircon result, and 0.57 for the combined set (l. 447 to 448). The value for the XRD fingerprints of Figure 11 is missing (also needed for the comparison in GB-42), so whether the main natural case meets the manuscript's own condition is not shown. Synthetic JS values come from 21 tracers, zircon values from 13 age bins (Figure 14); comparability across dimensions is not discussed. |
| Suggestion | Report the JS distance of the natural XRD fingerprints in Section 4.2 and place all three natural values on the axis of Figure 8; state the ice-covered area share; discuss in Section 5 that the Gorner case meets recommendation a) only partly and what follows for Figures 13 to 16. |
| Status | verified (values from text, measured on Figure 7); inferred (comparability across dimensions) |
| Severity | moderate |
| Source | SD |

**GB-51 The second criterion of an ideal fingerprint, stability between source and sink, is not tested, and the remedy the Discussion names for grain-size effects is not stated for the manuscript's own samples, which the figures show taken by a pump sampler**

| Field | Content |
|---|---|
| Check | P15, P18 |
| Location | p. 15, l. 469 to 473; p. 1, l. 24 to 25 (repeated p. 3, l. 91 to 92); p. 9, l. 251 to 253; p. 14, l. 423 to 424; Figure 1c (p. 22); Figure 3a (p. 24) |
| Quotation | "This can be diminished by powdering samples and using depth-integrated suspended sediment samples to average out sorting effects during transport (Butler et al., 2019)."; "An ideal fingerprint is 1) capable of distinguishing among sources and 2) remains stable during erosion, transport, and storage" |
| Concern | The limitation is named in the Discussion. Criterion 1 is tested (JS distance, scenario 2); criterion 2 is not. The sources are in-situ bedrock samples, powdered (l. 251 to 252); the sinks are suspended sediment, labelled "pump sampler" in Figures 1 and 3. The only description of a detrital sample is a date and time (l. 423 to 424). Neither the grain-size fraction of the detrital samples, nor whether they were depth-integrated as the Discussion recommends, nor any size matching between bedrock powder and suspended sediment is stated; the mitigation of preferred orientation is conditional ("should help cancel out", l. 473). Were the Gornergletscher samples depth-integrated? If not, the grain-size limitation applies to the natural results. |
| Suggestion | State in Sections 3.4 and 4.2 how the detrital samples were taken (sampler, intake depth, integration, grain-size fraction) and in l. 469 to 471 whether the remedy was applied; test conservativeness, for example with a range test of detrital values per mineral against the source ranges, or by comparing bedrock powder with fine material of the same unit. |
| Status | verified (absence); assumption (sampling mode and its effect, posed as question) |
| Severity | moderate |
| Source | S4, SD |

**GB-52 The Conclusions do not take up any of the three research aims of the natural-data tests, and the Discussion takes up only the third**

| Field | Content |
|---|---|
| Check | P15 |
| Location | p. 16, l. 477 to 489; p. 15, l. 450 to 476; p. 10, l. 282 to 285; p. 13, l. 399 to 401; p. 14, l. 413 to 418 |
| Quotation | "1) to investigate whether the inferred XRD source fingerprints align with the expected mineralogical compositions of the lithologies, 2) to test if sediment samples from a subcatchment are attributed only to lithologies present within the subcatchment boundaries, 3) to assess how the incorporation of XRD-based fingerprints alongside zircon data improves the stability and accuracy of the posterior solution." |
| Concern | The Conclusions report synthetic results only ("Using synthetic forward-inverse experiments, we show", l. 482). Aim 1 (fingerprints against expected mineralogy, l. 399 to 401) and aim 2 (natural known mixture, Section 4.2.1, with "Some spillover" from adjacent lithologies, l. 414 to 415) appear neither in the Discussion nor in the Conclusions; aim 3 appears only in the Discussion (GB-42). The overclaim of the Abstract on the natural data (l. 8) is treated in GB-03. |
| Suggestion | Add to Section 6 one sentence per aim with its answer and limits, for example on the spillover in the Gorner-Grenz test and on the single-sample basis of the zircon comparison, and discuss aims 1 and 2 briefly in Section 5. |
| Status | verified |
| Severity | moderate |
| Source | S4 |

**GB-53 The Conclusions say that resolution and posterior covariance can be used to assess reliability, but no result relates these metrics to the known error of the synthetic tests, and in Figure 5 the lowest posterior covariance lies where the error is largest**

| Field | Content |
|---|---|
| Check | P15 |
| Location | p. 16, l. 483 to 484; p. 10, l. 297 to 304; Figure 5c, 5d, 5e (p. 26) |
| Quotation | "We highlight how model resolution and posterior covariance can be used to assess the reliability of inferred erosion patterns." |
| Concern | Section 4.1.1 describes the spatial patterns of resolution and covariance (l. 299 to 304) but does not relate them to the true error, although the synthetic test is the only setting in which the error is known. The text places the main differences "within larger lithological units" (l. 297) and lower resolution in "Small lithological units" (l. 299), and states that "Posterior covariance is lowest in regions of high erosion" (l. 301). In Figure 5 the lowest posterior covariance (light colours in panel e) lies at the hotspot, where panel c shows the strongest difference (at least minus 2.26 mm/y, GB-25). If this reading holds, the covariance signals the highest certainty where the reconstruction is least accurate. Does a pixel-wise comparison support the use stated in l. 483 to 484? |
| Suggestion | Add to Section 4.1.1 a pixel-wise comparison of the absolute difference between true and posterior map with the resolution diagonal and the posterior covariance diagonal (for example a scatter plot or rank correlation), and qualify l. 483 to 484 according to the outcome. |
| Status | verified (missing comparison); inferred (spatial coincidence in Figure 5, from colour scales and the measurement in GB-25), posed partly as question |
| Severity | moderate |
| Source | S4 |

**GB-54 The Conclusions attribute the condition "minimal sediment storage" to the results, although no result tests storage and the Discussion treats it as a model assumption**

| Field | Content |
|---|---|
| Check | P15 |
| Location | p. 16, l. 484 to 485; p. 15, l. 466 to 468 |
| Quotation | "Our results suggest that the method is best applied in catchments with"; "minimal sediment storage" |
| Concern | The Discussion says: "We caution against using this method in catchments with significant sediment storage, as the inversion directly links sediment provenance to erosion rates and assumes immediate sediment export (Collins et al., 2020)" (l. 466 to 468). This is a consequence of the model assumption, supported by literature, not a result of the tests; "storage" occurs only in l. 23, 25, 90, 91, 467 and 485 (Python search), never in Sections 4.1 or 4.2. |
| Suggestion | Rephrase l. 484 to 485, for example "Because the model assumes immediate sediment export, the method is best applied in catchments with minimal sediment storage; our results further suggest". |
| Status | verified |
| Severity | minor |
| Source | S4 |

**GB-55 Two proposals in the outlook run against the manuscript's own results: zircon U-Pb data, whose only run was "highly unstable", and land-use classes, where fingerprint distinctiveness, the main limiting factor, is not addressed**

| Field | Content |
|---|---|
| Check | P15, P9 |
| Location | p. 16, l. 487 to 489; p. 15, l. 466; p. 14, l. 430 to 436; p. 12, l. 351 to 354 and l. 363 to 364 |
| Quotation | "Similarly, the method is not limited to XRD-derived fingerprints and can be applied to other types of tracer data, including zircon U-Pb age distributions or geochemical compositions."; "the approach is flexible and can be extended to alternative classifications such as land use or sub-catchments." |
| Concern | Each proposal held against the manuscript's results: (1) Zircon U-Pb: the only zircon-only inversion gave "extreme erosion rate values (>8000 mm/y), low resolution, and a high total normalized uncertainty" (l. 435 to 436); the manuscript links this to missing and duplicated fingerprints (l. 430 to 434, GB-41), a condition the outlook does not name. (2) Land use: Section 4.1.3 shows that poorly distinguishable fingerprints are "a major limitation in source attribution" (l. 353 to 354) and the strongest factor (l. 363 to 364); whether XRD fingerprints of land-use classes on the same lithology are distinct enough is not examined. (3) Sub-catchments: consistent with Section 4.2.1. (4) Geochemical compositions: no own result for or against. Are mineralogical fingerprints of land-use classes expected to be distinct where the classes share the same lithology? |
| Suggestion | In l. 488 to 489 add that zircon fingerprints require sufficient zircon yield and complete fingerprints for all source units (Section 4.2.2); in l. 466 and l. 487 to 488 add that land-use classes are suitable only where their mineralogical fingerprints are distinct (average JS distance above about 0.55, Section 4.1.3) and how this would be tested. |
| Status | verified (zircon point); assumption (land-use point, posed as question) |
| Severity | moderate |
| Source | S4, SD |

**GB-56 The code and data availability statement covers only "the inversion tests" and does not say whether raw XRD diffractograms, sample metadata, zircon ages, the inferred geological map and the synthetic test inputs are included**

| Field | Content |
|---|---|
| Check | P12 |
| Location | p. 16, l. 490; data sources at p. 9, l. 250 to 262 and l. 270 to 272; p. 10, l. 288 to 289; p. 11, l. 327 to 334; p. 12, l. 343 to 349 and l. 355 to 358; p. 13, l. 391 to 398; p. 13, l. 406 to p. 14, l. 413; p. 14, l. 423 to 425 |
| Quotation | "The data and codes used for the inversion tests in the study are available at https://doi.org/10.5281/zenodo.17120374" |
| Concern | The manuscript provides a persistent DOI, and it resolves to the Zenodo record "fdedonck/Non-Linear-XRD-Inversion: First public release", v1.0.0, 15 September 2025, CC BY 4.0, one zip file of 49.3 MB. The statement itself names only the "inversion tests". The Methods name at least these data sources, and the statement does not say whether each is published, available on request or withheld: (1) raw diffractograms of source and detrital samples (l. 250 to 253) and the Peak Finder output (l. 254 to 255); (2) sample metadata: number and position of source samples per unit (l. 251, l. 391 to 392), number and dates of the "multiple detrital samples" (l. 406, l. 413) and position of the dated sample (l. 423 to 424); (3) zircon U-Pb ages (l. 423 to 425); (4) the inferred geological map (l. 270 to 272); (5) the synthetic inputs: true map (l. 288 to 289), synthetic fingerprints (Figure 5k), modified maps (l. 327 to 334), the 20 blended fingerprint sets (l. 348 to 349) and the PCA subsets (l. 355 to 358). The repository README lists raw XRD, RRUFF and raw zircon data, so the material may be there; a reader of the manuscript cannot tell this from the statement. The content of the zip file was not checked. |
| Suggestion | Expand the statement at l. 490 into an itemised list of the data sources (1) to (5), each with its location in the archive or the reason for withholding, state the archive version (v1.0.0), and say whether the archived XRD data are raw diffractograms before or after the Peak Finder correction. |
| Status | verified (wording of the statement; DOI resolution and record metadata; README content); inferred (whether items 1 to 5 are in the zip file, which was not opened) |
| Severity | moderate |
| Source | S2 |

**GB-57 Several reference entries lack elements that the other entries carry, and one gives a wrong author initial**

| Field | Content |
|---|---|
| Check | P16, P4 |
| Location | p. 17, l. 521 (Bearth); p. 19, l. 583 (Gjems); p. 19, l. 599 to 600 (Lafuente); title case in p. 17, l. 507 and l. 517, p. 18, l. 552 to 553 and l. 557, p. 19, l. 595 and l. 604 to 605, p. 20, l. 643 |
| Quotation | "Lafuente, B., Downs, R., Yang, Y., and Stone, N.: The power of databases: the RRUFF project, Highlights in Mineralogical Crystallography"; "Gjems, O.: Studies on clay minerals and clay-mineral formation in soil profiles in Scandinavia, 1967."; "Bearth, P.: Blatt 535 Zermatt - Geologischer Atlas der Schweiz 1:25 000, 1953." |
| Concern | (1) Lafuente et al.: the publisher record gives the authors as Lafuente, B., Downs, R. T., Yang, H., and Stone, N., the chapter as part of the book "Highlights in Mineralogical Crystallography" (Walter de Gruyter), pages 1 to 29, DOI 10.1515/9783110417104-003, with 2016 as year; the entry has "Yang, Y.", no "in:", no publisher and no DOI, unlike the other chapter entries (Aster et al., l. 514 to 516; Menke, l. 610 to 611). (2) Gjems has no series, publisher or place. (3) Bearth has no publisher. (4) Article titles are partly in title case (Allan; Backus and Gilbert; Das et al. 2023; Davis and Fox; Klages and Hsieh; Lipp et al.; Wall and Wilding) and otherwise in sentence case. 9 of 64 entries have no DOI, which is acceptable for maps, theses and books. |
| Suggestion | Replace l. 599 to 600 by "Lafuente, B., Downs, R. T., Yang, H., and Stone, N.: The power of databases: the RRUFF project, in: Highlights in Mineralogical Crystallography, Walter de Gruyter, 1 to 29, https://doi.org/10.1515/9783110417104-003, 2015." and check the year against the book; complete Gjems (series, volume, pages) and Bearth (publisher, place); set all article titles in one case. |
| Status | verified (Lafuente details in the publisher record; missing elements and mixed case on page images 17 to 20) |
| Severity | minor |
| Source | S4 |

#### Minor corrections

| ID | Location | Quotation | Replacement | Source |
|---|---|---|---|---|
| KK-32 | p. 15, l. 460 | "which can be challenging in glaciated catchments" | "which can be challenging in glacierized catchments", the term used in l. 16, 62, 83, 129 and 329 | S4 |
| KK-33 | p. 16, l. 490 | "available at https://doi.org/10.5281/zenodo.17120374" | "available at https://doi.org/10.5281/zenodo.17120374." | S4 |
| KK-34 | p. 16, l. 491 | "All authors (FDD, FH, BB, TA)" | "All authors (F.D.D., F.H., B.B., T.A.)", the form used in l. 491 to 494 | S4 |
| KK-35 | p. 17, l. 522 to 523 | "Master’s thesis, University of Lausanne, unpublished master’s thesis, 2021." | "Master’s thesis, University of Lausanne, 2021." | S4 |
| KK-36 | p. 17, l. 526 | "no. 20 in Reviews in mineralogy, Mineralogical society of America" | "no. 20 in Reviews in Mineralogy, Mineralogical Society of America" | S4 |
| KK-37 | p. 19, l. 578 | "[No title found]" | "Landscape indicators of human impacts to riverine systems" (publication record) | S4 |
| KK-38 | p. 20, l. 612 to 613 | "New-York, 378" | "New York, pp. 378" | S4 |
| KK-39 | p. 20, l. 635 | "ISBN 9780898715729 9780898717921" | "ISBN 9780898715729" | S4 |
| KK-40 | p. 20, l. 639 | "Bomb-fallout137 Cs as a marker" (superscript attached to "fallout", space before "Cs", page image) | "Bomb-fallout ¹³⁷Cs as a marker" | S4 |

#### Verification log

| ID | Check | Checked | Values | Result |
|---|---|---|---|---|
| PP-53 | P4 | Section numbering and headings, whole manuscript | 1 Introduction (l. 9), 2 Introduction (l. 76), 3 Methods (l. 143) with 3.1 to 3.4 (l. 144, 165, 220, 249), 4 Validation (l. 266) with 4.1, 4.1.1 to 4.1.4 (l. 286, 287, 309, 322, 366), 4.2, 4.2.1, 4.2.2 (l. 390, 402, 419), 5 Discussion (l. 450), 6 Conclusions (l. 477) | no gaps; one duplicated section (GB-04); no tables, appendices or graphical abstract |
| PP-54 | P4, P3 | Figure numbers and every figure and panel reference | Figures 1 to 16 on p. 22 to 37, numbered consecutively in the order of first reference (l. 146, 166, 251, 268, 289, 314, 334, 347, 356, 371, 398, 412, 414, 429, 438, 445); panel references 1A to 1D, 2A to 2C, 3A to 3E, 5A to 5K, 6C to 6G checked against captions and panels | all figures numbered without gap or double and referenced; all panel targets exist, except l. 317 (GB-27) |
| PP-55 | P4 | Equation numbers and equation references | eq. 1 to 22 on p. 5 to 8; references "eq. 7" (l. 190, 240, 245), "eq. 12 and eq. 13 into eq. 11" (l. 200), "eq. 14 and eq. 15 in eq. 10" (l. 204), "eq. 16" (l. 213, 217), "eq. 1-4" (l. 263) | no gaps; every reference reaches an equation of the stated content |
| PP-56 | P4 | Citations against the reference list in both directions (Python), years, name spelling, "et al." | 64 entries, 64 distinct cited author-year keys; citations without entry 0; entries without citation 0; years agree for all 64; "et al." for all entries with three or more authors, "and" for all two-author entries; list in alphabetical order | no orphan in either direction; content and name errors in GB-05, GB-07, GB-57 |
| PP-57 | P15 | Each statement of Discussion and Conclusions mapped to a result | distinct signatures essential (l. 457) to l. 351 to 354 and Figure 8: consistent; accurate delineation crucial (l. 459 to 460) to l. 337 to 342 and l. 363 to 364: consistent, the counterexample of the minimal-change map not discussed; recommendations a) and b) (l. 464 to 465): see GB-50; c) multiple tracers: consistent with the 7-tracer threshold; storage caution (l. 466 to 468): assumption with literature; XRD limitations (l. 469 to 476): literature-based; "reliably recovered" (l. 482): see GB-23 and GB-25; "robust across a range of parameters" (l. 483): hedged, range not named (GB-03); extension to sub-catchments (l. 488): consistent with Section 4.2.1 | findings for the remaining statements: GB-42, GB-49, GB-51, GB-53, GB-54, GB-55 |
| PP-58 | P15 | Verbs against evidence | "validated" (l. 451); "highlight" (l. 456, 483); "are essential", "is crucial" (l. 457, 460); "proves" (l. 462); "show" (l. 482); "suggest" (l. 484) | "proves" and "Our results suggest" for storage and source-area number exceed the evidence (GB-42, GB-49, GB-54); the other verbs match their results |
| PP-59 | P15 | Outlook proposals held against own results | land use (l. 466, 488), sub-catchments (l. 488), zircon U-Pb (l. 489), geochemical compositions (l. 489) | sub-catchments consistent with Section 4.2.1; geochemistry without own evidence; zircon and land use in GB-55 |
| PP-60 | P15 | Framework and key terms of the Introduction and the aims in Discussion and Conclusions | Bayesian, frequentist and hybrid framing (l. 43 to 57): MAP framework applied, comparison with BLMM and hierarchical models not revisited; erosion rate maps, spatially informed inversion, posterior uncertainty: taken up (l. 451 to 455, 478 to 484); natural aims 1 to 3; cost and time efficiency; spatio-temporal dynamics | missing: GB-01, GB-02, GB-52 |
| PP-61 | P16 | Grammar, word choice and characters in l. 450 to 499, on page images 15 and 16 | paragraphs of Sections 5 and 6, declarations | errors in l. 455 (GB-09), l. 461 to 463 (GB-42), l. 460, 490, 491 (KK-32 to KK-34); no other hyphenation or character errors |
| PP-62 | P16 | Uniformity of the reference list l. 500 to 653, on page images 17 to 21 | DOI form "https://doi.org/" in 55 of 64 entries; article numbers with thin space throughout; journal names spelled identically; line break inside the Steck et al. DOI (l. 632 to 633) at an existing hyphen; wide word spacing in l. 584 and l. 625 is justification | deviations in GB-05, GB-57, KK-35 to KK-40; check against a citation style not run (optional check) |

## Optional checks

| Area | What it needs | Responsible | Run |
|---|---|---|---|
| DOI resolution | one request per reference entry with a DOI | `science-quellenapparat-pruefung` | no |
| Citation style | the name of the style or the style rules of the journal | `science-zitierstil-harvard-ctr` or the journal's style rules | no |
| AI statement against publisher policy | the publisher's policy on the use of AI | this review, on request | no |
| Relation to the authors' own prior work | the authors' prior work, as files or DOIs | this review, on request | no |
| Journal requirements | the author guidelines of the target journal | this review, on request | no |
| Subject accuracy | access to the sources of the checked statements and a selection of sections | `science-faktenbeleg-pruefung`, `geo-frage-belegbasiert-klaeren` | no |

## Limits of this review

- Checked version: egusphere-2025-4695.pdf, 37 pages, SHA-256 9c80676054f96ecd6f00f4d2a8b5ba568e03c6949e3856d363ac1c4abb42e7bd.
- Sources not readable: full texts of Das et al. (2023, 2024), Niu et al. (2020) and De Doncker et al. (2020); Klages and Hsieh (1975), Haddadchi et al. (2013), Fathabadi and Jansen (2022), Yang et al. (2025), Collins et al. (2020), Torres Astorga et al. (2020) and Avdeev et al. (2011); full texts of Wilson et al. (1993), Walden et al. (1997) and Blaen et al. (2016) (title and metadata only); the UNESCO 2009 report (title page); the master's thesis of Belotti (2021); the content of the Zenodo archive (zip file not opened). The statements in PP-01 and PP-04 that rest on these sources were not checked.
- Findings with status assumption for at least one sub-statement: 14 of 57.
- Optional checks run: 0 of 6.
- Omitted instances: none.
- Discarded findings: 0 of 96 instance findings; all had the mandatory fields, and none was refuted on re-checking. 67 instance findings were merged into 26 findings; two instance findings (one on cost and timing, one on the processing chain) each contributed to two findings. Of 65 instance minor corrections, 20 went into findings (one of them in part), and 21 were merged into 7. One finding (GB-12) and eight minor corrections were added during merging from notes of the instances that no responsible instance had treated. Two verification logs on figure numbering were merged into one (PP-54), and one verification log was added (PP-07).
- Figure values: measured by the figure instance at 300 and 600 dpi and by the design instance at 150 dpi; where both measured the same quantity, the values agree within the stated tolerance, and the 300 dpi values are given.
