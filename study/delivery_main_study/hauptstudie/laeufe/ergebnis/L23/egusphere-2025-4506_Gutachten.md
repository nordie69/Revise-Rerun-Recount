# Review report: Energy and structural evolution process of high-altitude and long-runout landslides induced by a strong earthquake

| Field | Value |
|---|---|
| Manuscript | Ge, Y., Hu, B., Tang, H., Fu, X., Zhu, L. (2025): Energy and structural evolution process of high-altitude and long-runout landslides induced by a strong earthquake, EGUsphere preprint, https://doi.org/10.5194/egusphere-2025-4506 |
| Checked version | egusphere-2025-4506.pdf, 29 pages, SHA-256 64cb3787456244aa6102e34f776b47e9a612d06e8894d391758ae240dbe415d6 |
| Date | 2026-10-18 |
| Language | English |
| Review instances | Segments 1 to 4, Figures, Study design; checked one after another, not context-separated: the six review instances ran sequentially in one context, without sub-agents |
| Note | The manuscript has margin line numbers every five lines; einlesen.py did not detect them (indented by 14 characters), so line numbers come from a patched copy of the script and every location was confirmed at the printed margin number on the page image. |

## Summary

The manuscript is a single-case numerical back-analysis of the Mogangling landslide, triggered on the right bank of the Dadu River (Sichuan) by the 1786 Kangding earthquake (Ms 7¾). The pre-failure topography is restored by straightening contour lines derived from a UAV DEM. A 3DEC discrete element model (25345 blocks, landslide mass divided into 8.7 m × 8.7 m columns, Mohr-Coulomb blocks and joints with the parameters of Table 1) is loaded with the acceleration record of the Luding station from the 2008 Wenchuan earthquake. From one 131 s run the authors derive stage velocities of 5.9 to 31.6 m/s, energy histories (PE, KE and DE, with DE defined as ME(t0) minus ME(t)) for the whole mass and for ten monitored blocks, 1,139 "effective collisions" detected as velocity peaks above a 30 % prominence threshold, and alpha-shape envelopes (α = 1) at ten times, from which volume swelling (VS) and area growth (AG) are computed; a solid-to-fluid transition is placed at VS 29.47 % and AG 319.5 %, where the kinetic energy is reported to peak at 1116.8 GJ.

## Strengths

1. The stage-by-stage kinematic description in Sect. 3.1 takes its velocities from the colour-bar maxima of Fig. 7, and all five values agree with the figure, so the narrative of stages can be traced to model output (PP-17).
2. Table 2 gives coordinates and volumes of every monitored block and Fig. 9 shows each block's energy separately; with the density of Table 1 a reader can recompute block masses and the heights implied by the energies (PP-20), which is what makes the datum question of GB-13 answerable at all.
3. Fig. 5 shows peak detection at five prominence thresholds (10 to 50 %) on the same curve, so the effect of the threshold on which peaks count is visible to the reader; what is still missing is the definition of the threshold and its effect on the results (GB-09).
4. The two central modelling limitations, omitted structural planes and the substitute Wenchuan ground motion, are disclosed where the model is introduced (PP-11), and all twelve figures are numbered without gap and referenced in their sections (PP-09).

## Weaknesses

1. The energy analysis does not test what it claims: the constant total energy follows from defining DE as a residual (GB-12), the whole-mass energies cannot be reconciled with either stated landslide volume or with the stated maximum velocity (GB-20), and the potential-energy datum differs between blocks (GB-13). The authors should compute dissipation, frictional and seismic work independently from the model, state the mass and a single datum, and replot Fig. 8 and 9 on that basis.
2. Geometry and input of the model are inconsistent or not reproducible: length, thickness and volume of the landslide disagree, and the modelled volume is 1/75 of the stated one (GB-05); seismic input, solver settings and the origin of the parameters are missing (GB-08); and all data are available only on request (GB-29). A table of geometry, input motion and solver settings, and a data repository, would let readers rebuild the run.
3. Several interpretations go beyond what the model shows: fragmentation is inferred from envelope growth of blocks for which no breakage is described (GB-24), the failure mechanism invokes structural planes that the model omits (GB-17), agreement with the field is asserted from a visual comparison (GB-18), and conclusion 4 compares front and rear mass without per-block data (GB-28). Each statement should be limited to model output, or supported by the quantitative comparison or per-block data proposed in these findings.
4. Detection and figure-derived quantities need definition and checking: the collision threshold (GB-09), the basis of the 1,139 collisions (GB-10), a 45 m/s block in Fig. 5 (GB-11), the timing of river impact (GB-21), the sampling of Fig. 12 that misses the kinetic-energy peak (GB-25) and the α value (GB-16); the literature framing also needs work, with unsupported gap claims (GB-02), missing directly preceding DEM work (GB-03), no discussion section (GB-26) and an incomplete reference list (GB-30). The authors should define each procedure, recompute the transition values, and add a discussion against prior work.

## Findings by segment

### Segment 1: Title, Abstract, Introduction (p. 1 to 2)

#### Substantive findings

**GB-01 A cited source does not appear to support the statement it is cited for**

| Field | Content |
|---|---|
| Check | P13 |
| Location | p. 1, l. 33 to 34 |
| Quotation | "In recent years, the chain disasters of high-level rock landslides in high-intensity earthquake areas have shown a trend of frequent occurrence (Carpignano et al., 2009; Fan et al., 2019a)" |
| Concern | Carpignano et al. (2009), J. Risk Res. 12, 513 to 534, is according to its abstract (JRC repository record JRC53161) a methodological approach to multi-risk maps for the Piedmont Region, Italy. The abstract names neither earthquake-induced landslide chains nor high-level rock landslides nor a trend in their frequency. The full text was not readable. |
| Suggestion | Replace Carpignano et al. (2009) at l. 34 by a source that documents the stated trend, or reword the sentence so that it states what the cited work supports. |
| Status | inferred (abstract only) |
| Severity | moderate |
| Source | S1 |

**GB-02 Gap claims are made without a described search, and counterexamples exist**

| Field | Content |
|---|---|
| Check | P28 |
| Location | p. 2, l. 42; p. 2, l. 49 to 51; p. 2, l. 63 to 64 |
| Quotation | "However, they still lack a quantitative and systematic study of this topic, especially on energy evolution during the collision." |
| Concern | The Introduction also states that "the terrain restoration before a landslide is less" (l. 42) and that contour restoration "can provide a new idea of terrain restoration before a landslide" (l. 50). No databases, search terms or dates are given for any of the three claims. Jaboyedoff et al. (2019) reconstruct pre-failure topography, failure surfaces and deposits with the SLBL method and test it against pre- and post-event lidar DEMs of 70 landslides. Zhao et al. (2018) analyse energy dissipation during the fragmentation of jointed blocks in rockslide-avalanches with DEM. The manuscript's own reference list contains Ge et al. (2021), "Mechanical energy evolution in the propagation of rock avalanches using field survey and numerical simulation" (p. 27, l. 540 to 542), which addresses the claimed gap and is not cited in the text. |
| Suggestion | State the search behind the claims in Sect. 1, or narrow the claims at l. 42, l. 49 to 51 and l. 63 to 64 to what is new relative to Ge et al. (2021), Jaboyedoff et al. (2019) and Zhao et al. (2018). |
| Status | verified (no search described; Ge et al. 2021 listed but not cited); inferred (counterexamples read as abstracts) |
| Severity | moderate |
| Source | S1 |

