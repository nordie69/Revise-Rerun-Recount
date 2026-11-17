# Review report: Quantifying Southern Hemisphere dust sources during the Last Glacial-Interglacial Transition using rare earth elements in the EPICA Dome C ice core

| Field | Value |
|---|---|
| Manuscript | Boxho, S., Vanderstraeten, A., Mattielli, N., Laruelle, G. G., Bory, A., Gabrielli, P., Bonneville, S. (2025): Quantifying Southern Hemisphere dust sources during the Last Glacial-Interglacial Transition using rare earth elements in the EPICA Dome C ice core. EGUsphere preprint, https://doi.org/10.5194/egusphere-2025-5046 |
| Checked version | egusphere-2025-5046.pdf, 29 pages, SHA-256 f598b53d01e375844cfb549eb05b9a3407bb30cae553e603c125d5f14886c722; supplement egusphere-2025-5046-supplement.pdf, 22 pages, SHA-256 759cfa14195948f5772d3d6d696081932424f4296e51c812415527ed3b108ea6 |
| Date | 2026-10-18 |
| Language | English |
| Review instances | Segments 1 to 4, figures, study design; the six review instances ran as separate agents; no instance omitted |

## Summary

The manuscript is a re-analysis of a published ice-core dataset: the REE concentrations of 294 dust samples from the EPICA Dome C (EDC) ice core (Gabrielli et al., 2010; 2852 to 33699 yr BP on the EDC3 chronology) are unmixed with the constrained least-squares algorithm DEPOT (MATLAB lsqnonneg) against a database of 217 dust-source patterns from seven potential source areas (PSA), using 13 UCC-normalised REE after removal of Gd and 2000 Monte Carlo runs per sample. After exclusion of 15 incomplete patterns and of 38 fits below the threshold R = 0.67, 241 samples remain (mean R 0.852). Patagonia supplies 65 to 75 % of the dust during MIS3, LGM and HS1 and 49 % in the Holocene, while Australia rises from 9 to 11 % to 23 % and Southern Africa and the Puna-Altiplano each reach about 11 % in the Holocene. The authors date the shift to about 14.5 kyr BP, test it by forward-calculating Sr-Nd isotopic compositions from the modelled contributions against published ice-core data, compare it with the EDML record of Vanderstraeten et al. (2023), and attribute it to the submergence of the Patagonian shelf and the reorganisation of Patagonian drainage.

## Strengths

1. The supplement gives per-sample medians (Table S1) and period means (Table S5) in a form from which every EDC period mean can be recomputed: all 56 EDC values of Table S5 follow from the 241 rows of Table S1 to 0.1 (PP-18), and most period values in Sections 3 and 4 agree with Table S5 (PP-20). The numerical claims can therefore be checked; the deviations reported in GB-37 and GB-45 could be found only because of this.
2. The REE unmixing is checked against an independent tracer: Sr-Nd compositions are forward-calculated from the modelled contributions with Eq. 3 and 4. For the LGM a recomputation from Tables S1 and S3 gives 0.70834 and εNd minus 2.62 against the EDC values 0.7086 to 0.7088 and minus 1.66 to minus 2.46 (PP-30); whether the test also holds for the interglacial is the subject of GB-33.
3. Sample loss is disclosed at the step where it happens: 15 incomplete patterns and Gd are removed in the Methods, 38 fits below the R threshold are removed with their age range and the reason, and the counts close (294 minus 15 = 279, 279 minus 38 = 241; PP-16); the sampling gap is stated with the number of samples it holds, which Table S1 confirms (PP-10). A reader can follow the sample basis, even where its consequences are not yet drawn (GB-23).
4. The figures are built from the published tables: Fig. 1 reproduces the Table S1 values it plots (PP-26), its period zones match the stated boundaries within 0.03 kyr (PP-24), and the 20 bars of Fig. 4 for YD, ACR, HS1 and LGM match the EDC minus EDML differences of Table S5 within 0.3 points (PP-33). The figures can therefore be used to check the text, as GB-28 and GB-45 do.

## Weaknesses

1. The accuracy of the unmixing itself is not tested: the significance attached to R ≥ 0.67 does not follow from its degrees of freedom, R measures the in-sample fit of 13 values by up to 217 non-negative sources, no recovery test with mixtures of known composition is reported, the database is dominated by Australian patterns and contains duplicates, and the 38 rejected samples are selected on the outcome of the fit (GB-21, GB-13, GB-15, GB-23). Suggestion: add to Section 2 a synthetic recovery test and database sensitivity runs, derive the R threshold from a null distribution, and report the period means for several thresholds.
2. The Sr-Nd validation (aim 2) does not reach the interglacial: all 22 measured Holocene values of Table S4 and Fig. 2 come from Taylor Glacier and Berkner Island, the EDC Holocene values cited in the text are not plotted, the modelled values exist only as symbols, the way they were calculated is not stated, and the agreement is not quantified (GB-33, GB-34, GB-35). Suggestion: add EDC Holocene data, tabulate the modelled values per sample and period, and report residuals per period.
3. Several interpretive statements are stronger than the analyses behind them: the main shift is placed at the onset of the ACR although the ACR period means lie within the glacial range (GB-32); the mechanisms are inferred from coincidence in time but stated as demonstrated (GB-36); single-sample minima and the Holocene variability are interpreted climatically without a noise estimate (GB-26), and the climate comparison is visual (GB-38); the low-latitude increase is relative, while the announced absolute fluxes are not shown (GB-20). Suggestion: a change-point analysis with dating uncertainty, replicate-based noise estimates and surrogate tests, the PSA fluxes, and weaker verbs where no test is made.
4. Numbers in text, figures and supplement do not always agree, and the material needed to rebuild the results is not released: values in Sections 3 and 4 differ from Table S5, Table S1 and the figures (GB-28, GB-37, GB-45, GB-46), Table S1 contains rows outside the stated rules (GB-24), and code, input data, correction factors and seven references are missing (GB-49, GB-12, GB-43). Suggestion: recheck all values against Table S5, correct Table S1, deposit code and input data with a DOI, and complete the reference list.

## Findings by segment

### Segment 1: Title, abstract, introduction (p. 1 to 3)

#### Substantive findings

**GB-01 The priority and coverage claims are stated without a search account, the claim in the abstract is unqualified, and "continuous" is not qualified by the sampling gap the manuscript reports**

