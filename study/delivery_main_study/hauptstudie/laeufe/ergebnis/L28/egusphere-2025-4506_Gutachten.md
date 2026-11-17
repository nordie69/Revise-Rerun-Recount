# Review report: Energy and structural evolution process of high-altitude and long-runout landslides induced by a strong earthquake

| Field | Value |
|---|---|
| Manuscript | Ge, Y., Hu, B., Tang, H., Fu, X., and Zhu, L. (2025): Energy and structural evolution process of high-altitude and long-runout landslides induced by a strong earthquake, EGUsphere preprint egusphere-2025-4506, https://doi.org/10.5194/egusphere-2025-4506 |
| Checked version | egusphere-2025-4506.pdf, 29 pages, SHA-256 64cb3787456244aa6102e34f776b47e9a612d06e8894d391758ae240dbe415d6 |
| Date | 2026-10-18 |
| Language | English |
| Review instances | Segments 1 to 4, figures, study design; the six review instances ran as separate agents; no instance omitted |

## Summary

The manuscript is a single-case numerical study of the 1786 Mogangling rock landslide on the Dadu River (Luding County, Sichuan), triggered by the Ms 7 ¾ Kangding earthquake. The pre-failure terrain is restored by straightening the contour lines of a UAV-derived DEM, and the runout is simulated with the three-dimensional discrete element code 3DEC (25345 blocks, Mohr-Coulomb blocks and discontinuities, viscous base and free-field lateral boundaries), driven by the acceleration record of the Luding station from the 2008 Wenchuan earthquake. Kinetic, potential and dissipated energy are computed for the whole sliding mass and for ten monitored blocks, with the dissipated energy defined as the loss of mechanical energy since the start (Eq. 4). "Effective collisions" are detected as prominent peaks of velocity against travel distance with a 30 % prominence threshold (1,139 detected), and alpha-shape envelopes (α = 1) at ten times give the volume swelling (VS) and area growth (AG) of the moving mass. Key numbers: a run of 131 s, a maximum velocity of 31.6 m/s, a total energy of about 6500 GJ (Fig. 8), a modelled landslide volume of 317563 m³ against a stated field volume of 2400 x 10^4 m³, and a "solid phase to a fluidized phase" transition at VS = 29.47 % and AG = 319.5 %. The manuscript concludes that the whole mass obeys energy conservation while single blocks do not, that the lower (front) mass collides more often and receives energy from the rear, and that collisions fragment the blocks and enlarge the envelope.

## Strengths

1. The energy terms are written out as Eq. (1) to (4) together with the potential energy datum (l. 252 to 255), and KE, PE, DE and ME are used consistently in text and figures (PP-20); this makes the energy balance checkable term by term, which is what allows the closure by definition and the magnitude checks of GB-31 and GB-32 to be traced.
2. The prominence threshold for effective collisions is shown at five values in Fig. 5b to 5f, with the same five values in text and caption, and the number of flagged peaks falls monotonically with the threshold (PP-18, PP-19); a reader can see how the threshold acts on the detected peaks, although the counts per threshold are not given (GB-26).
3. The main departures of the model from the 1786 event are disclosed where the method is introduced: the ignored structural planes, the substitute Wenchuan record, the smooth restored terrain and the relative PE datum, and in the results the unmodelled dam breach (PP-27); the reader therefore learns where the model differs from the event, although the consequences are not drawn (GB-23, GB-24, GB-41).
4. Stage times and maximum velocities agree across the text, the Fig. 7 colour bars and the captions (5.9 to 31.6 m/s, 0 to 131 s), and the kinetic energy maximum of Fig. 8 lies within one bar of the stated impact at about 13 s (PP-30, PP-31, PP-32); the kinematic sequence of Sect. 3.1 can be followed figure by figure.

## Weaknesses

1. The energy results rest on a balance that closes by definition and on magnitudes that the stated mass, velocity and datum do not reproduce: KE + PE + DE equals ME(t0) for any data and any block (GB-31), the kinetic energy peak exceeds the bound set by 317563 m³ and 31.6 m/s by a factor of 3.1 to 4.6 and the PE datum differs from block to block (GB-32), and the landslide volume appears with three incompatible values (GB-18). Suggestion: compute dissipation independently of Eq. (4), state the mass and the datum actually used, and reconcile the volume, Fig. 8 and Fig. 9.
2. The collision results do not carry the front and rear and energy transfer statements of the Abstract and Conclusion 4: collisions are counted only against travel distance, without initial position, stage or normalisation (GB-43), the detection rests on an undefined threshold applied to an unidentified curve and is not checked against contact data (GB-26), and the population behind the 1,139 collisions and Fig. 10b is undefined (GB-44). Suggestion: report collision rates per block or per position group and stage, validate the detection against contact forces, or reword the claims as hypotheses.
3. The link between the model and the 1786 event is not tested: the validation against the present, post-breach deposit is qualitative (GB-41), the seismic input is a record of another earthquake without record parameters or sensitivity runs (GB-24), and Sect. 3.1 explains the failure by structural planes and wave effects that the model ignores or does not measure (GB-23). Suggestion: add a quantitative comparison with the DEM and with Zhao et al. (2021), sensitivity runs for the input motion, and either specify the discontinuities of the model or mark the mechanism text as interpretation.
4. Several claims exceed the design, and several inputs cannot be traced: fragmentation and a solid to fluid transition are claimed without a fragmentation measure or criterion (GB-46), aims such as a general law and early-warning support have no instrument (GB-02), and the terrain restoration, the parameters, the third-party inputs, the data and the references cannot be reproduced or traced (GB-16, GB-22, GB-14, GB-47, GB-48). Suggestion: restrict the claims to what the single run measures, and add the missing method details, sources and a public data deposit.

## Findings by segment

### Segment 1: Abstract, introduction, state of research (p. 1 to 2)

#### Substantive findings

**GB-01 The first source for the claimed increase of earthquake-induced rock landslide chains does not address this trend, and "Fan et al., 2019a" cannot be assigned to one of the two Fan 2019 entries.**

| Field | Content |
|---|---|
| Check | P13, P4 |
| Location | p. 1, l. 33 to 34; p. 2, l. 56 to 57; p. 27, l. 530 to 536 |
| Quotation | "In recent years, the chain disasters of high-level rock landslides in high-intensity earthquake areas have shown a trend of frequent occurrence (Carpignano et al., 2009; Fan et al., 2019a)" |
| Concern | Carpignano et al. (2009), J. Risk Res., 12, 513-534, presents a methodological approach for multi-risk maps at the regional level with a first application in Piedmont (Italy); according to its abstract it treats natural and technological hazards in general and contains no statement on earthquake-induced rock landslides, disaster chains or a trend in their frequency. The trend claim therefore rests on Fan et al. alone. The reference list holds two Fan et al. 2019 entries without suffix (l. 530 to 532, Rev. Geophys.; l. 533 to 536, Landslides), while the text cites "Fan et al., 2019a" (l. 34) and "Fan et al., 2019" (l. 56 to 57), so the reader cannot tell which entry supports the trend. |
| Suggestion | In l. 33 to 34 replace Carpignano et al. (2009) by a source that documents the frequency trend of coseismic landslide chains, or restrict the sentence to what Fan et al. support; label the two Fan entries "2019a" and "2019b" in l. 530 to 536 and use the matching suffix in l. 34 and l. 56 to 57. |
| Status | verified (abstract of Carpignano et al. 2009 read at ideas.repec.org; two Fan 2019 entries without suffix on the page image p. 27); inferred (full text of Carpignano et al. 2009 not readable) |
| Severity | moderate |
| Source | S1, S4 |

**GB-02 Several stated aims (a general law, energy accumulation, energy per collision, early warning and the Dadu River evaluation basis) have no instrument in the single-case, single-run design and are not taken up again, and there is no discussion section.**

| Field | Content |
|---|---|
| Check | P10, P15 |
| Location | p. 2, l. 39 to 41; p. 2, l. 63 to 64; p. 2, l. 65 to 73; p. 5, l. 123 to 125; p. 25, l. 460 to 479; p. 26, l. 480 to 492 |
| Quotation | "so as to summarize the law of high-level rock landslide induced by earthquake"; "it focuses on revealing the mechanisms of energy accumulation, transfer, and dissipation during the landslide event"; "The findings are intended to provide a theoretical foundation and scientific support for early warning and risk mitigation of high-altitude and long-runout landslides triggered by intense earthquakes." |
| Concern | The reconstruction of the Mogangling runout (motion, velocity, deposition) is covered by Sect. 3.1, Fig. 7 and Fig. 10a. The manuscript states no research questions, and four further aims have no instrument or result. (a) A "law" for earthquake-induced high-level rock landslides (l. 40) needs variation across cases or conditions, but the design has one case, one input motion, one parameter set (Table 1) and one run. (b) The gap named in l. 63 to 64, energy during the collision, is not measured: collisions are detected from velocity peaks and counted (l. 220 to 234, Fig. 10b), but no energy exchanged per collision is computed (see GB-43). (c) "energy accumulation" occurs only in l. 68 (text search) and in no result or conclusion. (d) Early warning and risk mitigation (l. 71 to 73) and the "evaluation basis for the potential landslide in the high-intensity area of the Dadu River" (l. 124) are not taken up in Sect. 3 or 4; the seismic trigger named in the title does not occur in the conclusions (l. 460 to 492, text search). There is no discussion section: all citations stand in l. 34 to 63 (Python over the body text), so the results are not compared with earlier work, although the reference list contains studies of the Mogangling landslide itself (Wu et al., 2013, l. 588 to 590; Zhao et al., 2021, l. 600 to 602) and of mechanical energy evolution in rock avalanches (Ge et al., 2021, l. 540 to 542), none of them cited. The limitations the manuscript discloses (l. 175 to 178, l. 183 to 191, l. 348 to 350, l. 354 to 355) are not drawn together, and there is no outlook. Major, because (a) and (b) concern what the study claims to contribute. |
| Suggestion | In l. 65 to 73 state research questions limited to the single-case reconstruction, or extend the design: compute the change of mechanical energy of each monitored block within each detected collision window and report energy per collision by position group (this answers l. 63 to 64); for any general statement add parametric runs (input motion, joint friction, block size) or a second case with comparable data. Otherwise remove "summarize the law" (l. 40), "energy accumulation" (l. 68) and the early-warning purpose (l. 71 to 73, l. 123 to 125). Insert a discussion section before Sect. 4 that compares the results with Wu et al. (2013), Zhao et al. (2021) and Ge et al. (2021) and lists the disclosed limitations with their expected effect. |
| Status | verified (no instrument and no uptake for a to d, checked through Sects. 2 to 4; no citation after l. 63); inferred (that a single run cannot support a general law) |
| Severity | major |
| Source | S4, SD |

**GB-03 The claims that pre-failure terrain restoration is rare and that contour restoration is "a new idea" rest on no described search and overlook a published reconstruction method that is also validated.**

| Field | Content |
|---|---|
| Check | P28, P14 |
| Location | p. 2, l. 42; p. 2, l. 46 to 51; p. 25, l. 463 to 468 |
| Quotation | "At present, in terms of surface terrain restoration, the terrain restoration before a landslide is less."; "which can provide a new idea of terrain restoration before a landslide for the same type of research." |
| Concern | Neither claim names a database, search terms, period or search date. Within the same paragraph, l. 46 to 47 presuppose a body of "numerical simulations involving terrain restoration", which sits uneasily with "less" in l. 42. A published open access method reconstructs pre-failure topography from post-event topography and checks it: Jaboyedoff, M., Chigira, M., Arai, N., Derron, M.-H., Rudaz, B., and Tsou, C.-Y.: Testing a failure surface prediction and deposit reconstruction method for a landslide cluster that occurred during Typhoon Talas (Japan), Earth Surf. Dynam., 7, 439-458, https://doi.org/10.5194/esurf-7-439-2019, 2019. It applies the sloping local base level (SLBL) method to 70 deep-seated landslides and states that "the inverse SLBL was used to check the validity of the reconstruction of the pre-event topography". The contour method of this manuscript is checked only visually ("the restored terrain is smooth", l. 161). The work is not in the reference list. The sentence in l. 42 is also ungrammatical. |
| Suggestion | In l. 42 to 51 state the search behind both claims or rephrase them relative to the cited works (for l. 42, for example, "few studies restore the pre-landslide terrain"); cite Jaboyedoff et al. (2019), state what the contour method adds over SLBL-type reconstructions, and qualify the "preliminary restoration" of Conclusion 1 (l. 463 to 468) against this method. |
| Status | verified (no search described; wording of l. 42 and l. 46 to 47; Jaboyedoff et al. 2019 read at esurf.copernicus.org, absent from the reference list) |
| Severity | moderate |
| Source | S1, S4 |

**GB-04 Do Song et al. (2017) and Wu et al. (2024), cited for photo, field, remote sensing, UAV and GIS mapping, contain such mapping?**

| Field | Content |
|---|---|
| Check | P13 |
| Location | p. 2, l. 43 to 46; p. 28, l. 569 to 571; p. 28, l. 585 to 587 |
| Quotation | "the key information of landslide characteristics is often obtained through photos, field surveys, optical remote sensing images and UAV impact, so as to further build geomorphic maps through GIS (Geographic Information System) for subsequent analysis" |
| Concern | In the reference list, Song et al. (2017) is "Landslide Deformation Prediction by Numerical Simulation in the Three Gorges, China" (l. 569 to 571), and Wu et al. (2024) is a numerical simulation of potential landslide-induced wave hazards with a hybrid method (l. 585 to 587). Neither title indicates photo, field, remote sensing, UAV or GIS mapping. Abstracts and full texts of both were not readable, so the doubt rests on the titles only. The other two works cited, Fan et al. (2020) and Zhang et al. (2024), have no entry in the reference list (GB-48). |
| Suggestion | Question to the authors: do Song et al. (2017) and Wu et al. (2024) describe the mapping workflow of l. 43 to 45? If not, replace them in l. 46 by studies that do (missing entries for Fan et al., 2020 and Zhang et al., 2024 in GB-48). |
| Status | inferred (titles only; abstracts not accessible) |
| Severity | moderate |
| Source | S1 |

**GB-05 The statement that "most" numerical simulations involving terrain restoration are two-dimensional is not supported by the three cited works, one of which involves neither terrain restoration nor a runout simulation.**

| Field | Content |
|---|---|
| Check | P13 |
| Location | p. 2, l. 46 to 49 |
| Quotation | "For most numerical simulations involving terrain restoration, a two-dimensional simulation is more often used. The simplified model is adopted to simulate the overall process of landslide by inputting external stress (Du et al., 2021; Cheng 2014; Li et al., 2024)." |
| Concern | Li et al. (2024), Front. Earth Sci., 12, 1466751, builds a GeoStudio seepage and stability model driven by a rainfall series; it does not reconstruct the pre-failure terrain and does not simulate the runout or an external stress input. Cheng and Yu-Sheng (2014) use UDEC with seismic acceleration for the Huanglang Valley ancient landslide, which fits the sentence. The abstract of Du et al. (2021) names a discrete element simulation with a paleo-earthquake trigger but states neither the model dimension nor a terrain restoration. Three works, of which one does not match and one is undetermined, cannot carry a statement about "most" simulations. |
| Suggestion | In l. 46 to 49 support the ranking with a review or a count of studies, or rephrase it as "Several simulations ... (e.g. Cheng and Yu-Sheng, 2014)" and remove Li et al. (2024) from this sentence. |
| Status | verified (Li et al. 2024, full text read at frontiersin.org; Cheng and Yu-Sheng 2014, abstract); inferred (Du et al. 2021, abstract only) |
| Severity | moderate |
| Source | S1 |

**GB-06 Two of the five works cited for landslide seismology are snow avalanche studies, and none of the five has an entry in the reference list.**

| Field | Content |
|---|---|
| Check | P13 |
| Location | p. 2, l. 61 to 63 |
| Quotation | "In recent years, landslide seismology has taken on more visibility (Navarre et al., 2009; Van Herwijnen and Schweizer, 2011; Helmstetter and Garambois, 2010; Cook et al., 2021; Pandey et al., 2021)." |
| Concern | Van Herwijnen and Schweizer (2011), "Monitoring avalanche activity using a seismic sensor", Cold Reg. Sci. Technol., 69, 165-176, detects snow avalanches with a geophone near Davos. That paper cites Navarre, J., Bourtova, E., Roulle, J., and Deliot, Y. (2009): The seismic detection of avalanches: an information tool for the avalanche forecaster, ISSW 2009, 379-383, also on snow avalanches. None of the five works is in the reference list (GB-48), so the identification of Navarre et al. (2009) rests on authors and year. The gap claim of l. 63 to 64 (GB-07) thus rests partly on literature from another process domain. |
| Suggestion | In l. 62 to 63 replace the two snow avalanche studies by seismological studies of rock avalanches or landslides (missing entries in GB-48). |
| Status | verified (Van Herwijnen and Schweizer 2011, full text read at slf.ch); inferred (Navarre et al. 2009, identified through the reference list of Van Herwijnen and Schweizer 2011, not read) |
| Severity | moderate |
| Source | S1 |

