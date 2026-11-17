# Review report: Energy and structural evolution process of high-altitude and long-runout landslides induced by a strong earthquake

| Field | Value |
|---|---|
| Manuscript | Ge, Y., Hu, B., Tang, H., Fu, X., and Zhu, L. (2025): Energy and structural evolution process of high-altitude and long-runout landslides induced by a strong earthquake, EGUsphere preprint egusphere-2025-4506, https://doi.org/10.5194/egusphere-2025-4506 |
| Checked version | egusphere-2025-4506.pdf, 29 pages, SHA-256 64cb3787456244aa6102e34f776b47e9a612d06e8894d391758ae240dbe415d6 |
| Date | 2026-10-17 |
| Language | English |
| Review instances | Segments 1 to 4, figures, study design; the six review instances ran as separate agents without shared context, and the merge was done by a seventh agent |

## Summary

The manuscript is a single-case numerical back-analysis of the 1786 Mogangling rock avalanche on the right bank of the Dadu River (Luding County, Sichuan), triggered by the Kangding earthquake (Ms 7¾). The pre-failure topography is restored by straightening the contour lines of a UAV-derived DEM across the scar, and the event is simulated with the three-dimensional discrete element code 3DEC (25345 blocks, model 2788 m × 3341 m × 1121 m, landslide volume 317563 m³ against a field estimate of about 2400×10⁴ m³), driven by the acceleration record of the 2008 Wenchuan earthquake at Luding station. Kinetic, potential and dissipated energy are computed for the whole mass and for ten monitored blocks, with dissipated energy defined as the loss of mechanical energy since t0 (Eq. 4); "effective collisions" are detected as velocity peaks above a 30 % prominence threshold (1,139 detections); and an alpha-shape envelope (α = 1) gives volume swelling (VS) and area growth (AG) at ten time points. Key numbers are a duration of 131 s, a maximum velocity of 31.6 m/s at 12 s, and a kinetic-energy peak of 1116.8 GJ at VS 29.47 % and AG 319.5 %, read as a solid-to-fluid transition. Five conclusions concern the restoration method, the value of the simulation, energy conservation of the whole mass versus non-conservation of single blocks, more collisions of the front than of the rear mass, and fragmentation as the cause of envelope growth.

## Strengths

1. The energy terms are defined explicitly per block from mass, velocity and elevation (Eq. 1 to 4, l. 241 to 255), and the same three terms are used consistently in the text, Fig1, Fig8, Fig9 and Fig12 (PP-21, PP-29); every plotted energy can therefore be traced to a formula, which is what allowed the review to show where the energy statements follow from the definitions (GB-42).
2. The kinematic stages of Sect. 3.1 are tied to figure panels with numbers: the six stage velocities in the text equal the colour-bar maxima of Fig7 (b) to (g), and the duration of 131 s agrees across text, Fig7, Fig8, Fig9 and Fig11 (PP-27, PP-25); a reader can follow the run stage by stage.
3. The location and geometry figures carry graticules, scale bars and a section line whose azimuth (74.1°) matches the stated sliding direction of 75°, and the dimension labels of Fig4 match the text (PP-12, PP-17); this made the positional and dimensional checks in GB-08 and GB-13 possible.
4. The manuscript names its main modelling limits where it introduces the model (structural planes ignored, surrogate ground motion, dam break not modelled, α fixed) and shows the collision detector at five thresholds side by side in Fig5 (PP-37, PP-07, PP-18); a reader can see the scope of the model and how the detector reacts to the threshold.

## Weaknesses

1. The energy results cannot carry the conclusions drawn from them. Conservation for the whole mass is an identity of Eq. (4), and the non-conservation claimed for single blocks is contradicted by the constant totals of Fig9 (GB-42); the stated potential-energy datum is not the one plotted (GB-27); and the absolute energies fit none of the stated landslide volumes (GB-13). Suggestion: state that DE is a residual, replace the conservation statements by an independent energy budget from 3DEC (seismic input work, boundary absorption, frictional and damping work) with its closure error, and state the mass and the datum used for Fig8, Fig9 and Fig12.
2. Several headline statements are not backed by reported results: the front versus rear collision and energy-transfer result of the Abstract and Conclusion 4 (GB-44), the fragmentation mechanism of Conclusion 5 (GB-47), the solid-to-fluid transition values, which belong to a point before the kinetic-energy maximum of Fig8 (GB-48), the seismic wave mechanisms of Sect. 3.1 (GB-38), and the restoration rules of Conclusion 1 (GB-49). Suggestion: add per-block and per-zone tables of collisions and energy, a fragmentation measure from the model, VS and AG recomputed at the actual kinetic-energy maximum, and acceleration outputs, or restrict these statements to what the results show.
3. The design rests on one realisation whose components are not tested: one run with one parameter set and one surrogate record (GB-02, GB-18), a collision detector calibrated by eye on an unidentified curve without comparison with contact events (GB-22, GB-26), an untested α (GB-34), an untested restoration (GB-49) and a qualitative validation (GB-39). Suggestion: a small ensemble over the uncertain inputs, a contact-force check of the detector with precision and recall, an α sensitivity, and a quantitative comparison of the simulated deposit with the mapped one.
4. Several findings of moderate grade limit reproducibility and the literature framing: model settings, parameter sources, third-party data and author data are not reported or not available (GB-11, GB-17, GB-19, GB-50); counts and indices lack their base (GB-25, GB-33, GB-46); objects carry several names and some figure labels contradict the text (GB-09, GB-24, GB-28, GB-31, GB-32, GB-08); and 14 citations have no entry while cited works do not support their sentences and the research gap ignores published energy studies (GB-01, GB-03, GB-05, GB-07, GB-51). Suggestion: a table of numerical settings, a public repository with persistent identifier, one naming scheme throughout, a revised reference list, and a research gap restated against the uncited prior work, including the first author's own energy study.

## Findings by segment

### Segment 1: Title, abstract, introduction (p. 1 to 2, l. 1 to 73)

#### Substantive findings

**GB-01 The two works cited for a rising frequency of earthquake-induced rock landslide chains do not state such a trend.**

| Field | Content |
|---|---|
| Check | P13 |
| Location | p. 1, l. 33 to 34; reference list p. 26, l. 511 to 513 and p. 27, l. 530 to 536 |
| Quotation | "In recent years, the chain disasters of high-level rock landslides in high-intensity earthquake areas have shown a trend of frequent occurrence (Carpignano et al., 2009; Fan et al., 2019a)" |
| Concern | The opening rightly places the study among earthquake-induced hazard chains, but the two works cited for the trend do not support it. Carpignano et al. (2009) present a methodology for regional multi-risk maps for the Piedmont Region as a decision support system; abstract and bibliographic record contain nothing on earthquake-induced landslide chains or on a temporal trend. The abstract of Fan et al. (2019, Rev. Geophys., 57, 421-503) speaks of an increased frequency of landslides that lasts for decades after a large earthquake, that is, a post-seismic decay, not a trend of more frequent chain disasters in recent years. In addition, "Fan et al., 2019a" cannot be resolved, because the list holds two entries Fan et al. 2019 (l. 530 to 532 and l. 533 to 536) without letters (KK-07). |
| Suggestion | In l. 33 to 34 either cite a work that documents an increase in the frequency of such events, with period and region, or reword the sentence to what the sources say (large earthquakes trigger hazard chains whose activity persists for years to decades, Fan et al., 2019a); remove Carpignano et al. (2009) from this sentence. |
| Status | topic of Carpignano et al. (2009): verified (abstract and record read by instance S1); statement of Fan et al. (2019): inferred (abstract only, full text not readable); ambiguity of "2019a": verified (page images p. 1 and p. 27) |
| Severity | moderate |
| Source | S1 |

**GB-02 A single simulation run without sensitivity analysis is used to state general laws and a basis for early warning.**

| Field | Content |
|---|---|
| Check | P10 |
| Location | p. 2, l. 39 to 41 and l. 71 to 73; p. 11, l. 206 to 207 and Table 1; p. 25 to 26, l. 461 to 492 |
| Quotation | "so as to summarize the law of high-level rock landslide induced by earthquake" and "provide a theoretical foundation and scientific support for early warning and risk mitigation" |
| Concern | The design has one case, one parameter set (Table 1, partly from "parameter inversion", l. 207), one block size (8.7 m), one input record, one α and one collision threshold; none is varied except the threshold, and that only on one curve (Fig5). A single realisation can describe this simulation, but it cannot yield a "law" for earthquake-induced rock landslides or a basis for early warning, and the effect of the uncertain inputs (inverted parameters, restored terrain, surrogate record, GB-18, GB-49) on runout, duration, energy partition and the VS and AG thresholds is unknown. The higher grade applies because the scope of every conclusion depends on it. |
| Suggestion | Counter-design for Sect. 2: a parameter study that varies friction and cohesion of the landslide mass and of the discontinuities within their uncertainty, block size, input record and α, and reports runout, duration, peak KE and the VS and AG thresholds as ranges. Otherwise restrict l. 39 to 41, l. 71 to 73 and the conclusions to the Mogangling simulation. |
| Status | verified (text, Table 1, Fig5) |
| Severity | major |
| Source | SD |

**GB-03 The claim that pre-failure terrain restoration is rare and that contour continuation is a new idea rests on no documented search, and a published study already restores pre-failure topography by modifying contour lines.**

| Field | Content |
|---|---|
| Check | P28, P14 |
| Location | p. 2, l. 42 and l. 49 to 51; p. 1, l. 16 to 17; p. 6 to 7, l. 136 to 142 and l. 157 to 162; p. 25, l. 463 to 468 |
| Quotation | "At present, in terms of surface terrain restoration, the terrain restoration before a landslide is less." and "which can provide a new idea of terrain restoration before a landslide for the same type of research" |
| Concern | The contour-based restoration is clearly described (l. 136 to 142, l. 157 to 162, Fig3) and is a practical step for an ancient event. The claim that such restoration is rare and that the approach is new, however, rests on no search: the manuscript names no database, search terms, period or date (no occurrence of "search", "Scopus", "Web of Science" or "CNKI"). A direct counterexample exists: von Wartburg, J., Ivy-Ochs, S., Aaron, J., Martin, S., Leith, K., Rigo, M., Vockenhuber, C., Campedel, P., and Viganò, A.: Constraining the age and source area of the Molveno landslide deposits in the Brenta Group, Trentino Dolomites (Italy), Front. Earth Sci., 8, 164, https://doi.org/10.3389/feart.2020.00164, 2020. In the section "Reconstruction of Pre-Failure Topography and Volume Analysis" the authors state that "we manually modified the contour lines in the source area to provide a smooth transition" and ran a 3-D runout model on the result. The work is not in the reference list (checked against all 31 entries). The grade is moderate because the simulation results do not depend on novelty, while the contribution claimed in l. 49 to 51 and Conclusion 1 does. |
| Suggestion | In l. 42 and l. 49 to 51 either document the search behind the rarity claim (databases, terms, period, date) or drop "new idea"; cite von Wartburg et al. (2020) after l. 49 and at l. 138 and state what the present procedure adds, for example the use of the restored surface as the sliding-mass geometry in 3DEC. |
| Status | missing search: verified (full text); counterexample: verified (full text read by instance S1; the quoted sentence re-checked on frontiersin.org) |
| Severity | moderate |
| Source | S1 |

**GB-04 The works cited for photo, field, remote sensing and UAV-based geomorphic mapping concern numerical simulation, and two of the four cannot be traced.**

| Field | Content |
|---|---|
| Check | P13 |
| Location | p. 2, l. 43 to 46; reference list p. 28, l. 569 to 571 and l. 585 to 587 |
| Quotation | "the key information of landslide characteristics is often obtained through photos, field surveys, optical remote sensing images and UAV impact, so as to further build geomorphic maps through GIS (Geographic Information System) for subsequent analysis" |
| Concern | Of the four citations, Fan et al. (2020) has no entry (the list holds only two Fan et al. 2019 entries), and Zhang et al. (2024) has no entry of that year; the only candidate is Zhang, J. et al. (2023) on the Da'ao landslide by InSAR and model simulation (KK-12). The two traceable works do not describe the stated practice: Song et al. (2017) build a 3-D numerical model of a Three Gorges reservoir landslide and validate it against GPS monitoring, without photos, UAV surveys or GIS geomorphic maps; Wu et al. (2024) is, by title and journal record, a numerical simulation of landslide-induced wave hazards. None of the traceable sources supports the sentence, and with it the contrast the paragraph draws between recent and ancient landslides. |
| Suggestion | In l. 43 to 46 replace Song et al. (2017) and Wu et al. (2024) by works that derive landslide characteristics from imagery, field mapping or UAV surveys, and add Fan et al. (2020) and the intended Zhang entry to the list or remove them. |
| Status | Song et al. (2017): verified (abstract read by instance S1); Wu et al. (2024): inferred (title and record only); missing entries: verified (page images p. 2 and p. 26 to 29) |
| Severity | moderate |
| Source | S1 |

**GB-05 Fourteen in-text citations have no entry in the reference list.**

| Field | Content |
|---|---|
| Check | P4 |
| Location | p. 2, l. 46 (Fan et al., 2020); l. 53 to 54 (Huang et al., 2012; Intrieri et al., 2018); l. 56 (Huang et al., 2019); l. 58 to 59 (Zhu et al., 2010; Zhang et al., 2020a, b; Cuomo et al., 2021; Shugar et al., 2021); l. 62 to 63 (Navarre et al., 2009; Van Herwijnen and Schweizer, 2011; Helmstetter and Garambois, 2010; Cook et al., 2021; Pandey et al., 2021) |
| Quotation | "(Zhu et al., 2010; Zhang et al., 2020a, b; Cuomo et al., 2021; Shugar et al., 2021)" and "(Navarre et al., 2009; Van Herwijnen and Schweizer, 2011; Helmstetter and Garambois, 2010; Cook et al., 2021; Pandey et al., 2021)" |
| Concern | The text contains 29 citation keys, all in the Introduction (Zhang et al., 2020a and 2020b counted separately). Fifteen can be assigned to an entry, seven of them only with deviations of year, spelling or author count (KK-07 to KK-09, KK-12 to KK-15); 14 have no entry at all. Quota 14/29 = 48.3 % (Python). Instance S1 counted 17 untraceable keys because it also counted the three keys whose year differs from the only fitting entry (Tian 2017, Zhang 2024, Zhao 2020). The whole state-of-the-art paragraph on field investigation, numerical analysis and landslide seismology (l. 52 to 64), on which the research gap rests (GB-07), cannot be checked by the reader. |
| Suggestion | Add the 14 missing entries to the reference list or remove the citations, then re-run the two-way check of text and list. |
| Status | verified (count from l. 33 to 64 against l. 508 to 605); quota inferred (calculation) |
| Severity | moderate |
| Source | S4 |

**GB-06 Li et al. (2024), cited for simplified two-dimensional simulations of restored terrain under external stress, performs no terrain restoration and applies no external stress.**

| Field | Content |
|---|---|
| Check | P13 |
| Location | p. 2, l. 46 to 49; reference list p. 27, l. 521 to 523 and l. 527 to 529; p. 28, l. 559 to 561 |
| Quotation | "For most numerical simulations involving terrain restoration, a two-dimensional simulation is more often used. The simplified model is adopted to simulate the overall process of landslide by inputting external stress" |
| Concern | The sentence serves to set the 3-D approach on restored terrain apart from earlier work, a useful framing that the cited works do not carry. Li et al. (2024) study the rainfall-triggered reactivation of the Zhongbao landslide with GeoStudio (transient seepage in SEEP/W, factor of safety by Morgenstern-Price in SLOPE/W) and describe no reconstruction of pre-sliding topography, no seismic or other external load and no runout simulation. Du et al. (2021) run a discrete element simulation of the Jiaobunong landslide with a paleo-earthquake trigger, which fits "inputting external stress", but the abstract states neither model dimension nor terrain restoration. Cheng and Yu-Sheng (2014) could not be read. The frequency claim ("most", "more often") carries no count of studies. |
| Suggestion | In l. 46 to 49 remove Li et al. (2024), state for each remaining source whether it is 2-D or 3-D and whether it reconstructs pre-failure terrain, and replace "most" and "more often" by what the cited works show. |
| Status | Li et al. (2024): verified (full text read by instance S1); Du et al. (2021): inferred (abstract only); Cheng and Yu-Sheng (2014): inferred (not readable); missing count: verified |
| Severity | moderate |
| Source | S1 |

