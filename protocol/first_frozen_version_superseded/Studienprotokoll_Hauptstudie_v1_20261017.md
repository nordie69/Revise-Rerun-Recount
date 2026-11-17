# Studienprotokoll der Hauptstudie: Wirksamkeit von Fassungen der Review-Skills

Eingefroren am 2026-10-17 nach Prüfung durch Paper 3 (Workplan Paper 3, Schritt 3.1). Die Prüfsumme steht in `Studienprotokoll_Hauptstudie_v1_20261017.sha256`. Änderungen gibt es nur als datierte Nachträge (Abschnitt 13). Paper: „Revise, Rerun, Recount: Measuring whether revising AI review skills helps them find the issues human referees raise in geoscience preprints“ (Paper 3, Entscheidung 18). Wortlaut von RQ3 bestätigt als Paper 3, Entscheidung 16. Grundlage: Studienhandbuch der Hauptstudie (DAT-29), Übergabe aus Paper 3 v3 vom 2026-10-16 (DAT-43).

## 1. Forschungsfragen und Erwartungen (P-8)

| Nr. | Frage | Vergleich | Erwartung |
|---|---|---|---|
| RQ1 | Wie verändern sich die Befunde der Review-Skills über ihre Fassungen an denselben Manuskripten, gemessen gegen externe Sollbefunde und gegen die Streuung zwischen Läufen derselben Fassung? | A gegen B | B trifft mehr bestätigte Sollbefunde als A, und der Unterschied ist größer als die Streuung der drei Läufe von B. |
| RQ2 | Finden getrennte Prüfinstanzen getrennte Fehler, und welcher Anteil der zutreffenden Befunde stammt von nur einer Instanz? | B gegen C | B trifft mehr als C; mindestens ein Fünftel der zutreffenden Befunde in B stammt nur von einer Instanz. |
| RQ3 | Kann ein Agent aus dem Prüfbericht eines Laufs die dem Skill fehlende Regel vorschlagen, und senkt die bestätigte Regel die betroffene Fehlerklasse im nächsten Lauf? | B gegen D | D zeigt je Gutachten weniger Fälle der Fehlerklassen F1 bis F7 (`rq3/Regelvorschlaege_RQ3.md`) als B, ohne weniger Sollbefunde zu treffen. |

Die Erwartungen wurden vor dem ersten Lauf der Hauptstudie festgelegt (Chatprotokoll C-95).

## 2. Fassungen (P-8, SB-24)

| Bedingung | science-review-gutachten | science-review-abbildungen | science-review-studiendesign |
|---|---|---|---|
| A | 1.0.0, `paket/science-review-gutachten_v1_20261015.skill`, SHA-256 7a2d507149f7af0bb2659e5c8c8cb91f56a8f719fd42cebe0c12eaac1f044fd5 | 1.0.0, SHA-256 3885b30294012f5ea102a9616a2751fd859c3330f31ac339af9472703dfe0bd6 | 1.0.0, SHA-256 a44abec7eafc9ea78830050836da09fca36b92b037e0e64c035426494b9ba106 |
| B, C (Ausgangsfassung) | 1.3.0, `paket/science-review-gutachten_v1_20261016_3.skill`, SHA-256 9fc7d78e7d326286ab1ac0209d5c704b18ccf4e54500dfade1bf5e008f63e263 | 1.2.0, SHA-256 d10a409da3e81186c7f7fa520913c5ff8a2073df566e8831d141b62c62675830 | 1.2.0, SHA-256 9c9a62f9996c8e814fcdca51213c4186652c76aca2e6347b8242ca8d23fbdb1a |
| D | 1.4.0, `paket/science-review-gutachten_v1_20261017.skill`, SHA-256 66dcd7c60f8a290e27f5a3a625daa652ec590119da2f5885fb379915d7d9ea20 | 1.3.0, SHA-256 ce3468d002152782e1b85bf761798a471c2229e7c7e8be55a3a1ad3acc4402d6 | 1.2.0, wie B |