**GB-07 The gap claim on energy evolution during collisions rests on no described search, while uncited entries of the manuscript's own reference list and an open access DEM study already address energy evolution and front to rear energy transfer.**

| Field | Content |
|---|---|
| Check | P28, P14 |
| Location | p. 2, l. 63 to 64; p. 1, l. 28 to 30; p. 26, l. 483 to 487 |
| Quotation | "However, they still lack a quantitative and systematic study of this topic, especially on energy evolution during the collision."; "When the rear rock mass collides with the front, its dissipated energy sharply increases and transfers energy to the front rock mass, enabling the front portion to slide farther." |
| Concern | No search is described. The reference list contains, uncited, Ge et al. (2021), "Mechanical energy evolution in the propagation of rock avalanches using field survey and numerical simulation", Landslides, 18, 3559-3576 (l. 540 to 542), and Chang et al. (2022), "Dynamic process analysis of the Xinmo landslide via seismic signal and numerical simulation", Landslides, 19, 1463-1478 (l. 514 to 516); their titles indicate that energy evolution in rock avalanche propagation and the combination of landslide seismology with simulation have been studied (abstracts not accessible). Not in the reference list: Lin, Q., Wang, Y., Xie, Y., Cheng, Q., and Deng, K.: Multiscale effects caused by the fracturing and fragmentation of rock blocks during rock mass movement: implications for rock avalanche propagation, Nat. Hazards Earth Syst. Sci., 22, 639-657, https://doi.org/10.5194/nhess-22-639-2022, 2022. With DEM simulations the authors find that fragmentation acts by "accelerating the front sub-block while decelerating the rear sub-block" and that "The energy transfer induced by fragmentation is more efficient than that induced by collision". This anticipates the rear to front transfer of the Abstract (l. 28 to 30) and Conclusion 4, and it bears on the attribution of the transfer to collisions, since the manuscript itself invokes fragmentation within the same process (l. 447 to 448) without separating the two. |
| Suggestion | In l. 63 to 64 state the search, cite and discuss Ge et al. (2021) and Chang et al. (2022), add Lin et al. (2022), and restate what remains open; in Sect. 3.2.2 and Conclusion 4 (l. 483 to 487) discuss whether the front acceleration in the 3DEC model can be separated into collision and fragmentation contributions. |
| Status | verified (no search; Ge et al. 2021 and Chang et al. 2022 listed and not cited, checked with Python; Lin et al. 2022 abstract read at nhess.copernicus.org, absent from the list); inferred (content of Ge et al. 2021 and Chang et al. 2022 from their titles) |
| Severity | moderate |
| Source | S1 |

**GB-08 Several sentences are grammatically incomplete or have an unclear reference, so that no single replacement can be given.**

| Field | Content |
|---|---|
| Check | P16 |
| Location | p. 2, l. 63 to 64; p. 5, l. 108 to 109; p. 5, l. 113 to 119 |
| Quotation | "the series of losses caused by earthquakes, landslides, river blocking, and a breach super flood disaster chain"; "the evaluation and analysis of dam break or dam overturning caused by abnormal bedrock landslide such as surging waves are relatively few." |
| Concern | In l. 63, "they still lack" has no clear antecedent (the seismology studies of l. 62 to 63, or landslide studies in general). In l. 108 to 109 the noun phrase is not well formed. In l. 113 to 119 the subject of "are relatively few" is not clear, and "abnormal bedrock landslide such as surging waves" mixes cause and effect. The meaning is only partly recoverable; single errors that can be replaced are listed as minor corrections. |
| Suggestion | Have the manuscript language-edited, starting with l. 63 to 64, l. 108 to 109 and l. 113 to 119. |
| Status | verified (page images p. 2 and 5) |
| Severity | minor |
| Source | S4 |

#### Minor corrections

| ID | Location | Quotation | Replacement | Source |
|---|---|---|---|---|
| KK-01 | p. 1, l. 13 | "Chengdu, 610041 ,China" | "Chengdu, 610041, China" | S4 |
| KK-02 | p. 1, l. 21; p. 3, l. 84 | "dissipation energy" | "dissipated energy (DE)", as in l. 242 | S2 |
| KK-03 | p. 1, l. 27 to 28 | "conservation of energy; For some blocks"; "surrounding rock mass; Compared with" | "conservation of energy; for some blocks"; "surrounding rock mass; compared with" | S4 |
| KK-04 | p. 1, l. 34 to 35 | "such as donghekou landslide debris flow dammed lake" | "such as the Donghekou landslide, debris flow and dammed lake chain" | S1, S4 |
| KK-05 | p. 1, l. 36 | "Wang, 2021" | "Wang et al., 2021" (the entry in l. 581 to 584 has seven authors) | S1, S4 |
| KK-06 | p. 1, l. 37; p. 28, l. 575 to 577 | "Tian et al., 2017" (entry dated 2016) | the same year in text and entry | S4 |
| KK-07 | p. 2, l. 42 to 43 | "For landslides that have not occurred too far away" | "For recent landslides" | S4 |
| KK-08 | p. 2, l. 44 | "optical remote sensing images and UAV impact" | "optical remote sensing images and UAV imagery" | S1, S4 |
| KK-09 | p. 2, l. 46 | "Song at al.2017" | "Song et al., 2017" | S1, S4 |
| KK-10 | p. 2, l. 48 to 49; p. 27, l. 521 | "Cheng 2014" (entry "Cheng, F., and Yu-Sheng, L.") | "Cheng and Yu-Sheng, 2014", after checking the order of family and given names in the entry | S4 |

#### Verification log

| ID | Check | Checked | Values | Result |
|---|---|---|---|---|
| PP-01 | P13 | Inventory of all cited statements and selection of those with numbers, rankings or evaluations | 28 citation strings (29 works, "Zhang et al., 2020a, b" counted twice), all on p. 1 to 2, l. 34 to 63; no citation elsewhere in the body (Python over the text, p. 1 to 26). Ranked or evaluative statements: l. 33 to 34, l. 43 to 46, l. 46 to 49, l. 61 to 63. Uncited figures from literature checked against a listed source: l. 110 to 112, l. 148 to 151 | findings GB-01, GB-04, GB-05, GB-06, GB-18; statements without number or ranking in PP-02 |
| PP-02 | P13 | Attributions without number or ranking: Donghekou and Hongshiyan (l. 34 to 37), genesis and propagation (l. 52 to 54), field methods (l. 54 to 57), numerical methods and drone video (l. 57 to 59) | 15 works, not opened because the sentences carry no number, ranking or evaluation; 9 of them have no entry in the reference list | no finding (missing entries in GB-48) |
| PP-03 | P14 | Search for work preceding or contradicting the contribution, five queries (Mogangling runout with discrete elements; reconstruction of pre-failure topography and SLBL; rock avalanche DEM energy evolution front and rear; a Chinese-language query on the Mogangling simulation; earthquake-triggered rock avalanche DEM energy for Donghekou or Daguangbao), each candidate checked against the reference list (l. 508 to 605) | Jaboyedoff et al. (2019) absent, proposed; Lin et al. (2022) absent, proposed; Yuan et al. (2014), Nat. Hazards Earth Syst. Sci., 14, 1195-1205, absent, same field only, not proposed; Zhao et al. (2021), Wu et al. (2013), Zhou et al. (2024), Ge et al. (2021), Chang et al. (2022) present in the list, so no proposal; Zhou et al. (2024) reports a numerical study of the same landslide, which the Introduction does not mention | findings GB-03, GB-07; uncited listed works in GB-02 and GB-07 |
| PP-04 | P28 | Gap and novelty sentences and search descriptions | l. 42 "the terrain restoration before a landslide is less"; l. 50 "a new idea of terrain restoration"; l. 61 "direct observation data are rarely available in previous studies"; l. 63 to 64 "they still lack a quantitative and systematic study"; l. 119 "relatively few"; no database, search term, period or search date anywhere in the manuscript | findings GB-03, GB-07, GB-13; l. 61 concerns the availability of observation data and is followed by works that address it: no finding |
| PP-05 | P18 | Principles the manuscript demands of others, applied to itself | demand for a quantitative study of energy during collision (l. 63 to 64); restoration offered "for the same type of research" (l. 50 to 51) | no further finding beyond GB-02 and GB-16 |

### Segment 2: Methods (p. 2 to 15)

#### Substantive findings

**GB-09 The workflow is announced as "three parts" but four are listed, and the parts carry different names in the text, in Fig. 1 and in the headings of Sects. 2.1 to 2.4.**

| Field | Content |
|---|---|
| Check | P38 |
| Location | p. 2, l. 76; p. 3, l. 77 to 90; Fig. 1 (p. 4); p. 5, l. 92; p. 11, l. 214; p. 12, l. 240; p. 14, l. 269 |
| Quotation | "the research method involves three parts: (1) surface terrain restoration"; "(4) Extraction of volume and area of landslide accumulation area" |
| Concern | Fig. 1 gives an overview with four colour-coded blocks, and the text lists four parts (1) to (4) after announcing three. Names per part: (1) "surface terrain restoration" (l. 77), "Geo-mechanical Model Building" (Fig. 1), "Geo-mechanical model building" (heading 2.1); (2) "Analysis of Landslide Evolution Process" (l. 80 and Fig. 1), which contains "effective collision extraction" (l. 82 to 83), while Sect. 2.2 "Effective collision identification" stands as a section of its own and no section carries the name of part (2); (3) "Energy evolution analysis" (l. 83), "Analysis of Energy Evolution During Block Motion" (Fig. 1), "Energy evolution" (heading 2.3); (4) "Extraction of volume and area of landslide accumulation area" (l. 87 to 88 and Fig. 1), "Structural extraction of landslide accumulation area" (heading 2.4). |
| Suggestion | Write "four parts" in l. 77 and give each part one name in l. 77 to 88, in Fig. 1 and in the headings of Sects. 2.1 to 2.4, or state which section treats which part. |
| Status | verified (page images p. 2 to 5) |
| Severity | minor |
| Source | S2, S4, AB, SD |

**GB-10 Fig. 1 uses energy symbols that are not explained and differ from Eq. (1) to (4), and one box label runs into its frame.**

| Field | Content |
|---|---|
| Check | P29 |
| Location | Fig. 1, panel "Analysis of Energy Evolution During Block Motion" (Global Perspective) and left column box "Extraction of volume and area of landslide accumulation area" (p. 4, caption l. 91) |
| Quotation | "Fig1. Flow chart of the proposed method of this study" |
| Concern | The flow chart expands KE, PE, DE, VS and AG, which helps a reader follow Sects. 2.1 to 2.4. The Global Perspective panel, however, uses "P0E", "PtE" and "KtE" (subscripts 0 and t), which are defined neither in the figure nor in the caption and differ from the notation PE(ti), KE(ti) of Eq. (1) to (4). In the left column the bold label "Extraction of volume" touches the left and right frame of its box at print size. |
| Suggestion | In Fig. 1 replace "P0E", "PtE", "KtE" by PE(t0), PE(ti), KE(ti) as in Eq. (1) to (4), or define them in the caption; reduce the font of the fourth stage box so that the label stays inside the frame. |
| Status | verified (page image p. 4) |
| Severity | minor |
| Source | AB, S2 |

**GB-11 The location markers in Fig. 2a and Fig. 2b do not lie at the landslide-centre coordinates given in the text, and the scale bar of Fig. 2a does not agree with its graticule.**

| Field | Content |
|---|---|
| Check | P3 |
| Location | p. 5, l. 95 to 96; Fig. 2a and Fig. 2b (p. 6) |
| Quotation | "The coordinates of the landslide center are: 29 ° 37 ′ 30.726 ″ north latitude, 102 ° 09 ′ 41.190 ″ east longitude." |
| Concern | Both panels carry a graticule, so the marker positions can be measured. Fig. 2b: the star lies on the grid crossing 29°37′00″N, 102°09′00″E (offset 0 ± 1 px). With the scale bar (0 to 600 m = 110 px), the text coordinates lie 30.726″ x 30.87 m = 948 m north and 41.190″ x 30.87 m x cos 29.6° = 1105 m east of that crossing, 1.46 km from the star, at the western edge of the Dadu River channel drawn in Fig. 2b, north-east of the landslide scar. Fig. 2a: the dot lies at 29.55°N, 101.17°E (± 0.03°), about 0.99° (about 96 km) west of the 102.16°E of the text. The scale bar of Fig. 2a (0 to 160 km = 147.6 px) does not match the graticule (2° of latitude = 155.5 px = 222 km): the bar is 15 % (east to west) to 32 % (north to south) too short. Either the text coordinates or the markers are wrong; a reader who uses the text coordinates to retrieve a DEM would select an area east of the landslide. |
| Suggestion | Check the coordinates in l. 95 to 96 against the DEM; place the star in Fig. 2b and the dot in Fig. 2a at the corrected coordinates; redraw the scale bar of Fig. 2a from the map projection or remove it in favour of the graticule. |
| Status | verified (positions and scale measured on the page image); inferred (which of the two is wrong) |
| Severity | moderate |
| Source | AB |

**GB-12 The lithological units carry different names and codes in the text, the map, the block diagram, the profile and the model, and the unit on the left bank is Triassic sand slate in the text but hybrid granite on the map.**

| Field | Content |
|---|---|
| Check | P38, P3 |
| Location | p. 5, l. 101 to 107; Fig. 2c legend (p. 6, caption l. 126 to 127); Fig. 3a and Fig. 3b legends (p. 8); Fig. 4 legend (p. 10) |
| Quotation | "strongly to weakly weathered Jinning plagioclase granite (γO2). Quartz diorite (O2) and a small amount of basic magmatic rocks are distributed on the western slope of Mogangling. The sand slate of the Triassic Baiguowan formation (T3bg) is exposed on the left bank of the Dadu River." |
| Concern | The geological description in l. 93 to 112 gives unit codes, which makes a cross-check possible. Names per unit, read on the page images: γo2 "Jinning plagioclase granite" (text, written "γO2"), "Plagiogranite" (Fig. 2c), "Granite" (Fig. 3a, Fig. 3b), "γo2" (Fig. 4); Q4del "landslide accumulation" (text), "Rubble soil" (Fig. 2c), "Qdel" without the subscript 4 (Fig. 4); Q4col+dl "colluvial Deluvial deposit" (text), "Massive gravel" (Fig. 2c), while Fig. 3b lists both "Massive gravelly soils" and "Massive gravel" and Fig. 3a only "Massive gravelly soils"; Q4al "alluvial deposit" (text), "Sand and pebble gravel" (Fig. 2c, Fig. 3a, Fig. 3b); quartz diorite "(O2)" (text, without the rock symbol that γO2 and γM2 carry), "Diorite" (Fig. 3a, Fig. 3b), absent from Fig. 2c. The text places T3bg on the left bank; no figure shows T3bg, and Fig. 2c and Fig. 4 show instead γM2 "Hybrid granite" east of the Dadu River, a unit the text never mentions. The river arrows in Fig. 2c point south, so the east side is the left bank. A reader cannot tell whether "Massive gravelly soils" is Q4del or Q4col+dl, nor where the diorite of Fig. 3b crops out in Fig. 2c. Moderate, because the mapping of units between map, profile and model feeds the material assignment (GB-22). |
| Suggestion | Introduce one name and one code per unit in l. 101 to 107 ("γo2" in l. 102, a complete code for the quartz diorite, "The Quaternary system" and "colluvial-deluvial deposit" in l. 104 to 105), add γM2 and its relation to T3bg there, and use the same names and codes ("Q4del" with subscript) in the legends of Fig. 2c, Fig. 3a, Fig. 3b and Fig. 4. |
| Status | verified (all names on the page images p. 5, 6, 8, 10); inferred (bank side from the flow arrows in Fig. 2c) |
| Severity | moderate |
| Source | S2, AB, S4 |

**GB-13 The statement that seismic slope instability and dam break analyses for the region are "relatively few" is a gap claim without source or search.**

