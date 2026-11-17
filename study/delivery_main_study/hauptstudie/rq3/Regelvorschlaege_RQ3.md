# Regelvorschläge RQ3

Kennungen der Fehlerklassen am 2026-10-17 von K1 bis K7 in F1 bis F7 umbenannt (Prüfvermerk Paper 3, PV-01 und PV-14), weil K1 bis K7 im Studienprotokoll Kennzahlen sind; sonst unverändert. Ursprüngliche Fassung: `original_K/` mit Prüfsummen.

Grundlage: die vier Prüfberichte aus `erprobung/verifikation4/` (LAM_A, LAM_B, TCD, HOR), die zugehörigen Gutachten aus `erprobung/durchgang4/` zum Nachlesen der beanstandeten Befunde, die installierten Skills `science-review-gutachten` (1.3.0), `science-review-abbildungen` (1.2.0) und `science-review-studiendesign` (1.2.0). Gesammelt wurden nach Schritt 1 des Auftrags alle Kennungen mit einem anderen Urteil als "echt", alle Fundortabweichungen (auch die als "ohne Einfluss auf die Zählung" vermerkten), alle genannten Doppelungen und Überschneidungen und alle Literaturvorschläge, die schon im Verzeichnis stehen. Ob zwei überlappende Kennungen aufeinander verweisen, wurde im Gutachten per Skript geprüft (Suche der jeweils anderen Kennung im Befundblock).

## Fälle