**GB-03 Directly preceding work on DEM energy dissipation and fragmentation is missing**

| Field | Content |
|---|---|
| Check | P14 |
| Location | p. 2, l. 52 to 64 |
| Quotation | "These efforts have been made to better understand the dynamic process of rockslide-debris avalanches." |
| Concern | Three works anticipate or constrain the contribution and are not in the reference list. Zhao, T., Crosta, G. B., Dattola, G., and Utili, S. (2018): Dynamic fragmentation of jointed rock blocks during rockslide-avalanches: insights from discrete element analyses, J. Geophys. Res. Solid Earth, 123, 3250 to 3269, https://doi.org/10.1002/2017JB015210: the lower block fragments intensely while the upper block fragments little, and joints dissipate energy, which bears on the abstract statement that the lower rock mass is compressed more and receives more energy. Zhao, T., Crosta, G. B., Utili, S., and De Blasio, F. V. (2017): Investigation of rock fragmentation during rockfalls and rock avalanches via 3-D discrete element analyses, J. Geophys. Res. Earth Surf., 122, 678 to 695, https://doi.org/10.1002/2016JF004060: fragmentation arises from bond breakage, which is relevant to the fragmentation reading of Sect. 3.4. Jaboyedoff, M., Chigira, M., Arai, N., Derron, M.-H., Rudaz, B., and Tsou, C.-Y. (2019): Testing a failure surface prediction and deposit reconstruction method for a landslide cluster that occurred during Typhoon Talas (Japan), Earth Surf. Dynam., 7, 439 to 458, https://doi.org/10.5194/esurf-7-439-2019: an established pre-failure reconstruction method. In addition, Zhao et al. (2021) and Wu et al. (2013), both on the Mogangling landslide itself, are in the list but never cited. |
| Suggestion | Discuss the three works in Sect. 1 after l. 64 and position the energy and fragmentation results against them; cite Zhao et al. (2021) and Wu et al. (2013) where the Mogangling event is introduced (l. 38, l. 110). |
| Status | verified (absence from the list); inferred (content from abstracts) |
| Severity | moderate |
| Source | S1 |

#### Minor corrections

| ID | Location | Quotation | Replacement | Source |
|---|---|---|---|---|
| KK-01 | p. 1, l. 13 | "Chengdu, 610041 ,China" | "Chengdu, 610041, China" | S4 |
| KK-02 | p. 1, l. 23; p. 11, l. 221, l. 225, l. 234; p. 25, l. 474 | "displacement velocity curve"; "velocity-travel-distance curve"; "velocity-distance profile"; "travel-distance versus velocity profile"; "displacement-velocity curves" | one term throughout, e.g. "velocity versus travel distance curve", also on the x axes of Fig. 5 ("Travel distance", "Travel Displacement") | S2 |
| KK-03 | p. 1, l. 34 | "such as donghekou" | "such as the Donghekou" | S1 |
| KK-04 | p. 2, l. 44 | "optical remote sensing images and UAV impact" | "optical remote sensing images and UAV imagery" | S1 |

#### Verification log

| ID | Check | Checked | Values | Result |
|---|---|---|---|---|
| PP-01 | P13 | statements with numbers or ratings from cited works, l. 33 to 64 | no numbers from sources; one rating ("trend of frequent occurrence") checked (GB-01); Hu et al. 2017 and Tian et al. 2016 titles concern Ludian 2014 as cited; Song et al. 2017 and Wu et al. 2024, cited at l. 46 for UAV and GIS mapping, not readable | no finding beyond GB-01 |
| PP-02 | P14 | searches (3 of at most 6) | "Mogangling landslide 1786 numerical simulation energy"; "rock avalanche energy evolution discrete element kinetic potential dissipated energy block collision fragmentation"; "Zhao Crosta Utili De Blasio 2017 ... abstract"; pages of this manuscript and its discussion appeared in results and were not opened | three proposals in GB-03 |
| PP-03 | P28 | searches (2 of at most 3) | "reconstruction of pre-failure topography prehistoric landslide contour lines DEM volume estimation"; "Carpignano ... multi-risk maps at the regional level abstract" | see GB-02 |

### Segment 2: Methodologies, Fig. 1 to 6, Tables 1 and 2 (p. 2 to 15)

#### Substantive findings

**GB-04 Geological units and the river carry different names in text and figures**

| Field | Content |
|---|---|
| Check | P38 |
| Location | p. 5, l. 101 to 105; Fig. 2(b), (c); Fig. 3(a), (b); Fig. 4 |
| Quotation | "The quaternary system mainly includes landslide accumulation (Q4del), colluvial Deluvial deposit (Q4col+dl) and alluvial deposit (Q4al)" |
| Concern | Text against legends (page images): Q4del is "landslide accumulation" in the text and "Rubble soil" in Fig. 2(c); Q4col+dl is "colluvial Deluvial deposit" and "Massive gravel"; γO2 is "Jinning plagioclase granite", "Plagiogranite" (Fig. 2c) and "Granite" (Fig. 3). The text names quartz diorite and the Triassic Baiguowan formation (T3bg) on the left bank; Fig. 2(c) shows neither but shows "Hybrid granite" (γM2), which the text does not name. Fig. 3 legends add "Massive gravelly soils" without symbol. Fig. 2(b) labels the river "Daduhe River", the text "Dadu River" (14 times). |
| Suggestion | Use one name and one symbol per unit in l. 101 to 105 and in the legends of Fig. 2(c), 3 and 4, add T3bg and the diorite to Fig. 2(c) or explain their absence, write "Dadu River" in Fig. 2(b), and capitalise "Quaternary" at l. 104. |
| Status | verified (page images) |
| Severity | minor |
| Source | S2, AB |

**GB-05 Length, thickness and volume of the landslide are mutually inconsistent, and the modelled volume is 1/75 of the stated one**

