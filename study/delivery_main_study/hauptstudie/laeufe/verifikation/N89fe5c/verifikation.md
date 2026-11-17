# Verifikation des Gutachtens zu egusphere-2025-4695

Grundlage: Manuskript-PDF (Seitenbilder `seiten/seite-01.png` bis `seite-37.png`, Abbildungsseiten 22 bis 37 zusätzlich mit 300 dpi gerendert), `text.json` als Suchhilfe, Zeilennummern an den gedruckten Randnummern der Seitenbilder bestätigt. Rechnungen, Suchen, Wortvergleich, Farb- und Schrifthöhenmessungen mit Python (Skripte in `vf/py/`). Literatur über WebSearch und WebFetch, nur Open-Access- oder Katalogseiten; Verlagsseite, Diskussionsseite und Folgefassungen des Manuskripts nicht geöffnet.

## 1 Urteile je Kennung

| Kennung | Urteil | Beleg (ein Satz mit Seite und Zeile) |
|:-|:-|:-|
| GB-01 | echt | Zeitliche Rahmung steht S. 1, Z. 1, 10, 13, Suchtreffer "temporal" 3 und "timing" 2 nur in der Motivation, die Vergleichsläufe nutzen die Probe vom 28. Juni 2019 (S. 14, Z. 423 bis 424) bei jährlicher Exportschätzung (S. 3, Z. 65 bis 66). |
| GB-02 | echt | "cost" 6 Treffer und "efficien" 4 Treffer liegen exakt auf S. 1, Z. 3 und 4, S. 2, Z. 40 und 42, S. 3, Z. 74 und 75, S. 4, Z. 107 und 109, S. 5, Z. 141 und 142, keiner in Diskussion und Schluss. |
| GB-03 | echt | "consistent convergence" steht S. 1, Z. 7, die drei Nichtkonvergenzfälle wörtlich S. 11, Z. 312, S. 12, Z. 353 und S. 13, Z. 387 bis 388. |
| GB-04 | echt | Überschriften "1 Introduction" S. 1, Z. 9 und "2 Introduction" S. 3, Z. 76; difflib ergibt 1153 gegen 1153 Wörter, Verhältnis 1,0. |
| GB-05 | echt | Zitate S. 1, Z. 18 bis 19, Z. 26, S. 2, Z. 28 und 30 wörtlich vorhanden; Barker et al. (Abstract), Blaen et al. (Abstract), Titel von Olley et al. (S. 20, Z. 621 bis 622) und Walden et al. (S. 20, Z. 641) bestätigen die Fehlzuordnung. |
| GB-06 | echt | Kriterium 2 steht S. 1, Z. 24 bis 25, "grain-size" hat nur den Treffer S. 15, Z. 469, "pump" 0 Treffer im Text, Abb. 3a nennt "detrital sampling: pump sampler" (S. 24). |
| GB-07 | echt | "Kobe, 2021" steht S. 2, Z. 31 und S. 4, Z. 98, Eintrag S. 19, Z. 597 bis 598; die Zeitschriftenseite zeigt einen theologischen Artikel ohne Bezug zu Pollen oder Sediment. |
| GB-08 | echt | Die drei Arbeiten fehlen im Literaturverzeichnis S. 17 bis 21; Inhalte an USGS-Seite, ESurf-Seite und PMC-Volltext bestätigt (11 Mischungen aus 4 Endgliedern, Inversion detritischer Abkühlalter, ILR-Transformation), Zitat S. 2, Z. 36 bis 37 wörtlich. |
| GB-09 | echt | Zitat S. 2, Z. 45 bis 48 wörtlich; das Springer-Abstract von Niu et al. (2020) nennt "Gaussian first-order approximation" und keine Zweiteilung frequentistisch und bayesianisch. |
| GB-10 | echt | "NLLS" S. 2, Z. 49 und "NNLS" S. 2, Z. 51 je 2 Treffer ohne Auflösung von NNLS, "Bayesian linear mixed models" S. 2, Z. 55 bis 56; GLUE heißt "Generalized likelihood uncertainty estimation". |
| GB-11 | echt | Zitate S. 2, Z. 58 bis 59, S. 5, Z. 151 bis 152 und S. 15, Z. 454 bis 455 wörtlich; Python bestätigt Gl. 1 gleich A·Softmax und Skaleninvarianz, Niu-Abstract nennt "a linear mixing model". |
| GB-12 | echt | "These sediments are then transported or stored." steht S. 5, Z. 147 bis 148, die Annahme sofortigen Exports erst S. 15, Z. 467 bis 468. |
| GB-13 | echt | Gl. 17 (S. 7, Z. 208) nutzt k, Gl. 18 und 19 (S. 8, Z. 215 und 219) nutzen n mit ε_k im Priorterm, Gl. 5 (S. 6, Z. 175) ε_m, S. 9, Z. 262 bis 263 A_t,xy. |
| GB-14 | echt | S. 6, Z. 167 verweist mit "(geological map) (Figure 2C)" auf eine Tafel mit "tracer 1" bis "tracer n"; schwarze Balken in Abb. 2b ohne Legende (S. 23). |
| GB-15 | echt | Am Seitenbild fehlt in Gl. 5 (S. 6, Z. 175) das Relationszeichen, Gl. 9 (S. 7, Z. 189) hat exp(s²/L²) ohne Minus, Gl. 12 (Z. 197) G = A·exp(ε), Gl. 14 (Z. 201) ohne Transponierte; exp(6,25) = 518,0. |
| GB-16 | echt | Annahme wörtlich S. 6, Z. 177 bis 178; "MCMC", "Markov", "sampling of" nur S. 2, Z. 53 und 57, S. 4, Z. 120 und 124; e³ = 20,1, e⁶ = 403. |
| GB-17 | echt | Gl. 19 (S. 8, Z. 219) invertiert G^T C_d^-1 G ohne C_m^-1, bei m kleiner n laut S. 6, Z. 170 bis 172 singulär (Python: Rang 21 einer 100 × 100-Matrix). |
| GB-18 | echt | Namen S. 8, Z. 236 bis 237, S. 10, Z. 303 und 306, S. 14, Z. 436 sowie in Abb. 5f, 5h, 7 bis 10 und 14 bis 16 am Seitenbild bestätigt; √0,87 = 0,93. |
| GB-19 | echt | Zitate S. 9, Z. 254 bis 257 und S. 16, Z. 490 wörtlich, Suchen nach Gerät und Einstellungen 0 Treffer, "threshold" nur S. 2, Z. 51, S. 4, Z. 118, S. 9, Z. 255; der README-Teil war für mich nicht abrufbar (Zenodo-DOI nicht freigegeben). |
| GB-20 | echt | Zitat S. 9, Z. 259 bis 260 wörtlich; in Abb. 11 (S. 32) sind Annit und Phlogopit sowie Anorthit und Pyroxen in allen 7 Spalten gleich breit, 21 − 4 = 17. |
| GB-21 | echt | Die Bildnachweise "Land cover data: SwissTopo 2018" und "Geological data: data from Steck et al., 2015, personal communication by L. Baumgartner, outcrops by GeoCover" stehen nur in Abb. 4 (S. 25), "topo", "geocover", "personal comm" 0 Treffer, S. 16, Z. 490 nennt nur die Inversionstests. |
| GB-22 | echt | "original geological map" S. 11, Z. 331 und 339, "Originial geology (same as forward)" in Abb. 7, "inferred geology" S. 9, Z. 270, Steck et al. als Quelle in Abb. 4 und als größte Abweichung S. 11, Z. 333 bis 334. |
| GB-23 | echt | Namensformen S. 10, Z. 275 und 299, S. 14, Z. 411, 414 und 432 und in den Legenden der Abb. 4, 5, 11 bis 16 am Seitenbild bestätigt; "ZSF" 2 Treffer, "S.,T.,G", "ELA", "Zr" 0 Treffer im Text. |
| GB-24 | echt | Prior gleich wahrem Mittel S. 10, Z. 295, S. 11, Z. 325 bis 326, S. 13, Z. 375 und S. 14, Z. 428, ein Hotspot S. 10, Z. 288 bis 289, Abb. 10 Zeile 1 fällt von etwa 257 auf 76 (Faktor 3,37). |
| GB-25 | echt | "After several iterations" S. 10, Z. 290 neben "100 iterations" Z. 293, Abschnitt 4.1.2 (S. 11, Z. 310 bis 321) ohne Einstellungen, Iterationsachsen in Abb. 6g bis 6i bis 200. |
| GB-26 | echt | Definitionen S. 8, Z. 235 bis 238; in Abb. 5, 6, 14 und 15 ist die Auflösung gerade am Hotspot niedriger (heller), wo die normierte Unsicherheit am niedrigsten ist, und nahe 1, wo sie hoch ist. |
| GB-27 | echt | "the difference between the true and posterior erosion rates" S. 10, Z. 305, "absolute error" S. 11, Z. 335, S. 12, Z. 352 und 361, "area difference" und "Geology misalignment" in Abb. 7 (S. 28). |
| GB-28 | echt | Zitat S. 11, Z. 320 bis 321 wörtlich; am 300-dpi-Bild endet Abb. 5g bei etwa 200 bis 201 nach Minimum um Iteration 22, Abb. 6g bei etwa 193 nach 200 Iterationen. |
| GB-29 | echt | S. 11, Z. 317 lautet "(Figure 6G versus Figure 6G)", Tafel 6h flacht erst um Iteration 135 bis 140 ab. |
| GB-30 | echt | Szenarien S. 11, Z. 323 bis 324, "noise" nur S. 9, Z. 255, "replicat", "repeat", "duplicate", "triplicate" 0 Treffer, Gl. 8 auf S. 6, Z. 186. |
| GB-31 | echt | S. 12, Z. 348 bis 349 nennt 20 Werte, in Abb. 8 (S. 29) zähle ich 14 Marker links und 14 in der Mitte, 20 − 14 − 1 = 5. |
| GB-32 | echt | "700 mm/yr" steht S. 12, Z. 352, einziger Treffer auf S. 1 bis 21, die Achse in Abb. 8 reicht bis 700000 ohne Einheit. |
| GB-33 | echt | Rangfolge wörtlich S. 12, Z. 363 bis 365; Maxima 274,8 (Abb. 7), 347,0 (Abb. 9) und Unsicherheit 0,746, 0,961, 0,893 am Seitenbild plausibel, 347/274,8 = 1,26. |
| GB-34 | echt | Zitate S. 12, Z. 373 bis S. 13, Z. 374 und S. 13, Z. 381 bis 382 wörtlich; Abb. 10 zeigt keine Werte über 3000 m, Zeile 3 mit Offset "+1.974e2" steigt monoton, markierte Werte L = 3000 m, σm = 6.2, σd = 0.003 mm/y. |
| GB-35 | echt | S. 13, Z. 395 nennt "Chrysolite", Abb. 11, 15 und 16 "Chrysotile", sonst identische 21er-Mengen (Python); Chrysolith ist laut minerals.net eine Olivin-Varietät. |
| GB-36 | echt | Zitate S. 10, Z. 282 bis 283 und S. 13, Z. 399 bis 400 wörtlich; Balkenbreiten in Abb. 11 (Almandin 4 und 11 px, Omphacit 7 px, Tremolit 109 px bei 122 px Vollskala) bestätigt. |
| GB-37 | echt | Zitate S. 14, Z. 410 bis 411 und 415 wörtlich; im Einschub von Abb. 13 liegt die Metabasit-Einheit außerhalb der gestrichelten Grenze, ihre KDE hat deutliche Masse über 0,25 mm/y, Abb. 12 zeigt keine Teilgebietsgrenze. |
| GB-38 | echt | "applied to the same detrital sample" S. 14, Z. 421 gegen "a detrital sample taken at the same date and time" S. 14, Z. 437 bis 438, ohne Proben-ID oder Ort. |
| GB-39 | echt | Zitat S. 14, Z. 423 bis 424 wörtlich, Eintrag S. 17, Z. 522 bis 523 "unpublished", UNIL-Katalogseite (Juni 2021) bestätigt, S. 16, Z. 490 erwähnt keine Zirkondaten. |
| GB-40 | teilweise echt | Prior "average true erosion rate" S. 14, Z. 428 und fehlender Exportwert sind bestätigt, nicht zutreffend ist, dass alle 6 Trefferzeilen die Schätzung als Eingabe nennen, denn S. 15, Z. 468 meint den Exportprozess ("assumes immediate sediment export"). |
| GB-41 | echt | Zitate S. 14, Z. 430 bis 434 wörtlich; in Abb. 14 fehlen gelbe und grüne Segmente, MR-Gneis und MR-Granit haben nahezu gleiche Pixelzahl (113453 gegen 113156), 4/7 = 57,1 %, 21 und 15 Paare. |
| GB-42 | echt | Zitate S. 15, Z. 446 bis 447 und Z. 461 bis 463 wörtlich, 0,86 − 0,82 = 0,04 (4,9 %) gegen 0,87 − 0,86 = 0,01, Farbskalen bis 8 (Abb. 15) und 12 (Abb. 16). |
| GB-43 | echt | Farbbalken in Abb. 5a bis 5c und 6a bis 6c ohne Größe und Einheit, Abb. 6g bis 6i ohne x-Achsentitel, Abb. 11 ohne Wertachse und Spaltenköpfe, obere Dichteachse in Abb. 13 ohne Teilung (S. 26 bis 34). |
| GB-44 | echt | "confiden", "hatch", "low con" 0 Treffer auf S. 1 bis 16, in Abb. 6 (S. 27) steht das Schraffurfeld ohne Beschriftung. |
| GB-45 | echt | Gemessen in Abb. 15: Balkenfarbe #ff844d liegt dem Legendenfeld MR-Gneis (#ff7f41, Summe 17) näher als S.,T.,G. (#ff5001, Summe 128), entsprechend 70 % Deckkraft; Abb. 14 ohne Legende (S. 35). |
| GB-46 | echt | Beide Achsen in Abb. 9 (S. 30) heißen "Avg. JS distance between lithologies" bei Werten 0 bis 21, Farbskala "Number of tracrs". |
| GB-47 | teilweise echt | Abb. 14 "8000" und Abb. 4 "46°N" messen 16 px = 5,3 pt wie angegeben, die Teilstrichzahlen "250" und "3000" in Abb. 10 (S. 31) messen aber 11 px = 3,7 pt statt 2,3 pt; der Kern (deutlich unter 6 pt) bleibt. |
| GB-48 | echt | In Abb. 11 haben vier Einheiten Quarz bei voller Breite (je 0,209 nach Zeilensumme), in Abb. 15 messe ich etwa 0,17, 0,23, 0,32 und 0,22. |
| GB-49 | teilweise echt | Die kopierte MR-Gneis-Signatur ist in Abb. 14 und 16 nicht gekennzeichnet (S. 14, Z. 430 bis 434), nicht zutreffend ist aber, dass die Abbildungen fehlende Daten nur für die Metabasite zeigen, denn auch Serpentinit-Segmente fehlen (vgl. GB-41). |
| GB-50 | echt | In Abb. 15 (S. 36) liegt das Maximum der Farbskala in der Mitte des Gebiets unter der Schraffur, in Abb. 16 (S. 37) umgeben Maximalzellen eine Schraffurfläche; Text S. 14, Z. 440 bis S. 15, Z. 441. |
| GB-51 | echt | "validated" S. 15, Z. 451 und S. 1, Z. 8, "validat" 12 Treffer an den genannten Zeilen, "natural" und "Gorner" in S. 15, Z. 450 bis S. 16, Z. 489 je nur auf S. 15, Z. 463. |
| GB-52 | echt | Zitate S. 15, Z. 458, Z. 460 bis 461 und S. 16, Z. 484 bis 485 wörtlich, "resol" und "source area" 0 Treffer in S. 11, Z. 322 bis S. 12, Z. 365, "storage" 6 Treffer. |
| GB-53 | echt | Zitate S. 15, Z. 459 bis 460 und 464 sowie S. 2, Z. 61 bis S. 3, Z. 62 wörtlich, "glaciated" 1 Treffer, "glacierized" 5 Treffer. |
| GB-54 | echt | Satz S. 16, Z. 483 bis 484 wörtlich; in Abb. 5 (S. 26) fällt der stärkste negative Unterschied (Tafel c) mit dem hellsten Wert der Kovarianzdiagonale (Tafel e) im Hotspot zusammen. |
| GB-55 | echt | Zitate S. 16, Z. 488 bis 489 und S. 15, Z. 466 wörtlich, "highly unstable" S. 14, Z. 435, "poorly distinguishable fingerprints are a major limitation" S. 12, Z. 353 bis 354. |
| GB-56 | echt | Bearth S. 17, Z. 521 ohne Verlag, Gjems S. 19, Z. 583 ohne Reihe und Verlag, Lafuente et al. S. 19, Z. 599 bis 600 ohne Herausgeber und Verlag. |
| KK-01 | echt | "Quasi-Newtonian" nur S. 1, Z. 5, sonst "quasi-Newton" (S. 7, Z. 211; S. 10, Z. 296) und "Quasi-Newton" (S. 10, Z. 287; S. 11, Z. 320). |
| KK-02 | echt | "(... Allan, 2004; E., 2009; ...)" S. 1, Z. 11 bis 12 und S. 3, Z. 78 bis 79, Eintrag "E., W. D." S. 18, Z. 567 bis 568; der Nachname Walling selbst war an der Quelle nicht lesbar. |
| KK-03 | echt | "hyper-parameters" S. 3, Z. 70 und S. 5, Z. 137, "hyperparameters" S. 10, Z. 281 und S. 12, Z. 370. |
| KK-04 | echt | Python zählt 28 Tafelverweise mit 33 Großbuchstaben von "Figure 1B" (S. 5, Z. 146) bis "(Figure 6D, 6E and 6F )" (S. 11, Z. 319). |
| KK-05 | echt | S. 6, Z. 181 lautet "becomes Tarantola (2005):". |
| KK-06 | echt | S. 8, Z. 236 enthält "considerately". |
| KK-07 | echt | S. 9, Z. 245 enthält "weighed by the model covariance". |
| KK-08 | echt | Fünf Schreibweisen an S. 9, Z. 267 und 272, S. 10, Z. 282, S. 13, Z. 392 und 400, S. 15, Z. 463, S. 16, Z. 498 und 499, Abb. 11 sowie Legenden der Abb. 5, 15, 16, zusammen 12 Stellen. |
| KK-09 | echt | "Zermatt Saas-Fee" S. 10, Z. 299, "Zermatt-Saas-Fee" S. 12, Z. 340, "Zermatt - Saas Fee" S. 14, Z. 411 und 414, "Zermatt- Saas Fee" in der Bildunterschrift von Abb. 12; 7 Treffer "Zermatt" im Text. |
| KK-10 | echt | Abb. 3c (S. 24) zeigt "quarz pattern alignment". |
| KK-11 | echt | Beide Legenden (Abb. 4, S. 25; Abb. 12, S. 33) enthalten "GornergratPermo-Mesozoic", "biotite schits", "caclcite-zoisite", "silimanite-biotite", "calcarious mica schist". |
| KK-12 | echt | S. 11, Z. 333 bis 334 lautet "the map proposed by (Steck et al., 2015)". |
| KK-13 | echt | S. 13, Z. 384 hat "10-2 mm/y" ohne Hochstellung, S. 13, Z. 388 "10−5" hochgestellt. |
| KK-14 | echt | S. 13, Z. 400 lautet "supporting the 1) the robustness". |
| KK-15 | echt | "sub-catchment" S. 14, Z. 409, 411, 413 und "sub-catchments" S. 16, Z. 488, "subcatchment" S. 10, Z. 283 und 284. |
| KK-16 | echt | S. 14, Z. 424 bis 425 "described in (Belotti, 2021)" und "outlined in (De Doncker et al., 2020)". |
| KK-17 | echt | Abb. 7 (S. 28) titelt "Originial geology (same as forward)". |
| KK-18 | echt | Abb. 10 (S. 31), Zeile 1: x-Achse Spalte 2 und Farbbalken Spalte 3 lauten "Smooting distance (m)". |
| KK-19 | echt | Bildunterschrift Abb. 11 (S. 32) enthält "Stockhorn-Turftgrat-Gornergrat" und "ecologites", Text "eclogites" S. 10, Z. 274. |
| KK-20 | echt | Abb. 13 (S. 34) zeigt sichtbare Sperrung "Monte R osa", "ZS F", "S tockhorn". |
| KK-21 | echt | Legenden der Abb. 14 bis 16 (S. 35 bis 37) zeigen "Low-con dence area", Abb. 5 "Low-confidence areas". |
| KK-22 | echt | In Abb. 15 (S. 36) überdeckt das nächste Farbfeld das Wortende von "ZSF serpentinite", in Abb. 16 (S. 37) ist die obere Legendenzeile beschnitten. |
| KK-23 | echt | S. 16, Z. 491 "(FDD, FH, BB, TA)", danach "F.H.", "F.D.D.", "B.B.", "T.A." bis Z. 494. |
| KK-24 | echt | S. 17, Z. 522 bis 523 "Master's thesis, University of Lausanne, unpublished master's thesis, 2021." |
| KK-25 | echt | S. 17, Z. 526 "Mineralogical society of America". |
| KK-26 | echt | S. 19, Z. 578 "[No title found]"; der Titel "Landscape indicators of human impacts to riverine systems" mit gleicher DOI ist auf der Illinois-Expertenseite bestätigt. |
| KK-27 | echt | S. 20, Z. 612 "New-York". |
| KK-28 | echt | S. 20, Z. 635 "ISBN 9780898715729 9780898717921". |
| KK-29 | echt | S. 20, Z. 639 zeigt hochgestelltes 137 direkt an "fallout" und Leerzeichen vor "Cs". |