| Nr. | Lauf | Kennung | Urteil im Prüfbericht | Grund (ein Satz) | Klasse |
|---|---|---|---|---|---|
| 1 | LAM_A | GB-09 | teilweise echt | Die Zählung "11 times, never with a stage" stammt aus text.json und schließt Tabellenzeilen ein, die den Zusatz gerade enthalten; im Fließtext sind es 8 Treffer. | F3 |
| 2 | TCD | GB-15 | teilweise echt | Das Gutachten zählt 2 orange, 1 schwarzen und 4 graue Pfeile, gemessen sind 5 graue, also 8 statt 7 Pfeile. | F3 |
| 3 | LAM_B | GB-07 | teilweise echt | Der Titelteil, der Schluss nehme keinen Kernbegriff von RQ2 oder RQ3 auf, ist widerlegt, weil der Schluss beide Kernbegriffe in anderer Wortform nennt. | F4 |
| 4 | HOR | KK-28 | teilweise echt | Der Ersatz behauptet dieselbe Namensform an zwei Stellen, an der zweiten fehlt aber ein diakritisches Zeichen. | F4 |
| 5 | LAM_B | GB-28 | teilweise echt | Ein Prüfdatum, das das Manuskript nur für einen Pfad nennt, wurde auf einen zweiten Pfad übertragen, und die Zählung "4 von 7" hängt davon ab. | F5 |
| 6 | LAM_B | GB-40 | teilweise echt | Der Beleg für "nicht gemessen" betrifft die nicht erfasste Bauzeit, nicht die Sitzungsdauer, um die es im Befund geht. | F5 |
| 7 | LAM_B | GB-42 | nicht prüfbar (Quellteil) | Definitionen mit Seiten- und Tabellenangabe aus einer Quelle sind als verifiziert ausgewiesen, der Prüfer konnte nur den Abstract lesen, der Volltext war nicht abrufbar. | F6 |
| 8 | LAM_A | GB-33 | echt, Fundort: Seitenangabe einer Nebenstelle falsch | Der Zeilenbereich ist mit S. 4 angegeben, seine ersten Zeilen stehen noch auf S. 3. | F1 |
| 9 | LAM_A | GB-42 | echt, Fundort: Seitenangabe einer Nebenstelle falsch | Der Zeilenbereich ist mit S. 8 angegeben, seine erste Zeile steht noch auf S. 7. | F1 |
| 10 | LAM_B | GB-03 | echt, Fundort: Seitenangabe einer Nebenstelle falsch | Zwei Zeilen sind mit p. 21 angegeben, sie stehen auf p. 20. | F1 |
| 11 | TCD | GB-53 | echt, Fundort-Anmerkung | Der Bereich ist als "p. 6 to 7" angegeben, alle Zeilen stehen auf S. 6. | F1 |
| 12 | LAM_A | GB-21 | echt, Fundort 1 bis 2 Zeilen daneben | Die Nebenstelle ist um eine Zeile verschoben und folgt der Verschiebung in text.json auf dieser Seite. | F2 |
| 13 | LAM_A | GB-41 | echt, Fundort 1 bis 2 Zeilen daneben | Das Ende des Zeilenbereichs ist um eine Zeile zu früh angegeben, ebenfalls nach der Verschiebung in text.json. | F2 |
| 14 | LAM_B | GB-26 | echt, Fundort 1 bis 2 Zeilen daneben | Eine Abstractstelle auf S. 1 ist mit Z. 7 statt Z. 8 angegeben. | F2 |
| 15 | HOR | GB-01 | echt, Fundort 1 bis 2 Zeilen daneben | Die Autorenzeile steht nach Rückzählung von der ersten Randnummer auf Z. 3, nicht Z. 2. | F2 |
| 16 | HOR | GB-17 | echt, Nebenangabe eine Zeile daneben | Die Zitate stehen eine Zeile tiefer als angegeben. | F2 |
| 17 | HOR | GB-44 | echt, Nebenangabe eine Zeile daneben | Dieselben Zitate wie in Fall 16 sind mit demselben Versatz angegeben. | F2 |
| 18 | HOR | GB-51 | echt, Nebenangabe eine Zeile daneben | Ein Eintrag im Literaturverzeichnis steht eine Zeile tiefer als angegeben. | F2 |
| 19 | TCD | GB-39 | echt, Fundort-Anmerkung | Der im Einwand zitierte Satz beginnt am Ende der Zeile vor der angegebenen. | F2 |
| 20 | LAM_A | GB-21 / GB-22 | Teilüberschneidung | Beide betreffen dieselbe Tabelle und schlagen eine Spalte für überlappende Wörter vor, ohne Verweis aufeinander. | F7 |
| 21 | LAM_A | GB-08 / GB-09 | Teilüberschneidung | Beide betreffen eine fehlende Version in derselben Tabelle, verschiedene Zeilen; GB-08 verweist auf GB-09. | nicht verwendet |
| 22 | LAM_A | GB-10 / GB-23 | Teilüberschneidung | Beide betreffen die Version des Faktendokuments je Prüflauf; GB-10 verweist auf GB-23. | nicht verwendet |
| 23 | LAM_A | GB-03 / GB-05 | Teilüberschneidung | Beide betreffen dieselbe Lückenstelle, Suchbeschreibung gegen fehlende Arbeit; GB-03 verweist auf GB-05. | nicht verwendet |
| 24 | LAM_A | GB-15 / GB-42 | Teilüberschneidung | Beide verlangen die Veröffentlichung einer Tabelle je Sitzung, ohne Verweis aufeinander. | F7 |
| 25 | LAM_A | KK-09 / KK-10 | Teilüberschneidung | Zwei Kleinkorrekturen zur selben Wendung in zwei Zellen derselben Tabellenzeile, ohne Verweis. | F7 |
| 26 | LAM_B | GB-18 / GB-35 | nahe Überschneidung | Beide nennen, dass die Fragen nur in einem Teil der Sitzungen vorab gezeigt wurden; GB-35 verweist auf GB-18. | nicht verwendet |
| 27 | LAM_B | GB-27 / GB-29 | nahe Überschneidung | Dieselbe Tabellenzelle, einmal Laufzahl, einmal fehlende Einheit, ohne Verweis aufeinander. | F7 |
| 28 | LAM_B | GB-24 / GB-28 | nahe Überschneidung | Beide berühren die Skriptversion; GB-24 verweist auf GB-28. | nicht verwendet |
| 29 | LAM_B | KK-02 / KK-07 | nahe Überschneidung | Zwei Kleinkorrekturen zur abgebrochenen Wiederholung an verschiedenen Stellen, ohne Verweis. | F7 |
| 30 | TCD | GB-34 / GB-36 | Teilüberschneidung | Gleiche Zeilen, zweiter Durchgang einer Prüfung; GB-36 verweist auf GB-34. | nicht verwendet |
| 31 | TCD | KK-05 / GB-32 | nahe Überschneidung | Gleiche Zeilen, Satzspiegel gegen Aufteilung, ohne Verweis. | F7 |
| 32 | TCD | KK-02 / GB-06 | nahe Überschneidung | Gleiche Zeilen, Satzspiegel gegen Inhalt, ohne Verweis. | F7 |
| 33 | TCD | GB-26 / GB-27 | nahe Überschneidung | Gleiche Zeile, Störgrößen gegen Beschreibung; GB-27 verweist auf GB-26. | nicht verwendet |
| 34 | TCD | GB-17 / GB-21 | nahe Überschneidung | Gleiche Zeilen, Chronologie gegen Arbeitsumgebung, ohne Verweis. | F7 |
| 35 | HOR | GB-30 / GB-34 (1) | Teilüberschneidung | Gleicher Fundort; GB-34 verweist für diesen Punkt auf GB-30. | nicht verwendet |
| 36 | HOR | GB-02 / GB-34 (3) | Teilüberschneidung | Gleicher Fundort, Aussage gegen Wortlaut des Items, ohne Verweis. | F7 |
| 37 | HOR | GB-08 / GB-34 (8) | Teilüberschneidung | Gleicher Fundort, Begriff gegen Zitattreue; GB-34 verweist auf GB-08. | nicht verwendet |
| 38 | HOR | GB-34 (5) / GB-38 / GB-19 | Teilüberschneidung | Drei Kennungen am selben Fundort (Wortlaut, Prozentwerte, Gerätebeschreibung), keine verweist auf eine andere. | F7 |
| 39 | HOR | GB-34 (8) / GB-38 | Teilüberschneidung | Gleicher Fundort, Wortlaut gegen Prozentwerte, ohne Verweis. | F7 |
| 40 | HOR | GB-10 / GB-45 | Teilüberschneidung | Gleiche Fundorte, Operationalisierung gegen Überzeichnung, ohne Verweis. | F7 |
| 41 | HOR | GB-10 / GB-43 | Teilüberschneidung | Gleiche Zeilen, Messung gegen Quellenzuschreibung; beide verweisen aufeinander. | nicht verwendet |
| 42 | HOR | GB-18 / GB-37 | Teilüberschneidung | Gleiche Zeilen, Design gegen Ergebnisbehauptung, ohne Verweis. | F7 |
| 43 | HOR | GB-21 / GB-24 | Teilüberschneidung | Gleiche Zeile, Summe gegen Teilnehmerfluss, ohne Verweis. | F7 |
| 44 | HOR | GB-17 / GB-47 | Teilüberschneidung | Gleiche offene Frage, Auswertung gegen Verfügbarkeit; GB-47 verweist auf GB-17. | nicht verwendet |
| 45 | LAM_A | GB-04 | Literaturvorschlag, im Verzeichnis: ja | Vorschlag, die Wiedergabe einer schon zitierten Metaanalyse um zwei Moderatoren zu ergänzen. | nicht verwendet |
| 46 | LAM_A | GB-33 | Literaturvorschlag, im Verzeichnis: ja | Vorschlag, eine schon zitierte Arbeit in der Diskussion aufzugreifen. | nicht verwendet |
| 47 | TCD | GB-08 | Literaturvorschlag, im Verzeichnis: ja | Vorschlag, einen Wert nur noch der passenden der zwei schon zitierten Arbeiten zuzuordnen. | nicht verwendet |
| 48 | TCD | GB-08 | Literaturvorschlag, im Verzeichnis: ja | Vorschlag, für die zweite schon zitierte Arbeit deren eigenes Ergebnis zu nennen. | nicht verwendet |
| 49 | TCD | GB-09, GB-41 | Literaturvorschlag, im Verzeichnis: ja | Vorschlag, eine schon zitierte Arbeit mit korrigierten Werten wiederzugeben und in der Diskussion aufzugreifen. | nicht verwendet |
| 50 | TCD | GB-11 | Literaturvorschlag, im Verzeichnis: ja | Vorschlag, die Wiedergabe einer schon zitierten Arbeit um den Vergleich mit getippter Eingabe zu ergänzen. | nicht verwendet |
| 51 | TCD | GB-12 | Literaturvorschlag, im Verzeichnis: ja | Vorschlag, die Lückenbehauptung gegen eine schon zitierte Arbeit abzugrenzen. | nicht verwendet |
| 52 | TCD | GB-52 | Literaturvorschlag, im Verzeichnis: ja | Vorschlag, die Maße einer schon zitierten Arbeit für ein Studiendesign zu verwenden. | nicht verwendet |

