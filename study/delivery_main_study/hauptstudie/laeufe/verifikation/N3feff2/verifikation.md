# Verifikation des Gutachtens zu egusphere-2025-4695

Geprüfte Fassung: egusphere-2025-4695.pdf, 37 Seiten, SHA-256 9c80676054f96ecd6f00f4d2a8b5ba568e03c6949e3856d363ac1c4abb42e7bd (identisch mit der im Gutachten genannten Fassung). Zeilennummern an den gedruckten Randnummern der Seitenbilder p. 1 bis 21 bestätigt; Abbildungen an den Seitenbildern (150 dpi) und an eigenen 300-dpi-Renderings (vf/r300) gemessen; Zahlen mit Python nachgerechnet (vf/py); Literatur über WebSearch und WebFetch, soweit erreichbar.

## 1. Urteile je Kennung

| Kennung | Urteil | Beleg (ein Satz mit Seite und Zeile) |
|---|---|---|
| GB-01 | echt | Wortlaut p. 1, l. 3 bis 4 und p. 3, l. 74 bis 75 (Duplikat p. 5, l. 141 bis 142) vorhanden; Suche bestätigt cost 6, time- 5, efficien 4, expens 2, cheap 0 Treffer, alle in Abstract und den beiden Einleitungen. |
| GB-02 | echt | "consistent convergence" steht p. 1, l. 7; Gradientennormierung p. 11, l. 312; in Fig. 8 (p. 29) fehlen 6 der 20 Läufe, alle bei JS unter 0,44. |
| GB-03 | echt | Überschriften p. 1, l. 9 und p. 3, l. 76; difflib über l. 10 bis 75 gegen l. 77 bis 142: je 1153 Wörter, Ähnlichkeit 1,0. |
| GB-04 | echt | "E., 2009" p. 1, l. 11 bis 12 und p. 3, l. 78 bis 79, Eintrag "E., W. D." p. 18, l. 567 bis 568; Suchtreffer ordnen den UNESCO-Bericht D. E. Walling zu (Volltext nicht lesbar, wie im Gutachten angegeben). |
| GB-05 | echt | Zitate p. 1, l. 18 bis 19, p. 2, l. 28, 30, 31 vorhanden; die Titel im Verzeichnis (Kobe p. 19, l. 597; Barker p. 17, l. 519; Wilson p. 21, l. 649; Walden p. 20, l. 641; Blaen p. 17, l. 528) betreffen andere Gegenstände. |
| GB-06 | teilweise echt | Ehlers et al. (2015) und Bernard et al. (2020) existieren mit den genannten Angaben und fehlen im Verzeichnis; nicht zutreffend ist die eingebettete Angabe "thermochron: 0 hits", denn Fox et al. (2014) enthält "thermochronometric" (p. 19, l. 574 bis 575, getrennt). |
| GB-07 | echt | Anspruchssätze p. 2, l. 36 bis 37, l. 58 bis 59 und p. 15, l. 454 bis 455 vorhanden; Suche in p. 1 bis 16 ergibt nur "database" p. 9, l. 257 (RRUFF); die Angabe zum Abstract von Das et al. (2023) war nicht abrufbar. |
| GB-08 | echt | Andrews und Eberl (2012, Marine Geology 291 bis 294, 24 bis 33) testen qXRD-Entmischung an künstlichen Mischungen (USGS-Eintrag), Eberl (2004) wendet sie auf das Yukon-System an; beide fehlen im Verzeichnis, Bezugsstellen p. 2, l. 40 und p. 13, l. 404 bis 406. |
| GB-09 | echt | Zitat p. 2, l. 45 bis 48; der Springer-Abstract von Niu et al. (2020) nennt lineares Mischmodell und "Gaussian first-order approximation", keine Bayes- oder Stichprobenverfahren. |
| GB-10 | echt | p. 2, l. 48 bis 51 (und p. 4, l. 115 bis 118): "Non-Linear Least Squares (NLLS) (a constrained linear regression)", "Generalist", "Maximal" und Rückverweis "NNLS" wörtlich vorhanden. |
| GB-11 | echt | Wortlaut p. 2, l. 61 bis p. 3, l. 62, p. 15, l. 460, 463 bis 468 vorhanden; inferierte Geologie p. 9, l. 270 bis 272; keine Nennung von "glaci" in p. 16, l. 477 bis 489. |
| GB-12 | echt | Python auf text.json: 8 Formen auf -ise (p. 5, l. 150 bis p. 15, l. 459) gegen 22 auf -ize; "centre" p. 12, l. 340 und 341, "center" p. 15, l. 441. |
| GB-13 | echt | Eq. 17 mit k (p. 7, l. 208 bis 209), Eq. 18 und 19 mit n und εk im Priorterm (p. 8, l. 215, 219), t und xy p. 9, l. 262 bis 263, "tracer mineral n" und "sample i" in Fig. 3d (p. 24). |
| GB-14 | echt | "dimensionless form" p. 6, l. 161, ė0 "set to 1" ohne Einheit p. 5, l. 157, σd "0.01 mm/y" p. 10, l. 295, p. 11, l. 325, p. 14, l. 428. |
| GB-15 | echt | "prior misfit" einmal p. 6, l. 184, "model misfit" 16 Treffer ab p. 7, l. 202 (13 Textzeilen und Bildunterschriften Fig. 5, 6, 10). |
| GB-16 | echt | Seitenbild p. 7, l. 189 zeigt exp(s²/L²) ohne Minus, l. 201 zeigt G C_d^-1 ohne Transponierte, l. 205 dagegen G^T. |
| GB-17 | echt | SD mit Eq. 18 p. 8, l. 213 bis 216, Normierung nur p. 11, l. 312 bis 314 ohne Form, Schrittweite und Iterationszahl; Achsen Fig. 6g bis 6i bis 200, Fig. 5g bis 5i bis 100. |
| GB-18 | echt | Eq. 19 p. 8, l. 219 invertiert (G^T C_d^-1 G); bei m = 21 und n = 300 Rang 21, Kondition 8,8e19 (Python), A hat mehr Spalten als Zeilen (p. 6, l. 172). |
| GB-19 | echt | Farbskalen 0,90 bis 1,00 (Fig. 5d), 0,88 bis 1,00 (Fig. 6d), 0,5 bis 1,0 (Fig. 14, 16), 0,80 bis 1,00 (Fig. 15) und überwiegend dunkle Karten bestätigt; Fläche 72,8 km² aus Fig. 4 nachgemessen, Spur(R) = 7,00 im Python-Test; Wortlaut p. 8, l. 235 bis 236. |
| GB-20 | echt | Eq. 22 mit Wurzeln p. 8, l. 239, Spurverhältnis erst p. 14, l. 436; die acht Bezeichnungen (u. a. p. 10, l. 303, p. 11, l. 335, Fig. 5h, Fig. 7 bis 10, 14 bis 16) vorhanden; Wurzel aus 0,87 = 0,933. |
| GB-21 | echt | "sample" 19 Treffer auf 17 Zeilen in p. 9, l. 250 bis p. 14, l. 449 ohne Probenzahl; nur ein datierter Termin p. 14, l. 423 bis 424; Belotti als "unpublished" p. 17, l. 522 bis 523; 13 Altersklassen in Fig. 14. |
| GB-22 | teilweise echt | Messparameter fehlen in p. 9, l. 252 bis 258; nicht zutreffend ist "2 hits ... p. 17, l. 533", denn die Suche ergibt nur "Scandinavia" p. 19, l. 583, p. 17, l. 533 enthält keinen der Begriffe. |
| GB-23 | echt | Maximumnormierung p. 9, l. 260 bis 262; Maximum je Einheit in Fig. 11 gemessen (Antigorit, viermal Quarz, Anorthit/Pyroxen); Zahlenbeispiel mit Python reproduziert (1,00/0,50/0,375 gegen 0,70/0,55/0,425, Gewicht 0,652). |
| GB-24 | echt | "proposed by (Steck et al., 2015)" p. 11, l. 333 bis 334, Steck als Quelle der Basiskarte p. 9, l. 272 und Fig. 4 (p. 25); Kartennamen und "Geology misalignment (m²)" in Fig. 7 (p. 28) vorhanden. |
| GB-25 | echt | "Bündnerschiefer" p. 10, l. 275, "MR g-g" nur p. 14, l. 432 bis 433, fünf Schreibweisen von Zermatt-Saas Fee (p. 10, l. 299; p. 12, l. 340; p. 14, l. 411; Fig. 12) und "Turftgrat", "ecologites" in der Bildunterschrift Fig. 11 (p. 32). |
| GB-26 | echt | Pfeilsymbol ohne Legende in Fig. 1b, 2b, 3b (p. 22 bis 24); in Fig. 2c nur die grüne Skala "low high", in Fig. 2b sieben dunkelgraue Balken ohne Ebene (p. 23). |
| GB-27 | echt | Gemessen (300 dpi): Stockhorn #ff7333, Stockhorn-Aufschlüsse #fd3333, MR-Gneis-Aufschlüsse #ff5933, RGB-Summendifferenzen 26 und 40, alle übrigen Paare über 60 (Fig. 4, p. 25). |
| GB-28 | echt | "ELA estimation" (Fig. 4), "S.,T.,G." und "MR gneiss, mica" (Fig. 5j, 15, 16) ohne Auflösung; Text: ELA 0, S.,T.,G. 0, MR nur p. 14, l. 432 bis 433, ZSF zuerst p. 14, l. 414, JS p. 12, l. 345. |
| GB-29 | echt | Prior gleich wahrem Mittel p. 10, l. 295 und p. 11, l. 325 bis 326; Erzeugung mit dem Vorwärtsmodell p. 10, l. 288; "noise" nur p. 9, l. 255; Schlusssatz p. 16, l. 482 bis 483. |
| GB-30 | echt | µ fehlt p. 10, l. 293 bis 295; SD ohne Parameter p. 11, l. 310 bis 311; Basiswerte fehlen p. 12, l. 367 bis 371; 4.2.1 ohne Parameter p. 13, l. 403; nur "same" p. 14, l. 437. |
| GB-31 | echt | "(Figure 6G versus Figure 6G)" p. 11, l. 317; Knick in Fig. 6g bei etwa 135 Iterationen (Achse 125 bis 150) und Maximum Fig. 6h bei etwa 137 gemessen (p. 27). |
| GB-32 | echt | Fig. 5g: Minimum etwa 197 bei 21 bis 23, Endwert etwa 201; Fig. 6g: Endwert etwa 193 (300 dpi, p. 26, 27); Wortlaut p. 11, l. 320 bis 321. |
| GB-33 | teilweise echt | PCA-Satz p. 12, l. 355 bis 356 und Mischung p. 12, l. 343 bis 344 ohne Regel, Schraffur ohne Definition; nicht zutreffend ist "confiden: 0 hits" für p. 1 bis 37, denn die Legende Fig. 5 (p. 26) trägt "Low-confidence areas". |
| GB-34 | echt | Text "highly blended, intermediate, original" p. 12, l. 348, Titel "Almost fully blended", "Medium blended", "Unblended" und Bildunterschrift "half-way in between" (p. 29). |
| GB-35 | echt | "20 values" p. 12, l. 348 bis 349; je 14 Marker links und Mitte in Fig. 8 bei 300 dpi gezählt, Lücken zwischen 0,272 und 0,338 sowie 0,359 und 0,441 (p. 29); 19 minus 14 = 5. |
| GB-36 | echt | "700 mm/yr" p. 12, l. 352 einziger Treffer, "mm/y" 5 Treffer; y-Achse Fig. 8 bis 700000 ohne Einheit; "pixel" 14 Treffer auf 13 Zeilen ohne Pixelzahl; 1200/4 = 3000/10 = 300 m. |
| GB-37 | echt | Eq. 7 und 8 (p. 6, l. 182, 186) summieren über Tracer mit 1/σd²; Fig. 9 Datenmisfit etwa 3,3e6 bei 21 Tracern (p. 30); Wortlaut p. 12, l. 360 bis 362 und p. 13, l. 382 bis 384. |
| GB-38 | echt | Rangfolge p. 12, l. 363 bis 365; Fig. 7: 197,3 auf 274,8 (plus 39 Prozent), Unsicherheit plus 0,0058; Fig. 9: 197,2 auf 347 (plus 76 Prozent), plus 0,22; "Surprisingly" p. 11, l. 338. |
| GB-39 | echt | Satz p. 12, l. 373 bis p. 13, l. 374; Fig. 10 Zeile 1 (p. 31) fällt monoton von etwa 257 auf 76, kein Wert über 3000 m. |
| GB-40 | echt | Fig. 10 Zeile 3 mit Versatz "+1.974e2", Werte 0,020 bis 0,043, Unsicherheit 0,74015 bis 0,74040, Modellmisfit 1,5614 bis 1,5623, monoton steigend (p. 31); "10-2" auf der Grundlinie p. 13, l. 384. |
| GB-41 | echt | Satz p. 13, l. 387 bis 389 ohne Bezugsgröße; Fig. 5i "1e8", Fig. 10 Zeile 5 "1e7"; Fig. 10 Zeile 5 zeigt Ausreißer nur bei n = 5, Minimum bei 25 (p. 31). |
| GB-42 | echt | "Chrysolite" p. 13, l. 395 gegen "Chrysotile" in Fig. 11, 15, 16 (p. 32, 36, 37); übrige 20 Namen gleich; Chrysotil als Serpentinmineral p. 10, l. 274. |
| GB-43 | echt | Fig. 11 bei 300 dpi gemessen: Antigorit 0,57, Chrysotil 0,58 im Stockhorn, 0,52 und 0,50 in ZSF-Sedimenten, Almandin 0,09 und 0,03, Tremolit 0,89 gegen Mikroklin 0,29 und Albit 0,23 im MR-Granit; Aussage p. 13, l. 399 bis 401 ohne Kriterium. |
| GB-44 | echt | Nur ZSF-Sedimente fehlen (p. 14, l. 411 bis 412); in Fig. 13 (p. 34) liegen die KDE-Gipfel von ZSF-Sedimenten und Furgg beide nahe 0, MR-Gneis bei etwa 0,6; "confirms" p. 14, l. 415. |
| GB-45 | echt | Fig. 14 (p. 35): 13 Altersklassen, MR-Granit und MR-Gneis gleich hoch, keine Segmente für Serpentinite und Metabasite; "same detrital sample" p. 14, l. 421 gegen "taken at the same date and time" p. 14, l. 437 bis 438. |
| GB-46 | echt | Einzelprobe "June 28, 2019, at 13:30" p. 14, l. 423 bis 424; Suche season/diurnal/daily/annual/yearly ergibt 5 Treffer (p. 3, l. 66; p. 5, l. 133; p. 15, l. 453; p. 16, l. 479; p. 17, l. 507), keiner zur Repräsentativität. |
| GB-47 | echt | "export" 5 Treffer (p. 3, l. 66; p. 5, l. 133; p. 15, l. 454, 468; p. 16, l. 479) ohne Wert; "a prior equal to the average true erosion rate" für Naturdaten p. 14, l. 428. |
| GB-48 | echt | "same inversion parameters" p. 15, l. 444 bis 445; C_d = σd² I (p. 6, l. 186); 13 Zirkonklassen in Fig. 14 und 21 XRD-Fenster. |
| GB-49 | echt | JS nur p. 15, l. 447 bis 448 mit 0,48 und 0,57, kein XRD-Wert; Paararithmetik 0,504 und 0,514 nachgerechnet; Fig. 16 hat 34 Balken (p. 37). |
| GB-50 | echt | Farbleisten Fig. 5 und 6 ohne Größe und Einheit, Fig. 6g bis 6i ohne x-Achsentitel, Fig. 6i ohne "1e8" und ohne Farbleistentitel, Fig. 7 x-Achsen "Area difference" ohne Einheit (p. 26 bis 28). |
| GB-51 | echt | x-Achsen "Avg. JS distance between lithologies" mit Werten 0 bis 20 und Farbleiste "Number of tracrs" in Fig. 9 (p. 30). |
| GB-52 | echt | Beschriftungen "L = 3000 m", "σm = 6.2", "σd = 0.003 mm/y", "μ = 0.1", "n_m = 25" in Fig. 10 (p. 31) ohne Erklärung; verwendete Werte p. 11, l. 324 bis 326; Verhältnisse 2,5, 2,07, 0,3. |
| GB-53 | echt | Ziffernhöhe "3000" in Fig. 10 bei 300 dpi 11 px, also etwa 3,7 pt; Breitengradbeschriftung Fig. 4 16 px, also etwa 5,3 pt (p. 25, 31). |
| GB-54 | echt | Fig. 11 bei 300 dpi gemessen: Anorthit und Pyroxen (0, 35, 245, 93, 243, 6, 103) sowie Annit und Phlogopit identisch, Muskovit 9 px, Dolomit/Ankerit 2 px, Albit/Paragonit 7 px Abweichung (p. 32); Satz p. 16, l. 475 bis 476. |
| GB-55 | echt | Fig. 11 (p. 32) hat keine Werteachse, keine Spaltenköpfe, längster Balken je Spalte 241 bis 245 px. |
| GB-56 | echt | Fig. 12 (p. 33) markiert das Teileinzugsgebiet nur durch Sättigung, ohne Grenzlinie; Fig. 13 (p. 34) zeigt eine gestrichelte Grenze. |
| GB-57 | echt | Fig. 13 oberes Feld "Density" ohne Zahlen, unteres Feld Skala 0 bis 2, Bildunterschrift "a taller peak" (p. 34). |
| GB-58 | echt | Fig. 14 ohne Legende; Legendentext Fig. 15/16 überlappt, Fig. 16 oberste Zeile beschnitten; gemessene Differenzen Legende gegen Balken 62 bis 153, S.,T.,G.-Balken #ff844d gegen MR-Gneis-Feld 17 (p. 35 bis 37). |
| GB-59 | echt | Fig. 15 Chrysotil Serpentinite etwa 0,63 gegen 0,42 aus Fig. 11 je Mineral umgerechnet; Pyroxen in Fig. 15 mit Furgg oben statt S.,T.,G. und Metabasit (p. 32, 36). |
| GB-60 | echt | "non-linear mixing model" p. 15, l. 455; "weighted average" p. 5, l. 151 bis 152 und "hence making this non-linear" p. 5, l. 157 bis 158. |
| GB-61 | echt | Satz p. 15, l. 458; Fig. 9 Fehler ab 7 Tracern konstant etwa 197,4; "resolution" 0 Treffer auf p. 12. |
| GB-62 | echt | Sätze p. 15, l. 460 bis 461 und p. 16, l. 484 bis 486; Suche nach "number of source/litholog/unit/distinct" und "storage/stored" in p. 10, l. 286 bis p. 15, l. 449 jeweils 0 Treffer. |
| GB-63 | echt | 0,87 (p. 14, l. 436), 0,82 (p. 15, l. 442), 0,86 (p. 15, l. 447); Differenzen minus 0,01, plus 0,04, minus 0,05 nachgerechnet; "accura" und "sharp" 0 Treffer in p. 14, l. 419 bis p. 15, l. 449. |
| GB-64 | echt | Ausrichtung nur der Peaklage p. 9, l. 256; Behauptung zu "shielding effects" p. 15, l. 473 bis p. 16, l. 474. |
| GB-65 | echt | Ziele p. 10, l. 282 bis 284; in p. 15, l. 450 bis p. 16, l. 489 je 0 Treffer für steepest/quasi/QN/Newton und Bayes/hierarch/frequentist/BLMM/GLUE/NLLS/NNLS/hybrid. |
| GB-66 | echt | Sätze p. 16, l. 487 bis 489; ">8000 mm/y" p. 14, l. 435; land use/land-use/land cover 4 Treffer (p. 9, l. 270; p. 15, l. 466; p. 16, l. 488; p. 17, l. 507). |
| GB-67 | echt | Ein Satz p. 16, l. 490; SwissTopo und GeoCover nur im Rasterbild Fig. 4 (p. 25), "coordinat" 0 Treffer; die README-Angaben zum Zenodo-Depot waren nicht abrufbar. |
| GB-68 | echt | Bearth p. 17, l. 521 und Gjems p. 19, l. 583 ohne Verlag, "Mineralogical society" p. 17, l. 526, "oCLC" p. 18, l. 567 bis 568, "378-379" (Halbgeviertstrich im Original) p. 20, l. 613, zwei ISBN p. 20, l. 635 am Seitenbild bestätigt. |
| KK-01 | echt | "Quasi-Newtonian" p. 1, l. 5 und "Quasi-Newton" p. 11, l. 320 gegen "quasi-Newton" p. 7, l. 211 und p. 10, l. 296. |
| KK-02 | echt | "Bayesian linear mixed models" p. 2, l. 55 bis 56 gegen "Bayesian Linear Mixing Models (BLMM)" p. 2, l. 53. |
| KK-03 | echt | Klammerzitate in Satzfunktion p. 2, l. 61, p. 6, l. 181, p. 11, l. 333 bis 334, p. 14, l. 424 bis 425 am Seitenbild vorhanden. |
| KK-04 | echt | "hyper-parameters" p. 3, l. 70 und p. 5, l. 137 gegen "hyperparameters" p. 10, l. 281 und p. 12, l. 370. |
| KK-05 | echt | Großbuchstaben in allen 23 genannten Zeilen (p. 5, l. 146 bis p. 11, l. 319) bestätigt, Abbildungen tragen (a) bis (k), "6F )" mit Leerzeichen p. 11, l. 319. |
| KK-06 | echt | "and a prior knowledge" p. 6, l. 174. |
| KK-07 | echt | Eq. 5 p. 6, l. 175 ohne Gleichheitszeichen am Seitenbild. |
| KK-08 | echt | "considerately" p. 8, l. 236. |
| KK-09 | echt | Kursiv "a posteriori erosion" über p. 8, l. 240 bis 241 am Seitenbild. |
| KK-10 | echt | "weighed by the model covariance" p. 9, l. 245. |
| KK-11 | echt | "(Figure 3A and 3B)" p. 9, l. 251 bis 252, Fig. 3a zeigt die Pumpprobenahme (p. 24). |
| KK-12 | teilweise echt | Vier Formen p. 9, l. 267, 272, p. 13, l. 392, p. 15, l. 463 bestätigt; nicht zutreffend für p. 16, l. 498 bis 499, wo "Gorner Glacier" den Gletscher und nicht das Einzugsgebiet bezeichnet. |
| KK-13 | echt | "quarz pattern alignment" in Fig. 3c (p. 24). |
| KK-14 | echt | "schits", "calcarious", "caclcite", "silimanite", "GornergratPermo-Mesozoic" in den Legenden Fig. 4 und 12 (p. 25, 33). |
| KK-15 | echt | "(such as Zermatt Saas-Fee sediments and Furgg series (Figure 4) and Figure 5J)" p. 10, l. 299. |
| KK-16 | echt | Gerade Anführungszeichen um "greedy" p. 11, l. 307 gegen typografische p. 8, l. 222 und p. 10, l. 288. |
| KK-17 | echt | "by approaching each lithology's mineral concentration to its mean" p. 12, l. 343 bis 344. |
| KK-18 | echt | "which measures the similarity" p. 12, l. 345, während l. 346 kleine Werte als ähnlicher erklärt. |
| KK-19 | echt | "The more resemblant" p. 12, l. 351. |
| KK-20 | echt | "the maximal amount of non-linear iterations" p. 12, l. 370. |
| KK-21 | echt | "supporting the 1) the robustness" p. 13, l. 400. |
| KK-22 | echt | "sub-catchment" p. 14, l. 409, 411, 413 und "sub-catchments" p. 16, l. 488 gegen "subcatchment" p. 10, l. 283 bis 284 und p. 14, l. 411. |
| KK-23 | echt | Titel "Originial geology (same as forward)" in Fig. 7 (p. 28). |
| KK-24 | echt | Zusätzliches "Σ" unter dem y-Achsentitel der linken Streugrafik Fig. 9 (p. 30). |
| KK-25 | echt | "Smooting distance (m)" als x-Achse Spalte 2 und als Farbleistentitel Zeile 1 in Fig. 10 (p. 31, 300 dpi). |
| KK-26 | echt | Beschriftung "n_m = 25" in Fig. 10, Zeile 5, gegen n mit Index m in der Bildunterschrift (p. 31). |
| KK-27 | echt | "Low-con dence area" in Fig. 14, 15, 16 (p. 35 bis 37). |
| KK-28 | echt | "using Zr fingerprint data" und "per Zr age bin" (p. 35), "combined XRD and Zr data" (p. 37). |
| KK-29 | echt | "FDD, FH, BB, TA" neben "F.H.", "F.D.D.", "B.B.", "T.A." p. 16, l. 491 bis 494. |
| KK-30 | echt | "Master's thesis, University of Lausanne, unpublished master's thesis, 2021." p. 17, l. 522 bis 523. |
| KK-31 | echt | "[No title found]" p. 19, l. 578; Suchtreffer bestätigen den Titel "Landscape indicators of human impacts to riverine systems" (Aquatic Sciences 64, 118 bis 128). |
| KK-32 | echt | "Oxford University Press, New-York" p. 20, l. 612. |
| KK-33 | echt | "Bomb-fallout137 Cs" mit hochgestelltem 137 am Wort "fallout" p. 20, l. 639. |

