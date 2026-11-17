# Review report: From XRD signal to erosion rate maps

| Field | Value |
|---|---|
| Manuscript | De Doncker, F., Herman, F., Belotti, B. and Adatte, T. (2025) From XRD signal to erosion rate maps, EGUsphere preprint, https://doi.org/10.5194/egusphere-2025-4695 |
| Checked version | egusphere-2025-4695.pdf, 37 pages, SHA-256 9c80676054f96ecd6f00f4d2a8b5ba568e03c6949e3856d363ac1c4abb42e7bd |
| Date | 2026-10-17 |
| Language | English |
| Review instances | Segments 1 to 4, figures, study design |
| Note | The six review instances ran as separate agents, each without context from the others; this report merges their results and rechecks wording and locations against the manuscript. Line numbers follow the printed margin numbers; pages 22 to 37 carry none, so figures are located by page and panel. Where the duplicated introduction (GB-04) repeats a passage, the first occurrence is cited and the repeat is given in brackets. |

## Summary

The manuscript is a method development study. It builds a log-parameterised least-squares inversion that converts binned X-ray diffraction (XRD) peak areas of source lithologies and of suspended sediment into spatially explicit erosion rate maps, with posterior covariance, resolution and a normalised posterior uncertainty as reliability metrics. Steepest descent and quasi-Newton schemes are compared on synthetic data generated with the same forward model from a "true" map with one hotspot. Three degradation scenarios follow (geological map mismatch with three maps, fingerprint blending over 20 levels down to an average Jensen-Shannon distance of 0.225, and 1 to 21 tracers), together with sweeps of five hyperparameters. The natural case is the Gornergletscher catchment with 7 source units and 21 tracer minerals. It is tested in three ways: plausibility of the source fingerprints, a natural known-mixture analogue at the Gorner-Grenz confluence, and a comparison with zircon U-Pb fingerprints for one detrital sample of 28 June 2019. Key settings are a pixel size of 300 m, L = 1200 m, σm = 3, σd = 0.01 mm/y and 25 or 100 iterations. The total normalised posterior uncertainty is 0.87 (zircon), 0.82 (XRD) and 0.86 (combined), and the average Jensen-Shannon distance is 0.48 (zircon) and 0.57 (combined).

## Strengths

1. The synthetic design pairs a known truth with three diagnostics (summed error, normalised uncertainty, misfit trade-off) and applies them to both schemes, three degradation scenarios and five sweeps. This makes failure thresholds visible to the reader. Where text and figures can be compared they mostly agree: the tracer test matches Fig. 9 (PP-21), run counts match plotted points in scenarios 1 and 3 (PP-14), baseline values agree across Figs. 7 to 10 (PP-18) and settings are stated identically in all places (PP-13). The scope is limited to one synthetic truth (GB-24).
2. The manuscript discloses its own failures and limits. These include the unstable steepest descent scheme and its correction before the reported run (PP-15, PP-16), the missing zircon data and the substituted fingerprint, which Fig. 14 reproduces to the pixel (PP-29), the inferred geology under ice, and the storage and XRD limitations (PP-04, PP-31). A reader can therefore locate the limits, although their consequences are not always drawn (GB-10, GB-57).
3. The natural known-mixture analogue leaves the tracer matrix unrestricted, and the zircon comparison uses a sample taken at the same date and time. The reported numbers are carried consistently between text and figure annotations (PP-30), the unit balance of the known-mixture test closes (PP-26) and the map scales agree between figures (PP-09). This gives the natural tests a checkable numerical basis, although they do not measure accuracy (GB-44, GB-53).
4. Code and data are archived under a DOI that resolves to an open-licence record (PP-33). Every in-text citation has a reference entry, and figures, panels and equations are numbered and cited in order (PP-35, PP-05). A reader can find the archive and follow the internal references; what the archive contains is not stated in the manuscript (GB-58).

## Weaknesses

1. The summary statements claim more than the results show. The Abstract and Conclusions report consistent convergence and robustness without the failure domain (GB-02). The natural tests are said to "validate" the method (GB-03), a cost and time advantage is claimed without any measure (GB-01), the combined zircon and XRD run is said to improve on XRD although its uncertainty is higher (GB-53), and two effects stated in the Discussion have no test (GB-55). The novelty claim also overlaps with the authors' earlier inversion framework and calls a linear mixture non-linear (GB-54). Suggestion: state each claim with the tested conditions and numbers, reserve "validate" for the synthetic tests, and either measure the cost claim or present it as motivation.
2. Assumptions the method rests on are untested. Normalising each diffractogram by its own maximum breaks the additivity that the linear mixing equation needs (GB-19). Data uncertainty is assumed and fingerprint variability is not propagated (GB-14). The synthetic tests use one noise-free truth and a prior equal to the true mean (GB-24). Several of the 21 XRD tracers are numerically identical in the natural fingerprints (GB-42). Suggestion: run laboratory mixtures of the source powders through the full pipeline, add noise and an ensemble of truths, derive σd from replicates, and merge identical tracers.
3. The natural-data tests check plausibility, not accuracy. The known-mixture analogue cannot separate the one absent unit from present ones and does not evaluate where the erosion is placed (GB-44). The agreement of the fingerprints with the lithology is asserted without a criterion (GB-43). The zircon benchmark has an unstated treatment of one unit (GB-48), rests on one instantaneous sample scaled by an annual export (GB-46), and the export estimate and prior used for all natural runs are not reported (GB-13). Suggestion: report the share of posterior erosion inside and outside the subcatchment, tabulate expected against measured mineralogy, state the zircon matrix and the export estimate, and invert a time series of samples.
4. Figures and text disagree in several results, and key settings are missing for reproduction. The plotted resolution diagonals cannot come from the stated operator (GB-25), the figures show steepest descent ending with a smaller error than the adopted quasi-Newton scheme (GB-30), and three sweep statements describe features that Fig. 10 does not show (GB-39). Further moderate findings: settings per test (GB-27), XRD measurement environment (GB-18), the archive inventory and sample identifiers (GB-58), the uncertainty metric's name and definition (GB-17), three printed equations (GB-16) and citations that do not support their statements (GB-05, GB-06). Suggestion: recompute and redraw the affected figures from stated formulas, and add a settings table, a sample table and an archive inventory.

## Findings by segment

### Segment 1: Title, abstract, introduction (p. 1 to 5)

#### Substantive findings

**GB-01 Cost and time efficiency is presented as validated, but no cost, time or effort measure is reported and no comparison is made.**

| Field | Content |
|---|---|
| Check | P33, P10 |
| Location | p. 1, l. 3 to 4; p. 2, l. 40 to 42 (repeated p. 4, l. 107 to 109); p. 3, l. 74 to 75 (repeated p. 5, l. 141 to 142) |
| Quotation | "In this study, we validate a time- and cost-effective fingerprinting approach based on X-ray diffraction (XRD) data." / "To conclude, we show and validate the potential of binned XRD peak-area data as a cost- and time-efficient approach for constructing erosion rate maps." |
| Concern | The efficiency claim is part of the stated aim ("offering an efficient alternative to conventional approaches", l. 41 to 42) and is presented as validated. A search of the whole text finds no cost per sample, no analysis or preparation time and no number of samples needed. The only support is the citation that other methods "are expensive and time-consuming (Das et al., 2023)" (l. 35), which could not be read (see Limits). The design does contain the comparison the claim requires, because the same detrital date was analysed by XRD and by zircon U-Pb dating (l. 420 to 424), but effort is reported for neither. Instances S1 and S4 noted the same gap independently. The grade is major because the claim is in the Abstract and in the stated aim. |
| Suggestion | In Section 4.2.2 report, for XRD and for zircon U-Pb on the same samples, preparation and measurement time per sample, consumables or instrument cost per sample and the sample mass needed. Otherwise remove "validate" and "cost- and time-efficient" from l. 3 to 4, l. 40 to 42 and l. 74 to 75 and keep efficiency as a motivation. |
| Status | verified (absence of any effort measure, whole text searched) |
| Severity | major |
| Source | SD |

**GB-02 Abstract and Conclusions report consistent convergence and robustness, while the results report non-convergence, instability and narrow working ranges.**

| Field | Content |
|---|---|
| Check | P2, P6, P15 |
| Location | p. 1, l. 7; p. 16, l. 482 to 483; against p. 11, l. 312; p. 12, l. 352 to 353, l. 360 to 361; p. 12 to 13, l. 373 to 374, l. 380 to 381, l. 387 to 388; p. 14, l. 435; Fig. 8 caption (p. 29); prior setting p. 10, l. 295; p. 11, l. 325 to 326 |
| Quotation | "Forward-inverse tests with synthetic data demonstrate consistent convergence of the posterior solution." / "we show that the true erosion pattern can be reliably recovered, and that the method is robust across a range of parameters" |
| Concern | The Results document their own failures openly. The summary statements do not carry them over. Reported failures: the unnormalised steepest descent scheme "proved unstable" (l. 312); for blended fingerprints "In many of these cases, the inversion fails to converge to a stable posterior solution" (l. 353), and the most blended case is not plotted (Fig. 8 caption; 6 of 20 runs are missing from Fig. 8, GB-34); error rises when fewer than 7 tracers are used (l. 360 to 361); the zircon-only natural run is "highly unstable" (l. 435). The text also gives a convergence threshold of 25 iterations (l. 387 to 388), whereas Fig. 10 places it between 5 and 15 (GB-39). In addition, every synthetic test sets the prior to "the average true erosion rate" (l. 295, l. 325 to 326), which is information an application does not have. "Reliably recovered" and "robust" therefore hold under conditions the Conclusions do not name: the quasi-Newton scheme, an average JS distance above about 0.44 to 0.55 (Fig. 8 label "avg. JS = 0.441"; l. 352), at least 7 tracers, the tested hyperparameter ranges and a prior at the true mean. The grade is major because the statement is the main validation claim of the Abstract. |
| Suggestion | Rephrase l. 7 and l. 482 to 483 so that they name the conditions under which convergence was obtained (scheme, JS distance, number of tracers, iteration count, tested parameter ranges), state the number of runs that did not converge, and add that the prior was set to the true mean erosion rate in all synthetic tests. |
| Status | verified (all quoted passages at the page images); inferred (JS threshold from l. 352 to 353 and the Fig. 8 label) |
| Severity | major |
| Source | S3, S4, SD |

**GB-03 Abstract, Introduction and Discussion say that the natural-data tests validate the method, although they test plausibility without an independent erosion reference.**

| Field | Content |
|---|---|
| Check | P15 |
| Location | p. 1, l. 7 to 8; p. 3, l. 74 (repeated p. 5, l. 141); p. 15, l. 451; basis p. 13 to 15, l. 390 to 449 |
| Quotation | "The application to real-world datasets further validates the practical utility and robustness of the model." / "We explained and validated the use of binned XRD peak-area data as mineralogical fingerprints" |
| Concern | The synthetic tests compare the posterior with a known map and can validate the inversion. The natural tests cannot. Section 4.2 compares the fingerprints with "established knowledge of the lithology" (l. 399 to 400) without a criterion (GB-43). Section 4.2.1 tests one condition, near-zero erosion in the one unit without outcrops, with "some spillover" (l. 414 to 415) and an unstated number of samples (GB-44). Section 4.2.2 compares XRD with zircon for one detrital sample, without reference erosion rates (GB-53). None of these tests measures the accuracy of the erosion rates on natural data. The Results use the cautious verb "supports" (l. 417); the Abstract and the Discussion do not. The grade is major because the sentence states the central claim of the study. |
| Suggestion | In l. 7 to 8, l. 74 and l. 451 replace "validates", "validate" and "validated" for the natural data with "supports the plausibility of" and name what was tested (absence of erosion in the one non-outcropping unit; comparison with zircon for one sample). Reserve "validate" for the synthetic forward-inverse tests. |
| Status | verified |
| Severity | major |
| Source | S4 |

**GB-04 The introduction is printed twice: Sections 1 and 2 are word for word identical, so every later section number is one too high.**

| Field | Content |
|---|---|
| Check | P4 |
| Location | p. 1 to 3, l. 9 to 75; p. 3 to 5, l. 76 to 142; consequently Sections 3 to 6 (l. 143, 266, 450, 477) |
| Quotation | "1 Introduction" / "2 Introduction" |
| Concern | A word-by-word comparison of l. 10 to 75 against l. 77 to 142 gives 1153 words in each block and a difflib similarity ratio of 1.0, so no word differs. Instances S1, S2 and S4 computed this independently, and AB and SD noted the duplicate as well; the heading "2 Introduction" is confirmed on page image 3. Methods, Validation, Discussion and Conclusions are therefore numbered 3 to 6 instead of 2 to 5. |
| Suggestion | Delete Section 2 (l. 76 to 142) and renumber Methods to Conclusions as Sections 2 to 5, including all subsections (3.1 to 3.4, 4.1 to 4.2.2). |
| Status | verified |
| Severity | minor |
| Source | S4 |

**GB-05 Three of the sources cited for sediment traps on dams do not concern sediment traps or dams.**

| Field | Content |
|---|---|
| Check | P13 |
| Location | p. 1, l. 18 to 19 (repeated p. 3, l. 85 to 86) |
| Quotation | "Direct measurements, such as sediment traps installed on dams, provide valuable information on sediment fluxes but do not reveal the origin of the transported material (Wilson et al., 1993; Barker et al., 1997; Davis and Fox, 2009)." |
| Concern | Davis and Fox (2009), a review of fingerprinting, fits the second half of the sentence. The other two sources do not support the first half. Barker, Dixon and Hooke (1997, Earth Surface Processes and Landforms, 22, pp. 1217 to 1227) test terrestrial photogrammetry for river bank erosion volumes; the abstract (read by S1 on the University of Portsmouth research portal) mentions neither sediment traps, nor dams, nor sediment flux past a point. Wilson et al. (1993, Applied Geography, 13, pp. 329 to 352) is, by its title, an assessment of soil erosion in the Falkland Islands; its abstract could not be read. No cited work supports the example "sediment traps installed on dams". Instance S4 flagged the same mismatch independently. |
| Suggestion | In l. 18 to 19 (and l. 85 to 86) replace Wilson et al. (1993) and Barker et al. (1997) with studies that measure sediment flux by traps, reservoir surveys or turbidity gauging, or rephrase the example to match what the cited works measure. |
| Status | verified for Barker et al. (1997) (abstract read); inferred for Wilson et al. (1993) (title only) |
| Severity | moderate |
| Source | S1 |

**GB-06 In the list of fingerprinting tracers, three of four sources checked do not use the tracer they are cited for; one is a theology article.**

| Field | Content |
|---|---|
| Check | P13, P4 |
| Location | p. 2, l. 28, l. 30, l. 31 (repeated p. 4, l. 95, l. 97, l. 98); reference list p. 17, l. 528 to 530 (Blaen et al.); p. 19, l. 597 to 598 (Kobe); p. 20, l. 641 to 642 (Walden et al.) |
| Quotation | "nutrients (Blaen et al., 2016; Asadi et al., 2025)" / "mineralogy (Walden et al., 1997; Nukazawa et al., 2021)" / "plant pollen content (Brown, 1985; Kobe, 2021)" |
| Concern | The list in l. 26 to 33 gives a useful overview of tracer families with 29 citations. Of four sources opened, three do not fit. (1) Kobe (2021), "Ubuntu as a spirituality of liberation for black theology of liberation", HTS Teologiese Studies / Theological Studies, 77(3), a6176, is a theology article without any reference to pollen or sediment; the article page was read by S1 and by S4 independently. (2) Walden, Slattery and Burt (1997, Journal of Hydrology, 202, pp. 353 to 372) use mineral magnetic measurements; they belong under magnetic susceptibility in l. 29, not under mineralogy. For an XRD paper this matters, because the mineralogy family is then backed by one source only. (3) Blaen et al. (2016) review real-time monitoring of nutrients and dissolved organic matter in rivers and do not use nutrients as source tracers. The fourth source opened, Torres Astorga et al. (2020), broadly supports "total organic carbon (TOC)". Quota: 3 of 4 opened sources do not support the attribution. By title alone, Olley et al. (1993), Delbecque et al. (2022) and Vanden Bygaart and Protz (2001) fit their categories only loosely; these were not opened. |
| Suggestion | In l. 28, 30 and 31 (and l. 95, 97, 98) delete Kobe (2021) from the text and from the reference list (l. 597 to 598) or replace it with the intended pollen fingerprinting study; move Walden et al. (1997) to magnetic susceptibility and add an XRD or petrography based fingerprinting study under mineralogy (for example Andrews and Eberl, 2012, see GB-07); replace Blaen et al. (2016) with a study that uses nutrients as source tracers; check every remaining entry of l. 26 to 33 against its source. |
| Status | verified for Kobe (2021), Walden et al. (1997) and Blaen et al. (2016) (sources read); inferred for Olley et al. (1993), Delbecque et al. (2022) and Vanden Bygaart and Protz (2001) (titles only) |
| Severity | moderate |
| Source | S1, S4 |

**GB-07 Published work that precedes the contribution directly is missing: an XRD-based unmixing method tested on known mixtures and a spatial erosion study from detrital data in a glacial catchment.**

