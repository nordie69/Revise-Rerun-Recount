# Verifikation der Befunde des Gutachtens zu egusphere-2025-5046

Geprüft am 2026-10-22 gegen egusphere-2025-5046.pdf (SHA-256 f598b53d...6c722) und Supplement (SHA-256 759cfa14...8ea6). Zeilennummern an den gedruckten Randnummern bestätigt (Seitenbilder S. 4, 5, 8, 16; Interpolation zwischen den Randankern sonst). Tabellen S1 bis S5 aus text.json des Supplements geparst (241 Zeilen S1, 217 Zeilen S2) und an Seitenbildern S. 13 und 21 bestätigt; Abbildungen an den eingebetteten Bildern (pdfimages) und Seitenbildern. Rechnungen in Python (Skripte a1.py bis a4.py, s1.py, s2.py, font.py in vf/). Literatur über WebSearch und WebFetch, Open-Access-Kopien zuerst.

## 1. Urteil je Kennung

| Kennung | Urteil | Beleg (ein Satz mit Seite und Zeile) |
|---|---|---|
| GB-01 | echt | S. 1 Z. 18 und S. 6 Z. 182 nennen 33.7 bis 2.9 kyr BP, S. 3 Z. 90 bis 91 nennt 33.6 bis 2.8, S. 9 Z. 304 nennt 2.7 kyr BP, Tabelle S1 reicht von 2852 bis 33699 yr. |
| GB-02 | echt | "we quantify for the first-time" steht S. 1 Z. 19 ohne Einschränkung, Coppo-Anteile S. 9 Z. 277 bis 278 wörtlich; Vallelonga et al. (2010, Einleitung) gibt für Revel-Rolland et al. (2006) 10 bis 20 % glazial und bis 50 % interglazial an. |
| GB-03 | echt | "We attribute" S. 1 Z. 29, "our data demonstrate" S. 14 Z. 466, "confirm" Z. 480, "due to" Z. 484 wörtlich; Tabelle S2 enthält für PAT nur Aeolian dust, Top soil und <63 µm Seesedimente, kein Schelfsediment. |
| GB-04 | echt | S. 2 Z. 40 bis 41 "~20 to 40 ppmv"; Lambert et al. (2015) Key Points "reduced LGM atmospheric CO2 levels by 20 ppm", Lambert et al. (2021) "between 12 and 29 ppmv", 40 ppmv in keiner Quelle; 40 minus 29 = 11 (38 %). |
| GB-05 | echt | Tabelle S4 (Suppl. S. 21) hat 18 Zeilen Aarons et al. (2017), die Arbeit fehlt im Verzeichnis S. 16 bis 22; Abstract (QSR 162, 60 bis 71) enthält beide zitierten Sätze. |
| GB-06 | echt | S. 4 Z. 110 bis 111 nennt 60 bis 140 Jahre; Abstände in Tabelle S1 0 bis 2280 yr, Median 98, 77 unter 60, 60 über 140, Holozän 43, LGM 134; Gabrielli et al. (2010) nennt ~60 und ~140 Jahre als Periodenwerte. |
| GB-07 | echt | S. 4 Z. 111 EDC3, S. 6 Z. 188 Veres et al. (2013) (AICC2012); für EDML und Potrok Aike ist keine Chronologie genannt (als Frage formuliert). |
| GB-08 | echt | S. 16 Z. 494 bis 496 wörtlich; REE-Rohdaten, cf_i, Unsicherheiten je Element, Code und Beschreibung der sechs Proben "this study" fehlen; Gabrielli et al. (2010) nennt keine Datenablage und nur Gruppenanteile ~0.55, 0.50, 0.40; PANGAEA-Angabe nicht nachgeprüft. |
| GB-09 | echt | S. 4 Z. 131 und 132 nennen AUS 106 und ANT 5; Tabelle S2 enthält AUS 107, ANT 4; Darling26 = Murray29 und Darling29 = Murray24 (gleiche Koordinaten und 13 Werte, Suppl. S. 17 und 18); Figure S1 zeigt 5 ANT-Marker. |
| GB-10 | echt | S. 4 Z. 134 behauptet UCC-Normierung; ANT-Zeilen Suppl. S. 19 Ce/Pr 9.00, 9.01, 9.16, 8.35 gegen Median 0.96 und Maximum 2.77 der übrigen 213; durch UCC geteilt Ce/Pr 0.94 bis 1.03. |
| GB-11 | echt | S. 4 Z. 136 "linear combination of PSA end-members", Titel Tabelle S2 "Table of PSAs database", Tabelle S1 "217 PSAs", Tabelle S3 "PSA end-members" für sieben Mittel; DS-Definition S. 5 Z. 144. |
| GB-12 | echt | S. 5 Z. 143 "217 columns" bei 13 REE; Tabelle S2 AUS 107 von 217 (49.3 %), Darling 45 von 107 (42.1 %); kein Wiederfindungstest im Manuskript. |
| GB-13 | echt | S. 5 Z. 155 bis 156 nennt 2 bis 10 %; Gabrielli et al. (2010) nennt für MREE und HREE 25 bis 35 % (Holozän) und 5 bis 8 % (LGS); Tabelle S1 und S5 nur Mediane bzw. Mittel, Fig. 1 ohne Unsicherheitsband. |
| GB-14 | echt | S. 5 Z. 166 bis 167 kündigt absolute Flüsse an; Fig. 1 (S. 24) zeigt nur "Total Contribution (%)", Figure S2 (Suppl. S. 4) nur nssCa, δ18O und Deuterium-Exzess. |
| GB-15 | echt | S. 5 Z. 171 "p < 0.01 ... degrees of freedom = 10"; kritisches r 0.708 (df 10) bzw. 0.684 (df 11), p(0.67) = 0.017 bzw. 0.012; drei Zeilen R = 0,66 (2888, 3267, erste 10511); 38 von 167 = 22.8 %. |
| GB-16 | echt | Figure S1 (Suppl. S. 2) eingebettet mit 800 × 450 px bei 78 ppi; Beschriftungen "Argentine", "Nouvelle-Zélande", "TERRITOIRE DE LA CAPITALE AUSTRALIENNE". |
| GB-17 | teilweise echt | Sossusvlei (24,76 S) und SuksesL (21,059 S) stehen unter "Etosha Pan", alle sechs Zeilen "this study" mit W (Suppl. S. 17); nicht zutreffend ist die Spanne "15,97 W to 16,836 W", denn Sossusvlei hat 15,29 W. |
| GB-18 | echt | Überschrift Tabelle S1 nennt 279 DIC, die Tabelle hat 241 Zeilen; Doppelalter 3559, 10511, 12841, 28709 mit den genannten Werten (Suppl. S. 11, 13, 14); ausgeschlossene Proben nirgends gelistet. |
| GB-19 | echt | Zählung Tabelle S1: LH 60, EH 56, YD 9, ACR 8, HS1 27, LGM 40, MIS3 41; Tabelle S5 ohne n; Vorbehalt erst S. 12 Z. 407 bis 409. |
| GB-20 | echt | S. 6 Z. 196 bis 197, S. 11 Z. 366, S. 12 Z. 386 wörtlich; weder Tabelle noch Abbildung gibt Werte für Valdes, Darling oder Häufigkeiten der SAF-Systeme; Figure S3 nur S. 11 Z. 355 zitiert. |
| GB-21 | echt | S. 6 Z. 201 bis 202 ordnet PAP vor NZ; Mittel aller 241 Proben NZ 7.85 gegen PAP 6.85, Mittel der sieben Periodenmittel NZ 7.46 gegen PAP 5.64. |
| GB-22 | echt | Tabelle S5 AUS HS1 11.3, ACR 11.1, YD 14.5; PAT+NZ je Probe LGM 79.9 ± 8.9, HS1 81.9 ± 10.0, ACR 75.5 ± 12.6; ACR-PAT 13412 bis 14601 yr Mittel 76.0, erste Werte unter 60 bei 13143 und 13032 (S. 7 Z. 233 bis 236). |
| GB-23 | echt | S. 6 Z. 207 bis S. 7 Z. 208 "~2%"; 33 Proben 9772 bis 11993 yr: SAF Mittel 4.32, Median 0.3, Spitzen 40.3 (10278) und 49.2 (erste 10511). |
| GB-24 | teilweise echt | Altiplano über 90 % nur bei 8629 (100.0) und 11228 (97.0), sonst 75.7, 58.5, 58.0, 62.7; Puna ≥ 20 % in acht Holozänproben (S. 7 Z. 212 bis 216); nicht zutreffend ist "22 samples", im Holozän sind es 20, die 22 gelten nur mit den zwei YD-Zeilen 12841. |
| GB-25 | echt | S. 7 Z. 217 "negligibly"; Tabelle S1 Zeile 3654 ANT 33.1 % und 13412 ANT 1.7 % (Suppl. S. 11 und 13). |
| GB-26 | echt | Eigene Messung an den eingebetteten Bildern: Fig. 1 Achsziffern 13 px bei 247 ppi = 5.3 pt, Fig. 5 11 px bei 249 ppi = 4.4 pt, Fig. 3 knapp unter 6 pt (S. 24, 27, 29). |
| GB-27 | echt | Bildunterschrift Fig. 1 (S. 25 Z. 851 bis 854) nennt nur CWA und Antarktis; Abkürzungen PAT, AUS, "Holo" (Fig. 4), "Iso" (Fig. 2) werden in keiner Bildunterschrift aufgelöst. |
| GB-28 | echt | Fig. 3 links PAT 12.3, 55.2, 73.0 entspricht dem Early Holocene (n = 56); Figure S4 Feld "Early Holocene" PAT 18.9, 61.7, 80.7 entspricht dem Late Holocene (Tabelle S1, Quartile exklusiv). |
| GB-29 | echt | S. 27 Z. 872 "lower and upper extremes"; Fig. 3 links AUS-Whisker 79.8 mit Punkten 84.3, 95.3, 98.1 darüber, Zaun Q3 + 1.5 IQR = 81.2; PAP-Whisker 28.0 mit 39.6, 75.7, 97.0, 100.0. |
| GB-30 | echt | Erste Zeile 10511 (Suppl. S. 13) summiert 93.5, alle anderen 240 Zeilen 99.9 bis 100.1. |
| GB-31 | echt | Tabelle S1 hat zwischen 11779 und 11993 keine Probe und SAF 94.7 bei 12227; Figure S3 (Suppl. S. 6) zeigt Spitzen Etosha ~88, Puna ~55, Altiplano ~39 bei ~11.9 kyr und keine Altiplano-Spitze bei 8.6 kyr. |
| GB-32 | echt | Figure S4 (Suppl. S. 8) hat nur im ersten Feld eine y-Achse; HS1-PAT abgelesen 68.1, 76.1, 80.7 gegen Tabelle S1 67.0, 75.0, 79.4. |
| GB-33 | echt | Tabelle S4: EDC nur LGM (2 Zeilen), Holozän 8 Taylor Glacier und 14 Berkner Island; S. 8 Z. 258 bis 259 wörtlich; nachgerechnet 12227: 0.72745 und -17.87; Holozän je Probe εNd -16.52 bis 2.20, 8 im EDC-Bereich, Periodenmittel 0.7101 und -4.99. |
| GB-34 | echt | S. 8 Z. 268 "~34 and 29.4 kyr BP"; Abstract Davies et al. (2020): "33 – 28 ka from 38°S to 48°S, and earlier, around 47 ka", Maße 350 km und 2090 km für 35 ka. |
| GB-35 | echt | S. 8 Z. 275 bis S. 9 Z. 277 "70-90%"; Krätschmer et al. (2022) "over 90 %", LGM australisch dominiert; Albani et al. (2012) ohne Prozentangaben, "secondary, but significant dust source"; Tabelle 4 des Preprints nicht nachgeprüft. |
| GB-36 | echt | NZ LGM 14.2 (Tabelle S5) gegen "~11%" S. 9 Z. 282; HS1 PAT+NZ 81.9 gegen "84 %" Z. 295; LGM PAT+AUS 75.9 gegen "~77%" Z. 276; Holozän SSA 60.0 gegen 61 % S. 10 Z. 321; YD 9 Zeilen gegen "7" S. 12 Z. 408. |
| GB-37 | echt | S. 9 Z. 286 bis 287 "14–32 %"; Abstract Neff und Bertler (2015) ohne Prozente, "in interior East Antarctica, source contributions are limited and highly mixed" (als Frage formuliert). |
| GB-38 | echt | S. 9 Z. 306 "significantly larger variability" ohne Test; SD PAT LGM 9.9, HS1 10.8, ACR 14.5, YD 29.5, Holozän 32.1; Median R Holozän 0.80, LGM 0.925; Abstand 43 gegen 134 yr; Gabrielli et al. (2010) 25 bis 35 % gegen 5 bis 8 %. |
| GB-39 | echt | Vallelonga et al. (2010) fehlt im Verzeichnis (nur Vallelonga et al. 2002, S. 21 Z. 807); dort "indicate a >50% input from such a local Antarctic dust source" bei interglazialen Proben und "Australian PSAs are not a major component". |
| GB-40 | echt | S. 10 Z. 333 bis 334 "from the east–southeast"; Abstract Speirs et al. (2010) "topographic modification of south-southwesterly airflow"; Peilung Dry Valleys nach Dome C 265°, Wind aus 112.5° weht nach 292.5°, Differenz 27°. |
| GB-41 | echt | S. 10 Z. 339 "matching well" ohne Maß; "SWW" Z. 339 vor Definition Z. 340 bis 341; "Potrok Aike bog" Z. 339 bis 340 und S. 11 Z. 348 gegen "lacustrine sediments in Laguna Potrok Aike" S. 29 Z. 881. |
| GB-42 | echt | Erste Nennungen Fig. 5 S. 10 Z. 340, Fig. 4 S. 12 Z. 405. |
| GB-43 | echt | S. 11 Z. 351 behauptet den Einbruch auch im Potrok-Aike-Signal; Fig. 5B (S. 29) verläuft zwischen 6 und 6.5 kyr flach bei etwa 15 bis 18 mT ohne erkennbares Merkmal. |
| GB-44 | echt | S. 11 Z. 358 "only after approximately 11.2 kyr BP"; Tabelle S1 Altiplano 16.6 und 12.8 % bei 12841 yr (Suppl. S. 13), YD-Mittel Altiplano 3.27 gegen Puna 1.26. |
| GB-45 | echt | Gili et al., 2016 (S. 11 Z. 365) und Speirs et al., 2001 (S. 10 Z. 334) ohne Eintrag, Verzeichnis hat Gili 2017, 2022 und Speirs 2010 (S. 21 Z. 781); "De Deccker et al., 2019" S. 13 Z. 439 gegen De Deckker, P., 2019; Gaiero et al. 2007 (S. 18 Z. 630) nicht zitiert. |
| GB-46 | echt | S. 11 Z. 368 bis 371 wörtlich; Magee et al. (2004) "Abrupt transitions ... (ca. 125 and 12 ka)" und "low intensity of the early Holocene Australian monsoon"; De Deckker et al. (2010) "more particularly during wet phases in Australia". |
| GB-47 | echt | S. 12 Z. 382 zitiert Figure S4 für einen Holozäntrend; Figure S4 hat ein einziges Holozänfeld (Suppl. S. 8); Tabelle S5 EH 9.8, LH 11.6. |
| GB-48 | echt | S. 12 Z. 391 wörtlich; Vickery et al. (2013): Pfannen 57 % der Quellen und 64 % der Fahnen (208 von 328), Flüsse 113 von 328, "more than half of all plume sources" nur für die Namib. |
| GB-49 | echt | Tabelle S5 EDML (Suppl. S. 22) PAT LGM 73.7, HS1 71.6, ACR 62.5, YD 58.4, EH 62.7; Abstract Vanderstraeten et al. (2023) "~68 %", AUS 14 bis 15 %, nach 14.5 kyr unter 50 %, 207 REE-Muster; S. 5 Z. 145 13 statt 14 REE. |
| GB-50 | echt | S. 13 Z. 422 "+4 and +6.5%"; Tabelle S5 ACR +6.4, YD +4.7, YD SAF +6.4; Holozän 49.0 minus 62.7 = -13.7 und AUS +12.3 aus ungleichen Fenstern; Fig. 4 zeigt ACR-Balken höher als YD. |
| GB-51 | echt | S. 13 Z. 435 und Z. 439 bis 440; Abstract Yang et al. (2024) ohne Staub, Aerosol oder Antarktis; Vallelonga et al. (2002) "Pb mined at Broken Hill and smelted at Broken Hill and Port Pirie" und "rock and soil dust Pb contribution of 8-12%". |
| GB-52 | echt | S. 13 Z. 449 "in both cores (Figures S2 and S5)"; Figure S2 zeigt nur EDC-Fluss, Figure S5 nur relative Anteile. |
| GB-53 | echt | Schluss S. 14 Z. 472 bis S. 15 Z. 492 ohne Sr-Nd-Vergleich und ohne Holozän-Konsens; Paleari et al. (2019) nur S. 3 Z. 92 genannt. |
| GB-54 | echt | S. 14 Z. 486 bis 487 "regional climatic dynamics in their respective source areas" gegen S. 13 Z. 425 bis 429 Lage zu Sturmbahn und Polarwirbel. |
| GB-55 | echt | Zwischen Z. 219 und 492 kein "iron", "fertili" oder "CO2" (Suche im Text); S. 15 Z. 491 "implications for biogeochemical fluxes". |
| GB-56 | echt | S. 16 Z. 497 "P.B performed the measurements"; Autorenzeile S. 1 Z. 4 bis 5 ohne Initialen P.B.; N.M. und A.B. nur unter "All authors reviewed". |
| GB-57 | echt | Supplement zitiert Marx and Kamber 2010 (101), Aarons 2017 (18), Bory 2010 (14), Marx 2005 (10), Diaz 2018 (4), McGowan 2005 (2), Delmonte 2004a (2); keine davon im Verzeichnis, Delmonte 2004 nur ohne Suffix; Befund nennt intern sieben, Vorschlag sechs. |
| GB-58 | echt | Steuercodes in 18 Einträgen auf S. 16 bis 22 (z. B. S. 16 Z. 528 am Seitenbild bestätigt); Parrenin et al. 2007 (S. 20 Z. 726 bis 729) ohne Band, Seiten, DOI und ohne neun Koautoren (laut NORA-Eintrag 27 Autoren, Clim. Past 3, 485 bis 497). |
| GB-59 | echt | S. 26 Z. 858 "Table S1", Z. 865 "(Table S4)" für Endglieder, S. 28 Z. 876 "(Table S4)"; Isotopenwerte stehen in S4, Endglieder in S3, Mittel in S5. |
| GB-60 | echt | Legende Fig. 2 (S. 26) trennt "Early Holocene" und "Holocene"; Tabelle S4 hat nur "Iso Holocene"; Australien-Umriss und "EDC YD" im eingebetteten Bild beide #ffc000 (Gutachten nennt #fcc404, Sachaussage gleiche Farbe trifft zu). |
| GB-61 | echt | Fig. 5 (S. 29) x-Achse 0.5 bis 3 ohne Titel und Einheit; blaues Band etwa 0.8 bis 1.14 und graue Zonen ohne Erklärung in der Bildunterschrift Z. 880 bis 882. |
| GB-62 | echt | Tabelle S3 (Suppl. S. 20) Zeilen "S-Puna", "S-Altiplano", "Southern Central Western Argentina (SCWA)", keine ANT-Zeile; Tabelle S5 ANT Holozän 0.3, LH 0.6. |
| GB-63 | echt | Figure S2 (Suppl. S. 4) Achsen "nssCa2+ flux", "δ18O", "deuterium excess" ohne Einheit, Feld B ohne Periodenschattierung. |
| KK-01 | echt | S. 1 Z. 20 "During the Marine isotope 3 (MIS3)". |
| KK-02 | echt | S. 1 Z. 27 "Comparison with the EDML ice core", EDML dort nicht ausgeschrieben. |
| KK-03 | echt | S. 3 Z. 101 "to ice core camples". |
| KK-04 | echt | S. 4 Z. 127 "(Figure S1, and Table S1)", Datenbank steht in Tabelle S2. |
| KK-05 | echt | S. 5 Z. 159 "by minimizing Eq. (1)", Minimierung betrifft Eq. 2. |
| KK-06 | echt | Tabelle S2 (Suppl. S. 17) "Omarur1inf5", "Omarur2inf5" neben "Omaruru3inf5". |
| KK-07 | echt | Tabelle S2 (Suppl. S. 18) aust8 bis aust13 "Murrumbigdee basin". |
| KK-08 | echt | Tabelle S2 (Suppl. S. 16) Blockkopf "Puna AltiPlano (PAP)". |
| KK-09 | echt | Tabelle S2 (Suppl. S. 19) und Tabelle S3 (Suppl. S. 20) "New-Zealand (NZ)". |
| KK-10 | echt | S. 6 Z. 189 "It contributes for 65-70%". |
| KK-11 | echt | S. 6 Z. 191 "during HSI is marked". |
| KK-12 | echt | S. 6 Z. 193 "(averages contributions)". |
| KK-13 | echt | S. 6 Z. 195 "contributing to 47-51% of the total mix". |
| KK-14 | echt | S. 6 Z. 198 "and therefore reflects regional mixed input" mit Subjekt "The samples". |
| KK-15 | echt | S. 6 Z. 199 "LREE (low rare earth elements)". |
| KK-16 | echt | S. 25 Z. 851 "between 2852 to 33699 yr BP". |
| KK-17 | echt | S. 25 Z. 852, S. 29 Z. 882 und Figure S5 (Suppl. S. 9) "mobile average over 9 steps". |
| KK-18 | echt | Legende PAP-Feld Fig. 1 (S. 24) "Raw data". |
| KK-19 | echt | S. 27 Z. 873 nennt HS1, ACR, YD, Figure S4 zeigt EH, YD, ACR, HS1, MIS3. |
| KK-20 | echt | Bildunterschrift Figure S4 (Suppl. S. 7) "Antarctica Cold Reveal", "Heindrich Stadial 1", "Marine Isotope 3". |
| KK-21 | echt | S. 7 Z. 220 "in the Epica". |
| KK-22 | echt | S. 7 Z. 229 "regional climatic evolution (3)" ohne Trennzeichen. |
| KK-23 | echt | S. 7 Z. 236 "This shift already describes by Gili et al. (2022)". |
| KK-24 | echt | S. 8 Z. 246 "e.i. Eq.3" (Seitenbild). |
| KK-25 | echt | S. 8 Z. 249 "is represents by CIR PSA" (Seitenbild). |
| KK-26 | echt | S. 8 Z. 261 "Persistance of high-latitude dust source". |
| KK-27 | echt | S. 8 Z. 270 "~763.10³ km²". |
| KK-28 | echt | S. 8 Z. 272 "those from SSA- to EDC". |
| KK-29 | echt | S. 9 Z. 300 "before 14.5 kyr BP reflect a transport regime". |
| KK-30 | echt | S. 9 Z. 301 "strong westerlies -a system". |
| KK-31 | echt | S. 9 Z. 305 Überschrift in Title Case, 4.1, 4.2, 4.4 in Satzschreibung. |
| KK-32 | echt | S. 10 Z. 311 "«wet scavenging»". |
| KK-33 | echt | S. 10 Z. 312 "trajectories inferred by increased". |
| KK-34 | echt | S. 10 Z. 325 "reduction in SSA input -down to 33%-". |
| KK-35 | echt | S. 10 Z. 327 "i.e., 23% and 14%, respectively vs. 23% and 11%, here -". |
| KK-36 | echt | S. 10 Z. 329 "our Dust Source (DS) database", DS bereits S. 4 Z. 129 eingeführt. |
| KK-37 | echt | S. 10 Z. 329 bis 330 verweist auf "(Section 4.2)", die Datenbank ist in Abschnitt 2 beschrieben. |
| KK-38 | echt | S. 10 Z. 331 "East Antarctic Plateau" ohne Kürzel, S. 13 Z. 427 "at the interior of EAP". |
| KK-39 | echt | S. 10 Z. 338 "centered ~9 kyrs BP". |
| KK-40 | echt | S. 10 Z. 341 "Moreno et al. (2010);" in Klammerzitat. |
| KK-41 | echt | S. 10 Z. 342 "(Quake and", Eintrag Quade and Kaplan 2017. |
| KK-42 | echt | S. 10 Z. 346 "mineral soil-dust particle". |
| KK-43 | echt | S. 11 Z. 353 "had its prime time". |
| KK-44 | echt | S. 11 Z. 354 "Dust emission from PAP are". |
| KK-45 | echt | S. 11 Z. 374 "(post-7.5 kry". |
| KK-46 | echt | S. 11 Z. 376 "El-Nino-Southern Oscillation". |
| KK-47 | echt | S. 12 Z. 384 bis 385 Wortgruppe doppelt. |
| KK-48 | echt | S. 12 Z. 396 "include few substantial inputs". |
| KK-49 | echt | S. 12 Z. 397 bis 398 Klammer vor "~15.4" wird nicht geschlossen. |
| KK-50 | echt | S. 12 Z. 399 "their low-frequency, high-magnitude nature of their dust emissions". |
| KK-51 | echt | S. 13 Z. 426 "receive dust from Patagonia dust brought". |
| KK-52 | echt | S. 13 Z. 428 "mid-latitude air masses incursions". |
| KK-53 | echt | S. 13 Z. 441 bis 442 Einschub mit Gedankenstrich geöffnet und mit " - " geschlossen. |
| KK-54 | echt | S. 14 Z. 457 "redirecting large portion of river catchment". |
| KK-55 | echt | S. 16 Z. 501 "SUPPLENTARY DATA. Supplementary data to this article" ohne Satzende. |
| KK-56 | echt | S. 20 Z. 748 "Environùental". |
| KK-57 | echt | S. 20 Z. 763 "Turkian KK". |
| KK-58 | echt | S. 21 Z. 800 "Sudgen, D. E.". |
| KK-59 | echt | S. 26 Z. 863 "the SAF and AUS domain is more extended than showed". |
| KK-60 | echt | Fig. 2 x-Achse "0,700", Fig. 3 und Figure S4 y-Achse "100,00" (eingebettete Bilder). |
| KK-61 | echt | S. 28 Z. 875 "Histograms representing", dargestellt sind Balken. |
| KK-62 | echt | Figure S5 y-Achsentitel "PAS EDC Contribution and PSA EDML Contribution ( in %)" (Suppl. S. 10). |

