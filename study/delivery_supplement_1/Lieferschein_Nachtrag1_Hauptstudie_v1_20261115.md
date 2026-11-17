# Nachtrag 1 zur Lieferung an Paper 3

Ergänzt die Lieferung `Paper3_Lieferung_Hauptstudie_v1_20261115.zip` um Ergebnisse aus Schritt 7.10 (Rückschreiben nach der Auswertung). Die Lieferung selbst bleibt unverändert.

## Inhalt

| Ordner oder Datei | Inhalt |
|---|---|
| `hauptstudie/rueckschreiben/Analyse_F3_v1_20261115.md` | Analyse der Fälle von F3 (falsche Zählung im Einwand) in den Bedingungen B und D |
| `hauptstudie/rueckschreiben/Randzeilen_Fassungen_v1_20261115.md` | Erkennung der Randzeilen je PDF des Testkorpus in den Fassungen 1.0.0 bis 1.5.0 |
| `hauptstudie/tools/f3_analyse.py`, `hauptstudie/tools/randzeilen_vergleich.py` | Skripte zu beiden Dateien |
| `hauptstudie/Studienhandbuch_Hauptstudie_v1_20261016.md` | Studienhandbuch mit Auswertungsregel 9 |
| `paket/science-review-gutachten_v1_20261115.skill`, `abbildungen/paket/science-review-abbildungen_v1_20261115.skill` | Gutachten 1.5.0 und Abbildungen 1.4.0, entstanden aus der Auswertung |
| `SHA256SUMS.txt` | Prüfsumme jeder Datei dieses Nachtrags |

## Hinweise für die Auswertung im Paper

1. F3 steigt von B nach D von 0,42 auf 1,17 Fällen je Gutachten. 12 der 14 Fälle in D sind falsche Trefferzahlen oder Suchangaben, mit denen ein Einwand belegt wird; in B kommt kein solcher Fall vor. Die Regeln zu F3 und F4 in Fassung 1.4.0 lassen fast jeden Einwand mit einer Suchangabe belegen: 28,5 Trefferangaben je Gutachten in D, 0,2 in B. Falsche Zählungen im Kern einer Aussage gehen von 5 in B auf 2 in D zurück. Der Rückgang von F1 bis F7 in D enthält also einen Anstieg, den die neuen Regeln selbst verursachen. Die Einordnung je Fall als Kern- oder Belegzählung ist Lesart des Assistenten und nicht unabhängig gezählt.
2. Auswertungsregel 9 (jede Kennzahl vor der Abgabe mit einem zweiten, unabhängig geschriebenen Skript gegenrechnen) wurde nach der Auswertung ins Studienhandbuch aufgenommen. Sie beschreibt das in der Auswertung angewandte Vorgehen (Lieferung, Hinweis 1), war aber nicht vor den Läufen festgelegt und steht nicht im eingefrorenen Studienprotokoll.
3. Bei egusphere-2025-4506 und egusphere-2025-5046 erkennt `einlesen.py` die Randzeilen in allen Fassungen der Bedingungen A bis D nicht. In 24 der 48 Läufe folgte `text.json` deshalb nicht den gedruckten Randnummern; dort wurden die Fundorte am Seitenbild abgezählt. Alle Bedingungen sind gleich betroffen. Fehler in Zeilenangaben (F1, F2) können in diesen beiden Manuskripten häufiger sein als in den beiden anderen.
4. Gutachten 1.5.0 und Abbildungen 1.4.0 sind aus den vier Manuskripten der Hauptstudie abgeleitet und nicht erprobt. Ob die geänderte Zählregel wirkt, lässt sich nur an neuen Manuskripten messen.
