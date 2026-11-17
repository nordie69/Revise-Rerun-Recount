# Verifikation des Gutachtens zu egusphere-2025-4695

Grundlage: Manuskript-PDF, Seitenbilder seiten/ (150 dpi), eigene Renderings der Abbildungsseiten mit 300 dpi (vf/r300/), text.json nur als Suchhilfe; Zeilennummern an den gedruckten Randnummern bestätigt. Rechnungen in vf/chk1.py, vf/chk2.py, vf/fig11.py, vf/markers.py.

## Urteile je Kennung

| Kennung | Urteil | Beleg (ein Satz mit Seite und Zeile) |
|---|---|---|
| GB-01 | echt | "validate a time- and cost-effective" steht S. 1, Z. 3 bis 4, "show and validate ... cost- and time-efficient" S. 3, Z. 74 bis 75; "cost" kommt nur in Z. 3, 4, 40, 74, 107, 141 vor, Abschnitte 3 bis 6 messen keine Zeit oder Kosten. |
| GB-02 | echt | Zitate S. 1, Z. 7 bis 8, S. 11, Z. 312, S. 12, Z. 352 bis 353, S. 13, Z. 385 bis 387 und S. 16, Z. 482 bis 483 wörtlich vorhanden; Abb. 10 Zeile 1 fällt von etwa 257 auf 76, Faktor 3,38. |
| GB-03 | echt | Abschnitt 1 (S. 1, Z. 10 bis 75) und Abschnitt 2 (S. 3, Z. 77 bis 142) haben je 66 Zeilen und 1153 Wörter, difflib-Verhältnis 1,0. |
| GB-04 | echt | Zitat "E., 2009" S. 1, Z. 11 bis 12 und Eintrag "E., W. D. ... oCLC:" S. 18, Z. 567 bis 568 am Seitenbild bestätigt; Zuschreibung an Walling bleibt wie im Gutachten erschlossen. |
| GB-05 | echt | S. 1, Z. 18 bis 19 zitiert Barker et al. (1997), dessen Abstract (Portsmouth-Portal) nur Photogrammetrie der Ufererosion behandelt, ohne Sedimentfallen, Dämme oder Fracht. |
| GB-06 | echt | Titel Kobe S. 19, Z. 597 bis 598, Walden S. 20, Z. 641, Olley S. 20, Z. 621 bis 622, Blaen S. 17, Z. 528 bis 530 wie angegeben; Blaen-Abstract (Birmingham-Portal) ohne Quellenzuordnung. |
| GB-07 | echt | Satz S. 2, Z. 36 bis 37 vorhanden, "search" kommt nicht vor, "database" nur S. 9, Z. 257; Andrews und Eberl (2012) testen laut USGS-Seite elf künstliche Mischungen aus vier Endgliedern mit qXRD. |
| GB-08 | echt | Die drei Arbeiten existieren mit den genannten Angaben (USGS, VU-Portal, UEA) und fehlen im Verzeichnis S. 17 bis 21; der zitierte Satz steht allerdings S. 2, Z. 40 bis 41, nicht Z. 42 bis 44. |
| GB-09 | echt | Abstract Niu et al. (2020) ohne Bayesian, frequentist, prior, posterior, mit Gaussian first-order approximation; Abstract Haddadchi et al. (2013) nennt sieben Modelle und lokale gegen globale Optimierung, nicht NLLS, GLUE, MLE (zu S. 2, Z. 45 bis 52). |
| GB-10 | echt | S. 2, Z. 48 bis 49 "(NLLS) (a constrained linear regression)", Z. 51 "similar to the NNLS approach"; NNLS sonst nirgends definiert, Standardname "Generalized Likelihood Uncertainty Estimation" bestätigt. |
| GB-11 | echt | S. 5, Z. 147 bis 148 nennt Speicherung ohne Modellannahme, die Annahme sofortigen Exports erst S. 15, Z. 466 bis 468, Korngrößeneffekte erst Z. 469 bis 470; Abschnitt 3.4 erwähnt beides nicht. |
| GB-12 | echt | Index k in Gl. (17) und S. 7, Z. 209, n in Gl. (18), (19) und S. 8, Z. 216 mit εk im Priorterm; t und xy in S. 9, Z. 262 bis 263; p(ε∣dobs) S. 6, Z. 176; Cm,post S. 14, Z. 436. |
| GB-13 | echt | "prior misfit" S. 6, Z. 184, "model misfit" in 13 Textzeilen (ab S. 7, Z. 202) und auf den Achsen der Abb. 5 bis 10, "prior variance" S. 7, Z. 190. |
| GB-14 | echt | Gl. (9) S. 7, Z. 189 ohne Minuszeichen am Seitenbild; Python: kleinster Eigenwert der gedruckten Form minus 6,1e23, mit Minuszeichen 6,8e-13. |
| GB-15 | echt | Gl. (12) S. 7, Z. 197 als A·exp(ε), Gl. (14) Z. 201 ohne Transponierte, Gl. (19) S. 8, Z. 219 invertiert GᵀCd⁻¹G, Rang 21 bei 500 und 900 Pixeln (Python); Gl. (18) ohne Normierung. |
| GB-16 | echt | Gl. (22) S. 8, Z. 239 als Wurzelverhältnis, S. 14, Z. 436 als Spurverhältnis; Namen in Z. 303, 335, 441, 446, Abb. 5(h) "Normalised covariance trace", Achsen "Trace(post. cov.)" mit Werten 0,3 bis 1,0. |
| GB-17 | echt | Stoppregel S. 9, Z. 243 bis 244, 115 Iterationen S. 13, Z. 388 bis 389; Abb. 10 Zeile 5 zeigt 268,7 bei n = 5, etwa 201 bei n = 15 und das Minimum bei n = 25. |
| GB-18 | echt | S. 9, Z. 251 bis 265 und S. 13, Z. 393 bis 398 nennen weder Gerät, Scanparameter, Fenster noch Probenzahlen; Calcit fehlt in der Liste, obwohl S. 10, Z. 275 und 278 kalkhaltige Gesteine nennen. |
| GB-19 | echt | Messung an Abb. 11 (S. 32): Annite und Phlogopite sowie Anorthite und Pyroxene in allen sieben Spalten gleich, Muscovite weicht von Annite in einer Spalte ab (zu S. 9, Z. 259 bis 260). |
| GB-20 | echt | Normierung auf das Maximum S. 9, Z. 261 bis 262; Python ergibt 0,208, 0,167, 0,625; Abb. 15 zeigt für Antigorit einen Serpentinitanteil von etwa 0,65 gegen 0,43 aus Abb. 11. |
| GB-21 | echt | S. 9, Z. 270 bis 271 vorhanden; Abb. 7 (S. 28) zeigt etwa 197,5 für die Vorwärtsgeologie und etwa 275 für Steck et al. (2015). |
| GB-22 | echt | Die Namensvarianten stehen S. 10, Z. 274 bis 276 und Z. 299, S. 12, Z. 340, S. 14, Z. 411, 414 und 432 sowie in den Legenden und Bildunterschriften der Abb. 4, 11, 12, 13, 15 und 16, darunter "Turftgrat" und "ecologites". |
| GB-23 | echt | Kreditzeile der Abb. 4 (S. 25) wie zitiert; SwissTopo und GeoCover fehlen im Verzeichnis, S. 16, Z. 490 nennt nur Inversionstests. |
| GB-24 | teilweise echt | Abb. 12 (S. 33) misst Stockhorn #ff7333, Stockhorn-Aufschlüsse #fd3333 und MR-Gneis-Aufschlüsse #ff5933 (Abstände 26 und 40); nicht zutreffend ist, dass alle drei gleich wirken, denn Stockhorn und seine Aufschlüsse unterscheiden sich um 66 und sind als Orange und Rot unterscheidbar. |
| GB-25 | echt | Abb. 14 (S. 35) ohne Lithologielegende trotz S. 14, Z. 430, Abb. 8 und 9 Kopfzeilen ohne Legende, Abb. 11 ohne Spaltenbeschriftung, "ZSF" erst S. 14, Z. 431 aufgelöst. |
| GB-26 | echt | S. 10, Z. 288 bis 289 und Z. 295 vorhanden, "noise" nur S. 9, Z. 255; der Wirgin-Satz steht im arXiv-Abstract math-ph/0401050. |
| GB-27 | echt | S. 10, Z. 293 bis 294, S. 11, Z. 332 bis 333, S. 12, Z. 343 bis 344 und Z. 355 bis 357 geben weder Generator, Mischformel, Faktoren noch Rangregel der PCA an. |
| GB-28 | echt | σd = 0,01 mm/y S. 10, Z. 295 ohne Ableitung, kein "replicate"; Python: 3,254e6/21 ergibt eine RMS-Abweichung von 3,9 mm/y, rund das 390-fache von σd. |
| GB-29 | echt | Abb. 5(c) (S. 26) zeigt am Hotspot Werte um minus 2,1 bis minus 2,2, die Skala von (b) endet bei 3,0 und eine Schraffur liegt auf dem Zentrum, gegen S. 10, Z. 296 bis 297. |
| GB-30 | echt | S. 11, Z. 320 bis 321 vorhanden; Abb. 6(g) endet bei etwa 193 nach 200 Iterationen, Abb. 5(g) bei etwa 201 nach 100 Iterationen. |
| GB-31 | echt | S. 11, Z. 317 lautet "(Figure 6G versus Figure 6G)"; Abb. 6(h) (S. 27) zeigt einen Knick bei etwa 140 Iterationen, keine Oszillation. |
| GB-32 | echt | "area mismatch" S. 11, Z. 330, 334, 335, Abb. 7 (S. 28) mit "Area difference", "Geology misalignment (m²)", "Originial geology"; "simplified" S. 11, Z. 338. |
| GB-33 | echt | S. 12, Z. 348 "highly blended, 2) intermediate", Bildunterschrift Abb. 8 "most blended ... half-way", Paneltitel "Almost fully blended", "Medium blended", "Unblended". |
| GB-34 | echt | S. 12, Z. 348 bis 349 nennt 20 Werte; in Abb. 8 (S. 29) wurden je Panel 14 Marker gezählt, bei JS 0,25, 0,27, 0,34, 0,36 und zehn Werten von 0,44 bis 0,62. |
| GB-35 | teilweise echt | Achse bis 700000 und Satz S. 12, Z. 351 bis 353 bestätigt; nicht zutreffend ist "one to three orders of magnitude", denn der Punkt bei JS 0,34 liegt mit etwa 5000 bis 6000 weniger als eine Größenordnung über 700. |
| GB-36 | echt | Gl. (7) S. 6, Z. 182 ohne Normierung; in Abb. 9 (S. 30) liegt der Datenfehlwert für 21 Tracer bei etwa 3,23e6, für 11 Tracer bei etwa 1,54e6. |
| GB-37 | echt | S. 12, Z. 363 bis 365 ohne Zahlen; Python: 77,3 entspricht 39,1 %, 151,0 entspricht 76,5 % über dem Referenzwert. |
| GB-38 | echt | Abb. 10 Zeile 1 (S. 31) hat 20 Punkte von 200 bis 3000 m mit monoton fallendem Fehler, kein Fall über 3000 m, gegen S. 12, Z. 373 bis S. 13, Z. 374. |
| GB-39 | echt | Abb. 10 Zeile 3 (S. 31) steigt mit Achsenversatz +1,974e2 monoton von etwa 197,420 auf 197,443, ohne Minimum oder Plateau, gegen S. 13, Z. 380 bis 384. |
| GB-40 | echt | S. 13, Z. 395 "Chrysolite", S. 10, Z. 274 und Abb. 11, 15, 16 "Chrysotile"; Chrysolith ist nach minerals.net eine Olivinvarietät. |
| GB-41 | echt | S. 13, Z. 399 bis 401 ohne Kriterium; Messung Abb. 11: Tremolit 0,893 im Monte-Rosa-Granit, 1,000 in der Furgg-Serie, Quarz 0 im Serpentinit. |
| GB-42 | echt | S. 14, Z. 410 bis 418 wie zitiert; Abb. 12 (S. 33) ohne Teileinzugsgebietsgrenze, Abb. 13 (S. 34) mit Metabasit-KDE breit um 0,3 mm/y und Bildunterschrift "all pixels within each lithological unit". |
| GB-43 | echt | S. 14, Z. 421 "the same detrital sample" und Z. 437 bis 438 "a detrital sample taken at the same date and time" wörtlich vorhanden. |
| GB-44 | echt | S. 14, Z. 428 nennt den "average true erosion rate" als Prior für Naturdaten; "export", "annual", "yearly", "multi-year" treten nur S. 3, Z. 66, S. 5, Z. 133, S. 9, Z. 268, S. 15, Z. 453 bis 454 und Z. 468, S. 16, Z. 479 ohne Wert auf. |
| GB-45 | echt | S. 14, Z. 430 bis 434 beschreibt fehlende und kopierte Zirkondaten; Abb. 14 und 16 (S. 35, 37) kennzeichnen die Kopie nicht. |
| GB-46 | echt | S. 14, Z. 435 bis 436 und S. 15, Z. 441 bis 449 nennen Unsicherheiten und JS, aber keine Fehlwerte, obwohl S. 8, Z. 240 sie verlangt. |
| GB-47 | echt | S. 15, Z. 441 bis 442 (0,82) und Z. 446 bis 447 (0,86) vorhanden; Python: minus 1,15 % gegen Zirkon, plus 4,88 % gegen XRD allein. |
| GB-48 | echt | S. 12, Z. 346 bis 347 und S. 15, Z. 447 bis 448 ohne Paarzahl und ohne XRD-Wert; Python: 0,48 × 15/14 = 0,514. |
| GB-49 | echt | Farbskalen der Abb. 5 und 6 ohne Einheit, Abb. 5(h) ohne y-Titel, Abb. 6(g) bis (i) ohne x-Titel und ohne Skalenfaktor, Abb. 13 oben ohne Dichtezahlen (S. 26, 27, 34). |
| GB-50 | echt | "confidence" kommt in S. 1 bis 16 nicht vor; Legende "Low-con dence area" in Abb. 14 bis 16, Schraffur auf dem Maximum in Abb. 15 (S. 36) und auf dem Hotspot in Abb. 14 (S. 35). |
| GB-51 | echt | Abb. 15 (S. 36): Legende Stockhorn #ff5001, Balken #ff844d, 17 vom MR-Gneis-Feld #ff7f41 entfernt; MR-Gneis-Balken #ffa57a liegt 47 vom MR-Granit-Feld #fa9b9a. |
| GB-52 | echt | Abb. 9 (S. 30): x-Achsen "Avg. JS distance between lithologies" mit Werten 0 bis 20, Farbbalken "Number of tracrs", zweites Σ an der y-Achse. |
| GB-53 | echt | Abb. 10 (S. 31) markiert L = 3000 m, σm = 6,2, σd = 0,003 mm/y, µ = 0,1, n_m = 25, während S. 14, Z. 427 bis 428 L = 1200 m, σm = 3, σd = 0,01 mm/y nennt. |
| GB-54 | echt | Ziffern der Achsen in Abb. 10 messen bei 300 dpi 9 bis 10 px Höhe, also deutlich unter 6 pt. |
| GB-55 | echt | Ziele 1 und 2 S. 10, Z. 282 bis 284 und der Verfahrensvergleich kommen in S. 15, Z. 451 bis S. 16, Z. 489 nicht vor. |
| GB-56 | echt | S. 15, Z. 454 bis 455 wie zitiert; der Abstract von De Doncker et al. (2020) (serval.unil.ch) beschreibt bereits die räumliche Inversion mit Prior und Kovarianz und Mineralgehalt als Tracer. |
| GB-57 | echt | S. 15, Z. 457 bis 458 gegen S. 12, Z. 360 und 365; Abb. 9 zeigt 197,4 von 7 bis 21 Tracern, Auflösung wird dort nicht gezeigt. |
| GB-58 | echt | S. 15, Z. 460 bis 461 und S. 16, Z. 484 bis 486 vorhanden; kein Test variiert Zahl der Quellgebiete oder Speicherung, S. 1, Z. 23 "without modelling storage". |
| GB-59 | echt | Empfehlung S. 15, Z. 463 bis 465 gegen S. 9, Z. 270 bis 271 und S. 3, Z. 62; ein JS-Wert für XRD allein fehlt. |
| GB-60 | echt | S. 16, Z. 487 bis 489 und S. 15, Z. 466 vorhanden; Zirkonlauf S. 14, Z. 435 bis 436 instabil, Probenahme S. 9, Z. 251 nur je Lithologie. |
| GB-61 | echt | "depth-integrated" nur S. 15, Z. 470; Abb. 3(a) (S. 24) "detrital sampling: pump sampler", keine Tiefenangabe in den Methoden. |
| GB-62 | echt | S. 16, Z. 490 ist ein einziger Satz ohne Aufzählung der Inhalte; Zenodo-Datensatz und README waren hier nicht abrufbar, der Prämissenteil zum Manuskript trifft zu. |
| GB-63 | echt | Einträge Bearth S. 17, Z. 521, Gjems S. 19, Z. 583, Lafuente Z. 599 bis 600, Moore S. 20, Z. 612 bis 613 ("New-York, 378–379"), Tarantola Z. 634 bis 635 mit zwei ISBN. |
| KK-01 | echt | S. 1, Z. 5 "Quasi-Newtonian", S. 7, Z. 211 und S. 10, Z. 296 "quasi-Newton". |
| KK-02 | echt | S. 1, Z. 24 bis 25 "An ideal fingerprint is 1) capable of ... and 2) remains stable". |
| KK-03 | echt | S. 2, Z. 55 bis 56 "Bayesian linear mixed models" gegen Z. 53 "Bayesian Linear Mixing Models (BLMM)". |
| KK-04 | echt | S. 2, Z. 61 "validated in (De Doncker et al., 2020)". |
| KK-05 | echt | S. 5, Z. 146 bis 147 "it undergoes erosion (Figure 1A) and thereby produces". |
| KK-06 | echt | Großbuchstaben "Figure 1B" S. 5, Z. 146, "Figure 3D and 3E" S. 9, Z. 258, "Figure 5K" S. 10, Z. 294, die Panels tragen Kleinbuchstaben. |
| KK-07 | echt | Gl. (1) S. 5, Z. 154 setzt "for i = 1, ...m" kursiv als Formel. |
| KK-08 | echt | S. 6, Z. 174 "and a prior knowledge". |
| KK-09 | echt | Gl. (5) S. 6, Z. 175 ohne Relationszeichen zwischen den beiden Termen am Seitenbild. |
| KK-10 | echt | S. 6, Z. 181 "becomes Tarantola (2005):". |
| KK-11 | echt | S. 8, Z. 236 "considerately". |
| KK-12 | echt | S. 8, Z. 240 bis 241, Kursivierung "posteriori erosion" am Seitenbild. |
| KK-13 | echt | S. 9, Z. 244 "or when it exceeds the user-defined maximal allowed number of iterations". |
| KK-14 | echt | S. 9, Z. 245 "weighed by the model covariance". |
| KK-15 | echt | S. 9, Z. 267 "Gorner-gletscher", Z. 272 und S. 10, Z. 282 "Gornergletscher", S. 15, Z. 463 "Gorner gletscher", S. 13, Z. 392 "Gorner Glacier". |
| KK-16 | echt | Abb. 3(c) (S. 24) "quarz pattern alignment". |
| KK-17 | echt | Legenden Abb. 4 (S. 25) und 12 (S. 33): "schits", "caclcite-zoisite", "silimanite-biotite", "bündnerschiefer, calcarious". |
| KK-18 | echt | S. 10, Z. 295 "as epsilon is dimensionless". |
| KK-19 | echt | S. 11, Z. 307 "greedy" und Bildunterschriften Abb. 5 und 6 "true" mit geraden Anführungszeichen, sonst typografische (S. 10, Z. 288). |
| KK-20 | echt | S. 11, Z. 319 "(Figure 6D, 6E and 6F )". |
| KK-21 | echt | S. 12, Z. 343 bis 344 "by approaching each lithology’s mineral concentration to its mean". |
| KK-22 | echt | S. 12, Z. 351 "The more resemblant". |
| KK-23 | echt | S. 12, Z. 370 "the maximal amount of non-linear iterations". |
| KK-24 | echt | S. 13, Z. 394 bis 396 mit großgeschriebenen Mineralnamen. |
| KK-25 | echt | S. 13, Z. 400 "supporting the 1) the robustness". |
| KK-26 | echt | "sub-catchment" S. 14, Z. 409, 411, 413 und S. 16, Z. 488 neben "subcatchment" S. 10, Z. 283, 284 und S. 14, Z. 411. |
| KK-27 | echt | S. 14, Z. 424 bis 425 "(Belotti, 2021)" und "(De Doncker et al., 2020)" als Satzglieder. |
| KK-28 | echt | S. 14, Z. 437 "nonlinear inversion technique". |
| KK-29 | echt | "center" S. 15, Z. 441, "normalized" S. 9, Z. 261, "normalised" S. 10, Z. 303, "centre" S. 12, Z. 340. |
| KK-30 | echt | Abb. 10 Zeile 1 (S. 31): x-Achse der zweiten Spalte und Farbbalken "Smooting distance (m)". |
| KK-31 | echt | Abb. 14 (S. 35) "using Zr fingerprint data", "per Zr age bin", Abb. 16 (S. 37) "combined XRD and Zr data". |
| KK-32 | echt | Abb. 15 (S. 36) Legende: "ZSF serpentinite" wird vom Feld "ZSF metabasites" überdeckt. |
| KK-33 | echt | S. 16, Z. 490: die URL ragt über den rechten Satzspiegel, kein Schlusspunkt. |
| KK-34 | echt | S. 16, Z. 491 "(FDD, FH, BB, TA)", in Z. 491 bis 494 sonst "F.H.", "F.D.D.", "B.B.", "T.A.". |
| KK-35 | echt | S. 17, Z. 522 bis 523 "Master’s thesis, University of Lausanne, unpublished master’s thesis". |
| KK-36 | echt | S. 17, Z. 526 bis 527 "Mineralogical society of America". |
| KK-37 | echt | S. 19, Z. 578 "[No title found]"; Titel laut Illinois-Portal "Landscape indicators of human impacts to riverine systems". |
| KK-38 | echt | S. 20, Z. 639 "Bomb-fallout¹³⁷ Cs" mit hochgestellter Zahl am Wort und Leerzeichen vor Cs. |

