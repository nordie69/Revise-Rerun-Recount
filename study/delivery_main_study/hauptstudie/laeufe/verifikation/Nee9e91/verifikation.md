# Verifikation des Gutachtens zu egusphere-2025-4695

Geprüfte Fassung: egusphere-2025-4695.pdf, SHA-256 9c80676054f96ecd6f00f4d2a8b5ba568e03c6949e3856d363ac1c4abb42e7bd (nachgerechnet, stimmt). Zeilennummern an den Randnummern der Seitenbilder bestätigt; text.json weicht auf S. 3 (l. 91 bis 94), S. 5 (Gl. 1 steht auf l. 154), S. 11 (l. 336 bis 339) und S. 12 (l. 372 bis 373) um eine Zeile ab. Abbildungen bei 300 dpi (Fig. 10 zusätzlich 600 dpi) gerendert und vermessen; Zahlen mit Python nachgerechnet.

## 1. Urteile je Kennung

| Kennung | Urteil | Beleg (ein Satz mit Seite und Zeile) |
|---|---|---|
| GB-01 | echt | Zitat steht p. 1, l. 3 bis 4, "cost- and time-efficient" p. 3, l. 74 bis 75, "expensive and time-consuming" p. 2, l. 35; nirgends werden Kosten, Zeit oder Durchsatz angegeben. |
| GB-02 | echt | Zitat p. 1, l. 7; "proved unstable" p. 11, l. 312; "fails to converge" p. 12, l. 353; Fig. 8 (p. 29) Bildunterschrift schließt den stärksten Blend aus. |
| GB-03 | echt | Eintrag "E., W. D.:" p. 18, l. 567 bis 568, Zitate "E., 2009" p. 1, l. 11 bis 12 und p. 3, l. 78 bis 79; der Schlüssel ist ein Initial. |
| GB-04 | echt | Kobe (2021) p. 19, l. 597 bis 598 ist ein Theologieaufsatz (DOI-Landeseite bestätigt Titel und HTS 77(3)), zitiert p. 2, l. 31 und p. 4, l. 98; Titel Wilson 1993 (p. 21, l. 649), Barker 1997 (p. 17, l. 519) und Butler 2019 (p. 18, l. 546) wie angegeben, Butler-Abstract erwähnt keine tiefenintegrierte Probenahme. |
| GB-05 | echt | Zitat p. 2, l. 58 bis 59, Neuheitsanspruch p. 15, l. 454 bis 455; Braun et al. 2018 (ESurf 6, 257 bis 270) und Ehlers et al. 2015 (JGR ES 120(6), 1023 bis 1039) existieren mit den genannten Angaben und fehlen im Verzeichnis (p. 17 bis 21). |
| GB-06 | echt | Abschnitt 1 (p. 1, l. 9 bis p. 3, l. 75) und Abschnitt 2 (p. 3, l. 76 bis p. 5, l. 142) je 67 Zeilen, difflib-Quote 1,0 (eigene Zählung 1145 Wörter je Abschnitt, Gutachten 1153, Unterschied nur durch Tokenisierung). |
| GB-07 | echt | Am Seitenbild: Gl. 5 ohne Relationszeichen und mit p(εprior) (p. 6, l. 175), Gl. 9 mit positivem Exponenten (p. 7, l. 189), Gl. 12 A·exp(ε) (l. 197), Gl. 14 ohne Transponierte (l. 201), Gl. 18 mit n und k gemischt (p. 8, l. 215), Gl. 19 ohne Cm^−1 (l. 219), R ohne Formel (l. 230 bis 234). |
| GB-08 | echt | Gl. 22 Wurzelquotient p. 8, l. 239, Spurquotient p. 14, l. 436, "normalised posterior variance" p. 10, l. 303, Fig. 5h Titel "Normalised covariance trace"; Zählungen 8, 5, 4, 4, 1, 1 im PDF-Text exakt reproduziert. |
| GB-09 | echt | Abschnitt 3.4 (p. 9, l. 250 bis 265) nennt weder Gerät, Scanbereich, 2θ-Fenster noch Probenzahl; Exportwert fehlt im ganzen Text (p. 3, l. 65 bis 66; p. 15, l. 453 bis 454); Fig. 6 (p. 27) läuft bis 200 Iterationen ohne Angabe im Text. |
| GB-10 | echt | Normierung durch das Maximum p. 9, l. 261; Fig. 11 (p. 32) zeigt je Spalte Maximum gleich 1, Figs. 5k, 15, 16 zeigen je Tracer auf 1 gestapelte Balken; die Folgerung zur Mischung ist als gefolgert gekennzeichnet. |
| GB-11 | teilweise echt | ELA (Fig. 4), S.,T.,G. (Figs. 5j, 15, 16), Schraffur ohne Text und fehlender Achsentitel in Fig. 6b und 6g (p. 27) stimmen; nicht zutreffend ist, dass Fig. 14 die Kürzel ZSF und MR trägt (keine Legende, p. 35) und dass ZSF erst p. 14, l. 431 aufgelöst wird (schon p. 14, l. 414 "Zermatt - Saas Fee unit (ZSF sediments)"). |
| GB-12 | echt | Zitat p. 10, l. 288 bis 289, Prior "equal to the average true erosion rate" p. 10, l. 295; Fig. 10 erste Zeile (p. 31) fällt über 20 Marker monoton von etwa 257 auf etwa 76 bei L = 3000 m; "beyond approximately 10 times the pixel size (3000 m)" p. 12, l. 373. |
| GB-13 | echt | Fig. 5c (p. 26): die blauen Hotspotpixel entsprechen am Farbbalken −2,2 bis −2,4, Fig. 5a endet bei 3,0; Textaussage p. 10, l. 296 bis 298. |
| GB-14 | echt | Farbbalken Fig. 5d 0,90 bis 1,00 (p. 26), Fig. 14 0,5 bis 1,0, Fig. 15 0,80 bis 1,00, Fig. 16 0,5 bis 1,0; Fläche Fig. 4 nachgemessen 893932 Pixel bei 110 px/km, also etwa 73,9 km² und etwa 818 Pixel zu 300 m; Spurgrenze 21 gegen mindestens 736. |
| GB-15 | echt | Monotonieaussage p. 11, l. 337 bis 338, gegenläufiger Satz l. 338 bis p. 12, l. 340; Fig. 7 (p. 28) zeigt etwa 193,5 (minimal) unter etwa 197,5 (original) und etwa 275 (Steck). |
| GB-16 | echt | Fig. 8 (p. 29) links und Mitte je 14 Marker (4 zwischen JS 0,25 und 0,36, 10 zwischen 0,44 und 0,62), Text "20 values" p. 12, l. 348; 20 − 1 − 14 = 5. |
| GB-17 | echt | "700 mm/yr for JS < 0.44" p. 12, l. 352 bis 353; Achse Fig. 8 bis 700000 ohne Einheit, Marker bei JS 0,54 etwa 18000, bei 0,34 etwa 5000, Grundwert etwa 197 in Figs. 7 und 9. |
| GB-18 | echt | Fig. 9 (p. 30): x-Achsen 0 bis 20 mit "Avg. JS distance between lithologies", Farbbalken "Number of tracrs"; zitiert p. 12, l. 356 bis 357. |
| GB-19 | echt | Rangfolge p. 12, l. 363 bis 365; Fig. 7 Steck etwa +77, Fig. 9 (p. 30) 3 und 4 Tracer etwa 293 und 296, 1 Tracer etwa 347 gegen etwa 197, also +96 bis +150. |
| GB-20 | echt | Fig. 10 (p. 31) markiert "L = 3000 m", "σm = 6.2", "σd = 0.003 mm/y", "μ = 0.1", "n_m = 25" ohne Erklärung in der Bildunterschrift; drei weichen von p. 11, l. 324 bis 326 ab (μ und n_m stimmen überein, das Gutachten behauptet für sie nichts anderes). |
| GB-21 | echt | Bei 600 dpi gemessen: Versalhöhe "D" in "Data standard deviation (mm/y)" 24 px, das ergibt 4,0 pt (p. 31). |
| GB-22 | echt | Fig. 10 dritte Zeile (p. 31): Offset "+1.974e2", Werte steigen monoton von etwa 0,020 auf etwa 0,043, Unsicherheit 0,74015 bis 0,74040; Text p. 13, l. 380 bis 384 beschreibt Minimum und Plateau. |
| GB-23 | echt | Satz p. 13, l. 399 bis 401 ohne Vergleich; Fig. 11 (p. 32) Almandin in MR-Gneis etwa 0,03, in Metabasiten etwa 0,09, Omphacit etwa 0,05, Pyroxen 1,0; "garnet-mica schists" p. 10, l. 276. |
| GB-24 | echt | Sechs Einheiten im Teileinzugsgebiet p. 14, l. 411; Fig. 13 (p. 34) KDE-Gipfel von Furgg series und ZSF sediments beide bei etwa 0 mm/y; Zitat p. 14, l. 415 bis 416, Abstract p. 1, l. 8. |
| GB-25 | echt | Fig. 12 (p. 33) ohne Grenzlinie und ohne Erklärung der blassen Farben; Fig. 13 obere Tafel "Density" ohne Werte, untere 0 bis 2 (p. 34); Fig. 12 zitiert p. 14, l. 412. |
| GB-26 | echt | "multiple detrital samples" p. 14, l. 413 ohne Anzahl, Datum oder Parameter; Bildunterschrift Fig. 13 (p. 34) enthält "all pixels within each lithological unit" und "a taller peak indicates greater consistency across inversions". |
| GB-27 | echt | Eine Probe "June 28, 2019, at 13:30" p. 14, l. 423 bis 424, Ort nicht genannt; "multi-year suspended sediment datasets" p. 9, l. 268; Teileinzugsgebiet nur Nordosten p. 14, l. 407. |
| GB-28 | echt | "a prior equal to the average true erosion rate" für die Naturdaten p. 14, l. 428, gleichlautend zu p. 11, l. 325 bis 326. |
| GB-29 | echt | Zitat p. 14, l. 439 bis 440; Fig. 14 (p. 35) Altersbalken ohne gelben Serpentinit- und ohne grünen Metabasitanteil, Hotspot im Südwesten über 8000 mm/y. |
| GB-30 | echt | Zitat p. 15, l. 446; Werte 0,87, 0,82 (p. 15, l. 442), 0,86 (l. 447), +4,9 % und −1,1 % nachgerechnet; Farbbalken Fig. 15 bis 8, Fig. 16 bis 12; p. 3, l. 72 bis 73 und p. 15, l. 461 bis 463 wie zitiert. |
| GB-31 | echt | JS nur 0,48 und 0,57 p. 15, l. 448, für XRD allein kein Wert; Schwelle 0,55 p. 12, l. 352. |
| GB-32 | echt | Gl. 3 d = A·exp(ε) linear in ė (p. 6, l. 162); "hence making this non-linear" p. 5, l. 157 bis 158; Zitat p. 15, l. 455; "linear mixing scheme" p. 2, l. 59. |
| GB-33 | echt | Sätze p. 15, l. 457 bis 458 und l. 460 bis 461; Szenarien p. 11, l. 327 bis p. 12, l. 362 variieren nie die Zahl der Einheiten; "7 tracers ... approximately the same" p. 12, l. 360; Figs. 7 bis 9 zeigen keine Auflösung. |
| GB-34 | echt | Zitat p. 15, l. 463 bis 464; Geologie unter Eis erschlossen p. 9, l. 270 bis 272; zirkonische JS 0,48 (p. 15, l. 448) unter 0,55 (p. 12, l. 352). |
| GB-35 | echt | Grenzen nur p. 15, l. 469 bis p. 16, l. 476; Abschnitt 3.4 (p. 9, l. 250 bis 265) erwähnt Korngröße und Orientierung nicht; der Unterschied Schwebstoff gegen Gesteinspulver wird nicht behandelt (nur Pulverisieren und tiefenintegrierte Proben, l. 470 bis 471). |
| GB-36 | echt | Satz p. 16, l. 490 wörtlich; Belotti 2021 "unpublished master's thesis" p. 17, l. 522 bis 523; Kreditzeile Fig. 4 (p. 25) wie zitiert; Exportwert nirgends angegeben. |
| KK-01 | echt | "Quasi-Newtonian" p. 1, l. 5; "quasi-Newton (QN)" p. 7, l. 211. |
| KK-02 | echt | "Non-Linear Least Squares (NLLS)" p. 2, l. 48 bis 49 und p. 4, l. 115 bis 116; "NNLS" p. 2, l. 51 und p. 4, l. 118. |
| KK-03 | echt | "Generalist Likelihood Uncertainty Estimation" p. 2, l. 50 und p. 4, l. 117. |
| KK-04 | echt | "Maximal Likelihood Estimation" p. 2, l. 51 und p. 4, l. 118. |
| KK-05 | echt | "Bayesian linear mixed models" p. 2, l. 55 bis 56 und p. 4, l. 122 bis 123 gegen "Bayesian Linear Mixing Models (BLMM)" p. 2, l. 53. |
| KK-06 | echt | Klammerzitate "validated in (De Doncker et al., 2020)" p. 2, l. 61, "proposed by (Steck et al., 2015)" p. 11, l. 333, "(Belotti, 2021)" und "(De Doncker et al., 2020)" p. 14, l. 424. |
| KK-07 | echt | "(Figure 1B)" p. 5, l. 146, 2A bis 2C p. 6, l. 166 bis 167, 3A bis 3E p. 9; Bildunterschriften mit (a), (b). |
| KK-08 | echt | Gl. 1 p. 5, l. 154 setzt "for i = 1, ...m" kursiv im Mathesatz. |
| KK-09 | echt | "and a prior knowledge" p. 6, l. 174. |
| KK-10 | echt | "becomes Tarantola (2005):" p. 6, l. 181. |
| KK-11 | echt | "considerately" p. 8, l. 236. |
| KK-12 | echt | "the model - here: our a posteriori erosion rate map - explains" p. 8, l. 240 bis 241, "erosion" ebenfalls kursiv. |
| KK-13 | echt | "weighed by the model covariance" p. 9, l. 245. |
| KK-14 | echt | Fig. 3c (p. 24) Legende "- quarz pattern alignment". |
| KK-15 | echt | "Gorner-gletscher catchment" p. 9, l. 267; Varianten 2, 2, 4, 1, 2 im PDF-Text exakt reproduziert. |
| KK-16 | echt | Fig. 4 (p. 25) und Fig. 12 (p. 33) Legenden: "schits", "calcarious", "caclcite-zoisite", "silimanite", "GornergratPermo-Mesozoic". |
| KK-17 | echt | Fünf Schreibweisen, acht Vorkommen: p. 9, l. 273 bis 274, p. 10, l. 299, p. 12, l. 340, p. 14, l. 411, 414, 431, 432, Bildunterschrift Fig. 12. |
| KK-18 | echt | "(Figure 6G versus Figure 6G)" p. 11, l. 317. |
| KK-19 | echt | Fig. 7 (p. 28) Kartentitel "Originial geology (same as forward)". |
| KK-20 | echt | "Smooting distance (m)" zweimal in Fig. 10 erste Zeile (x-Achse Tafel 2, Farbbalken Tafel 3), p. 31. |
| KK-21 | echt | "approximately 10-2 mm/y" p. 13, l. 384; hochgestellt "10−5" p. 13, l. 388. |
| KK-22 | echt | "Chrysolite" p. 13, l. 395; "chrysotile" p. 10, l. 274. |
| KK-23 | echt | Bildunterschrift Fig. 11 (p. 32): "Stockhorn-Turftgrat-Gornergrat" und "ecologites". |
| KK-24 | echt | "supporting the 1) the robustness" p. 13, l. 400. |
| KK-25 | echt | "applied to the same detrital sample" p. 14, l. 421 gegen "a detrital sample taken at the same date and time" p. 14, l. 437 bis 438. |
| KK-26 | echt | Figs. 14 bis 16 (p. 35 bis 37) zeigen auch im gerenderten Bild "Low-con dence area" mit Lücke. |
| KK-27 | echt | "Monte Rosa garnet-gneiss (MR g-g)" p. 14, l. 432 gegen "Monte Rosa (gneiss, micaschist)" Figs. 11, 13, "MR gneiss, mica" Figs. 15, 16 und "Monte Rosa (garnet gneiss and micaschist)" Fig. 4. |
| KK-28 | echt | Fig. 15 (p. 36) Feld "ZSF metabasites" überdeckt "ZSF serpentinite"; Fig. 16 (p. 37) erste Legendenzeile oben abgeschnitten. |
| KK-29 | echt | "oCLC:" p. 18, l. 567. |
| KK-30 | echt | "[No title found]" p. 19, l. 578. |