Herkunft der Regeln von D: Ein eigener Agent R ohne Skill erhielt nur die vier Prüfberichte von Prüfdurchgang 4, die zugehörigen Gutachten und die installierten Skills der Ausgangsfassung (Auftrag `rq3/auftrag_R.txt`). Er sammelte 52 Fälle, ordnete 33 davon sieben Fehlerklassen zu und schlug je Klasse eine Regel mit Zählregel vor (`rq3/Regelvorschlaege_RQ3.md`). Der Auftraggeber bestätigte alle sieben (`rq3/Entscheidungen_RQ3.md`), der Assistent baute sie in Gutachten 1.4.0 und Abbildungen 1.3.0 ein. Der Skill selbst hat keine Regel vorgeschlagen; eigene Regeln des Assistenten zum Vergleich gibt es nicht, weil er die Vorschläge von R vor einer eigenen Ableitung kannte. Stattdessen lief ein zweiter Agent R2 mit demselben Auftrag unabhängig (`rq3/R2/`), und K9 misst die Übereinstimmung. Ort jeder Regel: `Herkunft_der_Regeln_v1_20261017.md`.

Die Ausgangsfassung (B) wurde vor dem Einfrieren in Prüfdurchgang 4 am Baumaterial mit den Abnahmekriterien AK-01 bis AK-14 abgenommen (EP-22, Trefferbilanz). Jede Bedingung liest ihre Skills aus dem entpackten Paket ihrer Fassung; vor jedem Lauf wird die Dateigleichheit des entpackten Ordners mit dem Paket geprüft und im Laufregister vermerkt.

## 3. Testmaterial (P-1, P-2)

Vier EGUsphere-Vorabdrucke fremder Autoren, Fassung 1, mit den Gutachten der ersten Runde und dem Supplement zu egusphere-2025-5046; 14 Dateien in `hauptstudie/korpus/testkorpus/`, schreibgeschützt seit 2026-10-16 (Supplement seit 2026-10-17). Prüfsummen je Datei in `hauptstudie/korpusliste.txt` (SHA-256 der Liste 812d012402a5fddca095eacf41f4ffde1a02ee62354d20282bffc6b4274b4c5c), gleich der Übergabe v3 (14 von 14).

| Vorabdruck | Zeitschrift | Seiten | Gutachten |
|---|---|---|---|
| egusphere-2025-4733 | Solid Earth | 33 | RC1, RC2 |
| egusphere-2025-4506 | NHESS | 29 | RC1, RC2, RC3 |
| egusphere-2025-4695 | Earth Surface Dynamics | 37 | RC1, RC2 |
| egusphere-2025-5046 | Climate of the Past | 29 (Supplement 22) | RC1 (PDF), RC2 |

Baumaterial sind LAM, TCD und Fall 3 (egusphere-2025-2248). Aus dem Testmaterial wird bis zum Abschluss der Auswertung keine Skillregel abgeleitet; ein Fehler, der dabei auffällt, wird notiert und erst danach umgesetzt.

## 4. Bedingungen und Wiederholungen (P-8, P-9)

| Bedingung | Fassung | Aufbau |
|---|---|---|
| A | 1.0.0 | sechs getrennte Prüfinstanzen, Vorbereiter, Zusammenführer |
| B | Ausgangsfassung | wie A |
| C | Ausgangsfassung | alle Schritte nacheinander in einem Kontext |
| D | Fassung D | wie A |

Jeder Vergleich ändert genau einen Faktor: A gegen B die Fassung, B gegen C den Aufbau, B gegen D die Regeln zu F1 bis F7. Dass B gegen D nur diese Regeln ändert, zeigt der Dateivergleich der Pakete (`Dateivergleich_D_gegen_B_20261017.md`): Außer den Versionsangaben gehört jede Änderung in Gutachten 1.4.0 und Abbildungen 1.3.0 zu einer Regel zu F1 bis F7. Jede Bedingung läuft auf jedem Manuskript dreimal unabhängig: 4 × 4 × 3 = 48 Gutachten. Die Reihenfolge der Läufe ist gemischt, nicht Bedingung für Bedingung. Modell und Effort sind in allen Läufen gleich: Modell `claude-opus-5-5`, wie für die Sitzung konfiguriert und von jedem Agenten geerbt; Effort "high", in jedem Agentenaufruf ausdrücklich gesetzt und je Lauf im Laufregister vermerkt. Die Vorstudie lief ohne gesetzten Effort; einen Wert gibt die Umgebung nicht aus. Das bedienende Modell kann vom konfigurierten abweichen; es wird je Lauf im Laufregister vermerkt, soweit es feststellbar ist (Regel 7 in Abschnitt 9).

## 5. Ablauf eines Laufs

