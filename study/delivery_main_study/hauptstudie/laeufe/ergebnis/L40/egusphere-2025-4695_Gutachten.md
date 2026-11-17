# Review report: From XRD signal to erosion rate maps

| Field | Value |
|---|---|
| Manuscript | De Doncker, F., Herman, F., Belotti, B. and Adatte, T. (2025) From XRD signal to erosion rate maps. EGUsphere preprint egusphere-2025-4695, https://doi.org/10.5194/egusphere-2025-4695 |
| Checked version | egusphere-2025-4695.pdf, 37 pages, SHA-256 9c80676054f96ecd6f00f4d2a8b5ba568e03c6949e3856d363ac1c4abb42e7bd |
| Date | 2026-10-18 |
| Language | English |
| Review instances | Segments 1 to 4, figures, study design; the six review instances ran as separate agents, each without context from the others; merging, overall assessment and format check by a further separate agent; no instance omitted |
| Note | Locations give the printed margin line numbers, confirmed on the page images; the figure pages 22 to 37 carry no line numbers and are located by figure and panel. A vertical bar inside a quotation is written as ∣ so that the tables stay intact. |

## Summary

The manuscript is a method-development study with synthetic forward-inverse tests and one natural application. It inverts binned X-ray diffraction (XRD) peak-area fingerprints of source rocks and of suspended sediment, together with a geological map of the source areas, into a raster map of erosion rates. The forward model is an erosion-weighted mixture of source fingerprints (Eq. 1 to 4) with erosion rates parametrised in log-space; the inverse problem is solved as a linearised Bayesian maximum a posteriori estimate with a steepest descent (SD) and a quasi-Newton (QN) scheme (Eq. 17 to 19), and posterior covariance, resolution and a normalised posterior covariance are reported as uncertainty metrics (Eq. 20 to 22). The synthetic part uses one "true" erosion map with a single hotspot, seven source units and 21 tracer minerals; it compares SD and QN, tests three degradation scenarios (three geological maps, 20 levels of fingerprint blending, 1 to 21 tracers) and sweeps five hyperparameters. The natural part uses the Gornergletscher catchment (Switzerland): XRD fingerprints of the seven units, a known-mixture analogue with samples from the Gorner-Grenz confluence subcatchment, in which one unit has no outcrops, and a comparison of zircon U-Pb, XRD and combined inversions of one detrital sample taken on 28 June 2019. Key numbers: total normalised posterior uncertainty 0.87 (zircon), 0.82 (XRD) and 0.86 (combined); average Jensen-Shannon (JS) distance of the source fingerprints 0.48 (zircon) and 0.57 (combined). The manuscript has 16 figures, no tables and no appendix.

## Strengths

1. The synthetic tests share one baseline configuration, so the effect of each degradation scenario and of each hyperparameter is read against the same reference; the baseline values agree across Figs. 5, 7, 8, 9 and 10 within the measurement uncertainty, and the tracer-number and map-mismatch statements agree with Figs. 7 and 9 (PP-24, PP-25, PP-27, PP-28). This makes the scenario results comparable with each other, which the manuscript uses for its recommendations (GB-33 limits the ranking drawn from them).
2. The linearised Bayesian formulation yields, for every inversion, spatial maps of posterior covariance, resolution and normalised covariance in addition to the erosion map, so that a reader sees where the solution is constrained; the uncertainty values given in the text for the natural inversions agree with those printed in Figs. 14 to 16 (PP-30, PP-34). GB-15 asks for exact definitions of the plotted metrics.
3. The natural known-mixture analogue uses a subcatchment in which one mapped unit has no outcrops as a negative control, and the zircon inversion of the same catchment serves as an independent benchmark; both give the natural part a test with an expected outcome rather than a description only (PP-31, GB-40, GB-44, which state what the tests can and cannot show in their present form).
4. The bookkeeping of the manuscript is consistent: every in-text citation has an entry and every entry is cited, figures 1 to 16 and equations 1 to 22 are numbered without gaps and referenced in order, and data and code have a persistent DOI; the authors also disclose the zircon data gaps, the instability of the unnormalised SD scheme and the inferred lithology under the ice (PP-06, PP-10, PP-17, PP-31, PP-37).

## Weaknesses

1. The main claims are stronger than the tests behind them. The synthetic validation generates and inverts noise-free data with the same forward model, a prior equal to the true mean and one map shape, and the Abstract nevertheless reports "consistent convergence" and a validated, time- and cost-effective method, although runs failed to converge and no time or cost is measured (GB-02, GB-03, GB-24, GB-58). Suggestion: add noisy ensemble tests with a prior not taken from the truth, and restate Abstract, Sect. 5 and Sect. 6 to what the tests show.
2. The natural comparison does not support its conclusion. The zircon matrix lacks or copies fingerprints for three of seven units, the comparison rests on one sample, and the combined inversion has a higher normalised uncertainty than XRD alone while the text says combining "further" stabilises and improves the solution; "stability" has no measure (GB-44, GB-45, GB-46, GB-47). Suggestion: compare on the units with measured fingerprints in both methods, on several dated samples, with a defined stability measure, and state the result relative to both single-data cases.
3. Several descriptions of the synthetic results do not match the figures they cite: the effect of the data standard deviation is negligible in Fig. 10 although the text reports a strong non-monotonic effect, the QN scheme is not more accurate than SD at the end of the runs, the ranking of degradation factors reverses under the manuscript's own metrics, and the statements on over-smoothing, on the iteration threshold and on errors "exceeding 700 mm/yr" have no support in the plotted values (GB-26, GB-30, GB-31, GB-32, GB-33, GB-34, GB-35, GB-36). Suggestion: rewrite Sect. 4.1.2 to 4.1.4 to the measured values, extend the sweeps where the text describes untested ranges, and report all runs.
4. Parts of the method cannot be checked or rebuilt. Normalising every sample by its own maximum peak area breaks the linear mixing that Eq. 1 assumes, the prior and the export estimate of the natural runs are not stated, the plotted uncertainty metrics do not match their definitions, Eq. 19 inverts a singular matrix, and the XRD settings, processing steps and raw data are neither described nor covered by the data statement (GB-12, GB-15, GB-16, GB-17, GB-18, GB-43, GB-66). Suggestion: add a methods table and an extended data statement, correct Eq. 19 and Sect. 3.3, and show in a synthetic test the bias caused by the normalisation.

## Findings by segment

### Segment 1: Title, Abstract, Introduction (p. 1 to 5)

#### Substantive findings

**GB-01 The temporal side of the motivation has no counterpart in the design.**

| Field | Content |
|---|---|
| Check | P10 |
| Location | p. 1, l. 1; p. 1, l. 10 to 14 |
| Quotation | "Understanding the spatio-temporal dynamics of suspended sediment source activation is essential" (p. 1, l. 1); p. 1, l. 13: "Identifying sediment source hotspots and the timing of their activation" |
| Concern | Abstract and Introduction frame the study with the temporal dynamics and the timing of source activation. The aims of Sect. 4 (p. 10, l. 280 to 285) and the results in Sect. 4 do not refer to time: search in `text.json`, p. 1 to 16, for "temporal" and "season": 3 hits (p. 1, l. 1 and l. 10, and the copy of l. 10 in Sect. 2, p. 3, l. 77), all in Abstract or Introduction. The catchment was chosen for the "availability of multi-year suspended sediment datasets" (p. 9, l. 268), but the zircon and XRD comparison uses one sample taken "on June 28, 2019, at 13:30" (p. 14, l. 423 to 424), and the samples of the subcatchment test are undated. Converting a single-time provenance signal into erosion rates with "a yearly sediment export estimate" (p. 16, l. 479 to 480) assumes that one sample represents the year; this assumption is not stated. GB-43 concerns the missing export value itself. |
| Suggestion | Either restrict the framing in Sect. 1 (p. 1, l. 1 and l. 10 to 14) to spatial attribution, or add a temporal analysis (dated samples over a season with the variation of source contributions); in both cases state in Sect. 3.1 the assumption that one sample represents the annual export. |
| Status | verified (wording and search) |
| Severity | moderate |
| Source | SD |

**GB-02 Time and cost efficiency is stated as a validated property of the method, but neither time nor cost is measured.**

| Field | Content |
|---|---|
| Check | P15, P33 |
| Location | p. 1, l. 3 to 4; p. 2, l. 40 to 42; p. 3, l. 74 to 75; p. 4, l. 107 to 109; p. 5, l. 141 to 142 |
| Quotation | "In this study, we validate a time- and cost-effective fingerprinting approach based on X-ray diffraction (XRD) data." (p. 1, l. 3 to 4); p. 3, l. 74 to 75: "To conclude, we show and validate the potential of binned XRD peak-area data as a cost- and time-efficient approach for constructing erosion rate maps." |
| Concern | Efficiency is part of the stated aim and of the concluding claim, and the comparison method, zircon U-Pb dating, was run in the same study (p. 14, l. 423 to 425), so both efforts could be reported. Search in `text.json`, p. 1 to 16, case-insensitive: "cost" 6 hits (p. 1, l. 3 and l. 4; p. 2, l. 40; p. 3, l. 74; p. 4, l. 107; p. 5, l. 141), "efficien" 4 hits (p. 2, l. 42; p. 3, l. 75; p. 4, l. 109; p. 5, l. 142), "inexpensive", "cheap", "hour", "price", "CHF", "USD", "EUR" 0 hits. All hits lie in Abstract and Introduction (l. 3 to 142); Methods, Results, Discussion and Conclusions (l. 143 to 489) contain none, and no cost, analyst time, instrument time or sample throughput is reported for XRD or for zircon dating. The only support is the citation "many of these methods are expensive and time-consuming (Das et al., 2023)" (p. 2, l. 35). Graded major: the headline claim of the Abstract, "validate a time- and cost-effective" approach, does not stand as stated if the finding holds. |
| Suggestion | Report per sample the preparation time, instrument time and cost of XRD and of zircon U-Pb dating (with sources) in Sect. 4.2.2 and take the comparison up in Sect. 5 and 6; otherwise remove "time- and cost-effective" (p. 1, l. 3 to 4) and "as a cost- and time-efficient approach" (p. 3, l. 74 to 75 and the copy at p. 5, l. 141 to 142) and keep cost only as motivation with the citation at p. 2, l. 35. |
| Status | verified (search as stated) |
| Severity | major |
| Source | S4, SD |

**GB-03 The Abstract reports "consistent convergence" of the synthetic tests, while the Results report unstable and non-converging runs.**

| Field | Content |
|---|---|
| Check | P2, P6 |
| Location | p. 1, l. 7; p. 11, l. 312; p. 12, l. 353; Fig. 8, caption |
| Quotation | "Forward-inverse tests with synthetic data demonstrate consistent convergence of the posterior solution." (p. 1, l. 7); "In initial experiments, the steepest descent approach proved unstable, requiring the normalization of the gradient." (p. 11, l. 312); "In many of these cases, the inversion fails to converge to a stable posterior solution." (p. 12, l. 353); Fig. 8, caption: "Note that the most blended example did not have a stable solution and is therefore not plotted." |
| Concern | The Results document convergence for the baseline QN and SD runs (Fig. 5 and 6, panels g), and the authors report the failures openly. The Abstract, however, generalises to the synthetic forward-inverse tests as a whole. Within these tests the SD scheme was unstable without gradient normalisation (p. 11, l. 312), the inversion "fails to converge" in "many" of the blended cases (p. 12, l. 353), and at least one run is excluded from Fig. 8 for lack of a stable solution. The Abstract therefore states a stronger result than Sect. 4.1 supports. GB-31 treats the number of excluded runs and GB-32 their error values; this finding concerns only the generalisation in the Abstract. |
| Suggestion | Restrict p. 1, l. 7 to the conditions under which convergence was shown (QN scheme, undegraded fingerprints or an average JS distance above a stated value) and state that the inversion fails to converge for poorly distinguishable fingerprints. |
| Status | verified (all passages read on the page images p. 1, 11, 12 and 29) |
| Severity | moderate |
| Source | S3, SD |

**GB-04 Sections 1 and 2 are the same Introduction twice.**

| Field | Content |
|---|---|
| Check | P4 |
| Location | p. 1, l. 9 (heading "1 Introduction"); p. 3, l. 76 (heading "2 Introduction") |
| Quotation | "1 Introduction" (p. 1, l. 9); p. 3, l. 76: "2 Introduction" |
| Concern | Section 1 runs from p. 1, l. 9 to p. 3, l. 75, Section 2 from p. 3, l. 76 to p. 5, l. 142. Word-by-word comparison with Python difflib of the body text (running heads excluded): 1153 words in each block, similarity ratio 1.0, no differing token; both blocks span 67 numbered lines. Confirmed on the page images: both headings, the identical citation lines (p. 2, l. 31 and p. 4, l. 98) and the identical last sentence (p. 3, l. 74 to 75 and p. 5, l. 141 to 142). As a result all later sections (3 Methods to 6 Conclusions) are numbered one too high, and every citation of the Introduction occurs twice (see PP-37). Graded minor because it concerns form only. |
| Suggestion | Delete Section 2 (p. 3, l. 76 to p. 5, l. 142) and renumber "3 Methods" to "6 Conclusions" as 2 to 5, including the subsections 3.1 to 4.2.2. |
| Status | verified (text comparison with Python; headings and repeated lines on the page images p. 1 to 5) |
| Severity | minor |
| Source | S4 |

**GB-05 The citation "E., 2009" and its reference entry carry an initial in place of the author surname.**

| Field | Content |
|---|---|
| Check | P4 |
| Location | p. 1, l. 11 to 12; p. 3, l. 78 to 79; p. 18, l. 567 to 568 |
| Quotation | "(Gergel et al., 2002; Allan, 2004; E., 2009; Hamel et al., 2015)" (p. 1, l. 11 to 12); p. 18, l. 567 to 568: "E., W. D.: The Impact of global change on erosion and sediment transport by rivers, UNESCO 2009, ISBN 9789231041358, oCLC: 1402659188, 2009." |
| Concern | The short citation consists of the letter "E." and cannot be matched to an author; the entry puts "E." in the surname position and is therefore sorted between Domingo (p. 18, l. 564) and Evrard (p. 18, l. 569). The entry also has "oCLC" in lower case and the year twice. The UNESCO report of this title is usually attributed to D. E. Walling, whose name the manuscript spells correctly in another entry (p. 20, l. 645); this attribution could not be confirmed from the report itself (archived copy returned a rate-limit page). Overlapping locations: GB-01 treats the temporal framing; this entry concerns the malformed citation "E., 2009". |
| Suggestion | Replace "E., 2009" at p. 1, l. 11 to 12 and p. 3, l. 78 to 79 by the surname printed on the report (presumably "Walling, 2009"), rewrite the entry at p. 18, l. 567 to 568, for example "Walling, D. E.: The impact of global change on erosion and sediment transport by rivers, UNESCO, ISBN 9789231041358, 2009.", after checking author and title on the report, and move it to its alphabetical place. |
| Status | verified for the malformed citation and entry (page images p. 1, 3, 18); inferred for the author identity (source not readable) |
| Severity | minor |
| Source | S4 |

**GB-06 The two citations for sediment traps on dams concern neither sediment traps, nor dams, nor sediment origin.**