Summe: 52 Fälle, davon 33 in sieben Klassen, 19 nicht verwendet.

## Fehlerklassen und Regeln

### F1 Seitenangabe eines Zeilenbereichs passt nicht zur Seite der Zeilen

| Feld | Inhalt |
|---|---|
| Klasse | Die Zeilen eines Fundorts stimmen, die Seitenangabe nicht, fast immer an einem Seitenwechsel: ein Bereich, der auf der Vorseite beginnt, wird nur mit der Folgeseite angegeben, oder ein Bereich auf einer Seite wird als "S. x bis y" angegeben. |
| Zahl der Fälle | 4 (LAM_A 2, LAM_B 1, TCD 1, HOR 0) |
| Regel (Wortlaut) | Seitenangaben werden an der Seitengrenze geprüft. Ein Zeilenbereich, der über einen Seitenwechsel reicht, wird als "S. x, Z. a bis S. y, Z. b" geschrieben, ein Bereich, der ganz auf einer Seite liegt, nennt nur diese Seite. `formatpruefung.py` erhält dafür `text.json` und listet jeden Fundort, dessen erste oder letzte Zeile in `text.json` auf einer anderen Seite steht als angegeben, und jeden Fundort, dessen erste oder letzte Zeile innerhalb der ersten oder letzten zwei Zeilen einer Seite liegt. Jeder gelistete Fundort wird am Seitenbild der genannten Seite und ihrer Nachbarseite bestätigt oder berichtigt, bevor das Gutachten übergeben wird. |
| Ziel | `science-review-gutachten`, `scripts/formatpruefung.py` (neue Prüfung, Aufruf mit `text.json`), beschrieben in `SKILL.md`, Abschnitt "7. Formatprüfung"; Verweis in `references/befundformat.md`, Abschnitt "Formulierung", Punkt 8 "Fundort bis zur Zelle". |
| Begründung | Alle vier Fälle liegen an einem Seitenwechsel, und in LAM_A stehen die betroffenen Zeilen laut Prüfbericht in `text.json` auf der falschen Seite; ein Abgleich nur gegen `text.json` fände sie also nicht, wohl aber die Liste der Fundorte an Seitengrenzen, die am Seitenbild bestätigt werden. Die bestehende Grundregel 4 verlangt die Bestätigung an der Randnummer, sagt aber nicht, welche Fundorte besonders gefährdet sind; die Regel macht daraus eine Liste, die abgearbeitet wird wie die Paare nach Schritt 4.2. |
| Zählregel | Gezählt wird je Kennung einmal, wenn der Prüfbericht für irgendeinen ihrer Fundorte (Haupt- oder Nebenstelle, auch in einer Anmerkung "ohne Einfluss auf die Zählung") feststellt, dass die genannten Zeilen stimmen, aber auf einer anderen Seite stehen als angegeben, oder dass ein Seitenbereich angegeben ist, den die Zeilen nicht überschreiten. Stimmt außerdem die Zeile nicht, zählt die Kennung nur hier, nicht in F2. |

