# Review report: Energy and structural evolution process of high-altitude and long-runout landslides induced by a strong earthquake

| Field | Value |
|---|---|
| Manuscript | Ge, Y., Hu, B., Tang, H., Fu, X. and Zhu, L. (2025) Energy and structural evolution process of high-altitude and long-runout landslides induced by a strong earthquake, EGUsphere preprint egusphere-2025-4506, https://doi.org/10.5194/egusphere-2025-4506 |
| Checked version | egusphere-2025-4506.pdf, 29 pages, SHA-256 64cb3787456244aa6102e34f776b47e9a612d06e8894d391758ae240dbe415d6 |
| Date | 2026-10-17 |
| Language | English |
| Review instances | Segments 1 to 4 (S1 to S4), figures (AB), study design and method (SD); the six review instances ran as separate agents without shared context; merging, verification of wording and overall assessment in a separate step (ZF); no instance omitted |
| Note | Line numbers are the printed margin numbers (printed every fifth line, intermediate lines counted from the nearest printed number) and were confirmed on the page images. Figures carry no printed numbers inside; they are cited by page and panel. Values read from figures were measured on 150 to 600 dpi renders by the instances named in each finding. |

## Summary

The manuscript is a single-case numerical back-analysis of the 1786 Mogangling landslide on the Dadu River (Luding County, Sichuan), triggered by the 1786 Kangding earthquake. The pre-failure surface is restored by straightening contour lines derived from a UAV DEM of the present terrain. A 3D discrete element model (3DEC, Mohr-Coulomb blocks, 8.7 m × 8.7 m columns, 25,345 blocks in the whole model, viscous and free-field boundaries) is loaded with the acceleration record of the Luding station from the 2008 Wenchuan earthquake and run for 131 s of simulated time. From the output the authors derive potential, kinetic and dissipated energy (dissipated energy defined as the residual ME(t0) minus ME(ti), Eq. 4) for the whole mass and for ten monitored blocks, identify "effective collisions" as velocity peaks above a 30 % prominence threshold (1,139 detected), and fit alpha-shape envelopes (alpha = 1) at ten time points to define volume swelling (VS) and area growth (AG). Key reported values are maximum velocities of 5.9 to 31.6 m/s, a whole-mass energy of about 6,500 GJ, a kinetic energy peak labelled 1116.8 GJ, and a "solid to fluidized" transition at VS = 29.47 % and AG = 319.5 %. The landslide volume is stated as about 2400 × 10⁴ m³ for the field and 317,563 m³ for the model. The abstract reports energy conservation for the whole mass, non-conservation for single blocks, and more frequent compression, more energy transfer and longer travel of the lower rock mass.

## Strengths

1. The manuscript names its main modelling limitations where the method is introduced: the structural planes that had to be ignored (l. 175 to 178), the substitute 2008 ground motion for the 1786 event (l. 183 to 191) and the smoothness of the restored terrain (l. 160 to 162). A reader can therefore see on which inputs every result is conditional (PP-13); the consequences are drawn only in part (GB-24, GB-36).
2. The detection threshold for effective collisions is not reported as a bare number: Fig. 5b to 5f show the detection at 10, 20, 30, 40 and 50 % side by side (l. 229 to 233), so the dependence of the detected peaks on the threshold can be judged visually (PP-22); a quantitative check of the chosen threshold is still missing (GB-27).
3. The energy terms and the dispersion indices are defined by explicit equations, Eqs. (1) to (6), with VS and AG normalised to the state at t = 0 (PP-32, PP-33). This makes the bookkeeping transparent enough that its consequences can be traced exactly, including the identity contained in Eq. (4) (GB-38).
4. The kinematic results are consistent between text and figures: the maximum velocities of 5.9 to 31.6 m/s in the text equal the colour bar maxima of Fig. 7b to 7f, the model dimensions in the text equal the labels of Fig. 4, and the timing of the kinetic energy peak in Fig. 8 agrees with the text within the bar width (PP-21, PP-27, PP-28); figures, tables and equations are numbered without gaps and cited in ascending order (PP-34).

## Weaknesses

1. The energy results stated first in the abstract and in Conclusions 3 and 5 rest on bookkeeping rather than on measured quantities: the constant energy total and its supposed failure for single blocks follow from Eq. (4) for any body (GB-38), and fragmentation and the solid to fluid transition are inferred from envelope growth without a fragmentation measure and at sampling times that miss the kinetic energy peak (GB-42, GB-43). Suggestion: compute an independent energy balance from the energy tracking of the code, including the work of the seismic input and of the boundaries, and report a fragmentation and a dispersal measure over time.
2. It is not shown that the simulated body and its loading represent the 1786 event: the stated volumes, the map and the energy level are mutually incompatible and the potential energy datum is unclear (GB-20, GB-29), the substitute input motion is neither sourced nor varied (GB-24), the failure mechanism in Sect. 3.1 relies on structural planes the model omits (GB-36), and the comparison with the field is qualitative (GB-37). Suggestion: define the simulated mass and datum, add runs with other input motions, and compare simulated and mapped deposit quantitatively.
3. The position-dependent result of the abstract and Conclusion 4 (lower or front blocks collide more, receive more energy, travel farther) has no reported data, and the detector it would rest on is not validated: no counts by position or stage exist (GB-40), velocity peaks are not checked against contact data and the population behind the 1,139 collisions is not stated (GB-27, GB-28), and energies of blocks of different mass are compared unnormalised (GB-39). Suggestion: validate the detector against contact histories and report per-block counts, travel distances and specific energies by zone.
4. Reproducibility and the literature basis are limited in several moderate points: data, code, model files and settings are available only on request or not stated (GB-44, GB-22, GB-25), 15 cited works lack a matching reference entry and 16 entries are never cited (GB-05, GB-45), gap and novelty claims are made without a described search and against the authors' own earlier energy study (GB-03, GB-08, GB-14), and key objects carry several names (GB-31, GB-32). Suggestion: deposit data and scripts with a persistent identifier, add a table of model and processing settings, reconcile citations and references, and use one defined name per object.

## Findings by segment

### Segment 1: Title, abstract, introduction (p. 1 to 2, l. 1 to 73)

#### Substantive findings

**GB-01 The single-case design cannot support the general aims and the general wording of title and conclusions.**

| Field | Content |
|---|---|
| Check | P10 |
| Location | p. 1, l. 1 to 3 (title); p. 2, l. 40 to 41 and l. 71 to 73; p. 2, l. 75 to 76; p. 5, l. 99 to 100 and l. 122 to 125; p. 25 to 26, l. 463 to 492 (Conclusions 1 to 5) |
| Quotation | "so as to summarize the law of high-level rock landslide induced by earthquake" (l. 40 to 41); "provide a theoretical foundation and scientific support for early warning and risk mitigation of high-altitude and long-runout landslides triggered by intense earthquakes" |
| Concern | The case is reconstructed in detail, and the manuscript states openly that one landslide is the object ("the representative Mogangling landslide is selected as a case study", l. 75 to 76). The design consists of one landslide, one input record, one parameter set and one model run (PP-04). A "law" for a class of landslides needs variation across cases or across controlling factors; the design has neither. The selection of Mogangling as "representative" among the "nearly 20 large and super large earthquake landslides" of the area (l. 99 to 100) has no stated criterion, and the early warning aim (l. 72 to 73) has no instrument and no result (see also GB-10). The statements about Mogangling remain; the general claims are not supported. |
| Suggestion | Either restrict title, aims (l. 39 to 41, l. 71 to 73) and Conclusions to the Mogangling case, or add a design that varies the controlling factors, for example a parametric study on the same model (input amplitude, friction, block size) plus a second well documented case, and report which of the five conclusions hold across all runs. State in Sect. 2 why Mogangling is representative of the class. |
| Status | verified (wording; single case, single run, no selection criterion); inferred (that a general law requires variation across cases or factors) |
| Severity | moderate |
| Source | SD |

**GB-02 The two sources cited for a "trend of frequent occurrence" of seismic landslide chain disasters do not state such a trend.**

| Field | Content |
|---|---|
| Check | P13 |
| Location | p. 1, l. 33 to 34 |
| Quotation | "In recent years, the chain disasters of high-level rock landslides in high-intensity earthquake areas have shown a trend of frequent occurrence (Carpignano et al., 2009; Fan et al., 2019a)" |
| Concern | Earthquake-induced hazard chains are a fitting motivation, and Fan et al. (2019) is a suitable general reference for such chains. Neither cited work, however, supports a temporal increase. Carpignano, A., Golia, E., Di Mauro, C., Bouchon, S. and Nordvik, J. (2009) 'A methodological approach for the definition of multi-risk maps at the regional level: first application', Journal of Risk Research, 12(3-4), pp. 513-534, doi:10.1080/13669870903050269, develops a multi-risk decision support approach for the Piedmont region (Italy); its abstract speaks of an increased vulnerability of society to natural and technological disasters and does not address earthquake-induced rock landslides or hazard chains. The abstract of Fan, X., Scaringi, G., Korup, O. et al. (2019) 'Earthquake-induced chains of geologic hazards: patterns, mechanisms, and impacts', Reviews of Geophysics, 57, pp. 421-503, doi:10.1029/2018RG000626, describes elevated landslide activity for years after a large earthquake, a post-seismic decay, not a secular trend of more frequent chain disasters. The central statement of the sentence (a trend) therefore has no supporting source. |
| Suggestion | In l. 33 to 34 either cite a study that documents a temporal increase of coseismic landslide chain events, with its period and region, or reformulate to a statement the sources support, for example that strong earthquakes frequently trigger hazard chains (Fan et al., 2019), and remove Carpignano et al. (2009) from this sentence. |
| Status | verified for Carpignano et al. (2009) (abstract read by instance S1); inferred for Fan et al. (2019) (abstract only, full text not read) |
| Severity | moderate |
| Source | S1 |

**GB-03 The claims that pre-failure terrain restoration is rare and mostly two-dimensional, and that contour restoration offers "a new idea", are made without a described literature search, and published 3D reconstructions exist.**

| Field | Content |
|---|---|
| Check | P28 |
| Location | p. 2, l. 42; l. 46 to 47; l. 49 to 51 |
| Quotation | "At present, in terms of surface terrain restoration, the terrain restoration before a landslide is less." and "For most numerical simulations involving terrain restoration, a two-dimensional simulation is more often used." and "which can provide a new idea of terrain restoration before a landslide for the same type of research." |
| Concern | Reconstructing the pre-failure surface of a 1786 event is a real difficulty, and the manuscript describes its approach openly (l. 136 to 143, l. 157 to 162). The three sentences are a gap claim, a frequency ranking ("most", "more often") and a novelty claim, but the manuscript names no database, search terms, period or date of search. Instance S1 found pre-failure topography reconstructions for historical and prehistoric rock slope failures used in runout analyses: Crosta, Frattini, Valbuzzi and Hermanns (2014, EGU2014-16272) rebuild the pristine surface of the Cerro Caquilluco rock avalanche sequence and simulate it with SPH and finite element codes; Körfgen, Mergili and Zangerl (2014, EGU2014-6621) reconstruct the pre-failure topography of the Köfels rockslide with GIS; De Pedrini, Ambrosi and Scapozza (2022) reconstruct the pre-failure surface of the 1513 Monte Crenone rock avalanche for runout modelling (GB-06); Gatter et al. (2018, PeerJ, 6, e5903, doi:10.7717/peerj.5903) run a 3D runout back-analysis (DAN3D) on a pre-event DEM, which contradicts the unqualified ranking of l. 46 to 47. What may be new is the specific contour-continuity procedure, which the text does not delimit from these approaches. A purely linguistic smoothing of l. 42 (for example "few studies have restored the pre-landslide terrain") would keep the unsupported claim and is therefore included here rather than as a minor correction. |
| Suggestion | In l. 42 to 51 either state the search that supports the claims (databases, terms, period, date) or reformulate them as a description of the chosen procedure; delimit the contour-continuity method from published pre-failure reconstructions (interpolation from adjacent slopes, removal of deposits, trial-and-error surfaces); drop or quantify "most" and "more often" in l. 46 to 47. |
| Status | verified (no search described, l. 42 to 51); verified for the counterexamples at abstract level and, for De Pedrini et al. (2022), in the open access full text (read by instance S1) |
| Severity | moderate |
| Source | S1, S4 |

**GB-04 Three of the works cited for the state of terrain restoration and simulation practice do not deal with what the sentences attribute to them.**

| Field | Content |
|---|---|
| Check | P13 |
| Location | p. 2, l. 43 to 46 and l. 46 to 49 |
| Quotation | "the key information of landslide characteristics is often obtained through photos, field surveys, optical remote sensing images and UAV impact, so as to further build geomorphic maps through GIS (Geographic Information System) for subsequent analysis (Zhang et al., 2024; Song at al.2017; Fan et al., 2020; Wu et al., 2024)" and "For most numerical simulations involving terrain restoration, a two-dimensional simulation is more often used. The simplified model is adopted to simulate the overall process of landslide by inputting external stress (Du et al., 2021; Cheng 2014; Li et al., 2024)" |
| Concern | The paragraph sets out the methodological gap at the right place; the cited works partly describe something else. (1) Song, K., Wang, F., Liu, Y. and Huang, H. (2017) 'Landslide deformation prediction by numerical simulation in the Three Gorges, China', in Advancing Culture of Living with Landslides, pp. 309-315, doi:10.1007/978-3-319-53483-1_36, builds a 3D numerical model of a reservoir landslide verified by GPS monitoring; it does not derive landslide characteristics from photos, field surveys, remote sensing or UAV images. (2) Wu, H. et al. (2024) 'Numerical simulation on potential landslide-induced wave hazards by a novel hybrid method', Engineering Geology, 331, 107429, is by its title a numerical wave hazard study of a potential landslide. (3) Li, Z., Dai, Z., Cheng, S., Yang, Z., Zhang, A. and Xiong, Q. (2024) 'Study on the chain-type failure mechanism of large-scale ancient landslides', Frontiers in Earth Science, 12, 1466751, doi:10.3389/feart.2024.1466751, models rainfall seepage and limit-equilibrium stability of the reactivated Zhongbao landslide; it reports no terrain restoration and no seismic or other external stress input. Du et al. (2021) and Cheng and Yu-Sheng (2014) fit the second sentence. For the first sentence two of four cited works do not support it, for the second one of three. |
| Suggestion | In l. 43 to 46 replace Song et al. (2017) and Wu et al. (2024) by works that derive landslide characteristics from imagery and field mapping, or delete them; in l. 46 to 49 remove Li et al. (2024) or restrict the sentence to what Du et al. (2021) and Cheng and Yu-Sheng (2014) show. |
| Status | verified for Song et al. (2017) (publisher abstract) and Li et al. (2024) (open access full text), both read by instance S1; inferred for Wu et al. (2024) (closed access, title and record only) |
| Severity | moderate |
| Source | S1 |

**GB-05 Fifteen of the 29 author-year keys cited in the introduction have no matching entry in the reference list.**

| Field | Content |
|---|---|
| Check | P4 |
| Location | p. 2, l. 45 to 46 (Zhang et al., 2024; Fan et al., 2020); l. 53 to 54; l. 56; l. 58 to 59; l. 62 to 63; reference list p. 26 to 29, l. 508 to 605 |
| Quotation | "(Zhu et al., 2010; Zhang et al., 2020a, b; Cuomo et al., 2021; Shugar et al., 2021)" (l. 58 to 59); "(Navarre et al., 2009; Van Herwijnen and Schweizer, 2011; Helmstetter and Garambois, 2010; Cook et al., 2021; Pandey et al., 2021)" |
| Concern | All in-text citations of the manuscript stand in l. 34 to 63; Sections 2 to 4 contain none (text search over all body lines). The introduction cites 29 author-year keys ("Zhang et al., 2020a, b" counted as two). Thirteen have no entry that could be meant: Huang et al. (2012), Intrieri et al. (2018), Huang et al. (2019), Zhu et al. (2010), Zhang et al. (2020a), Zhang et al. (2020b), Cuomo et al. (2021), Shugar et al. (2021), Navarre et al. (2009), Van Herwijnen and Schweizer (2011), Helmstetter and Garambois (2010), Cook et al. (2021) and Pandey et al. (2021). For two more, "Zhang et al., 2024" and "Fan et al., 2020" (l. 45 to 46), only entries of the same first author with another year exist (Zhang, J. et al., 2023, Landslides 21, l. 594 to 596; Fan, X. et al., 2019, Landslides 17, l. 533 to 536). 15/29 = 52 % (computed) of the keys thus have no matching entry. The statements that build the research gap (field methods, l. 52 to 57; numerical and drone co-analysis, l. 57 to 60; landslide seismology, l. 61 to 63) rest wholly or mostly on these works, so a reader cannot trace the state of the art from which the gap in l. 63 to 64 is derived. The results are not affected; the traceability of the introduction is. |
| Suggestion | Add complete entries for the 13 missing works to the reference list or remove the citations; state whether "Zhang et al., 2024" and "Fan et al., 2020" refer to the entries at l. 594 to 596 and l. 533 to 536 and align the years. |
| Status | verified (citation to entry comparison in the text and on the page images p. 1, 2, 26 to 29); share inferred (computed) |
| Severity | moderate |
| Source | S4 |

