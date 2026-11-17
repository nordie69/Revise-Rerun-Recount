# Verifikation des Gutachtens zu egusphere-2025-4506

Geprüfte Fassung: egusphere-2025-4506.pdf, 29 Seiten, SHA-256 64cb3787456244aa6102e34f776b47e9a612d06e8894d391758ae240dbe415d6 (nachgerechnet, stimmt mit dem Gutachten überein). Zeilennummern aus pdftotext -layout mit den gedruckten Randnummern als Anker; Seiten mit Tabellen und Formeln (S. 11, 13, 14) und alle Abbildungsbefunde an den Seitenbildern (150 dpi) und eigenen 300-dpi-Renderings geprüft. Rechnungen in vf/calc.py, Zitatsuche in vf/find.py und vf/quotes.py.

## 1 Urteil je Kennung

| Kennung | Urteil | Beleg |
|---|---|---|
| GB-01 | echt | Zitat steht wörtlich S. 1, Z. 33 bis 34; die Abstracts von Carpignano et al. 2009 (Piemont, Multi-Risk-Karten, "increased vulnerability", kein Erdbeben- oder Häufigkeitstrend) und Fan et al. 2019 (Chi-Chi, Wenchuan, Hangrutschaktivität über Jahrzehnte erhöht, kein Trend der Häufigkeit) bestätigen den Einwand. |
| GB-02 | echt | Alle sieben Abweichungen stehen so im Text und Verzeichnis (S. 1, Z. 34, 36, 37; S. 2, Z. 45 bis 46, 48 bis 49, 56 bis 57; S. 27, Z. 521, 530 bis 536; S. 28, Z. 577; S. 29, Z. 596, 602), und der Datensatz der Universität Twente nennt für Fan, Yang et al. Landslides 17(1), 147 bis 164, 2020. |
| GB-03 | echt | Alle sechs Wendungen und der subjektlose Satz stehen wörtlich an S. 1, Z. 38 bis S. 2, Z. 39; S. 2, Z. 42 bis 44; S. 3, Z. 85; S. 5, Z. 110 bis 111; S. 10, Z. 193 bis 195; S. 25, Z. 463 bis 464. |
| GB-04 | echt | Die Ziele stehen S. 2, Z. 40 bis 41 und Z. 71 bis 73, das Manuskript hat keine Forschungsfragen und keinen Diskussionsteil (Gliederung 1 bis 4), und "warning" kommt in S. 25 bis 26, Z. 460 bis 492 nicht vor. |
| GB-05 | echt | Die Aussagen stehen S. 2, Z. 42 und Z. 49 bis 51 ohne Suchangabe; Jaboyedoff et al. 2019 (ESurf 7, 439 bis 458, SLBL, 70 Rutschungen, Rekonstruktion früherer Topographie und erodierter Ablagerungen) und Crosta et al. EGU2014-16272 (Rekonstruktion der Vorbruchoberfläche, SPH- und FE-Simulation) sind an der Quelle bestätigt. |
| GB-06 | echt | Der Satz S. 2, Z. 43 bis 46 zitiert Zhang 2024 und Fan 2020, für die kein Eintrag existiert, und Song 2017 sowie Wu 2024 tragen laut Verzeichnis S. 28, Z. 569 bis 570 und Z. 585 bis 586 "Numerical simulation" im Titel. |
| GB-07 | echt | Die Rangaussage S. 2, Z. 46 bis 49 hat keine Zählung; das Abstract von Li et al. 2024 nennt Starkregen und Sickerströmung, keine seismische Eingabe; Cheng und Li 2014 war online nicht lesbar, dieser Teil ist nicht prüfbar. |
| GB-08 | echt | Die 13 Zitate S. 2, Z. 53 bis 63 haben unter den 31 Einträgen S. 26 bis 29, Z. 508 bis 605 keine Entsprechung, 13/29 = 44,8 % nachgerechnet. |
| GB-09 | echt | Der Satz S. 2, Z. 63 bis 64 steht ohne Suche, Ge, Tang und Li 2021 steht S. 27, Z. 540 bis 542 und wird nirgends zitiert, Lin et al. 2022 (NHESS 22, 639 bis 657) quantifiziert laut Abstract den Energietransfer durch Fragmentierung und Kollision. |
| GB-10 | echt | Lin et al. 2022 (Front beschleunigt, Rückteil gebremst, elastische Dehnungsenergie, Fragmentierung effizienter als Kollision), De Blasio und Crosta 2015 (GRL 42, 8463 bis 8470, Schub nur bei Hang über 70° und gleichmäßigen Klasten) und Jaboyedoff 2019 sind an der Quelle bestätigt und fehlen im Verzeichnis S. 26 bis 29; das Zitat steht S. 26, Z. 485 bis 487. |
| GB-11 | echt | Text S. 5, Z. 101 bis 105 und S. 11, Z. 208 bis 209, Fig2(c) (Plagiogranite, Massive gravel, Rubble soil, Hybrid granite östlich des Flusses), Fig3(a) und (b) (Granite braun bzw. rosa gepunktet, Massive gravelly soils hellbraun bzw. grün), Fig4 ("Q del" ohne 4) und Table 1 (zwei Gesteinszeilen) zeigen die genannten Abweichungen; die Farbdifferenz Diorite zu Sand and pebble gravel maß ich mit 22 statt 32 Summen-RGB, ebenfalls unter 40. |
| GB-12 | echt | Die Sätze stehen S. 5, Z. 113 bis 114 und Z. 116 bis 119 ohne Beleg, und He, J. et al. 2023 steht S. 27, Z. 546 bis 548 ohne Zitat im Text. |
| GB-13 | echt | S. 6, Z. 130 bis 135, S. 9, Z. 169, S. 11, Z. 226 bis 229, S. 14, Z. 272 und S. 26, Z. 494 bis 506 nennen weder UAV, Datum, Auflösung, Koordinatensysteme, 3DEC-Version noch Software für Punktwolke, Alpha Shape oder Peak-Erkennung. |
| GB-14 | echt | S. 7, Z. 145 bis 146 nennt vier Teile, Z. 152 bis 156 vier andere Höhenzonen, und Fig3(a) auf S. 8 zeigt nur "I Sliding bed" und "II Accumulation area" mit gepunkteter Trennlinie. |
| GB-15 | echt | Aus S. 7, Z. 149 bis 151 und S. 9, Z. 182 ergeben sich 0,45 km² × 100 m = 4500 × 10⁴ m³, 2400 × 10⁴ / 317563 = 75,6, 12,5 m³ je Block gegen 756,2 bis 1754,3 m³ in Table 2 und 914 bis 1250 m Horizontallänge gegen 450 m; das Abstract von Zhao et al. 2021 nennt 4500 × 10⁴ m³, 450 m × 1000 m und über 100 000 Tote; die Kartenmaße aus Fig2(c) habe ich nicht nachgemessen. |
| GB-16 | echt | S. 7, Z. 160 bis 162 begründet die Restaurierung nur mit sichtbarer Kontinuität, und weder S. 6 bis 9 noch S. 25, Z. 463 bis 468 enthalten einen Volumen- oder Fehlervergleich. |
| GB-17 | echt | S. 7, Z. 159 bis 160 nennt a-a' und b-b', Fig2(c) auf S. 6 zeigt nur eine rote Linie mit "a" und "a'" (300-dpi-Ausschnitt), Fig3(b) auf S. 8 ist mit "(a-a')" betitelt und hat Achsen ohne Größe und Einheit sowie das unerklärte "80°". |
| GB-18 | echt | S. 9, Z. 175 bis 182, S. 10, Z. 193 bis 203 und S. 11, Z. 206 bis 212 nennen weder Dämpfung, Blocktyp, Zonengröße noch Fugengeometrie; Table 2 ergibt 10,0 bis 23,2 m Blockhöhe, und Table 1 hat Schersteifigkeit über Normalsteifigkeit (1500 zu 960 und 180 zu 100 GPa/m). |
| GB-19 | echt | Die Bezeichnungen stehen S. 9, Z. 176 bis 180, S. 11, Z. 209 bis 210, Table 1 ("discontinuities", "potential discontinuities") und S. 15, Z. 308 bis 309, 313 und 320, ohne Zuordnung zu Tabellenzeilen. |
| GB-20 | teilweise echt | Unbelegte Aussage S. 10, Z. 186 bis 189, kein Zitat nach Z. 63, fehlende Angaben zum Datensatz und fehlende Sensitivität sind belegt, Feng et al. 2023 nennt die Moxi-Störung als Quelle; nicht zutreffend ist der Widerspruch zur eigenen tektonischen Beschreibung, denn S. 5, Z. 97 bis 99 nennt die Longmenshan-Störung selbst als einen der drei Äste am Standort. |
| GB-21 | echt | S. 10, Z. 189 bis 192, die Fig2-Legende S. 6, Z. 126 bis 127, S. 9, Z. 180, S. 6, Z. 136 bis 137, S. 11, Z. 206 bis 207 und S. 26, Z. 505 bis 506 nennen für Luding-Datensatz, Bild, Karte, Profil, Tafel und Labortests keine Quelle. |
| GB-22 | echt | Der Einschub in Fig4 auf S. 10 hat die Ordinate "Acceleration (gal)" mit -100, 0, 100, eine Abszisse ohne Titel und Werte und die unerklärten Marken tp, tPGA, tf, te; die Legende γo2, Q del, γM2 ist in der Bildunterschrift Z. 192 nicht aufgelöst. |
| GB-23 | echt | Fig5(a) "Travel distance (m)", Fig5(b) bis (f) "Travel Displacement (m)" (S. 12), S. 11, Z. 221, 225, 227, 234, S. 1, Z. 23, S. 25, Z. 474 und Fig10(b) "Travel distance (m)" (S. 23) zeigen die genannten Varianten. |
| GB-24 | echt | S. 11, Z. 227 bis 234 definiert die Bezugsgröße der Schwelle nicht; meine Zählung ergab in Fig5(d) etwa 80 bis 110 rote Marken und in Fig10(b) eine Summe von etwa 1200 bis 1225, also beides ungleich 1139; die Abweichung zur Zahl 130 des Gutachtens ändert die Prämisse nicht. |
| GB-25 | echt | Mit Table 2 (S. 13) und den abgelesenen Anfangswerten von Fig9 ergeben sich 239, 223, 235, 164, 316, 173, 30, 193, 82 und 44 m Höhe über Bezug und ein Bezugsniveau von 101 bis 711 m, und 756,2 × 2300 × 9,81 × 840 = 14,3 GJ; die Datumsangabe steht S. 13, Z. 253 bis 255. |
| GB-26 | echt | S. 13, Z. 256 bis 257 und Table 2 benutzen verschiedene Namen, und Fig6 auf S. 14 beschriftet hangabwärts "Top", "Lower middle part", "Upper middle part", "Bottom", ohne Punktkennungen und ohne Achsentitel. |
| GB-27 | echt | "unbalanced" steht nur S. 13, Z. 258 und in Table 2, Zeile 11, und Abschnitt 3 (S. 15 bis 22) zeigt weder Spannungsverläufe der Blöcke noch die Kraftgeschichte. |
| GB-28 | echt | S. 14, Z. 281 bis 284 setzt α = 1 ohne Einheit, Eingabepunkte oder Sensitivität, obwohl Z. 281 den direkten Einfluss von α selbst nennt. |
| GB-29 | echt | Die Varianten stehen S. 1, Z. 25; S. 3, Z. 89; S. 14, Z. 275 und 287 bis 288; S. 24, Z. 440 bis 441; S. 25, Z. 453 und 458 bis 459; S. 26, Z. 488, und Z. 440 benutzt "A" gegen S0 und St in Gl. (6); Z. 287 liegt auf S. 14, nicht S. 15. |
| GB-30 | echt | S. 14, Z. 278 bis 280 bezieht V0 und S0 auf die Rutschmasse, Vt und St auf die Hülle, keine Absolutwerte werden genannt, die sieben Namen stehen an den genannten Stellen, und die Achsenmaxima von Fig9 ergeben 50,7 GJ gegen über 6000 GJ am Start von Fig12. |
| GB-31 | echt | Fig7(h) bis (n) auf S. 18 zeigen einen Vertikalschnitt mit Abszisse 0 bis 2700 und Ordinate 0 bis 1200 ohne Achsentitel, Farbskalen 0, -33, -31, -33, -33, -33, -47 "Mpa", während S. 15, Z. 301 bis 302 von "along the sliding plane" spricht. |
| GB-32 | echt | Fig7(h) auf S. 18 ist einheitlich rot mit Skala 0 bis "0Mpa", Fig7(i) zeigt bereits 0 bis -33 MPa mit Tiefengradient, und S. 10, Z. 199 bis 200 verlangt statisches Gleichgewicht vor der Dynamik; ρgh = 33,1 MPa nachgerechnet. |
| GB-33 | teilweise echt | Table 2 (S. 13) enthält keine Beschleunigung, und S. 15, Z. 308 bis 323 schreibt P- und S-Wellen, Verstärkung und Trennflächensteuerung zu; nicht zutreffend ist, dass Trennflächen aus dem Modell ausgeschlossen wurden, denn S. 9, Z. 179 bis 180 und S. 11, Z. 209 bis 212 mit Table 1 führen eine Trennfläche und zwei Fugenscharen ein. |
| GB-34 | echt | Die Aussagen S. 16, Z. 327 bis 329, 333 bis 335 und 350 bis 352 tragen keine Quellenangabe, und Feldarbeit wird S. 2, Z. 65, S. 13, Z. 265 bis 266 und S. 25, Z. 472 bis 473 genannt, aber nirgends beschrieben. |
| GB-35 | echt | Der höchste Punkt in Fig5(b) auf S. 12 liegt bei etwa 45 m/s (eigene Ablesung 44,8 m/s), während S. 16, Z. 330 31,6 m/s nennt und die Bildunterschrift Z. 238 bis 239 keinen Block nennt; die Einschübe haben keine Achsentitel. |
| GB-36 | echt | S. 16, Z. 353 bis 359 und S. 25, Z. 471 bis 472 stützen die Übereinstimmung nur auf zwei markierte Merkmale in Fig7(o) (S. 19), ohne Maße, Zeitschritt oder Bildquelle. |
| GB-37 | echt | Aus Gl. (1), (4) und S. 13, Z. 252 folgt KE + PE + DE = ME(t0) identisch (1000 Zufallsfälle nachgerechnet), Fig8 (S. 20) und alle zehn Panels von Fig9 (S. 21 bis 22) zeigen konstante Summen, und S. 20, Z. 393 bis 394 sowie S. 25 bis 26, Z. 479 bis 482 sprechen den Einzelblöcken die Erhaltung ab. |
| GB-38 | echt | Mit 317563 m³ und 2300 kg/m³ ergeben sich 908 m mittlerer Abstieg gegen 878 m Relief (S. 9, Z. 174 bis 175), höchstens 364,7 GJ kinetische Energie bei 31,6 m/s gegen etwa 1650 bis 1685 GJ in Fig8 (eigene Pixelmessung 1654 GJ bei 13,2 bis 13,6 s) und mit 2400 × 10⁴ m³ nur 12,0 m Abstieg. |
| GB-39 | echt | In Fig9(a) und (c) auf S. 21 steigt PE nach etwa 80 bzw. 90 s ohne sichtbare KE-Schicht, und der Anstieg um 0,368 GJ entspricht 17,4 m Hub bei 939,9 m³, was S. 20, Z. 398 bis 399 als Abprallen deutet. |
| GB-40 | echt | Die Aussagen S. 1, Z. 28 bis 30, S. 22, Z. 418 bis 419 und S. 26, Z. 484 bis 487 stützen sich nur auf Fig10(b) (S. 23), die ungekennzeichnete Punkte gegen Laufweg zeigt; eigener Anteil ab 2200 m 595/1213 = 49 %. |
| GB-41 | echt | Die rote Kurve in Fig10(b) hat keine Legende oder Funktion, und alle Bahnen in Fig10(a) beginnen in einem gemeinsamen Punkt bei Z = 0 und reichen unter -840; die Bildunterschrift S. 23, Z. 423 bis 424 nennt nur "movement trails". |
| GB-42 | echt | Fig12(a) auf S. 25 trägt auf der DE-Kurve etwa 28 bis 30 Marken gegen "10 representative time points" auf S. 23, Z. 427, und das Etikett 1116,8 GJ liegt unter dem Fig8-Maximum (1116,8/1685 = 0,663). |
| GB-43 | echt | Die Beschriftungen in Fig11, Fig3(c) und Fig12 sind am 300-dpi-Bild winzig (Ziffern des Etiketts in Fig12(a) etwa 10 px, rund 2,4 pt Ziffernhöhe), und die Etiketten "29. 47", "319. 5" und "1116. 8" tragen sichtbar ein Leerzeichen nach dem Punkt (S. 25); die einzelnen pt-Werte stammen aus der Messung des Gutachtens. |
| GB-44 | echt | S. 9, Z. 178 bis 182 beschreibt keinen Bruchmechanismus, S. 24, Z. 445 nennt die Fragmentierung eine Deutung, S. 26, Z. 489 bis 492 stellt sie als Schluss dar, und Fig12 reicht bis etwa 1250 % VS und 4300 % AG. |
| GB-45 | echt | Die Wörter "earthquake", "seismic", "accumulation", "warning" und "risk" kommen in S. 25 bis 26, Z. 460 bis 492 nicht vor, und Abschnitt 4 enthält keinen Ausblick. |
| GB-46 | echt | Trajektoriengleichungen und Bezug auf andere Berggebiete stehen nur S. 25, Z. 464 bis 468, nicht in S. 6, Z. 137 bis 141, S. 7, Z. 157 bis 162, Fig1 oder Fig3(c). |
| GB-47 | echt | Beide Erklärungen S. 26, Z. 494 bis 495 und Z. 505 bis 506 lauten "upon reasonable request" ohne Grund, Link oder Anhang. |
| GB-48 | echt | 16 der 31 Einträge (51,6 %) werden nirgends zitiert, alle Zeilenangaben S. 26 bis 29 stimmen, im Text nach Z. 63 steht kein Zitat, Dahal, Nava und Sinčić sind auf S. 27 bis 28 grau und im Flattersatz gesetzt, und die Abstracts von Zhao et al. 2021 und Zhou et al. 2024 bestätigen die genannten Mechanismen; Wu et al. 2013 war online nicht lesbar. |
| KK-01 | echt | "dissipation energy" steht S. 1, Z. 21 und S. 3, Z. 84, "dissipated energy" in Z. 241 bis 242, Fig1 und Fig12. |
| KK-02 | echt | Beide Großschreibungen nach Semikolon stehen S. 1, Z. 27 und Z. 28. |
| KK-03 | echt | "such as donghekou" steht S. 1, Z. 34 (Fortsetzung Z. 35), die Titel S. 28, Z. 572, 579 und 582 schreiben "Donghekou". |
| KK-04 | echt | S. 2, Z. 76 bis S. 3, Z. 77 nennt "three parts", es folgen vier Punkte (1) bis (4) in Z. 77 bis 90, und Fig1 (S. 4) hat vier Zeilen. |
| KK-05 | echt | Die Schreibung steht S. 5, Z. 98. |
| KK-06 | echt | S. 5, Z. 110 zeigt "(Ms7" und "¾)" als getrennte Wörter. |
| KK-07 | echt | Die Legende von Fig2(b) auf S. 6 lautet "Daduhe River". |
| KK-08 | echt | S. 7, Z. 151 setzt "2400×104" als ein Wort in voller Schriftgröße (pdftotext -bbox). |
| KK-09 | echt | "1120 m-1330m is the front edge" steht S. 7, Z. 152. |
| KK-10 | echt | Die drei Großschreibungen stehen S. 7, Z. 153, 154 und 156. |
| KK-11 | echt | Fig3(a) und Fig3(b) auf S. 8 schreiben "Dadu river". |
| KK-12 | echt | "can" steht am Ende von S. 9, Z. 176, "not be obtained" in Z. 177. |
| KK-13 | echt | "1121m high" steht S. 9, Z. 182. |
| KK-14 | echt | Beide Bindestriche statt Satzzeichen stehen S. 11, Z. 218 und Z. 228. |
| KK-15 | echt | Die Legende von Fig5(a) auf S. 12 lautet "Non-obvios acceleration". |
| KK-16 | echt | S. 13, Z. 246 nennt nur PE und DE, obwohl Gl. (2) KE definiert (am Seitenbild bestätigt). |
| KK-17 | echt | "(m/s);h(ti)" steht ohne Leerzeichen S. 13, Z. 251. |
| KK-18 | echt | Die Bildunterschrift S. 20, Z. 390 lautet nur "Fig8. Evolution of energy during the landslide". |
| KK-19 | echt | "after it approaches zero" bezieht sich S. 20, Z. 397 bis 398 auf "some blocks". |
| KK-20 | echt | Die Bildunterschrift S. 22, Z. 410 bis 413 hat Leerzeichen vor jedem Semikolon. |
| KK-21 | echt | Auf 3.2.2 (S. 20) folgt direkt "3.4" auf S. 23, Z. 425, einen Abschnitt 3.3 gibt es nicht. |
| KK-22 | echt | S. 24, Z. 438 bis 439 nennt "(a-i)" für zehn Zeiten, die Abbildung hat zehn Panels (a) bis (j). |
| KK-23 | echt | Beide fehlenden Leerzeichen stehen S. 25, Z. 464 und Z. 466. |
| KK-24 | echt | "The codes that support" steht S. 26, Z. 494. |
| KK-25 | echt | Der Punkt zwischen XF und LZ steht S. 26, Z. 499. |
| KK-26 | echt | Die Überschrift S. 26, Z. 507 lautet "Reference". |
| KK-27 | echt | S. 27, Z. 530 kürzt mit "et al.", und der Cardiff-ORCA-Datensatz nennt die 17 Autoren in der vorgeschlagenen Reihenfolge. |

