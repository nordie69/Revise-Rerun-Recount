# Verifikation des Gutachtens zu egusphere-2025-4695

Grundlage: Manuskript-PDF, Seitenbilder (150 dpi) und eigene 300-dpi-Renderings der Abbildungsseiten 22 bis 37, text.json. Zeilennummern an den gedruckten Randnummern der Seitenbilder bestätigt (Seiten 1 bis 3, 5 bis 20 gesichtet; Seite 4 als Dublette von Seite 2 und 3 über text.json und difflib). Zahlen mit Python nachgerechnet, Abbildungen am Seitenbild vermessen, Literatur über WebSearch und WebFetch geprüft, soweit lesbar.

## 1. Urteile je Kennung

| Kennung | Urteil | Beleg (ein Satz mit Seite und Zeile) |
|---|---|---|
| GB-01 | echt | S. 1, Z. 3 bis 4 und S. 2, Z. 40 bis 42 stehen wörtlich so; eine Zeit- oder Kostenangabe zu XRD oder Zirkon fehlt im ganzen Text, gestützt nur auf Das et al. (2023) in S. 2, Z. 35. |
| GB-02 | echt | Beide Zitate stehen wörtlich auf S. 1, Z. 7 bis 8 und S. 16, Z. 482 bis 483; die Einschränkungen (S. 11, Z. 312; S. 12, Z. 353; S. 14, Z. 435) stehen dort wie angegeben. |
| GB-03 | echt | Abschnitt 1 (S. 1, Z. 10 bis S. 3, Z. 75) und Abschnitt 2 (S. 3, Z. 77 bis S. 5, Z. 142) ergeben mit difflib je 1153 Wörter, Ähnlichkeit 1,0, kein abweichendes Token. |
| GB-04 | echt | S. 1, Z. 11 bis 12 "E., 2009" und S. 18, Z. 567 bis 568 "E., W. D.: ... UNESCO 2009, ISBN 9789231041358, oCLC" am Seitenbild bestätigt; die Zuordnung zu Walling ist wie im Gutachten nur erschlossen (UNESCO-Seite nicht lesbar). |
| GB-05 | echt | Die Titel von Barker et al. (1997, S. 17, Z. 519 bis 520) und Wilson et al. (1993, S. 21, Z. 649 bis 650) lauten wie zitiert und nennen keine Sedimentfallen oder Dämme (Zitat S. 1, Z. 18 bis 19). |
| GB-06 | echt | Olley et al. (S. 20, Z. 621 bis 622) ist eine Radioaktivitätsstudie und Walden et al. (S. 20, Z. 641 bis 642) eine Magnetikstudie, beide unter Geochemie bzw. Mineralogie zitiert (S. 1, Z. 26; S. 2, Z. 30). |
| GB-07 | echt | Eintrag S. 19, Z. 597 bis 598 wie zitiert; die Verlagsseite hts.org.za zeigt eine Theologie-Arbeit, deren Abstract weder Pollen noch Sediment nennt (Zitat S. 2, Z. 31). |
| GB-08 | echt | Satz S. 2, Z. 36 bis 37 wörtlich; USGS-Einträge bestätigen Eberl (2004, qXRD-Unmixing der Yukon-Sedimente) und Andrews und Eberl (2012, elf künstliche Mischungen), 19 bzw. 11 Jahre vor 2023. |
| GB-09 | echt | Eberl (2004), Andrews und Eberl (2012) und Ehlers et al. (2015, JGR Earth Surface 120(6), 1023 bis 1039) existieren mit den genannten Angaben und fehlen im Verzeichnis S. 17 bis 21; Zitat S. 2, Z. 40 bis 41. |
| GB-10 | echt | Zitat S. 2, Z. 45 bis 48 wörtlich; das Springer-Abstract von Niu et al. (2020) nennt "linear mixing model" und "Gaussian first-order approximation", aber weder Bayes noch frequentistisch. |
| GB-11 | echt | Nordpfeil in Abb. 1b und 2b (S. 22, 23) unerklärt, in Abb. 2b sind 4 von 11 Balken farbig und 7 schwarz, nur die grüne Ebene in Abb. 2c hat eine Farbskala. |
| GB-12 | echt | Zitate S. 5, Z. 151 bis 152 und S. 9, Z. 261 bis 262 wörtlich; das Rechenbeispiel ergibt mit Python (1; 0,6) gegen (1; 0,273) und einen Anteil 0,909 statt 0,5. |
| GB-13 | echt | Gl. 17 (S. 7, Z. 208 bis 209) zählt mit k, Gl. 18 und 19 (S. 8, Z. 215, 219) mit n, aber mit εk im Prior-Term, am Seitenbild bestätigt; n und m sind in Gl. 1 und 4 Pixel- und Tracerzahl. |
| GB-14 | echt | Textsuche: "export", "annual", "yearly" nur S. 3, Z. 66; S. 5, Z. 133; S. 15, Z. 453 bis 454 und 468; S. 16, Z. 479, ohne Wert oder Quelle; Gl. 2 auf S. 5, Z. 160. |
| GB-15 | echt | Gl. 8 (S. 6, Z. 186) Cd = σd²I, 0,01 mm/y in S. 10, Z. 295 und S. 14, Z. 427 bis 428; die Spanne in Abb. 10, Zeile 3 beträgt mit Python 0,012 %. |
| GB-16 | echt | Am Seitenbild S. 7, Z. 189 fehlt das Minus im Exponenten, Gl. 12 (Z. 197) ohne diag, Gl. 14 (Z. 201) ohne Transposition, Gl. 19 (S. 8, Z. 219) ohne Cm⁻¹; Eigenwerte mit Python −0,58 und −15,46 bzw. 0,55 und 5,69. |
| GB-17 | echt | S. 11, Z. 312 nennt die Gradientennormierung ohne Formel, S. 10, Z. 293 bis 295 keinen Schrittweitenwert, S. 12, Z. 355 bis 357 keine Auswahlregel; das Schraffursymbol in Abb. 6 (S. 27) ist unbeschriftet. |
| GB-18 | echt | Gl. 22 (S. 8, Z. 239) mit Wurzeln, S. 14, Z. 436 Spurverhältnis ohne Wurzel mit Index "m,post"; Bezeichnungen in S. 10, Z. 303 und 306, S. 12, Z. 352 und 361 sowie in Abb. 5, 7 bis 10, 14 bis 16 wie angegeben. |
| GB-19 | echt | S. 9, Z. 250 bis 265 und S. 13, Z. 393 bis 398 nennen weder Gerät, Strahlung, Scanbereich, Software-Version noch 2θ-Fenster oder Probenzahl je Einheit. |
| GB-20 | echt | Das Zitat steht auf S. 15, Z. 470 bis 471; Abschnitt 3.4 (S. 9, Z. 250 bis 265) nennt keine dieser Einschränkungen, Abb. 3a zeigt einen Pumpsammler. |
| GB-21 | echt | S. 16, Z. 490 lautet wörtlich "used for the inversion tests" und nennt keine natürlichen Daten; die Angaben zum Zenodo-Archiv waren nicht lesbar (Seite gesperrt). |
| GB-22 | teilweise echt | Vermessung S. 32 bestätigt identische Zeilen Anorthit/Pyroxen und Annit/Phlogopit sowie Ankerit≈Dolomit; nicht zutreffend ist "höchstens 17 von 21", da Muskovit in den Metabasiten abweicht (43 gegen 52 px) und damit 18 unterscheidbare Zeilen bleiben. |
| GB-23 | echt | Chrysotil der Serpentinite in Abb. 15 (S. 36) etwa 0,63 gegen 0,43 aus Abb. 11; bei Quarz ergeben sich Faktoren gegenüber der Furgg-Serie von etwa 0,34, 0,77 und 1,45 wie im Gutachten. |
| GB-24 | echt | S. 14, Z. 420 bis 421 "the same detrital sample" und Z. 437 bis 438 "a detrital sample taken at the same date and time" wörtlich, S. 14, Z. 413 nur "multiple". |
| GB-25 | echt | Legendenfarben in Abb. 4 (S. 25, 300 dpi) #ff7333, #fd3333 und #ff5933, RGB-Summendifferenzen 26 und 40; Abb. 12 (S. 33) hat keine Grenzlinie des Teileinzugsgebiets. |
| GB-26 | echt | Abb. 4 Unterschrift nur "Study area: location, land cover and geology." (S. 25), Abb. 11 ohne Werteachse und Spaltenköpfe (S. 32). |
| GB-27 | echt | Im Credit-Block von Abb. 4 stehen SwissTopo 2018, GeoCover und eine persönliche Mitteilung, beide Quellen fehlen im Verzeichnis; S. 6, Z. 167 nennt die geologische Karte als Grundlage. |
| GB-28 | echt | "Bündnerschiefer" nur S. 10, Z. 275, "ZSF" ab S. 14, Z. 414 vor der Definition in Z. 431, "MR g-g" (Z. 432 bis 433) in keiner Abbildung. |
| GB-29 | echt | Vermessene Balken in Abb. 11: Monte-Rosa-Gneis Tremolit 0,50, Almandin 0,04; ZSF-Sedimente Antigorit 0,52, Dolomit 0,02; Satz S. 13, Z. 399 bis 401 wörtlich ohne Vergleich. |
| GB-30 | echt | S. 10, Z. 288 und S. 13, Z. 374 bis 375 wörtlich, keine Rauschzugabe beschrieben; Abb. 10, Zeile 1 fällt auf etwa 76, mit Python 61,5 % unter 197,4. |
| GB-31 | echt | Farbskala Abb. 5b endet bei 3,0 ohne Überlaufmarke, am Ort des tiefsten Blaus in Abb. 5c (etwa −2) zeigt Abb. 5a etwa 2,8, was eine Posterior über 3 erfordert (S. 26; Text S. 10, Z. 296 bis 297). |
| GB-32 | echt | ZSF, MR, S.,T.,G., JS und Zr stehen unerklärt in Abb. 5j, 8, 9, 14 bis 16, "ELA estimation" (Abb. 4) ist nirgends aufgelöst, "n_m" in Abb. 10 in Codeschrift. |
| GB-33 | echt | Farbskalen 0,90 (Abb. 5d), 0,88 (6d), 0,5 (14), 0,80 (15), 0,5 (16) bis 1,0 bei fast durchgehend dunkelster Farbe; mit Python 819 Pixel und mittleres Diagonalelement höchstens 0,026, 0,016, 0,042. |
| GB-34 | echt | In Abb. 6g bis 6i (S. 27) fehlen x-Beschriftungen, Exponent und Farbskalentitel; Fehlerachsen in Abb. 5 bis 10 ohne Einheit. |
| GB-35 | echt | S. 11, Z. 317 lautet "(Figure 6G versus Figure 6G)"; Abb. 6h zeigt einen Knick bei etwa 138 und danach eine glatte, leicht fallende Kurve ohne Schwingung. |
| GB-36 | echt | Abb. 5g: Minimum etwa 197 bei 20 bis 25, Ende etwa 201 bei 100; Abb. 6g endet bei etwa 193 nach 200 Iterationen; Satz S. 11, Z. 320 bis 321 wörtlich. |
| GB-37 | echt | Im linken und mittleren Streudiagramm von Abb. 8 (S. 29) zähle ich je 14 Marker, bei 20 getesteten Werten (S. 12, Z. 348) und einem als nicht dargestellt genannten. |
| GB-38 | echt | S. 12, Z. 352 "errors exceeding 700 mm/yr"; die y-Achse von Abb. 8 ist eine Pixelsumme, Werte über 700 liegen auch bei JS 0,50 bis 0,54. |
| GB-39 | echt | Die x-Achsen des linken und mittleren Streudiagramms in Abb. 9 (S. 30) heißen "Avg. JS distance between lithologies" und laufen von 0 bis 20. |
| GB-40 | echt | Satz S. 12, Z. 363 bis 365 wörtlich; Höchstfehler etwa 275 (Abb. 7), 348 (Abb. 9) und 677 000 (Abb. 8), mit Python plus 39,6 % und plus 76,6 %. |
| GB-41 | echt | Abb. 10, Zeile 1 endet bei L = 3000 m mit dem kleinsten Fehler, markiert sind L = 3000 m, σm = 6,2, σd = 0,003 mm/y, die Läufe nutzen 1200 m, 3 und 0,01 mm/y (S. 10, Z. 294 bis 295). |
| GB-42 | echt | Abb. 10, Zeile 3 trägt den Offset "+1.974e2" bei monoton steigendem Fehler, Zeile 5 zeigt schon bei 15 Iterationen etwa 200; Text S. 13, Z. 380 bis 389 behauptet anderes. |
| GB-43 | echt | Calcit fehlt in der Liste S. 13, Z. 394 bis 396 und in Abb. 11 und 15, obwohl S. 10, Z. 275 und 278 kalkige Glimmerschiefer und Marmore nennen. |
| GB-44 | echt | S. 13, Z. 395 "Chrysolite", Abb. 11 und 15 "Chrysotile"; Mengenvergleich mit Python ergibt nur diesen Unterschied. |
| GB-45 | echt | S. 14, Z. 411 bis 418 wie zitiert, ohne Probenzahl oder Kriterium; in Abb. 13 (S. 34) liegen ZSF-Sedimente und Furgg-Serie beide mit Maximum nahe 0 mm/y. |
| GB-46 | echt | Im oberen Feld von Abb. 13 trägt die Achse "Density" keine Werte, nur das untere Feld hat 0 bis 2; Zitat aus der Unterschrift wörtlich. |
| GB-47 | echt | S. 14, Z. 428 "a prior equal to the average true erosion rate" wörtlich für die natürlichen Daten; S. 15, Z. 444 bis 445 "same inversion parameters". |
| GB-48 | echt | Abb. 14 (S. 35) ohne Lithologielegende, in Abb. 15 überdeckt das Metabasit-Feld "ZSF serpentinite", in Abb. 16 ist die obere Legendenzeile angeschnitten. |
| GB-49 | echt | In Abb. 14 tragen die beiden Monte-Rosa-Einheiten in jedem Altersbin gleiche Anteile, die Unterschrift nennt die Übertragung aus S. 14, Z. 433 bis 434 nicht. |
| GB-50 | echt | Hotspot in Abb. 14 im Südwesten über den Serpentiniten, Serpentinitfarbe in den Zirkonbalken nur als 1-px-Linien (300 dpi); Zitat S. 14, Z. 439 bis 440 wörtlich. |
| GB-51 | echt | S. 14, Z. 436: 0,87; S. 15, Z. 442: 0,82; Z. 447: 0,86; mit Python minus 1,1 % gegen Zirkon und plus 4,9 % gegen XRD; Farbskala Abb. 16 bis etwa 12 gegen etwa 8,5 in Abb. 15. |
| GB-52 | echt | S. 15, Z. 447 bis 448 nennt 0,48 und 0,57 ohne Paarbasis und ohne XRD-Wert; 21 bzw. 15 Paare mit Python, 13 und 34 Spalten in Abb. 14 und 16. |
| GB-53 | echt | S. 15, Z. 454 bis 455 wörtlich; das Abstract von De Doncker et al. (2020) auf serval.unil.ch enthält beide zitierten Wendungen; S. 5, Z. 151 bis 152 und 158 bis 159 wie angegeben. |
| GB-54 | echt | Zitate S. 15, Z. 458, 460 bis 461 und S. 16, Z. 484 bis 486 wörtlich; S. 12, Z. 360 nennt 7 Tracer als gleichwertig, ein Test zur Zahl der Quellgebiete fehlt. |
| GB-55 | echt | S. 15, Z. 464 Bedingung a) wörtlich, S. 9, Z. 270 bis 272 abgeleitete Geologie unter Eis; mit Python 275 gegen 197,4 ergibt plus 39,3 %. |
| GB-56 | echt | S. 16, Z. 488 bis 489 wörtlich, dagegen S. 14, Z. 435 "highly unstable" mit Werten über 8000 mm/y. |
| GB-57 | echt | Bearth (S. 17, Z. 521), Gjems (S. 19, Z. 583), Lafuente et al. (S. 19, Z. 599 bis 600) und Moore und Reynolds (S. 20, Z. 612 bis 613, "New-York, 378–379") wie beschrieben unvollständig. |
| KK-01 | echt | S. 1, Z. 5 "Quasi-Newtonian", S. 10, Z. 287 und S. 11, Z. 320 "Quasi-Newton", dagegen S. 7, Z. 211 und S. 10, Z. 296 klein geschrieben. |
| KK-02 | echt | S. 2, Z. 48 bis 49 "Non-Linear Least Squares (NLLS) (a constrained linear regression)" und Z. 51 "NNLS" wörtlich. |
| KK-03 | echt | S. 2, Z. 50 "Generalist Likelihood Uncertainty Estimation (GLUE)" wörtlich. |
| KK-04 | echt | S. 2, Z. 51 "Maximal Likelihood Estimation (MLE)" wörtlich. |
| KK-05 | echt | S. 2, Z. 53 "Bayesian Linear Mixing Models (BLMM)" gegen Z. 55 bis 56 "Bayesian linear mixed models". |
| KK-06 | echt | S. 2, Z. 61; S. 11, Z. 333 bis 334; S. 14, Z. 424 bis 425 tragen die Klammerzitate wie zitiert. |
| KK-07 | echt | Text S. 5, Z. 146 bis 149 und S. 10 bis 11 mit Großbuchstaben (Figure 1B, 5A, 6C), Abbildungen mit (a), (b). |
| KK-08 | echt | S. 6, Z. 174 "and a prior knowledge" wörtlich. |
| KK-09 | echt | Am Seitenbild S. 6, Z. 175 steht zwischen p(εm|dobs) und p(dobs|εm) kein Zeichen. |
| KK-10 | echt | S. 6, Z. 181 "Which, in an approximately Gaussian setting, becomes Tarantola (2005):" wörtlich. |
| KK-11 | echt | S. 8, Z. 236 "considerately" wörtlich. |
| KK-12 | echt | Am Seitenbild S. 8, Z. 240 bis 241 ist "a posteriori erosion" kursiv. |
| KK-13 | echt | S. 9, Z. 244 und S. 12, Z. 370 wörtlich. |
| KK-14 | echt | S. 9, Z. 245 "weighed by the model covariance" wörtlich. |
| KK-15 | echt | S. 9, Z. 251 bis 252 verweist für Quellproben auf Abb. 3A und 3B, Abb. 3a zeigt Detritusbeprobung mit Pumpsammler. |
| KK-16 | echt | Abb. 3c (S. 24) "quarz pattern alignment". |
| KK-17 | echt | S. 9, Z. 257 "selected from RRUFF database reference spectra" wörtlich. |
| KK-18 | echt | S. 9, Z. 267 "Gorner-gletscher", Z. 272 "Gornergletscher", S. 13, Z. 392 "Gorner Glacier", S. 15, Z. 463 "Gorner gletscher". |
| KK-19 | echt | Alle sieben Schreibfehler stehen in den Legenden von Abb. 4 (S. 25) und Abb. 12 (S. 33). |
| KK-20 | echt | S. 10, Z. 299 "Zermatt Saas-Fee", S. 12, Z. 340 "Zermatt-Saas-Fee", S. 14, Z. 411 und 414 "Zermatt - Saas Fee", Abb. 12 "Zermatt- Saas Fee". |
| KK-21 | echt | Unterschrift Abb. 11 (S. 32) "Gorner-gletscher", "Stockhorn-Turftgrat-Gornergrat", "ecologites". |
| KK-22 | echt | S. 10, Z. 299 wörtlich wie zitiert. |
| KK-23 | echt | S. 10, Z. 303 "normalised", S. 11, Z. 307 "optimisation", S. 3, Z. 70 "optimize", S. 9, Z. 250 "characterise", S. 13, Z. 398 "characterizing". |
| KK-24 | echt | S. 11, Z. 319 "(Figure 6D, 6E and 6F )" mit Leerzeichen. |
| KK-25 | echt | Abb. 7 (S. 28) Titel "Originial geology (same as forward)". |
| KK-26 | echt | S. 12, Z. 343 bis 344 wörtlich. |
| KK-27 | echt | S. 12, Z. 351 "The more resemblant" wörtlich. |
| KK-28 | echt | S. 12, Z. 352 "mm/yr"; Zählung über Text und Abbildungen ergibt 14-mal "mm/y" und einmal "mm/yr". |
| KK-29 | echt | Abb. 9 (S. 30) Farbskalentitel "Number of tracrs", unter dem y-Achsentitel ein zweites Summenzeichen. |
| KK-30 | echt | Abb. 10, Zeile 1 (S. 31): x-Achse des mittleren Feldes und Farbskalentitel "Smooting distance (m)". |
| KK-31 | echt | Am Seitenbild S. 13, Z. 384 "10-2 mm/y" ohne Hochstellung, Z. 388 "10⁻⁵" hochgestellt. |
| KK-32 | echt | S. 13, Z. 400 "supporting the 1) the robustness" wörtlich. |
| KK-33 | echt | Legenden in Abb. 14 bis 16 (S. 35 bis 37) "Low-con dence area". |
| KK-34 | echt | S. 15, Z. 455 "incorporation of non-linear mixing model." wörtlich. |
| KK-35 | echt | S. 15, Z. 461 bis 462 mit Komma vor "proves" wörtlich. |
| KK-36 | echt | S. 16, Z. 491 "(FDD, FH, BB, TA)", folgende Sätze "F.H.", "F.D.D.", "B.B.", "T.A.". |
| KK-37 | echt | S. 17, Z. 522 bis 523 "Master's thesis, University of Lausanne, unpublished master's thesis, 2021." |
| KK-38 | echt | S. 17, Z. 526 "Mineralogical society of America". |
| KK-39 | echt | S. 19, Z. 578 "[No title found]"; experts.illinois.edu bestätigt "Landscape indicators of human impacts to riverine systems", Aquatic Sciences 64(2), 118 bis 128. |

