# Verifikation des Gutachtens zu egusphere-2025-5046

Grundlage: Manuskript (29 S.) und Supplement (22 S.), Seitenbilder in seiten/ und supplement/seiten/, eigene 300-dpi-Renderings der Abbildungsseiten (vf/r/), Zeilenzuordnung aus den gedruckten Randnummern (vf/zeilen.tsv; Gleichungsbereiche S. 4, 5 und 8 am Seitenbild nachgezählt), Tabellen S1 bis S5 mit Python ausgelesen (vf/s1.json, vf/s2.json), Literatur über WebFetch und WebSearch. Alle 119 Zitatfelder wurden automatisch gegen den Text gesucht und an der angegebenen Zeile verortet.

## 1. Urteile je Kennung

| Kennung | Urteil | Beleg (ein Satz mit Seite und Zeile) |
|---|---|---|
| GB-01 | echt | Zitate p. 1, l. 19 bis 20, p. 7, l. 220 bis 221 und p. 14, l. 472 bis 473 wörtlich vorhanden, Suchbegriffe 0 Treffer, "database" 2 Treffer (p. 4, l. 129; p. 10, l. 329), Lücke p. 4, l. 113, 1800/8 = 225 und 1200/9 = 133,3 (Python). |
| GB-02 | echt | Zitat p. 2, l. 36 bis 38, einzige Quelle Martínez-García et al. (2014) in l. 40; deren Abstract enthält den Satz zum Sedimentkern (boris.unibe.ch/57917). |
| GB-03 | echt | p. 2, l. 41 "~20 to 40 ppmv"; Lambert 2015: "~20 ppm" (frühere Schätzungen bis 40 % von 80 bis 100 ppm nur in der Einleitung), Lambert 2021: "between 12 and 29 ppmv" und "About one quarter" (Volltexte gelesen). |
| GB-04 | echt | Zitat p. 2, l. 45 bis 46; Abstract Lambert 2008: "the sources and lifetime of dust are the main factors" und "a strengthening of South American dust sources". |
| GB-05 | echt | Ziele p. 3, l. 91 bis 98 ohne Eisenbezug; "iron", "fertili", "HNLC", "pCO2" in p. 7 bis 15 0 Treffer; einzige Spur p. 15, l. 491. |
| GB-06 | echt | Zitat p. 2, l. 51 bis 52; Abstract Engelbrecht 2019 enthält "generally wetter during the LGM", keine Treffer für westerl, circulation, ocean. |
| GB-07 | echt | p. 2, l. 63; Abstracts Delmonte 2008 (Sr-Nd-Herkunft) und 2017 (Dome B, Korngrößen) ohne Flussverhältnis; Lambert 2008: "approximately 25-fold increase in glacial dust flux". |
| GB-08 | teilweise echt | Aarons 2017 und Struve 2022 fehlen im Verzeichnis (p. 16 bis 22, 0 Treffer), Zitat Aarons wörtlich bestätigt; nicht zutreffend ist, dass Struve et al. das Mischmodell auf REE rechnen: MixSIAR nutzt nur Nd, Sr, Pb, die REE dienen nur ergänzend. |
| GB-09 | echt | Suppl. p. 17, Seitenbild: sechs Zeilen "this study", alle "Etosha Pan", Längen 15,29 W bis 16,836 W, Sossusvlei 24,76 S, Li-Zeilen 15° 50' bis 15° 53' E; Methodenteil p. 4, l. 104 bis 105 nennt nur Literaturmuster. |
| GB-10 | echt | Zitat p. 4, l. 110 bis 111; Table S1: 77 von 240 Abständen unter 60, 60 über 140, Median 98, Mittel 128,5, Maximum 2280 (23104 bis 25384), vier Doppelalter (Python). |
| GB-11 | echt | p. 4, l. 111 EDC3, Periodengrenzen p. 6, l. 185 bis 188 nach Veres et al. 2013, Titel "(AICC2012)" p. 21, l. 819 bis 820. |
| GB-12 | echt | "cf" 4 Treffer (p. 4, l. 119, 122; p. 5, l. 154, 157), "correction factor" 2 (l. 120, 154), Supplement 0; keine Werte angegeben. |
| GB-13 | echt | p. 5, l. 142 bis 145 (13 mal 217), l. 157 variiert nur cfi und Dusti; Table S2: AUS 107, ANT 4, CWA 5 von 217 (Python). |
| GB-14 | teilweise echt | Die vier Fehlverweise stimmen (p. 4, l. 127; p. 26, l. 858 und 865; p. 28, l. 876; Titel Suppl. p. 11, 16, 20, 21, 22); die Nebenangabe "22 occurrences" trifft nicht zu, es sind 23 (S5 in p. 7, l. 218 nach Zeilenumbruch), also 19 korrekte. |
| GB-15 | echt | Darling26 = Murray29 und Darling29 = Murray24 in allen 13 Werten, einzige Dubletten über 217 Zeilen; Zählung PAT 39, CWA 5, PAP 14, SAF 23, AUS 107, NZ 25, ANT 4 gegen p. 4, l. 131 bis 133 (AUS 106, ANT 5). |
| GB-16 | echt | p. 4, l. 136 bis 137 "PSA end-members", Titel Table S1 "217 PSAs" (Suppl. p. 11), Table S2 "Table of PSAs database", Table S3 "PSA end-members". |
| GB-17 | echt | Zitat p. 5, l. 160 bis 161; 240 von 241 Zeilen summieren auf mindestens 99,5 (Python); p. 5, l. 159 "minimizing Eq. (1)"; keine MATLAB-Version (l. 140). |
| GB-18 | teilweise echt | p. 5, l. 144 bis 145 (n = 14 gegen 13) und keine Angabe zur Neuberechnung von EDML (p. 12, l. 403 bis 409) bestätigt; die Spanne "0.4 to 15.6 points" stimmt nicht, kleinste Differenz in Table S5 ist 0,2 (HS1 PAP), 15,6 ist ein Frühholozän-Vergleich. |
| GB-19 | echt | p. 5, l. 153 bis 165 beschreibt PDFs, Table S1 und S5 enthalten nur Mediane und Mittel, kein Streumaß; l. 163 bis 164 ohne Wert. |
| GB-20 | echt | Fig. S2 (Suppl. p. 4) zeigt nur nssCa, δ18O, d-excess; Verhältnisse 0,091, 0,068, 0,122 und 0,453, 0,340, 0,611 nachgerechnet; Zitate p. 5, l. 167 und p. 6, l. 183 bis 184. |
| GB-21 | echt | p. 5, l. 170 bis 172; kritisches r 0,7079 (df 10) und 0,6835 (df 11), p(0,67) 0,0171 und 0,0122; bei 0,708 fallen 19 Proben, YD n = 7 mit PAT 67,6, AUS 9,1, SAF 17,9 (scipy). |
| GB-22 | echt | Fig. S2 (Suppl. p. 4): Achsen "nssCa2+ flux", "δ18O", "deuterium excess" ohne Einheit, Panel B ohne Zonen, Legende Suppl. p. 3 ohne Erklärung. |
| GB-23 | echt | p. 6, l. 174 bis 175; Table S1 129 Zeilen unter 14 kyr, 38/(129 + 38) = 22,8 %; ausgeschlossene Proben nirgends gelistet. |
| GB-24 | echt | Seitenbilder Suppl. p. 11 und 13: R = 0,66 bei 2888, 3267 und erster Zeile 10511, deren Summe 93,5; Doppelalter 3559, 10511, 12841, 28709. |
| GB-25 | echt | Titel Suppl. p. 11 "279 DIC" und "217 PSAs" gegen 241 Zeilen; p. 6, l. 183 bis 184 nennt "flux" und Intervalle, die Table S1 nicht enthält. |
| GB-26 | echt | Zitat p. 6, l. 194; p. 4, l. 112 (2 bis 3 Jahre); Paare 3559 (86,7/0,0), 10511, 12841, 28709 bestätigt; Holozän 23 von 116 PAT = 0, Lag-1 0,12, mittlere Nachbardifferenz 33,6 gegen 10,7 (Python). |
| GB-27 | echt | Zitat p. 6, l. 196 bis 197; Table S2 hat 7 PAT-Zeilen Valdes/Puerto Madryn, "Darling" nur in 45 Zeilen Table S2; keine DS-Ergebnisse für p. 11, l. 366 und p. 12, l. 385 bis 398. |
| GB-28 | echt | p. 7, l. 211 bis 215; Table S1 Altiplano über 90 nur bei 8629 (100,0) und 11228 (97,0), Puna ab 20 % in 8 Holozänzeilen, YD Puna 1,26/Alti 3,27, ACR 5,23/0; Fig. S3 Puna-Spitze etwa 43 % bei 11,1 kyr (Seitenbild). |
| GB-29 | echt | Zitat p. 10, l. 330; Table S1 3654 ANT 33,1, 13412 ANT 1,7, Holozänmittel 0,3; Table S3 ohne ANT. |
| GB-30 | echt | Legende Fig. 1 (p. 25) ohne Auflösung der Kürzel, Zonen in Fig. 1 (p. 24) abwechselnd grau und weiß. |
| GB-31 | echt | Ziffernhöhe 300 dpi: Fig. 1 und 3 16 px (etwa 5,3 pt), Fig. 5 13 bis 14 px, Fig. 4 19 px (eigene Messung, gleiche Umrechnung). |
| GB-32 | teilweise echt | Zitate p. 7, l. 233 und p. 14, l. 477 bis 478, Summen 79,4/79,9/81,9/75,5/66,4/54,9 und 20,6 bis 44,8 nachgerechnet; "Only PAP rises at the ACR" trifft nicht zu, SAF steigt von HS1 4,9 auf ACR 8,0 (Table S5). |
| GB-33 | echt | Table S4 (Suppl. p. 21): 35 Werte, Holozän 8 Taylor Glacier und 14 Berkner Island, kein EDC-Holozänwert; Nachrechnung Holozän 0,71013 und minus 4,99, je Probe Median minus 2,44, 8 von 116 (6,9 %) im Bereich (Python); Zitat p. 8, l. 258 bis 260. |
| GB-34 | echt | p. 8, l. 244 bis 245 "For each time interval"; Fig. 2 (p. 26) zeigt viele Punkte je Intervall (eigene Zählung 35 blau, 20 cyan, 4 grün, 31 dunkelrot), Legende ohne MIS3. |
| GB-35 | echt | Zitat p. 8, l. 251 bis 253 (Seitenbild); Periodenwerte MIS3 bis Spätholozän nachgerechnet (YD 0,70943, minus 5,39), gelber Punkt bei 0,7275/minus 17,9 und grüne bei 0,7105/minus 5,3 und 0,7116/minus 9,8 gemessen, Probe 12227 ergibt 0,7274/minus 17,87. |
| GB-36 | echt | Wortlaut p. 8, l. 271; p. 9, l. 296 und 306; p. 13, l. 450; p. 14, l. 466, 480 und 484 wörtlich bestätigt. |
| GB-37 | echt | p. 9, l. 282 "~11%" gegen p. 7, l. 209 "14%" und Table S5 14,2; Summen 75,9, 79,9/20,1, 81,9, 60,0 gegen l. 276, 294, 295 und p. 10, l. 321 (61 %). |
| GB-38 | echt | Zitat p. 10, l. 338 bis 340; in Abschnitt 4.3 und Fig. 5 keine Kennzahl, kein Test. |
| GB-39 | echt | "bog" p. 10, l. 340 und p. 11, l. 349; "Laguna Potrok Aike" p. 19, l. 692, p. 29, l. 882 und Achse Fig. 5B; SWW erst p. 10, l. 340 bis 341 definiert. |
| GB-40 | echt | Erstzitate Fig. 5 p. 10, l. 340 vor Fig. 4 p. 12, l. 405. |
| GB-41 | echt | p. 11, l. 350 bis 351; Fig. 5B (p. 29) zwischen 0,60 und 0,65 ×10^4 flach bei etwa 17 mT ohne Einbruch. |
| GB-42 | echt | Fig. S3 (Suppl. p. 6) Altiplano-Maximum etwa 66 %, keine 100-%-Spitze bei 8,6 kyr, Spitze etwa 39 % bei 11,9 kyr; Table S1 Altiplano 16,6 und 12,8 bei 12841 gegen p. 11, l. 358. |
| GB-43 | echt | "Gili et al., 2016" p. 11, l. 365 ohne Eintrag (nur Gili 2017, 2022); Aarons, Bory, Diaz, Marx und Kamber (101 Zeilen), Marx 2005, McGowan 2005 ohne Eintrag; Delmonte nur ein Eintrag 2004 gegen "2004a". |
| GB-44 | echt | p. 12, l. 382 verweist auf Fig. S4, diese hat nur ein Holozänpanel (Suppl. p. 8). |
| GB-45 | echt | Zitate p. 13, l. 421 bis 424; Table S5: ACR PAT +6,4, YD +4,7, YD SAF +6,4, Holozän minus Frühholozän EDML minus 13,7/+12,3, gleichartig minus 15,6/+14,1 (Python); Fig. 4 Balken passen. |
| GB-46 | echt | Zitat p. 12, l. 407 bis 408 "8 and 7"; YD-Block Suppl. p. 13 hat 9 Zeilen, Mittel 63,06/4,52/14,63/14,50/3,28 = Table S5. |
| GB-47 | echt | Schluss p. 14, l. 472 bis p. 15, l. 492: Holocene, isotop, Sr, Nd, validat, REE 0 Treffer, "nterglacial" nur l. 473, 474, 492. |
| GB-48 | echt | p. 14, l. 486 bis 487 gegen p. 13, l. 424 bis 425 "geographic positioning of the two sites" und p. 12, l. 416. |
| GB-49 | echt | Zitat p. 16, l. 494 bis 496; code, GitHub, Zenodo, repository, 10.5281 im Text außer "CODE" und im Supplement 0 Treffer. |
| GB-50 | echt | p. 16, l. 497 "P.B" passt zu keinem der sieben Autoren (p. 1, l. 4 bis 5), N.M. ohne Rolle, "St. B", "St.B.", "Si.B". |
| GB-51 | echt | Seitenbild p. 16, l. 528 zeigt "471\uc0舑{}501 ... ra\"; 33 Escape-Folgen und 18 Zeilen mit Endbackslash in p. 16 bis 22 (Python), Formatfälle p. 17, l. 584 bis 585 usw. bestätigt. |
| GB-52 | echt | Fig. 2 (p. 26): Legende "Iso Early Holocene" und "Iso Holocene", kein MIS3, Label "Southern Central Western Argentina"; Table S4 nur "Iso Holocene". |
| GB-53 | echt | Fig. 3 "Holocene" zeigt Frühholozän (SAF-Maximum 54, NZ 90, PAT-Median etwa 55 = Table S1 7,5 bis 11,7 kyr), Fig. S4 "Early Holocene" zeigt Spätholozän (SAF 73,5, NZ 61,7, PAP 62,7). |
| GB-54 | echt | p. 27, l. 872; Fig. 3 Holozän SAF-Whisker etwa 25 % mit Punkten bis 54 %, LGM SAF-Whisker etwa 14 % mit Punkten 28 und 35 %. |
| GB-55 | echt | Fig. 5 (p. 29) ohne Zeitachsentitel, blaues Band etwa 0,8 bis 1,14 ×10^4, Legende p. 29, l. 880 bis 882 ohne Erklärung der Bänder. |
| KK-01 | echt | p. 1, l. 15 "Dust deposits in ice cores provides". |
| KK-02 | echt | p. 1, l. 19 "for the first-time". |
| KK-03 | echt | p. 1, l. 20 "Marine isotope 3", p. 6, l. 184 "Marine Isotope Stage 3". |
| KK-04 | echt | p. 1, l. 27 "EDML" ohne Auflösung; "Dronning" nur p. 21, l. 789 und 813. |
| KK-05 | echt | p. 2, l. 40 bis 41 "are modelled". |
| KK-06 | echt | p. 2, l. 62 "fluxes is low". |
| KK-07 | echt | p. 3, l. 71 "than REE ratio". |
| KK-08 | echt | p. 3, l. 73 "multi-decadal" gegen 60 bis 140 Jahre p. 4, l. 110 bis 111. |
| KK-09 | echt | p. 3, l. 88 bis 91 mit gesperrten Bindestrichen und "33.6 kyr to 2.8 kyr" gegen Table S1 2852 bis 33699. |
| KK-10 | echt | p. 3, l. 101 "camples". |
| KK-11 | echt | p. 4, l. 128 "subdivised" (Seitenbild). |
| KK-12 | echt | p. 4, l. 138 "matrixes (Eq.2)". |
| KK-13 | echt | p. 5, l. 145 bis 146 "For any given time step." als Fragment (Seitenbild). |
| KK-14 | echt | Suppl. p. 16 Überschrift "Puna AltiPlano (PAP)" gegen p. 4, l. 129 bis 130. |
| KK-15 | echt | Suppl. p. 17 Darling12 "138°17'6.00"E" bei Breite von Darling11, alle übrigen Darling-Zeilen 141° bis 148° E. |
| KK-16 | echt | "New-Zealand" in Suppl. p. 19 Überschrift, Table S3 Zeile 4 und Fig. 2 (p. 26); Haupttext nur "New Zealand". |
| KK-17 | echt | p. 6, l. 191 "HSI"; sonst 24 mal "HS1" (16 Haupttext, 8 Supplement). |
| KK-18 | echt | p. 6, l. 193 "(averages contributions)". |
| KK-19 | echt | p. 6, l. 198 "reflects". |
| KK-20 | echt | p. 6, l. 199 "LREE (low rare earth elements)". |
| KK-21 | echt | p. 7, l. 213 und p. 9, l. 290 "South Altiplano" gegen p. 4, l. 130 und p. 11, l. 358, 362. |
| KK-22 | echt | Legende Fig. 1 (p. 25) "between 2852 to", "mobile average" auch p. 29, l. 882 und Fig. S5 (Suppl. p. 9). |
| KK-23 | echt | p. 7, l. 220 "Epica Dome C", Table S4 "Epica dome C". |
| KK-24 | echt | p. 7, l. 233. |
| KK-25 | echt | p. 7, l. 236 "already describes". |
| KK-26 | echt | p. 8, l. 246 "e.i. Eq.3". |
| KK-27 | echt | p. 8, l. 249 "is represents". |
| KK-28 | echt | p. 8, l. 261 "Persistance". |
| KK-29 | echt | p. 8, l. 266 "Sugden" gegen Eintrag p. 21, l. 800 "Sudgen". |
| KK-30 | echt | p. 8, l. 270 "~763.10³ km²" (Seitenbild). |
| KK-31 | echt | p. 8, l. 272 "SSA- to EDC". |
| KK-32 | echt | p. 9, l. 277 "(i.e., Albani". |
| KK-33 | echt | p. 9, l. 300 bis 301 "reflect", "westerlies -a system". |
| KK-34 | echt | p. 9, l. 303 bis 304 "2.7 kyr BP" gegen jüngste Probe 2852. |
| KK-35 | echt | p. 10, l. 311 «wet scavenging», l. 313 "of Indian Ocean". |
| KK-36 | echt | p. 10, l. 329 bis 330 verweist auf 4.2, McMurdo steht nur p. 4, l. 133. |
| KK-37 | echt | p. 10, l. 334 "Speirs et al., 2001", Eintrag p. 21, l. 781 mit 2010. |
| KK-38 | echt | p. 10, l. 338 "~9 kyrs", p. 11, l. 374 "kry". |
| KK-39 | echt | p. 10, l. 341 "Moreno et al. (2010)" in Klammer. |
| KK-40 | echt | p. 10, l. 342 bis 343 "Quake", Eintrag p. 20, l. 755 Quade. |
| KK-41 | echt | p. 10, l. 346 "particle". |
| KK-42 | echt | p. 11, l. 354 "are". |
| KK-43 | echt | p. 11, l. 365 Leerzeichen vor Punkt. |
| KK-44 | echt | p. 11, l. 366 "As far as". |
| KK-45 | echt | p. 11, l. 367 "De Deccker". |
| KK-46 | echt | p. 11, l. 376 "El-Nino". |
| KK-47 | echt | p. 12, l. 384 bis 385 doppelte Phrase. |
| KK-48 | echt | p. 12, l. 396 "few", l. 397 bis 398 offene Klammer. |
| KK-49 | echt | p. 12, l. 399 "their ... of their". |
| KK-50 | echt | p. 12, l. 408 "number samples". |
| KK-51 | echt | p. 13, l. 426 "from Patagonia dust". |
| KK-52 | echt | p. 13, l. 427 bis 428, "EAP" einziger Treffer l. 427. |
| KK-53 | echt | p. 13, l. 439 "De Deccker et al., 2019", Eintrag p. 17, l. 551 Einzelautor. |
| KK-54 | echt | p. 13, l. 449 bis 450; Fig. S2 nur EDC, Fig. S5 nur Anteile (Suppl. p. 3, 9). |
| KK-55 | echt | p. 14, l. 457. |
| KK-56 | echt | p. 16, l. 501 "SUPPLENTARY" und unvollständiger Satz. |
| KK-57 | echt | p. 16, l. 536 "cuaternarios". |
| KK-58 | echt | Eintrag p. 18, l. 630 bis 632 nirgends als "Gaiero et al., 2007" zitiert (p. 8, l. 274 und p. 26, l. 862 zitieren den Einzelautoreintrag p. 18, l. 619). |
| KK-59 | echt | p. 20, l. 748 "Environùental". |
| KK-60 | echt | p. 26, l. 859 und 863. |
| KK-61 | echt | Fig. 2 Achse "0,700" (p. 26), Fig. 3 "0,00" bis "100,00" (p. 27). |
| KK-62 | echt | p. 28, l. 875 "Histograms". |
| KK-63 | echt | Legende Fig. S4 (Suppl. p. 7) "Antarctica Cold Reveal", "Heindrich", "Marine Isotope 3". |
| KK-64 | echt | Achsentitel Fig. S5 (Suppl. p. 10) "PAS EDC Contribution and PSA EDML Contribution ( in %)". |

