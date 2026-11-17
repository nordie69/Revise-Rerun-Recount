# Review report: Energy and structural evolution process of high-altitude and long-runout landslides induced by a strong earthquake

| Field | Value |
|---|---|
| Manuscript | Ge, Y., Hu, B., Tang, H., Fu, X., and Zhu, L., 2025, Energy and structural evolution process of high-altitude and long-runout landslides induced by a strong earthquake, EGUsphere preprint, https://doi.org/10.5194/egusphere-2025-4506 |
| Checked version | egusphere-2025-4506.pdf, 29 pages, SHA-256 64cb3787456244aa6102e34f776b47e9a612d06e8894d391758ae240dbe415d6 |
| Date | 2026-10-17 |
| Language | English |
| Review instances | Segments 1 to 4, figures (AB), study design (SD); the six instances ran one after another in a single context, not context-separated; no instance omitted |

## Summary

The manuscript is a single-case numerical back-analysis of the Mogangling rock landslide on the Dadu River, triggered by the 1786 Kangding (Moxi) earthquake. The pre-failure surface is reconstructed from a UAV DEM by straightening contour lines across the slide; a 3DEC discrete-element model (25345 blocks, Mohr-Coulomb, two rock-mass parameter sets in Table 1) is driven by the acceleration record of the Luding station from the 2008 Wenchuan earthquake. The run lasts 131 s with maximum snapshot velocities of 5.9 to 31.6 m/s. Kinetic, potential and dissipated energy are computed for the whole mass (Fig. 8, about 6500 GJ) and for ten monitored blocks (Fig. 9); effective collisions are picked as velocity peaks with a 30 % prominence threshold (1,139 collisions); alpha-shape envelopes give volume swelling and area growth, with the kinetic-energy peak at VS = 29.47 % and AG = 319.5 %. The manuscript concludes that energy is conserved for the whole mass but not for single blocks and that the lower or front part of the mass collides more often and travels farther.

## Strengths

1. The pre-failure geometry is built from a site DEM by a documented contour modification, and Fig. 3 shows the contours and surfaces before and after the modification with consistent scale bars, so a reader can see where the model surface departs from the present slope (PP-08).
2. Ten monitoring blocks are chosen by a stated rule, two or three in each of four height zones, and all ten are reported in the energy panels and trajectory plots, so the block-level results are not a selected subset (PP-10, PP-18).
3. The collision threshold is shown at five levels, and the number of marked peaks falls steadily from 10 % to 50 %, so the reader can see how the choice of 30 % changes the detected set (PP-09).
4. The stage description of Section 3.1 is tied to Fig. 7 by maximum velocities and times that agree exactly with the colour bars and the caption, and the disclosed limits stand where the methods are introduced (PP-15, PP-16, PP-11).

## Weaknesses

1. The energy results do not yet carry the conclusions drawn from them: conservation of the whole mass follows from the definition of DE, the energy magnitudes cannot be reconciled with the stated volume, density and maximum velocity, and the potential-energy datum differs from the stated one. Compute DE independently with the seismic work included, and recompute Fig. 8, 9 and 12 from the stated model mass (GB-14, GB-21, GB-15).
2. The mechanistic reading of the simulation is not tested against the model or the field: the failure mechanisms of Section 3.1 are not model outputs, validation rests on visual comparison with two photographs, and fragmentation and fluidization are asserted without a mechanism or criterion. Report the model quantities behind each mechanism and add a quantitative comparison with the DEM-derived deposit (GB-18, GB-19, GB-26, GB-27).
3. The headline statement on collisions by position in the mass has no result behind it, and the collision count has no stated basis. Add per-block and per-zone collision counts and energy received, and state what the 1,139 collisions count (GB-23, GB-12, GB-03).
4. Several moderate points limit reproducibility: inconsistent volumes and dimensions, unspecified input motion and model parameters, judgement-based thresholds without sensitivity runs, unreported stress and stability checks, data on request only, and citations that do not support their statements or have no entry. Specify the model in a table, add sensitivity runs, deposit data and code, and repair the citations (GB-06, GB-09, GB-11, GB-16, GB-29, GB-01, GB-30).

## Findings by segment

### Segment 1: Abstract, introduction (p. 1 to 2)

#### Substantive findings

**GB-01 Three cited works do not support the statements they are cited for**

| Field | Content |
|---|---|
| Check | P13 |
| Location | p. 1, l. 33 to 34; p. 2, l. 43 to 46; p. 2, l. 47 to 49 |
| Quotation | "In recent years, the chain disasters of high-level rock landslides in high-intensity earthquake areas have shown a trend of frequent occurrence (Carpignano et al., 2009; Fan et al., 2019a)" |
| Concern | The introduction places the study in a well chosen set of earthquake-landslide cases, but three citations do not carry their sentences. Carpignano et al. (2009) develops a multi-risk mapping framework for the Piedmont Region, Italy (abstract read); it says nothing about earthquake-triggered rock-landslide chains or their frequency. Song et al. (2017), cited in l. 43 to 46 for photos, field surveys, UAV imagery and GIS geomorphic maps, is a 3-D numerical deformation model of a Three Gorges reservoir landslide checked against GPS (abstract read); Wu et al. (2024), cited in the same group, is by its title a numerical simulation of landslide-induced waves. Li et al. (2024), cited in l. 47 to 49 for two-dimensional simulations "involving terrain restoration" with "inputting external stress", models the rainfall-triggered Zhongbao landslide with GeoStudio seepage and limit-equilibrium analyses and restores no terrain (full text read). |
| Suggestion | Replace each of these citations in l. 33 to 34, l. 43 to 46 and l. 47 to 49 by a work that makes the stated point, or delete it; check the remaining citations of the introduction against their sources. |
| Status | verified (Carpignano et al. 2009, Song et al. 2017, Li et al. 2024 at the source); inferred (Wu et al. 2024, title only) |
| Severity | moderate |
| Source | S1 |

**GB-02 Novelty and gap claims rest on no stated search and are contradicted by works the reference list already contains**

| Field | Content |
|---|---|
| Check | P28, P14 |
| Location | p. 2, l. 42; p. 2, l. 49 to 51; p. 2, l. 63 to 64 |
| Quotation | "This paper uses the method of restoring the continuity of contour lines to establish the terrain data before a landslide, which can provide a new idea of terrain restoration before a landslide for the same type of research." |
| Concern | No databases, search terms or dates are given for the claims in l. 42, l. 49 to 51 and l. 63 to 64 ("they still lack a quantitative and systematic study of this topic, especially on energy evolution during the collision"). Restoring a pre-landslide surface by joining the contours on both sides of a landslide and interpolating a new DEM is published, for example by Guimpier et al. (2021), who connect contours across the landslide boundary using "the overall topography outside the landslide". On energy evolution, the reference list contains Ge, Tang and Li (2021), "Mechanical energy evolution in the propagation of rock avalanches using field survey and numerical simulation", by the first author, which the text never cites; Zhao et al. (2021), Wu et al. (2013) and Zhou et al. (2024), all on the Mogangling landslide itself, are listed but not cited either (see GB-30). The contribution is not delimited against this prior work. |
| Suggestion | Replace l. 49 to 51 and l. 63 to 64 by a delimitation against Ge et al. (2021), Zhao et al. (2021), Wu et al. (2013) and Zhou et al. (2024) that says what this study adds, and cite a contour-based reconstruction such as: Guimpier, A., Conway, S., Pajola, M., Lucchetti, A., Simioni, E., Re, C., Mangold, N., Thomas, N., Cremonese, G., and the CaSSIS team: Pre-landslide topographic reconstruction using a Digital Elevation Model from CaSSIS onboard the Trace Gas Orbiter, EGU General Assembly 2021, EGU21-4803, https://meetingorganizer.copernicus.org/EGU21/EGU21-4803.html, 2021. Alternatively state the search on which the gap claim rests. |
| Status | verified (claims and missing search; Guimpier et al. 2021 abstract read); inferred (content of Ge et al. 2021 beyond its title) |
| Severity | moderate |
| Source | S1 |

