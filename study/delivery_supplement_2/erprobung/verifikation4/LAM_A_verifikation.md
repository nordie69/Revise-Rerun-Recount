# Verifikation des Gutachtens zu "Listen. Answer. Memorize."

Geprüft: Listen_Answer_Memorize_Copernicus_Gutachten_20261016.md gegen Listen_Answer_Memorize_Copernicus.pdf (26 Seiten, SHA-256 9065d593...595aa laut fassung.json). Zeilennummern an den gedruckten Randnummern der Seitenbilder bestätigt. Fig. 4 und Fig. 7 zusätzlich mit 300 dpi aus der PDF gerendert und vermessen (Skripte f4.py, f4lines.py, f7.py im Arbeitsordner), Zählungen und Rechnungen mit Python (zaehl.py). Literatur über WebFetch an der Quelle oder am Abstract.

Abweichungen von text.json, an den Seitenbildern festgestellt: S. 8 trägt Punkt 5 der Bedingungen Z. 181 und der Satz "When the learning path has been cut ..." Z. 182 bis 183 (text.json: 180 bis 182); S. 9 die zweite Zeile des letzten Aufzählungspunkts Z. 201; Fig.-5-Legende S. 17 Z. 358 bis 363; Z. 73 bis 74 und Z. 164 stehen noch auf S. 3 bzw. S. 7.

## 1. Urteil je Kennung