**GB-06 A published reconstruction of the pre-failure surface of a historical, valley-damming rock avalanche for runout modelling is missing as a reference point for the restoration method.**

| Field | Content |
|---|---|
| Check | P14 |
| Location | p. 2, l. 49 to 51 |
| Quotation | "This paper uses the method of restoring the continuity of contour lines to establish the terrain data before a landslide, which can provide a new idea of terrain restoration before a landslide for the same type of research." |
| Concern | The restoration of the pre-failure terrain is the first method part (l. 77 to 80) and the subject of Conclusion 1 (l. 463 to 468). De Pedrini, A., Ambrosi, C. and Scapozza, C. (2022) 'The 1513 Monte Crenone rock avalanche: numerical model and geomorphological analysis', Geographica Helvetica, 77, pp. 21-37, doi:10.5194/gh-77-21-2022 (open access), faces the same problem for a historical event that dammed a valley and caused an outburst flood: no pre-event maps exist, and the pre-failure surface is reconstructed from boreholes, field evidence and trial-and-error modelling before runout simulation. It is a published alternative to contour continuation and a comparison case for the uncertainty of a restored surface. The work is not in the reference list (checked against all 31 entries). |
| Suggestion | Cite De Pedrini et al. (2022) in l. 42 to 51 and state what contour continuation offers relative to such reconstructions, including how the uncertainty of the restored surface was assessed. |
| Status | verified (open access full text read by instance S1; absence from the reference list checked) |
| Severity | moderate |
| Source | S1 |

**GB-07 The references given for "landslide seismology" include snow avalanche monitoring studies.**

| Field | Content |
|---|---|
| Check | P13 |
| Location | p. 2, l. 61 to 63 |
| Quotation | "In recent years, landslide seismology has taken on more visibility (Navarre et al., 2009; Van Herwijnen and Schweizer, 2011; Helmstetter and Garambois, 2010; Cook et al., 2021; Pandey et al., 2021)" |
| Concern | Pointing to seismic monitoring as a source of direct observation is a useful bridge to the energy question. Van Herwijnen, A. and Schweizer, J. (2011) 'Monitoring avalanche activity using a seismic sensor', Cold Regions Science and Technology, 69, pp. 165-176, concerns snow avalanches detected with a geophone near Davos, not landslides. Navarre et al. (2009) could not be identified unambiguously; the seismic detection work of Navarre and co-authors that could be found also concerns snow avalanches. None of the five works has a reference entry (GB-05), so a reader cannot check which works are meant. |
| Suggestion | In l. 61 to 63 either replace the snow avalanche references by seismological studies of rock landslides or rock avalanches, or broaden the term to "mass-movement seismology", and add full entries for all five works. |
| Status | verified for Van Herwijnen and Schweizer (2011) (open access full text read by instance S1); inferred for Navarre et al. (2009) (not identifiable from the manuscript) |
| Severity | minor |
| Source | S1 |

**GB-08 The gap statement on energy evolution during collisions is made without a described search and is contradicted by a work in the manuscript's own reference list.**

| Field | Content |
|---|---|
| Check | P28 |
| Location | p. 2, l. 63 to 64; reference list p. 27, l. 540 to 542 |
| Quotation | "However, they still lack a quantitative and systematic study of this topic, especially on energy evolution during the collision." |
| Concern | This sentence motivates the central contribution (l. 67 to 69). The reference list contains Ge, Y., Tang, H. and Li, C. (2021) 'Mechanical energy evolution in the propagation of rock avalanches using field survey and numerical simulation', Landslides, 18, pp. 3559-3576, doi:10.1007/s10346-021-01750-1, by the first and the third author of this manuscript, whose title names a quantitative study of mechanical energy evolution in rock avalanche propagation; a text search over all body lines finds no in-text citation of it. Outside the list, Zhang et al. (2022) quantify for the earthquake-triggered Hongshiyan rock avalanche, which the manuscript cites as an example in l. 36, that "64% and 36% of the total energy are dissipated by collision and friction, respectively" (publisher abstract, re-read in the merge; see GB-09). A reader cannot tell what the present study adds beyond Ge et al. (2021). |
| Suggestion | In l. 63 to 64 cite Ge et al. (2021) and the works of GB-09, state in one or two sentences what they already quantified, and narrow the gap to what remains open (for example effective-collision identification per block, or the coupling of energy terms with envelope volume and area); otherwise document the search behind the claim. |
| Status | verified (no search described; Ge et al. (2021) listed but not cited, text search; Zhang et al. (2022) publisher abstract); inferred for the content of Ge et al. (2021) beyond its title (closed access) |
| Severity | moderate |
| Source | S1 |

**GB-09 Two discrete element studies of energy dissipation and fragmentation in earthquake-triggered rock avalanches, which anticipate part of the contribution, are missing from the reference list.**

| Field | Content |
|---|---|
| Check | P14 |
| Location | p. 2, l. 63 to 64 and l. 65 to 69 |
| Quotation | "it focuses on revealing the mechanisms of energy accumulation, transfer, and dissipation during the landslide event" |
| Concern | Contribution in one sentence: a 3DEC simulation of the 1786 Mogangling landslide on a contour-restored terrain, used to quantify potential, kinetic and dissipated energy for the whole mass and ten blocks, to identify effective collisions from velocity peaks, and to relate energy to alpha-shape volume and area growth. Two works missing from the list address the same coupling: (1) Zhang, S., Yin, Y., Li, H., Wang, W. and Zhou, J. (2022) 'Transport process and mechanism of the Hongshiyan rock avalanche triggered by the 2014 Ludian earthquake, China', Landslides, 19, pp. 1987-2004, doi:10.1007/s10346-022-01878-8: DEM simulation, energy partition into collision (64 %) and friction (36 %) dissipation, and the progression from disintegration to fragmentation, for a case the manuscript already cites (l. 36). (2) Gao, G., Meguid, M.A., Chouinard, L. and Xu, C. (2020) 'Insights into the transport and fragmentation characteristics of earthquake-induced rock avalanche: numerical study', International Journal of Geomechanics, 20(9), doi:10.1061/(ASCE)GM.1943-5622.0001800: calibrated DEM of the Tangjia Valley rock avalanche tracing energy conversion and fragmentation along the runout. Neither work is in the reference list (31 entries checked). |
| Suggestion | Add both works in the introduction after l. 63 and state how the present energy terms and the effective-collision approach differ from their energy partition and fragmentation analysis; compare the Mogangling energy partition with the Hongshiyan values where possible. |
| Status | verified (Zhang et al., 2022: publisher abstract, re-read in the merge; Gao et al., 2020: abstract read by instance S1; absence from the reference list checked) |
| Severity | moderate |
| Source | S1 |

**GB-10 The conclusions do not return to the stated purpose (early warning, risk mitigation, hazard evaluation for the Dadu River) or to the core terms "energy accumulation" and "long-runout", and the manuscript has no discussion against prior work.**

| Field | Content |
|---|---|
| Check | P15 |
| Location | p. 2, l. 65 to 73; p. 2, l. 61 to 64; p. 5, l. 122 to 125; p. 1, l. 1 to 3 (title); p. 25 to 26, l. 460 to 492 |
| Quotation | "it focuses on revealing the mechanisms of energy accumulation, transfer, and dissipation during the landslide event" (l. 67 to 68); "The findings are intended to provide a theoretical foundation and scientific support for early warning and risk mitigation of high-altitude and long-runout landslides triggered by intense earthquakes." |
| Concern | Energy transfer and dissipation are taken up in Conclusions 3 and 4, movement in Conclusion 2. Not taken up in Sections 3 and 4: "energy accumulation" (only occurrence of the phrase l. 68; later occurrences of "accumulation" refer to the deposit), early warning and risk mitigation (only l. 72 to 73), the evaluation basis for potential landslides in the Dadu River area (l. 122 to 125), the gap of landslide seismology (l. 61 to 64), and "long-runout" (title, l. 60, l. 73 only; no conclusion addresses runout or mobility). There is no discussion section: the results are not compared with the earlier studies of the same landslide or of energy evolution that the reference list contains (GB-45). A reader cannot see whether and how the conclusions serve the purpose for which the study was undertaken. |
| Suggestion | Add a discussion section before Sect. 4 that relates the results to prior work and states the limits of the simulation; state in Sect. 4 what the results imply for early warning and hazard evaluation in the Dadu River area, or remove this purpose from l. 71 to 73 and l. 122 to 125; address energy accumulation and runout in the conclusions or remove them from l. 68 and the framing. |
| Status | verified (term occurrences counted in the text and checked on the page images) |
| Severity | moderate |
| Source | S4 |

#### Minor corrections

| ID | Location | Quotation | Replacement | Source |
|---|---|---|---|---|
| KK-01 | p. 1, l. 13 | "610041 ,China" | "610041, China" | S4 |
| KK-02 | p. 1, l. 21; p. 3, l. 84 | "dissipation energy" | "dissipated energy (DE)" at l. 21 and "dissipated energy" at l. 84, as defined in l. 241 to 242 | S2 |
| KK-03 | p. 1, l. 23; p. 3, l. 88 to 89; p. 14, l. 272 and l. 281; p. 23, l. 426 | "the Alpha shape algorithm"; "alpha shape"; "An alpha-shape algorithm"; "the Alpha Shape algorithm"; "Alpha Shape envelope fitting" | "alpha-shape algorithm" and "alpha-shape envelope fitting" throughout | S2, S4 |
| KK-04 | p. 1, l. 27 to 28 | "conservation of energy; For some blocks" and "rock mass; Compared with" | "conservation of energy; for some blocks" and "rock mass; compared with" | S4 |
| KK-05 | p. 1, l. 32 | "Landslide is a common and widespread geological disaster, which causes great loss of life and property." | "Landslides are a common and widespread geological hazard that cause great loss of life and property." | S1 |
| KK-06 | p. 1, l. 33; p. 2, l. 39 to 40 | "high-level rock landslides"; "high-level rock landslide" | "high-altitude rock landslides" (term of the title, l. 1, and of l. 73) | S1 |
| KK-07 | p. 1, l. 34; p. 2, l. 56 to 57; p. 27, l. 530 to 536 | "Fan et al., 2019a" (l. 34); "Fan et al., 2019" (l. 56 to 57); two entries "Fan, X., ... 2019." without suffix | "Fan et al., 2019a" and "Fan et al., 2019b" in the text, with matching suffixes "2019a" and "2019b" in the two entries | S4 |
| KK-08 | p. 1, l. 34 to 35 | "such as donghekou landslide debris flow dammed lake" | "such as the Donghekou landslide, debris flow and dammed lake" | S1, S4 |
| KK-09 | p. 1, l. 36 | "Wang, 2021" | "Wang et al., 2021" (the entry at l. 581 to 584 has seven authors) | S1, S4 |
| KK-10 | p. 1, l. 37; p. 28, l. 575 to 577 | "Tian et al., 2017" (entry ends "2016.") | "Tian et al., 2016", or the year of the entry changed to 2017, so that text and entry agree | S4 |
| KK-11 | p. 1 to 2, l. 38 to 39 | "the Mogangling landslide that occurred in 1786 was repaired and reconstructed" | "the pre-failure topography of the Mogangling landslide that occurred in 1786 was reconstructed" | S1, S4 |
| KK-12 | p. 2, l. 44 | "UAV impact" | "UAV imagery" | S1, S4 |
| KK-13 | p. 2, l. 46 | "Song at al.2017" | "Song et al., 2017" | S1, S4 |
| KK-14 | p. 2, l. 48 to 49; p. 27, l. 521 to 523 | "Cheng 2014" | "Cheng and Yu-Sheng, 2014", as in the entry "Cheng, F., and Yu-Sheng, L."; check whether "Yu-Sheng" is the surname or the given name of the second author and correct entry and citation together | S1, S4 |
| KK-15 | p. 2, l. 57; p. 29, l. 600 to 602 | "Zhao et al., 2020" (entry ends "2021.") | "Zhao et al., 2021" | S4 |
| KK-16 | p. 2, l. 73; p. 26, l. 508 to 510; p. 27, l. 524 to 526; p. 28, l. 562 to 568; p. 29, l. 597 to 599 | "altitude" in "high-altitude" (l. 73) and the entries Bernardie et al., Dahal et al., Nava et al., Sinčić et al. and Zhang, K. et al. are set in grey, the five entries also in smaller, unjustified type (page images) | all text in the same black typeface; the five entries in the size and justification of the other entries | S4 |

#### Verification log

| ID | Check | Checked | Values | Result |
|---|---|---|---|---|
| PP-01 | P13 | All statements in Segment 1 that attribute findings, rankings or evaluations to cited works: l. 33 to 34 (trend), l. 34 to 37 (Donghekou and Hongshiyan examples), l. 42 to 49 (restoration practice), l. 52 to 59 (methods), l. 60 to 64 (seismology, gap). The abstract (l. 15 to 30) contains no attributed statement. | Hu et al. (2017): 235 coseismic Ludian landslides interpreted; Tian et al. (2016): 1,053 coseismic and 284 pre-earthquake landslides; both general Ludian studies, acceptable for the Ludian example. Du et al. (2021): DEM simulation of a paleo-earthquake-triggered landslide; Cheng and Yu-Sheng (2014): UDEC dynamic response; both fit l. 47 to 49. Sun et al. (2011), Wang et al. (2014), Wang et al. (2021): titles name the Donghekou landslide and the Wenchuan earthquake, consistent with l. 34 to 36. The 13 works without entry (GB-05) were not traced. | no finding beyond GB-02, GB-04, GB-07; the manuscript does not disclose limits of its literature base |
| PP-02 | P14 | Literature search for the contribution of the manuscript: six queries (Mogangling simulation; earthquake-induced rock avalanche DEM energy dissipation; reconstruction of pre-failure topography; ancient rock avalanche 3D DEM; alpha shape envelope of landslide deposits; pre-event topography back-analysis, open access) | Candidates and comparison with the list: Zhou et al. (2024), Zhao et al. (2021), Ge et al. (2021) already in the list (Ge et al. treated as a citation change in GB-08); Yang et al. (2021, Frontiers 9, 720872) and Steger et al. (EGU2018-8846) same field only; Zhang et al. (2022), Gao et al. (2020), De Pedrini et al. (2022) not in the list, proposed. No alpha-shape precedent for landslide deposits found. | findings GB-06 and GB-09; no further finding |
| PP-03 | P28 | Gap and novelty sentences in Segment 1: l. 42, l. 46 to 47, l. 49 to 51, l. 60 to 61 ("direct observation data are rarely available"), l. 63 to 64 | Search description in the manuscript: none (no database, terms, period or date in l. 31 to 73). l. 60 to 61 is consistent with the cited seismology literature, whose stated rationale is the rarity of direct observation. | no finding for l. 60 to 61; findings GB-03 and GB-08 |

### Segment 2: Methods (p. 2 to 15, l. 74 to 296)

#### Substantive findings

**GB-11 The overview announces "three parts" but lists four, and the four parts carry different names in the overview, in Fig. 1 and in the headings of Sects. 2.1 to 2.4.**

| Field | Content |
|---|---|
| Check | P38 |
| Location | p. 2 to 3, l. 76 to 90; Fig. 1 (p. 4, l. 91); p. 5, l. 92; p. 11, l. 214; p. 12, l. 240; p. 14, l. 269 |
| Quotation | "the research method involves three parts: (1) surface terrain restoration" (l. 76 to 77); "(3) Energy evolution analysis" (l. 83); "(4) Extraction of volume and area of landslide accumulation area" |
| Concern | Fig. 1 is a useful map of the method and has four blocks, matching the four numbered items (1) to (4) of l. 77 to 90, whereas l. 77 announces "three parts" (confirmed on the page image p. 3). Part (1) is "surface terrain restoration" in l. 77 but "Geo-mechanical Model Building" in Fig. 1 and Sect. 2.1; part (3) is "Energy evolution analysis" (l. 83), "Analysis of Energy Evolution During Block Motion" (Fig. 1) and "Energy evolution" (Sect. 2.3); part (4) is "Extraction of volume and area of landslide accumulation area" (l. 87 to 88, Fig. 1) and "Structural extraction of landslide accumulation area" (Sect. 2.4); part (2) "Analysis of Landslide Evolution Process" (l. 80, Fig. 1) corresponds to Sect. 2.2 "Effective collision identification" only in part. A reader cannot match the overview items to the sections by name. |
| Suggestion | Replace "three parts" by "four parts" in l. 77; use one name per part in l. 77 to 90, in the left column of Fig. 1 and in the headings at l. 92, l. 214, l. 240 and l. 269, and add the section number to each item of the overview. |
| Status | verified (pages 3, 4, 5, 11, 12, 14) |
| Severity | minor |
| Source | S2, AB, S4 |

**GB-12 Several figures have axes without titles or units and symbols or abbreviations that are explained neither in the figure nor in the caption.**

