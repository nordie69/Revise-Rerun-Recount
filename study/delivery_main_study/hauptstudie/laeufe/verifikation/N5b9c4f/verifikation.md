# Verifikation des Gutachtens zu egusphere-2025-4695

Grundlage: Manuskript-PDF (37 Seiten), Seitenbilder seiten/ (150 dpi), eigene 300-dpi-Renderings der Seiten 25, 32, 33 und 36, pdftotext -layout und -bbox. Zeilennummern wurden an den gedruckten Randnummern geprüft (Seitenbilder S. 5 bis 8, 12 bis 14, 16, 20; Randnummern-Anker im Layout-Text für alle übrigen Textseiten). text.json ist auf S. 14 ab der Bruchzeile l. 436 um eine Zeile verschoben. Zahlen wurden mit Python nachgerechnet, Abbildungswerte an den Seitenbildern gemessen oder abgelesen, Literatur über WebSearch und WebFetch an offenen Quellen geprüft.

## 1. Urteile je Kennung

| Kennung | Urteil | Beleg |
|---|---|---|
| GB-01 | echt | Beide Zitate stehen wörtlich auf S. 1, l. 3 bis 4 und S. 3, l. 74 bis 75, und der Volltext enthält außer sechs Nennungen von "cost" (l. 3, 4, 40, 74, 107, 141) keine Zahl zu Aufwand, Zeit oder Kosten. |
| GB-02 | echt | Die Zitate stehen auf S. 1, l. 7 bis 8 und S. 16, l. 482 bis 483; die Gegenbelege "proved unstable" (S. 11, l. 312), "fails to converge" (S. 12, l. 353), "highly unstable" (S. 14, l. 435) und die Bildunterschrift von Fig. 8 (S. 29) sind wörtlich vorhanden. |
| GB-03 | echt | Abschnitt 1 (S. 1, l. 9) und Abschnitt 2 (S. 3, l. 76) tragen beide "Introduction"; difflib über l. 10 bis 75 gegen l. 77 bis 142 ergibt je 1153 Wörter und Ähnlichkeit 1.0. |
| GB-04 | echt | Kurzbeleg "E., 2009" auf S. 1, l. 11 bis 12 und S. 3, l. 78 bis 79 sowie Eintrag "E., W. D.: The Impact of global change ..." auf S. 18, l. 567 bis 568 bestätigt; die Autorschaft Walling ist im Gutachten korrekt nur als Frage gestellt (UNESCO-PDF nicht lesbar). |
| GB-05 | echt | Zitate auf S. 1, l. 18 bis 19 und S. 2, l. 28 bis 31 wörtlich; Kobe (Titel S. 19, l. 597), Walden ("mineral magnetic measurements", S. 20, l. 641), Blaen (Abstract ohne Sediment oder Fingerprinting), Olley (226Ra/232Th, 7Be, 137Cs) und Barker (Photogrammetrie, keine Fallen oder Dämme) an den Quellen bestätigt. |
| GB-06 | echt | Zitat S. 2, l. 36 bis 37 wörtlich; Eberl (2004, American Mineralogist 89(11-12), 1784 bis 1794, qXRD-Entmischung) und Andrews und Eberl (2012, Marine Geology 291-294, 24 bis 33, bis sechs Endglieder, elf künstliche Mischungen) an den USGS-Seiten bestätigt und im Literaturverzeichnis S. 17 bis 21 nicht vorhanden. |
| GB-07 | echt | Zitat S. 2, l. 45 bis 48 wörtlich; das Abstract von Niu et al. (2020) nennt lineares Mischmodell und Gauß-Näherung erster Ordnung, aber keinen Vergleich frequentistisch gegen Bayes; Fathabadi und Jansen (2022) mit diesem Vergleich im Titel stehen auf S. 18, l. 572 bis 573. |
| GB-08 | echt | "Non-Linear Least Squares (NLLS) (a constrained linear regression)" auf S. 2, l. 48 bis 49 und "similar to the NNLS approach" auf l. 51 wörtlich vorhanden. |
| GB-09 | echt | Zitate S. 2, l. 58 bis 59 und S. 15, l. 454 bis 455 wörtlich; im ganzen Text keine Datenbank, Suchbegriffe oder Suchzeitraum. |
| GB-10 | echt | Eq. 1 auf S. 5, l. 154 ist ein mit exp(εj) gewichtetes Mittel, die Nichtlinearität entsteht laut l. 157 bis 158 nur aus der Log-Parametrisierung; Zitat S. 15, l. 455 ohne Artikel "a" bestätigt. |
| GB-11 | echt | "optimize" (S. 3, l. 70), "optimisation" (S. 11, l. 307), "normalised" (S. 10, l. 303), "normalized" (S. 11, l. 335), "centre" (S. 12, l. 341), "center" (S. 15, l. 441), "mm/yr" (S. 12, l. 352) gegen "mm/y" (S. 10, l. 295) am Seitenbild bestätigt. |
| GB-12 | echt | "These sediments are then transported or stored." steht auf S. 5, l. 147 bis 148 ohne Annahme zur Speicherung, die Annahme erscheint nur auf S. 1, l. 23 und S. 15, l. 466 bis 468; datiert ist nur die Probe auf S. 14, l. 423 bis 424. |
| GB-13 | echt | Normierung auf das Probenmaximum (S. 9, l. 261 bis 262) und lineares Mittel (S. 5, l. 151 bis 152) wörtlich; das Rechenbeispiel ergibt mit Python 0.556 und 0.444. |
| GB-14 | echt | Am Seitenbild S. 7 und 8: Eq. 17 (l. 208) mit k, Eq. 18 und 19 (l. 215, 219) mit n und εk, Eq. 14 (l. 201) G ohne Transponierte gegen Eq. 16 (l. 205) mit GT, At,xy auf S. 9, l. 262 bis 263; "prior misfit" einmal (S. 6, l. 184) gegen 13 Textstellen plus 2 Bildunterschriften "model misfit". |
| GB-15 | echt | Eq. 2 auf S. 5, l. 160 skaliert d mit der Gesamterosion, ein Wert für den Sedimentexport fehlt im Text, und S. 14, l. 428 nennt für Naturdaten "a prior equal to the average true erosion rate". |
| GB-16 | echt | "simplified, dimensionless form" auf S. 6, l. 161 und "a data standard deviation of 0.01 mm/y" auf S. 10, l. 295 wörtlich vorhanden. |
| GB-17 | echt | Am Seitenbild S. 8, l. 219 wird (GnT Cd−1 Gn)−1 ohne Cm−1 invertiert; bei m < n (S. 6, l. 170 bis 172) hat diese n×n-Matrix höchstens Rang m und ist singulär. |
| GB-18 | echt | Am Seitenbild S. 7, l. 189 lautet Eq. 9 σm² exp(si,j²/L²) ohne Minuszeichen. |
| GB-19 | echt | Fig. 5d (S. 26) zeigt fast flächig Werte zwischen 0.98 und 1.00 auf einer Skala ab 0.90, Fig. 14 (S. 35) ein dunkles Feld auf Skala bis 1.0, was bei Rang(G) ≤ 7 (A hängt nur von der Lithologie ab, S. 9, l. 262 bis 263) und Hunderten Pixeln der Spurgrenze widerspricht. |
| GB-20 | echt | Eq. 22 (S. 8, l. 239) ist ein Wurzelquotient, S. 14, l. 436 ein Spurquotient; Fig. 5f "Normalised posterior covariance", Fig. 5h "Normalised covariance trace", Fig. 7 bis 9 "Trace(post. cov.)", Fig. 10 "Trace(post.covar.)" am Seitenbild; Rechenbeispiel 0.625 gegen 0.75 bestätigt. |
| GB-21 | echt | Die Zitate stehen auf S. 11, l. 312 und S. 12, l. 355 bis 357, und weder Text noch Bildunterschriften beschreiben wahre Karte, Rauschen, Mischformel, PCA-Auswahlregel, Schraffurkriterium (Fig. 5b, S. 26) oder Schrittweite des ersten QN-Tests (S. 10, l. 293 bis 295). |
| GB-22 | echt | Zitate S. 9, l. 250 und l. 254 bis 255 wörtlich; Gerät, Strahlung, 2θ-Bereich, Softwareversion und Probendaten fehlen im ganzen Text. |
| GB-23 | echt | Zitate S. 9, l. 257 und l. 259 bis 260 wörtlich; eine Tabelle der 21 Fenster oder eine Aggregationsregel fehlt. |
| GB-24 | echt | Zitat S. 9, l. 256 bis 257 wörtlich, und in Fig. 11 (S. 32) hat die Spalte ZSF serpentinites in der Zeile Quartz keinen Balken (1 px bei 300 dpi). |
| GB-25 | echt | Zitate S. 9, l. 261 bis 262 und S. 13, l. 399 wörtlich; in Fig. 11 (S. 32) misst der Tremolit-Balken bei MR granite 218 px gegen 244 px Quarz, Antigorit und Chrysotil bei STG 139 und 141 px gegen 245 px Maximum. |
| GB-26 | echt | Namensformen "Gorner-gletscher" (S. 9, l. 267), "Gornergletscher" (l. 272), "Gorner Glacier" (S. 13, l. 392), "Gorner gletscher" (S. 15, l. 463), "Gorner glacier" (Legende Fig. 5, 15, 16) und "metamorphic bündnerschiefer" als Aufschluss der "Zermatt - Saas Fee sediments" (Fig. 4, S. 25) bestätigt. |
| GB-27 | echt | Die Quellzeile "Land cover data: SwissTopo 2018 ... outcrops by GeoCover" steht in Fig. 4 (S. 25), und das Literaturverzeichnis enthält weder "SwissTopo" noch "GeoCover" (0 Treffer). |
| GB-28 | echt | Fig. 4 (S. 25) nennt Steck et al., 2015 als Basis, Fig. 7 (S. 28) zeigt "Geology by Steck et al. 2015" als abweichendste Karte mit "Area difference" und "Geology misalignment (m²)"; "area mismatch" auf S. 11, l. 330, 334, 335. |
| GB-29 | echt | Gemessen auf S. 25 bei 300 dpi: Stockhorn #ff7333, Aufschlüsse Stockhorn #fd3333, Aufschlüsse MR-Gneis #ff5933, RGB-Abstände 26 und 40. |
| GB-30 | teilweise echt | ELA, S.,T.,G. (Fig. 5, 15, 16) und avg. JS (Fig. 8, S. 29) sind unaufgelöst, aber die Bildunterschrift von Fig. 5 (S. 26) nennt (k) ausdrücklich "synthetic source tracer concentrations", und die Bildunterschrift von Fig. 11 (S. 32) löst ZSF und MR nicht auf. |
| GB-31 | echt | Bildunterschriften Fig. 4 und 12 wörtlich; Fig. 10 (S. 31) markiert L = 3000 m, σm = 6.2, σd = 0.003 mm/y, μ = 0.1, n_m = 25 gegen die Vorgaben auf S. 11, l. 324 bis 326; Fig. 12 (S. 33) hat keine Teilgebietsgrenze. |
| GB-32 | echt | Zitate S. 9, l. 270 bis 271 und S. 15, l. 463 bis 464 wörtlich; Fig. 7 (S. 28) zeigt die Steck-Karte bei etwa 1.15 × 10⁷ m², 1.15e7 / 7.37e7 = 15.6 % (Python). |
| GB-33 | echt | Prior "equal to the average true erosion rate" auf S. 10, l. 295, Folge auf S. 13, l. 374 bis 376, eine einzige wahre Karte auf S. 10, l. 288 bis 289, kein Rauschen beschrieben, Datenmisfit in Fig. 5i (S. 26) gegen null. |
| GB-34 | echt | Gemessen auf S. 36 bei 300 dpi: Legende STG #ff5001, MR gneiss #ff7f41, MR granite #fa9b9a; STG-Balken #ff844d (Abstand zur MR-gneiss-Legende 17), MR-gneiss-Balken #ffa57a (Abstand zur MR-granite-Legende 47). |
| GB-35 | echt | Farbskalen Fig. 5a bis c und 6a bis c sowie Achsen "∑ etrue - epost" (S. 26 bis 28) ohne Einheit, Fig. 13 oberes Feld (S. 34) ohne Dichteskala, Fig. 11 (S. 32) ohne Werteachse. |
| GB-36 | echt | Pixelgröße nur aus "4 times the pixel size (L = 1200 m)" (S. 10, l. 294) und "10 times the pixel size (3000 m)" (S. 12, l. 373) ableitbar, Pixelzahl n nirgends genannt. |
| GB-37 | echt | Zitate S. 11, l. 314 bis 316 und l. 320 bis 321 wörtlich, keine Parameter für den SD-Lauf auf S. 11, l. 310 bis 319; Fig. 6g (S. 27) endet nach 200 Iterationen bei etwa 194, Fig. 5g (S. 26) nach 100 bei etwa 201. |
| GB-38 | echt | Fig. 6 (S. 27) zeigt in g und h keine x-Titel, in i weder "Data misfit" noch "1e8" noch Farbskalentitel, und das Schraffurfeld unter b ist unbeschriftet. |
| GB-39 | echt | "(Figure 6G versus Figure 6G)" steht auf S. 11, l. 317; Fig. 6h (S. 27) zeigt einen Knick bei etwa Iteration 140 und danach eine glatte Kurve ohne sichtbare Schwingung. |
| GB-40 | echt | "run with 25 iterations" (S. 11, l. 324) und "Beyond 115 iterations" (S. 13, l. 388) wörtlich; 25 / 115 = 21.7 % (Python). |
| GB-41 | echt | Zitat S. 11, l. 337 bis 338 wörtlich, "Surprisingly" auf l. 338; Fig. 7 (S. 28) zeigt Fehler etwa 197.5, 193.5 und 274.7 für drei Karten. |
| GB-42 | echt | "20 values" auf S. 12, l. 348; in jedem Streudiagramm von Fig. 8 (S. 29) stehen 14 Punkte, die Bildunterschrift nennt nur den am stärksten gemischten Fall als nicht dargestellt. |
| GB-43 | echt | S. 12, l. 352 bis 353 nennt "700 mm/yr for JS < 0.44" mit sichtbar doppeltem Leerraum vor "0.55", während die Fehlerachse von Fig. 8 (S. 29) ohne Einheit bis 700000 reicht und der Punkt bei JS 0.54 ebenfalls über 700 liegt. |
| GB-44 | echt | Beide x-Achsen links und Mitte in Fig. 9 (S. 30) heißen "Avg. JS distance between lithologies", reichen aber von 0 bis 20 und tragen die Tracerzahl. |
| GB-45 | echt | Zitat S. 12, l. 360 bis 362 wörtlich; Fig. 9 rechts (S. 30) zeigt Datenmisfit etwa 3.25e6 bei 21 und 1.55e6 bei 11 Tracern, je Tracer 1.55e5 und 1.41e5 (Python). |
| GB-46 | echt | Zitat S. 12, l. 363 bis 365 wörtlich; 347/197 = +76 % und 274.7/197.5 = +39 % (Python) aus Fig. 9 und 7, Mischung bis über 10⁵ in Fig. 8. |
| GB-47 | echt | pdftotext -bbox für S. 31 ergibt 242 Wortboxen mit 4.8 pt und 62 mit 5.6 pt Höhe gegen etwa 10 pt der Bildunterschrift. |
| GB-48 | echt | Fig. 10 Zeile 1 (S. 31) fällt monoton von etwa 257 auf 76 bis L = 3000 m ohne Läufe darüber, Zeile 3 mit Versatz "+1.974e2" spannt 0.020 bis 0.043, also 0.012 % (Python), gegen die Beschreibung auf S. 12 bis 13, l. 373 bis 384. |
| GB-49 | echt | "Chrysolite" in der Liste auf S. 13, l. 395 gegen "Chrysotile" in Fig. 11, 15, 16 und "chrysotile" auf S. 10, l. 274, an derselben Listenposition. |
| GB-50 | teilweise echt | Bei 300 dpi auf S. 32 sind Annite und Phlogopite sowie Anorthite und Pyroxene in allen sieben Spalten gleich lang, Muscovite weicht nur bei ZSF metabasites ab (44 gegen 53 px), aber aus zwei identischen Paaren folgen 19 und nicht 18 verschiedene Zeilen. |
| GB-51 | echt | Für Chrysotile ergibt Fig. 11 (S. 32) einen erwarteten Anteil der ZSF serpentinites von 224/527 = 0.425, in Fig. 15 (S. 36) misst der gelbe Anteil etwa 0.64. |
| GB-52 | echt | Zitate S. 14, l. 410 bis 411, 413 bis 414 und 415 bis 416 wörtlich; in Fig. 13 (S. 34) hat Furgg series dieselbe auf null gipfelnde Verteilung wie ZSF sediments, und Probenzahl und Datum fehlen. |
| GB-53 | echt | Die Zuweisung des Granit-Fingerabdrucks an MR g-g steht auf S. 14, l. 433 bis 434, die Instabilität auf l. 435, und in Fig. 14 (S. 35) sind die Segmente beider Monte-Rosa-Einheiten gleich hoch. |
| GB-54 | echt | "the same detrital sample" (S. 14, l. 421) gegen "a detrital sample taken at the same date and time" (l. 437 bis 438), ein Entnahmeort fehlt im ganzen Text. |
| GB-55 | echt | "following the methodology described in (Belotti, 2021)" auf S. 14, l. 424 und "unpublished master’s thesis, 2021" auf S. 17, l. 523 wörtlich. |
| GB-56 | echt | In Fig. 14 (S. 35) sind MR-gneiss- und MR-granite-Segmente in jedem Altersintervall gleich hoch, Bildunterschrift (Zitat wörtlich) und Legende nennen keine Imputation. |
| GB-57 | echt | S. 14 bis 15, l. 435 bis 449 nennt Maximalwert und "low resolution" nur für Zirkon, JS nur für Zirkon und kombiniert, Misfits für keinen Fall. |
| GB-58 | echt | Zitat S. 15, l. 443 bis 444 wörtlich, Zahl 34 und Altersintervalle fehlen im Text, Fig. 14 (S. 35) zeigt 13 Intervalle von 40 bis 800 Ma. |
| GB-59 | teilweise echt | 0.86 kombiniert (S. 15, l. 447) liegt über 0.82 XRD (l. 442), +4.9 % (Python), und S. 15, l. 461 bis 462 kehrt die Richtung um, aber S. 3, l. 72 bis 73 ("integrating XRD with zircon data") kehrt sie nicht um, und der Fundort "p. 14, l. 437" für 0.87 liegt auf l. 436. |
| GB-60 | echt | JS 0.48 und 0.57 auf S. 15, l. 448 und Schwelle 0.55 auf S. 12, l. 352 wörtlich; ein JS-Wert für XRD allein fehlt. |
| GB-61 | echt | "Including a broad set of tracer minerals further improves model stability and resolution." (S. 15, l. 458) gegen "The inversion with 7 tracers results in approximately the same posterior solution" (S. 12, l. 360). |
| GB-62 | echt | Zitate S. 15, l. 460 bis 461 und S. 16, l. 484 bis 486 wörtlich, und kein Test in Abschnitt 4.1 oder 4.2 verändert die Zahl der Einheiten oder die Speicherung. |
| GB-63 | echt | Zitate S. 16, l. 488 bis 489 und S. 15, l. 466 wörtlich gegen "highly unstable" und 0.87 auf S. 14, l. 435 bis 436. |
| GB-64 | echt | Die Verfügbarkeitszeile auf S. 16, l. 490 nennt nur "the inversion tests"; die Datenquellen sind belegt (S. 9, l. 252 und 268; S. 14, l. 424), die zweite Nennung der Probe vom 28. Juni steht aber auf l. 437 bis 438 statt 438 bis 439. |
| GB-65 | echt | "[No title found]" (S. 19, l. 578), Gjems (l. 583), Bearth (S. 17, l. 521), doppeltes "master’s thesis" (l. 522 bis 523), "oCLC" (S. 18, l. 567), "New-York" mit Seitenangabe (S. 20, l. 612 bis 613), zwei ISBN (l. 635) bestätigt; der Gergel-Titel ist am Illinois-Eintrag bestätigt. |
| KK-01 | echt | "(steepest descent and Quasi-Newtonian)" auf S. 1, l. 5, "quasi-Newton" auf S. 7, l. 211 und S. 10, l. 296. |
| KK-02 | echt | "spectrocolourmetrics" auf S. 2, l. 34 und S. 4, l. 101. |
| KK-03 | echt | "Generalist Likelihood Uncertainty Estimation (GLUE)" auf S. 2, l. 50 und S. 4, l. 117. |
| KK-04 | echt | "Maximal Likelihood Estimation (MLE)" auf S. 2, l. 51 und S. 4, l. 118. |
| KK-05 | echt | "Bayesian linear mixed models" auf S. 2, l. 55 bis 56 gegen "Bayesian Linear Mixing Models (BLMM)" auf l. 53. |
| KK-06 | echt | "validated in (De Doncker et al., 2020)" auf S. 2, l. 61 und S. 4, l. 128. |
| KK-07 | echt | Satz mit "unique lithological fingerprint (Figure 1B), it undergoes erosion" auf S. 5, l. 146 bis 147 wörtlich. |
| KK-08 | echt | "(Figure 1B)" S. 5, l. 146, "(Figure 5K)" S. 10, l. 294, "(Figure 6D, 6E and 6F )" S. 11, l. 319, während Abbildungen und Unterschriften Kleinbuchstaben verwenden. |
| KK-09 | echt | Am Seitenbild S. 5, l. 154 ist "for i = 1, ...m" kursiv im Formelsatz. |
| KK-10 | echt | "a prior knowledge" auf S. 6, l. 174. |
| KK-11 | echt | Am Seitenbild S. 6, l. 175 steht zwischen p(εm∣dobs) und p(dobs∣εm) kein Relationszeichen. |
| KK-12 | echt | "Which, in an approximately Gaussian setting, becomes Tarantola (2005):" auf S. 6, l. 181. |
| KK-13 | echt | "G = A · exp(ε)" in Eq. 12 auf S. 7, l. 197 und dε = A · exp(ε) auf l. 195. |
| KK-14 | echt | "considerately" auf S. 8, l. 236. |
| KK-15 | echt | Satz auf S. 8, l. 240 bis 241 wörtlich, am Seitenbild ist "posteriori erosion" kursiv. |
| KK-16 | echt | "when it exceeds the user-defined maximal allowed number of iterations" auf S. 9, l. 244. |
| KK-17 | echt | "weighed by the model covariance" auf S. 9, l. 245. |
| KK-18 | echt | S. 9, l. 251 bis 252 verweist für Quellproben auf Figure 3A und 3B, Fig. 3a (S. 24) zeigt aber "detrital sampling: pump sampler". |
| KK-19 | echt | Fig. 3c (S. 24) schreibt "quarz pattern alignment". |
| KK-20 | echt | Legenden Fig. 4 (S. 25) und Fig. 12 (S. 33) enthalten "schits", "caclcite", "silimanite", "GornergratPermo-Mesozoic" und "bündnerschiefer, calcarious". |
| KK-21 | echt | "Small lithological units (such as Zermatt Saas-Fee sediments and Furgg series (Figure 4) and Figure 5J)" auf S. 10, l. 299. |
| KK-22 | echt | Am Seitenbild S. 11, l. 307 steht "greedy" mit geraden Anführungszeichen. |
| KK-23 | echt | "the map proposed by (Steck et al., 2015) with the biggest area mismatch" auf S. 11, l. 333 bis 334. |
| KK-24 | echt | Kartentitel "Originial geology (same as forward)" in Fig. 7 (S. 28). |
| KK-25 | echt | "erosion-rate bump" auf S. 12, l. 341 und "a localised hotspot" auf S. 10, l. 289. |
| KK-26 | echt | "by approaching each lithology’s mineral concentration to its mean" auf S. 12, l. 343 bis 344. |
| KK-27 | echt | "measures the similarity" auf S. 12, l. 345, "Values closer to zero indicate more similar" auf l. 346. |
| KK-28 | echt | "then the half-way in between source signatures" in der Bildunterschrift von Fig. 8 (S. 29). |
| KK-29 | echt | "The more resemblant the source fingerprints are" auf S. 12, l. 351. |
| KK-30 | echt | Farbskalentitel "Number of tracrs" in Fig. 9 (S. 30). |
| KK-31 | echt | "the maximal amount of non-linear iterations" auf S. 12, l. 370. |
| KK-32 | echt | "Smooting distance (m)" steht in Fig. 10, erste Zeile (S. 31), an der mittleren x-Achse und am Farbskalentitel. |
| KK-33 | echt | Am Seitenbild S. 13, l. 384 steht "10-2 mm/y" ohne Hochstellung, auf l. 388 "10⁻⁵" hochgestellt. |
| KK-34 | echt | "Stockhorn-Turftgrat-Gornergrat" in der Bildunterschrift von Fig. 11 (S. 32) gegen "Tuftgrat" auf S. 10, l. 276. |
| KK-35 | echt | "ZSF ophiolites (metabasites, ecologites)" in der Bildunterschrift von Fig. 11 (S. 32). |
| KK-36 | echt | "supporting the 1) the robustness" auf S. 13, l. 400. |
| KK-37 | echt | "Gorner-Grenzgletscher confluence" (S. 13, l. 406), "sub-catchment" (S. 14, l. 409, 411, 413), "Gorner–Grenz" mit Halbgeviertstrich in der Bildunterschrift von Fig. 13 (S. 34). |
| KK-38 | echt | "described in (Belotti, 2021). Using the approach outlined in (De Doncker et al.," auf S. 14, l. 424 bis 425. |
| KK-39 | echt | Am Seitenbild S. 35 bis 37 steht "Low-con dence area" ohne fi-Ligatur. |
| KK-40 | echt | In Fig. 15 (S. 36) überdeckt das Feld ZSF metabasites den Text "ZSF serpentinites", in Fig. 16 (S. 37) ist die obere Hälfte der Zeile abgeschnitten. |
| KK-41 | echt | y-Achse "Normalised abundance per mineral or age" in Fig. 15 (S. 36), die keine Altersintervalle enthält. |
| KK-42 | echt | Am Seitenbild S. 16, l. 490 läuft die URL in den rechten Rand, und der Satz hat keinen Punkt. |
| KK-43 | echt | "All authors (FDD, FH, BB, TA)" auf S. 16, l. 491 gegen "F.H." und "F.D.D." in den Folgesätzen. |
| KK-44 | echt | Am Seitenbild S. 20, l. 639 steht "Bomb-fallout¹³⁷ Cs" mit Hochstellung am Wort und Leerzeichen vor "Cs". |