### F2 Zeilennummer um eine oder zwei Zeilen versetzt

| Feld | Inhalt |
|---|---|
| Klasse | Die Seite stimmt, die Zeile weicht um eine oder zwei Zeilen von der gedruckten Randnummer ab, typisch vor der ersten Randnummer einer Seite (Kopf, Autorenzeile), in Literaturverzeichnis und eingerückten Zitaten, an Stellen mit Verschiebung in `text.json`, oder weil der Beginn eines zitierten Satzes am Ende der Vorzeile übersehen wurde. |
| Zahl der Fälle | 8 (LAM_A 2, LAM_B 1, TCD 1, HOR 4) |
| Regel (Wortlaut) | Unsichere Zeilen werden abgezählt, nicht übernommen. `formatpruefung.py` listet mit `text.json` jeden Fundort, dessen Zeile dort `zeile_sicher: false` hat oder vor der ersten oder nach der letzten Randnummer einer Seite liegt. Jeder gelistete Fundort wird am Seitenbild von der nächsten gedruckten Randnummer aus abgezählt; die Zählung steht im Prüfprotokoll mit der Randnummer, von der aus gezählt wurde. Die erste Zeile eines Zitats ist die Zeile, in der sein erstes Wort steht, die letzte die seines letzten Wortes. Lässt sich eine Zeile nicht sicher abzählen, nennt der Fundort Seite und Element statt einer Zeile. |
| Ziel | `science-review-gutachten`, `SKILL.md`, Abschnitt "4. Zusammenführen", Schritt 5 "Wortlaut nachprüfen" (neuer Satz), mit der Liste aus `scripts/formatpruefung.py`; der Satz in Abschnitt "1. Einlesen" ("An unsicheren Zeilen nennt das Gutachten Seite und Element oder die am Seitenbild bestätigte Zeile") verweist darauf. |
| Begründung | Die bestehende Vorgabe beschreibt, was an unsicheren Zeilen gelten soll, aber kein Schritt stellt fest, welche Fundorte unsicher sind; deshalb wurden Nummern aus `text.json` übernommen. Mindestens drei der acht Fälle liegen nachweislich in solchen Bereichen (zwei folgen laut Prüfbericht der Verschiebung in `text.json`, einer liegt vor der ersten Randnummer der Seite); zwei weitere sind dieselbe Zitatgruppe in zwei Befunden mit demselben Versatz, was auf eine gemeinsame, nicht abgezählte Quelle der Nummer hinweist. Die Liste mit Pflicht zum Abzählen und die Regel für den Zitatbeginn treffen alle drei beobachteten Ursachen. |
| Zählregel | Gezählt wird je Kennung einmal, wenn der Prüfbericht für irgendeinen ihrer Fundorte oder für eine Zeilenangabe im Einwand feststellt, dass die Zeile bei richtiger Seite um mindestens eine Zeile von der gedruckten Randnummer abweicht, gleich ob in der Fundorttabelle oder in einer Anmerkung "ohne Einfluss". Ist zugleich die Seite falsch, zählt die Kennung in F1. |

