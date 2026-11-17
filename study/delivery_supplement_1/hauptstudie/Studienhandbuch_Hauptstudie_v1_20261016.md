# Studienhandbuch: Hauptstudie Paper 3

Arbeitsdokument (DAT-29). Es beschreibt das Studiendesign der Hauptstudie, gibt für jeden Schritt die Anweisung vor und führt den Stand. Es ist das Leitdokument für Block 7 des Workplans: Der Workplan steuert, dieses Handbuch sagt im Einzelnen, was zu tun ist und wo es steht. Das eingefrorene Studienprotokoll (Schritt 4) wird aus diesem Handbuch abgeleitet.

| Feld | Wert |
|---|---|
| Projekt | `science-review-gutachten`, Block 7 (Workplan DAT-01) |
| Auftraggeber | Stefan Mohr |
| Angelegt | 2026-10-16 |
| Letzte Änderung | 2026-10-16 |
| Stand in einem Satz | Schritte 1, 2 und 3a erledigt (Ausgangsfassung Gutachten 1.3.0, Abbildungen 1.2.0, Studiendesign 1.2.0 bestätigt; Testkorpus mit Supplement, 14 Dateien, eingefroren); Schritt 3 erledigt (198 bestätigte Sollbefunde); als Nächstes Schritt 4 (Studienprotokoll), Schritt 3b erledigt (Fassungen für D gebaut); EP-15 und EP-18 entschieden; Spin-off: S1 bis S3 erledigt, S4 beim Auftraggeber; EP-15 und EP-18 offen. |

## Anweisung für jede Sitzung

Wer an der Hauptstudie weiterarbeitet, Mensch oder Assistent, geht so vor:

1. Dieses Handbuch ganz lesen, zuerst die Tabelle "Ablauf und Stand".
2. Den ersten Schritt suchen, der nicht "erledigt" ist. Nur an diesem Schritt arbeiten.
3. Prüfen, ob sein Tor offen ist: Alle Voraussetzungen in der Spalte "Tor" müssen erfüllt sein. Ist eine offen, zuerst sie erledigen oder den Auftraggeber fragen.
4. Den Schritt nach seiner Anweisung ausführen. Keine Abkürzung, auch wenn sie naheliegt.
5. Danach in diesem Handbuch Stand und Datum der Zeile nachtragen, im Log des Projekts einen Eintrag mit Messwert schreiben, neue Erkenntnisse als Befund in den Workplan eintragen.
6. Weicht etwas vom Design ab, wird nicht still angepasst: Die Abweichung kommt in den Abschnitt "Abweichungen und Nachträge", vor dem Einfrieren als Änderung, nach dem Einfrieren als datierter Nachtrag.

## Zweck

Die Hauptstudie misst an Manuskripten, an denen nichts gebaut wurde, ob eine verbesserte Fassung der Skills mehr findet und ob getrennte Prüfinstanzen mehr finden als nacheinander laufende. Die Durchgänge 1 bis 3 (2026-10-15 und 2026-10-16) sind die Vorstudie; sie zeigen, woraus die Regeln entstanden, und gehen getrennt in das Paper.

## Forschungsfragen

| Nr. | Frage | Vergleich |
|---|---|---|
| RQ1 | Wie verändern sich die Befunde der Review-Skills über ihre Fassungen an denselben Manuskripten, gemessen gegen externe Sollbefunde und gegen die Streuung zwischen Läufen derselben Fassung? | Bedingung A gegen B; Streuung aus den Wiederholungen (K5) |
| RQ2 | Finden getrennte Prüfinstanzen getrennte Fehler, und welcher Anteil der zutreffenden Befunde stammt von nur einer Instanz? | Bedingung B gegen C; Anteil aus nur einer Instanz in B (K6) |
| RQ3 | Kann ein Skill aus den Befunden eines Laufs die ihm fehlende Regel selbst vorschlagen, und senkt die bestätigte Regel die betroffene Fehlerklasse im nächsten Lauf? | nach EP-15 |

Wortlaut nach Entscheidung 6 des Projekts Paper 3 (Übergabe vom 2026-10-16, `hauptstudie/uebergabe/`).

## Erwartungen

Vor den Läufen festgelegt (C-95).