| Field | Content |
|---|---|
| Check | P28, P15 |
| Location | p. 1, l. 19 to 20; p. 3, l. 74 to 76; p. 7, l. 220 to 221; p. 12, l. 403 to 404; p. 14, l. 472 to 473 |
| Quotation | "we quantify for the first-time contributions from key Southern Hemisphere dust sources"; "we present the first continuous and quantitative record of dust provenance in the Epica Dome C ice core spanning the entire LGIT"; "This study presents the first high-resolution, continuous and quantitative reconstruction of dust provenance in the EDC ice core" |
| Concern | Most of these claims are carefully qualified (continuous, high-resolution, at EDC), and the searches for counterexamples found no earlier continuous quantitative provenance record for EDC (PP-01). Three points remain. (1) No search is described: a search of text.json, p. 1 to 16, for "search", "Web of Science", "Scopus", "Google Scholar", "literature review", "to our knowledge" and "keyword" gave 0 hits each; "database" gave 2 hits (p. 4, l. 126; p. 10, l. 329), both on the dust source database. (2) The sentence of the abstract claims a first-time quantification without the qualifiers used elsewhere, while the manuscript itself reports an isotope-based quantification for East Antarctica: "Coppo et al. (2022) estimated LGM dust composition over EA as 64% from SSA" (p. 9, l. 277 to 278), with Holocene values from the same study in p. 10, l. 324 to 328. (3) "Continuous" is not qualified by the limits the Methods state: "A sampling gap exists between 21.7 and 27.3 kyr BP, where only four samples were available" (p. 4, l. 113), inside the LGIT as defined in p. 3, l. 90 to 91 (33.6 to 2.8 kyr BP); the mean spacing is about 100 years (l. 110), but 1800/8 = 225 years in the ACR and 1200/9 = 133 years in the YD (Python, sample counts from Table S1). The literature that precedes the claim in l. 74 to 76 is treated in GB-08. |
| Suggestion | In p. 1, l. 19 to 20 restrict the claim (for example "the first continuous, high-resolution quantification ... at EDC"); in l. 74 to 76, l. 220, l. 403 and l. 472 state the basis of the claims (databases, search terms, date) or write "to our knowledge"; qualify "continuous" in l. 220 and l. 472 ("near-continuous, with a gap between 21.7 and 27.3 kyr BP") and give the resolution per period; name Coppo et al. (2022) in the introduction (l. 69 to 87) as an earlier isotope-based quantification for East Antarctica. |
| Status | absence of a search account: verified (text search as stated); Coppo et al. (2022) as quantification: verified in the manuscript and, for the unmixing approach, in its abstract (BOA record https://boa.unimib.it/handle/10281/393168); spacing per period: inferred (Python) |
| Severity | moderate |
| Source | S1, S4 |

**GB-02 The introduction ascribes to ice core studies a finding whose only reference is a marine sediment study**

| Field | Content |
|---|---|
| Check | P13 |
| Location | p. 2, l. 36 to 40 |
| Quotation | "Over recent decades, studies on these ice cores have revealed the connection between dust fluxes, ocean export productivity, and the development of deep glaciations" |
| Concern | The link between dust, productivity and glacial climate is correctly stated and is documented by Martínez-García et al. (2014). The cited study, however, is not an ice core study; its abstract states "In a sediment core from the Subantarctic Atlantic, we measured foraminifera-bound nitrogen isotopes to reconstruct ice age nitrate consumption, burial fluxes of iron, and proxies for productivity." The only reference given for "studies on these ice cores" is therefore a marine record. |
| Suggestion | In p. 2, l. 36 to 40 replace "studies on these ice cores have revealed" by wording that names both archives (for example "studies combining ice core dust records with marine sediment records have revealed"), or add an ice core reference that itself establishes the link to export productivity. |
| Status | verified (abstract, Bern Open Repository and Information System, https://boris.unibe.ch/57917) |
| Severity | minor |
| Source | S1 |

**GB-03 The pCO2 range of "~20 to 40 ppmv" exceeds the estimates of both cited studies**

| Field | Content |
|---|---|
| Check | P13 |
| Location | p. 2, l. 40 to 42 |
| Quotation | "Enhanced iron delivery by atmospheric dust during glacial periods are modelled to have lowered the atmospheric pCO2 by ~20 to 40 ppmv" |
| Concern | The qualitative part ("a significant portion of the glacial-interglacial pCO2 difference", l. 41 to 42) agrees with Lambert et al. (2021), who write "About one quarter of that difference is thought to be due to a stronger biological pump". The numbers do not: Lambert et al. (2015) conclude "Based on our results, the LGM atmospheric pCO2 was reduced by ~20 ppm due to enhanced dust loads", and Lambert et al. (2021) give "The model-calculated range of CO2 change for global-scale IF is between 12 and 29 ppmv". Python: 40/20 = 2.0; 40 minus 29 = 11 ppmv. Neither study gives 40 ppmv as its own result; Lambert et al. (2015) mention higher values only as earlier estimates they contrast with their own. Question to the authors: does the upper bound come from one of those earlier estimates, and if so, which study is meant? The sentence follows the citation treated in GB-02; its verb agreement is KK-05. Graded moderate rather than minor because a reader who checks the motivation against the cited sources cannot find the stated bound. |
| Suggestion | In p. 2, l. 41 replace "~20 to 40 ppmv" by the values of the two cited studies (about 20 ppm in Lambert et al., 2015; 12 to 29 ppmv in Lambert et al., 2021), or cite the study that gives 40 ppmv. |
| Status | verified (full text Lambert et al. 2015, AWI repository, https://epic2-clone.awi.de/38919/1/lambert15grl.pdf; full text Lambert et al. 2021, BOA Università di Milano-Bicocca, https://boa.unimib.it/retrieve/e39773b7-1d77-35a3-e053-3a05fe0aac26/Lambert_2021_EPSL_Dust-iron-CO2.pdf); origin of the 40 ppmv bound: assumption |
| Severity | moderate |
| Source | S1 |

**GB-04 The controls on dust deposition are given as source location and residence time, while the cited study names source strength and atmospheric lifetime**

| Field | Content |
|---|---|
| Check | P13 |
| Location | p. 2, l. 44 to 46 |
| Quotation | "dust deposition rates are primarily influenced by both the geographic location of dust sources and the residence time of dust in the atmosphere (Lambert et al., 2008)" |
| Concern | The residence time part agrees with the source. For the other factor, the abstract of Lambert et al. (2008) states that "the sources and lifetime of dust are the main factors controlling the high glacial dust input" and attributes the glacial increase to "a strengthening of South American dust sources, together with a longer lifetime for atmospheric dust particles". The source speaks of source strength, not of the geographic location of sources; the next sentences of the manuscript argue from source identity to the need for provenance quantification, so the substitution matters. |
| Suggestion | In p. 2, l. 45 replace "the geographic location of dust sources" by "the strength of the dust sources", or cite a study that supports the role of source location. |
| Status | verified (abstract, Bern Open Repository and Information System, https://boris.unibe.ch/37302); full text not accessible, so the body of Lambert et al. (2008) was not checked |
| Severity | minor |
| Source | S1 |

**GB-05 The iron-fertilization frame that motivates the study is not taken up in aims, results, discussion or conclusion**

| Field | Content |
|---|---|
| Check | P15, P10 |
| Location | p. 2, l. 49 to 50; p. 15, l. 491 |
| Quotation | "identifying and quantifying the contributions of individual PSA is essential to help better constrain models of dust-driven iron fertilization" |
| Concern | The introduction builds its motivation on dust-borne iron fertilization, pCO2 and source-specific iron content and solubility (p. 2, l. 36 to 50). None of the four aims (p. 3, l. 91 to 98) refers to it. Search in Sections 4 and 5 (p. 7, l. 219 to p. 15, l. 492, text.json) for "iron", "fertili", "HNLC" and "pCO2": 0 hits each; on p. 3 to 16, "iron" occurs twice, both in the reference list (p. 16, l. 526 to 527). The only link is "with implications for biogeochemical fluxes" (p. 15, l. 491). The absolute PSA fluxes announced in the Methods (GB-20) would allow such a link but are not reported. The sources cited for the frame are treated in GB-02 to GB-04. |
| Suggestion | Add in Section 4.3 or 5 a short paragraph on what the source shift implies for iron delivery (PSA-specific fluxes combined with literature iron contents and solubilities per PSA), or reduce the motivation in p. 2, l. 36 to 52 to provenance and circulation. |
| Status | verified (search as stated) |
| Severity | minor |
| Source | S4, SD |

**GB-06 The statement on the role of the Southern Hemisphere westerlies rests on a regional downscaling study of LGM climate in southern Africa**

| Field | Content |
|---|---|
| Check | P13 |
| Location | p. 2, l. 51 to 52 |
| Quotation | "and thus advancing our understanding of changes in Southern Hemisphere westerly winds, which play a crucial role in atmospheric and oceanic circulation (Engelbrecht et al., 2019)" |
| Concern | Engelbrecht et al. (2019), "Downscaling Last Glacial Maximum climate over southern Africa", report that "Southern Africa is projected to have been generally wetter during the LGM". A search of the abstract for "westerl", "circulation" and "ocean" gave 0 hits each. Whether the full text supports the sentence is not known. Question to the authors: which passage of Engelbrecht et al. (2019) supports the role of the westerlies in atmospheric and oceanic circulation? |
| Suggestion | In p. 2, l. 52 cite a work that addresses the role of the Southern Hemisphere westerlies in atmospheric and oceanic circulation, or name the passage of Engelbrecht et al. (2019) that does. |
| Status | verified for the abstract (Arizona State University research portal, https://asu.elsevierpure.com/en/publications/downscaling-last-glacial-maximum-climate-over-southern-africa/); full text: inferred |
| Severity | minor |
| Source | S1 |

**GB-07 The factor "up to 25 times" is attributed to two Delmonte studies whose abstracts do not state it**

| Field | Content |
|---|---|
| Check | P13 |
| Location | p. 2, l. 63 |
| Quotation | "dust fluxes are up to 25 times lower than LGM fluxes (e.g. Delmonte et al., 2008; Delmonte et al., 2017)" |
| Concern | The abstract of Delmonte et al. (2008) deals with Sr and Nd provenance in glacial ages, that of Delmonte et al. (2017) with dust size sorting at Dome B during MIS 2; neither gives a glacial to interglacial flux ratio. The factor is stated in the abstract of Lambert et al. (2008), already cited in l. 36 and l. 46 ("the observed approximately 25-fold increase in glacial dust flux over all eight glacial periods"), for glacial periods in general, not for the LGM. The Delmonte full texts were not accessible. Question to the authors: where in Delmonte et al. (2008, 2017) is the factor given? The factor is used in GB-20. |
| Suggestion | In p. 2, l. 63 add Lambert et al. (2008) as the source of the factor, or give the page or figure of Delmonte et al. (2008, 2017) that contains it. |
| Status | verified for the abstracts (https://boa.unimib.it/handle/10281/6594; https://boa.unimib.it/handle/10281/156340; https://boris.unibe.ch/37302); absence in the Delmonte full texts: inferred |
| Severity | minor |
| Source | S1 |

**GB-08 Two studies that directly precede the contribution are missing: an REE and Sr-Nd study of an East Antarctic ice record across the same transition, and a quantitative REE and isotope mixing model for Southern Hemisphere dust with a wind-based explanation of the low-latitude rise**

| Field | Content |
|---|---|
| Check | P14 |
| Location | p. 3, l. 72 to 76; p. 1, l. 19 to 20 |
| Quotation | "Previous studies using REE patterns in Antarctic ice cores (e.g., Gabrielli et al., 2010; Wegner et al., 2012) achieved multi-decadal resolution but could not fully resolve dust provenance" |
| Concern | Contribution in one sentence: a continuous, high-resolution, quantitative REE-based reconstruction of dust provenance at EDC over the LGIT, with a shift from high- to low-latitude sources at about 14.5 kyr BP attributed to shelf flooding and Patagonian drainage reorganisation. The searches of PP-05 gave two candidates; reference list (p. 16, l. 503 to p. 22, l. 846) searched for "Aarons" and "Struve": 0 hits each. (a) Aarons, S.M., Aciego, S.M., Arendt, C.A., Blakowski, M.A., Steigmeyer, A., Gabrielli, P., Sierra-Hernandez, M.R., Beaudon, E., Delmonte, B., Baccolo, G., May, N.W., Pratt, K.A. (2017) Dust composition changes from Taylor Glacier (East Antarctica) during the last glacial-interglacial transition: A multi-proxy approach. Quaternary Science Reviews 162, 60 to 71, https://doi.org/10.1016/j.quascirev.2017.03.011. It measured REE with 87Sr/86Sr and εNd across the same transition and reports that "The increased isotopic variability during the early Holocene suggests a shift in dust provenance", attributed to local Ross Sea sector sources and southern South America; this bears on the negligible Antarctic contribution found here (GB-29). The manuscript uses its isotope values in Table S4 without listing it (GB-43). (b) Struve, T., Longman, J., Zander, M., Lamy, F., Winckler, G., Pahnke, K. (2022) Systematic changes in circumpolar dust transport to the Subantarctic Pacific Ocean over the last two glacial cycles. Proceedings of the National Academy of Sciences 119(47), e2206085119, https://doi.org/10.1073/pnas.2206085119. It quantified Southern Hemisphere dust sources with a Bayesian mixing model on Pb, Sr and Nd isotopes and REE in a Subantarctic Pacific sediment core (South America about 55 %, Australia and New Zealand about 42 %), with the Australian and New Zealand maxima in deglacial and interglacial intervals linked to reduced westerly wind speeds. It precedes the claim of a first quantitative apportionment across the Southern Hemisphere (l. 74 to 76, see GB-01) and offers an explanation of the low-latitude rise that the shelf-flooding argument does not address (see GB-36). |
| Suggestion | Cite Aarons et al. (2017) in p. 3, l. 72 to 74 among previous REE studies of Antarctic ice and discuss its local-source result in Section 4.3 (p. 10, l. 329 to 334); cite Struve et al. (2022) in l. 74 to 76 as an earlier quantitative apportionment of Southern Hemisphere dust and discuss its wind-based explanation alongside the shelf-flooding mechanism in Section 4.4. |
| Status | Aarons et al. (2017): verified (full text, https://byrd.osu.edu/sites/default/files/2020-12/Aarons_et_al_QSR_2017.pdf); Struve et al. (2022): verified (full text, https://pmc.ncbi.nlm.nih.gov/articles/PMC9704702); whether Struve et al. (2022) fit full REE patterns or use REE only as tracers: inferred |
| Severity | moderate |
| Source | S1 |

#### Minor corrections

| ID | Location | Quotation | Replacement | Source |
|---|---|---|---|---|
| KK-01 | p. 1, l. 15 | "Dust deposits in ice cores provides" | "Dust deposits in ice cores provide" | S1 |
| KK-02 | p. 1, l. 19 | "for the first-time" | "for the first time"; the scope of the same claim is GB-01, the preceding literature GB-08 | S1 |
| KK-03 | p. 1, l. 20 | "During the Marine isotope 3 (MIS3)" | "During Marine Isotope Stage 3 (MIS3)", as in p. 6, l. 184; the neighbouring claim is GB-01 and GB-08 | S1, S2 |
| KK-04 | p. 1, l. 27 | "Comparison with the EDML ice core reveals" | "Comparison with the EPICA Dronning Maud Land (EDML) ice core reveals"; search p. 1 to 15 for "Dronning", "Maud", "(EDML)" and "EPICA DML": 0 hits; "Dronning" occurs only in the reference list (p. 21, l. 789 and 813) | ZF |
| KK-05 | p. 2, l. 40 to 41 | "Enhanced iron delivery by atmospheric dust during glacial periods are modelled" | "Enhanced iron delivery by atmospheric dust during glacial periods is modelled"; the numbers of this sentence are GB-03, the citation before it GB-02 | S1 |
| KK-06 | p. 2, l. 62 | "high altitude site such as EDC where dust fluxes is low" | "high-altitude sites such as EDC where dust fluxes are low" | S1 |
| KK-07 | p. 3, l. 71 | "than REE ratio" | "than REE ratios" | S1 |
| KK-08 | p. 3, l. 73 | "achieved multi-decadal resolution" | "achieved multi-decadal to centennial resolution"; the manuscript gives 60 to 140 years for this dataset (p. 4, l. 110 to 111); the missing study in this sentence is GB-08 | S1 |
| KK-09 | p. 3, l. 88 to 91 | "our ‘DEPOT’ model - to the REE pattern dataset measured - in the EPICA Dome C"; "of the East Antarctica during the LGIT from 33.6 kyr to 2.8 kyr BP" | "our DEPOT model to the REE pattern dataset measured in the EPICA Dome C"; "of East Antarctica during the LGIT from 33.7 to 2.9 kyr BP" (one sentence; spaced hyphens confirmed on the page image; Table S1 runs from 2852 to 33699 yr, as in p. 1, l. 18 and p. 6, l. 182); the aims that follow are used in GB-47 | S1, S3, ZF |

#### Verification log

| ID | Check | Checked | Values | Result |
|---|---|---|---|---|
| PP-01 | P28 | Counterexamples to the priority claims of p. 1, l. 19 to 20, p. 3, l. 74 to 76, p. 7, l. 220, p. 12, l. 403, p. 14, l. 472: three web searches (Coppo et al. 2022 abstract; "Dome C ice core dust isotopic mixing model percentage contribution"; "continuous record dust provenance EPICA Dome C last deglaciation Holocene Sr Nd Pb isotopes time series") | Found: isotope unmixing for East Antarctic Plateau dust (Coppo et al., 2022, cited); Pb isotope studies (Gili et al., 2016; De Deckker et al., 2010) and EDC dust records (Lambert et al., 2008; Marino et al., 2008), none continuous and quantitative for provenance at EDC | no earlier continuous quantitative EDC provenance record found; scope of the abstract sentence and missing search account in GB-01 |
| PP-02 | P13 | Qualitative statements in p. 2, l. 34 to 36 and l. 41 to 42 against Lambert et al. (2008), abstract, and Lambert et al. (2021), full text (accesses as in GB-03 and GB-04); the DOI landing page of Lambert et al. (2015) was refused (HTTP 429), the full text was read in the AWI repository | Lambert et al. (2008): 800 kyr EDC dust record, coupling of dust and temperature; Lambert et al. (2021): "About one quarter of that difference" from a stronger biological pump | no finding for the qualitative statements; numbers in GB-03 |
| PP-03 | P13 | Cited statements in segment 1 without numbers or rankings: l. 47 to 49 (Qu, 2016; Shi et al., 2009, 2011, 2015), l. 53 to 55 (Grousset and Biscaye, 2005; Basile et al., 1997; Delmonte et al., 2010; Gili et al., 2017), l. 65 to 67 (Gaiero et al., 2004; Delmonte et al., 2020), l. 92 to 93 (Paleari et al., 2019; Coppo et al., 2022; Delmonte et al., 2007) | not opened, except Paleari et al. (2019) (fetch failed) and Coppo et al. (2022) (abstract read); l. 57 to 59 ranks the "most prominent PSAs" without citation | not checked against the sources; no finding |
| PP-04 | P13 | p. 3, l. 72 to 74 and p. 4, l. 108 to 113 against Gabrielli et al. (2010), full text, Byrd Polar and Climate Research Center | Source: 294 samples, 2.9 to 33.7 kyr BP, spacing about 60 years (Holocene) and 140 years (glacial), gap 21.7 to 27.3 kyr BP with four samples, "it might not be possible to trace back the dust sources during the LGS". Manuscript: 294 samples, 2852 to 33699 yr BP, about 100 years, 60 to 140 years | no finding; "multi-decadal" applies to the Holocene part only (KK-08) |
| PP-05 | P14 | Six literature searches for preceding work (REE mixing models, Taylor Glacier, quantitative provenance for East Antarctica, Patagonian shelf), Pflichtabgleich with the reference list | Proposed: Aarons et al. (2017), Struve et al. (2022) (GB-08). Not proposed: Kutuzov et al. (2026, received after the manuscript); PNAS 2024 South Atlantic mixing model (doi 10.1073/pnas.2402120121, full text not readable); Marino et al. (2008, without source quantification); hits on egusphere.copernicus.org and cp.copernicus.org not opened | two proposals; other candidates no finding |
| PP-06 | P13 | p. 3, l. 77 to 87 (summary of Vanderstraeten et al., 2023) against its abstract (VLIZ record https://marineinfo.org/doc/publication/382930; full text not open access) | Abstract: Patagonia about 68 % before the shift, "The most striking change occurred -14.5 kyr BP when Patagonia dropped below 50 % on average", Southern Africa 21 to 23 %, Australia 13 to 21 %, early Holocene "highly variable". Manuscript: drop below 50 % at about 14.5 kyr BP, Australia and Southern Africa sharply increased, early Holocene more variable | no finding |
| PP-07 | P10 | Design sketch (whole manuscript and supplement) and gaps against aims | Study type: re-analysis of a published REE dataset with NNLS unmixing, no new ice-core measurements; aims (1) to (4) in p. 3, l. 91 to 98 serve as research questions; no hypotheses stated; comparison conditions: Sr-Nd forward calculation, EDML record, proxy records; no synthetic test (GB-21). Gaps: Holocene "no consensus" to aim 1, isotope limits (p. 2, l. 59 to 68) to aim 2, regional climate to aim 3, EDML (p. 3, l. 77 to 87) to aim 4; the iron-fertilization frame has no aim (GB-05) | no finding beyond GB-05, GB-21, GB-33, GB-38 |

### Segment 2: Materials and methods, supplement data (p. 3 to 5)

#### Substantive findings

**GB-09 Six Southern African dust sources are new measurements ("this study") whose sampling and analysis are not described, and their locations and longitudes are inconsistent**

| Field | Content |
|---|---|
| Check | P19, P8, P38 |
| Location | p. 4, l. 104 to 105; Suppl. p. 17, Table S2, rows EtoshaL1 to EtoshaL4, SuksesL and Sossusvlei, columns Reference, Location, Latitude and Longitude |
| Quotation | "The fit between the REE patterns measured in the EDC ice core and literature reported patterns from known potential source areas (PSA)" |
| Concern | Table S2 (page image Suppl. p. 17) gives "this study" as reference for 6 of 23 SAF dust sources; these are the only new measurements in the database, while the Methods speak of literature patterns. The manuscript contains no description of their sampling, size separation (below 5 µm), digestion or measurement. All six have the location "Etosha Pan", including the row named Sossusvlei at 24,76 S and SuksesL at 21,059 S, 2 to 6 degrees south of EtoshaL1 to 4 (18,557 S to 19,1249 S) and of the Li et al. (2020) Etosha rows (18° 53' to 19° 02' S). All six give western longitudes (15,29 W to 16,836 W), whereas the Li et al. (2020) Etosha rows of the same table give 15° 50' to 15° 53' E. Figure S1 maps the sources of this table. |
| Suggestion | In Section 2 (after p. 4, l. 105) describe the six new samples (sampling, size fraction, digestion, analytical method, blanks, reference materials) or cite their source; in Table S2 correct the Location entries of SuksesL and Sossusvlei and the hemisphere of the six longitudes, and check Fig. S1 for the same points. |
| Status | verified (cell contents on the page image Suppl. p. 17); inferred (that "W" is an error and that Sossusvlei is not at Etosha Pan, from the region and the coordinates in the table) |
| Severity | moderate |
| Source | SD, S2 |

**GB-10 The stated sample spacing of 60 to 140 years does not describe the retained samples: 77 of 240 intervals are shorter than 60 years**

| Field | Content |
|---|---|
| Check | P6, P36 |
| Location | p. 4, l. 110 to 111 |
| Quotation | "with an average temporal resolution of approximately 100 years, ranging from 60 to 140 years between adjacent samples" |
| Concern | Between the 241 rows of Table S1 (Python, column Time), 77 of 240 intervals are shorter than 60 years (shortest 0), 60 are longer than 140 years (longest 2280 years, 23104 to 25384 yr BP), median 98 years, mean 128.5 years. Exclusions can lengthen intervals but not shorten them below 60 years, so the range does not describe the dataset used. Four ages occur twice (3559, 10511, 12841, 28709 yr BP); these pairs are treated in GB-24 and GB-26. |
| Suggestion | In p. 4, l. 110 to 111 give the actual spacing distribution (median and range) of the 279 fitted and the 241 retained samples, and explain the identical ages. |
| Status | verified (Table S1, Python); interpretation of the identical ages: assumption |
| Severity | moderate |
| Source | SD |

**GB-11 The ages follow EDC3 while the period boundaries are taken from the AICC2012 study; on which time scale the boundaries were applied, and on which EDML is compared, is not stated**

| Field | Content |
|---|---|
| Check | P7, P35 |
| Location | p. 4, l. 111; p. 6, l. 185 to 188; p. 21, l. 817 to p. 22, l. 821 |
| Quotation | "The age model follows the EDC3 chronology (Parrenin et al., 2007)." |
| Concern | The period boundaries (p. 6, l. 185 to 188) are cited from Veres et al. (2013), whose title in the reference list is "The Antarctic ice core chronology (AICC2012)" (p. 21, l. 819 to 820); the sample ages are on EDC3 (l. 111, the sentence after the spacing of GB-10). With 8 ACR and 9 YD samples, moving a boundary by one or two samples changes the period means of Table S5 and the differences of Fig. 4. The size of the offset between the two scales could not be assessed (Veres et al., 2013 not readable). Question to the authors: were the DIC ages transferred to AICC2012, or the boundaries to EDC3, and on which time scale is the EDML record of Section 4.4? |
| Suggestion | State the time scale in Section 2 (after p. 4, l. 111) and in the caption of Table S5, give the EDML time scale in Section 4.4, and, if they differ, recompute the period means on a common time scale. |
| Status | naming of the two time scales: verified; offset and its effect: assumption |
| Severity | moderate |
| Source | SD |

**GB-12 The correction factors cfi enter every fit and every Monte Carlo run, but no values, uncertainties or source samples are given**

| Field | Content |
|---|---|
| Check | P8, P27 |
| Location | p. 4, l. 118 to 124; p. 5, l. 153 to 158 |
| Quotation | "we applied cfi derived from parallel measurements of fully digested EDC samples to obtain total REE concentrations allowing fitting with REE patterns from PSA" |
| Concern | Eq. 1 defines cfi, but neither the values per element, the number and ages of the fully digested samples, nor the "variability" used to draw cfi in the Monte Carlo runs (p. 5, l. 157 to 158) are given. Search p. 1 to 16 (text.json): "cf" 4 hits (l. 119, 122, 154, 157), "correction factor" 2 hits (l. 120, 154); supplement: 0 hits for both. The cfi set shapes every DIC pattern before unmixing. Whether one set is valid for glacial and Holocene dust, whose composition differs according to the manuscript's own results, is not discussed. The release of these values is also part of GB-49. |
| Suggestion | Add a supplementary table with cfi per element, its standard deviation, the number and ages of the digested samples and the source; state in Section 2 whether cfi is period-independent, and show the sensitivity of the period means to cfi (for example cfi at plus and minus one standard deviation). |
| Status | verified (search as stated); validity across periods: inferred |
| Severity | moderate |
| Source | SD |

**GB-13 The unmixing is underdetermined (13 equations, 217 unknowns), the Monte Carlo spread does not include end-member or database variability, and the influence of a database in which Australia holds 107 of 217 patterns is not tested**

| Field | Content |
|---|---|
| Check | P9, P27 |
| Location | p. 4, l. 126 to 133; p. 5, l. 142 to 152; p. 5, l. 153 to 158 |
| Quotation | "Sources with CDS equal to 0 are excluded from the fit, indicating no detectable contribution to that specific DIC sample." |
| Concern | The input matrix has 13 rows and 217 columns (p. 5, l. 142 to 145). Such a system generally has many non-negative solutions of similar residual; lsqnonneg returns one. The Monte Carlo runs vary only DIC concentrations and cfi (l. 153 to 158, see GB-12), not the source patterns or the composition of the database, so the PDFs express analytical noise, not the non-uniqueness of the solution. A zero contribution is therefore not evidence of absence, as l. 151 to 152 state. Table S2 holds 107 AUS patterns of 217, 49.3 % (Python: 107/217 = 0.493; counted on Suppl. p. 17 to 19), against 4 ANT and 5 CWA; two pairs are duplicates (GB-15). Whether the number of patterns per PSA influences which PSA is chosen is not examined; the Holocene rise of AUS (p. 6, l. 203 to 205) is the result most exposed to it. |
| Suggestion | Add to Section 2 (i) a bootstrap over the patterns within each PSA, (ii) a run with an equal number of patterns per PSA or with PSA mean patterns, (iii) leave-one-PSA-out runs, and report the range of period means for each; report per sample the set of solutions within the residual tolerance. Replace "indicating no detectable contribution" in p. 5, l. 151 to 152 by a statement conditional on the database. |
| Status | numbers verified; consequence for uniqueness inferred from the stated dimensions |
| Severity | major |
| Source | SD |

**GB-14 Supplementary tables are cited under wrong numbers at four places**

| Field | Content |
|---|---|
| Check | P38, P4 |
| Location | p. 4, l. 127 to 128; p. 26, l. 858; p. 26, l. 865 to 866; p. 28, l. 876 |
| Quotation | "(Figure S1, and Table S1). This dataset (Table S2) includes samples" |
| Concern | Supplement titles on the page images: Table S1 "Median of PSA's contribution" (Suppl. p. 11), Table S2 "Table of PSAs database" (p. 16), Table S3 Sr and Nd end-members of the PSA (p. 20), Table S4 "Measured isotopic values in ice core" (p. 21), Table S5 average contributions of EDC and EDML (p. 22). Against these: the PSA database is called Table S1 and one sentence later Table S2 (p. 4, l. 127 to 128, in the database description of GB-13); the ice-core isotopes are "refs. Table S1" in the caption of Fig. 2 (p. 26, l. 858), but they are Table S4; the PSA isotopic fingerprints are "(Table S4)" in p. 26, l. 865, but they stand in Table S3 with the concentrations; the EDC minus EDML differences of Fig. 4 are said to be in "(Table S4)" (p. 28, l. 876), but derive from Table S5. All 22 occurrences of "Table S" with a digit in main text and supplement were checked; the other 18 match the titles. |
| Suggestion | Replace "Table S1" by "Table S2" in p. 4, l. 127; "(refs. Table S1, - open symbols)" by "(refs. Table S4, open symbols)" in p. 26, l. 858; "the isotopic fingerprint (Table S4) and elemental concentration of the PSAs end-members (Table S3)" by "the isotopic fingerprint and elemental concentration of the PSA end-members (Table S3)" in l. 865 to 866; "(Table S4)" by "(Table S5)" in p. 28, l. 876. |
| Status | verified (page images of the five titles and the four locations) |
| Severity | minor |
| Source | S2, S4, SD, AB |

**GB-15 Two Australian source patterns appear twice in Table S2 under different names and basins, and the regional counts in the Methods do not match the table**

| Field | Content |
|---|---|
| Check | P38 |
| Location | p. 4, l. 131 to 133; Suppl. p. 17 to 18, Table S2, rows Darling26, Darling29, Murray24 and Murray29; p. 11, l. 366 |
| Quotation | "Australia (AUS; 106 DS, predominantly from the central and southeastern regions)"; "Antarctica (ANT; 5 DS from the McMurdo Dry Valleys" |
| Concern | Row Darling26 ("Darling Basin", 34° 3'0.00"S 142° 3'10.80"E) and row Murray29 ("Murray 15", "Murray Basin", same coordinates) carry the same 13 values; so do Darling29 ("DR 3", 34°28'48.00"S 142°49'48.00"E) and Murray24 ("Murray 10"). Identity of all 13 values found by Python over the 217 rows of Table S2 (exactly these two pairs) and confirmed on Suppl. p. 17 and 18. Row counts per region (Python, confirmed on Suppl. p. 16 to 19): PAT 39, CWA 5, PAP 14, SAF 23, AUS 107, NZ 25, ANT 4, total 217; the Methods give AUS 106 and ANT 5, which also sum to 217. Identical columns in Eq. 2 make the split of that pattern between Darling and Murray arbitrary, so the sub-basin attribution of p. 11, l. 366 is not uniquely defined for these patterns, and the effective number of sources is 215. Not graded major because 2 of 107 AUS patterns cannot be shown to change the AUS totals. The six new SAF rows of the same table are GB-09; the dominance of AUS patterns is GB-13. |
| Suggestion | In Table S2 remove or merge the duplicate rows, or state that they are the same sample and to which basin it belongs; correct the counts in p. 4, l. 131 to 133 to the rows used ("AUS; 107 DS", "ANT; 4 DS", or add the missing ANT pattern); state after l. 135 whether the duplicates entered the unmixing and, if so, how the Darling and Murray split in the Holocene was affected. |
| Status | verified (identity of rows, row counts, Methods counts); inferred (arbitrary split for identical columns; effect on p. 11, l. 366 not quantified) |
| Severity | moderate |
| Source | S2, SD |

**GB-16 "PSA" names both the seven source regions and the 217 individual source patterns**

| Field | Content |
|---|---|
| Check | P38 |
| Location | p. 4, l. 136 to 137; p. 5, l. 142 to 144; Suppl. p. 11, Table S1, caption; Suppl. p. 16, Table S2, title; Suppl. p. 20, Table S3 |
| Quotation | "the REE pattern of each EDC sample was modeled as a linear combination of PSA end-members" |
| Concern | The Methods define PSA as potential source areas (p. 4, l. 105) and list seven of them (l. 129 to 133), each made of several dust sources (DS); Eq. 2 and p. 5, l. 142 to 144 use the 217 DS as columns. The caption of Table S1 calls the 217 DS "217 PSAs", Table S2 is titled "Table of PSAs database", and p. 4, l. 136 to 137 calls the 217 columns "PSA end-members", while Table S3 uses "PSA end-members" for the regional isotope end-members. A reader of l. 136 to 137 or Table S1 is led to think that the unmixing used regional end-members, the design the paper sets itself apart from. The other errors of the Table S1 caption are GB-25. |
| Suggestion | Reserve "PSA" for the seven regions and "DS" for the 217 patterns: in p. 4, l. 136 to 137 write "a linear combination of the 217 DS patterns", in the caption of Table S1 "using 217 DS", in the title of Table S2 "Dust source (DS) database". |
| Status | verified (wording at all locations, page images Suppl. p. 11, 16, 20 and p. 4) |
| Severity | minor |
| Source | S2 |

**GB-17 Several steps of the procedure cannot be rebuilt from the text: conversion of CDS to percent, scale of R, aggregation from DS to PSA, the moving average, the minimised equation and the software environment**

| Field | Content |
|---|---|
| Check | P8, P35 |
| Location | p. 5, l. 139 to 140; p. 5, l. 142 to 152; p. 5, l. 159 to 165; p. 29, l. 882 |
| Quotation | "the ensuing CDS results (in % of total deposition) generate a probability density function (PDF) for every DS which were subsequently aggregated by PSA" |
| Concern | Eq. 2 has no sum constraint, yet 240 of 241 rows of Table S1 sum to 99.5 % or more (Python); how CDS are converted to percent is not stated. Whether R is computed on linear or logarithmic UCC-normalised values is not stated. "aggregated by PSA" leaves open whether DS draws are summed per simulation before the median is taken or medians of DS are summed. The "mobile average over 9 steps" (caption of Fig. 1; p. 29, l. 882) is applied to irregularly spaced samples with gaps up to 2280 years (GB-10) without definition. p. 5, l. 159 refers to minimising "Eq. (1)", which defines cfi; the minimised norm is Eq. 2. The MATLAB version and the code are not given (release in GB-49). The detailed method is referred to Vanderstraeten et al. (2023), but the configuration here differs (13 REE, extended database; GB-18). |
| Suggestion | State in Section 2 the normalisation to percent, the scale of R, the order of aggregation and the definition of the moving average; replace "by minimizing Eq. (1)" by "by minimizing Eq. (2)" in p. 5, l. 159; give the MATLAB version. |
| Status | verified |
| Severity | moderate |
| Source | SD, S2, S4 |

**GB-18 The EDC run uses 13 REE and an extended database, while the EDML values come from the 2023 study with 14 REE; whether EDML was recomputed with the same configuration is not stated**

| Field | Content |
|---|---|
| Check | P7 |
| Location | p. 5, l. 144 to 145; p. 12, l. 403 to 409 |
| Quotation | "In Vanderstraeten et al. (2023), n was equal to 14 but is only 13 in the present study because of the exclusion of Gd." |
| Concern | Aim 4 rests on differences between EDC and EDML of 0.4 to 15.6 points (Table S5, see GB-45). If the EDML values of Table S5 are those of the 2023 study, they were obtained with Gd and possibly without the six new SAF samples (GB-09), so method and site differences are confounded. The neighbouring descriptions of the system (GB-13, GB-16, GB-17) do not say which applies. If EDML was not recomputed, the smaller differences (HS1 up to 5.3 points, ACR and YD up to 7.4 points) cannot be attributed to circulation. Question to the authors: were the EDML values recomputed with 13 REE and the present database? |
| Suggestion | State the EDML configuration in Section 4.4 (p. 12, l. 403 to 409); if it differs, rerun EDML with the identical configuration and report both versions in Table S5 and Fig. 4. |
| Status | difference in n: verified; whether EDML was recomputed: assumption |
| Severity | moderate |
| Source | SD |

**GB-19 The Monte Carlo uncertainty of the contributions is computed but no spread is reported for any sample or period, and the 5000-run comparison is given without values**

| Field | Content |
|---|---|
| Check | P11, P31, P33 |
| Location | p. 5, l. 153 to 165; p. 6, l. 179 to 181 |
| Quotation | "To evaluate the impact of uncertainties in REE concentrations in DIC samples and their associated correction factors (cfi) on our model outputs, we performed Monte Carlo (MC) simulations for each DIC sample."; "but the use of a larger number of simulations (5000) does not significantly affect the results" |
| Concern | The Methods describe 2000 simulations per sample and PDFs per DS and PSA. The Results give only medians (Table S1) and period means (Table S5), and Fig. 1 shows no uncertainty band. No interquartile range, interval or standard deviation of the PSA contributions appears for any sample or period, and the 5000-run comparison has no measure of the effect. Without these values the reader cannot judge whether period differences of a few points (for example HS1 differences "not exceeding ~5%", p. 13, l. 420 to 421; ACR and YD differences in GB-45) exceed the model uncertainty. The varied inputs themselves are GB-12 and GB-13; the aggregation step in l. 159 to 165 is GB-17. |
| Suggestion | Add to Table S1 the 25th and 75th percentiles (or a 95 % interval) of each PSA contribution, add a dispersion measure to Table S5, and give in p. 5, l. 162 to 164 the maximum and mean absolute difference of PSA medians between 2000 and 5000 runs. |
| Status | verified |
| Severity | moderate |
| Source | S3, SD |

**GB-20 The announced conversion into absolute PSA fluxes is not reported, so the rise of low-latitude sources is shown only in relative terms; normalised by the total flux it may reverse**

| Field | Content |
|---|---|
| Check | P11, P21, P12 |
| Location | p. 5, l. 165 to 167; p. 6, l. 183 to 184; p. 10, l. 315 to 318; p. 13, l. 440 to 443; p. 1, l. 23; Suppl. p. 4, Fig. S2 |
| Quotation | "to convert PSA contributions into absolute dust fluxes (Figure S2)"; "summarize the relative contributions (in % of total deposition and flux) from each PSA" |
| Concern | Fig. S2 (page image Suppl. p. 4) has three panels: nssCa2+ flux, δ18O, deuterium excess; no PSA flux. Fig. 1 has the y axes "Total Contribution (%)", Table S1 is in percent and has no flux column, and no other figure or table gives a PSA flux; the data statement does not mention them. The careful wording in places (p. 7, l. 226; p. 14, l. 463 "relative increase") contrasts with p. 13, l. 440 to 443 ("increased aridity in low-latitude regions (see above), which likely amplified dust emissions and transport from these sources"), which needs absolute emissions. With the factor of p. 2, l. 63 (interglacial fluxes "up to 25 times lower", see GB-07), the Holocene flux relative to the LGM is (23.1/10.2)/25 = 0.09 for AUS, (10.7/6.3)/25 = 0.07 for SAF and (11.0/3.6)/25 = 0.12 for PAP; with a ratio of only 5: 0.45, 0.34 and 0.61 (Python, Table S5). On this estimate, low-latitude dust deposited at EDC fell in absolute terms and only its share rose. The abstract (p. 1, l. 23, "greater inputs from low-latitude") can be read either way. Question to the authors: does the conversion with nssCa assume a constant Ca fraction across sources while the source mix changes? The same paragraph of the Methods is concerned by GB-17 and GB-19. |
| Suggestion | Add the PSA fluxes (per sample and per period, with the Ca assumption stated) as a panel of Fig. S2 or columns of Table S1 and S5, or delete p. 5, l. 165 to 167 and "and flux" in p. 6, l. 184; in p. 1, l. 23, p. 10, l. 316 and p. 13, l. 440 to 443 write "relative contributions" or support the absolute increase with the flux values. |
| Status | absence of PSA fluxes: verified (page images Fig. S2, Fig. 1, Table S1); flux ratios: inferred (the factor 25 refers to EDC interglacial fluxes in general); Ca assumption: assumption |
| Severity | moderate |
| Source | S2, S3, SD |

**GB-21 The R threshold is an in-sample measure of fit whose stated significance does not match its degrees of freedom, and no independent accuracy test of DEPOT is reported**

| Field | Content |
|---|---|
| Check | P31, P32, P1 |
| Location | p. 5, l. 168 to 172; p. 6, l. 174 to 181 |
| Quotation | "We determined that R ≥ 0.67 corresponds to a statistically significant match (p < 0.01, two-tailed test, degrees of freedom = 10)" |
| Concern | The use of a per-simulation R distribution and its median is clearly described. (a) With 13 REE per pattern (p. 4, l. 117) a Pearson correlation has 11 degrees of freedom, not 10. Critical r for two-tailed p = 0.01 (r = t/√(t² + df), scipy): 0.708 at df 10 and 0.684 at df 11; R = 0.67 corresponds to p = 0.017 (df 10) or 0.012 (df 11). With the threshold 0.708, 19 of the 241 retained samples would drop; the YD would fall from 9 to 7 samples and change markedly (PAT 63.1 to 67.6, AUS 14.5 to 9.1, SAF 14.6 to 17.9; recomputed from rounded Table S1 values), so "~15% during the YD" (p. 6, l. 204) would not hold; with 0.684, 9 samples drop and the YD is unchanged. (b) The modelled pattern is the best non-negative combination of 217 candidate patterns fitted to the same 13 values (GB-13). A significance test for the correlation of two independent series does not apply to a fitted model; R ≥ 0.67 shows that an approximating combination exists, not that the apportionment is correct. No test with mixtures of known composition is reported: search p. 1 to 29 and supplement for "synthetic", "artificial", "known mixture", "recover" and "benchmark": 0 hits each; "validat": 1 hit (p. 3, l. 93, the aim). "robust" (l. 172) and "considered meaningful" (p. 6, l. 180) rest on fit quality only. |
| Suggestion | Add to Section 2 a recovery test: synthetic DIC patterns from DS of known proportions (with the DS used left out of the database), noise according to the Monte Carlo error model, the same 13-element configuration, and the recovery error per PSA and the R distribution. Derive the R threshold from a null distribution (DEPOT fitted to random or shuffled patterns) and correct "degrees of freedom = 10" and "p < 0.01" in p. 5, l. 171 to 172. If Vanderstraeten et al. (2023) contains such a test, state its result and whether it holds for 13 REE and the present database. |
| Status | (a) calculation: inferred (Python, from p. 4, l. 117 and p. 5, l. 170 to 172); effect on the means: inferred (rounded Table S1 values); (b) absence of a recovery test: verified (search); consequence: inferred |
| Severity | major |
| Source | SD, S3 |

**GB-22 The three panels of Figure S2 have no units, and the zones and lines are not explained**

| Field | Content |
|---|---|
| Check | P29 |
| Location | Suppl. p. 4, Fig. S2, panels A, B and C; Suppl. p. 3, caption of Fig. S2 |
| Quotation | "Figure S2: (A) Non Sea Salt Calcium (nssCa2+) flux in EDC ice core (Fischer et al., 2007) (B) δ18O in EDC ice core" |
| Concern | The y axes read "nssCa2+ flux", "δ18O" and "deuterium excess" without units, although p. 5, l. 166 gives µg m⁻² yr⁻¹ for the flux. Panel B has no period zones while A and C have them, and the caption explains neither the zones nor the bold and thin lines. The missing PSA fluxes announced for this figure are GB-20. |
| Suggestion | Add µg m⁻² yr⁻¹, ‰ (VSMOW) and ‰ to the axes, add the period zones to panel B, and explain zones and lines in the caption. |
| Status | verified |
| Severity | minor |
| Source | AB |

#### Minor corrections

| ID | Location | Quotation | Replacement | Source |
|---|---|---|---|---|
| KK-10 | p. 3, l. 101 | "to ice core camples" | "to ice core samples" (page image p. 3) | ZF |
| KK-11 | p. 4, l. 128 | "subdivised into Patagonia" | "subdivided into Patagonia" (page image p. 4); the table reference in l. 127 to 128 is GB-14, the database GB-13 | ZF |
| KK-12 | p. 4, l. 138 | "solving the system of matrixes (Eq.2)" | "solving the system of matrices (Eq. 2)" (page image p. 4) | ZF |
| KK-13 | p. 5, l. 145 to 146 | "For any given time step." | "For any given time step, the vector of 217 components represents" (the sentence is a fragment on the page image p. 5); the paragraph is concerned by GB-13, GB-17 and GB-18 | ZF |
| KK-14 | Suppl. p. 16, Table S2, region heading | "Puna AltiPlano (PAP)" | "Puna-Altiplano Plateau (PAP)", as in p. 4, l. 129 to 130 and p. 11, l. 353; other content of Table S2 is GB-09 and GB-15 | S2 |
| KK-15 | Suppl. p. 17, Table S2, row Darling12, column Longitude | "31° 2'49.20"S 138°17'6.00"E" | check the longitude: the row has the latitude of Darling11 and its minutes and seconds (31° 2'49.20"S 144°17'6.00"E), and all other Darling rows lie at 141° to 149° E (page image Suppl. p. 17); "144°17'6.00"E" if a copying error; see also GB-09, GB-15 and KK-14 | ZF |
| KK-16 | Suppl. p. 19, Table S2, region heading; Suppl. p. 20, Table S3, row 4; p. 26, Fig. 2, label | "New-Zealand (NZ)" | "New Zealand (NZ)", as in p. 2, l. 59 and p. 4, l. 132 (text.json main text: 0 hyphenated, 10 unhyphenated; the figure labels read on the page images p. 26 and Suppl. p. 20); see also GB-09, GB-15, KK-14 and KK-15 | S2 |

#### Verification log

| ID | Check | Checked | Values | Result |
|---|---|---|---|---|
| PP-08 | P12 | Every data source of Section 2 (p. 3, l. 99 to p. 5, l. 172) and of the method captions against the statement p. 16, l. 494 to 496 and the supplement | EDC REE patterns: cited, not supplied; cfi: not supplied; per-element uncertainty: range 2 to 10 % only; PSA database: Table S2, 217 rows, 13 REE; original sources Gili et al. 2017, Gaiero et al. 2004, Li et al. 2020, Vanderstraeten et al. 2023, Koffman et al. 2021 in the list, Marx et al. 2005, McGowan et al. 2005, Marx and Kamber 2010, Diaz et al. 2018 not; MC output: medians and R in Table S1 (241 rows); nssCa flux (Fischer et al., 2007), δ18O (EPICA Community Members, 2006), d-excess (Stenni et al., 2010) in Fig. S2; Sr-Nd end-members Table S3; ice-core isotopes Table S4; EDML Table S5; no data link in statement or supplement, so no link reachability could be checked | findings GB-12, GB-20, GB-43, GB-49; the method is disclosed as described elsewhere (p. 4, l. 106 to 107) |
| PP-09 | P38 | Identifiers over main text, captions, references and supplement (text.json, page images) | "DEPOT" 5 hits, model and algorithm for one object; "MIS3" 16 and "MIS 3" 2 (spacing only); "HS1" 23, "HSI" 1 (KK-17); "Southern" and "South Altiplano" (KK-21); "South Puna" 5 and "S-Puna" in Table S3 and labels; CWA and SCWA: SCWA rows are a subset of CWA, two objects; "Darling sub-basin" and "Darling Basin": same basin; "Old Dome C" (Basile et al., 1997) is another core than EDC; DIC, DS, CDS, cfi, CONTR, CIR used consistently after definition | remaining identifiers no finding; GB-14 to GB-16, GB-39 |
| PP-10 | P5 | Sampling gap, p. 4, l. 113 | retained Table S1 rows between 21676 and 27425 yr: 22150, 23104, 25384, 25640 = 4 ("only four samples") | no finding |
| PP-11 | P26 | Guarantee "physically meaningful" (p. 5, l. 139) | refers to non-negativity only; NNLS in all samples | no finding; sum normalisation in GB-17 |
| PP-12 | P25 | Information flow per step | cfi from parallel digestions (p. 4, l. 122 to 124); end-member isotopes and concentrations in Table S3 for 7 of 8 source groups, no ANT end-member (GB-29) | no finding beyond GB-29 |
| PP-13 | P33 | Effort statements | only p. 5, l. 162 to 163 (computation cost), without values | GB-19 |
| PP-14 | P35 | Environment fields | MATLAB lsqnonneg named (p. 5, l. 140), version missing; no instrument change reported; instruments of the dataset in Gabrielli et al. (2010) | GB-17 |
| PP-15 | P7 | Method version over the data | one DEPOT configuration for all 279 EDC samples; version difference only between EDC and EDML (GB-18) and time scale (GB-11) | no finding beyond GB-11, GB-18 |

### Segment 3: Results (p. 6 to 7, Fig. 1, Tables S1 and S5)

#### Substantive findings

**GB-23 The 38 samples excluded by the R threshold are selected on the outcome of the fit, make up 22.8 % of the samples younger than 14 kyr BP, and are neither listed nor assessed for their effect**

| Field | Content |
|---|---|
| Check | P9, P34, P11, P22 |
| Location | p. 6, l. 174 to 179 |
| Quotation | "Out of the 279 DIC samples treated by our algorithm, 38 did not meet the R threshold (R≥0.67) and were excluded from the provenance record." |
| Concern | The exclusion and its reason are disclosed (PP-16), and the threshold itself is GB-21. The consequence is not drawn. Table S1 lists 241 rows, 129 of them younger than 14 kyr BP and 112 older (Python). With all 38 excluded samples younger than 14 kyr BP (l. 175), 38 of 167 samples in that interval are excluded, 22.8 % (Python: 38/(129 + 38)). The selection is made on fit quality, that is on the outcome of the method; samples whose source mix is poorly represented in the database would be removed preferentially, which can bias the Holocene means of aim 1. Neither the ages, concentrations and R values of the excluded samples nor their distribution over the periods are given, although the caption of Table S1 says "279 DIC" (GB-25), so the per-period sample loss needed to weigh the tentative ACR and YD results (p. 12, l. 407 to 409) cannot be derived. The missing spread of the retained samples is GB-19. |
| Suggestion | In Section 3 and the supplement list the 38 excluded samples with age, total REE concentration and median R, give the number of samples per period before and after the threshold, report the period means of Table S5 for thresholds of, for example, 0.60, 0.67 and 0.75, and test among the retained samples whether R correlates with concentration and with the dominant PSA. |
| Status | counts verified (Table S1, p. 6, l. 174 to 175); share inferred (Python); bias inferred |
| Severity | major |
| Source | SD, S3 |

**GB-24 Table S1 contains rows that do not meet the stated rules: three R values below the threshold, one row that sums to 93.5 %, and four pairs of identical ages**

| Field | Content |
|---|---|
| Check | P1, P5, P23 |
| Location | p. 6, l. 174 to 175; Suppl. p. 11, Table S1, rows 2888 and 3267, column R; Suppl. p. 13, Table S1, first row 10511; Suppl. p. 11, 13 and 14, Table S1, rows 3559, 10511, 12841 and 28709 |
| Quotation | "38 did not meet the R threshold (R≥0.67) and were excluded from the provenance record" |
| Concern | (1) Rows 2888, 3267 and the first row 10511 show R = 0,66 on the page images; a value printed as 0.66 is below 0.665 and cannot round to 0.67. Either these samples should have been excluded (then 41 excluded, 238 retained) or the printed R is wrong. (2) The first row 10511 reads 0,0 / 0,0 / 3,1 / 6,7 / 49,2 / 29,5 / 5,0 / 0,0, sum 93.5; all other 240 rows sum to 100 within 0.25 (Python). Either one cell is mistyped (6.5 points missing) or a column is omitted. (3) Four ages occur twice with different compositions (3559, 10511, 12841, 28709 yr BP); either two samples share one age on EDC3 or an age was copied wrongly. This matters for the YD count (GB-46: two of the 9 YD rows are the pair at 12841) and for the spacing (GB-10). The exclusion procedure is GB-23 and the threshold GB-21; the terms of the caption of the same table are GB-16. |
| Suggestion | Check and correct the three R values and the first row 10511 in Table S1; state in its caption why identical ages occur, or correct them; if samples are removed, update the counts in p. 6, l. 174 and 179 and in the abstract (p. 1, l. 19). |
| Status | values verified (page images); causes: assumption |
| Severity | moderate |
| Source | S3, SD |

**GB-25 The caption of Table S1 and its citation in the Results describe content the table does not have**

| Field | Content |
|---|---|
| Check | P20, P2 |
| Location | p. 6, l. 183 to 184; Suppl. p. 11, Table S1, caption |
| Quotation | "Median of PSA's contribution (in percents) based on th DEPOT model results - using 217 PSAs and 279 DIC from EDC ice core REE patterns." |
| Concern | Table S1 has 241 rows (Python; the row 17148 carries the period label "HS" in text.json), the number retained after the R threshold (p. 6, l. 179), not 279. The number 217 refers to dust sources, while the table has seven PSA columns (Puna and Altiplano separate, CWA, ANT; GB-16 treats the term). Table S1 gives per-sample medians in percent; it has no flux values and no interval means, which are in Table S5, although p. 6, l. 183 to 184 says that Fig. 1 and Table S1 summarise the contributions "in % of total deposition and flux ... across major climatic intervals". The missing fluxes themselves are GB-20; the rows that break the rules are GB-24. |
| Suggestion | Revise the caption to "Median contributions (%) of the PSA to each of the 241 DIC samples that passed the R threshold, based on the DEPOT model with 217 dust sources (DS)" and correct "th"; in p. 6, l. 183 to 184 write "Figure 1 and Table S1 (per sample) and Table S5 (per period) summarize the relative contributions (in % of total deposition)". |
| Status | verified |
| Severity | minor |
| Source | S3, SD, S4 |

**GB-26 Single samples integrate 2 to 3 years about every 100 years, and the manuscript's own same-age pairs differ by up to 87 points, yet single-sample minima and the Holocene variability are interpreted climatically**

| Field | Content |
|---|---|
| Check | P9 |
| Location | p. 6, l. 194; p. 9, l. 306 to 308; p. 4, l. 112 |
| Quotation | "Three distinct minima in PAT contributions occur at 10, 8.6, and 6.3 kyr BP." |
| Concern | Each Holocene sample integrates 2 to 3 years (p. 4, l. 112), about 2.5 % of a 100-year interval (Python: 2.5/100). The two samples dated 3559 yr BP give PAT 86.7 % and 0.0 %, AUS 12.8 % and 49.8 %; at 10511 yr BP PAT 0.0 % and 38.2 %; at 12841 yr BP PAT 39.5 % and 71.9 %; only the glacial pair at 28709 yr BP is close (68.8 % and 72.5 %) (Table S1, page images). In the Holocene 23 of 116 samples have PAT = 0, the lag-1 autocorrelation of PAT is 0.12, and the mean absolute difference between adjacent samples is 33.6 points against 10.7 in the LGM (Python, Table S1). This pattern is what interannual dust variability or fit instability (GB-13) would produce; it does not by itself indicate "seemingly higher frequency changes in sources" (p. 9, l. 307 to 308). Several minima and maxima discussed in Section 4.3 rest on single samples (for example 9772 yr BP, AUS 98.1 %; 8629 yr BP, Altiplano 100 %). The verb "significantly" in p. 9, l. 306 is treated in GB-36. Question to the authors: what are the same-age pairs? |
| Suggestion | Estimate replicate variability from same-depth replicates or contiguous samples over one Holocene interval; compare the Holocene variance with it; test each minimum or maximum of the 9-step moving average discussed in Sections 3 and 4.3 against a white-noise null with the observed variance (Monte Carlo), and restrict the interpretation to features that pass. |
| Status | values verified; statistics inferred (Python); nature of the pairs: assumption |
| Severity | major |
| Source | SD |

**GB-27 Statements on individual dust sources and sub-basins rest on results that are not reported**

| Field | Content |
|---|---|
| Check | P11, P34, P19 |
| Location | p. 6, l. 196 to 197; p. 11, l. 366; p. 12, l. 385 to 387; p. 12, l. 392 to 398 |
| Quotation | "Among the 39 DS from PAT, our algorithm highlights three specific REE patterns collected in or near the Valdes Peninsula." |
| Concern | The model resolves 217 DS, and the text draws conclusions at DS and sub-basin level: three Valdes Peninsula patterns (not named; Table S2 has 7 PAT rows at Peninsula de Valdes or Puerto Madryn), the Darling sub-basin as dominant Holocene AUS source (p. 11, l. 366, where two patterns are duplicated, GB-15), the detection frequencies and relative contributions of Namibian coast, Etosha and Makgadikgadi (p. 12, l. 385 to 398). Table S1 splits only PAP into Puna and Altiplano; for PAT, AUS and SAF no DS-level contribution, detection count or frequency is given, and Fig. S3 shows only the PAP and SAF sub-regions. "detected most frequently" has no count and no denominator. |
| Suggestion | Add a supplementary table with, for each sub-basin or DS named in Sections 3 and 4.3 (Darling, Murray, Lachlan, Murrumbidgee, Wimmera, Eyre; Namibian rivers, Etosha, Makgadikgadi; the three Valdes patterns), the number of samples with a contribution above 0 out of 241 and the mean contribution per period, and name the three patterns in p. 6, l. 196 to 197. |
| Status | verified (search; "Darling" occurs in the supplement only in Table S2, in the 45 rows Darling1 to Darling45 and their basin column) |
| Severity | moderate |
| Source | S3, SD |

**GB-28 The statements on the Puna and Altiplano sub-regions in the Results contradict Table S1, Fig. 1 and Fig. S3, and "over 90%" has no stated denominator**

| Field | Content |
|---|---|
| Check | P2, P20, P24, P3 |
| Location | p. 7, l. 211 to 215 |
| Quotation | "contributing over 90% at 11.2, 10, 8.6, 6, and 3.5 kyr BP. In contrast, contributions of South Puna remained consistently below 20% during this interval (Figure 1)." |
| Concern | Table S1 is the only artefact that splits PAP into Puna and Altiplano, and the split is a strength of the dataset. (1) "~5% during the ACR and YD, primarily from the South Puna region" (l. 212): YD means Puna 1.26 and Altiplano 3.27, ACR Puna 5.23 and Altiplano 0.00 (Python, Table S1); the statement holds for the ACR only. (2) Of the five ages, only two exceed 90 %: Table S1 Altiplano 8629 yr 100.0 and 11228 yr 97.0, against 9957 yr 75.7, 5967 yr 58.5, 6166 yr 58.0 and 3465 yr 62.7; Fig. 1 raw PAP peaks, measured on the page image (y: 100 at 2595.5 px, 0 at 3056.5 px; about ±0.5 %): 98.8 % at 8.66 kyr, 97.1 % at 11.23 kyr, 76.0 % at 9.97 kyr, 57.8 % at 5.98 kyr, 60.0 % at 3.48 kyr. If "over 90%" means the share within PAP, all five ages give 100 %, but then the denominator is PAP. (3) South Puna is 20 % or more in 8 Holocene rows of Table S1 (3503: 25.0, 4387: 20.6, 5657: 23.4, 5850: 29.1, 6775: 20.7, 7833: 25.6, 10205: 25.7, 11117: 20.2), and Fig. S3 shows raw Puna peaks above 20 % at eight ages up to 42.9 % at 11.11 kyr BP (measured). (4) The sentence cites Fig. 1, which shows only the PAP total; the sub-regions are in Fig. S3. The onset of the Altiplano contribution is GB-42; the naming "South Altiplano" is KK-21. |
| Suggestion | In p. 7, l. 211 to 215 state the denominator ("of total dust" or "of PAP dust"), give the actual ages and values (for example "over 90 % at 11.2 and 8.6 kyr BP and 58 to 76 % at 10, 6 and 3.5 kyr BP"), replace "primarily from the South Puna region" by a period-specific statement, replace "consistently below 20%" by the observed range (mostly below 30 %, one sample at about 43 % in Fig. S3), and cite Fig. S3 instead of Fig. 1. |
| Status | Table S1 values: verified (page images of the cited rows and Python); figure values: verified by measurement |
| Severity | moderate |
| Source | S3, AB |

**GB-29 The statements that Antarctic sources contribute negligibly hold on average but not for one sample with 33.1 % ANT, which the Sr-Nd calculation cannot represent**

| Field | Content |
|---|---|
| Check | P6, P25 |
| Location | p. 7, l. 217; p. 10, l. 329 to 330 |
| Quotation | "our results do not indicate significant Antarctic contributions to EDC" |
| Concern | On average the statement holds (Holocene ANT 0.3 %, Table S5). At sample level, row 3654 yr BP of Table S1 has ANT 33.1 % (page image Suppl. p. 11) and row 13412 yr BP 1.7 %. Table S3 has no ANT end-member, so Eq. 3 and 4 cannot include these contributions. The local Antarctic sources found at Taylor Glacier by Aarons et al. (2017) are cited in GB-08; the section reference in p. 10, l. 329 to 330 is KK-36. |
| Suggestion | In p. 7, l. 217 and p. 10, l. 329 to 330 refer to the average and mention the single sample; add an ANT end-member to Table S3 or state how ANT was handled in Eq. 3 and 4. |
| Status | verified |
| Severity | minor |
| Source | SD |

**GB-30 The caption of Figure 1 does not resolve the abbreviations in the figure**

| Field | Content |
|---|---|
| Check | P29 |
| Location | Fig. 1, p. 24; p. 25, caption of Fig. 1 |
| Quotation | "Gray vertical zones delineate the various periods of the transition from end of MIS3 to Holocene." |
| Concern | The panel titles PAT, AUS, SAF, NZ, PAP and the period labels YD, ACR, HS1, LGM, MIS3 are not expanded in the caption; they are defined only in the text (p. 4, l. 129 to 132; p. 6, l. 184 to 188). The periods are marked by alternating grey and white zones, not by grey zones alone. The x axis title appears only under the lowest panel, which is acceptable for a shared axis. |
| Suggestion | Expand the PSA and period abbreviations with the period ages in the caption of Fig. 1 and write "Alternating grey and white zones". |
| Status | verified |
| Severity | minor |
| Source | AB |

**GB-31 Axis numbers and legends in Figures 1, 2, 3 and 5 are below 6 pt at the printed size**

| Field | Content |
|---|---|
| Check | P29 |
| Location | Fig. 1, p. 24; Fig. 2, p. 26; Fig. 3, p. 27; Fig. 5, p. 29 |
| Quotation | "Figure 1: Evolution of dust PSA contributions to EDC ice core" |
| Concern | Cap heights measured on the 300 dpi page images, pt = px × 72 / 300 / 0.72 (method uncertainty about ±0.6 pt): Fig. 1 tick numbers 16 px = 5.3 pt, legend 14 px = 4.7 pt, axis titles 17 px = 5.7 pt; Fig. 2 legend 16 px = 5.3 pt; Fig. 3 tick numbers 16 px = 5.3 pt; Fig. 5 tick numbers 13 to 14 px = 4.3 to 4.7 pt, legend 14 px = 4.7 pt. All these stay below 6 pt even with +0.6 pt; Fig. 4 reaches 6.3 to 7.0 pt (PP-44). The caption of Fig. 1 is GB-30. |
| Suggestion | Enlarge tick numbers and legends in Fig. 1, 2, 3 and 5 to at least 7 pt at final size. |
| Status | verified (measurement) |
| Severity | minor |
| Source | AB |

#### Minor corrections

| ID | Location | Quotation | Replacement | Source |
|---|---|---|---|---|
| KK-17 | p. 6, l. 191 | "the PSA dust assemblage during HSI is marked" | "the PSA dust assemblage during HS1 is marked" (the other 24 occurrences of the period in text.json read "HS1"; page image) | S2, S3 |
| KK-18 | p. 6, l. 193 | "(averages contributions)" | "(average contributions)"; the YD and ACR values of the sentence are concerned by GB-46 | S3 |
| KK-19 | p. 6, l. 198 | "and therefore reflects regional mixed input" | "and therefore reflect regional mixed input" | S3 |
| KK-20 | p. 6, l. 199 | "LREE (low rare earth elements)" | "LREE (light rare earth elements)" | S3 |
| KK-21 | p. 7, l. 213; p. 9, l. 290 | "the emergence of South Altiplano dust"; "in the South Altiplano linked to" | "Southern Altiplano" at both places, as in p. 4, l. 130 and p. 11, l. 358 and 362 (compared on the page images); the values of the sentence in l. 213 are GB-28 | S2 |
| KK-22 | p. 25, caption of Fig. 1; p. 29, l. 882; Suppl. p. 9, caption of Fig. S5 | "between 2852 to 33699 yr BP"; "Bold lines denote the mobile average over 9 steps"; "as their dust emissions contribution are very low" | "between 2852 and 33699 yr BP"; "moving average over 9 samples" (in all three captions; its definition is GB-17); "as their contributions are very low"; see also GB-30, GB-31, GB-39 and GB-55 | S4, AB |

#### Verification log

| ID | Check | Checked | Values | Result |
|---|---|---|---|---|
| PP-16 | P1 | Sample balance in Methods and Results | 294 minus 15 = 279 (p. 4, l. 114, 117); 279 minus 38 = 241 (p. 6, l. 174, 179); 241/279 = 86.4 % ("86%"); Table S1 241 rows; abstract "241 samples" (p. 1, l. 19) | no finding; distribution of the excluded samples in GB-23 |
| PP-17 | P1 | Mean R and age span of the retained record | mean R of Table S1 = 0.8523 ("R = 0.852", p. 6, l. 181); ages 2852 to 33699 ("33.7 kyr BP to 2.9 kyr BP", p. 6, l. 182; p. 1, l. 18) | no finding; other spans in KK-09 and KK-34 |
| PP-18 | P1, P2, P37 | Table S5 (EDC) against the means of Table S1, period boundaries of p. 6, l. 185 to 188 | 8 periods by 7 PSA, all 56 values agree to 0.1 (n: Late Holocene 60, Early Holocene 56, YD 9, ACR 8, HS1 27, LGM 40, MIS3 41; sum 241); for example YD 63.06, 4.53, 14.63, 14.50, 3.28 (PAT, PAP, SAF, AUS, NZ) | no finding; Table S5 is the sample-weighted mean of Table S1; YD count in GB-46 |
| PP-19 | P1 | Row sums of Table S5 | EDC 100.1, 99.9, 100.0, 100.0, 100.0, 100.1, 100.0, 100.0; EDML 100.0, 100.0, 100.0, 99.9, 100.0 | no finding |
| PP-20 | P2, P15, P36 | Period values of abstract, Section 3 and Section 4 against Table S5 | PAT 65 to 75 % in MIS3, LGM, HS1 (70.3, 65.7, 74.8); 69 and 63 % in ACR and YD (68.9, 63.1); 47 to 51 % Holocene (47.1, 50.7); AUS 9, 10, 11, 11, ~15, 23 (9.1, 10.2, 11.3, 11.1, 14.5, 23.1); SAF ~5 to 9 %, 15 %, ~11 % (4.9 to 9.3, 14.6, 10.7); NZ 14, 7, 6.5, 3, 6 (14.2, 7.1, 6.6, 3.3, 5.9); PAP below 4, ~5, 11 (2.2, 3.6, 2.0; 5.2, 4.5; 11.0); p. 10, l. 317 to 319 (23, 11, 11; 10, 4, 6; 49, 6); SSA LGM 65.7 + 3.6 = 69.3 (~70, p. 9, l. 281); EDML NZ ~6 (6.2) | no finding for these values; deviations in GB-37 |
| PP-21 | P21 | Sample weighting against time weighting of the period means | time-weighted LGM PAT 65.8, NZ 15.3, AUS 9.0 (sample-weighted 65.7, 14.2, 10.2); Holocene PAT 51.6, AUS 21.7 (49.0, 23.1); HS1 75.0, 10.9 (74.8, 11.3) | no finding; order of sources and period contrasts do not change |
| PP-22 | P11 | Periods of the result matrix against the reported quantities | EDC: Table S5 all 8 periods; EDML: Early Holocene, YD, ACR, HS1, LGM, in line with the disclosed EDML range 7.5 to 27 kyr (p. 12, l. 406 to 407); Fig. 3 Holocene and LGM, Fig. S4 the other periods | no finding beyond GB-19, GB-20, GB-23, GB-27, GB-45 |
| PP-23 | P24, P2 | "SAF input drops to minimal levels (~2%) between 9.5 and 12 kyr BP" (p. 6, l. 207 to p. 7, l. 208) against Table S1 and Fig. 1; contradiction between instance AB (finding on the smoothed line) and instance S3 (no finding) decided here | Table S1, 33 rows from 9772 to 11993 yr: median 0.3 %, 23 rows at 2 % or less, mean 4.32 %; means per half-millennium 0.96 (9.5 to 10.0 kyr, n 7), 5.84 (n 9), 9.34 (n 8), 1.20 (n 6), 0.0 (11.5 to 11.7, n 1), 0.65 (11.7 to 12.0, n 2); the higher window means are carried by single samples (10278 yr 40.3 %, first 10511 yr 49.2 %); AB measured the 9-step moving average (4.2, 8.5, 3.8, 2.0, 11.6, 12.5 %), which spreads the YD values (12227 yr, SAF 94.7 %) into the window | no finding; the statement agrees with the sample values; the finding of instance AB was discarded (see Limits) |
| PP-24 | P24 | Period zones in Fig. 1 (all panels) and Fig. 5 A and B against p. 6, l. 185 to 188 | Fig. 1 zone edges 11.71, 12.90, 14.70, 18.01, 29.01 kyr BP (±0.024 kyr); text 11.7, 12.9, 14.7, 18, 29; Fig. 5A 11.75, 12.88, 14.70, 18.02, 29.00; Fig. 5B 11.74, 13.03, 14.75, 17.99, 29.03 | no finding; the YD and ACR edge of Fig. 5B lies 0.13 kyr later than in panel A |
| PP-25 | P24 | Dated extremes in Fig. 1 against p. 6, l. 194 and l. 205 | PAT smoothed minima 26.4 % at 6.28 kyr, 28.1 % at 8.49 kyr, 20.1 % at 10.11 kyr (text 6.3, 8.6, 10 kyr); AUS smoothed maxima 41.0 % at 6.33 and 10.18 kyr (text ~6.3 and 9.5 to 10 kyr) | no finding (within half the line width, about 0.1 kyr) |
| PP-26 | P3 | Fig. 1 raw SAF peaks against Table S1 | Fig. 1: 71.7 % at 3.38 kyr, 55.6 at 4.83, 58.0 at 5.62, 63.9 at 6.57, 70.2 at 6.97, 54.3 at 8.80 kyr (±0.7 %); Table S1: 73.5 at 3425, 56.7 at 4863, 58.2 at 5580, 63.3 at 6570, 71.0 at 7013, 54.3 at 8790 yr | no finding; Fig. 1 plots Table S1 |
| PP-27 | P30 | Reported errors and corrections | none reported in p. 1 to 16 or the supplement | no finding |
| PP-28 | P17 | Place of the disclosed limits | sampling gap (p. 4, l. 113) and Gd removal (l. 115 to 117) at the method; R exclusion in the Results with the threshold in the Methods; ACR and YD caveat only in Section 4.4 | finding only for the ACR and YD caveat (GB-46) |
| PP-29 | P19 | Provenance classes of the core statements | all provenance values model-generated from secondary inputs; sources named; undocumented primary data (GB-09); non-EDC isotope data used as EDC validation (GB-33) | no finding beyond GB-09, GB-33 |

### Segment 4: Discussion, conclusion, declarations, references, Figures 2 to 5 (p. 7 to 29)

#### Substantive findings

**GB-32 Discussion and Conclusion place the main provenance shift at the onset of the ACR, but the ACR period means lie within the glacial range; the clear shift appears in the YD and the Holocene**

| Field | Content |
|---|---|
| Check | P15 |
| Location | p. 7, l. 225 to 226; p. 7, l. 233 to 236; p. 14, l. 477 to 480 |
| Quotation | "Our calculations highlight a major shift in dust provenance occurred at the onset of the ACR"; "From ~14.5 kyr BP onward, a marked reorganization in dust provenance occurred" |
| Concern | The Results give the period means, consistent with Table S5 (PP-20). By these means the ACR does not differ from the glacial periods as claimed. AUS: MIS3 9.1, LGM 10.2, HS1 11.3, ACR 11.1 %; the Results themselves say "reaching 11% during the ACR" (p. 6, l. 204), the same as HS1 (l. 203). SAF: "relatively stable ... during MIS3, LGM, HS1 and ACR" (p. 6, l. 206 to 207); ACR 8.0 % lies within the MIS3 to HS1 range 4.9 to 9.3 %. PAT: ACR 68.9 % is above the LGM (65.7 %). Sums from Table S5 (Python): PAT + NZ = 79.4 (MIS3), 79.9 (LGM), 81.9 (HS1), 75.5 (ACR), 66.4 (YD), 54.9 (Holocene); PAP + SAF + AUS = 20.6, 20.1, 18.2, 24.3, 33.6, 44.8. The ACR differs from MIS3 by 3.7 points; the step to the YD is 9.3 points and to the Holocene a further 11.2. Only PAP rises at the ACR (2.0 to 5.2 %). The manuscript calls the ACR and YD results tentative (p. 12, l. 407 to 408; GB-46), yet "significantly increased" contributions at the onset of the ACR rest on the period it calls tentative, and no test is reported. The date also varies: "after ~14.5 kyr BP" (p. 7, l. 225; p. 1, l. 23), "at the onset of the ACR" (l. 233), which Section 3 places at 14.7 kyr BP (p. 6, l. 186), and "after ~14.7 kyr BP" (p. 10, l. 315); the 14.5 kyr date may come from the moving average of Fig. S5 ("between 15 and 14 kyr BP", p. 13, l. 445), a different basis from the period means. Grammar in l. 233 and l. 236 is KK-24 and KK-25. |
| Suggestion | In p. 7, l. 225 to 226 and l. 233 to 236 and p. 14, l. 477 to 480 either state the shift with the basis that shows it (for example a change-point analysis on the sample series of Table S1, with the uncertainty of the date) or describe it as a stepwise change that becomes clear in the YD and Holocene; replace "significantly" by a tested statement or remove it; use one date throughout and repeat the ACR caveat in Sections 4.1 and 5. |
| Status | values verified (Table S5 and text, page images p. 6, 7, 14); sums inferred (Python) |
| Severity | major |
| Source | S4, S1 |

**GB-33 The Sr-Nd validation claims agreement with values "measured in EDC" for glacial and interglacial intervals, but all measured Holocene values in Table S4 and Fig. 2 come from Taylor Glacier and Berkner Island, and the agreement is not quantified**

| Field | Content |
|---|---|
| Check | P15, P10, P19, P3, P2 |
| Location | p. 7, l. 238 to 240; p. 8, l. 254 to 260; Fig. 2, p. 26; Suppl. p. 21, Table S4 |
| Quotation | "Overall, the close agreement between our modeled isotopic compositions and those measured in EDC for both glacial and interglacial intervals supports the robustness of our DEPOT algorithm" |
| Concern | The forward calculation of Sr-Nd is a useful independent check, and it delivers aim 2 (p. 3, l. 93 to 94). Table S4 (page image Suppl. p. 21) lists 35 measured values: Iso LGM 6 (EDC 2, Taylor Glacier 4), Iso HS1 3 (Old Dome C 1, Taylor Glacier 2), Iso ACR 2 and Iso YD 2 (Taylor Glacier), Iso Holocene 22 (Taylor Glacier 8, Berkner Island 14; εNd minus 2.30 to minus 14.71) (Python: 6 + 3 + 2 + 2 + 22 = 35). No EDC Holocene value is in Table S4 or Fig. 2. The EDC Holocene values of p. 7, l. 239 to 240 (~0.710; minus 4.51 to minus 5.68) stand in the sentence that cites Delmonte et al. (2004) for the LGM, without saying whether they come from that study, and they are not plotted. Three recomputations show what the comparison can support. (a) From period means of Table S1 with Eq. 3 and 4 and Table S3: Holocene 0.7101 and εNd minus 4.99, which agrees with the EDC values in the text (PP-30). (b) Per sample (Table S1 and S3, ANT omitted): Holocene median εNd minus 2.44 (range minus 16.52 to 2.20), median 87Sr/86Sr 0.7091; 8 of 116 Holocene samples (6.9 %) fall within minus 5.68 to minus 4.51 (Python). (c) Measured on Fig. 2 (600 dpi; 0.700 at 310.5 px, 0.730 at 2976 px; εNd 5 at 55.5 px, minus 25 at 1578 px): at least 57 filled Holocene dots spanning εNd plus 2.1 to minus 16.5, of which 5 lie near the EDC Holocene range; the open Berkner Island circles lie at minus 7.3 to minus 14.7, where many modelled Holocene dots plot. The mean of the model thus matches the EDC Holocene values, while the samples spread far beyond them, and the plotted measured values belong to other cores. "close agreement" is not quantified for any period. How the plotted values were calculated is GB-34; the glacial cluster is GB-35. |
| Suggestion | Add the EDC Holocene values (with their source) to Table S4 and Fig. 2 with their own symbol, name the cores of the open symbols in the legend, and restrict "measured in EDC" in p. 8, l. 258 to the LGM unless EDC Holocene data are plotted; quantify the agreement per period (difference between modelled and measured means, share of samples within the measured range), and propagate the Monte Carlo spread and the end-member variability into the modelled values. |
| Status | Table S4 content: verified (page image); recomputations (a) and (b): inferred (rounded supplement values); positions in Fig. 2: verified by measurement, counts are lower bounds because overlapping dots were not separated |
| Severity | major |
| Source | S3, S4, AB, SD |

**GB-34 Figure 2 plots one calculated value per sample, while the method text describes one calculation per time interval**

| Field | Content |
|---|---|
| Check | P3 |
| Location | p. 8, l. 244 to 246; Fig. 2, p. 26 |
| Quotation | "For each time interval of the LGIT, the relative contribution of each PSA (CONTR) was multiplied by its average Sr and Nd concentrations" |
| Concern | Eq. 3 and 4 are clearly written, and the figure shows their result. Read literally, p. 8, l. 244 to 246 yields one value per interval (six or seven points). Fig. 2 shows many filled dots per interval: counted on the 600 dpi image (legend markers excluded), at least 37 blue (EDC LGM), 19 cyan (HS1), 4 green (ACR), 30 dark red and 27 light red components. A reader cannot tell whether CONTR is the contribution of each sample or an interval mean, nor whether MIS3 samples are included in "EDC LGM" (the legend has no MIS3 entry, while l. 251 speaks of "MIS3/LGM"). The comparison itself is GB-33; the notation in l. 246 is KK-26. |
| Suggestion | State in p. 8, l. 244 that Eq. 3 and 4 were applied to each DIC sample (if so), give the number of plotted samples per interval in the caption of Fig. 2, and add MIS3 to the legend or state that MIS3 samples are shown as LGM. |
| Status | counts verified (page image); number of hidden dots inferred |
| Severity | moderate |
| Source | AB |

**GB-35 Not all glacial and deglacial modelled values cluster at low 87Sr/86Sr and high εNd as stated, and the modelled values are given only as symbols**

| Field | Content |
|---|---|
| Check | P3, P22, P1, P12 |
| Location | p. 8, l. 251 to 254; Fig. 2, p. 26; Suppl. p. 20, Table S3 |
| Quotation | "The modeled isotopic signatures for the end of MIS3/LGM, HS1, ACR, and the YD (represented on Figure 2 by blue, cyan, green, and yellow filled symbols) cluster around lower 87Sr/86Sr and higher ε(Nd)" |
| Concern | The modelled values appear only as symbols; no table gives them, and to recompute them the reader must combine Table S3 (end-members for S-Puna and S-Altiplano separately), Table S5 (only PAP) and Table S1 (the split). Two recomputations disagree with the sentence, and they were reconciled here: (a) from period means of Table S1 (Eq. 3 and 4, Table S3): MIS3 0.70831 and minus 3.37, LGM 0.70834 and minus 2.62, HS1 0.70757 and minus 1.55, ACR 0.70817 and minus 2.91, YD 0.70943 and minus 5.39, Early Holocene 0.71017 and minus 4.76, Late Holocene 0.71010 and minus 5.22; the YD mean lies within the Holocene range of p. 7, l. 240, driven by SAF 14.6 % with εNd minus 18.61. (b) Per sample, as plotted (GB-34): one yellow dot (colour #fcc404, the legend field "EDC YD") lies at 0.7275 and minus 17.88, next to the SAF end-member (0.7280, minus 18.61), consistent with the YD sample at 12227 yr BP with 94.7 % SAF; two green ACR dots lie at (0.7105, minus 5.3) and (0.7116, minus 9.8). Both bases show that the YD, and part of the ACR, do not belong to the glacial cluster. The validation against measured values is GB-33. |
| Suggestion | Add a supplementary table of the modelled 87Sr/86Sr and εNd per sample and per period (with the PAP split used), and revise p. 8, l. 251 to 254 ("most" rather than all symbols; the YD with the Holocene or as a transition; name the SAF-dominated YD sample). |
| Status | (a) inferred (recomputed from rounded supplement values); (b) verified (measurement, colour match) |
| Severity | moderate |
| Source | S3, AB, S2 |

**GB-36 Several conclusions use stronger verbs than the evidence: the mechanisms are inferred from coincidence in time, but the text says "demonstrate", "confirm", "explain", "due to" and "significantly"**

| Field | Content |
|---|---|
| Check | P15 |
| Location | p. 8, l. 271 to 272; p. 9, l. 306; p. 14, l. 466 to 468; p. 14, l. 480 to 484 |
| Quotation | "Importantly, our data demonstrate that these feedback mechanisms influenced dust deposition not only in EDML" |
| Concern | The record shows a change in composition and its timing. The mechanisms (shelf submergence, drainage reversal, aridity) are taken from the literature and linked by coincidence in time ("this provenance shift coincides with", p. 13, l. 450); no test separates them, and an alternative wind-based explanation exists in the literature (GB-08). "confirm" (p. 14, l. 480) covers the earlier EDML attribution, which is not tested here either. For the 18 to 15 kyr decline the Discussion writes "likely reflects intensified" rainout (p. 9, l. 296), which the Conclusion turns into "due to changing atmospheric transport dynamics" (p. 14, l. 484). "These factors collectively explain the predominance" (p. 8, l. 271) rests on the same kind of argument. "reveals a significantly larger variability" (p. 9, l. 306) has no variance test, and the samples near the detection limit lie in this interval (p. 6, l. 174 to 177), so analytical noise is a second possible cause; the sample-level noise is GB-26. The hyphen in l. 272 is KK-31. |
| Suggestion | Replace "demonstrate" (p. 14, l. 466) by "are consistent with"; "As such those results confirm our previous study on the EDML dust record showing similar shift" (l. 480 to 481) by "These results are consistent with our previous study on the EDML dust record, which showed a similar shift"; "due to" (l. 484) by "likely due to"; "explain" (p. 8, l. 271) by "can explain"; in p. 9, l. 306 report a variance comparison per period with a test, or delete "significantly". |
| Status | wording: verified; absence of a mechanism test: verified by reading Sections 2 to 4 |
| Severity | moderate |
| Source | S4 |

**GB-37 Several values in Sections 4.2 and 4.3 differ from the Results, Table S5 and Fig. 3, among them the LGM contribution of New Zealand (~11 % against 14 %)**

| Field | Content |
|---|---|
| Check | P2, P15, P3, P1 |
| Location | p. 9, l. 276; p. 9, l. 281 to 282; p. 9, l. 293 to 295; p. 10, l. 321 |
| Quotation | "However, we find a higher average NZ contribution (~11%), making it the second-largest dust source to EDC during the LGM." |
| Concern | The Results say "NZ was the second-largest contributor during the LGM with an average of 14%" (p. 7, l. 208 to 209), Table S5 gives LGM NZ 14.2 %, and in Fig. 3 (LGM, NZ) the mean cross lies at 15.1 % and the median at 15.4 % (measured; 6.97 px per %). From Table S5 (Python): LGM PAT + AUS = 65.7 + 10.2 = 75.9 %, not "~77%" (l. 276); LGM PAT + NZ = 79.9 % and AUS + SAF + PAP = 20.1 %, not "~79 %" and "~21 %" (l. 294); HS1 PAT + NZ = 74.8 + 7.1 = 81.9 %, not "84 %" (l. 295); Holocene PAT + CWA + PAP = 49.0 + 0.0 + 11.0 = 60.0 %, which l. 326 states and l. 321 gives as 61 %. The values ~11 and ~77 match the means of MIS3 and LGM ((9.1 + 14.2)/2 = 11.65; (79.4 + 75.9)/2 = 77.65), which would be other quantities. In l. 275 to 276 the cited model range refers to "SSA and AUS", while the EDC value is given for PAT + AUS; SSA + AUS in the LGM is 65.7 + 3.6 + 0.0 + 10.2 = 79.5 %. The contrast with Coppo et al. (2022) (5 % NZ) and with EDML (~6 %, l. 288) depends on the NZ value. Question to the authors: is ~11 % meant as the mean of MIS3 and LGM? |
| Suggestion | In p. 9, l. 282 replace "(~11%)" by "(~14%)" or name the interval; in l. 276 write "~76%" (or give SSA + AUS = ~80 % to match the cited quantity); in l. 294 "~80 %" and "~20 %"; in l. 295 "82 %"; in p. 10, l. 321 "60%"; check the remaining Discussion values against Table S5. |
| Status | values verified (text, Table S5, Fig. 3 by measurement); sums inferred (Python); MIS3 and LGM mean as origin: assumption |
| Severity | moderate |
| Source | S3, S4, AB |

**GB-38 The relation of provenance to regional climate (aim 3) is assessed only by visual matching, without a common time axis, age uncertainty or a quantitative measure**

| Field | Content |
|---|---|
| Check | P10, P31 |
| Location | p. 10, l. 338 to 340; p. 11, l. 350 to 352; p. 11, l. 371 to 372 |
| Quotation | "Overall, our Holocene provenance record for PAT contributions is matching well with the SWW intensity proxies in Potrok Aike bog (see Figure 5)." |
| Concern | Aim 3 (p. 3, l. 95) asks for a relation between provenance shifts and regional climate. The instrument is a visual comparison with records on their own age models; no correlation, lag analysis or significance test is reported, and the ice-core age uncertainty is not considered (see GB-11). Together with the sample-level variability (GB-26, which concerns the noise of the record, whereas this finding concerns the missing test), "matching well" cannot be assessed. A specific feature claimed in the comparison is GB-41; the naming of the record is GB-39. |
| Suggestion | Resample the PAT record and the Potrok Aike MDF record to a common time step, compute a correlation with significance against autocorrelated surrogates, include the age uncertainty of both records, and apply the same to the AUS and SAF comparisons in Section 4.3, or present these passages as hypotheses. |
| Status | verified (absence of a metric in Section 4.3 and Fig. 5) |
| Severity | moderate |
| Source | SD |

**GB-39 The Potrok Aike record is called a bog in the text and a lake in Figure 5 and in the cited source**

| Field | Content |
|---|---|
| Check | P38 |
| Location | p. 10, l. 339 to 341; p. 11, l. 348 to 349; p. 29, l. 881 to 882; p. 19, l. 690 to 692 |
| Quotation | "the SWW intensity proxies in Potrok Aike bog (see Figure 5)"; "(Potrok Aike bog 52°S; Lago Cardiel 48.9°S" |
| Concern | All five occurrences of "Potrok" (text.json, main text, captions and references: l. 339, 348, 351, 692, 882) refer to the same record, the rock-magnetic wind proxy of Lisé-Pronovost et al. (2015). The text calls the site a bog twice; the caption (p. 29, l. 881 to 882) and the reference title (p. 19, l. 692, "from lacustrine sediments of Laguna Potrok Aike") call it a lake, and the y axis of Fig. 5B reads "Laguna Potrok Aike 52°S" (page image p. 29). Bog and lake are different archive types. In the same sentence, SWW is used in l. 339 before its definition in l. 340 to 341 ("South Westerlies Winds (SWW)"). The comparison itself is GB-38. |
| Suggestion | Replace "Potrok Aike bog" by "Laguna Potrok Aike" in p. 10, l. 339 to 340 and p. 11, l. 348 to 349; define SWW at its first use in l. 339 as "Southern Westerly Winds (SWW)" and write "a weakening of the SWW" in l. 340 to 341. |
| Status | verified (all occurrences on the page images p. 10, 11, 29 and in the reference list) |
| Severity | minor |
| Source | S2, S4, AB |

**GB-40 Figure 5 is cited before Figure 4**

| Field | Content |
|---|---|
| Check | P3, P4 |
| Location | p. 10, l. 340; p. 12, l. 405 |
| Quotation | "(see Figure 5)" |
| Concern | Search in text.json, p. 1 to 22, for "Fig", "Figure" and "Figures": first citations Fig. 1 p. 6, l. 183; Fig. 2 p. 8, l. 244; Fig. 3 p. 9, l. 281; Fig. 5 p. 10, l. 340; Fig. 4 p. 12, l. 405. The numbering does not follow the order of first citation; the supplementary figures are in order (S1 l. 127, S2 l. 167, S3 l. 355, S4 l. 382, S5 l. 405). The sentence in l. 338 to 340 is concerned by GB-38 and GB-39. |
| Suggestion | Swap the numbers of Fig. 4 and Fig. 5, or move the comparison with Potrok Aike behind Section 4.4. |
| Status | verified (search as stated) |
| Severity | minor |
| Source | AB, S4 |

**GB-41 Figure 5B shows no drop in the Potrok Aike record between 6 and 6.5 kyr BP, which the text says it contains**

| Field | Content |
|---|---|
| Check | P24 |
| Location | p. 11, l. 350 to 351; Fig. 5, panel B, p. 29 |
| Quotation | "Apart from a well-marked drop in PAT contributions between 6-6.5 kyr BP (also present in Potrok Aike wind intensity record)" |
| Concern | Panel B calibrated (y: 10 mT at 1266.5 px, 60 mT at 1567 px, 0.17 mT per px; x: 0.5 at 685.5 px, 3 at 1788.5 px). The bold curve spans 13.9 to 21.6 mT in 5.0 to 5.5 kyr, 16.6 to 20.4 in 5.5 to 6.0, 16.6 to 18.4 in 6.0 to 6.5, 15.4 to 17.6 in 6.5 to 7.0 and 14.9 to 17.9 in 7.0 to 7.5 kyr; the 6.0 to 6.5 kyr window has the smallest range of the five, without a minimum, while the curve reaches about 55 mT within the blue band (8 to 11.4 kyr BP). The PAT drop itself is visible in panel A and in Fig. 1 (minimum 26.4 % at 6.28 kyr BP, PP-25). Whether the source record has a feature below the plotted resolution is not known. This is part of the visual comparison of GB-38. |
| Suggestion | Show the 6 to 6.5 kyr BP feature in the Potrok Aike record (for example in an inset at the original resolution of Lisé-Pronovost et al., 2015) or delete the parenthesis in p. 11, l. 351. |
| Status | verified (measurement at the plotted resolution); a feature below this resolution: assumption |
| Severity | moderate |
| Source | AB |

**GB-42 The Altiplano panel of Figure S3 does not reproduce Table S1 and Fig. 1, and both Table S1 and Fig. S3 show Altiplano contributions before the stated onset at 11.2 kyr BP**

| Field | Content |
|---|---|
| Check | P24, P2 |
| Location | p. 11, l. 357 to 358; Suppl. p. 6, Fig. S3, panel Altiplano |
| Quotation | "the Southern Altiplano begins contributing dust only after approximately 11.2 kyr BP" |
| Concern | Raw peaks in the Altiplano panel of Fig. S3 (y: 100 at 67.5 px, 0 at 792 px; x: 0.4 at 758.5 px, 3.2 at 2503.5 px; ±0.016 kyr per px): 30.9 % at 3.56 kyr, 34.1 at 4.86, 46.5 at 6.17, 66.1 at 6.37, 27.2 at 8.87 and 38.9 % at 11.87 kyr BP; no value above 66.1 %. Table S1 gives Altiplano 100.0 % at 8629 yr and 75.7 % at 9957 yr, and Fig. 1 shows PAP 98.8 % at 8.66 kyr and 97.1 % at 11.23 kyr (GB-28), so Fig. S3 misses the two largest Altiplano contributions of the record. Before 11.2 kyr BP, Table S1 has Altiplano 16.6 % and 12.8 % in the two YD rows dated 12841 yr (page image Suppl. p. 13), and Fig. S3 shows 38.9 % at 11.87 kyr BP and a non-zero smoothed line up to about 12.8 kyr BP. The onset is linked to the final desiccation of paleolake Coipasa (l. 358 to 360). Question to the authors: does Fig. S3 plot another statistic (for example means instead of medians of the Monte Carlo runs), or is it a plotting error? The y labels read "Altiplano" and "Puna", the text "Southern Altiplano" and "South Puna". |
| Suggestion | State in the caption of Fig. S3 which statistic is plotted, replot the Altiplano panel from the values of Table S1, revise p. 11, l. 357 to 358 to the onset the data show (or explain why the two 12841 yr rows are disregarded) and check whether the link to the Coipasa desiccation still holds; label the panels "South Altiplano" and "South Puna". |
| Status | verified (figure by measurement; Table S1 values at the page images); cause: assumption |
| Severity | moderate |
| Source | AB, S3 |

**GB-43 Six works cited in the supplement and one in the main text have no entry in the reference list**

| Field | Content |
|---|---|
| Check | P4 |
| Location | p. 11, l. 365; Suppl. p. 21, Table S4, column Reference; Suppl. p. 16 to 19, Table S2, column Reference; p. 16, l. 502 to p. 22, l. 846 |
| Quotation | "with the previous Pb isotopic study (Gili et al., 2016) ." |
| Concern | Matching of all author-year citations in the main text (p. 1 to 15 and captions) and the supplement against the 91 entries of the reference list, both directions: Gili et al. 2016 has no entry (Gili entries for 2017 and 2022 only). Aarons et al. 2017, Bory et al. 2010 (Table S4), Diaz et al. 2018, Marx and Kamber 2010, Marx et al. 2005 and McGowan et al. 2005 (Table S2) have no entry, and the supplement has no reference list of its own (its last page ends with Table S5). These works supply the source patterns (Marx and Kamber 2010 for 101 rows of Table S2) and the measured isotope values of Fig. 2 (Table S4; see GB-33). "Delmonte et al., 2004a" in Table S4 implies a 2004b, but the list has one Delmonte 2004 entry. The spacing before the full stop in l. 365 is KK-43, the spelling of EPICA in Table S4 KK-23; the format of the list is GB-51. |
| Suggestion | Add entries for Gili et al. (2016), Aarons et al. (2017), Bory et al. (2010), Diaz et al. (2018), Marx and Kamber (2010), Marx et al. (2005) and McGowan et al. (2005) to the reference list or to a supplement reference list, and resolve "2004a". |
| Status | verified (search as stated; supplement read via supplement/text.json) |
| Severity | moderate |
| Source | S4 |

**GB-44 Figure S4 cannot show the Holocene SAF trend it is cited for**

| Field | Content |
|---|---|
| Check | P3, P4 |
| Location | p. 12, l. 382; Suppl. p. 8, Fig. S4 |
| Quotation | "results show an increasing trend in SAF dust contribution to EDC ice core (Figure S4)" |
| Concern | Fig. S4 has one Holocene panel ("Early Holocene") next to YD, ACR, HS1 and MIS3, so it gives no trend within the Holocene. The trend is visible only by comparing the mislabelled panels of Fig. 3 and Fig. S4 (GB-53) or in the time series of Fig. 1 and Fig. S3. |
| Suggestion | Cite Fig. 1 and Fig. S3 in p. 12, l. 382, or add Early and Late Holocene panels to Fig. S4 after the correction of GB-53. |
| Status | verified |
| Severity | minor |
| Source | AB, S4 |

**GB-45 The EDC minus EDML differences stated in Section 4.4 do not match Table S5 and Fig. 4 for ACR and YD, and the Holocene difference compares the whole EDC Holocene with the EDML Early Holocene, contrary to the stated common interval**

| Field | Content |
|---|---|
| Check | P2, P21, P3, P15, P5 |
| Location | p. 12, l. 405 to 407; p. 13, l. 421 to 424; Fig. 4, p. 28; p. 28, l. 875 to 876 |
| Quotation | "the ACR and YD intervals exhibit a slight enrichment of Patagonian dust (+4 and +6.5%) in EDC, primarily at the expense of Southern African and Australian contributions."; "EDC appears to receive substantially less PAT dust (-14%) but higher contributions of Australian dust (+12%) than EDML." |
| Concern | The LGM and HS1 statements match Table S5 and Fig. 4 (PP-33). From Table S5 (Python): ACR PAT +6.4, SAF minus 4.4, AUS minus 7.4; YD PAT +4.7, SAF +6.4, AUS minus 4.5, NZ minus 3.9, PAP minus 2.4. Bars of Fig. 4 measured (10 at 790.5 px, 0 at 857 px, minus 10 at 922 px; about ±0.3 %): PAT ACR +6.3, YD +4.8; SAF YD +6.3. (a) The PAT values in l. 422 are in reverse order. (b) In the YD, EDC has more SAF than EDML, so the YD gain in PAT is not at the expense of Southern Africa; the YD losses are AUS, NZ and PAP. (c) Table S5 has an EDML Holocene row only for 7.5 to 11.7 kyr, and the comparison is defined over the "overlapping interval ... between 7.5 and 27 kyr BP" (p. 12, l. 406 to 407). The Holocene bars of Fig. 4 (PAT minus 13.5, AUS +12.2, SAF minus 0.5, NZ minus 0.2, PAP +1.4, measured) and the values of l. 424 equal EDC Holocene 2.8 to 11.7 kyr minus EDML Early Holocene (minus 13.7 and +12.3); like for like (EDC Early Holocene minus EDML Early Holocene) gives minus 15.6 and +14.1. The comparison thus includes the 60 Late Holocene EDC samples outside the overlap; the direction stays, the size changes. (d) No uncertainty is attached to any difference, although ACR and YD rest on 8 and 9 samples (GB-46), and the comparison is concerned by the EDML configuration (GB-18). The figure order is GB-40; the table reference and the term "Histograms" in the caption are GB-14 and KK-62. |
| Suggestion | In p. 13, l. 421 to 422 write "(+6.4 and +4.7 % for ACR and YD)" and name AUS, NZ and PAP as the compensating sources for the YD; recompute the Holocene bars of Fig. 4 from the EDC Early Holocene, label them "Early Holocene", and give minus 15.6 and +14.1 in l. 423 to 424; give each difference with a bootstrap interval from the per-sample values of both cores. |
| Status | Table S5 values: verified (page image); differences: inferred (Python); bar heights: verified by measurement; which rows were subtracted for the Holocene bars: inferred from the agreement with Table S5 |
| Severity | moderate |
| Source | S3, S4, AB, SD |

**GB-46 The ACR and YD results rest on 8 and 9 samples; the reservation is given only in Section 4.4 and with a wrong YD count**

| Field | Content |
|---|---|
| Check | P2, P17, P36 |
| Location | p. 12, l. 407 to 409; p. 6, l. 192 to 193; p. 6, l. 207 |
| Quotation | "results for ACR and YD are tentative due to the limited number samples covering those periods in EDC (8 and 7 samples in ACR and YD," |
| Concern | The manuscript rightly flags the ACR and YD results as tentative. The YD block of Table S1 (page image Suppl. p. 13) holds 9 rows: 11779, 11993, 12227, 12477, 12588, 12754, 12841, 12841, 12867; their mean (PAT 63.06, PAP 4.53, SAF 14.63, AUS 14.50, NZ 3.28) is exactly the YD row of Table S5 (63.1, 4.5, 14.6, 14.5, 3.3); the ACR count of 8 (13032 to 14601) matches. Two of the 9 YD rows are the same-age pair of GB-24. The reservation is not given where the periods are reported: Section 3 states the PAT decline in ACR and YD (p. 6, l. 192 to 193) and "a sharp increase during the YD with 15%" for SAF (l. 207) without it, and no spread is given for any period mean (GB-19). The EDML counts (47 and 27) cannot be checked from the manuscript. The same paragraph is concerned by GB-18 and GB-45; the grammar of l. 408 is KK-50. |
| Suggestion | Correct "7" to "9" in p. 12, l. 408 (or state which two YD samples were excluded and recompute the YD values); move the reservation to Section 3 where the periods are introduced (p. 6, l. 183 to 188), and give n per period and a spread in Table S5. |
| Status | verified (count on the page image, mean recomputed) |
| Severity | moderate |
| Source | S3, SD |

**GB-47 The Conclusion does not take up research aims (1) and (2): it has no statement on the Holocene provenance debate and none on the Sr-Nd validation**

| Field | Content |
|---|---|
| Check | P15 |
| Location | p. 14, l. 472 to p. 15, l. 492; p. 3, l. 91 to 94 |
| Quotation | "(1) establishing a quantitative record of dust provenance in EDC throughout the LGIT and particularly during the Holocene for which there is no consensus" |
| Concern | Search in the Conclusion (p. 14, l. 472 to p. 15, l. 492, text.json, case-sensitive) for "Holocene", "isotop", "Sr", "Nd", "validat" and "REE": 0 hits; "interglacial" (any case) 3 hits (l. 473, 474, 492), all within "Glacial-Interglacial", "glacial to interglacial" or "glacial-interglacial". Aim 1 names the Holocene as the period of particular interest, and Section 4.3 compares with Kok et al. (2021) and Coppo et al. (2022), but the Conclusion states no Holocene result and does not say how the record bears on the named disagreement; Paleari et al. (2019) is not discussed in Sections 4 and 5 (search "Paleari", p. 7, l. 219 to p. 15, l. 492: 0 hits). Aim 2 is answered in Section 4.1, with the limits of GB-33, but not in the Conclusion. The first sentence of the Conclusion is part of GB-01, the timing in l. 477 to 480 is GB-32, the verbs of l. 466 to 484 are GB-36, and the iron-fertilization frame, whose only trace in the Conclusion is l. 491, is GB-05. |
| Suggestion | Add to Section 5 one sentence on the Holocene composition (for example PAT 49 %, AUS 23 %, PAP 11 %, SAF 11 %, Table S5) and its relation to Paleari et al. (2019), Coppo et al. (2022) and Delmonte et al. (2007), and one on the outcome and scope of the Sr-Nd comparison. |
| Status | verified (search as stated, confirmed on the page images p. 14 and 15) |
| Severity | moderate |
| Source | S4 |

**GB-48 The Conclusion attributes the EDC and EDML differences to source-area climate, while the Discussion attributes them to the position of the two sites in the atmospheric circulation**

| Field | Content |
|---|---|
| Check | P15 |
| Location | p. 14, l. 486 to 487; p. 13, l. 424 to 443 |
| Quotation | "the relative contributions of PAT, SAF, NZ and AUS differed reflecting regional climatic dynamics in their respective source areas" |
| Concern | Section 4.4 explains the differences by site position: "These differences are consistent with the geographic positioning of the two sites" (p. 13, l. 424 to 425), EDML exposed to the Atlantic storm track, EDC insulated by the polar vortex, intrusions by Rossby waves and the STJ and PFJ (l. 425 to 435), and "atmospheric circulation modulates dust delivery" (p. 12, l. 416). Source-area climate cannot explain differences between two cores that sample the same sources at the same time; it explains the common changes (p. 13, l. 444 to 447). The Conclusion therefore gives for aim 4 an explanation the Discussion does not give. The coverage of the other aims by the Conclusion is GB-47; the wording of l. 426 to 428 is KK-51 and KK-52. |
| Suggestion | In p. 14, l. 487 replace "reflecting regional climatic dynamics in their respective source areas" by the explanation of Section 4.4, for example "reflecting the different exposure of the two sites to mid- and low-latitude air masses". |
| Status | verified |
| Severity | moderate |
| Source | S4 |

**GB-49 The CODE/DATA AVAILABILITY statement says nothing about code and claims that all data needed are present, but code, input data and intermediate results are missing**

| Field | Content |
|---|---|
| Check | P12, P6, P18 |
| Location | p. 16, l. 494 to 496 |
| Quotation | "All data needed to evaluate the conclusions in the paper are present in the paper and/or the Supplementary Materials. Additional data related to the paper may be requested from the authors." |
| Concern | The supplement publishes the source database (Table S2) and the model outputs (Tables S1 and S5), which allows the period values to be checked (PP-18). Missing are: (1) code: the DEPOT implementation in MATLAB (p. 5, l. 139 to 140), the Monte Carlo loop and the R computation (l. 153 to 172) and the figure scripts; search of main text and supplement for "code" (any case), "GitHub", "Zenodo", "repository" and "10.5281": 1 hit, the heading word "CODE" in l. 494; (2) inputs: the 279 corrected and normalised EDC REE patterns (only the origin, Gabrielli et al. 2010, is cited), the cfi values (GB-12), the per-element uncertainties (only the range 2 to 10 %, p. 5, l. 155 to 156), the 38 excluded samples (GB-23); (3) links between output and input: Table S1 identifies samples only by age, with four duplicated ages (GB-24), so its rows cannot be matched one to one to the original samples; (4) intermediate and derived results: DS-level contributions (GB-27), per-sample spreads (GB-19), PSA fluxes (GB-20), modelled Sr-Nd values (GB-35), per-sample EDML values behind Fig. 4 and Fig. S5. The second sentence reserves "Additional data" without saying what they are or why they are withheld, although no personal data are involved. Whether the Gabrielli et al. (2010) REE data are archived publicly could not be established (one search; the NOAA record found holds Pb isotopes and Ba). |
| Suggestion | Deposit the DEPOT and Monte Carlo code, the input matrices, the cfi set, the excluded samples, a sample identifier or depth for each row of Table S1 and the intermediate results in a public repository with a DOI and licence, and revise p. 16, l. 494 to 496 to name it, or state the reason for any restriction. |
| Status | statement wording and absence of code and inputs: verified (search as stated); public archive of the original REE data: inferred (one search only) |
| Severity | moderate |
| Source | S2, SD |

**GB-50 The author contribution statement names "P.B", which matches none of the seven authors, and gives no role to N.M.**

| Field | Content |
|---|---|
| Check | P4 |
| Location | p. 16, l. 497 to 499; p. 1, l. 4 to 5 |
| Quotation | "P.B performed the measurements; A.V., St. B and G.L. developed together the model" |
| Concern | The authors are Sibylle Boxho, Aubry Vanderstraeten, Nadine Mattielli, Goulven G. Laruelle, Aloys Bory, Paolo Gabrielli and Steeve Bonneville (p. 1, l. 4 to 5). No author has the initials P.B.; the measurements of the dataset were published by Gabrielli et al. (2010) (p. 4, l. 108), so P.G. is a possible reading, A.B. another. N.M. is covered only by "All authors reviewed". The initials are written inconsistently ("St. B", "St.B.", "Si.B"). Question to the authors: which author is meant by "P.B"? |
| Suggestion | Correct "P.B" in p. 16, l. 497 (for example to "P.G." if Paolo Gabrielli is meant), give N.M. a role if applicable, and unify the initials ("Si.B.", "St.B."). |
| Status | absence of matching initials: verified; intended author: assumption |
| Severity | minor |
| Source | S4, S2 |

**GB-51 The reference list prints RTF escape codes and trailing backslashes in 18 entries and mixes citation formats**

| Field | Content |
|---|---|
| Check | P16 |
| Location | p. 16, l. 528; p. 17, l. 553; p. 18, l. 632; p. 19, l. 703; p. 22, l. 821; formats: p. 17, l. 584 to 585; p. 18, l. 633 to 636; p. 20, l. 729; p. 20, l. 762 to 763; p. 22, l. 844 |
| Quotation | "471\uc0\u8211{}501. https://doi.org/10.1191/0309133303pp386ra\"; "O\uc0\u8217{}Loingsigh"; "Mall\uc0\u237{}n Pollux" |
| Concern | The codes are printed (page image p. 16, l. 528; S4 confirmed p. 16 to 22). Count in text.json, reference list p. 16 to 22 (Python): 33 sequences of the form "\uc0\u...{}" and 18 lines ending in a backslash (p. 16, l. 528; p. 17, l. 556, 588, 593; p. 18, l. 606, 632, 648, 654; p. 19, l. 694, 707, 710; p. 20, l. 716, 747, 758; p. 21, l. 795, 799; p. 22, l. 821, 828), in the entries Bullard and McTainsh 2003, De Deckker et al. 2014, Dukes et al. 2018, Engelbrecht et al. 2019, Fletcher and Moreno 2012, Gaiero et al. 2007, Gingele and De Deckker 2005, Grousset and Biscaye 2005, Lisé-Pronovost et al. 2015, Markgraf et al. 2007, Markle et al. 2018, Moreno et al. 2010, Power et al. 2008, Quade and Kaplan 2017, Stone et al. 2010, Stuut et al. 2002, Veres et al. 2013 and Wagner et al. 2021. Format: Ding et al. 2011 uses "et al." in the entry and puts the year at the end (p. 17, l. 584 to 585); Gaiero et al. 2013 puts initials before surnames and the year in parentheses (p. 18, l. 633 to 636); Parrenin et al. 2007 has no volume, pages or DOI (p. 20, l. 729); Rudnick and Gao 2003 has "01 Composition" and "Turkian" (p. 20, l. 762 to 763); Yang et al. 2024 uses "&" (p. 22, l. 844). The missing entries are GB-43. |
| Suggestion | Regenerate the reference list from the reference manager so that dashes, apostrophes and accented letters are printed (for example "O'Loingsigh", "Mallín Pollux"), remove the trailing backslashes, and bring the five entries named into the format of the others. |
| Status | verified (page image p. 16; count from text.json, Python) |
| Severity | minor |
| Source | S4 |

**GB-52 The legend and labels of Figure 2 cannot be read without the text and the supplement**

| Field | Content |
|---|---|
| Check | P29 |
| Location | Fig. 2, legend and domain labels, p. 26; p. 26, l. 857 to 866; Suppl. p. 21, Table S4 |
| Quotation | "Compilation of 87Sr/86Sr and εNd isotopic compositions representative of PSA, dust in ice cores" |
| Concern | (1) The legend splits the measured values into "Iso Early Holocene" and "Iso Holocene"; Table S4 has one group "Iso Holocene". Ring colours measured: a Berkner Island circle (0.7228, minus 14.15) is #fcbcbc, matching the legend field "Iso Early Holocene" (#fcc4c4); a Taylor Glacier circle (0.7119, minus 5.6) is #e4acac, the "Iso Holocene" hue. The basis of this split is not given. (2) "Iso" is not explained. (3) The caption says "dust in ice cores" without naming the cores, although four of the six measured groups come from Taylor Glacier and Berkner Island (GB-33). (4) The domain label reads "Southern Central Western Argentina", the text "Central Western Argentina (CWA)" (p. 4, l. 129) and Table S3 "SCWA". (5) The legend has no MIS3 entry (GB-34). The plotted values are GB-35; the table references of the caption are GB-14, its wording KK-60. |
| Suggestion | Explain "Iso" and the two Holocene groups in the caption, give the core of each measured group, and use one name and abbreviation for CWA in Fig. 2, Table S3 and the text. |
| Status | verified |
| Severity | minor |
| Source | AB |

**GB-53 The "Holocene" panel of Figure 3 shows the Early Holocene values of Table S5, and the "Early Holocene" panel of Figure S4 shows the Late Holocene values**

| Field | Content |
|---|---|
| Check | P3 |
| Location | Fig. 3, left panel, p. 27; p. 27, l. 869; Suppl. p. 8, Fig. S4, panel Early Holocene |
| Quotation | "Figure 3: Box plots of provenance contributions (in %) of Holocene, and Last Glacial Maximum (LGM)" |
| Concern | The box plots with means, medians and individual samples are an informative choice. The mean crosses of the Fig. 3 "Holocene" panel (located with a template on the 600 dpi image; 0 at 1432.5 px, 100 at 735.5 px of the 300 dpi image; about ±0.2 %) are PAT 47.1, AUS 24.9, SAF 9.9, NZ 8.1, PAP 10.2 %; Table S5 gives for the Early Holocene 47.1, 24.9, 9.8, 8.1, 10.0 and for the Holocene 49.0, 23.1, 10.7, 5.9, 11.0. The panel matches the Early Holocene within 0.2 points and differs from the Holocene by up to 2.2 points. The Fig. S4 "Early Holocene" means (Suppl. p. 8; 0 at 1981 px, 100 at 167.5 px) are PAT 50.6, AUS 21.7, SAF 11.6, NZ 3.8, PAP 12.7, matching the Late Holocene row (50.7, 21.4, 11.6, 3.8, 12.0). The highest SAF dot in Fig. 3 "Holocene" is about 54 %, whereas the Late Holocene samples at 3.38 and 6.97 kyr BP reach about 72 % and 70 % in Fig. 1 (PP-26) and appear in Fig. S4 "Early Holocene". Either the panels are mislabelled or their windows differ from Table S5; the text compares Holocene and LGM with the Table S5 values (p. 10, l. 316 to 318), and no figure shows the whole Holocene. The use of Fig. S4 for a Holocene trend is GB-44. |
| Suggestion | Relabel the Fig. 3 panel "Early Holocene (7.5 to 11.7 kyr BP)" and the Fig. S4 panel "Late Holocene (2.8 to 7.5 kyr BP)", or replot both with the windows of Table S5; state the windows and the number of samples per panel in both captions. |
| Status | verified (means by measurement, Table S5 at the page image) |
| Severity | moderate |
| Source | AB |

**GB-54 The whiskers in Figures 3 and S4 are not the "lower and upper extremes" the captions state**

| Field | Content |
|---|---|
| Check | P29 |
| Location | Fig. 3, both panels, p. 27; p. 27, l. 872; Suppl. p. 7, caption of Fig. S4 |
| Quotation | "and the whiskers indicate the lower and upper extremes" |
| Concern | Measured on the 300 dpi image: in Fig. 3 Holocene the SAF whisker ends at 25.5 % with dots up to about 54 %, the AUS whisker at 79.8 % with dots at about 84, 95 and 98 %, the NZ whisker at 16.5 % with dots up to about 90 %, the PAP whisker at 28.0 % with dots up to about 100 %; in LGM the SAF whisker ends at 14.4 % with dots at about 28 and 35 %. The plots follow a rule that excludes outliers (for example 1.5 times the interquartile range), which the captions do not name. The panel windows are GB-53. |
| Suggestion | State the whisker rule in the captions of Fig. 3 (p. 27, l. 872) and Fig. S4, and say that points beyond the whiskers are individual samples. |
| Status | verified (measurement) |
| Severity | minor |
| Source | AB |

**GB-55 Figure 5 has no time axis title or unit, and its shaded bands are not explained**

| Field | Content |
|---|---|
| Check | P29 |
| Location | Fig. 5, panels A and B, p. 29; p. 29, l. 880 to 882; p. 10, l. 340 |
| Quotation | "Figure 5: Comparison of the contribution of Patagonian dust (PAT) to EDC ice core (A) and (B) the Median Destructive Field" |
| Concern | (1) Neither panel has an x axis title or unit; the tick labels 0.5 to 3 need the factor 10^4 yr BP that only Fig. 1 states. (2) A blue band bounded by dashed lines spans 7.96 to 11.43 kyr BP (±0.05; ticks 0.5 at 685.5 px, 3 at 1788.5 px), and grey bands mark the periods; the caption explains neither. The text links the band to "The 11 to 8 kyr BP period" (p. 10, l. 340), which differs from the measured 11.43 kyr boundary by more than the uncertainty. The feature claimed for panel B is GB-41, the naming of the record GB-39, the figure order GB-40, the visual comparison GB-38, and the moving average named in l. 882 is GB-17. |
| Suggestion | Add "Time (yr BP) ×10^4" (or kyr BP) to both panels, explain the blue band with its ages and the grey period bands in the caption, and align the band with the 11 to 8 kyr BP of p. 10, l. 340 or correct the text. |
| Status | verified (measurement) |
| Severity | minor |
| Source | AB |

#### Minor corrections

| ID | Location | Quotation | Replacement | Source |
|---|---|---|---|---|
| KK-23 | p. 7, l. 220; Suppl. p. 21, Table S4, column Localisation | "in the Epica Dome C ice core"; "Epica dome C" | "EPICA Dome C" at both places, as in p. 1, l. 18 and p. 3, l. 88; the claim of l. 220 is GB-01, the references of Table S4 GB-43 | S2, S4 |
| KK-24 | p. 7, l. 233 | "highlight a major shift in dust provenance occurred" | "highlight that a major shift in dust provenance occurred"; the content of the sentence is GB-32 | S4 |
| KK-25 | p. 7, l. 236 | "This shift already describes by Gili et al. (2022)" | "This shift, already described by Gili et al. (2022)"; see GB-32 | S4 |
| KK-26 | p. 8, l. 246 | "(Table S3, e.i. Eq.3)" | "(Table S3, i.e. Eq. 3)"; the calculation basis of this sentence is GB-34 | S4 |
| KK-27 | p. 8, l. 249 | "where the mean isotopic signatures is represents by CIR PSA" | "where the mean isotopic signature is represented by CIR_PSA" | S4 |
| KK-28 | p. 8, l. 261 | "4.2 Persistance of high-latitude dust source" | "4.2 Persistence of high-latitude dust sources" | S4 |
| KK-29 | p. 8, l. 266; p. 21, l. 800 | "(Sugden et al., 2009)"; "Sudgen, D. E., McCulloch, R. D." | correct the entry to "Sugden, D. E., McCulloch, R. D., ..." | S4 |
| KK-30 | p. 8, l. 270 | "by ~763.10³ km2" | "by ~763 × 10³ km²" (printed with a superscript 3 on the page image; text.json reads "763.103") | S4 |
| KK-31 | p. 8, l. 272 | "those from SSA- to EDC" | "those from SSA to EDC"; the verb "explain" in l. 271 is GB-36 | S4 |
| KK-32 | p. 9, l. 277 | "(i.e., Albani et al., 2012; Krätschmer et al., 2022)" | "(e.g., Albani et al., 2012; Krätschmer et al., 2022)" | S4 |
| KK-33 | p. 9, l. 300 to 301 | "high-latitude dominance before 14.5 kyr BP reflect a transport regime"; "strong westerlies -a system" | "reflects a transport regime"; "strong westerlies, a system" | S4 |
| KK-34 | p. 9, l. 303 to 304 | "(from 14.5 kyr BP until 2.7 kyr BP)" | "(from 14.5 kyr BP until 2.9 kyr BP)"; youngest retained sample 2852 yr BP (p. 6, l. 182) | S3, S4 |
| KK-35 | p. 10, l. 311; p. 10, l. 313 | "enhanced «wet scavenging»"; "from the mid-latitudes of Indian Ocean" | "enhanced "wet scavenging"" (same quotation marks as "rainout" in p. 9, l. 297); "from the mid-latitudes of the Indian Ocean" (one sentence) | S4 |
| KK-36 | p. 10, l. 329 to 330 | "includes several McMurdo region sites (Section 4.2)" | "includes several McMurdo region sites (Section 2; Table S2)"; Section 4.2 does not mention McMurdo, p. 4, l. 132 to 133 does; the statement of l. 330 is GB-29 | S4 |
| KK-37 | p. 10, l. 334 | "(Speirs et al., 2001)" | "(Speirs et al., 2010)"; entry p. 21, l. 781 | S4 |
| KK-38 | p. 10, l. 338; p. 11, l. 374 | "centered ~9 kyrs BP"; "(post-7.5 kry" | "centered at ~9 kyr BP"; "(post-7.5 kyr"; the sentence after l. 338 is GB-38 | S4 |
| KK-39 | p. 10, l. 341 | "(Fletcher and Moreno, 2012; Moreno et al. (2010); Lisé-" | "(Fletcher and Moreno, 2012; Moreno et al., 2010; Lisé-"; the SWW wording of the same sentence is GB-39 | S4 |
| KK-40 | p. 10, l. 342 to 343 | "(Quake and Kaplan, 2017)" | "(Quade and Kaplan, 2017)"; entry p. 20, l. 755 | S4 |
| KK-41 | p. 10, l. 346 | "Fires co-emit mineral soil-dust particle" | "Fires co-emit mineral soil-dust particles" | S4 |
| KK-42 | p. 11, l. 354 | "Dust emission from PAP are primarily linked" | "Dust emission from PAP is primarily linked" | S4 |
| KK-43 | p. 11, l. 365 | "(Gili et al., 2016) ." | "(Gili et al., 2016)."; the missing entry is GB-43 | S4 |
| KK-44 | p. 11, l. 366 | "As far as Australian dust contribution, our model identifies" | "As for the Australian dust contribution, our model identifies"; the content of the sentence is GB-27, the duplicate patterns GB-15 | S4 |
| KK-45 | p. 11, l. 367 | "De Deccker et al. (2010)" | "De Deckker et al. (2010)" | S4 |
| KK-46 | p. 11, l. 376 | "El-Nino-Southern Oscillation (ENSO)" | "El Niño Southern Oscillation (ENSO)" | S4 |
| KK-47 | p. 12, l. 384 to 385 | "suggesting strengthened dust transport from southern Africa suggesting strengthened dust transport from southern Africa (Stuut et al., 2002)" | "suggesting strengthened dust transport from southern Africa (Stuut et al., 2002)"; the following SAF statements are GB-27 | S4 |
| KK-48 | p. 12, l. 396 to 398 | "but include few substantial inputs"; "coinciding roughly with dry periods of the lake during the LGIT (" | "but include a few substantial inputs"; close the parenthesis before "(Brook et al., 2011)", for example "(about 15.4 to 13.6, 11.5 to 8.4 and 5.5 to 4.0 kyr BP; Brook et al., 2011)" (one sentence); the detection statements of the paragraph are GB-27 | S4 |
| KK-49 | p. 12, l. 399 | "likely reflect their low-frequency, high-magnitude nature of their dust emissions" | "likely reflect the low-frequency, high-magnitude nature of their dust emissions" | S4 |
| KK-50 | p. 12, l. 408 | "due to the limited number samples" | "due to the limited number of samples"; the count in the same sentence is GB-46, the EDML configuration of the paragraph GB-18 | S4 |
| KK-51 | p. 13, l. 426 | "to receive dust from Patagonia dust brought in the mid-" | "to receive Patagonian dust brought in the mid-"; the explanation of this paragraph is used in GB-48 | S4 |
| KK-52 | p. 13, l. 427 to 428 | "located at the interior of EAP"; "from such mid-latitude air masses incursions" | "located in the interior of the East Antarctic Plateau"; "from such incursions of mid-latitude air masses" (one sentence; "EAP" is not defined: 1 hit in the whole text, l. 427); see GB-48 | S4 |
| KK-53 | p. 13, l. 439 | "(De Deccker et al., 2019;" | "(De Deckker, 2019;"; the entry p. 17, l. 551 has a single author; the paragraph is used in GB-48 | S4 |
| KK-54 | p. 13, l. 449 to 450 | "in both cores (Figures S2 and S5)" | "(Figure S2 for EDC; Vanderstraeten et al., 2023, for EDML)"; Fig. S5 shows relative contributions only and Fig. S2 EDC only | S4 |
| KK-55 | p. 14, l. 457 | "redirecting large portion of river catchment" | "redirecting a large portion of river catchments" | S4 |
| KK-56 | p. 16, l. 501 | "APPENDIX S. SUPPLENTARY DATA. Supplementary data to this article" | "SUPPLEMENTARY DATA. Supplementary data to this article are available in the Supplement (Figures S1 to S5, Tables S1 to S5)." | S4 |
| KK-57 | p. 16, l. 536 | "Las glaciaciones cuaternarios en la Patagonia" | "Las glaciaciones cuaternarias en la Patagonia"; the list as a whole is GB-43 and GB-51 | S4 |
| KK-58 | p. 18, l. 630 to 632 | "Gaiero, D.M., Brunet, F., Probst, J.-L., Depetris, P.J., 2007. A uniform isotopic and chemical signature" | cite the entry where intended (for example p. 8, l. 274 or the caption of Fig. 2, which cite "Gaiero, 2007") or delete it; no citation of this four-author entry in main text or supplement; the escape code in l. 632 is GB-51 | S4 |
| KK-59 | p. 20, l. 748 | "Environùental characterization" | "Environmental characterization" | S4 |
| KK-60 | p. 26, l. 859; p. 26, l. 863 | "solid dots (see section 4.1 for details)"; "the SAF and AUS domain is more extended than showed in the Figure" | "EDC (solid dots; see Section 4.1 for details)" in place of the dash between "EDC" and "solid dots"; "the SAF and AUS domains extend beyond the area shown in the figure"; the legend is GB-52 | S4 |
| KK-61 | p. 26, Fig. 2, x axis; p. 27, Fig. 3, y axes | "0,700"; "0,00"; "100,00" | decimal points: "0.700" to "0.730"; "0" to "100" for percentages; Fig. 2 is otherwise concerned by GB-33, GB-34, GB-35 and GB-52 | AB |
| KK-62 | p. 28, l. 875 | "Figure 4: Histograms representing" | "Figure 4: Bar charts representing"; the content of the figure is GB-45 | AB |
| KK-63 | Suppl. p. 7, caption of Fig. S4 | "(3) Antarctica Cold Reveal (ACR), (4) Heindrich Stadial 1 (HS1), and (5) Marine Isotope 3 (MIS3)" | "(3) Antarctic Cold Reversal (ACR), (4) Heinrich Stadial 1 (HS1), and (5) Marine Isotope Stage 3 (MIS3)", as in p. 6, l. 184 to 186; the use of Fig. S4 is GB-44 | S2, AB |
| KK-64 | Suppl. p. 10, Fig. S5, y axis title | "PAS EDC Contribution and PSA EDML Contribution ( in %)" | "PSA EDC and EDML contribution (%)" | AB |

#### Verification log

| ID | Check | Checked | Values | Result |
|---|---|---|---|---|
| PP-30 | P1 | Eq. 3 and 4 with Table S3 and period means of Table S1 against the values of p. 7, l. 238 to 240 | modelled LGM 0.70834 and minus 2.62 against ~0.708 and minus 1.66 to minus 2.46; modelled Holocene 0.71013 and minus 4.99 against ~0.710 and minus 4.51 to minus 5.68; sum of contributions per period 0.995 to 1.000 | no finding for the period means; per-sample spread in GB-33, YD in GB-35 |
| PP-31 | P3 | Fig. 2 colours and counts against Table S4 | legend fields EDC Early Holocene #fc5454, EDC Holocene #c40404, EDC YD #fcc404, EDC ACR #34cc34, EDC HS1 #34ccfc, EDC LGM #0404fc; Table S4 groups 6 + 3 + 2 + 2 + 22 = 35; 4 separate ACR dots counted against 8 ACR samples, hidden dots likely | no finding beyond GB-33 to GB-35 and GB-52 |
| PP-32 | P3 | Fig. 3 LGM panel against Table S5 and p. 9, l. 280 to 295 | means PAT 65.8, AUS 10.3, SAF 7.2, NZ 15.1, PAP 3.6 %; medians 65.8, 10.1, 4.5, 15.4, 1.9 %; Table S5 LGM 65.7, 10.2, 6.3, 14.2, 3.6; SSA 65.8 + 3.6 = 69.4 against "~70%" | no finding except NZ in GB-37; the SAF and NZ crosses deviate by 0.9 points, but both are overlaid by sample dots |
| PP-33 | P2, P3 | EDC minus EDML for LGM and HS1 (p. 13, l. 417 to 421) and the Fig. 4 bars for YD, ACR, HS1 and LGM against Table S5 | LGM NZ +8.0, PAT minus 8.0 ("+8%", "equivalent reduction"); HS1 PAT +3.2, PAP minus 0.2, SAF minus 5.3, AUS +1.9, NZ +0.6 (largest 5.3, "not exceeding ~5%"); 20 bars measured against Table S5, for example PAT +4.8/+4.7, +6.3/+6.4, +3.2/+3.2, minus 7.8/minus 8.0; largest deviation 0.3 | no finding; ACR, YD and Holocene in GB-45 |
| PP-34 | P15, P9 | Outlook and proposals | search p. 14, l. 472 to p. 15, l. 492 for "future", "further", "should", "need", "recommend", "perspective", "outlook", "would", "next": 0 hits; Section 4 for "future", "should be", "need to", "recommend": 0 hits; the Conclusion contains no proposal | no finding; disclosed limits: sampling gap (p. 4, l. 113), ACR and YD tentative (p. 12, l. 407 to 409), exclusion of 38 samples (p. 6, l. 174 to 179) |
| PP-35 | P15 | Statements of Section 5 mapped to Results and Discussion; frame terms | p. 14, l. 474 to 477 glacial dominance: p. 6, l. 189 to 192, l. 209, Table S5; l. 478 to 480 rise of AUS, PAP, SAF: p. 6, l. 202 to p. 7, l. 216 (timing in GB-32); l. 482 to 484 decoupling from the flux decline: p. 9, l. 295 to 299, p. 13, l. 447 to 450; l. 485 to 486 synchronous changes: p. 13, l. 444 to 447; l. 488 to 489 paleolake desiccation: p. 11, l. 358 to 360; LGIT, DEPOT and SWW taken up in Section 4 | no finding beyond GB-32, GB-36, GB-47, GB-48 |
| PP-36 | P18 | Declared principles applied to the manuscript itself | data statement p. 16, l. 494 to 495 (GB-49); no other principle recommended to others | no finding beyond GB-49 |
| PP-37 | P4 | Numbering of sections, equations, figures and supplementary elements; order of first citation | Sections 1 to 5 (4.1 to 4.4); Eq. 1 to 4 (p. 4, l. 125; p. 5, l. 141; p. 8, l. 247, l. 250); Fig. 1 to 5 (p. 24 to 29); Fig. S1 to S5 and Tables S1 to S5 each once; first citations Table S1 l. 127, S2 l. 128, S5 l. 191, S3 l. 246, S4 caption of Fig. 2 | no gaps or duplicates; Fig. 4 and 5 out of order (GB-40) |
| PP-38 | P4 | Author-year citations against the reference list, both directions | 91 entries; 90 distinct citations in main text and captions, 17 in the supplement; without entry: Gili 2016, and in the supplement 6 works plus the suffix 2004a (GB-43); spelling variants Speirs 2001, Quake and Kaplan, De Deccker, Sugden (KK-29, KK-37, KK-40, KK-45, KK-53); without citation: Gaiero et al. 2007 (KK-58); "et al." with more than two authors: only De Deccker et al. 2019 is wrong | GB-43 and the KK named |
| PP-39 | P4 | Cross references that lead to the correct target | p. 5, l. 167 and p. 9, l. 296, 299 and p. 10, l. 312 Fig. S2; Table S5 at l. 191, 216, 218, 281, 295, 318, 326; Fig. 2 at l. 244, 252, 257; Table S3 at l. 246; Fig. 3 at l. 281, 294 to 295; Section 4.2 at l. 310; Fig. 5 at l. 340; Fig. S3 at l. 355; Fig. S5 at l. 405, 409, 446 | no finding; wrong targets in GB-14, GB-28, GB-44, KK-36, KK-54 |
| PP-40 | P16 | Characters seen in text.json that are artefacts | Eq. 1, 2 and 4 split over several lines in text.json but set correctly on p. 4, 5 and 8; superscripts in "87Sr/86Sr" and "763.10³" correct on the page images; "Lisé- Pronovost" at the line break p. 10, l. 341 to 342 is a hyphenated name | no finding for these; printed RTF codes in GB-51 |
| PP-41 | P29, P3 | Inventory of figures and their citations | Fig. 1 p. 24 (5 panels, raster), caption p. 25, cited l. 183, 205, 215, 217, 221, 307, 338; Fig. 2 p. 26, caption l. 857 to 866, cited l. 244, 252, 257; Fig. 3 p. 27, caption l. 869 to 873, cited l. 281, 294 to 295; Fig. 4 p. 28, caption l. 875 to 876, cited l. 405, 419; Fig. 5 p. 29, caption l. 880 to 882, cited l. 340; Fig. S1 to S5 on Suppl. p. 2, 4, 6, 8, 10, each cited; no graphical abstract | every figure cited; order in GB-40 |
| PP-42 | P29 | Fig. S1 (map) | panels PAT, NZ, SAF, AUS, Puna Alti, CWA, ANT, overview; scale bars and north arrows present; several samples per site with nearly identical coordinates, so markers cannot be counted against the DS numbers | no finding; marker count not measurable |
| PP-43 | P29, P24 | Fig. S5 | time axis "Time (in kyr BP)", 7 to 27 kyr, period labels, legend in each panel, font well above 6 pt; p. 13, l. 445 to 446 checked visually only | no finding except KK-64 |
| PP-44 | P29 | Font size Fig. 4 | cap heights "Holo" 19 px = 6.3 pt, tick "10" 20 px = 6.5 pt, panel title 20 px = 6.7 pt, y title 21 px = 7.0 pt | no finding |
| PP-45 | P29 | Placeholders, watermarks and cut-off labels in all figures | p. 24, 26 to 29 and Suppl. p. 2, 4, 6, 8, 10 at 150 and 300 dpi: none; Fig. S1 carries "© Google Earth Pro" in its caption | no finding |
| PP-46 | P38 | Merging: contradictions between instances decided at the manuscript | (1) Table S4: one instance read all Holocene values as Berkner Island and all HS1 values as Taylor Glacier; the page image Suppl. p. 21 shows Holocene 8 Taylor Glacier and 14 Berkner Island, HS1 1 Old Dome C and 2 Taylor Glacier, LGM 2 EDC and 4 Taylor Glacier (GB-33 corrected). (2) Table S1 row count: 240 (one instance, text.json) against 241 (three instances); row 17148 carries the label "HS" in text.json, so 241 (Python). (3) The row of 10511 yr with R 0,66 and sum 93.5 is the first of the pair on Suppl. p. 13 (text.json line order), not the second. (4) Sr-Nd recomputation per period mean against per sample (GB-33, GB-35): both kept, as they answer different questions. (5) The Holocene EDC isotope values of p. 7, l. 239 to 240 stand in the sentence that cites Delmonte et al. (2004); "no citation" (one instance) was narrowed to "source not stated". (6) SAF minimum (PP-23); (7) `formatpruefung.py --paare`: 108 pairs of IDs with overlapping locations; pairs with the same location and subject were merged before (27 substantive findings, 22 minor corrections into findings, 11 minor corrections with each other); the remaining 108 pairs concern different subjects and each later ID names the earlier one with the distinction | decisions entered in GB-33, GB-35, GB-24, PP-23; 0 pairs without cross reference |
| PP-47 | P38 | Locations at page boundaries and on uncounted lines (SKILL step 4.5 and 7): text.json numbers lines per page (randzeilen: false), so every manuscript line was mapped by script from the printed margin numbers (every fifth line); equation lines on p. 4, 5 and 8 were set to one line each from the page images; `formatpruefung.py --fundorte` was run and its list worked through against this map | Page images viewed: p. 3, 4, 5, 7, 9, 13, 16 and Suppl. p. 17, 21. Counts from margin numbers: p. 4 Eq. 1 = l. 125 (printed), l. 126 to 129 counted back from 130; p. 5 l. 139 back from 140, Eq. 2 = l. 141, l. 142 to 144 back from 145; p. 8 l. 246 to 254 between 245 and 255 with Eq. 3 = 247 and Eq. 4 = 250; p. 7 headings l. 219 and 232 counted; first lines of pages counted back from the first printed number and closed against the previous page (p. 2/3, 4/5, 5/6, 6/7, 7/8, 8/9, 9/10, 10/11, 11/12, 12/13, 13/14, 14/15 close without gap; p. 1/2 skips the empty l. 32, p. 15/16 the empty l. 493); caption of Fig. 1 on p. 25 has no reliable line (located by page and element); supplement without line numbers (page and element) | `--fundorte` listed 343 endpoints (332 without entry in text.json, 11 with the line on another page), all because text.json counts lines per page; each was checked against the map by script: every endpoint exists on its page, and every quotation starts inside its location, except the caption of Fig. 1, which is located by element; corrections made during merging: "25 times" is p. 2, l. 63 (not l. 34), the abstract wording on low-latitude inputs p. 1, l. 23 (not l. 28), "241 samples" in the abstract p. 1, l. 19 (not l. 24) |

## Optional checks

| Area | What it needs | Responsible | Run |
|---|---|---|---|
| DOI resolution | one request per reference entry with a DOI | `science-quellenapparat-pruefung` | no |
| Citation style | the name of the style | `science-zitierstil-harvard-ctr` or the style rules of the journal | no |
| AI statement against publisher policy | the policy of the target publisher | this review, on request | no |
| Relation to the authors' earlier work | the earlier work of the authors | this review, on request | no |
| Journal requirements | the author guidelines of the target journal | this review, on request | no |
| Factual accuracy | access to the sources of the checked statements and a selection of sections | `science-faktenbeleg-pruefung`, `geo-frage-belegbasiert-klaeren` | no |

## Limits of this review

- Checked version: egusphere-2025-5046.pdf, 29 pages, SHA-256 f598b53d01e375844cfb549eb05b9a3407bb30cae553e603c125d5f14886c722; supplement egusphere-2025-5046-supplement.pdf, 22 pages, SHA-256 759cfa14195948f5772d3d6d696081932424f4296e51c812415527ed3b108ea6.
- Sources not readable in full: Lambert et al. (2008) (abstract only, full text restricted); Engelbrecht et al. (2019) (abstract only); Delmonte et al. (2008) and Delmonte et al. (2017) (abstracts only); Coppo et al. (2022) (abstract only); Vanderstraeten et al. (2023) (abstract only; whether it contains a recovery test or the EDML configuration is open, GB-18, GB-21); Veres et al. (2013), https://doi.org/10.5194/cp-9-1733-2013 (request rejected, HTTP 429; size of the EDC3 to AICC2012 offset not assessed, GB-11); Paleari et al. (2019) and Gili et al. (2016) (fetch failed); PNAS 2024 South Atlantic mixing study, doi 10.1073/pnas.2402120121 (not readable, not proposed).
- Findings with status assumption (in at least one part): 11 of 55 (GB-03, GB-10, GB-11, GB-18, GB-20, GB-24, GB-26, GB-37, GB-41, GB-42, GB-50); each is put as a question where its central statement depends on the assumption.
- Optional checks run: 0 of 6.
- Omitted instances: none.
- Discarded findings: 1 (instance AB, SAF minimum of ~2 % between 9.5 and 12 kyr BP: the statement agrees with the sample values of Table S1, median 0.3 %, 23 of 33 samples at 2 % or less; the higher values measured on the moving average are carried by single samples and the YD; PP-23).
- Merged: 83 substantive findings of the six instances became 55 (27 merged into others, 1 discarded); 91 minor corrections became 58 (22 merged into substantive findings, 11 merged with other minor corrections), and 6 minor corrections were added during merging (ZF); 54 verification logs became 45, and 2 were added (PP-46, PP-47).
- Values in figures were measured by instance AB (300 and 600 dpi renderings); instance SD did not measure figures. Literature was read by the review instances with WebSearch and WebFetch; the merging step read no web pages. The supplement has no line numbers; its locations are given by page and element.
