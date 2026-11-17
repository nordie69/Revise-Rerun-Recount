# Verifikation des Gutachtens zu egusphere-2025-4506

Grundlage: Seitenbilder (150 dpi, eigene Renderings mit 300 und 600 dpi), Textschicht text.json, Zeilennummern an den gedruckten Randnummern bestätigt (S. 1, 2, 6, 9 bis 14, 18 bis 26). Rechnungen in vf/rechnung.py.

## 1. Urteile je Kennung

| Kennung | Urteil | Beleg (ein Satz mit Seite und Zeile) |
|---|---|---|
| GB-01 | echt | Zitat S. 1, Z. 33 bis 34 wörtlich, "involving terrain restoration" und "inputting external stress" S. 2, Z. 47 bis 48 wörtlich; Carpignano et al. 2009 behandelt laut Abstract Multi-Risk-Karten für das Piemont ohne Erdbeben oder Hangrutschungen, Li et al. 2024 laut Abstract den regenausgelösten Zhongbao-Hang mit Sicker- und Standsicherheitsrechnung, Wu et al. 2024 ist laut Titel (S. 28, Z. 585 bis 587) eine Wellensimulation; nicht nachlesbar waren die Einzelheiten GPS (Song 2017) und GeoStudio (Li 2024). |
| GB-02 | teilweise echt | Zitat S. 2, Z. 49 bis 51 und Lückenbehauptung Z. 63 bis 64 wörtlich, Guimpier et al. 2021 enthält "the overall topography outside the landslide" wörtlich, Ge et al. 2021, Wu 2013 und Zhou 2024 sind gelistet und nie zitiert; nicht zutreffend ist, dass Zhao et al. 2021 nicht zitiert werde, denn S. 2, Z. 57 zitiert "Zhao et al., 2020", was GB-30 selbst als Jahresabweichung zu diesem Eintrag (S. 29, Z. 600 bis 602) wertet. |
| GB-03 | echt | Zitat S. 2, Z. 67 bis 68 wörtlich, "early warning and risk mitigation" Z. 72 und "for the potential landslide in the high-intensity area of the Dadu River" S. 5, Z. 124 wörtlich; "accumulation" kommt sonst nur als Ablagerungsbegriff vor, keine Analyse der Energieakkumulation. |
| GB-04 | echt | Koordinaten S. 5, Z. 95 bis 96 wörtlich; am 300-dpi-Bild von S. 6 liegt der Punkt bei x 821,5 px zwischen den Beschriftungen 100°E (736,5) und 102°E (888,5), also bei 101,1 bis 101,2°E, und der Maßstab misst 146 px für 160 km (0,91 px/km) gegen 154 px für 2° Breite (0,69 px/km). |
| GB-05 | echt | S. 5, Z. 103 bis 105 nennen T3bg, Q4del "landslide accumulation" und "colluvial Deluvial deposit", die Legende Fig. 2c (S. 6) dagegen "Rubble soil", "Massive gravel", "Hybrid granite" ohne T3bg und Diorit, Fig. 3a "Massive gravelly soils", Fig. 3b zusätzlich "Massive gravel" und durchgehend "Diorite" (S. 8). |
| GB-06 | echt | Werte S. 7, Z. 149 bis 156 und S. 9, Z. 174 und 181 bis 182 wörtlich; mit Python nachgerechnet: 1,875; 75,6; 0,71 m; 10,0 bis 23,2 m; 914 bis 1250 m; Mittel 1151,3 m3 mal 25345 gleich 2,92 × 10^7 m3. |
| GB-07 | echt | Zitat S. 7, Z. 159 bis 160 wörtlich; Fig. 2c (S. 6) zeigt nur die Linie a, Fig. 3b (S. 8) trägt "(a-a')", Fig. 3c (S. 9) zeigt Höhenlinienkarten und Oberflächen, keine Profile. |
| GB-08 | teilweise echt | Zitat S. 7, Z. 151 bis 152 wörtlich und Achsen ohne Größe und Einheit (S. 8) zutreffend; nicht reproduzierbar ist der Wert 1172 m, denn am 300-dpi-Bild liegen die Achsenmarken 1000 bei 2392 px und 2000 bei etwa 1852 px, die Wasseroberfläche bei 2312 px, also etwa 1146 m und rund 31 m statt 57 m über dem Fluss. |
| GB-09 | echt | Zitat S. 10, Z. 189 bis 191 und "Extensive research indicates ..." Z. 187 bis 189 ohne Beleg wörtlich; Einschub Fig. 4 (S. 10) ohne Zeitwerte, tp, tPGA, tf, te unerklärt, vier Materialien in der Legende, Achsen positiv; Tabelle 1 (S. 11) zwei Gesteinssätze und Scherstiffness 1500 über Normalsteifigkeit 960 GPa/m; Tabelle 2 (S. 13) x von minus 719 bis minus 68, y von minus 557 bis 286. |
| GB-10 | teilweise echt | Zitat S. 11, Z. 221 wörtlich, "displacement velocity curve" S. 1, Z. 23, "travel-distance versus velocity profile" Z. 234, Achsen "Travel distance (m)" in Fig. 5a und 10b gegen "Travel Displacement (m)" in Fig. 5b bis 5f, "Daduhe River" in Fig. 2b; nicht zutreffend ist "surface area growth rate" für S. 1, Z. 25 (dort steht "area growth rate"), und "dissipated energy" steht in Z. 242, nicht 241. |
| GB-11 | echt | Zitat S. 11, Z. 232 bis 233 wörtlich, α = 1 und "This approach ensures a tight fit of the envelope model" S. 14, Z. 283 wörtlich, Parameterherkunft S. 11, Z. 207; im Manuskript keine Sensitivitätsrechnung. |
| GB-12 | echt | Zitat S. 11, Z. 233 bis 234 wörtlich ohne Angabe der Blockbasis; in Fig. 5d (S. 12) zählt die Pixelauswertung je nach Schwelle 61 bis 110 rote Marken, weit unter 1139, und die 24 erkannten Punkte in Fig. 10b (S. 23) summieren sich auf 1215,1. |
| GB-13 | echt | Zitate S. 16, Z. 330 und 337 wörtlich; in Fig. 5d (S. 12, 300 dpi) Marken 50 bei 1301,5 px und 0 bei 1780,5 px, oberster Kurvenpunkt 1345 px, also 45,5 m/s bei etwa 250 m. |
| GB-14 | echt | Zitat S. 19, Z. 375 bis 377 wörtlich, Gl. 4 auf S. 13, Z. 249 am Seitenbild als DE(ti) = ME(t0) − ME(ti) bestätigt; Fig. 8 (S. 20) und Fig. 9a bis 9j (S. 21 bis 22) mit flachen Summen (Fig. 8 gemessen etwa 6520 GJ, Panels visuell 5,06 bis 0,95 GJ), Zitate Z. 388 bis 389 und S. 20, Z. 393 bis 394 wörtlich. |
| GB-15 | echt | Zitat S. 13, Z. 253 bis 254 wörtlich; PE beginnt in Fig. 9 (S. 21 bis 22) auf Höhe der Summe und fällt gegen 0; Fallhöhen 238,7 bis 43,4 m und Bezugshöhen 101,3 bis 711,6 m mit Python bestätigt; Zitat S. 20, Z. 397 bis 398 wörtlich. |
| GB-16 | echt | Zitat S. 13, Z. 258 bis 259 wörtlich, Z. 262 bis 263 nennt Spannungsverläufe der zehn Blöcke, Tabelle 2 listet Stress-XX bis ZZ und ID 11; Abschnitt 3 enthält weder Blockspannungsverläufe noch eine Unwuchtkraftkurve. |
| GB-17 | echt | In Fig. 6 (S. 14, vergrößert) liegen 2, 3, 3 und 2 Punkte in den Zonen, die Zone neben "Top" heißt "Lower middle part", die neben "Bottom" "Upper middle part", Punkte ohne Nummern. |
| GB-18 | echt | Zitat S. 15, Z. 308 bis 309 und die Wendungen in Z. 310 bis 318 und 323 wörtlich, Ausschluss der Strukturflächen S. 9, Z. 176 bis 178 und einheitliche Fläche Z. 179 bis 180; Zhou et al. 2024 nennt laut Abstract Beschleunigungsverstärkung, Back-slope- und Grenzflächen-Spannungseffekte für Mogangling. |
| GB-19 | echt | Zitat S. 16, Z. 353 wörtlich, Fig. 7o (S. 19) zeigt zwei Fotos ohne Datum oder Quelle, "ensures that the simulation outcomes align with actual conditions" S. 25, Z. 471 bis 472 wörtlich, Feldbefunde S. 13, Z. 265 bis 266 nicht berichtet. |
| GB-20 | echt | Zitat S. 15, Z. 301 bis 302 wörtlich; Fig. 7h (S. 18) einheitlich rot mit Farbskala "0" bis "0Mpa", Fig. 7i bis "-33Mpa", Achsen 0 bis 2700 und 0 bis 1200 ohne Größe; 2700 × 9,81 × 1250 = 33,1 MPa. |
| GB-21 | echt | Fig. 8 (S. 20, 300 dpi) Summe etwa 6520 GJ, KE 1570 GJ bei 12,4 s und 1657 GJ bei 13,6 s, Fig. 12 (S. 25) beschriftet "1116.8"; alle Massen, Fallhöhen und Grenzen (907 m, 365 GJ, 12 m, 43,5 GJ, 3,78 MJ/m3, 1201 GJ, 3,3 × 10^9 kg) mit Python bestätigt. |
| GB-22 | echt | Ziffernhöhe am 600-dpi-Bild: Fig. 9a Zeitachse 30 bis 32 px, also 5,0 bis 5,3 pt, Fig. 11a Achsenziffern 13 bis 16 px, also 2,2 bis 2,7 pt (S. 21, S. 23). |
| GB-23 | echt | Zitat S. 22, Z. 414 bis 415 wörtlich, Ankündigung S. 3, Z. 86 bis 87, Abstract S. 1, Z. 29 bis 30 und Schluss 4 S. 26, Z. 484 bis 485 wörtlich; Fig. 10b trägt nur Häufigkeit gegen Laufweg, keine Zählung je Block oder Teil. |
| GB-24 | echt | Zitat S. 22, Z. 418 bis 419 wörtlich; gemessen in Fig. 10b (S. 23): 700 m 16,0, 800 m 7,0, 900 m 27,1, 1000 m 20,0, 2300 m 157, 2400 m 150, 2500 m 146, also nicht stetig steigend. |
| GB-25 | echt | Zitat S. 23, Z. 426 bis 427 wörtlich; in Fig. 12a (S. 25, 600 dpi) rund 22 DE-Marker oberhalb VS 200 % und rund 11 darunter, Fig. 11 hat 10 Panels. |
| GB-26 | echt | Zitat S. 24, Z. 448 bis 450 und Schluss 5 S. 26, Z. 488 bis 492 wörtlich; die Methode S. 9, Z. 178 bis 180 nennt 8,7-m-Blöcke und eine einheitliche Strukturfläche, ein Bruchkriterium fehlt. |
| GB-27 | echt | Zitat S. 25, Z. 454 wörtlich; einzige Grundlage ist das KE-Maximum bei 29,47 % und 319,5 % (Z. 453 bis 455), kein Fluidisierungsmaß. |
| GB-28 | echt | Zitat S. 25, Z. 467 bis 468 wörtlich, die Methode S. 6, Z. 140 ("modified to be straight") und S. 7, Z. 157 bis 158 nutzt keine anderen Gebirgsteile derselben Einheit. |
| GB-29 | echt | Zitat S. 26, Z. 505 bis 506 und Codehinweis Z. 494 bis 495 wörtlich, die Luding-Aufzeichnung S. 10, Z. 190 ohne Quelle. |
| GB-30 | echt | Zitat S. 2, Z. 62 bis 63 wörtlich; Abgleich der Zitate Z. 34 bis 63 mit den 31 Einträgen S. 26, Z. 508 bis S. 29, Z. 605 bestätigt 14 Zitate ohne Eintrag, 3 Jahresabweichungen, die Formfehler und 16 nie zitierte Einträge. |
| KK-01 | echt | "610041 ,China" steht wörtlich, aber laut Randnummern auf S. 1 in Z. 13, nicht Z. 21. |
| KK-02 | echt | "donghekou" klein geschrieben S. 1, Z. 34. |
| KK-03 | echt | "UAV impact" S. 2, Z. 44. |
| KK-04 | echt | "three parts" S. 3, Z. 77 bei vier aufgezählten Teilen (1) bis (4) in Z. 77 bis 90. |
| KK-05 | echt | "As shown in Fig1., the research method" S. 2, Z. 76. |
| KK-06 | echt | "burst the Dadu River after 9 days" S. 5, Z. 110 bis 111 wörtlich. |
| KK-07 | echt | Satz S. 10, Z. 193 bis 195 wörtlich und grammatisch unvollständig. |
| KK-08 | echt | "velocities-hereafter termed" S. 11, Z. 218. |
| KK-09 | echt | "must be chosen-one that quantifies" S. 11, Z. 228. |
| KK-10 | echt | Legende Fig. 5a "Non-obvios acceleration" am Seitenbild S. 12. |
| KK-11 | echt | S. 13, Z. 246 nennt nur "PE(ti), and DE(ti)", KE fehlt (Seitenbild). |
| KK-12 | echt | "(m/s);h(ti)" ohne Leerzeichen S. 13, Z. 251. |
| KK-13 | echt | Überschrift "3.4 Structural evolution ..." S. 23, Z. 425, ein Abschnitt 3.3 fehlt. |
| KK-14 | echt | Bildunterschrift S. 24, Z. 438 nennt "(a-i)" für die 10 Panels (a) bis (j). |
| KK-15 | echt | "noted that:(a)" S. 25, Z. 464 und "contours;(b)" Z. 466. |
| KK-16 | echt | Überschrift "Reference" S. 26, Z. 507. |

