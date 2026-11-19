# Prüfung auf Wortlaut des KI-Peer-Review-Dienstes in den Dateien zu Prüfdurchgang 4

Geprüft sind die vier Gutachten und die vier Prüfberichte von Prüfdurchgang 4 gegen die beiden Gutachten des KI-Peer-Review-Dienstes zu LAM und TCD (Entscheidung 38). Eine Fundstelle ist eine längste Wortfolge von mindestens n Wörtern, die in einer geprüften Datei und in einem Gutachten des Dienstes gleich steht; Groß- und Kleinschreibung und Satzzeichen zählen nicht. Folgen, die auch im Text eines der drei Manuskripte stehen, zählt das Skript nicht mit. Jede verbliebene Fundstelle ist danach an Gutachtenzeile, Dienststelle und Manuskript gesichtet und eingeordnet:

- **Manuskript:** Beide geben Wortlaut oder Inhalt des Manuskripts wieder, den das Skript nicht als Manuskripttext erkennt, weil er in einer Abbildung steht, über Zeilen mit Randnummern läuft oder nur aus Literaturangaben, Zahlen und Bezeichnungen besteht.
- **Wendung:** Gutachten und Dienst haben dieselbe Formulierung, die das Manuskript so nicht hat. Das ist eine wörtliche Übereinstimmung mit dem Dienst; ob sie übernommen oder unabhängig entstanden ist, lässt sich nicht feststellen.

Der Bericht nennt Datei, Zeile und Länge, nicht den Wortlaut, damit er selbst keinen Wortlaut des Dienstes enthält. Nichts wurde entfernt. Gerechnet mit `tools/dienst_wortlaut.py` und `tools/dienst_wortlaut_bericht.py`; die Einordnung ist Lesart des Assistenten.

## Zählung

| Schwelle | Fundstellen | davon Manuskript | davon Wendung | in Gutachten | in Prüfberichten |
|---|---|---|---|---|---|
| ab 6 Wörtern | 43 | 34 | 9 | 40 | 3 |
| ab 8 Wörtern | 13 | 12 | 1 | 12 | 1 |

Im Gutachten und im Prüfbericht zu Fall 3 (egusphere-2025-2248) und in den Prüfberichten zu LAM gibt es keine Fundstelle. Die längste Fundstelle der Art Wendung hat 10 Wörter.

## Fundstellen der Art Wendung

| Datei | Zeile | Wörter | ab 8 Wörtern | Einordnung |
|---|---|---|---|---|
| `erprobung/durchgang4/LAM_A/Listen_Answer_Memorize_Copernicus_Gutachten_20261016.md` | 496 | 7 | nein | Satz des Manuskripts gekürzt ("; it found" zu "found"), in Gutachten und Dienst gleich gekürzt |
| `erprobung/durchgang4/LAM_B/Listen_Answer_Memorize_Copernicus_Gutachten_20261016.md` | 486 | 6 | nein | Zahlen und Begriffe des Manuskripts in einer Fügung, die das Manuskript nicht hat |
| `erprobung/durchgang4/TCD/Talk_Check_Decide_A_Skill-Based_Workflow_Gutachten_20261016.md` | 14 | 6 | nein | Wendung zu "written procedures" und "skills", im Manuskript anders gefügt |
| `erprobung/durchgang4/TCD/Talk_Check_Decide_A_Skill-Based_Workflow_Gutachten_20261016.md` | 14 | 10 | ja | Aufzählung der sechs Prüfachsen des Manuskripts in einer Reihenfolge, die das Manuskript nicht hat |
| `erprobung/durchgang4/TCD/Talk_Check_Decide_A_Skill-Based_Workflow_Gutachten_20261016.md` | 108 | 6 | nein | Wendung zu den Vergleichsmodellen, im Manuskript anders gefügt |
| `erprobung/durchgang4/TCD/Talk_Check_Decide_A_Skill-Based_Workflow_Gutachten_20261016.md` | 114 | 6 | nein | Beschreibung des Nenners einer Quote, im Manuskript nicht so formuliert |
| `erprobung/durchgang4/TCD/Talk_Check_Decide_A_Skill-Based_Workflow_Gutachten_20261016.md` | 470 | 6 | nein | Begriffe einer Abbildungsunterschrift des Manuskripts mit angehängtem "are reported" |
| `erprobung/durchgang4/TCD/Talk_Check_Decide_A_Skill-Based_Workflow_Gutachten_20261016.md` | 509 | 6 | nein | Wendung zur Zahl der Einträge mit DOI; das Manuskript nennt nur die Einträge |
| `erprobung/durchgang4/TCD/Talk_Check_Decide_A_Skill-Based_Workflow_Gutachten_20261016.md` | 510 | 6 | nein | Wendung zur Zahl der Einträge mit DOI; das Manuskript nennt nur die Einträge |

