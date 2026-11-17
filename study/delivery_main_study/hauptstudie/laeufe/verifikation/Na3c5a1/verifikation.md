# Verifikation des Gutachtens zu egusphere-2025-4506

Grundlage: Manuskript-PDF (29 Seiten), Seitenbilder in seiten/ (150 dpi) und eigene Renderings mit 300 und 600 dpi in vf/hr/, Zeilennummern an den gedruckten Randnummern bestätigt, Zahlen mit Python nachgerechnet (vf/rechnungen.py), Abbildungswerte per Pixelauswertung gemessen (vf/fig8c.py, vf/fig10.py, vf/fig2c.py, vf/grey.py), Literatur über WebSearch und WebFetch, soweit lesbar.

## 1. Urteil je Kennung

| Kennung | Urteil | Beleg (ein Satz mit Seite und Zeile) |
|---|---|---|
| GB-01 | echt | Zitat steht wörtlich S. 1, Z. 33 bis 34; Carpignano et al. (2009) behandelt laut Abstract Multi-Risk-Karten für das Piemont ohne Erdbeben-Hangrutschketten oder Trend, Fan et al. (2019) nennt laut Abstract eine Jahrzehnte anhaltende erhöhte Rutschungshäufigkeit nach Beben, und S. 27, Z. 530 bis 536 enthält zwei Fan-2019-Einträge ohne Buchstaben. |
| GB-02 | echt | Zitate S. 2, Z. 40 bis 41 und Z. 72 vorhanden; ein Lauf mit einem Parametersatz (Tab. 1), Blockgröße 8,7 m (S. 9, Z. 178) und ein Eingangssignal (S. 10, Z. 189 bis 191), Variation nur des Schwellwerts in Fig5. |
| GB-03 | echt | Zitate S. 2, Z. 42 und Z. 50 bis 51 wörtlich; keine Treffer für search, Scopus, Web of Science, CNKI im Text; von Wartburg et al. (2020) enthält im Abschnitt "Reconstruction of Pre-Failure Topography and Volume Analysis" den zitierten Satz und nutzt Dan3D-Flex, und die Arbeit fehlt unter den 31 Einträgen. |
| GB-04 | echt | Zitat S. 2, Z. 43 bis 45 wörtlich; Fan et al. (2020) und Zhang et al. (2024) haben keinen Eintrag, Song et al. (2017, S. 28, Z. 569 bis 571) und Wu et al. (2024, Z. 585 bis 587) sind laut Titel numerische Simulationen (GPS-Detail zu Song nicht lesbar). |
| GB-05 | echt | Auszählung S. 1, Z. 33 bis S. 2, Z. 63 ergibt 29 Schlüssel, davon 14 ohne Eintrag (Fan 2020, Huang 2012, Intrieri, Huang 2019, Zhu, Zhang 2020a, 2020b, Cuomo, Shugar, Navarre, Van Herwijnen, Helmstetter, Cook, Pandey), 14/29 = 48,3 %. |
| GB-06 | echt | Zitat S. 2, Z. 46 bis 48 wörtlich; Li et al. (2024) behandelt laut Abstract die regengetriebene Reaktivierung des Zhongbao-Rutsches ohne Geländerekonstruktion oder äußere Last, Du et al. (2021) laut Abstract DEM mit Paläobeben ohne Angabe der Dimension (GeoStudio-Details nicht lesbar). |
| GB-07 | echt | Zitat S. 2, Z. 63 bis 64 wörtlich; die zitierten Sätze aus Hibert et al. (2011), Farin et al. (2015) und Lin et al. (2022) stehen in den Quellen, und Ge et al. (2021, S. 27, Z. 540 bis 542) sowie Chang et al. (2022, S. 26, Z. 514 bis 516) werden im Text nicht zitiert. |
| GB-08 | echt | Der Punkt in Fig2 (a) liegt bei etwa 101,1 °E gegenüber 102,161 °E im Text (S. 5, Z. 95 bis 96), und der Stern in Fig2 (b) sitzt auf dem Kreuz 102°09'E/29°37'N, die Textkoordinate liegt rund 1107 m östlich und 947 m nördlich davon am Flusslauf. |
| GB-09 | echt | Text S. 5, Z. 101 bis 105 nennt γO2, O2, T3bg, Q4del, Q4col+dl, Fig2 (c) zeigt Plagiogranite, Hybrid granite (γM2), Rubble soil, Massive gravel ohne O2 und T3bg, Fig3 nennt Granite und Diorite, Fig4 γo2, Qdel, γM2, und Tab. 1 (S. 11) hat nur bed rock und landslide mass. |
| GB-10 | echt | Beide Zitate stehen S. 5, Z. 113 bis 114 und Z. 119 ohne Beleg, He, J. et al. (2023) steht S. 27, Z. 546 bis 548 und wird nirgends zitiert. |
| GB-11 | echt | Zitate S. 6, Z. 139 bis 140 und S. 11, Z. 206 bis 207 wörtlich; Begradigungsregel, Inversionsziel, Herkunft je Tabellenwert, DEM-Auflösung und Filterwerte fehlen, "trajectory equations" erscheint nur S. 25, Z. 465. |
| GB-12 | echt | S. 7, Z. 144 bis 146 nennt vier Teilbereiche, die Legende von Fig3 (a) auf S. 8 enthält nur "I Sliding bed" und "II Accumulation area". |
| GB-13 | echt | S. 7, Z. 149 bis 151 und S. 9, Z. 182 liefern 2400×10⁴, 4500×10⁴ (Faktor 1,875) und 317563 m³ (Faktor 75,6), die Grenze in Fig2 (c) umschließt rund 0,99 km², Q4del 0,47 km², und mit 7,304×10⁸ kg verlangt das gemessene Fig8-Total von 6497 bis 6516 GJ eine mittlere Fallhöhe von 907 m. |
| GB-14 | echt | Die Wasserlinie in Fig3 (b) auf S. 8 misst etwa 1145 m, S. 7, Z. 151 bis 152 impliziert rund 1115 m. |
| GB-15 | echt | S. 7, Z. 159 bis 160 nennt a-a' und b-b', Fig2 (c) zeigt nur eine Linie mit "a" im Westen und "a'" im Osten (600 dpi geprüft), Fig3 (b) ist mit "(a-a')" überschrieben. |
| GB-16 | echt | Fig3 (b) auf S. 8 hat Achsen ohne Größe und Einheit und ein "80°"-Symbol ohne Legende, Fig3 (c) auf S. 9 vier Karten ohne Buchstaben mit unerklärten blauen Rechtecken, untere Karten ohne Maßstab und Nordpfeil; Bildunterschrift Z. 166 bis 167. |
| GB-17 | echt | Zitat S. 9, Z. 169 bis 170 wörtlich ohne Beleg; Version, Dämpfung, Zeitschritt, Kontaktmodell und Signalaufbereitung fehlen, der Einschub in Fig4 (S. 10) hat keine beschriftete Zeitachse und keinen PGA-Wert. |
| GB-18 | echt | Zitat S. 10, Z. 187 bis 189 ohne Beleg, nur ein Signal (Z. 189 bis 191), Z. 186 bis 187 nennt Longmenshan, S. 5, Z. 97 bis 99 das Y-Störungssystem. |
| GB-19 | echt | Zitat S. 10, Z. 189 bis 191 wörtlich; für Signal, Satellitenbild, Karte, Tafel, Labortests und Fotos fehlen Herkunftsangaben, die Datenerklärung S. 26, Z. 505 bis 506 verweist nur auf den Erstautor. |
| GB-20 | echt | Der Einschub "Acceleration (gal)" in Fig4 (S. 10) hat unbeschriftete Zeitticks, tp, tPGA, tf, te kommen im Text nicht vor, die Bildunterschrift Z. 192 erwähnt den Einschub nicht. |
| GB-21 | echt | S. 11, Z. 209 bis 210, S. 9, Z. 177 und 179 bis 180, S. 15, Z. 308 bis 309, 313 und 320 verwenden unterschiedliche Bezeichnungen, Tab. 1 nennt "discontinuities" und "potential discontinuities" ohne Zuordnung. |
| GB-22 | echt | Zitate S. 11, Z. 220 und Z. 232 bis 233 wörtlich; ein Abgleich der Geschwindigkeitsspitzen mit Kontaktereignissen fehlt, S. 16, Z. 331 nennt eine Flugphase. |
| GB-23 | echt | In Fig5 (a) auf S. 12 folgt auf den roten Marker bei etwa 243 m/13,0 m/s ein höherer unmarkierter Punkt bei etwa 262 m/13,4 m/s, auf den roten bei etwa 463 m/4,2 m/s höhere Punkte, und der letzte Punkt liegt unter 0 m/s. |
| GB-24 | echt | Bezeichnungen S. 1, Z. 23, S. 11, Z. 221, 225, 227, 234 und S. 25, Z. 474 bis 475 wörtlich; Achsen "Travel distance (m)" in Fig5 (a), Fig10 (b), Fig1, "Travel Displacement (m)" in Fig5 (b) bis (f). |
| GB-25 | echt | S. 11, Z. 233 bis 234 nennt 1,139 ohne Bezugsmenge, Fig5 (d) zeigt einige Dutzend Marker, die gemessenen Werte in Fig10 (b) (S. 23) summieren sich auf etwa 1215, davon rund 595 in 2200 bis 2500 m. |
| GB-26 | echt | Die Kurve in Fig5 (b) bis (f) auf S. 12 erreicht etwa 45 m/s bei rund 250 m, die Farbskalen in Fig7 und S. 16, Z. 330 enden bei 31,6 m/s, und Fig8 zeigt KE 1570 GJ bei 12,4 s und 1657 GJ bei 13,6 s. |
| GB-27 | echt | Zitat S. 13, Z. 253 bis 255 wörtlich, Fig8 startet bei etwa 6500 GJ und Fig9 erreicht je Block PE = 0; h0 aus Fig9 und Tab. 2 ergibt 29,8 bis 315,3 m, Bezugsniveau 101,9 bis 711,5 m, r = minus 0,70. |
| GB-28 | echt | Fig6 auf S. 14 beschriftet von oben "Top", "Lower middle part", "Upper middle part", "Bottom", während Tab. 2 (S. 13) lower middle bei z = 465 bis 498 m und upper middle bei z = 660 bis 692 m führt; Punkte ohne Nummern, Achsen ohne Einheit. |
| GB-29 | echt | Zitate S. 13, Z. 257 und S. 11, Z. 221 wörtlich, keine Auswahlregel; Summe der Tab.-2-Volumina 11512,7 m³ = 3,6 % von 317563 m³. |
| GB-30 | echt | Zitat S. 13, Z. 265 bis 266 wörtlich, außer den Fotos in Fig7 (o) werden keine Felddaten berichtet, Konklusionen 2 bis 5 (S. 25 bis 26) beruhen auf der Simulation. |
| GB-31 | teilweise echt | Alle aufgeführten Bezeichnungen stehen an den genannten Stellen (S. 3, Z. 88 bis 89; S. 14, Z. 269 bis 278; S. 23, Z. 427 und 429; S. 24, Z. 438, 449, 452; S. 25, Z. 458; S. 26, Z. 491), nicht zutreffend ist die Zahl "seven", die Aufzählung im Befund selbst enthält acht Namen. |
| GB-32 | echt | "volume swelling"/"area growth" S. 14, Z. 275 und S. 15, Z. 288, Fig1, Fig12-Achsen, dagegen "volume expansion rate"/"(surface) area growth rate" S. 1, Z. 25, S. 3, Z. 89, S. 24, Z. 441, S. 25, Z. 453, und Bildunterschrift Z. 458 bis 459 "as a function of volume/area". |
| GB-33 | echt | Zitat S. 14, Z. 278 bis 279 wörtlich, V0, S0, Vt, St werden nirgends beziffert, Fig12 endet bei etwa 1250 % VS und 4280 % AG. |
| GB-34 | echt | Zitat S. 14, Z. 282 bis 284 wörtlich, keine Einheit oder Konvention für α und kein Sensitivitätstest. |
| GB-35 | echt | S. 13, Z. 258 bis 259 und Z. 262 bis 263 kündigen Unbalanced Force und Spannungs- sowie Verschiebungsverläufe an, Sect. 3.1 (S. 15 bis 16) berichtet nur Geschwindigkeiten, Reichweite und Interpretation der Spannungskarten fehlen. |
| GB-36 | echt | Zitat S. 15, Z. 301 bis 302 wörtlich, die Panels (h) bis (n) auf S. 18 sind Vertikalschnitte mit Achsen 0 bis 2700 und 0 bis 1200 ohne Größe und Einheit, Spannungskomponente nicht genannt. |
| GB-37 | echt | Fig7 (h) auf S. 18 ist einheitlich rot bei Skala "0" bis "0Mpa", (i) reicht bis minus 33 MPa, ρgh = 2700×9,81×1200 = 31,8 MPa, und Fig7 (a) ist rot, während 0 m/s in (b) bis (g) blau ist; Zitate S. 15, Z. 304 bis 305 und S. 10, Z. 199 bis 200. |
| GB-38 | echt | Zitate S. 15, Z. 308 bis 309 und Z. 316 bis 318 wörtlich, Tab. 2 nennt nur Verschiebung, Geschwindigkeit und Spannung, keine Beschleunigungs- oder PGA-Ausgaben. |
| GB-39 | echt | Zitate S. 16, Z. 353 bis 354 und S. 25, Z. 471 bis 472 wörtlich, Z. 359 sagt "support", Z. 469 nennt "geological structures" trotz S. 9, Z. 176 bis 177, und für die Simulation werden keine Maße angegeben. |
| GB-40 | echt | Der Kamm in Fig7 (h) auf S. 18 liegt deutlich über dem Tick 1200 bei rund 1400, S. 9, Z. 182 nennt 1121 m Modellhöhe. |
| GB-41 | echt | Fig7 (o) auf S. 19 hat weder Maßstab noch Blickrichtung, Fotodatum oder Quelle, Bildunterschrift Z. 369 bis 370. |
| GB-42 | echt | Mit Gl. (1) und (4) (S. 12, Z. 245, S. 13, Z. 249) ist KE+PE+DE identisch ME(t0) (100000 von 100000 Zufallszuständen), das Fig8-Total misst 6497 bis 6516 GJ, die Fig9-Totale sind je Block konstant, und die Zitate S. 19, Z. 375 bis 377, Z. 388 bis 389, S. 20, Z. 393 bis 394 stehen wörtlich. |
| GB-43 | echt | Zitate S. 20, Z. 399 bis 400 und S. 25, Z. 466 bis 467 wörtlich, in Sect. 2.1 und 2.3 fehlen diese Einschränkungen. |
| GB-44 | echt | Zitate S. 22, Z. 414 bis 415 und S. 26, Z. 484 bis 485 wörtlich, es gibt keine Ergebnisse je Positionsgruppe, und Fig10 (b) zeigt fünf Rückgänge (700/800, 900/1000, 1200/1300, 2300/2400, 2400/2500 m) gegen "rises continuously" (Z. 419). |
| GB-45 | echt | In Fig10 (b) auf S. 23 ist die rote Kurve unbenannt, die Klassenbreite von 100 m nicht angegeben, die Achsbeschriftung von (a) winzig; Bildunterschrift Z. 423 bis 424. |
| GB-46 | echt | S. 23, Z. 427 nennt 10 Zeitpunkte, Fig11 zeigt zehn Hüllen, jede Kurve in Fig12 auf S. 25 trägt deutlich mehr als 20 Marker. |
| GB-47 | echt | Zitate S. 24, Z. 448 bis 450 und S. 25, Z. 454 wörtlich, kein Bruchmaß berichtet, VS etwa 1249 % (Faktor 13,5) und AG etwa 4281 % (Faktor 43,8), 1116,8/6503 = 17,2 %. |
| GB-48 | echt | Fig12 markiert 1116,8 GJ, das Maximum in Fig8 misst 1657 GJ bei 13,6 s (48,4 % höher), Zitat S. 24, Z. 452 bis S. 25, Z. 455 wörtlich. |
| GB-49 | echt | Zitate S. 25, Z. 465 und Z. 467 bis 468 wörtlich, die Methoden S. 6, Z. 139 bis 140 und S. 7, Z. 157 nennen nur Begradigung entlang der Nachbarhänge ohne Gleichung und ohne Vergleichsfläche. |
| GB-50 | echt | Zitat S. 26, Z. 505 bis 506 wörtlich, Code-Erklärung Z. 494 bis 495 gleichlautend, kein Link, kein Anhang, keine Begründung. |
| GB-51 | echt | Von 31 Einträgen (S. 26 bis 29) sind 15 zitiert und 16 nicht (16/31 = 51,6 %), die beiden zitierten Einträge Ge, Y. et al. und Wu, J. et al. stehen wörtlich S. 27, Z. 540 und S. 28, Z. 588. |
| GB-52 | echt | Die Einträge Bernardie (S. 26), Dahal (S. 27), Nava, Sinčić (S. 28) und Zhang, K. (S. 29) haben als dunkelsten Wert Grau 34 statt 0 und uneinheitlichen rechten Rand, S. 27, Z. 530 kürzt mit "et al.", acht Titel in Title Case. |
| KK-01 | echt | "dissipation energy" steht S. 1, Z. 21 und S. 3, Z. 84, sonst "dissipated energy" (S. 12, Z. 242). |
| KK-02 | echt | Schreibweisen S. 1, Z. 23, S. 3, Z. 88 bis 89, S. 14, Z. 272 und 281, S. 23, Z. 426 wie angegeben. |
| KK-03 | echt | "; For some blocks" S. 1, Z. 27 und "; Compared with" S. 1, Z. 28 mit Großbuchstaben nach Semikolon. |
| KK-04 | echt | S. 1, Z. 32 lautet "Landslide is a common and widespread geological disaster". |
| KK-05 | echt | "high-level rock landslides" S. 1, Z. 33 und "high-level rock landslide" S. 2, Z. 39 bis 40, Titel und Z. 73 sagen "high-altitude". |
| KK-06 | echt | S. 1, Z. 34 bis 35 "such as donghekou landslide" kleingeschrieben ohne Artikel. |
| KK-07 | echt | "Fan et al., 2019a" S. 1, Z. 34 und "Fan et al., 2019" S. 2, Z. 56 bis 57, zwei Einträge 2019 ohne Buchstaben S. 27, Z. 530 bis 536. |
| KK-08 | echt | "Wang, 2021" S. 1, Z. 36, der Eintrag S. 28, Z. 581 bis 584 hat sieben Autoren. |
| KK-09 | echt | "Tian et al., 2017" S. 1, Z. 37, Eintrag S. 28, Z. 575 bis 577 mit Jahr 2016. |
| KK-10 | echt | Die Wendung "For landslides that have not occurred too far away" steht S. 2, Z. 42 bis 43. |
| KK-11 | echt | "UAV impact" steht S. 2, Z. 44. |
| KK-12 | echt | "Zhang et al., 2024" S. 2, Z. 45 bis 46, einziger passender Eintrag Zhang, J. et al. 2023 S. 29, Z. 594 bis 596. |
| KK-13 | echt | "Song at al.2017" steht S. 2, Z. 46. |
| KK-14 | echt | "Cheng 2014" S. 2, Z. 48 bis 49, Eintrag "Cheng, F., and Yu-Sheng, L." S. 27, Z. 521. |
| KK-15 | echt | "Zhao et al., 2020" S. 2, Z. 57, Eintrag S. 29, Z. 600 bis 602 mit 2021. |
| KK-16 | echt | S. 2 bis 3, Z. 76 bis 77 "three parts", es folgen (1) bis (4), Fig1 zeigt vier Stufen. |
| KK-17 | echt | S. 3, Z. 77 "(1) surface terrain restoration", Fig1 und Überschrift S. 5, Z. 92 "Geo-mechanical model building". |
| KK-18 | echt | Fig1 (S. 4) schreibt P0E, PtE, KtE mit tiefgestelltem Index zwischen P bzw. K und E. |
| KK-19 | echt | "colluvial Deluvial deposit" steht zweimal S. 5, Z. 105. |
| KK-20 | echt | Legende von Fig2 (b) auf S. 6 lautet "Daduhe River". |
| KK-21 | echt | Der Satz S. 10, Z. 193 bis 195 hat in der zitierten Form keinen tragenden Hauptsatz. |
| KK-22 | echt | Tabellentitel S. 11, Z. 213 "Table 1 Physical ..." ohne Doppelpunkt, Tab. 2 (S. 13, Z. 267) mit Doppelpunkt. |
| KK-23 | echt | Legende Fig5 (a) auf S. 12 lautet "Non-obvios acceleration". |
| KK-24 | echt | S. 13, Z. 246 nennt nur PE(ti) und DE(ti), KE(ti) fehlt. |
| KK-25 | echt | Tab. 2 auf S. 13 enthält Zeile ID 11 "Maximum unbalanced force" unter dem Titel Z. 267 "blocks where the 10 monitoring points are located". |
| KK-26 | echt | Farbskalen Fig7 (h) bis (n) auf S. 18 lauten "0Mpa", "-33Mpa", "-31Mpa", "-47Mpa". |
| KK-27 | echt | S. 20, Z. 397 bis 398 "exhibit a rebound in potential energy after it approaches zero" mit Singular "it" für mehrere Blöcke. |
| KK-28 | echt | Überschrift S. 23, Z. 425 lautet "3.4", auf 3.2.2 folgt kein Abschnitt 3.3. |
| KK-29 | echt | Bildunterschrift S. 24, Z. 438 "(a-i)" bei zehn Panels (a) bis (j) und zehn Zeiten. |
| KK-30 | echt | S. 24, Z. 440 "surface area (A)", Gl. (6) auf S. 14 verwendet S0 und St. |
| KK-31 | echt | S. 25, Z. 464 "that:(a) Outside" und Z. 466 "contours;(b) The" ohne Leerzeichen. |
| KK-32 | echt | S. 26, Z. 494 lautet "The codes that support the findings". |
| KK-33 | echt | S. 26, Z. 499 trennt "XF: ... Investigation. LZ:" mit Punkt statt Semikolon. |
| KK-34 | echt | Überschrift S. 26, Z. 507 lautet "Reference". |
| KK-35 | echt | Gedehnte Wortabstände vor zeilenendender DOI in S. 27, Z. 535, 541, 551, S. 28, Z. 560, 583, 589 und S. 29, Z. 601. |

