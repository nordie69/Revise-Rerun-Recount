# Verifikation des Gutachtens zu egusphere-2025-5046

Grundlage: Manuskript (29 S.), Supplement (22 S.), text.json beider Dokumente, Seitenbilder in seiten/ und supplement/seiten/, eigene 300-dpi-Renderings der Abbildungsseiten (vf/render/). Zeilennummern an den gedruckten Randnummern der Seitenbilder bestätigt (S. 4, 5, 8, 10, 16, 20 als Bild geprüft; übrige Seiten ohne Abweichung zwischen Randanker und Zeilenfolge). Zahlen mit Python aus Table S1 (241 Zeilen geparst), Table S2 (217 Zeilen), Table S3, S4, S5 (Skripte in vf/skripte/). Literatur: Delmonte et al. 2010 QSR (taldice.org, Volltext), Davies et al. 2020 (ORE Exeter, Abstract), Kok et al. 2021 (ACP, Volltext-PDF, Table 2).

## 1. Urteil je Kennung

| Kennung | Urteil | Beleg (ein Satz mit Seite und Zeile) |
|---|---|---|
| GB-01 | echt | S. 1 Z. 18 und S. 6 Z. 182 "33.7 to 2.9", S. 3 Z. 90 bis 91 "33.6 kyr to 2.8 kyr", S. 4 Z. 109 bis 110 "2852 to 33699", S. 9 Z. 304 "until 2.7 kyr BP"; Table S1 reicht von 2852 bis 33699. |
| GB-02 | echt | Prioritätsaussagen S. 1 Z. 19, S. 3 Z. 74 bis 75, S. 7 Z. 220, S. 14 Z. 472 wörtlich vorhanden; nirgends ist eine Literatursuche beschrieben. |
| GB-03 | echt | S. 3 Z. 92 Zitat vorhanden; Delmonte et al. 2010 QSR 29, 256 bis 264 nennt interglaziales Feld 87Sr/86Sr 0.710030 ± 0.000759, eNd 6.7 ± 2.3 (glazial 1.5 ± 2.2, Vorzeichen negativ) und "East Australia ... or the low-latitude high Andean plateaus"; das Verzeichnis (S. 17 Z. 572 bis 575) enthält nur Delmonte 2010 JQS. |
| GB-04 | echt | S. 4 Z. 110 bis 111 "60 to 140 years"; Table S1: von 240 Abständen 77 unter 60 yr, 4 gleich 0 (3559, 10511, 12841, 28709 doppelt, 3559 am Bild Suppl. S. 11 bestätigt), Maximum 2280 yr (23104 bis 25384), Z. 113 nennt die Lücke. |
| GB-05 | echt | S. 4 Z. 111 EDC3, S. 6 Z. 188 Veres et al. 2013 (AICC2012); für EDML und Potrok Aike (Abb. 5, S. 29) ist keine Chronologie genannt. |
| GB-06 | teilweise echt | Echt: Z. 127 Table S1 statt S2, Z. 159 Eq. (1) statt (2), Z. 215 Abb. 1 zeigt nur PAP gesamt (Bild S. 24), Z. 329 bis 330 Section 4.2, Z. 382 Figure S4 (Boxplots), Z. 449 bis 450 Figure S5 zeigt keine Deposition (Bild Suppl. S. 10), S. 26 Z. 858 und 865, S. 28 Z. 876 falsche Tabellen; nicht tragfähig ist der Teil zu S. 6 Z. 183, weil Table S1 die Einzelwerte nach den genannten Intervallen gegliedert enthält und parallel zu Abb. 1 korrekt verwiesen ist. |
| GB-07 | echt | S. 4 Z. 131 bis 132 "AUS; 106" und "ANT; 5"; Table S2 zählt PAT 39, CWA 5, PAP 14, SAF 23, AUS 107, NZ 25, ANT 4 (217), Darling26 = Murray29 und Darling29 = Murray24 in allen 13 Werten und Koordinaten; ANT-Inset Abb. S1 (Suppl. S. 2) zeigt 5 Marker. |
| GB-08 | echt | S. 5 Z. 164 bis 165 Zitat vorhanden; 240 von 241 Zeilensummen in Table S1 liegen innerhalb 0.2 von 100, Zeile 10511 (Suppl. S. 13) ergibt 93.5; keine cfi-Tabelle im Supplement. |
| GB-09 | echt | S. 5 Z. 144 "a vector of 217 components", Z. 145 n = 13; R wird zwischen DIC und Modellmuster berechnet (Z. 168 bis 169); kein Rückgewinnungstest, keine MC-Streuung je PSA berichtet. |
| GB-10 | echt | S. 5 Z. 167 und S. 6 Z. 183 bis 184 kündigen Flüsse an; Abb. S2 (Suppl. S. 4) zeigt nur nssCa2+, d18O und Deuteriumexzess, Table S1 und S5 nur Prozent. |
| GB-11 | echt | S. 5 Z. 171 bis 172 "degrees of freedom = 10"; scipy: rkrit 0.7079 (df 10) und 0.6835 (df 11), p bei R 0.67 = 0.0171 bzw. 0.0122; 19 Proben unter rkrit df 10 (17 Holozän), 9 unter df 11 (alle Holozän); R 0.66 bei 2888, 3267 (Bild Suppl. S. 11) und 10511 (Suppl. S. 13). |
| GB-12 | echt | Table S2 Suppl. S. 17 Z. 5 bis 10: sechs Zeilen "this study", alle "Etosha Pan", Sossusvlei 24,76 S, SuksesL 21,059 S, Längen 15,29 bis 16,836 W; Section 2 beschreibt keine eigene Probenahme. |
| GB-13 | echt | S. 6 Z. 175 Zitat vorhanden; Table S1 hat 129 Proben jünger als 14 kyr, 38/167 = 22.8 %. |
| GB-14 | echt | S. 6 Z. 207 bis S. 7 Z. 208 "~2%"; Table S1 9500 bis 12000 yr: n 33, SAF Mittel 4.32, Median 0.3, Maximum 49.2. |
| GB-15 | echt | S. 7 Z. 214 Zitat vorhanden; Altiplano über 90 nur 8629 (100.0) und 11228 (97.0), sonst 75.7, 58.5, 58.0, 62.7; acht Holozänproben Puna 20.2 bis 29.1; YD (n 9) Puna 1.26, Altiplano 3.27; Altiplano 16.6 und 12.8 bei 12841 gegen S. 11 Z. 358; geglättete Altiplano-Kurve in Abb. S3 (Suppl. S. 6) im YD-Band über null. |
| GB-16 | echt | Gemessen bei 300 dpi: Abb. 1 "0.4" 15 px (5.0 pt), Abb. 5 "0.5" 13 px (4.3 pt), Abb. 2 "EDC" 17 px (5.7 pt), Abb. 4 "H" in "Holo" 18 px (6.0 pt), innerhalb der genannten Unsicherheit. |
| GB-17 | echt | Abb. 3 (S. 27) Holozän-Panel: PAT Box etwa 12 bis 73, Median etwa 55, entspricht Early Holocene aus Table S1 (12.3, 55.2, 73.0; Holozän gesamt 18.4, 58.6, 73.8); Abb. S4 (Suppl. S. 8) "Early Holocene" mit PAT 18.9, 61.7, 80.7 und Maxima PAT 97.9, AUS 94.0, NZ 61.7 = Late Holocene; Punkte jenseits der Whisker (NZ 90.4, PAP 100); Tippfehler in der Legende Suppl. S. 7 vorhanden. |
| GB-18 | echt | Abb. S3 (Suppl. S. 6): Altiplano-Rohmaximum etwa 66 % bei etwa 6.3 kyr, Puna etwa 55 % bei etwa 11.8 kyr; Table S1: Altiplano 100.0 und 97.0, Puna maximal 29.1 (5850), 11 bis 12.5 kyr maximal 20.2. |
| GB-19 | echt | Suppl. S. 11 Legende "th DEPOT ... using 217 PSAs and 279 DIC", Tabelle hat 241 Zeilen. |
| GB-20 | echt | S. 8 Z. 258 Zitat vorhanden; Table S4 (Bild Suppl. S. 21) hat EPICA-Dome-C-Werte nur im LGM, Holozän 8 Taylor Glacier und 14 Berkner Island (0.7090 bis 0.7228, eNd -7.33 bis -14.71); Nachrechnung Eq. 3 und 4: LH 0.7099/-4.06, EH 0.7098/-3.92, LGM 0.7084/-2.39. |
| GB-21 | echt | S. 8 Z. 268 "between ~34 and 29.4 kyr BP"; Davies et al. 2020 Abstract: Maximum bis 33 bis 28 ka zwischen 38°S und 48°S, "around 47 ka" südlich, "350 km wide and 2090 km long" bei 35 ka. |
| GB-22 | echt | S. 9 Z. 276 "~77%", Z. 294 "~79 %" und "~21 %", Z. 295 "84 %", S. 10 Z. 321 "61%", Z. 326 "60%"; aus Table S5 75.9, 79.9, 20.1, 81.9, 60.0; die Zählung "four of the five" untertreibt, da auch 61 gegen 60.0 um 1.0 abweicht. |
| GB-23 | echt | S. 9 Z. 282 "(~11%)", S. 7 Z. 209 "14%", Table S5 NZ LGM 14.2, Median LGM aus Table S1 15.5. |
| GB-24 | teilweise echt | Kok et al. 2021 Table 2 nennt für Antarktis Südafrika 8 (3 bis 13), Australien 18 (6 bis 36), Südamerika 71 (50 bis 90); die "about 10 %" stehen aber nicht im Abstract, sondern in Abschnitt 3.4.1, und der Satz steht S. 10 Z. 322 bis 323, nicht Z. 312 bis 313. |
| GB-25 | echt | S. 11 Z. 365 "Gili et al., 2016" ohne Eintrag; Marx et al. 2005, McGowan et al. 2005, Marx and Kamber 2010, Diaz et al. 2018 (Table S2), Aarons et al. 2017, Bory et al. 2010, "Delmonte et al., 2004a" (Table S4) ohne Eintrag oder eindeutige Zuordnung; Gaiero, Brunet et al. 2007 (S. 18 Z. 630 bis 632) nirgends zitiert, EPICA 2006 nur in der Legende Abb. S2; 101 + 4 + 2 AUS, 6 NZ und 4 ANT Endglieder betroffen. |
| GB-26 | echt | S. 13 Z. 424 Zitat vorhanden; Table S5: EDC Holozän gesamt minus EDML Early Holocene PAT -13.7, AUS +12.3, SAF -0.5 entspricht den Holo-Balken in Abb. 4 (S. 28); Early Holocene gegeneinander -15.6, +14.1, -1.4, NZ +2.6. |
| GB-27 | echt | S. 12 Z. 408 "(8 and 7 samples"; Table S1 YD 9 Proben (11779 bis 12867, 12841 doppelt), ACR 8. |
| GB-28 | echt | S. 13 Z. 422 "(+4 and +6.5%)"; Table S5 PAT ACR +6.4, YD +4.7, SAF ACR -4.4, YD +6.4, AUS -7.4 und -4.5; Abb. 4 Balken entsprechend. |
| GB-29 | echt | S. 14 Z. 466 bis 467 "our data demonstrate", Z. 484 "due to changing atmospheric transport dynamics", S. 9 Z. 296 "likely"; kein Meeresspiegel- oder Schelfflächen-Datensatz wird mit EDC verglichen. |
| GB-30 | echt | S. 16 Z. 494 bis 496 nennt nur Daten "on request", nichts zum Code trotz Überschrift CODE/DATA. |
| GB-31 | echt | S. 8 Z. 244 "For each time interval"; Abb. 2 (S. 26) zeigt viele Punkte je Periode, einzelner gelber Punkt bei etwa 0.7275 und -18 = Nachrechnung YD-Maximum 0.7274/-17.87; Legende "EDC Early Holocene", "EDC Holocene", kein MIS3. |
| GB-32 | echt | Abb. 5 (S. 29) ohne x-Achsentitel; blaues Band etwa 8.0 bis 11.4 kyr, in Legende Z. 880 bis 882 nicht erklärt; graue YD-Oberkante Panel B etwa 13040 gegen 12880 yr in Panel A (300 dpi gemessen). |
| GB-33 | echt | Abb. S2 (Suppl. S. 4): "nssCa2+ flux" und "δ18O" ohne Einheit, Panel B ohne Periodenschattierung. |
| KK-01 | echt | S. 1 Z. 15 "Dust deposits in ice cores provides". |
| KK-02 | echt | S. 1 Z. 20 "the Marine isotope 3 (MIS3)". |
| KK-03 | echt | S. 3 Z. 101 "ice core camples". |
| KK-04 | echt | S. 4 Z. 128 "subdivised into Patagonia" (Bild bestätigt). |
| KK-05 | echt | S. 5 Z. 145 bis 146 Satzfragment "For any given time step." (Bild bestätigt). |
| KK-06 | echt | S. 6 Z. 189 "It contributes for 65-70%". |
| KK-07 | echt | S. 6 Z. 191 "during HSI is marked". |
| KK-08 | echt | S. 7 Z. 236 "This shift already describes by". |
| KK-09 | echt | S. 8 Z. 246 "(Table S3, e.i. Eq.3)" (Bild bestätigt). |
| KK-10 | echt | S. 8 Z. 249 "the mean isotopic signatures is represents by" (Bild bestätigt). |
| KK-11 | echt | S. 8 Z. 261 "Persistance of high-latitude dust source". |
| KK-12 | echt | S. 8 Z. 270 "~763.10³ km²" (Bild bestätigt). |
| KK-13 | echt | S. 9 Z. 302 "until the onset of the LGIT", während S. 3 Z. 90 die LGIT über den ganzen Datensatz spannt. |
| KK-14 | echt | S. 10 Z. 334 "(Speirs et al., 2001)", Eintrag S. 21 Z. 781 ist 2010. |
| KK-15 | echt | S. 10 Z. 342 "(Quake and", Eintrag Quade and Kaplan 2017. |
| KK-16 | echt | S. 11 Z. 367 "De Deccker et al. (2010)", Eintrag De Deckker et al. 2010. |
| KK-17 | echt | S. 11 Z. 374 "(post-7.5 kry". |
| KK-18 | echt | S. 12 Z. 384 bis 385 Wiederholung "suggesting strengthened dust transport from southern Africa". |
| KK-19 | echt | S. 12 Z. 397 bis 398 Klammer nach "(~15.4" wird nicht geschlossen. |
| KK-20 | echt | S. 12 Z. 399 "their low-frequency, high-magnitude nature of their dust emissions". |
| KK-21 | echt | S. 13 Z. 439 "(De Deccker et al., 2019;", Eintrag De Deckker, P., 2019 (Einzelautor). |
| KK-22 | echt | S. 16 Z. 497 "P.B performed the measurements", kein Autor mit Initialen P.B. |
| KK-23 | echt | S. 16 Z. 501 "APPENDIX S. SUPPLENTARY DATA. Supplementary data to this article". |
| KK-24 | echt | S. 16 Z. 528 "471\uc0舑{}501" am Bild; 17 weitere Einträge mit RTF-Codes auf S. 17 bis 22 gezählt. |
| KK-25 | echt | S. 20 Z. 729 Parrenin et al. 2007 endet mit "Clim. Past." ohne Band, Seiten, DOI (Bild bestätigt). |
| KK-26 | echt | S. 20 Z. 748 "Environùental characterization" (Bild bestätigt). |
| KK-27 | echt | S. 20 Z. 763 "Turkian KK (eds)" (Bild bestätigt). |
| KK-28 | echt | S. 21 Z. 800 "Sudgen, D. E." (im Text S. 8 Z. 266 "Sugden"). |
| KK-29 | echt | Abb. S5 (Suppl. S. 10) y-Achse "PAS EDC Contribution and PSA EDML Contribution ( in %)". |

