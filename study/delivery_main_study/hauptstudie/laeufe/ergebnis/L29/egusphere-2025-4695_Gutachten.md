# Review report: From XRD signal to erosion rate maps

| Field | Value |
|---|---|
| Manuscript | De Doncker, F., Herman, F., Belotti, B. and Adatte, T. (2025) From XRD signal to erosion rate maps, EGUsphere preprint egusphere-2025-4695, https://doi.org/10.5194/egusphere-2025-4695 |
| Checked version | egusphere-2025-4695.pdf, 37 pages, SHA-256 9c80676054f96ecd6f00f4d2a8b5ba568e03c6949e3856d363ac1c4abb42e7bd |
| Date | 2026-10-18 |
| Language | English |
| Review instances | Segments 1 to 4 (S1 to S4), figures (AB), study design (SD); the six review instances ran as separate agents, each without context from the others; the merge (ZF) ran as a further separate agent; no instance omitted |

## Summary

The manuscript is a methods-development study with a field application. It presents a Bayesian maximum a posteriori inversion in which binned XRD peak areas of 21 tracer minerals, assigned to seven lithological units through a geological map, are unmixed from detrital suspended sediment into a pixel-wise erosion rate map; erosion rates are parameterised in log-space, which makes the inversion non-linear, and are solved with steepest descent and quasi-Newton schemes, with posterior covariance, resolution and a normalised covariance ratio as uncertainty metrics. Synthetic forward-inverse tests on one true map with a single hotspot (pixel size 300 m) compare the two schemes, test three degradation scenarios (geological map uncertainty, fingerprint blending, tracer reduction) and sweep five hyperparameters. The natural-data tests in the Gornergletscher catchment (Pennine Alps) compare the fingerprints with the known lithology, use the Gorner-Grenz subcatchment as a natural known-mixture test with one absent unit, and compare zircon U-Pb, XRD and combined fingerprints on a detrital sample of 28 June 2019, with total normalised posterior uncertainties of 0.87, 0.82 and 0.86 and an average Jensen-Shannon distance rising from 0.48 (zircon) to 0.57 (combined). The introduction is printed twice (GB-03).

## Strengths

1. The synthetic forward-inverse framework with a known true map, three degradation scenarios and five parameter sweeps makes the sensitivity of the inversion to map errors, fingerprint distinctiveness, tracer number and hyperparameters visible; all announced tests are reported, and the figures agree with the text on the plateau from seven tracers, the optimum step size of 0.1 and the misfits of scenario 1 (PP-14, PP-18, PP-19, PP-20); how far these tests carry is limited by their set-up (GB-29).
2. Reporting one scalar uncertainty metric for all three natural-data inversions, identical in text and figures (0.87, 0.82, 0.86), makes the zircon, XRD and combined runs directly comparable and lets a reader check the claims drawn from them (PP-13, PP-23, GB-63).
3. The manuscript states its data gaps where they arise: the inferred lithology under the ice is declared where the map is introduced and tested in scenario 1, and the missing zircon data for two units and the substituted fingerprint are declared in Sect. 4.2.2, so a reader can trace the instability of the zircon run to its inputs (PP-08, PP-18, GB-45).
4. The internal referencing is consistent: 64 citations match 64 reference entries in both directions, Equations 1 to 22 and Figures 1 to 16 are numbered without gaps and first cited in order, and code and data for the inversion tests are deposited under a resolving DOI (PP-26, PP-10, PP-29).

## Weaknesses

1. Central claims go beyond the evidence reported: time and cost efficiency is stated as validated without any measure (GB-01); the combination of XRD and zircon is said to improve the solution although its uncertainty is higher than for XRD alone (GB-63); the synthetic tests are summarised as reliable recovery although they give the inversion the true mean and noise-free data from the same operator (GB-29); and the natural known-mixture test is said to confirm that geological boundaries are respected although the absent unit is not separated from present ones (GB-44). Restrict abstract, introduction and conclusions to what the reported metrics show, and add the missing comparisons and tests.
2. The XRD fingerprint chain is not validated: maximum normalisation before mixing is incompatible with the linear mixing model (GB-23), several tracers duplicate each other (GB-54), the fingerprints contain signals that the unit descriptions do not lead one to expect (GB-43), the fingerprints entering the natural inversion differ from Fig. 11 by an undescribed step (GB-59), and the measurement protocol is not given (GB-22). Test the chain with laboratory mixtures of known proportions and document windows, instrument settings and every normalisation step.
3. The uncertainty metrics and the solvers are partly not reproducible or not plausible as printed: the plotted resolution near 1 is incompatible with the rank of the problem (GB-19), two different quantities share one name (GB-20), the quasi-Newton update inverts a singular matrix (GB-18), Eq. 9 and 14 contain errors (GB-16), and the scheme comparison does not support the stated higher accuracy of QN (GB-32, GB-17). Give the formulas actually implemented and recheck the plotted metrics against them.
4. Several moderate gaps prevent reproduction: the export estimate and the prior of the natural runs (GB-47), the parameters per test (GB-30), sample numbers, dates and the zircon protocol (GB-21), an itemised availability statement (GB-67), the omitted runs of Fig. 8 (GB-35) and the meaning of the highlighted values in Fig. 10 (GB-52). Add a parameter table, a sample table and an itemised availability statement.

## Findings by segment

### Segment 1: Abstract, Introduction (p. 1 to 5)

#### Substantive findings

**GB-01 The abstract and the introduction present time and cost efficiency as validated, but no measure of time or cost is reported anywhere in the manuscript.**

| Field | Content |
|---|---|
| Check | P15, P31, P33 |
| Location | p. 1, l. 3 to 4; p. 2, l. 40 to 42 and p. 4, l. 107 to 109; p. 3, l. 74 to 75 and p. 5, l. 141 to 142 |
| Quotation | "In this study, we validate a time- and cost-effective fingerprinting approach based on X-ray diffraction (XRD) data."; "To conclude, we show and validate the potential of binned XRD peak-area data as a cost- and time-efficient approach for constructing erosion rate maps." |
| Concern | The introduction motivates XRD by the cost of other tracers ("many of these methods are expensive and time-consuming", p. 2, l. 35, citing Das et al., 2023), and the abstract and the last paragraph of the introduction present cost and time efficiency as validated. Search in p. 1 to 21 (text.json): "cost" 6 hits (p. 1, l. 3 and 4; p. 2, l. 40; p. 3, l. 74; p. 4, l. 107; p. 5, l. 141), "time-" 5 hits (p. 1, l. 3; p. 2, l. 35; p. 3, l. 75; p. 4, l. 102; p. 5, l. 142), "efficien" 4 hits (p. 2, l. 42; p. 3, l. 75; p. 4, l. 109; p. 5, l. 142), "expens" 2 hits (p. 2, l. 35; p. 4, l. 102), "cheap" 0 hits; all lie in the abstract and in the two copies of the introduction, none in Methods, Results, Discussion or Conclusions. No preparation or measurement time, instrument time or cost per sample is given, although the zircon U-Pb workflow used as benchmark in Sect. 4.2.2 (p. 14, l. 420 to 425) would allow a direct comparison. Graded major because the first result stated in the abstract would not stand if the finding holds; the inversion results themselves are unaffected. |
| Suggestion | Either report in Sect. 4.2.2 (or a new subsection) preparation and measurement time, instrument time and consumable cost per sample for XRD and for zircon separation and U-Pb dating, and discuss them in Sect. 5 and 6, or reword p. 1, l. 3 to 4, p. 3, l. 74 to 75 and p. 5, l. 141 to 142 as a motivation (for example "potentially cost-effective, following Das et al. (2023)") instead of a validated result. |
| Status | verified (wording at all locations; absence by the search stated) |
| Severity | major |
| Source | S4, SD |

**GB-02 The abstract states consistent convergence of the synthetic tests, while the results report an unstable steepest descent scheme and blending runs without a stable solution.**

| Field | Content |
|---|---|
| Check | P2 |
| Location | p. 1, l. 7; p. 3, l. 70 to 71 and p. 5, l. 137 to 138 |
| Quotation | "Forward-inverse tests with synthetic data demonstrate consistent convergence of the posterior solution."; "demonstrate the convergence of the inversion" |
| Concern | The results section states the limits of convergence openly; the abstract does not carry them over. The steepest descent scheme needed gradient normalisation (p. 11, l. 312), and in scenario 2 six of the 20 blending runs have no plotted solution, all at average JS distance below about 0.44 (counted in GB-35). The condition under which the inversion converges (QN scheme, sufficiently distinct fingerprints) is itself a result that users of the method need. The count of missing runs is treated in GB-35; here the concern is the abstract statement. |
| Suggestion | Qualify p. 1, l. 7 and p. 3, l. 70 to 71 (and p. 5, l. 137 to 138), for example: the QN inversion converged when source fingerprints were sufficiently distinct (average JS distance above about 0.44 in the synthetic tests) and failed to converge for strongly blended fingerprints. |
| Status | verified (wording at the page images p. 1, 3, 11, 12, 29); the count of six non-plotted runs inferred (measurement in the cited finding) |
| Severity | moderate |
| Source | S3 |

**GB-03 Section 2 "Introduction" repeats Section 1 "Introduction" word for word, so all later sections are numbered one higher.**

| Field | Content |
|---|---|
| Check | P4 |
| Location | p. 1, l. 9; p. 3, l. 76 |
| Quotation | "1 Introduction"; "2 Introduction" |
| Concern | Python word-by-word comparison (difflib) of l. 10 to 75 against l. 77 to 142 in text.json: 1153 words each, similarity ratio 1.0, no differing segment; both headings and the repeated paragraphs confirmed on the page images p. 1 to 5. The same observation was reported independently by S1, S2, S3, AB and SD as a note. Consequences: every statement and citation of the introduction appears twice (all locations in Segment 1 of this report are therefore given twice), and Methods, Validation, Discussion and Conclusions are numbered 3 to 6 instead of 2 to 5. |
| Suggestion | Delete Section 2 (p. 3, l. 76 to p. 5, l. 142) and renumber Sections 3 to 6 as 2 to 5. |
| Status | verified |
| Severity | minor |
| Source | S4 |

**GB-04 The short citation "E., 2009" and its reference entry "E., W. D." carry an initial in place of the author surname.**

| Field | Content |
|---|---|
| Check | P4 |
| Location | p. 1, l. 11 to 12 and p. 3, l. 78 to 79; p. 18, l. 567 to 568 |
| Quotation | "(Gergel et al., 2002; Allan, 2004; E., 2009; Hamel et al., 2015)"; "E., W. D.: The Impact of global change on erosion and sediment transport by rivers, UNESCO 2009" |
| Concern | Citation and entry match each other, but the name form is defective: "E." is an initial and the entry has no surname. The order "E., W. D." looks like a mis-parsed "Walling, D. E."; web search results associate the UNESCO report of this title with D. E. Walling, but the UNESCO PDF could not be read (rate limit). If confirmed, the citation must remain distinguishable from Walling et al. (1979), already in the list (p. 20, l. 645 to 646). The other formal defects of the same entry are part of GB-68. |
| Suggestion | Correct the entry at p. 18, l. 567 to 568 to the author on the title page (presumably "Walling, D. E.") and the citations at p. 1, l. 11 to 12 and p. 3, l. 78 to 79 accordingly (presumably "Walling, 2009"). |
| Status | verified (defective name form, page images p. 1, 3, 18); inferred (author D. E. Walling, from web search results; the UNESCO full text was not readable) |
| Severity | minor |
| Source | S1, S4 |

**GB-05 Five citations in the introduction concern a different subject than the statement they support.**

| Field | Content |
|---|---|
| Check | P13 |
| Location | p. 1, l. 18 to 19 and p. 3, l. 85 to 86; p. 2, l. 28 and p. 4, l. 95; p. 2, l. 30 and p. 4, l. 97; p. 2, l. 31 and p. 4, l. 98; p. 17, l. 519 to 520; p. 17, l. 528 to 530; p. 19, l. 597 to 598; p. 20, l. 641 to 642; p. 21, l. 649 to 650 |
| Quotation | "Direct measurements, such as sediment traps installed on dams, provide valuable information on sediment fluxes but do not reveal the origin of the transported material (Wilson et al., 1993; Barker et al., 1997; Davis and Fox, 2009)"; "nutrients (Blaen et al., 2016; Asadi et al., 2025)"; "mineralogy (Walden et al., 1997; Nukazawa et al., 2021)"; "plant pollen content (Brown, 1985; Kobe, 2021)" |
| Concern | The list of fingerprinting tools (p. 1, l. 26 to p. 2, l. 33) gives a useful overview with two references per tracer class, but five cited works do not report what they are cited for. (a) Kobe (2021) is "Ubuntu as a spirituality of liberation for black theology of liberation" (p. 19, l. 597), a theology article; its article page and abstract mention neither pollen nor sediment. (b) Barker et al. (1997) measure bank erosion with terrestrial photogrammetry (title at p. 17, l. 519; abstract read); this is not a study of sediment traps on dams. (c) Wilson et al. (1993) is, by its title, "Soil erosion in the Falkland Islands: an assessment" (p. 21, l. 649). (d) Walden et al. (1997) is, by its title, "Use of mineral magnetic measurements to fingerprint suspended sediment sources" (p. 20, l. 641), a magnetic tracer, which the same sentence lists separately as "magnetic susceptibility" (p. 2, l. 29). (e) Blaen et al. (2016) is, by its title, "Real-time monitoring of nutrients and dissolved organic matter in rivers" (p. 17, l. 528 to 529), not a use of nutrients as source fingerprints. A reader who follows these references cannot check the statements. |
| Suggestion | In Section 1 (and its duplicate), replace Kobe (2021) with a study that uses pollen as a sediment source tracer, Barker et al. (1997) and Wilson et al. (1993) with studies of sediment traps or reservoir sedimentation, move Walden et al. (1997) to "magnetic susceptibility" or cite a mineralogical (for example XRD) fingerprinting study under "mineralogy", and replace Blaen et al. (2016) with a study that uses nutrients as source tracers; correct the reference list accordingly. |
| Status | (a) verified: article page and abstract read, https://hts.org.za/index.php/hts/article/view/6176 (via DOI 10.4102/hts.v77i3.6176), version of record; absence of pollen in the full text inferred. (b) verified: abstract read, https://researchportal.port.ac.uk/en/publications/use-of-terrestrial-photogrammetry-for-monitoring-and-measuring-ba/. (c), (d), (e) inferred from the titles in the reference list; sources not opened |
| Severity | moderate |
| Source | S1 |

**GB-06 Work on detrital erosion mapping in glacial catchments, and on how ice transport and storage distort the detrital signal, is missing.**

| Field | Content |
|---|---|
| Check | P14 |
| Location | p. 1, l. 23 and p. 3, l. 90; p. 2, l. 61 to p. 3, l. 62 and p. 4, l. 128 to 129; p. 15, l. 466 to 468 |
| Quotation | "Importantly, this approach links sediment directly to its origin, without modelling storage or transport."; "This spatially informed approach to sediment provenance is particularly valuable in glacierized catchments, where ice cover limits direct observations" |
| Concern | The manuscript discloses the storage-free assumption and cautions against storage-dominated catchments (p. 15, l. 466 to 468), but argues that the approach is particularly suited to glacierized catchments without citing work on that setting. (a) Ehlers et al. (2015) inferred spatial variations of erosion in a glacial catchment (Tiedemann Glacier) from detrital thermochronology of outwash, which anticipates the aim of mapping glacial erosion from detrital data. (b) Bernard et al. (2020) showed by modelling that detrital age distributions in glacial settings diverge from the bedrock source distribution because of storage in tributary glaciers and moraines, variable transport times and limited lateral mixing. This bears directly on the assumption at p. 1, l. 23. Neither work is in the reference list (search for "Ehlers", "Bernard", "thermochron" in p. 17, l. 501 to p. 21, l. 653: 0 hits). Whether the own catchment meets the storage condition is treated in GB-11; here the concern is the missing literature. |
| Suggestion | Cite Ehlers, T. A., Szameitat, A., Enkelmann, E., Yanites, B. J., and Woodsworth, G. J.: Identifying spatial variations in glacial catchment erosion with detrital thermochronology, J. Geophys. Res. Earth Surf., 120, 1023 to 1039, https://doi.org/10.1002/2014JF003432, 2015, in Section 1 at p. 2, l. 58 to p. 3, l. 63, and Bernard, M., Steer, P., Gallagher, K., and Lundbek Egholm, D.: Modelling the effects of ice transport and sediment sources on the form of detrital thermochronological age probability distributions from glacial settings, Earth Surf. Dynam., 8, 931 to 953, https://doi.org/10.5194/esurf-8-931-2020, 2020, at p. 1, l. 23 and in Section 5 at p. 15, l. 466 to 468, with a statement of how ice transport and storage at Gornergletscher affect the inferred maps. |
| Status | verified: (a) abstract read, https://deepblue.lib.umich.edu/items/460ed15b-87a0-45fd-8c50-840c87a1b68e; (b) abstract read, https://esurf.copernicus.org/articles/8/931/2020/ (version of record); bearing on the own catchment inferred |
| Severity | moderate |
| Source | S1 |

**GB-07 Three gap and novelty claims are made without any account of how the literature was searched, and one is weakened by the authors' own cited predecessor.**

| Field | Content |
|---|---|
| Check | P28 |
| Location | p. 2, l. 36 to 37 and p. 4, l. 103 to 104; p. 2, l. 58 to 59 and p. 4, l. 125 to 126; p. 15, l. 454 to 455 |
| Quotation | "X-ray diffraction (XRD) has recently gained attention as a proxy for mineral abundance in provenance analysis but remains underutilized (Das et al., 2023)."; "However, these approaches typically yield relative source contributions without translating them into spatially explicit erosion rate maps"; "The novelty of our method lies in the spatially informed approach of this underdetermined inversion problem, and in the incorporation of non-linear mixing model." |
| Concern | The introduction motivates the study with a gap (XRD underused; existing unmixing does not give erosion rate maps) and the discussion states the novelty. None of these claims names databases, search terms, period or date of a search: search in p. 1, l. 1 to p. 16, l. 499 for "database", "Web of Science", "Scopus", "Google Scholar", "search", "literature review", "systematic", "keyword": 1 hit (p. 9, l. 257, "RRUFF database", a mineral reference database). The first claim rests on one citation, whose abstract contains none of the terms "underutilized", "underused", "rarely" (see PP-02). The second claim is weakened by the predecessor the manuscript itself builds on, De Doncker et al. (2020), whose title in the reference list is "Inversion of provenance data and sediment load into spatially varying erosion rates" (p. 18, l. 559). The literature that predates the XRD claim is treated in GB-08, the wording of the non-linearity claim in GB-60; here the concern is the missing search. |
| Suggestion | In Section 1 at p. 2, l. 36 to 37 and l. 58 to 59, and in Section 5 at p. 15, l. 454 to 455, either state the literature search (databases, terms, period, date) that supports the gap, or rephrase the claims to what the cited works show, and say at p. 2, l. 58 to 61 that spatially varying erosion rates from provenance data were introduced by De Doncker et al. (2020), so that the novelty is located in the binned XRD fingerprints and the non-linear scheme. |
| Status | verified (absence of a search description, search as stated; wording on the page images p. 2, 15); the scope of De Doncker et al. (2020) inferred from its title in the reference list |
| Severity | moderate |
| Source | S1 |

**GB-08 Quantitative XRD unmixing of sediment provenance, including tests with known artificial mixtures, predates Das et al. (2023) and is not cited.**

| Field | Content |
|---|---|
| Check | P14 |
| Location | p. 2, l. 36 to 42 and p. 4, l. 103 to 109; p. 13, l. 404 to 406 |
| Quotation | "Building on the work of Das et al. (2023, 2024), we investigate the potential of binned XRD data as a cost-effective fingerprinting method."; "Typically, the reliability of a given fingerprinting method is tested using known mixture experiments" |
| Concern | The manuscript traces XRD fingerprinting to Das et al. (2023, 2024). Andrews and Eberl (2012) determined sediment provenance by unmixing quantitative XRD mineralogy of source end members with the program SedUnMix and tested it on artificial mixtures of known proportions; Eberl (2004) applied the approach to suspended sediment of the Yukon River. This anticipates the XRD unmixing step and is exactly the known mixture test that the manuscript replaces by a "natural analogue" (p. 13, l. 406). Neither work is in the reference list (search for "Andrews", "Eberl", "SedUnMix" in p. 17, l. 501 to p. 21, l. 653: 0 hits). The contribution of the manuscript (binned peak areas within a spatially explicit non-linear inversion) remains. Distinct from GB-07, which concerns the missing search; here a specific omitted precedent is named. The neighbouring GB-01 at an overlapping place concerns the unsupported claim of time and cost efficiency; this finding concerns missing prior work on quantitative XRD unmixing with known mixtures. |
| Suggestion | Cite Andrews, J. T. and Eberl, D. D.: Determination of sediment provenance by unmixing the mineralogy of source-area sediments: The "SedUnMix" program, Marine Geology, 291 to 294, 24 to 33, https://doi.org/10.1016/j.margeo.2011.10.007, 2012, and Eberl, D. D., American Mineralogist, 89, 1784 to 1794, 2004, in Section 1 at p. 2, l. 36 to 42, and discuss in Sect. 4.2.1 why an artificial known mixture test as in that study was not done. |
| Status | verified: abstract and bibliographic record read, https://pubs.usgs.gov/publication/70032707; Eberl (2004): abstract read, https://pubs.usgs.gov/publication/70026557 |
| Severity | moderate |
| Source | S1 |

**GB-09 The source cited for the frequentist and Bayesian distinction uses a sampling-free uncertainty estimate, which falls outside the stated dichotomy and anticipates the feature claimed as distinctive.**

| Field | Content |
|---|---|
| Check | P13 |
| Location | p. 2, l. 45 to 48 and p. 4, l. 112 to 115; p. 2, l. 55 to 57 and p. 4, l. 122 to 124 |
| Quotation | "Where frequentist methods estimate the uncertainty on the resulting source contributions by sampling the different possible sets of source contributions, Bayesian methods use priors, model and data uncertainty to allow error propagation so the a posteriori uncertainty can be inferred from different posterior metrics (Niu et al., 2020)."; "without requiring the generation and sampling of multiple posterior solutions." |
| Concern | The introduction sorts unmixing methods into two classes and positions the authors' approach against both. Niu et al. (2020), cited for the classification, use according to their abstract a linear mixing model with multiple composite fingerprints and quantify uncertainty with a Gaussian first-order approximation; the abstract describes neither Bayesian priors and posterior metrics nor frequentist sampling. A first-order Gaussian propagation is itself an uncertainty estimate without sampling, so the cited study is a precedent for the feature the manuscript presents as distinguishing its approach (p. 2, l. 56 to 57). The citation for linear mixing at p. 2, l. 59 is consistent with the abstract. |
| Suggestion | At p. 2, l. 45 to 48 (and the duplicate) cite a source that makes the frequentist and Bayesian distinction, and at p. 2, l. 55 to 57 state that analytical first-order uncertainty propagation without sampling has been used in linear unmixing (Niu et al., 2020), so that the contribution is limited to the non-linear, spatially explicit inversion. |
| Status | verified for the content of Niu et al. (2020): abstract read, https://link.springer.com/article/10.1007/s11368-019-02424-1 (version of record); inferred for the full text, which was not read |
| Severity | moderate |
| Source | S1 |

