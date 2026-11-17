# Review report: Energy and structural evolution process of high-altitude and long-runout landslides induced by a strong earthquake

| Field | Value |
|---|---|
| Manuscript | Ge, Y., Hu, B., Tang, H., Fu, X., and Zhu, L. (2025): Energy and structural evolution process of high-altitude and long-runout landslides induced by a strong earthquake, EGUsphere preprint, https://doi.org/10.5194/egusphere-2025-4506 |
| Checked version | egusphere-2025-4506.pdf, 29 pages, SHA-256 64cb3787456244aa6102e34f776b47e9a612d06e8894d391758ae240dbe415d6 |
| Date | 2026-10-22 |
| Language | English |
| Review instances | Segments 1 to 4, figures, study design; run sequentially in one context, not context-separated (nacheinander geprüft, nicht kontextgetrennt); no instance omitted |
| Note | The manuscript prints line numbers every fifth line; all line numbers below were read from these printed margin numbers on the page images. |

## Summary

The manuscript is a single-case numerical back-analysis of the Mogangling rock avalanche on the Dadu River (Luding County, Sichuan), triggered by the 1786 Kangding earthquake. The pre-failure topography is restored by straightening the contours of a UAV-derived DEM. The sliding mass is divided into blocks on an 8.7 m × 8.7 m grid in 3DEC (25345 blocks in the whole model; landslide volume 317563 m3 in the model against about 2400×10^4 m3 stated for the field). It is loaded with the acceleration record of the Luding station from the 2008 Wenchuan earthquake. Kinetic, potential and dissipated energy are computed for the whole mass and for 10 monitored blocks, with the dissipated energy defined as the loss of mechanical energy. Effective collisions are detected as velocity peaks above a 30 % prominence threshold (1,139 reported). Alpha-shape envelopes (α = 1) at 10 times give volume swelling and area growth. The manuscript reports a runout of 131 s with a largest velocity of 31.6 m/s, a constant total energy of the whole mass, non-conserved energy of single blocks, collision counts rising with travel distance, and a transition from solid to fluidized behaviour at a volume swelling of 29.47 % and an area growth of 319.5 %.

## Strengths

1. The restoration of the pre-failure terrain is documented as a chain of steps (DEM, contour generation, straightening, point cloud, noise reduction, normal correction; Fig. 1, l. 130 to 143), with maps before and after restoration and a profile (Fig. 3). A reader can therefore inspect the restored geometry, and the stated elevations form a contiguous slope description (PP-10).
2. The effect of the prominence threshold on peak detection is shown for five thresholds (Fig. 5b to 5f). The number of marked peaks falls steadily from 164 to 64 (PP-09), so the reader sees how strongly the detected collisions depend on this choice.
3. The kinematic stages are reported with values that agree with the figures. Stage velocities and times in Sect. 3.1 match the colour bars and caption of Fig. 7, the drop of kinetic energy at about 13 s matches Fig. 8, and the values in Sect. 3.4 match the annotations of Fig. 12 (PP-15, PP-16, PP-20).
4. Key limitations are disclosed where the method is introduced: the missing instrumental record of 1786 and the use of a proxy record, the lack of data on structural planes, and the dam break that is not modelled (PP-04, PP-13).

## Weaknesses

1. The energy analysis does not test what it reports. Conservation follows from Eq. (4) for the whole mass and for every block (GB-20). The magnitudes in Figs. 8 and 12 fit neither stated volume (GB-21), and length, area and volume of the mass disagree (GB-07). Suggestion: close an independent energy balance from 3DEC (work of gravity and of the seismic input, friction, damping, boundary absorption) for the volume actually simulated.
2. The collision analysis takes velocity peaks as collisions without verification (GB-13). Its counts are neither normalised (GB-23) nor tied to a defined unit (GB-14), and conclusion 4 has no result per zone behind it (GB-28). Suggestion: validate the detector against contact events, normalise per block and per distance, and report collisions per zone.
3. The model is validated only qualitatively, with a single run (GB-18). The failure mechanism invokes structural planes that the model is said to ignore (GB-10), and fragmentation (GB-26) and the solid to fluid transition (GB-27) are asserted without a measure. Suggestion: calibrate against quantitative deposit targets with a sensitivity set, describe the modelled joints, and measure fragmentation and fluidization directly.
4. Reproducibility and positioning are weak. The input motion, model settings and alpha-shape parameters are underspecified (GB-11, GB-12, GB-17), data and code are available only on request (GB-29), the reference list does not match the citations (GB-30), and the gap claims ignore the authors' own earlier study (GB-02). Suggestion: add a model table, deposit data and code, repair the reference list, and set the contribution apart from Ge et al. (2021).

## Findings by segment

### Segment 1: Title, abstract, introduction (p. 1 to 2, l. 1 to 73)

#### Substantive findings

**GB-01 Two cited sources do not support the statements they are cited for**

| Field | Content |
|---|---|
| Check | P13 |
| Location | p. 1, l. 33 to 34; p. 2, l. 45 to 46 |
| Quotation | "the chain disasters of high-level rock landslides in high-intensity earthquake areas have shown a trend of frequent occurrence (Carpignano et al., 2009; Fan et al., 2019a)" |
| Concern | Carpignano et al. (2009, J. Risk Res., 12, 513 to 534) develop a multi-risk decision support approach for the Piedmont Region, Italy. Their abstract does not mention earthquake-induced landslides, disaster chains or their frequency. In l. 43 to 46, the use of "photos, field surveys, optical remote sensing images" and UAV data to "build geomorphic maps through GIS" is attributed, among others, to Song et al. (2017) and Wu et al. (2024). Song et al. (2017) predict the deformation of a reservoir landslide in the Three Gorges with a 3-D numerical model checked against GPS monitoring; GIS mapping, photographs and UAV data are not mentioned. Wu et al. (2024) could not be read. Its title in the reference list ("Numerical simulation on potential landslide-induced wave hazards by a novel hybrid method") indicates a numerical study of landslide-generated waves. |
| Suggestion | In l. 33 to 34, replace Carpignano et al. (2009) with a source on the frequency of coseismic landslide chains, or remove it, and write "the Donghekou" for "donghekou" in l. 34. In l. 45 to 46, cite works that build geomorphic maps from photographs, UAV and remote sensing data, and correct "Song at al.2017" to "Song et al., 2017". |
| Status | verified (Carpignano et al., 2009, and Song et al., 2017: abstracts read); inferred (Wu et al., 2024: not readable, judged from its title) |
| Severity | moderate |
| Source | S1 |

**GB-02 Gap claims are stated without a search, and one is contradicted by a work in the own reference list**

| Field | Content |
|---|---|
| Check | P28 |
| Location | p. 2, l. 42; l. 50 to 51; l. 61 to 64 |
| Quotation | "However, they still lack a quantitative and systematic study of this topic, especially on energy evolution during the collision." |
| Concern | The introduction claims that "the terrain restoration before a landslide is less" (l. 42), a sentence that is also not understandable as written. It claims that contour restoration "can provide a new idea of terrain restoration" (l. 50 to 51) and that quantitative studies of energy evolution during collisions are lacking (l. 63 to 64). No database, search terms or search date are given. Ge, Tang and Li (2021, Landslides, 18, 3559 to 3576) appear in the reference list (p. 27, l. 540 to 542) but are not cited in the text. According to their abstract, they extracted kinetic, potential and dissipated energy from kinematic parameters and identified effective collisions from local velocity peaks. They also found that blocks at the front collide more often, receive more energy and travel farther. This covers the gap claimed in l. 63 to 64 and anticipates conclusions 3 and 4 (p. 25 to 26, l. 476 to 487). Earlier work on terrain restoration is treated in GB-03. |
| Suggestion | Cite Ge et al. (2021) in the introduction and state what the present study adds beyond it (the case, the seismic loading, the alpha-shape indices). Reword l. 42, l. 50 to 51 and l. 63 to 64 as delimited claims, or report the literature search that supports them. |
| Status | verified |
| Severity | moderate |
| Source | S1 |

