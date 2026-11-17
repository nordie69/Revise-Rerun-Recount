# Review report: Energy and structural evolution process of high-altitude and long-runout landslides induced by a strong earthquake

| Field | Value |
|---|---|
| Manuscript | Ge, Y., Hu, B., Tang, H., Fu, X. and Zhu, L. (2025) Energy and structural evolution process of high-altitude and long-runout landslides induced by a strong earthquake. EGUsphere preprint egusphere-2025-4506, https://doi.org/10.5194/egusphere-2025-4506 |
| Checked version | egusphere-2025-4506.pdf, 29 pages, 5544638 bytes, SHA-256 64cb3787456244aa6102e34f776b47e9a612d06e8894d391758ae240dbe415d6 |
| Date | 2026-10-17 |
| Language | English |
| Review instances | Segments 1 to 4 (S1 to S4), figures (AB), study design (SD); the six review instances ran as separate agents; merge (ZF) in a further separate agent; no instance omitted |
| Note | Line numbers are the printed margin numbers of the manuscript (every fifth line printed), with intermediate lines counted from the nearest printed number on the page image. Between p. 13, l. 266 and p. 14, l. 269 the count is uncertain (four elements for three numbers); locations in Table 2 and at Fig6 are therefore given by page and element. Figure values marked as measured were measured on page images at 150 or 300 dpi by the instance named under Source. |

## Summary

The manuscript is a single case study with numerical modelling. It reconstructs the Mogangling rock landslide, triggered by the 1786 Kangding (Moxi) earthquake (Ms 7¾) on the Dadu River, Sichuan, with the three-dimensional discrete element code 3DEC. The pre-failure topography is restored by straightening contour lines of a UAV-derived DEM; the model has 25345 blocks, a landslide volume of 317563 m3, Mohr-Coulomb blocks and joints with the parameters of Table 1, viscous and free-field boundaries, and the acceleration record of the Luding station from the 2008 Wenchuan earthquake as a substitute input. One dynamic run of 131 s is reported. Kinetic, potential and dissipated energy (KE, PE, DE, with DE defined as ME(t0) minus ME(t)) are computed for the whole mass and for ten monitored blocks in four position groups; effective collisions are detected as velocity peaks above a 30 % prominence threshold (1,139 detections); alpha-shape envelopes at ten times give the indices volume swelling (VS) and area growth (AG), and a solid-to-fluidized transition is placed at VS 29.47 % and AG 319.5 %. Five conclusions state that contour restoration is feasible, that the simulation agrees with field imagery, that the whole mass conserves energy while single blocks do not, that front or lower blocks collide more and receive energy from the rear, and that collisions fragment the blocks and enlarge the envelope.

## Strengths

1. The energy bookkeeping is written out as Eqs. (1) to (4) and plotted as stacked bars of PE, KE and DE for the whole mass and for each of the ten blocks; because the definitions are explicit and the bars are drawn consistently with them (bar totals and timing measured in PP-35), a reader can check exactly what the energy figures show and what they cannot show (GB-40).
2. The ten monitored blocks are documented with position group, coordinates and volume in Table 2, and the group sizes 2, 3, 3 and 2 agree between text, Table 2 and the markers in Fig6 (PP-25, PP-26); this makes the block-level results traceable to individual blocks, which is what allows the inconsistencies in GB-34 and GB-44 to be located at all.
3. The choice of the prominence threshold for effective collisions is exposed rather than hidden: Fig5 (b) to (f) shows the detections for five thresholds from 10 % to 50 %, and the thresholds agree between text and caption (PP-21); the reader can see qualitatively how strongly the detection depends on the threshold, which is the starting point for the quantitative check asked for in GB-30.
4. The kinematic description is internally consistent where it can be checked: the stage velocities in the text match the colour bar maxima of Fig7, the model dimensions match the labels of Fig4, and the duration and time points agree across Fig7, Fig8, Fig9 and Fig11 (PP-17, PP-32, PP-34); in addition, the main input limitations (no structural-plane data, no 1786 ground-motion record, smoothed restored terrain) are disclosed where the affected method is introduced (PP-05, PP-39).

## Weaknesses

1. The central energy results do not rest on the simulation in the way stated: the constant sum of KE, PE and DE follows from the definition of DE as a residual, the absolute energies of the whole mass and of the blocks cannot be reconciled with any stated volume, density and datum, and energy transfer between blocks is inferred from that residual without being computed (GB-40, GB-41, GB-42, GB-44). The authors should state the mass and datum behind Fig8 and Fig9 and replace the conservation argument by an energy balance whose terms (frictional, damping and boundary work, seismic input) are taken independently from the solver.
2. The comparative results of the abstract and of Conclusions 4 and 5 have no reported basis: the Results contain no collision counts, energy receipts or travel distances per position group, Fig10 (b) pools all collisions over travel distance without population or normalisation, and fragmentation and the fluidization threshold are interpreted from envelope growth rather than measured, at a sampling that misses the KE maximum (GB-45, GB-46, GB-47, GB-49, GB-50). These statements should be derived from per-block and per-group tables and a direct fragmentation measure, or restricted to what Fig10 (b) and Fig12 show.
3. The reconstruction of the 1786 event rests on inputs that are not checked: the restored terrain is accepted visually, the field dimensions contradict each other and the map, the single substitute input is not varied, the steep planes that explain the failure mechanism may be the block grid, and the validation is a visual comparison with a deposit eroded for two centuries (GB-15, GB-17, GB-21, GB-23, GB-38). A quantitative test of the restoration, a sensitivity series for the input and the discretisation, and metric validation targets kept separate from any calibration are needed before the run can be read as a reproduction of the event.
4. Several steps cannot be rebuilt or traced: model settings (version, damping, time step, contact model), the prominence definition and the population behind the 1,139 collisions, the alpha-shape set-up and the field and laboratory bases of Table 1 are missing, data and code are available only on request, half of the cited works have no reference entry, and the study is not positioned against earlier work on Mogangling or against the first author's own energy-evolution study (GB-05, GB-06, GB-08, GB-02, GB-20, GB-26, GB-30, GB-36, GB-51). The authors should add a table of numerical settings, deposit inputs, outputs and scripts with a persistent identifier, and rewrite the introduction against the listed earlier studies.

## Findings by segment

### Segment 1: Abstract, introduction, state of research (p. 1 to 2)

#### Substantive findings

**GB-01 The trend claim in l. 33 to 34 is not supported by the cited works, and the citation "2019a" cannot be resolved.**