| Field | Content |
|---|---|
| Check | P28 |
| Location | p. 5, l. 113 to 119; p. 27, l. 546 to 548 |
| Quotation | "the analysis of the instability probability of potentially unstable high and steep slopes under the action of seismic force and the evaluation and analysis of dam break or dam overturning caused by abnormal bedrock landslide such as surging waves are relatively few." |
| Concern | Neither a citation nor a search (databases, terms, period) is given for this claim or for "the effect of seismic force on slope instability has been underestimated to a certain extent" (l. 113 to 114). The reference list contains, uncited, He et al. (2023), "Seismic response of an irregular slope containing surficial weak layer and internal fractures in Dadu River, southwest China", Landslides, 21, 621-640 (l. 546 to 548), whose title addresses seismic slope response on the Dadu River itself. |
| Suggestion | In l. 113 to 119 cite the studies on which the assessment rests, including He et al. (2023) from the own list, or state the search; otherwise present the claim as the authors' assessment. |
| Status | verified (no citation and no search; He et al. 2023 listed and not cited); inferred (content of He et al. 2023 from its title) |
| Severity | moderate |
| Source | S1 |

**GB-14 Third-party inputs (remote sensing image, geological map, historical tablet, strong-motion record) and the field investigation are used without origin, and the field findings that support the failure sequence are not reported.**

| Field | Content |
|---|---|
| Check | P12, P19 |
| Location | p. 6, l. 126 to 127 (Fig. 2b, Fig. 2c); p. 6, l. 136 to 137; p. 9, l. 180; p. 10, l. 189 to 191; p. 13, l. 264 to 266; p. 16, l. 345; p. 19, l. 367 to 370 (Fig. 7o); p. 25, l. 472 to 473; p. 26, l. 505 to 506 |
| Quotation | "(b) remote sensing image of Mogangling; and (c) engineering geological map."; "this study adopts the acceleration records measured at the Luding station during the Wenchuan earthquake as the input ground motion"; "the sequence of failure and run-out at Mogangling was inferred by integrating the numerical results with field-investigation findings"; "The existing deposits still reflect this flow pattern." |
| Concern | The manuscript explains openly why the Wenchuan record replaces the missing 1786 record (l. 183 to 191); the gap here is origin and access, not the choice (record parameters in GB-24). Five inputs come from outside the authors' simulation, and for none of them does the manuscript give an operator, a record or scene identifier, a date or a citation: (a) the Luding station record (network or data centre); (b) the remote sensing image of Fig. 2b (sensor or provider, acquisition date); (c) the engineering geological map of Fig. 2c, which is also the "geological engineering drawing" of l. 180 (own mapping or adapted from a published map); (d) the Tiezhuang Temple tablet (l. 136 to 137, no citation); (e) the field investigation and the photographs of Fig. 7o (date, author). The field findings are used to infer the failure sequence (l. 265 to 266) and the flow pattern (l. 345) and support Conclusion 2 (l. 472 to 473), but no section reports dates, mapped features, measurements or samples, so the reader cannot separate model output from field evidence. The data statement (l. 505 to 506) covers none of (a) to (e). Whether (a) to (c) are subject to third-party licences is not stated. |
| Suggestion | Add in Sect. 2.1 (after l. 191), in the captions of Fig. 2 and Fig. 7 and in the data statement the origin of (a) to (e): data provider and record identifier for the Luding record, provider and acquisition date for Fig. 2b, the source of the map in Fig. 2c, a citation for the tablet, and date, author and scope of the field investigation and the photographs. Add a subsection on the field campaign (date, observations, measurements), or give the source of each field statement at l. 345, l. 353 to 359 and l. 472 to 473. |
| Status | verified (no origin in text, captions or statement; no field data reported); inferred (that a to c are third-party data, from the wording and the missing authorship claim); assumption (licence restrictions) |
| Severity | moderate |
| Source | S2, SD |

**GB-15 Several symbols in Fig. 2 and Fig. 3b are not explained in a legend, and latitude labels of Fig. 2a are overprinted by panel (b).**

| Field | Content |
|---|---|
| Check | P29 |
| Location | Fig. 2a, Fig. 2b and Fig. 2c (p. 6, caption l. 126 to 127); Fig. 3b (p. 8) |
| Quotation | "Fig2. Position of the study area: (a) the location of the Mogangling landslide; (b) remote sensing image of Mogangling; and (c) engineering geological map." |
| Concern | The legend of Fig. 2c explains units, boundary, fault, bridge and river, but not the attitude symbols with "60°" and "80°", the red section line, the blue flow arrows or the contour lines (no interval and no unit, although values such as 1825 to 1125 are printed). Fig. 3b shows an attitude symbol "80°" without explanation. The right-hand latitude labels of Fig. 2a are printed into the gap next to panel (b) and overlap its label "29°37′N". The inset map of China in Fig. 2a is not mentioned in the caption. |
| Suggestion | Add the section line, attitude symbol, flow arrow and contour interval (in m a.s.l.) to the legends of Fig. 2c and Fig. 3b; move the right-hand latitude labels of Fig. 2a inside its frame or delete them; mention the inset in the caption of Fig. 2. |
| Status | verified (page images p. 6 and 8) |
| Severity | minor |
| Source | AB |

**GB-16 The terrain restoration cannot be reproduced, and the two procedures named in Conclusion 1 (trajectory equations, reference to other mountain areas) appear neither in the methods nor in the results.**

| Field | Content |
|---|---|
| Check | P8, P15, P17 |
| Location | p. 6, l. 130 to 140; p. 7, l. 141 to 143 and l. 157 to 162; Fig. 1 (p. 4); Fig. 3c (p. 9); p. 25, l. 463 to 468 |
| Quotation | "the contour lines corresponding to the sliding bed and accumulation area are modified to be straight"; "their trajectory equations can be extracted as a basis for restoring the contours"; "In such cases, restoration can be guided by referencing other mountain areas within the same stratigraphic unit." |
| Concern | The steps have no stated rules: which contours are changed, how they are straightened (Fig. 1: "Curve Straightening", "Curve Regularization"), and how the deposit was removed to obtain the bed beneath it (Fig. 1: "Lower Slide Bed Restoration", "Deposit Removal"). DEM resolution, UAV survey date, screening density, and noise reduction and cavity repair settings are missing. No trajectory equation is given, and no step that refers to other mountain areas of the same stratigraphic unit appears in Sect. 2.1, in Fig. 1 or in the results; the contours of the accumulation area were straightened like those of the sliding bed (l. 139 to 140), so the limitation stated in l. 466 to 468 is not visible where the method is introduced. The restored terrain is assessed only visually (l. 160 to 162), and no volume balance between restored source volume and deposit volume is reported, although the restored surface defines the sliding mass (l. 171 to 172) and thus every energy value. The core of Conclusion 1 (a preliminary restoration is possible) stands, which is why the grade is moderate. |
| Suggestion | In Sect. 2.1 (l. 136 to 143, l. 157 to 162) describe the procedure with a rule for each step and for the deposit area, move the limitation of l. 466 to 468 there, and give the DEM metadata. Quantify the uncertainty with a blind test: remove the contours of an intact slope next to the landslide, restore them with the same procedure, compare with the true DEM and report the root mean square error; add the volume balance. Either demonstrate both procedures of Conclusion 1 in Sect. 2.1 or mark them in l. 464 to 468 as suggestions for future work. |
| Status | verified (page images p. 4, 6, 7, 25) |
| Severity | moderate |
| Source | SD, S4 |

**GB-17 Fig. 3a is cited for a division into four parts, but its legend shows two zones with other names, two legend colours are indistinguishable and one layer has no legend entry.**

| Field | Content |
|---|---|
| Check | P38, P4, P3 |
| Location | p. 7, l. 144 to 146; Fig. 3a (p. 8, caption l. 166) |
| Quotation | "As shown in Fig3.(a), the geometric model of the terrain surface is established according to DEM. The whole landslide occurrence area can be divided into four parts: the rock wall area, colluvial slope area, slope debris flow area, and main accumulation area." |
| Concern | The legend of Fig. 3a marks only "I Sliding bed" and "II Accumulation area". Of the four parts named in l. 145 to 146 only "accumulation area" has a counterpart; "rock wall area", "colluvial slope area" and "slope debris flow area" appear in no figure, and l. 152 to 156 describe elevation bands under yet other names. Measured median colours: legend "Diorite" (137, 120, 112) and "Sand and pebble gravel" (138, 118, 91) differ by a sum of 24, below the threshold of 40 for distinct colours; a grey band (116, 116, 116) of the block diagram has no legend entry. The scale bar (5 x 200 m) is drawn in an oblique 3D view, where it holds at most along one direction. |
| Suggestion | Mark the four parts of l. 145 to 146 in Fig. 3a, or state how they relate to zones I and II and to the elevation bands of l. 152 to 156; give "Diorite" and "Sand and pebble gravel" clearly different colours, add the grey layer to the legend, and replace the scale bar by a note "not to scale" or by distance ticks along the block edges. |
| Status | verified (page images p. 7 and 8; colours measured) |
| Severity | minor |
| Source | S2, S4, AB |

**GB-18 The landslide dimensions and volume are inconsistent: area times thickness does not give the stated volume, the stated values differ from the cited source, the dimensions match the deposit rather than the landslide, and the modelled volume is 1/75.6 of the stated one.**

| Field | Content |
|---|---|
| Check | P1, P2, P3, P13, P27 |
| Location | p. 7, l. 148 to 151; p. 9, l. 173 to 174 and l. 178 to 182; Table 2, column Volume (p. 13); Fig. 2c (p. 6); p. 5, l. 110 to 112 |
| Quotation | "about 450 m long, about 1000 m wide along the river, and a planar area of 0.45 km2. The average thickness of the landslide mass is about 100 m, and the volume is about 2400×104 m3."; "The length of the landslide mass in the sliding direction is 1021 m"; "the volume of the landslide is 317563 m3"; "tens of thousands of people drowned." |
| Concern | The relief is consistent (PP-12); the volumes are not (all values computed with Python). (1) 450 m x 1000 m = 0.45 km² is consistent, but 0.45 km² x 100 m = 4.5 x 10^7 m³ = 4500 x 10^4 m³, not 2400 x 10^4 m³ (which would imply a mean thickness of 53.3 m). Zhao et al. (2021), Nat. Hazards, 106, 459-485, in the reference list (l. 600 to 602) but not cited, give in their abstract "a volume of approximately 4500 × 104 m3, 450 m long and 1000 m wide" and report over 100 000 deaths after the dam breach; the manuscript repeats length and width but gives 2400 x 10^4 m³ and "tens of thousands" of deaths (l. 111 to 112), without any source. (2) The exponent in l. 151 is printed on the line, so "2400×104 m3" reads 249 600 m³. (3) The modelled volume of 317563 m³ (l. 182) is 1/75.6 of 2400 x 10^4 m³ and 1/141.7 of 4500 x 10^4 m³; the manuscript does not say whether only part of the mass was modelled. (4) Length: 450 m (l. 149) against 1021 m in the sliding direction (l. 174, Fig. 4). Measured on Fig. 2c (scale 0 to 600 m = 273.3 px), the deposit polygon Q4del encloses 0.478 km², is 987 m wide and has a mean length of 484 m, while the landslide boundary encloses 0.99 km², with 1158 m of the section line inside it; the 450 m, 1000 m and 0.45 km² therefore describe the deposit, not the landslide as a whole. (5) The ten blocks of Table 2 have volumes of 756.2 to 1754.3 m³, i.e. heights of 10.0 to 23.2 m on the 8.7 m x 8.7 m bases (l. 178), against a mean thickness of about 100 m; if they are representative, 317563 m³ corresponds to about 276 blocks. (6) No mass balance of the restored terrain is reported (GB-16), although the volume and mass enter every energy value (GB-32). Major: if 317563 m³ is the modelled mass, the model holds about 1/76 of the landslide, and its energies, runout and dam are not those of the event. |
| Suggestion | In l. 148 to 151 state the outline to which length, width and area refer and add length and area of the whole landslide; correct the volume (4500 x 10^4 m³ if Zhao et al. (2021) is followed, otherwise explain 2400 x 10^4 m³ and the thickness) and set the exponent as a superscript; cite the sources of the figures in l. 110 to 112 and l. 148 to 156. In l. 182 state the modelled volume, the number of landslide blocks and their plan area, explain the difference to the field volume, and report the source volume between the restored and present surfaces against the deposit volume. |
| Status | verified (arithmetic; printed values; exponent on the page image p. 7; Zhao et al. 2021 abstract read via ideas.repec.org); inferred (assignment of the dimensions to Q4del from measurements on Fig. 2c; block count, which depends on the representativeness of the Table 2 blocks) |
| Severity | major |
| Source | S1, S3, SD, AB, S4 |

**GB-19 The text refers to sections a-a' and b-b' in Fig. 2c and to their results in Fig. 3c, but Fig. 2c has one section line labelled "a" at both ends, and the only profile is Fig. 3b.**

| Field | Content |
|---|---|
| Check | P4, P38, P3 |
| Location | p. 7, l. 159 to 160; Fig. 2c (p. 6); Fig. 3b (p. 8); Fig. 3c (p. 9) |
| Quotation | "As shown in Fig3. (b), make a section along a-a'and b-b' in Fig2. (c). The results are shown in Fig3. (c)." |
| Concern | Fig. 2c contains one red section line; both ends are labelled "a", without prime, and there is no b-b'. Fig. 3b is headed "(a-a')" and shows one profile. Fig. 3c shows contour maps and shaded surfaces before and after restoration, not section results. The sentence therefore points to a missing section and to the wrong panel. |
| Suggestion | Label the east end of the line in Fig. 2c "a'"; either add section b-b' to Fig. 2c and its profile to Fig. 3 or delete "and b-b'" in l. 160; let "The results are shown in" refer to Fig. 3b and keep Fig. 3c for the comparison of the surfaces. |
| Status | verified (page images p. 6, 7, 8, 9) |
| Severity | minor |
| Source | S2, S4, AB |

**GB-20 The profile in Fig. 3b places the river and the slope toe about 55 to 75 m higher than the elevations given in the text.**

| Field | Content |
|---|---|
| Check | P3 |
| Location | Fig. 3b (p. 8); p. 7, l. 151 to 152 |
| Quotation | "The elevation of the slope toe is 1120 m (about 5 m higher than the river surface)" |
| Concern | Elevation axis calibrated on the boundaries of the black and white elevation bar (1000 m at 2406 px, 2000 m at 1864 px at 300 dpi; calibration error 10 px). The water surface lies at 1173 ± 20 m and the profile surface at the slope toe at about 1173 to 1190 m, against 1120 m for the toe and about 1115 m for the river in the text; the difference of about 58 m at the river exceeds the uncertainty plus rounding (20 + 5 m). The slopes along the profile agree roughly with l. 153 to 156 (PP-10), so the offset concerns the absolute elevations. |
| Suggestion | Check the elevation scale of Fig. 3b against the DEM and correct either the profile or the elevations in l. 151 to 156; state in the caption whether the profile follows a-a' of Fig. 2c exactly. |
| Status | verified (measured on the page image) |
| Severity | minor |
| Source | AB |

**GB-21 Several figures have axes or scales without quantity or unit.**

| Field | Content |
|---|---|
| Check | P29 |
| Location | Fig. 3b (p. 8), both axes; Fig. 3c (p. 9), contour values; Fig. 4 inset (p. 10), time axis; Fig. 6 (p. 14), all three axes; Fig. 7h to 7n (p. 18), both axes |
| Quotation | "Fig6. Location of 10 monitoring points" |
| Concern | Fig. 3b has numbers 1000 to 2000 and 0 to 1500 but no axis titles. Fig. 3c gives contour values without unit. The Fig. 4 inset shows "Acceleration (gal)", but its time axis has neither title, numbers nor unit. Fig. 6 has numbers 0 to 800, 400 to 2400 and 400 to 3200 without x, y, z or (m), while Fig. 4 and Fig. 7 label the same views "x(m)", "y(m)", "z(m)". Fig. 7h to 7n have numbers 0 to 1200 and 0 to 2700 without titles, and it is not said which section of the model they show. The y axis of Fig. 10b is treated in GB-44. |
| Suggestion | Add axis titles with units: Fig. 3b "Elevation (m a.s.l.)" and "Distance along a-a' (m)"; the contour interval and unit in the legend of Fig. 3c; "Time (s)" with ticks in the Fig. 4 inset; "x (m)", "y (m)", "z (m)" in Fig. 6; "Elevation (m)", "Distance (m)" and the position of the section in Fig. 7h to 7n. |
| Status | verified (page images p. 8, 9, 10, 14, 18) |
| Severity | minor |
| Source | AB |