| Frage | Erwartung |
|---|---|
| RQ1 | B trifft mehr bestätigte Sollbefunde als A, und der Unterschied ist größer als die Streuung der drei Läufe von B. |
| RQ2 | Getrennte Instanzen (B) treffen mehr als nacheinander (C); mindestens ein Fünftel der zutreffenden Befunde stammt nur von einer Instanz. |
| RQ3 | D zeigt je Gutachten weniger Fälle der Klassen F1 bis F7 als B, ohne weniger Sollbefunde zu treffen. |

## Auswertungs- und Abbruchregeln

Vor den Läufen festgelegt (C-96).

1. Jede Kennzahl wird je Bedingung als Mittelwert und Spannweite über die drei Läufe angegeben.
2. Ein Unterschied zwischen zwei Bedingungen gilt als Effekt, wenn sich ihre Spannweiten nicht überlappen; Signifikanztests entfallen, weil drei Läufe dafür zu wenige sind.
3. "Getroffen" und "teilweise" werden getrennt gezählt.
4. Jede Kennzahl wird mit und ohne die Gutachten mit KI-Herkunft berechnet (EP-19).
5. Ein Lauf ist ungültig und wird wiederholt bei Zugriff auf eine verbotene Quelle, bei Abbruch durch ein Limit ohne vollständiges Gutachten oder wenn die Formatprüfung nach der Zusammenführung nicht 0 Fehler meldet.
6. Je Lauf höchstens zwei Wiederholungen; danach entscheidet der Auftraggeber.
7. Wechselt das Modell während der Serie, wird die Serie für das betroffene Manuskript in allen Bedingungen wiederholt.
8. Jeder ungültige Lauf steht mit Grund im Laufregister.
9. Jede Kennzahl wird vor der Abgabe mit einem zweiten, unabhängig geschriebenen Skript aus den Rohdateien gegengerechnet; eine Abweichung wird behoben und als Befund geführt, bevor die Kennzahl abgegeben wird (Nachtrag 2026-11-15).

## Bedingungen

Jeder Vergleich ändert genau einen Faktor. Bedingung B dient beiden Vergleichen.

| Bedingung | Skillversion | Aufbau | Modell und Effort |
|---|---|---|---|
| A | Fassung 1.0.0 aller drei Skills (EP-18) | getrennte Instanzen | gleich in allen Bedingungen, im Laufregister festgehalten |
| B | eingefrorene Fassung aus Block 6 (Gutachten 1.3.0, Abbildungen 1.2.0, Studiendesign 1.2.0) | getrennte Instanzen | wie A |
| C | wie B | nacheinander in einem Kontext | wie A |
| D | B plus die vom Agenten vorgeschlagenen und vom Auftraggeber bestätigten Regeln F1 bis F7: Gutachten 1.4.0, Abbildungen 1.3.0, Studiendesign 1.2.0 (EP-15) | getrennte Instanzen | wie A |

Jede Bedingung läuft auf jedem Manuskript mindestens dreimal unabhängig. Bei den vier Manuskripten des Testkorpus sind das 4 × 4 × 3 = 48 Gutachten. A gegen B misst RQ1, B gegen C RQ2, B gegen D RQ3.

## Kennzahlen

| Nr. | Kennzahl | Wie gemessen | Für |
|---|---|---|---|
| K1 | Trefferquote | bestätigte Sollbefunde, die ein Gutachten trifft, je Manuskript; "getroffen" und "teilweise" getrennt gezählt und beide berichtet (Schritt 6) | RQ1, RQ2 |
| K2 | Anteil nicht zutreffender Befunde | Befunde, die in Schritt 7 als nicht zutreffend eingestuft sind, an allen Befunden | RQ1, RQ2 |
| K3 | Zusatzbefunde | zutreffende Befunde ohne Sollbefund (Schritt 7) | RQ1, RQ2 |
| K4 | Doppelungen | Paare mit gleichem Fundort und Gegenstand nach der Zusammenführung, unabhängige Verifikation | Güte |
| K5 | Streuung | Spannweite von K1 über die drei Wiederholungen; Anteil gleicher Schweregrade bei gemeinsamen Befunden | Güte |
| K6 | Anteil aus nur einer Instanz | zutreffende Befunde in Bedingung B, deren Herkunft nur eine Prüfinstanz nennt, an allen zutreffenden Befunden | RQ2 |
| K7 | Übereinstimmung der Urteilenden | Anteil gleicher Antworten der drei Zuordnungsläufe (Schritt 6); Anteil gleicher Einstufungen von Auftraggeber und KI vor der Entscheidung (Schritt 7) | Güte |