## 2. Literaturvorschläge: bereits im Literaturverzeichnis?

| Vorschlag | Kennung | Im Verzeichnis |
|---|---|---|
| Eberl (2004), American Mineralogist 89 | GB-06 | nein |
| Andrews und Eberl (2012), Marine Geology 291-294 | GB-06 | nein |
| Fathabadi und Jansen (2022) | GB-07 | ja (S. 18, l. 572 bis 573) |
| Haddadchi et al. (2013) | GB-07, GB-09 | ja (S. 19, l. 586 bis 587) |
| Collins et al. (2020) | GB-09 | ja (S. 18, l. 548 bis 551) |
| Walling (2009), UNESCO | GB-04 | ja, als "E., W. D." (S. 18, l. 567 bis 568) |
| SwissTopo-Produkt 2018 | GB-27 | nein |
| GeoCover-Blätter | GB-27 | nein |

## 3. Doppelungen

| Paar | Fundort | Gegenstand |
|---|---|---|
| GB-26 und KK-21 | S. 10, l. 299 | Namensform "Zermatt Saas-Fee sediments" |
| GB-26 und KK-34 | Bildunterschrift Fig. 11 (S. 32) | Namensform der Einheit Stockhorn-Tuftgrat-Gornergrat |

Teilüberschneidungen mit gleichem Fundort, aber anderem Hauptgegenstand: GB-11 und GB-43 (Einheit "mm/yr", S. 12, l. 352), GB-59 und GB-60 (fehlender JS-Wert für XRD allein, S. 15, l. 447 bis 448), KK-07 und KK-08 (Großbuchstaben der Teilbilder, S. 5, l. 146 bis 147).

## 4. Fundorte

| Klasse | Anzahl | Kennungen |
|---|---|---|
| genau | 107 | alle übrigen |
| 1 bis 2 Zeilen daneben | 2 | GB-59 (0.87 auf l. 436 statt 437), GB-64 (l. 437 bis 438 statt 438 bis 439) |
| weiter daneben | 0 | keine |

## 5. Zählungen

| Urteil | Anzahl |
|---|---|
| echt | 106 |
| teilweise echt | 3 |
| falsch | 0 |
| nicht prüfbar | 0 |
| gesamt | 109 (65 GB, 44 KK) |

Literaturvorschläge: 8, davon 4 bereits im Verzeichnis, 4 nicht. Doppelungen: 2, dazu 3 Teilüberschneidungen.
