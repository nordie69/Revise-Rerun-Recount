# Verifikation des Gutachtens zu egusphere-2025-4695

Grundlage: Manuskript-PDF (37 Seiten), Seitenbilder in seiten/ (150 dpi), eigene Renderings der Seiten 25 bis 37 mit 300 dpi, Zeilennummern aus den gedruckten Randnummern (pdftotext -layout, auf den Gleichungsseiten 5 bis 8 und Seite 14 am Seitenbild nachgezählt). Rechnungen und Bildmessungen mit Python. Literatur über WebSearch und WebFetch.

## 1. Urteile je Kennung

| Kennung | Urteil | Beleg (ein Satz mit Seite und Zeile) |
|---|---|---|
| GB-01 | echt | "temporal" und "timing" stehen nur in l. 1, 10, 13, 77, 80 (Python), keine Testfrage in l. 280 bis 285, Einzelprobe l. 423 bis 424, Abschnitt 3.1 sagt nur "transported or stored" (S. 5, l. 147 bis 148). |
| GB-02 | echt | "cost" nur in l. 3, 4, 40, 74, 107, 141, kein Aufwandsmaß im Text, keine Erwähnung in den Conclusions (S. 16, l. 477 bis 489), Zitate S. 1, l. 3 bis 4 und S. 3, l. 74 bis 75 wörtlich. |
| GB-03 | echt | "consistent convergence" S. 1, l. 7 und "robust across a range of parameters" S. 16, l. 483 wörtlich, Gegenbelege l. 312, 353, 387 bis 388, 435 vorhanden, Figur 8 zeigt 14 statt 20 Läufe. |
| GB-04 | echt | Wortvergleich l. 10 bis 75 gegen l. 77 bis 142: je 1153 Wörter, difflib-Ratio 1.0, je 66 Zeilen (S. 1 bis 5). |
| GB-05 | echt | Zitat "E., 2009" S. 1, l. 11 bis 12 und Eintrag "E., W. D." mit "UNESCO 2009", "oCLC" zwischen Domingo und Evrard S. 18, l. 567 bis 568. |
| GB-06 | echt | Barker et al. 1997 ist laut Titel Photogrammetrie der Ufererosion (S. 17, l. 519), Wilson et al. 1993 Bodenerosion Falklandinseln (S. 21, l. 649); die Schlagwortangabe zu Wilson wurde nicht geprüft. |
| GB-07 | echt | 29 Zitate in l. 26 bis 33 (Python), Kobe 2021 ist Theologie (S. 19, l. 597, Verlagsseite hts.org.za), Olley "radioactivity", Walden "mineral magnetic", Blaen "Real-time monitoring" (S. 20, l. 621, 641; S. 17, l. 528); 4/29 = 13,8 %. |
| GB-08 | echt | Eberl und Andrews fehlen, Cooper nur als Koautor bei Wilson (S. 21, l. 649); Bibliodaten aller drei Vorschläge an USGS und UEA bestätigt (Cooper: 21 Prozentpunkte). |
| GB-09 | echt | Gl. 1 bis 3 (S. 5, l. 154; S. 6, l. 162) sind linear in den Erosionsraten, "non-linear mixing model" S. 15, l. 455; Abstract De Doncker et al. 2020 (serval.unil.ch) nennt Prior, Kovarianz und "mineral content". |
| GB-10 | echt | Gl. 17 mit k, Gl. 18 und 19 mit n und εk (S. 8, l. 215, 219), n für Pixel und Iteration, "tracer n" in Fig. 1b, 2b, 2c, 3d, 3e, "prior misfit" S. 6, l. 184 gegen "model misfit" S. 7, l. 202 und S. 9, l. 245. |
| GB-11 | echt | "export" nur in l. 66, 133, 454, 468, 479 (Python), kein Wert, Prior "average true erosion rate" auch im Naturlauf S. 14, l. 428; Fundteil "l. 444 bis 445" steht auf S. 15, nicht S. 14. |
| GB-12 | echt | "dimensionless" S. 6, l. 161 und Werte 0 bis 1 S. 9, l. 261 bis 262, dagegen σd in mm/y in l. 295, 325, 384, 428 und Achse in Fig. 10, dritte Zeile. |
| GB-13 | echt | Annahme wörtlich S. 6, l. 177 bis 178; exp(±3) = 0,050 bis 20,09, Verhältnis 403 (Python); ">8000 mm/y" S. 14, l. 435, Farbskala Fig. 15 bis etwa 8. |
| GB-14 | echt | Gl. 19 (S. 8, l. 219) invertiert G^T Cd^-1 G ohne Cm^-1, A hat laut S. 6, l. 172 mehr Spalten als Zeilen, damit Rang höchstens Tracerzahl. |
| GB-15 | echt | Gl. 22 mit Wurzeln (S. 8, l. 239) gegen tr(Cm,post)/tr(Cm) (S. 14, l. 436); alle genannten Namensformen in Text und Figuren 5 bis 10, 14 bis 16 vorhanden; 0,87² = 0,757, 0,82² = 0,672, 0,86² = 0,740. |
| GB-16 | echt | Kein Diffraktometer, keine Strahlung, keine Software oder Sprache genannt (Suche ergebnislos), Zitat S. 9, l. 252. |
| GB-17 | echt | Zitate S. 9, l. 257 und S. 15, l. 443 bis 444 wörtlich, keine Fensterliste, keine Peak-Finder-Schwellen, keine Gewichtung der Blöcke. |
| GB-18 | echt | Zitat S. 9, l. 261 bis 262; Rechenbeispiel ergibt 0,556 und 0,444 (Python); gemessen Antigorit 0,43 (Fig. 11) gegen 0,64 (Fig. 15), Fayalit 0,54 gegen 0,73, Anorthit Metabasite 0,34 gegen 0,17. |
| GB-19 | echt | Belotti 2021 "unpublished" (S. 17, l. 522 bis 523), Kartenquelle mit "personal communication" und GeoCover im Bildnachweis Fig. 4 (S. 25), GeoCover und swisstopo nicht im Verzeichnis. |
| GB-20 | echt | Namensformen S. 10, l. 274 bis 276, l. 299, S. 14, l. 411, 414, 431 bis 432 und in den Legenden Fig. 4, 5, 11, 12, 13, 15, 16 wie angegeben, "Bündnerschiefer" nur l. 275. |
| GB-21 | echt | Pfeilspitze in Fig. 1b, 2b, 3b, in Fig. 2b vier farbige und sieben schwarze Balken, nur eine Farbrampe in Fig. 2c, nichts davon erklärt (S. 22 bis 24). |
| GB-22 | echt | Bildunterschrift Fig. 4 nur "Study area: location, land cover and geology." (S. 25), "ELA estimation" unerklärt, Hauptkarte nur mit 1-km-Maßstab. |
| GB-23 | echt | Prior gleich Mittel der Wahrheit S. 10, l. 295 und S. 11, l. 325 bis 326, eingeräumt S. 13, l. 374 bis 375, "noise" nur S. 9, l. 255, eine Wahrheitskarte (Fig. 5a). |
| GB-24 | echt | "mm/yr" nur S. 12, l. 352, sonst "mm/y", Achsen Σ beziehungsweise sum in Fig. 8 und 10, keine Pixelzahl; 1,14e7/300² = 127, C(7,2) = 21 (Python). |
| GB-25 | echt | Gemessen 300 dpi: Panelversatz 698 px, Schwerpunkt der Hotspotzellen 18 px westlich (Gutachten 20,5), Farbskala 5a und 5b endet bei 3,0, Minimum in 5c am Hotspot (S. 26; Text S. 10, l. 296 bis 298). |
| GB-26 | echt | 5g Minimum etwa 197 bei Iteration 22, Ende etwa 201 bei 100; 6g Ende etwa 193 bei 200 (Bild 300 dpi, S. 26 und 27), Normierung erst S. 11, l. 312. |
| GB-27 | echt | "(Figure 6G versus Figure 6G)" S. 11, l. 317 wörtlich; Fig. 6h zeigt glatten Verlauf mit Knick bei etwa 137 ohne sichtbare Oszillation (S. 27). |
| GB-28 | echt | Namen in S. 11, l. 330 bis 339 und Fig. 7 ("Originial geology", "Geology misalignment (m²)") sowie Fig. 8 wie angegeben, Steck et al. 2015 auch im Bildnachweis Fig. 4. |
| GB-29 | echt | Keine Angaben zu Erzeugung der Fingerprints, PCA-Rangfolge, Mischgraden, Probenzahl je Einheit, Zirkonkörnern (S. 12, l. 343 bis 357; S. 13, l. 391 bis 392). |
| GB-30 | teilweise echt | 14 Marker in beiden Panels, Bilanz 20 minus 14 bestätigt (S. 29, S. 12, l. 348 bis 353); nicht belegt ist "every plotted value from JS 0.501 downward exceeds 700": die Punkte bei 0,441 bis 0,481 liegen auf der Grundlinie wie die bei 0,56 bis 0,62 (1 px etwa 1400). |
| GB-31 | echt | Gl. 7 und 8 summieren über Tracer, Fig. 9 rechts etwa 3,3e6 (21) und 0,12e6 (1), je Tracer 1,57e5 gegen 1,2e5 (Python; S. 12, l. 360 bis 362). |
| GB-32 | echt | Fig. 7: 198, 193,5, 274,8 und 0,7402, 0,7376, 0,7460 nicht monoton; +39 % gegen +76 %, 0,69/1,14 = 61 % (Python; S. 12, l. 363 bis 365, S. 11, l. 337 bis 338). |
| GB-33 | echt | Fig. 10 erste Zeile fällt monoton bis 3000 m, kein Lauf darüber, Marken L = 3000 m, σm = 6.2, σd = 0.003 mm/y, μ = 0.1, n_m = 25 gegen Testwerte S. 10, l. 294 bis 295; (197,6 minus 76,6)/76,6 = 158 %. |
| GB-34 | echt | Achsenoffset "+1.974e2", Werte 0,020 bis 0,043 monoton steigend, Unsicherheit 0,74015 bis 0,74040, Modellmisfit 1,5614 bis 1,5623 (S. 31) gegen Beschreibung S. 13, l. 380 bis 384. |
| GB-35 | echt | "falls below 10−5" S. 13, l. 388 ohne Angabe absolut oder relativ, Datenmisfit in Fig. 10, fünfte Zeile, mit Faktor 1e7. |
| GB-36 | teilweise echt | Gemessen: Annit und Phlogopit sowie Anorthit und Pyroxen identisch, Muskovit nur Spalte 5 abweichend, Ankerit und Dolomit bis 2 px, Albit und Paragonit bis 7 px (S. 32), Fig. 15 Paare identisch; nach der eigenen Regel (bis 2 px) ergeben sich 18 statt "16 or 17" unterscheidbare Tracer. |
| GB-37 | echt | "Chrysolite" S. 13, l. 395 gegen "Chrysotile" in Fig. 11, 15, 16 und S. 10, l. 274; Chrysolith ist eine Olivinvarietät (minerals.net). |
| GB-38 | echt | Zitat S. 13, l. 399 bis 401 mit doppeltem Artikel; gemessen Almandin höchstens 0,10, Omphazit 0,05, Mikroklin 0,29, Tremolit 0,89, Fayalit 0,61 (Fig. 11), Calcit fehlt in l. 394 bis 396. |
| GB-39 | echt | Nur eine Einheit ohne Aufschluss (S. 14, l. 411), Probenzahl nirgends genannt, KDE-Panel ohne Dichteskala, Einzugsgebiet im Inset überwiegend Monte-Rosa-Granit (S. 34). |
| GB-40 | echt | "the same detrital sample" S. 14, l. 421 gegen "a detrital sample taken at the same date and time" S. 14, l. 437 bis 438, Probenort nicht genannt. |
| GB-41 | echt | Text S. 14, l. 430 bis 434; in Fig. 14 kein Metabasit-Segment in den 13 Altersklassen, MR-Granit und MR-Gneis jeweils gleich hoch, Bildunterschriften ohne Hinweis. |
| GB-42 | echt | 0,82 (S. 15, l. 442) gegen 0,86 (l. 447): +4,9 %, −5,7 %, −1,1 % (Python), Aussagen S. 15, l. 461 bis 463 und S. 3, l. 72 bis 73 wörtlich, kein JS-Wert für XRD allein. |
| GB-43 | echt | Farbskalen in Fig. 5 und 6 ohne Einheit, 5g, 5h ohne y-Titel, 6g bis 6i ohne x-Titel, 6i ohne Skalentitel, Schraffur in Fig. 6 ohne Beschriftung, Tracer A bis U (S. 26, 27). |
| GB-44 | echt | Legendenfarben gemessen #ff5001, #ff7f41, #32a02d, Balken #ff844d, #ffa57a, #70bc6c (S. 36); Fig. 4 Abstände 64, 24, 40 bestätigt; die Zahlen "21" und "60 to 151" sind mit Summen- oder euklidischer Metrik nicht genau reproduzierbar (17 beziehungsweise 95 bis 153), die Aussage bleibt. |
| GB-45 | echt | x-Achse "Avg. JS distance between lithologies" mit Skala 0 bis 20 und 21 Markern in Fig. 9 (S. 30). |
| GB-46 | echt | Fig. 12 zeigt das Teileinzugsgebiet nur durch Sättigung, ohne Grenzlinie und ohne Erklärung (S. 33), Fig. 13 mit gestrichelter Linie. |
| GB-47 | echt | Fig. 14 hat nur die Legende "Low-con dence area", keine Geologielegende (S. 35). |
| GB-48 | echt | Auflösungspanels in Fig. 14 bis 16 überwiegend achromatisch dunkel, das obere Ende der Skala bei 1 (eigene Schätzung über 90 %, Werte schwellenabhängig), Text "low resolution" S. 14, l. 436. |
| GB-49 | echt | Zitate S. 15, l. 458 und l. 460 bis 461 wörtlich, kein Test mit variierter Zahl der Quellgebiete in Abschnitt 4.1, 7/21 = 33,3 %. |
| GB-50 | echt | Empfehlung S. 15, l. 463 bis 465, Geologie unter Eis erschlossen S. 9, l. 270 bis 272, JS nur 0,48 und 0,57 (S. 15, l. 448). |
| GB-51 | echt | Abhilfe S. 15, l. 470 bis 471, "pump sampler" in Fig. 1c und 3a, keine Angabe zu Tiefenintegration oder Kornfraktion der eigenen Proben. |
| GB-52 | echt | Conclusions S. 16, l. 478 bis 489 nur synthetisch, Ziele 1 und 2 (S. 10, l. 282 bis 284) in Diskussion und Schluss nicht aufgegriffen. |
| GB-53 | echt | Satz S. 16, l. 483 bis 484, kein pixelweiser Vergleich in S. 10, l. 297 bis 304, in Fig. 5e geringste Kovarianz am Hotspot, wo 5c die größte Differenz zeigt. |
| GB-54 | echt | "storage" nie in Abschnitt 4 (Python), Annahme S. 15, l. 466 bis 468; die eingebettete Zeilenliste nennt l. 91, richtig ist l. 92. |
| GB-55 | echt | Ausblick S. 16, l. 487 bis 489 gegen "highly unstable" S. 14, l. 435 und S. 12, l. 353 bis 354. |
| GB-56 | echt | Erklärung S. 16, l. 490 nennt nur "inversion tests"; die Zenodo-Angaben (Version, Größe, README) waren nicht abrufbar und sind ungeprüft. |
| GB-57 | echt | Einträge S. 19, l. 583, 599 bis 600 und S. 17, l. 521 wie zitiert; Verlagsdaten Lafuente: Yang, H., S. 1 bis 29, de Gruyter, DOI 10.1515/9783110417104-003, 2016 (experts.azregents.edu); 9 von 64 Einträgen ohne DOI. |
| KK-01 | echt | "Quasi-Newtonian" S. 1, l. 5, "quasi-Newton" S. 7, l. 211. |
| KK-02 | echt | "E-DNA information (Evrard et al., 2019)" S. 2, l. 32 und S. 4, l. 99. |
| KK-03 | echt | "Generalist Likelihood Uncertainty Estimation" S. 2, l. 50 und S. 4, l. 117. |
| KK-04 | echt | "Maximal Likelihood Estimation (MLE) (similar to the NNLS" S. 2, l. 51, eingeführt ist NLLS in l. 48 bis 49. |
| KK-05 | echt | "Bayesian linear mixed models" S. 2, l. 55 bis 56 gegen "Bayesian Linear Mixing Models (BLMM)" l. 53. |
| KK-06 | echt | "validated in (De Doncker et al., 2020)" S. 2, l. 61 und S. 4, l. 128. |
| KK-07 | echt | "hyper-parameters" S. 3, l. 70 und S. 5, l. 137, sonst "hyperparameter" l. 281, 370. |
| KK-08 | echt | Gl. 5 S. 6, l. 175 ohne Relationszeichen zwischen den Termen (Seitenbild). |
| KK-09 | echt | "becomes Tarantola (2005):" S. 6, l. 181. |
| KK-10 | echt | Gl. 9 S. 7, l. 189 ohne Minuszeichen im Exponenten (Seitenbild). |
| KK-11 | echt | Gl. 12 S. 7, l. 197 "G = A · exp(ε)". |
| KK-12 | echt | Gl. 14 S. 7, l. 201 ohne Transponierte, Gl. 16 mit G^T. |
| KK-13 | echt | "considerately" S. 8, l. 236. |
| KK-14 | echt | "weighed by the model covariance" S. 9, l. 245. |
| KK-15 | echt | "Gorner-gletscher" S. 9, l. 267 und Bildunterschrift Fig. 11 (S. 32). |
| KK-16 | echt | "quarz pattern alignment" in Fig. 3c (S. 24). |
| KK-17 | echt | Alle sechs Schreibfehler in den Legenden von Fig. 4 und 12 vorhanden (S. 25, 33). |
| KK-18 | echt | "(such as Zermatt Saas-Fee sediments and Furgg series (Figure 4) and Figure 5J)" S. 10, l. 299. |
| KK-19 | echt | "(Figure 6D, 6E and 6F )" S. 11, l. 319. |
| KK-20 | echt | "Zermatt-Saas-Fee ophiolites" S. 12, l. 340 gegen l. 431. |
| KK-21 | echt | "approximately 10-2 mm/y" ohne Hochstellung S. 13, l. 384 (Seitenbild). |
| KK-22 | echt | "sub-catchment" S. 14, l. 409, 411, 413, "subcatchment" l. 283, 284, 411. |
| KK-23 | echt | "described in (Belotti, 2021)" und "outlined in (De Doncker et al.," S. 14, l. 424. |
| KK-24 | echt | "Steepest-Descent (SD)" in der Bildunterschrift Fig. 6 (S. 27). |
| KK-25 | echt | "Number of tracrs" an der Farbskala Fig. 9 (S. 30). |
| KK-26 | echt | Zweites, einzelnes "Σ" unter dem y-Titel Fig. 9 links (S. 30). |
| KK-27 | echt | "Smooting distance (m)" an x-Achse Spalte 2 und Farbskala Zeile 1, Fig. 10 (S. 31). |
| KK-28 | echt | "ecologites" in der Bildunterschrift Fig. 11 (S. 32). |
| KK-29 | echt | Inset-Beschriftung "Gorner-Grenz catchment" in Fig. 13 (S. 34). |
| KK-30 | echt | "Low-con dence area" in Fig. 14 bis 16 (S. 35 bis 37). |
| KK-31 | echt | "Zr fingerprint data", "per Zr age bin", "combined XRD and Zr data" (S. 35, 37). |
| KK-32 | echt | "glaciated" S. 15, l. 460, sonst "glacierized" l. 16, 62, 83, 129, 329. |
| KK-33 | echt | Satz S. 16, l. 490 endet ohne Punkt nach der DOI. |
| KK-34 | echt | "All authors (FDD, FH, BB, TA)" S. 16, l. 491, danach "F.H.", "F.D.D.", "B.B.", "T.A.". |
| KK-35 | echt | "Master’s thesis, University of Lausanne, unpublished master’s thesis, 2021." S. 17, l. 522 bis 523. |
| KK-36 | echt | "Reviews in mineralogy, Mineralogical society of America" S. 17, l. 526. |
| KK-37 | echt | "[No title found]" S. 19, l. 578; Titel "Landscape indicators of human impacts to riverine systems" im Publikationsnachweis (experts.illinois.edu). |
| KK-38 | echt | "New-York, 378–379" S. 20, l. 612 bis 613; der Ersatz "pp. 378" lässt "–379" weg. |
| KK-39 | echt | Doppelte ISBN S. 20, l. 635. |
| KK-40 | echt | "Bomb-fallout¹³⁷ Cs" mit Hochzahl am Wort und Leerzeichen vor Cs, S. 20, l. 639 (Seitenbild). |