| Field | Content |
|---|---|
| Check | P14 |
| Location | p. 2, l. 36 to 42 and l. 58 to 63 (repeated p. 4, l. 103 to 109 and l. 125 to 130); related p. 13, l. 404 to 406 |
| Quotation | "X-ray diffraction (XRD) has recently gained attention as a proxy for mineral abundance in provenance analysis but remains underutilized (Das et al., 2023)." / "This spatially informed approach to sediment provenance is particularly valuable in glacierized catchments" |
| Concern | The contribution is that binned XRD peak areas serve as fingerprints in a spatially explicit inversion that turns suspended sediment into erosion rate maps for a glacierized catchment. Three works that bear directly on it are missing from the reference list (checked against p. 17 to 21; the records were read by S1). (1) Andrews, J.T. and Eberl, D.D. (2012) 'Determination of sediment provenance by unmixing the mineralogy of source-area sediments: The "SedUnMix" program', Marine Geology, 291 to 294, pp. 24 to 33, https://doi.org/10.1016/j.margeo.2011.10.007. This is an earlier quantitative XRD unmixing of provenance, tested on eleven artificial mixtures of four end members, which is the known-mixture test that l. 404 to 406 names as standard. (2) Ehlers, T.A., Szameitat, A., Enkelmann, E., Yanites, B.J. and Woodsworth, G.J. (2015) 'Identifying spatial variations in glacial catchment erosion with detrital thermochronology', Journal of Geophysical Research: Earth Surface, 120, pp. 1023 to 1039, https://doi.org/10.1002/2014JF003432. It infers the spatial distribution of erosion in a glacierized catchment from detrital data. (3) De Doncker, F., Herman, F., Prasicek, G., Adatte, T., Mettra, F. and Belotti, B. (2021) 'Present-day sediment dynamics and provenance of the Gornergletscher', EGU General Assembly 2021, EGU21-6207, https://doi.org/10.5194/egusphere-egu21-6207. It reports erosion rate maps for the same catchment from a non-linear inverse model (see GB-54). Candidates already in the reference list were dropped (Lipp et al., 2021; Das et al., 2024; De Doncker et al., 2020; Belotti, 2021). |
| Suggestion | In l. 36 to 42 add Andrews and Eberl (2012) as earlier XRD-based unmixing and contrast it with binned peak areas; in l. 61 to 63 add Ehlers et al. (2015) and state what the inversion adds; cite or discuss the EGU21-6207 results for the same catchment. |
| Status | verified (each record read; reference list checked) |
| Severity | moderate |
| Source | S1 |

**GB-08 Two general statements about the unmixing literature, one of which defines the gap the paper fills, are attributed to a single-catchment case study.**

| Field | Content |
|---|---|
| Check | P13 |
| Location | p. 2, l. 44 to 48 and l. 58 to 59 (repeated p. 4, l. 111 to 115 and l. 125 to 126) |
| Quotation | "However, these approaches typically yield relative source contributions without translating them into spatially explicit erosion rate maps and implicitly rely on a linear mixing scheme (Niu et al., 2020)." |
| Concern | The quoted sentence carries the gap the manuscript sets out to fill, so its source matters. According to its abstract (read by S1 on link.springer.com), Niu et al. (2020, Journal of Soils and Sediments, 20, pp. 1097 to 1111) test composite fingerprints in one catchment (66 samples), quantify uncertainty with a first-order Gaussian approximation and use a linear mixing model. The abstract neither compares frequentist and Bayesian methods (attributed in l. 44 to 48) nor states what "these approaches typically" yield. A single case study can illustrate the practice but cannot support a statement about the field. Reviews already in the reference list (Haddadchi et al., 2013; Collins et al., 2020) would be natural sources. The full text was not readable. |
| Suggestion | In l. 47 to 48 and l. 58 to 59 attribute both characterisations to a review, or point to the passage of Niu et al. (2020) that makes them; keep Niu et al. (2020) as an example of a linear mixing model. |
| Status | inferred (abstract only) |
| Severity | moderate |
| Source | S1 |

**GB-09 In the overview of unmixing methods, the same methods appear under two names and one abbreviation is undefined.**

| Field | Content |
|---|---|
| Check | P38 |
| Location | p. 2, l. 48 to 49, l. 51, l. 53, l. 55 to 56 (repeated p. 4, l. 115 to 116, l. 118, l. 120, l. 122 to 123) |
| Quotation | "1) the Non-Linear Least Squares (NLLS) (a constrained linear regression)" / "similar to the NNLS approach" / "a hybrid between Bayesian linear mixed models and hierarchical Bayesian models" |
| Concern | The abbreviation introduced in l. 48 to 49 is NLLS; the back reference in l. 51 uses NNLS, which is not defined. The gloss "a constrained linear regression" fits non-negative linear least squares rather than non-linear least squares. The instances proposed opposite repairs: S1 and S4 read NNLS, SD read NLLS, so the intended method cannot be decided from the manuscript. Likewise "Bayesian Linear Mixing Models (BLMM)" (l. 53) is referred to as "Bayesian linear mixed models" (l. 55 to 56), a name that in statistics denotes a different model class. The manuscript positions its own approach against exactly these categories (l. 55 to 57). |
| Suggestion | In l. 48 to 51 state which method is meant and use one name and abbreviation in both places; in l. 55 to 56 write "Bayesian linear mixing models (BLMM)"; correct the repeat on p. 4 or remove it (GB-04). |
| Status | verified (page image 2); assumption (which least squares variant is meant, posed as a question) |
| Severity | minor |
| Source | S2, S1, S4, SD |

#### Minor corrections

| ID | Location | Quotation | Replacement | Source |
|---|---|---|---|---|
| KK-01 | p. 1, l. 5; p. 10, l. 287 (heading); p. 11, l. 320; Fig. 5 caption (p. 26) | "(steepest descent and Quasi-Newtonian)"; "the Quasi-Newton (QN) approach" | "(steepest descent and quasi-Newton)"; "the quasi-Newton (QN) approach", as defined in l. 211 | S2, S4 |
| KK-02 | p. 2, l. 50 (repeated p. 4, l. 117) | "Generalist Likelihood Uncertainty Estimation (GLUE)" | "Generalized Likelihood Uncertainty Estimation (GLUE)" | S1, S4 |
| KK-03 | p. 2, l. 51 (repeated p. 4, l. 118) | "Maximal Likelihood Estimation (MLE)" | "Maximum Likelihood Estimation (MLE)" | S4 |
| KK-04 | p. 2, l. 61 (repeated p. 4, l. 128); p. 6, l. 181; p. 11, l. 333 to 334; p. 14, l. 424 to 425 | "validated in (De Doncker et al., 2020)"; "becomes Tarantola (2005):"; "the map proposed by (Steck et al., 2015)"; "described in (Belotti, 2021)"; "outlined in (De Doncker et al., 2020)" | "validated by De Doncker et al. (2020)"; "becomes (Tarantola, 2005):"; "the map proposed by Steck et al. (2015)"; "described in Belotti (2021)"; "outlined in De Doncker et al. (2020)" | S1, S3, S4 |
| KK-05 | p. 3, l. 70; p. 9, l. 261; p. 11, l. 335; p. 13, l. 398; p. 14, l. 436; p. 15, l. 441, l. 446; captions of Figs. 14 to 16; against p. 10, l. 303; p. 11, l. 307; p. 5, l. 150; captions of Figs. 5, 6, 10 | "optimize"; "normalized"; "characterizing" beside "optimisation"; "normalised"; "characterised" | one spelling throughout; with "colour" in l. 33, l. 336 and l. 349, the British forms "optimise", "normalised", "characterising" | S4 |

#### Verification log

| ID | Check | Checked | Values | Result |
|---|---|---|---|---|
| PP-01 | P14 | Positioning of the contribution (abstract l. 3 to 8; l. 63 to 66): binned XRD peak areas as fingerprints in a spatially explicit, positivity-constrained inversion for a glacierized catchment | 4 search queries (Gornergletscher provenance; detrital thermochronology erosion maps; XRD fingerprinting unmixing; inverse model spatially explicit erosion map). Candidates in the reference list dropped: Belotti (2021), De Doncker et al. (2020), Das et al. (2024), Lipp et al. (2021). Not in the list: Andrews and Eberl (2012), Ehlers et al. (2015), EGU21-6207. Results pointing to later versions or discussion pages of this manuscript were not opened. The manuscript discloses no limits on positioning. | GB-07 |
| PP-02 | P28 | Gap and novelty sentences: l. 3 "often based on costly fingerprinting methods", l. 36 to 37 "remains underutilized", l. 58 to 59 "typically ... without translating them into spatially explicit erosion rate maps", l. 61 to 63 "particularly valuable in glacierized catchments", l. 454 to 455 "The novelty of our method lies in" | No database, search terms, period or search date are named for any of the five. l. 36 to 37 is attributed to Das et al. (2023), a citation and not the authors' own gap claim; "recently gained attention" is consistent with Das et al. (2024). l. 3 is a cost statement (GB-01). | GB-54 for l. 58 to 59 and l. 454 to 455; GB-08 for the source; otherwise no finding |
| PP-03 | P13 | Statements in segment 1 that attribute content to cited works; 13 sources looked up, 10 readable at least as abstract | Torres Astorga et al. (2020) for TOC (l. 30): consistent. Das et al. (2024) for "Building on the work of" (l. 40): XRD mineralogy with MixSIAR, consistent. De Doncker et al. (2020) for the inversion framework (l. 61): consistent. Haddadchi et al. (2013) for the four frequentist methods (l. 48 to 52): abstract lists seven mixing models on 41 catchments, full text not readable, no finding. Belotti (2021) for the zircon method (l. 424): consistent. Not readable: Das et al. (2023), Klages and Hsieh (1975); Wilson et al. (1993) title only. | GB-05, GB-06, GB-08; otherwise no finding |
| PP-04 | P9, P19 | Design sketch: questions, type, cases, data sources, timeline, environment, components, disclosed limits | Objective l. 63 to 64; validation questions 1) to 3) l. 282 to 285; one stated expectation l. 72 to 73 and one hypothesis l. 410 to 411. Type: method development with synthetic tests and one natural case. 7 source units, 21 tracers, pixel 300 m; source samples per unit not stated; detrital samples in 4.2.1 "multiple"; one detrital sample (28 June 2019, 13:30) in 4.2.2. Data classes: model-generated (synthetic), primary (XRD source and detrital), interpreted (map under ice), secondary unpublished (zircon). Disclosed limits: underdetermination (l. 170 to 172), Gaussian approximation (l. 178 to 179), inferred geology (l. 270 to 272), small units (l. 299 to 300), steepest descent instability (l. 312), non-convergence for similar fingerprints (l. 351 to 354), missing zircon data (l. 430 to 434), spillover (l. 414 to 415), storage (l. 466 to 468), grain size, orientation and peak overlap (l. 469 to 476). | basis of GB-01, GB-10, GB-13, GB-14, GB-19, GB-22, GB-24, GB-43, GB-44, GB-46, GB-53 |

### Segment 2: Methods, data, study area, Figures 1 to 4 (p. 5 to 10)

#### Substantive findings

**GB-10 Limitations of the XRD pipeline and of the forward model appear only in the Discussion, and the mitigations claimed there are not measured.**

| Field | Content |
|---|---|
| Check | P17, P31 |
| Location | p. 5, l. 145 to 152 (Section 3.1); p. 9, l. 249 to 265 (Section 3.4); p. 15 to 16, l. 466 to 476 |
| Quotation | "Preferred orientation of minerals such as micas may bias measurements (Weir et al., 1975), but applying the same sample preparation and analysis protocol to both detrital and source material should help cancel out such effects." |
| Concern | Grain-size effects, preferred orientation, shielding and peak overlap (l. 469 to 476) and the neglect of storage (l. 466 to 468) are disclosed, which deserves credit, but only in the Discussion. Section 3.4, where the XRD pipeline is introduced, does not mention them, and Section 3.1 says that sediments "are then transported or stored" (l. 147 to 148) without stating that storage is neglected. The mitigations ("should help cancel out", "helps normalize", "reduces the possible impact") are stated as effects, but no measurement of them is reported. A common preparation protocol does not remove a grain-size difference between source rock powder and suspended sediment; this last point is general knowledge and is put as a question. For the peak overlap claim the manuscript's own Fig. 11 shows identical tracers (GB-42). |
| Suggestion | Move the assumptions to Sections 3.1 and 3.4 where the methods are introduced. Either measure the mitigations (for example repeated preparation of one sample for orientation effects, sieved fractions for grain size) or rephrase them as untested expectations. |
| Status | verified (placement, absence of measurement); assumption (grain-size difference between source and detrital material) |
| Severity | moderate |
| Source | SD |

**GB-11 The schematic Figures 1 and 2 use colours that their legends do not explain.**

| Field | Content |
|---|---|
| Check | P29 |
| Location | Fig. 1 panels (c) and (d) (p. 22); Fig. 2 panels (b) and (c) (p. 23) |
| Quotation | "(c) suspended sediment sampling at sink, with lithology proportions (d) reflecting the erosion rates in the different lithologies." |
| Concern | In Fig. 1d dark grey segments alternate with the four lithology colours in the sample cylinder and are not in the legend. In Fig. 2b several bars of the detrital tracer concentration are black, and in Fig. 2c only the green layer (tracer n) has a concentration scale. Both figures are schematic, so no scale is expected, but every colour should be identifiable. |
| Suggestion | Add the dark grey and black elements to the legends or explain them in the captions, and note that the colour ramp applies to all tracer layers. |
| Status | verified (page images) |
| Severity | minor |
| Source | AB |

**GB-12 The iteration index changes within one update formula, and tracer and pixel indices change between equations, text and Figures 1 to 3.**

| Field | Content |
|---|---|
| Check | P38 |
| Location | p. 5, eq. 1 (l. 155 to 156); p. 6, eq. 4; p. 7, eq. 17 and l. 209; p. 8, eq. 18 (l. 215), l. 216, eq. 19; p. 9, l. 262 to 263; Fig. 1b (p. 22); Figs. 2b and 2c (p. 23); Figs. 3d and 3e (p. 24) |
| Quotation | "with µ being the step size, and εk+1 the posterior model after k + 1 non-linear iteration steps" / "where Gn is the Jacobian at iteration n" |
| Concern | Eq. 17 iterates over k. Eq. 18 and 19 write εn+1 = εn minus a step that contains (εk minus εprior), so the current iterate appears under two indices in one formula (page image 8). In eq. 1 and 4, n is the number of pixels and m the number of tracers. The tracer index is i in eq. 1, t in l. 262 and n in Figs. 1 to 3 ("tracer n", "tracer mineral n"), where i denotes a detrital sample instead; the pixel index is j in eq. 1 and xy in l. 262. Together these make eq. 18 and 19 ambiguous about where the prior term is evaluated, which matters for anyone reimplementing the update; hence moderate rather than minor. |
| Suggestion | Use one iteration index in eq. 17 to 19 and l. 216 and replace εk in eq. 18 and 19 by the current iterate; keep n for the number of pixels and m for the number of tracers; use i for tracers and j for pixels also in l. 262 to 263 and in the labels of Figs. 1 to 3. |
| Status | verified (page images 5 to 9, 22 to 24) |
| Severity | moderate |
| Source | S2, SD |

**GB-13 The sediment export estimate that scales all natural results and the prior used for the natural runs are neither given nor sourced; the prior is described as the true mean erosion rate.**

| Field | Content |
|---|---|
| Check | P12, P11, P25, P8 |
| Location | p. 5, l. 160 to 162 (eq. 2); p. 3, l. 65 to 66 (repeated p. 5, l. 132 to 133); p. 9, l. 267 to 268; p. 14, l. 426 to 428; p. 15, l. 444 to 445, l. 452 to 454; p. 16, l. 479 to 480, l. 490 |
| Quotation | "For simplicity, we redefine the data vector d as scaled by the total erosion rate" / "a prior equal to the average true erosion rate" / "a site well-suited for this study due to the availability of multi-year suspended sediment datasets" |
| Concern | The method needs an estimate of the total annual suspended sediment export as one of four inputs (l. 65 to 66, l. 452 to 454, l. 479 to 480); by eq. 2 it scales the data vector and hence the absolute erosion rates. No section gives its value, source, period, or the conversion from mass export to erosion rate (rock density, pixel area 300 m by 300 m, catchment area). The suspended sediment record that justifies the site choice (l. 267 to 268) has no citation, provider, station or period, and the data statement (l. 490) covers "data and codes used for the inversion tests" without saying whether this record is archived. For the natural zircon run, and by "the same inversion parameters" (l. 444 to 445) for the XRD and combined runs, the prior is "the average true erosion rate" (l. 428), a quantity that exists only in the synthetic tests. The absolute values in Figs. 13 to 16 (0 to 3 mm/y, 8.4 mm/y, above 8000 mm/y) therefore cannot be traced to inputs. A file name in the code repository that the Zenodo record points to suggests that load data are included, which the manuscript does not say. The grade is major because the absolute erosion rates of all natural results depend on these inputs. |
| Suggestion | Question to the authors: which export estimate and which prior were used for the natural inversions, from which source and period? In Section 3.1 next to eq. 2 and in Section 4.2 give the export value with its uncertainty, the conversion to an erosion rate and the resulting prior per natural case; replace "average true erosion rate" in l. 428; cite the suspended sediment record in l. 267 to 268 and state in l. 490 whether it is archived or where it can be obtained. |
| Status | verified (absence of value, source and statement coverage; wording of l. 428); inferred (load data in the repository, from a file name); assumption (which values were used, posed as a question) |
| Severity | major |
| Source | S2, S3, SD |

**GB-14 Posterior uncertainty and error propagation are claimed, but the data uncertainty is assumed, fingerprint variability is not propagated, the Gaussian approximation is not checked, and the uncertainty metric hardly responds to the data uncertainty.**

| Field | Content |
|---|---|
| Check | P31, P19 |
| Location | p. 6, l. 178 to 179; p. 1, l. 6 to 7; p. 6, l. 185 to 186 (eq. 8); p. 10, l. 295; p. 13, l. 380 to 384; Fig. 10 rows 1 and 3, second column (p. 31); p. 14, l. 435 to 436 |
| Quotation | "We assume weak nonlinearity, where our forward model can be linearized around the prior, hence, the a posteriori probability density remains approximately Gaussian." / "in order to invert detrital mineralogical data into erosion rate maps while quantifying posterior uncertainty and error propagation" |
| Concern | (a) σd = 0.01 mm/y is set, not derived from replicate XRD measurements; no replicate is reported. (b) The source fingerprints in A enter as exact values; the number of source samples per unit is not stated (l. 251), so within-unit variability is neither measured nor propagated, although the Abstract claims error propagation. (c) The linear Gaussian posterior (eq. 20) rests on the weak non-linearity assumption, which is disclosed (l. 178 to 179) but not checked, while the zircon run reaches "extreme erosion rate values (>8000 mm/y)" (l. 435), a regime in which a linearisation around the prior is questionable. (d) In Fig. 10 the normalised posterior uncertainty varies between 0.74015 and 0.74040 (span 0.00025, axis labels) over σd from about 0 to 0.9 mm/y, but from about 0.99 to about 0.27 (span about 0.72) over L from 250 to 3000 m. The metric is thus governed by the prior settings, not by the data uncertainty. The grade is major because this metric is the main criterion of the natural comparison (GB-53). |
| Suggestion | In Sections 3.3 and 4.2: derive σd from replicate diffractograms of some source and detrital samples; state the number of source samples per unit and propagate their spread, for example by resampling A; check eq. 20 against a sampling estimate for the synthetic case and one natural case; state in the Abstract that the uncertainties are conditional on the assumed σd and the prior. |
| Status | verified for (a), (b) and the σd span in (d) (axis labels); inferred for (c) and the L span in (d) (read from the axis) |
| Severity | major |
| Source | SD |

