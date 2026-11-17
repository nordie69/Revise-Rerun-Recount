# Review report: Energy and structural evolution process of high-altitude and long-runout landslides induced by a strong earthquake

| Field | Value |
|---|---|
| Manuscript | Ge, Y., Hu, B., Tang, H., Fu, X., and Zhu, L. (2025): Energy and structural evolution process of high-altitude and long-runout landslides induced by a strong earthquake, EGUsphere preprint, https://doi.org/10.5194/egusphere-2025-4506 |
| Reviewed version | egusphere-2025-4506.pdf, 29 pages, 5544638 bytes, SHA-256 64cb3787456244aa6102e34f776b47e9a612d06e8894d391758ae240dbe415d6 |
| Date | 2026-10-18 |
| Language | English |
| Review instances | Segments 1 to 4, figures, study design; the six review instances ran as separate agents, each without the context of the others; merging, overall assessment and format check by a seventh agent |
| Line numbers | Printed margin numbers of the manuscript (every fifth line printed, intermediate lines counted on the page images); page numbers are PDF pages |

## Summary

The manuscript is a single-case numerical reconstruction of the Mogangling rock landslide on the Dadu River (Sichuan), which was triggered by the 1786 Kangding (Moxi) earthquake and dammed the river. The pre-failure surface is restored by straightening contour lines of a present-day UAV DEM; the landslide is then simulated in one dynamic run of 131 s with the discrete element code 3DEC (25345 blocks with 8.7 m by 8.7 m plan section, Mohr-Coulomb blocks and joints, the 2008 Wenchuan acceleration record of Luding station as substitute input). Kinetic, potential and dissipated energy (KE, PE, DE, with DE defined as the loss of mechanical energy, Eq. 4) are computed for the whole mass and for ten monitored blocks; "effective collisions" are detected as velocity peaks above a 30 % prominence threshold (1,139 detections); and the spreading of the mass is expressed by the alpha-shape indices volume swelling (VS) and area growth (AG) at 10 times. Key reported numbers are a field volume of about 2400×10⁴ m³ against a simulated volume of 317563 m³, maximum snapshot velocities of 5.9 to 31.6 m/s, a whole-mass energy budget of about 6500 GJ, and a "solid to fluidized" transition at VS 29.47 % and AG 319.5 % coinciding with a KE peak of 1116.8 GJ. The main conclusions are energy conservation for the whole mass and non-conservation for single blocks, more collisions and longer runout of the lower or front mass, and fragmentation as the cause of envelope growth.

## Strengths

1. The energy terms are defined explicitly as equations (Eq. 1 to 4) and plotted for the whole mass and for every monitored block, so that the energy bookkeeping can be followed and checked step by step; this transparency is what makes the definitional identity of the energy sum visible at all (PP-30, GB-45).
2. The method is laid out as an explicit chain (terrain restoration, simulation, collision detection, energy analysis, envelope indices) in Fig1 and Sect. 2, and the dispersion indices VS and AG are defined as formulas (Eq. 5 and 6), which gives a reader a reproducible frame for each step even where parameters are missing (PP-09, PP-08, GB-34).
3. The authors disclose the main limits of the reconstruction where the affected method is introduced: unknown pre-failure discontinuities, no instrumental record of 1786 and the use of a substitute record, the historical basis of the restoration and the smoothness of the restored terrain (PP-12, PP-03).
4. The snapshot velocities stated in Sect. 3.1 agree with the colour-bar maxima of Fig7, the snapshot times agree between Fig7, Fig11 and the text, and the timing of the KE peak in Fig8 agrees with the stage description, so the kinematic narrative is internally tied to the plotted output (PP-25, PP-23, PP-29).

## Weaknesses

1. The central energy results do not test the simulation: the constant sum KE + PE + DE follows from defining DE as a residual, the stated PE datum does not produce the plotted values, and the absolute energies cannot be reconciled with any stated mass, so neither "conservation" nor the energy magnitudes are established (GB-45, GB-46, GB-31). Suggestion: compute dissipation independently from contact and damping work, state the mass and datum used, and restate the conservation result as an observation on the decrease of mechanical energy.
2. The reconstruction is not tied quantitatively to the Mogangling event: the field dimensions and volume are internally inconsistent and differ from the simulated mass by a factor of about 76, the restored terrain is not checked against any known surface, and the validation is a visual match with the present, post-breach landscape (GB-16, GB-14, GB-41, GB-03). Suggestion: reconcile field and model volumes, check the restoration by a mass balance or on a case with a pre-event DEM, compare simulated and mapped deposit quantitatively, and restrict the stated aims to this reconstruction unless a sensitivity study is added.
3. The collision results rest on a detector that is not validated, on counts whose population and threshold are unclear, and on comparisons that are not normalised; the claims that the lower or front mass collides more often, receives energy from the rear and travels farther have no corresponding result (GB-26, GB-29, GB-47, GB-52). Suggestion: validate detected peaks against contact records, state blocks, threshold and binning behind 1,139 and Fig10b, and report collisions and travel distance per monitored block before stating position-dependent conclusions.
4. Further results and their reproducibility are weakened by several moderate issues: the solid to fluid transition is read at a sampled point whose KE differs from the Fig8 peak (GB-51), fragmentation is concluded without a fragmentation measure (GB-50), the movement stages place most of the descent before 15 s although the energy record does not (GB-40), model settings, input motion and data are not available (GB-21, GB-25, GB-53), and names, figure labels and literature support are inconsistent in many places (GB-32, GB-11, GB-02, GB-07, GB-08). Suggestion: define VS and AG on the envelope at t = 0 and at the times of Fig8, report a fragmentation measure or rephrase Conclusion 5, add a settings table and a data and code repository, harmonise names and labels, and position the work against the missing literature.

## Findings by segment

### Segment 1: Abstract, Introduction, state of research (p. 1 to 2)

#### Substantive findings

**GB-01 The trend statement on earthquake-induced chain disasters is supported by a source that does not address earthquakes or landslides.**

| Field | Content |
|---|---|
| Check | P13 |
| Location | p. 1, l. 33-34 |
| Quotation | "In recent years, the chain disasters of high-level rock landslides in high-intensity earthquake areas have shown a trend of frequent occurrence (Carpignano et al., 2009; Fan et al., 2019a)" |
| Concern | The introduction opens the case for the study with a frequency trend and gives two sources. Carpignano et al. (2009), J. Risk Res., 12, 513-534, develops a multi-risk mapping approach for a region in Italy that combines stakeholder perception with a conventional risk assessment framework for technological and natural risks; its abstract mentions neither earthquakes nor landslides nor a frequency trend, and refers only to an increased vulnerability of society, which is exposure, not event frequency. The source therefore does not carry the stated trend. The second source (Fan et al., 2019, Rev. Geophys.) is thematically pertinent but could not be read; the suffix "a" has no counterpart "b" in the reference list, so it is unclear which of the two Fan et al. (2019) entries is meant (see also GB-02). |
| Suggestion | In l. 33-34 replace Carpignano et al. (2009) by a source that documents a frequency trend of seismically triggered rock-landslide chains (for example an inventory or review), or reformulate the sentence without the trend claim; state which Fan et al. (2019) entry is meant. |
| Status | verified for Carpignano et al. (2009) (abstract and stated scope read by the review instance); inferred for Fan et al. (2019) (source not readable) |
| Severity | moderate |
| Source | S1 |

**GB-02 Citations and reference list do not match in either direction: 14 cited works have no entry, 16 entries are never cited, and 7 further citations differ from their entry.**

| Field | Content |
|---|---|
| Check | P4 |
| Location | p. 1-2, l. 33-64 (all citations of the manuscript stand in the Introduction); reference list p. 26-29, l. 508-605 |
| Quotation | "Fan et al., 2019a" (l. 34); "Wang, 2021" (l. 36); "Tian et al., 2017" (l. 37); "Fan et al., 2020" (l. 46); "Cheng 2014" (l. 48-49); "Zhao et al., 2020" |
| Concern | The manuscript has 29 distinct citation keys and 31 entries; 8 citations match their entry without discrepancy. (1) No entry, 14 citations: Fan et al. 2020 (l. 46); Huang et al. 2012 (l. 53); Intrieri et al. 2018 (l. 53-54); Huang et al. 2019 (l. 56); Zhu et al. 2010 (l. 58); Zhang et al. 2020a and 2020b (l. 58-59); Cuomo et al. 2021 (l. 59); Shugar et al. 2021 (l. 59); Navarre et al. 2009 (l. 62); Van Herwijnen and Schweizer 2011 (l. 62); Helmstetter and Garambois 2010 (l. 62-63); Cook et al. 2021 (l. 63); Pandey et al. 2021 (l. 63). (2) Year differs, 3: Tian et al. 2017 against entry 2016; Zhao et al. 2020 (l. 57) against entry 2021; Zhang et al. 2024 against the nearest entry Zhang, J. et al. 2023. Online-first versus issue year is a possible explanation: which year is intended? (3) Author form, 2: "Wang, 2021" for an entry with seven authors; "Cheng 2014" for the two-author entry "Cheng, F., and Yu-Sheng, L.". (4) Label, 2: "Fan et al., 2019a" (l. 34) and "Fan et al., 2019" (l. 56-57), while the list has two Fan et al. 2019 entries without a or b. (5) Entries never cited, 16: Bernardie et al. 2021; Chang et al. 2022; Chen et al. 2024; Dahal et al. 2022; Gao et al. 2023; Ge et al. 2021; Gong et al. 2024; He, J. et al. 2023; He, K. et al. 2022; He, N. et al. 2023; Nava et al. 2025; Sinčić et al. 2025; Wu, J. et al. 2013; Yang et al. 2022; Zhang, K. et al. 2019; Zhou et al. 2024. Check sums: 8 + 2 + 2 + 3 + 14 = 29 citations; 8 + 2 + 2 + 3 + 16 = 31 entries. Three uncited entries bear directly on the study: Wu et al. (2013) and Zhao et al. (2021) treat the Mogangling landslide itself, and Ge et al. (2021) treats mechanical energy evolution in rock avalanches, the approach of Sect. 2.3. Sections 2 to 4 contain no citation at all. |
| Suggestion | Add the 14 missing entries; cite or delete the 16 uncited entries; correct the seven short citations (for example "Wang et al., 2021", "Cheng and Yu-Sheng, 2014" or a corrected author name); label the two Fan et al. 2019 entries a and b and use the labels in l. 34 and l. 56-57; cite Wu et al. (2013), Zhao et al. (2021) and Ge et al. (2021) in Sect. 2.1 and 2.3. |
| Status | verified (text and reference list on the page images); online-first explanation of the year differences: assumption, asked as a question |
| Severity | moderate |
| Source | S4 |

**GB-03 The stated aims to "summarize the law" of earthquake-induced high-level rock landslides and to support early warning cannot be met by one deterministic run of one case without any sensitivity analysis.**

| Field | Content |
|---|---|
| Check | P10 |
| Location | p. 1-2, l. 38-41; p. 2, l. 71-73; p. 5, l. 122-125; p. 10, l. 183-191; p. 11, l. 206-207, l. 229-233; p. 14, l. 281-284 |
| Quotation | "so as to summarize the law of high-level rock landslide induced by earthquake" (l. 40-41); "The findings are intended to provide a theoretical foundation and scientific support for early warning and risk mitigation" |
| Concern | A general law or a basis for early warning requires several cases or a systematic variation of the controlling inputs. The design contains one landslide and one run; the inputs that the manuscript itself calls substitutes or choices (seismic record of another earthquake, l. 189-191; parameters partly from "empirical analogy, and parameter inversion", l. 207; threshold 30 % "deemed acceptable", l. 233; α = 1, l. 283) are not varied. Neither the gap stated in l. 63-64 nor any result addresses early warning. Which results are robust and which depend on these choices therefore cannot be judged. Graded major because it concerns the stated aims. |
| Suggestion | Either restrict the aims in l. 38-41 and l. 71-73 to the reconstruction of this case, or add a sensitivity study in Sect. 2 and 3: runs with at least two further input motions (other records or scaling), with the friction angles of the discontinuities varied within a plausible range, and with α and the prominence threshold varied, reporting runout, deposit extent, peak KE, final DE and collision counts for each run. |
| Status | verified |
| Severity | major |
| Source | SD |

**GB-04 The English contains literal translations and sentences without a clear main clause beyond the individual minor corrections.**

| Field | Content |
|---|---|
| Check | P16 |
| Location | p. 2, l. 39-41; p. 5, l. 108-112; p. 5, l. 113-119; p. 19, l. 388-389; p. 23, l. 429-431; see also KK-02 to KK-11, KK-22, KK-24, KK-25, KK-30 |
| Quotation | "so as to summarize the law of high-level rock landslide induced by earthquake" (l. 40); "The sudden flood made the downstream area a vast ocean" (l. 111); "This can be regarded as a successful energy extraction numerical simulation." |
| Concern | Beyond the single corrections listed, several sentences are hard to parse; the sentence in l. 114-119 has no clear main clause ("the stability investigation ... mostly focuses on ..., and the analysis of the instability probability ... are relatively few"). Recurrent literal translations ("cloud map", "repaired", "law of landslide") reduce precision. |
| Suggestion | Have the whole manuscript edited by a fluent speaker, with priority on Sect. 1, Sect. 2.1 and Sect. 3. |
| Status | verified |
| Severity | minor |
| Source | S4 |

**GB-05 The gap and novelty claims of the introduction rest on no described literature search, and published counterexamples exist, including the authors' own uncited energy study.**

| Field | Content |
|---|---|
| Check | P28 |
| Location | p. 2, l. 42; l. 49-51; l. 63-64; reference list p. 27, l. 540-542 |
| Quotation | "At present, in terms of surface terrain restoration, the terrain restoration before a landslide is less." (l. 42); "However, they still lack a quantitative and systematic study of this topic, especially on energy evolution during the collision." |
| Concern | Three sentences state that a topic has hardly been studied or that the method is new (l. 42, l. 49-51, l. 63-64). No databases, search terms, period or date of a search are named. Targeted searches found counterexamples for two of the claims: a contour-line reconstruction of pre-failure topography used for runout modelling (GB-07), and quantitative studies of energy transfer by collision and fragmentation between blocks (GB-08, GB-09). The authors' own earlier study, Ge et al. (2021), "Mechanical energy evolution in the propagation of rock avalanches using field survey and numerical simulation", is in the reference list (l. 540-542) but never cited, although its title addresses the topic declared missing in l. 63-64. |
| Suggestion | In l. 42-64 either describe the search (databases, search terms, period, date) or weaken the claims to what the cited literature shows; state explicitly what the present paper adds beyond Ge et al. (2021) and the works in GB-07 to GB-09. |
| Status | verified for the absent search description and the uncited Ge et al. (2021) entry; verified for the counterexamples (sources read, see GB-07 to GB-09); content of Ge et al. (2021) inferred from its title (not readable) |
| Severity | moderate |
| Source | S1 |

**GB-06 Three of the works cited for GIS-based landslide mapping and for terrain-restoration simulations do not treat these topics, and two cited works have no entry.**

| Field | Content |
|---|---|
| Check | P13 |
| Location | p. 2, l. 43-49; reference list p. 28, l. 559-561, l. 569-571, l. 585-587 |
| Quotation | "For most numerical simulations involving terrain restoration, a two-dimensional simulation is more often used. The simplified model is adopted to simulate the overall process of landslide by inputting external stress (Du et al., 2021; Cheng 2014; Li et al., 2024)." |
| Concern | The paragraph sets out the state of the art on which the method builds (l. 49-51). (a) Li et al. (2024), Front. Earth Sci., 12, 1466751, models an ancient landslide with limit-equilibrium and seepage software under rainfall fluctuation; the full text describes no restoration of pre-failure terrain and no seismic or other external stress input. (b) Song et al. (2017), "Landslide Deformation Prediction by Numerical Simulation in the Three Gorges", and Wu et al. (2024), "Numerical simulation on potential landslide-induced wave hazards by a novel hybrid method", are cited for GIS-based geomorphic mapping from photos, field surveys or UAV data, which their titles do not indicate. (c) Du et al. (2021) uses a discrete element simulation with an earthquake trigger and partly fits the second sentence; its abstract does not say whether the model is 2D or whether pre-failure terrain was restored. (d) Zhang et al. (2024) and Fan et al. (2020) have no entry (GB-02), so the first sentence rests on no verifiable source matching its content. The ranking "more often used" has no source. |
| Suggestion | In l. 45-49 cite for each sentence works that perform GIS mapping of recent landslides from imagery and that simulate landslides on restored pre-failure terrain; remove Li et al. (2024), Song et al. (2017) and Wu et al. (2024) from these sentences or move them to statements they support; support "more often used" with a count from a review or delete it. |
| Status | verified for Li et al. (2024) (full text) and Du et al. (2021) (abstract); inferred for Song et al. (2017) and Wu et al. (2024) (titles in the reference list, sources not read); Cheng (2014) not readable |
| Severity | moderate |
| Source | S1 |

