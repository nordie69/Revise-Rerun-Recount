# Verifikation des Gutachtens zu egusphere-2025-4506

Grundlage: egusphere-2025-4506.pdf (Text über pdftotext mit gedruckten Randnummern, eingebettete Abbildungen in Originalauflösung über pdfimages, Seiten 2, 5, 26 bis 29 neu gerendert), Seitenbild seite-13.png, Zahlen mit Python (vf/skripte/rechnen.py), Zitate automatisch gegen den Volltext (vf/skripte/zitate.py, zitate2.py), Literatur über WebSearch und WebFetch.

## 1. Urteile je Kennung

| Kennung | Urteil | Beleg (ein Satz mit Seite und Zeile) |
|---|---|---|
| GB-01 | echt | Zitat steht p. 1, l. 33 bis 34; das Abstract von Carpignano et al. (2009, IDEAS/RePEc) behandelt Multi-Risk-Karten für das Piemont und nennt weder Erdbeben, Hangrutschketten noch einen Häufigkeitstrend. |
| GB-02 | echt | Beide Zitate stehen p. 2, l. 42 und l. 49 bis 51, keine Datenbank oder Suche wird genannt (0 Treffer, "search" nur in "research"), und De Pedrini et al. (2022, Geogr. Helv. 77, 21 bis 37) rekonstruieren eine Prä-Ereignis-Oberfläche mit Höhenlinien und RAMMS::DEBRISFLOW und stehen nicht im Verzeichnis. |
| GB-03 | echt | Zitat p. 2, l. 43 bis 46; die Einträge Song et al. 2017 (p. 28, l. 569 bis 571) und Wu, H. et al. 2024 (p. 28, l. 585 bis 587) tragen "Numerical Simulation" im Titel, Fan et al. 2020 hat keinen Eintrag, Zhang et al. 2024 nur Zhang, J. 2023 (p. 29, l. 594 bis 596). |
| GB-04 | echt | Zitat p. 2, l. 46 bis 49; Li et al. 2024 (DOAJ-Abstract) behandeln eine regenausgelöste Reaktivierung mit Sicker- und Stabilitätsrechnung ohne Geländerekonstruktion, Du et al. 2021 (Abstract) nennen weder 2-D noch 3-D. |
| GB-05 | echt | Zitat p. 2, l. 61 bis 63, keiner der fünf Titel im Verzeichnis; van Herwijnen und Schweizer (2011, CRST 69, 165 bis 176) überwachen Schneelawinen bei Davos mit einem Geophon und zitieren Navarre et al. 2009 mit dem genannten Lawinentitel. |
| GB-06 | echt | Zitate p. 2, l. 63 bis 64 und p. 26, l. 485 bis 487; Ge et al. 2021 steht p. 27, l. 540 bis 542 und wird im Text nie zitiert (sechs In-Text-Zitate mit 2021), Lin et al. 2022 und Daudon et al. 2015 bestätigen die beschriebenen Inhalte an der Verlagsseite. |
| GB-07 | echt | P. 2, l. 76 bis p. 3, l. 77 nennt "three parts", l. 77 bis 90 zählen (1) bis (4) auf, Fig1 zeigt vier Kästen mit den genannten abweichenden Namen, Überschriften l. 92, 214, 240, 269. |
| GB-08 | teilweise echt | Die Werte unter 6 pt bestätigen sich für Fig5, Fig7, Fig11 (Ziffernhöhe 7 bis 8 px bei 272 ppi, rund 2,8 pt), nicht aber für Fig1 p. 4: "Input Seismic Force" hat 30 px Versalhöhe bei 426 ppi, also rund 7 pt und mehr als "Travel distance" (rund 6,3 pt). |
| GB-09 | echt | Koordinaten p. 5, l. 95 bis 96; in Fig2 (a) p. 6 liegt der Punkt bei etwa 101,1 Grad Ost und 29,56 Grad Nord, in Fig2 (b) sitzt der Stern auf 102°09'E und 29°37'N, Abstand 949 m Nord und 1106 m Ost (Python). |
| GB-10 | echt | Text p. 5, l. 101 bis 105 nennt γO2 (Großbuchstabe am Seitenbild), O2 und T3bg, die neun Legendeneinträge von Fig2 (c) p. 6 enthalten weder Quarzdiorit noch T3bg, Fig3 (a) p. 8 hat keine Symbole und Diorit #897870 gegen Sand und Kies #8a765b. |
| GB-11 | echt | Nach p. 2, l. 63 steht kein Autor-Jahr-Zitat mehr (0 Treffer), die Aussagen p. 5, l. 110 bis 112, p. 10, l. 187 bis 189 und p. 15, l. 311 bis 312 sind unbelegt, Zhao et al. 2021 nennen "over 100 000 deaths" und Zhou et al. 2024 die drei Mechanismen im Abstract. |
| GB-12 | echt | Suchen über den ganzen Text: "damp", "time step", "rigid", "deformab", "resolution" 0 Treffer, "version" nur in "inversion" (p. 11, l. 207) und "conversion", "accuracy" 1 Treffer (p. 14, l. 282). |
| GB-13 | echt | Die Restaurierung p. 6, l. 138 bis p. 7, l. 143 und l. 157 bis 162 gibt keine Regel und keine Prüfung außer dem Bildvergleich in Fig3 (c) p. 9. |
| GB-14 | echt | P. 7, l. 145 bis 146 nennt vier Bereiche, Fig3 (a) p. 8 zeigt nur I "Sliding bed" und II "Accumulation area" mit einer Trennlinie. |
| GB-15 | echt | P. 7, l. 149 bis 150 gibt 450 m und 0,45 km², p. 9, l. 174 1021 m; die Profilwerte p. 7, l. 151 bis 156 ergeben 914,0 bis 1250,2 m und sqrt(1021² minus 747²) = 696 m (Python), die Grenze in Fig2 (c) misst grob 1190 m längs a-a'. |
| GB-16 | echt | P. 7, l. 150 bis 151 und p. 9, l. 181 bis 182: 0,45 km² mal 100 m = 4,5 x 10^7 m³, 317563 m³ sind 1,3 % von 2,4 x 10^7 m³, Fallhöhe 910 m, Effektivgeschwindigkeit 67,4 m/s und KE-Obergrenze 364,7 GJ (Python) gegen den KE-Gipfel von rund 1670 GJ in Fig8 p. 20. |
| GB-17 | echt | Gegen p. 7, l. 151 bis 156 zeigt Fig3 (b) p. 8 den Wasserspiegel bei rund 1146 m und für 1120 bis 1330 m etwa 22 bis 27 Grad statt 50 Grad; die übrigen Winkel weichen in meiner Ablesung um wenige Grad von den Gutachtenwerten ab. |
| GB-18 | echt | P. 7, l. 160 nennt a-a' und b-b', Fig2 (c) p. 6 zeigt nur die Linie a bis a' (Strich am Seitenbild vergrößert bestätigt), Fig3 (c) p. 9 zeigt Höhenlinien und Schummerung, keine Schnitte. |
| GB-19 | echt | Fig3 (b) p. 8 hat Zahlen ohne Achsentitel und ein unerklärtes "80°", Fig3 (a) einen Maßstab "0 400 1000m" auf einem Schrägblock, die unteren Felder von Fig3 (c) p. 9 haben weder Maßstab noch Nordpfeil. |
| GB-20 | echt | P. 9, l. 177 bis 178 "has to be ignored" steht neben "A uniform structural plane is set inside" (l. 179 bis 180), p. 11, l. 209 bis 210 und Table 1 nennen Trennflächensätze, p. 15, l. 308 bis 310, l. 323 und p. 25, l. 469 erklären mit Strukturflächen. |
| GB-21 | echt | P. 10, l. 189 bis 191 ein Ersatzbeben, keine Vergleichsrechnung; "amplif" nur p. 15, l. 311 und l. 316, "peak ground" nur l. 317, "PGA", "gravity", "sensitiv" 0 Treffer. |
| GB-22 | echt | P. 10, l. 189 bis 191 nennt nur "Luding station", die Bildunterschrift p. 6, l. 126 bis 127 und die Felder von Fig2 haben keine Quelle, die Datenerklärung p. 26, l. 505 bis 506 verweist nur auf Anfrage. |
| GB-23 | echt | Im Einsatz von Fig4 p. 10 hat die Zeitachse nur Striche, tp, tPGA, tf, te sind nirgends erklärt, die Achse reicht bis etwa +151 und -176 gal, die Spur bis etwa +219 und -225 gal (Pixelmessung). |
| GB-24 | echt | P. 11, l. 206 bis 207 nennt drei Quellen ohne Zuordnung, Table 1 p. 11 gibt Normalsteifigkeit 960 und 100 GPa/m gegen Schersteifigkeit 1500 und 180 GPa/m sowie Kohäsion 0,8 und 1,1 MPa. |
| GB-25 | echt | Table 1 p. 11 hat "bed rock" und "landslide mass", Fig4 p. 10 vier Legendenfarben (γo2, Q del, γM2, Sliding mass), p. 11, l. 208 bis 210 Verwitterungszonen und Trennflächen, eine Zuordnung fehlt. |
| GB-26 | echt | P. 11, l. 226 bis 234 definiert den Schwellenwert als "prominence threshold" ohne Bezugsgröße und nennt 30 % "deemed acceptable", eine Prüfung gegen Kontaktdaten fehlt. |
| GB-27 | echt | In Fig5 (a) p. 12 liegt der rote Marker bei etwa 243 m (13,05 m/s) vor dem höheren Punkt bei 262 m (13,4 m/s) und der rote Marker bei etwa 463 m (4,2 m/s) vor weiter steigenden Punkten. |
| GB-28 | echt | Fig5 (b) bis (f) p. 12 tragen "Travel Displacement (m)", Fig5 (a) und Fig10 (b) "Travel distance (m)", p. 1, l. 23 und p. 25, l. 474 "displacement". |
| GB-29 | echt | Fig5 (b) bis (f) p. 12 erreichen rund 45 m/s bei etwa 250 m gegen 31,6 m/s in p. 16, l. 330, "1,139" steht nur p. 11, l. 233, und die Summe der 26 Punkte von Fig10 (b) ist 1212,8 (Python). |
| GB-30 | echt | Fig5 (b) bis (f) p. 12 haben weder Legende noch Erklärung für rote Marker, grauen Kasten und Einsatz ohne Achsentitel, in (a) fehlen die schwarzen Punkte in der Legende und Punkte bei etwa 590 m liegen unter 0 m/s. |
| GB-31 | echt | P. 13, l. 253 bis 255 nennt die Anfangshöhe als Bezug, Fig9 p. 21 bis 22 zeigt PE von Maximum auf 0 fallend, die impliziten Höhen 233, 223, 232, 163, 317, 172, 30, 193, 82, 43 m stehen gegen z = 340 bis 755 m, Rangkorrelation -0,65 (Python). |
| GB-32 | echt | "unbalanced" nur p. 13, l. 258 und Table 2, "stress" in l. 297 bis 459 nur l. 302, 312, 369, und Fig9 (a) und (c) p. 21 zeigen nach 100 s noch steigende PE. |
| GB-33 | echt | "field" außerhalb Literatur und Randbedingungen nur p. 2, l. 65, p. 13, l. 266, p. 16, l. 354, p. 25, l. 471 und 472 bis 473, ohne Beschreibung; 15 + 1 + 10 + 2 + 10 + 2 = 40 Ergebnisfelder, nur Fig7 (o) mit Fotos. |
| GB-34 | echt | Fig6 p. 14 zeigt von oben 2, 3, 3, 2 Kugeln mit den Beschriftungen "Top", "Lower middle part", "Upper middle part", "Bottom", ohne Nummern, mit gelber, oranger und rosa Kugel, die in der Legende von Fig10 (a) p. 23 fehlen. |
| GB-35 | echt | P. 14, l. 272 bis 284 nennt weder Punktmenge noch Einheit von α noch Software, V0 und S0 (l. 278 bis 279) werden nicht beziffert, Fig12 p. 25 beginnt bei VS = 0. |
| GB-36 | echt | "volume expansion" steht p. 1, l. 25, p. 3, l. 89, p. 24, l. 441, p. 25, l. 453, p. 26, l. 488, "surface area growth" viermal, und p. 24, l. 440 schreibt "surface area (A)" gegen S in Gl. (6) p. 14, l. 277. |
| GB-37 | echt | Abschnitt 3.1 p. 15 bis 16 nennt sechs Phasen ohne Zeiten, p. 19, l. 381 nennt 3 bis 12 s, und der KE-Gipfel in Fig8 p. 20 liegt bei etwa 13,5 s mit rund 1670 GJ (Pixelmessung). |
| GB-38 | echt | P. 16, l. 353 "compelling evidence" und p. 25, l. 471 bis 472 "ensures", während Fig7 (o) p. 19 nur zwei gestrichelte Kästen ohne Messgröße zeigt. |
| GB-39 | echt | Fig7 (h) p. 18 ist einheitlich rot mit Farbskala "0" bis "0Mpa", (i) zeigt bereits 0 bis -33 MPa, und 2700 x 9,81 x 1250 Pa = 33,1 MPa (Python) bei statischem Gleichgewicht nach p. 10, l. 199 bis 201. |
| GB-40 | echt | Fig7 (h) bis (n) p. 18 haben Achsenzahlen ohne Titel und Farbskalen bis 0, -33, -31, -33, -33, -33, -47 MPa, Fig7 (o) p. 19 hat weder Maßstab noch Zeit noch Blickrichtung. |
| GB-41 | echt | Aus Gl. (1) p. 12, l. 245 und Gl. (4) p. 13, l. 249 folgt KE + PE + DE = ME(t0) identisch (10.000 Zufallszustände, maximale Abweichung 1,7 x 10^-13, Python), und Fig8 und alle Felder von Fig9 zeigen konstante Balkenhöhen. |
| GB-42 | echt | P. 1, l. 28 bis 30 und p. 26, l. 483 bis 487 haben in Abschnitt 3 keine Zählung je Block oder Lage, Fig10 (b) p. 23 hat 26 Distanzklassen mit fünf Rückgängen und Summe 1212,8, davon 49,1 % ab 2200 m (Python). |
| GB-43 | echt | Alle zehn Bahnen in Fig10 (a) p. 23 beginnen in einem Punkt, die Z-Achse reicht bis unter -840, Bahn 5 endet darunter, während die Fig9-Summen Fallhöhen von rund 223 bis 317 m für die Blöcke 1, 2 und 5 ergeben. |
| GB-44 | echt | Die Bildunterschrift p. 24, l. 437 bis 439 erklärt hellgrüne Hülle und dunkelgrünen Einsatz nicht, und Fig11 (a) p. 23 reicht in Z von -300 bis 300, Fig11 (i) p. 24 von -600 bis 400 und in X bis 1500. |
| GB-45 | echt | P. 24, l. 448 bis 450 und p. 26, l. 490 bis 492 erklären die Hüllenvergrößerung mit Fragmenten im Inneren, in Abschnitt 2 stehen "fragment" nur l. 285 und 294, "break" nur l. 118 und 137, "fractur" nicht, und Fig12 p. 25 endet bei rund 1245 % VS und 4250 % AG. |
| GB-46 | echt | Fig12 (a) und (b) p. 25 haben je rund 30 Punkte gegen die 10 Zeitpunkte von p. 23, l. 427, und der markierte KE-Gipfel 1116,8 GJ liegt 540 GJ (33 %) unter dem Gipfel von Fig8 p. 20. |
| GB-47 | echt | In p. 25, l. 460 bis p. 26, l. 492 haben "earthquake", "seismic", "warning", "risk", "hazard", "accumulat", "Mogangling" und die übrigen Suchwörter je 0 Treffer, eine Discussion fehlt. |
| GB-48 | echt | "equation" nur p. 13, l. 263 und p. 25, l. 465, "stratigraphic" nur l. 468, während die Methode p. 6, l. 139 bis 140 die Höhenlinien nur gerade zieht. |
| GB-49 | echt | Beide Erklärungen p. 26, l. 494 bis 495 und l. 505 bis 506 verweisen ohne Grund auf Anfrage beim Erstautor. |
| GB-50 | echt | Die Einleitung p. 1, l. 34 bis p. 2, l. 63 zitiert 29 Werke (10 mit Eintrag gleichen Jahres, 3 Jahreskonflikte, 2 Fan-2019, 14 ohne Eintrag), von 31 Einträgen p. 26, l. 508 bis p. 29, l. 605 sind 16 unzitiert. |
| KK-01 | echt | "dissipation energy" steht p. 1, l. 21 und p. 3, l. 84, "dissipated energy" p. 12, l. 242 und l. 287, 387, 399, 442, 478, 481, 486. |
| KK-02 | echt | Fünf Schreibweisen p. 1, l. 23 "Alpha shape", p. 3, l. 88 bis 89 "alpha shape", p. 14, l. 272 "alpha-shape", l. 281 und p. 23, l. 426 "Alpha Shape". |
| KK-03 | echt | P. 1, l. 24 nennt "3D point cloud data", p. 23, l. 426 "numerical simulation data". |
| KK-04 | echt | Großschreibung nach Semikolon p. 1, l. 27 und 28 sowie p. 7, l. 153, 154 und 156. |
| KK-05 | echt | P. 1, l. 34 "such as donghekou". |
| KK-06 | echt | "Fan et al., 2019a" p. 1, l. 34 und "Fan et al., 2019" p. 2, l. 56 bis 57 gegen zwei Einträge ohne Suffix p. 27, l. 530 und 533, "Wang, 2021" p. 1, l. 36 gegen sieben Autoren p. 28, l. 581, Tian 2017 gegen 2016 p. 28, l. 577. |
| KK-07 | echt | P. 2, l. 42 bis 43 "For landslides that have not occurred too far away". |
| KK-08 | echt | P. 2, l. 44 "UAV impact" und p. 6, l. 130 bis 131 ohne Auflösung von DEM und UAV, DEM nur in Fig1 ausgeschrieben. |
| KK-09 | echt | P. 2, l. 46 "Song at al.2017" und "Zhang et al., 2024" gegen Zhang, J. 2023 p. 29, l. 594 bis 596. |
| KK-10 | echt | "Cheng 2014" p. 2, l. 48 bis 49 und Eintrag "Cheng, F., and Yu-Sheng, L.:" p. 27, l. 521. |
| KK-11 | echt | "Zhao et al., 2020" p. 2, l. 57 gegen Eintrag 2021 p. 29, l. 600 bis 602. |
| KK-12 | echt | "altitude" in "high-altitude" p. 2, l. 73 hat bei 200 dpi den dunkelsten Wert 39 gegen 0 im Wortteil "high". |
| KK-13 | echt | Fig1 p. 4, Feld "Global Perspective", zeigt "P0E", "PtE", "KtE". |
| KK-14 | echt | Der Text "Extraction of volume and area of landslide accumulation area" in Fig1 p. 4 reicht bis an den Kastenrand. |
| KK-15 | echt | Fig2 (b) p. 6 "Daduhe River", Fig3 (a) und (b) p. 8 "Dadu river", Text 11 Zeilen "Dadu River" auf p. 5 bis 16. |
| KK-16 | echt | P. 9, l. 182 "1121m high". |
| KK-17 | echt | Legende Fig5 (a) p. 12 "Non-obvios acceleration". |
| KK-18 | echt | P. 13, l. 246 nennt PE(ti) und DE(ti), nicht KE(ti), Gl. (2) folgt in l. 247 (Seitenbild). |
| KK-19 | echt | P. 13, l. 251 "(m/s);h(ti)". |
| KK-20 | echt | Titel von Table 2 p. 13 nennt Blöcke, Zeile ID 11 ist "Maximum unbalanced force". |
| KK-21 | echt | "cloud maps" p. 15, l. 301 und "cloud map" p. 19, l. 368 und 369. |
| KK-22 | echt | Farbskalen Fig7 (h) bis (n) p. 18 tragen "Mpa". |
| KK-23 | echt | P. 20, l. 397 bis 398 "after it approaches zero" mit Bezug auf zwei Blöcke. |
| KK-24 | echt | Bildunterschrift p. 22, l. 410 bis 413 hat acht Mal "point n ;". |
| KK-25 | echt | Überschriften 3.1 (p. 15, l. 298), 3.2, 3.2.1, 3.2.2, dann 3.4 (p. 23, l. 425), keine 3.3. |
| KK-26 | echt | P. 24, l. 438 bis 439 "(a-i)" bei zehn Zeiten und zehn Feldern. |
| KK-27 | echt | P. 25, l. 458 bis 459 "as a function of volume", Achsentitel "Volume Swelling (%)" und "Area Growth (%)". |
| KK-28 | echt | P. 25, l. 464 "that:(a) Outside" und l. 466 "contours;(b) The". |
| KK-29 | echt | P. 26, l. 499 "XF: Data curation, Investigation. LZ:". |
| KK-30 | echt | P. 26, l. 507 "Reference". |
| KK-31 | echt | Bei 200 dpi haben Bernardie, Dahal, Nava, Sinčić und Zhang, K. (p. 26 bis 29) den dunkelsten Wert 34, alle anderen Einträge 0. |
| KK-32 | echt | P. 27, l. 530 "Fan, X., Scaringi, G., Korup, O., et al.:" als einziger Eintrag mit "et al.". |

