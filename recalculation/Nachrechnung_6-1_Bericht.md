# Nachrechnung der Kennzahlen der Hauptstudie (Workplan Paper 3, Schritt 6.1)

Unabhängige Nachrechnung aller Kennzahlen aus den Rohdaten der Lieferung `lieferung_hauptstudie_20261115` nach den Definitionen des Studienprotokolls (Fassung mit drei Nachträgen, SHA-256 93d2e122...f859, gleich der Prüfsummendatei). Die Skripte unter `hauptstudie/tools/` wurden weder benutzt noch gelesen; die Quellen wurden nur gelesen. Je Bedingung Mittelwert und Spannweite über die drei Wiederholungen, je Wiederholung die vier Manuskripte gepoolt (Summe der Treffer durch Summe der Sollbefunde; Zählgrößen als Mittel je Gutachten). Ein Wert gilt als gleich, wenn er um höchstens 0,05 Prozentpunkte beziehungsweise 0,05 Fälle je Gutachten vom gelieferten Wert abweicht (die Lieferung rundet auf 0,1 Prozentpunkte beziehungsweise 0,01 Fälle).

## 1. Ergebnis in Zahlen

| Messgröße | Wert |
|---|---|
| verglichene Werte der Trefferbilanz (ohne Doppelzählung) | 592 |
| davon gleich | 581 |
| davon abweichend (> 0,05) | 11 |
| abweichende Werte, die mit der Definition der Lieferung exakt reproduziert werden | 9 |
| abweichende Werte mit belegbarem Fehler in der Lieferung | 2 (K9) |
| Werte je Gutachten aus `kennzahlen_je_gutachten.json` verglichen, davon abweichend | 912, 0 |
| K4 und F1 bis F7 je Gutachten aus `k8/mehrheit.json` verglichen, davon abweichend | 384, 0 |
| Zellen von `kennzahlen_teil1.md` und `kennzahlen_k4_k8.md` gleich der Trefferbilanz | 180 von 180 |
| Urteile der Effektregel (RQ1 bis RQ3, mit und ohne G03) gleich | 6 von 6 |
| Übereinstimmung der Stichprobe (K7, Schwelle 80 %) | 60 Einzelbefunde, 95,0 %, Schwelle erreicht |

## 2. Prüfung der Eingaben und Mehrheiten

| Prüfung | Ergebnis |
|---|---|
| Laufplan: Läufe, je Bedingung und Manuskript Wiederholungen 1 bis 3 | 48 Läufe, alle 16 Zellen mit 1, 2, 3; keine Kennung doppelt, keine Nachverarbeitungskennung doppelt |
| Fassungen und Pakete je Bedingung | je Bedingung genau eine Kombination, gleich Protokoll Abschnitt 2 und 4 (A 1.0.0, B und C 1.3.0/1.2.0/1.2.0, D 1.4.0/1.3.0/1.2.0; Paketprüfsummen gleich den ersten 12 Stellen im Protokoll) |
| Sollbefunde | 205 Einwände, 198 bestätigt (143 inhaltlich, 55 Kleinkorrekturen), 7 nicht bestätigt, 5 vom Auftraggeber entschieden; G03: 20 bestätigte Sollbefunde; Mehrheit der drei Prüfer aus `mehrheit.md` für alle Kennungen nachvollzogen, 0 Abweichungen |
| Einzelbefunde gegen Gutachtendateien | 4418 Einzelbefunde, Kennungen GB und KK in allen 48 Gutachten gleich (0 Abweichungen); Feld Source in allen erkannt, 114 Einträge nennen nur ZF |
| Zuordnungsmehrheit aus den drei Zuordnungsläufen (alle 48 Gutachten, alle Sollbefunde, 7128 Einzelantworten) | Mehrheitsantwort in jeder Zeile gleich `mehrheit.md`; keine Zeile ohne Mehrheit, kein "unklar". In 3 Zeilen listet `mehrheit.md` unter "Einträge mit Mehrheit" zusätzlich einen Eintrag, den nur ein Lauf als getroffen und ein zweiter als teilweise nennt (L01 4695-RC1-07 GB-14, L18 4733-RC1-13 GB-22, L45 5046-RC2-03 GB-39); ohne Folge, weil diese Einträge über andere Sollbefunde ohnehin zutreffend sind |
| zutreffend nach Zuordnung (von mindestens 2 Läufen für denselben Sollbefund als getroffen genannt) | 676 Einzelbefunde; strittig 3742, gleich der Kennzeichnung in `einzelbefunde.json` (0 Unterschiede) |
| Befundgruppen | 896 Gruppen, 3742 Einzelbefunde je genau einmal, jede Zufallskennung auf einen strittigen Befund des richtigen Manuskripts |
| KI-Mehrheit aus den drei Einstufungsläufen (alle 896 Gruppen) | gleich `mehrheit.json` in Urteilen und Mehrheit (0 Abweichungen); 3 ohne Mehrheit, 3 mit Mehrheit "unklar" |
| Ziehung der Stichprobe | mit `random.Random(202610221)`, je Bedingung `sample(sortierte Kennungen, 15)` aus einem Generator nachgezogen: gleich `gezogen.json` (ja); 15 je Bedingung; alle aus Gruppen mit Mehrheit zutreffend, nicht zutreffend oder Ansichtssache; Teil 2 der Erfassung gleich den 6 Gruppen ohne Mehrheit oder mit "unklar" |
| endgültige Urteile (KI-Mehrheit, Auftraggeber für 6 Gruppen, Abweichungen der Stichprobe für die ganze Gruppe) | eigene Ableitung gleich `endgueltig_einzelbefunde.json` (0 Abweichungen bei 4418) und `endgueltig_gruppen.json` (0 bei 896) |
| K8-Mehrheit (Fall zählt, wenn mindestens 2 von 3 Zählern ihn nennen) | gleich `k8/mehrheit.json` in allen 384 Werten; der Median der drei Zählungen je Klasse ergäbe nur in L33 (A, 4506, Lauf 3) einen Fall weniger (8 statt 9; A Lauf 3: 6,50 statt 6,75 je Gutachten) |
| K4 aus der Schlusszeile des Prüfberichts | in 25 Prüfberichten maschinell lesbar, dort gleich der Zählermehrheit |

## 3. Tabellen je Kennzahl

Spalten: nachgerechnet, geliefert (Trefferbilanz), gleich. Anteile in Prozent, Zählgrößen in Fällen je Gutachten.

Festlegungen, wo das Protokoll eine Zählung nicht ausschreibt: Ein Sollbefund ist getroffen oder teilweise, wenn mindestens zwei der drei Zuordnungsläufe das sagen. Ein Befund ist zutreffend nach Zuordnung, wenn mindestens zwei Läufe ihn für denselben Sollbefund als getroffen nennen; alle übrigen sind strittig und übernehmen das Urteil ihrer Gruppe. K2 und K6 beziehen sich auf alle Einträge (Befunde und Kleinkorrekturen) mit endgültigem Urteil. K3: Befund ohne Sollbefund heißt, kein Sollbefund mit Mehrheit getroffen oder teilweise, für den mindestens zwei Läufe diesen Befund nennen (Variante b; Variante a steht unten). Ohne G03 entfallen die Sollbefunde 4506-RC3-nn aus Zähler, Nenner und Zuordnung; die Einstufung der Befunde bleibt. K6 zählt Einträge, deren Feld Source genau eine der Instanzen S1 bis S4, AB, SD nennt; Einträge nur mit ZF stehen im Nenner. K4 und K8: Fall zählt, wenn mindestens zwei der drei Zähler ihn nennen. Zählgrößen je Lauf als Mittel über die vier Gutachten.

### K1 inhaltlich, getroffen (Hauptmaß) (mit G03)

| Bedingung, Größe | nachgerechnet | geliefert | gleich |
|---|---|---|---|
| A, Mittel | 29,14 | 29,1 | ja |
| A, min | 23,78 | 23,8 | ja |
| A, max | 33,57 | 33,6 | ja |
| B, Mittel | 28,67 | 28,7 | ja |
| B, min | 25,17 | 25,2 | ja |
| B, max | 30,77 | 30,8 | ja |
| C, Mittel | 21,91 | 21,9 | ja |
| C, min | 21,68 | 21,7 | ja |
| C, max | 22,38 | 22,4 | ja |
| D, Mittel | 27,74 | 27,7 | ja |
| D, min | 25,87 | 25,9 | ja |
| D, max | 30,77 | 30,8 | ja |

### K1 inhaltlich, teilweise (mit G03)

| Bedingung, Größe | nachgerechnet | geliefert | gleich |
|---|---|---|---|
| A, Mittel | 32,17 | 32,2 | ja |
| A, min | 28,67 | 28,7 | ja |
| A, max | 37,06 | 37,1 | ja |
| B, Mittel | 31,00 | 31,0 | ja |
| B, min | 28,67 | 28,7 | ja |
| B, max | 34,97 | 35,0 | ja |
| C, Mittel | 29,84 | 29,8 | ja |
| C, min | 25,87 | 25,9 | ja |
| C, max | 35,66 | 35,7 | ja |
| D, Mittel | 30,77 | 30,8 | ja |
| D, min | 30,07 | 30,1 | ja |
| D, max | 31,47 | 31,5 | ja |