**GB-10 The names of the four frequentist methods are inconsistent or non-standard: one method is abbreviated "NLLS" and referred back to as "NNLS", and GLUE and MLE are misnamed.**

| Field | Content |
|---|---|
| Check | P38 |
| Location | p. 2, l. 48 to 51; p. 4, l. 115 to 118 |
| Quotation | "1) the Non-Linear Least Squares (NLLS) (a constrained linear regression)"; "3) Generalist Likelihood Uncertainty Estimation (GLUE)"; "4) Maximal Likelihood Estimation (MLE) (similar to the NNLS approach, but with a probabilistic error model)" |
| Concern | The back-reference in item 4 can only point to item 1, so one method carries two abbreviations, in both copies of the introduction (compared on the page images p. 2 and 4). The expansion "Non-Linear" also sits uneasily with the gloss "a constrained linear regression"; non-negative least squares would fit the gloss and the abbreviation NNLS (assumption). GLUE was introduced by Beven and Binley (1992) as "Generalized Likelihood Uncertainty Estimation", and the estimator is "Maximum Likelihood Estimation". The neighbouring GB-09 at an overlapping place concerns the source cited for the frequentist and Bayesian distinction; this finding concerns the names and abbreviations of the four frequentist methods. |
| Suggestion | Which method is meant in item 1? Use one name and abbreviation in both places, for example "Non-Negative Least Squares (NNLS)"; write "Generalized Likelihood Uncertainty Estimation (GLUE)" and "Maximum Likelihood Estimation (MLE)" at p. 2, l. 50 to 51 and p. 4, l. 117 to 118. |
| Status | verified (inconsistency and wording at the page images p. 2 and 4); intended method: assumption, asked as a question; standard names from general knowledge (assumption) |
| Severity | minor |
| Source | S1, S2, S4 |

**GB-11 The introduction presents the approach as particularly valuable in glacierized catchments, while the Discussion recommends it only under conditions (well-constrained lithology, no storage) that are stated late and not checked for the own glacier catchment.**

| Field | Content |
|---|---|
| Check | P15, P17, P18 |
| Location | p. 2, l. 61 to p. 3, l. 62 and p. 4, l. 128 to 129; p. 15, l. 463 to 464; p. 15, l. 466 to 468 |
| Quotation | "This spatially informed approach to sediment provenance is particularly valuable in glacierized catchments, where ice cover limits direct observations"; "we recommend applying this method in catchments where: a) the spatial distribution of source lithologies is well constrained"; "We caution against using this method in catchments with significant sediment storage, as the inversion directly links sediment provenance to erosion rates and assumes immediate sediment export (Collins et al., 2020)." |
| Concern | The Discussion states that spatial delineation "can be challenging in glaciated catchments with limited outcrop exposure" (p. 15, l. 460), and scenario 1 ranks map uncertainty as "the second most influential factor" (p. 12, l. 364). In the study area the lithology under the ice is inferred, not mapped (p. 9, l. 270 to 272), and the alternative map of Steck et al. (2015) differs from it by about 1.1e7 m2 (Fig. 7, read from the colour axis). Recommendation a) therefore narrows the use case that motivates the paper. The assumption of immediate export appears only at p. 15, l. 466 to 468, not in Sect. 3.1 where the forward model is introduced, and whether the Gornergletscher meets it is not discussed; the recommended depth-integrated sampling (p. 15, l. 470) is not related to the own samples. The Conclusions do not mention glaciers (search "glaci" in p. 16, l. 477 to 489: 0 hits). The missing glacial literature is treated in GB-06. |
| Suggestion | State the immediate-export assumption in Sect. 3.1; add to Sect. 5 a check of the Gornergletscher against conditions a) to c) and the storage caution, including the area share of inferred lithology and the map uncertainty up to which the method remained usable in scenario 1 (Fig. 7); state whether the own suspended samples were depth-integrated; then adjust p. 2, l. 61 to 63 (and p. 4, l. 128 to 130) or qualify recommendation a) for glacierized catchments. |
| Status | verified (wording and location); the area difference read from the axis of Fig. 7 (inferred) |
| Severity | moderate |
| Source | S4, SD |

#### Minor corrections

| ID | Location | Quotation | Replacement | Source |
|---|---|---|---|---|
| KK-01 | p. 1, l. 5; p. 11, l. 320 | "(steepest descent and Quasi-Newtonian)"; "we adopt the Quasi-Newton (QN) approach" | "(steepest descent and quasi-Newton)"; "we adopt the quasi-Newton (QN) approach", as at p. 7, l. 211 and p. 10, l. 296 (headings may keep capitals); see GB-32 (the accuracy of QN against SD in Figs. 5g and 6g), which treats a different aspect of the same place | S2, S4 |
| KK-02 | p. 2, l. 55 to 56; p. 4, l. 122 to 123 | "a hybrid between Bayesian linear mixed models and hierarchical Bayesian models" | "a hybrid between Bayesian linear mixing models (BLMM) and hierarchical Bayesian models", as introduced at p. 2, l. 53 and p. 4, l. 120; see GB-09 (the source cited for the frequentist and Bayesian distinction), which treats a different aspect of the same place; see GB-65 (aims 1 and 2, the scheme comparison and the Bayesian positioning missing from the Discussion), which treats a different aspect of the same place | S1, S2 |
| KK-03 | p. 2, l. 61; p. 4, l. 128; p. 6, l. 181; p. 11, l. 333 to 334; p. 14, l. 424; p. 14, l. 424 to 425 | "validated in (De Doncker et al., 2020)"; "becomes Tarantola (2005):"; "proposed by (Steck et al., 2015)"; "described in (Belotti, 2021)"; "outlined in (De Doncker et al., 2020)" | "validated by De Doncker et al. (2020)"; "becomes (Tarantola, 2005):"; "proposed by Steck et al. (2015)"; "described by Belotti (2021)"; "outlined by De Doncker et al. (2020)"; see GB-06 (missing literature on detrital erosion mapping in glacial catchments), which treats a different aspect of the same place; see GB-11 (the recommended site conditions against the own glacier catchment), which treats a different aspect of the same place; see GB-46 (the temporal representativeness of single samples), which treats a different aspect of the same place | S1, S4 |
| KK-04 | p. 3, l. 70; p. 5, l. 137 | "we optimize the hyper-parameters" | "we optimize the hyperparameters", as at p. 10, l. 281 and p. 12, l. 370; see GB-02 (the abstract statement of consistent convergence), which treats a different aspect of the same place; see GB-52 (the highlighted values in Fig. 10 and the choice of the hyperparameters), which treats a different aspect of the same place | S2 |

#### Verification log

| ID | Check | Checked | Values | Result |
|---|---|---|---|---|
| PP-01 | P13 | Numbers, rankings and valuations from cited works in Segment 1 (p. 1, l. 1 to p. 5, l. 142) | Numbers other than years and enumerators (Python on text.json): 0. Rankings and valuations: "most common methods" (p. 2, l. 48; Haddadchi et al., 2013; Yang et al., 2025), "Despite their effectiveness" (p. 2, l. 35), "ideal fingerprint" criteria (p. 1, l. 24 to 25; Klages and Hsieh, 1975), "validated" (p. 2, l. 61; De Doncker et al., 2020). Haddadchi et al., Klages and Hsieh, Fathabadi and Jansen and Collins et al. checked against their titles only; Yang et al. (2025) not readable | no finding beyond GB-05 and GB-09; attribution of the four frequentist methods to their sources not verified (limit) |
| PP-02 | P13 | Statements attributed to Das et al. (2023): p. 2, l. 35 ("expensive and time-consuming") and p. 2, l. 36 to 37 ("remains underutilized"), with duplicates p. 4, l. 102 to 104 | Crossref record of DOI 10.1029/2023WR034500: abstract present; terms "expensive", "cost", "time-consuming", "rapid", "inexpensive", "underutilized", "underused", "rarely": 0 hits in the abstract, which describes an erosion susceptibility index from XRD spectra; full text not reachable (fetch error at doi.org and the publisher page) | no finding; whether the full text states cost, time and underuse is not verified (limit of this review); the underuse claim is taken up in GB-07 only for the missing search |
| PP-03 | P14 | Contribution in one sentence and six literature searches (SedUnMix and XRD unmixing; detrital thermochronology in glacial catchments; XRD fingerprinting in glacierized catchments; Gornergletscher provenance; inversion of detrital tracers into erosion maps; whole-pattern XRD unmixing) | Candidates held against the reference list (p. 17, l. 501 to p. 21, l. 653): Andrews and Eberl (2012), absent; Eberl (2004), absent; Ehlers et al. (2015), absent; Bernard et al. (2020), absent; De Doncker et al. (2020), present (p. 18, l. 559 to 560); Lipp et al. (2021), present; Saylor et al. (2019), present; an EGU21 abstract by the same authors on erosion maps at Gornergletscher, absent and not proposed (own preliminary report). Search results pointing to the manuscript itself or its discussion were not opened | proposals in GB-08 and GB-06 |
| PP-04 | P28 | Gap and novelty claims collected with "novel", "first time", "no stud", "not been", "has not", "underutil", "lack", "unexplored", "gap", "rarely", "to date", "our knowledge" and similar terms in p. 1, l. 1 to p. 16, l. 499 | Gap or novelty claims: p. 2, l. 37 and p. 4, l. 104 ("underutilized"), p. 15, l. 454 ("novelty"), p. 2, l. 58 to 59 and p. 4, l. 125 to 126 ("typically yield ... without"); other hits not gap claims (p. 1, l. 17 "lack of direct observations"; p. 14, l. 433 "lack of age data") | finding GB-07 |

### Segment 2: Methods, data, study area (p. 5 to 10, Figs. 1 to 4)

#### Substantive findings

**GB-12 The text mixes -ise and -ize spellings, and "centre" with "center".**

| Field | Content |
|---|---|
| Check | P16 |
| Location | p. 5, l. 150; p. 9, l. 246; p. 9, l. 250; p. 10, l. 289; p. 10, l. 303; p. 11, l. 307; p. 15, l. 459; p. 12, l. 340 to 341; p. 15, l. 441 |
| Quotation | "To characterise the mineralogical fingerprints"; "we obtained the mineral concentrations characterizing each lithological unit"; "shift the centre of the Zermatt-Saas-Fee ophiolites"; "center of the domain" |
| Concern | Count on text.json, body p. 1 to 16 (headers excluded), stems characteris, optimis, minimis, normalis, regularis, localis against characteriz, optimiz, minimiz, normaliz, stabiliz, homogeniz, visualiz, summariz ("characteristic" removed as false hit): -ise 8 occurrences (characterised p. 5, l. 150; regularised p. 9, l. 246; characterise p. 9, l. 250; localised p. 10, l. 289; normalised p. 10, l. 303; optimisation and minimising p. 11, l. 307; optimising p. 15, l. 459), -ize 22 occurrences (normaliz 7, characteriz 1, optimiz 3, stabiliz 4, minimiz 4, homogeniz 1, visualiz 1, summariz 1; 7+1+3+4+4+1+1+1 = 22, Python). "centre" at p. 12, l. 340 and 341, "center" at p. 15, l. 441. Either convention is acceptable, but not both. |
| Suggestion | Apply one convention at the listed lines, for example -ize with "center" throughout, or -ise with "centre". |
| Status | verified (count on text.json, spot checks on the page images p. 5, 9 to 13, 15) |
| Severity | minor |
| Source | S4 |

**GB-13 Index symbols change meaning between equations and figures: the iteration index is k and n, n also counts pixels, and the tracer index is i, t and n.**

| Field | Content |
|---|---|
| Check | P38 |
| Location | p. 5, l. 154 to 156; p. 6, l. 164; p. 6, l. 175 to 176; p. 7, l. 208 to 209; p. 8, l. 215 to 216; p. 8, l. 219; p. 9, l. 262 to 263; Fig. 3 (d) (p. 24) |
| Quotation | "εk+1 the posterior model after k + 1 non-linear iteration steps"; "where Gn is the Jacobian at iteration n"; "the abundance of a given tracer t at pixel xy in At,xy as well as in the detrital data dt (eq. 1-4)" |
| Concern | The derivation from Eq. 1 to Eq. 16 is largely in one notation, but the indices drift afterwards. (1) Iteration: Eq. 17 and l. 209 use k; Eq. 18 and 19 use n for iterate, Jacobian, data and step size but keep εk in the prior term, so a reader cannot tell whether εk is the current iterate or a fixed earlier model. (2) n is also the number of pixels (Eq. 1, upper summation limit; Eq. 4, last element εn). (3) Tracer: i in Eq. 1, t at l. 262 to 263 (which refers back to "eq. 1-4"), n in Fig. 3d ("tracer mineral n"), where i denotes the detrital sample. (4) Pixel: j in Eq. 1, xy at l. 262 to 263. (5) Posterior: p(εm\|dobs) in Eq. 5, p(ε\|dobs) at l. 176. Graded moderate rather than minor because Eq. 18 and 19 cannot be implemented unambiguously. The singularity of the matrix inverted in Eq. 19 is treated in GB-18, the typographical errors of Eq. 9 and 14 in GB-16. |
| Suggestion | Fix one index per object throughout Section 3 and Figs. 1 to 3 (for example i for tracers, j for pixels, k for iterations); rewrite Eq. 18 and 19 with εk, Gk, dk, µk and state which model the prior term uses; replace At,xy and dt at p. 9, l. 263 by Aij and di; use one symbol for the model in Eq. 5 and at p. 6, l. 176. |
| Status | verified at the page images p. 5 to 9 and 24 |
| Severity | moderate |
| Source | S2 |

**GB-14 The forward model is called dimensionless, but the data standard deviation is given in mm/y, and after Eq. 2 the units of the data vector are not stated.**

| Field | Content |
|---|---|
| Check | P38 |
| Location | p. 6, l. 161; p. 10, l. 294 to 295; p. 11, l. 325 |
| Quotation | "This allows us to rewrite the forward model in a simplified, dimensionless form:"; "a model standard deviation of 3 (dimensionless, as epsilon is dimensionless), a data standard deviation of 0.01 mm/y" |
| Concern | Section 3.4 defines the data as concentrations scaled to the sample maximum "on a scale from 0 to 1" (p. 9, l. 261 to 262), and p. 6, l. 161 calls the rescaled forward model dimensionless. The data standard deviation is nevertheless given in mm/y at every place (p. 10, l. 295; p. 11, l. 325; p. 14, l. 428). Eq. 2 multiplies the data by the total erosion rate, which would give d the unit of an erosion rate if ė0 carries one; ė0 is "set to 1" (p. 5, l. 157) without unit. A reader cannot tell which quantity σd = 0.01 refers to, and therefore how it relates to the measurement error of normalised peak areas. The same observation was noted outside the checklists by S2, S3 and AB; no responsible instance treated it as a finding, and it was confirmed at the page images p. 5, 6, 10, 11, 14 (origin ZF). The choice of one σd for all data types is treated in GB-48. |
| Suggestion | State after Eq. 2 the units of d, ė0 and σd, and express σd in the units of the data actually inverted (Sect. 3.1 and 4.1.1). |
| Status | verified (wording at all locations); the unit of d after Eq. 2 inferred |
| Severity | moderate |
| Source | ZF |

**GB-15 The prior term of the misfit is called "prior misfit" once and "model misfit" everywhere else.**

| Field | Content |
|---|---|
| Check | P38 |
| Location | p. 6, l. 184; p. 7, l. 202 |
| Quotation | "and the prior misfit"; "and the gradient of the model misfit can be written as:" |
| Concern | The term ϕprior is introduced as "prior misfit" (p. 6, l. 184) and from Eq. 15 on called "model misfit". Search in text and captions (text.json, p. 1 to 37): "prior misfit" 1 hit (p. 6, l. 184); "model misfit", "model-misfit" and "data- and model misfit" together 16 hits (13 text lines from p. 7, l. 202 to p. 13, l. 386, and the captions of Figs. 5, 6 and 10); the figure axes read "Model misfit". |
| Suggestion | At p. 6, l. 184 write "the prior (model) misfit ϕprior" or use "model misfit" there, and keep one name throughout. |
| Status | verified (search on text.json, page images p. 6 to 9) |
| Severity | minor |
| Source | S2 |

**GB-16 Eq. 9 lacks the minus sign in the exponent of the covariance kernel, and Eq. 14 lacks the transpose of G that Eq. 16 carries.**

| Field | Content |
|---|---|
| Check | P38 |
| Location | p. 7, l. 189; p. 7, l. 201; p. 7, l. 205 |
| Quotation | "Cm(i, j) = σm2 exp(si,j2 / L2)"; "∇ε ϕd = G Cd−1 (dε − dobs)" |
| Concern | As printed on the page image p. 7, Eq. 9 is σm² exp(s²/L²), which grows with distance and is not a valid smoothing covariance; the text describes L as "the smoothing distance" (p. 7, l. 190), so exp(−s²/L²) is evidently meant. Eq. 14 writes G C_d^-1 (dε − dobs), while Eq. 16, which combines Eq. 14 and 15, writes G^T C_d^-1 (dε − dobs) (p. 7, l. 205); only the transposed form has the dimension of the model vector. Both were noted by S4 outside its checklist; the responsible instance S2 checked notation from Eq. 1 and Eq. 17 to 19 but not these two equations (origin ZF). Graded moderate because a reader implementing Eq. 9 as printed obtains a different model covariance. Index inconsistencies in the later equations are treated in GB-13. |
| Suggestion | Correct Eq. 9 to Cm(i, j) = σm² exp(−s_ij²/L²) and Eq. 14 to G^T C_d^-1 (dε − dobs) in Sect. 3.2, and check the code against the corrected forms. |
| Status | verified (page image p. 7) |
| Severity | moderate |
| Source | ZF |

**GB-17 The steepest descent results come from a gradient-normalised variant that differs from Eq. 18; the change is disclosed only in the Results, and its settings are not given.**

| Field | Content |
|---|---|
| Check | P7, P8, P17 |
| Location | p. 8, l. 213 to 216; p. 11, l. 312 to 314 |
| Quotation | "In initial experiments, the steepest descent approach proved unstable, requiring the normalization of the gradient." |
| Concern | Sect. 3.2 introduces SD with Eq. 18 and a step size µn; the variant used for Fig. 6 normalises the gradient, which forces steps of similar magnitude (p. 11, l. 313 to 314). The form of the normalisation, the step size and the iteration number are not stated (the axes of Fig. 6g to 6i run to 200 iterations, those of Fig. 5g to 5i to 100). The comparison that leads to adopting QN (p. 11, l. 320 to 321) is thus between QN as described and an SD variant not described, with different iteration budgets, while the abstract presents both schemes as implemented and compared (p. 1, l. 4 to 5). What Figs. 5g and 6g show about the accuracy of the two schemes is treated in GB-32; here the concern is the documentation of the variant. The neighbouring GB-13 at an overlapping place concerns index symbols that change meaning between equations and figures; this finding concerns the undocumented gradient-normalised steepest descent variant. |
| Suggestion | Add the normalised update rule, step size and iteration number to Sect. 3.2 next to Eq. 18, and compare QN and SD at equal iteration counts or computing time. |
| Status | verified (wording; iteration axes at the page images p. 26 and 27) |
| Severity | moderate |
| Source | SD |

**GB-18 The quasi-Newton update of Eq. 19 inverts G^T C_d^-1 G, which is singular for the underdetermined problem the manuscript describes.**