| Kennung | Urteil | Beleg |
|---|---|---|
| GB-01 | echt | Alle sechs Belegstellen der fünf Dreiautorenwerke stehen wörtlich mit drei Namen (S. 2 Z. 36 und 37 bis 38, S. 3 Z. 57 und 59 bis 60, S. 20 Z. 436, S. 12 Z. 252), Vierautorenwerke stehen mit "et al."; die Copernicus-Vorgaben (biogeosciences.net/submission.html) zeigen "Smith et al." schon für drei Autoren. |
| GB-02 | echt | RQ3 fragt wörtlich nach "what the learner has not yet mastered" (S. 3 Z. 47 bis 48), während S. 12 Z. 256 bis 257 und S. 18 Z. 392 bis 393 die Noten als Prozessdaten erklären und S. 20 Z. 424 bis 425 keinen Zweitbewerter nennt. |
| GB-03 | echt | Die drei Zitate stehen wörtlich auf S. 4 Z. 97 und Z. 103 bis 104 sowie S. 14 Z. 319 bis 320, und in Sect. 2, 3.6 und 3.7 steht keine Angabe zu Datenbanken, Suchbegriffen oder Suchdatum. |
| GB-04 | echt | Das Zitat steht auf S. 4 Z. 101 bis 102; der Abstract bei SAGE (doi 10.3102/00346543211060871) enthält wörtlich g = 0.07, p = .23, den Vorteil des Lesens bei Selbsttaktung (g = 0.13, p = .049) und bei inferentiellem und allgemeinem Verständnis, eine Sekundärquelle bestätigt 46 Studien und N = 4,687. |
| GB-05 | echt | Das Zitat steht auf S. 4 Z. 101 bis 104; die Berichtsseite der Universität Edinburgh bestätigt Titel, Autoren, IJAIED 16, S. 145 bis 170, und die Abstractstellen "caused changes in the learning gains" und "made less difference", und Litman fehlt im Literaturverzeichnis S. 24 bis 26. |
| GB-06 | echt | Die Zitate stehen auf S. 4 Z. 106 bis 107 und S. 11 Z. 250 bis 251; die ICER-2025-Seite bestätigt Gandhi und Muldner, Python, ChatGPT-4o, fünf Sitzungen, Selbstüberwachung und "a (limited) learning-mediating tool rather than a more knowledgeable other", und der Titel fehlt im Literaturverzeichnis. |
| KK-01 | echt | Der Satz steht wörtlich auf S. 2 Z. 36; der ERIC-Volltext von Cheek, LaDue und Shipley sagt, Lernende und Lehrkräfte "can be off by several orders of magnitude". |
| KK-02 | echt | Das Zitat steht auf S. 3 Z. 58 bis 59; der Abstract nennt 29 Studien insgesamt, 39 Effektstärken mit g = 0.74 in Teilmenge 1 und 54 mit g = 0.034 in Teilmenge 2. |
| KK-03 | echt | Der Satz steht auf S. 4 Z. 76 bis 77; der Abstract von Terzopoulos und Satratzemi (2020) sagt "have just started to be used in schools and universities". |
| GB-07 | echt | S. 5 Z. 113 und Fig. 1 Legende S. 6 Z. 121 bis 122 sagen, jeder Pfad habe die Prüfung bestanden, während nur die Tabellenlegende S. 5 Z. 117 bis 119 die neu geschnittenen Pfade mit 15 und 14 Sitzungen ohne dokumentierten Prüflauf nennt. |
| GB-08 | echt | Tabelle 1 (S. 5) nennt "version 1 (file name: version 6)", Fig. 1 (S. 6) "version 1: passed after exclusions", und die Zeile "Geology of Germany" in Tabelle 4 (S. 14) trägt keine Version. |
| GB-09 | teilweise echt | "stage 1" steht nur in Tabelle 1, Tabelle 4 und Fig. 1 und wird im Text nicht erklärt, Tabelle 4 nennt keine Version 4 (S. 5, S. 6, S. 14); nicht zutreffend ist die Zählung "11 times, never with a stage", denn unter den 11 Treffern in text.json sind die Tabellenzeilen "Volcanology, stage 1" (S. 5) und Tabelle 4 (S. 14), im Fließtext sind es 8 Treffer. |
| GB-10 | echt | Tabelle 4 (S. 14) beschriftet "Geological eras (fact document), version 7", die Legende S. 5 Z. 117 bis 119 zählt zugleich "version 10" des Faktendokuments und "both of its learning paths", S. 15 Z. 343 und 346 nennen die Erzählfassung ein eigenes Faktendokument mit eigenem Pfad. |
| GB-11 | echt | Am Seitenbild S. 6 trägt die Zeile der Erzählfassung in Fig. 1 "own document project (German)", die Legende Z. 121 sagt dasselbe für jedes Faktendokument, während S. 7 Z. 157 bis 159 und S. 18 Z. 382 die Erzählfassung im Projekt zu den Erdzeitaltern verorten. |
| GB-12 | echt | Die sechs Schritte (S. 7 Z. 142 bis 149) stehen im Präsens, S. 12 Z. 270 bis 272 sagt, dass keine Sitzung unter 2.6.6 oder 2.6.5 lief; 3, 8 und 14 von 25 Sitzungen sind 12, 32 und 56 Prozent (Python). |
| GB-13 | echt | S. 10 Z. 214 bis 216 nennt die korrekte Deutung "in the recorded cases" ohne Anzahl und Verfahren, S. 11 Z. 233 sagt, dass Spracheingaben nur als erkannter Text vorliegen. |
| GB-14 | echt | S. 11 Z. 228 bis 230 und S. 14 Z. 325 bis 327 stehen wörtlich, Fig. 4 (S. 15) beschriftet die gestellten Sitzungen mit 14 bis 17, und 13 von 17 sind 76,5 Prozent (Python). |
| GB-15 | echt | S. 11 Z. 238 bis 239 und 245 bis 247 sowie S. 12 Z. 275 bis 276 stehen wörtlich; 18 Abweichungen ohne Bezugszahl, 30 von 85 = 35,3 Prozent und 37 von 93 = 39,8 Prozent, 31 und 34 Befunde gegen 30 und 37 Abweichungen (Python). |
| GB-16 | echt | S. 11 Z. 240 bis 241 und Z. 248 bis 249 stehen wörtlich, das kompaktierte Gespräch wird nicht benannt, und 74 von 86 sind 86,0 Prozent (Python). |
| GB-17 | echt | S. 12 Z. 252 bis 256 nennt die drei Kriterien ohne Datum oder Quelle ihrer Festlegung, S. 17 Z. 365 verweist nur auf Sect. 3.6. |
| GB-18 | echt | Laut S. 24 Z. 497 bis 498 liegt dem Paket Pfadversion 5 bei, deren Fragen 3.1 und 3.3 in Tabelle A3 (S. 24) nach Länge und Riftphasen bis "55 Ma" fragen, gegen die Regel auf S. 2 Z. 40 bis 41; die Antworten haben 24, 21 und 22 Wörter (Python). |
| KK-04 | echt | Am Seitenbild S. 6 lautet die zweite Zeilenbeschriftung von Fig. 1 nur "Geological eras", Tabelle 1 (S. 5) "Geological eras, fact document". |
| KK-05 | echt | S. 12 Z. 265 sagt "after the ten sessions", Tabelle A2 (S. 23) datiert die Regeln der ersten Linie von 2.6.0 auf "rules proposed from 5 October", den ersten Tag der Erzählsitzungen (S. 16 Z. 349 bis 350). |
| KK-06 | echt | Am Seitenbild S. 23 ist in Tabelle A1 "Wiederholung" und "ssitzung" ohne Trennstrich auf zwei Zeilen umbrochen. |
| GB-19 | echt | Sect. 4.1 (S. 13 Z. 282 bis 299) beschreibt Prüfungen nur für Vulkanologie, Geologie Deutschlands und Erzählfassung, für Südnorwegen und die Erdzeitalter nur Chatdaten (Z. 294 bis 298), während "verified" in Titel, Z. 7, Z. 43, Z. 412, Fig. 6 und Z. 467 steht. |
| GB-20 | echt | S. 13 Z. 301 nennt sieben Läufe, die Zeile Geology of Germany in Tabelle 4 (S. 14) nennt einen ersten Lauf mit 577 Befunden und danach Korrekturen, also mindestens einen weiteren Lauf. |
| GB-21 | echt | S. 13 Z. 305 bis 306 kündigt die Prüfung der Bildblöcke an, Tabelle 4 (S. 14) hat dafür und für Überlappungen keine Spalte, Tabelle 6 Nr. 9 (S. 16) belegt einen Fehlschlag. |
| GB-22 | echt | Tabelle 4 gibt Words als Einzelzahl (S. 14 Z. 310 bis 311 "covered by the sessions"), Tabelle 1 definiert dieselbe Spalte als "in the learning path" (S. 5 Z. 115). |
| GB-23 | echt | Die Legende S. 14 Z. 312 bis 314 nennt 13,859 und 13,890 Wörter für denselben Pfad (31 Wörter, 0,22 Prozent, Python), Tabelle 4 hat keine Spalten für Datum, Skript und Faktendokumentversion, und S. 13 Z. 297 bis 298 lässt offen, welcher Pfad am 5. Oktober geprüft wurde. |
| GB-24 | echt | Tabelle 6 Nr. 6 bis 8 (S. 16) belegt abweichende Fragen in vier Sitzungen und zwei Hinweise, 12 von 75 sind 16 Prozent und 14 von 75 sind 18,7 Prozent, und die Vermessung von Fig. 4 (S. 15) ergibt für Erzählsitzungen 6 und 7 genau 1 richtig, 2 teilweise, 3 nicht richtig. |
| GB-25 | echt | Tabelle 6 Nr. 2 (S. 16) sagt "session 1 ran twice", die Legende S. 5 Z. 115 bis 117 schließt die Sitzung vom 29. September aus, und Tabelle 5 sowie S. 14 Z. 322 bis 327 erwähnen die Wiederholung nicht; Sitzung 1 misst in Fig. 4 als 1 richtig, 2 teilweise. |
| GB-26 | echt | Die Spaltenabtastung von Fig. 4 bei 300 dpi findet gestrichelte Linien nur bei x = 586,5, 744, 1946,5 und 2051,5 px (2.2.0, 2.4.0, 2.6.5, 2.6.6), keine am 9. Oktober, obwohl Tabelle A2 (S. 23) 2.6.0 zweite Linie und 2.6.1 auf den 9. Oktober 2026 datiert und die Legende S. 15 Z. 332 bis 333 alle tagesgenau datierten Versionen verspricht. |
| GB-27 | echt | Die Balken von Fig. 4 messen 12, 8, 13 sowie 1, 5, 6 sowie 16, 6, 8 Antworten (115,5 px je Antwort) und entsprechen Tabelle 5, deren Legende S. 15 Z. 328 bis 329 die Neubewertung nennt, die Legende von Fig. 4 (Z. 331 bis 334) nicht. |
| GB-28 | echt | S. 15 Z. 338 bis 340 nennt 24 Einträge aus Version 6 mit zwei Schließungen durch Neubewertung, Tabelle 5 ergibt 8 + 13 = 21 nicht voll richtige Antworten; vor der Neubewertung ergeben k = 0 bis 3 hochgestufte Antworten 21 bis 24 (Python), die Bilanz schließt also nur mit einer nicht genannten Lesart. |
| GB-29 | echt | S. 15 Z. 340 bis 341 nennt nur zwei abgeschlossene Wiederholungen, die abgebrochene steht nur in Tabelle 6 Nr. 5 (S. 16) und S. 20 Z. 439, und Modus, Version und Note der Wiederholungen fehlen, obwohl Tabelle 3 (S. 10) sie im Protokoll führt. |
| GB-30 | echt | S. 15 Z. 344 bis 345 nennt eine einzige Prüfung durch "a second AI agent" ohne Modell, Anweisung oder Ergebnis, S. 18 Z. 382 bis 383 und S. 4 Z. 100 bis 101 übernehmen die Vollständigkeit als Ergebnis. |
| GB-31 | echt | Am Seitenbild S. 17 hat Fig. 5 Marken für 2.1.0, 2.2.0, 2.4.0, 2.5.0, 2.6.0 erste Linie, 2.6.1, 2.6.5 und 2.6.6, keine für 2.3.1 und 2.6.0 zweite Linie, obwohl die Legende Z. 359 bis 360 die Versionen nach Tabelle A2 verspricht und S. 12 Z. 262 die ersten drei Sitzungen 2.3.1 zuordnet. |
| GB-32 | echt | S. 17 Z. 369 nennt "three or four cases" am Bildschirm, Z. 371 bis 372 aus den Protokollen höchstens zwei Sitzungen und nennt das "a similar picture". |
| KK-07 | echt | "marks as no learning material" steht auf S. 13 Z. 306 bis 307 und in Tabelle 6 Nr. 3 (S. 16). |
| KK-08 | echt | Die Legende S. 15 Z. 331 nennt kein Jahr, und die Achsenbeschriftungen von Fig. 4 lauten "28 Sep" bis "13 Oct" ohne Jahr. |
| KK-09 | echt | Tabelle 6 Nr. 4, Spalte Trigger (S. 16), lautet "an own list of exclusions replaced the default". |
| KK-10 | echt | Tabelle 6 Nr. 4, Spalte Rule or remedy (S. 16), lautet "proposal that own exclusions supplement the default". |
| KK-11 | echt | Tabelle 6 Nr. 8 (S. 16) lautet "the voice gave a hint on question 4.3". |
| KK-12 | echt | Die Legende von Fig. 5 verweist S. 17 Z. 359 für Sitzungen je Tag auf Tabelle 1, die nur Summen je Fall enthält (S. 5). |
| GB-33 | echt | Die Suche in Z. 380 bis 482 findet weder Clinton-Lisell, Putnam, Terzopoulos, Nückles, Zhang noch "journal" oder "listen", obwohl S. 4 Z. 107 bis 108 die dritte und vierte Hinsicht RQ2 und RQ3 zuordnet. |
| GB-34 | echt | Das Zitat steht auf S. 18 Z. 389 bis 391; "decimal" und "interrupt" stehen sonst nur in Z. 165, Z. 198 und Tabelle A2, nicht in Sect. 4.3, 4.4, 4.7 oder Tabelle 6, und die Raute "do not interrupt the learner" liegt in Fig. 5 (S. 17) am 12. Oktober im grauen Feld "no sessions after 8 October". |
| GB-35 | echt | S. 18 Z. 394 behauptet die Wirkung als Schutz, Fig.-7-Legende S. 19 Z. 409 bis 410 sagt, Lesen, Fragen und Bewerten beruhten nur auf Regeln, und Tabelle 6 Nr. 6 und 7 belegen vier Sitzungen mit abweichenden Fragen (16 Prozent). |
| GB-36 | echt | S. 2 Z. 32 und S. 19 Z. 397 bis 398 stehen wörtlich, der Standardmodus beginnt mit Einleitung (S. 11 Z. 224 bis 225), und S. 20 Z. 432 bis 433 und 448 bis 449 erlauben Allgemeinwissen im Erklärmodus. |
| GB-37 | echt | Bei 300 dpi zeigt der Pfeil Sources nach Fact document (S. 19) Striche von 10 bis 11 px mit 6 px Lücke, die Legende "checked in the document project" Punkte von 6 bis 7 px mit 13 px Lücke und die Strichlegende 19 bis 21 px; die Werte des Gutachtens für die Legendenpunkte (5 bis 6 px, Lücke 10 bis 11 px) weichen um 1 bis 2 px ab, der Befund bleibt. |
| GB-38 | echt | S. 20 Z. 438 bis 439 datiert beide Zahlen auf den 8. Oktober, S. 15 Z. 338 bis 340 bezieht das Datum nur auf Südnorwegen ("for that case"). |
| GB-39 | echt | S. 22 Z. 469 sagt "built the learning environment himself", S. 12 Z. 277 bis 278, S. 20 Z. 446 bis 447 und Fig.-8-Legende S. 21 Z. 459 bis 460 schreiben Entwurf und Bau der Skillversionen dem Assistenten zu. |
| GB-40 | echt | Der Vorschlag steht auf S. 22 Z. 473 bis 475; S. 14 Z. 325 bis 327 (13 von 17 Sitzungen ohne Fragen, 76,5 Prozent), S. 20 Z. 434 bis 437 (kein Zeitplan), S. 12 Z. 256 bis 257 und S. 11 Z. 221 bis 224 stehen wie zitiert. |
| GB-41 | echt | S. 22 Z. 476 bis 477 steht wörtlich und weiter als die fünf Bedingungen in S. 8 Z. 168 bis 181, und Z. 479 bis 480 sowie S. 1 Z. 21 bis 22 nennen den Einsatz in anderen Fächern ungeprüft. |
| GB-42 | echt | S. 24 Z. 495 bis 500 nennt nur das Skillpaket und die nicht veröffentlichten Protokolle und Methodenanalysen, die übrigen Quellen aus S. 11 Z. 232 bis 249, S. 7 bis 8 Z. 164 bis 167 und S. 10 Z. 203 fehlen; die Biogeosciences-Datenrichtlinie verlangt wörtlich eine Zugangserklärung und "a detailed explanation". |
| KK-13 | echt | Die Anmerkung in Fig. 7 (S. 19) lautet "no second grader (Sect. 3.6)", "second grader" steht im Text nur in S. 20 Z. 425. |
| KK-14 | echt | Die URL ist auf S. 24 Z. 495 bis 496 am Bindestrich "Listen-" / "Answer-Memorize" umbrochen. |
| KK-15 | echt | Die drei DOIs sind auf S. 25 Z. 530 bis 531 und S. 26 Z. 548 bis 549 sowie 554 bis 555 am Bindestrich umbrochen. |
| KK-16 | echt | Latimier (S. 26 Z. 548) und Nückles (Z. 559 bis 560) stehen ohne Heftnummer, Agarwal in derselben Zeitschrift mit "33(4)" (S. 25 Z. 512); die vorgeschlagene Heftnummer 4 für Nückles war über die erreichbaren Seiten nicht zu bestätigen (Crossref gesperrt). |