| Field | Content |
|---|---|
| Check | P13 |
| Location | p. 1, l. 18 to 19; p. 3, l. 85 to 86; p. 17, l. 519 to 520; p. 21, l. 649 to 650 |
| Quotation | "Direct measurements, such as sediment traps installed on dams, provide valuable information on sediment fluxes but do not reveal the origin of the transported material (Wilson et al., 1993; Barker et al., 1997; Davis and Fox, 2009)." |
| Concern | The statement itself is uncontroversial, and Davis and Fox (2009), a review of sediment fingerprinting, fits it. The two other citations do not. Barker et al. (1997) evaluate terrestrial photogrammetry for monitoring and measuring river bank erosion; the abstract mentions neither sediment traps, dams, sediment fluxes nor sediment origin. Wilson et al. (1993) is, by its title in the reference list ("Soil erosion in the Falkland Islands: an assessment", p. 21, l. 649), an assessment of soil erosion; its bibliographic record lists soil erosion, grazing and burning as subjects. A reader who follows these two citations finds no support for the claim about sediment traps on dams. |
| Suggestion | In both copies of the sentence (p. 1, l. 19 and p. 3, l. 86) replace Wilson et al. (1993) and Barker et al. (1997) by works that measure sediment fluxes with traps or reservoir deposits, or keep only Davis and Fox (2009); delete the two entries if they are cited nowhere else. |
| Status | Barker et al. (1997): verified, abstract read on the University of Portsmouth research portal (https://researchportal.port.ac.uk/en/publications/use-of-terrestrial-photogrammetry-for-monitoring-and-measuring-ba/). Wilson et al. (1993): inferred, only title and subject metadata read (OpenAlex record https://api.openalex.org/works/doi:10.1016/0143-6228(93)90036-Z, no abstract). |
| Severity | minor |
| Source | S1 |

**GB-07 Four citations in the list of fingerprinting tools do not belong to the tracer they are cited for, among them a theology article for pollen and a mineral magnetic study for mineralogy.**

| Field | Content |
|---|---|
| Check | P4, P13 |
| Location | p. 2, l. 27 to 31; p. 3, l. 94 to p. 4, l. 98; p. 17, l. 528 to 530; p. 19, l. 597 to 598; p. 20, l. 639 to 642 |
| Quotation | "radionuclides (Vanden Bygaart and Protz, 2001; Bezuidenhout, 2023; Abere et al., 2025)"; "nutrients (Blaen et al., 2016; Asadi et al., 2025)"; "mineralogy (Walden et al., 1997; Nukazawa et al., 2021)"; "plant pollen content (Brown, 1985; Kobe, 2021)" |
| Concern | The list of "Common fingerprinting tools" is the manuscript's overview of the state of the art, and most of its citations fit their tracer. Four do not. (1) Kobe (2021), cited for plant pollen content, is "Ubuntu as a spirituality of liberation for black theology of liberation" in HTS Teologiese Studies (p. 19, l. 597); the article page and abstract contain nothing on pollen, sediment or source fingerprinting, so the pollen statement rests on Brown (1985) alone. (2) Vanden Bygaart and Protz (2001), cited for radionuclides, use bomb-fallout 137Cs profiles as a marker of geomorphic stability in dune sands; the abstract describes no attribution of sediment to sources. (3) Walden et al. (1997), cited for mineralogy, is titled "Use of mineral magnetic measurements to fingerprint suspended sediment sources" (p. 20, l. 641), so it belongs to the magnetic category the same sentence lists separately. (4) Blaen et al. (2016), cited for nutrients, is titled "Real-time monitoring of nutrients and dissolved organic matter in rivers" (p. 17, l. 528 to 529), which points to water quality monitoring rather than to source tracing. The misplacement under "mineralogy" matters most, because mineralogy is the tracer class the manuscript sets out to advance, while Klages and Hsieh (1975), already in the reference list (p. 19, l. 595 to 596) and an X-ray diffraction study of suspended-solids sources, is not cited at this place. Graded moderate because a reader cannot trace the precedents for the tracer class on which the contribution rests; the results are not affected. GB-08 concerns the gap claim that follows the list. |
| Suggestion | In both copies of the list (p. 2, l. 27 to 31 and p. 3, l. 94 to p. 4, l. 98) delete Kobe (2021) or replace it by a pollen fingerprinting study; move Walden et al. (1997) to "magnetic susceptibility" and cite Klages and Hsieh (1975) under "mineralogy"; replace Vanden Bygaart and Protz (2001) and Blaen et al. (2016) by studies that use radionuclides or nutrients to discriminate sediment sources, or delete them; update the reference list. |
| Status | Kobe (2021): verified, publisher article page with abstract read (https://hts.org.za/index.php/hts/article/view/6176, via https://doi.org/10.4102/hts.v77i3.6176), independently by two instances. Vanden Bygaart and Protz (2001): verified, abstract read in OpenAlex (https://api.openalex.org/works/doi:10.1002/esp.215). Walden et al. (1997): verified from the title on page image p. 20 and the OpenAlex record (https://api.openalex.org/works/doi:10.1016/S0022-1694(97)00078-4). Blaen et al. (2016): title verified on page image p. 17; that it does not use nutrients as source tracers is inferred (no abstract in OpenAlex). Klages and Hsieh (1975): verified, abstract read in OpenAlex (https://api.openalex.org/works/doi:10.2134/jeq1975.00472425000400010016x). |
| Severity | moderate |
| Source | S1, S4 |

**GB-08 The claim that XRD has only recently gained attention in provenance analysis and remains underutilised has no stated basis, and a work the manuscript itself cites used XRD for sediment sources in 1975.**

| Field | Content |
|---|---|
| Check | P28 |
| Location | p. 2, l. 36 to 37; p. 4, l. 103 to 104 |
| Quotation | "X-ray diffraction (XRD) has recently gained attention as a proxy for mineral abundance in provenance analysis but remains underutilized (Das et al., 2023)." |
| Concern | The sentence is the gap claim that motivates the study ("Building on the work of Das et al. (2023, 2024)", p. 2, l. 40). The manuscript names no literature search: in `text.json`, p. 1 to 16, "search", "Web of Science", "Scopus", "Google Scholar" and "literature" give 0 hits, "database" 1 hit, which refers to the RRUFF mineral database (p. 9, l. 257). Three works show that XRD mineralogy for sediment provenance is not recent: Klages and Hsieh (1975), cited by the manuscript for the fingerprinting principle (p. 1, l. 21 and l. 25), inferred the sources of the silt and clay of the Gallatin River by X-ray diffraction; Eberl (2004) determined the proportions of sediment sources in river sediment by unmixing quantitative XRD mineralogy; Andrews and Eberl (2012) published the SedUnMix program for this unmixing and tested it with mixtures of known proportions. "Recently" therefore does not hold, and "underutilized" needs a basis. Whether Das et al. (2023) states it could not be checked (only a summary of the abstract was accessible). GB-09 proposes the two works by Eberl as missing literature; this finding concerns the unsupported gap claim. |
| Suggestion | Rewrite the sentence in both copies (p. 2, l. 36 to 37; p. 4, l. 103 to 104), for example: "XRD mineralogy has been used to infer suspended sediment sources since Klages and Hsieh (1975) and in quantitative unmixing (Eberl, 2004; Andrews and Eberl, 2012), but binned XRD peak areas have rarely been used as fingerprints (Das et al., 2023)", and either give the basis for "underutilized" or delete the word. |
| Status | Absence of a search description: verified (search as stated). Klages and Hsieh (1975): verified, abstract read (https://api.openalex.org/works/doi:10.2134/jeq1975.00472425000400010016x). Eberl (2004) and Andrews and Eberl (2012): verified, abstracts read on the USGS publication pages (https://pubs.usgs.gov/publication/70026557, https://pubs.usgs.gov/publication/70032707). Content of Das et al. (2023): inferred, full text not accessible (https://api.semanticscholar.org/graph/v1/paper/DOI:10.1029/2023WR034500, summary of the abstract only). |
| Severity | moderate |
| Source | S1 |

**GB-09 Work on quantitative XRD unmixing of sediment provenance and on spatial patterns of glacial catchment erosion from detrital data is missing from the positioning.**

| Field | Content |
|---|---|
| Check | P14 |
| Location | p. 2, l. 36 to 42; p. 4, l. 103 to 109; p. 2, l. 58 to p. 3, l. 63; p. 4, l. 125 to p. 5, l. 130 |
| Quotation | "Building on the work of Das et al. (2023, 2024), we investigate the potential of binned XRD data as a cost-effective fingerprinting method."; "This spatially informed approach to sediment provenance is particularly valuable in glacierized catchments, where ice cover limits direct observations" |
| Concern | The Introduction positions the XRD part only against Das et al. (2023, 2024) and the spatial part only against the authors' own framework (De Doncker et al., 2020). Three works that anticipate or bound parts of the contribution are not in the reference list (search in `text.json`, p. 17 to 21, for "Eberl", "Andrews", "Ehlers", "Enkelmann": 0 hits each). (1) Eberl, D. D. (2004) Quantitative mineralogy of the Yukon River system: changes with reach and season, and determining sediment provenance. American Mineralogist, 89, 1784-1794, https://doi.org/10.2138/am-2004-11-1225: it determines the proportions of sediment sources in river sediment by unmixing quantitative XRD mineralogy and reports that at least three sources can be identified with good accuracy. (2) Andrews, J. T. and Eberl, D. D. (2012) Determination of sediment provenance by unmixing the mineralogy of source-area sediments: the "SedUnMix" program. Marine Geology, 291-294, 24-33, https://doi.org/10.1016/j.margeo.2011.10.007: an unmixing program for XRD mineralogy with up to six end members that recommends validation with artificial mixtures of known proportions, the test which the manuscript replaces by a "natural analogue" (p. 13, l. 404 to 406). (3) Ehlers, T. A., Szameitat, A., Enkelmann, E., Yanites, B. J. and Woodsworth, G. J. (2015) Identifying spatial variations in glacial catchment erosion with detrital thermochronology. Journal of Geophysical Research: Earth Surface, 120, 1023-1039, https://doi.org/10.1002/2014JF003432: it infers the spatial distribution of erosion in a heavily glaciated catchment from detrital grains, which bears directly on the claim that a spatially informed approach is particularly valuable in glacierised catchments. GB-08 concerns the gap claim at p. 2, l. 36 to 37; this finding the missing literature. Overlapping locations: GB-02 treats the unmeasured time and cost efficiency; this entry concerns missing literature. |
| Suggestion | Add the three works to the Introduction, (1) and (2) in the XRD paragraph (p. 2, l. 36 to 42 and its copy), (3) in the paragraph on spatially explicit erosion maps (p. 2, l. 58 to p. 3, l. 63 and its copy), and state what binned peak areas and the spatial inversion add to them. |
| Status | Eberl (2004) and Andrews and Eberl (2012): verified, abstracts read on the USGS pages (https://pubs.usgs.gov/publication/70026557, https://pubs.usgs.gov/publication/70032707), bibliographic data from OpenAlex (https://api.openalex.org/works/doi:10.1016/j.margeo.2011.10.007; OpenAlex gives 2011 for the online version, USGS 2012 for the volume). Ehlers et al. (2015): verified, abstract read in OpenAlex (https://api.openalex.org/works/doi:10.1002/2014JF003432). Absence from the reference list: verified (search as stated). |
| Severity | moderate |
| Source | S1 |

**GB-10 The Introduction places the approach between Bayesian linear mixing and hierarchical Bayesian models, but the method has no hierarchical element, and the model class is named in two ways.**

| Field | Content |
|---|---|
| Check | P10, P38 |
| Location | p. 2, l. 53 to 57; p. 4, l. 120 to 124 |
| Quotation | "Our approach can be seen as a hybrid between Bayesian linear mixed models and hierarchical Bayesian models" |
| Concern | The manuscript itself defines hierarchical models as those which "aim to model the uncertainties in the parameters themselves" (p. 2, l. 54). The method is a MAP estimate with a linearised Gaussian posterior (p. 6, l. 173 to 180) and fixed hyperparameters chosen by synthetic sweeps (p. 10, l. 293 to 295); no hyperprior and no group level is estimated. The frame is not taken up again in Sect. 5 or 6: search in `text.json`, p. 1 to 16, for "hierarch": 4 hits, all in the two copies of the Introduction (p. 2, l. 54 and l. 56; p. 4, l. 121 and l. 123). In addition, the sentence names "Bayesian linear mixed models", while l. 53 introduces "Bayesian Linear Mixing Models (BLMM)" (compared on the page images: "mixed" at p. 2, l. 55 to 56 and p. 4, l. 122 to 123, "Mixing" at p. 2, l. 53 and p. 4, l. 120). |
| Suggestion | Describe the approach in Sect. 1 (p. 2, l. 55 to 57 and its copy) as a linearised Bayesian (MAP) inversion in the sense of Tarantola (2005), or add a hierarchical treatment of the data and model standard deviations and the smoothing distance; if the comparison is kept, write "Bayesian Linear Mixing Models (BLMM)" as in l. 53. |
| Status | verified (wording, search) |
| Severity | minor |
| Source | SD, S1, S2, S4 |

#### Minor corrections

| ID | Location | Quotation | Replacement | Source |
|---|---|---|---|---|
| KK-01 | p. 1, l. 5 | "(steepest descent and Quasi-Newtonian)" | "(steepest descent and quasi-Newton)", the form used at p. 7, l. 211 and p. 10, l. 296 | S2 |
| KK-02 | p. 2, l. 48 to 51; p. 4, l. 115 to 118 | "the Non-Linear Least Squares (NLLS) (a constrained linear regression)"; "Generalist Likelihood Uncertainty Estimation (GLUE)"; "Maximal Likelihood Estimation (MLE) (similar to the NNLS approach" | "the Non-Negative Least Squares (NNLS) (a constrained linear regression)", "Generalized Likelihood Uncertainty Estimation (GLUE)" (the method of Beven and Binley, 1992), "Maximum Likelihood Estimation (MLE) (similar to the NNLS approach". The instances disagreed on the direction (NNLS for NLLS, or NLLS for NNLS); decided for NNLS because the description "constrained linear regression" fits non-negative least squares; if non-linear least squares is meant, write "NLLS" in both places and delete "(a constrained linear regression)". Compared on the page images: both copies read "NLLS", "Generalist", "Maximal" and "NNLS". | S1, S2, S4, SD |
| KK-03 | p. 2, l. 61; p. 4, l. 128; p. 11, l. 333 to 334; p. 14, l. 424 to 425 | "validated in (De Doncker et al., 2020)"; "proposed by (Steck et al., 2015)"; "described in (Belotti, 2021)"; "outlined in (De Doncker et al., 2020)" | narrative citations: "validated in De Doncker et al. (2020)", "proposed by Steck et al. (2015)", "described in Belotti (2021)", "outlined in De Doncker et al. (2020)"; five places compared on the page images p. 2, 4, 11, 14 Overlapping locations: GB-09 treats missing literature; this entry concerns the form of narrative citations. | S3, S4 |
| KK-04 | p. 3, l. 70; p. 5, l. 137 | "we optimize the hyper-parameters" | "we optimize the hyperparameters", the form at p. 10, l. 281 and p. 12, l. 370. GB-50 concerns the content of this sentence (which values were selected). | S2 |

#### Verification log

| ID | Check | Checked | Values | Result |
|---|---|---|---|---|
| PP-01 | P13 | Statements in Abstract and Introduction that report content of cited works, checked against the source where readable | Abstract (p. 1, l. 1 to 8): no statement from cited works, no numbers from other works. Torres Astorga et al. (2020) for TOC (p. 2, l. 30): abstract fits. Klages and Hsieh (1975) for the fingerprinting principle (p. 1, l. 20 to 21): abstract fits; for the two criteria of an ideal fingerprint (p. 1, l. 24 to 25) the abstract is silent, full text not read. Das et al. (2024) for "Building on the work" (p. 2, l. 40): abstract read on the Rothamsted repository page, compares MIR and XRD fingerprints with MixSIAR, fits. De Doncker et al. (2020) for the spatial framework (p. 2, l. 61): abstract fits. Niu et al. (2020) for linear mixing (p. 2, l. 59): record lists "linear mixing model" as keyword. Delbecque et al. (2022) for magnetic susceptibility (p. 2, l. 29): record concerns urban soils, no abstract, not raised. No sentence in Segment 1 reports a number from another work. | no finding beyond GB-06 and GB-07 |
| PP-02 | P13 | Sources not readable beyond metadata or a summary | Das et al. (2023), https://doi.org/10.1029/2023WR034500: summary of the abstract only (claims at p. 2, l. 35 and l. 37 not checkable). Haddadchi et al. (2013), Yang et al. (2025), Fathabadi and Jansen (2022), Niu et al. (2020): no abstract available (Yang et al. repository entry https://hub.hku.hk/handle/10722/368192 without file). Asadi et al. (2025): tracers not identifiable from the record. Wilson et al. (1993): metadata only. | no finding; sources named under Limits of this review |
| PP-03 | P14 | Search for works that anticipate, bound or contradict the contribution, five queries; each candidate held against the reference list p. 17 to 21 | Queries on XRD unmixing (SedUnMix, Eberl), detrital thermochronology of glacial erosion (Ehlers et al. 2015), Bayesian inversion of detrital data into erosion maps, Avdeev et al. (2011), XRD fingerprinting in glacierised catchments. Candidates: Eberl (2004), Andrews and Eberl (2012), Ehlers et al. (2015): 0 hits in the reference list, proposed in GB-09. Avdeev et al. (2011), https://doi.org/10.1016/j.epsl.2011.03.020: not proposed, neither abstract nor full text readable. Results pointing to this manuscript, its discussion or a later version were not opened. | finding GB-09 |
| PP-04 | P28 | Gap and novelty sentences in p. 1 to 16 and whether a search method is given | `text.json`, case-insensitive: "recently" 2 hits (p. 2, l. 36; p. 4, l. 103), "underutil" 2 hits (p. 2, l. 37; p. 4, l. 104), "novel" 1 hit (p. 15, l. 454), "first time", "for the first", "no stud", "not been", "has not", "have not", "never" together 1 hit ("Nevertheless", p. 11, l. 317, no gap claim); search method terms 0 hits. The sentence on approaches without spatially explicit maps (p. 2, l. 58 to 59) is hedged by "typically" and names the own framework, not raised. | findings GB-08 and GB-59 |

### Segment 2: Methods, data preparation, study area (p. 5 to 10; Fig. 1 to 4)

#### Substantive findings

**GB-11 Methodologically important limits appear only in the Results or the Discussion, not where the affected method is introduced.**

| Field | Content |
|---|---|
| Check | P17 |
| Location | p. 5, l. 147 to 148; p. 8, l. 213 to 214; p. 9, l. 249; p. 3, l. 71 to 73 |
| Quotation | "These sediments are then transported or stored." (p. 5, l. 147 to 148); p. 15, l. 466 to 468: "We caution against using this method in catchments with significant sediment storage, as the inversion directly links sediment provenance to erosion rates and assumes immediate sediment export" |
| Concern | Four limits are stated far from their method. (1) The immediate-export assumption belongs to the forward model of Sect. 3.1, which instead says that sediments "are then transported or stored" (p. 5, l. 147 to 148); the assumption appears only in the Discussion (p. 15, l. 466 to 468). (2) The gradient normalisation of the SD scheme changes Eq. 18 (p. 8, l. 213 to 215), but it is mentioned only in Sect. 4.1.2 (p. 11, l. 312 to 313). (3) Grain size and preferred orientation affect the XRD chain of Sect. 3.4 (from p. 9, l. 249), but are discussed only in Sect. 5 (p. 15, l. 469 to p. 16, l. 476). (4) The zircon gaps are stated only in Sect. 4.2.2 (p. 14, l. 430 to 434), not where the zircon comparison is announced (p. 3, l. 71 to 73; p. 10, l. 284 to 285). A reader of the Methods does not see them. GB-26 concerns the SD normalisation as a reproducibility issue of the scheme comparison, GB-44 the consequences of the zircon gaps, GB-63 the XRD mitigations. |
| Suggestion | State each limit at its method: the storage assumption in Sect. 3.1, the gradient normalisation as part of Eq. 18, the XRD biases in Sect. 3.4, the zircon gaps in Sect. 1 (p. 3, l. 71 to 73) and in the aims of Sect. 4 (p. 10, l. 284 to 285). |
| Status | verified |
| Severity | moderate |
| Source | SD |

**GB-12 The quasi-Newton update in Eq. 19 inverts a matrix that is singular in this underdetermined problem, so the step cannot be computed as printed.**

| Field | Content |
|---|---|
| Check | P25 |
| Location | p. 6, l. 170 to 172; p. 8, l. 219 (Eq. 19); p. 8, l. 225 (Eq. 20) |
| Quotation | "Our inverse problem is underdetermined: the number of tracers, representing the data we have, is smaller than the number of pixels for which we want to infer the erosion rates." |
| Concern | Eq. 19, as printed on page image p. 8, contains the inverse of GnT Cd^-1 Gn without the prior term. G has m rows (21 tracers) and n columns (pixels), so GT Cd^-1 G is an n by n matrix of rank at most 21, and at most 7 because pixels of one unit share one fingerprint; it has no inverse when n exceeds this rank, as the manuscript states it does (p. 6, l. 170 to 172). Eq. 20 includes Cm^-1 in the same matrix, which makes it invertible; Eq. 19 does not. A reader cannot tell which update the code applies (prior term included, damping or a pseudo-inverse). KK-10 concerns the iteration index in the same equation. |
| Suggestion | State the update actually implemented and correct Eq. 19 accordingly, for example with the inverse of (GnT Cd^-1 Gn + Cm^-1), consistent with Eq. 20, with a reference to the code version on Zenodo. |
| Status | verified (equation and stated dimensions on page image p. 8); inferred (rank argument) |
| Severity | moderate |
| Source | SD |

**GB-13 The Gaussian approximation behind all uncertainty metrics is applied without a check, also to runs that are far from weakly non-linear.**

| Field | Content |
|---|---|
| Check | P26 |
| Location | p. 6, l. 177 to 178; p. 8, l. 223 to 225; p. 10, l. 294 to 295 |
| Quotation | "We assume weak nonlinearity, where our forward model can be linearized around the prior, hence, the a posteriori probability density remains approximately Gaussian." |
| Concern | Erosion rates are modelled as exp(ε) with a prior standard deviation of 3 in ε (p. 10, l. 294 to 295). One standard deviation therefore spans a factor of exp(-3) = 0.050 to exp(3) = 20.1 around the prior, two standard deviations a factor of exp(6) = 403 (Python). The zircon run reaches "extreme erosion rate values (>8000 mm/y)" (p. 14, l. 435). Under such ranges a linearisation around the prior is not evidently valid, yet Eq. 20 and the derived metrics are reported for every run, including the one the authors call "highly unstable". No check of the Gaussian approximation, for example by sampling the posterior for one case, is reported. |
| Suggestion | State in Sect. 3.3 the conditions under which Eq. 20 is used, and for the synthetic QN case and one natural case compare the linearised uncertainty with a sampled posterior (for example Markov chain Monte Carlo or randomised maximum likelihood); flag runs outside the validity range in Fig. 14. |
| Status | verified (parameter values and the stated premise of weak non-linearity); inferred (factor spans) |
| Severity | moderate |
| Source | SD |

**GB-14 The claimed error propagation covers only an assumed data variance; the uncertainty of the source fingerprints is not propagated, and the data standard deviation is not derived from measurements.**

| Field | Content |
|---|---|
| Check | P31 |
| Location | p. 6, l. 185 to 186 (Eq. 8); p. 1, l. 6 to 7; p. 10, l. 295; p. 14, l. 427 to 428 |
| Quotation | "in order to invert detrital mineralogical data into erosion rate maps while quantifying posterior uncertainty and error propagation" |
| Concern | The data covariance is Cd = σd² I (Eq. 8), with σd = 0.01 mm/y taken over from the synthetic tests for the natural runs (p. 14, l. 427 to 428). The tracer matrix A enters as exact: the variability of the fingerprints within a unit, the uncertainty of the inferred geology and the uncertainty of the export estimate are not part of the propagated error. With noise-free synthetic data σd hardly matters (Fig. 10, third row: range of about 0.012 % in the total absolute difference, see GB-35), so the sweep does not show which σd is appropriate for real XRD data. The posterior uncertainty values compared in Sect. 4.2.2 (0.82, 0.86, 0.87) therefore exclude the source term, which may differ strongly between XRD and zircon. GB-03 concerns the convergence claim in the next sentence of the Abstract; this finding concerns the scope of "error propagation". |
| Suggestion | Derive σd in Sect. 3.2 from replicate XRD measurements of detrital samples and add a fingerprint covariance from replicate source samples to Cd; otherwise state in the Abstract and in Sect. 3.3 that the reported uncertainty is conditional on exact fingerprints, geology and export. |
| Status | verified (Eq. 8, parameter values); inferred (consequence for the comparison) |
| Severity | moderate |
| Source | SD |

**GB-15 The plotted and reported uncertainty metrics do not match their definitions in Sect. 3.3, and they carry many names.**

| Field | Content |
|---|---|
| Check | P2, P8, P38 |
| Location | p. 8, l. 230 to 239 (Eq. 21, Eq. 22); p. 10, l. 303; p. 14, l. 436; Fig. 5, panels (d), (f), (h); Fig. 7; Fig. 10, second column; Fig. 14, resolution panel |
| Quotation | "Where the diagonal of R is close to 1, data have improved our knowledge considerately relative to the prior." (p. 8, l. 235 to 236); p. 14, l. 436: "a high total normalized uncertainty (tr(Cm,post)/tr(Cm)) value of 0.87" |
| Concern | Sect. 3.3 introduces the metrics with a source (Tarantola, 2005). Three points do not fit the results. (1) Definition of the normalised uncertainty: Eq. 22 defines an element-wise ratio of square roots of the posterior and prior covariance, written with C̃m; the Results use a ratio of traces without square root, written with Cm,post (p. 14, l. 436). The trace of Eq. 22 is not this ratio. (2) Names: the map quantity of Eq. 22 is called "normalised posterior covariance" (Fig. 5 and 6, panels f and captions), "normalised posterior variance" (p. 10, l. 303) and "Normalised posterior uncertainty" (Fig. 14 to 16): 3 names. The scalar is called "Normalised covariance trace" (Fig. 5 and 6, panel h), "normalised posterior covariance during non-linear iterations" (captions of Fig. 5 and 6), "posterior covariance" (p. 10, l. 306; p. 11, l. 316), "Posterior uncertainty" (panel titles of Fig. 7 to 9), "normalized posterior uncertainty" (p. 11, l. 335; p. 15, l. 441 and l. 446), "posterior uncertainty" (p. 12, l. 352 and l. 361), "Normalised posterior uncertainty" (Fig. 10), "total normalized uncertainty" (p. 14, l. 436) and "Total normalised posterior uncertainty" (Fig. 14 to 16): 9 names (count over the whole manuscript, basis page images and `text.json`, places listed). The axis labels "Trace(post. cov.)" (Fig. 7 to 9) and "Trace(post.covar.)" (Fig. 10) read as an unnormalised trace, which would be a sum over all pixels, while the plotted values of 0.73 to 0.96 can only be normalised. That all scalar names denote one quantity is inferred from the common value range (about 0.74 for the baseline in Fig. 5h, 7, 8, 9 and 10). (3) Resolution: for a linearised Gaussian inversion the trace of R cannot exceed the rank of G, here at most 7 because the pixels of one unit share one fingerprint; with n pixels the mean of diag(R) is therefore at most 7/n, for example 7/837 = 0.0084 for about 837 pixels (catchment of about 75 km2 measured on the scale bar of Fig. 4, pixels of 300 m; Python). Fig. 5d shows most pixels at the dark end of a scale from 0.90 to 1.00, and the resolution panel of Fig. 14 shows the zircon case almost entirely at the dark end (1.0) of a 0.5 to 1.0 scale, while the text calls this case "low resolution" (p. 14, l. 436). Is a different quantity plotted (for example 1 minus diag(R)), or is the colour scale inverted? The comparison of 0.87, 0.82 and 0.86 is an argument for combining XRD and zircon data (GB-46), so a reader must know which formula produced these numbers. KK-11 concerns the spelling "considerately" in the quoted sentence; GB-29 the units of the error axes in the same figures. |
| Suggestion | In Sect. 3.3 give the exact formula of every plotted metric (R or 1 minus R; variances or standard deviations; element-wise or trace ratio), define one name and one symbol for the map quantity and one for the scalar (for example "normalised posterior standard deviation" for Eq. 22 and "total normalised posterior variance, tr(C̃m)/tr(Cm)"), use C̃m throughout, and align the panel titles, axis labels and colour bars of Fig. 5 to 10 and 14 to 16 and the text at p. 10, l. 303 and l. 306, p. 11, l. 316 and l. 335, p. 12, l. 352 and l. 361, p. 14, l. 436 and p. 15, l. 441 and l. 446. |
| Status | verified (formulas, names, labels and colour scales on the page images p. 8, 10 to 15, 26 to 31, 35 to 37); inferred (identity of the scalar across figures; rank bound; pixel number) |
| Severity | moderate |
| Source | S2, S3, SD, AB |

**GB-16 Instrument and software settings that determine the XRD fingerprints are not reported.**

| Field | Content |
|---|---|
| Check | P35 |
| Location | p. 9, l. 252 to 258; p. 13, l. 396 to 397 |
| Quotation | "Secondly, these samples are then powdered and analysed using XRD producing one diffractogram per sample" |
| Concern | Search in `text.json`, p. 1 to 16: "diffractometer", "Cu K", "kV", "scan", "software" 0 hits; "WinXRD" 2 hits (p. 9, l. 254; p. 15, l. 473), both without version or settings. Not stated are: diffractometer, radiation, 2θ range, step width, counting time, grinding method and grain size after powdering, sample mounting, the WinXRD version and Peak Finder thresholds, the language and version of the inversion code, and the dates of the XRD analyses. These settings determine the peak areas and therefore A and d. |
| Suggestion | Add an instrument and software paragraph to Sect. 3.4 with these items, and name the Zenodo record version and the code language. |
| Status | verified (search as stated) |
| Severity | moderate |
| Source | SD |

**GB-17 Several steps of the XRD processing chain and of the construction of the synthetic tests cannot be rebuilt from the text.**

| Field | Content |
|---|---|
| Check | P8 |
| Location | p. 9, l. 257 to 260; p. 10, l. 293 to 294; p. 12, l. 343 to 344; p. 12, l. 355 to 357; p. 15, l. 443 to 445 |
| Quotation | "In a fifth step, diagnostic 2θ windows for each mineral are selected from RRUFF database reference spectra" (p. 9, l. 257 to 258); p. 9, l. 259 to 260: "Sixth, to mitigate peak overlap, we average the total peak area within the 2θ windows corresponding to each mineral" |
| Concern | Named but not specified are: the 2θ windows of the 21 minerals (no list); what "average the total peak area" means (sum or mean, over how many windows); how several source samples of a unit are combined into one fingerprint; how the synthetic fingerprints of Fig. 5k were generated (p. 10, l. 293 to 294); how the "minimal changes" map of scenario 1 was derived (p. 11, l. 332 to 333); the blending formula and the 20 blending levels (p. 12, l. 343 to 344 and l. 348 to 349); how a principal component analysis, which yields components, selects individual tracers (p. 12, l. 355 to 357); how the two data blocks are weighted when concatenated (p. 15, l. 443 to 445). Search in `text.json`, p. 1 to 16: "blend" 3 hits (p. 12, l. 343 and two in l. 348), none with a formula; "PCA" or "principal comp" 2 hits (p. 12, l. 355 and l. 356), none with a selection rule. GB-16 concerns the instrument settings of the preceding steps, GB-48 the hatching criterion, GB-40 the merging rule of Fig. 13. |
| Suggestion | Add a methods table or appendix listing the 2θ windows and Peak Finder settings, the aggregation rule per unit, the generation of the synthetic fingerprints and maps, the blending formula with all 20 levels, the PCA selection rule and the data weighting of the combined run. |
| Status | verified (search and reading) |
| Severity | moderate |
| Source | SD |

**GB-18 Normalising each sample by its own maximum peak area breaks the linear mixing assumed in Eq. 1, so erosion can be shifted between units.**

| Field | Content |
|---|---|
| Check | P26 |
| Location | p. 9, l. 259 to 264; p. 5, l. 150 to 152 |
| Quotation | "these are normalized within each sample by dividing by the maximum observed peak area, yielding relative mineral concentrations on a scale from 0 to 1" (p. 9, l. 261 to 262); p. 9, l. 263 to 264: "This approach allows for consistent comparison across both source and detrital samples while minimizing the influence of absolute intensity differences" |
| Concern | Eq. 1 treats the detrital data as an erosion-weighted average of the source fingerprints ("the detrital data are a weighted average of the tracer mineral concentrations, with the weights being the erosion rates", p. 5, l. 151 to 152). If the peak areas P mix linearly, a detrital sample has Pmix = sum over j of wj Pj. After the normalisation of p. 9, l. 261 to 262, Aj = Pj / max(Pj) and d = Pmix / max(Pmix), so d is proportional to the sum over j of wj max(Pj) Aj: the weights recovered by the inversion are the erosion weights multiplied by each unit's maximum peak area. These maxima belong to different minerals in different units (Fig. 11: antigorite in the serpentinites, quartz in the ZSF sediments, MR granite, MR gneiss and Furgg series, anorthite and pyroxene in S.,T.,G. and the metabasites), and their absolute values are not reported. Unless they are equal, erosion is shifted between units by their ratios. The stated guarantee (p. 9, l. 263 to 264) holds for an overall intensity scale, not for this path. Do the absolute maximum peak areas of the source samples differ, and by how much? GB-17 concerns the averaging step before the normalisation. Graded major because it affects every natural-data erosion rate if it holds. |
| Suggestion | State in Sect. 3.4 the absolute maximum peak areas of the source samples, and either normalise all samples by a common reference (internal standard or total peak area) or include the factors max(Pj) in A; show in a synthetic test with the measured fingerprints how large the resulting bias is. |
| Status | inferred (algebra on the procedure stated at p. 9, l. 259 to 262 and Eq. 1; normalising minerals read from Fig. 11 on page image p. 32) |
| Severity | major |
| Source | SD |

**GB-19 The geological map that defines the tracer matrix is partly expert-inferred, and its sources are credited only inside Fig. 4.**

| Field | Content |
|---|---|
| Check | P12, P19 |
| Location | p. 9, l. 270 to 272; Fig. 4, credit block and legend; p. 11, l. 332 to 334; p. 16, l. 490 |
| Quotation | "In ice-covered regions, where direct geological mapping is not possible, we infer the lithology based on regional geological knowledge." (p. 9, l. 270 to 271); "Land cover data: SwissTopo 2018"; Fig. 4, credit block: "Geological data: data from Steck et al., 2015, personal communication by L. Baumgartner, outcrops by GeoCover" |
| Concern | Fig. 4 openly credits its data, which helps. The inferred map is, however, an input of every inversion: the tracer matrix A is built from it (p. 14, l. 408). According to the credit block it rests on Steck et al. (2015), a personal communication and GeoCover outcrop data; the land cover comes from SwissTopo 2018; the "Glacier outline" and the "ELA estimation" of the inset legend carry no source. Search in `text.json`, all 37 pages including the reference list, for "SwissTopo", "GeoCover" and "personal comm": 0 hits; the credits exist only as raster text of Fig. 4 (page image p. 25). The share of inferred area and the relation to Steck et al. (2015) are not stated in the text: scenario 1 uses "the map proposed by (Steck et al., 2015)" as the map "with the biggest area mismatch" (p. 11, l. 333 to 334) without saying that the map used is a modification of it, and only three maps are tested (Fig. 7, three markers), so the uncertainty of the inferred map is not propagated into the natural results. The data statement (p. 16, l. 490) does not say whether the inferred map is archived. GB-20 treats the unit names in the same legend, GB-62 the condition of a well-constrained lithology. |
| Suggestion | Add SwissTopo (product and version of 2018) and GeoCover (sheet or dataset) to the reference list; name the sources of glacier outline and ELA estimate in the caption of Fig. 4; state in Sect. 4 (p. 9, l. 270 to 272) which map parts rest on the personal communication, the inferred share of the catchment and the differences to Steck et al. (2015); invert the natural data also with the Steck et al. map and report the change; state in the data statement whether the inferred map is archived. |
| Status | verified (text, credit block, search, marker count on the page images p. 25 and 28) |
| Severity | moderate |
| Source | S2, SD |

**GB-20 The lithological units are named differently in text, captions and legends, and the abbreviations ZSF, MR and S.,T.,G. are used before or without being introduced.**

| Field | Content |
|---|---|
| Check | P29, P38 |
| Location | p. 9, l. 273 to p. 10, l. 276; p. 10, l. 299; p. 12, l. 340; p. 14, l. 411; p. 14, l. 414; p. 14, l. 431 to 434; Fig. 4, legend; Fig. 5, panel (j) legend; Fig. 11, caption; Fig. 12, legend and caption; Fig. 13, curve labels; Fig. 15 and Fig. 16, legend |
| Quotation | "the Monte Rosa garnet-gneiss (MR g-g) unit" (p. 14, l. 432); "Monte Rosa (garnet gneiss and micaschist)" (Fig. 4, Fig. 12); "Monte Rosa (gneiss, micaschist)" (Fig. 11, Fig. 13); "MR gneiss, mica" (Fig. 5j, 15, 16); "Stockhorn-Turftgrat-Gornergrat" (Fig. 11); "S.,T.,G." (Fig. 5j, 15, 16); Fig. 11: "ZSF ophiolites (metabasites, ecologites)" |
| Concern | Fig. 4 gives a complete legend with seven units, which allows each name to be mapped. Against it: (1) the Monte Rosa gneiss unit carries four names (Fig. 4 and 12; p. 14, l. 432 to 433; Fig. 11 and 13; Fig. 5j, 15 and 16); "MR g-g" is used nowhere else. (2) The Stockhorn unit carries four names ("The Stockhorn, Tuftgrat, and Gornergrat units", p. 10, l. 276; "Stockhorn basement, Tuftgrat Mesozoic and GornergratPermo-Mesozoic", Fig. 4 and 12; "Stockhorn-Turftgrat-Gornergrat", Fig. 11, with "Turftgrat" misspelt; "S.,T.,G.", Fig. 5j, 15, 16); "S.,T.,G." is never spelled out. (3) The ZSF sediments are introduced in the geology description only as "Penninic Mesozoic sedimentary units (Bündnerschiefer)" (p. 10, l. 274 to 275); "Zermatt Saas-Fee sediments" first appears at p. 10, l. 299. (4) The unit name is spelled in five ways: "Zermatt Saas-Fee" (p. 10, l. 299), "Zermatt-Saas-Fee" (p. 12, l. 340), "Zermatt - Saas Fee" (p. 14, l. 411 and l. 414; Fig. 4 and Fig. 12 legends), "Zermatt-Saas Fee" (p. 9, l. 273 to p. 10, l. 274; p. 14, l. 431 and l. 432), "Zermatt- Saas Fee" (Fig. 12 caption); compared character by character on the page images p. 9, 10, 12, 14, 25 and 33. (5) "ZSF" is used in Fig. 5j and Fig. 11, cited at p. 10, l. 299 and p. 13, l. 398, but introduced only at p. 14, l. 431; "MR" only at p. 14, l. 432; no caption expands ZSF, MR or S.,T.,G. (6) The Fig. 11 caption writes "ecologites" for eclogites (p. 10, l. 274; p. 14, l. 431). Search basis: `text.json`, all pages, for "Zermatt", "Saas", "ZSF", "Monte R", "MR ", "Stockhorn", "Tuftgrat", "Turftgrat", "S.,T", "eclog", "ecolog", plus the page images of Fig. 4, 5 and 11 to 16. GB-19 concerns the data credits in the same Fig. 4 legend; KK-14 the glacier name, KK-22 the subcatchment name in the same captions. |
| Suggestion | Define each unit once in Sect. 4 (p. 9, l. 273 to p. 10, l. 279) with its full name and abbreviation (ZSF, MR, STG), state there that the ZSF sediments are the Bündnerschiefer, and use exactly these names and one spelling ("Zermatt-Saas Fee") in the text (p. 10, l. 299; p. 12, l. 340; p. 14, l. 411, l. 414 and l. 431 to 434), in the captions of Fig. 5 and 11 to 13 and in the legends of Fig. 4, 5j, 12, 15 and 16; correct "Turftgrat" to "Tuftgrat" and "ecologites" to "eclogites" in the caption of Fig. 11. |
| Status | verified |
| Severity | minor |
| Source | S2, AB, S3, S4 |

**GB-21 Symbols in the schematic Figures 1 to 3 are not explained.**

| Field | Content |
|---|---|
| Check | P29 |
| Location | Fig. 1, panels (b) and (d); Fig. 2, panels (b) and (c); Fig. 3, panel (b) |
| Quotation | "(b) geology and fingerprints of every lithology" (Fig. 1 caption); Fig. 2c legend: "tracer concentration low high" |
| Concern | The schematics are clear in their sequence, and the captions explain each panel. Three graphical elements have no legend entry and no explanation: the black arrowhead next to the map in Fig. 1b, 2b and 3b (north arrow or flow direction?); the dark grey segments between the lithology colours in the sample cylinder of Fig. 1d; and in Fig. 2c the "low to high" scale is given only for the green layer, while the magenta, orange and blue layers have none. Checked at 150 and 300 dpi. |
| Suggestion | Add the arrow symbol and the grey cylinder segments to the legends of Fig. 1 to 3 or name them in the captions; state in the caption of Fig. 2 that each tracer layer has its own low to high colour scale. |
| Status | verified |
| Severity | minor |
| Source | AB |

**GB-22 The caption of Fig. 4 names three topics without explaining the panels, and "ELA" is not expanded.**

| Field | Content |
|---|---|
| Check | P29 |
| Location | Fig. 4, caption, land cover inset and inset legend |
| Quotation | "Figure 4. Study area: location, land cover and geology." |
| Concern | The geological legend of Fig. 4 is detailed and the location inset carries graticule labels. The caption, however, does not say which part shows what (main map: inferred geology and outcrops; upper inset: land cover with glacier outline and "ELA estimation"; lower insets: location). "ELA" appears only in the inset legend: search in `text.json`, all 37 pages, for "ELA" (case-sensitive) and "equilibrium": 0 hits, and Fig. 4 is a raster image, so the term is defined nowhere a reader can find it. The land cover inset has no scale bar of its own. GB-19 concerns the missing sources of the same inset; GB-20 the unit names of the legend. |
| Suggestion | Rewrite the caption to name the parts and how to read them, expand "ELA" (equilibrium line altitude, if that is meant), and add a scale to the land cover inset or state that it has the scale of the main map. |
| Status | verified |
| Severity | minor |
| Source | AB |

**GB-23 Two pairs of legend colours in Fig. 4 and Fig. 12 cannot be told apart.**

| Field | Content |
|---|---|
| Check | P3 |
| Location | Fig. 4, legend; Fig. 12, legend |
| Quotation | "Stockhorn basement, Tuftgrat Mesozoic and GornergratPermo-Mesozoic"; "Outcrops: garnet-bearing silimanite-biotite gneiss"; "Outcrops: garnet mica & muscovite schist" |
| Concern | Measured legend fields (300 dpi for Fig. 4, 600 dpi for Fig. 12, identical in both): Stockhorn unit #fc7434, Monte Rosa gneiss outcrops #fc5c34, Stockhorn outcrops #fc3434. Sum of RGB differences: Stockhorn unit against Monte Rosa gneiss outcrops 0 + 24 + 0 = 24; Stockhorn outcrops against Monte Rosa gneiss outcrops 0 + 40 + 0 = 40. Both pairs lie at or below the threshold of 40, so a reader cannot assign these map colours to one legend field, the more so as the map is shaded by a hillshade. GB-19, GB-20 and GB-22 concern other parts of the Fig. 4 legend and caption. |
| Suggestion | Give the Monte Rosa gneiss outcrops a colour or hatching clearly distinct from both Stockhorn fields in Fig. 4 and 12. |
| Status | verified |
| Severity | minor |
| Source | AB |

#### Minor corrections

| ID | Location | Quotation | Replacement | Source |
|---|---|---|---|---|
| KK-05 | p. 5, l. 146; p. 5, l. 148; p. 5, l. 149; p. 6, l. 166; p. 6, l. 167; p. 9, l. 252; p. 9, l. 258; p. 9, l. 262; p. 10, l. 289 to 306; p. 11, l. 307 to 319 | "(Figure 1B)"; "(Figure 5K)"; "(Figure 6D, 6E and 6F )" | lower-case panel letters as printed in the figures and captions, "(Figure 1b)", "(Figure 5k)", and "(Figure 6d, 6e and 6f)" without the space before the closing parenthesis (p. 11, l. 319) Overlapping locations: GB-11 treats the placement of disclosed limits, GB-16 treats the missing instrument settings, GB-17 treats the unspecified processing and test-construction steps, GB-18 treats the per-sample normalisation; this entry concerns the letter case of panel references. | AB, S3, S4 |
| KK-06 | p. 6, l. 175 to 176; p. 6, l. 184 | Eq. 5: "p (εm ∣dobs ) p (dobs ∣εm ) ·" without relation sign; "Where p (ε∣dobs ) is the posterior"; "ϕprior (εm ) = (ε − εprior )" | Eq. 5 with a proportionality or equality sign between the posterior and the likelihood term; "Where p(εm∣dobs) is the posterior"; "ϕprior(εm) = (εm − εprior)T Cm^-1 (εm − εprior)", symbol εm as in Eq. 5 to 7 (missing sign confirmed on page image p. 6) | S2, ZF |
| KK-07 | p. 6, l. 181 | "becomes Tarantola (2005):" | "becomes (Tarantola, 2005):"; line counted on page image p. 6 from margin number 180 | S4 |
| KK-08 | p. 7, l. 189 (Eq. 9) | "Cm(i, j) = σm² exp(si,j² / L²)" (as printed) | "Cm(i, j) = σm² exp(−si,j² / L²)"; the page image p. 7 shows no minus sign, so the covariance as printed would grow with distance | SD |
| KK-09 | p. 7, l. 201 (Eq. 14) | "∇ε ϕd = GC−1 d (dε − dobs )" | "∇ε ϕd = GT Cd^-1 (dε − dobs)", with the transpose that Eq. 16 has (p. 7, l. 205); confirmed on page image p. 7 | ZF |
| KK-10 | p. 8, l. 215 (Eq. 18); p. 8, l. 219 (Eq. 19) | "(εk − εprior )" | "(εn − εprior)" in both equations, iteration index n as on the left side and at p. 8, l. 216. GB-12 concerns the matrix inverse in Eq. 19. | S2, SD |
| KK-11 | p. 8, l. 236 | "considerately" | "considerably". GB-15 concerns the content of this sentence. | S4 |
| KK-12 | p. 9, l. 245 | "weighed by the model covariance" | "weighted by the model covariance" | S4 |
| KK-13 | p. 9, l. 251 to 252 | "in-situ source samples are collected from every lithological unit across the study area (Figure 3A and 3B)" | "(Figure 3b)"; panel (a) shows the detrital pump sampling. GB-16 concerns the analysis steps that follow in the same paragraph. Overlapping locations: KK-05 treats the letter case of panel references; this entry concerns the panel reference to Fig. 3. | AB |
| KK-14 | p. 9, l. 267; p. 9, l. 272; p. 10, l. 282; p. 13, l. 392; p. 13, l. 400; p. 15, l. 463; p. 16, l. 498; p. 16, l. 499; Fig. 5, panel (j) legend; Fig. 11, caption; Fig. 15 and Fig. 16, legend | "Gorner-gletscher" (p. 9, l. 267; Fig. 11); "Gornergletscher" (p. 9, l. 272; p. 10, l. 282); "Gorner Glacier" (p. 13, l. 392 and l. 400; p. 16, l. 498 and l. 499); "Gorner gletscher" (p. 15, l. 463); "Gorner glacier" (Fig. 5j, 15, 16) | one name at all 12 places, for example "Gorner Glacier"; 5 forms at 12 places, whole manuscript, basis `text.json` and page images of Fig. 5, 11, 15, 16 (Python: 2 + 2 + 4 + 1 + 3 = 12). GB-20 concerns the unit names in the same caption and legends. Overlapping locations: GB-15 treats the definitions and names of the uncertainty metrics, GB-19 treats the provenance of the geological map; this entry concerns the name of the glacier. | S2, S3, S4 |
| KK-15 | Fig. 3, panel (c), legend | "quarz pattern alignment" | "quartz pattern alignment" | AB |
| KK-16 | Fig. 4, legend; Fig. 12, legend | "caclcite-zoisite amphibolites"; "biotite schits"; "garnet-bearing silimanite-biotite gneiss"; "GornergratPermo-Mesozoic"; "calcarious mica schist" | "calcite-zoisite amphibolites"; "biotite schists"; "garnet-bearing sillimanite-biotite gneiss"; "Gornergrat Permo-Mesozoic"; "calcareous mica schist"; compared on page images p. 25 and 33. GB-19, GB-20, GB-22 and GB-23 concern sources, names, caption and colours of the same legend. | AB |

#### Verification log

| ID | Check | Checked | Values | Result |
|---|---|---|---|---|
| PP-05 | P9 | Design sketch of the whole manuscript (questions, data sources, time axis, environment, components, disclosed limits, chain from aim to result) | Aims at p. 1, l. 3 to 4, p. 2, l. 41 to 42, p. 3, l. 63 to 64; operational aims p. 10, l. 280 to 285; no numbered research questions; one hypothesis (p. 14, l. 410 to 411); 7 source units, 21 tracers, one synthetic true map; data sources: synthetic data, inferred geological map, XRD of source and detrital samples, zircon ages from an unpublished thesis, export estimate and natural prior not stated | sketch used for GB-01, GB-11, GB-24, GB-43, GB-44 and GB-62 |
| PP-06 | P12 | Data sources of Sect. 3 and 4 covered by the statement at p. 16, l. 490 | Covered by "data and codes used for the inversion tests": synthetic true map and fingerprints (p. 10, l. 288 to 289; Fig. 5k), synthetic detrital data, blended and reduced fingerprint sets, modified maps of scenario 1, binned source fingerprints and detrital vectors of Sect. 4.2, inversion code ("F.D.D. developed all code", p. 16, l. 492) | no finding for these sources; the manuscript names its data link openly; uncovered sources in GB-19, GB-43 and GB-66 |
| PP-07 | P12 | Appendices and supplements inside the manuscript | `text.json`, all 37 pages: "appendix" 0 hits, "supplement" 0 hits, "table" 10 hits, all inside "stable" or "unstable" | no finding; no data source is made accessible inside the manuscript |
| PP-08 | P12 | Reachability of the data link | https://doi.org/10.5281/zenodo.17120374 (p. 16, l. 490): WebFetch refused by the proxy (HTTP 429), not retried; web search "zenodo 17120374": no record page | link present; contents and reachability not checked (named under Limits of this review) |
| PP-09 | P38 | Names that could denote one or two objects | "inversion framework validated in (De Doncker et al., 2020)" (p. 2, l. 61) against the own "non-linear adaptation": two objects, named as such; "Belotti, B." (p. 17, l. 522) and co-author Bruno Belotti (title block): one person; "Peak Finder algorithm" (p. 13, l. 396) as short form of "WinXRD Peak Finder algorithm" (p. 9, l. 254): one object | no finding |
| PP-10 | P4 | Section and equation numbering and equation references | Sections 1 to 6 with 3.1 to 3.4 and 4.1 to 4.2.2; equations (1) to (22) without gap; references "eq. 1-4" (p. 9, l. 263), "eq. 7" (p. 7, l. 191; p. 8, l. 240; p. 9, l. 245), "eq. 12 and eq. 13 into eq. 11" (p. 7, l. 200), "eq. 14 and eq. 15 in eq. 10" (p. 7, l. 204), "eq. 16" (p. 8, l. 213 and l. 217) point to the matching equations; no section cross-references in the text | no finding except the doubled Introduction (GB-04) |
| PP-11 | P1, P38 | Pixel size implied by the smoothing distances | "4 times the pixel size (L = 1200 m)" (p. 10, l. 294; p. 11, l. 325; p. 14, l. 427): 1200/4 = 300.0 m; "10 times the pixel size (3000 m)" (p. 12, l. 373): 3000/10 = 300.0 m (Python) | consistent; the pixel size is stated only implicitly (part of GB-29) |
| PP-12 | P7 | Collection window against method versions | XRD analysis dates not stated; one detrital sample dated 28 June 2019, others undated; synthetic runs undated; one protocol change (SD normalisation, p. 11, l. 312) without date | no finding of its own; shares per method version cannot be computed; dates of the analyses in GB-16 |
| PP-13 | P30 | Reported errors and their correction against the reported runs | errors reported: SD instability (p. 11, l. 312), missing zircon data (p. 14, l. 430 to 434); no dated corrections; Fig. 6 described as after normalisation | no finding |
| PP-14 | P27 | Unchecked components and where their output flows | inferred geology under ice flows into A of all natural runs (GB-19); copied MR g-g zircon fingerprint flows into Fig. 14 and 16 and the zircon comparison (GB-44, GB-55); PCA tracer selection affects only scenario 3 (GB-17); hatching criterion affects display only (GB-48) | no finding of its own |
| PP-15 | P35 | Numerical settings of the inversion runs | QN test: 100 iterations, L = 1200 m, σm = 3, σd = 0.01 mm/y, prior equal to the mean of the truth, step size not stated (p. 10, l. 293 to 295); degradation and natural runs: 25 iterations, step size 0.1, same L, σm, σd (p. 11, l. 324 to 326; p. 14, l. 426 to 428); SD iterations not stated (Fig. 6 axis to 200) | missing values raised in GB-26 and GB-16 |
| PP-16 | P17 | Disclosed limits placed at their method | inferred lithology (p. 9, l. 270 to 272) stated in the study-area paragraph where the map is introduced | no finding for this limit; others in GB-11 |
| PP-17 | P3, P4, P29 | Figure inventory, numbering, order of first reference, panel references against captions | 16 figures on p. 22 to 37, one per page, no graphical abstract, no tables; first references: Fig. 1 p. 5, l. 146; Fig. 2 p. 6, l. 166; Fig. 3 p. 9, l. 251; Fig. 4 p. 9, l. 268; Fig. 5 p. 10, l. 289; Fig. 6 p. 11, l. 314 to 315; Fig. 7 l. 334; Fig. 8 p. 12, l. 347; Fig. 9 l. 356 to 357; Fig. 10 l. 371; Fig. 11 p. 13, l. 398; Fig. 12 p. 14, l. 412; Fig. 13 l. 414; Fig. 14 l. 429; Fig. 15 l. 438; Fig. 16 p. 15, l. 445 (ascending, no gap); panel references 1A to 1D, 2A to 2C, 3A to 3E, 5A to 5K, 6C to 6F against captions with panels (a) to (k) and (a) to (i) | no finding except the self-reference at p. 11, l. 317 (GB-27), the panel at p. 9, l. 251 to 252 (KK-13) and the letter case (KK-05) |
| PP-18 | P29 | Smallest text of each figure, cap height at 600 dpi | Fig. 4 legend 6.83 pt, credits 6.33 pt; Fig. 5 ticks 6.33 pt, legend 6.17 pt; Fig. 7 ticks 5.83 pt; Fig. 8 axis label 6.50 pt; Fig. 9 ticks 5.83 pt; Fig. 11 labels 7.00 pt; Fig. 13 ticks 6.17 pt; Fig. 14 colour bar 5.50 pt, bin labels 5.33 to 5.50 pt; Fig. 15 colour bar 5.50 pt, legend 6.50 pt (method tolerance 0.6 pt) | within tolerance of 6 pt or above: no finding; Fig. 10 and 16 in GB-51 |
| PP-19 | P3 | Catchment width from the scale bars of Fig. 4, 12, 14, 15, 16 | 13.18 km, 13.14 km, 13.39 km, 13.32 km, 13.34 km (scale bar uncertainty 0.9 % to 1.2 %) | differences up to 1.9 %, within the uncertainty: no finding |

### Segment 3: Results of the synthetic and natural tests (p. 10 to 15; Fig. 5 to 16)

#### Substantive findings

**GB-24 The synthetic validation inverts noise-free data made with the same forward model, a prior taken from the truth and a single map shape, so its convergence and robustness claims do not transfer to real data.**

| Field | Content |
|---|---|
| Check | P9 |
| Location | p. 10, l. 288 to 295; p. 11, l. 324 to 326; p. 12, l. 360; p. 16, l. 482 to 483 |
| Quotation | "we generate synthetic detrital data using the forward model applied to a “true” erosion rate map featuring a localised hotspot" (p. 10, l. 288 to 289); "a prior equal to the average true erosion rate" (p. 10, l. 295); p. 16, l. 482 to 483: "we show that the true erosion pattern can be reliably recovered, and that the method is robust across a range of parameters" |
| Concern | The forward-inverse tests are documented with all metrics and show the expected trade-offs. Their design has four features that favour the inversion. (1) Data are generated and inverted with the same forward model and, outside scenario 1, the same tracer matrix, and no measurement noise is added: search in `text.json`, p. 1 to 16, for "noise": 1 hit (p. 9, l. 255, XRD background). This is what Wirgin (2004) calls the inverse crime, the use of the same or nearly the same theoretical ingredients to synthesise and to invert data. A sign of it is the third row of Fig. 10, in which the total absolute difference varies by about 0.012 % over the whole σd sweep (GB-35). (2) The prior equals the mean of the truth (p. 10, l. 295; p. 11, l. 325 to 326), so the inversion is given the correct mean erosion rate. (3) All synthetic tests use one "true" map with one smooth hotspot (Fig. 5a and 6a identical); the hyperparameter sweep then favours the largest smoothing distance tested (GB-34), which describes the shape of this map rather than erosion patterns in general, and p. 12, l. 340 to 341 explains the scenario 1 result by the position of "the true erosion-rate bump". (4) With 7 source units and one fingerprint per unit, the Jacobian has at most 7 linearly independent columns; that 7 tracers give "approximately the same posterior solution as with the full tracer set" (p. 12, l. 360) is consistent with this rank bound and with the absence of noise, and does not show that XRD tracers beyond 7 are redundant in practice (see GB-37 and GB-60). Graded major because the synthetic tests are the main evidence for convergence and robustness (p. 1, l. 7; p. 16, l. 482 to 483); if the concern holds, these statements are limited to noise-free data with a correct prior mean and one map shape. Overlapping locations: GB-13 treats the Gaussian approximation, GB-14 treats the scope of the error propagation, GB-17 treats the unspecified processing and test-construction steps, KK-05 treats the letter case of panel references; this entry concerns the design of the synthetic validation. |
| Suggestion | Add to Sect. 4.1 a test set that (a) perturbs the synthetic detrital data and fingerprints with noise of the size of XRD replicate scatter, (b) uses a prior not taken from the truth (for example from the export estimate alone, or biased by a factor of 2), (c) uses an ensemble of true maps (several hotspots, random positions, broad and narrow features, uniform erosion) and (d) generates data on a finer or perturbed source map than the one inverted; report error and coverage of the posterior uncertainty over the ensemble, and restate p. 1, l. 7 and p. 16, l. 482 to 483 on that basis. Literature: Wirgin, A. (2004) The inverse crime. arXiv:math-ph/0401050. Available at: https://arxiv.org/abs/math-ph/0401050 (not in the reference list). |
| Status | verified for the design features (1) to (3) (text and page images); inferred for the rank argument (4); Wirgin (2004) read as abstract at https://arxiv.org/abs/math-ph/0401050 (v1) |
| Severity | major |
| Source | SD |

**GB-25 The QN posterior is said to match the true map in magnitude, while the difference map shows a deviation of about 2 at the hotspot that the posterior map cannot display.**

| Field | Content |
|---|---|
| Check | P36 |
| Location | p. 10, l. 296 to 298; Fig. 5, panels (a) to (c) |
| Quotation | "The quasi-Newton (QN) approach generates a posterior erosion rate map that closely matches the true erosion pattern, both in spatial distribution and magnitude (Figure 5B)." |
| Concern | The colour bar of Fig. 5c ("Difference (true - posterior)") runs from about -2 to 2, and the cells at the hotspot are at its dark-blue end, about -2, i.e. the posterior exceeds the true rate there by about 2, where the true map reaches about 3 (colour bar of Fig. 5a ends at 3.0). The colour bar of the posterior map, Fig. 5b, also ends at 3.0, so the overshoot is not visible there. The next sentence places the "primary differences" within the larger lithological units (p. 10, l. 297 to 298), while the largest difference in Fig. 5c lies at the hotspot. The values were read from the colour scales on the page image p. 26, not measured. GB-26 compares the same panel with the SD result. Overlapping locations: GB-15 treats the definitions and names of the uncertainty metrics, KK-05 treats the letter case of panel references, KK-14 treats the name of the glacier; this entry concerns the hotspot overshoot in Fig. 5. |
| Suggestion | Report the maximum and mean difference between true and posterior map in Sect. 4.1.1, extend the colour bar of Fig. 5b to the posterior maximum, and rephrase p. 10, l. 296 to 298 to these values. |
| Status | verified (colour scales and wording on page images p. 10 and 26); inferred (size of the overshoot, read from the colour scale) |
| Severity | moderate |
| Source | SD |

**GB-26 The comparison of steepest descent and quasi-Newton uses unequal and partly unreported settings, and the plotted errors do not show that QN is more accurate.**

| Field | Content |
|---|---|
| Check | P2, P3, P9, P11 |
| Location | p. 11, l. 312 to 321; p. 10, l. 293 to 295; Fig. 5, panels (c) and (g); Fig. 6, panels (c) and (g) |
| Quotation | "more iterations are needed to converge to a posterior result as close to the true erosion rate map as the QN posterior" (p. 11, l. 315 to 316); p. 11, l. 320 to 321: "we adopt the Quasi-Newton (QN) approach for all subsequent tests, as it provides a more stable and accurate reconstruction of the erosion rate patterns." |
| Concern | The comparison is well set up (same synthetic data, same metrics, identical figure layout), and comparing the two schemes is an aim of the Abstract (p. 1, l. 4 to 5). Three instances measured Fig. 5g and 6g independently at 300 dpi (y axes calibrated on the ticks, resolution about 0.3 to 1.2 units): QN starts at about 348, reaches its minimum of about 197.0 to 197.4 near iteration 22 and ends at 200.4 to 201.1 after 100 iterations; SD stands at 211.3 after 100 iterations and ends at 193.0 to 193.2 after 200 iterations. At equal iteration count QN is closer to the truth (about 201 against 211.3), which supports "more iterations are needed". At the end of the shown runs, however, SD is closer to the truth: (201.1 − 193.0)/201.1 = 4.0 % and (200.4 − 193.2)/200.4 = 3.6 % lower (Python); SD is also below the QN minimum. The difference maps agree: the colour scale of Fig. 5c (QN) reaches -2 at the hotspot, that of Fig. 6c (SD) -1.5. The manuscript gives no other accuracy measure, so "more accurate" is not shown by the figures it cites. In addition, the QN step size is not reported (p. 10, l. 293 to 295), the SD run has no reported settings (its 200 iterations can only be read from Fig. 6g), the gradient normalisation is not part of Eq. 18 (p. 11, l. 312), and neither run time nor cost per iteration is reported, so "faster convergence" (p. 8, l. 218) is not measured either. With one true map and one run per scheme, no difference can be separated from chance features of that map. S3 and AB graded moderate, SD major; the merged finding takes the higher grade because the choice of QN for all later results rests on this comparison. GB-03 concerns the convergence claim of the Abstract that includes this test; GB-25 the hotspot in Fig. 5c. Overlapping locations: GB-15 treats the definitions and names of the uncertainty metrics, KK-05 treats the letter case of panel references, KK-14 treats the name of the glacier; this entry concerns the comparison of SD and QN. |
| Suggestion | In Sect. 4.1.2 run both schemes to the same stopping criterion (p. 9, l. 243 to 244) and report iterations, wall-clock time, step sizes and final error for each; give the SD normalisation as an equation in Sect. 3.2; repeat on the ensemble of true maps proposed in GB-24; rephrase p. 11, l. 320 to 321 to what the figures support (faster convergence per iteration, stability), or add a measure under which QN is more accurate. |
| Status | verified (text on page images p. 10 and 11; values measured on Fig. 5g and 6g by three instances) |
| Severity | major |
| Source | S3, AB, SD |

**GB-27 The reference "(Figure 6G versus Figure 6G)" compares a panel with itself, and the oscillations it is meant to show are not visible at the stated iteration.**

| Field | Content |
|---|---|
| Check | P3, P4 |
| Location | p. 11, l. 316 to 317; Fig. 6, panel (h) |
| Quotation | "This limited sensitivity to strong gradients also leads to oscillations in the posterior covariance, visible after 125 iterations, as the Jacobian fluctuates between iterations (Figure 6G versus Figure 6G)." |
| Concern | The reference compares panel G with itself; the posterior covariance during the iterations is panel (h) in both captions (Fig. 5 and 6). In Fig. 6h (600 dpi, x axis calibrated on the ticks 0 and 200) the curve has a kink at 137 to 143 iterations, not at 125, and declines smoothly after it; the thickness of the marker band is 33 to 34 px before and 33 to 36 px after the kink, so no oscillation is resolved at print size. Is the oscillation meant to be read from another quantity or from a zoom that is not shown? GB-26 concerns the scheme comparison in the same paragraph. Overlapping locations: KK-05 treats the letter case of panel references; this entry concerns the panel reference and the oscillations in Fig. 6. |
| Suggestion | Correct the reference, for example to "(Figure 6h versus Figure 5h)", state the iteration of the kink as shown, and show the oscillation in an inset if it is used as an argument. |
| Status | verified |
| Severity | minor |
| Source | AB, S3, S4, SD |

**GB-28 The test cases and the measure of map mismatch in scenarios 1 to 3 have different names in text, captions and panels, and the x axis of Fig. 9 names the tracer count "Avg. JS distance between lithologies".**

| Field | Content |
|---|---|
| Check | P29, P38 |
| Location | p. 11, l. 330 to 335; p. 12, l. 347 to 348; Fig. 7, panel titles, x axes, colour bar and caption; Fig. 8, panel titles and caption; Fig. 9, x axes and colour bar of the left and middle scatterplot |
| Quotation | "quantified by area mismatch (expressed in m2)" (p. 11, l. 330); "Area difference" (Fig. 7, x axes); "Geology misalignment (m2)" (Fig. 7, colour bar); "Originial geology (same as forward)" (Fig. 7); "Almost fully blended (avg. JS = 0.225)" (Fig. 8); "Avg. JS distance between lithologies" (Fig. 9, x axes); Fig. 9, colour bar: "Number of tracrs" |
| Concern | Each scenario figure labels its three examples, which makes the link to the text possible. The names, however, differ: the mismatch measure has three names ("area mismatch", text; "area difference (m2)", caption, and "Area difference" without unit, axes; "Geology misalignment (m2)", colour bar); the maps of scenario 1 are "the same geological map", "Originial geology (same as forward)" and "Forward geology", and "a geological map with minimal difference", "Geology with minimal changes" and "Minimal changes"; the fingerprint sets of scenario 2 are "highly blended" and "intermediate" (p. 12, l. 348), "the most blended" and "the half-way in between" (caption), and "Almost fully blended" and "Medium blended" (panels). In Fig. 9 the x axes of the left and middle scatterplot carry the label of Fig. 8, "Avg. JS distance between lithologies", but their 21 markers lie at 1.001, 1.999, ... 20.97 (calibrated on the ticks 2.5 and 20.0), i.e. at the tracer counts 1 to 21 that the colour bar and p. 12, l. 357 to 358 describe; one quantity carries the name of another. Below the y label of the left scatterplot of Fig. 9 a stray second "Σ" is printed. Labels with spelling errors: "Originial" (Fig. 7), "tracrs" (Fig. 9). GB-29 concerns the error measure on the y axes of the same figures, GB-15 the uncertainty axes, GB-17 the construction of the test cases, GB-19 the relation of the scenario 1 map to Steck et al. (2015). Overlapping locations: KK-03 treats the form of narrative citations; this entry concerns the names of test cases and axes in Fig. 7 to 9. |
| Suggestion | Use one name for the mismatch measure, for example "area mismatch (m2)", in p. 11, l. 330 to 335 and in the caption, axes and colour bar of Fig. 7; use the text names of the examples in the panels and captions of Fig. 7 and 8 and correct "Originial" to "Original"; relabel the x axes of Fig. 9 "Number of tracer minerals", correct the colour bar to "Number of tracers" and remove the stray "Σ". |
| Status | verified (names and labels on the page images p. 11, 12, 28 to 30; marker positions measured) |
| Severity | minor |
| Source | S2, AB, S3 |

**GB-29 The accuracy measure of all synthetic tests is an unnormalised sum without unit over an unstated number of pixels.**

| Field | Content |
|---|---|
| Check | P20, P22, P29 |
| Location | p. 11, l. 334 to 335; p. 10, l. 294; p. 12, l. 373; Fig. 5, panels (a) to (c) and (g); Fig. 6, panels (a) to (c) and (g); Fig. 7 to Fig. 9, left scatterplots; Fig. 10, first column |
| Quotation | "as well as their impact on the absolute error, the normalized posterior uncertainty, and the trade-off between data- and model misfit" (p. 11, l. 334 to 335); y axis, Fig. 5g, 6g, 7 to 9: "Σ∣etrue - epost∣" |
| Concern | Every accuracy statement in Sect. 4.1 rests on the sum of absolute differences between true and posterior erosion rates, which the axes show as a sum over pixels (about 197 for the baseline, up to about 676 000 in Fig. 8). The manuscript states neither the number of pixels nor the catchment area: search in `text.json`, p. 1 to 16, for "pixel" and "pixels": 14 hits, none with a count. The pixel size is given only implicitly (300 m, PP-11). The axes carry no unit, nor do the colour bars of the erosion and difference maps in Fig. 5 and 6 (0.5 to 3.0 and about -2 to 2), while Fig. 14 to 16 give "(mm/y)" in their titles and the text gives this error in "mm/yr" (p. 12, l. 352). Without the pixel count a reader cannot tell whether 197 means a small or a large mean error relative to true erosion rates of about 0.3 to 3 mm/y (colour bar of Fig. 5a), nor convert the "700 mm/yr" of the text into the figure's scale (GB-32). Comparisons between scenarios on the same grid remain valid; the absolute size of the errors cannot be judged. GB-28 concerns the names of the x axes and test cases in the same figures, GB-15 the uncertainty axes. Overlapping locations: KK-03 treats the form of narrative citations, GB-19 treats the provenance of the geological map, KK-14 treats the name of the glacier, GB-24 treats the design of the synthetic validation, GB-25 treats the hotspot overshoot in Fig. 5, GB-26 treats the comparison of SD and QN; this entry concerns the unnormalised error measure. |
| Suggestion | State in Sect. 4.1.1 the pixel size (300 m) and the number of pixels; report the error also as mean absolute error per pixel or relative to the summed true erosion; add units to all erosion colour bars and error axes of Fig. 5 to 10. |
| Status | verified (search, axis labels and colour bars on page images p. 26 to 31); inferred (per-pixel interpretation) |
| Severity | moderate |
| Source | S3, AB |

**GB-30 Scenario 1 states a monotonic relation between map mismatch and posterior error that two of its three cases contradict.**

| Field | Content |
|---|---|
| Check | P2 |
| Location | p. 11, l. 337 to p. 12, l. 340; Fig. 7, left and middle scatterplot |
| Quotation | "We observe that the greater the mismatch between the geological map used in the inversion and the one used to generate the synthetic data, the larger the discrepancy between the posterior and true erosion rate maps. Surprisingly, a simplified geological map with minimal changes from the truth results in a more accurate posterior erosion map than the original geological map itself." |
| Concern | The authors report the exception openly and explain it (p. 12, l. 340 to 341). The general sentence is nevertheless not consistent with it. Scenario 1 has three cases ("Three geological cases", p. 11, l. 332; three markers in each panel of Fig. 7). Measured on Fig. 7 (300 dpi; about 0.17 error units and 0.00002 uncertainty units per pixel; two instances): area difference 0, 0.69 × 10^7 and 1.15 × 10^7 m2; summed absolute difference 197.3 to 197.4, 193.4 to 193.6 and 274.8; normalised uncertainty 0.7402, 0.7376 and 0.7460. Both metrics fall from the first to the second case and rise only in the third. With three cases, one of which reverses the direction, the data show no monotonic relation, only that the largest mismatch gives the largest error. The statement that both misfits increase "in all cases" (p. 12, l. 341 to 342) agrees with the trade-off panel (PP-25). GB-33 concerns the ranking across scenarios. Overlapping locations: GB-20 treats the names of the lithological units, GB-28 treats the names of test cases and axes in Fig. 7 to 9; this entry concerns the trend statement of scenario 1. |
| Suggestion | Rephrase p. 11, l. 337 to 338 to what the three cases show (only the largest mismatch, the Steck et al. 2015 map, increases error and uncertainty), or add intermediate maps to scenario 1 so that a trend can be stated. |
| Status | verified (text on page images p. 11 and 12; values measured on Fig. 7) |
| Severity | moderate |
| Source | S3, SD |

**GB-31 Scenario 2 reports 20 tested fingerprint sets, but Fig. 8 shows 14, and the caption accounts for one of the six missing runs.**

| Field | Content |
|---|---|
| Check | P3, P11, P23, P34 |
| Location | p. 12, l. 348 to 349; p. 12, l. 353; Fig. 8, all three scatterplots and caption |
| Quotation | "In total, 20 values between the highly blended and the original synthetic fingerprints are tested" (p. 12, l. 348 to 349); Fig. 8, caption: "Note that the most blended example did not have a stable solution and is therefore not plotted." |
| Concern | Counted independently by three instances on the page image (300 dpi), the left and the middle scatterplot each have 14 markers, at average JS distances of about 0.249, 0.272, 0.338, 0.359 and ten values from 0.441 to 0.624 in steps of about 0.02. Balance (Python): 20 tested − 14 plotted − 1 excluded in the caption = 5 runs unaccounted for; 6 of 20 (30 %) are not shown. The gaps between about 0.272 and 0.338 and between about 0.359 and 0.441 lie where the text reports failures ("In many of these cases, the inversion fails to converge", p. 12, l. 353). Resolution A: the five runs also failed and were dropped; this fits "many of these cases" but is not stated, and it would mean that about 6 of 10 runs below JS 0.44 failed while the error statement in that range (p. 12, l. 352 to 353) rests on the 4 that converged; the exclusions are then selected by outcome. Resolution B: markers coincide; with a marker spacing of about 0.02 on the axis this is unlikely for the observed gaps. Resolution C: fewer than 20 sets were run. The manuscript does not say which applies. For comparison, scenario 3 is complete (21 markers for 1 to 21 tracers, PP-27). GB-03 concerns the convergence claim of the Abstract, GB-32 the plotted values of the same figure, GB-17 the blending formula. Overlapping locations: GB-28 treats the names of test cases and axes in Fig. 7 to 9; this entry concerns the number of plotted runs in Fig. 8. |
| Suggestion | List in Sect. 4.1.3 or in the caption of Fig. 8 all 20 fingerprint sets with their average JS distance and convergence status, plot non-converged runs with a distinct symbol, and give the number of non-converging runs instead of "many". |
| Status | verified (marker count on the page image p. 29); resolutions A to C inferred |
| Severity | moderate |
| Source | S3, AB, SD |

**GB-32 The statement on errors "exceeding 700 mm/yr for JS < 0.44" does not describe the values plotted in Fig. 8, and the error does not rise monotonically below JS 0.55.**

| Field | Content |
|---|---|
| Check | P2, P3, P20 |
| Location | p. 12, l. 352 to 353; Fig. 8, left and middle scatterplot |
| Quotation | "As the JS distance decreases below 0.55, both absolute error and posterior uncertainty rise sharply, with errors exceeding 700 mm/yr for JS < 0.44." |
| Concern | The y axis of the left scatterplot of Fig. 8 is the summed absolute difference with ticks from 0 to 700 000 and no unit. Measured at 300 dpi by two instances (about 1 400 units per pixel): JS 0.249: 45 900 and 47 360; 0.272: 676 300 and 676 400; 0.338: 4 900 and 5 556; 0.359: 321 500 and 322 100; 0.50: 7 700 and 7 222; 0.52: 2 800 and 4 167; 0.54: 18 100 and 20 000; at 0.44 to 0.48 and 0.56 to 0.62 within one to two pixels of 0. Reading 1, axis in the unit of the text: values above 700 occur also at JS 0.50 to 0.54, so 0.44 is not the threshold for "exceeding 700", and the four values below 0.44 exceed it by one to three orders of magnitude. Reading 2, the "700" is the top tick 700 000 divided by 1 000: then no plotted value exceeds it (maximum 676 400). Under neither reading does the sentence describe the figure. The error is also not monotonic: it jumps at 0.54, returns near the unblended level at 0.44 to 0.48 ("Medium blended") and rises again below 0.44. The sharp rise of the posterior uncertainty below 0.55 agrees with the figure (0.747 at JS 0.561, 0.842 at 0.541, PP-26). Since the error is a sum over all pixels, a value in mm/yr per pixel cannot be read from it without the pixel count (GB-29). The unit is written "mm/yr" only here, "mm/y" elsewhere (p. 10, l. 295; p. 11, l. 325; p. 13, l. 384; p. 14, l. 428 and l. 435). GB-31 concerns the number of runs in the same figure, GB-03 the convergence claim. |
| Suggestion | Rewrite p. 12, l. 352 to 353 to the measured pattern, give the error values and the JS range they belong to in the unit of the figure or as per-pixel mean error with the pixel count, explain why the "Medium blended" set (JS 0.441) reaches the error of the unblended set, add the unit to the y axis of Fig. 8, and write "mm/y". |
| Status | verified (text on page image p. 12; values measured on Fig. 8 by two instances) |
| Severity | moderate |
| Source | S3, AB, SD, S2, S4 |

**GB-33 The ranking of the three degradation scenarios compares perturbations of incommensurable size, and the manuscript's own metrics give a different order.**

| Field | Content |
|---|---|
| Check | P9, P21 |
| Location | p. 12, l. 363 to 365; Fig. 7; Fig. 8; Fig. 9; p. 15, l. 456 to 461 |
| Quotation | "To summarize, among the three tested scenarios, the strongest impact on the posterior solution arises from reduced fingerprint distinctiveness. Geological map uncertainty follows as the second most influential factor." |
| Concern | The three scenarios share one baseline (summed absolute difference about 197, normalised uncertainty about 0.740), which makes them comparable in principle. The size of each effect, however, depends on how far each perturbation is pushed, and the three ranges are not on a common scale (map mismatch up to 1.15 × 10^7 m2 with three cases; JS down to 0.225; 21 down to 1 tracer). Maximum effects measured on Fig. 7 to 9, relative to the baseline (Python): scenario 1 error 274.8 (+39.3 %), uncertainty 0.7460 (+0.006); scenario 2 error up to 676 300 (about 3 400 times the baseline), uncertainty up to 0.893 (+0.153), plotted runs only; scenario 3 error up to 348.2 (+76.6 %), uncertainty up to 0.962 (+0.222). On both metrics, reducing the number of tracers has a larger effect than map uncertainty, and on the uncertainty metric the largest of all three. The ranking holds only under the proviso "provided that the most informative ones are retained" (p. 12, l. 365), a proviso not applied to the other scenarios. The ranking is a stated outcome of the synthetic tests and is carried into the recommendations of the Discussion (p. 15, l. 456 to 461). Graded major because it is a stated result of Sect. 4.1.3 and reverses under the manuscript's own metrics. GB-30 concerns the trend within scenario 1; GB-60 and GB-61 two Discussion claims drawn from the same scenarios. Overlapping locations: GB-28 treats the names of test cases and axes in Fig. 7 to 9; this entry concerns the ranking of the degradation scenarios. |
| Suggestion | Express each degradation on a common scale (for example the change in the data or in the average JS distance that each perturbation causes, or the ranges plausible in the field case) and rank at equal size, or replace the ranking with a statement per scenario of the range within which the posterior stays close to the baseline (for example at least 7 tracers, JS of at least 0.56, map mismatch below about 0.7 × 10^7 m2); adjust p. 15, l. 456 to 461. |
| Status | verified (text on page image p. 12; values measured on Fig. 7 to 9); inferred (dependence of the ranking on the tested ranges) |
| Severity | major |
| Source | S3, SD |

**GB-34 The statement that smoothing distances beyond 3000 m over-smooth the solution has no data behind it, and the smoothing distance used in all tests is not the best one tested.**

| Field | Content |
|---|---|
| Check | P3, P11 |
| Location | p. 12, l. 373 to p. 13, l. 374; Fig. 10, first row |
| Quotation | "However, beyond approximately 10 times the pixel size (3000 m), the solution becomes overly smooth, causing the posterior to deviate from the true erosion rates." |
| Concern | The first row of Fig. 10 has 20 runs with smoothing distances from about 200 m to 3000 m (counted at 300 dpi). The summed absolute difference falls monotonically from 256.5 to 76.1 to 76.3 at 3000 m, and the normalised uncertainty from about 0.99 to 0.27 (measured by three instances). No run beyond 3000 m is shown, so the deviation stated for larger distances is not reported anywhere. The same row shows that the smoothing distance used in all other tests (L = 1200 m) gives about 195 to 198, i.e. about 2.5 times the error at 3000 m (194.5/76.3 = 2.55, Python); the text does not explain why 1200 m was chosen. GB-24 discusses why the largest smoothing favours this one map shape; GB-50 the labelled value "L = 3000 m" in the same row; GB-35 and GB-36 other rows of Fig. 10. Overlapping locations: GB-29 treats the unnormalised error measure; this entry concerns the over-smoothing claim. |
| Suggestion | Extend the sweep in Fig. 10 beyond 3000 m so that the over-smoothing is visible, or remove the sentence; state in Sect. 4.1.1 the criterion by which L = 1200 m was chosen. |
| Status | verified (text on page images p. 12 and 13; values measured on Fig. 10, first row) |
| Severity | moderate |
| Source | S3, AB, SD |

**GB-35 The text describes a strong, non-monotonic effect of the data standard deviation, while Fig. 10 shows a monotonic change of about 0.01 %.**

| Field | Content |
|---|---|
| Check | P2, P3, P21 |
| Location | p. 13, l. 380 to 384; Fig. 10, third row |
| Quotation | "Very low data standard deviation values lead to large differences between the posterior and true erosion rate maps, likely due to overfitting or unstable gradients. As data standard deviation increases, the absolute difference first decreases to a minimum, then rises to a plateau at higher values." (p. 13, l. 380 to 382); p. 13, l. 383 to 384: "Beyond a data standard deviation of approximately 10-2 mm/y, model misfit begins to decrease rapidly while data misfit stabilizes." |
| Concern | The third row of Fig. 10 uses offset axes ("+1.974e2"). Measured at 300 dpi by three instances: the summed absolute difference rises monotonically from 197.4197 to 197.4203 at the smallest σd to 197.4431 at about 0.9 mm/y, a span of 0.0228 to 0.0234, i.e. about 0.012 % of its value (Python); the normalised uncertainty rises from 0.74015 to 0.7404; the model misfit stays between 1.5614 and 1.5623 (0.058 %). There are no "large differences" at very low σd (they are the lowest values), no minimum and no plateau, and the "rapid" decrease of the model misfit amounts to 0.0009. Read with the axis offsets, the row shows that the inversion is practically insensitive to σd over the tested range, which is the opposite of the reported result. Either the text describes a different sweep (for example one reaching lower σd than the plot shows) or the figure shows a sweep in which σd has no effect; which applies? The sensitivity to hyperparameters is one of the stated aims of the synthetic tests (p. 10, l. 280 to 281). The notation "10-2" lacks the superscript (page image p. 13). S3 graded major, AB and SD moderate; the merged finding takes the higher grade because a reported sensitivity result reverses from strong to negligible. GB-24 relates the flat response to the noise-free design; GB-34 and GB-36 concern other rows of the figure, GB-50 the labelled value "σd = 0.003 mm/y". |
| Suggestion | Rewrite p. 13, l. 380 to 384 to the values of Fig. 10 (third row) with the span of each metric, or show the sweep the text describes with a logarithmic σd axis; plot the row without offset or with a common y range; write "10⁻² mm/y". |
| Status | verified (text on page image p. 13; values measured on Fig. 10, third row) |
| Severity | major |
| Source | S3, AB, SD, S4 |

**GB-36 The iteration threshold of 25 is not supported by Fig. 10, the 115-iteration statement has no figure or number behind it, and the fixed 25 iterations replace the stated stopping rule.**

| Field | Content |
|---|---|
| Check | P2, P3, P5, P11 |
| Location | p. 13, l. 387 to 389; p. 9, l. 243 to 244; Fig. 10, fifth row |
| Quotation | "Only when the maximum number of non-linear steps is reduced below 25 does the posterior fail to converge to the true erosion map. Beyond 115 iterations, the change in data misfit between successive steps falls below 10−5" (p. 13, l. 387 to 388); p. 9, l. 243 to 244: "We stop the non-linear iterations when the data-misfit stops decreasing, or when it exceeds the user-defined maximal allowed number of iterations." |
| Concern | The fifth row of Fig. 10 has 20 runs at 5, 15, 25, ... 195 iterations (counted). Measured by three instances: 268.7 at 5 iterations, 200.5 to 200.9 at 15, 197.3 to 197.6 at 25, 199.5 to 199.7 at 35 and 200.3 to 201.1 from 45 to 195. Only the run at 5 iterations deviates; the run at 15 reaches the same value as the runs with 55 or more. The threshold therefore lies between 5 and 15, not at 25. The change of the data misfit between successive steps (10−5 beyond 115 iterations) is shown in no figure and given nowhere else as a number. The degradation and natural runs use a fixed 25 iterations (p. 11, l. 324; p. 14, l. 426), while the stated stopping rule (p. 9, l. 243 to 244) would not stop there if the data misfit still changes until about iteration 115; at 25 iterations the error is lowest, so the fixed number acts as early stopping chosen by comparison with the truth, which is not available for natural data. GB-34 and GB-35 concern other rows of Fig. 10, GB-50 the selection of the hyperparameters. |
| Suggestion | State in p. 13, l. 387 to 388 the threshold the sweep supports and why 25 was chosen; add the per-step change of the data misfit to Fig. 10 or remove the 115-iteration statement; either apply the stated stopping rule in all runs or replace p. 9, l. 243 to 244 by the fixed iteration number with its justification. |
| Status | verified (text on page images p. 9 and 13; values measured on Fig. 10, fifth row) |
| Severity | moderate |
| Source | S3, AB, SD |

**GB-37 Two pairs of tracer minerals have identical fingerprints in all seven units, so the 21 tracers are not 21 independent signals.**

| Field | Content |
|---|---|
| Check | P8, P38 |
| Location | p. 13, l. 394 to 395; Fig. 11, rows Anorthite, Pyroxene, Annite, Phlogopite |
| Quotation | "Tremolite, Talc, Quartz, Pyroxene, Phlogopite, Paragonite, Omphacite, Muscovite, Microcline, Magnesite, Glaucophane, Fayalite, Dolomite, Diopside, Chrysolite, Antigorite, Anorthite, Annite, Ankerite" |
| Concern | Bar lengths in Fig. 11, measured on the page image p. 32 at 150 dpi (Python, `zf/fig11.py`), in the order ZSF sediments, S.,T.,G., MR granite, ZSF metabasites, MR gneiss, Furgg series (serpentinites without bar): Anorthite 18, 122, 47, 122, 3, 53 px and Pyroxene 18, 122, 47, 122, 3, 53 px; Annite 67, 38, 69, 26, 80, 67 px and Phlogopite 67, 38, 69, 26, 80, 67 px. Muscovite equals Annite except in the metabasites (22 against 26 px), Ankerite equals Dolomite except in MR granite (4 against 2 px). The figure instance found the same at 300 dpi (Anorthite and Pyroxene 34, 243, 92, 243, 6, 103 px; Annite and Phlogopite 130, 74, 136, 51, 160, 131 px). Two minerals with different structures and chemistry are unlikely to have identical normalised peak areas in seven rock units; identical rows suggest that the same or overlapping 2θ windows were used for both, which the text, which lists no windows (GB-17), cannot exclude. "Pyroxene" is moreover a mineral group listed next to two pyroxenes, diopside and omphacite. Duplicated rows double the weight of the same information in the data misfit and mean that the natural XRD matrix has at most 19 distinct rows. Were the same 2θ windows used for Anorthite and Pyroxene and for Annite and Phlogopite? GB-38 concerns the name of another mineral in the same list; GB-24 and GB-60 the meaning of the tracer count. |
| Suggestion | State in Sect. 3.4 or in the methods table proposed in GB-17 the 2θ windows of each mineral, explain the identical rows, and either merge duplicated tracers or show that they carry independent information; replace "Pyroxene" by the intended mineral or justify the group next to diopside and omphacite. |
| Status | verified (bar lengths measured on page image p. 32); assumption (cause of the duplication), therefore put as a question |
| Severity | moderate |
| Source | ZF |

**GB-38 One of the 21 tracer minerals is called "Chrysolite" in the text and "Chrysotile" in the figures.**

| Field | Content |
|---|---|
| Check | P3, P38 |
| Location | p. 13, l. 395; Fig. 11, row label; Fig. 15 and Fig. 16, x axis of the fingerprint panel; p. 10, l. 274 |
| Quotation | "Fayalite, Dolomite, Diopside, Chrysolite, Antigorite, Anorthite" (p. 13, l. 395); "Chrysotile" (Fig. 11, Fig. 15, Fig. 16); p. 10, l. 274: "serpentinites (predominantly antigorite and chrysotile)" |
| Concern | The text lists the 21 minerals once (p. 13, l. 394 to 396). Comparison with Python of the text list against the row labels of Fig. 11 (both 21 entries): text minus figure = {"Chrysolite"}, figure minus text = {"Chrysotile"}. Chrysolite is a name for a yellowish green variety of olivine, chrysotile the serpentine mineral that the manuscript names for the serpentinites (p. 10, l. 274); the names denote two different minerals. Because the 2θ windows are chosen per mineral from RRUFF reference spectra (p. 9, l. 257 to 258), the name decides which reference a reader would use to rebuild the fingerprint. The intended mineral is probably chrysotile (inferred from p. 10, l. 274 and the figures). The result is not affected, its reproducibility is, hence moderate. GB-37 concerns two other rows of the same list. Overlapping locations: GB-20 treats the names of the lithological units; this entry concerns the name "Chrysolite". |
| Suggestion | Replace "Chrysolite" by "Chrysotile" at p. 13, l. 395 if chrysotile is meant, and name the RRUFF reference used for this mineral in the table of 2θ windows suggested in GB-17. |
| Status | verified (difference of names on page images p. 13, 32, 36, 37; chrysolite as olivine variety read at https://minerals.net/variety/chrysolite); inferred (identity of the intended mineral) |
| Severity | moderate |
| Source | S2, AB, S3, S4, SD |

**GB-39 The validity of the XRD fingerprints is asserted from a qualitative match, without a quantitative reference and without the variability within a unit.**

| Field | Content |
|---|---|
| Check | P31 |
| Location | p. 13, l. 399 to 401; p. 9, l. 251; p. 10, l. 282 to 283; Fig. 11 |
| Quotation | "The mineralogical fingerprints derived from processed and binned XRD data align well with established knowledge of the lithology in the Gorner Glacier catchment (Bearth, 1953; Steck et al., 2015), supporting the 1) the robustness of the cleaning and binning approach, and 2) the validity of the input data for the inversion method." |
| Concern | Aim 1 of the natural tests (p. 10, l. 282 to 283) is answered by a statement without a measure. No per-mineral comparison with expected compositions, no independent quantitative mineralogy (for example Rietveld refinement on a subset) and no replicate measurement is reported: search in `text.json`, p. 1 to 16, for "replicat": 0 hits. The number of source samples per unit is not stated ("collected from every lithological unit", p. 9, l. 251), and Fig. 11 shows one bar per mineral and unit without spread, so the variability of the fingerprints within a unit, which enters the data misfit, is unknown. GB-37 shows that two pairs of rows are identical, which a quantitative check would have revealed. KK-21 concerns the wording of the quoted sentence. Overlapping locations: KK-13 treats the panel reference to Fig. 3, KK-14 treats the name of the glacier, GB-38 treats the name "Chrysolite"; this entry concerns the qualitative fingerprint check. |
| Suggestion | Report in Sect. 4.2 the number of source samples per unit with mean and spread per tracer (error bars in Fig. 11), and test the binned peak areas against an independent quantitative method on a subset, giving the agreement as a number. |
| Status | verified |
| Severity | moderate |
| Source | SD |

**GB-40 The natural known-mixture test is reported without sample count, settings or a quantitative criterion, rests on one small unit, and Fig. 13 has no common density scale.**

| Field | Content |
|---|---|
| Check | P3, P11, P20, P29, P31 |
| Location | p. 14, l. 413 to 416; p. 10, l. 283 to 284; Fig. 13, upper and lower panel, inset and caption |
| Quotation | "Merging the inversion results from multiple detrital samples collected at the sink of this sub-catchment shows that the predicted erosion rates for pixels within the Zermatt - Saas Fee unit (ZSF sediments) are close to zero (Figure 13). Some spillover occurs from adjacent lithologies, but the overall pattern confirms that the inversion respects geological boundaries" (p. 14, l. 413 to 415); Fig. 13, caption: "a taller peak indicates greater consistency across inversions" |
| Concern | Using a subcatchment in which one mapped unit does not crop out as a negative control is a useful design. As reported, however: (1) the number of detrital samples and of inversions is not given ("multiple", p. 14, l. 413; "multiple inversions", caption; search in `text.json`, p. 1 to 16, for "multiple" and "several": 9 hits, none with a count for this test), nor their dates, nor the inversion settings (Sect. 4.2.1 contains none, unlike Sect. 4.2.2, p. 14, l. 426 to 428), nor how the inversions are merged; (2) "close to zero" has no threshold, and no share of the predicted sediment flux attributed to the ZSF sediments and no size of the "spillover" is reported; (3) the test rests on one unit, the ZSF sediments, which the manuscript itself calls a small unit with "lower resolution" (p. 10, l. 299 to 300), while 6 of 7 units have outcrops in the subcatchment (Fig. 12 caption); (4) the tracer matrix is built per lithology, so pixels of present units outside the subcatchment (most of the ZSF serpentinites, ZSF metabasites and MR gneiss lie outside the dashed boundary in the inset of Fig. 13) are indistinguishable from those inside and receive erosion, which a KDE pooling all pixels of a unit cannot show; (5) the six ridgelines of the upper panel share one "Density" label without scale, while the lower panel has a scale from 0 to 2, although the caption tells the reader to compare peak heights; (6) the Furgg series, which crops out in the subcatchment (p. 14, l. 411), also has its density maximum at about 0 to 0.12 mm/y, so "close to zero" alone does not separate the non-contributing unit from a contributing one, and the MR gneiss peaks at about 0.55 to 0.61 mm/y although its outcrop inside the subcatchment is a small patch at the south-eastern edge; (7) the x axis ends at about 3.3 mm/y while the ZSF serpentinite and Stockhorn curves are still above zero. The claim that the inversion "respects geological boundaries" is thus an intended property, not a measured one. GB-54 concerns the premise of the test (subcatchment boundary and outcrops in Fig. 12), GB-58 the verb "confirms", KK-22 the names of the subcatchment. Overlapping locations: GB-20 treats the names of the lithological units; this entry concerns the reporting of the known-mixture test. |
| Suggestion | Give in Sect. 4.2.1 the number and dates of the samples, the number of inversions, the inversion settings and the merging rule; define a pass criterion (for example the fraction of the predicted flux from the absent unit and from pixels outside the subcatchment) and report it per sample against a reference (prior-only inversion or permuted fingerprints), comparing the ZSF sediments with the Furgg series explicitly; give each ridgeline of Fig. 13 a density scale or plot all KDEs on one axis and extend the x axis to the maximum rate; consider a second subcatchment or a synthetic test with the measured fingerprints in which several units are absent. |
| Status | verified (text, search, figure on page images p. 14, 33 and 34); inferred (Furgg and MR gneiss peak positions read on axis labels without ticks; indistinguishability of pixels within a unit) |
| Severity | moderate |
| Source | S3, SD, AB |

**GB-41 Zircon and XRD results are described once as coming from the same detrital sample and once from a sample taken at the same date and time.**

| Field | Content |
|---|---|
| Check | P2 |
| Location | p. 14, l. 420 to 421; p. 14, l. 437 to 438 |
| Quotation | "we compare it against a zircon-based fingerprinting approach applied to the same detrital sample" (p. 14, l. 420 to 421); p. 14, l. 437 to 438: "We then applied the same nonlinear inversion technique to the XRD-derived dataset acquired from a detrital sample taken at the same date and time." |
| Concern | The first passage says one sample; the second can be read as a second sample collected simultaneously. For a benchmark of two fingerprinting methods it matters whether both data sets come from the same material, because the variability between two samples would add to the method difference. Is it one sample split into two aliquots, or two samples (for example from the pump sampler and a separate bulk sample)? |
| Suggestion | State in Sect. 4.2.2 whether the zircon and XRD data come from one sample or from two, and if two, how they were taken. |
| Status | verified (both passages on the page image p. 14); assumption (reading as two samples), therefore put as a question |
| Severity | minor |
| Source | S3 |

**GB-42 Several counts needed to read the natural and synthetic results are given only in figures.**

| Field | Content |
|---|---|
| Check | P22 |
| Location | p. 14, l. 423 to 425; p. 15, l. 443 to 444; p. 13, l. 391 to 392; p. 11, l. 329 to 331; Fig. 7; Fig. 11; Fig. 14; Fig. 16 |
| Quotation | "we derived mineralogical fingerprints based on distinct age-concentration distributions of zircon populations" (p. 14, l. 425); p. 15, l. 443: "we combine both zircon and XRD data by concatenating the tracer concentration matrices A" |
| Concern | Not stated in the text: the number of zircon age bins (13, counted on the x axis of Fig. 14, from 40 to 140 Ma to 750 to 800 Ma); the number of tracers in the combined set (21 + 13 = 34, Python, matching the 34 bars of Fig. 16); the number of source units (7, counted in the caption of Fig. 11; the text says "the main lithological units", p. 13, l. 392); the area mismatch of the two modified maps of scenario 1 (about 0.69 × 10^7 and 1.15 × 10^7 m2, read on Fig. 7). Search in `text.json`, p. 1 to 16, for "13", "34", "seven", "thirteen" and "age bin": 4 hits (p. 7, l. 199 and l. 200, equation references; p. 14, l. 414, "Figure 13"; p. 14, l. 424, "13:30"), none of them one of these counts. Each is needed to judge the underdetermination of the natural inversions (tracers against units) and the size of the map perturbation. GB-41 concerns the sample identity in the same passage, GB-29 the pixel count. Overlapping locations: KK-03 treats the form of narrative citations, GB-28 treats the names of test cases and axes in Fig. 7 to 9, GB-30 treats the trend statement of scenario 1, GB-33 treats the ranking of the degradation scenarios; this entry concerns counts given only in figures. |
| Suggestion | State these four counts in Sect. 4.1.3 and 4.2 (number of source units, number and limits of the zircon age bins, number of tracers in the combined inversion, area mismatch of each scenario 1 map). |
| Status | verified (counts on the page images; search in `text.json`) |
| Severity | minor |
| Source | S3 |

**GB-43 For the natural inversions, the prior value and the annual sediment export estimate, both named as required inputs, are not reported.**

| Field | Content |
|---|---|
| Check | P11, P12, P15, P25 |
| Location | p. 14, l. 426 to 428; p. 3, l. 65 to 66; p. 5, l. 132 to 133; p. 5, l. 160 (Eq. 2); p. 9, l. 268; p. 15, l. 452 to 454; p. 16, l. 479 to 480 |
| Quotation | "a data standard deviation of 0.01 mm/y, a prior equal to the average true erosion rate, and a step size µ of 0.1" (p. 14, l. 427 to 428); "and d) an estimate of the total annual suspended sediment export from the catchment" (p. 5, l. 132 to 133); p. 16, l. 479 to 480: "The approach integrates prior erosion estimates, a yearly sediment export estimate, and spatial information on source areas." |
| Concern | (1) For the zircon, XRD and combined inversions the parameter list repeats the synthetic setting "a prior equal to the average true erosion rate" (p. 14, l. 428; "same inversion parameters", p. 15, l. 444 to 445). In a natural catchment the true erosion rate is the unknown, so the prior actually used is not stated. (2) The total annual suspended sediment export is listed among the four inputs of the method in the Introduction, the Discussion and the Conclusions, and Eq. 2 rescales the data vector by the total erosion rate. Its value, source and uncertainty are given nowhere: search in `text.json`, p. 1 to 16, for "export": 5 hits (p. 3, l. 66; p. 5, l. 133; p. 15, l. 454 and l. 468; p. 16, l. 479), none with a value or source; "sediment load", "sediment yield", "t/y" and "tonne" 0 hits. The "multi-year suspended sediment datasets" occur only as a reason for choosing the site (p. 9, l. 268) and are not cited. (3) The natural results are reported in absolute units (for example "(>8000 mm/y)", p. 14, l. 435; Fig. 13 to 16 in mm/y), so a value must have been used (inferred). Both inputs control the absolute erosion rates in Fig. 13 to 16, which therefore cannot be reproduced or judged. The data statement (p. 16, l. 490) mentions neither (see GB-66). GB-01 concerns the assumption that one sample represents the annual export. Overlapping locations: GB-14 treats the scope of the error propagation; this entry concerns the missing prior and export estimate. |
| Suggestion | State in Sect. 4.2 the prior erosion rate used for the natural runs and how it was obtained (if derived from the export estimate, say so at p. 14, l. 428), and the annual export with value, source, period and uncertainty; cite the multi-year datasets; add both to the data statement; otherwise remove the export from the list of inputs at p. 3, l. 65 to 66, p. 15, l. 452 to 454 and p. 16, l. 479. |
| Status | verified (wording and absence by search); inferred (use of a value from the units of the results); assumption (what was actually used), therefore asked |
| Severity | moderate |
| Source | S2, S3, S4, SD |

**GB-44 The comparison of zircon and XRD inversions is confounded by missing zircon source fingerprints and rests on a single detrital sample.**

| Field | Content |
|---|---|
| Check | P9 |
| Location | p. 14, l. 430 to 434; p. 14, l. 439; p. 3, l. 71 to 73; p. 10, l. 284 to 285; Fig. 14; Fig. 15 |
| Quotation | "zircon data were not available for two lithological units: no zircon grains were recovered from the Zermatt-Saas Fee (ZSF) ophiolites (metabasites and eclogites), and no age data were available for the Monte Rosa garnet-gneiss (MR g-g) unit" (p. 14, l. 430 to 432); p. 14, l. 439: "Compared to the zircon-only results, the XRD-based posterior shows greater stability." |
| Concern | The manuscript discloses the zircon gaps; their consequences for the comparison are not drawn. Of the 7 units, the zircon matrix has no data for one (ZSF metabasites), a copied fingerprint for a second (MR g-g equal to MR granite, p. 14, l. 433 to 434) and "only very low concentrations" for a third (serpentinites, p. 14, l. 432 to 433), while XRD has measured fingerprints for all 7 (PP-31). In the forward model a unit with a near-zero fingerprint column can explain a signal only through a very large exp(ε); the zircon map peaks above 8000 mm/y in the serpentinite area (p. 14, l. 435; Fig. 14), about 1 000 times the upper end of the XRD colour scale (8 mm/y, Fig. 15). The instability may therefore stem from incomplete source data rather than from zircon as a tracer. The comparison also uses one detrital sample (28 June 2019), although "multi-year suspended sediment datasets" exist (p. 9, l. 268) and "multiple detrital samples" were inverted in Sect. 4.2.1 (p. 14, l. 413). No truth is available, so the "accuracy" in aim 3 (p. 10, l. 285) cannot be assessed by this design. Graded major because the claim that XRD outperforms zircon changes if the instability is due to missing source data. GB-11 concerns where the gaps are disclosed, GB-46 the claim on the combination, GB-55 the display of the copied fingerprint. Overlapping locations: GB-20 treats the names of the lithological units; this entry concerns the confounded zircon comparison. |
| Suggestion | Add in Sect. 4.2.2 a comparison restricted to the units with measured fingerprints in both methods (or a synthetic test with the measured zircon and XRD matrices and a known truth), repeat the natural comparison on several dated detrital samples with their spread, replace "accuracy" at p. 10, l. 285 by what the natural test can show, and state the zircon gaps where the comparison is announced (p. 3, l. 71 to 73). |
| Status | verified (gaps, single sample, values); inferred (mechanism through the near-zero column) |
| Severity | major |
| Source | SD |

**GB-45 The three-way comparison of zircon, XRD and combined inversions gives numbers for some cases and only descriptions for others.**

| Field | Content |
|---|---|
| Check | P11 |
| Location | p. 14, l. 435 to 436; p. 14, l. 439 to p. 15, l. 442; p. 15, l. 446 to 449; Fig. 14 to Fig. 16 |
| Quotation | "the resulting posterior solution is highly unstable, with extreme erosion rate values (>8000 mm/y), low resolution" (p. 14, l. 435 to 436); p. 15, l. 448 to 449: "The resulting erosion pattern more closely resembles the XRD-only solution" |
| Concern | The cases are compared on five properties. What the text reports (zircon / XRD / combined): maximum erosion rate above 8000 mm/y / not given / not given; resolution "low" without number / not given / not given; total normalised uncertainty 0.87 / 0.82 / 0.86; average JS distance 0.48 / not given / 0.57; data and model misfit not given in any case. "Stability" (p. 14, l. 439; p. 15, l. 446) and "more closely resembles" (p. 15, l. 448 to 449) have no number. Values for some empty cells can be read from the figures (colour bars end at about 8000, 8 and 12 mm/y), but the text draws its conclusions from the qualitative descriptions. GB-46 and GB-47 concern the interpretation of the uncertainty and the basis of the JS distance; GB-44 the confounding of the comparison; this finding the completeness of the comparison. Overlapping locations: GB-15 treats the definitions and names of the uncertainty metrics; this entry concerns the incomplete three-way comparison. |
| Suggestion | Add a table to Sect. 4.2.2 with one row per case and the same quantities for each: maximum and median posterior erosion rate, mean resolution, total normalised posterior uncertainty, average JS distance, data misfit, model misfit, and a similarity measure between the combined and each single-data posterior map. |
| Status | verified (text on page images p. 14 and 15; colour bar ticks on the page images of Fig. 14 to 16) |
| Severity | moderate |
| Source | S3 |

**GB-46 The claim that combining XRD with zircon data further stabilises and improves the solution is not supported by the reported values.**

| Field | Content |
|---|---|
| Check | P2, P6, P15, P21 |
| Location | p. 15, l. 446 to 447; p. 15, l. 461 to 462; p. 3, l. 72 to 73; p. 5, l. 139 to 140; p. 10, l. 284 to 285; p. 14, l. 436; p. 15, l. 441 to 442; Fig. 14; Fig. 15; Fig. 16 |
| Quotation | "Adding XRD data to the zircon dataset stabilizes the inversion and improves the posterior solution. The normalized posterior uncertainty decreases slightly to 0.86 (from 0.87 in the zircon-only case)" (p. 15, l. 446 to 447); "combining XRD data with other fingerprint data such as zircon data, proves to further stabilize and improve the posterior solution" (p. 15, l. 461 to 462); p. 3, l. 72 to 73: "showing that integrating XRD with zircon data improves the stability and sharpness of the posterior solution" |
| Concern | The three values agree between text and figures (0.87, 0.82, 0.86; PP-30). The comparison is drawn against the weakest case. Differences (Python): zircon to combined −0.01 (−1.1 %), XRD to combined +0.04 (+4.9 %), zircon to XRD −0.05. With values rounded to two decimals, the zircon to combined difference lies between −0.020 and 0.000 and may be zero. Relative to XRD alone, combining increases the normalised uncertainty, which contradicts "further stabilize and improve" (p. 15, l. 461 to 462). From the manuscript's own Eq. 12 and 20 it follows that, with the same Cd and Cm (p. 15, l. 444 to 445), stacking the zircon rows under the XRD rows adds a positive semidefinite term to GT Cd^-1 G, so at the same linearisation point the trace of the posterior covariance cannot increase; that the combined value is higher than the XRD value means that G was evaluated at different posterior models, so the metric mixes information content with the location of the posterior. "Stability" and "sharpness" are not measured: search in `text.json`, p. 1 to 16, "stabil" 10 hits and "sharp" 5 hits, none with a definition or value. The JS distance is given for zircon (0.48) and combined (0.57) but not for XRD alone, so the manuscript's own threshold of 0.55 (p. 12, l. 352) cannot be applied to the XRD case. How the two data types are weighted in the concatenated inversion (same σd of 0.01 mm/y for zircon age bins and XRD peak areas?) is not stated. The evidence is one detrital sample, which does not carry "proves". Graded major because it concerns the answer to aim 3 of the natural tests and a conclusion carried into Introduction and Discussion. GB-44 concerns the confounding of the single-data comparison, GB-45 the completeness of the reported quantities, GB-47 the JS values, GB-15 the definition of the metric. |
| Suggestion | Compare the combined case in Sect. 4.2.2 with both single-data cases, with more decimals; report the JS distance of the XRD case; define "stability" as a measurable quantity (for example the spread of posterior maps over several detrital samples or starting models) and report it for all three cases; compute the posterior covariance of all three cases also at a common linearisation point; state the data weighting of the combined run; and rewrite p. 3, l. 72 to 73 (with its copy at p. 5, l. 139 to 140), p. 15, l. 446 and l. 461 to 463 to what these numbers show; drop "accuracy" from aim 3 (p. 10, l. 285) or say how it is assessed for natural data. |
| Status | verified (values in text and on page images of Fig. 14 to 16; search); inferred (differences; argument from Eq. 12 and 20) |
| Severity | major |
| Source | S3, S4, SD |

**GB-47 The average Jensen-Shannon distance of the natural fingerprints has no stated basis, and the zircon set contains units without data and a duplicated unit.**

| Field | Content |
|---|---|
| Check | P20 |
| Location | p. 15, l. 447 to 448; p. 14, l. 430 to 434; p. 12, l. 346 to 347; Fig. 14, source fingerprints |
| Quotation | "the average Jensen-Shannon distance between source fingerprints increases from 0.48 to 0.57, indicating improved distinguishability" (p. 15, l. 447 to 448); p. 14, l. 433 to 434: "we assigned the MR g-g unit the same zircon-age fingerprint as the Monte Rosa granite unit" |
| Concern | For the synthetic tests the denominator is stated: the average over all pairs of source signatures (p. 12, l. 346 to 347; with 7 units 21 pairs, Python). For the natural case it is not. In the zircon set the ZSF metabasites have no zircon grains (p. 14, l. 430 to 431), the serpentinites only very low concentrations (p. 14, l. 432 to 433; no visible share in any of the 13 age bins of Fig. 14), and MR g-g is a copy of MR granite (equal shares in each bin of Fig. 14). The JS distance of the copied pair is 0 by construction, and for a unit with an all-zero fingerprint it is undefined. Whether such pairs were included, excluded or treated otherwise changes the average and with it the meaning of "0.48"; no value is given for the XRD-only set. GB-46 concerns the uncertainty values of the same sentence; this finding the JS distance. Overlapping locations: GB-44 treats the confounded zircon comparison; this entry concerns the basis of the natural JS distances. |
| Suggestion | State in Sect. 4.2.2 over which lithology pairs the average is taken for each of the three sets, how units without zircon data and the duplicated MR g-g fingerprint are handled, and give the value for all three sets. |
| Status | verified (text on page images p. 12, 14, 15; shares on the page image of Fig. 14); inferred (effect of the pair handling on the average) |
| Severity | moderate |
| Source | S3 |

**GB-48 The hatched "low-confidence areas" in Fig. 5, 6 and 14 to 16 are not defined, and the legend swatch in Fig. 6 has no label.**

| Field | Content |
|---|---|
| Check | P8, P29 |
| Location | Fig. 5, panel (b) legend; Fig. 6, legend swatch below panel (b); Fig. 14, Fig. 15 and Fig. 16, legend below the erosion map |
| Quotation | "Low-confidence areas" (Fig. 5); Fig. 14 to 16: "Low-con dence area" |
| Concern | The posterior maps mark some pixels with hatching. Neither the captions nor the text say by which criterion (resolution, normalised variance, threshold) a pixel is "low-confidence": search in `text.json`, all pages, for "confiden" and "hatch": 0 hits; "Low-con" 3 hits, all in Fig. 14 to 16, where the "fi" ligature is missing in the rendered label (page images p. 35 to 37). In Fig. 6 the hatched swatch stands without text. Without the criterion a reader cannot tell whether the hatched hotspot pixels in Fig. 15 and 16 weaken the statements at p. 14, l. 439 to p. 15, l. 441 and p. 15, l. 446 to 449. GB-15, GB-25, GB-26 and GB-29 concern other panels of Fig. 5. Overlapping locations: KK-14 treats the name of the glacier; this entry concerns the hatching criterion. |
| Suggestion | Define the hatching criterion in Sect. 3.3 and in the caption of Fig. 5, refer to it in the captions of Fig. 6 and 14 to 16, add the label to the swatch in Fig. 6, and correct "Low-con dence area" to "Low-confidence area" in Fig. 14 to 16. |
| Status | verified |
| Severity | moderate |
| Source | AB, SD, S3 |

**GB-49 Figure 6, panels (g) to (i), lack axis labels, and the data misfit axis in (i) appears to lack its scale factor.**

| Field | Content |
|---|---|
| Check | P29 |
| Location | Fig. 6, panels (g), (h) and (i) |
| Quotation | "(i) Trade-off data- vs model-misfit" |
| Concern | In Fig. 5 the panels (g) and (h) have the x label "Iteration", panel (i) has "Data misfit" with the factor "1e8" and the colour bar label "Iteration". In Fig. 6 all four labels and the factor are missing (300 dpi). Both runs use the same synthetic data and data covariance (p. 11, l. 310 to 311), so the data misfit at the prior must be the same. In Fig. 6i the first point lies at model misfit 0.00 (the prior) and data misfit about 2.3, in Fig. 5i the first plotted point, after at least one iteration, at about 1.88 × 10^8; the data misfit at the prior is therefore at least 1.88 × 10^8, which suggests that the factor 1e8 is missing in Fig. 6i. Is that the case? GB-26 and GB-27 concern the values and the reference of other panels of Fig. 6. |
| Suggestion | Add "Iteration" to Fig. 6g and 6h, "Data misfit" with its scale factor to Fig. 6i, and "Iteration" to the colour bar of Fig. 6i. |
| Status | verified (missing labels); inferred (missing factor) |
| Severity | minor |
| Source | AB |

**GB-50 The parameter values marked in Fig. 10 differ from the set used in all other tests, and neither the meaning of the marks nor a selection criterion is given.**

| Field | Content |
|---|---|
| Check | P2, P5, P11, P29 |
| Location | Fig. 10, third column, rows 1 to 5, and caption; p. 11, l. 324 to 326; p. 10, l. 293 to 295; p. 14, l. 426 to 428 |
| Quotation | "L = 3000 m", "σm = 6.2", "σd = 0.003 mm/y", "μ = 0.1", "n_m = 25" (Fig. 10); p. 11, l. 324 to 326: "These sensitivity tests are run with 25 iterations, a smoothing distance of 4 times the pixel size (L = 1200 m), a model standard deviation of 3, a data standard deviation of 0.01 mm/y, a prior equal to the average true erosion rate, and a step size µ of 0.1." |
| Concern | Each trade-off panel highlights one point with a label and a leader line. For the step size and the iteration number the labels equal the reported settings (0.1, 25); for L, σm and σd they do not (3000 m against 1200 m, 6.2 against 3, 0.003 against 0.01 mm/y); two of five agree. The caption does not say what the marks are (optimum, default or example), and the text does not say which values the other four parameters had in each sweep. The Introduction announces that "we optimize the hyper-parameters" (p. 3, l. 70), but no selection criterion is stated, and the sweeps use the known truth, which is unavailable for natural data. The first row of Fig. 10 suggests that the set used is not the optimum (GB-34). GB-34, GB-35 and GB-36 concern the values of rows 1, 3 and 5; GB-51 and KK-23 the labels of the same figure; KK-04 the spelling in p. 3, l. 70. Overlapping locations: GB-24 treats the design of the synthetic validation, GB-43 treats the missing prior and export estimate; this entry concerns the marked parameter values of Fig. 10. |
| Suggestion | State in the caption of Fig. 10 what the marked runs are and give the fixed values of the other parameters for each row; state in Sect. 4.1.4 the selected value of each hyperparameter and a selection criterion that does not use the truth (for example an L-curve or the discrepancy principle). |
| Status | verified (labels on page image p. 31; text on page images p. 10, 11, 14) |
| Severity | moderate |
| Source | S3, AB, SD |

**GB-51 Text in Fig. 10 and Fig. 16 is smaller than 6 pt at print size.**

| Field | Content |
|---|---|
| Check | P29 |
| Location | Fig. 10, all panels; Fig. 16, colour bars and mineral labels |
| Quotation | "+1.974e2" (Fig. 10, third row); Fig. 10, first row: "Smooting distance (m)" |
| Concern | Cap heights measured at 600 dpi: Fig. 10 tick label "150" 3.67 pt, offset label "+1.974e2" 3.50 pt, axis title 4.33 pt, annotation "σd = 0.003 mm/y" 4.33 pt; Fig. 16 colour bar label "12" 5.17 pt, rotated mineral names 4.83 to 5.17 pt. All lie below 6 pt by more than the method tolerance of 0.6 pt (comparison values in PP-18). GB-34 to GB-36 and GB-50 concern the content of Fig. 10, KK-23 its spelling. Overlapping locations: GB-35 treats the effect of the data standard deviation; this entry concerns the font size of Fig. 10 and 16. |
| Suggestion | Enlarge the labels of Fig. 10 (for example full page width or two figures) and of Fig. 16 to at least 6 pt at print size. |
| Status | verified |
| Severity | minor |
| Source | AB |

**GB-52 Figure 11 has no value axis and no column labels.**

| Field | Content |
|---|---|
| Check | P29 |
| Location | Fig. 11 |
| Quotation | "From left to right: ZSF ophiolites (serpentinites), ZSF sediments, Stockhorn-Turftgrat-Gornergrat, Monte Rosa (granite), ZSF ophiolites (metabasites, ecologites), Monte Rosa (gneiss, micaschist), Furgg series." |
| Concern | The seven columns of horizontal bars have no axis, no tick marks and no scale, so the reader cannot read the "relative mineral concentrations on a scale from 0 to 1" (p. 9, l. 261 to 262). The columns are identified only by their order in the caption. The longest bar of each column measures 242 to 243 px at 300 dpi, consistent with a per-sample normalisation to 1, but this must be inferred. GB-37 and GB-38 concern rows of the same figure, GB-53 its agreement with Fig. 15 and 16, GB-20 the unit names of the caption. Overlapping locations: GB-39 treats the qualitative fingerprint check; this entry concerns the axes of Fig. 11. |
| Suggestion | Add a value axis (0 to 1) under each column and the unit names above the columns; state in the caption that each column is normalised to its largest peak area. |
| Status | verified |
| Severity | minor |
| Source | AB |

**GB-53 The source fingerprints in Fig. 11 and in Fig. 15 and 16 do not agree in their relative proportions.**

| Field | Content |
|---|---|
| Check | P3 |
| Location | Fig. 11, all rows; Fig. 15, stacked bars; Fig. 16, first 21 stacked bars; p. 13, l. 398 |
| Quotation | "we obtained the mineral concentrations characterizing each lithological unit (Figure 11)" (p. 13, l. 398); Fig. 15 and 16, y axis: "Normalised abundance per mineral or age" |
| Concern | If Fig. 15 shows the Fig. 11 values normalised per mineral, each segment share must equal the share of the corresponding bar length in Fig. 11. Measured at 300 dpi (±1 px per bar or segment, share uncertainty below 0.01): Quartz, Fig. 11 bar lengths ZSF sediments 242, S.,T.,G. 128, MR granite 242, ZSF metabasites 62, MR gneiss 243, Furgg 243 px, shares 0.209, 0.110, 0.209, 0.053, 0.209, 0.209; Fig. 15 segments 79, 19, 104, 7, 147, 98 px of 454, shares 0.174, 0.042, 0.229, 0.015, 0.324, 0.216. Fayalite, Fig. 11 shares serpentinites 0.543 and S.,T.,G. 0.170, Fig. 15 shares 0.729 and 0.062. A per-unit factor would give a constant ratio of Fig. 15 share to Fig. 11 share for each unit; the measured ratios vary from 0.36 to 1.06 for S.,T.,G. (17 minerals) and from 1.08 to 1.95 for MR granite (11 minerals), and equal Fig. 11 values (Quartz 242 to 243 px in four units) appear as different Fig. 15 shares, which also rules out a monotonic transform. Fig. 16 reproduces Fig. 15. Either Fig. 11 or Fig. 15 and 16 do not show the tracer matrix A used in the inversion. Which matrix entered the inversion, and how is the normalisation of Fig. 15 and 16 defined? GB-56 concerns the bar colours of Fig. 15 and 16, GB-52 the axes of Fig. 11. Overlapping locations: GB-37 treats the duplicated tracer rows, GB-38 treats the name "Chrysolite", GB-39 treats the qualitative fingerprint check; this entry concerns the proportions in Fig. 11, 15 and 16. |
| Suggestion | State in the captions of Fig. 11, 15 and 16 which normalisation each shows and derive all from the same matrix A; provide the matrix as a table in the data repository (p. 16, l. 490). |
| Status | verified (measured shares); inferred (no single normalisation explains the difference) |
| Severity | moderate |
| Source | AB |

**GB-54 Figure 12 does not draw the subcatchment boundary, so the statement on outcrops cannot be checked, and a strip coloured like ZSF sediment outcrops lies in the highlighted area.**

| Field | Content |
|---|---|
| Check | P29 |
| Location | Fig. 12, north-east of the confluence marker, and caption; p. 14, l. 410 to 412; Fig. 13, inset |
| Quotation | "Lithology and outcrops in the Gorner-Grenz confluence subcatchment. The only unit not having outcrops in the subcatchment is the Zermatt- Saas Fee sediments unit." |
| Concern | The caption describes the subcatchment, but Fig. 12 shows the whole catchment with the colours outside a north-eastern area faded; the boundary is not drawn and the fading is not explained; the boundary appears only as a dashed line in the small inset of Fig. 13. Inside the saturated area north-east of the confluence (600 dpi) a narrow strip along the northern ridge has the colour #6c745c, closest to the legend field "Outcrops: metamorphic bündnerschiefer, calcarious mica schist" (#647c44, sum of differences 40), i.e. the outcrops of the ZSF sediments; the outcrops of the ZSF metabasites (#348434) differ by 112. Scaled from the inset of Fig. 13, the strip lies partly east of the point where the dashed boundary meets the ridge. Because the map has no grid and is shaded, this can only be inferred. The study-design instance found the statement "Only the Zermatt - Saas Fee sediment unit does not have outcrops" (p. 14, l. 411) consistent with the caption and the map; that check could not use a boundary, which the map does not draw, so it does not resolve the question. Does the strip belong to the ZSF sediment outcrops, and does it lie inside the subcatchment? If so, the known-mixture test (p. 14, l. 410 to 416, Fig. 13) loses its premise; this is why the finding is graded major although its verified core is the missing boundary. GB-40 concerns the reporting of the test, GB-23 the legend colours, KK-22 the names of the subcatchment. Overlapping locations: GB-20 treats the names of the lithological units; this entry concerns the subcatchment boundary in Fig. 12. |
| Suggestion | Draw the subcatchment boundary in Fig. 12, explain the faded colours in the caption, and give the outcrop area of each unit inside the subcatchment (for example in km2) in the caption or in Sect. 4.2.1. |
| Status | verified (boundary missing, page images p. 33 and 34); inferred (colour and position of the strip); the consequence for the test is put as a question |
| Severity | major |
| Source | AB |

**GB-55 Figure 14 has no colour legend, and the captions of Fig. 14 and 16 present a copied and a missing zircon fingerprint as source fingerprints without saying so.**

| Field | Content |
|---|---|
| Check | P29, P37 |
| Location | Fig. 14, geology panel, stacked bars and caption; Fig. 16, caption and fingerprint panel; p. 14, l. 430 to 434 |
| Quotation | "As shown in the source signatures in Figure 14, zircon data were not available for two lithological units" (p. 14, l. 430); Fig. 14, caption: "the geological map and the source fingerprints" |
| Concern | Fig. 15 and 16 carry a legend of the seven units; Fig. 14 does not, and its caption lists the panels without saying how to read them; the age unit "Ma" appears only at the last bin label. The text argues from the source signatures of Fig. 14 that two units have no zircon ages and that MR g-g received the granite fingerprint. Measured at 300 dpi, the bars contain the colours of ZSF sediments, MR granite, MR gneiss, S.,T.,G. and Furgg only, and the MR gneiss and MR granite segments are equal in every age bin (for example 228/227, 215/215, 64/66 px), which supports the text (PP-30); without a legend and a note in the captions a reader cannot see this. GB-44 concerns the consequences of the gaps for the comparison; KK-24 the abbreviation "Zr" in the same caption; GB-45 to GB-47 other quantities shown in Fig. 14. Overlapping locations: GB-20 treats the names of the lithological units, GB-46 treats the claim on combining XRD and zircon data; this entry concerns the legend and captions of Fig. 14 and 16. |
| Suggestion | Add the unit legend to Fig. 14, explain colours and age bins in Ma in the caption, and add to the captions of Fig. 14 and 16: "MR g-g zircon fingerprint copied from MR granite; no zircon data for ZSF metabasites". |
| Status | verified (page images p. 35 and 37) |
| Severity | minor |
| Source | AB, SD |

**GB-56 The stacked bar colours in Fig. 15, 16 and 5k do not match their legend fields, and two orange tones match the wrong unit.**

| Field | Content |
|---|---|
| Check | P3 |
| Location | Fig. 15 and Fig. 16, stacked bars and legend; Fig. 5, panel (k) with legend in panel (j); top rows of Fig. 8 and 9 |
| Quotation | "S.,T.,G.", "MR gneiss, mica", "MR granite" |
| Concern | Measured at 300 dpi: legend fields ZSF serpentinites #e4dc1c, ZSF sediments #849c44, S.,T.,G. #fc5404, MR granite #fc9c9c, ZSF metabasites #34a42c, MR gneiss #fc7c44, Furgg #bcdc6c; bar colours #ece45c, #a4b47c, #fc844c, #fcbcbc, #6cbc6c, #fca47c, #cce494. The bars are the legend colours at about 70 % opacity on white (for S.,T.,G.: 0.7 × (252, 84, 4) + 0.3 × 255 = (253, 135, 80), measured (252, 132, 76)). None of the seven bar colours matches its own legend field within a sum of differences of 40 (64 to 144). The S.,T.,G. bars (#fc844c) match the legend field "MR gneiss, mica" (sum 16), and the MR gneiss bars (#fca47c) match "MR granite" (sum 40). A reader who matches colours therefore assigns the S.,T.,G. contributions to the Monte Rosa gneiss and the Monte Rosa gneiss contributions to the granite, which affects the reading of the source signatures referred to at p. 14, l. 430 and p. 15, l. 446 to 449. GB-53 concerns the proportions of the same bars, GB-57 the legend layout of Fig. 15 and 16. |
| Suggestion | Draw the stacked bars with the opaque legend colours, or the legend swatches with the same opacity as the bars. |
| Status | verified |
| Severity | moderate |
| Source | AB |

**GB-57 Legend entries in Fig. 15 and 16 overlap or are cut off.**

| Field | Content |
|---|---|
| Check | P3 |
| Location | Fig. 15, legend; Fig. 16, legend |
| Quotation | "ZSF serpentinites", "ZSF metabasites" |
| Concern | In both figures the swatch of "ZSF metabasites" covers the last letters of "ZSF serpentinites"; in Fig. 16 the upper edge of the first legend row is cut off, so the tops of "ZSF serpentinites" and "ZSF metabasites" are missing (page image p. 37; the area above the row is white background, so the cut is in the figure). GB-56 concerns the colours of the same legends. |
| Suggestion | Widen the legend columns in Fig. 15 and 16 and move the legend of Fig. 16 so that the first row is complete. |
| Status | verified |
| Severity | minor |
| Source | AB |

#### Minor corrections

| ID | Location | Quotation | Replacement | Source |
|---|---|---|---|---|
| KK-17 | p. 10, l. 299 | "(such as Zermatt Saas-Fee sediments and Furgg series (Figure 4) and Figure 5J)" | "(such as the Zermatt-Saas Fee sediments and the Furgg series; Figures 4 and 5j)"; GB-20 concerns the unit name, this correction the form of the reference Overlapping locations: KK-05 treats the letter case of panel references; this entry concerns the reference form at p. 10, l. 299. | S3 |
| KK-18 | p. 12, l. 345 to 346 | "which measures the similarity between two probability distributions" | "which measures the dissimilarity between two probability distributions"; the next sentence states that values closer to zero indicate more similar signatures, so the distance measures dissimilarity Overlapping locations: GB-47 treats the basis of the natural JS distances; this entry concerns the word "similarity". | ZF |
| KK-19 | p. 12, l. 351 | "The more resemblant the source fingerprints are" | "The more similar the source fingerprints are" | S4 |
| KK-20 | p. 12, l. 370 | "the maximal amount of non-linear iterations" | "the maximum number of non-linear iterations" | S4 |
| KK-21 | p. 13, l. 400 | "supporting the 1) the robustness" | "supporting 1) the robustness"; GB-39 concerns the content of the sentence Overlapping locations: KK-14 treats the name of the glacier; this entry concerns the repeated article at p. 13, l. 400. | S3, S4 |
| KK-22 | p. 13, l. 406 to p. 14, l. 407; p. 14, l. 409; p. 14, l. 411; Fig. 12, map label and caption; Fig. 13, caption | "Gorner-Grenzgletscher conflu-ence" (p. 13, l. 406 to p. 14, l. 407); "contributing sub-catchment" (p. 14, l. 409); "sub-catchment. Only the Zermatt - Saas Fee sediment unit does not have outcrops in the Gorner-Grenz subcatchment" (p. 14, l. 411); "Gorner-Grenz confluence subcatchment" (Fig. 12 caption) | "subcatchment" throughout (form at p. 10, l. 283 and l. 284 and p. 14, l. 411); one name, "Gorner-Grenz confluence subcatchment", for the area and "Gorner-Grenzgletscher confluence" for the sampling point; in the caption of Fig. 13 join "Gorner" and "Grenz" with a hyphen as elsewhere. GB-20 concerns the unit name at p. 14, l. 411, GB-54 the content of Fig. 12, GB-40 the test reported at p. 14, l. 413 to 416. | S2 |
| KK-23 | Fig. 10, first row, x axis of the middle panel; Fig. 10, fifth row, annotation in the third panel | "Smooting distance (m)"; "n_m = 25" | "Smoothing distance (m)"; "nm = 25" with subscript m, as in the caption; GB-34 to GB-36, GB-50 and GB-51 concern the content and the font size of the same figure Overlapping locations: GB-35 treats the effect of the data standard deviation; this entry concerns the labels of Fig. 10. | S3, AB |
| KK-24 | Fig. 14, caption and y axis of the fingerprint panel; Fig. 16, title of the left panel | "using Zr fingerprint data"; "Normalised abundance per Zr age bin"; "combined XRD and Zr data" | "using zircon fingerprint data"; "Normalised abundance per zircon age bin"; "combined XRD and zircon data" (the text uses "zircon" throughout Sect. 4.2.2; Zr is the element). GB-44 to GB-47 and GB-55 concern the content of the same figures. Overlapping locations: GB-45 treats the incomplete three-way comparison, GB-46 treats the claim on combining XRD and zircon data; this entry concerns the abbreviation "Zr". | S2 |

#### Verification log

| ID | Check | Checked | Values | Result |
|---|---|---|---|---|
| PP-20 | P2, P38 | Number and names of the tracer minerals across text and figures | "21 minerals" (p. 13, l. 393), "21 target minerals" (p. 13, l. 397), "between 1 and 21 tracers" (p. 12, l. 358), "All tracers (21)" (Fig. 9); list at p. 13, l. 394 to 396: 21 names (Python); Fig. 11: 21 rows; Fig. 15: 21 axis labels; Fig. 5k: letters A to U = 21 | count consistent; one name differs (GB-38), two pairs of rows identical (GB-37) |
| PP-21 | P2, P38 | Standard parameter set across Sect. 4.1.1, 4.1.3, 4.2.2 and Fig. 10 caption | L = 1200 m, σm = 3, σd = 0.01 mm/y, prior equal to the average true erosion rate at p. 10, l. 293 to 295, p. 11, l. 324 to 326, p. 14, l. 426 to 428; 100 iterations in 4.1.1 (Fig. 5 x axis 0 to 100), 25 in 4.1.3 and 4.2.2; step size 0.1 in 4.1.3 and 4.2.2; symbols L, σm, σd, µ, nm in the caption of Fig. 10 | consistent; gaps raised in GB-26, GB-43 and GB-50 |
| PP-22 | P38 | Name of the distinctiveness measure | "Jensen-Shannon (JS) distance" (p. 12, l. 345), "JS distance" (p. 12, l. 346, l. 351 to 353), "average Jensen-Shannon distance" (p. 15, l. 447), "avg. JS" (Fig. 8) | no finding; misuse of the label in Fig. 9 in GB-28, wording in KK-18 |
| PP-23 | P2 | QN convergence statements against Fig. 5g and 5h | summed absolute difference 348 (iteration 1), about 197.4 (about iteration 22), 201.1 (iteration 100); normalised covariance trace rising from about 0.733 to 0.7426 and levelling off | "decreases rapidly, then plateaus" (p. 10, l. 305 to 306) and "rises steeply ... before levelling off" (p. 10, l. 306 to p. 11, l. 307) agree; the rise of the error by about 3.7 after iteration 22 is not mentioned |
| PP-24 | P3 | Same default configuration across Fig. 5, 7, 8, 9 and 10 | summed absolute difference: Fig. 7 forward geology 197.4; Fig. 10 row 1 interpolated to 1200 m 197.5; row 3 near σd = 0.01: 197.42; row 4 at µ = 0.100: 197.5; row 5 at n = 25: 197.6; Fig. 5g at iteration 25: 197.8; normalised trace: Fig. 7 0.7402, Fig. 8 unblended 0.7403, Fig. 9 at 7 to 21 tracers 0.7404, Fig. 10 row 3 0.74015 | consistent within the measurement uncertainty: no finding |
| PP-25 | P2, P3 | Scenario 1 misfits against the trade-off panel of Fig. 7 | data misfit 3.255, 3.490, 3.687 × 10^6; model misfit 1.562, 1.922, 2.460 (measured by two instances) | "in all cases, both data misfit and model misfit increase as map uncertainty grows" (p. 12, l. 341 to 342) agrees; the lower error of the minimally changed map is disclosed ("Surprisingly", p. 11, l. 338) and explained (p. 12, l. 340 to 341); trend statement in GB-30 |
| PP-26 | P2, P5 | Scenario 2 thresholds against Fig. 8, and the own JS thresholds against the natural values | uncertainty 0.8418 at JS 0.541 and 0.7467 at JS 0.561, so the jump lies at about 0.55 as stated (p. 12, l. 352); natural JS values: zircon 0.48 (between 0.44 and 0.55, where the synthetic uncertainty rises; result "highly unstable", consistent), combined 0.57 (above 0.55 by 0.02), XRD alone not reported | no finding on the 0.55 threshold of the uncertainty; error statement in GB-32, missing XRD value in GB-46 and GB-47 |
| PP-27 | P2, P3, P34 | Scenario 3 statements and counts against Fig. 9 | 21 markers at tracer counts 1 to 21 (counted at 300 dpi by three instances); error: 1 to 6 tracers 347.1 to 347.2, 348.2 to 348.4, 293.3 to 293.5, 296.4 to 296.5, 223.9 to 224.1, 205.0 to 205.2, 7 to 21 tracers 197.2 to 197.4; uncertainty 0.962, 0.918, 0.879, 0.834, 0.797, 0.769, then about 0.740; example panel "11 tracers" with 11 bars | "with 7 tracers ... approximately the same" and "below 7 ... increases rapidly" (p. 12, l. 360 to 361) agree: no finding; axis label in GB-28 |
| PP-28 | P2, P3 | Fig. 10 rows 2 and 4 against p. 13, l. 377 to 379 and l. 385 to 386 | row 4: µ = 0.010: 328.3; 0.015: 308.0; 0.022: 283.3; 0.032: 254.6; 0.046: 225.1; 0.068: 203.8; 0.100: 197.5; 0.147: 199.0; 0.215: 200.8; 0.316: 201.3; row 2: four markers near σm = 0 at 209.1, 204.1, 200.9, 198.9, cluster near σm = 0.32 at 197.6, then σm = 1.43 to 10.0 at 197.4; low σm at the highest data and model misfit | text agrees (optimum at µ = 0.1; low σm gives high misfits and larger differences): no finding |
| PP-29 | P3 | Colour of Fig. 5e at the hotspot; column order of Fig. 11 | Fig. 5e at the hotspot of Fig. 5a #fce4b4, colour bar bottom #fcf4b4 (sum 16); Fig. 11 column colours in the order of the caption and of the Fig. 5j legend | low posterior covariance at the hotspot as stated (p. 10, l. 300 to 301); column order consistent: no finding |
| PP-30 | P2, P3 | Natural-case values in text against Fig. 14 to 16 | text 0.87 (p. 14, l. 436), 0.82 (p. 15, l. 442), 0.86 (p. 15, l. 447); panel labels "Total normalised posterior uncertainty = 0.87", "= 0.82" and "= 0.86"; Fig. 14 colour bar top at 8534 ± 60 mm/y with yellow cells in the hotspot ("(>8000 mm/y)", p. 14, l. 435); Fig. 14: 13 age bins, MR gneiss and MR granite segments equal within ±2 px, no metabasite colour; Fig. 16 bars 1 to 21 equal Fig. 15 within ±5 px, bars 22 to 34 equal Fig. 14 | values agree: no finding; the JS values 0.48 and 0.57 are shown in no figure; interpretation in GB-46 |
| PP-31 | P23 | Coverage of the seven source units by zircon fingerprints | 7 units; zircon fingerprints for 5 colours in Fig. 14 (ZSF sediments, S.,T.,G., MR granite, MR gneiss as copy of MR granite, Furgg); no share for ZSF metabasites (no grains, p. 14, l. 430 to 431) and ZSF serpentinites (very low concentration, p. 14, l. 432 to 433): 5 + 2 = 7 | balance closes; the manuscript discloses the gaps; consequences in GB-44 and GB-47 |
| PP-32 | P1 | Number of tracers in the combined inversion | 21 minerals + 13 zircon age bins = 34 (Python); Fig. 16 shows 34 bars (counted) | arithmetic consistent; count not stated in the text (GB-42) |
| PP-33 | P20 | Denominator of the average JS distance in the synthetic tests | "between all pairs of source XRD signatures and use the average across all combinations" (p. 12, l. 346 to 347); 7 units give 21 pairs (Python) | no finding for the synthetic case; natural case in GB-47 |
| PP-34 | P11 | Coverage of the posterior metrics announced in Sect. 3.3 per test | 4.1.1 and 4.1.2: all metrics (Fig. 5 and 6, panels d to i); 4.1.3 and 4.1.4: error, normalised uncertainty, data and model misfit (Fig. 7 to 10), no resolution; 4.2.1: posterior erosion only (Fig. 13); 4.2.2: posterior map, resolution map, normalised uncertainty, no misfits (Fig. 14 to 16) | gaps in GB-40, GB-45 and GB-60 |
| PP-35 | P24 | Figures with time axes or dated events | no figure has a date axis or dated markers; time axes are iteration counts (Fig. 5, 6, 10); the sampling date of p. 14, l. 423 to 424 is shown in no figure | P24 not applicable: no finding |
| PP-36 | P6 | Absolute statements ("only", "all", "in all cases") | "Only the Zermatt - Saas Fee sediment unit does not have outcrops" (p. 14, l. 411): consistent with the caption of Fig. 12, the map cannot confirm it (GB-54); "in all cases, both data misfit and model misfit increase" (p. 12, l. 341 to 342): monotone in Fig. 7 (PP-25); "for all subsequent tests" QN (p. 11, l. 320): Sect. 4.1.3 and 4.2.2 name no SD run | no finding beyond GB-03 and GB-54 |

### Segment 4: Discussion, Conclusions, statements, references (p. 15 to 21)

#### Substantive findings

**GB-58 "Validated", "confirms" and "reliably recovered" are stronger than the tests behind them.**

| Field | Content |
|---|---|
| Check | P15, P32 |
| Location | p. 15, l. 451; p. 14, l. 415; p. 16, l. 482 |
| Quotation | "We explained and validated the use of binned XRD peak-area data as mineralogical fingerprints within a non-linear inversion scheme to infer erosion rate maps." |
| Concern | The natural-data evidence is limited by the manuscript's own descriptions. The subcatchment test checks attribution for exactly one unit ("Only the Zermatt - Saas Fee sediment unit does not have outcrops", p. 14, l. 411), reports "Some spillover" and gives no numeric criterion for "close to zero" (p. 14, l. 414 to 415); its conclusion "the overall pattern confirms that the inversion respects geological boundaries" (p. 14, l. 415) generalises from one unit. The fingerprint check is qualitative ("align well with established knowledge", p. 13, l. 399). The zircon comparison has no reference erosion rates (p. 14, l. 420 to p. 15, l. 449). The synthetic tests generate and invert data with the same forward model (p. 10, l. 288 to 290), so "the true erosion pattern can be reliably recovered" (p. 16, l. 482) holds for data consistent with the model. "Supports" (p. 14, l. 417) matches this evidence; "validated" and "confirms" do not; the same applies to "validate" and "validates" in the Abstract (p. 1, l. 3 and l. 8). No independent re-measurement is reported (PP-43). Graded major because the central claim "validated" does not stand unchanged if the finding holds. GB-24, GB-39 and GB-40 concern the tests themselves; GB-64 the content missing from the Conclusions. |
| Suggestion | Replace "validated" at p. 15, l. 451 by "tested", "confirms" at p. 14, l. 415 by "suggests", qualify p. 16, l. 482 as "with synthetic data generated by the same forward model, the true erosion pattern is recovered", and adapt "validate" and "validates" at p. 1, l. 3 and l. 8. |
| Status | verified |
| Severity | major |
| Source | S4 |

**GB-59 The Discussion claims the spatially informed approach and a non-linear mixing model as novel, although the Introduction attributes the spatial framework to the authors' 2020 paper and Eq. 1 is a linear mixture.**

| Field | Content |
|---|---|
| Check | P15, P28 |
| Location | p. 15, l. 454 to 455; p. 2, l. 59 to 61; p. 4, l. 126 to 128; p. 5, l. 150 to 152; p. 5, l. 157 to 158; p. 18, l. 559 to 560 |
| Quotation | "The novelty of our method lies in the spatially informed approach of this underdetermined inversion problem, and in the incorporation of non-linear mixing model." |
| Concern | The Introduction is careful here: it presents the method as "a non-linear adaptation of the inversion framework validated in (De Doncker et al., 2020)" (p. 2, l. 60 to 61), and that work is listed as "Inversion of provenance data and sediment load into spatially varying erosion rates" (p. 18, l. 559); its abstract describes a formal inversion that converts detrital zircon data into an erosion rate map from the spatial distribution of the source signatures. The spatially informed approach is therefore taken over, not introduced here. The second part also needs care: the manuscript describes the mixing as linear, "the detrital data are a weighted average of the tracer mineral concentrations, with the weights being the erosion rates" (p. 5, l. 151 to 152), and places the non-linearity in the parametrisation, "We cast the erosion rates in log-space to impose a positivity constraint, hence making this non-linear" (p. 5, l. 157 to 158). Is the novelty meant to be the log-space parametrisation of a linear mixture rather than a non-linear mixing model? Ehlers et al. (2015, GB-09) also derived spatial erosion patterns from detrital data. The sentence lacks an article ("of non-linear mixing model"). The results are not affected; what the manuscript can claim as its contribution is. Overlapping locations: KK-03 treats the form of narrative citations, GB-43 treats the missing prior and export estimate; this entry concerns the novelty claim. |
| Suggestion | Rewrite p. 15, l. 454 to 455, for example: "Building on the spatially explicit inversion of De Doncker et al. (2020), the novelty of this study lies in the use of binned XRD peak-area fingerprints and in a log-space parametrisation of the erosion rates that makes the inversion non-linear while the mixing remains linear in the erosion rates." |
| Status | verified (wording on page images p. 2, 4, 5, 15 and 18); De Doncker et al. (2020): abstract read in OpenAlex (https://api.openalex.org/works/doi:10.1002/esp.5008, reconstructed from the word index; full text not read); assumption (intended novelty), therefore asked |
| Severity | moderate |
| Source | S1, S4 |

**GB-60 The Discussion states that a broad tracer set further improves the inversion, while the Results show no gain above about 7 tracers.**

| Field | Content |
|---|---|
| Check | P9, P15 |
| Location | p. 15, l. 457 to 458; p. 12, l. 360 to 365; p. 15, l. 465 |
| Quotation | "Including a broad set of tracer minerals further improves model stability and resolution." |
| Concern | Scenario 3 reports: "The inversion with 7 tracers results in approximately the same posterior solution as with the full tracer set" (p. 12, l. 360), an increase of error and uncertainty only "when the number of tracers drops below 7" (p. 12, l. 360 to 361), and "reducing the number of tracers has a comparatively limited effect" (p. 12, l. 364 to 365). Scenario 3 reports neither resolution nor a stability measure (PP-34). The Results thus support a minimum number of informative tracers (about 7 of 21), not a further improvement from a broad set, and not for resolution or stability. With 7 source units the 7-tracer result is also consistent with a rank bound (GB-24), and the natural XRD set contains duplicated tracers (GB-37). GB-33 concerns the ranking of the scenarios from which this sentence is drawn. |
| Suggestion | Replace p. 15, l. 458 by, for example: "Below about 7 of the 21 tracers, error and posterior uncertainty increase rapidly; above this number, additional tracers change the posterior solution little." Align recommendation c) at p. 15, l. 465 ("multiple XRD tracers") with this threshold. |
| Status | verified |
| Severity | moderate |
| Source | S4, SD |

**GB-61 The effect of the number of source areas on resolution and uncertainty is stated as a finding but was not tested.**

| Field | Content |
|---|---|
| Check | P9, P15 |
| Location | p. 15, l. 460 to 461; p. 16, l. 485 |
| Quotation | "A higher number of distinct source areas leads to higher posterior resolution and lower uncertainty." |
| Concern | No test varies the number of source areas. Search in `text.json`, Results p. 10, l. 286 to p. 15, l. 449, for "number of": 4 hits, p. 12, l. 355, l. 361 and l. 364 (tracers) and p. 13, l. 387 (non-linear steps); none concerns source areas. Scenario 1 varies the mismatch between maps (p. 11, l. 327 to p. 12, l. 342), not the number of units. The nearest results concern unit boundaries (lower uncertainty at boundaries, p. 10, l. 301 to 303; p. 11, l. 318 to 319) and unit size (lower resolution of small units, p. 10, l. 299 to 300). The Conclusions build on it ("multiple mineralogically distinct source areas", p. 16, l. 485). GB-33 and GB-60 concern other Discussion claims drawn from the synthetic scenarios. Overlapping locations: GB-46 treats the claim on combining XRD and zircon data; this entry concerns the untested number of source areas. |
| Suggestion | Either add a synthetic test that varies the number of source units at constant fingerprint distinctiveness and reports resolution and uncertainty, or rephrase p. 15, l. 460 to 461 as a hypothesis, for example: "Because uncertainty is lower at boundaries between units (Sect. 4.1.1), a finer subdivision into distinct source areas may increase resolution; this was not tested here", and adapt p. 16, l. 485. |
| Status | verified (search as stated) |
| Severity | moderate |
| Source | S4, SD |

**GB-62 The recommended conditions of use exclude the setting for which the Introduction claims the method is most valuable, and the study catchment is not assessed against them.**

| Field | Content |
|---|---|
| Check | P15, P18 |
| Location | p. 15, l. 463 to 468; p. 16, l. 484 to 486; p. 2, l. 61 to p. 3, l. 63; p. 1, l. 23 |
| Quotation | "we recommend applying this method in catchments where: a) the spatial distribution of source lithologies is well constrained" (p. 15, l. 463 to 464); p. 16, l. 484 to 486: "Our results suggest that the method is best applied in catchments with minimal sediment storage, multiple mineralogically distinct source areas, and good prior knowledge of the spatial distribution of source areas." |
| Concern | The Introduction calls the approach "particularly valuable in glacierized catchments, where ice cover limits direct observations" (p. 2, l. 61 to p. 3, l. 62) and presents the absence of storage modelling as an advantage: "Importantly, this approach links sediment directly to its origin, without modelling storage or transport." (p. 1, l. 23). The Discussion notes that delineation "can be challenging in glaciated catchments with limited outcrop exposure" (p. 15, l. 460), recommends catchments with well-constrained lithology (p. 15, l. 464) and cautions against "significant sediment storage" (p. 15, l. 467). In the study catchment the lithology under the ice is inferred "based on regional geological knowledge" (p. 9, l. 271); the Steck et al. (2015) map differs from the map used by about 11.3 km2, about 15 % of a catchment of about 75 km2 measured on Fig. 4, and in scenario 1 that difference raised the error by 39 % (Fig. 7; GB-30). Search in `text.json`, p. 1 to 16, for "storage" and "stored": 7 hits (p. 1, l. 23 and l. 25, their copies in Sect. 2, p. 5, l. 148, p. 15, l. 467, p. 16, l. 485), none on storage in the Gornergletscher catchment. The recommendations thus exclude conditions that the Introduction names as the main field of use, and the manuscript does not say how its own catchment fares against them. That glacierised catchments often store sediment is general knowledge, not shown in the manuscript (assumption). How do the recommendations and the claimed application to glacierised catchments fit together, and does the Gornergletscher catchment meet the storage and delineation conditions? GB-19 concerns the provenance of the inferred map, GB-63 the sampling recommendations. Overlapping locations: KK-03 treats the form of narrative citations, KK-14 treats the name of the glacier, GB-60 treats the claim on a broad tracer set; this entry concerns the conditions of use. |
| Suggestion | State in Sect. 5 how far the Gornergletscher catchment meets conditions a) to c) (p. 15, l. 464 to 466) and the storage condition (p. 15, l. 467 to 468), with the inferred share of the catchment (Fig. 4); adapt either p. 2, l. 61 to p. 3, l. 63 (and its copy) or p. 16, l. 484 to 486 so that the claimed field of use and the recommendations agree; rewrite p. 1, l. 23 as an assumption of the method rather than an advantage. |
| Status | verified (textual tension, search); inferred (area shares measured on page images); assumption (sediment storage in glacierised catchments), therefore asked |
| Severity | moderate |
| Source | S4, SD |

**GB-63 The Discussion names mitigations of XRD limitations without saying whether they were applied to the samples of this study.**

| Field | Content |
|---|---|
| Check | P15 |
| Location | p. 15, l. 469 to p. 16, l. 476; Fig. 1, panel (c); Fig. 3, panel (a) |
| Quotation | "This can be diminished by powdering samples and using depth-integrated suspended sediment samples to average out sorting effects during transport (Butler et al., 2019)." |
| Concern | Search in `text.json`, p. 1 to 16, for "depth-integrat": 1 hit (p. 15, l. 470), and "pump": 0 hits. The text does not state how the detrital samples were taken (depth, integration, grain-size fraction); Fig. 1c and Fig. 3a label the device "pump sampler" (page images p. 22 and 24). Whether the samples were depth-integrated is therefore open, and the mitigation named at p. 15, l. 470 may not apply to the data used here. Likewise, the statement that peak finding with quartz alignment "helps normalize for instrumental and sample-related biases, including shielding effects" (p. 15, l. 473 to p. 16, l. 474) is not tested in the Results. Were the detrital samples depth-integrated, and which of the named mitigations were applied? GB-21 concerns the symbols of Fig. 1, GB-11 the placement of these limits, GB-62 the conditions of use. |
| Suggestion | State the sampling of the detrital samples in Sect. 3.4 or 4.2, and say at p. 15, l. 469 to p. 16, l. 476 which mitigations were applied in this study and which are recommendations. |
| Status | verified (search and figure labels on page images); assumption (that the pump samples were not depth-integrated), therefore asked |
| Severity | moderate |
| Source | S4, SD |

**GB-64 The Conclusions rest on the synthetic tests only; the natural-data tests and the comparison of the two schemes are not taken up.**

| Field | Content |
|---|---|
| Check | P15 |
| Location | p. 16, l. 477 to 489; p. 15, l. 450 to p. 16, l. 476; p. 10, l. 282 to 285 |
| Quotation | "Using synthetic forward-inverse experiments, we show that the true erosion pattern can be reliably recovered, and that the method is robust across a range of parameters." |
| Concern | Search in the Conclusions (p. 16, l. 477 to 489, `text.json`) for "natural", "real", "Gorner", "known mixture", "sub-catchment", "subcatchment", "Grenz", "zircon", "glaci": 2 hits, l. 488 ("sub-catchments" as an alternative classification) and l. 489 ("zircon U-Pb age distributions" as an alternative tracer); none reports a natural-data result. The Discussion takes up natural data once (p. 15, l. 462 to 463, see GB-46). Aims 1 and 2 of the natural tests (p. 10, l. 282 to 284) and their results (p. 13, l. 399 to 401; p. 14, l. 413 to 418) appear in neither section. The comparison of steepest descent and quasi-Newton announced in the Abstract (p. 1, l. 4 to 5) has 0 hits for "steepest", "quasi", "QN", "SD", "Newton" in p. 15, l. 450 to p. 16, l. 489. The Abstract states that "The application to real-world datasets further validates the practical utility and robustness of the model" (p. 1, l. 7 to 8), which the Conclusions do not carry. GB-58 concerns the strength of the verbs; GB-65 the outlook in the last paragraph of the Conclusions. Overlapping locations: GB-24 treats the design of the synthetic validation, GB-43 treats the missing prior and export estimate, GB-59 treats the novelty claim, GB-60 treats the claim on a broad tracer set, GB-61 treats the untested number of source areas, GB-62 treats the conditions of use, GB-63 treats the XRD mitigations; this entry concerns the omissions of the Conclusions. |
| Suggestion | Add to the Conclusions one sentence each on the QN against SD comparison as rephrased under GB-26, the agreement of the XRD fingerprints with the mapped lithologies (p. 13, l. 399 to 401) with its limits (GB-39), the subcatchment test with its limits (GB-40), and the zircon comparison as rephrased under GB-46. |
| Status | verified (search as stated) |
| Severity | moderate |
| Source | S4 |

**GB-65 The proposed extensions are untested, and the zircon proposal runs against the manuscript's own zircon result.**

| Field | Content |
|---|---|
| Check | P15 |
| Location | p. 16, l. 487 to 489; p. 15, l. 466; p. 14, l. 435; p. 15, l. 448 |
| Quotation | "Similarly, the method is not limited to XRD-derived fingerprints and can be applied to other types of tracer data, including zircon U-Pb age distributions or geochemical compositions." |
| Concern | Proposals of Discussion and Conclusions, each held against the manuscript: (1) source maps based on land use (p. 15, l. 466; p. 16, l. 488): not tested; "land use" occurs only there (search, p. 1 to 16, 2 hits). (2) Sub-catchments as source areas (p. 16, l. 488): not tested. (3) Zircon U-Pb age distributions (p. 16, l. 489): the manuscript's own zircon-only inversion was "highly unstable, with extreme erosion rate values (>8000 mm/y)" (p. 14, l. 435), and its average JS distance of 0.48 (p. 15, l. 448) lies in the range where the synthetic tests show a sharp rise of the uncertainty (below 0.55, p. 12, l. 352); the manuscript attributes the instability to missing zircon data for two units (p. 14, l. 430 to 434), but the proposal does not carry this condition. (4) Geochemical compositions: not tested, no own finding against it. For (1) the forward model requires a distinct fingerprint per source area, and fingerprint distinctiveness is stated as the strongest factor (p. 12, l. 363 to 364); whether land-use classes on the same lithology differ in XRD mineralogy is not shown (assumption, asked as a question). GB-64 concerns the omissions of the same section. Overlapping locations: GB-45 treats the incomplete three-way comparison, GB-47 treats the basis of the natural JS distances, GB-62 treats the conditions of use; this entry concerns the proposed extensions. |
| Suggestion | Phrase p. 15, l. 466 and p. 16, l. 487 to 489 as untested possibilities and attach the conditions the manuscript has shown: zircon fingerprints only where all units yield zircon ages and the average JS distance exceeds about 0.55; for land-use classes, state that their mineralogical distinctiveness must be checked first. |
| Status | verified for (2) and (3) and for the absence of tests; assumption for the mineralogy of land-use classes |
| Severity | moderate |
| Source | S4 |

**GB-66 The data availability statement covers only "the inversion tests" and does not refer to the raw XRD data, the processing parameters, the sample metadata or the zircon ages.**

| Field | Content |
|---|---|
| Check | P12 |
| Location | p. 16, l. 490; p. 9, l. 252 to 253; p. 9, l. 256 to 258; p. 13, l. 396 to 398; p. 13, l. 406 to p. 14, l. 407; p. 14, l. 423 to 424; p. 17, l. 522 to 523 |
| Quotation | "The data and codes used for the inversion tests in the study are available at https://doi.org/10.5281/zenodo.17120374" (p. 16, l. 490); "Zircon grains were extracted and U-Pb dated from both the source lithologies and the detrital sample collected on June 28, 2019, at 13:30, following the methodology described in (Belotti, 2021)." (p. 14, l. 423 to 424); p. 17, l. 523: "unpublished master’s thesis, 2021." |
| Concern | The manuscript provides a persistent DOI for data and code, which is the right place for them (PP-06). The statement, however, is limited by its own wording to what was "used for the inversion tests". Sect. 3.4 and 4.2 name further data sources that precede the inversion: (1) the raw diffractograms of the source and detrital samples (p. 9, l. 252 to 253; p. 13, l. 396 to 397); (2) the processing parameters that turn diffractograms into fingerprints: the 2θ windows of the 21 minerals (p. 9, l. 257 to 258), the quartz reference pattern (p. 9, l. 256 to 257) and the Peak Finder thresholds; (3) the sample metadata: locations of the source samples (Fig. 3b shows them only schematically), number and dates of the detrital samples at the Gorner-Grenz confluence (p. 13, l. 406 to p. 14, l. 407); (4) the zircon U-Pb ages of source lithologies and detrital sample (p. 14, l. 423 to 424), whose only cited source is an unpublished master's thesis (p. 17, l. 522 to 523), so method and age data have no public access route named anywhere. The manuscript has no appendix or supplement (PP-07). Whether the Zenodo record contains some of these sources could not be checked (PP-08); the finding concerns what the statement says. None of these data concern persons, so no reason for withholding is apparent. GB-43 concerns the export estimate and GB-19 the third-party map data, which the same statement does not mention; GB-16 the instrument settings; KK-27 the form of the thesis entry. Overlapping locations: GB-17 treats the unspecified processing and test-construction steps, KK-13 treats the panel reference to Fig. 3, GB-42 treats counts given only in figures, GB-53 treats the proportions in Fig. 11, 15 and 16, KK-22 treats the names of the subcatchment; this entry concerns the scope of the data statement. |
| Suggestion | Extend the statement at p. 16, l. 490 to list each data class with its access route: raw diffractograms, the table of 2θ windows with the RRUFF identifiers, the quartz reference pattern, the Peak Finder settings, sample coordinates and dates, the inferred geological map, the export estimate and the zircon U-Pb ages with a public reference or repository; if some are already in the Zenodo record, name them there. |
| Status | verified (wording of the statement and of the data sources at the given locations); Zenodo record contents and reachability not checked |
| Severity | moderate |
| Source | S2 |

#### Minor corrections

| ID | Location | Quotation | Replacement | Source |
|---|---|---|---|---|
| KK-25 | p. 16, l. 491 | "All authors (FDD, FH, BB, TA)" | "All authors (F.D.D., F.H., B.B., T.A.)", the form used at p. 16, l. 491 to 494 | S2, S4 |
| KK-26 | p. 17, l. 521 | "Bearth, P.: Blatt 535 Zermatt - Geologischer Atlas der Schweiz 1:25 000, 1953." | "Bearth, P.: Blatt 535 Zermatt, Geologischer Atlas der Schweiz 1:25 000, [publisher], [place], 1953."; publisher and place not verified | S4 |
| KK-27 | p. 17, l. 522 to 523 | "Master’s thesis, University of Lausanne, unpublished master’s thesis, 2021." | "unpublished Master’s thesis, University of Lausanne, 2021."; GB-66 concerns the access to the zircon data of this source | S4 |
| KK-28 | p. 19, l. 578 | "[No title found]" | "Landscape indicators of human impacts to riverine systems" (record at experts.illinois.edu: Aquatic Sciences 64(2), 118 to 128, 2002, DOI 10.1007/s00027-002-8060-2) | S4 |
| KK-29 | p. 19, l. 583 | "Gjems, O.: Studies on clay minerals and clay-mineral formation in soil profiles in Scandinavia, 1967." | "Gjems, O.: Studies on clay minerals and clay-mineral formation in soil profiles in Scandinavia, [series, volume, pages, publisher, place], 1967."; unlike the other book and series entries the entry has no place of publication; details not verified | S4 |
| KK-30 | p. 19, l. 599 to 600 | "Lafuente, B., Downs, R., Yang, Y., and Stone, N.: The power of databases: the RRUFF project, Highlights in Mineralogical Crystallography, pp. 1" | "Lafuente, B., Downs, R. T., Yang, H., and Stone, N.: The power of databases: the RRUFF project, in: Highlights in Mineralogical Crystallography, edited by Armbruster, T. and Danisi, R. M., W. De Gruyter, Berlin, 1-30, 2015." (as recommended at rruff.info; the publisher record at experts.azregents.edu gives 2016 and pp. 1-29, so year and pages should be checked against the volume) | S4 |
| KK-31 | p. 20, l. 612 to 613 | "Oxford University Press, New-York, 378" | "Oxford University Press, New York, 1990.", with the page range moved to the citation at p. 9, l. 265 ("Moore and Reynolds, 1990, pp. 378-379"), since the entry is a book | S4 |
| KK-32 | p. 20, l. 635 | "ISBN 9780898715729 9780898717921" | "ISBN 9780898715729" (one ISBN, as in the other book entries) | S4 |

#### Verification log

| ID | Check | Checked | Values | Result |
|---|---|---|---|---|
| PP-37 | P4 | Citations against the reference list in both directions, years, name spellings, "et al." | 64 entries (p. 17, l. 501 to p. 21, l. 653); 64 distinct cited keys in p. 1 to 16 (63 by regular expression plus "E., 2009"); every entry cited, every citation has an entry; years agree; two-author entries cited with "and" (11 keys), three or more with "et al."; the 53 keys cited in the Introduction occur twice because of GB-04 | no finding except GB-05 and GB-07; DOIs not resolved (optional check) |
| PP-38 | P15 | Assignment of Discussion and Conclusion statements to Results | p. 15, l. 457 distinct signatures to p. 12, l. 351 to 354 and l. 363; p. 15, l. 459 to 460 map delineation to p. 11, l. 336 to p. 12, l. 342 and l. 364; p. 15, l. 464 to 465 b) to p. 12, l. 363 to 364; p. 16, l. 483 to 484 resolution and covariance to p. 10, l. 299 to 304 and p. 11, l. 318 to 319; p. 16, l. 478 to 481 to Sect. 3.1 to 3.4 | consistent statements: no finding; statements without or against Results in GB-46, GB-58 to GB-61 and GB-43 |
| PP-39 | P15 | Each proposal of Discussion and Conclusions held against own results | a) well-constrained lithology (p. 15, l. 464) against scenario 1: consistent, see GB-62; b) mineralogical contrast (p. 15, l. 464 to 465) against p. 12, l. 351 to 354: consistent; c) multiple XRD tracers: GB-60; land-use maps and sub-catchments: GB-65; zircon: GB-65; storage caution: GB-62; depth-integrated samples: GB-63; same protocol for source and detrital samples (p. 15, l. 472 to 473) against p. 9, l. 250 to 253: consistent | proposals b), geochemical tracers and same protocol without finding |
| PP-40 | P15 | Key terms and frame of Introduction and aims taken up in Discussion and Conclusions | searches in p. 15, l. 450 to p. 16, l. 489: "uncertaint" 1 hit (l. 461), "covariance" 1 (l. 483), "resolution" 3 (l. 458, 461, 483), "fingerprint" 8, "stabil" 3, "cost" and "time" 0, "steepest", "quasi", "QN", "SD", "Newton" 0, "sharp" 0; Bayesian frame (p. 2, l. 43 to 57) not taken up, but applied in Sect. 3.2 to 3.3 | Bayesian frame: no finding (hierarchical label in GB-10); cost and time in GB-02; scheme comparison and natural tests in GB-64 |
| PP-41 | P16 | Language and form of Segment 4 on the page images p. 15 to 21 | Discussion, Conclusions, Code and data availability (p. 16, l. 490), Author contributions (l. 491 to 495), Competing interests (l. 496), Acknowledgements (l. 497 to 499), 64 reference entries for uniformity | findings KK-25 to KK-32 and the grammar points included in GB-46 and GB-59; extraction artefacts (for example "108 336" with thin space, "Bomb-fallout137 Cs" with superscript 137 at p. 20, l. 639) are no finding |
| PP-42 | P16 | Line numbers of the locations of Segment 4 and of the Introduction at the printed margin numbers | counted on the page images from the nearest printed number: l. 9 and l. 76 (headings, p. 1 and 3), l. 477 (p. 16, between 475 and 480), l. 496 to 499 (p. 16, after 495; the count up to 500 on p. 17 closes), l. 567 to 568 (p. 18, from 565), l. 578 and l. 583 (p. 19, from 575 and 580), l. 597 to 600 (p. 19, from 595 and 600) | confirmed |
| PP-43 | P32 | Statements "validated", "confirms", "robust" against an independent check sample | "validate" p. 1, l. 3; p. 3, l. 69 and l. 74; p. 15, l. 451; "confirms" p. 14, l. 415; no independent re-measurement or check sample reported | no finding of its own; raised in GB-58, GB-39 and GB-40 |
| PP-44 | P16 | Merging step: every location listed by `formatpruefung.py --fundorte` (page boundary, line on another page in `text.json`, uncertain line) counted on the page image from the nearest printed margin number | 101 listed locations, checked on the page images p. 1 to 16, 20 and 21: p. 1 from 5 (l. 1, 3, 4); p. 2 from 30 and 60 (l. 27, 61); p. 3 from 65 and 75 (l. 62 is the first line of p. 3; l. 63, 70, 94); p. 4 from 125 (l. 126, 128); p. 5 from 150, 155, 160 (l. 150 to 152, 157 to 158; Eq. 2 at 160); p. 6 from 175, 180, 185 (Eq. 5 at 175; l. 176 to 178, 181, 184; Eq. 8 at 186); p. 7 from 190 and 200 (Eq. 9 at 189, Eq. 14 at 201); p. 8 from 215, 220, 225, 235 (l. 213, 214, 223, 236; Eq. 19 at 219, Eq. 20 at 225, Eq. 22 at 239); p. 9 from 245 and 270 (l. 243, 244, 272, 273); p. 10 from 275 (l. 274); p. 11 from 335 (l. 337); p. 12 from 370 (l. 373); p. 13 from 405 (l. 406); p. 14 from 410, 435, 440 (l. 407, 409, 435 to 439); p. 15 from 440 and 445 (l. 441 to 444); p. 16 from 495 (l. 498, 499); p. 20 from 615 (l. 612, 613); p. 21 from 650 (l. 649) | all confirmed except one: "p. 3, l. 61" in GB-62 corrected to "p. 2, l. 61 to p. 3, l. 63"; `text.json` deviates from the page image at p. 6 (l. 181 given as 180, Eq. 8 placed on p. 7), p. 11 (l. 337 given as 336), p. 12 (l. 373 placed on p. 13) and p. 5 (Eq. 2 placed on p. 6) |
| PP-45 | P2, P38 | Merging step: wording check of quotations and embedded statements | every quotation from the running text searched in `text.json` after normalising spaces and line-end hyphens (script `zf/zitate.py`); quotations from figures read on the page images p. 22 to 37; counts and percentages recomputed with Python; search claims rerun (for example "pixel" 14 hits, "export" 5, "stabil" 10, "sharp" 5, "replicat" 0, "confiden" 0, "multiple" or "several" 9) | wording confirmed; corrected during merging: line of the over-smoothing sentence (l. 373, not l. 372), hit count for "pixel" (14), and the scope of searches to the stated page ranges; the 158 pairs of entries with overlapping locations listed by `formatpruefung.py --paare` were each decided: none concerns the same subject at the same place, so all were kept separate with a mutual reference |

