# Herkunft der Regeln je Fassung (P-11)

Arbeitsdokument zum Studienprotokoll. Je Regel, die eine Fassung gegenüber der vorigen hinzufügt, stehen Anlass, Durchgang und Material. Alle Anlässe stammen aus dem Baumaterial (LAM, TCD, Fall 3 HOR = egusphere-2025-2248) oder aus Konsistenzprüfungen der Skills selbst; keine Regel stammt aus dem Testkorpus der Hauptstudie.

## Vorstudie: Durchgänge und geänderter Faktor

| Durchgang | Fassung | Aufbau | geänderter Faktor gegenüber dem vorigen | Läufe |
|---|---|---|---|---|
| D1 | 1.0.0 | nacheinander in einem Kontext | Ausgangspunkt | V1-LAM-1, V1-LAM-2, V1-TCD-1, V1-HOR-1 |
| D2 | 1.0.0 | getrennte Instanzen | Aufbau (EP-13 A) | V2-LAM-1, V2-TCD-1, V2-HOR-1 |
| D3 | 1.1.0 | getrennte Instanzen | Fassung | V3-LAM-1, V3-LAM-2, V3-TCD-1, V3-HOR-1 |
| D4 | Gutachten 1.3.0, Abbildungen 1.2.0, Studiendesign 1.2.0 | getrennte Instanzen | Fassung (Abnahme der Ausgangsfassung, EP-22) | V4-LAM-1, V4-LAM-2, V4-TCD-1, V4-HOR-1 |

## Übergang D3 zu D4 im Einzelnen

| Faktor | D3 | D4 | geändert |
|---|---|---|---|
| Fassung science-review-gutachten | 1.1.0 | 1.3.0 (über 1.2.0) | ja: 1.2.0 Zeilenzählung in `einlesen.py` (SB-32) und Arbeitsdateien nur im Ordner der Instanz (SB-33); 1.3.0 Befunde K-01 bis K-29 des Konsistenzberichts |
| Fassung science-review-abbildungen | 1.1.0 | 1.2.0 | ja: Befunde K-01 bis K-29 |
| Fassung science-review-studiendesign | 1.1.0 | 1.2.0 | ja: Befunde K-01 bis K-29 |
| Aufbau | Vorbereiter, sechs getrennte Instanzen, Zusammenführer, Verifikation | gleich | nein |
| Material | LAM zweifach, TCD, Fall 3 | gleich | nein |
| Modell | Sitzung für `claude-opus-5-5` konfiguriert, Agenten erben | gleich | nein |
| Aufträge der Agenten | Fassung D3 | je ein Satz ergänzt | gering: in 28 Aufträgen von Vorbereiter und Instanzen und in den 4 Aufträgen des Zusammenführers nur der Satz "Eigene Hilfsdateien nur im Unterordner ..." (Regel von SB-33); in den 4 Aufträgen der Verifikation nur der Satz zur Zugriffsdatei; sonst wortgleich (Vergleich `hauptstudie/d4/auftraege_d3/` gegen `auftraege_d4/`, 36 von 36) |

Der Übergang ändert damit im Kern einen Faktor, die Fassung der drei Skills; die Ergänzungen der Aufträge betreffen nur Ablage und Protokoll der Arbeitsdateien, nicht die Prüfung.

## Fassung 1.1.0 (gegenüber 1.0.0), gebaut 2026-10-15 nach D1 und D2 (L-19)