Schwellen und Auswertungsverfahren legt das Studienprotokoll in Schritt 4 fest, nicht vorher und nicht nachher.

## Rollen

| Rolle | Wer | Darf | Darf nicht |
|---|---|---|---|
| Auftraggeber | Stefan Mohr | wählt Manuskripte, entscheidet Zweifelsfälle und Abweichungen (HITL), stuft verblindet ein | vor seiner Einstufung das Urteil der KI sehen |
| Assistent | Claude im Projektchat | baut Läufe auf, führt Register und Handbuch, wertet aus | die öffentlichen Gutachten des Testkorpus und die Sollbefundlisten vor Schritt 7 lesen; Skillregeln aus dem Testkorpus ableiten |
| Prüfinstanzen | getrennte Agenten | Manuskript, Prüfliste, Befundformat | andere Instanzdateien, Gutachten, Verlags- oder Diskussionsseite |
| KI-Prüfer Sollbefunde | unabhängiger Agent, drei Läufe | öffentliche Gutachten und PDF | Skills, Workplan, Gutachten der Läufe |
| Zuordnungsagent | unabhängiger Agent, drei Läufe | Sollbefundliste und ein Gutachten | Skills, Workplan, Trefferbilanz |
| Einstufungs-KI | unabhängiger Agent | Gutachten, Manuskript | das Urteil des Auftraggebers |
| Projekt Paper 3 | Parallelchat | prüft den Protokollentwurf vor dem Einfrieren, erhält die eingefrorene Fassung | Läufe ausführen |

## Ablauf und Stand

