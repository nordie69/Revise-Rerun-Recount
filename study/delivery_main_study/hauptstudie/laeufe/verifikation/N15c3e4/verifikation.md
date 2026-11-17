# Verifikation des Gutachtens zu egusphere-2025-4695

Geprüfte Fassung: egusphere-2025-4695.pdf, 37 Seiten, SHA-256 9c80676054f96ecd6f00f4d2a8b5ba568e03c6949e3856d363ac1c4abb42e7bd (mit sha256sum bestätigt). Zeilennummern an den gedruckten Randnummern der Seitenbilder 1 bis 16, 18 und 20 bestätigt; Abbildungen an den Seitenbildern 24 bis 37 und an eigenen 300-dpi-Renderings (vf/r300) geprüft; Rechnungen mit Python (calc.py), Balken- und Farbmessungen mit fig11.py, fig14.py, fig15.py, leg.py, Schriftgrößen mit digit.py.

## 1. Urteil je Kennung

| Kennung | Urteil | Beleg |
|---|---|---|
| GB-01 | echt | Beide Zitate stehen wörtlich auf S. 1, Z. 3 bis 4 und S. 3, Z. 74 bis 75; die Textsuche findet "cost", "time-consuming" und "efficien" nur in Z. 3 bis 4, 35, 40 bis 42, 74 bis 75 und deren Dubletten, in Abschnitt 5 und 6 (S. 15, Z. 450 bis S. 16, Z. 489) nicht. |
| GB-02 | echt | Gl. 8 (S. 6, Z. 186) setzt Cd = σd² I mit einem σd, das in Abb. 10 (S. 31, dritte Zeile) variiert und in Z. 295 und 428 auf 0,01 mm/y gesetzt wird; Replikate fehlen, "with the same inversion parameters" steht S. 15, Z. 444 bis 445. |
| GB-03 | echt | Abstract S. 1, Z. 7 und Schluss S. 16, Z. 482 bis 483 stehen wörtlich, während S. 11, Z. 312, S. 12, Z. 353, S. 13, Z. 387 bis 388 und die Legende von Abb. 8 (S. 29) die nicht konvergierenden Fälle nennen. |
| GB-04 | echt | Überschriften "1 Introduction" (S. 1, Z. 9) und "2 Introduction" (S. 3, Z. 76) am Seitenbild bestätigt; difflib ergibt für Z. 10 bis 75 gegen Z. 77 bis 142 je 1153 Wörter und Ähnlichkeit 1,0. |
| GB-05 | echt | "spatio-temporal dynamics" und "timing of their activation" stehen S. 1, Z. 10 bis 13, die Einzelprobe vom 28.06.2019, 13:30 auf S. 14, Z. 423 bis 424, die Skalierung in Gl. 2 auf S. 5, Z. 160; keine Forschungsfrage behandelt die Zeit (S. 10, Z. 282 bis 285). |
| GB-06 | echt | "E., 2009" steht S. 1, Z. 11 bis 12 und S. 3, Z. 78 bis 79, der Eintrag "E., W. D.: ... oCLC: 1402659188, 2009." mit doppelter Jahreszahl auf S. 18, Z. 567 bis 568; die Zuschreibung an D. E. Walling war online nicht prüfbar (UNESDOC nur Sitzungsprüfung) und ist im Gutachten als gefolgert markiert. |
| GB-07 | echt | Zitat S. 2, Z. 61 bis S. 3, Z. 62 wörtlich; Ehlers et al. (2015), JGR Earth Surface 120(6), 1023 bis 1039, nennt laut Deep Blue 106 AHe- und 100 AFT-Alter aus Schmelzwassersediment, und "Ehlers" kommt im Literaturverzeichnis (S. 17 bis 21) nicht vor. |
| GB-08 | echt | "(Brown, 1985; Kobe, 2021)" steht S. 2, Z. 31 und S. 4, Z. 98, der Eintrag ohne Artikelnummer S. 19, Z. 597 bis 598; der Abstract auf hts.org.za (Artikel 6176) behandelt Ubuntu und Black Theology, ohne Pollen, Sediment oder Fingerprinting. |
| GB-09 | echt | Zitate S. 2, Z. 36 bis 37 und S. 13, Z. 404 wörtlich; Eberl (2004) enthält laut USGS-Seite die zitierte Wendung "at least three sediment sources...", Andrews und Eberl (2012) testen laut USGS-Seite elf künstliche Mischungen aus vier Endgliedern, und beide fehlen im Verzeichnis. |
| GB-10 | echt | S. 2, Z. 48 bis 49 "Non-Linear Least Squares (NLLS) (a constrained linear regression)", Z. 51 "NNLS", Z. 50 "Generalist Likelihood", Z. 51 "Maximal Likelihood", Z. 53 "(BLMM)" und Z. 55 bis 56 "Bayesian linear mixed models" am Seitenbild 2 bestätigt. |
| GB-11 | echt | Neuheitssatz S. 15, Z. 454 bis 455, "weighted average" S. 5, Z. 151 bis 152 und "hence making this non-linear" S. 5, Z. 157 bis 158 wörtlich; der Serval-Abstract von De Doncker et al. (2020) nennt Least-Squares-Inversion mit Prior und Kovarianz und andere Tracer wie "mineral content", der Springer-Abstract von Niu et al. (2020) ein lineares Mischmodell. |
| GB-12 | echt | Gl. 17 (S. 7, Z. 208) nutzt k, Gl. 18 und 19 (S. 8, Z. 215 und 219) nutzen εn und εk zugleich, n ist in Gl. 1 und 4 (S. 5, Z. 154; S. 6, Z. 164) die Pixelzahl, und S. 9, Z. 262 bis 263 sowie Abb. 3d ("tracer mineral n", "detrital sample i") nutzen t und n als Tracerindex. |
| GB-13 | echt | Die Exportschätzung wird S. 3, Z. 65 bis 66, S. 15, Z. 452 bis 454 und S. 16, Z. 479 bis 480 genannt, aber nirgends beziffert ("export" nur in Z. 66, 133, 454, 468, 479); S. 14, Z. 428 nennt für die Naturdaten "a prior equal to the average true erosion rate". |
| GB-14 | echt | Gl. 18 auf S. 8, Z. 215 enthält keine Normierung, obwohl S. 11, Z. 312 sie für die SD-Läufe nennt, und Gl. 19 (Z. 219) invertiert (GnT Cd⁻¹ Gn), während S. 6, Z. 170 bis 172 weniger Tracer als Pixel angibt. |
| GB-15 | echt | Am Seitenbild 6 und 7: Gl. 5 (Z. 175) ohne Relationszeichen, Gl. 9 (Z. 189) exp(s²/L²) ohne Minus, Gl. 12 (Z. 197) G = A·exp(ε), Gl. 14 (Z. 201) G Cd⁻¹ ohne Transponierung gegenüber GT in Gl. 16 (Z. 205); das Zitat steht Z. 190. |
| GB-16 | echt | Gl. 22 (S. 8, Z. 239) ist ein Wurzelverhältnis, S. 14, Z. 436 definiert tr(Cm,post)/tr(Cm); die Benennungen in Z. 303, 335, 436, 441, 446 und in Abb. 5, 7 bis 10 und 14 bis 16 sind wie angegeben, wobei zwei der acht Namen sich nur in der Schreibung s/z unterscheiden; √0,82 = 0,906. |
| GB-17 | echt | Die Auflösungskarten in Abb. 5d (S. 26, Skala 0,90 bis 1,00) und Abb. 14 bis 16 sind fast flächig in der dunkelsten Farbe (≈1), in Abb. 15 (S. 36) heller nur am Erosionsmaximum, wo die normierte Unsicherheit am niedrigsten ist; Zitat S. 8, Z. 235 bis 236 wörtlich; 7/849 = 0,008. |
| GB-18 | echt | Der Speicherhinweis steht erst S. 15, Z. 466 bis 468, die XRD-Einschränkungen S. 15, Z. 469 bis S. 16, Z. 476, während Abschnitt 3.4 (S. 9, Z. 249 bis 265) die Peakflächen ohne diese Vorbehalte als "relative mineral concentrations" (Z. 261 bis 262) einführt. |
| GB-19 | echt | Abschnitt 3.4 (S. 9, Z. 250 bis 262) nennt weder Gerät noch Scanparameter noch 2θ-Fenster, und die Verfügbarkeitsangabe S. 16, Z. 490 nennt nur "data and codes used for the inversion tests" und endet ohne Punkt. |
| GB-20 | echt | Probenzahl, Lage und Aggregation fehlen; S. 14, Z. 413 spricht von "multiple detrital samples", Z. 421 von "the same detrital sample", Z. 437 bis 438 von "a detrital sample taken at the same date and time". |
| GB-21 | echt | S. 9, Z. 251 bis 252 verweist für die Quellproben auf "Figure 3A and 3B", Abb. 3 (S. 24) zeigt in (a) "detrital sampling: pump sampler" und in (b) "in-situ source sampling". |
| GB-22 | echt | S. 9, Z. 270 bis 271 (Lithologie unter Eis abgeleitet) und S. 15, Z. 463 bis 464 (Empfehlung a) stehen wörtlich, Abb. 4 trägt "Inferred geology and outcrops", Abb. 3a zeigt einen "pump sampler", und eine Tiefenintegration der Proben wird nirgends angegeben. |
| GB-23 | echt | S. 10, Z. 274 bis 275 "(Bündnerschiefer)", Z. 299 "Zermatt Saas-Fee", S. 12, Z. 340 "Zermatt-Saas-Fee", S. 14, Z. 431 bis 432 "Zermatt-Saas Fee" und "MR g-g", Legende Abb. 11 "Stockhorn-Turftgrat-Gornergrat" und "ecologites", "S.,T.,G." in Abb. 5, 15, 16 ohne Auflösung, Abb. 14 ohne Lithologielegende. |
| GB-24 | echt | Der Nachweis "Land cover data: SwissTopo 2018 Geological data: ... outcrops by GeoCover" steht nur in Abb. 4 (S. 25); SwissTopo und GeoCover fehlen im Verzeichnis, S. 16, Z. 490 nennt das Quellgebietsraster nicht. |
| KK-01 | echt | S. 1, Z. 5 "(steepest descent and Quasi-Newtonian)" gegenüber "quasi-Newton (QN)" in S. 7, Z. 211 und S. 10, Z. 296. |
| KK-02 | echt | Alle fünf Wendungen stehen wörtlich (S. 2, Z. 61; S. 4, Z. 128; S. 11, Z. 333 bis 334; S. 14, Z. 424 bis 425), "becomes Tarantola (2005):" jedoch in S. 6, Z. 181 statt der angegebenen Z. 180 (dort steht Gl. 6). |
| KK-03 | echt | "Gorner-gletscher catchment" S. 9, Z. 267 und Legende Abb. 11, "Gorner gletscher catchment" S. 15, Z. 463, dagegen "Gornergletscher" S. 9, Z. 272 und S. 10, Z. 282 und "Gorner Glacier" in Z. 392, 400, 498, 499. |
| KK-04 | echt | Abb. 3c (S. 24) trägt "quarz pattern alignment". |
| KK-05 | echt | "biotite schits" steht in den Legenden von Abb. 4 (S. 25) und Abb. 12 (S. 33). |
| KK-06 | echt | "caclcite-zoisite amphibolites" steht in den Legenden von Abb. 4 und Abb. 12. |
| KK-07 | echt | "silimanite-biotite gneiss" steht in den Legenden von Abb. 4 und Abb. 12. |
| KK-08 | echt | "calcarious mica schist" steht in den Legenden von Abb. 4 und Abb. 12. |
| KK-09 | echt | "GornergratPermo-Mesozoic" steht in den Legenden von Abb. 4 und Abb. 12. |
| GB-25 | echt | S. 10, Z. 288 bis 289 und S. 13, Z. 374 bis 375 stehen wörtlich, "noise" kommt nur S. 9, Z. 255 und in Abb. 3 vor, der Prior ist in Z. 295 und 325 bis 326 der wahre Mittelwert; Wirgin (2004) enthält laut arXiv-Abstract den zitierten Satz und fehlt im Verzeichnis; 103/163 = 63,2 %. |
| GB-26 | echt | S. 10, Z. 288 bis 294, S. 11, Z. 327 bis 333 und S. 12, Z. 343 bis 347 und 355 bis 357 nennen keine Erzeugungsregel für Fingerprints, Hotspot, Pixelgitter, geänderte Karte, Mischformel oder Tracerauswahl; das PCA-Zitat steht Z. 355 bis 356. |
| GB-27 | echt | Abb. 5g (S. 26) endet bei 100 Iterationen um 201 mit Minimum um 197 nahe Iteration 20, Abb. 6g (S. 27) endet bei 200 Iterationen um 193, während S. 11, Z. 320 bis 321 QN "more stable and accurate" nennt; 8,0/201,0 = 4,0 %. |
| GB-28 | echt | S. 11, Z. 316 bis 317 steht "visible after 125 iterations ... (Figure 6G versus Figure 6G)", die Legenden von Abb. 5 und 6 ordnen die Kovarianz Feld (h) zu, und Abb. 6h zeigt einen Knick bei etwa 140 Iterationen ohne erkennbare Schwingung. |
| GB-29 | echt | Text "area mismatch" (S. 11, Z. 330, 335), Legende Abb. 7 "area difference (m2)", Achse "Area difference", Farbskala "Geology misalignment (m²)", Titel "Originial geology (same as forward)" und Label "Forward geology"; Abb. 8 "Almost fully blended", "Medium blended", "Unblended" gegenüber S. 12, Z. 348. |
| GB-30 | echt | S. 12, Z. 345 bis 347 definiert den JS-Abstand für Wahrscheinlichkeitsverteilungen, S. 9, Z. 261 normiert auf das Maximum, und eine Umrechnung oder Logarithmusbasis wird nirgends genannt. |
| GB-31 | echt | S. 12, Z. 348 bis 349 nennt 20 Stufen, die Legende von Abb. 8 schließt eine aus, und in den Feldern absoluter Fehler und Unsicherheit von Abb. 8 (S. 29) zähle ich je 14 Marker, vier unter 0,37 und zehn von 0,44 bis 0,62. |
| GB-32 | echt | Die Fehlerachsen in Abb. 5 bis 10 tragen die Größe "sum etrue minus epost" ohne Einheit, Abb. 8 reicht bis etwa 676 000, während S. 12, Z. 352 "700 mm/yr" schreibt; 1200/4 = 300 und 3000/10 = 300. |
| GB-33 | echt | Die Rangfolge steht S. 12, Z. 363 bis 364, die Monotonieaussage S. 11, Z. 337 bis 338; Abb. 7 zeigt Fehler um 197, 193 und 275 und Unsicherheit 0,740, 0,738 und 0,746, Abb. 9 Fehler 197 bis 348 und Unsicherheit 0,74 bis 0,96; 77,5/197,4 = 39,3 %, 150,7/197,2 = 76,4 %. |
| GB-34 | echt | Abb. 10 (S. 31) markiert L = 3000 m, σm = 6.2, σd = 0.003 mm/y, μ = 0.1 und n_m = 25, der Text S. 11, Z. 324 bis 326 nennt 1200 m, 3, 0,01 mm/y, 0,1 und 25 Iterationen. |
| GB-35 | echt | Die erste Zeile von Abb. 10 endet bei 3000 m, der Fehler fällt über 20 Werte monoton von etwa 257 auf etwa 76, während S. 12, Z. 373 bis S. 13, Z. 374 eine Verschlechterung jenseits 3000 m behauptet; 195,0/76,1 = 2,56. |
| GB-36 | echt | Die dritte Zeile von Abb. 10 zeigt mit Versatz +1.974e2 einen monoton steigenden Fehler von 0,020 bis 0,043, Unsicherheit 0,74015 bis 0,74040 und Modellmisfit 1,5614 bis 1,5623, entgegen S. 13, Z. 380 bis 384; "10-2" steht Z. 384. |
| GB-37 | echt | S. 13, Z. 387 bis 388 steht wörtlich, die fünfte Zeile von Abb. 10 zeigt nur beim ersten Lauf (etwa 5 Iterationen, etwa 269) eine Abweichung und ab etwa 15 Iterationen das Plateau um 200; 25/115 = 21,7 %. |
| GB-38 | echt | S. 13, Z. 395 nennt "Chrysolite", Abb. 11, 15 und 16 und S. 10, Z. 274 "chrysotile"; minerals.net führt Chrysolith als Olivinvarietät und Chrysotil als Serpentinmineral. |
| GB-39 | echt | Zitat S. 13, Z. 399 bis 401 mit doppeltem Artikel wörtlich; meine Balkenmessung an Abb. 11 (300 dpi) ergibt identische Längen für Anorthit und Pyroxen sowie Annit und Phlogopit, Ankerit und Dolomit bis 2 px, Muskovit gleich Annit in sechs von sieben Spalten; laut BGS besteht Eklogit zu über 70 % aus Granat und Omphazit. |
| GB-40 | echt | S. 14, Z. 411 und 415 bis 416 stehen wörtlich, eine einzige Einheit ist ausgeschlossen, und in Abb. 13 (S. 34) liegen die KDE-Maxima von Furgg und Monte-Rosa-Granit wie bei den ZSF-Sedimenten bei 0. |
| GB-41 | echt | S. 14, Z. 430 bis 434 nennt die fehlenden Zirkondaten und die kopierte MR-g-g-Signatur, Z. 439 die "greater stability"; meine Messung an Abb. 14 ergibt gleiche Anteile von MR gneiss und MR granite in allen 13 Klassen (Differenz bis 0,004); 3/7 = 42,9 %. |
| GB-42 | echt | S. 14, Z. 433 bis 434 regelt nur MR g-g, nicht die ZSF-Metabasite; in Abb. 14 (S. 35) fehlen Segmente in Gelb und Dunkelgrün in allen 13 Altersklassen, eine Lithologielegende fehlt, die Legenden nennen die Kopie nicht. |
| GB-43 | echt | S. 14, Z. 435 bis 436 und S. 15, Z. 441 bis 449 nennen JS-Werte nur für Zirkon (0,48) und kombiniert (0,57) und keine Misfits, obwohl S. 8, Z. 240 sie verlangt. |
| GB-44 | echt | S. 15, Z. 446 bis 447 nennt 0,86 gegenüber 0,87 (Zirkon), S. 15, Z. 441 bis 442 für XRD allein 0,82; die Aussagen S. 3, Z. 72 bis 73 und S. 15, Z. 461 bis 463 stehen wörtlich; minus 0,01/0,87 = minus 1,1 %, plus 0,04/0,82 = plus 4,9 %. |
| GB-45 | echt | In Abb. 15 (S. 36) und Abb. 16 (S. 37) liegt die Schraffur auf dem zentralen Erosionsmaximum, das S. 14, Z. 440 bis S. 15, Z. 441 als Hauptergebnis nennt; ein Kriterium steht nirgends, die Legende lautet "Low-con dence area". |
| GB-46 | echt | Meine Farbmessung an Abb. 15 (300 dpi) ergibt: Balken S.,T.,G. liegt 15 vom Feld "MR gneiss, mica" und 126 vom eigenen, Balken MR gneiss 41 vom Feld "MR granite" und 95 vom eigenen. |
| GB-47 | echt | In Abb. 6 (S. 27) fehlen in (g), (h) und (i) die x-Achsentitel, in (i) "Data misfit", der Faktor "1e8" und der Farbskalentitel, und das Schraffurfeld unter (b) hat keinen Text, alles in Abb. 5 vorhanden. |
| GB-48 | echt | In Abb. 9 (S. 30) tragen die linken beiden Streudiagramme "Avg. JS distance between lithologies" bei Ticks 0,0 bis 20,0, die Farbskala "Number of tracrs", und unter dem y-Titel steht ein zweites Σ. |
| GB-49 | echt | Meine Messung (300 dpi) ergibt 11 px Ziffernhöhe in Abb. 10, nach dem Verfahren des Gutachtens etwa 3,7 pt, und 16 px an den Farbskalen von Abb. 15, etwa 5,3 pt. |
| GB-50 | echt | Abb. 11 (S. 32) hat weder Werteachse noch Spaltenköpfe; die Spalten sind nur über die Legende benannt. |
| GB-51 | echt | Abb. 12 (S. 33) zeigt das gesamte Einzugsgebiet ohne Teilgebietsgrenze, mit kräftigen Farben nur im Nordosten und blassen Farben sonst, und die Legende erklärt das nicht. |
| GB-52 | echt | Das obere Feld von Abb. 13 (S. 34) trägt "Density" ohne Tickwerte, das untere eine Skala 0 bis 2, und die Furgg-Kurve reicht in das Band darüber. |
| GB-53 | echt | Meine Messung an Abb. 15 ergibt für Quarz Anteile 0,33 (MR gneiss) und 0,04 (S.,T.,G.), aus Abb. 11 bei Normierung je Mineral folgen 0,21 und 0,11; Zitat S. 9, Z. 261 bis 262 wörtlich. |
| GB-54 | echt | In Abb. 16 (S. 37) ist die obere Legendenzeile oben abgeschnitten, und in Abb. 15 und 16 läuft "ZSF serpentinites" in das Feld von "ZSF metabasites". |
| KK-10 | echt | S. 10, Z. 306 bis S. 11, Z. 307 nennt einen "similar trend", obwohl der Fehler in Abb. 5g fällt und die normierte Kovarianz in Abb. 5h steigt. |
| KK-11 | echt | S. 11, Z. 319 steht "(Figure 6D, 6E and 6F )" mit Leerzeichen vor der Klammer. |
| KK-12 | echt | Die x-Achse des mittleren Felds der ersten Zeile von Abb. 10 (S. 31) lautet "Smooting distance (m)". |
| KK-13 | echt | Die Annotation in Abb. 10, fünfte Zeile rechts, lautet "n_m = 25", die Legende schreibt nm mit tiefgestelltem m. |
| KK-14 | echt | Legende Abb. 14 "using Zr fingerprint data", y-Achse "Normalised abundance per Zr age bin", Titel Abb. 16 "combined XRD and Zr data". |
| GB-55 | echt | S. 15, Z. 451 und S. 1, Z. 8 schreiben "validated" und "further validates", die Naturdatenabschnitte S. 13, Z. 400 und S. 14, Z. 417 "supporting" und "supports". |
| GB-56 | echt | S. 15, Z. 458 und 460 bis 461 stehen wörtlich, S. 12, Z. 360 und 364 bis 365 widersprechen der ersten Aussage, Abb. 9 zeigt keine Auflösung, und kein Test variiert die Zahl der Quellgebiete. |
| GB-57 | echt | S. 15, Z. 470 bis 471 stützt die tiefenintegrierte Probenahme auf Butler et al. (2019); der Abstract im SLU-Portal (12 Böden, 5 Bearbeiter, 60 Messungen) nennt weder Schwebstoff noch Sortierung, Abschirmung oder Peaküberlagerung; der Volltext war auch für mich nicht lesbar (PMC mit reCAPTCHA). |
| GB-58 | echt | Abschnitt 6 (S. 16, Z. 477 bis 489) nennt nur synthetische Versuche und keines der drei Naturdatenziele aus S. 10, Z. 282 bis 285, weder die Bayes-Einordnung (S. 2, Z. 55 bis 56) noch die Fehlerfortpflanzung (S. 1, Z. 7). |
| GB-59 | echt | S. 16, Z. 487 bis 489 erweitert ohne Bedingung auf Landnutzung und Zirkonalter, während S. 15, Z. 464 bis 466 die Bedingung nennt und S. 14, Z. 435 die Zirkonlösung "highly unstable" nennt. |
| KK-15 | echt | S. 15, Z. 460 "glaciated catchments" gegenüber "glacierized" in S. 1, Z. 16, S. 3, Z. 62 und S. 11, Z. 329. |
| KK-16 | echt | S. 16, Z. 480 lautet "identify the mineralogical contributions of different source areas". |
| KK-17 | echt | S. 16, Z. 491 "All authors (FDD, FH, BB, TA)", Z. 491 bis 494 "F.H.", "F.D.D.", "B.B.", "T.A.". |
| KK-18 | echt | S. 17, Z. 514 schreibt "Chapter Ten" und S. 19, Z. 610 "Chapter 9", jeweils mit freistehendem Bindestrich vor "Nonlinear Inverse Problems". |
| KK-19 | echt | S. 17, Z. 522 bis 523 "Master’s thesis, University of Lausanne, unpublished master’s thesis, 2021." |
| KK-20 | echt | S. 17, Z. 526 "Reviews in mineralogy, Mineralogical society of America". |
| KK-21 | echt | S. 19, Z. 578 "[No title found]"; der Titel "Landscape indicators of human impacts to riverine systems" ist für Gergel et al. (2002), Aquatic Sciences 64, 118 bis 128, im Portal der University of Illinois bestätigt. |
| KK-22 | echt | S. 20, Z. 612 bis 613 "Oxford University Press, New-York," mit Seitenangabe 378 bis 379 in einem Bucheintrag. |
| KK-23 | echt | S. 20, Z. 635 "ISBN 9780898715729 9780898717921". |
| KK-24 | teilweise echt | Am Seitenbild 20, Z. 639 steht die 137 bereits hochgestellt ("Bomb-fallout¹³⁷ Cs"); die Zitierung "Bomb-fallout137 Cs" gibt die Textschicht wieder, echt ist nur der Leerzeichenfehler, nicht die fehlende Hochstellung. |