| Nr. | Regel in 1.1.0 | Ort | Anlass | Durchgang, Material |
|---|---|---|---|---|
| 1 | Verlags- und Diskussionsseite, öffentliche Gutachten und spätere Fassungen des Manuskripts werden nicht geöffnet | `science-review-gutachten`, SKILL.md, Grundregel 1 | SB-21: eine Websuche lieferte die Verlagsseite des eigenen Manuskripts | D1, TCD |
| 2 | Jeder Fundort wird an der gedruckten Randnummer bestätigt; `text.json` kann verschoben sein | SKILL.md, Grundregel 4 | SB-24: Fundorte nur 19 von 31 genau | D1, LAM |
| 3 | Die Prüfinstanzen startet die Sitzung als getrennte Agenten | SKILL.md, Abschnitt 3 | SB-20: Instanzen liefen nacheinander im selben Kontext; SB-29: getrennt höhere Trefferquote | D1, alle; D2 |
| 4 | Doppelungen auch zwischen Befund und Kleinkorrektur auflösen | SKILL.md, Zusammenführung Regel 2 | SB-23: drei Paare Befund und Kleinkorrektur zur selben Stelle | D1, HOR |
| 5 | Widersprüche zwischen Instanzen am Manuskript klären | SKILL.md, Zusammenführung Regel 3 | SB-30: Paare mit gleichem Fundort nicht zusammengeführt, Widerspruch KK und GB | D2, HOR und TCD |
| 6 | Wortlaut jedes Zitats und jeder Angabe im Einwand nachprüfen | SKILL.md, Zusammenführung Regel 5 (neu) | SB-25: überzogene Nebensätze, ungenaue Einbettungen | D1, alle |
| 7 | vier weitere typische Fehler | SKILL.md, Typische Fehler | SB-22: fünf Muster der verfehlten Sollbefunde | D1, LAM und TCD |
| 8 | Abgrenzung zu `science-abbildungen` | SKILL.md, Verhältnis zu anderen Skills; `science-review-abbildungen` | SB-18: namensnaher Skill ohne Abgrenzung | Installation 2026-10-15 |
| 9 | Gegenprobe für den Schweregrad wesentlich | `references/befundformat.md`, Schweregrade | SB-26: Einstufung LAM-1 gegen LAM-2 76,5 %, alle Abweichungen an der Grenze wesentlich zu mittel | D1, LAM |
| 10 | Formulierungsregel 12 "Kern und Nebensatz" | befundformat.md, Formulierung | SB-25 | D1, alle |
| 11 | Literaturabgleich jedes Vorschlags mit dem Verzeichnis | befundformat.md, Zusatzregel 4 | AK-07 und SB-22: Vorschläge von Arbeiten, die schon zitiert sind | D1 |
| 12 | P15 Schritte 4 und 5 | `references/segment-4.md` | SB-22, Muster 2 und 5; SB-29 | D1 und D2, LAM und TCD |
| 13 | `formatpruefung.py --paare` | scripts | SB-23, SB-30; Länge der Liste SB-31 | D1 und D2, HOR |
| 14 | `einlesen.py`: Tabellenzeilen ohne Randnummer und Anschluss an die Vorseite | scripts | SB-24, SB-28 | D1 und D2, LAM und TCD |

## Fassung 1.2.0 (gegenüber 1.1.0), gebaut 2026-10-16 nach D3

| Nr. | Regel | Ort | Anlass | Durchgang, Material |
|---|---|---|---|---|
| 1 | Zeilenzählung an Seitenzahl, freistehender Randnummer, Seitenende und Tabellenkopf | `einlesen.py`, Tests je Stellenart | SB-32 | D3, LAM, TCD, HOR |
| 2 | Arbeitsdateien nur im Arbeitsordner der Instanz | SKILL.md, Grundregel | SB-33: Kollision paralleler Instanzen | D3 |

Abbildungen 1.2.0 und Studiendesign 1.2.0 sowie Gutachten 1.3.0 setzen die 29 Befunde des Konsistenzberichts um (K-01 bis K-29, `konsistenz/Umsetzung_Konsistenzbericht_20261016.md`); Anlass ist die Prüfung der Skills gegeneinander, nicht ein Manuskript.

## Fassung für Bedingung D: Gutachten 1.4.0, Abbildungen 1.3.0 (gegenüber der Ausgangsfassung)

Regeln zu den Fehlerklassen F1 bis F7 (bei der Entscheidung K1 bis K7), vorgeschlagen von einem eigenen Agenten aus den Verifikationsberichten von D4 (Baumaterial), bestätigt vom Auftraggeber (`rq3/Regelvorschlaege_RQ3.md`, `rq3/Entscheidungen_RQ3.md`, L-67, L-68).
