# Verifikation des Gutachtens zu egusphere-2025-5046

Grundlage: Seitenbilder (Randnummern), text.json, Supplement-Seitenbilder, Python-Nachrechnung aus Table S1, S2, S3, S4, S5 (Skripte in vf/skripte/), Literatur über WebSearch und WebFetch.

## 1. Urteile je Kennung

| Kennung | Urteil | Beleg (ein Satz mit Seite und Zeile) |
|---|---|---|
| GB-01 | echt | Zitat wörtlich S. 1, Z. 19 bis 20, ohne Angabe zur Literatursuche; qualifizierte Ansprüche S. 3, Z. 74 bis 76, S. 7, Z. 220, S. 14, Z. 472, Coppo et al. S. 9, Z. 277 bis 279 vorhanden. |
| GB-02 | echt | S. 1, Z. 18 und S. 6, Z. 182 nennen 33,7 bis 2,9, S. 3, Z. 90 bis 91 nennt 33,6 bis 2,8, S. 9, Z. 304 nennt 2,7; Table S1 reicht von 2852 bis 33699. |
| GB-03 | echt | S. 1, Z. 23 "greater inputs", S. 10, Z. 316 "increased contributions", S. 2, Z. 63 Faktor 25, S. 14, Z. 463 "relative increase"; 23,1/25 = 0,92 gegen 10,2 nachgerechnet. |
| GB-04 | echt | Zitat S. 2, Z. 40 bis 41; Lambert 2015 (AWI-Repositorium) nennt unter 10 plus etwa 10 ppm, Lambert 2021 (Repositorium) 12 bis 29 ppmv im Text und 8,9 bis 33,1 ppmv in Table 2. |
| GB-05 | echt | Zitat S. 2, Z. 52; Abstract von Engelbrecht et al. 2019 behandelt LGM-Downscaling über Südafrika ohne Westwinde. |
| GB-06 | echt | Zitat S. 2, Z. 63; Lambert 2008 Abstract: "approximately 25-fold increase ... over all eight glacial periods", Eintrag S. 19, Z. 676 bis 678; Abstract Delmonte 2017 ohne Flussverhältnis. |
| GB-07 | echt | Zitat S. 3, Z. 72 bis 74; die drei Arbeiten existieren mit den genannten Aussagen (Repositorien) und fehlen im Verzeichnis S. 16 bis 22, das nur Marino 2009 und Vallelonga 2002 enthält. |
| GB-08 | echt | Zitat S. 3, Z. 79 bis 81; Abstract Vanderstraeten 2023: AUS 14 bis 15 vor und 13 bis 21 % nach 14,5 kyr, SAF 9 auf 21 bis 23 %; Table S5 EDML (Supp. S. 22) mit PAT 71,6/73,7 und 58,4 bis 62,7. |
| GB-09 | echt | Supp. S. 11 Titel "using 217 PSAs and 279" und Supp. S. 16 "Table of PSAs database", DS-Definition S. 4, Z. 129. |
| GB-10 | echt | Datenaussage wörtlich S. 16, Z. 494 bis 496; Supplement enthält keine Eingangsdaten, cf_i oder Code; PANGAEA.696109 ist ein EDC-REE-Datensatz. |
| GB-11 | echt | Zitat S. 4, Z. 110 bis 111; aus Table S1: 112 Proben ab 14 kyr, 29 Lücken über 140 Jahre, 33 fehlende Proben, Mittel 128,5, Median 98, Spanne 0 bis 2280 Jahre. |
| GB-12 | echt | S. 4, Z. 111 EDC3 nach Parrenin; Periodengrenzen S. 6, Z. 184 bis 188 nach Veres et al. 2013 (AICC2012, S. 21, Z. 817 bis 820); ACR 8, YD 9 Proben. |
| GB-13 | echt | Table S2 gezählt: PAT 39, CWA 5, PAP 14, SAF 23, AUS 107, NZ 25, ANT 4; 101 Marx and Kamber, 45 Darling Basin; Zitat S. 11, Z. 366 bis 367. |
| GB-14 | echt | Bezeichnungen in Table S1 bis S3 und Abb. 2 (S. 26) so vorhanden; Nachrechnung Eq. 3 und 4: 0,7094/minus 4,13 und 0,7104/minus 5,33. |
| GB-15 | echt | S. 4, Z. 131 bis 132 nennt AUS 106 und ANT 5; Seitenbild Supp. S. 19 zeigt 4 ANT-Zeilen, Zählung AUS 107; Figure S1 mit 22 PAT-Koordinaten. |
| GB-16 | echt | Supp. S. 19: ELB La 0,720323, Lu 0,008290; La/Lu 35,8 bis 129,3 gegen 0,26 bis 2,48 sonst; Division durch UCC ergibt etwa 0,02 bis 0,03; Zitat S. 4, Z. 134 bis 135. |
| GB-17 | echt | Zitat S. 5, Z. 164 bis 165; Supp. S. 13, erste Zeile 10511 summiert 93,5, alle anderen 240 Zeilen innerhalb 0,15. |
| GB-18 | echt | S. 5, Z. 140 nennt nur lsqnonneg in MATLAB, ohne Version, Toleranz oder Seed (S. 5, Z. 157 bis 162). |
| GB-19 | echt | Zitat S. 5, Z. 153 bis 154; Table S1 und S5 ohne Streuung, S. 7, Z. 235 "significantly increased", Spitzen 94,7 (12227) und 100,0 (8629) bestätigt. |
| GB-20 | echt | S. 5, Z. 167 kündigt Flüsse an; Abb. 1 (S. 24) zeigt nur "Total Contribution (%)", Figure S2 (Supp. S. 4) nur Gesamtfluss, δ18O und d-excess. |
| GB-21 | teilweise echt | Zitat S. 5, Z. 170 bis 172, kritisches r 0,708 (df 10) und 0,684 (df 11) sowie drei Zeilen R 0,66 bestätigt; bei Schwelle 0,708 bleiben aber 222, nicht 221 Proben. |
| GB-22 | echt | Supp. S. 17 bis 19 und 21 nennen Marx and Kamber (101), Marx et al. (10), McGowan (2), Diaz (4), Aarons, Bory; keiner davon im Verzeichnis S. 16 bis 22; 117 von 217. |
| GB-23 | echt | Supp. S. 17 Darling26 und Darling29 und Supp. S. 18 Murray29 und Murray24 sind in allen 13 Werten und Koordinaten identisch. |
| GB-24 | echt | Supp. S. 17: SuksesL 21,059 S und Sossusvlei 24,76 S mit Ort "Etosha Pan", alle sechs "this study"-Zeilen mit W-Länge. |
| GB-25 | echt | S. 6, Z. 175 bis 176; Table S1 behält 129 Proben unter 14 kyr, 38 von 167 = 22,8 % ausgeschlossen. |
| GB-26 | teilweise echt | Die drei Muster sind S. 6, Z. 196 bis 198 nicht benannt und nur PataGi5 heißt "Peninsula de Valdes" (Topsoil), aber Supp. S. 16 führt bei Puerto Madryn (42°46'S) und Trelew äolische Staubproben in Valdes-Nähe, der Widerspruch zur Probenart trägt also nicht. |
| GB-27 | echt | Zitat S. 6, Z. 201 bis 202; Probenmittel AUS 16,5, SAF 9,2, NZ 7,9, PAP 6,8; zeitgewichtet 12,9/9,4/9,0/5,0; Mittel der sechs Perioden 13,2/9,0/7,7/4,8. |
| GB-28 | echt | Zitat S. 6, Z. 207 bis S. 7, Z. 208; 9,5 bis 12 kyr: 33 Proben, Mittel 4,3, Median 0,3, 15 Nullwerte; YD ohne 12227 4,6; 2,8 bis 9,5 kyr 13,0. |
| GB-29 | echt | Zitat S. 7, Z. 214 bis 215 und S. 11, Z. 358 bis 359; Altiplano über 90 nur bei 8629 und 11228, Puna 20 % oder mehr in acht Proben, Altiplano 16,6 und 12,8 bei 12841 (Supp. S. 13). |
| GB-30 | echt | Abb. 1 auf S. 24, Legende S. 25 ohne Auflösung von PAT, AUS, SAF, NZ, PAP. |
| GB-31 | echt | Abb. 3 (S. 27) Holocene-Box PAT etwa 12/55/73 entspricht Early Holocene (12,3/55,2/73,0); Figure S4 (Supp. S. 8) "Early Holocene" etwa 19/62/81 entspricht Late Holocene (18,9/61,7/80,7). |
| GB-32 | echt | Legende S. 27, Z. 872; Abb. 3 zeigt Punkte jenseits der Whisker, LGM PAT Whisker 84,4 und Ausreißer 93,5 nach Table S1. |
| GB-33 | echt | Figure S4 (Supp. S. 8) nur erstes Panel mit Achse; YD-PAT-Box liest etwa 86/71/48 gegen Table S1 84,8/70,2/47,1, YD-Whiskerkappe bei 100 gegen Maximum 98,7. |
| GB-34 | echt | Table S1 (Supp. S. 11, 13, 14) ohne Tiefe, Alter 3559, 10511, 12841, 28709 doppelt mit verschiedenen Werten. |
| GB-35 | echt | Gezählt aus Table S1: MIS3 41, LGM 40, HS1 27, ACR 8, YD 9, EH 56, LH 60; Table S5 (Supp. S. 22) ohne n. |
| GB-36 | echt | S. 7, Z. 233 "onset of the ACR" gegen S. 7, Z. 225, S. 1, Z. 23 und S. 14, Z. 477 mit etwa 14,5 kyr. |
| GB-37 | echt | Zitat S. 8, Z. 258 bis 260; Table S4 (Supp. S. 21): 22 Holozänwerte aus Taylor Glacier (8, Mittel 0,7111/minus 4,64) und Berkner Island (14, 0,7132/minus 11,50), keine EDC-Holozänwerte. |
| GB-38 | echt | S. 7, Z. 238 und Eintrag S. 17, Z. 561 bis 564 (Climate Dynamics), Table S4 "2004a"; Earth-Science Reviews 66, 63 bis 87 mit Sr-Nd laut IRD-Datensatz existiert und fehlt. |
| GB-39 | echt | Zitat S. 8, Z. 267 bis 269; Davies 2020 Abstract (Exeter): Maximum 33 bis 28 ka von 38 bis 48°S, um 47 ka südlich, 350 km und 2090 km bei 35 ka. |
| GB-40 | echt | Zitat S. 8, Z. 275 bis S. 9, Z. 277; Krätschmer 2022 Abstract "over 90 %", Text nennt Australien als vorherrschende LGM-Quelle; SSA plus AUS 79,5 nachgerechnet. |
| GB-41 | echt | S. 9, Z. 276 "~77%" und Z. 282 "~11%" gegen Table S5 75,9 und 14,2; gepoolte MIS3 plus LGM: NZ 11,6, PAT plus AUS 77,7. |
| GB-42 | echt | S. 9, Z. 295 nennt 84 %; Table S5 HS1 PAT plus NZ 81,9, Median je Probe 83,2, mit PAP auf Basis Table S5 83,9. |
| GB-43 | echt | Zitat S. 9, Z. 306 bis 308; Table S1: mittleres R 0,799 (Holozän, min 0,66) gegen 0,924 (LGM, min 0,88), SD PAT 32,1 gegen 9,9, Paardifferenzen 87,2/52,9/39,4/10,2. |
| GB-44 | echt | S. 10, Z. 321 "61%" und Z. 326 "60%"; Table S5 49,0 plus 0,0 plus 11,0 = 60,0. |
| GB-45 | echt | Zitate S. 10, Z. 338 bis 340 und S. 11, Z. 351; Abb. 5 (S. 29) Panel B ohne MDF-Ausschlag bei 6 bis 6,5 kyr, blaues Band etwa 8 bis 11,4 kyr; Korrelationswerte nicht nachdigitalisiert. |
| GB-46 | echt | S. 10, Z. 339 bis 340 und S. 11, Z. 348 bis 349 "bog"; Legende S. 29, Z. 881 bis 882 und Eintrag S. 19, Z. 690 bis 692 nennen Seesedimente. |
| GB-47 | echt | Erstzitate: Abb. 5 S. 10, Z. 340, Abb. 4 erst S. 12, Z. 405. |
| GB-48 | echt | S. 11, Z. 365 Gili et al. 2016; Verzeichnis S. 18, Z. 637 und 641 nur 2017 und 2022. |
| GB-49 | echt | S. 12, Z. 382 verweist auf Figure S4, die nur Boxplots je Periode zeigt (Supp. S. 8). |
| GB-50 | echt | S. 12, Z. 406 bis 407, S. 13, Z. 423 bis 424; minus 13,7 und plus 12,3 nur mit vollem Holozän, EH minus 15,6 und plus 14,1; 15 von 40 LGM-Proben über 27 kyr. |
| GB-51 | echt | Vorbehalt erst S. 12, Z. 407 bis 409; ACR- und YD-Mittel in S. 6, Z. 192, 204, 207 und S. 7, Z. 212 ohne Vorbehalt. |
| GB-52 | echt | S. 12, Z. 408 "8 and 7 samples"; Table S1 (Supp. S. 13) zeigt neun YD-Zeilen. |
| GB-53 | echt | S. 13, Z. 422 "+4 and +6.5%"; Table S5: ACR plus 6,4, YD plus 4,7, YD SAF plus 6,4. |
| GB-54 | teilweise echt | "demonstrate" S. 14, Z. 466 und NZ-Halbierung LGM 14,2 auf HS1 7,1 bestätigt, Binmittel 83,1/72,0/64,3; aber "due to" in S. 14, Z. 484 bezieht sich auf den Flussrückgang 18 bis 15 kyr, nicht auf den Meeresspiegelmechanismus. |
| GB-55 | teilweise echt | Zitat S. 14, Z. 486 bis 487 und Lagebegründung S. 13, Z. 425 bis 440 bestätigt, doch Abschnitt 4.4 nennt in S. 13, Z. 440 bis 443 ebenfalls zunehmende Aridität der Quellgebiete. |
| GB-56 | echt | Zitat S. 15, Z. 491 bis 492; Abschnitte 3 und 4 ohne Fluss- oder Eisenergebnisse. |
| GB-57 | echt | S. 16, Z. 497 "P.B"; Autorenliste S. 1 ohne Initialen P.B. |
| GB-58 | echt | Legende Abb. 2 (S. 26): "EDC Early Holocene" hellrot, "EDC Holocene" dunkelrot; Probe 6570 (LH) liegt auf hellrotem, 8629 (EH) auf dunkelrotem Punkt; die Benennung "end of MIS3/LGM" steht S. 8, Z. 251, nicht Z. 252. |
| GB-59 | echt | Abb. 5 (S. 29) mit Ticks 0,5 bis 3 ohne Titel, Einheit oder Multiplikator, Band und graue Zonen in der Legende Z. 880 bis 882 nicht erklärt. |
| GB-60 | echt | Figure S2 (Supp. S. 4) Achsen "nssCa2+ flux", "δ18O", "deuterium excess" ohne Einheit, Ticks minus 49,05 usw. |
| GB-61 | echt | Figure S3 (Supp. S. 6) Altiplano-Spitze etwa 66 bei 6,4 kyr, bei 8,6 und 11,2 kyr niedrig, Puna-Spitzen etwa 43 und 55 sowie Etosha etwa 88 um 11 bis 12 kyr ohne Gegenstück in Table S1. |
| GB-62 | echt | Figure S5 (Supp. S. 10) EDML-Legendentext (219,233,246) auf Weiß, Kontrast etwa 1,2 zu 1. |
| KK-01 | echt | S. 1, Z. 15 "provides" wörtlich. |
| KK-02 | echt | S. 1, Z. 19 "for the first-time contributions" wörtlich. |
| KK-03 | echt | S. 1, Z. 20 "Marine isotope 3" wörtlich. |
| KK-04 | echt | S. 2, Z. 39 wörtlich. |
| KK-05 | echt | S. 2, Z. 40 bis 41 "delivery ... are modelled" wörtlich. |
| KK-06 | echt | S. 2, Z. 48 bis 49 wörtlich. |
| KK-07 | echt | S. 2, Z. 62 wörtlich. |
| KK-08 | echt | S. 3, Z. 70 bis 71 wörtlich. |
| KK-09 | echt | S. 3, Z. 88 wörtlich. |
| KK-10 | echt | S. 3, Z. 90 wörtlich. |
| KK-11 | echt | S. 3, Z. 101 "camples" wörtlich. |
| KK-12 | echt | S. 4, Z. 127 verweist auf Table S1, die Datenbank ist Table S2. |
| KK-13 | echt | S. 4, Z. 128 "subdivised" wörtlich. |
| KK-14 | echt | S. 5, Z. 147 "(DIC mit Index la bis lu) sample" am Seitenbild. |
| KK-15 | echt | S. 5, Z. 159 "minimizing Eq. (1)", Eq. 1 ist der Korrekturfaktor, Eq. 2 die Minimierung. |
| KK-16 | echt | Supp. S. 16 Kopfzeile "Lattitude". |
| KK-17 | echt | Supp. S. 17 Darling12 138°17'6.00"E bei gleicher Breite wie Darling11 mit 144°17'6.00"E. |
| KK-18 | echt | S. 6, Z. 189 wörtlich. |
| KK-19 | echt | S. 6, Z. 191 "HSI" wörtlich. |
| KK-20 | echt | S. 6, Z. 193 wörtlich. |
| KK-21 | echt | S. 6, Z. 198 "The samples ... reflects" wörtlich. |
| KK-22 | echt | S. 6, Z. 199 "low rare earth elements" wörtlich. |
| KK-23 | echt | Legende Abb. 1 S. 25 beide Stellen wörtlich. |
| KK-24 | echt | S. 27, Z. 872 bis 873 nennt nur HS1, ACR, YD, Figure S4 zeigt fünf Perioden. |
| KK-25 | echt | Supp. S. 7 Legende Figure S4 wörtlich. |
| KK-26 | echt | S. 7, Z. 220 bis 221 "Epica" wörtlich. |
| KK-27 | echt | S. 7, Z. 233 wörtlich. |
| KK-28 | echt | S. 7, Z. 236 wörtlich. |
| KK-29 | echt | S. 8, Z. 246 "e.i." am Seitenbild. |
| KK-30 | echt | Wortlaut vorhanden, steht am Seitenbild aber in S. 8, Z. 249, nicht Z. 248. |
| KK-31 | echt | S. 8, Z. 261 "Persistance" wörtlich. |
| KK-32 | echt | S. 8, Z. 270 "~763.10³ km²" am Seitenbild. |
| KK-33 | echt | S. 9, Z. 300 "persistence ... reflect" wörtlich. |
| KK-34 | echt | S. 10, Z. 329 bis 330 verweist auf Abschnitt 4.2, die DS-Datenbank steht in Abschnitt 2. |
| KK-35 | echt | S. 10, Z. 334 "2001", Eintrag S. 21, Z. 781 Speirs et al. 2010. |
| KK-36 | echt | S. 10, Z. 338 wörtlich. |
| KK-37 | echt | S. 10, Z. 340 bis 341 wörtlich. |
| KK-38 | echt | S. 10, Z. 341 wörtlich. |
| KK-39 | echt | S. 10, Z. 342 bis 343 "Quake", Eintrag S. 20, Z. 755 Quade. |
| KK-40 | echt | S. 10, Z. 346 wörtlich. |
| KK-41 | echt | S. 11, Z. 354 wörtlich. |
| KK-42 | echt | S. 11, Z. 365 Leerzeichen vor Punkt. |
| KK-43 | echt | S. 11, Z. 366 "Darling sub-basin", Table S2 und S. 11, Z. 371 "Darling Basin". |
| KK-44 | echt | S. 11, Z. 367 "De Deccker", Eintrag S. 17, Z. 557 De Deckker. |
| KK-45 | echt | S. 11, Z. 374 "kry" wörtlich. |
| KK-46 | echt | S. 12, Z. 384 bis 385 Wiederholung wörtlich. |
| KK-47 | echt | S. 12, Z. 396 wörtlich. |
| KK-48 | echt | S. 12, Z. 399 wörtlich. |
| KK-49 | echt | S. 12, Z. 408 wörtlich. |
| KK-50 | echt | S. 13, Z. 426 wörtlich. |
| KK-51 | echt | S. 13, Z. 427 "EAP" ohne Definition im Text. |
| KK-52 | echt | S. 13, Z. 428 wörtlich. |
| KK-53 | echt | S. 13, Z. 439 "De Deccker et al., 2019", Eintrag S. 17, Z. 551 Einzelautor. |
| KK-54 | echt | S. 14, Z. 457 wörtlich. |
| KK-55 | echt | S. 14, Z. 481 wörtlich. |
| KK-56 | echt | S. 16, Z. 501 "SUPPLENTARY" am Seitenbild. |
| KK-57 | teilweise echt | 18 Einträge mit gedruckten RTF-Codes bestätigt (Seitenbild S. 16, Z. 528), aber Z. 528 gehört zu Bullard and McTainsh 2003, nicht Bryant 2003, und gedruckt steht "\uc0舑{}", nicht das zitierte Zeichen. |
| KK-58 | echt | Eintrag S. 18, Z. 630 bis 632 wird nicht zitiert, Text nennt nur "Gaiero, 2007" (S. 8, Z. 274; S. 26, Z. 862). |
| KK-59 | echt | S. 20, Z. 728 bis 729 ohne Band und Seiten. |
| KK-60 | echt | S. 20, Z. 748 "Environùental" wörtlich. |
| KK-61 | echt | S. 20, Z. 763 "Turkian" wörtlich. |
| KK-62 | echt | S. 21, Z. 800 "Sudgen" gegen S. 8, Z. 266 "Sugden". |
| KK-63 | echt | S. 22, Z. 844 bis 846 im APA-Stil abweichend. |
| KK-64 | echt | S. 26, Z. 857 bis 858 "refs. Table S1", Eiskernwerte stehen in Table S4. |
| KK-65 | echt | S. 26, Z. 863 wörtlich. |
| KK-66 | echt | S. 26, Z. 865 bis 866 nennt Table S4 für Quellsignaturen, diese stehen in Table S3. |
| KK-67 | echt | S. 28, Z. 875 "Histograms", Abb. 4 zeigt Balken. |
| KK-68 | echt | S. 28, Z. 876 "(Table S4)", Werte stammen aus Table S5. |
| KK-69 | echt | Supp. S. 5 Legende Figure S3 wörtlich. |
| KK-70 | echt | Supp. S. 10 y-Achse "PAS EDC Contribution ..." am Seitenbild. |
| KK-71 | falsch | "x 1000" steht nur in der Textschicht von Supp. S. 10, im gerenderten Seitenbild ist im Panel AUS unten rechts keine solche Beschriftung sichtbar. |

## 2. Literaturvorschläge

| Vorschlag | Kennung | Im Verzeichnis? |
|---|---|---|
| Lambert et al. 2008 | GB-06 | ja (S. 19, Z. 676 bis 678) |
| Siggaard-Andersen et al. 2007 | GB-07 | nein |
| Marino et al. 2008 | GB-07 | nein |
| Vallelonga et al. 2010 | GB-07 | nein |
| Delmonte et al. 2004a, Earth-Science Reviews | GB-38 | nein |
| Marx et al. 2005 | GB-22 | nein |
| Marx and Kamber 2010 | GB-22 | nein |
| McGowan et al. 2005 | GB-22 | nein |
| Diaz et al. 2018 | GB-22 | nein |
| Aarons et al. 2017 | GB-22 | nein |
| Bory et al. 2010 | GB-22 | nein |
| Gili et al. 2016 | GB-48 | nein |

## 3. Doppelungen

Keine zwei Kennungen mit gleichem Fundort und gleichem Gegenstand. Gleicher Fundort, aber verschiedener Gegenstand: GB-48 und KK-42 (S. 11, Z. 365), GB-52 und KK-49 (S. 12, Z. 408), GB-36 und KK-27 (S. 7, Z. 233), GB-01 und KK-02 (S. 1, Z. 19).

## 4. Fundorte

Gezählt wird der erste Fundort je Kennung am Seitenbild.

## Zählungen

| Größe | Wert |
|---|---|
| Kennungen geprüft | 133 (62 GB, 71 KK) |
| echt | 127 |
| teilweise echt | 5 |
| falsch | 1 |
| nicht prüfbar | 0 |
| Literaturvorschläge | 12 (ja 1, nein 11) |
| Doppelungen | 0 |
| Fundorte genau | 132 |
| Fundorte 1 bis 2 Zeilen daneben | 1 |
| Fundorte weiter daneben | 0 |
