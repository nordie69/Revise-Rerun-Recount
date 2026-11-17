# Review report: From XRD signal to erosion rate maps

| Field | Value |
|---|---|
| Manuscript | De Doncker, F., Herman, F., Belotti, B. and Adatte, T. (2025) From XRD signal to erosion rate maps. EGUsphere preprint, https://doi.org/10.5194/egusphere-2025-4695 |
| Version checked | egusphere-2025-4695.pdf, 37 pages, SHA-256 9c80676054f96ecd6f00f4d2a8b5ba568e03c6949e3856d363ac1c4abb42e7bd |
| Date | 2026-10-18 |
| Language | English |
| Review instances | Segments 1 to 4, figures, study design; the six review instances ran as separate agents, each without context from the others or from the merge |
| Note | Line numbers follow the printed margin numbers on p. 1 to 21; figure pages 22 to 37 have no margin numbers and are cited by page and panel. Sections 1 and 2 of the manuscript are identical (GB-03), so locations in the Introduction name both copies where relevant. |

## Summary

The manuscript is a method development study with synthetic forward-inverse tests and a natural case study. It presents a Bayesian maximum a posteriori inversion that turns binned XRD peak-area fingerprints of source lithologies and detrital suspended sediment into erosion rate maps: the forward model mixes source tracer abundances with weights proportional to the erosion rates, erosion rates are log-parameterised, a Gaussian model covariance with smoothing distance L regularises the underdetermined problem, and uncertainty is expressed by posterior covariance, resolution and a normalised posterior covariance. Steepest descent and quasi-Newton updates are compared on one synthetic "true" map with a single hotspot; three degradation scenarios (geological map mismatch with three maps, 20 levels of fingerprint blending, 1 to 21 tracers) and one-at-a-time sweeps of five hyperparameters follow. The natural tests use the Gornergletscher catchment (Pennine Alps) with seven lithological units, 21 tracer minerals and 300 m pixels: a known-mixture analogue with samples from the Gorner-Grenz subcatchment, from which one unit (ZSF sediments) is absent, and a comparison of zircon U-Pb (13 age bins), XRD and combined inversions for one detrital sample of 28 June 2019. Key numbers: thresholds of the average Jensen-Shannon distance of 0.55 and 0.44 for rising error, about 7 informative tracers for a stable solution, total normalised posterior uncertainty 0.87 (zircon), 0.82 (XRD) and 0.86 (combined), and average JS distance 0.48 (zircon) and 0.57 (combined).

## Strengths

1. The synthetic forward-inverse design with a known "true" map gives every synthetic test an absolute error reference, and the shared baseline run (QN, 25 iterations, L = 1200 m) reproduces at an absolute error of about 197 to 198 in Figures 5, 7, 8, 9 and 10, so the degradation and sweep results can be compared across figures (PP-16, PP-18).
2. The Results state failure cases instead of omitting them: the initial instability of steepest descent and its correction before the reported run, non-convergence for strongly blended fingerprints and the non-monotonic result of the minimally changed map are named in the text (PP-14, PP-17); this gives the reader the material needed to qualify the summary claims, which the Abstract and Conclusions do not yet do (GB-02).
3. The natural known-mixture analogue uses a subcatchment from which one mapped unit is absent, so a field sample can test source attribution without laboratory mixtures; the subcatchment geology in Figure 12 agrees with the description in the text (PP-23), although the test as reported does not yet separate the absent unit from present ones (GB-52).
4. Posterior uncertainty is reported as maps and as a scalar total, and the reported values are internally consistent: the normalised map of Figure 5f matches Eq. 22 within measurement uncertainty, the totals 0.87, 0.82 and 0.86 agree between text and Figures 14 to 16, and the imputed zircon fingerprint is disclosed and visible in the source fingerprints (PP-12, PP-25, PP-26).

## Weaknesses

1. Several summary claims go beyond the tests: time and cost efficiency is not measured, convergence and robustness are stated without the conditions under which they were observed, the combined zircon and XRD inversion is less certain (0.86) than XRD alone (0.82) although it is said to improve the solution further, a broad tracer set, a higher number of source areas and zircon-only data are recommended without or against the reported evidence, and the forward model mixes linearly although the stated novelty is a non-linear mixing model (GB-01, GB-02, GB-10, GB-59, GB-61, GB-62, GB-63). Restrict Abstract, Discussion and Conclusions to what Sections 4.1 and 4.2 show, with the tested ranges and the number of natural samples.
2. The synthetic validation favours recovery and is partly described against its own figures: the prior equals the mean of the truth, the data appear noise-free and one true map is used; non-convergence may be produced by the 25-iteration cap; five of 20 blending runs are unaccounted for; the sweeps of L and σd are described against Figure 10; the steepest descent comparison does not support "more accurate"; and the ranking of degradation factors compares ranges that are not commensurate (GB-33, GB-37, GB-40, GB-42, GB-46, GB-48). Add ensembles of true maps, noisy data and offset priors, report all runs including failed ones, and rewrite Section 4.1.4 to what Figure 10 shows.
3. The natural validation and the fingerprint basis are not yet independent checks: the known-mixture analogue does not separate the absent unit from present ones, the zircon benchmark is confounded by an imputed fingerprint, the map under the ice is inferred and its uncertainty is not propagated, window peak areas are not compared with an independent mineral quantification, and normalisation by the per-sample maximum biases a linear mixture (GB-13, GB-25, GB-32, GB-52, GB-53, GB-60). Add a laboratory known-mixture series with a pass criterion fixed beforehand, a Rietveld or modal comparison of the source powders, and natural inversions repeated with the alternative maps and an equal source partition for zircon and XRD.
4. Formulation and reproducibility fall short in several places of moderate weight: Eq. 19 inverts a singular matrix, Eq. 9 lacks the minus sign, the plotted resolution diagonals exceed what Eq. 21 allows, notation and the uncertainty metric change names and formulas, and the export estimate, the prior of the natural runs, the XRD windows, instrument settings, spatial layers and most data classes are neither reported nor deposited (GB-14, GB-15, GB-17, GB-18, GB-19, GB-20, GB-22, GB-27, GB-64). Correct the equations to the implemented form, add tables of inputs, windows and settings, and extend the data statement to every data class.

## Findings by segment

### Segment 1: Abstract, Introduction (p. 1 to 5)

#### Substantive findings

**GB-01 The time and cost efficiency named in the Abstract, the objective and the closing sentence of the Introduction is not measured anywhere in the manuscript.**

| Field | Content |
|---|---|
| Check | P33, P31 |
| Location | p. 1, l. 3 to 4; p. 2, l. 35 and l. 40 to 42 (duplicate p. 4, l. 102 and l. 107 to 109); p. 3, l. 74 to 75 (duplicate p. 5, l. 141 to 142); p. 15, l. 451 to 455 |
| Quotation | "In this study, we validate a time- and cost-effective fingerprinting approach based on X-ray diffraction (XRD) data." and "we show and validate the potential of binned XRD peak-area data as a cost- and time-efficient approach for constructing erosion rate maps" |
| Concern | The manuscript motivates XRD with the cost of other tracers (l. 35, "many of these methods are expensive and time-consuming") and states efficiency as a validated result. It gives no number of samples, no preparation or instrument time, no cost per sample and no comparison with the zircon U-Pb workflow that the same study used (l. 423 to 425, l. 494). Efficiency is therefore a design intention, not a measured property. Rated major because "validate" in the Abstract and at the end of the Introduction presents it as a result of the study. |
| Suggestion | In Section 3.4 or 4.2.2 add a table with the number of source and detrital samples, preparation and measurement time and cost per sample for XRD and for zircon U-Pb in this study; otherwise reword l. 3 to 4 and l. 74 to 75 (and 141 to 142) to "potentially cost-effective" and drop "validate" for this property. |
| Status | verified (absence of any effort or cost figure, full text searched) |
| Severity | major |
| Source | SD |

**GB-02 Abstract and Conclusions claim consistent convergence, reliable recovery and robustness without the conditions under which the Results observed them.**

| Field | Content |
|---|---|
| Check | P2, P6, P15 |
| Location | p. 1, l. 7 to 8; p. 16, l. 482 to 483; counter-evidence at p. 10, l. 288 to 289; p. 11, l. 312 to 313; p. 12, l. 352 to 353 and l. 360 to 361; p. 13, l. 380 and l. 385 to 387; p. 14, l. 435; Figure 8 caption (p. 29) |
| Quotation | "Forward-inverse tests with synthetic data demonstrate consistent convergence of the posterior solution. The application to real-world datasets further validates the practical utility and robustness of the model." and "we show that the true erosion pattern can be reliably recovered, and that the method is robust across a range of parameters" |
| Concern | The Results disclose their limits, which is to their credit: the steepest descent scheme "proved unstable" (l. 312); for many blended fingerprint sets "the inversion fails to converge to a stable posterior solution" (l. 353), and the most blended case "did not have a stable solution and is therefore not plotted" (Figure 8 caption); the error rises rapidly below 7 tracers (l. 360 to 361); very low data standard deviations "lead to large differences" (l. 380); step sizes below 0.1 prevent convergence (l. 385 to 386); fewer than 25 iterations fail (l. 387); the zircon inversion is "highly unstable" (l. 435). All synthetic tests use one true map with a single localised hotspot (l. 288 to 289), and the natural tests rest on one subcatchment and one dated detrital sample (l. 406 to 413, l. 423 to 424). Abstract (l. 7 to 8) and Conclusions (l. 482 to 483) carry none of these conditions and name no range. The disclosure exists; its consequence for the summary claims is not drawn. Rated major because these sentences state the main result of the synthetic and natural validation. |
| Suggestion | Rephrase l. 7 to 8 and l. 482 to 483 with the conditions under which convergence and recovery were observed, for example: "for the synthetic hotspot scenario, the QN scheme recovers the true pattern when the average JS distance between sources exceeds about 0.55, at least 7 informative tracers are used, and step size and iteration number are at least 0.1 and 25"; name the failure cases in the Abstract and restrict "real-world datasets" to the one subcatchment and the one sample tested. |
| Status | verified (wording and counter-evidence at the cited lines) |
| Severity | major |
| Source | S3, S4, SD |

**GB-03 The Introduction is printed twice, as Section 1 and again as Section 2, so that every later section number is shifted by one.**

| Field | Content |
|---|---|
| Check | P4 |
| Location | p. 1 to 3, Section 1, l. 9 to 75; p. 3 to 5, Section 2, l. 76 to 142 |
| Quotation | "1 Introduction" and "2 Introduction" |
| Concern | Both sections carry the same heading and the same text: a word-by-word comparison (Python, difflib) of l. 10 to 75 against l. 77 to 142 gives 1153 words in each copy and a similarity ratio of 1.0. The duplicate occupies about three pages and shifts Methods, Validation, Discussion and Conclusions to Sections 3 to 6, although the manuscript has five distinct sections. All six review instances noted the duplication independently. It is a matter of form, hence minor. |
| Suggestion | Delete Section 2 (l. 76 to 142) and renumber Sections 3 to 6 as 2 to 5. |
| Status | verified (page images p. 1 to 5; difflib comparison) |
| Severity | minor |
| Source | S4 |

**GB-04 The short citation "E., 2009" and its reference entry use an initial in place of the author's surname.**

| Field | Content |
|---|---|
| Check | P4 |
| Location | p. 1, l. 11 to 12; p. 3, l. 78 to 79; reference list p. 18, l. 567 to 568 |
| Quotation | "(Gergel et al., 2002; Allan, 2004; E., 2009; Hamel et al., 2015)" and "E., W. D.: The Impact of global change on erosion and sediment transport by rivers, UNESCO 2009" |
| Concern | Citation and entry match each other, so the citation is not orphaned, but "E." is not a surname and the entry lists three initials without a family name; a reversed name field in the reference manager would explain this. A reader cannot find the work under "E." in a catalogue. The UNESCO title page could not be read to confirm the author (request rate-limited), so the identity of the author is put as a question. |
| Suggestion | Can the authors check the author field of this entry? If the report is by D. E. Walling, change the entry at l. 567 to 568 to "Walling, D. E.: The impact of global change on erosion and sediment transport by rivers, UNESCO, ISBN 9789231041358, 2009." and the citations at l. 11 to 12 and l. 78 to 79 to "Walling, 2009". |
| Status | verified (malformed name on page images p. 1, 3 and 18); assumption (that the author is D. E. Walling; source not readable) |
| Severity | minor |
| Source | S4, S1 |

**GB-05 Five citations in the overview of fingerprinting methods do not support the statement they are attached to.**

| Field | Content |
|---|---|
| Check | P13 |
| Location | p. 1, l. 18 to 19 and p. 3, l. 85 to 86 (Barker et al., 1997); p. 1, l. 26 and p. 3, l. 93 (Olley et al., 1993); p. 2, l. 28 and p. 4, l. 95 (Blaen et al., 2016); p. 2, l. 30 and p. 4, l. 97 (Walden et al., 1997); p. 2, l. 31 and p. 4, l. 98 (Kobe, 2021); reference list p. 19, l. 597 to 598 (Kobe entry) |
| Quotation | "Direct measurements, such as sediment traps installed on dams, provide valuable information on sediment fluxes but do not reveal the origin of the transported material (Wilson et al., 1993; Barker et al., 1997; Davis and Fox, 2009)" and "plant pollen content (Brown, 1985; Kobe, 2021)" and "mineralogy (Walden et al., 1997; Nukazawa et al., 2021)" and "nutrients (Blaen et al., 2016; Asadi et al., 2025)" |
| Concern | The overview of tracer families (l. 26 to 35) is broad and gives two or more references for nearly every family. For five references, however, the cited work does not contain what it is cited for. (1) Kobe (2021), HTS Teologiese Studies 77, is titled "Ubuntu as a spirituality of liberation for black theology of liberation"; it mentions neither pollen nor sediment. (2) Walden et al. (1997) use mineral magnetic measurements as tracers, not mineralogical composition; magnetic susceptibility is a separate family in l. 29. (3) Blaen et al. (2016) review in-situ high-frequency monitoring of nutrients and dissolved organic matter in rivers; their abstract mentions neither sediment, fingerprinting nor source apportionment. (4) Olley et al. (1993), cited for geochemistry in l. 26, identify sources with the 226Ra/232Th ratio, 7Be and 137Cs, that is with radionuclides, the family listed in l. 27. (5) Barker et al. (1997) measure bank erosion with terrestrial photogrammetry; they use neither sediment traps nor dams, and their method does locate the origin of the eroded material, against the sentence it is cited for. Each statement keeps at least one other reference, so the results are not affected, but a reader who follows these five references cannot confirm the statements, and the Kobe entry shows that the reference list was not checked against the text. Rated moderate rather than minor for this reason. |
| Suggestion | In l. 31 and 98, remove Kobe (2021) from the text and the reference list (l. 597 to 598) or replace it with the pollen tracer study that was intended. Move Walden et al. (1997) to magnetic susceptibility (l. 29 and 96) and Olley et al. (1993) to radionuclides (l. 27 and 94). Replace Blaen et al. (2016) with a study that uses nutrients as sediment source tracers. Replace Barker et al. (1997) in l. 18 to 19 and 85 to 86 with a sediment trap or reservoir sedimentation study, or rephrase the sentence to cover direct erosion measurements in general. |
| Status | verified (title page or abstract of each source read: Kobe at hts.org.za; Walden at the St Andrews research portal; Blaen at the Birmingham research portal; Olley at EarthRef ERR 67869; Barker at the Portsmouth research portal); for Barker, "no sediment traps or dams" verified, "does locate the origin" inferred from the abstract |
| Severity | moderate |
| Source | S1 |

**GB-06 Quantitative XRD unmixing of sediment sources was published about two decades before Das et al. (2023) and is not cited, which qualifies "recently gained attention" and the framing of the contribution.**

| Field | Content |
|---|---|
| Check | P14 |
| Location | p. 2, l. 36 to 42; p. 4, l. 103 to 109; p. 3, l. 74 to 75 and p. 5, l. 141 to 142; p. 13, l. 404 to 406 |
| Quotation | "X-ray diffraction (XRD) has recently gained attention as a proxy for mineral abundance in provenance analysis but remains underutilized (Das et al., 2023)." and "Building on the work of Das et al. (2023, 2024), we investigate the potential of binned XRD data as a cost-effective fingerprinting method." |
| Concern | The contribution in one sentence: binned XRD peak-area fingerprints of source lithologies, inverted with a spatially informed, log-parameterised Bayesian scheme into erosion rate maps of a glacierised catchment. The Introduction frames the XRD part as recent and as starting with Das et al. (2023, 2024). Two earlier works already used quantitative XRD mineralogy to unmix sediment sources, and neither is in the reference list (checked against p. 17 to 21). Eberl (2004) measured the mineralogy of bed and suspended sediment of the Yukon River with quantitative XRD and calculated the relative sediment contribution of tributaries; Andrews and Eberl (2012) developed the program SedUnMix, which unmixes qXRD mineralogy of up to six source end members and was tested on eleven artificial mixtures of known composition, the known-mixture test that the manuscript replaces with a natural analogue (l. 404 to 406). From Eberl (2004) to Das et al. (2023): 2023 minus 2004 = 19 years. Neither work produces erosion rate maps, so the spatial part of the contribution stands; the XRD-as-fingerprint part is not new, and the manuscript does not say how binned peak areas differ from full quantitative phase analysis in accuracy or cost. Literature: Eberl, D. D. (2004) 'Quantitative mineralogy of the Yukon River system: changes with reach and season, and determining sediment provenance', American Mineralogist, 89(11-12), pp. 1784-1794. Available at: https://pubs.usgs.gov/publication/70026557; Andrews, J. T. and Eberl, D. D. (2012) 'Determination of sediment provenance by unmixing the mineralogy of source-area sediments: the "SedUnMix" program', Marine Geology, 291-294, pp. 24-33. https://doi.org/10.1016/j.margeo.2011.10.007. |
| Suggestion | In l. 36 to 42 (and 103 to 109) cite Eberl (2004) and Andrews and Eberl (2012), replace "recently gained attention", and state what binned peak areas add over qXRD unmixing; in Section 4.2.1 (l. 404 to 406) consider an artificial known-mixture test after Andrews and Eberl (2012). |
| Status | verified (both abstracts read on pubs.usgs.gov and usgs.gov; absence in the reference list checked in the text and on page image p. 19) |
| Severity | moderate |
| Source | S1 |

**GB-07 The contrast between frequentist and Bayesian unmixing is attributed to Niu et al. (2020), a study that, judging from its abstract, makes no such comparison.**

