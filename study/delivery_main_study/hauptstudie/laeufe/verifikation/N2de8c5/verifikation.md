# Verifikation des Gutachtens zu egusphere-2025-4733

Prüfgrundlage: Manuskript-PDF (33 Seiten), Seitenbilder in seiten/ (150 dpi), eigene Renderings mit 300 dpi für Messungen, text.json nur als Suchhilfe. Zeilennummern an den gedruckten Randnummern bestätigt. text.json ist an folgenden Stellen um eine Zeile verschoben: S. 2, Z. 47 bis 49 (dort 46 bis 48), S. 5, Z. 112 bis 114 (dort 111 bis 113), S. 9, Z. 186 bis 188, S. 11, Z. 249 und 259, S. 13, Z. 304. Rechnungen in vf/calc.py, Pixelauswertungen mit vf/prof.py und Inline-Skripten.

## 1. Urteile je Kennung

| Kennung | Urteil | Beleg (ein Satz mit Seite und Zeile) |
|---|---|---|
| GB-01 | teilweise echt | Zitate S. 1, Z. 21 bis 22 und S. 2, Z. 50 bis 52 wörtlich vorhanden, Osten et al. (2024) und Kneafsey et al. (2025) an der Quelle bestätigt, aber die Angabe "Osten cited only for densities (p. 10, l. 232) and Fig. 10" ist falsch, da Osten et al. (2024) auch S. 9, Z. 186 bis 187 zitiert wird, und die Tiefenangabe 3,5 km für Evans et al. (2004) ist nicht an deren Abstract bestätigt (siehe GB-07). |
| GB-02 | teilweise echt | URL nur S. 1, Z. 24, BULGG nur in Abb. 1b und Abb. 3 ohne Auflösung, aber es sind vier und nicht fünf Bezeichnungen (URL, Underground Laboratory, Bedretto Lab, BULGG), und "Bedretto Lab at TM2000" steht auf S. 5, Z. 114, nicht Z. 113. |
| GB-03 | teilweise echt | Zitate S. 1, Z. 30 bis 32, S. 23, Z. 463 und Z. 465 bis 467 wörtlich, Verhältnisse 16, 49 und "6 von 8" nachgerechnet, aber die Spanne der effektiven In-situ-Hauptspannungen "7.5 to 25.8 MPa" lässt σHmax weg, mit 27,9 MPa (S. 5, Z. 117) und 0,7 MPa Porendruck reicht sie bis 27,2 MPa. |
| GB-04 | echt | Zitat S. 2, Z. 40 bis 41 wörtlich, Abstract Mizrahi et al. (2024) trennt deterministische Vorhersage und probabilistische Prognose, Navarro-Rodríguez et al. (2025) behandelt ML-Magnitudenschätzung für Frühwarnung. |
| GB-05 | echt | Brixel et al. (2020) fehlt im Literaturverzeichnis S. 29 (zwischen Bischoff und Brace), der Eos-Highlight bestätigt Einzelbohrloch-Permeabilität, Abfall neben dem Kern und Potenzgesetz zwischen Kluftdichte und Permeabilität. |
| GB-06 | teilweise echt | Mischung belegt (characterisation S. 2, Z. 65 gegen characterized Z. 61, behaviour 6 gegen behavior 2, metre 4 gegen meter als Einheit 9), aber die Zählung "characteris 4" enthält dreimal "characteristics" (keine Schreibvariante, tatsächlich 1), "realis 2" enthält "realistic", und centimetre und decametre stehen S. 2, Z. 47 und Z. 49, nicht Z. 46 und Z. 48. |
| GB-07 | teilweise echt | Cappa et al. (2018) ist laut Volltext eine 2-D-Modellierung 200 m × 50 m, parametrisiert an einer Injektion in 282 m Tiefe (S. 2, Z. 47 bis 48 zitiert sie als Laborstudie), aber die Angaben 3,6 km Bohrloch und Störung bei 3,5 km stehen im Abstract von Evans, Genter und Sausse (2005), für Evans et al. (2004) nicht bestätigt; deren Titel (S. 30, Z. 614 bis 615) nennt 3 km, der Gegenbeleg zu S. 2, Z. 50 bis 51 bleibt bestehen. |
| GB-08 | teilweise echt | Satz S. 3, Z. 71 bis 72 wörtlich, Abstract Guillot und Ménot (2009) nennt Mittelkarbon bis Perm vor der Öffnung der Paläotethys und kein Trias, aber der Volltext erwähnt Aar-Gotthard und Gotthard-Massiv, so dass die Aussage zur regionalen Zuordnung über das Abstract hinausgeht. |
| GB-09 | echt | Zitat S. 3, Z. 81 bis 82 wörtlich, Abstract Rast et al. (2022) nennt Altersspannen 285 bis 319 Ma und 280 bis 335 Ma, spätvariszisch, und Tremola und Prato als kaledonische Wirtsgesteine, also älter, nicht jünger. |
| GB-10 | echt | Abb. 1 S. 4: FEAR und TM ohne Auflösung, Streifengneiss und Penninic units beide weiß, Rot für Fibbia (a) und Rotondo (b), "Furka Tunnel TM5221" gegen "TM 5218" S. 3, Z. 87. |
| GB-11 | echt | Abb. 3 S. 8 zeigt FEAR1 volume, FEAR2 volume, BO7 und FEAR tunnel, BO7 kommt im Text nicht vor, Zitat S. 7, Z. 152 wörtlich. |
| GB-12 | echt | Definition S. 5, Z. 101 bis 102, Bildunterschriften Abb. 2 (S. 6), Abb. 12 (S. 22, Z. 456) und Abb. A3 (S. 26, Z. 515) wörtlich, ausgeschriebene Fazies 13-mal gezählt. |
| GB-13 | echt | Zitat S. 5, Z. 109 bis 110 wörtlich, zwei Klassen dort, "fractures with infillings" S. 10, Z. 227, vier Symbole in der Legende von Abb. 2, keine Kriterien angegeben. |
| GB-14 | echt | S. 5, Z. 117 nennt σv ≈ 26,5 MPa, die Stereonetze in Abb. 2 (S. 6) "Sv = 30 MPa", "25.4 ± 2.3 MPa" und "14.6 ± 1.4 MPa", Differenz 3,5 MPa (13 %). |
| GB-15 | echt | Definition S. 5, Z. 126 wörtlich, in Abb. 7 (S. 16) liegt F0 ab 28,9 m, P10-Klassen 29 bis 33 m gemessen 4, 6, 9, 7 m-1 mit 4 und 5 offenen Klüften in 29 bis 30 m und 31 bis 32 m. |
| GB-16 | echt | Abb. 2 (S. 6): Intervall- und Probenspalten ohne Legende, großes BO5-Stereonetz überdeckt die Logspuren ab etwa 46,7 m, Legende nur Fazies und Klufttypen. |
| GB-17 | echt | Zitat S. 7, Z. 153 bis 155 wörtlich, Intervallgrenzen in Abb. 2 bei 300 dpi gemessen (37,41 bis 38,13 m bis 45,20 bis 45,92 m), 8 von 11 Stopfen in 5 von 7 Intervallen, Verhältnisse 4,6 × 10^5, 4,0 × 10^6, 62 bis 224 nachgerechnet, Median Intervall 6 gemessen 1,4 × 10-13 m². |
| GB-18 | echt | Maßstab Abb. 3 gemessen 5,11 px/m (300 dpi), BO6-Spur etwa 313 px, also rund 61 m, gegen 55 × cos 10,3° = 54,1 m nach S. 5, Z. 103 bis 104. |
| GB-19 | echt | S. 8, Z. 175 bis 183 und S. 9, Z. 190 bis 200 nennen weder Methode je Stopfen noch Auswertungsgrößen, 2,0 × 10-13 m² (S. 18, Z. 374) liegt über dem Bereich 10-16 bis 10-21 m² (S. 9, Z. 191), Zitat S. 8, Z. 182 bis 183 wörtlich. |
| GB-20 | echt | Zitat S. 11, Z. 250 bis 251 wörtlich, kein Gerät in S. 8 bis 11 und S. 26 mit Hersteller oder Modell genannt, nSIGHTS nur mit Jahr (S. 11, Z. 250). |
| GB-21 | echt | Zitat S. 8, Z. 180 bis 181 wörtlich, 32/27,9 = 1,15, maximale effektive Hauptspannung 24,3 bis 27,2 MPa und mittlere 17,9 bis 20,8 MPa nachgerechnet, Fundort "p. 5, l. 112 to 113" liegt tatsächlich in Z. 113 bis 114. |
| GB-22 | echt | Abb. 4a (S. 9) zeigt "Helium supply" und roten Kasten "Vref", rechte Achse "ln(Pup - Pdown) (-)", Text S. 8, Z. 176 nennt Wasser als Arbeitsfluid. |
| GB-23 | echt | Zitate S. 18, Z. 385 bis 386 und S. 26, Z. 511 bis 513 wörtlich, Zählungen aus Abb. A1 (22 Stopfen, 12 Segmente), A2b (4), A2a (5), A2c (12), A3 (8), A4 (5 Tabellenzeilen) bestätigt, WIP/He-Verhältnisse 0,64, 0,56, 0,67, 0,98. |
| GB-24 | echt | S. 10, Z. 230 "(in BO5, only Vp was measured)", dagegen Vs-Mittel für BO5 S. 13, Z. 294 bis 295, Vp- und Vs-Kurven in Abb. 6 (S. 14) und nur Vp in Abb. 7 (S. 16). |
| GB-25 | echt | Zitate S. 10, Z. 231 bis 233 und S. 13, Z. 316 bis 317 wörtlich, Dichten 2,385, 2,630, 2,881 g cm-3 und Korndichten 2,624 und 2,890 (gesättigt) sowie 2,797 und 2,895 (trocken), −15,8 %, 8,7 % und 13,3 % mit Python nachgerechnet, BO6 −3,6 % bis −7,1 %. |
| GB-26 | echt | Gleichung (2) S. 10, Z. 235 und Verweis Z. 232 stehen vor Gleichung (1) S. 12, Z. 268 bis 269. |
| GB-27 | echt | Zitate S. 11, Z. 260 bis 262 und S. 15, Z. 346 bis 347 wörtlich, keine Datierung, keine Quelle, S. 28, Z. 530 nennt nur eine DOI. |
| GB-28 | echt | Zitate S. 11, Z. 245 bis 246 und S. 13, Z. 307 bis 308 wörtlich, keine Integritätsergebnisse berichtet, Kluft 39,80 bis 40,10 m liegt nach Messung in Abb. 2 im Intervall 4 (39,69 bis 40,42 m). |
| GB-29 | teilweise echt | Zitate S. 13, Z. 300 bis 301 und S. 12, Z. 278 bis 280 wörtlich, Median Intervall 2 in Abb. 6 bei 300 dpi gemessen 10^-12,28 (5,3 × 10-13 m², Faktor 30), aber die Mächtigkeit der T-zu-k-Umrechnung ist angegeben, S. 11, Z. 255 nennt "the known interval thickness" (0,73 m nach Z. 239). |
| GB-30 | echt | S. 15, Z. 347 "The interval size was 2.4 m" gegen Z. 349 "26.0-29.7 m (3.7 m interval)", Thiem-Eingaben fehlen, Abstände 15,1 m und 19,5 bis 23,4 m sowie umskalierte Werte 5,3 × 10-15, 1,3 × 10-14 und 2,0 × 10-14 m² nachgerechnet. |
| GB-31 | echt | Abb. 5 (S. 12): b in MPa (etwa 3,24 bis 3,99), d "Hydraulic head (m)" etwa 340 bis 409, e "Pressure (kPa)" etwa 330 bis 410, 3,24 bis 3,99 MPa entsprechen 330 bis 407 m Druckhöhe. |
| GB-32 | echt | Abschnitt 4.1 (S. 13 bis 15) nennt keine Fließdimension, Zitate S. 20, Z. 430 bis 431 und S. 23, Z. 470 bis 471 wörtlich, Abb. 11 (S. 21) hat sechs BO5- und vier BO6-Einträge. |
| GB-33 | echt | S. 13, Z. 300 bis 313 gibt Werte nur für BO5-Intervalle 2, 3, 5 und 7, S. 15, Z. 333 bis 335 für alle vier BO6-Intervalle, Porosität BO6 nur Mittel 2,0 % (Z. 338). |
| GB-34 | echt | Zitat S. 13, Z. 301 bis 302 wörtlich, Abb. 2, 6 und 7 ohne Intervallnummern, Boxmitten Abb. 6 gemessen 37,75 bis 45,56 m, Abb. 11 nennt 37,13 bis 44,86 m (Versatz 0,60 bis 0,68 m). |
| GB-35 | echt | Kopf "Caliper (mm) 12.1 25" (Abb. 6, S. 14) und "13.8 29" (Abb. 7, S. 16) ohne Ticks, keine Fazieslegende, Legenden überdecken Daten, P10-Achsen etwa 7 und 13 m-1. |
| GB-36 | echt | Zitat S. 14, Z. 321 wörtlich, F4-Laborwerte 5,0 % und 6,3 % (S. 18, Z. 381 bis 383), He etwa 9,4 % (Abb. A2b), CT 7,97 % und 4,47 % (Abb. A4, S. 27). |
| GB-37 | echt | Zitate S. 15, Z. 327 und Z. 333 bis 334 wörtlich, Faziesspalte Abb. 7 (S. 16) zeigt F4 nur oberhalb des F3-Kerns (F0 darunter), Intervall 2 um 27,87 m umfasst F1 und F4, nicht F3. |
| GB-38 | echt | Abb. 7 bei 300 dpi gemessen (68 px pro Dekade): Intervall 1 Median 10^-13,37, oberes Quartil 10^-12,38, Ausreißer 10^-11,94, die Angabe 3,4 × 10-14 m² (S. 15, Z. 333) liegt unter dem Median. |
| GB-39 | echt | Zitat S. 15, Z. 336 bis 337 wörtlich, P10-Klassen gemessen BO5 Mittel 3,4 m-1, BO6 7,1 m-1 (6,8 mit letzter Klasse), Verhältnis 2,0 bis 2,1, Winkelargument S. 15, Z. 328 bis 330 vorhanden. |
| GB-40 | echt | Zitate S. 15, Z. 340 bis 341 und S. 22, Z. 451 bis 454 wörtlich, Abb. 7 bei 150 dpi gemessen 1,37, 1,99, 1,72, 2,01 MPa, Kernintervall also niedriger als beide Nachbarn, 1000 × 9,81 × 1000 m = 9,8 MPa. |
| GB-41 | echt | Zitate S. 17, Z. 371 und S. 18, Z. 374 bis 375 wörtlich, Abb. 8c gemessen Maximum etwa 4,5 × 10-17 und Minimum etwa 4,2 × 10-19 m², Abb. 8d etwa 2,9 × 10-13 m², gegen 3,5 × 10-17, 4,0 × 10-18 und 2,0 × 10-13 m² im Text. |
| GB-42 | teilweise echt | Bildunterschrift S. 17, Z. 367 bis 368 wörtlich, je Fazies nur ein Kernfoto ohne Maßstab und Ticks wie "7e10-19", aber ohne Bild sind 5 und nicht 6 von 11 Stopfen, da 35.0-35.27, 39.15-39.35, 37.50-37.60 und 43.30-43.50 m zusammen sechs Stopfen enthalten. |
| GB-43 | echt | Zitat S. 18, Z. 376 bis 377 und Z. 379 wörtlich, Abstract Evans et al. (1997): Protolith am druckempfindlichsten wegen kurzer, schlecht verbundener Klüfte, Kern mit der niedrigsten Permeabilität. |
| GB-44 | echt | Zitat S. 18, Z. 383 bis 385 wörtlich, Abb. A1 (S. 24): Fazies 1 sechs höher, zwei niedriger, Fazies 2 Stopfen niedriger, Fazies 3 fünf von sechs niedriger, Fazies 4 je einer. |
| GB-45 | teilweise echt | Zitat S. 18, Z. 386 bis 387 wörtlich, Abb. A2a (S. 25) zeigt etwa 4420 und 2420 m s-1 außerhalb von 2,49 bis 4,08 km s-1, aber die beiden Stopfen 43.35-43.39 und 43.40-43.44 m liegen 5 cm (Mitten) und nicht 5 mm auseinander. |
| GB-46 | echt | "43.40-43.50 m" nur S. 18, Z. 387 gegen fünfmal "43.30-43.50", "43.35-43.38" zweimal in Abb. A4 gegen sechsmal "43.35-43.39", Fundort "l. 373" für 43.35-43.39 liegt tatsächlich in Z. 372. |
| GB-47 | echt | Abb. A1 (S. 24) Kernwert 41.57-41.70 m bei 1,04 %, Abb. A2c (S. 25) bei etwa 0,81 %, übrige Segmente übereinstimmend. |
| GB-48 | echt | Abb. A1 Fazies 3, Segment 38.55-38.75 m, Stopfen etwa 2,76 %, Abb. A2b Stopfen 38.58-38.62 m WIP etwa 1,48 % bei He etwa 2,66 %. |
| GB-49 | echt | A.1, Abb. A3 und A4 (S. 26 bis 27) werden im Haupttext nicht zitiert, XRD und CT fehlen in Abschnitt 3, Zahlen 1, 2, 6, 7 in Abb. A3 blass, 5 und 4 sowie 2 und 7 überlappen. |
| GB-50 | echt | Bildunterschrift S. 27, Z. 520 nennt vier Proben, Bildgruppen vier, Tabelle fünf Zeilen mit 41.31-41.35, Achsenbeschriftungen unlesbar, rote und grüne Pfeile unerklärt. |
| GB-51 | echt | Hunt (2003, S. 19, Z. 404), Lützenkirchen und Loew (2011), Masset und Loew (2010) und Ofterdinger (2001, Z. 412 bis 413) fehlen unter den 69 Einträgen S. 29 bis 33, Legende Abb. 10 nennt "Lützenkirchen 2002", Abstract Lützenkirchen und Löw (2011) ohne hydraulische Daten. |
| GB-52 | echt | Zitat S. 19, Z. 410 bis 411 wörtlich, Volltext Davy et al. (2023) führt Skaleneffekt auf Konnektivität und Transmissivitätsverteilung zurück und nennt Hunt nur als Gegenposition. |
| GB-53 | echt | Legende Abb. 9 (S. 19): Lab N = 63, 42, 84, 6 (195), Feld 14, 10, 11, 8 (43), gegen 11 Stopfen mal 3 Stufen = 33 (S. 8, Z. 175 und Z. 181), Verhältnisse 7, 7, 7, 1. |
| GB-54 | echt | Zitat S. 19, Z. 418 bis S. 20, Z. 420 wörtlich, Achse Abb. 10 kategorial, Dreiecke dieser Studie rechts der Mitte zwischen "0.5 - 25 m" und "25 - 300 m", Abstände 15,1 m und 17 bis 23 m nachgerechnet. |
| GB-55 | echt | Bildunterschrift S. 20 "Triangles indicate single values", Einzelwerte von Ofterdinger, Ma und Münger aber als kleine Quadrate, Schema nach Caine nur in Z. 420 bis 421 erklärt. |
| GB-56 | echt | Zitate S. 20, Z. 425 bis 426 und S. 23, Z. 469 bis 470 wörtlich, 3,9/1,6 = 2,4, 1,2 × 10-11/3,9 × 10-15 = 3077 und 1,6 × 10-11/3,9 × 10-15 = 4103, Injektion 43,2 bis 45,6 m außerhalb des BO5-F3 (etwa 37,5 bis 39 m in Abb. 6). |
| GB-57 | echt | Abb. 11 (S. 21): farbige Bohrlochsegmente und Seitenpanels mit Boxplots und orangen Marken, Legende nur Mapped Fractures, Packed-off intervals, Major flow paths. |
| GB-58 | echt | Abb. 12 (S. 22) "SW (strike ~ 220°)", Linie der upper fault trace in Abb. 3 (S. 8) gemessen etwa 066°/246°, Differenz etwa 26°. |
| GB-59 | echt | Zitate S. 23, Z. 473 bis 474 und Z. 481 bis 482 wörtlich, kein Test auf der Gegenseite berichtet, D4-Flächen unter 30 m Länge S. 7, Z. 149 bis 150. |
| GB-60 | echt | Zitat S. 23, Z. 478 bis 480 wörtlich, Gegenbelege S. 11, Z. 245 bis 246, S. 13, Z. 307 bis 308 und Z. 313 bis 314, S. 15, Z. 342 bis 344 vorhanden. |
| GB-61 | echt | Zitat S. 28, Z. 528 wörtlich, kein Grund für die Beschränkung genannt. |
| GB-62 | echt | Zitat S. 28, Z. 530 wörtlich, keine Zuordnung von Datensätzen. |
| GB-63 | echt | Literaturverzeichnis: "Geol, 24, 1025" S. 29, Z. 579, Cappa 2018 ohne Artikelnummer Z. 584 bis 586, "JGS" S. 31, Z. 654, "SP" S. 33, Z. 700, NIST und Sandia ohne URL, Achtziger-Zupančič mit Tagesdatum S. 29, Z. 557. |
| KK-01 | echt | S. 1, Z. 25 "These findings pose a necessary foundation" wörtlich. |
| KK-02 | echt | S. 2, Z. 35 wörtlich. |
| KK-03 | echt | S. 3, Z. 87 "located at TM 5218" wörtlich, sonst TM1138, TM2805, TM3437 ohne Leerzeichen. |
| KK-04 | echt | S. 3, Z. 88 "At the same time, it be biotite-rich and porphyroclastic (RG2)" wörtlich. |
| KK-05 | echt | Bildunterschrift Abb. 1 (S. 4) "the Pizzo Rotondo", Abb. 1a und Abb. 3 "Piz Rotondo". |
| KK-06 | echt | Abb. 1b (S. 4) "Furka Tunnel", Abb. 1a, Abb. 3 und S. 3, Z. 86 bis 87 "Furka Base Tunnel". |
| KK-07 | echt | "Bedretto tunnel" in Bildunterschrift Abb. 1b, S. 5, Z. 122, Bildunterschrift Abb. 10 und S. 23, Z. 474, "Bedretto Tunnel" S. 2, Z. 52 und S. 3, Z. 81. |
| KK-08 | echt | Abb. 2 (S. 6) Beschriftungen "Sv", "SHmax", "Shmin" gegen σv, σHmax, σhmin S. 5, Z. 117. |
| KK-09 | echt | S. 8, Z. 181 bis 182 wörtlich. |
| KK-10 | echt | S. 9, Z. 190 wörtlich. |
| KK-11 | echt | S. 10, Z. 221 "a spatial sampling rate of 1 cm-1" wörtlich. |
| KK-12 | echt | S. 10, Z. 235 Gleichung mit kursivem p statt ρ. |
| KK-13 | echt | S. 11, Z. 252 "transmissivity (m s-2)" wörtlich. |
| KK-14 | echt | S. 11, Z. 254 und Z. 255 im Seitenbild ohne hochgestellte 2. |
| KK-15 | echt | S. 11, Z. 257 "1 mPa s-1" wörtlich. |
| KK-16 | echt | S. 11, Z. 263 doppelte Klammer wörtlich. |
| KK-17 | echt | S. 11, Z. 266 "hydraulic head gradient ΔΦ" und "pw", ebenso in Gleichung (1) S. 12. |
| KK-18 | echt | S. 12, Z. 275 ohne Abkürzung, "GRF" erstmals Z. 277. |
| KK-19 | echt | S. 13, Z. 293 "poor tool eccentricity" wörtlich. |
| KK-20 | echt | S. 13, Z. 295 wörtlich. |
| KK-21 | echt | S. 13, Z. 299 "2018).The" wörtlich. |
| KK-22 | echt | S. 13, Z. 301 wörtlich. |
| KK-23 | echt | S. 13, Z. 310 bis 311 Satz bricht mit "slightly higher due." ab. |
| KK-24 | echt | S. 13, Z. 313 "The amount of open fractures" wörtlich. |
| KK-25 | echt | Legenden "SPP" in Abb. 6 und 7, Bildunterschriften S. 14, Z. 319 bis 320 und S. 16 nur "static pore pressure". |
| KK-26 | echt | S. 14, Z. 323 "m3 s-1 MPa." wörtlich. |
| KK-27 | echt | S. 17, Z. 364 wörtlich. |
| KK-28 | echt | S. 17, Z. 365 "Figure 8 (c)" wörtlich. |
| KK-29 | echt | S. 17, Z. 370 "38.58-38.62 has a partial open fracture" wörtlich. |
| KK-30 | echt | Abb. A2a (S. 25) zweiter Legendeneintrag "38.49-35.53 m". |
| KK-31 | echt | Abb. A2c (S. 25) fünfter Legendeneintrag "38.40-35.55 m". |
| KK-32 | echt | Abb. A3 (S. 26) Beschriftung "quartzolit". |
| KK-33 | echt | S. 18, Z. 394 bis 395 im Seitenbild viermal "m" ohne hochgestellte 2. |
| KK-34 | echt | S. 19, Z. 415 "10-16 m ," ohne hochgestellte 2. |
| KK-35 | echt | S. 20, Z. 428 "after Caine's (1996) definition" wörtlich. |
| KK-36 | echt | S. 20, Z. 430 "values between 1.95 and 1.58" wörtlich. |
| KK-37 | echt | S. 20, Z. 431 bis 432 wörtlich. |
| KK-38 | echt | S. 21, Z. 444 "at the same showing" wörtlich. |
| KK-39 | echt | Abb. 11 (S. 21) "30 (30.84)", 30/cos 10,3° = 30,49, die übrigen BO6-Marken 20,32 und 40,64 folgen diesem Faktor. |
| KK-40 | echt | S. 23, Z. 473 wörtlich. |
| KK-41 | echt | S. 23, Z. 479 bis 480 wörtlich. |
| KK-42 | echt | S. 23, Z. 480 "cross-hole", sonst "crosshole" (S. 20, Z. 425, S. 23, Z. 469, Abb. 11). |
| KK-43 | echt | S. 28, Z. 533 bis 535 "M.A. M" zweimal. |
| KK-44 | echt | S. 28, Z. 534 bis 535 "writing - original draft" mit Bindestrich, bei "review and editing" steht ein anderes Strichzeichen. |
| KK-45 | echt | S. 32, Z. 678 "National Institute of Standards and Technology, (NIST)" ohne URL. |