### K1 Kleinkorrekturen, getroffen (mit G03)

| Bedingung, Größe | nachgerechnet | geliefert | gleich |
|---|---|---|---|
| A, Mittel | 65,45 | 65,5 | ja |
| A, min | 60 | 60 | ja |
| A, max | 69,09 | 69,1 | ja |
| B, Mittel | 64,24 | 64,2 | ja |
| B, min | 61,82 | 61,8 | ja |
| B, max | 67,27 | 67,3 | ja |
| C, Mittel | 46,06 | 46,1 | ja |
| C, min | 45,45 | 45,5 | ja |
| C, max | 47,27 | 47,3 | ja |
| D, Mittel | 66,67 | 66,7 | ja |
| D, min | 65,45 | 65,5 | ja |
| D, max | 69,09 | 69,1 | ja |

### K1 Kleinkorrekturen, teilweise (mit G03)

| Bedingung, Größe | nachgerechnet | geliefert | gleich |
|---|---|---|---|
| A, Mittel | 7,27 | 7,3 | ja |
| A, min | 5,45 | 5,5 | ja |
| A, max | 9,09 | 9,1 | ja |
| B, Mittel | 9,70 | 9,7 | ja |
| B, min | 7,27 | 7,3 | ja |
| B, max | 10,91 | 10,9 | ja |
| C, Mittel | 6,06 | 6,1 | ja |
| C, min | 3,64 | 3,6 | ja |
| C, max | 9,09 | 9,1 | ja |
| D, Mittel | 6,67 | 6,7 | ja |
| D, min | 5,45 | 5,5 | ja |
| D, max | 7,27 | 7,3 | ja |

### K2 nicht zutreffend, Anteil an allen Einträgen (mit G03)

| Bedingung, Größe | nachgerechnet | geliefert | gleich |
|---|---|---|---|
| A, Mittel | 0,68 | 0,7 | ja |
| A, min | 0,43 | 0,4 | ja |
| A, max | 0,93 | 0,9 | ja |
| B, Mittel | 0,58 | 0,6 | ja |
| B, min | 0,50 | 0,5 | ja |
| B, max | 0,74 | 0,7 | ja |
| C, Mittel | 0,48 | 0,5 | ja |
| C, min | 0 | 0 | ja |
| C, max | 1,45 | 1,4 | ja |
| D, Mittel | 0,08 | 0,1 | ja |
| D, min | 0 | 0 | ja |
| D, max | 0,25 | 0,3 | ja |

### K2 ergänzend: Ansichtssache, Anteil (mit G03)

| Bedingung, Größe | nachgerechnet | geliefert | gleich |
|---|---|---|---|
| A, Mittel | 5,76 | 5,8 | ja |
| A, min | 4,65 | 4,7 | ja |
| A, max | 6,51 | 6,5 | ja |
| B, Mittel | 4,58 | 4,6 | ja |
| B, min | 3,06 | 3,1 | ja |
| B, max | 5,96 | 6,0 | ja |
| C, Mittel | 1,77 | 1,8 | ja |
| C, min | 1,36 | 1,4 | ja |
| C, max | 2,50 | 2,5 | ja |
| D, Mittel | 5,09 | 5,1 | ja |
| D, min | 4,26 | 4,3 | ja |
| D, max | 6,02 | 6,0 | ja |

### K3 Zusatzbefunde je Gutachten (Anzahl) (mit G03)

| Bedingung, Größe | nachgerechnet | geliefert | gleich |
|---|---|---|---|
| A, Mittel | 75,083 | 75,10 | ja |
| A, min | 72,500 | 72,50 | ja |
| A, max | 77,750 | 77,80 | ja |
| B, Mittel | 66,667 | 66,70 | ja |
| B, min | 65,500 | 65,50 | ja |
| B, max | 68,250 | 68,20 | ja |
| C, Mittel | 36,833 | 36,80 | ja |
| C, min | 33,250 | 33,20 | ja |
| C, max | 39,750 | 39,80 | ja |
| D, Mittel | 69,583 | 69,60 | ja |
| D, min | 67,250 | 67,20 | ja |
| D, max | 72,750 | 72,80 | ja |

### K7 Zuordnung, drei Läufe gleich (mit G03)

| Bedingung, Größe | nachgerechnet | geliefert | gleich |
|---|---|---|---|
| A, Mittel | 91,08 | 91,1 | ja |
| A, min | 86,87 | 86,9 | ja |
| A, max | 94,44 | 94,4 | ja |
| B, Mittel | 92,26 | 92,3 | ja |
| B, min | 91,41 | 91,4 | ja |
| B, max | 93,43 | 93,4 | ja |
| C, Mittel | 92,76 | 92,8 | ja |
| C, min | 92,42 | 92,4 | ja |
| C, max | 93,43 | 93,4 | ja |
| D, Mittel | 92,76 | 92,8 | ja |
| D, min | 90,40 | 90,4 | ja |
| D, max | 95,96 | 96,0 | ja |

### K1 inhaltlich getroffen 4506 (mit G03)

| Bedingung, Größe | nachgerechnet | geliefert | gleich |
|---|---|---|---|
| A, Mittel | 32,26 | 32,3 | ja |
| A, min | 25,81 | 25,8 | ja |
| A, max | 41,94 | 41,9 | ja |
| B, Mittel | 36,56 | 36,6 | ja |
| B, min | 29,03 | 29,0 | ja |
| B, max | 41,94 | 41,9 | ja |
| C, Mittel | 23,66 | 23,7 | ja |
| C, min | 22,58 | 22,6 | ja |
| C, max | 25,81 | 25,8 | ja |
| D, Mittel | 35,48 | 35,5 | ja |
| D, min | 32,26 | 32,3 | ja |
| D, max | 38,71 | 38,7 | ja |

### K1 inhaltlich getroffen 4695 (mit G03)

| Bedingung, Größe | nachgerechnet | geliefert | gleich |
|---|---|---|---|
| A, Mittel | 43,14 | 43,1 | ja |
| A, min | 35,29 | 35,3 | ja |
| A, max | 47,06 | 47,1 | ja |
| B, Mittel | 37,25 | 37,3 | ja |
| B, min | 29,41 | 29,4 | ja |
| B, max | 41,18 | 41,2 | ja |
| C, Mittel | 41,18 | 41,2 | ja |
| C, min | 35,29 | 35,3 | ja |
| C, max | 47,06 | 47,1 | ja |
| D, Mittel | 41,18 | 41,2 | ja |
| D, min | 35,29 | 35,3 | ja |
| D, max | 47,06 | 47,1 | ja |

### K1 inhaltlich getroffen 4733 (mit G03)

| Bedingung, Größe | nachgerechnet | geliefert | gleich |
|---|---|---|---|
| A, Mittel | 23,33 | 23,3 | ja |
| A, min | 15 | 15 | ja |
| A, max | 35 | 35 | ja |
| B, Mittel | 16,67 | 16,7 | ja |
| B, min | 10 | 10 | ja |
| B, max | 30 | 30 | ja |
| C, Mittel | 15 | 15 | ja |
| C, min | 10 | 10 | ja |
| C, max | 20 | 20 | ja |
| D, Mittel | 13,33 | 13,3 | ja |
| D, min | 5 | 5 | ja |
| D, max | 20 | 20 | ja |

### K1 inhaltlich getroffen 5046 (mit G03)

| Bedingung, Größe | nachgerechnet | geliefert | gleich |
|---|---|---|---|
| A, Mittel | 26,22 | 26,2 | ja |
| A, min | 20 | 20 | ja |
| A, max | 30,67 | 30,7 | ja |
| B, Mittel | 26,67 | 26,7 | ja |
| B, min | 24 | 24 | ja |
| B, max | 30,67 | 30,7 | ja |
| C, Mittel | 18,67 | 18,7 | ja |
| C, min | 18,67 | 18,7 | ja |
| C, max | 18,67 | 18,7 | ja |
| D, Mittel | 25,33 | 25,3 | ja |
| D, min | 24 | 24 | ja |
| D, max | 28 | 28 | ja |

### K1 inhaltlich, getroffen (Hauptmaß) (ohne G03)

| Bedingung, Größe | nachgerechnet | geliefert | gleich |
|---|---|---|---|
| A, Mittel | 28,49 | 28,5 | ja |
| A, min | 23,39 | 23,4 | ja |
| A, max | 32,26 | 32,3 | ja |
| B, Mittel | 26,34 | 26,3 | ja |
| B, min | 24,19 | 24,2 | ja |
| B, max | 28,23 | 28,2 | ja |
| C, Mittel | 21,24 | 21,2 | ja |
| C, min | 20,97 | 21,0 | ja |
| C, max | 21,77 | 21,8 | ja |
| D, Mittel | 25,27 | 25,3 | ja |
| D, min | 23,39 | 23,4 | ja |
| D, max | 28,23 | 28,2 | ja |

### K1 inhaltlich, teilweise (ohne G03)