| Field | Content |
|---|---|
| Check | P13 |
| Location | p. 2, l. 45 to 48; p. 4, l. 112 to 115 |
| Quotation | "Where frequentist methods estimate the uncertainty on the resulting source contributions by sampling the different possible sets of source contributions, Bayesian methods use priors, model and data uncertainty to allow error propagation so the a posteriori uncertainty can be inferred from different posterior metrics (Niu et al., 2020)." |
| Concern | The distinction is relevant, because the manuscript places its own approach between Bayesian model families (l. 55 to 57). According to its abstract, Niu et al. (2020) estimate source contributions in an arid catchment with composite fingerprints and a linear mixing model and quantify uncertainty with a Gaussian first-order approximation; the publisher page shows no comparison of frequentist and Bayesian methods. Fathabadi and Jansen (2022), already cited in l. 55, carry this comparison in their title. Is Fathabadi and Jansen (2022), or Haddadchi et al. (2013), the intended source for this sentence? |
| Suggestion | In l. 48 and 115 cite the work that makes the frequentist and Bayesian distinction (for example Fathabadi and Jansen, 2022), and keep Niu et al. (2020) for the linear mixing statement in l. 59 and 126, which its abstract supports. |
| Status | inferred (only the abstract and reference list of Niu et al. (2020) were readable) |
| Severity | minor |
| Source | S1 |

**GB-08 Method 1) of the frequentist list is introduced as "NLLS" and referred back to as "NNLS".**

| Field | Content |
|---|---|
| Check | P38 |
| Location | p. 2, l. 48 to 52; p. 4, l. 115 to 119 |
| Quotation | "the Non-Linear Least Squares (NLLS) (a constrained linear regression)" and "(similar to the NNLS approach, but with a probabilistic error model)" |
| Concern | l. 51 refers back to method 1) of l. 48 under a different acronym, and no NNLS method is introduced elsewhere. The expansion "Non-Linear Least Squares" also sits uneasily with the explanation "a constrained linear regression". Is non-negative least squares meant, which fits both the explanation and the acronym NNLS? |
| Suggestion | Use one acronym at l. 49 and 51 (and l. 116 and 118); if non-negative least squares is meant, write "Non-Negative Least Squares (NNLS)" at l. 48 to 49 and l. 115 to 116. |
| Status | verified (two acronyms on page image p. 2); assumption (that non-negative least squares is meant; posed as a question) |
| Severity | minor |
| Source | S2, S1, S4 |

**GB-09 The research gap and the "underutilized" status of XRD are asserted without a described search, and the novelty statement of the Discussion depends on them.**

| Field | Content |
|---|---|
| Check | P28 |
| Location | p. 2, l. 58 to 61 and p. 4, l. 125 to 128; p. 2, l. 36 to 37 and p. 4, l. 103 to 104; p. 15, l. 454 to 455 |
| Quotation | "However, these approaches typically yield relative source contributions without translating them into spatially explicit erosion rate maps and implicitly rely on a linear mixing scheme (Niu et al., 2020)." and "The novelty of our method lies in the spatially informed approach of this underdetermined inversion problem, and in the incorporation of non-linear mixing model." |
| Concern | The Introduction lays out the families of unmixing methods clearly (l. 43 to 57) and names its own predecessor openly (De Doncker et al., 2020, l. 61). The gap, however, rests on one case study (Niu et al., 2020), whose abstract confirms a linear mixing model and nothing about the field as a whole. No databases, search terms, period or search date are named. This matters because the Discussion turns the gap into a claim of novelty (l. 454 to 455), and because De Doncker et al. (2020), according to their abstract, already converted provenance data into erosion rate maps by least-squares inversion with prior and covariance information. Three searches by this review found no obvious counterexample to the spatial part of the gap; the XRD part has two (GB-06). |
| Suggestion | In l. 58 to 61 (and 125 to 128) state what the gap rests on: a short search statement (databases, search terms, period, date) or a narrower wording such as "the reviews by Haddadchi et al. (2013) and Collins et al. (2020) list no method that ..."; in l. 454 to 455 state the novelty relative to De Doncker et al. (2020) explicitly. |
| Status | verified (no search described, whole text checked); inferred for the scope of De Doncker et al. (2020) (abstract only) |
| Severity | moderate |
| Source | S1 |

**GB-10 The stated novelty of a non-linear mixing model is not supported by the forward model, which remains a linear mixture in the erosion rates.**

| Field | Content |
|---|---|
| Check | P10 |
| Location | p. 2, l. 58 to 61 (duplicate p. 4, l. 125 to 128); p. 5, l. 151 to 152, l. 154 (Eq. 1) and l. 157 to 158; p. 15, l. 454 to 455 |
| Quotation | "Hence, the detrital data are a weighted average of the tracer mineral concentrations, with the weights being the erosion rates." and "We cast the erosion rates in log-space to impose a positivity constraint, hence making this non-linear." and "and in the incorporation of non-linear mixing model" |
| Concern | Eq. 1 is a linear mixture of source concentrations with weights proportional to the erosion rates. The non-linearity arises only from the reparametrisation εj = log(ėj/ė0), that is from the positivity constraint, not from the mixing. The gap named at l. 58 to 59 (reliance on "a linear mixing scheme") therefore has no matching design: the method is a linear mixing model solved in log space. A design that addresses the gap would include a mixing law that departs from linearity (for example grain-size or fertility dependent mixing, or matrix effects on XRD intensities) and test it against the linear one. Rated major because the claim is one of the two stated novelties of the method. The phrase at l. 455 also lacks the article "a". |
| Suggestion | In l. 59 to 61 and l. 454 to 455 replace "non-linear mixing model" by "a linear mixing model with log-parameterised erosion rates (non-linear inversion)"; or, if non-linear mixing is intended, state the mixing law in Section 3.1 and compare it with the linear case in Section 4.1. |
| Status | verified (wording and Eq. 1 on page images p. 2 and 5); inferred (that the gap is left unanswered) |
| Severity | major |
| Source | SD, S4 |

**GB-11 British and American spellings and two notations of the erosion-rate unit are mixed throughout text and figures.**

| Field | Content |
|---|---|
| Check | P16 |
| Location | p. 3, l. 70 and p. 5, l. 137; p. 5, l. 150; p. 9, l. 261; p. 10, l. 303; p. 11, l. 307 and l. 335; p. 12, l. 340 and l. 352; p. 13, l. 398; p. 15, l. 441; labels and captions of Figures 5, 6, 10, 14 to 16 |
| Quotation | "we optimize the hyper-parameters" and "optimisation strategy" and "normalised posterior variance" and "normalized posterior uncertainty" and "centre" and "center of the domain" and "700 mm/yr" |
| Concern | The text switches between -ise and -ize forms and between centre and center within the same paragraphs, and writes the erosion-rate unit as "mm/yr" (l. 352) and "mm/y" (l. 295, 325, 428 and figure labels). The figure labels also mix "Normalised" (Figures 5, 6, 10, 14 to 16) and "normalized" (captions of Figures 14 to 16). Form only. |
| Suggestion | Choose one spelling convention for text, captions and figure labels, and write the erosion-rate unit uniformly as "mm/y" or "mm yr⁻¹". |
| Status | verified (page images) |
| Severity | minor |
| Source | S4 |

#### Minor corrections

| ID | Location | Quotation | Replacement | Source |
|---|---|---|---|---|
| KK-01 | p. 1, l. 5 | "(steepest descent and Quasi-Newtonian)" | "(steepest descent and quasi-Newton)", as at l. 211 and l. 296; "quasi-Newton" in lower case within sentences | S2, S4 |
| KK-02 | p. 2, l. 33 to 34; p. 4, l. 100 to 101 | "including spectrocolourmetrics or multi-proxy approaches" | "including spectrocolorimetry or multi-proxy approaches" | S4 |
| KK-03 | p. 2, l. 50; p. 4, l. 117 | "Generalist Likelihood Uncertainty Estimation (GLUE)" | "Generalized Likelihood Uncertainty Estimation (GLUE)" | S1, S4 |
| KK-04 | p. 2, l. 51; p. 4, l. 118 | "Maximal Likelihood Estimation (MLE)" | "Maximum Likelihood Estimation (MLE)"; for the acronym NNLS in the same sentence see GB-08 | S1, S4 |
| KK-05 | p. 2, l. 55 to 56; p. 4, l. 122 to 123 | "a hybrid between Bayesian linear mixed models and hierarchical Bayesian models" | "a hybrid between Bayesian linear mixing models and hierarchical Bayesian models", as introduced at l. 53 ("Bayesian Linear Mixing Models (BLMM)") | S1, S4 |
| KK-06 | p. 2, l. 61; p. 4, l. 128 | "the inversion framework validated in (De Doncker et al., 2020)" | "the inversion framework validated by De Doncker et al. (2020)" | S1, S4 |

#### Verification log

| ID | Check | Checked | Values | Result |
|---|---|---|---|---|
| PP-01 | P13 | Statements in Segment 1 that report numbers, rankings or evaluations of other works (l. 11 to 61, duplicates l. 78 to 128) | 0 sentences with numbers from other works; 14 evaluative or attributive statements; sources read: Kobe 2021, Walden 1997, Blaen 2016, Olley 1993, Barker 1997, Niu 2020; De Doncker 2020 abstract (synthetic and natural examples, least squares with prior and covariance) consistent with "inversion framework validated"; Niu 2020 abstract ("a linear mixing model") consistent with l. 59; Das 2024 abstract (MixSIAR, contributions 36 to 61 %, 15 to 39 %, 19 to 32 %) consistent with "Building on"; Das 2023 and Yang 2025 not readable; 28 further tracer-list references checked by title only, none contradicting its family | findings GB-05 and GB-07; no further finding |
| PP-02 | P14 | Search for prior work on the contribution (binned XRD fingerprints, spatially informed log-parameterised inversion into erosion maps, glacierised catchment) | 3 searches; candidates Andrews and Eberl 2012 and Eberl 2004 (not in list, proposed); Das 2024, De Doncker 2020, Lipp 2021 (in list, dropped); Ehlers et al. 2015 on glacial erosion from detrital thermochronology (not in list, rejected: neither anticipates nor contradicts the XRD contribution); search results pointing to this preprint or later versions not opened | finding GB-06; no further finding |
| PP-03 | P28 | Gap statements and search description | gap statements at l. 36 to 37, l. 58 to 59 (and l. 103 to 104, l. 125 to 126), p. 15, l. 454 to 455; sentences of the form "no study", "first" or "for the first time": 0; databases 0, search terms 0, period 0, search date 0 | finding GB-09 |
| PP-04 | P38 | Definitions and use of abbreviations and method names over the whole manuscript | XRD defined at l. 36 and again at l. 103, 135, 250, 391 (same object); MAP l. 173; SD l. 210 to 211; QN l. 211, used at l. 217, 293, 296, 320, 426; JS l. 345, used at l. 352 to 353 and Figures 8 and 9, written out again at l. 447; PCA l. 355 to 356; KDE Figure 13 caption; WinXRD Peak Finder at l. 254 and l. 473, shortened at l. 396 (one object) | findings GB-08 and KK-01; no further finding |

### Segment 2: Methods, study area, Figures 1 to 4 (p. 5 to 10, Figures p. 22 to 25)

#### Substantive findings

**GB-12 The no-storage and immediate-export assumption is stated only in the Introduction and the Discussion, and its consequence for single instantaneous samples in a glacierised catchment is not drawn.**

| Field | Content |
|---|---|
| Check | P17, P18 |
| Location | p. 5, l. 147 to 148; p. 1, l. 23; p. 14, l. 423 to 424 and l. 437 to 438; p. 15, l. 466 to 468; p. 16, l. 484 to 486 |
| Quotation | "These sediments are then transported or stored." and "We caution against using this method in catchments with significant sediment storage, as the inversion directly links sediment provenance to erosion rates and assumes immediate sediment export" |
| Concern | The forward model in Section 3.1 mentions storage but does not say that the inversion assumes none; the assumption appears in the Introduction ("without modelling storage or transport", l. 23) and as a caution in the Discussion (l. 466 to 468). The natural tests use one sample taken at one time of day for the zircon comparison (l. 423 to 424) and an unstated number of samples at the confluence (l. 413), scaled by an annual export (GB-15). Whether storage under the glacier is negligible, and whether one sample represents the annual erosion pattern, is not discussed for Gornergletscher, although the manuscript recommends the method only for catchments with minimal storage (l. 484 to 486). Question to the authors: what is known about subglacial storage and diurnal variability of provenance at this site? Rated major because the natural results are interpreted as erosion rate maps under this assumption. |
| Suggestion | State the no-storage and steady-state assumption at Eq. 1 in Section 3.1; in Section 4.2 give number, dates and times of all detrital samples and show the spread of the inversions across them; discuss storage at the study site in Section 5. |
| Status | verified (location of the disclosure, single dated sample); assumption (that storage or diurnal variation matters at this site; posed as a question) |
| Severity | major |
| Source | SD |

**GB-13 Normalising each sample by its own maximum peak area is incompatible with the linear mixing of Eq. 1 and biases the recovered contributions.**

| Field | Content |
|---|---|
| Check | P9, P31 |
| Location | p. 5, l. 151 to 152 and l. 154 (Eq. 1); p. 9, l. 260 to 265 |
| Quotation | "Hence, the detrital data are a weighted average of the tracer mineral concentrations, with the weights being the erosion rates." and "these are normalized within each sample by dividing by the maximum observed peak area, yielding relative mineral concentrations on a scale from 0 to 1" |
| Concern | If source j has raw window areas aj with maximum Mj, the mixture of raw areas, normalised by its own maximum, equals up to one common factor the mixture of normalised fingerprints with weights proportional to wj times Mj, not wj. The inversion then returns contributions scaled by the maximum peak area of each source. Numerical example with two sources, raw maxima 10 and 8 and true weights 0.5 and 0.5: recovered weights 0.556 and 0.444, identical to wj Mj normalised (Python). Sources with one strong peak, for example quartz-rich units, are over-weighted. The synthetic tests cannot reveal this, because they generate the detrital data with the same normalised fingerprints and Eq. 1. The intended effect, "minimizing the influence of absolute intensity differences" (l. 264), is stated, not measured. GB-51 shows that the fingerprints plotted in Figures 15 and 16 are rescaled per lithology; whether that scaling carries Mj into A is not stated. Rated major because the bias affects every natural erosion map. |
| Suggestion | In Section 3.4 either normalise by a quantity that preserves linear mixing (for example the sum of all window areas or an internal standard) or carry Mj into A; test the choice in Section 4.1 with synthetic detrital data built from raw mixtures and normalised afterwards, as a laboratory mixture would be. Counter-design: a laboratory known-mixture series of source powders in set proportions, processed with the same pipeline. |
| Status | inferred (algebraic consequence of the stated normalisation and Eq. 1; whether the code applies a correction is not stated) |
| Severity | major |
| Source | SD |

**GB-14 In Sections 3.1 to 3.4 the same objects carry different symbols and the same symbols denote different objects; Eq. 18 and 19 mix the iteration indices n and k, and Eq. 14 lacks the transpose of Eq. 16.**

| Field | Content |
|---|---|
| Check | P38 |
| Location | p. 5, l. 154 to 157 (Eq. 1); p. 6, l. 164 (Eq. 4), l. 175 to 184 (Eq. 5 to 7); p. 7, l. 189 to 190 (Eq. 9), l. 195, l. 201 (Eq. 14), l. 202, l. 205 (Eq. 16), l. 208 to 209 (Eq. 17); p. 8, l. 215 to 216 (Eq. 18), l. 219 (Eq. 19); p. 9, l. 262 to 263; Figure 3 (p. 24) panel d; Figure 10 caption (p. 31) |
| Quotation | "εk+1 the posterior model after k + 1 non-linear iteration steps" and "where Gn is the Jacobian at iteration n" and "the abundance of a given tracer t at pixel xy in At,xy" |
| Concern | (1) Eq. 17 counts iterations with k; Eq. 18 and 19 use n for the iterate and k inside the prior term of the same update (εk − εprior), so it is not defined which iterate enters the prior term. (2) n denotes the number of pixels (Eq. 1, Eq. 4, where εn is the last pixel), the iteration (Eq. 18, 19, l. 216), the tracer mineral (Figure 3d, "tracer mineral n") and, as nm, the maximum number of iterations (Figure 10 caption); m denotes the number of tracers (Eq. 1, Eq. 4) and the model subscript (Cm, εm, σm). (3) The tracer matrix is Aij with i tracer and j pixel (l. 155 to 156) but At,xy at l. 262 to 263, while Eq. 9 uses i and j for two pixels. (4) The model vector is εm in Eq. 5 to 7 and ε in l. 176, 179 and Eq. 10 to 17; predicted data are d(εm) (Eq. 7), dε (l. 183, 195) and dn (Eq. 18, 19). (5) The gradient of the data misfit is G Cd⁻¹(dε − dobs) in Eq. 14 but Gᵀ Cd⁻¹(dε − dobs) in Eq. 16. (6) The second misfit term is "prior misfit" ϕprior (l. 184, Eq. 10, 15) and "model misfit" elsewhere (15 text occurrences against 1). Notation alone would be minor; rated moderate because item (1) leaves the update rule of Eq. 18 and 19 ambiguous for reimplementation. |
| Suggestion | Use k as the only iteration index in Eq. 17 to 19, l. 209 and l. 216 and kmax in Figure 10; write (εk − εprior) with the same index as the iterate in Eq. 18 and 19; keep n for the number of pixels and m for the number of tracers and give the model subscript another letter; write Aij at l. 262 to 263 and use other letters for the pixel pair in Eq. 9; use ε throughout Eq. 5 to 7; add the transpose in Eq. 14; use one name for ϕprior. |
| Status | verified (all symbols on page images p. 5 to 9, 24 and 31) |
| Severity | moderate |
| Source | S2, SD |

**GB-15 The inputs of the natural inversions are not reported: the sediment export estimate that scales all erosion rates, the prior mean, which is given as "the average true erosion rate" although no true rate exists for natural data, and the inversion parameters of Section 4.2.1.**

| Field | Content |
|---|---|
| Check | P11, P19, P8, P25 |
| Location | p. 5, l. 159 to 160 (Eq. 2); p. 3, l. 65 to 66 (duplicate p. 5, l. 132 to 133); p. 13 to 14, l. 402 to 418; p. 14, l. 426 to 428; p. 15, l. 444 to 445 and l. 452 to 454; p. 16, l. 479 to 480 |
| Quotation | "For simplicity, we redefine the data vector d as scaled by the total erosion rate:" and "an estimate of the total annual suspended sediment export from the catchment" and "a prior equal to the average true erosion rate, and a step size µ of 0.1" |
| Concern | Through Eq. 2 the export estimate sets the absolute level of all natural erosion rates: the mm/y values of Figures 13 to 16 and the value above 8000 mm/y at l. 435 that is used as evidence of instability. The manuscript names the estimate as one of four required inputs (l. 65 to 66, l. 452 to 454, l. 479 to 480) but gives no value, source, year, conversion from mass to erosion rate (density, contributing area) or uncertainty, neither for the Gornergletscher nor for the Gorner-Grenz subcatchment. For the zircon, XRD and combined inversions the prior is "the average true erosion rate" (l. 428; by reference at l. 437 and l. 444 to 445), a wording carried over from the synthetic tests; for natural data no true rate exists, so the value used and its derivation are unknown. Question to the authors: was the prior mean derived from the export estimate? Section 4.2.1 gives no inversion parameters at all. The magnitude statements of Section 4.2 therefore rest on inputs the reader cannot see. |
| Suggestion | Add to Section 4.2 a list of inputs per natural case: export estimate with value, source, year, conversion and uncertainty, and whether this uncertainty enters Cd; prior mean with value and derivation in place of "average true erosion rate" at l. 428; and the inversion parameters of Section 4.2.1. |
| Status | verified (absence of the values; wording at l. 428); assumption (derivation of the prior; posed as a question) |
| Severity | moderate |
| Source | S3, SD |