**GB-07 A published contour-line reconstruction of pre-failure topography for runout modelling is missing from the positioning of the restoration method.**

| Field | Content |
|---|---|
| Check | P14 |
| Location | p. 2, l. 49-51; p. 1, l. 16-18; p. 25, l. 463-468 |
| Quotation | "This paper uses the method of restoring the continuity of contour lines to establish the terrain data before a landslide, which can provide a new idea of terrain restoration before a landslide for the same type of research." |
| Concern | The restoration of pre-landslide terrain from contour continuity is presented as a contribution in the Abstract, the Introduction and Conclusion 1. von Wartburg, J., Ivy-Ochs, S., Aaron, J., Martin, S., Leith, K., Rigo, M., Vockenhuber, C., Campedel, P., and Viganò, A.: Constraining the age and source area of the Molveno landslide deposits in the Brenta Group, Trentino Dolomites (Italy), Front. Earth Sci., 8, 164, https://doi.org/10.3389/feart.2020.00164, 2020, "manually modified the contour lines in the source area to provide a smooth transition with surrounding terrain" (p. 10), combined this with an assumed pre-failure river profile, and used the estimated pre-failure surface as "a key input for the runout modeling" with Dan3D-Flex (p. 10-11). This anticipates the procedure of l. 49-51 and offers a model for treating its uncertainty. The work is not in the reference list. Graded major because it restricts an explicitly claimed contribution. |
| Suggestion | In l. 49-51 and Conclusion 1 (l. 463-468) cite this work, state what differs in the present procedure, and discuss the uncertainty of the restored surface. |
| Status | verified (source full text read, p. 10-11; absence in the reference list checked) |
| Severity | major |
| Source | S1 |

**GB-08 A published discrete element study of energy transfer between front and rear sub-blocks by collision and by fragmentation is missing, although it bears on the gap claim and on Conclusion 4.**

| Field | Content |
|---|---|
| Check | P14 |
| Location | p. 2, l. 63-64; p. 26, l. 483-487; p. 1, l. 28-30 |
| Quotation | "When the rear rock mass collides with the front, its dissipated energy sharply increases and transfers energy to the front rock mass, enabling the front portion to slide farther." |
| Concern | Lin, Q., Wang, Y., Xie, Y., Cheng, Q., and Deng, K.: Multiscale effects caused by the fracturing and fragmentation of rock blocks during rock mass movement: implications for rock avalanche propagation, Nat. Hazards Earth Syst. Sci., 22, 639-657, https://doi.org/10.5194/nhess-22-639-2022, 2022, simulate with DEM how fragmentation accelerates the front sub-block while decelerating the rear sub-block, and state that "The energy transfer induced by fragmentation is more efficient than that induced by collision." This quantifies rear-to-front energy transfer between blocks, contradicting the claim in l. 63-64 that energy evolution during collision lacks quantitative study, and it names fragmentation as a competing transfer mechanism, while Conclusion 4 attributes the transfer to collision alone. The work is not in the reference list. Graded major because it bears on what the manuscript can claim as its result on energy transfer. |
| Suggestion | In the Introduction (l. 61-64), Sect. 3.2.2 and Conclusion 4 cite the work, compare the results, and state whether the 3DEC model can separate fragmentation-induced from collision-induced transfer. |
| Status | verified (abstract read on the journal page; absence in the reference list checked) |
| Severity | major |
| Source | S1 |

**GB-09 A discrete element study of energy conversion, collisions and fragmentation in a seismically triggered rock avalanche is missing.**

| Field | Content |
|---|---|
| Check | P14 |
| Location | p. 2, l. 63-64; p. 26, l. 488-492 |
| Quotation | "However, they still lack a quantitative and systematic study of this topic, especially on energy evolution during the collision." |
| Concern | Gao, G., Meguid, M. A., Chouinard, L. E., and Xu, C.: Insights into the transport and fragmentation characteristics of earthquake-induced rock avalanche: numerical study, Int. J. Geomech., 20, 04020157, https://doi.org/10.1061/(ASCE)GM.1943-5622.0001800, 2020, simulate the Tangjia Valley rock avalanche (2013 Lushan earthquake) with a calibrated 2D discrete element model, track energy conversion, collisions and solid fraction, and show that fragmentation continues with runout while solid concentration drops. This precedes the link between collisions, fragmentation and expansion of the deposit in Conclusion 5. The work is not in the reference list. |
| Suggestion | In l. 61-64 and in Sect. 3.4 cite the work and state how VS and AG relate to the solid fraction used there. |
| Status | verified (abstract read by the review instance; absence in the reference list checked) |
| Severity | moderate |
| Source | S1 |

#### Minor corrections

| ID | Location | Quotation | Replacement | Source |
|---|---|---|---|---|
| KK-01 | p. 1, l. 13 | "Chengdu, 610041 ,China" | "Chengdu, 610041, China" | S4 |
| KK-02 | p. 1, l. 15-16 | "ancient landslides that have occurred over a long time" | "ancient landslides that occurred long ago" | S1 |
| KK-03 | p. 1, l. 21; p. 3, l. 84 | "dissipation energy" | "dissipated energy" (as defined in l. 242 and used elsewhere) | S1, S2 |
| KK-04 | p. 1, l. 23; p. 3, l. 88-89; p. 14, l. 272, l. 281; p. 23, l. 426 | "Alpha shape algorithm"; "alpha shape"; "Alpha Shape algorithm"; "Alpha Shape envelope" | "alpha-shape algorithm", "alpha-shape envelope" in all places | S2 |
| KK-05 | p. 1, l. 27 and l. 28; p. 7, l. 153, l. 154 and l. 156 | "; For some blocks", "; Compared with", "; The elevation" | "; for some blocks", "; compared with", "; the elevation" | S4 |
| KK-06 | p. 1, l. 34-35 | "such as donghekou landslide debris flow dammed lake induced by the 2008 Wenchuan earthquake" | "such as the Donghekou landslide, debris flow and dammed lake induced by the 2008 Wenchuan earthquake" | S1, S4 |
| KK-07 | p. 1, l. 38 to p. 2, l. 39 | "the Mogangling landslide that occurred in 1786 was repaired and reconstructed" | "the pre-landslide topography of the Mogangling landslide, which occurred in 1786, was restored and the event was reconstructed" | S1, S4 |
| KK-08 | p. 2, l. 42 | "At present, in terms of surface terrain restoration, the terrain restoration before a landslide is less." | "At present, few studies have restored the surface terrain before a landslide." | S1, S4 |
| KK-09 | p. 2, l. 42-43 | "For landslides that have not occurred too far away" | "For recent landslides" | S4 |
| KK-10 | p. 2, l. 44 | "optical remote sensing images and UAV impact" | "optical remote sensing images and UAV imagery" | S1, S4 |
| KK-11 | p. 2, l. 46 | "Song at al.2017" | "Song et al., 2017" | S1, S4 |

#### Verification log

| ID | Check | Checked | Values | Result |
|---|---|---|---|---|
| PP-01 | P13 | Sentences that report numbers, rankings or assessments from other works, against the cited source where readable (l. 33-189) | l. 34-37: titles of Sun et al. (2011), Wang et al. (2014), Wang et al. (2021) name the Donghekou landslide of the 2008 Wenchuan earthquake, Hu et al. (2017) and Tian et al. (2016) the 2014 Ludian Ms 6.5 earthquake, consistent with the sentence; l. 52-63: 12 cited works without entry, fidelity not checkable (GB-02); l. 99-100 "nearly 20 large and super large earthquake landslides" without citation; Zhou et al. (2024) abstract: seismic amplification, back-slope effect and interface dynamic stress as failure factors for Mogangling. Disclosed limits: no instrumental record (l. 183-186), structural planes ignored (l. 175-178), dam break not modelled (l. 348-350) | no further finding beyond GB-01, GB-06, GB-16, GB-24 |
| PP-02 | P4 | Citations against reference list in both directions, short citation against entry (year, spelling, et al.) | Citations only on p. 1-2, l. 33-64; 29 citation keys, 31 entries; 8 matched without discrepancy (Carpignano 2009, Sun 2011, Wang 2014, Hu 2017, Song 2017, Wu 2024, Du 2021, Li 2024); label 2, author form 2, year 3, no entry 14, uncited 16; check sums 29 and 31 close; DOIs not resolved | see GB-02 |
| PP-03 | P10 and others | Design sketch from the whole manuscript: questions, type, data, timeline, settings, principles, components, disclosed limits | No explicit research question, 5 aims (l. 38-41, 49-51, 65-73); single case, one deterministic 3DEC run of 131 s, 25345 blocks, 10 monitored blocks, envelopes at 10 times; 7 data sources (UAV DEM, restored surface, tablet, Luding record, parameters, model output, field photographs); 7 declared principles or guarantees; 9 components, of which 0 tested independently; 7 disclosed limitations, 4 stated at the method and 3 only in the Results | findings in GB-03, GB-14, GB-21, GB-23, GB-26 |
| PP-04 | P10 | Mapping of stated gaps to aims | Gap l. 42 to restoration aim l. 49-51; gap l. 63-64 to energy aims l. 67-69; aims without gap: early warning (l. 71-73), general law (l. 40-41) | 2 gaps, 5 aims, 2 aims without gap; see GB-03 |
| PP-05 | P28 | Sentences of the form "less", "rarely", "new idea", "still lack" in Abstract and Introduction | 3 gap or novelty sentences (l. 42, l. 49-51, l. 63-64); 1 rarity statement without novelty claim (l. 60-61, direct observation data rarely available, plausible for sudden events); search description: none; own searches 2 | see GB-05 |
| PP-06 | P14 | Contribution in one sentence and search for missing closely related work, with mandatory check against the reference list | 5 searches; candidates absent from the list and proposed: von Wartburg et al. (2020), Lin et al. (2022), Gao et al. (2020); dropped because already listed: Ge et al. (2021), Zhao et al. (2021), Zhou et al. (2024), Wu et al. (2013), Chang et al. (2022), Gao et al. (2023); dropped as only the same field: 3 further studies | see GB-07, GB-08, GB-09 |
| PP-07 | P18 | Principles the manuscript declares or recommends | The Introduction criticises the lack of "a quantitative and systematic study" (l. 63-64); no declared principle on data openness; 1 principle checked | no separate finding; the qualitative validation is raised in GB-41 |

### Segment 2: Methods, model, collision detection, energy and envelope definitions (p. 2 to 15)

#### Substantive findings

**GB-10 The location symbols in Fig2 (a) and (b) do not sit at the coordinates given in the text.**

| Field | Content |
|---|---|
| Check | P3 |
| Location | p. 5, l. 95-96; Fig2 (a) and (b), p. 6 |
| Quotation | "The coordinates of the landslide center are: 29 ° 37 ′ 30.726 ″ north latitude, 102 ° 09 ′ 41.190 ″ east longitude." |
| Concern | Fig2 (a) is graticuled and Fig2 (b) has graticule lines and a scale bar, so both positions can be measured. (a) Calibrated on the graticule ticks (600 dpi), the centre of the "Mogangling landslide" dot lies at 101.17°E and 29.55°N (each ±0.01°), whereas the text gives 102.161°E, 29.625°N; the longitude differs by 0.99°, about 96 km at 29.6°N (0.99 × 111.32 km × cos 29.6°). (b) The red star "Study area" sits on the intersection of the graticule lines labelled 102°09'E and 29°37'N (offsets 0.2 and 0.7 px). The text coordinates lie 30.726" north (948 m) and 41.190" east (1105 m) of that intersection, about 1.46 km away. Either the graticule labels in (b) are truncated values of lines that run through the stated centre, or the star or the coordinates are wrong. |
| Suggestion | Place the dot in Fig2 (a) at 102°09'41"E, 29°37'31"N; in Fig2 (b) label the graticule lines with their true values or move the star to the stated centre, and check the coordinates in l. 95-96 against the map. |
| Status | verified (positions measured on the page image); distances inferred |
| Severity | moderate |
| Source | AB |

**GB-11 The lithological units carry different names and symbols in the text, Fig2 (c), Fig3, Fig4 and Table 1, and it is not stated which Table 1 parameter set belongs to which model material.**

| Field | Content |
|---|---|
| Check | P38, P3 |
| Location | p. 5, l. 101-105; p. 6, Fig2 (c) legend; p. 8, Fig3 (a) and (b) legends; p. 10, Fig4 legend; p. 11, l. 207-209; p. 11, Table 1, column "Rock mass" |
| Quotation | "Quartz diorite (O2) and a small amount of basic magmatic rocks are distributed on the western slope of Mogangling. The sand slate of the Triassic Baiguowan formation (T3bg) is exposed on the left bank of the Dadu River." (l. 102-104); "The slope is underlain by plagioclase granite, which is subdivided into strongly weathered and moderately weathered zones." |
| Concern | Same objects, different names (page images checked): Q4del is "landslide accumulation" (text) and "Rubble soil" (Fig2 c); Q4col+dl is "colluvial Deluvial deposit" (text) and "Massive gravel" (Fig2 c, Fig3 b); Q4al is "alluvial deposit" (text) and "Sand and pebble gravel" (Fig2 c, Fig3); γo2 is "Jinning plagioclase granite" (text), "Plagiogranite" (Fig2 c) and "Granite" (Fig3). Neither the quartz diorite (symbol "(O2)" without rock prefix) nor T3bg appears in the legend of Fig2 (c); the left bank is mapped as γM2 "Hybrid granite", which the text does not mention, while Fig3 (a) and (b) show "Diorite" as the main unit below the sliding mass. The weathering grades differ between l. 101 ("strongly to weakly") and l. 208 ("strongly weathered and moderately weathered"). The model in Fig4 has four materials (γo2, Qdel, γM2, sliding mass), Table 1 has two parameter sets ("bed rock", "landslide mass"), and l. 208-209 suggests a third split by weathering; the assignment of parameter sets to model materials is not stated and cannot be rebuilt. |
| Suggestion | Add in Sect. 2.1 one table or legend that lists each unit with symbol, one name, the figures it appears in and the Table 1 parameter set used for it in the model; harmonise the legends of Fig2 (c), Fig3 (a), Fig3 (b) and Fig4 with the text names in l. 101-107; complete the symbol of the quartz diorite in l. 102. |
| Status | differing names and symbols verified (page images p. 5, 6, 8, 10, 11); identity of Q4del with "Massive gravelly soils" in Fig3 inferred; mapping of Table 1 rows to model materials verified as absent |
| Severity | moderate |
| Source | S2, AB |

**GB-12 The scale bar in Fig2 (a) does not agree with the graticule of the same map.**

| Field | Content |
|---|---|
| Check | P3 |
| Location | Fig2 (a), p. 6, scale bar |
| Quotation | "0  40      160km" |
| Concern | The bar has four segments of about equal length (68, 75, 69 and 75 px at 600 dpi); "40" sits at the first division, so the whole bar of 294 px represents 160 km, 1.84 px per km. The graticule gives 31°N to 29°N over 311 px, 1.40 px per km north to south, and 155.4 px per degree of longitude, 1.61 px per km east to west at 29.6°N. The bar is 31 % too long for the north to south scale and 14 % too long for the east to west scale, far above the reading uncertainty of about ±0.7 %. |
| Suggestion | Recompute the scale bar of Fig2 (a) for its projection, or remove it and rely on the graticule. |
| Status | verified (measured on the page image) |
| Severity | minor |
| Source | AB |

**GB-13 The legend of Fig2 (c) leaves several map symbols unexplained.**

| Field | Content |
|---|---|
| Check | P29 |
| Location | Fig2 (c), p. 6 |
| Quotation | "(c) engineering geological map." |
| Concern | The map shows contour lines labelled 1125 to 1825 without stated interval or unit, the red section line a-a', orange dip symbols "60°" and "80°", and blue flow arrows in the river; none of them is in the legend. |
| Suggestion | Add contour interval and unit, the section line, the dip symbol and the flow direction to the legend of Fig2 (c). |
| Status | verified |
| Severity | minor |
| Source | AB |

**GB-14 The contour restoration is offered as a new method and is the input to every later result, but it is neither tested against any known surface nor described consistently, and Conclusion 1 recommends steps that the study does not perform.**