| Bedingung, Größe | nachgerechnet | geliefert | gleich |
|---|---|---|---|
| A, Mittel | 30,11 | 30,1 | ja |
| A, min | 25,81 | 25,8 | ja |
| A, max | 35,48 | 35,5 | ja |
| B, Mittel | 28,76 | 28,8 | ja |
| B, min | 25 | 25 | ja |
| B, max | 34,68 | 34,7 | ja |
| C, Mittel | 26,88 | 26,9 | ja |
| C, min | 24,19 | 24,2 | ja |
| C, max | 32,26 | 32,3 | ja |
| D, Mittel | 28,49 | 28,5 | ja |
| D, min | 28,23 | 28,2 | ja |
| D, max | 29,03 | 29,0 | ja |

### K1 Kleinkorrekturen, getroffen (ohne G03)

| Bedingung, Größe | nachgerechnet | geliefert | gleich |
|---|---|---|---|
| A, Mittel | 66,05 | 66,0 | ja |
| A, min | 61,11 | 61,1 | ja |
| A, max | 70,37 | 70,4 | ja |
| B, Mittel | 64,20 | 64,2 | ja |
| B, min | 61,11 | 61,1 | ja |
| B, max | 66,67 | 66,7 | ja |
| C, Mittel | 46,91 | 46,9 | ja |
| C, min | 46,30 | 46,3 | ja |
| C, max | 48,15 | 48,1 | ja |
| D, Mittel | 67,28 | 67,3 | ja |
| D, min | 66,67 | 66,7 | ja |
| D, max | 68,52 | 68,5 | ja |

### K1 Kleinkorrekturen, teilweise (ohne G03)

| Bedingung, Größe | nachgerechnet | geliefert | gleich |
|---|---|---|---|
| A, Mittel | 6,17 | 6,2 | ja |
| A, min | 3,70 | 3,7 | ja |
| A, max | 7,41 | 7,4 | ja |
| B, Mittel | 9,26 | 9,3 | ja |
| B, min | 7,41 | 7,4 | ja |
| B, max | 11,11 | 11,1 | ja |
| C, Mittel | 4,32 | 4,3 | ja |
| C, min | 1,85 | 1,9 | ja |
| C, max | 7,41 | 7,4 | ja |
| D, Mittel | 5,56 | 5,6 | ja |
| D, min | 3,70 | 3,7 | ja |
| D, max | 7,41 | 7,4 | ja |

### K2 nicht zutreffend, Anteil an allen Einträgen (ohne G03)

| Bedingung, Größe | nachgerechnet | geliefert | gleich |
|---|---|---|---|
| A, Mittel | 0,68 | 0,7 | ja |
| A, min | 0,43 | 0,4 | ja |
| A, max | 0,93 | 0,9 | ja |
| B, Mittel | 0,58 | 0,6 | ja |
| B, min | 0,50 | 0,5 | ja |
| B, max | 0,74 | 0,7 | ja |
| C, Mittel | 0,48 | 0,5 | ja |
| C, min | 0 | 0 | ja |
| C, max | 1,45 | 1,4 | ja |
| D, Mittel | 0,08 | 0,1 | ja |
| D, min | 0 | 0 | ja |
| D, max | 0,25 | 0,3 | ja |

### K2 ergänzend: Ansichtssache, Anteil (ohne G03)

| Bedingung, Größe | nachgerechnet | geliefert | gleich |
|---|---|---|---|
| A, Mittel | 5,76 | 5,8 | ja |
| A, min | 4,65 | 4,7 | ja |
| A, max | 6,51 | 6,5 | ja |
| B, Mittel | 4,58 | 4,6 | ja |
| B, min | 3,06 | 3,1 | ja |
| B, max | 5,96 | 6,0 | ja |
| C, Mittel | 1,77 | 1,8 | ja |
| C, min | 1,36 | 1,4 | ja |
| C, max | 2,50 | 2,5 | ja |
| D, Mittel | 5,09 | 5,1 | ja |
| D, min | 4,26 | 4,3 | ja |
| D, max | 6,02 | 6,0 | ja |

### K3 Zusatzbefunde je Gutachten (Anzahl) (ohne G03)

| Bedingung, Größe | nachgerechnet | geliefert | gleich |
|---|---|---|---|
| A, Mittel | 78,917 | 78,90 | ja |
| A, min | 76,750 | 76,80 | ja |
| A, max | 80,500 | 80,50 | ja |
| B, Mittel | 70,167 | 70,20 | ja |
| B, min | 68,250 | 68,20 | ja |
| B, max | 73 | 73 | ja |
| C, Mittel | 39,417 | 39,40 | ja |
| C, min | 35,500 | 35,50 | ja |
| C, max | 43 | 43 | ja |
| D, Mittel | 72,667 | 72,70 | ja |
| D, min | 70,500 | 70,50 | ja |
| D, max | 76,250 | 76,20 | ja |

### K7 Zuordnung, drei Läufe gleich (ohne G03)

| Bedingung, Größe | nachgerechnet | geliefert | gleich |
|---|---|---|---|
| A, Mittel | 92,32 | 92,3 | ja |
| A, min | 88,20 | 88,2 | ja |
| A, max | 95,51 | 95,5 | ja |
| B, Mittel | 92,70 | 92,7 | ja |
| B, min | 92,13 | 92,1 | ja |
| B, max | 93,26 | 93,3 | ja |
| C, Mittel | 93,82 | 93,8 | ja |
| C, min | 93,26 | 93,3 | ja |
| C, max | 94,38 | 94,4 | ja |
| D, Mittel | 93,63 | 93,6 | ja |
| D, min | 92,13 | 92,1 | ja |
| D, max | 96,07 | 96,1 | ja |

### K1 inhaltlich getroffen 4506 (ohne G03)

| Bedingung, Größe | nachgerechnet | geliefert | gleich |
|---|---|---|---|
| A, Mittel | 30,56 | 30,6 | ja |
| A, min | 25 | 25 | ja |
| A, max | 41,67 | 41,7 | ja |
| B, Mittel | 25 | 25 | ja |
| B, min | 25 | 25 | ja |
| B, max | 25 | 25 | ja |
| C, Mittel | 19,44 | 19,4 | ja |
| C, min | 16,67 | 16,7 | ja |
| C, max | 25 | 25 | ja |
| D, Mittel | 22,22 | 22,2 | ja |
| D, min | 16,67 | 16,7 | ja |
| D, max | 25 | 25 | ja |

### K1 inhaltlich getroffen 4695 (ohne G03)

| Bedingung, Größe | nachgerechnet | geliefert | gleich |
|---|---|---|---|
| A, Mittel | 43,14 | 43,1 | ja |
| A, min | 35,29 | 35,3 | ja |
| A, max | 47,06 | 47,1 | ja |
| B, Mittel | 37,25 | 37,3 | ja |
| B, min | 29,41 | 29,4 | ja |
| B, max | 41,18 | 41,2 | ja |
| C, Mittel | 41,18 | 41,2 | ja |
| C, min | 35,29 | 35,3 | ja |
| C, max | 47,06 | 47,1 | ja |
| D, Mittel | 41,18 | 41,2 | ja |
| D, min | 35,29 | 35,3 | ja |
| D, max | 47,06 | 47,1 | ja |

### K1 inhaltlich getroffen 4733 (ohne G03)

| Bedingung, Größe | nachgerechnet | geliefert | gleich |
|---|---|---|---|
| A, Mittel | 23,33 | 23,3 | ja |
| A, min | 15 | 15 | ja |
| A, max | 35 | 35 | ja |
| B, Mittel | 16,67 | 16,7 | ja |
| B, min | 10 | 10 | ja |
| B, max | 30 | 30 | ja |
| C, Mittel | 15 | 15 | ja |
| C, min | 10 | 10 | ja |
| C, max | 20 | 20 | ja |
| D, Mittel | 13,33 | 13,3 | ja |
| D, min | 5 | 5 | ja |
| D, max | 20 | 20 | ja |

### K1 inhaltlich getroffen 5046 (ohne G03)

| Bedingung, Größe | nachgerechnet | geliefert | gleich |
|---|---|---|---|
| A, Mittel | 26,22 | 26,2 | ja |
| A, min | 20 | 20 | ja |
| A, max | 30,67 | 30,7 | ja |
| B, Mittel | 26,67 | 26,7 | ja |
| B, min | 24 | 24 | ja |
| B, max | 30,67 | 30,7 | ja |
| C, Mittel | 18,67 | 18,7 | ja |
| C, min | 18,67 | 18,7 | ja |
| C, max | 18,67 | 18,7 | ja |
| D, Mittel | 25,33 | 25,3 | ja |
| D, min | 24 | 24 | ja |
| D, max | 28 | 28 | ja |

### Einträge je Gutachten

| Bedingung, Größe | nachgerechnet | geliefert | gleich |
|---|---|---|---|
| A, Mittel | 111 | 111 | ja |
| A, min | 107,500 | 107,50 | ja |
| A, max | 115,250 | 115,20 | ja |
| B, Mittel | 99,833 | 99,80 | ja |
| B, min | 98 | 98 | ja |
| B, max | 100,750 | 100,80 | ja |
| C, Mittel | 55,583 | 55,60 | ja |
| C, min | 51,750 | 51,80 | ja |
| C, max | 60 | 60 | ja |
| D, Mittel | 101,750 | 101,80 | ja |
| D, min | 99,750 | 99,80 | ja |
| D, max | 105,750 | 105,80 | ja |

### davon inhaltliche Befunde