## 2. Literaturvorschläge

| Vorschlag | Kennung | Bereits im Literaturverzeichnis |
|---|---|---|
| Braun, Gemignani und van der Beek (2018), ESurf 6, 257 bis 270 | GB-05 | nein |
| Ehlers, Szameitat, Enkelmann, Yanites und Woodsworth (2015), JGR Earth Surface 120(6), 1023 bis 1039 | GB-05 | nein |

## 3. Doppelungen

Keine zwei Kennungen mit gleichem Fundort und gleichem Gegenstand. Teilüberschneidungen in Nebenpunkten, nicht als Doppelung gezählt: GB-07 und GB-14 (fehlende Formel für R, p. 8, l. 230 bis 234), GB-09 und GB-36 (fehlender Exportwert, p. 15, l. 453 bis 454), GB-09 und GB-17 (fehlende Pixelzahl). Gleicher Fundort bei verschiedenem Gegenstand: GB-03 und KK-29 (p. 18, l. 567), KK-15 und KK-23 (Bildunterschrift Fig. 11), GB-05 und GB-32 (p. 15, l. 454 bis 455).

## 4. Fundorte

Gezählt je Kennung (66): genau 65; um 1 bis 2 Zeilen daneben 1 (GB-10: "p. 5, l. 151 to 152 (eq. 1)", Gl. 1 steht auf l. 154); weiter daneben 0. GB-35 nennt "p. 15, l. 469 to 476", die Zeilen 474 bis 476 stehen auf p. 16; als genau gezählt.

## Zählungen

| Urteil | Anzahl |
|---|---|
| echt | 65 (GB 35, KK 30) |
| teilweise echt | 1 (GB-11) |
| falsch | 0 |
| nicht prüfbar | 0 |
| Literaturvorschläge bereits im Verzeichnis | 0 von 2 |
| Doppelungen | 0 |
| Fundorte genau / 1 bis 2 Zeilen daneben / weiter daneben | 65 / 1 / 0 |