**GB-03 Several stated aims have no analysis and no conclusion**

| Field | Content |
|---|---|
| Check | P10 |
| Location | p. 2, l. 65 to 73; p. 2, l. 61 to 64; p. 5, l. 122 to 125 |
| Quotation | "On this basis, it focuses on revealing the mechanisms of energy accumulation, transfer, and dissipation during the landslide event." |
| Concern | Energy transfer and dissipation are analysed (Fig. 8, 9, 12). "energy accumulation" is analysed nowhere; "early warning and risk mitigation" (l. 72) and the evaluation basis "for the potential landslide in the high-intensity area of the Dadu River" (l. 124) appear in no result or conclusion; the gap of l. 63 to 64, energy evolution "during the collision", is answered by collision counts (Fig. 10b) and not by the energy exchanged per collision. The manuscript states aims but no research questions, so the reader cannot tell which analysis answers which aim. |
| Suggestion | Add research questions that match the analyses; either add an analysis of the energy exchanged per effective collision and a paragraph on hazard implications, or narrow the aims in l. 65 to 73 and l. 122 to 125. |
| Status | verified |
| Severity | moderate |
| Source | SD, S4 |

#### Minor corrections

| ID | Location | Quotation | Replacement | Source |
|---|---|---|---|---|
| KK-01 | p. 1, l. 21 | "610041 ,China" | "610041, China" | S4 |
| KK-02 | p. 1, l. 34 | "donghekou" | "Donghekou" | S1 |
| KK-03 | p. 2, l. 44 | "UAV impact" | "UAV imagery" | S1 |

#### Verification log

| ID | Check | Checked | Values | Result |
|---|---|---|---|---|
| PP-01 | P13 | Sentences with numbers, rankings or evaluations from cited works | 9 citation groups, all in l. 34 to 63; no numbers taken from literature; uncited numerical statements elsewhere ("nearly 20 large and super large earthquake landslides", l. 99 to 100; "after 9 days", "tens of thousands", l. 110 to 112) belong to the optional check of factual accuracy | no finding |
| PP-02 | P13 | Hu et al. 2017, Sun et al. 2011, Wang et al. 2014, Fan et al. 2019 (Rev. Geophys.) against their sentences, by the titles in the reference list | Ludian 2014 landslides; Donghekou rockslide-debris flow; Donghekou large landslide; earthquake-induced hazard chains | no finding |
| PP-03 | P14 | WebSearch queries: "Mogangling landslide 1786 numerical simulation runout dynamic process"; "reconstruction of pre-landslide topography from contour lines interpolation ancient landslide DEM numerical simulation"; "rock avalanche energy dissipation kinetic potential energy evolution discrete element simulation earthquake-induced landslide open access" | candidates: Zhou et al. 2024 (in list), Guimpier et al. 2021 (not in list, used in GB-02), Garcia et al. 2017 (single-boulder rebound dissipation, same field only, discarded); results on the preprint's own discussion pages and on later versions not opened | no further finding |

### Segment 2: Material, methods (p. 2 to 15)

#### Substantive findings

**GB-04 Does the location dot in Fig. 2a sit about one degree west of the stated coordinates?**

| Field | Content |
|---|---|
| Check | P3 |
| Location | p. 5, l. 95 to 96; Fig. 2a, p. 6 |
| Quotation | "The coordinates of the landslide center are: 29 ° 37 ′ 30.726 ″ north latitude, 102 ° 09 ′ 41.190 ″ east longitude." |
| Concern | The map frame of Fig. 2a has no tick marks, so the degree labels are the only reference. With the centres of the labels 100°E and 102°E (745 and 888 px) and 31°N and 29°N (880 and 1035 px, page rendered at 300 dpi), the dot centre (821.7, 980.3 px) lies at about 101.1°E, 29.7°N, about 1.1° west of 102.16°E. The scale bar (145 px for 160 km, 0.91 px/km) also differs from the latitude labels (155 px for 2°, about 0.70 px/km). Both readings rest on label centres and may be off by a few pixels. |
| Suggestion | Please check the position of the dot and the scale bar in Fig. 2a and add graticule ticks to the frame. |
| Status | inferred |
| Severity | minor |
| Source | AB |

**GB-05 Lithological units carry different names and symbols in the text and in Fig. 2c, 3 and 4**

| Field | Content |
|---|---|
| Check | P38 |
| Location | p. 5, l. 101 to 105; Fig. 2c, p. 6; Fig. 3a and 3b, p. 8; Fig. 4, p. 10; p. 11, l. 207 to 209 |
| Quotation | "The sand slate of the Triassic Baiguowan formation (T3bg) is exposed on the left bank of the Dadu River." |
| Concern | Q4del is "landslide accumulation" in l. 104 and "Rubble soil" in the legend of Fig. 2c; Q4col+dl is "colluvial Deluvial deposit" in l. 105, "Massive gravel" in Fig. 2c and "Massive gravelly soils" in Fig. 3a and 3b, where Fig. 3b lists "Massive gravel" as a further unit. The left bank is T3bg sand slate in l. 103 to 104 but γM2 "Hybrid granite" in Fig. 2c, which shows no T3bg. Quartz diorite occurs "on the western slope" in l. 102 to 103 and is absent from Fig. 2c, yet "Diorite" underlies the whole section in Fig. 3b. The granite is subdivided into strongly and moderately weathered zones in l. 207 to 209, which neither the figures nor Table 1 show. Whether these are the same units under different names cannot be decided from the manuscript. |
| Suggestion | Use one name and one symbol per unit in l. 101 to 105 (with "colluvial and deluvial deposit" for "colluvial Deluvial deposit"), in the legends of Fig. 2c, 3a, 3b and 4 and in Table 1, and state which units form the left bank and the slope. |
| Status | verified (legends at the page images) |
| Severity | minor |
| Source | S2 |

**GB-06 The stated dimensions and volumes of the landslide do not fit together**

