# Review report: Energy and structural evolution process of high-altitude and long-runout landslides induced by a strong earthquake

| Field | Value |
|---|---|
| Manuscript | Ge, Y., Hu, B., Tang, H., Fu, X., and Zhu, L. (2025): Energy and structural evolution process of high-altitude and long-runout landslides induced by a strong earthquake, EGUsphere preprint egusphere-2025-4506, https://doi.org/10.5194/egusphere-2025-4506 |
| Checked version | egusphere-2025-4506.pdf, 29 pages, SHA-256 64cb3787456244aa6102e34f776b47e9a612d06e8894d391758ae240dbe415d6 |
| Date | 2026-10-18 |
| Language | English |
| Review instances | Segments 1 to 4 (S1 to S4), figures (AB), study design (SD); the six review instances ran as separate agents; no instance dropped |
| Note | Line numbers (l.) are the printed margin numbers of the manuscript, confirmed on the page images; the manuscript prints every fifth number, the others are counted from the nearest printed number. Page numbers (p.) are the printed page numbers. Figures are named as in the manuscript (Fig1 to Fig12). |

## Summary

The manuscript is a single case study that reconstructs the Mogangling rock landslide, triggered by the 1786 Kangding earthquake (Ms 7¾) on the Dadu River, Sichuan, with the three-dimensional distinct element code 3DEC. The pre-failure topography is restored by straightening contour lines of a UAV-derived DEM over the sliding bed and deposit; the slide mass is discretised into 25345 blocks of 8.7 m × 8.7 m in plan with Mohr-Coulomb properties (Table 1) and driven by the acceleration record of the Luding station from the 2008 Wenchuan earthquake. Kinetic, potential and dissipated energy (DE defined as the loss of mechanical energy, Eq. 4) are tracked for the whole mass and for ten monitored blocks; "effective collisions" are identified as local peaks of velocity against travel distance at a 30 % prominence threshold (1,139 detections); alpha-shape envelopes (α = 1) at ten times give a volume swelling VS and an area growth AG. Key reported numbers are a simulated duration of 131 s, a peak velocity of 31.6 m/s at 12 s, a constant energy total of about 6500 GJ (Fig8) and a "solid to fluidized" transition at VS of 29.47 % and AG of 319.5 % at the kinetic energy peak. The five conclusions concern the restoration method, the agreement with field imagery, energy conservation of the whole mass and its absence for single blocks, collision-driven energy transfer from rear to front, and fragmentation as the cause of envelope growth.

## Strengths

1. The energy budget is defined in closed form (Eq. 1 to 4, l. 241 to 255) and displayed as stacked PE, KE and DE for the whole mass (Fig8) and for each of the ten monitored blocks (Fig9). This lets a reader check the budget from the figures: constant totals, the timing of the KE maximum and the initial block energies could be measured and compared with the text (PP-14, PP-33, PP-34), which is also what makes the problems in GB-37, GB-38 and GB-25 visible.
2. The detection of effective collisions is shown as a threshold sweep: Fig5(b) to (f) displays the detections at 10 % to 50 % side by side with labels that match the text (PP-13), so the reader sees how the chosen 30 % changes the result; the gaps that remain in the definition are collected in GB-24.
3. The dynamic set-up and its main simplifications are stated where they apply: viscous and free-field boundaries with a static stage before the dynamic one (l. 193 to 202), and the missing record of the 1786 event, the ignored structural planes and the smooth restored surface at the place of the respective method (PP-21). The reader therefore knows the model's simplifications; their consequences are taken up in GB-20 and GB-33.
4. The kinematic narrative is tied to figure values: the velocity maxima of Section 3.1 match the Fig7 colour bars (PP-29), the dimension labels of Fig4 match the text (PP-11), the stage times agree with the course of KE in Fig8 within one bar (PP-28, PP-34), and figures, tables and equations are numbered consecutively and cited in order (PP-27, PP-44). The simulated sequence can thus be followed panel by panel.

## Weaknesses

1. The energy results do not test the simulation. The sum KE + PE + DE is constant by the definition of DE in Eq. (4), so the stated conservation for the whole mass and its absence for single blocks are not results, and the work of the seismic input is missing from the budget (GB-37). The absolute energies cannot be reconciled with either of the two stated volumes, the stated velocities or the block energies (GB-38, GB-15), and the datum of the potential energy is not the one stated (GB-25). Suggestion: compute dissipation independently from contact friction and damping, add the input work at the base, state mass, density and PE datum, and recompute Fig8, Fig9 and Fig12.
2. Several mechanisms are stated as results although the model output reported does not measure them: more collisions, more energy received and longer runout of the lower or front blocks (GB-40), fragmentation as the cause of envelope growth (GB-44), a solid to fluid threshold read at a kinetic energy peak that Fig12 probably does not sample (GB-42), and P- and S-wave action, amplification and structural-plane control (GB-33). Suggestion: add per-block, normalised and stage-resolved collision counts, a direct measure of fragmentation, an envelope at the time of the KE maximum and acceleration monitoring, or reword these statements as interpretation.
3. The reconstruction of the real 1786 event is not checked against independent evidence: the restored pre-failure surface is not tested (GB-16), validation is a visual comparison of two features (GB-36), the input is a proxy record from 2008 without sensitivity analysis and with an uncited justification (GB-20), the field investigation is not documented (GB-34), and the aims of a general law and of early warning exceed a single-case design (GB-04). Suggestion: compare runout, deposit area and thickness quantitatively with the present DEM, run a suite of input motions and two or three restoration variants, document the field work, and narrow the aims to what the design can answer.
4. Reproducibility and referencing are weak in many places of moderate weight: model parameters, discontinuities and geological units cannot be mapped to the model (GB-18, GB-19, GB-11), the collision threshold, the reference quantities of VS and AG and the alpha convention are undefined (GB-24, GB-30, GB-28), data, code, software and external data sources are not available or not named (GB-47, GB-13, GB-21), 13 citations have no reference entry and 16 entries are never cited, among them the earlier studies of the same landslide (GB-08, GB-48), and the novelty and gap claims rest on no reported search (GB-05, GB-09). Suggestion: add a table of model parameters with sources and a table of data and software, deposit inputs and scripts, define every threshold and reference quantity, and reconcile text and reference list.

## Findings by segment

### Segment 1: Abstract, introduction, state of research (p. 1 to 2)

#### Substantive findings

**GB-01 The temporal trend stated in the opening sentence is not supported by either cited work.**

| Field | Content |
|---|---|
| Check | P13 |
| Location | p. 1, l. 33 to 34 |
| Quotation | "In recent years, the chain disasters of high-level rock landslides in high-intensity earthquake areas have shown a trend of frequent occurrence (Carpignano et al., 2009; Fan et al., 2019a)" |
| Concern | The opening sentence motivates the study with a trend over time. Carpignano et al. (2009) develop a methodological framework for multi-risk maps of the Piedmont Region (Italy); according to the abstract they report an increased vulnerability of society to multiple risks and do not deal with earthquakes, landslides or a change in event frequency. Fan et al. (2019, Rev. Geophys., 57, 421-503) describe chains of hazards after large earthquakes (mainly Chi-Chi 1999 and Wenchuan 2008); the increase they report is the elevated landslide activity that persists for years to decades after a given earthquake, not a rise in the occurrence of such chains in recent years. Neither work carries the trend as written. The suffix "2019a" cannot be resolved because the list has two Fan entries of 2019 without suffixes (GB-02). |
| Suggestion | In l. 33 to 34 either cite a study that counts such events over a defined period, or restate what Fan et al. (2019) show, for example "Large earthquakes trigger chains of geohazards, and landslide activity can remain elevated for years to decades after the event"; remove Carpignano et al. (2009) here or cite it for multi-risk mapping. |
| Status | content of both works: verified at abstract level (abstracts read by instance S1); that the full texts contain no such trend: inferred (Carpignano et al. 2009 closed access; the open full text of Fan et al. 2019 not read beyond the abstract) |
| Severity | moderate |
| Source | S1 |

**GB-02 Seven short citations disagree with their reference entries in year, author form or spelling, and the two Fan entries cannot be assigned unambiguously.**

| Field | Content |
|---|---|
| Check | P4 |
| Location | p. 1, l. 34, l. 36, l. 37; p. 2, l. 45 to 46, l. 48 to 49, l. 56 to 57; p. 27, l. 521, l. 530 to 536; p. 28, l. 575 to 577, l. 581 to 584; p. 29, l. 594 to 596, l. 600 to 602 |
| Quotation | "(Carpignano et al., 2009; Fan et al., 2019a)"; "Wang, 2021"; "Tian et al., 2017"; "Song at al.2017"; "Cheng 2014"; "Fan et al., 2019; Zhao et al., 2020" |
| Concern | (1) Fan: the list has two Fan entries, both dated 2019 and without suffix (Fan, Scaringi, Korup et al., l. 530 to 532; Fan, Yang, Siva Subramanian et al., l. 533 to 536), while the text cites "Fan et al., 2019a" (l. 34), "Fan et al., 2019" (l. 56 to 57) and "Fan et al., 2020" (l. 46). Case A: "2020" means Fan, Yang et al., whose issue year is 2020 (Landslides 17, 147-164, issue 1 of 2020, per the University of Twente repository record read by instance S4); then the entry year is wrong and "2019a" should be "2019". Case B: both 2019 citations mean different works; then a and b must be assigned in the list and "2020" has no entry. (2) "Tian et al., 2017" (l. 37) against entry year 2016 (l. 577). (3) "Zhao et al., 2020" (l. 57) against entry year 2021 (l. 602). (4) "Zhang et al., 2024" (l. 45 to 46): the only plausible entry, Zhang, J. et al., Landslides 21 (l. 594 to 596), is dated 2023; otherwise the citation has no entry. (5) "Wang, 2021" (l. 36) for an entry with seven authors (l. 581 to 584). (6) "Cheng 2014" (l. 48 to 49) for a two-author entry whose second author is printed "Yu-Sheng, L." (l. 521), apparently given name first. (7) "Song at al.2017" (l. 46). In items 2 to 4 the volume years suggest that online-first and issue years were mixed; this is offered as a question, not checked. |
| Suggestion | Decide case A or B and align l. 34, l. 46 and l. 56 to 57 with l. 530 to 536 (label the entries "2019a" and "2019b" if case B applies); use one year convention throughout and align l. 37, l. 45 to 46 and l. 57 with l. 577, l. 596 and l. 602; replace "Wang, 2021" by "Wang et al., 2021" (l. 36) and "Song at al.2017" by "Song et al., 2017" (l. 46); if the second author of the Cheng entry is Li Yu-Sheng, write "Cheng and Li, 2014" in l. 48 to 49 and "Cheng, F. and Li, Y.-S.:" in l. 521. |
| Status | mismatches between citations and entries: verified (page images p. 1, 2, 27 to 29); issue year 2020 of Fan, Yang et al.: verified (repository record); online-first explanation for items 2 to 4: assumption, put as a question |
| Severity | minor |
| Source | S1, S4, SD |

**GB-03 Several sentences use loan translations or lack a grammatical subject, which obscures their meaning.**

| Field | Content |
|---|---|
| Check | P16 |
| Location | p. 1, l. 38 to p. 2, l. 39; p. 2, l. 42 to 44; p. 3, l. 85; p. 5, l. 110 to 111; p. 10, l. 193 to 195; p. 25, l. 463 to 464 |
| Quotation | "was repaired and reconstructed"; "the terrain restoration before a landslide is less. For landslides that have not occurred too far away"; "UAV impact"; "some individuals"; "burst the Dadu River after 9 days"; "a preliminary restoration of the ancient landslide can be performed" |
| Concern | "repaired" stands for reconstructed (l. 38 to 39); "is less" for has rarely been attempted (l. 42); "not occurred too far away" for "recent" (l. 43); "UAV impact" for UAV imagery (l. 44); "individuals" for selected blocks (l. 85); "burst the Dadu River after 9 days" for a dam that breached after 9 days (l. 110 to 111); Conclusion 1 speaks of restoring "the ancient landslide" where the pre-landslide topography is meant (l. 463 to 464). The sentence in l. 193 to 195 ("In the course of a discrete-element simulation-particularly when modeling nominally semi-infinite bodies such as the use of fixed or elastic boundaries in a static analysis will inevitably reflect outbound seismic waves into the model during a subsequent dynamic analysis.") has no grammatical subject for "will inevitably reflect". Further corrections that need only a replacement are listed as minor corrections. |
| Suggestion | Replace in l. 38 to 39 "was repaired and reconstructed" by "was reconstructed"; in l. 42 to 43 write "Reconstructions of the pre-landslide terrain are rare. For recent landslides"; in l. 44 "UAV imagery"; in l. 85 "selected blocks"; in l. 110 to 111 "dammed the Dadu River; the dam breached after 9 days"; in l. 193 to 195 "In discrete-element simulations of nominally semi-infinite bodies, fixed or elastic boundaries used in the static analysis would reflect outgoing seismic waves back into the model during the subsequent dynamic analysis."; in l. 463 to 464 "a preliminary restoration of the pre-landslide topography can be performed". Have the full text language-edited, starting with Abstract, Introduction and Conclusions. |
| Status | verified (page images p. 1 to 3, 5, 10, 25) |
| Severity | minor |
| Source | S1, S4, SD |

**GB-04 The aims of deriving a general law and of supporting early warning cannot be served by a single-case design with one input, one parameter set and no sensitivity analysis.**

| Field | Content |
|---|---|
| Check | P10 |
| Location | p. 2, l. 39 to 41; p. 2, l. 71 to 73; p. 5, l. 122 to 125; p. 25, l. 469 to 470 |
| Quotation | "so as to summarize the law of high-level rock landslide induced by earthquake and reduce the impact of landslide on life and property"; "The findings are intended to provide a theoretical foundation and scientific support for early warning and risk mitigation of high-altitude and long-runout landslides triggered by intense earthquakes." |
| Concern | The design is one historical case, one reconstructed geometry, one proxy input motion, one parameter set, one threshold and one alpha value; there is no variation, no second case and no discussion section that relates the results to other landslides or to earlier energy studies (Ge et al., 2021 is in the reference list but not cited, GB-48). The manuscript states no research questions, so the aims are the only link to the design; for the generalising aims no instrument exists, and early warning is not taken up in the conclusions (GB-45). |
| Suggestion | Either narrow the aims in Section 1 (l. 39 to 41, l. 71 to 73) to the reconstruction of this case, or add a design that can carry a general statement: a parametric study over input motion, friction and joint parameters with the same post-processing, or a second well-documented case, plus a discussion section that compares the energy partition with published rock avalanche studies. State explicit research questions at the end of Section 1. |
| Status | verified |
| Severity | major |
| Source | SD |

**GB-05 The gap and novelty claims on pre-landslide terrain restoration are made without a reported search, and established reconstruction methods exist.**

| Field | Content |
|---|---|
| Check | P28 |
| Location | p. 2, l. 42; p. 2, l. 49 to 51; p. 1, l. 16 to 18 |
| Quotation | "At present, in terms of surface terrain restoration, the terrain restoration before a landslide is less."; "This paper uses the method of restoring the continuity of contour lines to establish the terrain data before a landslide, which can provide a new idea of terrain restoration before a landslide for the same type of research." |
| Concern | No databases, search terms, period or search date are given for either statement. Reconstructing pre-failure topography is an established step: Jaboyedoff, M., Chigira, M., Arai, N., Derron, M.-H., Rudaz, B., and Tsou, C.-Y. (2019): Testing a failure surface prediction and deposit reconstruction method for a landslide cluster that occurred during Typhoon Talas (Japan), Earth Surf. Dynam., 7, 439-458, https://doi.org/10.5194/esurf-7-439-2019, use the sloping local base level (SLBL) method to rebuild failure surfaces, pre-event topography and eroded deposits from DEMs for about 70 landslides; Crosta et al. (EGU General Assembly 2014, EGU2014-16272, conference abstract) rebuilt the pre-failure surface of the Cerro Caquilluco rock avalanches by extrapolating the preserved morphology and used it for runout simulations. The manuscript states limits of its own restoration (l. 160 to 162: the restored terrain "is smooth and the surface does not fluctuate"; l. 466 to 467: the deposit area "is often difficult to restore"), which is credited; missing is the comparison with these methods, without which "a new idea" cannot be assessed. The missing test of the restored surface itself is GB-16. |
| Suggestion | In Section 1 after l. 42 report the search (databases, terms, period, date) or drop "a new idea" in l. 50; add two or three sentences that compare the contour-continuity restoration with SLBL-type and morphological extrapolation methods and state what it adds (see also GB-10, item 3). |
| Status | absence of a reported search: verified; existence of the cited reconstruction methods: verified (Jaboyedoff et al. 2019 open access article page; Crosta et al. 2014 abstract, read by instance S1) |
| Severity | moderate |
| Source | S1 |

**GB-06 The works cited for field-based and GIS geomorphic mapping are numerical studies or are missing from the reference list.**