## 2. Literaturvorschläge

| Vorschlag | Kennung | Bereits im Literaturverzeichnis |
|---|---|---|
| Eberl (2004), American Mineralogist 89, 1784 bis 1794 | GB-08 | nein |
| Andrews und Eberl (2012), Marine Geology 291 bis 294, 24 bis 33 | GB-08 | nein |
| Cooper et al. (2014), Water Resources Research 50, 9031 bis 9047 | GB-08 | nein |
| GeoCover (Datensatz) | GB-19 | nein |
| swisstopo Landbedeckung 2018 (Datensatz) | GB-19 | nein |

## 3. Doppelungen

Keine. Geprüfte Nahfälle mit gleichem Ort, aber anderem Gegenstand: GB-20 und KK-17 (Benennung gegen Schreibfehler in den Legenden Fig. 4 und 12), GB-20 und KK-18 (Name gegen Klammersetzung l. 299), GB-24 und GB-30 (Einheit gegen Schwelle l. 352 bis 353), GB-49 und GB-54 (verschiedene Bedingungen im Satz l. 484 bis 485), GB-03 und GB-23 (Bedingungen gegen Testanlage zu l. 482 bis 483), GB-45, KK-25, KK-26 (verschiedene Elemente in Fig. 9).

## 4. Fundorte

| Klasse | Anzahl |
|---|---|
| genau | 97 |
| um 1 bis 2 Zeilen daneben | 0 |
| weiter daneben | 0 |

Anmerkung: Bei GB-11 sind die Zeilen 444 bis 445 richtig, aber der Seite 14 statt Seite 15 zugeordnet. In eingebetteten Angaben weicht GB-54 um eine Zeile ab (91 statt 92).

## 5. Zählungen je Urteil

| Urteil | GB | KK | Gesamt |
|---|---|---|---|
| echt | 55 | 40 | 95 |
| teilweise echt | 2 | 0 | 2 |
| falsch | 0 | 0 | 0 |
| nicht prüfbar | 0 | 0 | 0 |