**GB-07 The stated research gap on quantitative energy evolution during collisions rests on no documented search, its supporting citations are not in the list, and published quantitative energy studies, among them one by the first author, are not discussed.**

| Field | Content |
|---|---|
| Check | P28, P14 |
| Location | p. 2, l. 61 to 64; reference list p. 27, l. 540 to 542 and p. 26, l. 514 to 516; p. 24, l. 445 to 450; p. 26, l. 483 to 487 |
| Quotation | "However, they still lack a quantitative and systematic study of this topic, especially on energy evolution during the collision." |
| Concern | This sentence is the gap that motivates the study. No search is documented (GB-03), and none of the five works cited for landslide seismology is in the list (GB-05). Published quantitative energy studies exist and are not cited (none is in the list): (a) Hibert, C., Mangeney, A., Grandjean, G., and Shapiro, N. M.: Slope instabilities in Dolomieu crater, Réunion Island: from seismic signals to rockfall characteristics, J. Geophys. Res., 116, F04032, https://doi.org/10.1029/2011JF002038, 2011, which confirms "a direct link between the seismic energy and potential energy" and uses the ratio to estimate rockfall volumes; (b) Farin, M., Mangeney, A., Toussaint, R., de Rosny, J., Shapiro, N., Dewez, T., Hibert, C., Mathon, C., Sedan, O., and Berger, F.: Characterization of rockfalls from seismic signal: insights from laboratory experiments, J. Geophys. Res. Solid Earth, 120, 7102-7137, https://doi.org/10.1002/2015JB012331, 2015, which sets up an impact energy budget in which, on rough thick blocks, "the elastic energy radiation represents less than 5% of the lost energy"; (c) Lin, Q., Wang, Y., Xie, Y., Cheng, Q., and Deng, K.: Multiscale effects caused by the fracturing and fragmentation of rock blocks during rock mass movement: implications for rock avalanche propagation, Nat. Hazards Earth Syst. Sci., 22, 639-657, https://doi.org/10.5194/nhess-22-639-2022, 2022, a PFC2D study stating that "The energy transfer induced by fragmentation is more efficient than that induced by collision", which bears directly on Conclusion 4 (front blocks travel farther by collision) and on l. 445 to 450, where fragmentation is invoked without separating the two mechanisms. The manuscript's own list also contains Ge et al. (2021), "Mechanical energy evolution in the propagation of rock avalanches using field survey and numerical simulation", by the first author, and Chang et al. (2022), on the Xinmo landslide "via seismic signal and numerical simulation"; neither is cited or discussed (GB-51). |
| Suggestion | In l. 61 to 64 narrow the gap to what is open (for example energy partition at block scale in a full 3-D seismically triggered rock avalanche), position the study against Ge et al. (2021) and Chang et al. (2022), cite Hibert et al. (2011), Farin et al. (2015) and Lin et al. (2022), and discuss in Sect. 3.2.2 and Conclusion 4 whether the energy gain of front blocks stems from collision or from release at block separation. |
| Status | missing search and missing entries: verified (page images p. 2 and p. 26 to 29); Hibert et al. (2011), Farin et al. (2015), Lin et al. (2022): verified (abstracts and full texts; quoted sentences re-checked); content of Ge et al. (2021): inferred (title only) |
| Severity | moderate |
| Source | S1 |

#### Minor corrections

| ID | Location | Quotation | Replacement | Source |
|---|---|---|---|---|
| KK-01 | p. 1, l. 21; p. 3, l. 84 | "potential energy, kinetic energy, and dissipation energy" (l. 21); "kinetic energy and dissipation energy" (l. 84) | "dissipated energy" in both places, as in l. 242 and the rest of the text | S1, S2 |
| KK-02 | p. 1, l. 23; p. 3, l. 88 to 89; p. 14, l. 272 and l. 281; p. 23, l. 426 | "Alpha shape algorithm" (l. 23); "alpha-shape algorithm" (l. 272); "Alpha Shape algorithm" (l. 281); "Alpha Shape envelope fitting" (l. 426) | one spelling throughout, for instance "alpha-shape algorithm" and "alpha-shape envelope" | S2 |
| KK-03 | p. 1, l. 27 and l. 28 | "; For some blocks" and "; Compared with the upper rock mass" | "; for some blocks" and "; compared with the upper rock mass" | S1 |
| KK-04 | p. 1, l. 32 | "Landslide is a common and widespread geological disaster" | "Landslides are a common and widespread geological hazard" | S1 |
| KK-05 | p. 1, l. 33; p. 2, l. 39 and l. 40 | "high-level rock landslides" (l. 33); "high-level rock landslide" (l. 39 to 40 and l. 40) | "high-altitude rock landslides", "high-altitude rock landslide" (term of the title and of l. 73) | S1 |
| KK-06 | p. 1, l. 34 to 35 | "such as donghekou landslide" | "such as the Donghekou landslide" | S1 |
| KK-07 | p. 1, l. 34; p. 2, l. 56 to 57; p. 27, l. 530 to 536 | "Fan et al., 2019a" (l. 34); "Fan et al., 2019" (l. 56 to 57) | assign "2019a" and "2019b" to the two Fan et al. (2019) entries (l. 530 to 532, l. 533 to 536) and use the matching letter at both places in the text | S1, S4 |
| KK-08 | p. 1, l. 36 | "Wang, 2021" | "Wang et al., 2021" (the entry, l. 581 to 584, has seven authors) | S1, S4 |
| KK-09 | p. 1, l. 37; p. 28, l. 575 to 577 | "Tian et al., 2017" | "Tian et al., 2016", or change the year of the entry, so that text and list agree | S1, S4 |
| KK-10 | p. 2, l. 43 | "For landslides that have not occurred too far away" | "For recent landslides" | S1 |
| KK-11 | p. 2, l. 44 | "optical remote sensing images and UAV impact" | "optical remote sensing images and UAV imagery" | S1 |
| KK-12 | p. 2, l. 45 to 46 | "Zhang et al., 2024" | "Zhang et al., 2023", matching the entry Zhang, J. et al. (l. 594 to 596), or correct the year of the entry; see GB-04 for the content | S4 |
| KK-13 | p. 2, l. 46 | "Song at al.2017" | "Song et al., 2017" | S1, S4 |
| KK-14 | p. 2, l. 48 to 49 | "Cheng 2014" | "Cheng and Yu-Sheng, 2014" (two authors, l. 521 to 523); please also check the order of given and family name of the second author | S1, S4 |
| KK-15 | p. 2, l. 57 | "Zhao et al., 2020" | "Zhao et al., 2021" (entry l. 600 to 602, Nat. Hazards, 106, 2021) | S4 |

#### Verification log

| ID | Check | Checked | Values | Result |
|---|---|---|---|---|
| PP-01 | P13 | Every sentence of Segment 1 that reproduces other work with a number, ranking or evaluation, and the resolvability of each citation | 29 citation instances in l. 33 to 63, none in the abstract; sources opened: Carpignano 2009, Fan 2019 (Rev. Geophys.), Song 2017, Wu 2024, Li 2024, Du 2021, Cheng and Yu-Sheng 2014; no finding for Sun 2011, Wang 2014 and Wang 2021 (titles name Donghekou and the Wenchuan earthquake, consistent with l. 34 to 36) and Hu 2017 for Hongshiyan (full text not readable, attribution not contested); claims in l. 52 to 60 not checkable because 9 of 10 citation instances have no entry | findings GB-01, GB-04, GB-06; disclosed by the manuscript: none |
| PP-02 | P4 | All citations against the 31 list entries in both directions, short citation against entry, alphabetical order | 29 keys: 8 exact, 7 with deviations (KK-07 to KK-09, KK-12 to KK-15), 14 without entry; 15 entries cited, 16 not; alphabetical order correct (He, J. before He, K. before He, N.; Wang 2014 before Wang 2021; Wu, H. before Wu, J.); no citations in Sect. 2 to 4; Zhao et al. (2021) confirmed as Nat. Hazards 106(1), 459-485 on its RePEc record; Crossref record of Cheng and Yu-Sheng (2014) not readable | findings GB-05, GB-51 |
| PP-03 | P10 | Each named gap against an aim and each aim against a design element | G1 restoration rare and mostly 2-D (l. 42 to 51) to Fig1 part 1 and Conclusion 1, test missing; G2 observations rare (l. 60 to 61) to simulation as substitute; G3 quantitative energy study (l. 63 to 64) to Sect. 2.3 and 3.2; aims "law" (l. 40 to 41) and early warning (l. 72 to 73) without design element | covered by GB-02, GB-42, GB-49 |
| PP-04 | P28 | All gap and novelty claims and whether a literature search is documented | four claims: l. 42, l. 49 to 51, l. 61 to 64, l. 113 to 119; l. 60 to 61 treated as a statement on data availability; full text searched without hit for search, Scopus, Web of Science, CNKI, Google Scholar, first time, novel (only "novel" in a reference title, l. 586) | findings GB-03, GB-07, GB-10; disclosed: none |
| PP-05 | P14 | Literature search for prior work on the contribution (contour restoration, 3DEC simulation under substitute record, block-scale energy, collisions, alpha shape) | six searches; candidates checked against the list: von Wartburg 2020, Lin 2022, Farin 2015, Hibert 2011 (none in the list, used in GB-03 and GB-07); Zhao, T. et al. 2017 (J. Geophys. Res. Earth Surf., 122, 678-695, not in the list, not proposed); dropped because in the list: Zhao, B. 2021, Wu, J. 2013, Zhou 2024, Ge 2021, Chang 2022, all uncited in the text; results pointing to the discussion or a later version of this manuscript were not opened | findings GB-03, GB-07 |
| PP-06 | P18 | Declared principles applied to the manuscript itself | gap of "a quantitative and systematic study" (l. 63 to 64) against qualitative validation and a threshold chosen by eye; α fixed to avoid tuning (l. 282 to 284) while the collision threshold is tuned visually; data and code on request, no openness principle declared | no separate finding; covered by GB-22, GB-39 |
| PP-07 | Design sketch | Research questions, study type, cases, data sources, timeline, environment, components and disclosed limitations | no explicit questions or hypotheses; aim l. 65 to 73; single-case 3DEC model, one run of 131 s, 25345 blocks, 317563 m³, 10 monitored blocks, 10 envelope times; sources: UAV DEM (date and resolution not stated), restored surface, Tiezhuang Temple tablet, Luding record of 2008, Table 1 parameters, 3DEC output, two field photographs; 3DEC version, damping, time step and record processing not stated | input for GB-02, GB-11, GB-17, GB-18, GB-22; disclosed: structural planes ignored (l. 175 to 178), no instrumental record (l. 183 to 191), restored terrain smooth (l. 160 to 162), dam break not modelled (l. 348 to 350), weathering since 1786 (l. 354 to 355) |

### Segment 2: Methods, data, model (p. 2 to 15, l. 74 to 296)

#### Substantive findings

**GB-08 The study-site markers in Fig2 (a) and (b) do not lie at the coordinates given in the text.**

| Field | Content |
|---|---|
| Check | P3 |
| Location | p. 6, Fig2 (a) and (b); p. 5, l. 95 to 96 |
| Quotation | "The coordinates of the landslide center are: 29 ° 37 ′ 30.726 ″ north latitude, 102 ° 09 ′ 41.190 ″ east longitude." |
| Concern | Fig2 is a careful three-scale location figure with graticule, scale bars and north arrows, which makes the check possible. (a) The red dot "Mogangling landslide" measures 101.19 ± 0.03 °E, 29.56 ± 0.03 °N (calibrated on the frame ticks 100 °E and 106 °E, 31 °N and 27 °N, regular spacing); the text gives 102.161 °E, 29.625 °N, a difference of 0.98° in longitude, about 95 km (Python: 0.98 × 111.32 km × cos 29.6°). (b) The red star "Study area" sits on the crossing of the graticule lines labelled 102°09'E and 29°37'N; the text coordinates lie 41.19" east and 30.73" north of that crossing, about 1105 m east and 948 m north, which with the panel's scale bar places them at the Dadu River channel rather than on the landslide scar. Either the map annotations or the coordinates are wrong. |
| Suggestion | Re-check the coordinates in l. 95 to 96 against the DEM, move the dot in Fig2 (a) to the correct longitude, place the star in Fig2 (b) at the stated coordinates or correct them, and state the datum (for example WGS84). |
| Status | positions verified (measured on the page image by instance AB; the offset of the dot in (a) re-checked on the page image); which of the two is wrong: inferred |
| Severity | moderate |
| Source | AB |

**GB-09 Geological units and model materials carry different names and symbols in the text, Fig2 (c), Fig3, Fig4 and Table 1, and the assignment of the Table 1 parameters to the model materials is not stated.**

