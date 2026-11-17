# Review report: Energy and structural evolution process of high-altitude and long-runout landslides induced by a strong earthquake

| Field | Value |
|---|---|
| Manuscript | Ge, Y., Hu, B., Tang, H., Fu, X. and Zhu, L. (2025) Energy and structural evolution process of high-altitude and long-runout landslides induced by a strong earthquake. EGUsphere preprint egusphere-2025-4506, https://doi.org/10.5194/egusphere-2025-4506 |
| Checked version | egusphere-2025-4506.pdf, 29 pages, SHA-256 64cb3787456244aa6102e34f776b47e9a612d06e8894d391758ae240dbe415d6 |
| Date | 2026-10-18 |
| Language | English |
| Review instances | Segments 1 to 4, figures, study design; the six review instances ran as separate agents |
| Line numbers | Printed margin numbers of the manuscript (5 to 605, continuous); lines between printed numbers are counted from the nearest printed number; figure pages and table bodies carry no margin numbers and are cited by page and element |

## Summary

The manuscript is a single-case, retrospective numerical back-analysis of the 1786 Mogangling rock landslide on the right bank of the Dadu River (Luding County, Sichuan), triggered by the Kangding (Moxi) earthquake of Ms 7¾. The pre-failure terrain is restored from a UAV-derived DEM by straightening contour lines across the sliding bed and accumulation area. A 3DEC discrete element model (25345 blocks, Mohr-Coulomb blocks and joints, landslide volume 317563 m³ against a reported field volume of about 2400×10⁴ m³) is driven by the 2008 Wenchuan acceleration record of Luding station and run for 131 s. Kinetic, potential and dissipated energy (the latter defined as the residual of mechanical energy, Eq. 4) are computed for the whole mass and for ten monitored blocks; "effective collisions" are detected as velocity peaks above a 30 % prominence threshold (1,139 collisions); and an alpha-shape envelope (α = 1) yields volume swelling and area growth at ten times. Key numbers are a peak velocity of 31.6 m/s at 12 s, a total energy of about 6500 GJ, and a kinetic energy peak of 1116.8 GJ at a volume swelling of 29.47 % and an area growth of 319.5 %, which the authors interpret as the transition from a solid to a fluidized phase.

## Strengths

1. The manuscript discloses its main modelling limits at the point where each method is introduced: structural planes ignored for lack of data (l. 175 to 178), no instrumental record of the 1786 event and use of a proxy record (l. 183 to 191), the smoothness of the restored terrain (l. 160 to 162) and the relative datum of potential energy (l. 253 to 255). A reader can therefore see which parts of the model rest on assumptions before reading the results (PP-18, PP-05).
2. The choice of the prominence threshold for effective collisions is made traceable: Fig. 5b to 5f show the same velocity profile at five thresholds, and the number of marked peaks falls monotonically from 10 % to 50 % (93 to 45 marker patches), so a reader can judge the effect of the 30 % setting on one curve, although the detection itself is not validated against contacts (PP-21, GB-24).
3. The kinematic narrative is consistent across text and figures: the stage maxima 5.9, 19.6, 27.1, 31.6 and 25.7 m/s in the text equal the colour-bar maxima of Fig. 7b to 7f, the run duration of 131 s recurs in the text, Fig. 7, Fig. 8 and Fig. 11, and the ten monitored blocks carry the same identities in Table 2, Fig. 9 and Fig. 10a. This lets a reader follow the stage sequence from figure to figure (PP-28, PP-29, PP-23).
4. Defining dissipated energy as the residual of mechanical energy makes the energy partition computable from kinematic output alone, for the whole mass and for single blocks; the block series in Fig. 9 thereby expose the intervals in which single blocks gain mechanical energy (six rises for block 1 and eleven for block 3), which the text links to rebounds visible in the trajectories, even though the same definition makes the conservation statements an identity (PP-32, GB-29).

## Weaknesses

1. The energy results do not yet carry the conclusions drawn from them: the constant total energy follows from the definition of DE and cannot show conservation for the whole mass or its absence for single blocks (GB-29); the absolute energies in Fig. 8, 9 and 12 cannot be reproduced from any stated volume, density, velocity and datum (GB-28); and the kinetic energy peak used for the solid to fluid transition is the largest sampled value in Fig. 12, not the peak of the series in Fig. 8 (GB-43). The authors should state the mass and datum behind each energy series, compute dissipation, seismic input and boundary work independently from the model output, and recompute the transition values on the full time series.
2. Whether the model represents the Mogangling event is open: the reported dimensions and volume are inconsistent with each other, with the geological map and with the modelled mass of 317563 m³ (GB-16); the terrain restoration that fixes the initial mass is neither fully described nor checked (GB-14); the proxy ground motion is given without amplitude, duration, scaling or sensitivity (GB-23); and the agreement with the field is shown only qualitatively (GB-38). The authors should give one consistent geometry, check the restoration by a mass balance, test at least two further input levels, and compare simulated and mapped deposits quantitatively.
3. Several mechanistic conclusions rest on analyses that are not shown: the comparison of collisions, energy received and travel distance between parts of the mass (GB-40), the detection of collisions from velocity peaks without a check against contacts (GB-24), fragmentation and a phase transition read from envelope growth (GB-42), and structural-plane control in a model that ignores structural planes (GB-36); a study that anticipates the energy transfer mechanism is not discussed (GB-06). The authors should report normalised per-block results, validate the collision detection, define a phase criterion and mark the provenance of each mechanism, or present these statements as hypotheses.
4. Several moderate findings limit reproducibility and positioning: the population behind the 1,139 collisions and the threshold reference are undefined (GB-26), the envelope analysis lacks its reference volumes, α unit and time base (GB-33), numerical settings and the equilibrium check are missing (GB-21, GB-31), data and code are available only on request without provenance of external inputs (GB-13, GB-45), half of the in-text citations have no reference list entry (GB-46), and the gap statements are not delimited against existing work (GB-05). The authors should add a table of numerical settings, define all counts and reference quantities, deposit inputs and scripts in a public repository, complete the reference list and delimit the contribution against the studies already in it.

## Findings by segment

### Segment 1: Abstract, introduction, state of research (p. 1 to 2)

#### Substantive findings

**GB-01 The two sources cited for a rising frequency of earthquake-induced rock landslide chains do not state such a trend.**