## 2. Literaturvorschläge: schon im Literaturverzeichnis?

| Vorgeschlagene Arbeit | Kennung | Im Verzeichnis |
|---|---|---|
| Aarons et al. (2017) | GB-08, GB-43 | nein |
| Struve et al. (2022) | GB-08 | nein |
| Lambert et al. (2008) als Quelle des Faktors 25 | GB-07 | ja (p. 19, l. 676) |
| Gili et al. (2016) | GB-43 | nein |
| Bory et al. (2010) | GB-43 | nein |
| Diaz et al. (2018) | GB-43 | nein |
| Marx and Kamber (2010) | GB-43 | nein |
| Marx et al. (2005) | GB-43 | nein |
| McGowan et al. (2005) | GB-43 | nein |
| Coppo et al. (2022) in Einleitung und Schluss | GB-01, GB-47 | ja (p. 16, l. 541) |
| Paleari et al. (2019) im Schluss | GB-47 | ja (p. 20, l. 722) |
| Delmonte et al. (2007) im Schluss | GB-47 | ja (p. 17, l. 565) |
| Lisé-Pronovost et al. (2015) als Einschub | GB-41 | ja (p. 19, l. 690) |

Zählung: 13 Vorschläge, 5 ja, 8 nein. Neue, bisher nirgends zitierte Literatur: 2 (Aarons 2017 wird im Supplement benutzt, Struve 2022 nirgends), beide nein.