**GB-16 The rescaled forward model is called "dimensionless", while the data standard deviation is given in mm/y, so the scale of σd relative to the data is undefined.**

| Field | Content |
|---|---|
| Check | P8 |
| Location | p. 6, l. 161; p. 5, l. 157 and l. 159 to 160 (Eq. 2); p. 10, l. 294 to 295; p. 11, l. 325; p. 14, l. 427 to 428 |
| Quotation | "This allows us to rewrite the forward model in a simplified, dimensionless form:" and "a model standard deviation of 3 (dimensionless, as epsilon is dimensionless), a data standard deviation of 0.01 mm/y" |
| Concern | After Eq. 2 the data vector is multiplied by the total erosion rate, so d carries the unit of an erosion rate, while l. 161 calls the resulting form dimensionless; the reference rate ė0 is set to 1 "to respect dimensional consistency" (l. 157). The text gives σm explicitly as dimensionless and σd in mm/y. Which unit d has in Eq. 3 and Eq. 7 decides what σd = 0.01 mm/y means relative to the data, and the sweep of σd in Figure 10 (row 3) cannot be related to the measurement precision of XRD peak areas. The point came from a hint outside the checklist of instance S2; no instance had checked the unit of d. |
| Suggestion | State in Section 3.1, after Eq. 2 and Eq. 3, the unit of d and of Cd, and give σd in the same unit or as a relative value; remove "dimensionless" at l. 161 if d carries mm/y. |
| Status | verified (wording on page images p. 5, 6 and 10); inferred (that d carries the unit of an erosion rate after Eq. 2) |
| Severity | moderate |
| Source | ZF |

**GB-17 The quasi-Newton update in Eq. 19 inverts a matrix that is singular for the underdetermined problem the manuscript describes.**

| Field | Content |
|---|---|
| Check | P25 |
| Location | p. 6, l. 170 to 172; p. 8, l. 219 (Eq. 19); p. 8, l. 225 (Eq. 20) |
| Quotation | "Our inverse problem is underdetermined: the number of tracers, representing the data we have, is smaller than the number of pixels for which we want to infer the erosion rates." |
| Concern | On page image p. 8 the matrix inverted in Eq. 19 is Gnᵀ Cd⁻¹ Gn without the prior term Cm⁻¹. It is n by n with rank at most m (21 tracers) and, because A has only 7 distinct columns (one per unit), at most 7 (SD script: rank 7 for about 819 pixels). It has no inverse, so Eq. 19 cannot be computed as printed. Eq. 20 contains the full Hessian Gᵀ Cd⁻¹ G + Cm⁻¹. Question to the authors: was the full Hessian or a pseudo-inverse used in the code? |
| Suggestion | Correct Eq. 19 in Section 3.2 to the update actually implemented, for example with (Gᵀ Cd⁻¹ G + Cm⁻¹)⁻¹, and state how the step size µn is chosen. |
| Status | verified (printed equation on page image p. 8; l. 170 to 172); inferred (singularity); assumption (what the code does; posed as a question) |
| Severity | moderate |
| Source | SD |

**GB-18 The model covariance of Eq. 9 is printed without a minus sign in the exponent, so the prior covariance would grow with the distance between pixels.**

| Field | Content |
|---|---|
| Check | P8 |
| Location | p. 7, l. 189 (Eq. 9) and l. 190 |
| Quotation | "Cm(i, j) = σm² exp(si,j²/L²)" |
| Concern | On page image p. 7, Eq. 9 reads σm² exp(si,j²/L²), without a minus sign. With a positive exponent the covariance grows without bound with the Euclidean distance s between pixels, the matrix is not a valid covariance, and L would not act as the smoothing distance described at l. 190 and l. 372 to 376. The code presumably uses a squared-exponential form, exp(−s²/L²) or exp(−s²/(2L²)); which of the two also changes the meaning of L by a factor √2 and hence of the values 1200 m and 3000 m. Question to the authors: which form was implemented? The point came from a hint outside the checklist of instance S2; no instance had checked Eq. 9. Rated moderate because a reader who reimplements Eq. 9 as printed cannot reproduce any inversion. |
| Suggestion | Correct Eq. 9 in Section 3.2 to the form used in the code, for example Cm(i, j) = σm² exp(−si,j²/(2L²)), and state the factor in the exponent. |
| Status | verified (missing sign on page image p. 7); assumption (form used in the code; posed as a question) |
| Severity | moderate |
| Source | ZF |

**GB-19 The plotted resolution diagonals close to 1 are not possible for the resolution operator of Eq. 21 with 7 source units and about 819 pixels.**

| Field | Content |
|---|---|
| Check | P8 |
| Location | p. 8, l. 230 to 236 (Eq. 21); p. 10, l. 299 to 300; p. 14, l. 436; p. 16, l. 483 to 484; Figure 5d (p. 26); Figure 6d (p. 27); Figures 14 to 16, panel "Resolution diagonal" (p. 35 to 37) |
| Quotation | "Where the diagonal of R is close to 1, data have improved our knowledge considerately relative to the prior." and "We highlight how model resolution and posterior covariance can be used to assess the reliability of inferred erosion patterns." |
| Concern | For the linearised problem R = C̃m Gᵀ Cd⁻¹ G has eigenvalues in [0, 1) and rank at most rank(G), so the sum of its diagonal is below rank(G). Because Aij depends only on the lithology of pixel j (l. 262 to 263, Figure 2c), rank(G) is at most 7. Colour measurement of Figure 5d (300 dpi, nearest colour on the colour bar): 99.1 % of the mapped area has values of at least 0.94, 85.9 % at least 0.98. With about 819 pixels (catchment 73.7 km² measured on Figure 4 with the 1 km scale bar, pixel 300 m) the plotted diagonal sums to at least about 763, against an upper bound of 7 (SD script: trace 7.00 for a comparable configuration, largest diagonal element 0.415). Figure 14 shows the same near-black field on a scale ending at 1.0 (page image p. 35). The plotted quantity is therefore not the diagonal of R as defined, and the formula used is not given. Figure 5f (normalised posterior covariance 0.33 to 0.99) is also hard to reconcile with near-perfect resolution. The interpretations at l. 300 and l. 436 and the reliability claim at l. 483 to 484 rest on these maps, hence major. |
| Suggestion | Give in Section 3.3 the formula used to compute R, check it against the bound trace(R) below rank(G), replot Figures 5d, 6d and 14 to 16, and revise the interpretations at l. 299 to 304 and l. 436. |
| Status | verified (wording; colour bar values on the page images); inferred (pixel count, colour quantification, trace bound) |
| Severity | major |
| Source | SD |

**GB-20 The third uncertainty metric appears under seven names and with two different formulas, so a reader cannot tell which quantity the values 0.87, 0.82 and 0.86 and the axes "Trace(post. cov.)" show.**

| Field | Content |
|---|---|
| Check | P38, P29 |
| Location | p. 8, l. 236 to 239 (Eq. 22); p. 10, l. 303; p. 10, l. 306 to p. 11, l. 307; p. 11, l. 335; p. 14, l. 436 to 437; p. 15, l. 441 to 442 and l. 446 to 447; Figure 5 (p. 26) panels f and h with caption; Figure 7 (p. 28) middle scatterplot; Figures 8 and 9 (p. 29, 30) middle panels; Figure 10 (p. 31) second column; Figures 14 to 16 (p. 35 to 37) right panels |
| Quotation | "The third metric is the ratio between the posterior model covariance and the “prior” model covariance." and "a high total normalized uncertainty" |
| Concern | Names found in text and on the page images: "normalised posterior covariance" (Figure 5f title and caption, Figure 6 caption), "normalised posterior variance" (l. 303), "Normalised covariance trace" (Figure 5h title), "posterior covariance" for the curve of Figure 5h (l. 306), "normalized posterior uncertainty" (l. 335, 441, 446; Figures 10, 14 to 16), "total normalized uncertainty" (l. 437) and "Posterior uncertainty" with the axis "Trace(post. cov.)" (Figures 7 to 9) or "Trace(post.covar.)" (Figure 10). The formulas differ: Eq. 22 is a ratio of square roots, that is of standard deviations; l. 436 to 437 gives the ratio of traces tr(Cm,post)/tr(Cm), that is of summed variances without a root; the sentence at l. 236 to 237 speaks of a ratio of covariances. The two choices give different numbers: for two pixels with prior variance 1 and posterior variances 0.25 and 1.0, the trace ratio is 0.625 and the mean of the square-root ratios 0.75 (Python). The map of Figure 5f follows Eq. 22 (PP-12), while the axis label "Trace(post. cov.)" names an unnormalised trace, yet its values lie in the range of the normalised total: Figure 7, original geology, 0.7402, against 0.7409 in Figure 5h at iteration 25 (measured). The posterior covariance also has two symbols, C̃m (Eq. 20, 22) and Cm,post (l. 436). The totals carry the comparison of zircon, XRD and combined data in Section 4.2.2. |
| Suggestion | In Section 3.3 define two quantities with one name and symbol each: the per-pixel map (Eq. 22, stating that it is taken elementwise on the diagonal) and the scalar summary (trace ratio, as a numbered equation); use these names in l. 303, 306, 335, 437, 441, 446, in all panel titles and in the axis labels of Figures 5 to 10 and 14 to 16 (for example "tr(Cpost)/tr(Cm)"), and write the posterior covariance with one symbol. |
| Status | verified (names and formulas on page images p. 8, 10, 14, 26, 28, 31, 35 to 37; values measured); inferred (that the "Trace(post. cov.)" axes show the normalised trace) |
| Severity | moderate |
| Source | S2, AB |

**GB-21 Several components of the inversion and of the synthetic tests are named but not specified, so the tests cannot be rebuilt.**

| Field | Content |
|---|---|
| Check | P8 |
| Location | p. 9, l. 243 to 244; p. 10, l. 288 to 295; p. 11, l. 312 to 314 and l. 330 to 334; p. 12, l. 343 to 347 and l. 355 to 357; Figure 5b legend (p. 26) |
| Quotation | "In initial experiments, the steepest descent approach proved unstable, requiring the normalization of the gradient." and "We perform a Principal Component Analysis (PCA) to retain the subset of tracers that explain the maximum variance in the mineralogical fingerprints." |
| Concern | Not given: (1) shape, amplitude and background of the "true" erosion map; (2) how the synthetic fingerprints of Figure 5k were generated and how they relate to the measured ones of Figure 11; (3) whether noise was added to the synthetic data; (4) the normalised-gradient steepest descent update and its step rule, which differ from Eq. 18; (5) the rule that turns principal components into a subset of original tracers; (6) the blending formula and its parameter values; (7) how the "minimal changes" map was constructed; (8) how the JS distance is computed for fingerprints normalised to their maximum rather than to unit sum; (9) the criterion for the hatched "Low-confidence areas"; (10) the step size of the first QN test (l. 293 to 295). The definition of the total normalised uncertainty is treated in GB-20. |
| Suggestion | Add a subsection or appendix to Section 4.1 with items (1) to (10), each with formula or parameter values, and refer to the script names in the Zenodo record. |
| Status | verified (absence of each item in text and captions) |
| Severity | moderate |
| Source | SD |

**GB-22 Instrument, acquisition settings, software versions and sampling dates of the XRD workflow are not given.**

| Field | Content |
|---|---|
| Check | P35, P7 |
| Location | p. 9, l. 250 to 258; p. 13, l. 396 to 397; p. 16, l. 490; p. 9, l. 267 to 268 |
| Quotation | "To characterise the mineralogical fingerprints of both source and detrital samples, we employed X-ray diffraction (XRD) analysis." and "the WinXRD Peak Finder algorithm corrects for baseline drift and removes the background noise, facilitating the identification of local maxima through thresholding and peak fitting" |
| Concern | Not given: diffractometer, radiation, 2θ range, step width and counting time, sample mass and preparation, WinXRD version, threshold and fitting settings, RRUFF entries used, programming environment of the inversion, and the sampling dates of source and detrital samples. The thresholds of the peak finder directly change the window areas. Because only one sample is dated (l. 423 to 424), it cannot be checked whether all XRD data were produced under one protocol. |
| Suggestion | Add to Section 3.4 a table of instrument and acquisition settings, software versions and peak-finder settings, and to Section 4.2 a sample table with dates, times and sampling method. |
| Status | verified (absence in text, captions and statements) |
| Severity | moderate |
| Source | SD |

**GB-23 The XRD processing chain from diffractogram to tracer value cannot be reproduced: windows, averaging and aggregation per unit are not specified.**

| Field | Content |
|---|---|
| Check | P8 |
| Location | p. 9, l. 251 and l. 257 to 262; p. 13, l. 393 to 398; Figure 11 (p. 32) |
| Quotation | "diagnostic 2θ windows for each mineral are selected from RRUFF database reference spectra" and "we average the total peak area within the 2θ windows corresponding to each mineral" |
| Concern | The 21 windows (2θ limits) are not listed anywhere; "average the total peak area" does not say whether areas are summed or averaged and over what; the number of source samples per unit and how several samples become one fingerprint (mean, median, single sample) are not stated; variability within units is not reported, so σd is not linked to measurement variability. The selection of windows is a judgement step without a described rule. The missing window table also limits the data statement (GB-64) and the identification of the tracer named "Chrysolite" (GB-49). |
| Suggestion | Add to Section 3.4 a table of the 21 windows with RRUFF identifiers, the exact area formula, the number of samples per unit and the aggregation rule, and report the variability within units alongside Figure 11. |
| Status | verified (absence in text and captions) |
| Severity | moderate |
| Source | SD |

**GB-24 The alignment to a pure quartz pattern cannot work as described for source samples without quartz.**

| Field | Content |
|---|---|
| Check | P26 |
| Location | p. 9, l. 256 to 257; p. 13, l. 396 to 397; p. 15 to 16, l. 473 to 475; Figure 11 (p. 32), column ZSF ophiolites (serpentinites), row Quartz |
| Quotation | "to correct for instrumental or sample-related misalignments in peak position, the diffractograms are aligned to a pure quartz pattern" |
| Concern | Figure 11 shows no quartz bar for the ZSF serpentinites. An alignment to a quartz pattern needs quartz peaks in the sample. The manuscript does not say how serpentinite samples, or detrital samples with little quartz, were aligned; the procedure is stated for all samples without this exception. Question to the authors: which reference phase was used for these samples? |
| Suggestion | State in Section 3.4 how samples without detectable quartz were aligned (other reference phase, internal standard, or no alignment) and quantify the residual peak shift for these samples. |
| Status | verified (no quartz bar in Figure 11 on page image p. 32); assumption (that another phase or no alignment was used; posed as a question) |
| Severity | moderate |
| Source | SD |

**GB-25 Window peak areas are presented as mineral concentrations, and their agreement with the known lithology is asserted without a criterion or an independent quantification.**

| Field | Content |
|---|---|
| Check | P31, P32 |
| Location | p. 9, l. 258 to 262; p. 13, l. 393 to 401; Figure 11 (p. 32) |
| Quotation | "yielding relative mineral concentrations on a scale from 0 to 1" and "The mineralogical fingerprints derived from processed and binned XRD data align well with established knowledge of the lithology in the Gorner Glacier catchment" |
| Concern | The binning measures diffracted intensity in windows, not mineral content; the list itself contains a group and two of its members ("Pyroxene", "Omphacite", "Diopside", l. 394 to 395), whose windows must overlap (see also GB-50 for identical rows). "Align well" has no criterion and no comparison with an independent quantification such as Rietveld refinement or modal mineralogy. Read on Figure 11: Monte Rosa granite has a tremolite bar close to its quartz bar, and the Stockhorn-Tuftgrat-Gornergrat unit shows antigorite and chrysotile at about half of its maximum. Question to the authors: are these values expected for these rocks, or do they reflect window overlap? The first aim of the natural tests (l. 282 to 283) is thus answered by assertion. Rated major because all natural inversions take these values as source fingerprints. |
| Suggestion | In Section 4.2 compare the binned values of the source samples with an independent quantification of the same powders (Rietveld refinement or modal analysis), report a quantitative agreement measure, document the overlap of windows, and call the values "window peak-area indices" instead of "mineral concentrations" unless the comparison supports the latter. |
| Status | verified (wording, list and bar readings on page image p. 32); assumption (mineralogical expectation for tremolite and serpentine minerals; posed as a question) |
| Severity | major |
| Source | SD |

**GB-26 The catchment and four of the seven lithological units carry up to five different names across text, captions and legends, and the control unit of Section 4.2.1 is described in Section 4 under a different name than in all maps and results.**

| Field | Content |
|---|---|
| Check | P38, P2, P16 |
| Location | p. 9, l. 267 and l. 272; p. 9 to 10, l. 273 to 279; p. 10, l. 282 and l. 299; p. 12, l. 340; p. 13, l. 392 and l. 400; p. 14, l. 411, l. 414 and l. 431 to 434; p. 15, l. 463; p. 16, l. 498 to 499; Figure 4 (p. 25) and Figure 12 (p. 33) legends and Figure 12 caption; Figure 5 (p. 26) panel j legend; Figure 11 caption (p. 32); Figure 13 (p. 34) labels; Figures 15 and 16 (p. 36, 37) legends |
| Quotation | "Gorner-gletscher catchment" and "Gorner Glacier catchment" and "while Penninic Mesozoic sedimentary units (Bündnerschiefer) consist mainly of calcareous mica schists and quartzites" and "the Monte Rosa garnet-gneiss (MR g-g) unit" |
| Concern | Catchment: "Gorner-gletscher" (l. 267, Figure 11 caption), "Gornergletscher" (l. 272, 282), "Gorner Glacier" (l. 392, 400, 498, 499), "Gorner gletscher" (l. 463), "Gorner glacier" (legends of Figures 5, 15, 16). Units, confirmed on the page images: (1) ZSF sediments: "Zermatt", spaced hyphen, "Saas Fee sediments" in the legends of Figures 4 and 12, with outcrops "metamorphic bündnerschiefer"; "Penninic Mesozoic sedimentary units (Bündnerschiefer)" at l. 274 to 275, set apart from the "Zermatt-Saas Fee ophiolites" by "while"; "Zermatt Saas-Fee sediments" (l. 299); "ZSF sediments" (l. 414, Figures 5, 11, 13, 15, 16). The outcrop legend of Figure 4 shows that both names denote one unit, the unit whose expected zero contribution carries the known-mixture test (l. 410 to 416). (2) Monte Rosa garnet gneiss: "Monte Rosa (garnet gneiss and micaschist)" (Figures 4, 12), "Monte Rosa (gneiss, micaschist)" (Figures 11, 13), "MR gneiss, mica" (Figures 5, 15, 16), "Monte Rosa garnet-gneiss (MR g-g)" (l. 432 to 434 only); l. 275 to 276 describes "The Monte Rosa nappe" as one entity. (3) Stockhorn, Tuftgrat, Gornergrat: five forms, among them "S.,T.,G." without expansion (Figures 5, 15, 16), and l. 276 speaks of three units where the maps have one. (4) ZSF metabasites: three forms. The Zermatt-Saas Fee zone itself is written "Zermatt-Saas Fee" (l. 273 to 274, 431, 432), "Zermatt Saas-Fee" (l. 299), "Zermatt-Saas-Fee" (l. 340), "Zermatt- Saas Fee" (Figure 12 caption) and with a spaced hyphen (l. 411, 414, legends), and ZSF is defined only at l. 414, after the long form has appeared four times. A naming issue alone would be minor; rated moderate because it hinders tracing the control unit of Section 4.2.1 from the geological description to the results. |
| Suggestion | Insert after l. 279 a table of the seven map units with full name, short label and legend colour; state there that the Bündnerschiefer form the unit labelled "ZSF sediments" (or rename the unit); introduce "Zermatt-Saas Fee (ZSF)" at l. 273 to 274; use exactly these labels and one form of the catchment name (for example "Gornergletscher") in l. 267 to 499 and in Figures 4, 5, 11, 12, 13, 15 and 16. |
| Status | verified (all forms on page images p. 9, 10, 12 to 16, 25, 26, 32 to 37; identity of Bündnerschiefer and ZSF sediments via the outcrop legend of Figure 4); inferred (identity of "MR g-g" with "Monte Rosa (garnet gneiss and micaschist)", because Figure 4 has only two Monte Rosa units) |
| Severity | moderate |
| Source | S2, S3, S4, AB |