| Bedingung, Größe | nachgerechnet | geliefert | gleich |
|---|---|---|---|
| A, Mittel | 59 | 59 | ja |
| A, min | 56 | 56 | ja |
| A, max | 61,750 | 61,80 | ja |
| B, Mittel | 57,917 | 57,90 | ja |
| B, min | 54 | 54 | ja |
| B, max | 60,250 | 60,20 | ja |
| C, Mittel | 33,333 | 33,30 | ja |
| C, min | 31,500 | 31,50 | ja |
| C, max | 35,250 | 35,20 | ja |
| D, Mittel | 58,167 | 58,20 | ja |
| D, min | 55,250 | 55,20 | ja |
| D, max | 60,500 | 60,50 | ja |

### davon Kleinkorrekturen

| Bedingung, Größe | nachgerechnet | geliefert | gleich |
|---|---|---|---|
| A, Mittel | 52 | 52 | ja |
| A, min | 48,250 | 48,20 | ja |
| A, max | 54,250 | 54,20 | ja |
| B, Mittel | 41,917 | 41,90 | ja |
| B, min | 38,500 | 38,50 | ja |
| B, max | 46,750 | 46,80 | ja |
| C, Mittel | 22,250 | 22,20 | ja |
| C, min | 18,500 | 18,50 | ja |
| C, max | 24,750 | 24,80 | ja |
| D, Mittel | 43,583 | 43,60 | ja |
| D, min | 41 | 41 | ja |
| D, max | 45,250 | 45,20 | ja |

### K6 zutreffende Einträge aus nur einer Prüfinstanz

| Bedingung, Größe | nachgerechnet | geliefert | gleich |
|---|---|---|---|
| A, Mittel | 63,30 | 63,3 | ja |
| A, min | 61,33 | 61,3 | ja |
| A, max | 64,57 | 64,6 | ja |
| B, Mittel | 61,08 | 61,1 | ja |
| B, min | 59,52 | 59,5 | ja |
| B, max | 63,61 | 63,6 | ja |
| C, Mittel | 78,97 | 79,0 | ja |
| C, min | 77,61 | 77,6 | ja |
| C, max | 81,11 | 81,1 | ja |
| D, Mittel | 62,52 | 62,5 | ja |
| D, min | 62,40 | 62,4 | ja |
| D, max | 62,70 | 62,7 | ja |

### K5 Spannweite K1 4506

| Bedingung, Größe | nachgerechnet | geliefert | gleich |
|---|---|---|---|
| A | 16,13 | 16,1 | ja |
| B | 12,90 | 12,9 | ja |
| C | 3,23 | 3,2 | ja |
| D | 6,45 | 6,5 | ja |

### K5 Spannweite K1 4695

| Bedingung, Größe | nachgerechnet | geliefert | gleich |
|---|---|---|---|
| A | 11,76 | 11,8 | ja |
| B | 11,76 | 11,8 | ja |
| C | 11,76 | 11,8 | ja |
| D | 11,76 | 11,8 | ja |

### K5 Spannweite K1 4733

| Bedingung, Größe | nachgerechnet | geliefert | gleich |
|---|---|---|---|
| A | 20 | 20 | ja |
| B | 20 | 20 | ja |
| C | 10 | 10 | ja |
| D | 15 | 15 | ja |

### K5 Spannweite K1 5046

| Bedingung, Größe | nachgerechnet | geliefert | gleich |
|---|---|---|---|
| A | 10,67 | 10,7 | ja |
| B | 6,67 | 6,7 | ja |
| C | 0 | 0 | ja |
| D | 4 | 4 | ja |

### K4

| Bedingung, Größe | nachgerechnet | geliefert | gleich |
|---|---|---|---|
| A, Mittel | 1,250 | 1,25 | ja |
| A, min | 0,500 | 0,50 | ja |
| A, max | 2,500 | 2,50 | ja |
| B, Mittel | 0,500 | 0,50 | ja |
| B, min | 0 | 0 | ja |
| B, max | 1 | 1 | ja |
| C, Mittel | 0,417 | 0,42 | ja |
| C, min | 0 | 0 | ja |
| C, max | 1 | 1 | ja |
| D, Mittel | 0,917 | 0,92 | ja |
| D, min | 0,500 | 0,50 | ja |
| D, max | 1,750 | 1,75 | ja |

### F1

| Bedingung, Größe | nachgerechnet | geliefert | gleich |
|---|---|---|---|
| A, Mittel | 0,333 | 0,33 | ja |
| A, min | 0 | 0 | ja |
| A, max | 1 | 1 | ja |
| B, Mittel | 0,333 | 0,33 | ja |
| B, min | 0,250 | 0,25 | ja |
| B, max | 0,500 | 0,50 | ja |
| C, Mittel | 0,083 | 0,08 | ja |
| C, min | 0 | 0 | ja |
| C, max | 0,250 | 0,25 | ja |
| D, Mittel | 0 | 0 | ja |
| D, min | 0 | 0 | ja |
| D, max | 0 | 0 | ja |

### F2

| Bedingung, Größe | nachgerechnet | geliefert | gleich |
|---|---|---|---|
| A, Mittel | 1,917 | 1,92 | ja |
| A, min | 0,750 | 0,75 | ja |
| A, max | 3,250 | 3,25 | ja |
| B, Mittel | 0,917 | 0,92 | ja |
| B, min | 0,750 | 0,75 | ja |
| B, max | 1,250 | 1,25 | ja |
| C, Mittel | 1,167 | 1,17 | ja |
| C, min | 0,250 | 0,25 | ja |
| C, max | 1,750 | 1,75 | ja |
| D, Mittel | 0,250 | 0,25 | ja |
| D, min | 0 | 0 | ja |
| D, max | 0,500 | 0,50 | ja |

### F3

| Bedingung, Größe | nachgerechnet | geliefert | gleich |
|---|---|---|---|
| A, Mittel | 0,833 | 0,83 | ja |
| A, min | 0,250 | 0,25 | ja |
| A, max | 1,250 | 1,25 | ja |
| B, Mittel | 0,417 | 0,42 | ja |
| B, min | 0,250 | 0,25 | ja |
| B, max | 0,500 | 0,50 | ja |
| C, Mittel | 0,500 | 0,50 | ja |
| C, min | 0,250 | 0,25 | ja |
| C, max | 0,750 | 0,75 | ja |
| D, Mittel | 1,167 | 1,17 | ja |
| D, min | 0,750 | 0,75 | ja |
| D, max | 1,500 | 1,50 | ja |

### F4

| Bedingung, Größe | nachgerechnet | geliefert | gleich |
|---|---|---|---|
| A, Mittel | 1,083 | 1,08 | ja |
| A, min | 0,250 | 0,25 | ja |
| A, max | 1,750 | 1,75 | ja |
| B, Mittel | 0,500 | 0,50 | ja |
| B, min | 0,250 | 0,25 | ja |
| B, max | 1 | 1 | ja |
| C, Mittel | 0,833 | 0,83 | ja |
| C, min | 0,500 | 0,50 | ja |
| C, max | 1 | 1 | ja |
| D, Mittel | 0,750 | 0,75 | ja |
| D, min | 0,500 | 0,50 | ja |
| D, max | 1 | 1 | ja |

### F5

| Bedingung, Größe | nachgerechnet | geliefert | gleich |
|---|---|---|---|
| A, Mittel | 0,500 | 0,50 | ja |
| A, min | 0 | 0 | ja |
| A, max | 1,250 | 1,25 | ja |
| B, Mittel | 0,333 | 0,33 | ja |
| B, min | 0 | 0 | ja |
| B, max | 0,500 | 0,50 | ja |
| C, Mittel | 0,750 | 0,75 | ja |
| C, min | 0,500 | 0,50 | ja |
| C, max | 1 | 1 | ja |
| D, Mittel | 0,417 | 0,42 | ja |
| D, min | 0,250 | 0,25 | ja |
| D, max | 0,500 | 0,50 | ja |

### F6

| Bedingung, Größe | nachgerechnet | geliefert | gleich |
|---|---|---|---|
| A, Mittel | 0,333 | 0,33 | ja |
| A, min | 0,250 | 0,25 | ja |
| A, max | 0,500 | 0,50 | ja |
| B, Mittel | 0,083 | 0,08 | ja |
| B, min | 0 | 0 | ja |
| B, max | 0,250 | 0,25 | ja |
| C, Mittel | 0,083 | 0,08 | ja |
| C, min | 0 | 0 | ja |
| C, max | 0,250 | 0,25 | ja |
| D, Mittel | 0 | 0 | ja |
| D, min | 0 | 0 | ja |
| D, max | 0 | 0 | ja |

### F7

| Bedingung, Größe | nachgerechnet | geliefert | gleich |
|---|---|---|---|
| A, Mittel | 1,917 | 1,92 | ja |
| A, min | 1 | 1 | ja |
| A, max | 2,500 | 2,50 | ja |
| B, Mittel | 3,083 | 3,08 | ja |
| B, min | 1,500 | 1,50 | ja |
| B, max | 4,750 | 4,75 | ja |
| C, Mittel | 1,583 | 1,58 | ja |
| C, min | 1,250 | 1,25 | ja |
| C, max | 2,250 | 2,25 | ja |
| D, Mittel | 0,333 | 0,33 | ja |
| D, min | 0 | 0 | ja |
| D, max | 1 | 1 | ja |