## 2 Literaturvorschläge: bereits im Literaturverzeichnis?

| Vorschlag | Kennung | Im Verzeichnis |
|:-|:-|:-|
| Andrews und Eberl (2012), Marine Geology | GB-08 | nein |
| Braun, Gemignani und van der Beek (2018), Earth Surface Dynamics | GB-08 | nein |
| Stock et al. (2018), PeerJ | GB-08 | nein |
| Klages und Hsieh (1975) | GB-05 | ja (S. 19, Z. 595 bis 596) |
| Wall und Wilding (1976) | GB-05 | ja (S. 20, Z. 643 bis 644) |
| Fathabadi und Jansen (2022) | GB-09 | ja (S. 18, Z. 572 bis 573) |
| Bearth (1953) | GB-36 | ja (S. 17, Z. 521) |
| Steck et al. (2015) | GB-36 | ja (S. 20, Z. 631 bis 633) |
| Collins et al. (2020) | PP-17 | ja (S. 18, Z. 548 bis 551) |
| SwissTopo (Landbedeckung 2018) | GB-21 | nein |
| GeoCover | GB-21 | nein |

## 3 Doppelungen

Vollständige Doppelungen (gleicher Fundort und gleicher Hauptgegenstand): keine. Die Kennungen grenzen sich gegenseitig ausdrücklich ab.