| Field | Content |
|---|---|
| Check | P1, P2 |
| Location | p. 7, l. 149 to 151; p. 9, l. 173 to 182; Table 2, column Volume; Fig. 2(c) |
| Quotation | "about 450 m long, about 1000 m wide along the river, and a planar area of 0.45 km2. The average thickness of the landslide mass is about 100 m, and the volume is about 2400×104 m3" |
| Concern | (1) 0.45 km² × 100 m = 4.5 × 10^7 m³, 1.875 times the stated 2.4 × 10^7 m³; the stated volume implies a mean thickness of 53 m. (2) The length of 450 m contradicts "The length of the landslide mass in the sliding direction is 1021 m" (l. 173 to 174) and the map: in Fig. 2(c), with the scale bar 0 to 600 m = 273.5 px at 300 dpi, the boundary measures 1102 m (± about 20 m) along a-a' and 927 m along the river; the width matches "about 1000 m", the length does not. (3) "the volume of the landslide is 317563 m3" (l. 182): 2.4 × 10^7 / 317563 = 75.6. (4) Block height is "the vertical height from the surface of the landslide mass to the sliding bed" (l. 178 to 179); Table 2 volumes of 756.2 to 1754.3 m³ on 8.7 m × 8.7 m give column heights of 10.0 to 23.2 m, not about 100 m. All energies in Fig. 8 and 9 scale with this mass. |
| Suggestion | Give in Sect. 2.1 one consistent set of length, area, mean thickness and volume, state whether 317563 m³ is the modelled mass and why it differs from the field volume, and reconcile the block heights with the stated thickness. |
| Status | verified (stated values; length measured on Fig. 2c); inferred (ratios and heights, calculated) |
| Severity | major |
| Source | S3, AB, SD |

**GB-06 Fig. 2(c) shows only section a-a', the text refers to a-a' and b-b'**

| Field | Content |
|---|---|
| Check | P3 |
| Location | p. 7, l. 159 to 160; Fig. 2(c); Fig. 3(b) |
| Quotation | "make a section along a-a'and b-b' in Fig2. (c). The results are shown in Fig3. (c)." |
| Concern | Fig. 2(c) (300 dpi) has one section line, labelled a and a'; there is no b-b'. Fig. 3(b) shows "(a-a')" only. |
| Suggestion | Add section b-b' to Fig. 2(c) and Fig. 3(b), or delete "and b-b'" at l. 160. |
| Status | verified (page images) |
| Severity | minor |
| Source | AB |

**GB-07 Several figures lack quantities, units or keys to their symbols**

| Field | Content |
|---|---|
| Check | P29 |
| Location | Fig. 3(b); Fig. 4, inset; Fig. 6; Fig. 7(h) to (n); Fig. 10(b) |
| Quotation | "Fig10. (a) movement trails of 10 monitoring points and (b) the plot of travel distance vs. collision frequency." |
| Concern | Fig. 3(b): both axes without quantity and unit. Fig. 4 inset: tp, tPGA, tf and te are undefined and the time axis has no label or unit. Fig. 6: axes without labels, and the ten coloured points have no key to IDs 1 to 10. Fig. 7(h) to (n): axes without quantity and unit, stress component not named. Fig. 10(b): the red curve is not explained (fit type, equation). |
| Suggestion | Add axis titles with units, define tp, tPGA, tf and te, label the points of Fig. 6 with their IDs, name the stress component in Fig. 7, and state the fitted function of Fig. 10(b) in its caption. |
| Status | verified (page images) |
| Severity | minor |
| Source | AB |

**GB-08 Seismic input and model set-up cannot be rebuilt from the text**

| Field | Content |
|---|---|
| Check | P8, P35 |
| Location | p. 10, l. 187 to 191; Fig. 4, inset; p. 11, l. 206 to 213; Table 1 |
| Quotation | "Extensive research indicates that the Kangding earthquake is comparable to the 2008 Wenchuan earthquake in terms of damage distribution, affected intensity, and estimated magnitude." |
| Concern | The comparability claim has no citation. For the input motion, the components, peak acceleration, duration, scaling, filtering, application at the base boundary and the provider of the Luding record are not given; the Fig. 4 inset shows about ± 100 gal without time axis. Not given either: 3DEC version, damping, time step and contact settings. Table 1 lists two rock materials, "bed rock" and "landslide mass", while Fig. 4 shows γo2, Qdel, γM2 and the sliding mass and the text names strongly and moderately weathered zones (l. 208 to 209). Which parameter comes from laboratory tests, analogy or inversion, and against what the inversion was run (l. 206 to 207), is not stated. |
| Suggestion | Add in Sect. 2.1 a table of input motion and solver settings, cite the comparability claim, and assign every unit of Fig. 4 its parameters with their origin. |
| Status | verified |
| Severity | moderate |
| Source | SD, AB |

**GB-09 The effective-collision threshold is undefined and chosen by eye**

| Field | Content |
|---|---|
| Check | P8 |
| Location | p. 11, l. 226 to 233; Fig. 5 |
| Quotation | "At a threshold of 30%, however, the identification of effective collisions is deemed acceptable." |
| Concern | The prominence threshold is given in percent without its reference quantity (peak velocity, range of the curve, difference to neighbours), and "standout height, width, and position" (l. 228) is not turned into a rule. Fig. 5 shows the five thresholds on one curve, which makes the choice visible, but 30 % is selected by visual judgement on that curve alone, and the effect of 20 % or 40 % on the collision counts of Fig. 10(b) is not shown. |
| Suggestion | Give the detection rule as a formula or a code reference in Sect. 2.2 and show Fig. 10(b) for 20 %, 30 % and 40 %. |
| Status | verified |
| Severity | moderate |
| Source | SD |

**GB-10 The count of 1,139 effective collisions has no stated basis and does not match Fig. 10(b)**

| Field | Content |
|---|---|
| Check | P20 |
| Location | p. 11, l. 233 to 234; Fig. 10(b); p. 22, l. 414 to 415 |
| Quotation | "Under this setting, 1,139 effective collisions were detected from the travel-distance versus velocity profile." |
| Concern | "the ... profile" is singular, but 1,139 peaks cannot come from the single curve of Fig. 5(d). It is not stated whether the count covers all blocks, the ten monitored blocks or one block. Fig. 10(b) shows 26 points at 100 m spacing from 0 to 2500 m; their measured values sum to about 1215 (PP-21), not 1,139. Whether "Frequency" counts per distance bin, per block or cumulatively, and whether it is normalised by the number of blocks reaching each distance, is not stated. |
| Suggestion | State at l. 233 to 234 the unit of analysis behind 1,139, and say in the caption of Fig. 10(b) what one point counts and over how many blocks. |
| Status | verified (wording); inferred (sum of measured points) |
| Severity | moderate |
| Source | S3, AB |

**GB-11 Fig. 5(b) to (f) show a block at 45 m/s, faster than any stage maximum in Sect. 3.1**

| Field | Content |
|---|---|
| Check | P3 |
| Location | Fig. 5(b) to (f), p. 12; Fig. 5(a); p. 16, l. 330 |
| Quotation | "during the impact-at-base stage, the maximum velocity reached 31.6 m/s" |
| Concern | Fig. 5(b): highest point of the curve at 751 px, ticks 0 at 1185.5 px and 50 at 707 px, value 45.4 ± 0.2 m/s at about 245 m travel. The stage maxima of Fig. 7 are 5.9 to 31.6 m/s. Fig. 5(a), described as "a typical velocity-travel-distance curve for an individual block" (l. 221), peaks near 13.5 m/s within 600 m and is a different curve from (b) to (f), which run over 2400 m. Neither block is identified. The snapshot maxima refer to 3, 7, 9, 12 and 15 s only, so a short peak between snapshots is a possible resolution. |
| Suggestion | Identify the block or blocks of Fig. 5 in the caption and explain the 45 m/s against the maxima of Sect. 3.1, or correct one of the values. |
| Status | verified (measured); inferred (comparison with the snapshot maxima) |
| Severity | moderate |
| Source | AB |

