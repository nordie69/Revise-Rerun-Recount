# Verifikation des Gutachtens zu egusphere-2025-4733

Grundlage: Manuskript-PDF (Seitenbilder neu gerendert mit 200 und 300 dpi), text.json als Hilfe, Zeilennummern an den gedruckten Randnummern bestätigt. Messungen an Abbildungen mit Python (Pixelkalibrierung an Gitterlinien und Achsenticks). Literatur über WebSearch und WebFetch (PMC, Eos, DOAJ).

## Urteile je Kennung

| Kennung | Urteil | Beleg (ein Satz mit Seite und Zeile) |
|---|---|---|
| GB-01 | echt | Zitat steht S. 1, Z. 22; Brixel et al. (2020) fehlt im Literaturverzeichnis (S. 29 bis 33, Brixel nur als Koautor von Amann et al. 2018, S. 29, Z. 558), und der Eos-Highlight bestätigt 10⁻¹³ bis 10⁻²¹ m² nahe dem Kern sowie Vorrang von Geometrie und Topologie vor den Spannungen (Volltext nicht gelesen). |
| GB-02 | echt | Zitate S. 1, Z. 28 und S. 10, Z. 207 wörtlich; FWS-Vp 5,05 km/s (S. 13, Z. 296), Kern-Vp 2,49 bis 4,08 km/s (S. 18, Z. 386 bis 387), Porositäten 0,51 bis 14,74 % (S. 13, Z. 317) und 0,7 bis 6,3 % (S. 18, Z. 382) werden in Kap. 5 und 6 nicht skalenübergreifend verglichen. |
| GB-03 | echt | Text S. 3, Z. 87 "TM 5218", Abb. 1b (S. 4) "Furka Tunnel TM5221", Abb. 1a und Abb. 3 "Piz Rotondo", Bildunterschrift "Pizzo Rotondo"; Farb- und Namensabweichungen der Panels sowie fehlende Auflösung von BULGG und FEAR in der Bildunterschrift bestätigt (Nebenangabe zu Rast et al. 2022 an der Quelle nicht auffindbar). |
| GB-04 | echt | S. 5, Z. 117 nennt σHmax 20,4 bis 27,9 und σhmin 11,2 bis 16,4 MPa; Bröker und Ma (2022, PMC9072525) geben Sv ≈ 26,5, S3 14,6 ± 1,4, Mittelwerte 11,1 bis 16,4 MPa und keine SHmax-Größe; Abb. 2 (S. 6) zeigt Sv ≈ 30, SHmax 25,4 ± 2,3, Shmin 14,6 ± 1,4 MPa (3,5/26,5 = 13,2 %). |
| GB-05 | echt | S. 5, Z. 120 bis 121 "occur throughout all intersecting boreholes" gegen S. 7, Z. 134 "F2 is missing in BO6" und S. 15, Z. 327. |
| GB-06 | echt | Definition S. 5, Z. 126; P10-Balken Abb. 7 (S. 16) für 29 bis 33 m gemessen 4, 6, 9, 7 je m, offene Klüfte 4, 1, 5 je m in 29 bis 32 m, F0-Zone ab etwa 28,9 m. |
| GB-07 | echt | Abb. 2 (S. 6): Legende erklärt nur Fazies und Klufttypen, nicht Intervallbalken, rote und blaue Dreiecke, Projektion und konturierte Kleinstereonetze. |
| GB-08 | echt | Stichprobe Abb. 2 (S. 6): Versalhöhe "OPTV" etwa 15 px bei 300 dpi, also rund 5 pt Schriftgrad, unter 6 pt; übrige Einzelwerte nicht jeweils nachgemessen. |
| GB-09 | echt | Ankündigung S. 7, Z. 153 bis 155; Kap. 5.1 (S. 18, Z. 392 bis 399) vergleicht nur gepoolt; Plug 43.35-43.39 m in Abb. 8d (S. 17) bei etwa 3e-13 m², Median des Intervalls bei 43,37 m in Abb. 6 (S. 14) gemessen 1,45e-13 m². |
| GB-10 | echt | Abb. 3 (S. 8) zeigt BO7, "~65", Fragezeichen, gestrichelte Kästen und rosa Band ohne Legende; BO7 kommt im Text nicht vor. |
| GB-11 | echt | S. 8, Z. 181 bis 183 wörtlich; mit S. 5, Z. 117 und Porendrücken 0,70 bis 3,64 MPa (Abb. 6, 7) ergibt Python 7,56 bis 15,7, 16,76 bis 27,2, 22,86 bis 25,8 (26,36 bis 29,3) MPa, 32 minus 29,3 = 2,7 MPa; Faktor 6,7 für 38.49-38.53 m in Abb. 8c bestätigt. |
| GB-12 | echt | Abb. 4a (S. 9) enthält "Helium supply" und "reference cell pressure transducer" (Vref), Text S. 8, Z. 176 nennt nur Wasser; Panels b und c ohne Probenangabe. |
| GB-13 | echt | S. 9, Z. 190 bis 200, S. 11, Z. 249 bis 251 und S. 12, Z. 275 bis 280 nennen keine der aufgezählten Parameter. |
| GB-14 | echt | S. 10, Z. 230 "(in BO5, only Vp was measured)" gegen S. 13, Z. 294 bis 295 (Vs 2,79 km/s), Abb. 6 mit Vp und Vs, Abb. 7 nur Vp. |
| GB-15 | echt | S. 10, Z. 231 bis 235 ohne Vp-Einheit, Herkunft von α und β, Korndichte und Porositätsgleichung; Gleichung (2) schreibt "p". |
| GB-16 | echt | Gleichung (2) S. 10, Z. 235, Gleichung (1) S. 12 über Z. 270. |
| GB-17 | echt | S. 11, Z. 261 bis 267 und S. 15, Z. 346 bis 350: keine Daten zur zweiten Kampagne, kein Abstand r, kein Überwachungsintervall in BO6 für den ersten Test; 29,7 minus 26,0 = 3,7 m gegen "interval size was 2.4 m" (Z. 347). |
| GB-18 | echt | Abb. 5 (S. 12): Panel b Achse etwa 3,25 bis 4,0 MPa, Panel e "Pressure (kPa)" etwa 330 bis 410, Verhältnis rund 9,8 entspricht m Wassersäule; Panel d "Hydraulic head (m)" 340 bis 410. |
| GB-19 | echt | Haupttext verweist nur auf A1 und A2 (S. 18, Z. 383, 388); A4 (S. 27) Bildunterschrift "four samples", Tabelle fünf Proben, 41.31-41.35 m ohne Bild, "43.35-43.38 m"; A3 (S. 26) "quartzolit". |
| GB-20 | echt | Boxpositionen Abb. 6 gemessen 37,77, 38,37, 39,47, 40,07, 42,03, 43,37, 45,58 m, Abb. 7 24,95, 27,84, 28,45, 29,05 m; Abweichungen zu Abb. 11 (S. 21) mit Python 0,64 bis 0,70 m (BO5) und 0,53, -0,07, -0,07, -0,09 m (BO6); Mittelwerte im Text nur für Intervalle 2, 3, 5, 7 (S. 13, Z. 300 bis 313). |
| GB-21 | echt | Abb. 7 (S. 16) Intervall 1 gemessen Q1 2,95e-14, Median 4,35e-14, Q3 4,27e-13, Ausreißer 1,15e-12 m²; Untergrenzen arithmetisch 1,30e-13 und geometrisch 5,8e-14 m² liegen über 3,4e-14 (S. 15, Z. 333). |
| GB-22 | echt | S. 13, Z. 308 bis 309 "all other intervals contain" gegen Z. 311 bis 313 (Intervall 7); Satz Z. 311 endet auf "due."; Mediane Abb. 6 gemessen 1,45e-13 (Intervall 6) und 3,2e-14 m² (Intervall 5). |
| GB-23 | echt | Abb. 6 Kaliberachse 12.1 bis 25, Abb. 7 13.8 bis 29 mm, Legenden "ms⁻¹", keine Fazieslegende in beiden Abbildungen. |
| GB-24 | echt | S. 15, Z. 327, 333 bis 334, 340 bis 342 gegen Abb. 7: F4 nur über dem Kern, Intervall 2 bei 27,84 m in F1/F4, Kernintervall Porendruck etwa 1,7 MPa statt 2, höchste Injektivität an der F1/F4-Grenze bei 27,8 m. |
| GB-25 | echt | P10 aus Abb. 6 und 7 abgelesen: BO5 34 bis 47 m Mittel 3,62 je m, BO6 24 bis 33 m 7,11 je m, Verhältnis 1,96; Zitat S. 15, Z. 337. |
| GB-26 | echt | Abb. 8c (S. 17) Maximum etwa 4,6e-17 und Minimum etwa 4,1e-19 m² gegen 3,5e-17 und 4,0e-18 (Z. 371); 8d etwa 3,0e-13 gegen 2,0e-13 (S. 18, Z. 374); 8a Minimum etwa 2,16e-19 gegen 2,0e-19 (Z. 363); Bildteile, "7e10−18", Überlappung 37.50/37.53 und fehlende Einheit Z. 370 bestätigt. |
| GB-27 | echt | Verhältnisse 15/32 MPa aus Abb. 8 gemessen: 41.52 m 2,8; 37.50 m 1,8; 38.58 m 1,74; 37.53 m 2,3; 38.49 m 6,9; 43.35 m 1,0; 43.40 m 5,3; Zitat S. 18, Z. 376. |
| GB-28 | echt | Abb. A2b (S. 25): He 2,80, 2,66, 9,37, 4,04 %, WIP 1,78, 1,46, 6,26, 3,95 %, WIP/He 0,55 bis 0,98, vier Plugs; Zitat S. 18, Z. 385. |
| GB-29 | echt | S. 18, Z. 387 "43.40-43.50 m" gegen "43.30-43.50 m" in A1, A2c, A3; A2-Legenden "38.49-35.53 m" und "38.40-35.55 m"; A2a Kern-Vp etwa 4420 und 2420 m/s gegen 4080 in A2c. |
| GB-30 | echt | Hunt (2003), Lützenkirchen und Loew (2011), Masset und Loew (2010), Ofterdinger (2001) zitiert S. 19, Z. 404 und 412 bis 413, fehlen im Verzeichnis (69 Einträge gezählt); Abb. 10 Legende "Lützenkirchen 2002", Quadrate und Schema nicht erklärt. |
| GB-31 | echt | Abb. 9 (S. 19) N = 63, 42, 84, 6 bei 3, 2, 4, 2 Plugs mal 3 Stufen ergibt 7, 7, 7, 1; Feld-N 14, 10, 11, 8 = 43; keine F0-Kurve. |
| GB-32 | echt | S. 15, Z. 346 bis 350 und S. 20, Z. 425 bis 426: Injektion 43,2 bis 45,6 m außerhalb des Kerns, 3,9/1,6 = 2,4, Kernabstand mit Python 15,1 m; Abb. 11 zeichnet den orangen Pfeil durch den Kern. |
| GB-33 | echt | Kap. 4 nennt keine Fließdimension, S. 20, Z. 430 bis 432 erst in der Diskussion; Abb. 11 zeigt 10 Boxplots (Einzelmediane nicht nachgemessen). |
| GB-34 | echt | Abb. 11 (S. 21): alle neun BO5-Paare ergeben mit Python 0,8772 (28,7°), 40/cos 29,5° = 45,96 m; BO6 "30 (30.84)" gegen 30,49 m bei 10,3°. |
| GB-35 | echt | S. 22, Z. 451 bis 454 gegen Abb. 6 (3,6 und 3,5 gegen 0,7 MPa) und Abb. 7 (Kern etwa 1,7 gegen 2,0 und 2,0 MPa). |
| GB-36 | echt | S. 23, Z. 465 bis 467 wörtlich; Konnektivität ist in Kap. 3 und 4 nicht gemessen, Kap. 5.1 stützt sie auf Davy et al. (2023) (S. 19, Z. 411). |
| GB-37 | echt | S. 23, Z. 473 bis 474 wörtlich; kein Ergebnis betrifft die andere Tunnelseite. |
| GB-38 | echt | S. 28, Z. 528 "Python codes can be provided upon email request" und Z. 530 eine Zenodo-DOI ohne Inhaltsangabe. |
| GB-39 | echt | S. 29, Z. 564 bis 565 (Berger ohne Verlag) und Z. 579 ("Geol"), S. 31, Z. 636 und 654, S. 32, Z. 678, S. 33, Z. 698 bis 704 ("40 Ar/39 Ar" gegen "40Ar/39Ar", SNL ohne URL). |
| KK-01 | echt | S. 1, Z. 25 wörtlich. |
| KK-02 | echt | S. 2, Z. 35 wörtlich. |
| KK-03 | echt | S. 3, Z. 88 wörtlich. |
| KK-04 | echt | S. 11, Z. 252 "transmissivity (m s-2)". |
| KK-05 | echt | S. 11, Z. 254 im Seitenbild "(m  s-1)" ohne sichtbare Hochzahl 2. |
| KK-06 | echt | S. 11, Z. 255 im Seitenbild "(m )". |
| KK-07 | echt | S. 11, Z. 257 "1 mPa s-1". |
| KK-08 | echt | S. 13, Z. 293 "poor tool eccentricity". |
| KK-09 | echt | S. 13, Z. 299 ").The fault" ohne Leerzeichen. |
| KK-10 | echt | S. 13, Z. 304 mit sichtbarem Einzug. |
| KK-11 | echt | S. 14, Z. 323 "m3 s-1 MPa." ohne Hochzahl -1. |
| KK-12 | echt | S. 18, Z. 394 im Seitenbild "m" statt m². |
| KK-13 | echt | S. 18, Z. 395 im Seitenbild "m" statt m². |
| KK-14 | echt | S. 19, Z. 415 im Seitenbild "m" statt m². |
| KK-15 | echt | S. 20, Z. 428 "Caine's (1996)". |
| KK-16 | echt | S. 21, Z. 444 "at the same showing". |
| KK-17 | echt | S. 23, Z. 479 bis 480 wörtlich. |
| KK-18 | echt | S. 28, Z. 533 bis 534 "M.A. M; resources", erneut Z. 535. |
| KK-19 | echt | S. 29, Z. 554 bis 557 zitiert den Preprint; DOAJ bestätigt Solid Earth 15, 1087-1112, 2024, doi 10.5194/se-15-1087-2024. |