| Field | Content |
|---|---|
| Check | P13 |
| Location | p. 2, l. 43 to 46 |
| Quotation | "the key information of landslide characteristics is often obtained through photos, field surveys, optical remote sensing images and UAV impact, so as to further build geomorphic maps through GIS (Geographic Information System) for subsequent analysis (Zhang et al., 2024; Song at al.2017; Fan et al., 2020; Wu et al., 2024)." |
| Concern | Of the four citations, two have no matching entry (no Zhang 2024 and no Fan 2020 in the list; see GB-02). The two that resolve are numerical studies by title and index keywords: Song et al. (2017) "Landslide Deformation Prediction by Numerical Simulation in the Three Gorges, China" and Wu et al. (2024) "Numerical simulation on potential landslide-induced wave hazards by a novel hybrid method" (keywords include material point method and smoothed particle hydrodynamics). None of the four can be confirmed to show the workflow from photographs, field survey, remote sensing and UAV data to GIS geomorphic maps that the sentence attributes to them. |
| Suggestion | In l. 45 to 46 replace the citations by works that build geomorphic maps from photographs, field survey, optical imagery or UAV data in GIS, and correct the entries as in GB-02. |
| Status | missing entries: verified (page images p. 26 to 29); content of Song et al. 2017 and Wu et al. 2024: inferred (titles and index keywords only) |
| Severity | minor |
| Source | S1 |

**GB-07 The ranking of two-dimensional simulations as the most common approach for terrain restoration rests on three citations that do not show it.**

| Field | Content |
|---|---|
| Check | P13 |
| Location | p. 2, l. 46 to 49 |
| Quotation | "For most numerical simulations involving terrain restoration, a two-dimensional simulation is more often used. The simplified model is adopted to simulate the overall process of landslide by inputting external stress (Du et al., 2021; Cheng 2014; Li et al., 2024)." |
| Concern | The sentence is the stated background for the 3-D contour-based restoration in l. 49 to 51. Li et al. (2024, Front. Earth Sci., 12, 1466751, open access, read by instance S1) model an ancient landslide with GeoStudio (SEEP/W, SLOPE/W, Morgenstern-Price limit equilibrium) under rainfall-driven transient seepage; they apply no seismic or other external stress input, simulate no runout and do not restore pre-failure terrain. Cheng and Li (2014) use UDEC for a dynamic analysis of the Huanglang Valley ancient landslide; the abstract does not mention a restoration of pre-failure terrain. Du et al. (2021) could not be read. A ranking ("most", "more often") is a quantitative statement; it is not supported by a count, and one of the three examples does not belong to the class described. |
| Suggestion | Either support the ranking with a count of studies (database, search terms, period), or reword l. 46 to 49, for example "Several numerical studies of ancient landslides used two-dimensional models with dynamic input (e.g. Cheng and Li, 2014)", and cite Li et al. (2024) only for seepage and limit-equilibrium stability of ancient landslides. |
| Status | Li et al. 2024: verified (full text); Cheng and Li 2014: verified at abstract level; Du et al. 2021: inferred (not readable); lack of support for the ranking: inferred |
| Severity | moderate |
| Source | S1 |

**GB-08 Thirteen in-text citations have no entry in the reference list.**

| Field | Content |
|---|---|
| Check | P4 |
| Location | p. 2, l. 53 to 54, l. 56 to 57, l. 58 to 59, l. 62 to 63 |
| Quotation | "(Huang et al., 2012; Intrieri et al., 2018)"; "(Huang et al., 2019; Fan et al., 2019; Zhao et al., 2020)"; "(Zhu et al., 2010; Zhang et al., 2020a, b; Cuomo et al., 2021; Shugar et al., 2021)"; "(Navarre et al., 2009; Van Herwijnen and Schweizer, 2011; Helmstetter and Garambois, 2010; Cook et al., 2021; Pandey et al., 2021)" |
| Concern | The 31 entries (l. 508 to 605) contain no author Huang, Intrieri, Zhu, Cuomo, Shugar, Navarre, Van Herwijnen, Helmstetter, Cook or Pandey and no Zhang entry from 2020. Without entry: Huang et al. 2012, Intrieri et al. 2018, Huang et al. 2019, Zhu et al. 2010, Zhang et al. 2020a, Zhang et al. 2020b, Cuomo et al. 2021, Shugar et al. 2021, Navarre et al. 2009, Van Herwijnen and Schweizer 2011, Helmstetter and Garambois 2010, Cook et al. 2021, Pandey et al. 2021; 13 of 29 cited works, 13/29 = 44.8 %. Together with Zhang et al. 2024 and Fan et al. 2020 (GB-02), 15 citations cannot be resolved. They carry the whole state-of-research paragraph on field investigation, numerical analysis and landslide seismology (l. 52 to 64), including the gap stated in l. 63 to 64 (GB-09); a reader cannot check that gap. |
| Suggestion | Add the 13 entries to the reference list (from l. 507), or remove the citations from l. 53 to 63. |
| Status | verified (l. 53 to 63 against l. 508 to 605; count recomputed) |
| Severity | moderate |
| Source | S4 |

**GB-09 The claim that energy evolution during collisions lacks quantitative study is made without a search and is contradicted by a work in the manuscript's own reference list.**

| Field | Content |
|---|---|
| Check | P28 |
| Location | p. 2, l. 63 to 64 |
| Quotation | "However, they still lack a quantitative and systematic study of this topic, especially on energy evolution during the collision." |
| Concern | The sentence defines the gap the study fills (l. 67 to 68: "it focuses on revealing the mechanisms of energy accumulation, transfer, and dissipation"). No search is reported. The reference list contains Ge, Tang and Li (2021) "Mechanical energy evolution in the propagation of rock avalanches using field survey and numerical simulation" (Landslides, 18, 3559-3576), which by its title treats the energy evolution of rock avalanche propagation; it is cited nowhere in the text (GB-48). Lin et al. (2022, Nat. Hazards Earth Syst. Sci., 22, 639-657) quantify with DEM how fragmentation and collisions transfer energy between front and rear parts of a sliding rock mass. In addition, "they" refers back to the landslide seismology studies of l. 61 to 63, so the gap is stated for a field that is not the one the study addresses. |
| Suggestion | Rewrite l. 63 to 64 so that the gap is stated relative to Ge et al. (2021) and Lin et al. (2022), for example as block-level energy transfer under seismic input in a 3-D DEM of a dated historical event, and report the search behind the claim. |
| Status | absence of a search and of any in-text citation of Ge et al. 2021: verified; content of Ge et al. 2021 beyond its title: inferred (closed access); Lin et al. 2022: verified (open access abstract) |
| Severity | moderate |
| Source | S1 |

**GB-10 Work that qualifies the collision-based interpretation of energy transfer, and work on pre-failure topography reconstruction, is missing from the reference list.**

| Field | Content |
|---|---|
| Check | P14 |
| Location | p. 2, l. 63 to 69; p. 1, l. 28 to 30; p. 24, l. 445 to 450; p. 26, l. 483 to 492; p. 2, l. 49 to 51 |
| Quotation | "When the rear rock mass collides with the front, its dissipated energy sharply increases and transfers energy to the front rock mass, enabling the front portion to slide farther." |
| Concern | Contribution in one sentence: a 3-D DEM reconstruction of the 1786 Mogangling landslide on contour-restored topography that tracks kinetic, potential and dissipated energy of the whole mass and of single blocks, identifies effective collisions and links envelope dilation to energy transfer. Three works bear directly on this and are not among the 31 entries: (1) Lin, Q., Wang, Y., Xie, Y., Cheng, Q., and Deng, K. (2022): Multiscale effects caused by the fracturing and fragmentation of rock blocks during rock mass movement: implications for rock avalanche propagation, Nat. Hazards Earth Syst. Sci., 22, 639-657, https://doi.org/10.5194/nhess-22-639-2022; with DEM they find that fragmentation accelerates the front and decelerates the rear through stored and released elastic strain energy and that energy transfer by fragmentation is more efficient than by collision, which qualifies Conclusion 4 and the reading in l. 445 to 450. (2) De Blasio, F. V. and Crosta, G. B. (2015): Fragmentation and boosting of rock falls and rock avalanches, Geophys. Res. Lett., 42, 8463-8470, https://doi.org/10.1002/2015GL064723; fragmentation at a slope break can add a horizontal momentum boost, but momentum and runout rise significantly only for slopes steeper than about 70° and fairly uniform clast sizes, which constrains when fragmentation lengthens runout as Conclusion 5 assumes. (3) Jaboyedoff et al. (2019, see GB-05) precede the contour-continuity restoration claimed as new in l. 49 to 51. |
| Suggestion | Discuss items 1 and 2 where the energy transfer mechanism is interpreted (l. 445 to 456), qualify Conclusion 4 (l. 483 to 487) accordingly and state whether blocks in the 3DEC model can fragment at all (GB-44); compare the restoration with item 3 in Section 1 (l. 49 to 51). |
| Status | items 1 and 3: verified (open access article pages, read by instance S1); item 2: verified at abstract level; absence from the reference list: verified (page images p. 26 to 29) |
| Severity | moderate |
| Source | S1 |

#### Minor corrections

| ID | Location | Quotation | Replacement | Source |
|---|---|---|---|---|
| KK-01 | p. 1, l. 21; p. 3, l. 84 | "dissipation energy" | "dissipated energy" (as in l. 241, Fig1 and Fig12) | S1, S2 |
| KK-02 | p. 1, l. 27 and l. 28 | "conservation of energy; For some blocks"; "surrounding rock mass; Compared with" | "conservation of energy; for some blocks"; "surrounding rock mass; compared with" | S4 |
| KK-03 | p. 1, l. 34 | "such as donghekou landslide" | "such as the Donghekou landslide" (as in the reference titles, l. 572, l. 579, l. 582) | S1, S2, S4 |

#### Verification log

| ID | Check | Checked | Values | Result |
|---|---|---|---|---|
| PP-01 | P13 | Inventory of all sentences that report numbers, rankings or evaluations from other works, whole manuscript | With citation: l. 33 to 34, 34 to 37, 42 to 46, 46 to 49, 52 to 54, 55 to 60, 61 to 64 (all in Segment 1). Without citation: l. 99 to 100, 110 to 112, 113 to 119, 136 to 137, 149 to 151, 169 to 170, 186 to 189. 29 in-text citations, of which 17 do not resolve to an entry (15 absent, 2 with year mismatch), 17/29 = 0.586; 31 entries | Findings GB-01, GB-06, GB-07, GB-15; uncited statements in GB-12, GB-20, GB-21, GB-48; the 15 unresolvable citations could not be checked for fidelity |
| PP-02 | P13 | Examples of earthquake-induced landslides, l. 34 to 37 | Sun et al. 2011 (Donghekou, Wenchuan), Wang et al. 2014 and 2021 (Donghekou, Wenchuan M8.0), Hu et al. 2017 and Tian et al. (Ludian Ms 6.5, 2014), all by title | no finding; whether Hu et al. and Tian et al. treat the Hongshiyan landslide in their full texts was not checked |
| PP-03 | P28 | Gap claims: l. 42, l. 46 to 47, l. 49 to 51, l. 60 to 61, l. 63 to 64, l. 113 to 119; two own searches on pre-failure topography reconstruction | No database, term, period or date given anywhere; counterexamples Jaboyedoff et al. 2019 and Crosta et al. EGU2014-16272; De Pedrini et al. 2022 (Geogr. Helv., 77, 21-37) not used, because the abstract states no pre-failure reconstruction | Findings GB-05, GB-09, GB-12; l. 60 to 61 no finding (a statement on scarce instrumental observations, not a claim that a topic is unstudied) |
| PP-04 | P14 | Contribution of the manuscript and six literature searches (energy evolution of rock avalanches, Mogangling landslide, fragmentation and momentum transfer) | Candidates: Ge et al. 2021, Zhao et al. 2021, Wu et al. 2013, Zhou et al. 2024 (all in the list, uncited); Lin et al. 2022, De Blasio and Crosta 2015, Jaboyedoff et al. 2019 (not in the list); Zhao, Crosta, Utili and De Blasio 2017 (J. Geophys. Res. Earth Surf., 122, 678-695) not proposed because of the limit of three | Findings GB-48 and GB-10; search results pointing to the discussion pages or later versions of this manuscript were not opened |

### Segment 2: Methods and model set-up (p. 2 to 15)

#### Substantive findings

**GB-11 The geological units carry different names, symbols and colours in the text, Fig2(c), Fig3(a), Fig3(b), Fig4 and Table 1, so the material parameters cannot be assigned to the model units.**

| Field | Content |
|---|---|
| Check | P38, P3, P29 |
| Location | p. 5, l. 101 to 107; p. 6, Fig2(c) legend; p. 8, Fig3(a) legend and block faces, Fig3(b) legend; p. 10, Fig4 legend; p. 11, l. 207 to 209; p. 11, Table 1, column "Rock mass", rows "bed rock" and "landslide mass" |
| Quotation | "The sand slate of the Triassic Baiguowan formation (T3bg) is exposed on the left bank of the Dadu River."; "colluvial Deluvial deposit (Q4col+dl)" |
| Concern | Names per unit, confirmed on the page images: γo2 is "strongly to weakly weathered Jinning plagioclase granite (γO2)" in l. 101 to 102 but "subdivided into strongly weathered and moderately weathered zones" in l. 208 to 209, "Plagiogranite" in Fig2(c), "Granite" in Fig3(a, b) and "γo2" in Fig4. Quartz diorite is "Quartz diorite (O2)" in l. 102 (printed like a chronostratigraphic code) and "Diorite" in Fig3(a, b), absent from Fig2(c) and Fig4. The left (east) bank is "sand slate of the Triassic Baiguowan formation (T3bg)" in l. 103 to 104, but Fig2(c) shows γM2 "Hybrid granite" east of the river and T3bg appears in no legend. Q4del is "landslide accumulation" in l. 104, "Rubble soil" in Fig2(c) and "Q del" without subscript 4 in Fig4. Q4col+dl is "colluvial Deluvial deposit" in l. 105 and "Massive gravel" in Fig2(c); Fig3(a) uses "Massive gravelly soils", Fig3(b) both "Massive gravelly soils" and "Massive gravel". Q4al is "alluvial deposit" in l. 105 and "Sand and pebble gravel" in Fig2(c) and Fig3. Colours differ between panels: Granite is dark brown in Fig3(a) and pink dotted in Fig3(b); Massive gravelly soils tan in (a) and green in (b). In Fig3(a) the swatches Diorite and Sand and pebble gravel differ by 32 in summed RGB, below the threshold of 40, and the largest grey area on the block faces (19 % of the sampled area) has no swatch. Table 1 gives two material sets ("bed rock", "landslide mass"), Fig4 four model units (γo2, Q del, γM2, "Sliding mass"). A reader cannot tell which Table 1 row applies to which Fig4 unit, nor which unit forms the left bank. |
| Suggestion | Add a unit key, for example as an extra column of Table 1, that maps each code (γo2, γM2, quartz diorite with its full symbol, T3bg, Q4del, Q4col+dl, Q4al) to one name used identically in l. 101 to 107, l. 207 to 209, Fig2(c), Fig3(a, b) and Fig4; state which Table 1 row is assigned to each Fig4 unit; resolve T3bg against γM2 on the left bank; give each unit one colour in Fig3(a) and (b) and clearly different colours for Diorite and Sand and pebble gravel; add the grey unit to the Fig3(a) legend; write "Q4del" in Fig4; in l. 104 to 105 write "The Quaternary System mainly includes ... colluvial-deluvial deposit ... of which the colluvial-deluvial deposit is". |
| Status | names, symbols and colours: verified (page images, colour values measured by instance AB); that the parameter assignment cannot be reconstructed: inferred |
| Severity | moderate |
| Source | S2, AB, S4 |

**GB-12 The statement that seismic instability analyses of reservoir slopes are "relatively few" is a gap claim without a reported search or citation.**

| Field | Content |
|---|---|
| Check | P28 |
| Location | p. 5, l. 113 to 119 |
| Quotation | "In the construction of major projects in Western China, the effect of seismic force on slope instability has been underestimated to a certain extent."; "the analysis of the instability probability of potentially unstable high and steep slopes under the action of seismic force and the evaluation and analysis of dam break or dam overturning caused by abnormal bedrock landslide such as surging waves are relatively few." |
| Concern | The passage motivates the case study (l. 122 to 125) with a gap in engineering practice but names neither studies nor a search. The reference list itself contains a seismic response study of a slope on the Dadu River (He, J. et al., 2023, "Seismic response of an irregular slope containing surficial weak layer and internal fractures in Dadu River, southwest China", Landslides, 21, 621-640, l. 546 to 548), which is cited nowhere in the text (GB-48). |
| Suggestion | In l. 113 to 119 cite the studies the statement summarises, including He, J. et al. (2023), and report the search, or reduce the statement to what can be documented. |
| Status | verified (page images p. 5 and p. 27) |
| Severity | moderate |
| Source | S1 |

**GB-13 Software, versions and survey properties needed to rebuild the workflow are not stated.**

| Field | Content |
|---|---|
| Check | P35 |
| Location | p. 6, l. 130 to 135; p. 9, l. 169; p. 11, l. 226 to 229; p. 14, l. 272; p. 26, l. 494 to 495, l. 505 to 506 |
| Quotation | "According to the DEM data obtained by UAV scanning, the point coordinates are extracted, and the landslide area is delimited for precision screening to reduce the point density." |
| Concern | Not stated: UAV platform and sensor, survey date, DEM resolution and accuracy, the target point density after "precision screening", the geographic and projected coordinate systems; the 3DEC version; the GIS and point-cloud software for noise reduction, cavity repair and normal correction; the alpha-shape and peak-detection implementations (provenance of the external data sources: GB-21). Code and data are available only on request (GB-47). |
| Suggestion | Add a table "Data and software" to Section 2 with these items and their versions. |
| Status | verified |
| Severity | moderate |
| Source | SD |