## 2. Literaturvorschläge gegen das Literaturverzeichnis

| Vorschlag | Kennung | Im Verzeichnis | Beleg |
|---|---|---|---|
| Ehlers et al. (2015), JGR Earth Surface 120, 1023 bis 1039 | GB-06 | nein | kein Eintrag Ehlers in p. 17, l. 501 bis p. 21, l. 653 |
| Bernard et al. (2020), Earth Surf. Dynam. 8, 931 bis 953 | GB-06 | nein | kein Eintrag Bernard |
| Andrews und Eberl (2012), Marine Geology 291 bis 294, 24 bis 33 | GB-08 | nein | kein Eintrag Andrews |
| Eberl (2004), American Mineralogist 89, 1784 bis 1794 | GB-08 | nein | kein Eintrag Eberl |
| Niu et al. (2020) | GB-09 | ja | p. 20, l. 617 bis 618 |
| De Doncker et al. (2020) | GB-07, GB-60 | ja | p. 18, l. 559 bis 560 |
| Das et al. (2023) | GB-01 | ja | p. 18, l. 552 bis 553 |
| UNESCO-Bericht 2009 (Walling) | GB-04 | ja | als "E., W. D." p. 18, l. 567 bis 568 |
| Gergel et al. (2002) | KK-31 | ja | p. 19, l. 578 bis 579 |
| Bearth (1953) | GB-43 | ja | p. 17, l. 521 |
| Steck et al. (2015) | GB-43 | ja | p. 20, l. 631 bis 633 |
| SwissTopo 2018 (Landbedeckung) | GB-67 | nein | nur in Fig. 4 (p. 25) |
| GeoCover (Aufschlussdaten) | GB-67 | nein | nur in Fig. 4 (p. 25) |
| Beven und Binley (1992), nur im Einwand genannt, nicht zur Zitierung vorgeschlagen | GB-10 | nein | kein Eintrag Beven |