## 3. Doppelungen (gleicher Fundort, gleicher Gegenstand)

| Paar | Fundort | Gegenstand |
|---|---|---|
| GB-16 / GB-25 | Suppl. p. 11, Titel Table S1 | "217 PSAs" soll "217 DS" heißen |
| GB-20 / GB-25 | p. 6, l. 183 bis 184 | "and flux": Table S1 enthält keine Flüsse |
| GB-33 / GB-52 | Fig. 2 und Legende p. 26 | Kerne der offenen Symbole nicht benannt |
| GB-34 / GB-52 | Fig. 2, Legende | fehlender MIS3-Eintrag |

Zählung: 4 Paare, jeweils Teilgegenstand mit Querverweis, keine vollständige Doppelung.

## 4. Fundorte

| Klasse | Anzahl |
|---|---|
| genau | 119 |
| um 1 bis 2 Zeilen daneben | 0 |
| weiter daneben | 0 |

Davon nur nach Seite und Element verortet (Supplement, Abbildungen, Legende Fig. 1): 9 (GB-22, GB-30, GB-31, KK-14, KK-15, KK-16, KK-61, KK-63, KK-64). Die Zeilen in den Gleichungsbereichen p. 4, l. 125 bis 138, p. 5, l. 139 bis 146 und p. 8, l. 244 bis 255 wurden am Seitenbild nachgezählt; dort ist text.json verschoben, die Angaben des Gutachtens stimmen.

## 5. Zählungen je Urteil

| Urteil | Anzahl |
|---|---|
| echt | 115 |
| teilweise echt | 4 (GB-08, GB-14, GB-18, GB-32) |
| falsch | 0 |
| nicht prüfbar | 0 |
| gesamt | 119 (55 GB, 64 KK) |