## 2. Literaturvorschläge gegen das Literaturverzeichnis

| Vorgeschlagene Arbeit | Vorgeschlagen in | Bereits im Verzeichnis |
|---|---|---|
| Eberl (2004), American Mineralogist 89 | GB-08, GB-09 | nein |
| Andrews und Eberl (2012), Marine Geology 291 bis 294 | GB-08, GB-09 | nein |
| Ehlers et al. (2015), JGR Earth Surface 120 | GB-09 | nein |
| Fathabadi und Jansen (2022), CATENA 217 | GB-10 | ja (S. 18, Z. 572 bis 573) |
| Walling (2009), UNESCO | GB-04 | ja, unter "E., W. D." (S. 18, Z. 567 bis 568) |
| De Doncker et al. (2020), ESPL 45 | GB-56 | ja (S. 18, Z. 559 bis 560) |
| Bearth (1953) und Steck et al. (2015) | GB-29, GB-55 | ja (S. 17, Z. 521; S. 20, Z. 631 bis 633) |
| SwissTopo (Landbedeckung 2018) | GB-27 | nein |
| GeoCover | GB-27 | nein |

## 3. Doppelungen

| Kennungen | Gemeinsamer Fundort | Gemeinsamer Gegenstand |
|---|---|---|
| GB-08 und GB-09 | S. 2, Z. 36 bis 37 (Dublette S. 4, Z. 103 bis 104) | frühere XRD-Unmixing-Arbeiten Eberl (2004) und Andrews und Eberl (2012), die fehlen; GB-08 verweist für die Abhilfe auf GB-09 |
| KK-20 und GB-28 | S. 10, Z. 299; S. 14, Z. 411, 414, 431 bis 432; Abb. 12 | uneinheitliche Benennung der Zermatt-Saas-Fee-Einheiten |