**GB-14 The subdivision of the landslide area is named in three ways, and Fig3(a), which the text cites for four parts, shows two zones.**

| Field | Content |
|---|---|
| Check | P38, P3 |
| Location | p. 7, l. 144 to 146, l. 151 to 156; p. 8, Fig3(a) outlines and legend |
| Quotation | "As shown in Fig3.(a), the geometric model of the terrain surface is established according to DEM. The whole landslide occurrence area can be divided into four parts: the rock wall area, colluvial slope area, slope debris flow area, and main accumulation area." |
| Concern | l. 151 to 156 describe the front edge of the accumulation mass (1120 to 1330 m), the landslide platform (1330 to 1380 m), a part covered by colluvial deposits (1380 to 1600 m) and the landslide walls (1600 to 1890 m). Fig3(a) marks only "I Sliding bed" and "II Accumulation area" with a dotted divider; none of the four names of l. 145 to 146 appears in Fig3(a) or Fig2(c), and the elevation ranges are not marked. A correspondence such as slope debris flow area = landslide platform is possible but not stated. Question to the authors: are the four parts of l. 145 to 146 the four elevation zones of l. 152 to 156? |
| Suggestion | Use one set of zone names in l. 145 to 156 and mark these zones with their elevation ranges in Fig3(a) or Fig2(c), or refer the text to the two zones shown. |
| Status | names, locations and figure content: verified; correspondence between the sets: assumption, put as a question |
| Severity | minor |
| Source | S2, AB |

**GB-15 The stated length, area, thickness and volume of the landslide do not fit together or the maps, and the two stated volumes differ by a factor of 75.6.**

| Field | Content |
|---|---|
| Check | P1, P2, P13, P27, P3 |
| Location | p. 7, l. 149 to 151; p. 9, l. 173 to 174; p. 9, l. 181 to 182; p. 13, Table 2, column "Volume"; p. 6, Fig2(c) landslide boundary and scale bar; p. 10, Fig4 label "1021m"; p. 5, l. 110 to 112 |
| Quotation | "about 450 m long, about 1000 m wide along the river, and a planar area of 0.45 km2. The average thickness of the landslide mass is about 100 m, and the volume is about 2400×104 m3"; "The length of the landslide mass in the sliding direction is 1021 m"; "the volume of the landslide is 317563 m3" |
| Concern | The field description gives every dimension needed for a cross-check. (a) 450 m × 1000 m = 0.45 km² is consistent, but 0.45 km² × 100 m = 4.5 × 10^7 m³ = 4500 × 10^4 m³, not 2400 × 10^4 m³; the stated volume implies a mean thickness of 53.3 m. The product equals the volume that Zhao et al. (2021), which is in the list but never cited, give in their abstract (about 4500 × 10^4 m³, 450 m long and 1000 m wide); 4500 / 2400 = 1.875. (b) The modelled volume of 317563 m³ (l. 182) is 1/75.6 of 2400 × 10^4 m³ (1.3 %). Spread over 25345 blocks it gives 12.5 m³ per block, while the ten monitored blocks in Table 2 hold 756.2 to 1754.3 m³ (mean 1151.3 m³); 2400 × 10^4 m³ / 25345 = 947 m³ per block matches the order of Table 2. (c) The length of 450 m conflicts with 1021 m "in the sliding direction" (l. 173 to 174, Fig4). The slope segments of l. 151 to 156 imply a horizontal length of 914 to 1250 m. Measured with the scale bar of Fig2(c), the landslide boundary extends 1221 m along a-a' and 1028 m across, encloses 0.97 km², and the deposit Q4del measures 654 m × 987 m and 0.47 km²: 0.45 km² fits only the deposit, 450 m fits no outline. (d) The casualty figure "tens of thousands of people drowned" (l. 111 to 112) is given without source; Zhao et al. (2021) report over 100 000 deaths. Possible resolutions: A, 317563 m³ is a typing error and the model holds about 2.4 × 10^7 m³; B, 317563 m³ is a sub-volume and the simulated volume is not stated; C, "450 m long" refers to another feature. Because the mass enters every energy value (GB-38) and in case B the simulated landslide would be 1.3 % of the real one, against which the claimed agreement of deposit extent (l. 357 to 359) could not be expected, the finding changes what the results can show. |
| Suggestion | In Section 2.1 (l. 149 to 151, l. 181 to 182) state the mapped volume, the restored source volume (restored minus present DEM) and the simulated volume separately, with the number of blocks of slide mass and base; say which outline (source area, deposit, whole landslide) l. 149 to 150 describe and correct length and area; recheck 0.45 km² × 100 m against 2400 × 10^4 m³; name the source of the dimensions and of the casualty figure in l. 110 to 112 (Zhao et al., 2021, if that is where they come from). |
| Status | values in text, Table 2 and Fig4: verified (page images p. 5, 7, 9, 10, 13); Fig2(c) dimensions: verified by measurement with the scale bar (instance AB); values of Zhao et al. 2021: verified at abstract level; quotients and segment lengths: inferred; that the dimensions were taken from Zhao et al. 2021: assumption, put as a question; resolutions A to C: assumption |
| Severity | major |
| Source | S1, S3, AB, SD |

**GB-16 The contour restoration is offered as a new method and as Conclusion 1, but the restored surface is not tested against independent evidence.**

| Field | Content |
|---|---|
| Check | P10 |
| Location | p. 7, l. 157 to 162; p. 6, l. 138 to p. 7, l. 143; p. 2, l. 49 to 51; p. 1, l. 16 to 17; p. 9, Fig3(c); p. 25, l. 463 to 468 |
| Quotation | "the mountains become continuous, which can be regarded as the terrain before the landslide" |
| Concern | The restoration step is documented with a clear flow (Fig1, Fig3). A methodological claim ("a new idea", l. 50; Conclusion 1) needs a test, but the only check is visual continuity (l. 160 to 162). No restored volume is compared with the deposit volume or with the field estimate of l. 151 (GB-15), no uncertainty band is given for the straightening, and no case with known pre-failure terrain is used. Every block geometry, every mass and therefore every result of Section 3 depends on the restored surface. |
| Suggestion | Counter-design for Section 2.1: apply the same contour straightening to a landslide with a pre-event DEM (for example a recent co-seismic landslide with pre- and post-event survey) and report vertical and volume errors; for Mogangling, compare the depleted volume (restored minus present surface in the source area) with the deposit volume (present minus restored surface in the deposit area, corrected for bulking) and with published estimates; report a range from two or three admissible contour variants and carry it into the simulation. |
| Status | verified |
| Severity | major |
| Source | SD |

**GB-17 The text names two section lines, a-a' and b-b', in Fig2(c), but Fig2(c) and Fig3(b) show only a-a', and the profile has no axis titles.**

| Field | Content |
|---|---|
| Check | P38, P4, P3, P29 |
| Location | p. 7, l. 159 to 160; p. 6, Fig2(c) section line; p. 8, Fig3(b) title, axes and symbol "80°" |
| Quotation | "As shown in Fig3. (b), make a section along a-a'and b-b' in Fig2. (c). The results are shown in Fig3. (c)." |
| Concern | Fig2(c) contains one red section line, labelled "a" at the west end and "a'" at the east end (checked on a 400 dpi render; one instance had read both ends as "a", the render shows the prime). Fig3(b) is titled "(a-a')" and shows one profile; b-b' appears in no figure. The profile's vertical axes carry 1000 to 2000 and its horizontal axis 0 to 1500 without quantity or unit, and the symbol "80°" is not explained. The sentence also says "The results are shown in Fig3. (c)", although Fig3(c) shows contours and terrain before and after modification in plan view, not section results. |
| Suggestion | In l. 159 to 160 delete "and b-b'" or add the line b-b' to Fig2(c) and its profile to Fig3(b); reword to "Fig3(b) shows the profile along a-a' in Fig2(c); Fig3(c) compares the contours and terrain before and after restoration."; label the profile axes, for example "Elevation (m)" and "Distance along a-a' (m)", and explain the dip symbol. |
| Status | verified (page images p. 6 to 8, 400 dpi crop of Fig2(c)) |
| Severity | minor |
| Source | S2, S4, AB |

**GB-18 The 3DEC model cannot be rebuilt from the text: damping, block type and zoning, internal joint geometry and the origin of each parameter are missing.**

| Field | Content |
|---|---|
| Check | P8 |
| Location | p. 9, l. 175 to 182; p. 10, l. 193 to 203; p. 11, l. 206 to 212; p. 11, Table 1; p. 13, Table 2, column "Volume"; p. 10, Fig4 legend |
| Quotation | "The landslide mass is evenly divided into 8.7 m×8.7 m blocks on the xoy surface. The height is determined by the vertical height from the surface of the landslide mass to the sliding bed. A uniform structural plane is set inside."; "the selection of physical-mechanical parameters was based primarily on laboratory testing, empirical analogy, and parameter inversion" |
| Concern | Boundary conditions and staging are described well (l. 193 to 202). Not reproducible: (1) mechanical damping in the static and dynamic stage; (2) rigid or deformable blocks, zone size, time step, static equilibrium criterion; (3) orientation and spacing of the "uniform structural plane"; Table 2 volumes divided by 8.7 m × 8.7 m give block heights of 10.0 to 23.2 m, whereas l. 178 to 179 implies one block per column through a mass about 100 m thick (l. 150 to 151), so the vertical subdivision is not described; (4) which value in Table 1 comes from which source, which laboratory tests, and which observation the parameter inversion was fitted to; (5) the assignment of the two rock-mass sets of Table 1 to the units of Fig4 (GB-11). The history of the maximum unbalanced force is not shown (GB-27). Question to the authors: the joint shear stiffness exceeds the normal stiffness for both joint sets (1500 against 960 GPa/m and 180 against 100 GPa/m); is this intended? |
| Suggestion | Add to Section 2.1 a model table with block type, zone size, joint geometry inside the mass, damping type and values, time step and equilibrium criterion, and add to Table 1 a source column for each parameter (test, analogy with citation, or inversion with target). |
| Status | missing items and computed block heights: verified; stiffness ratio as intended or not: assumption, put as a question |
| Severity | moderate |
| Source | SD |

**GB-19 The discontinuities appear under seven names, and the manuscript does not say which Table 1 row belongs to which, nor how they relate to the structural plane that is said to be ignored.**

| Field | Content |
|---|---|
| Check | P38 |
| Location | p. 9, l. 176 to 180; p. 11, l. 209 to 210; p. 11, Table 1, column "Discontinuities"; p. 15, l. 308 to 310, l. 313, l. 320 |
| Quotation | "the impact of the structural plane on the landslide process has to be ignored in this study"; "The discontinuities are represented by both fully developed potential rupture planes and joint sets" |
| Concern | Names found: "structural plane" of the landslide mass, ignored (l. 176 to 178); "A uniform structural plane is set inside" (l. 179 to 180); "potential rupture planes" and "joint sets" (l. 209 to 210); Table 1 "discontinuities" and "potential discontinuities"; in the results "steeply dipping structural planes" (l. 308 to 309), "pre-existing potential sliding surfaces" (l. 313) and "potential failure planes" (l. 320). The pairing potential discontinuities = potential rupture planes and discontinuities = joint sets is plausible but not stated, and it is not stated whether the uniform structural plane is one of the two Table 1 sets or the block contacts of the 8.7 m subdivision. The results then attribute the failure to structural planes that the methods say were not modelled (content treated in GB-33). Question to the authors: are these names one object, two objects or more, and where are they located in the model? |
| Suggestion | In Section 2.1 (l. 176 to 180, l. 209 to 212) define each discontinuity type once, map it to a Table 1 row, show its position (for example in Fig4), and use the same terms in Section 3.1 (l. 308 to 320). |
| Status | the seven names and their locations: verified; whether they denote the same objects: assumption, put as a question |
| Severity | moderate |
| Source | S2 |

**GB-20 The input motion is a proxy record whose choice rests on an uncited statement that conflicts with the manuscript's own tectonic description, and its influence is not tested.**

| Field | Content |
|---|---|
| Check | P27, P9 |
| Location | p. 10, l. 183 to 191; p. 10, Fig4 inset; p. 5, l. 97 to 99; p. 5, l. 110; p. 29, l. 600 to 602 |
| Quotation | "It is worth noting that both the Mogangling landslide and the Wenchuan earthquake zone belong to the tectonic system of the Longmenshan Fault Zone. Extensive research indicates that the Kangding earthquake is comparable to the 2008 Wenchuan earthquake in terms of damage distribution, affected intensity, and estimated magnitude." |
| Concern | The manuscript discloses the lack of a 1786 record at the right place (l. 183 to 186). The consequences are not drawn. (1) "Extensive research" carries no citation; no reference is cited anywhere after l. 63. (2) l. 97 to 99 place the site at the intersection of the Xianshuihe, Longmenshan and Anninghe faults, l. 110 gives Ms 7¾ and the reference list titles the event "the 1786 Moxi M 7.75 earthquake" (l. 600 to 601), while the listed Wang et al. (2014, 2021) give Wenchuan as M8.0; 10^(1.5 × 0.25) = 2.37 in radiated energy. Feng et al. (2023) identify faults of the Xianshuihe system (Moxi segment) as the source of the 1786 event. (3) The record as plotted in the Fig4 inset has amplitudes of about ±100 gal (0.10 g), with peaks up to about 150 gal; no component, scaling, duration, filtering or baseline correction is stated (provenance of the record: GB-21), nor whether it was scaled to the near-field intensity of an M 7¾ event at the site. (4) No run with another motion is reported, although stage velocities (l. 307 to 346), timing and the failure narrative depend on the input. Question to the authors: what was the distance of the Luding station to the 2008 rupture? |
| Suggestion | In Section 2.1 cite the sources for the comparison, state component, PGA, duration, processing and any scaling of the record, and justify it against the 1786 rupture. Counter-design: a small suite of input motions (recorded near-field records scaled to the site intensity, or synthetic motions for an M 7¾ strike-slip rupture at the site distance), reporting how runout, peak velocity, timing and the energy curves vary. Literature: Feng, J., Chen, L., Han, M., Gao, S., Li, Y., Lu, L., and Chen, S. (2023): Multi-fault rupture behavior of the 1786 M 7¾ Kangding earthquake on the eastern margin of the Tibetan Plateau, Front. Earth Sci., 11, 1140326, https://doi.org/10.3389/feart.2023.1140326 (not in the reference list). |
| Status | uncited statement, internal fault description, amplitudes on the page image, missing processing details and missing sensitivity: verified; Feng et al. 2023: verified at abstract level (instance SD; title and DOI confirmed in a search during the merge); distance and far-field character of the Luding record: assumption, put as a question |
| Severity | major |
| Source | SD |

**GB-21 External data sources used in the Methods are given without provenance, citation or access route.**

| Field | Content |
|---|---|
| Check | P12 |
| Location | p. 10, l. 189 to 191 and Fig4 inset; p. 6, Fig2(b), caption l. 126 to 127; p. 6, Fig2(c); p. 8, Fig3(b); p. 9, l. 180; p. 6, l. 136 to 137; p. 11, l. 206 to 207; p. 26, l. 505 to 506 |
| Quotation | "this study adopts the acceleration records measured at the Luding station during the Wenchuan earthquake as the input ground motion for the dynamic numerical simulation analysis of the Mogangling landslide" |
| Concern | The data statement (l. 505 to 506) does not say whether third-party data are included or how they can be obtained. (a) The Luding record drives the whole dynamic simulation; network or operator, component, record identifier, scaling or filtering and access route are not given, and no source is cited at l. 189 to 191 or in the Fig4 caption (l. 192). (b) The image in Fig2(b): provider, acquisition date and licence are not given. (c) The engineering geological map Fig2(c), the profile Fig3(b) and the "geological engineering drawing" (l. 180) are neither declared as the authors' own mapping nor cited. (d) The records on the Tiezhuang Temple tablet (l. 136 to 137) carry no citation. (e) The laboratory tests on which Table 1 is "based primarily" (l. 207) are not reported. The missing 1786 record is disclosed (l. 183 to 186) and not raised again; raised is the missing provenance of the substitute and of the other sources. |
| Suggestion | In Section 2.1 cite the strong-motion data source with station code, component and processing (l. 189 to 191); add source and date of the image to the Fig2 caption (l. 126 to 127); state the origin of Fig2(c) and Fig3(b) and cite the tablet (l. 136 to 137); report or cite the laboratory tests (l. 206 to 207); and name all these items with access route or licence restriction in "Availability of data and material" (l. 505 to 506). |
| Status | verified |
| Severity | moderate |
| Source | S2 |

**GB-22 In Fig4 the legend abbreviations and the inset accelerogram are not explained.**

| Field | Content |
|---|---|
| Check | P29 |
| Location | p. 10, Fig4 legend and inset; caption l. 192; l. 189 to 191 |
| Quotation | "Fig4. Discrete numerical model with fine topography" |
| Concern | The inset is the only display of the seismic input. Its ordinate "Acceleration (gal)" has values (-100, 0, 100), but the abscissa has no title, unit or values, and the four time markers tp, tPGA, tf and te are not defined in figure, caption or text. The legend symbols γo2, Q del and γM2 are not expanded (names in GB-11). |
| Suggestion | Expand the abbreviations in the caption (l. 192); give the inset a time axis with unit, the record name, component and any scaling; define tp, tPGA, tf and te. |
| Status | verified |
| Severity | minor |
| Source | AB |