## 2. Literaturvorschläge: bereits im Literaturverzeichnis?

| Vorschlag | Kennung | Im Verzeichnis |
|---|---|---|
| von Wartburg et al. (2020), Front. Earth Sci. 8, 164 | GB-03 | nein |
| Hibert et al. (2011), J. Geophys. Res. 116, F04032 | GB-07 | nein |
| Farin et al. (2015), J. Geophys. Res. Solid Earth 120, 7102-7137 | GB-07 | nein |
| Lin et al. (2022), Nat. Hazards Earth Syst. Sci. 22, 639-657 | GB-07 | nein |
| Ge et al. (2021), Landslides 18, 3559-3576 | GB-07, GB-51 | ja (S. 27, Z. 540 bis 542, unzitiert) |
| Chang et al. (2022), Landslides 19, 1463-1478 | GB-07 | ja (S. 26, Z. 514 bis 516, unzitiert) |
| He, J. et al. (2023), Landslides 21, 621-640 | GB-10 | ja (S. 27, Z. 546 bis 548, unzitiert) |
| Wu, J. et al. (2013), J. Geol. Soc. India 82 | GB-51 | ja (S. 28, Z. 588 bis 590, unzitiert) |
| Zhao, B. et al. (2021), Nat. Hazards 106 | GB-51 | ja (S. 29, Z. 600 bis 602, als 2020 zitiert) |
| Zhou et al. (2024), J. Earth Sci. 35 | GB-51 | ja (S. 29, Z. 603 bis 605, unzitiert) |