| Field | Content |
|---|---|
| Check | P29 |
| Location | Fig. 1 (p. 4); Fig. 3b (p. 8); Fig. 4 (p. 10); Fig. 6 (p. 14); Figs. 7h to 7n (p. 18); Figs. 8, 9 and 12 (p. 20 to 25); Fig. 11 (p. 23 to 24) |
| Quotation | "Fig1. Flow chart of the proposed method of this study" |
| Concern | Fig. 3b has elevation (1000 to 2000) and distance (0 to 1500) without axis title or unit; Fig. 6 has three axes with numbers only; the stress sections of Fig. 7 likewise. PE, KE and DE are defined in the text (l. 241 to 243) but in none of the captions of Figs. 8, 9 and 12; the notation P₀E, PₜE, KₜE in Fig. 1 is used nowhere else; the geological symbols in the legend of Fig. 4 are not spelled out (they are in Fig. 2c). The caption of Fig. 11 does not say that the inset shows the simulated mass and the main view the envelope. Each figure has to be read together with the text. |
| Suggestion | Add axis titles with units to Figs. 3b, 6 and 7h to 7n; resolve PE, KE and DE in the captions of Figs. 8, 9 and 12, the geological symbols in the caption of Fig. 4 and the notation of Fig. 1 in its caption; say in the caption of Fig. 11 what inset and main view show. |
| Status | verified (page images) |
| Severity | minor |
| Source | AB |

**GB-13 The landslide marker in Fig. 2a lies about one degree of longitude west of the coordinates given in the text.**

| Field | Content |
|---|---|
| Check | P3 |
| Location | p. 5, l. 95 to 96; Fig. 2a, marker "Mogangling landslide" (p. 6) |
| Quotation | "The coordinates of the landslide center are: 29 ° 37 ′ 30.726 ″ north latitude, 102 ° 09 ′ 41.190 ″ east longitude." |
| Concern | Fig. 2a carries graticule ticks, so the marker can be measured. On a 600 dpi render the 100°E and 102°E ticks interpolate to x = 419.25 px and 730.0 px at the marker height; the marker centre lies at x = 601.5 px, i.e. 101.17 ± 0.01°E. The text gives 102°09′41.19″E = 102.161°E (computed). The difference of 0.99° corresponds to 0.99 × 111.32 km × cos(29.6°) = 96 km (computed). The latitude reads 29.55°N against 29.625°N; this smaller difference can arise from the curvature of parallels in a conic projection and is not raised. Either the marker or the graticule labels are shifted by about one degree. |
| Suggestion | Place the marker in Fig. 2a at 102.16°E, 29.63°N, or correct the graticule labels, and state the projection of panel (a). |
| Status | verified (measured position); which of marker or graticule is wrong: inferred |
| Severity | minor |
| Source | AB |

**GB-14 Statements on the state of research and practice in Sects. 2 and 2.1 carry no source, although they justify the choice of site and method.**

| Field | Content |
|---|---|
| Check | P13, P28 |
| Location | p. 5, l. 99 to 100; p. 5, l. 113 to 121; p. 9, l. 168 to 170 |
| Quotation | "the effect of seismic force on slope instability has been underestimated to a certain extent" (l. 113 to 114); "When the development background and laws of these major earthquake landslides have not been fully studied in detail" (l. 120 to 121); "the three-dimensional discrete element program (3DEC), one of the most widely used numerical methods in rock mechanics" |
| Concern | Sections 2 to 4 contain no citation at all (text search; see GB-05). Section 2.1 nevertheless makes claims about the field that need a source or a described basis: that "nearly 20 large and super large earthquake landslides are densely distributed here (from the Detuo Guza river section)" (l. 99 to 100); that the effect of seismic force on slope instability "has been underestimated" (l. 113 to 114); that analyses of seismic instability of high steep slopes and of resulting dam failures "are relatively few" (l. 117 to 119); that the laws of these landslides "have not been fully studied in detail" (l. 120 to 121); and that 3DEC is "one of the most widely used numerical methods in rock mechanics" (l. 169 to 170). The first four statements carry the relevance argument for the Dadu River site (l. 122 to 125). The uncited comparison of the Kangding and Wenchuan earthquakes (l. 187 to 189) is treated in GB-24. This finding arises from the merge: the hints of instances S1 and S4 named these places, and no instance whose checklist covers sourcing (P13, P28) was responsible for Segment 2. |
| Suggestion | Give a source for the landslide count of l. 99 to 100 and for 3DEC usage in l. 169 to 170; support the statements of l. 113 to 121 with studies or a described search, or reformulate them as the authors' assessment. |
| Status | verified (absence of any citation in the quoted places, text search and page images p. 5 and 9) |
| Severity | moderate |
| Source | ZF |

**GB-15 The geological units carry different names and codes in the text and in the legends of Figs. 2c, 3a, 3b and 4, and two units appear only in the text or only in the figures.**

| Field | Content |
|---|---|
| Check | P38, P3 |
| Location | p. 5, l. 101 to 107; p. 7, l. 155; Fig. 2c legend (p. 6); Fig. 3a and Fig. 3b legends (p. 8); Fig. 4 legend (p. 10) |
| Quotation | "The sand slate of the Triassic Baiguowan formation (T3bg) is exposed on the left bank of the Dadu River. The quaternary system mainly includes landslide accumulation (Q4del), colluvial Deluvial deposit (Q4col+dl) and alluvial deposit (Q4al)" |
| Concern | Same code, different names: Q4del is "landslide accumulation" (l. 104) and "Rubble soil" (Fig. 2c), with no entry in Figs. 3a and 3b; Q4col+dl is "colluvial Deluvial deposit" (l. 105, twice), "colluvial deposits" (l. 155) and "Massive gravel" (Fig. 2c, Fig. 3b); Q4al is "alluvial deposit" (l. 105) and "Sand and pebble gravel" (Figs. 2c, 3a, 3b); γO2 is "Jinning plagioclase granite" (l. 101 to 102), "Plagiogranite" (Fig. 2c) and "Granite" (Figs. 3a, 3b). The quartz diorite "(O2)" of l. 102 appears in Figs. 3a and 3b as "Diorite" without code and is absent from Fig. 2c; Figs. 3a and 3b also contain "Massive gravelly soils", which has no counterpart in the text or in Fig. 2c. Only in the figures: γM2 "Hybrid granite" (Fig. 2c, Fig. 4). Only in the text: T3bg sand slate on the left bank (l. 103 to 104); Fig. 2c shows the river flowing south, so its left bank is the eastern side, where the map shows γM2, Q4col+dl and Q4al and no T3bg. A reader cannot tell which unit of the section Fig. 3b corresponds to which map unit of Fig. 2c, although Fig. 3b is the section a-a' of Fig. 2c. Are T3bg and γM2 the same left-bank unit under two names, or does Fig. 2c not reach the T3bg outcrop? Is "(O2)" meant as a code of the same intrusive series as γO2? Is "Massive gravelly soils" the deposit Q4del? In addition "quaternary" (l. 104) and "colluvial Deluvial" (l. 105) are misspelt. |
| Suggestion | Give one unit list (code, lithology, genesis) in Sect. 2.1 after l. 107 and use the same code and name in l. 101 to 107, l. 155 and the legends of Figs. 2c, 3a, 3b and 4; add to each legend the units the panel shows; show T3bg in Fig. 2c or correct l. 103 to 104; explain or correct "(O2)" at l. 102; write "Quaternary" and "colluvial-deluvial deposit". |
| Status | verified (names and codes in text and legends on the page images p. 5, 6, 8 and 10); assumption for the identity of T3bg and γM2, the meaning of "(O2)" and of "Massive gravelly soils", put as questions |
| Severity | minor |
| Source | S2, AB, S4 |

**GB-16 The remote sensing image, the base map and the geological map of Fig. 2 and the tablet record have no stated provenance, and the data statement does not cover third-party sources.**

| Field | Content |
|---|---|
| Check | P12 |
| Location | p. 6, l. 126 to 127 and Figs. 2a to 2c; p. 6, l. 136 to 138; p. 26, l. 505 to 506 |
| Quotation | "(b) remote sensing image of Mogangling; and (c) engineering geological map" (l. 126 to 127); "only the Tiezhuang Temple tablet unearthed in the 1980s has records of earthquake landslide, river dam break, and water discharge" |
| Concern | The remote sensing image of Fig. 2b and the base map of Fig. 2a carry no source or acquisition date; for the engineering geological map of Fig. 2c it is not stated whether it is the authors' own mapping or adapted from a published map. The tablet record (l. 136 to 138) has no reference. The data statement (l. 505 to 506) speaks only of data "available from the first author" and says nothing about third-party sources. The provenance of the seismic input record is treated in GB-24. Whether the authors may pass these data on is not stated; is redistribution permitted? |
| Suggestion | Give source and date of the image and the base map and the origin of the geological map in the caption of Fig. 2 (l. 126 to 127); add a reference for the tablet record at l. 137; list the third-party sources with their access conditions in the data statement (l. 505 to 506). |
| Status | verified (absence of provenance in text, captions and statement, pages 6 and 26); assumption whether redistribution is permitted, put as a question |
| Severity | moderate |
| Source | S2 |

**GB-17 Labels in eight figures are smaller than 6 pt at print size, down to about 3 pt.**

| Field | Content |
|---|---|
| Check | P29 |
| Location | Fig. 2a and Fig. 2c (p. 6); Fig. 3c (p. 9); Fig. 5 (p. 12); Fig. 7 (p. 17 to 18); Fig. 9 (p. 21 to 22); Fig. 10 (p. 23); Fig. 11 (p. 23 to 24); Fig. 12 (p. 25) |
| Quotation | "Fig11. Comparison of the overall envelope fitting of the landslide at 10 different times" |
| Concern | Cap or digit heights measured on 300 dpi renders (size in pt = px / 3, ±0.6 pt): Fig. 3c contour labels 2.7 to 3.0 pt; Fig. 11 axis numbers 3.0 pt; Fig. 12 annotations ("1116.8", "29.47") 3.3 pt; Fig. 5b to 5f inset tick labels 3.3 to 3.7 pt; Fig. 2c legend subscripts 3.7 pt; Fig. 10a Z tick labels 4.7 pt; Fig. 12 tick labels 4.7 to 5.0 pt; Fig. 5a, Fig. 7, Fig. 9 and Fig. 10b tick labels 5.0 to 5.3 pt; Fig. 2a scale bar numbers 5.7 pt. Figs. 1, 3b, 4, 6 and 8 reach 6.3 to 7.7 pt (PP-16). |
| Suggestion | Enlarge all labels to at least 6 pt at print size, first the contour labels of Fig. 3c, the axes of Fig. 11, the annotations of Fig. 12 and the insets of Fig. 5. |
| Status | verified (measured) |
| Severity | minor |
| Source | AB |

**GB-18 The contour restoration is described by three different rules, two of which appear only in Conclusion 1, and the restored surface is not tested against a known terrain.**

| Field | Content |
|---|---|
| Check | P10, P15 |
| Location | p. 6 to 7, l. 138 to 143 and l. 157 to 162; Fig. 1 (p. 4); Fig. 3c (p. 9); p. 2, l. 49 to 51; p. 25, l. 463 to 468 |
| Quotation | "the contour lines corresponding to the sliding bed and accumulation area are modified to be straight" (l. 139 to 140); "The contour line is modified along the extension direction of the mountains on the left and right sides" (l. 157); "their trajectory equations can be extracted as a basis for restoring the contours" (l. 465 to 466); "In such cases, restoration can be guided by referencing other mountain areas within the same stratigraphic unit." |
| Concern | Fig. 1 and Fig. 3 show the workflow clearly ("Curve Straightening", "Curve Regularization", "Deposit Removal"). The rule itself differs between three places: "modified to be straight" (l. 140), "along the extension direction of the mountains" (l. 157) and "trajectory equations" (l. 465 to 466); no trajectory equation is extracted or reported in Sect. 2.1. Conclusion 1(b) says the deposit area "is often difficult to restore" and proposes referencing other mountain areas of the same stratigraphic unit (l. 466 to 468), which Sect. 2.1 does not report as applied; the deposit removal named in Fig. 1 is not described in the text. The method is presented as a contribution (l. 49 to 51), but there is no comparison with a terrain of known pre-event shape and no volume uncertainty, although the restored volume determines the sliding mass and every energy value (GB-20). The only check is visual (l. 161 to 162); the authors disclose that the restored surface is smooth, and "preliminary" (l. 463) matches this disclosure, which is not raised again. |
| Suggestion | Give the restoration rule in Sect. 2.1 as an algorithm (which contours, which interpolation, how trajectory equations are fitted, how the deposit is removed and to which valley floor) and show the result in Fig. 3; test it on a landslide with a pre-event DEM and report the volume and elevation error; report the restored sliding volume with an uncertainty range. Otherwise reduce Conclusion 1 to what was done and present (a) and (b) as suggestions for future work. |
| Status | verified (three rule wordings; no trajectory equations and no test reported) |
| Severity | moderate |
| Source | SD, S4 |

**GB-19 Fig. 3a, cited for a division of the landslide area into four parts, shows only two zones.**

| Field | Content |
|---|---|
| Check | P3 |
| Location | p. 7, l. 144 to 146; Fig. 3a (p. 8) |
| Quotation | "As shown in Fig3.(a), the geometric model of the terrain surface is established according to DEM. The whole landslide occurrence area can be divided into four parts: the rock wall area, colluvial slope area, slope debris flow area, and main accumulation area." |
| Concern | Fig. 3a marks two zones, "I Sliding bed" and "II Accumulation area", separated by a dotted red line (page image p. 8). The rock wall area, colluvial slope area, slope debris flow area and main accumulation area are not marked, and the elevation ranges of l. 151 to 156 (1120 to 1330 m, 1330 to 1380 m, 1380 to 1600 m, 1600 to 1890 m) are shown in no figure. |
| Suggestion | Mark the four parts with their elevation ranges in Fig. 3a or in the profile Fig. 3b, or change l. 144 to 146 to the two zones that the figure shows. |
| Status | verified |
| Severity | minor |
| Source | AB |

**GB-20 The size of the simulated sliding mass is undefined: the text gives three incompatible volumes and two lengths, the map shows a larger landslide, and the energy level of Fig. 8 fits none of the stated volumes.**

| Field | Content |
|---|---|
| Check | P1, P2, P9, P3 |
| Location | p. 7, l. 149 to 151; p. 9, l. 173 to 174 and l. 181 to 182; Fig. 2c (p. 6); Table 2 (p. 13, l. 267); Fig. 8 (p. 20, l. 390); Fig. 12a (p. 25); p. 16, l. 330 |
| Quotation | "about 450 m long, about 1000 m wide along the river, and a planar area of 0.45 km2. The average thickness of the landslide mass is about 100 m, and the volume is about 2400×104 m3" (l. 149 to 151); "The length of the landslide mass in the sliding direction is 1021 m" (l. 173 to 174); "the volume of the landslide is 317563 m3" |
| Concern | The model geometry itself is well documented in Fig. 4. The numbers, however, do not describe one body (Python): (1) 450 m × 1000 m = 0.45 km² is consistent, but times 100 m gives 4.5 × 10⁷ m³, not 2.4 × 10⁷ m³ (factor 1.875). Zhao et al. (2021), which is in the reference list (l. 600 to 602) and cited once in l. 57 as "Zhao et al., 2020", give in their abstract a volume of about 4500 × 10⁴ m³ with 450 m length and 1000 m width (re-read in the merge). (2) The model volume, 317,563 m³ (l. 182), is 1/75.6 of 2.4 × 10⁷ m³; the length is 450 m in l. 149 but 1021 m in the sliding direction in l. 174. (3) The landslide boundary drawn in Fig. 2c encloses 1.03 km² and extends 1258 m along the sliding direction of 75° and 1035 m across it (measured by instance AB, scale 2.194 m/px); the deposit unit Q4del alone has 0.475 km². (4) An 8.7 m × 8.7 m column has 75.69 m²; the Table 2 block volumes of 756.2 to 1754.3 m³ imply block heights of 10.0 to 23.2 m, whereas l. 178 to 179 define the height as the full distance from surface to sliding bed and the mean thickness is about 100 m; 317,563 m³ divided by the mean Table 2 block volume of 1,151 m³ is about 276 blocks, against 0.45 km² / 75.69 m² = 5,945 columns. (5) Energy: the initial total in Fig. 8 measures 6,503 to 6,523 GJ (instances S3, AB and SD). With the landslide density 2300 kg/m³ (Table 1), 317,563 m³ gives 7.30 × 10⁸ kg and a mean drop of 908 m, more than the whole relief of 747 m + 131 m = 878 m (l. 174 to 175); 2.4 × 10⁷ m³ gives 12.0 m and 4.5 × 10⁷ m³ 6.4 m, far below the drops of 29.8 to 312.7 m implied for the monitored blocks (GB-29). The kinetic energy maximum of Fig. 8, 1,687 ± 5 GJ at about 13.6 s (instance AB; SD measured 1,683 GJ), would need an rms velocity of 68.0 m/s for 7.30 × 10⁸ kg, the label 1116.8 GJ of Fig. 12a 55.3 m/s; both exceed the maximum velocity of 31.6 m/s (l. 330), which caps the kinetic energy of this mass at 365 GJ. At the mean block drop of 169.0 m, 6,512 GJ corresponds to about 1.7 × 10⁶ m³. The energies thus fit a mass of roughly 1 to 2 × 10⁶ m³, which matches none of the stated volumes. Possible resolutions, put as questions: do l. 149 to 151 describe the present deposit and l. 174 and l. 182 the restored source mass? Is 317563 a typing error? Does the energy calculation use another density, a subset of blocks or a sum over blocks not stated in Sect. 2.3? The grade is major rather than moderate because the body that was simulated determines all absolute energies, the velocities and the runout, i.e. the reconstruction of the Mogangling event that the study aims at (l. 66 to 67), and the deposit comparison of Fig. 7o. |
| Suggestion | Give in Sect. 2.1 one table with length, width, area, thickness and volume for the present deposit, the restored source mass and the simulated sliding mass, with the number of sliding blocks and their mean volume; correct l. 151 or explain the factor between area × thickness and the stated volume, and cite Zhao et al. (2021) at l. 147 to 151; state in Sect. 2.3 the mass, the density and the set of blocks summed for Figs. 8 and 12. If the simulated body is smaller than the landslide, rebuild the model with the restored volume or restrict the claims to a scaled model. |
| Status | verified (stated numbers in l. 149 to 151, l. 173 to 174, l. 182; Zhao et al. (2021) abstract); verified by measurement (Fig. 8 total and kinetic energy maximum; Fig. 2c areas); inferred (implied drops, velocities and masses, computed in Python); assumption (resolutions, put as questions) |
| Severity | major |
| Source | S3, SD, AB, S4 |