**GB-15 The regularisation term is called "prior misfit" where it is defined and "model misfit" everywhere else.**

| Field | Content |
|---|---|
| Check | P38 |
| Location | p. 6, l. 183 to 184; p. 7, sentence before eq. 15; p. 8, l. 240; p. 9, l. 245, l. 247; Figs. 5i, 6i, 7 to 10 (axis "Model misfit") |
| Quotation | "and the gradient of the model misfit can be written as" / "The model misfit (eq. 7) measures the deviation from the prior" |
| Concern | The term is introduced in l. 183 to 184 as "the prior misfit" with the symbol φprior and then called "model misfit" 13 times in the text and on the trade-off axes ("prior misfit" 1 match, "model misfit" 16 matches, 3 of them in figure text). The text never says that both names denote the same term, and "model misfit" is easily read as the misfit of the model prediction, that is the data misfit. |
| Suggestion | In l. 183 to 184 write "the prior (or model) misfit φprior" once, then keep one name in the text and on the axes of Figs. 5 to 10. |
| Status | verified |
| Severity | minor |
| Source | S2 |

**GB-16 Three printed equations do not give the quantities the text describes: the model covariance grows with distance, and the Jacobian and the data-misfit gradient are dimensionally inconsistent.**

| Field | Content |
|---|---|
| Check | P1 |
| Location | p. 7, eq. 9 (between l. 186 and l. 190); p. 7, eq. 12 (between l. 196 and l. 200); p. 7, eq. 14 (after l. 200); against p. 7, eq. 16 (l. 205) |
| Quotation | "Cm(i, j) = σm² exp(si,j² / L²)" / "∂dε/∂ε = G = A · exp(ε)" / "∇ε φd = G Cd⁻¹ (dε - dobs)" |
| Concern | Transcribed from page image 7. (1) Eq. 9 has no minus sign in the exponent. As printed, the covariance between two pixels grows with their distance s: for s = 3000 m and L = 1200 m the factor is exp(6.25) = 518 (Python), whereas a smoothing prior, as l. 190 describes L ("the smoothing distance"), needs a covariance that decays with distance, exp(minus s²/L²). (2) In eq. 12 the Jacobian is written as A · exp(ε), the same product that defines the predicted data dε in l. 195, which is an m-vector; the Jacobian of eq. 3 is the m by n matrix A · diag(exp(ε)). (3) Eq. 14 writes G Cd⁻¹ without transpose, which does not conform (m by n times m by m), while eq. 16, which combines eq. 14 and eq. 15, writes Gᵀ Cd⁻¹. No instance treated these equations within its checklist; S2 and S4 noted them outside their checklists, and the observation is confirmed at the page image. The code may implement the correct forms; the grade is moderate because a reader who reimplements from the printed equations obtains a covariance that does not smooth. |
| Suggestion | In eq. 9 write exp(minus si,j²/L²) and confirm that the code uses this form; in eq. 12 write G = A · diag(exp(ε)) or give the element form Gij = Aij exp(εj); in eq. 14 write Gᵀ Cd⁻¹ (dε minus dobs). |
| Status | verified (printed forms at page image 7); inferred (consequences and dimension argument) |
| Severity | moderate |
| Source | ZF |

**GB-17 The posterior uncertainty metric used in Figures 5, 7 to 10 and 14 to 16 appears under at least seven names, two symbols and two different definitions.**

| Field | Content |
|---|---|
| Check | P38, P20 |
| Location | p. 8, l. 236 to 239 and eq. 22; p. 10, l. 303; p. 10 to 11, l. 306 to 307; p. 11, l. 335; p. 14, l. 436 to 437; p. 15, l. 441 to 442, l. 446 to 447; Fig. 5 panels (f) and (h) and caption (p. 26); Figs. 7 to 10, panel titles and y-axes (p. 28 to 31); Figs. 14 to 16, map titles and annotation (p. 35 to 37) |
| Quotation | "The third metric is the ratio between the posterior model covariance and the “prior” model covariance." / "The same pattern is visible in the normalised posterior variance" |
| Concern | Names for what is presented as one metric: "ratio between the posterior model covariance and the prior model covariance" (l. 236 to 237), "normalised posterior variance" (l. 303, against "normalised posterior covariance" for the same panel in the Fig. 5 caption, item f), "posterior covariance" (l. 306), "Normalised covariance trace" (Fig. 5h), "Posterior uncertainty" (Figs. 7 to 9 titles), "Trace(post. cov.)" and "Trace(post.covar.)" (y-axes of Figs. 7 to 10), "normalized posterior uncertainty" (l. 335, l. 441, l. 446), "total normalized uncertainty" (l. 436), "Total normalised posterior uncertainty" (Figs. 14 to 16). Eq. 22 defines a per-pixel ratio of square roots, that is of standard deviations; the total in l. 436 to 437 is a ratio of traces, tr(Cm,post)/tr(Cm), that is of summed variances. Both carry the same name in Figs. 14 to 16. The plotted scalars (about 0.27 to 1.0 in Fig. 10) cannot be an unnormalised trace, because single diagonal elements of the posterior covariance reach 2 to 8 (Fig. 5e colour bar). A reader cannot tell which formula produced the curves in Figs. 5h and 7 to 10, nor relate the totals (0.82 to 0.87) to the map values. |
| Suggestion | After eq. 22 in Section 3.3 define the scalar used in the figures as a separate quantity with its own name and symbol, state for each quantity whether it is based on variances or standard deviations, and use these names in l. 303, 306, 335, 436, 441, 446 and on all panel titles and axes of Figs. 5 and 7 to 16. |
| Status | verified (names and labels at page images 8, 10, 11, 14, 15, 26, 28 to 31, 35 to 37); inferred (the plotted scalar is not an unnormalised trace, from value ranges) |
| Severity | moderate |
| Source | S2, S3, S4 |

**GB-18 The XRD measurement and sampling environment is not described well enough to rebuild the fingerprints.**

| Field | Content |
|---|---|
| Check | P35, P8 |
| Location | p. 9, l. 251 to 262; p. 13, l. 393 to 398; Fig. 3a (p. 24); p. 15, l. 470 |
| Quotation | "In a third step, the WinXRD Peak Finder algorithm corrects for baseline drift and removes the background noise, facilitating the identification of local maxima through thresholding and peak fitting." |
| Concern | Not stated: diffractometer, radiation, 2θ range, step width and counting time; WinXRD version and Peak Finder thresholds; the 21 diagnostic 2θ windows (positions, widths, selection criterion); how "average the total peak area within the 2θ windows" (l. 260) is computed when a window holds several peaks; number and location of source samples per unit; the detrital sampling device and depth (the Discussion recommends "depth-integrated suspended sediment samples", l. 470, while Fig. 3a shows a pump sampler); the grain-size fraction analysed; number and dates of detrital samples. Steps 3 and 5 rest on thresholds and window choices that are not described. |
| Suggestion | Add to Section 3.4 a table of the 21 windows (mineral, RRUFF reference, 2θ limits), the instrument settings and the Peak Finder parameters; add to Section 4.2 the number, location, date, sampling method and grain-size fraction of every source and detrital sample, or place them in a supplement and the archive (see GB-58). |
| Status | verified (absence) |
| Severity | moderate |
| Source | SD |

**GB-19 Normalising each sample by its own maximum peak area is incompatible with the linear mixing of eq. 1 and biases the inferred contributions by the sources' maximum intensities.**

| Field | Content |
|---|---|
| Check | P25, P9 |
| Location | p. 9, l. 260 to 264; p. 5, l. 151 to 152 (eq. 1); p. 13, l. 404 to 406 |
| Quotation | "At the end, these are normalized within each sample by dividing by the maximum observed peak area, yielding relative mineral concentrations on a scale from 0 to 1" / "Hence, the detrital data are a weighted average of the tracer mineral concentrations, with the weights being the erosion rates." |
| Concern | Eq. 1 requires that the tracer quantity of the mixture equals the erosion-weighted average of the same quantity in the sources. After each sample is divided by its own maximum, this holds only if all sources share the same maximum peak area; with the free scale of eq. 2 and 3 the fit recovers weights proportional to the true weight times the source maximum. Example (Python): two sources with maxima 10 and 8, mixed 50:50; the max-normalised mixture is fitted exactly (residual 0.0) with a share of 0.556 for source 1 instead of 0.5. The bias is invisible in the data misfit. The step is said to minimise "the influence of absolute intensity differences" (l. 264), but it introduces a dependence on exactly these intensities. Whether peak areas are linear in mass fraction at all (matrix absorption) is not tested; this part rests on general knowledge and is put as a question. Collins, A.L. et al. (2020) 'Sediment source fingerprinting: benchmarking recent outputs, remaining challenges and emerging themes', Journal of Soils and Sediments, 20, pp. 4160 to 4193, https://doi.org/10.1007/s11368-020-02755-4, already in the reference list (p. 18) and read by SD, recommend artificial mixtures in Sect. 2.2 regardless of tracer type. The grade is major because the bias affects every natural XRD inversion. |
| Suggestion | Prepare laboratory mixtures of the powdered source samples in predefined mass proportions (the test named in l. 404 to 406), run them through the full XRD pipeline and the inversion, and report recovered against true proportions. In Section 3.4 replace the per-sample maximum by a normalisation that preserves additivity (internal standard or total integrated intensity), or show that the bias is negligible for the measured maxima. Question to the authors: are the window peak areas linear in mass fraction for these minerals? |
| Status | inferred (mathematical consequence of the described steps); assumption (linearity of peak area in mass fraction, posed as a question) |
| Severity | major |
| Source | SD |

**GB-20 The third-party data behind the geological map and land cover, credited only inside Figure 4, have no reference entries and are not covered by the data statement.**

| Field | Content |
|---|---|
| Check | P12, P4 |
| Location | Fig. 4, credit block at lower right (p. 25); p. 9, l. 270 to 272; p. 16, l. 490; reference list p. 17 to 21 |
| Quotation | "Land cover data: SwissTopo 2018 Geological data: data from Steck et al., 2015, personal communication by L. Baumgartner, outcrops by GeoCover" |
| Concern | The geological map turns source fingerprints into the tracer matrix A (l. 166 to 167; l. 408) for all natural inversions. Its provenance is given only in the image credit of Fig. 4. Steck et al. (2015) has an entry (l. 631 to 633); SwissTopo and GeoCover do not, so these are citations without target, and Baumgartner appears only in the Acknowledgements (l. 499). The glacier outline and the "ELA estimation" in the Fig. 4 inset have no stated source. The manuscript discloses that the geology under ice is inferred (l. 270 to 272); what is missing is where the resulting map and its inputs can be obtained. Instance S4 graded the missing entries minor, S2 graded the data availability gap moderate; the higher grade applies because a reader cannot obtain an input of every natural result. |
| Suggestion | Add reference entries (product, version, year, licence) for the swisstopo land cover and the GeoCover dataset and cite them in the Fig. 4 caption and in l. 270 to 272; name the source of the glacier outline and the ELA; mark the personal communication as such in the text; state in l. 490 that the inferred map used for A and the modified maps of Scenario 1 (l. 327 to 334) are archived. |
| Status | verified (credit block at page image 25; absence in reference list and statement) |
| Severity | moderate |
| Source | S2, S4 |

**GB-21 Several figures use an abbreviation, colours or symbols that neither the figure nor the caption resolves.**