**GB-27 Third-party and author-built spatial inputs (land cover, outcrops, geological map basis, the lithology inferred under the ice) are named only in the credit line of Figure 4 and appear neither in the reference list nor in the data statement.**

| Field | Content |
|---|---|
| Check | P12 |
| Location | Figure 4 (p. 25), credit block and legend; p. 9, l. 270 to 272; p. 6, l. 166 to 167; p. 14, l. 408; p. 11, l. 327 to 334 with Figure 7 (p. 28); p. 16, l. 490; reference list p. 17 to 21 |
| Quotation | "Land cover data: SwissTopo 2018 Geological data: data from Steck et al., 2015, personal communication by L. Baumgartner, outcrops by GeoCover" and "In ice-covered regions, where direct geological mapping is not possible, we infer the lithology based on regional geological knowledge." |
| Concern | The geological map determines the tracer matrix A (l. 166 to 167, l. 408), so it is a primary input of every inversion. Its basis combines a published map (Steck et al., 2015), a personal communication, GeoCover outcrops and the authors' own inference under the ice; the land cover layer comes from SwissTopo 2018; Figure 4 also shows a glacier outline and an "ELA estimation" without source; scenario 1 adds two further maps (Figure 7). The inversion grid has a pixel size of 300 m (1200 m / 4 and 3000 m / 10, l. 294 and l. 373), but the raster itself is not described as available. A text search of the reference list for "SwissTopo" and "GeoCover" gives 0 hits. A map that rests partly on a personal communication can only be reproduced if the resulting map is published. |
| Suggestion | Add the SwissTopo product and the GeoCover sheets with version to the reference list; state at l. 490 whether the inferred geological map, the two scenario 1 maps and the 300 m raster are in the Zenodo record (with format), and under which licence third-party layers are redistributed or where they can be obtained. |
| Status | verified (credit line and legend on page image p. 25; absence in the reference list by text search); inferred (that the inferred map is needed to rebuild A) |
| Severity | moderate |
| Source | S2 |

**GB-28 The citation "Steck et al., 2015" designates two different geological maps, the base map of Figure 4 and the most deviating map of scenario 1, and the mismatch between maps is named in three ways.**

| Field | Content |
|---|---|
| Check | P38 |
| Location | Figure 4 (p. 25) credit block; p. 11, l. 329 to 335; Figure 7 (p. 28) map titles, x-axes, colour bar and caption |
| Quotation | "3) the map proposed by (Steck et al., 2015) with the biggest area mismatch" and "Geology by Steck et al. 2015" |
| Concern | Figure 7 shows three maps: "Originial geology (same as forward)", "Geology with minimal changes" and "Geology by Steck et al. 2015"; in the left scatterplot the Steck map has the largest area difference. The original map, which is also the map of Figure 4 used for all other tests, is credited in Figure 4 to "Steck et al., 2015" as well. One citation thus names the reference map and the map that differs most from it. The mismatch measure is called "area mismatch" (l. 330, 334, 335), "Area difference" (Figure 7 x-axes and caption) and "Geology misalignment (m²)" (Figure 7 colour bar). Rated moderate because the label decides which map a reader would use to reproduce scenario 1. |
| Suggestion | Give the three maps distinct labels in l. 332 to 334, in the credit of Figure 4 and in the titles of Figure 7 (for example "inferred map, this study, after Steck et al. (2015) and pers. comm.", "minimally modified map", "Steck et al. (2015) as published"), say how the published map differs from the inferred one, and use one term for the mismatch measure in text, axes and colour bar. |
| Status | verified (page images p. 25 and 28; text l. 329 to 335) |
| Severity | moderate |
| Source | S2 |

**GB-29 In the legends of Figures 4 and 12, three red-orange classes cannot be told apart by colour.**

| Field | Content |
|---|---|
| Check | P3 |
| Location | Figure 4 legend (p. 25); Figure 12 legend (p. 33) |
| Quotation | "Stockhorn basement, Tuftgrat Mesozoic and GornergratPermo-Mesozoic" |
| Concern | Measured swatches: Stockhorn unit #fc7434, its outcrops #fc3434, Monte Rosa gneiss outcrops #fc5c34. Sums of RGB deviations: unit to Monte Rosa gneiss outcrops 24, Stockhorn outcrops to Monte Rosa gneiss outcrops 40, both within the equality criterion of 40. On the map the colours are further blended with the hillshade, so outcrops of two different units cannot be distinguished. |
| Suggestion | Give the outcrop classes of Stockhorn and Monte Rosa gneiss clearly different hues or a hatch in Figures 4 and 12. |
| Status | verified (measured colours) |
| Severity | minor |
| Source | AB |

**GB-30 Abbreviations and codes in several figures are not resolved in caption or legend.**

| Field | Content |
|---|---|
| Check | P29 |
| Location | Figure 4 land cover legend (p. 25); Figure 5 (p. 26) panel j legend and panel k x-axis; Figures 8 and 9 (p. 29, 30) titles; Figures 15 and 16 (p. 36, 37) legends |
| Quotation | "ELA estimation" and "S.,T.,G." and "avg. JS" |
| Concern | "ELA", "S.,T.,G.", "ZSF" and "MR" are not resolved in any caption except that ZSF and MR are resolved in the caption of Figure 11; JS is resolved only in the text (l. 345). The 21 synthetic tracers of Figure 5k are labelled A to U without saying that they are synthetic placeholders and not the minerals of Figure 11. |
| Suggestion | Resolve the abbreviations in the captions of Figures 4, 5, 8, 9, 15 and 16, and state in the caption of Figure 5 that A to U are synthetic tracers. |
| Status | verified (page images) |
| Severity | minor |
| Source | AB |

**GB-31 Several captions name the content but not how to read it, and the highlighted runs in Figure 10 carry parameter values that differ from those stated for the tests.**

| Field | Content |
|---|---|
| Check | P29, P2 |
| Location | captions of Figures 4, 10, 12, 14, 15 and 16 (p. 25, 31, 33, 35 to 37); Figure 10 (p. 31) third column, rows 1 to 5; p. 10, l. 294 to 295; p. 11, l. 324 to 326 |
| Quotation | "Figure 4. Study area: location, land cover and geology." and "Figure 12. Lithology and outcrops in the Gorner-Grenz confluence subcatchment." and "These sensitivity tests are run with 25 iterations, a smoothing distance of 4 times the pixel size (L = 1200 m), a model standard deviation of 3, a data standard deviation of 0.01 mm/y" |
| Concern | Figure 4: the caption does not mention the land cover inset, the location insets or what "inferred" means. Figure 12: the subcatchment has no boundary line and no legend entry and can only be inferred from the stronger colour saturation in the north-east (the dashed outline appears only in the inset of Figure 13). Figures 14 to 16: no inversion parameters, no sample date, no explanation of the hatching, and the age bins carry the unit "Ma" only on the last label. Figure 10: rows 4 and 5 highlight µ = 0.1 and nm = 25, as stated in the text, but rows 1 to 3 highlight L = 3000 m, σm = 6.2 and σd = 0.003 mm/y instead of 1200 m, 3 and 0.01 mm/y (l. 324 to 326), and neither caption nor text says what the highlighted runs mean (reference run, optimum, threshold). The errors in rows 2 to 5 (about 197 to 201) match the reference value at L = 1200 m in row 1, so the sweeps appear to have used the stated defaults and the labels mark something else. |
| Suggestion | Extend the captions: Figure 4 (insets, meaning of "inferred"), Figure 12 (draw the subcatchment boundary), Figures 14 to 16 (parameters, date 28 June 2019, hatching criterion, age unit), Figure 10 (meaning of the highlighted runs, or highlight the reference values of l. 324 to 326). |
| Status | verified (page images); inferred (that the sweeps used the defaults) |
| Severity | minor |
| Source | AB, S3 |

**GB-32 The natural tests use a geological map that is largely inferred under the ice, although the own synthetic test and recommendation make map accuracy decisive; map uncertainty is not propagated.**

| Field | Content |
|---|---|
| Check | P18, P19 |
| Location | p. 9, l. 270 to 272; p. 12, l. 363 to 364; p. 15, l. 459 to 460 and l. 463 to 464; Figure 4 (p. 25) legend; Figure 7 (p. 28) |
| Quotation | "In ice-covered regions, where direct geological mapping is not possible, we infer the lithology based on regional geological knowledge." and "we recommend applying this method in catchments where: a) the spatial distribution of source lithologies is well constrained" |
| Concern | The manuscript ranks map uncertainty as the second most influential factor (l. 363 to 364) and recommends well-constrained source maps, but applies the method to a catchment where the map under the ice is inferred. The share of pixels with inferred lithology is not given. The alternative map of Steck et al. (2015) differs by about 1.15 × 10⁷ m² (Figure 7), that is 15.6 % of the 73.7 km² catchment (Python: 1.15 × 10⁷ / 7.37 × 10⁷), yet the natural inversions are run with one map only. The disclosure is present; its consequence for Section 4.2 is not drawn. Rated major because all natural erosion maps depend on this map. |
| Suggestion | In Section 4.2 give the fraction of pixels with mapped and with inferred lithology, repeat the natural inversions with the Steck et al. (2015) map and the minimal-change map, and report the differences in Figures 13 to 16. |
| Status | verified (wording; value read on Figure 7); inferred (15.6 %) |
| Severity | major |
| Source | SD |

#### Minor corrections

| ID | Location | Quotation | Replacement | Source |
|---|---|---|---|---|
| KK-07 | p. 5, l. 146 to 147 | "The idea is that each source area has its unique lithological fingerprint (Figure 1B), it undergoes erosion (Figure 1A) and thereby produces sediments" | "The idea is that each source area has its own lithological fingerprint (Figure 1b), undergoes erosion (Figure 1a) and thereby produces sediments" | S4 |
| KK-08 | p. 5 to 11, l. 146 to 149, 166 to 167, 251 to 262, 289 to 319 (all panel references) | "(Figure 1B)" and "(Figure 5K)" and "(Figure 6D, 6E and 6F )" | lower-case panel letters as printed in the figures and captions, for example "(Figure 1b)", "(Figure 5k)", "(Figure 6d, e and f)" | S4, AB |
| KK-09 | p. 5, l. 154, Eq. 1 | "f or i = 1, . . . m" (the word "for" set in math italics) | upright "for" and "i = 1, …, m" | S4 |
| KK-10 | p. 6, l. 174 | "given the observed detrital data and a prior knowledge" | "given the observed detrital data and prior knowledge" | S4 |
| KK-11 | p. 6, l. 175, Eq. 5 (conditional bars rendered as ∣) | "p (εm ∣dobs ) p (dobs ∣εm )" (no relation sign between the two terms on the page image) | insert "=" between p(εm∣dobs) and p(dobs∣εm) | S4 |
| KK-12 | p. 6, l. 181 | "Which, in an approximately Gaussian setting, becomes Tarantola (2005):" | "In an approximately Gaussian setting, this becomes (Tarantola, 2005):" | S4 |
| KK-13 | p. 7, l. 195 and l. 197, Eq. 12 | "= G = A · exp(ε)" | "G = A · diag(exp(ε))", since the Jacobian is an m by n matrix | SD |
| KK-14 | p. 8, l. 236 | "data have improved our knowledge considerately relative to the prior" | "data have improved our knowledge considerably relative to the prior" | S4 |
| KK-15 | p. 8, l. 240 to 241 | "The data misfit explains how well the model - here: our a posteriori erosion rate map - explains the observed data." ("a posteriori erosion" set in italics on the page image) | "The data misfit measures how well the model (here: our a posteriori erosion rate map) explains the observed data.", with only "a posteriori" in italics | S4 |
| KK-16 | p. 9, l. 243 to 244 | "or when it exceeds the user-defined maximal allowed number of iterations" | "or when the number of iterations reaches the user-defined maximum" | S4 |
| KK-17 | p. 9, l. 245 | "weighed by the model covariance" | "weighted by the model covariance" | S4 |
| KK-18 | p. 9, l. 251 to 252; Figure 3 (p. 24), panels a and b | "In a first step, in-situ source samples are collected from every lithological unit across the study area (Figure 3A and 3B)." | "In a first step, detrital samples are collected with a pump sampler (Figure 3a) and in-situ source samples from every lithological unit across the study area (Figure 3b)."; panel a shows "detrital sampling: pump sampler" | S4 |
| KK-19 | Figure 3 (p. 24), panel c, legend | "quarz pattern alignment" | "quartz pattern alignment", as at l. 256 and l. 397 | S2, S4, AB |
| KK-20 | Figures 4 and 12 (p. 25, 33), legends | "biotite schits" and "caclcite-zoisite amphibolites" and "silimanite-biotite gneiss" and "GornergratPermo-Mesozoic" and "metamorphic bündnerschiefer, calcarious mica schist" | "biotite schist"; "calcite-zoisite amphibolites"; "sillimanite-biotite gneiss"; "Gornergrat Permo-Mesozoic"; "metamorphic Bündnerschiefer, calcareous mica schist" | S4, AB |

#### Verification log

| ID | Check | Checked | Values | Result |
|---|---|---|---|---|
| PP-05 | design sketch (P5 to P37, all groups) | Questions, data sources, time axis, environment, declared principles and components, disclosed limits, filled from the full text, all captions and figure pages 22 to 37 | 7 source units, 21 tracers, about 819 pixels of 300 m (73.7 km² measured on Figure 4, scale bar 110 px per km at 300 dpi), 1 dated detrital sample, 3 synthetic degradation scenarios, 5 swept parameters, 3 natural inversions in Section 4.2.2; 4 of 7 test sections (57 %) and 6 of 12 result figures (50 %) rest on model-generated data; disclosed limits: lithology under ice inferred (l. 270 to 272), small units poorly resolved (l. 299 to 300), steepest descent unstable (l. 312 to 316), poorly distinguishable fingerprints (l. 353 to 354), zircon imputation (l. 430 to 434), storage (l. 466 to 468), grain size and orientation (l. 469 to 476) | basis of GB-01, GB-10, GB-12, GB-13, GB-17, GB-19, GB-21 to GB-25, GB-32 and of the design findings in Segment 3 |
| PP-06 | P29, P3 | Figures 1 to 3 (schematic): legends, panel letters, counts | Figure 1b: 4 fingerprint rows of 11 tracer columns, legend colours lithology 1 #64ccd4, 2 #848cc4, 3 #bc9ccc, 4 #cca494, rows coloured 1, 3, 2, 4 from top and not labelled (conceptual figure, not raised); Figure 2c: layers "tracer 1" to "tracer n"; Figure 2b: 11 bars; Figure 3: legends complete except the clock symbol in panel a | no finding beyond KK-19 |
| PP-07 | P4 | Each figure panel reference against panel content and caption | Figure 1a to d (l. 146 to 149) match; Figure 2a to c (l. 166 to 167) match; Figure 3c to e (l. 252 to 262) match, 3a does not (KK-18); Figure 5a to k (l. 289 to 308) match the caption; Figure 6c to f (l. 315, 319) match; "Figure 6G versus Figure 6G" (l. 317) does not (GB-39); Figures 7 to 16 referenced as whole figures, matching the captions | findings GB-39, KK-08, KK-18 |
| PP-08 | P27 | Untested components and where their output flows | inferred geology into A for all natural inversions (GB-32); maximum normalisation into A and d (GB-13); export estimate into d and all mm/y values (GB-15); imputed MR g-g zircon fingerprint into the zircon benchmark and the combined result (GB-53); prior mean into all inversions (GB-15, GB-33); no further untested component steers a selection | no further finding |
| PP-09 | P7 | Whether a single method version applied to all data | no method version, protocol change or instrument change reported besides the steepest descent correction; one sample date (28 June 2019, 13:30); zircon method dated 2021 (thesis); data collection window not stated; settings differ between tests (100 iterations in Section 4.1.1, 25 in Sections 4.1.3 and 4.2.2) and are stated per test | no finding; missing dates in GB-22 |
| PP-10 | P3 | Scale bars of Figures 4, 12 and 14 and the raster cell against the implied pixel size | Figure 4: 1 km = 110 px, catchment width 1448 px = 13.2 km; Figure 12: 1 km = 147 px, width 1924 px = 13.1 km; Figure 14 inset: 2 km = 85 px, width 564 px = 13.3 km; consistent within 2 %; raster cell in Figure 5d 12 ± 0.5 px in a map 569 px wide, 278 ± 12 m against 300 m implied by l. 294, within about 1.5 standard uncertainties | no finding |

### Segment 3: Results of synthetic and natural tests, Figures 5 to 16 (p. 10 to 15, Figures p. 26 to 37)

#### Substantive findings

**GB-33 The synthetic tests combine a prior equal to the mean of the truth, apparently noise-free data from the same forward operator and a single true map, so they cannot show that the true erosion pattern is reliably recovered in general.**