## 2. Literaturvorschläge

| Vorschlag | Kennung | Bereits im Literaturverzeichnis? |
|---|---|---|
| Delmonte et al. (2010) QSR 29, 256 bis 264, doi:10.1016/j.quascirev.2009.05.010 | GB-03, GB-20 | nein (nur Delmonte et al. 2010, J. Quaternary Sci. 25, S. 17 Z. 572 bis 575) |
| Gili et al. (2016) | GB-25 | nein |
| Marx et al. (2005) | GB-25 | nein |
| McGowan et al. (2005) | GB-25 | nein |
| Marx and Kamber (2010) | GB-25 | nein |
| Diaz et al. (2018) | GB-25 | nein |
| Aarons et al. (2017) | GB-25 | nein |
| Bory et al. (2010) | GB-25 | nein |
| Delmonte et al. (2004a) | GB-25 | nein (ein Eintrag Delmonte et al. 2004, Climate Dynamics 23, existiert, ein "2004a" nicht) |

## 3. Doppelungen

| Paar | Gemeinsamer Fundort | Gemeinsamer Gegenstand |
|---|---|---|
| GB-07 und GB-19 | Legende Table S1 (Suppl. S. 11) | Bezeichnung der 217 dust sources als "PSAs" |
| GB-05 und GB-32 | Abbildung 5 (S. 29) | fehlende Angabe der Chronologie des Potrok-Aike-Datensatzes |

## 4. Fundorte

| Kategorie | Anzahl |
|---|---|
| genau | 61 |
| um 1 bis 2 Zeilen daneben | 0 |
| weiter daneben | 1 (GB-24: Z. 312 bis 313 statt Z. 322 bis 323) |

## Zählungen je Urteil

| Urteil | GB | KK | Summe |
|---|---|---|---|
| echt | 31 | 29 | 60 |
| teilweise echt | 2 | 0 | 2 |
| falsch | 0 | 0 | 0 |
| nicht prüfbar | 0 | 0 | 0 |
| gesamt | 33 | 29 | 62 |