## 2. Literaturvorschläge

| Vorschlag | Kennung | Bereits im Literaturverzeichnis |
|---|---|---|
| Litman, Rosé, Forbes-Riley, VanLehn, Bhembe und Silliman (2006), IJAIED 16 | GB-05 | nein |
| Gandhi und Muldner (2025), ICER 2025 | GB-06 | nein |
| Clinton-Lisell (2022), Moderatoren ergänzen | GB-04 | ja (S. 25 Z. 520 bis 522) |
| Nückles et al. (2020), in der Diskussion aufgreifen | GB-33 | ja (S. 26 Z. 558 bis 560) |
| ICS-Chart v2026/06, Lehrbücher und Open-Access-Quellen der Faktendokumente zitieren | GB-42 | nein |
| Ruan et al. (2019) QuizBot, nur im Prüfprotokoll PP-26 genannt, ohne Befund | PP-26 | nein |

## 3. Doppelungen

Keine zwei Kennungen haben denselben Fundort und denselben Gegenstand. Teilüberschneidungen ohne volle Doppelung: GB-21 und GB-22 (beide Tabelle 4, beide schlagen eine Spalte für überlappende Wörter vor); GB-08 und GB-09 (beide fehlende Pfadversion in Tabelle 4, aber verschiedene Zeilen); GB-10 und GB-23 (Faktendokumentversion je Prüflauf, GB-10 verweist selbst auf GB-23); GB-03 und GB-05 (dritte Hinsicht der Lücke, S. 4 Z. 101 bis 104 und S. 14 Z. 319 bis 320, aber Suchbeschreibung gegen fehlende Arbeit); GB-15 und GB-42 (Veröffentlichung einer Tabelle je Sitzung); KK-09 und KK-10 (Wendung "own exclusions" in zwei Zellen derselben Zeile 4 von Tabelle 6).

## 4. Fundorte

58 Kennungen (42 GB, 16 KK) geprüft.

| Lage des Fundorts | Anzahl | Kennungen |
|---|---|---|
| genau | 56 | alle übrigen; bei GB-33 (Z. 73 bis 74 stehen auf S. 3, nicht S. 4) und GB-42 (Z. 164 steht auf S. 7, nicht S. 8) stimmen die Zeilen, nur die Seitenangabe einer Nebenstelle ist falsch |
| 1 bis 2 Zeilen daneben | 2 | GB-21 (S. 8 Z. 180 bis 182 statt 181 bis 183), GB-41 (S. 8 Z. 168 bis 180 statt bis 181) |
| weiter daneben | 0 | |

Beide Abweichungen betreffen Nebenstellen und folgen der Verschiebung in text.json auf S. 8; die Hauptfundorte stimmen in allen 58 Kennungen.

## 5. Zählung je Urteil

| Urteil | Anzahl |
|---|---|
| echt | 57 |
| teilweise echt | 1 (GB-09) |
| falsch | 0 |
| nicht prüfbar | 0 |