**GB-03 Works that precede the terrain restoration and the fragmentation interpretation are missing**

| Field | Content |
|---|---|
| Check | P14 |
| Location | p. 2, l. 49 to 51; p. 24, l. 447 to 450 |
| Quotation | "This paper uses the method of restoring the continuity of contour lines to establish the terrain data before a landslide, which can provide a new idea of terrain restoration" |
| Concern | Two works that are not in the reference list bear directly on the contribution. (1) Jaboyedoff, M., Chigira, M., Arai, N., Derron, M.-H., Rudaz, B., and Tsou, C.-Y.: Testing a failure surface prediction and deposit reconstruction method for a landslide cluster that occurred during Typhoon Talas (Japan), Earth Surf. Dynam., 7, 439 to 458, https://doi.org/10.5194/esurf-7-439-2019, 2019. This study reconstructs failure surfaces, deposits and palaeotopography with the sloping local base level method, reports volumes within about ±35 % of published values, and notes a strong sensitivity to the parameters. It restricts the novelty claim and offers a quantitative benchmark for the contour method. (2) Zhao, T., Crosta, G. B., Utili, S., and De Blasio, F. V.: Investigation of rock fragmentation during rockfalls and rock avalanches via 3-D discrete element analyses, J. Geophys. Res. Earth Surf., 122, 678 to 695, https://doi.org/10.1002/2016JF004060, 2017. This study models fragmentation in a 3-D DEM through bond breakage and links fragmentation intensity to input energy, whereas the manuscript infers fragmentation (l. 447 to 450) without describing a breakage mechanism. Both abstracts were read. |
| Suggestion | Discuss Jaboyedoff et al. (2019) in the introduction (l. 42 to 51) and compare the contour restoration with their method. Discuss Zhao et al. (2017) in Sect. 3.4, where fragmentation is interpreted, and state how fragmentation is represented in the present model. |
| Status | verified |
| Severity | moderate |
| Source | S1 |

**GB-04 Core terms of the aims are not taken up in the conclusions**

| Field | Content |
|---|---|
| Check | P15, P10 |
| Location | p. 2, l. 65 to 73; p. 25, l. 460 to 479; p. 26, l. 480 to 492 |
| Quotation | "it focuses on revealing the mechanisms of energy accumulation, transfer, and dissipation during the landslide event" |
| Concern | The aims name "energy accumulation" (l. 68), the "spatiotemporal evolution of velocity, and debris flow propagation characteristics" (l. 70 to 71) and "early warning and risk mitigation" (l. 72). None of these recurs in the five conclusions, and the manuscript has no discussion section in which they could be taken up. The energy analysis shows only the decrease of potential energy from its initial value, and no research question links the aims to the instruments. |
| Suggestion | Add a discussion section that answers each aim of l. 65 to 73, or narrow the aims to what Sect. 3 delivers. |
| Status | verified |
| Severity | moderate |
| Source | S4, SD |

#### Minor corrections

| ID | Location | Quotation | Replacement | Source |
|---|---|---|---|---|
| KK-01 | p. 1, l. 36 | "Wang, 2021" | "Wang et al., 2021" | S4 |
| KK-02 | p. 2, l. 44 | "optical remote sensing images and UAV impact" | "optical remote sensing images and UAV imagery" | S4 |
| KK-03 | p. 2, l. 48 to 49 | "Cheng 2014" | "Cheng and Yu-Sheng, 2014" | S4 |

#### Verification log

| ID | Check | Checked | Values | Result |
|---|---|---|---|---|
| PP-01 | P13 | Sentences in Sect. 1 that attribute statements to cited works | l. 34 Carpignano et al. 2009 (read, does not support, GB-01); l. 34 Fan et al. 2019a (title of the Rev. Geophys. entry fits); l. 35 to 36 Sun 2011, Wang 2014, Wang 2021 (titles concern the Donghekou landslide, consistent); l. 36 to 37 Hu 2017 (title concerns Ludian landslides, consistent); l. 45 to 46 Song 2017 (read, does not support), Wu 2024 (not readable); l. 48 to 49 Du 2021, Cheng 2014, Li 2024 (not opened); Sect. 1 quotes no numbers from cited works | finding GB-01; no finding for the others checked |
| PP-02 | P14 | Literature search on the contribution (four queries) | "Mogangling landslide 1786 earthquake numerical simulation runout Dadu River"; "sloping local base level SLBL reconstruction pre-failure topography landslide volume Jaboyedoff"; "Zhao Crosta Utili De Blasio rock fragmentation rockfalls rock avalanches 3-D discrete element energy JGR Earth Surface 2017"; "momentum transfer rock avalanche rear blocks push front blocks travel farther Van Gassen Cruden 1989"; candidates checked against the reference list: Zhao et al. 2021 and Zhou et al. 2024 (listed, uncited, GB-30), Wang et al. 2020 on the Baige dam flood (not relevant), EPFL records on momentum transfer (not readable) | two missing works, GB-03 |
| PP-03 | P28 | Gap and novelty sentences and the search behind them | l. 42 "the terrain restoration before a landslide is less"; l. 50 to 51 "a new idea of terrain restoration"; l. 61 "direct observation data are rarely available"; l. 63 to 64 "still lack a quantitative and systematic study"; search method stated: none | finding GB-02 |

### Segment 2: Methods (p. 2 to 15, l. 74 to 296)

#### Substantive findings

**GB-05 Rock units in the text and in the map legends differ**

| Field | Content |
|---|---|
| Check | P3 |
| Location | p. 5, l. 101 to 104; Fig. 2c; Fig. 3a; Fig. 3b; Fig. 4 |
| Quotation | "The sand slate of the Triassic Baiguowan formation (T3bg) is exposed on the left bank of the Dadu River." |
| Concern | The text names plagioclase granite (γO2), quartz diorite (O2) and Triassic sand slate (T3bg) on the left bank. The legend of Fig. 2c shows γo2 "Plagiogranite" and γM2 "Hybrid granite", the latter on the left bank at Huashibao, but neither O2 nor T3bg. Fig. 4 also shows γM2 on the left bank. Figs. 3a and 3b show "Granite" and "Diorite", with diorite beneath the valley floor in the profile. The bedrock is a single material in the model (Table 1), so the discrepancy affects the description only. |
| Suggestion | Use the same unit names and symbols in l. 101 to 104 and in the legends of Figs. 2c, 3 and 4. |
| Status | verified |
| Severity | minor |
| Source | AB |

**GB-06 Several sentences are ungrammatical or use calques**