| Nr. | Schritt | Anweisung | Ergebnis | Tor | Stand | Datum |
|---|---|---|---|---|---|---|
| 1 | Laufregister | Datei `hauptstudie/Laufregister.md` anlegen. Je Lauf eine Zeile: Kennung, Datum, Bedingung, Manuskript, Wiederholung, Skillversionen mit SHA-256 der Pakete, Aufbau, konfiguriertes Modell, Effort, Zahl der Agenten, Ordner, SHA-256 der PDF und des Gutachtens. Die 11 Läufe der Vorstudie (Durchgang 1: 4, Durchgang 2: 3, Durchgang 3: 4) aus Log und Trefferbilanz nachtragen; nicht Erfasstes als "nicht festgehalten". | `hauptstudie/Laufregister.md` (DAT-30), Zeilen der Vorstudie per `hauptstudie/tools/laufregister_vorstudie.py` | keines | erledigt | 2026-10-16 |
| 2 | Testmanuskripte | Testkorpus aus der Übergabe von Paper 3 übernehmen (EP-14): vier EGUsphere-Vorabdrucke fremder Autoren aus vier Zeitschriften, jeweils Fassung 1, mit den Gutachten der ersten Runde. ZIP und Übergabe in `hauptstudie/uebergabe/`, ausgepackt nach `hauptstudie/korpus/testkorpus/`, Prüfsummen gegen die Liste und die Tabelle der Übergabe prüfen, schreibgeschützt setzen, `hauptstudie/korpusliste.txt` schreiben. Die Gutachten nicht öffnen. Kein Skill liest das Korpus vor Schritt 5. | eingefrorenes Testkorpus, 13 Dateien | EP-14 entschieden | erledigt | 2026-10-16 |
| 3 | Sollbefundlisten | Je Manuskript zieht ein Extraktionsagent aus den Gutachten in `hauptstudie/korpus/testkorpus/gutachten/` jeden Einwand als Zeile mit Kennung (Herkunft RC1 bis RC3, Art inhaltlich oder Kleinkorrektur, Fundort, Kennzeichen Supplement). Drei getrennte Prüfer urteilen je Kennung am PDF: bestätigt, nicht bestätigt oder unklar. Bestätigt ist ein Sollbefund bei zwei von drei; ohne Mehrheit oder bei Mehrheit "unklar" entscheidet der Auftraggeber (`hitl.md`). Mehrheit per `soll/mehrheit_schritt3.py`, das dem Assistenten nur Zählungen ausgibt (EP-23). Einwände aus Gutachten mit erkennbarer KI-Herkunft werden nach EP-19 über ihre Herkunft gekennzeichnet. Die Listen liegen in `hauptstudie/soll/`; der Assistent liest sie erst in Schritt 7. | Sollbefundlisten mit Urteil je Lauf | Schritt 2 erledigt; EP-19 und EP-20 entschieden (2026-10-16); Supplements zu egusphere-2025-5046 (und zu -4733, falls vorhanden) eingefroren | erledigt: 205 Einwände, 198 bestätigt (143 inhaltlich, 55 Kleinkorrektur), 7 nicht bestätigt; 5 Fälle vom Auftraggeber entschieden; `soll/<M>/sollbefunde.md` schreibgeschützt, Prüfsummen in `soll/sollbefunde_SHA256.txt` | 2026-10-17 |
| 3a | Prüfdurchgang 4 (EP-22) | Die aktuellen Fassungen (Gutachten 1.3.0, Abbildungen 1.2.0, Studiendesign 1.2.0) wie Durchgang 3 auf LAM (zweifach), TCD und HOR laufen lassen, unabhängig verifizieren, mit AK-01 bis AK-14 abnehmen. Arbeitsdateien jedes Agenten nur im eigenen Laufordner, jede geschriebene Datei im Zugriffsprotokoll (SB-33, SB-50). Läufe ins Laufregister als Vorstudie D4 | Gutachten, Verifikationen, Trefferbilanz gegen D3 | Ausgangsfassung von Schritt 4 nur, wenn alle Abnahmekriterien erfüllt sind | erledigt; alle Abnahmekriterien erfüllt, Ausgangsfassung bestätigt | 2026-10-17 |
| 3b | Regelvorschlag für RQ3 (EP-15 A) | Ein eigener Agent erhält nur die Verifikationsberichte von Durchgang 4 (`erprobung/verifikation4/`), dazu die Prüflisten der Skills, keine Sollbefunde und keine Gutachten des Testkorpus; er nennt je Fehler die Fehlerklasse und schlägt je Klasse eine Regel mit Wortlaut vor. Der Auftraggeber bestätigt oder verwirft je Regel. Die bestätigten Regeln werden als Fassung 1.4.0 geschrieben (Paket, Tests, Korpusscan). Je Regel wird die Fehlerklasse festgelegt, die in Schritt 7 gezählt wird | Regelvorschläge, Entscheidungen, Paket 1.4.0 | Schritt 3a erledigt; vor Schritt 4 | erledigt: 7 Regeln F1 bis F7 bestätigt; Gutachten 1.4.0 (SHA-256 66dcd7c60f8a), Abbildungen 1.3.0 (ce3468d00215) | 2026-10-17 |
| 4 | Studienprotokoll | Aus diesem Handbuch das Protokoll schreiben: Fragen, Bedingungen, Manuskripte, Kennzahlen mit Schwellen, Zahl der Wiederholungen, Verfahren der Schritte 3, 6 und 7, Versionen mit SHA-256. Der Auftraggeber bringt den Entwurf in das Projekt Paper 3; dessen Rückmeldungen werden eingearbeitet. Dann mit Datum und SHA-256 einfrieren und die eingefrorene Fassung an Paper 3 geben. | `hauptstudie/Studienprotokoll_<Datum>.md`, eingefroren | Schritte 1 und 2 erledigt; EP-15 und EP-18 entschieden; Vorgaben P-1 bis P-12 abgehakt; Prüfung durch Paper 3 | offen | |
| 5 | Läufe | Je Bedingung, Manuskript und Wiederholung ein Lauf in eigenem Ordner unter `hauptstudie/laeufe/`, mit Zugriffsprotokoll je Agent und Hilfsdateien nur im eigenen Unterordner. Reihenfolge der Läufe gemischt, nicht Bedingung für Bedingung. Modell und Effort werden im Aufruf jedes Agenten ausdrücklich gesetzt, mit den Werten aus dem Studienprotokoll, und vor dem Start ins Laufregister eingetragen. Nach jedem Durchgang: Zugriffsprotokolle prüfen, Laufregister nachtragen, ZIP-Export. | 36 Gutachten | Schritte 3 und 4 erledigt | offen | |
| 6 | Zuordnung | Je Gutachten drei unabhängige Läufe eines Zuordnungsagenten. Je Sollbefund eine Antwort: getroffen, teilweise, verfehlt oder unklar. Mehrheit entscheidet; ohne Mehrheit oder bei Mehrheit "unklar" entscheidet der Auftraggeber. Übereinstimmung der drei Läufe als Anteil festhalten. Dasselbe Verfahren für die Vorstudie. | Zuordnungstabellen, Liste der HITL-Entscheidungen | Schritt 5 erledigt | offen | |
| 7 | Einstufung und Auswertung | Befunde mit Mehrheit "getroffen" gelten als zutreffend. Alle übrigen, auch "teilweise" und Zusatzbefunde, sind strittig und werden nach Paper 3, Entscheidung 19 eingestuft (Studienprotokoll Abschnitt 7): Befundgruppen je Manuskript, KI in drei Läufen mit Mehrheit, Auftraggeber für Gruppen ohne Mehrheit oder "unklar", verblindete Stichprobe von 60 Einzelbefunden (15 je Bedingung) mit Schwelle 80 %. Danach K1 bis K9 je Bedingung berechnen, mit und ohne Sollbefunde aus Gutachten mit erkennbarer KI-Herkunft, mit Python, und Vorstudie und Hauptstudie getrennt berichten. | Einstufungstabelle, Trefferbilanz Hauptstudie | Schritt 6 erledigt | offen | |