| Field | Content |
|---|---|
| Check | P10, P15 |
| Location | p. 6-7, l. 133-143; p. 7, l. 157-162; p. 2, l. 49-51; Fig1 (p. 4, upper panel); Fig3 (b), (c) (p. 8-9); p. 25, l. 463-468 (Conclusion 1) |
| Quotation | "the contour lines corresponding to the sliding bed and accumulation area are modified to be straight" (l. 139-140); "The contour line is modified along the extension direction of the mountains on the left and right sides" (l. 157); "their trajectory equations can be extracted as a basis for restoring the contours" (l. 465-466); "In such cases, restoration can be guided by referencing other mountain areas within the same stratigraphic unit." |
| Concern | The only assessment of the restored surface is visual ("can be regarded as the terrain before the landslide", l. 161-162). The rule for modifying contours is given twice in different form ("straight", l. 140; "along the extension direction", l. 157). The "trajectory equations" of Conclusion 1 (a) are not extracted or reported in Sect. 2.1, and the guidance from other mountain areas of the same stratigraphic unit in Conclusion 1 (b) is not done in this study. Fig1 shows "Deposit Removal", but the text generates "the existing model as the sliding bed" (l. 135-136) and does not say whether and how the 1786 deposit was removed. The restored surface determines the volume of the simulated mass (GB-16), so every later result depends on this unvalidated step. The first sentence of Conclusion 1 is supported by Sect. 2.1 and Fig3 as a visual result. Graded major because a methodological contribution is claimed in Introduction and Conclusion 1 and the step feeds all results. |
| Suggestion | In Sect. 2.1 state one rule for contour modification with its parameters, describe the deposit removal shown in Fig1, and report the volume between restored and present surfaces in the source area and in the deposit area against the field volume of l. 151 (mass balance with a stated bulking factor). To support the method claim, apply the procedure to a landslide with a known pre-event DEM and report elevation and volume errors. Otherwise move Conclusion 1 (a) and (b) to an outlook marked as proposals and remove the method claim in l. 49-51. |
| Status | verified |
| Severity | major |
| Source | SD, S4 |

**GB-15 Fig3 (a) shows two zones where the text says it shows four.**

| Field | Content |
|---|---|
| Check | P3 |
| Location | p. 7, l. 144-146; Fig3 (a), p. 8 |
| Quotation | "The whole landslide occurrence area can be divided into four parts: the rock wall area, colluvial slope area, slope debris flow area, and main accumulation area." |
| Concern | Fig3 (a) delimits two zones, "I Sliding bed" and "II Accumulation area", separated by a dotted line; the four parts named in the text are not marked. The 3D view also carries a planar scale bar "0 400 1000m", which is not valid in an oblique perspective. |
| Suggestion | Mark the four parts in Fig3 (a) or change the text to the two zones shown; remove the scale bar from the perspective view or replace it by labelled distances. |
| Status | verified |
| Severity | minor |
| Source | AB |

**GB-16 The dimensions and the volume of the landslide do not fit together: area times thickness does not give the stated volume, the stated length contradicts three figures and the model, the source in the reference list gives other values, and the simulated volume is 1.3 % of the field volume.**

| Field | Content |
|---|---|
| Check | P1, P2, P3, P13, P9 |
| Location | p. 7, l. 149-156; p. 5, l. 110-112; p. 9, l. 173-175 and l. 181-182; Fig2 (c) (p. 6); Fig3 (b) (p. 8); Fig4 (p. 10); Table 2 (p. 13, column "Volume"); reference list p. 29, l. 600-602 |
| Quotation | "about 450 m long, about 1000 m wide along the river, and a planar area of 0.45 km2. The average thickness of the landslide mass is about 100 m, and the volume is about 2400×104 m3." (l. 149-151); "The length of the landslide mass in the sliding direction is 1021 m" (l. 173-174); "the volume of the landslide is 317563 m3." |
| Concern | The geometry of the event is the basis of the model and of the validation in Fig7 (o). (1) Length times width matches the area (450 m × 1000 m = 0.45 km²), but area times average thickness gives 0.45 × 10⁶ m² × 100 m = 4500×10⁴ m³, 1.875 times the stated 2400×10⁴ m³; conversely 2400×10⁴ m³ requires an average thickness of 53.3 m. (2) The length of 450 m contradicts Fig2 (c) (1167 m ± 10 m from the boundary to the river bank along a-a', measured with the map scale bar), Fig3 (b) (about 1080 m) and the model (1021 m, l. 173-174); the elevation profile of l. 151-156 (1120 to 1890 m with slopes of 50°, 5 to 12°, 35° and 57°) also implies a horizontal length of about 914 to 1250 m. (3) Zhao et al. (2021), Nat. Hazards, 106, 459-485, which is in the reference list but never cited, gives for the same landslide 450 m by 1000 m, a volume of about 4500×10⁴ m³ and "over 100 000 deaths" when the dam broke; the manuscript gives 2400×10⁴ m³ and "tens of thousands" (l. 111-112) without citation. (4) The simulated volume of 317563 m³ (l. 182) is 1.32 % of 2400×10⁴ m³ (factor 75.6); spread over 0.45 km² it would be 0.71 m thick. The ten monitored blocks in Table 2 have a mean volume of 1151.3 m³; 25345 blocks of that size would give 29.2 × 10⁶ m³, close to the field value, not to 317563 m³. Every energy value in Fig8, Fig9 and Fig12 scales with the simulated mass (GB-46), so these differences decide whether the energy results describe the Mogangling event. Graded major for this reason. |
| Suggestion | In Sect. 2.1 (l. 149-151) state which of length, area, thickness and volume is measured and which is derived, cite the source of each value and of the casualty figure, and correct the inconsistent values or explain the difference to Zhao et al. (2021); in l. 173-182 give the simulated volume, mass, number of blocks of the landslide mass and plan dimensions next to the field values and explain any difference. |
| Status | manuscript values verified (page images p. 5, 7, 9; Fig2 c and Fig3 b measured); values in Zhao et al. (2021) verified (abstract); products, ratios and implied lengths inferred (Python) |
| Severity | major |
| Source | S1, S3, AB, SD |

**GB-17 The text refers to a section b-b' in Fig2 (c) and to its result in Fig3 (c); Fig2 (c) and Fig3 (b) show only section a-a', and Fig3 (c) shows no section.**

| Field | Content |
|---|---|
| Check | P4, P3 |
| Location | p. 7, l. 159-160; Fig2 (c) (p. 6); Fig3 (b) and (c) (p. 8-9) |
| Quotation | "As shown in Fig3. (b), make a section along a-a'and b-b' in Fig2. (c). The results are shown in Fig3. (c)." |
| Concern | Fig2 (c) carries one red section line from a to a' (measured length 1559 m); Fig3 (b) is headed "(a-a')"; Fig3 (c) shows contour maps and shaded terrain before and after modification in plan view. The restored profile ("Presumed original slope") is in Fig3 (b), not in Fig3 (c). Section b-b' exists nowhere. |
| Suggestion | Add section b-b' to Fig2 (c) and its profile to Fig3 (b), or delete "and b-b'"; in l. 160 refer to Fig3 (b) for the restored profile and to Fig3 (c) for the plan view. |
| Status | verified |
| Severity | minor |
| Source | S4, AB |

**GB-18 In Fig3 two legend fields cannot be told apart, and the same unit has different colours in (a) and (b).**

| Field | Content |
|---|---|
| Check | P3 |
| Location | Fig3 (a) and (b) legends, p. 8 |
| Quotation | "(a) 3D views of the study area; (b) Engineering geological profile" |
| Concern | Measured on the legend fields (300 dpi), "Diorite" is #8c7c74 and "Sand and pebble gravel" #8c745c; the summed RGB difference is 0 + 8 + 24 = 32, below the threshold of 40 at which two colours count as equal. Granite is brown in (a) and pink with crosses in (b), and "Massive gravelly soils" is tan in (a) and green in (b), so the two panels cannot be read with each other. |
| Suggestion | Use one colour per unit across Fig2 (c), Fig3 (a) and Fig3 (b), and make Diorite and Sand and pebble gravel clearly different. |
| Status | verified |
| Severity | minor |
| Source | AB |

**GB-19 The axes of Fig3 (b) have no quantity or unit, and the distance axis has no ticks and uneven labels.**

| Field | Content |
|---|---|
| Check | P29 |
| Location | Fig3 (b), p. 8 |
| Quotation | "(b) Engineering geological profile" |
| Concern | The vertical rulers (1000 to 2000) and the horizontal axis (0 to 1500) carry no quantity or unit. The horizontal axis has no tick marks; the label spacings are 319.5, 321.5, 317.5, 345.5 and 336.0 px for equal steps of 300, so the horizontal scale is uncertain by up to 8 % and the vertical exaggeration cannot be stated exactly. The "80°" symbol is not explained. |
| Suggestion | Label the axes "Elevation (m a.s.l.)" and "Distance along a-a' (m)", add ticks at the labelled positions, and explain the 80° symbol. |
| Status | verified |
| Severity | minor |
| Source | AB |

**GB-20 The water level in Fig3 (b) lies about 30 m above the river level implied by the text.**

| Field | Content |
|---|---|
| Check | P3 |
| Location | Fig3 (b), p. 8; p. 7, l. 151-152 |
| Quotation | "The elevation of the slope toe is 1120 m (about 5 m higher than the river surface)" |
| Concern | Calibrated on the vertical ruler of Fig3 (b) (2000 at 116.5 px, 1000 at 1200.5 px, 600 dpi), the top of the light blue river fill is at 1146.7 m ± 2 m. The text puts the river surface at about 1115 m. The difference of about 32 m exceeds the reading uncertainty by an order of magnitude; Fig2 (c) also has a contour labelled 1125 on the slope just east of the river. |
| Suggestion | Check the river level in the profile against the DEM and correct either Fig3 (b) or l. 151-152; state the elevation reference (for example m a.s.l.). |
| Status | verified (profile measured); comparison with the Fig2 (c) contour inferred |
| Severity | moderate |
| Source | AB |

**GB-21 Settings that determine the energy terms and the trigger are not reported: damping, time step and output interval, code version, and the characteristics of the input motion, which Fig4 shows without a readable time axis.**

| Field | Content |
|---|---|
| Check | P35, P29 |
| Location | p. 9, l. 168-170; p. 6, l. 130-136; p. 10, l. 189-202; Fig4 inset and legend (p. 10); p. 11, l. 203-213; p. 14, l. 272, l. 281-284 |
| Quotation | "the three-dimensional discrete element program (3DEC)" (l. 169); "this study adopts the acceleration records measured at the Luding station during the Wenchuan earthquake as the input ground motion" |
| Concern | DE is the residual of all non-conservative work (Eq. 4), so its time course depends on contact friction and numerical damping; damping type and value are not stated anywhere. The input motion is described only by station and event: component or components applied, peak acceleration, duration, scaling to the 1786 event, filtering and conversion to stress at the viscous base are missing, although the Results attribute stages to P- and S-waves (l. 308-310). The inset of Fig4 has a time axis with ticks but no numbers, quantity or unit, and its markers tp, tPGA, tf and te are not explained; the Fig4 legend uses γo2, Qdel and γM2 without resolving them. Missing as well: 3DEC version, time step, output interval of the histories (which governs the detectable velocity peaks), UAV sensor, survey date, DEM resolution, and the software for point-cloud processing, alpha shape and peak detection. Whether damping or output interval change the results is an assumption from general knowledge of DEM codes: could the authors state how the damping setting enters the DE curves of Fig8 and Fig9? |
| Suggestion | Add to Sect. 2.1 a table of model settings (code version, damping type and value, time step, contact model, history output interval) and of the input motion (components, PGA, duration, scaling, filtering, application at the base); give the inset of Fig4 a time axis in s and explain its markers in the caption; add sensor, date and resolution of the UAV DEM to l. 130-136, and name the software used in Sect. 2.2 and 2.4. |
| Status | missing settings and unreadable inset verified; influence of damping and output interval: assumption, asked as a question |
| Severity | moderate |
| Source | SD, AB |

**GB-22 The model ignores the real structural planes, yet the Results explain the failure by structural-plane control, and "structural plane" names both the ignored discontinuities and the modelled ones without a link to the two Table 1 types.**

| Field | Content |
|---|---|
| Check | P6, P38 |
| Location | p. 9, l. 175-180; p. 11, l. 208-210; p. 11, Table 1, rows "discontinuities" and "potential discontinuities"; p. 15, l. 308-313 and l. 323-324; p. 25, l. 469 |
| Quotation | "the impact of the structural plane on the landslide process has to be ignored in this study" (l. 176-178); "A uniform structural plane is set inside." (l. 179-180); "The first-arriving P-waves caused intense vertical dislocation along the steeply dipping structural planes outside the slope." (l. 308-309); "Under the combined influence of structural plane control and strong seismic forces, the landslide mass was ejected" |
| Concern | The authors disclose where the model is introduced that the pre-failure discontinuity pattern is unknown and ignored, and replace it by an 8.7 m grid with a "uniform structural plane" and potential rupture surfaces (l. 178-180, l. 208-210). The consequence is not carried into Sect. 3.1: the steeply dipping planes that control failure in the model are the artificial grid planes, so the mechanism in l. 308-313 and l. 323-324 is a property of the discretisation, not evidence about the Mogangling rock mass; Conclusion 2 repeats the capability claim without restriction (l. 469). The naming adds to this: Table 1 lists "discontinuities" and "potential discontinuities", the text "fully developed potential rupture planes and joint sets" (l. 209-210); which is which, and which of them the "uniform structural plane" is, is not stated. With 15° against 10° friction and 960 against 100 GPa/m normal stiffness, the assignment changes the model. |
| Suggestion | In Sect. 2.1 (l. 175-180, l. 208-213) name each modelled discontinuity type once and use these names as row labels in Table 1; in Sect. 3.1 (l. 306-324) state that the structural planes acting in the model are those of Sect. 2.1 and restrict the mechanism statements accordingly; add the restriction to Conclusion 2. A second run with a different block size or grid orientation would show whether the grid controls the failure. |
| Status | disclosure, statements and names verified; that the acting planes are the grid planes inferred; mapping between text and table rows: assumption, asked as a question |
| Severity | moderate |
| Source | S2, SD |

**GB-23 Several processing steps cannot be rebuilt: the subdivision of the block columns, the target of the parameter inversion, the base of the 30 % prominence threshold, and the point set and unit of the alpha shape.**

| Field | Content |
|---|---|
| Check | P8, P20 |
| Location | p. 9, l. 178-180; p. 11, l. 206-207; p. 11, l. 226-233; Fig5 (p. 12) and caption l. 238-239; p. 14, l. 272-273 and l. 281-284 |
| Quotation | "The landslide mass is evenly divided into 8.7 m×8.7 m blocks on the xoy surface. The height is determined by the vertical height from the surface of the landslide mass to the sliding bed." (l. 178-179); "a suitable prominence threshold must be chosen-one that quantifies each peak’s standout height, width, and position relative to adjacent peaks" (l. 227-229); "At a threshold of 30%, however, the identification of effective collisions is deemed acceptable." |
| Concern | (1) Block heights computed from the Table 2 volumes and the 75.69 m² plan area are 10.0 to 23.2 m, while the mean thickness is about 100 m (l. 150-151), so the columns are subdivided; spacing and orientation of the internal planes are not given. (2) Which parameters were inverted and against which observation is not stated (l. 206-207). (3) The prominence threshold is a percentage without a reference quantity (of the peak velocity, of the local or global maximum, of the velocity range); l. 227-229 names height, width and position, three different quantities. The choice between 10 % and 50 % changes the detections visibly (Fig5 b to f), so the base determines the collision count of 1,139; the choice itself is a visual judgement without criterion. The visual comparison of five thresholds in Fig5 is helpful but does not define the rule. (4) The point set fed to the alpha shape (block vertices, centroids, surface points) and the unit of α are not given. |
| Suggestion | In Sect. 2.1 give the spacing and orientation of the internal planes and, for each Table 1 parameter, its source (test, analogy, inversion) and the observation used for the inversion; in Sect. 2.2 give the peak criterion as a formula with its reference quantity and minimum peak distance, name the software function, state a criterion for the threshold and report the collision counts for 10 % to 50 %; in Sect. 2.4 name the point set and the unit of α. |
| Status | verified |
| Severity | moderate |
| Source | SD, S3 |

**GB-24 The justification of the seismic input rests on an uncited "extensive research" statement, and the fault assignment of the landslide differs between two places.**

