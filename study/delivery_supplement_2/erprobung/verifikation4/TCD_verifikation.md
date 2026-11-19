# Verifikation des Gutachtens zu "Talk, Check, Decide" (TCD)

Geprüft: Talk_Check_Decide_A_Skill-Based_Workflow_Gutachten_20261016.md gegen Talk_Check_Decide_A_Skill-Based_Workflow.pdf (25 Seiten). Zeilen an den gedruckten Randnummern der Seitenbilder seite-01 bis seite-25 bestätigt; text.json stimmt mit den Randnummern überein, außer bei den Bildunterschriften auf S. 2 und S. 8 (dort um eine Zeile verschoben; maßgeblich sind die Seitenbilder: Graphical abstract l. 21 bis 24, Figure 2 l. 151 bis 154). Rechnungen mit Python (rechnen.py im Arbeitsordner), Farben am Seitenbild gemessen, eingebettete Bilder mit pdfimages gezählt. Literatur: gelesen wurden die Geoinfo-Richtlinie, SkillsBench (aktuelle arXiv-Fassung und v1 als HTML), Topaz et al. (2026a, arXiv-Abstract), Güneş, Cesur und Çamur (2026, dirjournal.org), Wolniewicz (2024, MDPI-Volltext), Revilla et al. (2020, SAGE-Abstract), Wu et al. (2025, Nature Communications) und Gao et al. (2023, ACL Anthology); nicht gelesen wurde Yang et al. (2025).

## 1 Urteile je Kennung