## 2 Literaturvorschläge: bereits im Literaturverzeichnis?

| Vorschlag | Kennung | Im Verzeichnis |
|---|---|---|
| Jaboyedoff et al. 2019, Earth Surf. Dynam. 7, 439 bis 458 | GB-05, GB-10 | nein |
| Crosta et al. 2014, EGU2014-16272 | GB-05 | nein |
| Lin et al. 2022, Nat. Hazards Earth Syst. Sci. 22, 639 bis 657 | GB-09, GB-10 | nein |
| De Blasio und Crosta 2015, Geophys. Res. Lett. 42, 8463 bis 8470 | GB-10 | nein |
| Feng et al. 2023, Front. Earth Sci. 11, 1140326 | GB-20 | nein |
| He, J. et al. 2023, Landslides 21, 621 bis 640 | GB-12 | ja (S. 27, Z. 546 bis 548) |
| Ge, Tang und Li 2021, Landslides 18, 3559 bis 3576 | GB-09, GB-48 | ja (S. 27, Z. 540 bis 542) |
| Zhao et al. 2021, Nat. Hazards 106, 459 bis 485 | GB-15, GB-48 | ja (S. 29, Z. 600 bis 602) |
| Wu et al. 2013, J. Geol. Soc. India 82, 277 bis 282 | GB-33, GB-48 | ja (S. 28, Z. 588 bis 590) |
| Zhou et al. 2024, J. Earth Sci. 35, 221 bis 234 | GB-33, GB-48 | ja (S. 29, Z. 603 bis 605) |