## Literaturvorschläge

| Vorschlag | Kennung | Bereits im Literaturverzeichnis |
|---|---|---|
| Brixel et al. (2020), JGR Solid Earth, e2019JB018200 | GB-01 | nein |
| Achtziger-Zupančič et al. (2024), Solid Earth 15, 1087-1112 | KK-19 | ja (als Preprint egusphere-2024-586, S. 29, Z. 554 bis 557) |

## Doppelungen

Keine Kennungspaare mit gleichem Fundort und gleichem Gegenstand. Teilüberschneidungen ohne Doppelung: GB-24 und GB-35 (beide stützen sich auf den BO6-Kerndruck S. 15, Z. 340, Gegenstand einmal Zahlenwert, einmal Kompartimentierungsdeutung); GB-19 und GB-08 (Achsen von Abb. A4 als Nebenpunkt).

## Fundorte

Geprüft 58 Kennungen. Genau: 58. Um 1 bis 2 Zeilen daneben: 0. Weiter daneben: 0.

## Zählungen

| Urteil | Anzahl |
|---|---|
| echt | 58 (39 GB, 19 KK) |
| teilweise echt | 0 |
| falsch | 0 |
| nicht prüfbar | 0 |
| Literaturvorschläge bereits im Verzeichnis: ja | 1 |
| Literaturvorschläge bereits im Verzeichnis: nein | 1 |
| Doppelungen | 0 |
| Fundorte genau | 58 |
| Fundorte 1 bis 2 Zeilen daneben | 0 |
| Fundorte weiter daneben | 0 |
