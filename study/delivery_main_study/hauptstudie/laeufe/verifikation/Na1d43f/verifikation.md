# Verifikation des Gutachtens zu egusphere-2025-4506

Grundlage: Manuskript-PDF (29 Seiten), Seitenbilder in seiten/ (150 dpi) und eigene Renderings in vf/r300/ (300 dpi) und vf/r600p7-07.png (600 dpi), text.json mit eigener Zuordnung der gedruckten Randnummern (vf/rand.txt, Skript vf/skripte/rand.py), Suchzählungen mit vf/skripte/suche.py, Rechnungen mit vf/skripte/rechnung.py, Abbildungsmessung Fig. 8 mit vf/skripte/fig8.py, Literatur über WebSearch und WebFetch (Liste in vf/zugriff_VF.txt).

## 1. Urteile je Kennung

| Kennung | Urteil | Beleg (ein Satz mit Seite und Zeile) |
|---|---|---|
| GB-01 | echt | Zitat wörtlich auf S. 1, Z. 33 bis 34; die Abstracts von Carpignano et al. (2009, IDEAS) und Fan et al. (2019a, USGS) nennen keinen Trend häufiger werdender Gefahrenketten, sondern gesteigerte Verwundbarkeit bzw. jahrzehntelang erhöhte Rutschungsaktivität nach einzelnen Beben. |
| GB-02 | echt | Zitate wörtlich auf S. 2, Z. 39 bis 41 und Z. 71 bis 73, "evaluation basis" auf S. 5, Z. 124; Suchen ergeben 0 Treffer für "question/hypothes" und 0 Treffer der elf Begriffe in S. 25, Z. 460 bis S. 26, Z. 492, "warning" einmal auf S. 2, Z. 72. |
| GB-03 | echt | Zitate wörtlich auf S. 2, Z. 42 und Z. 49 bis 51; Suchbegriffe 6 Treffer ohne Suchbeschreibung; Jaboyedoff et al. (2019, ESurf 7, 439 bis 458, SLBL, ±35 %, 10 % bis 25 %) und De Pedrini et al. (2022, Geogr. Helv. 77, 21 bis 37, Vorereignis-DEM und RAMMS) an der Quelle bestätigt, beide nicht im Verzeichnis. |
| GB-04 | echt | Zitat wörtlich auf S. 2, Z. 43 bis 46; für Zhang 2024 und Fan 2020 fehlt ein Eintrag (Verzeichnis S. 26 bis 29), Wu et al. (2024) ist laut Eintrag S. 28, Z. 585 bis 587 eine Wellensimulation; Inhalt von Song et al. (2017) war online nicht lesbar. |
| GB-05 | echt | Auszählung der 29 Zitierschlüssel auf S. 1, Z. 34 bis S. 2, Z. 63 ergibt 12 Treffer, 1 Jahresabweichung (Tian) und 16 ohne Eintrag; nach S. 2, Z. 74 0 Treffer für "et al". |
| GB-06 | echt | Zitat wörtlich auf S. 2, Z. 46 bis 49; Li et al. (2024, DOAJ/Frontiers) behandeln Sickerströmung und Stabilität unter Starkregen ohne Geländerekonstruktion, Du et al. (2021, JMS) DEM mit Paläobeben ohne Angabe der Modelldimension; die Softwareangabe GeoStudio war nicht bestätigbar. |
| GB-07 | echt | Zitat wörtlich auf S. 2, Z. 61 bis 63; van Herwijnen und Schweizer (2011, CRST 69, 165 bis 176) behandeln Schneelawinen, ihr Verzeichnis nennt Navarre et al. (2009) "The seismic detection of avalanches". |
| GB-08 | echt | Zitate wörtlich auf S. 2, Z. 63 bis 64 und S. 1, Z. 22 bis 23; das Springer-Abstract von Ge et al. (2021) enthält Kollisionen über lokale Geschwindigkeitsspitzen, Energieerhaltung der Gesamtmasse und mehr Kollisionen und Energie für die Front; "Ge" im Textkörper 4 Treffer nur als Autorname. |
| GB-09 | echt | Zitate wörtlich auf S. 7, Z. 149 bis 151 und S. 15, Z. 310 bis 312; Zhao et al. (2021, IDEAS) nennen 4500 × 10⁴ m³ bei 450 m × 1000 m, Zhou et al. (2024, HEP) dieselben drei Effekte; 450 × 1000 × 100 = 4500 × 10⁴ m³; Angaben zu He et al. (2023) und Wu et al. (2013) waren nicht abrufbar. |
| GB-10 | echt | "three parts" auf S. 2, Z. 76 bis S. 3, Z. 77, die Aufzählung (1) bis (4) auf S. 3, Z. 77 bis 90 und vier Modulkästen in der linken Spalte von Fig. 1 (S. 4). |
| GB-11 | echt | Zitate wörtlich auf S. 5, Z. 102 bis 104 und S. 11, Z. 207 bis 209; Legenden auf S. 6 (Fig. 2c: Plagiogranite, Massive gravel, Hybrid granite, Rubble soil), S. 8 (Fig. 3a/3b: Granite, Diorite, Massive gravelly soils) und S. 10 (Fig. 4: γo2, Qdel, γM2, Sliding mass) bestätigen die Benennungsvielfalt; "hybrid/γM" 0 Treffer. |
| GB-12 | echt | Zitat wörtlich auf S. 5, Z. 116 bis 119, keine Zitation auf S. 5; das Abstract zu Fan et al. (2019, Baige; Universität Twente) nennt Versagenswahrscheinlichkeit, Reichweite, Aufstau, Dammbruch und Flutwelle; He et al. (2023) nicht abrufbar. |
| GB-13 | teilweise echt | Zitate wörtlich auf S. 6, Z. 139 bis 140 und S. 25, Z. 465 bis 466; nicht zutreffend ist die Zählung "stratigraph only in Conclusion 1 (1 hit)", denn es gibt 2 Treffer, der zweite in Conclusion 2 auf S. 25, Z. 469. |
| GB-14 | echt | Zitat wörtlich auf S. 7, Z. 144 bis 146; Fig. 3a (S. 8) zeigt nur die Zonen "I Sliding bed" und "II Accumulation area". |
| GB-15 | echt | Zitate wörtlich auf S. 7, Z. 149 bis 151 und S. 9, Z. 173 bis 174 und Z. 182; Python bestätigt 4500 × 10⁴ m³, 53,3 m, 914 bis 1250 m, Faktor 75,6, 0,71 m, 10,0 bis 23,2 m, 276 Blöcke, 909 m, 67,8 m/s, 365 GJ, 12,0 m, 1,46 × 10⁶ m³ und 197 m; Fig. 8 (S. 20) beginnt bei rund 6500 GJ, der Wasserspiegel in Fig. 3b (S. 8) liegt bei rund 1145 m. |
| GB-16 | echt | Zitat wörtlich auf S. 7, Z. 159 bis 160; Fig. 2c (S. 6) zeigt nur eine Schnittlinie a, Fig. 3b (S. 8) ist mit "(a-a')" betitelt, Fig. 3c (S. 9) zeigt Höhenlinien und Schummerung. |
| GB-17 | echt | Fig. 3b (S. 8) ohne Achsentitel und mit "80°", Fig. 4 (S. 10) Zeitachse ohne Zahlen mit tp, tPGA, tf, te, Fig. 6 (S. 14) und Fig. 7h bis 7n (S. 18) ohne Achsentitel; "PGA/peak ground" 1 Treffer auf S. 15, Z. 317. |
| GB-18 | echt | Zitate wörtlich auf S. 9, Z. 168 bis 170 und S. 13, Z. 258 bis 259; "version", "resolution", "damp", "interval" 0 Treffer, "time step" 1 Treffer (S. 15, Z. 291), "unbalanced" 2 Treffer (S. 13, Z. 258 und Tabelle 2, ID 11). |
| GB-19 | echt | Zitat wörtlich auf S. 10, Z. 186 bis 189 ohne Zitation; Fault-Kreuzung auf S. 5, Z. 98 bis 99; Einschub von Fig. 4 (S. 10) zeigt rund ±100 gal ohne Skalierungsangabe. |
| GB-20 | echt | Zitate wörtlich auf S. 10, Z. 189 bis 190 und S. 11, Z. 206 bis 207; Suchen ergeben 7 Treffer (nur S. 10, Z. 190 nennt die Station) und 6 Treffer (4 auf S. 11, Z. 207, 2 in Affiliationen). |
| GB-21 | echt | Alle zitierten Wendungen wörtlich auf S. 10, Z. 193 bis 195, S. 5, Z. 110 bis 111 und Z. 119 bis 120, S. 1, Z. 38, S. 2, Z. 42 bis 44, S. 6, Z. 132 und S. 7, Z. 159. |
| GB-22 | echt | Zitate wörtlich auf S. 11, Z. 220 und Z. 230 bis 233; die Einschübe von Fig. 5c und 5d (S. 12) sind am Seitenbild deckungsgleich, Zusatzmarker in 5c nur jenseits von rund 1900 m. |
| GB-23 | echt | Sechs Kurvennamen auf S. 1, Z. 23, S. 11, Z. 221, 225, 227, 234 und S. 25, Z. 474 bis 475; Achsen "Travel distance (m)" in Fig. 5a und Fig. 1, "Travel Displacement (m)" in Fig. 5b bis 5f (S. 4, S. 12). |
| GB-24 | echt | Zitate wörtlich auf S. 11, Z. 233 bis 234 und S. 26, Z. 483; Fig. 5b (S. 12) erreicht rund 45 m/s, die abgelesenen 25 Punkte von Fig. 10b (S. 23) summieren sich auf rund 1214, 1139/10 = 113,9. |
| GB-25 | echt | Achsenzahlen in Fig. 11a bis 11j (S. 23 bis 24), Fig. 5 Einschübe (S. 12) und Fig. 12 (S. 25) sind am 300-dpi-Bild deutlich kleiner als 6 pt; die Einzelmaße wurden nicht nachgemessen. |
| GB-26 | echt | Zitate wörtlich auf S. 13, Z. 253 bis 255 und S. 19, Z. 378; in Fig. 8 und Fig. 9 (S. 20 bis 22) beginnt PE beim Gesamtwert, mit Tabelle 2 und 2300 kg/m³ ergeben sich Höhen 239 bis 30 m und Bezugsniveaus 101 bis 712, Spanne 611. |
| GB-27 | teilweise echt | Zitat wörtlich auf S. 13, Z. 256 bis 257, Fig. 6 (S. 14) zeigt die Reihenfolge Top, Lower middle part, Upper middle part, Bottom; nicht zutreffend ist "the only hits are p. 6, l. 132 and the Table 2 heading", denn "coordinate" steht auch auf S. 5, Z. 95 und S. 6, Z. 131 und 133. |
| GB-28 | teilweise echt | Zitate wörtlich auf S. 14, Z. 271 bis 273 und Z. 278, alle Einzelzählungen stimmen; nicht zutreffend ist die Gesamtzahl "nine names", denn aufgezählt werden acht Namen im Text und zwei in Bildunterschriften, also zehn. |
| GB-29 | echt | Zählungen auf S. 1, Z. 25 bis S. 26, Z. 488 bestätigt (VS 2 + 4 + 1 = 7, "area growth" 7); Zitate wörtlich auf S. 14, Z. 274 bis 275 und S. 24, Z. 440 bis 441, Achsen von Fig. 12 (S. 25) "Volume Swelling (%)", "Area Growth (%)". |
| GB-30 | echt | Zitate wörtlich auf S. 9, Z. 175 bis 178, S. 15, Z. 308 bis 309 und S. 25, Z. 469 bis 470, ferner "pre-existing potential sliding surfaces" S. 15, Z. 313 und "structural plane control" Z. 323. |
| GB-31 | echt | Zitate wörtlich auf S. 16, Z. 353 bis 354 und S. 25, Z. 471 bis 472; "RMSE/error/deviation/accura" in Abschnitt 3 und "sensitiv" im Text je 0 Treffer, 317563/24000000 = 0,0132. |
| GB-32 | echt | Farbskalen auf S. 17 bis 18 abgelesen: 0, 5.9, 19.6, 27.1, 31.6, 25.7, 0.21 m/s und 0, -33, -31, -33, -33, -33, -47 MPa, nur Endwerte, 7a vollständig rot. |
| GB-33 | echt | Eq. (4) auf S. 13, Z. 249 lautet DE(ti) = ME(t0) minus ME(ti), daraus folgt KE + PE + DE = ME(t0) algebraisch; Zitate wörtlich auf S. 19, Z. 375 bis 377, Z. 388 bis 389 und S. 20, Z. 393 bis 394; Gesamthöhen in Fig. 8 und 9 konstant. |
| GB-34 | echt | Zitat wörtlich auf S. 19, Z. 381 bis 384; eigene Pixelmessung an Fig. 8 (S. 20) ergibt KE rund 1080 GJ bei 11 s, 1570 GJ bei 12,2 s und Maximum rund 1660 GJ bei 13,4 s. |
| GB-35 | echt | Zitat wörtlich auf S. 13, Z. 256 bis 258; in Fig. 9 (S. 21 bis 22) sind die KE-Anteile nur schmale Säume, in Fig. 8 (S. 20) rund ein Viertel, 1681/6516 = 25,8 %. |
| GB-36 | echt | Zitate wörtlich auf S. 1, Z. 28 bis 30, S. 22, Z. 414 bis 415 und S. 26, Z. 485 bis 487; "front" 3, "rear" 2, "farther" 0 Treffer in den Ergebnissen, Fig. 10b (S. 23) fällt bei 700 bis 800 m von rund 16 auf rund 7. |
| GB-37 | echt | Zitat wörtlich auf S. 23, Z. 427 bis 428; Fig. 11 (S. 23 bis 24) enthält keine Volumen- oder Flächenwerte, die Suche ergibt V0, S0, m³, m² nur in den Definitionen S. 14, Z. 272 bis 280. |
| GB-38 | echt | Zitate wörtlich auf S. 24, Z. 445 und Z. 451 bis 452 und S. 26, Z. 489 bis 490; "fragment" 11 Treffer an den genannten Stellen, "fractur/breakag/split/crack/number of blocks" bis S. 15, Z. 296 0 Treffer. |
| GB-39 | echt | Zitat wörtlich auf S. 26, Z. 485 bis 487; Lin et al. (2022, NHESS 22, 639 bis 657, PFC2D) bestätigen den Satz "The energy transfer induced by fragmentation is more efficient than that induced by collision", kein Eintrag im Verzeichnis S. 26, Z. 507 bis S. 29, Z. 605. |
| GB-40 | echt | Zitat wörtlich auf S. 25, Z. 453 bis 455; Fig. 12 (S. 25) trägt weit mehr als zehn Marker und die Annotation "1116. 8", während Fig. 8 (S. 20) ein KE-Maximum von rund 1660 GJ zeigt; α ohne Einheit auf S. 14, Z. 283. |
| GB-41 | echt | Zitate wörtlich auf S. 26, Z. 494 bis 495 und Z. 505 bis 506; Suche ergibt 5 Treffer (4 in den Erklärungen, 1 auf S. 2, Z. 61), "appendix/supplement" 0 Treffer. |
| GB-42 | echt | 31 Einträge, davon 13 zitiert und 18 nicht zitiert; die Startzeilen aller 18 Einträge stimmen mit den Randnummern auf S. 26 bis 29 überein, die Aussagen S. 5, Z. 99 bis 100 und S. 10, Z. 187 sind ohne Zitation. |
| KK-01 | echt | Alle sechs Schreibweisen am Seitenbild an S. 1, Z. 13, S. 7, Z. 152, S. 9, Z. 182, S. 13, Z. 251 und S. 25, Z. 464 und 466 vorhanden. |
| KK-02 | teilweise echt | "dissipation energy" steht auf S. 1, Z. 21 und S. 3, Z. 84; nicht zutreffend sind "8 other places" und "10 hits", denn "dissipated energy" kommt neunmal vor, zusätzlich auf S. 25, Z. 470 bis 471, also 11 Treffer. |
| KK-03 | echt | Schreibweisen auf S. 1, Z. 23, S. 3, Z. 88 bis 89, S. 14, Z. 272 und 281, S. 23, Z. 426 und "Alpha Shape" in Fig. 1 (S. 4). |
| KK-04 | echt | Großschreibung nach Semikolon auf S. 1, Z. 27 und 28 und S. 7, Z. 153, 154, 156. |
| KK-05 | echt | Satz wörtlich auf S. 1, Z. 32. |
| KK-06 | echt | "high-level" 3 Treffer auf S. 1, Z. 33 und S. 2, Z. 39 und 40, "high-altitude" im Titel und auf S. 2, Z. 73. |
| KK-07 | echt | "such as donghekou" auf S. 1, Z. 34 (fortgesetzt Z. 35), "Donghekou" großgeschrieben in den Einträgen S. 28, Z. 572 und 579. |
| KK-08 | echt | "Fan et al., 2019a" auf S. 1, Z. 34, "Fan et al., 2019" auf S. 2, Z. 56 bis 57, beide Einträge auf S. 27, Z. 532 und 536 enden mit "2019." ohne Suffix. |
| KK-09 | echt | "Wang, 2021" auf S. 1, Z. 36, Eintrag S. 28, Z. 581 bis 584 mit sieben Autoren. |
| KK-10 | echt | "Tian et al., 2017" auf S. 1, Z. 37, Eintrag S. 28, Z. 575 bis 577 mit Jahr 2016. |
| KK-11 | echt | "Song at al.2017" auf S. 2, Z. 46. |
| KK-12 | echt | "Cheng 2014" auf S. 2, Z. 48 bis 49, Eintrag S. 27, Z. 521 mit zwei Autoren. |
| KK-13 | echt | Regex ohne Bildunterschriften ergibt 27 Abbildungsverweise in 25 Zeilen an genau den genannten Stellen von S. 2, Z. 76 bis S. 24, Z. 443. |
| KK-14 | echt | Fig. 1 (S. 4), Kasten "Global Perspective", zeigt P₀E, PₜE und KₜE. |
| KK-15 | echt | „"Y" - shaped faults“ auf S. 5, Z. 98. |
| KK-16 | echt | "The quaternary system" auf S. 5, Z. 104 und "colluvial Deluvial deposit" auf Z. 105. |
| KK-17 | echt | "According to the DEM data" auf S. 6, Z. 130, "digital elevation" 0 Treffer, "DEM" 2 Treffer (S. 6, Z. 130; S. 7, Z. 144). |
| KK-18 | echt | Legende Fig. 2b (S. 6) "Daduhe River", Fig. 2c "Dadu River", "Dadu" im Text 13 Treffer von S. 5, Z. 94 bis S. 16, Z. 348. |
| KK-19 | echt | Legenden Fig. 3a und 3b (S. 8) lauten "Dadu river". |
| KK-20 | echt | Am Seitenbild S. 7, Z. 151 steht "2400×104 m³" mit 104 auf der Grundlinie und hochgestellter 3. |
| KK-21 | echt | "can not be obtained" auf S. 9, Z. 176 bis 177. |
| KK-22 | echt | "velocities-hereafter" auf S. 11, Z. 218 und "chosen-one" auf Z. 228, am Seitenbild als Bindestrich gesetzt. |
| KK-23 | echt | Tabelle 1 (S. 11) mit "bed rock" und Schubmodul "6.9" neben 15.10, 21.90, 11.90. |
| KK-24 | echt | "Table 1 Physical parameters" (S. 11) und "Table 2: The basic information" (S. 13). |
| KK-25 | echt | Legende Fig. 5a (S. 12) "Non-obvios acceleration". |
| KK-26 | echt | Satz wörtlich auf S. 13, Z. 246, KE(ti) fehlt in der Aufzählung. |
| KK-27 | echt | Farbskalen Fig. 7h bis 7n (S. 18) "0Mpa", "-33Mpa", "-31Mpa", "-47Mpa". |
| KK-28 | teilweise echt | Leerzeichen vor Semikolon am Seitenbild S. 22, Z. 410 bis 413 vorhanden; nicht zutreffend ist "nine semicolons", es sind acht (nach point 1 bis point 8). |
| KK-29 | echt | Überschriften 3 (S. 15, Z. 297), 3.1 (Z. 298), 3.2 und 3.2.1 (S. 19, Z. 371, 372), 3.2.2 (S. 20, Z. 391), 3.4 (S. 23, Z. 425), kein 3.3. |
| KK-30 | echt | Bildunterschrift S. 24, Z. 438 bis 439 "(a-i)" mit zehn Zeitpunkten, Panels (a) bis (j) auf S. 23 bis 24. |
| KK-31 | echt | Annotationen "1116. 8", "29. 47", "319. 5" in Fig. 12a und 12b (S. 25). |
| KK-32 | echt | "XF: Data curation, Investigation. LZ:" auf S. 26, Z. 499. |
| KK-33 | echt | Überschrift "Reference" auf S. 26, Z. 507. |
| KK-34 | echt | Am Seitenbild sind Dahal (S. 27, Z. 524 bis 526), Nava und Sinčić (S. 28, Z. 562 bis 568) heller und im Flattersatz ohne Einzug gesetzt; Bernardie und Zhang, K. nicht einzeln geprüft. |
| KK-35 | echt | Eintrag S. 27, Z. 530 "Fan, X., Scaringi, G., Korup, O., et al.:", alle übrigen Einträge mit voller Autorenliste. |