| Field | Content |
|---|---|
| Check | P2, P23 |
| Location | p. 7, l. 149 to 156; p. 9, l. 174; p. 9, l. 178 to 182; Table 2, p. 13 |
| Quotation | "The whole model contains 25345 blocks, 2788 m long, 3341 m wide, 1121m high, and the volume of the landslide is 317563 m3." |
| Concern | The field description gives "about 450 m long, about 1000 m wide along the river, and a planar area of 0.45 km2", "average thickness of the landslide mass is about 100 m" and "the volume is about 2400×104 m3" (l. 149 to 151). (1) 0.45 km2 × 100 m = 4.5 × 10^7 m3, 1.875 times 2.4 × 10^7 m3. (2) 2.4 × 10^7 / 317563 = 75.6. (3) 317563 m3 over 0.45 km2 is a mean thickness of 0.71 m. (4) Block columns are 8.7 m × 8.7 m with the full height from surface to sliding bed (l. 178 to 179); the Table 2 volumes of 756.2 to 1754.3 m3 give heights of 10.0 to 23.2 m, not about 100 m. (5) The elevation bands and slopes of l. 152 to 156 add up to a horizontal length of 914 to 1250 m (176 m at 50°, 235 to 572 m at 12° to 5°, 314 m at 35°, 188 m at 57°), which fits the 1021 m of l. 174 but not 450 m. Resolutions: A, the simulated mass is 317563 m3, 1.3 % of the field volume and about 0.7 m thick; B, the model holds about 25345 blocks of the Table 2 mean of 1151.3 m3, 2.9 × 10^7 m3, close to 2.4 × 10^7 m3, and 317563 m3 is a typing error; C, 450 m is the width of part of the slide. The manuscript does not say which applies. |
| Suggestion | Give in l. 149 to 151 the length, width, area, thickness and volume of the field landslide with their source, and in l. 181 to 182 the volume and number of blocks of the simulated sliding mass; explain any difference. |
| Status | verified (values); inferred (ratios and resolutions, computed with Python) |
| Severity | moderate |
| Source | S3 |

**GB-07 Section b-b' is referred to but drawn nowhere, and the section results are referred to the plan-view panel**

| Field | Content |
|---|---|
| Check | P4, P3 |
| Location | p. 7, l. 159 to 160; Fig. 2c, p. 6; Fig. 3b and 3c, p. 8 to 9 |
| Quotation | "As shown in Fig3. (b), make a section along a-a'and b-b' in Fig2. (c). The results are shown in Fig3. (c)." |
| Concern | Fig. 2c shows only section line a-a'; Fig. 3b is labelled "(a-a')"; b-b' appears in no figure. Fig. 3c shows contour maps and shaded surfaces before and after repair, not sections. |
| Suggestion | Draw b-b' in Fig. 2c and add its profile to Fig. 3b, or delete "and b-b'" in l. 160; refer the comparison of restored and present surface to the panel that shows it. |
| Status | verified (page images 6, 8, 9) |
| Severity | minor |
| Source | S4, AB |

**GB-08 In Fig. 3b the water level lies about 57 m above the river level of the text, and the axes have no quantity or unit**

| Field | Content |
|---|---|
| Check | P3, P29 |
| Location | Fig. 3b, p. 8; p. 7, l. 151 to 152 |
| Quotation | "The elevation of the slope toe is 1120 m (about 5 m higher than the river surface)" |
| Concern | Measured at 300 dpi: water surface at 2313 px, ticks 1000 at 2406 px and 2000 at 1864 px, elevation 1172 ± 4 m; the text implies a river surface of about 1115 m. Neither axis of Fig. 3b states quantity or unit (0 to 1500; 1000 to 2000). |
| Suggestion | Correct the water level or the elevation axis of Fig. 3b, or the elevations in l. 151 to 152, and label the axes "Distance (m)" and "Elevation (m a.s.l.)". |
| Status | verified (measured) |
| Severity | minor |
| Source | AB |

**GB-09 Input motion and model setup are not specified well enough to rebuild the simulation**

| Field | Content |
|---|---|
| Check | P8, P35 |
| Location | p. 10, l. 183 to 191; Fig. 4, p. 10; p. 10, l. 196 to 203; p. 11, l. 206 to 212; Table 1, p. 11; Table 2, p. 13 |
| Quotation | "Therefore, this study adopts the acceleration records measured at the Luding station during the Wenchuan earthquake as the input ground motion for the dynamic numerical simulation analysis of the Mogangling landslide." |
| Concern | The boundary conditions are described carefully (l. 193 to 202). Not given: which components of the Luding record, its scaling, PGA, duration, filtering and baseline correction, and how acceleration was applied at a viscous base; a source for "Extensive research indicates that the Kangding earthquake is comparable to the 2008 Wenchuan earthquake" (l. 187 to 189); damping, time step, contact law and contact parameters during runout; the 3DEC version. The inset of Fig. 4 has no time values or unit, and tp, tPGA, tf and te are not explained. Table 1 gives two rock-mass sets while Fig. 4 shows four materials (γo2, Qdel, γM2, sliding mass), and the weathered zones of l. 208 to 209 have no parameters; the laboratory tests and the "parameter inversion" of l. 207 are not described. Table 2 coordinates (x from −719 to −68, y from −557 to 286) do not fit the positive axes of Fig. 4 and 6, and no reference frame is given. Question: Table 1 gives a joint shear stiffness of 1500 GPa/m above the normal stiffness of 960 GPa/m; is this intended? |
| Suggestion | Add to Section 2.1 a table of the input motion (record, component, scaling, PGA, duration, processing, application), of all material sets of Fig. 4 with their sources, of contact and damping parameters and of the 3DEC version; describe the inversion; label the time axis of the Fig. 4 inset and explain its symbols; give the coordinate frame of Table 2. |
| Status | verified (omissions, page images 10, 11, 13); assumption (stiffness question) |
| Severity | moderate |
| Source | SD, AB |

**GB-10 The same quantities are named differently across sections and figures**

| Field | Content |
|---|---|
| Check | P38 |
| Location | p. 11, l. 221; p. 1, l. 23; Fig. 5, p. 12; p. 14, l. 275; p. 24, l. 441; Fig. 2b, p. 6 |
| Quotation | "presents a typical velocity-travel-distance curve for an individual block" |
| Concern | The curve used for collision detection is the "displacement velocity curve" (l. 23, l. 474), the "velocity-travel-distance curve" (l. 221) and the "travel-distance versus velocity profile" (l. 234); its axis reads "Travel distance (m)" in Fig. 5a and 10b but "Travel Displacement (m)" in Fig. 5b to 5f. VS and AG are "volume swelling" and "area growth" in l. 275 but "volume expansion rate" and "surface area growth rate" in l. 25 and l. 441. DE is "dissipation energy" in l. 21 and l. 84 and "dissipated energy" in l. 241. The river is "Daduhe River" in the legend of Fig. 2b and "Dadu River" elsewhere. |
| Suggestion | Fix one term per quantity (travel distance; volume swelling VS; area growth AG; dissipated energy; Dadu River) and use it in text, axis titles and legends. |
| Status | verified |
| Severity | minor |
| Source | S2 |

**GB-11 Collision threshold, alpha value and material parameters are set once by judgement, without a sensitivity test**