**GB-21 The section b-b' announced in the text is drawn in no figure.**

| Field | Content |
|---|---|
| Check | P3 |
| Location | p. 7, l. 159 to 160; Fig. 2c (p. 6); Fig. 3b (p. 8) |
| Quotation | "As shown in Fig3. (b), make a section along a-a'and b-b' in Fig2. (c)." |
| Concern | Fig. 2c contains one section line, labelled "a" at both ends, without prime and without b. Fig. 3b shows only the profile "(a-a')". Fig. 3c, which l. 160 gives for the results, shows contour maps and terrain models, not sections. The drawn line in Fig. 2c measures 1552 m (instance AB), which fits the 0 to 1500 m axis of Fig. 3b, so the one section is consistent; the second is missing. The sentence is also not grammatical as a description. |
| Suggestion | Add section b-b' to Fig. 2c and its profile to Fig. 3, or replace l. 159 to 160 by "Fig. 3b shows the section along line a-a' in Fig. 2c."; label the ends of the line in Fig. 2c as a and a'. |
| Status | verified |
| Severity | minor |
| Source | AB, S4 |

**GB-22 Result-relevant settings of the computing and survey environment are missing.**

| Field | Content |
|---|---|
| Check | P35 |
| Location | p. 9, l. 168 to 170 and l. 178; p. 10, l. 193 to 202; p. 13, l. 258 to 259; p. 14, l. 272 and l. 283; p. 11, l. 227 to 233; p. 6, l. 130 to 135 |
| Quotation | "the three-dimensional discrete element program (3DEC), one of the most widely used numerical methods in rock mechanics, is used to simulate the motion process" |
| Concern | Boundary conditions are described carefully (l. 193 to 202). Missing are: the 3DEC version; rigid or deformable blocks and zone size; mechanical damping (type and value) during the dynamic stage; time step; contact law beyond the Table 1 values; the convergence criterion and the value reached for the static equilibrium the manuscript itself requires (l. 199 to 200) and for the "maximum unbalanced force" used to verify post-failure stability (l. 258 to 259), which is shown nowhere; UAV device, survey date and DEM resolution; the software used for the alpha shape and for the peak detection. Damping and block deformability enter the dissipated energy, the main quantity of the paper; how large their effect is here, the authors can answer. |
| Suggestion | Add a table "Model and processing settings" to Sect. 2 with these entries, including the unbalanced force ratio reached before dynamic loading, and deposit the 3DEC input files with the code (l. 494 to 495). |
| Status | verified (absence); assumption (size of the damping effect in this model, put as a question) |
| Severity | moderate |
| Source | SD |

**GB-23 The model materials and interfaces have different names in the text, in Table 1 and in Fig. 4, and no statement says which parameter set belongs to which model unit.**

| Field | Content |
|---|---|
| Check | P38, P3 |
| Location | p. 9, l. 179 to 181; Fig. 4 legend (p. 10, l. 192); p. 11, l. 207 to 210; Table 1 (p. 11, l. 213), rows "bed rock", "landslide mass", "discontinuities", "potential discontinuities" |
| Quotation | "The slope is underlain by plagioclase granite, which is subdivided into strongly weathered and moderately weathered zones." (l. 207 to 209); "A uniform structural plane is set inside. According to the geological engineering drawing, different strata are generated and marked with different colors." |
| Concern | Rock mass: the text has "strongly weathered" and "moderately weathered" zones (2 names), Table 1 "bed rock" and "landslide mass" (2 parameter sets, densities 2700 and 2300 kg/m³), and the legend of Fig. 4 four units, γo2, Qdel, γM2 and "Sliding mass". Interfaces: the text has "fully developed potential rupture planes" and "joint sets" (l. 209 to 210) and "A uniform structural plane" (l. 179 to 180), Table 1 "discontinuities" and "potential discontinuities". A plausible reading is that "landslide mass" is the strongly weathered zone and the "Sliding mass" of Fig. 4, "bed rock" the moderately weathered zone, "potential discontinuities" the "potential rupture planes" and "discontinuities" the "joint sets"; the manuscript does not say so. In particular it does not say which of the two rock parameter sets the three base units γo2, Qdel and γM2 receive (four units against two sets), nor where each interface type is placed. Is this reading correct, and is the cyan Qdel unit modelled as landslide mass, as bedrock or with a third set? |
| Suggestion | Add a column "model unit" to Table 1 that names, for each parameter set, the units of Fig. 4 and the zones of l. 208 to 209 it applies to, and state where each interface type is placed; use one name per unit and per interface type in l. 179 to 181, l. 207 to 210, Table 1 and the legend of Fig. 4. |
| Status | verified (names in text, Table 1 and Fig. 4 legend, pages 9 to 11); assumption (correspondence between the names, put as a question) |
| Severity | moderate |
| Source | S2, AB |

**GB-24 The substitute input motion is disclosed, but its justification is uncited and partly contradicted within the manuscript, the record is not identified, and its effect on the results is not tested.**

| Field | Content |
|---|---|
| Check | P17, P29, P12 |
| Location | p. 10, l. 183 to 191; Fig. 4 inset and caption (p. 10, l. 192); p. 5, l. 97 to 99; p. 7, l. 146 to 147 |
| Quotation | "It is worth noting that both the Mogangling landslide and the Wenchuan earthquake zone belong to the tectonic system of the Longmenshan Fault Zone. Extensive research indicates that the Kangding earthquake is comparable to the 2008 Wenchuan earthquake" (l. 186 to 188); "this study adopts the acceleration records measured at the Luding station during the Wenchuan earthquake as the input ground motion" |
| Concern | The authors state openly that no record exists for 1786 (l. 183 to 186). Not drawn to the end: (1) "Extensive research" carries no citation. (2) The manuscript places the site at the intersection of the Xianshuihe, Longmenshan and Anninghe faults (l. 97 to 99) and names the Dadu River (Detuo) fault at the slope (l. 146 to 147); the reference list names the trigger the "1786 Moxi M 7.75 earthquake" (Zhao et al., 2021, l. 600 to 601), whose abstract links the landslide to the Detuo fault crossing the slope foot (re-read in the merge). The assignment of the site to the Longmenshan system needs a source. (3) The record is identified only as "the Luding station during the Wenchuan earthquake": no data provider, station code, record identifier, component, duration, processing or scaling is given. The inset of Fig. 4 shows one trace in gal whose horizontal axis has no title, unit or tick labels; the marks tp, tPGA, tf and te are explained nowhere; the caption mentions neither inset nor station; the trace exceeds the ±100 gal ticks (instance SD measured about +250 and -210 gal). (4) No run with another record or amplitude exists, although all stage velocities (5.9 to 31.6 m/s), the duration of 131 s and the energy partition depend on this one input. The unmeasured amplification claim of l. 316 to 318 is treated in GB-33. Whether the record represents near-field shaking of an M 7.75 event at the site is a question the manuscript does not address. The grade is major because the reconstruction of the Mogangling event is the first aim and every reported value is conditional on this input. |
| Suggestion | In Sect. 2.1 cite the source for the tectonic comparison; give provider, station code, record identifier, component(s), duration, PGA, scaling and processing of the record; give the inset of Fig. 4 a time axis with unit and explain tp, tPGA, tf and te in the caption. Add a sensitivity study (for example two or three further records, or the same record scaled to a site PGA estimated for the 1786 event) reporting runout, peak velocity and energy partition per run. |
| Status | verified (missing citation, internal statements, missing record metadata, inset on the page image, Table 2 contents); verified by measurement (inset peak, instance SD); assumption (adequacy of the record for the 1786 event, put as a question) |
| Severity | major |
| Source | SD, AB, S2 |

**GB-25 The provenance of the Table 1 parameters and the target of the "parameter inversion" are not stated.**

| Field | Content |
|---|---|
| Check | P8 |
| Location | p. 11, l. 206 to 213 (Table 1) |
| Quotation | "the selection of physical-mechanical parameters was based primarily on laboratory testing, empirical analogy, and parameter inversion" |
| Concern | Table 1 gives complete values for rock and joints. Which value comes from which of the three sources is not stated; the laboratory tests (samples, number, test type) are not described; and the observation against which parameters were inverted is not named. If the inversion target was the present deposit, the same deposit cannot serve as independent validation (GB-37). The step cannot be rebuilt. |
| Suggestion | Add a column "source" to Table 1 (laboratory test with sample, analogy with reference, inversion), describe the tests in Sect. 2.1, and state the inversion target and objective function. |
| Status | verified |
| Severity | moderate |
| Source | SD |

**GB-26 The abscissa of the velocity curve used to detect effective collisions is called travel distance in some places and displacement in others, and it is not defined.**

| Field | Content |
|---|---|
| Check | P38 |
| Location | p. 11, l. 220 to 234; p. 1, l. 22 to 23; Fig. 1 (p. 4); Figs. 5a to 5f, x-axes (p. 12); Fig. 10b (p. 23, l. 423 to 424); p. 25, l. 473 to 475 |
| Quotation | "presents a typical velocity-travel-distance curve for an individual block" (l. 221); "the effective collision of blocks in the process of landslide is obtained by extracting the local peak value of the displacement velocity curve" (l. 22 to 23); "effective block collisions during the landslide can be identified by extracting local peaks from displacement-velocity curves" |
| Concern | The definition of effective collisions in l. 220 to 234 is concrete and illustrated by five threshold variants. The curve is named "velocity-travel-distance curve" (l. 221), "velocity-distance profile" (l. 225), "velocity-distance curve" (l. 227), "travel-distance versus velocity profile" (l. 234), "displacement velocity curve" (l. 23) and "displacement-velocity curves" (l. 474 to 475); the axis label is "Travel distance (m)" in Fig. 1, Fig. 5a and Fig. 10b and "Travel Displacement (m)" in Figs. 5b to 5f. Path length and displacement are different quantities. The axes of Figs. 5b to 5f and 10b reach 2,500 m, whereas the slide mass is 1021 m long in the sliding direction with its toe 179 m from the river (l. 174 to 175), which suggests a cumulative path length. Instance S3 read the wordings as one quantity and recorded no finding; the merge raises it because the prominence criterion is said to depend on each peak's "height, width, and position" (l. 228), so the abscissa enters the count of 1,139. Is the abscissa the cumulative path length of the block or the magnitude of its displacement from the start? |
| Suggestion | Define the abscissa once in Sect. 2.2 (l. 220 to 221), use one term, for example "velocity versus travel-distance curve", in l. 22 to 23, l. 221 to 234 and l. 474 to 475, and label all axes of Fig. 5 and Fig. 10b identically. |
| Status | verified (names in text and axis labels, pages 1, 4, 11, 12, 23, 25); inferred (dependence of the count on the abscissa, from l. 228; path length reading, from the axis range) |
| Severity | moderate |
| Source | S2, S1, S4, SD |

**GB-27 Velocity peaks are equated with collisions without a check against contact data, the 30 % threshold has no reference quantity and is set by eye, and the population behind the 1,139 effective collisions is not stated.**

| Field | Content |
|---|---|
| Check | P31, P20 |
| Location | p. 11, l. 224 to 234; Fig. 5 (p. 12, l. 235 to 239); p. 22, l. 414 to 421; Fig. 10b (p. 23, l. 423 to 424); p. 25, l. 473 to 475 |
| Quotation | "effective collisions can be detected by pinpointing the significant local maxima on the velocity-distance profile" (l. 224 to 225); "At a threshold of 30%, however, the identification of effective collisions is deemed acceptable. Under this setting, 1,139 effective collisions were detected from the travel-distance versus velocity profile." |
| Concern | Fig. 5 shows the threshold variants transparently. (1) What is detected is a velocity maximum, not a collision. A block also accelerates through the seismic shaking at the base, through gravity on slopes of 50 to 57° (l. 153 to 156) and after "a brief airborne trajectory" (l. 331); these causes are not separated. (2) The prominence threshold is given in per cent without reference quantity, and one number is said to quantify each peak's "height, width, and position" (l. 228); 30 % is chosen because the identification "is deemed acceptable" (l. 233), a visual judgement; no detected peak is checked against the contact histories of the code, so precision and recall are unknown. (3) The population is not stated: the quotation names one "profile"; the 1,139 collisions may belong to the block of Fig. 5, to the ten monitored blocks or to all blocks of the model (25,345 blocks, l. 181). The 26 points of Fig. 10b sum to 1,215.6 (values measured by instance AB at 600 dpi; S3 and SD read about 1,213), close to 1,139, which suggests that Fig. 10b distributes the collisions over 100 m bins, but the manuscript does not say so; panel 5d (30 %) shows about 115 to 130 red markers (estimate of instance AB), not 1,139. The axis "Frequency" has no unit, and pooled counts are not divided by the number of blocks still moving in each bin. For ten blocks the mean would be 1,139 / 10 = 113.9 collisions per block (computed). (4) Conclusion 2 states that effective collisions "can be identified" (l. 473 to 474), which is stronger than this evidence. The grade is major because Conclusion 4 and the abstract statement on compression frequency rest on these counts (GB-40). |
| Suggestion | In Sect. 2.2 define the prominence (reference value, tool, function and parameters) and state which blocks and profiles yield 1,139; state the unit, bin width and pooling of Fig. 10b in its caption. Verify the detector against the contact histories of the monitored blocks and report precision and recall for the thresholds 10 to 50 %; run a control without base excitation after initiation to separate seismic acceleration from collisions; normalise the binned counts by the number of contributing blocks. |
| Status | verified (wording; absence of a contact check, of a reference quantity and of the population); verified by measurement (Fig. 10b values and marker estimate in Fig. 5d, instance AB); inferred (pooling over bins, per-block mean) |
| Severity | major |
| Source | SD, S3, AB, S4 |

**GB-28 In Fig. 5, two red markers of panel (a) sit on rising flanks, panel (a) shows negative velocities, and the curve of panels (b) to (f) is unidentified and peaks at about 45 m/s, above the 31.6 m/s reported as maximum.**

| Field | Content |
|---|---|
| Check | P3, P29 |
| Location | Fig. 5a and Figs. 5b to 5f (p. 12, l. 235 to 239); p. 11, l. 220 to 225; p. 16, l. 330 |
| Quotation | "(highlighted in red) yield a substantial velocity increase" (l. 223); "As shown in Fig7. (e) and (l), during the impact-at-base stage, the maximum velocity reached 31.6 m/s." |
| Concern | The text defines effective collisions as pronounced local velocity peaks marked red (l. 221 to 225). Measured on a 600 dpi render of Fig. 5a (uncertainty ±0.017 m/s, ±0.57 m): the red marker at 243.4 m (13.05 m/s) is followed at 261.5 m by a higher point (13.41 m/s) without marker; the red marker at 463.3 m (4.21 m/s) is followed at 475.7 m by 4.84 m/s. Both sit on rising flanks; the other four red markers (48, 190, 308, 448 m) are local maxima. The lowest points near 590 m lie at -0.34 m/s, below zero, on an axis "Velocity (m/s)". Fig. 5a is "a typical velocity-travel-distance curve for an individual block" (l. 221) and ends at about 590 m with at most 13.5 m/s; the curve of Figs. 5b to 5f is a different one (to 2403 m, peak 44.9 ± 0.1 m/s at 255 m in panel d), and neither caption nor text says which block or aggregate it shows. The field maximum reported in l. 330 is 31.6 m/s at 12 s, equal to the colour bar of Fig. 7e (PP-27). Does the peak fall between the snapshot times of Fig. 7, or is a different quantity plotted, for example a signed velocity component? |
| Suggestion | Place the red markers of Fig. 5a on the local maxima that the detection returns, or explain why flank points are flagged; state in the caption of Fig. 5 whether speed or a velocity component is plotted and which block or aggregate panels (b) to (f) show; explain the 45 m/s against the 31.6 m/s of l. 330. |
| Status | verified (measured positions and peak, instance AB); assumption (cause of the negative values and of the velocity difference, put as questions) |
| Severity | moderate |
| Source | AB |

**GB-29 The stated potential-energy datum does not match Figs. 8 and 9: the initial block energies imply block-specific reference levels.**