### F1 bis F7 zusammen

| Bedingung, Größe | nachgerechnet | geliefert | gleich |
|---|---|---|---|
| A, Mittel | 6,917 | 6,92 | ja |
| A, min | 4,250 | 4,25 | ja |
| A, max | 9,750 | 9,75 | ja |
| B, Mittel | 5,667 | 5,67 | ja |
| B, min | 5,250 | 5,25 | ja |
| B, max | 6,250 | 6,25 | ja |
| C, Mittel | 5 | 5 | ja |
| C, min | 3,500 | 3,50 | ja |
| C, max | 6 | 6 | ja |
| D, Mittel | 2,917 | 2,92 | ja |
| D, min | 2,500 | 2,50 | ja |
| D, max | 3,500 | 3,50 | ja |

### F1 bis F7 je 100 Einträge (ergänzend)

| Bedingung, Größe | nachgerechnet | geliefert | gleich |
|---|---|---|---|
| A, Mittel | 6,260 | 6,26 | ja |
| A, min | 3,855 | 3,85 | ja |
| A, max | 9,070 | 9,07 | ja |
| B, Mittel | 5,683 | 5,68 | ja |
| B, min | 5,211 | 5,21 | ja |
| B, max | 6,378 | 6,38 | ja |
| C, Mittel | 9,143 | 9,14 | ja |
| C, min | 5,833 | 5,83 | ja |
| C, max | 11,594 | 11,59 | ja |
| D, Mittel | 2,858 | 2,86 | ja |
| D, min | 2,506 | 2,51 | ja |
| D, max | 3,310 | 3,31 | ja |

### Einzelwerte (K5 Schweregrade, K7, K8 Zähler, K9, Vorstudie)

| Kennzahl | nachgerechnet | geliefert | gleich |
|---|---|---|---|
| K5 gleiche Schweregrade, A (eigene Hauptdefinition: nur getroffen) | 79,15 | 71,8 | nein |
| K5 gleiche Schweregrade, Paare, A (eigene Hauptdefinition: nur getroffen) | 494 | 691 | nein |
| K5 gleiche Schweregrade, B (eigene Hauptdefinition: nur getroffen) | 73,81 | 68,1 | nein |
| K5 gleiche Schweregrade, Paare, B (eigene Hauptdefinition: nur getroffen) | 527 | 756 | nein |
| K5 gleiche Schweregrade, C (eigene Hauptdefinition: nur getroffen) | 79,25 | 72,8 | nein |
| K5 gleiche Schweregrade, Paare, C (eigene Hauptdefinition: nur getroffen) | 265 | 375 | nein |
| K5 gleiche Schweregrade, D (eigene Hauptdefinition: nur getroffen) | 76,29 | 70,0 | nein |
| K5 gleiche Schweregrade, Paare, D (eigene Hauptdefinition: nur getroffen) | 502 | 680 | nein |
| K7 Einstufung, Anteil Gruppen mit KI-Mehrheit (Mehrheit "unklar" mitgezählt) | 99,67 | 99,3 | nein |
| K7 Stichprobe gesamt | 95 | 95 | ja |
| K7 Stichprobe A, gleiche Urteile | 14 | 14 | ja |
| K7 Stichprobe B, gleiche Urteile | 14 | 14 | ja |
| K7 Stichprobe C, gleiche Urteile | 14 | 14 | ja |
| K7 Stichprobe D, gleiche Urteile | 15 | 15 | ja |
| K8 Zähler, Fälle von allen drei genannt | 256 | 256 | ja |
| K8 Zähler, genannte Fälle | 315 | 315 | ja |
| K9 vorgeschlagene Regeln | 7 | 7 | ja |
| K9 Anteil bestätigt | 100 | 100 | ja |
| K9 Anteil der Fälle einer Klasse zugeordnet | 63,46 | 63,5 | ja |
| K9 Fälle, die R und R2 beide sammeln | 52 | 44 | nein |
| K9 Anteil Fallpaare gleich gruppiert | 93,59 | 94,8 | nein |
| Vorstudie V1-LAM-1 Sollbefunde | 46 | 46 | ja |
| Vorstudie V1-LAM-1 getroffen (alle Arten) | 18 | 18 | ja |
| Vorstudie V1-LAM-1 teilweise (alle Arten) | 12 | 12 | ja |
| Vorstudie V1-LAM-1 getroffen in % (alle Arten) | 39,13 | 39,1 | ja |
| Vorstudie V1-LAM-1 getroffen oder teilweise in % | 65,22 | 65,2 | ja |
| Vorstudie V1-LAM-1 drei Läufe gleich | 44 | 44 | ja |
| Vorstudie V1-LAM-2 Sollbefunde | 46 | 46 | ja |
| Vorstudie V1-LAM-2 getroffen (alle Arten) | 20 | 20 | ja |
| Vorstudie V1-LAM-2 teilweise (alle Arten) | 7 | 7 | ja |
| Vorstudie V1-LAM-2 getroffen in % (alle Arten) | 43,48 | 43,5 | ja |
| Vorstudie V1-LAM-2 getroffen oder teilweise in % | 58,70 | 58,7 | ja |
| Vorstudie V1-LAM-2 drei Läufe gleich | 44 | 44 | ja |
| Vorstudie V1-TCD-1 Sollbefunde | 52 | 52 | ja |
| Vorstudie V1-TCD-1 getroffen (alle Arten) | 25 | 25 | ja |
| Vorstudie V1-TCD-1 teilweise (alle Arten) | 13 | 13 | ja |
| Vorstudie V1-TCD-1 getroffen in % (alle Arten) | 48,08 | 48,1 | ja |
| Vorstudie V1-TCD-1 getroffen oder teilweise in % | 73,08 | 73,1 | ja |
| Vorstudie V1-TCD-1 drei Läufe gleich | 49 | 49 | ja |
| Vorstudie V1-HOR-1 Sollbefunde | 51 | 51 | ja |
| Vorstudie V1-HOR-1 getroffen (alle Arten) | 26 | 26 | ja |
| Vorstudie V1-HOR-1 teilweise (alle Arten) | 7 | 7 | ja |
| Vorstudie V1-HOR-1 getroffen in % (alle Arten) | 50,98 | 51,0 | ja |
| Vorstudie V1-HOR-1 getroffen oder teilweise in % | 64,71 | 64,7 | ja |
| Vorstudie V1-HOR-1 drei Läufe gleich | 46 | 46 | ja |
| Vorstudie V2-LAM-1 Sollbefunde | 46 | 46 | ja |
| Vorstudie V2-LAM-1 getroffen (alle Arten) | 25 | 25 | ja |
| Vorstudie V2-LAM-1 teilweise (alle Arten) | 10 | 10 | ja |
| Vorstudie V2-LAM-1 getroffen in % (alle Arten) | 54,35 | 54,3 | ja |
| Vorstudie V2-LAM-1 getroffen oder teilweise in % | 76,09 | 76,1 | ja |
| Vorstudie V2-LAM-1 drei Läufe gleich | 45 | 45 | ja |
| Vorstudie V2-TCD-1 Sollbefunde | 52 | 52 | ja |
| Vorstudie V2-TCD-1 getroffen (alle Arten) | 36 | 36 | ja |
| Vorstudie V2-TCD-1 teilweise (alle Arten) | 8 | 8 | ja |
| Vorstudie V2-TCD-1 getroffen in % (alle Arten) | 69,23 | 69,2 | ja |
| Vorstudie V2-TCD-1 getroffen oder teilweise in % | 84,62 | 84,6 | ja |
| Vorstudie V2-TCD-1 drei Läufe gleich | 48 | 48 | ja |
| Vorstudie V2-HOR-1 Sollbefunde | 51 | 51 | ja |
| Vorstudie V2-HOR-1 getroffen (alle Arten) | 27 | 27 | ja |
| Vorstudie V2-HOR-1 teilweise (alle Arten) | 8 | 8 | ja |
| Vorstudie V2-HOR-1 getroffen in % (alle Arten) | 52,94 | 52,9 | ja |
| Vorstudie V2-HOR-1 getroffen oder teilweise in % | 68,63 | 68,6 | ja |
| Vorstudie V2-HOR-1 drei Läufe gleich | 50 | 50 | ja |
| Vorstudie V3-LAM-1 Sollbefunde | 46 | 46 | ja |
| Vorstudie V3-LAM-1 getroffen (alle Arten) | 23 | 23 | ja |
| Vorstudie V3-LAM-1 teilweise (alle Arten) | 10 | 10 | ja |
| Vorstudie V3-LAM-1 getroffen in % (alle Arten) | 50 | 50 | ja |
| Vorstudie V3-LAM-1 getroffen oder teilweise in % | 71,74 | 71,7 | ja |
| Vorstudie V3-LAM-1 drei Läufe gleich | 41 | 41 | ja |
| Vorstudie V3-LAM-2 Sollbefunde | 46 | 46 | ja |
| Vorstudie V3-LAM-2 getroffen (alle Arten) | 28 | 28 | ja |
| Vorstudie V3-LAM-2 teilweise (alle Arten) | 10 | 10 | ja |
| Vorstudie V3-LAM-2 getroffen in % (alle Arten) | 60,87 | 60,9 | ja |
| Vorstudie V3-LAM-2 getroffen oder teilweise in % | 82,61 | 82,6 | ja |
| Vorstudie V3-LAM-2 drei Läufe gleich | 45 | 45 | ja |
| Vorstudie V3-TCD-1 Sollbefunde | 52 | 52 | ja |
| Vorstudie V3-TCD-1 getroffen (alle Arten) | 34 | 34 | ja |
| Vorstudie V3-TCD-1 teilweise (alle Arten) | 8 | 8 | ja |
| Vorstudie V3-TCD-1 getroffen in % (alle Arten) | 65,38 | 65,4 | ja |
| Vorstudie V3-TCD-1 getroffen oder teilweise in % | 80,77 | 80,8 | ja |
| Vorstudie V3-TCD-1 drei Läufe gleich | 50 | 50 | ja |
| Vorstudie V3-HOR-1 Sollbefunde | 51 | 51 | ja |
| Vorstudie V3-HOR-1 getroffen (alle Arten) | 33 | 33 | ja |
| Vorstudie V3-HOR-1 teilweise (alle Arten) | 8 | 8 | ja |
| Vorstudie V3-HOR-1 getroffen in % (alle Arten) | 64,71 | 64,7 | ja |
| Vorstudie V3-HOR-1 getroffen oder teilweise in % | 80,39 | 80,4 | ja |
| Vorstudie V3-HOR-1 drei Läufe gleich | 49 | 49 | ja |
| Vorstudie V4-LAM-1 Sollbefunde | 46 | 46 | ja |
| Vorstudie V4-LAM-1 getroffen (alle Arten) | 25 | 25 | ja |
| Vorstudie V4-LAM-1 teilweise (alle Arten) | 9 | 9 | ja |
| Vorstudie V4-LAM-1 getroffen in % (alle Arten) | 54,35 | 54,3 | ja |
| Vorstudie V4-LAM-1 getroffen oder teilweise in % | 73,91 | 73,9 | ja |
| Vorstudie V4-LAM-1 drei Läufe gleich | 46 | 46 | ja |
| Vorstudie V4-LAM-2 Sollbefunde | 46 | 46 | ja |
| Vorstudie V4-LAM-2 getroffen (alle Arten) | 22 | 22 | ja |
| Vorstudie V4-LAM-2 teilweise (alle Arten) | 10 | 10 | ja |
| Vorstudie V4-LAM-2 getroffen in % (alle Arten) | 47,83 | 47,8 | ja |
| Vorstudie V4-LAM-2 getroffen oder teilweise in % | 69,57 | 69,6 | ja |
| Vorstudie V4-LAM-2 drei Läufe gleich | 44 | 44 | ja |
| Vorstudie V4-TCD-1 Sollbefunde | 52 | 52 | ja |
| Vorstudie V4-TCD-1 getroffen (alle Arten) | 38 | 38 | ja |
| Vorstudie V4-TCD-1 teilweise (alle Arten) | 10 | 10 | ja |
| Vorstudie V4-TCD-1 getroffen in % (alle Arten) | 73,08 | 73,1 | ja |
| Vorstudie V4-TCD-1 getroffen oder teilweise in % | 92,31 | 92,3 | ja |
| Vorstudie V4-TCD-1 drei Läufe gleich | 49 | 49 | ja |
| Vorstudie V4-HOR-1 Sollbefunde | 51 | 51 | ja |
| Vorstudie V4-HOR-1 getroffen (alle Arten) | 32 | 32 | ja |
| Vorstudie V4-HOR-1 teilweise (alle Arten) | 9 | 9 | ja |
| Vorstudie V4-HOR-1 getroffen in % (alle Arten) | 62,75 | 62,7 | ja |
| Vorstudie V4-HOR-1 getroffen oder teilweise in % | 80,39 | 80,4 | ja |
| Vorstudie V4-HOR-1 drei Läufe gleich | 46 | 46 | ja |
| Vorstudie V1 getroffen in % (alle Arten, gepoolt) | 45,64 | 45,6 | ja |
| Vorstudie V1 getroffen oder teilweise in % | 65,64 | 65,6 | ja |
| Vorstudie V2 getroffen in % (alle Arten, gepoolt) | 59,06 | 59,1 | ja |
| Vorstudie V2 getroffen oder teilweise in % | 76,51 | 76,5 | ja |
| Vorstudie V3 getroffen in % (alle Arten, gepoolt) | 60,51 | 60,5 | ja |
| Vorstudie V3 getroffen oder teilweise in % | 78,97 | 79,0 | ja |
| Vorstudie V4 getroffen in % (alle Arten, gepoolt) | 60 | 60 | ja |
| Vorstudie V4 getroffen oder teilweise in % | 79,49 | 79,5 | ja |
| Vorstudie K7 gesamt | 94,82 | 94,8 | ja |