| Field | Content |
|---|---|
| Check | P9 |
| Location | p. 10, l. 288 to 295; p. 11, l. 325 to 326; p. 13, l. 374 to 376; p. 16, l. 482 to 483; Figure 5i (p. 26) |
| Quotation | "a data standard deviation of 0.01 mm/y and a prior equal to the average true erosion rate" and "Using synthetic forward-inverse experiments, we show that the true erosion pattern can be reliably recovered" |
| Concern | (1) The prior mean is the mean of the truth, information no real application has; the manuscript notes that a longer L pulls the posterior towards this prior and lowers the error (l. 374 to 376), which shows that the error metric profits from this oracle. (2) No addition of noise to the synthetic data is described, and Figure 5i shows the data misfit falling to near zero. (3) Data are generated with the same A, grid and forward model as used in the inversion, except in scenario 1. (4) All tests use one true map with one hotspot. The prior is disclosed (l. 295) and its consequence named (l. 374 to 376), but not drawn for the conclusion. Rated major because the conclusion of reliable recovery (l. 482) rests on these tests. |
| Suggestion | Counter-design for Section 4.1: several true maps (hotspots in large and small units, several hotspots, uniform), detrital data with noise at the level of σd and with replicate variability of the fingerprints, and priors offset from the true mean (for example by factors 0.5 and 2); report error and resolution as distributions over these cases, and restrict l. 482 to 483 to the tested conditions. |
| Status | verified (prior, single map, no noise described); inferred (that the data were noise-free, from Figure 5i and the absence of a description) |
| Severity | major |
| Source | SD |

**GB-34 The fingerprint bars in Figures 5, 15 and 16 are semi-transparent while the legend swatches are opaque, so the STG bars match the "MR gneiss, mica" swatch and the MR gneiss bars match the "MR granite" swatch.**

| Field | Content |
|---|---|
| Check | P3 |
| Location | Figure 5 (p. 26) panel j legend and panel k; Figure 15 (p. 36) legend and fingerprint panel; Figure 16 (p. 37) legend and fingerprint panel |
| Quotation | "S.,T.,G." and "MR gneiss, mica" and "MR granite" |
| Concern | Measured colours (Figure 15; Figure 5 identical): legend swatches STG #fc5404, MR gneiss #fc7c44, MR granite #fc9c9c; bars #fc844c (STG), #fca47c (MR gneiss), #fcbcbc (MR granite). Sums of RGB deviations: STG bar to STG swatch 120, to MR gneiss swatch 16; MR gneiss bar to MR gneiss swatch 96, to MR granite swatch 40; MR granite bar to MR granite swatch 64. Under the equality criterion (sum at most 40) a reader matching colours assigns the STG bars to MR gneiss and the MR gneiss bars to MR granite. The bar colours equal the swatches blended with white at about 70 % opacity (STG: 0.7 × (252, 84, 4) + 0.3 × 255 = (253, 135, 79), measured (252, 132, 76) in colour bins of 8). Figures 8, 9 (top rows) and 11 have no colour legend at all. Rated moderate because the source fingerprints of the natural tests cannot be read correctly. |
| Suggestion | Draw the legend swatches with the same opacity as the bars, or draw the bars opaque, in Figures 5, 15 and 16; add a lithology legend to Figures 8, 9 and 11 or refer to the legend of Figure 5j in their captions. |
| Status | verified (measured) |
| Severity | moderate |
| Source | AB |

**GB-35 Units and symbols are missing or inconsistent on the result figures.**

| Field | Content |
|---|---|
| Check | P29 |
| Location | Figure 5 (p. 26) panels a, b, c, e, g; Figure 6 (p. 27) panels a to g; Figures 7 to 10 (p. 28 to 31), y-axes of the first scatterplot column; Figure 11 (p. 32); Figure 13 (p. 34) upper panel |
| Quotation | "Density" and "Posterior erosion rate (mm/y): zircon data" |
| Concern | (1) The colour bars of the erosion and difference maps in Figures 5 and 6 and the absolute error axes of Figures 5g, 6g and 7 to 10 give no unit, while Figures 14 to 16 give mm/y. (2) The symbol e in the error axis label is not defined; the text uses ε (log erosion) and ė (erosion rate). (3) The upper panel of Figure 13 has no density scale, so the ridge heights (Monte Rosa gneiss 416 px, MR granite 144 px, Stockhorn 24 px at maximum) cannot be compared with the lower panel, and the Stockhorn ridge is still 5.5 px high at the right edge (3.27 mm/y), so its distribution is cut off. (4) Figure 11 has no value axis. The label "Trace(post. cov.)" is treated in GB-20. |
| Suggestion | Add units (mm/y) to all erosion-rate colour bars and error axes, define e or use ė, add a density scale or a statement that the ridges share one scale to Figure 13 and extend its x-axis to the end of the Stockhorn distribution, and add a 0 to 1 scale to Figure 11. |
| Status | verified (page images and measurement) |
| Severity | minor |
| Source | AB |

**GB-36 The pixel size and the number of pixels are not stated; the pixel size can only be derived by combining two statements.**

| Field | Content |
|---|---|
| Check | P22 |
| Location | p. 10, l. 294; p. 12, l. 373; p. 6, l. 170 to 172 |
| Quotation | "a smoothing distance of 4 times the pixel size (L = 1200 m)" and "beyond approximately 10 times the pixel size (3000 m)" |
| Concern | Pixel size = 1200 m / 4 = 300 m and 3000 m / 10 = 300 m (Python); consistent, but only by calculation. The number of pixels n is not given anywhere, although the manuscript stresses that the problem is underdetermined (l. 170 to 172) and the error metric is a sum over pixels (GB-43). The ratio of data (21 tracers, 34 combined) to unknowns cannot be stated. |
| Suggestion | State the pixel size (300 m) and the number of pixels n in Section 4 or 4.1.1. |
| Status | verified (wording); inferred (pixel size, computed) |
| Severity | minor |
| Source | S3 |

**GB-37 The comparison of steepest descent and quasi-Newton does not support "more accurate": the settings of the steepest descent run are not stated, the iteration budgets differ, and Figure 6g ends at a lower total error than Figure 5g.**

| Field | Content |
|---|---|
| Check | P3, P11 |
| Location | p. 11, l. 310 to 321; p. 10, l. 293 to 295; Figure 5 (p. 26) panels c and g; Figure 6 (p. 27) panels c, g to i |
| Quotation | "As a result, sharp features and narrow peaks in the posterior erosion rate distribution are smoothed out or missed (Figure 6C), and more iterations are needed to converge to a posterior result as close to the true erosion rate map as the QN posterior (Figure 5)." and "we adopt the Quasi-Newton (QN) approach for all subsequent tests, as it provides a more stable and accurate reconstruction of the erosion rate patterns" |
| Concern | The side-by-side layout of Figures 5 and 6 makes the comparison easy. For the QN test the text gives iterations (100), L, σm, σd and prior (l. 293 to 295); for the steepest descent test it gives none of these, no step size and no form of the gradient normalisation, and Figure 6 runs to 200 iterations against 100 for QN. Measured on panel g: QN reaches its minimum 197.3 ± 0.5 at iteration 20 to 23 and ends at 201.0 ± 0.5 at iteration 100; steepest descent is at 194.0 ± 0.6 from iteration 145 and ends at 193.0 ± 0.6 at iteration 200, 4.0 % below the final QN value (Python: (201.0 − 193.0) / 201.0). Panel c: the colour bar of Figure 5c spans ±2.40 ± 0.02, that of Figure 6c ±1.76 ± 0.01; if the limits are set to the largest absolute difference (question to the authors), the largest pixel error is also smaller for steepest descent, which does not show sharp features "smoothed out or missed". What the figures do show is that steepest descent needs about 140 iterations against about 20 for QN. Rated major because the choice of QN for all later tests (l. 320) rests on this comparison. |
| Suggestion | State in Section 4.1.2 the full parameter set of the steepest descent run, including iterations, step size and gradient normalisation; report final and minimum values of panel g for both schemes, compare them at equal iteration counts or report the iteration at which each reaches a given error, and base the choice of QN on speed if that is the reason; state in the captions of Figures 5 and 6 how the colour limits of panel c are set. |
| Status | verified (settings in the text; panel g values measured); inferred (smaller largest pixel error from the colour limits); assumption (that the limits equal the largest difference; posed as a question) |
| Severity | major |
| Source | AB, S3 |

**GB-38 The lower panels of Figure 6 have no axis titles, no exponent for the data misfit and no colour bar title, and the hatch swatch has no text.**

| Field | Content |
|---|---|
| Check | P29 |
| Location | Figure 6 (p. 27), panel b legend and panels g, h, i |
| Quotation | "(i) trade-off between data- and model misfit during non-linear iterations." |
| Concern | Compared with Figure 5, Figure 6 lacks the x titles "Iteration" in panels g and h, the x title "Data misfit" and the exponent "1e8" in panel i, and the title "Iteration" of the colour bar in panel i. Without the exponent the data misfit values 0.0 to 2.0 cannot be interpreted. The hatch swatch under panel b has no label; in Figure 5 it reads "Low-confidence areas", but neither caption defines the criterion. |
| Suggestion | Add the missing axis and colour bar titles and the exponent to Figure 6; label the hatch and define "low confidence" in the captions of Figures 5, 6 and 14 to 16. |
| Status | verified (page image p. 27) |
| Severity | minor |
| Source | AB |

**GB-39 The oscillations in the posterior covariance named in l. 316 to 317 are not visible in Figure 6h, and the reference "Figure 6G versus Figure 6G" compares a panel with itself.**

| Field | Content |
|---|---|
| Check | P3, P4 |
| Location | p. 11, l. 316 to 317; Figure 6 (p. 27) panels g and h; Figure 5 (p. 26) panel h |
| Quotation | "This limited sensitivity to strong gradients also leads to oscillations in the posterior covariance, visible after 125 iterations, as the Jacobian fluctuates between iterations (Figure 6G versus Figure 6G)." |
| Concern | The same panel is named on both sides of "versus". Panel g shows the summed difference between true and posterior map, not the covariance; the covariance trace is panel h. Measured on Figure 6h: the curve rises to a kink at iteration 138 to 143 and then declines monotonically by about 0.0001 up to iteration 200; the band of markers keeps a constant height of one marker diameter along the plateau, so any oscillation is below 1 px, about 0.00002 in trace units. The kink lies at about iteration 140, not 125. A wrong reference alone would be minor; rated moderate because the described behaviour is not shown by the figure. |
| Suggestion | Is "Figure 5h versus Figure 6h" meant? Correct the reference at l. 317; either show the oscillation with a zoomed inset or a plot of successive differences, or replace "oscillations" by the observed kink at about 140 iterations. |
| Status | verified (self-reference on page image p. 11; absence of a resolvable oscillation measured); assumption (the intended reference; posed as a question) |
| Severity | moderate |
| Source | AB, S4, S3 |

**GB-40 Non-convergence in scenario 2 is not defined and may be produced by the cap of 25 iterations, which lies below the own convergence point of 115 iterations.**

| Field | Content |
|---|---|
| Check | P9, P8 |
| Location | p. 11, l. 324 to 326; p. 12, l. 352 to 353; p. 13, l. 387 to 389; p. 9, l. 243 to 244; Figure 8 caption (p. 29) |
| Quotation | "These sensitivity tests are run with 25 iterations" and "In many of these cases, the inversion fails to converge to a stable posterior solution." and "Beyond 115 iterations, the change in data misfit between successive steps falls below 10−5" |
| Concern | The stopping rule (l. 243 to 244) ends the iterations when the data misfit stops decreasing or at the cap; the cap of 25 is 21.7 % of the 115 iterations after which the own criterion is met (Python: 25 / 115), and 25 is the threshold below which "the posterior fail[s] to converge" (l. 387). "Fails to converge" and "stable solution" are not defined. Iteration cap and fingerprint distinctiveness therefore vary together: blended fingerprints may simply need more iterations, and the JS thresholds 0.55 and 0.44 derived from this test may shift. Rated major because these thresholds are the main quantitative result of scenario 2 and are applied to the natural data (GB-60). |
| Suggestion | Define convergence and stability in Section 3.3; rerun scenario 2 with the stopping rule of l. 243 to 244 and a cap of at least 115 iterations, and report for each of the 20 cases whether and after how many iterations it converged. |
| Status | verified (settings and wording); inferred (confounding of cap and distinctiveness) |
| Severity | major |
| Source | SD |

**GB-41 Scenario 1 tests three maps, one of which contradicts the stated monotonic relation; three points cannot establish it.**

| Field | Content |
|---|---|
| Check | P9, P10 |
| Location | p. 11, l. 332 to 339; p. 12, l. 340 to 342; Figure 7 (p. 28) |
| Quotation | "We observe that the greater the mismatch between the geological map used in the inversion and the one used to generate the synthetic data, the larger the discrepancy between the posterior and true erosion rate maps." |
| Concern | Measured on Figure 7: absolute error 197.5 (same map), 193.5 (minimal changes) and 274.7 (Steck et al. 2015); the second case is 2 % better than the exact map, which the text itself calls surprising (l. 338). With three cases and one non-monotonic case the general relation is not shown; the area mismatch also does not say where the boundaries move relative to the hotspot, which the manuscript names as the cause (l. 340 to 341). Rated moderate because the ranking built on it is treated in GB-46. |
| Suggestion | Counter-design for Section 4.1.3: an ensemble of perturbed maps (random boundary displacements at several controlled mismatch levels, many realisations each, hotspot at several positions); report error against mismatch with its spread, and reword l. 337 to 338 until then. |
| Status | verified (wording; values measured on page image p. 28); inferred (percentage) |
| Severity | moderate |
| Source | SD |

**GB-42 Twenty blending levels are said to be tested, but only 14 appear in Figure 8, and only one omission is explained.**

| Field | Content |
|---|---|
| Check | P23, P34 |
| Location | p. 12, l. 348 to 353; Figure 8 (p. 29), all three scatterplots and caption |
| Quotation | "In total, 20 values between the highly blended and the original synthetic fingerprints are tested" and "Note that the most blended example did not have a stable solution and is therefore not plotted." |
| Concern | Counted on the page image by three instances: 14 points in each scatterplot, at JS of about 0.25, 0.27, 0.34, 0.36 and ten values from 0.44 to 0.62, with gaps between 0.27 and 0.34 and between 0.36 and 0.44. Balance: 20 minus 1 (stated) = 19 expected, 14 shown, 5 unaccounted (Python). Resolution A: five further runs did not converge and were omitted without mention, which would fit "in many of these cases" (itself without a count); then the curve shown is selected by outcome, and the error and uncertainty values below JS 0.44 rest on four converged runs. Resolution B: points overlap; unlikely, because the gaps lie where a regular spacing of about 0.02 would put the missing runs. Resolution C: fewer than 20 runs were made. The figure instance AB recorded the same count as a verification without finding, reading the caption as disclosing the unstable cases; the merge checked the caption: it names only the most blended case, so the finding stands. The gap between JS 0.36 and 0.44, where the stated threshold of 0.44 lies, has no points. |
| Suggestion | Show all 20 cases in Figure 8, marking non-converged ones with a separate symbol; list the 20 JS values with their outcome in a table in Section 4.1.3, and replace "many of these cases" (l. 353) with the count. |
| Status | verified (count on the page image; caption wording); inferred (balance and resolutions) |
| Severity | moderate |
| Source | S3, SD |

**GB-43 The threshold "700 mm/yr" in l. 352 does not match Figure 8, whose absolute-error axis is a sum over pixels without unit and runs to 700000.**

| Field | Content |
|---|---|
| Check | P20, P3 |
| Location | p. 12, l. 351 to 353; Figure 8 (p. 29), left scatterplot; Figures 5g, 7, 9 and 10 (first column), y-axes |
| Quotation | "As the JS distance decreases below  0.55, both absolute error and posterior uncertainty rise sharply, with errors exceeding 700 mm/yr" |
| Concern | All figures plot the error as a sum of absolute pixel differences, so the quantity scales with the number of pixels, which is not given (GB-36); the text gives it a rate unit as if it were a per-pixel value. Measured markers on Figure 8: JS 0.249 at 47200 ± 1400, 0.272 at 676400, 0.338 at 5600, 0.359 at 321500; for JS 0.441 to 0.624 between 700 and 19400 (0.541 at 19400, 0.501 at 9000). Case 1, axis and text in the same unit: every point below JS 0.44 exceeds 700, the smallest by a factor of 8, but the point at JS 0.541 does too, so 0.44 is not a threshold. Case 2, the text means 700000: no point exceeds it (largest 676400 ± 1400). Case 3, the axis is in another unit; 700000 / 700 = 1000. The unblended point lies at about 700 ± 1400 on this axis, consistent with about 197 in Figure 5g. The unit is written "mm/yr" here and "mm/y" elsewhere (GB-11), and the line has a double space before "0.55" on the page image. |
| Suggestion | Define the error metric once in Section 3.3 or 4.1.1 (sum or mean over n pixels, with n), give the unit on the y-axes of Figures 5 and 7 to 10, correct l. 352 to 353 to a value and threshold that Figure 8 supports, write "mm/y" and remove the double space. |
| Status | verified (wording and axis labels on the page image; marker values measured); inferred (the three readings and ratios) |
| Severity | moderate |
| Source | S3, AB, S4 |

**GB-44 The x-axes of the left and middle scatterplots in Figure 9 are labelled "Avg. JS distance between lithologies" but show the number of tracers.**

| Field | Content |
|---|---|
| Check | P3 |
| Location | Figure 9 (p. 30), left and middle scatterplot |
| Quotation | "Avg. JS distance between lithologies" |
| Concern | The axes run from 0.0 to 20.0; the 21 markers sit at 1.0 to 21.0 and their colour follows the colour bar "Number of tracrs". The label is copied from Figure 8. The values support the text (l. 360 to 362): measured absolute difference 347.2 (1 tracer), 293.5 (3), 224.0 (5), 205.1 (6), 197.3 from 7 to 21 tracers. |
| Suggestion | Relabel both x-axes of Figure 9 as "Number of tracer minerals". |
| Status | verified (page image and measurement) |
| Severity | minor |
| Source | AB |

**GB-45 In the tracer-reduction scenario the data misfit is compared across runs with different numbers of tracers without normalisation, so its "drop" may only reflect fewer data terms.**

| Field | Content |
|---|---|
| Check | P21 |
| Location | p. 12, l. 360 to 362; Figure 9 (p. 30), right panel; p. 6, l. 182 (Eq. 7) |
| Quotation | "However, when the number of tracers drops below 7, the absolute error increases rapidly, as does the posterior uncertainty, while the data misfit and model misfit drop." |
| Concern | The data misfit (Eq. 7) is a sum over the m data. In Figure 9 the data misfit falls steadily as tracers are removed, also between 21 and 7 tracers, where the error stays at about 197: about 3.25 × 10⁶ at 21 tracers and 1.55 × 10⁶ at 11 tracers, per tracer 1.55 × 10⁵ and 1.41 × 10⁵, nearly equal (Python). The drop is therefore largely an effect of the number of summands and does not by itself indicate a better or worse fit. |
| Suggestion | Report the data misfit per datum (divided by m) in Figure 9 and at l. 360 to 362, or state that the absolute misfit is not comparable across tracer counts. |
| Status | verified (wording; point positions on the page image); inferred (per-tracer values) |
| Severity | moderate |
| Source | S3 |