**GB-23 The abscissa of the velocity curves from which effective collisions are detected is called travel distance, travel displacement and displacement.**

| Field | Content |
|---|---|
| Check | P38 |
| Location | p. 11, l. 220 to 221, l. 225, l. 227, l. 234; p. 12, Fig5(a) and Fig5(b) to (f) x axes; p. 23, Fig10(b) x axis; p. 1, l. 22 to 23; p. 25, l. 473 to 475 |
| Quotation | "the local peak value of the displacement velocity curve"; "effective block collisions during the landslide can be identified by extracting local peaks from displacement-velocity curves" |
| Concern | Fig5(a) "Travel distance (m)"; Fig5(b) to (f) "Travel Displacement (m)"; Section 2.2 "velocity-travel-distance curve" (l. 221), "velocity-distance profile" (l. 225), "velocity-distance curve" (l. 227), "travel-distance versus velocity profile" (l. 234); Abstract "displacement velocity curve" (l. 23); Conclusion 2 "displacement-velocity curves" (l. 474); Fig10(b) "Travel distance (m)". Distance travelled along the path and displacement are different quantities, and for blocks that rebound (l. 397 to 398, l. 416) they diverge; peak prominence and therefore the count of effective collisions depend on the abscissa. As a pure naming issue this would be minor; it is moderate because the name may hide a different quantity in the detection step. Question to the authors: which quantity was used? |
| Suggestion | State in Section 2.2 (l. 220 to 221) which quantity forms the abscissa and use that term throughout; if it is travel distance, write in l. 22 to 23 "the local peaks of the velocity versus travel-distance curve", in l. 474 "local peaks from velocity versus travel-distance curves", and label the x axes of Fig5(b) to (f) "Travel distance (m)". |
| Status | names and locations: verified; that the two quantities differ for the analysed block: assumption, put as a question |
| Severity | moderate |
| Source | S2, S1, S4, AB, SD |

**GB-24 The count of 1,139 effective collisions has no stated threshold reference, population or validation, and it does not match the counts in Fig5(d) or Fig10(b).**

| Field | Content |
|---|---|
| Check | P20, P22, P3, P8, P32 |
| Location | p. 11, l. 227 to 234; p. 12, Fig5(a), Fig5(b) to (f), Fig5(d); p. 23, Fig10(b), axis "Frequency"; p. 22, l. 414 to 415 |
| Quotation | "a suitable prominence threshold must be chosen-one that quantifies each peak’s standout height, width, and position relative to adjacent peaks"; "At a threshold of 30%, however, the identification of effective collisions is deemed acceptable. Under this setting, 1,139 effective collisions were detected from the travel-distance versus velocity profile." |
| Concern | The threshold sweep in Fig5(b) to (f) shows how the choice changes the detections. Still: (a) the percentages have no reference (peak velocity, curve range, neighbouring peak height), it is not said how width and position enter, which software performed the detection, or by which criterion 30 % is "acceptable"; (b) "the travel-distance versus velocity profile" is singular: Fig5(a) is "a typical velocity-travel-distance curve for an individual block" (l. 221) with about 13.5 m/s and 580 m travel, while Fig5(b) to (f) show a profile reaching about 45 m/s and about 2400 m (GB-35), and the block or set behind Fig5(b) to (f) and behind 1,139 is not named; (c) Fig5(d), threshold 30 %, shows about 130 red markers (±20, counted on enlargements); Fig10(b) shows 26 points at 100 m spacing whose values sum to 1213 ± 10 (measured), 74 more than 1,139, and its ordinate "Frequency" has no unit, bin width or population; (d) no detected collision is checked against the contact record of the DEM, so false positives and missed collisions are not estimated. |
| Suggestion | In Section 2.2 (l. 227 to 234) define the prominence measure as a formula, name the tool, state which blocks the 1,139 collisions come from and how they relate to Fig5(d) and Fig10(b), and give the count per monitored block; define ordinate, bin width and population of Fig10(b) in its caption (l. 423 to 424); validate the detector on a sample by comparing detected peaks with contact events of the same blocks and report precision and miss rate per threshold. |
| Status | missing definitions: verified (text, page images p. 11, 12, 23); counts in Fig5(d) and Fig10(b): verified by counting and measurement (instance AB), sum read independently by S3 and SD at about 1,213 to 1,223; relation between the three numbers: inferred |
| Severity | moderate |
| Source | S3, AB, SD |

**GB-25 The stated reference datum of the potential energy cannot produce the initial energies of the ten blocks in Fig9; the data imply a different datum for each block.**

