# Verifikation des Gutachtens zu egusphere-2025-4733

Prüfgrundlage: PDF, Seitenbilder in seiten/ (150 dpi) und eigene 300-dpi-Renderings, text.json nur als Suchhilfe. Zeilennummern an den gedruckten Randnummern bestätigt. Rechnungen mit Python. Literatur über WebSearch und WebFetch, soweit lesbar.

Fundortregel: genau, wenn die zitierte Stelle vollständig im angegebenen Zeilenbereich liegt und die erste angegebene Zeile zur Stelle oder zu ihrem Satz gehört; daneben, wenn die erste angegebene Zeile eine Leerzeile oder ein fremder Satz ist.

## 1. Urteile je Kennung

| Kennung | Urteil | Beleg |
|---|---|---|
| GB-01 | echt | Brixel steht im Literaturverzeichnis nur als Mitautor von Amann et al. 2018 (S. 29, Z. 558); Brixel et al. 2020a ist an der Quelle (Eos-Hinweis) mit dem genannten Inhalt bestätigt, 2020b war nicht lesbar. |
| GB-02 | echt | Zitate S. 1, Z. 24 bis 25 und S. 2, Z. 65 bis 66 wörtlich; keine Forschungsfrage, S. 23, Z. 474 bis 482 nennt kein ausgewähltes Intervall. |
| GB-03 | echt | Zitat S. 2, Z. 40 bis 41 wörtlich; Mizrahi et al. 2024 (USGS-Abstract) enthält "remains impossible" und OEF in Italien, Neuseeland, USA; Navarro-Rodríguez et al. 2025 ist eine Frühwarn-Übersicht mit Prognoseaussage nur in der Einleitung mit Fremdbeleg. |
| GB-04 | echt | Zitat S. 2, Z. 47 bis 48; Cappa et al. 2018 behandelt das In-situ-Experiment "at 282-m depth into a natural fault" (Autorenfassung gelesen), nicht ein Labor im cm bis dm Bereich. |
| GB-05 | teilweise echt | Zitat S. 2, Z. 50 bis 52 wörtlich und der Kern hält, aber der Satz "intersects a relatively transmissive fault near the bottom at 3.5 km" stammt aus Evans, Genter und Sausse 2005 (JGR 110), nicht aus dem zitierten Evans et al. 2004, dessen Titel 3 km nennt (S. 30, Z. 613 bis 616); die Faktoren 3,5 und 1000/282 = 3,5 sind rechnerisch richtig. |
| GB-06 | echt | Zitat S. 2, Z. 53; Ma et al. 2022 nennen "average overburden of 1000 m" und Maximum "∼ 1632 m" (Quelle gelesen), 1632 minus 1500 = 132. |
| GB-07 | echt | S. 3, Z. 87 "TM 5218" mit Leerzeichen, Abb. 1 (b) S. 4 "Furka Tunnel TM5221". |
| GB-08 | echt | BULGG, BO7, FEAR1, FEAR2, stim1 bis stim3 nur in Abb. 1 und 3 (S. 4, S. 8), SPP nur in den Legenden von Abb. 6 und 7, Textsuche ohne Treffer; Streifengneiss und Penninic units beide weiß. |
| GB-09 | echt | Beschriftungen wie "Plunge +12" in Abb. 1 (b) S. 4 und die Achsenzahlen der CT-Bilder in Abb. A4 S. 27 sind am 300-dpi-Bild deutlich unter 6 pt; die einzelnen pt-Werte wurden nicht nachgemessen. |
| GB-10 | teilweise echt | Text S. 5, Z. 117 gibt 26,5 MPa, Abb. 2 S. 6 "Sv ≈ 30 MPa", 25,4 ± 2,3 und 14,6 ± 1,4 MPa (3,5/26,5 = 13,2 %), aber die Abbildung schreibt "Shmin", nicht "min" ohne h. |
| GB-11 | echt | Zählung mit Python: 7 Treffer F0 bis F4, davon nach der Definition nur S. 7, Z. 134; 9 mal "Facies n"; 13 Zahlwortformen; "zero or one" S. 20, Z. 435. |
| GB-12 | teilweise echt | Definitionen S. 5, Z. 126 bis 127 wörtlich, BO5 bei 40,5 bis 43 m nur offene Klüfte (Abb. 6, S. 14) und in BO6 drei von fünf Klassen über 5 je m (Abb. 7, S. 16), aber die Klasse bei 33 bis 34 m misst 4,0 je m, nicht 1,8. |
| GB-13 | echt | Legenden von Abb. 2 (S. 6), 9 (S. 19) und 11 (S. 21) enthalten weder Intervallbalken, Probendreiecke (10 sichtbar), Stufenhistogramme noch Faziesfelder und Boxplots. |
| GB-14 | echt | Zitat S. 8, Z. 181; 32 minus 27,9 = 4,1 MPa; mittlere effektive Spannung aus den Textbereichen 15,8 bis 22,9 MPa nachgerechnet. |
| GB-15 | echt | S. 10, Z. 230 "(in BO5, only Vp was measured)", aber S. 13, Z. 294 bis 295 und Abb. 6 (S. 14) zeigen Vs für BO5, Abb. 7 (S. 16) nur Vp. |
| GB-16 | echt | Zitate S. 10, Z. 231 bis 232 und S. 13, Z. 316 bis 317 wörtlich; Dichten 2,385, 2,630, 2,880 und Korndichten 2,890, 2,624, 2,685 nachgerechnet; SEG Wiki gibt ρ = aV^1/4 mit a = 0,31 für m/s; Gl. (2) S. 10, Z. 235 zeigt kursives p. |
| GB-17 | echt | Gardner trägt (2) auf S. 10, Z. 235, Thiem (1) auf S. 12 nach Z. 267; Thiem wird nicht mit Nummer genannt. |
| GB-18 | echt | Zitate S. 11, Z. 244 bis 245 und S. 12, Z. 279 bis 280; keine nSIGHTS-Version (S. 11, Z. 249 bis 250), "known interval thickness" S. 11, Z. 255. |
| GB-19 | echt | Zitat S. 11, Z. 259 bis 260; Abb. 6 (S. 14) zeigt Kern etwa 3,6 und 3,5 MPa, Nachbarn etwa 0,7 MPa, ohne Kennzeichnung extrapolierter Werte. |
| GB-20 | echt | S. 11, Z. 261 und S. 15, Z. 346 bis 347 wörtlich, im ganzen Text kein Kampagnendatum und kein Gerät genannt. |
| GB-21 | echt | Zitat S. 11, Z. 265 bis 267, "hydraulic head gradient" Z. 266; Abstand der Intervallmitten Test 2 nachgerechnet 15,1 m. |
| GB-22 | echt | Abb. 5 (S. 12): (e) "Pressure (kPa)" mit Werten etwa 330 bis 410, (d) Druckhöhe etwa 340 bis 406 m, (b) etwa 3,2 bis 4,0 MPa. |
| GB-23 | echt | S. 13, Z. 300 bis 302 und Z. 310 bis 311 wörtlich, Satz endet auf "due.", Werte nur für Intervalle 5 und 7 explizit. |
| GB-24 | echt | Abschnitt 4.1 (S. 13 bis 15) ohne Fließdimension; Zitat S. 20, Z. 430; Achsen in Abb. 11 (S. 21) 1,70 bis 2,00 und 1,5 bis 2,0. |
| GB-25 | echt | Permeabilitätsspalten in Abb. 6 und 7 (S. 14, S. 16) ohne Intervallnummern, Bildunterschriften ohne Boxplotdefinition; Zitat S. 13, Z. 301. |
| GB-26 | echt | Kaliberachsen 12.1 bis 25 mm und 13.8 bis 29 mm (S. 14, S. 16) gegen 96 mm in S. 5, Z. 104. |
| GB-27 | echt | Zitat S. 15, Z. 327; F4 in Abb. 7 (S. 16) bei 24,5 bis 27,2 und 27,8 bis 28,1 m, beide oberhalb F3 bei 28,4 bis 28,9 m. |
| GB-28 | echt | Zitat S. 15, Z. 333; gemessen am 300-dpi-Bild unterer Boxrand etwa 3,0 bis 3,4 × 10^-14, oberer Rand etwa 4,3 × 10^-13, Ausreißer etwa 1,2 × 10^-12; Schranken 1,23 × 10^-13 und 5,8 × 10^-14 nachgerechnet. |
| GB-29 | echt | Zitat S. 15, Z. 333 bis 335; Intervall 2 (27,49 bis 28,22 m) enthält nach Abb. 7 nur F1 (59 %) und F4 (41 %), Anteile nachgerechnet (Intervall 3: 56 % F3 statt 58 %, innerhalb der Ablesegenauigkeit). |
| GB-30 | echt | Abb. 7 (S. 16) Druckmarken gemessen 1,35, 1,96, 1,70, 1,99 MPa, Intervall 3 niedriger als Intervall 2 und 4; Zitate S. 15, Z. 334 bis 335 und 340, S. 22, Z. 453. |
| GB-31 | echt | Zitat S. 15, Z. 337 bis 338; keine Aussage zu einer Orientierungskorrektur von P10 im Methodenteil S. 10. |
| GB-32 | echt | Zitate S. 15, Z. 340 und S. 14, Z. 322 bis 323; BO5 außerhalb des Kerns 0,7 bis 1,85 MPa (Abb. 6) gegen BO6 1,37 bis 2 MPa. |
| GB-33 | echt | Zitat S. 15, Z. 347 bis 348; Längen 2,4, 2,4 und 3,7 m nachgerechnet, Beobachtungsintervall von Test 1 fehlt (Z. 348). |
| GB-34 | echt | Abb. 8 (c) S. 17 gemessen höchster F3-Wert etwa 4,4 × 10^-17, niedrigster etwa 4,2 × 10^-19 gegen 4,0 × 10^-18 in Z. 371; (d) etwa 2,9 × 10^-13 gegen 2,0 × 10^-13 in S. 18, Z. 374; S. 18, Z. 395 ohne Exponent. |
| GB-35 | echt | S. 18, Z. 382 nennt 35.19-35.23 m, nicht unter den elf Plugs (S. 17, Z. 361); Abb. A1 Facies 1 (S. 24) zeigt zehn Punkte aus fünf Kernstücken; Abb. A3 (S. 26) "(4) F3 38.70 - 38.74 m". |
| GB-36 | teilweise echt | Zitat S. 18, Z. 383 bis 385 wörtlich und F2 widerspricht der Aussage, aber in Abb. A1 Facies 2 (S. 24) liegt der Punkt bei etwa 1,06/1,06 % auf der 1:1-Linie, nicht wie behauptet alle vier darüber. |
| GB-37 | echt | Zitat S. 18, Z. 385 bis 386; Abb. A2 (b) S. 25 zeigt vier Plugs, Abb. A4 S. 27 nennt 7,97 % für 43.35-43.38 gegen 6,3 % WIP in S. 18, Z. 382. |
| GB-38 | echt | S. 18, Z. 387 "43.40-43.50 m", dagegen 43.30-43.50 m in Z. 382, Abb. A1, Abb. A2 (c) und Abb. 8 (d). |
| GB-39 | echt | Textsuche: XRD, QAP, CT nur in A.1 (S. 26, Z. 509 bis 513) und den Bildunterschriften, A3 und A4 nur in ihren eigenen Unterschriften. |
| GB-40 | echt | Bildunterschrift S. 27, Z. 520 "four samples", Tabelle mit fünf Zeilen, Bild und Tabelle "43.35-43.38". |
| GB-41 | echt | Abb. 9 (S. 19) N = 63, 42, 84, 6 und 14, 10, 11, 8; 63/9 = 42/6 = 84/12 = 7, 6/6 = 1, Summe 195 und 43 nachgerechnet. |
| GB-42 | echt | Hunt 2003, Lützenkirchen und Loew 2011, Masset und Loew 2010, Ofterdinger 2001 (S. 19, Z. 404, 412 bis 413) ohne Eintrag; 69 Einträge gezählt; Legende Abb. 10 "Lützenkirchen 2002", übrige Legendenjahre stimmen. |
| GB-43 | echt | Abb. 10 (S. 20) elf Laborbalken dieser Studie, der erste reicht am 300-dpi-Bild bis etwa 1,1 × 10^-19 m² und damit unter den tiefsten Wert in Abb. 8 von etwa 2,2 × 10^-19; Zuordnung nach Tiefe bleibt Annahme. |
| GB-44 | echt | Zitate S. 20, Z. 425 bis 426 und S. 23, Z. 469; Faziesanteile 88/12, 40/24/22/14 und 63 % sowie 1,2 × 10^-11 / 3,9 × 10^-15 = 3077 nachgerechnet. |
| GB-45 | echt | Abb. 11 (S. 21): Verhältnisse 1,0157 bis 1,0160 für die übrigen BO6-Marken, 30.84/30 = 1,028, 1/cos 10,3° = 1,0164. |
| GB-46 | echt | Zitat S. 22, Z. 452 bis 453; "hydrostatic" kommt im Text nur dort vor, kein Referenzdruck angegeben. |
| GB-47 | echt | Zitate S. 23, Z. 463 und 467 wörtlich; 2,0 × 10^-13 / 5,6 × 10^-16 = 357 und / 1,7 × 10^-15 = 118 nachgerechnet; Ausnahme nur in S. 19, Z. 415. |
| GB-48 | echt | Zitate S. 23, Z. 465 bis 467 und S. 7, Z. 153 bis 155; acht von elf Plugtiefen liegen in einem Intervall, 35.04, 41.31, 41.52 m in keinem. |
| GB-49 | echt | Zitat S. 23, Z. 473 bis 474; keine Daten von der Tunnelgegenseite, Abstand Test 2 etwa 15 m nachgerechnet. |
| GB-50 | echt | Zählung S. 18, Z. 389 bis S. 23, Z. 487: 0 mal "injectiv", "porosity", "Vp", "velocit", 1 mal "pore pressure" (S. 22, Z. 451). |
| GB-51 | echt | Zitat S. 23, Z. 478 bis 480 wörtlich, Gegenstelle S. 11, Z. 245 bis 246 und S. 15, Z. 342 bis 344. |
| GB-52 | echt | Zitat S. 23, Z. 481 bis 482; keine gleichzeitige Injektion und keine Seismizität in den Ergebnissen. |
| GB-53 | echt | Code availability S. 28 wörtlich wie zitiert; S. 11, Z. 250 bis 251 nennt eigenen Code. |
| GB-54 | echt | S. 28, Z. 530 nennt nur die DOI ohne Inhaltsangabe. |
| GB-55 | echt | S. 29, Z. 557 "1 March 2024", Z. 579 "Geol, 24, 1025", S. 31, Z. 654 "JGS", S. 33, Z. 700 "SP"; Cappa 2018 und Passelègue 2018 ohne Artikelnummer. |
| KK-01 | echt | S. 1, Z. 23 bis 24 wörtlich, "URL" nur einmal im Text. |
| KK-02 | echt | S. 1, Z. 25 wörtlich. |
| KK-03 | echt | S. 2, Z. 35 wörtlich. |
| KK-04 | echt | S. 3, Z. 88 "it be biotite-rich" am Seitenbild. |
| KK-05 | echt | Bildunterschrift Abb. 2, S. 6 wörtlich. |
| KK-06 | echt | S. 11, Z. 252 "transmissivity (m s-2)" am Seitenbild. |
| KK-07 | echt | S. 11, Z. 254 bis 255 am Seitenbild ohne Exponent bei m (text.json zeigt m²). |
| KK-08 | echt | S. 11, Z. 257 "1 mPa s-1". |
| KK-09 | echt | S. 12, Z. 275 wörtlich, "GRF" erstmals Z. 277 ohne Einführung. |
| KK-10 | echt | S. 13, Z. 299 fehlendes Leerzeichen am Seitenbild. |
| KK-11 | echt | S. 13, Z. 301 wörtlich. |
| KK-12 | echt | S. 14, Z. 323 "MPa." ohne -1, Achse von Abb. 6 mit MPa-1. |
| KK-13 | echt | S. 17, Z. 370 wörtlich. |
| KK-14 | echt | S. 18, Z. 375 wörtlich. |
| KK-15 | echt | Abb. A2 (a), S. 25, zweiter Legendeneintrag "38.49-35.53 m". |
| KK-16 | echt | Abb. A2 (c), S. 25, fünfter Legendeneintrag "38.40-35.55 m". |
| KK-17 | echt | S. 26, Z. 515 "borehole five". |
| KK-18 | echt | Abb. A3, S. 26, Feldbeschriftung "quartzolit". |
| KK-19 | echt | S. 18, Z. 394 am Seitenbild "m" ohne Exponent. |
| KK-20 | echt | S. 18, Z. 397 "displays". |
| KK-21 | echt | S. 19, Z. 415 "10-16 m ," ohne Exponent am Seitenbild. |
| KK-22 | echt | S. 20, Z. 428 "Caine's (1996)". |
| KK-23 | echt | S. 20, Z. 431 bis 432 wörtlich. |
| KK-24 | echt | S. 21, Z. 444 "at the same showing". |
| KK-25 | echt | Bildunterschrift Abb. 12, S. 22 "boreholes five and six". |
| KK-26 | echt | S. 28, Z. 533 bis 535 "M.A. M" zweimal. |
| KK-27 | echt | S. 32, Z. 678 "Technology, (NIST):". |