**GB-46 The ranking of the three degradation factors compares effects of perturbations whose ranges are not commensurate and are chosen by the authors.**

| Field | Content |
|---|---|
| Check | P21, P10 |
| Location | p. 12, l. 363 to 365; p. 15, l. 456 to 461; Figures 7, 8 and 9 (p. 28 to 30) |
| Quotation | "To summarize, among the three tested scenarios, the strongest impact on the posterior solution arises from reduced fingerprint distinctiveness. Geological map uncertainty follows as the second most influential factor. In contrast, reducing the number of tracers has a comparatively limited effect" |
| Concern | The size of each effect depends on how far each perturbation was pushed: blending down to JS 0.225 (fully blended limit), map mismatch up to one alternative map (about 1.15 × 10⁷ m², three maps, GB-41), tracer removal down to a single tracer. One tracer raises the error from about 197 to 347 (+76 %), the Steck et al. map to about 275 (+40 %), blending to above 10⁵ (Python). With other ranges the order could change; a mismatch beyond one alternative map was not tested, and the blending results may carry the cap effect of GB-40 and the missing runs of GB-42. The scenarios share no normalised axis. Rated major because the ranking is carried into the Discussion (l. 456 to 461) and the recommendations. |
| Suggestion | Either express all three perturbations on a common scale (for example the JS distance of the resulting fingerprint set, or perturbation levels realistic for this catchment from replicate fingerprints, the two published maps and analytically achievable tracer counts) and compare at those levels, or restrict the ranking in l. 363 to 365 and l. 456 to 461 to a description of each effect within its tested range. |
| Status | verified (wording; tick labels on the page images); inferred (percentages and the dependence of the ranking on ranges) |
| Severity | major |
| Source | S3, SD |

**GB-47 The text in Figure 10 is set at about 5 pt and is hard to read at print size.**

| Field | Content |
|---|---|
| Check | P3 |
| Location | Figure 10 (p. 31), all panels |
| Quotation | "Smooting distance (m)" and "Max. number of non-linear iterations" |
| Concern | Word boxes from the PDF (vector text): 242 words in the figure have a box height of 4.8 to 4.9 pt (tick labels) and 62 words 5.6 to 5.7 pt (axis titles), against 10 pt in the caption. |
| Suggestion | Enlarge tick labels and axis titles of Figure 10, for example by splitting it into two figures or reducing the number of rows per page. |
| Status | verified (measured from the PDF word boxes) |
| Severity | minor |
| Source | AB |

**GB-48 The sweeps of the smoothing distance and of the data standard deviation are described against Figure 10, and the chosen hyperparameters are not the optimum of the own sweeps although the hyperparameters are said to be optimised.**

| Field | Content |
|---|---|
| Check | P21, P11, P3, P36 |
| Location | p. 12 to 13, l. 372 to 376; p. 13, l. 380 to 384; Figure 10 (p. 31), rows 1 and 3; p. 3, l. 70 (duplicate p. 5, l. 137); chosen L at p. 10, l. 294, p. 11, l. 325, p. 14, l. 427 |
| Quotation | "However, beyond approximately 10 times the pixel size (3000 m), the solution becomes overly smooth, causing the posterior to deviate from the true erosion rates." and "As data standard deviation increases, the absolute difference first decreases to a minimum, then rises to a plateau at higher values." and "Through forward-inverse testing, we optimize the hyper-parameters" |
| Concern | Row 1 (smoothing distance), measured: 20 markers from 199 ± 8 m to 3000 ± 8 m; the total absolute difference falls monotonically from 257.1 ± 0.7 to 76.0 ± 0.7 at 3000 m; at the marker nearest to L = 1200 m (1231 ± 8 m), the value used in all later tests, it is 194.9 ± 0.7. No run beyond 3000 m is plotted, so the stated deterioration beyond 3000 m is not shown, and by the own metric L = 3000 m lowers the error by 61 % (factor 2.6; Python: 194.9 / 76.0). The manuscript names the reason for the decrease, the prior equal to the mean true rate (l. 374 to 376, see GB-33), but does not draw the consequence that the sweep cannot select L under that prior. Row 3 (data standard deviation), measured with the axis offset "+1.974e2": the smallest σd values lie at 0.0198 ± 0.0001, rising to 0.0431 ± 0.0001 at σd = 0.89 mm/y, so the absolute difference spans 197.420 to 197.443, a change of 0.012 % (Python), lowest at the smallest σd, with no minimum and no plateau. The model misfit varies between 1.5614 and 1.5623 (0.06 %), which l. 384 calls a rapid decrease. For comparison, L changes the error by 70 %, the step size by about 40 % and σm by about 6 %. Three instances read the same values independently. Rated major because the stated sensitivity results and the claim of optimised hyperparameters do not hold for the figure, and all later tests use the unoptimised L. |
| Suggestion | Extend the L sweep beyond 3000 m or delete the sentence at l. 373 to 374; state in Section 4.1.4 the selection criterion for L = 1200 m, σm = 3 and σd = 0.01 mm/y; rewrite l. 380 to 384 to the monotonic and numerically negligible dependence on σd within 0 to 0.9 mm/y that Figure 10 shows, or add the runs the text refers to; remove the axis offset or give absolute values in the caption; replace "optimize" at l. 70 and l. 137 if no optimisation criterion is applied. |
| Status | verified (wording; values measured on page image p. 31); inferred (percentages and factor) |
| Severity | major |
| Source | S3, AB, SD |

**GB-49 The tracer list in the text names "Chrysolite", while Figures 11, 15 and 16 and the lithology description name "Chrysotile" in the same slot; the two names denote different minerals.**