| Field | Content |
|---|---|
| Check | P16 |
| Location | p. 5, l. 113 to 119; p. 10, l. 193 to 195; p. 15, l. 301 |
| Quotation | "In the course of a discrete-element simulation-particularly when modeling nominally semi-infinite bodies such as the use of fixed or elastic boundaries in a static analysis will inevitably reflect outbound seismic waves into the model" |
| Concern | In the quoted sentence (l. 193 to 195), "will inevitably reflect" has no grammatical subject. L. 113 to 119 is a single sentence of seven lines with the nested structure "the analysis of ... and the evaluation and analysis of ... such as surging waves are relatively few". The term "cloud maps" (l. 301; "cloud map" in the caption of Fig. 7) is a calque for contour plots. A hyphen stands in for a dash in "simulation-particularly" (l. 193); the same in l. 228 is treated in GB-13. |
| Suggestion | Rewrite l. 193 to 195 as "In a discrete-element simulation of a semi-infinite body, fixed or elastic boundaries used in the static analysis reflect outgoing seismic waves back into the model during the subsequent dynamic analysis." Split l. 113 to 119 into separate sentences, replace "cloud map" with "contour plot", and use a comma instead of the hyphen in l. 193. |
| Status | verified |
| Severity | minor |
| Source | S4 |

**GB-07 Length, area and volume of the landslide disagree with each other and with the model**

| Field | Content |
|---|---|
| Check | P1, P2 |
| Location | p. 7, l. 149 to 151; l. 151 to 156; p. 9, l. 174; l. 182; Fig. 2c; Fig. 4 |
| Quotation | "about 450 m long, about 1000 m wide along the river, and a planar area of 0.45 km2. The average thickness of the landslide mass is about 100 m, and the volume is about 2400×104 m3" |
| Concern | (1) Area times thickness gives 0.45×10^6 m2 × 100 m = 4.5×10^7 m3, which is 1.88 times the stated 2.4×10^7 m3; the stated volume implies a mean thickness of 53 m. (2) The slope segments in l. 151 to 156 (1120 to 1330 m at 50°, 1330 to 1380 m at 5 to 12°, 1380 to 1600 m at 35°, 1600 to 1890 m at 57°) give a horizontal length of 210/tan 50° + 50/tan 8.5° + 220/tan 35° + 290/tan 57° = 176 + 335 + 314 + 188 = 1013 m (914 m with 12° and 1250 m with 5° on the platform). The model mass is 1021 m long (l. 174, Fig. 4). The boundary in Fig. 2c measures about 1237 m along 75° and about 1018 m across and encloses about 0.99 km2 (scale bar 600 m = 273.5 px at 300 dpi). The 450 m and 0.45 km2 thus disagree with the scale of about 1000 m given by all other sources. (3) The model volume of 317563 m3 (l. 182) is 2.4×10^7 / 317563 = 75.6 times smaller than the field volume, and the text does not say whether the model represents only part of the mass. In the page image, "2400×104" lacks the superscript of 10^4. |
| Suggestion | In Sect. 2.1, state one consistent set of length, width, area, mean thickness and volume with their sources, and explain how the model volume (l. 182) relates to the field volume. Write "2400×10^4 m3" in l. 151 and "1121 m" in l. 182. |
| Status | verified (stated values, page image, measurement in Fig. 2c); inferred (computed products and lengths) |
| Severity | major |
| Source | S3, AB |

**GB-08 The section line b-b' cited in the text does not exist**

| Field | Content |
|---|---|
| Check | P4, P3 |
| Location | p. 7, l. 159 to 160; Fig. 2c; Fig. 3b |
| Quotation | "make a section along a-a'and b-b' in Fig2. (c). The results are shown in Fig3. (c)." |
| Concern | Fig. 2c shows one section line, labelled "a" at both ends. Fig. 3b shows only "(a-a')", and Fig. 3c shows contour and terrain maps, not section results. |
| Suggestion | Label the east end of the line a' in Fig. 2c, delete "and b-b'" or add the second section, and refer to Fig. 3b for the section results. |
| Status | verified |
| Severity | minor |
| Source | S4, AB |

**GB-09 Axes, symbols and curves are not explained in several figures**

| Field | Content |
|---|---|
| Check | P29 |
| Location | Fig. 3b (p. 8); Fig. 4 (p. 10); Fig. 7h to 7n (p. 18); Fig. 10b (p. 23); Fig. 6 (p. 14) |
| Quotation | "Fig4. Discrete numerical model with fine topography" |
| Concern | Fig. 3b: neither axis has a quantity or unit. Fig. 4, inset: the time axis has ticks but no values and no unit, and tp, tPGA, tf and te are not defined in the caption or the text. Fig. 7h to 7n: the axes have no quantity or unit, and the stress component shown is not named. Fig. 10b: the red curve, apparently a fit, is not explained. Fig. 6: the point colours have no key and differ from the line colours of Fig. 10a. |
| Suggestion | Add axis titles with units, define the inset symbols in the caption of Fig. 4, name the stress component in the caption of Fig. 7, and state the fitted function in the caption of Fig. 10. |
| Status | verified |
| Severity | minor |
| Source | AB |

**GB-10 The model ignores structural planes, but the results invoke them**

| Field | Content |
|---|---|
| Check | P6 |
| Location | p. 9, l. 176 to 180; p. 11, l. 209 to 212; Table 1; p. 15, l. 308 to 313; l. 323 |
| Quotation | "the impact of the structural plane on the landslide process has to be ignored in this study" |
| Concern | Two lines later the text states "A uniform structural plane is set inside" (l. 179 to 180), and l. 209 to 212 and Table 1 define "discontinuities" and "potential discontinuities" as "fully developed potential rupture planes and joint sets". Sect. 3.1 explains the failure by "intense vertical dislocation along the steeply dipping structural planes outside the slope" (l. 308 to 309), by tensile cracking "along these structural planes" (l. 310), by "pre-existing potential sliding surfaces" (l. 313) and by "structural plane control" (l. 323). The manuscript does not state which planes exist in the model or how they are oriented, so the mechanism in Sect. 3.1 cannot be traced to the model. |
| Suggestion | Describe in Sect. 2.1 the geometry (orientation, spacing, persistence) of every joint set and potential rupture plane in the model, reconcile this with l. 176 to 178, and restrict the mechanism in Sect. 3.1 to planes that are modelled. |
| Status | verified |
| Severity | major |
| Source | SD |

**GB-11 The proxy ground motion is neither supported by a source nor specified**

| Field | Content |
|---|---|
| Check | P9, P8 |
| Location | p. 10, l. 183 to 191; Fig. 4 |
| Quotation | "Extensive research indicates that the Kangding earthquake is comparable to the 2008 Wenchuan earthquake in terms of damage distribution, affected intensity, and estimated magnitude." |
| Concern | The lack of an instrumental record is disclosed where the method is introduced. The claim of comparability, however, has no citation, and the record is not specified: component, direction of application, duration, scaling or filtering and peak value are not stated. The inset of Fig. 4 has an amplitude axis of about ±150 gal but no time values. The manuscript does not discuss whether a record from the Luding station of the 2008 event represents the shaking of a slope next to the 1786 source. It is a question whether a near-source motion would be markedly stronger. The velocities and timing of the initiation in Sect. 3.1 depend on this input. |
| Suggestion | Cite the studies behind l. 187 to 189. State the component, direction, duration, scaling and PGA of the input in Sect. 2.1, and test at least one scaled or near-source input. |
| Status | verified (missing citation and specification); assumption (representativeness of the record) |
| Severity | moderate |
| Source | SD |

**GB-12 Model settings and the energy reference level cannot be reproduced from the text**