| Field | Content |
|---|---|
| Check | P29 |
| Location | Fig. 4 inset legend and caption (p. 25); Figs. 8 and 9, top rows (p. 29 to 30); Figs. 15 and 16, legends (p. 36 to 37) |
| Quotation | "ELA estimation" |
| Concern | "ELA" in the Fig. 4 inset is not resolved anywhere, and the caption of Fig. 4 ("Study area: location, land cover and geology.") does not explain the inset maps or the printed sources (GB-20). The stacked bars in the top rows of Figs. 8 and 9 use the lithology colours without a legend. In Figs. 15 and 16 the bar fills are the legend colours at about 70 % opacity: after blending with white at 0.7 every fill matches its legend patch within a colour difference of 3 to 8, without blending the differences are 57 to 148. Without blending, the Stockhorn, Tuftgrat and Gornergrat fill (#ff844d) is closest to the legend patch of the Monte Rosa gneiss (#fc7c44, difference 20), so a reader matching colours by eye can confuse the two units. The unit abbreviations are treated in GB-23 and the missing legend of Fig. 14 in GB-49. |
| Suggestion | Resolve "ELA" and extend the caption of Fig. 4; add legends to the top rows of Figs. 8 and 9; draw the legend patches of Figs. 15 and 16 with the same opacity as the fills. |
| Status | verified (page images, colour measurement) |
| Severity | minor |
| Source | AB |

**GB-22 The validation site does not demonstrably meet the manuscript's own application criteria, and the map that defines A is partly interpreted under ice.**

| Field | Content |
|---|---|
| Check | P18, P19 |
| Location | p. 9, l. 270 to 272; p. 2 to 3, l. 61 to 63 (repeated p. 4, l. 128 to 130); Fig. 4 credits (p. 25); p. 15, l. 459 to 468; p. 16, l. 484 to 486 |
| Quotation | "In ice-covered regions, where direct geological mapping is not possible, we infer the lithology based on regional geological knowledge." / "This spatially informed approach to sediment provenance is particularly valuable in glacierized catchments, where ice cover limits direct observations" |
| Concern | The manuscript recommends the method where source lithologies are "well constrained" and storage is minimal (l. 464 to 468, l. 484 to 486), yet promotes it for glacierized catchments where ice "limits direct observations" (l. 62 to 63) and tests it on a glacier catchment whose geology under ice is inferred (l. 270 to 272), partly from a personal communication (Fig. 4). The share of the catchment that is inferred rather than mapped is not given. Scenario 1 shows that map mismatch raises the error (Fig. 7), so the interpreted part of A is an unquantified error source in all natural results. Whether the Gornergletscher has significant subglacial or proglacial storage is not discussed; this is put as a question, since the manuscript gives no information on it (see also GB-57). |
| Suggestion | In Section 4 give the ice-covered, inferred area as a share of the catchment and of each unit; discuss storage at the site; state under which ice cover the method remains applicable, using Scenario 1 as quantitative basis, so that l. 62 to 63 and l. 464 agree. |
| Status | verified (wording, missing shares); inferred (tension between recommendation and test site); assumption (storage at the site, posed as a question) |
| Severity | moderate |
| Source | SD |

**GB-23 The seven source units carry different names in the study area text, in Figure 4 and in the result figures, and the text describes five groups while the inversion uses seven units.**

| Field | Content |
|---|---|
| Check | P38 |
| Location | p. 9 to 10, l. 273 to 279; p. 10, l. 299; p. 12, l. 340; p. 14, l. 411, l. 414, l. 431 to 434; Fig. 4 legend (p. 25); Fig. 5j legend (p. 26); Fig. 11 caption (p. 32); Fig. 12 legend and caption (p. 33); Fig. 13 labels (p. 34); Figs. 15 and 16 legends (p. 36 to 37) |
| Quotation | "while Penninic Mesozoic sedimentary units (Bündnerschiefer) consist mainly of calcareous mica schists and quartzites" / "the Monte Rosa garnet-gneiss (MR g-g) unit" |
| Concern | Name variants counted in the text and on the page images: serpentinite unit 4 forms ("Zermatt-Saas Fee ophiolites", "ZSF ophiolites (serpentinites)", "ZSF serpentinites", "Zermatt-Saas Fee ophiolites (serpentinites)"); sediment unit 7 forms, from "Penninic Mesozoic sedimentary units (Bündnerschiefer)" (l. 274 to 275), which shares no word with the others, to "ZSF sediments" (Figs. 5j, 11, 13, 15, 16); Stockhorn unit 5 forms, including "S.,T.,G." in Figs. 5j, 15 and 16, never expanded; granite unit 4 forms; metabasite unit 4 forms; gneiss unit 4 forms ("Monte Rosa (garnet gneiss and micaschist)", "MR g-g", "Monte Rosa (gneiss, micaschist)", "MR gneiss, mica"); Furgg series 1 form. ZSF is used in Fig. 5j and in the Fig. 11 caption but introduced only in l. 414 and l. 431; MR appears only as "MR g-g" (l. 432). Section 4 groups the geology into five tectonic groups (l. 273 to 279) and never states that the inversion uses seven units, nor which groups were split. That the Bündnerschiefer of l. 274 to 275 are the "ZSF sediments" unit is inferred from the Fig. 4 outcrop description. The known-mixture test depends on recognising exactly this unit, so the naming affects traceability of a result; hence moderate. |
| Suggestion | After l. 279 add a sentence or small table listing the seven source units with one fixed name and abbreviation each, state that the Bündnerschiefer of l. 274 to 275 form the ZSF sediments unit, and use these names in all legends, labels and captions. |
| Status | verified (all forms in the text and on the page images); inferred (identity of the l. 274 to 275 group with the ZSF sediments unit) |
| Severity | moderate |
| Source | S2, AB |

#### Minor corrections

| ID | Location | Quotation | Replacement | Source |
|---|---|---|---|---|
| KK-06 | p. 5 to 15, all panel references (first p. 5, l. 146), against the panel labels "(a)" to "(k)" in the figures | "(Figure 1B)"; "(Figure 5A)" | "(Figure 1b)"; "(Figure 5a)", matching the panel labels | AB |
| KK-07 | p. 6, l. 174 | "given the observed detrital data and a prior knowledge" | "given the observed detrital data and prior knowledge" | S4 |
| KK-08 | p. 6, l. 175, eq. 5 | "p(εm∣dobs) p(dobs∣εm) · p(εprior)/p(dobs)" (no relation sign between the first two terms at the page image) | "p(εm∣dobs) = p(dobs∣εm) · p(εprior)/p(dobs)" | S4 |
| KK-09 | p. 6, l. 178; p. 14, l. 437 | "We assume weak nonlinearity"; "the same nonlinear inversion technique" | "We assume weak non-linearity"; "the same non-linear inversion technique", as in l. 158 to 159 | S4 |
| KK-10 | p. 8, l. 236 | "data have improved our knowledge considerately relative to the prior" | "data have improved our knowledge considerably relative to the prior" | S4 |
| KK-11 | p. 8, l. 240 to 241 | "how well the model [spaced hyphen] here: our a posteriori erosion rate map [spaced hyphen] explains the observed data" | "how well the model (here, our a posteriori erosion rate map) explains the observed data" | S4 |
| KK-12 | p. 9, l. 243 to 244 | "or when it exceeds the user-defined maximal allowed number of iterations" | "or when the number of iterations reaches the user-defined maximum" | S4 |
| KK-13 | p. 9, l. 245 | "weighed by the model covariance" | "weighted by the model covariance" | S4 |
| KK-14 | p. 9, l. 251 to 252 | "in-situ source samples are collected from every lithological unit across the study area (Figure 3A and 3B)" | "in-situ source samples are collected from every lithological unit across the study area (Figure 3b)"; panel (a) shows detrital sampling | AB |
| KK-15 | Fig. 3, panel (c), legend (p. 24) | "quarz pattern alignment" | "quartz pattern alignment" | AB |
| KK-16 | p. 9, l. 263 | "(eq. 1-4)" | "(eqs. 1 to 4)" | S4 |
| KK-17 | p. 9, l. 267; p. 13, l. 392, l. 400; p. 15, l. 463; Fig. 11 caption (p. 32); legends of Figs. 5j, 15, 16 | "Gorner-gletscher catchment"; "Gorner Glacier catchment"; "Gorner gletscher catchment"; "Gorner glacier" | "Gornergletscher catchment" throughout, as in l. 272 and l. 282 | S2, S4, AB |
| KK-18 | Fig. 4 legend (p. 25) and Fig. 12 legend (p. 33) | "calcarious mica schist"; "GornergratPermo-Mesozoic"; "biotite schits"; "caclcite-zoisite amphibolites"; "silimanite-biotite gneiss" | "calcareous mica schist"; "Gornergrat Permo-Mesozoic"; "biotite schists"; "calcite-zoisite amphibolites"; "sillimanite-biotite gneiss" | AB |

#### Verification log

| ID | Check | Checked | Values | Result |
|---|---|---|---|---|
| PP-05 | P4, P29 | Numbering and targets of figures, panels, equations and sections; list of figures | Figures 1 to 16 each cited, first citations ascending (Fig. 1 l. 146, 2 l. 166, 3 l. 251, 4 l. 268, 5 l. 289, 6 l. 314, 7 l. 334, 8 l. 347, 9 l. 356, 10 l. 371, 11 l. 398, 12 l. 412, 13 l. 414, 14 l. 429, 15 l. 439, 16 l. 445). Panel references 1A to 1D, 2A to 2C, 3A to 3E, 5A to 5K, 6C to 6G resolve, except l. 317 (GB-31) and l. 251 (KK-14). Equations 1 to 22 consecutive; references to eq. 1 to 4, 7, 10 to 16 resolve. No tables, appendices or graphical abstract. Section numbering consecutive apart from the duplicate (GB-04). The decision on l. 251: S4 found the panel targets matching, AB found panel 3A cited for source sampling; at page image 24 panel (a) shows detrital sampling, so KK-14 is kept. | no further finding |
| PP-06 | P12 | Data sources named in Methods and Section 4 against the statement in l. 490 | 15 sources: source diffractograms, detrital diffractograms, Peak Finder outputs and settings, quartz alignment pattern, RRUFF spectra and window table, fingerprint tables, inferred and Scenario 1 maps, swisstopo, GeoCover, glacier outline and ELA, multi-year suspended sediment record, export estimate, synthetic inputs, zircon U-Pb ages and protocol, code, figure scripts, sample identifiers. Named explicitly: 2 of 15 (inversion code, synthetic test data); covered only by the general wording or not at all: 13 of 15 (quota inferred). No data concern persons. | GB-13, GB-20, GB-47, GB-58 |
| PP-07 | P29 | Figure text, labels and typography confirmed at page images (300 and 600 dpi), not only in the extracted text | Observations only in text.json were discarded (split equations, "ce 1/r2" fragments, ligatures in "fluvial", a line-end hyphen inside the Steck et al. DOI). "Low-con dence area" is a missing fi ligature visible in the rendered image. | KK-15, KK-18, KK-24, KK-28, KK-30, KK-32, KK-35; GB-21, GB-26, GB-37 |
| PP-08 | P26 | Scope of declared guarantees | "this stabilization prevents divergence" (l. 312 to 313) is claimed for steepest descent only, so the quasi-Newton zircon run above 8000 mm/y is no gap; "the inversion respects geological boundaries" (l. 415) is restricted by the text itself to sufficiently distinct fingerprints; "minimizing the influence of absolute intensity differences" (l. 264) see GB-19. Disclosed: spillover (l. 414 to 415). | GB-19, GB-44; otherwise no finding |
| PP-09 | P3 | Map scale between Fig. 4 and the geology inset of Fig. 15 | Fig. 4: catchment 892 100 px, scale bar 1 km = 110 px at 300 dpi, area 73.7 km². Fig. 15 inset: 137 896 px, 2 km = 85 px, area 76.3 km². Difference 3.5 %, within the scale-bar uncertainty of about 5 % in area. | no finding |
| PP-10 | P27 | Where unchecked components flow into results | Hyperparameters tuned on the synthetic truth flow into all natural runs (l. 426 to 428, l. 444 to 445); inferred geology under ice defines A (l. 270 to 272); the substituted MR g-g zircon fingerprint flows into the zircon and combined runs and the JS values 0.48 and 0.57 (l. 448); the per-sample maximum normalisation flows into every natural XRD result; the undefined low-confidence criterion steers which cells a reader discounts. Disclosed: missing zircon data, inferred geology. | GB-19, GB-22, GB-32, GB-48, GB-49, GB-52 |
| PP-11 | P19 | Provenance class under each core claim | 7 core claims (convergence and accuracy; degradation ranking; hyperparameter choice; fingerprint match; subcatchment attribution; zircon comparison; cost efficiency). Model-generated data only: 3 of 7 (42.9 %); primary XRD with an interpreted map: 3 of 7 (42.9 %), one of them also on unpublished zircon data; no data: 1 of 7 (14.3 %). Synthetic data are named as synthetic (l. 280) and the zircon source as a master's thesis (l. 424, l. 522 to 523). | GB-01, GB-22; otherwise no finding |

### Segment 3: Results, Figures 5 to 16 (p. 10 to 15)

#### Substantive findings

**GB-24 The synthetic validation uses one truth with a single hotspot, noise-free data from the same forward model and a prior at the true mean, and it ranks degradation factors from ranges that are not comparable.**

| Field | Content |
|---|---|
| Check | P9, P10, P21 |
| Location | p. 10, l. 288 to 295; p. 11, l. 325 to 338; p. 12, l. 348, l. 357 to 358, l. 363 to 365; p. 15, l. 456 to 461; Fig. 5a (p. 26); Figs. 7 to 9 (p. 28 to 30) |
| Quotation | "To validate our inversion model, we generate synthetic detrital data using the forward model applied to a “true” erosion rate map featuring a localised hotspot with elevated erosion intensities" / "To summarize, among the three tested scenarios, the strongest impact on the posterior solution arises from reduced fingerprint distinctiveness. Geological map uncertainty follows as the second most influential factor." |
| Concern | (a) All synthetic results use one true map with one hotspot (Fig. 5a); no noise on d or on A is described, and the data come from the same forward model and grid used for the inversion, which favours recovery. (b) The prior equals the average true erosion rate (l. 295, l. 326). (c) The ranking compares three maps (area mismatch 0, about 6.9 and about 11.5 km², Fig. 7) with 20 blending steps down to JS 0.225 and with 1 to 21 tracers, without a common scale; it depends on how far each factor was pushed. On the plotted values, the largest increase of the summed error over the baseline of about 197 is about 78 (39.6 %) for the map scenario (275, Steck et al. map) and about 151 (76.6 %) for the tracer scenario (348.1 at 2 tracers, measured by AB), and the uncertainty spans about 0.008 against about 0.22, so the order of the second and third factor reverses on these readings. (d) With three maps the error is not monotonic in the mismatch (about 197, 193, 275), so the general statement in l. 337 to 338 rests on one rising and one falling step. Decision on a disagreement between instances: AB found that the text matches Fig. 7 (PP-17), SD found the statement unsupported. At the page image both hold: the text names the exception ("Surprisingly", l. 338) but keeps the general rule. The ranking enters the recommendations in l. 456 to 461; hence major. |
| Suggestion | Add to Section 4.1 an ensemble of true maps (several hotspot positions and sizes, multiple hotspots, a random smooth field), noise on d and on A at the level of measured replicate scatter, a prior from a perturbed export estimate, and at least 10 maps spanning the mismatch range in Scenario 1. Express the three factors on a common, normalised scale before ranking them (for example area mismatch as share of the catchment), or withdraw the ranking in l. 363 to 365 and l. 456 to 461 and report the effects per scenario. |
| Status | verified (single truth, no noise described, prior, ranking statement); inferred (readings and percentages) |
| Severity | major |
| Source | SD, S3 |

**GB-25 The resolution diagonals plotted in Figures 5d, 6d and 14 to 16 lie at 0.90 to 1.00 for about 820 cells, which is incompatible with a resolution operator built from 13 to 34 tracers and with the uncertainties shown in the same figures.**

| Field | Content |
|---|---|
| Check | P3 |
| Location | Fig. 5 panels (d) and (h) (p. 26); Fig. 6 panel (d) (p. 27); Figs. 14 to 16, panel "Resolution diagonal" (p. 35 to 37); p. 8, l. 230 to 236 (eq. 21); p. 14, l. 435 to 437 |
| Quotation | "Where the diagonal of R is close to 1, data have improved our knowledge considerately relative to the prior." |
| Concern | Resolution maps are a useful addition, since resolution is one of three metrics for judging reliability (Section 3.3; l. 483). The plotted values cannot be those of the stated operator under the linearisation the manuscript adopts. (1) Fig. 5d colour bar runs from 0.90 to 1.00; margin cells without hillshade measure #0c0c24 against #04040c at the top of the bar, about 1.00; in Fig. 14 the margin cells equal the top of the bar (1.0). Most interior cells are the same dark grey. (2) Cells: catchment area 73.7 km² (Fig. 4, PP-09) divided by 0.09 km² per 300 m pixel gives about 819 cells; a raster count in Fig. 5d gives about 883. (3) With eq. 20, R = C̃m Gᵀ Cd⁻¹ G = I minus C̃m Cm⁻¹; its rank is at most the number of tracers m and its eigenvalues lie between 0 and 1, so trace(R) is at most 21 (synthetic and XRD), 13 (zircon) or 34 (combined). The figures imply a trace of at least 0.90 × 819 ≈ 737, which exceeds these bounds by factors of 35, 57 and 22 (Python). (4) R near I implies a normalised posterior uncertainty near 0, but the same figures show 0.742 (Fig. 5h) and 0.82 to 0.87 (Figs. 14 to 16). (5) l. 437 calls the zircon result "low resolution" while Fig. 14 shows 1.0 for almost all cells. How R was computed is not stated, so the cause is open (a different definition, a colour-scale error or a computation error). The grade is major because resolution is one of the three metrics on which the reliability claims rest. |
| Suggestion | State in Section 3.3 the formula by which R is computed from G, Cd and Cm, report trace(R) per inversion next to the normalised uncertainty, redraw Figs. 5d, 6d and 14 to 16 from that formula, and reconcile l. 437 with Fig. 14. Question to the authors: which quantity is plotted as "Resolution diagonal"? |
| Status | verified (colours measured, cell count); inferred (trace bound, incompatibility); assumption (cause of the discrepancy, posed as a question) |
| Severity | major |
| Source | AB |

**GB-26 Quantities and units are missing on several axes and colour bars of Figures 5, 6 and 11.**

| Field | Content |
|---|---|
| Check | P29 |
| Location | Fig. 5 panels (a), (b), (c), (e) (p. 26); Fig. 6 panels (a), (b), (c), (e), (g), (h), (i) (p. 27); Fig. 11 (p. 32) |
| Quotation | "Trace(post. cov.)" |
| Concern | (1) The erosion colour bars of Figs. 5 and 6 (panels a, b: 0.5 to 3.0; c: difference) carry no unit, whereas Figs. 14 to 16 give mm/y; the covariance in panel (e) has no unit. (2) Fig. 6 panels (g), (h) and (i) have no x-axis labels, (i) lacks the multiplier of the data misfit, and its colour bar has no title, while Fig. 5 has "Iteration", "Data misfit" and "1e8". (3) Fig. 11 has no value axis, no scale and no column headings; the column order is given only in the caption. The unit and symbol of the summed error are treated in GB-36, the trace labels on normalised values in GB-17. |
| Suggestion | Add quantity and unit to every axis and colour bar of Figs. 5 and 6, complete the axis labels of Fig. 6, and add column headings and a 0 to 1 scale to Fig. 11. |
| Status | verified (page images and vector text) |
| Severity | minor |
| Source | AB |

**GB-27 Inversion settings are reported for some tests and missing for others, including the steepest descent run, whose normalised update appears only in the Results.**

| Field | Content |
|---|---|
| Check | P11, P17, P35 |
| Location | p. 10, l. 293 to 295; p. 8, l. 213 to 216 (eq. 18); p. 11, l. 310 to 321; p. 11, l. 324 to 326; p. 12, l. 367 to 371; p. 13 to 14, l. 402 to 418; p. 14 to 15, l. 426 to 428, l. 444 to 445 |
| Quotation | "we use the QN approach with 100 iterations" / "In initial experiments, the steepest descent approach proved unstable, requiring the normalization of the gradient." |
| Concern | Tests against the settings named in l. 324 to 326 (scheme, iterations, L, σm, σd, prior, step size): quasi-Newton test, step size missing; steepest descent test, none of the settings given, neither the iteration count (the axis of Fig. 6g to 6i ends at 200; "visible after 125 iterations", l. 316) nor the step size; the gradient normalisation is described only in Section 4.1.2, while eq. 18 in Section 3.2 shows the unnormalised update, and the "initial experiments" are not reported; parameter sweeps, the values held fixed in each sweep are not stated; natural known-mixture experiment, no setting at all; zircon case, all settings; XRD and combined, "the same". The two schemes are therefore compared at unknown and probably different iteration counts; the accuracy comparison itself is GB-30. |
| Suggestion | Write the normalised steepest descent update in Section 3.2 as used; add a settings table to Section 4 with one row per test (quasi-Newton, steepest descent, Scenarios 1 to 3, each sweep, known mixture, zircon, XRD, combined) and columns for scheme, iterations, L, σm, σd, prior, step size and gradient normalisation. |
| Status | verified (text at the page images) |
| Severity | moderate |
| Source | S3, SD |

**GB-28 Key counts of the set-up are not stated and must be derived by the reader.**

| Field | Content |
|---|---|
| Check | P22 |
| Location | p. 10, l. 294; p. 13, l. 393; Fig. 11 caption (p. 32); Figs. 14 and 16 (p. 35, 37) |
| Quotation | "a smoothing distance of 4 times the pixel size (L = 1200 m)" |
| Concern | The pixel size follows only from 1200 / 4 = 300 m; the number of source units (7) only from counting the Fig. 11 caption; the number of zircon age bins (13, contiguous from 40 to 800 Ma) only from counting the Fig. 14 labels; the number of tracers of the combined run (21 + 13 = 34) only from two figures. The number of pixels, and hence the ratio of unknowns to data behind "underdetermined" (l. 170 to 172), is not derivable from the text; AB estimated about 819 to 883 cells by measuring figures (GB-25). These counts are needed to read the JS averages, the summed errors (GB-36) and the degree of underdetermination. |
| Suggestion | State in Section 4 the pixel size, the number of pixels, the number of source units and the number of tracers in each run (21 XRD, 13 zircon, 34 combined). |
| Status | verified (text and labels); inferred (derived counts) |
| Severity | minor |
| Source | S3 |

**GB-29 Several steps that build the synthetic tests cannot be rebuilt from the text.**

| Field | Content |
|---|---|
| Check | P8 |
| Location | p. 10, l. 294 (Fig. 5k); p. 11, l. 330 to 334; p. 12, l. 343 to 347, l. 355 to 357 |
| Quotation | "We perform a Principal Component Analysis (PCA) to retain the subset of tracers that explain the maximum variance in the mineralogical fingerprints." |
| Concern | Not described: how the synthetic fingerprints of Fig. 5k were generated; how the "geological map with minimal difference" was produced; the blending formula behind "approaching each lithology's mineral concentration to its mean" (l. 343 to 344) and its 20 steps; how a PCA, which yields components, is turned into a ranking of individual tracers; on which normalisation the JS distance is computed, given that fingerprints are scaled 0 to 1 by their maximum (l. 261 to 262) and are not probability distributions. The undefined low-confidence criterion is treated in GB-52. |
| Suggestion | Add to Section 4.1.3 the formulas for blending, map modification and tracer ranking and the normalisation used for JS, and describe the generation of the synthetic fingerprints in Section 4.1.1. |
| Status | verified (absence) |
| Severity | moderate |
| Source | SD |

**GB-30 Figures 5g and 6g show the steepest descent run ending with a smaller total error than the quasi-Newton run, while the text adopts quasi-Newton as the more accurate scheme.**

| Field | Content |
|---|---|
| Check | P3 |
| Location | p. 11, l. 314 to 316, l. 320 to 321; Fig. 5 panels (c) and (g) (p. 26); Fig. 6 panels (c) and (g) (p. 27); Fig. 10 row 5, column 1 (p. 31) |
| Quotation | "we adopt the Quasi-Newton (QN) approach for all subsequent tests, as it provides a more stable and accurate reconstruction of the erosion rate patterns." |
| Concern | Running both schemes on the same synthetic map with the same diagnostics makes the comparison direct. The measured end points (600 dpi, calibration error 1 px) favour steepest descent in the accuracy metric the figures show: Fig. 5g (quasi-Newton, 100 iterations) ends at 201.0 ± 0.3 with a minimum of 197.3 ± 0.3 at iteration 22; Fig. 6g (steepest descent, 200 iterations) ends at 193.0 ± 0.4, which is 8.0 below the quasi-Newton end value and 4.3 below its minimum. More quasi-Newton iterations do not close the gap: Fig. 10 row 5 gives 200.9 ± 0.1 at 195 iterations. The colour bars of the difference maps also differ (Fig. 5c ends at ±2.39, Fig. 6c at ±1.75); if their limits are the largest absolute difference, the quasi-Newton map also has the larger local error, against "sharp features ... are smoothed out or missed (Figure 6C)". This interpretation of the colour bar limits is an assumption and is put as a question. Faster convergence of quasi-Newton is visible (plateau after about 20 against about 136 iterations), higher accuracy is not. The grade is major because the choice of scheme for all later tests is a stated result of Section 4.1. |
| Suggestion | In Section 4.1.2 state the end values of the summed absolute difference for both schemes, plot Figs. 5c and 6c on one colour scale, and base the choice of quasi-Newton on convergence speed and stability, or show a metric in which it is more accurate. |
| Status | verified (end values measured); assumption (meaning of the colour bar limits, posed as a question) |
| Severity | major |
| Source | AB |

**GB-31 The oscillation of the posterior covariance after 125 iterations is not visible in Figure 6, and the reference "Figure 6G versus Figure 6G" compares a panel with itself.**

| Field | Content |
|---|---|
| Check | P3, P4 |
| Location | p. 11, l. 316 to 317; Fig. 6 panels (g) and (h) (p. 27) |
| Quotation | "This limited sensitivity to strong gradients also leads to oscillations in the posterior covariance, visible after 125 iterations, as the Jacobian fluctuates between iterations (Figure 6G versus Figure 6G)." |
| Concern | Panel (g) shows the error, not the covariance, which is in panel (h). At 600 dpi panel (h) rises monotonically to a kink at iteration 136.2 ± 0.2 and then decreases slightly and smoothly (less than one tick interval of 0.002), without visible oscillation; panel (g) shows the same kink. Oscillations smaller than about 1 px cannot be excluded. The instances proposed different repairs of the reference ("Figure 6H versus Figure 5H" by S3, S4 and AB; "Figure 6H" or "Figure 6G versus Figure 6H" by SD), so the intended panels cannot be decided from the manuscript. |
| Suggestion | Correct the reference to the panels meant and either show the oscillation (for example an inset of panel h after iteration 125 with an expanded axis) or describe the curve as a kink followed by a plateau. |
| Status | verified (page image at 600 dpi) |
| Severity | moderate |
| Source | AB, S3, S4, SD |

**GB-32 The hyperparameters are said to be optimised, but the values used differ from those marked in Figure 10, and the selection relies on a known truth that natural data lack.**

| Field | Content |
|---|---|
| Check | P2, P29, P5, P10 |
| Location | p. 11, l. 324 to 326; p. 10, l. 293 to 295; p. 14, l. 426 to 428; p. 3, l. 70 (repeated p. 5, l. 137); p. 13, l. 388 to 389; Fig. 10, column 3, rows 1 to 5, annotations and thick circles (p. 31) |
| Quotation | "Through forward-inverse testing, we optimize the hyper-parameters" / "a smoothing distance of 4 times the pixel size (L = 1200 m), a model standard deviation of 3, a data standard deviation of 0.01 mm/y" |
| Concern | (a) Each trade-off panel of Fig. 10 highlights one point with a label: "L = 3000 m", "σm = 6.2", "σd = 0.003 mm/y", "μ = 0.1", "n_m = 25". Only μ = 0.1 and n_m = 25 match the values used in Sections 4.1.3 and 4.2.2; 3000 m matches the over-smoothing threshold of l. 373; σm = 6.2 and σd = 0.003 mm/y match no value in the text. Neither caption nor text says whether the marks are optima, chosen values or knees of the curve. (b) The tests use 25 iterations although "posterior solutions evolve only minimally after the 115th iteration" (l. 388 to 389); 25 is 22 % of 115. (c) The selection criterion is the difference to the true map, which cannot be computed for natural data; transferring the synthetic optimum to the Gornergletscher assumes that the single synthetic hotspot represents the natural pattern. The edge of the L sweep at 3000 m is treated in GB-39. |
| Suggestion | Explain the highlighted points in the Fig. 10 caption; in Section 4.1.4 state the criterion for "optimal", list the chosen values and justify where they differ from the marked ones; for the natural data add a criterion that does not need the truth (for example an L-curve, the discrepancy principle or cross-validation over detrital samples) and show that the natural results are stable across the plausible range. |
| Status | verified (annotations at the page image and in the vector text); inferred ((b), (c)) |
| Severity | moderate |
| Source | S3, AB, SD |

**GB-33 The quantity that grades the maps of Scenario 1 has three names, and the maps carry different names in text and Figure 7.**

| Field | Content |
|---|---|
| Check | P38 |
| Location | p. 11, l. 330, l. 332 to 336; p. 11 to 12, l. 338 to 340; Fig. 7, panel titles, x-axes, colour bar and caption (p. 28) |
| Quotation | "is quantified by area mismatch (expressed in m2) between the lithological unit boundaries" / "Surprisingly, a simplified geological map with minimal changes from the truth" |
| Concern | One quantity, three names: "area mismatch" (l. 330, 334, 335), "Area difference" (Fig. 7 axes and caption), "Geology misalignment (m²)" (Fig. 7 colour bar). The three maps are named "the same geological map", "a geological map with minimal difference", "the map proposed by (Steck et al., 2015)" (l. 332 to 334), "a simplified geological map with minimal changes" and "the original geological map" (l. 338 to 339), and in Fig. 7 "Originial geology (same as forward)", "Forward geology", "Geology with minimal changes", "Minimal changes", "Geology by Steck et al. 2015". "Simplified" appears only in l. 338 and suggests a different kind of change than "minimal changes". |
| Suggestion | Use "area mismatch (m²)" in the Fig. 7 caption, axes and colour bar; name the three maps once in l. 332 to 334 and use these names in l. 338 to 339 and in Fig. 7; drop or explain "simplified". |
| Status | verified (page images 11, 12, 28) |
| Severity | minor |
| Source | S2 |

**GB-34 Figure 8 plots 14 of the 20 blending cases; the caption accounts for one, and between JS 0.44 and 0.55 the error does not rise as described.**

| Field | Content |
|---|---|
| Check | P23, P3, P34 |
| Location | p. 12, l. 348 to 353; Fig. 8, left and middle scatterplots and caption (p. 29) |
| Quotation | "In total, 20 values between the highly blended and the original synthetic fingerprints are tested" / "In many of these cases, the inversion fails to converge to a stable posterior solution." / "Note that the most blended example did not have a stable solution and is therefore not plotted." |
| Concern | Three instances counted 14 markers in each scatterplot. Balance: 20 tested minus 1 explained = 19, against 14 plotted, so 5 runs are unaccounted; "many" is not quantified. AB measured the marker positions at JS = 0.249, 0.272, 0.338, 0.359, then 0.441 to 0.624 in steps of about 0.020 (± 0.0004). S3 had inferred the missing runs from an assumed even grid of step 0.021 between 0.225 and 0.624; the measured positions do not lie on that grid (0.441 against 0.435, 0.461 against 0.456), so the grid assumption is not adopted and the missing JS values cannot be read from the figure. Measured errors (± 700): 47 200, 676 800, 5 800 and 322 000 below JS 0.44; 800, 1 000 and 700 at 0.441 to 0.481; 8 700, 3 800 and 19 400 at 0.501 to 0.541; 300, 300 and 200 at 0.561 to 0.624. Between 0.44 and 0.48 the error is not distinguishable from the unblended case, and the rise below 0.55 is not monotonic; the posterior uncertainty does jump between 0.541 (0.842) and 0.561 (0.747) (PP-20). If the missing runs are the non-converged ones, the plotted curve is selected by outcome. |
| Suggestion | In l. 352 to 353 and in the Fig. 8 caption state how many of the 20 runs did not converge, at which JS values, and the convergence criterion; mark non-converged runs in the plot; plot the error on a logarithmic axis; revise l. 351 to 353 so that the thresholds match the plotted values. |
| Status | verified (counted and measured) |
| Severity | moderate |
| Source | S3, AB, SD |

**GB-35 The JS threshold derived in the synthetic tests is not applied to the natural XRD fingerprints, so "sufficiently distinct" cannot be checked.**

| Field | Content |
|---|---|
| Check | P5 |
| Location | p. 12, l. 351 to 353; p. 14, l. 415 to 416; p. 15, l. 447 to 448 |
| Quotation | "As the JS distance decreases below 0.55, both absolute error and posterior uncertainty rise sharply" / "when the XRD fingerprints provide sufficiently distinct signals" |
| Concern | The manuscript sets a rule from Scenario 2. For the natural data it reports JS for zircon (0.48, below 0.55) and for the combined set (0.57, above), but not for the XRD-only fingerprints on which Section 4.2.1 relies. The synthetic fingerprints had JS 0.624 (Fig. 8), so whether the natural case lies in the tested range is unknown; identical tracers in the natural fingerprints (GB-42) would also change the value. |
| Suggestion | In Section 4.2 report the average JS of the natural XRD fingerprints (Fig. 11) and place the three natural datasets on the axis of Fig. 8. |
| Status | verified |
| Severity | moderate |
| Source | SD |

**GB-36 The error metric is a sum over pixels, but the text gives it a rate unit and a value that differs from the plotted values by orders of magnitude.**

| Field | Content |
|---|---|
| Check | P20 |
| Location | p. 12, l. 352; Fig. 5g and Fig. 6g (p. 26, 27); Figs. 7 to 9, left scatterplots (p. 28 to 30); Fig. 10, column 1 (p. 31) |
| Quotation | "with errors exceeding 700 mm/yr for JS < 0.44" |
| Concern | All figures plot the sum of absolute differences between true and posterior erosion rates over all pixels; the text calls it "absolute error" (l. 335, 352, 361) and attaches mm/yr, which reads as a rate per pixel. The symbol e on the axes is not defined, so the reader cannot tell whether it is the erosion rate or its logarithm ε, and no axis gives a unit. The number of pixels is not stated (GB-28), so the sum cannot be converted to a mean error per pixel and compared with true rates of 0 to 3 (Fig. 5a). For JS below 0.44 the measured sums are 5 800 to 676 800 (GB-34), one to three orders of magnitude above 700; the top tick of Fig. 8 is 700 000, a factor of 1000 above the value in the text, which suggests either a conversion or a different quantity. |
| Suggestion | Define the error metric in Section 3.3 or 4.1 (sum or mean over pixels, erosion rate or log rate, unit), state the number of pixels, and report errors in the text in the same quantity as in the figures, preferably as mean absolute error per pixel in mm/y. |
| Status | verified (text and axis labels at the page images); inferred (factor) |
| Severity | moderate |
| Source | S3, AB |

**GB-37 The x-axes of the two left scatterplots in Figure 9 are labelled as JS distance but show the number of tracers.**

| Field | Content |
|---|---|
| Check | P29 |
| Location | Fig. 9, scatterplots "Absolute error" and "Posterior uncertainty" (p. 30) |
| Quotation | "Avg. JS distance between lithologies" |
| Concern | The tick labels run from 0.0 to 20.0 and the 21 markers lie at 1 to 21 (measured), which are tracer counts as in the caption and in l. 357 to 359. The label is carried over from Fig. 8. A second "Σ" stands below the y-axis label of the left panel. S2, S3 and SD noted the same label outside their checklists. |
| Suggestion | Label both x-axes "Number of tracer minerals" with integer ticks and remove the stray "Σ". |
| Status | verified (page image) |
| Severity | minor |
| Source | AB |

**GB-38 The text in Figure 10 is set at about 5 pt in print.**

| Field | Content |
|---|---|
| Check | P3 |
| Location | Fig. 10, all panels (p. 31) |
| Quotation | "Smoothing distance (m)" |
| Concern | From the vector text, tick labels in Fig. 10 have a box height of 4.8 pt and axis titles 5.7 pt, against 7.7 pt in Figs. 8 and 9 and 10.7 pt in Fig. 13. Fifteen panels on one page reduce every label to the edge of legibility; offsets such as "+1.974e2", on which the reading of row 3 depends (GB-39), are smaller still. |
| Suggestion | Split Fig. 10 into two figures or use full page width with fewer columns, so that labels reach the size used in Figs. 8 and 9. |
| Status | verified (measured) |
| Severity | minor |
| Source | AB |

**GB-39 Statements of Section 4.1.4 on the parameter sweeps describe features that Figure 10 does not show.**

| Field | Content |
|---|---|
| Check | P3, P21, P11 |
| Location | p. 12 to 13, l. 372 to 389; p. 10 to 11, l. 306 to 307; Fig. 10, row 1 column 1, row 3 columns 1 and 3, row 5 column 1 (p. 31); Fig. 5h (p. 26) |
| Quotation | "However, beyond approximately 10 times the pixel size (3000 m), the solution becomes overly smooth, causing the posterior to deviate from the true erosion rates." / "As data standard deviation increases, the absolute difference first decreases to a minimum, then rises to a plateau at higher values." / "Only when the maximum number of non-linear steps is reduced below 25 does the posterior fail to converge to the true erosion map." |
| Concern | Sweeping five hyperparameters with the same diagnostics is useful for transfer. Measured at 600 dpi: (a) Row 1: 20 values of L from 199.7 to 3000 m; the summed difference falls monotonically from 256.9 to 76.2 at 3000 m. No value beyond 3000 m is plotted, so the over-smoothing "beyond 3000 m" is not shown, and the next sentence (l. 374 to 376) says that a longer smoothing distance reduces the difference, which contradicts the deviation claimed in l. 373 to 374. At L = 1231 m, the value nearest the 1200 m used in all tests, the difference is 194.9, 2.6 times the value at 3000 m. (b) Row 3: the axis carries the offset "+1.974e2"; all points lie between 197.4197 and 197.4432, a span of 0.023 or 0.012 % (Python), rising monotonically; there are no "large differences" at low σd (l. 380 to 381), no minimum and no plateau. The model misfit spans 1.56142 to 1.56232 (0.058 %), not a rapid decrease (l. 383 to 384). Across the tested range the posterior is practically insensitive to σd, and the offered explanation "overfitting or unstable gradients" refers to a change that may lie within numerical precision. (c) Row 5: 268.8, 200.9, 197.6, 199.7, 200.6, 201.0 at 5, 15, 25, 35, 45, 55 iterations, and 200.9 at 195; the run with 15 iterations reaches the value of the run with 195, so the threshold lies between 5 and 15, not at 25. (d) l. 306 says the posterior covariance "follows a similar trend" as the error, but the error falls (Fig. 5g) while the covariance rises (Fig. 5h). Decision on a disagreement between instances: S3 also objected to "rises steeply" for a rise of about 1.3 % in Fig. 5h, while AB found the curve shape in line with the text (PP-12); at the page image the curve does rise steeply in the early iterations on its own axis, so only the "similar trend" wording is kept. The grade is major because these sensitivity statements are results of Section 4.1.4 and support the robustness claim (GB-02). |
| Suggestion | Rewrite l. 372 to 389 and l. 306 to 307 from the plotted values; extend row 1 beyond 3000 m if the over-smoothing claim is kept and reconcile l. 373 to 374 with l. 374 to 376; plot row 3 with a logarithmic x-axis and without offset notation and state that the result is insensitive to σd over the tested range; give the iteration threshold as observed. |
| Status | verified (measured); inferred (relative changes, calculation) |
| Severity | major |
| Source | AB, S3 |

**GB-40 The convergence threshold for the iteration count has no stated reference, and the record it rests on is not shown.**

| Field | Content |
|---|---|
| Check | P20 |
| Location | p. 13, l. 388 to 389; p. 9, l. 243 to 244; Fig. 10, row 5 (p. 31) |
| Quotation | "Beyond 115 iterations, the change in data misfit between successive steps falls below" |
| Concern | The data misfit in Fig. 10 is of the order 1e6 to 1e8 (axis multipliers), so an absolute change below 10⁻⁵ would be a relative change of about 1e-11 or less; a relative criterion would mean a different stopping point. The text does not say which applies, and the stopping rule in l. 243 to 244 ("when the data-misfit stops decreasing") is a third criterion. No figure shows the misfit change per iteration. |
| Suggestion | State whether the threshold is absolute or relative, which criterion (l. 243 to 244 or l. 388) was used in the reported runs, and show the change per iteration, for example in a supplement. |
| Status | verified (text and axis multipliers); inferred (order of magnitude) |
| Severity | minor |
| Source | S3 |

**GB-41 One of the 21 tracer minerals is called "Chrysolite" in the text but "Chrysotile" in all figures, which leaves open which reference spectrum defines its window.**

| Field | Content |
|---|---|
| Check | P38, P2 |
| Location | p. 13, l. 395; p. 10, l. 274; Fig. 11, y-axis (p. 32); Fig. 15, x-axis (p. 36); Fig. 16, x-axis (p. 37) |
| Quotation | "Fayalite, Dolomite, Diopside, Chrysolite, Antigorite, Anorthite" / "serpentinites (predominantly antigorite and chrysotile)" |
| Concern | The text list (l. 393 to 396) and the figure axes contain 21 minerals each and agree in content, except at one position (Python set difference: text minus Fig. 11 = Chrysolite, Fig. 11 minus text = Chrysotile). The two names denote different minerals: chrysolite is a name for an Mg-rich olivine, chrysotile a serpentine mineral, and l. 274 names chrysotile as a main constituent of the serpentinites, which suggests a misspelling. Since the 2θ windows are taken from RRUFF reference spectra by mineral name (l. 257 to 258), the question matters for reproducing the tracer. Five instances reported this independently. |
| Suggestion | Confirm which mineral and which RRUFF entry define this window and correct l. 395 (or the figures); list the RRUFF identifiers of all 21 reference spectra in Section 3.4 or a supplement. |
| Status | verified (naming at page images 13, 32, 36, 37); assumption (whether a wrong reference spectrum was used, posed as a question) |
| Severity | moderate |
| Source | S2, S3, S4, AB, SD |

**GB-42 In Figure 11 several pairs and triples of minerals have identical bar lengths in almost every lithology, so the 21 mineral windows do not yield 21 independent tracers.**

| Field | Content |
|---|---|
| Check | P3 |
| Location | Fig. 11, all seven columns (p. 32); Fig. 15 fingerprint panel (p. 36); p. 9, l. 259 to 260; p. 13, l. 393 to 398; p. 16, l. 475 to 476 |
| Quotation | "Sixth, to mitigate peak overlap, we average the total peak area within the 2θ windows corresponding to each mineral, rather than relying on individual peaks." |
| Concern | Bar lengths in Fig. 11 were measured per column colour at 300 dpi (longest bar per column 242 to 243 px). Annite, muscovite and phlogopite: 130/130/130, 74/74/74, 136/136/136, 51/42/51, 160/160/160, 131/131/131, 0/0/0 px in the seven columns. Anorthite and pyroxene: 34/34, 243/243, 92/92, 243/243, 6/6, 103/103, 0/0. Ankerite and dolomite: 3/3, 44/44, 6/3, 34/34, 0/0, 6/6, 0/0. Fig. 15 confirms this independently at 600 dpi: phlogopite and annite have identical segment lengths (180, 329, 19, 198, 38, 146 px), as do anorthite and pyroxene. Identity to the pixel in six or seven of seven lithologies is not plausible for independent minerals and indicates that the windows of these minerals select the same peaks; S2 noted separately that "Pyroxene" is listed beside the pyroxene species diopside and omphacite. The tracer matrix A then has at most about 17 distinct rows for the natural XRD data, and the claim that averaging over windows reduces peak overlap (l. 475 to 476) is not borne out for these groups. This affects the JS distances and the transfer of the tracer-count result of Section 4.1.3 (7 tracers suffice) to natural data. The grade is major because the number and distinctness of the XRD tracers is the basis of the main claim. |
| Suggestion | In Section 3.4 list the 2θ windows per mineral and state which minerals share windows; merge identical tracers or report the rank of A; recompute the natural inversions and JS distances with distinct tracers only. |
| Status | verified (bar lengths measured); inferred (shared windows as cause) |
| Severity | major |
| Source | AB |

**GB-43 Validation question 1, agreement of the fingerprints with the expected mineralogy, is answered without a criterion and partly by construction, and Figure 11 shows little garnet or omphacite in units described as garnet-bearing or eclogitic.**

| Field | Content |
|---|---|
| Check | P10, P31, P9, P3 |
| Location | p. 13, l. 399 to 401; p. 13, l. 393 to 394; p. 10, l. 273 to 277, l. 282 to 283; Fig. 11, rows Almandine and Omphacite (p. 32); Fig. 4 legend (p. 25); Fig. 15 fingerprint panel (p. 36) |
| Quotation | "The mineralogical fingerprints derived from processed and binned XRD data align well with established knowledge of the lithology in the Gorner Glacier catchment (Bearth, 1953; Steck et al., 2015)" / "we focused on a set of 21 minerals expected to be characteristic of the main lithologies in the catchment" |
| Concern | "Align well" has no criterion, no table of expected against measured minerals per unit and no agreement measure. Because the mineral list was chosen by expectation and window areas are non-zero for any phase with peaks there, agreement is partly built in. The manuscript itself names garnet as characteristic of the Monte Rosa gneiss and micaschist (l. 276; Fig. 4 legend "garnet-bearing silimanite-biotite gneiss", "garnet micaschist") and of the Stockhorn, Tuftgrat and Gornergrat units (l. 277), and eclogites in the ZSF metabasite unit (l. 274). Measured normalised bar lengths (maximum 1): almandine 0.029 (Monte Rosa gneiss), 0.082 (Stockhorn, Tuftgrat, Gornergrat), 0.095 (ZSF metabasites); omphacite 0.053 in the ZSF metabasite and eclogite unit, while quartz, micas and tremolite reach 0.5 to 1.0 in the same columns. Possible causes are the normalisation by the maximum peak (l. 261, GB-19), weak or overlapping garnet reflections, or sampling; further distributions in Fig. 15 (fayalite in the serpentinites, talc and magnesite in the metabasites) rest on general mineralogical knowledge and are put as questions. The conclusion "robustness of the cleaning and binning approach" and "validity of the input data" (l. 400 to 401) does not follow from a qualitative match. The grade is major because the finding concerns validation question 1. |
| Suggestion | Add to Section 4.2 a table of expected main minerals per unit against measured relative peak areas with an agreement measure (for example the share of correct presence or absence calls); determine the mineralogy of the same source samples independently (Rietveld refinement or point counting); discuss the low almandine and omphacite values. Question to the authors: how do you explain the omphacite, fayalite, talc and magnesite distributions? |
| Status | verified (no criterion, no table; bar lengths measured); inferred (construction effect; divergence from the lithology descriptions); assumption (individual mineral distributions and causes, posed as questions) |
| Severity | major |
| Source | SD, AB |

**GB-44 The natural known-mixture test has one negative control that it cannot distinguish from present units, and it does not evaluate the spatial attribution it sets out to test.**

| Field | Content |
|---|---|
| Check | P10, P9, P32, P34, P3, P20 |
| Location | p. 13 to 14, l. 402 to 418; p. 10, l. 283 to 284, l. 299 to 300; Fig. 13 and caption (p. 34); Fig. 12 (p. 33) |
| Quotation | "to test if sediment samples from a subcatchment are attributed only to lithologies present within the subcatchment boundaries" / "Some spillover occurs from adjacent lithologies, but the overall pattern confirms that the inversion respects geological boundaries when the XRD fingerprints provide sufficiently distinct signals." |
| Concern | Designing a natural test without restricting A deserves credit. However: (a) only one of seven units, the ZSF sediments, is absent (l. 411), and it is one of the small units the manuscript says are "under-represented" with "lower resolution" (l. 299 to 300). (b) KDE peak positions measured at 300 dpi (x-axis calibrated on the label centres, ± 0.009 mm/y): ZSF sediments 0.00, Furgg series 0.00, Monte Rosa granite 0.03, ZSF serpentinites 0.03, ZSF metabasites 0.23, Stockhorn, Tuftgrat, Gornergrat flat between 0.77 and 1.17, Monte Rosa gneiss and micaschist 0.60. The absent unit thus peaks where the Furgg series and the Monte Rosa granite peak, which both crop out in the subcatchment; a peak near zero does not separate absent from present units. (c) The KDEs cover all pixels of each unit in the whole domain (Fig. 13 caption), so erosion placed on pixels of present units outside the subcatchment counts as correct; the highest erosion goes to the Monte Rosa gneiss, whose area in the inset lies mostly south of the dashed boundary. (d) Neither the number of samples nor of inversions ("multiple", l. 413), nor the number of pixels per unit is given; the upper panel has no density scale; "close to zero" has no reference value and the spillover is not quantified. (e) No independent check supports "confirms". The grade is major because this is one of the three natural validations named in l. 282 to 285. |
| Suggestion | In Section 4.2.1 report the share of total posterior erosion attributed to pixels inside and outside the subcatchment per inversion; compare with an inversion whose A is restricted to the subcatchment; give the number and dates of samples and inversions and the pixels per unit, show the individual results and add a density axis to the upper panel of Fig. 13; use further sampling points whose catchments exclude several units; add laboratory known mixtures (GB-19; Andrews and Eberl, 2012, GB-07, is an XRD example). |
| Status | verified (single absent unit, missing counts, caption; peak positions measured); inferred (location of the gneiss unit relative to the boundary, from an inset without grid; spatial share) |
| Severity | major |
| Source | SD, AB, S3 |

**GB-45 Figure 12 is captioned as the subcatchment but does not draw the subcatchment boundary.**

| Field | Content |
|---|---|
| Check | P29 |
| Location | Fig. 12 and caption (p. 33); p. 14, l. 411 to 412 |
| Quotation | "Lithology and outcrops in the Gorner-Grenz confluence subcatchment." |
| Concern | The map shows the whole catchment with the confluence marked by a point; parts of the map are drawn with stronger colours than others, but no boundary and no legend entry explain this. The dashed boundary appears only in the inset of Fig. 13. Without it the reader cannot check which units crop out inside the subcatchment, the condition on which Section 4.2.1 depends. |
| Suggestion | Draw the subcatchment boundary in Fig. 12, explain the faded colours in the legend, and list the outcropping units with their areas inside the boundary. |
| Status | verified (page image) |
| Severity | moderate |
| Source | AB |

**GB-46 The natural erosion maps combine the composition of single instantaneous samples with an annual export estimate, so the design cannot separate temporal variability of source activation from spatial erosion patterns.**

| Field | Content |
|---|---|
| Check | P9, P10 |
| Location | p. 14, l. 423 to 424, l. 437 to 438; p. 3, l. 65 to 66 (repeated p. 5, l. 132 to 133); p. 1, l. 10 to 11; p. 9, l. 267 to 268; p. 14, l. 413 |
| Quotation | "the detrital sample collected on June 28, 2019, at 13:30" / "an estimate of the total annual suspended sediment export from the catchment" |
| Concern | The natural comparison (Section 4.2.2) rests on one detrital sample taken at one moment; the Gorner-Grenz test merges "multiple detrital samples" (l. 413) without dates. The scaling to absolute erosion rates uses an annual export (l. 65 to 66). A sample taken at 13:30 in late June reflects the sources active at that time, not the annual mean, so the map in mm/y mixes an instantaneous provenance signal with an annual flux. The site was chosen for its "multi-year suspended sediment datasets" (l. 268), which are not used. The framing around "spatio-temporal dynamics" (l. 10) and "the timing of their activation" (l. 13) is not addressed by the design. The grade is major because it affects the meaning of every natural erosion rate map. |
| Suggestion | Invert a time series of detrital samples (for example several samples per day over a melt season, using the record of l. 268), each scaled by the export of its own interval, and report the spread of the maps; or use flux-weighted composite samples for an annual map. Give date, time and discharge of every detrital sample in Sections 4.2.1 and 4.2.2, and state in Section 3.1 that a single sample yields an instantaneous provenance map. |
| Status | verified (single sample, missing dates); inferred (temporal mismatch from the described scaling) |
| Severity | major |
| Source | SD |

**GB-47 The zircon data and their analytical protocol rest on an unpublished master's thesis, and the data statement does not say whether the zircon data or the thesis are accessible.**

| Field | Content |
|---|---|
| Check | P12 |
| Location | p. 14, l. 423 to 425; p. 17, l. 522 to 523; p. 16, l. 490 |
| Quotation | "following the methodology described in (Belotti, 2021)" / "Master’s thesis, University of Lausanne, unpublished master’s thesis, 2021." |
| Concern | The zircon comparison (Section 4.2.2, Figs. 14 and 16) is one of the three natural tests named in l. 284 to 285. The manuscript states openly that the thesis is unpublished. The consequence is not drawn: the only description of grain extraction, dating and age binning is in a document readers cannot obtain, and l. 490 mentions neither the zircon ages nor the thesis. The repository named by the Zenodo record lists zircon data files and a thesis PDF; if these are in the archived release, one sentence in the statement would make them findable. |
| Suggestion | In l. 490 list the zircon source and detrital U-Pb ages and, if permitted, the thesis as archived items; in Section 4.2.2 add the essential protocol details (grains per sample, dating method, laboratory) or point to a supplement. |
| Status | verified (unpublished status, silence of the statement); inferred (presence in the repository, from a file listing, not from the archived release) |
| Severity | moderate |
| Source | S2 |

**GB-48 The zircon-only and combined inversions leave the treatment of one of the seven units open, and the zircon balance of units does not close.**

| Field | Content |
|---|---|
| Check | P23 |
| Location | p. 14, l. 430 to 435; p. 15, l. 443 to 448; Fig. 11 caption (p. 32); Fig. 14 (p. 35); Fig. 16 (p. 37) |
| Quotation | "To compensate for the lack of age data for the MR g-g unit, we assigned the MR g-g unit the same zircon-age fingerprint as the Monte Rosa granite unit." |
| Concern | Balance: 7 source units, 2 without zircon data, 1 substituted, so 6 units with a zircon fingerprint and 1 unit (ZSF metabasites and eclogites) whose treatment is not stated. Fig. 14 shows no metabasite segment in any age bin (PP-29). Possible resolutions: A, its column in the zircon tracer matrix is zero, so the zircon data cannot constrain erosion there; B, the unit is excluded from the zircon matrix, which changes the parameterisation between the zircon, XRD and combined runs; C, a substitute fingerprint was assigned without mention. The choice also determines the average JS distances 0.48 and 0.57 (l. 448): with 7 units there are 21 pairs; under A one fingerprint is not a probability distribution and JS is undefined for its 6 pairs; under B 15 pairs remain; in all cases the substituted pair MR g-g and MR granite has a zircon JS distance of 0. The instability of the zircon-only solution (l. 435) may therefore have at least three causes (the unhandled unit, two identical fingerprints, the low zircon content of the serpentinites, l. 432 to 433); which one applies is a question to the authors. The grade is major because the zircon run is the benchmark of Section 4.2.2. |
| Suggestion | State in Section 4.2.2 how the ZSF metabasite and eclogite unit enters the zircon and the combined matrices, how many unit pairs the average JS distance comprises and how the concatenated vectors are normalised; report a zircon-only run without the substitution, or with both affected units merged, to separate the causes of instability. |
| Status | verified (balance from l. 430 to 434 and the Fig. 11 caption); inferred (resolutions A to C, pair counts); assumption (attribution of the instability, posed as a question) |
| Severity | major |
| Source | S3 |

**GB-49 Figures 14 and 16 show the substituted Monte Rosa garnet-gneiss zircon fingerprint without marking it, and Figure 14 has no legend for the units.**

| Field | Content |
|---|---|
| Check | P37 |
| Location | p. 14, l. 433 to 434; Fig. 14, fingerprint panel and caption (p. 35); Fig. 16, fingerprint panel and caption (p. 37) |
| Quotation | "Posterior erosion rate map using Zr fingerprint data, the resolution for the posterior, the normalized posterior uncertainty" |
| Concern | In the zircon age bins of Figs. 14 and 16 the two Monte Rosa colours appear in equal shares (equal within 1 px in all 11 bins in which they occur, PP-29), consistent with the copied fingerprint, but the captions call them the source fingerprints without saying that one is substituted. Fig. 14 has neither a geology legend nor a fingerprint legend; the colours can only be inferred from Fig. 15. |
| Suggestion | Add to the captions of Figs. 14 and 16 that the MR g-g zircon fingerprint is copied from MR granite and that no zircon data exist for the ZSF metabasites and eclogites; add the unit legend to Fig. 14. |
| Status | verified (equal shares measured, missing legend); inferred (colour assignment via the Fig. 15 legend) |
| Severity | minor |
| Source | SD, AB |

**GB-50 The comparison of the three natural cases gives numbers for some cases and only descriptions for others, and "stability" has no measure.**

| Field | Content |
|---|---|
| Check | P11 |
| Location | p. 14 to 15, l. 435 to 449; Figs. 14 to 16 (p. 35 to 37) |
| Quotation | "Compared to the zircon-only results, the XRD-based posterior shows greater stability." |
| Concern | Section 3.3 announces several metrics (posterior covariance, resolution, normalised covariance, data and model misfit). Reported in the text per case: zircon-only, maximum erosion rate (above 8000 mm/y), resolution only as "low", total normalised uncertainty 0.87, JS 0.48; XRD-only, total normalised uncertainty 0.82 only; combined, 0.86 and JS 0.57. Empty cells: maximum erosion rate for XRD-only and combined, any resolution value for all three, JS for XRD-only, data and model misfit for all three. "Stability" (l. 439, l. 446) is defined by no measure, so the central comparison of Section 4.2.2 rests on one number per case. |
| Suggestion | Add a table to Section 4.2.2 with one row per case and the same columns: number of tracers, average JS distance, maximum and median posterior erosion rate, mean resolution diagonal, total normalised uncertainty, final data and model misfit; define "stability" by one of these columns. |
| Status | verified (text at the page images) |
| Severity | moderate |
| Source | S3 |

**GB-51 The stacked fingerprints of Figure 15 cannot be derived from Figure 11 by normalising each mineral across lithologies, and the manuscript does not say how they were computed.**

| Field | Content |
|---|---|
| Check | P3 |
| Location | Fig. 15, fingerprint panel, bars Quartz and Muscovite (p. 36); Fig. 11, rows Quartz and Muscovite (p. 32) |
| Quotation | "Normalised abundance per mineral or age" |
| Concern | Both figures show the same 21 minerals for the same seven units. In Fig. 11 quartz reaches 1.000 in four units (ZSF sediments, Monte Rosa granite, Monte Rosa gneiss, Furgg); a per-mineral normalisation would give them equal shares (0.209 each). The quartz bar of Fig. 15 (segments measured at 600 dpi, total 910 px) gives 0.175, 0.227, 0.323 and 0.215, a ratio of 1.85 between the largest and smallest share. For muscovite Fig. 11 predicts 0.194, 0.110, 0.203, 0.062, 0.237, 0.194; Fig. 15 shows 0.160, 0.041, 0.219, 0.017, 0.365, 0.199. A reader cannot tell which of the two presentations enters the tracer matrix A. |
| Suggestion | State in the captions of Figs. 11 and 15 (and 5k, 14, 16) how the plotted values are normalised and which values form A; if the two figures stem from different processing, say so. |
| Status | verified (shares measured); inferred (inconsistency) |
| Severity | moderate |
| Source | AB |

**GB-52 The main erosion peak of the XRD solution lies under cells marked "low confidence", and the criterion for these cells is not defined anywhere.**

| Field | Content |
|---|---|
| Check | P29, P8 |
| Location | Fig. 15, panel "Posterior erosion rate" (p. 36); hatched cells also in Figs. 5b, 6b, 14 and 16; p. 14 to 15, l. 440 to 441 |
| Quotation | "the XRD solution identifies the main erosion peak in the center of the domain and a secondary peak in the Monte Rosa granite area." |
| Concern | At 600 dpi the cells with the highest values in Fig. 15 (colour at the top of the 0 to 8.4 colour bar) border on and partly lie beneath the hatched cells, so the peak value itself is concealed. The text reports the peak without mentioning this. The legend entry "Low-confidence area" is the only explanation; a text search finds no definition (threshold on resolution, on normalised uncertainty or on another quantity), although the hatching steers which cells a reader discounts. |
| Suggestion | Define the low-confidence criterion in Section 3.3 and refer to it in the captions, give the peak value, and qualify l. 440 to 441 accordingly. |
| Status | verified (page image; text search) |
| Severity | moderate |
| Source | AB, SD |

**GB-53 The combined zircon and XRD solution is more uncertain than the XRD-only solution, yet Introduction and Discussion say the combination improves and further stabilises the result; the benchmark is also confounded.**

| Field | Content |
|---|---|
| Check | P2, P15, P10, P9, P31 |
| Location | p. 15, l. 441 to 449; p. 3, l. 72 to 73 (repeated p. 5, l. 139 to 140); p. 10, l. 284 to 285; p. 14, l. 420 to 422, l. 430 to 436; p. 15, l. 461 to 463; Figs. 14 to 16, annotation "Total normalised posterior uncertainty" (p. 35 to 37); Fig. 10 row 1 (p. 31) |
| Quotation | "Adding XRD data to the zircon dataset stabilizes the inversion and improves the posterior solution." / "showing that integrating XRD with zircon data improves the stability and sharpness of the posterior solution" / "combining XRD data with other fingerprint data such as zircon data, proves to further stabilize and improve the posterior solution" |
| Concern | Section 4.2.2 is careful about direction and compares the combined run with zircon alone. The values agree between text and annotations (0.87, 0.82, 0.86; PP-30). Calculated with Python: zircon to XRD 0.82 minus 0.87 = minus 0.05 (minus 5.75 %); zircon to combined minus 0.01 (minus 1.15 %); XRD to combined plus 0.04 (plus 4.88 %); of the 0.05 reduction XRD achieves over zircon, 0.04 or 80 % is lost when zircon is added. The Discussion ("further stabilize", l. 461 to 463) and the Introduction ("improves the stability and sharpness", l. 72 to 73) therefore claim a gain the numbers do not show against XRD alone. Further: "sharpness" is not measured anywhere; "accuracy" in validation question 3 (l. 285) cannot be assessed without a reference map; "proves" rests on one detrital sample (l. 423 to 424), and l. 421 says "the same detrital sample" while l. 437 to 438 says "a detrital sample taken at the same date and time" (KK-34); the zircon benchmark is incomplete by construction (two units without own zircon data, GB-48); the largest difference between datasets (0.05) is small against the span of about 0.72 that the same metric shows over the L sweep (GB-14), and no uncertainty of the metric is given; the JS of the XRD-only fingerprints is not reported (GB-35). Instances S1, S2 and AB noted the same contradiction outside their checklists. The grade is major because the finding concerns the third validation question. |
| Suggestion | In l. 72 to 73, l. 446 and l. 461 to 463 state that the combined result lies between the two single-method results (0.87 zircon, 0.86 combined, 0.82 XRD), replace "proves" by "suggests, for one sample,", and delete "sharpness" or define and report a sharpness measure; remove "accuracy" from l. 285 or name its measure. Define "stability" in Section 3.3 (for example the variance over bootstrap resamples of the detrital data or over the plausible hyperparameter range) and report it for all three datasets; add a synthetic benchmark with zircon-like and XRD-like matrices, with and without the two missing units, and repeated natural samples. |
| Status | verified (values in text and annotations; wording); inferred (percentages, calculated; span read from Fig. 10) |
| Severity | major |
| Source | S3, S4, SD |

#### Minor corrections

| ID | Location | Quotation | Replacement | Source |
|---|---|---|---|---|
| KK-19 | p. 10, l. 299; p. 12, l. 340; p. 14, l. 411, l. 414; Fig. 12 caption (p. 33); legends of Figs. 4 and 12 | "Zermatt Saas-Fee sediments"; "Zermatt-Saas-Fee ophiolites"; "Zermatt - Saas Fee"; "Zermatt- Saas Fee sediments unit" | "Zermatt-Saas Fee" in every occurrence, as in l. 273 to 274 and l. 431 | S2, S4, AB |
| KK-20 | p. 10, l. 299 | "(such as Zermatt Saas-Fee sediments and Furgg series (Figure 4) and Figure 5J)" | "(such as the Zermatt-Saas Fee sediments and the Furgg series; Figures 4 and 5J)" | S3, S4 |
| KK-21 | p. 11, l. 307; captions of Figs. 5 and 6 (p. 26, 27) | "the model’s "greedy" optimisation strategy"; "(a) "true" erosion map" | typographic quotation marks as in l. 288 and l. 291: “greedy”, “true” | S4 |
| KK-22 | Fig. 6 caption (p. 27) | "Results of the Steepest-Descent (SD) approach" | "Results of the steepest descent (SD) approach", as in l. 210 and l. 309 | S2 |
| KK-23 | p. 11, l. 319 | "(Figure 6D, 6E and 6F )" | "(Figure 6D, 6E and 6F)" | S3, S4 |
| KK-24 | Fig. 7, title of the left map (p. 28) | "Originial geology (same as forward)" | "Original geology (same as forward)" | AB |
| KK-25 | p. 12, l. 345 | "which measures the similarity between two probability distributions" | "which measures the dissimilarity between two probability distributions"; l. 346 already states that values near zero indicate more similar signatures | ZF |
| KK-26 | p. 12, l. 351 | "The more resemblant the source fingerprints are" | "The more similar the source fingerprints are" | S4 |
| KK-27 | p. 12, l. 352 | "decreases below  0.55, both absolute error and posterior uncertainty rise sharply, with errors exceeding 700 mm/yr" | "decreases below 0.55, both absolute error and posterior uncertainty rise sharply, with errors exceeding 700 mm/y" (single space; unit form of l. 295, 325, 384, 428, 435; value to be corrected per GB-36) | S2, S3, S4 |
| KK-28 | Fig. 9, colour bar title (p. 30) | "Number of tracrs" | "Number of tracers" | AB |
| KK-29 | p. 12, l. 370 | "the maximal amount of non-linear iterations" | "the maximum number of non-linear iterations" | S4 |
| KK-30 | Fig. 10, row 1, column 2, x-axis (p. 31) | "Smooting distance (m)" | "Smoothing distance (m)" | AB |
| KK-31 | p. 13, l. 384 | "approximately 10-2 mm/y" | "approximately 10⁻² mm/y", as "10⁻⁵" in l. 388 | S3, S4 |
| KK-32 | Fig. 11 caption (p. 32) | "Stockhorn-Turftgrat-Gornergrat"; "ZSF ophiolites (metabasites, ecologites)" | "Stockhorn-Tuftgrat-Gornergrat"; "ZSF ophiolites (metabasites, eclogites)" | S2, S4, AB |
| KK-33 | p. 13, l. 400 | "supporting the 1) the robustness of the cleaning and binning approach" | "supporting 1) the robustness of the cleaning and binning approach" | S3, S4, SD |
| KK-34 | p. 14, l. 420 to 421 | "applied to the same detrital sample" | "applied to a detrital sample taken at the same date and time", matching l. 437 to 438, or state in l. 437 to 438 that it is the same sample | SD |
| KK-35 | Figs. 14, 15, 16, legend below the erosion map (p. 35 to 37) | "Low-con dence area" | "Low-confidence area" | AB |
| KK-36 | Fig. 14 caption and y-axis of the fingerprint panel (p. 35); Fig. 16 title of the erosion map (p. 37) | "Posterior erosion rate map using Zr fingerprint data"; "Normalised abundance per Zr age bin"; "combined XRD and Zr data" | "zircon" instead of "Zr", as in the text (Zr is the element symbol) | S2 |

#### Verification log

| ID | Check | Checked | Values | Result |
|---|---|---|---|---|
| PP-12 | P3 | Maps and curves of Figs. 5 and 6 against Sections 4.1.1 and 4.1.2 | Fig. 5e: hotspot cells at the lower end of the colour bar (about 2), surroundings 6 to 8, in line with l. 301. Fig. 5d: lighter cells along the northern strip (Furgg series) and the western strip (ZSF sediments), in line with l. 299 to 300. Fig. 5g: rapid decrease and plateau, in line with l. 305 to 306; Fig. 5h rising and levelling off, in line with l. 306 to 307. Maps are blended with a hillshade, so interior colours compare only qualitatively. | no finding beyond GB-25, GB-39 |
| PP-13 | P1, P2, P38 | Hyperparameter names, symbols and values stated in more than one place; abbreviations | L = 1200 m = 4 × 300 m and 3000 m = 10 × 300 m, consistent in l. 294, 325, 373, 427; σm = 3, σd = 0.01 mm/y, prior equal to the average true erosion rate identical in l. 294 to 295, 324 to 326, 426 to 428; iterations 100 (l. 293) and 25 (l. 324, l. 426) belong to different tests; step size 0.1 in l. 326, 385, 428 and Fig. 10. QN and SD defined in l. 210 to 211, MAP l. 173, JS l. 345, PCA l. 355 to 356, KDE in the Fig. 13 caption, each with one meaning. | no finding beyond GB-32, KK-01, KK-22 |
| PP-14 | P23, P3, P22 | Run counts against plotted points; zircon age bins | Scenario 1: three geological cases (l. 332), 3 points per scatterplot of Fig. 7. Scenario 3: 1 to 21 tracers, 21 points in Fig. 9. Fig. 10: 20 markers per sweep. Fig. 5k: 21 tracers A to U. Figs. 14 and 16: 13 bins from 40 to 140 Ma to 750 to 800 Ma, contiguous without gap or overlap; Fig. 16: 21 minerals plus 13 bins = 34 bars. Fig. 8: 14 of 20 (GB-34). | balances close except GB-34; counts not stated in text (GB-28) |
| PP-15 | P7 | Validity of method version and protocol | One method change (gradient normalisation in steepest descent, l. 312) after unreported initial experiments; all reported steepest descent results use the normalised scheme, all later tests quasi-Newton (l. 320). No instrument, software or protocol change for XRD stated. Collection date known for one detrital sample only. Disclosed: instability (l. 312). | no finding beyond GB-27 |
| PP-16 | P30 | Order of corrections and reported runs | One reported error (steepest descent instability), corrected before the reported run by the order of the text; no dated corrections; no reported run predates a correction affecting it. | no finding |
| PP-17 | P3 | Fig. 7 against l. 337 to 342 | Read by eye from the raster: summed error 197 (forward geology), 193 (minimal changes), 275 (Steck et al. 2015); data misfit 3.26e6, 3.49e6, 3.69e6; model misfit 1.57, 1.92, 2.46; normalised trace 0.7402, 0.7376, 0.7459; area differences 0, about 0.69e7 and 1.15e7 m². The text names the non-monotonic error and the monotonic rise of both misfits, both in line with the figure. | no finding on the figure; the general statement is taken up in GB-24 |
| PP-18 | P2 | Baseline of the default synthetic configuration across Figs. 7 to 10 | Summed error about 197 (Fig. 7 forward geology, Fig. 9 all tracers, Fig. 10 row 3 at 197.42); normalised uncertainty about 0.740 (Fig. 7, Fig. 8 unblended, Fig. 9 all, Fig. 10 row 3 at 0.74015). | consistent, no finding |
| PP-19 | P20 | Reference of the average JS distance in Scenario 2 | "between all pairs of source XRD signatures and use the average across all combinations" (l. 347); 7 synthetic units, 7 × 6 / 2 = 21 pairs. Stated for the synthetic case; for the natural zircon and combined cases see GB-48. | no finding for Scenario 2 |
| PP-20 | P3 | Posterior uncertainty in Fig. 8 against l. 351 to 352 | Middle scatterplot (ticks 0.74 at 1124.0 px, 0.90 at 105.0 px): 0.893, 0.880, 0.883, 0.880 below JS 0.44; 0.832 to 0.842 at JS 0.441 to 0.541; 0.747, 0.741, 0.740, 0.740 at JS 0.561 to 0.624. The jump below 0.55 is present for the uncertainty. | no finding for the uncertainty; error in GB-34 |
| PP-21 | P3 | Fig. 9 against l. 360 to 362 | Summed error (600 dpi, ± 0.2): 2 tracers 348.1, 3 tracers 293.5, 4 tracers 296.5, 5 tracers 224.1, 6 tracers 205.2, 7 to 21 tracers 197.4; 1 tracer about 347 by eye. Posterior uncertainty about 0.77 at 6 and 0.74 from 7 tracers; misfits lower for fewer tracers. Matches "with 7 tracers ... approximately the same posterior solution" and the rise below 7. | no finding beyond GB-37 |
| PP-22 | P1, P2, P38 | Number and names of tracer minerals | Text list l. 394 to 396: 21 entries, 21 distinct (Python); "21 minerals" (l. 393), "21 target minerals" (l. 397), "between 1 and 21 tracers" (l. 358), Fig. 9 "All tracers (21)", Fig. 5k 21 labels, Fig. 11 21 rows, Fig. 15 21 labels in the order of the text. Only difference: chrysolite against chrysotile. | GB-41 |
| PP-23 | P36 | Approximate self-reports against the manuscript's own figures | "approximately the same posterior solution" with 7 tracers (l. 360) against Fig. 9: about 197 at 7 and 21 tracers, 205 at 6, 224 at 5, consistent. "beyond approximately 10 times the pixel size" (l. 373): GB-39. "Beyond 115 iterations ... below 10⁻⁵" (l. 388 to 389): no record shown (GB-40). "many of these cases" (l. 353): GB-34. "multiple detrital samples" (l. 413): GB-44. | no further finding |
| PP-24 | P3 | Normalisation of Fig. 11 | Longest bar per column 243, 242, 243, 242, 243, 243, 243 px (300 dpi): every column reaches full length once, as required by division by the maximum peak area (l. 261). Column colours follow the caption order and the colours of Figs. 5j and 15. | no finding beyond GB-42, GB-51 |
| PP-25 | P38 | Names of the subcatchment, sampling site and detrital samples | "Gorner-Grenzgletscher confluence" (l. 406, Fig. 12 label), "Gorner-Grenz subcatchment" (l. 411), "Gorner-Grenz confluence subcatchment" (captions of Figs. 12 and 13), "Gorner-Grenz catchment" (Fig. 13 inset): one place with a consistent stem. The sample of 28 June 2019, 13:30 is referred to consistently. | no finding; sample identifiers missing (GB-58) |
| PP-26 | P23 | Unit balance of the natural known-mixture experiment | 7 units (Fig. 11 caption); 1 without outcrop in the subcatchment (l. 411; Fig. 12 caption); Fig. 13 shows 6 units in the upper and ZSF sediments in the lower panel, 6 + 1 = 7. Disclosed: spillover (l. 414 to 415). | balance closes |
| PP-27 | P24 | Dated events against figures | One dated event: the detrital sample of "June 28, 2019, at 13:30" (l. 423 to 424), used for Figs. 14 to 16. No figure has a time axis; the only sequential axes are iteration counts (Figs. 5, 6, 10). | no date check possible, no finding |
| PP-28 | P13, P15, P38 | Notes outside the checklists (66 in all) checked at the manuscript where no responsible instance had treated the place | Adopted: eq. 9, 12 and 14 (S2, S4; GB-16); "measures the similarity" in l. 345 (S3; KK-25). Not adopted: "mineralogical fingerprints" for zircon age distributions in l. 425 (zircon is a mineral, the term is defensible); edition and pages of Moore and Reynolds (1990), l. 612 to 613, and the order of names in Astakhov et al., l. 511 (optional checks, not run); missing financial support statement although l. 492 mentions secured funding (optional check of journal requirements, not run); naming inside the Zenodo archive (outside the manuscript). The other 57 notes were already covered by findings. | GB-16, KK-25 |
| PP-29 | P3 | Fig. 14 fingerprint against l. 430 to 434 | Segment lengths (600 dpi) of Monte Rosa gneiss and Monte Rosa granite in the 11 bins in which they occur: 455/455, 430/430, 454/455, 450/451, 417/418, 129/129, 72/73, 52/53, 54/54, 378/378, 195/194 px, equal within 1 px. No serpentinite and no metabasite segment in any bin, consistent with l. 430 to 433. Bin 40 to 140 Ma only ZSF sediments, bin 750 to 800 Ma only Stockhorn, Tuftgrat, Gornergrat. | consistent; unmarked substitution in GB-49 |
| PP-30 | P1, P2 | Values and differences of Section 4.2.2 against figure annotations | 0.87 (l. 437, Fig. 14), 0.82 (l. 442, Fig. 15), 0.86 (l. 447, Fig. 16), identical in vector text. "decreases slightly to 0.86 (from 0.87)": minus 0.01, correct direction; JS 0.48 to 0.57: plus 0.09 (plus 18.75 %), "increases" correct. "(>8000 mm/y)" (l. 435) against the Fig. 14 colour bar labelled up to 8000 with the bar extending above: consistent. JS values are shown in no figure. | arithmetic correct; comparison basis in GB-53 |

### Segment 4: Discussion, conclusions, statements, references (p. 15 to 21)

#### Substantive findings

**GB-54 The novelty claim overlaps with the authors' earlier inversion of provenance data into erosion rate maps and calls a linear mixture with log-parameterised rates a non-linear mixing model.**

| Field | Content |
|---|---|
| Check | P28, P14, P15, P18 |
| Location | p. 15, l. 454 to 455; p. 2, l. 58 to 61 (repeated p. 4, l. 125 to 128); p. 5, l. 151 to 159 (eq. 1 to 3) |
| Quotation | "The novelty of our method lies in the spatially informed approach of this underdetermined inversion problem, and in the incorporation of non-linear mixing model." / "We cast the erosion rates in log-space to impose a positivity constraint, hence making this non-linear." |
| Concern | The Introduction is open about building on the earlier framework (l. 60 to 61). (1) Spatially informed approach: De Doncker, F., Herman, F. and Fox, M. (2020) 'Inversion of provenance data and sediment load into spatially varying erosion rates', Earth Surface Processes and Landforms (reference list p. 18, l. 559), already converts detrital provenance data and sediment load into an erosion rate map by a least-squares inversion with prior and covariance information, tested on synthetic and natural data, and names mineral content as a possible tracer (abstract read by S1 on the UNIL Serval record). The EGU 2021 abstract of the same group (GB-07) reports erosion rate maps for the Gornergletscher from a non-linear inverse model. No search is named behind the novelty statement (PP-02). (2) Non-linear mixing: by the manuscript's own wording the detrital data are "a weighted average of the tracer mineral concentrations, with the weights being the erosion rates" (l. 151 to 152); eq. 3 is linear in the erosion rates, and the non-linearity arises only from the log parameterisation for positivity (l. 158 to 159). The contrast with approaches that "implicitly rely on a linear mixing scheme" (l. 59) therefore applies to this method as well. The sentence also lacks an article ("of non-linear mixing model"). What remains new after this comparison is the binned XRD peak areas as tracers in this framework, the log-space positivity constraint, the comparison of two schemes and the posterior metrics. Three instances raised the second point independently. The grade is major because the finding changes what the manuscript can claim as its contribution. |
| Suggestion | In l. 454 to 455 restrict the novelty to what differs from De Doncker et al. (2020): XRD-based fingerprints, the log-space parameterisation that enforces positive erosion rates, and the comparison of steepest descent and quasi-Newton schemes; write "a non-linear (log-space) parameterisation of the erosion rates within a linear mixing model" instead of "non-linear mixing model"; in l. 58 to 61 state in one sentence what the 2020 framework already did and relate the work to EGU21-6207. |
| Status | verified (content of the two abstracts as read; eq. 1 to 3 and l. 151 to 159 at page image 5); inferred (that no search was run, since none is reported) |
| Severity | major |
| Source | S1, S4, SD |

**GB-55 The Discussion states effects that no test examined or that the tests contradict: more tracers "further" improve the solution, and more source areas raise resolution.**

| Field | Content |
|---|---|
| Check | P15, P10, P6 |
| Location | p. 15, l. 458, l. 460 to 461; p. 16, l. 485; basis p. 12, l. 355 to 365; Fig. 9 (p. 30) |
| Quotation | "Including a broad set of tracer minerals further improves model stability and resolution." / "A higher number of distinct source areas leads to higher posterior resolution and lower uncertainty." |
| Concern | Tracers: Section 4.1.3 reports that 7 tracers give "approximately the same posterior solution as with the full tracer set" (l. 360) and that reducing the number of tracers has "a comparatively limited effect" (l. 364 to 365); in Fig. 9 summed error and normalised uncertainty are flat from 7 to 21 tracers (PP-21), so 7 of 21 tracers (33 %) suffice in this test. This supports "a minimum number of informative tracers is needed", not "a broad set further improves"; resolution is not among the metrics of the tracer test. Source areas: no scenario varies the number of source areas (Scenario 1 map geometry, Scenario 2 distinctiveness, Scenario 3 tracers, Section 4.1.4 hyperparameters); the only related observation concerns unit size (l. 299 to 300). Both statements feed the recommendations (l. 463 to 466) and the Conclusions (l. 485); hence major. |
| Suggestion | Rephrase l. 458 to match Section 4.1.3 (below about seven informative tracers error and uncertainty rise; above that, additional tracers changed the synthetic solution little), or add resolution to Fig. 9 if the claim on resolution stays. Either add a synthetic test that varies the number of source units at constant distinctiveness, or present l. 460 to 461 as an expectation and drop it from the evidence-based part of l. 484 to 485. |
| Status | verified (text, page image 30); inferred (33 %, calculated) |
| Severity | major |
| Source | S4, SD |

**GB-56 The proposed extension to land-use source areas is untested and drops the condition the manuscript identifies as essential.**

| Field | Content |
|---|---|
| Check | P15 |
| Location | p. 15, l. 466; p. 16, l. 487 to 488; basis p. 12, l. 351 to 354, l. 363 to 364; p. 15, l. 457 |
| Quotation | "Other types of source area maps, such as those based on land use, can also be incorporated." |
| Concern | The strongest effect in the degradation tests is fingerprint distinctiveness (l. 363 to 364), and the Discussion calls distinct source signatures "essential" (l. 457). The fingerprints are mineralogical. Whether land-use classes on the same bedrock have distinct XRD fingerprints is not shown; if they do not, the proposal drops the essential condition. Question to the authors: do you expect land-use classes to differ in XRD mineralogy, or does the extension require other tracers? |
| Suggestion | In l. 466 and l. 487 to 488 add the condition that the land-use classes have sufficiently distinct fingerprints (cf. Section 4.1.3, Scenario 2) and mark the extension as untested. |
| Status | verified (necessity of distinct fingerprints, l. 351 to 354, l. 363 to 364, l. 457); assumption (mineralogical contrast between land-use classes, posed as a question) |
| Severity | moderate |
| Source | S4 |

**GB-57 The Conclusions present "minimal sediment storage" as a result, although storage was never tested and is a model assumption.**

| Field | Content |
|---|---|
| Check | P15 |
| Location | p. 16, l. 484 to 485; basis p. 1, l. 23 (repeated p. 3, l. 90); p. 15, l. 466 to 468 |
| Quotation | "Our results suggest that the method is best applied in catchments with minimal sediment storage" |
| Concern | The Discussion derives the restriction correctly from the model assumption ("assumes immediate sediment export", l. 467 to 468), and the Introduction says the approach works "without modelling storage or transport" (l. 23). No test in Section 4 varies storage. The Conclusions attribute the restriction to "our results". Storage at the study site is taken up in GB-22. |
| Suggestion | In l. 484 to 485 separate the two sources: the results suggest application where source areas are mineralogically distinct and their spatial distribution is well known; by construction, the method also assumes minimal sediment storage. |
| Status | verified (wording, absence of a storage test) |
| Severity | moderate |
| Source | S4 |

**GB-58 The one-sentence data statement does not enumerate what is archived, and the manuscript gives no sample identifiers, so archived files cannot be matched to the samples used in the text.**

| Field | Content |
|---|---|
| Check | P12 |
| Location | p. 16, l. 490; p. 9, l. 250 to 262; p. 13, l. 391 to 398; p. 14, l. 406 to 407, l. 413, l. 423 to 424, l. 437 to 438 |
| Quotation | "The data and codes used for the inversion tests in the study are available at https://doi.org/10.5281/zenodo.17120374" |
| Concern | The link resolves to an open-licence record (PP-33). Sections 3.4 and 4.2 name raw source and detrital diffractograms, Peak Finder output, the quartz alignment pattern, the RRUFF spectra and the resulting window table, the normalised fingerprint tables, synthetic inputs, the Gorner-Grenz detrital samples and the detrital sample of 28 June 2019, 13:30. The statement says only "data and codes used for the inversion tests", which does not tell a reader whether raw diffractograms, the window table or figure scripts are included (PP-06: 2 of 15 sources named). The manuscript gives no sample codes, coordinates or number of source samples per unit, so even with the archive a reader cannot tell which file is which sample. The Peak Finder settings are not reported (GB-18), so processed files cannot be regenerated from raw files. In the visible part of the repository listing named by the Zenodo record, detrital file names look like dates such as 28_7_11_26_1 and none encodes 28 June, 13:30; whether the sample is from 28 June or 28 July is therefore put as a question. |
| Suggestion | Expand l. 490 into a short inventory (raw source and detrital diffractograms, Peak Finder outputs, 2θ window table, fingerprint tables, geological maps, zircon data, synthetic inputs, figure scripts) with the folder of each item; add a sample table (code, unit or site, coordinates, date and time) to Section 3.4 or a supplement and identify the samples of Sections 4.2.1 and 4.2.2 by code; confirm the sampling date. |
| Status | verified (wording of the statement, absence of identifiers and settings); inferred (file codes and possible date mismatch, from a truncated repository listing, not from the archived release) |
| Severity | moderate |
| Source | S2 |

**GB-59 Three reference entries lack publisher or containing work, unlike the rest of the list.**

| Field | Content |
|---|---|
| Check | P16 |
| Location | p. 17, l. 521 (Bearth); p. 19, l. 583 (Gjems); p. 19, l. 599 to 600 (Lafuente et al.) |
| Quotation | "Gjems, O.: Studies on clay minerals and clay-mineral formation in soil profiles in Scandinavia, 1967." |
| Concern | Other book and map entries give publisher and place (for example Tarantola, l. 634 to 635; Menke, l. 610 to 611). The entries for Bearth (1953), Gjems (1967) and Lafuente et al. (2015) give neither publisher nor series, and Lafuente et al. give neither editors nor publisher of the edited volume, so the works are harder to locate. Only uniformity is assessed here; conformity with a citation style is an optional check. |
| Suggestion | Complete the three entries with publisher and series (map series publisher for Bearth; series and publisher for Gjems; editors, publisher and DOI of the volume for Lafuente et al.) in the format of l. 610 to 611. |
| Status | verified (page images 17, 19) |
| Severity | minor |
| Source | S4 |

**GB-60 The short citation "E., 2009" and its entry "E., W. D." use an initial as surname.**

| Field | Content |
|---|---|
| Check | P4 |
| Location | p. 18, l. 567 to 568; p. 1, l. 11 to 12 (repeated p. 3, l. 78 to 79) |
| Quotation | "(Gergel et al., 2002; Allan, 2004; E., 2009; Hamel et al., 2015)" |
| Concern | The surname field of the entry is the initial "E.", and the short citation repeats it. The pattern "E., W. D." corresponds to "Walling, D. E." with surname and initials swapped. A web search for the title returns the UNESCO report "The Impact of Global Change on Erosion and Sediment Transport by Rivers: Current Progress and Future Challenges" attributed to Walling; the UNESCO PDF itself could not be opened, so the attribution is inferred. The entry also contains "UNESCO 2009" in the publisher field, the stray string "oCLC" and an abbreviated title. |
| Suggestion | Replace "E., 2009" by "Walling, 2009" in l. 11 to 12 (and l. 78 to 79) and rewrite the entry as "Walling, D. E.: The impact of global change on erosion and sediment transport by rivers: current progress and future challenges, UNESCO, Paris, ISBN 9789231041358, 2009.", sorted under W. |
| Status | verified (corrupted name); inferred (identity of the author) |
| Severity | minor |
| Source | S4, S1 |

#### Minor corrections

| ID | Location | Quotation | Replacement | Source |
|---|---|---|---|---|
| KK-37 | p. 16, l. 490 | "are available at https://doi.org/10.5281/zenodo.17120374" | "are available at https://doi.org/10.5281/zenodo.17120374." | S4 |
| KK-38 | p. 16, l. 491 to 494 | "All authors (FDD, FH, BB, TA)"; "F.H. led the conceptual development"; "F.D.D. developed all code" | one form of initials throughout, for example "F.D.D., F.H., B.B., T.A." | S2, S4 |
| KK-39 | p. 17, l. 522 to 523 | "Master’s thesis, University of Lausanne, unpublished master’s thesis, 2021." | "Master’s thesis, University of Lausanne, unpublished, 2021." | S4 |
| KK-40 | p. 17, l. 526 | "Mineralogical society of America" | "Mineralogical Society of America" | S4 |
| KK-41 | p. 19, l. 578 | "Gergel, S. E., Turner, M. G., Miller, J. R., Melack, J. M., and Stanley, E. H.: [No title found], Aquatic Sciences, 64," | "Gergel, S. E., Turner, M. G., Miller, J. R., Melack, J. M., and Stanley, E. H.: Landscape indicators of human impacts to riverine systems, Aquatic Sciences, 64," (title from the article record, DOI 10.1007/s00027-002-8060-2) | S4 |
| KK-42 | p. 20, l. 612 | "Oxford University Press, New-York" | "Oxford University Press, New York" | S4 |

#### Verification log

| ID | Check | Checked | Values | Result |
|---|---|---|---|---|
| PP-31 | P15 | Each statement of the Discussion (l. 451 to 476) and Conclusions (l. 478 to 489) against a place in the Results | Supported as stated: four inputs (l. 452 to 454) against l. 65 to 66 and Section 3; distinct signatures essential (l. 457) against l. 351 to 354 and l. 363 to 364; accurate spatial delineation crucial (l. 459 to 460) against l. 337 to 342 and Fig. 7 (about 198 for the forward map, about 275 for the Steck et al. map); recommendations a) to c) (l. 464 to 466) against Scenarios 1 to 3; resolution and covariance as reliability measures (l. 483 to 484) against l. 299 to 304; applicability to zircon ages (l. 489) against Section 4.2.2. The Conclusions do not mention the natural tests at all, an omission rather than a contradiction. Disclosed: storage (l. 466 to 468); grain size, orientation, peak overlap (l. 469 to 476). | not supported as stated: GB-02, GB-03, GB-53, GB-54, GB-55, GB-56, GB-57 |
| PP-32 | P9 | Announced future studies whose design could be checked | None announced; the Discussion and Conclusions name possible extensions (land use, sub-catchments, other tracers, l. 466, l. 487 to 489) without a study design. | nothing to check |
| PP-33 | P12 | Reachability and content of the linked archive | https://doi.org/10.5281/zenodo.17120374 redirects to zenodo.org/records/17120374: "First public release", version v1.0.0, published 15 September 2025, CC BY 4.0, open access, one zip file of 49.3 MB, no newer version listed. The zip was not opened. The repository named by the record lists inversion scripts, fingerprint generation scripts with source and detrital input folders, geological maps, a DEM, a glacier mask, zircon data files and a thesis PDF; the listing was truncated. Disclosed: unpublished thesis (l. 522 to 523), inferred geology (l. 270 to 272). | link present and reachable; contents not stated in the manuscript (GB-13, GB-20, GB-47, GB-58) |
| PP-34 | P16 | Language and typesetting of running text, captions and statements at the page images; uniformity of the reference list | Pages 1 to 3, 5 to 21, 25 to 30, 32, 33, 35 to 37 read at the page images. Statements present: Code and data availability, Author contributions, Competing interests, Acknowledgements. Observations only in text.json were discarded (see PP-07). | KK-01 to KK-42 where from S4; GB-59 |
| PP-35 | P4 | Every in-text citation against the reference list in both directions; years, spelling, "et al." | 64 distinct cited works (63 by pattern plus "E., 2009"), 64 entries (l. 501 to 653; two merged entries separated by hand). Every citation has an entry, every entry is cited, all years agree; "et al." for all works with three or more authors, "and" for all two-author works. DOIs not resolved (optional check). | deviations GB-06, GB-20, GB-60, KK-41 |