| Field | Content |
|---|---|
| Check | P8, P9 |
| Location | p. 11, l. 226 to 233; p. 14, l. 281 to 284; p. 25, l. 452 to 454 |
| Quotation | "At a threshold of 30%, however, the identification of effective collisions is deemed acceptable." |
| Concern | Showing the threshold at five levels (Fig. 5b to 5f) is useful, but 30 % is chosen by visual inspection of one profile, and what the 30 % refers to (peak velocity, curve range) is not said. α = 1 is set without unit or convention, although the blocks are 8.7 m wide, and "This approach ensures a tight fit of the envelope model" (l. 283) is not measured. All results come from one run with one parameter set taken from "laboratory testing, empirical analogy, and parameter inversion". The quantitative statements that depend on these choices (1,139 collisions; VS = 29.47 % and AG = 319.5 % as transition point) carry no range. |
| Suggestion | Define the prominence measure, report collision counts for 10 % to 50 % and VS and AG for several α values, and repeat the run with at least the friction angle and the input scaling at two further values; give the transition values as ranges. |
| Status | verified |
| Severity | moderate |
| Source | SD |

**GB-12 The count of 1,139 effective collisions and the frequency of Fig. 10b have no stated basis**

| Field | Content |
|---|---|
| Check | P20 |
| Location | p. 11, l. 232 to 234; Fig. 5d, p. 12; Fig. 10b, p. 23 |
| Quotation | "Under this setting, 1,139 effective collisions were detected from the travel-distance versus velocity profile." |
| Concern | "the travel-distance versus velocity profile" reads as the single block profile of Fig. 5d, which carries far fewer marked peaks (82 red marks counted in panel d including its inset). Whether 1,139 counts one block, the ten monitored blocks or all 25345 blocks is not said. The 26 points of Fig. 10b sum to about 1215 (measured, ±0.36 per point), which is not 1,139 either; "Frequency" in Fig. 10b is not defined (count per 100 m bin? per block? for which blocks?). |
| Suggestion | State in l. 233 which blocks and which time window the 1,139 collisions refer to; define "Frequency" in the caption of Fig. 10b and state how it is binned and summed. |
| Status | verified (text, counts); inferred (sum of Fig. 10b, measured values) |
| Severity | moderate |
| Source | S3, AB |

**GB-13 The block velocity in Fig. 5 exceeds the maximum velocity of the whole model given in Section 3.1**

| Field | Content |
|---|---|
| Check | P3 |
| Location | Fig. 5b to 5f, p. 12; p. 16, l. 330; p. 16, l. 337; Fig. 7e, p. 17 |
| Quotation | "As shown in Fig7. (e) and (l), during the impact-at-base stage, the maximum velocity reached 31.6 m/s." |
| Concern | The curve of Fig. 5d peaks at 45.4 ± 0.2 m/s at about 250 m travel distance (y ticks 0 at 1780.5 px and 50 at 1302 px, 300 dpi, calibration error 1 px; the top pixel may belong to a marker, so the maximum lies between about 45.1 and 45.4 m/s). The text says that "The velocity reached its peak upon arrival at the valley floor" with 31.6 m/s. Resolutions: A, Fig. 5 shows a block of a different run; B, the 45 m/s fell between the snapshots of Fig. 7 (3, 7, 9, 12, 15 s), and 31.6 m/s is not the maximum of the run. |
| Suggestion | Name the block (ID) and the run of Fig. 5 in its caption, and give in Section 3.1 the maximum velocity over the whole run, not only at the snapshot times. |
| Status | verified (measured) |
| Severity | moderate |
| Source | AB |

**GB-14 Energy "conservation" holds by definition of DE, for the whole mass and for every block, and cannot serve as a result or as a check of the simulation**

| Field | Content |
|---|---|
| Check | P31, P6, P3, P15 |
| Location | p. 13, l. 247 to 252; Fig. 8, p. 20; Fig. 9a to 9j, p. 21 to 22; p. 19, l. 375 to 377; p. 19, l. 388 to 389; p. 20, l. 393 to 396; p. 1, l. 26 to 28; p. 25, l. 476 to 479 |
| Quotation | "It is evident that, due to the law of energy conservation, the total sum of the three forms of energy remains constant throughout the landslide." |
| Concern | Eq. 4 defines DE(ti) = ME(t0) − ME(ti); hence KE + PE + DE = ME(t0) at every time, for any body, whatever the simulation does. The figures show exactly this: the median top of the stacked bars, measured column by column, is 6502 GJ in Fig. 8 and 5.062, 5.134, 4.011, 3.565, 11.095, 6.591, 1.178, 4.356, 1.595 and 0.947 GJ in Fig. 9a to 9j (±1 px, ±0.003 to ±0.024 GJ), flat in every panel. The contrast "unlike the total landslide mass, the energy of single blocks is not conserved" (l. 393 to 394) is therefore not shown; what differs for single blocks is only that DE decreases at times (Fig. 9a and 9c after about 80 s). l. 388 to 389 ("This can be regarded as a successful energy extraction numerical simulation"), the abstract and conclusion 3 rest on this identity. The seismic input does work on the slope through the base; in this bookkeeping it appears as negative dissipation and is not shown. Whether the velocities in Eq. 2 include rotation of the blocks is a question to the authors. |
| Suggestion | Delete the conservation claims in l. 375 to 377, l. 388 to 389, l. 393 to 396, the abstract and conclusion 3; compute DE independently (frictional and damping work from the 3DEC energy tracking), report the work done by the seismic boundary, and test ME(t0) + W_seismic = KE + PE + DE; to show non-conservation of single blocks, plot ME(t) = KE + PE without DE. |
| Status | verified (identity from Eq. 4; flat totals measured); assumption (rotational kinetic energy) |
| Severity | major |
| Source | SD, AB, S4 |

**GB-15 The potential-energy datum in Fig. 9 is not the stated one and differs from block to block**

| Field | Content |
|---|---|
| Check | P3, P8 |
| Location | p. 13, l. 252 to 255; Fig. 9a to 9j, p. 21 to 22; Table 2, p. 13; p. 20, l. 397 to 398 |
| Quotation | "the potential-energy calculation uses the model's initial height as the reference datum rather than true sea level" |
| Concern | With the initial height as datum, PE(t0) would be 0 and PE would become negative during descent; Fig. 9 shows PE starting at the totals of GB-14 and falling to about 0. With the Table 1 density of 2300 kg/m3 and the Table 2 volumes, the initial PE corresponds to drops of 238.7, 222.7, 235.1, 163.4, 316.6, 172.6, 29.8, 192.4, 82.5 and 43.4 m (blocks 1 to 10); subtracted from the Table 2 z coordinates these give datum elevations from 101.3 m (block 1) to 711.6 m (block 10). The datum appears to be each block's own lowest or final position, which makes PE of different blocks incomparable and makes "a rebound in potential energy after it approaches zero" (l. 397 to 398) a consequence of that choice. |
| Suggestion | State in l. 252 to 255 the datum actually used for each block and for the whole mass, and use one common datum for all blocks. |
| Status | verified (measured totals); inferred (drops and datum elevations, computed with Python) |
| Severity | moderate |
| Source | AB |

**GB-16 Announced stress histories and the stability check by unbalanced force are not reported**