Teilüberschneidungen (dieselbe Tatsache am selben Ort wird in zwei Kennungen erhoben, Hauptgegenstand verschieden):

| Paar | Gemeinsamer Ort und Gegenstand |
|:-|:-|
| GB-25 und GB-28 | Abschnitt 4.1.2, Abb. 6: Iterationszahl 200 und Schrittweite des SD-Laufs nicht angegeben |
| GB-32 und GB-43 | Abb. 7 bis 9: fehlende Einheit der y-Achse des absoluten Fehlers |
| GB-37 und GB-40 | S. 14, Z. 410 bis 416: fehlende Parameter der Gorner-Grenz-Läufe |
| GB-41 und GB-49 | Abb. 14, S. 14, Z. 430 bis 434: kopierte MR-Gneis-Zirkonsignatur |
| GB-24 und GB-34 | S. 16, Z. 482 bis 483: "robust across a range of parameters" zu weit gefasst |
| GB-01 und GB-41 | S. 9, Z. 268 und S. 14, Z. 423 bis 424: eine einzelne Probe trotz mehrjähriger Daten |

## 4 Fundorte

Geprüft wurden alle 85 Kennungen mit zusammen 272 Fundortangaben (221 in Befunden, 51 in Kleinkorrekturen) an den Randnummern der Seitenbilder.

| Lage | Kennungen | Einzelangaben |
|:-|:-|:-|
| genau | 85 | 272 |
| um 1 bis 2 Zeilen daneben | 0 | 0 |
| weiter daneben | 0 | 0 |

Auch die im Einwand eingebetteten Zeilenangaben trafen bei der Stichprobenprüfung durchweg zu.

## 5 Zählungen je Urteil

| Urteil | Befunde (GB) | Kleinkorrekturen (KK) | Zusammen |
|:-|:-|:-|:-|
| echt | 53 | 29 | 82 |
| teilweise echt | 3 (GB-40, GB-47, GB-49) | 0 | 3 |
| falsch | 0 | 0 | 0 |
| nicht prüfbar | 0 | 0 | 0 |
| Summe | 56 | 29 | 85 |