## Optional checks

| Area | What it needs | Responsible | Run |
|---|---|---|---|
| DOI resolution | one retrieval per reference entry with a DOI | `science-quellenapparat-pruefung` | no |
| Citation style | the name of the style or the target journal's style rules | `science-zitierstil-harvard-ctr` or the journal's style rules | no |
| AI statement against publisher policy | the target publisher's policy on AI use | this review, on request | no |
| Relation to the authors' prior work | the authors' prior publications, as files or DOIs | this review, on request | no |
| Journal requirements | the target journal's author guidelines | this review, on request | no |
| Factual accuracy | access to the sources of each checked statement and a choice of sections | `science-faktenbeleg-pruefung`, `geo-frage-belegbasiert-klaeren` | no |

Need in this manuscript: the relation to prior work is the most relevant area, because the novelty claim overlaps with De Doncker et al. (2020), EGU21-6207 and Belotti (2021) (GB-54, GB-07, GB-47). Journal requirements would cover the missing financial support statement (PP-28). DOI resolution and citation style would cover the reference defects that the P4 check found only in part (PP-35).

## Limits of this review

- Checked version: egusphere-2025-4695.pdf, 37 pages, SHA-256 9c80676054f96ecd6f00f4d2a8b5ba568e03c6949e3856d363ac1c4abb42e7bd.
- Review set-up: six instances (segments 1 to 4, figures, study design) ran as separate agents; their results were merged here, wording and locations of all quotations were checked against text.json and, for figures, tables and line numbers, against the page images.
- Unreadable sources: Das et al. (2023) and Klages and Hsieh (1975) (not readable); Wilson et al. (1993) (title only); Niu et al. (2020) and Haddadchi et al. (2013) (abstract only); the UNESCO 2009 report (PDF not readable); the archived Zenodo zip (not opened, only the record and a truncated repository listing).
- Findings with status assumption: 0 of 60 rest on an assumption in their central statement; 11 of 60 contain a partial statement with status assumption (GB-09, GB-10, GB-13, GB-19, GB-22, GB-25, GB-30, GB-41, GB-43, GB-48, GB-56), each put as a question.
- Discarded findings: 0 of 84 instance findings; all carried the mandatory fields.
- Merged findings: 84 instance findings became 59 findings (25 merged into others), plus 1 new finding from the merge (Source ZF), 60 in all. Of 74 instance minor corrections, 14 were absorbed into findings and 60 merged into 41 corrections, plus 1 new correction (Source ZF), 42 in all. Of 42 instance verification logs, 8 were merged, giving 34, plus 1 new log (Source ZF), 35 in all.
- Disagreements between instances decided at the manuscript: 5 (GB-09, GB-24, GB-34, GB-39, PP-05).
- Optional checks run: 0 of 6.