| Kennung | Urteil | Beleg |
|---|---|---|
| GB-01 | echt | RQ1 bis RQ3 (S. 2, l. 34 bis 38) nennen Diktat nicht, die Lücke steht S. 4, l. 84 bis 85, "the share was not measured" S. 8, l. 155 bis 156, Titel "Talk" S. 1, l. 1 und Abstract l. 10. |
| GB-02 | echt | Am Seitenbild S. 2 führt ein Pfeil vom oberen Rand des AUTHOR-Kastens "confirms, changes or rejects" zum AI-Kasten "researches, proposes full wording", Farbe gemessen #d95f2b gleich dem AUTHOR-Kopf; die Unterschrift l. 21 bis 24 erklärt ihn nicht, das Zitat l. 141 bis 142 ist wörtlich vorhanden. |
| GB-03 | echt | "graphical" kommt nur in der Unterschrift S. 2 (l. 21) und in "Geographical" S. 24, l. 562 vor; Figures 1 bis 6 sind an l. 108, 122, 158, 161, 214/331, 261 zitiert. |
| GB-04 | echt | Manuskript S. 2, l. 27 bis 28; die Richtlinie (geoinfo.org-PDF) sagt "Sufficient information necessary to replicate the trip should be included" und "This may be in the form of a road log with mileage between stops, GPS coordinates at each stop ... or any other method", also Koordinaten als Option. |
| GB-05 | echt | SkillsBench fehlt im Literaturverzeichnis (S. 19 bis 25); arXiv v1 (HTML) bestätigt "86 tasks across 11 domains" (Abstract; der Haupttext nennt 84), 7.308 Trajektorien, 24,3 % auf 40,6 % (+16,2 Punkte), selbst erzeugte Skills "-1.3pp" ("no benefit on average"), "human-curated domain expertise" und die Autorenfolge Li, Chen, Liu; die aktuelle arXiv-Fassung weicht ab (87 Aufgaben, 8 Domänen, 33,9 % auf 50,5 %, Folge Li, Liu, Chen), die vorgeschlagene Angabe sollte daher die Version v1 nennen. |
| GB-06 | echt | S. 3, l. 45 bis 46 gibt nur 59,6 % für Claude 3 Opus; die Quelle (dirjournal.org) nennt 80,8 % voll korrekte Angaben für Claude 3.5 Sonnet, "<8% fully accurate references" für die ChatGPT-Modelle (5,6 bis 7,3 %) und 2,7 % für Gemini 1.5 Pro; die Fabrikationswerte des Manuskripts (3,1 %, 18,3 %, 27,7 bis 60,6 %) stimmen. |
| GB-07 | echt | Das Abstract von Topaz et al. (2026a) nennt "Fabrication ranged from 10.2% (Claude Opus 4.8, which declined 52.1% of prompts)", 54,6 % für Opus 4.6 und 55,4 % insgesamt; 18,5 % steht nicht im Abstract; 10,2/(1 - 0,521) = 21,3 % nachgerechnet; Manuskript S. 3, l. 46 bis 48. |
| GB-08 | echt | S. 3, l. 50 bis 51 zitiert Gao et al. (2023) und Wu et al. (2025) gemeinsam; Wu et al. (Nature Communications) sagt "Even for GPT-4o with Web Search, approximately 30% of individual statements are unsupported", das ALCE-Abstract von Gao et al. (ACL Anthology) nennt GPT-4o nicht und gibt "lack complete citation support 50% of the time". |
| GB-09 | echt | Die Quelle (MDPI, Llama 3, 299 Texte) nennt 134 polnische Texte (44,8 %) mit Nachbearbeitungsbedarf, 4 englische (1,3 %) mit Bedarf an deutlicher Sprachverbesserung, 10 (3,3 %) und 9 (3,0 %) mit falschem oder missverständlichem Inhalt; der Inhalt wurde "manually scanned", die Feldarbeit entfernte 123 von 299 Orten; Manuskript S. 3, l. 65 bis 67 vergleicht also zwei Kategorien. |
| GB-10 | echt | Der Sprachabsatz S. 3 bis 4, l. 72 bis 78 und die Lücke l. 84 bis 85 nennen keine Arbeit zum LLM-gestützten Schreiben mit Sprache; Yang et al. (2025) selbst konnte ich nicht lesen, die Einordnung stützt sich auf das bekannte System Rambler (Lin et al., CHI 2024). |
| GB-11 | echt | Das Abstract von Revilla et al. (2020, SAGE) sagt "when dictation was used, we found fewer valid answers and less information provided" bei Kontrollgruppen mit Texteingabe, Sprachaufnahme gab längere Antworten; das Manuskript (S. 4, l. 74 bis 75; S. 15, l. 301 bis 304) nennt nur den Abstand zur Sprachaufnahme. |
| GB-12 | echt | S. 4, l. 83 bis 85 nennt 24 Anfragen, Sprachen und Werkzeuge, aber keine Suchbegriffe, kein Datum und kein GeoRef; Zhang et al. (2020) steht S. 4, l. 76 bis 77. |
| GB-13 | echt | Tabelle 1 (S. 4): Germany nennt Dateiarten ohne Zahlen und Literatur ohne Anhänge, Norway Zahlen und Anhänge ohne Literatur; "Germany organisation file" steht nur in Fig. 6, Zeile 6 (S. 14), sonst nirgends; "logs" S. 19, l. 390, "the decision log" S. 10, l. 194. |
| GB-14 | echt | Sechs Dimensionen (Tab. A1, S. 18), 11 Pflichten und 15 Typen (S. 13, l. 249 bis 250), 12 Gruppen (S. 5, l. 100) und drei Beispielmetriken (S. 6, l. 124) werden genannt, aber nicht aufgelistet. |
| GB-15 | teilweise echt | Fig. 1 (S. 6) hat orange, schwarze und graue Pfeile, die Legende erklärt nur Kastenfarben; falsch ist "the remaining four arrows are dark grey": gemessen sind fünf Pfeile grau (#4b4b4b), zwei orange (#d95f2b), einer schwarz (#1a1a1a). |
| GB-16 | echt | "which closes the loop" S. 6, l. 120 gegen "The loop does not close" S. 5, l. 107 bis 108, beide wörtlich. |
| GB-17 | echt | Acht datierte Ergebnisse (13., 15., 18., 19., 19., 21., 24., 26. September) liegen sieben vor dem 26. und alle vor dem 27. September; Skills "in their state of 27 September 2026" S. 19, l. 386, Verfahren seit 26. September S. 7, l. 136 bis 137; Norway 10. bis 28. September = 19 Tage, 3 ab dem 26. (15,8 %). |
| GB-18 | echt | Zusage S. 7, l. 146 bis 147, Verlust der 30 Eingaben nur S. 17, l. 352 bis 353, Chatprotokoll seit 1.5.0 vom 27. September S. 19, l. 384 bis 385; die Frage beruht auf zutreffenden Prämissen. |
| GB-19 | echt | "75 by 28 September 2026, this one included" S. 7, l. 144; Regel "keep working notes out of the deliverable" S. 10, l. 180. |
| GB-20 | echt | "the system" steht genau achtmal: S. 8, l. 156, 158 (zweimal), 160; S. 15, l. 300, 302, 306; S. 17, l. 369; "assistant" 40-mal nachgezählt. |
| GB-21 | echt | Spracherkennung in Fig. 4 (S. 9) ohne Namen, Modellwechsel S. 11, l. 203 bis 204 ohne Datum, nur 3 von 22 Einträgen mit Version (S. 19, l. 383 bis 384), also 19 ohne. |
| GB-22 | echt | Unterschrift Fig. 4 (S. 9) sagt "are caught because ...", der Text S. 8, l. 160 begrenzt auf "in the author's experience"; keine Zählung im Manuskript. |
| GB-23 | echt | Abschnitt 4 berichtet Germany für Konsistenz, Faktenbeleg, Literatur, Gattung, Norway für Konsistenz, Fundstelle, Nutzen: 5 von 12 Feldern leer; Reihenfolge und Abweichung für Germany S. 10, l. 186 bis 189. |
| GB-24 | echt | Namen nachgezählt: "consistency run(s)" 7-mal, "reference check" l. 14, 262, 269, "fact check" l. 287, 364 bis 365, "three-perspective critique" l. 254, "genre analysis" l. 187, 363, "consistency checks" für Skills l. 106, 119; Tabelle 2 (S. 10) führt keine Kurzformen. |
| GB-25 | echt | Quellenklassen S. 10, l. 196 bis 198; 32 von 117 = 27,4 % (l. 199 bis 200); Museumsprüfung ohne Datum und Version S. 12, l. 232. |
| GB-26 | echt | Fig. 5 (S. 12): Befunde 18, 4, 6, 4, 0, 2, 71, Nichtbefunde 9, 6, 10, 12, 12, 10, 42; nachgerechnet kumuliert 9, 15, 25, 37, 49, 59 und Verdachtsfälle 27, 10, 16, 16, 12, 12, 113; "report only" und "two-part run" am Seitenbild; Germany 10+9+7 = 26, 3+5+4 = 12. |
| GB-27 | echt | Differenzen -14, +2, -2, -4, +2 nachgerechnet; Anstiege nach "localities renumbered, literature added" (Run 3) und "measures of the three-perspective critique" (Run 6), Fig. 5 gibt keine Größe der Änderungen; Satz S. 11, l. 211. |
| GB-28 | echt | Zitate S. 11, l. 215, S. 5, l. 100 bis 101 und S. 10, l. 202 bis S. 11, l. 203 wörtlich; 9+6+10+12+12+10+42 = 101 nachgerechnet. |
| GB-29 | echt | S. 11, l. 215 bis 218 nennt 16 Nichtbefunde nur für den ersten Kapitel-1-Lauf, drei Läufe auf zwei Daten, Kapitel-1-Läufe ohne Datum. |
| GB-30 | echt | Am Seitenbild S. 12 stehen unter Run 1 "first run, report only" und unter Run 7 "target format now dossier; two-part run"; Unterschrift l. 221 bis 222 kündigt "the change made before it" an. |
| GB-31 | echt | S. 12, l. 231 bis 232: 20 Aussagen in 19 Zeilen, Urteile 12 + 4 + 3 = 19 Zeilen; 3/19 = 15,8 %, 3/20 = 15,0 %, 1/36 = 2,8 % nachgerechnet. |
| GB-32 | echt | S. 13, l. 237 bis 241 nennt 5, 6, 4 von 6 und 3 ohne vollständige Aufteilung; 13/211 = 6,16 %, 211/8 = 26,4 nachgerechnet. |
| GB-33 | echt | 226 Einträge in v15 (Tab. 1, S. 4; S. 15, l. 311) gegen 211 am 18. September (S. 13, l. 237); 226 - 211 = 15 = 6,6 % nachgerechnet; "one in eight" für "the Germany list" S. 14, l. 273 bis 274 und S. 17, l. 362. |
| GB-34 | echt | Keine Stichprobe der als richtig durchgelassenen Einträge oder der 29 nicht markierten Mindat-Zitate berichtet (S. 13, l. 237 bis 247); 26/55 = 47,3 % nachgerechnet. |
| GB-35 | echt | S. 13, l. 244 bis 247: 55 Zitate, 26 Vorschläge, 21 + 4 + 1 = 26, 22 Änderungen, ohne Zuordnung der Einheiten. |
| GB-36 | echt | S. 13, l. 246 bis 247 sagt wörtlich "which had not seen the results of the first pass, confirmed 21 of them"; die Frage nach der Eingabe ist logisch begründet. |
| GB-37 | echt | S. 13, l. 249 bis 254 gibt 9 von 11 nur für eine Gattung; Tab. A1 (S. 18): "a finished report against every candidate genre". |
| GB-38 | echt | Tab. A1 (S. 18): "with 15 measures each" bei drei Perspektiven, 3 × 15 = 45; S. 13, l. 255 bis 256 zweimal 45. |
| GB-39 | echt | Fig. 6 (S. 14): Zeilen 1 und 6 template-dokumentprojekt, 2 bis 4 science-quellenapparat-pruefung, 5 science-arbeitsplan-erstellen; 43 Regeln nicht aufgelistet, "examples" S. 14, l. 268 bis 269 (im Einwand mit l. 269 angegeben). |
| GB-40 | echt | S. 11, l. 206 bis 208 nennt "Claude" ohne Version und "verified against" bibliografische Ziele; S. 19, l. 395 "wrote, reviewed and edited the manuscript". |
| GB-41 | echt | Wolniewicz nur S. 3, l. 67 und im Verzeichnis; Walters, Güneş und Topaz nur in Abschnitt 2; Abschnitt 6 (S. 17, l. 367 bis 379) nimmt die Lücke nicht auf. |
| GB-42 | echt | Zitate S. 14, l. 271 bis 273 und S. 17, l. 367 bis 368 wörtlich, Abstract S. 1, l. 15 bis 16 "suggest"; 68 + 6 + 1 = 75, keine Ausgangszählung der Vorschläge in Abschnitt 4. |
| GB-43 | echt | RQ2-Antwort S. 14, l. 274 bis 280 ohne Herkunft; Fig. 6 Zeilen 2 und 4 am Seitenbild; "invisible to both" S. 15, l. 290; "unchecked bibliography" S. 12, l. 233. |
| GB-44 | echt | Konvention S. 5, l. 113 bis 114 "Each of their rules names the incident it came from" gegen Beleg S. 15, l. 281 bis 283; 31 + 12 = 43. |
| GB-45 | echt | "Every finding carried a count or a location" S. 15, l. 292 gegen ungeprüfte Wiederherstellung S. 13, l. 265, Fig. 6 Zeile 4 und fehlende Daten S. 12, l. 232 und S. 13, l. 255. |
| GB-46 | echt | Empfehlung und Wechsel S. 16, l. 340 bis 343 wörtlich, Wortzählproblem l. 338 bis 339; Prüfweg nach dem 27. September nicht genannt. |
| GB-47 | echt | pdfimages zählt 7 Bilder (S. 2, 6, 8, 9 zweimal, 12, 14), Graphical abstract 211 ppi, Figuren 200 ppi; Satz S. 16, l. 345 bis 346. |
| GB-48 | echt | "each tested once or not at all" S. 17, l. 362 bis 363 gegen beide Verwendungen S. 13, l. 249 bis 253. |
| GB-49 | echt | "243 log entries" S. 17, l. 363 bis 364, "doubled the work" S. 16, l. 336; keine Zeitangabe, keine Aufwandszahl für Germany. |
| GB-50 | echt | Leichtere Fassung S. 17, l. 364 bis 365 nennt nur Register, Konsistenz und Faktenprüfung; Gegenstellen l. 289 bis 290, 279 bis 280, 256 bis 257, 186 bis 187, 347 bis 351 wörtlich; dass die übrigen Achsen entfallen, ist eine zulässige Lesart der Aufzählung. |
| GB-51 | echt | S. 17, l. 368 bis 369 "complete wording of every proposed change" gegen Ausnahmen S. 6, l. 125 bis 126 und Beginn 26. September S. 7, l. 136 bis 138. |
| GB-52 | echt | S. 17, l. 374 bis 376 nennt beide Studien ohne Vergleichsbedingung. |
| GB-53 | echt | Ausblick S. 17, l. 377 bis 379; Gegenstellen S. 16, l. 328 bis 330, S. 13, l. 264 bis 265, S. 6, l. 128 bis 133 (alle auf S. 6, Fundort sagt "p. 6 to 7"), S. 5, l. 114 bis 116. |
| GB-54 | echt | Acht Quellenarten S. 10, l. 196 bis 198, davon Kritiken, Zusammenfassungsdokument und Chats nicht in der Erklärung S. 19, l. 389 bis 392; Skripte "kept with the figures" S. 16, l. 346. |
| GB-55 | echt | Am Seitenbild: Amershi (S. 20, l. 406 bis 407) und Deng (S. 21, l. 440 bis 443) mit Verlag und Ort, Jansen (S. 22, l. 485) nur "IEEE", Gao, Manakul, Dhuliawala, Rohanian ohne Verlag; Christiano ohne Seiten, Ouyang und Madaan mit; ISBN-10 bei Compton und Schön. |
| KK-01 | echt | Titelzeile im Graphical abstract (S. 2) lautet "Talk, Check, Decide: AI-assisted scientific geological excursion reports", abweichend vom Titel S. 1, l. 1 bis 2. |
| KK-02 | echt | Am Seitenbild S. 3 endet l. 44 mit "18.3", l. 45 beginnt mit "%, against". |
| KK-03 | echt | S. 10, l. 198 "the Norway records begin on 10 September" ohne Jahr (das Jahr steht im selben Satz bei "28 September 2026"). |
| KK-04 | echt | S. 10, l. 201 bis 202 "so numbered since 21 September 2026" wörtlich vorhanden. |
| KK-05 | echt | Am Seitenbild S. 13 endet l. 237 mit "about 6", l. 238 beginnt mit "%."; 13/211 = 6,16 %. |
| KK-06 | echt | S. 16, l. 317 bis 318 wörtlich, der Beleg steht hinter "section 3.2". |
| KK-07 | echt | S. 16, l. 323 "the permanent feedback between skill, report and review" wörtlich. |
| KK-08 | echt | S. 17, l. 374 "Two questions should be measured then:" wörtlich. |
| KK-09 | echt | S. 19, l. 394 "carried out the fieldwork and both excursion reports" wörtlich. |

## 2 Literaturvorschläge: bereits im Literaturverzeichnis?

| Vorschlag | Kennung | Im Verzeichnis |
|---|---|---|
| Li et al. (2026) SkillsBench, arXiv 2602.12670 | GB-05 | nein |
| Yang et al. (2025) Rambler in the wild, CHI EA '25 | GB-10 | nein |
| Lin et al. (2024) Rambler, CHI '24 | GB-10 | nein |
| Wu et al. (2025), allein für den GPT-4o-Wert | GB-08 | ja (S. 24, l. 568 bis 570) |
| Gao et al. (2023), mit eigenem ALCE-Ergebnis | GB-08 | ja (S. 21, l. 455 bis 457) |
| Wolniewicz (2024), mit korrigierten Werten | GB-09, GB-41 | ja (S. 24, l. 566 bis 567) |
| Revilla et al. (2020), Vergleich mit getippter Eingabe | GB-11 | ja (S. 23, l. 533 bis 534) |
| Zhang et al. (2020), Abgrenzung der Diktathälfte | GB-12 | ja (S. 25, l. 571 bis 572) |
| Lenzner, Höhne und Gavras (2024), Maße für Studie 1 | GB-52 | ja (S. 22, l. 492 bis 494) |
| GeoRef und Google Scholar | GB-12 | entfällt (Datenbanken, keine Arbeiten) |

Neu vorgeschlagene Arbeiten: 3, davon 0 bereits im Verzeichnis.

## 3 Doppelungen

Kein Paar mit gleichem Fundort und vollständig gleichem Gegenstand. Ein Paar überschneidet sich teilweise: GB-34 (Mindat-Teil: der zweite Durchgang prüfte nur die Vorschläge, nicht die 29 durchgelassenen Zitate) und GB-36 (was der zweite Durchgang als Eingabe sah), beide S. 13, l. 245 bis 247; GB-36 verweist selbst auf GB-34. Nahe, aber im Gegenstand verschieden: KK-05 und GB-32 (S. 13, l. 237 bis 238, Satzspiegel gegen Aufteilung), KK-02 und GB-06 (S. 3, l. 44 bis 46, Satzspiegel gegen Inhalt), GB-26 und GB-27 (S. 11, l. 211, Störgrößen gegen Beschreibung), GB-17 und GB-21 (S. 19, l. 383 bis 386, Chronologie gegen Arbeitsumgebung).

## 4 Fundorte

| Klasse | Anzahl |
|---|---|
| genau | 64 |
| um 1 bis 2 Zeilen daneben | 0 |
| weiter daneben | 0 |

Anmerkungen ohne Einfluss auf die Zählung: GB-53 gibt "p. 6 to 7, l. 128 to 133" an, die Zeilen stehen alle auf S. 6. Im Einwand von GB-39 steht "The six rows are examples" bei l. 269, gedruckt beginnt der Satz am Ende von l. 268.

## 5 Zählungen je Urteil

| Urteil | Anzahl | Kennungen |
|---|---|---|
| echt | 63 | alle übrigen |
| teilweise echt | 1 | GB-15 |
| falsch | 0 | |
| nicht prüfbar | 0 | |
| gesamt | 64 | 55 GB, 9 KK |

Nachprüfung am 17. Oktober 2026: GB-06, GB-09 und GB-11 von "nicht prüfbar" auf "echt", GB-05 nach Lesen von SkillsBench v1 von "teilweise echt" auf "echt"; GB-08 an beiden Quellen bestätigt.