## 2. Literaturvorschläge

| Vorgeschlagene Arbeit | Kennung | Im Literaturverzeichnis |
|---|---|---|
| Kneafsey et al. (2025), EGS Collab, Geothermics 126, 103178 | GB-01 | nein |
| Brixel et al. (2020), JGR Solid Earth 125, e2019JB018200 | GB-05 | nein |
| Osten et al. (2024) | GB-01 | ja |
| Achtziger-Zupančič et al. (2024) | GB-01 | ja |
| Geller (1997), Mizrahi et al. (2024) | GB-04 | ja |
| Evans et al. (1997) | GB-43 | ja |
| Davy et al. (2023) | GB-52 | ja |
| Hunt (2003) | GB-51 | nein |
| Masset und Loew (2010) | GB-51 | nein |
| Ofterdinger (2001) | GB-51 | nein |
| Lützenkirchen (2002, tatsächliche Datenquelle) | GB-51 | nein |

Ausdrücklich neu vorgeschlagene Arbeiten mit vollständiger Angabe: 2, beide nein.

## 3. Doppelungen

Keine zwei Kennungen mit gleichem Fundort und gleichem Gegenstand. Teilüberschneidungen mit Querverweis, aber verschiedenem Gegenstand: GB-33 und KK-23 (S. 13, Z. 310 bis 311, fehlende Werte gegen abgebrochener Satz), GB-34 und GB-35 Punkt 3 (fehlende Intervallnummern in Abb. 6 und 7), GB-54 und GB-55 Punkt 3 (kategoriale Achse Abb. 10), GB-60 und KK-41 (S. 23, Z. 479 bis 480, Umsetzbarkeit gegen Wortlaut).

## 4. Fundorte

| Klasse | Anzahl | Kennungen |
|---|---|---|
| genau | 104 | alle übrigen |
| um 1 bis 2 Zeilen daneben | 4 | GB-02 (S. 5, Z. 113 statt 114), GB-06 (S. 2, Z. 46 und 48 statt 47 und 49), GB-21 (S. 5, Z. 112 bis 113 statt 113 bis 114), GB-46 (S. 18, Z. 373 statt 372) |
| weiter daneben | 0 | |

Gewertet wurde das Feld Location; Zeilenbereiche, die die belegte Stelle vollständig einschließen, gelten als genau.

## 5. Zählungen je Urteil

| Urteil | GB | KK | Summe |
|---|---|---|---|
| echt | 54 | 45 | 99 |
| teilweise echt | 9 | 0 | 9 |
| falsch | 0 | 0 | 0 |
| nicht prüfbar | 0 | 0 | 0 |
| Summe | 63 | 45 | 108 |

Teilweise echt: GB-01, GB-02, GB-03, GB-06, GB-07, GB-08, GB-29, GB-42, GB-45.