| Field | Content |
|---|---|
| Check | P13 |
| Location | p. 10, l. 186-189; p. 5, l. 97-99 and l. 110 |
| Quotation | "It is worth noting that both the Mogangling landslide and the Wenchuan earthquake zone belong to the tectonic system of the Longmenshan Fault Zone. Extensive research indicates that the Kangding earthquake is comparable to the 2008 Wenchuan earthquake in terms of damage distribution, affected intensity, and estimated magnitude." |
| Concern | The manuscript discloses openly that no instrumental record of the 1786 event exists (l. 183-186). The substitute record is then justified by a comparison attributed to "extensive research" without a single citation, so it cannot be checked. The manuscript's own references give M 7.75 for the 1786 event (Zhao et al., 2021, title; "Ms7 ¾" in l. 110) and M8.0 for Wenchuan (Wang et al., 2014 and 2021, titles), and no damage or intensity comparison. In addition, l. 97-99 places the middle reaches of the Dadu River at the intersection of the Xianshuihe, Longmenshan and Anninghe faults, while l. 186-187 assigns the landslide to the Longmenshan system. Could the authors state which studies make the comparison and on which fault they place the 1786 event? |
| Suggestion | In l. 187-189 cite the studies that compare the two events and give the compared values (magnitude, intensity, damage extent); reconcile the fault assignment with l. 97-99. |
| Status | missing citation and internal values verified; correctness of the comparison itself: assumption, asked as a question |
| Severity | moderate |
| Source | S1 |

**GB-25 Third-party data used in the Methods are neither identified nor covered by the availability statement: the input record, the remote sensing image, the geological map and the temple tablet.**

| Field | Content |
|---|---|
| Check | P12 |
| Location | p. 10, l. 189-191; p. 6, Fig2 (b) and (c), caption l. 126-127; p. 9, l. 180; p. 6, l. 136-138; p. 26, l. 505-506 |
| Quotation | "According to the geological engineering drawing, different strata are generated" (l. 180-181); "only the Tiezhuang Temple tablet unearthed in the 1980s has records of earthquake landslide, river dam break, and water discharge" |
| Concern | The authors explain why recorded motion from 2008 is used instead of 1786 data, a disclosed limitation not raised here. Missing is the provenance of the record itself: no network, data provider, station code, component, processing or citation is given (see also GB-21). The same applies to the remote sensing image in Fig2 (b) (provider, acquisition date), the engineering geological map in Fig2 (c) and the "geological engineering drawing" of l. 180 (author, scale, year), and the Tiezhuang Temple tablet (no edition or report cited). The blanket statement in l. 505-506 names the first author as access route; for third-party records the right to redistribute normally lies with the provider. Are the authors entitled to redistribute the Luding record and the map? The seismic input is the only loading of the model, so the dynamic analysis cannot be repeated without it. |
| Suggestion | In Sect. 2.1 (l. 189-191) name provider, station, component and processing of the input record and cite it; in the caption of Fig2 give source and date of the image and the source of the map; at l. 136-138 cite a publication of the tablet text; in "Availability of data and material" list these third-party sources separately with their access route. |
| Status | missing provenance verified (text, captions, statement, page images of Fig2 and Fig4); redistribution rights: assumption, asked as a question |
| Severity | moderate |
| Source | S2 |

**GB-26 Effective collisions are identified only as velocity peaks; that a detected peak is a collision is never checked.**

| Field | Content |
|---|---|
| Check | P31 |
| Location | p. 11, l. 215-234; Fig5 (a) (p. 12); p. 25, l. 473-475; p. 26, l. 483-485 |
| Quotation | "Effective collisions of rock blocks are identified by their characteristic velocity changes." (l. 220); "effective block collisions during the landslide can be identified by extracting local peaks from displacement-velocity curves" |
| Concern | A local velocity maximum shows that a block stopped accelerating, not that it was struck; acceleration can also come from gravity on a steepening path or from the seismic input during shaking, whose duration is not stated (GB-21). The detector identifies a peak of one block, not the colliding partner or the direction of transfer. Conclusion 2 states that the detector identifies collisions, but no comparison of detected peaks with contact events is reported, so the rates of false and missed detections are unknown; the threshold comparison in Fig5 (b) to (f) judges only which peaks look important. Graded major because Conclusions 2 and 4 and the Abstract rest on the detector. |
| Suggestion | In Sect. 2.2 validate the detector on a sample: for detected peaks and for curve segments without peaks, check in the DEM contact records whether a new contact or a contact-force pulse with another block occurred, and report precision and recall per threshold; restrict Conclusion 2 (l. 473-475) to the validated performance. |
| Status | verified (no validation reported) |
| Severity | major |
| Source | SD |

**GB-27 The abscissa of the curve used to detect effective collisions is named "travel distance", "travel displacement", "displacement" and "distance" without saying whether path length or net displacement is meant.**

| Field | Content |
|---|---|
| Check | P38, P16 |
| Location | p. 11, l. 220-234; p. 1, l. 22-23; Fig1 (p. 4); Fig5 (a) to (f) x axes (p. 12); Fig10 (b) x axis (p. 23); p. 1, l. 30; p. 22, l. 418; p. 25, l. 474 |
| Quotation | "Fig5. (a) presents a typical velocity-travel-distance curve for an individual block." (l. 220-221); "1,139 effective collisions were detected from the travel-distance versus velocity profile" (l. 233-234); "the effective collision of blocks in the process of landslide is obtained by extracting the local peak value of the displacement velocity curve" |
| Concern | The detection rule of Sect. 2.2 is the core of the collision analysis, and its x variable carries four names. On the page images, Fig5 (a) is labelled "Travel distance (m)" and Fig5 (b) to (f) "Travel Displacement (m)"; Fig10 (b) uses "Travel distance (m)"; the Abstract (l. 22-23) and Conclusion 2 (l. 474) use "displacement"; l. 30 and l. 418 add "migration distance". Path length and net displacement differ as soon as a path bends or reverses, which the manuscript reports for Blocks 1 and 3 that bounce to the opposite bank (l. 397-399, l. 416). Peak positions and their spacing depend on the variable, and so does the prominence-based detection. |
| Suggestion | Define the abscissa once in Sect. 2.2 (for example cumulative path length of the block centroid) and use that name in l. 22-23, l. 30, Fig1, the axis titles of Fig5 (a) to (f) and Fig10 (b), l. 418 and l. 474 ("the velocity versus travel-distance curve"). |
| Status | names verified (text and page images p. 4, 12, 23); that the variables differ for bouncing blocks inferred from l. 397-399 and l. 416 |
| Severity | moderate |
| Source | S2, S4 |

**GB-28 In Fig5 (a) two of the six red "effective collision" markers are not at local peaks, the highest peak is unmarked, and the curve falls below zero.**

| Field | Content |
|---|---|
| Check | P3 |
| Location | Fig5 (a), p. 12; p. 11, l. 220-225 |
| Quotation | "A local velocity peak (denoted by red or purple markers) corresponds to an acceleration phase, but only those pronounced peaks (highlighted in red) yield a substantial velocity increase" |
| Concern | Calibrated at 600 dpi (58.19 px per m/s), the red markers lie at 47.6, 190.4, 243.3, 307.9, 448.1 and 463.3 m. The marker at 243.3 m (13.05 m/s) is followed by an unmarked point at 261.3 m with 13.41 m/s, the highest point of the curve; the marker at 463.3 m (4.21 m/s) lies on a rising branch after the minimum near 462 m and is followed by 4.84 and 5.23 m/s. Both differences (0.36 and 0.63 m/s) exceed the uncertainty of ±0.02 m/s many times. The curve also reaches about minus 0.3 m/s near 588 m, and the axis runs to minus 2 m/s, which is impossible for a speed; the caption does not say whether a velocity component is plotted. The black markers are not in the legend. |
| Suggestion | Recheck the marker placement in Fig5 (a) (a one-sample offset is a possible explanation and could be stated), state which velocity is plotted, and add the black markers to the legend. |
| Status | verified (measured on the page image) |
| Severity | moderate |
| Source | AB |

**GB-29 The origin of the 1,139 effective collisions and of Fig10 (b) is unclear: one profile, ten blocks or all blocks, the bins of Fig10 (b) sum to more than 1,139, and their distribution does not match the 30 % detections of Fig5 (d).**

| Field | Content |
|---|---|
| Check | P20, P3, P5 |
| Location | p. 11, l. 233-234; Fig5 (a) to (f) (p. 12); p. 22, l. 414-415 and l. 418-419; Fig10 (b) (p. 23) |
| Quotation | "Under this setting, 1,139 effective collisions were detected from the travel-distance versus velocity profile." (l. 233-234); "Fig10. (b) presents the frequency of effective collisions experienced by blocks at different locations during the landslide process." |
| Concern | Three analysis units are possible and none is stated: one block (Fig5 a is "a typical velocity-travel-distance curve for an individual block", l. 221; Fig5 b to f show one profile to about 2400 m), the ten monitored blocks, or all blocks. Fig5 (d), the 30 % panel, carries about 100 red markers, 30 of them in the inset, so about 70 on the profile, an order of magnitude below 1,139. Fig10 (b) has 26 points from 0 to 2500 m in steps of 100 m; measured on the page image, they sum to about 1,213 to 1,220, that is 74 to 81 more than 1,139 (6.5 % to 7.1 %). The four bins from 2200 to 2500 m hold 142, 157, 150 and 146, about half of the total, while Fig5 (d) has almost no red markers beyond 2000 m (2 resolvable clusters of 64), against 39 clusters in the 10 % panel (Fig5 b). If Fig10 (b) comes from the curve of Fig5, it reflects a lower threshold than 30 %, the overcounting the manuscript itself warns against (l. 230-231); if it pools other blocks, "the profile" of l. 234 is not the source and the pooling is not described. The peak "once the blocks enter the river channel" (l. 419) may therefore be a detection artefact. Graded major because the collision-frequency result rests on it. |
| Suggestion | In Sect. 2.2 and in the caption of Fig10 state the blocks, threshold, time window and binning from which the count of 1,139 and Fig10 (b) are derived; reconcile the two totals; show Fig10 (b) for the 30 % threshold actually chosen and, if the peak beyond 2150 m disappears, revise l. 418-421 and Conclusion 4. |
| Status | quotations verified; marker counts and bin values verified by measurement on the page images; sums and shares inferred; identity of the data sets: assumption, asked as a question |
| Severity | major |
| Source | S3, AB, SD |

**GB-30 The block velocity in Fig5 (b) to (f) peaks at about 45 m/s for an unnamed block, far above the maximum velocity of 31.6 m/s that the text calls the peak.**

| Field | Content |
|---|---|
| Check | P3, P2 |
| Location | Fig5 (b) to (f), p. 12; p. 16, l. 330 and l. 337; Fig7 (e) colour scale (p. 17); Fig9 (p. 21-22) |
| Quotation | "As shown in Fig7. (e) and (l), during the impact-at-base stage, the maximum velocity reached 31.6 m/s." (l. 330); "The velocity reached its peak upon arrival at the valley floor." |
| Concern | The colour-scale maxima of Fig7 match the text (5.9, 19.6, 27.1, 31.6, 25.7 m/s). The velocity-distance profile in Fig5 (d), calibrated on its ticks, peaks at 45.2 m/s ± 0.3 m/s at about 253 m of travel. Neither caption nor text says which block this is, or whether it is the block of Fig5 (a), which reaches 13.5 m/s and travels about 590 m. The energies in Fig9 give peak velocities of 3.9 to 17.5 m/s for the ten monitored blocks (KE maximum 0.030 to 0.297 GJ, m = ρV with 2300 kg/m³). Either the profile belongs to a block that peaked between the snapshots of Fig7, in which case 31.6 m/s is a snapshot maximum and l. 337 needs qualification, or Fig5 (b) to (f) come from another run or quantity. Which applies? |
| Suggestion | Name the block and run of Fig5 (b) to (f) in the caption, with its position (Table 2 or Fig6); in Sect. 3.1 give the overall maximum block velocity and its time in addition to the snapshot maxima. |
| Status | peak and colour-scale values verified by measurement; comparison with Fig9 inferred (density assumed from Table 1); explanation: assumption, asked as a question |
| Severity | moderate |
| Source | S3, AB |

**GB-31 The potential-energy datum stated in Sect. 2.3 does not produce the plotted values; the plotted block energies imply a separate datum for each block.**

| Field | Content |
|---|---|
| Check | P2, P5 |
| Location | p. 13, l. 252-255; Table 2 (p. 13); Fig8 (p. 20); Fig9 (a) to (j) (p. 21-22); p. 20, l. 397-399 |
| Quotation | "the potential-energy calculation uses the model’s initial height as the reference datum rather than true sea level; only the change in potential energy due to relative displacement is considered" |
| Concern | With each block's initial height as datum, PE would start at 0 and become negative; Fig8 and Fig9 instead start at their maximum PE and fall towards zero. A common fixed datum is excluded as well: block 1 (bottom, z = 340, 939.9 m³) starts at about 5.05 GJ and block 10 (top, z = 755, 967.8 m³) at about 0.95 GJ, a ratio of 0.188, whereas a common datum at z = 0 would give 2.29 for block 10 against block 1. With m = 2300 kg/m³ × V the initial PE corresponds to heights above datum of 236 to 238 m (block 1), 29.8 m (block 7) and 43.5 m (block 10), i.e. datum elevations of about z = 104 m for block 1 and z = 711 m for block 10. PE reaches zero at each block's lowest point, and blocks 1 and 3 rise again (l. 397-399). The values thus fit a datum at the lowest elevation each block reaches, which is not what l. 253-255 states. The datum changes the PE and KE split and the totals of Fig8 (GB-46). |
| Suggestion | In Sect. 2.3 (l. 252-255) state the datum actually used (common model datum, final or lowest elevation per block) and give h(t0) and the final elevation of the ten blocks in Table 2. |
| Status | quotation and figure shapes verified; initial PE of the blocks measured on the page images (about ±0.1 GJ); implied datum elevations inferred |
| Severity | moderate |
| Source | S3, SD |

**GB-32 The four position zones of the monitoring points carry different names in the text, Table 2, Fig6, Abstract and Conclusions, and Fig6 swaps the labels "Lower middle part" and "Upper middle part".**

| Field | Content |
|---|---|
| Check | P38, P4, P3 |
| Location | p. 13, l. 256-257; p. 13, Table 2, columns "Position" and "Coordinate"; p. 14, Fig6 zone labels; p. 1, l. 28-30; p. 26, l. 483-487 |
| Quotation | "As shown in Fig6., ten monitoring points were installed in the lower, lower-middle, upper-middle, and upper portions of the slide mass" (l. 256-257); "Compared with the upper rock mass, the lower rock mass is compressed more frequently" |
| Concern | Table 2 groups IDs 1 and 2 as "bottom" (z = 340 and 355), 3 to 5 as "lower middle part" (z = 465 to 498), 6 to 8 as "upper middle part" (z = 660 to 692) and 9 and 10 as "top" (z = 752 and 755). In Fig6 the labels read, from upslope, "Top", "Lower middle part", "Upper middle part", "Bottom" (confirmed on the page image); the point counts per band (2, 3, 3, 2) agree with Table 2, so only the two middle labels are swapped. The text uses "lower" and "upper" for the outer zones, the Abstract compares "upper" and "lower rock mass" (l. 28-30), Conclusion 4 "front" and "rear portion" (l. 484-485); whether front equals lower and rear equals upper is not stated. Because the zone attribution carries the comparison in the Abstract, a reader cannot tell which blocks it refers to. |
| Suggestion | Swap the two middle labels in Fig6; use one set of zone names in l. 256-257, Table 2, Fig6, Abstract l. 28-30 and Conclusion 4; state in l. 256 whether "front" and "rear" in Sect. 4 refer to these zones. |
| Status | names and label order verified (page images p. 13, 14); swap inferred from the z coordinates of Table 2; equivalence of front and lower: assumption, asked as a question |
| Severity | moderate |
| Source | S2, S4, AB |

**GB-33 Fig6 does not identify the monitoring points and uses a coordinate frame different from Table 2.**

| Field | Content |
|---|---|
| Check | P29 |
| Location | Fig6, p. 14; Table 2, p. 13; Fig10 (a), p. 23 |
| Quotation | "Fig6. Location of 10 monitoring points" |
| Concern | The ten points carry no IDs and their colours are not explained, so the panels of Fig9 (point 1 to 10) cannot be linked to a location. The colours do not follow the legend of Fig10 (a) (there 1 is red and 3 magenta, which in Fig6 are both in the top band, whereas Table 2 puts 1 at the bottom and 3 in the lower middle part). The axes of Fig6 have no titles or units and run from 0 to 2400, 0 to 3200 and 0 to 800, while Table 2 gives coordinates such as (-79, -284, 340) and (-719, 120, 755), with negative x and y that do not exist on these axes. |
| Suggestion | Label each point in Fig6 with its ID, use the colours of Fig10 (a), add axis titles with units, and state the origin of the Table 2 coordinates relative to Fig4 and Fig6. |
| Status | verified |
| Severity | moderate |
| Source | AB |

