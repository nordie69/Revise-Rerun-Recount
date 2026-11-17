# Review report: Energy and structural evolution process of high-altitude and long-runout landslides induced by a strong earthquake

| Field | Value |
|---|---|
| Manuscript | Ge, Y., Hu, B., Tang, H., Fu, X., and Zhu, L. (2025): Energy and structural evolution process of high-altitude and long-runout landslides induced by a strong earthquake, EGUsphere preprint egusphere-2025-4506, https://doi.org/10.5194/egusphere-2025-4506 |
| Checked version | egusphere-2025-4506.pdf, 29 pages, SHA-256 64cb3787456244aa6102e34f776b47e9a612d06e8894d391758ae240dbe415d6 |
| Date | 2026-10-18 |
| Language | English |
| Review instances | Segments 1 to 4, figures, study design; the six review instances ran as separate agents; no instance dropped |
| Note | Line numbers are the printed margin numbers (in steps of 5), counted at the page images from the nearest printed number; pages 4 and 8 carry no margin numbers, so locations there name page and element. Display equations count as lines (p. 12, l. 245 is Eq. 1; p. 13, l. 246 to 249 are the lead-in and Eq. 2 to 4). |

## Summary

The manuscript is a single case study with numerical modelling of the 1786 Mogangling rock landslide on the Dadu River (Luding County, Sichuan), triggered by the Kangding (Moxi) earthquake. The pre-failure terrain is restored by straightening the contour lines of a UAV-derived DEM, and the failure is reconstructed with one three-dimensional discrete element run (3DEC, 25,345 blocks, blocks of 8.7 m x 8.7 m in plan, Mohr-Coulomb) loaded by the acceleration record of the Luding station from the 2008 Wenchuan earthquake. Kinetic, potential and dissipated energy are computed for the whole sliding mass and for ten monitored blocks, with dissipated energy defined as the loss of mechanical energy since the start; "effective collisions" are identified as local velocity peaks above a 30 % prominence threshold (1,139 detected); and alpha-shape envelopes (α = 1) fitted at ten time points give volume swelling (VS) and area growth (AG). Key numbers: simulated duration 131 s, maximum velocity 31.6 m/s, a stated landslide volume of about 2400 x 10^4 m³ against a model volume of 317,563 m³, and a transition from solid to fluidised behaviour placed at VS of about 29.47 % and AG of about 319.5 %. The authors conclude that the whole mass conserves energy while single blocks do not, that lower or front blocks collide more often and travel farther, and that envelope growth reflects fragmentation.

## Strengths

1. The model geometry can be traced from the present terrain to the model: section a-a' in Fig2 (c) matches the length and direction of the profile in Fig3 (b) and the stated sliding direction, and the dimension labels of Fig4 agree with the text (PP-15, PP-14); this lets a reader follow how the restored surface becomes the sliding mass, although the restored surface itself is not checked (GB-13).
2. Every energy term is defined explicitly in Eq. (1) to (4), and the velocity maxima reported for the seven stages agree with the colour bars of Fig7 (PP-35); because the bookkeeping is open, a reader can check it algebraically, which is how the constant total was recognised as a consequence of the definition (GB-41).
3. The ten monitored blocks are spread over four elevation groups with consistent IDs, positions and coordinates (2 + 3 + 3 + 2 blocks, z rising by group), and energy histories are shown for all ten (PP-24, PP-19, PP-42); this makes single-block behaviour visible, for example the potential-energy rebound of blocks 1 and 3 (PP-37).
4. The main modelling limits are disclosed where the affected method is introduced, among them the missing record of 1786 and its substitution, the ignored structural-plane data, the influence of the detection threshold and of α, the PE datum and the unmodelled dam break (PP-21, PP-07); and the threshold choice is shown over five values in Fig5 (b) to (f), so its effect on the detected peaks can be measured (GB-29).

## Weaknesses

1. The energy results rest on quantities that do not test what they claim: the sum KE + PE + DE is constant by the definition of DE, for the whole mass and for every block, so it shows neither conservation nor its absence; DE also absorbs the work of the seismic input; PE is plotted against a datum other than the one stated; and the magnitudes in Fig8 fit neither of the stated volumes, which differ by a factor of 75.6 (GB-41, GB-31, GB-16). Suggestion: compute dissipation, seismic work and base work independently, state datum and mass, and reconcile the landslide and model volumes before drawing energy conclusions.
2. The position-dependent claims of the abstract and Conclusion 4 (lower or front blocks collide more often, receive more energy and travel farther) have no counted basis: no collision count per block or position is reported, Fig10 (b) bins collisions by travel distance and grows with exposure, the detector counts velocity peaks with a threshold chosen by eye, and the basis of the 1,139 collisions is not stated (GB-42, GB-26, GB-29). Suggestion: validate the detector against contact data and report per-block counts normalised by travel distance, time and mass, grouped by the positions of Table 2.
3. The structural interpretation is not supported: envelope growth is read as fragmentation, although fragments filling the interior cannot enlarge an envelope and no breakage is shown; the phase-transition threshold is taken at the kinetic-energy peak it is meant to explain; Fig12 has about three times more points than the ten fitted time points and a KE peak 33 % below that of Fig8; and the alpha-shape procedure and its reference values are not reported (GB-45, GB-46, GB-35). Suggestion: measure fragmentation and spreading separately, report t, V, S, VS and AG per time point, and define the transition independently of KE.
4. The design and its reporting limit what the case can show: one run with one substitute record and no comparison condition, an unchecked restored terrain, structural planes declared ignored yet used to explain failure, a qualitative validation presented as ensuring agreement, unstated model settings and parameter sources, data and code only on request, and novelty and gap claims that are not set against existing reconstructions and energy studies, including the first author's own (GB-21, GB-13, GB-20, GB-38, GB-12, GB-24, GB-49, GB-02, GB-06). Suggestion: add comparison runs and a quantitative validation against the DEM deposit, state settings and parameter sources, deposit data and code, and add a Discussion against the literature.

## Findings by segment

### Segment 1: Abstract, introduction, state of research (p. 1 to 2)

#### Substantive findings

**GB-01 The regional multi-risk mapping study by Carpignano et al. (2009) is cited as evidence that earthquake-induced chain disasters of high rock landslides have become more frequent.**