**GB-12 Energy conservation of the whole mass follows from Eq. 4 by definition and is presented as a result**

| Field | Content |
|---|---|
| Check | P31, P6 |
| Location | p. 13, l. 249; p. 19, l. 375 to 377; p. 19, l. 387 to 389; p. 1, l. 26 to 27; p. 25, l. 476 to 479 |
| Quotation | "It is evident that, due to the law of energy conservation, the total sum of the three forms of energy remains constant throughout the landslide." |
| Concern | Eq. 4 defines DE(ti) = ME(t0) minus ME(ti), so PE + KE + DE = ME(t0) at every time for any model output, correct or not; Fig. 8 shows this constant total (6483 to 6512 GJ, PP-19). The constancy therefore shows neither conservation nor "a successful energy extraction numerical simulation" (l. 389). The model is driven by an acceleration input at its base (l. 189 to 199), so the slide mass is not a closed system, and DE as a residual mixes seismic work, frictional and damping losses and exchange with the bed. The same identity is what makes single blocks appear "not conserved" (l. 393 to 394), namely as decreases of the residual. |
| Suggestion | Compute the terms independently from the model output (work of the seismic input, frictional work at contacts, damping, strain energy) and show that they close the budget, in Sect. 2.3 and 3.2.1; reword the abstract (l. 26 to 27) and conclusion 3. Counter-design: a budget W_input + ΔPE = ΔKE + W_friction + W_damping + ΔU with every term taken from the solver. |
| Status | verified (identity from Eq. 4); assumption (that the solver can report the separate terms) |
| Severity | major |
| Source | SD, S4, S1 |

**GB-13 The potential-energy datum is not reproducible and differs between blocks**

| Field | Content |
|---|---|
| Check | P8, P2 |
| Location | p. 13, l. 250 to 255; Table 2; Fig. 9 |
| Quotation | "the potential-energy calculation uses the model's initial height as the reference datum rather than true sea level; only the change in potential energy due to relative displacement is considered" |
| Concern | With m = 2300 kg/m³ × Table 2 volume and the measured initial energies of Fig. 9 (PP-20), h = E0 / (m g) is 238.9, 222.9, 235.6, 163.5, 316.0, 172.8, 29.8, 193.3, 82.6 and 43.4 m for blocks 1 to 10, and the datum elevation z minus h is 101, 132, 238, 302, 182, 487, 631, 499, 669 and 712 m. No common datum fits; the top blocks 7, 9 and 10 (z = 661 to 755) start with the smallest PE, and most curves end near PE = 0. "only the change ... is considered" would make PE(t0) = 0, which contradicts "ME(t0) reduces to the initial potential energy" (l. 252). Comparisons of energy between blocks (abstract l. 28 to 30, conclusion 4) depend on this datum. |
| Suggestion | State the datum of each block in Sect. 2.3 (for example the lowest elevation reached, or one common elevation) and replot Fig. 9 on a common datum. |
| Status | verified (wording); inferred (heights from measured energies) |
| Severity | major |
| Source | SD, S3, AB |

**GB-14 Position classes of the monitored blocks are named three ways, and Fig. 6 swaps the two middle classes**

| Field | Content |
|---|---|
| Check | P38, P3 |
| Location | p. 13, l. 256; Table 2, column Position; Fig. 6 |
| Quotation | "ten monitoring points were installed in the lower, lower-middle, upper-middle, and upper portions of the slide mass" |
| Concern | Text: lower, lower-middle, upper-middle, upper; Table 2: bottom, lower middle part, upper middle part, top. Fig. 6 (400 dpi) lists from upslope to downslope: Top, Lower middle part, Upper middle part, Bottom. Table 2 assigns the lower middle part to z = 465 to 498 and the upper middle part to z = 660 to 692, so the upslope middle zone in Fig. 6 should be the upper middle part. |
| Suggestion | Use the Table 2 names at l. 256 and swap the two middle labels in Fig. 6. |
| Status | verified (text and page image) |
| Severity | minor |
| Source | S2, AB |

**GB-15 The volume and area indices compare two different objects and carry several names**

| Field | Content |
|---|---|
| Check | P38 |
| Location | p. 14, l. 275 to 280; p. 24, l. 440 to 441; p. 1, l. 25 |
| Quotation | "V0 denotes the initial volume of the landslide mass (m³); Vt denotes the volume of the enclosing envelope at time t (m³)" |
| Concern | V0 and S0 are properties of the landslide mass, Vt and St properties of the alpha-shape envelope. With V0 as mass volume, VS would not be zero at t = 0, yet Fig. 12 starts at VS = 0 and AG = 0, which implies envelope values at t = 0. The indices are called "volume swelling (VS)" and "area growth (AG)" at l. 275 and "volume expansion rate (VS)" and "surface area growth rate (AG)" at l. 441, and the area is S in Eq. 6 but A at l. 440. |
| Suggestion | Define V0 and S0 at l. 278 to 280 as the envelope volume and area at t = 0, or state the mass values used, and use one name and one symbol for each index in the abstract, Sect. 2.4 and Sect. 3.4. |
| Status | verified (definitions); inferred (what Fig. 12 implies) |
| Severity | moderate |
| Source | S2 |

**GB-16 The alpha value has no unit and no sensitivity test, although the text calls it decisive**

| Field | Content |
|---|---|
| Check | P8, P31 |
| Location | p. 14, l. 281 to 284 |
| Quotation | "this study uniformly sets the α value to 1. This approach ensures a tight fit of the envelope model while minimizing geometric deviations introduced by parameter tuning." |
| Concern | The same paragraph says that α "directly affects the accuracy of the envelope fitting as well as the computed volume and surface area" (l. 281 to 282), but gives no unit for α, no point set (block centroids or vertices) and no variation of α. Whether α = 1 is small or large relative to 8.7 m blocks cannot be judged, and the stated effect "ensures a tight fit" is not shown. |
| Suggestion | State unit and point set in Sect. 2.4 and show VS and AG for at least two further α values. |
| Status | verified |
| Severity | moderate |
| Source | SD |

#### Minor corrections

| ID | Location | Quotation | Replacement | Source |
|---|---|---|---|---|
| KK-05 | p. 3, l. 77 | "the research method involves three parts" | "the research method involves four parts" | S3 |
| KK-06 | p. 10, l. 193 to 195 | "In the course of a discrete-element simulation-particularly when modeling nominally semi-infinite bodies such as the use of fixed or elastic boundaries in a static analysis will inevitably reflect outbound seismic waves" | "In a discrete-element simulation of nominally semi-infinite bodies, fixed or elastic boundaries used in a static analysis reflect outbound seismic waves" | S4 |
| KK-07 | p. 11, Table 1, row 3 | "bed rock" | "bedrock" | S2 |
| KK-08 | p. 12, Fig. 5(a), legend | "Non-obvios acceleration" | "Non-obvious acceleration" | AB |
| KK-09 | p. 13, l. 246 | "where, at time ti, PE(ti), and DE(ti) can be expressed as" | "where, at time ti, KE(ti), PE(ti) and DE(ti) can be expressed as" | S4 |
| KK-10 | p. 13, l. 251 | "(m/s);h(ti)" | "(m/s); h(ti)" | S4 |