## 2. Literaturvorschläge: bereits im Verzeichnis?

| Vorgeschlagene Arbeit | Ort im Gutachten | Im Verzeichnis |
|---|---|---|
| Revel-Rolland et al. (2006) | GB-02 | ja (S. 20 Z. 759) |
| Coppo et al. (2022) | GB-02 | ja (S. 16 Z. 541) |
| Aarons et al. (2017) | GB-05, GB-57 | nein |
| Vallelonga et al. (2010) | GB-39 | nein |
| Delmonte et al. (2004) | GB-33 | ja (S. 17 Z. 561) |
| Fischer et al. (2007) | GB-52 | ja (S. 17 Z. 596) |
| Lambert et al. (2008) | PP-02 | ja (S. 19 Z. 676) |
| Gili et al. (2016) | GB-45 | nein |
| Marx and Kamber (2010) | GB-57 | nein |
| Bory et al. (2010) | GB-57 | nein |
| Marx et al. (2005) | GB-57 | nein |
| Diaz et al. (2018) | GB-57 | nein |
| McGowan et al. (2005) | GB-57 | nein |

## 3. Doppelungen

Keine zwei Kennungen mit gleichem Fundort und gleichem Gegenstand. Teilüberschneidung ohne Doppelung: GB-05 und GB-57 nennen beide das Fehlen von Aarons et al. (2017) im Verzeichnis, GB-05 mit dem Gegenstand fehlende Diskussion (Fundort S. 3 Z. 72 bis 74), GB-57 mit dem Gegenstand fehlende Einträge aller Supplementquellen; GB-57 verweist ausdrücklich auf GB-05.

## 4. Fundorte

Erste Fundortangabe je Kennung gegen die Randnummern geprüft (125 Kennungen): 125 genau, 0 um 1 bis 2 Zeilen daneben, 0 weiter daneben.

## Zählungen

| Urteil | Anzahl |
|---|---|
| echt | 123 (61 GB, 62 KK) |
| teilweise echt | 2 (GB-17, GB-24) |
| falsch | 0 |
| nicht prüfbar | 0 |
| Summe | 125 |

Literaturvorschläge: 13, davon 5 bereits im Verzeichnis, 8 nicht. Doppelungen: 0. Fundorte: 125 genau, 0 um 1 bis 2 Zeilen, 0 weiter daneben.