| Field | Content |
|---|---|
| Check | P2, P22, P3, P8 |
| Location | p. 13, l. 252 to 255; p. 13, Table 2, columns "Coordinate" and "Volume"; p. 21 to 22, Fig9(a) to (j), first bar; p. 20, Fig8; p. 23, Fig10(a), Z axis |
| Quotation | "Since the initial velocity is 0, ME(t0) reduces to the initial potential energy."; "the potential-energy calculation uses the model’s initial height as the reference datum rather than true sea level; only the change in potential energy due to relative displacement is considered." |
| Concern | Table 2 gives coordinates and volumes, so the datum can be back-calculated. With the measured initial totals of Fig9 (5.06, 5.13, 4.01, 3.57, 11.08, 6.59, 1.18, 4.37, 1.59, 0.95 GJ for blocks 1 to 10), ρ = 2300 kg/m³ and h = PE0 / (ρ V g), the implied heights above datum are 239, 223, 235, 164, 316, 173, 30, 193, 82 and 44 m, and the implied datum z - h ranges from 101 m (block 1, z = 340) to 711 m (block 10, z = 755). The top blocks 9 and 10 carry about 806 and 427 J/kg, the bottom blocks 1 and 2 about 2341 and 2184 J/kg, the reverse of their elevations. Read literally, "the model's initial height" as datum makes PE(t0) zero, but Fig8 and every panel of Fig9 start at their maximum PE and fall to about zero. A separate datum per block at its lowest point would fit the curves but not the text. Fig10(a) adds a question: its Z axis runs below -840 m; a monitored block descending 840 m would release at least 756.2 m³ × 2300 kg/m³ × 9.81 m/s² × 840 m = 14.3 GJ, more than the largest PE0 in Fig9 (11.08 GJ); this point is inferred, because a 3-D projection cannot be read exactly. The density used per block and the coordinate frame of Table 2 (x from -79 to -719, z from 340 to 755, which fits neither the axes of Fig4 and Fig6 nor those of Fig11) are not stated. Possible causes: (i) a datum per block; (ii) Fig9 panels or Table 2 IDs assigned to the wrong blocks; (iii) other volumes or densities than stated. Which one applies? |
| Suggestion | In Section 2.3 (l. 253 to 255) state the datum actually used (one common reference level, or each block's lowest elevation), the mass per block and the formula applied, keep it the same for Fig8 and Fig9, give the coordinate frame of Table 2, and add the initial and final elevation and the initial PE of each block to Table 2; if cause (ii) applies, correct the assignment in the Fig9 caption. |
| Status | text and Table 2 values: verified; PE0 in Fig9: verified by measurement (instance AB; S3 and SD read the same values within 0.1 GJ at the gridlines); implied heights and datum: inferred; the cause: assumption, put as a question |
| Severity | moderate |
| Source | S3, AB, SD |

**GB-26 The four position classes of the monitoring points are named differently in the text, Table 2 and Fig6, Fig6 swaps the two middle labels, and the points carry no IDs.**

| Field | Content |
|---|---|
| Check | P38, P3, P29 |
| Location | p. 13, l. 256 to 257; p. 13, Table 2, column "Position"; p. 14, Fig6 labels, markers and axes, caption l. 268 |
| Quotation | "ten monitoring points were installed in the lower, lower-middle, upper-middle, and upper portions of the slide mass" |
| Concern | Text: lower, lower-middle, upper-middle, upper. Table 2: bottom, lower middle part, upper middle part, top. Fig6 reads from upslope downwards "Top", "Lower middle part", "Upper middle part", "Bottom". The dashed lines split the points 2, 3, 3, 2, and the Table 2 elevations rise from bottom (z 340, 355) through lower middle (465 to 498) and upper middle (660 to 692) to top (752, 755), so the band below "Top" must be the upper middle part. The ten coloured points have no IDs or colour key, so they cannot be linked to Table 2, Fig9, Fig10(a) or "Block 1 and Block 3" (l. 397). The axes carry values without quantity or unit. |
| Suggestion | Use the Table 2 terms in l. 256 to 257; swap the two middle labels in Fig6; write the ID next to each point or add a colour key consistent with Fig10(a); label the axes x (m), y (m), z (m) as in Fig4. |
| Status | names, label order, counts per zone and Table 2 values: verified; that the upper part of Fig6 is upslope: inferred from Table 2 elevations and the same view in Fig4 |
| Severity | minor |
| Source | S2, AB |

**GB-27 Several monitored quantities announced in the Methods are not reported, including the maximum unbalanced force meant to verify the end state.**

| Field | Content |
|---|---|
| Check | P11 |
| Location | p. 13, l. 258 to 264; p. 13, Table 2, column "Monitoring contents" and row ID 11; p. 3, l. 81 to 82; p. 15 to 16, Section 3.1; p. 19 to 22, Section 3.2 |
| Quotation | "In addition, the maximum unbalanced force was tracked to verify that the model reached post-failure stability."; "For the local analysis, displacement, velocity, and stress histories were extracted for each of the ten monitored blocks" |
| Concern | Table 2 lists clearly what was recorded: 10 blocks × 9 quantities (displacement, velocity and stress components) plus the unbalanced force (ID 11). In the Results velocity enters only through KE (Fig9) and displacement only as trajectories (Fig10(a)); the stress components of the blocks appear in no figure or text passage, and the maximum unbalanced force is not shown or quantified anywhere ("unbalanced" occurs only in l. 258 and Table 2). Section 3.1 cites the stress maps Fig7(h) to (n) but gives numbers only for velocity (5.9, 19.6, 27.1, 31.6, 25.7 m/s); the "stress variations of the entire slide mass" (l. 260) are not quantified. The convergence check of the static stage and of the end state is therefore not documented. |
| Suggestion | In Section 3.1 or a supplement add the history of the maximum unbalanced force with the convergence criterion and the stress histories of the monitored blocks, or remove these quantities from Table 2 and l. 258 to 264. |
| Status | verified (text search and page images) |
| Severity | moderate |
| Source | S3, SD |

**GB-28 The claim that α = 1 "ensures a tight fit" at all time steps is untested, and the input points and the unit of α are not stated.**

| Field | Content |
|---|---|
| Check | P26, P8 |
| Location | p. 14, l. 272 to 284; p. 1, l. 23 to 24; p. 23 to 24, Fig11(a) to (j) |
| Quotation | "this study uniformly sets the α value to 1. This approach ensures a tight fit of the envelope model while minimizing geometric deviations introduced by parameter tuning." |
| Concern | The guarantee is claimed for all time points, but the point spacing changes as the mass spreads (Fig11 shows the mass growing to more than 2000 m in plan). Whether α is a radius in metres or another convention, and which points enter (block centroids, block vertices, or a "3D point cloud" as in l. 24), is not stated; with blocks of 8.7 m an α of 1 m on centroids would not enclose the mass, so a different convention seems to be used. No sensitivity of VS and AG to α is reported, although l. 281 states that α "directly affects" the result. Question to the authors: does a fixed α over- or under-enclose the spread deposit? |
| Suggestion | In Section 2.4 name the implementation, the α convention and unit and the input points; show VS and AG for two or three α values at early and late time points (reference values V0 and S0: GB-30). |
| Status | missing definitions and sensitivity: verified; behaviour of a fixed α with spreading: assumption, put as a question |
| Severity | moderate |
| Source | SD |

**GB-29 The two dispersion indices VS and AG appear under several names and two area symbols, and "rate" suggests a quantity per unit time that Eq. (5) and (6) do not define.**

| Field | Content |
|---|---|
| Check | P38 |
| Location | p. 14, l. 274 to 275, Eq. (5) and (6) l. 276 to 277, l. 278 to 280; p. 1, l. 25; p. 3, l. 89; p. 4, Fig1 lowest panel; p. 15, l. 287 to 288; p. 24, l. 440 to 441; p. 25, l. 453 to 454, Fig12(a), (b) x axes, caption l. 458 to 459; p. 26, l. 488 |
| Quotation | "two dimensionless indices are introduced: volume swelling (VS) and area growth (AG)"; "we first extracted its volume (V) and surface area (A) at each time point, based on which the volume expansion rate (VS) and surface area growth rate (AG) were calculated" |
| Concern | Counts in the body text: "volume swelling" 2 (l. 275, l. 287 to 288), plus Fig1 and the Fig12(a) axis; "volume expansion rate" 4 (l. 25, l. 89, l. 441, l. 453); "volume expansion" 1 (l. 488); Fig12 caption "as a function of volume". For AG: "area growth" 2, plus Fig1 and the Fig12(b) axis; "area growth rate" 1 (l. 25); "surface area growth rate" 2 (l. 89, l. 441); "surface area growth" 2 (l. 453, l. 488); Fig12 caption "as a function of area". Eq. (6) uses S0 and St, l. 440 uses A. Eq. (5) and (6) define a relative change in percent, not a rate. |
| Suggestion | Use "volume swelling (VS)" and "area growth (AG)" throughout (l. 25, l. 89, l. 441, l. 453, l. 488) and drop "rate"; in l. 440 write "its volume (V) and surface area (S)"; in l. 441 "the volume swelling (VS) and area growth (AG)"; change the Fig12 caption (l. 458 to 459) to "(a) as a function of volume swelling (VS); (b) as a function of area growth (AG)." |
| Status | verified |
| Severity | minor |
| Source | S2, S3, S4, AB |

**GB-30 The reference values V0 and S0 of VS and AG belong to a different object than Vt and St, none of the four is reported, and the enveloped body has seven names.**

| Field | Content |
|---|---|
| Check | P38, P20, P22 |
| Location | p. 14, l. 276 to 280; p. 14, l. 269 to 272; p. 3, l. 88; p. 4, Fig1 lowest panel; p. 23, l. 427, l. 429; p. 24, l. 440 to 441, l. 451 to 452; p. 25, l. 453 to 454, Fig12 caption l. 458; for comparison p. 20, Fig8 and p. 21 to 22, Fig9 |
| Quotation | "V0 denotes the initial volume of the landslide mass (m³); Vt denotes the volume of the enclosing envelope at time t (m³); S0 denotes the initial surface area of the landslide mass (m²); St denotes the surface area of the enclosing envelope at time t (m²)."; "the sharp rise of DE shown in the figure further confirms significant fragmentation and disintegration in the monitored block group" |
| Concern | The indices are defined as dimensionless ratios, which makes them comparable across time. But (a) V0 and S0 belong to "the landslide mass", Vt and St to "the enclosing envelope". At t = 0 the envelope (α = 1) and the block assembly need not have the same volume and area, so part of the reported growth may be the difference between two measures. Both Fig12 panels start at 0 %, which suggests that V0 and S0 are the envelope values at t = 0, but the text does not say so; if V0 were a block volume (317563 m³, l. 182, or 2400 × 10^4 m³, l. 151; GB-15), VS would not start at 0. (b) VS = 29.47 % means Vt / V0 = 1.2947 and AG = 319.5 % means St / S0 = 4.195, but no absolute volume or area is given anywhere, so the reader cannot check whether such a pair is geometrically plausible. (c) The enveloped body is called "landslide accumulation area" (l. 88, heading l. 269, Fig1), "landslide deposition zone" and "deposition zone" (l. 270, l. 272), "slide mass" (l. 272), "landslide mass" (l. 88, l. 278 to 279), "deposit mass" (l. 427), "deposit region" (l. 429) and "sliding mass" (Fig12 caption); at t = 0 (Fig11(a)) it is the intact source mass. (d) Fig12 starts with PE above the 6000 GJ tick, the level of Fig8 for the entire sliding mass, while the y-axis maxima of the ten Fig9 panels add up to 50.7 GJ (0.845 % of 6000 GJ); Fig12 therefore shows the whole mass, and "monitored block group" in l. 452 names a different object. |
| Suggestion | In Section 2.4 (l. 269 to 280) name the body once (for example "sliding mass") and use that name in l. 88, l. 427, l. 429, l. 452, Fig1, Fig11 and Fig12; define V0 and S0 as envelope volume and area at t = 0 or justify the mixed definition; replace "monitored block group" in l. 452; report V0, S0 and the envelope values at each time (table proposed in GB-42). |
| Status | definitions, names, absence of values, start of Fig12 at 0 % and above 6000 GJ, Fig9 axis maxima: verified; ratios and the reading of V0 from the 0 % start: inferred |
| Severity | moderate |
| Source | S2, S3 |

#### Minor corrections

| ID | Location | Quotation | Replacement | Source |
|---|---|---|---|---|
| KK-04 | p. 2, l. 76 to p. 3, l. 77 | "the research method involves three parts" | "the research method involves four parts" (four items (1) to (4) in l. 77 to 90 and four rows in Fig1) | S3, S4, AB, SD |
| KK-05 | p. 5, l. 98 | “"Y" - shaped faults” | "Y-shaped faults" | S4 |
| KK-06 | p. 5, l. 110 | "(Ms7 ¾)" | "(Ms 7¾)" | S4 |
| KK-07 | p. 6, Fig2(b) legend | "Daduhe River" | "Dadu River" | S2, AB |
| KK-08 | p. 7, l. 151 | "the volume is about 2400×104 m3" (exponent printed at full size on the baseline) | "the volume is about 2400 × 10⁴ m³" (the value itself: GB-15) | S3, S4 |
| KK-09 | p. 7, l. 152 | "1120 m-1330m is the front edge" | "1120 to 1330 m is the front edge" | S4 |
| KK-10 | p. 7, l. 153, l. 154, l. 156 | "about 50°; The elevation"; "about 5-12°; The elevation"; "about 57°; The elevation" | "about 50°; the elevation"; "about 5-12°; the elevation"; "about 57°; the elevation" | S4 |
| KK-11 | p. 8, Fig3(a) legend and Fig3(b) legend | "Dadu river" | "Dadu River" | S2 |
| KK-12 | p. 9, l. 176 to 177 | "can not be obtained" | "cannot be obtained" | S4 |
| KK-13 | p. 9, l. 182 | "1121m high" | "1121 m high" | S4 |
| KK-14 | p. 11, l. 218; l. 228 | "increase block velocities-hereafter termed"; "must be chosen-one that quantifies" | "increase block velocities, hereafter termed"; "must be chosen, one that quantifies" | S4, SD |
| KK-15 | p. 12, Fig5(a) legend | "Non-obvios acceleration" | "Non-obvious acceleration" | AB |
| KK-16 | p. 13, l. 246 | "where, at time ti, PE(ti), and DE(ti) can be expressed as:" | "where, at time ti, KE(ti), PE(ti) and DE(ti) can be expressed as:" | S4, SD |
| KK-17 | p. 13, l. 251 | "(m/s);h(ti)" | "(m/s); h(ti)" | S4 |

#### Verification log

| ID | Check | Checked | Values | Result |
|---|---|---|---|---|
| PP-05 | design sketch | Questions, study type, data sources, time axis, environment, declared principles, disclosed limitations and chain from aims to results, whole manuscript | Single case study; no research questions or hypotheses; no comparison condition: one parameter set, one input motion, one restoration, threshold 30 %, α = 1; 25345 blocks, 10 monitored blocks, 10 envelope times; one run of 131 s simulated time; disclosed limitations: structural planes ignored (l. 175 to 178), no 1786 record (l. 183 to 191), smooth restoration (l. 160 to 162), dam break not modelled (l. 349 to 350), weathering (l. 354 to 355), DE artefact (l. 399 to 402); no discussion section, no outlook | Sketch complete; findings GB-04, GB-16, GB-20, GB-33, GB-36, GB-37, GB-40, GB-44 |
| PP-06 | P13 | Uncited statements: "nearly 20 large and super large earthquake landslides" (l. 99 to 100), "burst the Dadu River after 9 days" (l. 110 to 111), Tiezhuang Temple tablet (l. 136 to 137), 3DEC as "one of the most widely used numerical methods" (l. 169 to 170), "Extensive research indicates" (l. 187 to 189) | No source named at any of these places; the abstract of Zhao et al. 2021 gives no duration of the blockage | no finding under P13 (no cited source to compare); treated in GB-20, GB-21, GB-48 |
| PP-07 | P38 | Name of the triggering earthquake | "Kangding earthquake" l. 110, l. 183, l. 188; "1786 Moxi M 7.75 earthquake" only in the reference title l. 600 to 601; Ms 7¾ (l. 110) equals 7.75 | no finding |
| PP-08 | P38 | Names of landslide, river and fault | "Mogangling" consistent; "Dadu River" 13 times in the body; "Dadu River fault (Detuo fault)" explained at l. 147 | no finding apart from KK-07 and KK-11 |
| PP-09 | P3 | Direction and width of the landslide in Fig2(c) against l. 148 to 149 | a-a' azimuth 74° with north up, text 75°; width across a-a' 1028 m, text "about 1000 m wide" | no finding (length and area: GB-15) |
| PP-10 | P1 | Derived numbers of Section 2.1, Table 1 and Table 2 | 450 m × 1000 m = 0.45 km²; Table 2 volumes sum 11,512.7 m³, mean 1151.3 m³, range 756.2 to 1754.3 m³; Poisson ratios from Table 1 bulk and shear moduli 0.22 (bed rock) and 0.26 (landslide mass); slope of the modelled mass atan(747 / 1021) = 36.2° | no finding (other derived values: GB-15) |
| PP-11 | P3 | Fig4 dimension labels against l. 173 to 175 | Labels "1021m", "747m", "179m", "131m"; text 1021 m, about 747 m, 179 m, about 131 m; axes x (m), y (m), z (m) present | no finding |
| PP-12 | P3 | Fig5(a) legend against l. 221 to 224 | Red "Effective collisions (Significant acceleration stage)", purple "Non-obvios acceleration"; text "red or purple markers", pronounced peaks "highlighted in red" | no finding (spelling: KK-15) |
| PP-13 | P38 | Threshold labels of the collision detection | l. 230 to 232: 10, 20, 30, 40, 50 %; Fig5 caption (b) to (f): threshold = 10 % to 50 % | no finding |
| PP-14 | P38 | Energy abbreviations | KE, PE, DE, ME defined l. 241 to 243; used identically in Eq. (1) to (4), Fig1, Fig8, Fig9, Fig12; "dissipated energy" 9 times, "dissipation energy" 2 times | no finding apart from KK-01 |
| PP-15 | P38 | IDs of the monitored blocks | Table 2 ID 1 to 10 plus 11 (maximum unbalanced force, explained l. 258 to 259); Fig9 caption "point 1" to "point 10"; Fig10(a) legend 1 to 10; l. 397 "Block 1 and Block 3"; link given by the Table 2 caption | no finding (labels in Fig6: GB-26) |
| PP-16 | P2 | Number of monitoring points and time sets across text, tables and captions | 10 points in l. 256, l. 262, l. 392, l. 403, Table 2 caption, Fig6, Fig9, Fig10; position groups bottom (1, 2), lower middle (3 to 5), upper middle (6 to 8), top (9, 10); Fig7 caption 7 times for 7 velocity and 7 stress panels; duration 131 s (l. 300) = last time in Fig7 and Fig11 = end of the Fig8 axis | no finding |
| PP-17 | P3 | Point counts per zone in Fig6 against Table 2 and l. 256 | 10 markers; per zone from the top 2, 3, 3, 2; Table 2: 2, 3, 3, 2 | no finding on the counts (labels: GB-26) |
| PP-18 | P38 | Name and parameter of the alpha-shape algorithm | "Alpha shape" l. 23, "alpha shape" l. 88 to 89, "alpha-shape" l. 272, "Alpha Shape" l. 281 and l. 426, Fig1 "Alpha Shape (α=1)"; α = 1 at l. 283 and in Fig1 | no finding |
| PP-19 | P5 | Own rules against own examples | Block heights from Table 2 and the 8.7 m plan size 10.0 to 23.2 m; Table 2 classes consistent with z; Fig5(d) labelled 30 %; Fig12 VS and AG start at 0 | no further finding beyond GB-15 and GB-18 |
| PP-20 | P37 | Figures or tables with corrected values | No recalculation or correction mentioned; Fig3(c) shows the restored terrain and is labelled so | no finding |
| PP-21 | P17 | Each disclosed limitation against the place of the method | Structural planes l. 175 to 178 (at the method); proxy input l. 183 to 191 (at the method); smooth restoration l. 160 to 162 (at the method); dam break l. 349 to 350; weathering l. 354 to 355; DE artefact l. 399 to 400 (not at Eq. 4) | finding only for the DE artefact (in GB-37); the unresolved consequences of the other limits are in GB-20 and GB-33 |
| PP-22 | P33 | Statements of effort | No statement of effort, run time or computing cost; 131 s is simulated time (l. 300 to 301) | no finding |
| PP-23 | P34 | Counted totals followed by a selection | 25345 blocks, 10 monitored (selection rule: GB-40); 1,139 collisions shown only as binned counts (GB-24); 10 envelope times against about 29 plotted points (GB-42); "nearly 20" landslides (l. 99 to 100) context only | no separate finding |
| PP-24 | P36 | Statements from memory or impression against own records | "about" values in l. 149 to 156 (GB-15); "approximately 20 meters" (l. 328, GB-34); "Extensive research indicates" (l. 187, GB-20) | no separate finding |
| PP-25 | P25 | Information each step needs and where it comes from | Restoration uses the present DEM; input motion from the 2008 record; "field-investigation findings" (l. 265 to 266) used but not described; fragmentation in a model without stated breakage | no separate finding beyond GB-34 and GB-44 |
| PP-26 | P7 | Time axis of the methods against the data | One model version, one run, one threshold and one α for all data; UAV survey date unknown (GB-13) | only GB-42 |
| PP-27 | P29, P3 | Register of figures: number, page, type, caption, first citation | Fig1 p. 4 flow chart, cited l. 76; Fig2 p. 6 maps, l. 93; Fig3 p. 8 to 9, l. 144; Fig4 p. 10, l. 173; Fig5 p. 12, l. 220; Fig6 p. 14, l. 256; Fig7 p. 17 to 19, l. 301; Fig8 p. 20, l. 375; Fig9 p. 21 to 22, l. 393; Fig10 p. 23, l. 414; Fig11 p. 23 to 24, l. 428; Fig12 p. 25, l. 443; no graphical abstract, no appendix figures | Numbering 1 to 12 consecutive; every figure cited in the text of its section; no placeholders or template remnants; no finding |

### Segment 3: Results (p. 15 to 25)

#### Substantive findings

**GB-31 The stress panels Fig7(h) to (n) do not state the stress component or the section shown, and their axes have no titles or units, while the text calls them stress along the sliding plane.**

| Field | Content |
|---|---|
| Check | P29, P3 |
| Location | p. 15, l. 301 to 302; p. 18, Fig7(h) to (n) and colour bars; p. 19, caption l. 368 to 370; p. 9, l. 181 to 182 |
| Quotation | "Fig7 illustrates the cloud maps of velocity distribution for the overall model and stress distribution along the sliding plane" |
| Concern | The panels show a vertical section (abscissa 0 to 2700, ordinate 0 to 1200), not a sliding plane; component and position of the section are not given. The colour bar ends differ (0, -33, -31, -33, -33, -33, -47 MPa; velocity panels 0 to 5.9 up to 0 to 31.6 m/s), so colours cannot be compared between panels, and the unit is printed "Mpa". Measured in (h): the profile reaches 1412 ± 5 m and the valley floor 414 ± 5 m on the ordinate, while the model is "1121m high" (l. 182); without an axis title the reader cannot tell whether the ordinate is model height or elevation. |
| Suggestion | Name the stress component and mark the section line in Fig4 or Fig6; add axis titles with units and state the datum of the ordinate; use one colour scale for (i) to (n) and for (b) to (f), or state why not; write "MPa" on the colour bars; change "along the sliding plane" in l. 302 if a vertical section is meant. |
| Status | missing elements and colour bar labels: verified (page image p. 18); measured extent: verified (instance AB); comparison with the model height: inferred |
| Severity | minor |
| Source | AB |

**GB-32 Fig7(h) shows zero stress in the whole model at t = 0 s, although dynamic loading is said to start from static equilibrium.**

| Field | Content |
|---|---|
| Check | P3 |
| Location | p. 15, l. 304; p. 18, Fig7(h), colour bar; p. 18, Fig7(i) to (n); p. 10, l. 199 to 202 |
| Quotation | "Dynamic loading must be introduced only after the model has attained static equilibrium"; "Fig7. (a) and (h) show the initial state of the landslide" |
| Concern | On the page image (h) is uniformly red and its colour bar runs from 0 to "0Mpa". Panel (i), at 3 s, already shows 0 to -33 MPa with a depth gradient; ρ g h for 2700 kg/m³ and about 1250 m depth is 33.1 MPa, so the range in (i) to (m) is that of gravitational stress, which after static equilibrium must already exist at t = 0. Panel (h) therefore shows either a state before gravity was applied, which is not the initial state of the dynamic run, or a plotting error. Which is it? |
| Suggestion | Replace (h) by the stress field after static equilibrium, or state in the caption (l. 368 to 370) what (h) shows. |
| Status | panel and colour bar: verified (page image p. 18); lithostatic estimate: inferred; the cause: assumption, put as a question |
| Severity | moderate |
| Source | AB |

**GB-33 The results attribute the failure to P- and S-wave action, topographic amplification and structural-plane control, none of which is measured, and the structural planes were excluded from the model.**

| Field | Content |
|---|---|
| Check | P31, P17 |
| Location | p. 15, l. 307 to 313; p. 15, l. 315 to 321; p. 15, l. 322 to 323; p. 9, l. 175 to 178; p. 13, Table 2, column "Monitoring contents" |
| Quotation | "The first-arriving P-waves caused intense vertical dislocation along the steeply dipping structural planes outside the slope."; "The back-slope effect and amplification at higher elevations during seismic wave propagation significantly increased the peak ground acceleration of the Mogangling slope"; "Under the combined influence of structural plane control and strong seismic forces" |
| Concern | The monitored quantities are displacement, velocity, stress and the unbalanced force (Table 2); acceleration is not recorded, so amplification and the increase of peak ground acceleration are not measured. No time history separates P- and S-wave arrivals at the slope. Steeply dipping structural planes and structural-plane control are invoked although the methods state that "the impact of the structural plane on the landslide process has to be ignored in this study" (l. 177 to 178; names of the discontinuities in GB-19). The narrative of l. 307 to 346 reads as an observed mechanism but is tied to no plotted model quantity apart from the maximum velocity of each snapshot. The same mechanisms (amplification at higher elevations, back-slope effect, dynamic interface stress) are given by Wu et al. (2013) and Zhou et al. (2024), which are listed but not cited (GB-48). Because reconstructing the failure process is the first stated aim (l. 65 to 67), the finding changes what the manuscript can show. |
| Suggestion | Either add acceleration monitoring points at several elevations and plot amplification factors and wave arrivals, or reword l. 307 to 323 as interpretation drawn from the literature, with citations, and remove references to structural-plane control that the model cannot reproduce. |
| Status | verified |
| Severity | major |
| Source | SD |

**GB-34 Model output is stated as fact about the 1786 event, and the field investigations that the aims, the inference of the failure sequence and Conclusion 2 rely on are not documented.**

| Field | Content |
|---|---|
| Check | P19 |
| Location | p. 16, l. 327 to 329; p. 16, l. 333 to 335; p. 16, l. 350 to 352; p. 13, l. 264 to 266; p. 2, l. 65; p. 25, l. 472 to 474 |
| Quotation | "ongoing impacts ultimately led to the formation of a loosely consolidated fractured layer approximately 20 meters thick near the interface between the landslide deposit and the underlying bedrock"; "the sequence of failure and run-out at Mogangling was inferred by integrating the numerical results with field-investigation findings" |
| Concern | Several sentences of Section 3.1 state properties of the real deposit (a fractured layer about 20 m thick, a "layered pseudo-bedrock", backflow flooding of "surrounding counties and cities") without saying whether they come from the model, the field or the literature. Of eight core result statements (three in the Abstract, five conclusions), six (75 %) rest only on model output, Conclusion 2 on model output and photographs, Conclusion 1 on the restoration. "field investigations" are named as a method in l. 65 and l. 265 to 266 and in Conclusion 2 ("Based on numerical simulation results and field investigations", l. 472 to 473), but no field campaign (date, observations, sampling, mapping) and no field result apart from the UAV DEM and the photographs of Fig7(o) is reported in Sections 2 or 3. |
| Suggestion | Mark in Section 3.1 which statements are model output and which are field observations with source; add a short subsection on the field investigation (date, what was observed and measured) or remove it from l. 65, l. 265 to 266 and Conclusion 2. |
| Status | missing description and wording: verified; share of statements: inferred |
| Severity | moderate |
| Source | SD, S4 |

**GB-35 The velocity profile in Fig5(b) to (f) peaks at about 45 m/s, above the peak velocity of 31.6 m/s reported for the landslide, and the caption does not say whose velocity it is.**

| Field | Content |
|---|---|
| Check | P2, P3, P29 |
| Location | p. 16, l. 330, l. 337; p. 12, Fig5(b) to (f), main plots and insets; p. 11, l. 220 to 225, l. 233 to 234; p. 17, Fig7(e) colour bar |
| Quotation | "during the impact-at-base stage, the maximum velocity reached 31.6 m/s"; "The velocity reached its peak upon arrival at the valley floor." |
| Concern | Measured in Fig5(b) (0 m/s at 1185 px, 50 m/s at 707 px of a 300 dpi render), the highest marker lies at 45.19 ± 0.42 m/s at a travel of 253 ± 4 m; (c) and (d) show the same peak (S3 measured 45.2 m/s independently). 45.2 / 31.6 = 1.43. The Fig7 colour bars give 5.9, 19.6, 27.1, 31.6, 25.7 and 0.21 m/s at 3, 7, 9, 12, 15 and 131 s. Cases: (i) one block whose peak falls between the Fig7 snapshots; then the peak velocity of the event is at least 45 m/s and l. 330 and l. 337 understate it; (ii) another quantity or another run; then caption and axis must say so. The maximum velocity also bounds the possible kinetic energy (GB-38). The insets in (b) to (f) have no axis titles or units. |
| Suggestion | Name the block or quantity of Fig5(b) to (f) in the caption (l. 238 to 239) and give the time of the 45 m/s peak; report in Section 3.1 the peak velocity over all time steps, not only over the snapshots; label the inset axes. Question to the authors: is the Fig5 curve from the same simulation as Fig7? |
| Status | text values: verified; Fig5 value: verified by measurement (instances AB and S3); cases: inferred; cause: assumption, put as a question |
| Severity | moderate |
| Source | S3, AB |

**GB-36 The simulation is declared to agree with reality on a qualitative visual comparison of two features, and Conclusion 2 turns this into a guarantee without the model's own limitations.**

| Field | Content |
|---|---|
| Check | P15, P32, P29, P3 |
| Location | p. 16, l. 353 to 359; p. 19, Fig7(o); p. 25, l. 471 to 472; limits p. 7, l. 160 to 162, p. 9, l. 175 to 178, p. 10, l. 183 to 191 |
| Quotation | "Fig7. (o) presents compelling evidence of agreement between the numerical simulation results and the actual field observations."; "Comparison with field imagery and result analysis ensures that the simulation outcomes align with actual conditions." |
| Concern | Fig7(o) marks two features (a protruding ridge in the source area, the deposit area) by dashed boxes in a model view and in two photographs, and l. 355 to 359 name them. No runout length, deposit extent, deposit thickness, dam height or volume is measured in the photographs or in the present DEM, which the study holds (l. 130 to 135), and set against the model; no deviation is reported. The simulated view has no time step, viewpoint or scale, and the photographs in Fig7(o) have no source, date, scale or viewing direction (for the image in Fig2(b) see GB-21), so even the visual match cannot be checked for size and position. "compelling evidence" (l. 353) and "ensures" (l. 471) are therefore stronger than the evidence. The manuscript itself states that the ground motion is a substitute (l. 183 to 191), that structural planes were ignored (l. 175 to 178) and that the restored terrain is smooth (l. 160 to 162); these limits bear directly on agreement with reality but do not appear in Conclusion 2. Because the aim is to reconstruct the real event (l. 65 to 67), without a quantitative check all event-specific results read as one plausible model scenario. The undocumented field investigation is GB-34. |
| Suggestion | In Section 3.1 (after l. 359) add a table that compares model and field for runout, deposit area, maximum and mean deposit thickness (present DEM minus restored surface), dam crest height and source-area depth, with differences in m and %; overlay the simulated deposit outline on the map of Fig2(c) and report an overlap index; give time step, viewpoint and scale of the simulated view and source, date and viewing direction of the photographs; in Conclusion 2 (l. 471 to 472) replace "ensures" by "indicates qualitative agreement" and name the three limits. |
| Status | qualitative nature of the comparison and missing figure information: verified (l. 353 to 359, page image p. 19); absence of a quantitative comparison: verified (Sections 2 and 3) |
| Severity | major |
| Source | S4, SD, AB |

**GB-37 Energy conservation of the whole landslide holds by the definition of DE in Eq. (4), so it is not a result; Fig9 shows the same constant total for single blocks for which the text states non-conservation, and the seismic input is missing from the budget.**

| Field | Content |
|---|---|
| Check | P23, P15, P3, P31, P6 |
| Location | p. 19, l. 375 to 377; p. 12, l. 245; p. 13, l. 249, l. 252; p. 19, l. 387 to 389; p. 20, l. 392 to 402; p. 20, Fig8; p. 21 to 22, Fig9(a) to (j); p. 1, l. 26 to 28; p. 25, l. 476 to 482 |
| Quotation | "It is evident that, due to the law of energy conservation, the total sum of the three forms of energy remains constant throughout the landslide."; "unlike the total landslide mass, the energy of single blocks is not conserved"; "Instances where dissipated energy appears to decrease are actually due to the calculation method used."; "the sum of the three energies equals the initial potential energy before sliding" |
| Concern | The energy terms are defined explicitly (Eq. 1 to 4), which makes the budget checkable. With ME = KE + PE (Eq. 1), DE(ti) = ME(t0) - ME(ti) (Eq. 4) and ME(t0) equal to the initial potential energy (l. 252), KE + PE + DE = ME(t0) holds for every block and for the whole mass at every time step, whatever the simulation returns (a check with 1000 random value sets by instance SD confirms the identity). The constant total of Fig8 is therefore an identity, not a result, and cannot show that the landslide "conforms to the law of conservation of energy" (l. 26 to 27) or that it "can be regarded as a successful energy extraction numerical simulation" (l. 388 to 389). Measured: the top of the Fig8 stack lies at 6507 ± 10 GJ in 100 of 104 bars and within 4 px in the rest; in all ten Fig9 panels the total is constant within 3 px, at 5.06, 5.13, 4.01, 3.57, 11.08, 6.59, 1.18, 4.37, 1.59 and 0.95 GJ. Fig9 thus shows for single blocks exactly the property that l. 393 to 394 and Conclusion 3 deny them. What does differ is narrower: DE of the whole mass never decreases (l. 387 to 388), whereas DE of some blocks decreases temporarily (Fig9(a), (c), (i); for example Fig9(a) from 80 to 122 s), that is, those blocks gain mechanical energy. The manuscript first calls these decreases an artefact of "the calculation method used" (l. 399 to 400) and then uses them as evidence of energy transfer (l. 480 to 482); the artefact is disclosed only in the Results, not at Eq. (4). In addition, the budget has no input term although the model is driven by an acceleration record at the base through viscous and free-field boundaries (l. 189 to 199); under Eq. (4) any work of the seismic loading, of the boundaries or of the base block is booked as negative or positive dissipation. Resolution A: DE in Fig8 and Fig9 is computed by Eq. (4); then the conservation claim is tautological and the meaningful finding is monotonic against non-monotonic DE. Resolution B: DE is taken independently from the code (friction and damping work); then Eq. (4) does not describe the figures, and the budget needs the external work term to close. Because the first result of the Abstract and Conclusion 3 rest on this budget, the finding changes what the manuscript can show. |
| Suggestion | In Section 2.3 (after l. 249) state how DE was obtained and that Eq. (4) makes the sum constant by construction; in the Abstract (l. 26 to 28), Section 3.2.1 (l. 375 to 377, l. 388 to 389), Section 3.2.2 (l. 393 to 402) and Conclusion 3 (l. 476 to 482) replace "conservation" and "not conserved" by the actual observation (DE monotonically increasing for the whole mass, temporarily decreasing for some blocks). If a conservation check is intended, compute dissipation independently (frictional and damping work reported by 3DEC), add the work done by the seismic input and absorbed at the boundaries, and show the residual over time; for Fig9 show the work done on each block by contact forces of its neighbours as a separate signed quantity. Counter-design: a run without seismic input after initiation shows which part of the dissipated energy is frictional. |
| Status | identity from Eq. (1), (4) and l. 252: verified; constant totals in Fig8 and Fig9: verified by measurement (instance AB) and on the page images; missing input work: inferred (from l. 189 to 199); how DE was actually computed: assumption, put as a question |
| Severity | major |
| Source | S3, S4, AB, SD |

**GB-38 The absolute energies in Fig8 and Fig12 cannot be reproduced from either stated volume together with the stated velocities, relief and the block energies of Fig9.**

| Field | Content |
|---|---|
| Check | P1, P23, P3, P27 |
| Location | p. 20, Fig8; p. 25, Fig12 label "1116.8"; p. 16, l. 330; p. 17, Fig7(b) to (f) colour bars; p. 11, Table 1, row "landslide mass", column "Density"; p. 13, Table 2, column "Volume"; p. 21 to 22, Fig9(a) to (j), first bar; p. 9, l. 174 to 175, l. 182; p. 7, l. 151 |
| Quotation | "during the impact-at-base stage, the maximum velocity reached 31.6 m/s"; "the volume of the landslide is 317563 m3" |
| Concern | The stacked display of Fig8 and Fig9 makes the budget readable, so it can be checked against the mass. Measured in Fig8: total 6507 ± 10 GJ (S3: 6492 to 6503 GJ), PE at the first bar 6497 ± 10 GJ, KE maximum 1685 ± 19 GJ at 13.6 s (S3: about 1666 GJ). Case A, V = 317563 m³ and ρ = 2300 kg/m³ (Table 1), M = 7.30 × 10^8 kg: an initial 6507 GJ requires a mean descent of 908 m, more than the full height from the top of the sliding mass to the river, 747 m + 131 m = 878 m (l. 174 to 175); KE cannot exceed ½ M v² = 364.7 GJ at the stated maximum of 31.6 m/s (746.1 GJ even at the 45.2 m/s of Fig5, GB-35), yet Fig8 shows about 1685 GJ and Fig12 labels 1116.8 GJ; against the bounds from the Fig7 colour bars (140, 268, 365 and 241 GJ at 7, 9, 12 and 15 s) Fig8 shows 603, 785, 1590 and 824 GJ, 2.9 to 4.4 times the bound, and the r.m.s. velocity at the KE maximum would be 67.9 m/s. With ρ = 2700 kg/m³ the descent is 774 m and the bound at 12 s 428 GJ, still exceeded. Case B, V = 2400 × 10^4 m³ (l. 151), M = 5.52 × 10^10 kg: KE lies below the bound, but 6507 GJ means a mean descent of only 12.0 m for a mass that spans 1120 to 1890 m elevation. The ten monitored blocks start with 43.5 GJ for 11,512.7 m³ (Fig9, Table 2), 3.78 MJ/m³; at that density the whole mass would hold about 1,200 GJ (case A) or 90,700 GJ (case B); 6507 GJ corresponds to about 1.72 × 10^6 m³, a volume stated nowhere. The manuscript does not say which mass, density or block set Fig8 and Fig12 are computed from. Because the absolute energies are the quantitative outcome of Sections 3.2 and 3.4 and the KE values feed the thresholds of l. 452 to 455, the finding changes what the results can show. |
| Suggestion | In Section 2.3 or the Fig8 caption state the mass, density and number of blocks used for Fig8 and Fig12 and the PE datum (GB-25); give initial PE and peak KE as numbers in Section 3.2.1 (l. 373 to 389) and check that KE never exceeds ½ M v²max; correct the volume in l. 151 or l. 182 (GB-15) or the energies in Fig8 and Fig12; consider giving energies per unit mass so that they can be compared with the velocities of Fig7. Question to the authors: is the energy in Fig8 computed for a subset of blocks, or with a unit or scaling factor not stated? |
| Status | Fig8 values: verified by measurement (instances AB and S3); Fig12 label and text values: verified; bounds, ratios, descents and energy densities: inferred (computed from the manuscript's numbers, recomputed in the merge); which subset or scaling causes the gap: assumption, put as a question |
| Severity | major |
| Source | S3, AB, SD |

**GB-39 Fig9(a) and (c) show the potential-energy rebound of Blocks 1 and 3 without preceding kinetic energy, which does not fit the explanation by bouncing.**

| Field | Content |
|---|---|
| Check | P3 |
| Location | p. 20, l. 397 to 399; p. 21, Fig9(a) and Fig9(c), 70 to 131 s; p. 22, l. 416 |
| Quotation | "This can be explained by these blocks bouncing to the opposite bank after impacting the base, increasing their potential energy." |
| Concern | The rebound itself is shown as described. Measured in Fig9(a): PE is 0 from 73 to 79 s, rises to 0.213 GJ at 91 s, stays near 0.19 to 0.21 GJ up to 108 s, rises to 0.368 GJ at 122 s and stays there to 131 s; the KE layer is below detection (less than 0.012 GJ) in every bar from 71 to 131 s. A ballistic rebound that raises PE by 0.368 GJ needs at least 0.368 GJ of KE just before. The gain equals 17.4 m of rise for 939.9 m³ at 2300 kg/m³, in two phases of about 12 and 14 s, while a free ballistic rise of 17.4 m takes about 1.9 s. Fig9(c): PE is 0 at 86 to 88 s, rises to 0.257 GJ at 100 s and 0.336 GJ at 121 s, with KE at most 0.02 GJ. The pattern is a slow lift, which matches the alternative the text gives for falling DE (pushing by neighbouring blocks, l. 400 to 402), not a bounce. |
| Suggestion | Revise l. 397 to 399 and l. 416, or support the bounce with velocity and elevation histories of Blocks 1 and 3 between 70 and 131 s at full time resolution. |
| Status | PE and KE values: verified by measurement (instance AB); kinematic argument: inferred |
| Severity | moderate |
| Source | AB |

**GB-40 The headline claim that lower or front blocks collide more often, receive more energy and travel farther rests on pooled counts against travel distance; no result compares positions or stages, and the causal direction is reversed.**

| Field | Content |
|---|---|
| Check | P11, P21, P15, P9 |
| Location | p. 22, l. 414 to 421; p. 23, Fig10(b), caption l. 423 to 424; p. 1, l. 28 to 30; p. 3, l. 85 to 87; p. 26, l. 483 to 487; p. 13, l. 256 to 258 |
| Quotation | "Compared with the upper rock mass, the lower rock mass is compressed more frequently, receives more energy transfer, and has a longer migration distance."; "as the migration distance increases during the landslide, the number of collisions also rises continuously"; "during the collapse stage, the front portion of the rock mass experiences more collisions than the rear portion, with a clear trend of decreasing collision frequency toward the rear. When the rear rock mass collides with the front, its dissipated energy sharply increases and transfers energy to the front rock mass, enabling the front portion to slide farther." |
| Concern | Placing ten monitored blocks in four position groups (Table 2) is a sound basis for this comparison, and l. 86 to 87 announce it ("the influence of effective collision frequency of different parts of landslide mass on energy transfer is analyzed"). The Results, however, give no collision count, energy received or travel distance per block or per position group, and no split by stage: of the 4 groups × 3 quantities, 0 of 12 cells are reported as numbers (travel paths only as trajectories in Fig10(a)). Fig10(b) shows 26 unlabelled points of "Frequency" against "Travel distance (m)" (measured; one instance counted about 28) with a fitted curve; it does not distinguish blocks by position or stage, so its description as "the frequency of effective collisions experienced by blocks at different locations" (l. 415) is not visible in the panel. Absolute counts per distance bin grow with how many blocks pass a bin and how long they stay; 49 % of the counted collisions lie at or beyond 2200 m. If lower blocks travel farther, they collect more collisions for that reason alone, so "compressed more frequently" and "longer migration distance" may be one fact counted twice; normalised per 100 m or per second in motion the difference could shrink, vanish or reverse. "Compressed" is not measured: stress histories are recorded but not shown (GB-27). Fig9 shows temporary DE decreases also for top block 9 (Fig9(i), about 25 to 35 s, read without measurement), which the text does not mention. The ten blocks were chosen as "representative" without a selection rule (l. 256 to 258). Finally, l. 418 to 419 read collisions as a consequence of distance travelled, while the Abstract and Conclusion 4 read them as the cause of the longer runout ("enabling the front portion to slide farther"); a correlation in Fig10(b) cannot decide between the two. Because this is the last result of the Abstract and Conclusion 4, the finding changes what the manuscript can show. |
| Suggestion | In Section 3.2.2 (after l. 421) add a table per monitored block: position group, travel distance, number of effective collisions, collisions per 100 m and per second in motion, energy received (sum of DE decreases or contact work), and the stage in which collisions occur; code the markers of Fig10(b) by block; count for all blocks or a stratified sample and compare position classes with a test; for the causal claim compare with a run in which the rear part is removed or fixed; state the rule used to choose the ten blocks; reword the Abstract (l. 28 to 30) and Conclusion 4 (l. 483 to 487) to what this analysis shows, using "is associated with" instead of "enabling" unless a test separates cause and consequence. |
| Status | absence of per-block, per-position and per-stage results and reversal of the causal wording: verified (l. 414 to 421, l. 483 to 487, page image p. 23); 26 points: verified by measurement (instance AB); 49 % share and effect of normalisation: inferred; DE decrease of block 9: verified on the page image, read without measurement |
| Severity | major |
| Source | S3, S4, SD |

**GB-41 Fig10 does not define its red curve, and Fig10(a) does not say that its coordinates are displacements from the start point.**

| Field | Content |
|---|---|
| Check | P29 |
| Location | p. 23, Fig10(a) and (b); caption l. 423 to 424; p. 22, l. 414 to 419 |
| Quotation | "Fig10. (a) movement trails of 10 monitoring points and (b) the plot of travel distance vs. collision frequency." |
| Concern | In (b) the red curve has no legend entry, function or measure of fit (ordinate and population: GB-24). In (a) all ten trails start at one point (0, 0, 0) and Z falls below -840 m, so the axes are displacements relative to each start, not positions, while the caption speaks of "movement trails". |
| Suggestion | Give the fitted function with parameters and goodness of fit, or remove the curve; state in the caption (l. 423 to 424) that (a) shows displacement relative to the initial position. |
| Status | verified |
| Severity | minor |
| Source | AB |

**GB-42 Fig12 is built from about three times more time points than the ten stated, and its kinetic-energy peak of 1116.8 GJ lies well below the maximum in Fig8, so VS and AG "at" the KE peak refer to a sampled time before the peak.**

| Field | Content |
|---|---|
| Check | P2, P11, P20, P3, P7 |
| Location | p. 23, l. 426 to 428; p. 24, Fig11 caption l. 437 to 439, l. 440 to 443; p. 24, l. 452 to p. 25, l. 455; p. 25, Fig12(a) and (b), markers and labels "1116.8", "29.47", "319.5"; p. 20, Fig8; p. 15, l. 291 to 292 |
| Quotation | "perform Alpha Shape envelope fitting on the deposit mass at 10 representative time points"; "When the volume expansion rate reaches approximately 29.47% and the surface area growth reaches about 319.5%, it can be considered that the landslide transitions from a solid phase to a fluidized phase. At this point, the kinetic energy peaks" |
| Concern | Linking VS and AG to the energy curves connects deposit shape with energy, and the labels in Fig12 tie the text values to the plot: the triangle sits at VS 29.47 ± 2.5 % and AG 320.2 ± 8.8 %, the annotation line at 1122 ± 17 GJ (measured). But (a) Fig11 lists ten times (0, 3, 7, 9, 12, 15, 32, 71, 100, 131 s), while Fig12(a) carries at least 27 markers on the DE curve (automatic detection, lower bound) and about 29 to 30 on enlargements; only 10 of 29 (34 %) correspond to the described times, and l. 291 to 292 speak only of "successive time steps". Fig12 therefore uses envelope fits at unstated times, or VS and AG were interpolated. (b) The KE maximum in Fig8 is 1685 ± 19 GJ at 13.6 s (S3 read about 1666 GJ); 1116.8 / 1685 = 0.663, a difference of 549 to 568 GJ. Fig8 shows about 1073 to 1082 GJ near 11.0 to 11.1 s, close to 1116.8 GJ, so the Fig12 sample with the highest KE probably lies before the true maximum. Then "At this point, the kinetic energy peaks" does not hold, and VS and AG at the actual peak, and thus the proposed solid to fluid threshold, would be different. No criterion for a "fluidized phase" is defined (GB-44). Because the threshold is the only quantitative result of Section 3.4, the finding changes what the manuscript can show. |
| Suggestion | In Section 3.4 add a table with, for every point in Fig12: time, envelope volume, envelope area, VS, AG, KE, PE, DE; fit an envelope at the time of the KE maximum (12.4 to 13.6 s in Fig8) and report VS and AG there; reconcile the KE values of Fig8 and Fig12; correct "10 representative time points" (l. 427) or state which times enter Fig12; revise l. 452 to 455 accordingly. |
| Status | marker counts: verified (page image, instances AB, SD and S3); KE in Fig8 and annotation positions: verified by measurement; that the Fig12 maximum is a sample before the peak: inferred; consequence for the threshold: inferred |
| Severity | major |
| Source | S3, AB, SD |

**GB-43 Several figures carry text below 6 pt at print size, down to about 2.7 pt, and the Fig12 annotations are typeset with spaces in the numbers.**

| Field | Content |
|---|---|
| Check | P29 |
| Location | p. 23 to 24, Fig11(a) to (j) axis labels; p. 9, Fig3(c) contour labels; p. 25, Fig12(a) and (b) annotations and ticks; p. 12, Fig5 ticks and Fig5(a) legend; p. 18, Fig7(i) to (n) ticks; p. 21 to 22, Fig9 ticks and legends; p. 23, Fig10(b) ticks; p. 17 to 18, Fig7 colour bar labels |
| Quotation | "300"; "1500"; "1116. 8"; "29. 47" |
| Concern | Glyph heights in 300 dpi renders: Fig11(a) Z tick "300" 2.7 pt; Fig3(c) contour label "1500" 2.7 pt; Fig12(a) "1116. 8" 3.0 pt and "29. 47" at most 4.7 pt; Fig5(b) tick "50" and Fig9(a) tick "6" 5.0 pt; Fig9(a) legend "PE", Fig10(b) tick "175", Fig12(a) tick "8000", Fig5 inset tick and Fig7(i) tick "1200" 5.3 pt; Fig5(a) legend and Fig7 colour bar label 5.7 pt (borderline, method accuracy about ±0.6 pt). For comparison Fig1 9 to 10 pt, Fig2(a) 6.3 to 6.7 pt, Fig6 7.0 pt. The Fig12 annotations "29. 47", "319. 5" and "1116. 8" carry a space after the decimal point and no unit. |
| Suggestion | Enlarge all figure text to at least 6 pt at print size; for Fig11 re-export the axes with larger labels or replace the 3-D tick labels by a scale bar; enlarge the contour labels in Fig3(c); write the Fig12 annotations as "29.47 %", "319.5 %" and "1116.8 GJ" at legible size. |
| Status | verified (measured by instance AB on 300 dpi renders) |
| Severity | minor |
| Source | AB |

**GB-44 Fragmentation, debris production and a solid to fluid transition are inferred from envelope growth and DE, but the model description contains no breakage mechanism and envelope growth also measures spreading; Conclusion 5 states the interpretation as established.**

| Field | Content |
|---|---|
| Check | P15, P31, P25 |
| Location | p. 24, l. 445 to 452; p. 25, l. 453 to 456; p. 25, Fig12; p. 23, l. 428 to 431; p. 16, l. 325 to 335; p. 26, l. 488 to 492; p. 9, l. 178 to 182 |
| Quotation | "collisions and friction cause block fragmentation and disintegration, producing large amounts of debris. These newly generated fragments fill the interior and surface of the deposit mass, causing a sudden expansion of the envelope volume"; "the sharp rise of DE shown in the figure further confirms significant fragmentation and disintegration"; "it can be concluded that during energy transfer, collisions and friction cause blocks to fracture and disintegrate, generating a large amount of debris" |
| Concern | Section 3.4 measures envelope volume and area (Fig11, Fig12) and their co-variation with KE (l. 443 to 444). The step to fragmentation is labelled an interpretation in l. 445 ("This phenomenon can be interpreted as follows"), but Conclusion 5 (l. 488 to 492) turns it into a conclusion. No result reports a number of fragments, a block-size distribution, a count of broken contacts or any other fragmentation measure. The model consists of a fixed set of 25345 blocks of 8.7 m × 8.7 m footprint with "A uniform structural plane" inside (l. 178 to 182); no breakage model or breakable bonded contacts are described, so it is open how "fine debris" (l. 326), "fragmented rock debris" (l. 333) or "newly formed fragments" (l. 490) arise in the simulation. Fig12 reaches VS of about 1250 % and AG of about 4300 % (page image); such values arise from spreading of blocks over the valley, which the alpha-shape envelope also encloses, so VS and AG do not separate fragmentation from dispersion. DE by Eq. (4) is the net loss of mechanical energy (friction, damping, boundary exchange) and cannot confirm fragmentation, as l. 451 states (GB-37). The thresholds 29.47 % and 319.5 % are read at a KE value (GB-42), but no criterion for a "fluidized phase" is defined. Literature that bears on fragmentation-driven runout is listed in GB-10. Because "structural evolution" is a title term and Conclusion 5 is the only conclusion on it, the finding changes what the manuscript can show. |
| Suggestion | State in Section 2.1 (l. 178 to 182) whether and how blocks can break. If they can, report a fragmentation measure (number of separated blocks or broken joint contacts per time step at the Fig11 times) next to VS and AG; measure dispersion separately (solid fraction inside the envelope, mean nearest-neighbour distance); define the phase criterion (for example an inertial number or granular temperature threshold) before reading it off Fig12. If they cannot, reword l. 325 to 335, l. 445 to 456 and Conclusion 5 as dispersion of intact blocks, for example "the envelope growth is consistent with dispersion and possibly fragmentation", and delete "further confirms" in l. 451. |
| Status | interpretation turned into conclusion, absence of a fragmentation measure and of a breakage mechanism in the description, Fig12 ranges: verified (text, page image p. 25); envelope growth reflecting spreading: inferred; whether 3DEC blocks in this set-up can break beyond the pre-set planes: assumption, put as a question |
| Severity | major |
| Source | S4, SD |

#### Minor corrections

| ID | Location | Quotation | Replacement | Source |
|---|---|---|---|---|
| KK-18 | p. 20, l. 390 (Fig8 caption) | "Fig8. Evolution of energy during the landslide" | "Fig8. Evolution of potential (PE), kinetic (KE) and dissipated (DE) energy of the whole sliding mass during the landslide" | AB |
| KK-19 | p. 20, l. 397 to 398 | "exhibit a rebound in potential energy after it approaches zero" | "exhibit a rebound in potential energy after their potential energy approaches zero" | S4 |
| KK-20 | p. 22, l. 410 to 413 (Fig9 caption) | "Fig9. Energy analysis for 10 individual blocks in Mogangling landslide: (a) energy evolution of point 1 ; (b) energy evolution of point 2 ;" | "Fig9. Potential (PE), kinetic (KE) and dissipated (DE) energy of the 10 monitored blocks (IDs as in Table 2): (a) energy evolution of point 1; (b) energy evolution of point 2;" and no space before the remaining semicolons | S4, AB |
| KK-21 | p. 23, l. 425 | "3.4 Structural evolution as a function of energy change" (no Section 3.3 exists) | "3.3 Structural evolution as a function of energy change" | S3, S4, SD |
| KK-22 | p. 24, l. 438 to 439 (Fig11 caption) | "(a-i) when time = 0s, 3s, 7s, 9s, 12s, 15s,32s,71s, 100s, 131s." (ten times, ten panels (a) to (j)) | "(a-j) at t = 0, 3, 7, 9, 12, 15, 32, 71, 100 and 131 s; main panels: alpha-shape envelope; insets: simulated landslide mass." | S3, S4, AB, SD |

#### Verification log

| ID | Check | Checked | Values | Result |
|---|---|---|---|---|
| PP-28 | P2 | Stage chronology of Section 3.1 against Section 3.2.1 and Fig8 | Fig7 maxima 5.9, 19.6, 27.1, 31.6, 25.7 m/s at 3, 7, 9, 12, 15 s; Fig8 KE about 0, 575, 670, 1551, 804 GJ at 3.8, 7.2, 9.0, 12.2, 15.1 s (S3 readings); KE maximum about 1666 to 1685 GJ at about 13.6 s against "Around 13 seconds" (l. 383); impact wording at 12 s (l. 331), 13 s (l. 383) and 15 s (l. 338 to 339) read as successive impacts | no finding (peak values: GB-42, GB-35) |
| PP-29 | P3 | Fig7 colour bar maxima against Section 3.1 | (b) 5.9, (c) 19.6, (d) 27.1, (e) 31.6, (f) 25.7, (g) 0.21 m/s; text l. 307 5.9, l. 315 19.6, l. 322 27.1, l. 330 31.6, l. 339 25.7 m/s, l. 346 to 347 "approached 0 m/s"; runtime 131 s (l. 300) | no finding |
| PP-30 | P24 | Stage sequence in Fig7 and envelope times in Fig11 | Fig7(e) at 12 s has the highest colour bar maximum, (f) at 15 s a decrease, in line with l. 330 to 339 and the impact around 13 s (l. 383); Fig11 has ten panels for the ten times of its caption, as in l. 427 | no finding (panel letters: KK-22) |
| PP-31 | P6 | Absolute statements ("entire", "all", "only", "continuously") | "successfully reproduced the entire process" (l. 299 to 300) against dam break not modelled, disclosed in the same section (l. 349 to 350); "continuous increasing trend" of the envelope volume (l. 429) consistent with Fig12; "only potential energy" initially (l. 378) against the datum statement (GB-25) | no separate finding beyond GB-37 and GB-25 |
| PP-32 | P2 | Abstract against Results | Collision extraction (l. 22 to 23, l. 220 to 234), alpha shape VS and AG (l. 23 to 26, Section 3.4), conservation (GB-37), lower block claim (GB-40); direction of the migration claim against Fig9: implied descents of bottom blocks 223 to 239 m, top blocks 44 to 82 m | no further finding; direction consistent (inferred) |
| PP-33 | P23 | Whole-mass energy budget in Fig8 and Fig12 | Fig8 stack top 6492 to 6503 GJ (S3) and 6507 ± 10 GJ (AB) at all times; PE near 0 after about 108 to 120 s; DE end about 6500 GJ; Fig12 PE start and DE end about 6500 GJ; Conclusion 3 "sum of the three energies equals the initial potential energy" (l. 479) | the budget closes, but by definition (GB-37) |
| PP-34 | P24 | Timing of KE in Fig8 against l. 378 to 384 | Bar spacing 1.26 s, 104 bars; KE below 9.6 GJ at 1.2, 2.5 and 3.7 s; 144 GJ at 5.0 s; 1082 GJ at 11.1 s; 1590 GJ at 12.4 s; maximum 1685 GJ at 13.6 s; 824 GJ at 14.9 s; 488 GJ at 16.0 s; zero from 62 s. Text: small conversion 0 to 3 s, increase 3 to 12 s, sharp drop around 13 s | order and times agree within one bar; no finding |
| PP-35 | P24 | Order of the PE rebound of Blocks 1 and 3 against l. 397 to 398 and l. 416 | Fig9(a): PE 0 at 73 to 79 s, then rises; Fig9(c): PE 0 at 86 to 88 s, then rises; Fig10(a) trails 1 (red) and 3 (magenta) end with a reversal | order agrees; no finding on timing (mechanism: GB-39) |
| PP-36 | P30 | Reported errors and corrections against runs | No error correction reported; DE artefact named in l. 399 to 400 without correction | no finding (artefact treated in GB-37) |
| PP-37 | P3 | Legend colours in Fig10(a) | 10 legend entries, 10 trails visible; smallest pairwise colour difference 77 (trails 4 and 9) | all above 40; no finding |
| PP-38 | P11 | Coverage of thresholds, blocks and times in the figures | 5 thresholds announced (l. 230 to 232) = Fig5(b) to (f); 10 blocks = 10 panels Fig9(a) to (j); 10 times = 10 panels Fig11; 7 times × 2 fields = 14 panels Fig7(a) to (n) | no finding (unreported monitored quantities: GB-27) |
| PP-39 | P21 | Comparisons of absolute values across blocks and times | Fig9 panel scales differ (1.2 to 12 GJ); the text compares blocks only qualitatively (rebound of Blocks 1 and 3); Fig8 and Fig12 show the same body | no finding apart from GB-40 |
| PP-40 | P3 | Position of the KE peak markers in Fig12 against l. 452 to 455 | Fig12(a) triangle at VS 29.47 ± 2.5 %; Fig12(b) at AG 320.2 ± 8.8 %; annotation line at 1122 ± 17 GJ against the label 1116.8 | no finding on the positions (peak value and sampling: GB-42) |
| PP-41 | P1 | VS and AG values and labels | Text 29.47 % and 319.5 % (l. 453 to 454) = labels in Fig12(a), (b); Vt / V0 = 1.2947, St / S0 = 4.195; Eq. (5), (6) correct as relative change × 100 % | no finding (anchoring: GB-30) |
| PP-42 | P29 | Axes, units and legends of Fig8, Fig9, Fig12 and the main plots of Fig5; font sizes of Fig1, Fig2(a), Fig6, Fig10(a) | Axis titles with units present ("Energy (GJ)", "Time (s)", "Velocity (m/s)", "Volume Swelling (%)", "Area Growth (%)"); legends PE, KE, DE present but not defined in the captions; Fig1 9.0 to 10.0 pt, Fig2(a) 6.3 to 6.7 pt, Fig6 7.0 pt, Fig10(a) 6.0 pt | no finding beyond KK-18, KK-20 and GB-43 |
| PP-43 | P22 | Numbering and implicit subsets | Figures 1 to 12, Tables 1 and 2, Equations 1 to 6 continuous; sections 3.1, 3.2 (3.2.1, 3.2.2), 3.4; method parts (1) to (4) | gaps recorded as KK-04, KK-21, KK-22 |

### Segment 4: Conclusions, declarations, references (p. 25 to 29)

#### Substantive findings

**GB-45 The Conclusions do not return to the earthquake trigger, to energy accumulation, to the landslide-seismology gap or to the stated practical purposes, and they contain no outlook that weighs these against the model's own limitations.**

| Field | Content |
|---|---|
| Check | P15 |
| Location | p. 25, l. 460 to 492; p. 1, title; p. 2, l. 39 to 41, l. 61 to 64, l. 65 to 73; p. 5, l. 119 to 125 |
| Quotation | "it focuses on revealing the mechanisms of energy accumulation, transfer, and dissipation during the landslide event"; "exploring the dynamic propagation characteristics can provide an evaluation basis for the potential landslide in the high-intensity area of the Dadu River" |
| Concern | The words "earthquake", "seismic", "accumulation", "warning" and "risk" do not occur in l. 460 to 492. The title ("induced by a strong earthquake") and the aims (l. 65 to 73) frame the study around a strong earthquake, but no conclusion states what the seismic loading did to the energy budget or to the failure sequence (l. 306 to 321 are not taken up). "Energy accumulation" (l. 68) is neither analysed in Section 3 nor concluded on. The Introduction motivates the work with a gap in landslide seismology (l. 61 to 64); the Conclusions do not say how the results close it. The practical purposes (early warning, l. 72; hazard evaluation for the Dadu River, l. 119 to 125; "a new idea of terrain restoration", l. 50) are not carried into a conclusion or outlook. These purposes are weakened by limits the manuscript states itself: a substitute ground motion (l. 183 to 191), ignored structural planes (l. 175 to 178) and a restored terrain that is "smooth" (l. 160 to 162). The disclosure is there; its consequences are not drawn. Whether the design can carry the generalising aims at all is GB-04. |
| Suggestion | Add to Section 4 one conclusion on the role of the seismic input (for example energy input by the base motion against DE), one sentence on whether energy accumulation is addressed or remove the term from l. 68, and a short outlook that states which of the purposes in l. 49 to 51, l. 71 to 73 and l. 122 to 125 the results support, given the substitute ground motion and the omitted structural planes. |
| Status | absence of the terms and of an outlook in l. 460 to 492: verified (text search, page images p. 25 to 26); weakening of the purposes by the stated limits: inferred |
| Severity | moderate |
| Source | S4 |

**GB-46 Conclusion 1 describes restoration steps (trajectory equations of contours, reference to other mountain areas of the same stratigraphic unit) that the Methods neither describe nor use.**

| Field | Content |
|---|---|
| Check | P15, P18 |
| Location | p. 25, l. 463 to 468; p. 6, l. 137 to 141; p. 7, l. 157 to 162; p. 9, Fig3(c); p. 4, Fig1 |
| Quotation | "Outside the landslide boundaries, there exist contour lines consistent with the continuity of the mountain range, and their trajectory equations can be extracted as a basis for restoring the contours;(b) The landslide deposit area is often difficult to restore due to the lack of surrounding reference features. In such cases, restoration can be guided by referencing other mountain areas within the same stratigraphic unit."; "the contour lines corresponding to the sliding bed and accumulation area are modified to be straight" |
| Concern | The Methods describe the restoration as modifying the contour lines over sliding bed and accumulation area "to be straight" (l. 139 to 140) and "along the extension direction of the mountains on the left and right sides" (l. 157 to 158). Neither trajectory equations (form, fitting, parameters) nor a reference to other mountain areas of the same unit appear there, in Fig1 or in Fig3(c). The deposit area, which Conclusion 1(b) calls "often difficult to restore", is restored in the study itself by straightening only. A recommendation in the conclusions should rest on a described procedure; the missing test of the restored surface is GB-16. |
| Suggestion | Either describe in Section 2.1 (after l. 141) how trajectory equations were fitted and how the deposit area was restored with reference to another mountain area, with that area named and shown in Fig3(c), or limit Conclusion 1 (l. 463 to 468) to the procedure actually applied. |
| Status | verified (l. 137 to 141 and l. 157 to 162 against l. 463 to 468; Fig1 and Fig3 on page images p. 4 and p. 9) |
| Severity | moderate |
| Source | S4, SD |

**GB-47 The availability statements withhold all own data and code "upon reasonable request" without a reason, although none of the data concern persons.**

| Field | Content |
|---|---|
| Check | P12 |
| Location | p. 26, l. 494 to 495; p. 26, l. 505 to 506; data products at p. 6, l. 130 to 135; p. 6 to 7, l. 138 to 143 and l. 157 to 159; p. 9, l. 168 to 182; p. 11, l. 226 to 234; p. 13, l. 256 to 264 and Table 2; p. 14, l. 272 to 284; p. 23, l. 426 to 428 |
| Quotation | "The codes that support the findings of this study are available from the first author, Yunfeng Ge, upon reasonable request."; "The data and materials that support the findings of this study are available from the first author, Yunfeng Ge, upon reasonable request." |
| Concern | The Methods name at least seven data products or code items produced by the authors: (1) the UAV-derived DEM and point cloud of the present topography (l. 130 to 135); (2) the restored pre-event terrain (l. 138 to 143, l. 157 to 159, Fig3(c)); (3) the 3DEC model with 25345 blocks and its material assignment (l. 168 to 182, Table 1); (4) the displacement, velocity and stress histories of the ten monitored blocks and of the whole mass (l. 256 to 264, Table 2); (5) the peak-detection procedure and the resulting 1,139 effective collisions (l. 226 to 234); (6) the alpha-shape processing with α = 1 and the envelope volumes and areas (l. 272 to 284, l. 426 to 428); (7) the energy time series of Fig8, Fig9 and Fig12. The two statements cover all of them with one blanket "upon reasonable request"; none of these data concern persons, and no reason for withholding (licence, size, third-party restriction) is given. The manuscript has no appendix or supplement and the statements contain no links, so apart from Tables 1 and 2 nothing is accessible, and the key numbers (1,139 collisions, l. 233 to 234; VS 29.47 % and AG 319.5 %, l. 453 to 454) cannot be checked by a reader. Third-party sources: GB-21. |
| Suggestion | In "Availability of data and material" (l. 505 to 506) and "Code availability" (l. 494 to 495) list items (1) to (7) separately and deposit the DEM, the restored terrain, the 3DEC input files, the monitoring histories, the energy series, the alpha-shape envelopes and the peak-detection script in a public repository with a DOI, or give a concrete reason for each item that is withheld. |
| Status | wording of both statements, list of sources with locations, absence of appendix, supplement and links: verified; that the key numbers cannot be checked without the data: inferred |
| Severity | moderate |
| Source | S2 |

**GB-48 Sixteen of 31 reference entries are cited nowhere, among them the earlier studies of the Mogangling landslide and the authors' own study on mechanical energy evolution, and the mechanisms these studies describe reappear as simulation results without attribution.**

| Field | Content |
|---|---|
| Check | P14, P4 |
| Location | p. 26, l. 508 to 510 (Bernardie), l. 514 to 516 (Chang); p. 27, l. 517 to 520 (Chen), l. 524 to 526 (Dahal), l. 537 to 539 (Gao), l. 540 to 542 (Ge), l. 543 to 545 (Gong), l. 546 to 548 (He, J.), l. 549 to 552 (He, K.), l. 553 to 555 (He, N.); p. 28, l. 562 to 565 (Nava), l. 566 to 568 (Sinčić), l. 588 to 590 (Wu, J.), l. 591 to 593 (Yang); p. 29, l. 597 to 599 (Zhang, K.), l. 603 to 605 (Zhou); p. 2, l. 38 to 41 and l. 65 to 73; p. 15, l. 310 to 313 and l. 316 to 318; p. 5, l. 92 to 125 |
| Quotation | "Ge, Y., Tang, H., and Li, C.: Mechanical energy evolution in the propagation of rock avalanches using field survey and numerical simulation"; "Wu, J., Wang, Y., Dong, S., Chen, Y., and Wang, L.: Genetic Mechanism and Failure Process of the Mogangling Seismic Landslide"; "Under the combined influence of seismic wave amplification at higher elevations, the back-slope effect, and dynamic interface stress effects, strong unloading-induced tension cracking occurred in the source area rock mass along pre-existing potential sliding surfaces." |
| Concern | All citations stand in l. 34 to 63; Sections 2 to 4 cite nothing (text search). Of the 31 entries, 16 have no citation of any form (16/31 = 51.6 %); three more are matched only by a citation with another year (Tian 2016 cited as 2017, Zhao 2021 as 2020, Zhang, J. 2023 possibly as 2024; GB-02). One instance counted 19 uncited entries, another 16; the difference is exactly these three entries. Among the uncited entries are the works that precede this contribution most directly: Wu et al. (2013), which attributes the Mogangling failure to seismic shaking, topographic amplification and back-slope effects of the 1786 earthquake (abstract); Zhou et al. (2024), which from field investigation, remote sensing and numerical calculation attributes it mainly to seismic acceleration amplification, back-slope effects, interface dynamic stress and double-sided slope effects (abstract); Zhao et al. (2021) on dimensions, volume, dam and outburst (cited at most as "Zhao et al., 2020"); and Ge et al. (2021), an earlier study by the first and third author on mechanical energy evolution with field survey and numerical simulation, the closest methodological precedent by its title. The Introduction does not say what these works established, and l. 310 to 313 and l. 316 to 318 present the same mechanisms as results of the simulation without attribution (content: GB-33); site description, magnitude, dam duration and parameter choices in Section 2.1 are given without any source (GB-15, GB-20). The reader cannot separate what is known about Mogangling from what this study adds. Since these works are in the list, this is missing citation, not missing literature. Five of the uncited entries (Bernardie, Dahal, Nava, Sinčić, Zhang, K.) are printed in grey and ragged right, unlike the black justified entries (page images p. 26 to 29). |
| Suggestion | Add a paragraph to Section 1 after l. 41 that summarises Wu et al. (2013), Zhao et al. (2021) and Zhou et al. (2024) on the Mogangling landslide and Ge et al. (2021) on energy evolution and states in one sentence what this manuscript adds; cite Wu et al. (2013) and Zhou et al. (2024) at l. 310 to 313 and l. 316 to 318 and say whether the simulation confirms their mechanisms or derives them independently; cite the sources of the site description in Section 2.1; cite or delete the remaining uncited entries; set all entries in the same typeface. |
| Status | absence of citations and typeface difference: verified (text search l. 1 to 506, page images p. 26 to 29, recomputed in the merge); content of Wu et al. 2013, Zhou et al. 2024 and Zhao et al. 2021: verified at abstract level (instance S1); Ge et al. 2021 as closest precedent: inferred from its title |
| Severity | moderate |
| Source | S1, S4 |

#### Minor corrections

| ID | Location | Quotation | Replacement | Source |
|---|---|---|---|---|
| KK-23 | p. 25, l. 464; l. 466 | "It should be noted that:(a) Outside"; "restoring the contours;(b) The landslide" | "It should be noted that: (a) outside"; "restoring the contours; (b) the landslide" | S4 |
| KK-24 | p. 26, l. 494 | "The codes that support the findings of this study are available" | "The code that supports the findings of this study is available" | S4 |
| KK-25 | p. 26, l. 499 | "XF: Data curation, Investigation. LZ: Data curation, Investigation." | "XF: Data curation, Investigation; LZ: Data curation, Investigation." | S4 |
| KK-26 | p. 26, l. 507 | "Reference" | "References" | S4 |
| KK-27 | p. 27, l. 530 | "Fan, X., Scaringi, G., Korup, O., et al.:" (all other entries list every author) | "Fan, X., Scaringi, G., Korup, O., West, A. J., van Westen, C. J., Tanyas, H., Hovius, N., Hales, T. C., Jibson, R. W., Allstadt, K. E., Zhang, L., Evans, S. G., Xu, C., Li, G., Pei, X., Xu, Q., and Huang, R.:" (author list per the Cardiff University repository record read by instance S4) | S4 |

#### Verification log

| ID | Check | Checked | Values | Result |
|---|---|---|---|---|
| PP-44 | P4 | Numbering and targets of sections, figures, tables and equations over the whole manuscript | Sections 1, 2, 2.1 to 2.4, 3, 3.1, 3.2, 3.2.1, 3.2.2, 3.4, 4; figures first referenced in order (Fig1 l. 76 to Fig12 l. 443); Table 1 l. 212, Table 2 l. 259; Eq. (1) to (6) l. 245 to 277; panel references Fig3(a) to (c), Fig5(a), (b-f), Fig7(a) to (o), Fig10(a), (b) checked against the page images | Figures 1 to 12 and Tables 1 and 2 consecutive, referenced in order, panel references reach existing panels. Deviations: KK-21, GB-17, KK-22, GB-29, GB-40 |
| PP-45 | P4 | Citations against reference list, both directions, and short form against entry | 29 cited works, all in l. 34 to 63; 31 entries l. 508 to 605; 7 exact matches (Carpignano 2009, Sun 2011, Wang 2014, Hu 2017, Wu 2024, Du 2021, Li 2024); 9 with year, name or assignment problems; 13 without entry; 16 entries uncited | Findings GB-08, GB-02, GB-48; DOIs not resolved (optional check) |
| PP-46 | P15 | Each statement of Conclusions 1 to 5 mapped to a Results location | C1 restoration: l. 137 to 162, Fig3 (in part); C2 model content: l. 168 to 213; extraction of KE, PE, DE: l. 372 to 402, Fig8, Fig9; agreement with reality: l. 353 to 359; effective collisions: l. 220 to 234, Fig5; C3 DE of the whole mass: l. 387 to 388, Fig8; DE decreases of blocks: l. 399 to 402, Fig9; C4 front against rear: no location; C5 envelope growth with KE: l. 428 to 429, l. 443 to 444, Fig11, Fig12; fragmentation as cause: interpretation only | Without location or overstated: GB-37, GB-40, GB-36, GB-44, GB-46 |
| PP-47 | P15 | Outlook and proposals, each held against the manuscript's own findings | Section 4 contains no outlook and no proposal for further work; purpose statements l. 49 to 51, l. 71 to 73, l. 122 to 125 held against l. 160 to 162, l. 175 to 178, l. 183 to 191 | no stand-alone outlook to check; purposes not carried into the Conclusions: GB-45 |
| PP-48 | P15 | Verb strength in Results and Conclusions | "presents compelling evidence" l. 353; "can be regarded as a successful energy extraction" l. 388 to 389; "it is clear that" l. 418; "confirming the previous inference" l. 416; "effectively reveals" l. 429; "further confirms" l. 451; "it can be considered" l. 454; "ensures" l. 471; "obeys" l. 478; "it can be concluded" l. 483, l. 489 | Overstated: l. 353 and l. 471 (GB-36); l. 388 to 389 and l. 478 (GB-37); l. 451 and l. 489 (GB-44); l. 483 (GB-40); "can be identified" (l. 473 to 474) follows from l. 220 to 234 as a method statement |
| PP-49 | P15 | Theory frame and key terms from title, Introduction and aims searched in Results and Conclusions | "energy evolution" (Section 3.2, C3), "structural evolution" (Section 3.4, C5) taken up; "high-altitude and long-runout", "strong earthquake", "energy accumulation", "movement trajectory", "spatiotemporal evolution of velocity", "debris flow propagation" and "landslide seismology" not in Section 4 | GB-45 |
| PP-50 | P16 | Language and form of Section 4, Statements and Declarations and reference list (page images p. 25 to 29) | Conclusions l. 460 to 492; Statements l. 493 to 506; 31 entries in alphabetical order, author form "Surname, Initials" except l. 521 and l. 530, DOI as https://doi.org/ in all 31, year at the end in all 31; wide word spacing before long DOIs in justified lines (l. 535, l. 541, l. 551, l. 560, l. 583, l. 589, l. 601) | Corrections KK-23 to KK-27; typeface difference in GB-48; wide spacing is a consequence of justification, readable, not raised; citation style not checked (optional check) |
| PP-51 | P16 | Characters and typesetting in Sections 1 to 3 flagged in the extracted text, confirmed or rejected on the page images | Confirmed: l. 151 exponent "104" at full size (8.04 pt against 5.25 pt for the superscript "3"); l. 152, l. 153 to 156, l. 176 to 177, l. 182, l. 193 to 195, l. 218, l. 228, l. 246, l. 251, l. 397 to 398, l. 410 to 413, l. 438. Rejected as extraction artefacts: symbols of Eq. (1) to (6), the copyright sign in the header, sub- and superscripts of Q4del, γO2, T3bg, km2 and m3 outside l. 151 | Confirmed items: KK-08, KK-09, KK-10, KK-12, KK-13, GB-03, KK-14, KK-16, KK-17, KK-19, KK-20, KK-22; rejected items: no finding |
| PP-52 | P12 | Links and appendices in the availability statements | Statements at l. 494 to 495 and l. 505 to 506 contain no URL or DOI; no appendix or supplement; disclosed limitation: no instrumental record of the 1786 earthquake (l. 183 to 186) | no finding on links (none present); the disclosed limitation is not raised again; availability itself: GB-47 |
| PP-53 | P9 | Proposed future studies | None in the Conclusions or elsewhere | no finding |

## Optional checks

| Area | What it needs | Responsible | Run |
|---|---|---|---|
| DOI resolution | one retrieval per reference entry with DOI | `science-quellenapparat-pruefung` | no |
| Citation style | the name of the style | `science-zitierstil-harvard-ctr` or the style rules of the journal | no |
| AI statement against publisher policy | the policy of the target publisher | this review, on request | no |
| Relation to the authors' own prior work | the authors' prior work | this review, on request | no |
| Journal requirements | the author guidelines of the target journal | this review, on request | no |
| Factual correctness | access to the sources of the checked statements and a selection of sections | `science-faktenbeleg-pruefung`, `geo-frage-belegbasiert-klaeren` | no |

## Limits of this review

- Checked version: egusphere-2025-4506.pdf, 29 pages, SHA-256 64cb3787456244aa6102e34f776b47e9a612d06e8894d391758ae240dbe415d6.
- Unreadable sources: Ge et al. (2021), Zhao et al. (2021), Wu et al. (2013), Carpignano et al. (2009), Du et al. (2021), Song et al. (2017), Wu et al. (2024) and Cheng and Li (2014) were read at abstract, title or index level only (closed access or publisher page not reachable); the open full text of Fan et al. (2019, Rev. Geophys.) was not read beyond its abstract; the 15 in-text citations without matching entry could not be identified and therefore not checked for fidelity.
- Findings with status assumption: 14 of 48 (in each, only the part marked assumption is put as a question).
- Optional checks run: 0 of 6.
- Dropped instances: none.
- Discarded findings: 0 of 76 instance findings (all carried the mandatory fields; no finding was refuted on re-checking). 45 instance findings were merged into 17 findings; 28 minor corrections were absorbed into findings that already treat their location and subject, and the remaining 44 were merged into 27. No hint outside the checklists became a finding of the merge (ZF), because every place concerned had been treated by a responsible instance.
- The review instances ran as separate agents. Values measured by the instances on 300 dpi renders were not re-measured in the merge; quotations were checked against the extracted text and the page images, calculations were recomputed, and contested readings were checked on the page images (p. 6 at 400 dpi, p. 13, 18, 20, 22, 23, 25). Two contradictions between instances were decided there: the east end of the section line in Fig2(c) is labelled a' (GB-17), and Fig10(b) has 26 points (GB-40).