### Nachgerechnete Werte ohne Gegenstück in der Lieferung

| Kennzahl | Wert |
|---|---|
| K7 Einstufung, Gruppen mit KI-Mehrheit je Bedingung (Gruppen mit mindestens einem Befund der Bedingung) | A 99,84 % von 643, B 99,83 % von 577, C 100,00 % von 311, D 99,83 % von 579 |
| K3 Variante a (mit G03): Zusatzbefund = kein Treffer nach Zuordnungsmehrheit, auch "teilweise" genannte, Einstufung zutreffend | A 88,33 (85,00 bis 92,25); B 79,33 (77,75 bis 81,75); C 44,33 (39,75 bis 48,75); D 81,00 (78,00 bis 85,25) |
| K3 Variante a (ohne G03): Zusatzbefund = kein Treffer nach Zuordnungsmehrheit, auch "teilweise" genannte, Einstufung zutreffend | A 89,92 (87,00 bis 93,25); B 81,50 (80,00 bis 83,25); C 45,33 (41,25 bis 49,75); D 83,08 (80,25 bis 87,25) |
| K5 Spannweite K1 Hauptmaß, gepoolt (mit G03), Prozentpunkte | A 9,8; B 5,6; C 0,7; D 4,9 |
| K5 Spannweite K1 Hauptmaß, gepoolt (ohne G03), Prozentpunkte | A 8,9; B 4,0; C 0,8; D 4,8 |
| K9 Fallpaare gleich gruppiert, nur Fälle, die beide Läufe einer Klasse zuordnen | 253 von 253 (100,0 %), 23 Fälle |
| K9 Fälle R und R2 | R 52 gesammelt, 33 klassiert; R2 54 gesammelt, 23 klassiert; nur in R2: Nr. 47, 48 (LAM_B GB-08 und GB-42, Literatur bereits im Verzeichnis) |

Vorstudie, K1 getrennt nach Art (Protokoll Abschnitt 8: inhaltlich und Kleinkorrekturen getrennt; die Trefferbilanz berichtet nur beide zusammen):

| Lauf | inhaltlich getroffen | inhaltlich teilweise | Kleinkorrekturen getroffen | Kleinkorrekturen teilweise | drei Läufe gleich |
|---|---|---|---|---|---|
| V1-HOR-1 | 16 von 34 (47,1 %) | 6 (17,6 %) | 10 von 17 (58,8 %) | 1 | 46 von 51 |
| V1-LAM-1 | 17 von 40 (42,5 %) | 12 (30,0 %) | 1 von 6 (16,7 %) | 0 | 44 von 46 |
| V1-LAM-2 | 19 von 40 (47,5 %) | 7 (17,5 %) | 1 von 6 (16,7 %) | 0 | 44 von 46 |
| V1-TCD-1 | 25 von 50 (50,0 %) | 13 (26,0 %) | 0 von 2 (0,0 %) | 0 | 49 von 52 |
| V2-HOR-1 | 17 von 34 (50,0 %) | 7 (20,6 %) | 10 von 17 (58,8 %) | 1 | 50 von 51 |
| V2-LAM-1 | 24 von 40 (60,0 %) | 10 (25,0 %) | 1 von 6 (16,7 %) | 0 | 45 von 46 |
| V2-TCD-1 | 36 von 50 (72,0 %) | 8 (16,0 %) | 0 von 2 (0,0 %) | 0 | 48 von 52 |
| V3-HOR-1 | 22 von 34 (64,7 %) | 6 (17,6 %) | 11 von 17 (64,7 %) | 2 | 49 von 51 |
| V3-LAM-1 | 21 von 40 (52,5 %) | 10 (25,0 %) | 2 von 6 (33,3 %) | 0 | 41 von 46 |
| V3-LAM-2 | 26 von 40 (65,0 %) | 10 (25,0 %) | 2 von 6 (33,3 %) | 0 | 45 von 46 |
| V3-TCD-1 | 34 von 50 (68,0 %) | 8 (16,0 %) | 0 von 2 (0,0 %) | 0 | 50 von 52 |
| V4-HOR-1 | 20 von 34 (58,8 %) | 8 (23,5 %) | 12 von 17 (70,6 %) | 1 | 46 von 51 |
| V4-LAM-1 | 23 von 40 (57,5 %) | 9 (22,5 %) | 2 von 6 (33,3 %) | 0 | 46 von 46 |
| V4-LAM-2 | 21 von 40 (52,5 %) | 10 (25,0 %) | 1 von 6 (16,7 %) | 0 | 44 von 46 |
| V4-TCD-1 | 38 von 50 (76,0 %) | 10 (20,0 %) | 0 von 2 (0,0 %) | 0 | 49 von 52 |