| Field | Content |
|---|---|
| Check | P8, P35 |
| Location | p. 10, l. 196 to 204; p. 13, l. 252 to 255; Table 1; Table 2 |
| Quotation | "uses the model’s initial height as the reference datum rather than true sea level" |
| Concern | Several settings are not stated: the 3DEC version, rigid or deformable blocks and the zone size, the contact law for block impacts during runout, the damping type and value, the time step and output interval, and the coordinate frame of Table 2 (x negative, z from 340 to 755). The reference level is also ambiguous. With the initial height as datum, PE(t0) would be zero, yet l. 252 equates ME(t0) with the initial potential energy, and Figs. 8 and 9 show PE falling to zero. The block energies imply drops of 238.6 m (point 1, z = 340 m), 316.7 m (point 5, z = 498 m), 29.8 m (point 7, z = 661 m) and 43.4 m (point 10, z = 755 m), i.e. different datum levels for different blocks, apparently each block's lowest or final elevation. Table 1 gives a shear stiffness above the normal stiffness for both joint types (1500 against 960 GPa/m, 180 against 100 GPa/m). Is this intended? The usual ratio is the reverse. |
| Suggestion | Add a model table to Sect. 2.1 with the missing settings, define the reference level of PE explicitly, and check the stiffness values in Table 1. |
| Status | verified (missing settings, ambiguous wording); inferred (datum from the figure values); assumption (stiffness ratio) |
| Severity | moderate |
| Source | SD |

**GB-13 Velocity peaks are taken as collisions without verification**

| Field | Content |
|---|---|
| Check | P31, P27 |
| Location | p. 11, l. 220 to 234; Fig. 5 |
| Quotation | "At a threshold of 30%, however, the identification of effective collisions is deemed acceptable." |
| Concern | A local velocity maximum marks the change from acceleration to deceleration. Besides a collision, it occurs at changes of slope gradient, during the seismic shaking and from numerical noise. The prominence threshold is given in percent without saying of what quantity, and 30 % is chosen by judgement. No detected peak is checked against contact events or contact forces from 3DEC. The unverified detections feed Fig. 10b, l. 418 to 421 and conclusion 4. |
| Suggestion | Define the prominence and state what it is relative to. Validate the detector on a sample of blocks against recorded contact events (hits and false alarms per threshold), and separate peaks during the shaking from later ones. Write "chosen, one" for "chosen-one" in l. 228. |
| Status | verified (missing definition and verification); inferred (alternative causes) |
| Severity | major |
| Source | SD |

**GB-14 The profile in Fig. 5b to 5f and the count of 1,139 collisions are not identified**

| Field | Content |
|---|---|
| Check | P20, P3 |
| Location | p. 11, l. 233 to 234; Fig. 5b to 5f; Fig. 10b; p. 16, l. 330 |
| Quotation | "Under this setting, 1,139 effective collisions were detected from the travel-distance versus velocity profile." |
| Concern | The sentence speaks of one profile. The main panel of Fig. 5d shows about 71 marked peaks (touching markers counted as one), and the bin values of Fig. 10b sum to about 1215 (24 dots measured, two hidden near zero). The manuscript does not say whether 1,139 refers to one block, the 10 monitored blocks or all blocks, nor over which time window. The profile itself peaks at 45.5 ± 0.1 m/s in Fig. 5b (calibration 50 m/s at 707.0 px and 30 m/s at 898.0 px; the marker radius adds about 0.3 m/s) and runs to about 2400 m. The largest velocity stated for the model is 31.6 m/s (l. 330). Is the profile taken from the same run, from one block, or from a velocity computed differently? |
| Suggestion | State in Sect. 2.2 the unit of analysis of the count (blocks, time window), name the block and run behind Fig. 5b to 5f in the caption, and make Fig. 10b and the count consistent. |
| Status | verified (counts and peak measured); inferred (unit and relation to Fig. 7) |
| Severity | moderate |
| Source | S3, AB |

**GB-15 Several objects carry two or more names without explanation**

| Field | Content |
|---|---|
| Check | P38 |
| Location | p. 14, l. 275; l. 278 to 280; p. 24, l. 440 to 441; p. 1, l. 25; p. 11, l. 221 to 227; p. 1, l. 23; p. 25, l. 474 to 475; Fig. 5a; Table 2; Fig. 2b |
| Quotation | "two dimensionless indices are introduced: volume swelling (VS) and area growth (AG)" |
| Concern | (a) VS is called "volume swelling" (l. 275) and "volume expansion rate" (l. 25, l. 441); AG is called "area growth" (l. 275), "area growth rate" (l. 25) and "surface area growth rate" (l. 441); the area is S in Eq. (6) and l. 279 to 280 but A in l. 440. (b) The curve used to detect collisions is called "velocity-travel-distance curve" (l. 221), "velocity-distance profile" (l. 225), "velocity-distance curve" (l. 227), "travel-distance versus velocity profile" (l. 234), "displacement velocity curve" (l. 23) and "displacement-velocity curves" (l. 474 to 475); its axis reads "Travel distance (m)" in Fig. 5a and "Travel Displacement (m)" in Fig. 5b to 5f. (c) The monitored units are called "monitoring points" (l. 256), "ID" (Table 2), "point 1" (Fig. 9 caption) and "Block 1" (l. 397). (d) The zones are called "lower, lower-middle, upper-middle, and upper portions" (l. 256 to 257) and "bottom", "lower middle part", "upper middle part" and "top" (Table 2). (e) The river is called "Dadu River" in the text, "Daduhe River" in the legend of Fig. 2b and "Dadu river" in Fig. 3. In each case the names denote the same object. |
| Suggestion | Fix one term per object at its definition (Eqs. 5 and 6 for VS, AG and the area symbol, Sect. 2.2 for the curve, Table 2 for block IDs and zones) and use it in the abstract, text, captions and figure labels. |
| Status | verified |
| Severity | minor |
| Source | S2 |

**GB-16 Fig. 6 labels the two middle zones in reverse order**

| Field | Content |
|---|---|
| Check | P3 |
| Location | Fig. 6 (p. 14); Table 2 (p. 13) |
| Quotation | "Fig6. Location of 10 monitoring points" |
| Concern | From the rear to the front of the mass, Fig. 6 labels the zones "Top", "Lower middle part", "Upper middle part" and "Bottom". In Table 2 the upper middle points (6 to 8) lie at z = 660 to 692 and the lower middle points (3 to 5) at z = 465 to 498, so the zone below "Top" must be the upper middle part. The figure shows 2, 3, 3 and 2 points per zone, as in Table 2. The ten points carry no IDs, so they cannot be matched to Table 2, to Fig. 9 or to the colours of Fig. 10a. |
| Suggestion | Swap the labels "Lower middle part" and "Upper middle part" in Fig. 6 and label each point with its ID from Table 2. |
| Status | verified |
| Severity | minor |
| Source | AB |

**GB-17 The fixed alpha value is said to ensure a tight envelope at all times, without a test**

| Field | Content |
|---|---|
| Check | P26, P31 |
| Location | p. 14, l. 281 to 284; p. 23, l. 426 to 428; Fig. 12 |
| Quotation | "This approach ensures a tight fit of the envelope model while minimizing geometric deviations introduced by parameter tuning." |
| Concern | The unit of α and the point set (block centroids or vertices) are not stated. As the mass spreads, the spacing of the points grows, so one fixed α gives envelopes of different tightness at different times. VS reaches about 1250 % and AG about 4300 % in Fig. 12, and part of this growth may reflect α rather than the mass. The claim that α = 1 "ensures a tight fit" is not tested at any time step. |
| Suggestion | State the unit of α and the point set, and show VS and AG for at least two further α values to demonstrate that the trends in Fig. 12 do not depend on α. |
| Status | verified (missing test and unit); inferred (dependence on α) |
| Severity | moderate |
| Source | SD |

#### Minor corrections