**GB-34 VS and AG cannot be reproduced: the enclosed object has six names, V0 and S0 are not tied to the envelope at t = 0 and are not reported, α = 1 is said to ensure a tight fit without any test, and Sect. 3.4 switches to "the monitored block group".**

| Field | Content |
|---|---|
| Check | P38, P20, P31 |
| Location | p. 14, l. 269-284; p. 4, Fig1 (fourth row); p. 1, l. 24; p. 23, l. 427 and l. 429; p. 24, l. 440-442, l. 449, l. 451-452 and Fig11 caption l. 437-439; p. 25, l. 453-454 and Fig12 caption l. 458; p. 26, l. 488; p. 7, l. 151; p. 9, l. 182 |
| Quotation | "In these expressions, V0 denotes the initial volume of the landslide mass (m³); Vt denotes the volume of the enclosing envelope at time t (m³)" (l. 278-279); "this study uniformly sets the α value to 1. This approach ensures a tight fit of the envelope model while minimizing geometric deviations introduced by parameter tuning." (l. 282-284); "the sharp rise of DE shown in the figure further confirms significant fragmentation and disintegration in the monitored block group" |
| Concern | Eq. (5) and (6) define the indices cleanly as relative changes. The enclosed object, however, is called "accumulation area" (l. 269), "deposition zone" (l. 270-272), "slide mass" (l. 272), "deposit mass" (l. 427), "landslide body" (l. 24) and "landslide mass" (l. 278); Fig11 (a) shows the envelope at t = 0 s around the intact source mass, when no deposit exists. V0 is the "initial volume of the landslide mass" and Vt an envelope volume; the manuscript gives two volumes for the landslide (2400×10⁴ m³, l. 151; 317563 m³, l. 182; GB-16), and a third candidate is the envelope at t = 0 s. If V0 is a mass volume and Vt an envelope volume, VS mixes two definitions and is not zero at t = 0; any offset enters every value, including 29.47 % (Vt/V0 = 1.2947) and 319.5 % (St/S0 = 4.195). Neither V0 nor S0 is reported. The manuscript itself states that α "directly affects the accuracy of the envelope fitting as well as the computed volume and surface area" (l. 281-282), but no other α is tried. In l. 451-452 the unit changes from the whole sliding mass (Fig12 caption, l. 441-442) to "the monitored block group", without saying whether the ten blocks of Table 2 or all blocks are meant. |
| Suggestion | In Sect. 2.4 name the enclosed object once and use that name in the heading, l. 24, l. 427-429, l. 449, l. 488 and Fig1; define V0 and S0 as envelope volume and area at t = 0 s and give their values next to the mass volume; show VS and AG for at least two further α values and state which conclusions hold for all; in l. 451-452 replace "monitored block group" by the unit plotted in Fig12. |
| Status | names, wording and absent values verified (text and page images p. 4, 14, 23, 24); ratios inferred (Python); that V0 differs from the envelope at t = 0 s inferred |
| Severity | moderate |
| Source | S2, S3, SD |

**GB-35 The two dispersion indices carry several names, some of which misname them as rates, and the surface-area symbol changes from S to A.**

| Field | Content |
|---|---|
| Check | P38, P16 |
| Location | p. 14, l. 274-275, Eq. (5) and (6); p. 1, l. 25; p. 3, l. 89; p. 14-15, l. 287-288; p. 24, l. 440-441 and l. 444; p. 25, l. 453-454; p. 25, Fig12 axis titles and caption l. 458-459; p. 26, l. 488 |
| Quotation | "two dimensionless indices are introduced: volume swelling (VS) and area growth (AG)" (l. 274-275); "we first extracted its volume (V) and surface area (A) at each time point, based on which the volume expansion rate (VS) and surface area growth rate (AG) were calculated" (l. 440-441); "Fig12. Overall energy variation of the sliding mass: (a) as a function of volume; (b) as a function of area." |
| Concern | Fig1 and the axis titles of Fig12 ("Volume Swelling (%)", "Area Growth (%)", confirmed on the page image) use the defined names. Elsewhere VS is "volume expansion (rate)" (l. 25, 89, 441, 453, 488) and AG "area growth rate" or "surface area growth" (l. 25, 89, 441, 453). "Rate" suggests change per unit time, while Eq. (5) and (6) define a ratio to the initial value; l. 444 then speaks of "the rate of increase in VS". The envelope area is St and S0 in Eq. (6) but "A" in l. 440. The caption of Fig12 names the abscissae "volume" and "area", while the plotted quantities are the percentages VS and AG (axes up to about 1,250 % and 4,300 %). |
| Suggestion | Use "volume swelling (VS)" and "area growth (AG)" throughout, including l. 25, l. 89, l. 441, l. 453-454 and l. 488; in l. 440 write "its volume (Vt) and surface area (St)"; change the Fig12 caption to "(a) as a function of volume swelling VS; (b) as a function of area growth AG". |
| Status | verified (text and page images p. 4, 14, 24, 25) |
| Severity | minor |
| Source | S2, S4 |

#### Minor corrections

| ID | Location | Quotation | Replacement | Source |
|---|---|---|---|---|
| KK-12 | p. 2, l. 74 (heading) | "2 Methodologies" | "2 Methodology" | S4 |
| KK-13 | p. 2, l. 76 to p. 3, l. 77 | "the research method involves three parts: (1)" | "the research method involves four parts: (1)" (the text lists (1) to (4), Fig1 shows four rows) | S4, AB |
| KK-14 | figure call-outs and captions throughout, for example p. 2, l. 76; p. 7, l. 160; p. 15, l. 301; p. 23, l. 428 | "As shown in Fig1., the research method"; "in Fig2. (c)"; "Fig7 illustrates"; "(Fig11.)." | "As shown in Fig. 1, the research method"; "in Fig. 2c"; "Fig. 7 illustrates"; "(Fig. 11)." (one form throughout) | S2, S4 |
| KK-15 | p. 5, l. 98 | "Y" - shaped faults (hyphen with a space on both sides, as set on the page) | "Y-shaped faults" | S4 |
| KK-16 | p. 5, l. 104 | "The quaternary system" | "The Quaternary system" | S4 |
| KK-17 | p. 5, l. 105 (twice) | "colluvial Deluvial deposit" | "colluvial-deluvial deposit" | S4 |
| KK-18 | p. 6, Fig2 (b) legend | "Daduhe River" | "Dadu River" (as in the text and in Fig2 c) | S2, AB |
| KK-19 | p. 7, l. 151 | "the volume is about 2400×104 m3" (the exponent 4 is set on the baseline, confirmed on the page image) | "the volume is about 2400 × 10⁴ m³", subject to GB-16 | S3, S4 |
| KK-20 | p. 7, l. 152 | "1120 m-1330m" | "1120 to 1330 m" | S4 |
| KK-21 | p. 9, l. 182 | "1121m high" | "1121 m high" | S4 |
| KK-22 | p. 10, l. 193-195 | "In the course of a discrete-element simulation-particularly when modeling nominally semi-infinite bodies such as the use of fixed or elastic boundaries in a static analysis will inevitably reflect outbound seismic waves into the model during a subsequent dynamic analysis." | "In a discrete-element simulation, particularly of nominally semi-infinite bodies, fixed or elastic boundaries used in a static analysis will reflect outgoing seismic waves back into the model during a subsequent dynamic analysis." | S4 |
| KK-23 | p. 11, l. 213; p. 13, l. 267 (table titles) | "Table 1 Physical parameters of rock mass and discontinuities"; "Table 2: The basic information of blocks where the 10 monitoring points are located" | one form for both, for example "Table 1. Physical parameters of rock mass and discontinuities." and "Table 2. Blocks containing the 10 monitoring points." | S2, S4 |
| KK-24 | p. 11, l. 218 | "block velocities-hereafter termed" | "block velocities, hereafter termed" | S4 |
| KK-25 | p. 11, l. 228 | "must be chosen-one that quantifies" | "must be chosen, one that quantifies" | S4 |
| KK-26 | p. 12, Fig5 (a) legend | "Non-obvios acceleration" | "Non-obvious acceleration" | S4, AB, SD |
| KK-27 | p. 13, l. 246 | "where, at time ti, PE(ti), and DE(ti) can be expressed as:" | "where, at time ti, KE(ti), PE(ti) and DE(ti) can be expressed as:" | S4, SD |
| KK-28 | p. 13, l. 251 | "(m/s);h(ti)" | "(m/s); h(ti)" | S4 |
| KK-29 | p. 13, Table 2, last row | "11" (ID) with "Maximum unbalanced force" | move the row below the table as a note: "In addition, the maximum unbalanced force of the whole model was recorded." (the title names 10 monitoring points) | S3 |

#### Verification log

| ID | Check | Checked | Values | Result |
|---|---|---|---|---|
| PP-08 | P4 | Every reference in the text to a figure, panel, table, equation and section against its target on the page image; numbering | Fig4 labels 1021 m, 747 m, 179 m, 131 m match l. 174-175; Fig5 (b) to (f) thresholds 10 to 50 % in caption order; Fig7 panel pairs (a, h) to (g, n) as in the text; figures 1 to 12, tables 1 and 2, equations (1) to (6) contiguous; section 3.3 skipped; equations not referred to by number; no appendix or supplement | findings in KK-13, GB-17, GB-32, KK-35 |
| PP-09 | P29, P3 | List of figures: type, caption, references in the text | 12 figures, numbered 1 to 12 without gap, each referenced in its own section (Fig1 l. 76; Fig2 l. 93, 160; Fig3 l. 144, 159, 160; Fig4 l. 173; Fig5 l. 220, 229; Fig6 l. 256; Fig7 l. 301 to 353, 387; Fig8 l. 375; Fig9 l. 393; Fig10 l. 414, 418; Fig11 l. 428; Fig12 l. 443); no graphical abstract; all captions are one-line titles without reading guidance | figure findings GB-10 to GB-13, GB-15, GB-17 to GB-20, GB-28, GB-33, GB-42, GB-43, GB-48, GB-49 |
| PP-10 | P38 | Names of study object, software, events, stations and energy terms, counted in the running text (p. 1 to 26 without the reference list) | "Mogangling" 24, no variant; "3DEC" 2, introduced at l. 169; "Kangding earthquake" 3 (l. 110, 183, 188); "Moxi M 7.75" only in the title of a cited entry, a name used by another study, not counted as inconsistency; "Luding station" 1; "Dadu River" 13 in the text; KE 8, PE 8, DE 7, ME 6, all defined in l. 241-243; "effective collision(s)" 17, defined at l. 218-219 | no further finding beyond KK-03 and KK-18 |
| PP-11 | P3 | Scale bars of Fig2 and Fig3 | Fig2 (b): segments 67, 75 and 69 px for 0, 200, 600 m, consistent; Fig2 (c): segments 178, 184, 177 px, consistent; Fig3 (c): 177, 181.5 and 265.5 px for 400, 400 and 600 m, consistent; section a-a' in Fig2 (c) 1559 m against about 1570 m horizontal extent of Fig3 (b), consistent | no finding except Fig2 (a), see GB-12 |
| PP-12 | P17 | Place of each limitation the manuscript discloses | Structural planes ignored (l. 175-177), substitute input (l. 183-191), historical basis of the restoration (l. 136-138), smooth restored terrain (l. 160-162): stated at the method; dam break not modelled (l. 348-350), weathering (l. 353-355), apparent DE decrease (l. 399-402): only in the Results; 7 limitations, 4 at the method, 3 only in the Results | consequences raised in GB-22 and GB-41; no separate finding |
| PP-13 | P27 | Unchecked components and where their output flows | Restored surface to mass geometry and all energies; substitute input to trigger and stages; unspecified parameter inversion to all results; unvalidated collision detector to Fig10 (b), Conclusion 4 and Abstract; α = 1 to VS, AG and the transition values; 5 components, 5 downstream uses | raised in GB-14, GB-16, GB-21, GB-23, GB-26, GB-29, GB-34, GB-52; no separate finding |
| PP-14 | P1 | Numbers in Sect. 2 that follow from other numbers | 450 m × 1000 m = 0.45 km², consistent; elevation bands (l. 151-156): 1120 to 1330 m (210 m), 1330 to 1380 m (50 m), 1380 to 1890 m (510 m) = 220 m + 290 m, consistent; river about 1115 m; block footprint 8.7 × 8.7 = 75.69 m²; Table 2 volumes 756.2 to 1754.3 m³ (sum 11,512.7 m³), column heights 10.0 to 23.2 m; VS 29.47 % gives Vt/V0 = 1.2947, AG 319.5 % gives St/S0 = 4.195 | area times thickness against volume inconsistent, see GB-16 |
| PP-15 | P7 | Whether the described method applied to all reported data | 1 simulation run; 0 reported version, protocol or instrument changes; UAV survey date and 3DEC version missing (GB-21) | no separate finding |
| PP-16 | P3 | Fig4 dimension labels against the text | Labels "1021m", "747m", "179m", "131m"; text l. 173-175: 1021 m, about 747 m, 179 m, about 131 m; perspective axes not measured | no finding |
| PP-17 | P26 | Guarantees and their scope | "ensures a tight fit" (l. 283-284, all envelopes); "ensures that the simulation outcomes align with actual conditions" (l. 471-472); "Dynamic loading must be introduced only after ... static equilibrium" (l. 199-201); 3 guarantees, 1 mode and path (one run) | raised in GB-34, GB-41, GB-44; no separate finding |
| PP-18 | P3 | Red markers per threshold panel in Fig5 and the inset box of Fig5 (d) | Whole panel / inset: (b) 139 / 36, (c) 122 / 30, (d) 100 / 30, (e) 87 / 26, (f) 63 / 3, falling with the threshold as stated in l. 229-233; shaded box in (d) x 1552 to 1830 m, y 14.9 to 26.0 m/s, matching the inset axes within the border width | no finding; counts used in GB-29 |
| PP-19 | P38 | Names of the ten monitored objects | "monitoring point" 6 occurrences; "point 1" to "point 10" in the Fig9 caption (l. 410-413); "Block 1", "Block 3", "Blocks 1 and 3" (l. 397, 416); Table 2 title relates blocks and points; Fig10 (a) legend 1 to 10 | point n and Block n denote the block of monitoring point n; no finding (zones see GB-32) |
| PP-20 | P34 | Counted sets with shown subsets | 10 monitoring blocks: complete list in Table 2 with selection rule (four height zones, l. 256-257); 10 envelope times: complete list in the Fig11 caption, selection rule not stated; 1,139 collisions: only aggregated in Fig10 (b); 3 sets, 1 complete with rule, 1 complete without rule, 1 only aggregated | raised in GB-23 and GB-29; no separate finding |
| PP-21 | P3 | Point counts in Fig6 against Table 2 | Points per band from upslope 2, 3, 3, 2 = 10; Table 2: top 2, upper middle 3, lower middle 3, bottom 2 | counts agree; label order see GB-32 |

### Segment 3: Results (p. 15 to 25)

#### Substantive findings

**GB-36 Outputs announced in the Methods are not reported, among them the unbalanced-force history, so neither the post-failure stability nor the stated duration of 131 s is shown.**

| Field | Content |
|---|---|
| Check | P11, P31 |
| Location | p. 15, l. 299-301; p. 3, l. 86-87; p. 13, l. 257-263 and Table 2 (column "Monitoring contents", ID 11); Fig7 (g) (p. 18); Fig9 (a), (c), (e), (i) (p. 21-22); Sect. 3 (p. 15-25) |
| Quotation | "By tracking the cumulative runtime, it was found that the landslide lasted for a total of 131 seconds from initiation to completion." (l. 300-301); "In addition, the maximum unbalanced force was tracked to verify that the model reached post-failure stability." (l. 258-259); "For the local analysis, displacement, velocity, and stress histories were extracted for each of the ten monitored blocks in all relevant directions" |
| Concern | Searched in Sect. 3 and Fig7 to Fig12 against the outputs announced in Sect. 2: reported are the velocity and stress fields of the whole mass (Fig7), the whole-mass energy (Fig8), the energy of all ten blocks (Fig9) and their trails (Fig10 a, without distances). Not reported: the displacement or runout of the whole mass as a number (the reproduction is judged only qualitatively, GB-41), the displacement and stress histories of the ten blocks listed in Table 2, the maximum unbalanced force (ID 11), and the link between collision frequency of different parts and energy transfer announced in l. 86-87 (GB-52). No reason is given. Without the unbalanced-force history, threshold or final value, the purpose stated in l. 258-259 is not shown to be achieved. At 131 s Fig7 (g) still shows velocities up to 0.21 m/s; in Fig9 (e) and (i) the PE of blocks 5 and 9 reaches zero only at about 120 s, and in Fig9 (a) and (c) the PE of blocks 1 and 3 rises until about 120 to 125 s. 131 s is the last snapshot of every figure and may be the end of the computation rather than a measured stop. |
| Suggestion | Add to Sect. 3.1 the unbalanced-force history with the stability criterion and the time at which it was met, and derive the duration in l. 300-301 from it (for example the time at which the mean block velocity falls below a stated value); add final runout and deposit extent compared with the field, and either the per-block displacement and stress histories or a statement that they were not used; remove from Table 2 what is not used. |
| Status | absence of the outputs and of a stability criterion verified; panel values read on the page images; that 131 s equals the run end inferred |
| Severity | moderate |
| Source | S3, SD |

