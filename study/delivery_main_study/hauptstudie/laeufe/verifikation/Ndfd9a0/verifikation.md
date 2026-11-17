# Verifikation des Gutachtens zu egusphere-2025-4695

Grundlage: egusphere-2025-4695.pdf (37 S.), gutachten.md. Zeilennummern wurden aus den gedruckten Randnummern abgeleitet (pdftotext mit Koordinaten, fortlaufende Zählung zwischen den Randmarken, Formelzeilen als je eine Zeile) und an den Seitenbildern 1, 2, 3, 5, 6, 7, 8 bestätigt. text.json weicht auf S. 6 (Z. 176 bis 184) und S. 14 (Z. 437 bis 440) um eine Zeile ab. Abbildungen wurden an den Seitenbildern und an Renderings mit 300 dpi geprüft, Balken und Segmente mit Python ausgemessen (vf/fig/, vf/zahlen.txt).

## 1. Urteile je Kennung

| Kennung | Urteil | Beleg (ein Satz mit Seite und Zeile) |
|---|---|---|
| GB-01 | echt | Beide Zitate stehen wörtlich auf S. 1, Z. 3 bis 4 und S. 3, Z. 74 bis 75 (S. 5, Z. 141 bis 142), und eine Volltextsuche nach cost, time, efficien findet außer diesen Behauptungen und Z. 35 keine Aufwandsangabe. |
| GB-02 | echt | Zitate auf S. 1, Z. 7 und S. 16, Z. 482 bis 483, Gegenbelege S. 11, Z. 312, S. 12, Z. 353, S. 14, Z. 435 vorhanden, Abb. 8 zeigt 14 Punkte je Streudiagramm (20 minus 14 = 6 fehlen), Abb. 10 Zeile 5 zeigt den Sprung zwischen 5 und 15 Iterationen. |
| GB-03 | echt | Zitate auf S. 1, Z. 7 bis 8 und S. 15, Z. 451 wörtlich, "supports" auf S. 14, Z. 417, "some spillover" auf Z. 414 bis 415. |
| GB-04 | echt | Z. 10 bis 75 und Z. 77 bis 142 haben je 1153 Wörter, difflib-Verhältnis 1,0 (Python), Überschrift "2 Introduction" auf S. 3, Z. 76. |
| GB-05 | echt | Satz auf S. 1, Z. 18 bis 19, Barker et al. (1997) behandeln laut Abstract (Portsmouth-Portal) Photogrammetrie der Ufererosion ohne Sedimentfallen oder Dämme, Wilson et al. (1993) laut Titel im Verzeichnis (S. 21, Z. 649 bis 650) Bodenerosion auf den Falklandinseln. |
| GB-06 | echt | Zitate auf S. 2, Z. 28, 30, 31, 29 Zitate in Z. 26 bis 33 (Python), Kobe (2021) ist laut HTS-Artikelseite ein Theologieartikel ohne Pollen, Walden et al. und Blaen et al. laut Titeln S. 20, Z. 641 bis 642 und S. 17, Z. 528 bis 530 Magnetik bzw. Nährstoffmonitoring. |
| GB-07 | echt | Zitate auf S. 2, Z. 36 bis 37 und Z. 61 bis 62, die drei Arbeiten fehlen im Verzeichnis S. 17 bis 21, Andrews und Eberl (2012) testen laut USGS-Eintrag elf künstliche Mischungen aus vier Endgliedern, Ehlers et al. (2015) und EGU21-6207 sind bibliographisch bestätigt. |
| GB-08 | echt | Zitat auf S. 2, Z. 58 bis 59, der Abstract von Niu et al. (2020) nennt 66 Proben, Gaußsche Näherung erster Ordnung und lineares Mischmodell, aber keinen Vergleich frequentistischer und bayesscher Verfahren. |
| GB-09 | echt | "Non-Linear Least Squares (NLLS) (a constrained linear regression)" auf S. 2, Z. 48 bis 49, "NNLS" auf Z. 51, "Bayesian Linear Mixing Models (BLMM)" Z. 53 gegen "Bayesian linear mixed models" Z. 55 bis 56. |
| GB-10 | echt | Zitat auf S. 15, Z. 471 bis 473, "transported or stored" auf S. 5, Z. 147 bis 148, Abschnitt 3.4 (S. 9, Z. 249 bis 265) nennt Korngröße, Orientierung und Überlappung nicht. |
| GB-11 | echt | Am Seitenbild 22 wechseln im Probenzylinder von Abb. 1d dunkelgraue Segmente mit den Lithologiefarben, am Seitenbild 23 sind Balken in Abb. 2b schwarz und nur die grüne Schicht in Abb. 2c hat eine Skala. |
| GB-12 | echt | Gl. 17 iteriert über k (S. 7, Z. 208), Gl. 18 und 19 schreiben εn+1 = εn mit (εk − εprior) (S. 8, Z. 215 und 219), Gl. 1 steht allerdings auf S. 5, Z. 154, nicht Z. 155 bis 156. |
| GB-13 | echt | Kein Exportwert im Text (Suche nach export auf S. 1 bis 16), Prior "the average true erosion rate" auf S. 14, Z. 428, das Zitat "For simplicity" steht auf S. 5, Z. 159, nicht ab Z. 160. |
| GB-14 | echt | Zitat steht auf S. 6, Z. 177 bis 178 (angegeben 178 bis 179), Abb. 10 Zeile 3 zeigt Unsicherheit 0,74015 bis 0,74040, Zeile 1 etwa 0,99 bis 0,27, σd = 0,01 mm/y auf S. 10, Z. 295. |
| GB-15 | echt | "prior misfit" einmal (S. 6, Z. 184), "model misfit" 13 mal im Fließtext (Python), Achsen "Model misfit" in Abb. 5i, 6i, 7 bis 10. |
| GB-16 | echt | Am Bild S. 7 lautet Gl. 9 σm² exp(si,j²/L²) ohne Minus, Gl. 12 G = A · exp(ε), Gl. 14 G Cd⁻¹ ohne Transposition gegen Gᵀ in Gl. 16 (Z. 205), exp(6,25) = 518,0 (Python). |
| GB-17 | echt | Bezeichnungen auf S. 8, Z. 236 bis 237, S. 10, Z. 303 und 306, S. 11, Z. 335, S. 14, Z. 436, S. 15, Z. 441 und 446 sowie in Abb. 5, 7 bis 10 und 14 bis 16 wie angegeben, Gl. 22 ist ein Quotient von Wurzeln. |
| GB-18 | echt | Zitat auf S. 9, Z. 254 bis 255, Gerät, Fenster, Schwellen, Probenzahl und Kornfraktion fehlen, Abb. 3a zeigt einen Pumpenprobenehmer, Z. 470 empfiehlt tiefenintegrierte Proben. |
| GB-19 | echt | Zitate auf S. 9, Z. 260 bis 262 und S. 5, Z. 151 bis 152, das Zahlenbeispiel ergibt mit NNLS Anteil 0,556 bei Residuum 0 (Python), die Angabe zu Collins et al. (2020), Abschnitt 2.2, war nicht lesbar (Springer und PMC gesperrt). |
| GB-20 | echt | Credit-Block am Seitenbild 25 wörtlich, Steck et al. im Verzeichnis S. 20, Z. 631 bis 633, swisstopo und GeoCover fehlen im Verzeichnis, Baumgartner nur S. 16, Z. 499. |
| GB-21 | echt | "ELA estimation" in Abb. 4 ohne Auflösung, Kopfzeilen von Abb. 8 und 9 ohne Legende, in Abb. 15 entspricht die S.,T.,G.-Füllung (255,132,77) der Legendenfarbe (255,80,1) bei 70 % Deckkraft und liegt näher an der MR-gneiss-Legende (255,127,65). |
| GB-22 | echt | Zitate auf S. 9, Z. 270 bis 271 und S. 2 bis 3, Z. 61 bis 62, Empfehlung "well constrained" S. 15, Z. 464, kein Anteil der interpretierten Fläche angegeben. |
| GB-23 | echt | Fünf Gruppen in S. 9 bis 10, Z. 273 bis 279, Zitate auf S. 10, Z. 274 bis 275 und S. 14, Z. 432, Varianten in Abb. 4, 5j, 11, 13, 15 wie angegeben. |
| GB-24 | echt | Zitate auf S. 10, Z. 288 bis 289 und S. 12, Z. 363 bis 364, Prior S. 10, Z. 295 und S. 11, Z. 326, Abb. 7 zeigt 197, 193, 275, Abb. 9 348 bei 2 Tracern, also 39,6 % gegen 76,7 % (Python). |
| GB-25 | echt | Farbskala Abb. 5d 0,90 bis 1,00 und Abb. 14 fast durchgehend am oberen Ende, 0,9 × 819 = 737 und Quotienten 35, 57, 22 (Python), "low resolution" steht auf S. 14, Z. 436, nicht Z. 437. |
| GB-26 | echt | Farbbalken in Abb. 5a, b, c, e ohne Einheit, Abb. 6g bis 6i ohne x-Achsentitel und ohne Faktor in 6i, Abb. 11 ohne Werteachse und Spaltenköpfe (Seitenbilder 26, 27, 32). |
| GB-27 | echt | Zitate auf S. 10, Z. 293 und S. 11, Z. 312, Gl. 18 (S. 8, Z. 215) ohne Normierung, für die SD-Rechnung und den Mischungsversuch S. 13 bis 14, Z. 402 bis 418 keine Einstellungen. |
| GB-28 | echt | Pixelgröße nur über "4 times the pixel size (L = 1200 m)" auf S. 10, Z. 294, keine Pixelzahl im Text, 13 Altersklassen nur in Abb. 14. |
| GB-29 | echt | Zitat auf S. 12, Z. 355 bis 356, für Mischformel (Z. 343 bis 344), Kartenänderung (S. 11, Z. 333) und JS-Normierung keine Angaben. |
| GB-30 | echt | Zitat auf S. 11, Z. 320 bis 321, Abb. 5g endet bei etwa 201 mit Minimum etwa 197, Abb. 6g bei etwa 193 (300 dpi abgelesen), Abb. 10 Zeile 5 etwa 201 bei 195 Iterationen. |
| GB-31 | echt | Zitat mit "Figure 6G versus Figure 6G" auf S. 11, Z. 316 bis 317, Abb. 6h steigt bis zu einem Knick bei etwa 136 und fällt danach glatt leicht ab. |
| GB-32 | echt | Markierungen "L = 3000 m", "σm = 6.2", "σd = 0.003 mm/y", "μ = 0.1", "n_m = 25" in Abb. 10 (Vektortext), Werte im Text S. 10, Z. 294 bis 295, 25/115 = 21,7 % (Python). |
| GB-33 | echt | "area mismatch" S. 11, Z. 330, 334, 335, in Abb. 7 "Area difference" und "Geology misalignment (m²)", Kartennamen wie angegeben, Zitat S. 11, Z. 338 bis 339. |
| GB-34 | echt | Zitate S. 12, Z. 348 bis 349 und Z. 353 sowie Bildunterschrift Abb. 8, je Streudiagramm 14 Punkte gezählt, Fehler bei JS 0,44 bis 0,54 nahe null, Sprung der Unsicherheit zwischen 0,54 und 0,56. |
| GB-35 | echt | JS 0,48 und 0,57 auf S. 15, Z. 448, kein JS-Wert für XRD allein, synthetisch "avg. JS = 0.624" in Abb. 8, Zitate S. 12, Z. 351 bis 352 und S. 14, Z. 416. |
| GB-36 | echt | "700 mm/yr for JS < 0.44" auf S. 12, Z. 352 bis 353, obere Marke der Abb. 8 ist 700000, Achse Σ\|etrue − epost\| ohne Einheit und e undefiniert. |
| GB-37 | echt | Beide linken Streudiagramme der Abb. 9 tragen "Avg. JS distance between lithologies" bei Marken 0,0 bis 20,0 und 21 Punkten, unter dem y-Titel steht ein zweites Σ (Seitenbild 30). |
| GB-38 | echt | Vektortext Abb. 10: Teilstriche 4,8 pt, Achsentitel 5,6 pt, Abb. 8 und 9 7,7 pt, Abb. 13 10,6 pt (Boxhöhen, Python). |
| GB-39 | echt | Zitate S. 12 bis 13, Z. 373 bis 374, Z. 381 bis 382, Z. 387 bis 388, Abb. 10 Zeile 1 fällt monoton bis 3000 m, Zeile 3 Spanne 0,0235 (0,012 %), Zeile 5 Sprung zwischen 5 und 15. |
| GB-40 | echt | Zitat S. 13, Z. 388, Abbruchregel S. 9, Z. 243 bis 244, Datenmisfit in Abb. 10 mit Faktoren 1e6 bis 1e8. |
| GB-41 | echt | "Chrysolite" auf S. 13, Z. 395, "chrysotile" S. 10, Z. 274, Abb. 11, 15, 16 "Chrysotile", Mengendifferenz genau dieses Paar (Python). |
| GB-42 | echt | Gemessen in Abb. 11: Annit, Muskovit, Phlogopit 132/132/132, 76/76/76, 138/138/138, 52/43/52, 161/161/161, 132/132/132 px, Anorthit und Pyroxen in allen Spalten gleich, in Abb. 15 identische Segmente (89, 164, 9, 98, 19, 72 px). |
| GB-43 | teilweise echt | Kriterium fehlt (S. 13, Z. 399 bis 401) und Almandin bzw. Omphacit sind niedrig (0,04 bis 0,10 bzw. 0,05), aber die Angabe, Quarz, Glimmer und Tremolit erreichten "in denselben Spalten" 0,5 bis 1,0, gilt nur für die MR-Gneis-Spalte, in der Metabasitspalte liegen sie bei 0,14 bis 0,25 (Abb. 11, S. 32). |
| GB-44 | teilweise echt | Zitate S. 10, Z. 283 bis 284 und S. 14, Z. 414 bis 416, ZSF-Sedimente, Furgg und MR-Granit gipfeln nahe 0, aber die Kurve Stockhorn, Tuftgrat, Gornergrat in Abb. 13 (S. 34) ist bei 0 am höchsten und fällt monoton, sie ist nicht "flat between 0.77 and 1.17". |
| GB-45 | echt | Abb. 12 (S. 33) zeigt den ganzen Einzugsbereich mit Punkt am Zusammenfluss und hervorgehobenen Farben, aber keine Grenzlinie, Bildunterschrift wörtlich. |
| GB-46 | echt | Zitate S. 14, Z. 423 bis 424 und S. 3, Z. 65 bis 66, "multiple detrital samples" ohne Datum Z. 413, "multi-year" S. 9, Z. 268. |
| GB-47 | echt | Zitate S. 14, Z. 424 und S. 17, Z. 522 bis 523, Datenhinweis S. 16, Z. 490 nennt weder Zirkondaten noch Arbeit. |
| GB-48 | echt | Zitat S. 14, Z. 433 bis 434, zwei Einheiten ohne Zirkondaten (Z. 430 bis 432), Behandlung der Metabasite nicht genannt, Abb. 14 ohne grünes Segment, 21 bzw. 15 Paare (Python). |
| GB-49 | echt | Bildunterschrift Abb. 14 wörtlich, die beiden Monte-Rosa-Farben sind in allen 11 gemeinsamen Klassen gleich lang, Abb. 14 ohne Geologielegende (S. 35). |
| GB-50 | echt | Zitat S. 14, Z. 439, im Text je Fall nur die genannten Einzelwerte (Z. 435 bis 448), "stability" ohne Maß. |
| GB-51 | echt | Abb. 11 Quarz 1,0 in vier Einheiten ergibt je 0,209, Abb. 15 zeigt 0,173, 0,228, 0,326, 0,215 (Python, 300 dpi), Muskovit 0,160, 0,040, 0,220, 0,016, 0,367, 0,198. |
| GB-52 | echt | In Abb. 15 (S. 36) liegen schraffierte Zellen über den hellsten Zellen des Maximums, Zitat S. 14 bis 15, Z. 440 bis 441, keine Definition von "low confidence" im Text. |
| GB-53 | echt | Zitate S. 15, Z. 446, S. 3, Z. 72 bis 73, S. 15, Z. 461 bis 462, Werte 0,87, 0,82, 0,86 und −5,75 %, −1,15 %, +4,88 %, 80 % (Python), "same detrital sample" Z. 421. |
| GB-54 | echt | Zitate S. 15, Z. 454 bis 455 und S. 5, Z. 157 bis 158, Abstract De Doncker et al. (2020, Serval) beschreibt Kleinste-Quadrate-Inversion mit Prior und Kovarianz, synthetisch und natürlich getestet, Mineralgehalt als Tracer, die Angabe "eq. 1 to 3" in "l. 151 to 159" trifft für Gl. 2 (Z. 160) und Gl. 3 (S. 6, Z. 162) nicht. |
| GB-55 | echt | Zitate S. 15, Z. 458 und Z. 460 bis 461, Abb. 9 ab 7 Tracern flach bei etwa 197, 7/21 = 33,3 %, kein Szenario variiert die Zahl der Quellgebiete. |
| GB-56 | echt | Zitat S. 15, Z. 466, Bedingung "essential" Z. 457, kein Test mit Landnutzungsklassen. |
| GB-57 | echt | Zitat S. 16, Z. 484 bis 485, Annahme "assumes immediate sediment export" S. 15, Z. 468, kein Speichertest in Abschnitt 4. |
| GB-58 | echt | Zitat S. 16, Z. 490 wörtlich, keine Probenkennungen im Text, die Angaben zum Zenodo-Archiv waren nicht abrufbar (URL gesperrt). |
| GB-59 | echt | Einträge Bearth (S. 17, Z. 521), Gjems (S. 19, Z. 583) und Lafuente et al. (S. 19, Z. 599 bis 600) ohne Verlag bzw. Herausgeber, Tarantola und Menke mit Verlag. |
| GB-60 | echt | "E., 2009" auf S. 1, Z. 11 bis 12, Eintrag "E., W. D." mit "oCLC" auf S. 18, Z. 567 bis 568, die Autorschaft Walling war an der UNESCO-PDF nicht lesbar. |
| KK-01 | echt | "Quasi-Newtonian" S. 1, Z. 5, "Quasi-Newton" S. 10, Z. 287 und S. 11, Z. 320 sowie Bildunterschrift Abb. 5, "quasi-Newton (QN)" S. 7, Z. 211. |
| KK-02 | echt | "Generalist Likelihood Uncertainty Estimation" auf S. 2, Z. 50 (S. 4, Z. 117). |
| KK-03 | echt | "Maximal Likelihood Estimation" auf S. 2, Z. 51 (S. 4, Z. 118). |
| KK-04 | echt | Klammerzitate in Satzfunktion auf S. 2, Z. 61, S. 6, Z. 181, S. 11, Z. 333 bis 334, S. 14, Z. 424 bis 425. |
| KK-05 | echt | "optimize" S. 3, Z. 70, "normalized" S. 9, Z. 261, "characterizing" S. 13, Z. 398 neben "optimisation" S. 11, Z. 307, "normalised" S. 10, Z. 303, "characterised" S. 5, Z. 150. |
| KK-06 | echt | Text "(Figure 1B)" S. 5, Z. 146 und "(Figure 5A)" S. 10, Z. 289, Panelbeschriftungen in den Abbildungen klein "(a)". |
| KK-07 | echt | "and a prior knowledge" auf S. 6, Z. 174. |
| KK-08 | echt | Am Seitenbild 6, Z. 175 steht zwischen p(εm\|dobs) und p(dobs\|εm) kein Relationszeichen. |
| KK-09 | echt | "We assume weak nonlinearity" steht auf S. 6, Z. 177 (angegeben 178), "nonlinear inversion technique" S. 14, Z. 437, "non-linear" S. 5, Z. 158. |
| KK-10 | echt | "considerately" auf S. 8, Z. 236. |
| KK-11 | echt | "the model - here: our a posteriori erosion rate map - explains" auf S. 8, Z. 240 bis 241. |
| KK-12 | echt | "or when it exceeds the user-defined maximal allowed number of iterations" auf S. 9, Z. 244. |
| KK-13 | echt | "weighed by the model covariance" auf S. 9, Z. 245. |
| KK-14 | echt | "(Figure 3A and 3B)" auf S. 9, Z. 251 bis 252 für Quellproben, Abb. 3a ist "detrital sampling: pump sampler". |
| KK-15 | echt | Abb. 3c (S. 24) enthält "quarz pattern alignment". |
| KK-16 | echt | "(eq. 1-4)" auf S. 9, Z. 263. |
| KK-17 | echt | Varianten S. 9, Z. 267, S. 13, Z. 392 und 400, S. 15, Z. 463, Bildunterschrift Abb. 11, Legenden "Gorner glacier", Sollform S. 9, Z. 272 und S. 10, Z. 282. |
| KK-18 | echt | Alle fünf Schreibfehler stehen in den Legenden von Abb. 4 (S. 25) und Abb. 12 (S. 33). |
| KK-19 | echt | "Zermatt Saas-Fee" S. 10, Z. 299, "Zermatt-Saas-Fee" S. 12, Z. 340, "Zermatt - Saas Fee" S. 14, Z. 411 und 414, Sollform S. 9 bis 10, Z. 273 bis 274 und S. 14, Z. 431. |
| KK-20 | echt | Klammerausdruck wörtlich auf S. 10, Z. 299. |
| KK-21 | echt | Gerade Anführungszeichen bei "greedy" S. 11, Z. 307 und in den Bildunterschriften Abb. 5 und 6, typographische auf S. 10, Z. 288 und 291. |
| KK-22 | teilweise echt | "Steepest-Descent (SD)" steht in der Bildunterschrift Abb. 6 (S. 27), aber die als Vorbild genannte Z. 210 auf S. 7 schreibt ebenfalls groß "Steepest Descent", nur Z. 309 schreibt klein. |
| KK-23 | echt | Leerzeichen vor der Klammer in "(Figure 6D, 6E and 6F )" auf S. 11, Z. 319 am Seitenbild. |
| KK-24 | echt | Titel "Originial geology (same as forward)" in Abb. 7 (S. 28). |
| KK-25 | echt | "measures the similarity" S. 12, Z. 345 neben "Values closer to zero indicate more similar" Z. 346. |
| KK-26 | echt | "The more resemblant" auf S. 12, Z. 351. |
| KK-27 | echt | Doppeltes Leerzeichen "below  0.55" und "mm/yr" auf S. 12, Z. 352 am Seitenbild, "mm/y" in Z. 295, 325, 384, 428, 435. |
| KK-28 | echt | Farbskalentitel "Number of tracrs" in Abb. 9 (S. 30). |
| KK-29 | echt | "the maximal amount of non-linear iterations" auf S. 12, Z. 370. |
| KK-30 | echt | "Smooting distance (m)" an der x-Achse Zeile 1, Spalte 2 der Abb. 10 (S. 31). |
| KK-31 | echt | "10-2 mm/y" ohne Hochstellung auf S. 13, Z. 384, "10−5" hochgestellt in Z. 388. |
| KK-32 | echt | "Stockhorn-Turftgrat-Gornergrat" und "ecologites" in der Bildunterschrift Abb. 11 (S. 32). |
| KK-33 | echt | "supporting the 1) the robustness" auf S. 13, Z. 400. |
| KK-34 | echt | "applied to the same detrital sample" S. 14, Z. 421 gegen "a detrital sample taken at the same date and time" Z. 437 bis 438. |
| KK-35 | echt | "Low-con dence area" in Abb. 14, 15, 16 (Vektortext und Seitenbilder 35 bis 37). |
| KK-36 | echt | "Zr fingerprint data" und "per Zr age bin" in Abb. 14, "combined XRD and Zr data" in Abb. 16. |
| KK-37 | echt | Der Satz auf S. 16, Z. 490 endet mit der DOI ohne Punkt. |
| KK-38 | echt | "(FDD, FH, BB, TA)" S. 16, Z. 491 neben "F.H." Z. 491 und "F.D.D." Z. 492. |
| KK-39 | echt | "Master’s thesis, ..., unpublished master’s thesis, 2021." auf S. 17, Z. 522 bis 523. |
| KK-40 | echt | "Mineralogical society of America" auf S. 17, Z. 526. |
| KK-41 | echt | "[No title found]" auf S. 19, Z. 578, Titel laut Illinois-Experts-Eintrag zur DOI 10.1007/s00027-002-8060-2 "Landscape indicators of human impacts to riverine systems". |
| KK-42 | echt | "Oxford University Press, New-York" auf S. 20, Z. 612. |