| ID | Location | Quotation | Replacement | Source |
|---|---|---|---|---|
| KK-04 | p. 2, l. 76 | "As shown in Fig1." | "As shown in Fig. 1" (likewise "Fig. n" throughout) | S4 |
| KK-05 | p. 3, l. 77 | "three parts:" | "four parts:" | S3 |
| KK-06 | p. 5, l. 105 | "colluvial Deluvial deposit" | "colluvial-deluvial deposit" | S2 |
| KK-07 | Table 1, row 1, column Rock mass | "bed rock" | "bedrock" | S4 |
| KK-08 | p. 11, l. 218 | "velocities-hereafter" | "velocities, hereafter" | S4 |
| KK-09 | Fig. 5a, legend | "Non-obvios acceleration" | "Non-obvious acceleration" | AB |
| KK-10 | p. 13, l. 246 | "where, at time ti, PE(ti), and DE(ti) can be expressed as:" | "where, at time ti, KE(ti), PE(ti), and DE(ti) can be expressed as:" | S4 |

#### Verification log

| ID | Check | Checked | Values | Result |
|---|---|---|---|---|
| PP-04 | P10 | Design sketch: questions, type, data, time axis, environment, components, disclosed limitations | single-case DEM back-analysis; aims l. 65 to 73, no research questions or hypotheses; one parameter set, one input record, one run of 131 s; no comparison condition; disclosed: no 1786 record (l. 183 to 186), no structural plane data (l. 175 to 178), dam break not modelled (l. 349 to 350); full sketch in instanz_SD.md | basis for GB-04, GB-10 to GB-13, GB-17, GB-18, GB-20, GB-26 to GB-28 |
| PP-05 | P12 | Data sources of Sect. 2 against the data and code statements | UAV DEM and point cloud (l. 130 to 135); restored contours (l. 138 to 143); Luding station record (l. 189 to 191); laboratory data and inversion (l. 207); 3DEC input; block histories; detection code (l. 226 to 234); alpha-shape scripts (l. 272 to 284); photographs (Fig. 7o); public: 0 of 9; reason for restriction: none | finding GB-29 |
| PP-06 | P38 | Identifiers counted across the manuscript | Mogangling landslide, Kangding earthquake (l. 110, l. 183, l. 188), 3DEC (l. 169, l. 196) consistent; KE, PE, DE, ME defined in l. 241 to 243 and used consistently except "dissipation energy" (l. 21, l. 84); Detuo fault and Dadu River fault defined as one object (l. 147) | finding GB-15 for the objects listed there |
| PP-07 | P29 | Inventory of figures | Fig. 1 p. 4, flow chart, cited l. 76; Fig. 2 p. 6, maps (a to c), cited l. 93, l. 160; Fig. 3 p. 8 to 9 (a to c), cited l. 144, l. 159 to 160; Fig. 4 p. 10, cited l. 173; Fig. 5 p. 12 (a to f), cited l. 220, l. 229; Fig. 6 p. 14, cited l. 256; Fig. 7 p. 17 to 19 (a to o), cited l. 301 to 353; Fig. 8 p. 20, cited l. 375; Fig. 9 p. 21 to 22 (a to j), cited l. 393; Fig. 10 p. 23, cited l. 414; Fig. 11 p. 23 to 24 (a to j), cited l. 428; Fig. 12 p. 25, cited l. 443; no graphical abstract, no appendix | every figure cited in its section |
| PP-08 | P3 | Scale and extent of the landslide in Fig. 2c, 300 dpi render | scale bar 0 m at 1559.5 px, 600 m at 1833.0 px (2.194 m/px); boundary length along 75° 1237 m, width 1018 m, enclosed area 0.99 km2 | used in GB-07 |
| PP-09 | P3 | Marked peaks per threshold in Fig. 5b to 5f (main panel and inset) | 164, 130, 102, 89, 64 for 10 %, 20 %, 30 %, 40 %, 50 %; Fig. 5d main panel 71, inset 31; touching markers counted as one | decrease with threshold as described in l. 229 to 232; no finding |
| PP-10 | P1 | Elevations of the slope description | toe 1120 m, front edge 1120 to 1330 m, platform 1330 to 1380 m, rear wall 1380 to 1890 m, ridge about 2000 m (l. 151 to 156); segments contiguous; model mass height 747 m and 131 m above the river (l. 174 to 175) | no finding for the elevations |
| PP-11 | P22 | Block dimensions derivable from Table 2 | footprint 8.7 m × 8.7 m = 75.69 m2; volumes 756.2 to 1754.3 m3 give heights of 10.0 to 23.2 m; number of blocks in the sliding mass not stated (25345 refers to the whole model, l. 181) | no separate finding |
| PP-12 | P7, P30, P37 | Method versions, corrections, revised data | none stated | no finding |
| PP-13 | P17 | Place of the disclosed limitations | proxy record and missing structural plane data disclosed in Sect. 2.1 where introduced; dam break disclosed in Sect. 3.1 and not a method of the study | no finding |
| PP-14 | P25 | Feasibility of the processing chain | DEM to model, record to input, block histories to energies: each step uses information available at that point | no finding |

### Segment 3: Results (p. 15 to 25, l. 297 to 459)

#### Substantive findings

**GB-18 The validation is qualitative and rests on one run, but is called compelling**

| Field | Content |
|---|---|
| Check | P10, P9, P15 |
| Location | p. 16, l. 353 to 359; Fig. 7o; p. 13, l. 265 to 266; p. 11, l. 206 to 207; p. 25, l. 471 to 472 |
| Quotation | "Fig7. (o) presents compelling evidence of agreement between the numerical simulation results and the actual field observations." |
| Concern | Fig. 7o compares two features by eye, a protruding ridge in the source area and the extent of the deposit; no runout distance, deposit area, thickness or dam height is compared numerically. The design has one parameter set (Table 1), one input motion and one run. Field-investigation findings are announced (l. 65, l. 265 to 266) but not reported beyond the two photographs, and the "parameter inversion" (l. 207) names no observable. Conclusion 2 nonetheless says the comparison "ensures that the simulation outcomes align with actual conditions" (l. 471 to 472), and the title and l. 39 to 41 generalise from this one case to earthquake-induced high-level landslides. Without a quantitative target and without varying friction, damping and input motion, the design cannot show that the simulated sequence is the one that occurred rather than one of several that produce a similar deposit. |
| Suggestion | Alternative design: derive quantitative targets from the restored and present terrain (deposit area and outline, runout to the opposite bank, deposit thickness from the elevation difference, dam height), calibrate against them, and report a sensitivity set (friction angles of Table 1, damping, scaling of the input motion) with the resulting spread of runout and energies. Until then, replace "compelling evidence" and "ensures" with "is consistent with". |
| Status | verified |
| Severity | major |
| Source | SD, S4 |

**GB-19 Fig. 7h shows zero stress at t = 0 s, although the dynamic run starts from static equilibrium**

| Field | Content |
|---|---|
| Check | P3 |
| Location | Fig. 7h (p. 18); p. 10, l. 199 to 202 |
| Quotation | "Dynamic loading must be introduced only after the model has attained static equilibrium" |
| Concern | Fig. 7h (t = 0 s) is uniformly red, with a colour bar from "0" to "0Mpa". Fig. 7i (t = 3 s) shows stresses down to minus 33 MPa, close to the lithostatic value ρgh = 2700 × 9.81 × 1121 = 29.7 MPa at the model base. A model in static equilibrium would show this gradient already at t = 0 s. Does Fig. 7h show the state before gravity was applied, or is the plot range set to zero? |
| Suggestion | Replace Fig. 7h with the stress field after static equilibrium, or state in the caption what t = 0 s denotes. |
| Status | verified (figure); inferred (interpretation) |
| Severity | moderate |
| Source | AB |