**GB-37 The times of the movement stages and of the solid to fluid transition are given only through figure captions, so the reader must combine Fig7, Fig8, Fig11 and Fig12 to place them.**

| Field | Content |
|---|---|
| Check | P22 |
| Location | p. 15-16, l. 304-347; p. 19, Fig7 caption l. 368-369; p. 24-25, l. 452-455; Fig8 (p. 20) |
| Quotation | "As shown in Fig7. (e) and (l), during the impact-at-base stage, the maximum velocity reached 31.6 m/s." |
| Concern | The stage descriptions in Sect. 3.1 name stages but not times; the times (0, 3, 7, 9, 12, 15, 131 s) are only in the caption of Fig7, so the reader must map panel (b) to 3 s, (c) to 7 s and so on. The transition in l. 452-455 has no time at all; the reader must locate the KE maximum of Fig12 (1116.8 GJ) in Fig8, where KE of that size occurs at about 11 s, while the Fig8 maximum is at about 13 s (GB-51). |
| Suggestion | Add the time to each stage sentence in Sect. 3.1 (for example "at t = 12 s, during the impact-at-base stage") and the time of the transition in l. 452-455. |
| Status | verified |
| Severity | minor |
| Source | S3 |

**GB-38 Seismic amplification at higher elevations and a back-slope effect are stated as having raised the peak ground acceleration, but no acceleration was monitored.**

| Field | Content |
|---|---|
| Check | P31 |
| Location | p. 15, l. 310-313 and l. 316-318; Table 2 (p. 13, column "Monitoring contents") |
| Quotation | "The back-slope effect and amplification at higher elevations during seismic wave propagation significantly increased the peak ground acceleration of the Mogangling slope, triggering the initial movement of the sliding mass." |
| Concern | Table 2 lists displacement, velocity and stress components and the unbalanced force; acceleration is not recorded at any point, and no comparison of motion at the base and at the crest is shown. The amplification and its role as trigger are asserted, not measured. The same mechanisms are named by Zhou et al. (2024), which is in the reference list but not cited here (GB-02). |
| Suggestion | Add acceleration histories at base, mid-slope and crest (or the ratio of peak accelerations) to Sect. 3.1, or rephrase l. 310-313 and l. 316-318 as interpretation from the literature with citations. |
| Status | verified |
| Severity | moderate |
| Source | SD |

**GB-39 Statements in Sect. 3.1 mix model output, field observation and inference beyond the model without saying which is which, and the field investigation said to enter the reconstruction is not reported.**

| Field | Content |
|---|---|
| Check | P19 |
| Location | p. 16, l. 326-335; p. 16, l. 350-352; p. 13, l. 264-266; p. 2, l. 65 |
| Quotation | "ongoing impacts ultimately led to the formation of a loosely consolidated fractured layer approximately 20 meters thick near the interface between the landslide deposit and the underlying bedrock" (l. 327-329); "However, based on the simulation results, it can be inferred that the landslide-induced damming caused a rapid rise in the water level behind the dam, resulting in backflow flooding in the surrounding counties and cities." |
| Concern | The 20 m fractured layer, the fine debris and the layered pseudo-bedrock (l. 334-335) are described as stages of the simulation, but the model as described (blocks of 10 to 23 m height, no breakage mechanism in Sect. 2.1, GB-50) does not output such layers; if they are field observations or literature, the source is not given, and no field data are presented apart from photographs, although l. 65 and l. 265-266 name the field investigation as a data source. The backflow flooding of "surrounding counties and cities" (l. 350-352) is inferred from a simulation that, as the authors state in l. 348-350, stops before the dam break and contains no water; it is historical or hydraulic reasoning, not model output. The reader cannot tell which parts of the reconstructed sequence are model output and which are observation or inference. |
| Suggestion | In Sect. 3.1 mark each statement as model output (with the figure that shows it), as observation (with method, location and date, or citation) or as inference; move l. 350-352 to a discussion with a source for the flooding; add a short subsection to Sect. 2 describing the field investigation and its findings. |
| Status | absence of sources and field data verified; that the layers are not model output inferred; the backflow statement verified as outside the modelled processes (l. 348-352) |
| Severity | moderate |
| Source | SD, ZF |

**GB-40 The stage description places the impact of the entire mass and the river blocking within the first 15 s, but the energy record shows that about 65 % of the initial potential energy is still unreleased at 15 s.**

| Field | Content |
|---|---|
| Check | P36 |
| Location | p. 16, l. 330-331; p. 16, l. 338-348; p. 19, l. 381-386; Fig7 (snapshots 0 to 15 s and 131 s); Fig8 (p. 20) |
| Quotation | "After a brief airborne trajectory, the entire landslide mass collided with the ground." (l. 330-331); "Subsequently, the upper portion of the landslide continued to move downward until coming to a complete stop." |
| Concern | Digitised from Fig8, PE falls from about 6,503 GJ to 4,443 GJ at 12 s and 4,213 GJ at 15 s, so 31.7 % and 35.2 % of the initial PE are released by these times; 65.0 % is released by 30 s and 95.3 % by 60 s. KE after its peak near 13 s stays between about 450 and 700 GJ until about 35 s. The larger part of the descent therefore happens between 15 and 60 s, a period for which Fig7 has no snapshot and the text gives one sentence (l. 385-386). The statements that the entire mass collided at 12 s and that the river was blocked "instantly" (l. 348) are not matched by the model's own energy record. Graded major because the reconstruction of the movement process is a stated aim. |
| Suggestion | In Sect. 3.1 add snapshots between 15 s and 131 s (for example 20, 30, 45, 60 s; the times of Fig11 serve in part), describe the phase in which most of the PE is released, give for each stage the fraction of initial PE released from the data behind Fig8, and revise l. 330-331 and l. 346-348. |
| Status | inferred (fractions from digitised Fig8 values, about 19 GJ per pixel) |
| Severity | major |
| Source | SD |

**GB-41 The validation is a visual match of two features with today's landscape, which was altered by the 1786 dam breach and centuries of weathering; it cannot "ensure" agreement with the event, and Fig7 (o) lacks time step, scale and photo source.**

| Field | Content |
|---|---|
| Check | P31, P15, P29 |
| Location | p. 16, l. 348-359; Fig7 (o) (p. 19); p. 5, l. 110-111; p. 25, l. 471-473 (Conclusion 2) |
| Quotation | "Fig7. (o) presents compelling evidence of agreement between the numerical simulation results and the actual field observations." (l. 353-354); "Furthermore, the extent and morphology of the accumulated landslide material in the simulation closely match those observed in reality." (l. 357-359); "Comparison with field imagery and result analysis ensures that the simulation outcomes align with actual conditions." |
| Concern | Fig7 (o) compares a rendered model view with two photographs by two rectangles (the protruding ridge in the source area, the deposit area); no quantity is compared (runout, deposit extent or area, thickness, dam height). The simulated view has no time step, scale or orientation; the photographs have no date, source, viewpoint or scale. The manuscript notes weathering (l. 354-355) and that the dam burst after 9 days (l. 110-111) while the breach is not modelled (l. 348-350); the present deposit is therefore the remnant after breach erosion, which the simulated pre-breach deposit should not "closely match". The consequence of these disclosed limits for the comparison is not drawn. The Results close with "support the validity" (l. 359); Conclusion 2 strengthens this to "ensures" (l. 471-472). Graded major because the validity of all simulation results rests on this comparison. |
| Suggestion | In Sect. 3.1 replace the visual comparison by quantities from the DEM and the historical record: outline overlap of simulated and mapped deposit (for example an area-based fit index), runout of the front, deposit thickness along a-a', and simulated dam height against the 9-day filling time of the river; state which parts of the present deposit are expected to differ because of the breach; give time step, scale and north arrow for the simulated view and date, source and viewing direction for the photographs; replace "ensures" by "supports" in l. 471. |
| Status | verified |
| Severity | major |
| Source | S4, SD, AB |

**GB-42 The colour scales and axes of Fig7 cannot be read across panels, and the stress quantity is not named.**

| Field | Content |
|---|---|
| Check | P29 |
| Location | Fig7 (a) to (n), p. 17-18; p. 15, l. 301-302 |
| Quotation | "Fig7 illustrates the cloud maps of velocity distribution for the overall model and stress distribution along the sliding plane" |
| Concern | Each velocity panel has its own colour bar with only end values (0 to 5.9, 19.6, 27.1, 31.6, 25.7 and 0.21 m/s), so equal colours mean different velocities. In (a) both ends are "0m/s" and the whole model is red, the colour of maximum velocity in (b) to (f); in (g) the bar runs from 0 m/s at the top to 0.21 m/s at the bottom. The stress panels (h) to (n) do not say which stress component is shown (Table 2 lists Stress-XX, YY, ZZ), their axes carry numbers without quantity or unit, and they show a vertical section, not the "sliding plane" of the text. |
| Suggestion | Use one fixed colour scale with intermediate values for (a) to (g) and one for (h) to (n), name the stress component, label the axes with quantity and unit, and state where the section lies. |
| Status | verified |
| Severity | minor |
| Source | AB |

**GB-43 The stress sections in Fig7 (h) to (n) are about 290 m higher than the model described in the text.**

| Field | Content |
|---|---|
| Check | P3 |
| Location | Fig7 (h) to (n), p. 18; p. 9, l. 181-182 |
| Quotation | "The whole model contains 25345 blocks, 2788 m long, 3341 m wide, 1121m high, and the volume of the landslide is 317563 m3." |
| Concern | In Fig7 (h), calibrated on the ticks (600 dpi; 0 to 1200 on the vertical, 0 to 2700 on the horizontal axis), the section reaches 1411 m ± 3 m and spans 7 to 2861 m. The model height in the text is 1121 m, and the length of 2854 m is 66 m more than 2788 m. Panels (i) to (n) have the same outline. |
| Suggestion | State where the section runs and in which coordinate system, and reconcile its height with the model dimensions in l. 181-182. |
| Status | verified (measured on the page image) |
| Severity | moderate |
| Source | AB |

**GB-44 The initial state in Fig7 (h) shows zero stress throughout, although the method requires static equilibrium under gravity before dynamic loading.**

| Field | Content |
|---|---|
| Check | P5 |
| Location | Fig7 (h), p. 18 (colour bar "0" to "0Mpa"); p. 10, l. 199-202; p. 15, l. 304-305 |
| Quotation | "Dynamic loading must be introduced only after the model has attained static equilibrium; i.e., the dynamic analysis is predicated on a prior static analysis that has reached convergence." (l. 199-201); "Fig7. (a) and (h) show the initial state of the landslide" |
| Concern | Fig7 (h) is uniformly red with a colour bar from 0 to 0 MPa (confirmed on the page image), while panels (i) to (n) show stresses down to minus 47 MPa increasing with depth. A model in gravitational equilibrium has depth-dependent stress at t = 0 s. Either Fig7 (h) shows the state before gravity was applied, and then it is not the start of the dynamic stage, or the dynamic stage started without the static stage described in l. 199-202. Which applies? |
| Suggestion | State in the caption of Fig7 (l. 368-370) and in l. 304-305 which state Fig7 (h) shows, and add the converged static stress field and the unbalanced force at the end of the static stage to Sect. 2.1. |
| Status | verified (page image); which of the two readings applies inferred, asked as a question |
| Severity | moderate |
| Source | SD |

**GB-45 The constant energy sum presented as energy conservation of the whole mass, and the contrast with non-conserving single blocks, follow from the definition of DE in Eq. (4), not from the simulation.**

| Field | Content |
|---|---|
| Check | P23, P15, P3, P10 |
| Location | p. 19, l. 375-377 and l. 387-389; p. 13, l. 245-252 (Eq. 1 to 4); p. 20, l. 393-402; Fig8 (p. 20); Fig9 (a) to (j) (p. 21-22); p. 1, l. 26-28; p. 25-26, l. 476-482 (Conclusion 3) |
| Quotation | "It is evident that, due to the law of energy conservation, the total sum of the three forms of energy remains constant throughout the landslide." (l. 375-377); "As shown in Fig9., the energy variation curves indicate that, unlike the total landslide mass, the energy of single blocks is not conserved." (l. 393-394); "The results show that for the whole landslide, its energy change conforms to the law of conservation of energy" |
| Concern | The energy terms are defined explicitly (Eq. 1 to 4), which makes the bookkeeping checkable. With ME = KE + PE (Eq. 1) and DE(ti) = ME(t0) minus ME(ti) (Eq. 4), KE + PE + DE equals ME(t0) at every time, for every block and every sum of blocks, whatever the simulation does; a numerical check over 100000 random states gives a maximum relative deviation of about 1.6e-12, round-off only. The figures show exactly this: measured bar by bar, the top of the stacked bars stays at 6469 to 6516 GJ in Fig8 (1 px = 9.6 GJ) and within at most 3.5 px in every panel of Fig9 (for example (a) 5.062 GJ throughout, (e) 11.095 GJ throughout). The constant sum therefore cannot show conservation for the whole mass (l. 375-377), nor a "successful energy extraction numerical simulation" (l. 388-389), nor its absence for single blocks (l. 393-394). What can differ is the sign of the change of DE: DE of the whole mass rises monotonically, and DE of a block decreases when its PE + KE rises; measurable rises of PE occur only in Fig9 (a) and (c) (up to 0.042 and 0.069 GJ per step), with single steps in (d) and (g), so the statement for single blocks in general is not supported by eight of ten panels. For a single block the residual DE mixes dissipation (friction, damping) with work exchanged with neighbours, so a temporary decrease is a measured energy input, not an artefact of the calculation as l. 399-400 suggests. The balance also lists no inflow: the base is driven by the input motion (l. 189-191, l. 197-199), and under Eq. (4) the work it does is absorbed into DE with negative sign. The final clause of Conclusion 3 (l. 481) states the observable correctly, but the leading statements of Conclusion 3 and of the Abstract are stronger. Graded major because the result is named in the Abstract and Conclusion 3. |
| Suggestion | In Sect. 2.3 state that KE + PE + DE is constant by construction and how DE is obtained; in l. 26-28, l. 375-377, l. 388-389, l. 393-396 and Conclusion 3 replace "obeys the law of energy conservation" and "not conserved" by the observed quantities (monotonic decrease of ME of the whole mass; temporary increases of ME of the blocks in Fig9 (a), (c), (d), (g) with times and sizes). To test conservation, compute dissipation independently in 3DEC (frictional slip work at contacts and damping work), report PE + KE + DE(independent) minus ME(t0) over time, add a term for the work of the seismic input, and for single blocks report the work done by contact forces of neighbours; rename the block residual (for example "mechanical energy loss"). |
| Status | identity verified (Eq. 1 and 4; Python); constancy of the stacked totals verified by measurement on the page images; interpretation of DE decreases as work by neighbours and of the missing input term inferred |
| Severity | major |
| Source | S3, S4, AB, SD |

**GB-46 The energy totals in Fig8 cannot be reconciled with any stated landslide mass: the initial PE of about 6500 GJ and the KE peak of about 1660 GJ imply an impossible mean fall height or a mean speed above the reported maximum speed.**