| Field | Content |
|---|---|
| Check | P38, P3 |
| Location | p. 5, l. 101 to 107; p. 6, Fig2 (c) legend; p. 8, Fig3 (a) and (b) legends; p. 10, Fig4 legend; p. 9, l. 180 to 181; p. 11, l. 207 to 209 and Table 1, column "Rock mass" |
| Quotation | "Quartz diorite (O2) and a small amount of basic magmatic rocks are distributed on the western slope of Mogangling. The sand slate of the Triassic Baiguowan formation (T3bg) is exposed on the left bank of the Dadu River." |
| Concern | Names per unit, all read on the page images: γo2 is "Jinning plagioclase granite" in the text, "Plagiogranite" in Fig2 (c) and "Granite" in Fig3; O2 "Quartz diorite" appears in the text and as "Diorite" in Fig3 but not in Fig2 (c) or Fig4; T3bg appears only in the text, while Fig2 (c) shows γM2 "Hybrid granite" on the left bank, a unit the text never mentions; Q4del is "landslide accumulation" in the text, "Rubble soil" in Fig2 (c) and "Qdel" in Fig4; Q4col+dl is "colluvial Deluvial deposit" in the text and "Massive gravel" in Fig2 (c) and Fig3 (b); Fig3 adds "Massive gravelly soils" without symbol. Fig4 shows four materials (γo2, Qdel, γM2, sliding mass), and its cyan Qdel colour (legend #04f4f4, slope surface #04fcfc) covers the whole middle band of the model from the source area across the valley floor, whereas Q4del in Fig2 (c) covers only the deposit of about 0.47 km². Table 1 gives parameters for two rock masses ("bed rock", "landslide mass"), and l. 208 to 209 speaks of strongly and moderately weathered granite. A reader cannot tell which parameter set was assigned to γo2, Qdel, γM2 and the sliding mass. |
| Suggestion | Use one name and one symbol per unit in l. 101 to 107 and in the legends of Fig2 (c), Fig3 (a, b) and Fig4; show T3bg and O2 in Fig2 (c) or remove them from l. 102 to 104 and explain γM2 in the text; state in l. 180 to 182 or in Table 1 which parameter set applies to each material in Fig4, and explain why Qdel extends beyond the mapped deposit. Question to the authors: do "bed rock" and "landslide mass" in Table 1 correspond to the moderately and strongly weathered zones of l. 208 to 209? |
| Status | names, symbols and colours: verified (page images, instances S2 and AB); assignment of Table 1 rows to the model materials: assumption, therefore asked as a question |
| Severity | moderate |
| Source | S2, AB |

**GB-10 The statement that seismic effects on slope instability are underestimated and analysed in relatively few studies has no citation, and the reference list itself holds an uncited study on this topic in the same river reach.**

| Field | Content |
|---|---|
| Check | P28 |
| Location | p. 5, l. 113 to 119; reference list p. 27, l. 546 to 548 |
| Quotation | "the effect of seismic force on slope instability has been underestimated to a certain extent" and "are relatively few" |
| Concern | The paragraph motivates the case study for the Dadu River. Both claims concern the state of research and practice but carry no citation and no description of how the literature was surveyed. The list contains He, J. et al. (2023), "Seismic response of an irregular slope containing surficial weak layer and internal fractures in Dadu River, southwest China", which addresses seismic slope response in the same river reach; it is not cited here or anywhere in the text. |
| Suggestion | In l. 113 to 119 support both claims with citations and discuss He et al. (2023), or reword the passage as the authors' assessment without a claim about the number of studies. |
| Status | missing citation and search: verified (page image p. 5); content of He et al. (2023): inferred (title in the list only) |
| Severity | moderate |
| Source | S1 |

**GB-11 Key model-building steps cannot be rebuilt from the text.**

| Field | Content |
|---|---|
| Check | P8 |
| Location | p. 6, l. 130 to 140; p. 7, l. 157 to 159; p. 9, l. 178 to 180; p. 11, l. 206 to 211 and Table 1; p. 25, l. 464 to 466 |
| Quotation | "the contour lines corresponding to the sliding bed and accumulation area are modified to be straight" and "the selection of physical-mechanical parameters was based primarily on laboratory testing, empirical analogy, and parameter inversion" |
| Concern | Judgement-dependent steps lack the rule behind the judgement: which contours are straightened, over which extent and by which interpolation; the "trajectory equations" of Conclusion 1 (l. 465) do not appear in the methods (GB-49). Parameter inversion has no target observation or objective, and it is not stated which value of Table 1 comes from tests, analogy or inversion. Orientation and spacing of the "uniform structural plane" and the assignment of the two discontinuity rows of Table 1 are open (GB-21). DEM resolution, point-density screening and noise filters (l. 131 to 134) have no values. |
| Suggestion | Add to Sect. 2.1 the straightening rule with extent and interpolation, the source of each value in Table 1 with inversion target and misfit, the geometry of the joint set, and DEM resolution and filter settings. |
| Status | verified (absence in the text) |
| Severity | moderate |
| Source | SD |

**GB-12 The four-part zoning attributed to Fig3 (a) does not appear there; the figure shows two zones.**

| Field | Content |
|---|---|
| Check | P4, P3 |
| Location | p. 7, l. 144 to 146; p. 8, Fig3 (a) |
| Quotation | "The whole landslide occurrence area can be divided into four parts: the rock wall area, colluvial slope area, slope debris flow area, and main accumulation area." |
| Concern | The legend of Fig3 (a) contains "I Sliding bed" and "II Accumulation area", separated by one dotted line; rock wall, colluvial slope and slope debris flow areas are not marked. |
| Suggestion | Mark the four parts in Fig3 (a) or reword l. 145 to 146 to the two zones shown, and give the source of the four-part zoning. |
| Status | verified (page image p. 8) |
| Severity | minor |
| Source | S4, AB |

**GB-13 Landslide dimensions, volume and mass are inconsistent among the text, the geological map, the model and the energy figures, so the mass behind all absolute energies cannot be identified.**

| Field | Content |
|---|---|
| Check | P1, P2, P9, P23, P3 |
| Location | p. 7, l. 148 to 151; p. 6, Fig2 (c); p. 9, l. 173 to 182; p. 11, Table 1, row "landslide mass", column "Density"; p. 13, Table 2, column "Volume"; p. 20, Fig8; p. 21 to 22, Fig9; p. 25, Fig12, label "1116.8"; p. 16, l. 330 |
| Quotation | "about 450 m long, about 1000 m wide along the river, and a planar area of 0.45 km². The average thickness of the landslide mass is about 100 m, and the volume is about 2400×10⁴ m³" and "the volume of the landslide is 317563 m³" |
| Concern | (1) Three volumes are in play: about 2400×10⁴ m³ (l. 151); 0.45 km² × 100 m = 4500×10⁴ m³, 1.875 times the stated value; and 317563 m³ for the model (l. 182), a factor of 75.6 below l. 151. Spread over 0.45 km², 317563 m³ gives 0.71 m mean thickness, and the Table 2 block volumes on the 8.7 m × 8.7 m grid give block heights of 10.0 to 23.2 m, against "about 100 m" (all Python, zf/rechnungen.py). (2) The length of about 450 m (l. 149) differs from the model length of 1021 m in the sliding direction (l. 174, Fig4 label). Measured on Fig2 (c) with its scale bar, the magenta landslide boundary encloses 0.95 to 1.00 km² and spans 1156 m along a-a', whereas the yellow unit Q4del alone measures 0.47 km² and 503 m along a-a'; the text dimensions therefore fit the deposit, not the landslide. (3) The energies fit none of the volumes. With ρ = 2300 kg/m³ (Table 1) and the measured Fig8 total of 6450 to 6516 GJ and KE maximum of 1657 to 1685 GJ (instances S3, AB, SD): case A, V = 317563 m³, m = 7.304×10⁸ kg: the mean drop needed for 6500 GJ is 907.2 m, more than the whole relief (back-wall ridge about 2000 m to river about 1115 m, 885 m; model 747 m plus 131 m, 878 m); the Fig12 peak of 1116.8 GJ needs an rms speed of 55.3 m/s and the Fig8 peak 67.4 m/s, against a maximum of 31.6 m/s (l. 330); at 31.6 m/s, 1657 GJ needs at least 3.32×10⁹ kg, that is 1.44×10⁶ m³. Case B, V = 2400×10⁴ m³: mean drop 12.0 m, incompatible with the relief and with the per-block drops of 30 to 316 m implied by Fig9 (GB-27). Case C, V = 4500×10⁴ m³: mean drop 6.4 m. Case D, an unstated mass: the ten monitored blocks carry 0.67 to 7.11 MJ/m³ initially, which would put the whole mass between 9.1×10⁵ and 9.7×10⁶ m³. Which mass the simulation represents is open, and with it the energy magnitudes and the comparison with the field in GB-39. |
| Suggestion | In Sect. 2.1 give one landslide volume with its derivation, the dimensions of the whole landslide and of the deposit separately with the outline in Fig2 (c) each refers to, and the number and volume of the landslide blocks of the model; in Sect. 3.2.1 state the mass used for Fig8 and Fig12 and the mean vertical drop of the centre of mass, so that 6500 GJ can be checked. |
| Status | text values and arithmetic: verified (text, Table 1, Table 2, Python); Fig2 (c) areas and Fig8 values: verified (measured by instances AB, S3, SD); that the text dimensions describe the deposit and that the energy mass is none of the stated volumes: inferred |
| Severity | major |
| Source | S3, SD, AB |

**GB-14 The water level in the profile Fig3 (b) lies about 35 m above the river level implied by the text.**

| Field | Content |
|---|---|
| Check | P3 |
| Location | p. 8, Fig3 (b); p. 7, l. 151 to 152 |
| Quotation | "The elevation of the slope toe is 1120 m (about 5 m higher than the river surface)" |
| Concern | The water surface in Fig3 (b) measures 1149 ± 11 m (calibration on the axis bar 2000 and 1000, regular label spacing, 5 px added because the axis has no ticks), while the text implies about 1115 m; the difference of 34 m exceeds the uncertainty. Does the profile show today's impounded water level rather than the natural river? |
| Suggestion | State in the caption or in l. 152 which water level the profile shows, or correct one of the two values. |
| Status | water level: verified (measured by instance AB); cause: assumption, therefore asked as a question |
| Severity | minor |
| Source | AB |

**GB-15 The section b-b' named in l. 159 to 160 does not exist, and the sentence sends the reader to Fig3 (c) for results of sections that are shown in Fig3 (b).**

| Field | Content |
|---|---|
| Check | P4, P3 |
| Location | p. 7, l. 159 to 160; p. 6, Fig2 (c); p. 8 to 9, Fig3 (b) and (c) |
| Quotation | "As shown in Fig3. (b), make a section along a-a'and b-b' in Fig2. (c). The results are shown in Fig3. (c)." |
| Concern | Fig2 (c) shows a single red section line, labelled "a" at its western end and "a'" at its eastern end; no line or label b or b' appears in any panel of Fig2, and Fig3 (b) shows one profile titled "(a-a')". Instances S2 and S4 read the eastern label as "a"; at 600 dpi the prime is visible next to the letter, partly overlapping a fault dash (rendering in zf/crop_aost.png), so the eastern end is labelled correctly and only b-b' is missing. Fig3 (c) shows contour maps and shaded terrain before and after restoration, which is the plan-view comparison discussed in the next sentence, not section results. |
| Suggestion | In l. 159 to 160 delete "and b-b'" or add the b-b' line to Fig2 (c) and its profile to Fig3 (b); point to Fig3 (b) for the profile and to Fig3 (c) for the plan-view comparison. |
| Status | verified (page images p. 6, 8, 9; eastern label re-checked at 600 dpi) |
| Severity | minor |
| Source | S4, AB, S2 |

**GB-16 Fig3 is not readable on its own: profile axes without quantity and unit, unexplained symbols, unlabelled sub-maps.**

| Field | Content |
|---|---|
| Check | P29 |
| Location | p. 8 to 9, Fig3 (a) to (c); caption l. 166 to 167 |
| Quotation | "Fig3. Landslide restoration diagram: (a) 3D views of the study area; (b) Engineering geological profile; (c) Comparison map of surface topography before and after restoration" |
| Concern | In (b) neither axis has a quantity or unit (y 1000 to 2000, x 0 to 1500), and the "80°" symbol with half-arrow is not in the legend. (c) consists of four maps without sub-letters; the blue rectangles in all four are not explained, the contour labels in the upper maps are rotated digits of about 2 pt at print size, and the lower maps have no scale or north arrow. (a) carries a planar scale bar on an oblique 3-D view. The caption only names the panels. |
| Suggestion | Label the axes of (b) ("Distance along a-a' (m)", "Elevation (m a.s.l.)") and explain the 80° symbol; letter the four maps of (c), explain the blue rectangles and enlarge the contour labels; replace the scale bar in (a) by an approximate scale note. |
| Status | verified (page images p. 8 and 9) |
| Severity | minor |
| Source | AB |

**GB-17 Result-relevant settings of the computing environment are not reported.**

| Field | Content |
|---|---|
| Check | P35 |
| Location | p. 9, l. 168 to 170; p. 10, l. 189 to 203 and Fig4 inset; p. 11, l. 227 to 229; p. 14, l. 272 |
| Quotation | "the three-dimensional discrete element program (3DEC), one of the most widely used numerical methods in rock mechanics, is used to simulate the motion process" |
| Concern | Missing are: 3DEC version; rigid or deformable blocks; damping type and value in the static and dynamic phase (damping enters DE directly, GB-42); time step; contact detection and joint model; record component, PGA, duration, scaling, filtering and conversion to a base stress for the viscous boundary (the Fig4 inset has no time axis and no PGA value); software and parameters for peak detection and alpha shapes. The ranking "one of the most widely used" carries no citation. |
| Suggestion | Add a table of numerical settings with these items to Sect. 2.1 and give the input record with time axis and PGA in Fig4. |
| Status | verified (absence in text and Fig4) |
| Severity | moderate |
| Source | SD |

**GB-18 The single surrogate ground motion rests on an uncited comparison and is not tested by any sensitivity run.**

| Field | Content |
|---|---|
| Check | P9 |
| Location | p. 10, l. 183 to 191; p. 10, Fig4 inset; p. 5, l. 97 to 99; p. 15, l. 306 to 321 |
| Quotation | "Extensive research indicates that the Kangding earthquake is comparable to the 2008 Wenchuan earthquake in terms of damage distribution, affected intensity, and estimated magnitude." |
| Concern | The manuscript discloses that no record of the 1786 event exists (l. 183 to 186). What is not drawn to an end: the "extensive research" carries no citation, only one record is used, and l. 186 to 187 assign the site to the Longmenshan system, while l. 97 to 99 place it at the junction of the Xianshuihe, Longmenshan and Anninghe faults. The initiation stages, velocities (5.9 to 31.6 m/s, l. 307 to 330) and timing of Sect. 3.1 all depend on this input. Neither the distance from the 1786 source to the site nor that from the Wenchuan rupture to Luding station is given. Does a record of a different event at a different station represent the motion at Mogangling in 1786? |
| Suggestion | Add the references for l. 187 to 189 and state component(s), PGA, duration and scaling of the input in Sect. 2.1. Counter-design: a small ensemble of records, or the Luding record scaled to bracket the intensity estimated for 1786, reporting how runout, peak velocity, duration and energy partition change. |
| Status | missing citation and sensitivity: verified; representativeness of the record: assumption, therefore asked as a question |
| Severity | major |
| Source | SD |

**GB-19 Third-party and archival sources used in the methods have no provenance, citation or mention in the data statement.**

| Field | Content |
|---|---|
| Check | P12 |
| Location | p. 10, l. 189 to 191 and Fig4 inset; p. 6, Fig2 (b) and (c), caption l. 126 to 127; p. 9, l. 180; p. 8, Fig3 (b), caption l. 166; p. 6, l. 136 to 138; p. 11, l. 206 to 207; p. 19, Fig7 (o), caption l. 369 to 370; p. 13, l. 265 to 266; p. 26, l. 505 to 506 |
| Quotation | "this study adopts the acceleration records measured at the Luding station during the Wenchuan earthquake as the input ground motion" |
| Concern | The input ground motion, the most influential model input, is identified only by station and event; agency or network, component, sampling interval, processing and access route are missing, and no reference is cited. The same holds for the satellite image of Fig2 (b) (provider, date), the geological map and profile of Fig2 (c) and Fig3 (b) (own mapping or adapted), the tablet record (no edition or secondary source), the laboratory tests (no values, samples or report) and the field photographs of Fig7 (o). The data statement promises availability "from the first author", which cannot cover data owned by third parties. The list contains three studies on the Mogangling area (Wu et al., 2013; Zhao et al., 2021; Zhou et al., 2024) that are not cited in the methods; whether map, profile or parameters derive from them cannot be told. Are Fig2 (c), Fig3 (b) or Table 1 adapted from these studies? |
| Suggestion | Add to Sect. 2.1 and to the captions of Fig2 and Fig3 the origin of each external source with a full citation (for the record: network, station code, component, sampling rate, processing); extend the data statement with one sentence per third-party source on where it can be obtained; report the laboratory values or state that Table 1 holds only back-analysed values. |
| Status | absence of source information: verified (text, captions, statements); adaptation from the cited Mogangling studies: assumption, therefore asked as a question |
| Severity | moderate |
| Source | S2 |

**GB-20 The ground-motion inset and the legend symbols of Fig4 are not explained.**

| Field | Content |
|---|---|
| Check | P29 |
| Location | p. 10, Fig4; caption l. 192 |
| Quotation | "Fig4. Discrete numerical model with fine topography" |
| Concern | The inset "Acceleration (gal)" has tick marks but no labels, quantity or unit on the time axis; the marks tp, tPGA, tf and te are explained neither in the caption nor in the text; the caption does not mention the inset or the component of the Luding record. The legend gives only the codes γo2, Qdel and γM2, resolved only in Fig2 (c) under partly different names (GB-09). |
| Suggestion | Extend the caption with the inset (component, station, event, meaning of tp, tPGA, tf, te), add a labelled time axis in s, and write the unit names next to the codes. |
| Status | verified (page image p. 10) |
| Severity | minor |
| Source | AB |

**GB-21 The two discontinuity sets of Table 1 are named differently in the text, and "structural plane" is used for several objects, one of which is said to be ignored and set at the same time.**