#### Verification log

| ID | Check | Checked | Values | Result |
|---|---|---|---|---|
| PP-04 | P10 | design sketch (instanz_SD.md) | study type single-case DEM back-analysis; one run of 131 s; 10 of 25345 blocks monitored; no control or variant; aims l. 65 to 73; chain frame, method part, result: conservation to Fig. 8 and 9, transfer to Fig. 10(b), structure to Fig. 11 and 12, early warning to no result | gaps in GB-12, GB-26, GB-28 |
| PP-05 | P12 | data sources against code and data statements | 8 sources: UAV DEM, restored surface, Luding record, laboratory tests, 3DEC model and outputs, block histories, peak-detection code, alpha-shape scripts; statements l. 494 to 495 and l. 505 to 506; no link, so no reachability check | see GB-29 |
| PP-06 | P38 | identifiers | "Mogangling" 26 times uniform in the text layer; "Kangding earthquake" in the text, "Moxi" earthquake only in a reference title; block IDs 1 to 10 uniform in Table 2, Fig. 9 and Fig. 10 | no finding beyond GB-04, GB-14, GB-15, KK-02 |
| PP-07 | P1 | Table 1 elastic constants | Poisson ratio (3K minus 2G) / (2(3K + G)): bedrock 21.90 and 15.10 GPa give 0.22, landslide mass 11.90 and 6.9 GPa give 0.26 | no finding |
| PP-08 | P1 | 450 m × 1000 m against 0.45 km² | 450000 m² = 0.45 km² | no finding |
| PP-09 | P29, P3 | inventory of figures | Fig. 1 p. 4 scheme, caption l. 91, ref. l. 76; Fig. 2 p. 6 maps and image, l. 126 to 127, ref. l. 93, 160; Fig. 3 p. 8 to 9, l. 166 to 167, ref. l. 144, 159, 160; Fig. 4 p. 10, l. 192, ref. l. 173; Fig. 5 p. 12, l. 238 to 239, ref. l. 220, 229; Fig. 6 p. 14, l. 268, ref. l. 256; Fig. 7 p. 17 to 19, l. 368 to 370, ref. l. 301 to 353, 387; Fig. 8 p. 20, l. 390, ref. l. 375; Fig. 9 p. 21 to 22, l. 410 to 413, ref. l. 393; Fig. 10 p. 23, l. 423 to 424, ref. l. 414, 418; Fig. 11 p. 23 to 24, l. 437 to 439, ref. l. 428; Fig. 12 p. 25, l. 458 to 459, ref. l. 443 | no finding: numbering 1 to 12 without gap, every figure referenced in its section |
| PP-10 | P29 | scale bars of Fig. 2 and 3 | Fig. 2(a) 0 to 160 km; Fig. 2(b) 0 to 600 m; Fig. 2(c) 600 m = 273.5 px at 300 dpi; Fig. 3(c) 0, 400, 800, 1400 m with 45, 44, 65 px at 150 dpi, about 44 px per 400 m | no finding |
| PP-11 | P17 | place of disclosure of limitations | structural planes ignored, l. 175 to 178; substitute ground motion, l. 183 to 191; restored terrain smooth, l. 160 to 162; all at the introduction of the method; dam break not modelled, l. 348 to 350, in Results | no finding (consequences see GB-17, GB-26) |
| PP-12 | P5 | own rules against own examples | block-height rule l. 178 to 179 against Table 2 heights 10.0 to 23.2 m (GB-05); 30 % threshold applied in Fig. 5(d) | see GB-05 |
| PP-13 | P7, P30, P37 | versions, corrections, recomputed data | none reported | no finding |
| PP-14 | P32, P33, P36 | error-free claims, effort statements, statements from recollection | none found | no finding |
| PP-15 | P34 | selection of 10 of 25345 blocks | "to capture representative kinematics" (l. 257), 2 or 3 blocks per class, no selection rule | taken up in GB-28 |
| PP-16 | P25, P26, P27 | feasibility, guarantees, unchecked components | threshold steers counts in Fig. 10(b); DE residual steers the fragmentation reading | see GB-09, GB-24 |

### Segment 3: Results, Fig. 7 to 12 (p. 15 to 25)

#### Substantive findings

**GB-17 The failure narrative of Sect. 3.1 rests on structural planes that the model omits and on details the model does not resolve**

| Field | Content |
|---|---|
| Check | P6, P19 |
| Location | p. 15, l. 308 to 313; p. 15, l. 323; p. 16, l. 326 to 335; p. 9, l. 175 to 178 |
| Quotation | "Under the combined influence of structural plane control and strong seismic forces, the landslide mass was ejected and transformed into a fragmented, granular state." |
| Concern | The model omits structural planes: "the impact of the structural plane on the landslide process has to be ignored in this study" (l. 177 to 178), and the mass is divided by a "uniform structural plane" (l. 180). Sect. 3.1 nevertheless attributes the failure to "steeply dipping structural planes" (l. 308 to 309) and "structural plane control" (l. 323), separates P-wave and S-wave effects (l. 308 to 310), and reports "fine debris such as rock fragments", "a loosely consolidated fractured layer approximately 20 meters thick" and "a layered pseudo-bedrock" (l. 326 to 335), which 8.7 m blocks cannot resolve as model output. Whether these statements come from the field survey, from literature or from the simulation is not stated. |
| Suggestion | Separate in Sect. 3.1 what the simulation shows (with figure reference) from field or literature evidence (with citation), and remove mechanism statements that depend on structural planes absent from the model. |
| Status | verified (contradiction in the text); inferred (that the details are not model output) |
| Severity | major |
| Source | SD |

**GB-18 Validation is a visual comparison and is reported as proof of agreement**

| Field | Content |
|---|---|
| Check | P31, P9 |
| Location | p. 16, l. 353 to 359; Fig. 7(o); p. 25, l. 471 to 472 |
| Quotation | "Fig7. (o) presents compelling evidence of agreement between the numerical simulation results and the actual field observations." |
| Concern | Fig. 7(o) compares a top view of the model with two oblique photographs without scale. No deposit outline, area, runout, thickness or dam height is compared numerically, and no variation of parameters or input is shown. Conclusion 2 states that the comparison "ensures that the simulation outcomes align with actual conditions". |
| Suggestion | Counter-design: compare simulated and mapped deposit outline (overlap ratio), runout, deposit thickness from the difference between restored and present DEM, and dam height, and run at least the parameter and input variants that bracket Table 1 and the ground motion; then reword l. 353 and l. 471 to 472 to what is shown. |
| Status | verified |
| Severity | major |
| Source | SD, S4 |