### F3 Falsche Zählung im Einwand

| Feld | Inhalt |
|---|---|
| Klasse | Eine Häufigkeit oder Aufteilung im Einwand stimmt nicht: der Zählbereich ist unklar oder gemischt (Fließtext und Tabellen über `text.json`), und eine daran geknüpfte Allaussage ("nie", "immer") widerspricht den mitgezählten Stellen, oder bei einer Aufteilung nach Eigenschaften fehlt ein Element, weil die Summe der Teile nicht gegen eine unabhängige Gesamtzahl gehalten wurde. |
| Zahl der Fälle | 2 (LAM_A 1, TCD 1) |
| Regel (Wortlaut) | Jede Zählung im Einwand nennt Bereich, Grundlage und Gesamtheit. Wer zählt, wie oft etwas vorkommt oder wie viele Elemente eine Eigenschaft haben, nennt den Zählbereich (Fließtext, Tabellen, Abbildungen oder ganzes Manuskript, mit Seiten oder Zeilen), die Grundlage (`text.json` oder Seitenbild) und die gezählten Fundorte oder Elemente einzeln. Eine Aufteilung nach Eigenschaften (Farbe, Form, Kategorie) wird gegen eine unabhängig gezählte Gesamtzahl der Elemente gehalten, und die Rechnung, dass die Teile die Gesamtzahl ergeben, steht mit Python im Befund. Eine Aussage über alle Treffer ("nie", "immer", "jedes Mal") gilt nur für den genannten Bereich und wird an jedem Treffer geprüft. Zählungen in Tabellen und Abbildungen werden am Seitenbild wiederholt. |
| Ziel | `science-review-gutachten`, `references/befundformat.md`, Abschnitt "Formulierung", neuer Punkt 13 "Zählungen"; die Prüfliste `science-review-abbildungen/references/pruefliste-abbildungen.md`, P3, Schritt 2 "Zählen", verweist darauf. |
| Begründung | Im ersten Fall hätte die Pflicht, den Bereich zu nennen und die Treffer aufzulisten, gezeigt, dass zwei der Treffer Tabellenzeilen mit dem fraglichen Zusatz sind; im zweiten hätte der Abgleich der Teilsummen gegen die Gesamtzahl der Pfeile das fehlende Element angezeigt. Beide Fehler entstehen nicht aus falschem Lesen, sondern aus einer Zählung ohne Gegenprobe; die Gegenprobe ist mechanisch und in jedem Manuskript möglich, das Elemente oder Wörter zählen lässt. Formulierung 12 (Kern und Nebensatz) und Schritt 4.5 der Zusammenführung verlangen das Nachzählen schon, aber ohne Bereich und Gesamtheit lässt sich eine falsche Zählung mit einer richtigen Rechnung bestätigen. |
| Zählregel | Gezählt wird je Kennung einmal, wenn ihr Urteil "teilweise echt" oder "falsch" ist und der Prüfbericht als Grund nennt, dass eine Anzahl, Häufigkeit oder Aufteilung im Einwand (oder im Titel) nicht mit seiner eigenen Zählung übereinstimmt. Weicht nur ein Messwert ab (Länge, Farbe, Lage), zählt der Fall nicht hier. |

### F4 Fehlanzeige oder Gleichheitsaussage über mehrere Stellen nicht an jeder Stelle geprüft