| Field | Content |
|---|---|
| Check | P25 |
| Location | p. 8, l. 217 to 219 |
| Quotation | "εn+1 = εn − µn (GnT Cd−1 Gn)−1 (GnT Cd−1 (dn − dobs) + Cm−1 (εk − εprior))" |
| Concern | G has m rows (tracers, 21) and n columns (pixels, n larger than m by p. 6, l. 170 to 172), so G^T C_d^-1 G is n by n with rank at most m and cannot be inverted. Because the abundance at each pixel is taken from the unit fingerprint (p. 9, l. 262 to 263), the rank is at most the number of units (7). A numerical check with m = 21 and n = 300 gives rank 21 of 300 and condition number 8.8e19; adding C_m^-1, as Eq. 20 does for the posterior covariance, gives full rank (Python, SD instance). As printed, Eq. 19 cannot be computed. Does the code use the Hessian with C_m^-1, damping or a pseudo-inverse? The index inconsistency of the same equation is treated in GB-13. |
| Suggestion | Correct Eq. 19 in Sect. 3.2 to the form implemented, for example (G^T C_d^-1 G + C_m^-1)^-1, and state any damping or pseudo-inverse. |
| Status | inferred (linear algebra from the manuscript's own statements; code not inspected); asked as a question |
| Severity | moderate |
| Source | SD |

**GB-19 The plotted resolution diagonal lies near 1 almost everywhere, which the resolution operator cannot reach in an underdetermined problem with 7 source units; what is plotted, and how is it to be read?**

| Field | Content |
|---|---|
| Check | P3, P8, P31 |
| Location | p. 8, l. 230 to 236; p. 10, l. 299 to 300; p. 14, l. 436; p. 16, l. 483 to 484; Fig. 5 (d) (p. 26); Fig. 6 (d) (p. 27); Figs. 14 to 16, second panel (p. 35 to 37) |
| Quotation | "Where the diagonal of R is close to 1, data have improved our knowledge considerately relative to the prior."; "We highlight how model resolution and posterior covariance can be used to assess the reliability of inferred erosion patterns." |
| Concern | R is defined only implicitly (Eq. 21); the formula used is not given. The colour scales of the resolution panels span 0.90 to 1.00 (Fig. 5d), 0.88 to 1.00 (Fig. 6d), 0.5 to 1.0 (Figs. 14 and 16) and 0.80 to 1.00 (Fig. 15); measured on 300 dpi renderings, the share of map pixels not in the darkest tone is 0.004 (Fig. 14), 0.013 (Fig. 15) and 0.002 (Fig. 16), so more than 98 % of the domain is near 1. With R = C_m G^T (G C_m G^T + C_d)^-1 G, which follows from Eq. 20 and 21, the trace of R is at most rank(G), here at most 7 (seven units, 21 tracers). With about 809 pixels of 300 m (catchment area 72.8 km2 measured on Fig. 4 with the scale bar; pixel size from p. 10, l. 294) the mean diagonal is at most 7/809 = 0.0087; a Python test with the manuscript's settings (812 pixels, 7 units, 21 tracers, L = 4 pixels, σm = 3, σd = 0.01) gives trace(R) = 7.00 and a maximum diagonal of 0.025. The plotted values behave instead like 1 minus diag(R) or a normalised posterior variance, and the total normalised uncertainty of 0.82 to 0.87 (p. 14, l. 436; p. 15, l. 442, 447) also indicates little resolution. If the quantity is inverted, the reading at p. 10, l. 299 to 300 ("lower resolution" for small units) and p. 14, l. 436 ("low resolution") changes, and the Conclusions (p. 16, l. 483 to 484) offer resolution as a reliability tool. Graded major because these maps are used as evidence for where the inversion is reliable. The naming of the uncertainty metrics is treated in GB-20. |
| Suggestion | Give the formula for R in Sect. 3.3, state the quantity plotted in Figs. 5d, 6d and 14 to 16, check it against trace(R) at most min(number of tracers, number of units), and revise the interpretations at p. 10, l. 299 to 300, p. 14, l. 436 and p. 16, l. 483 to 484 accordingly. |
| Status | colour scale ranges and coloured shares verified (measurement, AB); rank bound and the alternative reading inferred (derived from Eq. 20 and 21, Python test); asked as a question |
| Severity | major |
| Source | AB, SD |

**GB-20 "Normalized posterior uncertainty" denotes two quantities, a per-pixel ratio of standard deviations (Eq. 22) and a global ratio of traces of variances, appears under eight names, and the global one is defined only in the last results section.**

| Field | Content |
|---|---|
| Check | P20, P38 |
| Location | p. 8, l. 236 to 239; p. 10, l. 303; p. 11, l. 335; p. 14, l. 435 to 436; p. 15, l. 441; p. 15, l. 446 to 447; Figs. 7 to 10, axis titles (p. 28 to 31) |
| Quotation | "The third metric is the ratio between the posterior model covariance and the “prior” model covariance."; "a high total normalized uncertainty"; "The same pattern is visible in the normalised posterior variance" |
| Concern | Section 3.3 introduces the posterior covariance as C̃m (Eq. 20) and, as third metric, a ratio of square roots of posterior and prior covariance (Eq. 22), read per pixel (a ratio of standard deviations). The results use a scalar, the ratio of traces of variances without square root, written with a different symbol, tr(Cm,post)/tr(Cm), and defined only in passing at p. 14, l. 436. It is used from Sect. 4.1.1 on (Fig. 5h "Normalised covariance trace", about 0.74; Figs. 7 to 10, axis "Trace(post. cov.)" or "Trace(post.covar.)", which omits the normalisation). Names found (text and captions from text.json, panel titles and axes at the page images): "normalised posterior covariance", "Normalised covariance trace", "normalised posterior variance" (p. 10, l. 303), "normalized posterior uncertainty" (p. 11, l. 335; p. 15, l. 441), "total normalized uncertainty" (p. 14, l. 436), "Total normalised posterior uncertainty", "Posterior uncertainty", "Normalised posterior uncertainty". The reading matters: 0.87 as a variance ratio is a 13 % variance reduction, equivalent to a standard-deviation ratio of 0.933 (Python). Because the prior variance is the same in every pixel, the trace ratio equals the pixel mean of the squared Eq. 22 values; the manuscript does not state this link. The plausibility of the plotted resolution is treated in GB-19. |
| Suggestion | In Sect. 3.3 after Eq. 22 define the scalar metric explicitly (for example tr(C̃m)/tr(Cm), with the symbol of Eq. 20), give the pixel-wise and the total metric one name each and state their relation; use these names in p. 10, l. 303, p. 11, l. 335, p. 14, l. 436, p. 15, l. 441 and 446 and in all panel titles, axis labels and captions of Figs. 5 to 10 and 14 to 16. |
| Status | verified (names, symbols and labels at the page images p. 8, 10, 11, 14, 15, 26 to 31, 35 to 37); identity of the plotted axis with the trace ratio and the conversion inferred (axis values, Python) |
| Severity | moderate |
| Source | S2, S3 |

**GB-21 Numbers, dates and sampling methods of the source and detrital samples are not reported, and the zircon extraction, dating and age binning are referenced only to an unpublished master's thesis.**

| Field | Content |
|---|---|
| Check | P8, P12, P20, P34 |
| Location | p. 9, l. 251 to 252; p. 13, l. 391 to 392; p. 14, l. 413; p. 14, l. 423 to 425; p. 17, l. 522 to 523 |
| Quotation | "In a first step, in-situ source samples are collected from every lithological unit across the study area (Figure 3A and 3B)."; "Merging the inversion results from multiple detrital samples collected at the sink of this sub-catchment"; "following the methodology described in (Belotti, 2021)"; "Master’s thesis, University of Lausanne, unpublished master’s thesis, 2021." |
| Concern | Search in p. 9, l. 250 to p. 14, l. 449 for "sample": 19 hits on 17 lines, none states a number of samples. Not stated: the number of source samples per unit, how several samples became one fingerprint and the spread within a unit; number, dates and times of the Gorner-Grenz samples ("multiple detrital samples", p. 14, l. 413), while only one sample is dated (p. 14, l. 423 to 424); sampling method and position (Fig. 3a shows a pump sampler; depth integration, recommended at p. 15, l. 470, is not mentioned for the own samples); the number of inversions merged in Fig. 13. The zircon comparison is one of the three natural-data aims (p. 10, l. 284 to 285), but separation, dating instrument, standards, filtering and the binning into 13 age classes shown in Fig. 14 (counted at the page image) are given only by reference to a thesis marked "unpublished" (p. 17, l. 523), without access route. Without these numbers the within-unit variability of Fig. 11 and the base of the KDE in Fig. 13 cannot be judged. The availability statement is treated in GB-67, the density scale of Fig. 13 in GB-57. |
| Suggestion | Add a sample table to Sect. 3.4 or 4.2 (identifier, unit, coordinates, date and time, sampling method, analyses, zircon grains), state the number of inversions merged in Fig. 13, summarise the zircon protocol and the age binning in Sect. 4.2.2 after p. 14, l. 425, and deposit the thesis with a persistent link or say why it is not accessible. |
| Status | verified (absence by the search stated; wording of reference and credit at the page images p. 9, 13, 14, 17; bin count at the page image p. 35) |
| Severity | moderate |
| Source | S2, S3, SD |

**GB-22 The XRD measurement and processing environment is not specified to a level that allows the fingerprints to be reproduced.**

| Field | Content |
|---|---|
| Check | P35 |
| Location | p. 9, l. 252 to 258; p. 13, l. 396 to 397 |
| Quotation | "In a third step, the WinXRD Peak Finder algorithm corrects for baseline drift and removes the background noise, facilitating the identification of local maxima through thresholding and peak fitting." |
| Concern | Not given: instrument and radiation, 2θ range, step width and counting time, grinding method and grain size, mounting, WinXRD version, Peak Finder thresholds and fitting function, the 2θ windows per mineral, replicate measurements. Search in p. 1 to 21 for "diffractometer", "Cu", "kV", "Kα", "scan": 2 hits, both in reference titles (p. 17, l. 533; p. 19, l. 583). Thresholds and windows determine the tracer values directly. The Discussion relies on the protocol to cancel orientation effects (p. 15, l. 472 to 473) without describing it. The consequences visible in the fingerprints (identical tracers) are treated in GB-54. The neighbouring GB-21 at an overlapping place concerns the undocumented samples and zircon protocol; this finding concerns the unspecified XRD measurement and processing environment. |
| Suggestion | Add a table to Sect. 3.4 with instrument, radiation, scan parameters, preparation, software version, Peak Finder settings and the 2θ windows per mineral (with RRUFF identifiers); report replicate measurements of at least one source and one detrital powder. |
| Status | verified (search as stated) |
| Severity | moderate |
| Source | SD |

**GB-23 Normalising each sample by its maximum peak area before mixing is not compatible with the erosion-weighted linear mixing of Eq. 1, and the synthetic tests cannot reveal this.**

| Field | Content |
|---|---|
| Check | P9, P25 |
| Location | p. 9, l. 260 to 262 |
| Quotation | "At the end, these are normalized within each sample by dividing by the maximum observed peak area, yielding relative mineral concentrations on a scale from 0 to 1 (Figure 3D and 3E)." |
| Concern | If the peak areas of a mixture are the erosion-weighted sum of the source peak areas, the mixture's maximum-normalised vector is not the weighted average of the sources' maximum-normalised vectors, because each sample is divided by a different factor, and the mineral giving the maximum differs between units (Fig. 11, measured: antigorite in the serpentinites, quartz in four units, anorthite and pyroxene in the Stockhorn-Tuftgrat-Gornergrat unit and the metabasites). A two-source example (Python): raw areas A = (100, 10, 5) and B = (20, 50, 40) mixed 50:50 and normalised after mixing give (1.00, 0.50, 0.375); Eq. 1 with normalised sources and the true weights predicts (0.70, 0.55, 0.425); the best-fitting weight of A under Eq. 1 is 0.652 instead of 0.500. The bias depends on composition and is not removed by treating source and detrital samples alike. The synthetic tests generate detrital data with Eq. 1 from already normalised fingerprints (Fig. 5k) and cannot show it; the manuscript names laboratory known-mixture experiments as the usual test (p. 13, l. 404 to 406) but does not run one. Graded major because the bias would affect every inversion of natural XRD data (Figs. 13, 15, 16). The neighbouring GB-13 at an overlapping place concerns index symbols that change meaning between equations and figures; this finding concerns the incompatibility of maximum normalisation with linear mixing. |
| Suggestion | Formulate the forward model on un-normalised or calibrated peak areas and apply the normalisation to the modelled mixture, or include the normalisation in the forward operator (Sect. 3.1 and 3.4); test the chain with physical mixtures of the source powders in known proportions measured with the same protocol, and report the recovered proportions in Sect. 4.2. |
| Status | inferred (from the stated normalisation and Eq. 1, illustrated with constructed numbers, Python); the absence of a laboratory mixture test verified |
| Severity | major |
| Source | SD |

**GB-24 "Steck et al. (2015)" labels both the source of the base geology and the alternative map with the largest mismatch in scenario 1, and the scenario maps and their mismatch measure carry several names.**

| Field | Content |
|---|---|
| Check | P38 |
| Location | p. 9, l. 271 to 272; p. 11, l. 331 to 334; p. 11, l. 338 to 339; Fig. 7, panel titles, colour bar and caption (p. 28); Fig. 4, credit text (p. 25) |
| Quotation | "3) the map proposed by (Steck et al., 2015) with the biggest area mismatch"; "Geological data: data from Steck et al., 2015, personal communication by L. Baumgartner, outcrops by GeoCover" |
| Concern | Scenario 1 is a useful test of map uncertainty, and Fig. 7 shows all three maps. The base geology of the study (Fig. 4, used for Figs. 5 and 12 to 16) is credited to "Steck et al., 2015" with additions from a personal communication, and p. 9, l. 272 and p. 14, l. 411 to 412 cite Steck et al. (2015) for it; scenario 1 uses "the map proposed by (Steck et al., 2015)" as the case with the largest mismatch from the "original geological map" (Fig. 7 right panel, "Geology by Steck et al. 2015"). The base map is called "the same geological map", "the original geological map", "Originial geology (same as forward)" and "Forward geology" (Fig. 7); the second map "a geological map with minimal difference", "the modified map", "a simplified geological map with minimal changes", "Geology with minimal changes" and "Minimal changes"; the measure "area mismatch" (p. 11, l. 330, 334, 335), "area difference" (Fig. 7 caption and x-axes) and "Geology misalignment (m²)" (colour bar). The ranking of scenario 1 against the other scenarios is treated in GB-38. The neighbouring GB-20 at an overlapping place concerns the two quantities called normalised posterior uncertainty; this finding concerns the names of the base map and of the scenario 1 maps. |
| Suggestion | Is the "original geological map" of scenario 1 the Fig. 4 map used for all natural-data inversions, and how does it differ from the map of Steck et al. (2015)? Give the base map its own name in Sect. 4 at p. 9, l. 270 to 272, and use one name for each scenario map and one for the mismatch measure at p. 11, l. 330 to 339 and in Fig. 7. |
| Status | names verified at the page images p. 9, 11, 14, 25, 28; whether base map and Steck et al. (2015) map are different objects: assumption, asked as a question |
| Severity | moderate |
| Source | S2 |

**GB-25 Each of the seven lithological units carries two to five names across text and figures, two units cannot be matched to the text description without the Fig. 4 legend, and several unit names are misspelled.**

| Field | Content |
|---|---|
| Check | P2, P38 |
| Location | p. 9, l. 273; p. 10, l. 274 to 276; p. 10, l. 299; p. 12, l. 340; p. 14, l. 411; p. 14, l. 414; p. 14, l. 431 to 433; Fig. 12 legend and caption (p. 33); Fig. 11 caption (p. 32); Fig. 13 labels (p. 34); Figs. 15 and 16 legends (p. 36 to 37); Fig. 4 legend (p. 25); Fig. 5 (j) legend (p. 26) |
| Quotation | "while Penninic Mesozoic sedimentary units (Bündnerschiefer) consist mainly of calcareous mica schists and quartzites"; "no age data were available for the Monte Rosa garnet-gneiss (MR g-g) unit"; "Stockhorn-Turftgrat-Gornergrat, Monte Rosa (granite), ZSF ophiolites (metabasites, ecologites)" |
| Concern | Distinct names per unit across text, Fig. 4 and 12 legends, Fig. 11 caption, Fig. 13 labels and Fig. 15 and 16 legends (counted at the page images): serpentinite unit 4, sediment unit 3, Stockhorn unit 5, Monte Rosa granite 3, metabasite unit 5, Monte Rosa gneiss unit 4, Furgg series 2. (a) The text describes "Penninic Mesozoic sedimentary units (Bündnerschiefer)" (p. 10, l. 274 to 275), while all figures and p. 10, l. 299 and p. 14, l. 414 use "ZSF sediments" or "Zermatt - Saas Fee sediments"; the link is visible only in the Fig. 4 legend. (b) "Monte Rosa garnet-gneiss (MR g-g)" (p. 14, l. 432; search "g-g" in p. 1 to 16: 3 hits on p. 14, l. 432 and 433) appears in no figure, where the unit is "Monte Rosa (garnet gneiss and micaschist)" (Figs. 4, 12), "Monte Rosa (gneiss, micaschist)" (Figs. 11, 13) or "MR gneiss, mica" (Figs. 15, 16). (c) Zermatt-Saas Fee is spelled five ways, compared at the page images: "Zermatt-Saas Fee" (p. 9, l. 273 to p. 10, l. 274; p. 14, l. 431, 432), "Zermatt Saas-Fee" (p. 10, l. 299), "Zermatt-Saas-Fee" (p. 12, l. 340), "Zermatt - Saas Fee" (p. 14, l. 411, 414; Fig. 12 legend), "Zermatt- Saas Fee" (Fig. 12 caption). (d) The Fig. 11 caption misspells "Turftgrat" (text p. 10, l. 276 and Fig. 13 "Tuftgrat") and "ecologites" (text p. 10, l. 274 "eclogites"). The abbreviations in the figure legends are treated in GB-28. |
| Suggestion | Introduce in Sect. 4 (p. 9, l. 273 to p. 10, l. 279) one name and one abbreviation per unit, in the order of the Fig. 4 legend, state that the Bündnerschiefer are the "ZSF sediments" unit, and use exactly these names at p. 10, l. 299, p. 12, l. 340, p. 14, l. 411, 414, 431 to 434 and in the legends and captions of Figs. 4, 5, 11 to 16, including "Stockhorn-Tuftgrat-Gornergrat" and "eclogites" in the Fig. 11 caption and "Zermatt-Saas Fee sediments" in the Fig. 12 caption. |
| Status | verified at the page images p. 9, 10, 12, 14, 25, 26, 32 to 37; counts verified (Python) |
| Severity | minor |
| Source | S2, S3, S4, AB |

**GB-26 The schematic Figures 1 to 3 contain symbols and colour scales that no legend or caption explains.**

| Field | Content |
|---|---|
| Check | P29 |
| Location | Fig. 1 (b), arrow symbol (p. 22); Fig. 2 (b) and (c) (p. 23); Fig. 3 (b), arrow symbol (p. 24) |
| Quotation | "tracer concentration low high"; "(c) tracer concentration maps based on geology and lithological fingerprints." |
| Concern | The three schematics are clear in their sequence, and the caption of Fig. 1 explains each panel. Two elements remain unexplained at the page images: (1) the black arrow symbol in Figs. 1b, 2b and 3b (north arrow or flow direction?); (2) in Fig. 2c only the green ramp is labelled "low high", while the upper layers use pink, orange and blue ramps, and the detrital bars in Fig. 2b use the same colours plus seven dark grey bars for which no layer is drawn. |
| Suggestion | Add the arrow to the legends of Figs. 1 to 3 (or remove it), and state in the caption of Fig. 2 that each layer has its own colour ramp and what the grey bars in (b) represent. |
| Status | verified (page images) |
| Severity | minor |
| Source | AB |

**GB-27 In the geology legend of Figures 4 and 12, three swatches cannot be told apart by colour.**

| Field | Content |
|---|---|
| Check | P3 |
| Location | Fig. 4 legend (p. 25); Fig. 12 legend (p. 33) |
| Quotation | "Stockhorn basement, Tuftgrat Mesozoic and GornergratPermo-Mesozoic"; "Outcrops: garnet-bearing silimanite-biotite gneiss" |
| Concern | Swatch colours measured at 300 dpi (centre of each swatch): Stockhorn unit #fc7434, Stockhorn outcrops #fc3434, Monte Rosa (garnet gneiss) outcrops #fc5c34. Sums of RGB differences (Python): 24 and 40, both within the limit of 40 used for "same colour". Red-orange areas in the north (Stockhorn) and at the south-east margin (Monte Rosa) therefore cannot be assigned to a unit from the legend alone; the other ten swatches differ by more than 40. |
| Suggestion | Give the Monte Rosa (garnet gneiss and micaschist) outcrops a colour that differs clearly from both Stockhorn swatches, in Fig. 4 and Fig. 12. |
| Status | verified (colour measurement) |
| Severity | minor |
| Source | AB |

**GB-28 Several abbreviations in the figures are resolved neither in the caption nor in the legend.**

| Field | Content |
|---|---|
| Check | P29 |
| Location | Fig. 4 inset legend (p. 25); Fig. 5 (j) legend (p. 26); Fig. 8 and Fig. 9 titles and axes (p. 29 to 30); Fig. 11 caption (p. 32); Fig. 13 labels (p. 34); Figs. 15 and 16 legends (p. 36 to 37) |
| Quotation | "ELA estimation"; "S.,T.,G."; "MR gneiss, mica"; "Almost fully blended (avg. JS = 0.225)" |
| Concern | Search in the body text (p. 1 to 21, text.json): "ELA" 0 hits, "equilibrium" 0 hits; "S.,T.,G." 0 hits; "MR" only as "MR g-g" (p. 14, l. 432 to 433); "ZSF" first at p. 14, l. 414, after Figs. 5 and 11 have been cited; "JS" defined at p. 12, l. 345 but not in the captions of Figs. 8 and 9. A reader of Fig. 5 or Fig. 15 cannot resolve S.,T.,G. or MR from the figure. Distinct from GB-25, which treats the unit names as such; here the concern is unresolved abbreviations. The neighbouring GB-27 at an overlapping place concerns indistinguishable legend swatches in Figs. 4 and 12; this finding concerns abbreviations not resolved in figures. |
| Suggestion | Spell out ELA (equilibrium line altitude, if that is meant) in the Fig. 4 legend; write the unit names in full in the legends of Figs. 5j, 15 and 16 or resolve ZSF, MR and S.,T.,G. in each caption; add "Jensen-Shannon (JS)" to the captions of Figs. 8 and 9. |
| Status | verified (search and page images) |
| Severity | minor |
| Source | AB |

#### Minor corrections

| ID | Location | Quotation | Replacement | Source |
|---|---|---|---|---|
| KK-05 | p. 5, l. 146, 148, 149; p. 6, l. 166, 167; p. 9, l. 252, 253, 258, 262; p. 10, l. 289, 290, 292, 294, 297, 298, 300, 301, 304, 306; p. 11, l. 307, 308, 315, 319 | "(Figure 1B)"; "(Figure 2A)"; "(Figure 3C)"; "(Figure 5K)"; "(Figure 6D, 6E and 6F )" | lowercase panel letters as printed in the figures, for example "(Figure 1b)", "(Figure 5k)", and "(Figure 6d, 6e and 6f)" without the space before the bracket; panel labels (a) to (k) checked on the page images p. 22 to 24, 26, 27; see GB-21 (the undocumented samples and zircon protocol), which treats a different aspect of the same place; see GB-22 (the unspecified XRD measurement and processing environment), which treats a different aspect of the same place; see GB-29 (the favourable set-up of the synthetic tests), which treats a different aspect of the same place | S3, S4 |
| KK-06 | p. 6, l. 174 | "given the observed detrital data and a prior knowledge" | "given the observed detrital data and prior knowledge" | S4 |
| KK-07 | p. 6, l. 175 | "p (εm ∣dobs ) p (dobs ∣εm ) · p(εprior ) / p(dobs )" | insert "=" between the two sides of Eq. 5 (or "∝" if the evidence term is dropped); confirmed on the page image p. 6; see GB-13 (index symbols that change meaning between equations and figures), which treats a different aspect of the same place | S4 |
| KK-08 | p. 8, l. 236 | "data have improved our knowledge considerately relative to the prior" | "data have improved our knowledge considerably relative to the prior"; see GB-19 (the plotted resolution diagonal near 1), which treats a different aspect of the same place; see GB-20 (the two quantities called normalised posterior uncertainty), which treats a different aspect of the same place | S4 |
| KK-09 | p. 8, l. 240 to 241 | "our a posteriori erosion rate map" | italics only for "a posteriori", not for "erosion" (page image p. 8) | S4 |
| KK-10 | p. 9, l. 245 | "weighed by the model covariance" | "weighted by the model covariance" | S4 |
| KK-11 | p. 9, l. 251 to 252 | "in-situ source samples are collected from every lithological unit across the study area (Figure 3A and 3B)" | "(Figure 3b)"; panel (a) shows detrital sampling with the pump sampler (page image p. 24); see GB-21 (the undocumented samples and zircon protocol), which treats a different aspect of the same place; see GB-22 (the unspecified XRD measurement and processing environment), which treats a different aspect of the same place; see KK-05 (upper-case panel letters in text references), which treats a different aspect of the same place | S4 |
| KK-12 | p. 9, l. 267; p. 9, l. 272; p. 10, l. 282; p. 13, l. 392; p. 13, l. 400; p. 15, l. 463; p. 16, l. 498 to 499; Fig. 11 caption (p. 32) | "the Gorner-gletscher catchment"; "the Gorner Glacier catchment"; "the Gorner gletscher catchment" | one form throughout, for example "the Gornergletscher catchment"; compared place by place on the page images: "Gorner-gletscher" (p. 9, l. 267; Fig. 11 caption), "Gornergletscher" (p. 9, l. 272; p. 10, l. 282), "Gorner Glacier" (p. 13, l. 392, 400; p. 16, l. 498, 499), "Gorner gletscher" (p. 15, l. 463); "Gorner-Grenzgletscher" (p. 13, l. 406) is a different name and stays; see GB-24 (the names of the base map and of the scenario 1 maps), which treats a different aspect of the same place; see GB-43 (the agreement of the fingerprints with the expected mineralogy (aim 1)), which treats a different aspect of the same place; see GB-54 (tracers with identical profiles in all units), which treats a different aspect of the same place; see GB-55 (the missing value axis and column labels of Fig. 11), which treats a different aspect of the same place; see GB-63 (the claim that combining XRD with zircon improves the solution (aim 3)), which treats a different aspect of the same place | S2, S4 |
| KK-13 | Fig. 3 (c), legend of the inset (p. 24) | "quarz pattern alignment" | "quartz pattern alignment" (as at p. 9, l. 256 "pure quartz pattern"); see GB-13 (index symbols that change meaning between equations and figures), which treats a different aspect of the same place | S2, AB |
| KK-14 | Fig. 4 legend (p. 25); Fig. 12 legend (p. 33) | "biotite schits"; "calcarious mica schist"; "caclcite-zoisite amphibolites"; "silimanite-biotite gneiss"; "GornergratPermo-Mesozoic" | "biotite schists"; "calcareous mica schist"; "calcite-zoisite amphibolites"; "sillimanite-biotite gneiss"; "Gornergrat Permo-Mesozoic"; compared at the page images of both legends; see GB-27 (indistinguishable legend swatches in Figs. 4 and 12), which treats a different aspect of the same place; see GB-28 (abbreviations not resolved in figures), which treats a different aspect of the same place; see GB-67 (the incomplete data availability statement), which treats a different aspect of the same place | AB |

#### Verification log

| ID | Check | Checked | Values | Result |
|---|---|---|---|---|
| PP-05 | P5 to P37 (design sketch) | Design sketch from the whole manuscript: questions and type, data sources with provenance class, timeline, environment, stated principles, components, disclosed limitations, chain from frame to result, outlook proposals | Study type: methods development with synthetic forward-inverse tests and a case study (Gornergletscher, 7 units, 21 tracers, pixel 300 m). Aims: p. 3, l. 63 to 64 and p. 10, l. 280 to 285. Hypothesis only at p. 14, l. 410 to 411. Data: synthetic (declared), XRD of source and detrital samples, zircon U-Pb (Belotti, 2021), inferred geological map, export estimate (not specified), prior. Only dated event: sample of 28 June 2019, 13:30. Disclosed limitations: inferred lithology (p. 9, l. 270 to 272, tested in scenario 1), small units (p. 10, l. 299 to 300), SD instability (p. 11, l. 312), zircon gaps (p. 14, l. 430 to 434), storage (p. 15, l. 466 to 468), grain size and orientation (p. 15, l. 469 to p. 16, l. 476) | no finding of its own; basis of the SD findings |
| PP-06 | P38 | Identifiers without finding | Tracer count 21 at p. 13, l. 393 and 397, p. 12, l. 358, Fig. 9 "All tracers (21)", 21 labels in Figs. 11 and 15, 21 letters A to U in Fig. 5k; pixel size 1200 m / 4 = 300 m and 3000 m / 10 = 300 m (Python); detrital sample "June 28, 2019, at 13:30" (p. 14, l. 423 to 424) and "the same date and time" (p. 14, l. 437 to 438); "WinXRD Peak Finder algorithm" and "Peak Finder algorithm" one tool; XRD, RRUFF, MAP, QN, SD, JS, PCA, ZSF unchanged after first use; "Gorner Glacier" at p. 16, l. 498 to 499 denotes the glacier, not the catchment; σm and σd identical at p. 10, l. 294 to 295, p. 11, l. 325 and p. 14, l. 427 to 428 | no finding |
| PP-07 | P25, P26, P27 | Information flow of each step, guarantees in every path, unchecked components and their downstream use | Gorner-Grenz runs with full-catchment A (p. 14, l. 408 to 410): feasible. Alignment before window extraction: feasible. Prior and total erosion for natural data: unclear. Eq. 19 not computable as printed. Positivity by log-space (p. 5, l. 157 to 158) holds in QN, SD, synthetic and natural runs. Inferred geology enters A (partly tested in scenario 1); σd enters all weights; MR g-g copy enters zircon and combined runs; Peak Finder thresholds and windows enter all fingerprints | findings GB-47, GB-18, GB-48, GB-45, GB-22 |
| PP-08 | P17, P31 | Location of each disclosed limitation; intended against measured effect per component | Inferred geology stated where the map is introduced: yes. Zircon gaps where zircon is introduced: yes. SD normalisation (p. 11, l. 312): not in Sect. 3.2. Storage (p. 15, l. 466 to 468): not in Sect. 3.1. Grain size, orientation, overlap (p. 15, l. 469 to p. 16, l. 476): not in Sect. 3.4. Window averaging, quartz alignment, normalisation and the resolution metric not measured; gradient normalisation in SD shown in Fig. 6 | findings GB-17, GB-11, GB-54, GB-64, GB-23, GB-19 |
| PP-09 | P3 | Number of tracers drawn in the schematics and windows against bars in Fig. 3d | Fig. 1b 4 rows of 11 bars; Fig. 2b 11 bars; Fig. 3d 11 grey 2θ windows and 11 bars; Fig. 3e 4 times 11 bars | no finding |
| PP-10 | P29, P3, P4 | Inventory of figures: number, page, type, caption, first citation in the text | 16 figures on p. 22 to 37, numbered 1 to 16 without gap or duplicate; first citations Fig. 1 p. 5, l. 146; Fig. 2 p. 6, l. 166; Fig. 3 p. 9, l. 251; Fig. 4 p. 9, l. 268 to 269; Fig. 5 p. 10, l. 289; Fig. 6 p. 11, l. 314 to 315; Fig. 7 p. 11, l. 334; Fig. 8 p. 12, l. 347; Fig. 9 p. 12, l. 356 to 357; Fig. 10 p. 12, l. 371; Fig. 11 p. 13, l. 398; Fig. 12 p. 14, l. 412; Fig. 13 p. 14, l. 414; Fig. 14 p. 14, l. 429; Fig. 15 p. 14, l. 438; Fig. 16 p. 15, l. 445, ascending; no graphical abstract, no tables, no appendix | no finding for numbering; panel references in GB-31, KK-05, KK-11, KK-15 |
| PP-11 | P3 | Scale bars and catchment size across the map figures | Catchment width divided by scale: Fig. 4 13.2 km; Fig. 12 13.1 km; Fig. 14 13.3 km; Fig. 15 13.2 km; Fig. 16 13.2 km; catchment area from Fig. 4 72.8 km2 | no finding |

### Segment 3: Results (p. 10 to 15, Figs. 5 to 16)

#### Substantive findings

**GB-29 The synthetic tests give the inversion the true mean and the true total erosion, use noise-free data from the same forward operator and test a single erosion pattern, yet the Conclusions state reliable recovery and robustness.**

| Field | Content |
|---|---|
| Check | P9, P10, P15 |
| Location | p. 10, l. 288 to 289; p. 10, l. 295; p. 11, l. 325 to 326; p. 16, l. 482 to 483 |
| Quotation | "to a “true” erosion rate map featuring a localised hotspot"; "a data standard deviation of 0.01 mm/y and a prior equal to the average true erosion rate."; "Using synthetic forward-inverse experiments, we show that the true erosion pattern can be reliably recovered, and that the method is robust across a range of parameters." |
| Concern | The authors state openly that the prior is the average true erosion rate and note its effect in the smoothing sweep (p. 13, l. 374 to 376); the consequence for the validation as a whole is not drawn. Four features favour recovery: (1) the prior mean equals the true mean; (2) Eq. 2 scales the data by the total erosion rate, which in the synthetic case is known from the true map (inferred); (3) the detrital data are generated "using the forward model" (p. 10, l. 288) with the same tracer matrix, grid and fingerprints the inversion uses (Fig. 5k), without added noise (search p. 1 to 21 for "noise": 1 hit, p. 9, l. 255, XRD background removal); (4) all tests use one true map "featuring a localised hotspot" (p. 10, l. 289). The Results also report where recovery fails: average JS distance below 0.44 with non-convergence (p. 12, l. 352 to 353), fewer than 7 tracers (p. 12, l. 361), smoothing distance beyond about 3000 m (p. 12, l. 373), step size below 0.1 and fewer than 25 iterations (p. 13, l. 385 to 387). "reliably" and "robust across a range of parameters" (p. 16, l. 482 to 483) name neither the favourable set-up nor these limits. Graded major because the synthetic tests are the main evidence for convergence and robustness (p. 3, l. 69 to 71). The undefined generation rules of the synthetic data are treated in GB-33. The neighbouring GB-12 at an overlapping place concerns mixed -ise and -ize spelling; this finding concerns the favourable set-up of the synthetic tests. |
| Suggestion | Repeat the tests of Sect. 4.1 with (a) priors offset from the true mean (for example factors 0.5, 2 and 10) and a total erosion taken from an independent estimate with error, (b) noise of the size seen in replicate XRD measurements added to the synthetic data and fingerprints perturbed within the scatter of several samples per unit, (c) an ensemble of true maps (hotspots in small and large units, several hotspots, uniform erosion), reporting the distribution of errors; at p. 16, l. 482 to 483 state the conditions and ranges within which recovery was shown. |
| Status | verified (prior, generation with the forward model, single map, no noise by search, failure ranges); role of the total erosion in the synthetic case inferred from Eq. 2 |
| Severity | major |
| Source | S4, SD |

**GB-30 The inversion parameters are not reported for every test: the step size of the first QN test, all settings of the SD test and of the natural known-mixture test, and the base values of the parameter sweeps are missing.**

| Field | Content |
|---|---|
| Check | P11 |
| Location | p. 10, l. 293; p. 11, l. 310 to 311; p. 12, l. 367 to 371; p. 13, l. 403; p. 14, l. 437 |
| Quotation | "In a first test, we use the QN approach with 100 iterations"; "this time using the steepest descent approach in the inversion method"; "We then applied the same nonlinear inversion technique to the XRD-derived dataset" |
| Concern | Matrix of tests against the parameters of Eq. 7 to 19 (scheme, iterations, L, σm, σd, prior, µ), built from the text: Sect. 4.1.1 QN: 100 iterations, L 1200 m, σm 3, σd 0.01 mm/y, prior average true rate, µ not stated. Sect. 4.1.2 SD: no parameter stated; the 200 iterations appear only as the x-axis range of Fig. 6. Sect. 4.1.3: complete (25 iterations, 1200 m, 3, 0.01 mm/y, average true rate, 0.1). Sect. 4.1.4: base values of the sweeps not stated; ranges only from the axes of Fig. 10. Sect. 4.2.1: no parameter stated. Sect. 4.2.2: zircon complete (p. 14, l. 426 to 428); XRD "the same nonlinear inversion technique" (p. 14, l. 437); combined "the same inversion parameters" (p. 15, l. 444 to 445). The QN versus SD conclusion (p. 11, l. 320 to 321) therefore compares runs whose settings are not fully reported. The SD variant is treated in GB-17, the prior of the natural runs in GB-47; here the concern is the parameter set per test. |
| Suggestion | Add a parameter table with one row per test (Sect. 4.1.1 to 4.2.2) and the columns scheme, iterations, L, σm, σd, prior value with unit, µ. |
| Status | verified (gaps by reading the named passages; iteration counts of Figs. 5 and 6 at the page images) |
| Severity | moderate |
| Source | S3 |

**GB-31 The SD section compares panel 6G with itself, refers to the wrong panel for the posterior covariance, and dates the onset of oscillations at 125 iterations where the figure shows a kink at about 134 to 138.**

| Field | Content |
|---|---|
| Check | P2, P3, P4 |
| Location | p. 11, l. 316 to 317; Fig. 6 (g), (h) (p. 27) |
| Quotation | "This limited sensitivity to strong gradients also leads to oscillations in the posterior covariance, visible after 125 iterations, as the Jacobian fluctuates between iterations (Figure 6G versus Figure 6G)." |
| Concern | A panel compared with itself has no target; according to both captions, panel (g) is the summed absolute difference and panel (h) the normalised posterior covariance during the iterations. Measured on the 300 dpi raster: the band in Fig. 6g turns flat at iteration 134.1 to 138.3 (±0.42), and in Fig. 6h it reaches its maximum at about iteration 137; after the kink the band in Fig. 6h is 16 to 17 px high against 13 to 14 px for a single marker, so a small alternation may be present, but it starts after iteration 134, not 125. Was "Figure 6H versus Figure 5H" (SD versus QN covariance trace) intended? |
| Suggestion | Replace the reference at p. 11, l. 317 by the intended panels (presumably "(Figure 6h versus Figure 5h)") and give the iteration at which the oscillation starts as read from the data, or mark it in Fig. 6h. |
| Status | verified (self-reference and wrong panel at the page image p. 11 and captions; kink position by measurement, AB); intended target: assumption |
| Severity | minor |
| Source | S3, S4, AB, SD |

**GB-32 Figures 5g and 6g show the steepest descent run ending closer to the true map than the quasi-Newton run, which the text does not reflect when it adopts QN as "more stable and accurate".**

| Field | Content |
|---|---|
| Check | P3 |
| Location | p. 11, l. 320 to 321; p. 10, l. 305 to 306; Fig. 6 (g) (p. 27); Fig. 5 (g) (p. 26) |
| Quotation | "Based on these findings, we adopt the Quasi-Newton (QN) approach for all subsequent tests, as it provides a more stable and accurate reconstruction of the erosion rate patterns." |
| Concern | The text correctly says that SD needs more iterations (p. 11, l. 315 to 316). Measured on the 300 dpi raster (tick marks as support points): Fig. 5g (QN, 100 iterations) minimum 197.3 ± 0.64 at iterations 21 to 23, final value 201.0 ± 0.64; Fig. 6g (SD, 200 iterations) final value 193.0 ± 0.78. Python: 201.0 minus 193.0 = 8.0, larger than 0.64 + 0.78 = 1.42. The QN error rises again by 3.7 after its minimum, which the text describes as "then plateaus" (p. 10, l. 306); Fig. 10 (row 5) shows the same for QN (197.6 at 25 iterations, 199.6 to 201.1 from 35 to 195). By the error measure the manuscript itself plots, SD after 200 iterations is more accurate than QN after 100. Does "accurate" refer to accuracy per iteration or to the hotspot amplitude? Graded major because the comparison of the two schemes is a stated aim (p. 1, l. 4 to 5), and its result changes from "QN more accurate" to "QN faster, SD at least as accurate". The documentation of the SD variant is treated in GB-17. The neighbouring GB-31 at an overlapping place concerns the panel reference "Figure 6G versus Figure 6G"; this finding concerns the accuracy of QN against SD in Figs. 5g and 6g. |
| Suggestion | Report the final errors of both schemes in Sect. 4.1.2, compare them at equal iterations and at convergence, reword p. 11, l. 320 to 321 to the criterion that actually favours QN (speed, stability), and mention at p. 10, l. 305 to 306 that the QN error passes a minimum near iteration 20 to 25. |
| Status | verified (measurement, AB); the meaning of "accurate": assumption, posed as a question |
| Severity | major |
| Source | AB |

**GB-33 Several rules of the synthetic tests and of the figures are named but not defined: blending, PCA ranking, generation of the synthetic data, grid size and the hatched low-confidence areas.**

| Field | Content |
|---|---|
| Check | P8, P29 |
| Location | p. 12, l. 343 to 344; p. 12, l. 355 to 357; Fig. 5 (b) and legend (p. 26); Fig. 6 (b) (p. 27); Figs. 14 to 16, legend below the first panel (p. 35 to 37) |
| Quotation | "We perform a Principal Component Analysis (PCA) to retain the subset of tracers that explain the maximum variance in the mineralogical fingerprints."; "Low-confidence areas" |
| Concern | (1) PCA yields components, not a subset of tracers; the rule that turns loadings into the ranked tracer subsets of Fig. 9 is not given. (2) How the synthetic fingerprints (Fig. 5k) and the true map (shape, amplitude, position of the hotspot) were generated is not described. (3) The blending "by approaching each lithology's mineral concentration to its mean" (p. 12, l. 343 to 344) has no formula or step, and the normalisation on which the JS distance is computed is not stated. (4) The hatched areas in Figs. 5, 6 and 14 to 16 have no definition: search p. 1 to 37 for "confiden" and "hatch": 0 hits; in Fig. 6 the hatch swatch below panel (b) has no label at all, and in Fig. 15 the hatching covers the main erosion peak discussed at p. 14, l. 440 to p. 15, l. 441. (5) Grid extent and number of pixels are not stated; only the pixel size follows from L = 1200 m = 4 pixels (p. 10, l. 294). The favourable set-up of the same tests is treated in GB-29, the missing pixel count as denominator of the error sum in GB-36. The neighbouring GB-19 at an overlapping place concerns the plotted resolution diagonal near 1; this finding concerns undefined rules of the synthetic tests and the undefined low-confidence areas. |
| Suggestion | Add to Sect. 4.1 the generation of synthetic fingerprints and true map, the blending formula, the PCA ranking rule and the JS computation; define the low-confidence criterion in Sect. 3.3 and in the captions of Figs. 5, 6 and 14 to 16, and add the missing label in Fig. 6; state grid extent and pixel count. |
| Status | verified (absence by reading and search; page images p. 26, 27, 35 to 37) |
| Severity | moderate |
| Source | AB, SD |

**GB-34 The three example fingerprint sets of scenario 2 are named differently in the text, the panel titles, the point labels and the caption of Fig. 8.**

| Field | Content |
|---|---|
| Check | P38 |
| Location | p. 12, l. 347 to 348; Fig. 8, panel titles, point labels and caption (p. 29) |
| Quotation | "Figure 8 illustrates three fingerprint sets: 1) highly blended, 2) intermediate, and 3) the original synthetic fingerprints"; "Almost fully blended (avg. JS = 0.225)"; "Medium blended (avg. JS = 0.441)"; "Unblended (avg. JS = 0.624)" |
| Concern | The same three sets appear under three naming triples: text "highly blended", "intermediate", "original synthetic fingerprints"; panel titles "Almost fully blended", "Medium blended", "Unblended"; caption "the most blended source signatures", "the half-way in between source signatures", "the original synthetic fingerprints". Fig. 9 shows that one triple is possible ("1 tracer", "11 tracers", "All tracers (21)" match p. 12, l. 357). Distinct from GB-35, which concerns the number of plotted runs. |
| Suggestion | Use one triple, for example "highly blended", "intermediate", "original (unblended)", at p. 12, l. 348 and in the Fig. 8 titles, point labels and caption. |
| Status | verified at the page images p. 12 and 29 |
| Severity | minor |
| Source | S2 |

**GB-35 Of the 20 blending levels tested in scenario 2, 14 are plotted in Fig. 8, the caption accounts for one, and five runs are missing without explanation.**

| Field | Content |
|---|---|
| Check | P3, P23, P34 |
| Location | p. 12, l. 348 to 349; p. 12, l. 352 to 353; Fig. 8, second row, left and middle scatterplots and caption (p. 29) |
| Quotation | "In total, 20 values between the highly blended and the original synthetic fingerprints are tested"; "In many of these cases, the inversion fails to converge to a stable posterior solution."; "Note that the most blended example did not have a stable solution and is therefore not plotted." |
| Concern | Balance: 20 runs tested. Markers counted independently by three instances on the page image (S3 and AB at 300 dpi, SD at 150 dpi): left scatterplot 14, middle scatterplot 14. Expected after the caption 20 minus 1 = 19; unaccounted for 19 minus 14 = 5 (Python). The JS positions of the 14 points (calibrated on the axis): 0.249, 0.272, 0.338, 0.359, 0.441, 0.461, 0.481, 0.501, 0.521, 0.541, 0.561, 0.581, 0.602, 0.624; neighbours are about 0.020 apart, matching an even spacing of (0.624 minus 0.225) / 19 = 0.021, except for two gaps, 0.272 to 0.338 (two missing values) and 0.359 to 0.441 (three missing values), together 5. Resolution A: the five runs did not converge and were omitted like the most blended one; then 6 of the 10 runs below JS 0.44 failed, which would be the "many" of p. 12, l. 353, but the caption names one. Resolution B: they converged but were removed for another reason; then a selection is unreported. Resolution C: fewer than 20 levels were run; then p. 12, l. 348 to 349 is wrong. The error statement for low JS distances rests on the remaining runs only. The abstract statement on convergence is treated in GB-02, the 700 mm/yr threshold in GB-36. |
| Suggestion | State at p. 12, l. 352 to 353 and in the caption of Fig. 8 how many of the 20 runs converged, define the convergence criterion and the JS values at which the inversion failed, and mark non-converged runs in the scatterplots. |
| Status | 20 runs and caption verified; count of 14 points verified (page image, three independent counts); positions and the five missing values inferred (measurement, Python); which resolution applies is a question to the authors |
| Severity | moderate |
| Source | S3, AB, SD |

**GB-36 The error threshold "700 mm/yr" is quoted as a rate, but the plotted quantity is a sum over an unstated number of pixels, and the thresholds cannot be read from Fig. 8.**

| Field | Content |
|---|---|
| Check | P3, P20 |
| Location | p. 12, l. 351 to 353; Fig. 8, second row, left scatterplot (p. 29) |
| Quotation | "As the JS distance decreases below 0.55, both absolute error and posterior uncertainty rise sharply, with errors exceeding 700 mm/yr" |
| Concern | The figures define the error as a sum over pixels ("Σ\|etrue − epost\|"); in the reference configuration it is about 197 (Figs. 7, 9, 10), and the y-axis of Fig. 8 reaches 700000. A per-pixel error cannot be derived because the number of pixels is not stated: search p. 1 to 16 for "pixel": 14 hits on 13 lines, none with a pixel count or catchment area; the pixel size appears only implicitly, 1200 m / 4 = 300 m (p. 10, l. 294), consistent with 3000 m / 10 = 300 m (p. 12, l. 372 to 373) (Python). Measured on Fig. 8 (support points 700000 and 0, ±1389 per value): absolute error 694 at JS 0.561, 19580 at 0.541, 4167 at 0.521, 9028 at 0.501, 1250 at 0.481, 1389 at 0.461; below 0.44: 5972 at 0.338, 322100 at 0.359, 676000 at 0.272, 46940 at 0.249. The rise below 0.55 is confirmed (694 to 19580; posterior uncertainty 0.747 to 0.842). The second threshold is not: if the axis is in mm/yr, all points from JS 0.441 to 0.541 already exceed 700, one point below 0.44 (5972 at 0.338) is lower than the point at 0.541, and 700 corresponds to 0.5 px at this scale; if "700" means 700000, no plotted point exceeds it. The unit is written "mm/yr" only here (search p. 1 to 16: "mm/yr" 1 hit, p. 12, l. 352; "mm/y" 5 hits), and the axes carry no unit. The missing runs of Fig. 8 are treated in GB-35, the missing pixel count as part of the undefined rules in GB-33. The neighbouring GB-34 at an overlapping place concerns the names of the three example fingerprint sets in Fig. 8; this finding concerns the 700 mm/yr error threshold and the unnormalised error sum. |
| Suggestion | State pixel size and number of pixels in Sect. 4 or 4.1.1; report the error as mean absolute error per pixel (in mm/y) or name it explicitly as a sum; revise p. 12, l. 352 to 353 to the quantity actually plotted and the measured behaviour (step at JS 0.55, non-monotonic below), write "mm/y" as elsewhere, and consider a logarithmic y-axis in Fig. 8. |
| Status | axis labels and text verified at the page images p. 12, 26 to 31; absence of the pixel count verified by search; point values verified by measurement (AB); pixel size inferred (Python); which quantity the text means is a question to the authors |
| Severity | moderate |
| Source | S2, S3, S4, AB |

**GB-37 Data misfits are compared across runs with different numbers of tracers and different data standard deviations without normalisation, so the reported drops follow from the definition alone.**

| Field | Content |
|---|---|
| Check | P21 |
| Location | p. 12, l. 360 to 362; p. 13, l. 382 to 384 |
| Quotation | "However, when the number of tracers drops below 7, the absolute error increases rapidly, as does the posterior uncertainty, while the data misfit and model misfit drop."; "with increasing data standard deviation, model misfit remains high while data misfit decreases sharply" |
| Concern | By Eq. 7 and 8 the data misfit is a sum over the m tracers, weighted by 1/σd². With fewer tracers the sum has fewer terms, so it drops even if the fit per tracer is unchanged: in Fig. 9 the misfit is about 3.3e6 for 21 tracers, about 1.6e5 per tracer, and about 1e5 for one tracer (read off the axis; Python). Between σd = 0.001 and 0.1 mm/y the weight changes by a factor of 1e4. The drops reported in both passages therefore follow from the definition and say nothing about the fit itself. The size of the σd effect on the solution is treated in GB-40; here the concern is the unnormalised misfit comparison. |
| Suggestion | When comparing runs with different m or σd, report the misfit per datum or in data units (for example root-mean-square residual), and revise p. 12, l. 360 to 362 and p. 13, l. 382 to 384. |
| Status | equations verified (page image p. 6); per-tracer values inferred (read off Fig. 9, Python) |
| Severity | moderate |
| Source | S3 |

**GB-38 The ranking of the three degradation scenarios compares perturbations of unequal, independently chosen size; at each scenario's tested extreme, tracer reduction affects error and uncertainty more than map uncertainty.**

| Field | Content |
|---|---|
| Check | P6, P21 |
| Location | p. 12, l. 363 to 365; p. 11, l. 337 to 338 |
| Quotation | "To summarize, among the three tested scenarios, the strongest impact on the posterior solution arises from reduced fingerprint distinctiveness. Geological map uncertainty follows as the second most influential factor."; "reducing the number of tracers has a comparatively limited effect" |
| Concern | Each scenario covers its own range: three maps with an area mismatch up to about 1.15e7 m2 (scenario 1), blending down to average JS 0.225 (scenario 2), reduction down to one tracer (scenario 3). Read at the 300 dpi renderings: scenario 1, absolute error 197.3 to 274.8 (plus 39 %), uncertainty plus 0.0058; scenario 3, absolute error 197.2 to 347 (plus 76 %), uncertainty plus 0.221 (Python); the SD instance read 274 and 346 independently on the 150 dpi images. At its tested extreme, tracer reduction exceeds map uncertainty in both metrics; the ranking holds only if scenario 3 is cut at seven tracers (the proviso "provided that the most informative ones are retained", p. 12, l. 365) while scenario 1 is taken at its extreme. The trend statement of scenario 1 rests on three cases, of which the middle one ("Minimal changes", 193.4, minus 2.0 %) has a smaller error than zero mismatch; the text notes this as "Surprisingly" (p. 11, l. 338) but keeps the general trend. The naming of the scenario 1 maps is treated in GB-24. |
| Suggestion | Compare the scenarios on a common scale (for example error against the JS distance of the resulting fingerprints, or against a normalised perturbation size), or state the ranking as conditional on the tested ranges at p. 12, l. 363 to 365 and p. 15, l. 457 to 461; base the scenario 1 trend on more maps or restrict it to the extreme case. |
| Status | quotations verified; values read off the scatterplots (inferred); percentages computed (Python) |
| Severity | moderate |
| Source | S3, SD |

**GB-39 The statement that smoothing distances beyond 3000 m make the solution overly smooth has no tested case; within the tested range the error decreases monotonically, as the next sentence also says.**

| Field | Content |
|---|---|
| Check | P3, P11 |
| Location | p. 12, l. 373 to p. 13, l. 376 |
| Quotation | "However, beyond approximately 10 times the pixel size (3000 m), the solution becomes overly smooth, causing the posterior to deviate from the true erosion rates."; "resulting in a reduced difference between posterior and true values" |
| Concern | Measured (x support points 500 and 3000 m, y support points 250 and 75; ±0.65): 20 markers from L = 200.5 m to 3001 m; the summed difference falls without exception from 257.1 to 76.1, with 195.0 at L = 1232 m (Python: 76.1 / 195.0 = 0.39). No value beyond 3000 m is plotted, so the stated deviation is not shown, and the plotted minimum lies at the upper end of the range. With the prior set to the average true erosion rate (p. 13, l. 375), does a very smooth posterior approach that mean and lower the summed difference simply because the hotspot is lost? Why the tests use L = 1200 m is treated in GB-52. |
| Suggestion | Extend the sweep beyond 3000 m and show the deviation, or delete the sentence at p. 12, l. 373 to p. 13, l. 374 and reconcile it with p. 13, l. 374 to 376; consider an error measure that penalises loss of the hotspot. |
| Status | text verified; tested range and values verified by measurement (AB); the explanation via the prior: assumption, posed as a question |
| Severity | moderate |
| Source | S3, AB |

**GB-40 The data standard deviation sweep changes the solution by less than 0.06 % and rises monotonically, yet the text describes large differences, a minimum and a plateau.**

| Field | Content |
|---|---|
| Check | P3, P21 |
| Location | p. 13, l. 380 to 384 |
| Quotation | "Very low data standard deviation values lead to large differences between the posterior and true erosion rate maps, likely due to overfitting or unstable gradients. As data standard deviation increases, the absolute difference first decreases to a minimum, then rises to a plateau at higher values."; "approximately 10-2 mm/y" |
| Concern | The panels of Fig. 10, third row, use offset axes (first panel "+1.974e2"). Measured on the 300 dpi rendering: summed difference 197.4197 at the cluster of low σd values (0.00 to about 0.09), then 197.4200 (0.10), 197.4203 (0.15), 197.4210 (0.21), 197.4224 (0.30), 197.4253 (0.44), 197.4312 (0.62) and 197.4431 (0.89 mm/y); range 0.0233, or 0.012 % of the value; normalised uncertainty 0.74015 to 0.74040 (0.034 %); model misfit 1.5614 to 1.5623 (0.057 %) (Python). No large difference at low σd, no minimum and no plateau are visible; the curve rises monotonically, and the descriptions follow the stretched axes. Are the "very low" σd values outside the plotted range? At p. 13, l. 384 the exponent is set on the base line ("10-2"; compare "10−5" at l. 388). The unnormalised misfit comparison in the same passage is treated in GB-37. |
| Suggestion | Plot the σd sweep on a logarithmic x-axis (as the colour bar already is), include the low values the text refers to, report the relative changes and revise p. 13, l. 380 to 384 to what the plot shows; set the exponent at p. 13, l. 384 as a superscript (10⁻² mm/y). |
| Status | offset label and axis values verified by measurement (AB, S3 independently); percentages computed (Python); exponent verified at the page image p. 13 |
| Severity | moderate |
| Source | S3, S4, AB, SD |

**GB-41 The 115-iteration threshold of 10^-5 has no reference quantity and is shown in no figure, and Fig. 10 shows failure to converge only at the smallest tested iteration number.**

| Field | Content |
|---|---|
| Check | P3, P20 |
| Location | p. 13, l. 387 to 389 |
| Quotation | "Only when the maximum number of non-linear steps is reduced below 25 does the posterior fail to converge to the true erosion map. Beyond 115 iterations, the change in data misfit between successive steps falls below 10−5" |
| Concern | Absolute or relative change is not stated. The data misfit is of the order 1e8 in Fig. 5i (axis multiplier "1e8") and 1e7 in Fig. 10, fifth row; an absolute change below 1e-5 would be a relative change of about 1e-13, a relative change of 1e-5 an absolute change of about 1000. No figure shows the step-to-step change. The stopping rule at p. 9, l. 243 to 244 ("when the data-misfit stops decreasing") is not related to this threshold or to the 25 iterations used later. Measured on Fig. 10, fifth row (±0.25): n = 5: 268.7; n = 15: 200.9; n = 25: 197.6 (minimum); n = 35: 199.6; n = 45 to 195: 200.6 to 201.1. The value at n = 15 lies within the range of n ≥ 45, so the figure shows failure only at n = 5, not "below 25" in general, and the error rises again after n = 25 (compare GB-32). |
| Suggestion | State whether the threshold is absolute or relative, show the data-misfit change per iteration (for example as a panel added to Fig. 10, fifth row), state for each test at which iteration the inversion stopped, and reword p. 13, l. 387 to 389 to the measured behaviour (failure at n = 5, minimum at n = 25, slight rise afterwards). |
| Status | text and axis multipliers verified at the page images; values by measurement (AB); magnitude comparison inferred |
| Severity | moderate |
| Source | S3, AB |

**GB-42 One of the 21 tracer minerals is "Chrysolite" in the text but "Chrysotile" in Figs. 11, 15 and 16.**

| Field | Content |
|---|---|
| Check | P2, P38 |
| Location | p. 13, l. 395; Fig. 16, x-axis labels of the fingerprint panel (p. 37); Fig. 15 (p. 36); Fig. 11, y-axis labels (p. 32) |
| Quotation | "Fayalite, Dolomite, Diopside, Chrysolite, Antigorite, Anorthite"; "Chrysotile" |
| Concern | The text list (p. 13, l. 393 to 396) and the label lists of Figs. 11 and 15 each contain 21 minerals; compared with Python, 20 names agree and one differs: text "Chrysolite", figures "Chrysotile" (Figs. 15 and 16 carry the same labels). Search p. 1 to 37 for "Chrysolite", "Chrysotile": 5 hits (p. 10, l. 274; p. 13, l. 395; Figs. 11, 15, 16). These are different minerals: the manuscript names chrysotile as a serpentine mineral of the serpentinites (p. 10, l. 274), whereas chrysolite is a variety of olivine; the tracer set already contains the olivine end member Fayalite. Which RRUFF reference pattern defined the 2θ window decides what this tracer measures, and that cannot be read from the manuscript. Graded moderate because the identity of a tracer, not only its spelling, is open. |
| Suggestion | Which mineral's RRUFF reference was used for this tracer? Correct the name at p. 13, l. 395 or in Figs. 11, 15 and 16 so that all places agree (presumably "Chrysotile"), and list the RRUFF identifiers and 2θ windows of all 21 tracers. |
| Status | name difference verified at the page images p. 13, 32, 36, 37; list comparison verified (Python); chrysolite as olivine variety verified (page text of https://minerals.net/variety/chrysolite, S2); which mineral was used: assumption, asked as a question |
| Severity | moderate |
| Source | S2, S3, S4, AB, SD |

**GB-43 Aim 1, the agreement of the XRD fingerprints with the expected mineralogy, is answered by a qualitative statement without criterion, while Fig. 11 shows strong serpentine and other signals that the manuscript's own unit descriptions do not lead one to expect.**

| Field | Content |
|---|---|
| Check | P3, P10, P19, P31 |
| Location | p. 13, l. 399 to 401; Fig. 11 (p. 32) |
| Quotation | "The mineralogical fingerprints derived from processed and binned XRD data align well with established knowledge of the lithology in the Gorner Glacier catchment (Bearth, 1953; Steck et al., 2015)" |
| Concern | No expected mineral list per unit, no agreement criterion and no independent mineralogical check is given. The serpentinite column fits the text (antigorite 1.00, chrysotile 0.91, quartz 0; bar lengths divided by 244 px). Three observations do not fit the unit descriptions at p. 10, l. 274 to 278 and in the Fig. 4 legend: (1) antigorite and chrysotile, named only for the serpentinites (p. 10, l. 274), reach 0.57 and 0.57 in the Stockhorn-Tuftgrat-Gornergrat unit (described as "amphibolite-bearing garnet-mica schists", p. 10, l. 277) and 0.52 and 0.49 in the ZSF sediments ("calcareous mica schists and quartzites", p. 10, l. 275); the SD instance measured 0.57, 0.58, 0.52 and 0.49 independently on the 150 dpi image; (2) almandine (garnet) is 0.09 in the Stockhorn unit and 0.03 in the Monte Rosa gneiss, although both are described as garnet-bearing; (3) tremolite is 0.89 in the Monte Rosa granite column, higher than microcline (0.28) and albite (0.23). The values are called "mineral concentrations" (p. 9, l. 261 to 262; p. 13, l. 398) although they are window peak areas scaled to the sample maximum. The text uses the claimed alignment as support for the cleaning and binning approach, the first validation aim (p. 10, l. 282 to 283). Are these signals caused by peak overlap within the 2θ windows (see GB-54)? Graded major because aim 1 and the claimed validity of the inversion input rest on this statement. |
| Suggestion | Add to Sect. 4.2 a table with, per unit, the minerals expected from Bearth (1953) and Steck et al. (2015), the minerals detected above a stated threshold and a pre-defined agreement criterion; discuss the mismatches with reference to the windows used; compare where possible with quantitative phase analysis of the same powders; call the values "normalised window peak areas" in Sect. 3.4, 4.2 and the figure axes; temper p. 13, l. 399 to 401 accordingly. |
| Status | bar values verified (measurement, AB and SD independently); mismatch for points (1) and (2) inferred from the manuscript's own unit descriptions; point (3) assumption from general mineralogy, posed as a question; absence of a criterion verified |
| Severity | major |
| Source | AB, SD |

**GB-44 The natural known-mixture test checks a single absent unit at lithology level, and Fig. 13 does not separate it from present units: the KDE of the ZSF sediments peaks at the same erosion rate as that of the Furgg series, which crops out in the subcatchment.**

| Field | Content |
|---|---|
| Check | P3, P9, P10 |
| Location | p. 14, l. 410 to 411; p. 14, l. 413 to 416; Fig. 13 (p. 34) |
| Quotation | "If the XRD fingerprinting method is robust, the inversion should attribute erosion only to lithologies present within the sub-catchment."; "Some spillover occurs from adjacent lithologies, but the overall pattern confirms that the inversion respects geological boundaries when the XRD fingerprints provide sufficiently distinct signals." |
| Concern | A subcatchment with known contributing area is a sound natural analogue of a known mixture, and the logic is explained clearly. The executed test has low discriminating power. (1) Only 1 of 7 units (ZSF sediments) is absent (p. 14, l. 411 to 412; Fig. 12), so there is one negative control. (2) KDE modes measured with the x-axis calibrated on the tick marks (AB at 300 dpi, ±0.002 mm/y per px): ZSF sediments 0.01 mm/y, Furgg series 0.01, MR granite 0.02, ZSF serpentinites 0.03, ZSF metabasites 0.13 to 0.23, MR gneiss 0.60; SD measured independently 0.00 for both ZSF sediments and Furgg. A near-zero mode therefore does not separate the absent unit from present ones. (3) The KDEs are built over "all pixels within each lithological unit" (Fig. 13 caption) in the whole catchment and cannot show whether erosion is placed on pixels outside the subcatchment; in the inset much of the mapped MR gneiss lies outside the dashed boundary, and this unit has the highest mode. (4) Small units have lower resolution (p. 10, l. 299 to 300), so a low value may reflect weak resolution. "Confirms" is stronger than the test allows. Graded major because the test answers aim 2 (p. 10, l. 283 to 284). The missing density scales of Fig. 13 are treated in GB-57, the undocumented samples in GB-21. The neighbouring GB-25 at an overlapping place concerns the naming scheme of the seven lithological units; this finding concerns the discriminating power of the natural known-mixture test (aim 2). |
| Suggestion | Report for each sample the fraction of total posterior sediment flux attributed to pixels outside the Gorner-Grenz subcatchment, against the same fraction from inversions with permuted fingerprints or from the prior alone; replace the whole-unit KDEs by flux shares inside and outside the boundary per unit; revise p. 14, l. 413 to 416 accordingly. A laboratory known-mixture experiment, which the manuscript names as the usual test (p. 13, l. 404 to 406), would add a test with known proportions. |
| Status | wording verified; KDE modes verified (measurement, AB and SD independently); KDE domain from the caption verified; position of the MR gneiss area relative to the boundary and point (4) inferred |
| Severity | major |
| Source | AB, SD |

**GB-45 The zircon benchmark rests on one sample and on zircon fingerprints without own signal for 3 of 7 units, so the instability of the zircon run cannot be attributed to the zircon method, and whether XRD and zircon used the same sample is unclear.**

| Field | Content |
|---|---|
| Check | P2, P9, P23, P37 |
| Location | p. 14, l. 420 to 421; p. 14, l. 433 to 434; p. 14, l. 437 to 438; Fig. 16, caption (p. 37); Fig. 14, caption (p. 35) |
| Quotation | "To benchmark the performance of our XRD-based fingerprinting method, we compare it against a zircon-based fingerprinting approach applied to the same detrital sample."; "we assigned the MR g-g unit the same zircon-age fingerprint as the Monte Rosa granite unit."; "the XRD-derived dataset acquired from a detrital sample taken at the same date and time" |
| Concern | The authors disclose the gaps in the zircon data (p. 14, l. 430 to 434); the consequences are not drawn. Balance: 7 units, of which the ZSF metabasites have no zircon, the MR gneiss received the MR granite fingerprint (in Fig. 14 the two segments have the same height in all 13 age bins, largest difference 0.004, measured), and the serpentinites show no visible segment in any bin; thus 3 of 7 units (42.9 %, Python) have no own zircon signal and only 4 sources are distinguishable. How the metabasite and serpentinite columns were built in the zircon and the concatenated matrices (p. 15, l. 443 to 444) is not stated (zero columns, removed pixels or assigned fingerprints). The unstable zircon result (">8000 mm/y", p. 14, l. 435) has at least four possible causes, missing fingerprints, identical columns, near-zero zircon in the serpentinites and the zircon method itself, which the text does not separate, yet the section is framed as a benchmark. The comparison uses one detrital sample, and p. 14, l. 421 ("the same detrital sample") and l. 437 to 438 ("a detrital sample taken at the same date and time") differ: one split or two samples? The assigned MR g-g fingerprint is shown in Figs. 14 and 16 like a measured one. Graded major because the benchmark answers aim 3 (p. 10, l. 284 to 285). The claims drawn from the comparison are treated in GB-63, the JS distance in GB-49. The neighbouring GB-42 at an overlapping place concerns the tracer named Chrysolite in the text and Chrysotile in the figures; this finding concerns the zircon benchmark with incomplete zircon fingerprints. |
| Suggestion | State in Sect. 4.2.2 how the metabasite and serpentinite columns were built for the zircon and concatenated matrices; rerun the XRD inversion under the restrictions of the zircon run (MR gneiss merged with MR granite, metabasites and serpentinites without signal) so that both methods are compared on equal source information, or compare them in a synthetic test; state whether one or two samples were analysed; mark the assigned MR g-g fingerprint in the captions of Figs. 14 and 16. |
| Status | disclosure and wording verified; identical segments and absent colours verified (measurement, AB and SD); the list of causes and the possible column treatments inferred; one or two samples: assumption, asked as a question |
| Severity | major |
| Source | S3, SD |

**GB-46 Single instantaneous samples are converted into erosion rate maps in mm/y via an annual export estimate, without addressing their temporal representativeness.**

| Field | Content |
|---|---|
| Check | P9, P10 |
| Location | p. 14, l. 423 to 424 |
| Quotation | "Zircon grains were extracted and U-Pb dated from both the source lithologies and the detrital sample collected on June 28, 2019, at 13:30" |
| Concern | The introduction frames the problem as "spatio-temporal dynamics" (p. 1, l. 1) and "the timing of their activation" (p. 1, l. 13). The design uses one sample taken at one hour for the zircon and XRD comparison and an unstated number of samples for the Gorner-Grenz test; the source mix of such samples is scaled by an annual export (p. 3, l. 65 to 66) to rates in mm/y. Search p. 1 to 21 for "season", "diurnal", "daily", "annual", "yearly": 5 hits, four naming the annual or yearly export (p. 3, l. 66; p. 5, l. 133; p. 15, l. 453; p. 16, l. 479) and one a journal title (p. 17, l. 507); none addresses how representative a single sample is of the annual mix. The multi-year suspended sediment datasets that motivate the site are not used in the analysis. The missing export value itself is treated in GB-47. The neighbouring GB-21 at an overlapping place concerns the undocumented samples and zircon protocol; this finding concerns the temporal representativeness of single samples. |
| Suggestion | State in Sect. 4 that the maps describe the source mix at sampling time scaled to annual rates under the assumption of a constant mix, and discuss that assumption in Sect. 5; or use a series of samples over the melt season or a flux-weighted composite and report the spread of posteriors. |
| Status | verified (wording; search as stated) |
| Severity | moderate |
| Source | SD |

**GB-47 The annual suspended sediment export, named as one of four required inputs and needed to scale the data (Eq. 2), is never given, and the prior of the natural-data runs is stated as the "average true erosion rate".**

| Field | Content |
|---|---|
| Check | P11, P12, P15, P25 |
| Location | p. 14, l. 428; p. 3, l. 65 to 66 and p. 5, l. 132 to 133; p. 15, l. 453 to 454; p. 16, l. 479 to 480 |
| Quotation | "a prior equal to the average true erosion rate"; "4) an estimate of the total annual suspended sediment export from the catchment"; "The approach integrates prior erosion estimates, a yearly sediment export estimate, and spatial information on source areas." |
| Concern | The method statement is clear about what is needed: the Discussion lists four key inputs, the fourth being the export estimate (p. 15, l. 452 to 454), and the Conclusions say it is integrated (p. 16, l. 479 to 480). Eq. 2 scales the data by the summed erosion rate, which for natural data must come from this estimate, and the results report absolute rates in mm/y (">8000 mm/y", p. 14, l. 435; Fig. 13 axis 0 to 3 mm/y; colour bars of Figs. 14 to 16). Search in p. 1 to 21 for "export": 5 hits (p. 3, l. 66; p. 5, l. 133; p. 15, l. 454; p. 15, l. 468, another sense; p. 16, l. 479), none in Methods or Results and none with a value, source, period or conversion to a catchment erosion rate; the availability statement (p. 16, l. 490) does not mention these data, although the site is chosen for its "multi-year suspended sediment datasets" (p. 9, l. 268). For the natural runs the prior is "the average true erosion rate" (p. 14, l. 428), the synthetic-test wording; a natural catchment has no true erosion rate. With total normalised posterior uncertainties of 0.82 to 0.87 (p. 14, l. 436; p. 15, l. 442, 447) the variance reduction is only 0.13 to 0.18 (1 minus ratio, Python), so the prior value matters. Graded moderate, not major: the spatial patterns remain, but their absolute scale cannot be traced. The other missing parameters per test are treated in GB-30, the temporal representativeness of single samples in GB-46. |
| Suggestion | In Sect. 4.2, before 4.2.1, state the export estimate with value, source (station, operator, years), uncertainty and the conversion to the total erosion rate (rock density, catchment area), state the prior value of the natural runs and how it was obtained (replacing "average true erosion rate" at p. 14, l. 428), and whether one value was used for all detrital samples; add the dataset to the availability statement at p. 16, l. 490. |
| Status | verified (wording; absence of value and source by the search stated); dependence of the mm/y values on the export estimate inferred from Eq. 2; variance reduction inferred (Python) |
| Severity | moderate |
| Source | S2, S3, S4, SD |

**GB-48 The data standard deviation is one tuned constant for XRD, zircon and their concatenation, so the weighting of the two data types in the combined run follows tracer counts, not measurement error.**

| Field | Content |
|---|---|
| Check | P27 |
| Location | p. 15, l. 444 to 445 |
| Quotation | "We run the inversion method with the same inversion parameters on this concatenated dataset, with the results shown in Figure 16." |
| Concern | σd = 0.01 mm/y comes from the synthetic set-up (p. 11, l. 325) and is used unchanged for natural XRD, zircon and combined data; no replicate measurement or counting statistic enters it. With C_d = σd² I (Eq. 8) every tracer has equal weight, so in the concatenated run the 21 XRD windows (several of them duplicates, GB-54) and the 13 zircon age bins (Fig. 14) are weighted by number, not by error. The combined result (Fig. 16) and the comparison in GB-63 depend on this unchecked choice. The unit of σd is treated in GB-14. |
| Suggestion | Derive σd per data type from replicate XRD measurements and from zircon counting statistics, use a block-diagonal C_d in the combined run, and show the sensitivity of Fig. 16 to the relative weighting (Sect. 4.2.2). |
| Status | verified (same parameters; equal weighting follows from Eq. 8); the effect on Fig. 16 inferred |
| Severity | moderate |
| Source | SD |

**GB-49 The average Jensen-Shannon distance of Sect. 4.2.2 is reported without the XRD-only value and without the set of pairs and the normalisation over which it is computed.**

| Field | Content |
|---|---|
| Check | P20 |
| Location | p. 15, l. 447 to 448 |
| Quotation | "the average Jensen-Shannon distance between source fingerprints increases from 0.48 to 0.57, indicating improved distinguishability" |
| Concern | (a) The value for the XRD-only fingerprints is missing (search "Jensen", "JS" in p. 14 to 15: 1 hit, p. 15, l. 447), so it cannot be seen whether the combined set is more distinguishable than XRD alone. (b) Denominator: 7 units give 21 pairs (Python). Because MR g-g received the MR granite fingerprint, one pair has distance 0 by construction, and the metabasite unit has no zircon distribution (GB-45). If 0.48 averages 21 pairs including the zero pair, the other 20 average 0.504; if it averages 6 units (15 pairs), the other 14 average 0.514 (Python). (c) JS is defined for probability distributions (p. 12, l. 345 to 346), but XRD fingerprints are scaled to their maximum, not to a sum of 1, and the combined vectors join 13 age bins and 21 minerals into 34 entries (counted at Figs. 14 and 16); renormalisation and the relative weight of the two blocks are not stated. The use of the uncertainty values for the combination claim is treated in GB-63. The neighbouring GB-20 at an overlapping place concerns the two quantities called normalised posterior uncertainty; this finding concerns the average Jensen-Shannon distance of Sect. 4.2.2. |
| Suggestion | Report the average JS distance for zircon, XRD and combined fingerprints; state which units and pairs enter, how identical and empty fingerprints are handled, and how the vectors are normalised before computing JS. |
| Status | values and definitions verified; pair arithmetic inferred (Python); bin counts verified at the page images |
| Severity | moderate |
| Source | S3 |

**GB-50 Quantities and units are missing on colour bars and axes of the synthetic-test figures.**

| Field | Content |
|---|---|
| Check | P29 |
| Location | Fig. 5 (a), (b), (c), (e), (g), (h) (p. 26); Fig. 6 (a), (b), (c), (e), (g), (h), (i) (p. 27); Fig. 7 axes (p. 28); Figs. 8 to 10, absolute-error axes (p. 29 to 31) |
| Quotation | "(a) True erosion map"; "Area difference" |
| Concern | Confirmed at the 300 dpi page images: (1) the erosion colour bars in Figs. 5 and 6 carry numbers but no quantity or unit, while the text gives erosion rates in mm/y and Figs. 13 to 16 state "(mm/y)"; (2) the absolute-error axes of Figs. 5g, 6g, 7, 8, 9 and the first column of Fig. 10 have no unit; (3) Figs. 6g, 6h and 6i have no x-axis title, the colour bar of Fig. 6i has no label, and Fig. 6i lacks the scale factor that Fig. 5i shows ("1e8"), so the magnitude of the data misfit is unknown; (4) Fig. 7 gives the unit of the area difference in the colour bar and in the caption ("area difference (m2)"), but not on the two x-axes "Area difference". The several names of the mismatch measure are treated in GB-24. The neighbouring GB-19 at an overlapping place concerns the plotted resolution diagonal near 1; this finding concerns missing quantities and units on colour bars and axes. The neighbouring GB-33 at an overlapping place concerns undefined rules of the synthetic tests and the undefined low-confidence areas; this finding concerns missing quantities and units on colour bars and axes. |
| Suggestion | Add quantity and unit to every colour bar and axis listed (for example "Erosion rate (mm/y)", "Iteration", "Data misfit (×10^8)"). |
| Status | verified (page images) |
| Severity | minor |
| Source | AB |

**GB-51 The x-axes of the two left scatterplots in Fig. 9 are labelled as JS distance but show the number of tracers, and the colour bar title is misspelled.**

| Field | Content |
|---|---|
| Check | P3 |
| Location | Fig. 9, second row, left and middle scatterplots and colour bar (p. 30) |
| Quotation | "Avg. JS distance between lithologies"; "Number of tracrs" |
| Concern | The axis runs from 0.0 to 20.0. Marker positions in the middle panel (calibrated on the axis): 0.997, 2.014, 2.998, 3.995, 5.004, 6.000, 6.996, then 11.00 ("11 tracers") and 21.01 ("All"); 21 markers in total, matching "the full range between 1 and 21 tracers" (p. 12, l. 358). The positions are integer tracer counts, and the colour bar of the same figure reads "Number of tracrs". The axis title is a leftover from Fig. 8. |
| Suggestion | Rename both x-axes "Number of tracer minerals" and correct the colour bar title to "Number of tracers". |
| Status | verified (measurement and page image) |
| Severity | minor |
| Source | AB |

**GB-52 Figure 10 highlights one parameter value per row without explanation, three of these values differ from the parameter set used in all tests, and the criterion that selected the values in use is not stated.**

| Field | Content |
|---|---|
| Check | P2, P5, P8, P29 |
| Location | Fig. 10, third column, labelled points, and caption (p. 31); p. 11, l. 324 to 326; p. 13, l. 377 to 378; p. 3, l. 70 and p. 5, l. 137 |
| Quotation | "Through forward-inverse testing, we optimize the hyper-parameters and demonstrate the convergence of the inversion."; "a smoothing distance of 4 times the pixel size (L = 1200 m), a model standard deviation of 3, a data standard deviation of 0.01 mm/y, a prior equal to the average true erosion rate, and a step size µ of 0.1" |
| Concern | The trade-off panels of Fig. 10 carry the labels "L = 3000 m", "σm = 6.2", "σd = 0.003 mm/y", "μ = 0.1" and "n_m = 25" (page image); the caption does not say what they mean (optimum, default or selected run). µ = 0.1 and 25 iterations agree with the values used (p. 11, l. 324 to 326; p. 14, l. 426 to 428); L differs by a factor of 2.5, σm by 2.07, σd by 0.3 (Python). In row 1 the error decreases monotonically up to 3000 m (GB-39), and the text says that increasing σm reduces the difference to the truth (p. 13, l. 377 to 378), yet L = 1200 m and σm = 3 are kept; the fixed values of the other parameters during each sweep are not stated. "we optimize the hyper-parameters" (p. 3, l. 70) therefore has no stated criterion. A reader taking the labels as the chosen parameters will reproduce a different inversion. The neighbouring GB-14 at an overlapping place concerns the units of the data vector and of the data standard deviation; this finding concerns the highlighted values in Fig. 10 and the choice of the hyperparameters. The neighbouring GB-29 at an overlapping place concerns the favourable set-up of the synthetic tests; this finding concerns the highlighted values in Fig. 10 and the choice of the hyperparameters. |
| Suggestion | Explain the highlighted points in the caption of Fig. 10; state in Sect. 4.1.4 the selection criterion and the fixed values of the other parameters in each sweep; if the labels mark optima, justify why the tests use L = 1200 m, σm = 3 and σd = 0.01 mm/y; if they mark the defaults, correct the labels. |
| Status | labels and text values verified at the page images p. 3, 10, 11, 14, 31; ratios computed (Python); meaning of the labels unknown, asked as a question |
| Severity | moderate |
| Source | S3, AB, SD |

**GB-53 Text in Figure 10 is printed at 3.5 to 4.7 pt, and some labels in Figs. 4, 14 and 16 fall below 6 pt.**

| Field | Content |
|---|---|
| Check | P29 |
| Location | Fig. 10, all panels (p. 31); Fig. 4, inset latitude labels (p. 25); Figs. 14 to 16, scale-bar label (p. 35 to 37); Fig. 16, colour-bar numbers (p. 37) |
| Quotation | "Total absolute difference etrue - epost"; "3000" |
| Concern | Measured cap or digit height (× 72 / dpi / 0.72, tolerance ±0.6 pt): Fig. 10 tick label "3000" 3.5 pt (median over 229 numeric labels 3.67 pt, minimum 3.33 pt), panel title 4.67 pt, axis title about 4.0 pt; Fig. 4 latitude labels 5.33 pt; "2 km" in Fig. 14 5.33 pt; Fig. 16 colour-bar numbers 5.17 and 5.33 pt. All are below 6 pt by more than the tolerance; tick labels of Figs. 5 to 9, 14 and 15 measure 5.5 to 6.33 pt (no finding). Distinct from GB-52, which concerns the content of Fig. 10. |
| Suggestion | Enlarge Fig. 10 (for example split it into two figures or reduce the panels per row) so that all text reaches at least 6 pt in print; raise the smaller labels in Figs. 4, 14 and 16 accordingly. |
| Status | verified (measurement) |
| Severity | minor |
| Source | AB |

**GB-54 Several of the 21 mineral tracers have identical or nearly identical values in every source unit, which points to shared 2θ windows, so the number of independent tracers is smaller than 21.**

| Field | Content |
|---|---|
| Check | P3, P9, P31 |
| Location | Fig. 11, rows Anorthite, Pyroxene, Annite, Phlogopite, Muscovite, Ankerite, Dolomite, Albite, Paragonite, Magnesite (p. 32); Fig. 15, fingerprint panel (p. 36); p. 16, l. 475 to 476 |
| Quotation | "Averaging peak areas across multiple 2θ values for the same mineral also reduces the possible impact of peak overlap between minerals with similar diffraction angles (Butler et al., 2019)." |
| Concern | Bar lengths measured along each row of Fig. 11 by two instances (AB at 300 dpi, longest bar 244 px; SD at 150 dpi, longest 122 to 123 px), order serpentinites, ZSF sediments, Stockhorn-Tuftgrat-Gornergrat, MR granite, metabasites, MR gneiss, Furgg: Anorthite and Pyroxene 0, 34, 244, 92, 243, 6, 104 (identical in all 7 units); Annite and Phlogopite 0, 131, 75, 137, 52, 161, 132 (identical); Muscovite differs from Annite in one unit by 9 px; Dolomite from Ankerite by 2 px in one unit; Paragonite from Albite by at most 4 px at 150 dpi. Merging profiles that differ by at most 4 px at 150 dpi leaves 16 distinct profiles, so 5 of 21 tracers (23.8 %, Python) are duplicates. In Fig. 15 the shares of Anorthite and Pyroxene, and of Annite and Phlogopite, agree to within 0.001. Identical values across seven different rocks point to shared windows, the overlap the averaging is said to mitigate (p. 16, l. 475 to 476); S4 noted the possible overlap of Pyroxene with Diopside and Omphacite. Consequences not discussed: with C_d = σd² I a duplicated tracer counts twice in the misfit, and the tracer-reduction scenario and the statement that 7 tracers suffice (p. 12, l. 360) count tracers that are not independent. Magnesite reaches at most 4.1 % of the unit maximum in Fig. 11 but is a full bar split 0.73 to 0.27 in Fig. 15. Graded major because the tracer set is the measuring instrument of the study. The missing value axis of Fig. 11 is treated in GB-55. |
| Suggestion | Give the 2θ windows per mineral in a table in Sect. 3.4, report the correlation matrix of the tracer profiles of the source samples, merge or remove tracers with shared windows, state how near-zero tracers are treated, rerun Fig. 9 with independent tracers, and correct "21" where it stands for independent information. |
| Status | identical bar lengths verified (measurement, AB and SD independently); shared windows as cause inferred, posed as a question |
| Severity | major |
| Source | AB, SD |

**GB-55 Figure 11 has no value axis, no scale and no column headings, so the fingerprints cannot be read without the caption and cannot be quantified.**

| Field | Content |
|---|---|
| Check | P29 |
| Location | Fig. 11 (p. 32) |
| Quotation | "From left to right: ZSF ophiolites (serpentinites), ZSF sediments, Stockhorn-Turftgrat-Gornergrat, Monte Rosa (granite), ZSF ophiolites (metabasites, ecologites), Monte Rosa (gneiss, micaschist), Furgg series." |
| Concern | The figure shows 7 columns of horizontal bars for 21 minerals, but no x-axis, no tick marks, no maximum value and no column labels; the units are assigned only by the order in the caption, and the colours by no legend. Section 3.4 says the values are normalised "on a scale from 0 to 1" (p. 9, l. 262); the longest bar in each column measures 243 to 244 px, consistent with a per-column maximum of 1, but this has to be inferred. This is the only figure that shows the measured XRD fingerprints of the natural sources. Graded moderate because the fingerprints cannot be read off or checked. Distinct from GB-54, which concerns the content of the rows; the spelling errors in the caption are part of GB-25. The neighbouring GB-43 at an overlapping place concerns the agreement of the fingerprints with the expected mineralogy (aim 1); this finding concerns the missing value axis and column labels of Fig. 11. |
| Suggestion | Add a value axis (0 to 1) under each column, the unit name above each column, and a colour legend shared with Figs. 5j, 15 and 16. |
| Status | verified (page image and measurement) |
| Severity | moderate |
| Source | AB |

**GB-56 In Figure 12 the Gorner-Grenz subcatchment is marked only by stronger colour saturation, without a boundary line or legend entry.**

| Field | Content |
|---|---|
| Check | P29 |
| Location | Fig. 12 (p. 33); Fig. 13, inset (p. 34) |
| Quotation | "Lithology and outcrops in the Gorner-Grenz confluence subcatchment." |
| Concern | The map shows the whole catchment; inside the subcatchment the colours are saturated, outside they are faded. Neither caption nor legend says this, and no boundary is drawn, while the inset of Fig. 13 draws it as a dashed line labelled "Gorner-Grenz catchment". Whether the small yellow and dark green patches in the northern strip belong to the subcatchment can only be guessed. The legend swatches of the same figure are treated in GB-27. The neighbouring GB-25 at an overlapping place concerns the naming scheme of the seven lithological units; this finding concerns the unmarked subcatchment in Fig. 12. |
| Suggestion | Draw the subcatchment boundary in Fig. 12 as in Fig. 13 and explain the faded colours in the caption. |
| Status | verified (page image) |
| Severity | minor |
| Source | AB |

**GB-57 Figure 13 gives no density scale for six of the seven curves, while the caption asks the reader to compare peak heights.**

| Field | Content |
|---|---|
| Check | P29 |
| Location | Fig. 13, upper panel and caption (p. 34); p. 14, l. 413 |
| Quotation | "a taller peak indicates greater consistency across inversions"; "based on multiple inversions" |
| Concern | The upper panel is a ridgeline plot with an axis title "Density" but no numbers, while the lower panel (ZSF sediments) has its own scale 0 to 2. The caption tells the reader to compare peak heights, which is impossible across panels with different or missing scales. The number of samples and inversions merged is not given (GB-21). Graded moderate because the test cannot be reproduced from the figure. The discriminating power of the test is treated in GB-44. |
| Suggestion | Add a density scale to each curve or plot all curves on one common axis, and state the number of detrital samples and inversions in the caption. |
| Status | verified (page image) |
| Severity | moderate |
| Source | AB |

**GB-58 The legends of Figures 14 to 16 are missing, clipped or ambiguous: Fig. 14 has none, Figs. 15 and 16 have overlapped and cut text, and their swatches do not match the bar colours.**

| Field | Content |
|---|---|
| Check | P3 |
| Location | Fig. 14, geology panel and bars (p. 35); Fig. 15 legend (p. 36); Fig. 16 legend (p. 37); Fig. 5 (j) legend (p. 26) |
| Quotation | "S.,T.,G."; "MR gneiss, mica" |
| Concern | (1) Fig. 14 shows the geology map and the zircon bars in five unit colours without any legend. (2) In Figs. 15 and 16 the text "ZSF serpentinites" runs into the swatch of "ZSF metabasites", and in Fig. 16 the top of the first legend row is cut off. (3) Swatch colours in the Fig. 15 legend against bar colours (sums of RGB differences): serpentinites 80, ZSF sediments 112, S-T-G 120, MR granite 64, metabasites 152, MR gneiss 96, Furgg 64; none is within 40. The S-T-G bars (#fc844c) instead match the MR gneiss swatch (#fc7c44, difference 16), so a reader assigns the orange bars to the wrong unit; the bars appear to be the legend colours at about 70 % opacity. The unresolved abbreviations are treated in GB-28. |
| Suggestion | Add a legend to Fig. 14; enlarge the legend boxes in Figs. 15 and 16 so that no text is cut; draw legend swatches with the same opacity as the bars (also in Fig. 5j). |
| Status | verified (page images and colour measurement) |
| Severity | minor |
| Source | AB |

**GB-59 The source fingerprints shown for the natural inversion (Figs. 15 and 16) do not follow from those of Fig. 11 by any step described in the text.**

| Field | Content |
|---|---|
| Check | P3, P8 |
| Location | Fig. 15 and Fig. 16, stacked bars and y-axis (p. 36 and 37); Fig. 11 (p. 32) |
| Quotation | "Normalised abundance per mineral or age" |
| Concern | Fig. 11 shows values normalised to the maximum within each unit, as described at p. 9, l. 261. Fig. 15 shows bars that sum to 1 per mineral across units, a second normalisation the text does not describe. The Fig. 15 shares also do not equal a per-mineral rescaling of Fig. 11 (measured by AB and SD independently): largest deviation per mineral 0.04 to 0.21, median 0.14; for example chrysotile in the serpentinites 0.639 (Fig. 15) against 0.427 (Fig. 11 rescaled). Within one mineral the order of units changes (pyroxene: in Fig. 11 S-T-G and metabasites highest, in Fig. 15 Furgg 0.261, MR granite 0.248, S-T-G 0.228, metabasites 0.168), which no per-mineral normalisation can do. A log-linear fit reproduces Fig. 15 as Fig. 11 times one factor per mineral and one per unit (residual standard deviation 0.7 %; unit factors relative to Furgg 0.28 to 1.51), which neither the axis label nor the caption mentions. How the detrital vector was transformed in the same way is not stated. The duplicate tracers visible in both figures are treated in GB-54. |
| Suggestion | Describe in Sect. 3.4 every step from window peak areas to the entries of A and d, including any normalisation across units and any unit weights (for example outcrop area), state it in the captions of Figs. 15 and 16, and state which data Figs. 11 and 15 show. |
| Status | mismatch verified (measurement of both figures, AB and SD); scaling model inferred (fit, AB); the reason is unknown and is asked |
| Severity | moderate |
| Source | AB, SD |

#### Minor corrections

| ID | Location | Quotation | Replacement | Source |
|---|---|---|---|---|
| KK-15 | p. 10, l. 299 | "(such as Zermatt Saas-Fee sediments and Furgg series (Figure 4) and Figure 5J)" | "(such as Zermatt-Saas Fee sediments and Furgg series; Figure 4 and Figure 5j)"; see GB-19 (the plotted resolution diagonal near 1), which treats a different aspect of the same place; see GB-25 (the naming scheme of the seven lithological units), which treats a different aspect of the same place | AB |
| KK-16 | p. 11, l. 307 | "the model’s "greedy" optimisation strategy" | typographic quotation marks as at p. 8, l. 222 and p. 10, l. 288 (straight marks confirmed on the page image p. 11); see GB-12 (mixed -ise and -ize spelling), which treats a different aspect of the same place; see KK-05 (upper-case panel letters in text references), which treats a different aspect of the same place | S4 |
| KK-17 | p. 12, l. 343 to 344 | "by approaching each lithology’s mineral concentration to its mean across all lithologies" | "by moving each lithology’s mineral concentration towards its mean across all lithologies"; see GB-33 (undefined rules of the synthetic tests and the undefined low-confidence areas), which treats a different aspect of the same place | S4 |
| KK-18 | p. 12, l. 345 to 346 | "which measures the similarity between two probability distributions" | "which measures the dissimilarity between two probability distributions" (p. 12, l. 346: values closer to zero indicate more similar signatures) | SD |
| KK-19 | p. 12, l. 351 | "The more resemblant the source fingerprints are" | "The more similar the source fingerprints are"; see GB-36 (the 700 mm/yr error threshold and the unnormalised error sum), which treats a different aspect of the same place | S4 |
| KK-20 | p. 12, l. 370 | "the maximal amount of non-linear iterations" | "the maximum number of non-linear iterations"; see GB-30 (inversion parameters not reported for every test), which treats a different aspect of the same place | S3, S4 |
| KK-21 | p. 13, l. 400 | "supporting the 1) the robustness of the cleaning" | "supporting 1) the robustness of the cleaning"; see GB-43 (the agreement of the fingerprints with the expected mineralogy (aim 1)), which treats a different aspect of the same place; see KK-12 (the spellings of the catchment name), which treats a different aspect of the same place | S3, S4 |
| KK-22 | p. 14, l. 409; p. 14, l. 411; p. 14, l. 413; p. 16, l. 488 | "sub-catchment"; "sub-catchments" | "subcatchment", "subcatchments", as at p. 10, l. 283 and 284, p. 14, l. 411 and in Figs. 12 and 13 (p. 14, l. 411 contains both spellings); see GB-44 (the discriminating power of the natural known-mixture test (aim 2)), which treats a different aspect of the same place; see GB-57 (the missing density scales in Fig. 13), which treats a different aspect of the same place; see GB-66 (the outlook on zircon data and land use), which treats a different aspect of the same place | S2 |
| KK-23 | Fig. 7, title of the left map (p. 28) | "Originial geology (same as forward)" | "Original geology (same as forward)"; see GB-20 (the two quantities called normalised posterior uncertainty), which treats a different aspect of the same place; see GB-24 (the names of the base map and of the scenario 1 maps), which treats a different aspect of the same place | AB |
| KK-24 | Fig. 9, left scatterplot, second Σ below the y-axis title (p. 30) | "Σ" | delete the stray character; see GB-51 (the mislabelled x-axes of Fig. 9), which treats a different aspect of the same place | AB |
| KK-25 | Fig. 10, first row, x-axis of the second column and colour-bar title (p. 31) | "Smooting distance (m)" | "Smoothing distance (m)"; see GB-52 (the highlighted values in Fig. 10 and the choice of the hyperparameters), which treats a different aspect of the same place; see GB-53 (font sizes below 6 pt), which treats a different aspect of the same place | AB |
| KK-26 | Fig. 10, fifth row, third column, label (p. 31) | "n_m = 25" | n with subscript m, "= 25", as in the caption; see GB-52 (the highlighted values in Fig. 10 and the choice of the hyperparameters), which treats a different aspect of the same place; see GB-53 (font sizes below 6 pt), which treats a different aspect of the same place; see KK-25 (Smooting in Fig. 10), which treats a different aspect of the same place | AB |
| KK-27 | Fig. 14, legend below the first panel (p. 35); Fig. 15 (p. 36); Fig. 16 (p. 37) | "Low-con dence area" | "Low-confidence area" (missing "fi" ligature, compared at the page images of all three figures); see GB-58 (missing, clipped and mismatched legends in Figs. 14 to 16), which treats a different aspect of the same place | AB |
| KK-28 | Fig. 14 caption and y-axis (p. 35); Fig. 16 panel title (p. 37) | "using Zr fingerprint data"; "Normalised abundance per Zr age bin"; "combined XRD and Zr data" | "using zircon U-Pb age fingerprint data"; "Normalised abundance per zircon age bin"; "combined XRD and zircon data" ("Zr" is the element symbol; the text uses "zircon"); see GB-58 (missing, clipped and mismatched legends in Figs. 14 to 16), which treats a different aspect of the same place; see KK-27 (the broken ligature in Low-confidence), which treats a different aspect of the same place | S2, AB |

#### Verification log

| ID | Check | Checked | Values | Result |
|---|---|---|---|---|
| PP-12 | P1 | Derived numbers in Sect. 4 and Figs. 5 to 16 | Pixel size 300 m twice consistent; 21 minerals in text = Fig. 11 = Fig. 15 = Fig. 5k = Fig. 9 = p. 12, l. 358; Fig. 16: 21 minerals + 13 age bins = 34 bars; 0.87 to 0.86 = minus 0.01 "decreases slightly"; 0.87 to 0.82 = minus 0.05 "slightly lower"; JS 0.48 to 0.57 = plus 0.09 "increases" (Python) | no finding |
| PP-13 | P2 | Quantities stated at more than one place, including the abstract | L, σm, σd identical at p. 10, l. 294 to 295, p. 11, l. 324 to 325 and p. 14, l. 427 to 428; µ = 0.1 at p. 11, l. 326, p. 13, l. 385 and p. 14, l. 428; 0.87, 0.82, 0.86 in text = labels of Figs. 14 to 16; QN 100 iterations = x-axis of Fig. 5g to 5i; 7-tracer threshold = Fig. 9; Fig. 8 labels JS 0.225, 0.441, 0.624; two schemes in abstract and results; 7 source units in Figs. 5j, 11, 13, 15, 16 | no finding beyond GB-63, GB-02, GB-52, GB-31, GB-42, GB-25, GB-45 |
| PP-14 | P11, P23 | Announced tests against reported results; balances of units, runs and vector entries | Synthetic scheme comparison, degradation, sensitivity and three natural-data aims announced (p. 10, l. 280 to 285); all six appear (Sect. 4.1.1 to 4.2.2). Scenario 1: 3 of 3 maps plotted; scenario 3: 21 of 21 configurations (counted at 300 dpi); five parameters announced = five rows of Fig. 10; Fig. 10, fifth row: 20 values from 5 to 195 in steps of 10, 20 points; Sect. 4.2.1: 7 units, 6 with outcrops in the subcatchment | no finding beyond GB-35, GB-30, GB-47, GB-39, GB-45 |
| PP-15 | P20, P21, P22 | Quotas and averages with stated denominators; comparisons across cases of different size; values the reader has to derive | Scenario 2 JS averaged "across all combinations" (p. 12, l. 347); 0 to 1 scaling by the maximum peak area (p. 9, l. 261 to 262); KDE over "all pixels within each lithological unit" (Fig. 13 caption); area mismatch in m2 = colour bar of Fig. 7; trace ratio normalised by the prior comparable across natural cases; KDE densities normalised per unit; "half-way" example at JS 0.441 refers to the blending step, not to the JS midpoint 0.4245 (Python) | no finding for these items; open denominators and unnormalised comparisons in GB-36, GB-20, GB-49, GB-21, GB-41, GB-40, GB-37, GB-38 |
| PP-16 | P3 | Fig. 5 against p. 10, l. 293 to 308 | 100 iterations in Fig. 5g to 5i; colour bar of 5i "Iteration"; in 5e and 5f the hotspot has the lowest values, as p. 10, l. 301 to 304 state; 5i runs from high data misfit and low model misfit (early) to low data misfit and model misfit 2.1 (late), as p. 11, l. 307 to 308 state | no finding (QN error course in GB-32, resolution in GB-19) |
| PP-17 | P3 | Synthetic fingerprints shown three times (Fig. 5k, Fig. 8 top right, Fig. 9 top right) and bar counts of the other top-row panels | 21 bars each; shares of the first five bars agree within 0.03; Fig. 8 top left and middle 21 bars each; Fig. 9 "11 tracers" 11 bars, "1 tracer" 1 bar | no finding |
| PP-18 | P3 | Fig. 7 against p. 11, l. 336 to p. 12, l. 342 | Absolute error: forward geology about 197.6, minimal changes 193.5, Steck et al. 274.8; area difference: minimal changes 0.69e7 m2, Steck et al. 1.14e7 m2; data misfit 3.26e6, 3.49e6, 3.68e6; model misfit 1.57, 1.92, 2.46 in the same order | no finding: the more accurate posterior for the minimal-change map and the increase of both misfits are shown; three cases only, as stated |
| PP-19 | P3 | Fig. 9 against p. 12, l. 360 to 362 | Absolute error: 1 tracer 347.1, 2: 347.7, 3: 293.4, 4: 296.5, 5: 224.1, 6: 205.2, 7 to 21: 197.4 | no finding: plateau from 7 tracers, rise below 7 and lower misfits for few tracers are shown (axis label in GB-51) |
| PP-20 | P3 | Fig. 10 rows 2 and 4 against p. 13, l. 377 to 379 and l. 385 to 386 | Row 4: µ = 0.068: 203.8; 0.100: 197.5 (minimum); 0.147: 199.0; 0.215: 200.8; 0.316: 201.3. Row 2: 209.1, 204.3, 200.9, 198.9, 197.5 for the smallest σm values, 197.4 for larger ones; all runs at 25 iterations give 197.4 to 197.6 (Figs. 7, 9, 10) | no finding: optimum step size 0.1 and the σm behaviour are shown |
| PP-21 | P29 | Font sizes not reported as findings | Fig. 5 colour-bar and axis numbers 6.0 to 6.33 pt; Fig. 6 6.0 to 6.33 pt; Fig. 7 5.67 to 6.0 pt; Figs. 8 and 9 5.83 pt; Figs. 14 and 15 5.5 pt; Figs. 2, 3, 11, 13 at least 6.0 pt | no finding within the 0.6 pt tolerance |
| PP-22 | P3 | Colours of the seven units across figures | Bars in Figs. 5k, 11, 14, 15: the same seven colours (differences at most 8); order in Fig. 11 matches the caption and the Fig. 5j legend | no finding for consistency between figures (legend swatches in GB-58) |
| PP-23 | P3 | Figs. 14 to 16 against p. 14, l. 429 to p. 15, l. 449 | "Total normalised posterior uncertainty" 0.87, 0.82, 0.86 in the figures = text; Fig. 14 colour bar top 8592 mm/y, text ">8000 mm/y" (p. 14, l. 435); Fig. 14 bars: 13 age bins, MR granite and MR gneiss equal in every bin (largest difference 0.004), metabasites and serpentinites 0 in all bins; Fig. 16: 34 bars, shares equal Figs. 15 and 14 within 0.006 | no finding beyond GB-45 |
| PP-24 | P24, P7, P30 | Dated events in figures; validity of the method over time; reported errors and their correction | Only dated event: detrital sample of 28 June 2019, 13:30; no figure has a time axis; one method version described, SD variant differs from Eq. 18; no error with correction reported in p. 1 to 21 | no finding; P24 not applicable; SD variant in GB-17 |
| PP-25 | P5, P6, P9, P32, P34, P36 | Own rules against own examples, absolute statements, confounding and selection, results called validated, counted sets with shown selection, statements from impression | Minimum 25 iterations against runs with 25: met at the limit; stopping rule compatible as a maximum; "from every lithological unit" met for XRD, disclosed exceptions for zircon; XRD and zircon samples from the same date and time, no sequential confound; Fig. 9 21 of 21, Fig. 7 3 of 3, Fig. 8 14 of 20 markers; "approximately the same posterior solution" with 7 tracers matches Fig. 9; "Some spillover" not quantified | findings GB-52, GB-44, GB-63, GB-35, GB-29; otherwise no finding |

### Segment 4: Discussion, Conclusions, statements, references (p. 15 to 21)

#### Substantive findings

**GB-60 The Discussion names the "incorporation of non-linear mixing model" as novelty, whereas the Methods describe the detrital data as a weighted average and attribute the non-linearity to the log-parametrisation.**

| Field | Content |
|---|---|
| Check | P15 |
| Location | p. 15, l. 454 to 455; p. 5, l. 157 to 158; p. 2, l. 59 to 60 |
| Quotation | "The novelty of our method lies in the spatially informed approach of this underdetermined inversion problem, and in the incorporation of non-linear mixing model."; "We cast the erosion rates in log-space to impose a positivity constraint, hence making this non-linear." |
| Concern | The Methods state that "the detrital data are a weighted average of the tracer mineral concentrations, with the weights being the erosion rates" (p. 5, l. 151 to 152). From Eq. 1, di is a sum of Aij times the share of erosion at pixel j, that is linear in the source proportions; non-linear is the parametrisation and hence the inversion. The introduction contrasts the method with approaches that "implicitly rely on a linear mixing scheme" (p. 2, l. 59), and the spatially informed inversion is introduced as an adaptation of "the inversion framework validated in (De Doncker et al., 2020)" (p. 2, l. 61), so its novelty needs delimiting. Is "non-linear mixing model" meant as "non-linear inversion of a linear mixing model"? S1 noted the same contrast outside its checklist. Distinct from GB-07, which concerns the missing literature search behind the novelty claim; here the concern is what the claim says about the model. The neighbouring GB-47 at an overlapping place concerns the missing export estimate and the undefined prior of the natural-data runs; this finding concerns the claimed novelty of a non-linear mixing model. |
| Suggestion | At p. 15, l. 454 to 455 locate the non-linearity in the log-parametrised inversion (for example "a non-linear, positivity-constrained inversion of a linear mixing model"), state what is new relative to De Doncker et al. (2020), adjust p. 2, l. 58 to 61 accordingly, and add the missing article. |
| Status | verified (wording at all locations); linearity in the source proportions inferred (derived from Eq. 1) |
| Severity | moderate |
| Source | S4 |

**GB-61 "Including a broad set of tracer minerals further improves model stability and resolution" is stronger than scenario 3, which shows saturation at seven tracers and reports no resolution.**

| Field | Content |
|---|---|
| Check | P6, P15 |
| Location | p. 15, l. 458 |
| Quotation | "Including a broad set of tracer minerals further improves model stability and resolution."; "The inversion with 7 tracers results in approximately the same posterior solution as with the full tracer set." |
| Concern | The Results state that 7 tracers give approximately the same solution as 21 (p. 12, l. 360) and that reducing the number of tracers "has a comparatively limited effect" if the most informative ones are retained (p. 12, l. 364 to 365); Fig. 9 shows the same error from 7 to 21 tracers (197.4, measured) and no resolution. Search p. 12 for "resolution": 0 hits. Beyond 7 of 21 tracers the Results show no further gain, and resolution is not evaluated in this scenario. The ranking of the scenarios is treated in GB-38, the dependence among the tracers in GB-54. |
| Suggestion | Replace p. 15, l. 458 by a statement that matches p. 12, l. 360 to 365, for example "Retaining at least the seven most informative tracers was sufficient; fewer tracers increased error and posterior uncertainty", or add the resolution for scenario 3 to Fig. 9. |
| Status | verified (wording, search, values of Fig. 9 by measurement) |
| Severity | moderate |
| Source | S4, SD |

**GB-62 The Discussion claim on the number of source areas and two of the three conditions introduced by "Our results suggest" in the Conclusions have no test in the Results.**

| Field | Content |
|---|---|
| Check | P6, P15 |
| Location | p. 15, l. 460 to 461; p. 16, l. 484 to 486 |
| Quotation | "A higher number of distinct source areas leads to higher posterior resolution and lower uncertainty."; "Our results suggest that the method is best applied in catchments with minimal sediment storage, multiple mineralogically distinct source areas, and good prior knowledge of the spatial distribution of source areas." |
| Concern | Search in the Results, p. 10, l. 286 to p. 15, l. 449, for "number of source", "number of litholog", "number of unit", "number of distinct": 0 hits; scenario 3 varies the number of tracers (p. 12, l. 355 to 359), not of source areas, and Sect. 4.1.3 and 4.1.4 vary maps, blending, tracer count and five hyperparameters. Search in the Results, p. 10, l. 286 to p. 15, l. 449, for "storage" and "stored": 0 hits; minimal storage is a model assumption (p. 1, l. 23; p. 15, l. 467 to 468), not a result. Only "mineralogically distinct" (scenario 2) and "good prior knowledge of the spatial distribution" (scenario 1) rest on tests. Is p. 15, l. 460 to 461 an inference from the pattern of Fig. 5 (lower resolution in small units, p. 10, l. 299 to 300) rather than a tested result? These statements underlie recommendations a) to c) (p. 15, l. 463 to 466), whose fit to the own catchment is treated in GB-11. |
| Suggestion | At p. 16, l. 484 separate the conditions backed by scenarios 1 and 2 from minimal storage, labelled as model assumption; at p. 15, l. 460 to 461 either add a synthetic test that varies the number of source areas or reword the sentence as an inference from Fig. 5d to 5f. |
| Status | verified (wording; absence by the searches stated) |
| Severity | moderate |
| Source | S4, SD |

**GB-63 The introduction and the Discussion state that combining XRD with zircon data improves stability, sharpness and accuracy, but the only reported metric is worse for the combination (0.86) than for XRD alone (0.82).**

| Field | Content |
|---|---|
| Check | P2, P6, P15, P31 |
| Location | p. 15, l. 461 to 463; p. 3, l. 72 to 73 and p. 5, l. 139 to 140; p. 10, l. 284 to 285; p. 15, l. 446 to 447 |
| Quotation | "Furthermore, combining XRD data with other fingerprint data such as zircon data, proves to further stabilize and improve the posterior solution, as shown with natural data for the Gorner gletscher catchment."; "showing that integrating XRD with zircon data improves the stability and sharpness of the posterior solution"; "The normalized posterior uncertainty decreases slightly to 0.86 (from 0.87 in the zircon-only case)" |
| Concern | Section 4.2.2 reports the same scalar metric for all three natural-data inversions, with text and figure labels in agreement, which makes the comparison checkable: zircon 0.87 (p. 14, l. 436), XRD 0.82 (p. 15, l. 442), combined 0.86 (p. 15, l. 447). Python: zircon to combined minus 0.01 (minus 1.15 %); XRD to combined plus 0.04 (plus 4.88 %); zircon to XRD minus 0.05 (minus 5.75 %). Case analysis: "adding XRD to zircon improves on zircon only" is supported, by 0.01; "adding zircon to XRD improves on XRD only", which is how p. 15, l. 461 to 462 reads ("further stabilize"), is contradicted by 0.82 against 0.86. The JS increase from 0.48 to 0.57 (p. 15, l. 448) also compares zircon with combined only (GB-49). Aim 3 asks for "stability and accuracy" (p. 10, l. 285), the introduction claims "stability and sharpness" (p. 3, l. 73); search p. 14, l. 419 to p. 15, l. 449 for "accura" and "sharp": 0 hits, and a natural sample has no true map against which accuracy could be measured. The posterior colour bars reach 8 mm/y for XRD alone and 12 mm/y for the combination (Figs. 15 and 16, read at the page images). "proves" rests on one detrital sample. Graded major because the finding concerns the answer to aim 3, repeated in introduction and Discussion. The incomplete zircon fingerprints behind the comparison are treated in GB-45, the weighting of the two data types in GB-48. The neighbouring GB-11 at an overlapping place concerns the recommended site conditions against the own glacier catchment; this finding concerns the claim that combining XRD with zircon improves the solution (aim 3). The neighbouring GB-62 at an overlapping place concerns statements on the number of source areas and on storage without a test; this finding concerns the claim that combining XRD with zircon improves the solution (aim 3). |
| Suggestion | Add to Sect. 4.2.2 one table with all metrics for the three cases (scalar normalised uncertainty, mean resolution, average JS distance, maximum posterior rate); rewrite p. 15, l. 461 to 463, p. 3, l. 72 to 73 and p. 5, l. 139 to 140 to state what the numbers show (for example "adding XRD data to zircon data reduced the normalised posterior uncertainty slightly, from 0.87 to 0.86, while XRD alone gave 0.82"); replace "proves" by "suggests"; define and report measures of stability and sharpness or drop these terms and "accuracy" from aim 3; discuss why the combined inversion is less certain than XRD alone. |
| Status | values and wording verified (text and page images p. 3, 10, 14, 15, 35 to 37); differences inferred (Python); absence of sharpness and accuracy metrics verified by the search stated |
| Severity | major |
| Source | S3, S4, SD |

**GB-64 The Discussion credits quartz peak alignment with correcting intensity biases such as shielding, while the Methods describe it as a correction of peak position only.**

| Field | Content |
|---|---|
| Check | P31 |
| Location | p. 15, l. 473 to p. 16, l. 474 |
| Quotation | "Moreover, our use of the WinXRD Peak Finder algorithm, combined with quartz peak alignment, helps normalize for instrumental and sample-related biases, including shielding effects" |
| Concern | By the manuscript's own description, alignment shifts the 2θ axis; shielding (absorption) changes intensities. No measurement shows that the processing chain removes intensity biases; the Discussion presents an intended effect as achieved. The step that might handle intensity effects, the maximum normalisation, is itself treated in GB-23. |
| Suggestion | In Sect. 5 either show the effect (for example replicate powders with different absorption) or restrict the sentence to peak position, and name the step that is meant to handle intensity effects. |
| Status | verified (both descriptions); that alignment cannot correct intensities inferred from the Methods description |
| Severity | moderate |
| Source | SD |

**GB-65 Research aims 1 and 2, the comparison of steepest descent and quasi-Newton schemes, and the Bayesian "hybrid" positioning are introduced but not taken up in the Discussion or Conclusions.**

| Field | Content |
|---|---|
| Check | P15 |
| Location | p. 16, l. 478 to 486; p. 10, l. 282 to 284; p. 2, l. 55 to 57 and p. 4, l. 122 to 124 |
| Quotation | "1) to investigate whether the inferred XRD source fingerprints align with the expected mineralogical compositions of the lithologies, 2) to test if sediment samples from a subcatchment are attributed only to lithologies present within the subcatchment boundaries"; "Our approach can be seen as a hybrid between Bayesian linear mixed models and hierarchical Bayesian models" |
| Concern | The Results answer aims 1 and 2 (fingerprints "align well with established knowledge", p. 13, l. 399; ZSF sediment pixels "close to zero" with "Some spillover", p. 14, l. 414 to 415), and Sect. 4.1.2 decides for QN (p. 11, l. 320 to 321). None of this reappears in Sect. 5 or 6: search p. 15, l. 450 to p. 16, l. 489 for "steepest", "quasi", "QN", "Newton": 0 hits; for "Bayes", "hierarch", "frequentist", "BLMM", "GLUE", "NLLS", "NNLS", "hybrid": 0 hits. The Discussion takes up only aim 3 (p. 15, l. 461 to 463). The Conclusions therefore do not say whether the known-mixture test succeeded, with its spillover qualification, nor what the hybrid positioning (uncertainties "without requiring the generation and sampling of multiple posterior solutions", p. 2, l. 57) gains over the methods reviewed at p. 2, l. 43 to 57. Graded moderate: the results stay, but a reader cannot check how the conclusions relate to aims 1 and 2. The untested conditions in the same Conclusions paragraph are treated in GB-62. The neighbouring GB-19 at an overlapping place concerns the plotted resolution diagonal near 1; this finding concerns aims 1 and 2, the scheme comparison and the Bayesian positioning missing from the Discussion. The neighbouring GB-29 at an overlapping place concerns the favourable set-up of the synthetic tests; this finding concerns aims 1 and 2, the scheme comparison and the Bayesian positioning missing from the Discussion. The neighbouring GB-47 at an overlapping place concerns the missing export estimate and the undefined prior of the natural-data runs; this finding concerns aims 1 and 2, the scheme comparison and the Bayesian positioning missing from the Discussion. |
| Suggestion | Add to Sect. 5 a paragraph on the natural known-mixture result including the spillover (p. 14, l. 414 to 415) and on the plausibility of the fingerprints (aim 1); state in Sect. 6 the outcome for all three aims and the reason for adopting QN; relate the posterior covariance and resolution metrics to the uncertainty estimates of the approaches of p. 2, l. 52 to 57, or drop the hybrid claim. |
| Status | verified (wording; absence by the searches stated) |
| Severity | moderate |
| Source | S4 |

**GB-66 The Conclusions state that the method "can be applied to ... zircon U-Pb age distributions" and extended to land use, although the zircon-only inversion was "highly unstable" and land-use source maps were not tested.**

| Field | Content |
|---|---|
| Check | P6, P15 |
| Location | p. 16, l. 487 to 489; p. 15, l. 466 |
| Quotation | "Similarly, the method is not limited to XRD-derived fingerprints and can be applied to other types of tracer data, including zircon U-Pb age distributions or geochemical compositions."; "Other types of source area maps, such as those based on land use, can also be incorporated." |
| Concern | The Results report for zircon extreme values (">8000 mm/y", p. 14, l. 435) and explain them openly by missing zircon data for two units (p. 14, l. 430 to 434); the Conclusions state applicability to zircon without this condition. Search p. 1 to 21 for "land use", "land-use", "land cover": 4 hits (p. 9, l. 270, the land cover of Fig. 4; p. 15, l. 466; p. 16, l. 488; p. 17, l. 507, a reference title), none in the Results; the extension to land use is a possibility not covered by the Results. The zircon benchmark itself is treated in GB-45. |
| Suggestion | Qualify p. 16, l. 488 to 489, for example "can in principle be applied to other tracer data provided all source units are characterised; with zircon data missing for two units the inversion was unstable (Sect. 4.2.2)", and mark the extension to land use (p. 15, l. 466; p. 16, l. 487 to 488) as untested. |
| Status | verified (wording; search as stated) |
| Severity | moderate |
| Source | S4, SD |

**GB-67 The availability statement covers only "the inversion tests" and does not itemise several data sources named in the methods and figures.**

| Field | Content |
|---|---|
| Check | P12 |
| Location | p. 16, l. 490; Fig. 4, credit text (p. 25) |
| Quotation | "The data and codes used for the inversion tests in the study are available at https://doi.org/10.5281/zenodo.17120374"; "Land cover data: SwissTopo 2018 Geological data: data from Steck et al., 2015, personal communication by L. Baumgartner, outcrops by GeoCover" |
| Concern | A public deposit with a DOI exists and resolves (PP-29), and its README lists "Raw XRD data and RRUFF files" and "Raw zircon data"; this is a good basis. The statement itself is one sentence for all data, and these sources named in the manuscript are not addressed: (1) land cover "SwissTopo 2018" and outcrops "GeoCover", credited only inside Fig. 4 (search p. 1 to 21 for "SwissTopo", "swisstopo", "GeoCover": 0 hits; no reference entry); (2) the inferred geological map under the ice (p. 9, l. 270 to 272), which rests partly on a personal communication, and the modified maps of scenario 1 (p. 11, l. 331 to 334); (3) the source sample locations, shown only schematically in Fig. 3b (search "coordinat": 0 hits); (4) the detrital samples of the known-mixture test; (5) the processing software "WinXRD Peak Finder" (p. 9, l. 254) with version and settings. The README does not mention sample locations, land cover or WinXRD (fetch tool answer). The data do not concern persons, so no reason for withholding is needed; the issue is that the statement does not say whether these sources are in the deposit, elsewhere, or not shared. The missing export dataset is treated in GB-47, the sample documentation in GB-21. The neighbouring GB-27 at an overlapping place concerns indistinguishable legend swatches in Figs. 4 and 12; this finding concerns the incomplete data availability statement. The neighbouring GB-28 at an overlapping place concerns abbreviations not resolved in figures; this finding concerns the incomplete data availability statement. |
| Suggestion | Replace the sentence at p. 16, l. 490 by an itemised statement: for each source (synthetic data, geological maps including the inferred and modified maps, land cover and outcrop data with providers, source and detrital XRD data with sample locations and dates, zircon data, export estimate, code) say where it is (deposit folder, external provider with reference, or not shared with reason); add SwissTopo 2018 and GeoCover to the reference list and cite them in Sect. 4 at p. 9, l. 270. |
| Status | wording verified at the page images p. 16 and 25; searches verified on text.json; deposit content verified for the two quoted folder names (README.md of tag v1.0.0 read via https://raw.githubusercontent.com/fdedonck/Non-Linear-XRD-Inversion/v1.0.0/README.md); absence of the other items in the README inferred; archive contents not checked |
| Severity | moderate |
| Source | S2 |

**GB-68 Several reference entries deviate from the format of the rest of the list: missing publisher or source, a whole-book page span, residual catalogue data, two ISBNs, lower case in a publisher name.**

| Field | Content |
|---|---|
| Check | P16 |
| Location | p. 17, l. 521; p. 17, l. 526 to 527; p. 18, l. 567 to 568; p. 19, l. 583; p. 19, l. 597 to 598; p. 19, l. 599 to 600; p. 20, l. 612 to 613; p. 20, l. 634 to 635 |
| Quotation | "Geologischer Atlas der Schweiz 1:25 000, 1953."; "Gjems, O.: Studies on clay minerals and clay-mineral formation in soil profiles in Scandinavia, 1967."; "UNESCO 2009, ISBN 9789231041358, oCLC: 1402659188, 2009"; "ISBN 9780898715729 9780898717921, 2005"; "Mineralogical society of America" |
| Concern | The other book and chapter entries give publisher and place (for example Aster et al., p. 17, l. 514 to 516; Menke, p. 19, l. 610 to 611). Deviating: Bearth (p. 17, l. 521) and Gjems (p. 19, l. 583) give no publisher or series; Lafuente et al. (p. 19, l. 599 to 600) give a volume title and pages but no editors or publisher; Kobe (p. 19, l. 597 to 598) gives a volume but no issue or article number; Moore and Reynolds (p. 20, l. 612 to 613) give a page span after the place of a whole book; the "E., W. D." entry (p. 18, l. 567 to 568) repeats the year in the publisher field and keeps a catalogue number "oCLC"; Tarantola (p. 20, l. 635) lists two ISBNs; Bish and Post (p. 17, l. 526) write "Mineralogical society of America". All confirmed on the page images p. 17 to 20. The author name of the "E., W. D." entry is treated in GB-04; conformity with a citation style is an optional check. |
| Suggestion | Add publisher and place (and series where applicable) for Bearth, Gjems and Lafuente et al., the issue and article number for Kobe; remove "oCLC: 1402659188" and the inner "2009"; keep one ISBN for Tarantola; write "Mineralogical Society of America"; for Moore and Reynolds give cited pages with "pp." or none. |
| Status | verified |
| Severity | minor |
| Source | S4 |

#### Minor corrections

| ID | Location | Quotation | Replacement | Source |
|---|---|---|---|---|
| KK-29 | p. 16, l. 491 to 494 | "All authors (FDD, FH, BB, TA)"; "F.H."; "F.D.D."; "B.B."; "T.A." | one form of initials throughout, for example "FDD, FH, BB, TA" | S4 |
| KK-30 | p. 17, l. 522 to 523 | "Master’s thesis, University of Lausanne, unpublished master’s thesis, 2021." | "Master’s thesis (unpublished), University of Lausanne, 2021."; see GB-21 (the undocumented samples and zircon protocol), which treats a different aspect of the same place | S4 |
| KK-31 | p. 19, l. 578 | "[No title found]" | "Landscape indicators of human impacts to riverine systems" (record read at https://experts.illinois.edu/en/publications/landscape-indicators-of-human-impacts-to-riverine-systems/: Aquatic Sciences 64(2), 118 to 128, doi 10.1007/s00027-002-8060-2) | S4 |
| KK-32 | p. 20, l. 612 | "Oxford University Press, New-York" | "Oxford University Press, New York"; see GB-68 (formal defects of reference entries), which treats a different aspect of the same place | S4 |
| KK-33 | p. 20, l. 639 | "Bomb-fallout137 Cs" | "Bomb-fallout ¹³⁷Cs" (superscript attached to "fallout" on the page image p. 20) | S4 |

#### Verification log

| ID | Check | Checked | Values | Result |
|---|---|---|---|---|
| PP-26 | P4 | Equation numbering and references; section numbering; citations against reference list in both directions | Equations (1) to (22) on p. 5 to 8, consecutive; references to Eq. 7, 10 to 16 and 1 to 4 point to the stated expressions; sections 1 to 6 without numeric gap; 64 distinct author-year citations in p. 1 to 16 and 64 entries in p. 17 to 21, each citation matched to exactly one entry by first surname and year, no entry without citation; "et al." for every entry with more than two authors; no "Section", "Table", "Appendix" or "Supplement" cross-reference in p. 1 to 21 | no finding beyond GB-03 and GB-04 |
| PP-27 | P15 | Each statement of Sect. 5 and 6 mapped to the Results; outlook proposals held against own findings; verbs | Consistent: "distinct source signatures are essential" (p. 15, l. 456 to 458) with scenario 2; "accurate spatial delineation ... is crucial" (p. 15, l. 459 to 460) with scenario 1; resolution and covariance as reliability measures with p. 10, l. 299 to 304; XRD limitations (p. 15, l. 469 to 476) argued from literature with hedged verbs. Proposal b) consistent with scenario 2; c) "multiple" tracers consistent with scenario 3. Search p. 15, l. 450 to p. 16, l. 489 for "future", "further work", "next step", "should be tested": 0 hits | findings GB-01, GB-65, GB-11, GB-47, GB-60, GB-61, GB-62, GB-63, GB-29, GB-66; remaining statements no finding |
| PP-28 | P12 | Every data source named in Sect. 3 and 4 and in the figure credits, held against the statement at p. 16, l. 490 and the deposit README | (1) synthetic data: covered; (2) geological maps: not named; (3) land cover, outcrops, personal communication: only Fig. 4 credit; (4) source samples: raw XRD in README, locations nowhere; (5) Gorner-Grenz samples: number and dates not stated; (6) WinXRD processing: not mentioned; (7) zircon: raw data in README, protocol only in an unpublished thesis; (8) export estimate: nowhere; (9) code: deposit; (10) figure scripts: README names Matplotlib and Seaborn | findings GB-47, GB-67, GB-21; items 1, 9, 10 no finding; limits stated by the manuscript itself: none on data access |
| PP-29 | P12 | Reachability and content of the link at p. 16, l. 490 | https://doi.org/10.5281/zenodo.17120374 redirects to https://zenodo.org/records/17120374; record "fdedonck/Non-Linear-XRD-Inversion: First public release", v1.0.0, published 15 September 2025, CC BY 4.0, one file of 49.3 MB; README.md of tag v1.0.0 read via raw.githubusercontent.com; archive contents not checked | no finding on reachability |
| PP-30 | P16 | Hyphenation, line and URL breaks, extraction artefacts, reference formalities | Line-end hyphenation checked on the page images p. 1 to 21 (for example "eco-/logical" p. 1, l. 1 to 2; "conflu-/ence" p. 13, l. 406 to p. 14, l. 407): correct; DOI break at p. 20, l. 632 to 633 falls on a genuine hyphen; article numbers with thin space uniform; only in text.json, not on the page image, hence not reported: copyright sign, ligature splits in the body text, "f or" in Eq. 1 | no finding beyond GB-68, GB-12 and the minor corrections |
| PP-31 | ZF 4.1 | Mandatory fields of every instance finding (title, check, location, quotation, concern, suggestion, status, severity, source) and of every minor correction (location, quotation, replacement, source) | Instance findings: S1 5, S2 11, S3 20, S4 15, AB 24, SD 23, total 98; minor corrections: S1 6, S2 12, S3 5, S4 29, AB 18, SD 4, total 74; verification logs: 54. Every finding and correction had all mandatory fields; none was returned or discarded for a missing field, and none was discarded after checking at the manuscript | 0 findings discarded |
| PP-32 | ZF 4.2, 4.3, 4.4 | Duplicates, contradictions and notes outside the checklists | Instance findings 98 resulted in 66 findings: 59 instance findings were combined into 27 merged findings (SD-GB-12 split into its four parts: ranking, tracer statement, source areas, outlook); 24 minor corrections were absorbed into findings that name their place; 27 minor corrections were combined into 10; mapping: GB-01 from S4-GB-01, SD-GB-01; GB-04 from S4-GB-03, S1-KK-06; GB-10 from S2-GB-11, S1-KK-01, S1-KK-02, S1-KK-03, S4-KK-02, S4-KK-03, S4-KK-04; GB-11 from S4-GB-05, SD-GB-21; GB-19 from AB-GB-06, SD-GB-15; GB-20 from S2-GB-06, S3-GB-05; GB-21 from S2-GB-03, S3-GB-10, SD-GB-18; GB-25 from S2-GB-08, S3-GB-19, S2-KK-08, S3-KK-05, S4-KK-14, S4-KK-29, AB-KK-12, AB-KK-13, AB-KK-14; GB-29 from S4-GB-12, SD-GB-02; GB-31 from S3-GB-17, S4-GB-06, AB-GB-08, SD-KK-02; GB-33 from AB-GB-05, SD-GB-19; GB-35 from S3-GB-03, AB-GB-09, SD-GB-11; GB-36 from S3-GB-04, AB-GB-10, S2-KK-09, S4-KK-19; GB-38 from S3-GB-15, SD-GB-12 (part); GB-39 from S3-GB-11, AB-GB-14; GB-40 from S3-GB-13, AB-GB-15, S3-KK-01, S4-KK-21, SD-KK-03; GB-41 from S3-GB-12, AB-GB-16; GB-42 from S2-GB-04, S3-GB-18, S4-KK-22, AB-KK-17, SD-KK-01; GB-43 from AB-GB-19, SD-GB-09; GB-44 from AB-GB-23, SD-GB-04; GB-45 from S3-GB-08, S3-GB-20, SD-GB-05; GB-47 from S2-GB-01, S3-GB-07, S4-GB-07, SD-GB-03; GB-51 from AB-GB-11, AB-KK-08; GB-52 from S3-GB-16, AB-GB-13, SD-GB-13; GB-54 from AB-GB-18, SD-GB-08; GB-59 from AB-GB-20, SD-GB-10; GB-61 from S4-GB-09, SD-GB-12 (part); GB-62 from S4-GB-10, SD-GB-12 (part); GB-63 from S3-GB-01, S4-GB-11, SD-GB-06; GB-66 from S4-GB-13, SD-GB-12 (part); KK-01 from S2-KK-01, S4-KK-01; KK-02 from S1-KK-04, S2-KK-02; KK-03 from S1-KK-05, S4-KK-05; KK-05 from S3-KK-04, S4-KK-06, S4-KK-16; KK-12 from S2-KK-04, S2-KK-05, S2-KK-06, S2-KK-07, S4-KK-13; KK-13 from S2-KK-12, AB-KK-01; KK-14 from AB-KK-02, AB-KK-03, AB-KK-04, AB-KK-05, AB-KK-06; KK-20 from S3-KK-03, S4-KK-20; KK-21 from S3-KK-02, S4-KK-23; KK-28 from S2-KK-11, AB-KK-16. Notes outside the checklists raised as findings of origin ZF: 2 (GB-14, GB-16); all other notes were covered by a responsible instance or by a merged finding. | 66 merged findings from the instances plus 2 findings of origin ZF = 68 findings; 33 minor corrections. The pair check of formatpruefung.py (option paare) lists 95 pairs with overlapping locations in the final version; each was decided: same subject merged as mapped, different subject kept separate with a cross-reference half-sentence in the later finding or in the replacement column of the minor correction |
| PP-33 | ZF 4.3 | Contradictions between instances at the same place, decided at the manuscript | (1) Resolution diagonal: AB major, SD moderate; merged as major because the maps are used as reliability evidence. (2) Fig. 8: S3 and AB counted 5 unexplained runs, SD 6 missing runs; both are consistent (20 minus 14 = 6 not plotted, 1 of them explained). (3) Fig. 11 fingerprints against mineralogy: AB and SD agree in values (0.57, 0.57 against 0.57, 0.58 in Stockhorn unit). (4) Duplicate tracers: AB moderate, SD major; merged as major. (5) Chrysolite: S2 moderate (tracer identity open), S3 minor, others minor corrections; merged as moderate. (6) AB-PP-09 found no finding for Fig. 5 against p. 10, l. 293 to 308, while S3, S4 and AB noted the rising posterior covariance (p. 10, l. 306 to p. 11, l. 307) only as hints; the place was treated by a responsible instance, so no finding was raised. (7) Sub-claims corrected at the manuscript: AB-GB-04 said that Fig. 7 gives the unit of the area difference only in the colour bar, but the caption gives it too (page image p. 28), so the merged finding is narrowed to the two x-axes; S1-GB-03 called the second gap claim contradicted by De Doncker et al. (2020), which was assessed by its title only, so the merged finding says weakened, with status inferred; SD-GB-22 located Eq. 8 at p. 6, l. 185, it stands at l. 186 | decisions as stated; no contradiction left open |
| PP-34 | ZF 4.5 | Wording of every quotation and embedded quotation in the findings and minor corrections, and every count in the concerns | 555 quoted strings in quotations, concerns, suggestions and minor corrections compared with text.json (line breaks and hyphenation joined, Python): 415 found; 140 not found. Of these, the manuscript wording that text.json does not hold in readable form (Eq. 5, 9, 14 and 19; labels and credit text of the raster Figs. 4, 5, 7 and 12; the label of Fig. 3c split over two extracted lines) was confirmed on the page images p. 6 to 8, 25, 26, 28 and 33, the Fig. 3c label by S2 and AB at the page image p. 24; the remaining strings are search terms, proposed replacement wording, quotations from the deposit README or terms of this review. One quotation was shortened to the wording actually printed (prior misfit, p. 6, l. 184). Counts in the concerns recomputed with Python on text.json: cost and efficiency terms, export, noise, storage, pixel, sample, misfit names, land use, season terms, search terms of the literature checks | all quotations found or confirmed at the page image; counts recomputed with Python on text.json where stated |
| PP-35 | ZF 4.5, 7 | Locations at page boundaries and on lines marked unsure in text.json, counted at the page image from the nearest printed margin number | The location listing of formatpruefung.py (option fundorte) listed 109 locations in the first draft and 107 in the final version (page boundary, line given on another page in text.json, or line marked unsure). Each was counted on the page image from the nearest printed margin number (p. 1 to 16, 20, 21 viewed): equations count as one line each (p. 5 to 8); text.json is one line low on p. 3 after printed 90 and on p. 11 after printed 335, and lists p. 12, l. 373 and p. 11, l. 339 on the following page. Corrections made: the -ise example "regularised" is p. 9, l. 246 (not p. 8); the smoothing statement starts at p. 12, l. 373 (counted from printed 370), not l. 372; "Surprisingly" stands at p. 11, l. 338 (from printed 335); Eq. 8 is p. 6, l. 186 (from printed 185). The instance counts S2-PP-04, S3-PP-08 and S4-PP-06 were confirmed at the same images | all listed locations confirmed or corrected as stated |

## Optional checks

| Area | What it needs | Responsible | Run |
|---|---|---|---|
| DOI resolution | one retrieval per reference entry with DOI | `science-quellenapparat-pruefung` | no |
| Citation style | the name of the style | `science-zitierstil-harvard-ctr` or the style rules of the journal | no |
| AI statement against publisher policy | the AI policy of the target publisher | this review, on request | no |
| Relation to the authors' prior work | the prior work of the authors | this review, on request | no |
| Journal requirements | the author guidelines of the target journal | this review, on request | no |
| Factual correctness | access to the sources of the checked statements and a selection of sections | `science-faktenbeleg-pruefung`, `geo-frage-belegbasiert-klaeren` | no |

## Limits of this review

- Checked version: egusphere-2025-4695.pdf, 37 pages, SHA-256 9c80676054f96ecd6f00f4d2a8b5ba568e03c6949e3856d363ac1c4abb42e7bd.
- Sources not readable or read only in part: Das et al. (2023), full text (fetch error; abstract only); Yang et al. (2025), not readable (rate limit); Walden et al. (1997), Wilson et al. (1993) and Blaen et al. (2016), assessed by their titles in the reference list only; Kobe (2021) and Niu et al. (2020), abstract and article page only; the UNESCO report cited as "E., 2009", not readable (rate limit); Haddadchi et al. (2013), Klages and Hsieh (1975), Fathabadi and Jansen (2022) and Collins et al. (2020), titles only; the 49.3 MB code archive on Zenodo, contents not checked (README only).
- Findings with status assumption: 8 of 68 findings have status assumption for at least one part; these parts are put as questions to the authors.
- Optional checks run: 0 of 6.
- Omitted instances: none.
- Discarded findings: 0. No instance finding lacked a mandatory field, and none was refuted when checked at the manuscript (PP-31). Merged: 59 of 98 instance findings combined into 27 findings, 24 minor corrections absorbed into findings, 27 minor corrections combined into 10 (PP-32).
- Because the introduction is printed twice, locations in Segment 1 name both copies; values read from figures are measurements on page renderings (150 to 600 dpi) with the tolerances stated in the findings, not data from the authors.