## Spin-off: KI-Herkunft der Gutachten

Eine kleine eigene Messung innerhalb von Paper 3 (EP-21): Erkennen eine KI und der Auftraggeber übereinstimmend, welche der neun Gutachten des Testkorpus Spuren der Formulierung durch ein Sprachmodell tragen? Anlass ist RC3 zu egusphere-2025-4506 (Übergabe B-1). Ordner `hauptstudie/spinoff_ki_herkunft/`.

| Nr. | Schritt | Anweisung | Ergebnis | Tor | Stand | Datum |
|---|---|---|---|---|---|---|
| S1 | Kriterienkatalog | Kriterien ohne Kenntnis der Gutachten schreiben, mit Urteilen (eindeutig, Hinweise, keine Hinweise, unklar) und Stufen A (eindeutige Marker), B (starke Hinweise), C (schwache Signale); einfrieren, Prüfsumme ins Log | `Kriterienkatalog_KI_Herkunft_v1_20261016.md`, schreibgeschützt | keines | erledigt | 2026-10-16 |
| S2 | Auftraggeber, Stufe 1 | Der Auftraggeber stuft jedes Gutachten nach eigenem Eindruck ein, bevor er den Katalog öffnet, im Formular `Formular_Auftraggeber_Stufe1.md` | ausgefülltes Formular | S1 erledigt | erledigt; `Stufe1_Auftraggeber_ausgefuellt_20261017.md`, schreibgeschützt | 2026-10-17 |
| S3 | KI-Einstufung | Drei unabhängige Läufe eines eigenen Agenten. Er erhält nur den Katalog, die neun Gutachten und die vier Vorabdrucke (für B1), keinen Hinweis auf B-1 oder auf ein bestimmtes Gutachten, keine Skills, Sollbefundlisten, Läufe oder Diskussionsseiten. Je Lauf zwei Dateien: Urteile mit Kriteriennummern ohne Zitate (`ki_lauf<n>_urteile.md`) und Belege mit Zitaten (`ki_lauf<n>_belege.md`). Mehrheit zwei von drei; ohne Mehrheit oder bei Mehrheit "unklar" bleibt das KI-Urteil "unklar" | 6 Dateien | S1 erledigt | erledigt; Ergebnis in `ki_mehrheit.md`, für den Auftraggeber gesperrt bis nach S4 | 2026-10-16 |
| S4 | Auftraggeber, Stufe 2 | Der Auftraggeber stuft nach dem Katalog ein, ohne die Urteile der KI zu kennen, im Formular `Formular_Auftraggeber_Stufe2.md` | ausgefülltes Formular | S2 erledigt | erledigt 2026-10-17 (L-85) | |
| S5 | Auswertung | Mit Python: Übereinstimmung der drei KI-Läufe; KI-Mehrheit gegen Stufe 1 und gegen Stufe 2; Stufe 1 gegen Stufe 2; Treffer je Kriterium. Weichen KI und Stufe 2 ab, entscheidet der Auftraggeber das Urteil, mit dem die Sollbefunde nach EP-19 gekennzeichnet werden | `auswertung_ki_herkunft.md`, Skript daneben | S3 und S4 erledigt; vor Schritt 7 der Hauptstudie | erledigt 2026-10-17: Stufe 2 gegen KI 9 von 9, Stufe 1 gegen KI 7 von 9; Kennzeichnung G03 durch den Auftraggeber (`spinoff_ki_herkunft/Kennzeichnung_KI_Herkunft_20261017.md`, `auswertung_S5.py`; L-86) | |