## 2. Literaturvorschläge: bereits im Verzeichnis?

| Vorschlag (Kennung) | Im Verzeichnis |
|---|---|
| Jaboyedoff et al. (2019), ESurf 7 (GB-03) | nein |
| De Pedrini et al. (2022), Geogr. Helv. 77 (GB-03) | nein |
| Lin et al. (2022), NHESS 22 (GB-39) | nein |
| Ge et al. (2021), Landslides 18 (GB-08) | ja (S. 27, Z. 540 bis 542) |
| Wu, J. et al. (2013) (GB-09) | ja (S. 28, Z. 588 bis 590) |
| Zhao et al. (2021) (GB-09) | ja (S. 29, Z. 600 bis 602) |
| He, J. et al. (2023) (GB-09, GB-12) | ja (S. 27, Z. 546 bis 548) |
| Zhou et al. (2024) (GB-09) | ja (S. 29, Z. 603 bis 605) |
| Fan et al. (2019, Baige) (GB-12) | ja (S. 27, Z. 533 bis 536) |
| Fan et al. (2019a, Rev. Geophys.) (GB-12) | ja (S. 27, Z. 530 bis 532) |

## 3. Doppelungen

| Paar | Fundort | Gegenstand |
|---|---|---|
| GB-09 und GB-42 | Einträge S. 27, Z. 546; S. 28, Z. 588; S. 29, Z. 600 und 603 | nie zitierte Arbeiten zum Mogangling-Rutsch im Verzeichnis; GB-42 schließt die vier Einträge von GB-09 ein |

Weitere Überschneidungen (GB-08 und GB-42 zu Ge et al. 2021; GB-19 und GB-20 zum Eingangssignal) betreffen verschiedene Gegenstände und sind nicht gezählt.

## 4. Fundorte

Geprüft wurden 77 Kennungen an den gedruckten Randnummern (Seitenbilder) bzw. am benannten Abbildungs- oder Tabellenelement.

| Klasse | Anzahl |
|---|---|
| genau | 77 |
| um 1 bis 2 Zeilen daneben | 0 |
| weiter daneben | 0 |

## Zählungen

| Urteil | Anzahl |
|---|---|
| echt | 72 |
| teilweise echt | 5 (GB-13, GB-27, GB-28, KK-02, KK-28) |
| falsch | 0 |
| nicht prüfbar | 0 |
| Summe | 77 |

Literaturvorschläge: 10, davon 7 ja, 3 nein. Doppelungen: 1. Fundorte: 77 genau, 0 um 1 bis 2 Zeilen, 0 weiter daneben.