**GB-20 Conservation and non-conservation of energy are both fixed by the definition of DE**

| Field | Content |
|---|---|
| Check | P31, P15, P3 |
| Location | p. 19, l. 375 to 377; l. 388 to 389; p. 13, l. 249 to 252; p. 20, l. 393 to 394; l. 399 to 400; Fig. 8; Fig. 9; p. 1, l. 26 to 28; p. 25, l. 476 to 479; p. 26, l. 480 to 482 |
| Quotation | "It is evident that, due to the law of energy conservation, the total sum of the three forms of energy remains constant throughout the landslide." |
| Concern | Eq. (4) defines DE(ti) as ME(t0) minus ME(ti), and Eq. (1) defines ME as KE + PE. Hence KE + PE + DE = ME(t0) at every time for any input. The constant total in Fig. 8 (measured at 6507 GJ in all columns) only restates this identity, as do l. 375 to 377, "This can be regarded as a successful energy extraction numerical simulation" (l. 388 to 389), the abstract (l. 26 to 27) and conclusion 3 ("the sum of the three energies equals the initial potential energy before sliding", l. 478 to 479); none of them tests conservation. The same identity holds for every block. Fig. 9 shows a constant stacked total in all ten panels (measured 5.06 GJ for point 1, 11.10 GJ for point 5, 1.178 GJ for point 7, 0.947 GJ for point 10), although l. 393 to 394 state that "unlike the total landslide mass, the energy of single blocks is not conserved". What would show dissipation by friction, impacts and damping, or the energy received from neighbours, is not measured. The work of the seismic input and the energy absorbed by the viscous boundaries are not accounted for, although the run is driven by an earthquake record. The manuscript itself attributes decreases of DE to "the calculation method used" (l. 399 to 400). |
| Suggestion | Remove the conservation claim and the contrast between whole mass and single blocks from the abstract, Sect. 3.2 and conclusion 3, or replace them with an independent balance. Alternative design: record in 3DEC the work of gravity and of the seismic input, the frictional and damping dissipation, the strain energy and the boundary absorption, and show that their sum closes; for single blocks, compute the work of the contact forces from neighbours directly. |
| Status | verified |
| Severity | major |
| Source | S4, SD, AB |

**GB-21 The energy magnitudes in Figs. 8 and 12 fit neither stated volume**

| Field | Content |
|---|---|
| Check | P23 |
| Location | Fig. 8 (p. 20); Fig. 12; Fig. 9; p. 9, l. 182; p. 7, l. 151; p. 16, l. 330 |
| Quotation | "Fig8. Evolution of energy during the landslide" |
| Concern | Measured values: total energy in Fig. 8 constant at 6507 GJ; largest KE band 1647 GJ at about 13 s; Fig. 12 labels the KE peak 1116.8 GJ. Calculated with ρ = 2300 kg m-3 (Table 1) and g = 9.81 m s-2. Resolution A, with the model volume of 317563 m3 (l. 182): m = 7.30×10^8 kg. The 6507 GJ then require a mean drop of 6.507×10^12 / (7.30×10^8 × 9.81) = 908 m, more than the entire relief of 747 + 131 = 878 m from the top of the mass to the river (l. 174 to 175). The 1647 GJ require an rms velocity of 67.2 m/s, while the largest velocity in the model is 31.6 m/s (l. 330), which limits KE to 365 GJ. Resolution B, with the field volume of 2.4×10^7 m3 (l. 151): m = 5.52×10^10 kg. The 6507 GJ then correspond to a mean drop of only 12 m, whereas the initial energies of the monitored blocks in Fig. 9 correspond to drops of 238.6 m (point 1), 316.7 m (point 5), 29.8 m (point 7) and 43.4 m (point 10). A volume between 9.1×10^5 and 9.7×10^6 m3 would fit these block drops, and neither stated volume lies in that range. The budget closes under neither resolution. |
| Suggestion | State in Sect. 2.3 the mass, density and reference level used for Figs. 8 and 12, recompute the energies with the volume actually simulated, and give the mean drop of the centre of mass as a check. |
| Status | verified (figure values measured); inferred (case calculation) |
| Severity | major |
| Source | S3, AB |

**GB-22 Several figures use type below 6 pt at print size**

| Field | Content |
|---|---|
| Check | P29 |
| Location | Fig. 9 (p. 21); Fig. 10b; Fig. 11; Fig. 12 |
| Quotation | "Fig11. Comparison of the overall envelope fitting of the landslide at 10 different times" |
| Concern | Digit heights were measured in the 300 dpi render and converted with pt = px × 72 / 300 / 0.72. Fig. 11: axis numbers 7 to 8 px, about 2.5 pt. Fig. 12: axis numbers 10 to 11 px, about 3.5 pt; the annotations "29.47" and "319.5" 9 px, about 3.0 pt. Fig. 9: axis numbers 11 px, about 3.7 pt. Fig. 10b: axis title 16 px, about 5.3 pt. |
| Suggestion | Enlarge the axis numbers, titles and annotations in Figs. 9 to 12 to at least 6 pt at print size. |
| Status | verified |
| Severity | minor |
| Source | AB |

**GB-23 Collision frequency against travel distance is not normalised**

| Field | Content |
|---|---|
| Check | P21 |
| Location | p. 22, l. 418 to 421; Fig. 10b |
| Quotation | "as the migration distance increases during the landslide, the number of collisions also rises continuously, reaching a peak once the blocks enter the river channel" |
| Concern | Fig. 10b gives absolute counts per 100 m bin, rising from about 7 at 500 m to 157 at 2300 m. Two effects could produce this rise without more collisions per block. (a) The number of block records contributing to each bin is not stated, so the bins may differ in sample size. (b) If peaks are detected on a record sampled in time, a slow block yields more samples and more local maxima per metre; the profile in Fig. 5b to 5f falls from about 45 m/s to about 6 m/s, i.e. about seven times more samples per metre near its end. Which effect applies cannot be decided from the manuscript. Could the authors show the trend after normalisation? |
| Suggestion | Report the frequency per block and per metre (or per second), with the number of contributing blocks per bin. Resample velocity at constant distance increments before peak detection, and then restate l. 418 to 421. |
| Status | inferred |
| Severity | major |
| Source | S3 |

**GB-24 The vertical displacements in Fig. 10a do not fit the energy drops in Fig. 9**

| Field | Content |
|---|---|
| Check | P3 |
| Location | Fig. 10a (p. 23); Fig. 9; Table 2 |
| Quotation | "Fig10. (a) movement trails of 10 monitoring points" |
| Concern | In Fig. 10a the trails of point 1 (red) and point 5 (navy) descend to roughly minus 640 m and minus 790 m on the Z axis. These values are estimated after correcting for the oblique X axis, because the 3-D projection cannot be calibrated exactly. The initial energies in Fig. 9 correspond to drops of 238.6 m (point 1) and 316.7 m (point 5), using ρ = 2300 kg m-3 and the volumes in Table 2, and point 1 starts at z = 340 m (Table 2). Do the Z values in Fig. 10a use a different unit or reference, or do Figs. 9 and 10a come from different runs? |
| Suggestion | State the reference point and units of Fig. 10a, and give the start and end elevations of each block in Table 2 or in a supplement. |
| Status | inferred |
| Severity | moderate |
| Source | AB |

**GB-25 Announced outputs are not reported**

