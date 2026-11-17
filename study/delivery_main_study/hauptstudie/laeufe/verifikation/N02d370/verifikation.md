# Verifikation des Gutachtens zu egusphere-2025-4695

Grundlage: Manuskript-PDF (37 Seiten), Seitenbilder `seiten/` (150 dpi), eigene Renderings der Abbildungsseiten 25 bis 37 mit 300 dpi (`vf/hr/`), `text.json` als Suchbasis. Alle Zeilennummern wurden an den gedruckten Randnummern der Seitenbilder 1 bis 21 bestätigt. Zahlen wurden mit Python nachgerechnet, Abbildungswerte an Fig. 5g, 6g, 6h, 7, 8, 9, 10, 11, 4 und 15 gemessen oder am Bild abgelesen. Literatur über WebFetch und WebSearch, soweit erreichbar (OpenAlex war nicht freigegeben).

## 1. Urteil je Kennung

| Kennung | Urteil | Beleg (ein Satz mit Seite und Zeile) |
|---|---|---|
| GB-01 | echt | "spatio-temporal" und "timing of their activation" stehen S. 1, Z. 1 und Z. 10 bis 13, die Suche nach "temporal" ergibt genau 3 Treffer (S. 1, Z. 1 und 10; S. 3, Z. 77), der Vergleich nutzt eine Probe vom 28.06.2019 (S. 14, Z. 423 bis 424). |
| GB-02 | echt | "validate a time- and cost-effective" steht S. 1, Z. 3 bis 4, "cost" hat 6 und "efficien" 4 Treffer nur in S. 1 bis 5 (Z. 3 bis 142), ab Z. 143 keiner, keine Kosten- oder Zeitangabe. |
| GB-03 | echt | "consistent convergence" steht S. 1, Z. 7, dagegen "proved unstable" S. 11, Z. 312, "fails to converge" S. 12, Z. 353 und der Ausschluss im Caption von Fig. 8 (S. 29). |
| GB-04 | echt | Abschnitt 1 (S. 1, Z. 9 bis S. 3, Z. 75) und Abschnitt 2 (S. 3, Z. 76 bis S. 5, Z. 142) sind je 1153 Wörter lang, difflib-Ähnlichkeit 1.0, je 67 Zeilen. |
| GB-05 | echt | Kurzbeleg "E., 2009" S. 1, Z. 11 bis 12 und S. 3, Z. 78 bis 79, Eintrag "E., W. D.: ... oCLC: 1402659188, 2009" S. 18, Z. 567 bis 568 zwischen Domingo (Z. 564) und Evrard (Z. 569); die Autorschaft Walling bleibt wie im Gutachten nur erschlossen (UNESCO-Archiv nicht lesbar). |
| GB-06 | echt | Satz S. 1, Z. 18 bis 19 und S. 3, Z. 85 bis 86; das Abstract von Barker et al. (1997, S. 17, Z. 519 bis 520) behandelt photogrammetrische Ufererosion ohne Sedimentfallen, Dämme oder Herkunft, Wilson et al. (S. 21, Z. 649) ist laut Titel eine Bodenerosionsbewertung. |
| GB-07 | echt | Kobe (2021, S. 19, Z. 597) ist laut Verlagsseite ein Theologieartikel ohne Pollen oder Sediment, Walden et al. (S. 20, Z. 641) und Vanden Bygaart und Protz (S. 20, Z. 639) tragen die genannten Titel, Blaen et al. (S. 17, Z. 528 bis 530) behandeln laut Abstract Sensorik zur Wasserqualität. |
| GB-08 | echt | Die Lückenbehauptung steht S. 2, Z. 36 bis 37 und S. 4, Z. 103 bis 104, "literature", "search" usw. haben 0 Treffer, Eberl (2004) und Andrews und Eberl (2012) entmischen XRD-Mineralogie laut USGS-Seiten; die XRD-Angabe zu Klages und Hsieh (1975) war nicht lesbar. |
| GB-09 | echt | Eberl, Andrews, Ehlers, Enkelmann haben 0 Treffer in S. 17 bis 21, die bibliographischen Angaben und Inhalte von Eberl (2004), Andrews und Eberl (2012) und Ehlers et al. (2015, JGR 120, 1023 bis 1039) bestätigt; Positionierung S. 2, Z. 36 bis 42 und S. 2, Z. 58 bis S. 3, Z. 63. |
| GB-10 | echt | "hybrid between Bayesian linear mixed models and hierarchical Bayesian models" S. 2, Z. 55 bis 56 gegen "Bayesian Linear Mixing Models (BLMM)" Z. 53, "hierarch" 4 Treffer nur in S. 2 und 4. |
| GB-11 | echt | "transported or stored" S. 5, Z. 147 bis 148 gegen Speicherwarnung S. 15, Z. 466 bis 468, Gradientennormierung nur S. 11, Z. 312 bis 313, Zirkonlücken nur S. 14, Z. 430 bis 434. |
| GB-12 | echt | Gl. 19 auf S. 8, Z. 219 enthält (GnT Cd^-1 Gn)^-1 ohne Cm^-1, Gl. 20 in Z. 225 mit Cm^-1, Unterbestimmtheit S. 6, Z. 170 bis 172. |
| GB-13 | echt | "We assume weak nonlinearity" S. 6, Z. 177 bis 178, σm = 3 S. 10, Z. 294, ">8000 mm/y" S. 14, Z. 435; exp(±3) = 0.050 und 20.1, exp(6) = 403 nachgerechnet. |
| GB-14 | echt | Cd = σd² I in Gl. 8 (S. 6, Z. 186), σd = 0.01 mm/y für die natürlichen Läufe S. 14, Z. 427 bis 428, keine Quellfingerabdruck-Kovarianz im Text. |
| GB-15 | echt | Gl. 22 (S. 8, Z. 239) ist ein elementweises Wurzelverhältnis, S. 14, Z. 436 nutzt tr(Cm,post)/tr(Cm), die Namen der Größe wechseln (S. 10, Z. 303 und 306; Fig. 5h, 7 bis 10, 14 bis 16), Fig. 5d und 14 zeigen fast alle Pixel am Wert 1.0. |
| GB-16 | echt | "diffractometer", "Cu K", "kV", "scan", "software" 0 Treffer in S. 1 bis 16, "WinXRD" nur S. 9, Z. 254 und S. 15, Z. 473 ohne Version. |
| GB-17 | echt | Die Schritte S. 9, Z. 257 bis 260 nennen keine 2θ-Fenster, "blend" 3 Treffer (S. 12, Z. 343 und 348) ohne Formel, PCA nur S. 12, Z. 355 bis 356 ohne Auswahlregel. |
| GB-18 | echt | Normierung auf das Maximum je Probe S. 9, Z. 261 bis 262 und gewichteter Mittelwert S. 5, Z. 151 bis 152; in Fig. 11 (S. 32) liegt das Maximum je Einheit bei verschiedenen Mineralen (Antigorit, Quarz, Anorthit und Pyroxen). |
| GB-19 | echt | Inferierte Lithologie S. 9, Z. 270 bis 271, Quellen nur im Rasterblock von Fig. 4 (S. 25), "SwissTopo", "GeoCover", "personal comm" 0 Treffer auf allen 37 Seiten, Fig. 7 zeigt drei Karten. |
| GB-20 | echt | Fünf Schreibweisen von Zermatt-Saas Fee (S. 10, Z. 299; S. 12, Z. 340; S. 14, Z. 411 und 414; S. 9, Z. 273; Fig. 12 Caption), "ZSF" erst S. 14, Z. 431 eingeführt, "Turftgrat" und "ecologites" im Caption von Fig. 11 (S. 32). |
| GB-21 | echt | Fig. 1b, 2b, 3b zeigen einen unbeschrifteten schwarzen Pfeil, Fig. 1d dunkelgraue Zylindersegmente, Fig. 2c nur eine grüne Skala "low high" (S. 22 bis 24). |
| GB-22 | echt | Caption "Figure 4. Study area: location, land cover and geology." (S. 25), "ELA" nur in der Inset-Legende, "ELA" und "equilibrium" 0 Treffer im Text, Inset ohne Maßstab. |
| GB-23 | echt | Legendenfelder in Fig. 4 bei 300 dpi gemessen: Stockhorn (255,115,51), MR-Gneis-Aufschlüsse (255,89,51), Stockhorn-Aufschlüsse (253,51,51), Summen 26 und 40, im Rahmen der Gutachtenwerte 24 und 40. |
| GB-24 | echt | Synthetische Daten mit demselben Vorwärtsmodell S. 10, Z. 288 bis 289, Prior gleich wahrer Mittelwert Z. 295, "noise" 1 Treffer (S. 9, Z. 255), Wirgin (2004) definiert das inverse crime so laut arXiv-Abstract. |
| GB-25 | echt | "closely matches ... both in spatial distribution and magnitude" S. 10, Z. 296 bis 297, Fig. 5c (S. 26) zeigt am Hotspot den dunkelblauen Rand der Skala bei etwa minus 2, Fig. 5b endet bei 3.0. |
| GB-26 | echt | Gemessen an Fig. 5g und 6g (300 dpi): QN 197.3 bei Iteration 22 und 201.0 bei 100, SD 211.3 bei 100 und 193.0 bei 200, also SD am Ende 4.0 % niedriger; "more stable and accurate" S. 11, Z. 320 bis 321. |
| GB-27 | echt | "(Figure 6G versus Figure 6G)" S. 11, Z. 317; der Knick in Fig. 6h liegt nach Messung bei etwa Iteration 136 bis 138, danach ein glattes Band. |
| GB-28 | echt | "area mismatch" S. 11, Z. 330 gegen "Area difference" und "Geology misalignment (m2)" in Fig. 7 (S. 28), Fig. 9 (S. 30) trägt "Avg. JS distance between lithologies" bei Markern 1 bis 21, "tracrs", "Originial" und ein zweites "Σ" sind sichtbar. |
| GB-29 | echt | Achsen "Σ∣etrue - epost∣" ohne Einheit in Fig. 5 bis 9, "pixel" 14 Treffer ohne Anzahl in S. 1 bis 16, "mm/yr" S. 12, Z. 352. |
| GB-30 | echt | Satz S. 11, Z. 337 bis S. 12, Z. 340; Fig. 7 zeigt Fehler etwa 197, 193.5, 275 und Unsicherheit 0.7402, 0.7376, 0.7460, also kein monotoner Verlauf. |
| GB-31 | echt | "20 values ... are tested" S. 12, Z. 348 bis 349, in Fig. 8 (S. 29) je 14 Marker gezählt, 20 minus 14 minus 1 = 5 nicht erklärt. |
| GB-32 | echt | "errors exceeding 700 mm/yr for JS < 0.44" S. 12, Z. 352 bis 353, die y-Achse von Fig. 8 reicht ohne Einheit bis 700000, Werte über 700 treten auch bei JS 0.50 bis 0.54 auf. |
| GB-33 | echt | Rangfolge S. 12, Z. 363 bis 365; nachgerechnet: Szenario 1 plus 39.2 % Fehler und plus 0.006 Unsicherheit, Szenario 3 plus 76.6 % und plus 0.222 (Fig. 7 und 9). |
| GB-34 | echt | Übermäßige Glättung "beyond approximately 10 times the pixel size (3000 m)" S. 12, Z. 373 bis S. 13, Z. 374, Fig. 10 Zeile 1 endet bei 3000 m mit fallendem Fehler (etwa 256 bis 76), bei 1200 m etwa 195 bis 198. |
| GB-35 | echt | Text S. 13, Z. 380 bis 384 beschreibt große Unterschiede bei kleinem σd, Fig. 10 Zeile 3 zeigt mit Offset "+1.974e2" monoton 197.420 bis 197.443 (0.012 %), "10-2" ohne Hochstellung Z. 384. |
| GB-36 | echt | "below 25" und "Beyond 115 iterations" S. 13, Z. 387 bis 388, Fig. 10 Zeile 5 zeigt nur bei 5 Iterationen eine Abweichung (etwa 269), feste 25 Iterationen S. 11, Z. 324 und S. 14, Z. 426. |
| GB-37 | echt | Bei 300 dpi gemessen sind Anorthit und Pyroxen (35, 243, 93, 244, 6, 104 px) sowie Annit und Phlogopit (131, 74, 138, 52, 160, 132 px) in Fig. 11 identisch; Liste S. 13, Z. 394 bis 395. |
| GB-38 | echt | "Chrysolite" S. 13, Z. 395 gegen "Chrysotile" in Fig. 11, 15, 16 und S. 10, Z. 274; Chrysolith ist laut minerals.net eine Olivinvarietät. |
| GB-39 | echt | Qualitative Aussage "align well" S. 13, Z. 399 bis 401, "replicat" 0 Treffer, Probenzahl je Einheit nicht genannt (S. 9, Z. 251). |
| GB-40 | echt | "multiple detrital samples" ohne Zahl S. 14, Z. 413, keine Parameter in 4.2.1, Fig. 13 (S. 34) mit Dichteskala nur im unteren Teil, Furgg-Kurve ebenfalls mit Maximum nahe 0, x-Achse endet bei etwa 3.3. |
| GB-41 | echt | "the same detrital sample" S. 14, Z. 420 bis 421 gegen "a detrital sample taken at the same date and time" Z. 437 bis 438. |
| GB-42 | echt | 13 Altersklassen (Fig. 14), 34 Balken (Fig. 16) und 7 Einheiten stehen nicht im Text, die Wortsuche nach "13" als Zahl ergibt nur Gleichungs-, Abbildungs- und Uhrzeitbezüge (S. 7, Z. 199 und 200; S. 14, Z. 414 und 424). |
| GB-43 | echt | "a prior equal to the average true erosion rate" auch für die natürlichen Läufe S. 14, Z. 428, "export" 5 Treffer ohne Wert (S. 3, Z. 66; S. 5, Z. 133; S. 15, Z. 454 und 468; S. 16, Z. 479). |
| GB-44 | echt | Zirkonlücken S. 14, Z. 430 bis 434, Instabilität ">8000 mm/y" Z. 435 im Serpentinitbereich (Fig. 14), Vergleich mit einer einzigen Probe Z. 423 bis 424. |
| GB-45 | echt | Zahlen nur für 0.87, 0.82, 0.86 (S. 14, Z. 436; S. 15, Z. 442 und 447) und JS 0.48 und 0.57 (S. 15, Z. 448), "greater stability" S. 14, Z. 439 ohne Maß. |
| GB-46 | echt | "further stabilize and improve" S. 15, Z. 461 bis 462, kombiniert 0.86 liegt über XRD 0.82 (plus 0.04, plus 4.9 %), gegenüber Zirkon nur minus 0.01; "stabil" 10 und "sharp" 5 Treffer ohne Definition. |
| GB-47 | echt | JS 0.48 auf 0.57 S. 15, Z. 447 bis 448 ohne Basis, Paarbasis nur für synthetische Tests S. 12, Z. 346 bis 347 (21 Paare), kopierter MR-g-g-Fingerabdruck S. 14, Z. 433 bis 434. |
| GB-48 | echt | "Low-confidence areas" in Fig. 5, unbeschriftetes Schraffurfeld in Fig. 6, "Low-con dence area" in Fig. 14 bis 16, "confiden" und "hatch" 0 Treffer auf allen Seiten. |
| GB-49 | echt | In Fig. 6g bis 6i (S. 27) fehlen "Iteration", "Data misfit", der Faktor 1e8 und die Farbbalkenbeschriftung, die in Fig. 5 (S. 26) vorhanden sind. |
| GB-50 | echt | Fig. 10 markiert "L = 3000 m", "σm = 6.2", "σd = 0.003 mm/y" gegen L = 1200 m, σm = 3, σd = 0.01 mm/y in S. 11, Z. 324 bis 326. |
| GB-51 | echt | Ziffernhöhen der Achsbeschriftung in Fig. 10 bei 300 dpi gemessen etwa 11 px, also unter 3 pt, deutlich unter 6 pt; "Smooting distance (m)" sichtbar (S. 31). |
| GB-52 | echt | Fig. 11 (S. 32) hat keine Werteachse und keine Spaltenbeschriftung, längste Balken je Spalte 241 bis 244 px bei 300 dpi. |
| GB-53 | echt | Quarz in Fig. 11: 243, 128, 244, 62, 243, 244 px (Anteile 0.209 bis 0.053), in Fig. 15 gemessen 0.174, 0.042, 0.230, 0.015, 0.325, 0.214, also nicht proportional. |
| GB-54 | echt | Fig. 12 (S. 33) zeichnet keine Teilgebietsgrenze, die gestrichelte Grenze steht nur im Inset von Fig. 13 (S. 34); Aussage S. 14, Z. 411. |
| GB-55 | echt | Fig. 14 (S. 35) hat keine Einheitenlegende, "Ma" nur am letzten Balken, MR-Granit und MR-Gneis gleich hoch je Altersklasse; Textbezug S. 14, Z. 430. |
| GB-56 | teilweise echt | Echt ist, dass die S.,T.,G.-Balken (255,132,77) der Legende "MR gneiss, mica" (255,127,65) gleichen (Summe 17) und kein Balken seiner Legende gleicht; nicht echt ist die Summe 40 für MR-Gneis-Balken gegen MR-Granit-Legende, ungerundet gemessen 47, also nur nächstliegend (Fig. 15, S. 36). |
| GB-57 | echt | In Fig. 15 und 16 überdeckt das Feld "ZSF metabasites" das Ende von "ZSF serpentinites", in Fig. 16 (S. 37) ist die erste Legendenzeile oben abgeschnitten. |
| GB-58 | echt | "explained and validated" S. 15, Z. 451, "confirms" S. 14, Z. 415, "reliably recovered" S. 16, Z. 482 bei einem Test für eine Einheit (S. 14, Z. 411) und Daten aus demselben Vorwärtsmodell (S. 10, Z. 288 bis 290). |
| GB-59 | echt | Neuheitssatz S. 15, Z. 454 bis 455 gegen "non-linear adaptation of the inversion framework validated in (De Doncker et al., 2020)" S. 2, Z. 60 bis 61 und lineare Mischung S. 5, Z. 151 bis 152. |
| GB-60 | echt | "further improves model stability and resolution" S. 15, Z. 458 gegen "7 tracers ... approximately the same" S. 12, Z. 360 und Fig. 9 ohne Auflösung. |
| GB-61 | echt | "A higher number of distinct source areas" S. 15, Z. 460 bis 461, "number of" in S. 10, Z. 286 bis S. 15, Z. 449 nur 4 Treffer zu Tracern und Iterationen. |
| GB-62 | echt | "particularly valuable in glacierized catchments" S. 2, Z. 61 bis S. 3, Z. 62 gegen Empfehlung S. 15, Z. 463 bis 468 und S. 16, Z. 484 bis 486, "storage" und "stored" 7 Treffer ohne Bezug zum Gornergletscher; die Fläche 11.3 km² weicht leicht von 1.15e7 m² in Fig. 7 ab, ohne die Aussage zu ändern. |
| GB-63 | echt | "depth-integrat" 1 Treffer (S. 15, Z. 470), "pump" 0 Treffer im Text, Fig. 1c und 3a beschriften "pump sampler" (S. 22 und 24). |
| GB-64 | echt | In S. 16, Z. 477 bis 489 nur "sub-catchments" (Z. 488) und "zircon" (Z. 489), keine Naturdatenergebnisse, "steepest", "quasi", "QN", "SD", "Newton" 0 Treffer in S. 15 bis 16. |
| GB-65 | echt | Vorschlag S. 16, Z. 487 bis 489 gegen "highly unstable ... (>8000 mm/y)" S. 14, Z. 435, "land use" nur 2 Treffer (S. 15, Z. 466; S. 16, Z. 488). |
| GB-66 | echt | "The data and codes used for the inversion tests" S. 16, Z. 490, Zirkonmethode nur in unveröffentlichter Arbeit S. 17, Z. 522 bis 523, kein Anhang. |
| KK-01 | echt | "(steepest descent and Quasi-Newtonian)" S. 1, Z. 5, "quasi-Newton" S. 7, Z. 211 und S. 10, Z. 296. |
| KK-02 | echt | "Non-Linear Least Squares (NLLS) (a constrained linear regression)", "Generalist", "Maximal", "similar to the NNLS" in S. 2, Z. 48 bis 51 und S. 4, Z. 115 bis 118. |
| KK-03 | echt | Klammerzitate als Erzählzitate an S. 2, Z. 61; S. 4, Z. 128; S. 11, Z. 333 bis 334; S. 14, Z. 424 und 424 bis 425. |
| KK-04 | echt | "hyper-parameters" S. 3, Z. 70 und S. 5, Z. 137, "hyperparameters" S. 10, Z. 281 und "hyperparameter" S. 12, Z. 370. |
| KK-05 | echt | Großbuchstaben "(Figure 1B)" S. 5, Z. 146, "(Figure 5K)" S. 10, Z. 294, "(Figure 6D, 6E and 6F )" mit Leerzeichen S. 11, Z. 319. |
| KK-06 | echt | Gl. 5 auf S. 6, Z. 175 ohne Relationszeichen, "p (ε∣dobs )" Z. 176 und "(ε − εprior )" Z. 184. |
| KK-07 | echt | "becomes Tarantola (2005):" S. 6, Z. 181. |
| KK-08 | echt | Gl. 9 auf S. 7, Z. 189 lautet σm² exp(si,j²/L²) ohne Minuszeichen. |
| KK-09 | echt | Gl. 14 auf S. 7, Z. 201 lautet GC_d^-1(dε − dobs) ohne Transposition, Gl. 16 Z. 205 mit G^T. |
| KK-10 | echt | Gl. 18 (S. 8, Z. 215) und Gl. 19 (Z. 219) enthalten (εk − εprior) bei Index n. |
| KK-11 | echt | "considerately" S. 8, Z. 236. |
| KK-12 | echt | "weighed by the model covariance" S. 9, Z. 245. |
| KK-13 | echt | "(Figure 3A and 3B)" für Quellproben S. 9, Z. 251 bis 252, Fig. 3a zeigt "detrital sampling: pump sampler" (S. 24). |
| KK-14 | echt | Fünf Formen an 12 Stellen: S. 9, Z. 267 und 272; S. 10, Z. 282; S. 13, Z. 392 und 400; S. 15, Z. 463; S. 16, Z. 498 und 499; Fig. 5j, 11, 15, 16. |
| KK-15 | echt | "quarz pattern alignment" in der Legende von Fig. 3c (S. 24). |
| KK-16 | echt | "caclcite", "schits", "silimanite", "GornergratPermo-Mesozoic", "calcarious" in den Legenden von Fig. 4 und 12 (S. 25 und 33). |
| KK-17 | echt | "(such as Zermatt Saas-Fee sediments and Furgg series (Figure 4) and Figure 5J)" S. 10, Z. 299. |
| KK-18 | echt | "measures the similarity" S. 12, Z. 345, Folgesatz Z. 346 "closer to zero indicate more similar". |
| KK-19 | echt | "The more resemblant" S. 12, Z. 351. |
| KK-20 | echt | "the maximal amount of non-linear iterations" S. 12, Z. 370. |
| KK-21 | echt | "supporting the 1) the robustness" S. 13, Z. 400. |
| KK-22 | echt | "sub-catchment" S. 14, Z. 409 und 411 neben "subcatchment" Z. 411, "Gorner-Grenzgletscher conflu-ence" S. 13, Z. 406 bis S. 14, Z. 407, im Caption von Fig. 13 "Gorner" und "Grenz" mit Halbgeviertstrich statt Bindestrich verbunden. |
| KK-23 | echt | "Smooting distance (m)" in Zeile 1 und "n_m = 25" in Zeile 5 von Fig. 10 (S. 31). |
| KK-24 | echt | "using Zr fingerprint data" und "Normalised abundance per Zr age bin" in Fig. 14 (S. 35), "combined XRD and Zr data" in Fig. 16 (S. 37). |
| KK-25 | echt | "All authors (FDD, FH, BB, TA)" S. 16, Z. 491 neben "F.H.", "F.D.D." Z. 491 bis 494. |
| KK-26 | echt | "Bearth, P.: Blatt 535 Zermatt - Geologischer Atlas der Schweiz 1:25 000, 1953." S. 17, Z. 521 ohne Verlag. |
| KK-27 | echt | "Master’s thesis, University of Lausanne, unpublished master’s thesis, 2021." S. 17, Z. 522 bis 523. |
| KK-28 | echt | "[No title found]" S. 19, Z. 578, Titel "Landscape indicators of human impacts to riverine systems" auf experts.illinois.edu bestätigt. |
| KK-29 | echt | Gjems-Eintrag S. 19, Z. 583 ohne Reihe, Verlag und Ort. |
| KK-30 | echt | Lafuente-Eintrag S. 19, Z. 599 bis 600 ohne Herausgeber und Verlag, "Yang, Y." und "Downs, R." |
| KK-31 | echt | "Oxford University Press, New-York," mit Seitenangabe 378 bis 379 im Bucheintrag, S. 20, Z. 612 bis 613. |
| KK-32 | echt | "ISBN 9780898715729 9780898717921" S. 20, Z. 635. |