| Field | Content |
|---|---|
| Check | P11 |
| Location | p. 13, l. 258 to 263; Table 2, p. 13 |
| Quotation | "In addition, the maximum unbalanced force was tracked to verify that the model reached post-failure stability." |
| Concern | Table 2 lists Stress-XX, Stress-YY and Stress-ZZ for all ten blocks and the maximum unbalanced force as ID 11; l. 262 says stress histories "were extracted for each of the ten monitored blocks". No stress history and no unbalanced-force curve appears in Section 3, so neither the static equilibrium before shaking (l. 199 to 201) nor the post-failure stability can be checked. |
| Suggestion | Add the unbalanced-force history of the static and the dynamic stage and the stress histories of the ten blocks to Section 3 or a supplement, or remove them from Table 2. |
| Status | verified |
| Severity | moderate |
| Source | S3 |

**GB-17 Fig. 6 labels the two middle zones in reverse order and does not identify the points**

| Field | Content |
|---|---|
| Check | P3, P29 |
| Location | Fig. 6, p. 14; Table 2, p. 13 |
| Quotation | "Fig6. Location of 10 monitoring points" |
| Concern | The dashed lines divide the mass into four zones holding 2, 3, 3 and 2 points from the crest down (counted at the enlarged section), as in Table 2. The zone next to "Top" is labelled "Lower middle part" and the zone next to "Bottom" "Upper middle part"; by Table 2 the lower middle part (z = 465 to 498) lies below the upper middle part (z = 660 to 692). The points have colours but no IDs, so the panels of Fig. 9 and the trajectories of Fig. 10a cannot be matched to positions. |
| Suggestion | Swap the two zone labels in Fig. 6 and write the IDs 1 to 10 next to the points, in the colours of Fig. 10a. |
| Status | verified |
| Severity | minor |
| Source | AB |

#### Minor corrections

| ID | Location | Quotation | Replacement | Source |
|---|---|---|---|---|
| KK-04 | p. 2, l. 76 to p. 3, l. 77 | "the research method involves three parts" | "the research method involves four parts" | S3 |
| KK-05 | p. 2, l. 76 | "As shown in Fig1., the research method" | "As shown in Fig. 1, the research method" (and "Fig. n" for all figure references) | S4 |
| KK-06 | p. 5, l. 110 to 111 | "burst the Dadu River after 9 days" | "dammed the Dadu River; the dam breached after 9 days" | SD |
| KK-07 | p. 10, l. 193 to 195 | "In the course of a discrete-element simulation-particularly when modeling nominally semi-infinite bodies such as the use of fixed or elastic boundaries in a static analysis will inevitably reflect outbound seismic waves" | "In a discrete-element simulation of a nominally semi-infinite body, fixed or elastic boundaries used in the static analysis would reflect outgoing seismic waves" | S4 |
| KK-08 | p. 11, l. 218 | "velocities-hereafter termed" | "velocities, hereafter termed" | S4 |
| KK-09 | p. 11, l. 228 | "must be chosen-one that quantifies" | "must be chosen, one that quantifies" | S4 |
| KK-10 | p. 12, Fig. 5a legend | "Non-obvios acceleration" | "Non-obvious acceleration" | AB |
| KK-11 | p. 13, l. 246 | "where, at time ti, PE(ti), and DE(ti) can be expressed as:" | "where KE(ti), PE(ti) and DE(ti) at time ti are:" | S4 |
| KK-12 | p. 13, l. 251 | "(m/s);h(ti)" | "(m/s); h(ti)" | S4 |

#### Verification log

| ID | Check | Checked | Values | Result |
|---|---|---|---|---|
| PP-04 | P10, P9 | Design sketch | single-case numerical back-analysis; case Mogangling 1786; no comparison condition, one run, one parameter set, one input record; no research questions or hypotheses; data: UAV DEM, restored surface, Luding 2008 record, Table 1 parameters, simulation output, two photos; no outlook section | basis of GB-03, GB-09, GB-11, GB-14, GB-18, GB-19 |
| PP-05 | P29, P3 | Inventory of figures | 12 figures, numbered in order, all raster images, each referenced in its section (first references l. 76, 93, 144, 173, 220, 256, 301, 375, 393, 414, 428, 443); panels: Fig. 2 a to c, 3 a to c, 5 a to f, 7 a to o, 9 a to j, 10 a, b, 11 a to j, 12 a, b; no graphical abstract | no finding |
| PP-06 | P38 | Names of the landslide, software and model objects | "Mogangling" in all 26 occurrences of the text layer; "3DEC" l. 169, l. 196; "monitoring points" and "blocks" both used for the ten objects, linked by the title of Table 2 | no finding |
| PP-07 | P1 | Planar area | 450 m × 1000 m = 0.45 km2 (l. 149 to 150) | no finding |
| PP-08 | P3 | Scale bars Fig. 3a and 3c | Fig. 3a: 5 segments of 33 to 37 px for "0 400 1000m", 200 m each; Fig. 3c: 0 to 400 m 89 px, 400 to 800 m 90 px, 800 to 1400 m 133 px (ratio 1.49 for 1.5) | no finding |
| PP-09 | P3 | Threshold series Fig. 5b to 5f | red marks counted with messen.py flecken, insets included: 158, 116, 82, 73, 48 for 10, 20, 30, 40, 50 %; decreasing as l. 230 to 232 describe | no finding |
| PP-10 | P34 | Selection of the monitored blocks | rule: 2, 3, 3, 2 blocks in four height zones (l. 256 to 257, Table 2); all 10 reported in Fig. 9 and 10a | no finding |
| PP-11 | P17 | Disclosed limits at the place of the method | structural planes ignored, l. 176 to 178, Section 2.1; no 1786 record, l. 183 to 186, Section 2.1; smoothed restored terrain, l. 160 to 162, Section 2.1; dam break not modelled, l. 348 to 350, Section 3.1 | no finding |
| PP-12 | P7, P30, P37 | Method versions, corrections, revised data | one run, no versions, no reported corrections, no revised values | not applicable, no finding |
| PP-13 | P33 | Effort statements | none | no finding |
| PP-14 | P5, P26, P27, P18 | Own rules, guarantees, untested components, self-application | threshold rule applied as stated (PP-09); no guarantees beyond GB-11 and GB-14; the unchecked restored surface feeds all results (GB-19); no principle demanded of others | no further finding |

### Segment 3: Results (p. 15 to 25)

#### Substantive findings

**GB-18 The failure mechanisms of Section 3.1 are not outputs of the model as described**

| Field | Content |
|---|---|
| Check | P6, P31 |
| Location | p. 15, l. 308 to 313; p. 15, l. 316 to 318; p. 15, l. 323; p. 9, l. 176 to 180 |
| Quotation | "The first-arriving P-waves caused intense vertical dislocation along the steeply dipping structural planes outside the slope." |
| Concern | The manuscript discloses that "the impact of the structural plane on the landslide process has to be ignored in this study" (l. 177 to 178), and the model has one uniform structural plane and an 8.7 m block grid. Section 3.1 nevertheless reports dislocation and "tensile cracking developed along these structural planes", "structural plane control", "seismic wave amplification at higher elevations, the back-slope effect, and dynamic interface stress effects" and an increased "peak ground acceleration of the Mogangling slope". No acceleration at any monitoring point, no amplification factor and no P- or S-wave arrival is reported. The same mechanisms (seismic acceleration amplification, back-slope effects, interface dynamic stress) are the conclusions of Zhou et al. (2024) on the Mogangling landslide (abstract read), which is in the reference list but not cited. The disclosed limit is thus not carried through to the interpretation. |
| Suggestion | Report the model quantities that would show these mechanisms (accelerations at the ten monitoring points against the base input, arrival times, times of crack initiation), or move the statements to a discussion that cites Zhou et al. (2024) and marks them as interpretation not tested by the model. |
| Status | verified |
| Severity | major |
| Source | SD |