| Field | Content |
|---|---|
| Check | P23, P2, P3, P9 |
| Location | Fig8, p. 20; p. 7, l. 151; p. 9, l. 174-175 and l. 182; Table 1 (density), p. 11; p. 16, l. 330; Fig9 (p. 21-22); Fig12 (p. 25) |
| Quotation | "Fig8. Evolution of energy during the landslide" |
| Concern | Measured on the page image, the bar total of Fig8 is about 6469 to 6516 GJ and the largest KE segment about 1657 GJ at about 13.6 s. With PE(t0) = m g h and KE = ½ m v² (Eq. 2, 3) and 2300 kg/m³ (Table 1, landslide mass): (A) model volume 317563 m³ (m = 7.30 × 10⁸ kg): mean height above datum 907 m (773 m with 2700 kg/m³), more than the full height of the mass plus its height above the river (747 m + 131 m = 878 m, l. 174-175); root-mean-square speed at the KE peak 67.4 m/s, more than twice the maximum of 31.6 m/s (l. 330), which a root-mean-square speed cannot exceed. (B) field volume 2400×10⁴ m³: mean height 12.0 m, although the mass descends several hundred metres and the smallest drop of any monitored block from Fig9 is about 30 m; the KE peak would correspond to 7.7 m/s. (C) literal printed value 249,600 m³ (KK-19): 1154 m and 76.0 m/s, both impossible. (D) Fig8 shows another population or unit; the text (l. 373-375) and the caption of Fig12 speak against a subset. The mean drop of the ten monitored blocks (169 m) would correspond to about 1.7 × 10⁶ m³. No single resolution makes PE and KE consistent at the same time; the mass entering Eq. (2) and (3), the datum (GB-31) and whether Fig8 sums all blocks would decide it. Graded major because all absolute energies in Fig8 and Fig12, including the 1116.8 GJ of the transition (GB-51), depend on it. |
| Suggestion | In Sect. 2.3 state the total mass used and the datum; in Sect. 3.2.1 give the initial PE, the peak KE with its time, and a check that the peak KE is compatible with the velocity field of Fig7 (for example the mass-weighted mean speed at 12 s). |
| Status | Fig8 values verified by measurement; manuscript values verified; implied heights and speeds inferred (Python); which resolution applies: open question to the authors |
| Severity | major |
| Source | S3, AB, SD |

**GB-47 The rise of collisions with travel distance is not shown as stated: Fig10 (b) is non-monotonic, gives absolute counts per bin without normalisation for time or number of blocks, and its quantity and fitted curve are undefined.**

| Field | Content |
|---|---|
| Check | P3, P21 |
| Location | p. 22, l. 414-421; Fig10 (b), p. 23; Fig5 (b) to (f), p. 12 |
| Quotation | "Combining this with Fig10. (b), it is clear that as the migration distance increases during the landslide, the number of collisions also rises continuously, reaching a peak once the blocks enter the river channel." |
| Concern | The y axis reads "Frequency" without saying per what (per 100 m bin, per block, all blocks); the red curve has no legend, equation or goodness of fit. Measured values (±0.2) fall from 15.9 to 6.9 between 700 and 800 m, from 27.0 to 19.9 between 900 and 1000 m, from 30.0 to 27.1 between 1200 and 1300 m and from 157.0 to 146.0 between 2300 and 2500 m; the largest step is 72.0 to 142.0 between 2100 and 2200 m, so "rises continuously" does not describe the points. The counts are absolute per 100 m bin (about 7.9 at 500 m and 142 at 2200 m, ratio 18.0). Along the profile of Fig5 (b) to (f) the speed falls from about 40 m/s near 500 m to about 10 m/s near 2200 m, so a block spends about four times longer in a bin near the river; per unit time the ratio would be about 18.0 × 10/40 = 4.5. The wording "the frequency at which individual blocks receive energy transfer" (l. 420) is a rate that Fig10 (b) does not show. If several blocks are pooled, the number of blocks reaching each distance is a second normalisation. The text (l. 414-415) describes collisions "experienced by blocks at different locations", but the x axis is travel distance, not location. |
| Suggestion | Define the y quantity and bin width of Fig10 (b), explain or remove the red curve, report collisions per second (or per time step) as a function of travel distance and divide by the number of blocks reaching each bin; describe the trend in l. 418-421 as found after normalisation, including the jump at 2100 to 2200 m. |
| Status | Fig10 (b) values verified by measurement; speeds from Fig5 read approximately; normalised ratio inferred |
| Severity | moderate |
| Source | S3, AB |

**GB-48 The vertical displacements of blocks 1, 3 and 5 in Fig10 (a) are several times the drops implied by their energies in Fig9.**

| Field | Content |
|---|---|
| Check | P3 |
| Location | Fig10 (a), p. 23; Fig9 (a), (c), (e), p. 21; Table 2, p. 13 |
| Quotation | "Fig10. (a) shows the trajectories of the 10 monitored blocks" |
| Concern | From Fig9 and Table 2, the total drop h = E0 / (ρ V g) with 2300 kg/m³ is 239 m for block 1 (5.062 GJ, 939.9 m³), 233 m for block 3 (3.976 GJ, 756.2 m³) and 317 m for block 5 (11.095 GJ, 1553.4 m³). In Fig10 (a), approximating the perspective axes from the tick labels, the vertical displacement compatible with the end points lies between 504 and 1129 m for block 1, 600 and 857 m for block 3 and 686 and 1311 m for block 5; even the lower bounds are about twice the drops from Fig9. Block 1 starts at z = 340 m (Table 2), so a drop of 504 m or more would take it below the model base. The trail of block 8 gives 92 to 218 m against 193 m from Fig9, which is consistent. |
| Suggestion | Check whether Fig9 and Fig10 (a) use the same blocks and the same vertical reference, and give Fig10 (a) axes with stated origin (displacement from start or absolute position). |
| Status | inferred (perspective calibration approximate; density assumed from Table 1) |
| Severity | moderate |
| Source | AB |

**GB-49 Fig11 shows neither volume nor area, its insets are not explained, and its axis ranges change from panel to panel.**

| Field | Content |
|---|---|
| Check | P29 |
| Location | Fig11 (a) to (j), p. 23-24; p. 23, l. 426-428 |
| Quotation | "This study utilized numerical simulation data of the landslide to perform Alpha Shape envelope fitting on the deposit mass at 10 representative time points, extracting the corresponding envelope volumes and surface areas (Fig11.)." |
| Concern | The panels show envelopes (light green) and, in insets, a dark green body; the caption speaks of "the shape of the landslide mass in numerical simulation" but does not say which is which. No volume or area value is given in any panel, and the axis ranges change (for example X from minus 1000 to 200 m in (a) and minus 1000 to 1500 m in (j)), so the growth cannot be seen. |
| Suggestion | Give V and S for each panel in Fig11 or in a table, explain the insets in the caption, and use common axis ranges. |
| Status | verified |
| Severity | minor |
| Source | AB |

**GB-50 Fragmentation and debris production are stated as the cause of envelope growth and of the rise of DE, but no fragmentation is measured and no breakage mechanism is described.**

| Field | Content |
|---|---|
| Check | P15, P31 |
| Location | p. 24, l. 445-452; p. 23, l. 429-431; p. 15-16, l. 319-327; p. 9, l. 178-181; Fig11 (p. 23-24); Fig12 (p. 25); p. 26, l. 488-492 (Conclusion 5) |
| Quotation | "In the process of energy transfer, collisions and friction cause block fragmentation and disintegration, producing large amounts of debris. These newly generated fragments fill the interior and surface of the deposit mass, causing a sudden expansion of the envelope volume" (l. 447-449); "it can be concluded that during energy transfer, collisions and friction cause blocks to fracture and disintegrate, generating a large amount of debris." |
| Concern | VS and AG give a reproducible measure of the envelope, but the Results measure only envelope volume and area and the energies. Sect. 2.1 describes a fixed set of 25345 blocks with Mohr-Coulomb contacts; no block count over time, fragment size distribution, number of broken contacts or other fragmentation measure is reported. A growing envelope is also produced by spreading of an unchanged set of blocks, which the manuscript itself calls "dispersion" (l. 271); DE as defined in Eq. (4) contains every loss of mechanical energy, including friction and damping, so its rise cannot confirm fragmentation (l. 451-452). The two causes of envelope growth are not separated. The Results frame the mechanism as an interpretation ("This phenomenon can be interpreted as follows", l. 445), Conclusion 5 turns it into "it can be concluded" (l. 489). Does "fragmentation" in the model mean separation of predefined blocks along the internal planes of l. 179-180 and Table 1? If so, "newly formed fragments" overstates what the model can produce. Graded major because Conclusion 5 rests on it. |
| Suggestion | Report a fragmentation measure over time in Sect. 3.4 (for example number of joint contacts broken, number of detached blocks or clusters) and separate envelope growth due to spreading from growth due to breakage, for instance by computing VS and AG for the block centroids of an unchanged block set; otherwise rewrite l. 445-452 and Conclusion 5 as a hypothesis in terms of dispersion. A run with breakable blocks (bonded sub-blocks with a tensile strength) compared with the present run would test the claim. |
| Status | absence of a fragmentation measure and of a breakage mechanism verified; fixed block count inferred (l. 181); whether blocks can break in this set-up: assumption, asked as a question |
| Severity | major |
| Source | S4, SD |

**GB-51 The solid to fluid transition at VS 29.47 % and AG 319.5 % has no criterion other than the KE maximum of Fig12, whose 1116.8 GJ is a third below the KE peak of Fig8, and Fig12 has about 30 points although envelopes were fitted at 10 times.**

| Field | Content |
|---|---|
| Check | P2, P3, P31 |
| Location | p. 25, l. 453-455; Fig12 (a) and (b) with the annotation "1116.8" (p. 25); Fig8 (p. 20); p. 23, l. 426-428; p. 24, l. 440-443; Fig11 caption l. 437-439 |
| Quotation | "the volume expansion rate reaches approximately 29.47% and the surface area growth reaches about 319.5%, it can be considered that the landslide transitions from a solid phase to a fluidized phase. At this point, the kinetic energy peaks" |
| Concern | Fig12 (a) and (b) mark the KE maximum at 1116.8 GJ (labels and plotted positions agree). In Fig8 the KE segment reaches about 1570 GJ at 12.4 s and 1657 GJ ± 20 GJ at 13.6 s, then falls to 795 GJ at 14.9 s; 1657 / 1116.8 = 1.48, a difference of about 540 GJ, about 25 times the reading uncertainty. KE of about 1116.8 GJ occurs in Fig8 near 11 s. Fig12 carries about 30 markers per curve (29 to 30 data points by morphological counting; confirmed on the page image), not the 10 times of Fig11, so either more envelopes were fitted than stated or values were interpolated; in either case the sampled maximum is not the KE peak of Fig8. No phase criterion is defined or measured (for example coordination number, granular temperature, ratio of collisional to frictional stress); the "transition" is the VS and AG value at the sampled KE maximum, so the two decimals of 29.47 % reflect the sampling, not a material threshold. Graded major because these values are the quantitative result of Sect. 3.4. |
| Suggestion | In Sect. 2.4 and 3.4 state the number and times of the envelope evaluations behind Fig12 and mark measured against interpolated points; reconcile the KE values of Fig12 and Fig8 or explain the difference; give VS and AG at the time of the Fig8 KE peak (about 13 to 14 s); define a phase criterion the DEM output can measure, or rephrase l. 452-455 as "the KE maximum coincides with VS of about 30 % and AG of about 320 %". |
| Status | 1116.8 GJ, labels and marker count verified on the page image; Fig8 peak verified by measurement; absence of a criterion verified; effect of the sampling on the threshold values inferred |
| Severity | major |
| Source | S3, AB, SD |

#### Minor corrections

| ID | Location | Quotation | Replacement | Source |
|---|---|---|---|---|
| KK-30 | p. 15, l. 301; p. 19, l. 368 and l. 369 | "the cloud maps of velocity distribution"; "cloud map of velocity"; "cloud map of stress" | "the contour maps of velocity distribution"; "contour map of velocity"; "contour map of stress" | S4 |
| KK-31 | p. 18, Fig7 (h) to (n) colour bars | "0Mpa", "-33Mpa", "-31Mpa", "-47Mpa" | "0 MPa", "-33 MPa", "-31 MPa", "-47 MPa" | S4, AB |
| KK-32 | p. 19, l. 372 (heading) | "3.2.1 Energy evolution for the whole debris mass" | "3.2.1 Energy evolution for the whole landslide mass" (the section uses "entire landslide mass", l. 373) | S2 |
| KK-33 | p. 20, l. 397-398 | "exhibit a rebound in potential energy after it approaches zero" | "exhibit a rebound in potential energy after their potential energy approaches zero" | S3 |
| KK-34 | p. 22, l. 410-413 (caption Fig9, nine times) | "energy evolution of point 1 ; (b)" | "energy evolution of point 1; (b)" (same for points 2 to 9) | S4 |
| KK-35 | p. 23, l. 425 (heading) | "3.4 Structural evolution as a function of energy change" | "3.3 Structural evolution as a function of energy change" (no Sect. 3.3 exists) | S3, S4, SD |
| KK-36 | p. 24, l. 438-439 (caption Fig11) | "(a-i) when time = 0s, 3s, 7s, 9s, 12s, 15s,32s,71s, 100s, 131s." | "(a) to (j) at t = 0, 3, 7, 9, 12, 15, 32, 71, 100 and 131 s." (ten times and ten panels) | S3, S4, AB, SD |

#### Verification log

| ID | Check | Checked | Values | Result |
|---|---|---|---|---|
| PP-22 | P11 | Matrix of cases (whole mass, blocks 1 to 10, ID 11) against the outputs announced in Sect. 2 (l. 77-90, l. 256-266, l. 270-296) | Present: Fig7 velocity and stress at seven times (14 panels and validation panel o); Fig8 whole-mass energy; Fig9 energy for all ten blocks; Fig10 (a) ten trails; Fig11 ten envelopes; Fig12 VS and AG; Fig5 all five thresholds; terrain restoration shown in Sect. 2 (Fig3) | missing cells see GB-36 |
| PP-23 | P2 | Quantities that appear in more than one place | Fig7 colour-scale maxima 5.9, 19.6, 27.1, 31.6, 25.7 m/s equal the text (l. 307, 315, 322, 330, 339); snapshot times 0, 3, 7, 9, 12, 15, 131 s equal in the Fig7 caption and among the Fig11 times; duration 131 s in l. 300-301, Fig7, Fig11, Fig8 and Fig9; thresholds 10 to 50 % in l. 230-232 and the Fig5 caption; ten monitoring points in l. 256, Table 2, Fig6, Fig9, Fig10 (a); impact "Around 13 seconds" (l. 383) between the 12 s and 15 s stages, consistent with the Fig8 KE maximum | no finding; inconsistencies in GB-16, GB-30, GB-31, GB-46, GB-51, GB-52 |
| PP-24 | P38 | Time points of figures and author identifiers | Fig7 times (l. 368-369) are a subset of the Fig11 times 0, 3, 7, 9, 12, 15, 32, 71, 100, 131 s (l. 438-439); Fig8 time axis ends at about 131 s; author initials YG, BH, HT, XF, LZ (l. 496-499) match the five authors | consistent; no finding |
| PP-25 | P3, P24 | Fig7 colour-bar maxima and times against the text | Colour-bar maxima read at 300 dpi: (b) 5.9, (c) 19.6, (d) 27.1, (e) 31.6, (f) 25.7, (g) 0.21 m/s; text l. 307 to 339 the same, (g) "gradually approached 0 m/s"; stress bar ends (h) 0, (i) minus 33, (j) minus 31, (k) to (m) minus 33, (n) minus 47 MPa; Fig8 last bar centred at 130.8 s | no finding |
| PP-26 | P24 | Time events in figures | No calendar dates in figures; Fig7 snapshot times against stage descriptions; Fig8 KE timing; Fig11 ten times against "10 representative time points" (agreement in number); Fig12 points against those times (GB-51); the year 1786 and the 9-day breach (l. 110-111) are not shown in any figure | no finding beyond GB-51 and KK-36 |
| PP-27 | P32 | Statements of the type "confirmed", "verified", "validation" | "confirming the previous inference" (l. 416), "further confirms significant fragmentation" (l. 451), "Validation of numerical simulation results" (l. 369-370), 1,139 detected collisions (l. 233-234); 4 statements, 0 with an independent check | consequences raised in GB-26, GB-41, GB-50; no separate finding |
| PP-28 | P25 | Whether each step uses information available to it | Whole-mass energy needs histories of all blocks, extracted according to l. 373-374 (feasible); partner and direction of a collision are not available from one velocity curve (GB-26, GB-52); the field-investigation findings of l. 265-266 are not reported (GB-39); 3 steps, 2 with missing information | no separate finding |
| PP-29 | P24 | Timing of kinetic energy in Fig8 against the text | 101 bars, mean spacing 1.296 s; KE (GJ): 0 at 1.2 and 2.5 s, 144 at 4.9 s, 450 at 6.2 s, 575 at 7.5 s, 670 at 8.6 s, 766 at 9.9 s, 1082 at 11.1 s, 1570 at 12.4 s, 1657 at 13.6 s, 795 at 14.9 s, 469 at 16.0 s, second maximum 680 at 33.5 s, below 100 after 49.7 s; PE 6497 GJ at 1.2 s and 6469 GJ at 2.5 s; text l. 378-384: small change 0 to 3 s, rise 3 to 12 s, sharp drop around 13 s | agrees within the bar resolution; no finding |
| PP-30 | P23 | Energy balance of the whole mass and of the ten blocks (stocks PE, KE; outflow DE; inflows) | Fig8 totals 6469 to 6516 GJ over 0 to 131 s; all Fig9 panels with flat totals; datum choice of l. 252-255 contradicted by the figures | balance closes by construction (GB-45); size incompatible with the stated masses (GB-46); datum see GB-31 |
| PP-31 | P3 | Block energies in Fig9 | Initial energy E0, maximum KE and drop h = E0 / (ρ V g) with 2300 / 2700 kg/m³: point 1: 5.062 GJ, 0.261 GJ, 239 / 203 m; 2: 5.134, 0.297, 223 / 190 m; 3: 3.976, 0.267, 233 / 199 m; 4: 3.565, 0.095, 163 / 139 m; 5: 11.095, 0.238, 317 / 270 m; 6: 6.591, 0.142, 173 / 147 m; 7: 1.178, 0.030, 30 / 25 m; 8: 4.367, 0.099, 193 / 164 m; 9: 1.595, 0.049, 82 / 70 m; 10: 0.947, 0.034, 43 / 37 m; PE rebound of blocks 1 and 3 (l. 397-399) confirmed (end values 0.362 and 0.331 GJ) | the PE rebound statement is confirmed; values used in GB-30, GB-31, GB-48 |
| PP-32 | P21 | Comparisons of absolute values on bases of different size | Fig9 shows absolute energies for blocks whose volumes differ by a factor of 2.32 (Table 2), y axes up to 1.2 to 12 GJ; Sect. 3.2.2 makes no quantitative comparison between blocks; sum of initial energies of the ten blocks (about 43 GJ) below the whole-mass total (about 6500 GJ), as required | no finding on Fig9; Fig10 (b) see GB-47 |
| PP-33 | P30 | Reported errors and their correction | None reported; the apparent DE decrease of single blocks is explained as a property of the calculation (l. 399-402), not as an error; 0 reported errors | no separate finding (see GB-45) |
| PP-34 | P20 | Every rate and "x of y" | VS and AG percentages (base V0, S0: GB-34); prominence threshold 30 % (no base: GB-23); 1,139 effective collisions (unit unclear: GB-29); "Frequency" in Fig10 (b) without unit (GB-47); no other rates in Sect. 3 | findings as listed |
| PP-35 | P22 | Numbering gaps and counts that follow from two places | Sections 3.1, 3.2 (3.2.1, 3.2.2), 3.4 (gap, KK-35); figures 1 to 12 and tables 1 and 2 without gaps; equations (1) to (6) without gaps; Fig11 panels a to j against caption "(a-i)" (KK-36) | findings as listed and GB-37 |
| PP-36 | P3 | Annotated values in Fig12 against their plotted positions | (a) red triangle at VS = 30.1 % ± 4 % (label 29.47); (b) at AG about 318 % (label 319.5); horizontal reference line at 1117 GJ (label 1116.8); initial PE and final DE about 6500 GJ, consistent with Fig8 | labels agree with plotted positions; no finding |
| PP-37 | P37 | Later corrections or recalculations of shown values | None declared; Fig8, Fig9 and Fig12 presented as direct outputs; 0 declared corrections | the Fig8 and Fig12 inconsistency is raised in GB-51 |
| PP-38 | P33 | Statements on effort, duration or amount of work | 0 statements used as result or limitation | no finding |