## Fundstellen der Art Manuskript

| Datei | Zeile | Wörter | Einordnung |
|---|---|---|---|
| `erprobung/durchgang4/LAM_A/Listen_Answer_Memorize_Copernicus_Gutachten_20261016.md` | 44 | 11 | Literaturangaben des Manuskripts |
| `erprobung/durchgang4/LAM_A/Listen_Answer_Memorize_Copernicus_Gutachten_20261016.md` | 222 | 6 | Modell-, Versions-, Abschnitts- oder Tabellenbezeichnungen des Manuskripts mit Bindewörtern |
| `erprobung/durchgang4/LAM_A/Listen_Answer_Memorize_Copernicus_Gutachten_20261016.md` | 562 | 6 | Text oder Werte aus Abbildung oder Tabelle des Manuskripts |
| `erprobung/durchgang4/LAM_A/Listen_Answer_Memorize_Copernicus_Gutachten_20261016.md` | 580 | 9 | Literaturangaben des Manuskripts |
| `erprobung/durchgang4/LAM_A/Listen_Answer_Memorize_Copernicus_Gutachten_20261016.md` | 580 | 8 | Literaturangaben des Manuskripts |
| `erprobung/durchgang4/LAM_A/Listen_Answer_Memorize_Copernicus_Gutachten_20261016.md` | 593 | 6 | Zitat oder Satz des Manuskripts |
| `erprobung/durchgang4/LAM_A/Listen_Answer_Memorize_Copernicus_Gutachten_20261016.md` | 690 | 6 | Abschnittstitel des Manuskripts |
| `erprobung/durchgang4/LAM_B/Listen_Answer_Memorize_Copernicus_Gutachten_20261016.md` | 174 | 10 | Literaturangaben des Manuskripts |
| `erprobung/durchgang4/LAM_B/Listen_Answer_Memorize_Copernicus_Gutachten_20261016.md` | 176 | 6 | Literaturangaben des Manuskripts |
| `erprobung/durchgang4/TCD/Talk_Check_Decide_A_Skill-Based_Workflow_Gutachten_20261016.md` | 108 | 6 | Modell-, Versions-, Abschnitts- oder Tabellenbezeichnungen des Manuskripts mit Bindewörtern |
| `erprobung/durchgang4/TCD/Talk_Check_Decide_A_Skill-Based_Workflow_Gutachten_20261016.md` | 196 | 8 | Text oder Werte aus Abbildung oder Tabelle des Manuskripts |
| `erprobung/durchgang4/TCD/Talk_Check_Decide_A_Skill-Based_Workflow_Gutachten_20261016.md` | 204 | 6 | Modell-, Versions-, Abschnitts- oder Tabellenbezeichnungen des Manuskripts mit Bindewörtern |
| `erprobung/durchgang4/TCD/Talk_Check_Decide_A_Skill-Based_Workflow_Gutachten_20261016.md` | 379 | 7 | Text oder Werte aus Abbildung oder Tabelle des Manuskripts |
| `erprobung/durchgang4/TCD/Talk_Check_Decide_A_Skill-Based_Workflow_Gutachten_20261016.md` | 408 | 8 | Modell-, Versions-, Abschnitts- oder Tabellenbezeichnungen des Manuskripts mit Bindewörtern |
| `erprobung/durchgang4/TCD/Talk_Check_Decide_A_Skill-Based_Workflow_Gutachten_20261016.md` | 431 | 8 | Zitat oder Satz des Manuskripts |
| `erprobung/durchgang4/TCD/Talk_Check_Decide_A_Skill-Based_Workflow_Gutachten_20261016.md` | 431 | 6 | Text oder Werte aus Abbildung oder Tabelle des Manuskripts |
| `erprobung/durchgang4/TCD/Talk_Check_Decide_A_Skill-Based_Workflow_Gutachten_20261016.md` | 431 | 9 | Modell-, Versions-, Abschnitts- oder Tabellenbezeichnungen des Manuskripts mit Bindewörtern |
| `erprobung/durchgang4/TCD/Talk_Check_Decide_A_Skill-Based_Workflow_Gutachten_20261016.md` | 432 | 6 | Modell-, Versions-, Abschnitts- oder Tabellenbezeichnungen des Manuskripts mit Bindewörtern |
| `erprobung/durchgang4/TCD/Talk_Check_Decide_A_Skill-Based_Workflow_Gutachten_20261016.md` | 445 | 8 | Text oder Werte aus Abbildung oder Tabelle des Manuskripts |
| `erprobung/durchgang4/TCD/Talk_Check_Decide_A_Skill-Based_Workflow_Gutachten_20261016.md` | 470 | 6 | Text oder Werte aus Abbildung oder Tabelle des Manuskripts |
| `erprobung/durchgang4/TCD/Talk_Check_Decide_A_Skill-Based_Workflow_Gutachten_20261016.md` | 496 | 6 | Text oder Werte aus Abbildung oder Tabelle des Manuskripts |
| `erprobung/durchgang4/TCD/Talk_Check_Decide_A_Skill-Based_Workflow_Gutachten_20261016.md` | 616 | 6 | Text oder Werte aus Abbildung oder Tabelle des Manuskripts |
| `erprobung/durchgang4/TCD/Talk_Check_Decide_A_Skill-Based_Workflow_Gutachten_20261016.md` | 617 | 6 | Text oder Werte aus Abbildung oder Tabelle des Manuskripts |
| `erprobung/durchgang4/TCD/Talk_Check_Decide_A_Skill-Based_Workflow_Gutachten_20261016.md` | 623 | 7 | Text oder Werte aus Abbildung oder Tabelle des Manuskripts |
| `erprobung/durchgang4/TCD/Talk_Check_Decide_A_Skill-Based_Workflow_Gutachten_20261016.md` | 623 | 6 | Text oder Werte aus Abbildung oder Tabelle des Manuskripts |
| `erprobung/durchgang4/TCD/Talk_Check_Decide_A_Skill-Based_Workflow_Gutachten_20261016.md` | 626 | 6 | Text oder Werte aus Abbildung oder Tabelle des Manuskripts |
| `erprobung/durchgang4/TCD/Talk_Check_Decide_A_Skill-Based_Workflow_Gutachten_20261016.md` | 641 | 8 | Modell-, Versions-, Abschnitts- oder Tabellenbezeichnungen des Manuskripts mit Bindewörtern |
| `erprobung/durchgang4/TCD/Talk_Check_Decide_A_Skill-Based_Workflow_Gutachten_20261016.md` | 680 | 12 | Zitat oder Satz des Manuskripts |
| `erprobung/durchgang4/TCD/Talk_Check_Decide_A_Skill-Based_Workflow_Gutachten_20261016.md` | 707 | 6 | Abschnittstitel des Manuskripts |
| `erprobung/durchgang4/TCD/Talk_Check_Decide_A_Skill-Based_Workflow_Gutachten_20261016.md` | 823 | 6 | Modell-, Versions-, Abschnitts- oder Tabellenbezeichnungen des Manuskripts mit Bindewörtern |
| `erprobung/durchgang4/TCD/Talk_Check_Decide_A_Skill-Based_Workflow_Gutachten_20261016.md` | 865 | 6 | Text oder Werte aus Abbildung oder Tabelle des Manuskripts |
| `erprobung/verifikation4/TCD_verifikation.md` | 34 | 6 | Text oder Werte aus Abbildung oder Tabelle des Manuskripts |
| `erprobung/verifikation4/TCD_verifikation.md` | 36 | 6 | Text oder Werte aus Abbildung oder Tabelle des Manuskripts |
| `erprobung/verifikation4/TCD_verifikation.md` | 64 | 8 | Text oder Werte aus Abbildung oder Tabelle des Manuskripts |

## Grenzen

- Übereinstimmungen unter sechs Wörtern sind nicht erfasst.
- Sinngemäße Übernahmen ohne wörtliche Gleichheit erfasst das Verfahren nicht.
- Die Einordnung beruht auf einer Sichtung durch den Assistenten, nicht auf einer unabhängigen zweiten Zählung.