Blindheit: Der Assistent liest nur die Urteilsdateien und die Formulare, nicht die Belegdateien und nicht die Gutachten; die Belege werden erst in Schritt 7 geöffnet. Der KI-Agent kennt das Urteil des Auftraggebers nicht, der Auftraggeber in Stufe 2 nicht das der KI.

Grenzen für das Paper: Es läuft nur ein Modell der Familie Claude; die Aussage lautet "eine KI erkennt KI-Herkunft in Gutachten", nicht "ein Modell erkennt seinen eigenen Text", denn von welchem Modell ein Gutachten stammt, ist unbekannt. Der Auftraggeber hat die Gutachten selbst von den Diskussionsseiten kopiert; sein Urteil ist nur gegenüber dem der KI blind. Der Katalog ist für RC3 nicht blind, weil dessen Einleitungssatz bekannt war (siehe Katalog). Neun Gutachten sind eine kleine Zahl; die Messung beschreibt, sie schätzt keine Häufigkeit.

## Feste Regeln

1. **Blind.** Keine Prüfinstanz, kein Zusammenführer und kein Zuordnungsagent sieht Sollbefundlisten, öffentliche Gutachten oder die Verlags- und Diskussionsseite des Manuskripts. Jeder Agent schreibt jeden gelesenen Pfad und jede URL in sein Zugriffsprotokoll.
2. **Kein Bauen am Testkorpus.** Aus den Manuskripten der Hauptstudie wird keine Skillregel abgeleitet, bis Schritt 7 abgeschlossen ist. Ein Fehler, der dabei auffällt, wird als Befund im Workplan notiert und erst danach umgesetzt.
3. **Eingefroren heißt eingefroren.** Skillversionen, Korpus und Protokoll ändern sich nach dem Einfrieren nicht. Was sich doch ändern muss, kommt als datierter Nachtrag unter "Abweichungen und Nachträge".
4. **Ein Faktor je Vergleich.** Modell und Effort sind in allen Bedingungen gleich und stehen im Laufregister.
5. **Der Auftraggeber entscheidet Zweifelsfälle.** Ohne Mehrheit, bei "unklar" und bei abweichender Einstufung entscheidet er, ausnahmslos.
6. **Alles liegt im Projekt.** Gutachten, Instanzdateien, Zugriffsprotokolle und Prüferberichte werden nach jedem Durchgang aus dem Scratchpad nach `hauptstudie/` übernommen, mit `diff -rq` geprüft und exportiert.
7. **Zahlen per Skript.** Jede Kennzahl wird mit Python gerechnet, und das Skript liegt neben dem Ergebnis.
8. **Bau- und Testmaterial getrennt.** LAM, TCD und Fall 3 (egusphere-2025-2248) sind Baumaterial, die vier Vorabdrucke sind Testmaterial (P-1). Der Assistent öffnet die Gutachten des Testkorpus nicht; nur der KI-Prüfer in Schritt 3 liest sie.

## Offene Entscheidungen