| Feld | Inhalt |
|---|---|
| Klasse | Ein Befund oder eine Kleinkorrektur behauptet, etwas komme in einem Bereich nicht vor ("kein Kernbegriff wird aufgenommen") oder laute an mehreren Stellen gleich ("dieselbe Form wie in Z. a und Z. b"), und mindestens eine Stelle widerlegt das, weil nach einer Wortform gesucht wurde statt nach dem Begriff oder weil die zweite Stelle nicht zeichengenau verglichen wurde. |
| Zahl der Fälle | 2 (LAM_B 1, HOR 1) |
| Regel (Wortlaut) | Fehlanzeigen und Gleichheitsaussagen werden als Suche belegt. Sagt ein Einwand, ein Titel oder ein Ersatzwortlaut, dass etwas in einem Bereich an keiner Stelle vorkommt, oder dass mehrere Stellen gleich lauten, nennt der Befund die Suche: den Bereich mit Seiten und Zeilen, die Suchbegriffe einschließlich Wortformen, Abkürzungen und gleichbedeutender Wendungen der gesuchten Begriffe, und die Trefferzahl. Bei einer Gleichheitsaussage wird jede genannte Stelle einzeln am Seitenbild zeichengenau verglichen, auch Akzente, Bindestriche und Leerzeichen; bei Kleinkorrekturen steht die Liste der verglichenen Stellen in der Spalte Ersatz. Fehlt diese Angabe, wird die Aussage auf die geprüften Stellen beschränkt oder gestrichen. |
| Ziel | `science-review-gutachten`, `references/befundformat.md`, Abschnitt "Formulierung", Punkt 12 "Kern und Nebensatz" (Erweiterung). |
| Begründung | Punkt 12 nennt "nirgends", "kein Item" und "nur" schon als prüfpflichtig, sagt aber nicht, woran die Prüfung erkennbar ist; beide Fälle haben den Status verifiziert ohne Angabe einer Suche. Wer die Suchbegriffe ausschreiben muss, merkt, dass ein Kernbegriff in anderer Wortform auftreten kann; wer jede gleichgesetzte Stelle zeichengenau vergleichen muss, findet das fehlende Zeichen. Die Klasse tritt in zwei verschiedenen Manuskripten und bei zwei verschiedenen Befundarten (Befund und Kleinkorrektur) auf und ist an jedes Manuskript übertragbar. |
| Zählregel | Gezählt wird je Kennung einmal, wenn ihr Urteil "teilweise echt" oder "falsch" ist und der Prüfbericht als Grund nennt, dass eine Aussage über das Fehlen ("kein", "nirgends", "nicht aufgenommen", "nur") oder über die Gleichheit mehrerer Stellen an mindestens einer Stelle des Manuskripts nicht zutrifft. Ist die widerlegte Aussage eine Anzahl, zählt der Fall in F3. |

### F5 Beleg oder Angabe auf einen benachbarten Gegenstand übertragen

| Feld | Inhalt |
|---|---|
| Klasse | Der Kern des Befunds stimmt, aber eine Teilaussage stützt sich auf eine Stelle, die einen anderen Gegenstand nennt (eine andere Größe, einen anderen Fall, einen anderen Zeitraum), oder ein Wert, den das Manuskript nur für einen Nachbarfall nennt, wird auf einen weiteren Fall übertragen und geht in eine Zählung ein. |
| Zahl der Fälle | 2 (LAM_B 2) |
| Regel (Wortlaut) | Jeder Beleg belegt genau die Teilaussage, an der er steht. Bevor eine Stelle als Beleg einer Teilaussage im Einwand steht, wird an ihrem Wortlaut geprüft, dass sie denselben Gegenstand nennt: dieselbe Größe, denselben Fall, denselben Zeitraum. Ein Wert (Datum, Zahl, Version), den das Manuskript nur für einen anderen Gegenstand oder gar nicht nennt, wird nicht übertragen; wird er erschlossen, steht er mit Herleitung und Status erschlossen, und jede Zählung, die von ihm abhängt, nennt zusätzlich die Zahl der Fälle, die ohne ihn sicher sind. |
| Ziel | `science-review-gutachten`, `SKILL.md`, Abschnitt "4. Zusammenführen", Schritt 5 "Wortlaut nachprüfen" (neuer Satz nach "Ein Nebensatz, der über den belegten Kern hinausgeht, wird belegt oder gestrichen."). |
| Begründung | Schritt 5 prüft bisher, ob ein Zitat oder eine Zahl im Manuskript steht, nicht, ob die Stelle dasselbe meint wie die Aussage, an der sie steht; beide Fälle bestehen diese Prüfung, weil die zitierten Stellen wörtlich vorhanden sind. Die Typischen Fehler des Skills kennen "benachbarter Befund: richtige Stelle, anderer Gegenstand" für ganze Befunde, nicht für einzelne Belege und übertragene Werte. Beide Fälle stehen zwar im selben Lauf, aber in verschiedenen Befunden aus verschiedenen Instanzen (S4; S2 und SD), und dieselbe Übertragung ist überall möglich, wo ein Manuskript mehrere ähnliche Fälle mit teils fehlenden Angaben führt. |
| Zählregel | Gezählt wird je Kennung einmal, wenn ihr Urteil "teilweise echt" oder "falsch" ist und der Prüfbericht als Grund nennt, dass eine angeführte Belegstelle einen anderen Gegenstand betrifft als die Teilaussage, oder dass ein Wert angegeben wird, den das Manuskript für diesen Gegenstand nicht nennt. |