| Field | Content |
|---|---|
| Check | P38 |
| Location | p. 11, l. 208 to 210 and Table 1, rows "discontinuities" and "potential discontinuities"; p. 9, l. 176 to 180; p. 15, l. 308 to 313 and l. 320 |
| Quotation | "The discontinuities are represented by both fully developed potential rupture planes and joint sets" and "A uniform structural plane is set inside." |
| Concern | Table 1 lists "discontinuities" and "potential discontinuities". The text names "fully developed potential rupture planes" and "joint sets" (l. 209 to 210), "structural plane" (l. 176 to 180), "steeply dipping structural planes" (l. 308 to 309), "pre-existing potential sliding surfaces" (l. 313) and "potential failure planes" (l. 320). Which Table 1 row belongs to which name is not stated, and "fully developed potential" is itself contradictory. The impact of the structural plane "has to be ignored" (l. 177), yet a uniform structural plane is set inside (l. 179 to 180). A reader cannot assign the parameters to the planes of the model. |
| Suggestion | Use the same two names in l. 208 to 210 and in Table 1 (for instance "joint set" and "potential sliding surface"), state which planes of the model each row applies to, and refer to the same names in l. 176 to 180 and l. 308 to 320. |
| Status | verified (text and Table 1 on the page image) |
| Severity | moderate |
| Source | S2 |

**GB-22 Effective collisions are identified from velocity peaks alone, without checking that the peaks are collisions.**

| Field | Content |
|---|---|
| Check | P31 |
| Location | p. 11, l. 215 to 234; p. 12, Fig5 (a) to (f); p. 16, l. 330 to 331; p. 25 to 26, l. 473 to 475 |
| Quotation | "Effective collisions of rock blocks are identified by their characteristic velocity changes." and "At a threshold of 30%, however, the identification of effective collisions is deemed acceptable." |
| Concern | The prominence approach is explained step by step and Fig5 shows its effect at five thresholds. But a velocity peak follows any acceleration: steepening slope, free fall ("After a brief airborne trajectory", l. 331), seismic shaking during the input, or numerical noise. The detected peaks are not compared with contact events, so neither false positives nor missed collisions are estimated (P32), and the 30 % threshold rests on visual judgement of one curve whose origin is unclear (GB-26). Conclusion 4 and the Abstract (l. 28 to 30) rest on these counts. |
| Suggestion | Counter-design for Sect. 2.2: for the ten monitored blocks export contact forces from 3DEC, define a collision as a contact-force pulse, report precision and recall of the velocity-peak detector at 10 to 50 %, choose the threshold from this comparison and state the error rate. |
| Status | absence of a ground-truth comparison: verified; alternative causes of peaks: inferred from l. 306 to 331 |
| Severity | major |
| Source | SD |

**GB-23 In Fig5 (a), two of the six red "effective collision" markers do not sit on local velocity maxima, and the curve falls below zero.**

| Field | Content |
|---|---|
| Check | P3 |
| Location | p. 12, Fig5 (a); p. 11, l. 220 to 225 |
| Quotation | "A local velocity peak (denoted by red or purple markers) corresponds to an acceleration phase, but only those pronounced peaks (highlighted in red) yield a substantial velocity increase" |
| Concern | Fig5 (a) defines an effective collision, so its markers must match the definition. Measured at 600 dpi: the red marker at 243 m, 13.04 m/s is followed directly by an unmarked point at 261 m, 13.40 m/s, the highest point of the curve; the red marker at 463 m, 4.21 m/s is followed by 4.84 m/s at 476 m. Both lie on rising flanks. The other four red and the five purple markers are local maxima. The last point lies at minus 0.36 ± 0.03 m/s, although the axis reads "Velocity (m/s)"; a speed cannot be negative, so either a velocity component is plotted or the data are offset. |
| Suggestion | Re-plot Fig5 (a) with the markers on the detected peaks, or explain why a marker precedes its peak, and state in the caption whether the curve is speed or a velocity component (which one). |
| Status | verified (47 data markers detected and measured by instance AB) |
| Severity | moderate |
| Source | AB |

**GB-24 The curve used to detect effective collisions is named after travel distance, travel displacement and displacement.**

| Field | Content |
|---|---|
| Check | P38 |
| Location | p. 11, l. 221, l. 225, l. 227 and l. 234; p. 1, l. 22 to 23; p. 25 to 26, l. 474 to 475; p. 12, Fig5 x-axes; p. 23, Fig10 (b) x-axis; p. 4, Fig1 |
| Quotation | "a typical velocity-travel-distance curve for an individual block" and "the local peak value of the displacement velocity curve" |
| Concern | The same curve is called "velocity-travel-distance curve" (l. 221), "velocity-distance profile" (l. 225), "velocity-distance curve" (l. 227), "travel-distance versus velocity profile" (l. 234), "displacement velocity curve" (l. 23) and "displacement-velocity curves" (l. 474 to 475). The axes read "Travel distance (m)" in Fig5 (a), Fig10 (b) and Fig1, but "Travel Displacement (m)" in Fig5 (b) to (f) (page image p. 12). Net displacement and path length are different quantities, so the Abstract and Conclusion 2 describe a different abscissa from the methods. |
| Suggestion | Choose one abscissa (travel distance, if path length is meant) and use it in l. 23 (for example "by extracting the significant local peaks of the velocity versus travel-distance curve"), l. 221 to 234, l. 474 and in all axis labels of Fig5 and Fig10 (b). |
| Status | verified (text and axis labels on the page images); that displacement and travel distance differ: inferred from the definitions |
| Severity | moderate |
| Source | S2, S1, AB |

**GB-25 The base of the 1,139 effective collisions is not stated: the count matches neither Fig5 (d) nor Fig10 (b), the threshold percentage has no reference quantity, and the bins of Fig10 (b) are not normalised.**

| Field | Content |
|---|---|
| Check | P20, P21, P8, P29 |
| Location | p. 11, l. 227 to 234; p. 12, Fig5 (b) to (f) and caption l. 238 to 239; p. 22, l. 414 to 421; p. 23, Fig10 (b) |
| Quotation | "Under this setting, 1,139 effective collisions were detected from the travel-distance versus velocity profile." |
| Concern | (1) Population: the count comes from "the" profile (singular); whether this is one block, the ten monitored blocks, all blocks or a mass average is not said, so 1,139 has no denominator. (2) Fig5 (d), the 30 % panel, shows roughly 60 to 100 red markers (63 separate areas and about 96 by total marker area in instance AB, about 73 clusters in instance SD), not 1,139. (3) Fig10 (b) has 26 bins of 100 m whose measured values sum to 1213 to 1217 (instances S3, AB, SD); if it bins the same collisions, the difference to 1,139 is 74 (6.5 %); 595 of 1213 (49.1 %) fall into 2200 to 2500 m, up to 157 per 100 m, one collision every 0.64 m if it were one block (Python). (4) The bin counts are absolute; the number of blocks still moving decreases with distance, so the per-block rate of l. 420 to 421 cannot be read from them. (5) The prominence threshold is given in percent (10 to 50 %, l. 227 to 232) without the quantity it is a percentage of, and the caption explains neither the inset nor the grey box (1550 to 1830 m) in each panel. Is 1,139 the total over all blocks of the model, and over which blocks is Fig10 (b) summed? |
| Suggestion | In Sect. 2.2 state whose profile Fig5 (b) to (f) shows, define the prominence measure and its reference value, and explain inset and grey box in the caption; in Sect. 3.2.2 state the population of Fig10 (b), reconcile its sum with 1,139, and give the number of blocks reaching each distance bin or plot collisions per block and per 100 m. |
| Status | counts: verified (measured by instances S3, AB, SD); missing denominators and missing reference quantity: verified; the population behind 1,139: assumption, therefore asked as a question |
| Severity | moderate |
| Source | S3, AB, SD |

**GB-26 The profile in Fig5 (b) to (f) reaches about 45 m/s, while the text gives 31.6 m/s as the maximum velocity, and the block shown is not identified.**

| Field | Content |
|---|---|
| Check | P3, P2 |
| Location | p. 12, Fig5 (b) to (f), caption l. 238 to 239; p. 11, l. 221; p. 16, l. 330 and l. 337; p. 17, Fig7 (e); p. 21 to 22, Fig9 |
| Quotation | "As shown in Fig7. (e) and (l), during the impact-at-base stage, the maximum velocity reached 31.6 m/s." and "The velocity reached its peak upon arrival at the valley floor." |
| Concern | The curve in Fig5 (b) and (d) peaks at 44.9 ± 0.3 m/s at a travel displacement of about 253 m (instance AB; 45.5 m/s at 252 m in instance S3), while the colour bars of Fig7 never exceed 31.6 m/s and the text calls 31.6 m/s the maximum. Fig5 (a), "a typical velocity-travel-distance curve for an individual block", is a different curve (up to about 13.4 m/s over 600 m). Two readings are possible. A: the block in Fig5 (b) to (f) belongs to this simulation and reached its peak between the snapshots at 12 s and 15 s; Fig8 shows KE still rising after 12 s (about 1570 GJ at 12.4 s, 1657 GJ at 13.6 s), so this cannot be excluded, but then 31.6 m/s is not the maximum, and none of the ten monitored blocks comes close (their KE maxima of 0.03 to 0.28 GJ give 3.7 to 17.2 m/s with the Table 2 volumes and 2300 kg/m³). B: the curve comes from another block set or another model. The grade is major because the 30 % threshold that sets all collision counts, and thus GB-44, is calibrated on this curve. |
| Suggestion | Name the block (ID from Table 2) and the run shown in Fig5 (b) to (f); state the maximum block velocity of the whole run and reconcile it with l. 330 and l. 337, or replace the curve by one from the Mogangling model. |
| Status | velocities: verified (measured by instances AB and S3; curve shapes and axis labels re-checked on the page image p. 12); speeds of the monitored blocks: inferred (density from Table 1); whether the curve comes from this simulation: assumption, therefore asked as a question |
| Severity | major |
| Source | AB, S3 |

**GB-27 The stated reference datum for potential energy does not match the potential energies plotted in Fig8 and Fig9.**

| Field | Content |
|---|---|
| Check | P2, P23, P5, P3 |
| Location | p. 13, l. 250 to 255; p. 20, Fig8; p. 21 to 22, Fig9 (a) to (j); p. 13, Table 2, columns "Coordinate" and "Volume"; p. 20, l. 397 to 399 |
| Quotation | "the potential-energy calculation uses the model’s initial height as the reference datum rather than true sea level; only the change in potential energy due to relative displacement is considered." |
| Concern | With the initial height as datum, PE would start at 0 and become negative. Instead Fig8 starts at about 6450 GJ and reaches 0 from about 110 s, and every block in Fig9 starts at its maximum and reaches PE = 0.000 GJ at its minimum; blocks 1 and 3 then rise again to about 0.34 and 0.32 GJ (instance AB). At t0 each block holds only PE, so h0 = E0/(ρVg) with Table 2 volumes gives 238.3, 222.3, 234.7, 163.1, 315.9, 172.3, 29.8, 192.5, 82.5 and 43.4 m for blocks 1 to 10 (instance S3), while their z coordinates are 340 to 755 m; the implied datum z minus h0 ranges from 101.7 to 711.6 m, and z and h0 are negatively correlated (r = minus 0.70). Case A: the datum is each block's lowest elevation during the run; this fits Fig9 but contradicts l. 253 to 254 and makes the panels show drop heights, not potential energies on a common scale. Case B: the datum is z = 0 of Table 2; then PE(t0) would be 7.21 GJ for block 1 (Fig9 (a): 5.05 GJ) and 16.49 GJ for block 10 (Fig9 (j): 0.95 GJ); excluded. Case C: the volumes or coordinates in Table 2 are not those of the monitored blocks. The rebound reading of l. 397 to 399 and any comparison of energies between blocks depend on the answer. |
| Suggestion | Define the datum of h(ti) in Sect. 2.3 next to Eq. (3) (fixed elevation or per block), add initial and lowest elevation of each block to Table 2, and state the datum in the captions of Fig8, Fig9 and Fig12. |
| Status | Table 2 values: verified (page image p. 13); PE values in Fig8 and Fig9: verified (measured by instances AB, S3, SD); datum actually used: inferred |
| Severity | moderate |
| Source | S3, SD, AB |

**GB-28 Fig6 swaps the labels of the two middle zones relative to Table 2, does not identify the ten points, and the position zones carry four different name sets.**

| Field | Content |
|---|---|
| Check | P38, P3, P29 |
| Location | p. 14, Fig6 and caption l. 268; p. 13, Table 2, column "Position"; p. 13, l. 256 to 257; p. 1, l. 28 to 29; p. 26, l. 484 to 485 |
| Quotation | "ten monitoring points were installed in the lower, lower-middle, upper-middle, and upper portions of the slide mass" and "Compared with the upper rock mass, the lower rock mass is compressed more frequently" |
| Concern | In Fig6 the zone labels read, from the crest downslope, "Top", "Lower middle part", "Upper middle part", "Bottom" (re-checked on the page image p. 14), with 2, 3, 3 and 2 points. In Table 2 the "lower middle part" holds IDs 3 to 5 at z = 465 to 498 m and the "upper middle part" IDs 6 to 8 at z = 660 to 692 m, so the two middle labels in Fig6 are swapped. The ten points are drawn in ten colours without IDs or colour key, the axes (0 to 2400, 0 to 3200, 0 to 800) have no quantity or unit, and the Table 2 coordinates (for example ID 1 at (-79,-284,340)) use a frame with negative x not shown in Fig6, so Block 1 and Block 3 of l. 397 and l. 416 cannot be located. The zones are called "bottom/top" (Table 2, Fig6), "lower/upper" (l. 256), "upper rock mass/lower rock mass" (l. 29) and "front portion/rear portion" (l. 484 to 485), without saying that these are the same; the position statements of the Abstract and Conclusion 4 rest on this assignment. |
| Suggestion | Swap the two middle labels in Fig6, number the ten points 1 to 10, add axis titles with units and the origin of the Table 2 coordinates, and use one set of position names in Table 2, l. 256, l. 29 and l. 483 to 487 (for instance "bottom, lower middle, upper middle, top"); define "front/rear" if it means something else. |
| Status | labels, points and Table 2 values: verified (page images p. 13 and 14); that the Fig6 labels and not Table 2 are wrong: inferred from the z coordinates |
| Severity | moderate |
| Source | S2, AB, S3, SD |

**GB-29 The ten monitored blocks, the block of Fig5 and the ten envelope times are called representative without a selection rule.**

| Field | Content |
|---|---|
| Check | P34 |
| Location | p. 13, l. 256 to 258 and Table 2; p. 11, l. 221; p. 23, l. 426 to 427 |
| Quotation | "to capture representative kinematics and deposition characteristics of the landslide blocks" and "presents a typical velocity-travel-distance curve for an individual block" |
| Concern | The number of landslide blocks is not given (25345 includes the base, l. 181). The ten blocks hold 11512.7 m³, 3.6 % of 317563 m³ (Python), and differ widely in initial energy density (0.67 to 7.11 MJ/m³ from Fig9 and Table 2). How they were chosen within each zone, and why the Fig5 block is typical, is not stated, yet results on these blocks are generalised to the "lower" and "upper" rock mass (l. 28 to 30). |
| Suggestion | In Sect. 2.3 state the selection rule (random within each zone, regular grid or other) and show, in a supplement, distributions of runout, collision count and energy change over all landslide blocks with the ten blocks marked. |
| Status | verified (text, Table 2); share and energy densities: inferred (calculation) |
| Severity | moderate |
| Source | SD |

**GB-30 The field investigations named as a basis of the inference are not reported, and all conclusions rest on model output.**

