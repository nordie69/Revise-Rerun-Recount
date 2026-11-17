# Verifikation des Gutachtens zu egusphere-2025-4695

Geprüft am Manuskript (Seitenbilder mit Randnummern, 300 und 600 dpi Neurenderung der Abbildungsseiten), Zahlen mit Python, Literatur über WebSearch und WebFetch.

## Urteile je Kennung

| Kennung | Urteil | Beleg (ein Satz mit Seite und Zeile) |
|---|---|---|
| GB-01 | echt | S. 1, Z. 3 bis 4, S. 2, Z. 40 bis 42 und S. 3, Z. 74 bis 75 behaupten Zeit- und Kosteneffizienz wörtlich, Abschnitt 5 und 6 (S. 15 bis 16) nennen weder Kosten noch Zeiten. |
| GB-02 | echt | Zitat steht S. 1, Z. 6; Eq. 8 (S. 6, Z. 186) ist das einzige Datenkovarianzglied, eine Zahl von Quellproben je Einheit fehlt (S. 9, Z. 251). |
| GB-03 | teilweise echt | Kobe (2021) ist laut Verzeichnis S. 19, Z. 597 und Verlagsseite ein Theologieartikel, zitiert S. 2, Z. 31, und Blaen et al. (2016) ist Echtzeitmonitoring (S. 17, Z. 528); nicht belastbar ist der Barker-Teil, denn Barker et al. (1997) steht S. 1, Z. 19 für direkte Messungen allgemein, Sedimentfallen sind dort nur Beispiel. |
| GB-04 | echt | Zitat S. 3, Z. 62 bis 63; Ehlers et al. (2015, JGR ES 120(6), 1023 bis 1039) und Madella et al. (2022, Geochronology 4, 177 bis 190, Aussage zu über 100 Körnern bestätigt) existieren mit den genannten Angaben und fehlen im Verzeichnis S. 17 bis 21. |
| GB-05 | echt | Abschnitt 2 (S. 3, Z. 76 bis S. 5, Z. 142) wiederholt Abschnitt 1 mit 66 Zeilen und je 1153 Wörtern, difflib-Verhältnis 1,0; 66/489 = 13,5 %. |
| GB-06 | echt | Eq. 1 bis 4 nutzen i, j (S. 5, Z. 154 bis 155), S. 9, Z. 262 bis 263 t und xy, Eq. 17 k (S. 7, Z. 208), Eq. 18 und 19 n mit εk in der Klammer (S. 8, Z. 215, 219), "dimensionless" S. 6, Z. 161 und mm/y S. 10, Z. 295. |
| GB-07 | echt | Zitat S. 6, Z. 166 bis 167; Python: Matrix mit 21 Zeilen und 818 einheitsweise identischen Spalten hat Rang 7, ebenso G = A·diag(exp(ε)). |
| GB-08 | echt | Pixelgröße nur über S. 10, Z. 294 und S. 12, Z. 373 ableitbar; eigene Pixelzählung in Fig. 4 (1 km = 55 px bei 150 dpi) ergibt etwa 73 bis 76 km², also rund 818 Pixel. |
| GB-09 | echt | Seitenbild S. 7, Z. 189 zeigt exp(s²/L²) ohne Minus, Z. 197 G = A·exp(ε), Z. 201 GCd⁻¹ ohne Transponierte, S. 8, Z. 219 Hessian ohne Cm⁻¹ gegen Eq. 20 Z. 225; Python: kleinster Eigenwert der Kovarianz mit positivem Exponenten stark negativ. |
| GB-10 | echt | Keine Formel für R auf S. 8, Z. 230 bis 236; Python: Spur von R = 7,00 bei Rang 7; Fig. 5d (0,90 bis 1,00) und 6d (0,88 bis 1,00) fast überall nahe 1, Fig. 14 Farbskala 0,5 bis 1,0 fast schwarz gegen "low resolution" S. 14, Z. 436. |
| GB-11 | echt | Eq. 22 S. 8, Z. 239 ist Quotient der Wurzeln, S. 14, Z. 436 Spurquotient; Namen "normalised posterior variance" (S. 10, Z. 303), Fig. 5f, 5h, 7 bis 10, 14 bis 16 wie angegeben. |
| GB-12 | echt | S. 9, Z. 251 bis 265 nennt weder Gerät, Strahlung, Scanbereich, Fraktion, Peak-Finder-Einstellungen noch 2θ-Fenster; PCA S. 12, Z. 356 und Gradientennormierung S. 11, Z. 312 ohne Regel. |
| GB-13 | echt | Normierung durch das Probenmaximum S. 9, Z. 261 wörtlich; Python reproduziert Verhältnis 1,25 = 10/8; Fig. 5k (S. 26) zeigt je Tracer auf Summe 1 gestapelte Balken. |
| GB-14 | echt | S. 10, Z. 288 bis 289 nennt eine wahre Karte mit einem Hotspot, Rauschen wird in Abschnitt 4.1 (S. 10 bis 13) nirgends erwähnt. |
| GB-15 | echt | S. 11, Z. 310 bis 319 nennt keine Inversionsparameter für steepest descent; S. 15, Z. 447 bis 448 nennt JS 0,48 und 0,57, für XRD allein keinen JS-Wert. |
| GB-16 | echt | Gemessen bei 300 dpi: Fig. 5g Endwert 200,9, Minimum 197,3 nahe Iteration 20; Fig. 6g Endwert 193,1 und 211,3 bei Iteration 100; Zitat S. 11, Z. 320. |
| GB-17 | echt | Fig. 8 (S. 29) zeigt 14 Punkte gegen "20 values" S. 12, Z. 348; die vier Punkte unter JS 0,44 liegen bei rund 4,6e4, 6,8e5, 5e3 bis 6e3 und 3,2e5 gegen "700 mm/yr" Z. 352, Achse ohne Einheit. |
| GB-18 | echt | Zitat S. 12, Z. 363; Werte Fig. 7 Steck rund 274,7, Fig. 9 ein Tracer rund 347, Fig. 8 rund 6,8e5 bestätigt; Datenmisfit fällt mit Tracerzahl (Fig. 9, S. 30). |
| GB-19 | echt | Fig. 10 Zeile 1 (600 dpi) endet bei 3000 m, Fehler fällt monoton von etwa 257 auf 76, bei rund 1230 m etwa 195 (Faktor 2,55); Zitat S. 12, Z. 373; Annotationen und "Smooting" sichtbar. |
| GB-20 | echt | Fig. 10 Zeile 3 (Offset +1,974e2) steigt monoton von 197,4197 auf 197,4431, Spanne 0,012 %; Unsicherheit 0,74015 bis 0,74040; Text S. 13, Z. 380 bis 384 beschreibt große, nichtmonotone Effekte. |
| GB-21 | echt | Python-Balkenmessung Fig. 11 (S. 32): Anorthit = Pyroxen und Annit = Phlogopit identisch, Ankerit/Dolomit Abstand 0,008, 18 von 21 bei 0,01 und 15 bei 0,05 unterscheidbar, Almandin höchstens etwa 0,1, Tremolit 0,89 im Granit; Captionfehler bestätigt; Zitat S. 13, Z. 399. |
| GB-22 | echt | Fig. 13 (S. 34) Maxima: ZSF-Sedimente und Furgg nahe 0, Granit und Serpentinite etwa 0,03 bis 0,05, Metabasite etwa 0,25 bis 0,3, MR-Gneis etwa 0,6 mm/y; Fig. 12 ohne Grenzlinie, Inset Fig. 13 lässt die Metabasite außerhalb; Zitat S. 14, Z. 414. |
| GB-23 | echt | S. 14, Z. 413 und Caption Fig. 13 nennen "multiple" Proben und Inversionen ohne Zahl, Datum oder Pixelzahl. |
| GB-24 | echt | S. 14, Z. 430 bis 434 bestätigt fehlende Zirkone für ZSF-Metabasite, kopierten MR-g-g-Fingerabdruck und sehr geringe Konzentration; Captions Fig. 14 und 16 ohne Hinweis, Kornzahlen fehlen. |
| GB-25 | teilweise echt | Prior "average true erosion rate" (S. 14, Z. 428), fehlender Sedimentexport und gleiches σd (S. 15, Z. 444 bis 445) bestätigt; nicht zutreffend ist "No sample location ... in text or figures", denn Fig. 12 und 13 (S. 33, 34) markieren den Probenort an der Gorner-Grenzgletscher-Konfluenz. |
| GB-26 | echt | Fig. 10 Ziffernhöhe 22 px bei 600 dpi (etwa 3,7 pt Schrift), Fig. 9 x-Titel "Avg. JS distance" bei 0 bis 21 Tracern (S. 30), Fig. 6g/6h/6i ohne x-Titel (S. 27), Fig. 11 ohne Skala und Spaltenköpfe, Fig. 13 oben ohne Dichtewerte, Schraffur nirgends definiert. |
| GB-27 | teilweise echt | De Doncker et al. (2020) invertieren laut Abstract (serval.unil.ch) Detritaldaten mit Prior und Kovarianz in Erosionskarten und nennen Mineralgehalt; der Neuheitssatz S. 15, Z. 454 bis 455 nennt aber auch das nichtlineare Mischmodell, das nicht im Vorgänger steckt. |
| GB-28 | echt | Zitat S. 15, Z. 461; Abschnitt 4.1.3 und 4.1.4 (S. 11 bis 13) variieren Karte, Mischung, Tracerzahl und fünf Hyperparameter, nie die Zahl der Quelleinheiten. |
| GB-29 | echt | S. 15, Z. 441 bis 442 (0,82) und Z. 447 (0,86 gegen 0,87) bestätigt gegen "further stabilize" Z. 462; Python: im linearen Gaussfall sinkt der Spurquotient mit Zusatzdaten (0,884 auf 0,712). |
| GB-30 | echt | Zitat S. 15, Z. 470; Probennahme nur als "pump sampler" in Fig. 1c (S. 22) und Fig. 3a (S. 24) dargestellt. |
| GB-31 | echt | Zitat S. 16, Z. 482; "Our results suggest ... minimal sediment storage" Z. 484 bis 485 gegen Annahme S. 15, Z. 466 bis 468 und Grenzen S. 12, Z. 353 und 360 bis 361. |
| GB-32 | echt | S. 16, Z. 490 nennt nur "data and codes used for the inversion tests"; Fig. 4 nennt "personal communication by L. Baumgartner"; Zenodo-Inhalt hier nicht abrufbar, vom Gutachten bereits als erschlossen markiert. |
| KK-01 | echt | S. 1, Z. 5 "Quasi-Newtonian", S. 7, Z. 211 "quasi-Newton". |
| KK-02 | echt | S. 1, Z. 11 bis 12 "E., 2009", S. 3, Z. 78 bis 79 wiederholt, S. 18, Z. 567 "E., W. D.:". |
| KK-03 | echt | S. 2, Z. 50 und S. 4, Z. 117 "Generalist Likelihood Uncertainty Estimation". |
| KK-04 | echt | S. 2, Z. 51 und S. 4, Z. 118 "NNLS" nach Einführung von "NLLS" Z. 49. |
| KK-05 | echt | Seitenbild S. 6, Z. 175 zeigt Eq. 5 ohne Relationszeichen. |
| KK-06 | echt | S. 6, Z. 181, S. 8, Z. 223 bis 224, S. 11, Z. 333, S. 2, Z. 61 und S. 14, Z. 424 wie angegeben. |
| KK-07 | echt | S. 9, Z. 245 "weighed by the model covariance". |
| KK-08 | echt | S. 9, Z. 267 "Gorner-gletscher", Z. 272 "Gornergletscher", S. 13, Z. 392 "Gorner Glacier", S. 15, Z. 463 "Gorner gletscher", Caption Fig. 11 "Gorner-gletscher". |
| KK-09 | echt | Fig. 3c Legende (S. 24) "quarz pattern". |
| KK-10 | echt | Fig. 4 (S. 25) und Fig. 12 (S. 33) zeigen "schits", "calcarious", "caclcite", "silimanite", "GornergratPermo-Mesozoic". |
| KK-11 | echt | S. 11, Z. 317 "(Figure 6G versus Figure 6G)"; Spurverlauf ist Fig. 6h. |
| KK-12 | echt | S. 11, Z. 319 "6F )" mit Leerzeichen. |
| KK-13 | echt | S. 12, Z. 340 "Zermatt-Saas-Fee" gegen Z. 299, 411, 431 und Caption Fig. 12 in anderen Schreibungen. |
| KK-14 | echt | S. 13, Z. 395 "Chrysolite" gegen "chrysotile" S. 10, Z. 274 und Fig. 11. |
| KK-15 | echt | Fig. 7 (S. 28) Titel "Originial geology". |
| KK-16 | echt | Fig. 9 (S. 30) Farbleiste "Number of tracrs". |
| KK-17 | echt | Fig. 14 bis 16 (S. 35 bis 37) "Low-con dence area". |
| KK-18 | echt | S. 17, Z. 522 bis 523 "Master’s thesis ... unpublished master’s thesis". |
| KK-19 | echt | S. 19, Z. 578 "[No title found]"; Titel "Landscape indicators of human impacts to riverine systems" über Verzeichnisrecherche bestätigt. |

## Literaturvorschläge

| Vorschlag | Kennung | Bereits im Literaturverzeichnis |
|---|---|---|
| Ehlers et al. (2015) | GB-04 | nein |
| Madella et al. (2022) | GB-04 | nein |

## Doppelungen

Keine zwei Kennungen mit gleichem Fundort und gleichem Gegenstand gefunden.

## Fundorte

| Klasse | Anzahl |
|---|---|
| genau | 50 |
| um 1 bis 2 Zeilen daneben | 1 (GB-11: Zitat beginnt S. 8, Z. 236, Fundort nennt Z. 237 bis 239) |
| weiter daneben | 0 |

## Zählungen je Urteil

| Urteil | Anzahl |
|---|---|
| echt | 48 |
| teilweise echt | 3 |
| falsch | 0 |
| nicht prüfbar | 0 |
| gesamt | 51 |

Literaturvorschläge: 2, davon bereits im Verzeichnis 0. Doppelungen: 0.