## 3. Doppelungen

Keine zwei Kennungen haben denselben Fundort und denselben Kerngegenstand. Teilüberschneidungen in Unterpunkten, jeweils mit unterschiedlichem Kerngegenstand:

| Paar oder Gruppe | Gemeinsamer Unterpunkt |
|---|---|
| GB-17 / GB-20 | fehlende Zeitachse und PGA im Einschub von Fig4 (S. 10) |
| GB-17 / GB-18 / GB-19 | fehlende Angaben zu Komponente, PGA, Aufbereitung des Luding-Signals (S. 10, Z. 189 bis 191) |
| GB-25 / GB-45 | unklare Grundgesamtheit von "Frequency" in Fig10 (b) (S. 23) |
| GB-52 / KK-35 | uneinheitliche Ausrichtung des Literaturverzeichnisses (S. 26 bis 29) |

## 4. Fundorte

Geprüft wurde je Kennung der zuerst genannte Fundort und die Stelle des Zitats an den gedruckten Randnummern.

| Kategorie | Anzahl |
|---|---|
| genau | 87 |
| um 1 bis 2 Zeilen daneben | 0 |
| weiter daneben | 0 |

Anmerkung: Bei KK-10 beginnt die Wendung mit "For" am Ende von Z. 42, der Hauptteil steht in der angegebenen Z. 43; gezählt als genau.

## 5. Zählungen

| Urteil | Anzahl |
|---|---|
| echt | 86 |
| teilweise echt | 1 |
| falsch | 0 |
| nicht prüfbar | 0 |
| gesamt | 87 (52 GB, 35 KK) |

Literaturvorschläge: 10, davon im Verzeichnis ja 6, nein 4.
Doppelungen (gleicher Fundort und Gegenstand): 0; Teilüberschneidungen in Unterpunkten: 4.
Fundorte: genau 87, um 1 bis 2 Zeilen daneben 0, weiter daneben 0.

Nicht selbst lesbare Einzelangaben (Kernaussage dennoch belegt): Song et al. (2017), Abgleich mit GPS-Monitoring (nur Titel); Li et al. (2024), Software GeoStudio (nur Abstract).