**GB-22 Material parameters and numerical settings cannot be traced or reproduced, and the material classes have different names in Table 1, the text and Fig. 4.**

| Field | Content |
|---|---|
| Check | P8, P35, P38 |
| Location | p. 9, l. 173 and l. 179 to 181; Fig. 4 legend (p. 10); p. 11, l. 203 to 213; Table 1 (p. 11, l. 213) |
| Quotation | "the selection of physical-mechanical parameters was based primarily on laboratory testing, empirical analogy, and parameter inversion"; "The slope is underlain by plagioclase granite, which is subdivided into strongly weathered and moderately weathered zones."; "the established model includes the landslide mass and base block" |
| Concern | Table 1 gives a complete parameter set per class, which is a good basis for reproduction. (1) No parameter has a stated source; laboratory tests (samples, number, method) and the inversion (target, objective, procedure) are not described. (2) Class names differ: the text names "strongly weathered and moderately weathered zones" (l. 208 to 209), Table 1 "bed rock" and "landslide mass", l. 173 "base block", and Fig. 4 shows four materials (γo2, Qdel, γM2, sliding mass); Table 1 has one row for the base but Fig. 4 three base units, and l. 101 calls the weathering range "strongly to weakly". For the discontinuities the text has "fully developed potential rupture planes and joint sets" (l. 209 to 210), Table 1 "discontinuities" and "potential discontinuities", and l. 179 to 180 "A uniform structural plane"; the mapping is only implied by the word "potential". (3) Missing settings: 3DEC version, rigid or deformable blocks, damping type and value in the dynamic stage, time step, contact detection, peak or residual friction during runout. (4) In Table 1 the shear stiffness exceeds the normal stiffness for both joint types (1500 against 960 GPa/m; 180 against 100 GPa/m). Question to the authors: are the two columns swapped? (5) No sensitivity run covers joint friction or damping, which control runout and dissipation. In addition, Table 1 writes "bed rock" and gives "6.9" where the other moduli carry two decimals. |
| Suggestion | In Sect. 2.1 add a table of parameter, value and source (laboratory with sample count, analogy with reference, inversion with target), a column "assigned to" in Table 1 that links each row to the Fig. 4 materials and the text names, and a list of the numerical settings; use the Table 1 names in l. 173, l. 179 to 180 and l. 207 to 210, write "bedrock" and "6.90"; add sensitivity runs for joint friction and damping (release of the model files in GB-47). |
| Status | verified (1 to 3 and 5; names on the page images p. 9, 10, 11); assumption (4), posed as a question |
| Severity | moderate |
| Source | SD, S2, S4 |

**GB-23 Sect. 3.1 attributes the failure to structural planes, P and S waves and topographic amplification, but the model ignores the structural planes, as stated, and the other effects are not measured.**

| Field | Content |
|---|---|
| Check | P6, P31 |
| Location | p. 9, l. 175 to 180; p. 11, l. 208 to 210; p. 15, l. 306 to 313, l. 316 to 318 and l. 323; Table 2, column Monitoring contents (p. 13) |
| Quotation | "the impact of the structural plane on the landslide process has to be ignored in this study"; "The first-arriving P-waves caused intense vertical dislocation along the steeply dipping structural planes outside the slope."; "Under the combined influence of structural plane control and strong seismic forces" |
| Concern | The limitation in l. 175 to 178 is disclosed where the model is introduced, but its consequences are not drawn. Sect. 3.1 explains tension cracking along "steeply dipping structural planes", "pre-existing potential sliding surfaces" (l. 313) and "structural plane control" (l. 323), which matters for the aim to study the "formation mechanism" (l. 39). At the same time "A uniform structural plane is set inside" (l. 179 to 180), and the discontinuities are "fully developed potential rupture planes and joint sets" (l. 209 to 210, Table 1), with no orientation, spacing or location; a reader cannot tell which planes exist in the model. The input is "the acceleration records" of one station (l. 189 to 190), with no components, direction or application stated. Question to the authors: was a vertical component applied, without which the sequence of P and S wave arrivals in l. 308 to 310 cannot arise in the model? Amplification "at higher elevations" and the "back-slope effect" (l. 311, l. 316 to 317) are not measured: no accelerations at different elevations are reported, and Table 2 records displacement, velocity and stress only. The Mogangling studies in the reference list (Wu et al., 2013; Zhou et al., 2024) are not cited for these mechanisms. Major, because the mechanism statements answer the aim on the formation mechanism. |
| Suggestion | In Sect. 2.1 specify the discontinuity sets of the model (orientation, spacing, extent), reconcile them with l. 175 to 178, and state the input components and how they are applied. In Sect. 3.1 either report measured quantities (acceleration amplification at monitoring points of different elevation, slip on discontinuities) or mark the mechanism text as interpretation, with literature. |
| Status | verified (l. 177 to 178 against l. 323; geometry not stated; no amplification measured); assumption (need for a vertical input), posed as a question |
| Severity | major |
| Source | SD |

**GB-24 The seismic input is a record from another earthquake and another station, given without reference, record parameters or sensitivity analysis.**

| Field | Content |
|---|---|
| Check | P9, P19 |
| Location | p. 10, l. 183 to 191; Fig. 4 inset (p. 10); p. 5, l. 97 to 99 and l. 110; p. 29, l. 600 to 601 |
| Quotation | "Extensive research indicates that the Kangding earthquake is comparable to the 2008 Wenchuan earthquake in terms of damage distribution, affected intensity, and estimated magnitude."; "this study adopts the acceleration records measured at the Luding station during the Wenchuan earthquake as the input ground motion" |
| Concern | The substitution is disclosed where the input is introduced, but its consequences are not drawn. (1) "Extensive research" has no citation. (2) l. 186 to 187 place the Mogangling landslide and the Wenchuan earthquake zone in the "tectonic system of the Longmenshan Fault Zone", while l. 97 to 99 place the site at the junction of the Xianshuihe, Longmenshan and Anninghe faults, and the listed Zhao et al. (2021) names the 1786 event the "Moxi M 7.75 earthquake" (l. 600 to 601). Question to the authors: why should the Luding record of the Wenchuan event represent the shaking at Mogangling in 1786 (source distance, fault, site)? (3) Record parameters are missing: components, PGA (the axis of the Fig. 4 inset spans about plus and minus 100 gal), duration, baseline correction, filtering, scaling, direction. (4) No sensitivity analysis is run, although all velocities (5.9 to 31.6 m/s, l. 307 to 330), energies and collision counts depend on the input. Major, because every dynamic result depends on the input motion. |
| Suggestion | Give the record parameters and cite the comparability studies in l. 187 to 189. Counter-design for Sect. 2.1: run the model with a small set of input motions, for example the Luding record scaled to PGA estimates for the 1786 event plus two other records or synthetic near-field motions, and report the spread of peak velocity, peak KE, runout and collision counts. |
| Status | verified (no citation, no parameters, no sensitivity analysis); assumption (difference between the shaking of the two events), posed as a question |
| Severity | major |
| Source | SD |

**GB-25 The input accelerogram in Fig. 4 carries symbols that are explained nowhere, and the caption does not mention it.**

| Field | Content |
|---|---|
| Check | P29 |
| Location | Fig. 4 inset and legend (p. 10, caption l. 192) |
| Quotation | "Fig4. Discrete numerical model with fine topography" |
| Concern | The inset marks four times "tp", "tPGA", "tf" and "te"; none of them occurs in the caption or in the text ("PGA" does not occur, "peak ground acceleration" appears once in l. 317 without abbreviation). The record is identified only in l. 190, not in the figure. The legend gives the codes γo2, Qdel, γM2 without names (GB-12). The labels "1021m", "747m", "179m", "131m" agree with l. 174 to 175 (PP-13). |
| Suggestion | Extend the caption of Fig. 4 with the identity of the inset record and the meaning of tp, tPGA, tf and te, and add names to the legend codes. |
| Status | verified (page image p. 10; text search) |
| Severity | minor |
| Source | AB |

**GB-26 Effective collisions are identified from velocity peaks with an undefined, visually chosen threshold, applied to a curve that is not identified, and the identification is not checked against contact data that the model records.**

| Field | Content |
|---|---|
| Check | P31, P32, P8, P29 |
| Location | p. 11, l. 215 to 234; Fig. 5a to 5f (p. 12, l. 235 to 239); Table 2, column Monitoring contents (p. 13); p. 16, l. 331; p. 25, l. 473 to 475; p. 1, l. 22 to 23 |
| Quotation | "a suitable prominence threshold must be chosen-one that quantifies each peak’s standout height, width, and position relative to adjacent peaks"; "At a threshold of 30%, however, the identification of effective collisions is deemed acceptable." |
| Concern | The threshold sensitivity is shown visually in Fig. 5b to 5f, the only sensitivity check of the study (PP-19). Open points: (1) The threshold is a percentage, but its reference quantity (maximum velocity of the block, local velocity, curve range) is not stated, nor how "height, width, and position" are combined; no formula, function or software is named. (2) "deemed acceptable" is a visual judgement on one curve; there is no reference set of known collisions, and the counts at 10, 20, 40 and 50 % are not given, so the sensitivity of the 1,139 cannot be quantified. (3) The curve in Fig. 5b to 5f is not identified, and the caption does not explain the red markers, the grey box or the inset; the curve reaches 45.5 ± 0.2 m/s at a travel displacement of 251 m (measured), more than every maximum velocity of Sect. 3.1 (largest 31.6 m/s, l. 330) and Fig. 7, while the "typical" block of Fig. 5a peaks at about 13.5 m/s. (4) A velocity peak marks the end of an acceleration phase. Question to the authors: how are collision-driven peaks separated from peaks caused by steeper ground, by the shaking during the input record, or by free fall during the "brief airborne trajectory" (l. 331)? (5) Table 2 lists stress histories (Stress-XX, Stress-YY, Stress-ZZ) for the monitored blocks, but they are not used to confirm the detected collisions. Major, because Conclusion 2 (l. 473 to 475) and the collision results of GB-43 rest on this detection. |
| Suggestion | In Sect. 2.2 define the prominence measure with formula, reference quantity and units, and name the implementation; name in the caption of Fig. 5 the block or quantity plotted in (b) to (f) and explain markers, box and inset. Validate the detection: for a random sample of detected peaks and of windows without peaks, check the stress or contact force histories for contact events, and report the shares of confirmed and of missed collisions. Report the collision counts for each threshold from 10 to 50 %, and separate peaks during the input motion from later ones. Question to the authors: at what time does the 45.5 m/s occur? |
| Status | verified (no definition, no validation, no counts; missing explanations; 45.5 m/s measured on the page image); assumption (alternative causes of velocity peaks; explanation of the 45.5 m/s), posed as questions |
| Severity | major |
| Source | SD, AB |

**GB-27 The curve on which effective collisions are detected has six names, and its abscissa is "Travel distance" in Fig. 5a but "Travel Displacement" in Fig. 5b to 5f.**

| Field | Content |
|---|---|
| Check | P38 |
| Location | p. 11, l. 221, l. 225, l. 227 and l. 234; Fig. 5 axis titles (p. 12); Fig. 1 (p. 4); p. 1, l. 23; p. 25, l. 474 to 475 |
| Quotation | "a typical velocity-travel-distance curve for an individual block"; "travel-distance versus velocity profile"; "the displacement velocity curve"; "extracting local peaks from displacement-velocity curves" |
| Concern | Sect. 2.2 explains the detection criterion and documents the threshold choice in Fig. 5b to 5f. Its object, however, has six names (counted with Python): "displacement velocity curve" (l. 23), "velocity-travel-distance curve" (l. 221), "velocity-distance profile" (l. 225), "velocity-distance curve" (l. 227), "travel-distance versus velocity profile" (l. 234), "displacement-velocity curves" (l. 474). The axis title is "Travel distance (m)" in Fig. 5a and Fig. 1, and "Travel Displacement (m)" in Fig. 5b to 5f. Travel distance (path length) and displacement (net change in position) differ for a block that rebounds, as blocks 1 and 3 do (l. 397, l. 416), so the detected peaks depend on which is meant. Moderate, because the input of the detection cannot be reproduced without it. |
| Suggestion | Define the abscissa once in l. 221 (cumulative path length or net displacement), use "velocity versus travel distance curve" in l. 23, l. 221, l. 225, l. 227, l. 234 and l. 474, and give all panels of Fig. 5 the same axis title. |
| Status | verified (wording; axis titles on the page images p. 4 and 12); inferred (that the two quantities differ for rebounding blocks) |
| Severity | moderate |
| Source | S2, S4, AB |

**GB-28 Two red markers in Fig. 5a are not local maxima, which contradicts the manuscript's own definition of effective collisions, and the plotted velocity becomes negative.**

| Field | Content |
|---|---|
| Check | P5 |
| Location | Fig. 5a (p. 12, l. 235); p. 11, l. 220 to 226 |
| Quotation | "Significant local maxima are defined as points whose velocity markedly exceeds that of their neighbors." |
| Concern | Measured on the page image (y axis 14.6 px per m/s; x axis 0 to 600 m over 264 px): the red marker at about 243 m (13.0 m/s) is followed at about 262 m by an unmarked point at 13.4 m/s, and the red marker at about 464 m (4.2 m/s) is followed by points rising to about 5.0 m/s. Neither marker exceeds its neighbours. Near 580 m the curve drops to about minus 0.34 m/s, so the plotted quantity is signed, possibly a velocity component; Eq. (2) uses v(ti), and Table 2 lists Velocity-X, Velocity-Y and Velocity-Z. Question to the authors: is the speed (magnitude) or a component used for KE and for the peak detection? |
| Suggestion | Correct the markers in Fig. 5a or explain the rule they follow, and state in Sects. 2.2 and 2.3 whether speed or a component is used. |
| Status | verified (measured on the page image, confirmed visually in the merge); assumption (use of a component), posed as a question |
| Severity | moderate |
| Source | SD |

**GB-29 The zoomed insets of Fig. 5c (threshold 20 %) and Fig. 5d (threshold 30 %) are pixel-identical, so the figure does not show what changes between the two thresholds in this window.**

| Field | Content |
|---|---|
| Check | P3 |
| Location | Fig. 5c and Fig. 5d, insets for a travel displacement of 1550 to 1830 m (p. 12, l. 236) |
| Quotation | "At a threshold of 30%, however, the identification of effective collisions is deemed acceptable." |
| Concern | Fig. 5 is the only evidence for the choice of 30 %. Insets aligned on their own axes and compared pixel by pixel over 170 x 305 px: mean absolute RGB difference 0.00, red marker pixels 799 and 799, pixels red in only one inset 0. For comparison, (b) against (c) differ in 478 red pixels, (d) against (e) in 168, (e) against (f) in 546. Outside the inset the main plots of (c) and (d) differ (964 and 497 red pixels). An identical inset is possible if both thresholds flag the same peaks in this window, but then the inset of (d) adds nothing to the comparison; if the inset of (c) was copied into (d), the visual argument for 30 % rests partly on a duplicate. |
| Suggestion | Question to the authors: were the insets of Fig. 5c and Fig. 5d generated separately? If yes, state in the caption that both thresholds select the same peaks between 1550 and 1830 m; if not, replace the inset, and add the number of detected peaks per threshold to each panel. |
| Status | verified (identity of the insets, measured); assumption (cause) |
| Severity | moderate |
| Source | AB |

**GB-30 Labels in Fig. 5, Fig. 7, Fig. 9, Fig. 10, Fig. 11 and Fig. 12 are smaller than 6 pt at print size.**

| Field | Content |
|---|---|
| Check | P29 |
| Location | Fig. 5 (p. 12); Fig. 7 (p. 17 to 18); Fig. 9 (p. 21 to 22); Fig. 10 (p. 23); Fig. 11 (p. 23 to 24); Fig. 12 (p. 25) |
| Quotation | "Fig11. Comparison of the overall envelope fitting of the landslide at 10 different times and the shape of the landslide mass in numerical simulation" |
| Concern | Cap height of digits measured on 300 dpi page images (method error ± 0.6 pt): Fig. 5 inset ticks 2.7 pt, main x numbers 3.7 pt, y numbers 4.7 to 5.3 pt; Fig. 7 axis numbers 4.7 to 5.0 pt; Fig. 9 ticks 5.0 pt; Fig. 10a 3.7 pt, Fig. 10b 4.7 pt; Fig. 11 axis numbers 2.8 to 3.0 pt; Fig. 12 axis numbers 4.7 pt, annotations "1116.8" and "29.47" 3.0 pt. All lie below 6 pt even with the method error. |
| Suggestion | Enlarge tick labels, axis titles and annotations of Fig. 5, Fig. 7, Fig. 9, Fig. 10, Fig. 11 and Fig. 12 to at least 7 pt at print size; for Fig. 11 consider fewer panels per page. |
| Status | verified (measured) |
| Severity | minor |
| Source | AB |