| Nr. | Frage | Vorschlag | Stand |
|---|---|---|---|
| EP-14 | Wie viele Testmanuskripte, welche? | entschieden 2026-10-16: die vier Vorabdrucke der Übergabe von Paper 3 (egusphere-2025-4733, -4506, -4695, -5046); Fall 3 bleibt Baumaterial | entschieden |
| EP-15 | Wie wird RQ3 gemessen? | Ein Agent erhält nur den Verifikationsbericht eines Laufs und schlägt Regeln vor; Vergleich mit den Regeln des Assistenten, Test an den neuen Manuskripten. Offen: Rückschreibschritt im Skill oder eigener Skill; welche Kennzahl als Verbesserung gilt | entschieden 2026-10-17: A, Vorschlag am Baumaterial, Test am Testkorpus als Bedingung D (Schritt 3b) |
| EP-18 | Welche frühere Fassung ist Bedingung A? | 1.0.0 (Stand vor allen Rückschreibungen); Alternative 1.1.0, dann misst RQ1 nur den Schritt aus dem Konsistenzlauf | entschieden 2026-10-17: 1.0.0 aller drei Skills |
| EP-19 | Wie werden Gutachten mit erkennbarer KI-Herkunft behandelt (B-1: RC3 zu egusphere-2025-4506)? | Sollbefunde daraus kennzeichnen, im Bestätigungslauf wie alle anderen prüfen, Kennzahlen mit und ohne sie berechnen, im Paper als Grenze nennen | entschieden 2026-10-16 wie vorgeschlagen; das Gutachten dient zugleich als Beispiel für KI-Einsatz bei Gutachten |
| EP-20 | Was geschieht mit Einwänden, die nur am Supplement prüfbar sind (B-2: egusphere-2025-5046; B-3: Supplement zu egusphere-2025-4733 ungeprüft)? | A: Supplements beschaffen (der Auftraggeber lädt sie herunter), vor Schritt 3 einfrieren und den Prüfinstanzen mitgeben. B: diese Sollbefunde als "nicht prüfbar" führen und aus K1 herausnehmen | entschieden 2026-10-16: A, Supplements beschaffen. Nachtrag Paper 3: Supplement zu egusphere-2025-5046 nachgereicht (Testkorpus 14 Dateien; übernommen und eingefroren 2026-10-17, Übergabe v3, 14 von 14 Prüfsummen gleich); zu egusphere-2025-4733 kein Supplement, Zenodo-Rohdatensatz nicht Testmaterial |
| EP-22 | Welche Fassung ist die Ausgangsfassung der Hauptstudie (Bedingung B)? Zwischen 1.1.0 (Durchgang 3) und heute liegen Gutachten 1.2.0 und 1.3.0, Abbildungen und Studiendesign 1.2.0 ohne eigenen Durchgang | A: die aktuellen Fassungen nach einem Prüfdurchgang 4 am Baumaterial mit AK-01 bis AK-14. B: 1.1.0 aller drei. C: die aktuellen ohne Durchgang, als Grenze offengelegt | entschieden 2026-10-16: A, Prüfdurchgang 4 am Baumaterial vor dem Einfrieren |
| EP-24 | Wie zählt ein vom Auftraggeber als teilweise zutreffend beurteilter Einwand? | bestätigt, mit Vermerk "teilweise" | entschieden 2026-10-17: A |

## Vorgaben aus Paper 3

Die Übergabe nennt zwölf Vorgaben, die das Studienprotokoll erfüllen muss. Vor dem Einfrieren (Schritt 4) wird jede hier abgehakt.

| Nr. | Vorgabe | Wo im Handbuch | Erfüllt |
|---|---|---|---|
| P-1 | Bau- und Testmaterial getrennt | Feste Regeln 2 und 8 | |
| P-2 | Testmaterial vor dem ersten Lauf mit Prüfsummen eingefroren | Schritt 2 | ja, 2026-10-16 |
| P-3 | Bestätigung und Zuordnung durch unabhängigen KI-Prüfer, drei Läufe, Mehrheit | Schritte 3 und 6 | |
| P-4 | Antwort "unklar"; ohne Mehrheit entscheidet der Auftraggeber | Schritte 3 und 6, Feste Regel 5 | |
| P-5 | Eindeutige Entsprechung gilt als zutreffend, alles andere strittig | Schritt 7 | |
| P-6 | Strittige Befunde verblindet von Auftraggeber und KI eingestuft, ohne Kenntnis der Herkunft | Schritt 7 | |
| P-7 | "getroffen" und "teilweise" getrennt; Übereinstimmungen gemessen | K1, K7 | |
| P-8 | Ein Faktor je Vergleich | Bedingungen, Feste Regel 4 | |
| P-9 | Mindestens drei Wiederholungen | Bedingungen | |
| P-10 | Laufregister mit allen Feldern | Schritt 1 | ja, 2026-10-16 |
| P-11 | Vorstudie gekennzeichnet, Herkunft jeder Regel aus 1.1.0 | Laufregister; Herkunftsliste noch offen (Workplan SB-40) | |
| P-12 | Protokoll vor dem ersten Lauf mit Prüfsumme eingefroren | Schritt 4, Feste Regel 3 | |

Grenzen, die das Protokoll nennen muss: Gutachten mit erkennbarer KI-Herkunft (B-1), fehlende Supplements (B-2, B-3), mögliche Kenntnis der veröffentlichten Artikel und Gutachten aus dem Trainingsmaterial des Modells (B-5). Optional nach der Hauptstudie: welche Einwände die Autoren in den Endfassungen angenommen haben (B-6).

## Abweichungen und Nachträge