### Segment 4: Conclusions, declarations, references (p. 25 to 29)

#### Substantive findings

**GB-52 The claims that the lower or front mass collides more often, receives energy from the rear and travels farther have no corresponding result, and the design cannot separate collisions as cause of runout from runout as cause of counted collisions.**

| Field | Content |
|---|---|
| Check | P15, P2, P11, P9 |
| Location | p. 26, l. 483-487 (Conclusion 4); p. 1, l. 28-30 (Abstract); p. 3, l. 86-87; p. 22, l. 414-421; Fig10 (a) and (b) (p. 23); Fig9 (p. 21-22) |
| Quotation | "during the collapse stage, the front portion of the rock mass experiences more collisions than the rear portion, with a clear trend of decreasing collision frequency toward the rear. When the rear rock mass collides with the front, its dissipated energy sharply increases and transfers energy to the front rock mass, enabling the front portion to slide farther." (l. 484-487); "Compared with the upper rock mass, the lower rock mass is compressed more frequently, receives more energy transfer, and has a longer migration distance." |
| Concern | The only collision result is Fig10 (b), one pooled plot of collision frequency against travel distance. It distinguishes neither the position of the blocks (Table 2 zones) nor the time or stage; the collapse stage is Fig7 (d) and (k), t = 9 s (l. 322). Sect. 3 reports no travel distance per monitored block or position (Fig10 a shows trails without distances), no number of effective collisions per block, position or stage, and no paired energy changes when a rear block hits a front block; Fig9 shows DE per block, but the text does not relate rises of DE in rear blocks to decreases in front blocks. The step from "more collisions at larger travel distance" to "the front portion experiences more collisions" presupposes that front blocks travel farther, which is itself a claim. A block that travels farther passes more distance bins and accumulates more detected peaks even without any causal effect, so "collisions enable sliding farther" cannot be separated from "sliding farther yields more counted collisions"; the detector of Sect. 2.2 identifies a peak of one block, not the partner or the direction of transfer (GB-26), and no energy received per block is computed. The lower blocks 1 to 5 do drop more than the upper blocks 7, 9 and 10 according to the initial PE in Fig9 (PP-31), which bears on the runout part of the Abstract sentence but not on collisions or transfer. Is "Frequency" in Fig10 (b) counted per interval or cumulatively? If cumulative, its rise with distance holds by construction. Graded major because the Abstract and Conclusion 4 rest on it. |
| Suggestion | Add to Sect. 3.2.2 a table for the ten monitored blocks with position, travel distance, number of effective collisions in total, per 100 m and per second and within the collapse stage, and the number and size of temporary increases of mechanical energy from Fig9; to support the causal statement, use DEM contact records (partner block and contact force at each detected peak) and compute the work done on each block by its neighbours; a paired run with reduced interaction of the rear mass would test whether the front travels less far. Otherwise restate Abstract l. 28-30 and Conclusion 4 as what l. 418-421 shows. |
| Status | absence of a position- or stage-resolved result and of an energy-transfer measure verified (text, Fig10 on the page image); confounding by travel distance inferred; counting rule of Fig10 (b): assumption, asked as a question |
| Severity | major |
| Source | S3, S4, SD |

**GB-53 The code and data statements withhold all of the authors' own data and code "upon reasonable request" without giving a reason, although none of the data concern persons.**

| Field | Content |
|---|---|
| Check | P12 |
| Location | p. 26, l. 494-495 (Code availability) and l. 505-506 (Availability of data and material); data and code named in the Methods: p. 6, l. 130-135; p. 6-7, l. 138-143 and l. 157-162; p. 9-11, l. 168-213; p. 11, l. 220-234; p. 13, l. 256-264 and Table 2; p. 14, l. 272-284 |
| Quotation | "The codes that support the findings of this study are available from the first author, Yunfeng Ge, upon reasonable request." (l. 494-495); "The data and materials that support the findings of this study are available from the first author, Yunfeng Ge, upon reasonable request." |
| Concern | The manuscript has both statements, and each covers the whole study in one sentence. The Methods name at least eight own data sources and two own code components (PP-41). For none of them is a repository, persistent identifier or reason for withholding given, and none concern persons: terrain models, model files, simulation output, laboratory parameters. The central quantitative results (1,139 effective collisions, l. 233; VS of 29.47 % and AG of 319.5 % at the KE peak, l. 453-454; the energy curves in Fig8, Fig9 and Fig12) depend on the restored terrain, the 3DEC model, the peak-detection code and the alpha-shape code, none of which a reader can obtain without contacting the author. The data policy of Copernicus Publications as published for one of its journals asks the data statement to say where data will appear and requires a detailed explanation where data cannot be deposited publicly; whether the same wording applies to the target journal was not checked. |
| Suggestion | In "Code availability" and "Availability of data and material" (p. 26) deposit the UAV DEM or point cloud, the restored pre-landslide surface, the 3DEC input files, the monitoring histories, the collision-detection script with its prominence setting, and the alpha-shape script with the envelope volumes and areas in a public repository with a DOI, and cite it; for any part that cannot be released, state the reason. |
| Status | missing reason and repository verified (p. 26, page image); non-personal nature of the data verified (Methods); applicability of the publisher policy to the target journal inferred |
| Severity | moderate |
| Source | S2 |

**GB-54 The formatting of the reference list is not uniform.**

| Field | Content |
|---|---|
| Check | P16 |
| Location | p. 26-29, l. 508-605: entries Bernardie et al. (l. 508-510), Dahal et al. (l. 524-526), Nava et al. (l. 562-565), Sinčić et al. (l. 566-568), Zhang, K. et al. (l. 597-599); Fan et al., Rev. Geophys. (l. 530-532); Chen et al. (l. 517-520), He, J. et al. (l. 546-548), Zhang, J. et al. (l. 594-596); Tian et al. (l. 575-577); Cheng and Yu-Sheng (l. 521-523) |
| Quotation | "Fan, X., Scaringi, G., Korup, O., et al.:" |
| Concern | (1) The five entries named first are set in a smaller grey type and ragged right on the page images, unlike all others; all five are among the uncited entries of GB-02. (2) Only the Fan et al. Rev. Geophys. entry shortens the author list with "et al."; all other entries list every author. (3) Landslides vol. 21 is dated 2023 in two entries (He, J.; Zhang, J.) and 2024 in one (Chen). (4) "Cheng, F., and Yu-Sheng, L." breaks the pattern surname, initials. |
| Suggestion | Set all entries in the same type and justification, list all authors in the Fan et al. 2019 entry, date all entries by one rule (issue year or online year), and check the second author name of the Cheng entry. |
| Status | verified |
| Severity | minor |
| Source | S4 |

#### Minor corrections

| ID | Location | Quotation | Replacement | Source |
|---|---|---|---|---|
| KK-37 | p. 25, l. 464 and l. 466 | "It should be noted that:(a)"; "restoring the contours;(b)" | "It should be noted that: (a)"; "restoring the contours; (b)" | S4 |
| KK-38 | p. 26, l. 494 | "The codes that support the findings of this study are available" | "The code that supports the findings of this study is available" | S4 |
| KK-39 | p. 26, l. 499 | "XF: Data curation, Investigation. LZ: Data curation, Investigation." | "XF: Data curation, Investigation; LZ: Data curation, Investigation." | S4 |
| KK-40 | p. 26, l. 504 | "We thank editors and anonymous reviewers for their valuable comments." | "We thank the editor and the anonymous reviewers for their valuable comments." | S4 |
| KK-41 | p. 26, l. 507 (heading) | "Reference" | "References" | S4 |

#### Verification log

| ID | Check | Checked | Values | Result |
|---|---|---|---|---|
| PP-39 | P15 | Each statement of the Conclusions (l. 460-492) and the result sentences of the Abstract (l. 26-30) assigned to a place in the Results | Introductory sentence: no claim; Conclusion 1 first sentence: Sect. 2.1 and Fig3, supported as a visual result, items (a) and (b) without place (GB-14); Conclusion 2: extraction of KE, PE, DE for monitored blocks supported by Fig9, "ensures" stronger than l. 359 (GB-41), movement process Sect. 3.1, detection Sect. 2.2 and Fig5 as a method; Conclusion 3: by definition (GB-45), "dissipated energy continuously increases" supported by Fig8; Conclusion 4: no place (GB-52); Conclusion 5: envelope growth supported by Fig11 and Fig12, fragment generation without place (GB-50); no Discussion or Outlook section; the aims of l. 71-73 and l. 122-125 are not taken up in the Conclusions | findings as listed |
| PP-40 | P15 | Strength of the verbs in Abstract, Results and Conclusions against what the results show | "The results show" (l. 26), "conforms to the law of conservation of energy" (l. 27), "It is evident that" (l. 375-376), "successful energy extraction numerical simulation" (l. 388-389): GB-45; "it is clear that" (l. 418): supported for the pooled trend only; "further confirms significant fragmentation" (l. 451), "laying a solid foundation" (l. 430-431): GB-50; "presents compelling evidence" (l. 353) against "support the validity" (l. 359), "ensures" (l. 471): GB-41; "successfully reproduced the entire process" (l. 299): stronger than the qualitative check of Fig7 (o), GB-41 | findings as listed |
| PP-41 | P12 | Every data and code source named in Sect. 2 and in figures belonging to Segment 2 against the two statements on p. 26 | 12 sources: UAV DEM and point cloud (l. 130-135, own), restored contours and surface (l. 138-143, 157-162, own), geological map and "geological engineering drawing" (Fig2 c, l. 180, provenance not stated), remote sensing image (Fig2 b, not stated), Tiezhuang Temple tablet (l. 136-138, third party), Luding record (l. 189-191, third party), laboratory tests behind Table 1 (l. 206-207, own, results not reported), 3DEC model files (own), monitoring histories (own), collision detection code and output (own), alpha-shape code and output (own), field findings and photographs (l. 265-266, Fig7 o, own); no appendix or supplement | 8 own sources only "on request" without reason (GB-53); 4 third-party or unattributed sources without provenance (GB-25) |
| PP-42 | P12 | Links and identifiers in the statements and in Sect. 2 | 0 URLs, 0 DOIs, 0 repository names in l. 493-506 and in Sect. 2; the reference list contains DOIs for literature only | no link to check for reachability |
| PP-43 | P16 | Language and typesetting of all 29 pages on the page images; extraction artefacts separated from real errors; uniformity of the reference list | Rejected as extraction artefacts: missing "=", "+" and minus in Eq. (1) to (4) in the extracted text (present on the page image); "c Author(s)" is the © sign; superscripts in "(kg/m3)", "km2" and "m3" present; diacritics in Grémont, Lourenço, Mihalić, Sinčić correct; wide word spacing in reference lines with long URLs is justification, not an error. Confirmed: exponent missing in "2400×104" (l. 151, KK-19); plain hyphens in l. 193, 218 and 228 (KK-22, KK-24, KK-25) | findings in GB-04, GB-54 and the minor corrections |

## Optional checks

| Area | What it needs | Responsible | Run |
|---|---|---|---|
| DOI resolution | one request per reference entry | `science-quellenapparat-pruefung` | no |
| Citation style | the name of the style | `science-zitierstil-harvard-ctr` or the style rules of the journal | no |
| AI statement against publisher policy | the policy of the target publisher | this review, on request | no |
| Relation to the authors' own prior work | the authors' prior publications | this review, on request | no |
| Journal requirements | the author guidelines of the target journal | this review, on request | no |
| Factual accuracy | access to the sources of each checked statement | `science-faktenbeleg-pruefung`, `geo-frage-belegbasiert-klaeren` | no |

## Limits of this review

- Reviewed version: egusphere-2025-4506.pdf, 29 pages, SHA-256 64cb3787456244aa6102e34f776b47e9a612d06e8894d391758ae240dbe415d6.
- Basis: the manuscript alone; the discussion page, other reviews, author replies and later versions of the manuscript were not read.
- Merging: the six instances delivered 87 substantive findings, 70 minor corrections and 43 verification logs. 0 findings were discarded for missing mandatory fields or failed checks at the manuscript. 33 substantive findings were merged into others (87 to 54); two instance findings were split between two merged findings (the volume and energy parts of one, the two naming parts of another). 9 minor corrections were folded into substantive findings with the same location and object, and 20 duplicate minor corrections were merged (70 to 41). One note outside the checklists was adopted after rechecking the manuscript (backflow flooding, l. 350-352, origin ZF, part of GB-39); the other notes were already treated by the responsible instance.
- Corrections during merging: the location of KK-01 was corrected from l. 14 to l. 13 at the page image; the description of Lin et al. (2022) in GB-08 was corrected after reading its abstract, which attributes the rear-to-front transfer to fragmentation rather than to the rear block striking the front one.
- Assignment to segments: each finding stands in the segment of its first location, and the first location is the place where the object of the finding is stated or shown in the body of the manuscript (definition, result, figure); repetitions in the Abstract and Conclusions are listed after it.
- Sources not readable: Fan et al. (2019, Rev. Geophys.), Cheng (2014), Song et al. (2017), Wu et al. (2024), Ge et al. (2021), full texts of Zhao et al. (2021) and Du et al. (2021), and the data policy page of the target journal. Literature statements from Lin et al. (2022), von Wartburg et al. (2020) and Zhao et al. (2021) were rechecked at the source during merging.
- Figure values rest on measurements of the raster images (150 to 600 dpi), not on source data, which are available only on request (GB-53).
- Findings with status assumption: 0 of 54 have an assumption as their central statement; 10 of 54 (GB-02, GB-21, GB-22, GB-24, GB-25, GB-29, GB-30, GB-32, GB-50, GB-52) contain an assumption as a partial statement, each phrased as a question to the authors.
- Optional checks run: 0 of 6.