| Field | Content |
|---|---|
| Check | P5, P3, P23 |
| Location | p. 13, l. 251 to 255; Fig. 8 (p. 20); Figs. 9a to 9j (p. 21 to 22); Table 2 (p. 13, l. 267); Fig. 10a (p. 23) |
| Quotation | "Since the initial velocity is 0, ME(t0) reduces to the initial potential energy." (l. 252); "uses the model’s initial height as the reference datum rather than true sea level; only the change in potential energy due to relative displacement is considered" |
| Concern | Read literally, a datum at each block's initial height gives PE(t0) = 0 and hence ME(t0) = 0. Figs. 8 and 9 instead start with the full stack as PE, and PE falls to about zero at the end in most panels. With m = V × 2300 kg/m³ (Table 1, Table 2) and the measured initial totals of Fig. 9 (instance S3; AB within 0.07 GJ), E0 / (m g) gives 238.1, 222.1, 233.9, 163.2, 312.7, 172.3, 29.8, 193.0, 82.2 and 43.0 m for points 1 to 10 (mean 169.0 m, computed). With one common datum these heights would increase with the initial elevation z of Table 2 (340 to 755 m); instead point 7 at z = 661 m gives 29.8 m and point 1 at z = 340 m gives 238.1 m. Each block thus appears to be referred to its own final or lowest elevation, against which blocks 1 and 3 show the PE "rebound" of l. 397 to 399. Fig. 10a suggests vertical displacements of several hundred metres for points 1, 2, 3 and 5, more than the heights above, but its perspective box could not be calibrated. Which datum was used? The absolute energy scale of Figs. 8, 9 and 12 cannot be reproduced; the qualitative statements remain. |
| Suggestion | State in Sect. 2.3 the datum actually used (common elevation, per-block final elevation or per-block minimum) and say so in the captions of Figs. 8 and 9; add a table next to Table 2 with mass, initial and final elevation, initial PE and vertical displacement of the ten blocks. |
| Status | verified (wording; initial totals of Fig. 9 measured by instances S3 and AB); inferred (implied heights and block-specific datum, computed); comparison with Fig. 10a inferred, put as a question |
| Severity | moderate |
| Source | SD, AB, S3 |

**GB-30 Fig. 6 swaps the labels of the two middle zones, its ten points carry no IDs, and the coordinate frame of Table 2 is not that of the figure axes, so the monitored blocks cannot be located.**

| Field | Content |
|---|---|
| Check | P38, P3 |
| Location | p. 13, l. 256 to 259; Table 2 (p. 13, l. 267), columns "Position", "ID", "Coordinate", row ID 11; Fig. 6 (p. 14, l. 268); Fig. 10a legend (p. 23); p. 20, l. 397; p. 22, l. 416 |
| Quotation | "ten monitoring points were installed in the lower, lower-middle, upper-middle, and upper portions of the slide mass" (l. 256 to 257); "Fig6. Location of 10 monitoring points" |
| Concern | Table 2 links "point", "Block" and "ID" through its title. (a) Order: Table 2 lists bottom (IDs 1 and 2, z = 340 to 355 m), lower middle (IDs 3 to 5, z = 465 to 498 m), upper middle (IDs 6 to 8, z = 660 to 692 m) and top (IDs 9 and 10, z = 752 to 755 m). In Fig. 6 the zone below "Top" is labelled "Lower middle part" and the next "Upper middle part" (page image p. 14); by the z values the zone next to the top is the upper middle part. The dot counts per zone (2, 3, 3, 2 from the top, PP-23) match Table 2 and cannot distinguish the middle zones. (b) The ten dots have no IDs and no colour key, and their colours do not follow Fig. 10a, where ID 1 is red and ID 3 magenta; in Fig. 6 the red and the magenta dot lie in the top zone, although Table 2 places IDs 1 and 3 at the bottom and in the lower middle part. Blocks 1 and 3, on which the rebound argument of l. 397 to 398 and l. 416 rests, cannot be located. (c) Table 2 gives coordinates such as (-79,-284,340) and (-719,120,755), while the axes of Figs. 4 and 6 run from 0 to more than 3200 m; the frame of Table 2 is not named. (d) Row ID 11, "Maximum unbalanced force", stands in a table of "blocks where the 10 monitoring points are located", although it is no block; instance S3 accepted the explanation in l. 258 to 259, the merge keeps it as a point of form. The text also says "lower" and "upper" (l. 256 to 257) where Table 2 says "bottom" and "top". |
| Suggestion | Swap the two middle labels in Fig. 6 (or correct Table 2 if the figure is right), print the ID 1 to 10 next to each dot in the line colours of Fig. 10a, give the axes titles and units, name the coordinate frame and its origin in the header of Table 2, move "Maximum unbalanced force" out of the ID column into a note, and write "in the bottom, lower middle, upper middle and top parts" in l. 256 to 257. |
| Status | verified (labels, dot positions and colours on pages 14 and 23; Table 2 values on page 13); inferred (that the zone next to "Top" is the upper middle part, from the z values) |
| Severity | moderate |
| Source | S2, AB, S4, SD |

**GB-31 The alpha-shape envelope is not specified: the enveloped object has at least nine names, the input points, the alpha convention and the meaning of V0 and S0 are not stated, and the claimed tight fit with alpha = 1 at all times is not tested.**

| Field | Content |
|---|---|
| Check | P26, P38 |
| Location | p. 14, l. 270 to 284; p. 1, l. 24; p. 3, l. 88; Fig. 1 (p. 4); p. 23, l. 426 to 429; Fig. 11 (p. 23 to 24, l. 437 to 438); p. 24, l. 449 and l. 452; Fig. 12 caption (p. 25, l. 458); p. 26, l. 491 |
| Quotation | "An alpha-shape algorithm is applied to the slide mass to generate an enclosing envelope" (l. 272 to 273); "this study uniformly sets the α value to 1. This approach ensures a tight fit of the envelope model while minimizing geometric deviations introduced by parameter tuning" (l. 282 to 284); "extract the volume and surface area of the landslide body from 3D point cloud data" |
| Concern | Fixing alpha avoids tuning, and Eqs. (5) and (6) are explicit. The enveloped object is called "landslide accumulation area" (l. 88, heading l. 269, Fig. 1), "deposition zone" (l. 270, l. 272), "slide mass" (l. 272), "landslide mass" (l. 278 to 279), "deposit mass" (l. 427, l. 449, l. 491), "deposit region" (l. 429), "the landslide" (l. 437), "sliding mass" (l. 458) and "monitored block group" (l. 452). Fig. 11a (t = 0 s) shows the envelope of the intact source mass, so "deposition zone", "accumulation area" and "deposit" name a body that does not yet exist at the reference time of V0 and S0; "monitored block group" elsewhere means the ten blocks of Table 2. The abstract gives the input as "3D point cloud data" (l. 24), a term the Methods use for the UAV terrain data (l. 133, l. 141, l. 159), whereas l. 426 says "numerical simulation data". Not stated: which points enter (block centroids, vertices, grid points), the alpha convention and unit (radius in m or its inverse), and whether V0 and S0 are envelope values at t = 0 or the block volume of l. 182 (l. 278 defines V0 as "the initial volume of the landslide mass", Vt as "the volume of the enclosing envelope"). The tight fit is not tested at any time, and its basis changes along the run: as blocks disperse, point spacing grows, so one alpha cannot give the same tightness at 0 s and at 131 s; VS reaches about 1250 % and AG about 4300 % (Fig. 12 axes). Which blocks are enveloped at each time step, and is V0 the envelope at t = 0 s? |
| Suggestion | Define in Sect. 2.4 the enveloped object once (for example "all blocks of the sliding mass in the 3DEC model at time t"), the input points, the alpha convention and unit, and V0 and S0 as envelope values at t = 0 if that is so; use this one name in l. 24, l. 88, l. 269 to 272, l. 426 to 429, l. 449, l. 452, l. 491 and the captions of Figs. 11 and 12, and replace "3D point cloud data" in l. 24 by the simulation output. Add a sensitivity of VS and AG for at least three alpha values and report whether the values 29.47 % and 319.5 % change. |
| Status | verified (names with line numbers; missing specifications; Fig. 11a on page 23; Fig. 12 axis range); inferred (dependence of tightness on point spacing); assumption (what is enveloped and what V0 means, put as a question) |
| Severity | moderate |
| Source | SD, S2 |

**GB-32 The two indices VS and AG appear under seven names, partly as "rate", and the surface area has two symbols.**

| Field | Content |
|---|---|
| Check | P38 |
| Location | p. 14, l. 275 to 280; p. 1, l. 25; p. 3, l. 89; Fig. 1 (p. 4); p. 15, l. 287 to 288; p. 24, l. 440 to 441; p. 25, l. 453; Fig. 12 axes and caption (p. 25, l. 458 to 459); p. 26, l. 488 |
| Quotation | "volume swelling (VS) and area growth (AG)" (l. 275); "we first extracted its volume (V) and surface area (A) at each time point, based on which the volume expansion rate (VS) and surface area growth rate (AG) were calculated" (l. 440 to 441); "(a) as a function of volume; (b) as a function of area." |
| Concern | VS is "volume expansion rate" (l. 25, l. 89, l. 441, l. 453), "volume swelling" (l. 275, l. 287 to 288, Fig. 1, Fig. 12a axis "Volume Swelling (%)") and "volume expansion" (l. 488). AG is "area growth rate" (l. 25), "surface area growth rate" (l. 89, l. 441), "area growth" (l. 275, l. 288, Fig. 1, Fig. 12b axis "Area Growth (%)") and "surface area growth" (l. 453, l. 488). Eqs. (5) and (6) define relative changes with respect to t = 0, not time derivatives, so "rate" names a different quantity. The surface area is S in Eq. (6) and l. 279 to 280 but A in l. 440. The caption of Fig. 12 says "as a function of volume" and "of area", while the axes show VS and AG in per cent. |
| Suggestion | Use "volume swelling (VS)" and "area growth (AG)" throughout (l. 25, l. 89, l. 441, l. 453, l. 488) and drop "rate"; write "volume (Vt) and surface area (St)" in l. 440; change the caption at l. 458 to 459 to "(a) as a function of volume swelling (VS); (b) as a function of area growth (AG)". |
| Status | verified (all occurrences with line numbers; Fig. 1 and Fig. 12 axes on pages 4 and 25) |
| Severity | minor |
| Source | S2, S3, S4, AB |

#### Minor corrections

| ID | Location | Quotation | Replacement | Source |
|---|---|---|---|---|
| KK-17 | p. 2, l. 76; p. 7, l. 144 and l. 159; p. 15, l. 301; p. 23, l. 428; all captions, l. 91 to 459 | "Fig1."; "Fig3.(a)"; "Fig3. (b)"; "Fig7"; "(Fig11.)" | one form throughout, for example "Fig. 1", "Fig. 3a", "Fig. 7" in the text and "Figure 1." in the captions | S4 |
| KK-18 | p. 5, l. 95 to 96 | "29 ° 37 ′ 30.726 ″ north latitude, 102 ° 09 ′ 41.190 ″ east longitude" (spaces confirmed on the page image) | "29°37′30.726″ N, 102°09′41.190″ E" | S4 |
| KK-19 | p. 5, l. 98 | "of "Y" - shaped faults" | "of Y-shaped faults" | S4 |
| KK-20 | p. 5, l. 111 | "The sudden flood made the downstream area a vast ocean" | "The sudden flood inundated the entire downstream area" | S4 |
| KK-21 | Fig. 2b legend (p. 6); Fig. 3a and Fig. 3b legends (p. 8) | "Daduhe River"; "Dadu river" | "Dadu River" | S2, AB |
| KK-22 | p. 6, l. 132 to 133 | "Convert the geographical coordinate system to the projection coordinate system" | "The geographic coordinates were converted to a projected coordinate system" | S4 |
| KK-23 | p. 7, l. 149 | "distributed along the NEE-SWW direction" | "oriented ENE-WSW" | S4 |
| KK-24 | p. 7, l. 151 | "2400×104 m3" ("104" set on the baseline, page image p. 7) | "2400 × 10⁴ m³" | S4 |
| KK-25 | p. 7, l. 152 | "1120 m-1330m" | "1120 m to 1330 m" | S4 |
| KK-26 | p. 9, l. 176 to 177 | "can not be obtained" | "cannot be obtained" | S4 |
| KK-27 | p. 9, l. 182 | "1121m high" | "1121 m high" | S4 |
| KK-28 | p. 10, l. 193 to 195 | "In the course of a discrete-element simulation-particularly when modeling nominally semi-infinite bodies such as the use of fixed or elastic boundaries in a static analysis will inevitably reflect outbound seismic waves into the model during a subsequent dynamic analysis." | "In discrete-element simulations, particularly of nominally semi-infinite bodies, fixed or elastic boundaries used in a static analysis will reflect outgoing seismic waves back into the model during a subsequent dynamic analysis." | S4 |
| KK-29 | p. 11, Table 1 (l. 213), row "bed rock", column "Rock mass" | "bed rock" | "bedrock" | S4 |
| KK-30 | p. 11, l. 213; p. 13, l. 267 | "Table 1 Physical parameters"; "Table 2: The basic information" | one form for both titles, for example "Table 1. Physical parameters ..." and "Table 2. Basic information ..." | S4 |
| KK-31 | p. 11, l. 218 and l. 228 | "block velocities-hereafter termed" (l. 218); "must be chosen-one that quantifies" (l. 228); hyphens on the page image | "block velocities, hereafter termed"; "must be chosen, one that quantifies" | S4 |
| KK-32 | Fig. 5a legend (p. 12) | "Non-obvios acceleration" | "Non-obvious acceleration" | AB, S4 |
| KK-33 | p. 13, l. 246 | "where, at time ti, PE(ti), and DE(ti) can be expressed as:" | "where KE(ti), PE(ti) and DE(ti) at time ti are given by:" | S4, SD |
| KK-34 | p. 13, l. 251 | "(m/s);h(ti)" | "(m/s); h(ti)" | S4 |

#### Verification log