## Optional checks

| Area | What it needs | Responsible | Run |
|---|---|---|---|
| DOI resolution | one request per reference entry with a DOI | `science-quellenapparat-pruefung` | no |
| Citation style | the name of the style | `science-zitierstil-harvard-ctr` or the style rules of the journal | no |
| AI statement against publisher policy | the policy of the target publisher | this review, on request | no |
| Relation to the authors' own prior work | the authors' prior work | this review, on request | no |
| Journal requirements | the author guidelines of the target journal | this review, on request | no |
| Scientific correctness | access to the sources of the checked statements and a selection of sections | `science-faktenbeleg-pruefung`, `geo-frage-belegbasiert-klaeren` | no |

## Limits of this review

- Checked version: egusphere-2025-4695.pdf, 37 pages, SHA-256 9c80676054f96ecd6f00f4d2a8b5ba568e03c6949e3856d363ac1c4abb42e7bd.
- Unreadable sources: Das et al. (2023), full text (summary of the abstract only); Haddadchi et al. (2013), Yang et al. (2025), Fathabadi and Jansen (2022), Niu et al. (2020), Blaen et al. (2016) and Asadi et al. (2025), no abstract available; Wilson et al. (1993), metadata only; Avdeev et al. (2011), not readable; the UNESCO report cited as "E., 2009" (archived copy rate-limited); the Zenodo record https://doi.org/10.5281/zenodo.17120374 (HTTP 429); Gjems (1967) and Bearth (1953), publication details not verified.
- Findings with status assumption: 0 of 66 with assumption as the central statement; 7 of 66 with assumption for a partial statement, each put as a question (GB-37, GB-41, GB-43, GB-59, GB-62, GB-63, GB-65).
- Optional checks run: 0 of 6.
- Omitted instances: none; the six review instances ran as separate agents.
- Discarded findings: 0; no instance finding lacked a mandatory field, and none was refuted on the manuscript. 171 instance items (95 substantive findings, 76 minor corrections) were merged into 65 substantive findings and 30 minor corrections; 1 substantive finding (GB-37) and 2 minor corrections (KK-09, KK-18) were added by the merging step from notes outside the checklists, and a third note became part of KK-06.
- Literature statements rest on what the instances read (abstracts, records or publisher pages, as named in each Status field); full texts were read only where stated.