| Field | Content |
|---|---|
| Check | P11 |
| Location | p. 24, l. 440 to 441; p. 13, l. 258 to 264; Table 2; p. 3, l. 86 to 87 |
| Quotation | "For the fitted envelope, we first extracted its volume (V) and surface area (A) at each time point" |
| Concern | Announced analyses compared with the results: the envelope volume and area at the 10 times (l. 440 to 441) are not given, nor are V0 and S0. The stress histories Stress-XX, YY and ZZ of each monitored block (Table 2, l. 262 to 264) are not shown. The maximum unbalanced force (ID 11, l. 258 to 259), used "to verify that the model reached post-failure stability", is not shown. The displacement components of each block appear only as trajectories (Fig. 10a). The collision frequency per part of the mass (l. 86 to 87) is not shown, because Fig. 10b plots against travel distance. |
| Suggestion | Add a table of V, A, VS and AG at the 10 times, and show the history of the unbalanced force and the block stress histories in figures or a supplement, or delete these announcements in Sect. 2.3 and Table 2. |
| Status | verified |
| Severity | moderate |
| Source | S3 |

**GB-26 Fragmentation is asserted but not measured**

| Field | Content |
|---|---|
| Check | P31, P15 |
| Location | p. 24, l. 445 to 452; p. 26, l. 488 to 492 |
| Quotation | "In the process of energy transfer, collisions and friction cause block fragmentation and disintegration, producing large amounts of debris." |
| Concern | No result counts blocks, fragments or broken contacts, and the manuscript describes no breakage mechanism. The evidence offered is the growth of envelope volume and area (Fig. 12) and the rise of DE (l. 451 to 452). Both also grow when the mass spreads without breaking. DE is defined as the loss of mechanical energy (Eq. 4) and therefore includes friction and damping. Conclusion 5 ("collisions and friction cause blocks to fracture and disintegrate, generating a large amount of debris", l. 489 to 490) is stronger than the evidence. |
| Suggestion | Report a fragmentation measure from the model (number of separated blocks or broken contacts over time), or reword l. 445 to 452 and conclusion 5 as dispersion of the mass. |
| Status | verified |
| Severity | major |
| Source | S4, SD |

**GB-27 The solid to fluid transition at VS 29.47 % and AG 319.5 % has no criterion, and the KE peak used is not the maximum**

| Field | Content |
|---|---|
| Check | P8, P3 |
| Location | p. 25, l. 453 to 456; Fig. 12; Fig. 8 |
| Quotation | "it can be considered that the landslide transitions from a solid phase to a fluidized phase" |
| Concern | The only criterion given is the KE peak; no kinematic or rheological measure of fluidization (for example a velocity profile with depth, granular temperature, or loss of block contacts) is used. Fig. 12 labels the KE peak 1116.8 GJ. In Fig. 8 the KE band is widest at 13.4 s, with 172 px = 1647 ± 19 GJ (axis 0 GJ at 1430.5 px, 7000 GJ at 699.5 px; ±2 px for both edges). The difference of 530 GJ exceeds the uncertainty, so Fig. 12 is apparently sampled at fewer times than Fig. 8. The KE maximum, and with it the VS and AG values of the transition, then lie elsewhere. |
| Suggestion | Define the transition by a measured quantity, plot Fig. 12 at the time steps of Fig. 8 (or state its sampling times), and determine VS and AG at the transition from the full time series; otherwise remove the threshold values. |
| Status | verified |
| Severity | major |
| Source | SD, AB |

#### Minor corrections

| ID | Location | Quotation | Replacement | Source |
|---|---|---|---|---|
| KK-11 | Fig. 7b to 7n, colour bars | "Mpa" | "MPa" | AB |
| KK-12 | p. 20, l. 397 | "exhibit a rebound in potential energy after it approaches zero" | "exhibit a rebound in potential energy after their potential energy approaches zero" | S4 |
| KK-13 | p. 23, l. 425 | "3.4 Structural evolution as a function of energy change" | "3.3 Structural evolution as a function of energy change" | S4 |
| KK-14 | p. 24, l. 438 | "(a-i) when time = 0s, 3s, 7s, 9s, 12s, 15s,32s,71s,100s," | "(a to j) at t = 0, 3, 7, 9, 12, 15, 32, 71, 100 and" | AB |

#### Verification log

| ID | Check | Checked | Values | Result |
|---|---|---|---|---|
| PP-15 | P2, P3 | Velocities and times of Sect. 3.1 against the colour bars and caption of Fig. 7 | text 5.9, 19.6, 27.1, 31.6, 25.7 m/s and "approached 0 m/s" (l. 307, 315, 322, 330, 339, 347) against colour bars 5.9, 19.6, 27.1, 31.6, 25.7, 0.21 m/s; times 0, 3, 7, 9, 12, 15, 131 s in the caption; duration 131 s (l. 300) | no finding |
| PP-16 | P24 | Timing of stages against the figures | KE maximum in Fig. 8 at 13.4 s (x axis 0 s at 682.5 px, 20 s at 820.5 px) against "Around 13 seconds" (l. 383); Fig. 11 has ten panels for ten times | no finding |
| PP-17 | P3 | Fig. 8 total and KE | top of the stacked bars at 751 px (median over all columns) = 6507 GJ; widest KE band 172 px = 1647 GJ | used in GB-20, GB-21, GB-27 |
| PP-18 | P2 | Monitoring points across text, table and figures | 10 points in l. 256, Table 2 (IDs 1 to 10, ID 11 for the unbalanced force), Fig. 9 (10 panels), Fig. 10a (10 lines); zones with 2, 3, 3, 2 points | no finding |
| PP-19 | P3 | Values in Fig. 10b | 24 visible dots (bins 200 to 2500 m): 3.3, 4.7, 6.0, 7.6, 15.0, 15.9, 6.9, 26.9, 19.9, 24.0, 30.0, 26.9, 37.0, 42.0, 49.0, 49.6, 52.9, 61.0, 69.0, 72.0, 142.0, 157.0, 150.0, 146.0; sum 1214.8; calibration 0 at 1190.5 px, 175 at 704.0 px | used in GB-14, GB-23 |
| PP-20 | P2 | Values of Sect. 3.4 against Fig. 12 and Fig. 11 | 29.47 % and 319.5 % (l. 453 to 454) against the labels 29.47 and 319.5 in Fig. 12a and 12b; 10 time points (l. 427) against ten times in the caption of Fig. 11 | no finding (caption range in KK-14) |
| PP-21 | P29 | Captions of Figs. 2, 5 and 9 name every panel | Fig. 2 (a to c), Fig. 5 (a to f), Fig. 9 (a to j) explained individually | no finding |
| PP-22 | P19 | Provenance of the core statements | all conclusions rest on model output; only Figs. 3 and 7o use primary field data; the manuscript presents the results as numerical | no separate finding |

### Segment 4: Conclusions, statements, references (p. 25 to 29, l. 460 to 605)

#### Substantive findings

**GB-28 Conclusion 4 and the last sentence of the abstract have no corresponding result**