## 3. Doppelungen

| Paar | Fundort | Gegenstand |
|---|---|---|
| GB-25 und KK-15 | p. 10, l. 299 | Schreibweise "Zermatt Saas-Fee" der ZSF-Sedimente; GB-25 (c) führt dieselbe Stelle als Schreibvariante, KK-15 ersetzt sie durch "Zermatt-Saas Fee" |

Weitere Paare mit überlappendem Fundort (etwa GB-17 und GB-30 zur SD-Dokumentation, KK-05 und KK-11 zu Fig. 3, GB-68 und KK-32 zu Moore und Reynolds) behandeln verschiedene Aspekte oder liegen nicht an derselben Stelle und sind nicht als Doppelung gezählt.

## 4. Fundorte

Gezählt sind alle Einzelangaben der Felder Location und der Fundortspalte der Kleinkorrekturen (Seitenübergreifende Bereiche als eine Angabe, Zeilenlisten wie in KK-05 und KK-22 je Zeile).

| Kategorie | Anzahl |
|---|---|
| Fundortangaben gesamt | 317 |
| genau | 317 |
| um 1 bis 2 Zeilen daneben | 0 |
| weiter daneben | 0 |

## 5. Zählungen je Urteil

| Urteil | GB | KK | Gesamt |
|---|---|---|---|
| echt | 65 | 32 | 97 |
| teilweise echt | 3 (GB-06, GB-22, GB-33) | 1 (KK-12) | 4 |
| falsch | 0 | 0 | 0 |
| nicht prüfbar | 0 | 0 | 0 |
| Summe | 68 | 33 | 101 |

Literaturvorschläge: 13 vorgeschlagene Arbeiten, davon 7 im Verzeichnis, 6 nicht; dazu 1 nur genannte Arbeit, nicht im Verzeichnis. Doppelungen: 1. Fundorte: 317 genau, 0 um 1 bis 2 Zeilen, 0 weiter daneben.