**GB-19 The simulation is validated only by visual comparison with two photographs**

| Field | Content |
|---|---|
| Check | P31, P32 |
| Location | p. 16, l. 353 to 359; Fig. 7o, p. 19; p. 25, l. 471 to 472; p. 13, l. 264 to 266 |
| Quotation | "Fig7. (o) presents compelling evidence of agreement between the numerical simulation results and the actual field observations." |
| Concern | The agreement rests on one ridge in the source area and a visually similar deposit extent, without any measure; the two photographs have no date, viewpoint, scale or source. Conclusion 2 states that the comparison "ensures that the simulation outcomes align with actual conditions". The authors hold a DEM of the present surface and a restored pre-failure surface, from which deposit thickness, area, runout and dam height could be compared quantitatively; the restored surface itself is not checked (l. 160 to 162 discloses only that it is smoother). The "field-investigation findings" integrated in l. 265 to 266 are not reported. |
| Suggestion | Add a quantitative comparison (map of simulated against observed deposit thickness from restored surface minus present DEM, footprint overlap, runout length, dam crest height, with errors), report the field findings used, give date, viewpoint and source of the photographs in Fig. 7o, and replace "ensures" in l. 471 by the measured agreement. |
| Status | verified |
| Severity | major |
| Source | SD, S4, AB |

**GB-20 Fig. 7h shows zero stress at t = 0 s, and the stress panels do not say which stress or which axes**

| Field | Content |
|---|---|
| Check | P3, P29 |
| Location | Fig. 7h to 7n, p. 18; p. 10, l. 199 to 201; p. 15, l. 301 to 302 |
| Quotation | "Fig7 illustrates the cloud maps of velocity distribution for the overall model and stress distribution along the sliding plane" |
| Concern | Fig. 7h (t = 0 s) is uniformly red with the colour bar running from 0 to "0Mpa"; Fig. 7i (t = 3 s) already shows a gradient to "-33Mpa" at the base, the order of the lithostatic stress (2700 kg/m3 × 9.81 m/s² × 1250 m = 33 MPa). If the dynamic run starts from static equilibrium (l. 199 to 201), t = 0 s should show the same gravitational stress. The panels name no stress component, their axes (0 to 2700, 0 to 1200) have no quantity or unit, and they show vertical sections, not the sliding plane named in l. 302. The unit is printed "Mpa". |
| Suggestion | Replace Fig. 7h by the equilibrium state, name the stress component and the section in the caption, label both axes with quantity and unit, and write "MPa". |
| Status | verified (page image); inferred (lithostatic estimate) |
| Severity | minor |
| Source | AB, S4 |

**GB-21 The energy magnitudes disagree between Fig. 8 and Fig. 12 and cannot belong to a sliding mass of 317563 m3 or of 2.4 × 10^7 m3**

| Field | Content |
|---|---|
| Check | P2, P3, P23 |
| Location | Fig. 8, p. 20; Fig. 12, p. 25; Fig. 9, p. 21 to 22; p. 9, l. 182; p. 16, l. 330; Table 1, p. 11 |
| Quotation | "Fig8. Evolution of energy during the landslide" |
| Concern | Measured in Fig. 8 (y ticks 0 GJ at 1430.5 px, 6000 GJ at 803.5 px, 300 dpi): total 6502 ± 10 GJ; KE 1569 GJ at 12.4 s, 1655 ± 20 GJ at 13.6 s, 794 GJ at 14.8 s. Fig. 12 labels the KE peak of the same "sliding mass" "1116.8"; even the Fig. 8 bar at 12.4 s exceeds it by 452 GJ. With 317563 m3 (l. 182) and 2300 kg/m3 (Table 1), M = 7.30 × 10^8 kg: 6502 GJ needs a mean drop of 907 m, more than the 747 m + 131 m = 878 m from the top of the mass to the river (Fig. 4); KE can be at most 0.5 × M × 31.6² = 365 GJ if every block moved at the maximum velocity of l. 330, but Fig. 8 shows 1655 GJ and Fig. 12 1116.8 GJ. With 2.4 × 10^7 m3 (M = 5.52 × 10^10 kg), 6502 GJ means a mean drop of 12 m. The ten blocks of Fig. 9 carry 43.5 GJ for 11512.7 m3 (3.78 MJ/m3); scaled, 317563 m3 would carry 1201 GJ and 2.4 × 10^7 m3 about 90750 GJ. A KE of 1655 GJ at 31.6 m/s needs at least 3.3 × 10^9 kg, that is 1.44 × 10^6 m3. No stated volume reproduces the energies, so it is open which mass the energy series describe. |
| Suggestion | State the mass and density used for each energy series, recompute Fig. 8, 9 and 12 from one time series of the stated model or correct the stated volume, and add the check that the summed KE stays below 0.5 M v² with the maximum velocity of the run. |
| Status | verified (values measured or printed); inferred (masses and bounds, computed with Python) |
| Severity | major |
| Source | S3, AB |

**GB-22 Axis and tick labels in Fig. 9 and Fig. 11 are below 6 pt**

| Field | Content |
|---|---|
| Check | P29 |
| Location | Fig. 9, p. 21 to 22; Fig. 11, p. 23 to 24 |
| Quotation | "Fig11. Comparison of the overall envelope fitting of the landslide at 10 different times and the shape of the landslide mass in numerical simulation" |
| Concern | Digit height measured at 600 dpi, converted with pt = px × 72 / 600 / 0.72: Fig. 9a time-axis numbers 32 px, 5.3 pt; Fig. 11a axis numbers 16 to 17 px, 2.7 to 2.8 pt. |
| Suggestion | Enlarge tick and axis labels of Fig. 9 and Fig. 11 to at least 6 pt at print size. |
| Status | verified (measured) |
| Severity | minor |
| Source | AB |

**GB-23 The announced analysis of collision frequency by position in the mass is not reported, yet the abstract and conclusion 4 rest on it**

| Field | Content |
|---|---|
| Check | P11, P15 |
| Location | p. 22, l. 414 to 421; p. 3, l. 85 to 87; p. 1, l. 28 to 30; p. 26, l. 483 to 487 |
| Quotation | "Fig10. (a) shows the trajectories of the 10 monitored blocks, while Fig10. (b) presents the frequency of effective collisions experienced by blocks at different locations during the landslide process." |
| Concern | The methods announce that "the influence of effective collision frequency of different parts of landslide mass on energy transfer is analyzed" (l. 86 to 87), and Table 2 assigns the blocks to four parts. Section 3 gives no collision count per block or per part and no measure of energy received by a block; Fig. 10b plots frequency against travel distance only. The abstract states that "the lower rock mass is compressed more frequently, receives more energy transfer, and has a longer migration distance", and conclusion 4 that "the front portion of the rock mass experiences more collisions than the rear portion"; neither statement has a table or figure in Section 3. |
| Suggestion | Add to Section 3.2.2 a table of effective-collision counts, energy received and travel distance per monitored block (IDs 1 to 10) and per part, and derive the abstract and conclusion 4 from it, or remove both statements. |
| Status | verified |
| Severity | major |
| Source | S3, S4 |