**GB-19 The stress section at t = 0 shows zero stress although the run starts from static equilibrium, and the section is higher than the model**

| Field | Content |
|---|---|
| Check | P3 |
| Location | Fig. 7(h), p. 18; p. 10, l. 199 to 202; p. 9, l. 181 to 182 |
| Quotation | "Dynamic loading must be introduced only after the model has attained static equilibrium" |
| Concern | Fig. 7(h) is uniformly red with the colour bar "0" to "0Mpa", while Fig. 7(i) to (n) at 3 to 131 s show minus 31 to minus 47 MPa. A gravitationally equilibrated model has non-zero stress at t = 0. The section in Fig. 7(h) reaches 1418 ± 5 m on its own axis (ticks 0 at 1235.5 px and 1200 at 995.5 px, top of the fill at 952 px), whereas the model is "1121m high" (l. 182). The unit is written "Mpa" in all seven colour bars. |
| Suggestion | Show the equilibrated stress state in Fig. 7(h) or state what t = 0 denotes, give the vertical datum of the sections, and write "MPa" in the colour bars. |
| Status | verified (page image, measurement); assumption (that the zero field contradicts the static step) |
| Severity | moderate |
| Source | AB |

**GB-20 The whole-mass energies cannot be reconciled with either stated volume or with the stated maximum velocity**

| Field | Content |
|---|---|
| Check | P2, P23 |
| Location | p. 19, l. 373 to 375; Fig. 8; Fig. 12; p. 16, l. 330 |
| Quotation | "during the impact-at-base stage, the maximum velocity reached 31.6 m/s" |
| Concern | Initial energy in Fig. 8 measured at 6502 GJ; kinetic-energy peak 1116.8 GJ (label in Fig. 12) or 1676 GJ (measured in Fig. 8). Case A, V = 317563 m³ (l. 182), ρ = 2300 kg/m³, m = 7.30 × 10^8 kg: root-mean-square speed sqrt(2 KE / m) = 55.3 m/s or 67.7 m/s, above the stated maximum of 31.6 m/s, which cannot be; mean drop E0 / (m g) = 907 m, above the relief of the modelled mass of 747 m + 131 m = 878 m (l. 174 to 175). Case B, V = 2.4 × 10^7 m³ (l. 151), m = 5.52 × 10^10 kg: speeds 6.4 to 7.8 m/s, but a mean drop of only 12.0 m. Case C, energies in another unit or for another mass: not stated. Which case holds decides the magnitude of every energy in Fig. 8, 9 and 12. |
| Suggestion | State in Sect. 3.2.1 the mass, density and datum behind Fig. 8 and check the energies against the velocities of Sect. 3.1. |
| Status | inferred (calculated from stated values and measured figure values) |
| Severity | major |
| Source | S3, AB |

**GB-21 Fig. 9 places the front blocks high on the slope at the time the text gives for the river impact**

| Field | Content |
|---|---|
| Check | P24 |
| Location | p. 19, l. 383 to 384; Fig. 9(a), (b) |
| Quotation | "Around 13 seconds, the sliding mass impacted the riverbed, causing a sharp drop in kinetic energy due to the obstruction of rock blocks." |
| Concern | At t = 13.2 to 13.6 s, block 1 (bottom) has PE 4.55 of 5.07 GJ (90 %) and block 2 (bottom) 4.2 of 5.14 GJ (82 %), measured. With m = 2300 × 939.9 kg and 2300 × 1021.6 kg they have descended 24.5 m and 40.8 m; they approach PE = 0 only after about 50 to 75 s. The front blocks were therefore not at the river at 13 s. A possible resolution is that only the leading edge, not containing blocks 1 and 2, reached the river. |
| Suggestion | Say at l. 383 which part of the mass reaches the river at 13 s and add the arrival times of blocks 1 and 2. |
| Status | verified (measured); inferred (descent heights) |
| Severity | moderate |
| Source | AB, S3 |

**GB-22 Axis labels in Fig. 9 to 11 are below 6 pt at print size**

| Field | Content |
|---|---|
| Check | P29 |
| Location | Fig. 9, p. 21 to 22; Fig. 10(b), p. 23; Fig. 11, p. 23 to 24 |
| Quotation | "Fig11. Comparison of the overall envelope fitting of the landslide at 10 different times" |
| Concern | Heights at 300 dpi, size in pt = px × 72 / 300 / 0.72: Fig. 11(a) axis digits 7 to 10 px = 2.3 to 3.3 pt; Fig. 10(b) axis digits 12 px = 4.0 pt; Fig. 9(a) capital T of the axis title 15 px = 5.0 pt, axis digits about 13 px = 4.3 pt. |
| Suggestion | Enlarge axis labels in Fig. 9, 10 and 11 to at least 6 pt at print size. |
| Status | verified (measured) |
| Severity | minor |
| Source | AB |

**GB-23 Announced analyses of the monitored blocks are not reported**

| Field | Content |
|---|---|
| Check | P11 |
| Location | p. 22, l. 414 to 421; p. 3, l. 85 to 87; p. 13, l. 258 to 263; Table 2, column Monitoring contents |
| Quotation | "the influence of effective collision frequency of different parts of landslide mass on energy transfer is analyzed" |
| Concern | Matrix of ten blocks against announced outputs (displacement, velocity and stress in X, Y and Z; energy; effective collisions; maximum unbalanced force). Reported: energy per block (Fig. 9) and trajectories (Fig. 10a). Not reported: effective collisions per block or per part (Fig. 10b is over travel distance), the stress histories, and the maximum unbalanced force (ID 11) that is to verify post-failure stability (l. 258 to 259). |
| Suggestion | Add a table of effective collisions per block and per position class, and report the stress and unbalanced-force histories, or remove them from Table 2 and l. 258 to 263. |
| Status | verified |
| Severity | moderate |
| Source | S3 |

**GB-24 VS and AG measure dispersion of blocks, not fragmentation**

| Field | Content |
|---|---|
| Check | P31 |
| Location | p. 24, l. 445 to 452; p. 26, l. 488 to 492; p. 14, l. 285 to 286 |
| Quotation | "In the process of energy transfer, collisions and friction cause block fragmentation and disintegration, producing large amounts of debris. These newly generated fragments fill the interior and surface of the deposit mass" |
| Concern | The manuscript describes no mechanism by which a block breaks: blocks are 8.7 m × 8.7 m columns (l. 178), the model contains 25345 blocks (l. 181), and no breakage criterion, bonded particles or block count over time is reported. VS and AG measure envelope growth, which spreading of intact blocks also produces. "the sharp rise of DE shown in the figure further confirms significant fragmentation" (l. 451) uses the Eq. 4 residual (GB-12). Conclusion 5 states fragmentation as a result. |
| Suggestion | Please state whether blocks can fracture in the model. If not, describe VS and AG as dispersion indices in Sect. 3.4 and conclusion 5; if yes, report number and size of fragments over time. Counter-design: a breakable-block or bonded-particle model as in Zhao et al. (2017, 2018), with fragment counts plotted against VS and AG. |
| Status | verified (no mechanism described); assumption (that blocks cannot fracture in this model) |
| Severity | major |
| Source | SD, S4 |

