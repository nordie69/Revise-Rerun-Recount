# Verifikation des Gutachtens zu egusphere-2025-4506

Grundlage: egusphere-2025-4506.pdf (Seitenbilder in seiten/ und eigene 300-dpi-Renderings in vf/png/), text.json mit Randnummernzuordnung (vf/margin.txt, gegen die gedruckten Randnummern der Seitenbilder abgeglichen), Rechnungen mit Python, Literatur über WebFetch.

## 1. Urteile je Kennung

| Kennung | Urteil | Beleg (ein Satz mit Seite und Zeile) |
|---|---|---|
| GB-01 | echt | Zitat steht wörtlich S. 1, Z. 33 bis 34; das Verzeichnis hat zwei Einträge Fan 2019 ohne Buchstaben (S. 27, Z. 530 bis 536); Carpignano 2009 nennt laut Abstract weder Erdrutsche noch Erdbeben, Fan 2019 nur eine jahrzehntelang erhöhte Rate nach Beben. |
| GB-02 | teilweise echt | Zitat S. 1, Z. 38 bis S. 2, Z. 39, Volumen 2400×10^4 m³ (S. 7, Z. 151), "tens of thousands" (S. 5, Z. 111) und Longmenshan (S. 10, Z. 186 bis 187) stimmen, Zhao 2021 (4500×10^4 m³, über 100 000 Tote), He 2023 (Faktor 5,3), Zhou 2024 und Dai 2005 (Xianshuihe, über 100 000 Tote) an der Quelle bestätigt; nicht zutreffend ist, dass Zhao 2021 nie zitiert wird (S. 2, Z. 57 "Zhao et al., 2020", vom Gutachten selbst in KK-09 und GB-52 als Zitat mit Jahresfehler gewertet), und Dai 2005 schreibt "Ten days later", nicht 9 Tage. |
| GB-03 | echt | Alle drei Zitate wörtlich S. 2, Z. 40, Z. 67 bis 68, Z. 71 bis 72; Suche in S. 25, Z. 460 bis S. 26, Z. 492 ergibt 0 Treffer für alle genannten Begriffe, "velocit" nur Z. 474, "trajector" nur Z. 465. |
| GB-04 | echt | Zitate S. 2, Z. 42, Z. 46 bis 47, Z. 50 bis 51 wörtlich; 10 Teilstringtreffer der Suchbegriffe, alle in "research", "reviewers" oder Titeln; Jaboyedoff 2019 (SLBL, Talas, 10 bis 25 %) an der Quelle bestätigt und nicht im Verzeichnis. |
| GB-05 | echt | Zitat S. 2, Z. 42 bis 46 wörtlich mit "Song at al.2017"; Song 2017 (S. 28, Z. 569 bis 571) und Wu 2024 (S. 28, Z. 585 bis 587) sind Simulationsarbeiten, Zhang 2024 und Fan 2020 fehlen im Verzeichnis. |
| GB-06 | echt | 29 zitierte Werke in S. 1, Z. 34 bis S. 2, Z. 63 nachgezählt, 15 ohne Eintrag (51,7 %), 31 Einträge S. 26, Z. 508 bis S. 29, Z. 605; keine Zitate nach S. 2, Z. 63. |
| GB-07 | echt | Zitat S. 2, Z. 61 bis 63 wörtlich; van Herwijnen und Schweizer 2011 behandeln laut Volltext Schneelawinen und zitieren Navarre et al. 2009 (ISSW). |
| GB-08 | echt | Zitat S. 2, Z. 63 bis 64 wörtlich; Ge et al. 2021 steht S. 27, Z. 540 bis 542 ohne Zitat; ResearchGate zeigt "Energy analysis for 16 individual blocks" und "travel distance vs. collision frequency"; Knapp und Krautblatter 2020 nennen 20 bis 50 % und fehlen im Verzeichnis. |
| GB-09 | echt | Text S. 5, Z. 95 bis 96 gibt 102,161° O; der Marker in Fig2 (a) liegt am 300-dpi-Bild bei etwa 101,2° O und 29,55° N. |
| GB-10 | echt | Text S. 5, Z. 100 bis 107 und die Legenden von Fig2 (c) (S. 6), Fig3 (a), (b) (S. 8) und Fig4 (S. 10) verwenden die genannten abweichenden Namen und Codes; am linken Ufer zeigt Fig2 (c) γM2 statt T3bg. |
| GB-11 | echt | Satz S. 5, Z. 113 bis 121 wörtlich, ohne Zitat und ohne Suchbeschreibung. |
| GB-12 | echt | Zitate S. 6, Z. 136 bis 137, S. 9, Z. 180 bis 181, S. 10, Z. 189 bis 190, S. 11, Z. 206 bis 207 wörtlich; "station" nur S. 5, Z. 115 und S. 10, Z. 190; Datenerklärung S. 26, Z. 505 bis 506 ohne Quellen; Legende Fig2 (b) "Daduhe River". |
| GB-13 | echt | Zitate S. 6, Z. 139 bis 140 und S. 25, Z. 465 bis 468 wörtlich; 0 Treffer für die fünf Suchbegriffe in S. 1 bis S. 25, Z. 459; Fig1 zeigt "Deposit Removal" und "Lower Slide Bed Restoration". |
| GB-14 | echt | S. 7, Z. 145 bis 146 nennt vier Teile, Fig3 (a) (S. 8) zeigt nur "I Sliding bed" und "II Accumulation area". |
| GB-15 | echt | Zitat S. 7, Z. 149 bis 152 wörtlich; 0,45 km² × 100 m = 4500×10^4 m³ (Faktor 1,875, Mittelmächtigkeit 53,3 m), Profillänge 914 bis 1250 m nachgerechnet; Wasserspiegel in Fig3 (b) bei etwa 1146 m. |
| GB-16 | teilweise echt | S. 7, Z. 159 bis 160 nennt b-b', das weder in Fig2 (c) noch in Fig3 (b) vorkommt; nicht zutreffend ist, dass beide Enden mit "a" beschriftet sind, das Ostende trägt am 300-dpi-Bild ein rotes "a′" in Schriftfarbe (RGB etwa 237,4,31). |
| GB-17 | echt | Zitate S. 7, Z. 160 bis 162 und S. 9, Z. 172 wörtlich; Prüfung nur visuell (Fig3 (c)); 2400×10^4 / 317563 = 75,6 nachgerechnet. |
| GB-18 | echt | Legendenfelder Fig3 (a) (S. 8) gemessen: Diorite (137,120,112) und Sand and pebble gravel (138,118,91) unterscheiden sich nur im Blaukanal, RGB-Summendifferenz 24. |
| GB-19 | echt | Fig3 (b), Fig6, Fig7 (h) bis (n), Fig5-Einsätze tragen nur Zahlen, die Zeitachse des Fig4-Einsatzes (S. 10) hat keine Zahlen. |
| GB-20 | echt | Zitate S. 9, Z. 169 bis 170 und S. 10, Z. 203 wörtlich; "damp" 0 Treffer; Version, Zeitschritt, Kontaktmodell fehlen. |
| GB-21 | echt | Zitate S. 9, Z. 177 bis 178, S. 15, Z. 308 bis 309 und Z. 323 wörtlich; Raster 8,7 m × 8,7 m S. 9, Z. 178. |
| GB-22 | echt | Fig4-Legende (S. 10) γo2, Qdel, γM2, Sliding mass gegen Table 1 "bed rock", "landslide mass" (S. 11) und S. 11, Z. 207 bis 209. |
| GB-23 | echt | Zitate S. 10, Z. 186 bis 189 wörtlich ohne Beleg; Einsatz zeigt tp, tPGA, tf, te ohne Werte; Dai 2005 (Xianshuihe) und He 2023 (5,3) an der Quelle bestätigt. |
| GB-24 | echt | Fig4-Legende nur Codes, "Qdel" ohne 4; "PGA" 0 Treffer, "peak ground acceleration" nur S. 15, Z. 317; Fig1 zeigt P0E, PtE, KtE. |
| GB-25 | echt | Zitate S. 10, Z. 199 bis 200 und S. 13, Z. 258 bis 259, Z. 262 bis 263 wörtlich; "unbalanced" 2 Treffer, "stress" im Ergebnisteil nur Z. 302, 312, 369. |
| GB-26 | echt | Zitate S. 11, Z. 206 bis 207 und S. 2, Z. 65 bis 66 wörtlich; keine Feld- oder Labordaten im Manuskript. |
| GB-27 | echt | Zitate S. 11, Z. 209 bis 210 und S. 9, Z. 179 bis 180 wörtlich; Table 1 nennt "discontinuities" und "potential discontinuities" ohne Zuordnung. |
| GB-28 | echt | Zitat S. 11, Z. 221 bis 223 wörtlich; am 300-dpi-Bild 6 rote, 5 violette Marker, rote Marker bei etwa 243 m und 463 m liegen auf steigenden Flanken; Legende "Non-obvios". |
| GB-29 | echt | Alle neun Varianten an S. 1, Z. 23 und 30, S. 11, Z. 221, 225, 227, 234, S. 22, Z. 418, S. 25, Z. 474 sowie die Achsentitel in Fig5 und Fig10 (b) bestätigt. |
| GB-30 | echt | Zitate S. 11, Z. 227 bis 228, Z. 232 bis 234 wörtlich; Zahl nur für 30 %; Kurven in Fig5 (b) bis (f) mit Spitze um 45 m/s gegen 31,6 m/s in S. 16, Z. 330. |
| GB-31 | echt | Fig11-Titel S. 24, Z. 437 bis 439 und Fig5-Titel S. 12, Z. 238 bis 239 erklären weder Netz und Einsatz noch Kasten und Einsatz. |
| GB-32 | echt | Ziffernhöhen am 300-dpi-Bild nachgemessen (z. B. Fig12 und Fig7 (a) etwa 4 bis 5 pt, Fig11 deutlich kleiner), alle unter 6 pt. |
| GB-33 | echt | Table 2 (S. 13) x von minus 719 bis minus 68, y von minus 557 bis 286, z 340 bis 755; Fig4, Fig6, Fig7 nur positive Achsen, Fig10 (a) Z bis minus 840. |
| GB-34 | echt | Fig6 (S. 14) Beschriftung von oben Top, Lower middle part, Upper middle part, Bottom bei Markerverteilung 2, 3, 3, 2 ohne IDs; Table 2 z-Werte bestätigen die Vertauschung. |
| GB-35 | echt | Alle Bezeichnungen an S. 1, Z. 24, S. 3, Z. 88 bis 89, S. 14, Z. 269 bis 272, S. 23, Z. 427 bis 429, S. 24, Z. 449 und 452, S. 26, Z. 491 bestätigt; Zitat S. 14, Z. 278 bis 279 wörtlich; Kurven in Fig12 beginnen bei VS 0 %. |
| GB-36 | echt | Zitat S. 14, Z. 282 bis 284 wörtlich; Punktmenge, Implementierung und Einheit von α fehlen; Fig12 reicht bis VS etwa 1240 % und AG etwa 4300 %. |
| GB-37 | echt | "volume swelling" oder "volume expansion" 6 Treffer, "area growth" 7 Treffer an den genannten Zeilen; Zitat S. 24, Z. 440 bis 441 wörtlich; Fig12-Titel S. 25, Z. 458 bis 459. |
| GB-38 | echt | Zitate S. 15, Z. 299, S. 16, Z. 353, S. 25, Z. 471 bis 472 wörtlich; keine Messgröße im Vergleich; Zhao 2021 nennt Dammkrone etwa 130 m über Fluss und Haupt- und Restablagerung. |
| GB-39 | echt | Zitat S. 15, Z. 301 bis 302 wörtlich; Fig7 (h) (S. 18) einheitlich rot mit Farbbalken "0" bis "0Mpa", (i) bis (n) minus 31 bis minus 47 "Mpa". |
| GB-40 | echt | Gl. (1) S. 12, Z. 245 und Gl. (4) S. 13, Z. 249 ergeben KE + PE + DE = ME(t0) identisch; Zitate S. 19, Z. 375 bis 377, Z. 388 bis 389, S. 1, Z. 27 bis 28, S. 25, Z. 479 wörtlich; Fig8-Summen gemessen 6469 bis 6516 GJ. |
| GB-41 | echt | Zitate S. 9, Z. 181 bis 182 und S. 7, Z. 151 wörtlich; Fig8 nachgemessen PE etwa 6500 GJ, KE-Maximum etwa 1657 GJ bei 13,4 s; Fallhöhe 907 m, v_rms 67,5 m/s, 756 GJ, 12,0 m, 12,53 m³, 7,1×10^5 m³ mit Python bestätigt. |
| GB-42 | echt | Zitate S. 20, Z. 393 bis 395 und S. 26, Z. 485 bis 487 wörtlich; keine Kontaktarbeit berechnet. |
| GB-43 | echt | Zitat S. 20, Z. 397 bis 399 wörtlich; Fig9 (a) und (c) (S. 21) zeigen PE-Anstieg über 30 bis 40 s ohne sichtbare KE. |
| GB-44 | echt | Zitate S. 13, Z. 250 und Z. 254 wörtlich; Fig9-Summen bestätigt; Fallhöhen 238,6 bis 29,8 m und Bezugshöhen etwa 100 bis 711 m, Volumenanteil 3,63 %, Energieanteil 0,67 % mit Python nachgerechnet. |
| GB-45 | echt | Zitate S. 1, Z. 29 bis 30 und S. 26, Z. 484 bis 485 wörtlich; im Ergebnisteil keine Zahl je Block oder Gruppe; 10 von 25345 = 0,039 %. |
| GB-46 | echt | Zitate S. 22, Z. 418 bis 419 und S. 11, Z. 233 bis 234 wörtlich; Fig10 (b) (S. 23) nachgemessen 26 Punkte, Summe etwa 1216, viermal fallend. |
| GB-47 | echt | Zitat S. 1, Z. 29 wörtlich; Fig10 (b) zeigt absolute Zahlen ohne Normierung. |
| GB-48 | echt | Fig10 (b) Achse "Frequency" ohne Einheit, rote Kurve ohne Legende; Titel S. 23, Z. 423 bis 424 wörtlich. |
| GB-49 | echt | Zitate S. 23, Z. 426 bis 427 und S. 25, Z. 455 wörtlich; Fig12 zeigt KE 1116,8 GJ und deutlich mehr als 10 Punkte je Kurve, Fig8 KE-Maximum etwa 1657 GJ. |
| GB-50 | echt | Zitate S. 25, Z. 453 bis 454 und S. 26, Z. 489 bis 490 wörtlich; "number of blocks", "number of fragments", "contact" im Ergebnisteil 0 Treffer. |
| GB-51 | echt | Zitate S. 26, Z. 494 bis 495 und Z. 505 bis 506 wörtlich; keine Links in Z. 493 bis 506. |
| GB-52 | echt | 17 von 31 Einträgen ohne Zitat (54,8 %), darunter Wu 2013 (S. 28, Z. 588 bis 590) und Ge 2021 (S. 27, Z. 540 bis 542); Zitate wörtlich. |
| KK-01 | echt | S. 1, Z. 13 "610041 ,China". |
| KK-02 | echt | "dissipation energy" S. 1, Z. 21 und S. 3, Z. 84; die übrigen 8 Treffer "dissipat* energy" verwenden "dissipated". |
| KK-03 | echt | Schreibungen S. 1, Z. 23, S. 3, Z. 88 bis 89, S. 14, Z. 272 und 281, S. 23, Z. 426 und im Flussdiagramm bestätigt. |
| KK-04 | echt | "high-level" S. 1, Z. 33 und S. 2, Z. 39 bis 40, "high-altitude" im Titel und S. 2, Z. 73. |
| KK-05 | echt | S. 1, Z. 34 "such as donghekou". |
| KK-06 | echt | S. 1, Z. 36 "Wang, 2021"; Eintrag S. 28, Z. 581 bis 584 hat sieben Autoren. |
| KK-07 | echt | S. 1, Z. 37 "Tian et al., 2017", Eintrag S. 28, Z. 575 bis 577 mit 2016. |
| KK-08 | echt | S. 2, Z. 48 bis 49 "Cheng 2014", Eintrag S. 27, Z. 521 bis 523 "Cheng, F., and Yu-Sheng, L.". |
| KK-09 | echt | S. 2, Z. 57 "Zhao et al., 2020", Eintrag S. 29, Z. 600 bis 602 mit 2021. |
| KK-10 | echt | Am Seitenbild S. 2, Z. 73 ist "altitude" grau gesetzt. |
| KK-11 | echt | S. 2, Z. 76 bis S. 3, Z. 77 "three parts", aufgezählt werden (1) bis (4), Fig1 hat vier Blöcke. |
| KK-12 | echt | 39 Fig-Nennungen gezählt: 12 Bildtitel und 27 Textverweise, davon nur S. 15, Z. 301 "Fig7" ohne Punkt. |
| KK-13 | echt | Im Flussdiagramm S. 4 berührt das "e" von "volume" den rechten Kastenrand. |
| KK-14 | echt | S. 5, Z. 97 "to the West". |
| KK-15 | echt | S. 5, Z. 98 "Y" - shaped. |
| KK-16 | echt | S. 5, Z. 99 bis 100 wörtlich. |
| KK-17 | echt | S. 5, Z. 110 bis 111 wörtlich. |
| KK-18 | echt | S. 6, Z. 132 bis 133 wörtlich. |
| KK-19 | echt | S. 7, Z. 152 "1120 m-1330m" und dreimal "; The elevation" in Z. 153, 154, 156. |
| KK-20 | echt | S. 9, Z. 182 "1121m high". |
| KK-21 | echt | S. 10, Z. 193 bis 195 wörtlich. |
| KK-22 | echt | S. 11, Z. 218 und Z. 228 Bindestrich als Gedankenstrich. |
| KK-23 | echt | Table 1 (S. 11) "bed rock" und "6.9" neben "15.10". |
| KK-24 | echt | "Table 1 Physical parameters" (S. 11) gegen "Table 2: The basic information" (S. 13). |
| KK-25 | echt | S. 13, Z. 246 ohne KE(ti) und Z. 251 "(m/s);h(ti)". |
| KK-26 | teilweise echt | S. 22, Z. 410 bis 413 setzt vor jedem Semikolon ein Leerzeichen, es sind aber 8 Semikolons (nach point 1 bis 8), nicht 9. |
| KK-27 | echt | S. 23, Z. 425 "3.4", kein Abschnitt 3.3. |
| KK-28 | echt | S. 24, Z. 438 bis 439 "(a-i)" bei zehn Teilbildern (a) bis (j). |
| KK-29 | echt | S. 25, Z. 464 "that:(a)" und Z. 466 "contours;(b)". |
| KK-30 | echt | S. 26, Z. 499 "Investigation. LZ:". |
| KK-31 | echt | S. 26, Z. 507 "Reference". |
| KK-32 | echt | Bernardie (S. 26), Dahal (S. 27), Nava, Sinčić (S. 28), Zhang K. (S. 29) am Seitenbild grau und nicht im Blocksatz. |
| KK-33 | echt | S. 27, Z. 530 "Fan, X., Scaringi, G., Korup, O., et al.:". |