| Durchgang | Gutachten | K1 inhaltlich getroffen, gepoolt | Mittel der Gutachten | K1 inhaltlich teilweise, gepoolt | K1 Kleinkorrekturen getroffen, gepoolt | K7 Zuordnung gleich |
|---|---|---|---|---|---|---|
| V1 | 4 | 47,0 % | 46,8 % | 23,2 % | 38,7 % | 93,8 % |
| V2 | 3 | 62,1 % | 60,7 % | 20,2 % | 44,0 % | 96,0 % |
| V3 | 4 | 62,8 % | 62,6 % | 20,7 % | 48,4 % | 94,9 % |
| V4 | 4 | 62,2 % | 61,2 % | 22,6 % | 48,4 % | 94,9 % |

Sollbefunde der Vorstudie: 162 Einwände, 149 bestätigt (124 inhaltlich, 25 Kleinkorrekturen), gleich Nachtrag 3 vom 2026-10-17. Zuordnungsmehrheit in allen 15 Gutachten gleich `mehrheit.md` (0 Abweichungen), keine Zeile ohne Mehrheit.

## 4. Abweichungen über 0,05

| Nr. | Kennzahl | nachgerechnet | geliefert | Ursache |
|---|---|---|---|---|
| 1 | K5 gleiche Schweregrade, A (eigene Hauptdefinition: nur getroffen) | 79,15 | 71,8 | Definition "gemeinsame Befunde" nicht im Protokoll festgelegt. Eigene Hauptdefinition: gleicher Sollbefund nur bei Mehrheit "getroffen" (oder gleiche Befundgruppe). Die Lieferung nimmt auch Sollbefunde mit Mehrheit "teilweise" und die dort von 2 Läufen genannten Einträge hinzu; mit dieser Variante reproduziert die Nachrechnung alle 8 Werte exakt (Abschnitt 5). |
| 2 | K5 gleiche Schweregrade, Paare, A (eigene Hauptdefinition: nur getroffen) | 494 | 691 | wie Nr. 1 |
| 3 | K5 gleiche Schweregrade, B (eigene Hauptdefinition: nur getroffen) | 73,81 | 68,1 | wie Nr. 1 |
| 4 | K5 gleiche Schweregrade, Paare, B (eigene Hauptdefinition: nur getroffen) | 527 | 756 | wie Nr. 1 |
| 5 | K5 gleiche Schweregrade, C (eigene Hauptdefinition: nur getroffen) | 79,25 | 72,8 | wie Nr. 1 |
| 6 | K5 gleiche Schweregrade, Paare, C (eigene Hauptdefinition: nur getroffen) | 265 | 375 | wie Nr. 1 |
| 7 | K5 gleiche Schweregrade, D (eigene Hauptdefinition: nur getroffen) | 76,29 | 70,0 | wie Nr. 1 |
| 8 | K5 gleiche Schweregrade, Paare, D (eigene Hauptdefinition: nur getroffen) | 502 | 680 | wie Nr. 1 |
| 9 | K7 Einstufung, Anteil Gruppen mit KI-Mehrheit (Mehrheit "unklar" mitgezählt) | 99,67 | 99,3 | Die Lieferung zählt die 3 Gruppen mit Mehrheit "unklar" als Gruppen ohne Mehrheit (890 von 896). Das Protokoll (Abschnitt 8, K7) misst den Anteil der Gruppen "mit Mehrheit"; eine Mehrheit "unklar" ist eine Mehrheit (893 von 896). Mit der Lesart der Lieferung exakt gleich. |
| 10 | K9 Fälle, die R und R2 beide sammeln | 52 | 44 | Der Fallabgleich R gegen R2 vergleicht die Kennungen als Zeichenkette: Zusätze wie "GB-34 (1)" in R und das Komma in "GB-09, GB-41" (R Nr. 49) gegen "GB-09 / GB-41" (R2 Nr. 51) verhindern 6 Zuordnungen (R Nr. 35 bis 39 und 49), und Fälle mit gleichem Lauf und gleicher Kennung werden zusammengelegt (R Nr. 8 und 46, 47 und 48; daher 50 statt 52 Fälle in R). Mit normierten Kennungen sammeln beide Läufe alle 52 Fälle von R; R2 hat 2 Fälle mehr. Fehler in der Lieferung. |
| 11 | K9 Anteil Fallpaare gleich gruppiert | 93,59 | 94,8 | wie Nr. 10 (mit normierten Kennungen 1241 von 1326 Fallpaaren gleich gruppiert) |

## 5. Gegenprobe mit der Definition der Lieferung

| Kennzahl (Variante) | nachgerechnet | geliefert | gleich |
|---|---|---|---|
| K5 gleiche Schweregrade, A (Variante getroffen oder teilweise) | 71,78 | 71,8 | ja |
| K5 gleiche Schweregrade, Paare, A (Variante getroffen oder teilweise) | 691 | 691 | ja |
| K5 gleiche Schweregrade, B (Variante getroffen oder teilweise) | 68,12 | 68,1 | ja |
| K5 gleiche Schweregrade, Paare, B (Variante getroffen oder teilweise) | 756 | 756 | ja |
| K5 gleiche Schweregrade, C (Variante getroffen oder teilweise) | 72,80 | 72,8 | ja |
| K5 gleiche Schweregrade, Paare, C (Variante getroffen oder teilweise) | 375 | 375 | ja |
| K5 gleiche Schweregrade, D (Variante getroffen oder teilweise) | 70,00 | 70,0 | ja |
| K5 gleiche Schweregrade, Paare, D (Variante getroffen oder teilweise) | 680 | 680 | ja |
| K7 Einstufung, Anteil Gruppen mit KI-Mehrheit (Variante: Mehrheit "unklar" nicht als Mehrheit) | 99,33 | 99,3 | ja |

## 6. Effektregel je Forschungsfrage

Effekt heißt: die Spannweiten der beiden Bedingungen überlappen sich nicht (Abschnitt 9, Regel 2; Nachtrag 2 vom 2026-10-17).

| Frage | Maß | Spannweiten | Effektregel | Urteil nachgerechnet | Urteil geliefert |
|---|---|---|---|---|---|
| RQ1 (mit G03) | K1 inhaltlich getroffen, A gegen B | A 23,8 bis 33,6; B 25,2 bis 30,8 | überlappen, kein Effekt | nicht erfüllt | nicht erfüllt |
| RQ1 (ohne G03) | K1 inhaltlich getroffen, A gegen B | A 23,4 bis 32,3; B 24,2 bis 28,2 | überlappen, kein Effekt | nicht erfüllt | nicht erfüllt |
| RQ2 (mit G03) | K1 inhaltlich getroffen, B gegen C; K6 in B | B 25,2 bis 30,8; C 21,7 bis 22,4; K6 B 61,1 % (kleinster Lauf 59,5 %) | getrennt, B über C; K6 über einem Fünftel in jedem Lauf | erfüllt | erfüllt |
| RQ2 (ohne G03) | K1 inhaltlich getroffen, B gegen C; K6 in B | B 24,2 bis 28,2; C 21,0 bis 21,8; K6 B 61,1 % (kleinster Lauf 59,5 %) | getrennt, B über C; K6 über einem Fünftel in jedem Lauf | erfüllt | erfüllt |
| RQ3 (mit G03) | F1 bis F7 je Gutachten, B gegen D; K1 inhaltlich getroffen | F: B 5,25 bis 6,25; D 2,50 bis 3,50; K1: B 25,2 bis 30,8; D 25,9 bis 30,8 | F getrennt, D unter B; K1 überlappen, D nicht weniger | erfüllt | erfüllt |
| RQ3 (ohne G03) | F1 bis F7 je Gutachten, B gegen D; K1 inhaltlich getroffen | F: B 5,25 bis 6,25; D 2,50 bis 3,50; K1: B 24,2 bis 28,2; D 23,4 bis 28,2 | F getrennt, D unter B; K1 überlappen, D nicht weniger | erfüllt | erfüllt |

RQ3 je Fehlerklasse (B gegen D, Fälle je Gutachten):

| Klasse | B | D | Ergebnis |
|---|---|---|---|
| F1 | 0,25 bis 0,50 | 0,00 bis 0,00 | D unter B, getrennt |
| F2 | 0,75 bis 1,25 | 0,00 bis 0,50 | D unter B, getrennt |
| F3 | 0,25 bis 0,50 | 0,75 bis 1,50 | B unter D, getrennt (umgekehrt) |
| F4 | 0,25 bis 1,00 | 0,50 bis 1,00 | überlappen, kein Effekt |
| F5 | 0,00 bis 0,50 | 0,25 bis 0,50 | überlappen, kein Effekt |
| F6 | 0,00 bis 0,25 | 0,00 bis 0,00 | überlappen, kein Effekt |
| F7 | 1,50 bis 4,75 | 0,00 bis 1,00 | D unter B, getrennt |

Die Erwartung von RQ3 ist für die Summe F1 bis F7 erfüllt, aber nicht in jeder Klasse: F1, F2 und F7 sinken mit Effekt, F4 bis F6 ohne Effekt, F3 steigt mit Effekt (B 0,25 bis 0,50, D 0,75 bis 1,50). Die Trefferbilanz nennt das in der Klassentabelle; Nachtrag 1 zur Lieferung, Hinweis 1, führt den Anstieg auf die neuen Regeln zu F3 und F4 zurück. Das Protokoll legt nicht fest, ob die Erwartung für die Summe oder je Klasse gilt.