| Datum | Was | Warum | Entschieden von |
|---|---|---|---|
| 2026-10-16 | Spin-off S3: Die Agenten erhalten den Katalog ohne seinen Herkunftsabsatz (`agent_eingabe/Kriterienkatalog_Agentenfassung.md`, SHA-256 29ee62aa068b…). Gegenüber dem eingefrorenen Katalog fehlen genau dieser Absatz und eine Leerzeile; Kriterien, Urteile und Vorgehen sind wortgleich. | Der Herkunftsabsatz nennt RC3 zu egusphere-2025-4506; S3 verbietet jeden Hinweis auf ein bestimmtes Gutachten. Der eingefrorene Katalog bleibt unverändert. | Assistent nach S3; Auftraggeber informiert |
| 2026-11-15 | Auswertungsregel 9 nachgetragen: Gegenrechnung jeder Kennzahl mit einem zweiten, unabhängigen Skript | Die Gegenrechnung in 7.8 fand einen Fehler in K6 (SB-71); die Regel beschreibt das dort angewandte Vorgehen | Auftraggeber (C-182) |

## Verlauf

| Datum | Änderung |
|---|---|
| 2026-10-16 | Handbuch angelegt aus Block 7 des Workplans (C-47 bis C-50) und dem Kurzplan vom 2026-10-16 (C-58); Bedingung B dient beiden Vergleichen, daher 27 statt 36 Gutachten bei drei Manuskripten; EP-18 neu. |
| 2026-10-16 | Schritt 1 erledigt: Laufregister mit 11 Läufen der Vorstudie (C-60, L-43); Schritt 5 um die Regel ergänzt, Modell und Effort im Agentenaufruf ausdrücklich zu setzen, weil sie in der Vorstudie nicht festgehalten wurden. |
| 2026-10-16 | Übergabe von Paper 3 aufgenommen (C-61): Forschungsfragen nach Entscheidung 6, EP-14 entschieden, Schritt 2 erledigt (13 Dateien, Prüfsummen 13 von 13), 36 statt 27 Gutachten, K6 und K7 neu, Feste Regel 8, EP-19 und EP-20 neu, Abschnitt "Vorgaben aus Paper 3". |
| 2026-10-16 | EP-19 und EP-20 wie vorgeschlagen entschieden (C-62). |
| 2026-10-16 | Spin-off KI-Herkunft angelegt (EP-21, C-63, C-64, C-65): Schritte S1 bis S5, S1 erledigt (Kriterienkatalog eingefroren), Formulare für Stufe 1 und 2. |
| 2026-10-16 | Nachträge Paper 3 (C-68): EP-20 ergänzt (Supplement 5046 nachgereicht, 4733 ohne Supplement), EP-22 neu (Ausgangsfassung). |
| 2026-10-16 | EP-22 entschieden: A (C-69); Schritt 3a Prüfdurchgang 4 neu. |
| 2026-10-17 | Schritt 3a erledigt: Prüfdurchgang 4 erfüllt alle Abnahmekriterien (Trefferbilanz, L-56). |
| 2026-10-17 | Nachtrag zu Schritt 2: Supplement zu egusphere-2025-5046 aus der Übergabe v3 in das eingefrorene Testkorpus aufgenommen (14 Dateien, Korpusliste 14 Zeilen, L-59). Die Prüfinstanzen von Schritt 3 und 5 erhalten es zum Manuskript egusphere-2025-5046 (EP-20 A). |
| 2026-10-17 | EP-23 entschieden: A (C-75); Schritt 3 mit Extraktion und drei getrennten Urteilen neu gefasst. |
| 2026-10-17 | EP-24 entschieden: A (C-78); zwei der fünf Fälle zu 5046 entschieden (bestätigt, teilweise). |
| 2026-10-17 | EP-18 entschieden: Bedingung A ist 1.0.0 (C-82). EP-15 entschieden: A (C-83); Bedingung D und Schritt 3b neu, 48 statt 36 Gutachten. |
| 2026-10-17 | Schritt 3b erledigt: K1 bis K7 bestätigt (C-88 bis C-94); Gutachten 1.4.0, Abbildungen 1.3.0 gebaut, nicht installiert; jede Bedingung liest ihren Skill aus dem entpackten Paket ihrer Fassung. |
| 2026-11-15 | Auswertungsregel 9 (Gegenrechnung) nachgetragen, Abweichungen und Nachträge ergänzt (SB-71, C-182). |