### F6 Quellendetail als verifiziert ausgewiesen, ohne nachprüfbaren Zugang

| Feld | Inhalt |
|---|---|
| Klasse | Ein Befund gibt aus einer Quelle Einzelheiten wieder, die über Abstract und Verlagsseite hinausgehen (Seitenzahl, Tabelle, wörtliche Definition), mit Status verifiziert, aber ohne Angabe, über welchen Zugang der Volltext gelesen wurde; der Prüfer erreicht nur den Abstract und kann den Teil nicht prüfen. |
| Zahl der Fälle | 1 (LAM_B 1) |
| Regel (Wortlaut) | Der Status einer Aussage über eine Quelle nennt den gelesenen Zugang. Bei jeder Aussage über eine Quelle steht im Status, was gelesen wurde (Volltext, Abstract oder Verlagsseite), über welche URL oder DOI und in welcher Fassung, wenn die Quelle in mehreren Fassungen vorliegt. Eine Angabe, die über das Gelesene hinausgeht, etwa Seite, Tabelle, Abschnitt oder wörtlicher Wortlaut aus dem Haupttext, hat nur dann den Status verifiziert, wenn der Volltext mit seinem Zugang genannt ist; sonst hat sie den Status erschlossen, und die Quelle steht unter "Grenzen des Gutachtens". |
| Ziel | `science-review-gutachten`, `references/befundformat.md`, Abschnitt "Status", Zeile "verifiziert" (Ergänzung); Verweis aus `references/segment-1.md`, P13, Schritt 4. |
| Begründung | Ein einzelner Fall, aber er wird in anderen Läufen in gleicher Art wieder auftreten: Jedes Gutachten gibt Quellen wieder, und deren Volltexte sind für den Prüfer wechselnd erreichbar. Im selben Durchgang standen im TCD-Bericht drei Kennungen zunächst auf "nicht prüfbar" und eine auf "teilweise echt", weil eine Quelle in zwei Fassungen mit verschiedenen Zahlen vorlag, und mehrere Prüfberichte vermerken ungeprüfte Teilaussagen zu Quellen, die nur über Sekundärquellen oder gar nicht zu lesen waren. Wer Zugang und Fassung nennt, macht die Aussage für den Prüfer erreichbar oder ihren Status ehrlich; P13 Schritt 4 regelt bisher nur den Fall, dass die Quelle gar nicht lesbar war, nicht den, dass nur ein Teil gelesen wurde. |
| Zählregel | Gezählt wird je Kennung einmal, wenn der Prüfbericht sie ganz oder für einen Teil als "nicht prüfbar" führt, weil die angeführte Quellenstelle nicht zugänglich war, und das Gutachten für diesen Teil den Status verifiziert ohne Angabe des Zugangs zum Volltext führt. Nennt das Gutachten für diesen Teil den Status erschlossen, zählt der Fall nicht. |

### F7 Getrennt gebliebene Nachbarbefunde ohne Querverweis