**GB-31 Energy conservation of the whole mass is an identity of Eq. (4), so it is not a result, and the reported non-conservation of single blocks contradicts the same identity.**

| Field | Content |
|---|---|
| Check | P23, P15, P31, P3 |
| Location | p. 13, l. 249 (Eq. 4); p. 12, l. 245 (Eq. 1); p. 19, l. 375 to 377 and l. 388 to 389; p. 20, l. 393 to 396 and l. 399 to 402; p. 1, l. 26 to 28; p. 25, l. 476 to 479; p. 26, l. 480 to 482; Fig. 8 (p. 20); Fig. 9 (p. 21 to 22) |
| Quotation | "It is evident that, due to the law of energy conservation, the total sum of the three forms of energy remains constant throughout the landslide."; "This can be regarded as a successful energy extraction numerical simulation."; "unlike the total landslide mass, the energy of single blocks is not conserved"; "for the whole landslide, its energy change conforms to the law of conservation of energy" |
| Concern | The manuscript states all three energy terms explicitly, which makes the balance checkable. With ME = KE + PE (Eq. 1) and DE(ti) = ME(t0) minus ME(ti) (Eq. 4), KE + PE + DE = ME(t0) at every time and for any mass, for the whole sliding mass and for every block alike (checked symbolically and with random values in Python). The figures show exactly this: the stack top of Fig. 8 is 6506.8 GJ in every one of the 103 measured bars from 3.7 s to 131 s (range 6468.5 to 6506.8 GJ, the two lower values in the first two bars, where DE is below one pixel), and the stack tops of all ten panels of Fig. 9 are constant within 0 to 3 px (5.057, 5.128, 4.012, 3.545, 11.060, 6.585, 1.178, 4.363, 1.593 and 0.946 GJ for blocks 1 to 10). (i) The whole-mass statement in the Abstract (l. 26 to 27), Sect. 3.2.1 and Conclusion 3 cannot fail, and "successful energy extraction" (l. 389) is not a check. (ii) The single-block statement "not conserved" (l. 394, l. 480) contradicts the identity, since the Fig. 9 stacks are flat as well; what Sect. 3.2.2 observes is that the residual DE of some blocks decreases at times, i.e. their mechanical energy rises (l. 399 to 402). The manuscript attributes these decreases to "the calculation method used" (l. 400) and at the same time to collisions with neighbouring blocks (l. 401 to 402), without separating the two. (iii) Because DE is a residual, it also absorbs the energy put in by the seismic loading at the base and removed by the viscous boundaries (l. 196 to 199), so it is not a measure of dissipation alone. Major, because the first two results of the Abstract rest on this balance. |
| Suggestion | In Sect. 2.3 compute the dissipated energy independently of Eq. (4), from frictional work at contacts and damping, together with the work done by the seismic input and at the boundaries, and show the closure error ME(t0) + W_input minus (KE + PE + DE_independent) over time for the whole mass (Fig. 8). For single blocks add the cumulative work of contact forces W_c(t), so that ME(t0) + W_c(t) = KE + PE + DE (Fig. 9). Rephrase the Abstract (l. 26 to 28), l. 375 to 377, l. 388 to 389, l. 393 to 396 and Conclusion 3 accordingly, for example: "the mechanical energy of individual blocks temporarily increases through work done by neighbouring blocks". |
| Status | verified (identity from Eq. 1 and 4; constant stack tops measured on Fig. 8 and Fig. 9); inferred (that DE contains seismic input and boundary work) |
| Severity | major |
| Source | S3, S4, AB, SD |

**GB-32 The energy magnitudes of Fig. 8, Fig. 9 and Fig. 12 cannot be reproduced from the stated mass, maximum velocity and potential energy datum.**

| Field | Content |
|---|---|
| Check | P23, P1, P3 |
| Location | p. 13, l. 252 to 255; Fig. 8 (p. 20); Fig. 9 (p. 21 to 22); Fig. 12 (p. 25); p. 9, l. 182; p. 16, l. 330; Table 1 and Table 2 (p. 11 and 13); p. 19, l. 378 |
| Quotation | "the potential-energy calculation uses the model’s initial height as the reference datum rather than true sea level; only the change in potential energy due to relative displacement is considered"; "Initially, the rock mass had not started to slide and therefore stored only potential energy."; "the maximum velocity reached 31.6 m/s" |
| Concern | Mass from the manuscript: 317563 m³ (l. 182) x 2300 kg/m³ (Table 1, landslide mass) = 7.304 x 10^8 kg (Python). (1) Kinetic energy: with no block faster than 31.6 m/s (l. 330), KE of the whole mass is at most 0.5 x 7.304e8 x 31.6² = 364.7 GJ. Fig. 8 shows a KE maximum of 1685.4 ± 19 GJ at 13.6 s (measured; root mean square velocity 67.9 m/s, 4.6 times the bound), and Fig. 12 marks a KE peak of 1116.8 GJ (55.3 m/s, 3.1 times the bound). (2) Potential energy: Fig. 8 starts at 6506.8 GJ, a mean drop of 908 m for this mass, more than the vertical extent of the modelled mass plus its height above the river (747 + 131 = 878 m, l. 174 to 175); with 2400 x 10^4 m³ the mean drop would be 12 m, while the KE maximum would then correspond to 7.8 m/s. (3) Datum: the initial energy of each monitored block (Fig. 9) divided by ρgV (V from Table 2) gives drops from 30 m (block 7) to 316 m (block 5); block 1 (z = 340 m, 939.9 m³) implies 238 m and block 10 (z = 755 m, 967.8 m³) 43 m, i.e. reference elevations of 102 m and 712 m. PE reaches 0 in all ten panels and rises again only for blocks 1 and 3. Under the datum of l. 254 PE(t0) would be 0 for every block and PE would turn negative; a common fixed datum would give one reference elevation. The data fit a datum at each block's own lowest position, so PE values of different blocks are not comparable. Possible resolutions: (A) the energies were computed with another mass than stated; (B) the volume in l. 182 is misreported (GB-18); (C) block velocities exceeded 31.6 m/s, so that the maxima of Sect. 3.1 are understated; (D) the datum differs from l. 254. The mass and datum actually used decide between them. Major, because the energy magnitudes are the quantitative results of Sect. 3.2 and would change under A, B or D. |
| Suggestion | State in Sect. 2.3 the mass used for Fig. 8 (volume, density, number of landslide blocks), the datum used for PE in Fig. 8 and Fig. 9, and the time step of the bars; check Fig. 8, Fig. 9 and the label 1116.8 GJ against 0.5 m v² and m g Δh; recompute Fig. 8 and Fig. 9 with one datum and the stated mass, or correct the volume in l. 182 or the maximum velocities in Sect. 3.1. Add to Sect. 3.2 a short table with initial PE, mass and implied mean drop for the whole mass and each monitored block. |
| Status | verified (the stated datum contradicts the shapes of Fig. 8 and Fig. 9 on the page images; printed values); inferred (energies measured on the page images; bounds and drops computed with Python) |
| Severity | major |
| Source | S3, AB, SD |

**GB-33 The position labels of the monitoring zones in Fig. 6 are swapped relative to Table 2, the points carry no IDs, and the coordinates of Table 2 use a frame different from Fig. 6.**

| Field | Content |
|---|---|
| Check | P38, P4, P3 |
| Location | p. 13, l. 256 to 257; Fig. 6 (p. 14, caption l. 268); Table 2, columns Position and Coordinate (p. 13, l. 267); Fig. 10a legend (p. 23) |
| Quotation | "As shown in Fig6., ten monitoring points were installed in the lower, lower-middle, upper-middle, and upper portions of the slide mass" |
| Concern | Table 2 orders the groups consistently with elevation: bottom IDs 1 and 2 (z = 340 and 355 m), lower middle part IDs 3 to 5 (z = 465 to 498 m), upper middle part IDs 6 to 8 (z = 660 to 692 m), top IDs 9 and 10 (z = 752 and 755 m). Fig. 6 shows the same four bands with 2, 3, 3 and 2 points, but reads from upslope down "Top", "Lower middle part", "Upper middle part", "Bottom", so the two middle labels are swapped. The text (l. 256) uses "lower" and "upper" for the classes that Table 2 and Fig. 6 call "bottom" and "top". The points carry colours but no IDs and there is no legend, and the colours do not follow Fig. 10a (the marker in the "Top" zone is red, while red is ID 1, a bottom block, in Fig. 10a). Table 2 gives coordinates such as (-79,-284,340) and (-719,120,755) with negative x and y, which cannot be located on the Fig. 6 axes. Moderate, because the position labels carry the lower and upper comparison of the Abstract and Conclusion 4 (GB-43). |
| Suggestion | Swap the labels "Lower middle part" and "Upper middle part" in Fig. 6; use the same four position terms in l. 256, Table 2 and Fig. 6; write the ID next to each point and use the colours of Fig. 10a; state the origin of the coordinate system of Table 2 or give the coordinates in the frame of Fig. 6. |
| Status | verified (labels, bands and point counts on the page image p. 14; z values from Table 2) |
| Severity | moderate |
| Source | S2, S4, AB, SD |

**GB-34 The announced stability, stress and displacement outputs are not reported, so the stated static equilibrium and post-failure stability are not shown.**

| Field | Content |
|---|---|
| Check | P11, P31 |
| Location | p. 13, l. 258 to 263; Table 2, row ID 11 and column Monitoring contents (p. 13); p. 10, l. 199 to 202; p. 15, l. 301 to 302; Fig. 7g to 7n (p. 18); p. 16, l. 346 to 347 |
| Quotation | "the maximum unbalanced force was tracked to verify that the model reached post-failure stability"; "displacement, velocity, and stress histories were extracted for each of the ten monitored blocks" |
| Concern | Announced outputs against Sect. 3: maximum unbalanced force (Table 2, ID 11), no history, value or criterion, and no step at which static equilibrium was reached before the dynamic loading (l. 199 to 202); stress histories of the ten blocks (Stress-XX, Stress-YY, Stress-ZZ), not reported; global stress, maps shown in Fig. 7h to 7n, but Sect. 3.1 gives no stress value, and the only stress wording in Sect. 3 is "dynamic interface stress effects" (l. 312); global displacement, no values. At 131 s the colour bar of Fig. 7g shows a maximum velocity of 0.21 m/s, not zero, so the end state described as "approached 0 m/s" (l. 346 to 347) is not backed by the stability criterion the methods announce. |
| Suggestion | Report in Sect. 2.3 or 3.1 the unbalanced-force history for the static and dynamic stages with the convergence criterion, add one sentence per stage on the stress maps (range and location of maxima), and report the stress histories of Table 2 or remove them from Table 2 and l. 262 to 263. |
| Status | verified |
| Severity | moderate |
| Source | S3, SD |

**GB-35 The body enclosed by the alpha-shape envelope is called accumulation area, deposition zone, slide mass, landslide mass, landslide body and deposit mass, although V0 and S0 refer to the mass at the start, before any deposit exists.**

| Field | Content |
|---|---|
| Check | P38 |
| Location | p. 14, l. 269 to 272 and l. 278 to 279; p. 1, l. 24; p. 3, l. 88; Fig. 1 (p. 4); p. 23, l. 427 and l. 429; p. 24, l. 449; p. 26, l. 491 |
| Quotation | "2.4 Structural extraction of landslide accumulation area"; "surface area of the deposition zone. An alpha-shape algorithm is applied to the slide mass"; "on the deposit mass at 10 representative time points" |
| Concern | One object, the point set enveloped at each time, has six names: "landslide accumulation area" (l. 88, l. 269, Fig. 1), "deposition zone" (l. 270, l. 272), "slide mass" (l. 272), "landslide mass" (l. 89, l. 278, l. 279), "landslide body" (l. 24), "deposit mass" or "deposit region" (l. 427, l. 429, l. 449, l. 491). The names are not equivalent: a deposition zone exists only after runout, while Eq. (5) and (6) start from V0 and S0 of the landslide mass, and Fig. 11a is an envelope at t = 0 s (l. 438). A reader cannot tell whether the envelope encloses all blocks of the sliding mass at every step or only blocks that have come to rest, and VS and AG differ between the two readings. Moderate, because the object of VS and AG cannot be reconstructed without it. |
| Suggestion | State in l. 272 which blocks enter the alpha shape (for example "all blocks of the sliding mass at time t"), use that one name in l. 24, l. 88, l. 269, l. 270, l. 427, l. 429, l. 449, l. 491 and in Fig. 1, and rename the heading of Sect. 2.4 accordingly. |
| Status | verified (wording and counts); inferred (that the two readings give different VS and AG) |
| Severity | moderate |
| Source | S2 |

**GB-36 The two dimensionless indices and the area symbol carry several names: "volume swelling (VS)" and "area growth (AG)" in Sect. 2.4 and Fig. 12, "volume expansion rate" and "(surface) area growth rate" elsewhere, and the area is S in Eq. (6) but A in l. 440.**

| Field | Content |
|---|---|
| Check | P38 |
| Location | p. 14, l. 274 to 275; p. 14, l. 276 to 280 (Eq. 5 and 6); p. 1, l. 25; p. 3, l. 89; p. 15, l. 288; p. 24, l. 440 to 441; p. 25, l. 453 to 454; Fig. 12, axis titles and caption (p. 25, l. 458 to 459); p. 26, l. 488 |
| Quotation | "two dimensionless indices are introduced: volume swelling (VS) and area growth (AG)"; "we first extracted its volume (V) and surface area (A) at each time point"; "the volume expansion rate (VS) and surface area growth rate (AG) were calculated"; "(a) as a function of volume; (b) as a function of area." |
| Concern | Sect. 2.4 defines both indices as relative changes in percent (Eq. 5 and 6). Names counted with Python: volume index "volume swelling" 2 (l. 275, l. 288) plus Fig. 1 and the Fig. 12a axis "Volume Swelling (%)", "volume expansion rate" 4 (l. 25, l. 89, l. 441, l. 453), "volume expansion" 1 (l. 488); area index "area growth" 2 (l. 275, l. 288) plus Fig. 1 and the Fig. 12b axis "Area Growth (%)", "area growth rate" 1 (l. 25), "surface area growth rate" 2 (l. 89, l. 441), "surface area growth" 2 (l. 453, l. 488). That Fig. 12 labels its axis "Volume Swelling" while l. 453 reads the same 29.47 % as "volume expansion rate" confirms that both names denote one object. "Rate" suggests a change per unit time, which Eq. (5) and (6) do not compute. The area is S0, St in Eq. (6) but A in l. 440, and the Fig. 12 caption says "as a function of volume" and "of area", while the axes show VS and AG. |
| Suggestion | Use "volume swelling (VS)" and "area growth (AG)" throughout (l. 25, l. 89, l. 441, l. 453, l. 488); write "surface area (S)" in l. 440; change the caption of Fig. 12 to "(a) as a function of volume swelling (VS); (b) as a function of area growth (AG)". |
| Status | verified (wording in the text and on the page images p. 4, 14 and 25; counts with Python) |
| Severity | minor |
| Source | S2, S3, S4, AB |

**GB-37 The alpha-shape envelope uses α = 1 without unit, point set or sensitivity analysis, although the manuscript states that α directly affects volume and area.**

| Field | Content |
|---|---|
| Check | P8, P31 |
| Location | p. 14, l. 281 to 284; p. 14, l. 272 to 273; p. 24, l. 440 to 444; Fig. 11 (p. 23 to 24); Fig. 12 (p. 25) |
| Quotation | "Considering that the choice of the alpha parameter (α) in the Alpha Shape algorithm directly affects the accuracy of the envelope fitting as well as the computed volume and surface area, this study uniformly sets the α value to 1. This approach ensures a tight fit of the envelope model while minimizing geometric deviations introduced by parameter tuning." |
| Concern | (1) The unit or convention of α (a radius in metres or its inverse) and the point set (block centroids or vertices) are not stated, and no implementation is named; the blocks are 8.7 m wide (l. 178). (2) "ensures a tight fit" is not measured: the envelope at t = 0 is not compared with the known mass volume, and it is unclear whether V0 (l. 278) is that envelope or the mass volume. (3) The manuscript tests the prominence threshold (Fig. 5b to 5f) but not α, which it calls equally decisive. In Fig. 12, VS reaches about 1250 % and AG about 4300 % (axis readings), so the envelope volume grows to about 13.5 times its start and encloses large voids. The sampling times of Fig. 12 are treated in GB-45. |
| Suggestion | In Sect. 2.4 define α with unit and point set, name the implementation, report VS and AG for at least three α values, and compare the envelope at t = 0 with the mass volume. |
| Status | verified (1 and 2); inferred (3, values read from the axes) |
| Severity | moderate |
| Source | SD |