Nicht gezählt: Cheng und Li 2014 sowie Li et al. 2024 in GB-07 (bereits zitiert, nur Umwidmung), Zhao, Crosta, Utili und De Blasio 2017 sowie De Pedrini et al. 2022 im Prüfprotokoll (ausdrücklich nicht vorgeschlagen).

## 3 Doppelungen

| Paar | Fundort | Gegenstand |
|---|---|---|
| GB-20 und GB-21 | S. 10, Z. 189 bis 191 und Einschub Fig4 | fehlende Angaben zum Luding-Datensatz (Komponente, Skalierung, Filterung), in GB-20 Punkt (3) und GB-21 Punkt (a) |
| GB-24 und GB-35 | S. 12, Fig5(b) bis (f) | nicht benannter Block hinter dem Profil bis etwa 45 m/s, in GB-24 Punkt (b) und GB-35 |

Nur angrenzend, nicht gezählt: GB-11 und GB-22 (Legende Fig4, einmal Namensabweichung, einmal fehlende Auflösung), GB-18 und GB-27 (Querverweis zur unbalancierten Kraft), GB-42 und GB-44 (Querverweis zum Phasenkriterium).

## 4 Fundorte

Geprüft wurde je Kennung, ob die zitierte Stelle in der angegebenen Seite und Zeile liegt (Seitenbild und Randnummern).

| Ergebnis | Anzahl |
|---|---|
| genau | 75 |
| um 1 bis 2 Zeilen daneben | 0 |
| weiter daneben | 0 |

Randbefund ohne Einfluss auf die Zählung: GB-29 nennt "p. 15, l. 287 to 288"; Z. 287 steht auf S. 14, Z. 288 auf S. 15.

## 5 Zählungen

| Urteil | Anzahl |
|---|---|
| echt | 73 |
| teilweise echt | 2 (GB-20, GB-33) |
| falsch | 0 |
| nicht prüfbar | 0 |
| gesamt | 75 (48 GB, 27 KK) |

Literaturvorschläge: 10, davon 5 im Verzeichnis, 5 nicht. Doppelungen: 2. Fundorte: 75 genau, 0 um 1 bis 2 Zeilen, 0 weiter daneben.

Nicht an der Quelle prüfbare Teilaussagen (ohne Einfluss auf das Gesamturteil der Kennung): Inhalt von Cheng und Li 2014 (GB-07), Inhalt von Wu et al. 2013 (GB-48), Kartenmessungen in Fig2(c) (GB-15), einzelne pt-Werte (GB-43).