## 2. Literaturvorschläge: bereits im Literaturverzeichnis?

| Vorgeschlagene Arbeit | Kennung | Im Verzeichnis |
|---|---|---|
| Andrews und Eberl (2012), Marine Geology 291 bis 294 | GB-07, GB-06, GB-44 | nein |
| Ehlers et al. (2015), JGR Earth Surface 120 | GB-07 | nein |
| De Doncker et al. (2021), EGU21-6207 | GB-07, GB-54 | nein |
| Haddadchi et al. (2013) als Übersichtsquelle | GB-08 | ja (S. 19, Z. 586 bis 587) |
| Collins et al. (2020) als Übersichtsquelle bzw. Beleg für künstliche Mischungen | GB-08, GB-19 | ja (S. 18, Z. 548 bis 551) |
| De Doncker et al. (2020) als Vergleich der Neuheit | GB-54 | ja (S. 18, Z. 559 bis 560) |
| Walling (2009), UNESCO, als Ersatz des Eintrags "E., W. D." | GB-60 | ja, als verstümmelter Eintrag (S. 18, Z. 567 bis 568) |

## 3. Doppelungen

Gezählt wurden Paare mit gleichem Fundort und gleichem Gegenstand.

| Paar | Fundort | Gegenstand |
|---|---|---|
| GB-23 und KK-19 | S. 10, Z. 299; S. 12, Z. 340; S. 14, Z. 411, 414; Abb. 4, Abb. 12 | uneinheitliche Benennung bzw. Schreibung der Zermatt-Saas-Fee-Einheiten |
| KK-19 und KK-20 | S. 10, Z. 299 | Schreibung "Zermatt Saas-Fee sediments", in beiden zur selben Form korrigiert |