## 2. Literaturvorschläge gegen das Literaturverzeichnis

| Vorschlag | Kennung | Bereits im Verzeichnis |
|---|---|---|
| Walling, D. E. (2009), UNESCO-Bericht | GB-06 | ja (als "E., W. D.", S. 18, Z. 567 bis 568) |
| Ehlers et al. (2015) | GB-07 | nein |
| Eberl (2004) | GB-09 | nein |
| Andrews und Eberl (2012) | GB-09 | nein |
| De Doncker et al. (2020) | GB-11 | ja (S. 18, Z. 559 bis 560) |
| SwissTopo (Landbedeckung) | GB-24 | nein |
| GeoCover (Aufschlüsse) | GB-24 | nein |
| Wirgin (2004) | GB-25 | nein |
| Collins et al. (2020) | GB-40 | ja (S. 18, Z. 548 bis 551) |

## 3. Doppelungen

Keine. Geprüfte Kandidaten mit gleichem Fundort, aber verschiedenem Gegenstand: GB-03 und GB-37 (S. 13, Z. 387 bis 388), GB-03 und GB-58 (S. 16, Z. 482 bis 483), GB-41 und GB-42 (S. 14, Z. 430 bis 434), GB-43 und GB-44 (S. 15, Z. 446 bis 449), GB-12 und GB-14 (Gl. 18 und 19), GB-46 und GB-54 (Legenden Abb. 15 und 16), KK-05 bis KK-09 (verschiedene Wörter derselben Legenden), KK-10 und GB-16 (verschiedene Zeilen).

## 4. Fundorte

Gezählt je Kennung nach der ungenauesten Einzelangabe; Zeilen an den Randnummern bestätigt.

| Klasse | Anzahl |
|---|---|
| genau | 82 |
| um 1 bis 2 Zeilen daneben | 1 (KK-02: "becomes Tarantola (2005):" in Z. 181 statt Z. 180) |
| weiter daneben | 0 |

## 5. Zählungen je Urteil

| Urteil | Anzahl |
|---|---|
| echt | 82 |
| teilweise echt | 1 |
| falsch | 0 |
| nicht prüfbar | 0 |
| Summe | 83 (59 GB, 24 KK) |

Literaturvorschläge: 9, davon ja 3, nein 6. Doppelungen: 0.