| Field | Content |
|---|---|
| Check | P19 |
| Location | p. 13, l. 264 to 266; p. 2, l. 65 to 66; p. 1, l. 26 to 30; p. 16, l. 345; p. 25 to 26, l. 461 to 492 |
| Quotation | "the sequence of failure and run-out at Mogangling was inferred by integrating the numerical results with field-investigation findings" |
| Concern | The aim names field investigations first (l. 65 to 66), and l. 265 to 266 says that the sequence of failure was inferred with field-investigation findings. Apart from two photographs in Fig7 (o), no field observation (mapping, deposit thickness, grain size, sections, survey date) is presented. Of the five conclusions, four (80 %) rest on simulation output and one (20 %) on the reconstructed topography; none rests on reported field measurements. The Abstract states "The results show that" for the landslide itself (l. 26) without saying that the statements concern the simulation. |
| Suggestion | Present the field data used in Sect. 2.1 or a supplement, or remove the references to field-investigation findings; phrase l. 26 to 30 and the conclusions as results of the simulation. |
| Status | verified (text); shares: inferred (count) |
| Severity | moderate |
| Source | SD |

**GB-31 The body enclosed by the alpha-shape envelope is called by seven different names, some of which denote a different object elsewhere.**

| Field | Content |
|---|---|
| Check | P38 |
| Location | p. 14, l. 269 to 272 and l. 278 to 280; p. 3, l. 88 to 89; p. 23, l. 427 and l. 429; p. 24, l. 438, l. 449 and l. 452; p. 25, l. 458; p. 26, l. 491; p. 4, Fig1; p. 23, Fig11 (a); compare p. 6, l. 140, p. 7, l. 146 and p. 8, Fig3 (a) |
| Quotation | "we quantify dispersion by extracting the volume and surface area of the deposition zone. An alpha-shape algorithm is applied to the slide mass" and "disintegration in the monitored block group" |
| Concern | The enveloped body is named "landslide accumulation area" (l. 88, l. 269, Fig1), "deposition zone" (l. 270, l. 272), "slide mass" (l. 272), "landslide mass" (l. 88 to 89, l. 278, l. 438), "deposit mass" (l. 427, l. 449, l. 491), "deposit region" (l. 429), "sliding mass" (l. 458) and "monitored block group" (l. 452). Fig11 (a), at t = 0 s, shows the envelope of the intact source mass, so the enveloped body is the whole moving mass, not a deposition zone. "Accumulation area" denotes a fixed terrain zone elsewhere (zone II of Fig3 (a), l. 140, l. 146), and "monitored block group" suggests the ten blocks of Table 2, whereas Fig12 shows the whole mass (its initial PE equals Fig8). A reader cannot tell whether VS and AG describe the dispersal of the deposit (l. 270) or of the whole mass (Eq. 5, Eq. 6, Fig11), which affects the interpretation in l. 445 to 456. |
| Suggestion | Name the enveloped body once in Sect. 2.4 (for instance "the sliding mass, that is, all blocks of the landslide body at time t"), use that name in l. 88 to 89, l. 269 to 280, l. 427 to 452, l. 458 and l. 491, rename the heading of Sect. 2.4, replace "monitored block group" in l. 452 by the same term, and reserve "accumulation area" for the terrain zone of Fig3 (a). |
| Status | text locations, Fig11 (a) and Fig3 (a): verified (page images); that the enveloped body is the whole mass: inferred from Fig11 (a), Eq. (5) and l. 278 |
| Severity | moderate |
| Source | S2, S3 |

**GB-32 The two dimensionless indices VS and AG appear under two names each, and the second name ("rate") suggests a time derivative.**

| Field | Content |
|---|---|
| Check | P38 |
| Location | p. 14, l. 274 to 275, Eq. (5) and (6); p. 1, l. 25; p. 3, l. 89; p. 14 to 15, l. 287 to 288; p. 24, l. 441; p. 25, l. 453 to 454; p. 26, l. 488; p. 4, Fig1; p. 25, Fig12 axis labels and caption l. 458 to 459 |
| Quotation | "two dimensionless indices are introduced: volume swelling (VS) and area growth (AG)" and "the volume expansion rate (VS) and surface area growth rate (AG) were calculated" |
| Concern | "Volume swelling" appears in l. 275, l. 287 to 288, Fig1 and on the Fig12 (a) axis; "volume expansion rate" in l. 25, l. 89, l. 441 and l. 453, "volume expansion" in l. 488. "Area growth" appears in l. 275, l. 288, Fig1 and on the Fig12 (b) axis; "(surface) area growth rate" in l. 25, l. 89 and l. 441, "surface area growth" in l. 453 and l. 488. The Fig12 caption uses neither and speaks of "a function of volume" and "a function of area" (l. 458 to 459), although the axes show VS and AG in percent. Eq. (5) and (6) define a relative change with respect to t = 0, not a change per unit time; Abstract, method overview and results all use "rate", which a reader takes as a time derivative, so the thresholds 29.47 % and 319.5 % become ambiguous. The higher grade applies because the naming affects how the solid-to-fluid criterion is read. |
| Suggestion | Use one name per index throughout ("volume swelling VS", "area growth AG", as in Eq. (5), (6), Fig1 and Fig12) and replace "volume expansion rate" and "(surface) area growth rate" in l. 25, l. 89, l. 441, l. 453 and l. 488; in the Fig12 caption write "(a) as a function of volume swelling VS; (b) as a function of area growth AG". |
| Status | verified (text counts; Fig1 and Fig12 labels on the page images) |
| Severity | moderate |
| Source | S2, S3, AB |

**GB-33 The values of VS and AG have no stated base: V0 and S0 are not reported, and V0 is defined differently from Vt.**

| Field | Content |
|---|---|
| Check | P20, P2 |
| Location | p. 14, l. 278 to 280, Eq. (5) and (6); p. 23, l. 426 to 429; p. 24, l. 440 to 441; p. 25, l. 453 to 454 and Fig12 (a) and (b) |
| Quotation | "V0 denotes the initial volume of the landslide mass (m³); Vt denotes the volume of the enclosing envelope at time t (m³)" |
| Concern | VS = 29.47 % means Vt/V0 = 1.2947 and AG = 319.5 % means St/S0 = 4.195; the curves of Fig12 end near VS of about 1250 % and AG of about 4250 to 4280 % (measured by instances S3 and S4). None of V0, S0, Vt or St is reported, so the ratios cannot be turned into volumes or areas or compared with other landslides. V0 is the volume of the landslide mass, Vt that of an envelope; a mass volume (317563 m³ or 2400×10⁴ m³, GB-13) and an envelope volume differ even at t = 0, while Fig12 starts at VS of about 0, which suggests that V0 is in fact the envelope at t = 0. The point set used for the envelope (block centroids or vertices) is not stated either. |
| Suggestion | In Sect. 2.4 define V0 and S0 as envelope volume and area at t = 0 (or state otherwise) and name the point set; in Sect. 3.4 add a table of V and S at each time point with V0 and S0. |
| Status | missing values: verified; that V0 is the envelope at t = 0: inferred (from Fig12) |
| Severity | moderate |
| Source | S3, SD |

**GB-34 The fixed α of 1 is said to ensure a tight envelope at all times, but neither this nor the sensitivity of VS and AG to α is shown.**

| Field | Content |
|---|---|
| Check | P26 |
| Location | p. 14, l. 281 to 284; p. 24, l. 440 to 444; p. 25, l. 453 to 454 and Fig12 |
| Quotation | "this study uniformly sets the α value to 1. This approach ensures a tight fit of the envelope model while minimizing geometric deviations introduced by parameter tuning." |
| Concern | Avoiding tuning by fixing α is a reasonable aim. But the mass passes from a compact body to a spread deposit (Fig11; envelope volume up to about 13.5 times V0 in Fig12 (a)), and one α cannot be shown to fit both without a test. Unit and convention of α (radius or inverse radius, in metres) are not stated; with 8.7 m blocks this decides whether the envelope closes or bridges gaps. The thresholds 29.47 % and 319.5 % (l. 453 to 454) and Conclusion 5 depend on this choice; this is why the finding is graded major. |
| Suggestion | In Sect. 2.4 state α with unit and convention and the software; add a sensitivity figure with VS and AG for at least three α values and report the 29.47 % and 319.5 % values for each. |
| Status | verified (text, Fig12) |
| Severity | major |
| Source | SD |

#### Minor corrections

| ID | Location | Quotation | Replacement | Source |
|---|---|---|---|---|
| KK-16 | p. 2 to 3, l. 76 to 77 | "the research method involves three parts" | "the research method involves four parts" (the text lists (1) to (4) and Fig1 shows four stages) | AB |
| KK-17 | p. 3, l. 77; p. 4, Fig1; p. 5, l. 92 | "(1) surface terrain restoration:" | "(1) Geo-mechanical model building (surface terrain restoration):", matching the first box of Fig1 and the heading of Sect. 2.1 | S2 |
| KK-18 | p. 4, Fig1, box "Global Perspective" | "P0E", "PtE", "KtE" | "PE(t0)", "PE(t)", "KE(t)", as in Eq. (1) to (4) | AB |
| KK-19 | p. 5, l. 105 (twice) | "colluvial Deluvial deposit" | "colluvial-deluvial deposit" | ZF |
| KK-20 | p. 6, Fig2 (b), legend | "Daduhe River" | "Dadu River" (as in Fig2 (c), Fig3 and the text) | S2, AB |
| KK-21 | p. 10, l. 193 to 195 | "In the course of a discrete-element simulation-particularly when modeling nominally semi-infinite bodies such as the use of fixed or elastic boundaries in a static analysis will inevitably reflect outbound seismic waves" | "In a discrete-element simulation, particularly when modeling nominally semi-infinite bodies, the use of fixed or elastic boundaries in a static analysis will inevitably reflect outbound seismic waves" (the sentence has no main clause) | ZF |
| KK-22 | p. 11, Table 1 title (l. 213) | "Table 1 Physical parameters of rock mass and discontinuities" | "Table 1: Physical parameters of rock mass and discontinuities" (same form as Table 2) | S2 |
| KK-23 | p. 12, Fig5 (a), legend | "Non-obvios acceleration" | "Non-obvious acceleration" | AB |
| KK-24 | p. 13, l. 246 | "where, at time ti, PE(ti), and DE(ti) can be expressed as:" | "where KE(ti), PE(ti) and DE(ti) at time ti can be expressed as:" | SD |
| KK-25 | p. 13, Table 2, last row (ID 11) and title l. 267 | "Table 2: The basic information of blocks where the 10 monitoring points are located" | remove row 11 and add below the table: "In addition, the maximum unbalanced force of the model was recorded (l. 258 to 259)."; the IDs 1 to 10 then denote the monitored blocks only, as in Fig9 and Fig10 (a) | S2, S3 |

#### Verification log

| ID | Check | Checked | Values | Result |
|---|---|---|---|---|
| PP-08 | P4 | Every reference to a figure, panel or table against its target on the page image | Fig1 (l. 76) flow chart; Fig2 (l. 93) location, Caihong bridge in panel (c); Fig4 (l. 173); Fig5 (l. 220, l. 229 to 230) thresholds 10 to 50 % match the caption; Fig6 (l. 256); Table 1 (l. 212); Table 2 (l. 259); Fig7 (l. 301 to 353) seven times in the caption, panel pairs b/i to g/n in text order; Fig8 to Fig12 (l. 375 to 443) match | references in order except GB-12, GB-15 and KK-29 |
| PP-09 | P29, P3 | Figure inventory | twelve figures, numbered 1 to 12 without gaps, all embedded raster images (272 to 743 ppi), each cited in the text of its section; no graphical abstract, no appendix figures | no finding |
| PP-10 | P29, P3 | Fig1 against l. 76 to 90 | four stages counted, matching items (1) to (4); VS, AG, KE, PE, DE written out; "α=1" agrees with l. 283 | KK-16, KK-18 |
| PP-11 | P36 | Approximate statements against the manuscript's own records | "nearly 20 large and super large earthquake landslides" (l. 99 to 100), no record given; "about 450 m", "about 100 m", "about 2400×10⁴ m³" against model values; "approximately 20 meters thick" fractured layer (l. 328), no measurement shown; "Around 13 seconds" (l. 383) consistent with Fig8 | no finding beyond GB-13 |
| PP-12 | P3 | Scales and section geometry in Fig2 and Fig3 | Fig2 (c) section a-a' 1546 m long, azimuth 74.1° (text 75°, l. 149); Fig3 (b) x extent 1544 m, consistent with a-a' if not exaggerated; scale bars of Fig2 (b), Fig2 (c), Fig3 (a) and Fig3 (c) regular | no finding; disclosed: none |
| PP-13 | P1 | Geometric products and relief used as inputs | 450 m × 1000 m = 0.45 km², consistent; relief 2000 m to 1115 m = 885 m against model 747 m plus 131 m = 878 m, difference 0.8 %, consistent; 0.45 km² × 100 m = 4500×10⁴ m³ against 2400×10⁴ m³ not consistent | finding GB-13; disclosed: dimensions given as approximate |
| PP-14 | P3 | Colours of Fig3 (a) against its legend | legend Granite #744c3c, Diorite #8c7c74, Massive gravelly soils #b49c74, Sand and pebble gravel #8c745c; block faces differ from their legend field by 6 to 18, the grey bottom layer by 35 from Diorite, all within the tolerance of 40 | no finding |
| PP-15 | P37 | Whether figures show corrected or reconstructed values without saying so | restored terrain in Fig3 (c) labelled "before and after restoration" (l. 167); no recalculation reported for Fig8, Fig9, Fig12 | no finding |
| PP-16 | P38 | Names of software, event, faults and authors | "3DEC" twice without variant (l. 169, l. 196); "Kangding earthquake" three times (l. 110, l. 183, l. 188) with "Ms7 ¾"; the title of Zhao et al. (2021) "1786 Moxi M 7.75 earthquake" is a cited title (7¾ = 7.75); "Dadu River fault (Detuo fault)" explained (l. 147); contribution initials YG, BH, HT, XF, LZ match the five authors | no finding |
| PP-17 | P3 | Labels of Fig4 against the text | "1021m", "747m", "179m", "131m" agree with l. 174 to 175; axis ranges compatible with 2788 m by 3341 m (l. 181); height not measurable in the perspective view | no finding; see GB-40 for the height |
| PP-18 | P3 | Counts and ranges in Fig5 | Fig5 (a): 6 red and 5 purple markers, colours identical to the legend; inset and grey box in (d) both 1549 to 1833 m and 14 to 26 m/s; velocity axis of (b) and (d) linear | no finding beyond GB-23, GB-25, GB-26 |
| PP-19 | P7 | Whether one method version applies to all reported data | one dynamic run (0 to 131 s); 7 snapshot times (Fig7); 10 envelope times (Fig11); thresholds 10 to 50 % applied to one curve; no protocol, software or parameter change reported; whether the 30 % threshold was applied to all ten blocks is not stated | no finding beyond GB-25 |
| PP-20 | P32 | Results called confirmed or acceptable and any independent check | collision detection "deemed acceptable" (l. 232 to 233) without check against contacts; validation "compelling evidence" (l. 353) without measure | covered by GB-22, GB-39 |
| PP-21 | P38 | Energy symbols in text and figures | KE, PE, DE, ME defined in l. 241 to 243, used in l. 287, l. 290, l. 442 to 443; legends "PE, KE, DE" in Fig8 (1 panel), Fig9 (10 panels), Fig12 (2 panels); Fig1 writes the three terms out; 13 of 13 panels consistent | no finding except KK-01 |
| PP-22 | P38, P2, P3 | Number and identifiers of the monitored blocks across text, tables and figures | Table 2 IDs 1 to 10 in groups 2 + 3 + 3 + 2; Fig6 ten points in the same grouping; Fig9 panels (a) to (j) for "point 1" to "point 10" (l. 410 to 413); Fig10 (a) legend 1 to 10; "Block 1", "Block 3" (l. 397, l. 416) linked to points by the Table 2 title | consistent apart from GB-28, GB-46 and KK-25 |
| PP-23 | P27 | Where outputs of untested components flow | restored topography to mass geometry, volume and PE(t0); surrogate record to initiation stages and velocities; 30 % threshold to collision counts, Fig10 (b) and Conclusion 4; α = 1 to VS and AG thresholds and Conclusion 5 | covered by GB-13, GB-18, GB-22, GB-34, GB-49 |