## 2. Literaturvorschläge

| Kennung | Vorgeschlagene Arbeit | Im Literaturverzeichnis |
|---|---|---|
| GB-02 | Guimpier et al. 2021, EGU21-4803 | nein |
| GB-02 | Ge, Tang und Li 2021, Landslides 18 | ja (S. 27, Z. 540 bis 542) |
| GB-02 | Zhao et al. 2021, Nat. Hazards 106 | ja (S. 29, Z. 600 bis 602) |
| GB-02 | Wu, J. et al. 2013, J. Geol. Soc. India 82 | ja (S. 28, Z. 588 bis 590) |
| GB-02 | Zhou et al. 2024, J. Earth Sci. 35 | ja (S. 29, Z. 603 bis 605) |
| GB-18 | Zhou et al. 2024, J. Earth Sci. 35 | ja (S. 29, Z. 603 bis 605) |

## 3. Doppelungen

Keine. Am selben Fundort mit gleichem Gegenstand stehen keine zwei Kennungen; Überschneidungen wie GB-11 und GB-12 (Z. 232 bis 234), GB-14 und GB-21 (Fig. 8), GB-12, GB-23 und GB-24 (Fig. 10b) oder GB-09 und GB-29 (Luding-Aufzeichnung) betreffen jeweils verschiedene Gegenstände.

## 4. Fundorte

| Lage | Anzahl |
|---|---|
| genau | 45 |
| 1 bis 2 Zeilen daneben | 0 |
| weiter daneben | 1 (KK-01: Z. 21 statt Z. 13) |

Gewertet ist je Kennung der Hauptfundort; als Nebenangabe ist in GB-10 "l. 241" eine Zeile daneben (richtig Z. 242).

## 5. Zählungen je Urteil

| Urteil | Anzahl |
|---|---|
| echt | 43 |
| teilweise echt | 3 (GB-02, GB-08, GB-10) |
| falsch | 0 |
| nicht prüfbar | 0 |
| gesamt | 46 |

Literaturvorschläge: 6, davon 5 ja, 1 nein. Doppelungen: 0.
