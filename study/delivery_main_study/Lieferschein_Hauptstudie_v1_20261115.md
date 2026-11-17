# Lieferung an Paper 3: Ergebnisse der Hauptstudie und der Vorstudie

Ergebnisse von Schritt 7.8 (Auswertung) und 7.V (Nachzählung der Vorstudie) nach dem Studienprotokoll vom 2026-10-17 mit drei Nachträgen. Hauptergebnis ist `hauptstudie/auswertung/Trefferbilanz_Hauptstudie_v1_20261115.md`.

## Inhalt

| Ordner oder Datei | Inhalt |
|---|---|
| `hauptstudie/auswertung/` | Trefferbilanz, Kennzahlen je Gutachten, K4 und K8 mit den drei Zählungen je Prüfbericht, Zählregeln |
| `hauptstudie/vorstudie/` | Nachzählung der Vorstudie, Zuordnungen der 15 Gutachten, Aufträge |
| `hauptstudie/tools/` | alle Skripte, darunter `auswertung.py`, `k8_mehrheit.py`, `trefferbilanz.py` und die unabhängige Gegenrechnung `gegenrechnung.py` |
| `hauptstudie/laeufe/` | Laufplan mit Zuordnung der Codes zu den Bedingungen, 48 Gutachten, Verifikationen, Zuordnungen |
| `hauptstudie/einstufung/` | Befundgruppen, KI-Einstufungen, Mehrheiten, Stichprobe und Urteile des Auftraggebers, endgültige Urteile |
| `hauptstudie/soll/`, `hauptstudie/soll_vorstudie/` | bestätigte Sollbefunde mit Extraktion und Mehrheit |
| `hauptstudie/rq3/` | Fehlerklassen F1 bis F7, Entscheidungen, Vergleich der Vorschlagsläufe R und R2 (K9) |
| `hauptstudie/spinoff_ki_herkunft/` | Kennzeichnung der Gutachten mit KI-Herkunft (G03) |
| `hauptstudie/Studienprotokoll_Hauptstudie_v1_20261017.md`, `hauptstudie/Laufregister.md` | Protokoll und Laufregister |
| `SHA256SUMS.txt` | Prüfsumme jeder Datei dieser Lieferung |

## Hinweise für die Auswertung im Paper

1. Jede Kennzahl ist mit einem zweiten, unabhängig geschriebenen Skript nachgerechnet (`tools/gegenrechnung.py`, 112 von 112 Werten gleich). Die erste Fassung von `auswertung.py` unterschätzte K6, weil die Prüfinstanz bei 90 zutreffenden Kleinkorrekturen nicht erkannt wurde; die Trefferbilanz enthält die korrigierten Werte.
2. Die Urteile des Auftraggebers zur Stichprobe (60 Einzelbefunde, 6 Gruppen) wurden dem Assistenten beim Hochladen angezeigt; der Assistent kannte damit vor der Auswertung die Inhalte dieser 66 Einträge, nicht ihre Bedingung.
3. In den Texten von 81 der 1917 Kleinkorrekturen blieb bei Gruppierung und Einstufung die Spalte mit der Prüfinstanz stehen; sie nennt die Instanz, nicht Bedingung oder Fassung.
4. In zwei Gutachten der Vorstudie wurden für die Nachzählung drei Nennungen von Skillnamen und einer Versionsnummer neutralisiert; in den Gutachten der Hauptstudie kommt kein Skillname vor.
5. Die bisherige Trefferbilanz der Vorstudie zählte gegen eine andere, kleinere Sollbefundliste; beide Zählungen stehen in der Nachzählung nebeneinander.