### Segment 3: Results (p. 15 to 25, l. 297 to 459)

#### Substantive findings

**GB-35 Several analyses announced in the methods are not reported in the results: stress and displacement histories, the maximum unbalanced force and the simulated runout.**

| Field | Content |
|---|---|
| Check | P11 |
| Location | p. 15 to 16, Sect. 3.1, l. 299 to 359; p. 13, l. 258 to 263 and Table 2, column "Monitoring contents"; p. 2, l. 69 to 71; p. 18, Fig7 (h) to (n) |
| Quotation | "the maximum unbalanced force was tracked to verify that the model reached post-failure stability" and "displacement, velocity, and stress histories were extracted for each of the ten monitored blocks in all relevant directions" |
| Concern | Announced outputs against results: velocity of the whole mass, reported (l. 304 to 347, Fig7 (a) to (g)); stress of the whole mass, maps shown (Fig7 (h) to (n), colour-bar limits 0, minus 33, minus 31, minus 33, minus 33, minus 33, minus 47 MPa) but not interpreted anywhere; displacement of the whole mass and runout distance, not reported, although the aim announces "movement trajectory" and "debris flow propagation characteristics" (l. 70); per-block displacement components only as unscaled 3-D trajectories (Fig10 (a)); per-block velocity and stress histories (Stress-XX, YY, ZZ), not reported; maximum unbalanced force (ID 11), not reported, so the stated stability check cannot be followed. No reason is given. |
| Suggestion | Add to Sect. 3.1 the simulated runout distance, travel angle or H/L and deposit dimensions, a short interpretation of Fig7 (h) to (n) and the history of the maximum unbalanced force; report per-block velocity and stress histories in Sect. 3.2.2 or a supplement, or remove them from Table 2 and l. 262 to 263. |
| Status | verified (absence in Sect. 3 and in all result figures) |
| Severity | moderate |
| Source | S3 |

**GB-36 The stress panels Fig7 (h) to (n) do not say what is plotted, and the text calls a vertical section the sliding plane.**

| Field | Content |
|---|---|
| Check | P29 |
| Location | p. 15, l. 301 to 302; p. 18, Fig7 (h) to (n); caption l. 368 to 370 |
| Quotation | "Fig7 illustrates the cloud maps of velocity distribution for the overall model and stress distribution along the sliding plane" |
| Concern | The panels are vertical sections with axes numbered 0 to 2700 and 0 to 1200 but without quantity or unit; neither caption nor text gives the position of the section in plan or the stress component (vertical stress, minimum principal stress, mean stress). The text says "along the sliding plane", but the panels show a vertical section through the whole model. |
| Suggestion | Add axis titles with units, mark the section line in Fig4 or Fig6, name the stress component in the caption, and correct "along the sliding plane" in l. 302 if a vertical section is meant. |
| Status | verified (page image p. 18) |
| Severity | moderate |
| Source | AB |

**GB-37 Fig7 (h) shows zero stress everywhere at t = 0 s, although the dynamic analysis starts from static equilibrium, and Fig7 (a) draws zero velocity in the colour of the other end of the scale.**