#### Minor corrections

| ID | Location | Quotation | Replacement | Source |
|---|---|---|---|---|
| KK-11 | p. 2, l. 76; p. 5, l. 93; p. 15, l. 301 and all other figure references and captions | "As shown in Fig1."; "As shown in Fig2."; "Fig7 illustrates" | "As shown in Fig. 1"; "As shown in Fig. 2"; "Fig. 7 illustrates" (one form throughout) | S4 |
| KK-12 | p. 5, l. 97 | "Kangding County to the West" | "Kangding County to the west" | S4 |
| KK-13 | p. 5, l. 98 | "Y" - shaped faults | "Y-shaped faults" | S4 |
| KK-14 | p. 5, l. 110 to 111 | "burst the Dadu River after 9 days. The sudden flood made the downstream area a vast ocean" | "dammed the Dadu River; the dam breached after 9 days, and the outburst flood inundated the downstream area" | S4 |
| KK-15 | Fig. 2b, legend (p. 6) | "Daduhe River" | "Dadu River", as in Fig. 2c, Fig. 3 and the text | S2, AB |
| KK-16 | p. 6, l. 130 to 131 | "According to the DEM data obtained by UAV scanning" | "According to the digital elevation model (DEM) data obtained by unmanned aerial vehicle (UAV) scanning" (first use in the methods) | S2 |
| KK-17 | p. 6, l. 132 to 133; p. 7, l. 159 | "Convert the geographical coordinate system to the projection coordinate system"; "make a section along" | "The geographic coordinates were converted to a projected coordinate system"; "a section was drawn along" | S4 |
| KK-18 | p. 7, l. 152; p. 9, l. 182 | "1120 m-1330m"; "1121m high" | "1120 to 1330 m"; "1121 m high" | S4 |
| KK-19 | p. 7, l. 153, l. 154 and l. 156 | "; The elevation" (three times) | "; the elevation" | S4 |
| KK-20 | p. 10, l. 193 to 195 | "In the course of a discrete-element simulation-particularly when modeling nominally semi-infinite bodies such as the use of fixed or elastic boundaries in a static analysis will inevitably reflect outbound seismic waves into the model" | "In a discrete-element simulation, particularly of nominally semi-infinite bodies, fixed or elastic boundaries used in a static analysis will inevitably reflect outgoing seismic waves back into the model" | S4 |
| KK-21 | p. 11, l. 218 and l. 228 | "block velocities-hereafter termed"; "must be chosen-one that quantifies" | "block velocities, hereafter termed"; "must be chosen, one that quantifies" | S4 |
| KK-22 | Fig. 5a, legend (p. 12) | "Non-obvios acceleration" | "Non-obvious acceleration" | AB |
| KK-23 | p. 13, l. 246 | "where, at time ti, PE(ti), and DE(ti) can be expressed as:" | "where, at time ti, KE(ti), PE(ti), and DE(ti) can be expressed as:" | S4, SD |
| KK-24 | p. 13, l. 251 | "(m/s);h(ti)" | "(m/s); h(ti)" | S4 |
| KK-25 | p. 13, l. 267 (Table 2 title and row ID 11) | "Table 2: The basic information of blocks where the 10 monitoring points are located" | "Table 2: Blocks carrying monitoring points 1 to 10, and global monitoring item 11 (maximum unbalanced force)" | S2 |
| KK-26 | p. 14, l. 272; p. 1, l. 23 | "An alpha-shape algorithm"; "the Alpha shape algorithm" | one spelling throughout, for example "alpha shape" (l. 281, l. 426 and Fig. 1 have "Alpha Shape") | S2 |

#### Verification log

| ID | Check | Checked | Values | Result |
|---|---|---|---|---|
| PP-06 | P10, P19 | Design sketch: study type, cases, comparison, data sources | single case, numerical (3DEC) with terrain reconstruction; one landslide (1786), one run of 131 s, 25345 blocks, 10 monitored blocks, 1,139 effective collisions, 10 envelope times; no comparison condition (no second input motion, parameter set, threshold count, alpha value or case); data sources: UAV DEM (date and resolution not stated), restored terrain, geological map, Luding record, Table 1 parameters, simulation output, field findings (not reported), photographs (Fig. 7o), tablet | design sketch complete; feeds GB-02, GB-14, GB-16, GB-22 to GB-24, GB-26, GB-31 to GB-34, GB-37, GB-41, GB-43, GB-46 |
| PP-07 | P13, P38, P2 | Year, name and magnitude of the trigger | 1786 in l. 38, l. 110, l. 183, l. 354; "Ms7 ¾" (l. 110) = 7.75; Zhao et al. (2021) title "1786 Moxi M 7.75 earthquake" (l. 600 to 601); Zhou et al. (2024) abstract Ms 7.75; Wu et al. (2013) abstract Ms 7.7 (rounded); "Kangding earthquake" in l. 110, l. 183, l. 188 | no finding; the naming difference to the listed title is taken up in GB-24 |
| PP-08 | P1 | Plan area, p. 7, l. 149 to 150 | 450 m x 1000 m = 450 000 m² = 0.45 km², stated 0.45 km² | no finding (volume in GB-18) |
| PP-09 | P3 | Fig. 2c: sliding direction and width against l. 149 | azimuth of the section line 74.4° (text 75°); north to south extent of the boundary 964 m; width of Q4del 987 m (text about 1000 m); scale 0 to 600 m = 273.3 px | no finding (outline assignment in GB-18) |
| PP-10 | P3 | Fig. 3b: slopes along the profile against l. 153 to 156 | 50 to 200 m: 58° (text wall 57°); 200 to 550 m: 31° (colluvium 35°); 550 to 800 m: 13° (platform 5 to 12°); 880 to 960 m: 45° (front edge 50°); horizontal 0.552 px/m, vertical 0.542 px/m, no vertical exaggeration | no finding for the slopes; absolute elevations in GB-20 |
| PP-11 | P3 | Scale bars of Fig. 3a and Fig. 3c | Fig. 3a: five segments of 35.75 px, labels 0, 400, 1000 m consistent with 200 m per segment; Fig. 3c: 0, 400, 800, 1400 m at 44, 44, 68 px, proportional | no finding (perspective caveat in GB-17) |
| PP-12 | P36 | Approximate statements against the manuscript's own records | relief 747 + 131 = 878 m (l. 174 to 175) against 2000 minus 1120 = 880 m (l. 151, l. 156); "nearly 20 large and super large earthquake landslides" (l. 99 to 100) has no own record to compare | no finding (volume in GB-18) |
| PP-13 | P3 | Fig. 4 labels against the text | "1021m", "747m", "179m", "131m" equal l. 174 to 175; axes compatible with the model size 2788 x 3341 m (l. 181 to 182) | no finding |
| PP-14 | P38 | Fault names | "Dadu River fault (Detuo fault)" (l. 147) with explicit alias; "reverse fault" (l. 146) and "Reverse fault" in Fig. 3b; "Fault" in Fig. 2c and Fig. 3a | no finding |
| PP-15 | P38 | Software and parameter names | "three-dimensional discrete element program (3DEC)" defined in l. 168 to 169; α = 1 in l. 283 and Fig. 1; threshold 30 % in l. 232 and Fig. 5d | no finding (spelling of alpha shape in KK-26) |
| PP-16 | P1 | Elastic constants of Table 1 | Poisson's ratio from (3K minus 2G) / (2(3K + G)): bed rock K = 21.90, G = 15.10 GPa gives 0.220; landslide mass K = 11.90, G = 6.9 GPa gives 0.257; both within 0 to 0.5 | no finding (joint stiffness question in GB-22) |
| PP-17 | P26 | Guarantees across modes | viscous base and free-field lateral boundaries in the dynamic stage (l. 196 to 199); velocity restraints in the static stage (l. 201 to 202), consistent | no finding; "ensures" claims at l. 283 and l. 471 in GB-37 and GB-41 |
| PP-18 | P2 | Prominence thresholds in text and Fig. 5 | l. 230 to 232: 10, 20, 30, 40, 50 %; caption l. 238 to 239: the same five values; chosen 30 % = panel (d) | no finding |
| PP-19 | P3 | Fig. 5 marker counts | (a): 6 red and 5 purple markers, consistent with "red or purple markers" (l. 222); (b) to (f), red pixels in inset and main plot: 1231 and 2646, 799 and 964, 799 and 497, 631 and 426, 85 and 416; monotonic decrease with the threshold as stated in l. 230 to 232 | no finding (identical insets in GB-29) |
| PP-20 | P38 | Energy abbreviations | KE, PE, DE, ME defined in l. 241 to 243, used in Eq. (1) to (4), l. 287, l. 290, l. 442, Fig. 1 and the Fig. 12 legends | no finding apart from KK-02 and GB-10 |
| PP-21 | P38, P2 | Names, number and grouping of the monitored blocks | "monitoring point(s)" 6 times, "monitored block(s)" 6 times; Table 2 title links points and blocks; "ten" (l. 256, l. 262), "10" (l. 392, l. 403); Table 2 IDs 1 to 10 plus 11; groups of 2, 3, 3, 2 with z 340 to 355, 465 to 498, 660 to 692, 752 to 755 m; Fig. 9 ten panels; Fig. 10a ten legend entries | no finding (labels of Fig. 6 in GB-33; ID 11 in KK-25) |
| PP-22 | P5 | The manuscript's own rules against its own examples | Table 2 z values ordered by zone; Fig. 6 has 2, 3, 3, 2 points per zone as in Table 2; α = 1 in Fig. 1 and l. 283; 30 % used in Fig. 5d | no finding beyond GB-28 and GB-33 |
| PP-23 | P38 | Names of the moving body in general | "landslide mass" 27, "sliding mass" 9, "slide mass" 3, "landslide body" 1; Fig. 4 "Sliding mass" | no finding beyond GB-35 |
| PP-24 | P20 | Denominators of VS and AG | Eq. (5) and (6), l. 276 to 280: VS relative to V0, AG relative to S0, both initial values of the landslide mass | no finding on the definition (values of V0 and S0 in GB-45) |
| PP-25 | P7 | Whether the described method applies to all reported data | one model, one run; no version, protocol or instrument change mentioned; Fig. 7 and Fig. 11 from the same run (shared times 0, 3, 7, 9, 12, 15, 131 s) | no finding |
| PP-26 | P37 | Post-hoc corrected data in figures | noise reduction, cavity repair and normal correction (l. 133 to 135, l. 141 to 143) labelled "Terrain before repair" and "Terrain after repair" in Fig. 3c | no finding |
| PP-27 | P17 | Each disclosed limitation against the place where the method is introduced | structural planes (l. 175 to 178), seismic proxy (l. 183 to 191), smooth terrain (l. 160 to 162), tablet (l. 136 to 138) and PE datum (l. 252 to 255) in place; dam break (l. 348 to 350) in the results; deposit-area restoration only in l. 466 to 468 | finding only for the deposit area (GB-16); consequences in GB-23, GB-24, GB-41 |
| PP-28 | P19 | Provenance class of the core statements | energy, velocity and collision results are model generated and called numerical simulation in the Abstract (l. 18 to 20) and in Sect. 3 | no finding for the model class; field class in GB-14, seismic proxy in GB-24 |
| PP-29 | P29 | Font size of figures not covered by GB-30 | cap heights: Fig. 1 6.7 pt; Fig. 3c scale bar 6.7 pt; Fig. 4 accelerogram numbers 6.0 pt; Fig. 6 axis numbers 6.7 pt; Fig. 8 axis numbers 7.7 pt; rotated contour labels of Fig. 2c and Fig. 3c not measured | no finding |

### Segment 3: Results (p. 15 to 25)

#### Substantive findings

**GB-38 Fig. 7 does not say which stress component and which section are shown, gives only end values on the colour bars, and the validation panel (o) lacks time step, scale and viewing direction.**

| Field | Content |
|---|---|
| Check | P29 |
| Location | p. 15, l. 301 to 302; Fig. 7a to 7o (p. 17 to 19); Fig. 7 caption (p. 19, l. 368 to 370) |
| Quotation | "Fig7 illustrates the cloud maps of velocity distribution for the overall model and stress distribution along the sliding plane" |
| Concern | Panels (h) to (n) are labelled only "Stress"; the component (vertical, maximum principal, von Mises) is not given, and they show a vertical section of the whole model, not a distribution "along the sliding plane" as l. 302 says. Every colour bar shows only its two end values (for example "0m/s" and "5.9m/s"), and the range changes from panel to panel (velocity 0 to 31.6 m/s, stress 0 to minus 47 MPa), so colours cannot be compared across panels. In (a) the whole model is red, the colour of the maximum, although the bar runs from 0 to 0 m/s. Panel (o) compares a simulation view with two photographs but gives no time step of the simulation, no scale and no viewing direction (origin of the photographs in GB-14). |
| Suggestion | Name the stress component and the position of the section in the caption; give intermediate ticks on the colour bars or use one common range per row; show (a) in the colour of 0 m/s; add time step, scale and viewing direction to (o). |
| Status | verified (page images p. 15, 17 to 19) |
| Severity | minor |
| Source | AB |

**GB-39 Stages, times and energy events are named differently in Sect. 3.1 and Sect. 3.2.1, and the reader must use the Fig. 7 caption to date them.**

| Field | Content |
|---|---|
| Check | P22 |
| Location | p. 15, l. 304 to 324; p. 16, l. 325 to 347; Fig. 7 caption (p. 19, l. 368 to 369); p. 19, l. 378 to 384; p. 25, l. 453 to 455; p. 26, l. 484 |
| Quotation | "As shown in Fig7. (d) and (k), during the collapse stage, the maximum velocity reached 27.1 m/s."; "From 3 to 12 seconds, the landslide experienced rapid initiation"; "Around 13 seconds, the sliding mass impacted the riverbed" |
| Concern | Sect. 3.1 gives no times; they follow only from combining panel letters with the caption: (b) 3 s tension cracking, (c) 7 s high-speed initiation, (d) 9 s collapse, (e) 12 s impact at base, (f) 15 s impact and disintegration, (g) 131 s damming. Sect. 3.2.1 calls 3 to 12 s "rapid initiation", which covers three stages of Sect. 3.1 (7, 9 and 12 s), and dates the riverbed impact at about 13 s, between stage (e) "upon arrival at the valley floor" (l. 337, 12 s) and stage (f) "Upon reaching the Dadu River valley" (l. 339, 15 s). The times of the KE peak and of VS = 29.47 % are not given. Conclusion 4 refers to "the collapse stage", which the reader can date only through the caption (9 s). |
| Suggestion | Add to Sect. 3.1 a stage table (stage, panel, time, maximum velocity, KE, VS, AG) and use the same stage names and times in Sect. 3.2.1, Sect. 3.4 and Conclusion 4. |
| Status | verified |
| Severity | minor |
| Source | S3 |

**GB-40 The stage description has the "entire" mass impacting by 12 to 13 s, but Fig. 8 shows about two thirds of the potential energy still present then, and no snapshot covers 15 to 131 s.**

| Field | Content |
|---|---|
| Check | P6, P34 |
| Location | p. 16, l. 330 to 331; p. 19, l. 381 to 384; Fig. 8 (p. 20); Fig. 7 caption (p. 19, l. 368 to 369); Fig. 11 caption (p. 24, l. 438 to 439) |
| Quotation | "After a brief airborne trajectory, the entire landslide mass collided with the ground."; "From 3 to 12 seconds, the landslide experienced rapid initiation, and the entire sliding mass abruptly descended along the sliding plane." |
| Concern | Measured on the Fig. 8 bars, PE is 68.2 % of its initial value at 12 s, 65.0 % at 13 s, 64.7 % at 15 s and 4.7 % at 60 s, so 60.0 percentage points of the initial PE are released between 15 and 60 s (Python). Fig. 7 shows 0, 3, 7, 9, 12, 15 and 131 s, with no snapshot in the interval where most energy is converted, and no rule for choosing the times is given; Fig. 11 uses 32, 71 and 100 s, so such states exist. Moderate: the energy and collision conclusions stand even if the finding holds. |
| Suggestion | Add velocity and stress snapshots at, for example, 30, 45 and 60 s to Fig. 7 and describe this stage in Sect. 3.1; in l. 331 and l. 381 to 382 replace "the entire landslide mass" by "the front of the landslide mass", or state the share of the mass in motion. |
| Status | verified (text, snapshot times); inferred (PE shares measured on Fig. 8) |
| Severity | moderate |
| Source | SD |