**GB-24 Fig. 10b does not show a continuous rise of collisions with travel distance**

| Field | Content |
|---|---|
| Check | P3 |
| Location | Fig. 10b, p. 23; p. 22, l. 418 to 419 |
| Quotation | "it is clear that as the migration distance increases during the landslide, the number of collisions also rises continuously, reaching a peak once the blocks enter the river channel" |
| Concern | Measured points (x ticks 0 at 1331 px, 2500 at 1910 px; y ticks 0 at 1190.5 px, 175 at 704 px; ±0.36 per point): 700 m 16.0, 800 m 6.9; 900 m 27.0, 1000 m 20.0; 2302 m 157, 2402 m 150, 2501 m 146. The trend rises, but not continuously; the travel distance at which blocks enter the river channel is not marked, and the red curve has no equation. |
| Suggestion | Write "rises overall" in l. 419, mark in Fig. 10b the distance at which the river channel is reached, and give the fitted function in the caption. |
| Status | verified (measured) |
| Severity | minor |
| Source | AB |

**GB-25 Fig. 12 plots about 33 states, but envelopes were fitted at 10 time points**

| Field | Content |
|---|---|
| Check | P3, P11 |
| Location | p. 23, l. 426 to 428; Fig. 12a and 12b, p. 25; Fig. 11, p. 23 to 24 |
| Quotation | "This study utilized numerical simulation data of the landslide to perform Alpha Shape envelope fitting on the deposit mass at 10 representative time points" |
| Concern | Counted at enlarged sections of Fig. 12a (600 dpi): about 22 markers on the DE curve above VS = 200 % and about 11 below, about 33 in all (dense markers below VS = 30 % may overlap). Fig. 11 shows 10 envelopes. How VS and AG were obtained at the other times is not stated. |
| Suggestion | State in Section 2.4 and in the caption of Fig. 12 at how many times the envelope was fitted, and mark the 10 times of Fig. 11 in Fig. 12. |
| Status | verified (counted at the enlarged section) |
| Severity | moderate |
| Source | AB, S3 |

**GB-26 Can the model generate the "newly generated fragments" said to fill the envelope?**

| Field | Content |
|---|---|
| Check | P25 |
| Location | p. 24, l. 445 to 450; p. 26, l. 488 to 492; p. 9, l. 178 to 180 |
| Quotation | "These newly generated fragments fill the interior and surface of the deposit mass, causing a sudden expansion of the envelope volume and a sharp increase in surface area." |
| Concern | The methods describe blocks of 8.7 m × 8.7 m with one uniform structural plane and no breakage criterion. If blocks cannot split, no new fragments arise, and the growth of envelope volume and area reflects spreading of the given blocks. The manuscript does not say whether block breakage was enabled. |
| Suggestion | Please state whether and how blocks can break in the model and report the number of blocks over time; otherwise attribute the envelope growth to spreading and revise l. 445 to 450 and conclusion 5. |
| Status | assumption |
| Severity | moderate |
| Source | SD |

**GB-27 The solid-to-fluidized transition at VS = 29.47 % is asserted without a criterion**

| Field | Content |
|---|---|
| Check | P31 |
| Location | p. 24, l. 452 to 456; Fig. 12, p. 25 |
| Quotation | "it can be considered that the landslide transitions from a solid phase to a fluidized phase" |
| Concern | The only basis given is that KE peaks at VS = 29.47 % and AG = 319.5 %. No measure of fluidization (porosity, coordination number, granular temperature, inertial number) is defined or computed. |
| Suggestion | Define a measurable criterion for the transition and show it against time and VS, or describe the point only as the kinetic-energy peak. |
| Status | verified |
| Severity | moderate |
| Source | SD |

#### Minor corrections

| ID | Location | Quotation | Replacement | Source |
|---|---|---|---|---|
| KK-13 | p. 23, l. 425 | "3.4 Structural evolution as a function of energy change" | "3.3 Structural evolution as a function of energy change" | S4 |
| KK-14 | p. 24, l. 438 | "(a-i) when time = 0s, 3s, 7s, 9s, 12s, 15s,32s,71s, 100s, 131s" | "(a-j) at t = 0, 3, 7, 9, 12, 15, 32, 71, 100 and 131 s" | AB |

#### Verification log

| ID | Check | Checked | Values | Result |
|---|---|---|---|---|
| PP-15 | P2, P3 | Maximum velocities in the text against the colour bars of Fig. 7 | text 5.9, 19.6, 27.1, 31.6, 25.7 m/s and "approached 0 m/s" (l. 307 to 347); colour bars 7b to 7g 5.9, 19.6, 27.1, 31.6, 25.7, 0.21 m/s | no finding |
| PP-16 | P2 | Times of Fig. 7 and Fig. 11 against the text | Fig. 7 caption 0, 3, 7, 9, 12, 15, 131 s; duration "131 seconds" (l. 300 to 301); Fig. 11 caption repeats the first six times | no finding |
| PP-17 | P2, P3 | KE peak and riverbed impact, l. 381 to 384, against Fig. 8 | bar spacing about 1.2 s (x ticks 0 s at 682.5 px, 120 s at 1509.5 px); KE peak bar 13.6 s, sharp drop at 14.8 s; text: peak by 12 s, impact around 13 s | no finding |
| PP-18 | P11 | Monitoring plan against results | 10 blocks in 4 parts (Table 2: 2, 3, 3, 2); energy curves for all 10 (Fig. 9a to 9j); trajectories for all 10 (Fig. 10a) | no finding beyond GB-16 |
| PP-19 | P21 | Comparisons of absolute values on different bases | block energies (756 to 1754 m3) compared only within their own panels; no cross-block energy ranking in the text | no finding |
| PP-20 | P22 | Implicit counts and numbering | section 3.3 missing (KK-13); no other count that must be derived | no finding |
| PP-21 | P24 | Dated events in figures | no calendar-dated events; simulation times checked in PP-16 | no finding |
| PP-22 | P19 | Provenance classes | energies, velocities, envelopes model-generated and presented as simulation; field basis photographs only (GB-19) | no further finding |
| PP-23 | P36 | Statements from memory | "about" values l. 149 to 156 are field dimensions (GB-06) | no further finding |

### Segment 4: Conclusions, declarations, references (p. 25 to 29)

#### Substantive findings

**GB-28 Conclusion 1(b) recommends a restoration practice the study did not apply**

| Field | Content |
|---|---|
| Check | P15 |
| Location | p. 25, l. 466 to 468; p. 6, l. 139 to 140 |
| Quotation | "In such cases, restoration can be guided by referencing other mountain areas within the same stratigraphic unit." |
| Concern | In the methods, the contours of the sliding bed and accumulation area were "modified to be straight" (l. 140); no reference to other mountain areas of the same stratigraphic unit is used or tested in Section 3. |
| Suggestion | Either describe and test such a reference-based restoration in Sections 2.1 and 3, or present l. 466 to 468 as a suggestion for future work. |
| Status | verified |
| Severity | minor |
| Source | S4 |