| Field | Content |
|---|---|
| Check | P15, P34 |
| Location | p. 26, l. 483 to 487; p. 1, l. 28 to 30; p. 22, l. 414 to 415; Table 2 |
| Quotation | "during the collapse stage, the front portion of the rock mass experiences more collisions than the rear portion, with a clear trend of decreasing collision frequency toward the rear" |
| Concern | Sect. 3 contains no collision count per position (front, rear, lower, upper) and no count for the collapse stage. Fig. 10b plots frequency against travel distance, although l. 414 to 415 describe it as the frequency "experienced by blocks at different locations". The transfer of energy from rear to front (l. 485 to 487) is not shown in any figure. The abstract (l. 28 to 30) says "lower" and "upper" where conclusion 4 says "front" and "rear", without stating that these are the same. The zone statements rest on two or three blocks per zone (Table 2), called "representative" (l. 257) without a selection rule. The same statements appear in the abstract of Ge et al. (2021), which is listed but not cited. |
| Suggestion | Add a result per zone (collisions per block for bottom, lower middle, upper middle and top within the time window of the collapse stage, and the energy received from neighbours, over all blocks of each zone), or restrict conclusion 4 and l. 28 to 30 to what Fig. 10 shows, and cite Ge et al. (2021) for the earlier finding. |
| Status | verified |
| Severity | major |
| Source | S4, SD |

**GB-29 Data and code are withheld "upon reasonable request" without a reason, and the third-party record has no source**

| Field | Content |
|---|---|
| Check | P12 |
| Location | p. 26, l. 494 to 495; l. 505 to 506; p. 10, l. 189 to 191 |
| Quotation | "The data and materials that support the findings of this study are available from the first author, Yunfeng Ge, upon reasonable request." |
| Concern | The methods name nine data sources (PP-05): the UAV DEM and point cloud, the restored terrain, the Luding station record, laboratory data and the parameter inversion, the 3DEC input, the block time histories behind Figs. 8 to 12, the peak detection code, the alpha-shape scripts and envelope values, and the field photographs. The code and data statements cover all of them only as "available ... upon reasonable request". No item is public and no reason is given, although none of the data concern persons. The Luding station record is third-party data and is neither cited nor attributed to an agency or database. No links are given, so reachability could not be checked. |
| Suggestion | Deposit the restored and present terrain, the 3DEC input files, the block time histories, and the detection and alpha-shape scripts in a public repository and cite it in the statements (l. 494 to 506). Cite the provider and record identifier of the Luding station record in l. 189 to 191, and give a reason for any item that remains restricted. |
| Status | verified |
| Severity | moderate |
| Source | S2 |

**GB-30 Citations and reference list do not match in either direction**

| Field | Content |
|---|---|
| Check | P4 |
| Location | p. 26 to 29, l. 507 to 605; in-text citations of Sect. 1 |
| Quotation | "Reference" |
| Concern | Of 29 citation keys in the text, 13 have no entry: Cook et al. 2021, Cuomo et al. 2021, Helmstetter and Garambois 2010, Huang et al. 2012, Huang et al. 2019, Intrieri et al. 2018, Navarre et al. 2009, Pandey et al. 2021, Shugar et al. 2021, Van Herwijnen and Schweizer 2011, Zhang et al. 2020a, Zhang et al. 2020b, Zhu et al. 2010. Four differ in year from the nearest entry: Tian et al. 2017 (entry 2016), Fan et al. 2020 (Baige entry 2019), Zhang et al. 2024 (Zhang J. entry 2023) and Zhao et al. 2020 (Zhao B. entry 2021). "Fan et al., 2019a" has no counterpart 2019b, while neither of the two Fan 2019 entries carries a letter. Of 31 entries, 16 are never cited: Bernardie et al. 2021, Chang et al. 2022, Chen et al. 2024, Dahal et al. 2022, Gao et al. 2023, Ge et al. 2021, Gong et al. 2024, He J. et al. 2023, He K. et al. 2022, He N. et al. 2023, Nava et al. 2025, Sinčić et al. 2025, Wu J. et al. 2013, Yang et al. 2022, Zhang K. et al. 2019 and Zhou et al. 2024. The uncited entries include the earlier studies of the Mogangling landslide (Wu et al. 2013, Zhou et al. 2024, and Zhao et al. 2021 unless this is meant by "Zhao et al., 2020") and the authors' own energy study (Ge et al. 2021). The heading reads "Reference". |
| Suggestion | Add the 13 missing entries, correct the four years and the letters a and b, cite or delete the 16 uncited entries, cite the Mogangling studies and Ge et al. (2021) where the contribution is set apart, and rename the heading "References". |
| Status | verified |
| Severity | moderate |
| Source | S4 |

#### Minor corrections

| ID | Location | Quotation | Replacement | Source |
|---|---|---|---|---|

#### Verification log

| ID | Check | Checked | Values | Result |
|---|---|---|---|---|
| PP-23 | P4 | Numbering and targets of figures, tables, equations and sections | Figs. 1 to 12 continuous and each cited in its section (l. 76, 93, 144, 173, 220, 256, 301, 375, 393, 414, 428, 443); Tables 1 and 2 cited (l. 212, l. 259); Eqs. 1 to 6 continuous; sections 1, 2.1 to 2.4, 3.1, 3.2.1, 3.2.2, 3.4, 4 (3.3 missing) | KK-13 for the section number; GB-08 for b-b' |
| PP-24 | P15 | Conclusions mapped to results | C1 (contour restoration) to Sect. 2.1 and Fig. 3: supported as a description of the method; C2 (simulation, validation, peak extraction) to Fig. 7o and Fig. 5: GB-18, GB-13; C3 to Figs. 8 and 9: GB-20; C4: GB-28; C5 to Figs. 11 and 12: GB-26; the manuscript has no outlook or proposals for future studies | findings as listed |
| PP-25 | P16 | Uniformity of the reference list | author format with surname and initials consistent; one entry shortened with "et al." (l. 530); DOIs given for all 31 entries; the Cheng entry lists "Yu-Sheng, L." as second author | no separate finding (checking the citation style is an optional area) |
| PP-26 | P32, P33, P36 | Claims of error-free results, statements of effort, statements from recollection | none found | no finding |
| PP-27 | P18, P9 | Principles recommended to others; proposed future studies | none stated; no outlook section | no finding |

## Optional checks

| Area | What it needs | Responsible | Run |
|---|---|---|---|
| DOI resolution | one fetch per reference entry with a DOI | `science-quellenapparat-pruefung` | no |
| Citation style | the name of the style | `science-zitierstil-harvard-ctr` or the style rules of the journal | no |
| AI statement against publisher policy | the AI policy of the target publisher | this review, on request | no |
| Relation to the authors' earlier work | the earlier work of the authors | this review, on request | no |
| Journal requirements | the author guidelines of the target journal | this review, on request | no |
| Scientific accuracy | access to the sources of the checked statements and a selection of sections | `science-faktenbeleg-pruefung`, `geo-frage-belegbasiert-klaeren` | no |

## Limits of this review

- Checked version: egusphere-2025-4506.pdf, 29 pages, SHA-256 64cb3787456244aa6102e34f776b47e9a612d06e8894d391758ae240dbe415d6.
- Unreadable sources: Wu et al. 2024 (Eng. Geol., 331, 107429; publisher page not reachable); EPFL repository records on momentum transfer in rock avalanches (empty or blocked). Ge et al. 2021, Carpignano et al. 2009, Song et al. 2017, Jaboyedoff et al. 2019 and Zhao et al. 2017 were read as abstracts only.
- Findings with status assumption: 0 of 30 as central statement; 2 of 30 contain a sub-statement with status assumption (GB-11, GB-12).
- Optional checks run: 0 of 6.
- Omitted instances: none.
- Discarded findings: 0.
- The six review instances ran sequentially in one context, not as separate agents.
- All figures are raster images; values were measured on 300 dpi renders. The 3-D views (Figs. 4, 6, 7, 10a, 11) cannot be calibrated, so statements about them carry the status inferred.