| Field | Content |
|---|---|
| Check | P13 |
| Location | p. 1, l. 33 to 34 |
| Quotation | "In recent years, the chain disasters of high-level rock landslides in high-intensity earthquake areas have shown a trend of frequent occurrence (Carpignano et al., 2009; Fan et al., 2019a)" |
| Concern | The introduction opens with a trend claim and gives two sources for it. The second, Fan et al. (2019), is listed with the title "Earthquake-induced chains of geologic hazards: patterns, mechanisms, and impacts" (p. 27, l. 530 to 532) and matches the topic. The first does not: Carpignano et al. (2009, J. Risk Res., 12, 513 to 534) propose a method for multi-risk maps and a decision support system for the Piedmont Region, Italy. Their abstract deals with regional risk management for technological and natural hazards and does not mention earthquake-triggered rock landslides, landslide chains, high-intensity seismic areas or any trend in frequency. The cited work therefore does not support the frequency claim attributed to it. |
| Suggestion | In p. 1, l. 33 to 34, remove Carpignano et al. (2009) as support for the trend, or cite it only for multi-risk assessment; support the trend with a work that documents an increase in frequency, and state the period and region the trend refers to. |
| Status | verified (abstract and subject metadata of Carpignano et al. 2009 read in the OpenAlex record, https://api.openalex.org/works/doi:10.1080/13669870903050269; full text closed); inferred for the suitability of Fan et al. (2019), from the title in the reference list only |
| Severity | moderate |
| Source | S1 |

**GB-02 The claims that pre-landslide terrain restoration is rare and that contour-continuity restoration offers "a new idea" rest on no documented search, and a published case has already reconstructed a pre-failure surface from contour lines before runout modelling.**

| Field | Content |
|---|---|
| Check | P28, P14 |
| Location | p. 2, l. 42; p. 2, l. 49 to 51; p. 1, l. 16 to 17 |
| Quotation | "At present, in terms of surface terrain restoration, the terrain restoration before a landslide is less."; "This paper uses the method of restoring the continuity of contour lines to establish the terrain data before a landslide, which can provide a new idea of terrain restoration before a landslide for the same type of research." |
| Concern | Both sentences make a claim about how much prior work exists, and the second presents the contour method as new; the abstract repeats the method as a contribution (p. 1, l. 16 to 17). The manuscript names no database, search terms, period or date of a search: a whole-word, case-insensitive search of text.json, pages 1 to 29, for "database", "Web of Science", "Scopus", "Google Scholar", "CNKI" and "search" gives 0 hits; the string "search" occurs 8 times, each time inside "research". The sentences between the two claims (p. 2, l. 43 to 49) cite works on GIS mapping and on 2-D simulation, not on the reconstruction of pre-failure topography (GB-03, GB-04). A published counterexample exists: De Pedrini, A., Ambrosi, C., and Scapozza, C.: The 1513 Monte Crenone rock avalanche: numerical model and geomorphological analysis, Geogr. Helv., 77, 21 to 37, https://doi.org/10.5194/gh-77-21-2022, 2022 (open access). Lacking maps from before the event, they built a pre-failure contour surface by hand from borehole data, surviving landforms and repeated numerical runs (Sect. 4.2), ran a runout model on it (RAMMS::DEBRISFLOW, Sect. 4.3), and, like Conclusion 1 (b) of the manuscript, note that the deposit area is poorly constrained (Sect. 4.3.1). The work is not among the 31 entries of the reference list (p. 26, l. 508 to p. 29, l. 605). It anticipates the method claimed as new and shows how the uncertainty of a reconstructed surface can be handled. |
| Suggestion | In p. 2, l. 42 to 51, either report the literature search (databases, search terms, period, date) behind "is less" and "new idea", or rephrase both as a description of the approach chosen for Mogangling; cite De Pedrini et al. (2022) and state what the contour-continuity method adds, for example its use in 3-D and the extension of contours from the flanking ridges. |
| Status | verified (absence of a search description, by text search of the manuscript); verified for De Pedrini et al. 2022 (full text read by instance S1, https://gh.copernicus.org/articles/77/21/2022/gh-77-21-2022.pdf, published version); inferred (that the method is not new as worded, from this counterexample) |
| Severity | moderate |
| Source | S1 |

**GB-03 Two of the four works cited for GIS mapping from photos, field surveys, remote sensing and UAV data deal with numerical simulation, and the other two have no reference entry.**

| Field | Content |
|---|---|
| Check | P13 |
| Location | p. 2, l. 43 to 46 |
| Quotation | "the key information of landslide characteristics is often obtained through photos, field surveys, optical remote sensing images and UAV impact, so as to further build geomorphic maps through GIS (Geographic Information System) for subsequent analysis (Zhang et al., 2024; Song at al.2017; Fan et al., 2020; Wu et al., 2024)" |
| Concern | Four works are cited for collecting data in the field and from images and then mapping in GIS. Song et al. (2017) build a 3-D numerical model of a reactivated landslide in the Three Gorges Reservoir and check it against GPS monitoring through one filling and drawdown cycle; the abstract does not mention photos, UAV data, optical remote sensing or GIS mapping. The title of Wu et al. (2024) ends in "induced wave hazards by a novel hybrid method" (p. 28, l. 585 to 587), which points to wave simulation, not mapping. Fan et al. (2020) has no entry in the reference list, and Zhang et al. (2024) has at most a candidate entry with another year (Zhang, J. et al., p. 29, l. 594 to 596, an InSAR and model study of the Da'ao landslide; see GB-50), so these two cannot be checked. Unlike GB-02, which concerns the novelty claim in l. 42 and l. 49 to 51, this finding concerns whether the works cited in l. 45 to 46 support the sentence they stand in. |
| Suggestion | In p. 2, l. 45 to 46, replace Song et al. (2017) and Wu et al. (2024) by works that build geomorphic maps from photos, field surveys, remote sensing or UAV data, and add reference entries for Zhang et al. (2024) and Fan et al. (2020). |
| Status | verified for Song et al. 2017 (abstract on the publisher's chapter page, https://link.springer.com/chapter/10.1007/978-3-319-53483-1_36, read by S1); inferred for Wu et al. 2024 (title and metadata only, DOI 10.1016/j.enggeo.2024.107429); verified that Fan et al. 2020 has no entry and Zhang et al. 2024 no entry with that year (reference list, page images p. 26 to 29) |
| Severity | moderate |
| Source | S1 |

**GB-04 The claim that "most" numerical simulations with terrain restoration are two-dimensional is supported by only one of the three works cited for it.**

| Field | Content |
|---|---|
| Check | P13 |
| Location | p. 2, l. 46 to 49 |
| Quotation | "For most numerical simulations involving terrain restoration, a two-dimensional simulation is more often used. The simplified model is adopted to simulate the overall process of landslide by inputting external stress (Du et al., 2021; Cheng 2014; Li et al., 2024)." |
| Concern | The sentence ranks practice in the field ("most", "more often"), and the ranking motivates the 3-D model used here. (1) Cheng and Li (2014) use UDEC on an ancient landslide in Huanglang Valley with critical seismic accelerations, which fits a 2-D discrete element model loaded by an external force. (2) Li et al. (2024) analyse the 2020 Zhongbao landslide with GeoStudio SEEP/W and SLOPE/W, driven by 20 days of rainfall seepage; the paper describes no restoration of the pre-failure terrain, and the only loading is rainfall, not an input of external stress; that the model is 2-D is only implied by its mesh. (3) Du et al. (2021) simulate the Jiaobunong landslide with a discrete element model triggered by a paleo-earthquake, but their abstract states neither the dimensionality nor how the topography was reconstructed. Song et al. (2017), cited in the sentence just before (GB-03), use a 3-D model. No count or review stands behind "most". GB-03 concerns the works cited in l. 45 to 46; this finding concerns the three works of l. 48 to 49. |
| Suggestion | In p. 2, l. 46 to 49, support the ranking with a review or a stated count of studies, or reword it as an observation about the cited cases; cite Li et al. (2024) only for what it does (seepage and limit equilibrium analysis) or remove it. |
| Status | verified for Cheng and Li 2014 (abstract, OpenAlex record https://api.openalex.org/works/doi:10.1109/isdea.2014.149); verified for Li et al. 2024 (full text, https://www.frontiersin.org/journals/earth-science/articles/10.3389/feart.2024.1466751/full), the 2-D geometry inferred from the mesh description; verified for Du et al. 2021 at abstract level (https://jms.imde.ac.cn/article/doi/10.1007/s11629-020-6617-y), modelling details unread; all read by instance S1 |
| Severity | moderate |
| Source | S1 |

**GB-05 Two of the five works cited for the rising visibility of "landslide seismology" appear to be studies of snow avalanches: is that intended?**

| Field | Content |
|---|---|
| Check | P13 |
| Location | p. 2, l. 61 to 63 |
| Quotation | "In recent years, landslide seismology has taken on more visibility (Navarre et al., 2009; Van Herwijnen and Schweizer, 2011; Helmstetter and Garambois, 2010; Cook et al., 2021; Pandey et al., 2021)." |
| Concern | None of the five works has an entry in the reference list (GB-50), so they can only be identified by author and year. The only work matching "Van Herwijnen and Schweizer, 2011" found by instance S1 is van Herwijnen, A. and Schweizer, J.: Monitoring avalanche activity using a seismic sensor, Cold Reg. Sci. Technol., 69, 165 to 176, https://doi.org/10.1016/j.coldregions.2011.06.008, 2011, which counts snow avalanches near Davos with a buried geophone. That paper cites Navarre et al. (2009), "The seismic detection of avalanches: an information tool for the avalanche forecaster", also on snow avalanches. If these are the works meant, two of the five citations come from snow-avalanche seismology and do not show that the seismology of rock landslides has become more visible. |
| Suggestion | In p. 2, l. 62 to 63, add full reference entries for all five works; if the snow-avalanche papers are meant, write "mass-movement seismology" or replace them by seismological studies of rock landslides or rockfalls. |
| Status | inferred (which works are meant, because none appears in the list); verified for the content of van Herwijnen and Schweizer 2011 (full text, https://www.slf.ch/fileadmin/user_upload/WSL/Mitarbeitende/schweizj/vanHerwijnen_Schweizer_Avalanche_activity_seismic_monitoring_CRST_2011.pdf, read by S1); Navarre et al. 2009 only through its entry in that paper |
| Severity | minor |
| Source | S1 |

**GB-06 The research gap "a quantitative and systematic study ... especially on energy evolution during the collision" is stated without a search, although the reference list contains such a study by the first author and further discrete element studies have quantified collisional energy dissipation and transfer.**

| Field | Content |
|---|---|
| Check | P28, P14 |
| Location | p. 2, l. 63 to 64; p. 2, l. 65 to 69; p. 27, l. 540 to 542; p. 26, l. 483 to 487 |
| Quotation | "However, they still lack a quantitative and systematic study of this topic, especially on energy evolution during the collision."; "When the rear rock mass collides with the front, its dissipated energy sharply increases and transfers energy to the front rock mass, enabling the front portion to slide farther." |
| Concern | This sentence sets out the gap that the aims in l. 65 to 69 address. No search is reported for it (0 hits for database names and "search", see GB-02). Three things contradict it. (1) The reference list contains Ge, Y., Tang, H., and Li, C.: Mechanical energy evolution in the propagation of rock avalanches using field survey and numerical simulation, Landslides, 18, 3559 to 3576, 2021 (p. 27, l. 540 to 542), a study by the first and third authors; the main text never cites it (search of text.json, p. 1 to p. 26, l. 506, for "Ge et al" and "Ge" followed by a year: 0 hits; the six in-text citations with the year 2021 are Wang, Du et al., Cuomo et al., Shugar et al., Cook et al. and Pandey et al.). (2) Hibert et al. (2017) compared, for each impact of single rockfall blocks, the potential energy lost and the kinetic energy with the radiated seismic energy, a quantitative energy study of collisions within the very field the sentence refers to. (3) Lin, Q., Wang, Y., Xie, Y., Cheng, Q., and Deng, K. (2022, Nat. Hazards Earth Syst. Sci., 22, 639 to 657, https://doi.org/10.5194/nhess-22-639-2022, open access) found in PFC2D models that fragmentation speeds up the front sub-block and slows the rear one and transfers energy more efficiently than collision, which bears on Conclusion 4 (p. 26, l. 483 to 487); Daudon, D., Villard, P., Richefeu, V., and Mollon, G. (2015, C. R. Mecanique, 343, 166 to 177, https://doi.org/10.1016/j.crme.2014.11.003, open access) computed the dissipated energy of a rock avalanche separately for collisions and friction and for block-block and block-base contacts. Neither work is in the reference list. What the manuscript adds beyond Ge et al. (2021) is not stated. GB-05 concerns which works are cited in l. 61 to 63; this finding concerns the gap claim that follows them. |
| Suggestion | In p. 2, l. 60 to 64, report the search behind the gap or reword it; cite Ge et al. (2021), Hibert, C., Malet, J.-P., Bourrier, F., Provost, F., Berger, F., Bornemann, P., Tardif, P., and Mermin, E.: Single-block rockfall dynamics inferred from seismic signal analysis, Earth Surf. Dynam., 5, 283 to 292, https://doi.org/10.5194/esurf-5-283-2017, 2017, Lin et al. (2022) and Daudon et al. (2015), and state what is new here, for example the earthquake input, the 3-D block model, the effective-collision criterion or the alpha-shape indices; compare Conclusion 4 with the mechanism found by Lin et al. (2022). |
| Status | verified (no search reported; Ge et al. 2021 in the list and not cited in the text, by text search and on the page image p. 27); verified for Hibert et al. 2017 (abstract, https://esurf.copernicus.org/articles/5/283/2017/), Lin et al. 2022 (publisher page, https://nhess.copernicus.org/articles/22/639/2022/, published version) and Daudon et al. 2015 (full text, https://comptes-rendus.academie-sciences.fr/mecanique/item/10.1016/j.crme.2014.11.003.pdf), all read by S1; inferred for the content of Ge et al. 2021 (title and metadata only) |
| Severity | moderate |
| Source | S1 |

#### Minor corrections

| ID | Location | Quotation | Replacement | Source |
|---|---|---|---|---|
| KK-01 | p. 1, l. 21; p. 3, l. 84 | "potential energy, kinetic energy, and dissipation energy"; "kinetic energy and dissipation energy of the landslide" | "dissipated energy" in both places, as defined at p. 12, l. 241 and used at the other 8 hits (l. 242, 287, 387, 399, 442, 478, 481, 486) | S2 |
| KK-02 | p. 1, l. 23; p. 3, l. 88 to 89; p. 14, l. 272; p. 14, l. 281; p. 23, l. 426 | "the Alpha shape algorithm"; "generated by alpha shape"; "An alpha-shape algorithm"; "the Alpha Shape algorithm"; "Alpha Shape envelope fitting" | one spelling throughout, for example "alpha-shape algorithm" (l. 23, l. 281), "generated by an alpha-shape algorithm" (l. 88 to 89), "alpha-shape envelope fitting" (l. 426) and "Alpha-shape (α = 1)" in Fig1 (p. 4); compared at the page images p. 1, 3, 4, 14, 23. GB-35 concerns the reproducibility of the procedure, not its spelling; GB-28 concerns another word of the abstract sentence in l. 22 to 23 | S2 |
| KK-03 | p. 1, l. 24; p. 23, l. 426 | "extract the volume and surface area of the landslide body from 3D point cloud data"; "This study utilized numerical simulation data of the landslide" | "extract the volume and surface area of the simulated landslide body from the block geometry of the numerical model", so that the abstract names the same data source as Section 3.4; the point set itself is part of GB-35 | ZF |
| KK-04 | p. 1, l. 27 to 29; p. 7, l. 153; p. 7, l. 154; p. 7, l. 156 | "conservation of energy; For some blocks"; "; Compared with the upper rock mass"; "about 50°; The elevation"; "about 5-12°; The elevation"; "about 57°; The elevation" | lower case after the semicolon: "; for some blocks", "; compared with the upper rock mass", "; the elevation" (three times); checked at the page images p. 1 and 7. GB-41, GB-42, GB-34 and GB-17 concern the content of these sentences | ZF |
| KK-05 | p. 1, l. 34 | "such as donghekou" | "such as the Donghekou"; GB-01 concerns the sources cited in the same sentence, this correction only the capitalisation | S1 |
| KK-06 | p. 1, l. 34 to 37; p. 2, l. 56 to 57; p. 27, l. 530 to 536; p. 28, l. 577 | "(Carpignano et al., 2009; Fan et al., 2019a)"; "Wang, 2021"; "(Hu et al., 2017; Tian et al., 2017)"; "Fan et al., 2019" | "Fan et al., 2019a" or "2019b" with matching suffixes added to both Fan 2019 entries (p. 27, l. 530 and l. 533) and to "Fan et al., 2019" (p. 2, l. 56 to 57); "Wang et al., 2021" (the entry, p. 28, l. 581 to 584, has seven authors); one year for Tian in text and list, preferably "2017" in the entry (p. 28, l. 577), since volume 32(9) was printed in 2017 (Crossref, read by S1); compared on the page images p. 1, 2, 27, 28. GB-01 concerns the content of the first citation and GB-50 the missing and uncited entries; KK-05 another word of the same sentence | S4, S1 |
| KK-07 | p. 2, l. 42 to 43 | "For landslides that have not occurred too far away" | "For recent landslides"; GB-03 concerns the sources of the same sentence, GB-02 the preceding sentence in l. 42 | S1 |
| KK-08 | p. 2, l. 44; p. 6, l. 130 to 131 | "optical remote sensing images and UAV impact"; "According to the DEM data obtained by UAV scanning" | "optical remote sensing images and UAV imagery" at l. 44, and "According to the digital elevation model (DEM) data obtained by unmanned aerial vehicle (UAV) scanning" at l. 130 to 131 (DEM is expanded only in Fig1, UAV nowhere; search in text.json "DEM/digital elevation" 2 hits, "UAV/unmanned" 2 hits). GB-03 concerns the sources of the l. 44 sentence and GB-12 the missing survey details; KK-07 another phrase of the same sentence | S1, S2 |
| KK-09 | p. 2, l. 45 to 46 | "(Zhang et al., 2024; Song at al.2017; Fan et al., 2020; Wu et al., 2024)" | "(Zhang et al., 2023; Song et al., 2017; Fan et al., 2020; Wu et al., 2024)", provided Zhang, J. et al. (p. 29, l. 594 to 596) is meant; Fan et al., 2020 needs an entry (GB-50). GB-03 concerns whether these works support the sentence and GB-04 the next sentence, which begins in l. 46; this correction only the citation form | S4, S1 |
| KK-10 | p. 2, l. 48 to 49; p. 27, l. 521 | "Cheng 2014"; "Cheng, F., and Yu-Sheng, L.:" | "Cheng and Li, 2014" and "Cheng, F. and Li, Y.:" (authors Fang Cheng and Yusheng Li in the OpenAlex record of DOI 10.1109/isdea.2014.149, read by S1); GB-04 concerns the content of the same citation; GB-02, GB-13 and GB-48 concern the next sentence, which begins in l. 49 | S1, S4 |
| KK-11 | p. 2, l. 57 | "Zhao et al., 2020" | "Zhao et al., 2021" (entry p. 29, l. 600 to 602: Nat. Hazards, 106, 2021), provided this work is meant; see GB-50; KK-06 concerns the Fan citation of the same sentence | S1, S4 |
| KK-12 | p. 2, l. 73 | "high-altitude" | set "altitude" in black like the rest of the line (on the page image the word is grey: darkest pixel sum 105 against 0 in the neighbouring words, measured at 150 dpi); GB-47 concerns the aim stated in this sentence | ZF |

#### Verification log

| ID | Check | Checked | Values | Result |
|---|---|---|---|---|
| PP-01 | P13 | Examples of earthquake-induced landslide chains, p. 1, l. 34 to 37 (Sun et al. 2011; Wang et al. 2014; Wang 2021; Hu et al. 2017; Tian et al. 2017) against their reference entries and, for Tian, Crossref (S1) | Sun 2011: "Donghekou rockslide-debris flow triggered by the 5.12 Wenchuan earthquake"; Wang 2014: "large landslide triggered by the 2008 Wenchuan (M8.0) earthquake in Donghekou area"; Wang 2021: "debris avalanche in Donghekou area"; Hu 2017: "Landslides Triggered by the Ms6.5 Ludian, China Earthquake"; Tian: Geocarto Int. 32(9), 978 to 989, online 2016, print 2017 | no finding; the examples match the titles; "Hongshiyan" appears in none of the titles, contents not read beyond titles; year of Tian in KK-06 |
| PP-02 | P13 | Year of the Mogangling landslide, p. 1, l. 38, against the two Mogangling papers in the list (S1) | Zhao et al. 2021 (abstract via IDEAS/RePEc): "1786 Moxi M 7.75 earthquake"; Wu et al. 2013 (abstract via OpenAlex): Kangding-Moxi earthquake, Ms 7.7, 1 June 1786 | no finding |
| PP-03 | P13, P4 | Traceability of the cited works: all in-text citations (p. 1, l. 34 to p. 2, l. 63; none from p. 3 to p. 26, l. 506) against the 31 entries (p. 26, l. 508 to p. 29, l. 605), text.json and page images p. 1, 2, 26 to 29 (S1, S4, recounted in the merger) | 29 cited works: 10 with entry and same year; 3 with candidate entry and other year (Tian, Zhang 2024, Zhao 2020); 2 ambiguous (Fan 2019a, Fan 2019); 14 without entry; 10 + 3 + 2 + 14 = 29 | the 14 works without entry could not be checked under P13; findings GB-50, GB-03, GB-05; sentences citing only such works and containing no number or ranking (p. 2, l. 52 to 60) not checked further |
| PP-04 | P13 | Statements with numbers, rankings or evaluations taken from other works in segment 1 (S1) | 7 places: p. 1, l. 33 to 34 (trend); l. 34 to 37 (examples); l. 38 (1786); p. 2, l. 43 to 46 (mapping); l. 46 to 49 ("most"); l. 57 to 59 ("well", sources without entry); l. 61 to 63 (seismology) | checked as recorded in GB-01, PP-01, PP-02, GB-03, GB-04, PP-03, GB-05 |
| PP-05 | P14 | Contribution in one sentence and six literature queries (S1): pre-failure terrain from contours, 3DEC reconstruction, energy of the whole mass and of 10 blocks, effective collisions, alpha-shape indices | Candidates against the 31 entries: De Pedrini 2022, Lin 2022, Daudon 2015 (not in list, proposed); Hibert 2017 (not in list, cited as evidence); Ge 2021, Zhao 2021, Wu 2013, Zhou 2024 (in list, not proposed); Zhou X. et al. 2021, Gao et al. 2020, Manzella and Labiouse 2013 (relevant, not proposed because of the limit of three); query on alpha-shape deposits without candidate | findings GB-02 and GB-06; results from the discussion page and later versions of this manuscript appeared in the result lists and were not opened |
| PP-06 | P28 | Statements that work is missing, rare or new, whole manuscript; search terms "first time", "for the first", "novel", "new idea", "new", "rarely", "lack", "is less", "few", "not been", "no study", "seldom", "unprecedented", "never" (S1) | 10 hits: p. 2, l. 42 and l. 50; p. 2, l. 61 (availability of data, supported by the next sentence); p. 2, l. 63; p. 5, l. 119 and l. 121; p. 10, l. 184 (lack of records, not a gap claim); p. 25, l. 467 (not a gap claim); p. 28, l. 562 and l. 586 (reference entries) | findings GB-02, GB-06 and, for p. 5, GB-11; no finding for p. 2, l. 61; no database or search is named anywhere |
| PP-07 | P9, P10 | Design sketch of the whole manuscript, p. 1 to 29 (SD) | single case study with one 3DEC run, one substitute input record (Luding, Wenchuan 2008), 10 monitored blocks, 25,345 model blocks, 10 alpha-shape time points; no research questions or hypotheses stated; no comparison condition; 9 data sources (UAV DEM, restored terrain, geological map, Tiezhuang Temple tablet, Luding record, Table 1 parameters, 3DEC output, field photographs, unspecified field investigations); 8 disclosed limits (p. 9, l. 175 to 178; p. 10, l. 183 to 191; p. 7, l. 160 to 162; p. 11, l. 229; p. 14, l. 281 to 282; p. 13, l. 252 to 255; p. 16, l. 348 to 350; p. 16, l. 354 to 355) | sketch complete; disclosed limits are not raised again except where their consequences are not drawn (GB-21, GB-20, GB-26, GB-45) |
| PP-08 | P10 | Gaps against aims (SD) | gap 1, terrain restoration rare and mostly 2-D (p. 2, l. 42 to 51), maps to restoration and 3-D model; gap 2, lack of quantitative study of energy evolution during collision (l. 63 to 64), maps to energy and collision analysis; structural change (l. 69) has an aim but no stated gap; "energy accumulation" (l. 68) has neither instrument nor result | no finding beyond GB-21; the unpursued "accumulation" is taken up in GB-47 |

### Segment 2: Material, methods (p. 2 to 15)

#### Substantive findings

**GB-07 The method is announced as "three parts" but four are listed, and the parts carry different names in the text, Fig1 and the section headings.**

| Field | Content |
|---|---|
| Check | P38 |
| Location | p. 2, l. 76 to p. 3, l. 77; p. 4, Fig1 (left column); p. 5, l. 92; p. 11, l. 214; p. 12, l. 240; p. 14, l. 269 |
| Quotation | "As shown in Fig1., the research method involves three parts: (1) surface terrain restoration" |
| Concern | L. 77 to 90 enumerate four parts, (1) to (4), and Fig1 shows four boxes, so "three parts" contradicts both. Part (1) is "surface terrain restoration" in the text but "Geo-mechanical Model Building" in Fig1 and "Geo-mechanical model building" in heading 2.1 (l. 92); part (3) is "Energy evolution analysis" in the text, "Analysis of Energy Evolution During Block Motion" in Fig1 and "Energy evolution" in heading 2.3 (l. 240); part (4) is "Extraction of volume and area of landslide accumulation area" in the text and Fig1 but "Structural extraction of landslide accumulation area" in heading 2.4 (l. 269). Section 2.2 "Effective collision identification" (l. 214) has no part of its own; it is contained in part (2), which is named identically in text and Fig1. |
| Suggestion | Replace "three parts" by "four parts" in p. 3, l. 77, and use one name per part in l. 77 to 88, in the left column of Fig1 (p. 4) and in the headings 2.1 to 2.4. |
| Status | verified (page images p. 2, 3, 4, 5, 11, 12, 14) |
| Severity | minor |
| Source | S2, S4, AB, SD |

**GB-08 Labels, axis numbers and legends in seven figures are set below 6 pt at print size.**

| Field | Content |
|---|---|
| Check | P29 |
| Location | p. 4, Fig1 (box "Input Seismic Force"); p. 12, Fig5 (a) to (f) and insets; p. 17, Fig7 (a) to (n); p. 21, Fig9 (a) to (j); p. 23, Fig10 (a) and (b); p. 23, Fig11 (a) to (j); p. 25, Fig12 (a) and (b); caption of Fig11, p. 24, l. 437 to 438 |
| Quotation | "Fig11. Comparison of the overall envelope fitting of the landslide at 10 different times and the shape of the landslide mass in numerical simulation" |
| Concern | Character heights (capitals and digits) were measured by instance AB on 600 dpi renders and converted with pt = H x 72 / 600 / 0.72 (uncertainty about 0.6 pt): Fig11 axis numbers and titles 12 to 15 px = 2.17 to 2.50 pt; Fig5 inset axis numbers 3.17 to 3.25 pt, main axis numbers 4.83 to 5.33 pt; Fig10 (a) Z axis numbers 4.00 to 4.33 pt (X and Y smaller, not measured), Fig10 (b) 5.00 pt; Fig7 velocity panels 4.67 pt, colour-bar labels 5.00 to 5.17 pt, stress panels 5.17 pt; Fig9 axis numbers 5.17 pt, legend 5.33 pt; Fig12 axis numbers 4.83 pt; Fig1 "Input Seismic Force" 5.00 pt. All lie more than the uncertainty below 6 pt; Fig11 cannot be read at print size, so its changing axis ranges are not usable. Values at or above 6 pt are in PP-17. GB-07 concerns the names of the parts in Fig1; this finding only type size. Other form issues of these figures are in GB-30, GB-40, GB-43 and GB-44. |
| Suggestion | Re-export Fig1, Fig5, Fig7, Fig9, Fig10, Fig11 and Fig12 with axis numbers, titles and legends of at least 7 pt at final print width; for Fig11, enlarge the panels or use one common axis range with larger labels. |
| Status | verified (measured on the page images) |
| Severity | minor |
| Source | AB |

**GB-09 The location markers in Fig2 (a) and (b) do not mark the landslide centre given in the text.**

| Field | Content |
|---|---|
| Check | P3 |
| Location | p. 5, l. 95 to 96; p. 6, Fig2 (a) and (b) |
| Quotation | "The coordinates of the landslide center are: 29 ° 37 ′ 30.726 ″ north latitude, 102 ° 09 ′ 41.190 ″ east longitude." |
| Concern | Fig2 (a): with the graticule ticks measured at 300 dpi (100 and 102 degrees E at 728.5 and 884.5 px; 31 and 29 degrees N at 867.5 and 1023.0 px), the dot "Mogangling landslide" (centre 821.5, 980.5 px) lies at 101.170 degrees E and 29.547 degrees N (0.0129 degrees per px, plus or minus 1 px), while the text gives 102.161 degrees E and 29.625 degrees N: 0.991 degrees (about 96 km) further west. Fig2 (b): the red star sits on the crossing of the dotted lines labelled 102°09'E and 29°37'N, that is at 29°37'00"N, 102°09'00"E. With the scale bar of (b) (5.505 m per px), the stated centre lies 949 m north and 1106 m east of that crossing, 1457 m in total (Python: 30.726 x pi/180/3600 x 6371000 and 41.190 x pi/180/3600 x 6371000 x cos 29.625 degrees), on the western outline of the Dadu River drawn in (b). Either the coordinates or the markers are wrong. |
| Suggestion | Check the coordinates in p. 5, l. 95 to 96 against the DEM; place the dot in Fig2 (a) and the star in Fig2 (b) at the stated centre, or correct the text; label the graticule of (b) with seconds if the star is meant to sit off the lines. |
| Status | verified (positions measured on the page image by AB); inferred (which of the two is wrong) |
| Severity | moderate |
| Source | AB |

**GB-10 The lithological units are named, symbolised and coloured differently in the text, Fig2 (c), Fig3 (a), Fig3 (b) and Fig4, two units of the text are not mapped, and two legend colours in Fig3 (a) cannot be told apart.**

| Field | Content |
|---|---|
| Check | P38, P3, P29 |
| Location | p. 5, l. 101 to 105; p. 6, Fig2 (c) legend; p. 8, Fig3 (a) legend; p. 8, Fig3 (b) legend; p. 10, Fig4 legend; p. 11, l. 208 |
| Quotation | "Jinning plagioclase granite (γO2). Quartz diorite (O2) and a small amount of basic magmatic rocks"; "The sand slate of the Triassic Baiguowan formation (T3bg) is exposed on the left bank of the Dadu River."; "landslide accumulation (Q4del), colluvial Deluvial deposit (Q4col+dl) and alluvial deposit (Q4al)" |
| Concern | (1) Names: where a symbol is given the unit is clear and only the name differs: γo2 is "plagioclase granite" in the text (l. 101 to 102, l. 208) but "Plagiogranite" in Fig2 (c); Q4del is "landslide accumulation" (l. 104) but "Rubble soil"; Q4col+dl is "colluvial Deluvial deposit" (l. 105) but "Massive gravel"; Q4al is "alluvial deposit" (l. 105) but "Sand and pebble gravel". The legends of Fig3 (a) and (b) carry no symbols and use further names ("Granite", "Diorite", "Massive gravelly soils", "Sand and pebble gravel", and in (b) also "Massive gravel"), so it is not possible to tell whether "Granite" means γo2 or γM2 ("Hybrid granite", Fig2 (c) and Fig4, not mentioned in the text) and whether "Massive gravelly soils" is Q4del or Q4col+dl. (2) Missing units: the nine legend entries of Fig2 (c) do not include the quartz diorite and the Triassic sand slate T3bg of l. 102 to 103, and the left bank is mapped as γM2. (3) Symbols: the text writes "γO2" with upper-case O, the legends of Fig2 (c) and Fig4 "γo2"; Fig4 writes "Q" with superscript "del" instead of Q4del. (4) Colours: granite is green in Fig2 (c), dark brown in Fig3 (a) and pink with crosses in Fig3 (b); in Fig3 (a) "Diorite" (#8c7c74) and "Sand and pebble gravel" (#8c745c) differ by 32 in the RGB sum, below the threshold of 40 for distinguishable colours, and the grey block body (#747474) differs from them by 32 and 48. Because the model strata are built "According to the geological engineering drawing" (p. 9, l. 180), the reader needs one consistent unit list to follow the model set-up. The different names may be intended as genetic names in the text and lithological names in the legends; this is put as a question. The location markers of Fig2 are treated in GB-09. |
| Suggestion | Use one name, one symbol and one colour per unit in p. 5, l. 101 to 105, the legends of Fig2 (c) (p. 6), Fig3 (a) and (b) (p. 8) and Fig4 (p. 10): write "γo2" in l. 102 and "Q4del" with subscript 4 in Fig4, add the symbols to the legends of Fig3, name γM2 in the text, map the quartz diorite and T3bg or remove them from l. 102 to 103, and give "Diorite" and "Sand and pebble gravel" in Fig3 (a) clearly different colours; if legend names are lithological and text names genetic, give both once in the legend of Fig2 (c). |
| Status | verified (names, symbols and colours at the page images p. 5, 6, 8, 10, measured by S2 and AB at 300 and 600 dpi); assumption (that the different names are intended as genetic versus lithological names) |
| Severity | moderate |
| Source | S2, AB |

**GB-11 Several factual statements in Sections 2 and 3 carry no citation, including the statement that justifies the substitute input motion, although the main text after p. 2, l. 63 cites no source at all.**

| Field | Content |
|---|---|
| Check | P13, P28 |
| Location | p. 5, l. 110 to 112; p. 5, l. 114 to 121; p. 6, l. 136 to 138; p. 9, l. 169 to 170; p. 10, l. 186 to 189; p. 15, l. 311 to 312 |
| Quotation | "tens of thousands of people drowned"; "Extensive research indicates that the Kangding earthquake is comparable to the 2008 Wenchuan earthquake in terms of damage distribution, affected intensity, and estimated magnitude." |
| Concern | A search of text.json from p. 3 to p. 26, l. 506 for author and year patterns ("et al", "and" followed by a year, a capitalised name followed by a comma and a four-digit year) gives 0 hits (PP-54); the only citations stand in p. 1, l. 34 to p. 2, l. 63. Hence the following statements have no source: (a) the 1786 breach "after 9 days" and the death toll (l. 110 to 112); the abstract of Zhao et al. (2021), which is in the list, gives "over 100 000 deaths" (read by S1 via IDEAS/RePEc); (b) the gap statements "relatively few" (l. 119) and "have not been fully studied in detail" (l. 121), without source or search (compare GB-02 and GB-06 for the introduction); (c) the Tiezhuang Temple tablet as the only record of the event (l. 136 to 138); (d) 3DEC as "one of the most widely used numerical methods in rock mechanics" (l. 169 to 170); (e) "Extensive research indicates" (l. 187 to 189), which is the only justification for using the 2008 Wenchuan record as the input motion (see GB-21 and GB-22); (f) the failure mechanisms "seismic wave amplification at higher elevations, the back-slope effect, and dynamic interface stress effects" (l. 311 to 312), which appear in the abstracts of Zhou et al. (2024) and Wu, J. et al. (2013), both in the list and never cited (GB-50). Graded moderate because (e) carries the choice of the load that drives every result. |
| Suggestion | Add sources at p. 5, l. 110 to 112 and l. 114 to 121, p. 6, l. 136 to 138, p. 9, l. 169 to 170, p. 10, l. 187 to 189 (the studies behind "Extensive research") and p. 15, l. 311 to 312 (for example Zhou et al. 2024 and Wu et al. 2013 if they are meant), or reword the statements as the authors' own assessment. |
| Status | verified (absence of citations, by text search; wording at the page images p. 5, 6, 9, 10, 15); verified for the figure in the abstract of Zhao et al. 2021 (read by S1, https://ideas.repec.org/a/spr/nathaz/v106y2021i1d10.1007_s11069-020-04471-1.html); inferred (that Zhou et al. 2024 and Wu et al. 2013 support l. 311 to 312, from their abstracts as reported by S1) |
| Severity | moderate |
| Source | ZF |

**GB-12 Settings that govern the simulated energy partition and the input data are not stated.**

| Field | Content |
|---|---|
| Check | P35 |
| Location | p. 6, l. 130 to 131; p. 9, l. 168 to 170; p. 10, l. 189 to 202; p. 10, Fig4 (inset) |
| Quotation | "According to the DEM data obtained by UAV scanning"; "the three-dimensional discrete element program (3DEC), one of the most widely used numerical methods in rock mechanics" |
| Concern | DE is computed as a residual (Eq. 4), so every setting that removes energy in the model enters DE directly (GB-41). Searches over the whole text.json: "damp" 0 hits, "time step" 0 hits, "version" 0 relevant hits (the hits are "inversion" and "conversion"), "rigid" 0, "deformab" 0, "resolution" 0, "accuracy" 1 hit (alpha, l. 282). Not stated are therefore: 3DEC version, damping scheme and value, time step, rigid or deformable blocks, DEM resolution, accuracy and survey date, UAV and sensor, and for the input motion the component, peak value, duration, scaling, filtering and how the record is applied at the viscous base; the Fig4 inset shows only an unlabelled acceleration trace (GB-23). The missing citation for "one of the most widely used" is part of GB-11; this finding concerns the settings themselves. |
| Suggestion | Add to Section 2.1 a table of model settings (software version, block type, damping, time step, contact law, run length) and of the input motion (station, component, PGA, duration, processing, application at the base), and state UAV, sensor, survey date, DEM resolution and vertical accuracy at p. 6, l. 130 to 131. |
| Status | verified (searches) |
| Severity | moderate |
| Source | SD |

**GB-13 The restored pre-landslide terrain, from which the whole sliding mass is built, is neither checked nor bounded.**

| Field | Content |
|---|---|
| Check | P10, P27 |
| Location | p. 6, l. 138 to p. 7, l. 143; p. 7, l. 157 to 162; p. 9, Fig3 (c); p. 2, l. 49 to 51 |
| Quotation | "the contour lines corresponding to the sliding bed and accumulation area are modified to be straight"; "the restored terrain is smooth and the surface does not fluctuate, the mountains become continuous, which can be regarded as the terrain before the landslide" |
| Concern | The manuscript discloses that the restored surface is smooth (l. 160 to 162). Beyond that, the restoration is a judgement step (which contours, how far, how straight) without a stated rule, and the only check is the visual comparison in Fig3 (c). The restored surface defines the sliding mass, so it enters every energy value, the runout and the validation unchecked. The "new idea" (l. 49 to 51) is a claim of methodological improvement, which needs a comparison or an error estimate; none is given (GB-02 concerns the literature behind the claim). A mass balance is available from the manuscript's own data: restored minus present source surface against present deposit minus valley floor. The stated volumes already disagree (GB-16), which shows that such a check matters. GB-11 concerns the uncited tablet record in p. 6, l. 136 to 138 and GB-04 the citations that end in p. 2, l. 49; this finding concerns the restoration itself. |
| Suggestion | In Section 2.1, state the restoration rule (which contours, interpolation, extent), compute the depleted source volume and the deposit volume from the UAV DEM and report the mass balance with a bulking factor; give an upper and a lower restoration and propagate the volume range to the energy results, or test the procedure on a landslide with a known pre-event DEM. |
| Status | verified (absence of rule and check); inferred (consequence for all results) |
| Severity | major |
| Source | SD |

**GB-14 Fig3 (a) shows two zones where the text announces four.**

| Field | Content |
|---|---|
| Check | P3 |
| Location | p. 7, l. 144 to 146; p. 8, Fig3 (a) |
| Quotation | "The whole landslide occurrence area can be divided into four parts: the rock wall area, colluvial slope area, slope debris flow area, and main accumulation area." |
| Concern | Fig3 (a) marks two zones (legend "I Sliding bed", "II Accumulation area"; labels I and II inside the red boundary, separated by one dotted line), counted on the page image. The four parts named in l. 145 to 146 are delimited neither in Fig3 (a) nor in any other figure. GB-13 concerns the restoration shown in Fig3 (c); this finding only the zones of Fig3 (a). |
| Suggestion | Delimit and label the four parts in Fig3 (a) (p. 8), or reduce p. 7, l. 145 to 146 to the two zones that are shown. |
| Status | verified |
| Severity | minor |
| Source | AB |

**GB-15 The length of 450 m given for the landslide contradicts the 1021 m of the model, the slope profile in the same paragraph and the landslide boundary mapped in Fig2 (c).**

| Field | Content |
|---|---|
| Check | P2, P1, P3 |
| Location | p. 7, l. 148 to 150; p. 9, l. 173 to 174; p. 6, Fig2 (c) |
| Quotation | "with a main sliding direction of 75°, distributed along the NEE-SWW direction, about 450 m long, about 1000 m wide along the river, and a planar area of 0.45 km²"; "The length of the landslide mass in the sliding direction is 1021 m, and the vertical height is about 747 m" |
| Concern | The planar values agree with each other (450 m x 1000 m = 0.45 km²), but not with three other sources. (a) Profile of l. 151 to 156: the horizontal extent of the four segments, sum of the elevation differences divided by tan(slope), is 176.2 m + (235.2 to 571.5 m) + 314.2 m + 188.3 m = 914.0 to 1250.2 m (Python), close to the model length of 1021 m and two to almost three times 450 m. (b) Model: 1021 m slope length and 747 m height give a horizontal length of sqrt(1021² - 747²) = 696 m (Python). (c) Map: in Fig2 (c) (2.194 m per px), the magenta landslide boundary spans 1217 m along the section line a-a' (azimuth 73.6 degrees, consistent with the stated 75 degrees) and 1030 m across it, with a convex hull of 0.989 km²; the yellow unit Q4del alone covers 0.476 km², 652 m along a-a' and 989 m across (measured by AB). Possible resolutions, put as questions: A, length and width are swapped (the dimension "along the river" is the width, since the sliding direction points to the river); B, the 450 m and 0.45 km² describe the deposit only. The reader cannot tell which outline the values refer to. The elevations and angles of l. 151 to 156 are checked against Fig3 (b) in GB-17; the volume in the same paragraph is treated in GB-16. Neighbouring GB-09 and GB-10 concern other content of Fig2. |
| Suggestion | In p. 7, l. 148 to 150, state whether length, width and area refer to the whole landslide or to the deposit, check for a swap of length and width, and give values consistent with the boundary in Fig2 (c) and with the 1021 m of the model (p. 9, l. 174). |
| Status | verified (discrepancy, page images p. 6, 7, 9; boundary measured by AB); inferred (horizontal extents, Python); assumption (resolutions A and B, put as a question) |
| Severity | moderate |
| Source | S3, AB |

**GB-16 The landslide volume is given as three incompatible values, the model holds 1.3 % of the stated volume, and the energy magnitudes in Fig8 fit neither volume.**

| Field | Content |
|---|---|
| Check | P1, P2, P3, P36 |
| Location | p. 7, l. 149 to 151; p. 9, l. 178 to 182; p. 13, Table 2 (column "Volume"); p. 20, Fig8; p. 16, l. 330 |
| Quotation | "The average thickness of the landslide mass is about 100 m, and the volume is about 2400×10⁴ m³"; "The whole model contains 25345 blocks, 2788 m long, 3341 m wide, 1121m high, and the volume of the landslide is 317563 m³." |
| Concern | (a) Planar area times mean thickness: 0.45 x 10^6 m² x 100 m = 4.5 x 10^7 m³, not 2.4 x 10^7 m³ (factor 1.875); 2.4 x 10^7 m³ over 0.45 km² implies a mean thickness of 53.3 m. (b) The model volume of 317,563 m³ is 1.3 % of 2.4 x 10^7 m³ (factor 75.6) and corresponds to a mean thickness of 0.71 m over 0.45 km²; the ten monitored blocks of Table 2 (756.2 to 1754.3 m³ on the 8.7 m x 8.7 m footprint of l. 178) are 10.0 to 23.2 m high, whereas l. 178 to 179 say that the block height is the full thickness to the sliding bed. The number of blocks in the sliding mass is not given; the 25,345 blocks of l. 181 include the base. (c) Fig8, measured by AB (0 GJ at 1430.5 px, 7000 GJ at 699.5 px): PE 6502 GJ at the first bar, total 6521 GJ, KE peak 1657 to 1681 GJ at 13.6 s. With the model volume and 2300 kg/m³ (Table 1), m = 7.304 x 10^8 kg, the mean fall height is 6.521 x 10^12 / (7.304 x 10^8 x 9.81) = 910 m, more than the whole relief from the top of the mass to the river, 747 m + 131 m = 878 m (l. 174 to 175), and the root-mean-square speed at the KE peak is sqrt(2 x 1.657 x 10^12 / 7.304 x 10^8) = 67.4 m/s, while the maximum block velocity is 31.6 m/s (l. 330), which caps KE at 364.7 GJ. With the field volume, the mean fall height is 12.0 m, while the Fig9 totals of the ten blocks imply 29.8 to 316.7 m (Python, all values). Possible resolutions, put as questions: A, 317,563 m³ is a typing or unit error; B, the model represents only part of the landslide; C, the field volume or thickness is wrong. Under B the simulation would not reproduce the Mogangling landslide at its size, which changes what Section 3.1 can show ("the extent and morphology ... closely match", p. 16, l. 357 to 359) and every energy magnitude; hence major. GB-15 concerns the planar dimensions in the same paragraph; the PE datum is treated in GB-31. |
| Suggestion | In Section 2.1 (p. 7, l. 149 to 151; p. 9, l. 178 to 182), state one volume for the real landslide and one for the modelled sliding mass with its number of blocks, derive the latter from restored minus present surface, explain any difference, correct thickness or volume so that area times thickness agrees, and state in Section 3.2.1 the mass (volume and density) used for Fig8; if the model mass is indeed about 0.3 x 10^6 m³, rebuild the model at full volume or explain why a reduced mass represents the event. |
| Status | verified (the stated values and their disagreement, page images p. 7, 9, 13; Fig8 values measured by AB); inferred (ratios, heights, fall heights and speeds, Python); assumption (resolutions A to C, put as a question) |
| Severity | major |
| Source | S3, SD, AB |

**GB-17 The elevations and slope angles given in the text do not match the profile in Fig3 (b).**

| Field | Content |
|---|---|
| Check | P3 |
| Location | p. 7, l. 151 to 156; p. 8, Fig3 (b) |
| Quotation | "The elevation of the slope toe is 1120 m (about 5 m higher than the river surface), and 1120 m-1330m is the front edge of the landslide accumulation mass, with a slope of about 50°" |
| Concern | Calibration by AB at 300 dpi: vertical scale 0.542 px per m (2000 m at 1849.5 px, 1000 m at 2391.5 px), x axis calibrated on the scale bars under 0 and 1500 (0.558 px per m), vertical exaggeration 0.97. Straight lines fitted to the digitised ground surface per elevation band give 22.3 degrees for 1120 to 1330 m (text about 50), 17.3 degrees for 1330 to 1380 m (text 5 to 12), 29.8 degrees for 1380 to 1600 m (text about 35) and 50.8 degrees for 1600 to 1831 m (text 57 for 1600 to 1890 m). The water surface in Fig3 (b) lies at 1146 plus or minus 2 m and the lowest ground point at 1147 m, whereas the text gives a toe at 1120 m about 5 m above the river; Fig2 (c) supports the text (the 1125 m contour runs along the river). Only the steep step of the deposit front reaches about 50 degrees, between 1294.3 m and 1231.5 m (atan(62.8 / 43.0) = 55.6 degrees), above the band given for the front edge. GB-16 and GB-15 concern the other values of the same paragraph; GB-15 uses these elevations for the horizontal extent; GB-14 and GB-13 concern Fig3 (a) and (c). |
| Suggestion | State in p. 7, l. 151 to 156 from which profile or DEM transect the elevations and angles were taken, or redraw Fig3 (b) so that toe, front edge, platform and wall carry the stated elevations, and mark these zones in the profile. |
| Status | verified (measured by AB); the cause (another transect or a drafting error) is open |
| Severity | moderate |
| Source | AB |

**GB-18 The text refers to sections a-a' and b-b' in Fig2 (c) and to results in Fig3 (c), but only section a-a' exists, and Fig3 (c) shows no section.**

| Field | Content |
|---|---|
| Check | P38, P4, P3 |
| Location | p. 7, l. 159 to 160; p. 6, Fig2 (c); p. 8, Fig3 (b); p. 9, Fig3 (c) |
| Quotation | "As shown in Fig3. (b), make a section along a-a'and b-b' in Fig2. (c). The results are shown in Fig3. (c)." |
| Concern | Search of the whole text.json for "a-a" and "b-b": 1 hit each, both at l. 160. Fig2 (c) shows one section line with end labels "a" and "a'" (AB at 600 dpi); there is no b or b'. Fig3 (b) is headed "(a-a')" and is the only profile; the length of a-a' measured in Fig2 (c), about 1509 m, agrees with its 0 to 1500 m axis (PP-15). Fig3 (c) shows contour maps and shaded terrain before and after restoration, not sections. The comparison of restored and present terrain (l. 160 to 162) is the only check of the restoration the model rests on (GB-13), so a reader who looks for b-b' cannot follow it; graded moderate for that reason. Neighbouring GB-09, GB-10 and GB-15 concern other content of Fig2. |
| Suggestion | Either draw section b-b' in Fig2 (c) and add its profile to Fig3 (b), or delete "and b-b'" in p. 7, l. 160; point "The results are shown in Fig3. (c)" to the panel that shows the section comparison, or say what Fig3 (c) shows. |
| Status | verified (text and figures at the page images) |
| Severity | moderate |
| Source | S2, S4, AB |

**GB-19 Fig3 lacks axis quantities and units in (b), explains neither the "80°" symbol nor the lower panels of (c), and puts a linear scale bar on an oblique block diagram.**

| Field | Content |
|---|---|
| Check | P29 |
| Location | p. 8, Fig3 (a) scale bar, Fig3 (b) axes and "80°" symbol; p. 9, Fig3 (c) lower panels; caption, p. 9, l. 166 to 167 |
| Quotation | "Fig3. Landslide restoration diagram: (a) 3D views of the study area; (b) Engineering geological profile; (c) Comparison map of surface topography before and after restoration" |
| Concern | Fig3 (b) has numbers on both axes (1000 to 2000; 0 to 1500) but no titles and no units. The symbol "80°" with a short line at the top of (b) has no legend entry and is not explained. Fig3 (a) is an oblique 3D block view with a scale bar "0 400 1000m", which cannot apply to all distances in such a view. The two lower panels of (c) (shaded terrain "before repair" and "after repair") have no scale and no north arrow; the upper panels of (c) have a north arrow pointing to the right, which the caption does not mention. GB-14 and GB-17 concern the content of (a) and (b), GB-13 the restoration shown in (c), GB-18 the sections; this finding only the form. |
| Suggestion | Add "Elevation (m)" and "Distance along a-a' (m)" to Fig3 (b); explain "80°" in the legend; remove the scale bar from (a) or replace it by a scale valid for one reference line; add scale and north arrow to the lower panels of (c) and state the rotation in the caption (p. 9, l. 166 to 167). |
| Status | verified |
| Severity | minor |
| Source | AB |

**GB-20 Structural planes are declared "ignored", yet the model contains discontinuities and the results explain failure by structural planes.**

| Field | Content |
|---|---|
| Check | P6, P17 |
| Location | p. 9, l. 175 to 180; p. 11, l. 208 to 210; p. 11, Table 1 (rows "discontinuities" and "potential discontinuities"); p. 15, l. 308 to 310; p. 15, l. 323; p. 25, l. 469 |
| Quotation | "the impact of the structural plane on the landslide process has to be ignored in this study"; "A uniform structural plane is set inside."; "Under the combined influence of structural plane control and strong seismic forces" |
| Concern | The limitation is disclosed where the model is introduced (l. 175 to 178), but its consequences are not drawn. In the same section the model receives "a uniform structural plane" (l. 179 to 180) and, in l. 209 to 210, "potential rupture planes and joint sets" with their own parameters (Table 1). Their geometry (orientation, spacing, persistence) is not stated, so the reader cannot tell whether "ignored", "uniform" or "joint sets" describes the model. The results then attribute dislocation and failure to "steeply dipping structural planes" (l. 308 to 309) and "structural plane control" (l. 323), and Conclusion 2 claims that the simulation incorporates "geological structures" (l. 469). Graded major because the failure mechanism described in Section 3.1 answers the aim "formation mechanism" (p. 2, l. 39) and cannot be shown by a model in which structural planes were ignored or uniform. The assignment of the Table 1 sets to model elements is treated in GB-25; GB-16 concerns the block size and volume stated in p. 9, l. 178 to 182. |
| Suggestion | In Section 2.1, state the geometry of the uniform structural plane, the joint sets and the potential rupture planes built into the model; then either remove the structural-plane explanations in p. 15, l. 308 to 310 and l. 323 and "geological structures" in p. 25, l. 469, or add a run with mapped or assumed steep discontinuity sets and compare the failure sequence with the uniform case. |
| Status | verified |
| Severity | major |
| Source | SD |

**GB-21 The design cannot isolate the role of the earthquake or support general laws: one run, one substitute input record, one case, no comparison condition.**

| Field | Content |
|---|---|
| Check | P10, P9 |
| Location | p. 10, l. 183 to 191; p. 15, l. 307 to 318; p. 1, l. 1 to 3; p. 2, l. 40 to 41; p. 2, l. 70 to 71 |
| Quotation | "this study adopts the acceleration records measured at the Luding station during the Wenchuan earthquake as the input ground motion"; "The back-slope effect and amplification at higher elevations during seismic wave propagation significantly increased the peak ground acceleration of the Mogangling slope"; "so as to summarize the law of high-level rock landslide induced by earthquake" |
| Concern | The manuscript states openly why the 1786 motion is unavailable and substitutes the Wenchuan Luding record (l. 183 to 191). Its consequences are not drawn. The title ("induced by a strong earthquake"), the aim "under strong seismic conditions" (l. 71) and the results narrative (P-waves, S-waves, back-slope effect, amplification, p. 15, l. 307 to 318) make causal statements about the seismic loading, but the design contains no comparison that could carry them: no gravity-only run, no second record or scaled amplitude, and no acceleration record at the slope against the base input. Searches over the whole text.json: "amplif" 2 hits (l. 311, l. 316, both narrative), "peak ground" 1 hit (l. 317), "PGA" no further hit, "gravity" 0, "sensitiv" 0. The claimed increase of the peak ground acceleration is therefore not measured in the reported results, and the aim of a general "law" (l. 40 to 41) rests on one case and one run. Graded major because the attribution of the failure stages to seismic wave effects would not stand without a comparison. The missing source for the substitution is part of GB-11; settings of the input are in GB-12. |
| Suggestion | In Sections 2.1 and 3.1, add a gravity-only run with an otherwise identical model, at least two further input motions or amplitude scalings of the Luding record, and acceleration histories at the monitoring points against the base input; report runout, peak velocity and energy partition for each run; restrict the title, p. 2, l. 40 to 41 and the conclusions to the Mogangling case unless further cases are added. |
| Status | verified (absence of a comparison condition and of amplification measurements, searches); inferred (that the narrative depends on such a comparison) |
| Severity | major |
| Source | SD |

**GB-22 Third-party inputs (the Luding strong-motion record, the remote sensing image, the geological map and the base map) are named without provenance, and the data statement cannot cover them.**

| Field | Content |
|---|---|
| Check | P12 |
| Location | p. 10, l. 189 to 191; p. 10, Fig4 (inset); p. 6, Fig2 (a), (b) and (c); p. 6, l. 126 to 127; p. 9, l. 180 to 181; p. 26, l. 505 to 506 |
| Quotation | "this study adopts the acceleration records measured at the Luding station during the Wenchuan earthquake as the input ground motion for the dynamic numerical simulation analysis of the Mogangling landslide"; "According to the geological engineering drawing, different strata are generated" |
| Concern | The input ground motion drives the whole simulation, and the manuscript explains why a substitute record is used. What is missing is where it comes from: no data provider, network, station code, component, sampling rate, scaling or citation. Search of the whole text.json for "station/record/network/center/bureau/provided by/Google/Landsat/satellite/survey": 13 hits, of which only l. 190 concerns the record, and no reference entry concerns strong-motion data. The same holds for the remote sensing image of Fig2 (b), the engineering geological map of Fig2 (c), the "geological engineering drawing" of l. 180 (it is not said whether it is the same map) and the base map of Fig2 (a): caption (l. 126 to 127), text and statements give no source, date or resolution, and the panels carry no credit line. The Luding record was recorded by a third party (2008 event, l. 190), so "available from the first author ... upon reasonable request" (l. 505 to 506) does not by itself give access to it. Whether image and map are own or third-party products cannot be decided from the manuscript. GB-21 concerns the design consequences of the substitution, GB-12 the processing of the record, GB-11 the unsourced justification in l. 187 to 189; this finding concerns provenance and access; GB-20 concerns the structural planes named in p. 9, l. 179 to 180. |
| Suggestion | At p. 10, l. 189 to 191, cite the provider of the Luding record (agency or database, station code, component, sampling interval, filtering or scaling) and name it in the data statement (p. 26, l. 505); add source, acquisition date and resolution of the image in Fig2 (b), the source of the map in Fig2 (c) and of the base map in Fig2 (a) to the caption (p. 6, l. 126 to 127), and state at p. 9, l. 180 whether the drawing is the map of Fig2 (c). |
| Status | verified (absence of provenance, search as stated); inferred (third-party origin of the Luding record, from l. 190); the origin of image and map is put as a question |
| Severity | moderate |
| Source | S2 |

**GB-23 The input acceleration inset in Fig4 has no time values or time unit, its markers are not explained, and the trace exceeds the axis range.**

| Field | Content |
|---|---|
| Check | P29 |
| Location | p. 10, Fig4 (inset, lower right) and legend; caption, p. 10, l. 192 |
| Quotation | "Fig4. Discrete numerical model with fine topography" |
| Concern | At 600 dpi (AB) the horizontal axis of the inset carries ticks but no numbers and no title, so neither duration nor time of peak can be read. The markers "tp", "tPGA", "tf" and "te" are explained nowhere (search of text.json for the markers: 0 hits; "peak ground acceleration" occurs once, l. 317, without reference to Fig4). With ticks at 100, 0 and -100 gal (99.25 px per 100 gal), the axis spans +153 to -175 gal, while the trace reaches -223 gal and at least about +216 gal, so the peak lies outside the axis. The legend symbols γo2, Q with superscript del and γM2 are not resolved in Fig4 or its caption. GB-22 concerns the source of the record and GB-12 its component and processing; this finding concerns what the figure shows. |
| Suggestion | Add a time axis in seconds with title, explain tp, tPGA, tf and te in the caption (p. 10, l. 192), extend the acceleration axis to include the peak, and resolve γo2, Q4del and γM2 in the legend. |
| Status | verified (measured by AB) |
| Severity | moderate |
| Source | AB |

**GB-24 The provenance of each material parameter and the target of the parameter inversion are not stated, and the stiffness values of both discontinuity sets raise a question.**

| Field | Content |
|---|---|
| Check | P8 |
| Location | p. 11, l. 206 to 207; p. 11, Table 1 (all rows) |
| Quotation | "the selection of physical-mechanical parameters was based primarily on laboratory testing, empirical analogy, and parameter inversion." |
| Concern | Three sources are named but not assigned to parameters; the laboratory tests are not described (search "laborator/test" in text.json: 1 hit in the body, l. 207), and the target of the inversion (runout, deposit shape or other) is not stated. If the inversion was made against the deposit, the validation in Fig7 (o) is not independent of the calibration (GB-38). In addition, in both discontinuity sets of Table 1 the shear stiffness exceeds the normal stiffness (1500 against 960 GPa/m; 180 against 100 GPa/m), and the "potential discontinuities" have a higher cohesion (1.1 MPa) than the joints (0.8 MPa). This is unusual for rock joints; the point rests on general practice, not on a source, so it is put as a question: are the stiffness columns swapped? The assignment of the parameter sets to the materials of Fig4 is treated in GB-25, the geometry of the planes in GB-20. |
| Suggestion | Add to Table 1 (p. 11) a column with the source of each value (test, analogy with reference, inversion), report the laboratory results, state the inversion target and procedure in Section 2.1 near l. 207, and confirm or correct the stiffness values of both discontinuity sets. |
| Status | verified (no assignment of sources, no inversion target, Table 1 values at the page image p. 11); assumption (that the stiffness columns may be swapped, from general practice, put as a question) |
| Severity | moderate |
| Source | SD, ZF |

**GB-25 The parameter sets of Table 1 ("bed rock", "landslide mass", "discontinuities", "potential discontinuities") are not assigned to the strata and planes of the model named in the text and drawn in Fig4.**

| Field | Content |
|---|---|
| Check | P38, P3 |
| Location | p. 11, l. 207 to 210; p. 11, Table 1 (rows "bed rock", "landslide mass", "discontinuities", "potential discontinuities"); p. 9, l. 173; p. 9, l. 176 to 181; p. 10, Fig4 legend |
| Quotation | "The slope is underlain by plagioclase granite, which is subdivided into strongly weathered and moderately weathered zones. The discontinuities are represented by both fully developed potential rupture planes and joint sets"; "the established model includes the landslide mass and base block" |
| Concern | The model elements appear under several names: the moving body is "landslide mass" (l. 173, Table 1), "Sliding mass" (Fig4 legend) and "slide mass" (l. 257); the stationary part is "base block" (l. 173) and "bed rock" (Table 1); the strata are γo2, Q with superscript del and γM2 in the Fig4 legend, which shows four materials in four colours (dark green, cyan, red, magenta), and "strongly weathered and moderately weathered zones" in l. 208 to 209; the planes are "potential rupture planes and joint sets" (l. 209 to 210), "A uniform structural plane" (l. 179 to 180) and "discontinuities" and "potential discontinuities" (Table 1). Table 1 gives two rock-mass sets and two discontinuity sets. It is not stated whether "bed rock" applies to all three strata of Fig4, including the Quaternary deposit, whether the weathering zones correspond to "bed rock" and "landslide mass", and which discontinuity set is which plane type. Without this assignment the model cannot be rebuilt from Table 1; hence moderate. GB-24 concerns the sources of the values, GB-20 the geometry of the planes, GB-10 the unit names. |
| Suggestion | In Section 2.1 near p. 11, l. 210 to 212, or as a column of Table 1, state for each parameter set the model element of Fig4 it is assigned to (or add one row per material of Fig4), and use the same names for the moving body and the planes in the text, Table 1 and Fig4. |
| Status | verified (all names at the page images p. 9, 10, 11; missing assignment as absence in p. 9 to 11) |
| Severity | moderate |
| Source | S2, AB |

**GB-26 "Effective collisions" are velocity peaks, not detected collisions; the threshold is chosen by eye and never checked against contact data, yet Conclusions 2 and 4 rest on them.**

| Field | Content |
|---|---|
| Check | P31, P32, P8 |
| Location | p. 11, l. 215 to 234; p. 12, Fig5 (a) to (f); p. 22, l. 414 to 421; p. 25, l. 473 to 475; p. 26, l. 483 to 487 |
| Quotation | "this study examines those collisions that markedly increase block velocities"; "At a threshold of 30%, however, the identification of effective collisions is deemed acceptable." |
| Concern | The method measures local velocity maxima, not collisions; a velocity peak can also follow acceleration by gravity on steep ground or by seismic shaking, and the manuscript does not separate these causes. The 30 % threshold is "deemed acceptable" by visual inspection of one curve (Fig5 (b) to (f)); no independent sample of peaks was checked against contact events, so neither false positives nor missed collisions are estimated. "30 %" is not defined (30 % of what quantity), and prominence, width and position are mixed in one threshold (l. 227 to 229). The tool performing the peak search is not named, and Fig5 (a) is called "typical" (l. 221) without a selection rule. Graded major because Conclusion 2 (l. 473 to 475), Conclusion 4 (l. 483 to 487) and the abstract claim on collision frequency depend on this detector. The marker counts per threshold measured in Fig5 and the basis of the count of 1,139 are in GB-29. |
| Suggestion | In Section 2.2, define the threshold quantity, name the tool and state the block set behind the detected events; validate the detector on a random sample of blocks against the contact records of the simulation (contact force or impulse time series), report precision and recall for 10 % to 50 %, choose the threshold from that comparison, and separate peaks after contact impulses from peaks after free acceleration. |
| Status | verified (absence of a check, a definition and a block set); assumption (alternative causes of velocity peaks), put as a question: were contact events used to confirm any detected peak? |
| Severity | major |
| Source | SD |

**GB-27 In Fig5 (a), two of the six red "effective collision" markers do not sit on local velocity maxima.**

| Field | Content |
|---|---|
| Check | P3 |
| Location | p. 11, l. 220 to 224; p. 12, Fig5 (a) |
| Quotation | "A local velocity peak (denoted by red or purple markers) corresponds to an acceleration phase, but only those pronounced peaks (highlighted in red) yield a substantial velocity increase" |
| Concern | Fig5 (a) at 600 dpi (AB): y ticks 14 m/s at 86.0 px and 0 at 900.5 px (0.01719 m/s per px), x ticks 0 m at 161.0 px and 600 m at 1212.0 px; 6 red and 5 purple markers. The red marker at 243.4 m has 13.05 m/s, the next point at 262.4 m 13.41 m/s, so it lies on a rising flank and the local maximum is unmarked. The red marker at 463.3 m has 4.21 m/s, and the following points rise further (cluster at 473.7 m with 4.67 m/s). The other four red markers (10.2, 12.3, 13.5 and 7.5 m/s) are local maxima. Since Fig5 (a) is the definition figure, the rule cannot be reproduced from it. GB-26 concerns whether velocity peaks are collisions at all; this finding concerns the placement of the markers in the definition figure. |
| Suggestion | Check the peak detection for Fig5 (a) (p. 12); move the two markers to the local maxima at 262 m and after 470 m, or explain in p. 11, l. 220 to 224 why a point on a rising flank counts as an effective collision. |
| Status | verified (measured by AB) |
| Severity | moderate |
| Source | AB |

**GB-28 The abscissa of the curves used to detect effective collisions is called "travel distance", "Travel Displacement" and "displacement", which are different quantities.**

| Field | Content |
|---|---|
| Check | P38 |
| Location | p. 11, l. 221 to 234; p. 12, Fig5 (a) to (f) (x-axis titles); p. 1, l. 22 to 23; p. 25, l. 473 to 475; p. 23, Fig10 (b) |
| Quotation | "presents a typical velocity-travel-distance curve for an individual block"; "the effective collision of blocks in the process of landslide is obtained by extracting the local peak value of the displacement velocity curve"; "effective block collisions during the landslide can be identified by extracting local peaks from displacement-velocity curves" |
| Concern | The method names the curve consistently as velocity against travel distance (l. 221, 225, 227, 234), and Fig5 (a) and Fig10 (b) label the axis "Travel distance (m)". The axes of Fig5 (b) to (f), on which the 30 % threshold and the count of 1,139 rest, are labelled "Travel Displacement (m)" (5 of 5 panels, page image p. 12), and the abstract (l. 22 to 23) and Conclusion 2 (l. 474 to 475) use "displacement". Travel distance (path length) and displacement (distance between start and current position) differ as soon as a block changes direction, which the manuscript reports for Blocks 1 and 3 (p. 20, l. 397 to 398; p. 22, l. 416). A reader who wants to repeat the peak detection cannot tell which quantity was used; hence moderate. GB-26 concerns the validity of the detector and GB-27 the markers of Fig5 (a); this finding concerns the name of the abscissa. |
| Suggestion | State in Section 2.2 at p. 11, l. 221 which quantity is on the abscissa, and use that name in the x-axis titles of Fig5 (b) to (f) (p. 12), in the abstract (p. 1, l. 22 to 23) and in Conclusion 2 (p. 25, l. 474 to 475). |
| Status | verified (axis titles at the page images p. 12 and 23; text hits in text.json); inferred (that the two quantities differ for the reported rebounding blocks) |
| Severity | moderate |
| Source | S2, AB, SD |

**GB-29 The curve used to choose the threshold in Fig5 (b) to (f) is not identified and peaks at about 45 m/s, above every maximum velocity reported for the run, and the count of 1,139 effective collisions has no stated basis.**

| Field | Content |
|---|---|
| Check | P3, P7, P20, P22 |
| Location | p. 11, l. 229 to 234; p. 11, l. 220 to 221; p. 12, Fig5 (b) to (f); p. 16, l. 330; p. 16, l. 337; p. 23, Fig10 (b) |
| Quotation | "Under this setting, 1,139 effective collisions were detected from the travel-distance versus velocity profile."; "during the impact-at-base stage, the maximum velocity reached 31.6 m/s." |
| Concern | (1) Peak: in Fig5 (b) at 600 dpi (AB: 0 at 1038.0 px, 50 m/s at 81.5 px) the curve reaches 45.3 to 45.5 m/s at about 250 m travel, whereas the text gives 31.6 m/s as the maximum (l. 330, "The velocity reached its peak upon arrival at the valley floor", l. 337) and the colour bars of Fig7 (a) to (g) end at 0, 5.9, 19.6, 27.1, 31.6, 25.7 and 0.21 m/s (PP-35); ratio 45.3 / 31.6 = 1.43. Snapshots could miss a short peak between output times, but the text presents 31.6 m/s as the maximum. (2) Identity: neither caption nor text says which block, which run or whether an aggregate is plotted; Fig5 (a) is another curve (maximum 13.5 m/s, end at about 590 m). (3) Basis of the count: the sentence uses the singular "profile", but it is not said whether 1,139 refers to one block, the ten monitored blocks or all blocks of the sliding mass (whose number is not given; the 25,345 blocks of l. 181 include the base), nor over which time window; the number occurs once in the manuscript (search "1,139" and "1139": 1 hit, l. 233). The red markers in the main plot of (d) number at least 60 below 1550 m and 9 beyond 1835 m, plus 30 in the inset (AB, touching markers merge, so lower bounds), of order 10², not 1,139. The read values of Fig10 (b) sum to 1212.8, 74 more than 1,139 (GB-42). (4) Threshold effect: the markers below 1550 m number 72, 60, 60, 60 and 59 for 10 % to 50 %, beyond 1835 m 30, 31, 9, 0 and 0, in the inset 35, 30, 30, 26 and 3 (AB), so between 20 % and 50 % the markers over the first 62 % of the travel hardly change. Either Fig5 comes from another run or model state, or the maxima of Section 3.1 are not maxima over all blocks; in both cases the threshold calibration may not belong to the data it is applied to. GB-26 concerns the validity of the detector, GB-27 the markers of Fig5 (a), GB-28 the name of the abscissa; this finding concerns the identity of the calibration curve and the count. |
| Suggestion | State in the caption of Fig5 (p. 12) and in Section 2.2 which block (ID in Table 2) or aggregate (b) to (f) show and from which run; explain the 45 m/s peak against the 31.6 m/s of p. 16, l. 330; state over which blocks and time window the 1,139 collisions were counted, give the number per block, and define the prominence threshold so the unchanged markers below 1550 m can be understood. |
| Status | verified (peak and marker counts measured by AB; missing basis at the page images p. 11 and 12); inferred (ratio, Python); assumption (the cause of the discrepancy), put as a question |
| Severity | moderate |
| Source | AB, SD, S3 |

**GB-30 Fig5 explains neither the markers in (b) to (f) nor the grey box and the insets, and plots negative values on a velocity axis.**

| Field | Content |
|---|---|
| Check | P29 |
| Location | p. 12, Fig5 (a) to (f); caption, p. 12, l. 238 to 239 |
| Quotation | "Fig5. Effective collisions identification: (a) definition of effective collisions; (b) threshold=10%; (c) threshold=20%; (d) threshold=30%; (e) threshold=40% and (f) threshold=50%." |
| Concern | Panels (b) to (f) have no legend: the red markers, the shaded grey box (about 1550 to 1830 m, 15 to 26 m/s) and the inset are explained neither in the panels nor in the caption, and the inset axes (1550 to 1800; 14 to 26) carry no titles or units. In (a) the black data points have no legend entry, and the lowest markers at about 590 m reach -0.34 m/s (bottom edge of the marker cluster at 933 px, 0 at 900.5 px, 0.01719 m/s per px, AB), below zero by more than the uncertainty; a speed cannot be negative, so either a velocity component is plotted (which one?) or the values are artefacts. Type size is in GB-08, the content of (a) in GB-27, the axis titles in GB-28, the curve and counts of (b) to (f) in GB-29 and the detector in GB-26; this finding concerns legend and labelling. |
| Suggestion | Add a legend to Fig5 (b) to (f) (red markers: detected peaks; grey box: zoomed range), explain the inset in the caption, give the inset axes titles, add the black points to the legend of (a), and state whether the plotted quantity is the speed or a component. |
| Status | verified |
| Severity | minor |
| Source | AB |

**GB-31 Fig8 and Fig9 plot potential energy relative to the lowest or final position of each block, not relative to the initial height as stated.**

| Field | Content |
|---|---|
| Check | P3, P8, P5 |
| Location | p. 13, l. 252 to 255; p. 13, Table 2 (columns "Coordinate" and "Volume"); p. 20, Fig8; p. 21, Fig9 (a) to (j) |
| Quotation | "the potential-energy calculation uses the model’s initial height as the reference datum rather than true sea level; only the change in potential energy due to relative displacement is considered." |
| Concern | With the initial height as datum, PE(t0) = 0 and PE becomes negative as blocks descend. In the figures PE is largest at t0 and falls to zero: Fig8 PE 6502 GJ at the first bar, below 9.6 GJ from about 110 s; in Fig9 the first-bar PE equals the bar total within 0.13 GJ in all ten panels (4.934, 5.135, 3.963, 3.566, 11.10, 6.578, 1.176, 4.368, 1.593 and 0.939 GJ for points 1 to 10), and the last bar is 0 in eight panels, while points 1 and 3 reach 0 at about 81 s and 89 s and end at 0.373 and 0.341 GJ (AB, measured). With 2300 kg/m³ and the volumes of Table 2, the initial PE implies heights above datum of 238, 221, 234, 163, 314, 170, 29, 192, 80 and 42 m for blocks 1 to 10, while their z coordinates rise from 340 to 755 m; the implied datum (z minus height) ranges from 102 m (block 1) to 713 m (block 10), and the rank correlation between z and implied height is -0.65 (SD, Python). A common datum would give the highest PE to the top blocks; a datum at each block's initial height would give PE(t0) = 0. Neither matches; a datum at each block's lowest elevation fits, which is put as a question. DE curves depend only on height differences and are unaffected, but the PE magnitudes, the PE "rebound" of blocks 1 and 3 (p. 20, l. 397 to 399) and the sum over blocks in Fig8 have no common datum. GB-16 concerns the mass behind the magnitudes in Fig8. |
| Suggestion | State the datum actually used for each block and for the whole mass, with an equation, in p. 13, l. 252 to 255, or recompute PE relative to the initial height (or one common datum) and redraw Fig8 and Fig9. |
| Status | verified (PE values measured by AB); inferred (implied heights and datum, Python); assumption (a per-block lowest elevation as datum), put as a question |
| Severity | moderate |
| Source | AB, SD |

**GB-32 Three analyses announced in the methods are not reported: the maximum unbalanced force that should show the end of the run, the stress histories of the ten monitored blocks, and an evaluation of the stress maps.**

| Field | Content |
|---|---|
| Check | P11, P31 |
| Location | p. 13, l. 258 to 263; p. 13, Table 2 (row ID 11 and column "Monitoring contents"); p. 3, l. 80 to 82; p. 15, l. 298 to p. 16, l. 359; p. 18, Fig7 (h) to (n) |
| Quotation | "In addition, the maximum unbalanced force was tracked to verify that the model reached post-failure stability."; "For the local analysis, displacement, velocity, and stress histories were extracted for each of the ten monitored blocks" |
| Concern | (a) Maximum unbalanced force (Table 2, ID 11): search for "unbalanced" in the whole manuscript gives 2 hits (l. 258 and Table 2), none in the results, so the check that the run reached equilibrium at 131 s, which is also the duration result of p. 15, l. 300 to 301 and the end point of Fig8, Fig9 and Fig11, is not documented; Fig9 (a) and (c) still show PE changing after 100 s. (b) Stress histories of the ten blocks (Stress-XX, -YY, -ZZ in Table 2): no plot or value in Section 3; Fig9 shows energies and Fig10 (a) trajectories only. (c) Stress maps of the whole mass: Section 3.1 gives a maximum velocity for each stage b to g (5.9, 19.6, 27.1, 31.6 and 25.7 m/s and "approached 0 m/s"), but neither a value nor a description for the stress maps h to n; search for "stress" in l. 297 to 459 gives 3 hits (l. 302, l. 312 and the Fig7 caption, l. 369), none describing the maps, although the methods name stress as a basis for inferring the evolution (p. 3, l. 81 to 82). The content of the stress panels is treated in GB-39 and GB-40; GB-16 and GB-31 use other columns of Table 2. |
| Suggestion | In Section 3.1, add the history of the maximum unbalanced force with the stability criterion and its value at 131 s, describe the stress maps of Fig7 (h) to (n) with the maximum stress per stage, and either report the stress histories of the ten blocks or remove them from p. 13, l. 262 and Table 2. |
| Status | verified (text search in text.json, confirmed at the page images p. 13, 15, 16, 19 and 21) |
| Severity | moderate |
| Source | S3, SD |

**GB-33 "Field investigations" are named as a data source for the aims, the failure sequence and Conclusion 2, but nowhere described.**

| Field | Content |
|---|---|
| Check | P19 |
| Location | p. 13, l. 264 to 266; p. 2, l. 65 to 66; p. 25, l. 472 to 473 |
| Quotation | "the sequence of failure and run-out at Mogangling was inferred by integrating the numerical results with field-investigation findings."; "This study aims to comprehensively utilize field investigations, drone aerial surveying, discrete element numerical simulation"; "Based on numerical simulation results and field investigations, the landslide movement process can be analyzed." |
| Concern | Search for "field" and "investigat" over the whole text.json: 11 and 10 hits; outside the literature, the reference list, the author contributions, the term "free-field boundaries" and l. 114 (reservoir slope investigations in general), the hits are only l. 65, l. 266, l. 354, l. 471 and l. 472 to 473. None says what was observed, when, where or by whom. Of the 40 result panels (Fig7 a to o, Fig8, Fig9 a to j, Fig10 a and b, Fig11 a to j, Fig12 a and b; 15 + 1 + 10 + 2 + 10 + 2 = 40), 39 are model generated and one (Fig7 (o)) contains field photographs. The failure sequence (l. 264 to 266) therefore rests on model output and on field findings a reader cannot see. GB-32 concerns other announced analyses in the same paragraph. |
| Suggestion | Add to Section 2 a subsection on the field investigation (date, observations, sampling, mapped features) and show the findings used for the failure sequence, or delete "field investigations" in p. 2, l. 65, p. 13, l. 266 and p. 25, l. 472 to 473. |
| Status | verified (searches); inferred (share of model-generated panels, count at the page images) |
| Severity | moderate |
| Source | SD |

**GB-34 The monitoring points of Fig6 cannot be matched to Table 2: the labels of the two middle zones are swapped, the points carry no IDs, and their colours differ from Fig10 (a).**

| Field | Content |
|---|---|
| Check | P38, P2, P3, P29 |
| Location | p. 14, Fig6 (zone labels, spheres, axes); p. 13, Table 2 (columns "Position" and "Coordinate"); p. 13, l. 256 to 257; p. 23, Fig10 (a) legend; p. 1, l. 29; p. 26, l. 483 to 487 |
| Quotation | "ten monitoring points were installed in the lower, lower-middle, upper-middle, and upper portions of the slide mass"; "Top"; "Lower middle part"; "Upper middle part"; "Bottom" |
| Concern | Table 2 assigns IDs 1 and 2 to "bottom" (z = 340 and 355), IDs 3 to 5 to "lower middle part" (465 to 498), IDs 6 to 8 to "upper middle part" (660 to 692) and IDs 9 and 10 to "top" (752 and 755). Fig6 (600 dpi, AB; 400 dpi, S3) divides the sliding mass into four bands with 2, 3, 3 and 2 spheres from the upslope end (2 + 3 + 3 + 2 = 10, as in Table 2) and labels them, from upslope to downslope, "Top", "Lower middle part", "Upper middle part", "Bottom"; the band next to "Top" must be the upper middle part, so the two middle labels are swapped. The spheres carry no numbers and no legend, so they cannot be matched to IDs 1 to 10, to the panels of Fig9 or to the trajectories of Fig10 (a); measured sphere colours include yellow (#f8f90b), orange (#f3b404) and pink (#f9a2b8), which do not occur among the legend lines of Fig10 (a), and the red sphere lies in the top band whereas red is ID 1 (bottom) in Fig10 (a). The axes of Fig6 have numbers but no titles or units, and the sliding mass is dark green, the colour of γo2 in Fig4. The same groups are called "lower, lower-middle, upper-middle, and upper" in l. 256 to 257, "bottom" and "top" in Table 2, "lower" and "upper rock mass" in the abstract (l. 29) and "front" and "rear portion" in Conclusion 4 (l. 484 to 487); the pairs agree in sense with the elevations but are not linked to the Table 2 names. |
| Suggestion | Swap the labels "Lower middle part" and "Upper middle part" in Fig6 (p. 14), number the spheres 1 to 10 with the colours of Fig10 (a), add x (m), y (m), z (m) to the axes, and use the position names of Table 2 in p. 13, l. 256 to 257, p. 1, l. 29 and p. 26, l. 483 to 487, or state once at l. 256 that "lower" corresponds to "front" and "upper" to "rear". |
| Status | verified (labels, bands, point counts and colours at the page images p. 13, 14 and 23) |
| Severity | minor |
| Source | S2, S3, AB |

**GB-35 The alpha-shape procedure is not reproducible, and the reference values V0 and S0 of VS and AG are neither reported nor defined consistently, so the thresholds 29.47 % and 319.5 % cannot be checked.**

| Field | Content |
|---|---|
| Check | P8, P21, P22 |
| Location | p. 14, l. 272 to 284; p. 24, l. 440 to 441; p. 24, l. 452 to p. 25, l. 455; p. 23, l. 426 to 428; p. 25, Fig12 |
| Quotation | "An alpha-shape algorithm is applied to the slide mass to generate an enclosing envelope"; "In these expressions, V0 denotes the initial volume of the landslide mass (m³); Vt denotes the volume of the enclosing envelope at time t (m³)"; "this study uniformly sets the α value to 1." |
| Concern | Not stated are the point set (block vertices, centroids or zone nodes), the unit and definition of α (a radius of 1 m against blocks of 8.7 m, or a normalised value), and the software. The section title and l. 270 to 272 speak of the deposition zone, l. 272 to 273 of the whole slide mass. Vt and St are envelope values, while V0 and S0 are defined as values of "the landslide mass" (l. 278 to 279); if V0 were the solid block volume (for example 317,563 m³), VS would mix the initial difference between envelope and solid volume with the swelling, yet Fig12 starts at VS = 0 and AG = 0, which holds only if V0 and S0 are the envelope values at t = 0. No envelope volume or area is given for any of the 10 time points, so 29.47 % (Vt / V0 = 1.2947) and 319.5 % (St / S0 = 4.195) cannot be recomputed, nor the time of the transition. The number of time points behind Fig12 is treated in GB-46. |
| Suggestion | In Section 2.4 (p. 14, l. 272 to 284), state point set, α with unit, software and the definitions of V0 and S0 (envelope at t = 0 if so) with their values; in Section 3.4, add a table of t, V, S, VS and AG for the time points used, and state the time at which VS = 29.47 % and AG = 319.5 % are reached. |
| Status | verified (missing specification and values, page images p. 14, 23, 24, 25); inferred (interpretation of V0 and the ratios, Python) |
| Severity | moderate |
| Source | SD, S3 |

**GB-36 The indices VS and AG are introduced under two names each, and the surface area is denoted S in Eq. (6) but A in p. 24, l. 440.**

| Field | Content |
|---|---|
| Check | P38 |
| Location | p. 14, l. 274 to 280; p. 24, l. 440 to 441; p. 25, l. 453 to 454; p. 26, l. 488; p. 1, l. 25; p. 3, l. 89; p. 25, Fig12 (axis titles); p. 4, Fig1 |
| Quotation | "two dimensionless indices are introduced: volume swelling (VS) and area growth (AG)"; "we first extracted its volume (V) and surface area (A) at each time point, based on which the volume expansion rate (VS) and surface area growth rate (AG) were calculated" |
| Concern | The definitions in Section 2.4, the axis titles of Fig12 ("Volume Swelling (%)", "Area Growth (%)") and the labels of Fig1 agree. Elsewhere the same quantities are "volume expansion rate" and "area growth rate" (l. 25), "surface area growth rate" (l. 89, l. 441) or "surface area growth" (l. 453, l. 488); l. 441 defines VS and AG a second time with the other names. Counts in text.json, whole manuscript: "volume swelling" 2 hits (l. 275; l. 287 to 288), "volume expansion" 5 hits (l. 25, 89, 441, 453, 488), "area growth" 7 hits, of which "surface area growth" 4. A "rate" suggests a quantity per unit time, while Eq. (5) and (6) define relative changes in percent. Eq. (6) and l. 278 to 280 use S0 and St, l. 440 uses A. GB-35 concerns the reproducibility of the same indices; this finding only their names and symbols. |
| Suggestion | Use "volume swelling (VS)" and "area growth (AG)" as defined at p. 14, l. 275 in p. 1, l. 25, p. 3, l. 89, p. 24, l. 440 to 441, p. 25, l. 453 to 454 and p. 26, l. 488, drop the second definition at l. 441, and replace "surface area (A)" at l. 440 by "surface area (S)". |
| Status | verified (all hits at the page images p. 1, 3, 4, 14, 24, 25, 26) |
| Severity | minor |
| Source | S2, S3 |

#### Minor corrections

| ID | Location | Quotation | Replacement | Source |
|---|---|---|---|---|
| KK-13 | p. 4, Fig1, panel "Global Perspective" | "P0E", "PtE", "KtE" | "PE(t0)", "PE(ti)", "KE(ti)", matching Eq. (1) to (4) (p. 12, l. 245; p. 13, l. 246 to 249); GB-07 concerns the names of the parts in Fig1 and GB-08 its type size | S2 |
| KK-14 | p. 4, Fig1, lower left box | "Extraction of volume and area of landslide accumulation area" | same wording in a box widened so that the text no longer touches the frame (checked at 600 dpi by AB); GB-07 concerns the name of this part, GB-08 the type size, KK-13 the symbols of another panel | AB |
| KK-15 | p. 6, Fig2 (b) legend; p. 8, Fig3 (a) legend; p. 8, Fig3 (b) legend | "Daduhe River"; "Dadu river" | "Dadu River" in all three legends, as in the text (11 lines with "Dadu River", text.json p. 5 to 16) and in the legend of Fig2 (c); GB-09, GB-10, GB-15 and GB-18 concern other content of Fig2 and Fig3 | S2, AB |
| KK-16 | p. 9, l. 182 | "1121m high" | "1121 m high"; GB-16 concerns the volume stated in the same sentence | ZF |
| KK-17 | p. 12, Fig5 (a) legend | "Non-obvios acceleration" | "Non-obvious acceleration"; GB-26, GB-27, GB-28, GB-29 and GB-30 concern content and form of Fig5 | AB |
| KK-18 | p. 13, l. 246 | "where, at time ti, PE(ti), and DE(ti) can be expressed as:" | "where, at time ti, KE(ti), PE(ti) and DE(ti) can be expressed as:" (Eq. 2 in the next line defines KE); confirmed at the page image p. 13, where Eq. (2) to (4) are l. 247 to 249 | ZF |
| KK-19 | p. 13, l. 251 | "(m/s);h(ti)" | "(m/s); h(ti)" | ZF |
| KK-20 | p. 13, Table 2, title and row ID 11 | "Table 2: The basic information of blocks where the 10 monitoring points are located" | "Table 2: Basic information of the 10 monitored blocks (IDs 1 to 10) and of the global monitoring item (ID 11)", because row 11 (maximum unbalanced force) is not a block; GB-16, GB-31, GB-32 and GB-42 use other columns or rows of Table 2 | S2 |

#### Verification log

| ID | Check | Checked | Values | Result |
|---|---|---|---|---|
| PP-09 | P12 | Every data source of the methods (p. 2 to 15) against the code statement (p. 26, l. 494 to 495), the data statement (l. 505 to 506) and appendices (S2) | (1) UAV DEM, (2) restored terrain, (3) laboratory tests, (4) 3DEC model and histories, (5) scripts, (6) field investigation and photos: covered generically, on request, no reason; (7) Luding record, (8) image Fig2 (b), (9) map Fig2 (c), (10) base map Fig2 (a): no provenance; (11) Tiezhuang Temple tablet: no citation; appendices: none; personal data: none | findings GB-49 (sources 1 to 6), GB-22 (7 to 10), GB-11 (11); disclosed limits (no 1786 record, l. 183 to 186; no structural plane data, l. 176 to 178) are reasons for modelling choices, not for withholding data |
| PP-10 | P12 | Links in the statements and their reachability (S2) | code and data statements contain 0 URLs, 0 DOIs, 0 repository names; the DOIs on p. 26 to 29 belong to cited literature | no finding beyond GB-49; reachability not applicable |
| PP-11 | P38 | Identifiers occurring in several places, counted in text.json and compared at the page images (S2) | "3DEC" 2 hits, same form; "Caihong bridge" l. 93 and Fig2 (c); "Huashibao" l. 342 and Fig2 (c); monitoring IDs 1 to 10 in Table 2, Fig9 caption, Fig10 (a) legend; time points of Fig7 (0, 3, 7, 9, 12, 15, 131 s) and Fig11 (0, 3, 7, 9, 12, 15, 32, 71, 100, 131 s) identical where shared; α = 1 in l. 283 and Fig1; KE, PE, DE, ME defined l. 241 to 243 and used consistently; "Kangding earthquake" (l. 110, 183, 188) against "1786 Moxi M 7.75 earthquake" in the title of Zhao et al. (2021) | no finding; the earthquake name in Zhao et al. is the naming of a cited source; "Luding" names a county (l. 94, 96) and a station (l. 190), two objects |
| PP-12 | P29, P3 | Inventory of all figures (AB) | Fig1 p. 4 flow chart; Fig2 p. 6 maps and image (a to c); Fig3 p. 8 to 9 block view, profile, contour maps (a to c); Fig4 p. 10 model with inset; Fig5 p. 12 six line plots; Fig6 p. 14 model with points; Fig7 p. 17 to 19 velocity, stress, photo comparison (a to o); Fig8 p. 20 stacked bars; Fig9 p. 21 to 22 ten stacked-bar plots; Fig10 p. 23 3D lines and scatter with fit; Fig11 p. 23 to 24 ten surfaces; Fig12 p. 25 two line plots; all 12 raster JPEG; no graphical abstract, no appendix figures | no finding (inventory) |
| PP-13 | P3, P4 | Numbering of figures, tables, equations and sections and their in-text references (AB, S4) | Fig1 to Fig12 in order of first reference, each referenced in its section; Tables 1 and 2 referenced at l. 212 and l. 259; Eq. (1) to (6) without gap, none referenced by number; panel letters against captions for Fig5, Fig7, Fig9, Fig10; every reference hits matching content except "Fig3. (c)" in l. 160 | no finding beyond GB-18, GB-07, KK-25, KK-26, KK-27 |
| PP-14 | P3 | Dimension labels in Fig4 against the text (AB) | labels "1021m", "747m", "179m", "131m" against p. 9, l. 174 to 175: 1021 m, 747 m, 179 m, 131 m | no finding |
| PP-15 | P3 | Section a-a' in Fig2 (c) against Fig3 (b) and the sliding direction (AB) | a-a' measured 688 px x 2.194 m per px = 1509 m against the 0 to 1500 m axis of Fig3 (b); azimuth 73.6 degrees against "main sliding direction of 75°" (l. 148 to 149) | no finding |
| PP-16 | P3 | Regularity of scale bars (AB) | Fig2 (b): segments 36, 37, 36 px; Fig2 (c): 90.5, 93, 90 px; Fig3 (c): 89, 88.5 and 134 px (expected 133) | no finding |
| PP-17 | P29 | Type sizes at or above 6 pt (AB, 600 dpi) | Fig1 "Travel distance" 6.67 pt; Fig2 (c) legend 6.08 pt; Fig2 (a) scale bar 5.67 pt (within the 0.6 pt uncertainty of 6 pt); Fig3 (a) scale bar 6.83 pt; Fig3 (c) scale bar 7.00 pt; Fig4 x axis 6.50 pt, inset y axis 6.33 pt; Fig6 z axis 6.92 pt; Fig8 y axis 7.83 pt | no finding for these; sizes below 6 pt in GB-08 |
| PP-18 | P3 | Fig5 (a) marker counts and legend (AB) | 6 red and 5 purple markers (600 dpi); legend with two entries, red and purple | no finding for the count; positions in GB-27 |
| PP-19 | P3 | Count of monitoring points in Fig6 against Table 2 (AB, S3) | 10 spheres; per band from the back 2, 3, 3, 2; Table 2: top 2 (IDs 9, 10), upper middle 3, lower middle 3, bottom 2; 2 + 3 + 3 + 2 = 10 | no finding for the count; labels in GB-34 |
| PP-20 | P7 | Method versions over the data (SD) | one run, one model, one parameter set; no version or protocol change stated | no finding beyond GB-29 and GB-46 |
| PP-21 | P17 | Place of disclosure of the 8 disclosed limits (SD) | all 8 stand where the affected method or stage is introduced (list in PP-07) | no finding on place; unfinished consequences in GB-21, GB-20, GB-26, GB-45 |
| PP-22 | P25 | Information available at each step (SD) | restoration uses the present DEM only (available); input motion from another event (available, disclosed); block breakage (not described); field findings for the failure sequence (not described) | no further finding beyond GB-45 and GB-33 |
| PP-23 | P26 | Guarantees and their paths (SD) | static equilibrium before dynamic loading (p. 10, l. 199 to 200): one run, no other path; "ensures a tight fit" (p. 14, l. 283 to 284) and "ensures that the simulation outcomes align" (p. 25, l. 471 to 472) | no further finding beyond GB-45, GB-38; the zero stress field of Fig7 (h) is in GB-39 |
| PP-24 | P5 | Own rules against own examples (SD) | 4 position groups (p. 13, l. 256 to 257) against Table 2: bottom IDs 1, 2; lower middle 3, 4, 5; upper middle 6, 7, 8; top 9, 10; z rising by group (340 to 355, 465 to 498, 660 to 692, 752 to 755); block footprint against Table 2 volumes; PE datum rule against Fig9; 30 % threshold applied in Fig5 (d), red markers present | consistent for the groups; deviations in GB-16 and GB-31 |
| PP-25 | P27 | Flow of unchecked components into results (SD) | unchecked: restored terrain, substitute input motion, parameters, collision threshold, selection of monitoring blocks, α; they flow into model mass and energies, all dynamic results, Fig10 (b) and Conclusion 4, Conclusion 5 | findings GB-13, GB-16, GB-21, GB-26, GB-42, GB-45 |
| PP-26 | P31 | Intent against measured effect per component (SD) | 8 components: 6 with intent only (restoration, input motion, collision detection, monitoring blocks, unbalanced force, alpha-shape fit), 1 qualitative (validation), 1 not stated (parameter inversion) | findings GB-13, GB-21, GB-26, GB-42, GB-32, GB-45, GB-38, GB-24 |
| PP-27 | P32 | Error rates without independent sample (SD) | "deemed acceptable" (p. 11, l. 232 to 233) is the only quality statement for a detection step; no independent sample anywhere | raised in GB-26 |

### Segment 3: Results (p. 15 to 25)

#### Substantive findings

**GB-37 The stages of the failure are given only through snapshot times, Section 3.2.1 divides the same period differently, and the kinetic-energy peak and drop in Fig8 come later than the times stated.**

| Field | Content |
|---|---|
| Check | P2, P22, P24 |
| Location | p. 15, l. 306 to p. 16, l. 347; p. 19, l. 368 to 370; p. 19, l. 378 to 384; p. 20, Fig8; p. 26, l. 483 to 484 |
| Quotation | "From 3 to 12 seconds, the landslide experienced rapid initiation, and the entire sliding mass abruptly descended along the sliding plane."; "Around 13 seconds, the sliding mass impacted the riverbed, causing a sharp drop in kinetic energy" |
| Concern | Section 3.1 names six stages but gives no time for any of them; the reader has to combine the panel letters with the times in the Fig7 caption (b = 3 s, c = 7 s, d = 9 s, e = 12 s, f = 15 s, g = 131 s). Section 3.2.1 calls the whole interval from 3 to 12 s "rapid initiation", which in Section 3.1 spans three stages (high-speed initiation at 7 s, collapse at 9 s, impact at base at 12 s). Conclusion 4 refers to "the collapse stage" for a collision result, but no collision result in Section 3 is tied to a stage or time. In Fig8 (AB, time axis 6.89 px per s, bars about every 1.24 s), KE per bar is 1082 GJ at 11.1 s, 1570 at 12.4 s, 1657 at 13.6 s, 804 at 14.9 s and 469 at 16.1 s (plus or minus 19 GJ), so the peak lies at 13.6 s, after the window of 3 to 12 s, and the sharp drop falls between 13.6 s and 14.9 s rather than "around 13 seconds"; Fig7 (e) at 12 s is described as the moment the "entire landslide mass collided with the ground" (p. 16, l. 331). The deviation is about 1 to 2 s. GB-32 concerns the unreported stress and stability results of the same section; the same passage of Section 3.1 is also used in GB-11 (unsourced mechanisms), GB-20 (structural planes), GB-21 (seismic narrative), GB-16 and GB-29 (the 31.6 m/s of p. 16, l. 330); this finding concerns only the time structure. |
| Suggestion | Add to Section 3.1 one sentence or a small table giving each stage with its time interval, give the time of the KE peak and of the drop as read from the data (about 13.6 s and 13.6 to 14.9 s) in p. 19, l. 381 to 384, and use the same stage names and intervals in Section 3.2.1 and Conclusion 4. |
| Status | verified (text at the page images p. 15, 16, 19, 26; KE values measured by AB) |
| Severity | minor |
| Source | S3, AB |

**GB-38 The validation of the simulation is qualitative, two features judged by eye, but is presented as ensuring agreement with reality, although the UAV DEM would allow a quantitative check.**

| Field | Content |
|---|---|
| Check | P15, P31, P26 |
| Location | p. 16, l. 353 to 359; p. 19, Fig7 (o); p. 25, l. 469 to 475; p. 15, l. 299; p. 11, l. 229 to 233 |
| Quotation | "presents compelling evidence of agreement between the numerical simulation results and the actual field observations"; "Comparison with field imagery and result analysis ensures that the simulation outcomes align with actual conditions." |
| Concern | The manuscript discloses that weathering has altered the topography since 1786 (l. 354 to 355), and Fig7 (o) sets simulation and photographs side by side. The comparison it shows consists of two boxes ("Protrusion at the source area", "Landslide deposit area") without any measured quantity, while the text speaks of "compelling evidence" (l. 353) and says that extent and morphology "closely match" (l. 357 to 358). No runout length, deposit outline, thickness or dam height is compared with field values, and it is not stated whether the compared features were used for the parameter inversion (GB-24). The verb "ensures" in Conclusion 2 (l. 471 to 472) is therefore stronger than the evidence, which supports "is consistent with", and the claim that the simulation "successfully reproduced the entire process" (p. 15, l. 299) depends on this validation; graded major for that reason. Conclusion 2 also says that collisions "can be identified" (l. 473 to 475) although the threshold was set by visual judgement (GB-26; the curve and count behind the threshold are in GB-29, the name of the abscissa in GB-28). GB-32 concerns other missing results of Section 3.1. |
| Suggestion | In Section 3.1 after p. 16, l. 359, compare the simulated final deposit with the present deposit from the UAV DEM quantitatively (outline overlap, runout length, thickness map, dam crest height) and give the deviation; state which observations were used for calibration and which only for validation; in p. 16, l. 353 to 354 and p. 25, l. 471 to 475 replace "compelling evidence" and "ensures" by wording that matches the comparison. |
| Status | verified (wording; content of Fig7 (o) at the page image p. 19) |
| Severity | major |
| Source | SD, S4 |

**GB-39 Fig7 (h) shows zero stress throughout the model at t = 0 s, although the dynamic run starts from static equilibrium, while the later panels show stresses of lithostatic size.**

| Field | Content |
|---|---|
| Check | P3 |
| Location | p. 18, Fig7 (h) and (i) to (n); p. 10, l. 199 to 202; p. 15, l. 304 to 305 |
| Quotation | "Dynamic loading must be introduced only after the model has attained static equilibrium; i.e., the dynamic analysis is predicated on a prior static analysis that has reached convergence." |
| Concern | The body of Fig7 (h) is uniform red #ec0404 (91.9 % of the pixels in the measured area, AB), the colour of the "0" end of its colour bar, whose other end is also labelled "0Mpa". Panel (i) at 3 s already spans 0 to -33 MPa with stresses increasing with depth. A lithostatic estimate with the bed-rock density of Table 1 and about 1250 m of rock above the base gives 2700 x 9.81 x 1250 Pa = 33.1 MPa (Python), the size of the colour-bar limits in (i) to (m). If the model was in static equilibrium at t = 0 s, (h) should already show this gravitational stress field; a uniform 0 suggests a state before gravity loading or a stress change relative to the start. GB-12 concerns the unstated settings of the static and dynamic phases; GB-38 and GB-32 concern other content of Fig7. |
| Suggestion | Explain what Fig7 (h) shows (total stress after the static stage or stress change); if it is total stress, replace (h) by the equilibrium stress field, and state the same for (i) to (n) in the caption (p. 19, l. 368 to 370). |
| Status | verified (colours measured by AB); inferred (interpretation), put as a question |
| Severity | moderate |
| Source | AB |

**GB-40 The stress panels of Fig7 have no axis titles, no section location and no stress component, use changing colour ranges, and panel (o) lacks scale, orientation and time.**

| Field | Content |
|---|---|
| Check | P29 |
| Location | p. 18, Fig7 (h) to (n); p. 19, Fig7 (o); caption, p. 19, l. 368 to 370 |
| Quotation | "(h-n) cloud map of stress when t = 0s, 3s, 7s, 9s, 12s, 15s, 131s; (o) Validation of numerical simulation results against real-world evidence." |
| Concern | Panels (h) to (n) have numbers but no axis titles and units, whereas (a) to (g) carry x (m), y (m), z (m). The text calls them "stress distribution along the sliding plane" (p. 15, l. 302), but they show a vertical section whose position and stress component (Table 2 monitors Stress-XX, -YY, -ZZ) are not stated. The colour bars end at 0, -33, -31, -33, -33, -33 and -47 MPa, so equal colours mean different stresses in (j) and (n). Panel (o) compares a simulated view with two photographs without scale, north arrow, view direction, simulation time or photo date. GB-39 concerns the zero field of (h), GB-38 the content of the validation in (o), GB-37 the stage times of the same caption; this finding concerns labelling. |
| Suggestion | Add axis titles with units to Fig7 (h) to (n), state section location and stress component in the caption, use one colour range for all stress panels, and give time, scale and view direction for (o). |
| Status | verified |
| Severity | minor |
| Source | AB |

**GB-41 The energy balance cannot fail by construction: with Eq. (4), KE + PE + DE equals ME(t0) at every time for the whole mass and for every block, so it shows neither that the whole mass conserves energy nor that single blocks do not.**

| Field | Content |
|---|---|
| Check | P23, P15, P31, P3, P6 |
| Location | p. 19, l. 375 to 377; p. 19, l. 387 to 389; p. 13, l. 249; p. 12, l. 245; p. 20, l. 393 to 396; p. 20, l. 399 to 402; p. 20, Fig8; p. 21, Fig9 (a) to (j); p. 1, l. 26 to 28; p. 25, l. 476 to p. 26, l. 482 |
| Quotation | "It is evident that, due to the law of energy conservation, the total sum of the three forms of energy remains constant throughout the landslide."; "This can be regarded as a successful energy extraction numerical simulation."; "unlike the total landslide mass, the energy of single blocks is not conserved."; "for the whole landslide, its energy change conforms to the law of conservation of energy" |
| Concern | The energy bookkeeping is laid out explicitly in Eq. (1) to (4). With ME = KE + PE (Eq. 1, p. 12, l. 245) and DE(ti) = ME(t0) minus ME(ti) (Eq. 4, p. 13, l. 249), KE + PE + DE = ME(t0) for any values of KE and PE; a check over 10,000 random states gives a maximum relative deviation of 1.8 x 10^-13 (Python, rounding only). The figures show exactly this: in Fig8 the top of all 95 bars lies at 6473 to 6521 GJ (the two lowest are the first two bars, all others 6521 plus or minus 10 GJ), and in every panel of Fig9 at least 101 of 104 to 106 bars end on the same pixel row (AB, measured). The constant total therefore confirms the arithmetic, not conservation, and cannot support "successful" (l. 388 to 389); and since Fig9 also has a constant total, the contrast of the abstract (l. 26 to 28), Section 3.2.2 (l. 393 to 394) and Conclusion 3 (l. 476 to 482) cannot rest on the sum. What distinguishes single blocks is that DE decreases at times (l. 399 to 402), which the manuscript attributes partly to "the calculation method used" (l. 400). Two resolutions, put as questions: A, "conserved" means that DE never decreases, which Conclusion 3 suggests ("dissipated energy continuously increases"); then the criterion is the monotonicity of a residual. B, DE is computed independently of Eq. 4, for example from frictional and damping work in 3DEC; then the balance would be a real test, but no such computation is described. In both cases the system is not closed: seismic waves enter at the viscous base (p. 10, l. 197 to 199) and the mass exchanges work with the base blocks, so DE as residual contains frictional dissipation, damping, strain energy, the work of the seismic input and work exchanged with the bed, and a decrease of DE can come from collisions, seismic input or base work, while the manuscript names only collisions (l. 394 to 396). Graded major because the first result of the abstract and Conclusion 3 depend on it. GB-37 concerns the timing of KE in Fig8, GB-31 the PE datum and GB-16 the magnitudes of the same figures. |
| Suggestion | In Section 2.3, call DE the residual it is and compute the energy terms independently (work of the seismic input at the base, frictional and damping dissipation over contacts and zones, strain energy), then check their balance against PE and KE; replace "conforms to the law of conservation of energy" in p. 1, l. 26 to 28, p. 19, l. 375 to 377 and p. 25, l. 477 to 479 by the result of that balance or by the actual criterion (monotonic DE), remove p. 19, l. 388 to 389, and attribute DE decreases of single blocks only after separating contact, seismic and base work. |
| Status | verified (identity from Eq. 1 and 4, Python; constant totals measured on the page images p. 20 to 22 by AB and S4); inferred (content of the residual, from Eq. 4 and l. 197 to 199); assumption (resolutions A and B), put as a question |
| Severity | major |
| Source | S3, S4, AB, SD |

**GB-42 The comparison of lower and upper, or front and rear, rock mass in the abstract and Conclusion 4 has no counted basis: there are no collision counts per block or position, Fig10 (b) bins collisions by travel distance, and absolute counts are not normalised.**

| Field | Content |
|---|---|
| Check | P11, P15, P20, P21, P3, P34 |
| Location | p. 22, l. 414 to 421; p. 23, Fig10 (b); p. 1, l. 28 to 30; p. 3, l. 86 to 87; p. 13, l. 256 to 263; p. 13, Table 2; p. 26, l. 483 to 487; p. 11, l. 233 to 234 |
| Quotation | "Compared with the upper rock mass, the lower rock mass is compressed more frequently, receives more energy transfer, and has a longer migration distance."; "Fig10. (b) presents the frequency of effective collisions experienced by blocks at different locations during the landslide process."; "it is clear that as the migration distance increases during the landslide, the number of collisions also rises continuously"; "during the collapse stage, the front portion of the rock mass experiences more collisions than the rear portion, with a clear trend of decreasing collision frequency toward the rear." |
| Concern | (a) Missing results: the methods announce an analysis of collision frequency per part of the mass (p. 3, l. 86 to 87), and Table 2 assigns the ten blocks to four positions; a search in Section 3 (l. 297 to 459) for "lower", "upper", "front", "rear", "bottom", "top", "position", "collision", "migration" and "collapse stage" finds positions only in the stage descriptions (l. 316, 320, 322, 324 to 327, 340, 385) and collisions only in l. 401, 404, 415, 418 to 419, 423, 446, 447 and 455; none states a count or an energy transfer per block or position, and none says that the lower blocks travel farther. Stress histories were recorded but not reported (GB-32), so "compressed more frequently" has no measurement, and energy transfer between blocks is not measured (GB-41). (b) Fig10 (b) (AB at 600 dpi): 26 points at 0, 100, ..., 2500 m with values 0, 0, 2, 4.5, 5.7, 7.5, 15.0, 15.9, 6.9, 27.0, 19.9, 23.9, 29.9, 27.1, 36.9, 42.0, 48.9, 49.7, 53.0, 61.0, 69.0, 72.0, 142.0, 157.0, 150.0 and 146.0; the points are distance classes, not the ten blocks or positions, so the figure cannot show "blocks at different locations" (l. 415); five decreases between neighbouring classes exceed the uncertainty (700 to 800 m, 900 to 1000 m, 1200 to 1300 m, 2300 to 2400 m, 2400 to 2500 m), against "rises continuously" (l. 419); the sum is 1212.8, 74 more than the 1,139 of p. 11, l. 233 (GB-29); the y axis reads only "Frequency" without unit, and the red curve has no legend, equation or fit statistic. (c) Normalisation: a block that travels farther passes more opportunities for collision, so an absolute count rises with travel distance even at a constant rate per metre; 49.1 % of the counted collisions fall in the classes from 2200 m (595 of 1212.8, Python). "Compressed more frequently" and "longer migration distance" can therefore be one effect counted twice, and the reverse causal direction of Conclusion 4 ("enabling the front portion to slide farther") is not separated. "Receives more energy transfer" is not normalised by mass, although the block volumes of Table 2 differ by a factor 2.32 and the group means are 980.8, 1092.1, 1483.4 and 912.3 m³ (bottom to top). The ten blocks are 0.04 % of the 25,345 model blocks and hold 11,512.7 m³, 3.6 % of the modelled volume (Python); their representativeness is asserted (l. 257), not shown. (d) The positional terms change between Table 2, l. 256, the abstract and Conclusion 4 (GB-34). GB-26 concerns whether the counted events are collisions; this finding concerns what the counts show, and GB-28 the name of the abscissa. The literature on the rear-to-front mechanism is in GB-06. |
| Suggestion | In Section 3.2.2 after p. 22, l. 421, add a table with, for each monitored block and each position group of Table 2, the travel distance, the number of effective collisions, the number per 100 m of travel and per second, and the energy received per unit mass, separated by stage; define what Fig10 (b) counts (all blocks or the ten monitored blocks, threshold, class width 100 m), reconcile its total with 1,139, give the fitted function or remove the curve, replace "rises continuously" by the measured trend, and restate the abstract (p. 1, l. 28 to 30) and Conclusion 4 (p. 26, l. 483 to 487) in the unit actually measured, or remove them. |
| Status | verified (missing counts, unit change and undefined axis, text search and page images p. 13, 22, 23; Fig10 (b) values measured by AB); inferred (sums, shares, ratios, Python; exposure effect and reverse direction); assumption (whether normalisation changes the result), put as a question |
| Severity | major |
| Source | S3, S4, SD, AB |

**GB-43 Fig10 (a) is an oblique 3D view with unreadable axis numbers, from which neither the fall height nor the rebound of blocks 1 and 3 can be read, and its vertical extent seems to exceed the fall heights implied by Fig9.**

| Field | Content |
|---|---|
| Check | P29, P3 |
| Location | p. 23, Fig10 (a); p. 22, l. 414 to 417 |
| Quotation | "It can be observed that Blocks 1 and 3 exhibit bouncing rebounds, confirming the previous inference." |
| Concern | All ten trajectories start at one point, so they show displacements, not positions; the caption does not say so. The view is oblique, so screen height mixes Z with X and Y. Z axis numbers measure 4.0 to 4.3 pt, X and Y numbers are smaller (GB-08). By line colour (AB, 600 dpi), trajectory 5 ends below the label -840, trajectory 1 at -840 and trajectory 2 at -630 (screen heights), while the Fig9 PE totals imply fall heights of 238.8 m (block 1), 222.8 m (block 2) and 316.7 m (block 5), and Table 2 gives initial z = 340 to 498 m for these blocks; a Z drop of 600 to 900 m would place them below the model base. The rebound claimed in l. 416 cannot be seen as a rise in Z in this projection. GB-42 concerns panel (b) and GB-26 the collision detection referred to in the same paragraph; colours against Fig6 are in GB-34. |
| Suggestion | Replace Fig10 (a) (p. 23) by a plan view (X, Y) and a profile (travel distance, Z) of the ten trajectories with numbered start points, or at least state that displacements are plotted and give the Z drop per block; enlarge the axis numbers. |
| Status | verified (projection, start point, type size); inferred (the conflict in Z), put as a question |
| Severity | moderate |
| Source | AB |

**GB-44 Fig11 does not say which rendering is the envelope and which the simulated mass, and its axis ranges change from panel to panel.**

| Field | Content |
|---|---|
| Check | P29 |
| Location | p. 23, Fig11 (a) to (j); caption, p. 24, l. 437 to 439 |
| Quotation | "Fig11. Comparison of the overall envelope fitting of the landslide at 10 different times and the shape of the landslide mass in numerical simulation" |
| Concern | Each panel shows a large light-green triangulated surface and a dark-green inset; the caption does not say which is the alpha-shape envelope and which the block assembly. Axis ranges differ between panels (Z from -300 to 300 in (a) and from -600 to 400 in (i); X up to 200 in (a) and up to 1500 in (i)), and at 2.2 to 2.5 pt (GB-08) they cannot be read. The envelope volumes and areas at the ten times are given nowhere (GB-35). |
| Suggestion | State in the caption (p. 24, l. 437 to 439) that the light-green surface is the envelope (α = 1) and the inset the simulated mass, and use one axis range for all panels. |
| Status | verified |
| Severity | minor |
| Source | AB |

**GB-45 The growth of envelope volume and area is read as fragmentation, but fragmentation is not measured, fragments filling the interior cannot enlarge an envelope, and the threshold for the transition "from a solid phase to a fluidized phase" is set at the KE peak it is then used to explain.**

| Field | Content |
|---|---|
| Check | P15, P31, P9, P25, P26 |
| Location | p. 24, l. 445 to 452; p. 24, l. 452 to p. 25, l. 456; p. 26, l. 488 to 492; p. 9, l. 178 to 181; p. 14, l. 283 to 284; p. 25, Fig12 |
| Quotation | "These newly generated fragments fill the interior and surface of the deposit mass, causing a sudden expansion of the envelope volume and a sharp increase in surface area."; "These newly formed fragments fill the interior and surface of the deposit mass, resulting in a sudden expansion of the overall envelope volume and a sharp increase in surface area."; "it can be considered that the landslide transitions from a solid phase to a fluidized phase" |
| Concern | The alpha-shape indices are a quantitative measure of dispersal. (1) The mechanism is introduced as an interpretation ("This phenomenon can be interpreted as follows", l. 445) and supported only by "the sharp rise of DE" (l. 451), while DE by Eq. 4 is the residual of all mechanical energy changes, not a measure of fragmentation (GB-41). (2) No count of blocks or fragments over time is reported; the model consists of blocks of 8.7 m x 8.7 m (l. 178), and no breakage mechanism is described (search in Section 2, l. 74 to 296: "fragment" 2 hits, l. 285 and l. 294, both naming fragmentation as a topic; "break" 2 hits, l. 118 and l. 137, both dam break; "fractur" 0). Whether blocks can split, and to what size, is put as a question; if not, "newly generated fragments" (l. 448, l. 490) and "fine debris" (p. 16, l. 326) cannot form in the model. (3) Fragments that fill the interior of a deposit do not enlarge its enclosing envelope; spreading does. Fig12 ends at VS of about 1243 % and AG of about 4250 % (4246 % and 4272 % in two measurements by S4 and AB), an envelope about 13 times the initial volume, mostly void, which spreading over the valley explains without fragmentation; VS and AG cannot separate the two causes. (4) 29.47 % and 319.5 % are the VS and AG values at the KE peak marked in Fig12; using them to define the transition and then citing the KE peak as evidence (l. 454 to 455) is circular, and no independent criterion of fluidisation is given. (5) The "tight fit" of α = 1 (l. 283 to 284) is not measured at any time point. (6) L. 451 to 452 speak of fragmentation "in the monitored block group", while Fig12 shows the whole sliding mass (caption, l. 458). Graded major because Conclusion 5 (l. 488 to 492) answers the structural part of the title and of the aim in p. 2, l. 69. GB-35 concerns the definition of the indices and GB-36 their names; GB-46 the time points and the KE value at the marked peak; GB-20 and GB-16 concern other statements of p. 9, l. 175 to 182. |
| Suggestion | In Sections 2.4 and 3.4, state whether and how blocks can break in the model; measure fragmentation directly (number and size distribution of blocks or separated clusters over time) and dispersion separately (spread of block centroids, deposit footprint, solid volume over envelope volume per time point); define the fluidisation criterion independently of KE or remove p. 24, l. 452 to p. 25, l. 455; reword Conclusion 5 (p. 26, l. 488 to 492) as an interpretation unless such data are added, and delete "fill the interior" as a cause of envelope expansion. |
| Status | verified (wording, absence of fragment counts; end values of VS and AG measured by S4 and AB); inferred (spreading as alternative cause, void share, circularity); assumption (absence of a breakage mechanism), put as a question |
| Severity | major |
| Source | S4, SD |

**GB-46 Fig12 contains about 30 time steps whose times are not given, although the envelope was fitted at 10 time points, and its kinetic-energy peak of 1116.8 GJ differs from the 1657 GJ peak in Fig8.**

| Field | Content |
|---|---|
| Check | P3, P2, P11 |
| Location | p. 25, Fig12 (a) and (b); p. 25, l. 453 to 455; p. 23, l. 426 to 427; p. 24, l. 440 to 443; p. 20, Fig8 |
| Quotation | "to perform Alpha Shape envelope fitting on the deposit mass at 10 representative time points"; "At this point, the kinetic energy peaks" |
| Concern | VS and AG are computed from the envelope "at each time point" (p. 24, l. 440 to 441), and the fitting was done at 10 time points (p. 23, l. 427; Fig11, 0 to 131 s), so Fig12 should have 10 points per curve. Counts at enlarged page images give far more: at least 18 distinct markers on the DE curve of (a) at VS above about 270 % (S3, 800 dpi), at least 17 on DE between about 350 % and 1250 % (SD), and about 32 data points in (a) in all (AB, 600 dpi: 23 distinct markers on PE up to VS of about 640 % and 9 further on DE, at least 30). In (a) at 300 dpi (AB: 8000 GJ at 987.0 px, 0 at 1447 px), the marked KE peak (red triangle, label "1116.8") lies at VS = 29.5 % and 1130 plus or minus 17 GJ, and in (b) at AG = 320 %, matching the labels (PP-38). Fig8 shows the KE peak of the same sliding mass at 1657 to 1681 GJ at 13.6 s (GB-37, GB-16); the difference of at least 540 GJ (33 %) exceeds both uncertainties, while PE at VS = 0 (about 6534 GJ) agrees with the first bar of Fig8 (6502 GJ), so both figures share the initial state. If Fig12 samples times that miss 13.6 s, its maximum is not the KE peak, and VS and AG at the true peak are unknown. GB-35 concerns the definition and missing values of VS and AG, GB-45 the reading of the transition, GB-36 their names. |
| Suggestion | State the times of all points in Fig12 (a table of t, VS, AG, KE, PE and DE), say in p. 23, l. 427 and in the Fig12 caption at how many time steps the envelope was fitted, include the time of the KE peak of Fig8, recompute VS and AG at that time, and reconcile 1116.8 GJ with Fig8. |
| Status | verified (values and points measured or counted at the page images by AB, S3 and SD; exact count differs between instances, all above 10); inferred (sampling explanation), put as a question |
| Severity | major |
| Source | AB, S3 |

#### Minor corrections

| ID | Location | Quotation | Replacement | Source |
|---|---|---|---|---|
| KK-21 | p. 15, l. 301; p. 19, l. 368 to 369 | "cloud maps of velocity distribution"; "cloud map of velocity"; "cloud map of stress" | "contour maps of velocity distribution", "contour map of velocity", "contour map of stress"; GB-32 concerns the evaluation of these maps and GB-40 their labelling | ZF |
| KK-22 | p. 18, Fig7 (h) to (n), colour bars | "0Mpa"; "-33Mpa"; "-31Mpa"; "-47Mpa" | "MPa" in all seven labels (0, -33, -31, -33, -33, -33 and -47 MPa); GB-40 concerns the same colour bars, GB-39 and GB-38 other content of Fig7 | AB |
| KK-23 | p. 20, l. 397 to 398 | "exhibit a rebound in potential energy after it approaches zero" | "exhibit a rebound in potential energy after their potential energy approaches zero" ("it" refers to two blocks); GB-31 concerns the PE values of these blocks | ZF |
| KK-24 | p. 22, l. 410 to 413 | "energy evolution of point 1 ; (b) energy evolution of point 2 ;" | "energy evolution of point 1; (b) energy evolution of point 2;" and so on for points 3 to 8 (8 instances, page image p. 22) | AB |
| KK-25 | p. 23, l. 425 | "3.4 Structural evolution as a function of energy change" | "3.3 Structural evolution as a function of energy change" (headings of Section 3: 3.1 l. 298, 3.2 l. 371, 3.2.1 l. 372, 3.2.2 l. 391, 3.4 l. 425; no 3.3; page images p. 15, 19, 20, 23) | S3, S4, SD |
| KK-26 | p. 24, l. 438 to 439 | "(a-i) when time = 0s, 3s, 7s, 9s, 12s, 15s,32s,71s, 100s, 131s." | "(a) to (j): t = 0, 3, 7, 9, 12, 15, 32, 71, 100 and 131 s." (ten panels a to j on p. 23 and 24; a to i are nine letters); GB-44 concerns the panels themselves and GB-08 their type size | S3, S4, SD, AB |
| KK-27 | p. 25, l. 458 to 459 | "(a) as a function of volume; (b) as a function of area." | "(a) as a function of volume swelling VS; (b) as a function of area growth AG." (axis titles "Volume Swelling (%)" and "Area Growth (%)"; p. 24, l. 443: "functions of VS and AG"); GB-36 concerns the names in the text, GB-46 and GB-45 the content of Fig12 | S3, S4, AB |

#### Verification log

| ID | Check | Checked | Values | Result |
|---|---|---|---|---|
| PP-28 | P1 | Arithmetic that follows from other numbers of the manuscript (S3) | 450 m x 1000 m = 0.45 km², consistent; Fig7: 7 times for 7 velocity and 7 stress panels; Fig9: 10 panels for 10 points; Fig11: 10 times; Table 2: 10 block IDs plus ID 11; sum of the 10 block volumes 11,512.7 m³; 31.6 m/s at 12 s is the largest of 5.9, 19.6, 27.1, 31.6, 25.7 m/s | no finding beyond GB-16, GB-15, GB-41 |
| PP-29 | P2 | Quantities stated in more than one place, abstract included (S3) | year 1786 (l. 38, 110, 183, 354); magnitude "Ms7 ¾" (l. 110) and "M 7.75" (l. 601); 131 s (l. 300 to 301, Fig7 and Fig11 captions); ten monitoring points (l. 256, 262, 392, 403, Table 2, Fig6, Fig9, Fig10); 30 % threshold (l. 232, Fig5 caption); slope toe 1120 m (l. 151 to 152) against base of the reconstructed mass 179 m from the river and 131 m high (l. 174 to 175): different quantities; vertical extent 1890 - 1120 = 770 m against about 747 m (l. 174): close | no finding beyond GB-16, GB-15, GB-34, GB-37, GB-46 |
| PP-30 | P11 | Matrix of announced analyses (p. 3, l. 77 to 90; p. 13, l. 256 to 266; p. 14, l. 270 to 296) against results (l. 297 to 459) (S3) | whole mass: velocity per stage present; stress maps shown, not evaluated; energy present; field validation present; ten blocks: energy and trajectories present for all 10; collisions per block missing; stress histories missing; unbalanced force missing; envelope at 10 times present; V, S, V0, S0 missing; disclosed: dam break not modelled (l. 348 to 350), structural planes ignored (l. 175 to 178) | findings GB-32, GB-42, GB-35 |
| PP-31 | P20 | Every rate and every count of the form x of y (S3) | Fig5 thresholds 10 % to 50 % relative to the peak (l. 227 to 232); VS and AG with denominators V0 and S0 (values missing); "nearly 20 large and super large earthquake landslides" with stated area (l. 99 to 100); rates without denominator: 1,139 collisions, "Frequency" in Fig10 (b) | findings GB-29, GB-42, GB-35 |
| PP-32 | P21 | Comparisons of absolute numbers on bases of different size (S3) | Fig8 and Fig9 not compared in absolute terms; VS and AG normalised; block energies absolute while block volumes differ by a factor of 2.32 (Table 2) | finding GB-42 |
| PP-33 | P22 | Numbering gaps and counts that emerge only from two places (S3) | Fig1 to Fig12, Tables 1 and 2, Eq. (1) to (6) without gaps; section 3.3 missing; stage times only through the Fig7 caption; Blocks 1 and 3 are a bottom and a lower middle block only through Table 2 | findings GB-37, GB-29, GB-35; KK-25 |
| PP-34 | P23 | Balances (S3) | energy balance KE + PE + DE; points per zone 2 + 3 + 3 + 2 = 10 against IDs 1 to 10; 25,345 blocks cannot be split into sliding mass and base | finding GB-41; block count in GB-16 |
| PP-35 | P3 | Velocity colour-bar maxima of Fig7 (a) to (g) against the text (AB) | Fig7: 0, 5.9, 19.6, 27.1, 31.6, 25.7, 0.21 m/s; text p. 15, l. 307: 5.9; l. 315: 19.6; l. 322: 27.1; p. 16, l. 330: 31.6; l. 339: 25.7; l. 346 to 347: "approached 0 m/s" | no finding; the manuscript discloses that the dam break is not modelled (l. 348 to 350) |
| PP-36 | P24 | Times in captions and on time axes against the event times in the text (AB) | Fig7: 0, 3, 7, 9, 12, 15, 131 s; Fig11: 0, 3, 7, 9, 12, 15, 32, 71, 100, 131 s; Fig8 last bar at 130.8 s; Fig9 axes 0 to 131 s; duration 131 s (l. 300 to 301); stage order follows the panel order | no finding beyond GB-37 |
| PP-37 | P3 | PE rebound of blocks 1 and 3 in Fig9 (a), (c) against p. 20, l. 397 to 399 (AB) | Fig9 (a): 4.934 GJ at the first bar, minimum 0.041 GJ at 80.7 s, 0.373 GJ at 130.8 s; Fig9 (c): 3.963 GJ, minimum 0.035 GJ at 89.5 s, 0.341 GJ at 130.8 s | no finding; the rebound is visible in Fig9 (its datum is in GB-31) |
| PP-38 | P3 | Position of the annotated transition points in Fig12 against p. 25, l. 453 to 454 (AB) | (a): triangle at VS = 29.5 % against 29.47 %; (b): triangle at AG = 320 % against 319.5 %; KE at the triangle 1130 plus or minus 17 GJ against the label 1116.8 | no finding for the annotation; comparison with Fig8 in GB-46 |
| PP-39 | P30 | Errors and corrections against runs (SD) | no error or correction reported | no finding |
| PP-40 | P37 | Figures with corrected values (SD) | no later correction or recalculation reported; Fig3 (c) labels the restored terrain "Terrain after repair" | no finding |
| PP-41 | P33 | Effort statements (SD) | whole text.json: "effort" 1 hit (l. 59, literature), "time-consuming" 0, "computational" 0, "hours" 0 | no finding |
| PP-42 | P34 | Shown selection from counted sets (SD) | Fig9 shows all 10 monitored blocks; Fig11 all 10 time points; Fig7 7 snapshots with stated times; Fig5 (a) "typical" without rule | no finding beyond GB-26 |
| PP-43 | P36 | Approximate statements against own records (SD) | "about 450 m long", "about 100 m", "about 2400×10⁴ m³" (p. 7, l. 149 to 151) against model values (p. 9, l. 174, l. 182; Table 2) | discrepancy in GB-16 and GB-15 |
| PP-44 | P19 | Provenance of each core statement (SD) | 39 of 40 result panels model generated (97.5 %); captions of Fig7, Fig9, Fig11, Fig12 label them as simulation results | no finding on labelling; undescribed field investigations in GB-33 |
| PP-45 | P6 | Absolute statements (SD) | "remains constant" (l. 376 to 377); "ignored" (l. 177 to 178); "rises continuously" (l. 419); "entire process" (l. 299) against the disclosed dam break (l. 348 to 350); "only the Tiezhuang Temple tablet" (l. 136 to 138); "continuous increasing trend" of envelope volume and area (l. 429): VS and AG increase monotonically along the curves of Fig12 | no further finding beyond GB-41, GB-20, GB-42 |

### Segment 4: Conclusions, statements, references (p. 25 to 29)

#### Substantive findings

**GB-47 The conclusions do not return to the earthquake, to the stated aims of a general law and of early warning, or to prior work, and there is no Discussion section.**

| Field | Content |
|---|---|
| Check | P15 |
| Location | p. 25, l. 460 to 462; p. 1, l. 1 to 3; p. 2, l. 39 to 41; p. 2, l. 63 to 73; p. 5, l. 122 to 125; p. 27, l. 540 to 542; p. 28, l. 588 to 590; p. 29, l. 600 to 605 |
| Quotation | "Energy and structural evolution process of high-altitude and long-runout landslides induced by a strong earthquake"; "so as to summarize the law of high-level rock landslide induced by earthquake"; "The findings are intended to provide a theoretical foundation and scientific support for early warning and risk mitigation of high-altitude and long-runout landslides triggered by intense earthquakes." |
| Concern | Search in the Conclusions (p. 25, l. 460 to p. 26, l. 492, text.json, checked on the page images p. 25 and 26) for "earthquake", "seismic", "quake", "altitude", "high-level", "runout", "run-out", "warning", "risk", "mitigation", "hazard", "accumulat" and "Mogangling": 0 hits each. The trigger of the title, the seismic loading discussed in the results (p. 15, l. 306 to 321), the aims of a "law" (l. 40), of "energy accumulation" (l. 68) and of early warning and risk mitigation (l. 72 to 73), and the evaluation basis for the Dadu River area (p. 5, l. 123 to 125) are not taken up, and no conclusion states what transfers to other landslides. There is no Discussion, and no citation occurs after p. 2, l. 63, so the results are not compared with prior studies, although the list contains studies on the failure process of the same landslide (Wu, J. et al. 2013, p. 28, l. 588 to 590), on the Mogangling landslide and its earthquake (Zhao et al. 2021, p. 29, l. 600 to 602), on landslides in Moxi Town (Zhou et al. 2024, l. 603 to 605) and by the first author on mechanical energy evolution in rock avalanches (Ge et al. 2021, p. 27, l. 540 to 542). GB-06 concerns the gap claim and the literature missing from the introduction; GB-50 counts these entries among the uncited ones; this finding concerns the missing link between conclusions, aims and prior work; GB-05 concerns the seismology citations that end in p. 2, l. 63. |
| Suggestion | Add a Discussion before Section 4 that compares the reconstructed process and energies with Wu et al. 2013, Zhao et al. 2021 and Ge et al. 2021, states the role of the seismic input in the energy results, names what transfers to other high-altitude, long-runout landslides, and states what the results contribute to early warning; take these points up in the Conclusions or remove the corresponding aims from p. 2, l. 40 to 41 and l. 71 to 73. |
| Status | verified (searches; titles of the entries as printed in the reference list) |
| Severity | moderate |
| Source | S4 |

**GB-48 Conclusion 1 recommends restoration steps (trajectory equations, reference to other mountains of the same stratigraphic unit) that the study did not carry out or test.**

| Field | Content |
|---|---|
| Check | P15, P18 |
| Location | p. 25, l. 463 to 468; p. 6, l. 138 to 140; p. 7, l. 157 to 162; p. 2, l. 49 to 51 |
| Quotation | "their trajectory equations can be extracted as a basis for restoring the contours"; "In such cases, restoration can be guided by referencing other mountain areas within the same stratigraphic unit."; "The contour line is modified along the extension direction of the mountains on the left and right sides" |
| Concern | Search over the whole text.json: "equation" 2 hits (l. 263, governing equations; l. 465, the conclusion), "stratigraphic" 1 hit (l. 468); "reference features" and "other mountain" occur only in Conclusion 1. The method describes another procedure: the contours of sliding bed and accumulation area "are modified to be straight" (l. 139 to 140) along the mountains on both sides (l. 157 to 158). It extracts no trajectory equations and refers to no other mountain area of the same stratigraphic unit. Conclusion 1 therefore presents as a finding a procedure the manuscript neither applied nor tested. GB-13 concerns the missing check of the restored surface in the method; this finding concerns the recommendation built on it. GB-04 and GB-18 concern other sentences of the passages cited here (p. 2, l. 46 to 49; p. 7, l. 159 to 160). |
| Suggestion | Either describe in Section 2.1 (p. 6, l. 138 to p. 7, l. 162) how trajectory equations were extracted and which reference areas were used for the deposit area, or reword Conclusion 1 (p. 25, l. 463 to 468) as a proposal for future work, limited to the procedure actually applied. |
| Status | verified (searches) |
| Severity | moderate |
| Source | S4, SD |

**GB-49 All own data and all code are withheld "upon reasonable request" without a reason, although none of them concern persons.**

| Field | Content |
|---|---|
| Check | P12 |
| Location | p. 26, l. 494 to 495; p. 26, l. 505 to 506; data sources in Sections 2.1 to 2.4, p. 6 to 15 |
| Quotation | "The codes that support the findings of this study are available from the first author, Yunfeng Ge, upon reasonable request."; "The data and materials that support the findings of this study are available from the first author, Yunfeng Ge, upon reasonable request." |
| Concern | The manuscript provides a code and a data statement, so every own source is covered generically. The methods name at least six own data sources, and the statements name none of them and give no reason for not depositing them: (1) the UAV-derived DEM and point cloud (p. 6, l. 130 to 135; GB-12); (2) the restored contours and pre-landslide surface (p. 6, l. 138 to p. 7, l. 143 and l. 157 to 159; Fig3 (c); GB-13); (3) the laboratory test results behind Table 1 (p. 11, l. 207), which are not reported (GB-24); (4) the 3DEC model and the displacement, velocity and stress histories of the ten blocks and the whole mass (p. 13, l. 256 to 264; GB-32); (5) the scripts for collision detection (p. 11, l. 226 to 233; GB-29), for Eq. (1) to (4) and for the alpha-shape envelopes (p. 14, l. 272 to 283; GB-35); (6) the field investigation results and photographs (p. 13, l. 266; Fig7 (o); GB-33). All are terrain, rock, simulation or code data; none concerns persons. The central quantities (1,139 effective collisions, VS = 29.47 % and AG = 319.5 %, the energy curves) therefore cannot be recomputed by a reader. Third-party inputs are treated in GB-22. |
| Suggestion | Deposit the DEM or point cloud, the restored surface, the 3DEC input files, the exported monitoring histories and the analysis scripts in a public repository with a persistent identifier, and replace the statements at p. 26, l. 494 to 495 and l. 505 to 506 by statements that name each item with its identifier; if an item cannot be released, name it and the reason. |
| Status | verified (wording of both statements; list of sources in the method text, p. 6 to 15) |
| Severity | moderate |
| Source | S2 |

**GB-50 About half of the works cited in the text have no reference entry, and about half of the reference entries are never cited.**

| Field | Content |
|---|---|
| Check | P4 |
| Location | p. 26, l. 508 to p. 29, l. 605; in-text citations of the introduction, p. 1 to 2 |
| Quotation | "(Huang et al., 2012; Intrieri et al., 2018)"; "(Navarre et al., 2009; Van Herwijnen and Schweizer, 2011; Helmstetter and Garambois, 2010; Cook et al., 2021; Pandey et al., 2021)" |
| Concern | The introduction cites 29 distinct works (p. 1, l. 34 to p. 2, l. 63; the quotations stand in p. 2, l. 53 to 54 and l. 62 to 63); no citation occurs after p. 2, l. 63 (GB-11). Matched against the 31 entries (page images p. 26 to 29): 10 citations have an entry with the same year; 3 have a candidate entry with another year (Tian et al. 2017 against 2016, p. 28, l. 577; Zhang et al. 2024 against Zhang, J. et al. 2023, Landslides 21, p. 29, l. 594 to 596; Zhao et al. 2020 against 2021, p. 29, l. 600 to 602); 2 cannot be told apart (Fan et al. 2019a and Fan et al. 2019 against two Fan entries of 2019 without suffix, p. 27, l. 530 to 536); 14 have no candidate entry: Cook et al. 2021, Cuomo et al. 2021, Fan et al. 2020, Helmstetter and Garambois 2010, Van Herwijnen and Schweizer 2011, Huang et al. 2012, Huang et al. 2019, Intrieri et al. 2018, Navarre et al. 2009, Pandey et al. 2021, Shugar et al. 2021, Zhang et al. 2020a, Zhang et al. 2020b, Zhu et al. 2010 (10 + 3 + 2 + 14 = 29, Python). Of the entries, 16 are cited nowhere: Bernardie 2021 (p. 26, l. 508), Chang 2022 (l. 514), Chen 2024 (p. 27, l. 517), Dahal 2022 (l. 524), Gao 2023 (l. 537), Ge 2021 (l. 540), Gong 2024 (l. 543), He, J. 2023 (l. 546), He, K. 2022 (l. 549), He, N. 2023 (l. 553), Nava 2025 (p. 28, l. 562), Sinčić 2025 (l. 566), Wu, J. 2013 (l. 588), Yang 2022 (l. 591), Zhang, K. 2019 (p. 29, l. 597) and Zhou 2024 (l. 603); 13 are cited and 2 are candidates (13 + 2 + 16 = 31). If Zhang, J. 2023 and Zhao 2021 are not the works meant, the counts become 16 cited works without entry and 18 uncited entries. Shares: 14 of 29 cited works without entry (48.3 %) and 16 of 31 entries uncited (51.6 %), both inferred. Five of the uncited entries are set in grey (KK-31), which suggests they were pasted from another list, and several uncited entries concern the Mogangling landslide itself (GB-47). |
| Suggestion | Add complete entries for the 14 works to the reference list (p. 26 to 29), resolve the three year conflicts and the two Fan 2019 citations, and either cite the 16 uncited entries where they support a statement or delete them. |
| Status | verified (citations and entries on the page images p. 1, 2, 26 to 29); inferred (identity of Zhang et al. 2024 with Zhang, J. et al. 2023 and of Zhao et al. 2020 with Zhao, B. et al. 2021; percentages, Python) |
| Severity | moderate |
| Source | S4 |

#### Minor corrections

| ID | Location | Quotation | Replacement | Source |
|---|---|---|---|---|
| KK-28 | p. 25, l. 464 to 466 | "It should be noted that:(a) Outside"; "restoring the contours;(b) The" | "It should be noted that: (a) outside" and "restoring the contours; (b) the"; GB-48 concerns the content of the sentence | S4 |
| KK-29 | p. 26, l. 499 | "XF: Data curation, Investigation. LZ: Data curation, Investigation." | "XF: Data curation, Investigation; LZ: Data curation, Investigation." | S4 |
| KK-30 | p. 26, l. 507 | "Reference" | "References" | S4 |
| KK-31 | p. 26, l. 508 to 510; p. 27, l. 524 to 526; p. 28, l. 562 to 565; p. 28, l. 566 to 568; p. 29, l. 597 to 599 | "Bernardie, S., Vandromme, R."; "Dahal, A., Tanyas, H."; "Nava, L., Novellino, A."; "Sinčić, M., Bernat Gazibara, S."; "Zhang, K., Wang, S." | set these five entries in black and justified like the other 26 (on the page images their text is grey, darkest pixel value 34 against 0 in the other entries, and ragged right, measured by S4); all five are uncited, see GB-50 | S4 |
| KK-32 | p. 27, l. 530 | "Fan, X., Scaringi, G., Korup, O., et al.:" | list all authors, as the other 30 entries do; KK-06 concerns the missing suffix of this entry and GB-50 the citation status of the list | S4 |

#### Verification log

| ID | Check | Checked | Values | Result |
|---|---|---|---|---|
| PP-46 | P4 | Numbering and in-text references of figures, tables, equations and sections at the page images (S4) | Fig1 l. 76, Fig2 l. 93, Fig3 l. 144, Fig4 l. 173, Fig5 l. 220 and 229, Fig6 l. 256, Fig7 l. 301 to 353, Fig8 l. 375, Fig9 l. 393, Fig10 l. 414 and 418, Fig11 l. 428, Fig12 l. 443; Tables 1 and 2 at l. 212 and l. 259; Eq. (1) to (6) without gap; sections 1, 2, 2.1 to 2.4, 3, 3.1, 3.2, 3.2.1, 3.2.2, 3.4, 4 | no finding beyond GB-18, GB-07, KK-25, KK-26, KK-27 |
| PP-47 | P4 | Short citation against entry for the cited works that have an entry (S4) | Carpignano (5 authors), Du (5), Hu (5), Li (6), Sun (4), Wang 2014 (4), Wu, H. 2024 (6): year, spelling and "et al." agree; Song agrees apart from the typo; deviations: Fan 2019a, Wang 2021, Tian, Zhang 2024, Zhao 2020, Cheng 2014 | no finding for the 7 agreeing citations; deviations in KK-06, KK-09, KK-10, KK-11 |
| PP-48 | P15 | Assignment of each conclusion to a place in the results (S4) | C1 restoration: p. 6 to 7, Fig3, partly; C2 model content: p. 9 to 11, Table 1, Fig4, yes, validation and collision method separately; C3 energy: p. 19 to 20, Fig8, Fig9; C4 front and rear: no place; C5 fragmentation: p. 24 to 25, Fig12, interpretation only; the solid-to-fluid transition (p. 25, l. 453 to 454) is not taken up in the conclusions (0 hits for "solid", "fluidi", "phase" in l. 460 to 492) | findings GB-48, GB-38, GB-41, GB-42, GB-45; the omission of the transition noted, not raised |
| PP-49 | P15 | Proposals and recommendations held against the manuscript's own findings (S4; no outlook section) | (1) "new idea" (p. 2, l. 50 to 51) against the unvalidated surface; (2) Conclusion 1 (b) against the procedure used; (3) early warning (p. 2, l. 72 to 73) and (4) evaluation basis for the Dadu River area (p. 5, l. 123 to 125) against the conclusions; (5) collision identification (p. 25, l. 473 to 475) against the threshold choice | findings GB-48, GB-47, GB-38; no proposal discards a step shown to be necessary |
| PP-50 | P15 | Verb strength in the conclusions and the results sentences they rest on (S4) | "can be drawn" (l. 462, 477), "ensures" (l. 471), "can be identified" (l. 474), "obeys the law" (l. 478), "it can be concluded" (l. 483, 489); results: "compelling evidence" (l. 353), "It is evident" (l. 375), "successful" (l. 389), "it is clear" (l. 418), "effectively reveals" (l. 429), "further confirms" (l. 451) | over-strong verbs raised in GB-41, GB-42, GB-45, GB-38; disclosed limits not raised again |
| PP-51 | P15 | Core terms of title and aims in the conclusions (p. 25, l. 460 to p. 26, l. 492, 36 text lines) (S4) | "transfer" 3, "dissipat" 4, "structur" 1, "stage" 1, "front" 4, "rear" 3, "compress" 1; 0 hits for "earthquake", "seismic", "quake", "altitude", "high-level", "runout", "run-out", "warning", "risk", "mitigation", "hazard", "accumulat", "Mogangling" | missing terms raised in GB-47 |
| PP-52 | P16 | Language and typesetting of p. 25 to 29 at the page images (S4) | conclusions without error apart from KK-28; statements with italic headings, punctuation at l. 499; 31 references in alphabetical order, each with title, journal, volume, pages or article number, DOI and year; preprints marked (Dahal 2022, Yang 2022); no line breaks inside DOIs | no finding beyond KK-28, KK-29, KK-30, KK-31, KK-32 |
| PP-53 | P9, P18 | Proposed future studies (SD) | whole text.json: "future" 0, "outlook" 0, "recommend" 0; "further" 1 hit in l. 460 to 492 (l. 473, "Furthermore"); one procedure proposal (Conclusion 1) | no finding under P9; procedure proposal in GB-48 |
| PP-54 | P2 | Wording of every quotation and of every embedded quotation in this report against text.json (whitespace and line breaks ignored, superscripts normalised); quotations from figures against the page images; citation search p. 3 to p. 26, l. 506 | 513 distinct quoted strings (615 occurrences) in findings, minor corrections and logs; 408 found verbatim in text.json (quotations with an ellipsis part by part, superscripts normalised); the other 105 are replacement wording, search terms, wording of cited literature or labels read from figures, the latter confirmed at the page images by the instances; first and last line of every quotation held against its location (188 location ranges); citation search p. 3 to p. 26, l. 506 for "et al", a name followed by a year and a year followed by a bracket: 0 hits | three quoted phrases that were paraphrases replaced by the manuscript wording or set without quotation marks (a label for the solid to fluid transition, a paraphrase of p. 10, l. 199 to 200, an abbreviation of p. 25, l. 471 to 472); 11 deviations between quotation and location remain and are explained: figure labels whose wording also occurs in the text, the title on p. 1, minor corrections whose wording also occurs earlier, and two citation quotations whose lines are named in the concern of GB-50 |
| PP-55 | P4 | Every location of this report; formatpruefung.py with the option fundorte lists 347 of them, because the line field of text.json counts lines per page (randzeilen: false) while this report uses the printed margin numbers | 347 entries (216 distinct page and line pairs): 325 without entry in text.json, 17 whose number occurs in text.json only on another page, 5 at a page boundary. Every pair was matched to the printed margin numbers carried in the page text (zf/finde.py, zf/orte.py); 36 pairs that do not lie between two printed numbers with a count that comes out (title, captions, page edges, table and equation lines on p. 1, 2, 3, 5, 6, 7, 9, 10, 11, 13, 14, 15, 16, 19, 20, 22, 24, 25) were counted at the page images from the nearest printed number, for example p. 13, l. 246 upwards from 250 over Eq. (4), (3) and (2), p. 11, l. 214 upwards from 215, p. 7, l. 143 upwards from 145, p. 22, l. 421 downwards from 420 | all 216 pairs confirmed after these corrections: p. 13, l. 244 (S3) to l. 246; p. 7, l. 138 to 143 (S2) to p. 6, l. 138 to p. 7, l. 143; locations extended where a quotation reaches the next line (GB-32 to l. 263, GB-36 from l. 274, KK-07 from l. 42, KK-04 to l. 29); figure captions added to the locations of GB-08, GB-19, GB-23, GB-30, GB-40, GB-44 |
| PP-56 | P2, P4 | Contradictions between instances, decided at the manuscript | (1) cited works without entry: S1 15 (Zhang et al. 2024 included), S4 14 plus candidates; decided 14, Zhang 2024 counted as a year conflict because Zhang, J. et al. is in Landslides 21 (GB-50); (2) uncited entries: S1 17, S4 16; decided 16 plus 2 candidates; (3) lead-in to Eq. (2) to (4): S3 l. 244, S4 l. 246; decided l. 246 at the page image (display equations count as lines, Eq. 1 is l. 245); (4) end label of section a-a' in Fig2 (c): S4 "a" at both ends (300 dpi), S2 and AB "a" and "a'" (AB at 600 dpi); higher resolution followed (GB-18); (5) severity of b-b': S2 moderate, S4 and AB minor; highest kept; (6) points in Fig12: S3 at least 18 on DE above about 270 %, SD at least 17 between about 350 % and 1250 %, AB about 32 in all; not contradictory, all above 10, all given (GB-46); (7) end value of AG: S4 4246 %, AB 4272 %; both given (GB-45); (8) the 450 m: S3 swap of length and width, AB deposit only; kept as alternative resolutions (GB-15); (9) fall height for Fig8: S3 and SD 907 m from a reading of 6500 GJ, AB 910 m from the measured 6521 GJ; measured value used (GB-16); (10) Tian: S1 entry year to 2017, S4 text year to 2016; S1 adopted with the alternative named (KK-06) | decided as stated; decisions entered in the findings named |
| PP-57 | P2 | Notes outside the checklists of all six instances (59 notes: S1 9, S2 12, S3 12, S4 9, AB 7, SD 10) | adopted into findings or minor corrections of the instances: S1 H1, H3, H7 to H9; S2 notes 1 to 10; S3 notes 1 to 5, 8, 9, 12; S4 notes 1 to 4, 6 (in part), 8, 9; AB notes 1 to 4; SD notes 1, 2, 4, 6, 7, 9, 10; new items of the merger after checking at the manuscript: GB-11 (S1 H2, H4 to H6; S2 note 12; S4 note 5; SD note 3), the stiffness question in GB-24 (S2 note 11, S3 note 6, SD note 5), KK-03 (S3 note 10, S4 note 8), KK-04, KK-12, KK-16, KK-19 (S4 note 6), KK-18 (S3 note 7, S4 note 4), KK-23 (S3 note 11), KK-21 (AB note 7) | 5 items discarded after checking: the fault-system contradiction of S4 note 5 and SD note 3 (p. 5, l. 97 to 99 place the area at the junction of the Xianshuihe, Longmenshan and Anninghe faults, so membership in the Longmenshan system at p. 10, l. 186 to 187 is no contradiction); the thanks to reviewers (S4 note 7, p. 26, l. 504; not an error); text features shown in no figure (AB note 5; no figure claims to show them); the figure citation style (AB note 6; belongs to the optional check of journal requirements, not run); the inferred backflow flooding (SD note 8; marked as an inference in p. 16, l. 350 to 352 after the disclosed limit in l. 348 to 350) |
| PP-58 | P4 | Pairs of findings and minor corrections with overlapping location (formatpruefung.py with the option paare) | 133 pairs listed after merging; each pair is either one merged finding or two entries of which the later names the earlier with what differs (formatpruefung reports them as notes, none as error); merged groups: 19 groups of 47 instance findings | every pair either merged or kept separate with a cross-reference stating what differs |

## Optional checks

| Area | What it needs | Responsible | Run |
|---|---|---|---|
| DOI resolution | one retrieval per reference entry with DOI | `science-quellenapparat-pruefung` | no |
| Citation style | the name of the style | `science-zitierstil-harvard-ctr` or the style rules of the journal | no |
| AI statement against publisher policy | the policy of the target publisher | this review, on request | no |
| Relation to the authors' own prior work | the authors' prior work | this review, on request | no |
| Journal requirements | the author guidelines of the target journal | this review, on request | no |
| Subject accuracy | access to the sources of the checked statements and a choice of sections | `science-faktenbeleg-pruefung`, `geo-frage-belegbasiert-klaeren` | no |

## Limits of this review

- Checked version: egusphere-2025-4506.pdf, 29 pages, SHA-256 64cb3787456244aa6102e34f776b47e9a612d06e8894d391758ae240dbe415d6.
- Sources not readable: Ge, Tang and Li (2021), Landslides 18, 3559 to 3576 (title and metadata only); Wu, H. et al. (2024) (title and metadata only); Carpignano et al. (2009) and Du et al. (2021) (abstract only); Navarre et al. (2009) (not read, identified through its entry in van Herwijnen and Schweizer 2011); the 14 cited works without reference entry could not be identified with certainty. Statements about literature rest on the accesses named in each finding, made by instances S1 and S4; the merger did not reopen them.
- Findings with status assumption: 10 of 50 have the status assumption for at least one partial statement; in none of them is the assumption the central statement, and each assumption is put as a question.
- Optional checks run: 0 of 6.
- Dropped instances: none.
- Discarded findings: 0 of the 77 findings delivered by the instances (all had the required fields); 47 of them were merged into 19 findings, so the 77 instance findings became 49 findings; one finding was added by the merger (ZF); 10 instance minor corrections were absorbed into findings and the remaining 38 merged into 24 rows, to which the merger added 8. Of the 59 notes outside the checklists, 5 items were discarded after checking at the manuscript (PP-57).
- Line numbers: text.json counts lines per page, so every location was counted from the printed margin numbers (PP-55); values read from figures are measurements by the instances AB, S3, S4 and SD at 300 to 800 dpi, not repeated by the merger except where stated.