## 2. Literaturvorschläge: bereits im Literaturverzeichnis?

| Vorschlag | Kennung | Im Verzeichnis |
|---|---|---|
| Dai, Lee, Deng und Tham (2005), Geomorphology 65 | GB-02 | nein |
| Jaboyedoff et al. (2019), Earth Surface Dynamics 7 | GB-04 | nein |
| Knapp und Krautblatter (2020), Frontiers in Earth Science 8 | GB-08 | nein |
| Ge, Tang und Li (2021), Landslides 18 (Zitiervorschlag) | GB-08, GB-52 | ja (S. 27, Z. 540 bis 542) |
| Wu et al. (2013) (Zitiervorschlag) | GB-02, GB-52 | ja (S. 28, Z. 588 bis 590) |
| Zhao et al. (2021) (Zitiervorschlag) | GB-02, GB-52 | ja (S. 29, Z. 600 bis 602) |
| He et al. (2023) (Zitiervorschlag) | GB-02 | ja (S. 27, Z. 546 bis 548) |
| Zhou et al. (2024) (Zitiervorschlag) | GB-02, GB-52 | ja (S. 29, Z. 603 bis 605) |

Neu vorgeschlagene Arbeiten: 3, davon 0 bereits im Verzeichnis. Zitiervorschläge für vorhandene Einträge: 5, alle im Verzeichnis.

## 3. Doppelungen (gleicher Fundort, gleicher Gegenstand)

| Paar | Fundort | Gegenstand |
|---|---|---|
| GB-45 und GB-47 | S. 1, Z. 29; S. 22, Z. 418 bis 421; Fig10 (b); S. 26, Z. 484 bis 485 | fehlende Grundlage der Aussage, die untere Masse kollidiere häufiger (GB-47 ist ein Teilaspekt, Normierung, derselben Aussage) |
| GB-46 und GB-48 | Fig10 (b); S. 23, Z. 423 bis 424 | undefinierte Zählgröße der Ordinate von Fig10 (b) (was ein Punkt zählt) |

## 4. Fundorte

| Kategorie | Anzahl |
|---|---|
| genau | 85 |
| um 1 bis 2 Zeilen daneben | 0 |
| weiter daneben | 0 |

## Zählungen

| Urteil | Anzahl |
|---|---|
| echt | 82 |
| teilweise echt | 3 (GB-02, GB-16, KK-26) |
| falsch | 0 |
| nicht prüfbar | 0 |
| Summe | 85 (52 GB, 33 KK) |