Nicht als Doppelung gezählt, weil der Gegenstand verschieden ist: KK-28 und GB-38 (Z. 352, Einheitenschreibung gegen Wert und Schwelle), KK-34 und GB-53 (Z. 455, Artikel gegen Neuheitsanspruch), KK-35 und GB-51 (Z. 461 bis 462, Komma gegen Inhalt), KK-21 und GB-28 (Schreibfehler gegen Namensvielfalt).

## 4. Fundorte

| Klasse | Anzahl | Kennungen |
|---|---|---|
| genau | 94 | alle übrigen |
| um 1 bis 2 Zeilen daneben | 0 | keine |
| weiter daneben | 2 | GB-50 und GB-53 geben Gl. 3 als "p. 6, l. 153" an; Gl. 3 steht auf S. 6, Z. 162 (Z. 153 ist S. 5, "Formally, the forward statement reads"); GB-53 setzt zudem "(eq. 1)" an Z. 158 bis 159, Gl. 1 steht in Z. 154 |

## 5. Zählungen

| Urteil | Anzahl |
|---|---|
| echt | 95 |
| teilweise echt | 1 |
| falsch | 0 |
| nicht prüfbar | 0 |
| Summe | 96 (57 GB, 39 KK) |

Literaturvorschläge: 9 geprüft, davon 4 bereits im Verzeichnis, 5 nicht. Doppelungen: 2. Fundorte: 94 genau, 0 um 1 bis 2 Zeilen daneben, 2 weiter daneben.