## 2. Literaturvorschläge: bereits im Literaturverzeichnis?

| Vorschlag (Kennung) | Im Verzeichnis |
|---|---|
| Klages und Hsieh (1975) (GB-07, GB-08) | ja (S. 19, Z. 595 bis 596) |
| Eberl (2004) (GB-08, GB-09) | nein |
| Andrews und Eberl (2012) (GB-08, GB-09) | nein |
| Ehlers et al. (2015) (GB-09) | nein |
| Wirgin (2004) (GB-24) | nein |
| Tarantola (2005) (GB-10) | ja (S. 20, Z. 634 bis 635) |
| De Doncker et al. (2020) (GB-59) | ja (S. 18, Z. 559 bis 560) |
| Beven und Binley (1992) (KK-02) | nein |
| SwissTopo 2018 (GB-19) | nein |
| GeoCover (GB-19) | nein |
| Walling (2009), UNESCO-Bericht (GB-05) | ja, als fehlerhafter Eintrag "E., W. D." (S. 18, Z. 567 bis 568) |

## 3. Doppelungen

Keine. Geprüft wurden alle Paare mit gemeinsamem Fundort, darunter KK-05 und KK-17 (S. 10, Z. 299: Großschreibung gegen Verweisform), GB-51 und KK-23 (Fig. 10: Schriftgröße gegen Schreibfehler), GB-08 und GB-09 (Lückenbehauptung gegen fehlende Literatur), GB-12 und KK-10 (Gl. 19: Inverse gegen Index), GB-40 und GB-58 (S. 14, Z. 415: Testbericht gegen Verbstärke), GB-11 und GB-63 (S. 15, Z. 469 bis 476: Platzierung gegen Anwendung der Gegenmaßnahmen). Jedes Paar behandelt am selben Ort einen anderen Gegenstand.

## 4. Fundorte

| Klasse | Anzahl |
|---|---|
| genau | 98 |
| 1 bis 2 Zeilen daneben | 0 |
| weiter daneben | 0 |

Hinweis: `text.json` weicht vom Seitenbild ab an S. 3 (Z. 91 bis 94 um eine Zeile zu niedrig), S. 6 (Z. 181), S. 11 (Z. 337 bis 339 um eine Zeile zu niedrig) und S. 12 (Z. 373 auf S. 13 gesetzt); das Gutachten folgt durchgehend den gedruckten Randnummern.

## 5. Zählungen

| Urteil | Anzahl |
|---|---|
| echt | 97 (65 GB, 32 KK) |
| teilweise echt | 1 (GB-56) |
| falsch | 0 |
| nicht prüfbar | 0 |
| Literaturvorschläge im Verzeichnis: ja | 4 |
| Literaturvorschläge im Verzeichnis: nein | 7 |
| Doppelungen | 0 |
| Fundorte genau | 98 |
| Fundorte 1 bis 2 Zeilen daneben | 0 |
| Fundorte weiter daneben | 0 |