Wie in Prüfdurchgang 4: ein blinder Vorbereiter (Einlesen, Segmentieren), sechs getrennte Prüfinstanzen (S1 bis S4, AB, SD), ein blinder Zusammenführer; in C ein Agent für alle Schritte. Jeder Agent erhält seinen Auftrag als Datei im eigenen Laufordner, wortgleich mit dem gesicherten Auftrag, und schreibt jede gelesene und geschriebene Datei und jede URL in ein Zugriffsprotokoll. Verboten sind: Verlags- und Diskussionsseiten des Manuskripts, öffentliche Gutachten, Autorenantworten, spätere Fassungen, Sollbefundlisten, andere Laufordner, Veröffentlichen, Netzabrufe aus der Shell, persönliche Daten des Auftraggebers in Abfragen und Dienste, die eine E-Mail-Adresse verlangen (SB-50 bis SB-52).

## 6. Laufregister (P-10)

`hauptstudie/Laufregister.md`, je Lauf eine Zeile, vor dem Start angelegt und nach dem Lauf ergänzt: Kennung, Datum, Studie und Bedingung, Manuskript, Wiederholung, Fassungen, SHA-256 der Pakete, Aufbau, Modell, Effort, Zahl und Art der Agenten, Ordner, SHA-256 von PDF und Gutachten, Verifikation, Gültigkeit mit Grund.

## 7. Sollbefunde, Zuordnung und Einstufung (P-3 bis P-6)

**Sollbefunde (erledigt).** Je Manuskript zog ein Extraktionsagent jeden Einwand der Gutachten als Zeile mit Kennung; drei getrennte Prüfer ohne Kenntnis der Skills urteilten je Kennung am PDF (bestätigt, nicht bestätigt, unklar); Mehrheit zwei von drei per Skript; ohne Mehrheit oder bei Mehrheit "unklar" entschied der Auftraggeber (5 Fälle); ein teilweise zutreffender Einwand zählt als bestätigt mit Vermerk (EP-23, EP-24). Vollständigkeit der Extraktion: Ein zweiter Extraktionsagent zog mit demselben Auftrag unabhängig 207 Einwände; ein dritter Agent glich beide Listen je Manuskript ab (`soll/<M>/extraktion2/`, `soll/<M>/abgleich/`). Ergebnis: 193 gleich, 14 nur anders zugeschnitten (eine Liste teilt, was die andere zusammenfasst), 0 nur in der zweiten, 0 nur in der ersten; es kam kein Einwand hinzu, die Bestätigung blieb unverändert. Ergebnis: 205 Einwände, 198 bestätigt (143 inhaltlich, 55 Kleinkorrekturen), 7 nicht bestätigt. Die Listen sind schreibgeschützt (`hauptstudie/soll/`, Prüfsummen in `soll/sollbefunde_SHA256.txt`, SHA-256 der Prüfsummenliste aee42be83cf8f3a50d5fbca2eddc33b72db874fd4a3fb7286130e56dff2000b2); der Assistent liest sie erst in der Auswertung.

**Zuordnung.** Je Gutachten drei unabhängige Läufe eines Zuordnungsagenten ohne Kenntnis der Skills und ihrer Entstehung und ohne Kenntnis von Bedingung, Fassung und Instanz. Je bestätigtem Sollbefund eine Antwort: getroffen, teilweise, verfehlt oder unklar. Bei getroffen und teilweise nennt die Antwort die Kennung jedes treffenden Befunds (GB oder KK). Trifft ein Befund mehrere Sollbefunde, zählt jeder als getroffen; treffen mehrere Befunde denselben Sollbefund, zählt er einmal. Ein Befund gilt als zutreffend, wenn ihn die Mehrheit der drei Läufe für denselben Sollbefund als getroffen nennt. Mehrheit zwei von drei; ohne Mehrheit oder bei Mehrheit "unklar" entscheidet der Auftraggeber.

**Einstufung (Paper 3, Entscheidung 19).** Befunde, die nach der Zuordnungsregel getroffen haben, gelten als zutreffend. Alle übrigen Befunde, auch "teilweise" zugeordnete und Zusatzbefunde ohne Sollbefund, sind strittig. Sie werden so eingestuft:

1. Befundgruppen: Ein Agent fasst je Manuskript gleiche strittige Befunde (gleicher Fundort und Gegenstand) über alle Wiederholungen und Bedingungen zu Befundgruppen zusammen. Er erhält die Befunde unter zufälligen Kennungen, ohne Bedingung, Fassung, Instanz und Wiederholung. Jeder Einzelbefund gehört zu genau einer Gruppe und übernimmt deren Urteil.
2. Urteil der KI: Ein Agent ohne Kenntnis der Skills, ihrer Entstehung und der Bedingungen stuft jede Befundgruppe am Manuskript ein (zutreffend, nicht zutreffend, Ansichtssache, unklar), in drei unabhängigen Läufen. Maßgeblich ist die Mehrheit von zwei aus drei.
3. Urteil des Auftraggebers: Gruppen ohne Mehrheit oder mit Mehrheit "unklar" stuft der Auftraggeber ein, ohne Kenntnis der Bedingung.
4. Stichprobe: Der Auftraggeber stuft zusätzlich 60 zufällig gezogene Einzelbefunde ein, 15 je Bedingung A bis D (Startwert vor der Ziehung festgelegt und im Laufregister vermerkt). Gezogen wird nur aus Befundgruppen, deren KI-Mehrheit "zutreffend", "nicht zutreffend" oder "Ansichtssache" lautet; Gruppen ohne Mehrheit oder mit Mehrheit "unklar" stuft er nach Punkt 3 ohnehin selbst ein. Er sieht weder die Bedingung noch das Urteil der KI. Verglichen wird sein Urteil mit dem Urteil der zugehörigen Gruppe; die Übereinstimmung wird vor jeder Entscheidung gezählt. Bei Abweichung entscheidet der Auftraggeber, und sein Urteil gilt für die ganze Gruppe.
5. Schwelle: Stimmen mindestens 80 % der Stichprobe überein, gilt das Urteil der Gruppen. Darunter wird die Stichprobe um 60 Einzelbefunde erweitert, wieder 15 je Bedingung, und die Übereinstimmung auf allen 120 berechnet. Bleibt sie unter 80 %, stuft der Auftraggeber alle Gruppen ein.
6. Die Übereinstimmung auf der Stichprobe wird als Kennzahl berichtet (K7).

Aufwand des Auftraggebers, gemessen an einer Probeeinstufung von Fall 3 aus Prüfdurchgang 4 (Baumaterial; 20 von 69 strittigen Einträgen, zufällig gezogen, ohne Fassung, Bedingung und Instanz; `probeeinstufung/`): 38,5 Minuten für 20 Einträge, im Mittel 1,9 Minuten je Eintrag (Median 1,4; Spanne 1,4 bis 4,2), 2,35 je Befund und 1,4 je Kleinkorrektur; dazu 10,5 Minuten Einlesen ins Manuskript, zusammen 49,0 Minuten. Hochrechnung mit 1,9 Minuten je Eintrag und 10,5 Minuten Einlesen je Manuskript: Stichprobe von 60 Einzelbefunden rund 2,6 Stunden, bei Erweiterung auf 120 rund 4,6 Stunden; Gruppen ohne Mehrheit oder mit "unklar" je Gruppe 1,9 Minuten, bei 100 Gruppen rund 3,2 Stunden. Zum Vergleich hätte die Einstufung jedes strittigen Befunds einzeln bei 69 strittigen Einträgen je Gutachten wie in der Probe rund 48 × 69 = 3312 Einstufungen und 107 Stunden erfordert. Die Zahl der Befundgruppen ist vor den Läufen nicht bekannt; die Zahlen sind eine Schätzung aus einem Gutachten. Nach dieser Schätzung bleibt die Einstufung nach Paper 3, Entscheidung 19 (Entscheidung des Auftraggebers vom 2026-10-17).

## 8. Kennzahlen und Zählregeln (P-7)