**GB-29 Data and code are available on request only, although no data source concerns persons, and the ground-motion record has no source**

| Field | Content |
|---|---|
| Check | P12 |
| Location | p. 26, l. 494 to 495; p. 26, l. 505 to 506; p. 6, l. 130 to 135; p. 10, l. 189 to 191; p. 11, l. 206 to 207 |
| Quotation | "The data and materials that support the findings of this study are available from the first author, Yunfeng Ge, upon reasonable request." |
| Concern | The methods use the UAV DEM and point cloud (l. 130 to 135), the restored contours and pre-failure surface (l. 138 to 143), the 3DEC model (l. 181), the Luding station record (l. 189 to 191), laboratory tests and inversion behind Table 1 (l. 206 to 207), the histories of ten blocks (Table 2), the peak-detection routine (l. 226 to 234), the alpha-shape envelopes (l. 272 to 284) and the field photographs of Fig. 7o. Data and code statements cover all of them only "upon reasonable request" and give no reason; none concerns persons. The Luding record is third-party data without citation or archive. |
| Suggestion | Deposit DEM, restored surface, 3DEC input files, block histories and the peak-detection and alpha-shape scripts in a public repository with a DOI and cite it in the statements of p. 26, l. 494 to 506; cite the source of the Luding record in l. 189 to 191. |
| Status | verified |
| Severity | moderate |
| Source | S2 |

**GB-30 Citations and reference list do not match: 14 cited works have no entry, 16 entries are never cited**

| Field | Content |
|---|---|
| Check | P4 |
| Location | p. 26, l. 508 to p. 29, l. 605; p. 1, l. 34 to p. 2, l. 63 |
| Quotation | "(Navarre et al., 2009; Van Herwijnen and Schweizer, 2011; Helmstetter and Garambois, 2010; Cook et al., 2021; Pandey et al., 2021)" |
| Concern | All citations stand in l. 34 to 63. Without entry: Fan et al. 2020, Huang et al. 2012, Intrieri et al. 2018, Huang et al. 2019, Zhu et al. 2010, Zhang et al. 2020a, Zhang et al. 2020b, Cuomo et al. 2021, Shugar et al. 2021, Navarre et al. 2009, Van Herwijnen and Schweizer 2011, Helmstetter and Garambois 2010, Cook et al. 2021, Pandey et al. 2021 (14). Year differs from the entry: Tian et al. 2017 (entry 2016), Zhang et al. 2024 (entry Zhang, J. et al. 2023), Zhao et al. 2020 (entry 2021). Misformed or ambiguous: "Fan et al., 2019a" (l. 34) and "Fan et al., 2019" (l. 56 to 57) against two Fan 2019 entries without a and b; "Wang, 2021" (l. 36) for an entry with seven authors; "Song at al.2017" (l. 46); "Cheng 2014" for an entry with two authors. Never cited, 16 of 31 entries: Bernardie et al. 2021, Chang et al. 2022, Chen et al. 2024, Dahal et al. 2022, Gao et al. 2023, Ge et al. 2021, Gong et al. 2024, He, J. et al. 2023, He, K. et al. 2022, He, N. et al. 2023, Nava et al. 2025, Sinčić et al. 2025, Wu, J. et al. 2013, Yang et al. 2022, Zhang, K. et al. 2019, Zhou et al. 2024; among them the closest prior work (GB-02). |
| Suggestion | Add entries for the 14 cited works, align the three years, write "Fan et al., 2019a/b", "Wang et al., 2021", "Song et al., 2017" and a two-author form for Cheng, and either cite the 16 listed works where they are relevant or delete them from the list. |
| Status | verified (counted with Python, confirmed at pages 1, 2 and 26 to 29) |
| Severity | moderate |
| Source | S4, S1 |

#### Minor corrections

| ID | Location | Quotation | Replacement | Source |
|---|---|---|---|---|
| KK-15 | p. 25, l. 464 to 466 | "It should be noted that:(a)" | "It should be noted that: (a)" (likewise "contours; (b)") | S4 |
| KK-16 | p. 26, l. 507 | "Reference" | "References" | S4 |

#### Verification log

| ID | Check | Checked | Values | Result |
|---|---|---|---|---|
| PP-24 | P4 | Numbering of figures, tables, equations and sections | Fig. 1 to 12 in order; Tables 1 and 2 referenced at l. 212 and l. 259; Eq. 1 to 6 in order; sections 1, 2, 2.1 to 2.4, 3, 3.1, 3.2, 3.2.1, 3.2.2, 3.4, 4 | no finding beyond KK-13 |
| PP-25 | P15 | Conclusions against results | C1(a) contour restoration: l. 157 to 162, Fig. 3; C1(b): GB-28; C2 energy extraction: Fig. 8, 9; C2 "ensures": GB-19; C3: GB-14; C4: GB-23; C5: l. 440 to 456, Fig. 11, 12, with GB-26 | no further finding |
| PP-26 | P15 | Core terms of the introduction in the conclusions | "energy transfer" taken up in C3 to C5; "energy accumulation", "early warning", "landslide seismology" not taken up (GB-03) | no further finding |
| PP-27 | P16 | Characters at the page images | superscripts in "2400×104 m3" (l. 151) and "km2" (l. 150) set as superscripts on the page; hyphens used as dashes at l. 193, 218, 228 (KK-07 to KK-09) | no further finding |

## Optional checks

| Area | What it needs | Responsible | Run |
|---|---|---|---|
| DOI resolution | one retrieval per reference entry with a DOI | `science-quellenapparat-pruefung` | no |
| Citation style | the name of the style | `science-zitierstil-harvard-ctr` or the journal's style rules | no |
| AI statement against publisher policy | the target publisher's policy | this review, on request | no |
| Relation to the authors' own prior work | the authors' prior publications | this review, on request | no |
| Journal requirements | the target journal's author guidelines | this review, on request | no |
| Factual accuracy | access to the sources of the checked statements and a selection of sections | `science-faktenbeleg-pruefung`, `geo-frage-belegbasiert-klaeren` | no |

## Limits of this review

- Checked version: egusphere-2025-4506.pdf, 29 pages, SHA-256 64cb3787456244aa6102e34f776b47e9a612d06e8894d391758ae240dbe415d6.
- The six instances ran one after another in a single context, not context-separated.
- The PDF has no machine-readable margin numbers; line numbers were mapped from the printed margin numbers and every cited line was confirmed at the page image. Lines inside Tables 1 and 2 and on figure pages without margin numbers are cited by page and element.
- Sources read only in part: Carpignano et al. 2009 (abstract), Song et al. 2017 (abstract), Zhou et al. 2024 (abstract), Guimpier et al. 2021 (abstract); not readable beyond the title: Wu et al. 2024, Ge et al. 2021, Zhao et al. 2021.
- All figures are raster images; values were measured on renderings at 300 and 600 dpi; Fig. 2a has no graticule ticks, and Fig. 10a and 11 are 3-D projections that were not measured.
- Findings with status assumption: 3 of 30 (central statement only in GB-26; partial in GB-09 and GB-14).
- Optional checks run: 0 of 6.
- Omitted instances: none.
- Discarded findings: 0.