**GB-25 Fig. 12 misses the kinetic-energy peak of Fig. 8 and has more points than the ten envelope times**

| Field | Content |
|---|---|
| Check | P3 |
| Location | p. 25, l. 453 to 455; Fig. 12; Fig. 8; p. 23, l. 426 to 427 |
| Quotation | "When the volume expansion rate reaches approximately 29.47% and the surface area growth reaches about 319.5%, it can be considered that the landslide transitions from a solid phase to a fluidized phase. At this point, the kinetic energy peaks" |
| Concern | Fig. 8, KE as top of yellow minus top of orange (ticks 0 at 1430.5 px and 7000 GJ at 699.5 px, 9.58 GJ per px): maximum 1676 ± 19 GJ at t = 13.4 s; at t = 11.0 to 11.4 s KE is 1101 to 1120 GJ. Fig. 12 marks the peak at 1116.8 GJ, which matches about 11 s, not the maximum at 13.4 s, so VS and AG at the actual peak are not shown. The labels 29.47 % and 319.5 % agree with the text (PP-22); the problem is the sampling. Fig. 12 also carries more than 20 markers on the DE curve above 5000 GJ alone (counted on an enlarged crop), whereas envelopes were fitted at "10 representative time points" (l. 427). No criterion for the "solid phase to a fluidized phase" transition is given. |
| Suggestion | State how the points of Fig. 12 were sampled, include t = 13.4 s, recompute the VS and AG values of l. 453 to 454, and give the criterion for the phase transition. |
| Status | verified (measured and counted) |
| Severity | major |
| Source | AB, S3 |

#### Minor corrections

| ID | Location | Quotation | Replacement | Source |
|---|---|---|---|---|
| KK-11 | p. 23, l. 425 | "3.4 Structural evolution as a function of energy change" | "3.3 Structural evolution as a function of energy change" | S4 |
| KK-12 | p. 24, l. 438 | "(a-i) when time = 0s, 3s, 7s, 9s, 12s, 15s,32s,71s, 100s," | "(a-j) when time = 0 s, 3 s, 7 s, 9 s, 12 s, 15 s, 32 s, 71 s, 100 s," | S4, AB |

#### Verification log

| ID | Check | Checked | Values | Result |
|---|---|---|---|---|
| PP-17 | P2, P3 | stage velocities in the text against Fig. 7 colour-bar maxima | 5.9, 19.6, 27.1, 31.6, 25.7 m/s at l. 307, 315, 322, 330, 339 equal Fig. 7(b) to (f); Fig. 7(g) 0.21 m/s, text "approached 0 m/s" | no finding |
| PP-18 | P2, P24 | times in Fig. 7 and 11 | Fig. 7: 0, 3, 7, 9, 12, 15, 131 s; Fig. 11 adds 32, 71, 100 s; stated duration 131 s (l. 300) equals the last time; stage order in the text equals panel order | no finding |
| PP-19 | P3 | Fig. 8 total energy over time | top of bars 6483 to 6512 GJ at all times | no finding: constant, as Eq. 4 implies (see GB-12) |
| PP-20 | P3 | Fig. 9 initial total energies (GJ, ± 0.002 to 0.024) | 1: 5.067; 2: 5.138; 3: 4.021; 4: 3.567; 5: 11.075; 6: 6.598; 7: 1.181; 8: 4.377; 9: 1.597; 10: 0.948 | see GB-13 |
| PP-21 | P3 | Fig. 10(b) points | 26 points, 0 to 2500 m in 100 m steps (23 found with `flecken`, 3 near zero counted on a crop): 0.5, 0.5, 2, 4.7, 5.8, 7.6, 15.0, 16.0, 7.0, 27.0, 20.0, 24.0, 30.0, 27.1, 37.1, 42.0, 49.0, 49.7, 53.0, 61.0, 69.0, 72.0, 142.0, 157.0, 150.0, 146.0; sum about 1215 | see GB-10 |
| PP-22 | P2 | VS, AG and KE at the transition, text against Fig. 12 labels | 29.47 %, 319.5 %, 1116.8 GJ in text (l. 453 to 454) and figure | no finding on the labels (sampling see GB-25) |
| PP-23 | P21, P22 | normalisation and derivability | block energies differ by block mass (756.2 to 1754.3 m³); comparisons between blocks in the text are qualitative | no finding beyond GB-10, GB-13 |

### Segment 4: Conclusions, Declarations, References (p. 25 to 29)

#### Substantive findings

**GB-26 There is no discussion, and the stated aims are not taken up**

| Field | Content |
|---|---|
| Check | P15 |
| Location | p. 25, l. 460 to 462; p. 2, l. 71 to 73; p. 5, l. 122 to 125 |
| Quotation | "The findings are intended to provide a theoretical foundation and scientific support for early warning and risk mitigation of high-altitude and long-runout landslides triggered by intense earthquakes." |
| Concern | Sect. 3 is followed directly by Sect. 4 Conclusions. The results are not compared with any study (there is no citation after l. 73), and the disclosed limitations (structural planes omitted, substitute ground motion, dam break not modelled) are not carried into the conclusions. Early warning and risk mitigation (l. 72) and the "evaluation basis for the potential landslide in the high-intensity area of the Dadu River" (l. 124) do not reappear in Sect. 4. |
| Suggestion | Add a discussion section that compares the energy and dispersion results with prior work (e.g. Ge et al., 2021; Zhao et al., 2021), states the effect of each limitation, and says what follows for early warning, or remove that aim from l. 71 to 73. |
| Status | verified |
| Severity | moderate |
| Source | S4, SD |

**GB-27 Conclusion 1 states procedures that the study did not carry out**

| Field | Content |
|---|---|
| Check | P15 |
| Location | p. 25, l. 463 to 468 |
| Quotation | "In such cases, restoration can be guided by referencing other mountain areas within the same stratigraphic unit." |
| Concern | Conclusion 1 also states that contour "trajectory equations can be extracted as a basis for restoring the contours" (l. 465 to 466). Sect. 2.1 describes contours "modified to be straight" (l. 140) and modified "along the extension direction of the mountains" (l. 157); no trajectory equations and no use of other mountain areas of the same unit are reported, and the restoration is not compared with any independent estimate. |
| Suggestion | Restrict conclusion 1 to the procedure of Sect. 2.1, or report the equations and the reference areas in Sect. 2.1. |
| Status | verified |
| Severity | moderate |
| Source | S4 |

**GB-28 Conclusion 4 and the abstract compare front and rear, lower and upper mass without per-part data**