| Nr. | Kennzahl | Zählregel | Für |
|---|---|---|---|
| K1 | Trefferquote | getroffene bestätigte Sollbefunde je Gutachten an allen bestätigten Sollbefunden des Manuskripts; "getroffen" und "teilweise" getrennt; getrennt für inhaltliche Sollbefunde (143) und Kleinkorrekturen (55). Hauptmaß für RQ1: K1 auf den inhaltlichen Sollbefunden, nur "getroffen" | RQ1, RQ2, RQ3 |
| K2 | Anteil nicht zutreffender Befunde | Befunde mit Einstufung "nicht zutreffend" an allen Befunden | RQ1, RQ2 |
| K3 | Zusatzbefunde | Befunde ohne Sollbefund mit Einstufung "zutreffend" | RQ1, RQ2 |
| K4 | Doppelungen | Paare mit gleichem Fundort und Gegenstand nach der Zusammenführung, aus der unabhängigen Verifikation | Güte |
| K5 | Streuung | Spannweite von K1 über die drei Wiederholungen; Anteil gleicher Schweregrade bei gemeinsamen Befunden | Güte, RQ1 |
| K6 | Anteil aus nur einer Instanz | zutreffende Befunde in B, deren Herkunft nur eine Prüfinstanz nennt, an allen zutreffenden Befunden | RQ2 |
| K7 | Übereinstimmung der Urteilenden | Anteil gleicher Antworten der drei Zuordnungsläufe; Anteil der Befundgruppen mit Mehrheit in den drei Einstufungsläufen der KI; Anteil gleicher Urteile von Auftraggeber und Gruppe auf der Stichprobe (60 oder 120 Einzelbefunde), gesamt und je Bedingung | Güte |
| K8 | Fehlerklassen F1 bis F7 aus RQ3 | Fälle je Klasse und Gutachten nach den Zählregeln in `rq3/Regelvorschlaege_RQ3.md`, aus der unabhängigen Verifikation jedes Gutachtens | RQ3 |
| K9 | Regelvorschläge | Zahl der vorgeschlagenen Regeln; Anteil der vom Auftraggeber bestätigten; Anteil der Fälle aus dem Prüfbericht, die einer Klasse zugeordnet sind; Übereinstimmung zweier unabhängiger Vorschlagsläufe R und R2 mit demselben Auftrag: Zahl der Fälle, die beide sammeln, und Anteil der Fallpaare, die beide gleich gruppieren (in derselben Klasse oder in verschiedenen) | RQ3, erster Teil |

Die Fehlerklassen heißen in allen Dateien unter `rq3/` F1 bis F7; bei der Entscheidung (C-88 bis C-94) hießen sie K1 bis K7, die ursprüngliche Fassung liegt in `rq3/original_K/`. Jedes Gutachten erhält eine unabhängige Verifikation wie in Prüfdurchgang 4 (echt, teilweise echt, falsch, nicht prüfbar; Doppelungen; Fundorte). Alle Kennzahlen werden mit Python gerechnet; das Skript liegt neben dem Ergebnis.

## 9. Auswertungs- und Abbruchregeln

1. Jede Kennzahl wird je Bedingung als Mittelwert und Spannweite über die drei Läufe angegeben.
2. Ein Unterschied zwischen zwei Bedingungen gilt als Effekt, wenn sich ihre Spannweiten nicht überlappen; Signifikanztests entfallen, weil drei Läufe dafür zu wenige sind.
3. "Getroffen" und "teilweise" werden getrennt gezählt.
4. Jede Kennzahl wird mit und ohne die Gutachten mit KI-Herkunft berechnet (Abschnitt 10).
5. Ein Lauf ist ungültig und wird wiederholt bei Zugriff auf eine verbotene Quelle, bei Abbruch durch ein Limit ohne vollständiges Gutachten oder wenn die Formatprüfung nach der Zusammenführung nicht 0 Fehler meldet.
6. Je Lauf höchstens zwei Wiederholungen; danach entscheidet der Auftraggeber.
7. Wechselt das Modell während der Serie, wird die Serie für das betroffene Manuskript in allen Bedingungen wiederholt.
8. Jeder ungültige Lauf steht mit Grund im Laufregister.

## 10. Sonderfall: Gutachten mit KI-Herkunft (Übergabe B-1, EP-19)

Sollbefunde aus Gutachten mit erkennbarer KI-Herkunft werden gekennzeichnet, im Bestätigungslauf wie alle anderen geprüft, und jede Kennzahl wird mit und ohne sie berechnet; im Paper als Grenze genannt. Welche Gutachten das sind, legt die eigene Messung "KI-Herkunft der Gutachten" fest: Kriterienkatalog vor dem Lesen eingefroren, Einstufung durch eine KI in drei Läufen mit Mehrheit und durch den Auftraggeber in zwei Stufen (eigener Eindruck, dann Katalog), bei Abweichung entscheidet der Auftraggeber; abgeschlossen vor der Auswertung.

## 11. Vorstudie (P-11)

