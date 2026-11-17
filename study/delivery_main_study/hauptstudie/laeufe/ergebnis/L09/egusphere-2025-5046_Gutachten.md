# Review report: Quantifying Southern Hemisphere dust sources during the Last Glacial-Interglacial Transition using rare earth elements in the EPICA Dome C ice core

| Field | Value |
|---|---|
| Manuscript | Boxho, S., Vanderstraeten, A., Mattielli, N., Laruelle, G. G., Bory, A., Gabrielli, P., Bonneville, S. (2025): Quantifying Southern Hemisphere dust sources during the Last Glacial-Interglacial Transition using rare earth elements in the EPICA Dome C ice core. EGUsphere preprint, https://doi.org/10.5194/egusphere-2025-5046 |
| Checked version | egusphere-2025-5046.pdf, 29 pages, SHA-256 f598b53d01e375844cfb549eb05b9a3407bb30cae553e603c125d5f14886c722; supplement egusphere-2025-5046-supplement.pdf, 22 pages, SHA-256 759cfa14195948f5772d3d6d696081932424f4296e51c812415527ed3b108ea6 |
| Date | 2026-10-17 |
| Language | English |
| Review instances | Segments 1 to 4, figures, study design. The six review instances ran as separate agents, each without context from the others; their results were merged here. No instance was omitted. |
| Note | Line numbers are the printed margin numbers of the preprint (every fifth number is printed), counted on the page images from the nearest printed number. The supplement has no line numbers; locations there give supplement page and element. Supplement pages are written "Suppl. p.". Calculations were run with Python on values read from the manuscript and the supplement. |

## Summary

The manuscript is a re-analysis study. It applies a numerical unmixing model (DEPOT: non-negative least squares on 13 UCC-normalised rare earth elements, implemented with the MATLAB function lsqnonneg, with 2000 Monte Carlo runs per sample over analytical and correction-factor uncertainties) to the published REE dataset of the EPICA Dome C ice core (Gabrielli et al., 2010: 294 samples, 279 usable). Each sample is fitted against a database of 217 source patterns grouped into seven potential source areas (Patagonia, Central Western Argentina, Puna-Altiplano, Southern Africa, Australia, New Zealand, Antarctica). Samples with a fit correlation below R = 0.67 are excluded, leaving 241 samples from 33.7 to 2.9 kyr BP. The record shows Patagonia dominant during MIS3, the LGM and HS1 (period means 65.7 to 74.8 %), a decline after about 14.5 kyr BP, and a Holocene mean of 49.0 % Patagonian dust with 23.1 % from Australia (Table S5). The authors check the result by a forward calculation of Sr and Nd isotope ratios (Eq. 3 and 4) against published ice-core values, compare it with their earlier EDML record, and attribute the deglacial shift to the flooding of the Patagonian shelf and hydrological changes in the source regions.

## Strengths

1. The per-sample model output is published in Table S1 (241 rows with medians per PSA and R), and the period means of Table S5 are its arithmetic means: three instances recomputed every EDC period mean from Table S1 to within 0.05 to 0.1 points, and the stated sample balance (294, 279, 241, 86 %) and the mean R of 0.852 were reproduced (PP-11, PP-24). A reader can therefore recheck every period statement against the sample level, which is what made most of the numerical findings of this review possible (GB-30, GB-49).
2. The Monte Carlo design propagates the analytical uncertainty of the ice-core REE data and the uncertainty of the leaching correction into every fit, and an explicit fit-quality criterion removes the samples whose patterns the authors judge distorted near the detection limit (PP-11, PP-14). The design thus addresses the two main error sources of the input data; what it still lacks is the reporting of the resulting spread and a calibrated threshold (GB-18, GB-20).
3. The Sr and Nd forward calculation from the modelled contributions (Eq. 3 and 4, Table S3) gives an independent plausibility check of the REE unmixing that a reader can reproduce: one plotted symbol was recomputed exactly from Table S1 and Table S3, and the modelled LGM values agree with the EDC LGM values quoted in the text (PP-44, GB-38). Its reach for the interglacial is limited (GB-38).
4. Several limits are disclosed where the data are introduced (the sampling gap between 21.7 and 27.3 kyr BP, the removal of Gd), and the period limits, figure bands and the EDC minus EDML bars of Figure 4 agree with the stated period definitions and with Table S5 (PP-15, PP-28, PP-48). This consistency between figures and tables lets a reader locate the disagreements that remain in the text (GB-48, GB-50).

## Weaknesses

1. Whether the unmixing can identify source contributions at all is not shown. Each sample gives 13 equations for 217 non-negative unknowns, no recovery test with known mixtures is reported, the R threshold does not correspond to the stated significance level, the published Antarctic end-members do not look UCC-normalised, and the isotope check for the interglacial uses cores other than EDC (GB-13, GB-20, GB-16, GB-38). Suggestion: add recovery and leave-one-out tests of the exact configuration, a null distribution of R, a comparison with an unmixing on regional mean end-members, and a validation against EDC isotope data for the same intervals.
2. Relative shares are interpreted as absolute inputs and as climatic signals. The rise of low-latitude shares is read as greater inputs although total deposition fell by an order of magnitude, the larger Holocene variability coincides with lower fit quality, lower concentrations and denser sampling, the ACR assemblage lies within the glacial range, and the conclusion states the mechanisms as demonstrated (GB-02, GB-25, GB-37, GB-52). Suggestion: report PSA fluxes and Monte Carlo spreads, test the period differences, and phrase the mechanisms as hypotheses where the data do not test them.
3. The EDC and EDML comparison (research aim 4) is not made on a common basis. The EDML values in Table S5 differ from the source the Introduction summarises, the two records come from different model configurations and possibly different chronologies, the Holocene bars compare different windows, and the ACR and YD values in the text are swapped (GB-06, GB-17, GB-48, GB-50). Suggestion: rerun EDML with the present configuration on a common timescale and window, and report differences with uncertainty.
4. Reproducibility and internal consistency are limited. The input REE data, correction factors and code are not available although the data statement says so, the published source database differs from the described one in counts and contains duplicate, misplaced and possibly mistyped entries, Figure S3 does not show the values of Table S1, and several numbers in the text disagree with Tables S1 and S5 (GB-54, GB-15, GB-21, GB-44, GB-30, GB-40, GB-49). Suggestion: deposit inputs, code and full model output in a public repository, reconcile Table S2 with the Methods, regenerate Figure S3, and recheck every number in the text against the tables.

## Findings by segment

### Segment 1: Abstract, Introduction (p. 1 to 3, l. 1 to 98)

#### Substantive findings

**GB-01 The priority claims ("novel", "for the first-time", "the first", "The only") are not backed by a described literature search, and the unrestricted claim in the Abstract conflicts with earlier quantifications the manuscript itself cites.**