| Field | Content |
|---|---|
| Check | P3 |
| Location | p. 15, l. 304 to 305; p. 17 to 18, Fig7 (a) and (h); p. 10, l. 199 to 201 |
| Quotation | "Fig7. (a) and (h) show the initial state of the landslide, during which the slope has not yet been affected by seismic forces" and "Dynamic loading must be introduced only after the model has attained static equilibrium" |
| Concern | Panel (h) is uniformly red (#ec0404, the "0" end of its colour bar, which runs "0" to "0Mpa"); in (i), 3 s later, the colours span 0 to minus 33 MPa. Under gravity in static equilibrium the vertical stress at the base is of the order ρgh ≈ 2700 × 9.81 × 1200 ≈ 32 MPa (Python), which matches (i) to (m), not (h). Panel (h) therefore seems to show the state before gravity was applied. Panel (a) is uniformly red, while zero velocity is blue in (b) to (g); the same value has different colours. |
| Suggestion | Replace (h) by the stress field after static equilibrium, or state in the caption that (h) precedes gravity loading and add the equilibrated state; draw (a) with the colour scale of (b) to (g). |
| Status | colours: verified (measured by instance AB; panel (h) re-checked on the page image p. 18); interpretation as a pre-gravity state: inferred |
| Severity | moderate |
| Source | AB |

**GB-38 Seismic wave mechanisms in Sect. 3.1 are stated as results, but no output that measures them is reported.**

| Field | Content |
|---|---|
| Check | P31 |
| Location | p. 15, l. 307 to 313 and l. 315 to 321; p. 13, Table 2, column "Monitoring contents" |
| Quotation | "The first-arriving P-waves caused intense vertical dislocation along the steeply dipping structural planes outside the slope." and "The back-slope effect and amplification at higher elevations during seismic wave propagation significantly increased the peak ground acceleration of the Mogangling slope" |
| Concern | The monitored quantities are displacement, velocity and stress (Table 2); no acceleration histories, PGA values at different elevations or amplification factors are shown, and the input components are not stated, although vertical motion from P waves requires a vertical component. The model contains one uniform structural plane, and pre-existing planes were ignored (l. 175 to 180, GB-21), so "steeply dipping structural planes" are not described in the model. The mechanisms may be correct, but as written they are interpretation, not outcome of this simulation; they carry the stage narrative of the results, hence the grade. |
| Suggestion | Show acceleration histories at monitoring points along the slope height, the resulting PGA amplification relative to the base and the input components in Sect. 3.1; otherwise mark l. 307 to 321 as interpretation from the literature, with references. |
| Status | verified (Table 2, absence in Sect. 3.1) |
| Severity | major |
| Source | SD |

**GB-39 The validation of the simulation is qualitative, yet the results call it compelling and Conclusion 2 says it ensures agreement; Conclusion 2 also credits the model with geological structures that were left out.**

| Field | Content |
|---|---|
| Check | P11, P15, P31 |
| Location | p. 16, l. 353 to 359; p. 19, Fig7 (o); p. 25, l. 469 to 472; p. 7, l. 148 to 156; p. 9, l. 175 to 180 |
| Quotation | "Fig7. (o) presents compelling evidence of agreement between the numerical simulation results and the actual field observations." and "Comparison with field imagery and result analysis ensures that the simulation outcomes align with actual conditions." |
| Concern | The comparison case "field" carries numbers (l. 148 to 156: about 450 m long, about 1000 m wide, 0.45 km², toe at 1120 m, platform at 1330 to 1380 m, slopes of 50°, 5 to 12°, 35° and 57°); the case "simulation" carries only an image and two qualitative correspondences (a ridge dividing the source area; extent and morphology of the deposit "closely match", l. 357 to 358). No simulated deposit length, width, area, thickness, toe elevation or dam height is given, and Fig7 (o) marks two rectangles without dimensions. The manuscript discloses centuries of weathering (l. 354 to 355) but does not say how this limits the comparison; it limits but does not prevent a comparison of deposit extent and dam position. The results themselves say "support" (l. 359), Conclusion 2 says "ensures". Conclusion 2 also lists "geological structures" among what the simulation incorporates (l. 469), although the structural planes "can not be obtained" and their impact "has to be ignored" (l. 176 to 177). The study criticises earlier work for lacking "a quantitative and systematic study" (l. 63 to 64) and validates qualitatively. |
| Suggestion | Add to Sect. 3.1 a table "field versus simulation" with deposit length, width, area, thickness or dam height and toe elevation, the deviation for each and the weathering caveat per quantity, and overlay the simulated final deposit on the UAV DEM with an overlap measure (for example intersection over union). In Conclusion 2 replace "ensures" by the measured agreement and remove or qualify "geological structures" ("a uniform structural plane in place of the unknown pre-failure structure"). |
| Status | verified (text, Fig7 (o) on the page image) |
| Severity | major |
| Source | S3, S4, SD |

**GB-40 If the vertical axis of Fig7 (h) is height in metres, the section reaches about 1417 m, while the model is stated to be 1121 m high.**

| Field | Content |
|---|---|
| Check | P3 |
| Location | p. 18, Fig7 (h); p. 9, l. 181 to 182 |
| Quotation | "The whole model contains 25345 blocks, 2788 m long, 3341 m wide, 1121m high" |
| Concern | The top of the section in (h) measures 1417 ± 10 (ticks 1200 and 0, regular spacing of 40 px per 200); the x extent (to about 2790) matches the 2788 m model length, the height does not match 1121 m (difference about 300, far above the uncertainty). Because the axis has no title (GB-36), the unit is assumed. |
| Suggestion | Check the model height in l. 182 against the section, or state what the vertical axis of (h) to (n) represents. |
| Status | crest height: verified (measured by instance AB; crest above the 1200 tick re-checked on the page image p. 18); meaning of the axis: inferred |
| Severity | moderate |
| Source | AB |

**GB-41 Fig7 (o) compares model and photographs without scale, orientation or photo details.**

| Field | Content |
|---|---|
| Check | P29 |
| Location | p. 19, Fig7 (o); caption l. 369 to 370; p. 16, l. 353 to 359 |
| Quotation | "(o) Validation of numerical simulation results against real-world evidence." |
| Concern | The model view and the two photographs have no scale, no north arrow or viewing direction, and the photographs have no date or source; the model time of the view is not stated (presumably 131 s). The reader cannot judge whether the boxes "Protrusion at the source area" and "Landslide deposit area" cover the same ground in model and photograph. |
| Suggestion | Add viewing direction, approximate scale, photo date and source, and model time to the caption. |
| Status | verified (page image p. 19) |
| Severity | minor |
| Source | AB |

**GB-42 The energy conservation reported for the whole landslide is an identity of Eq. (4), and the non-conservation reported for single blocks is contradicted by Eq. (4) and by the constant totals in Fig9.**

| Field | Content |
|---|---|
| Check | P23, P2, P15, P31, P5, P3 |
| Location | p. 19, l. 375 to 377 and l. 386 to 389; p. 20, l. 393 to 402; p. 12 to 13, l. 241 to 252, Eq. (1) to (4); p. 20, Fig8; p. 21 to 22, Fig9 (a) to (j); p. 1, l. 26 to 28; p. 25 to 26, l. 476 to 482; p. 4, Fig1; p. 10, l. 189 to 197 |
| Quotation | "It is evident that, due to the law of energy conservation, the total sum of the three forms of energy remains constant throughout the landslide." and "This can be regarded as a successful energy extraction numerical simulation." and "unlike the total landslide mass, the energy of single blocks is not conserved" |
| Concern | The energy terms are clearly defined (Eq. 1 to 4), which makes the balance easy to follow. With ME = KE + PE (Eq. 1) and DE(ti) = ME(t0) minus ME(ti) (Eq. 4, l. 249), KE + PE + DE equals ME(t0) at every time step for any history of velocities and heights, including physically wrong ones; a check over 100000 random states returns the identity in every case (Python, zf/rechnungen.py; instances S3 and S4 obtained the same). The constant stacked total of Fig8 (6449 to 6516 GJ over all bar columns, measured by instances S3, S4, SD and AB) is therefore bookkeeping, not evidence for conservation or for a "successful" simulation (l. 388 to 389). The same identity holds per block, because Eq. (1) to (4) are introduced "For an individual rock block" (l. 243), and Fig9 indeed shows constant totals for every block (about 5.05, 5.12, 4.00, 3.56, 11.05, 6.57, 1.18, 4.36, 1.59 and 0.95 GJ for blocks 1 to 10 in instances S3 and SD; instance AB reads 10.56 GJ for block 5). The statement that block energy "is not conserved" (l. 393 to 394, Conclusion 3) thus uses a different criterion, a temporary decrease of the residual DE (l. 399 to 402), which is a rise of ME through work by neighbouring blocks; internal work cancels in the sum over all blocks. A measurable net DE decrease occurs only in blocks 1 (0.379 GJ, 7.5 % of PE0), 3 (0.355 GJ, 8.9 %), 9 (0.028 GJ) and 7 (0.018 GJ) (instance AB); the Abstract says "For some blocks", while l. 393 to 394 and Conclusion 3 generalise to single blocks as such. The rebound explanation in l. 398 (bouncing to the opposite bank raises PE) converts KE into PE and does not by itself raise ME. In addition, the seismic input at the base (l. 189 to 191) adds work and the viscous boundaries (l. 196 to 197) remove radiated energy; both are folded into the residual DE, so DE is not dissipation alone, and the stated aim of separating accumulation, transfer and dissipation (l. 67 to 68) cannot be met. Case A: DE is the residual of Eq. (4); then the balance closes trivially, and the block result is a statement about the sign of dDE/dt. Case B: DE was tracked independently (frictional, damping and boundary work from 3DEC); then Eq. (4) is not what was used, and the constant totals would be a genuine test. The manuscript names only the formula of case A. |
| Suggestion | In Sect. 2.3 state whether DE is the residual of Eq. (4) or an independently tracked quantity. If residual, remove the conservation statements (Abstract l. 26 to 27, l. 375 to 377, l. 388 to 389, Conclusion 3 l. 477 to 479) and rephrase the block result (l. 393 to 402, Abstract l. 27 to 28, Conclusion 3) as transient gains of mechanical energy through work by neighbouring blocks, restricted to the blocks that show them. Counter-design: record the work of the seismic input at the base, the energy absorbed by the viscous boundaries, the frictional and the damping work as separate histories, show in Fig8 whether their sum with KE and PE closes to ME(t0), with the closure error over time, and plot per block the contact work from contact forces and velocities. |
| Status | identity: verified (Eq. 4, Python); constant totals in Fig8 and Fig9 and DE decreases per block: verified (measured by instances S3, S4, SD, AB); input and boundary terms within DE: inferred from l. 189 to 197 and Eq. (1) to (4); which case applies: inferred |
| Severity | major |
| Source | S3, S4, SD, AB |

**GB-43 Three methodological limitations appear only in the results or conclusions, not where the methods are introduced.**

| Field | Content |
|---|---|
| Check | P17 |
| Location | p. 20, l. 399 to 402 (method at p. 13, l. 249); p. 25, l. 466 to 468 (method at p. 6 to 7, l. 136 to 162); p. 16, l. 353 to 355 (no methods section for the validation) |
| Quotation | "Instances where dissipated energy appears to decrease are actually due to the calculation method used." and "The landslide deposit area is often difficult to restore due to the lack of surrounding reference features." |
| Concern | A reader of Sect. 2.3 does not learn that DE can decrease; a reader of Sect. 2.1 does not learn that the deposit area is hard to restore and whether the remedy of l. 467 to 468 (referencing other mountain areas) was applied here; the effect of weathering on the validation appears only in Sect. 3.1. |
| Suggestion | Move each limitation to the place of its method: after Eq. (4) in Sect. 2.3, after l. 140 in Sect. 2.1, and into a short validation paragraph in Sect. 2. |
| Status | verified (text) |
| Severity | moderate |
| Source | SD |

**GB-44 The position-wise collision and energy-transfer result of the Abstract and Conclusion 4 has no counterpart in the results, and the statement that collisions rise continuously with travel distance does not match Fig10 (b).**

| Field | Content |
|---|---|
| Check | P11, P15, P21, P10, P2, P3 |
| Location | p. 22, l. 414 to 421; p. 23, Fig10 (a) and (b); p. 1, l. 28 to 30; p. 3, l. 86 to 87; p. 13, Table 2, column "Position"; p. 26, l. 483 to 487 |
| Quotation | "Fig10. (b) presents the frequency of effective collisions experienced by blocks at different locations during the landslide process" and "the front portion of the rock mass experiences more collisions than the rear portion, with a clear trend of decreasing collision frequency toward the rear" |
| Concern | The methods define four position groups (Table 2) and announce an analysis by part of the mass (l. 86 to 87). The results never report collision counts, energy received or travel distance per group, per block or per stage. Fig10 (b) is one pooled series of frequency against travel distance with one fitted curve, without block, position or stage dimension, so it cannot show "blocks at different locations"; Fig10 (a) shows displacement trajectories from a common origin in perspective projection, without distance values. None of the three Abstract claims (the lower rock mass is compressed more frequently, receives more energy transfer and travels farther, l. 28 to 30) and none of the Conclusion 4 claims (front versus rear during the collapse stage, rear mass transferring energy to the front, which therefore slides farther) is backed by a number, table or panel; Conclusion 4 also generalises from ten monitored blocks to "the entire landslide mass". Blocks that travel farther collect more collisions simply through a longer path and time in motion, so counts would need normalisation per metre or per second, and energies between blocks of 756.2 to 1754.3 m³ would need specific energy (J/kg); the causal direction ("enabling the front portion to slide farther") cannot be shown by tracer blocks in a single run. Finally, "rises continuously" (l. 419) is not borne out: of 25 successive bins, 5 decrease (16 to 7 at 700 to 800 m, 27 to 20 at 900 to 1000 m, 30 to 28 at 1200 to 1300 m, 157 to 150 and 150 to 146 at 2300 to 2500 m; values measured by instances S3, AB and SD, Python count; instance AB reported four decreases, its own values show five), and the travel distance at which blocks enter the river channel is not stated. |
| Suggestion | Add to Sect. 3.2.2 a table per monitored block and per position group, split by the stages of Sect. 3.1, with travel distance, effective collisions, collisions per 100 m and per second in motion, and energy received from neighbours (sum of positive ME increments, in GJ and J/kg); show for one rear and one front block the DE and KE series around collision times. For the causal claim, counter-design: a comparison run with the rear mass removed or fixed, reporting the change of front runout and front-block energy. Otherwise restrict the Abstract (l. 28 to 30) and Conclusion 4 to "collision frequency increases overall with travel distance", write "rises overall" in l. 419 and give the distance of the river channel. |
| Status | absence of per-block, per-zone and per-stage results: verified (Sect. 3, Fig10 on the page image); Fig10 (b) values: verified (measured); causal limitation: inferred |
| Severity | major |
| Source | S3, S4, SD, AB |

**GB-45 Fig10 (b) does not explain the fitted curve, the bin width or what "Frequency" counts, and the axis labels of Fig10 (a) are illegible.**

| Field | Content |
|---|---|
| Check | P29 |
| Location | p. 23, Fig10 (a) and (b); caption l. 423 to 424 |
| Quotation | "Fig10. (a) movement trails of 10 monitoring points and (b) the plot of travel distance vs. collision frequency." |
| Concern | The red curve in (b) is neither named nor given an equation or goodness of fit; the points are spaced 100 m (26 bins from 0 to 2500 m), but the bin width is not stated; whether "Frequency" counts collisions of the ten monitored blocks or of all blocks is open (GB-25). The axis labels of (a) are about 1.5 pt at print size. |
| Suggestion | Name the fit (type, equation, R²), state bin width and counted population in the caption, and enlarge the axis labels of (a). |
| Status | verified (page image p. 23) |
| Severity | minor |
| Source | AB |

**GB-46 The text reports envelope fitting at ten time points, but each curve in Fig12 has more than twenty data points.**

| Field | Content |
|---|---|
| Check | P2, P11, P5, P3 |
| Location | p. 23, l. 426 to 428; p. 24, Fig11 caption l. 437 to 439 and l. 440 to 441; p. 25, Fig12 (a) and (b) |
| Quotation | "to perform Alpha Shape envelope fitting on the deposit mass at 10 representative time points" |
| Concern | Fig11 shows ten envelopes (t = 0, 3, 7, 9, 12, 15, 32, 71, 100, 131 s), and l. 440 to 441 derives VS and AG "at each time point". Each curve of Fig12 carries at least 22 separately detectable markers (lower bound in instance AB; about 30 in instance S3; more than 20 in instance SD). Either VS and AG were computed at more times than reported, or Fig12 interpolates; in both cases its sampling is not described, Fig12 carries no time labels, and this bears on GB-48. |
| Suggestion | In Sect. 3.4 state the number and times of the samples used in Fig12, whether values between them are interpolated, and list t, VS, AG, KE, PE and DE per sample in a table consistent with Fig8. |
| Status | verified (page image p. 25; exact marker count approximate) |
| Severity | moderate |
| Source | S3, AB, SD |

**GB-47 Fragmentation, debris production and a solid-to-fluid transition are concluded, but no fragmentation measure is reported, the model as described has no breakage mechanism, and envelope growth of the reported size reflects spreading rather than interior filling.**

| Field | Content |
|---|---|
| Check | P15, P25 |
| Location | p. 24 to 25, l. 445 to 456; p. 26, l. 488 to 492; p. 9, l. 178 to 182; p. 16, l. 325 to 329; p. 25, Fig12 |
| Quotation | "These newly generated fragments fill the interior and surface of the deposit mass, causing a sudden expansion of the envelope volume and a sharp increase in surface area." and "it can be considered that the landslide transitions from a solid phase to a fluidized phase" |
| Concern | The results report a co-variation of KE amplitude with the growth of VS and AG (l. 443 to 444) and then "This phenomenon can be interpreted as follows" (l. 445); Conclusion 5 turns the interpretation into "it can be concluded" (l. 489). The model consists of a fixed set of blocks of 8.7 m × 8.7 m plan size (l. 178, l. 181) with one uniform structural plane; no breakage criterion, sub-block discretisation, number of separated blocks, broken contacts or fragment size distribution is reported, so the "large amounts of debris" and the "fine debris such as rock fragments" (l. 326) are not measured. Fig12 reaches VS of about 1249 % and AG of about 4281 % (measured by instance S4), that is, an envelope of about 13 times the initial volume and about 44 times the initial area; fragments that fill the interior of a mass do not enlarge its envelope, while spreading along the runout path does, and spreading with frictional sliding explains the joint rise of VS, AG and DE without fragmentation. A rise of DE, a residual (GB-42), cannot confirm fragmentation (l. 451 to 452). The solid-to-fluid threshold is placed at the KE peak (1116.8 GJ, 17.2 % of the initial 6503 GJ), so the criterion is defined by the quantity it is meant to explain, and no fluidisation measure is given. Can blocks fracture in the 3DEC model, or only separate along predefined joints? |
| Suggestion | Report in Sect. 3.4 a fragmentation measure from the model (number of block groups or broken contacts over time) next to VS and AG, separate spreading from densification (for example envelope volume divided by solid block volume), and state in Sect. 2.1 whether and how blocks can break; otherwise rewrite l. 445 to 456 and Conclusion 5 as block separation and spreading, phrase Conclusion 5 as an interpretation, and use a fluidisation criterion independent of KE (for example granular temperature or coordination number). |
| Status | absence of a fragmentation measure and of a breakage mechanism: verified (Sect. 2.1, 2.4, 3.4); VS and AG maxima: verified (measured); geometric argument: inferred from Eq. (5); circularity of the threshold: verified (l. 453 to 455, Fig12); whether 3DEC blocks can break in this set-up: assumption, therefore asked as a question |
| Severity | major |
| Source | S4, SD |

**GB-48 The kinetic-energy peak marked in Fig12 (1116.8 GJ) is about one third lower than the kinetic-energy maximum in Fig8, so the transition values 29.47 % and 319.5 % do not belong to the kinetic-energy peak they are tied to.**

| Field | Content |
|---|---|
| Check | P2, P22, P3 |
| Location | p. 24 to 25, l. 452 to 455; p. 25, Fig12 (a) and (b), labels "1116.8", "29.47", "319.5"; p. 20, Fig8; p. 19, l. 381 to 383 |
| Quotation | "When the volume expansion rate reaches approximately 29.47% and the surface area growth reaches about 319.5%, it can be considered that the landslide transitions from a solid phase to a fluidized phase. At this point, the kinetic energy peaks" |
| Concern | Measured KE in Fig8: about 1082 GJ at 11.1 s, 1570 GJ at 12.4 s and 1657 GJ at 13.6 s (instance AB, ± 10 GJ), or 1140, 1590 and 1685 GJ at 11, 12 and 13 to 14 s (instance S3); 1116.8 GJ matches neither the maximum, which exceeds it by 48.4 to 50.9 % (Python), nor any of the envelope times listed for Fig11. Initial PE and final DE agree between Fig8 and Fig12 (about 6500 GJ), so both show the whole mass. Case A: the samples of Fig12 skip 12 to 14 s, and 1116.8 GJ is the value at about 11 s; then 29.47 % and 319.5 % belong to a point before the KE peak, and VS and AG at the peak are unknown. Case B: Fig8 and Fig12 use different KE computations or mass sets; l. 452 speaks of "the monitored block group", but the equal totals argue against it. The time of the transition is not stated and can only be inferred by combining both figures (P22). These two values are the only quantitative result of Sect. 3.4, hence the grade. |
| Suggestion | In Sect. 3.4 state the time of the marked point, use the same samples in Fig8 and Fig12 (or add the 12 to 14 s samples to Fig12), recompute VS and AG at the actual KE maximum and revise l. 453 to 455 accordingly. |
| Status | Fig8 values: verified (measured by instances AB and S3); Fig12 labels: verified (page image p. 25); which case applies: inferred |
| Severity | major |
| Source | S3, AB, SD |

#### Minor corrections

| ID | Location | Quotation | Replacement | Source |
|---|---|---|---|---|
| KK-26 | p. 18, Fig7 (h) to (n), colour bars | "-33Mpa", "-31Mpa", "-47Mpa", "0Mpa" | "-33 MPa", "-31 MPa", "-47 MPa", "0 MPa" | AB |
| KK-27 | p. 20, l. 397 | "exhibit a rebound in potential energy after it approaches zero" | "exhibit a rebound in potential energy after their potential energy approaches zero" | ZF |
| KK-28 | p. 23, l. 425 (section heading) | "3.4 Structural evolution as a function of energy change" | "3.3 Structural evolution as a function of energy change" (Sect. 3.3 does not exist; numbering jumps from 3.2.2 to 3.4) | S3, S4, SD |
| KK-29 | p. 24, l. 438 (Fig11 caption) | "(a-i) when time = 0s, 3s, 7s, 9s, 12s, 15s,32s,71s, 100s, 131s." | "(a) to (j) at t = 0, 3, 7, 9, 12, 15, 32, 71, 100 and 131 s." (ten panels and ten times) | S3, S4, SD, AB |
| KK-30 | p. 24, l. 440 | "we first extracted its volume (V) and surface area (A) at each time point" | "we first extracted its volume (V) and surface area (S) at each time point" (Eq. 6 uses S0 and St) | S2, S3 |

#### Verification log

| ID | Check | Checked | Values | Result |
|---|---|---|---|---|
| PP-24 | P6 | Absolute statements | "entire process" (l. 299) refers to the motion, the dam break being excluded (l. 348 to 350); "remains constant throughout" (l. 376 to 377); "rises continuously" (l. 419); "ensures" (l. 471); "continuous increasing trend" (l. 429) not checkable against time because Fig12 has no time labels | no finding beyond GB-39, GB-42, GB-44 |
| PP-25 | P2 | Total duration in all places | 131 s in l. 300 to 301, Fig7 caption (l. 368 to 369), Fig11 caption (l. 438 to 439); last bar of Fig8 at 131.2 s (measured); Fig9 time axes end at about 131 s | consistent; disclosed: none |
| PP-26 | P33 | Statements of effort or extent used as result or limitation | "131 seconds" (l. 300) is a simulated duration; no computing time or field days stated or used | no finding |
| PP-27 | P2, P24 | Stage velocities in Sect. 3.1 against the colour-bar maxima of Fig7 (a) to (g) | 3 s 5.9 m/s (l. 307), 7 s 19.6 m/s (l. 315), 9 s 27.1 m/s (l. 322), 12 s 31.6 m/s (l. 330), 15 s 25.7 m/s (l. 339), 131 s "approached 0 m/s" against 0.21 m/s (l. 346 to 347); stress colour-bar ends minus 33, minus 31, minus 33, minus 33, minus 33, minus 47 MPa, not stated in the text | consistent; disclosed: velocities given only at the sampled times |
| PP-28 | P2, P24 | Timing of the motion stages in Sect. 3.1 and 3.2.1 against Fig8 | bars every 1.25 s; 0 to 3 s PE 6497 to 6469 GJ, KE about 0; KE 766 GJ at 9.9 s, 1082 GJ at 11.1 s, 1570 GJ at 12.4 s, 1657 GJ at 13.6 s (maximum), 804 GJ at 14.9 s; text: KE rises from 3 to 12 s and drops "Around 13 seconds" (l. 381 to 384), within about one bar | consistent; the mismatch with Fig12 is GB-48; disclosed: dam break not modelled (l. 348 to 350) |
| PP-29 | P23 | Closure of the whole-mass energy budget across figures | Fig8 stacked total 6449 to 6516 GJ (median 6516 GJ); Fig12 initial PE and final DE about 6500 GJ; Fig8 final PE about 0 | closes in all three places; that it closes by definition is GB-42; disclosed: DE decreases attributed to the calculation method (l. 399 to 400) |
| PP-30 | P30 | Reported errors and their correction | no error or correction reported; the DE decreases (l. 399 to 400) are explained, not corrected | no finding; placement of the explanation is GB-43 |
| PP-31 | P3 | Fig9 per block | axis maximum, PE0, minimum PE, PE at 131 s, KE maximum, drop PE0/(mg): 1: 6, 5.04, 0, 0.344, 0.26 GJ, 237 m; 2: 6, 5.11, 0, 0, 0.28, 221 m; 3: 5, 3.99, 0, 0.316, 0.26, 234 m; 4: 4, 3.51, 0, 0, 0.09, 161 m; 5: 12, 10.54, 0, 0, 0.24, 301 m; 6: 8, 6.54, 0, 0, 0.13, 171 m; 7: 1.5, 1.17, 0, 0, 0.03, 30 m; 8: 5, 4.34, 0, 0, 0.09, 192 m; 9: 2.0, 1.59, 0, 0, 0.05, 82 m; 10: 1.2, 0.94, 0, 0, 0.03, 43 m; bars every about 1.25 s, so KE maxima are lower bounds | PE rebound of blocks 1 and 3 (l. 397 to 399) confirmed; findings GB-27, GB-42 |
| PP-32 | P21 | Comparisons of absolute quantities on bases of different size | Fig9 block energies (0.95 to 11.07 GJ) belong to blocks of 756.2 to 1754.3 m³ but are compared only qualitatively (l. 397 to 402); Fig8 and Fig12 single series of one mass; Fig10 (b) absolute counts per 100 m | no further comparison whose direction could reverse; normalisation in GB-25, GB-44 |
| PP-33 | P3, P29 | Fig10 (a) | legend colours of the ten trajectories pairwise distinguishable (smallest difference 73); all trajectories start at one common point, so they show displacement; Z tick spacing decreases from 168 to 154.5 px per 210 m, a perspective projection; "Blocks 1 and 3 exhibit bouncing rebounds" (l. 416) not checkable against the trajectories | no finding beyond GB-28, GB-45 |
| PP-34 | P4, P22, P3 | Numbering of sections, figures, tables and equations, and implicit counts | sections 1, 2, 2.1 to 2.4, 3, 3.1, 3.2, 3.2.1, 3.2.2, 3.4, 4 (3.3 missing); Fig1 to Fig12 each once, first cited in ascending order (l. 76 to 443); Tables 1 and 2 cited l. 212 and l. 259; Eq. (1) to (6) consecutive, none cited by number; every cited panel letter exists except b-b' and "(a-i)"; number of landslide blocks not stated (25345 includes the base, l. 181); time of the solid-to-fluid transition only inferable | KK-28, KK-29, GB-15, GB-13, GB-48 |
| PP-35 | P3, P24 | Annotations of Fig11 and Fig12 | Fig11 ten panels for ten times in the stated order; Fig12 (a) KE marker centre at VS of about 31 % (marker half width about 1.3 %), compatible with the label "29.47"; annotation line at 1116.7 GJ for the label "1116.8"; PE at VS 0 and final DE about 6500 GJ, consistent with Fig8 | no finding beyond GB-46, GB-48 |
| PP-36 | P20 | Every percentage and every "x of y" in Sect. 3 and the quantities feeding them | VS 29.47 % and AG 319.5 % (l. 453 to 454), base missing; prominence thresholds 10 to 50 % (l. 230 to 232), reference missing; 1,139 collisions (l. 233), population missing; no other rate or share in Sect. 3 | GB-25, GB-33; disclosed: the 30 % threshold is a visual judgement ("deemed acceptable", l. 232 to 233) |

### Segment 4: Conclusions, declarations, references (p. 25 to 29, l. 460 to 605)

#### Substantive findings

**GB-49 Conclusion 1 states restoration rules that the methods do not describe, and the contour restoration presented as a new idea is not tested against any known surface.**

| Field | Content |
|---|---|
| Check | P15, P10 |
| Location | p. 25, l. 463 to 468; p. 2, l. 49 to 51; p. 6 to 7, l. 136 to 143 and l. 157 to 162; p. 9, Fig3 (c) |
| Quotation | "their trajectory equations can be extracted as a basis for restoring the contours" and "In such cases, restoration can be guided by referencing other mountain areas within the same stratigraphic unit." |
| Concern | The methods describe the restoration plainly: contour lines of sliding bed and accumulation area "are modified to be straight" (l. 140) and modified "along the extension direction of the mountains on the left and right sides" (l. 157). No trajectory equation, fitting function or parameter appears anywhere, and no reference to other mountain areas of the same stratigraphic unit is described for this case. The only assessment is qualitative (the restored terrain is smooth and the mountains become continuous, l. 160 to 162), which the manuscript states openly; a comparison with a known surface is missing. Conclusion 1 therefore states rules that the study did not apply or test, and since the Introduction presents the restoration as a new idea (l. 49 to 51, GB-03), it carries a claimed contribution. The restored surface also defines the mass geometry and volume that feed every energy value (GB-13), so its uncertainty propagates unquantified into all results. |
| Suggestion | Either describe in Sect. 2.1 how contour trajectories were fitted (function, parameters, extent) and how the deposit area was treated, and test the restored surface (counter-design: apply the same procedure blind to a landslide with a pre-event DEM, for example a 2008 Wenchuan landslide, and report elevation error and volume error; for Mogangling compare the depletion volume between restored and present DEM with the deposit volume and with l. 151), or reduce Conclusion 1 to what was done: straightening of contour lines inside the scar along the trend of the adjacent slopes. |
| Status | verified (absence in Sect. 2.1 and 3, Fig3 (c)) |
| Severity | major |
| Source | S4, SD |

**GB-50 The data and code statements withhold all author-generated, non-personal data behind "upon reasonable request" without giving a reason.**

| Field | Content |
|---|---|
| Check | P12 |
| Location | p. 26, l. 505 to 506 and l. 494 to 495; data sources in the methods: p. 6, l. 130 to 135; p. 6 to 7, l. 138 to 143 and l. 157 to 159; p. 9, l. 171 to 182; p. 11, l. 226 to 234; p. 13, l. 256 to 263 and Table 2; p. 14, l. 272 to 284 |
| Quotation | "The data and materials that support the findings of this study are available from the first author, Yunfeng Ge, upon reasonable request." |
| Concern | The manuscript does say where data and code can be obtained and separates the two. The methods produce at least six author-generated data sets: (1) UAV DEM and filtered point cloud (l. 130 to 135); (2) modified contour lines and restored surface (l. 138 to 143, l. 157 to 159, Fig3 (c)); (3) 3DEC model geometry and input files (l. 171 to 182, Fig4); (4) histories of the whole mass and of the ten monitored blocks (l. 260 to 263, Table 2); (5) the peak-detection script and the detected collisions (l. 226 to 234, Fig5, Fig10 (b)); (6) the alpha-shape envelopes and VS and AG series (l. 272 to 284, Fig11, Fig12). None concerns persons, so privacy does not justify the withholding, and no other reason (size, licence, ongoing use) is named. Without items 2 to 6 a reader cannot recompute the energy curves (Fig8, Fig9, Fig12) or the collision counts that carry the conclusions. |
| Suggestion | In "Availability of data and material" (l. 505 to 506) list the data sets individually and deposit at least the restored surface, the model input files, the histories underlying Fig8 to Fig12 and the two scripts in a public repository with a persistent identifier; for anything that stays on request, state the reason per data set, and adjust the code statement (l. 494 to 495). |
| Status | wording of both statements, absence of links and of an appendix: verified; that none of the data concern persons: inferred from their description |
| Severity | moderate |
| Source | S2 |

**GB-51 Sixteen of the 31 reference entries are never cited, among them two studies of the Mogangling landslide itself and the first author's earlier study on mechanical energy evolution in rock avalanches.**

| Field | Content |
|---|---|
| Check | P4 |
| Location | p. 26 to 29: Bernardie et al. 2021 (l. 508 to 510), Chang et al. 2022 (l. 514 to 516), Chen et al. 2024 (l. 517 to 520), Dahal et al. 2022 (l. 524 to 526), Gao et al. 2023 (l. 537 to 539), Ge et al. 2021 (l. 540 to 542), Gong et al. 2024 (l. 543 to 545), He, J. et al. 2023 (l. 546 to 548), He, K. et al. 2022 (l. 549 to 552), He, N. et al. 2023 (l. 553 to 555), Nava et al. 2025 (l. 562 to 565), Sinčić et al. 2025 (l. 566 to 568), Wu, J. et al. 2013 (l. 588 to 590), Yang et al. 2022 (l. 591 to 593), Zhang, K. et al. 2019 (l. 597 to 599), Zhou et al. 2024 (l. 603 to 605) |
| Quotation | "Ge, Y., Tang, H., and Li, C.: Mechanical energy evolution in the propagation of rock avalanches using field survey and numerical simulation" and "Wu, J., Wang, Y., Dong, S., Chen, Y., and Wang, L.: Genetic Mechanism and Failure Process of the Mogangling Seismic Landslide" |
| Concern | Of 31 entries, 15 are cited (both Fan et al. 2019 entries counted as cited, and three entries cited with a deviating year, KK-09, KK-12, KK-15) and 16 are not; quota 16/31 = 51.6 % (Python). Instance S1 counted 19 because it treated the three entries with deviating year as uncited. Several uncited entries bear directly on the study: Wu et al. (2013) on the failure process of the Mogangling landslide, Zhou et al. (2024) on earthquake-triggered landslides at Moxi Town, Ge et al. (2021) on mechanical energy evolution in rock avalanches, and He, J. et al. (2023) on the seismic response of a Dadu River slope (GB-10); Zhao et al. (2021), also on Mogangling, is cited only with a wrong year (KK-15). The reader cannot see how the present results relate to earlier reconstructions of the same event or to the earlier energy analysis by the same first author, which matters for the research gap (GB-07). |
| Suggestion | Cite and discuss Wu et al. (2013), Zhao et al. (2021), Zhou et al. (2024) and Ge et al. (2021) where the event, the seismic input and the energy method are introduced (Sect. 1, 2.1, 2.3), compare the results with them, and delete or cite the remaining uncited entries. |
| Status | verified (two-way check of text and list); quota: inferred (calculation) |
| Severity | moderate |
| Source | S4 |

**GB-52 The reference list is not uniformly formatted: five entries are set in grey and unjustified, one entry truncates the author list, and title capitalisation varies.**

| Field | Content |
|---|---|
| Check | P16 |
| Location | p. 26 to 29: grey entries Bernardie et al. (l. 508 to 510), Dahal et al. (l. 524 to 526), Nava et al. (l. 562 to 565), Sinčić et al. (l. 566 to 568), Zhang, K. et al. (l. 597 to 599); "et al." in l. 530; title case in l. 521 to 522, l. 537 to 538, l. 549 to 551, l. 553 to 555, l. 556 to 557, l. 569 to 570, l. 588 to 589, l. 603 to 604 |
| Quotation | "Fan, X., Scaringi, G., Korup, O., et al.: Earthquake-induced chains of geologic hazards" |
| Concern | Measured on the page images, the darkest pixel of the five listed entries is RGB (34, 34, 34), while all other entries reach (0, 0, 0), and these five are set ragged right while the others are justified; all five are uncited (GB-51). The Fan et al. (2019, Rev. Geophys.) entry is the only one that does not list all authors. Eight entries use title case, the other 23 sentence case. The two book chapters (Hu et al., 2017; Song et al., 2017) give neither editors nor publisher. |
| Suggestion | Set all entries in the same colour and alignment, list all authors of Fan et al. (2019, Rev. Geophys.), use one capitalisation style for titles, and complete the book chapter entries with editors and publisher. |
| Status | verified (page images p. 26 to 29, pixel colour measured by instance S4) |
| Severity | minor |
| Source | S4 |

#### Minor corrections

| ID | Location | Quotation | Replacement | Source |
|---|---|---|---|---|
| KK-31 | p. 25, l. 464 and l. 466 | "It should be noted that:(a) Outside" and "restoring the contours;(b) The landslide" | "It should be noted that: (a) outside" and "restoring the contours; (b) the landslide" | S4 |
| KK-32 | p. 26, l. 494 | "The codes that support the findings of this study are available" | "The code that supports the findings of this study is available" | S4 |
| KK-33 | p. 26, l. 499 | "XF: Data curation, Investigation. LZ: Data curation, Investigation." | "XF: Data curation, Investigation; LZ: Data curation, Investigation." | S4 |
| KK-34 | p. 26, l. 507 (heading) | "Reference" | "References" | S4 |
| KK-35 | p. 27 to 29, l. 535, l. 541, l. 551, l. 560, l. 583, l. 589, l. 601 | "approach: the Baige landslide, Jinsha River, China, Landslides, 17, 147-164," (set with stretched word spaces before a line-final DOI) | set the reference list ragged right, as the grey entries already are, so that lines before a DOI are not stretched | S4 |

#### Verification log

| ID | Check | Checked | Values | Result |
|---|---|---|---|---|
| PP-37 | P15 | Each statement of Sect. 4 against a location in Sect. 2 and 3, recommendations against central results, strength of verbs | C1 (l. 463 to 468) no location in Sect. 3; C2 first sentence (l. 469 to 471) Sect. 2.1, 2.3, "geological structures" against l. 176 to 178; C2 "ensures" against l. 353 to 359; C2 movement process (l. 472 to 473) Sect. 3.1, matches; C2 effective collisions (l. 473 to 475) Sect. 2.2, matches in substance; C3 whole mass (l. 476 to 479) definitional; C3 blocks (l. 479 to 482) matches as description of DE decreases, without the qualification of l. 399 to 400; C4 (l. 483 to 487) no location; C5 (l. 488 to 492) given as interpretation in l. 445 to 450; verbs "can be concluded" (l. 483, l. 489) and "ensures" (l. 471) stronger than the evidence; no outlook and no limitations section | findings GB-39, GB-42, GB-44, GB-47, GB-49; disclosed: structural planes ignored (l. 176 to 178), Wenchuan record at Luding (l. 183 to 191), dam break not modelled (l. 349 to 350), α fixed at 1 (l. 282 to 284); only the first is not drawn through to the conclusions |
| PP-38 | P12 | Presence and content of availability statements, appendices, supplements and links | statements "Code availability" (l. 494 to 495) and "Availability of data and material" (l. 505 to 506); appendices 0; supplements 0; links or DOIs to data or code 0; 6 author-generated and 6 external or archival data sources identified in the methods | reachability not applicable (no links); findings GB-19, GB-50; disclosed: lack of instrumental records (l. 183 to 186) and of structural-plane data (l. 175 to 178) |
| PP-39 | P16 | Grammar, wording and typesetting of l. 460 to 605 on the page images p. 25 to 29 | errors listed as KK-31 to KK-35 and GB-52; not counted as errors: the dash in l. 478 (correct English punctuation), hyphenated page ranges (uniform), diacritics in Grémont, Sinčić, Mihalić, Lourenço, Da'ao (correct in the image), the hyphen in "multi-risk" (l. 512, extraction artefact only), the repeated phrase "the following conclusions can be drawn" (l. 462, l. 476 to 477); declarations present: code, contributions, competing interests, funding, data; no statement on the use of AI tools | no further finding |

## Optional checks

| Area | What it needs | Responsible | Run |
|---|---|---|---|
| DOI resolution | one retrieval per reference entry | `science-quellenapparat-pruefung` | no |
| Citation style | the name of the style | `science-zitierstil-harvard-ctr` or the journal's style rules | no |
| AI statement against publisher policy | the target publisher's AI policy | this review, on request | no |
| Relation to the authors' prior work | the authors' prior work | this review, on request | no |
| Journal requirements | the target journal's author guidelines | this review, on request | no |
| Subject-matter correctness | access to the sources of each checked statement | `science-faktenbeleg-pruefung`, `geo-frage-belegbasiert-klaeren` | no |

## Limits of this review

- Checked version: egusphere-2025-4506.pdf, 29 pages, SHA-256 64cb3787456244aa6102e34f776b47e9a612d06e8894d391758ae240dbe415d6.
- Review instances: the six instances (S1 to S4, AB, SD) ran as separate agents without shared context; the merge (steps 4 to 7) was done by a separate agent that read only the manuscript, its derived files and the six instance reports.
- Discarded findings: 0. All 83 substantive findings of the instances carried every mandatory field, and none was refuted when the manuscript was re-checked. Three sub-statements were corrected during the merge: the eastern end of the section line in Fig2 (c) is labelled "a'", not "a" (GB-15); Fig10 (b) shows five, not four, decreases (GB-44); the abstract line numbers given by instance SD (l. 34 to 38) were replaced by the printed margin numbers l. 26 to 30.
- Merged findings: 83 instance findings were merged into 52 (31 absorbed as duplicates of the same location and subject); 54 instance minor corrections became 32, of which 8 were absorbed into substantive findings and 14 merged with each other, and 3 minor corrections were added from hints outside the checklists (Source ZF, confirmed on page images p. 5, 10 and 20); 45 verification logs were merged into 39.
- Hints outside the checklists were promoted only where no responsible instance had treated the location; all other hints were already covered by findings or concerned locations an instance had checked.
- Placement: each finding stands in the segment of its first-listed location; locations are listed with the place of the substantive claim first, so findings on the Results that also concern the Abstract stand in Segment 3.
- Line numbers follow the printed margin numbers (every fifth line printed); quotations and line numbers were re-checked against a layout extraction of the PDF and against the page images. Table bodies and figure contents carry no margin numbers and are cited by page and element.
- Values measured in figures were taken from the instances; the merge re-checked labels, legends and positions on the page images but did not re-measure. Where instances measured the same quantity, their range is given.
- Unreadable sources: Cheng and Yu-Sheng (2014) (not readable), Ge et al. (2021) (title only), Wu et al. (2024) (record only), Fan et al. (2019, Rev. Geophys.) (abstract only), Du et al. (2021) (abstract only), Hu et al. (2017) (full text not readable), He, J. et al. (2023) (title only); the Crossref record of Cheng and Yu-Sheng (2014) was refused by the network proxy.
- Findings with status assumption: 0 of 52 as central statement; 7 of 52 contain a sub-statement with status assumption (GB-09, GB-14, GB-18, GB-19, GB-25, GB-26, GB-47), each put as a question to the authors.
- Optional checks run: 0 of 6.