Nicht als Doppelung gezählt, weil der Hauptgegenstand verschieden ist und die Stelle nur als Beleg oder mit Querverweis wiederkehrt: GB-02 mit GB-24, GB-34, GB-39; GB-53 mit KK-34; GB-10 mit GB-42 (S. 16, Z. 475 bis 476); GB-44 mit GB-46 (S. 14, Z. 413); GB-36 mit KK-27 (S. 12, Z. 352); GB-47 mit GB-58 (S. 16, Z. 490).

## 4. Fundorte

| Klasse | Anzahl | Kennungen |
|---|---|---|
| genau | 96 | alle übrigen |
| 1 bis 2 Zeilen daneben | 6 | GB-12 (Gl. 1 auf Z. 154 statt 155 bis 156), GB-13 (Zitat Z. 159 statt ab 160), GB-14 (Z. 177 bis 178 statt 178 bis 179), GB-25 ("low resolution" Z. 436 statt 437), GB-54 (Gl. 2 und 3 auf Z. 160 und S. 6, Z. 162, nicht in Z. 151 bis 159), KK-09 (Z. 177 statt 178) |
| weiter daneben | 0 | keine |

## 5. Zählungen

| Urteil | GB | KK | gesamt |
|---|---|---|---|
| echt | 58 | 41 | 99 |
| teilweise echt | 2 | 1 | 3 |
| falsch | 0 | 0 | 0 |
| nicht prüfbar | 0 | 0 | 0 |
| Summe | 60 | 42 | 102 |

Literaturvorschläge: 7 Arbeiten, davon 4 bereits im Verzeichnis, 3 nicht.
Doppelungen: 2 Paare.
Fundorte: 96 genau, 6 um 1 bis 2 Zeilen daneben, 0 weiter daneben.

Teilprüfungen ohne Zugang (Urteil davon nicht berührt): Collins et al. (2020), Abschnitt 2.2 (GB-19); Zenodo-Datensatz (GB-13, GB-47, GB-58); UNESCO-PDF zu Walling (GB-60).