| Field | Content |
|---|---|
| Check | P15, P10 |
| Location | p. 26, l. 483 to 487; p. 1, l. 28 to 30; p. 22, l. 418 to 421 |
| Quotation | "during the collapse stage, the front portion of the rock mass experiences more collisions than the rear portion, with a clear trend of decreasing collision frequency toward the rear." |
| Concern | The Results show collision frequency against travel distance (Fig. 10b), not by position class or block and not restricted to the collapse stage; no collision counts per block are given (GB-23). That the rear mass "transfers energy to the front rock mass, enabling the front portion to slide farther" (l. 486 to 487) is not measured: block energies (Fig. 9) are shown separately and on datums that differ between blocks (GB-13), and no contact work between blocks is computed. The abstract claims that the lower rock mass "is compressed more frequently, receives more energy transfer, and has a longer migration distance" (l. 29 to 30); the travel distances of the ten blocks are not given. Each class holds 2 or 3 blocks (Table 2), selected without a stated rule (PP-15). |
| Suggestion | Report collisions, travel distance and energy gain per block and per position class, with the number of blocks per class, and restrict the abstract and conclusion 4 to what these data show. Counter-design: track all blocks of the mass, group them by initial position, and compute the contact work received by each group over time. |
| Status | verified |
| Severity | major |
| Source | S4, SD, S3 |

**GB-29 The data statement withholds all data on request only, without a reason, and does not name the ground-motion source**

| Field | Content |
|---|---|
| Check | P12 |
| Location | p. 26, l. 494 to 495; p. 26, l. 505 to 506; p. 10, l. 189 to 191 |
| Quotation | "The data and materials that support the findings of this study are available from the first author, Yunfeng Ge, upon reasonable request." |
| Concern | The Methods name eight data sources (PP-05). All are covered only by "upon reasonable request"; none concerns persons, and no reason is given. For the Luding acceleration record, the provider or network is not named at all. |
| Suggestion | Deposit the model files, monitored-block histories, envelope data and scripts in a repository and cite it in the data statement (l. 505 to 506); name the source of the Luding record at l. 190. |
| Status | verified |
| Severity | moderate |
| Source | S2 |

**GB-30 Sixteen citations have no reference entry and eighteen entries are never cited**

| Field | Content |
|---|---|
| Check | P4 |
| Location | p. 26, l. 507 to 605; p. 1, l. 33 to 38; p. 2, l. 45 to 63 |
| Quotation | "(Navarre et al., 2009; Van Herwijnen and Schweizer, 2011; Helmstetter and Garambois, 2010; Cook et al., 2021; Pandey et al., 2021)" |
| Concern | Cited without entry (16): Fan et al. 2020; Huang et al. 2012; Intrieri et al. 2018; Huang et al. 2019; Zhao et al. 2020; Zhu et al. 2010; Zhang et al. 2020a; Zhang et al. 2020b; Cuomo et al. 2021; Shugar et al. 2021; Navarre et al. 2009; Van Herwijnen and Schweizer 2011; Helmstetter and Garambois 2010; Cook et al. 2021; Pandey et al. 2021; Zhang et al. 2024. Entries without citation (18 of 31): Bernardie 2021; Chang 2022; Chen 2024; Dahal 2022; Gao 2023; Ge 2021; Gong 2024; He J. 2023; He K. 2022; He N. 2023; Nava 2025; Sinčić 2025; Wu J. 2013; Yang 2022; Zhang J. 2023; Zhang K. 2019; Zhao 2021; Zhou 2024. Mismatches: "Tian et al., 2017" (l. 37) against entry year 2016 (l. 577); "Wang, 2021" (l. 36) against a seven-author entry (l. 581); "Cheng 2014" (l. 48 to 49) against "Cheng, F., and Yu-Sheng, L." (l. 521); "Fan et al., 2019a" (l. 34) and "Fan et al., 2019" (l. 56 to 57) against two 2019 entries without a and b; "Song at al.2017" (l. 46) for "Song et al., 2017". |
| Suggestion | Complete the reference list for the 16 citations, cite or remove the 18 entries, and align years, author names and the a and b suffixes. |
| Status | verified |
| Severity | moderate |
| Source | S4 |

#### Minor corrections

| ID | Location | Quotation | Replacement | Source |
|---|---|---|---|---|
| KK-13 | p. 25, l. 464 | "It should be noted that:(a)" | "It should be noted that: (a)" | S4 |
| KK-14 | p. 26, l. 507 | "Reference" | "References" | S4 |
| KK-15 | p. 27, l. 530 | "Fan, X., Scaringi, G., Korup, O., et al.:" | full author list, as in the other 30 entries | S4 |

#### Verification log

| ID | Check | Checked | Values | Result |
|---|---|---|---|---|
| PP-24 | P4 | section, table, figure and equation numbers | sections 1, 2, 2.1 to 2.4, 3, 3.1, 3.2, 3.2.1, 3.2.2, 3.4, 4; tables 1 and 2; figures 1 to 12; equations 1 to 6 | gap only at 3.3 (KK-11) |
| PP-25 | P4 | references to figures and tables against their targets | Fig. 1 to 12 and Table 1 and 2 referenced and present; Fig. 3(c) cited at l. 160 for the sections (see GB-06) | no finding beyond GB-06 |
| PP-26 | P15 | conclusions against results | conclusion 1 to GB-27; 2 to GB-18; 3 to GB-12; 4 to GB-28; 5 to GB-24 | all five carry a finding |
| PP-27 | P16 | uniformity of the reference list | 31 entries, 31 DOIs; author lists complete except Fan, Scaringi et al. (KK-15) | no finding beyond KK-15 |
| PP-28 | P15 | proposals in the outlook | no further studies proposed; conclusion 1(b) proposes a restoration rule (GB-27) | no finding beyond GB-27 |

## Optional checks

| Area | What it needs | Responsible | Run |
|---|---|---|---|
| DOI resolution | one request per reference entry with DOI | `science-quellenapparat-pruefung` | no |
| Citation style | the name of the style | `science-zitierstil-harvard-ctr` or the journal's style rules | no |
| AI statement against publisher policy | the target publisher's policy | this review, on request | no |
| Relation to the authors' previous work | the authors' previous work | this review, on request | no |
| Journal requirements | the target journal's author guidelines | this review, on request | no |
| Factual accuracy | access to the sources of the checked statements and a selection of sections | `science-faktenbeleg-pruefung`, `geo-frage-belegbasiert-klaeren` | no |

## Limits of this review

- Checked version: egusphere-2025-4506.pdf, 29 pages, SHA-256 64cb3787456244aa6102e34f776b47e9a612d06e8894d391758ae240dbe415d6.
- Sources not readable: Carpignano et al. (2009) full text (abstract read); Song et al. (2017) and Wu et al. (2024) (publisher pages not retrievable); Zhao et al. (2017, 2018) full texts (abstracts read via Crossref); a Crossref search for a review on failure-surface reconstruction was refused with HTTP 429 and not repeated.
- Findings with status assumption: 3 of 30 (GB-12, GB-19, GB-24, each for a partial statement only).
- Optional checks run: 0 of 6.
- Omitted instances: none; all six instances ran one after another in one context.
- Discarded findings: 0.