| Field | Content |
|---|---|
| Check | P38, P2, P3 |
| Location | p. 13, l. 395; p. 10, l. 274; Figure 11 (p. 32), row label; Figures 15 and 16 (p. 36, 37), x-axis labels of the fingerprint panels |
| Quotation | "Dolomite, Diopside, Chrysolite, Antigorite" and "serpentinites (predominantly antigorite and chrysotile)" |
| Concern | The list at l. 394 to 396 and the labels of Figure 11 both contain 21 minerals, and Figure 15 the same 21 as Figure 11 (Python set comparison); the only difference between text and figures is Chrysolite against Chrysotile. The text list is in reverse alphabetical order and Figure 11 in alphabetical order, and both names occupy the same position, so they refer to one tracer. They are, however, two minerals: chrysotile is the serpentine mineral that l. 274 names as a main constituent of the serpentinites, whereas chrysolite denotes a yellowish green olivine, the group to which fayalite, also in the list, belongs (Minerals.net (n.d.) Chrysolite. Available at: https://minerals.net/variety/chrysolite, accessed 18 October 2026). Because the 2θ windows are selected per mineral from RRUFF reference spectra (l. 257) and are not tabulated (GB-23), the name decides which reference spectrum a reader would use to rebuild this tracer. As a spelling issue it would be minor; rated moderate for this reason. |
| Suggestion | Replace "Chrysolite" with "Chrysotile" at l. 395 if the serpentine mineral was used; if an olivine reference spectrum was used, correct Figures 11, 15, 16 and l. 274 accordingly; give the RRUFF identifier per mineral in the window table of GB-23. |
| Status | verified (both names on page images p. 10, 13, 32, 36, 37; definition of chrysolite in the source); inferred (that both names denote the same tracer, from count and position) |
| Severity | moderate |
| Source | S2, S3, AB, S4, SD |

**GB-50 Figure 11 shows identical fingerprints for several of the 21 minerals, so fewer than 21 distinct tracers are shown.**

| Field | Content |
|---|---|
| Check | P3 |
| Location | Figure 11 (p. 32), rows Annite, Phlogopite, Muscovite, Anorthite, Pyroxene, Ankerite, Dolomite; same pairs in Figures 15 and 16; p. 9, l. 259 to 260; p. 13, l. 393 to 398 |
| Quotation | "By extracting the relative peak areas within diagnostic 2θ windows for each of the 21 target minerals, we obtained the mineral concentrations characterizing each lithological unit (Figure 11)." |
| Concern | Bar lengths in px for the seven lithologies (ZSF serpentinites, ZSF sediments, STG, MR granite, ZSF metabasites, MR gneiss, Furgg): Annite and Phlogopite both 0, 131.3, 74.3, 137.3, 51.4, 160.5, 131.7; Muscovite the same except ZSF metabasites 42.4; Anorthite and Pyroxene both 0, 34.8, 243.3, 92.7, 243.1, 6.4, 103.7; Ankerite and Dolomite both 0, 4.3, 44.8, x, 34.1, 0, 6.1 with x = 6.7 and 4.0 for MR granite. Identity to 0.1 px in all seven lithologies for two pairs means these rows carry no independent information; the fingerprint has 18 distinct rows, two of which (Muscovite, Dolomite) differ in one lithology only. The text names peak overlap as a concern and states that averaging over windows mitigates it (l. 259 to 260). Question to the authors: were identical windows assigned to Annite and Phlogopite and to Anorthite and Pyroxene? |
| Suggestion | In Section 3.4 list the 2θ windows per mineral and state which minerals share windows; report the number of independent tracers used in Sections 4.2 and 4.2.2. |
| Status | verified (identical bar lengths measured); assumption (shared windows as the cause; posed as a question) |
| Severity | moderate |
| Source | AB |

**GB-51 The source fingerprints in Figures 15 and 16 are the fingerprints of Figure 11 rescaled per lithology by factors between 0.35 and 1.85, which differs from the normalisation stated in Section 3.4.**

| Field | Content |
|---|---|
| Check | P3 |
| Location | Figure 11 (p. 32); Figure 15 (p. 36), fingerprint panel; Figure 16 (p. 37), XRD part of the fingerprint panel; p. 9, l. 260 to 262 |
| Quotation | "At the end, these are normalized within each sample by dividing by the maximum observed peak area, yielding relative mineral concentrations on a scale from 0 to 1 (Figure 3D and 3E)." |
| Concern | Figure 11 follows the stated normalisation: in every lithology the longest bar measures 243.1 to 243.4 px (ZSF serpentinites 241.1 px). Figure 15 stacks, per mineral, the shares of the seven lithologies; if it showed the matrix of Figure 11, each share would be A(l,m) divided by the sum over l of A(l,m). Measured on 21 bars of 454 to 456 px: mean absolute deviation from that expectation 0.056, largest 0.214 (Chrysotile, ZSF serpentinites: expected 0.425, measured 0.640); 54 % of the 147 shares deviate by more than 0.03. Normalising by the sum per lithology does not explain it either (mean 0.041). A fitted factor per lithology reproduces Figure 15 to a mean deviation of 0.003 (largest 0.026): relative to ZSF sediments, ZSF serpentinites 1.71, STG 0.46, MR granite 1.30, ZSF metabasites 0.35, MR gneiss 1.85, Furgg 1.23. Figures 15 and 16 agree with each other (mean deviation 0.0014). The data are the same, but the scaling per lithology that enters A is not the one described; this bears on GB-13. Question to the authors: do the bars of Figure 15 use raw peak areas or a global maximum? |
| Suggestion | State in Section 3.4 which matrix A enters the inversion (normalised by the per-sample maximum as in Figure 11, or scaled otherwise as in Figure 15) and add the scaling to the captions of Figures 11 and 15. |
| Status | verified (bar lengths measured); inferred (factors from a least-squares fit); assumption (the cause; posed as a question) |
| Severity | moderate |
| Source | AB |

**GB-52 The natural known-mixture test has a single absent unit, no pass criterion and no sample count, and units present in the subcatchment show the same near-zero distribution as the absent one.**

| Field | Content |
|---|---|
| Check | P10, P31, P32, P3, P20 |
| Location | p. 13, l. 404 to p. 14, l. 418; p. 10, l. 299 to 300; Figure 12 (p. 33); Figure 13 (p. 34) with caption |
| Quotation | "If the XRD fingerprinting method is robust, the inversion should attribute erosion only to lithologies present within the sub-catchment." and "Merging the inversion results from multiple detrital samples collected at the sink of this sub-catchment shows that the predicted erosion rates for pixels within the Zermatt - Saas Fee unit (ZSF sediments) are close to zero (Figure 13)." and "the overall pattern confirms that the inversion respects geological boundaries when the XRD fingerprints provide sufficiently distinct signals" |
| Concern | The natural analogue of a known-mixture test is a good idea, and the ZSF sediments ridge does peak at zero. (1) Measured on the curves of Figure 13 (area under each ridge integrated column by column): ZSF sediments, median 0.11 mm/y, 77 % of the area below 0.25 mm/y, 85 % below 0.5 mm/y; Furgg series, which crops out inside the subcatchment (inset of Figure 13, Figure 12), median 0.09 mm/y, 77 % below 0.25 mm/y, 93 % below 0.5 mm/y. The absent unit is indistinguishable from a present one; Monte Rosa gneiss, which lies mostly outside the dashed outline, has the highest rates (median 0.56 mm/y). (2) Only one of seven units is absent, a small unit that the manuscript itself names as poorly resolved (l. 299 to 300). (3) Presence is defined by outcrops (Figure 12 caption), while A is built from the inferred map (l. 408); the dashed outline in the inset of Figure 13 encloses no area mapped as ZSF ophiolites (metabasites, eclogites), yet this unit receives erosion up to about 1.5 mm/y. (4) Because A depends only on lithology, the data cannot place erosion inside or outside the subcatchment within one unit; only the prior and the smoothing can. (5) The number and dates of the "multiple detrital samples", the number of inversions and of pixels per unit are not given, so the KDE heights and the caption's "a taller peak indicates greater consistency across inversions" cannot be interpreted (the KDE pools pixels and inversions); "close to zero" and "some spillover" are not quantified. Rated major because this test carries the second aim of the natural tests (l. 283 to 284) and the claim that the approach is reliable (l. 417 to 418). |
| Suggestion | In Section 4.2.1 give number and dates of the samples, number of inversions and pixels per unit; define a pass criterion beforehand, for example the fraction of posterior erosion (rate times area) on pixels outside the subcatchment boundary, and report it per sample; compare the ZSF sediments distribution with those of the units present, at least Furgg, and give the share of each unit's area inside the subcatchment in Figure 13; add a laboratory known-mixture series of source powders, the test the manuscript names as standard (l. 404 to 406). |
| Status | verified (wording; curve shares measured; absence of counts); inferred (location of Furgg and Monte Rosa gneiss relative to the subcatchment from the inset and Figure 12, items 3 and 4) |
| Severity | major |
| Source | AB, SD, S3 |

**GB-53 The comparison of zircon and XRD is confounded by the missing and imputed zircon fingerprints, which make two units indistinguishable for zircon only.**

| Field | Content |
|---|---|
| Check | P9, P27 |
| Location | p. 14, l. 420 to 422 and l. 430 to 436; p. 14 to 15, l. 439 to 442 |
| Quotation | "To compensate for the lack of age data for the MR g-g unit, we assigned the MR g-g unit the same zircon-age fingerprint as the Monte Rosa granite unit." and "Despite these adjustments, the resulting posterior solution is highly unstable" |
| Concern | With identical fingerprints the two Monte Rosa units form a perfect trade-off in the zircon data (equality of the segments confirmed by measurement, PP-25), and the ZSF metabasites have no zircon signal (l. 430 to 431). The XRD inversion has distinct fingerprints for all seven units. The instability attributed to the zircon method may come from this imputation rather than from zircon as a tracer, and the imputed values flow unchecked into the benchmark (0.87) and the combined result (0.86). Rated major because the benchmark is the basis of the stated advantage of XRD over zircon. |
| Suggestion | Counter-design for Section 4.2.2: compare both tracers on the same source partition, either by merging MR granite and MR g-g into one source in both inversions or by giving MR g-g the XRD fingerprint of MR granite as well, and report both results. |
| Status | verified (imputation stated at l. 433 to 434); inferred (confounding) |
| Severity | major |
| Source | SD |

**GB-54 It is unclear from which location the detrital sample of the zircon comparison was taken, and whether the XRD and zircon analyses used one sample or two.**

| Field | Content |
|---|---|
| Check | P2 |
| Location | p. 14, l. 420 to 421, l. 423 to 424, l. 437 to 438 and l. 439 to 440; Figures 14 to 16 (p. 35 to 37) |
| Quotation | "we compare it against a zircon-based fingerprinting approach applied to the same detrital sample" and "the detrital sample collected on June 28, 2019, at 13:30" and "the XRD-derived dataset acquired from a detrital sample taken at the same date and time" |
| Concern | l. 421 says "the same detrital sample", l. 437 to 438 "a detrital sample taken at the same date and time"; these are two different statements (one sample split, or two samples). "The same" also has no referent: the previous section used "multiple detrital samples" from the Gorner-Grenz confluence (l. 413). The sampling location of the 28 June 2019 sample is not stated anywhere in the manuscript. This matters for interpretation: if the sample came from the Gorner-Grenz confluence, the attribution of erosion to "the serpentinite-rich region in the southwest" (l. 440), outside that subcatchment, would contradict the result of Section 4.2.1; question to the authors: was the sample taken at the catchment outlet? |
| Suggestion | In Section 4.2.2 (l. 420 to 424) state the sampling site, whether one sample was split for zircon and XRD analysis or two samples were taken, and how this sample relates to the Gorner-Grenz samples of Section 4.2.1; if two samples, write at l. 420 to 421 "applied to a detrital sample collected at the same date and time (28 June 2019, 13:30)". |
| Status | verified (wording and absence of a location); assumption (the possible contradiction with Section 4.2.1; posed as a question) |
| Severity | moderate |
| Source | S3, SD |

**GB-55 The zircon method is documented only by an unpublished master's thesis.**

| Field | Content |
|---|---|
| Check | P8, P19 |
| Location | p. 14, l. 423 to 425; reference list p. 17, l. 522 to 523 |
| Quotation | "Zircon grains were extracted and U-Pb dated from both the source lithologies and the detrital sample collected on June 28, 2019, at 13:30, following the methodology described in (Belotti, 2021)." and "unpublished master’s thesis, 2021" |
| Concern | Grain extraction, analytical set-up, age binning (13 bins from 40 to 800 Ma in Figure 14, page image p. 35), number of grains per sample and treatment of discordant ages cannot be checked by the reader. Whether the zircon fertility of each unit enters A is not stated; question to the authors, because the serpentinites "contain only very low concentrations of zircons" (l. 432 to 433). |
| Suggestion | Summarise the zircon method in Section 4.2.2 or an appendix (instrument, grains per sample, bin definition, handling of fertility) and deposit the age data with the Zenodo record. |
| Status | verified (citation and wording); assumption (handling of fertility; posed as a question) |
| Severity | moderate |
| Source | SD |

**GB-56 Figures 14 and 16 show the imputed MR g-g zircon fingerprint without marking it as imputed.**

| Field | Content |
|---|---|
| Check | P37 |
| Location | Figure 14 (p. 35), bar chart and caption; Figure 16 (p. 37), zircon bins and caption; p. 14, l. 433 to 434 |
| Quotation | "Posterior erosion rate map using Zr fingerprint data, the resolution for the posterior, the normalized posterior uncertainty, the geological map and the source fingerprints." |
| Concern | On the page images the MR gneiss segments in the zircon bins have the same heights as the MR granite segments (measured within 2 px of 456 px, PP-25), consistent with the copied fingerprint; captions and legends do not say that this unit's fingerprint is imputed. |
| Suggestion | Mark the MR g-g segments as imputed (hatching or legend note) in Figures 14 and 16 and add the information to both captions. |
| Status | verified (caption wording; equality of segments measured) |
| Severity | moderate |
| Source | SD |

**GB-57 The three natural cases (zircon, XRD, combined) are compared with different metrics per case.**

| Field | Content |
|---|---|
| Check | P11 |
| Location | p. 14 to 15, l. 435 to 449 |
| Quotation | "low resolution, and a high total normalized uncertainty" and "the average Jensen-Shannon distance between source fingerprints increases from 0.48 to 0.57" |
| Concern | Matrix of metrics against cases: normalised uncertainty for all three; maximum erosion rate only for zircon in the text, for XRD and combined only via the colour bars (8.38 and 12.17 mm/y, measured); resolution only qualitatively for zircon ("low") and not at all for XRD and combined; JS distance for zircon and combined, missing for XRD only; data and model misfit for none. The comparison that the section sets out to make (l. 420 to 422) cannot be checked on equal terms; GB-59 shows that the missing XRD-only values affect the conclusion. |
| Suggestion | Add a table to Section 4.2.2 with one row per case and the same columns: maximum and median erosion rate, mean resolution diagonal, total normalised uncertainty, JS distance, data misfit, model misfit. |
| Status | verified (text; colour bar values measured) |
| Severity | moderate |
| Source | S3 |

**GB-58 The number of tracers in the combined inversion (34) and the number of zircon age bins (13) appear only in the figures.**

| Field | Content |
|---|---|
| Check | P22 |
| Location | p. 15, l. 443 to 445; p. 14, l. 425; Figure 14 (p. 35) and Figure 16 (p. 37), x-axes of the fingerprint panels |
| Quotation | "we combine both zircon and XRD data by concatenating the tracer concentration matrices A of the zircon and XRD approaches, as well as both corresponding detrital data vectors" |
| Concern | The reader must count the age bins in Figure 14 (13 contiguous bins from 40 to 800 Ma) and add the 21 minerals to obtain 34 tracers in the combined case (Python: 21 + 13). The relative weight of the two data sets in the misfit (13 against 21 data, same σd) is not discussed. |
| Suggestion | State at l. 425 the age bins used and at l. 443 to 445 the resulting number of tracers (21 + 13 = 34), and whether the two data sets are weighted equally. |
| Status | verified (bin labels on page image p. 35); inferred (counts) |
| Severity | minor |
| Source | S3 |

**GB-59 The claim that combining zircon and XRD further stabilises and improves the posterior is contradicted by the reported uncertainties against the XRD-only case, and stability and sharpness are not measured.**

| Field | Content |
|---|---|
| Check | P2, P15, P6, P31 |
| Location | p. 15, l. 446 to 449; p. 14, l. 437; p. 15, l. 441 to 442; p. 3, l. 72 to 73 (duplicate p. 5, l. 139 to 140); p. 10, l. 284 to 285; p. 15, l. 461 to 463; Figures 14 to 16 (p. 35 to 37), label "Total normalised posterior uncertainty" |
| Quotation | "Adding XRD data to the zircon dataset stabilizes the inversion and improves the posterior solution. The normalized posterior uncertainty decreases slightly to 0.86 (from 0.87 in the zircon-only case)" and "The normalized posterior uncertainty is slightly lower at 0.82." and "showing that integrating XRD with zircon data improves the stability and sharpness of the posterior solution" and "combining XRD data with other fingerprint data such as zircon data, proves to further stabilize and improve the posterior solution" |
| Concern | The three values in the text agree with the figure labels (0.87, 0.82, 0.86; PP-26), and Section 4.2.2 correctly states the direction "XRD added to zircon". The Introduction and the Discussion reverse it to zircon added to XRD ("further", l. 462). Against the XRD-only case, which the manuscript presents as its own method, the combination is worse: 0.86 minus 0.82 = +0.04, that is 4.9 % relative to 0.82, while the gain over zircon only is 0.01 (1.1 %) (Python). The second argument, the JS distance rising from 0.48 to 0.57, again starts from zircon only; the JS distance of the XRD-only fingerprints is not reported. "Stability" and "sharpness" are not defined or measured: one detrital sample, no repeated inversions, no perturbation of the data, no resolution summary, so it is unknown whether a difference of 0.01 exceeds run-to-run variation. The combined solution also has a higher peak (colour scale to 12.17 mm/y in Figure 16 against 8.38 mm/y in Figure 15). "Proves" is stronger than the evidence, and "further" contradicts the reported numbers. Rated major because the statement concerns the third aim of the natural tests (l. 284 to 285) and a conclusion of the Discussion. The sentence at l. 462 also lacks a comma pair around "such as zircon data". |
| Suggestion | Report all three cases with the same metrics in Section 4.2.2 (GB-57), state explicitly that the combined case is less certain than the XRD-only case by the total normalised uncertainty, define stability and sharpness in Section 3.3 (for example spread of posterior maps under resampling of detrital data or bootstrap of source fingerprints, and mean resolution) and report them for all three inversions; rewrite l. 72 to 73, l. 139 to 140, l. 284 to 285 and l. 461 to 463 to "adding XRD to zircon data", for example: "Adding XRD data to zircon data stabilised the inversion for one natural sample (0.86 against 0.87 for zircon alone), while the XRD-only inversion gave the lowest value (0.82)." Counter-design: repeat the three inversions on several detrital samples and report the distribution of the metrics. |
| Status | verified (values and wording in text and figure labels); inferred (differences and percentages) |
| Severity | major |
| Source | S3, S4, SD |

**GB-60 By the manuscript's own JS thresholds the zircon fingerprints lie in the unreliable range, and the JS distance of the XRD fingerprints, the method under test, is not reported.**

| Field | Content |
|---|---|
| Check | P5 |
| Location | p. 15, l. 447 to 448; p. 12, l. 351 to 353; Figure 8 (p. 29), unblended synthetic set at JS 0.624 |
| Quotation | "the average Jensen-Shannon distance between source fingerprints increases from 0.48 to 0.57" and "As the JS distance decreases below  0.55, both absolute error and posterior uncertainty rise sharply" |
| Concern | The rule from scenario 2 (error rises sharply below 0.55) applied to the own natural data: zircon at 0.48 lies below it, the combination at 0.57 just above. The XRD-only set is the subject of the manuscript, but its JS distance is not given, so the reader cannot judge whether the natural XRD inversion lies in the reliable range. Whether thresholds derived from synthetic fingerprints with 21 tracers transfer to 13 zircon age bins is not discussed, and the thresholds themselves may shift with the iteration cap (GB-40). Rated major because the natural XRD result cannot be placed against the manuscript's own reliability criterion. |
| Suggestion | Report the average JS distance of the XRD-only source set in Section 4.2 and Figure 11; in Section 4.2.2 relate all three values to the thresholds of Section 4.1.3 and discuss their transferability to other tracer sets. |
| Status | verified (values and wording) |
| Severity | major |
| Source | SD |

#### Minor corrections

| ID | Location | Quotation | Replacement | Source |
|---|---|---|---|---|
| KK-21 | p. 10, l. 299 to 300 | "Small lithological units (such as Zermatt Saas-Fee sediments and Furgg series (Figure 4) and Figure 5J) may be under-represented" | "Small lithological units (such as the Zermatt-Saas Fee sediments and the Furgg series; Figures 4 and 5j) may be under-represented" | S4, AB |
| KK-22 | p. 11, l. 307 | "the model’s "greedy" optimisation strategy" (straight quotation marks on the page image, curly ones elsewhere, for example at l. 288) | "the model’s “greedy” optimisation strategy" | S4 |
| KK-23 | p. 11, l. 333 to 334 | "the map proposed by (Steck et al., 2015) with the biggest area mismatch" | "the map proposed by Steck et al. (2015), which has the largest area mismatch" (for the label of the maps see GB-28) | S4 |
| KK-24 | Figure 7 (p. 28), title of the left map | "Originial geology (same as forward)" | "Original geology (same as forward)" | AB |
| KK-25 | p. 12, l. 341 | "closer to the centre of the true erosion-rate bump" | "closer to the centre of the true erosion-rate hotspot", as at l. 289 ("a localised hotspot") | S4 |
| KK-26 | p. 12, l. 343 to 344 | "by approaching each lithology’s mineral concentration to its mean across all lithologies" | "by moving each lithology’s mineral concentrations towards their mean across all lithologies" | S4 |
| KK-27 | p. 12, l. 345 | "which measures the similarity between two probability distributions" | "which measures the dissimilarity between two probability distributions"; l. 346 states that values near zero indicate similar signatures | S4 |
| KK-28 | Figure 8 caption (p. 29) | "first the most blended source signatures, then the half-way in between source signatures, and then the original synthetic fingerprints" | "first the most blended source signatures, then an intermediate blend, and then the original synthetic fingerprints" | S4 |
| KK-29 | p. 12, l. 351 | "The more resemblant the source fingerprints are" | "The more similar the source fingerprints are" | S4 |
| KK-30 | Figure 9 (p. 30), colour bar title | "Number of tracrs" | "Number of tracers" | S4, AB |
| KK-31 | p. 12, l. 370 | "the maximal amount of non-linear iterations" | "the maximum number of non-linear iterations" | S4 |
| KK-32 | Figure 10 (p. 31), first row, x-axis label | "Smooting distance (m)" | "Smoothing distance (m)" | S4 |
| KK-33 | p. 13, l. 384 | "approximately 10-2 mm/y" (no superscript on the page image, whereas l. 388 sets the exponent as superscript) | "approximately 10⁻² mm/y" | S3, S4 |
| KK-34 | Figure 11 caption (p. 32) | "Stockhorn-Turftgrat-Gornergrat" | "Stockhorn-Tuftgrat-Gornergrat", as at l. 276 and in Figure 13 | S2, S3, AB, S4 |
| KK-35 | Figure 11 caption (p. 32) | "ZSF ophiolites (metabasites, ecologites)" | "ZSF ophiolites (metabasites, eclogites)" | S2, S3, AB, S4 |
| KK-36 | p. 13, l. 400 | "supporting the 1) the robustness of the cleaning and binning approach" | "supporting 1) the robustness of the cleaning and binning approach" | S3, S4 |
| KK-37 | p. 13, l. 406; p. 14, l. 409, 411, 413; Figure 12 caption (p. 33); Figure 13 caption and inset (p. 34) | "Gorner-Grenzgletscher confluence" and "Gorner-Grenz subcatchment" and "contributing sub-catchment" | "Gorner-Grenz subcatchment" with a hyphen throughout (Figure 13 caption joins Gorner and Grenz with an en dash), and "subcatchment" without hyphen, as at l. 283, 284 and l. 411 | S2 |
| KK-38 | p. 14, l. 424 to 425 | "following the methodology described in (Belotti, 2021). Using the approach outlined in (De Doncker et al., 2020)" | "following the methodology described by Belotti (2021). Using the approach outlined by De Doncker et al. (2020)" | S4 |
| KK-39 | Figures 14, 15 and 16 (p. 35 to 37), legend below the erosion-rate map | "Low-con dence area" (the "fi" ligature is missing on the page image) | "Low-confidence area" | S4, AB |
| KK-40 | Figures 15 and 16 (p. 36, 37), legend, first entry | "ZSF serpentinites" (overlapped by the ZSF metabasites swatch in Figure 15, upper half of the line cut off in Figure 16) | "ZSF serpentinites", fully visible (move the second legend column or the legend box) | AB |
| KK-41 | Figure 15 (p. 36), y-axis of the fingerprint panel | "Normalised abundance per mineral or age" | "Normalised abundance per mineral" (Figure 15 contains no ages) | AB |

#### Verification log

| ID | Check | Checked | Values | Result |
|---|---|---|---|---|
| PP-11 | P1, P38 | Names, values and implied pixel size of the inversion hyperparameters across Sections 3, 4.1.1, 4.1.3, 4.1.4, 4.2.2 and Figure 10 | L = 1200 m = 4 pixel sizes (l. 294, 325, 427) and 3000 m = 10 pixel sizes (l. 373), both 300 m per pixel; σm = 3 (l. 294, 325, 427); σd = 0.01 mm/y (l. 295, 325, 428); µ = 0.1 (l. 326, 385, 428); iterations 100 (l. 293) and 25 (l. 324, 426), differing by design; symbols L, σm, σd, µ in Figure 10 match Eq. 8, 9 and 17 | consistent; nm in Figure 10 in GB-14, highlighted values in GB-31 |
| PP-12 | P3 | Figure 5f against Eq. 22 with σm = 3 | colour bar e: 0.984 ± 0.027 to 8.842 ± 0.027; colour bar f: 0.332 ± 0.002 to 0.988 ± 0.002; expected sqrt(0.984 / 9) = 0.331 and sqrt(8.842 / 9) = 0.991, assuming both colour bars span the data range | consistent; no finding |
| PP-13 | P3 | Figure 5 panels g, h, i against l. 305 to 308 | 5g: 348.5 ± 0.5 at iteration 1, minimum 197.3 ± 0.5 at iterations 20 to 23, 201.0 ± 0.5 at iteration 100 (rise of 3.7, 1.9 %, not raised); 5h: 0.7330 at iteration 1, 0.7409 at 25, 0.7426 at 100, rising and levelling off as stated; 5i: early iterations at high data misfit and low model misfit, late iterations the reverse, as described | no finding |
| PP-14 | P30 | Reported errors and the order of their correction relative to reported runs | one reported error (steepest descent instability, l. 312); the reported steepest descent run (Figure 6) already uses the corrected, normalised gradient (l. 312 to 316); no run before the correction is reported as a result | no finding; the undescribed corrected update is part of GB-21 |
| PP-15 | P11 | Coverage of announced tests by reported results | three degradation scenarios announced (l. 323), each reported (l. 327 to 342, Figure 7; l. 343 to 354, Figure 8; l. 355 to 362, Figure 9); five hyperparameters announced (l. 367 to 370), each reported (l. 372 to 389) and shown in the five rows of Figure 10; three aims of the natural tests (l. 282 to 285) addressed at l. 399 to 401, Section 4.2.1 and Section 4.2.2 | complete; cells with incomplete content in GB-15, GB-37, GB-48, GB-57 |
| PP-16 | P2, P3 | Values of the common baseline run (QN, 25 iterations, L = 1200 m, σm = 3, σd = 0.01 mm/y, µ = 0.1, original fingerprints and map) across Figures 5, 7, 8, 9 and 10 | absolute error 197.6 ± 0.5 at iteration 25 in Figure 5g; 197.5 ± 0.3 in Figure 7 (original geology); 197.3 in Figure 9 (21 tracers); 197.6 ± 0.3 in Figure 10, row 5 (25 iterations); near 0 on the 7 × 10⁵ axis for "Unblended" in Figure 8; normalised uncertainty 0.7402 to 0.7409 in Figures 5h, 7, 8; data misfit about 3.25 × 10⁶ in Figures 7 and 9 | consistent; no finding |
| PP-17 | P3 | Figure 7 against l. 337 to 342 | original geology: area difference 0.00 × 10⁷ m², error 197.5, trace 0.7402, data misfit 3.254 × 10⁶, model misfit 1.561; minimal changes: 0.69 × 10⁷ m², 193.5, 0.7376, 3.490 × 10⁶, 1.922; Steck et al. 2015: 1.14 × 10⁷ m², 274.7, 0.7460, 3.687 × 10⁶, 2.463; lower error for the minimal-change map confirmed and disclosed ("Surprisingly", l. 338); misfits increase with mismatch as stated | no finding beyond GB-41 |
| PP-18 | P23, P34, P3 | Balance of runs in scenarios 1 and 3 and counts in Figures 7, 9 and 10 | scenario 1: three maps announced (l. 332 to 334), three points in each panel of Figure 7; scenario 3: tracer counts 1 to 21 announced (l. 358), 21 points at 1.0 to 21.0 in the left and middle panels of Figure 9; Figure 10: no number of tested values stated per sweep, so no comparison possible | balanced; scenario 2 in GB-42 |
| PP-19 | P3 | Figure 8: count and labelled examples | 14 markers in each scatterplot (counted at 2x zoom); labelled examples "Medium" at JS 0.441 and "Unblended" at 0.624, matching the panel titles; posterior uncertainty 0.7403 at JS 0.624, 0.7471 at 0.561, 0.8419 at 0.541, 0.8324 at 0.441, the jump between 0.56 and 0.54 confirming "below 0.55" for the uncertainty | count used in GB-42; absolute error values in GB-43 |
| PP-20 | P2, P36 | Stated optimum step size, minimum iterations and 7-tracer statement against Figures 9 and 10 | Figure 10 row 4: 10 values from 0.010 to 0.316; 203.8 at 0.068, 197.5 at 0.100, 199.0 at 0.147, 201.3 at 0.316, minimum at 0.1 as stated (l. 385); row 5: 20 values from 5 to 195 iterations; 268.7 at 5, 200.9 at 15, 197.6 at 25, 201.0 from 55 on; "below 25 ... fail to converge" (l. 387) supported clearly only by the run with 5 iterations (one point affected, not raised); Figure 9: about 197 from 7 to 21 tracers, consistent with l. 360 | no finding |
| PP-21 | P38, P2 | Names and number of tracer minerals in text and Figures 11, 15, 16, and of the synthetic tracers | text 21 names, 21 distinct, "21 minerals" (l. 393) and "21 target minerals" (l. 397 to 398); Figure 11, 15: 21 labels, identical sets; Figure 16: the same 21 plus 13 zircon age bins; synthetic tracers labelled A to U in Figure 5k (21), matching "between 1 and 21 tracers" (l. 358) and "All tracers (21)" (Figure 9); 7 units in the caption of Figure 11, the legends of Figures 15 and 16 and l. 273 to 278 | consistent except Chrysolite and Chrysotile (GB-49) |
| PP-22 | P3 | Figure 11 normalisation against l. 261 | longest bar per lithology 243.1 to 243.4 px, ZSF serpentinites 241.1 px (Antigorite); each lithology scaled to its maximum as stated | consistent; identical rows in GB-50 |
| PP-23 | P3 | Figure 12 against l. 410 to 412 | in the saturated north-east area (subcatchment): Stockhorn with outcrops, Furgg series, a serpentinite band inside the Furgg strip, small metabasite outcrop streaks, Monte Rosa granite with outcrops and Monte Rosa gneiss outcrops at the east margin; no ZSF sediment colour; map without grid, so inferred | consistent with caption and l. 411 to 412; no finding |
| PP-24 | P24 | Events and dates in figures | no figure has a time axis or dated markers; the only date (28 June 2019, 13:30, l. 423 to 424 and l. 438 to 439) appears in no figure or caption | no P24 finding; caption gap in GB-31 |
| PP-25 | P2, P3 | Zircon age bins and imputed fingerprint in Figures 14 and 16 | 13 contiguous bins: 40 to 140, 140 to 200, 200 to 210, 210 to 250, 250 to 263, 263 to 270, 270 to 340, 340 to 430, 430 to 475, 475 to 555, 555 to 585, 585 to 750, 750 to 800 Ma, identical in both figures; MR gneiss and MR granite shares agree within 2 px of 456 px in every bin (for example 228 and 228 px for 140 to 200 Ma), confirming l. 433 to 434; no ZSF metabasite segment; zircon part of Figure 16 equals Figure 14 (mean deviation 0.0008), XRD part equals Figure 15 (0.0014) | consistent; marking of the imputation in GB-56 |
| PP-26 | P2, P3 | Total normalised posterior uncertainty and colour bar maxima of the three natural cases, text against figures | zircon 0.87 (l. 437; Figure 14), XRD 0.82 (l. 442; Figure 15), combined 0.86 (l. 447; Figure 16); colour bar maxima 8622 ± 29 mm/y (Figure 14, consistent with "above 8000 mm/y" at l. 435), 8.38 ± 0.03 mm/y (Figure 15), 12.17 ± 0.04 mm/y (Figure 16); JS 0.48 and 0.57 (l. 448) only in the text | all agree; interpretation in GB-59 |
| PP-27 | P1 | Arithmetic and direction of the stated changes in Section 4.2.2 | 0.87 to 0.82: −0.05 (−5.7 %), called "slightly lower"; 0.87 to 0.86: −0.01 (−1.1 %), called "decreases slightly"; JS 0.48 to 0.57: +0.09, called "increases" | correct relative to the zircon case; comparison with XRD only in GB-59 |

### Segment 4: Discussion, Conclusions, statements, references (p. 15 to 21)

#### Substantive findings

**GB-61 The Discussion states that a broad set of tracer minerals improves stability and resolution, whereas the tracer-reduction test found no gain above 7 tracers and did not assess resolution.**

| Field | Content |
|---|---|
| Check | P15 |
| Location | p. 15, l. 457 to 458; p. 12, l. 355 to 365; Figure 9 (p. 30) |
| Quotation | "Including a broad set of tracer minerals further improves model stability and resolution." |
| Concern | The manuscript's own result is: "The inversion with 7 tracers results in approximately the same posterior solution as with the full tracer set" (l. 360), and reducing the number of tracers "has a comparatively limited effect" provided that the most informative ones are retained (l. 364 to 365). Figure 9 shows absolute error and posterior uncertainty levelling off from about 7 tracers onward (197.3 from 7 to 21 tracers, GB-44). 7 of 21 tracers are 33.3 % of the set (Python). The results therefore support "a minimum of about 7 informative tracers is needed", not "a broad set further improves". Resolution (the diagonal of R, Section 3.3) is not reported for this scenario at all. The statement is stronger than its evidence and partly opposite in direction, hence major. |
| Suggestion | Rephrase l. 457 to 458 in line with l. 360 to 365, for example: "A minimum number of informative tracer minerals (here about 7 of 21, selected by PCA) is required; beyond this number, adding tracers did not change the posterior solution noticeably." Drop "resolution" or add the resolution metric to the results of scenario 3. |
| Status | verified (text l. 355 to 365 and l. 457 to 458; Figure 9 on page image p. 30); inferred (the 33.3 % share) |
| Severity | major |
| Source | S4 |

**GB-62 The number of source areas and the degree of sediment storage are presented as findings of the study, but neither was varied in any test.**

| Field | Content |
|---|---|
| Check | P15 |
| Location | p. 15, l. 460 to 461; p. 15, l. 466 to 468; p. 16, l. 484 to 486; p. 10, l. 299 to 300; p. 11 to 12, l. 327 to 342 |
| Quotation | "A higher number of distinct source areas leads to higher posterior resolution and lower uncertainty." and "Our results suggest that the method is best applied in catchments with minimal sediment storage, multiple mineralogically distinct source areas, and good prior knowledge of the spatial distribution of source areas." |
| Concern | Three conditions are attributed to "our results". Two have a location in the Results: mineralogical distinctness (scenario 2, l. 343 to 354) and spatial knowledge of source areas (scenario 1, l. 327 to 342). (1) No test varies the number of source areas; all synthetic tests use the same seven-unit map, and scenario 1 changes unit boundaries, not their number. The only related result points the other way: small units "may be under-represented in the mixing process, making their signals harder to distinguish, leading to lower resolution" (l. 299 to 300), so more but smaller units would not necessarily raise resolution. (2) Sediment storage is not tested; it is excluded by the model assumption (l. 23; l. 467 to 468, "assumes immediate sediment export"). The Discussion presents this correctly as a caution following from the model; the Conclusions present it as a result. Its consequence for the study site is treated in GB-12. Rated major because the Conclusions state these conditions as findings. |
| Suggestion | At l. 460 to 461 delete the sentence or present it as a hypothesis for future tests, and add a synthetic test with a varied number of units if the claim is to be kept; at l. 484 to 486 separate result from assumption, for example: "Our results show that the method requires mineralogically distinct source areas and an accurate map of their spatial distribution; by construction, it also assumes minimal sediment storage." |
| Status | verified (absence of a test with a varied number of units and of a storage test in Sections 4.1 and 4.2; quoted lines) |
| Severity | major |
| Source | S4 |

**GB-63 The Conclusions recommend applying the method to zircon U-Pb age data and to land-use maps, although the zircon-only inversion failed in the Results and land use was never tested.**

| Field | Content |
|---|---|
| Check | P15 |
| Location | p. 16, l. 487 to 489; p. 15, l. 466; p. 14, l. 435 to 437 |
| Quotation | "Similarly, the method is not limited to XRD-derived fingerprints and can be applied to other types of tracer data, including zircon U-Pb age distributions or geochemical compositions." and "Other types of source area maps, such as those based on land use, can also be incorporated." |
| Concern | The only zircon-only application in the manuscript gave a posterior that "is highly unstable", with extreme erosion rate values above 8000 mm/y, low resolution and a high total normalised uncertainty of 0.87 (l. 435 to 437). Recommending zircon U-Pb data as a tracer without qualification therefore runs against the manuscript's own finding, although the confounding by the imputed fingerprint (GB-53) may explain part of that failure. Land-use maps and geochemical data are not used in any test. The flexibility of the forward model (Eq. 1 to 4) makes these extensions possible in principle, but the Conclusions present them as established. Rated major because a conclusion is stated against the reported result. |
| Suggestion | Qualify l. 487 to 489, for example: "In principle the formulation accepts other tracers and other source-area classifications; in our test, zircon U-Pb ages alone did not give a stable solution (Section 4.2.2), and land-use classes and geochemical tracers remain to be tested." Move the land-use sentence at l. 466 to an outlook phrased the same way. |
| Status | verified (quoted lines) |
| Severity | major |
| Source | S4 |

**GB-64 The Code and data availability statement covers only "the inversion tests" and says nothing about six classes of data sources that the Methods and Validation sections name.**

| Field | Content |
|---|---|
| Check | P12 |
| Location | p. 16, l. 490; data sources at p. 9, l. 251 to 258 and l. 267 to 268; p. 13, l. 391 to 398; p. 13, l. 406 to p. 14, l. 413; p. 14, l. 423 to 425 and l. 438 to 439; p. 15, l. 452 to 454; reference list p. 17, l. 522 to 523; Figure 3 (p. 24), panels a to e |
| Quotation | "The data and codes used for the inversion tests in the study are available at https://doi.org/10.5281/zenodo.17120374" |
| Concern | The manuscript gives a persistent DOI for code and data, which is the right vehicle. The statement, however, is limited to "the inversion tests", and it is not said whether this includes the natural data tests of Section 4.2 or only the synthetic tests of Section 4.1. None of the following is mentioned as published, available on request, or withheld with a reason: (a) raw XRD diffractograms of the source rock samples, "one diffractogram per sample" (l. 252); (b) XRD diffractograms of the detrital samples, the "multiple detrital samples" of the Gorner-Grenz confluence (l. 406, 413) and the sample of 28 June 2019 (l. 423 to 424, 438 to 439); (c) processing parameters of the fingerprints: peak-finder thresholds, the quartz reference pattern and the 21 diagnostic 2θ windows (l. 254 to 258), which are not tabulated (GB-23); (d) zircon U-Pb ages of sources and detrital sample, obtained "following the methodology described in (Belotti, 2021)" (l. 424), an "unpublished master’s thesis" (l. 522 to 523); (e) the "multi-year suspended sediment datasets" (l. 268) and the export estimate required as input (l. 452 to 454, GB-15); (f) sample metadata: source sample locations per lithology (shown only schematically in Figure 3b) and detrital sampling sites, dates and times. All six concern rock and sediment samples, not persons, so no privacy reason for withholding applies, and the manuscript has no appendix or supplement. The DOI could not be resolved (HTTP 429), so the content of the record is unknown to this review. The spatial inputs are treated in GB-27. |
| Suggestion | Extend the statement at l. 490 to list each data class (a) to (f) with its location (file names in the Zenodo record or another repository), say whether "inversion tests" includes Section 4.2, and state where the zircon ages are published, since the cited thesis is unpublished. |
| Status | verified (wording and scope of the statement on page image p. 16; absence of any mention of (a) to (f)); inferred (that the zircon ages are not accessible elsewhere); content of the record not checked |
| Severity | moderate |
| Source | S2 |

**GB-65 Several reference entries are incomplete or carry leftover fields from a reference manager.**

| Field | Content |
|---|---|
| Check | P16 |
| Location | reference list p. 17 to 20, l. 521, 522 to 523, 567 to 568, 578 to 579, 583, 599 to 600, 612 to 613, 634 to 635 |
| Quotation | "Gergel, S. E., Turner, M. G., Miller, J. R., Melack, J. M., and Stanley, E. H.: [No title found], Aquatic Sciences, 64" and "Gjems, O.: Studies on clay minerals and clay-mineral formation in soil profiles in Scandinavia, 1967." and "Bearth, P.: Blatt 535 Zermatt - Geologischer Atlas der Schweiz 1:25 000, 1953." and "Master’s thesis, University of Lausanne, unpublished master’s thesis, 2021." and "Oxford University Press, New-York" and "ISBN 9780898715729 9780898717921" |
| Concern | Most entries follow one pattern (authors, title, venue, volume, pages, DOI, year). The listed entries deviate: one has a placeholder instead of a title; the Gjems, Bearth and Lafuente et al. entries lack publisher or series and editors; the Belotti entry repeats "master's thesis"; the E. entry (GB-04) contains an export field ("oCLC: 1402659188") and the publisher repeated with the year; the Moore and Reynolds book entry gives a page range as if for an article and a hyphenated "New-York"; the Tarantola entry gives two ISBNs. The missing Gergel title is "Landscape indicators of human impacts to riverine systems" (Aquatic Sciences 64(2), 118 to 128, 2002, doi:10.1007/s00027-002-8060-2), verified on the publication record of the University of Illinois. |
| Suggestion | Insert the Gergel title; add publisher and place for Gjems (1967) and Bearth (1953, Schweizerische Geologische Kommission); add editors and publisher for Lafuente et al. (2015); write "unpublished MSc thesis, University of Lausanne" once for Belotti; delete "oCLC: 1402659188"; write "New York" and drop or explain the page range for Moore and Reynolds; keep one ISBN for Tarantola. |
| Status | verified (page images p. 17 to 20; Gergel title in the publication record) |
| Severity | minor |
| Source | S4 |

#### Minor corrections

| ID | Location | Quotation | Replacement | Source |
|---|---|---|---|---|
| KK-42 | p. 16, l. 490 | "The data and codes used for the inversion tests in the study are available at https://doi.org/10.5281/zenodo.17120374" (the URL runs into the right margin on the page image and the sentence has no full stop) | "The data and codes used for the inversion tests in this study are available at https://doi.org/10.5281/zenodo.17120374.", with a permitted line break in the URL (for the scope see GB-64) | S4 |
| KK-43 | p. 16, l. 491 to 494 | "All authors (FDD, FH, BB, TA) contributed" | "All authors (F.D.D., F.H., B.B., T.A.) contributed", as in the following sentences | S4 |
| KK-44 | p. 20, l. 639 | "Bomb-fallout137 Cs as a marker" (superscript attached to "fallout", space before "Cs" on the page image) | "Bomb-fallout ¹³⁷Cs as a marker" | S4 |

#### Verification log

| ID | Check | Checked | Values | Result |
|---|---|---|---|---|
| PP-28 | P15 | Each statement of Discussion and Conclusions mapped to a location in the Results; recommendations against the central findings; strength of the verbs | with a result location: distinct source signatures essential (l. 457 to 458; results l. 351 to 354, 363 to 364); accurate spatial delineation crucial (l. 459 to 460; l. 337 to 342); recommendations a) and b) (l. 464 to 465; scenarios 1 and 2); resolution and posterior covariance as reliability measures (l. 483 to 484; l. 299 to 304, Figures 14 to 16); method description (l. 478 to 481; Section 3); storage caution (l. 466 to 468) framed as model assumption with reference; XRD limitations (l. 469 to 476) worded with "may", "can be diminished", "should help", matching the absence of own tests; without or against a result location: GB-59, GB-61 to GB-63 | findings GB-59, GB-61, GB-62, GB-63 |
| PP-29 | P9 | Announced future studies and their designs | Discussion and Conclusions name possible extensions (land use, subcatchments, other tracers, l. 466, l. 487 to 489) but announce no specific study with a measurement design | no finding; the wording of the extensions in GB-63 |
| PP-30 | P12 | Code and data availability statement against all data sources named in Sections 3, 4 and Figures 3, 4, 7, 14; link; appendices | one sentence, one DOI (10.5281/zenodo.17120374), scope "data and codes used for the inversion tests"; inversion code covered; synthetic fingerprints and true map of Section 4.1 covered if "inversion tests" means Section 4.1; classes (a) to (f) of GB-64 and spatial inputs of GB-27 not mentioned; appendices or supplements: none; DOI request refused by the network proxy (HTTP 429), web search returned no record page | findings GB-27 and GB-64 |
| PP-31 | P4 | In-text citations against the reference list in both directions; years, spelling of names, "et al." for more than two authors | 64 distinct short citations and 64 reference entries; every citation has an entry and every entry is cited; 11 two-author citations match two-author entries; 12 single-author citations match; 41 "et al." citations match entries with three or more authors; all years agree; most cited: Das et al. 2023 (8), Butler et al. 2019 (7), Yang et al. 2025 (7), counts including the duplicated Introduction; only deviation the name "E." | finding GB-04; DOIs not resolved (optional check) |
| PP-32 | P4, P29, P3 | Numbering of sections, figures, equations, tables and appendices; existence of every target; figure inventory | Sections 1, 2, 3 (3.1 to 3.4), 4 (4.1.1 to 4.1.4, 4.2.1 to 4.2.2), 5, 6 consecutive, Section 2 duplicating Section 1 (GB-03); Figures 1 to 16 consecutive, each cited, first citations in ascending order (l. 146, 166, 251, 268, 289, 314, 334, 347, 356, 371, 398, 412, 414, 429, 439, 445); Equations 1 to 22 consecutive, references "eq. 1-4" (l. 263), "eq. 7" (l. 191, 240, 245), "eq. 10" to "15" (l. 200, 204), "eq. 16" (l. 213, 217) point to equations with the described content; no tables, no appendices, no graphical abstract; Figures 5 and 6 raster images of about 226 ppi, Figures 7 and 14 to 16 contain raster images of 690 to 1240 ppi, Figures 10 and 11 vector graphics | no finding beyond GB-03 |
| PP-33 | P16 | Grammar, word choice, characters and typesetting on the page images of all text pages (p. 1 to 21) and of the figure pages 24, 25, 27, 29 to 32, 35 to 37 | 3 findings on form (GB-11, GB-26 in part, GB-65) and the minor corrections of this report; not raised because they appear only in the extracted text: the "fl" ligature in Figures 1 and 2, broken equation fragments (l. 154 to 244), "c Author(s)" in the header, fragments of rotated labels in Figures 1 to 3; the em dashes at l. 145, 365 and 576 are standard English punctuation | no further finding |