## Literaturvorschläge

| Vorschlag (Kennung) | Bereits im Literaturverzeichnis |
|---|---|
| Andrews und Eberl (2012), Marine Geology 291-294 (GB-07, GB-08) | nein |
| Braun, Gemignani und van der Beek (2018), Earth Surface Dynamics 6 (GB-08) | nein |
| Cooper, Krueger, Hiscock und Rawlins (2014), Water Resources Research 50 (GB-08) | nein |

Nicht als Ergänzung vorgeschlagen, nur im Einwand oder als Korrektur genannt: Wirgin (2004) (GB-26, nicht im Verzeichnis) und Walling (2009) (GB-04, im Verzeichnis als "E., W. D.").

## Doppelungen

Keine. Geprüfte Nachbarpaare mit gleichem Fundort und verschiedenem Gegenstand: GB-17 und KK-13 (S. 9, Z. 244: Geltung der Stoppregel gegen Wortlaut), GB-40 und KK-24 (S. 13, Z. 395: Mineralname gegen Großschreibung), GB-26 und GB-28 (S. 10, Z. 295: Prior gegen σd), GB-24 und KK-17 (Legende Abb. 4 und 12: Farben gegen Schreibung), GB-51 und KK-32 (Legende Abb. 15: Farben gegen Überdeckung), GB-12 und GB-16 (S. 14, Z. 436: Symbolwechsel als Teilpunkt gegen Definition der Kennzahl).

## Fundorte

| Klasse | Anzahl | Kennungen |
|---|---|---|
| genau | 99 | alle übrigen |
| um 1 bis 2 Zeilen daneben | 2 | GB-08 (zitierter Satz S. 2, Z. 40 bis 41 statt Z. 42 bis 44), GB-11 (Satz beginnt S. 15, Z. 466 statt Z. 467) |
| weiter daneben | 0 | |

## Zählungen

| Urteil | GB | KK | Summe |
|---|---|---|---|
| echt | 61 | 38 | 99 |
| teilweise echt | 2 | 0 | 2 |
| falsch | 0 | 0 | 0 |
| nicht prüfbar | 0 | 0 | 0 |
| geprüft gesamt | 63 | 38 | 101 |

Literaturvorschläge: 3, davon bereits im Verzeichnis 0. Doppelungen: 0. Fundorte: 99 genau, 2 um 1 bis 2 Zeilen daneben, 0 weiter daneben.