| ID | Check | Checked | Values | Result |
|---|---|---|---|---|
| PP-04 | P10 | Design sketch from the whole manuscript, captions and declarations: questions, study type, cases, comparison condition, data sources with provenance class, time axis, environment, stated principles, components, disclosed limitations, chain from frame to result | Aims in wording l. 39 to 41 and l. 65 to 73; no research questions or hypotheses, the four method parts (l. 77 to 90) stand in for them; study type single case by 3D DEM with method development; one landslide, one input record, one parameter set, one run, one threshold (30 %), one alpha (1); data sources: UAV DEM (primary, date and resolution not given), restored terrain (model-generated), 2008 Luding record (substitute), Table 1 (mixed, not assigned per value), model output and derived energies, collisions and envelopes (model-generated), field photographs (Fig. 7o), tablet record; disclosed limitations: structural planes ignored (l. 175 to 178), substitute input (l. 183 to 191), smooth terrain (l. 160 to 162), dam break not modelled (l. 349 to 350), weathering (l. 354 to 355, only in the results), deposit restoration difficult (l. 466 to 468, only in the conclusions) | basis for GB-01, GB-18, GB-20, GB-22, GB-24, GB-25, GB-27, GB-31, GB-33, GB-36 to GB-38, GB-40, GB-42, GB-43 |
| PP-05 | P7 | Time axis: versions, protocol changes, runs | event 1786; input record 2008; DEM date not given; one model and one run of 131 s; snapshots at 0, 3, 7, 9, 12, 15, 131 s (Fig. 7) and envelopes at 0, 3, 7, 9, 12, 15, 32, 71, 100, 131 s (Fig. 11); no protocol change reported | no finding (substitute input in GB-24, DEM date in GB-22) |
| PP-06 | P30 | Reported errors and their correction relative to runs | no error or correction reported | no finding |
| PP-07 | P37 | Post-hoc changed values in figures and tables | terrain "corrected by the normal vector" (l. 135) and point cloud filtering are processing steps of Sect. 2.1; no recalculation of results mentioned | no finding |
| PP-08 | P33 | Effort statements | none found ("efforts" in l. 59 refers to the literature) | no finding |
| PP-09 | P25 | Information flow: slide bed in the deposit area; parameters; peak detection | Fig. 1 shows "Deposit Removal" for the slide bed, so the base is restored and the debris does not run onto the present deposit; inversion target unknown (GB-25) | no finding beyond GB-18 and GB-25 |
| PP-10 | P18 | Stated principles applied to the manuscript itself | static equilibrium before dynamic loading (l. 199 to 200): applied according to the text, value not reported (GB-22); uniform alpha (l. 282 to 283): applied, Fig. 1 shows "(α=1)"; datum rule (GB-29) | no further finding |
| PP-11 | P27 | Flow of untested components into results | restored terrain into mass and all energies (GB-18, GB-20); substitute input into all dynamics (GB-24); 30 % threshold into Fig. 10b, Conclusion 4 and the abstract (GB-27, GB-40); fixed alpha into VS, AG and the transition values (GB-31, GB-43) | covered by the cited findings |
| PP-12 | P32 | Independent sample of results called "acceptable" or "successful" | "deemed acceptable" (l. 233), "successful energy extraction" (l. 389): no independent check | included in GB-27 and GB-38 |
| PP-13 | P17 | Location of disclosures | structural planes (l. 175 to 178) and substitute input (l. 183 to 191) disclosed where the model is built; smooth terrain where the restoration is described (l. 160 to 162); weathering only in the results (l. 354 to 355); deposit restoration only in the conclusions (l. 466 to 468) | consequences in GB-24, GB-36, GB-37, GB-18 |
| PP-14 | P36 | Approximate statements against own records | "about 450 m ... 2400×104 m3" (l. 149 to 151) against model numbers: GB-20; "Around 13 seconds" (l. 383) against Fig. 8: KE about 1,683 GJ near 13.6 s and 822 GJ near 14.8 s, consistent; "approximately 29.47%" (l. 453) equals the Fig. 12 label; "approximately 20 meters" (l. 328) has no record (GB-33) | no further finding |
| PP-15 | P29, P3 | Inventory of figures: type, panels, caption, first citation | Fig. 1 flow chart (cited l. 76); Fig. 2 maps a to c (l. 93); Fig. 3 block diagram, profile, contour maps (l. 144); Fig. 4 3D model with inset (l. 173); Fig. 5 six line diagrams (l. 220); Fig. 6 3D model (l. 256); Fig. 7 panels a to o (l. 301); Fig. 8 stacked bars (l. 375); Fig. 9 ten stacked bar charts (l. 393); Fig. 10 trajectories and scatter (l. 414); Fig. 11 ten envelopes (l. 428); Fig. 12 two line diagrams (l. 443); no graphical abstract, no appendix figures; Tables 1 and 2 are typeset text | no finding: numbering 1 to 12 consecutive, every figure cited in its own section |
| PP-16 | P29 | Font size where at least 6 pt | Fig. 1 7.0 pt; Fig. 2a place name 6.3 pt; Fig. 2c legend text 6.0 to 6.3 pt; Fig. 3a legend 7.0 pt; Fig. 3b axis numbers 6.3 pt; Figs. 4 and 6 axis numbers 6.7 pt; Fig. 8 tick labels 7.7 pt | no finding for these labels |
| PP-17 | P3, P29 | Fig. 1 against Sect. 2 (l. 76 to 90) | four coloured blocks (model building, evolution process, energy evolution, volume and area extraction) against items (1) to (4) | no finding beyond GB-11 and GB-12 |
| PP-18 | P3 | Fig. 2 against the text, measured | sliding direction of the section line in Fig. 2c 74.1° against 75° (l. 149); length of the line 1552 m against the axis 0 to 1500 m of Fig. 3b; scale bar segments 90, 93, 90 px for 200 m each; marker latitude 29.55°N against 29.625°N, within the curvature of parallels | no finding beyond GB-13, GB-15, GB-20, GB-21 |
| PP-19 | P1 | Planar area and volume ratios | 450 m × 1000 m = 450,000 m² = 0.45 km²; 2400 × 10⁴ / 317,563 = 75.6; 0.45 km² / 75.69 m² = 5,945 columns; 317,563 m³ / 1,151 m³ = 276 blocks | area consistent; ratios used in GB-20 |
| PP-20 | P3 | Fig. 3, measured | Fig. 3c scale bar 0 to 400 m 89 px, 400 to 800 m 90.5 px, 800 to 1400 m 133 px, ratio 1.48 against 1.5; Fig. 3a block colours match the legend; Fig. 3b elevation axis: water surface at about 1147 m, upper end of the deposit surface 1382 m (text 1380 m); horizontal axis without ticks, so distances and slopes were not measured; absolute elevations not raised because the bar convention of the axis is open (offset up to 25 m) | no finding for scale and colours |
| PP-21 | P3 | Fig. 4 dimension labels against l. 173 to 175 | "1021m", "747m", "179m", "131m" in the figure; 1021 m, 747 m, 179 m, 131 m in the text | no finding |
| PP-22 | P3 | Fig. 5: counts, legend, threshold variants | Fig. 5a 6 red and 5 purple markers plus one of each in the legend; panels b to f labelled 10, 20, 30, 40, 50 % as in the caption and l. 229 to 233 | findings GB-27, GB-28 |
| PP-23 | P3, P5, P2 | Fig. 6 points per zone against Table 2; number of monitoring points across the manuscript | counted at 600 dpi between the dashed lines: 2, 3, 3, 2 points from the top; Table 2: top 2 (IDs 9, 10), upper middle 3 (6 to 8), lower middle 3 (3 to 5), bottom 2 (1, 2); z coordinates 340 to 355, 465 to 498, 660 to 692, 752 to 755 m increase with the zone; "10 monitoring points" in l. 256, l. 262, l. 392, l. 403, Fig. 6, Fig. 9 (ten panels) and Fig. 10 caption; ID 11 is the maximum unbalanced force (l. 258 to 259) | counts agree; labels and IDs in GB-30 |
| PP-24 | P12 | Inventory of data sources and scripts named in Sect. 2 and Figs. 1 to 7 against the code statement (l. 494 to 495), the data statement (l. 505 to 506) and the printed tables | own data on request: UAV DEM and point cloud, restored terrain, laboratory tests, 3DEC model, histories of 10 points and of the unbalanced force, list of 1,139 collisions, envelopes and V, S series, field photographs; scripts on request: peak detection, energy calculation, alpha shape; printed: Table 1, Table 2, Eqs. (1) to (6), threshold 30 %, alpha = 1; third party, not mentioned: Luding record, image Fig. 2b, base map Fig. 2a, map Fig. 2c, tablet; no appendix | findings GB-44, GB-16, GB-24; threshold and alpha are stated and not counted as missing |
| PP-25 | P12 | Links in the code and data statements | 0 URLs and 0 DOIs in l. 494 to 495 and l. 505 to 506 | no finding; nothing to test for reachability |
| PP-26 | P38 | Names checked without finding | "3DEC" uniform (l. 169, l. 196); "Kangding earthquake" uniform (l. 110, l. 183, l. 188); "Moxi" names a town (l. 97), a river (l. 95) and appears in the title of Zhao et al. (2021), different objects or a cited study; "Luding station" (l. 190) and "Luding County" (l. 94, l. 96) different objects; KE, PE, DE, ME defined in l. 241 to 243 and used identically in Eqs. (1) to (4) and Figs. 1, 8, 9, 12; "effective collisions" defined in l. 218 to 219 and used uniformly; "landslide mass", "sliding mass", "slide mass" as generic synonyms for the moving body | no finding (raised only where they name the enveloped object, GB-31) |

### Segment 3: Results (p. 15 to 25, l. 297 to 459)

#### Substantive findings

**GB-33 Section 3.1 mixes model output, mechanism interpretation and field statements without saying which is which, and the field findings are not reported.**

| Field | Content |
|---|---|
| Check | P19 |
| Location | p. 15 to 16, l. 299 to 359; p. 13, l. 264 to 266; p. 25, l. 472 to 473 |
| Quotation | "the sequence of failure and run-out at Mogangling was inferred by integrating the numerical results with field-investigation findings" (l. 265 to 266); "ongoing impacts ultimately led to the formation of a loosely consolidated fractured layer approximately 20 meters thick" |
| Concern | The stage-by-stage description is easy to follow alongside Fig. 7. Of the 40 sentences of Sect. 3.1 (l. 299 to 359), instance SD classified 15 as model output shown in Fig. 7 (times, velocities, contact with the base), 16 as mechanism statements that no reported model quantity shows (P- and S-wave action, tension cracking along structural planes, amplification, brecciation, "fine debris", the "approximately 20 meters" fractured layer, "layered pseudo-bedrock", backflow flooding), 7 as field observations and 2 as framing; 16 / 40 = 40 %. One example: the statement that amplification "significantly increased the peak ground acceleration of the Mogangling slope" (l. 317 to 318) has no measurement, since Table 2 monitors displacement, velocity and stress but no acceleration. With 8.7 m blocks (l. 178) a 20 m layer of fine debris is not resolvable unless it comes from the field; the field investigation itself (dates, methods, observations) is reported nowhere, although the aims (l. 65) and Conclusion 2 (l. 472 to 473) rely on it. |
| Suggestion | Mark each statement in Sect. 3.1 as model output (with the panel of Fig. 7 or a monitored quantity), interpretation, or field observation (with source); add a subsection on the field investigation (dates, methods, observed thickness of the fractured layer, pseudo-bedrock) or cite it; add acceleration histories to the monitoring if amplification is to be claimed, or delete l. 316 to 318; move interpretations without model support to a discussion. |
| Status | verified (wording; absence of a field report); inferred (sentence classification and share, instance SD) |
| Severity | moderate |
| Source | SD |

**GB-34 The stress panels of Fig. 7 (h to n) do not say which stress component and which section they show, and their axes have no titles.**

| Field | Content |
|---|---|
| Check | P29 |
| Location | p. 15, l. 301 to 302; Figs. 7h to 7n (p. 18, l. 363 to 366); caption p. 19, l. 368 to 369; Fig. 7a (p. 17) |
| Quotation | "Fig7 illustrates the cloud maps of velocity distribution for the overall model and stress distribution along the sliding plane" |
| Concern | The panels show a vertical section (horizontal axis 0 to 2700, vertical axis 0 to 1200, both without title or unit) with a colour bar "Stress" from 0 to -31, -33 or -47 MPa. Caption and text name neither the stress component (Table 2 monitors Stress-XX, YY, ZZ), nor the position of the section in the model, nor the sign convention; the text speaks of stress "along the sliding plane", the figure shows a section through the whole model. In panel (a) both ends of the velocity colour bar read "0m/s". |
| Suggestion | State in the caption of Fig. 7 the stress component, the sign convention and the location of the section (for example as a line in Fig. 4 or Fig. 6), add axis titles with units to panels (h) to (n), and correct the colour bar of panel (a). |
| Status | verified (page images p. 17 to 19) |
| Severity | minor |
| Source | AB |

**GB-35 The stage sequence in Sect. 3.1 is given without times, and Sect. 3.2.1 uses other stage names and boundaries, so the two can only be matched through the caption of Fig. 7.**

| Field | Content |
|---|---|
| Check | P22, P2 |
| Location | p. 15 to 16, l. 306, l. 314, l. 322, l. 330, l. 338 and l. 346; p. 19, l. 368 to 369; p. 19, l. 381 to 384 |
| Quotation | "As shown in Fig7. (e) and (l), during the impact-at-base stage, the maximum velocity reached 31.6 m/s." (l. 330); "From 3 to 12 seconds, the landslide experienced rapid initiation" (l. 381); "Around 13 seconds, the sliding mass impacted the riverbed" |
| Concern | Sect. 3.1 names six stages by figure panel only; their times (3, 7, 9, 12, 15 and 131 s) follow only from the caption (l. 368 to 369). Sect. 3.2.1 calls the whole interval from 3 to 12 s "rapid initiation", which in Sect. 3.1 spans three stages (high-speed initiation at 7 s, collapse at 9 s, impact at base at 12 s), and places the impact on the riverbed at about 13 s, between panel (e) at 12 s ("impact-at-base", l. 330) and panel (f) at 15 s ("Upon reaching the Dadu River valley", l. 339). The measured timing of the kinetic energy peak in Fig. 8 (13.6 ± 0.6 s, PP-28) is consistent with "Around 13 seconds"; the issue is that the reader has to combine three places to see that both sections describe the same sequence. |
| Suggestion | Give the time of each stage in Sect. 3.1 (for example "(e) and (l), t = 12 s") and use the same stage names and boundaries in Sect. 3.2.1, or add a short table of stages with time window, maximum velocity and energy state. |
| Status | verified (l. 306 to 346, l. 368 to 369, l. 381 to 384) |
| Severity | minor |
| Source | S3 |

**GB-36 Structural planes are excluded from the model, yet the results explain the failure by structural planes, and Conclusion 2 says the simulation incorporates geological structures.**

| Field | Content |
|---|---|
| Check | P17, P15 |
| Location | p. 15, l. 308 to 313 and l. 323; p. 9, l. 175 to 180; p. 11, l. 208 to 210 and Table 1 (l. 213); p. 25, l. 469 to 470 |
| Quotation | "The first-arriving P-waves caused intense vertical dislocation along the steeply dipping structural planes outside the slope." (l. 308 to 309); "Under the combined influence of structural plane control and strong seismic forces" (l. 323); "the impact of the structural plane on the landslide process has to be ignored in this study" (l. 177 to 178); "Discrete element numerical simulation can incorporate terrain, stratigraphy, geological structures, and boundary conditions" |
| Concern | The manuscript discloses the limitation where the model is built (l. 175 to 178). Its consequences are not drawn: Sect. 3.1 attributes vertical dislocation, tensile cracking "along these structural planes" (l. 310), unloading cracking "along pre-existing potential sliding surfaces" (l. 313) and the collapse to "structural plane control" (l. 323), and Conclusion 2 lists "geological structures" among what the simulation incorporates (l. 469). What the model contains is "A uniform structural plane" (l. 179 to 180) and two joint categories in Table 1 whose orientation and location are not given (GB-23). A steeply dipping plane "outside the slope" cannot act in a model in which the structural planes were ignored, unless the uniform plane or the 8.7 m grid joints are meant; then the mechanism is a property of the artificial block grid, not of the slope. The formation mechanism is a stated aim (l. 39), so the reading of Sect. 3.1 changes. |
| Suggestion | State in Sect. 2.1 the orientation and position of the uniform structural plane and of the two joint categories of Table 1; in Sect. 3.1 remove mechanism statements that depend on unmodelled structural planes, or add model variants with an assumed steep joint set and compare initiation and velocities with the uniform case; delete "geological structures" in l. 469 or describe what was represented. |
| Status | verified |
| Severity | major |
| Source | SD, S4 |

**GB-37 The validation against the field is qualitative, the observed deposit is altered by the dam breach and two centuries of erosion, and Conclusion 2 states that the comparison "ensures" agreement.**