| Field | Content |
|---|---|
| Check | P13 |
| Location | p. 1, l. 33 to 34; p. 2, l. 56 to 57; reference list p. 26, l. 511 to 513 and p. 27, l. 530 to 536 |
| Quotation | "In recent years, the chain disasters of high-level rock landslides in high-intensity earthquake areas have shown a trend of frequent occurrence (Carpignano et al., 2009; Fan et al., 2019a)" |
| Concern | The sentence makes a temporal claim (more frequent occurrence in recent years). Carpignano et al. (2009) develop a decision support approach for multi-risk maps of the Piedmont Region (Italy); their abstract mentions neither landslides nor earthquakes and speaks of an increased vulnerability of society, not of more frequent events. The abstract of Fan et al. (2019, Rev. Geophys.) describes earthquake-induced hazard chains and an increased frequency of landslides that lasts for decades after an earthquake, that is, an elevated post-seismic rate in the affected area, not a trend over recent years. "2019a" cannot be resolved: the list has two entries Fan et al. 2019 without letters (p. 27, l. 530 to 532 and l. 533 to 536), and p. 2, l. 56 to 57 cites "Fan et al., 2019" without letter. Neither readable source supports the specific claim. Graded moderate: the claim is background and leaves the results unchanged, but a reader cannot check it. |
| Suggestion | In p. 1, l. 33 to 34 cite a work that documents an increase in frequency with data, or restate the sentence as what Fan et al. (2019) support (earthquakes frequently trigger chains of hazards such as rock landslides, landslide dams and outburst floods); remove Carpignano et al. (2009) here; label the two list entries "2019a" (Fan, Scaringi, Korup) and "2019b" (Fan, Yang et al.) and use the letters in l. 34 and l. 56 to 57. |
| Status | Carpignano et al. (2009): verified (abstract, https://ideas.repec.org/a/taf/jriskr/v12y2009i3-4p513-534.html, DOI 10.1080/13669870903050269). Fan et al. (2019): verified for the abstract (https://pubs.usgs.gov/publication/70204730, DOI 10.1029/2018RG000626); that the full text contains no trend statement is inferred (full text not read). Ambiguity of "2019a": verified on the page image p. 27. |
| Severity | moderate |
| Source | S1, S4 |

**GB-02 The introduction does not position the study against earlier studies of the Mogangling landslide; four of them are in the reference list without citation, and their volume, death toll and controlling fault differ from the manuscript without discussion.**

| Field | Content |
|---|---|
| Check | P14 |
| Location | p. 1, l. 38 to p. 2, l. 41; p. 5, l. 110 to 112; p. 7, l. 149 to 151; p. 10, l. 186 to 187; p. 15, l. 311 to 312 and l. 316 to 318; reference list p. 27, l. 546 to 548; p. 28, l. 588 to 590; p. 29, l. 600 to 605 |
| Quotation | "In this study, the Mogangling landslide that occurred in 1786 was repaired and reconstructed to study the formation mechanism and energy transfer process of high-level rock landslide induced by earthquake" |
| Concern | The comparison of simulated and observed deposits (Fig7 (o)) is a useful check against the field. The introduction, however, cites no earlier work on this landslide, although the list contains four that are never cited (PP-01): Wu et al. (2013) on its genetic mechanism and failure process; Zhao et al. (2021), whose abstract gives a volume of about 4500 × 10^4 m³ and over 100 000 deaths when the landslide dam broke; He et al. (2023), who recorded ground motion on the Mogangling slope and found the peak ground acceleration at the crest 5.3 times that near the toe; Zhou et al. (2024), who attribute the failure mainly to seismic amplification, back-slope effects and interface dynamic stress effects. The manuscript uses the same mechanisms (p. 15, l. 311 to 312 and l. 316 to 318) without citing them. It differs on three points without discussion. (1) Volume: p. 7, l. 151 gives 2400 × 10^4 m³; its own area and thickness give 4500 × 10^4 m³, the value of Zhao et al. (2021); the internal inconsistency itself is GB-15. (2) Death toll: p. 5, l. 111 to 112 "tens of thousands of people drowned", against over 100 000 deaths in Zhao et al. (2021) and in Dai et al. (2005). (3) Tectonic setting: p. 10, l. 186 to 187 assigns Mogangling to the Longmenshan system; Dai et al. (2005) state that seismic activity of the Kangding-Luding area is controlled primarily by the Xianshuihe fault zone, and the manuscript itself names the Xianshuihe, Longmenshan and Anninghe faults (p. 5, l. 97 to 99). Dai et al. (2005), the first detailed study of the 1786 landslide dam and its breach, is not in the list. The breach after 9 days (p. 5, l. 110 to 111) agrees with Dai et al. (2005). Whether the tectonic assignment affects the choice of input record is GB-23. |
| Suggestion | Add a paragraph after p. 2, l. 41 that summarises Dai et al. (2005), Wu et al. (2013), Zhao et al. (2021), He et al. (2023) and Zhou et al. (2024) and states what the present simulation adds; cite the sources of the case data in Sect. 2.1 (p. 5, l. 99 to 112; p. 7, l. 147 to 156) and reconcile volume, death toll and tectonic assignment with them or explain the differences; write "was reconstructed" instead of "was repaired and reconstructed" (p. 1, l. 38 to p. 2, l. 39). Missing work: Dai, F. C., Lee, C. F., Deng, J. H. and Tham, L. G. (2005) The 1786 earthquake-triggered landslide dam and subsequent dam-break flood on the Dadu River, southwestern China. Geomorphology, 65, 205 to 221, https://doi.org/10.1016/j.geomorph.2004.08.011; it is the reference account of the event being reconstructed and contradicts two of the case statements. |
| Status | Zhao et al. (2021): verified (abstract, https://ideas.repec.org/a/spr/nathaz/v106y2021i1d10.1007_s11069-020-04471-1.html). He et al. (2023): verified (abstract, https://link.springer.com/article/10.1007/s10346-023-02171-y). Zhou et al. (2024): verified (abstract, https://journal.hep.com.cn/jes/EN/1160318253862020026). Wu et al. (2013): inferred (title only). Dai et al. (2005): verified (full text PDF, https://wpg.forestry.oregonstate.edu/sites/default/files/seminars/2005_Daietal_geomorph.pdf); page numbers of the passages inferred. Volume arithmetic: inferred (computed). Absence of in-text citations: verified (PP-01). |
| Severity | moderate |
| Source | S1, S4 |

**GB-03 The aims announce a general law, energy accumulation, seismic effects and early warning, but the single-case design has no instrument for three of them, and the Conclusions take up neither these aims nor any limitation or outlook.**

| Field | Content |
|---|---|
| Check | P10, P15 |
| Location | p. 2, l. 39 to 41; p. 2, l. 65 to 73; p. 5, l. 122 to 125; title p. 1; Conclusions p. 25 to 26 |
| Quotation | "so as to summarize the law of high-level rock landslide induced by earthquake"; "it focuses on revealing the mechanisms of energy accumulation, transfer, and dissipation"; "The findings are intended to provide a theoretical foundation and scientific support for early warning and risk mitigation" |
| Concern | The manuscript states aims, not research questions (PP-05). (1) A law for a class of landslides is a generalising claim; the design has one case and one run, so no statement beyond Mogangling can be supported. (2) Energy accumulation has no measurement: the budget starts at ME(t0) equal to the initial potential energy (p. 13, l. 252), and no result section treats accumulation. (3) A search of the Conclusions (p. 25, l. 460 to p. 26, l. 492, text.json) gives 0 hits each for "seism", "earthquake", "warning", "risk", "mitigat", "accumulat", "formation mechanism", "high-altitude", "long-runout", "propagat", "debris flow", "Dadu", "dam", "hydropower", "limit", "future", "further stud" and "outlook"; "velocit" and "trajector" occur once each in other senses (l. 474 to 475, l. 465). The title names a strong earthquake as trigger and Sect. 3.1 describes P-wave and S-wave effects (p. 15, l. 306 to 318), but the Conclusions say nothing about the seismic loading, the velocity evolution or the application to the Dadu River area (p. 5, l. 122 to 125), and there is no discussion section. Unlike GB-02, which concerns the missing positioning against earlier studies in the same sentence, this finding concerns what the study answers for its own aims. Graded moderate: the case results remain; what changes is the reach the introduction announces. |
| Suggestion | Restate the aims in p. 2, l. 39 to 41 and l. 65 to 73 as case-specific research questions that one simulation can answer; drop "accumulation" or add a measure for it (elastic strain energy before failure, work of the seismic input); add to Sect. 4, or to a new discussion section, one statement each on the effect of the seismic input, on the velocity evolution, on what the results imply for hazard evaluation in the Dadu River area with the disclosed limits, and an outlook. If a general law is intended, a design with several cases or a parametric series (slope height, volume, input motion) is needed. |
| Status | verified (wording; search counts in text.json, confirmed on the page images p. 25 and 26); the reach of a single case is inferred |
| Severity | moderate |
| Source | SD, S4 |

**GB-04 The claims that pre-landslide terrain restoration is rare, mostly two-dimensional, and that contour restoration is a "new idea" give no literature search and leave out established three-dimensional reconstruction methods such as SLBL.**

| Field | Content |
|---|---|
| Check | P28, P14 |
| Location | p. 2, l. 42; p. 2, l. 46 to 51; p. 25, l. 463 to 468 |
| Quotation | "At present, in terms of surface terrain restoration, the terrain restoration before a landslide is less."; "For most numerical simulations involving terrain restoration, a two-dimensional simulation is more often used."; "which can provide a new idea of terrain restoration before a landslide for the same type of research." |
| Concern | The three claims about the state of the literature rest on no stated search: a search of text.json over the whole manuscript for "database", "Web of Science", "Scopus", "Google Scholar", "CNKI", "GeoRef", "search", "keyword" and "review" gives 10 substring hits, all inside "research", "reviewers" or a reference title (PP-04). The frequency claim of l. 46 to 47 is supported by three single case studies (Du et al., 2021; Cheng 2014; Li et al., 2024), whose abstracts, where read, mention neither a two-dimensional model nor terrain restoration (PP-01). Against the novelty claim stands an established method: Jaboyedoff et al. (2019) apply the sloping local base level (SLBL) method to lidar DEMs to estimate three-dimensional failure surfaces and to reconstruct deposits and pre-event topography for a landslide cluster of Typhoon Talas (2011), and report expansion coefficients of 10 to 25 %, a comparison value for the volume swelling at p. 25, l. 453. "Jaboyedoff" and "SLBL" give 0 hits in text.json, so the work is not in the list. The suggested wording change for l. 42 is part of this finding. |
| Suggestion | In p. 2, l. 42 to 51 state the search (databases, terms, period, date) or rephrase the three claims as non-exhaustive (for l. 42, for example "Few studies have restored the pre-landslide terrain"); position contour restoration against DEM-based reconstructions such as SLBL and cite: Jaboyedoff, M., Chigira, M., Arai, N., Derron, M.-H., Rudaz, B. and Tsou, C.-Y. (2019) Testing a failure surface prediction and deposit reconstruction method for a landslide cluster that occurred during Typhoon Talas (Japan). Earth Surface Dynamics, 7, 439 to 458, https://doi.org/10.5194/esurf-7-439-2019. |
| Status | Absence of a search description: verified (search of text.json). Jaboyedoff et al. (2019): verified (article page and abstract, https://esurf.copernicus.org/articles/7/439/2019/esurf-7-439-2019.html; final revised manuscript PDF https://esurf.copernicus.org/preprints/esurf-2018-61/esurf-2018-61-manuscript-version5.pdf). Du et al. (2021) and Li et al. (2024): verified for the abstracts; whether their full texts use two-dimensional models: inferred. |
| Severity | moderate |
| Source | S1, S4 |

**GB-05 Of the four works cited for image-, field- and GIS-based mapping in l. 43 to 46, two are numerical simulation studies by their titles and two have no entry in the reference list; could the authors check which works were meant?**

| Field | Content |
|---|---|
| Check | P13 |
| Location | p. 2, l. 42 to 46; reference list p. 28, l. 569 to 571 and l. 585 to 587 |
| Quotation | "For landslides that have not occurred too far away, the key information of landslide characteristics is often obtained through photos, field surveys, optical remote sensing images and UAV impact, so as to further build geomorphic maps through GIS (Geographic Information System) for subsequent analysis (Zhang et al., 2024; Song at al.2017; Fan et al., 2020; Wu et al., 2024)" |
| Concern | Song et al. (2017) is listed as "Landslide Deformation Prediction by Numerical Simulation in the Three Gorges, China" (p. 28, l. 569 to 571), Wu et al. (2024) as a numerical simulation of potential landslide-induced wave hazards (p. 28, l. 585 to 587). Neither title points to photo, field, remote sensing or UAV based mapping in GIS. Zhang et al. (2024) and Fan et al. (2020) have no entry with these years; whether they are the entries listed as 2023 and 2019 is discussed in GB-06. None of the four citations can therefore be confirmed as support for the sentence. The sentence also contains three wording errors ("not occurred too far away", "UAV impact", "Song at al.2017"), corrected here. The adjacent two-dimensional claim in l. 46 to 51 is GB-04. |
| Suggestion | In p. 2, l. 46 replace Song et al. (2017) and Wu et al. (2024) by works that report such mapping, or move them to the sentence on numerical simulations (l. 46 to 49); resolve Zhang et al. (2024) and Fan et al. (2020) as in GB-06; reword l. 43 to 44 as "For recent landslides, ... optical remote sensing and UAV imagery" and write "Song et al., 2017". |
| Status | Content of Song et al. (2017) and Wu et al. (2024): inferred (titles from the reference list; no abstract page found). Missing list entries: verified (page images p. 27 and 29; search of text.json). Wording: verified (page image p. 2). |
| Severity | moderate |
| Source | S1, S4 |

**GB-06 Fifteen of the 29 works cited in the introduction have no entry in the reference list.**

| Field | Content |
|---|---|
| Check | P4 |
| Location | p. 2, l. 45 to 46; p. 2, l. 53 to 54; p. 2, l. 56; p. 2, l. 58 to 59; p. 2, l. 62 to 63; reference list p. 26, l. 508 to p. 29, l. 605 |
| Quotation | "(Huang et al., 2012; Intrieri et al., 2018)"; "(Zhu et al., 2010; Zhang et al., 2020a, b; Cuomo et al., 2021; Shugar et al., 2021)" |
| Concern | All in-text citations of the manuscript stand in p. 1, l. 34 to p. 2, l. 63; a search of the rest of the manuscript for "et al", four-digit years and author names finds no further citation (PP-01). These are 29 cited works (Zhang et al., 2020a, b counted as two), each held against the 31 entries (p. 26, l. 508 to p. 29, l. 605). No entry exists for Huang (2012, 2019), Intrieri, Zhu, Zhang (2020a, 2020b), Cuomo, Shugar, Navarre, Van Herwijnen, Helmstetter, Cook and Pandey, and none with the cited year for Zhang et al. (2024) and Fan et al. (2020): 15 of 29 works (51.7 %) have no source a reader can look up, among them the whole paragraph on landslide seismology (l. 61 to 63; content in GB-07) on which the gap claim (GB-08) rests. Decision on a count difference between instances: S1 counted 16 by treating "Zhao et al., 2020" (l. 57) as without entry; it is counted here as a year mismatch to the only Zhao entry (2021, Mogangling, KK-09). Case distinction: the list itself assigns Landslides volume 18 to 2021, 19 to 2022 and 21 to 2024 (l. 540 to 542, l. 514 to 516, l. 517 to 520); by that pattern the entries Fan, Yang et al. (Landslides 17, listed 2019) and Zhang, J. et al. (Landslides 21, listed 2023) belong to 2020 and 2024. If they are the works meant, 13 of 29 (44.8 %) remain without entry and the two entries carry the wrong year. The neighbouring GB-04 and GB-05 concern the content of citations in l. 42 to 51; this finding concerns their resolvability. Graded moderate: the introduction cannot be traced; the results do not depend on these citations. |
| Suggestion | Add complete entries for the 13 works without any entry to the reference list (p. 26 to 29); for Zhang et al. (2024) and Fan et al. (2020) correct the year in the entries p. 27, l. 533 to 536 and p. 29, l. 594 to 596 or add the intended works; then repeat the two-way check against the list. |
| Status | verified (citations and entries on the page images p. 1, 2, 26 to 29; search ranges as stated); inferred (assignment of Zhang et al. 2024 and Fan et al. 2020 to listed entries via the volume pattern) |
| Severity | moderate |
| Source | S4, S1 |

**GB-07 At least one of the five works cited for "landslide seismology" concerns the seismic detection of snow avalanches, not landslides.**

| Field | Content |
|---|---|
| Check | P13 |
| Location | p. 2, l. 61 to 63 |
| Quotation | "In recent years, landslide seismology has taken on more visibility (Navarre et al., 2009; Van Herwijnen and Schweizer, 2011; Helmstetter and Garambois, 2010; Cook et al., 2021; Pandey et al., 2021)." |
| Concern | van Herwijnen and Schweizer (2011), "Monitoring avalanche activity using a seismic sensor", Cold Regions Science and Technology, 69, opens with the statement that avalanche activity data are the most direct instability data for avalanche forecasting; its subject is snow avalanches. "Navarre et al., 2009" has no entry; the only matching work found is Navarre et al. (2009), "The seismic detection of avalanches: an information tool for the avalanche forecaster", International Snow Science Workshop 2009, which van Herwijnen and Schweizer (2011) cite. None of the five works has an entry (GB-06). The statement itself is not contested; its support is partly off topic. The capital "V" in "Van Herwijnen" is corrected here as well. |
| Suggestion | In p. 2, l. 62 to 63 replace the snow avalanche works by landslide seismology studies or widen the wording to "seismology of mass movements (landslides and snow avalanches)"; write "van Herwijnen and Schweizer, 2011"; add list entries for all five works. |
| Status | van Herwijnen and Schweizer (2011): verified (full text PDF, https://www.slf.ch/fileadmin/user_upload/WSL/Mitarbeitende/schweizj/vanHerwijnen_Schweizer_Avalanche_activity_seismic_monitoring_CRST_2011.pdf, DOI 10.1016/j.coldregions.2011.06.008). Identity and topic of Navarre et al. (2009): inferred (identified via the reference list of van Herwijnen and Schweizer 2011). Missing entries: verified. |
| Severity | minor |
| Source | S1 |

**GB-08 The gap claim in l. 63 to 64 is contradicted by Ge et al. (2021), which stands in the reference list without citation and already analysed energy evolution, block energies and collision frequency against travel distance in a rock avalanche.**

| Field | Content |
|---|---|
| Check | P28, P14 |
| Location | p. 2, l. 63 to 64; p. 2, l. 65 to 73; reference list p. 27, l. 540 to 542; p. 22, l. 410; p. 23, l. 423 to 424; p. 26, l. 485 to 487 |
| Quotation | "However, they still lack a quantitative and systematic study of this topic, especially on energy evolution during the collision." |
| Concern | No search is given (GB-04). Ge, Tang and Li (2021), co-authored by the first and third authors of the manuscript, state in their abstract that the mechanical energy evolution of rock avalanches was investigated by numerical simulation and field investigation, with the Jiweishan landslide as example; their figure captions, as shown on the ResearchGate figure page, include an energy analysis for 16 individual blocks and a plot of travel distance against collision frequency, and they report that rear blocks transferred energy to front blocks through collision. The manuscript has the corresponding elements: Fig9 "Energy analysis for 10 individual blocks" (p. 22, l. 410), Fig10 (b) "the plot of travel distance vs. collision frequency" (p. 23, l. 423 to 424) and Conclusion 4 (p. 26, l. 485 to 487). Ge et al. (2021) is one of the entries never cited (GB-52). The introduction thus claims a gap that the authors' own earlier study addresses with the same analyses, and it does not say what is new. The gap sentence follows the seismology paragraph whose content is GB-07 and whose citations lack entries (GB-06). A conceptual frame for the dissipation terms is also missing: Knapp and Krautblatter (2020) describe friction, collision and fragmentation as energy sinks and give about 20 to 50 % of the potential energy as consumed during disintegration; "Knapp" and "Krautblatter" give 0 hits in text.json. Graded moderate, not major: the simulation results stand; what changes is what can be claimed as new. |
| Suggestion | In p. 2, l. 61 to 64 cite Ge et al. (2021), delete or restrict the gap sentence, and state in l. 65 to 73 what this study adds (earthquake trigger with dynamic input, restored topography, VS and AG). Add as frame for the dissipated energy: Knapp, S. and Krautblatter, M. (2020) Conceptual framework of energy dissipation during disintegration in rock avalanches. Frontiers in Earth Science, 8, 263, https://doi.org/10.3389/feart.2020.00263. |
| Status | Ge et al. (2021): verified for the abstract excerpt and figure captions on the ResearchGate figure page (https://www.researchgate.net/figure/Study-area-a-the-location-of-Jiweishan-rock-avalanche-b-engineering-geology-map-and-c_fig1_354170611; publisher page not loadable); methods of the full text inferred. Knapp and Krautblatter (2020): verified (full text PDF, https://www.frontiersin.org/journals/earth-science/articles/10.3389/feart.2020.00263/pdf). Absence of in-text citations: verified (PP-01). |
| Severity | moderate |
| Source | S1 |

#### Minor corrections

| ID | Location | Quotation | Replacement | Source |
|---|---|---|---|---|
| KK-01 | p. 1, l. 13 | "Chengdu, 610041 ,China" | "Chengdu, 610041, China" | S4 |
| KK-02 | p. 1, l. 21; p. 3, l. 84 | "dissipation energy" | "dissipated energy", the term defined at p. 12, l. 242 and used at the other 8 hits of "dissipat* energy" | S2 |
| KK-03 | p. 1, l. 23; p. 3, l. 88 to 89; p. 14, l. 272; p. 14, l. 281; p. 23, l. 426; flow chart on p. 4 | "Alpha shape", "alpha shape", "alpha-shape", "Alpha Shape" | "alpha shape" (noun) and "alpha-shape" (adjective) throughout; compared on the page images: l. 23 "Alpha shape", l. 88 to 89 "alpha shape", l. 272 "alpha-shape", l. 281 "Alpha Shape", l. 426 "Alpha Shape", flow chart "Alpha Shape". Spelling only; the terms of the abscissa are GB-29, the enveloped object GB-35, the alpha set-up GB-36, the sampling GB-49 | S2 |
| KK-04 | p. 1, l. 33; p. 2, l. 39 to 41 | "high-level rock landslides"; "high-level rock landslide induced by earthquake" | one term throughout, as in the title and p. 2, l. 73: "high-altitude rock landslides"; content of these sentences in GB-01, GB-02 and GB-03 | S4 |
| KK-05 | p. 1, l. 34 | "such as donghekou" | "such as the Donghekou"; the claim of the same sentence is GB-01 | S1, S4 |
| KK-06 | p. 1, l. 36 | "Wang, 2021" | "Wang et al., 2021" (entry p. 28, l. 581 to 584 has seven authors) | S1, S4 |
| KK-07 | p. 1, l. 37 | "Tian et al., 2017" | "Tian et al., 2016", as in the entry p. 28, l. 575 to 577, or correct the entry year | S1, S4 |
| KK-08 | p. 2, l. 48 to 49 | "Cheng 2014" | "Cheng and Yu-Sheng, 2014", matching the entry p. 27, l. 521 to 523 (check the order of given name and surname of the second author, "Yu-Sheng, L."); the claim of this sentence is GB-04, the restoration check of the following sentence GB-17 | S1, S4 |
| KK-09 | p. 2, l. 57 | "Zhao et al., 2020" | "Zhao et al., 2021", as in the entry p. 29, l. 600 to 602, or correct the entry; see GB-06 for the count and GB-01 for the "Fan et al., 2019" of the same sentence | S4 |
| KK-10 | p. 2, l. 73 | "high-altitude" (the word "altitude" set in grey on the page image) | set in black like the surrounding text; the aims of this sentence are GB-03, the novelty claim before it GB-08 | S4 |

#### Verification log

| ID | Check | Checked | Values | Result |
|---|---|---|---|---|
| PP-01 | P13 | All statements that attribute content to cited works, and the match of in-text citations to the reference list | Python over text.json: all author-year citations stand in p. 1, l. 34 to p. 2, l. 63; none in p. 2, l. 64 to p. 26, l. 506. 29 cited works; 14 with an entry (two with year mismatch: Tian, Zhao), 15 without (GB-06). Reference list: 31 entries (p. 26: 3, p. 27: 12, p. 28: 12, p. 29: 4, counted on the page images); 17 never cited (GB-52). Sources read: Carpignano 2009 (abstract), Fan 2019 Rev. Geophys. (abstract), Du 2021 (abstract, https://jms.imde.ac.cn/article/doi/10.1007/s11629-020-6617-y: discrete element simulation of earthquake response, four movement stages; 2D or 3D not stated), Li 2024 (abstract, https://public-pages-files-2025.frontiersin.org/journals/earth-science/articles/10.3389/feart.2024.1466751/text: rainfall-triggered reactivation; 2D or 3D not stated), van Herwijnen and Schweizer 2011 (full text). Not read: Cheng 2014, Hu 2017 (publisher page did not load), Tian 2016, Sun 2011, Wang 2014, Wang 2021, Song 2017, Wu H. 2024 and the 15 works without entry | Findings GB-01, GB-05, GB-07. No finding for the Donghekou and Hongshiyan examples (p. 1, l. 34 to 37; sources not read). Limits: sources not read and full texts of sources read only as abstracts |
| PP-02 | P4 | Short citation against entry (year, spelling, "et al." for more than two authors) for the 14 cited works with an entry | Carpignano 2009 (5 authors); Fan 2019a and Fan 2019 (two 2019 entries without letter, GB-01); Sun 2011 (4); Wang 2014 (4); Wang 2021 (7, without et al., KK-06); Hu 2017 (5); Tian 2017 against entry 2016 (KK-07); Song 2017 ("at al.", GB-05); Wu 2024 (6); Du 2021 (5); Cheng 2014 (2, KK-08); Li 2024 (6); Zhao 2020 against entry 2021 (KK-09). Surnames identical to the entries (page images p. 1, 2, 26 to 29) | 7 deviations, as listed; the rest no finding. DOIs not resolved (optional check) |
| PP-03 | P14 | Contribution and searches for missing literature (4 of at most 6 queries) | Contribution: 3DEC reconstruction of the 1786 Mogangling landslide on contour-restored topography, with KE, PE and DE of the whole mass and ten blocks, effective collisions, and alpha-shape VS and AG. Queries on Mogangling DEM runout, rock avalanche energy evolution of blocks, pre-failure topography reconstruction (SLBL), alpha shape deposit volume and bulking. Candidates against the list: Ge et al. 2021, Zhao et al. 2021, He et al. 2023, Zhou et al. 2024, Wu et al. 2013 (in list, uncited: GB-08, GB-02); Dai et al. 2005, Jaboyedoff et al. 2019, Knapp and Krautblatter 2020 (not in list: proposals in GB-02, GB-04, GB-08); Tai et al. 2020 (same point as Jaboyedoff, not proposed); Liu et al. 2024, Landslides 21 (fragmentation energy in DEM, abstract read, not proposed); Li D. et al. 2021 (no finding). Not readable: Zhao et al. 2017 and 2018 (JGR), Yi et al. 2025 (JGR Earth Surface). A Landslides article of 2026 postdating the preprint and search hits on later versions or the discussion of this manuscript were not opened | three proposals and two citation suggestions, as listed |
| PP-04 | P28 | Gap and novelty claims and whether a search is described | Claims found by searching text.json for "first", "new", "novel", "rarely", "few", "less", "lack", "not been", "never", "no study", "seldom", "underestimated", "fully studied": p. 2, l. 42; p. 2, l. 50 to 51; p. 2, l. 60 to 61; p. 2, l. 63 to 64; p. 5, l. 113 to 114; p. 5, l. 119; p. 5, l. 120 to 121. Search description: 0 of 10 substring hits for database and search terms describe a search | Findings GB-04, GB-08, GB-11. No finding for p. 2, l. 60 to 61: the sentence that follows cites the seismological literature and the claim is not used as novelty claim |
| PP-05 | design sketch | Design sketch from the whole manuscript (text, captions, tables, declarations) | Frame: energy conservation and transfer (KE, PE, DE), no named theory; aims in p. 2, l. 39 to 41 and l. 65 to 73, no research questions, no hypotheses; type: single case study, 3DEC modelling of a historical landslide with method development; cases: one landslide, one run of 131 s, 10 monitored blocks of 25345 (0.039 %), 10 envelope times; no comparison condition (no second input, parameter variation or case). Data sources: UAV DEM (date, resolution, sensor not stated), restored topography (model-generated), Tiezhuang Temple tablet, engineering geological map (origin not stated), laboratory tests and inversion (not reported), Luding record of the Wenchuan earthquake (substitute), 3DEC output, field imagery (Fig7 (o)). Disclosed limitations: structural planes ignored (p. 9, l. 175 to 178), no 1786 record (p. 10, l. 183 to 191), smooth restored terrain (p. 7, l. 160 to 162), single tablet (p. 6, l. 136 to 138), each stated where the method is introduced; dam break not modelled (p. 16, l. 348 to 350), weathering since 1786 (p. 16, l. 353 to 355), DE decreases due to the calculation method (p. 20, l. 399 to 400), deposit area hard to restore (p. 25, l. 466 to 468), stated only in Results or Conclusions | sketch complete; gaps entered as not stated; findings GB-03, GB-13, GB-17, GB-20, GB-23, GB-26 |

### Segment 2: Material, methods, data (p. 2 to 15)

#### Substantive findings

**GB-09 The landslide marker in Fig2 (a) lies about 1° (about 94 km) west of the coordinates given in the text.**

| Field | Content |
|---|---|
| Check | P3 |
| Location | p. 5, l. 95 to 96; Fig2 (a), marker "Mogangling landslide" (p. 6) |
| Quotation | "The coordinates of the landslide center are: 29 ° 37 ′ 30.726 ″ north latitude, 102 ° 09 ′ 41.190 ″ east longitude." |
| Concern | Calibrated on the outward frame ticks of Fig2 (a) (bottom 100°E at 728.5 px, 102°E at 884.5 px, 104°E at 1039.5 px, 106°E at 1195.5 px; left 31°N at 867.5 px, 29°N at 1023.0 px, 27°N at 1181.5 px, 300 dpi), the marker centre (821.6, 980.5 px) lies at 101.15 to 101.20 ± 0.013°E and 29.55 ± 0.013°N. The text gives 102.161°E, 29.625°N. The latitude agrees within the marker radius; the longitude is 1.0° too far west, about 94 km at this latitude. The coordinates in the text are also typeset with spaces around the degree, minute and second signs. |
| Suggestion | Move the marker in Fig2 (a) to 102.16°E, 29.63°N; write the coordinates in p. 5, l. 95 to 96 as "29°37′30.726″ N, 102°09′41.190″ E". |
| Status | verified (measured on the page image) |
| Severity | minor |
| Source | AB, S4 |

**GB-10 The lithological units carry different names and codes in the text, in Fig2 (c), Fig3 (a), Fig3 (b) and Fig4, and the left-bank unit of the map contradicts the text.**

| Field | Content |
|---|---|
| Check | P38, P3 |
| Location | p. 5, l. 100 to 107; p. 11, l. 208; Fig2 (c) legend (p. 6); Fig3 (a) and (b) legends (p. 8); Fig4 legend (p. 10) |
| Quotation | "The lithology of the landslide area is mainly gray white, strongly to weakly weathered Jinning plagioclase granite (γO2). Quartz diorite (O2) and a small amount of basic magmatic rocks are distributed on the western slope of Mogangling. The sand slate of the Triassic Baiguowan formation (T3bg) is exposed on the left bank of the Dadu River. The quaternary system mainly includes landslide accumulation (Q4del), colluvial Deluvial deposit (Q4col+dl) and alluvial deposit (Q4al)" |
| Concern | Compared on the page images. Legends: Fig2 (c) Plagiogranite (γo2), Massive gravel (Q4col+dl), Sand and pebble gravel (Q4al), Hybrid granite (γM2), Rubble soil (Q4del); Fig3 (a) Granite, Diorite, Massive gravelly soils, Sand and pebble gravel; Fig3 (b) the same plus Massive gravel; Fig4 γo2, Qdel, γM2. (1) Granite: "γO2" in the text, "Plagiogranite" γo2 in Fig2 (c), "Granite" in Fig3, code only in Fig4. (2) Q4del: "landslide accumulation" in the text, "Rubble soil" in Fig2 (c), "Qdel" in Fig4, absent from Fig3 unless it is "Massive gravelly soils". (3) Q4col+dl: "colluvial Deluvial deposit" in the text, "Massive gravel" in Fig2 (c); Fig3 (b) has both "Massive gravel" and "Massive gravelly soils". (4) "Quartz diorite (O2)" in the text, "Diorite" in Fig3, absent from Fig2 (c) and Fig4; the code lacks the rock symbol of the granite code. (5) The text places T3bg sand slate on the left bank; Fig2 (c) shows "Hybrid granite" γM2 there (Huashibao), and neither T3bg nor γM2 occurs in the other source. The text also writes "gray white", "quaternary" and "colluvial Deluvial". This finding concerns the unit names; the other aspects of Fig2 are GB-09 (marker in (a)). Severity: one instance graded minor (naming), the other moderate; the higher grade applies because a reader cannot tell which units the model in Fig4 contains (see also GB-22). |
| Suggestion | Use one name and one code per unit in Sect. 2.1 (p. 5, l. 101 to 107) and in the legends of Fig2 (c), Fig3 (a), Fig3 (b) and Fig4 (for example "plagiogranite, γo2"; "landslide deposit, Q4del"; "colluvial-deluvial deposit, Q4col+dl"; "alluvial deposit, Q4al"); resolve whether the left bank is T3bg or γM2; say which unit "Massive gravelly soils" denotes; write "gray-white", "Quaternary" and "colluvial-deluvial deposit" (twice in l. 105). |
| Status | verified (names and codes on the page images); assumption (identity of "Massive gravelly soils" and of γM2 with units of the text) |
| Severity | moderate |
| Source | S2, AB, S4 |

**GB-11 The statements in l. 113 to 121 that seismic instability of high steep slopes and landslide-induced dam breaks are "relatively few" in the literature and "have not been fully studied" give neither a search nor a citation.**

| Field | Content |
|---|---|
| Check | P28 |
| Location | p. 5, l. 113 to 121 |
| Quotation | "the analysis of the instability probability of potentially unstable high and steep slopes under the action of seismic force and the evaluation and analysis of dam break or dam overturning caused by abnormal bedrock landslide such as surging waves are relatively few." |
| Concern | The paragraph motivates the case choice with a gap claim but has no citation (no author-year citation after p. 2, l. 63, PP-01) and no search description (PP-04). The reference list itself holds works that address parts of the claim: He et al. (2023) on the seismic response of the Mogangling slope (abstract read) and, by its title, Fan et al. (2019, Landslides) on the prediction of a multi-hazard chain including the Baige landslide. No counter-search was run for this sentence. |
| Suggestion | In p. 5, l. 113 to 121 cite the studies the statement rests on and state the search, or rephrase as motivation without a frequency claim. |
| Status | Absence of search and citation: verified (text.json, page image p. 5). He et al. (2023): verified (abstract). Fan et al. (2019, Landslides): inferred (title only). |
| Severity | moderate |
| Source | S1 |

**GB-12 External sources used in the Methods (remote sensing image, geological map, Tiezhuang Temple tablet, Luding strong-motion record, laboratory tests) are named neither in the data statement nor with a citation.**

| Field | Content |
|---|---|
| Check | P12 |
| Location | p. 6, l. 126 to 127 and Fig2 (b), (c); p. 6, l. 136 to 138; p. 9, l. 180 to 181; p. 10, l. 189 to 191 and Fig4 inset; p. 11, l. 206 to 207; p. 26, l. 505 to 506 |
| Quotation | "this study adopts the acceleration records measured at the Luding station during the Wenchuan earthquake as the input ground motion"; "According to the geological engineering drawing, different strata are generated"; "only the Tiezhuang Temple tablet unearthed in the 1980s has records of earthquake landslide"; "the selection of physical-mechanical parameters was based primarily on laboratory testing" |
| Concern | These sources do not originate from the authors' simulation, yet the data statement (p. 26, l. 505 to 506) treats all data as available from the first author and names none of them. The Methods give no citation for any of them: a search for in-text citations over p. 2, l. 74 to p. 15, l. 296 returns 0 hits; "station" occurs twice in the manuscript (p. 5, l. 115, power stations; p. 10, l. 190), "Tiezhuang" once (p. 6, l. 136). For the ground motion the reader learns neither provider, station code, component nor time window; for the image in Fig2 (b) and the map in Fig2 (c) neither origin nor date; the laboratory results behind Table 1 are not reported. Whether third-party records or imagery may be passed on by the first author is not stated; this is an assumption about licensing and is asked as a question. The legend of Fig2 (b) also writes "Daduhe River", while the text (12 hits) and Fig2 (c), Fig3 (a), Fig3 (b) write Dadu River. Other aspects of Fig2 are GB-09 and GB-10; the consequences of the substitute input are GB-23, the unreported laboratory data GB-26. |
| Suggestion | Cite the strong-motion record with provider, station, event, component and access route at p. 10, l. 189 to 191; name source and date of the image and the geological map in the caption of Fig2 (p. 6, l. 126 to 127); cite the publication of the tablet (p. 6, l. 137); add a sentence on the laboratory tests at p. 11, l. 207; list each source with its access route in the data statement (p. 26, l. 505 to 506); write "Dadu River" in the legend of Fig2 (b). May the Luding record and the image be redistributed by the authors, or must readers obtain them from the provider? |
| Status | verified (absence of citations and of mention in the data statement, by search in the stated range; legend on the page image p. 6); assumption (redistribution restrictions) |
| Severity | moderate |
| Source | S2, AB |

**GB-13 The procedure for restoring the deposit area and the "trajectory equations" of the contours appear only in Conclusion 1, not in the Methods.**

| Field | Content |
|---|---|
| Check | P17, P8, P15 |
| Location | p. 6, l. 138 to p. 7, l. 143; p. 7, l. 157 to 162; Fig1 (p. 4); p. 25, l. 463 to 468 |
| Quotation | "the contour lines corresponding to the sliding bed and accumulation area are modified to be straight"; "their trajectory equations can be extracted as a basis for restoring the contours"; "In such cases, restoration can be guided by referencing other mountain areas within the same stratigraphic unit." |
| Concern | The Methods say only that contour lines "are modified to be straight" (p. 6, l. 140) and are modified "along the extension direction of the mountains on the left and right sides" (p. 7, l. 157). Fig1 shows "Deposit Removal" and "Lower Slide Bed Restoration", and Conclusion 1 adds two method elements: extracted trajectory equations and, for the deposit area, reference to other mountains of the same stratigraphic unit. A search of p. 1, l. 1 to p. 25, l. 459 for "trajectory equation", "equation of", "stratigraphic unit", "other mountain" and "reference feature" gives 0 hits. Which curve form, which reference mountains and how the valley floor under the deposit was set are not described, so the sliding bed in the accumulation area cannot be rebuilt. This finding concerns the missing procedure; the missing accuracy check of the restoration is GB-17, the novelty claim GB-04, the uncited external sources of the same paragraph GB-12. |
| Suggestion | Describe in Sect. 2.1 after p. 7, l. 162 the equation form, the fitting procedure, the reference areas used for the deposit zone and the resulting valley floor elevation; keep only the finding in Conclusion 1 (p. 25, l. 463 to 468), or delete parts (a) and (b) there. |
| Status | verified (wording and search in text.json) |
| Severity | moderate |
| Source | SD, S4 |

**GB-14 The text says Fig3 (a) shows four parts of the landslide, but Fig3 (a) marks only two zones.**

| Field | Content |
|---|---|
| Check | P3 |
| Location | p. 7, l. 144 to 146; Fig3 (a), legend and zone labels I, II (p. 8) |
| Quotation | "The whole landslide occurrence area can be divided into four parts: the rock wall area, colluvial slope area, slope debris flow area, and main accumulation area." |
| Concern | Fig3 (a) shows the landslide boundary with two zones, "I Sliding bed" and "II Accumulation area" (legend, page image p. 8); none of the four names of l. 145 to 146 appears in the figure. |
| Suggestion | Mark the four parts in Fig3 (a) and add them to the legend, or change p. 7, l. 145 to 146 to the two zones shown. |
| Status | verified |
| Severity | minor |
| Source | AB |

**GB-15 The field dimensions in l. 149 to 152 contradict each other, the model length and the mapped landslide: area times thickness is not the stated volume, the length is less than half of the mapped and modelled length, and the river surface in Fig3 (b) lies about 30 m higher.**

| Field | Content |
|---|---|
| Check | P1, P2, P3 |
| Location | p. 7, l. 149 to 152; p. 7, l. 153 to 156; Fig2 (c), landslide boundary and scale bar (p. 6); Fig3 (b), water level (p. 8); p. 9, l. 173 to 174; Fig4 label "1021m" (p. 10) |
| Quotation | "about 450 m long, about 1000 m wide along the river, and a planar area of 0.45 km2. The average thickness of the landslide mass is about 100 m, and the volume is about 2400×104 m3. The elevation of the slope toe is 1120 m (about 5 m higher than the river surface)" |
| Concern | The field geometry is given in detail, which makes the check possible. (1) Volume: 450 m × 1000 m = 0.45 km² agrees with the area, but 0.45 × 10^6 m² × 100 m = 4500 × 10^4 m³, 1.875 times the stated 2400 × 10^4 m³; the stated volume implies a mean thickness of 53.3 m (Python). The exponent is printed on the base line ("2400×104", page image p. 7). (2) Length: the model length in the sliding direction is 1021 m (p. 9, l. 173 to 174; Fig4). The elevation bands and slopes of l. 151 to 156 give a horizontal profile length of 914 to 1250 m (front 210 m at 50°, colluvium 220 m at 35°, wall 290 m at 57°, platform 50 m at 5° to 12°; Python), which excludes 450 m. On Fig2 (c), calibrated on the scale bar (2.190 m/px), the mapped boundary encloses 0.993 ± 0.03 km² and spans 1162 ± 15 m along the section line a-a (azimuth 74°, consistent with the 75° of l. 149); the chord along the river is 925 m, so the width "about 1000 m" agrees. (3) Fig3 (b): the blue water level lies at 1146 ± 2 m on the striped elevation bar, whereas l. 151 to 152 imply a river surface at about 1115 m. Is the 450 m the width of another part, or were length and width swapped (the product is the same 0.45 km², but the mapped area is 0.99 km²)? The model volume is treated in GB-41; the difference to the volume of Zhao et al. (2021) in GB-02, which concerns the missing comparison with that study. Other aspects of Fig2 (marker, unit names, image source) are GB-09, GB-10 and GB-12; here only the dimensions are at issue. |
| Suggestion | State in p. 7, l. 149 to 152 to which part (source, deposit or whole landslide) length, area, thickness and volume refer, correct the values that do not fit the mapped boundary and the model, write the exponent as "2400 × 10⁴ m³", and reconcile the slope-toe and river elevations with Fig3 (b). |
| Status | verified (values on the page images p. 7, 9; map and profile measured on the page images p. 6 and p. 8); inferred (products, profile length, Python); the swap of length and width is an assumption, posed as a question |
| Severity | moderate |
| Source | S3, AB, S4 |

**GB-16 The text refers to a section b-b' in Fig2 (c), but neither Fig2 (c) nor Fig3 (b) contains it, and the ends of the section line a-a' are both labelled "a".**

| Field | Content |
|---|---|
| Check | P4, P3 |
| Location | p. 7, l. 159 to 160; Fig2 (c), section line (p. 6); Fig3 (b) (p. 8) |
| Quotation | "As shown in Fig3. (b), make a section along a-a'and b-b' in Fig2. (c)." |
| Concern | At 300 dpi, Fig2 (c) shows one section line, labelled "a" at the west end and "a" at the east end; no line labelled b or b' is drawn. Fig3 (b) shows one profile, headed "(a-a’)". The reference to b-b' therefore leads nowhere. Since the restored pre-landslide slope ("Presumed original slope" in Fig3 (b)) is the input of the whole simulation, a second section would be the reader's only check of the restoration across the slide body. The restoration procedure itself is GB-13. Other aspects of Fig2 are GB-09, GB-10, GB-12 and GB-15. |
| Suggestion | Either draw section b-b' in Fig2 (c) and add its profile to Fig3 (b), or delete "and b-b'" in p. 7, l. 160; label the east end of the line in Fig2 (c) "a′"; insert the missing space in "a-a'and". |
| Status | verified (page images p. 6, 7, 8; Fig2 (c) re-rendered at 300 dpi) |
| Severity | minor |
| Source | S4, AB |

**GB-17 The restored pre-landslide terrain, which defines the landslide mass and hence every energy value, is accepted visually and not checked.**

| Field | Content |
|---|---|
| Check | P31, P27, P10 |
| Location | p. 7, l. 160 to 162; p. 6, l. 138 to p. 7, l. 143; p. 9, l. 172; p. 2, l. 49 to 51 |
| Quotation | "although compared with the real terrain, the restored terrain is smooth and the surface does not fluctuate, the mountains become continuous, which can be regarded as the terrain before the landslide"; "the landslide mass is constructed according to the restored terrain surface" |
| Concern | The restoration is introduced as a method contribution ("a new idea of terrain restoration", p. 2, l. 50 to 51; Conclusion 1), but the only check is visual (Fig3 (c)). No error of the restored surface and no uncertainty of the resulting volume are given, although the landslide mass is constructed from the restored surface (p. 9, l. 172) and thus fixes mass, PE(t0) and all later energies. The volumes stated in the manuscript disagree by factors of 1.875 (GB-15) and 75.6 (GB-41), which a quantitative check of the restoration would have to resolve. The abstract of Zhao et al. (2021), in the reference list, gives about 4500 × 10^4 m³ for the same landslide. This finding concerns the missing accuracy check; GB-13 concerns the missing procedure of the same paragraph, GB-16 the missing second section at l. 160, GB-04 the novelty claim. |
| Suggestion | In Sect. 2.1 after p. 7, l. 162 add a quantitative check of the restoration: apply the same contour procedure blind to a landslide with a known pre-event DEM and report elevation and volume errors, or at least compare the restored source volume with the deposit volume (with a stated bulking factor) and with the published estimate. |
| Status | verified (wording, numbers in the manuscript); inferred (volume ratios, computed); Zhao et al. (2021) verified in the abstract (https://ideas.repec.org/a/spr/nathaz/v106y2021i1d10.1007_s11069-020-04471-1.html) |
| Severity | major |
| Source | SD |

**GB-18 In Fig3 (a) the legend colours of "Diorite" and "Sand and pebble gravel" are practically identical, so the layers of the block diagram cannot be assigned.**

| Field | Content |
|---|---|
| Check | P3 |
| Location | Fig3 (a), legend and block faces (p. 8) |
| Quotation | "Diorite"; "Sand and pebble gravel" |
| Concern | Measured on the legend fields: Granite #744c3c, Diorite #8c7c74, Massive gravelly soils #b49c74, Sand and pebble gravel #8c745c. Diorite and Sand and pebble gravel differ by 0 + 8 + 24 = 32 in the RGB sum, below the limit of 40 for distinguishable colours. The block faces contain #747474 (29.9 % of the sampled face area), which differs from Diorite by 32 and from Sand and pebble gravel by 48; the grey layer at the base of the block cannot be assigned. The content of the zones in Fig3 (a) is GB-14. |
| Suggestion | Give Diorite and Sand and pebble gravel clearly different colours or hatchings in Fig3 (a), as in Fig3 (b). |
| Status | verified (measured) |
| Severity | minor |
| Source | AB |

**GB-19 Several axes have no quantity or unit.**

| Field | Content |
|---|---|
| Check | P29 |
| Location | Fig3 (b), both axes (p. 8); Fig6, all three axes (p. 14); Fig7 (h) to (n), both axes (p. 18); Fig4 inset, time axis (p. 10); Fig5 (b) to (f), insets (p. 12) |
| Quotation | "0 300 600 900 1200 1500"; "1000 1200 1400 1600 1800 2000" |
| Concern | Checked on the page images. Fig3 (b): no title or unit on the horizontal (distance) or vertical (elevation) axis. Fig6: numbers only (0 to 2400, 0 to 3200, 0 to 800), while Fig4 and Fig7 (a) to (g) label the same axes "x(m)", "y(m)", "z(m)". Fig7 (h) to (n): numbers only. Fig4 inset: tick marks without numbers, title or unit, so the record duration cannot be read. Fig5 insets: numbers only. Other aspects of Fig3 are GB-14 and GB-18. |
| Suggestion | Add axis titles with units: Fig3 (b) "Distance (m)" and "Elevation (m a.s.l.)"; Fig6 "x (m)", "y (m)", "z (m)"; Fig7 (h) to (n) "x (m)" and "z (m)"; Fig4 inset "Time (s)" with tick values; Fig5 insets as in the main plot. |
| Status | verified |
| Severity | minor |
| Source | AB |

**GB-20 The model environment is not specified to a degree that allows the run to be rebuilt: software version, damping, time step, block type and contact model are missing.**

| Field | Content |
|---|---|
| Check | P35, P8 |
| Location | p. 9, l. 168 to 170; p. 9, l. 178 to 182; p. 10, l. 193 to 202; p. 10, l. 203 to p. 11, l. 213 |
| Quotation | "the three-dimensional discrete element program (3DEC), one of the most widely used numerical methods in rock mechanics, is used"; "In the numerical simulations, the blocks were assigned a Mohr-Coulomb constitutive model." |
| Concern | Settings that change the dynamic result are not given: 3DEC version; damping scheme and value (search "damp" over p. 1 to 29: 0 hits), although any damping enters DE by Eq. (4); time step; whether blocks are rigid or deformable and the zone size if deformable (a Mohr-Coulomb constitutive model implies deformable blocks); contact model and parameters for block impacts; orientation of the "uniform structural plane" (p. 9, l. 179 to 180). The availability of code and data only on request is GB-51; the missing record of static equilibrium GB-25. |
| Suggestion | Add to Sect. 2.1 after Table 1 a table of numerical settings: software and version, block type and zone size, damping type and value, time step, contact model, joint orientation, total run time. |
| Status | verified (search in text.json); the effect of damping on DE inferred from Eq. (4) |
| Severity | moderate |
| Source | SD |

**GB-21 Structural planes are excluded from the model, yet the Results attribute the failure mechanism to steeply dipping structural planes and "structural plane control"; the only steep planes in the model may be the faces of the block grid.**

| Field | Content |
|---|---|
| Check | P6, P31 |
| Location | p. 9, l. 175 to 180; p. 11, l. 208 to 210; Table 1 (p. 11); p. 15, l. 307 to 313; p. 15, l. 323 |
| Quotation | "the impact of the structural plane on the landslide process has to be ignored in this study"; "The first-arriving P-waves caused intense vertical dislocation along the steeply dipping structural planes outside the slope."; "Under the combined influence of structural plane control and strong seismic forces" |
| Concern | The Methods exclude geological structural planes (p. 9, l. 175 to 178) and then divide the mass evenly into 8.7 m × 8.7 m blocks on the xoy surface, with heights from the surface to the sliding bed and a uniform structural plane set inside (l. 178 to 180). Sect. 3.1 explains the failure by P-wave dislocation along steeply dipping structural planes, tensile cracking along these planes and pre-existing potential sliding surfaces. If the steep planes are the vertical faces of the grid blocks, the mechanism in Sect. 3.1 is a property of the discretisation, not of the slope. The aim to study the formation mechanism (p. 2, l. 39) rests on this section. The manuscript does not say which planes l. 309 refers to. The missing settings of the same model description are GB-20, the unnamed source of the geological drawing in l. 180 is GB-12; here the mechanism is at issue. Graded major: if the planes are grid artefacts, Sect. 3.1 cannot show the mechanism it states. |
| Suggestion | State in Sect. 2.1 which planes exist in the model (grid faces, the uniform structural plane, the "fully developed potential rupture planes" of p. 11, l. 209) with orientation. Then either remove the mechanism statements of p. 15, l. 307 to 313 and l. 323, or test them by rerunning with a different block size and grid orientation (for example 5 m and 15 m, grid rotated by 45°) and reporting whether the failure sequence persists. |
| Status | verified (both wordings); that the steep planes are the grid faces is inferred, posed as a question |
| Severity | major |
| Source | SD |

**GB-22 Fig4 shows four model units, Table 1 gives parameters for two, and the text names two weathering zones, without a key between them.**

| Field | Content |
|---|---|
| Check | P38 |
| Location | p. 9, l. 180 to 181; Fig4 legend (p. 10); p. 11, l. 207 to 209; Table 1, column Rock mass (p. 11) |
| Quotation | "According to the geological engineering drawing, different strata are generated and marked with different colors."; "The slope is underlain by plagioclase granite, which is subdivided into strongly weathered and moderately weathered zones." |
| Concern | The Fig4 legend lists four units: γo2, Qdel, γM2 and Sliding mass. Table 1 has two parameter sets, "bed rock" and "landslide mass". The text names a strongly and a moderately weathered zone, which occur neither in Table 1 nor in Fig4; Sect. 2.1 speaks of "strongly to weakly weathered" granite (p. 5, l. 101). Sliding mass and landslide mass plausibly denote the same body. Whether γo2, Qdel and γM2 all receive the bed rock parameters, and whether the strongly weathered zone is the landslide mass, remains open, so the material assignment of the model cannot be rebuilt. The unit names themselves are GB-10, the unnamed source of the geological drawing GB-12, the model planes GB-21 and the other settings GB-20. |
| Suggestion | Add a column "Model unit (Fig4)" to Table 1 (p. 11) and state at p. 11, l. 209 which of γo2, Qdel, γM2 and the sliding mass receive which row, and which weathering zone corresponds to which row. |
| Status | verified (legend, table rows and text); inferred (identity of Sliding mass and landslide mass) |
| Severity | moderate |
| Source | S2 |

**GB-23 The substitute seismic input is disclosed, but its consequences are not drawn: one record, no parameters, no sensitivity run, and the comparability claim has no citation.**

| Field | Content |
|---|---|
| Check | P9, P17 |
| Location | p. 10, l. 183 to 191; Fig4 inset (p. 10); p. 15, l. 306 to 318 |
| Quotation | "Extensive research indicates that the Kangding earthquake is comparable to the 2008 Wenchuan earthquake in terms of damage distribution, affected intensity, and estimated magnitude."; "It is worth noting that both the Mogangling landslide and the Wenchuan earthquake zone belong to the tectonic system of the Longmenshan Fault Zone." |
| Concern | The manuscript discloses that no 1786 record exists (p. 10, l. 183 to 186); this is not raised again. Not drawn through: (1) the comparability statement has no reference; (2) component, PGA, duration, filtering, scaling and the conversion to the viscous base boundary are not given, and the inset of Fig4 shows an acceleration trace with time markers tp, tPGA, tf, te without values; (3) the argument rests on a shared Longmenshan system, while the site is described at the junction of the Xianshuihe, Longmenshan and Anninghe faults (p. 5, l. 97 to 99), and Dai et al. (2005) attribute the regional seismicity to the Xianshuihe fault zone (GB-02); He et al. (2023) measured a crest-to-toe PGA ratio of 5.3 on this slope, which bears on how the record is applied at the model base; (4) one input, one run: the stage velocities (5.9 to 31.6 m/s), the 131 s duration and the P-wave and S-wave mechanism of p. 15, l. 307 to 313 are all conditional on this record, and the manuscript presents them as a reproduction of the 1786 event (p. 15, l. 299 to 300). The missing provenance of the record in the data statement is GB-12, the unexplained inset markers of Fig4 GB-24 and the model units of Fig4 GB-22; here the consequences of the input are at issue. Graded major: all kinematic results and the mechanism depend on one substitute input, so the reproduction claim cannot be judged without a sensitivity run. |
| Suggestion | In Sect. 2.1 after p. 10, l. 191 give the record parameters and any scaling, cite the comparability studies, and add a sensitivity series: the same model under several inputs (the Luding record scaled to two or three target PGAs bracketing estimates for an M 7.75 near-source site, and at least one other strong-motion record), reporting runout, peak velocity, duration and final DE for each. State in Sect. 3.1 that stage velocities and timing hold for the chosen input. |
| Status | verified (wording, inset, missing parameters); He et al. (2023) verified in the abstract (https://link.springer.com/article/10.1007/s10346-023-02171-y); the dependence of the results on the input is inferred |
| Severity | major |
| Source | SD, S1 |

**GB-24 Abbreviations in Fig1 and Fig4 are not resolved in legend or caption.**

| Field | Content |
|---|---|
| Check | P29 |
| Location | Fig4, legend and inset (p. 10); Fig1, panel "Global Perspective" (p. 4); p. 10, l. 192; p. 4, l. 91 |
| Quotation | "γo2", "Qdel", "γM2"; "tp", "tPGA", "tf", "te"; "P0E", "PtE", "KtE" |
| Concern | Fig4 names three units only by codes, whose names appear only in the Fig2 (c) legend, and "Qdel" lacks the "4" of "Q4del" used in the text (p. 5, l. 104) and in Fig2 (c). The inset markers tp, tPGA, tf, te are explained nowhere (full text.json searched for "PGA" and for "tp", "tf", "te" as whole words: 0 hits; "peak ground acceleration" occurs once, p. 15, l. 317, without reference to Fig4). Fig1 uses P0E, PtE, KtE, while the text uses PE(ti), KE(ti) and ME(t0). The unit names across figures are GB-10, the model units of Fig4 GB-22, the missing record parameters behind the inset GB-23. |
| Suggestion | Write the unit names next to the codes in the Fig4 legend and use "Q4del"; explain tp, tPGA, tf, te in the caption of Fig4 (p. 10, l. 192); use the notation of Eqs. (1) to (4) in Fig1. |
| Status | verified |
| Severity | minor |
| Source | AB |

**GB-25 The manuscript requires static equilibrium before dynamic loading and announces stress histories and the maximum unbalanced force as monitored, but reports none of them.**

| Field | Content |
|---|---|
| Check | P11, P18, P31 |
| Location | p. 10, l. 199 to 202; p. 13, l. 258 to 263; row 11 of Table 2 (p. 13) |
| Quotation | "Dynamic loading must be introduced only after the model has attained static equilibrium"; "the maximum unbalanced force was tracked to verify that the model reached post-failure stability"; "displacement, velocity, and stress histories were extracted for each of the ten monitored blocks in all relevant directions" |
| Concern | Search for "unbalanced" in the whole manuscript (text.json): 2 hits, p. 13, l. 258 and row 11 of Table 2; none in the Results. Search for "stress" in p. 15, l. 297 to p. 25, l. 459: 3 hits (l. 302 and l. 369 on Fig7, l. 312 "dynamic interface stress effects"); none reports a stress history of a monitored block. No convergence criterion for the static stage is given. That equilibrium and post-failure stability were reached is thus asserted, not shown. Row 11 of Table 2 ("Maximum unbalanced force") is not a block and does not fit the table title. The model settings of the same paragraph are GB-20. |
| Suggestion | Add to Sect. 2.1 the convergence criterion of the static stage and a plot or values of the maximum unbalanced force over the static and dynamic stages (supplement if needed); either add the stress histories of the ten blocks or remove them from p. 13, l. 262 and from Table 2; replace row 11 of Table 2 by a table note. |
| Status | verified (search as stated) |
| Severity | moderate |
| Source | S3, SD, S2 |

**GB-26 Field investigations and laboratory tests are named as bases of the study, but no field or laboratory data are reported.**

| Field | Content |
|---|---|
| Check | P19 |
| Location | p. 11, l. 206 to 207; p. 2, l. 65 to 66; p. 13, l. 264 to 266; p. 25, l. 472 to 473 |
| Quotation | "the selection of physical-mechanical parameters was based primarily on laboratory testing, empirical analogy, and parameter inversion"; "This study aims to comprehensively utilize field investigations, drone aerial surveying, discrete element numerical simulation, and block energy calculation methods" |
| Concern | Search over p. 1 to 29 for "field investigation", "field-investigation", "field survey" and "laboratory": the only field-related material is the UAV DEM (acquisition parameters not given), the map of Fig2 (c) (origin not stated) and the photographs in Fig7 (o). No observations, sample list, test type or number of tests appear, and Table 1 does not say which values come from tests, analogy or inversion. All 5 conclusions rest wholly or partly on model-generated data (PP-42). The missing citation of the tests is GB-12; which Table 1 row belongs to which model unit is GB-22; the numerical settings of the same section are GB-20. Here the unreported data are at issue. |
| Suggestion | Add to Sect. 2.1 (or a supplement) what was investigated in the field and when, which samples and tests produced which Table 1 values, and which values were inverted against what target; add a column "source" per parameter to Table 1. |
| Status | verified (search in text.json, pages 1 to 29) |
| Severity | moderate |
| Source | SD |

**GB-27 The two discontinuity classes of Table 1 are not matched to the "potential rupture planes and joint sets" of the text or to the "uniform structural plane" of the model.**

| Field | Content |
|---|---|
| Check | P38 |
| Location | p. 11, l. 209 to 210; Table 1, column Discontinuities (p. 11); p. 9, l. 177 to 180 |
| Quotation | "The discontinuities are represented by both fully developed potential rupture planes and joint sets"; "A uniform structural plane is set inside." |
| Concern | Table 1 names two classes, "discontinuities" and "potential discontinuities". The text names fully developed potential rupture planes and joint sets; p. 9 names "structural plane" twice and "uniform structural plane" once; the Results speak of "pre-existing potential sliding surfaces" (p. 15, l. 313). Which Table 1 row belongs to the rupture planes and which to the joint sets is not stated; "potential" occurs in the text name and in the second row, but the text calls these planes "fully developed", which fits the first row equally well. A reader cannot assign the parameters (for example cohesion 0.8 or 1.1 MPa) to the planes in the model. The question whether these planes or the grid faces control the mechanism is GB-21; the rock units of Table 1 are GB-22; the numerical settings, including the orientation of the uniform plane, are GB-20. |
| Suggestion | Rename the two rows in Table 1 (p. 11) with the terms of the text ("joint sets", "potential rupture planes") or add a sentence at p. 11, l. 210 that maps them; state at p. 9, l. 180 which class the uniform structural plane is. |
| Status | verified (names); inferred (that the assignment is ambiguous) |
| Severity | moderate |
| Source | S2 |

**GB-28 Two of the six red markers in Fig5 (a) are not local velocity maxima, although the text defines the markers as peaks.**

| Field | Content |
|---|---|
| Check | P3 |
| Location | p. 11, l. 221 to 224; Fig5 (a) (p. 12) |
| Quotation | "A local velocity peak (denoted by red or purple markers) corresponds to an acceleration phase, but only those pronounced peaks (highlighted in red) yield a substantial velocity increase" |
| Concern | Calibration on the tick marks of Fig5 (a) (300 dpi): y axis minus 2 at 1175.5 px and 14 at 710.0 px (29.09 px per m/s); x axis 0 m at 614.5 px and 600 m at 1139.5 px. Counted: 6 red and 5 purple markers in the plot. Red markers at (travel distance, velocity): (47.3 m, 10.2 m/s), (190.3, 12.3), (243.4, 13.05), (307.9, 13.5), (448.2, 7.5), (463.4, 4.2). The marker at 243.4 m is followed by a grey point at 261.4 m and 13.38 m/s, 0.33 m/s higher (uncertainty ± 0.034 m/s). The marker at 463.4 m is followed by grey points rising to about 5.2 m/s. Both red markers lie on rising flanks, not on peaks. Since the 1,139 effective collisions (p. 11, l. 233) rest on this peak definition, how were these two markers selected? The legend of Fig5 (a) also reads "Non-obvios acceleration". |
| Suggestion | Correct the marker positions in Fig5 (a) or explain in Sect. 2.2 why points on a rising flank count as effective collisions; correct the legend to "Non-obvious acceleration". |
| Status | verified (measured) |
| Severity | moderate |
| Source | AB |

**GB-29 The abscissa of the curve used to detect effective collisions is called travel distance, travel displacement, displacement and migration distance.**

| Field | Content |
|---|---|
| Check | P38 |
| Location | p. 11, l. 221; p. 11, l. 225; p. 11, l. 227; p. 11, l. 234; Fig5 (a) to (f), axis titles (p. 12); p. 1, l. 22 to 23; p. 1, l. 30; p. 22, l. 418; Fig10 (b), axis (p. 23); p. 25, l. 474 to 475 |
| Quotation | "presents a typical velocity-travel-distance curve for an individual block"; "value of the displacement velocity curve"; "extracting local peaks from displacement-velocity curves" |
| Concern | Variants over the whole manuscript (text.json, 9 hits) and the axis titles on the page images: "velocity-travel-distance curve" (l. 221), "velocity-distance profile" (l. 225), "velocity-distance curve" (l. 227), "travel-distance versus velocity profile" (l. 234), "displacement velocity curve" (l. 23), "displacement-velocity curves" (l. 474), "migration distance" (l. 30, l. 418), axis "Travel distance (m)" (Fig5 (a), Fig10 (b)) and axis "Travel Displacement (m)" (Fig5 (b) to (f)). Travel distance (path length) and displacement (straight-line distance from the start) differ for a block that bounces, and the prominence criterion includes peak width, which depends on the abscissa. The markers of Fig5 (a) are GB-28, the threshold GB-30. |
| Suggestion | State in Sect. 2.2 (p. 11, l. 221) whether the abscissa is cumulative path length or displacement, and use one term in the abstract (p. 1, l. 22 to 23 and l. 30), p. 11, l. 225 to 234, p. 22, l. 418, p. 25, l. 474 to 475 and the axis titles of Fig5 (b) to (f), for example "velocity-travel-distance curve" and "Travel distance (m)". |
| Status | verified (names); inferred (effect on peak width) |
| Severity | minor |
| Source | S2, SD, AB |

**GB-30 Effective collision detection cannot be reproduced: the prominence threshold has no reference quantity, the 30 % choice rests on a visual judgement with a count for only one threshold, velocity peaks are not checked against contacts, and the curves in Fig5 are not identified.**

| Field | Content |
|---|---|
| Check | P8, P11, P31, P34 |
| Location | p. 11, l. 226 to 234; Fig5 (b) to (f) (p. 12); p. 12, l. 238 to 239; p. 25, l. 473 to 475 |
| Quotation | "a suitable prominence threshold must be chosen-one that quantifies each peak’s standout height, width, and position relative to adjacent peaks"; "At a threshold of 30%, however, the identification of effective collisions is deemed acceptable."; "Under this setting, 1,139 effective collisions were detected from the travel-distance versus velocity profile." |
| Concern | Showing the detections for five thresholds in Fig5 is a useful sensitivity display (PP-21). (1) A percentage threshold is given without the quantity it refers to, and one threshold is said to quantify height, width and position at once; the software or function is not named; the caption ("threshold=10%") does not say percent of what either. (2) The choice of 30 % rests on judgement between visually over- and under-detecting thresholds; counts are given only for 30 % (1,139), while for 10 %, 20 %, 40 % and 50 % the text says only "overestimation" and "undercount", and the panels carry no counts. (3) What is measured is a local velocity maximum; that it is a collision that accelerates the block is not checked, although contact data and stress histories exist in the model (Table 2). Other causes of a local maximum (terrain, free flight, ground shaking) are not separated. (4) The block behind Fig5 is not named: Fig5 (a) runs to about 600 m and 13.5 m/s, Fig5 (b) to (f) to 2500 m with a peak of 45.2 to 45.5 m/s (measured by two instances), more than the largest velocity in the snapshots of Fig7 (31.6 m/s at 12 s, p. 16, l. 330); whether this is a peak between snapshots or another run is not said. Conclusion 2 states that effective collisions "can be identified" (p. 25, l. 473 to 475) without naming the threshold or its visual basis. The population behind the 1,139 is GB-46; the abscissa GB-29; the markers of Fig5 (a) GB-28. |
| Suggestion | In Sect. 2.2 define the prominence (absolute in m/s or relative to the local velocity range), name the implementation, give an objective criterion for 30 %, report the number of detections for each of the five thresholds (p. 11, l. 233 or caption of Fig5), and validate detected peaks against logged contact events for a sample of blocks; name the block and run shown in Fig5 (a) and (b) to (f); restate Conclusion 2 (p. 25, l. 473 to 475) with the threshold and its basis. |
| Status | verified (wording; Fig5 values measured); assumption (other causes of velocity peaks), posed as a question |
| Severity | moderate |
| Source | SD, S3, S4 |

**GB-31 Renderings, boxes and insets in Fig5 and Fig11 are not explained.**

| Field | Content |
|---|---|
| Check | P29 |
| Location | Fig5 (b) to (f), shaded box and inset (p. 12); Fig11 (a) to (j), light green mesh and dark green inset (pp. 23 to 24); p. 24, l. 437 to 439 |
| Quotation | "Fig11. Comparison of the overall envelope fitting of the landslide at 10 different times and the shape of the landslide mass in numerical simulation" |
| Concern | Fig11 shows two renderings per panel (light green mesh, dark green inset); the caption does not say which is the alpha-shape envelope and which the simulated mass. Fig5 (b) to (f): the caption does not say that the inset enlarges the shaded box. The missing reference quantity of the threshold is part of GB-30; the unnumbered markers of Fig6 are part of GB-34; the font size of the insets GB-32; the markers of Fig5 (a) are GB-28 and the axis titles of Fig5 GB-29; here only box, inset and renderings are at issue. |
| Suggestion | Name both renderings in the caption of Fig11 (p. 24, l. 437 to 439); explain inset and box in the caption of Fig5 (p. 12, l. 238 to 239). |
| Status | verified |
| Severity | minor |
| Source | AB |

**GB-32 Axis numbers and titles in Fig5, Fig7, Fig9, Fig10, Fig11 and Fig12 are smaller than 6 pt in print.**

| Field | Content |
|---|---|
| Check | P29 |
| Location | Fig5 (b) to (f) insets and main plots (p. 12); Fig7 (a) to (g) (p. 17); Fig9 (a) to (j) (pp. 21 to 22); Fig10 (a), (b) (p. 23); Fig11 (a) to (j) (pp. 23 to 24); Fig12 (a), (b) (p. 25) |
| Quotation | "300 200 100 0 -100 -200 -300"; "Z(m)" |
| Concern | Measured as digit or capital height of the smallest labels in the 300 dpi page images (pt = height in px × 72 / 300 / 0.72; tolerance ± 0.6 pt): Fig11 axis numbers 3.0 pt and axis titles 2.3 pt; Fig5 inset numbers 3.7 pt; Fig9 x axis numbers and title 4.0 pt; Fig12, Fig7 (a) to (g) and Fig10 (a) axis numbers 5.0 pt; Fig10 (b) and Fig5 main y axis numbers 5.3 pt. All are below 6 pt by more than the tolerance; Fig11 and the Fig5 insets are below 4 pt. The explanation of the Fig5 insets and Fig11 renderings is GB-31; the markers, axis terms and threshold of Fig5 are GB-28, GB-29 and GB-30; here only the type size is at issue. |
| Suggestion | Enlarge axis numbers, titles and legends in these figures to at least 7 pt at print size, if necessary with fewer panels per row (Fig11) or by replacing the insets of Fig5 with separate enlarged panels. |
| Status | verified (measured) |
| Severity | minor |
| Source | AB |

**GB-33 The coordinates of Table 2 use a frame that does not match the axes of Fig4, Fig6 and Fig7, and Fig10 (a) and Fig11 use yet other frames, without stated origins.**

| Field | Content |
|---|---|
| Check | P38 |
| Location | Table 2, column Coordinate (p. 13); Fig4 axes (p. 10); Fig6 axes (p. 14); Fig7 axes (pp. 17 to 18); Fig10 (a), axis Z(m) (p. 23); Fig11 axes (pp. 23 to 24) |
| Quotation | "(-79,-284,340)"; "(-719,120,755)" |
| Concern | All these show the same model. Table 2 has x from minus 719 to minus 68, y from minus 557 to 286, z from 340 to 755. Fig4, Fig6 and Fig7 show x(m) and y(m) axes with positive values only (0 to about 2400 and 0 to 3200) and z(m) 0 to 800. Fig10 (a) shows Z(m) from 0 down to minus 840, so it is relative to the start. Fig11 shows X(m), Y(m) and Z(m) with negative and positive values. No origin is given for any of them (p. 9, l. 178 names only the "xoy surface"). With negative x the Table 2 points cannot be placed in Fig6, which also has no IDs (GB-34). Row 11 of Table 2 is part of GB-25. |
| Suggestion | Give origin and orientation of the model coordinate system at p. 9, l. 178, express Table 2 (p. 13) in the frame of the Fig4 and Fig6 axes or state the offset, and say in the captions of Fig10 (p. 23, l. 423 to 424) and Fig11 (p. 24, l. 437 to 439) that their axes are relative and to which origin. |
| Status | verified (axis ranges on the page images, Table 2 values); inferred (that no offset is stated, from reading Sect. 2.1 to 2.4) |
| Severity | moderate |
| Source | S2 |

**GB-34 In Fig6 the zone labels "Lower middle part" and "Upper middle part" are swapped relative to Table 2, and the ten markers carry neither IDs nor a colour key.**

| Field | Content |
|---|---|
| Check | P38, P3, P29 |
| Location | Fig6, zone labels and markers (p. 14); Table 2, column Position (p. 13); p. 13, l. 256 to 257 |
| Quotation | "Top"; "Lower middle part"; "Upper middle part"; "Bottom" |
| Concern | The monitoring groups are introduced with coordinates in Table 2, which makes them traceable. In Table 2 the upper middle part (IDs 6 to 8) has z = 660 to 692 and the lower middle part (IDs 3 to 5) z = 465 to 498. In Fig6 three dashed lines divide the mass into four bands; from upslope to downslope the labels read "Top", "Lower middle part", "Upper middle part", "Bottom" (page image p. 14, enlarged). The markers per band are 2, 3, 3 and 2 from the top (recounted by ZF on an enlarged crop: red and magenta; yellow, light blue and green; orange, purple and lavender; dark blue and pink), matching the group sizes of Table 2; the count 3, 2, 3, 2 noted by one instance as a hint is not confirmed. So the band next to "Top" is called "Lower middle part". The ten markers have ten colours without numbers or key, so they cannot be linked to the IDs 1 to 10 of Table 2, Fig9 and Fig10 (a), which the Results discuss by number (p. 20, l. 397; p. 22, l. 416). Severity: one instance graded minor (label), the other moderate; the higher applies because a reader cannot assign the monitored blocks to their positions, on which the block results depend. The frame of the Table 2 coordinates is GB-33; the naming of positions in abstract and conclusions is part of GB-45. |
| Suggestion | In Fig6 (p. 14) swap the labels "Lower middle part" and "Upper middle part" and add the IDs 1 to 10 next to the markers, or a colour key matching the legend of Fig10 (a). |
| Status | verified (label order and marker counts on the page image; z values in Table 2); inferred (that the top of the image is the top of the slope, from the 3D view and Fig4) |
| Severity | moderate |
| Source | S2, AB |

**GB-35 The object enclosed by the alpha-shape envelope carries several names, and V0 and S0 are defined on another object than Vt and St.**

| Field | Content |
|---|---|
| Check | P38, P20 |
| Location | p. 14, l. 269 to 272; p. 14, l. 278 to 280; Fig1, fourth block (p. 4); p. 1, l. 24; p. 3, l. 88 to 89; p. 23, l. 427 to 429; p. 24, l. 449 to 452; p. 26, l. 491 |
| Quotation | "An alpha-shape algorithm is applied to the slide mass"; "In these expressions, V0 denotes the initial volume of the landslide mass (m³); Vt denotes the volume of the enclosing envelope at time t (m³)" |
| Concern | Sect. 2.4 states the purpose of VS and AG clearly, and the normalisation is a good idea for comparing shapes. The enveloped object, however, is named "landslide body" from "3D point cloud data" (p. 1, l. 24), "landslide mass" (p. 3, l. 88 to 89), "landslide accumulation area" (heading p. 14, l. 269; Fig1), "deposition zone" (l. 270, l. 272), "slide mass" (l. 272), "deposit mass" (p. 23, l. 427; p. 24, l. 449; p. 26, l. 491), "deposit region" (p. 23, l. 429) and "monitored block group" (p. 24, l. 452); at t = 0 s no deposit exists. In Eqs. (5) and (6) V0 and S0 refer to the landslide mass, Vt and St to the envelope. If V0 is the block volume (317563 m3, p. 9, l. 182) and not the envelope at t = 0 s, VS(0) is not zero and VS mixes the envelope effect with the expansion. In Fig12 (a) the curves start at VS = 0 % (page image p. 25), which suggests that V0 is the envelope at t = 0 s; the text says otherwise. The thresholds 29.47 % and 319.5 % (p. 25, l. 453 to 454) depend on this choice. The restoration blocks of Fig1 are GB-13; here only the envelope block is at issue. |
| Suggestion | In Sect. 2.4 (p. 14, l. 270 to 280) name the enveloped object once ("the simulated block assembly of the landslide mass") and use that name in the heading l. 269, Fig1, p. 23, l. 427 to 429, p. 24, l. 452 and the abstract; define V0 and S0 as envelope volume and area at t = 0 s, if that is what was used. Which definition underlies Fig12? |
| Status | verified (names at the cited lines and in Fig1; start of the curves at VS = 0 % on the page image); inferred (consequence for VS at t = 0); assumption (which V0 was used), posed as a question |
| Severity | moderate |
| Source | S2, S3 |

**GB-36 The alpha-shape envelope is not specified (point set, implementation, unit of alpha), and the claim that a fixed alpha ensures a tight fit at all times is untested.**

| Field | Content |
|---|---|
| Check | P8, P35, P26, P31 |
| Location | p. 14, l. 281 to 284; p. 14, l. 272 to 273; p. 1, l. 23 to 25 |
| Quotation | "this study uniformly sets the α value to 1. This approach ensures a tight fit of the envelope model while minimizing geometric deviations introduced by parameter tuning." |
| Concern | Not stated: which points form the "3D point cloud" (block vertices, centroids, zone gridpoints), the implementation, and the unit or convention of alpha (radius in metres or its inverse); the block footprint is 8.7 m (p. 9, l. 178), so the value 1 cannot be judged. Fixing alpha avoids tuning but does not show a tight fit; the fit is not measured (for example the fraction of block volume inside the envelope). The guarantee is claimed for every time, while the mass disperses to VS of about 1250 % and AG of about 4300 % (Fig12); whether one alpha fits a compact mass and a dispersed deposit equally is not shown (assumption, posed as a question). The definition of V0 and S0 is GB-35. |
| Suggestion | In Sect. 2.4 name the point set, the implementation and the alpha convention, and add a sensitivity check: VS and AG at the ten times for at least three alpha values, with the fraction of block volume enclosed. |
| Status | verified (missing specifications); assumption (effect of a fixed alpha under dispersion) |
| Severity | moderate |
| Source | SD |

**GB-37 VS and AG are called "volume swelling" and "area growth" in their definition and "volume expansion rate" and "surface area growth rate" elsewhere, and the surface area has the symbol S in Eq. (6) and A in Sect. 3.4.**

| Field | Content |
|---|---|
| Check | P38 |
| Location | p. 14, l. 274 to 277; p. 1, l. 25; p. 3, l. 89; p. 14, l. 287 to p. 15, l. 288; p. 24, l. 440 to 441; p. 25, l. 453 to 454; p. 25, l. 458 to 459; Fig12 axes (p. 25); p. 26, l. 488 |
| Quotation | "two dimensionless indices are introduced: volume swelling (VS) and area growth (AG)"; "we first extracted its volume (V) and surface area (A) at each time point, based on which the volume expansion rate (VS) and surface area growth rate (AG) were calculated" |
| Concern | Search over the whole manuscript (text.json: "volume swelling" or "volume expansion" 6 hits; "area growth" 7 hits) gives for VS "volume expansion rate" (l. 25, l. 89, l. 441, l. 453), "volume swelling" (l. 275, l. 287 to 288; Fig1; Fig12 (a) axis "Volume Swelling (%)") and "volume expansion" (l. 488); for AG "area growth rate" (l. 25), "surface area growth rate" (l. 89, l. 441), "area growth" (l. 275, l. 288; Fig1; Fig12 (b) axis "Area Growth (%)") and "surface area growth" (l. 453, l. 488). VS is a relative change, not a rate in time, so "rate" adds a second meaning. Eq. (6) uses S for the surface area, p. 24, l. 440 uses A and V instead of St and Vt. The Fig12 caption says "as a function of volume" and "as a function of area", while the axes show VS and AG. The object behind V0 is GB-35; the sampling of Fig12 GB-49. |
| Suggestion | Use "volume swelling (VS)" and "area growth (AG)" throughout (p. 1, l. 25; p. 3, l. 89; p. 24, l. 441; p. 25, l. 453 to 454; p. 26, l. 488); write "volume (Vt) and surface area (St)" at p. 24, l. 440; change the caption of Fig12 (p. 25, l. 458 to 459) to "(a) as a function of volume swelling (VS); (b) as a function of area growth (AG)". |
| Status | verified |
| Severity | minor |
| Source | S2, S3, SD, AB |

#### Minor corrections

| ID | Location | Quotation | Replacement | Source |
|---|---|---|---|---|
| KK-11 | p. 2, l. 76 to p. 3, l. 77 | "As shown in Fig1., the research method involves three parts:" | "As shown in Fig. 1, the research method involves four parts:" (the text lists (1) to (4) in p. 3, l. 77 to 90, and Fig1 shows four blocks) | S3, S4, AB |
| KK-12 | figure references in the running text from p. 2 to p. 25 (27 references) and the 12 figure captions | "Fig1." (26 references and all 12 captions with a full stop directly after the number); "Fig7" (1 reference without full stop) | "Fig. 1", "Fig. 7" in all 27 references and "Fig. 1" to "Fig. 12" in the captions | S4 |
| KK-13 | flow chart, box "Extraction of volume and area of landslide accumulation area" (p. 4) | "Extraction of volume" (the last letter runs into the right border of the box) | widen the box or break the line; the name of the enveloped object in this box is GB-35, the restoration blocks of the flow chart GB-13, its abbreviations GB-24 | AB |
| KK-14 | p. 5, l. 97 | "Kangding County to the West" | "Kangding County to the west" | S4 |
| KK-15 | p. 5, l. 98 | "intersection of "Y" - shaped faults" | "intersection of "Y"-shaped faults" | S4 |
| KK-16 | p. 5, l. 99 to 100 | "nearly 20 large and super large earthquake landslides" | "nearly 20 large and very large earthquake-induced landslides"; the unit names of the following sentence are GB-10 | S4 |
| KK-17 | p. 5, l. 110 to 111 | "burst the Dadu River after 9 days. The sudden flood made the downstream area a vast ocean" | "dammed the Dadu River; the dam burst after 9 days, and the sudden flood inundated the downstream area"; the death toll of the same sentence is GB-02, the dam breach in the validation GB-38 | S4 |
| KK-18 | p. 6, l. 132 to 133 | "Convert the geographical coordinate system to the projection coordinate system to facilitate the export of the filtered point cloud." | "The geographic coordinates were converted to a projected coordinate system to facilitate the export of the filtered point cloud." | S4 |
| KK-19 | p. 7, l. 152 to 156 | "1120 m-1330m"; "; The elevation" (three times) | "1120 m to 1330 m"; "; the elevation"; the values of these lines are GB-15, their use for validation GB-38 | S4 |
| KK-20 | p. 9, l. 182 | "1121m high" | "1121 m high"; the volume of the same sentence is GB-41, the model settings GB-20 | S4 |
| KK-21 | p. 10, l. 193 to 195 | "In the course of a discrete-element simulation-particularly when modeling nominally semi-infinite bodies such as the use of fixed or elastic boundaries in a static analysis will inevitably reflect outbound seismic waves into the model during a subsequent dynamic analysis." | "In a discrete-element simulation, particularly when nominally semi-infinite bodies are modelled, fixed or elastic boundaries used in a static analysis will inevitably reflect outgoing seismic waves back into the model during a subsequent dynamic analysis."; the missing settings of this paragraph are GB-20 | S4 |
| KK-22 | p. 11, l. 218; p. 11, l. 228 | "block velocities-hereafter termed"; "must be chosen-one that quantifies" | "block velocities, hereafter termed"; "must be chosen, one that quantifies" (hyphen used as a dash on the page image); the content of l. 228 is GB-30 | S4 |
| KK-23 | Table 1, row "bed rock", column Rock mass; row "landslide mass", column Shear (p. 11) | "bed rock"; "6.9" | "bedrock"; "6.90" (two decimals as in the other cells of the column); the assignment of the rows to model units is GB-22, the discontinuity rows GB-27, the structural planes GB-21, the caption KK-24 | S4 |
| KK-24 | Table 1 caption (p. 11); Table 2 caption (p. 13) | "Table 1 Physical parameters"; "Table 2: The basic information" | one form for both, for example "Table 1: Physical parameters"; see KK-23 for the cells of Table 1 and GB-21, GB-22, GB-27 for its content | S4 |
| KK-25 | p. 13, l. 246; p. 13, l. 251 | "where, at time ti, PE(ti), and DE(ti) can be expressed as:"; "(m/s);h(ti)" | "where, at time ti, KE(ti), PE(ti) and DE(ti) can be expressed as:" (Eq. (2) defines KE); "(m/s); h(ti)"; the mass and datum of the same paragraph are GB-44 | S4, SD |

#### Verification log

| ID | Check | Checked | Values | Result |
|---|---|---|---|---|
| PP-06 | P4, P29 | Every reference to a figure, table, panel and equation with its target; numbering and first mention order | First mentions p. 2, l. 76 (Fig1), p. 5, l. 93 (Fig2), p. 7, l. 144 (Fig3), p. 9, l. 173 (Fig4), p. 11, l. 220 (Fig5), p. 13, l. 256 (Fig6), p. 15, l. 301 (Fig7), p. 19, l. 375 (Fig8), p. 20, l. 393 (Fig9), p. 22, l. 414 (Fig10), p. 23, l. 428 (Fig11), p. 24, l. 443 (Fig12), ascending; each figure mentioned in its own section; panels against captions: Fig2 3/3, Fig3 3/3, Fig5 6/6, Fig7 15/15, Fig9 10/10, Fig10 2/2, Fig12 2/2, Fig11 10 panels against "(a-i)"; Table 1, 2; Eqs. (1) to (6) without gap; headings with a gap at 3.3. No appendix | no finding apart from KK-11, GB-16, KK-27, KK-28 |
| PP-07 | P11 | The four announced parts (p. 3, l. 77 to 90) against the Results | (1) restoration: Fig3; (2) evolution: Sect. 3.1, Fig7 (a) to (o); (3) energy of the whole mass: Fig8; of ten blocks: Fig9 (a) to (j); trajectories: Fig10 (a), ten trails; (4) envelopes: Fig11, ten times; VS and AG against energy: Fig12 | no finding for the cells listed; gaps in GB-25, GB-30, GB-38, GB-45 |
| PP-08 | P29, P3 | Inventory of all figures (no graphical abstract, no appendix figures) | Fig1 p. 4 flow chart; Fig2 p. 6 maps (a) location, (b) satellite image, (c) geological map; Fig3 p. 8 to 9 (a) block diagram, (b) profile, (c) contour maps; Fig4 p. 10 model with inset time series; Fig5 p. 12 six line charts; Fig6 p. 14 model; Fig7 p. 17 to 19 15 panels; Fig8 p. 20 stacked bars; Fig9 p. 21 to 22 ten stacked bar charts; Fig10 p. 23 (a) 3D trajectories, (b) scatter with curve; Fig11 p. 23 to 24 ten meshes; Fig12 p. 25 two line charts; all embedded as raster images (272 to 743 ppi) | 12 figures, all raster |
| PP-09 | P38, P2 | Name and magnitude of the triggering earthquake | "Kangding earthquake (Ms7 ¾) in 1786" (p. 5, l. 110), "1786 Kangding earthquake" (p. 10, l. 183), "Kangding earthquake" (p. 10, l. 188); "1786 Moxi M 7.75 earthquake" only in the title of Zhao et al. (2021) (p. 29, l. 600 to 601); Ms 7¾ = 7.75 | no finding; the second name stems from a cited study |
| PP-10 | P38 | Place and structure names in text and figures | "Caihong bridge" (p. 5, l. 93; Fig2 (c)), "Huashibao" (p. 16, l. 342; Fig2 (c)), "Mogangling Mountain" (Fig2 (c)), "Dadu River fault (Detuo fault)" (p. 7, l. 147) and "Reverse fault" (Fig3 (b)), "Dadu River" (12 hits in the text) | no finding beyond GB-12 (Daduhe) |
| PP-11 | P3 | Scale bars and map orientation | Fig2 (c): 0, 200, 400, 600 m at 1559.5, 1650.5, 1743.0, 1833.5 px; Fig2 (a) segments 0, 40, 160 km equal; Fig2 (b) 0, 200, 600 m; Fig3 (a) 0, 400, 1000 m; Fig3 (c) segments 266, 270, 402 px for 400, 400, 600 m; section a-a azimuth 73.9° against 75° (p. 7, l. 149) | no finding; length and area in GB-15 |
| PP-12 | P12 | Inventory of data sources in the Methods (p. 2, l. 74 to p. 15, l. 296) against the code and data statements (p. 26, l. 494 to 506) | Author-held: UAV DEM and point cloud (p. 6, l. 130 to 135), restored contours and surface (p. 6, l. 138 to p. 7, l. 143), 3DEC model (p. 9, l. 168 to 182), block histories (p. 13, l. 260 to 264), peak detection (p. 11, l. 226 to 234), energy series (Eqs. 1 to 4), envelopes and VS and AG (p. 14, l. 270 to 284), field findings (p. 13, l. 265 to 266). External: Luding record, image Fig2 (b), map Fig2 (c), Tiezhuang tablet, laboratory tests. In the manuscript: Table 1, Table 2. Links in the statements: 0. No source concerns persons | findings GB-12, GB-51; the disclosed absence of a 1786 record (p. 10, l. 183 to 186) is a reason for the substitute record, not for withholding it |
| PP-13 | P1, P36 | Field area from length and width; approximations against own records | 450 m × 1000 m = 0.45 km²; "about" 9 hits (geometry, p. 7, l. 149 to 156; p. 9, l. 174), "approximately" 2 (p. 16, l. 328; p. 25, l. 453), "nearly" 1 (p. 5, l. 99), "several" 2 (p. 2, l. 52; p. 16, l. 355) | no finding beyond GB-15 |
| PP-14 | P38 | Section labels a-a' and b-b' | Fig2 (c) and Fig3 (b) show only a-a'; p. 7, l. 159 to 160 names a-a' and b-b' | no naming finding (b-b' is an absent object, GB-16) |
| PP-15 | P3 | Vertical scale of Fig3 (b) | striped bar, 20 stripes of 27.1 px (50 m each) between 1000 m at 2391.5 px and 2000 m at 1849.0 px; horizontal labels about 0.54 px/m | drawn without vertical exaggeration as far as can be judged; water level in GB-15 |
| PP-16 | P37 | Figures or tables with corrected values | no post-hoc correction mentioned; the restored terrain is labelled as such in Fig3 (c) ("Terrain after repair") and Fig1 | no finding |
| PP-17 | P2, P3 | Model dimensions in text and Fig4; vertical extent against field elevations | "1021m", "747m", "179m", "131m" in Fig4 against p. 9, l. 173 to 175 (1021 m, 747 m, 179 m, 131 m); 131 m + 747 m = 878 m above the river against back wall ridge 2000 m minus slope toe 1120 m = 880 m | no finding |
| PP-18 | P22 | Column heights implied by the 8.7 m × 8.7 m grid (p. 9, l. 178 to 179) and Table 2 | 75.69 m² base; Table 2 volumes give 10.0 to 23.2 m per block; whether a column is one block or several is not stated; 0.45 km² / 75.69 m² = 5945 columns | no finding of its own; used in GB-41 |
| PP-19 | P38 | Software and threshold names | "three-dimensional discrete element program (3DEC)" (p. 9, l. 169), "3DEC" (p. 10, l. 196); thresholds 10 %, 20 %, 30 %, 40 %, 50 % in p. 11, l. 230 to 233 and p. 12, l. 238 to 239 | no finding |
| PP-20 | P26 | Guarantee of non-reflecting boundaries (p. 10, l. 196 to 197) across paths | one dynamic path; base viscous, sides free-field (p. 10, l. 197 to 199); static stage with velocity restraints (p. 10, l. 201 to 202) | no finding for the boundary statement; guarantees of p. 14, l. 283 and p. 25, l. 471 in GB-36 and GB-38 |
| PP-21 | P2, P3 | Thresholds in text and caption; markers per threshold in Fig5 | 10, 20, 30, 40, 50 % in p. 11, l. 230 to 232 and p. 12, l. 238 to 239; red blobs in the insets (touching markers counted once): (b) 35, (c) 30, (d) 30, (e) 27, (f) 3 | consistent; definition and counts in GB-30 |
| PP-22 | P38 | Energy terms and abbreviations | KE, PE, DE, ME defined p. 12, l. 241 to 243; used in Fig1, Fig8, Fig9 legends, Fig12 legends, p. 14, l. 287, p. 24, l. 442 | no finding beyond KK-02 and GB-24 |
| PP-23 | P16 | Observations in text.json that the page images do not confirm | equation operators missing in text.json at p. 12, l. 245, p. 13, l. 247 to 249 and p. 14, l. 276 to 277 (present on the page images); copyright symbol in the page header; affiliation numbers on separate lines (p. 1, l. 5 to 13); Table 1 and Table 2 headers split; spaced reference lines reflect justified type | extraction artefacts, no finding |
| PP-24 | P7 | Described method against data for the energy and envelope steps | Eq. (4) applied to whole mass and blocks; PE datum in GB-44; time points in GB-49 | no further finding |
| PP-25 | P2, P5, P22, P3 | Number and grouping of the monitoring points in text, Table 2, Fig6, Fig9 and Fig10 | 10 points in p. 13, l. 256 and l. 262, Table 2 caption, Fig6 caption, p. 20, l. 392, Fig9 caption p. 22, l. 410 to 413, Fig10 caption p. 23, l. 423; Table 2 has eleven IDs, ID 11 being the maximum unbalanced force (p. 13, l. 258); groups bottom IDs 1, 2 (z 340, 355), lower middle 3 to 5 (z 465 to 498), upper middle 6 to 8 (z 660 to 692), top 9, 10 (z 752, 755); 2 + 3 + 3 + 2 = 10; z ranges do not overlap; Fig6 bands 2, 3, 3, 2 | no finding on the counts; labels in GB-34, row 11 in GB-25 |
| PP-26 | P38 | Names of the ten monitored objects | "monitoring points" (p. 13, l. 256 and l. 259, Table 2 caption, Fig6 caption, p. 20, l. 392, Fig10 caption), "monitored blocks" (p. 13, l. 262 to 263; p. 20, l. 401; p. 22, l. 414 and l. 417), "Block 1 and Block 3" (p. 20, l. 397), "Blocks 1 and 3" (p. 22, l. 416), "point 1" to "point 10" (Fig9 caption), legend 1 to 10 (Fig10 (a)) | no finding; Table 2 title ties points to blocks |
| PP-27 | P1 | Table 2 volumes as a share of the model volume | sum 11512.7 m³, mean 1151.3 m³, range 756.2 to 1754.3 m³; 11512.7 / 317563 = 3.63 % | no finding on the arithmetic; used in GB-41, GB-44 |
| PP-28 | P21 | Normalisation of the shape indices (p. 14, l. 274 to 280) | VS and AG are dimensionless ratios to the initial state | no finding on normalisation; the base of the ratio is GB-35 |
| PP-29 | location check | Locations on uncertain lines (p. 13 to 14 between l. 266 and l. 269) | Table 2 and Fig6 cited by page and element in all instances and here | no finding |
| PP-30 | P30 | Reported errors and their correction against reported runs | no error or correction reported; one run | no finding |
| PP-31 | P33 | Effort statements | search "time-consuming", "comput" (3 hits, none on effort) | no finding |

### Segment 3: Results (p. 15 to 25)

#### Substantive findings

**GB-38 The validation is a visual comparison of two features with a deposit eroded for two centuries, while the Results and Conclusion 2 claim that the simulation reproduced the entire process and ensures agreement.**

| Field | Content |
|---|---|
| Check | P10, P11, P9, P15, P32, P17 |
| Location | p. 15, l. 299 to 300; p. 16, l. 348 to 359; Fig7 (o) (p. 19); p. 19, l. 369 to 370; p. 25, l. 471 to 472; p. 5, l. 110 to 111; p. 7, l. 149 to 156 |
| Quotation | "The results of the numerical simulation successfully reproduced the entire process of the Mogangling landslide."; "Fig7. (o) presents compelling evidence of agreement between the numerical simulation results and the actual field observations."; "Comparison with field imagery and result analysis ensures that the simulation outcomes align with actual conditions." |
| Concern | The comparison in Fig7 (o) identifies two corresponding features (a ridge dividing the source area; extent and morphology of the deposit), which is a sensible first check, but without a metric; the Results sentence says "support" (p. 16, l. 359), Conclusion 2 says "ensures". No simulated quantity is put beside a field quantity, although p. 7, l. 149 to 156 gives length, width, area, thickness, volume and elevations. The manuscript discloses weathering since 1786 (p. 16, l. 353 to 355) and that the dam break was not modelled (p. 16, l. 348 to 350); not drawn through is that the simulated end state is the intact dam, while the dam burst after 9 days (p. 5, l. 110 to 111) and the present deposit is what remained after breaching and erosion. The abstract of Zhao et al. (2021), in the reference list, describes a main right-bank and a residual left-bank deposit and a dam crest about 130 m above the present river, quantitative targets the simulation could be held against. Parameters were partly obtained by "parameter inversion" (p. 11, l. 207); if the inversion target was the deposit, the comparison is not independent (question). "reproduced the entire process" claims more than an end-state comparison can show, since no intermediate state was observed. The field values are themselves inconsistent (GB-15), which a quantitative comparison would have to resolve first. Conclusion 2 also omits the disclosed limits (ignored structural planes, proxy ground motion, smoothed terrain, unmodelled dam break) and the volume difference of GB-41. Severity: two instances graded moderate, one major; the higher applies because the claimed reproduction of the 1786 event underlies the reading of all results. |
| Suggestion | Add to Sect. 3.1 a table of simulated against field values (deposit outline overlap, runout, length, width, thickness or surface elevation difference against the post-event DEM in areas not affected by later erosion, dam crest against the published value); state the inversion target and keep calibration and validation targets separate; reword p. 15, l. 299, p. 16, l. 353 and Conclusion 2 (p. 25, l. 471 to 472) to the end-state agreement actually tested ("supports" instead of "ensures"), and name the disclosed limits in the Conclusions. |
| Status | verified (wording; absence of metrics; page image p. 19); Zhao et al. (2021) verified in the abstract (https://ideas.repec.org/a/spr/nathaz/v106y2021i1d10.1007_s11069-020-04471-1.html, not full text); independence of the inversion: assumption, posed as a question |
| Severity | major |
| Source | S3, SD, S4 |

**GB-39 Fig7 (h) to (n) do not say which stress is shown on which section, and Fig7 (h) shows 0 MPa everywhere although the dynamic run starts from static equilibrium.**

| Field | Content |
|---|---|
| Check | P3 |
| Location | p. 15, l. 301 to 302; Fig7 (h) to (n), colour bars and axes (p. 18); p. 19, l. 368 to 370; p. 10, l. 199 to 201 |
| Quotation | "Fig7 illustrates the cloud maps of velocity distribution for the overall model and stress distribution along the sliding plane" |
| Concern | The panels show a vertical section (x 0 to 2700, z 0 to 1200, no axis titles) with colour bars from 0 (red) to minus 31 to minus 47 "Mpa"; neither caption nor text says which stress (a component such as Stress-ZZ of Table 2, a principal stress, a mean stress) and which section is shown, and "along the sliding plane" does not fit a full vertical section. Fig7 (h), t = 0 s, has a colour bar labelled "0" at both ends and is uniformly red. After static equilibrium under gravity (p. 10, l. 199 to 201) the stress at t = 0 should increase with depth, as it does in (i) to (n). Was the stress reset to zero, or does (h) show another quantity? The colour bar labels read "0Mpa", "-33Mpa", "-31Mpa", "-47Mpa" (compared in all seven panels), and the text and caption say "cloud map" (p. 15, l. 301; p. 19, l. 368 to 369). The missing axis titles are part of GB-19, the unreported equilibrium record GB-25, the field comparison in Fig7 (o) GB-38; here only the stress panels are at issue. |
| Suggestion | State in the caption of Fig7 (p. 19, l. 368 to 370) the stress quantity, the sign convention and the position of the section, and mark it in Fig7 (a); explain or correct the uniform 0 MPa in Fig7 (h); write "MPa" with a space after the number in all colour bars; replace "cloud map" by "contour map" in p. 15, l. 301 and p. 19, l. 368 to 369. |
| Status | verified (labels and colours); inferred (expected stress state at t = 0) |
| Severity | moderate |
| Source | AB, S4 |

**GB-40 The energy balance presented as evidence of conservation closes by definition through Eq. (4), for the whole mass and for every block, so Fig8 cannot show that the whole mass conserves energy or that the simulation succeeded.**

| Field | Content |
|---|---|
| Check | P23, P15, P3, P31, P10 |
| Location | p. 19, l. 375 to 377; p. 19, l. 387 to 389; p. 12, l. 245; p. 13, l. 249; p. 20, l. 393 to 394; p. 1, l. 26 to 28; p. 25, l. 476 to p. 26, l. 482; Fig8 (p. 20); Fig9 (a) to (j) (pp. 21 to 22) |
| Quotation | "It is evident that, due to the law of energy conservation, the total sum of the three forms of energy remains constant throughout the landslide."; "This can be regarded as a successful energy extraction numerical simulation."; "its energy change conforms to the law of conservation of energy; For some blocks, the energy is not conserved"; "the sum of the three energies equals the initial potential energy before sliding" |
| Concern | The bookkeeping is laid out clearly in Eqs. (1) to (4), which makes this check possible. Eq. (1) defines ME = KE + PE, Eq. (4) DE(ti) = ME(t0) minus ME(ti) (page images p. 12 and 13). Then KE + PE + DE = ME(t0) at every time and for every block, whatever the simulation does; a numerical check over 10 000 random states gives a maximum deviation of 0. The constant total in Fig8 is therefore a property of the definition. Measured on the page images, the top of the stack is constant in Fig8 (all 105 bars within 1 px = 9.6 GJ of 6516 GJ in one measurement, 868 of 893 pixel columns within 3 px of 6501 GJ in another) and equally constant in every panel of Fig9 (each within 3 px). The contrast "conserved" against "not conserved" (abstract, p. 20, l. 393 to 394, Conclusion 3) thus cannot rest on the sum; it rests on whether the residual DE rises monotonically (p. 19, l. 387 to 388) or falls at times (p. 20, l. 399 to 402), which the manuscript itself attributes to "the calculation method used" (p. 20, l. 399 to 400). Moreover DE as a residual lumps together friction, numerical damping, energy radiated through the viscous boundaries and, with opposite sign, the work of the seismic input at the base (p. 10, l. 189 to 198), which can raise ME; under this definition any net seismic input appears as a reduction of DE, and p. 19, l. 380 to 381 attributes early DE to friction without separating these terms. Is DE taken as the residual, or from an independent energy record of 3DEC? Only in the second case would closure be a test. The abstract also continues with capitals after semicolons ("; For some blocks", "; Compared with"). The cause attributed to the falling DE of single blocks is GB-42. Graded major: the first result named in the abstract and Conclusion 3 follows from a definition. |
| Suggestion | State in Sect. 2.3 (p. 13, l. 249 to 255) how DE was obtained; if it is the residual, say so in the captions of Fig8 and Fig9 and replace the conservation statements in the abstract (p. 1, l. 26 to 28), Sect. 3.2.1 (p. 19, l. 375 to 377 and l. 388 to 389), Sect. 3.2.2 (p. 20, l. 393 to 396) and Conclusion 3 (p. 25, l. 476 to p. 26, l. 482) by an energy balance whose terms are taken independently from the solver (frictional work at contacts, damping work, boundary work of the seismic input and radiated energy, elastic strain energy), with the closure error against ME(t0); report as results what is not definitional, the monotonic rise of DE for the whole mass and the intervals of falling DE for blocks 1 and 3. Write "; for some blocks" and "; compared with" in the abstract. |
| Status | verified (Eqs. (1) and (4) on the page images p. 12 and 13; bar tops measured by three instances); inferred (composition of the residual); assumption (whether 3DEC energy records were used instead of Eq. (4)), posed as a question |
| Severity | major |
| Source | S3, S4, AB, SD |

**GB-41 The energies of the whole mass in Fig8 cannot be reconciled with either stated landslide volume, with the block count and block volumes, with the density and with the velocities of Fig5 and Fig7.**

| Field | Content |
|---|---|
| Check | P2, P3, P8 |
| Location | Fig8 (p. 20); p. 9, l. 181 to 182; p. 7, l. 151; p. 9, l. 173 to 175; Table 2, column Volume (p. 13); Table 1, row landslide mass, column Density (p. 11); Fig7 (e), colour bar (p. 17); Fig5 (b) (p. 12) |
| Quotation | "The whole model contains 25345 blocks, 2788 m long, 3341 m wide, 1121m high, and the volume of the landslide is 317563 m3."; "and the volume is about 2400×104 m3" |
| Concern | Fig8 was measured bar by bar (y: 0 at 1430.5 px, 7000 GJ at 699.5 px; x: 0 s at 682.5 px, 120 s at 1509.5 px): initial PE about 6500 GJ (6501 to 6516 GJ in three independent measurements); KE maximum 1666 to 1685 GJ at about 13.6 to 13.7 s. Case distinction (Python, g = 9.81 m/s², ρ = 2300 kg/m³ from Table 1). (A) V = 317563 m³ (p. 9, l. 182): m = 7.30 × 10^8 kg; the initial PE requires a mean drop of the centre of mass of 907 to 909 m, more than the relief from the crest of the mass to the river (747 m + 131 m = 878 m, p. 9, l. 174 to 175) unless the datum lies below the river; the KE maximum requires a root mean square speed of 67.5 to 67.9 m/s, while the largest velocity in the snapshots of Fig7 is 31.6 m/s and the fastest curve of Fig5 (b) peaks at 45.5 m/s (at 45.5 m/s this mass holds at most 756 GJ). (B) V = 2400 × 10^4 m³ (p. 7, l. 151, intended reading): m = 5.52 × 10^10 kg; the PE then corresponds to a mean drop of only 12.0 m, against drops of hundreds of metres in Fig3 (b) and Fig10 (a). (C) Block count: if all 25345 blocks belonged to the landslide mass, the mean block volume would be 12.53 m³, while the ten monitored blocks in Table 2 have 756.2 to 1754.3 m³ (mean 1151.3 m³); at that mean 317563 m³ holds only 276 blocks, whereas 25345 such blocks would give 2.92 × 10^7 m³. Independently of the volume, 1685 GJ at speeds of at most 45.5 m/s needs at least 1.63 × 10^9 kg, that is 7.1 × 10^5 m³, 2.2 times the volume of p. 9, l. 182. The field volume is itself inconsistent with area and thickness (GB-15), and the restoration that defines the mass is unchecked (GB-17); the conservation identity is GB-40. The model description at p. 9, l. 173 to 182 is also the subject of GB-20 (settings), GB-21 (planes) and GB-22 (units); here only the mass is at issue; the unnamed source of the geological drawing in the same passage is GB-12. Severity: one instance graded major, two moderate; the higher applies because every energy in Fig8, Fig9 and Fig12, and the KE value at the transition of Sect. 3.4, scales with the mass that cannot be determined. |
| Suggestion | State in Sect. 2.1 (p. 9, l. 173 to 182) the number of blocks of the landslide mass, its volume and mass, and the number of base blocks; state in Sect. 2.3 and the caption of Fig8 the mass and the reference elevation used for PE, and the time step of the bars; check the energy computation behind Fig8, Fig9 and Fig12 against these values and the velocities in Fig7; reconcile p. 7, l. 151 and p. 9, l. 182, or state the scale factor between field and model and its effect on the energies. |
| Status | verified (values in text and tables; Fig8 and Fig5 measured); inferred (implied drops, speeds and masses, Python; that no stated volume fits) |
| Severity | major |
| Source | S3, AB, SD, S4 |

**GB-42 Energy transfer between blocks is stated as the cause of non-conservation and of longer runout, but it is not measured; decreases of DE are a property of the residual and have other possible causes.**

| Field | Content |
|---|---|
| Check | P31, P27 |
| Location | p. 20, l. 392 to 402; Fig9 (a), (c) (p. 21); p. 1, l. 27 to 30; p. 24, l. 445 to 447; p. 25, l. 479 to p. 26, l. 482; p. 26, l. 485 to 487 |
| Quotation | "unlike the total landslide mass, the energy of single blocks is not conserved. This is because each block is subjected to compression and pushing forces from surrounding blocks"; "When the rear rock mass collides with the front, its dissipated energy sharply increases and transfers energy to the front rock mass, enabling the front portion to slide farther." |
| Concern | Fig9 shows the same identity as Fig8 (GB-40): for every block the bar tops stay constant, so "not conserved" means only that DE, the residual, decreases at times. The manuscript partly discloses this ("due to the calculation method used", p. 20, l. 399 to 400) but still draws a causal conclusion. A rise of a block's ME can come from contact forces of neighbours, from the seismic input transmitted through the base, or from numerical effects; these are not separated, and no inter-block work is computed. No passage reports DE of rear blocks rising at the moment of contact with front blocks, and the step to "enabling the front portion to slide farther" is not measured either. The comparison of front and rear groups is GB-45. Graded major: the abstract and Conclusions 3 and 4 state the cause. |
| Suggestion | Compute for the monitored blocks the work of contact forces from each neighbour (force times relative displacement at the contacts) and the work of the base input, and show that the ME increases coincide with contact work from upslope blocks; otherwise restrict p. 20, l. 393 to 402 and Conclusions 3 and 4 to the observation that the ME of single blocks increases at times, without attributing a cause. |
| Status | verified (wording; Fig9 bar tops measured); inferred (alternative causes, from Eq. (4) and the boundary set-up) |
| Severity | major |
| Source | SD |

**GB-43 The potential-energy rebound of blocks 1 and 3 in Fig9 is a slow rise over 30 to 40 s without kinetic energy, which does not look like a bounce to the opposite bank.**

| Field | Content |
|---|---|
| Check | P3 |
| Location | p. 20, l. 397 to 399; Fig9 (a) and (c) (p. 21); p. 22, l. 415 to 416 |
| Quotation | "exhibit a rebound in potential energy after it approaches zero. This can be explained by these blocks bouncing to the opposite bank after impacting the base, increasing their potential energy." |
| Concern | The rebound itself is confirmed by measurement. Fig9 (a), block 1: PE = 0 from 73 to 80 s, then 0.04 GJ at 81 s, 0.21 GJ at 91 s and 110 s, 0.37 GJ at 121 s and constant to 131 s. Fig9 (c), block 3: PE = 0 from 85 to 88 s, then 0.26 GJ at 99 s, 0.12 GJ at 108 s, 0.34 GJ at 121 s. During these rises the KE layer is below 1 px (0.012 GJ in (a), 0.010 GJ in (c)) in every bar of (a) and at most 0.02 GJ in (c). A ballistic bounce converts KE into PE within seconds and needs at least as much KE as the PE gained; here PE grows over 30 to 40 s with no visible KE. The accompanying DE decrease rather suggests that the blocks are pushed or lifted by surrounding debris. One instance accepted "confirming the previous inference" (p. 22, l. 416) because Fig10 (a) shows a rebound in the trajectories; this does not contradict the measurement, which concerns the mechanism, not the occurrence. The sentence also has an unclear "it" ("after it approaches zero"). The causal reading of DE decreases is GB-42. Could the authors check the Z history of blocks 1 and 3? |
| Suggestion | Revise p. 20, l. 397 to 399 and p. 22, l. 415 to 416 using the Z history of blocks 1 and 3 (for example "after their potential energy approaches zero"); mark the rebound interval in Fig9 (a) and (c). |
| Status | verified (measured PE and KE); inferred (mechanism) |
| Severity | moderate |
| Source | AB, S4 |

**GB-44 The block energies in Fig9 cannot be reconciled with the block volumes and elevations of Table 2, the density of Table 1 and a common datum, and their kinetic share is far below that of the whole mass.**

| Field | Content |
|---|---|
| Check | P2, P3, P7, P8 |
| Location | Fig9 (a) to (j) (pp. 21 to 22); Table 2, columns Coordinate and Volume (p. 13); p. 13, l. 250 to 255; Table 1, row landslide mass, column Density (p. 11); Fig8 (p. 20); Fig5 (a), (b) (p. 12) |
| Quotation | "m is the mass of the monitored block (kg)"; "uses the model’s initial height as the reference datum rather than true sea level" |
| Concern | Measured totals of the bars (each panel calibrated on its own ticks) for blocks 1 to 10, in GJ: 5.06, 5.13, 3.98 to 4.01, 3.55 to 3.57, 11.08, 6.59, 1.18, 4.36, 1.60, 0.95 (two further instances read the same within reading accuracy). With ρ = 2300 kg/m³ and the Table 2 volumes, the drop implied by E = ρVgh is 238.5, 222.5, 234.0, 163.1, 316.2, 172.5, 29.8, 192.7, 82.5 and 43.4 m (Python). Under one common datum, the top blocks 9 and 10 (z = 752 and 755) start 397 to 415 m above the bottom blocks 1 and 2 (z = 340 and 355) and should hold more PE per volume; the implied drops are reversed (82.5 and 43.4 m against 238.5 and 222.5 m), and the neighbours 7 and 8 (z = 661 and 692) differ by a factor of 6.5. The implied datums lie at model z of about 100 to 710 m, different for every block, so PE and DE magnitudes in Fig9 are not comparable between blocks, and the described datum ("initial height") does not fit PE falling to about zero. The ten blocks hold 3.63 % of the model volume but 0.67 % of the initial energy of Fig8. KE maxima of the blocks are 2.1 to 6.7 % of their bar totals; at about 13.6 s, when the whole mass holds 25.9 % of its energy as KE, the ten blocks hold 1.3 %, and their peak speeds implied by Table 2 masses are 3.9 to 17.5 m/s, against 45.5 m/s and 13.5 m/s in Fig5 (b) and (a). The mass behind the whole-mass energies is GB-41; the KE(ti) missing at p. 13, l. 246 is KK-25; the causal reading of the DE decreases in Fig9 is GB-42 and the rebound of blocks 1 and 3 GB-43; here the magnitudes are at issue. Severity: one instance graded major, two moderate; the higher applies because the block energies carry the abstract claim that the lower rock mass receives more energy transfer (p. 1, l. 29). |
| Suggestion | Give in Table 2 the mass and the initial PE of each monitored block, state in Sect. 2.3 (p. 13, l. 250 to 255) the datum actually used for each PE value and the velocity definition (resultant or component), and check Fig9 against these values; if per-block datums were used, recompute with a common datum before comparing blocks; state which block Fig5 (a) and (b) show. |
| Status | verified (Table values on the page images p. 11 and 13; bar values measured); inferred (implied drops, datums and speeds, Python, assuming the Table 1 density applies), posed as a question |
| Severity | major |
| Source | S3, SD, AB |

**GB-45 The abstract and Conclusion 4 compare collision frequency, compression, energy received and travel distance between lower and upper or front and rear parts, but the Results report none of these per block or group, and the parts are named in three ways.**

| Field | Content |
|---|---|
| Check | P11, P15, P10, P34, P9, P6, P38 |
| Location | p. 22, l. 414 to 421; Fig10 (b) (p. 23); p. 1, l. 28 to 30; p. 3, l. 86 to 87; p. 13, l. 256 to 259; Table 2, column Position (p. 13); p. 26, l. 483 to 487 |
| Quotation | "Compared with the upper rock mass, the lower rock mass is compressed more frequently, receives more energy transfer, and has a longer migration distance."; "during the collapse stage, the front portion of the rock mass experiences more collisions than the rear portion, with a clear trend of decreasing collision frequency toward the rear" |
| Concern | The design with ten monitored blocks in four position groups (Table 2) suits the announced comparison (p. 3, l. 86 to 87). The matrix of four groups against the announced quantities (effective collisions, energy received, travel distance, compression) has, however, no filled cell in the Results. Search of p. 15, l. 297 to p. 25, l. 459 (text.json, confirmed on the page images) for "front", "rear", "lower", "upper", "bottom", "top", "migration", "run-out", "runout" and "travel distance": 10 hits on 9 lines, none giving a count, an energy or a distance per block or group; "collapse stage" occurs once (p. 15, l. 322), in the velocity description, without collision counts. Fig10 (b) plots collisions against travel distance in one pooled series without block ID, position or stage. "compressed more frequently" is not measured: the stress histories were recorded but not reported (GB-25). Selection: 10 of 25345 blocks (0.039 %), 2 or 3 per zone, chosen as "representative" (p. 13, l. 257) without a rule, so no dispersion within a zone can be estimated. Naming: the same kind of finding is stated with lower and upper (abstract; p. 13, l. 256 to 257), bottom and top (Table 2; Fig6) and front and rear (Conclusion 4); whether "front" means the Table 2 groups bottom and lower middle part or the front of the moving mass cannot be decided. The headline comparison therefore has no reported basis. The energy-transfer cause is GB-42, the labels of Fig6 GB-34, the term migration distance GB-29, the rebound of blocks 1 and 3 GB-43; here the comparison of groups is at issue. Graded major: the statement is one of three results named in the abstract. |
| Suggestion | Add to Sect. 3.2.2 a table with, for each of the ten blocks and each position group, the number of effective collisions (in total and per stage of Fig7), the energy received (sum of DE decreases) and the travel distance; better, run the detection for all blocks of the mass or a stratified sample (for example at least 30 per zone) and report counts per zone and stage with spread; use the Table 2 terms in the abstract (p. 1, l. 28 to 30), p. 13, l. 256 to 257 and Conclusion 4 (p. 26, l. 483 to 487), or define front and rear; otherwise restrict the abstract and Conclusion 4 to the relation between travel distance and collision frequency that Fig10 (b) shows. |
| Status | verified (search as stated; Table 2 groups and Fig10 (b) on the page images); assumption (whether front and lower denote the same blocks), posed as a question |
| Severity | major |
| Source | S3, S4, SD, S2 |

**GB-46 It is not stated over which population the 1,139 effective collisions and the points of Fig10 (b) are counted; the points sum to about 1217 and do not rise continuously as stated.**

| Field | Content |
|---|---|
| Check | P20, P3 |
| Location | p. 22, l. 418 to 419; Fig10 (b) (p. 23); p. 11, l. 233 to 234; p. 11, l. 221; p. 22, l. 414 to 415 |
| Quotation | "it is clear that as the migration distance increases during the landslide, the number of collisions also rises continuously, reaching a peak once the blocks enter the river channel"; "Under this setting, 1,139 effective collisions were detected from the travel-distance versus velocity profile." |
| Concern | The count has no denominator. Fig5 (a) is "a typical velocity-travel-distance curve for an individual block" (p. 11, l. 221) reaching about 600 m, Fig5 (b) to (f) show one curve reaching about 2500 m, and p. 11, l. 234 speaks of one "profile"; the 1,139 may refer to one block, to the ten monitored blocks or to all blocks of the mass, whose number is not given (GB-41). Fig10 (b), measured at 300 dpi (y: 0 at 1190.5 px, 175 at 704.0 px; x: 0 at 1331.0 px, 2500 m at 1910.5 px), has 26 points at 100 m spacing from 0 to 2500 m with values 0, about 0.5, 3.1, 4.9, 5.8, 7.7, 15.1, 16.0, 7.0, 27.2, 20.0, 23.9, 29.9, 27.9, 37.1, 41.9, 48.9, 49.8, 52.9, 61.0, 69.1, 71.9, 142.1, 157.0, 150.0, 146.0 (each ± 0.4); sum 1216.7 ± 10, 6.8 % above 1,139 (two further instances: 1213 and about 1218). The values fall four times (700 to 800 m, 900 to 1000 m, 1200 to 1300 m, after the maximum at 2300 m), so "rises continuously" describes the fitted curve, not the points. The comparison of positions is GB-45, the axis title and the curve GB-48, the normalisation GB-47, the markers of Fig5 (a) GB-28 and the name of the abscissa GB-29. Where along the travel distance do the blocks enter the river channel? |
| Suggestion | State at p. 11, l. 233 the population (number of blocks or profiles) and in the caption of Fig10 (b) (p. 23, l. 423 to 424) what one point is (collisions per 100 m bin, summed over which blocks) and how the sum relates to the 1,139; describe at p. 22, l. 418 to 419 the trend of the points (overall increase, maximum at 2300 m, local decreases); mark the river channel on the x axis. |
| Status | verified (missing population; point values and non-monotonic course measured); inferred (relation of the sum to the 1,139) |
| Severity | moderate |
| Source | S3, AB |

**GB-47 The statement that the lower mass collides "more frequently" rests on absolute counts that are not normalised by path length or by the number of blocks contributing to each distance.**

| Field | Content |
|---|---|
| Check | P21 |
| Location | p. 22, l. 418 to 421; Fig10 (b) (p. 23); p. 1, l. 29; p. 26, l. 484 to 485 |
| Quotation | "the lower rock mass is compressed more frequently" |
| Concern | Fig10 (b) shows absolute numbers of effective collisions per 100 m of travel distance. Blocks that travel farther pass through more bins and collide more often in total even at the same rate per metre; conversely, if counts are summed over blocks, fewer blocks reach the far bins. Blocks starting low reach the river channel, where the bins rise from about 72 (2100 m) to 142 to 157 (2200 to 2300 m), so position and distance are confounded. Without the number of blocks contributing to each bin, a rise with distance can reflect the composition of the population as well as a higher rate; "more frequently" requires a rate per block and per metre or per second. This finding asks for normalisation; the missing per-group values are GB-45, the missing population GB-46, the term migration distance GB-29. Would the comparison of lower and upper blocks hold if the counts were divided by each block's travel distance? |
| Suggestion | Add to Fig10 (b) or to the table proposed in GB-45 the collisions per block per 100 m (or per second) and the number of blocks contributing to each bin. |
| Status | verified (absence of normalisation, page image p. 23); assumption (effect on the comparison), posed as a question |
| Severity | moderate |
| Source | S3 |

**GB-48 Fig10 (b) does not say what "Frequency" counts, nor what the red curve is.**

| Field | Content |
|---|---|
| Check | P29 |
| Location | Fig10 (b), y axis and red curve (p. 23); p. 23, l. 423 to 424 |
| Quotation | "Fig10. (a) movement trails of 10 monitoring points and (b) the plot of travel distance vs. collision frequency." |
| Concern | The y axis is titled "Frequency" without unit or reference (collisions per 100 m bin, per block, per second?), and the red curve has no legend entry, equation or mention in caption or text (searched p. 22, l. 414 to 421 and the caption for "curve", "fit", "fitted", "exponential", "regression": 0 hits). A reader cannot tell whether the curve is a model fit and on which data. Unlike GB-46, which concerns what the text reads from the points and their population, and GB-45 and GB-47, which concern the comparison of positions, this finding concerns the figure's self-explanation; the earlier study with the same plot type is GB-08, which concerns novelty, not the figure. |
| Suggestion | Title the y axis "Number of effective collisions per 100 m" (or the actual definition); add a legend entry for the red curve with its type, equation and R²; extend the caption (p. 23, l. 423 to 424) accordingly. |
| Status | verified |
| Severity | minor |
| Source | AB |

**GB-49 Fig12 plots at least 30 points per curve although envelopes were fitted at ten times, and its kinetic energy maximum (1116.8 GJ) is not the maximum of Fig8, so VS = 29.47 % and AG = 319.5 % do not mark the kinetic energy peak.**

| Field | Content |
|---|---|
| Check | P2, P3, P7, P34 |
| Location | p. 23, l. 426 to 427; Fig12 (a), (b) (p. 25); Fig11 (pp. 23 to 24); p. 24, l. 440 to 441; p. 25, l. 453 to 456; Fig8 (p. 20) |
| Quotation | "to perform Alpha Shape envelope fitting on the deposit mass at 10 representative time points"; "At this point, the kinetic energy peaks" |
| Concern | Fig11 shows ten envelopes (0 s to 131 s), consistent with p. 23, l. 427. On the DE curve of Fig12 (a), markers were counted at VS = 20, 29, 32, 33, 37, 48, 50, 74, 104, 201, 219, 373, 381, 426, 480, 516, 536, 567, 603, 636, 679, 742, 806, 855, 894, 922, 1088, 1147, 1212 and 1238 %: 30 markers, a lower bound because touching markers below 40 % count as one (two further instances counted at least 12 and 13 markers above VS 500 % alone). Either more envelopes were fitted or values were interpolated; neither is described, nor the rule for choosing the ten times. Every Fig12 point sums to the Fig8 total (VS 74 %: 3548 + 2304 + 670 = 6522 GJ; VS 103 %: 6517 GJ; VS 201 %: 6516 GJ), so Fig12 uses the Fig8 energies. The labelled maximum (PE 4983, KE 1117, DE 426 GJ) matches the Fig8 bar at 11.1 s (PE 4994, KE 1082, DE 440 GJ); the bars at 12.4 s (KE 1590 GJ) and 13.7 s (KE 1685 GJ) have no counterpart among the Fig12 points, and the KE maximum of Fig8 (1666 to 1685 GJ, measured by two instances) is 549 to 568 GJ (33 to 34 %) above the 1116.8 GJ labelled in Fig12. The VS and AG at the actual KE maximum are therefore unknown, and the transition values of p. 25, l. 453 to 454 refer to an earlier sampled state. The labelled marker itself is placed correctly (PP-38). The naming of VS and AG is GB-37; the interpretation of the transition GB-50; the object enclosed by the envelope GB-35. |
| Suggestion | State in Sect. 2.4 or 3.4 and in the caption of Fig12 at how many times VS and AG were computed, how the times were chosen and whether points are interpolated (mark them); compute VS and AG at the times of the KE maximum of Fig8 (12 to 14 s) and correct p. 25, l. 453 to 455. |
| Status | verified (marker counts as lower bounds; measured values); inferred (time matching between Fig12 and Fig8) |
| Severity | moderate |
| Source | S3, AB, SD |

**GB-50 Fragmentation, debris production and a "solid to fluidized" transition are inferred from envelope growth and DE, not measured, and Conclusion 5 states them as results.**

| Field | Content |
|---|---|
| Check | P31, P10, P15 |
| Location | p. 24, l. 445 to p. 25, l. 456; p. 16, l. 325 to 329; p. 23, l. 429 to 431; Fig12 (p. 25); p. 26, l. 488 to 492; p. 9, l. 178 to 181 |
| Quotation | "When the volume expansion rate reaches approximately 29.47% and the surface area growth reaches about 319.5%, it can be considered that the landslide transitions from a solid phase to a fluidized phase."; "it can be concluded that during energy transfer, collisions and friction cause blocks to fracture and disintegrate, generating a large amount of debris" |
| Concern | The measured quantities are envelope volume and area (VS, AG; Fig11, Fig12). Sect. 3.4 offers the fragmentation mechanism as an interpretation ("can be interpreted as follows", p. 24, l. 445) and takes the rise of DE as confirmation (p. 24, l. 451). No fragmentation measure is reported: a search of the Results for "number of blocks", "number of fragments" and "contact" gives 0 hits; there is no count of broken contacts or separated blocks and no block size distribution. Envelope growth measures spreading and would also occur without fracture; DE is a residual (GB-40) and contains every mechanical energy loss. The model mass is pre-cut into 8.7 m × 8.7 m columns with an internal structural plane (p. 9, l. 178 to 180); can these blocks fracture into "newly formed fragments", or does the envelope grow by separation of pre-cut blocks? What in the model represents "fine debris such as rock fragments" and the "loosely consolidated fractured layer approximately 20 meters thick" (p. 16, l. 326 to 328)? Fragments that fill the interior of the deposit would not by themselves enlarge an alpha-shape envelope. "fluidized phase" has no criterion, and the threshold is the VS value of one sampled point that misses the KE maximum (GB-49). Neighbouring findings treat the planes and units of the model (GB-21, GB-22), its mass (GB-41), the name of the enveloped object (GB-35), the names of VS and AG (GB-37) and the causal reading of DE decreases (GB-42); here the fragmentation mechanism is at issue. Severity: one instance graded moderate, the other major; the higher applies because Conclusion 5 and the phase-transition result rest on the unmeasured mechanism. |
| Suggestion | Add a direct fragmentation measure (number of broken potential-discontinuity contacts and block size distribution over time) and show it against VS, AG and DE in Sect. 3.4; define the fluidization criterion before applying it and determine the threshold from a densely sampled series that contains the KE maximum; otherwise present the mechanism in p. 24, l. 445 to p. 25, l. 456 and Conclusion 5 (p. 26, l. 488 to 492) as interpretation and keep the measured growth of VS and AG as the result. |
| Status | verified (wording and search); inferred (that envelope growth can occur without fracture); assumption (whether the 3DEC blocks can fracture), posed as a question |
| Severity | major |
| Source | SD, S4 |

#### Minor corrections

| ID | Location | Quotation | Replacement | Source |
|---|---|---|---|---|
| KK-26 | p. 22, l. 410 to 413 | "point 1 ; (b) energy evolution of point 2 ;" (space before each of the 9 semicolons) | "point 1; (b) energy evolution of point 2;" and so on; the content of Fig9 is GB-44, the earlier study with the same figure type GB-08 | S4 |
| KK-27 | p. 23, l. 425 | "3.4 Structural evolution as a function of energy change" | "3.3 Structural evolution as a function of energy change" (search for "3.3" in text.json: 0 hits; headings 3.1, 3.2, 3.2.1, 3.2.2, 3.4 on the page images) | S3, S4, SD |
| KK-28 | p. 24, l. 438 to 439 | "(a-i) when time = 0s, 3s, 7s, 9s, 12s, 15s,32s,71s, 100s," | "(a to j) when t = 0 s, 3 s, 7 s, 9 s, 12 s, 15 s, 32 s, 71 s, 100 s and 131 s." (ten panels (a) to (d) on p. 23 and (e) to (j) on p. 24); the renderings of Fig11 are GB-31 | S3, S4, SD, AB |

#### Verification log

| ID | Check | Checked | Values | Result |
|---|---|---|---|---|
| PP-32 | P2, P24 | Duration and time points in text and figures | 131 s in p. 15, l. 300 to 301, Fig7 caption (p. 19, l. 368 to 369) and Fig11 caption (p. 24, l. 438 to 439); Fig7 times 0, 3, 7, 9, 12, 15, 131 s are a subset of the Fig11 times 0, 3, 7, 9, 12, 15, 32, 71, 100, 131 s; end of all Fig9 axes 131 s; Fig9 (a) PE = 0 from 73 to 80 s, Fig9 (c) from 85 to 88 s | no finding on dates; rebound in GB-43 |
| PP-33 | P2 | Stage sequence in Sect. 3.1 against the time line in Sect. 3.2.1 (p. 15, l. 306 to p. 16, l. 347; p. 19, l. 378 to 384) | maximum velocities 5.9, 19.6, 27.1, 31.6, 25.7 m/s, then about 0 m/s at 3, 7, 9, 12, 15, 131 s; peak at the valley floor after 12 s and impact on the riverbed around 13 s compatible | no finding |
| PP-34 | P3 | Fig7 colour bar maxima against the text | (b) 5.9 m/s (p. 15, l. 307), (c) 19.6 (p. 15, l. 315), (d) 27.1 (p. 15, l. 322), (e) 31.6 (p. 16, l. 330), (f) 25.7 (p. 16, l. 339), (g) 0.21 m/s against "gradually approached 0 m/s" (p. 16, l. 346 to 347) | no finding |
| PP-35 | P23, P24, P3 | Fig8 totals and timing; agreement of totals between Fig8 and Fig12 | 105 bars, pitch 1.25 s; KE 0 GJ at 3.7 s, 144 GJ at 5.0 s, 1082 at 11.1 s, 1590 at 12.4 s, 1685 at 13.7 s, 824 at 14.9 s; last bar 130.8 s; stack total 6516 ± 10 GJ in all bars; total about 6500 GJ at start (PE) and end (DE) in Fig8, Fig12 (a) and Fig12 (b) | timing consistent with p. 19, l. 378 to 384 within one bar; totals agree; meaning of the constant total in GB-40 |
| PP-36 | P3 | Colours against legend fields | Fig8 and Fig9 PE #fc8404, KE #fcfc04, DE #0404fc in legend and bars; Fig10 (a) legend lines 1 to 10, smallest pairwise RGB sum difference 77 (lines 4 and 9) | distinguishable (limit 40); Fig3 (a) in GB-18 |
| PP-37 | P29 | Font size of labels at print size, figures at or above 6 pt | Fig8 axis numbers 8.3 pt; Fig6 7.0 pt; Fig4 6.3 pt; Fig7 (h) to (n) 5.7 pt; Fig9 y axis 5.3 to 5.7 pt; Fig5 (a) legend 5.7 pt; caption text 8.0 pt | Fig4, Fig6, Fig8 at or above 6 pt; values below 6 pt in GB-32 |
| PP-38 | P1, P3 | VS and AG at the transition against Eqs. (5), (6) and the labels of Fig12 | VS 29.47 % gives Vt/V0 = 1.2947, AG 319.5 % gives St/S0 = 4.195; labels "29.47" and "319.5" in Fig12 (a) and (b); triangle at VS about 32 ± 2.5 % and 1073 to 1104 GJ (label 1116.8 GJ), in (b) at AG about 316 ± 9 % | labels agree with the text and are placed correctly; sampling in GB-49 |

### Segment 4: Conclusions, declarations, references (p. 25 to 29)

#### Substantive findings

**GB-51 Data and code are withheld "upon reasonable request" without a reason, although none of the listed sources concerns persons.**

| Field | Content |
|---|---|
| Check | P12 |
| Location | p. 26, l. 494 to 495; p. 26, l. 505 to 506 |
| Quotation | "The codes that support the findings of this study are available from the first author, Yunfeng Ge, upon reasonable request."; "The data and materials that support the findings of this study are available from the first author, Yunfeng Ge, upon reasonable request." |
| Concern | The manuscript has a code statement and a data statement, which is good. The Methods name at least these author-held sources (PP-12): the UAV DEM and filtered point cloud, the restored surface, the 3DEC model with 25345 blocks, the histories of the ten blocks and the whole mass, the peak detection that yields the 1,139 collisions, the energy calculation, the alpha-shape envelopes and the VS and AG series, and field findings. All are terrain, rock and simulation data; none concerns persons. Both statements withhold all of them behind a request to one person and give no reason. A reader cannot rebuild the collisions, the energy curves of Fig8 and Fig9 or the VS and AG values (29.47 %, 319.5 %) without the simulation output and the detection and envelope code. The statements contain no link (search "http", "doi", "repositor", "zenodo", "github" in p. 26, l. 493 to 506: 0 hits). The missing numerical settings are GB-20; the external sources missing from the data statement GB-12. |
| Suggestion | In "Code availability" and "Availability of data and material" (p. 26, l. 494 to 506) deposit at least the restored pre-landslide surface, the 3DEC input files, the exported block histories and whole-mass energy series, the peak-detection script and the alpha-shape script in a public repository with a persistent identifier, and cite it; for anything that stays on request, state the reason per item. |
| Status | verified (wording, absence of links, list of sources); inferred (that no source concerns persons, from the method descriptions) |
| Severity | moderate |
| Source | S2, SD |

**GB-52 Seventeen of the 31 reference entries are never cited, among them the earlier studies of the Mogangling landslide and the first author's own energy-evolution study.**

| Field | Content |
|---|---|
| Check | P4 |
| Location | p. 26, l. 508 to 510; p. 26, l. 514 to 516; p. 27, l. 517 to 520; p. 27, l. 524 to 526; p. 27, l. 537 to 555; p. 28, l. 562 to 568; p. 28, l. 588 to 593; p. 29, l. 594 to 599; p. 29, l. 603 to 605 |
| Quotation | "Wu, J., Wang, Y., Dong, S., Chen, Y., and Wang, L.: Genetic Mechanism and Failure Process of the Mogangling Seismic Landslide"; "Ge, Y., Tang, H., and Li, C.: Mechanical energy evolution in the propagation of rock avalanches using field survey and numerical simulation" |
| Concern | Held against all citations (p. 1, l. 34 to p. 2, l. 63, GB-06), 17 of 31 entries (54.8 %) have no citation: Bernardie, Chang, Chen, Dahal, Gao, Ge, Gong, He J., He K., He N., Nava, Sinčić, Wu J., Yang, Zhang J., Zhang K., Zhou. If Zhang et al. (2024) refers to the entry Zhang, J. (GB-06), 16 of 31 (51.6 %). One instance counted 18 by treating the entry Zhao et al. (2021) as uncited; it is counted here as cited with a year mismatch (KK-09). The uncited entries include the Mogangling studies Wu et al. (2013) and Zhou et al. (2024) and Ge et al. (2021) on mechanical energy evolution in rock avalanches, the topic of this manuscript (GB-02, GB-08). The five entries set in a smaller grey typeface (KK-32) are all among the uncited ones. This finding concerns entries without citation; GB-06 concerns citations without entry. |
| Suggestion | Cite each retained entry at the place where it supports a statement, in particular Wu et al. (2013), Zhao et al. (2021) and Zhou et al. (2024) in Sect. 2.1 for the Mogangling setting and Ge et al. (2021) in Sect. 1 and 2.3 for the energy method, and delete the entries that have no such place. |
| Status | verified (entries on the page images p. 26 to 29; citations by search of text.json) |
| Severity | minor |
| Source | S4, S1 |

#### Minor corrections

| ID | Location | Quotation | Replacement | Source |
|---|---|---|---|---|
| KK-29 | p. 25, l. 464; p. 25, l. 466 | "It should be noted that:(a)"; "restoring the contours;(b)" | "It should be noted that: (a)"; "restoring the contours; (b)"; the content of parts (a) and (b) is GB-13, the novelty claim of Conclusion 1 GB-04 | S4 |
| KK-30 | p. 26, l. 499 | "XF: Data curation, Investigation. LZ: Data curation, Investigation." | "XF: Data curation, Investigation; LZ: Data curation, Investigation." | S4 |
| KK-31 | p. 26, l. 507 | "Reference" | "References" | S4 |
| KK-32 | p. 26, l. 508 to 510; p. 27, l. 524 to 526; p. 28, l. 562 to 568; p. 29, l. 597 to 599 | entries Bernardie, Dahal, Nava, Sinčić, Zhang, K. (smaller grey typeface, not justified, on the page images) | set in the typeface of the other 26 entries; whether they stay at all is GB-52, the list as a whole GB-06 | S4 |
| KK-33 | p. 27, l. 530 | "Fan, X., Scaringi, G., Korup, O., et al.:" | full author list as in the other 30 entries; the year label of this entry is GB-01 | S4 |

#### Verification log

| ID | Check | Checked | Values | Result |
|---|---|---|---|---|
| PP-39 | P15 | Each statement of the Conclusions against a place in the Results | C1 restoration: Methods p. 6, l. 138 to p. 7, l. 162, parts (a), (b) without place (GB-13); C2 model ingredients: p. 9, l. 168 to p. 11, l. 212, place found; C2 field comparison: p. 16, l. 353 to 359, verb stronger (GB-38); C2 movement process: Sect. 3.1, place found; C2 collision identification: p. 11, l. 220 to 234, verb stronger (GB-30); C3 whole mass: p. 19, l. 375 to 389, definitional (GB-40); C3 DE rises continuously: p. 19, l. 387 to 388 and Fig8, place found; C3 blocks, temporary DE decrease: p. 20, l. 393 to 402 and Fig9 (a), place found; C4: no place (GB-45); C5 envelope growth: p. 23, l. 426 to 431 and p. 24, l. 440 to 444, place found; C5 mechanism: interpretation only (GB-50). Disclosed: structural planes ignored, proxy ground motion, dam break not modelled, DE decreases due to the calculation method | places found for 6 of 11 statements; the other 5 in GB-13, GB-30, GB-38, GB-40, GB-45, GB-50 |
| PP-40 | P15, P9 | Proposals, recommendations and outlook, each held against the manuscript's own findings | no outlook section; "future" 0 hits, "further" 6 hits, none proposes a study. Proposals found: contour restoration as "a new idea" (p. 2, l. 49 to 51) against the visual acceptance of the smoothed terrain (p. 7, l. 160 to 162); Conclusion 1 (b) reference mountains (p. 25, l. 466 to 468) against the documented procedure; early warning (p. 2, l. 71 to 73) and evaluation basis for the Dadu River area (p. 5, l. 122 to 125) against the Conclusions | in GB-03, GB-04, GB-13, GB-17; no proposal renounces something the manuscript shows to be necessary |
| PP-41 | P15 | Verbs of Abstract, Results and Conclusions against the evidence | "ensures" (p. 25, l. 471), "can be identified" (p. 25, l. 474), "it can be concluded" (p. 26, l. 483 and l. 489), "The results show" (p. 1, l. 26), "It is evident ... due to the law of energy conservation" (p. 19, l. 375 to 376), "confirming the previous inference" (p. 22, l. 416), "it is clear that" (p. 22, l. 418), "further confirms" (p. 24, l. 451). Hedged: "preliminary restoration" (p. 25, l. 463), "support the validity" (p. 16, l. 359), "can be interpreted" (p. 24, l. 445) | overstatements in GB-30, GB-38, GB-40, GB-45, GB-46, GB-50; "confirming the previous inference" no finding on the occurrence of the rebound (mechanism in GB-43) |
| PP-42 | P19 | Data class of each conclusion | Conclusion 1: DEM (primary) plus reconstruction (model); Conclusions 2 to 5: simulation (model); 5 of 5 = 100 % rest wholly or partly on model-generated data; the manuscript names restoration and simulation as basis (p. 25, l. 461 to 462) | no finding for the simulation class; unreported field and laboratory data in GB-26 |
| PP-43 | P16 | Uniformity of the reference list (form only, not against a style) | 31 entries, all with a DOI as https URL and ending with the year; page ranges with hyphen; 30 with full author lists, 1 with "et al." (KK-33); 5 in a deviating typeface (KK-32); alphabetical order kept; book chapters (Hu, Song) without editors or publisher, conference paper (Cheng) with proceedings title, left to the optional citation style check | no finding apart from KK-31, KK-32, KK-33 |
| PP-44 | merge | Mandatory fields and merging of the instance results (step 4.1 and 4.2) | Delivered: 77 substantive findings (S1 7, S2 11, S3 13, S4 9, AB 20, SD 17), 75 minor corrections (S1 7, S2 5, S3 5, S4 43, AB 9, SD 6), 54 verification log entries (S1 3, S2 7, S3 13, S4 7, AB 13, SD 11). All findings had all mandatory fields; discarded: 0. Merged findings: 42 into 17 (GB-03, GB-10, GB-13, GB-15, GB-16, GB-25, GB-30, GB-34, GB-35, GB-38, GB-40, GB-41, GB-44, GB-45, GB-46, GB-49, GB-50); SD-GB-11 split between GB-41 (whole mass) and GB-44 (blocks); S4-GB-06 assigned to GB-38 with parts in GB-30 and GB-41. Minor corrections absorbed into findings whose quotation or suggestion covers the same wording: 30; merged among themselves: 20 into 8; kept unchanged: 25; result 33. Verification log entries merged: 21 into 10; result 43 plus 5 from the merge (PP-44 to PP-48). Hints outside the checklists: all 60 hints (S1 10, S2 12, S3 9, S4 15, AB 8, SD 6) were held against the findings; each was either already covered by a responsible instance or not confirmed (Fig6 band count 3, 2, 3, 2, see GB-34); none became a new finding with source ZF | 52 findings, 33 minor corrections, 48 log entries |
| PP-45 | merge | Contradictions between instances (step 4.3), each rechecked on the manuscript | (1) Citations without entry 15 or 16 and uncited entries 17 or 18: "Zhao et al., 2020" (p. 2, l. 57) counted as year mismatch to the only Zhao entry (GB-06, GB-52, KK-09). (2) Fig6 markers per band: 2, 3, 3, 2 confirmed on an enlarged crop (GB-34). (3) Severity of Fig6 labels, lithology names, validation, whole-mass energies, block energies, front and rear claims, fragmentation: higher grade applied with reason in the concern. (4) Fig8 initial total 6501, 6512, 6516 GJ and KE maximum 1666 or 1685 GJ: reported as ranges (GB-41, GB-49). (5) Fig10 (b): 24 or 26 points; 26 measured by two instances (GB-46). (6) Fig5 (b) to (f) peak against 31.6 m/s: 31.6 m/s is the maximum of the Fig7 snapshot at 12 s (p. 16, l. 330), not of the run; wording restricted (GB-30). (7) Rebound of blocks 1 and 3 accepted by one instance (occurrence) and questioned by another (mechanism): both kept (GB-43). (8) Fig12 markers 12, 13 or 30: lower bounds on different ranges (GB-49) | 8 contradictions decided |
| PP-46 | merge | Wording of quotations and embedded statements (step 4.5) | every quoted string from the manuscript text searched in text.json after normalising line breaks and spaces with Python; strings that stand only in figures (legend labels, axis numbers, colour bar labels) confirmed on the page images p. 4, 6, 8, 10, 12, 14, 18, 23, 25; counts and calculations recomputed with Python (area times thickness, volume ratios, block counts, implied drops and speeds, profile length, reference counts) | 297 quoted strings found in text.json; 79 not found: 47 figure labels, all confirmed on the page images; 23 search terms for which the finding reports 0 hits; 2 titles of cited literature (GB-07); 7 pieces of text between one-character labels such as the section letters. Corrected on rechecking: 3 capitalisations, 1 paraphrase in quotation marks removed (GB-04), 1 quotation with a wrong initial letter (GB-21); all recomputed values agree with the values given |
| PP-47 | merge | Locations at page boundaries and on unsure lines (step 4.5 and 7) | `formatpruefung.py --fundorte` lists locations against text.json, whose line field is the line on the page, not the printed margin number (fassung.json: margin lines not detected); every listed location was therefore counted from the nearest printed margin number: by a mapping of each text.json line to the margin number printed at its start (printed numbers every fifth line) and, for the pages with tables, equations or figures (p. 1, 4, 6, 7, 8, 10, 12, 13, 14, 18, 23, 25), on the page images | 385 locations listed by the script (all, because of the page-line field); all 422 line ends in the locations of the 52 findings and 33 minor corrections held against the printed margin range of their page: 1 outside, corrected (GB-37, now p. 14, l. 287 to p. 15, l. 288); 64 in the first or last two printed lines of a page, each confirmed against the text of that line; quotation positions: 119 of 130 quotations of at least 8 characters start and end within the stated lines, the other 11 stand in tables, equations, captions or figures where the text.json lines are shifted and were confirmed on the page images or are located by element; 3 locations widened to the line of the first quoted word (GB-05 to p. 2, l. 42; GB-10 to p. 5, l. 100; GB-12 to p. 9, l. 181) |
| PP-48 | merge | Pairs with overlapping locations (step 4.2) | `formatpruefung.py --paare` on the draft; every pair decided as merge, absorption or cross-reference in the later identifier | first run 125 pairs, 36 without cross-reference; final run 127 pairs, all with a cross-reference that names what is treated where; 0 errors |

## Optional checks

| Area | What it needs | Responsible | Run |
|---|---|---|---|
| DOI resolution | one fetch per reference entry with a DOI | `science-quellenapparat-pruefung` | no |
| Citation style | the name of the style | `science-zitierstil-harvard-ctr` or the journal's style rules | no |
| AI statement against publisher policy | the target publisher's policy | this review, on request | no |
| Relation to the authors' own prior work | the authors' prior work | this review, on request | no |
| Journal requirements | the author guidelines of the target journal | this review, on request | no |
| Factual correctness | access to the sources of the checked statements and a selection of sections | `science-faktenbeleg-pruefung`, `geo-frage-belegbasiert-klaeren` | no |

## Limits of this review

- Checked version: egusphere-2025-4506.pdf, 29 pages, 5544638 bytes, SHA-256 64cb3787456244aa6102e34f776b47e9a612d06e8894d391758ae240dbe415d6.
- Sources not readable or read only in part: full texts of Ge et al. (2021), Fan et al. (2019, Rev. Geophys.), Zhao et al. (2021), He et al. (2023), Zhou et al. (2024), Du et al. (2021) and Li et al. (2024) (abstracts or figure pages only); Wu et al. (2013), Song et al. (2017), Wu et al. (2024) and Fan et al. (2019, Landslides) (titles only); Hu et al. (2017) (publisher page did not load); Zhao et al. (2017, 2018) and Yi et al. (2025) (publisher fetch error); the 15 cited works without entry.
- Findings with status assumption in at least one part: 11 of 52 (GB-10, GB-12, GB-15, GB-30, GB-35, GB-36, GB-38, GB-40, GB-45, GB-47, GB-50); in none of them is the central statement an assumption, and each assumption is posed as a question.
- Optional checks run: 0 of 6.
- Omitted instances: none.
- Discarded findings: 0 (all 77 findings of the instances had all mandatory fields; none was rejected on rechecking; 42 were merged into 17).