## 2. Literaturvorschläge

| Vorschlag | Kennung | Im Literaturverzeichnis |
|---|---|---|
| Brixel et al. 2020a | GB-01 | nein |
| Brixel et al. 2020b | GB-01 | nein |
| Geller 1997 | GB-03 | ja |
| Mizrahi et al. 2024 | GB-03 | ja |
| Evans et al. 2004 | GB-05 | ja |
| Ma et al. 2022 | GB-06 | ja |
| Hunt 2003 | GB-42 | nein |
| Lützenkirchen und Loew 2011 | GB-42 | nein |
| Masset und Loew 2010 | GB-42 | nein |
| Ofterdinger 2001 | GB-42 | nein |
| Achtziger-Zupančič et al. 2024 | GB-49 | ja |
| Caine et al. 1996 | KK-22 | ja |

## 3. Doppelungen

Keine. Geprüfte Paare mit gleichem Fundort (GB-19 und GB-46, GB-30 und GB-32, GB-47 und GB-48, GB-37 und GB-39, GB-34 und KK-19) behandeln jeweils verschiedene Gegenstände.

## 4. Fundorte

Genau: 80. Um 1 bis 2 Zeilen daneben: 2 (GB-04 beginnt bei der Leerzeile S. 2, Z. 46, Zitat ab Z. 47; GB-19 beginnt bei der Leerzeile S. 11, Z. 258, Zitat ab Z. 259). Weiter daneben: 0.

## Zählungen

| Urteil | Anzahl |
|---|---|
| echt | 78 |
| teilweise echt | 4 |
| falsch | 0 |
| nicht prüfbar | 0 |
| Summe | 82 |

Literaturvorschläge: 12, davon ja 6, nein 6. Doppelungen: 0. Fundorte: genau 80, daneben 1 bis 2 Zeilen 2, weiter daneben 0.