| Field | Content |
|---|---|
| Check | P13 |
| Location | p. 1, l. 33 to 34 |
| Quotation | "In recent years, the chain disasters of high-level rock landslides in high-intensity earthquake areas have shown a trend of frequent occurrence (Carpignano et al., 2009; Fan et al., 2019a)" |
| Concern | The sentence opens the motivation and attributes a temporal trend to two sources. Carpignano et al. (2009, J. Risk Res., 12, 513 to 534, https://doi.org/10.1080/13669870903050269) is a methodological paper on regional multi-risk maps for the Piedmont Region, Italy; its abstract mentions neither earthquakes, rock landslides nor hazard chains. The abstract of Fan et al. (2019, Rev. Geophys., 57, 421 to 503, https://doi.org/10.1029/2018RG000626) describes earthquake-induced hazard chains and their long after-effects after single events (Chi-Chi 1999, Wenchuan 2008), but no increasing frequency. The label "2019a" has no counterpart, since the two "Fan et al. 2019" entries carry no letters (KK-05). |
| Suggestion | In l. 33 to 34 either cite a source that reports a frequency trend, with its period and region, or reword the sentence without a trend, for example "Earthquake-induced chains of rock landslide hazards are a recurrent threat in high-intensity seismic areas (Fan et al., 2019a)", and remove Carpignano et al. (2009) from it. |
| Status | verified (subject of Carpignano et al. 2009 from its abstract); inferred (absence of a trend statement in the full texts, only abstracts were readable) |
| Severity | moderate |
| Source | S1 |

**GB-02 The claim that pre-failure terrain restoration is rarely studied and that contour restoration is a "new idea" rests on no documented search, and an established, tested reconstruction method (SLBL) is not cited.**

| Field | Content |
|---|---|
| Check | P28, P14 |
| Location | p. 2, l. 42 and l. 49 to 51; p. 1, l. 16 to 17 (Abstract); p. 25, l. 463 to 468 (Conclusion 1) |
| Quotation | "At present, in terms of surface terrain restoration, the terrain restoration before a landslide is less." (l. 42); "This paper uses the method of restoring the continuity of contour lines to establish the terrain data before a landslide, which can provide a new idea of terrain restoration before a landslide for the same type of research." |
| Concern | The Abstract and Conclusion 1 present the contour-continuity restoration as one of the two contributions. The gap and novelty sentences name no database, search terms, period or date, and the paragraph cites no work on reconstructing pre-failure topography; the works in l. 45 to 49 concern mapping or simulation. Jaboyedoff, M., Chigira, M., Arai, N., Derron, M.-H., Rudaz, B. and Tsou, C.-Y. (2019) 'Testing a failure surface prediction and deposit reconstruction method for a landslide cluster that occurred during Typhoon Talas (Japan)', Earth Surface Dynamics, 7, pp. 439 to 458, https://doi.org/10.5194/esurf-7-439-2019 (open access), test the sloping local base level (SLBL) method for reconstructing palaeotopography, failure surfaces and eroded deposits from DEMs on 70 deep-seated landslides with pre- and post-event lidar DEMs; most reconstructed volumes fall within about 35 % of independent estimates, and the results are sensitive to the chosen parameters. The work is not in the reference list. It anticipates the task and shows how such a reconstruction can be validated and its uncertainty stated, whereas the manuscript only states that the restored terrain "can be regarded as the terrain before the landslide" (l. 162). Graded major because, if the finding holds, the novelty of one of the two stated contributions changes. |
| Suggestion | In l. 42 to 51 replace the gap and novelty claims by a short review of existing pre-failure topography reconstruction methods (SLBL, surface interpolation, DEM differencing), cite Jaboyedoff et al. (2019), state what the contour-continuity approach adds, and either report the search (databases, terms, period, date) or drop "new idea"; adjust the Abstract (l. 16 to 17) and Conclusion 1 accordingly. |
| Status | verified (absence of search details and of the work in the reference list; content of Jaboyedoff et al. 2019 read on the publisher page by instance S1; a second reading during merging was refused by the server) |
| Severity | major |
| Source | S1 |

**GB-03 Two of the works cited for field, photo, UAV and GIS mapping of landslides are numerical simulation studies, and two further citations of the same sentence are not in the reference list.**

| Field | Content |
|---|---|
| Check | P13 |
| Location | p. 2, l. 43 to 46 |
| Quotation | "the key information of landslide characteristics is often obtained through photos, field surveys, optical remote sensing images and UAV impact, so as to further build geomorphic maps through GIS (Geographic Information System) for subsequent analysis (Zhang et al., 2024; Song at al.2017; Fan et al., 2020; Wu et al., 2024)." |
| Concern | Song et al. (2017, https://doi.org/10.1007/978-3-319-53483-1_36) is titled "Landslide Deformation Prediction by Numerical Simulation in the Three Gorges, China", with indexed keywords on 3D numerical simulation, strength reduction and GPS monitoring. Wu et al. (2024, Eng. Geol., 331, 107429) is titled "Numerical simulation on potential landslide-induced wave hazards by a novel hybrid method", with keywords on the material point method and SPH. Neither appears to concern mapping from photos, field surveys, optical imagery, UAV data or GIS. "Zhang et al., 2024" and "Fan et al., 2020" have no entry in the reference list (see GB-46), so none of the four citations can be confirmed as support. |
| Suggestion | In l. 46 replace the four citations by works that document field, photo, UAV or GIS mapping of landslides, and add every cited work to the reference list. |
| Status | inferred (only titles and indexed keywords of Song et al. 2017 and Wu et al. 2024 were readable); verified (Zhang et al. 2024 and Fan et al. 2020 missing from the reference list) |
| Severity | moderate |
| Source | S1 |

**GB-04 The ranking "a two-dimensional simulation is more often used" is supported only by three examples, and the one readable example does not concern terrain restoration or external stress input.**

| Field | Content |
|---|---|
| Check | P13 |
| Location | p. 2, l. 46 to 49 |
| Quotation | "For most numerical simulations involving terrain restoration, a two-dimensional simulation is more often used. The simplified model is adopted to simulate the overall process of landslide by inputting external stress (Du et al., 2021; Cheng 2014; Li et al., 2024)." |
| Concern | "For most" and "more often" are a ranking that needs a count of studies; the manuscript gives three citations and no count. The abstract of Li et al. (2024, Front. Earth Sci., 12, 1466751) describes the rainfall-triggered reactivation of the ancient Zhongbao landslide, studied by field investigation, drilling and numerical simulation of seepage and stability; it names neither a two-dimensional model, nor a restoration of pre-failure terrain, nor an external stress input. For Du et al. (2021) the indexed record names the discrete element method but not the dimensionality; Cheng (2014) could not be read. The sentence is the basis for presenting the 3D model with restored terrain as an advance. |
| Suggestion | In l. 46 to 49 either support the ranking with a count of studies and its basis, or describe the cited cases, stating for each whether it is 2D or 3D and whether pre-failure terrain was restored; replace Li et al. (2024) if it does not involve terrain restoration. |
| Status | verified (no count given); inferred (content of Li et al. 2024 from its abstract and of Du et al. 2021 from metadata); Cheng (2014) not read |
| Severity | moderate |
| Source | S1 |

**GB-05 The gap statement on energy evolution rests on no documented search and is not delimited against the studies of the same landslide and the earlier energy-evolution study of the first and third authors, which are in the reference list but never cited.**

| Field | Content |
|---|---|
| Check | P28, P10 |
| Location | p. 2, l. 60 to 64; p. 27, l. 540 to 542 (Ge et al., 2021); p. 26, l. 514 to 516 (Chang et al., 2022); p. 28, l. 588 to 590 (Wu et al., 2013); p. 29, l. 600 to 602 (Zhao et al., 2021); p. 29, l. 603 to 605 (Zhou et al., 2024); p. 2, l. 71 to 73 |
| Quotation | "However, they still lack a quantitative and systematic study of this topic, especially on energy evolution during the collision." |
| Concern | This is the gap on which the energy part of the study rests. No database, search terms, period or date are given, and none of the five works cited in the preceding sentence (l. 62 to 63) is in the reference list (GB-46), so "they" cannot be traced. The reference list contains Ge, Tang and Li (2021) "Mechanical energy evolution in the propagation of rock avalanches using field survey and numerical simulation" by the first and third authors, Chang et al. (2022) "Dynamic process analysis of the Xinmo landslide via seismic signal and numerical simulation", Wu et al. (2013) "Genetic Mechanism and Failure Process of the Mogangling Seismic Landslide" and Zhou et al. (2024) on earthquake-triggered landslides in Moxi Town; none is cited in the text, and Zhao et al. (2021) on the Mogangling landslide appears at most as "Zhao et al., 2020" (l. 57, KK-16). Their titles show that energy evolution in rock avalanches and the failure process of Mogangling have been studied before; what this study adds is not stated. A further counterexample outside the list is discussed in GB-06. The aim of supporting "early warning and risk mitigation" (l. 72 to 73) has no matching question or result. |
| Suggestion | In l. 52 to 73 summarise what these studies found, delimit the gap against them (for example the effective-collision detection or the coupling with envelope volume and area), formulate explicit research questions matched to the gaps, and either report the search or remove the claim that such studies are lacking. |
| Status | verified (absence of search details; listing and absence of in-text citations, checked by Python); inferred (content of the listed studies beyond their titles; Ge et al. 2021 was not readable online) |
| Severity | moderate |
| Source | S1, SD |

**GB-06 A study that quantifies rear-to-front energy transfer by collision and by fragmentation in sliding rock masses is not cited; it anticipates the central energy-transfer statement and finds fragmentation the more efficient mechanism.**

| Field | Content |
|---|---|
| Check | P14 |
| Location | p. 2, l. 63 to 64; p. 1, l. 28 to 30 (Abstract); p. 26, l. 483 to 487 (Conclusion 4) |
| Quotation | "When the rear rock mass collides with the front, its dissipated energy sharply increases and transfers energy to the front rock mass, enabling the front portion to slide farther." |
| Concern | Lin, Q., Wang, Y., Xie, Y., Cheng, Q. and Deng, K. (2022) 'Multiscale effects caused by the fracturing and fragmentation of rock blocks during rock mass movement: implications for rock avalanche propagation', Natural Hazards and Earth System Sciences, 22, pp. 639 to 657, https://doi.org/10.5194/nhess-22-639-2022 (open access), simulate a jointed rock block sliding down a slope and track kinetic, strain and dissipated energy of front and rear sub-blocks. Their abstract states that "The energy transfer induced by fragmentation is more efficient than that induced by collision"; in their Sect. 4.2 the horizontal velocity of the front sub-block rises by 12.56 % with fragmentation against 3.72 % with collision only. This anticipates the mechanism of Conclusion 4 and questions attributing the transfer to "effective collisions" alone. The work is not in the reference list. Graded major because it concerns the interpretation of a stated result. |
| Suggestion | Cite Lin et al. (2022) next to l. 63 to 64 and discuss in Sect. 3.2.2 and Conclusion 4 whether the rear-to-front transfer in the 3DEC model stems from collisions or from separation of blocks along the internal structural plane (l. 179 to 180), and how the effective-collision count separates the two. |
| Status | verified (content read on the publisher page by instance S1 and again during merging; absence from the reference list) |
| Severity | major |
| Source | S1 |

**GB-07 A 3DEC study of an earthquake-related rockslide shows that fracture density controls block kinematics; it limits the generality of results obtained with a uniform block grid and no structural planes, and it is not cited.**

| Field | Content |
|---|---|
| Check | P14 |
| Location | p. 2, l. 65 to 67; p. 9, l. 175 to 180 |
| Quotation | "Because the occurrence distribution data of the structural plane of the landslide mass before the landslide can not be obtained, the impact of the structural plane on the landslide process has to be ignored in this study. The landslide mass is evenly divided into 8.7 m×8.7 m blocks on the xoy surface." |
| Concern | The manuscript discloses that structural planes are ignored and replaced by a uniform 8.7 m block grid. Liu, B., Zhang, Y., Hu, X., Li, J., Yuan, K., He, K., Cui, J. and Yin, Z. (2025) 'Kinetic characteristics investigation of the Yingxingping rockslide based on discrete element method combined with discrete fracture network', Natural Hazards and Earth System Sciences, 25, pp. 4247 to 4262, https://doi.org/10.5194/nhess-25-4247-2025 (open access), model a post-earthquake rockslide in Wenchuan with 3DEC and a discrete fracture network and test how fracture density and friction angle change the motion. Since collision counts and block energies depend on block size and joint layout, this restricts how far the 1,139 effective collisions (l. 233) and the energy transfer pattern can be generalised; the consequence of the disclosed limitation is not drawn. Not in the reference list. |
| Suggestion | Cite Liu et al. (2025) in the introduction and in Sect. 2.1 (l. 175 to 180), and add a sensitivity test of block size or joint spacing on the number of effective collisions and the block energy curves, or state the dependence as a limitation in the conclusions. |
| Status | verified (content read on the publisher page by instance S1; absence from the reference list) |
| Severity | moderate |
| Source | S1 |

#### Minor corrections

| ID | Location | Quotation | Replacement | Source |
|---|---|---|---|---|
| KK-01 | p. 1, l. 13 | "Chengdu, 610041 ,China" | "Chengdu, 610041, China" | S4 |
| KK-02 | p. 1, l. 21; p. 3, l. 84 | "kinetic energy, and dissipation energy" (l. 21); "kinetic energy and dissipation energy" (l. 84) | "kinetic energy, and dissipated energy"; "kinetic energy and dissipated energy" (term used in l. 242 and Sect. 2.3) | S1, S2 |
| KK-03 | p. 1, l. 32 | "Landslide is a common and widespread geological disaster, which causes great loss of life and property." | "Landslides are common and widespread geological hazards that cause great loss of life and property." | S4 |
| KK-04 | p. 1, l. 33; p. 2, l. 39 and 40 | "high-level rock landslides"; "high-level rock landslide" | "high-altitude rock landslides"; "high-altitude rock landslide" (as in the title and l. 73) | S4 |
| KK-05 | p. 1, l. 34; p. 2, l. 56 to 57; p. 27, l. 530 to 536 | "Fan et al., 2019a"; "Fan et al., 2019"; two entries "Fan, X., Scaringi, G., Korup, O., et al." and "Fan, X., Yang, F., ..." both dated 2019 | "2019a" in the entry Fan, Scaringi et al. and "2019b" in the entry Fan, Yang et al.; in l. 56 to 57 "2019a" or "2019b", whichever is meant | S4 |
| KK-06 | p. 1, l. 34 to 35 | "such as donghekou landslide debris flow dammed lake" | "such as the Donghekou landslide, debris flow and dammed lake" | S1, S4 |
| KK-07 | p. 1, l. 36 | "Wang, 2021" | "Wang et al., 2021" (the entry has seven authors) | S1, S4 |
| KK-08 | p. 1, l. 37; p. 28, l. 575 to 577 | "Tian et al., 2017"; entry ending "2016." | the same year in citation and entry | S4 |
| KK-09 | p. 1, l. 37 | "which has seriously affected people's lives" | "which have seriously affected people's lives" | S4 |
| KK-10 | p. 1, l. 38 to p. 2, l. 39 | "the Mogangling landslide that occurred in 1786 was repaired and reconstructed" | "the Mogangling landslide that occurred in 1786 was reconstructed" | S4 |
| KK-11 | p. 2, l. 42 | "At present, in terms of surface terrain restoration, the terrain restoration before a landslide is less." | "At present, few studies have restored the terrain before a landslide." (if the claim is kept, see GB-02) | S4 |
| KK-12 | p. 2, l. 43 | "For landslides that have not occurred too far away" | "For recent landslides" | S1, S4 |
| KK-13 | p. 2, l. 44 | "UAV impact" | "UAV imagery" | S1, S4 |
| KK-14 | p. 2, l. 46 | "Song at al.2017" | "Song et al., 2017" | S1, S4 |
| KK-15 | p. 2, l. 48 to 49; p. 27, l. 521 | "Cheng 2014" | a citation matching the two-author entry, for example "Cheng and Yu-Sheng, 2014"; please also check the order of given and family name in "Yu-Sheng, L." in the entry | S4 |
| KK-16 | p. 2, l. 57; p. 29, l. 600 to 602 | "Zhao et al., 2020"; entry ending "2021." | the same year in citation and entry | S4 |

#### Verification log

| ID | Check | Checked | Values | Result |
|---|---|---|---|---|
| PP-01 | P14 | Contribution in one sentence and search for prior work that anticipates it | Contribution: contour-continuity restoration of the 1786 Mogangling terrain, 3DEC simulation with a Wenchuan record, energies of the whole mass and ten blocks, effective collisions from velocity peaks, alpha-shape envelope volume and area against energy. Six queries (Mogangling simulation; pre-failure topography SLBL; rock avalanche energy fragmentation collision; alpha-shape envelope of deposits; 3DEC energy evolution). Candidates already in the reference list (Zhao 2021, Zhou 2024, Ge 2021, Chang 2022) were not proposed; Zhou X. et al. 2021 (Taihongcun, PFC2D) same field without energy quantification; no work on alpha-shape envelopes of deposits found | three proposals (GB-02, GB-06, GB-07), otherwise no finding |
| PP-02 | P28 | All gap and novelty sentences in title, abstract and introduction | Found in l. 42, l. 49 to 51 (GB-02) and l. 63 to 64 (GB-05). Not gap claims: l. 60 to 61 "direct observation data are rarely available" (data) and l. 15 to 16 "It is often difficult to restore the evolution process" (difficulty). No "first" or "for the first time". Search details: none anywhere | two findings, otherwise no finding |
| PP-03 | P13 | All sentences citing works by author and year | 29 in-text citations, all in l. 34 to 63, none elsewhere; 12 of 29 match an entry by first author and year, 17 do not (15 without entry, 2 with a different year), 17 / 29 = 58.6 %. Tian et al. (Geocarto Int., 32, 978 to 989): abstract reports 284 pre-earthquake and 1,053 coseismic landslides of the 2014 Ludian earthquake, which fits l. 36 to 37; Fan et al. (2019, Rev. Geophys.) supports the existence of earthquake-induced hazard chains | no finding beyond GB-01, GB-03, GB-04 and GB-46 |
| PP-04 | P13, P14, P28 | Readability of the sources used | Not readable or refused: doi 10.3389/feart.2024.1466751 and 10.1007/s11629-020-6617-y (HTTP 429, OpenAlex records read instead); Ge et al. 2021 (publisher page blocked, Crossref and OpenAlex without abstract); Hu et al. 2017 (HTTP 429); Cheng 2014 (not opened). Statements on these sources carry status inferred | limits recorded |
| PP-05 | Design sketch | Questions, gaps, study type, comparison, data sources, environment, disclosed limits | No explicit research questions or hypotheses (aims l. 65 to 73); type single-case retrospective 3DEC back-analysis; no comparison condition, one parameter set, one input motion, parameter variation only for the collision threshold (10 to 50 %); data sources UAV DEM (date and resolution not stated), restored contours, geological map, laboratory tests and inversion (not attributed per value), Luding record of 2008, 3DEC output, field photographs, Tiezhuang Temple tablet; 3DEC version, damping, time step not stated; disclosed limits: structural planes ignored (l. 175 to 178), proxy input (l. 183 to 191), smooth restored terrain (l. 160 to 162), PE datum (l. 253 to 255), dam break not modelled (l. 348 to 350), weathering since 1786 (l. 354 to 355) | basis for GB-14, GB-21, GB-23, GB-24, GB-36, GB-40, GB-42 |

### Segment 2: Material, methods (p. 2 to 15)

#### Substantive findings

**GB-08 The text announces three parts of the method and then lists four, and Fig. 1 shows four stages.**

| Field | Content |
|---|---|
| Check | P3, P4 |
| Location | p. 2, l. 76 to p. 3, l. 77; p. 3, l. 77 to 90; Fig. 1 (p. 4) |
| Quotation | "As shown in Fig1., the research method involves three parts" |
| Concern | Fig. 1 has four stage boxes (Geo-mechanical Model Building; Analysis of Landslide Evolution Process; Analysis of Energy Evolution During Block Motion; Extraction of volume and area of landslide accumulation area), and l. 77 to 90 enumerate (1) to (4). |
| Suggestion | Replace "three parts" by "four parts" in l. 77. |
| Status | verified (page image p. 4 and text) |
| Severity | minor |
| Source | AB, S4 |

**GB-09 Symbols and abbreviations in Fig. 1, 2c, 3b, 4 and 7 are not explained in legend or caption, and Fig. 1 uses an energy notation that differs from Eq. (1) to (4).**

| Field | Content |
|---|---|
| Check | P29 |
| Location | Fig. 1, panel "Global Perspective" (p. 4); Fig. 2c (p. 6); Fig. 3b (p. 8); Fig. 4 (p. 10); Fig. 7a, 7h and 7o (p. 17 to 19) |
| Quotation | "Fig4. Discrete numerical model with fine topography" |
| Concern | Fig. 1 uses "P0E", "PtE", "KtE" instead of PE(t0), PE(ti), KE(ti) of Eq. (1) to (4). Fig. 2c shows the section line a to a', dip symbols "60°" and "80°", blue flow arrows and contour labels (1125 to 1825) without unit or interval, none in the legend; Fig. 3b shows an "80°" dip symbol without explanation. Fig. 4 uses γo2, Qdel, γM2 without resolving them (see GB-10) and tp, tPGA, tf, te, which appear nowhere in text or caption. Fig. 7o states neither the simulation time, the viewing direction, a scale, nor source and date of the two photographs. Fig. 7a (0 to 0 m/s) and Fig. 7h (0 to 0 MPa) colour the whole model in the end colour of the scale, which a reader takes for the maximum. |
| Suggestion | Replace "P0E", "PtE", "KtE" in Fig. 1 by "PE(t0)", "PE(t)", "KE(t)"; add the missing symbols to the legends of Fig. 2c and 3b; define tp, tPGA, tf, te in the caption of Fig. 4; complete the caption of Fig. 7o; render the t = 0 panels of Fig. 7 in the colour for zero. |
| Status | verified (page images p. 4, 6, 8, 10, 17 to 19) |
| Severity | minor |
| Source | AB |

**GB-10 Lithological units carry different names and symbols in the text, Fig. 2c, 3a, 3b, 4 and Table 1, so the material parameters cannot be assigned to the modelled units.**

| Field | Content |
|---|---|
| Check | P38, P3 |
| Location | p. 5, l. 101 to 105; Fig. 2c legend (p. 6); Fig. 3a and 3b legends (p. 8); p. 9, l. 180 to 181; Fig. 4 legend (p. 10); p. 11, l. 207 to 209 and Table 1, rows "bed rock", "landslide mass" |
| Quotation | "The sand slate of the Triassic Baiguowan formation (T3bg) is exposed on the left bank of the Dadu River." |
| Concern | The map, block view, profile and model view together give a good picture of the setting, but the units do not match. Text: plagioclase granite γO2, quartz diorite O2, sand slate T3bg on the left bank, Q4del, Q4col+dl, Q4al. Fig. 2c: Plagiogranite γo2, Hybrid granite γM2 (on the left bank), Massive gravel Q4col+dl, Sand and pebble gravel Q4al, Rubble soil Q4del; no diorite, no T3bg. Fig. 3a: Granite, Diorite, Massive gravelly soils, Sand and pebble gravel; Fig. 3b adds Massive gravel, so "Massive gravel" and "Massive gravelly soils" appear side by side as different units. Fig. 4: γo2, Qdel, γM2, Sliding mass. Table 1: only "bed rock" and "landslide mass". γM2 is not mentioned in the text; weathering is "strongly to weakly" in l. 101 and "strongly weathered and moderately weathered zones" in l. 208 to 209. A reader cannot tell which Table 1 set was assigned to γo2, Qdel and γM2. Graded moderate because the assignment of material parameters cannot be reproduced. |
| Suggestion | Use one name and one symbol per unit in l. 101 to 105, l. 208 to 209 and the legends of Fig. 2c, 3a, 3b and 4; add to Table 1 a column "model unit (Fig. 4)"; state in l. 103 to 104 whether T3bg and γM2 are the same unit, or map T3bg. |
| Status | verified (legend entries and symbols on page images p. 5, 6, 8, 10, 11); inferred (correspondence of "Massive gravelly soils" to Q4del from its position); assumption (whether T3bg and γM2 denote the same rock, posed as question) |
| Severity | moderate |
| Source | S2, AB |

**GB-11 In Fig. 2a the landslide marker lies about 1° of longitude (about 93 km) west of the coordinates in the text, and the scale bar is about 30 % too long.**

| Field | Content |
|---|---|
| Check | P3 |
| Location | Fig. 2a, marker "Mogangling landslide" and scale bar (p. 6); p. 5, l. 95 to 96 |
| Quotation | "The coordinates of the landslide center are: 29 ° 37 ′ 30.726 ″ north latitude, 102 ° 09 ′ 41.190 ″ east longitude." |
| Concern | Graticule ticks of Fig. 2a (300 dpi): 100°E at 728.5 px, 102°E at 884.5, 104°E at 1039.5, 106°E at 1195.5 px; 31°N at 867.5, 29°N at 1023.0, 27°N at 1181.5 px. The marker centre at 821.7, 980.5 px gives 101.20 ± 0.02°E, 29.57 ± 0.02°N, against 102.161°E, 29.625°N in the text: 0.96° × 111.3 km × cos 29.6° = 93 km. The scale bar spans 147 px for 160 km; one degree of latitude (111 km) spans 78.5 px, so 160 km should span 113 px. |
| Suggestion | Re-plot the marker at the coordinates of l. 95 to 96 and correct the scale bar of Fig. 2a. |
| Status | verified (measured against the graticule of the same panel) |
| Severity | minor |
| Source | AB |

**GB-12 Do the grid lines in Fig. 2b mark 29°37'00" N and 102°09'00" E? The star sits on their crossing, whereas the text places the centre 30.7" further north and 41.2" further east.**

| Field | Content |
|---|---|
| Check | P3 |
| Location | Fig. 2b, grid labels "29°37'N", "102°09'E" and star "Study area" (p. 6); p. 5, l. 95 to 96 |
| Quotation | "29 ° 37 ′ 30.726 ″ north latitude, 102 ° 09 ′ 41.190 ″ east longitude" |
| Concern | If the grid labels are exact, the text coordinates lie 30.7" × 30.9 m = 948 m north and 41.2" × 26.9 m = 1107 m east of the star; with the scale bar of Fig. 2b (600 m in about 107 px) that point lies in or beyond the Dadu River channel, not on the landslide. If the labels are rounded, the figure does not show the precision. |
| Suggestion | Label the grid lines in Fig. 2b with seconds, or place the star at the coordinates of l. 95 to 96. |
| Status | verified (star position and labels at the page image); inferred (offset); assumption (whether the labels are rounded, posed as question) |
| Severity | minor |
| Source | AB |

**GB-13 The data availability statement names no source for the external inputs (strong-motion record, UAV DEM, remote sensing image, geological map, historical record, laboratory tests, field photographs).**

| Field | Content |
|---|---|
| Check | P12 |
| Location | p. 6, l. 130 to 131 and l. 136 to 137; Fig. 2b and 2c (p. 6); p. 9, l. 180; p. 10, l. 189 to 191; p. 11, l. 206 to 207; Fig. 7o (p. 19); p. 26, l. 505 to 506 |
| Quotation | "this study adopts the acceleration records measured at the Luding station during the Wenchuan earthquake as the input ground motion" (l. 189 to 190); "The data and materials that support the findings of this study are available from the first author, Yunfeng Ge, upon reasonable request." |
| Concern | The methods name the inputs openly, including their limits (no record of 1786, l. 184 to 186; no data on structural planes, l. 175 to 178). Neither the statement nor the methods give provenance for: the Luding strong-motion record (operator, record identifier, component, sampling, scaling); the UAV DEM (date, resolution, who acquired it); the image of Fig. 2b (sensor, date); the map of Fig. 2c, called "geological engineering drawing" in l. 180 (author or agency); the Tiezhuang Temple tablet (no citation, transcription or translation); the laboratory tests of l. 207 (no results, no reference); the photographs of Fig. 7o. The statement treats all data as authors' data. The Wenchuan main-shock records belong to the national strong-motion network, which recorded more than 1,400 acceleration components at 460 permanent stations (Li et al., 2008, abstract); whether such records may be passed on by the authors is not stated. |
| Suggestion | Extend the statement in l. 505 to 506 by one line per external source with provider and access route, and give in l. 189 to 191 network, station code and component of the record with a reference, for example Li, X., Zhou, Z., Yu, H., Wen, R., Lu, D., Huang, M., Zhou, Y. and Cu, J. (2008) 'Strong motion observations and recordings from the great Wenchuan Earthquake', Earthquake Engineering and Engineering Vibration, 7(3), pp. 235 to 246, https://doi.org/10.1007/s11803-008-0892-x (not in the reference list); cite the sources of Fig. 2b, 2c and the tablet record, and report or cite the laboratory results of l. 207. |
| Status | verified (absence of provenance in text and captions); inferred (content of Li et al. 2008 from its abstract page, full text not read); assumption (redistribution rights of the record, posed as question) |
| Severity | moderate |
| Source | S2 |

**GB-14 The contour-based terrain restoration, which fixes the initial mass and thus all energy values, is neither fully described nor checked, and Conclusion 1 states two rules that the method section does not apply.**

| Field | Content |
|---|---|
| Check | P10, P8, P17, P27, P15 |
| Location | p. 6, l. 135 to 140; p. 7, l. 141 to 143 and l. 157 to 162; Fig. 1, upper block (p. 4); Fig. 3c (p. 9); p. 25, l. 463 to 468 (Conclusion 1); p. 2, l. 49 to 51 |
| Quotation | "the contour lines corresponding to the sliding bed and accumulation area are modified to be straight" (l. 139 to 140); "(a) Outside the landslide boundaries, there exist contour lines consistent with the continuity of the mountain range, and their trajectory equations can be extracted as a basis for restoring the contours" |
| Concern | The Introduction offers the method as "a new idea of terrain restoration" for similar studies (l. 50 to 51), and the restored surface fixes the initial mass and therefore every energy value. The only check is visual: the restored terrain "is smooth and the surface does not fluctuate" but "can be regarded as the terrain before the landslide" (l. 160 to 162). Sect. 2.1 leaves open how contours are "modified to be straight" (rule, extent, which contours), how the present deposit was removed (Fig. 1 names "Deposit Removal", the text does not describe it), and which software performed noise reduction, cavity repair and normal correction. Conclusion 1 adds two rules, trajectory equations of contours and reference to "other mountain areas within the same stratigraphic unit" (l. 465 to 468), that are neither in Sect. 2.1 nor applied: no trajectory equation is reported, and the accumulation area was restored by the same straightening (l. 139 to 140). Question to the authors: was the deposit-free valley floor below the present deposit available when the model was built, or does the model run over the present deposit surface? |
| Suggestion | In Sect. 2.1 (l. 135 to 162) state the straightening rule, the deposit removal, the trajectory equations and the use of reference slopes, and name the software; check the restoration by a mass balance (volume between restored and present surface in the source area against the volume of the present deposit above the restored valley floor, with a stated bulking factor); add the profile along a-a' with both surfaces and their difference in metres. Otherwise reformulate Conclusion 1 (l. 463 to 468) as a recommendation for future work. |
| Status | verified (absence of a quantitative check and of the two rules in Sect. 2.1); inferred (role of the restored surface for all energies); assumption (model run over the present deposit surface, posed as question) |
| Severity | major |
| Source | SD, S4 |

**GB-15 Fig. 3a shows two zones, while the text says Fig. 3a divides the area into four parts.**

| Field | Content |
|---|---|
| Check | P3 |
| Location | p. 7, l. 144 to 146; Fig. 3a, legend items "I Sliding bed", "II Accumulation area" (p. 8) |
| Quotation | "As shown in Fig3.(a), the geometric model of the terrain surface is established according to DEM. The whole landslide occurrence area can be divided into four parts: the rock wall area, colluvial slope area, slope debris flow area, and main accumulation area." |
| Concern | The block diagram marks two zones separated by a dotted red line; the four parts named in the text are not delineated. |
| Suggestion | Mark the four parts in Fig. 3a, or refer in l. 144 to 146 to the two zones shown. |
| Status | verified (page image p. 8) |
| Severity | minor |
| Source | AB |

**GB-16 Length, area, thickness and volume of the Mogangling landslide are inconsistent with each other, with Fig. 2c, with the modelled landslide volume of 317563 m³ and with the listed study of the same event.**

| Field | Content |
|---|---|
| Check | P2, P1, P9, P13, P3 |
| Location | p. 7, l. 149 to 151; p. 9, l. 173 to 174 and l. 181 to 182; p. 13, Table 2, column "Volume (m3)"; Fig. 2c (p. 6); p. 5, l. 110 to 112 |
| Quotation | "about 450 m long, about 1000 m wide along the river, and a planar area of 0.45 km2. The average thickness of the landslide mass is about 100 m, and the volume is about 2400×104 m3" (l. 149 to 151); "the volume of the landslide is 317563 m3" |
| Concern | Length times width gives the stated area (450 m × 1000 m = 0.45 km²). Beyond that the figures disagree. (1) 0.45 km² × 100 m = 4.5×10⁷ m³, not 2.4×10⁷ m³ (factor 1.875); the stated volume implies a mean thickness of 53.3 m. (2) The modelled volume 317563 m³ is 1.32 % of 2.4×10⁷ m³ (factor 75.6) and corresponds to a mean thickness of 0.71 m over 0.45 km²; the Table 2 block volumes (756.2 to 1754.3 m³, mean 1151.3 m³) correspond to column heights of 10.0 to 23.2 m on 8.7 m × 8.7 m columns, and 317563 m³ would be only about 276 such blocks, whereas 0.45 km² holds about 5945 columns. (3) The length of 450 m contrasts with the model length of 1021 m in the sliding direction (l. 174) and with the slope geometry of l. 151 to 156, whose bands add up to a horizontal extent of 914 to 1250 m. (4) On the map of Fig. 2c (scale bar 2.194 m/px, ±1.5 %) the landslide boundary measures 1389 ± 21 m by 963 ± 15 m and encloses 0.974 km², while the deposit unit Q4del measures 0.476 km² (845 m by 921 m), close to 0.45 km²; l. 149 to 150 may describe the deposit. (5) Zhao et al. (2021), in the reference list, give in their abstract the same length and width but a volume of about 4500×10⁴ m³, equal to area times thickness, and more than 100 000 deaths, against "tens of thousands of people drowned" (l. 111 to 112); the manuscript gives no source for these numbers. Possible resolutions: the printed "2400×104" read literally as 249600 m³, which contradicts area times thickness; different objects (source, deposit, modelled subset), which the text does not state; or a typing error in l. 182. This matters for the results because V0 in Eq. (5) and all energies scale with the modelled mass (GB-28), and the validation refers to the same event (GB-38). |
| Suggestion | In Sect. 2.1 (l. 149 to 151) state length, width, area, thickness and volume for one defined object (source area or deposit), consistent with Fig. 2c, l. 174 and the cited literature; in l. 182 give total volume, mass and number of the landslide blocks in the model and explain any difference from the field volume; cite the source of the event data in l. 110 to 112. |
| Status | verified (quoted values on page images p. 7 and 9; Fig. 2c dimensions measured; values in the abstract of Zhao et al. 2021); inferred (products, ratios, implied thicknesses; reference of l. 149 to 150 to the deposit) |
| Severity | major |
| Source | S1, S3, AB, SD |

**GB-17 The text refers to a section b-b' in Fig. 2c and to section results in Fig. 3c; neither exists there.**

| Field | Content |
|---|---|
| Check | P4, P3 |
| Location | p. 7, l. 159 to 160; Fig. 2c (p. 6); Fig. 3b and 3c (p. 8 to 9) |
| Quotation | "As shown in Fig3. (b), make a section along a-a'and b-b' in Fig2. (c). The results are shown in Fig3. (c)." |
| Concern | Fig. 2c shows one section line, a to a'; no "b" appears. Fig. 3b is the only profile, titled "(a-a')"; Fig. 3c shows contour maps and shaded surfaces before and after restoration, not sections. The measured length of a to a' (1510 m) and its azimuth (74.1°) agree with Fig. 3b (0 to 1500 m) and the sliding direction of 75° (PP-13). The sentence also lacks a space in "a-a'and". |
| Suggestion | In l. 159 to 160 either add section b-b' to Fig. 2c and its profile to Fig. 3b, or delete "and b-b'"; change "The results are shown in Fig3. (c)" to "The profile is shown in Fig. 3b, and the plan-view comparison of the terrain before and after restoration in Fig. 3c." |
| Status | verified (page images p. 6, 8, 9) |
| Severity | minor |
| Source | S4, AB |

**GB-18 In Fig. 3a two legend colours are indistinguishable by measurement, a grey layer has no legend entry, and the scale bar is drawn on an oblique perspective view.**

| Field | Content |
|---|---|
| Check | P3 |
| Location | Fig. 3a, legend items "Diorite" and "Sand and pebble gravel", block faces, scale bar (p. 8) |
| Quotation | "Fig3. Landslide restoration diagram: (a) 3D views of the study area" |
| Concern | Measured swatches: Diorite #8c7c74, Sand and pebble gravel #8c745c, Massive gravelly soils #b49c74, Granite #744c3c. Diorite and Sand and pebble gravel differ by 0 + 8 + 24 = 32, below the limit of 40 at which two colours count as equal. On the block face the layers are #b29b77, #89776f and #747474; #89776f matches both Diorite and Sand and pebble gravel, and #747474 has no grey swatch in the legend. The scale bar (labels 0, 400, 1000 m) sits on a perspective block view whose scale varies across the image. |
| Suggestion | Use clearly different colours or patterns for Diorite and Sand and pebble gravel, add the grey layer to the legend, and replace the scale bar by a statement that the view is not to scale, or give scales along the block edges. |
| Status | verified (colours measured); inferred (scale-bar issue) |
| Severity | minor |
| Source | AB |

**GB-19 Several axes have no quantity or unit: Fig. 3b, Fig. 7h to 7n, the time axis of the accelerogram in Fig. 4, and the axis "Frequency" of Fig. 10b, whose fitted curve is not explained.**

| Field | Content |
|---|---|
| Check | P29 |
| Location | Fig. 3b (p. 8); Fig. 4 inset (p. 10); Fig. 7h to 7n (p. 18); Fig. 10b (p. 23) |
| Quotation | "Fig10. (a) movement trails of 10 monitoring points and (b) the plot of travel distance vs. collision frequency." |
| Concern | Fig. 3b has a chequered elevation scale and distance labels 0 to 1500 without names or units. Fig. 7h to 7n have numbers 0 to 1200 and 0 to 2700 without names or units, and the colour bar says "Stress" without component, although Table 2 lists Stress-XX, YY and ZZ. The accelerogram inset of Fig. 4 has "Acceleration (gal)" but a time axis without values or unit, so duration and the times tp, tPGA, tf, te cannot be read. Fig. 10b labels the vertical axis "Frequency" without saying whether it is a count per 100 m bin (see GB-26), and the red curve has no equation, fit type, goodness of fit or legend entry. |
| Suggestion | Add axis names with units to Fig. 3b, the inset of Fig. 4 and Fig. 7h to 7n, name the stress component, define "Frequency" and the bin width in the caption of Fig. 10b, and give the fitted function with its parameters. |
| Status | verified (page images) |
| Severity | minor |
| Source | AB |

**GB-20 Several labels are too small to read at print size: contour labels of Fig. 3c, tick labels of Fig. 10a and Fig. 11, and the annotations in Fig. 12.**

| Field | Content |
|---|---|
| Check | P3 |
| Location | Fig. 3c (p. 9); Fig. 10a (p. 23); Fig. 11a to 11j (p. 23 to 24); Fig. 12a and 12b, annotations "1116.8", "29.47", "319.5" (p. 25) |
| Quotation | "Fig11. Comparison of the overall envelope fitting of the landslide at 10 different times" |
| Concern | Measured digit heights at 300 dpi: Fig. 11 tick labels 8 to 9 px (about 0.7 mm), in light grey; Fig. 12 annotation "1116.8" 11 px (about 0.8 mm), and "29.47" overlaps the axis label "0"; Fig. 3c contour labels about 8 px, several upside down; Fig. 10a tick labels about 9 px. The axis numbers of Fig. 5d, for comparison, are 15 px (1.3 mm). At about 0.7 mm the axes of Fig. 11 and the annotated values of Fig. 12 cannot be checked by a reader in print. |
| Suggestion | Enlarge tick labels and annotations to the size used in Fig. 5 and 8, and move "29.47" away from the axis label. |
| Status | verified (measured) |
| Severity | minor |
| Source | AB |

**GB-21 Settings of the dynamic simulation that control dissipation and runout are not given: damping, time step, block size check, discontinuity geometry, parameter sources and software version.**

| Field | Content |
|---|---|
| Check | P35, P8 |
| Location | p. 9, l. 168 to 170 and l. 178 to 180; p. 10, l. 193 to 202; p. 11, l. 206 to 212 and Table 1; p. 6, l. 130 to 131 |
| Quotation | "the selection of physical-mechanical parameters was based primarily on laboratory testing, empirical analogy, and parameter inversion" |
| Concern | Dissipated energy is the central quantity of the study, but the mechanical damping of the dynamic stage (type and value) is not stated; damping removes energy independently of friction and collisions and enters DE directly. Also missing: time step and number of steps; whether results were checked for a block size other than 8.7 m (compare GB-07); orientation and spacing of the "uniform structural plane" (l. 179 to 180) and of both discontinuity sets of Table 1; which Table 1 values come from laboratory tests, which from analogy and which from inversion, and what the inversion was fitted to; the 3DEC version; date, sensor and resolution of the UAV DEM. Provenance and access are treated in GB-13 and GB-45. |
| Suggestion | Add to Sect. 2.1 (p. 9 to 11) a table of numerical settings (3DEC version, damping, time step, block size, contact model, discontinuity orientation and spacing), a column in Table 1 with the source of each value, the target and result of the inversion, and date and resolution of the DEM. |
| Status | verified (absences in the text) |
| Severity | moderate |
| Source | SD |

**GB-22 The terms for structural discontinuities vary between six expressions, and Table 1 cannot be matched to them.**

| Field | Content |
|---|---|
| Check | P38 |
| Location | p. 9, l. 176 to 180; p. 11, l. 209 to 210 and Table 1, rows "discontinuities", "potential discontinuities"; p. 15, l. 302, l. 308 to 309, l. 313, l. 320, l. 323 |
| Quotation | "The discontinuities are represented by both fully developed potential rupture planes and joint sets" |
| Concern | Table 1 gives two contact parameter sets, which is what is needed to rebuild the joint model, but the modelled planes are named "structural plane", "discontinuities", "joint sets", "potential rupture planes", "potential sliding surfaces" and "potential failure planes". Two pairings are possible (joint sets as "discontinuities" and rupture planes as "potential discontinuities", or the reverse), and the text does not say which. "Structural plane" denotes both the real planes that are ignored (l. 176 to 178) and the model's "uniform structural plane" (l. 179 to 180), and in Sect. 3.1 planes that control failure (l. 308 to 309, 323). "Fully developed potential rupture planes" combines contradicting qualifiers. Which plane is the basal sliding surface, and which parameters it carries, cannot be read from the manuscript. |
| Suggestion | Define two terms once in l. 209 to 210 (for example "block joints" for the 8.7 m grid and "basal sliding surface"), use them as row names in Table 1, and replace the terms in l. 180, 302, 308 to 309, 313, 320 and 323 accordingly. |
| Status | verified (term counts in the text layer; wording on page images p. 9, 11); assumption (which row corresponds to which plane, posed as question) |
| Severity | moderate |
| Source | S2 |

**GB-23 The seismic input is a proxy record whose amplitude, duration, components, scaling and representativeness are not given, and whose tectonic justification conflicts with the site description.**

| Field | Content |
|---|---|
| Check | P35, P9 |
| Location | p. 10, l. 183 to 191; p. 5, l. 97 to 99 and l. 110; Fig. 4 inset (p. 10); p. 29, l. 600 to 602 |
| Quotation | "It is worth noting that both the Mogangling landslide and the Wenchuan earthquake zone belong to the tectonic system of the Longmenshan Fault Zone. Extensive research indicates that the Kangding earthquake is comparable to the 2008 Wenchuan earthquake in terms of damage distribution, affected intensity, and estimated magnitude." |
| Concern | The authors disclose that no record of the 1786 event exists (l. 183 to 186), so a proxy is understandable. Not stated are the peak ground acceleration as applied, the duration, which components were applied in which direction, whether the record was scaled or filtered, and how it was converted for the viscous base (l. 196 to 198); the inset of Fig. 4 shows amplitudes of roughly ±100 gal without explanation. "Extensive research" (l. 187) carries no citation. Sect. 2.1 places the site at the junction of the Xianshuihe, Longmenshan and Anninghe faults (l. 98 to 99), and the listed Zhao et al. (2021) name the event "the 1786 Moxi M 7.75 earthquake" (l. 601); the statement that the site belongs to the Longmenshan system (l. 186 to 187) needs to be reconciled with this. All motion and energy results follow from this single input, and no sensitivity analysis shows which results depend on it. Question to the authors: how far was Luding station from the Wenchuan rupture, and is a record from that distance representative of near-field shaking at Mogangling? |
| Suggestion | In l. 183 to 191 give network, station code, components, PGA, duration, scaling, filtering and application at the base, and cite the sources for comparability; repeat the simulation with the record scaled to at least two further PGA levels, or with a second record, and report in Sect. 3 how runout, peak KE and the DE partition change. |
| Status | verified (missing parameters, missing citation, fault inconsistency); assumption (representativeness of a distant record, posed as question) |
| Severity | major |
| Source | SD |

**GB-24 Velocity peaks are used as collisions without any check against contacts in the model, and no false positive or false negative rate is given.**

| Field | Content |
|---|---|
| Check | P32, P31 |
| Location | p. 11, l. 220 to 234; Fig. 5 (p. 12); p. 1, l. 22 to 23 (Abstract); p. 25, l. 473 to 475 (Conclusion 2) |
| Quotation | "Hence, effective collisions can be detected by pinpointing the significant local maxima on the velocity-distance profile." |
| Concern | The method assumes that a pronounced velocity peak is caused by a collision. A block also accelerates on steeper ground or after losing contact with the bed and decelerates on flatter ground, so peaks can arise without a collision; a collision can also change direction without raising speed. The threshold was chosen by visual judgement on one curve (Fig. 5b to 5f) as the one at which identification "is deemed acceptable" (l. 232 to 233); no reference set of true collisions exists against which the over- and undercounting described in l. 230 to 232 could be measured. The model's contacts and contact forces between blocks are not used to confirm that detected peaks coincide with contacts, yet Conclusion 2 presents the identification as established. Question to the authors: were the detected peaks compared with contact events in the model? |
| Suggestion | For the ten monitored blocks extract contact events (contact force above a threshold, change of contact partners) from the model and compare them with the detected peaks; report in Sect. 2.2 the share of peaks with a coinciding contact (precision) and the share of contacts with a peak (recall) for each threshold of Fig. 5, choose the threshold on this basis, and limit Conclusion 2 (l. 473 to 475) to the measured agreement. |
| Status | verified (absence of a validation); assumption (alternative causes of peaks from general mechanics and availability of contact output, posed as questions) |
| Severity | major |
| Source | SD |

**GB-25 The curve from which effective collisions are extracted carries five names, and its abscissa is called both "travel distance" and "travel displacement".**

| Field | Content |
|---|---|
| Check | P38 |
| Location | p. 11, l. 221, l. 225, l. 227, l. 233 to 234; p. 1, l. 22 to 23; Fig. 1, panel "Effective Collision" (p. 4); Fig. 5a and 5b to 5f, x axes (p. 12); Fig. 10b (p. 23); p. 25, l. 474 to 475 |
| Quotation | "a typical velocity-travel-distance curve" (l. 221); "the velocity-distance profile" (l. 225); "the travel-distance versus velocity profile" (l. 233 to 234); "local peak value of the displacement velocity curve" (l. 22 to 23); "displacement-velocity curves" |
| Concern | Section 2.2 shows the effect of the prominence threshold in Fig. 5b to 5f, which makes the choice traceable (PP-21), but the same curve is named in five ways, and two names suggest velocity against displacement. Fig. 5a labels the abscissa "Travel distance (m)", Fig. 5b to 5f "Travel Displacement (m)". Travelled path length and net displacement are different quantities and diverge for a block that bounces to the opposite bank (l. 397 to 399). Fig. 10b, which supports the conclusion on collision frequency against migration distance, uses "Travel distance". Graded moderate because the ambiguity affects how Fig. 10b and the 1,139 collisions can be reproduced. |
| Suggestion | Define the abscissa once in Sect. 2.2 (for example "travel distance, the cumulative path length of the block centroid"), call the curve "velocity versus travel distance curve" in l. 23, 221, 225, 227, 233 to 234 and 474 to 475, and relabel the x axes of Fig. 5b to 5f "Travel distance (m)". |
| Status | verified (names and axis labels on page images p. 1, 11, 12, 23, 25); inferred (divergence of path length and displacement for the monitored blocks) |
| Severity | moderate |
| Source | S2, AB, S4 |

**GB-26 The population behind the 1,139 effective collisions, the bin width of Fig. 10b and the reference quantity of the threshold are not stated, and the frequencies in Fig. 10b add up to about 1214.**

| Field | Content |
|---|---|
| Check | P20, P3, P8 |
| Location | p. 11, l. 227 to 234; Fig. 5b to 5f (p. 12); p. 22, l. 414 to 415; Fig. 10b (p. 23, caption l. 423 to 424) |
| Quotation | "At a threshold of 30%, however, the identification of effective collisions is deemed acceptable. Under this setting, 1,139 effective collisions were detected from the travel-distance versus velocity profile." |
| Concern | "The travel-distance versus velocity profile" is singular, while 1,139 is a total; it is not said whether it covers one block, the ten monitored blocks (113.9 per block) or all blocks, and the routine is not named. The threshold "30%" has no reference quantity (peak height, maximum velocity of the block, or curve range). Fig. 10b, introduced as collisions "experienced by blocks at different locations" (l. 415), has 26 points at 100 m spacing from 0 to 2500 m; calibrated readings (2, 4, 5, 7, 15, 16, 7, 27, 20, 24, 30, 28, 37, 42, 49, 50, 53, 61, 69, 72, 142, 157, 150, 146, about 0 and 0.5) sum to 1213.8 ± 9.4, confirmed independently (about 1214); this is 75 (6.6 %) more than 1,139. The threshold-30 % profile in Fig. 5d carries only about 87 red markers, mostly below 1900 m, whereas 49.0 % of the collisions in Fig. 10b fall in the last four bins (2200 to 2500 m). The three numbers cannot describe the same set. If Fig. 10b showed the collisions of one block binned by distance, it could not support statements about locations. Could the authors confirm whether Fig. 10b shows one block or several? |
| Suggestion | In l. 227 to 234 define the prominence threshold as a formula, name the routine and the block population behind 1,139; in the caption of Fig. 10b state the population, bin width, total count and the fitted function with its fit statistic; make the totals agree or explain the difference. |
| Status | verified (missing definitions; sum measured by two instances); inferred (identity of the populations); assumption (one-block reading, posed as question) |
| Severity | moderate |
| Source | S3, AB, SD |

**GB-27 The block in Fig. 5b to 5f reaches 45.2 m/s, above the maximum velocity of 31.6 m/s reported for the landslide, and the block is not identified; the ten monitored blocks of Fig. 9 do not exceed about 15 m/s.**

| Field | Content |
|---|---|
| Check | P3 |
| Location | Fig. 5b to 5f (p. 12, caption l. 238 to 239); p. 11, l. 220 to 221; p. 16, l. 330 and l. 337; Fig. 9 (p. 21 to 22); Table 2 |
| Quotation | "As shown in Fig7. (e) and (l), during the impact-at-base stage, the maximum velocity reached 31.6 m/s." |
| Concern | In Fig. 5d (0 m/s at 1780.5 px, 50 m/s at 1302.0 px) the curve peaks at 1348 ± 2 px, i.e. 45.2 ± 0.3 m/s, at a travel distance of 255 m. The colour bars of Fig. 7 give 27.1 m/s at 9 s and 31.6 m/s at 12 s as maxima of the whole model, and l. 337 calls the valley-floor arrival the velocity peak. A block reaching 45 m/s after 255 m from rest does so within about 11 s, i.e. within the interval of Fig. 7b to 7e. The kinetic energy segments in Fig. 9 have maxima of 0.024 to 0.262 GJ, which with Table 2 volumes and 2300 kg/m³ correspond to 3.4 to 14.9 m/s. Fig. 5 calls its curve "typical" (l. 221), yet it is three times faster than any monitored block. Fig. 7 shows only seven instants, so a short excursion above 31.6 m/s between them is a possible resolution. |
| Suggestion | Identify in the caption of Fig. 5 the block of panels b to f and state when its peak occurs, and either report the overall maximum velocity in Sect. 3.1 or explain why this block exceeds it. |
| Status | verified (45.2 m/s and Fig. 9 values measured; peak confirmed at the page image during merging); inferred (conflict with the overall maximum) |
| Severity | moderate |
| Source | AB |

**GB-28 The energy values in Fig. 8, 9 and 12 cannot be reproduced from the stated volumes, density, velocities and potential-energy datum.**

| Field | Content |
|---|---|
| Check | P23, P1, P3, P5 |
| Location | p. 13, l. 248 (Eq. 3) and l. 252 to 255; p. 11, Table 1, row "landslide mass", column "Density"; p. 9, l. 182; p. 7, l. 151; p. 16, l. 330; Fig. 8 (p. 20); Fig. 9a to 9j (p. 21 to 22); Fig. 12 (p. 25); p. 13, Table 2 |
| Quotation | "the potential-energy calculation uses the model's initial height as the reference datum rather than true sea level; only the change in potential energy due to relative displacement is considered" (l. 253 to 255); "the volume of the landslide is 317563 m3" |
| Concern | (1) Whole mass. Measured in Fig. 8: total 6526 ± 10 GJ in all 105 bars (6531 GJ in an independent measurement), kinetic energy peak 1685 ± 30 GJ at about 13.7 s; Fig. 12 marks 1116.8 GJ. With 2300 kg/m³ (Table 1) and 317563 m³, m = 7.30×10⁸ kg: releasing 6526 GJ needs a mean drop of the centre of mass of 911 m, more than the total relief of 747 m + 131 m = 878 m (l. 174 to 175); at the reported maximum of 31.6 m/s (l. 330) KE cannot exceed 0.5 × 7.30×10⁸ × 31.6² = 365 GJ, whereas 1116.8 GJ and 1685 GJ need rms velocities of 55.3 and 67.9 m/s. With 2.4×10⁷ m³ (l. 151), KE fits (rms 7.8 m/s) but the mean drop becomes 12.1 m. With 2700 kg/m³ the values are 776 m, 62.7 m/s and 428 GJ, or 10.3 m. The block totals of Fig. 9 (sum about 43.6 GJ for 11512.7 m³) scaled to 6526 GJ point to about 1.7×10⁶ m³. No stated combination of volume and density reproduces both PE and KE. (2) Datum. A datum at the initial height gives PE(t0) = 0 and negative values later; Fig. 8 and 9 start with PE at its maximum and end at about 0. Initial PE per block (measured: 5.057, 5.128, 4.017, 3.569, 11.084, 6.601, 1.179, 4.373, 1.596, 0.948 GJ) with Table 2 volumes gives drops of 238, 222, 235, 164, 316, 173, 30, 193, 83 and 43 m and datum heights of 102 to 712 m in Table 2 coordinates; the drops decrease with initial height (Spearman rho = -0.65), so they cannot share one datum, and blocks 1 and 3 reach PE = 0 and rise again. This suggests each block's lowest position as datum, which makes block PE values incomparable; DE is not affected because the datum cancels in Eq. (4). Possible resolutions, none stated: a different mass, density, unit, block set or datum. |
| Suggestion | In Sect. 2.3 (l. 250 to 255) state the datum actually used and the total mass (volume and density) behind Fig. 8 and Fig. 12; add to Table 2 the mass, initial and lowest elevation and initial PE of each monitored block; give in Sect. 3.2.1 the highest block velocity of the run; correct either the volume in l. 182 or the energy values. |
| Status | verified (energies measured in Fig. 8 and 9 by two instances; peak confirmed at page image p. 20 during merging; 31.6 m/s, 317563 m³, 2300 kg/m³ and the datum wording at page images); inferred (products, implied heights, rank correlation); assumption (which mass and datum were used, posed as question) |
| Severity | major |
| Source | S3, AB, SD |

**GB-29 Energy conservation of the whole mass follows from the definition of DE in Eq. (4) and cannot be a simulation result; the same identity holds for every single block, so the contrast between whole mass and single blocks does not follow from Fig. 8 and Fig. 9.**

| Field | Content |
|---|---|
| Check | P23, P15, P31, P10, P3 |
| Location | p. 13, l. 249 (Eq. 4); p. 19, l. 375 to 377 and l. 387 to 389; p. 20, l. 392 to 396 and l. 399 to 402; Fig. 8 (p. 20); Fig. 9a to 9j (p. 21 to 22); p. 1, l. 26 to 28 (Abstract); p. 25, l. 476 to p. 26, l. 482 (Conclusion 3) |
| Quotation | "It is evident that, due to the law of energy conservation, the total sum of the three forms of energy remains constant throughout the landslide." (l. 375 to 377); "unlike the total landslide mass, the energy of single blocks is not conserved" |
| Concern | The comparison of whole mass and single blocks is the first result named in the Abstract and Conclusion 3. Eq. (4) defines DE(ti) = ME(t0) minus ME(ti), so KE + PE + DE = ME(t0) for every block and every sum of blocks at every time, whatever the simulation does (numerical check with arbitrary values: ratio 1.0). The constant total in Fig. 8 (6526 GJ in all 105 bars) therefore cannot confirm conservation or that the run "can be regarded as a successful energy extraction numerical simulation" (l. 388 to 389). All ten panels of Fig. 9 also show a constant stacked total within ±1 px; what differs is only whether DE decreases, i.e. whether PE + KE rises: block 1 six rises totalling 0.43 GJ, block 3 eleven rises totalling 0.49 GJ, block 7 one of 0.014 GJ, block 9 two of 0.022 GJ, the other six none. The manuscript states that apparent DE decreases are "due to the calculation method used" (l. 399 to 400), but the consequence is not drawn. A rise of ME can stem from work by neighbouring blocks but also from the seismic input applied at the base throughout the dynamic stage (l. 196 to 198), which is not separated; energy leaving through the viscous boundaries is equally counted as "dissipation". With an external input the system is not closed, so "obeys the law of energy conservation" (l. 477 to 478) would require the input work in the balance. |
| Suggestion | In Sect. 2.3 call DE the residual of mechanical energy and list what it contains (friction, damping, contact work by neighbours, seismic input, boundary loss); if a physical balance is intended, compute seismic input work at the base, boundary work, frictional and damping dissipation and, for single blocks, contact work separately from the model output and report the closure error over time in Sect. 3.2.1. Rewrite l. 375 to 377, l. 388 to 389, l. 392 to 394, the Abstract (l. 26 to 28) and Conclusion 3 so that the result is the timing and size of mechanical-energy gains of single blocks, and mark these intervals in Fig. 9a and 9c. Was the energy tracking of 3DEC available and used? |
| Status | verified (Eq. 4; constant totals measured in Fig. 8 and Fig. 9; quotations); inferred (identity derived from Eq. 1 and 4; content of DE including seismic input and boundary loss) |
| Severity | major |
| Source | S3, S4, AB, SD |

**GB-30 The four zones of monitoring points carry different names in the abstract, text, Table 2, Fig. 6 and the conclusions, Fig. 6 labels the two middle zones in the reverse order of Table 2, and its points carry no IDs.**

| Field | Content |
|---|---|
| Check | P38, P3, P29 |
| Location | p. 13, l. 256 to 257; Table 2, column "Position" (p. 13); Fig. 6, zone labels and points (p. 14, caption l. 268); Fig. 10a legend (p. 23); p. 1, l. 28 to 29; p. 26, l. 483 to 485 |
| Quotation | "ten monitoring points were installed in the lower, lower-middle, upper-middle, and upper portions of the slide mass" |
| Concern | Grouping the points by slope position suits the comparison of different parts of the mass, but the zones are called lower and upper (l. 256, Abstract), bottom and top (Table 2, Fig. 6) and front and rear (Conclusion 4). From upslope to downslope Fig. 6 reads "Top", "Lower middle part", "Upper middle part", "Bottom", with 2, 3, 3 and 2 spheres. Table 2 elevations rise from bottom to top (mean z: bottom 347.5 m, lower middle 479.0 m, upper middle 671.0 m, top 753.5 m), so the zone next to "Top" must be the upper middle part. The ten spheres of Fig. 6 carry no ID and no colour legend, and the three axes have no names or units; in Fig. 10a red is point 1, which Table 2 places at the bottom, whereas the red sphere in Fig. 6 lies in the zone labelled "Top". Since the Abstract (l. 28 to 30) and Conclusion 4 are stated in terms of these zones, a reader cannot check which blocks they refer to. |
| Suggestion | Swap the labels "Lower middle part" and "Upper middle part" in Fig. 6, label each sphere with its Table 2 ID using the colours of Fig. 10a, add axis names with units, and use one set of zone names in l. 28 to 29, l. 256 and l. 483 to 485, stating whether "front" means "lower". |
| Status | verified (labels, sphere colours and counts on page images p. 14 and 23; elevations from Table 2); inferred (direction of the swap); assumption (that "front" in l. 484 means "lower") |
| Severity | moderate |
| Source | S2, AB |

**GB-31 Two announced verification steps and the stress histories are not reported: static equilibrium before dynamic loading, the maximum unbalanced force, and the block stresses.**

| Field | Content |
|---|---|
| Check | P11, P31 |
| Location | p. 13, l. 258 to 259 and l. 262 to 263; Table 2, column "Monitoring contents" and row ID 11 (p. 13); p. 10, l. 199 to 201; Fig. 7h to 7n (p. 18) |
| Quotation | "the maximum unbalanced force was tracked to verify that the model reached post-failure stability" |
| Concern | Sect. 2.1 requires static convergence before dynamic loading, and Table 2 lists the maximum unbalanced force and Stress-XX, YY, ZZ as monitored quantities; l. 262 to 263 announce stress histories for each monitored block. Sect. 3 reports neither the convergence criterion, nor the history or end value of the unbalanced force, nor any block stress history; Fig. 7h to 7n are mentioned with the velocity maps, but no stress value is discussed. Whether the model was at rest at t = 0 matters for the early energy partition (DE already about 58 to 134 GJ at 0 to 3 s in Fig. 8, measured), and whether it was at rest at 131 s matters for the stated duration (l. 300), since KE in Fig. 8 falls to near zero by about 65 s. |
| Suggestion | Show in Sect. 3.1 or a supplement the unbalanced-force history for the static and dynamic stages with the convergence criterion, state how the end of motion at 131 s was determined, and either report the block stress histories in Sect. 3.2.2 or remove them from Table 2 and l. 262. |
| Status | verified (absences; DE and KE values measured in Fig. 8) |
| Severity | moderate |
| Source | S3, SD |

**GB-32 Table 2, Fig. 4, Fig. 6, Fig. 7, Fig. 10a and Fig. 11 use at least five coordinate frames without saying how they relate, so monitoring points and envelopes cannot be located in the model.**

| Field | Content |
|---|---|
| Check | P29 |
| Location | Table 2, column "Coordinate" (p. 13); Fig. 4 and Fig. 6 axes (p. 10, 14); Fig. 7a to 7g and 7h to 7n axes (p. 17 to 18); Fig. 10a axes (p. 23); Fig. 11a to 11j axes (p. 23 to 24) |
| Quotation | "Table 2: The basic information of blocks where the 10 monitoring points are located" |
| Concern | Table 2 gives x from -719 to -68, y from -557 to 286, z from 340 to 755. Fig. 4, Fig. 6 and Fig. 7a to 7g show x from 0 to about 2400 to 2800, y from 0 to about 3200, z from 0 to 800. Fig. 7h to 7n show axes of 0 to 2860 and 0 to 1416 (GB-39). Fig. 10a shows X from 0 to 2500, Y from -158 to 237 and Z from 0 to below -840, with all ten trajectories starting at one point, so it plots displacements. Fig. 11 shows X from about -1000 to 1500, Y from -1000 to 1000 and Z from about -600 to 400. No caption names origin or orientation; the negative Table 2 coordinates cannot be placed on the positive axes of Fig. 6. |
| Suggestion | Define one model coordinate frame in Sect. 2.1 (origin, axis directions relative to north and to the sliding direction), give Table 2 in it, and state in the captions of Fig. 7h to 7n, 10a and 11 which frame or which relative coordinates are used. |
| Status | verified (axis ranges and table values at page images); inferred (incompatibility) |
| Severity | moderate |
| Source | AB |

**GB-33 The envelope analysis cannot be reproduced: the enclosed body has six names, V0 and S0 refer to a different object than Vt and St, α = 1 has no unit, point set or sensitivity check, Vt and St are not reported, and Fig. 12 plots about 30 states instead of the ten envelope times.**

| Field | Content |
|---|---|
| Check | P38, P11, P2, P8, P35, P26, P3 |
| Location | p. 14, l. 269 to 284 (heading 2.4, Eq. 5 and 6); p. 3, l. 88 to 89; Fig. 1, bottom panel (p. 4); p. 23, l. 426 to 429; Fig. 11 caption (p. 24, l. 437 to 439); p. 24, l. 440 to 441; Fig. 12a and 12b (p. 25) |
| Quotation | "In these expressions, V0 denotes the initial volume of the landslide mass (m³); Vt denotes the volume of the enclosing envelope at time t (m³)" (l. 278 to 279); "this study uniformly sets the α value to 1" |
| Concern | Using an envelope to quantify dispersion is a clear idea, and α is fixed. (1) The enclosed body is the "landslide accumulation area" (l. 88, heading 2.4, Fig. 1), "deposition zone" (l. 270, 272), "slide mass" (l. 272), "deposit mass" (l. 427, 449, 491), "deposit region" (l. 429) and the landslide or sliding mass (captions of Fig. 11 and 12); Fig. 11a at t = 0 s shows the intact mass, and "Accumulation area" is also zone II of Fig. 3a. (2) V0 and S0 belong to "the landslide mass", Vt and St to the envelope; if V0 were the block volume (317563 m³, l. 182) VS would not be 0 at t = 0, but the curves start at VS = 0, which suggests the envelope at t = 0. (3) α has no unit, the point set (centroids, vertices, surface points) and software are not named; with 8.7 m blocks a radius of 1 m would hardly connect neighbouring points (question: in which unit is α = 1?); fixing α does not "ensure" a tight fit (l. 283), it removes the variation without showing its effect. (4) V0, S0, Vt and St are not reported anywhere; Fig. 11 shows shapes and Fig. 12 only VS and AG. (5) Fig. 12a carries about 28 to 31 markers per curve (counted by two instances), while l. 427 and Fig. 11 name ten times; the VS values of the markers (29.5, 31.9, 33.2, 36.6, 73.7, 103.9, ... %) match every third output step of Fig. 8 (3 × 1.245 s), not the times 3, 7, 9, 12, 15 s of Fig. 11. |
| Suggestion | In Sect. 2.4 (l. 269 to 284) define V0 and S0 as the volume and surface area of the envelope at t = 0 if that was used, give the point set, the unit of α and the software, and add VS and AG for at least two further α values; use one name for the enclosed body in l. 88, 270 to 272, 427, 429, 449, 491 and the captions; add to Sect. 3.4 a table with time, Vt, St, VS and AG for every evaluated time and state all times used for Fig. 12. |
| Status | verified (names; missing values and specifications; marker counts at page image p. 25); inferred (assignment of Fig. 12 markers to every third output step of Fig. 8); assumption (which reference volume and which unit of α were used, posed as questions) |
| Severity | moderate |
| Source | S2, S3, AB, SD |

**GB-34 The indices VS and AG are expanded with different names, called "rates" although they are relative changes, and surface area is denoted both A and S.**

| Field | Content |
|---|---|
| Check | P38 |
| Location | p. 14, l. 275 and Eq. (6), l. 277 to 280; p. 1, l. 25; p. 3, l. 89; Fig. 1, bottom panel (p. 4); p. 24, l. 440 to 441; p. 25, l. 453 to 454 and axis titles of Fig. 12a and 12b; p. 26, l. 488 |
| Quotation | "volume swelling (VS) and area growth (AG)" (l. 275); "the volume expansion rate (VS) and surface area growth rate (AG)" (l. 441); "its volume (V) and surface area (A)" |
| Concern | Eq. (5) and (6) give clear definitions. VS is "volume swelling" in l. 275, Fig. 1 and Fig. 12a and "volume expansion rate" in l. 25, 89, 441 and 453; AG is "area growth" in l. 275, Fig. 1 and Fig. 12b, "area growth rate" in l. 25, "surface area growth rate" in l. 89 and 441 and "surface area growth" in l. 453. "Rate" suggests a time derivative, which makes "the rate of increase in VS" (l. 443 to 444) ambiguous. Surface area is S in Eq. (6) and A in l. 440. |
| Suggestion | Keep "volume swelling (VS)" and "area growth (AG)" as defined in l. 275 and use them in l. 25, 89, 441, 453 to 454 and 488; replace "its volume (V) and surface area (A)" in l. 440 by "its volume (Vt) and surface area (St)". |
| Status | verified (text and page images p. 4, 14, 24, 25) |
| Severity | minor |
| Source | S2, S3, S4, SD |

**GB-35 Section 2.4 says each energy curve in Fig. 12 has a unique marker and line style, but all three curves use the same solid line and round marker and differ only in colour.**

| Field | Content |
|---|---|
| Check | P3 |
| Location | p. 15, l. 290 to 291; Fig. 12a and 12b (p. 25) |
| Quotation | "Each energy curve is distinguished by a unique marker and line style to ensure clarity and facilitate visual comparison." |
| Concern | At the enlarged crops PE, KE and DE are solid lines with small filled circles; only the colour differs (grey, red, blue). In greyscale print PE and KE cannot be told apart. |
| Suggestion | Give the three curves different markers or line styles, or delete the sentence in l. 290 to 291. |
| Status | verified (page image p. 25) |
| Severity | minor |
| Source | AB |

#### Minor corrections

| ID | Location | Quotation | Replacement | Source |
|---|---|---|---|---|
| KK-17 | throughout, for example p. 2, l. 76; p. 7, l. 144; p. 15, l. 301; captions of Fig. 1 to 12 | "Fig1."; "Fig3.(a)"; "Fig7 illustrates" | "Fig. 1"; "Fig. 3a"; "Fig. 7 illustrates" (one form throughout text and captions) | S4 |
| KK-18 | Fig. 1, top panel (p. 4) | "Lower Slide Bed Restoration"; "Slide Bed Topography" | "Lower Sliding Bed Restoration"; "Sliding Bed Topography" (as "sliding bed" in l. 130, 136, 140, 158, 179) | S2 |
| KK-19 | p. 5, l. 95 to 96 | "29 ° 37 ′ 30.726 ″ north latitude, 102 ° 09 ′ 41.190 ″ east longitude" | "29°37′30.726″ N, 102°09′41.190″ E" | S4 |
| KK-20 | p. 5, l. 98 | "Y" - shaped faults | Y-shaped faults | S4 |
| KK-21 | p. 5, l. 102; Fig. 2c legend and map (p. 6); Fig. 4 legend (p. 10) | "(γO2)" (capital O); "γo2" (lower case o) | one form in all three places, for example "(γo2)" in l. 102 | S2 |
| KK-22 | p. 5, l. 104 | "The quaternary system" | "The Quaternary system" | S4 |
| KK-23 | p. 5, l. 105 (two occurrences) | "colluvial Deluvial deposit" | "colluvial-deluvial deposit" | S4 |
| KK-24 | p. 5, l. 110 to 111 | "burst the Dadu River after 9 days. The sudden flood made the downstream area a vast ocean" | "dammed the Dadu River; the dam breached after 9 days, and the sudden flood inundated the downstream area" | S4 |
| KK-25 | Fig. 2b legend (p. 6); Fig. 3a and 3b legends (p. 8) | "Daduhe River" (Fig. 2b); "Dadu river" (Fig. 3a, 3b) | "Dadu River" (as in the text and Fig. 2c) | S2, AB |
| KK-26 | p. 6, l. 132; p. 7, l. 159 | "Convert the geographical coordinate system to the projection coordinate system"; "make a section along" | "The geographic coordinate system was converted to a projected coordinate system"; "a section was drawn along" | S4 |
| KK-27 | p. 7, l. 151 | "the volume is about 2400×104 m3" (exponent 4 set on the baseline at the page image) | "the volume is about 2400 × 10⁴ m³" (for the value itself see GB-16) | S3, S4 |
| KK-28 | p. 7, l. 152; p. 9, l. 182 | "1120 m-1330m"; "1121m high" | "1120 to 1330 m"; "1121 m high" | S4 |
| KK-29 | p. 7, l. 153, 154 and 156 | "50°; The elevation"; "5-12°; The elevation"; "57°; The elevation" | "50°; the elevation"; "5 to 12°; the elevation"; "57°; the elevation" | S4 |
| KK-30 | p. 9, l. 176 to 177 | "can not be obtained" | "cannot be obtained" | S4 |
| KK-31 | p. 10, l. 193 to 195 | "In the course of a discrete-element simulation-particularly when modeling nominally semi-infinite bodies such as the use of fixed or elastic boundaries in a static analysis will inevitably reflect outbound seismic waves into the model during a subsequent dynamic analysis." | "In a discrete-element simulation, particularly of nominally semi-infinite bodies, fixed or elastic boundaries used in the static analysis would reflect outgoing seismic waves back into the model during the subsequent dynamic analysis." | S4 |
| KK-32 | p. 11, l. 218 and 228 | "block velocities-hereafter termed"; "must be chosen-one that quantifies" | "block velocities, hereafter termed"; "must be chosen, one that quantifies" | S4 |
| KK-33 | Fig. 5a legend (p. 12) | "Non-obvios acceleration" | "Non-obvious acceleration" | S4, AB |
| KK-34 | p. 13, l. 246 | "where, at time ti, PE(ti), and DE(ti) can be expressed as:" | "where, at time ti, KE(ti), PE(ti) and DE(ti) can be expressed as:" | S4, SD |
| KK-35 | p. 13, l. 251 | "(m/s);h(ti)" | "(m/s); h(ti)" | S4 |
| KK-36 | p. 13, l. 257 and l. 260 | "portions of the slide mass"; "of the entire slide mass" | "portions of the landslide mass"; "of the entire landslide mass" (the term used 27 times) | S2 |
| KK-37 | Table 2, title and last row (p. 13) | "Table 2: The basic information of blocks where the 10 monitoring points are located"; row ID "11", "Maximum unbalanced force" | "Table 2: Monitored blocks (ID 1 to 10)", and below the table "In addition, the maximum unbalanced force of the whole model was recorded." with the row ID 11 deleted | S2, SD |

#### Verification log

| ID | Check | Checked | Values | Result |
|---|---|---|---|---|
| PP-06 | P29, P3 | Register of all figures, captions and text references | 12 figures numbered 1 to 12 without gap; text references Fig. 1 l. 76; Fig. 2 l. 93, 160; Fig. 3 l. 144, 159, 160; Fig. 4 l. 173; Fig. 5 l. 220, 229 to 230; Fig. 6 l. 256; Fig. 7 l. 301 to 353, 387; Fig. 8 l. 375; Fig. 9 l. 393; Fig. 10 l. 414, 418; Fig. 11 l. 428; Fig. 12 l. 443; panel counts Fig. 5 six, Fig. 7 fifteen, Fig. 9 ten, Fig. 11 ten, Fig. 12 two; no graphical abstract, no appendix figures | no finding beyond those listed |
| PP-07 | P13 | Event data outside the introduction against the listed studies of the same landslide | Zhao et al. (2021) abstract: Moxi M 7.75 earthquake, volume about 4500×10⁴ m³, deposit about 450 m by 1000 m, dam crest about 130 m above the river, lake about 9.504×10⁸ m³, outburst flow over 7100 m³/s, over 100 000 deaths; "Ms7 ¾" in l. 110 equals 7.75; "after 9 days" not in the abstract. Zhou et al. (2024) abstract: amplification, back-slope effect, interface dynamic stress and double-sided slope effect as causes, no energy analysis or terrain reconstruction | magnitude consistent; deviations raised in GB-16 |
| PP-08 | P38 | Identifiers without finding | "Mogangling" 26 times without variant; KE 8, PE 8, DE 7, ME 6 times, all as defined in l. 241 to 243 and in the legends of Fig. 1, 8, 9, 12; "monitoring point", "monitored block", "Block 1", "point 1" denote the same ten objects, linked by the title of Table 2; Fig. 10a legend numbers 1 to 10 match Table 2 IDs; "Kangding earthquake" and "1786 Moxi M 7.75 earthquake" (title of Zhao et al. 2021) denote the same event, 7 + 3/4 = 7.75; "Dadu River fault (Detuo fault)" defined at first use | no finding |
| PP-09 | P12 | Every data source and code item in Sect. 1 to 2.4 against the statements in l. 494 to 506 | 13 sources: UAV DEM, remote sensing image, geological map, tablet record, restored terrain, Luding record, laboratory tests and inversion, 3DEC model, peak-detection routine and 1,139 collisions, block histories, global energy series, alpha-shape routine and envelopes, field imagery; 0 published, 8 covered only by "upon reasonable request", 5 external or unclear sources not addressed; 0 links; no appendix or supplement. Disclosed limits: no record of 1786, no structural-plane data, tablet as only historical record, dam break not modelled | GB-13, GB-45 |
| PP-10 | P1 | Planar area from length and width (l. 149 to 150) | 450 m × 1000 m = 450000 m² = 0.45 km², stated 0.45 km² | consistent, no finding |
| PP-11 | P2 | Apparent conflict of elevations relative to the river | slope toe 1120 m, "about 5 m higher than the river surface" (l. 151 to 152) against "179 m away from the Dadu River, and the vertical height is about 131 m" (l. 174 to 175): the first describes the present deposit toe, the second the pre-failure model mass | different objects, no finding |
| PP-12 | P3 | Slopes of l. 151 to 156 against the ground line of Fig. 3b | ground surface 1841 m at 13 m, 1577 m at 200 m, 1384 m at 499 m, 1297 m at 850 m, 1192 m at 999 m; mean slopes 50.6° (text 57°), 29.8° (35°), 16.6° (5 to 12°), 25.3° with a 59° step (50°); text values derive from the reconstructed surface, Fig. 3b is one profile; disclosed: restored terrain is smooth (l. 161) | no finding |
| PP-13 | P3 | Section line a to a' in Fig. 2c against Fig. 3b and the sliding direction | scale 2.194 m/px; line length 1510 m, azimuth 74.1°; Fig. 3b axis 0 to 1500 m, vertical exaggeration 0.97; river at about 1145 to 1260 m along a to a', water in Fig. 3b at about 1100 to 1300 m; text 75° | consistent, no finding |
| PP-14 | P29 | Every hatch and colour of the map body of Fig. 2c against its legend | γo2, γM2, Q4col+dl, Q4al, Q4del, landslide boundary, faults, river, bridge all in the legend; section line, dip symbols, flow arrows and contour unit not (GB-09); north arrow and scale bar present | finding GB-09 only |
| PP-15 | P3 | Linearity of the scale bars of Fig. 2c and 3c | Fig. 2c: 0, 200, 400, 600 m at 1559.5, 1649.5, 1743, 1833 px; Fig. 3c: 0, 400, 800, 1400 m at 567, 655.5, 746, 879 px, expected 880.3 px for 1400 m | linear within 2 px, no finding |
| PP-16 | P7 | Validity of method and version for all reported data | one run, one parameter set, one threshold (30 %), one α (1); Fig. 5a shows another block (about 600 m, about 14 m/s) than Fig. 5b to 5f (about 2500 m, about 45 m/s); no method versions, protocol or device changes reported | no finding |
| PP-17 | P3 | Annotations of Fig. 4 against l. 173 to 175 | 1021 m, 747 m, 179 m, 131 m in figure and text; perspective view not measurable | consistent, no finding |
| PP-18 | P17 | Each disclosed limitation against the place where the method is introduced | structural planes ignored (l. 175 to 178), missing 1786 record (l. 183 to 186), smooth restored terrain (l. 160 to 162), PE datum (l. 253 to 255): at the method, correct; dam break not modelled (l. 348 to 350): not a method of the study; deposit restoration difficulty (l. 466 to 468): only in Conclusions (GB-14) | no further finding |
| PP-19 | P18 | Principles stated by the manuscript applied to itself | static equilibrium before dynamic loading (l. 199 to 201): applied, result not shown (GB-31); viscous base and free-field boundaries (l. 196 to 198): stated as applied; criticism of 2D simplified models (l. 47 to 49): study is 3D; restoration offered for reuse (l. 50 to 51): see GB-14 | no further finding |
| PP-20 | P26 | Scope of all guarantee formulations | "ensures that the simulation outcomes align" (l. 471): GB-38; α "ensures a tight fit" (l. 283): GB-33; viscous boundaries (l. 196 to 198): one mode and path, none suspended; unbalanced force "to verify" (l. 258): GB-31 | no further finding |
| PP-21 | P2, P3 | Thresholds of the collision identification in text, caption and Fig. 5 | text l. 230 to 232: 10, 20, 30, 40, 50 %; caption (b) to (f) the same; red marker pixels 3595, 1586, 934, 806, 790 px and patches 93, 72, 52, 46, 45 for 10 to 50 %, monotonic; Fig. 5a with 6 red and 5 purple markers as stated in l. 221 to 224 | consistent; reference quantity missing (GB-26) |
| PP-22 | P27 | Unchecked components and their use downstream | restored terrain: initial mass and all energies (GB-14, GB-16); proxy input: all motion results (GB-23); 30 % threshold: 1,139 collisions, Fig. 10b, Abstract, Conclusion 4 (GB-24, GB-26, GB-40); α = 1: VS, AG, phase transition (GB-33, GB-42); parameter inversion: Table 1 (GB-21) | no further finding |
| PP-23 | P2, P11, P3 | Number and identity of monitored blocks across text, table and figures | ten points in l. 256, 262, 392; Table 2 IDs 1 to 10 in four positions (2, 3, 3, 2 blocks), ID 11 the unbalanced force announced in l. 258; Fig. 6: ten spheres, zones from top 2, 3, 3, 2; Fig. 9 panels (a) to (j) for points 1 to 10; Fig. 10a legend 1 to 10 | count consistent; labels and IDs in GB-30 |
| PP-24 | P1, P21 | Block volumes of Table 2 as basis for block comparisons | 939.9, 1021.6, 756.2, 966.8, 1553.4, 1692.3, 1754.3, 1003.5, 856.9, 967.8 m³; mean 1151.3 m³; max/min 2.32; column heights 10.0 to 23.2 m on 75.69 m² | used in GB-16, GB-28, GB-40 |
| PP-25 | P30 | Reported errors and corrections against the run | none reported | no finding |
| PP-26 | P37 | Marking of subsequently changed data in Fig. 3c, Fig. 7 to 12, Table 1 and 2 | restored terrain in Fig. 3c labelled "Terrain after repair"; no other changes described; disclosed: smoothness of the restored terrain (l. 160 to 162) | no finding |
| PP-27 | P33 | Statements on effort, duration or workload | none found | no finding |

### Segment 3: Results (p. 15 to 25)

#### Substantive findings

**GB-36 Sect. 3.1 attributes failure to structural planes and describes brecciation and a 20 m fractured layer, although the model ignores structural planes, and the provenance of these statements is not stated.**

| Field | Content |
|---|---|
| Check | P6, P19 |
| Location | p. 15, l. 307 to 313, l. 319 to 320 and l. 323; p. 16, l. 327 to 329 and l. 333 to 335; p. 9, l. 175 to 180; p. 11, l. 208 to 210 and Table 1; p. 25, l. 469 (Conclusion 2) |
| Quotation | "The first-arriving P-waves caused intense vertical dislocation along the steeply dipping structural planes outside the slope." (l. 308 to 309); "the impact of the structural plane on the landslide process has to be ignored in this study" |
| Concern | The disclosed limitation (l. 176 to 178) is placed correctly, but its consequences are not drawn in Sect. 3.1. The model contains "a uniform structural plane" (l. 179 to 180) and two discontinuity sets in Table 1 whose orientation and spacing are not given. Sect. 3.1 nevertheless explains initiation by P- and S-wave action on steeply dipping structural planes, by "structural plane control" (l. 323), by brecciation along failure planes (l. 319 to 320), by "a loosely consolidated fractured layer approximately 20 meters thick" (l. 328) and by "a layered pseudo-bedrock" (l. 335). None of these is shown in Fig. 7 or measured in the model output, and a model of 8.7 m blocks cannot resolve brecciation. It is not stated whether these statements come from the simulation, from field observation or from the literature; Wu et al. (2013) and Zhao et al. (2021) on the same landslide are in the reference list but not discussed. Conclusion 2 adds that the simulation "can incorporate ... geological structures" (l. 469). |
| Suggestion | In Sect. 3.1 (l. 306 to 345) mark for each mechanism whether it is model output (with figure and quantity), field observation (with location) or literature (with citation), and remove model attributions of structural-plane control; give in Sect. 2.1 orientation and spacing of the uniform structural plane and of both discontinuity sets. |
| Status | verified (contradiction and missing provenance); inferred (inability of 8.7 m blocks to resolve brecciation) |
| Severity | major |
| Source | SD |

**GB-37 Backflow flooding is inferred "based on the simulation results", although the simulation models neither water nor the dam break.**

| Field | Content |
|---|---|
| Check | P19 |
| Location | p. 16, l. 348 to 352; p. 5, l. 110 to 112; p. 6, l. 136 to 138 |
| Quotation | "However, based on the simulation results, it can be inferred that the landslide-induced damming caused a rapid rise in the water level behind the dam, resulting in backflow flooding in the surrounding counties and cities." |
| Concern | The preceding sentence discloses that "the subsequent dam-break process after river blockage was not modeled" (l. 349 to 350), and the model description in Sect. 2.1 contains no water or fluid phase. A rise of the water level and backflow flooding can therefore come only from the historical record (l. 110 to 112; the Tiezhuang Temple tablet, l. 136 to 138) or from the literature, not from the simulation; the sentence assigns a statement from outside the model to model output. Graded moderate because a reader cannot trace the provenance of the statement. |
| Suggestion | In l. 350 to 352 attribute the statement to its source (historical record or literature, with citation) and limit the simulation statement to what the model shows, for example the position and height of the simulated deposit in the channel. |
| Status | verified (text l. 348 to 352; absence of water or fluid in the model description of Sect. 2.1) |
| Severity | moderate |
| Source | ZF |

**GB-38 The validation against the field is qualitative only, yet it is described as compelling and as ensuring agreement with actual conditions.**

| Field | Content |
|---|---|
| Check | P11, P15, P31, P26 |
| Location | p. 16, l. 353 to 359; Fig. 7o (p. 19); p. 7, l. 149 to 156; p. 13, l. 264 to 266; p. 25, l. 469 to 475 (Conclusion 2) |
| Quotation | "Fig7. (o) presents compelling evidence of agreement between the numerical simulation results and the actual field observations." (l. 353 to 354); "Comparison with field imagery and result analysis ensures that the simulation outcomes align with actual conditions." |
| Concern | Fig. 7o compares a simulated view with two photographs by two dotted frames (a protruding ridge in the source area, a deposit area), and the text names "several clear points of correspondence" (l. 355 to 356). No quantity is compared, although Sect. 2.1 provides field values that would allow it (planar area 0.45 km², width about 1000 m, toe elevation 1120 m, platform 1330 to 1380 m, volume about 2400×10⁴ m³): not runout, deposit footprint, thickness, dam height, nor deposit position relative to the river at 131 s. The authors note that weathering has altered the topography (l. 354 to 355), which makes a quantitative comparison harder but does not replace it. Because the sliding bed is taken from the present DEM (l. 135 to 136), part of the agreement in deposit position may be inherited from the input terrain. "Ensures" (l. 471) is stronger than the evidence; the manuscript's own "support the validity" (l. 359) fits it. Field investigations are announced as input to the analysis (l. 265 to 266, l. 472 to 473), but no field result is reported apart from the photographs. Graded major because the claimed agreement is the basis on which all energy conclusions are transferred to the real event. |
| Suggestion | Add to Sect. 3.1 a table "field against simulation at t = 131 s" with deposit area, length, width, maximum thickness or dam height and volume, each with its deviation in per cent, or the overlap of simulated and mapped deposit footprints; repeat it for at least two alternative friction values of Table 1; replace "ensures that the simulation outcomes align with actual conditions" in l. 471 to 472 by a statement of the measured agreement, and "compelling evidence" in l. 353. |
| Status | verified (text and page image p. 19) |
| Severity | major |
| Source | S3, S4, SD |

**GB-39 The stress sections in Fig. 7h to 7n reach an elevation of about 1416 m on their own axis, while the model is stated to be 1121 m high.**

| Field | Content |
|---|---|
| Check | P3 |
| Location | Fig. 7h to 7n (p. 18); p. 9, l. 181 to 182 |
| Quotation | "The whole model contains 25345 blocks, 2788 m long, 3341 m wide, 1121m high" |
| Concern | In Fig. 7h the vertical ticks 0 to 1200 lie at 1235.5 to 994.5 px (4.98 m/px); the highest red pixel of the section is at 951 px, i.e. 1416 ± 10 m. The horizontal axis (ticks every 64.3 px, 4.67 m/px) ends at 2860 ± 10 m against a model length of 2788 m. The ratio of the axis scales is 0.94, so the section is close to undistorted. Either the axis is offset, the section is not of the described model, or the stated model height is wrong; Fig. 4 and 7a to 7g label the vertical axis only up to 800 m. |
| Suggestion | State in the caption of Fig. 7 where the section runs and what the vertical axis measures, and correct either the axis or the model dimensions in l. 181 to 182. |
| Status | verified (section height and length measured); inferred (which value is wrong) |
| Severity | moderate |
| Source | AB |

**GB-40 The comparison of collisions, received energy and travel distance between parts of the mass, stated in the Abstract and Conclusion 4, is not reported, and the counts by travel distance are not normalised and grow with distance by construction.**

| Field | Content |
|---|---|
| Check | P11, P2, P21, P15, P9, P34, P31 |
| Location | p. 22, l. 414 to 421; Fig. 10b (p. 23); p. 3, l. 85 to 87; p. 13, l. 256 to 258 and Table 2; Fig. 9 (p. 21 to 22); p. 20, l. 397 to 399; p. 1, l. 28 to 30 (Abstract); p. 26, l. 483 to 487 (Conclusion 4) |
| Quotation | "Compared with the upper rock mass, the lower rock mass is compressed more frequently, receives more energy transfer, and has a longer migration distance." (l. 28 to 30); "during the collapse stage, the front portion of the rock mass experiences more collisions than the rear portion, with a clear trend of decreasing collision frequency toward the rear" |
| Concern | The comparison is announced (l. 85 to 87), and ten blocks in four positions (Table 2) suit it, but the results leave the cells empty. (a) Collisions per block or position are not reported; Fig. 10b plots "Frequency" against travel distance in 26 bins of 100 m, without block identity, position or time axis, so it cannot show a trend "toward the rear" or a pattern "during the collapse stage". (b) Travel distances of the blocks are not stated, only drawn in Fig. 10a. (c) Energy received is not quantified: Sect. 3.2.2 explains the rebounds of Blocks 1 and 3 by bouncing to the opposite bank, i.e. by a rise of PE, not by energy from the rear, and Fig. 9i shows a slight PE rise for the top block 9 as well. A block that travels farther passes more bins and accumulates more peaks, and the long paths end in the channel where the mass converges; distance, time in motion and location are confounded, and the direction of cause in "enabling the front portion to slide farther" cannot be read from the association. Block volumes differ by a factor of 2.32, so absolute block energies are not comparable: read from the axes, the totals of blocks 9, 10 and 7 (about 1.6, 0.95 and 1.18 GJ) against blocks 1 and 2 (about 5.05 and 5.1 GJ) are 0.81, 0.43 and 0.29 against 2.34 and 2.17 kJ/kg. The ten blocks are 0.04 % of 25345 blocks, placed "to capture representative kinematics" (l. 257) without a stated rule, two or three per class. |
| Suggestion | Add to Sect. 3.2.2 a table per monitored block (ID, position, travel distance, effective collisions, collisions per 100 m and per second in motion, number and size of mechanical-energy gains in J/kg) aggregated by the four positions of Table 2, preferably for all blocks or a sample stratified by initial position, by the stage windows of Fig. 7 and with the contact work on each block; state in l. 256 to 258 how the ten blocks were chosen; align the Abstract (l. 28 to 30) and Conclusion 4 with this table, or present them as a hypothesis. |
| Status | verified (absence of position-wise results; axes of Fig. 10b at page image p. 23; Table 2 volumes); inferred (counting effect; normalised values from Fig. 9 read from the axes; share 0.04 %) |
| Severity | major |
| Source | S3, S4, SD |

**GB-41 Sect. 3.4 attributes the energies of Fig. 12 to the "monitored block group", while the caption and the values indicate the whole sliding mass.**

| Field | Content |
|---|---|
| Check | P20 |
| Location | p. 24, l. 442 to 443, l. 445 to 447 and l. 451 to 452; Fig. 12 caption (p. 25, l. 458) |
| Quotation | "the sharp rise of DE shown in the figure further confirms significant fragmentation and disintegration in the monitored block group" |
| Concern | The initial PE in Fig. 12 (about 6500 GJ, read from the axis) equals the total of Fig. 8 (whole mass), while the ten monitored blocks together hold about 43.5 GJ (sum of the Fig. 9 totals). The caption reads "Fig12. Overall energy variation of the sliding mass". The unit of analysis thus changes from the whole mass (figure) to the monitored blocks and to a single "target block" (l. 446 to 447) within one paragraph. |
| Suggestion | In l. 452 replace "monitored block group" by "whole sliding mass" if that is meant, and keep the unit of analysis fixed in Sect. 3.4. |
| Status | verified (wording, caption); inferred (unit from values read from the axes) |
| Severity | minor |
| Source | S3 |

**GB-42 Fragmentation, debris production and a solid to fluid transition are read from envelope volume, envelope area and DE, none of which measures them.**

| Field | Content |
|---|---|
| Check | P31, P10, P15 |
| Location | p. 24, l. 445 to 452; p. 25, l. 453 to 456; Fig. 12 (p. 25); p. 23, l. 429 to 431; p. 14, l. 270 to 272; p. 9, l. 178 to 181; p. 26, l. 488 to 492 (Conclusion 5) |
| Quotation | "These newly generated fragments fill the interior and surface of the deposit mass, causing a sudden expansion of the envelope volume and a sharp increase in surface area." (l. 448 to 450); "collisions and friction cause blocks to fracture and disintegrate, generating a large amount of debris" |
| Concern | In Sect. 3.4 the mechanism is introduced as an interpretation ("This phenomenon can be interpreted as follows", l. 445); in Conclusion 5 it becomes "it can be concluded". The model consists of blocks of fixed size (8.7 m × 8.7 m columns with "a uniform structural plane", l. 178 to 181); no breakage rule, fragment count or size distribution over time is reported, so "newly generated fragments" are not shown to exist in the model. The x axis of Fig. 12a extends to about 1200 % volume swelling, an envelope about 13 times the initial volume; filling by fragments of a constant rock volume cannot produce this, whereas spreading of the blocks over the valley floor can, and Sect. 2.4 itself introduces VS and AG as measures of "dispersal degree" (l. 270). DE as defined in Eq. (4) is the residual of all gains and losses (GB-29) and cannot confirm fragmentation. The values 29.47 % and 319.5 % are VS and AG at the marked kinetic energy maximum; no criterion for a "solid phase" or "fluidized phase" (for example solid fraction or inertial number) is defined, so the transition is a label for the KE peak, and "indicating an increased collision frequency" (l. 455) is not backed by a collision count at that time. Since VS, AG and DE all increase with time, their joint rise does not show a coupling beyond common time dependence. |
| Suggestion | Report over time the number of separate blocks or contact-connected clusters and, if breakage is modelled, the fragment count and size distribution; define a phase criterion from model output and test whether its change coincides with VS 29.47 %; until then describe VS and AG in Sect. 3.4 (l. 445 to 456) and Conclusion 5 (l. 488 to 492) as measures of spreading, replacing "fracture and disintegrate, generating a large amount of debris" by "separate and disperse". Could blocks break in the 3DEC model? |
| Status | verified (absence of fragmentation measures and of a phase criterion; fixed block size, l. 178); inferred (growth to about 1200 % read from the axis); assumption (whether blocks could break in the model, posed as question) |
| Severity | major |
| Source | SD, S4 |

**GB-43 The kinetic energy peak marked in Fig. 12 (1116.8 GJ at VS 29.47 % and AG 319.5 %) is not the peak of the same series in Fig. 8 (about 1685 GJ); Fig. 12 omits the time steps with the highest kinetic energy, and the time of the transition is not stated.**

| Field | Content |
|---|---|
| Check | P3, P22 |
| Location | p. 24, l. 452 to p. 25, l. 455; Fig. 12a and 12b, annotations "1116.8", "29.47", "319.5" (p. 25, caption l. 458 to 459); Fig. 8 (p. 20, caption l. 390); p. 19, l. 381 to 383; Fig. 11 caption (p. 24, l. 438 to 439) |
| Quotation | "When the volume expansion rate reaches approximately 29.47% and the surface area growth reaches about 319.5%, it can be considered that the landslide transitions from a solid phase to a fluidized phase. At this point, the kinetic energy peaks" |
| Concern | Fig. 8 and Fig. 12 show the same quantities for the entire sliding mass, both starting at about 6500 GJ. Measured in Fig. 8 (9.58 GJ/px; 105 bars at 1.245 s): KE per bar rises to 1082 GJ (about 11.2 s), 1590 GJ (about 12.4 s) and 1685 GJ (about 13.7 s), then falls to 824 and 488 GJ (±30 GJ); an independent measurement gives about 1666 GJ at about 13 s, and the KE band of about 1700 GJ at 13 to 14 s is visible on the page image. The largest KE in Fig. 12 is the labelled 1116.8 GJ. Matching the markers of Fig. 12a to the bars of Fig. 8 by their PE values gives a one-to-one match to bars 2, 5, 8, 11, 14, ... (for example PE 4983 GJ at VS 29.5 % to bar 8 with 4994 GJ); the 1116.8 GJ marker corresponds to bar 8 (1082 ± 30 GJ), and bars 9 and 10, which carry the peak (1685 GJ is 51 % above 1116.8 GJ), are not plotted. The statement that KE peaks at VS 29.47 % and AG 319.5 %, and with it the transition threshold, therefore refers to the largest sampled value, not to the peak of the series. In addition, the reader learns the time of this point only by combining l. 381 to 382, Fig. 12 and the time list of Fig. 11, and VS and AG are given with different precision (two and one decimals). Graded major because the threshold values are a quantitative result of Sect. 3.4 and would move to the VS and AG at about 13.7 s, which the manuscript does not report. |
| Suggestion | Plot all time steps of Fig. 8 in Fig. 12 (at least those at about 12.4 and 13.7 s), state the time of each point, recompute VS and AG at the true KE maximum and state its simulation time in l. 453 to 455, with VS and AG at the same precision. |
| Status | verified (values measured in Fig. 8 and Fig. 12 by two instances; peak in Fig. 8 confirmed at page image p. 20 during merging); inferred (correspondence of Fig. 12 markers to every third bar of Fig. 8) |
| Severity | major |
| Source | AB, S3 |

#### Minor corrections

| ID | Location | Quotation | Replacement | Source |
|---|---|---|---|---|
| KK-38 | Fig. 7h to 7n, colour-bar labels (p. 18) | "-33Mpa" | "−33 MPa" (likewise "0 MPa", "−31 MPa", "−47 MPa") | AB |
| KK-39 | p. 20, l. 397 to 398 | "exhibit a rebound in potential energy after it approaches zero" | "exhibit a rebound in potential energy after their potential energy approaches zero" | S4 |
| KK-40 | Fig. 9 caption, p. 22, l. 410 to 413 | "(a) energy evolution of point 1 ; (b) energy evolution of point 2 ;" | "(a) monitoring point 1; (b) monitoring point 2;" and so on, without space before the semicolon | AB |
| KK-41 | p. 23, l. 425 | "3.4 Structural evolution as a function of energy change" | "3.3 Structural evolution as a function of energy change" (Sect. 3.2.2 is followed by 3.4; there is no 3.3) | S3, S4 |
| KK-42 | Fig. 11 caption, p. 24, l. 438 to 439 | "(a-i) when time = 0s, 3s, 7s, 9s, 12s, 15s,32s,71s, 100s, 131s." | "(a) to (j) at t = 0, 3, 7, 9, 12, 15, 32, 71, 100 and 131 s." (ten panels, ten times) | S3, S4, AB, SD |
| KK-43 | Fig. 12 caption, p. 25, l. 458 to 459 | "(a) as a function of volume; (b) as a function of area." | "(a) as a function of volume swelling VS; (b) as a function of area growth AG." (axis titles "Volume Swelling (%)" and "Area Growth (%)") | S4 |

#### Verification log

| ID | Check | Checked | Values | Result |
|---|---|---|---|---|
| PP-28 | P2, P24, P3 | Duration of the run and time course of Fig. 8 against the text | 131 s in l. 300 to 301; last panels of Fig. 7g and 7n at 131 s; Fig. 11j at 131 s; Fig. 8: 105 bars, period 8.578 px = 1.245 s, axis end about 131 s; KE 0 until 3.7 s, 144 GJ at 5.0 s, 1082 at 11.2 s, 1590 at 12.4 s, 1685 at 13.7 s, 824 at 14.9 s (±30 GJ); PE below 120 GJ from about 71 s, 0 from about 108 s; total 6526 GJ in all bars; text: initiation 3 to 12 s, KE peak, drop around 13 s; disclosed: dam breach after 131 s not modelled (l. 348 to 350) | consistent within one bar width, no finding |
| PP-29 | P2, P3, P24 | Stage velocities of Sect. 3.1 against the colour bars of Fig. 7 and the energy timeline of Sect. 3.2.1 | text 5.9 (3 s, l. 307), 19.6 (7 s, l. 315), 27.1 (9 s, l. 322), 31.6 (12 s, l. 330), 25.7 m/s (15 s, l. 339), approaching 0 (131 s); colour bars a 0, b 5.9, c 19.6, d 27.1, e 31.6, f 25.7, g 0.21 m/s; stress bars h 0, i -33, j -31, k -33, l -33, m -33, n -47 MPa (not discussed); peak between 12 and 15 s agrees with l. 337 | consistent, no finding |
| PP-30 | P36 | Statements with "about", "nearly", "around" against records in the manuscript | "nearly 20 large and super large earthquake landslides" (l. 99 to 100): no record to compare; "Around 13 seconds, the sliding mass impacted the riverbed" (l. 383) against Fig. 8: KE maximum at about 13 s (about 1666 GJ), about 804 GJ at about 14 s; 31.6 m/s at 12 s against "peak upon arrival at the valley floor" (l. 337) | consistent, no finding |
| PP-31 | P19 | Provenance class of the core energy statements | Fig. 8, 9 and 12 rest on 3DEC kinematics combined with the restored terrain (model-generated data), named "numerical simulation results"; 4 of 5 conclusions (2 to 5) rest on model-generated data = 80 %; historical flood record (l. 110 to 112) attributed to the event; disclosed: no instrumental data for 1786 (l. 184 to 185) | class named; separate finding GB-37 |
| PP-32 | P3, P24 | Rebounds of blocks 1 and 3 (l. 397 to 399, l. 415 to 416) against Fig. 9 and Fig. 10a | PE + KE rises above 2 px only in panels a (6, total 0.43 GJ, minimum 0 at about 72 s, end 0.34 GJ), c (11, 0.49 GJ, end 0.32 GJ), g (1, 0.014 GJ) and i (2, 0.022 GJ); Fig. 10a cannot confirm the rebounds because a vertical rise cannot be separated from movement towards the viewer | consistent with the text, no finding |
| PP-33 | P3 | Distinguishability of the ten line colours in the legend of Fig. 10a | 1 #f96862, 2 #6c68fa, 3 #ca63d4, 5 #241c67, 6 #8034c3, 7 #7c3f81, 8 #743642, 9 #91984b, 4 green and 10 light blue distinct by eye; closest pairs 6 and 7: 81, 7 and 8: 80, all above 40 | no finding |
| PP-34 | P2, P24 | Time points of Fig. 7 and Fig. 11 against the text | Fig. 7a to 7g and 7h to 7n: seven times each (0, 3, 7, 9, 12, 15, 131 s), seven panels each; Fig. 11: ten times (0, 3, 7, 9, 12, 15, 32, 71, 100, 131 s), ten panels, matching "10 representative time points" (l. 427); only the caption letter range is wrong (KK-42) | consistent, no finding |
| PP-35 | P2, P3 | Values in the text of Sect. 3.4 against the annotations of Fig. 12 | VS 29.47 % (l. 453) and annotation "29. 47"; AG 319.5 % and annotation "319. 5"; KE annotation 1116.8 GJ identical in (a) and (b), reference line at 1117 GJ; marker positions VS 29.5 % (±2.5 %) and AG 320.1 % (±8.8 %); initial PE in Fig. 12 and total in Fig. 8 both about 6500 GJ; Vt/V0 = 1.2947, St/S0 = 4.195 | text and annotations agree; comparison with Fig. 8 in GB-43 |

### Segment 4: Conclusions, declarations, references (p. 25 to 29)

#### Substantive findings

**GB-44 The Conclusions do not return to the stated aims, do not carry the limitations disclosed in the methods into the conclusions, and give no outlook.**

| Field | Content |
|---|---|
| Check | P15 |
| Location | p. 25, l. 460 to p. 26, l. 492; p. 2, l. 65 to 73; p. 5, l. 122 to 125; p. 9, l. 176 to 178; p. 10, l. 183 to 191; p. 16, l. 348 to 350; p. 11, l. 232 to 233; p. 14, l. 281 to 284 |
| Quotation | "The findings are intended to provide a theoretical foundation and scientific support for early warning and risk mitigation of high-altitude and long-runout landslides triggered by intense earthquakes." |
| Concern | The manuscript discloses several limitations itself: structural planes ignored (l. 176 to 178), ground motion substituted by the 2008 Wenchuan record (l. 183 to 191), dam break not modelled (l. 348 to 350), the 30 % threshold "deemed acceptable" by visual comparison (l. 232 to 233), α fixed at 1 (l. 281 to 284). None appears in the Conclusions, which speak of "the landslide" and "the front portion of the rock mass" in general terms from one simulation with one input. The aims of l. 69 to 73 (movement trajectory, spatiotemporal evolution of velocity, propagation characteristics; early warning and risk mitigation) and the hazard motivation of l. 122 to 125 are not answered; the velocity results (5.9 to 31.6 m/s, 131 s) and the transition values of l. 453 to 454 do not appear. There is no outlook. |
| Suggestion | Add to Sect. 4 one paragraph on scope (single event, substituted input, no structural planes, single threshold and α), one sentence per stated aim with the corresponding result, and an outlook (for example sensitivity runs for input motion, threshold and α). |
| Status | verified |
| Severity | moderate |
| Source | S4 |

**GB-45 Data and code are withheld "upon reasonable request" without a reason, although no personal data are involved.**

| Field | Content |
|---|---|
| Check | P12 |
| Location | p. 26, l. 494 to 495 and l. 505 to 506 |
| Quotation | "The codes that support the findings of this study are available from the first author, Yunfeng Ge, upon reasonable request." |
| Concern | The manuscript has both a code and a data statement. The study produces at least: the restored pre-landslide terrain (l. 138 to 143, Fig. 3c); the 3DEC model and input files (l. 169 to 202, Table 1); the histories of the ten blocks and the global energy series (l. 256 to 264, Fig. 8, Fig. 9); the peak-detection routine with the list of 1,139 effective collisions (l. 226 to 234); the alpha-shape routine and the envelope volumes and areas (l. 281 to 283, Fig. 11, Fig. 12). None concerns persons. Both statements give no reason for withholding and no repository or link, and there is no supplement or appendix. |
| Suggestion | Deposit the restored DEM, the 3DEC input files, the block histories, the envelope series and the scripts for peak detection and alpha shape in a public repository with a persistent identifier and cite it in l. 494 to 495 and l. 505 to 506; for any item that cannot be released, name it and give the reason. |
| Status | verified (text p. 26; absence of appendix and supplement checked on all 29 pages) |
| Severity | moderate |
| Source | S2 |

**GB-46 Fifteen of the 29 in-text citation keys have no entry in the reference list.**

| Field | Content |
|---|---|
| Check | P4 |
| Location | reference list, p. 26, l. 507 to p. 29, l. 605; citations p. 1, l. 34 to 37 and p. 2, l. 45 to 63 (l. 45 to 46 "Zhang et al., 2024", "Fan et al., 2020"; l. 53 to 54 "Huang et al., 2012", "Intrieri et al., 2018"; l. 56 "Huang et al., 2019"; l. 58 to 59 "Zhu et al., 2010", "Zhang et al., 2020a, b", "Cuomo et al., 2021", "Shugar et al., 2021"; l. 62 to 63 "Navarre et al., 2009", "Van Herwijnen and Schweizer, 2011", "Helmstetter and Garambois, 2010", "Cook et al., 2021", "Pandey et al., 2021") |
| Quotation | "In recent years, landslide seismology has taken on more visibility (Navarre et al., 2009; Van Herwijnen and Schweizer, 2011; Helmstetter and Garambois, 2010; Cook et al., 2021; Pandey et al., 2021)." |
| Concern | The Introduction carries the whole literature basis; no citation occurs after l. 74. Of 29 author-year keys ("2020a" and "2020b" counted separately) held against the 31 entries, 7 match exactly, 3 match with a form error (KK-07, KK-14, KK-15), 2 are ambiguous (KK-05), 2 differ in year from a unique entry of the same first author (KK-08, KK-16) and 15 have no entry, 15 / 29 = 51.7 %. "Fan et al., 2020" may refer to Fan, Yang et al. (Landslides 17, listed as 2019) and "Zhang et al., 2024" to Zhang, J. et al. (Landslides 21, listed as 2023), but neither can be assigned with certainty. The remaining 13 keys, including all five landslide-seismology sources on which the gap of l. 63 to 64 rests (GB-05), have no candidate. |
| Suggestion | Add full entries for the 15 keys to the reference list (p. 26 to 29), or remove the citations; for "Fan et al., 2020" and "Zhang et al., 2024" make citation year and entry year agree. |
| Status | verified (absence of entries); inferred (possible intended entries for Fan 2020 and Zhang 2024; share calculated) |
| Severity | moderate |
| Source | S4 |

**GB-47 Sixteen of the 31 reference list entries are never cited, among them a study of the Mogangling landslide and the first author's earlier study of energy evolution.**

| Field | Content |
|---|---|
| Check | P4 |
| Location | p. 26, l. 508 to 510 (Bernardie et al. 2021) and l. 514 to 516 (Chang et al. 2022); p. 27, l. 517 to 520 (Chen et al. 2024), l. 524 to 526 (Dahal et al. 2022), l. 537 to 539 (Gao et al. 2023), l. 540 to 542 (Ge et al. 2021), l. 543 to 545 (Gong et al. 2024), l. 546 to 548 (He, J. et al. 2023), l. 549 to 552 (He, K. et al. 2022), l. 553 to 555 (He, N. et al. 2023); p. 28, l. 562 to 565 (Nava et al. 2025), l. 566 to 568 (Sinčić et al. 2025), l. 588 to 590 (Wu, J. et al. 2013), l. 591 to 593 (Yang et al. 2022); p. 29, l. 597 to 599 (Zhang, K. et al. 2019), l. 603 to 605 (Zhou et al. 2024) |
| Quotation | "Wu, J., Wang, Y., Dong, S., Chen, Y., and Wang, L.: Genetic Mechanism and Failure Process of the Mogangling Seismic Landslide, J. Geol. Soc. India, 82, 277-282" |
| Concern | 16 of 31 entries (51.6 %) have no citation in the text (17 if "Zhang et al., 2024" does not refer to Zhang, J. et al.). Among them are Wu et al. (2013) on the failure process of the Mogangling landslide, Ge et al. (2021) on mechanical energy evolution of rock avalanches by the first and third authors, and Zhou et al. (2024) on earthquake-triggered landslides in Moxi Town, the closest prior work, neither cited nor discussed (see GB-05). Five uncited entries (Bernardie, Dahal, Nava, Sinčić, Zhang, K.) are set in lighter grey, unjustified type (KK-47). |
| Suggestion | Cite each entry where it supports a statement, in particular Wu et al. (2013), Zhao et al. (2021) and Ge et al. (2021) in the Introduction and Sect. 2.1, or delete the entries that are not used. |
| Status | verified; inferred (share calculated) |
| Severity | minor |
| Source | S4 |

#### Minor corrections

| ID | Location | Quotation | Replacement | Source |
|---|---|---|---|---|
| KK-44 | p. 25, l. 464 and 466 | "It should be noted that:(a)"; "restoring the contours;(b)" | "It should be noted that: (a)"; "restoring the contours; (b)" | S4 |
| KK-45 | p. 26, l. 504 | "We thank editors and anonymous reviewers for their valuable comments." | delete the sentence in the discussion preprint, or add it after review | ZF |
| KK-46 | p. 26, l. 507 (heading) | "Reference" | "References" | S4 |
| KK-47 | p. 26, l. 508 to 510; p. 27, l. 524 to 526; p. 28, l. 562 to 565 and 566 to 568; p. 29, l. 597 to 599 | entries "Bernardie, S., ...", "Dahal, A., ...", "Nava, L., ...", "Sinčić, M., ...", "Zhang, K., ..." (set in lighter grey, unjustified type on the page images) | the same black, justified type as all other entries, or deletion (GB-47) | S4 |
| KK-48 | p. 27, l. 530 | "Fan, X., Scaringi, G., Korup, O., et al.:" | "Fan, X., Scaringi, G., Korup, O., West, A. J., van Westen, C. J., Tanyas, H., Hovius, N., Hales, T. C., Jibson, R. W., Allstadt, K. E., Zhang, L., Evans, S. G., Xu, C., Li, G., Pei, X., Xu, Q., and Huang, R.:" (all other entries list all authors; author list from the repository record https://orca.cardiff.ac.uk/123110) | S4 |

#### Verification log

| ID | Check | Checked | Values | Result |
|---|---|---|---|---|
| PP-36 | P15 | Each of the five conclusions against a place in Sect. 3 or Sect. 2, and verbs against evidence | C1 (l. 463 to 468) to l. 136 to 162 and Fig. 3: rules (a) and (b) not applied (GB-14); C2 (l. 469 to 475) to Sect. 3.1 and Fig. 7o: qualitative only (GB-38), "geological structures" not covered (GB-36), collision identification described in Sect. 2.2 (GB-24); C3 (l. 476 to 482) to Fig. 8 and 9: identity of Eq. 4 (GB-29); C4 (l. 483 to 487) to Fig. 10b: no position-wise result (GB-40); C5 (l. 488 to 492) to Fig. 12: interpretation turned into conclusion (GB-42); overstating verbs in Sect. 3: "It is evident" (l. 375), "it is clear that" (l. 418), "further confirms" (l. 451), "presents compelling evidence" (l. 353); disclosed limits not carried into the conclusions (GB-44) | findings GB-14, GB-24, GB-29, GB-36, GB-38, GB-40, GB-42, GB-44 |
| PP-37 | P4 | Numbering of sections, figures, tables and equations | Sections 1 (l. 31), 2 (l. 74), 2.1 (l. 92), 2.2 (l. 214), 2.3 (l. 240), 2.4 (l. 269), 3 (l. 297), 3.1 (l. 298), 3.2 (l. 371), 3.2.1 (l. 372), 3.2.2 (l. 391), 3.4 (l. 425), 4 (l. 460); Fig. 1 to 12 each once; Tables 1 (p. 11) and 2 (p. 13); Eq. (1) to (6) on p. 12 to 14; no appendix, no supplement | one gap, Sect. 3.3 (KK-41) |
| PP-38 | P4 | Every reference to a figure, panel or table at its target | Fig. 1 (l. 76): four blocks against three parts (GB-08); Fig. 2c and 3 (l. 159 to 160): GB-17; Fig. 4 (l. 173): 1021, 747, 179, 131 m as in l. 174 to 175; Table 1 (l. 212) present; Fig. 5a red and purple markers as in l. 222 to 223; Fig. 6 and Table 2 (l. 256, 259) present; Fig. 7 (l. 301 to 353) panel maxima as in the text; Fig. 8 (l. 375, 387); Fig. 9 (l. 393) ten panels; Fig. 10a and 10b (l. 414, 418); Fig. 11 (l. 428) ten panels (KK-42); Fig. 12 (l. 443) axes VS and AG (KK-43) | all other references reach their target |
| PP-39 | P4 | Citations against the reference list in both directions | 29 in-text keys (all in l. 34 to 63), 31 entries; exact 7, form error 3, ambiguous 2, year mismatch 2, no entry 15; entries never cited 16 (17 if Zhang, J. 2023 is not meant by "Zhang et al., 2024"); list in alphabetical order; Fan, Scaringi et al. the only entry with "et al."; DOIs not resolved (optional check) | GB-46, GB-47, KK-05, KK-07, KK-08, KK-15, KK-16, KK-48 |
| PP-40 | P16 | Observations from the extracted text that could be extraction artefacts, at the page images | equation characters missing in the text layer at l. 245 to 249 and 276 to 277 are "=", "+", minus and "×" on the images; "c Author(s)" is "©"; superscripts in "km2" (l. 150) and "m3" (l. 151, 182, Table 2) are set as superscripts, only the exponent in "104" (l. 151) is on the baseline (KK-27); "potential / discontinuities" in Table 1 is a two-line cell; wide spacing in the reference list (l. 535, 541, 551, 560, 583, 589, 601) is justified type | one character finding (KK-27) and one typesetting finding (KK-47), otherwise artefacts |

## Optional checks

| Area | What it needs | Responsible | Run |
|---|---|---|---|
| DOI resolution | one request per reference list entry | `science-quellenapparat-pruefung` | no |
| Citation style | the name of the style | `science-zitierstil-harvard-ctr` or the journal's style rules | no |
| AI statement against publisher policy | the publisher's policy on AI use | this review, on request | no |
| Relation to the authors' prior work | the authors' prior work | this review, on request | no |
| Journal requirements | the target journal's author guidelines | this review, on request | no |
| Factual correctness | access to the sources of every checked statement | `science-faktenbeleg-pruefung`, `geo-frage-belegbasiert-klaeren` | no |

## Limits of this review

- Checked version: egusphere-2025-4506.pdf, 29 pages, SHA-256 64cb3787456244aa6102e34f776b47e9a612d06e8894d391758ae240dbe415d6.
- Review instances: S1 to S4, AB and SD ran as separate agents without context from each other; their results were merged in a separate step.
- Sources not readable: Ge et al. (2021) (publisher page blocked, records without abstract), Cheng (2014) (not opened), Hu et al. (2017), Li et al. (2024) and Du et al. (2021) full texts (HTTP 429, metadata or abstracts only), Li et al. (2008) full text (abstract only); the publisher page of Jaboyedoff et al. (2019) was read by instance S1, but a second reading during merging was refused by the server (HTTP 429). Statements resting on these sources carry status inferred.
- Findings with status assumption: 12 of 47, each for a partial statement and posed as a question to the authors (GB-10, GB-12, GB-13, GB-14, GB-22, GB-23, GB-24, GB-26, GB-28, GB-30, GB-33, GB-42); GB-12 is formulated as a question as a whole.
- Merging: 75 substantive findings from the six instances were checked for mandatory fields; 0 were discarded for missing fields. They were merged into 46 findings (29 merged into others), plus 1 finding from the merging step (ZF, GB-37). 72 minor corrections were merged into 48 (10 absorbed into substantive findings, 15 duplicates, 1 added by the merging step, KK-45). 46 verification log entries were merged into 40 (6 duplicates).
- Discarded: 0 findings for missing mandatory fields; 9 notes outside the checklists were not adopted, because a responsible instance had already treated the passage without a finding (5) or because the merging check did not confirm a defect or no check type covered it (4).
- Optional checks run: 0 of 6.