Die Durchgänge 1 bis 4 an LAM, TCD und Fall 3 sind Vorstudie und im Laufregister so gekennzeichnet (V1 bis V4). Geänderter Faktor je Übergang und Herkunft jeder Regel der Fassungen 1.1.0, 1.2.0 und der Fassung D: `hauptstudie/Herkunft_der_Regeln_v1_20261017.md`.

## 12. Grenzen, die vorab feststehen

1. Ein Modell einer Modellfamilie erstellt, verifiziert, ordnet zu und stuft ein.
2. Die Vorabdrucke sind 2026 als Artikel erschienen; sie und ihre Gutachten können im Trainingsmaterial enthalten sein (Übergabe B-5).
3. In Websuchen von Prüfern erschienen Seiten zu den Manuskripten in Trefferlisten; nach den Zugriffsprotokollen nicht geöffnet, Kurzvorschauen nicht ausgeschlossen.
4. Drei Wiederholungen je Bedingung erlauben Spannweiten, keine Signifikanztests.
5. Die Regeln der Fassung D stützen sich auf wenige Fälle je Klasse (1 bis 14).
6. Der Auftraggeber ist zugleich Autor der Studie, Einstufer der Stichprobe und der Gruppen ohne Mehrheit und letzte Instanz bei Abweichungen.
7. Gutachten der Bedingung C können an ihrer Form erkennbar sein; das schwächt die Verblindung der Zuordnung und Einstufung für den Vergleich B gegen C.
8. Teilweise zutreffende Einwände der Fremdgutachten zählen als bestätigte Sollbefunde (mit Vermerk); das erhöht die Zahl der Sollbefunde gegenüber einer strengen Bestätigung.
9. Strittige Befunde werden überwiegend von einer KI derselben Modellfamilie eingestuft; der Auftraggeber prüft das an einer Stichprobe, nicht an jedem Befund. Ein Gruppenurteil gilt für jeden Befund der Gruppe, auch wenn sich die Befunde im Wortlaut unterscheiden.

## 13. Nachträge nach dem Einfrieren

| Datum | Änderung | Grund | Entschieden von |
|---|---|---|---|
| | | | |

## Anhang: Umsetzung der Vorgaben aus Paper 3

| Vorgabe | Umsetzung | Abschnitt |
|---|---|---|
| P-1 Bau- und Testmaterial getrennt | LAM, TCD, Fall 3 Baumaterial; vier Vorabdrucke Testmaterial; keine Regelableitung aus dem Testmaterial | 3, 11 |
| P-2 Testmaterial eingefroren | 14 Dateien schreibgeschützt, Prüfsummen gleich Übergabe v3 | 3 |
| P-3 Sollbefunde und Zuordnung durch unabhängigen KI-Prüfer, drei Läufe, Mehrheit | Sollbefunde erledigt; Zuordnung festgelegt | 7 |
| P-4 "unklar" zulässig, ohne Mehrheit an den Auftraggeber | in Bestätigung und Zuordnung | 7 |
| P-5 nur eindeutige Entsprechung zutreffend, übrige strittig | Mehrheit "getroffen" zutreffend, alles übrige strittig | 7 |
| P-6 strittige Befunde durch Auftraggeber und KI, unabhängig, verblindet, Auftraggeber entscheidet | ersetzt durch Paper 3, Entscheidung 19: Befundgruppen, KI in drei Läufen mit Mehrheit, Auftraggeber für Gruppen ohne Mehrheit oder "unklar" und für eine verblindete Stichprobe von 60 Einzelbefunden mit Schwelle 80 % | 7 |
| P-7 getroffen und teilweise getrennt; Übereinstimmungen | K1, K7 | 8 |
| P-8 ein Faktor je Vergleich | A/B Fassung, B/C Aufbau, B/D Regeln | 1, 4 |
| P-9 mindestens drei Wiederholungen | 3 je Bedingung und Manuskript, 48 Gutachten | 4 |
| P-10 Laufregister mit Pflichtangaben | festgelegt | 6 |
| P-11 Vorstudie gekennzeichnet, Herkunft der Regeln | V1 bis V4; Herkunftsliste | 11 |
| P-12 Protokoll vor dem ersten Lauf eingefroren, danach nur Nachträge | dieser Entwurf; Einfrieren nach Prüfung durch Paper 3 | Kopf, 13 |