**GB-41 The validation against the field is qualitative and uses the present, post-breach deposit, yet Conclusion 2 states that it "ensures" agreement with actual conditions.**

| Field | Content |
|---|---|
| Check | P11, P15, P9, P32 |
| Location | p. 16, l. 353 to 359; Fig. 7o (p. 19); p. 25, l. 471 to 472; p. 15, l. 299; p. 16, l. 348 to 350; p. 5, l. 110 to 111; p. 7, l. 149 to 156 |
| Quotation | "Fig7. (o) presents compelling evidence of agreement between the numerical simulation results and the actual field observations."; "the extent and morphology of the accumulated landslide material in the simulation closely match those observed in reality"; "Comparison with field imagery and result analysis ensures that the simulation outcomes align with actual conditions." |
| Concern | The manuscript names the weathering since 1786 (l. 354 to 355) and marks two matching features in Fig. 7o: the ridge dividing the source area and the deposit extent. (1) No quantity is compared, although the field side has numbers (length 450 m, width 1000 m, area 0.45 km², toe at 1120 m, platform at 1330 to 1380 m, l. 149 to 154) and the UAV DEM (l. 130 to 135) would allow elevation differences: no length, width, area, thickness, elevation range or dam height of the simulated deposit is reported. (2) The target is the present deposit. The dam burst "after 9 days" (l. 110 to 111) and the breach is not modelled (l. 348 to 350), so the simulated deposit at 131 s is pre-breach and the present one post-breach; the weathering disclosure does not draw this consequence. The listed Zhao et al. (2021) state in their abstract that river erosion split the deposit into right and left bank parts and that the dam crest stood about 130 m above the present river. (3) "successfully reproduced the entire process" (l. 299), "compelling evidence" (l. 353) and "ensures" (l. 471) rest on this qualitative comparison only; the results section itself is more cautious ("These consistencies support the validity", l. 359). None of the disclosed limitations (smooth terrain l. 160 to 162, ignored structural planes l. 175 to 178, substitute record l. 183 to 191, unmodelled breach, weathering) is carried into the conclusions. Major: all energy and collision results are transferred to the 1786 event through this statement; with a qualitative check only they remain statements about the model. |
| Suggestion | Counter-design for Sect. 3.1: compare the simulated final surface quantitatively with the present DEM in zones the breach did not reach (scarp, upslope deposit), and compare runout, deposit area and maximum dam height with Zhao et al. (2021) (dam crest about 130 m above the present river) and with the lake record of the Tiezhuang Temple tablet (l. 136 to 138); report error measures in a table "simulated versus observed". Replace "ensures" in l. 471 by "is qualitatively consistent with the field evidence" unless the measured agreement supports more, and replace "compelling" in l. 353. |
| Status | verified (no quantitative measure; the manuscript's own statements on breach and weathering; Zhao et al. 2021 abstract read via ideas.repec.org); inferred (consequence of the breach for the validation target) |
| Severity | major |
| Source | S3, S4, SD |

**GB-42 Fig. 7h shows zero stress throughout the model at t = 0 s, although the text says that the dynamic analysis starts from static equilibrium.**

| Field | Content |
|---|---|
| Check | P3 |
| Location | Fig. 7h to 7m (p. 18); Fig. 7 caption (p. 19, l. 368 to 370); p. 10, l. 199 to 200; p. 15, l. 304 to 305 |
| Quotation | "Dynamic loading must be introduced only after the model has attained static equilibrium" |
| Concern | The colour bar of Fig. 7h runs from "0" to "0Mpa" and the whole section is red, i.e. zero stress at t = 0 s. Three seconds later (Fig. 7i) the section shows a stress field that increases with depth to "-33Mpa", and (j) to (m) show similar ranges (minus 31 to minus 33 MPa). A lithostatic vertical stress at 1200 m depth is 2700 kg/m³ x 9.81 m/s² x 1200 m = 31.8 MPa (bed rock density of Table 1), which matches panels (i) to (m). If the model was in static equilibrium at the start of the dynamic phase, this gravitational field should already be present at t = 0 s. Either Fig. 7h shows the model before gravity was applied, or the plotted quantity is a stress change, in which case the colour bars of (i) to (n) need another label. |
| Suggestion | Question to the authors: does Fig. 7h show the state before or after the static stage? Replace Fig. 7h by the equilibrium stress field at the start of the dynamic phase, or state in the caption that (h) to (n) show stress changes relative to t = 0. |
| Status | verified (displayed values on the page image); inferred (interpretation) |
| Severity | moderate |
| Source | AB |

**GB-43 The Abstract and Conclusion 4 compare collisions and energy transfer between lower (front) and upper (rear) parts, but the results contain no analysis by initial position or stage, and the collision counts are not normalised.**

| Field | Content |
|---|---|
| Check | P11, P15, P21, P25, P34 |
| Location | p. 22, l. 414 to 421; Fig. 10b (p. 23); p. 1, l. 28 to 30; p. 26, l. 483 to 487; p. 3, l. 86 to 87; p. 11, l. 222 to 224; p. 13, l. 260 to 264 |
| Quotation | "Compared with the upper rock mass, the lower rock mass is compressed more frequently, receives more energy transfer, and has a longer migration distance."; "Based on the analysis of effective collisions within the entire landslide mass, it can be concluded that during the collapse stage, the front portion of the rock mass experiences more collisions than the rear portion"; "as the migration distance increases during the landslide, the number of collisions also rises continuously, reaching a peak once the blocks enter the river channel." |
| Concern | The methods announce an analysis of "effective collision frequency of different parts of landslide mass" (l. 86 to 87). The only collision result is Fig. 10b, collisions against travel distance (x axis "Travel distance (m)", l. 418 to 421). No sentence in Sect. 3 (l. 297 to 459) and no figure breaks the collisions down by initial position (bottom, lower middle, upper middle, top in Table 2) or by stage ("during the collapse stage", Fig. 7d, 9 s); no DE of rear blocks at collision instants and no energy received by front blocks is shown, so "receives more energy transfer" is not measured (see also GB-02). The methods extract velocity histories only for the ten monitored blocks (l. 262 to 264) plus overall variables of the whole mass (l. 260 to 261), so the per-block profiles needed for collisions "within the entire landslide mass" (l. 483) are not described. Exposure is not separated from rate: if each point of Fig. 10b sums the collisions of all blocks within a 100 m interval, the count depends on how many blocks are still moving there; if it relates a block's total path to its collisions, a longer path offers more opportunities. Moreover, effective collisions are by definition the peaks that "yield a substantial velocity increase and, consequently, a markedly longer travel distance" (l. 222 to 224), so the association with travel distance is partly built into the definition, and the causal claim "enabling the front portion to slide farther" (l. 487) can confuse cause and exposure. The ten monitored blocks are 0.039 % of the 25345 model blocks and 3.6 % of the modelled volume (Python), chosen by position (l. 256 to 257), and their representativeness is not checked. Major: the Abstract statement and Conclusion 4 answer the aim on energy transfer (l. 68). |
| Suggestion | Counter-design for Sect. 3.2.2: detect collisions for all blocks of the sliding mass, or for a stratified random sample (for example 100 blocks per position group), and report per position group and stage the number of effective collisions normalised by path length and by time, with dispersion, the travel distance, and the energy received (sum of positive ME increments); test the relation of initial position, normalised collision rate and runout, for example with a rank correlation. Otherwise reword the Abstract (l. 28 to 30) and Conclusion 4 (l. 483 to 487) as hypotheses. Questions to the authors: were the profiles of all blocks exported, and which reading of Fig. 10b applies? |
| Status | verified (no per-position, per-stage or normalised result; definition in l. 222 to 224; data flow in l. 260 to 264); inferred (shares of blocks and volume, Python); assumption (whether all profiles were exported; whether normalisation removes the trend), posed as questions |
| Severity | major |
| Source | S3, S4, SD |

**GB-44 The population behind the 1,139 effective collisions and behind Fig. 10b is not stated, the points of Fig. 10b add up to more than 1,139, and they do not rise continuously as the text says.**

| Field | Content |
|---|---|
| Check | P20, P3, P29 |
| Location | Fig. 10b (p. 23, l. 422 to 424); p. 11, l. 233 to 234; p. 22, l. 414 to 415 and l. 418 to 419; p. 9, l. 181 |
| Quotation | "Under this setting, 1,139 effective collisions were detected from the travel-distance versus velocity profile."; "presents the frequency of effective collisions experienced by blocks at different locations during the landslide process" |
| Concern | "the ... profile" is singular and Fig. 5a shows the curve of one block, yet the manuscript does not say whether 1,139 refers to one block, the ten monitored blocks or all landslide blocks; the number of landslide blocks is not given, and the 25345 blocks of l. 181 include the base. Fig. 10b shows 26 points at 100 m spacing from 0 to 2500 m. Read independently by two instances on the page images, they sum to 1213 and to 1216.7 ± 9.4, i.e. 74 to 78 (6.5 to 6.8 %) more than 1,139. If Fig. 10b bins the same collisions, the two counts disagree; if not, its population is undefined. The y axis "Frequency" is not defined (per bin, per block), the bin width is not stated, and the red curve is not explained (function, fit). The series falls at 800 m (16.0 to 7.0), 1000 m (27.1 to 19.9), 1300 m (30.0 to 28.2) and at 2400 and 2500 m (157.0 to 150.0 to 146.0), so "rises continuously" (l. 419) goes beyond the figure; the overall trend holds. Moderate: the major grade of the position analysis belongs to GB-43; this part concerns traceability. |
| Suggestion | In l. 233 to 234 and in the caption of Fig. 10 state the population (number of blocks), the bin width and what one count represents; title the y axis, for example "Number of effective collisions per 100 m"; make the sum of Fig. 10b equal the stated total or explain the difference; give the fitted function and its R²; mark where the river channel begins; replace "rises continuously" in l. 419 by "increases overall". |
| Status | verified (no population, bin or fit definition; non-monotonic points on the page image p. 23); inferred (sums from readings) |
| Severity | moderate |
| Source | S3, AB, SD |

**GB-45 Fig. 12 has many more sampling points than the ten envelope times stated, and its kinetic energy peak (1116.8 GJ) lies a third below the maximum of Fig. 8, so the transition values may refer to another time.**

| Field | Content |
|---|---|
| Check | P2, P3 |
| Location | p. 23, l. 426 to 427; Fig. 12a and 12b (p. 25); Fig. 11 caption (p. 24, l. 437 to 439); p. 24, l. 440; p. 25, l. 453 to 455; Fig. 8 (p. 20) |
| Quotation | "perform Alpha Shape envelope fitting on the deposit mass at 10 representative time points"; "At this point, the kinetic energy peaks" |
| Concern | l. 427 and the caption of Fig. 11 state ten envelope times (0, 3, 7, 9, 12, 15, 32, 71, 100, 131 s), and l. 440 computes VS and AG "at each time point". Counted on the page images, the DE curve of Fig. 12a carries at least 30 markers (± 3 where markers overlap near VS = 0; at least 15 above VS of about 560 %), and PE and KE after the peak match bars of Fig. 8 (PE 1750 GJ and KE 700 GJ at VS of about 105 %, against 1718.9 and 708.6 GJ in the Fig. 8 bar at 33.5 s). VS and AG were therefore evaluated at many more times than the ten of Fig. 11, and the method does not say how. The KE peak marked in Fig. 12 is 1116.8 GJ, while Fig. 8 shows 1082.1 GJ at 11.1 s, 1589.6 GJ at 12.4 s and a maximum of 1685.4 ± 19 GJ at 13.6 s; 1116.8 GJ matches no bar and lies 568.6 GJ (33.7 %) below the maximum (Python). If the true KE maximum lies later than the marked point, the transition values VS = 29.47 % and AG = 319.5 % (l. 453 to 454) refer to another time than the KE peak. The times of the points, the time of the marked peak, and V0 and S0 are not given, so the envelope volumes cannot be recovered. |
| Suggestion | State in Sect. 2.4 or 3.4 at which times VS and AG were computed for Fig. 12 and how, the time of the marked KE peak, and the values of V0 and S0; mark in Fig. 12 the point that corresponds to the KE maximum of Fig. 8 (13.6 s) and recompute the values in l. 453 to 454 for it, or explain why Fig. 8 and Fig. 12 differ. |
| Status | verified (marker count above 10 and printed label 1116.8 on the page images); inferred (Fig. 8 values, measured) |
| Severity | moderate |
| Source | S3, AB, SD |

**GB-46 Fragmentation, debris production and a solid to fluid transition are claimed, but only the envelope volume and area of the block assembly are measured, and the announced link between collisions and dilation is not reported.**

| Field | Content |
|---|---|
| Check | P15, P31, P11 |
| Location | p. 23, l. 429 to 431; p. 24, l. 445 to 452; p. 25, l. 453 to 456; p. 26, l. 488 to 492; p. 11, l. 217; p. 16, l. 325 to 328; p. 9, l. 178 to 181; Fig. 11 (p. 23 to 24); Fig. 12 (p. 25) |
| Quotation | "These newly generated fragments fill the interior and surface of the deposit mass, causing a sudden expansion of the envelope volume and a sharp increase in surface area."; "When the volume expansion rate reaches approximately 29.47% and the surface area growth reaches about 319.5%, it can be considered that the landslide transitions from a solid phase to a fluidized phase."; "To elucidate the anomalous dilation of the sliding mass" |
| Concern | The model consists of 25345 blocks cut as 8.7 m x 8.7 m columns (l. 178 to 181). No breakage or fragmentation method is described, and the results report no block count over time, no fragment size distribution and no count of broken contacts; the only measured quantities are the envelope volume and area (Fig. 11, Fig. 12). Growth of an alpha-shape envelope also results from the separation and spreading of unbroken blocks, which is what Sect. 2.4 sets out to measure ("we quantify dispersion", l. 271). "the sharp rise of DE shown in the figure further confirms significant fragmentation" (l. 451) does not hold, because DE is the residual of Eq. (4) and contains friction, damping and boundary work, not breakage energy alone (GB-31). Question to the authors: can blocks break into new blocks during the 3DEC run? If not, the "newly generated fragments" (l. 448), the "newly formed fragments" (l. 490), the "fine debris such as rock fragments" (l. 326) and the "fractured layer" about 20 m thick (l. 328) are not model outputs. No criterion for "fluidized" is defined, so 29.47 % and 319.5 % have no definition behind them, and they depend on the sampling of Fig. 12 (GB-45). Sect. 2.2 introduces effective collisions "To elucidate the anomalous dilation of the sliding mass" (l. 217), but no result relates collisions to VS or AG; Sects. 3.2.2 and 3.4 are not connected. Major: structural evolution is in the title and is the fourth part of the method (Fig. 1). |
| Suggestion | In Sect. 2.1 state whether and how blocks can break. If they cannot, replace "fragmentation" and "debris production" in l. 285, l. 294, l. 430, l. 445 to 456 and Conclusion 5 by "dispersion of the block assembly". If they can, measure fragmentation directly (number of blocks or fragment size distribution over time) and relate it to VS and AG. Define a criterion for the phase transition in Sect. 2.4 before applying it, or delete l. 452 to 456. Relate the effective collisions to VS and AG in Sect. 3.4, or remove the purpose stated in l. 217. |
| Status | verified (no breakage method, fragmentation measure or phase criterion described; no result linking collisions to VS or AG); assumption (whether blocks can break), posed as a question |
| Severity | major |
| Source | S4, SD, ZF |

#### Minor corrections

| ID | Location | Quotation | Replacement | Source |
|---|---|---|---|---|
| KK-27 | p. 15, l. 301; p. 19, l. 368 and l. 369 | "cloud maps of velocity distribution"; "cloud map of velocity"; "cloud map of stress" | "contour maps of velocity"; "contour map of velocity"; "contour map of stress" | S4 |
| KK-28 | Fig. 7h to 7n, colour bars (p. 18) | "0Mpa", "-33Mpa", "-31Mpa", "-47Mpa" | "0 MPa", "-33 MPa", "-31 MPa", "-47 MPa" | AB |
| KK-29 | p. 20, l. 397 to 398 | "exhibit a rebound in potential energy after it approaches zero" | "exhibit a rebound in potential energy after their potential energy approaches zero" | S3 |
| KK-30 | p. 22, l. 410 to 413 (caption Fig. 9) | "point 1 ; (b)", and the same space before the semicolon after points 2 to 9 | "point 1; (b)", without a space before each semicolon | S4 |
| KK-31 | p. 23, l. 425 | "3.4 Structural evolution as a function of energy change" | "3.3 Structural evolution as a function of energy change" (there is no Sect. 3.3) | S3, S4, SD |
| KK-32 | p. 24, l. 438 (caption Fig. 11) | "(a-i) when time = 0s, 3s, 7s, 9s, 12s, 15s,32s,71s, 100s," | "(a to j) when t = 0, 3, 7, 9, 12, 15, 32, 71, 100 and 131 s" (ten panels, ten times) | S3, S4, AB, SD |

#### Verification log

| ID | Check | Checked | Values | Result |
|---|---|---|---|---|
| PP-30 | P2, P24 | Duration, time stamps and colour bar maxima of Fig. 7 and Fig. 11 against Sect. 3.1 | 131 s at l. 300, Fig. 7 caption (g) and (n), Fig. 11 caption, Fig. 8 time axis; Fig. 7 times 0, 3, 7, 9, 12, 15, 131 s; Fig. 11 the same first six times, then 32, 71, 100, 131 s; colour bar maxima (b) 5.9, (c) 19.6, (d) 27.1, (e) 31.6, (f) 25.7, (g) 0.21 m/s, equal to l. 307, l. 315, l. 322, l. 330, l. 339 and "approached 0 m/s" (l. 347) | no finding (caption lettering in KK-32; 0.21 m/s in GB-34) |
| PP-31 | P2 | Maximum velocities per stage against "peak" and "decrease" wording | 5.9, 19.6, 27.1, 31.6, 25.7 m/s; 31.6 is the largest, matching "reached its peak" (l. 337) and "began to decrease" (l. 338) | no finding |
| PP-32 | P24 | Fig. 8: timing of the KE rise, peak and drop against l. 378 to 384 | bar spacing 1.23 s; KE 0 GJ up to 3.7 s, 143.6 GJ at 4.9 s, 1082.1 at 11.1 s, 1589.6 at 12.4 s, 1685.4 at 13.6 s (maximum), 814.0 at 14.9 s, 488.4 at 16.1 s | no finding: the peak lies within one bar width of "Around 13 seconds" |
| PP-33 | P2 | Total mechanical energy across figures | Fig. 8 stack top 6506.8 GJ (measured); Fig. 12 PE at VS = 0 and DE at the last point both about 6500 GJ (read) | no finding between figures (magnitude in GB-32) |
| PP-34 | P3, P2 | Rebound of blocks 1 and 3 (l. 397 to 398, l. 416) | PE minimum 0.000 GJ in all ten panels of Fig. 9; final PE (a) 0.362 GJ, (c) 0.331 GJ, all others 0.000 GJ; largest KE per block 0.023 to 0.261 GJ (3.4 to 15.5 m/s with 2300 kg/m³ and the Table 2 volumes) | no finding for the rebound statement (energies in GB-31 and GB-32) |
| PP-35 | P3, P29 | Fig. 10a: legend colours and trajectories | smallest pairwise colour differences 79 (blocks 7 and 8) and 80 (blocks 4 and 9), above 40; positions not measurable in the oblique 3D projection; rebound of blocks 1 and 3 visible qualitatively | no finding; drop heights not checkable |
| PP-36 | P3 | Fig. 12 annotations against the text | annotations "1116.8", "29.47" (a) and "319.5" (b); text l. 453 to 454 "29.47%" and "319.5%" | no finding for the agreement (discrepancy to Fig. 8 in GB-45) |
| PP-37 | P21 | Absolute energy comparisons between whole mass and blocks | whole mass (Fig. 8, about 6507 GJ) and blocks (Fig. 9, 0.95 to 11.06 GJ) compared only in kind, not by magnitude | no finding |
| PP-38 | P24 | Historical event dates in figures | Fig. 2 to Fig. 12 contain no dated historical events; the 1786 event and the tablet of the 1980s appear only in the text | no finding |
| PP-39 | P30, P33 | Reported errors and corrections; effort statements | no errors or corrections reported (search for "error", "correct", "revis": only terrain correction in l. 135 and l. 142); no effort statement used as result or limitation | no finding |

### Segment 4: Conclusions, declarations, references (p. 25 to 29)

#### Substantive findings

**GB-47 The code and data statements defer all author-generated data and code to a request to the first author, name none of the sources, and give no reason for withholding non-personal data.**

| Field | Content |
|---|---|
| Check | P12 |
| Location | p. 26, l. 494 to 495 and l. 505 to 506; p. 6, l. 130 to 135; p. 9, l. 168 to 182; p. 11, l. 206 to 213; p. 11, l. 220 to 234; p. 13, l. 256 to 267; p. 14, l. 272 to 284 |
| Quotation | "The codes that support the findings of this study are available from the first author, Yunfeng Ge, upon reasonable request."; "The data and materials that support the findings of this study are available from the first author, Yunfeng Ge, upon reasonable request." |
| Concern | The methods name at least nine author-generated data sources or scripts: (1) the UAV-derived DEM and point cloud (l. 130 to 135); (2) the restored contour lines and pre-landslide surface (l. 138 to 143, l. 157 to 162); (3) the 3DEC model with 25345 blocks, boundary conditions and material assignment (l. 168 to 182, l. 193 to 202); (4) the laboratory results behind Table 1 (l. 206 to 207); (5) the time histories of the ten monitored blocks and the maximum unbalanced force (l. 256 to 264, Table 2); (6) the whole-mass block parameters used for Fig. 8 (l. 373 to 375); (7) the velocity curves and the list of the 1,139 effective collisions (l. 220 to 234); (8) the alpha-shape envelopes, volumes and areas (l. 272 to 284, l. 426 to 428); (9) the scripts for peak detection, alpha shape and Eq. (1) to (6). Neither statement names any of them, no link or identifier is given, and none of the data concern persons. |
| Suggestion | Replace both statements (l. 494 to 495, l. 505 to 506) by an itemised statement that lists sources (1) to (9) and gives for each a repository with a persistent identifier, or a stated reason why it cannot be released (for example a licence restriction on the 3DEC project files). |
| Status | verified (wording of both statements on the page image p. 26; list of sources from the methods text) |
| Severity | moderate |
| Source | S2 |

**GB-48 About half of the cited works have no entry in the reference list, and more than half of the entries are never cited.**

| Field | Content |
|---|---|
| Check | P4 |
| Location | p. 26, l. 507 to 516; p. 27 to 29, l. 517 to 605; p. 2, l. 45 to 63 |
| Quotation | "(Huang et al., 2012; Intrieri et al., 2018)"; "(Navarre et al., 2009; Van Herwijnen and Schweizer, 2011; Helmstetter and Garambois, 2010; Cook et al., 2021; Pandey et al., 2021)" |
| Concern | The text cites 29 works in 28 citation strings, all in l. 34 to 63; the list has 31 entries (counted with Python). Cited without entry (15): Zhang et al., 2024; Fan et al., 2020; Huang et al., 2012; Intrieri et al., 2018; Huang et al., 2019; Zhu et al., 2010; Zhang et al., 2020a and 2020b; Cuomo et al., 2021; Shugar et al., 2021; Navarre et al., 2009; Van Herwijnen and Schweizer, 2011; Helmstetter and Garambois, 2010; Cook et al., 2021; Pandey et al., 2021; in addition, Zhao et al., 2020 (l. 57) has no 2020 entry. Entries never cited (17): Bernardie et al., 2021; Chang et al., 2022; Chen et al., 2024; Dahal et al., 2022; Gao et al., 2023; Ge et al., 2021; Gong et al., 2024; He, J. et al., 2023; He, K. et al., 2022; He, N. et al., 2023; Nava et al., 2025; Sinčić et al., 2025; Wu, J. et al., 2013; Yang et al., 2022; Zhang, J. et al., 2023; Zhang, K. et al., 2019; Zhou et al., 2024. Quotas (Python): 15 of 29 cited works (51.7 %) cannot be traced, 16 of 29 (55.2 %) if "Zhao et al., 2020" is not the 2021 entry; 17 of 31 entries (54.8 %) are not cited, 18 of 31 (58.1 %) under the same condition. Five of the uncited entries (Bernardie, l. 508 to 510; Dahal, l. 524 to 526; Nava, l. 562 to 565; Sinčić, l. 566 to 568; Zhang, K., l. 597 to 599) are set in grey, unjustified type (darkest grey value 34 against 0 for all other entries, measured on the page images). Question to the authors: do "Fan et al., 2020", "Zhang et al., 2024" and "Zhao et al., 2020" refer to the entries in l. 533 to 536 (dated 2019), l. 594 to 596 (dated 2023) and l. 600 to 602 (dated 2021)? Moderate: the reader cannot check half of the statements on the state of research. |
| Suggestion | Add entries for the 15 missing works; cite the uncited entries where they support a statement (notably Wu et al., 2013 and Zhao et al., 2021 in Sect. 2.1, Ge et al., 2021 in Sect. 2.3) or delete them; align the years of the three pairs named above; set all entries in the same type and justification. |
| Status | verified (counts with Python; grey type measured); inferred (quotas, calculated); assumption (correspondence of the three pairs), posed as a question |
| Severity | moderate |
| Source | S4 |

#### Minor corrections

| ID | Location | Quotation | Replacement | Source |
|---|---|---|---|---|
| KK-33 | p. 25, l. 464 and l. 466 | "It should be noted that:(a)"; "restoring the contours;(b)" | "It should be noted that: (a)"; "restoring the contours; (b)" | S4 |
| KK-34 | p. 26, l. 507 | "Reference" | "References" | S4 |
| KK-35 | p. 27, l. 530 | "Fan, X., Scaringi, G., Korup, O., et al.:" (all other entries list all authors) | the full author list | S4 |

#### Verification log

| ID | Check | Checked | Values | Result |
|---|---|---|---|---|
| PP-40 | P12 | Links, repositories and appendices in the statements; coverage of each data source | 0 links, 0 DOIs, 0 repositories in l. 494 to 495 and l. 505 to 506; no appendix or supplement; 9 author-generated sources and 5 third-party inputs, none named; 0 personal data | findings GB-47 and GB-14; reachability not checkable, since nothing is linked |
| PP-41 | P4 | Figure numbering, citation of every figure, panel references against captions and images | Figs. 1 to 12 contiguous; first citations in order: Fig. 1 l. 76, Fig. 2 l. 93, Fig. 3 l. 144, Fig. 4 l. 173, Fig. 5 l. 220, Fig. 6 l. 256, Fig. 7 l. 301, Fig. 8 l. 375, Fig. 9 l. 393, Fig. 10 l. 414, Fig. 11 l. 428, Fig. 12 l. 443; panel references of Fig. 5, Fig. 7, Fig. 9 and Fig. 10 match captions and panels | no finding beyond GB-09, GB-17, GB-19, GB-33, GB-36 and KK-32 |
| PP-42 | P4 | Tables, equations, sections, appendices | Table 1 cited in l. 212, Table 2 in l. 259; Eq. (1) to (6) contiguous, none cited by number; sections 1, 2, 2.1 to 2.4, 3, 3.1, 3.2, 3.2.1, 3.2.2, 3.4, 4; no appendix, no supplement | no finding except the missing Sect. 3.3 (KK-31) |
| PP-43 | P4 | Short citations against entries | exact matches (8): Carpignano et al., 2009; Sun et al., 2011; Wang et al., 2014; Hu et al., 2017; Wu et al., 2024; Du et al., 2021; Li et al., 2024; Song et al., 2017; matches with deviation: Fan 2019a and 2019, Wang 2021, Tian 2017 against 2016, Cheng 2014 | findings GB-48 and GB-01; minor corrections KK-05, KK-06, KK-09, KK-10; DOIs not resolved (optional check) |
| PP-44 | P15 | Each statement of Sect. 4 assigned to a place in the results | Conclusion 1 core: l. 136 to 162, Fig. 3 (holds); 1 (a) and (b): no place (GB-16). Conclusion 2, first sentence: l. 168 to 202, l. 240 to 266 (holds); "ensures": GB-41; movement process: l. 298 to 352 (holds); collision identification: GB-26. Conclusion 3: GB-31. Conclusion 4: no place (GB-43). Conclusion 5: no fragmentation measure (GB-46). No recommendation and no outlook | findings as listed |
| PP-45 | P15 | Strength of verbs in Abstract, results and conclusions against the evidence | "can be performed" (l. 464), "can be analyzed" (l. 473), "can be identified" (l. 474), "obeys" (l. 478), "it can be concluded" (l. 483, l. 489), "ensures" (l. 471), "confirms" (l. 451), "it is clear that" (l. 418) | "ensures", "obeys" and "confirms" are stronger than the evidence (GB-41, GB-31, GB-46); the others are appropriate or covered by GB-43 |
| PP-46 | P15 | Key terms of the aim (l. 65 to 73) and of Fig. 1 in Sect. 4 | taken up: energy transfer, dissipation, effective collision, volume and area growth, contour restoration, movement process; not taken up: energy accumulation, early warning, risk mitigation, seismic trigger, Dadu River evaluation basis | finding GB-02 |
| PP-47 | P16 | Characters and layout confirmed on the page images before reporting; extraction artefacts excluded | Eq. (1) complete on the page image although the extracted text lacks "=" and "+"; Fig. 1 labels with subscripts; placeholder cells in row 11 of Table 2 intended; "can not" split across l. 176 to 177 (acceptable spelling); Statements section with code, contributions, competing interests, funding and data availability present | no finding for the artefacts listed |
| PP-48 | P9 | Proposals as future studies | none proposes a study with its own design; l. 49 to 51, l. 71 to 73, l. 123 to 125 and l. 466 to 468 are applications of the present method, none with a comparison condition | no further finding (GB-02, GB-16) |

## Optional checks

| Area | What it needs | Responsible | Run |
|---|---|---|---|
| DOI resolution | one retrieval per reference entry with a DOI | `science-quellenapparat-pruefung` | no |
| Citation style | the name of the style | `science-zitierstil-harvard-ctr` or the style rules of the journal | no |
| AI statement against publisher guidelines | the AI policy of the target publisher | this review, on request | no |
| Relation to the authors' prior work | the authors' prior work | this review, on request | no |
| Journal requirements | the author guidelines of the target journal | this review, on request | no |
| Subject-matter accuracy | access to the sources of the checked statements and a selection of sections | `science-faktenbeleg-pruefung`, `geo-frage-belegbasiert-klaeren` | no |

## Limits of this review

- Checked version: egusphere-2025-4506.pdf, 29 pages, SHA-256 64cb3787456244aa6102e34f776b47e9a612d06e8894d391758ae240dbe415d6.
- Review instances: S1 to S4, AB and SD ran as separate agents without context from each other; the merge used only their results, the manuscript, the extracted text and the page images.
- Line numbers: the printed margin numbers (1 to 605). The extracted text carries no margin numbers of its own; lines were mapped by counting from the margin numbers printed every five lines and confirmed on page images at tables, equations and figures (by the merge on pages 1, 4, 6, 8, 12, 13, 14, 20 and 23, by the instances on further pages). Figures are located by figure and panel.
- Measurements on figures were made by the instances AB, S3 and SD; the merge did not repeat them. Where two instances measured the same quantity, the values agree within reading accuracy (KE maximum of Fig. 8: 1666 GJ at 400 dpi and 1685.4 ± 19 GJ at 300 dpi; sum of Fig. 10b: 1213 and 1216.7 ± 9.4), and the review gives the value with stated uncertainty.
- Sources not readable or only partly readable: Ge et al. (2021), Chang et al. (2022), Song et al. (2017), Wu et al. (2024) and He et al. (2023) (titles only); Carpignano et al. (2009), Du et al. (2021) and Zhao et al. (2021) (abstracts only); Navarre et al. (2009) (not read, identified through a citing paper); works cited without an entry could not be identified with certainty.
- Findings with status assumption: 10 of 48 contain a partial statement with status assumption, each posed as a question (GB-14, GB-22, GB-23, GB-24, GB-26, GB-28, GB-29, GB-43, GB-46, GB-48); none has assumption as its central status.
- Optional checks run: 0 of 6.
- Omitted instances: none.
- Discarded findings: 0 of 79 instance findings; none lacked a mandatory field, and none was refuted at the manuscript. Two locations of the language finding (S4, p. 2, l. 42 to 46 and p. 15, l. 293 to 296) were removed from GB-08, because the first is covered by KK-07 and KK-08 and the second was not confirmed as ungrammatical.
- Merged: 51 instance findings were combined into 20 findings; 19 minor corrections were absorbed into findings that name their place and subject; 19 further minor corrections were combined into 8; one hint outside the checklists was confirmed at the manuscript and added to GB-46 with source ZF.