## 2. Literaturvorschläge: bereits im Verzeichnis?

| Vorschlag (Kennung) | Im Verzeichnis |
|---|---|
| De Pedrini et al. 2022 (GB-02) | nein |
| Ge, Tang und Li 2021 (GB-06, GB-47) | ja, p. 27, l. 540 bis 542 |
| Hibert et al. 2017 (GB-06) | nein |
| Lin et al. 2022 (GB-06) | nein |
| Daudon et al. 2015 (GB-06) | nein |
| Zhou et al. 2024 (GB-11) | ja, p. 29, l. 603 bis 605 |
| Wu, J. et al. 2013 (GB-11, GB-47) | ja, p. 28, l. 588 bis 590 |
| Zhao et al. 2021 (GB-47) | ja, p. 29, l. 600 bis 602 |

## 3. Doppelungen (gleicher Fundort, gleicher Gegenstand)

| Paar | Fundort | Gegenstand |
|---|---|---|
| GB-29 / GB-42 | p. 11, l. 233 und Fig10 (b) p. 23 | Summe 1212,8 der Fig10 (b) gegen 1,139 |
| GB-12 / GB-22 | p. 10, l. 189 bis 191 und Einsatz Fig4 | Komponente und Skalierung des Luding-Records |
| GB-10 / GB-23 | Legende Fig4 p. 10 | Symbole γo2, Q del, γM2 |
| KK-06 / GB-50 | p. 27, l. 530 bis 536; p. 28, l. 577 | Fan-2019-Suffixe und Jahr Tian |
| KK-09 / GB-50 | p. 2, l. 45 bis 46; p. 29, l. 594 bis 596 | Jahreskonflikt Zhang 2024 gegen 2023 |
| KK-11 / GB-50 | p. 2, l. 57; p. 29, l. 600 bis 602 | Jahreskonflikt Zhao 2020 gegen 2021 |

## 4. Fundorte

Geprüft wurde der Fundort jeder der 82 Kennungen gegen die gedruckten Randnummern (für Gleichungs- und Tabellenseiten am Seitenbild p. 13 bestätigt).

| Klasse | Anzahl |
|---|---|
| genau | 82 |
| um 1 bis 2 Zeilen daneben | 0 |
| weiter daneben | 0 |

## Zählungen

| Urteil | Anzahl |
|---|---|
| echt | 81 |
| teilweise echt | 1 |
| falsch | 0 |
| nicht prüfbar | 0 |
| Summe | 82 |

Literaturvorschläge: 8, davon 4 bereits im Verzeichnis, 4 nicht. Doppelungen: 6 Paare. Fundorte: 82 genau, 0 um 1 bis 2 Zeilen, 0 weiter daneben.