## Optional checks

| Area | What it needs | Responsible | Run |
|---|---|---|---|
| DOI resolution | one request per reference entry with DOI | `science-quellenapparat-pruefung` | no |
| Citation style | the name of the style | `science-zitierstil-harvard-ctr` or the style rules of the journal | no |
| AI statement against publisher policy | the AI policy of the target publisher | this review, on request | no |
| Relation to the authors' own prior work | the authors' prior publications | this review, on request | no |
| Journal requirements | the author guidelines of the target journal | this review, on request | no |
| Subject-matter accuracy | access to the sources of each checked statement | `science-faktenbeleg-pruefung`, `geo-frage-belegbasiert-klaeren` | no |

## Limits of this review

- Version checked: egusphere-2025-4695.pdf, 37 pages, SHA-256 9c80676054f96ecd6f00f4d2a8b5ba568e03c6949e3856d363ac1c4abb42e7bd.
- Review mode: the six review instances (S1 to S4, AB, SD) ran as separate agents without context from one another; the merge, the overall assessment and the format check were done by a seventh agent (ZF), which re-checked quotations against the manuscript text, decided contradictions at the page images and verified the two findings adopted from hints (GB-16 and GB-18) at the page images.
- Unreadable sources: full text of Das et al. (2023), Water Resources Research (publisher error); full texts of Niu et al. (2020), Das et al. (2024) and De Doncker et al. (2020) (abstracts only); Yang et al. (2025) (not found in open sources); the Zenodo record 10.5281/zenodo.17120374 (HTTP 429, content not checked); the title page of the UNESCO report cited as "E., 2009" (rate-limited). Findings that depend on abstracts are marked as such.
- Findings with status assumption: 0 of 65 for the central statement; 14 of 65 contain a partial statement with status assumption, each posed as a question to the authors.
- Optional checks run: 0 of 6.
- Discarded findings: 0. All 85 substantive findings of the six instances had every mandatory field; one contradiction between an instance finding and a verification log without finding (Figure 8, GB-42) was decided at the manuscript in favour of the finding.
- Merged items: 85 instance findings plus 2 findings adopted from hints gave 65 findings (22 merged); 83 instance minor corrections gave 44 (15 absorbed into findings, 24 merged with other corrections); 43 verification logs gave 33 (10 merged).
- Hints outside the checklists: 68 from the six instances; 2 adopted as findings with source ZF (GB-16, GB-18); all others were already treated by a responsible instance or not confirmed. Among those not adopted: the support of "sediment traps installed on dams" by Wilson et al. (1993), whose content was not read.
- Values from figures were measured at 300 dpi by the figure instance; values that other instances read from tick labels are marked as read, not measured. Line numbers of the extracted text can be shifted at page ends, equations and figure pages; all line numbers in this report follow the printed margin numbers.