| Field | Content |
|---|---|
| Check | P28 |
| Location | p. 1, l. 17; p. 1, l. 19 to 20; p. 3, l. 74 to 75; p. 7, l. 220 to 221; p. 12, l. 403; p. 14, l. 472 to 473 |
| Quotation | "we quantify for the first-time contributions from key Southern Hemisphere dust sources"; "we presented the first quantitative apportionment algorithm based on REE pattern fitting"; "The only continuous and quantitative dust provenance record in EA available for direct comparison" |
| Concern | The claims in the Discussion and Conclusion are restricted to EDC and the LGIT, and the review found no earlier percentage apportionment at EDC. None of the claims names a search basis: a search of the whole manuscript (text layer, p. 1 to 29) for "search", "Web of Science", "Scopus", "Google Scholar", "literature review" and "to our knowledge" gives 7 hits, all inside journal names in the reference list (p. 17, l. 556 and 570; p. 18, l. 620; p. 19, l. 681 and 700; p. 20, l. 724; p. 22, l. 823). The Abstract claim in l. 19 to 20 is not restricted to EDC, whereas the manuscript itself reports earlier quantifications of Southern Hemisphere source contributions: for EDML by Vanderstraeten et al. (2023) (p. 3, l. 74 to 81), for East Antarctica by Coppo et al. (2022), who "estimated LGM dust composition over EA as 64% from SSA, 15% from Antarctica, 11% from AUS" (p. 9, l. 278), and model estimates (p. 9, l. 275 to 277; p. 10, l. 319 to 323). What is new at EDC is the quantification by source: the change in EDC dust composition across the LGIT was reported before from the same REE dataset by Gabrielli et al. (2010) and from lithium by Siggaard-Andersen et al. (2007) (see GB-07). The priority claim for the algorithm (l. 74 to 75) could not be tested within the search budget. The word "continuous" in the same sentences is treated separately in GB-36, the hyphenation in l. 19 in KK-02. |
| Suggestion | In p. 1, l. 19 to 20 restrict the claim, for example "we provide the first continuous quantification of source contributions at EDC across the LGIT". After p. 3, l. 87 either state the search basis (databases, terms, date) or soften the priority claims to "to our knowledge", and name Gabrielli et al. (2010) and Siggaard-Andersen et al. (2007) as earlier reports of the EDC shift whose sources this study quantifies. |
| Status | Absence of a search description verified (text search, page images p. 1, 3, 7, 12, 14); conflict of l. 19 to 20 with the cited quantifications verified (p. 3, 9, 10); Gabrielli et al. (2010) verified (full text, author copy of the published article, https://bpcrc.osu.edu/sites/default/files/2020-12/QSR Gabrielli 2010.pdf); Siggaard-Andersen et al. (2007) verified for the abstract (https://www.iceandclimate.nbi.ku.dk/publications/papers/abstracts/abstract_10/) |
| Severity | moderate |
| Source | S1 |

**GB-02 Rising relative shares of low-latitude sources are interpreted as greater inputs and amplified emissions, although total deposition fell by more than an order of magnitude.**

| Field | Content |
|---|---|
| Check | P21 |
| Location | p. 1, l. 23 to 24; p. 13, l. 440 to 443; p. 2, l. 63; Figure S2, panel A (Suppl. p. 4) |
| Quotation | "After ~14.5 kyr BP, the dust assemblage shifted toward greater inputs from low-latitude"; "which likely amplified dust emissions and transport from these sources" |
| Concern | All results are shares of total deposition. The manuscript itself states that interglacial dust fluxes are "up to 25 times lower than LGM fluxes" (p. 2, l. 63), and Figure S2 A shows the drop of the total flux. With the Table S5 shares and the factor 25 of l. 63, the Holocene to LGM ratio of the absolute Australian input is 23.1 / 10.2 / 25 = 0.09 (about 11 times less), of SAF 10.7 / 6.3 / 25 = 0.07 (about 15 times less) and of PAP 11.0 / 3.6 / 25 = 0.12 (about 8 times less) (Python). Under normalisation to flux, "greater inputs" (l. 23) and "amplified dust emissions" (l. 443) would reverse: all low-latitude sources would deliver less dust to EDC. Elsewhere the manuscript speaks of a "relative increase" (p. 14, l. 463). The causal attribution to increased low-latitude aridity (research aim 3, p. 3, l. 94 to 95) cannot be read from relative shares. The missing PSA fluxes themselves are GB-19. Since the statement answers research aim 3 and appears in the Abstract, and its direction changes under flux normalisation, the finding is major. |
| Suggestion | Report absolute PSA fluxes (GB-19) and phrase the Abstract (l. 23 to 24) and p. 13, l. 440 to 443 in terms of relative shares, or show from the fluxes that low-latitude inputs increased. |
| Status | Shares and the cited factor verified at the page images (p. 1, 2, 13; Table S5, Suppl. p. 22); absolute ratios inferred (own calculation with the factor 25 of l. 63, which is a literature value and was not measured on EDC fluxes in this review) |
| Severity | major |
| Source | S3 |

**GB-03 Two background statements in the Introduction are attributed to sources whose archive or subject, as far as read, differs from the statement.**

| Field | Content |
|---|---|
| Check | P13 |
| Location | p. 2, l. 36 to 40; p. 2, l. 51 to 52 |
| Quotation | "Over recent decades, studies on these ice cores have revealed the connection between dust fluxes, ocean export productivity, and the development of deep glaciations"; "changes in Southern Hemisphere westerly winds, which play a crucial role in atmospheric and oceanic circulation (Engelbrecht et al., 2019)" |
| Concern | (a) The first sentence is supported by Martínez-García et al. (2014) as to the link itself, but that study analysed "a sediment core from the Subantarctic Atlantic" using foraminifera-bound nitrogen isotopes; its abstract does not mention an ice-core study, while the sentence presents the link as a result of "studies on these ice cores". (b) Engelbrecht et al. (2019) is a dynamical downscaling of LGM temperature and rainfall over southern Africa; its abstract does not mention the Southern Hemisphere westerlies or their role in atmospheric and oceanic circulation. Only the abstracts were readable. Question to the authors: does the full text of Engelbrecht et al. (2019) contain the general statement on the westerlies, or was another work intended? |
| Suggestion | p. 2, l. 36 to 37: write "studies combining these ice-core dust records with marine sediment records have revealed ..." or cite an ice-core study for this link. p. 2, l. 52: cite a work on the role of the westerlies in atmospheric and oceanic circulation, or limit the citation of Engelbrecht et al. (2019) to southern African LGM climate. |
| Status | (a) verified for the abstract (BORIS Bern record, https://boris.unibe.ch/57917); that the full text makes no ice-core attribution: inferred. (b) verified for the abstract (https://asu.elsevierpure.com/en/publications/downscaling-last-glacial-maximum-climate-over-southern-africa/); for the full text: assumption, hence the question |
| Severity | minor |
| Source | S1 |

**GB-04 The iron-fertilisation frame of the Introduction has no research aim, measurement or result, and returns only as a closing phrase.**

| Field | Content |
|---|---|
| Check | P10, P15 |
| Location | p. 2, l. 37 to 52; p. 15, l. 490 to 491 |
| Quotation | "identifying and quantifying the contributions of individual PSA is essential to help better constrain models of dust-driven iron fertilization"; "with implications for biogeochemical fluxes" |
| Concern | The Introduction motivates the study with dust-borne iron fertilisation, pCO2 and inter-source differences in iron content and solubility (p. 2, l. 37 to 51). None of the four aims (p. 3, l. 91 to 98) addresses it, and no iron estimate is made. Search of p. 1 to 15 for "iron", "fertiliz", "biogeochem" and "CO2" (case-insensitive, hits inside "Environnement" in the affiliations excluded): hits only at p. 2, l. 38, 40, 41, 42, 47 and 50 and p. 15, l. 491. The closing statement on biogeochemical fluxes therefore has no place in the Results or the Discussion. This finding is separate from GB-03, which concerns the source of the first sentence of the same paragraph, and from GB-05, which concerns the pCO2 numbers. |
| Suggestion | Either add a short paragraph to Section 4 on what the new provenance record implies for the iron supply to the Southern Ocean (using published iron content and solubility per PSA), or shorten the motivation in p. 2, l. 37 to 52 to what the study addresses and delete "biogeochemical fluxes" from p. 15, l. 491. |
| Status | verified (search as stated; wording at the page images p. 2 and 15) |
| Severity | minor |
| Source | SD, S4 |

**GB-05 The pCO2 range "~20 to 40 ppmv" attributed to Lambert et al. (2015) and Lambert et al. (2021) exceeds both cited sources at its upper end.**

| Field | Content |
|---|---|
| Check | P13 |
| Location | p. 2, l. 40 to 42 |
| Quotation | "Enhanced iron delivery by atmospheric dust during glacial periods are modelled to have lowered the atmospheric pCO2 by ~20 to 40 ppmv" |
| Concern | The qualitative part is supported: both sources attribute part of the glacial CO2 drawdown to dust-borne iron fertilisation. The numbers are not. Lambert et al. (2015) state that "Iron fertilization reduced LGM atmospheric CO2 levels by 20 ppm". Lambert et al. (2021) give "The model-calculated range of CO2 change for global-scale IF is between 12 and 29 ppmv"; their Table 2 gives global LGM values from 8.9 to 33.1 ppmv for six dust data sets (Python). Neither source gives 40 ppmv for iron fertilisation; the only "40" values are a share ("up to 40%" of the glacial difference, cited in Lambert et al., 2015) and a different mechanism in Lambert et al. (2021). Is the upper bound taken from the share? "a significant portion" in the same sentence is consistent with about 20 ppm of 80 to 100 ppm, i.e. 20 to 25 % (Python). The verb agreement in the same sentence is KK-06; the frame as a whole is GB-04, the preceding citation GB-03. |
| Suggestion | In p. 2, l. 41 replace "~20 to 40 ppmv" by the range the cited sources give, for example "by ~10 to 30 ppmv", or add the source of the 40 ppmv value. |
| Status | verified for Lambert et al. (2015) (full text, https://agupubs.onlinelibrary.wiley.com/doi/full/10.1002/2015GL064250, journal version) and Lambert et al. (2021) (full text PDF of the published version, https://boa.unimib.it/retrieve/e39773b7-1d77-35a3-e053-3a05fe0aac26/Lambert_2021_EPSL_Dust-iron-CO2.pdf); the share of 20 to 25 % is inferred (own calculation) |
| Severity | moderate |
| Source | S1 |

**GB-06 The EDML values of Table S5, on which the EDC and EDML comparison rests, disagree with the EDML results of Vanderstraeten et al. (2023) that the Introduction reports.**

| Field | Content |
|---|---|
| Check | P13 |
| Location | p. 3, l. 77 to 83; Table S5 (Suppl. p. 22), EDML block, column PAT; p. 13, l. 423 to 424 |
| Quotation | "up until ~14.5 kyr BP when a sudden drop in Patagonian contribution (below 50% on average) was evidenced"; "EDC appears to receive substantially less PAT dust (-14%) but higher contributions of Australian dust (+12%) than EDML" |
| Concern | The summary in p. 3, l. 77 to 87 agrees with the abstract of Vanderstraeten et al. (2023): before 14.5 kyr BP Patagonia yields about 68 % of total deposition, afterwards "Patagonia dropped below 50 % on average", and in the early Holocene the Patagonian contribution is about 50 % on average. The EDML values in Table S5 do not agree with this: PAT is 62.5 (ACR), 58.4 (YD) and 62.7 (Early Holocene), so no weighting of the periods after 14.7 kyr BP can give a value below 50; before 14.5 kyr BP Table S5 gives 73.7 (LGM) and 71.6 (HS1), both above about 68 % (values at the page image Suppl. p. 22). The Holocene comparison rests on these values: 49.0 minus 62.7 gives the "-14%" of l. 424. With the source value of about 50 %, the PAT difference would be minus 1.0 (EDC Holocene 49.0) or minus 2.9 (EDC Early Holocene 47.1) (Python). Possible resolutions, as questions: (a) Were the EDML values recomputed with the present configuration (13 REE, 217 patterns, p. 5, l. 144 to 145)? Then the manuscript should say so (see GB-17 for the configuration difference). (b) Do the source and Table S5 use different statistics? (c) Is it a transcription error? The comparison window of l. 423 to 424 is treated separately in GB-48. Because research aim 4 and the Abstract statement on regional differences (p. 1, l. 27 to 29) depend on which EDML values are correct, the finding is major. |
| Suggestion | State in Section 4.4 (p. 12, l. 403 to 409) and in the caption of Table S5 where the EDML values come from (published values of Vanderstraeten et al., 2023, or a rerun with the present database and REE set). If rerun, report both sets and revise p. 3, l. 79 to 80 accordingly. |
| Status | Source statements verified for the abstract (record of Vanderstraeten et al., 2023, https://marineinfo.org/id/publication/382930; the full text was not accessible); Table S5 values and the text verified at the page images (Suppl. p. 22; p. 3, 13); differences inferred (Python); the cause is an assumption, put as questions |
| Severity | major |
| Source | S1 |

**GB-07 Three studies of dust provenance at Dome C that anticipate the deglacial shift or report Antarctic and non-Australian signatures in interglacial dust are missing from the reference list.**

| Field | Content |
|---|---|
| Check | P14 |
| Location | p. 3, l. 91 to 93; p. 10, l. 329 to 330; Table S5 (Suppl. p. 22), EDC, row Holocene, columns AUS and ANT |
| Quotation | "particularly during the Holocene for which there is no consensus (e.g. Paleari et al., 2019; Coppo et al., 2022; Delmonte et al., 2007)"; "our results do not indicate significant Antarctic contributions to EDC" |
| Concern | The manuscript confronts the Antarctic component of Coppo et al. (2022) with a transport argument (p. 10, l. 330 to 334) but does not cite three studies from the same core or site. Check against the reference list (p. 16 to 22, text layer): "Siggaard" occurs once, as co-author of Fischer et al. (2007); "Vallelonga" as first author only for Vallelonga et al. (2002); the Delmonte entries are 2004, 2007, 2008, 2010, 2017 and 2020. (1) Siggaard-Andersen, M.-L., Gabrielli, P., Steffensen, J.P., Strømfeldt, T., Barbante, C., Boutron, C., Fischer, H., Miller, H., 2007. Soluble and insoluble lithium dust in the EPICA DomeC ice core: Implications for changes of the East Antarctic dust provenance during the recent glacial-interglacial transition. Earth and Planetary Science Letters 258, 32 to 43: at EDC the changes over the transition "are indicative of a change in the major dust source areas", which anticipates the timing result of p. 7, l. 233. (2) Vallelonga, P., Gabrielli, P., Balliana, E., Wegner, A., Delmonte, B., Turetta, C., Burton, G., Vanhaecke, F., Rosman, K.J.R., Hong, S., Boutron, C.F., Cescon, P., Barbante, C., 2010. Lead isotopic compositions in the EPICA Dome C ice core and Southern Hemisphere Potential Source Areas. Quaternary Science Reviews 29, 247 to 255, https://doi.org/10.1016/j.quascirev.2009.06.019: Section 5.4 states that the data suggest "that Australian dust is not the main component of dust deposited in Antarctic ice", and Section 5.5 that the EDC samples indicating more than 50 % input from a local Antarctic dust source correspond to interglacial periods (the source cautions that volcanic Pb limits interglacial attributions). This contradicts the Holocene result of 23.1 % AUS and 0.3 % ANT (Table S5). (3) Delmonte, B., Baroni, C., Andersson, P.S., Narcisi, B., Salvatore, M.C., Petit, J.R., Scarchilli, C., Frezzotti, M., Albani, S., Maggi, V., 2013. Modern and Holocene aeolian dust variability from Talos Dome (Northern Victoria Land) to the interior of the Antarctic ice sheet. Quaternary Science Reviews 64, 76 to 89, https://doi.org/10.1016/j.quascirev.2012.11.033: Holocene and modern Dome C dust is "consistent with the isotopic signature of Antarctic Ferrar Dolerites and Beacon sandstone". The Antarctic end-members of the database are treated in GB-16; the conclusion's silence on the Holocene question is GB-08. Overlapping location with GB-06 (the EDML values of Table S5 against the published EDML record); this finding concerns missing literature on Dome C provenance. |
| Suggestion | Add the three works to the state of research in p. 3, l. 88 to 93 and discuss them in Section 4.3 (p. 10, l. 324 to 334): explain why the REE unmixing yields almost no Antarctic and a 23 % Australian Holocene share where the Pb isotope record of Vallelonga et al. (2010) points to minor Australian and, in some interglacial samples, a majority local Antarctic input. |
| Status | Vallelonga et al. (2010) verified (full text, author copy of the published article, https://bpcrc.osu.edu/sites/default/files/2020-12/QSR Vallelonga 2010.pdf); Delmonte et al. (2013) verified (full text PDF, https://www.taldice.org/pub/taldice/2013_Delmonte_QSR.pdf); Siggaard-Andersen et al. (2007) verified for the abstract (https://www.iceandclimate.nbi.ku.dk/publications/papers/abstracts/abstract_10/); absence from the reference list verified (text search) |
| Severity | moderate |
| Source | S1 |

**GB-08 Research aim 2, the isotopic validation, and the Holocene question for which aim 1 states that there is "no consensus" are not taken up again in the Conclusion.**

| Field | Content |
|---|---|
| Check | P15 |
| Location | p. 3, l. 91 to 94; p. 14, l. 472 to p. 15, l. 492 |
| Quotation | "(2) confronting and validating the EDC results from our REE pattern-based model against Sr-Nd isotopic data published in the literature" |
| Concern | Search in the Conclusion (l. 472 to 492, text layer, case-sensitive for "Sr" and "Nd") for "isotop", "Sr", "Nd", "Holocene", "consensus" and "Paleari": 0 hits each. The Conclusion therefore does not state the outcome of aim 2, and it does not say how the EDC Holocene record bears on the lack of consensus named in aim 1. In the Discussion (l. 219 to 470) Paleari et al. (2019) is cited 0 times; of the three works named for the lack of consensus, only Coppo et al. (2022) is compared with the Holocene results (p. 10, l. 324 to 330). The same sentence of the aims is the location of GB-07, which concerns missing literature rather than the Conclusion. |
| Suggestion | Add to the Conclusion one sentence on the isotopic consistency check with its limitation (GB-38), and one sentence that places the EDC Holocene provenance relative to Paleari et al. (2019), Delmonte et al. (2007) and Coppo et al. (2022); add the corresponding comparison to Section 4.3. |
| Status | verified (search in the text layer; wording at the page images p. 3, 14 and 15) |
| Severity | moderate |
| Source | S4 |

#### Minor corrections

| ID | Location | Quotation | Replacement | Source |
|---|---|---|---|---|
| KK-01 | p. 1, l. 15 | "Dust deposits in ice cores provides" | "Dust deposits in ice cores provide" | S1 |
| KK-02 | p. 1, l. 19 | "for the first-time" | "for the first time"; the scope of the claim is GB-01 | S1, S4 |
| KK-03 | p. 1, l. 20 | "During the Marine isotope 3 (MIS3)" | "During Marine Isotope Stage 3 (MIS3)", as in p. 6, l. 184 to 185 (page images p. 1 and 6); overlapping location with GB-01 (the priority claims), where a different point is treated | S1, S2 |
| KK-04 | p. 1, l. 24 | "sources - Australia, Southern Africa, and the Puna-Altiplano - culminating" | "sources (Australia, Southern Africa and the Puna-Altiplano), culminating"; spaced hyphens used as parenthetical dashes; the content of the sentence is GB-02 | ZF |
| KK-05 | p. 1, l. 27 | "Comparison with the EDML ice core" | "Comparison with the EPICA Dronning Maud Land (EDML) ice core"; search for "Dronning" in the text layer: 2 hits, both in reference titles (p. 21, l. 789 and 813); EDML is not expanded elsewhere in the text | ZF |
| KK-06 | p. 2, l. 40 to 41 | "Enhanced iron delivery by atmospheric dust during glacial periods are modelled" | "Enhanced iron delivery by atmospheric dust during glacial periods is modelled"; the numbers of the same sentence are GB-05; overlapping location with GB-03 (the attribution of two background statements), GB-04 (the iron-fertilisation frame), where a different point is treated | S1 |
| KK-07 | p. 2, l. 48 to 49 | "(Qu, 2016; Shi et al., 2009, Shi et al. 2011, Shi et al. 2015)" | "(Qu, 2016; Shi et al., 2009, 2011, 2015)"; overlapping location with GB-04 (the iron-fertilisation frame), where a different point is treated | S1 |
| KK-08 | p. 2, l. 62 | "high altitude site such as EDC where dust fluxes is low" | "high-altitude sites such as EDC, where dust fluxes are low" | S1 |
| KK-09 | p. 3, l. 71 | "information than REE ratio" | "information than REE ratios" | S1 |
| KK-10 | p. 3, l. 73 | "achieved multi-decadal resolution" | "achieved decadal to centennial resolution"; the manuscript itself gives "ranging from 60 to 140 years" (p. 4, l. 110 to 111), and Wegner et al. (2012) state "decadal to centennial resolution" | S1 |
| KK-11 | p. 3, l. 88 | "model - to the REE pattern dataset measured - in the EPICA Dome C" | "model to the REE pattern dataset measured in the EPICA Dome C"; spaced hyphens without function | ZF |
| KK-12 | p. 3, l. 90 | "in the Indian Ocean sector of the East Antarctica" | "in the Indian Ocean sector of East Antarctica" | S1 |
| KK-13 | p. 3, l. 90 to 91 | "from 33.6 kyr to 2.8 kyr BP" | "from 33.7 kyr to 2.9 kyr BP", as in p. 1, l. 18 and p. 6, l. 182 (Table S1 spans 2852 to 33699 yr); same sentence as KK-12, different phrase; the aims in this sentence are GB-07 and GB-08 | S3 |

#### Verification log

| ID | Check | Checked | Values | Result |
|---|---|---|---|---|
| PP-01 | P13 | Lambert et al. (2008) as source for p. 2, l. 34 to 36 and l. 44 to 46 (dust deposition controlled by the location of the sources and the residence time of dust in the atmosphere) | Abstract (https://www.nature.com/articles/nature06763, preview only): "the sources and lifetime of dust are the main factors controlling the high glacial dust input" | no finding; "geographic location" paraphrases "sources"; abstract only |
| PP-02 | P13 | p. 2, l. 62 to 63: "up to 25 times lower than LGM fluxes (e.g. Delmonte et al., 2008; Delmonte et al., 2017)" | Lambert et al. (2008), abstract (https://ideas.repec.org/a/nat/nature/v452y2008i7187d10.1038_nature06763.html): "25-fold increase in glacial dust flux"; Delmonte et al. (2008) abstract (https://boa.unimib.it/handle/10281/6594): no flux ratio; Delmonte et al. (2017) not readable | no finding; the factor exists in Lambert et al. (2008), cited in l. 36; whether the two Delmonte works give it is not verified |
| PP-03 | P13 | p. 3, l. 72 to 74: earlier REE studies "could not fully resolve dust provenance" | Gabrielli et al. (2010), author copy of the published article: 294 samples, 2.9 to 33.7 kyr BP, about 60 yr (Holocene) to 140 yr (glacial); Holocene analysis "does not allow the exclusion of any major PSA"; Wegner et al. (2012), Clim. Past abstract (https://cp.copernicus.org/articles/8/135/2012/): "decadal to centennial resolution" | no finding on "could not fully resolve"; resolution wording is KK-10 |
| PP-04 | P13 | p. 3, l. 77 to 87: summary of Vanderstraeten et al. (2023) | Abstract (https://marineinfo.org/id/publication/382930): about 68 % Patagonia before 14.5 kyr BP, "Patagonia dropped below 50 % on average", early Holocene about 50 %, 386 of 398 samples unmixed | the Introduction reproduces the abstract faithfully; the conflict with Table S5 is GB-06 |
| PP-05 | P13 | p. 3, l. 92 to 93: "the Holocene for which there is no consensus" | Revel-Rolland et al. (2006) abstract (https://repository.geologyscience.ru/handle/123456789/45867): Australian dust possibly dominant in interglacials; Vallelonga et al. (2010): Australian dust not the main component; Delmonte et al. (2013): Holocene Dome C isotopes consistent with Antarctic rocks; Aarons et al. (2017) (https://byrd.osu.edu/sites/default/files/2020-12/Aarons_et_al_QSR_2017.pdf): local Ross Sea and South American Holocene sources at Taylor Glacier | no finding; the read sources disagree, so "no consensus" is supported; Paleari et al. (2019) and Delmonte et al. (2007) not readable, Coppo et al. (2022) abstract only |
| PP-06 | P14 | Contribution in one sentence (first continuous percentage apportionment of Southern Hemisphere dust sources at EDC over 33.7 to 2.9 kyr BP by REE unmixing, checked against Sr-Nd data and compared with EDML), five literature searches with the queries listed by instance S1 | Candidates checked against the reference list: Vallelonga et al. (2010), Siggaard-Andersen et al. (2007), Delmonte et al. (2013) not in the list; Aarons et al. (2017) only in Table S4 (see GB-56); Revel-Rolland et al. (2006) (p. 20, l. 759) and Gili et al. (2022) (p. 18, l. 641) in the list, dropped; Marino et al. (2008) found but not readable, not proposed | three proposals in GB-07 |
| PP-07 | P28 | Gap and priority claims p. 1, l. 17 and 19 to 20; p. 3, l. 74 to 75 and l. 92; p. 7, l. 220; p. 12, l. 403; p. 14, l. 472, with two own searches | Search vocabulary in the text layer: 7 hits, all journal names; no database, term, period or date; the searches returned no earlier percentage apportionment at EDC | finding GB-01; the "no consensus" statement in l. 92 is a literature statement with citations, see PP-05 |
| PP-08 | P10 | Gaps named in the Introduction against the four aims (p. 3, l. 91 to 98) | "no consensus" for the Holocene (l. 92 to 93) to aim 1; limits of isotope fingerprinting (p. 2, l. 60 to 68) to the REE approach and aim 2; only one quantitative record (EDML) to aim 4; aim 3 has no explicit gap | no finding beyond GB-04, GB-13 and GB-41 |
| PP-09 | design sketch | Questions, study type, data sources, environment, principles, components, disclosed limits and chain from frame to result, over the whole manuscript and supplement (instance SD) | Study type: re-analysis of a published REE dataset with NNLS unmixing and Monte Carlo; 294, 279, 241 samples; 217 source patterns in seven PSA; no control for the unmixing itself (no synthetic mixtures); external comparisons: literature Sr-Nd values (Table S4), EDML record, DustCOMM and Coppo et al. (2022); software MATLAB lsqnonneg without version; declared principles: R threshold with p value, non-negativity, removal of Gd, 60 to 140 yr spacing, complete data availability; outlook: none | sketch complete; findings from it are GB-04, GB-11, GB-13, GB-20, GB-38 and GB-54 |

### Segment 2: Materials and methods, Figure S1, Table S2 (p. 3 to 5, l. 99 to 172; Suppl. p. 1 to 2 and 16 to 19)

#### Substantive findings

**GB-09 Six SAF source patterns are new data of "this study" without any description of sampling or analysis, two of them carry the location of another site, and all six give western longitudes for Namibian sites.**

| Field | Content |
|---|---|
| Check | P12, P38, P19 |
| Location | p. 4, l. 105; p. 4, l. 126 to 127; Table S2 (Suppl. p. 17), rows EtoshaL1 to EtoshaL4, SuksesL and Sossusvlei, columns Reference, Location, Latitude and Longitude; p. 12, l. 385 to 387; Figure S3 (Suppl. p. 6) |
| Quotation | "literature reported patterns from known potential source areas (PSA)"; "we compiled a comprehensive database of 217 REE patterns" |
| Concern | Table S2 labels six SAF rows "this study" (page image Suppl. p. 17). They are primary data of the authors and enter every fit, while p. 4, l. 105 describes the database as literature patterns and the Methods give no sampling, size separation or analytical procedure for them; the author contribution statement does not name who produced them (see GB-55). The rows also contradict themselves: SuksesL (21.059 S) and Sossusvlei (24.76 S) are filed under "Etosha Pan", whereas the other seven Etosha rows lie between 18.557 and 19.125 S; SuksesL lies about 215 km and Sossusvlei about 627 km further south (Python: (21.059 minus 19.125) times 111.2 = 215; (24.76 minus 19.125) times 111.2 = 627). The six longitudes are given as W (15.29 to 16.836 W), whereas Etosha1 to Etosha3 at nearly the same latitude are given as 15° 50' to 15° 53' E; a western longitude at these latitudes lies in the Atlantic. Section 4.3 (p. 12, l. 385 to 387) and Figure S3 attribute SAF dust to the Etosha, Makgadikgadi and Namibian coast systems; if the sub-region grouping follows the location column, SuksesL and Sossusvlei are counted as Etosha. The counts of the database are GB-15; the naming of PSA and DS is GB-10. |
| Suggestion | Describe sampling, size fractionation and REE analysis of the six samples in Section 2 or the supplement, write "literature and new patterns" in p. 4, l. 105 and l. 126 to 127, give SuksesL and Sossusvlei their actual locality, correct the six longitudes to E, and state in the caption of Figure S3 which DS form each SAF sub-region. |
| Status | Labels, coordinates and references verified (page image Suppl. p. 17); distances inferred (Python from the table coordinates); that the sub-region grouping follows the location column: assumption, put as a question |
| Severity | moderate |
| Source | S2, SD |

**GB-10 "PSA" names both the seven source regions and the 217 source samples, and the caption of Table S1 gives "217 PSAs and 279 DIC" for a table of 241 samples.**

| Field | Content |
|---|---|
| Check | P38, P20 |
| Location | p. 4, l. 105; p. 4, l. 136 to 137; Table S1, caption (Suppl. p. 11); Table S2, caption (Suppl. p. 16) |
| Quotation | "using 217 PSAs and 279 DIC from EDC ice core REE patterns"; "the REE pattern of each EDC sample was modeled as a linear combination of PSA end-members" |
| Concern | The manuscript defines PSA as "Potential Source Areas" (p. 2, l. 44), uses it for the seven regions (p. 4, l. 128 to 133; Table S1 columns), and calls the 217 individual samples "dust sources, DS" (p. 4, l. 129) with contributions CDS 1 to 217 (p. 4, l. 137). The Table S1 caption ("217 PSAs") and the Table S2 caption ("Table of PSAs database") apply PSA to the 217 samples, and l. 136 to 137 calls the end-members of the fit PSA patterns, although the fit uses the 217 DS columns and aggregates to PSA only afterwards (p. 5, l. 161 to 162). In addition, Table S1 contains 241 rows (Python, confirmed at the page images Suppl. p. 11 to 15), the retained samples of p. 6, l. 179, not the 279 treated samples; a reader looking for the 38 excluded samples in Table S1 will not find them (see GB-24). The caption also reads "based on th DEPOT model results". Same first location as GB-09, different object. |
| Suggestion | Use "DS" for the 217 samples throughout: p. 4, l. 105 "patterns of dust source samples (DS) from known potential source areas (PSA)", p. 4, l. 136 to 137 "a linear combination of DS end-members", Table S2 caption "Table of the DS database", and Table S1 caption "Median contribution of each PSA (in percent) based on the DEPOT model results, using 217 dust sources (DS) grouped into seven PSA, for the 241 DIC samples with R of at least 0.67 (of 279 treated)". |
| Status | verified (text layer; captions at the page images Suppl. p. 11 and 16; row count with Python) |
| Severity | minor |
| Source | S2, S3, SD |

**GB-11 The stated sample spacing of 60 to 140 years is contradicted by the retained samples, which include shorter spacings and four ages that occur twice.**

| Field | Content |
|---|---|
| Check | P6, P20 |
| Location | p. 4, l. 110 to 111; Table S1 (Suppl. p. 11, 13 and 14), rows 3559, 10511, 12841 and 28709 |
| Quotation | "with an average temporal resolution of approximately 100 years, ranging from 60 to 140 years between adjacent samples" |
| Concern | Removing samples can only widen spacings. Yet among the 240 spacings of the 241 retained samples of Table S1, 4 are 0 yr, 73 are 1 to 59 yr, 103 are 60 to 140 yr and 60 exceed 140 yr (Python: 4 plus 73 plus 103 plus 60 = 240). The Holocene median spacing is 42 to 43 yr (see GB-25). Four ages occur twice: 3559 (Suppl. p. 11), 10511 and 12841 (Suppl. p. 13) and 28709 (Suppl. p. 14), each pair with strongly different values (for 3559 PAT 86.7 and 0.0; confirmed at the page images Suppl. p. 11 and 13). If the pairs are replicates of one depth, the unit of the record is a measured pattern, not a sample, and the counts (241, the YD count of GB-49) and the period means weight these depths twice; if they are separate samples, the ages need more digits. Question to the authors: which is the case? Overlapping location with GB-10 (the naming of PSA and DS and the caption of Table S1); this finding concerns sample spacing and duplicated ages. |
| Suggestion | Correct p. 4, l. 110 to 111 with the actual range per period, and state in Section 2 and in Table S1 whether the duplicated ages are replicates, adjacent depths with the same age, or errors. |
| Status | Spacings and duplicates verified (Python on Table S1; page images Suppl. p. 11 and 13); nature of the duplicates: assumption, put as a question |
| Severity | moderate |
| Source | SD, S3 |

**GB-12 Question to the authors: on which concentration basis are the ice-core and source patterns fitted, and how are the coefficients turned into percentages?**

| Field | Content |
|---|---|
| Check | P25 |
| Location | p. 4, l. 117 to 124; p. 5, l. 142 to 149 |
| Quotation | "The vector of 217 components represents the proportional contribution of each DS required to best approximate the REE signature of a given dust ice core" |
| Concern | Eq. (2) is a linear combination of UCC-normalised source concentrations without a sum-to-one constraint. For the coefficients to be mass proportions, the DIC REE values must be per mass of dust, which requires the dust mass of each sample; the manuscript does not say where this comes from. If concentrations per mass of ice are fitted, the coefficients scale with the dust content and the shares depend on the absolute REE level of each source pattern (Table S2 values of the 213 non-Antarctic rows range from 0.048 to 3.34 times UCC, apart from the single value 6.20 treated in GB-22; Python). The scaling of the Antarctic patterns is a separate problem (GB-16). |
| Suggestion | State in Section 2 the concentration basis of DIC and DS in Eq. (2), the source of the dust mass if used, and how the coefficients are normalised into percentages. |
| Status | assumption (the basis is not stated; the range of Table S2 values is verified with Python) |
| Severity | moderate |
| Source | SD |

**GB-13 The unmixing design has not been shown to identify source contributions: 13 equations face 217 non-negative unknowns, and no recovery test is reported.**

| Field | Content |
|---|---|
| Check | P10, P9 |
| Location | p. 4, l. 126 to 133; p. 5, l. 142 to 152; Table S2 (Suppl. p. 16 to 19) |
| Quotation | "comprising “n” rows (one for each UCC-normalized REE) and 217 columns"; "n was equal to 14 but is only 13 in the present study" |
| Concern | With more unknowns than equations, a non-negative least-squares solution is in general not unique, and NNLS returns one of possibly many equally good combinations. Aim 1 asks for quantitative contributions, which requires that the design can recover known contributions. The manuscript reports no such test: a search of p. 1 to 15 and 23 to 29 (text layer) for "synthetic", "artificial", "recover", "test mixture", "known mixture", "unique", "identifiab", "cross-valid" and "leave-one" gives 0 hits; "sensitivity" gives 1 hit (p. 12, l. 388, "climatic sensitivity"). The Methods defer to Vanderstraeten et al. (2023) (p. 4, l. 106 to 107); whether a test exists there could not be checked (abstract only). As an indication, instance SD re-ran the setup on the 217 patterns of Table S2 (NNLS on the UCC-normalised values, multiplicative Gaussian noise): synthetic glacial-like mixtures (PAT 70, NZ 12, AUS 10, SAF 5, PAP 3 %) at 2 % noise were recovered with a mean PAT estimate of 58.5 % and a mean absolute PAT error of 17.8 points; single AUS, NZ or SAF patterns with 5 % noise were assigned less than half to their own region in 65, 63 and 68 % of 300 trials; unstructured random patterns reached R of at least 0.67 in 40 % of 2000 trials. These numbers depend on assumptions about scaling and noise and are no measurement of DEPOT itself, but they show that identifiability cannot be taken for granted. The database itself is the object of GB-09, GB-15 and GB-16; the threshold of GB-20. |
| Suggestion | Add to Section 2 a recovery test of the exact DEPOT configuration: synthetic mixtures drawn from Table S2 at the measured noise levels (2 to 10 % per REE, and higher near the detection limit), leave-one-out tests per PSA, a confusion matrix between PSA, and the R distribution of fitted random patterns as a null for the threshold. As a counter-design, compare the 217-column solution with an unmixing on seven regional mean end-members (or a Bayesian mixing model with posterior intervals) and report where they disagree. |
| Status | verified (13 rows, 217 columns, no recovery test, search as stated); inferred (simulation results of instance SD under stated assumptions) |
| Severity | major |
| Source | SD |

**GB-14 Question to the authors: do the different size fractions and the uneven number of patterns per region bias the apportionment?**

| Field | Content |
|---|---|
| Check | P9 |
| Location | p. 4, l. 126 to 133; Table S2 (Suppl. p. 16 to 19), column "Type of sample" |
| Quotation | "Australia (AUS; 106 DS, predominantly from the central and southeastern regions)" |
| Concern | Counted in Table S2 (instance SD, text layer): AUS 100 of 107 patterns are fractions below 90 µm, 6 are surface sediments and 1 a dust trap, none is a fraction below 5 µm; NZ 19 of 25, SAF 17 of 23, PAT 12 of 39 and CWA 5 of 5 are fractions below 5 µm; PAT 24 and ANT 4 are aeolian dust. AUS supplies 107 of 217 columns (49.3 %), ANT 4 (1.8 %). With an NNLS that selects among columns, a region with many columns may have more chances to fit noise. Whether REE patterns differ between these fractions is not discussed: search of p. 1 to 15 for "grain size", "grain-size", "fraction" and "µm": 0 hits. No measurement of the effect is available, hence a question. This finding shares the location with GB-13 and asks a narrower question about the database; the counts themselves are GB-15. Overlapping location with GB-09 (the six new SAF patterns); this finding concerns size fractions and pattern numbers per region. |
| Suggestion | Discuss the size fractions of the end-members in Section 2, and repeat the unmixing with a database balanced per region (random subsets of equal size, or regional means) and with fine fractions only where available; report the change in PSA shares. |
| Status | Counts verified; effect on the results: assumption |
| Severity | moderate |
| Source | SD |

**GB-15 The published source database (Table S2) does not match the counts given in the Methods: AUS has 107 rows instead of 106, ANT 4 instead of 5.**

| Field | Content |
|---|---|
| Check | P12 |
| Location | p. 4, l. 131 to 133; Table S2 (Suppl. p. 17 to 19), group blocks AUS and ANT |
| Quotation | "Australia (AUS; 106 DS, predominantly from the central"; "Antarctica (ANT; 5" |
| Concern | Table S2 is the only published form of the source database. Rows per group block counted with Python on the supplement text and confirmed at the page images Suppl. p. 17 and 19: PAT 39, CWA 5, PAP 14, SAF 23, AUS 107, NZ 25, ANT 4. Python: 39 plus 5 plus 14 plus 23 plus 107 plus 25 plus 4 = 217, and for the Methods 39 plus 5 plus 14 plus 23 plus 106 plus 25 plus 5 = 217. The totals agree, but AUS has one row more and ANT one row fewer than stated; the ANT block holds exactly ELB, Expcove, Miers and Vict. Two AUS rows are moreover duplicates (GB-21), so the table has 105 distinct AUS patterns. Either one ANT pattern is missing from the published table and one AUS row too many, or the counts in l. 131 to 133 are wrong. This finding concerns the counts; the new SAF data are GB-09, the size fractions GB-14, the identifiability GB-13. |
| Suggestion | Reconcile Table S2 with p. 4, l. 131 to 133: add the missing ANT pattern and remove the surplus AUS row, or correct the counts to 107 and 4. |
| Status | verified (row counts with Python, page images Suppl. p. 17 and 19) |
| Severity | moderate |
| Source | S2, SD |

**GB-16 The four Antarctic patterns in Table S2 do not look UCC-normalised, although the Methods state that all source patterns were normalised; question to the authors whether they entered the fit in this form.**

| Field | Content |
|---|---|
| Check | P2 |
| Location | p. 4, l. 133 to 135; Table S2 (Suppl. p. 19), ANT block, rows ELB, Expcove, Miers and Vict; p. 7, l. 217 to 218; p. 10, l. 329 to 334 |
| Quotation | "all PSA REE patterns were normalized to the UCC composition of Rudnick and Gao (2003)" |
| Concern | The header of Table S2 reads "REE normalised on the Upper Continental Crust (Rudnick and Gao, 2003)". For the 213 non-Antarctic rows, La/Lu lies between 0.258 and 2.477 and the ratio of the largest to the smallest of the 13 values is at most 4.13. For the four ANT rows, La/Lu is 35.8 to 129.3 and that ratio 77.9 to 251.9; Pr/Ce is 0.109 to 0.120 against at least 0.361 in all other rows; and the successive differences from La to Lu change sign 9 times in each ANT row against at most 8 in any other row (Python on the supplement text; values confirmed at the page image Suppl. p. 19, for example ELB: La 0,720323, Ce 1,414516, Pr 0,157226, Lu 0,008290). The ANT values thus rise and fall alternately from element to element and decline by two orders of magnitude from La to Lu, as concentrations do that have not been divided by a reference composition. If the ANT columns entered Eq. (2) in this form, they can hardly fit a UCC-normalised ice-core pattern, and the near-zero ANT shares (p. 7, l. 217 to 218; Table S5 at most 0.6 %) and the argument against an Antarctic contribution (p. 10, l. 329 to 334) may be artefacts of scaling, with the Antarctic fraction absorbed by other sources. Against this reading, Table S1 contains ANT 33.1 % at 3654 yr and 1.7 % at 13412 yr, so ANT columns were selected at least twice. Questions: were the ANT patterns UCC-normalised before the fit, and are the values of Table S2 those that were used? The Antarctic attribution matters because published isotope studies of Dome C point to local Antarctic input in the Holocene (GB-07). This finding was raised by instance S2 as a note outside its checklist; no instance treated it, and it was confirmed here at the page image. It is related to, but not the same as, the concentration basis of GB-12 and the counts of GB-15; GB-13 and GB-14 share the location p. 4, l. 133. Since, if it holds, the ANT result and all other shares change, the finding is major. Overlapping location with GB-09 (the six new SAF patterns); this finding concerns the normalisation of the Antarctic patterns. |
| Suggestion | State in Section 2 how the ANT patterns of Diaz et al. (2018) were normalised; if the printed values were used, normalise them to UCC, rerun the fit and report the change in all PSA shares, and correct Table S2. |
| Status | Table values verified (page image Suppl. p. 19); ratios and sign changes inferred (Python); that the printed values entered the fit: assumption, put as a question |
| Severity | major |
| Source | ZF |

**GB-17 The EDC and EDML records come from different model configurations and possibly different chronologies; the regional differences of 4 to 14 points are interpreted without controlling for this.**

| Field | Content |
|---|---|
| Check | P9, P7 |
| Location | p. 5, l. 144 to 145; p. 4, l. 111; p. 6, l. 184 to 188; p. 13, l. 424 to 425; p. 13, l. 444 to 446; Figure 4 (p. 28) |
| Quotation | "In Vanderstraeten et al. (2023), n was equal to 14 but is only 13 in the present study because of the exclusion of Gd"; "These differences are consistent with the geographic positioning of the two sites" |
| Concern | Aim 4 compares EDC (13 REE, 217 database patterns) with the EDML record computed with 14 REE; according to its abstract, the EDML model used "a new database of 207 Rare Earth Element (REE) patterns". The EDML input data come from a different laboratory dataset (Wegner et al., 2012, p. 3, l. 74). Each difference can shift PSA shares, especially between end-members with similar patterns (GB-13). The manuscript states the REE difference but does not discuss it as a cause of between-core differences, and the differences it interprets (NZ plus 8 in the LGM, PAT plus 4 and plus 6.5 in ACR and YD, PAT minus 14 and AUS plus 12 in the Holocene, p. 13, l. 417 to 424) are of the size such changes could produce, with no uncertainty attached. The chronology of the EDML record is not stated for the "synchronous millennial-scale changes" (l. 444 to 446): search of p. 1 to 15 for "chronolog", "age model", "EDC3" and "AICC": hits only in p. 4, l. 111. In addition (raised by instance S2 as a note and added here): the EDC sample ages follow EDC3 (p. 4, l. 111), whereas the period limits are taken from Veres et al. (2013) (p. 6, l. 188), whose entry in the reference list is titled "The Antarctic ice core chronology (AICC2012)" (p. 21, l. 819 to 820). Whether the limits were transferred to EDC3 before the samples were assigned to periods is not stated. Whether the EDML values in Table S5 are the published ones is GB-06; the comparison windows are GB-48. Overlapping location with GB-11 (sample spacing and duplicated ages); GB-12 (the concentration basis of the fit); this finding concerns model configuration and chronology of EDC and EDML. |
| Suggestion | Rerun the EDML record in Section 4.4 with the identical configuration (13 REE, 217 patterns, same cf and Monte Carlo settings), report the period differences with Monte Carlo uncertainty and a test, state the chronology of both cores and of the period limits (or put all on a common timescale), and interpret only differences that remain after harmonisation. |
| Status | 13 against 14 REE and the chronology statements verified (text, page images p. 4, 5, 6, 21); 207 patterns in EDML verified for the abstract (https://marineinfo.org/id/publication/382930); effect on the differences: inferred; transfer of the period limits: assumption, put as a question |
| Severity | major |
| Source | SD, ZF |

**GB-18 The Monte Carlo uncertainty of the PSA contributions is computed but not reported.**

| Field | Content |
|---|---|
| Check | P11 |
| Location | p. 5, l. 153 to 165; Table S1 (Suppl. p. 11 to 15); Table S5 (Suppl. p. 22) |
| Quotation | "Each DIC sample was subjected to 2000 simulations and the ensuing CDS results (in % of total deposition) generate a probability density function (PDF) for every DS" |
| Concern | The Methods build a PDF per PSA and sample, but only its median is reported (Table S1); no spread, interval or percentile appears in Table S1, Table S5, Figure 1 or the text. Search of p. 1 to 15 and the captions (p. 25 to 29) for "uncertaint", "confidence", "percentile", "standard deviation", "±" and "quartile": 11 hits; those on model uncertainty are all in the Methods (p. 5, l. 153 to 163) or general (p. 6, l. 180); the "±" values at p. 10, l. 320 and p. 12, l. 394 are literature values, and "quartiles" at p. 27, l. 872 describes spread between samples. The statement that 5000 runs do not "significantly affect the results" (p. 5, l. 163 to 164) has no number. Without the PDF widths a reader cannot judge whether differences of 4 to 8 points between periods or cores (p. 13, l. 417 to 424) exceed the model uncertainty. The equation reference in p. 5, l. 159 is KK-19. Overlapping location with GB-10 (the naming of PSA and DS and the caption of Table S1); GB-11 (sample spacing and duplicated ages); this finding concerns the unreported Monte Carlo uncertainty. |
| Suggestion | Add the 16th and 84th (or 2.5th and 97.5th) percentiles per PSA to Table S1, a period-level uncertainty to Table S5, and the comparison of 2000 and 5000 runs as numbers in the supplement. |
| Status | verified (search as stated) |
| Severity | moderate |
| Source | S3 |

**GB-19 The announced conversion of PSA shares into absolute dust fluxes is not reported in any table or figure.**

| Field | Content |
|---|---|
| Check | P11, P3, P31 |
| Location | p. 5, l. 166 to 167; p. 6, l. 183 to 184; Figure S2 (Suppl. p. 3 to 4); Figure 1 (p. 24) |
| Quotation | "to convert PSA contributions into absolute dust fluxes (Figure S2)"; "Figure 1 and Table S1 summarize the relative contributions (in % of total deposition and flux)" |
| Concern | Figure S2 shows the nssCa2+ flux, δ18O and deuterium excess, with no PSA-specific flux (page image Suppl. p. 4). Figure 1 (axes "Total Contribution (%)") and Table S1 give percentages only. Instance AB checked the axis titles of all ten figures (Figures 1 to 5, S1 to S5); none shows a PSA flux. Search for "flux" on p. 1 to 15 and 23 to 29 (text layer): 11 matches, none reporting a PSA flux. The announced analysis is therefore absent for every PSA and period; its consequence for the interpretation is GB-02. In addition, nssCa2+ is used as a proxy of total dust without saying so. |
| Suggestion | Add PSA fluxes with the conversion factor and its uncertainty (per sample in Table S1 and per period in Table S5, or as a panel in Figure 1 or S2), or delete the conversion sentence in p. 5, l. 166 to 167 and "and flux" in p. 6, l. 184. |
| Status | verified (search and page images p. 24, Suppl. p. 4) |
| Severity | moderate |
| Source | S3, AB, SD |

**GB-20 The R threshold does not correspond to the stated significance level, the degrees of freedom do not match 13 REE, and three retained samples fall below the threshold.**

| Field | Content |
|---|---|
| Check | P1, P5, P2 |
| Location | p. 5, l. 170 to 172; p. 6, l. 174 to 179; Table S1 (Suppl. p. 11), rows 2888 and 3267, column R; Table S1 (Suppl. p. 13), first row 10511, column R |
| Quotation | "We determined that R ≥ 0.67 corresponds to a statistically significant match (p"; "38 did not meet the R threshold (R≥0.67)" |
| Concern | For Pearson r with df = n minus 2, the two-tailed critical value at p = 0.01 is 0.708 for df = 10 and 0.684 for df = 11 (Python, scipy). With 13 REE per pattern (p. 4, l. 117) df is 11, not 10. R = 0.67 gives p = 0.017 at df = 10 and p = 0.012 at df = 11, so the rule holds only one-tailed. Applying the stated level would exclude further samples: 9 rows of Table S1 have R below 0.684 and 19 below 0.708, all younger than 13 kyr BP (Python). Moreover the p value of a correlation between an observed pattern and a pattern fitted to it with up to 13 non-zero coefficients does not follow the textbook null distribution, because the fit itself creates correlation (GB-13). Finally, Table S1 lists R = 0,66 at 2888, 3267 and the first row 10511 (page images Suppl. p. 11 and 13); a printed 0.66 means R below 0.665, so these three samples fail the rule of p. 6, l. 174, yet they are part of the 241 and of Table S5 (Table S5 is reproduced only with all 241 rows). Removing them changes the Holocene means by at most 0.8 points (Python). The selection of the Holocene samples depends on this threshold (GB-24, GB-25), and the sum of the first row 10511 is GB-34. Overlapping location with GB-10 (the naming of PSA and DS and the caption of Table S1); GB-11 (sample spacing and duplicated ages); GB-18 (the unreported Monte Carlo uncertainty); this finding concerns the R threshold. |
| Suggestion | In Section 2 state one-tailed or correct the threshold (0.708 for df = 10 or 0.684 for df = 11), correct df to 11, derive the threshold from a null distribution of R for fitted random patterns, and either remove the three samples with R = 0.66 from Table S1, Table S5 and Figure 1 or state the rounding rule that keeps them. |
| Status | Wording and Table S1 values verified (page images p. 5, 6, Suppl. p. 11, 13); critical values, p values and counts inferred (Python) |
| Severity | moderate |
| Source | S3, SD |

**GB-21 Two Australian source patterns appear twice in Table S2 under different names and basins, with identical coordinates and identical values for all 13 REE.**

| Field | Content |
|---|---|
| Check | P38 |
| Location | Table S2 (Suppl. p. 17), rows Darling26 and Darling29; Table S2 (Suppl. p. 18), rows Murray24 and Murray29; p. 4, l. 131; p. 11, l. 366 to 367 |
| Quotation | "our model identifies the Darling sub-basin as the dominant source region during the Holocene" |
| Concern | A comparison of all 217 rows of Table S2 (13 values each, Python by instance S2) finds exactly two pairs with identical value vectors: Darling26 (Suppl. p. 17) equals Murray29 (Suppl. p. 18), and Darling29 equals Murray24, with Eu 0,507000 in both; both pairs were confirmed value by value at the page images. In each pair the coordinates also coincide (34° 3'0.00"S 142° 3'10.80"E; 34°28'48.00"S 142°49'48.00"E), but one row is filed under "Darling Basin" and the other under "Murray Basin". These are one sample under two names. In Eq. (2) this gives two identical columns, between which an NNLS solution can split the contribution arbitrarily, so the share attributed to the Darling or the Murray sub-basin is not determined by the data; the Holocene statement on the Darling sub-basin (p. 11, l. 366) rests on such an attribution (see also GB-26). The AUS row count is GB-15. Overlapping location with GB-09 (the six new SAF patterns); GB-13 (the identifiability of the unmixing); GB-14 (size fractions and pattern numbers per region); GB-16 (the normalisation of the Antarctic patterns); this finding concerns the duplicated Darling and Murray patterns. |
| Suggestion | Check the original data of Marx and Kamber (2010) for the two samples, keep each sample once with its correct basin, rerun the fit, and state in Section 4.3 whether the Darling attribution in p. 11, l. 366 changes. |
| Status | Duplicates verified (Python, page images Suppl. p. 17 and 18); non-uniqueness inferred from the structure of Eq. (2); effect on the Darling attribution: assumption, put as a question |
| Severity | moderate |
| Source | S2 |

**GB-22 Two further entries of Table S2 look like transcription errors: a Dy value in Kuiseb2inf5 and the longitude of Darling12.**

| Field | Content |
|---|---|
| Check | P2 |
| Location | Table S2 (Suppl. p. 17), row Kuiseb2inf5, column Dy; Table S2 (Suppl. p. 17), row Darling12, column Longitude |
| Quotation | "6,200013"; "138°17'6.00"E" |
| Concern | In Kuiseb2inf5, Dy = 6,200013 lies between Tb = 2,692922 and Ho = 2,149792. The ratio of Dy to the geometric mean of Tb and Ho is 2.58 for this row and at most 1.27 for all other 212 non-Antarctic rows (median 1.04; Python). Darling12 has the same latitude as Darling11 (31° 2'49.20"S) but the longitude 138°17'6.00"E instead of 144°17'6.00"E; the other 44 Darling rows lie between 141.84 and 148.58 °E (Python). Both entries were confirmed at the page image Suppl. p. 17. If the Dy value entered the fit as printed, it distorts one SAF end-member; if the correct value was used, the published table does not reproduce the fit. Both were raised as notes by instances S2 and SD; no instance treated them, and they were confirmed here. They are separate from the duplicated rows of GB-21. Overlapping location with GB-09 (the six new SAF patterns); GB-13 (the identifiability of the unmixing); GB-14 (size fractions and pattern numbers per region); GB-15 (the AUS and ANT counts of Table S2); GB-16 (the normalisation of the Antarctic patterns); this finding concerns probable typing errors in Table S2. |
| Suggestion | Check both entries against the original data (Vanderstraeten et al., 2023; Marx and Kamber, 2010), correct Table S2, and state whether the fit used the corrected values. |
| Status | Table values verified (page image Suppl. p. 17); outlier measures inferred (Python); whether the fit used the printed values: assumption, put as a question |
| Severity | moderate |
| Source | ZF |

**GB-23 Figure S1 shows 19 sites in Patagonia, whereas the text lists 39 Patagonian dust sources, and the caption does not say that one pin can stand for several samples.**

| Field | Content |
|---|---|
| Check | P3 |
| Location | Figure S1, panel PAT (Suppl. p. 2); p. 4, l. 129 |
| Quotation | "Localization of dust sources (DS) used in our DEPOT algorithm" |
| Concern | Instance AB counted 19 location pins in the PAT panel at 300 dpi. Table S2 gives 22 distinct coordinate pairs for the 39 PAT rows (Python on the supplement text), for example six PataGa samples at 42°46'S 65° 2'W, so most of the difference comes from samples sharing a site, and a few nearby sites may overlap at map scale; the map is embedded at 78 ppi, so overlapping pins cannot be separated. The caption says each DS is localised, which a reader cannot check. Overlapping location with GB-13 (the identifiability of the unmixing); GB-14 (size fractions and pattern numbers per region); this finding concerns the pins of Figure S1. |
| Suggestion | State in the caption of Figure S1 that one pin can stand for several samples and give the number of samples per pin, or label the pins with their counts. |
| Status | Pins counted by instance AB (verified at the page image); coordinate pairs inferred (Python on Table S2) |
| Severity | minor |
| Source | AB |

#### Minor corrections

| ID | Location | Quotation | Replacement | Source |
|---|---|---|---|---|
| KK-14 | p. 3, l. 101 | "to ice core camples" | "to ice core samples" | ZF |
| KK-15 | p. 4, l. 109; p. 6, l. 190 | "the end of MIS 3" (both places) | "the end of MIS3"; search in the text layer: "MIS 3" 2 hits (listed), "MIS3" 10 hits; the period definitions near p. 6, l. 190 are KK-22, the data sources in p. 4, l. 107 to 109 GB-54 | S2 |
| KK-16 | p. 4, l. 127 | "(Figure S1, and Table S1)" | "(Figure S1 and Table S2)"; Table S1 holds the contributions per sample, Table S2 the source database; same sentence as the database statements of GB-09, GB-13 and GB-14 | S4, SD |
| KK-17 | p. 4, l. 128 | "subdivised into Patagonia" | "subdivided into Patagonia"; see GB-13, GB-14 for the database itself | ZF |
| KK-18 | p. 4, l. 138 | "solving the system of matrixes" | "solving the system of matrices" | ZF |
| KK-19 | p. 5, l. 159 | "by minimizing Eq. (1)" | "by minimizing Eq. (2)"; Eq. (1) defines the correction factor; the Monte Carlo reporting of the same sentence is GB-18 | S4, SD |
| KK-20 | Table S2 (Suppl. p. 16), group heading | "Puna AltiPlano (PAP)" | "Puna-Altiplano Plateau (PAP)", as defined in p. 4, l. 129 to 130; other Table S2 issues are GB-21 and GB-22; overlapping location with GB-09 (the six new SAF patterns), GB-13 (the identifiability of the unmixing), GB-14 (size fractions and pattern numbers per region), GB-15 (the AUS and ANT counts of Table S2), GB-16 (the normalisation of the Antarctic patterns), GB-56 (supplement citations missing from the reference list), where a different point is treated | S2 |
| KK-21 | Table S2 (Suppl. p. 19), group heading; Table S3 (Suppl. p. 20), row 4 and plot legend; Figure 2, frame label (p. 26) | "New-Zealand (NZ)"; "New-Zealand" | "New Zealand (NZ)"; "New Zealand", as in p. 4, l. 132; search for "New-Zealand": main text 0 hits, supplement text 2 hits plus the plot and figure labels at the page images; Table S2 and Figure 2 are also the objects of GB-21, GB-22 and GB-58; overlapping location with GB-09 (the six new SAF patterns), GB-13 (the identifiability of the unmixing), GB-14 (size fractions and pattern numbers per region), GB-15 (the AUS and ANT counts of Table S2), GB-16 (the normalisation of the Antarctic patterns), GB-56 (supplement citations missing from the reference list), KK-20 (a group heading), where a different point is treated | S2, AB |

#### Verification log

| ID | Check | Checked | Values | Result |
|---|---|---|---|---|
| PP-10 | P12 | Every data source named in Section 2 (p. 3, l. 99 to p. 5, l. 172) and in Figure S1 and Table S2, against the statement p. 16, l. 494 to 496 and the supplement | EDC REE dataset (294 DIC, Gabrielli et al., 2010): not in the supplement, not per sample in the source; excluded samples (15 and 38): not identified; UCC (Rudnick and Gao, 2003): published reference; cf_i: not given; EDC3 (Parrenin et al., 2007): published reference, sample ages in Table S1; source database: Table S2; Dust_i: range only (2 to 10 %); MATLAB code: not mentioned; Monte Carlo output: medians and R only; nssCa2+ (Fischer et al., 2007): published reference, plotted in Figure S2 A; PSA fluxes: not published; Figure S1: in supplement; no link or DOI in the statement | findings GB-54, GB-09 and GB-15; the manuscript names no data withheld for reasons of personal data |
| PP-11 | P38, P23, P1 | Sample balance and fit quality from dataset to record (p. 4, l. 108 to 117; p. 6, l. 174 to 181; p. 1, l. 19) | 294 minus 15 = 279; 279 minus 38 = 241; 241 / 279 = 86.4 % (text 86 %); Table S1 rows: 241 (Python, page images Suppl. p. 11 to 15); mean R of Table S1 0.852 (text 0.852); samples between 21.7 and 27.3 kyr BP: 22150, 23104, 25384, 25640 = 4 (text "only four samples") | no finding; the selection rule itself is GB-20 |
| PP-12 | P38 | Name of the unmixing tool in manuscript and supplement | "'DEPOT' model" (p. 3, l. 88), "DEPOT" algorithm (p. 3, l. 100; p. 8, l. 259; Figure S1 caption), "DEPOT model" (Table S1 caption); generic "statistical unmixing algorithm" (p. 1, l. 19) and "unmixing model" (p. 9, l. 306) | no finding; one proper name, no second identifier |
| PP-13 | P38 | Region abbreviations and core names in Section 2, Tables S1 to S5 and captions | PAT, CWA, PAP, SAF, AUS, NZ, ANT defined p. 4, l. 128 to 133 and used unchanged in Tables S1, S2, S5 (Table S1 splits PAP into Puna and Altiplano); Table S3 adds the sub-region SCWA; EDC defined p. 1, l. 18; DIC p. 4, l. 108 to 109; DS p. 4, l. 129 | no finding beyond GB-10, KK-03, KK-20, KK-21 and KK-39 |
| PP-14 | P7 | Method versions within the EDC data | One dataset (Gabrielli et al., 2010), one cf set, Gd removed from all DIC and PSA patterns (p. 4, l. 115 and l. 134 to 135), one Monte Carlo setting (2000 runs) | no finding within EDC; the version difference to EDML is GB-17 |
| PP-15 | P17 | Place of disclosure of the sampling gap and of the removal of Gd | Gap at p. 4, l. 113 and Gd at p. 4, l. 115 to 117, both in Section 2 where the data are introduced | no finding on the place of disclosure; instance SD also noted that the gap is visible as a straight segment in Figure 1, whereas instance AB raised the unmarked gap in the figures as a finding; decided: the straight segment is not labelled in any figure or caption, so GB-33 stands; the placement of the ACR and YD caveat is part of GB-37 |
| PP-16 | P26 | Non-negativity across all paths | lsqnonneg in every fit and Monte Carlo run (p. 5, l. 138 to 140); Table S1 contains no negative value (241 rows, 8 columns) | no finding |
| PP-17 | P27 | Unverified components that control later steps | R threshold controls the sample selection (GB-20, GB-25); cf_i enter every fit but are not shown (GB-54); the 9-step moving average controls the visible variability in Figure 1 (GB-25) | covered by the findings named |
| PP-18 | P35 | Instruments and software | ICP-SFMS via the cited title (Gabrielli et al., 2006), HNO3 leaching, analytical uncertainty 2 to 10 % (1 RSD) stated (p. 5, l. 155 to 156); MATLAB version and random seed not given | finding GB-54 |
| PP-19 | P33 | Effort statements | "computation cost" of the Monte Carlo runs (p. 5, l. 162 to 163) is not used as a result or limit | no finding; the missing number for 5000 runs is part of GB-18 |
| PP-20 | P36 | Statements by recollection ("approximately", "about") against own records | "approximately 100 years" mean spacing in range, range claim fails (GB-11); EDML counts "47 and 27" (p. 12, l. 409) cannot be checked in this manuscript | no further finding |
| PP-21 | P18 | Declared principles applied to the manuscript itself | Open-data claim (p. 16, l. 494 to 495) against the content of the supplement | finding GB-54 |
| PP-22 | P32 | Claims "validating", "robust" and independent re-checks | "validat" 1 hit (p. 3, l. 93), "robust" 2 hits (p. 5, l. 172; p. 8, l. 259); no independent re-check on samples | no finding beyond GB-13 and GB-38 |
| PP-23 | P38 | Duplicate check of all 217 value vectors of Table S2 | Python on the supplement text, Suppl. p. 16 to 19: 217 rows, 2 identical pairs (GB-21), all other rows differ already in the first three values; Murray27 and Murray28 share coordinates but differ in values (La 1,242032 and 0,315935) | Murray27 and Murray28 are two samples from one site: no finding for this pair |

### Segment 3: Results, Figure 1, Tables S1 and S5 (p. 6 to 7, l. 173 to 218; p. 24 to 25; Suppl. p. 11 to 15 and 22)

#### Substantive findings

**GB-24 The 38 excluded samples are not listed, so their ages, their distribution over the periods and the claim that all are younger than 14 kyr BP cannot be checked.**

| Field | Content |
|---|---|
| Check | P11, P34 |
| Location | p. 6, l. 174 to 176; Table S1 (Suppl. p. 11 to 15) |
| Quotation | "These excluded samples are all younger than 14 kyr BP and have very low REE concentrations near the detection limit." |
| Concern | Table S1 lists only the 241 retained samples (GB-10). Ages, R values and REE concentrations of the 38 excluded samples appear nowhere. Since all exclusions fall in the ACR, YD and Holocene, they thin exactly the periods for which the manuscript reports the largest variability and the smallest sample numbers (GB-25, GB-49): with the 129 retained rows younger than 14 kyr BP, 38 of 167 samples (22.8 %) were excluded there, against 0 of 112 older samples (Python; the 167 assumes that all 38 lie below 14 kyr BP as stated). The R threshold that produces the exclusions is GB-20; the missing data statement is GB-54. Overlapping location with GB-11 (sample spacing and duplicated ages); GB-18 (the unreported Monte Carlo uncertainty); this finding concerns the unlisted excluded samples. |
| Suggestion | Add the 38 excluded samples to Table S1 (flagged, with age, R and REE level), or give their number per period in Section 3. |
| Status | Absence verified (Table S1, page images Suppl. p. 11 to 15); share inferred (Python) |
| Severity | moderate |
| Source | S3, SD |

**GB-25 The larger Holocene variability coincides with the samples of lowest fit quality, lowest concentrations and densest sampling; noise and sampling density are not separated from the climatic interpretation.**

| Field | Content |
|---|---|
| Check | P9 |
| Location | p. 6, l. 174 to 181; p. 9, l. 306 to 308; Table S1 (Suppl. p. 11 to 15) |
| Quotation | "our unmixing model reveals a significantly larger variability in the dust assemblages reaching EDC as shown in Figure 1" |
| Concern | The manuscript states that low concentrations near the detection limit distort REE patterns and render fitting meaningless (p. 6, l. 176 to 179), but draws this consequence only for the 38 excluded samples (GB-24). Among the retained samples, fit quality also drops: R below 0.75 in 40 of 125 samples younger than 12.9 kyr BP and in 0 of 116 older samples; mean R is 0.787 (Late Holocene), 0.812 (Early Holocene) and 0.779 (YD) against 0.843 to 0.924 (ACR to MIS3). The mean absolute change of PAT between consecutive samples is 35.8, 31.7 and 39.6 points (Late Holocene, Early Holocene, YD) against 10.7 to 11.9 points (ACR to MIS3). The median spacing is 42 to 43 yr in the Holocene and 102.5 to 150 yr before (all Python on Table S1, checked by this review), so the 9-step moving average of Figure 1 (p. 25, l. 852) spans about 340 yr in the Holocene and about 820 to 1200 yr before. "significantly" is not backed by a test (search of p. 1 to 15 for "test", "statistic" and the string "p" followed by a less-than sign: hits only in p. 1, l. 19 and p. 5, l. 171). The variability and its attribution to climatic processes (p. 9, l. 308 to 314) and to regional source dynamics (Section 4.3) are therefore confounded with analytical noise, lower fit quality and denser sampling; without per-sample uncertainty (GB-18) a reader cannot separate signal from noise. Because the Holocene interpretation (aim 3) rests on this variability, the finding is major. Overlapping location with GB-10 (the naming of PSA and DS and the caption of Table S1); this finding concerns Holocene variability confounded with noise and sampling. |
| Suggestion | Report per sample the Monte Carlo interquartile range of every PSA share and the REE concentration level; test whether the between-sample variance in each period exceeds the within-sample Monte Carlo variance; repeat the Holocene statistics with a stricter threshold (for example R of at least 0.75) and with fixed time bins (for example 500 yr) instead of a 9-step average; run the recovery test of GB-13 at the noise level of the Holocene samples, and interpret in Section 4.3 only variability that survives these tests. |
| Status | Wording verified (page images p. 6, 9); counts, R values and spacings verified on Table S1 and computed with Python; the confounding is inferred |
| Severity | major |
| Source | SD |

**GB-26 Sub-regional and single-source attributions are stated in Results and Discussion but not reported in any table or figure.**

| Field | Content |
|---|---|
| Check | P11, P34 |
| Location | p. 6, l. 196 to 197; p. 11, l. 366 to 367; p. 12, l. 385 to 387; p. 12, l. 391 to 392; p. 5, l. 161 to 162 |
| Quotation | "Among the 39 DS from PAT, our algorithm highlights three specific REE patterns collected in or near the Valdes Peninsula."; "Among SAF sources, the Namibian coast and ephemeral riverbeds were detected most frequently" |
| Concern | The Methods announce aggregation "by PSA or specific sub-regions within PSA" (p. 5, l. 161 to 162). Results per sub-region are reported only for Puna and Altiplano (Table S1, Figure S3) and for Etosha, Namibia and Sua (Figure S3). There is no AUS sub-region result (Darling, Murray, Lachlan, Murrumbidgee, Wimmera, Lake Eyre in Table S2), no identification of the three Valdes Peninsula patterns, and no detection frequency for any SAF source, although "most frequently" is a frequency statement that needs counts. The Darling attribution is moreover affected by the duplicated rows of GB-21; the SAF sub-regions by the mislabelled rows of GB-09. Overlapping location with GB-18 (the unreported Monte Carlo uncertainty); this finding concerns unreported sub-regional results. |
| Suggestion | Add a supplementary table with the mean contribution per period and the detection frequency (number of samples with a non-zero CDS) per DS or sub-region for AUS, SAF and PAT, and name the three Valdes Peninsula patterns by their Table S2 identifiers. |
| Status | verified (search for "Valdes", "Darling sub", "detected most" and "frequen" in the text layer; Figure S3 panels at the page image Suppl. p. 6) |
| Severity | moderate |
| Source | S3, SD |

**GB-27 The stated order of importance of the secondary sources (PAP before NZ) is not borne out by Table S1 or Table S5.**

| Field | Content |
|---|---|
| Check | P2 |
| Location | p. 6, l. 201 to 202 |
| Quotation | "AUS, SAF, PAP and NZ, in decreasing order of importance" |
| Concern | Mean over all 241 rows of Table S1: AUS 16.51, SAF 9.17, NZ 7.85, PAP 6.85. Mean over the six periods of Table S5 (MIS3, LGM, HS1, ACR, YD, Holocene): AUS 13.22, SAF 8.97, NZ 7.70, PAP 4.75 (Python). Under both weightings NZ ranks before PAP. |
| Suggestion | Write "AUS, SAF, NZ and PAP" in p. 6, l. 202, or state the basis of the ranking. |
| Status | Inputs verified; means inferred (Python) |
| Severity | minor |
| Source | S3 |

**GB-28 The "sharp increase" of SAF in the YD rests on a single sample.**

| Field | Content |
|---|---|
| Check | P21 |
| Location | p. 6, l. 206 to 207; p. 13, l. 422; Table S1 (Suppl. p. 13), YD block, column SAF |
| Quotation | "followed by a sharp increase during the YD with 15%" |
| Concern | YD SAF values in Table S1 (n = 9, page image Suppl. p. 13): 0.0, 1.3, 94.7, 8.8, 5.5, 5.0, 6.2, 2.4, 7.8; sum 131.7, mean 14.63 (Table S5: 14.6). The single sample 12227 (94.7) contributes 94.7 / 131.7 = 71.9 % of the sum. Without it the YD mean is 4.62; the YD median is 5.5 (Python). The "sharp increase" disappears under either check and lies within the 5 to 9 % band of the other glacial periods. The same sample drives the YD SAF difference to EDML (GB-50) and plots at the SAF end-member in Figure 2 (GB-59). Overlapping location with GB-10 (the naming of PSA and DS and the caption of Table S1); GB-11 (sample spacing and duplicated ages); GB-18 (the unreported Monte Carlo uncertainty); GB-20 (the R threshold); GB-24 (the unlisted excluded samples); GB-25 (Holocene variability confounded with noise and sampling); this finding concerns the YD SAF mean driven by one sample. |
| Suggestion | Report median and n alongside the YD mean, and qualify p. 6, l. 207 ("driven by one sample at 12.2 kyr BP"). |
| Status | Table values verified (page image Suppl. p. 13); means and median inferred (Python) |
| Severity | moderate |
| Source | S3 |

**GB-29 The SAF values "~2%" for 9.5 to 12 kyr BP and "~11%" for the subsequent Holocene have no recoverable basis.**

| Field | Content |
|---|---|
| Check | P20 |
| Location | p. 6, l. 207 to p. 7, l. 208 |
| Quotation | "Although SAF input drops to minimal"; "levels (~2%) between 9.5 and 12 kyr BP, it rebounds in the subsequent Holocene, averaging ~11%" |
| Concern | From Table S1, SAF between 9.5 and 12 kyr BP (n = 33): mean 4.32, median 0.3; neither gives about 2 %. Instance AB measured the smoothed SAF curve of Figure 1 in the same interval: median 5.3 %, minimum 0.9 % at 11.38 kyr BP, and logged no finding; the three statistics together do not yield about 2 % either, so the finding stands. For the "subsequent Holocene" (2.8 to 9.5 kyr BP, n = 85) the mean is 13.0; about 11 % matches only the mean over the whole Holocene (Table S5: 10.7), which includes the minimum it is contrasted with (Python). The neighbouring statement on the YD in p. 6, l. 206 to 207 is GB-28. |
| Suggestion | State the statistic and interval behind each number, for example "mean 4 %, median 0.3 %, n = 33" and "mean 13 %, n = 85". |
| Status | Inputs verified; means and medians inferred (Python); smoothed values measured by instance AB |
| Severity | minor |
| Source | S3 |

**GB-30 The statements on South Altiplano above 90 % at five ages and South Puna below 20 % in the Holocene disagree with Table S1, and Figure 1, which is cited for them, shows neither sub-region.**

| Field | Content |
|---|---|
| Check | P2, P3, P20 |
| Location | p. 7, l. 212 to 215; Table S1 (Suppl. p. 11 to 13), columns Puna and Altiplano; Figure 1, panel PAP (p. 24); Figure S3, panels Altiplano and Puna (Suppl. p. 6) |
| Quotation | "contributing over 90% at 11.2, 10, 8.6, 6, and 3.5 kyr BP. In contrast, contributions of South Puna remained consistently below 20% during this interval (Figure 1)." |
| Concern | Figure 1 shows only the PAP total, so neither South Altiplano nor South Puna can be read from it; instance AB measured the PAP raw curve at least 88 % only at 8615 and 11231 yr BP. In Table S1 (column Altiplano, % of total deposition) values above 90 occur only at 8629 (100.0) and 11228 (97.0); near 10, 6 and 3.5 kyr BP the largest values are 75.7 (9957), 58.5 (5967), 58.0 (6166) and 62.7 (3465). If "over 90%" referred to the share of Altiplano within PAP, all 22 rows with Altiplano above 0 and Puna 0 would qualify, far more than five. South Puna exceeds 20 % in 8 of the 116 Holocene rows: 3503 (25.0), 4387 (20.6), 5657 (23.4), 5850 (29.1), 6775 (20.7), 7833 (25.6), 10205 (25.7) and 11117 (20.2) (Python; all eight values confirmed at the page images Suppl. p. 11 to 13). The instances listed 8 (S3), 7 (SD) and 5 (AB) of these rows; the count of 8 was decided here at the page images. The qualitative statement that South Altiplano dominates several samples holds (above 50 % in seven rows). The wording "South Altiplano" against "Southern Altiplano" (p. 4, l. 130) is corrected here; other places are KK-39. The disagreement between Figure S3 and Table S1 is GB-44. Overlapping location with GB-10 (the naming of PSA and DS and the caption of Table S1); GB-11 (sample spacing and duplicated ages); GB-18 (the unreported Monte Carlo uncertainty); GB-20 (the R threshold); GB-24 (the unlisted excluded samples); GB-25 (Holocene variability confounded with noise and sampling); GB-28 (the YD SAF mean driven by one sample); this finding concerns the South Altiplano and South Puna values. |
| Suggestion | In p. 7, l. 213 to 215 cite Table S1 and Figure S3 instead of Figure 1, write "Southern Altiplano", give the ages at which Altiplano exceeds 90 % (8.6 and 11.2 kyr BP) or state the reference quantity, and replace "consistently below 20%" by "mostly below 20 % (8 of 116 Holocene samples exceed 20 %, maximum 29.1 %)". |
| Status | Table values verified (page images Suppl. p. 11 to 13); counts inferred (Python); Figure 1 by measurement of instance AB |
| Severity | moderate |
| Source | S3, AB, SD |

**GB-31 Labels in Figures 1, 3 and 5 are smaller than 6 pt at print size.**

| Field | Content |
|---|---|
| Check | P29 |
| Location | Figure 1 (p. 24); Figure 3 (p. 27); Figure 5 (p. 29) |
| Quotation | "Raw data"; "Contributions (%)"; "PSA Contribution (in %)" |
| Concern | Cap or digit heights measured by instance AB in 300 dpi page images (pt = px times 72 / 300 / 0.72; method deviation up to 0.6 pt): Figure 5 tick numbers 4.3 to 4.7 pt, legend 4.7 pt, y title 5.7 pt; Figure 1 tick numbers 5.0 to 5.7 pt, legend "Raw data" 4.7 to 5.0 pt, y titles 5.3 pt; Figure 3 axis numbers 5.3 pt. Figure 5 is below 6 pt beyond the method uncertainty; Figures 1 and 3 by 0.3 to 1.3 pt. Figures 2 and 4 measure 6.0 to 7.3 pt (PP-52). The same figures are the objects of GB-32 (captions) and GB-33 (gap). |
| Suggestion | Enlarge axis numbers, axis titles and legends in Figures 1, 3 and 5 to at least 7 pt at final print width. |
| Status | verified (measurement) |
| Severity | minor |
| Source | AB |

**GB-32 Abbreviations used in the figures are not resolved in the captions.**

| Field | Content |
|---|---|
| Check | P29 |
| Location | Figures 1 to 5, captions (p. 25 to 29) |
| Quotation | "Evolution of dust PSA contributions to EDC ice core" |
| Concern | Search in the caption lines p. 25, l. 851 to p. 29, l. 882 (text layer, confirmed at the page images) for each abbreviation and for an expansion of the form name followed by abbreviation in parentheses: PSA (6 occurrences), EDC (6), EDML (2), AUS, SAF, YD, ACR, HS1, MIS3 and LGIT (1 each) appear without expansion; NZ, PAP, CWA, "Holo" (Figure 4) and "Iso" (Figure 2) appear only inside the figures. Expanded are only PAT (Figure 5), LGM (Figure 3) and MDF (Figure 5). The figures therefore cannot be read without the text. Font sizes are GB-31, the gap marking GB-33. |
| Suggestion | Add to each caption a sentence resolving the region and period abbreviations used in that figure, for example "PAT, Patagonia; AUS, Australia; SAF, Southern Africa; NZ, New Zealand; PAP, Puna-Altiplano Plateau; YD, Younger Dryas; ACR, Antarctic Cold Reversal; HS1, Heinrich Stadial 1; LGM, Last Glacial Maximum; MIS3, Marine Isotope Stage 3; EDC, EPICA Dome C; EDML, EPICA Dronning Maud Land". |
| Status | verified (search as stated, page images p. 24 to 29) |
| Severity | minor |
| Source | AB |

**GB-33 Figures 1, 5A and S5 draw continuous lines across the sampling gap between 21.7 and 27.3 kyr BP without marking it.**

| Field | Content |
|---|---|
| Check | P29 |
| Location | Figure 1, all panels (p. 24); Figure 5, panel A (p. 29); Figure S5 (Suppl. p. 10); p. 4, l. 113 |
| Quotation | "A sampling gap exists between 21.7 and 27.3 kyr BP, where only four samples were available." |
| Concern | The gap is disclosed in the Methods (PP-15). In Figure 1 the smoothed PAT and NZ curves between 23.3 and 25.2 kyr BP, the interval between the samples at 23104 and 25384 yr in Table S1, are straight lines (instance AB: linear fit over 80 pixel columns, maximum residual 0.12 and 0.06 %). A 9-step moving average across 4 samples in 5.6 kyr mixes samples several kyr apart, and no figure or caption says so. Instance SD noted the straight segment without raising a finding; it is decided here as a finding because nothing marks it. The text claim of continuity is GB-36; font sizes and captions of the same figures are GB-31 and GB-32. |
| Suggestion | Interrupt the curves or shade 21.7 to 27.3 kyr BP in Figures 1, 5A and S5 and add "sampling gap" to the captions. |
| Status | verified (measurement by instance AB; ages in Table S1) |
| Severity | minor |
| Source | AB |

**GB-34 One row of Table S1 sums to 93.5 % instead of 100 %.**

| Field | Content |
|---|---|
| Check | P23 |
| Location | Table S1 (Suppl. p. 13), first of the two rows 10511 |
| Quotation | "10511" with the values "0,0", "0,0", "3,1", "6,7", "49,2", "29,5", "5,0", "0,0", "0,66" |
| Concern | 0.0 plus 0.0 plus 3.1 plus 6.7 plus 49.2 plus 29.5 plus 5.0 plus 0.0 = 93.5. All other 240 rows sum to 100 within 0.25 (Python). Possible resolutions: (A) one value is mistyped, 6.5 points are missing in one column; (B) medians of separate Monte Carlo PDFs need not sum to 100, but then other rows would deviate too, and none deviates by more than 0.25; (C) the row belongs to an excluded sample (its R of 0.66 is below the threshold, GB-20) and was carried over with incomplete values. A or C would change the Early Holocene means of Table S5 by at most 6.5 / 56 = 0.12 points per column. The age 10511 also occurs twice (GB-11). Overlapping location with GB-10 (the naming of PSA and DS and the caption of Table S1); GB-18 (the unreported Monte Carlo uncertainty); GB-24 (the unlisted excluded samples); GB-25 (Holocene variability confounded with noise and sampling); GB-28 (the YD SAF mean driven by one sample); GB-30 (the South Altiplano and South Puna values); this finding concerns the row sum of 93.5 % in Table S1. |
| Suggestion | Check the row against the model output and correct it in Table S1; if it belongs to an excluded sample, remove it and recompute Table S5. |
| Status | Row verified (page image Suppl. p. 13); sum inferred (Python); resolutions are questions |
| Severity | minor |
| Source | S3 |

**GB-35 The number of samples per period is not stated, so the period means in Table S5 can only be weighted by counting rows in Table S1.**

| Field | Content |
|---|---|
| Check | P22 |
| Location | Table S5 (Suppl. p. 22) |
| Quotation | "Average contributions for each PSA (in percents) based on dust samples from EDC and EDML" |
| Concern | Only the ACR and YD counts are given in the text (p. 12, l. 408; see GB-49); the Results (p. 6, l. 189 to p. 7, l. 218) quote the period means without n. A reader must count Table S1 to learn the base of each mean: Late Holocene 60, Early Holocene 56, Holocene 116, YD 9, ACR 8, HS1 27, LGM 40, MIS3 41 (Python: 116 plus 9 plus 8 plus 27 plus 40 plus 41 = 241). Table S5 also gives no dispersion, so a YD mean based on 9 samples looks as firm as an LGM mean based on 40 (see GB-28). Overlapping location with GB-06 (the EDML values of Table S5 against the published EDML record); GB-07 (missing literature on Dome C provenance); this finding concerns n and dispersion in Table S5. |
| Suggestion | Add to Table S5 a column n and a column with standard deviation or interquartile range, for EDC and EDML. |
| Status | Counts verified (Python on Table S1, block limits at the page images Suppl. p. 11 to 15) |
| Severity | minor |
| Source | S3 |

#### Minor corrections

| ID | Location | Quotation | Replacement | Source |
|---|---|---|---|---|
| KK-22 | p. 6, l. 189 to 190 | "It contributes for 65-70%" | "It contributes 65 to 70%"; same sentence as "MIS 3" in KK-15 | S3 |
| KK-23 | p. 6, l. 191 | "the PSA dust assemblage during HSI is marked" | "the PSA dust assemblage during HS1 is marked"; "HSI" confirmed at the page image p. 6, all other mentions read "HS1" | S2, S3 |
| KK-24 | p. 6, l. 193 | "(averages contributions)" | "(average contributions)" | S3 |
| KK-25 | p. 6, l. 195 | "contributing to 47-51% of the total mix" | "contributing 47 to 51% of the total mix" | S3 |
| KK-26 | p. 6, l. 199 | "LREE (low rare earth elements)" | "LREE (light rare earth elements)" | ZF |
| KK-27 | p. 25, l. 851; Figure S3 caption (Suppl. p. 5) | "between 2852 to 33699 yr BP"; "between 2.852 to 33.699 kyr BP" | "between 2852 and 33699 yr BP"; "between 2.852 and 33.699 kyr BP"; overlapping location with GB-44 (Figure S3 against Table S1), GB-45 (the onset of Southern Altiplano dust), where a different point is treated | AB |
| KK-28 | p. 25, l. 852; p. 29, l. 882; Figure S5 caption (Suppl. p. 9) | "Bold lines denote the mobile average over 9 steps"; "(mobile average over 9" | "Bold lines denote the moving average over 9 steps"; "(moving average over 9"; same caption line as KK-27; Figure 5 caption is also GB-62; overlapping location with GB-64 (the bands and legend of Figure S5), where a different point is treated | S4 |

#### Verification log

| ID | Check | Checked | Values | Result |
|---|---|---|---|---|
| PP-24 | P1, P2 | EDC rows of Table S5 against the means of the Table S1 rows per period (period limits of p. 6, l. 185 to 188) | Maximum absolute difference 0.05 over 8 periods and 7 PSA; n = 60, 56, 116, 9, 8, 27, 40, 41; for example Holocene PAT 49.0, PAP 11.0, SAF 10.7, AUS 23.1, NZ 5.9; LGM 65.7, 3.6, 6.3, 10.2, 14.2; row sums of Table S5 99.9 to 100.1 (EDC) and 99.9 to 100.0 (EDML); reproduced independently by instances S3, AB and SD and by this review | no finding; Table S5 is the arithmetic mean of the per-sample medians |
| PP-25 | P2 | Results text against Table S5 (p. 6, l. 189 to p. 7, l. 218) and the Abstract (p. 1, l. 21 to 25) | PAT 65 to 70 (70.3, 65.7), 75 (74.8), 69 and 63 (68.9, 63.1), 47 to 51 (47.1, 50.7); AUS 9, 10, 11 (9.1, 10.2, 11.3), 11 (11.1), about 15 (14.5), 23 (23.1); SAF about 5 to 9 (9.3, 6.3, 4.9, 8.0), 15 (14.6); NZ 14 (14.2), 7 (7.1), 6.5, 3, 6 (6.6, 3.3, 5.9); PAP below 4 (2.2, 3.6, 2.0), about 5 (5.2, 4.5), 11 (11.0); Abstract about 65 to 75 and about 49 (49.0) | no finding beyond GB-27, GB-28 and GB-29 |
| PP-26 | P20 | Percentage bases in the Results | "241 DIC samples (86%)" with base 279 stated; period means based on samples (Table S5 caption); Table S1 "% of total deposition" | no finding beyond GB-10, GB-29 and GB-30 |
| PP-27 | P2 | CWA and ANT "negligible" (p. 7, l. 217) | CWA 0.0 in all 241 rows; ANT non-zero only at 3654 (33.1) and 13412 (1.7); Table S5 ANT at most 0.6 | no finding on the means; the scaling of the ANT patterns is GB-16 |
| PP-28 | P24 | Figure 1: grey period bands against the period limits of p. 6, l. 185 to 188 | Instance AB, x calibrated on ticks 0.4 and 3.0 (times 10^4 yr BP), 1 px = 24 yr; band edges PAT panel 11.69, 12.90, 14.71, 18.01, 28.99 kyr BP, the other four panels within 0.03 kyr; text 11.7, 12.9, 14.7, 18, 29 kyr BP; axis ends 2859 and 33680 yr (caption 2852 and 33699) | no finding |
| PP-29 | P24, P3 | Figure 1: dated extremes named in the text | Smoothed PAT minima 10.13 (22.7 %), 8.54 (30.6 %), 6.33 kyr BP (28.2 %); text p. 6, l. 194: 10, 8.6, 6.3; AUS smoothed maxima 6.30 kyr BP and 9.8 to 10.8 kyr BP; text p. 6, l. 205: 9.5 to 10 and about 6.3 kyr BP; SAF smoothed 9.5 to 12 kyr BP: median 5.3 %, minimum 0.9 % (instance AB) | no finding for the PAT and AUS dates; the SAF value of the text is GB-29, where this log entry and the finding of instance S3 were reconciled |
| PP-30 | P29, P3 | Inventory of all figures with type, caption and citations | Figures 1 to 5 on p. 24 to 29 with captions p. 25 to 29, cited first at p. 6, l. 183; p. 8, l. 244; p. 9, l. 281; p. 12, l. 405; p. 10, l. 340; Figures S1 to S5 on Suppl. p. 2 to 10, cited first at p. 4, l. 127; p. 5, l. 167; p. 11, l. 355; p. 12, l. 382; p. 12, l. 405; no graphical abstract | all ten figures are cited; the order of Figures 4 and 5 is GB-42 |
| PP-31 | P11 | Matrix of periods and PSA in Table S5 | EDC: 8 periods by 7 PSA complete; EDML: 5 periods, no Late Holocene and no MIS3 | no finding; the omission follows from the EDML record span 7 to 27 kyr (reference title p. 21, l. 813 to 814) |
| PP-32 | P23 | Row sums of Table S1 | 240 of 241 rows sum to 100 within 0.25 | no finding beyond GB-34 |
| PP-33 | P21 | Base of the LGM comparison EDC (18 to 29 kyr) against EDML (record to 27 kyr) | EDC LGM restricted to 18 to 27 kyr, n = 25: PAT 65.2, PAP 3.5, SAF 7.1, AUS 9.8, NZ 14.3, against the full LGM (n = 40) 65.7, 3.6, 6.3, 10.2, 14.2 | no finding; differences to EDML change by at most 0.8 points |

### Segment 4: Discussion, Conclusion, declarations, references, Figures 2 to 5, Figures S2 to S5, Tables S3 and S4 (p. 7 to 29, l. 219 to 882; Suppl. p. 3 to 10 and 20 to 21)

#### Substantive findings

**GB-36 Discussion and Conclusion call the record "continuous", although the Methods disclose a sampling gap with four samples between 21.7 and 27.3 kyr BP.**

| Field | Content |
|---|---|
| Check | P15 |
| Location | p. 7, l. 220; p. 7, l. 230; p. 12, l. 403; p. 14, l. 472; p. 4, l. 113; Table S1 (Suppl. p. 14), LGM block |
| Quotation | "This study presents the first high-resolution, continuous and quantitative reconstruction of dust" |
| Concern | The gap is disclosed (p. 4, l. 113), but the claim of continuity is repeated in p. 7, l. 220 and 230, p. 12, l. 403 and p. 14, l. 472 without that qualification. In Table S1 the four samples in the gap are at 22150, 23104, 25384 and 25640 yr BP; the largest spacings between adjacent samples are 2280 yr (23104 to 25384) and 1785 yr (25640 to 27425), against the stated mean resolution of about 100 years (p. 4, l. 110) (Python). The 38 excluded samples, all younger than 14 kyr BP, add an unknown thinning of the Holocene coverage (GB-24). The priority claims of the same sentences are GB-01, the unmarked gap in the figures GB-33; the capitalisation in p. 7, l. 220 is KK-29. Overlapping location with GB-10 (the naming of PSA and DS and the caption of Table S1); GB-11 (sample spacing and duplicated ages); GB-18 (the unreported Monte Carlo uncertainty); GB-20 (the R threshold); GB-25 (Holocene variability confounded with noise and sampling); GB-28 (the YD SAF mean driven by one sample); GB-30 (the South Altiplano and South Puna values); GB-34 (the row sum of 93.5 % in Table S1); this finding concerns the word "continuous". |
| Suggestion | Qualify "continuous" in p. 7, l. 220, p. 12, l. 403 and p. 14, l. 472, for example "continuous except for a sampling gap between 21.7 and 27.3 kyr BP". |
| Status | Text verified (page images p. 4, 7, 12, 14); spacings inferred (Python on Table S1) |
| Severity | moderate |
| Source | S4 |

**GB-37 The shift "at the onset of the ACR" and "from ~14.5 kyr BP onward" is stated more strongly than the EDC period means support, and the caveat on the small ACR and YD sample numbers appears only in Section 4.4.**

| Field | Content |
|---|---|
| Check | P15, P17 |
| Location | p. 7, l. 233 to 236; p. 13, l. 445 to 447; p. 14, l. 477 to 480; p. 12, l. 407 to 409; Table S5 (Suppl. p. 22), EDC rows; Table S1 (Suppl. p. 13), ACR block |
| Quotation | "Our calculations highlight a major shift in dust provenance occurred at the onset of the ACR"; "diverse mixture with significantly increased contributions from low-latitude sources"; "From ~14.5 kyr BP onward, a marked reorganization in dust provenance occurred" |
| Concern | The record does show a decline in PAT from its HS1 maximum, and the authors note that "results for ACR and YD are tentative" (p. 12, l. 407). This caveat is not carried into the Results (p. 6, l. 192 to 193, ACR and YD means of 69 and 63 %), Section 4.1 or the Conclusion. EDC means from Table S5: PAT plus NZ is 79.4 (MIS3), 79.9 (LGM), 81.9 (HS1), 75.5 (ACR), 66.4 (YD), 54.9 (Holocene); AUS plus SAF plus PAP is 20.6, 20.1, 18.2, 24.3, 33.6, 44.8 (Python). Case analysis: against HS1, PAT in the ACR is 5.9 points and PAT plus NZ 6.4 points lower; against the LGM, PAT in the ACR is 3.2 points higher and PAT plus NZ 4.4 points lower; against MIS3, PAT is 1.4 points lower. AUS is 11.1 in the ACR and 11.3 in HS1. The ACR mean therefore lies within the glacial range; the change towards low-latitude sources is carried mainly by the YD and the Holocene. The ACR has 8 samples (page image Suppl. p. 13, 13032 to 14601 yr) with PAT from 41.9 to 81.7. "significantly" (l. 235) is not backed by a test (see GB-25 for the search). Sub-interval means of PAT from Table S1 are 83.2 (15 to 16 kyr BP, n = 8), 72.0 (14 to 15 kyr BP, n = 7) and 64.3 (13 to 14 kyr BP, n = 4) (Python), so the decline between 15 and 14 kyr BP (p. 13, l. 445 to 446) exists but ends at LGM levels. The timing matters because the attribution to Meltwater Pulse 1A and shelf submergence (p. 13, l. 450 to p. 14, l. 455; p. 14, l. 480 to 482) rests on it. Because the finding concerns research aim 3 and the timing of the main result, it is major. The YD sample count is GB-49; the grammar of l. 233 and l. 236 is KK-31 and KK-32. Overlapping location with GB-06 (the EDML values of Table S5 against the published EDML record); GB-07 (missing literature on Dome C provenance); GB-35 (n and dispersion in Table S5); this finding concerns strength and timing of the ACR shift. |
| Suggestion | Test the ACR against HS1 and the LGM (for example a rank test on the per-sample values of Table S1 or on the Monte Carlo distributions) and report the result. Reword p. 7, l. 233 to 236 and p. 14, l. 477 to 480 so that they describe a decline from the HS1 maximum around 15 to 14 kyr BP and a low-latitude increase that becomes pronounced in the YD and the Holocene, or justify the stronger wording by the test. Move the sample numbers and the caveat of p. 12, l. 407 to 409 into Section 3 and Section 4.1 and the Conclusion. |
| Status | Table values verified (page images Suppl. p. 13 and 22); text verified (page images p. 6, 7, 12, 13, 14); sums, differences and sub-interval means inferred (Python) |
| Severity | major |
| Source | S4, SD |

**GB-38 The isotopic check claims agreement with values "measured in EDC" for glacial and interglacial intervals, but every measured Holocene, ACR and YD value comes from other cores, the agreement is not quantified, and the modelled Holocene values do not reproduce the EDC Holocene values quoted in the text.**

| Field | Content |
|---|---|
| Check | P15, P31, P32, P3 |
| Location | p. 8, l. 258 to 260; p. 8, l. 251 to 257; p. 7, l. 227 to 228; p. 7, l. 238 to 240; p. 1, l. 25 to 26; p. 3, l. 93 to 94; Figure 2, open symbols (p. 26); Table S4 (Suppl. p. 21) |
| Quotation | "Overall, the close agreement between our modeled isotopic compositions and those measured in EDC for both glacial and interglacial intervals supports the robustness of our DEPOT algorithm" |
| Concern | The forward calculation (Eq. 3 and 4) is the only independent check of the model (aim 2, p. 3, l. 93 to 94), and the glacial comparison rests on EDC data. Table S4, which lists the open symbols of Figure 2, has 35 rows (counted at the page image Suppl. p. 21 by instances S4 and SD): "Iso LGM" 6 (2 "Epica dome C", 4 "Taylor Glacier"), "Iso HS1" 3 (1 "Old Dome C", 2 Taylor Glacier), "Iso ACR" 2 and "Iso YD" 2 (Taylor Glacier), "Iso Holocene" 22 (8 Taylor Glacier, 14 Berkner Island); 6 plus 3 plus 2 plus 2 plus 22 = 35. Three of 35 values come from Dome C, and no ACR, YD or Holocene value comes from EDC. Instance AB measured one open light-red circle in Figure 2 at 0.7228 and minus 14.17, which is the Berkner Island value 0.7228 and minus 14.15; Berkner Island lies in the Atlantic sector, where Section 4.4 itself expects a different Holocene provenance. No agreement measure (residual, overlap or test) is given; the judgement is visual. The EDC Holocene values in p. 7, l. 240 ("~0.710" and "-4.51 to -5.68") appear in no row of Table S4. Instance SD recomputed Eq. 3 and 4 for all 241 samples from Table S1 and Table S3: LGM median εNd minus 2.05 and 87Sr/86Sr 0.7081, in line with the EDC LGM values of p. 7, l. 238 to 239; Holocene median εNd minus 2.44 and 0.7091, with 8 of 116 Holocene samples within minus 5.68 to minus 4.51 and 77 less negative. The Holocene shift that the Abstract calls "supported by Sr-Nd isotopic calculations" (p. 1, l. 25 to 26) is therefore not reproduced in magnitude for EDC. If the finding holds, the answer to aim 2 changes from "validated for glacial and interglacial intervals" to "consistent at EDC for the glacial interval", hence major. Which Delmonte 2004 work supplies the values of l. 238 is asked in GB-56; legend, symbols and table references of Figure 2 are GB-57, GB-58 and GB-59. Overlapping location with GB-07 (missing literature on Dome C provenance); this finding concerns the isotopic validation. |
| Suggestion | In Section 4.1 restrict the EDC agreement to the glacial interval or compare modelled and measured values for the same core and depth intervals (the EDC LGM and Holocene values of p. 7, l. 238 to 240, with their sample ages), report residuals with Monte Carlo uncertainty and an agreement measure per period, present Taylor Glacier and Berkner Island values as regional context with their own symbols, give the source of the Holocene values in l. 240 and add them to Table S4, and adjust p. 7, l. 227 to 228, the Abstract (p. 1, l. 25 to 26) and the Conclusion accordingly. |
| Status | Composition of Table S4, legend and wording verified (page images Suppl. p. 21, p. 1, 7, 8, 26); symbol position measured by instance AB; recomputed isotope values inferred (Python by instance SD); that the l. 240 values come from a source outside Table S4: inferred |
| Severity | major |
| Source | S4, AB, SD |

**GB-39 Several group sums in Sections 4.2 and 4.3 deviate from the sums of the Table S5 values by more than rounding.**

| Field | Content |
|---|---|
| Check | P1 |
| Location | p. 9, l. 276; p. 9, l. 292 to 295; p. 10, l. 321; p. 10, l. 326 |
| Quotation | "(here, PAT+AUS is ~77%)"; "with high-latitude sources totaling 84 %"; "compared to 61% in our record when combining PAT, CWA, and PAP" |
| Concern | From Table S5 (EDC): LGM PAT plus AUS = 65.7 plus 10.2 = 75.9 (text about 77); LGM PAT plus NZ = 79.9 (text about 79, p. 9, l. 293); LGM AUS plus SAF plus PAP = 10.2 plus 6.3 plus 3.6 = 20.1 (text about 21, l. 294); HS1 PAT plus NZ = 74.8 plus 7.1 = 81.9 (text 84, l. 295); Holocene PAT plus CWA plus PAP = 49.0 plus 0.0 plus 11.0 = 60.0, given as 61 in p. 10, l. 321 and as 60 in p. 10, l. 326, so the same quantity carries two values one page apart (Python). All deviations exceed the 0.5-point rounding tolerance; none changes a conclusion. The LGM NZ value in p. 9, l. 282 is GB-40. |
| Suggestion | Recompute the sums from Table S5 and write about 76 % (p. 9, l. 276), about 80 % and about 20 % (l. 293 to 294), 82 % (l. 295) and 60 % (p. 10, l. 321). |
| Status | Inputs verified (Table S5, page image Suppl. p. 22); sums inferred (Python) |
| Severity | minor |
| Source | S3 |

**GB-40 The mean LGM New Zealand contribution is given as about 11 % in the Discussion, but as 14 % in the Results, in Table S5 and in Figure 3.**

| Field | Content |
|---|---|
| Check | P2, P3 |
| Location | p. 9, l. 281 to 282; p. 7, l. 209; Figure 3, LGM panel, NZ (p. 27); Table S5 (Suppl. p. 22), row LGM, column NZ |
| Quotation | "However, we find a higher average NZ contribution (~11%), making it the second-largest dust source to EDC during the LGM." |
| Concern | Table S5 gives NZ LGM 14.2, the mean of the 40 LGM rows of Table S1 is 14.17 (Python), p. 7, l. 209 says 14 %, and instance AB measured the NZ mean cross of the LGM panel of Figure 3 at 14.0 % (median 15.4 %). About 11 % matches none of the EDC periods (MIS3 9.1, LGM 14.2, HS1 7.1). With 14.2 the sum PAT plus NZ of p. 9, l. 293 (about 79 %) is reproduced (65.7 plus 14.2 = 79.9); with 11 it is not. The ranking "second-largest" holds with either value, but the comparison with Coppo et al. (5 %) is understated. The other group sums of the same page are GB-39. |
| Suggestion | Replace "~11%" by "~14%" in p. 9, l. 282. |
| Status | verified (Table S5 at the page image, Figure 3 by measurement); mean inferred (Python) |
| Severity | moderate |
| Source | S3, AB |

**GB-41 The attributions of provenance changes to regional climate (aim 3) rest on visual coincidence, without a measure of agreement or chronological uncertainty.**

| Field | Content |
|---|---|
| Check | P10 |
| Location | p. 10, l. 338 to 339; p. 11, l. 371 to 372; Figure 5 (p. 29) |
| Quotation | "Overall, our Holocene provenance record for PAT contributions is matching well with the SWW intensity proxies in Potrok" |
| Concern | Aim 3 asks for shifts "in relation to regional climatic changes affecting the PSA". Section 4.3 (p. 10 to 12) compares single-sample peaks and minima with dated phases of other records, for example the AUS peak with the Darling dry phase (p. 11, l. 371 to 372). No correlation, lag or significance is given (search of p. 1 to 15 for "correlat": 2 hits, both on fit quality, p. 5, l. 168 and p. 6, l. 181), and the age uncertainty of EDC3 and of the regional records is not considered. Given the sample-to-sample scatter of GB-25, coincidences of single samples can arise by chance. The visibility of one such coincidence in Figure 5 is GB-43; the axes of Figure 5 are GB-62; the wording of p. 10, l. 338 is KK-47. |
| Suggestion | In Section 4.3 put the PAT, AUS and SAF shares and the regional records on a common time grid, compute correlations with age-uncertainty ensembles and test them against red-noise surrogates; otherwise phrase the links as hypotheses. |
| Status | Absence of a measure verified (search as stated); risk of chance coincidence inferred |
| Severity | moderate |
| Source | SD |

**GB-42 Figure 5 is cited before Figure 4, so the figure numbers do not follow the order of first citation.**

| Field | Content |
|---|---|
| Check | P3, P4 |
| Location | p. 10, l. 340; p. 12, l. 405 |
| Quotation | "Aike bog (see Figure 5)"; "Figures 4 and S5 (for millennial trends)" |
| Concern | First citations in the text (search for "Figure" and "Figures" on p. 1 to 15): Figure 1 p. 6, l. 183; Figure 2 p. 8, l. 244; Figure 3 p. 9, l. 281; Figure 5 p. 10, l. 340; Figure 4 p. 12, l. 405. All five figures are cited; only the order of 4 and 5 is reversed. The supplementary figures are first cited in order (PP-30). |
| Suggestion | Swap the numbers of Figures 4 and 5 with captions and all citations, or move the comparison with Potrok Aike behind Section 4.4. |
| Status | verified (search; page images p. 10 and 12) |
| Severity | minor |
| Source | AB, S4 |

**GB-43 Question to the authors: the PAT drop at 6 to 6.5 kyr BP, said to be also present in the Potrok Aike wind record, is not visible in Figure 5B.**

| Field | Content |
|---|---|
| Check | P24 |
| Location | p. 11, l. 350 to 351; Figure 5, panel B (p. 29) |
| Quotation | "Apart from a well-marked drop in PAT contributions between 6-6.5 kyr BP (also present in Potrok Aike wind intensity record)" |
| Concern | The PAT drop is clear in Figure 5A: instance AB measured the smoothed PAT at 33.8 % on average (minimum 28.4 %) between 6.0 and 6.5 kyr BP, against 50.1 % (5.0 to 6.0) and 49.7 % (6.5 to 7.0). In panel B (MDF axis calibrated on the ticks 10 and 60 mT) the smoothed MDF between 6.0 and 6.5 kyr BP is 16.9 to 18.0 mT (mean 17.4), against 18.1 (5.5 to 6.0) and 16.3 mT (6.5 to 7.0). The change is about 1 mT on an axis where the excursions between 8 and 11.5 kyr BP reach 41 mT, so no change of wind intensity at 6 to 6.5 kyr BP can be seen at this scale. It may exist in the original record at higher resolution. The general lack of a coincidence measure is GB-41. |
| Suggestion | Show the 6 to 7 kyr BP interval of the Potrok Aike record enlarged or give the MDF values of Lisé-Pronovost et al. (2015) that support "also present", or remove the parenthesis in p. 11, l. 350 to 351. |
| Status | Figure values verified by measurement (instance AB); whether the original record shows the drop: assumption, hence the question |
| Severity | moderate |
| Source | AB |

**GB-44 Figure S3, on which Section 4.3 builds its sub-regional argument, does not show the same per-sample values as Table S1 and Figure 1.**

| Field | Content |
|---|---|
| Check | P3 |
| Location | p. 11, l. 355 to 360; Figure S3, panels Altiplano, Puna and Etosha (Suppl. p. 6); Figure 1, panels PAP and SAF (p. 24); Table S1 (Suppl. p. 11 to 15) |
| Quotation | "Evolution of contribution to EDC from subregions of the Puna-Altiplano and Southern Africa PSA" |
| Concern | Several Figure S3 peaks agree with Table S1 in date and to within 2.1 points (Altiplano 32.9 % at 3559 yr, measured 30.8 % at 3559 yr; 34.6 % at 4863 yr, measured 34.0 % at 4859 yr), which shows that axis and dating are right (instance AB; x calibrated on the ticks 0.4 and 3.2, 1 px = 16 yr). Yet the largest Altiplano values of Table S1 are missing from Figure S3: at 8629 yr Table S1 gives 100.0 % and Figure 1 (PAP) shows 97.9 %, but Figure S3 has at most 5.7 % Altiplano and 2.4 % Puna within 120 yr; at 11228 yr Table S1 gives 97.0 % and Figure 1 96.0 %, Figure S3 at most 14.6 %; at 9957 yr Table S1 gives 75.7 %, Figure S3 at most 2.2 %. Conversely, Figure S3 shows peaks that Table S1 does not have: Altiplano 38.8 % and Puna 54.9 % at about 11.86 kyr BP and Etosha 88.5 % at 11854 yr BP, whereas Table S1 lists at most 0.5 % for Altiplano, Puna and SAF at 11779 and 11993 yr; and the SAF event of Table S1 (94.7 % at 12227 yr) appears in Figure 1 (raw SAF peak 93.8 % at 12239 yr) but not at that date in Figure S3. A reader cannot tell which data set carries the sub-regional results, on which Section 4.3 (p. 11, l. 355 to 360) and the link to paleolake Coipasa (aim 3) depend; hence major. The onset date derived from these curves is GB-45. |
| Suggestion | Regenerate Figure S3 from the same model run as Table S1 and Figure 1, or state in its caption which run or statistic it shows and why it differs; then recheck p. 11, l. 355 to 365 against the corrected figure. |
| Status | verified (measurement against Table S1 by instance AB; Table S1 values at the page images Suppl. p. 11 to 13) |
| Severity | major |
| Source | AB |

**GB-45 The onset of Southern Altiplano dust "only after approximately 11.2 kyr BP" is contradicted by Table S1 and Figure S3.**

| Field | Content |
|---|---|
| Check | P24 |
| Location | p. 11, l. 357 to 360; Figure S3, panel Altiplano (Suppl. p. 6); Table S1 (Suppl. p. 13), YD rows |
| Quotation | "Southern Altiplano begins contributing dust"; "only after approximately 11.2 kyr BP, a timing that coincides with the final desiccation of paleolake Coipasa" |
| Concern | Table S1 lists Altiplano contributions of 16.6 and 12.8 % in the two samples dated 12841 yr (page image Suppl. p. 13), and 7.8 % at 11117 yr; Figure S3 shows a raw peak of 38.8 % at 11856 yr BP and a smoothed curve above zero from 11.3 kyr BP to the end of the YD shading (instance AB). The earliest Altiplano contribution is therefore about 12.8 kyr BP in Table S1 and about 11.9 kyr BP in Figure S3, not 11.2 kyr BP. The coincidence with the final desiccation of paleolake Coipasa is argued from this date. The disagreement between Figure S3 and Table S1 in general is GB-44. |
| Suggestion | Give the first Altiplano contribution with its date from Table S1 (12.84 kyr BP), and either revise the link to the Coipasa desiccation or explain why the YD values are not counted. |
| Status | verified (Table S1 at the page image; Figure S3 by measurement of instance AB) |
| Severity | moderate |
| Source | AB |

**GB-46 One citation in the Discussion has no entry, and one entry is cited nowhere.**

| Field | Content |
|---|---|
| Check | P4 |
| Location | p. 11, l. 365; p. 18, l. 630 to 632 |
| Quotation | "with the previous Pb isotopic study (Gili et al., 2016)" |
| Concern | The reference list has Gili et al. entries for 2017 and 2022 only. Search for "Gaiero et al., 2007", "Gaiero et al. 2007" and "Gaiero et al. (2007)" in the main text, the captions and the supplement: 0 hits; "Gaiero, 2007" (p. 8, l. 274; p. 26, l. 862) belongs to the single-author entry (p. 18, l. 619). Is the 2007 entry by Gaiero, Brunet, Probst and Depetris (p. 18, l. 630 to 632) intended for one of the "Gaiero, 2007" citations? Spelling and year mismatches of other citations are KK-45, KK-51, KK-56, KK-66 and KK-77; the spacing of the same citation is KK-54. |
| Suggestion | Add the entry for Gili et al. (2016) or correct the citation in p. 11, l. 365; cite the Gaiero et al. (2007) entry at the intended place or delete it. |
| Status | verified (two-way comparison of 145 citation occurrences with 91 entries by instance S4; page images p. 11, 17 and 18) |
| Severity | minor |
| Source | S4 |

**GB-47 Two figure references in the Discussion point to figures that do not show the cited content.**

| Field | Content |
|---|---|
| Check | P3, P4 |
| Location | p. 12, l. 382; p. 13, l. 449 to 450 |
| Quotation | "increasing trend in SAF dust contribution to EDC ice core (Figure S4)" |
| Concern | Figure S4 shows box plots per period without a time axis and without a Late Holocene panel under that name (GB-60), so no Holocene trend can be read from it; the SAF time series are in Figure 1 and, by sub-region, in Figure S3. In p. 13, l. 449 to 450 Figures S2 and S5 are cited for a decline of deposition "in both cores", but Figure S5 shows relative contributions only and Figure S2 the nssCa2+ flux of EDC only; no figure shows total deposition at EDML. |
| Suggestion | In p. 12, l. 382 cite "Figure 1; Figure S3"; in p. 13, l. 449 to 450 cite Figure S2 for EDC and a source or an added panel for EDML deposition, and drop Figure S5 from that reference. |
| Status | verified (page images p. 12, 13, Suppl. p. 4 and 8) |
| Severity | minor |
| Source | AB, S4 |

**GB-48 The Holocene comparison of EDC and EDML uses different time windows: Figure 4 and the text compare the whole EDC Holocene with the EDML Early Holocene, not the overlap named in the text.**

| Field | Content |
|---|---|
| Check | P9, P21, P3 |
| Location | p. 12, l. 405 to 407; p. 13, l. 423 to 424; Figure 4, bars "Holo" (p. 28); Table S5 (Suppl. p. 22) |
| Quotation | "over their overlapping interval shared by both datasets, i.e., between 7.5 and 27 kyr BP" |
| Concern | Table S5 gives EDML only for the Early Holocene (7.5 to 11.7 kyr), EDC for 2.8 to 11.7 kyr. The differences of p. 13, l. 424 equal EDC Holocene minus EDML Early Holocene (PAT 49.0 minus 62.7 = minus 13.7; AUS 23.1 minus 10.8 = plus 12.3). Figure 4 shows the same: instance AB measured the Holo bars at PAT minus 13.8, AUS plus 12.2, SAF minus 0.4, NZ about 0, PAP plus 1.3, and instance SD at minus 13.6 and plus 12.1. With the stated overlap (EDC Early Holocene, 56 samples) the differences are PAT minus 15.6, AUS plus 14.1, SAF minus 1.4, NZ plus 2.6, PAP plus 0.6 (Python). Half of the EDC Holocene samples (60 of 116) lie outside the stated overlap. The direction of the result remains; the stated values and the figure do not follow the stated design. For the LGM the effect is small (PP-33). Whether the EDML values themselves are correct is GB-06, the model configuration GB-17; the first citation of Figure 4 in l. 405 is GB-42. Overlapping location with GB-37 (strength and timing of the ACR shift); this finding concerns the Holocene comparison window. |
| Suggestion | Compare EDC Early Holocene with EDML Early Holocene in Figure 4, Table S5 and p. 13, l. 423 to 424, label the category "Early Holocene (7.5 to 11.7 kyr BP)", and name the windows in the caption of Figure 4. |
| Status | Table S5 values verified (page image Suppl. p. 22); Figure 4 bars measured by instances AB and SD; differences inferred (Python) |
| Severity | moderate |
| Source | S3, AB, SD |

**GB-49 The number of Younger Dryas samples at EDC is given as 7, but Table S1 lists 9 samples in the YD block, and Table S5 is their mean.**

| Field | Content |
|---|---|
| Check | P2 |
| Location | p. 12, l. 407 to 409; Table S1 (Suppl. p. 13), YD block |
| Quotation | "due to the limited number samples covering those periods in EDC (8 and 7 samples in ACR and YD, respectively" |
| Concern | The manuscript rightly flags the small sample size for ACR and YD, and the ACR count of 8 is correct (13032 to 14601 yr). The YD block holds 9 rows (11779, 11993, 12227, 12477, 12588, 12754, 12841, 12841, 12867), counted at the page image Suppl. p. 13 and with Python (ages 11700 to below 12900: n = 9). Even if the two rows dated 12841 were one sample (GB-11), the count would be 8, not 7. The YD row of Table S5 is reproduced exactly by the mean over these 9 rows (PAT 63.06, PAP 4.52, SAF 14.63, AUS 14.50, NZ 3.28). The same sentence lacks "of" ("limited number samples"). The placement of the caveat is part of GB-37; the comparison window of the preceding sentence is GB-48. Overlapping location with GB-10 (the naming of PSA and DS and the caption of Table S1); GB-18 (the unreported Monte Carlo uncertainty); GB-20 (the R threshold); GB-25 (Holocene variability confounded with noise and sampling); GB-28 (the YD SAF mean driven by one sample); GB-30 (the South Altiplano and South Puna values); GB-34 (the row sum of 93.5 % in Table S1); GB-36 (the word "continuous"); this finding concerns the YD sample count. |
| Suggestion | Write in p. 12, l. 408 "the limited number of samples covering those periods in EDC (8 and 9 samples in ACR and YD, respectively", or explain which rows are not counted as separate samples. |
| Status | verified (page image Suppl. p. 13; Python) |
| Severity | moderate |
| Source | S3, SD, S4 |

**GB-50 The text gives the PAT enrichment of EDC over EDML for the ACR and YD with swapped values, and the loss of Southern African dust that it names does not hold for the YD.**

| Field | Content |
|---|---|
| Check | P2, P1, P3 |
| Location | p. 13, l. 421 to 422; Figure 4, panels PAT and SAF, bars YD and ACR (p. 28); Table S5 (Suppl. p. 22) |
| Quotation | "In contrast, the ACR and YD intervals exhibit a slight enrichment of Patagonian dust (+4 and +6.5%) in EDC, primarily at the expense of Southern African and Australian contributions." |
| Concern | From Table S5: ACR PAT 68.9 minus 62.5 = plus 6.4; YD PAT 63.1 minus 58.4 = plus 4.7 (Python). Read in the order of the sentence, plus 4 belongs to the ACR and plus 6.5 to the YD, so the values are swapped. Figure 4 agrees with Table S5 (instance AB measured PAT ACR plus 6.2, YD plus 4.6). For SAF, ACR is 8.0 minus 12.4 = minus 4.4, but YD 14.6 minus 8.2 = plus 6.4 (measured plus 6.2), so in the YD EDC receives more Southern African dust than EDML; the YD deficit falls on AUS (minus 4.5), NZ (minus 3.9) and PAP (minus 2.4). The YD SAF surplus is driven by one sample (GB-28). Overlapping location with GB-17 (model configuration and chronology of EDC and EDML); GB-48 (the Holocene comparison window); this finding concerns the swapped ACR and YD values. |
| Suggestion | In p. 13, l. 422 write "(+6.4 and +4.7 %, respectively)" and restrict "at the expense of Southern African and Australian contributions" to the ACR; for the YD name AUS, NZ and PAP. |
| Status | Table S5 values verified (page image Suppl. p. 22); differences inferred (Python); Figure 4 by measurement (instance AB) |
| Severity | moderate |
| Source | S3, AB |

**GB-51 Vallelonga et al. (2002), a study of lead pollution at Law Dome, is cited for Australian regions as significant contributors of dust to Antarctica.**

| Field | Content |
|---|---|
| Check | P13 |
| Location | p. 13, l. 438 to 440; p. 21, l. 807 to 810 |
| Quotation | "Other studies have similarly identified regions in Australia as"; "significant contributors to both western and eastern Antarctica" |
| Concern | The entry is "The lead pollution history of Law Dome, Antarctica, from isotopic measurements on ice cores: 1500 AD to 1989 AD" (p. 21, l. 807 to 809). Its abstract attributes a major pollution event at Law Dome between 1884 and 1908 AD to "Pb mined at Broken Hill and smelted at Broken Hill and Port Pirie, Australia", and gives "an average rock and soil dust Pb contribution of 8-12%" without naming Australia as the source of that dust. The abstract thus shows Australia as a source of anthropogenic lead, not of mineral dust, which is the subject of the sentence in p. 13, l. 438 to 440. Raised by instance S1 as a note outside its segment; no instance with a source check for Segment 4 treated it; confirmed here. The citation of De Deckker in the same sentence is KK-66. Question to the authors: does the full text support Australian mineral dust as a contributor? Overlapping location with GB-02 (relative shares read as absolute inputs); this finding concerns Vallelonga et al. (2002) as a dust source. |
| Suggestion | Replace Vallelonga et al. (2002) in p. 13, l. 440 by a study of mineral dust provenance, or restrict the statement to lead. |
| Status | verified for the abstract (NOAA dataset record of the article with its abstract, https://paleo.ltrr.arizona.edu/json/noaa-icecore-11918.json); for the full text: assumption, hence the question |
| Severity | minor |
| Source | ZF |

**GB-52 Section 4.4 and the Conclusion state the causal mechanisms with "demonstrate", "confirm" and "due to", although the results contain no data on sea level, drainage or transport, and Section 4.2 itself says "likely".**

| Field | Content |
|---|---|
| Check | P15 |
| Location | p. 14, l. 466 to 468; p. 14, l. 480 to 484; p. 9, l. 296 to 298 |
| Quotation | "Importantly, our data demonstrate that these feedback mechanisms influenced dust deposition not only in EDML"; "As such those results confirm our previous study on the EDML dust record"; "18 and 15 kyr BP due to changing atmospheric transport dynamics" |
| Concern | The Results (p. 6, l. 173 to p. 7, l. 218) report provenance shares only. The mechanisms (shelf submergence by Meltwater Pulse 1A, drainage reversal, enhanced rainout) come from literature cited in the Discussion and are not tested against EDC data. Section 4.2 formulates the transport explanation for the flux decline as "likely" (p. 9, l. 296), but the Conclusion turns it into "due to" (p. 14, l. 484). The EDC data show that the provenance shift is synchronous with that at EDML; they do not "demonstrate" that the mechanisms acted at EDC, and they "confirm" the shift seen at EDML, not its ascription. The same applies to "a significantly larger variability" (p. 9, l. 306; see GB-25). The Abstract uses the appropriate verb "We attribute" (p. 1, l. 29). The verbs carry the answer to aim 3; with the wording corrected, the mechanism is a supported hypothesis, not a shown result, hence major. The term "feedback" is KK-68, the article in l. 481 KK-69. |
| Suggestion | Replace "demonstrate" (p. 14, l. 466) by "are consistent with the hypothesis that", "confirm our previous study ... that we ascribed to" (l. 480 to 482) by "confirm the shift found in EDML, which we ascribed to", and "due to" (l. 484) by "most likely due to". |
| Status | verified (wording at the page images p. 9 and 14; absence of sea-level, drainage or transport data checked by reading p. 6, l. 173 to p. 7, l. 218) |
| Severity | major |
| Source | S4 |

**GB-53 The Conclusion explains the EDC and EDML differences by climatic dynamics in the source areas, whereas Section 4.4 explains them by the position of the two sites relative to atmospheric circulation.**

| Field | Content |
|---|---|
| Check | P15 |
| Location | p. 14, l. 486 to 487; p. 13, l. 424 to 425 |
| Quotation | "SAF, NZ and AUS differed reflecting regional climatic dynamics in their respective source areas"; "These differences are consistent with the geographic positioning of the two sites" |
| Concern | Section 4.4 attributes the between-core differences to the storm track over EDML, the polar vortex over EDC, Rossby-wave intrusions and the STJ and PFJ pathway (p. 13, l. 425 to 440). Climatic changes in the source areas would affect both cores alike and cannot by themselves explain a difference between them; Section 4.4 uses source-area aridity only for the Holocene increase of low-latitude sources at EDC (p. 13, l. 440 to 443). The concluding sentence thus names a different cause than the Discussion from which it should follow (aim 4). The comparability of the two records is GB-17. Overlapping location with GB-08 (aims 1 and 2 in the Conclusion); this finding concerns the cause of EDC and EDML differences in the Conclusion. |
| Suggestion | Rewrite p. 14, l. 486 to 487 so that it reflects Section 4.4, for example "differed, which we relate to the different exposure of the two sites to mid-latitude air masses and to the pathways of low-latitude dust". |
| Status | verified (page images p. 13 and 14) |
| Severity | moderate |
| Source | S4 |

**GB-54 The data availability statement claims that all data are in the paper or supplement, but the EDC input REE data, the correction factors, the Monte Carlo inputs, the code and most model outputs are neither published there nor addressed by the statement.**

| Field | Content |
|---|---|
| Check | P12, P8, P35 |
| Location | p. 16, l. 494 to 496; p. 4, l. 107 to 109; p. 4, l. 118 to 124; p. 5, l. 140; p. 5, l. 155 to 158; Figure S2 (Suppl. p. 3 to 4); Table S1 (Suppl. p. 11 to 15) |
| Quotation | "All data needed to evaluate the conclusions in the paper are present in the paper and/or the Supplementary Materials. Additional data related to the paper may be requested from the authors." |
| Concern | The supplement publishes the source database (Table S2) and the median PSA contributions with R for 241 samples (Table S1). Against the data sources named in the Methods (PP-10), the following are neither in the paper or supplement nor addressed by the statement: (1) the 279 UCC-normalised EDC REE patterns that form the right-hand vector of Eq. (2); Gabrielli et al. (2010) report the 294 samples with summary statistics only (their Table 2), no per-sample values (article text read; its supplementary file was not read); (2) the element-specific correction factors cf_i and their variability; Gabrielli et al. (2010) give leachable fractions only per element group; (3) the element-specific analytical uncertainties used in the Monte Carlo runs (only the range 2 to 10 %, p. 5, l. 155 to 156); (4) the DEPOT implementation (MATLAB code with lsqnonneg, the Monte Carlo wrapper, the aggregation), with version and random seed; the heading reads "CODE/DATA AVAILABILITY", but the statement says nothing about code; (5) derived outputs: the identity of the 15 and 38 excluded samples (GB-24), the per-DS contributions (GB-26), the Monte Carlo spread (GB-18) and the absolute PSA fluxes (GB-19). How the PSA medians are combined is not stated either: 175 of the 241 rows of Table S1 sum to exactly 100.0 %, 65 to 99.9 to 100.1 %, and one to 93.5 % (GB-34), which suggests a renormalisation that the Methods do not mention. The second sentence of the statement withholds data without a reason, although no data concern persons. Without items 1 to 4 the record in Table S1 cannot be recomputed. The flux conversion in p. 5, l. 166 to 167 is GB-19; the term "MIS 3" in p. 4, l. 109 is KK-15. Overlapping location with GB-02 (relative shares read as absolute inputs); GB-12 (the concentration basis of the fit); this finding concerns data and code availability. |
| Suggestion | Deposit in a public repository with a DOI (for example PANGAEA or Zenodo) the 279 DIC REE patterns as used (raw and UCC-normalised, corrected), the cf_i values with their uncertainties, the analytical uncertainties per element, the MATLAB code with version and seed, the list of excluded samples with reason, the per-DS and per-PSA Monte Carlo results and the PSA fluxes; rewrite p. 16, l. 494 to 496 to list each item with its location, and state in Section 2 how the PSA medians are aggregated and normalised. |
| Status | Content of the manuscript and supplement verified (text layer, page images Suppl. p. 3, 4 and 11); Gabrielli et al. (2010) verified for the article text (full text, author copy, https://bpcrc.osu.edu/sites/default/files/2020-12/QSR Gabrielli 2010.pdf); that its supplementary file holds no EDC per-sample data: inferred; row sums verified by instance SD with Python; that the EDC REE data are in no public archive: assumption, put as a question to the authors |
| Severity | moderate |
| Source | S2, SD |

**GB-55 The author contribution statement credits the measurements to "P.B", initials that match none of the seven authors, and does not name who produced the new SAF data.**

| Field | Content |
|---|---|
| Check | P38, P4 |
| Location | p. 16, l. 497 to 498; p. 1, l. 4 to 5 |
| Quotation | "P.B performed the measurements; A.V., St. B and G.L. developed together the model" |
| Concern | The authors (p. 1, l. 4 to 5) are Sibylle Boxho, Aubry Vanderstraeten, Nadine Mattielli, Goulven G. Laruelle, Aloys Bory, Paolo Gabrielli and Steeve Bonneville. No author has the initials P.B.; the author who measured the EDC REE data in the cited source is Paolo Gabrielli. Is "P.B" meant to be "P.G."? The two authors with initials S.B. are abbreviated in three forms ("Si.B", "St. B", "St.B."); N.M. and A.B. are named only in "All authors reviewed the manuscript". Who measured the six new SAF patterns (GB-09) is not said. |
| Suggestion | Correct the initials in p. 16, l. 497, write "Si.B." and "St.B." uniformly, state the contributions of N.M. and A.B., and name who produced the new SAF data. |
| Status | Mismatch verified (page images p. 1 and 16); intended person: assumption, hence the question |
| Severity | minor |
| Source | S2, S4 |

**GB-56 The supplement cites at least six sources for the source database and the ice-core isotope values that are not in the reference list, and "Delmonte et al., 2004a" points to a work the list does not contain.**

| Field | Content |
|---|---|
| Check | P4 |
| Location | p. 7, l. 238; reference list (p. 16 to 22); Table S2 (Suppl. p. 16 to 19), column Reference; Table S4 (Suppl. p. 21), column Reference |
| Quotation | "Delmonte et al. (2004) reported 87Sr/86Sr ratios of ~0.708" |
| Concern | The supplement has no reference list of its own. These citations in it have no entry in the main reference list: Marx and Kamber (2010) and McGowan et al. (2005) (AUS block of Table S2), Marx et al. (2005) (AUS and NZ blocks), Diaz et al. (2018) (ANT block), Aarons et al. (2017) (18 rows of Table S4) and Bory et al. (2010) (14 rows of Table S4) (search in the main text: 0 hits each, "McGowan" only as co-author of Speirs et al. 2010; rows counted at the page image Suppl. p. 21 by instance S4). Most AUS end-members, all ANT end-members (GB-16) and 32 of the 35 measured isotope values of Figure 2 (GB-38) thus cannot be traced to a publication. "Delmonte et al., 2004a" implies a second Delmonte 2004 work, but the list has one entry, "Dust size evidence for opposite regional atmospheric circulation changes over east Antarctica during the last climatic transition" (Climate Dynamics 23, 427 to 438). Delmonte et al. (2004), "Comparing the Epica and Vostok dust records during the last 220,000 years: stratigraphical correlation and provenance in glacial periods", Earth-Science Reviews 66, 63 to 87, https://doi.org/10.1016/j.earscirev.2003.10.004, reports Sr and Nd isotopes of glacial Dome C dust in its abstract. Is this the work intended in Table S4 and in p. 7, l. 238? The Table S2 rows are also the objects of GB-21 and GB-22. Overlapping location with GB-09 (the six new SAF patterns); GB-13 (the identifiability of the unmixing); GB-14 (size fractions and pattern numbers per region); GB-15 (the AUS and ANT counts of Table S2); this finding concerns supplement citations missing from the reference list. |
| Suggestion | Add full entries for Marx and Kamber (2010), Marx et al. (2005), McGowan et al. (2005), Diaz et al. (2018), Aarons et al. (2017) and Bory et al. (2010) to the reference list, or add a reference list to the supplement; resolve "2004a" by adding the second Delmonte 2004 work and labelling both entries 2004a and 2004b in the list, in p. 7, l. 238, p. 12, l. 416 and the caption of Figure 2, or remove the letter. |
| Status | Citations verified (page images Suppl. p. 17 to 19 and 21); absence from the list verified (comparison with the 91 entries); Earth-Science Reviews record and abstract verified (https://www.documentation.ird.fr/hor/PAR00000018); Climate Dynamics abstract verified (https://www.iceandclimate.nbi.ku.dk/publications/papers/abstracts/Abstract202/); which 2004 work supplies the values of l. 238: assumption, hence the question |
| Severity | moderate |
| Source | S4 |

**GB-57 Three table references in the captions of Figures 2 and 4 point to the wrong supplementary table.**

| Field | Content |
|---|---|
| Check | P3, P4 |
| Location | p. 26, l. 858; p. 26, l. 865 to 866; p. 28, l. 876 |
| Quotation | "cores (refs. Table S1, - open symbols)"; "the isotopic fingerprint (Table S4)"; "between EDC and EDML ice cores (Table S4)" |
| Concern | Table S1 holds the median PSA contributions per sample; the measured ice-core isotope values with references are in Table S4 ("Measured isotopic values in ice core"). The isotopic fingerprints and elemental concentrations of the PSA end-members are both in Table S3, not Table S4. The EDC and EDML period means behind Figure 4 are in Table S5; the measured bars match the Table S5 differences (PP-48). Table headings read at the page images Suppl. p. 11, 20, 21 and 22. Abbreviations in the same captions are GB-32. |
| Suggestion | Figure 2 caption: "(refs. Table S4, open symbols)" and "(ii) the isotopic fingerprint and elemental concentration of the PSA end-members (Table S3)"; Figure 4 caption: "between EDC and EDML ice cores (Table S5)". |
| Status | verified (page images p. 26, 28, Suppl. p. 11, 20 to 22) |
| Severity | minor |
| Source | AB, S4, SD |

**GB-58 The legend of Figure 2 uses categories that neither the caption nor Table S4 define.**

| Field | Content |
|---|---|
| Check | P29 |
| Location | Figure 2, legend (p. 26); p. 26, l. 857 to 866; p. 8, l. 251 to 252 |
| Quotation | "The modeled isotopic signatures for the end of MIS3/LGM" |
| Concern | The legend separates "Early Holocene" and "Holocene" for modelled and measured symbols; "Holocene" includes the Early Holocene, and the caption does not say that it means the Late Holocene. Table S4 has no "Early Holocene" group, so the split of the measured values cannot be traced. "Iso" is not explained. The text says that the end of MIS3 and the LGM are shown in blue, whereas the legend lists only "EDC LGM". The label "Southern Central Western Argentina" differs from "Central Western Argentina (CWA)" in p. 4, l. 129. Colours match legend and text (instance AB: #fc5454, #c40404, #fcc404, #34cc34, #34ccfc, #0404fc). The caption table references are GB-57; the provenance of the measured symbols is GB-38. |
| Suggestion | Rename the legend entries "Early Holocene (7.5 to 11.7 kyr)" and "Late Holocene (2.8 to 7.5 kyr)", explain "Iso" as measured ice-core data, label the blue symbols "MIS3 and LGM" if MIS3 samples are included, assign each Table S4 row to its legend group, and use "Central Western Argentina" throughout. |
| Status | verified (page images p. 8 and 26) |
| Severity | minor |
| Source | AB |

**GB-59 One YD symbol in Figure 2 lies at the Southern African end-member, which the description "cluster around lower 87Sr/86Sr and higher ε(Nd)" omits.**

| Field | Content |
|---|---|
| Check | P3 |
| Location | Figure 2, filled yellow symbol at the lower right (p. 26); p. 8, l. 252 to 253 |
| Quotation | "Figure 2 by blue, cyan, green, and yellow filled symbols) cluster around lower 87Sr/86Sr and higher ε(Nd)" |
| Concern | The symbol in the "EDC YD" legend colour measures 0.7275 and minus 17.88 (instance AB). Recomputed with Eq. 3 and 4 and Table S3 for the YD sample at 12227 yr (Table S1: SAF 94.7 %, AUS 5.3 %) it should lie at 0.72745 and minus 17.87, so the figure and the calculation agree. The text describes the YD as clustering with the glacial symbols, while one YD sample is nearly pure Southern African dust; it is the sample that drives the YD SAF mean (GB-28). The legend is GB-58, the isotopic validation as a whole GB-38. |
| Suggestion | Add in p. 8, l. 253 that one YD sample (12.23 kyr BP) plots at the SAF end-member, and say how it affects the YD period mean. |
| Status | verified (measurement and recalculation by instance AB) |
| Severity | minor |
| Source | AB |

**GB-60 The panel of Figure 3 labelled "Holocene" shows the Early Holocene only, and the panel "Early Holocene" of Figure S4 shows the Late Holocene.**

| Field | Content |
|---|---|
| Check | P3 |
| Location | p. 27, l. 869; Figure 3, left panel (p. 27); Figure S4, panel "Early Holocene" (Suppl. p. 8) |
| Quotation | "Box plots of provenance contributions (in %) of Holocene, and Last Glacial Maximum (LGM)" |
| Concern | Instance AB measured box edges and medians and compared them with quartiles computed from Table S1 (the method reproduces the LGM panel: PAT 58.8, 65.7, 71.6 measured against 58.9, 65.8, 71.7). For the "Holocene" panel the measured PAT Q1, median and Q3 are 12.2, 55.1 and 72.9 %, the PAT mean cross 47.0 %; the Early Holocene (7.5 to 11.7 kyr, n = 56) gives 12.3, 55.2, 73.0 and mean 47.1, the whole Holocene (n = 116) 18.4, 58.6, 73.8 and mean 49.0. The panel "Early Holocene" of Figure S4 measures PAT 18.9, 61.6 and 80.7 %, which matches the Late Holocene (2.8 to 7.5 kyr, n = 60: 18.9, 61.7, 80.7). The text quotes means for the whole Holocene (p. 10, l. 316 to 318), so Figure 3 does not show the distribution the text discusses. Instance SD logged that Figures 3 and S4 cover all periods of Table S5 without a finding; that log did not compare the panels with the data, so the measured finding stands. The whiskers of the same figures are GB-61. Overlapping location with GB-40 (the LGM NZ value); this finding concerns the Holocene panels of Figures 3 and S4. |
| Suggestion | Recompute the left panel of Figure 3 for 2.8 to 11.7 kyr BP or relabel it "Early Holocene (7.5 to 11.7 kyr BP)"; relabel the first panel of Figure S4 "Late Holocene" or replace it; state n per period in both captions. |
| Status | verified (measurement and recalculation from Table S1 by instance AB) |
| Severity | moderate |
| Source | AB |

**GB-61 The whiskers in Figures 3 and S4 are not the "lower and upper extremes" stated in the captions.**

| Field | Content |
|---|---|
| Check | P29 |
| Location | p. 27, l. 872; Figure 3 (p. 27); Figure S4, caption (Suppl. p. 7) |
| Quotation | "the whiskers indicate the lower and upper extremes" |
| Concern | Points are plotted beyond the whiskers in both figures (Figure 3, Holocene SAF up to 54 %, NZ up to 90 %). For the Holocene panel of Figure 3 (Early Holocene data, GB-60) instance AB measured the upper whisker ends at SAF 25.5 %, NZ 16.4 %, PAP 28.0 % and AUS 79.8 %. These equal the largest values below Q3 plus 1.5 IQR from Table S1, while the maxima are 54.3, 90.4, 100.0 and 98.1 %. The whiskers follow the 1.5 IQR rule; a reader who takes the caption literally reads the whisker end as the maximum. Overlapping location with GB-40 (the LGM NZ value); this finding concerns the whiskers of Figures 3 and S4. |
| Suggestion | Change the captions of Figure 3 and Figure S4 to "whiskers extend to the most extreme values within 1.5 times the interquartile range; points beyond them are shown individually". |
| Status | verified (measurement against Table S1 by instance AB) |
| Severity | minor |
| Source | AB |

**GB-62 Figure 5 cannot be read without the text: the time axis has no title, unit or multiplier, and the shaded bands are not explained.**

| Field | Content |
|---|---|
| Check | P29 |
| Location | p. 29, l. 880 to 882; Figure 5, panels A and B (p. 29) |
| Quotation | "Comparison of the contribution of Patagonian dust (PAT) to EDC ice core (A) and (B) the Median Destructive Field" |
| Concern | Both x axes carry only the numbers 0.5 to 3, without "Time (yr BP)" and without the factor 10^4 shown in Figure 1. Instance AB measured grey bands at 11.71 to 12.89, 14.68 to 18.01 and from 28.98 kyr BP (the periods of Figure 1) and a blue band with dashed edges from 7.90 to 11.48 kyr BP; the caption explains neither, and the period names are missing. The arrow "Wind intensity" with minus and plus signs implies that low MDF means strong wind; the caption does not say so, nor whether the 9-step average also applies to panel B. The word "mobile" in l. 882 is KK-28; the use of the figure for the climate link is GB-41 and GB-43. |
| Suggestion | Add "Time (kyr BP)" with the correct numbers to both x axes, name the grey bands (YD, HS1, MIS3) in the caption, explain the blue band, and state that the MDF axis is inverted so that up means stronger westerlies. |
| Status | verified (measurement by instance AB, page image p. 29) |
| Severity | minor |
| Source | AB |

**GB-63 Figure S2 lacks units on all three y axes and the period shading in panel B.**

| Field | Content |
|---|---|
| Check | P29 |
| Location | Figure S2, panels A to C (Suppl. p. 4); Figure S2, caption (Suppl. p. 3) |
| Quotation | "nssCa2+ flux"; "δ18O"; "deuterium excess" |
| Concern | The text gives the flux unit as µg m⁻² yr⁻¹ (p. 5, l. 166), but the axis has none; δ18O and deuterium excess have no per-mil sign. Panels A and C carry grey period bands (11.71 to 12.90, 14.70 to 18.01 and from 29.0 kyr BP), panel B has none, and the period labels appear only in C. Panel B ends at 31.0 kyr BP, while A and C run to 33.7 to 34.0 kyr BP. The y tick labels of panel B are minus 49.05, minus 51.05 and so on, not round values (all measured by instance AB). That Figure S2 shows no PSA fluxes is GB-19. Overlapping location with GB-02 (relative shares read as absolute inputs); GB-54 (data and code availability); this finding concerns the units of Figure S2. |
| Suggestion | Add units ("nssCa2+ flux (µg m⁻² yr⁻¹)", "δ18O (‰)", "deuterium excess (‰)"), add the shading to panel B, extend it to the full record and use round tick values. |
| Status | verified (measurement by instance AB, page image Suppl. p. 4) |
| Severity | minor |
| Source | AB |

**GB-64 In Figure S5 the shaded period bands are offset against the time axis of the PAT panel, and the EDML legend entry is almost invisible.**

| Field | Content |
|---|---|
| Check | P3 |
| Location | Figure S5, all panels (Suppl. p. 10) |
| Quotation | "Comparison between EDC and EDML ice cores in terms of dust provenance contributions" |
| Concern | The bands run through all panels at the same pixel columns, but the axis of the PAT panel (7 at 391 px, 27 at 3044 px) is shifted against the other panels (7 at 374 px, 27 at 3040 px). The YD band therefore reads 11.56 to 12.88 kyr BP in the PAT panel and 11.67 to 12.98 kyr BP in the others, HS1 14.68 to 17.89 and 14.77 to 17.96 (instance AB). The legend entry "EDML" is set in #dcecf4 on white (contrast 1.21 to 1); the EDC entry in #5c9cd4 has 2.93 to 1. The y-axis title of the same figure is KK-82. |
| Suggestion | Align the axis of the PAT panel with the other panels or draw the bands per panel, and set the EDML legend text in a darker shade. |
| Status | verified (measurement by instance AB) |
| Severity | minor |
| Source | AB |

#### Minor corrections

| ID | Location | Quotation | Replacement | Source |
|---|---|---|---|---|
| KK-29 | p. 7, l. 220 | "in the Epica" | "in the EPICA"; compared with p. 1, l. 2 and 18 and p. 3, l. 88, all "EPICA Dome C" (page images p. 1, 3, 7); the claims of the same sentence are GB-01 and GB-36 | S2, S4 |
| KK-30 | p. 7, l. 229 | "regional climatic evolution (3)" | "regional climatic evolution; and (3)" | S4 |
| KK-31 | p. 7, l. 233 | "highlight a major shift in dust provenance occurred" | "highlight that a major shift in dust provenance occurred"; the content of the sentence is GB-37 | S4 |
| KK-32 | p. 7, l. 236 | "This shift already describes by Gili et al. (2022) and Vanderstraeten et al. (2023), appears" | "This shift, already described by Gili et al. (2022) and Vanderstraeten et al. (2023), appears"; see GB-37 | S4 |
| KK-33 | p. 7, l. 242; p. 11, l. 374 | "(Basile et al. 1997; Delmonte et al. 2007)"; "(Gingele et al. 2007;" | "(Basile et al., 1997; Delmonte et al., 2007)"; "(Gingele et al., 2007;" | S4 |
| KK-34 | p. 8, l. 246 | "e.i. Eq.3" | "i.e. Eq. 3" | S4 |
| KK-35 | p. 8, l. 249 | "where the mean isotopic signatures is represents by CIR" | "where CIR PSA represents the mean isotopic signature of each PSA" | S4 |
| KK-36 | p. 8, l. 261 | "Persistance of high-latitude dust source to EDC" | "Persistence of high-latitude dust sources to EDC" | S4 |
| KK-37 | p. 8, l. 270 | "~763.10" (followed by a superscript 3) | "~763 × 10³ km²" | S4 |
| KK-38 | p. 8, l. 272 | "those from SSA- to EDC" | "those from SSA to EDC" | S4 |
| KK-39 | p. 9, l. 290; Table S3 (Suppl. p. 20), rows 5 and 6 | "South Altiplano" (p. 9, l. 290); "S-Puna", "S-Altiplano" (Table S3) | "Southern Altiplano" in the text, as in p. 4, l. 130 and p. 11, l. 358 and 362; "South Puna" and "Southern Altiplano" in Table S3; search for "South Altiplano", "Southern Altiplano" and "S-Altiplano": main text 5 hits (2 "South", 3 "Southern"), supplement text 1 hit; the place p. 7, l. 213 is corrected within GB-30 | S2 |
| KK-40 | p. 9, l. 300 | "before 14.5 kyr BP reflect a transport regime" | "before 14.5 kyr BP reflects a transport regime" | S4 |
| KK-41 | p. 9, l. 303 to 304 | "until 2.7 kyr BP" | "until 2.9 kyr BP", as in p. 1, l. 18 and p. 6, l. 182 | S3 |
| KK-42 | p. 10, l. 311 | "«wet scavenging»" | "\"wet scavenging\"" (English quotation marks) | S4 |
| KK-43 | p. 10, l. 325 | "input -down to 33%-" | "input (down to 33%)" | S4 |
| KK-44 | p. 10, l. 329 to 330 | "includes several McMurdo region sites (Section 4.2)" | "includes several McMurdo region sites (Section 2; Table S2)"; Section 4.2 does not mention the McMurdo sites, which are described in p. 4, l. 132 to 133; the Antarctic end-members are GB-16, the missing literature GB-07 | S4 |
| KK-45 | p. 10, l. 334 | "(Speirs et al., 2001)" | "(Speirs et al., 2010)" (entry p. 21, l. 781); see GB-16 for the argument of the same paragraph | S4 |
| KK-46 | p. 10, l. 336 | "ACR, YD reaching minimum values" | "ACR and YD, reaching minimum values" | S4 |
| KK-47 | p. 10, l. 338 | "centered ~9 kyrs BP" | "centered ~9 kyr BP"; the climate link of the next sentence is GB-41 | S4 |
| KK-48 | p. 10, l. 339 to 340; p. 11, l. 348 to 349 | "Potrok" and "Aike bog" (across the line break, both places) | "Laguna Potrok Aike", as in the caption of Figure 5 (p. 29, l. 882); both places confirmed at the page images; see GB-41 and GB-42 for the same sentence | AB |
| KK-49 | p. 10, l. 340 to 341 | "weakening of South Westerlies" and "Winds (SWW)" (across the line break) | "weakening of the Southern Westerly Winds (SWW)"; same sentence as KK-48 and the figure citation of GB-42 | S4 |
| KK-50 | p. 10, l. 341 | "Moreno et al. (2010);" | "Moreno et al., 2010;"; same sentence as KK-49 | S4 |
| KK-51 | p. 10, l. 342 to 343 | "(Quake and" and "Kaplan, 2017)" (across the line break) | "(Quade and Kaplan, 2017)" (entry p. 20, l. 755) | S4 |
| KK-52 | p. 10, l. 346 | "Fires co-emit mineral soil-dust particle" | "Fires co-emit mineral soil-dust particles" | S4 |
| KK-53 | p. 11, l. 354 | "Dust emission from PAP are" | "Dust emissions from PAP are" | S4 |
| KK-54 | p. 11, l. 365 | "(Gili et al., 2016) ." | "(Gili et al., 2016)."; the missing entry is GB-46 | S4 |
| KK-55 | p. 11, l. 366 | "As far as Australian dust contribution, our model" | "As far as the Australian dust contribution is concerned, our model"; the content of the sentence is GB-21 and GB-26 | S4 |
| KK-56 | p. 11, l. 367 | "De Deccker et al. (2010)" | "De Deckker et al. (2010)"; see GB-26 for the attribution of the same sentence; overlapping location with GB-21 (the duplicated Darling and Murray patterns), where a different point is treated | S4 |
| KK-57 | p. 11, l. 374 to 375 | "(post-7.5 kry BP)" | "(post-7.5 kyr BP)"; same line as the citation of KK-33 | S4 |
| KK-58 | p. 11, l. 376 | "El-Nino-Southern Oscillation" | "El Niño Southern Oscillation (ENSO)" | S4 |
| KK-59 | p. 12, l. 384 to 385 | "suggesting strengthened dust transport from southern Africa suggesting strengthened dust transport from southern Africa" | "suggesting strengthened dust transport from southern Africa" (clause printed twice, confirmed at the page image); the SAF statements of the next sentence are GB-09 and GB-26 | S4 |
| KK-60 | p. 12, l. 396 | "include few substantial inputs" | "include a few substantial inputs" | S4 |
| KK-61 | p. 12, l. 397 to 398 | "during the LGIT (~15.4" | close the parenthesis opened in l. 397, for example "during the LGIT (about 15.4 to 13.6, 11.5 to 8.4 and 5.5 to 4.0 kyr BP; Brook et al., 2011)." | S4 |
| KK-62 | p. 12, l. 399 | "likely reflect their low-frequency, high-magnitude nature of their dust emissions" | "likely reflect the low-frequency, high-magnitude nature of their dust emissions" | S4 |
| KK-63 | p. 13, l. 426 | "receive dust from Patagonia dust brought" | "receive Patagonian dust brought" | S4 |
| KK-64 | p. 13, l. 427 | "located at the interior of EAP" | "located in the interior of the East Antarctic Plateau (EAP)"; "EAP" occurs once in the text layer and is not defined | S4 |
| KK-65 | p. 13, l. 428 | "such mid-latitude air masses incursions" | "such incursions of mid-latitude air masses" | S4 |
| KK-66 | p. 13, l. 439 | "(De Deccker et al., 2019;" | "(De Deckker, 2019;" (single-author entry p. 17, l. 551); the other source of the same sentence is GB-51 | S4 |
| KK-67 | p. 14, l. 457 | "redirecting large portion of river catchment" | "redirecting a large portion of the river catchments" | S4 |
| KK-68 | p. 14, l. 467; p. 14, l. 488 | "these feedback mechanisms"; "hydrological feedbacks" | "these mechanisms"; "hydrological changes"; the processes named act as forcings of dust emission, and no feedback loop is described; the verb strength of l. 466 is GB-52 | S4 |
| KK-69 | p. 14, l. 481 | "showing similar shift" | "showing a similar shift"; the claim of the sentence is GB-52; overlapping location with GB-08 (aims 1 and 2 in the Conclusion), where a different point is treated | S4 |
| KK-70 | p. 16, l. 501 | "APPENDIX S. SUPPLENTARY DATA. Supplementary data to this article" | "APPENDIX S. SUPPLEMENTARY DATA. Supplementary data to this article are available online." | S4 |
| KK-71 | References, 18 entries with printed RTF codes, for example p. 16, l. 528 (Bullard and McTainsh 2003); further p. 17 to 22 as listed by instance S4 (De Deckker et al. 2014, Dukes et al. 2018, Engelbrecht et al. 2019, Fletcher and Moreno 2012, Gaiero et al. 2007, Gingele and De Deckker 2005, Grousset and Biscaye 2005, Lisé-Pronovost et al. 2015, Markgraf et al. 2007, Markle et al. 2018, Moreno et al. 2010, Power et al. 2008, Quade and Kaplan 2017, Stone et al. 2010, Stuut et al. 2002, Veres et al. 2013, Wagner et al. 2021) | "\uc0" codes and a backslash after the DOI, as printed in p. 16, l. 528 | Replace every RTF code by its character (page ranges and compound names with a hyphen or en rule as in the journal style, apostrophes in O'Loingsigh and O'Neal, "í", "é", "ñ", "°", prime and double prime, colon) and delete the trailing backslash after each DOI; 33 codes and 18 trailing backslashes counted in the text layer, all printed at the page images p. 16 to 22 | S4 |
| KK-72 | p. 17, l. 584 to 585; p. 18, l. 633 to 636; p. 22, l. 844 to 846 | "Ding, Q., Steig, E., Battisti, D. et al. Winter warming"; "Gaiero, D. M., L. Simonella, S. Gassó"; "Yang, Y., Carey-Smith, T., & Turner, R. (2024)." | Bring the three entries into the format of the other 88 entries (all authors with surname first, year after the authors without parentheses, no "&"), for example "Yang, Y., Carey-Smith, T., Turner, R., 2024. ..." | S4 |
| KK-73 | p. 20, l. 726 to 729 | "chronology for the EPICA Dome C ice core. Clim. Past." | Add volume, page range and DOI to the entry of Parrenin et al. (2007), as in the other journal entries | S4 |
| KK-74 | p. 20, l. 732 | "doi: https://doi.org/10.1130/B25770.1" | "https://doi.org/10.1130/B25770.1" | S4 |
| KK-75 | p. 20, l. 748 | "Environùental characterization" | "Environmental characterization" | S4 |
| KK-76 | p. 20, l. 763 | "Holland HD, Turkian KK (eds)" | "Holland, H.D., Turekian, K.K. (Eds.)" | S4 |
| KK-77 | p. 21, l. 800; citation p. 8, l. 266 | "Sudgen, D. E., McCulloch, R. D." | "Sugden, D. E., McCulloch, R. D." (the text cites "Sugden et al., 2009") | S4 |
| KK-78 | p. 26, l. 863 | "Note that the SAF and AUS domain is more extended than showed in the Figure." | "Note that the SAF and AUS domains extend beyond the plotted area."; the legend of the same figure is GB-58 | S4, AB |
| KK-79 | Figure 2, x axis (p. 26); Figure 3, y axes (p. 27); Table S3 (Suppl. p. 20); Table S4 (Suppl. p. 21); Figure S4, y axis (Suppl. p. 8) | "0,700"; "0,7060"; "0,7086"; "100,00" | Decimal points as in the main text: "0.700", "0.7060", "0.7086", "100" (all values in these elements); Figure 2 is also the object of GB-38, GB-58 and GB-59 | S4, AB |
| KK-80 | p. 28, l. 875 | "Histograms representing" | "Bar charts representing" (the panels show one bar per period, not a frequency distribution) | AB |
| KK-81 | Figure S4, caption (Suppl. p. 7) | "Antarctica Cold Reveal (ACR), (4) Heindrich Stadial 1 (HS1), and (5) Marine Isotope 3 (MIS3)" | "Antarctic Cold Reversal (ACR), (4) Heinrich Stadial 1 (HS1), and (5) Marine Isotope Stage 3 (MIS3)", as in p. 6, l. 184 to 186 | S2, S4, AB |
| KK-82 | Figure S5, y-axis title (Suppl. p. 10) | "PAS EDC Contribution and PSA EDML Contribution ( in %)" | "PSA contribution to EDC and EDML (in %)"; the bands and legend of the same figure are GB-64; overlapping location with KK-28 ("moving average"), where a different point is treated | S4, AB |

#### Verification log

| ID | Check | Checked | Values | Result |
|---|---|---|---|---|
| PP-34 | P15 | Each statement of the Conclusion (p. 14, l. 472 to p. 15, l. 492) assigned to a place in Results or Discussion | "first high-resolution, continuous" (l. 472): p. 6, l. 182 to 183, limited by p. 4, l. 113 (GB-36); glacial to interglacial shift (l. 473 to 474): Table S5, supported; MIS3, LGM, HS1 dominated by PAT and NZ (l. 474 to 476): supported; "From ~14.5 kyr BP onward" (l. 477 to 480): GB-37; "confirm our previous study" and "due to" (l. 480 to 484): GB-52; EDC and EDML "broadly synchronous" (l. 486): p. 13, l. 444 to 447, supported; "regional climatic dynamics" (l. 487): GB-53; "biogeochemical fluxes" (l. 491): no place, GB-04 | findings as named; the other statements have a place in the Results |
| PP-35 | P15, P9 | Outlook and proposals in the Conclusion; aims and frames of the Introduction taken up | Search in p. 14, l. 472 to p. 15, l. 492 for "future", "further", "should", "need", "recommend", "perspective", "outlook", "next": 0 hits (instances S4 and SD); aims: (1) taken up l. 472, Holocene question not (GB-08); (2) not in the Conclusion (GB-08, content GB-38); (3) taken up l. 488 to 492 (GB-37, GB-52); (4) taken up l. 484 to 487 (GB-53); frame iron fertilisation not taken up (GB-04); frame westerlies taken up p. 10, l. 339 to 352 and p. 13, l. 425 to 427 | no finding for the outlook (there is none); findings GB-04 and GB-08 |
| PP-36 | P13 | p. 10, l. 319 to 323: DustCOMM values from Kok et al. (2021) | Full text (https://acp.copernicus.org/articles/21/8169/2021/), Section 3.4.1: South America about 70 %, Australia about 20 %, southern Africa about 10 %; "± 20%" and the ranges "6% to 36%" and "3% to 13%" not found in the text; Table 2 is an image and was not readable | no finding; the uncertainty ranges could not be checked (limit of this review) |
| PP-37 | P13 | p. 7, l. 236 and p. 11, l. 381: Gili et al. (2022) | Full text, open access (https://www.nature.com/articles/s43247-022-00464-z): southern African signature in archives during warm periods; mixing diagrams, no percentage contribution for EDC | no finding; the source does not anticipate a quantification at EDC |
| PP-38 | P15 | Comparison values in Section 4.4 (p. 13, l. 417 to 424) against Table S5 (EDC minus EDML) | LGM: PAT minus 8.0, NZ plus 8.0; HS1: PAT plus 3.2, PAP minus 0.2, SAF minus 5.3, AUS plus 1.9, NZ plus 0.6; ACR: PAT plus 6.4, SAF minus 4.4, AUS minus 7.4; YD: PAT plus 4.7, SAF plus 6.4, AUS minus 4.5; Holocene variants: minus 13.7 and plus 12.3, or minus 15.6 and plus 14.1 | LGM and HS1 statements (l. 417 to 421) agree; ACR and YD are GB-50, the Holocene GB-48 |
| PP-39 | P4 | Numbering of sections, equations, figures and tables, page images p. 2 to 29 and Suppl. p. 1 to 22 | Sections 1, 2, 3, 4, 4.1 to 4.4, 5 (one unnumbered subheading in Section 2, p. 3, l. 100); Eq. (1) to (4) at p. 4, l. 125, p. 5, l. 141, p. 8, l. 247 and 250; Figures 1 to 5 and S1 to S5, Tables S1 to S5, each number once | no gap and no duplicate number; order of Figures 4 and 5 is GB-42 |
| PP-40 | P4 | Every reference to a section, equation, figure, table or supplement element, checked against its target | 56 references in text and captions (instance S4); wrong targets at p. 4, l. 127 (KK-16), p. 5, l. 159 (KK-19), p. 10, l. 329 to 330 (KK-44), p. 12, l. 382 (GB-47), p. 26, l. 858 and 865, p. 28, l. 876 (GB-57); Table S1 is cited in p. 6, l. 183 for period summaries but lists samples; all other targets match, among them p. 5, l. 167 and p. 9, l. 296, 299, 312 (Figure S2 panels), p. 6, l. 191 and 216, p. 9, l. 281, 295 and 318 (Table S5), p. 8, l. 246 (Table S3), p. 11, l. 355 (Figure S3) | findings as named |
| PP-41 | P4 | Two-way comparison of citations and reference list, main text p. 1 to 15, captions p. 25 to 29 and supplement citations | 145 citation occurrences, 91 entries, 83 matched; citations without matching entry: Sugden 2009, Speirs 2001, Quake and Kaplan 2017, De Deccker 2010 and 2019, Gili 2016; entries without citation in the main text: Gaiero et al. 2007, EPICA Community Members 2006 (cited only in the caption of Figure S2); "et al." rule: 9 two-author entries cited with "and", 5 single-author entries, only De Deckker 2019 cited with "et al."; supplement citations without entry listed in GB-56 | findings GB-46, GB-56, KK-45, KK-51, KK-56, KK-66, KK-77; DOIs not resolved (optional check) |
| PP-42 | P16 | Language and typesetting of p. 7 to 29 and of the supplement elements of Segment 4, each observation at the page image | Pages read at the image p. 7 to 22 and 25 to 29, Suppl. p. 6, 7, 8, 10, 13, 21; RTF codes 33 and trailing backslashes 18; breaks inside DOIs at p. 16, l. 509 to 510 and 524 to 525, p. 17, l. 563 to 564, p. 20, l. 746 to 747, p. 22, l. 835 to 836 are breaks at a hyphen or slash of the DOI itself | findings KK-29 to KK-82 as far as they concern Segment 4; DOI breaks: no finding |
| PP-43 | P30, P37 | Reported errors and corrections; corrected values in figures and tables | No error or correction reported; the cf correction is applied to all samples and stated in Section 2; no later recalculation reported | no finding |
| PP-44 | P3 | Figure 2: legend colours against the text, recomputation of one symbol, counting of symbols | Legend colours match p. 8, l. 252 and 255; symbol at 0.7275 and minus 17.88 recomputed as 0.72745 and minus 17.87 from Table S1 and Table S3 (GB-59); open symbol at 0.7228 and minus 14.17 equals Berkner Island in Table S4 (GB-38); counts of dot-shaped components per colour are lower bounds because symbols overlap at 0.706 to 0.712 (instance AB) | no finding from counting; the overlap is a limit of this check |
| PP-45 | P3 | Figure 3, LGM panel, against Table S1 (18 to 29 kyr, n = 40) | Measured Q1, median, Q3: PAT 58.8, 65.7, 71.6 (table 58.9, 65.8, 71.7); AUS 5.7, 10.2, 13.9 (5.8, 10.2, 14.0); SAF 1.7, 4.6, 7.6 (1.8, 4.6, 7.6); NZ 10.8, 15.4, 18.9 (10.8, 15.5, 18.9); NZ mean cross 14.0 (14.2) | no finding for the LGM panel; Holocene panel GB-60, NZ value of the text GB-40 |
| PP-46 | P34 | Box plots and period figures (instance SD) | Figure 3 (Holocene, LGM) and Figure S4 (other periods) cover all periods of Table S5; Figure S3 shows PAP and SAF sub-regions | no finding on coverage; the measured content of the panels is GB-60, where this log entry was weighed against the measurement of instance AB |
| PP-47 | P3 | Figure S4, panels YD, ACR, HS1 and MIS3, PAT boxes, against Table S1 | Measured Q1, median, Q3: YD 47.9, 71.4, 86.3 (table, n = 9: 47.1, 70.2, 84.8); ACR 58.0, 74.3, 81.4 (57.2, 73.2, 80.2); HS1 68.1, 76.0, 80.5 (67.0, 75.0, 79.4); MIS3 63.4, 71.6, 78.4 (62.5, 70.5, 77.2) | no finding; uniform offset of about 1 point, too small to change any statement |
| PP-48 | P3 | Figure 4 bars against Table S5 differences and p. 13, l. 417 to 424 | Measured (uncertainty about 0.4): PAT YD plus 4.6, ACR plus 6.2, HS1 plus 3.0, LGM minus 8.0; AUS YD minus 4.3, ACR minus 7.2, HS1 plus 1.9; SAF YD plus 6.2, ACR minus 4.3, HS1 minus 5.1, LGM minus 2.7; NZ YD minus 3.9, ACR plus 3.0, LGM plus 7.5; PAP YD minus 2.2, ACR plus 1.6, LGM plus 1.7; Table S5: plus 4.7, plus 6.4, plus 3.2, minus 8.0; minus 4.5, minus 7.4, plus 1.9; plus 6.4, minus 4.4, minus 5.3, minus 2.7; minus 3.9, plus 3.4, plus 8.0; minus 2.4, plus 1.8, plus 2.2 | no finding for these bars; Holo bars GB-48, text on ACR and YD GB-50 |
| PP-49 | P24, P3 | Figure 5 against p. 10, l. 336 to p. 11, l. 352 | PAT smoothed below 5 kyr BP: mean 52.7 %, range 39.8 to 61.3 % (text p. 11, l. 352: "50-55%"); MDF smoothed 8.0 to 9.0 kyr BP mean 26.8 mT with excursions from 8.14 kyr BP (text p. 11, l. 348: "After 8.1 kyr BP"); YD band of panel B ends 0.12 kyr later than in panel A | no finding except GB-43 and GB-62 |
| PP-50 | P24 | Figure S2 against p. 9, l. 296 to 299, p. 10, l. 312 and p. 13, l. 448 to 449 | nssCa2+ smoothed flux 868 at 22.0, 534 at 18.0, 40 at 15.0, 22 at 14.0 kyr BP; δ18O smoothed minus 55.9 at 18 and minus 52.3 at 15 kyr BP; text: decline of flux and rise of δ18O from about 18 to 15 kyr BP | no finding; axis units GB-63 |
| PP-51 | P24, P3 | Figure S3 against p. 11, l. 355 to 357 and p. 12, l. 392 to 398 | Puna mean per Holocene bin (Table S1) 2.5, 2.1, 4.3, 5.0 % from old to young, increasing toward the present as l. 357 says; Sua peaks between 8.31 and 3.46 kyr BP (text "between ~8.2 and 2.8 kyr BP"); Etosha peaks between 11.85 and 5.17 kyr BP (text "between ~12.2 and ~5.1 kyr BP") | no finding for these dates; Altiplano and Puna values GB-44 and GB-45 |
| PP-52 | P29 | Font size of Figures 2, 4 and S2 to S5 | Figure 2: legend 6.0 pt, axis numbers 7.3 pt; Figure 4: tick numbers 6.7 pt, category labels 5.7 to 6.3 pt; Figures S2 and S3 8.3 pt; Figure S4 10.7 to 11.0 pt; Figure S5 12.0 to 13.7 pt (instance AB) | no finding (Figure 4 labels within the method uncertainty of 6 pt); Figures 1, 3 and 5 are GB-31 |
| PP-53 | P3 | EDC PAT curve of Figure S5 against Figure 1 (both 9-step average) at 16 ages from 7.5 to 25 kyr BP | Differences up to 12 points on steep flanks (9.0 kyr BP: 41.4 against 53.5 %); minima and plateaus agree (for example 10.13 kyr BP: 26.3 against 22.7 %) | no finding |
| PP-54 | P3 | Residues and hidden elements on p. 24 to 29 and Suppl. p. 2 to 10 | Text layer of Figure S5 contains "x 1000" in the AUS panel, not visible on the rendered page; no placeholders, watermarks or cut labels | no finding (not visible) |
| PP-55 | merging (ZF) | Pflichtfelder, duplicates, contradictions and pairs of overlapping locations over all six instance reports (steps 4.1 to 4.3 and 4.6 of the skill) | Instance findings: S1 5, S2 6, S3 21, S4 10, AB 23, SD 17, together 82; all had the required fields; merged into 61 findings (21 findings absorbed into others; S2-GB-02 and SD-GB-15 each split into two findings by object); minor corrections: 97, of which 11 absorbed into findings and 11 merged with each other, giving 75; added by the merger from notes outside the checklists: 3 findings (GB-16, GB-22, GB-51) and 7 minor corrections (KK-04, KK-05, KK-11, KK-14, KK-17, KK-18, KK-26); contradictions decided at the manuscript: South Puna count 8 (GB-30), SAF "~2%" (GB-29 against PP-29), unmarked gap (GB-33 against PP-15), Figure 3 and S4 panels (GB-60 against PP-46); every pair of overlapping locations listed by formatpruefung.py with the option for pairs was decided as merged or kept separate with a cross-reference | 0 findings discarded |
| PP-56 | wording (ZF) | Every quotation and every embedded quotation of the findings and minor corrections, searched in the text layer of manuscript and supplement with line breaks joined; embedded counts recomputed | 280 quoted strings checked by script, and the printed line of each match in a Quotation field compared with the location given; strings not found in the text layer are search terms, quotations from cited sources, suggested wording, and labels inside raster figures (checked at the page images); two locations extended to the last line of their quotation (GB-21 to p. 11, l. 367; GB-55 to p. 16, l. 498); counts recomputed with Python from Table S1 (241 rows) and Table S2 (217 rows): spacings, period means, row sums, threshold counts, Puna and Altiplano rows, group counts, coordinate pairs, outliers; searches repeated for GB-01, GB-04, GB-08, GB-13, GB-14, GB-17, GB-18, GB-19, GB-41 and KK-15, KK-39, KK-64; two counts of the instances corrected (uncertainty terms 11 instead of 13 hits; "flux" 11 matches instead of 10) | all quotations found at the stated locations |
| PP-57 | locations (ZF) | Every location listed by formatpruefung.py with the option for locations, counted from the nearest printed margin number | The text layer counts lines per page (randzeilen false), so the script lists 392 locations; 313 lie between two printed margin numbers of the text layer on the same page and were confirmed by counting from them; 75 lie before the first or after the last printed number of a page, next to equations or in captions and were counted at the page images (p. 3, 4, 5, 6, 7, 9, 10, 11, 12, 13, 14, 15, 16, 25 and the caption pages 26 to 29 from their printed numbers 860, 865, 870, 875 and 880; p. 4: equation l. 125, l. 126 to 129 counted from 130; p. 5: equation l. 141, l. 142 to 144 counted from 145; p. 8: equations l. 247 and 250); 4 on p. 25, where the text layer has no number, were counted at the page image from the printed 855 below the caption of Figure 1 | all locations confirmed; ranges across a page break are written "p. x, l. a to p. y, l. b" |
| PP-58 | notes (ZF) | Notes outside the checklists of all six instances, decided by step 4.4 of the skill | Became findings because no responsible instance treated them and the page images confirmed them: ANT normalisation (GB-16), Table S2 typing errors (GB-22), Vallelonga et al. (2002) (GB-51), chronology of the period limits (added to GB-17), spaced hyphens, EDML expansion, "camples", "subdivised", "matrixes", "LREE" (KK-04, KK-05, KK-11, KK-14, KK-17, KK-18, KK-26); not taken because a responsible instance had treated the place: AUS "rose after 14.7 kyr BP" (p. 6, l. 203 to 204, PP-25), single ANT sample 3654 (PP-27), symbols per sample in Figure 2 (PP-44), Coppo et al. (2022) percentages (not readable, limit); the remaining notes duplicated findings or corrections and were merged there | 11 notes turned into findings or corrections; 4 notes not taken |

## Optional checks

| Area | What it needs | Responsible | Run |
|---|---|---|---|
| DOI resolution | one request per reference entry with a DOI | `science-quellenapparat-pruefung` | no |
| Citation style | the name of the style or the style rules of the journal | `science-zitierstil-harvard-ctr` or the style rules of the journal | no |
| AI statement against publisher policy | the publisher's policy on the use of AI | this review, on request | no |
| Relation to the authors' own previous work | the previous work of the authors | this review, on request | no |
| Journal requirements | the author guidelines of the target journal | this review, on request | no |
| Subject accuracy | access to the sources of the checked statements and a selection of sections | `science-faktenbeleg-pruefung`, `geo-frage-belegbasiert-klaeren` | no |

## Limits of this review

- Checked version: egusphere-2025-5046.pdf, 29 pages, SHA-256 f598b53d01e375844cfb549eb05b9a3407bb30cae553e603c125d5f14886c722, with supplement egusphere-2025-5046-supplement.pdf, 22 pages, SHA-256 759cfa14195948f5772d3d6d696081932424f4296e51c812415527ed3b108ea6.
- Sources not readable or only partly readable: Vanderstraeten et al. (2023), full text (abstract only); Coppo et al. (2022), full text (abstract only), so the percentages attributed to it in p. 9, l. 278 to 279 and p. 10, l. 324 to 328 were not checked; Delmonte et al. (2007), (2008) and (2017); Paleari et al. (2019); Kok et al. (2021), Table 2 (image); Siggaard-Andersen et al. (2007), Engelbrecht et al. (2019), Martínez-García et al. (2014) and Vallelonga et al. (2002), full texts (abstracts only); Lambert et al. (2008), full text (preview only); the supplementary file of Gabrielli et al. (2010); Lisé-Pronovost et al. (2015); Marino et al. (2008); Qu (2016) and Shi et al. (2009, 2011, 2015) not checked.
- Findings with status assumption in at least one part: 15 of 64 (GB-03, GB-06, GB-09, GB-11, GB-12, GB-14, GB-16, GB-17, GB-21, GB-22, GB-43, GB-51, GB-54, GB-55, GB-56); findings whose central statement has the status assumption and that are therefore phrased as questions: 6 of 64 (GB-03, GB-12, GB-14, GB-16, GB-43, GB-51).
- Optional checks run: 0 of 6.
- Omitted instances: none; the six review instances ran as separate agents.
- Discarded findings: 0. All 82 substantive findings of the instances had the required fields and were confirmed or reconciled at the manuscript; they were merged into 61 findings, and the merger added 3 (PP-55).
- Measurements in figures (font sizes, curve values, bar heights, symbol positions) were made by instance AB at 300 dpi and are taken over with its stated calibration; the recovery simulations in GB-13 and the isotope recalculation in GB-38 were made by instance SD under the assumptions stated there and are no measurement of DEPOT itself.