## 7. Schwelle der Stichprobe (Protokoll Abschnitt 7, Punkt 5)

Übereinstimmung Auftraggeber gegen Gruppenurteil auf 60 Einzelbefunden: 57 gleich, 95,0 %; je Bedingung A 14, B 14, C 14, D 15 von 15. Die Schwelle von 80 % ist erreicht; eine Erweiterung auf 120 war nicht nötig. Die drei Abweichungen:

| Zufallskennung | Gruppe | Gruppengröße | KI-Mehrheit | Auftraggeber |
|---|---|---|---|---|
| Bb0138 | Gdd8515/BG-151 | 1 | ansichtssache | nicht veröffentlicht |
| B269b0 | G51faf2/BG-195 | 9 | ansichtssache | nicht veröffentlicht |
| B17541 | Gc9d1ce/BG-176 | 9 | zutreffend | nicht veröffentlicht |

Nach Punkt 4 gilt das Urteil des Auftraggebers für die ganze Gruppe; das ist in `endgueltig_gruppen.json` so umgesetzt (19 Einzelbefunde betroffen).

## 8. Abweichungen vom Protokoll und Nachträge in Abschnitt 13

Abschnitt 13 des gelieferten Protokolls enthält drei Nachträge, alle vom 2026-10-17 (Zählung der Vorstudie nur in der Zuordnung; Effektregel entscheidet; Neubestätigung der Sollbefunde der Vorstudie). Nach dem ersten Lauf steht kein Nachtrag.

| Nr. | Abweichung | Beleg in den Daten | datierter Nachtrag in Abschnitt 13 |
|---|---|---|---|
| P1 | In allen 24 Läufen zu egusphere-2025-4506 und egusphere-2025-5046 (je Bedingung A bis D, je 3 Läufe) erkannte `einlesen.py` die Randzeilen nicht; die Fundorte wurden am Seitenbild abgezählt. Bei 4695 und 4733 folgte `text.json` den Randnummern. Das Einlesen und damit die Grundlage der Fundorte war in der Hälfte der Läufe ein anderes als vorgesehen; F1 und F2 können dort häufiger sein, alle Bedingungen sind gleich betroffen. | Laufplan: genau 24 Läufe zu 4506 und 5046 (12 und 12, je Bedingung 6). Laufregister: kein Vermerk in diesen Zeilen und keine Korrekturzeile. Beschrieben nur in Nachtrag 1 zur Lieferung, Hinweis 3, und `Randzeilen_Fassungen_v1_20261115.md` (Fassungen 1.0.0 bis 1.4.0: "nein" für 4506, 5046 und das Supplement). Die Prüfberichte nennen in allen vier Manuskripten fast durchweg die Bestätigung an den gedruckten Randnummern der Seitenbilder (4506: 12 von 12, 5046: 11 von 12, 4695 und 4733: je 12 von 12); an ihnen allein ist die Abweichung nicht erkennbar. | nein |
| P2 | Spalte Verifikation im Laufregister (Pflichtangabe nach Abschnitt 6) ist in allen 48 Zeilen der Hauptstudie leer, obwohl zu jedem Lauf ein Prüfbericht vorliegt. | Laufregister, Spalte 15, 48 von 48 leer; `laeufe/verifikation/` hat 48 Prüfberichte, Zuordnung über `nachverarbeitung.json`. | nein |
| P3 | Die Prüfung der Dateigleichheit des entpackten Skillordners mit dem Paket vor jedem Lauf soll im Laufregister vermerkt werden (Abschnitt 2); das Laufregister hat dafür keine Spalte und keinen Vermerk. | Laufregister; `status.json` enthält ein Feld `paket` (Werte 2 bis 18, in L01 bis L03 fehlend) ohne Erläuterung. | nein |
| P4 | Bedienendes Modell nicht festgehalten: alle 48 Zeilen "claude-opus-5-5 konfiguriert", `status.json` Feld `modell` in allen 48 leer. Das Protokoll verlangt den Vermerk nur, soweit feststellbar (Abschnitt 4); Regel 7 (Modellwechsel) ist damit nicht prüfbar. | Laufregister Spalte Modell; `status.json`. | nicht nötig, als Grenze offen |
| P5 | Verblindung der Gruppierung und Einstufung: In 81 der 1917 Kleinkorrekturen blieb die Spalte mit der Prüfinstanz stehen (Abschnitt 7, Punkt 1: Befunde "ohne ... Instanz"). | Lieferschein, Hinweis 3. In `einzelbefunde.json` tragen alle 1917 Kleinkorrekturen die Spalte Source; welche 81 Texte so an die Agenten gingen, ist aus der Lieferung nicht nachprüfbar, weil die Eingabedateien `befunde_kurz.md` und `befunde_voll.md` nicht geliefert sind. | nein |
| P6 | Der Assistent sah die Urteile des Auftraggebers zur Stichprobe (60 Einzelbefunde, 6 Gruppen) vor der Auswertung. | Lieferschein, Hinweis 2. | nein |
| P7 | Auswertungsregel 9 (Gegenrechnung mit zweitem Skript) wurde nach der Auswertung ins Studienhandbuch aufgenommen und steht nicht im Protokoll. | Nachtrag 1 zur Lieferung, Hinweis 2. | nein |
| P8 | Neutralisierung von drei Skillnamen und einer Versionsnummer in zwei Gutachten der Vorstudie vor der Nachzählung. | Lieferschein, Hinweis 4; `vorstudie/plan.json` Feld `neutralisiert`. | nein |
| P9 | Erste Fassung der Auswertung unterschätzte K6 (Instanz bei 90 zutreffenden Kleinkorrekturen nicht erkannt); korrigiert. | Lieferschein, Hinweis 1. Die Nachrechnung bestätigt die korrigierten Werte. | nicht nötig (Rechenfehler, behoben) |
| P10 | Die Trefferbilanz berichtet K1 der Vorstudie nur für inhaltliche Sollbefunde und Kleinkorrekturen zusammen; Abschnitt 8 verlangt die getrennte Angabe, Hauptmaß ist K1 inhaltlich getroffen. | Trefferbilanz, Abschnitt Vorstudie; die getrennten Werte stehen hier in Abschnitt 3. | nein (Berichtsfehler) |
| P11 | K7 je Bedingung: Für die Einstufung durch die KI nennt die Trefferbilanz nur den Gesamtwert; Abschnitt 8 verlangt K7 "gesamt und je Bedingung". | Trefferbilanz, K7; die Werte je Bedingung stehen hier in Abschnitt 3. | nein (Berichtsfehler) |
| P12 | Belege zur Vollständigkeit der Extraktion (`soll/<M>/extraktion2/`, `soll/<M>/abgleich/`), auf die Abschnitt 7 verweist, fehlen in der Lieferung; ebenso die im Protokoll genannte `Herkunft_der_Regeln_v1_20261017.md` und `Dateivergleich_D_gegen_B_20261017.md` (sie liegen nur in den Ordnern des Studienprotokolls unter `quellen/`). | Verzeichnis `hauptstudie/soll/` enthält je Manuskript nur `extraktion/`, `hitl.md`, `mehrheit.md`, `sollbefunde.md`. | nicht nötig (Lieferumfang) |

Ohne Befund geprüft: 48 Läufe, keiner fehlt, keiner doppelt, keine Wiederholung eines ungültigen Laufs, alle "gültig" mit geprüften Zugriffen; je Bedingung genau die Fassung, Paketprüfsummen und der Aufbau nach Abschnitt 2 und 4; Effort "high" in allen 48 Zeilen; Agentenzahl 8 bei getrennt, 1 bei nacheinander; Reihenfolge gemischt (drei Wellen zu je 16 Läufen); PDF-Prüfsumme je Manuskript einheitlich; Prüfsumme jedes Gutachtens gleich den ersten 12 Stellen in Laufregister und `status.json`; Startwerte der Stichprobe im Laufregister vermerkt und die Ziehung damit reproduzierbar.

## 9. Skripte

Ausführung mit `python3 -I` in dieser Reihenfolge; jedes Skript liest nur die Lieferung und die Ausgaben der vorherigen.

| Datei | Zweck | SHA-256 |
|---|---|---|
| `nachrechnung.py` | Kennzahlen aus Rohdaten nachrechnen, Mehrheiten prüfen | 03c25055f2661e8d7e535bbad1ff88870c9f6cf29464ae0889cb02702f08302f |
| `vergleich.py` | Nachgerechnete gegen gelieferte Werte vergleichen | c6e6ab5195c1e86e03181045d95726cc91a01817006ddb248c5aedc82d2387e5 |
| `bericht.py` | diesen Bericht aus den Ergebnisdateien erzeugen | 0b66c2a72a76bd34133952653458d5d68f81a1b42f8b95982347315a80205132 |

Ausgaben: `ergebnis.json` (alle Kennzahlen je Bedingung und je Gutachten), `pruefungen.json` (Prüfungen der Eingaben), `vergleich.json` (jeder Vergleich mit Differenz).