| Feld | Inhalt |
|---|---|
| Klasse | Zwei oder mehr Kennungen haben einen überlappenden Fundort oder einen eng verwandten Gegenstand, wurden zu Recht nicht zusammengelegt, nennen einander aber nicht; der Prüfer muss die Abgrenzung selbst herstellen. Dazu gehören auch zwei Kleinkorrekturen zur selben Wendung in derselben Tabellenzeile. |
| Zahl der Fälle | 14 (LAM_A 3, LAM_B 2, TCD 3, HOR 6) |
| Regel (Wortlaut) | Getrennt gebliebene Nachbarbefunde verweisen aufeinander. Bleiben zwei Kennungen mit überlappendem Fundort oder verwandtem Gegenstand nach Schritt 4.2 getrennt, nennt die spätere im Einwand die frühere mit einem Halbsatz zur Abgrenzung, also was hier anders geprüft oder verlangt wird als dort; bei Kleinkorrekturen steht der Verweis in der Spalte Ersatz. Betreffen zwei Kleinkorrekturen dieselbe Wendung in derselben Tabellenzeile oder demselben Satz, werden sie eine Kleinkorrektur. `formatpruefung.py --paare` meldet jedes Paar, in dem keine der beiden Kennungen die andere nennt, als Fehler, nicht als Hinweis. |
| Ziel | `science-review-gutachten`, `SKILL.md`, Abschnitt "4. Zusammenführen", Schritt 2 "Doppelungen auflösen" (neuer Satz), umgesetzt in `scripts/formatpruefung.py`, Funktion für `--paare`. |
| Begründung | Von 25 Überschneidungen, die die vier Prüfberichte nennen, tragen 11 schon einen Verweis, und für diese halten die Prüfer die Abgrenzung ohne weitere Prüfung fest; die 14 ohne Verweis mussten sie selbst abgrenzen. Schritt 4.2 verlangt, dass jedes Paar entschieden wird, hält die Entscheidung aber nicht im Gutachten fest; der Pflichtverweis macht sie sichtbar und lässt sich mechanisch prüfen, weil das Skript die Paare schon bildet. Paare mit verwandtem Gegenstand an verschiedenen Fundorten erkennt das Skript nicht; für sie gilt die Regel beim Lesen in Schritt 4.2. |
| Zählregel | Gezählt wird jeder Eintrag (Paar oder Gruppe) im Abschnitt "Doppelungen" eines Prüfberichts, den der Prüfer als Teilüberschneidung oder nahe Überschneidung nennt und in dem keine der beteiligten Kennungen eine andere beteiligte Kennung im Gutachten nennt; eine Gruppe aus drei Kennungen zählt einmal. Einträge mit mindestens einem Verweis zählen nicht. Eine volle Doppelung (gleicher Fundort und gleicher Gegenstand) zählt nicht hier, sondern wird gesondert gezählt. |

## Nicht verwendete Fälle

| Nr. | Lauf | Kennung | Grund für die Nichtverwendung |
|---|---|---|---|
| 21, 22, 23 | LAM_A | GB-08 / GB-09, GB-10 / GB-23, GB-03 / GB-05 | Die spätere oder frühere Kennung verweist ausdrücklich auf die andere; das ist das Sollverhalten nach Regel F7, kein Fehler. |
| 26, 28 | LAM_B | GB-18 / GB-35, GB-24 / GB-28 | wie oben, Querverweis vorhanden. |
| 30, 33 | TCD | GB-34 / GB-36, GB-26 / GB-27 | wie oben, Querverweis vorhanden. |
| 35, 37, 41, 44 | HOR | GB-30 / GB-34, GB-08 / GB-34, GB-10 / GB-43, GB-17 / GB-47 | wie oben, Querverweis vorhanden; der Prüfbericht vermerkt bei drei davon den Verweis selbst. |
| 45, 46 | LAM_A | GB-04, GB-33 | Der Vorschlag betrifft die Wiedergabe oder das Aufgreifen einer schon zitierten Arbeit, nicht fehlende Literatur; das erlaubt `references/befundformat.md`, Zusatzregel 4, ausdrücklich. Der Prüfbericht führt die Arbeiten nur der Vollständigkeit halber in der Spalte "im Verzeichnis: ja". |
| 47 bis 52 | TCD | GB-08, GB-09 und GB-41, GB-11, GB-12, GB-52 | wie oben: Jeder Vorschlag ändert die Zitierung einer schon zitierten Arbeit oder nutzt sie für einen Gegenentwurf; der Prüfbericht zählt "Neu vorgeschlagene Arbeiten: 3, davon 0 bereits im Verzeichnis". Eine Regel würde hier nichts senken, weil kein Fehler vorliegt. |

Nicht als Fälle aufgenommen, weil Schritt 1 sie nicht erfasst: Abweichungen von Messwerten innerhalb eines echten Befunds, die der Prüfbericht als für den Befund folgenlos bezeichnet (LAM_A GB-37, HOR GB-13), und Arbeiten, die ein Prüfbericht ausdrücklich nicht als Vorschlag führt (LAM_B zu GB-08 und GB-42, HOR zu GB-50).