| Field | Content |
|---|---|
| Check | P9, P15 |
| Location | p. 16, l. 353 to 359; Fig. 7o (p. 19, l. 368 to 370); p. 5, l. 110 to 111; p. 16, l. 349 to 350; p. 11, l. 206 to 207; p. 25, l. 471 to 472 |
| Quotation | "Fig7. (o) presents compelling evidence of agreement between the numerical simulation results and the actual field observations." (l. 353 to 354); "Furthermore, the extent and morphology of the accumulated landslide material in the simulation closely match those observed in reality." (l. 357 to 359); "Comparison with field imagery and result analysis ensures that the simulation outcomes align with actual conditions." |
| Concern | The two features compared in Fig. 7o, the ridge that divides the source area and the deposit area, are well chosen. The comparison has no measure (no overlap of footprints, runout distance, deposit elevation, thickness or volume), although the UAV DEM and the profile a-a' (Fig. 3b) would allow it. The present deposit is not the simulated end state: the dam "burst the Dadu River after 9 days" (l. 110 to 111), "significant topographic alterations have resulted from centuries of weathering" (l. 354 to 355), and the simulation ends before the breach (l. 349 to 350). A match of the simulated pre-breach deposit with the post-breach remnant is therefore not expected even for a correct model, and an apparent match may be coincidental. If the parameter inversion (l. 207) used the same deposit, the comparison is not independent (GB-25). "Compelling evidence" and "ensures" state more than a qualitative comparison can give; Conclusion 2 does not carry the disclosed limits (smoothed terrain, ignored structural planes, substitute input). The aim is to reconstruct the dynamic evolution of the Mogangling landslide (l. 66 to 67); without a shown agreement the results describe a model scenario rather than the 1786 event, which is why the grade is major. |
| Suggestion | Add a quantitative comparison in Sect. 3.1: simulated against mapped deposit footprint (overlap ratio), runout distance and the elevation profile along a-a', with an estimate of the volume removed by the breach; separate calibration targets from validation targets; state the erosion limitation where the DEM and the sliding bed are introduced (l. 130 to 136); replace "compelling evidence" (l. 353) and "ensures" (l. 471) by wording that matches a qualitative comparison, and carry the disclosed limits into Conclusion 2. |
| Status | verified (wording; absence of measures); inferred (confounding by breach and erosion, from the manuscript's own statements) |
| Severity | major |
| Source | SD, S4 |

**GB-38 The constant energy total presented as evidence of energy conservation for the whole mass, and its supposed failure for single blocks, are identities of Eq. (4); Figs. 8 and 9 show the same constant total for both.**

| Field | Content |
|---|---|
| Check | P23, P15, P31, P3 |
| Location | p. 19, l. 375 to 377 and l. 387 to 389; p. 12 to 13, Eq. (1) l. 245 and Eq. (4) l. 249; p. 1, l. 26 to 28; p. 20, l. 392 to 396 and l. 399 to 402; p. 25 to 26, l. 476 to 482; Fig. 8 (p. 20); Figs. 9a to 9j (p. 21 to 22) |
| Quotation | "It is evident that, due to the law of energy conservation, the total sum of the three forms of energy remains constant throughout the landslide." (l. 375 to 377); "for the whole landslide, its energy change conforms to the law of conservation of energy; For some blocks, the energy is not conserved" (l. 26 to 28); "unlike the total landslide mass, the energy of single blocks is not conserved" (l. 393 to 394); "Instances where dissipated energy appears to decrease are actually due to the calculation method used." |
| Concern | The energy forms are clearly defined, and the initial state holds only potential energy (l. 252). With ME = KE + PE (Eq. 1) and DE(ti) = ME(t0) - ME(ti) (Eq. 4), KE + PE + DE = ME(t0) at every time for every block and every sum of blocks, whatever the simulation does. The constant total in Fig. 8 therefore confirms the definition, not the law of conservation, and it cannot show "a successful energy extraction numerical simulation" (l. 388 to 389). The same identity holds for single blocks, and the figures show it: three instances measured flat stack tops independently; instance AB found in every panel of Fig. 9 89 to 95 % of the bar columns within ±1.5 px of the median top, with totals of 5.00, 5.07, 3.97, 3.54, 10.93, 6.63, 1.16, 4.32, 1.60 and 0.95 GJ for points 1 to 10, and the top of Fig. 8 at 6,503 to 6,523 GJ. What the text calls non-conservation of single blocks (l. 393 to 394, l. 480 to 482) is an increase of PE + KE that Eq. (4) books as a decrease of DE (l. 399 to 402), visible only as the PE rebound in Figs. 9a and 9c. Two readings are possible. If DE is the residual of Eq. (4), which l. 399 to 400 ("due to the calculation method used") indicates, conservation for the whole mass is true by construction and the only testable quantity is whether DE is non-decreasing; instance SD found no decrease of PE + KE in Fig. 8 (PP-29). If DE were tracked independently by the code, the constant sum would be a real check, but the manuscript does not say so. In either reading the system is open: the seismic input acts at the model base (l. 189 to 191, l. 197 to 198) and the viscous boundaries absorb energy, but the balance has no term for either, so DE lumps friction, damping, boundary work, input work and contact work. The first two results of the abstract and Conclusion 3 thus restate the definition; if the finding holds, what the manuscript can show about conservation changes. |
| Suggestion | State in Sect. 2.3 whether DE is the residual of Eq. (4) or tracked independently. Replace the conservation statements by an energy balance from the code's energy tracking that can leave a residual, for example PE0 + W_input = PE + KE + W_friction + W_damping + W_boundary + U_strain; for single blocks report the work of contact forces separately from frictional dissipation, and quantify the DE decreases per block with their times. Revise the abstract (l. 26 to 28), l. 375 to 377, l. 388 to 389, l. 393 to 394 and Conclusion 3 (l. 476 to 482) accordingly. |
| Status | verified (identity from Eqs. 1 and 4; constant totals in Figs. 8 and 9 measured by instances S3, S4 and AB); inferred (DE computed as residual, from l. 399 to 400; missing input and boundary work, from l. 189 to 191 and l. 197 to 198) |
| Severity | major |
| Source | S3, S4, AB, SD |

**GB-39 Energies of blocks with different masses are compared in absolute terms; normalised by mass, the ranking between positions can reverse.**

| Field | Content |
|---|---|
| Check | P21 |
| Location | p. 20, l. 392 to 396; Figs. 9a to 9j (p. 21 to 22); Table 2 (p. 13, l. 267), column "Volume"; p. 1, l. 29 |
| Quotation | "The dynamic parameters of 10 monitoring points were recorded to determine the energy of individual blocks at different locations." (l. 392 to 393); "the lower rock mass is compressed more frequently, receives more energy transfer" |
| Concern | The ten monitored blocks differ in volume from 756.2 m³ (point 3) to 1754.3 m³ (point 7), a factor of 2.32 (computed), and Fig. 9 gives absolute energies in GJ on different y-axis scales. Absolute energy received or dissipated scales with mass. The measured initial energies divided by mass (2300 kg/m³, Table 1) give 2.34, 2.18, 2.29, 1.60, 3.07, 1.69, 0.29, 1.89, 0.81 and 0.42 kJ/kg for points 1 to 10 (computed). Point 6 (upper middle) has more absolute energy than point 3 (lower middle), 6.58 against 3.99 GJ, but less specific energy, 1.69 against 2.29 kJ/kg. A comparison of energy transfer between positions, as stated in the abstract, can therefore change sign depending on whether it is made per block or per unit mass. The grade is moderate because the results do not yet make this comparison (GB-40); it becomes major if the comparison is added unnormalised. |
| Suggestion | Plot or tabulate specific energies (J/kg) per block in Sect. 3.2.2, or state that the comparison is made per block and give the masses next to the energies, and base the abstract statement on the normalised values. |
| Status | verified (block volumes, Table 2; initial energies measured by instance S3); inferred (specific energies and reversal, computed) |
| Severity | moderate |
| Source | S3 |

**GB-40 The comparison of lower and upper (front and rear) rock mass in the abstract and Conclusion 4 has no basis in the results, and Fig. 10b is described as showing locations it does not show.**

| Field | Content |
|---|---|
| Check | P11, P15, P9, P3 |
| Location | p. 22, l. 414 to 421; Fig. 10 (p. 23, l. 423 to 424); p. 1, l. 28 to 30; p. 3, l. 85 to 87; Table 2 (p. 13, l. 267); p. 26, l. 483 to 487 |
| Quotation | "Compared with the upper rock mass, the lower rock mass is compressed more frequently, receives more energy transfer, and has a longer migration distance." (l. 28 to 30); "presents the frequency of effective collisions experienced by blocks at different locations during the landslide process" (l. 414 to 415); "during the collapse stage, the front portion of the rock mass experiences more collisions than the rear portion, with a clear trend of decreasing collision frequency toward the rear" |
| Concern | The Methods set up the comparison (l. 85 to 87), and Table 2 assigns the ten blocks to four zones (2, 3, 3, 2 blocks). The results do not carry it out: Fig. 10b has one series of 26 points, "Frequency" against "Travel distance (m)", without any distinction of blocks, positions or stages (page image p. 23), although l. 414 to 415 say it shows blocks "at different locations"; no collision count, travel distance or received energy is reported per block or per zone in text or table. Fig. 10a supports only the part on migration distance (trajectories 8, 9 and 10 of the upper blocks are the shortest, PP-31). Conclusion 4 refers to "the collapse stage", which Sect. 3.1 places at 9 s (l. 322), while l. 418 to 419 place the collision peak "once the blocks enter the river channel", a later stage. The causal clause "enabling the front portion to slide farther" (l. 487) rests on co-occurrence; travel distance confounds it, since a block decelerating near the river spends more time per 100 m bin, and the last four bins (2,200 to 2,500 m) hold 595 of 1,215.6 counts, 49 % (computed from the values of instance AB). With 2 or 3 blocks per zone, a zone difference cannot be separated from block-to-block scatter. The position terms change between lower and upper (abstract), bottom to top (Table 2) and front and rear (Conclusion 4) without being related. One of three results of the abstract thus has no reported basis. |
| Suggestion | Add to Sect. 3.2.2 a table with one row per monitored block giving position, effective-collision count (total and per stage), travel distance and energy received (sum of DE decreases or positive contact work), normalised by mass (GB-39); count collisions for all sliding blocks, group them by initial zone, normalise by time in motion and path length, and test the zone difference, for example with a rank test; correct the description of Fig. 10b in l. 414 to 415; otherwise restrict the abstract and Conclusion 4 to what Fig. 10b shows. Align the position terms. |
| Status | verified (absence of position-resolved results in text and Figs. 10a and 10b; Table 2 zones); verified by measurement (Fig. 10b values, instance AB); inferred (confounding, 49 % share, causal argument) |
| Severity | major |
| Source | S3, S4, AB, SD |

**GB-41 The text says the number of collisions "rises continuously" with travel distance, but the plotted counts of Fig. 10b fall five times, and the fitted curve is not explained.**

| Field | Content |
|---|---|
| Check | P6, P29, P3 |
| Location | p. 22, l. 418 to 419; Fig. 10b (p. 23, l. 423 to 424) |
| Quotation | "as the migration distance increases during the landslide, the number of collisions also rises continuously, reaching a peak once the blocks enter the river channel" |
| Concern | The fitted curve rises. The plotted counts, measured by instance AB (600 dpi, ±0.18 per point) and read by instance SD with the same result, fall from 15.9 to 6.9 at 800 m, from 27.0 to 19.9 at 1000 m, from 29.9 to 27.1 at 1300 m, from 157.0 to 150.0 at 2400 m and from 150.0 to 146.0 at 2500 m; the maximum (157.0) lies at 2300 m, not at the end. The red curve has no legend entry, equation, fit type or goodness of fit, and the y-axis "Frequency" does not say per what (GB-27). |
| Suggestion | Replace "rises continuously" by "generally rises" in l. 419, and give fit type, equation and R² of the red curve, the bin width and the definition of "Frequency" in the caption of Fig. 10. |
| Status | verified (measured values) |
| Severity | minor |
| Source | AB, SD |

**GB-42 The envelope values behind Fig. 12 are not reported, Fig. 12 plots about 30 points per curve although envelopes were fitted at "10 representative time points", and its kinetic energy peak of 1116.8 GJ lies below the maximum of Fig. 8.**

| Field | Content |
|---|---|
| Check | P11, P22, P34, P3 |
| Location | p. 23, l. 426 to 428; Fig. 11 (p. 23 to 24, l. 437 to 439); p. 24, l. 440 to 444; Figs. 12a and 12b (p. 25, l. 457 to 459); p. 25, l. 452 to 455; Fig. 8 (p. 20) |
| Quotation | "perform Alpha Shape envelope fitting on the deposit mass at 10 representative time points, extracting the corresponding envelope volumes and surface areas (Fig11.)" (l. 426 to 428); "When the volume expansion rate reaches approximately 29.47% and the surface area growth reaches about 319.5%" |
| Concern | VS and AG are a sound way to compare dispersal over time on a constant basis. V0 and S0, and V and S or VS and AG at the announced time points, are reported nowhere; the text gives only one pair, 29.47 % and 319.5 % (Vt/V0 = 1.2947, St/S0 = 4.195, computed). Each curve of Fig. 12a carries about 30 markers (instance AB counted 33 ± 3 on enlarged crops, SD about 30, S3 more than 20 for DE above VS = 200 % alone), so VS and AG were computed at more than the ten times of Fig. 11; neither the number of evaluation times nor how the ten shown times were chosen (32, 71 and 100 s are irregular) is stated. The kinetic energy peak of Fig. 12 is annotated 1116.8 GJ, while Fig. 8 reaches 1,687 ± 5 GJ at about 13.6 s (instance AB; SD 1,683 GJ). The sampling of Fig. 12 thus misses the kinetic energy maximum of Fig. 8, and the values 29.47 % and 319.5 % do not mark the point where "the kinetic energy peaks" (l. 455). The time of this point is not given. |
| Suggestion | Add to Sect. 3.4 a table with time, V, S, VS, AG, KE, PE and DE for every envelope fit used in Fig. 12, including V0 and S0; state the number of fits, the time step and the rule for selecting the ten times of Fig. 11; use the same time series for Figs. 8 and 12 and give the time of the point VS = 29.47 %. |
| Status | verified (absence of values; marker counts and annotation on the page image); verified by measurement (Fig. 8 kinetic energy maximum, instances AB and SD); inferred (sampling explanation; ratios) |
| Severity | moderate |
| Source | S3, AB, SD |

**GB-43 Fragmentation and a "solid to fluidized" transition are concluded from envelope growth, but no fragmentation measure exists, spreading of unbroken blocks would give the same growth, and Conclusion 5 states as concluded what Sect. 3.4 offers as interpretation.**

| Field | Content |
|---|---|
| Check | P15, P31 |
| Location | p. 24, l. 445 to 452; p. 25, l. 452 to 456; p. 26, l. 488 to 492; p. 14, l. 270 to 284; p. 9, l. 178 to 181; Figs. 11 and 12 (p. 23 to 25); p. 15, l. 319 to 320 |
| Quotation | "This phenomenon can be interpreted as follows" (l. 445); "Simultaneously, the sharp rise of DE shown in the figure further confirms significant fragmentation" (l. 451); "it can be concluded that during energy transfer, collisions and friction cause blocks to fracture and disintegrate, generating a large amount of debris" |
| Concern | VS and AG are a clear dispersion measure. What is measured is the envelope of the block set (l. 272 to 284); the model consists of 25,345 predefined blocks of 8.7 m × 8.7 m (l. 178 to 181), and no breakage mechanism, fragment count or block size distribution is defined in Sect. 2.4 or reported in Sect. 3.4. Sect. 3.4 hedges ("can be interpreted as follows"), Conclusion 5 upgrades to "it can be concluded". The rise of DE (l. 451) cannot "confirm" fragmentation: by Eq. (4) DE is the residual of mechanical energy and contains every loss (GB-38). The mechanism is also not the only one compatible with the data: fragments that "fill the interior" would not enlarge an enclosing envelope, whereas spreading of the mass across the valley would; the manuscript itself calls the quantity "dispersal degree" and "dispersion degree" (l. 270, l. 430), and the axes of Fig. 12 extend to 1400 % (VS) and 5000 % (AG), with the last points beyond 1200 % and 4000 %. The two causes need to be separated. The "solid to fluidized" transition (l. 453 to 454) has no criterion; it is the VS and AG at the sampled time with the highest kinetic energy, which misses the maximum of Fig. 8 (GB-42). Can blocks break in the model beyond the preset joints, and if not, what do "newly formed fragments" (l. 490) refer to? Conclusion 5 restates the interpretation as a finding, so the grade is major. |
| Suggestion | Define and report a fragmentation measure (for example number of separated blocks or broken contacts over time) and a dispersal measure (for example footprint area or spread of block centroids), and show which of them drives VS and AG; state in Sect. 2.1 whether the model permits breakage beyond the preset joints. Until then formulate Conclusion 5 as an interpretation, delete "further confirms" in l. 451, and either define the transition by a criterion evaluated at the full time resolution of Fig. 8 or remove "fluidized phase" from Sect. 3.4 and Sect. 3.1 (l. 319 to 320). |
| Status | verified (absence of a fragmentation measure; change from "can be interpreted" to "it can be concluded"; Fig. 12 axis extent); inferred (alternative cause spreading; DE as residual cannot single out fragmentation); assumption (whether blocks can break in the model, put as a question) |
| Severity | major |
| Source | S4, SD |

#### Minor corrections

| ID | Location | Quotation | Replacement | Source |
|---|---|---|---|---|
| KK-35 | p. 15, l. 301; p. 19, l. 368 to 369 | "Fig7 illustrates the cloud maps"; "cloud map of velocity"; "cloud map of stress" | "Fig. 7 shows the contour maps"; "contour map of velocity"; "contour map of stress" | S4 |
| KK-36 | Figs. 7h to 7n, colour bars (p. 18, l. 363 to 366) | "Mpa" | "MPa" | AB |
| KK-37 | p. 20, l. 397 to 398 | "exhibit a rebound in potential energy after it approaches zero" | "exhibit a rebound in potential energy after their potential energy approaches zero" | S4 |
| KK-38 | p. 22, l. 410 to 413 (Fig. 9 caption); p. 20, l. 397 | "energy evolution of point 1"; "Block 1 and Block 3" | "energy evolution of block 1 (monitoring point 1)", and one term for the monitored blocks throughout | S3 |
| KK-39 | p. 23, l. 425 | "3.4 Structural evolution as a function of energy change" (no Sect. 3.3; Sect. 3.2.2 precedes it) | "3.3 Structural evolution as a function of energy change" | S3, S4, SD |
| KK-40 | p. 24, l. 438 to 439 (Fig. 11 caption; ten times and ten panels a to j) | "(a-i) when time = 0s, 3s, 7s, 9s, 12s, 15s,32s,71s, 100s, 131s" | "(a to j) at t = 0, 3, 7, 9, 12, 15, 32, 71, 100 and 131 s" | S3, S4, SD, AB |

#### Verification log

| ID | Check | Checked | Values | Result |
|---|---|---|---|---|
| PP-27 | P2, P24, P3 | Duration and stage velocities across Sect. 3.1, Fig. 7, Fig. 8 and Fig. 11; colour bar maxima of Fig. 7 | 131 s in l. 300, l. 369, l. 439 and on the time axis of Fig. 8; text maxima 5.9 (l. 307), 19.6 (l. 315), 27.1 (l. 322), 31.6 (l. 330), 25.7 (l. 339) m/s, "approached 0 m/s" (l. 346 to 347); colour bar maxima Fig. 7a to 7g 0, 5.9, 19.6, 27.1, 31.6, 25.7, 0.21 m/s; caption times 0, 3, 7, 9, 12, 15, 131 s in the order of the stages | no finding |
| PP-28 | P24, P3 | Fig. 8 time course against l. 378 to 384 | bars about every 1.23 s; DE first visible at 3.7 s (38 GJ), KE at 4.9 s (139 GJ); KE 446, 580, 671, 767, 1088, 1591, 1687 GJ at 6.2, 7.4, 8.6, 9.9, 11.1, 12.4, 13.6 s; 800 GJ at 14.9 s; total top 6,504 to 6,523 GJ where visible | no finding: peak at 13.6 ± 0.6 s and drop by 14.9 s agree with "From 3 to 12 seconds" and "Around 13 seconds" within the bar width |
| PP-29 | P6 | Absolute statements on monotonic trends | "Dissipated energy continuously increased" (l. 387 to 388): PE + KE in Fig. 8 measured 6197, 6063, 6024, 5910 GJ at about 10.1, 11.3, 12.5, 13.6 s and 4380, 4380, 4303, 4189 GJ at about 17.1, 17.7, 18.8, 20.0 s, no increase found; "continuous increasing trend" of volume and area (l. 428 to 429): x-values in Fig. 12 increase monotonically | no finding (collision trend: GB-41) |
| PP-30 | P3 | Fig. 9, rebound of blocks 1 and 3 (l. 397 to 399) | panel (a): PE reaches 0 near 75 s, last bars 0.415 GJ; panel (c): PE reaches 0 near 85 s, last bars 0.375 GJ; panel (i): slight PE rise between about 25 and 40 s | no finding on the rebound (totals and datum in GB-38, GB-29) |
| PP-31 | P3, P1 | Fig. 10 values and colours; sum of Fig. 10b against 1,139 | Fig. 10b, 26 points from 0 to 2500 m in 100 m steps: 1.0, 1.3, 2.2, 4.7, 5.8, 7.6, 15.0, 15.9, 6.9, 27.0, 19.9, 24.0, 29.9, 27.1, 36.9, 42.0, 48.9, 49.6, 52.9, 61.0, 69.0, 72.0, 142.0, 157.0, 150.0, 146.0; sum 1,215.6 (computed) against 1,139 (6.7 % higher); Fig. 10a legend colours, smallest RGB difference between two series 55; trajectories of 8, 9 and 10 (upper blocks) the shortest | no finding for colours; values used in GB-27, GB-40, GB-41; migration distance part of the abstract supported |
| PP-32 | P1, P3 | VS and AG against Eqs. (5), (6) and the annotations of Fig. 12; Fig. 12 against Fig. 8 | VS 29.47 % gives Vt/V0 = 1.2947, AG 319.5 % gives St/S0 = 4.195; Fig. 12 marks "29.47" and "319.5" at the KE peak "1116.8"; Fig. 12a PE at VS = 0 about 6565 GJ, DE at the end about 6500 GJ (Fig. 8: 6500 GJ); x axes run to about 1250 % (VS) and 4300 % (AG) | no finding on the arithmetic and on PE and DE; sampling in GB-42 |
| PP-33 | P21 | Basis of the time comparisons of the whole mass | Fig. 8 sums the same mass at each step; VS and AG are normalised by V0 and S0 | no finding |

### Segment 4: Conclusions, declarations, references (p. 25 to 29, l. 460 to 605)

#### Substantive findings

**GB-44 The data and code statements withhold every data set and script that the Methods describe "upon reasonable request" without a reason, although none of the data concern persons.**

| Field | Content |
|---|---|
| Check | P12 |
| Location | p. 26, l. 494 to 495 (Code availability) and l. 505 to 506 (Availability of data and material); sources in p. 6, l. 130 to 135; p. 6 to 7, l. 138 to 143 and l. 157 to 162; p. 9, l. 168 to 182; p. 10, l. 193 to 202; p. 11, l. 206 to 207 and l. 226 to 234; p. 13, l. 256 to 264; p. 14, l. 272 to 284; Fig. 7o (p. 19); p. 24, l. 440 to 441 |
| Quotation | "The codes that support the findings of this study are available from the first author, Yunfeng Ge, upon reasonable request." (l. 494 to 495); "The data and materials that support the findings of this study are available from the first author, Yunfeng Ge, upon reasonable request." |
| Concern | The manuscript has both statements and prints the material parameters (Table 1) and the coordinates and volumes of the ten monitored blocks (Table 2). Beyond that, the Methods name eight own data sources, none of which the statements name and all of which are withheld without a reason: (1) the UAV DEM and the post-landslide point cloud (l. 130 to 135); (2) the modified contour lines and the restored terrain (l. 138 to 143, l. 157 to 162); (3) the laboratory test results behind Table 1 (l. 206 to 207); (4) the 3DEC model with 25,345 blocks, material assignment, boundary and loading settings (l. 168 to 182, l. 193 to 202); (5) the histories of the ten monitoring points and of the maximum unbalanced force (l. 256 to 264); (6) the list of the 1,139 effective collisions (l. 233); (7) the envelopes and the volume and area series behind VS and AG (l. 272 to 284, l. 440 to 441); (8) the field photographs (Fig. 7o). Scripts implied by the Methods: the peak detection with prominence threshold (l. 226 to 232), the energy calculation of Eqs. (1) to (4), and the alpha-shape fitting (l. 281 to 284). Of these 8 data sources and 3 script groups, none is deposited and none carries a reason for withholding; none concerns persons. A reader cannot rebuild the model or recompute Figs. 5, 8, 9, 10 and 12. |
| Suggestion | List the items (1) to (8) and the three script groups individually in the statements at l. 494 to 495 and l. 505 to 506 and deposit them in a public repository with a persistent identifier; for any item that cannot be released, state the reason next to it. |
| Status | verified (wording of both statements; list of sources with line numbers); the count of 8 data sources and 3 script groups is inferred from the Methods text |
| Severity | moderate |
| Source | S2 |

**GB-45 Sixteen of the 31 reference entries match no citation in the text, among them the earlier studies of the Mogangling landslide and the first author's study of energy evolution in rock avalanches.**

| Field | Content |
|---|---|
| Check | P4 |
| Location | p. 26, l. 508 to 510 (Bernardie et al.) and l. 514 to 516 (Chang et al.); p. 27, l. 517 to 520 (Chen et al.), l. 524 to 526 (Dahal et al.), l. 537 to 539 (Gao et al.), l. 540 to 542 (Ge et al.), l. 543 to 545 (Gong et al.), l. 546 to 548 (He, J. et al.), l. 549 to 552 (He, K. et al.), l. 553 to 555 (He, N. et al.); p. 28, l. 562 to 565 (Nava et al.), l. 566 to 568 (Sinčić et al.), l. 588 to 590 (Wu, J. et al.), l. 591 to 593 (Yang et al.); p. 29, l. 594 to 596 (Zhang, J. et al.), l. 597 to 599 (Zhang, K. et al.), l. 603 to 605 (Zhou et al.) |
| Quotation | "Wu, J., Wang, Y., Dong, S., Chen, Y., and Wang, L.: Genetic Mechanism and Failure Process of the Mogangling Seismic Landslide" (l. 588 to 589); "Ge, Y., Tang, H., and Li, C.: Mechanical energy evolution in the propagation of rock avalanches using field survey and numerical simulation" |
| Concern | The last in-text citation of the manuscript is in l. 63. Sixteen entries match no citation: Bernardie et al., Chang et al., Chen et al., Dahal et al., Gao et al., Ge et al., Gong et al., He, J. et al., He, K. et al., He, N. et al., Nava et al., Sinčić et al., Wu, J. et al., Yang et al., Zhang, K. et al. and Zhou et al.; 16/31 = 52 % (computed). A seventeenth, Zhang, J. et al. (2023), is cited only if "Zhang et al., 2024" (l. 45 to 46) refers to it (GB-05). The uncited entries include a study of the same landslide (Wu et al., 2013), a study of mechanical energy evolution in rock avalanches by the first and the third author (Ge et al., 2021), a seismic-response study in the Dadu River valley (He, J. et al., 2023) and a study of earthquake-triggered landslides in Moxi Town (Zhou et al., 2024). The second study of the Mogangling landslide in the list, Zhao et al. (2021), is cited once, in l. 57 with the year 2020 (KK-15); instance SD reported it as uncited, which the merge corrected. Because these works treat the same event and the same energy approach, a reader cannot see what the present results add, which is what the novelty statements in l. 49 to 51 and l. 63 to 64 claim. The grade is moderate rather than minor because the omission concerns the traceability of the contribution, not only the form of the list. |
| Suggestion | Cite each entry where it is used or delete it; relate the results of Sects. 3.1 to 3.4 explicitly to Wu et al. (2013), Zhao et al. (2021) and Ge et al. (2021), for example in a discussion section before Sect. 4 (GB-10). |
| Status | verified (citation to entry comparison, text search and page images p. 26 to 29); share inferred (computed) |
| Severity | moderate |
| Source | S4 |

#### Minor corrections

| ID | Location | Quotation | Replacement | Source |
|---|---|---|---|---|
| KK-41 | p. 25, l. 464 and l. 466 | "It should be noted that:(a) Outside"; "restoring the contours;(b) The landslide" | "It should be noted that (a) outside"; "restoring the contours; (b) the landslide" | S4 |
| KK-42 | p. 26, l. 499 | "XF: Data curation, Investigation. LZ: Data curation" | "XF: Data curation, Investigation; LZ: Data curation" | S4 |
| KK-43 | p. 26, l. 507 | "Reference" | "References" | S4 |
| KK-44 | p. 27, l. 530 | "Fan, X., Scaringi, G., Korup, O., et al.:" | the full author list, as in the other 30 entries | S4 |

#### Verification log

| ID | Check | Checked | Values | Result |
|---|---|---|---|---|
| PP-34 | P4, P22 | Numbering of sections, figures, tables and equations, counted on the page images | sections 1, 2, 2.1 to 2.4, 3, 3.1, 3.2, 3.2.1, 3.2.2, 3.4, 4; figures 1 to 12, first called in l. 76, 93, 144, 173, 220, 256, 301, 375, 393, 414, 428, 443 in ascending order, each with one caption; tables 1 (called l. 212) and 2 (l. 259); equations (1) to (6) at l. 245, 247, 248, 249, 276, 277 | no gap or double number in figures, tables and equations; missing Sect. 3.3 in KK-39 |
| PP-35 | P4 | Every call of a figure or table against its target | l. 76 Fig. 1 four parts (GB-11); l. 93 Fig. 2 as stated; l. 144 Fig. 3a (GB-19); l. 159 to 160 section b-b' (GB-21); l. 160 Fig. 3c as stated; l. 173 Fig. 4 dimensions equal l. 174 to 175; l. 212 Table 1 as stated; l. 220 to 233 Fig. 5 thresholds equal the caption; l. 256 Fig. 6 (GB-30); l. 259 Table 2 IDs 1 to 10 plus 11 as stated in l. 258 to 259; l. 301 to 353 Fig. 7a to 7o, panel pairs and times as stated; l. 375 Fig. 8 and l. 393 Fig. 9 as stated, PE rebound of blocks 1 and 3 visible in Figs. 9a and 9c; l. 414 Fig. 10b (GB-40); l. 428 Fig. 11 (KK-40); l. 443 Fig. 12 labels 1116.8, 29.47 and 319.5 equal l. 453 to 454 | no finding beyond those named |
| PP-36 | P4 | In-text citations against the reference list in both directions; year, spelling, "et al." | 28 citation instances with 29 author-year keys, all in l. 34 to 63, none in Sects. 2 to 4; 31 entries; 14 keys matched to an entry, 6 of them with a deviation of year or form (Tian 2017/2016, Zhao 2020/2021, Wang 2021 without "et al.", Cheng 2014 without second author, "Song at al.2017", "Fan et al., 2019a" without a "2019b"); 2 keys with only a candidate entry of another year and 13 keys without entry (GB-05); entries without citation 16 plus 1 candidate (GB-45) | GB-05, GB-45, KK-07, KK-09, KK-10, KK-13, KK-14, KK-15; DOIs not resolved (optional check) |
| PP-37 | P15 | Each statement of Sect. 4 against a place in Sect. 3 | C1 restoration along adjacent ridges: l. 157 to 158, Fig. 3c; trajectory equations and C1(b): no place (GB-18). C2 terrain, strata, boundaries: l. 168 to 202; geological structures contradicted by l. 175 to 178 (GB-36); extraction of KE, PE, DE: Fig. 9; agreement with reality: Fig. 7o, qualitative (GB-37); collision identification: Sect. 2.2 (GB-27). C3 monotonic DE of the whole mass: Fig. 8; conservation: identity (GB-38). C4: no position- or stage-resolved place (GB-40). C5: interpretation l. 445 to 452 only (GB-43). Results not carried into Sect. 4: duration 131 s, transition at VS 29.47 % and AG 319.5 % | findings as named; the omission of the two results is the authors' choice, no finding |
| PP-38 | P15, P9 | Proposals and outlook, each against an own result | no outlook section and no proposed follow-up study; proposals found: trajectory equations (l. 465 to 466) and reference to other mountain areas (l. 467 to 468), not applied (GB-18); contour restoration as "a new idea" (l. 49 to 51), restored surface not checked (GB-03, GB-18); basis for early warning (l. 71 to 73) and for the Dadu River area (l. 122 to 125), not returned to (GB-10) | no proposal declared consistent; covered by the cited findings |
| PP-39 | P15 | Strength of verbs in Sects. 3 and 4 against their evidence | "ensures" l. 471 and "compelling evidence" l. 353 (GB-37); "can be identified" l. 473 to 474 (GB-27); "obeys the law of energy conservation" l. 477 to 478 and "due to the law of energy conservation" l. 376 (GB-38); "it can be concluded" l. 483 (GB-40) and l. 489 (GB-43); "a clear trend" l. 485 (GB-40); "further confirms" l. 451 (GB-43); "a preliminary restoration" l. 463 matched to l. 160 to 162; "it is clear that ... the number of collisions also rises" l. 418 to 419 matched to the overall trend of Fig. 10b | no finding beyond those named |
| PP-40 | P15 | Core terms and aims of title and introduction in Sects. 3 and 4 | energy transfer: 13 occurrences, in Conclusions 3 to 5; dissipation: Conclusions 3 and 4; trajectory and movement: Sect. 3.1, Fig. 10a, Conclusion 2; structural evolution (title): Sect. 3.4, Conclusion 5; energy accumulation: l. 68 only; long-runout: title, l. 60, l. 73 only; early warning and mitigation: l. 72 to 73 only; Dadu River hazard evaluation: l. 122 to 125 only; landslide seismology: l. 61 to 64 only | GB-10 |
| PP-41 | P16 | Language and typesetting of all 29 pages on the page images; observations that appear only in the extracted text | not raised because the page image is correct: missing "=" and "+" in Eqs. (1) to (4) and the fraction bars of Eqs. (5) and (6); sub- and superscripts in "γO2", "Q4del", "Q4col+dl", "km2", "m3" (except l. 151, KK-24); "c Author(s)" in the page header; "Ms7 ¾" (l. 110); long dashes in l. 357, l. 397 and l. 478 are set correctly | no finding beyond the minor corrections listed |
| PP-42 | P16 | Uniformity of the reference list | 31 entries in alphabetical order; all 31 with DOI in the form "https://doi.org/..." followed by the year; book chapters (Hu et al., Song et al.) and preprints (Dahal et al., Yang et al.) each in one pattern; journal abbreviations consistent | deviations in KK-16, KK-07, KK-43, KK-44 |
| PP-43 | P16 | Form of the Statements and Declarations | five items present (code, contributions, competing interests, funding, data); initials YG, BH, HT, XF, LZ correspond to the five authors; three grant numbers given | punctuation in KK-42; content of the availability statements in GB-44 |

## Optional checks

| Area | What it needs | Responsible | Run |
|---|---|---|---|
| DOI resolution | one retrieval per reference entry with DOI | `science-quellenapparat-pruefung` | no |
| Citation style | the name of the style | `science-zitierstil-harvard-ctr` or the style rules of the journal | no |
| AI statement against publisher policy | the policy of the target publisher | this review, on request | no |
| Relation to the authors' prior work | the prior work of the authors | this review, on request | no |
| Journal requirements | the author guidelines of the target journal | this review, on request | no |
| Factual accuracy | access to the sources of the checked statements and a selection of sections | `science-faktenbeleg-pruefung`, `geo-frage-belegbasiert-klaeren` | no |

## Limits of this review

- Checked version: egusphere-2025-4506.pdf, 29 pages, SHA-256 64cb3787456244aa6102e34f776b47e9a612d06e8894d391758ae240dbe415d6.
- Unreadable sources: full text of Fan et al. (2019) (abstract only); Wu et al. (2024) (closed access, title and record only); Ge et al. (2021) (closed access, no abstract retrievable); Navarre et al. (2009) (not identifiable from the manuscript); the 13 cited works without reference entry (GB-05) were not traced. Literature statements in GB-02 to GB-09 rest on the reading of instance S1; two of them (Zhao et al., 2021; Zhang et al., 2022) were re-read at their abstracts in the merge.
- Findings with status assumption: 9 of 45 (GB-15, GB-16, GB-20, GB-22, GB-23, GB-24, GB-28, GB-31, GB-43); in each the assumption concerns a partial statement and is put as a question; no finding rests on an assumption as its central statement.
- Optional checks run: 0 of 6.
- Omitted instances: none.
- Discarded findings: 0. All 68 instance findings had their mandatory fields; none was refuted on the manuscript. In the merge, 68 instance findings became 44 findings (four instance findings were split between two or more findings), one finding was added from the hints of the instances (GB-14, source ZF), 17 of 76 minor corrections were absorbed into findings and 15 merged with other minor corrections, 52 verification logs became 43, and one verification log (instance S3, collision wording) was overridden by GB-26. Overreaching subclauses were corrected in the merge (line numbers of the abstract in two findings of instance AB, the count of figures in GB-17, the count of entries without citation in GB-05 and GB-45, the citation status of Zhao et al. (2021) in GB-20 and GB-45).
