# Dateivergleich Fassung D gegen Ausgangsfassung (PV-09)

Verglichen wurden die entpackten Pakete `science-review-gutachten_v1_20261016_3.skill` (1.3.0) gegen `science-review-gutachten_v1_20261017.skill` (1.4.0) und `science-review-abbildungen_v1_20261016_2.skill` (1.2.0) gegen `science-review-abbildungen_v1_20261017.skill` (1.3.0) mit `diff -ru`. `science-review-studiendesign` ist in B und D dasselbe Paket. Erzeugt mit dem Befehl am Ende dieser Datei.

## Ergebnis

| Skill | Datei | Stelle | Änderung | Fehlerklasse |
|---|---|---|---|---|
| Gutachten | SKILL.md | Kopf | Versionsangabe 1.3.0 auf 1.4.0 | keine (Kennzeichnung) |
| Gutachten | SKILL.md | Schritt 1, Zwischenzeilen | Fundorte an Seitengrenzen und auf unsicheren Zeilen mit `formatpruefung.py --fundorte` auflisten | F1, F2 |
| Gutachten | SKILL.md | Zusammenführung, Regel 2 | sich überschneidende Befunde zusammenlegen oder aufeinander verweisen | F7 |
| Gutachten | SKILL.md | Zusammenführung, Regel 5 | jeder Beleg belegt genau die Teilaussage, an der er steht; Werte nicht auf andere Gegenstände übertragen; unsichere Zeilen mit `--fundorte` abzählen | F5, F2 |
| Gutachten | SKILL.md | Formatprüfung (Beschreibung) | Kennungen mit überlappendem Fundort ohne gegenseitigen Verweis sind Fehler; Zeilenbereich über Seitenwechsel als "S. x, Z. a bis S. y, Z. b", Seitengrenzen mit `--fundorte` prüfen | F7, F1 |
| Gutachten | references/befundformat.md | Status "verifiziert" | Status einer Aussage über eine Quelle nennt den gelesenen Zugang | F6 |
| Gutachten | references/befundformat.md | Formulierung 8 | Zeilenbereich über Seitenwechsel, Fundorte an Seitengrenzen und unsicheren Zeilen | F1, F2 |
| Gutachten | references/befundformat.md | Formulierung 12 | Fehlanzeigen und Gleichheitsaussagen als Suche belegen (Bereich, Suchbegriffe mit Wortformen, Ergebnis) | F4 |
| Gutachten | references/befundformat.md | Formulierung 13 (neu) | Zählungen mit Bereich, Grundlage und Gesamtheit | F3 |
| Gutachten | references/segment-1.md | P13, Schritt 4 | nur teilweise lesbare Quelle: Status nennt den Zugang | F6 |
| Gutachten | scripts/formatpruefung.py | `paare()`, `fundorte()`, CLI `--fundorte`, `main()` | maschinelle Prüfung der Regeln zu F1, F2, F7 | F1, F2, F7 |
| Gutachten | scripts/test_formatpruefung.py | drei neue Tests | Tests zu `paare()` und `fundorte()` | F1, F2, F7 |
| Abbildungen | SKILL.md | Kopf | Versionsangabe 1.2.0 auf 1.3.0 | keine (Kennzeichnung) |
| Abbildungen | references/pruefliste-abbildungen.md | P3, Schritt 2 | Aufteilung nach Farbe, Form oder Kategorie gegen unabhängige Gesamtzahl prüfen | F3 |

Alle übrigen Dateien beider Skills sind bytegleich. Jede inhaltliche Änderung gehört zu einer der Regeln F1 bis F7; außer den Versionsangaben gibt es keine weitere Änderung. B gegen D ändert damit einen Faktor: die Regeln zu F1 bis F7.

## Vollständiger Unterschied

```diff
diff -ru gB/science-review-gutachten/SKILL.md gD/science-review-gutachten/SKILL.md
--- gB/science-review-gutachten/SKILL.md	2026-10-16 16:19:30.000000000 +0000
+++ gD/science-review-gutachten/SKILL.md	2026-10-17 14:35:12.000000000 +0000
@@ -2,7 +2,7 @@
 name: science-review-gutachten
 description: "Begutachtet ein wissenschaftliches Manuskript als PDF wie ein Peer Review: sechs Prüfinstanzen parallel (vier Segmente, Abbildungen, Studiendesign), Befunde mit Fundort, Zitat, Status und Schweregrad, Gesamturteil mit vier Stärken und vier Schwächen, keine Annahmeempfehlung. Immer verwenden bei: Manuskript begutachten, Gutachten erstellen, Peer Review, Review Report, Paper vor Einreichung prüfen, Preprint begutachten."
 metadata:
-  version: "1.3.0"
+  version: "1.4.0"
 ---
 
 # Manuskript begutachten
@@ -33,7 +33,7 @@
 - `seiten/`: jede Seite als Bild, 150 dpi (`seite-1.png` oder `seite-01.png`, je nach Seitenzahl);
 - `fassung.json`: Dateiname, Seitenzahl, Größe, SHA-256 und ob das Manuskript Randzeilen hat.
 
-Hat das Manuskript Randzeilen nur in Abständen, zählt das Skript die Zwischenzeilen. Geht die Zählung zwischen zwei Randnummern auf, gelten die Zwischenzeilen als sicher. Unsicher sind sie, wenn sie nicht aufgeht, und vor der ersten oder nach der letzten Randnummer einer Seite. Dabei gilt: Seitenzahlen zählen nicht als Zeile. Eine allein stehende Randnummer gehört zur Textzeile auf ihrer Höhe; steht sie nicht auf Zeilenhöhe, zählt sie eine leere Zeile. Tabellenzeilen erhalten die Nummer davor, ein Tabellenblock, der im Manuskript als eine Zeile zählt, eine eigene. Nach der letzten Randnummer einer Seite wird höchstens bis zur Nummer vor der ersten Randnummer der Folgeseite gezählt. Eine Seite ohne jede Randnummer hat in `text.json` die Zeile `null`. An unsicheren Zeilen nennt das Gutachten Seite und Element oder die am Seitenbild bestätigte Zeile.
+Hat das Manuskript Randzeilen nur in Abständen, zählt das Skript die Zwischenzeilen. Geht die Zählung zwischen zwei Randnummern auf, gelten die Zwischenzeilen als sicher. Unsicher sind sie, wenn sie nicht aufgeht, und vor der ersten oder nach der letzten Randnummer einer Seite. Dabei gilt: Seitenzahlen zählen nicht als Zeile. Eine allein stehende Randnummer gehört zur Textzeile auf ihrer Höhe; steht sie nicht auf Zeilenhöhe, zählt sie eine leere Zeile. Tabellenzeilen erhalten die Nummer davor, ein Tabellenblock, der im Manuskript als eine Zeile zählt, eine eigene. Nach der letzten Randnummer einer Seite wird höchstens bis zur Nummer vor der ersten Randnummer der Folgeseite gezählt. Eine Seite ohne jede Randnummer hat in `text.json` die Zeile `null`. An unsicheren Zeilen nennt das Gutachten Seite und Element oder die am Seitenbild bestätigte Zeile; welche Fundorte unsicher sind, listet `formatpruefung.py --fundorte` (Schritt 4.5 und 7).
 
 ### 2. Segmentieren
 
@@ -74,10 +74,10 @@
 ### 4. Zusammenführen
 
 1. **Pflichtfelder prüfen.** Ein Befund ohne Pflichtfeld wird an die Instanz zurückgegeben oder verworfen; verworfene werden gezählt.
-2. **Doppelungen auflösen.** Befunde zum selben Fundort und Gegenstand werden ein Befund. Er nennt alle Fundorte und alle Herkünfte; Status und Schweregrad sind die höchsten der zusammengeführten. Das gilt auch zwischen Befund und Kleinkorrektur: Nennt ein Befund die Stelle einer Kleinkorrektur schon, geht die Kleinkorrektur im Befund auf. Gesucht wird nicht nur lesend: `python3 scripts/formatpruefung.py --paare <entwurf.md>` listet Befunde und Kleinkorrekturen mit überlappendem Fundort, nach Seite und Zeile sowie nach dem ersten genannten Element (Abbildung, Tabelle, Anhang, Graphical Abstract), und jedes Paar wird entschieden.
+2. **Doppelungen auflösen.** Befunde zum selben Fundort und Gegenstand werden ein Befund. Er nennt alle Fundorte und alle Herkünfte; Status und Schweregrad sind die höchsten der zusammengeführten. Das gilt auch zwischen Befund und Kleinkorrektur: Nennt ein Befund die Stelle einer Kleinkorrektur schon, geht die Kleinkorrektur im Befund auf. Gesucht wird nicht nur lesend: `python3 scripts/formatpruefung.py --paare <entwurf.md>` listet Befunde und Kleinkorrekturen mit überlappendem Fundort, nach Seite und Zeile sowie nach dem ersten genannten Element (Abbildung, Tabelle, Anhang, Graphical Abstract), und jedes Paar wird entschieden. Getrennt gebliebene Nachbarbefunde verweisen aufeinander: Bleiben zwei Kennungen mit überlappendem Fundort oder verwandtem Gegenstand getrennt, nennt die spätere im Einwand die frühere mit einem Halbsatz zur Abgrenzung, also was hier anders geprüft oder verlangt wird als dort; bei Kleinkorrekturen steht der Verweis in der Spalte Ersatz. Betreffen zwei Kleinkorrekturen dieselbe Wendung in derselben Tabellenzeile oder demselben Satz, werden sie eine Kleinkorrektur. Ein Paar mit überlappendem Fundort ohne Verweis ist in der Formatprüfung ein Fehler.
 3. **Widersprüche klären.** Meldet eine Instanz einen Befund und eine andere zur selben Stelle ein Prüfprotokoll ohne Befund, eine Kleinkorrektur mit anderer Lesart oder einen anderen Befund, wird die Stelle am Manuskript nachgeprüft und entschieden. Die Entscheidung steht im Einwand.
 4. **Hinweise einordnen.** Ein Hinweis außerhalb der Prüfliste wird nur Befund, wenn keine zuständige Instanz die Stelle behandelt hat und die Nachprüfung am Manuskript ihn bestätigt. Herkunft ist dann "ZF".
-5. **Wortlaut nachprüfen.** Jedes Zitat und jede Angabe im Einwand, auch eingebettete Zitate und Zählungen, wird wörtlich in `text.json` gesucht oder mit Python nachgezählt. Ein Nebensatz, der über den belegten Kern hinausgeht, wird belegt oder gestrichen.
+5. **Wortlaut nachprüfen.** Jedes Zitat und jede Angabe im Einwand, auch eingebettete Zitate und Zählungen, wird wörtlich in `text.json` gesucht oder mit Python nachgezählt. Ein Nebensatz, der über den belegten Kern hinausgeht, wird belegt oder gestrichen. Jeder Beleg belegt genau die Teilaussage, an der er steht: Bevor eine Stelle als Beleg einer Teilaussage im Einwand steht, wird an ihrem Wortlaut geprüft, dass sie denselben Gegenstand nennt, dieselbe Größe, denselben Fall, denselben Zeitraum. Ein Wert (Datum, Zahl, Version), den das Manuskript nur für einen anderen Gegenstand oder gar nicht nennt, wird nicht übertragen; wird er erschlossen, steht er mit Herleitung und Status erschlossen, und jede Zählung, die von ihm abhängt, nennt zusätzlich die Zahl der Fälle, die ohne ihn sicher sind. Unsichere Zeilen werden abgezählt, nicht übernommen: `python3 scripts/formatpruefung.py --fundorte <entwurf.md> <arbeitsordner>` listet jeden Fundort an einer Seitengrenze, auf einer Zeile, die laut `text.json` auf einer anderen Seite steht, und auf einer unsicheren Zeile. Jeder gelistete Fundort wird am Seitenbild von der nächsten gedruckten Randnummer aus abgezählt; die Zählung steht im Prüfprotokoll mit der Randnummer, von der aus gezählt wurde. Die erste Zeile eines Zitats ist die Zeile, in der sein erstes Wort steht, die letzte die seines letzten Wortes. Lässt sich eine Zeile nicht sicher abzählen, nennt der Fundort Seite und Element statt einer Zeile.
 6. **Zuordnen und nummerieren.** Jeder Befund kommt in das Segment seines ersten Fundorts. Die endgültigen Kennungen GB, KK und PP werden in der Reihenfolge der Fundorte vergeben, lückenlos.
 
 ### 5. Gesamturteil
@@ -94,7 +94,7 @@
 
 ### 7. Formatprüfung
 
-`python3 scripts/formatpruefung.py <gutachten.md>` prüft unter anderem Rubriken, lückenlose Kennungen, Pflichtfelder je Befund, Status, Schweregrad und Herkunft aus den erlaubten Werten, die Tabelle der sechs Zusatzbereiche und Gedankenstriche, und listet Kennungen mit überlappendem Fundort als Hinweise; die vollständige Liste nennt `python3 scripts/formatpruefung.py --help`. Das Gutachten wird erst bei 0 Fehlern und entschiedenen Hinweisen übergeben.
+`python3 scripts/formatpruefung.py <gutachten.md>` prüft unter anderem Rubriken, lückenlose Kennungen, Pflichtfelder je Befund, Status, Schweregrad und Herkunft aus den erlaubten Werten, die Tabelle der sechs Zusatzbereiche und Gedankenstriche, und meldet Kennungen mit überlappendem Fundort ohne gegenseitigen Verweis als Fehler, mit Verweis als Hinweis; die vollständige Liste nennt `python3 scripts/formatpruefung.py --help`. Seitenangaben werden an der Seitengrenze geprüft: Ein Zeilenbereich, der über einen Seitenwechsel reicht, wird als "S. x, Z. a bis S. y, Z. b" geschrieben, ein Bereich, der ganz auf einer Seite liegt, nennt nur diese Seite. `python3 scripts/formatpruefung.py --fundorte <gutachten.md> <arbeitsordner>` listet jeden Fundort, dessen erste oder letzte Zeile in `text.json` auf einer anderen Seite steht als angegeben oder in den ersten oder letzten zwei Zeilen einer Seite liegt; jeder gelistete Fundort wird am Seitenbild der genannten Seite und ihrer Nachbarseite bestätigt oder berichtigt. Das Gutachten wird erst bei 0 Fehlern, entschiedenen Hinweisen und abgearbeiteter Fundortliste übergeben.
 
 ## Ausgabe
 
diff -ru gB/science-review-gutachten/references/befundformat.md gD/science-review-gutachten/references/befundformat.md
--- gB/science-review-gutachten/references/befundformat.md	2026-10-16 16:19:30.000000000 +0000
+++ gD/science-review-gutachten/references/befundformat.md	2026-10-17 14:35:12.000000000 +0000
@@ -34,7 +34,7 @@
 
 | Status | Wann |
 |---|---|
-| verifiziert | am Manuskript belegt: im Text mit Fundort, bei Zeichen, Satz und Abbildungen am Seitenbild, bei Werten in Diagrammen durch Messung; bei Aussagen über Quellen in der Quelle selbst |
+| verifiziert | am Manuskript belegt: im Text mit Fundort, bei Zeichen, Satz und Abbildungen am Seitenbild, bei Werten in Diagrammen durch Messung; bei Aussagen über Quellen in der Quelle selbst. Der Status einer Aussage über eine Quelle nennt den gelesenen Zugang: was gelesen wurde (Volltext, Abstract oder Verlagsseite), über welche URL oder DOI und in welcher Fassung, wenn die Quelle in mehreren Fassungen vorliegt. Eine Angabe, die über das Gelesene hinausgeht (Seite, Tabelle, Abschnitt oder wörtlicher Wortlaut aus dem Haupttext), ist nur verifiziert, wenn der Volltext mit seinem Zugang genannt ist; sonst hat sie den Status erschlossen, und die Quelle steht unter "Grenzen des Gutachtens". |
 | erschlossen | aus belegten Angaben abgeleitet, aber nicht selbst belegt; dazu gehören Quoten, die das Gutachten aus Zahlen des Manuskripts errechnet, und Aussagen über Quellen, die nicht lesbar waren |
 | Vermutung | eine Annahme über die Umgebung, die Absicht oder das Vorgehen der Autoren, die das Manuskript nicht hergibt; ebenso jedes Argument aus allgemeinem Wissen über Werkzeuge oder Modelle ohne Beleg |
 
@@ -61,11 +61,12 @@
 5. **Literatur als Beleg.** Stützt eine Studie den Einwand selbst, wird sie genannt, mit vollständiger Angabe; sie muss gelesen sein.
 6. **Gegenentwurf.** Wer ein Design kritisiert, nennt ein Design, das die Frage beantworten würde.
 7. **Ersatzwortlaut.** Jede Kleinkorrektur nennt den Ersatz.
-8. **Fundort bis zur Zelle.** Seite, Zeile, Tabellenzeile und Spalte, Feld einer Abbildung.
+8. **Fundort bis zur Zelle.** Seite, Zeile, Tabellenzeile und Spalte, Feld einer Abbildung. Ein Zeilenbereich über einen Seitenwechsel heißt "S. x, Z. a bis S. y, Z. b"; Fundorte an Seitengrenzen und auf unsicheren Zeilen werden nach SKILL.md, Schritt 4.5 und 7, am Seitenbild bestätigt.
 9. **Quoten mit Rechnung.** Eine Quote, die das Gutachten errechnet, steht mit Rechnung und Status erschlossen.
 10. **Eigene Vorfälle als Beleg.** Dokumentiert das Manuskript selbst Fehler oder Abweichungen, können sie einen Befund belegen, mit Fundort.
 11. **Ursachen trennen.** Hat ein Messwert mehrere mögliche Ursachen, nennt der Befund jede und verlangt ihre Trennung.
-12. **Kern und Nebensatz.** Jede Teilaussage des Einwands ist belegt. Ein Nebensatz, der über den belegten Kern hinausgeht ("nirgends", "kein Item", "nur"), wird geprüft oder gestrichen; ein eingebettetes Zitat steht wörtlich im Manuskript.
+12. **Kern und Nebensatz.** Jede Teilaussage des Einwands ist belegt. Ein Nebensatz, der über den belegten Kern hinausgeht ("nirgends", "kein Item", "nur"), wird geprüft oder gestrichen; ein eingebettetes Zitat steht wörtlich im Manuskript. Fehlanzeigen und Gleichheitsaussagen werden als Suche belegt: Sagt ein Einwand, ein Titel oder ein Ersatzwortlaut, dass etwas in einem Bereich an keiner Stelle vorkommt, oder dass mehrere Stellen gleich lauten, nennt der Befund die Suche, also den Bereich mit Seiten und Zeilen, die Suchbegriffe einschließlich Wortformen, Abkürzungen und gleichbedeutender Wendungen der gesuchten Begriffe, und die Trefferzahl. Bei einer Gleichheitsaussage wird jede genannte Stelle einzeln am Seitenbild zeichengenau verglichen, auch Akzente, Bindestriche und Leerzeichen; bei Kleinkorrekturen steht die Liste der verglichenen Stellen in der Spalte Ersatz. Fehlt diese Angabe, wird die Aussage auf die geprüften Stellen beschränkt oder gestrichen.
+13. **Zählungen.** Jede Zählung im Einwand nennt Bereich, Grundlage und Gesamtheit. Wer zählt, wie oft etwas vorkommt oder wie viele Elemente eine Eigenschaft haben, nennt den Zählbereich (Fließtext, Tabellen, Abbildungen oder ganzes Manuskript, mit Seiten oder Zeilen), die Grundlage (`text.json` oder Seitenbild) und die gezählten Fundorte oder Elemente einzeln. Eine Aufteilung nach Eigenschaften (Farbe, Form, Kategorie) wird gegen eine unabhängig gezählte Gesamtzahl der Elemente gehalten, und die Rechnung, dass die Teile die Gesamtzahl ergeben, steht mit Python im Befund. Eine Aussage über alle Treffer ("nie", "immer", "jedes Mal") gilt nur für den genannten Bereich und wird an jedem Treffer geprüft. Zählungen in Tabellen und Abbildungen werden am Seitenbild wiederholt.
 
 Die Sprache bleibt vorsichtig, aber eindeutig: "Die Angabe in Z. 120 weicht von Tabelle 3 ab" statt "Es könnte möglicherweise eine Abweichung geben". Keine Wertungen ohne Gegenstand ("hervorragend", "geschickt"). Keine Gedankenstriche.
 
diff -ru gB/science-review-gutachten/references/segment-1.md gD/science-review-gutachten/references/segment-1.md
--- gB/science-review-gutachten/references/segment-1.md	2026-10-15 16:33:16.000000000 +0000
+++ gD/science-review-gutachten/references/segment-1.md	2026-10-17 14:35:18.000000000 +0000
@@ -10,7 +10,7 @@
 1. Alle Sätze mit Zahlen, Rangfolgen oder Wertungen aus fremden Arbeiten sammeln, mit Zitat und Fundort.
 2. Je Satz die Quelle öffnen, zuerst über DOI oder Verlagsseite mit WebFetch, Open Access zuerst. Verfahren nach `science-faktenbeleg-pruefung`, Phase 2.
 3. Prüfen: Steht die Zahl so in der Quelle? Ist sie vollständig wiedergegeben, oder fehlt der Vergleichswert, der sie einordnet? Bezieht sie sich auf denselben Nenner?
-4. Ist die Quelle nicht lesbar, erhält der Befund den Status "erschlossen", und das Gutachten nennt die Quelle unter "Grenzen".
+4. Ist die Quelle nicht lesbar, erhält der Befund den Status "erschlossen", und das Gutachten nennt die Quelle unter "Grenzen". Ist nur ein Teil lesbar (etwa der Abstract), nennt der Status den gelesenen Zugang, und Angaben aus dem ungelesenen Teil sind erschlossen (`references/befundformat.md`, Status verifiziert).
 
 **Befund ist:** eine Zahl, die in der Quelle anders steht; eine selektive Wiedergabe, bei der ein Vergleichswert derselben Studie fehlt, der die Aussage ändert; eine Quote ohne ihren Nenner, wenn bedingte und unbedingte Rate auseinanderliegen.
 
diff -ru gB/science-review-gutachten/scripts/formatpruefung.py gD/science-review-gutachten/scripts/formatpruefung.py
--- gB/science-review-gutachten/scripts/formatpruefung.py	2026-10-16 16:18:34.000000000 +0000
+++ gD/science-review-gutachten/scripts/formatpruefung.py	2026-10-17 14:34:22.000000000 +0000
@@ -2,11 +2,18 @@
 """Prüft das Format eines Gutachtens nach assets/gutachten-vorlage.md.
 
 Aufruf: python3 formatpruefung.py [--paare] <gutachten.md>
+        python3 formatpruefung.py --fundorte <gutachten.md> <arbeitsordner>
 
 Gibt je Fehler eine Zeile aus und endet mit Code 1; ohne Fehler mit
 "0 Fehler, n Hinweise" und Code 0. Kennungen GB und KK mit überlappendem
-Fundort werden als Hinweise gelistet (kein Fehler); mit --paare nur diese
-Liste, als Prüfauftrag für die Zusammenführung. Fundorte sind Seite mit
+Fundort, von denen eine die andere nennt, werden als Hinweise gelistet;
+nennt keine die andere, ist das Paar ein Fehler (getrennt gebliebene
+Nachbarbefunde verweisen aufeinander). Mit --paare nur diese Liste, als
+Prüfauftrag für die Zusammenführung, Code 0. Mit --fundorte liest das
+Skript `text.json` aus dem Arbeitsordner und listet jeden Fundort, der vor
+der Übergabe am Seitenbild zu bestätigen ist: Zeile laut `text.json` auf
+einer anderen Seite als angegeben, Zeile in den ersten oder letzten zwei
+Zeilen einer Seite, Zeile mit "zeile_sicher": false oder ohne Eintrag. Fundorte sind Seite mit
 Zeile (S. 3, Z. 10; p. 3, l. 10) und Elemente (Abbildung, Tabelle, Anhang,
 Graphical Abstract mit Nummer oder Buchstabe); zwei Kennungen bilden ein
 Paar, wenn die erste Zeilenangabe der einen unter den Zeilenangaben der
@@ -254,22 +261,26 @@
     """Kennungen (GB, KK), bei denen der erste Fundort der einen in den Fundorten der
     anderen liegt: Prüfaufträge für die Zusammenführung."""
     zeilen = text.split("\n")
-    orte, erste = {}, {}
+    orte, erste, bloecke = {}, {}, {}
     starts = [i for i, z in enumerate(zeilen) if re.match(r"^\*\*GB-\d{2,3}\b", z)]
     for k, i in enumerate(starts):
         kennung = re.match(r"^\*\*(GB-\d{2,3})", zeilen[i]).group(1)
         ende = starts[k + 1] if k + 1 < len(starts) else len(zeilen)
+        block = [zeilen[i]]
         for z in zeilen[i + 1:ende]:
             if z.startswith("#"):
                 break
+            block.append(z)
             m = re.match(r"^\|\s*(Fundort|Location)\s*\|(.*)\|\s*$", z)
             if m:
                 orte[kennung] = fundstellen(m.group(2))
                 erste[kennung] = fundstellen(m.group(2), nur_erste=True)
+        bloecke[kennung] = re.sub(r"^\*\*GB-\d{2,3}", "", "\n".join(block))
     for z in tabellenzeilen(zeilen):
         if re.fullmatch(r"KK-\d{2,3}", z[0]) and len(z) > 1:
             orte[z[0]] = fundstellen(z[1])
             erste[z[0]] = fundstellen(z[1], nur_erste=True)
+            bloecke[z[0]] = " | ".join(z[1:])
     namen = sorted(orte, key=lambda x: (x[:2], int(x.split("-")[1])))
     res = []
     for i, a in enumerate(namen):
@@ -288,7 +299,61 @@
                 else:
                     e = sorted(gemeinsam)[0]
                     ort = {"Abb": "Abbildung", "Tab": "Tabelle", "Anh": "Anhang", "GA": "Graphical Abstract"}[e[1]] + (f" {e[2]}" if e[2] else "")
-                res.append(f"Hinweis: {a} und {b} haben überlappende Fundorte ({ort}); gleicher Gegenstand?")
+                if b in bloecke.get(a, "") or a in bloecke.get(b, ""):
+                    res.append(f"Hinweis: {a} und {b} haben überlappende Fundorte ({ort}); Verweis vorhanden")
+                else:
+                    res.append(f"Fehler: {a} und {b} haben überlappende Fundorte ({ort}) ohne gegenseitigen Verweis; "
+                               "zusammenlegen oder in der späteren Kennung auf die frühere verweisen")
+    return res
+
+
+def fundorte(text, eintraege):
+    """Fundorte, die vor der Übergabe am Seitenbild zu bestätigen sind (Seitengrenze, andere Seite,
+    unsichere Zeile). eintraege: Liste aus text.json. Ergebnis: Liste von Zeilen "Prüfen: ..."."""
+    sicher, seiten = {}, {}
+    for e in eintraege:
+        if e.get("zeile") is None:
+            continue
+        sicher[(e["seite"], e["zeile"])] = bool(e.get("zeile_sicher"))
+        seiten.setdefault(e["seite"], []).append(e["zeile"])
+    grenzen = {s: (sorted(set(z))[:2], sorted(set(z))[-2:]) for s, z in seiten.items()}
+    zeilen = text.split("\n")
+    quellen = []
+    gb = None
+    for z in zeilen:
+        m = re.match(r"^\*\*(GB-\d{2,3})\b", z)
+        if m:
+            gb = m.group(1)
+        m = re.match(r"^\|\s*(Fundort|Location)\s*\|(.*)\|\s*$", z)
+        if m and gb:
+            quellen.append((gb, m.group(2)))
+    quellen += [(z[0], z[1]) for z in tabellenzeilen(zeilen) if re.fullmatch(r"KK-\d{2,3}", z[0]) and len(z) > 1]
+    res = []
+    for kennung, ort in quellen:
+        seite = None
+        for m in TOKEN.finditer(ort):
+            if m.group(1):
+                seite = int(m.group(1))
+                continue
+            if seite is None:
+                continue
+            von = int(m.group(2))
+            seite_bis = int(m.group(3)) if m.group(3) else seite
+            bis = int(m.group(4)) if m.group(4) else von
+            for s, zl, rolle in ((seite, von, "erste"), (seite_bis, bis, "letzte")):
+                gruende = []
+                if (s, zl) not in sicher:
+                    andere = sorted(x for (x, y) in sicher if y == zl and x != s)
+                    gruende.append("Zeile laut text.json auf S. " + ", ".join(map(str, andere)) if andere else "Zeile ohne Eintrag in text.json")
+                else:
+                    if not sicher[(s, zl)]:
+                        gruende.append("unsichere Zeile")
+                    anfang, ende = grenzen.get(s, ([], []))
+                    if zl in anfang or zl in ende:
+                        gruende.append("Seitengrenze")
+                if gruende:
+                    res.append(f"Prüfen: {kennung} S. {s}, Z. {zl} ({rolle} Zeile): {'; '.join(gruende)}")
+            seite = seite_bis
     return res
 
 
@@ -296,6 +361,21 @@
     if any(a in ("-h", "--help") for a in sys.argv[1:]):
         print(__doc__)
         sys.exit(0)
+    if sys.argv[1:2] == ["--fundorte"]:
+        if len(sys.argv) != 4:
+            print("Aufruf: python3 formatpruefung.py --fundorte <gutachten.md> <arbeitsordner>", file=sys.stderr)
+            sys.exit(2)
+        import json
+        import os
+        with open(sys.argv[2], encoding="utf-8") as fh:
+            text = fh.read()
+        with open(os.path.join(sys.argv[3], "text.json"), encoding="utf-8") as fh:
+            eintraege = json.load(fh)
+        liste = fundorte(text, eintraege)
+        for x in liste:
+            print(x)
+        print(f"{len(liste)} Fundorte am Seitenbild zu bestätigen")
+        sys.exit(0)
     args = [a for a in sys.argv[1:] if a != "--paare"]
     nur_paare = "--paare" in sys.argv[1:]
     if len(args) != 1:
@@ -303,13 +383,14 @@
         sys.exit(2)
     with open(args[0], encoding="utf-8") as fh:
         text = fh.read()
-    hinweise = paare(text)
+    liste = paare(text)
     if nur_paare:
-        for x in hinweise:
+        for x in liste:
             print(x)
-        print(f"{len(hinweise)} Paare mit überlappendem Fundort")
+        print(f"{len(liste)} Paare mit überlappendem Fundort")
         sys.exit(0)
-    fehler = pruefe(text)
+    fehler = pruefe(text) + [x for x in liste if x.startswith("Fehler:")]
+    hinweise = [x for x in liste if x.startswith("Hinweis:")]
     for x in fehler:
         print(x)
     for x in hinweise:
diff -ru gB/science-review-gutachten/scripts/test_formatpruefung.py gD/science-review-gutachten/scripts/test_formatpruefung.py
--- gB/science-review-gutachten/scripts/test_formatpruefung.py	2026-10-16 16:18:20.000000000 +0000
+++ gD/science-review-gutachten/scripts/test_formatpruefung.py	2026-10-17 14:34:36.000000000 +0000
@@ -6,7 +6,7 @@
 import unittest
 
 sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
-from formatpruefung import pruefe, paare, fundstellen  # noqa: E402
+from formatpruefung import pruefe, paare, fundstellen, fundorte  # noqa: E402
 
 SKRIPT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "formatpruefung.py")
 
@@ -242,6 +242,40 @@
         treffer = [x for x in paare(t) if "Abbildung 3" in x]
         self.assertEqual(len(treffer), 1, paare(t))
 
+    def test_paare_ohne_verweis_fehler(self):
+        t = gutachten().replace('| KK-01 | S. 2, Z. 4 |', '| KK-01 | S. 2, Z. 10 |')
+        h = paare(t)
+        self.assertTrue(h[0].startswith("Fehler:"), h)
+        pfad = os.path.join(os.path.dirname(SKRIPT), "_probe_paar.md")
+        with open(pfad, "w", encoding="utf-8") as fh:
+            fh.write(t)
+        try:
+            r = subprocess.run([sys.executable, SKRIPT, pfad], capture_output=True, text=True)
+        finally:
+            os.remove(pfad)
+        self.assertEqual(r.returncode, 1, r.stdout)
+        self.assertIn("ohne gegenseitigen Verweis", r.stdout)
+
+    def test_paare_mit_verweis_hinweis(self):
+        t = gutachten().replace('| KK-01 | S. 2, Z. 4 |', '| KK-01 | S. 2, Z. 10 |')
+        t = t.replace("| Einwand | Tabelle 2 nennt 38 Proben. |", "| Einwand | Tabelle 2 nennt 38 Proben; anders als KK-01 geht es um die Zahl. |", 2)
+        h = paare(t)
+        self.assertTrue(h and all(x.startswith("Hinweis:") for x in h), h)
+
+    def test_fundorte(self):
+        tj = [{"seite": 3, "zeile": z, "zeile_sicher": z != 12, "text": "x"} for z in range(1, 31)]
+        tj += [{"seite": 4, "zeile": z, "zeile_sicher": True, "text": "x"} for z in range(31, 61)]
+        t = gutachten().replace("| Fundort | S. 1, Z. 10 |", "| Fundort | S. 3, Z. 12 |", 1)
+        t = t.replace("| Fundort | S. 2, Z. 10 |", "| Fundort | S. 3, Z. 29 bis S. 4, Z. 32 |", 1)
+        t = t.replace("| Fundort | S. 3, Z. 10 |", "| Fundort | S. 3, Z. 40 |", 1)
+        t = t.replace("| Fundort | S. 4, Z. 10 |", "| Fundort | S. 4, Z. 45 |", 1)
+        r = "\n".join(fundorte(t, tj))
+        self.assertIn("GB-01 S. 3, Z. 12 (erste Zeile): unsichere Zeile", r)
+        self.assertIn("GB-02 S. 3, Z. 29 (erste Zeile): Seitengrenze", r)
+        self.assertIn("GB-02 S. 4, Z. 32 (letzte Zeile): Seitengrenze", r)
+        self.assertIn("GB-03 S. 3, Z. 40 (erste Zeile): Zeile laut text.json auf S. 4", r)
+        self.assertNotIn("GB-04", r)
+
     def test_hilfe(self):
         r = subprocess.run([sys.executable, SKRIPT, "--help"], capture_output=True, text=True)
         self.assertEqual(r.returncode, 0)
diff -ru aB/science-review-abbildungen/SKILL.md aD/science-review-abbildungen/SKILL.md
--- aB/science-review-abbildungen/SKILL.md	2026-10-16 16:20:10.000000000 +0000
+++ aD/science-review-abbildungen/SKILL.md	2026-10-17 14:35:12.000000000 +0000
@@ -2,7 +2,7 @@
 name: science-review-abbildungen
 description: "Prüft die Abbildungen eines wissenschaftlichen Manuskripts als PDF: Eigenständigkeit, Beschriftung, Legende, gezählte und gemessene Werte gegen Text und Tabellen, Ereignisse gegen Daten. Prüfinstanz AB von science-review-gutachten, auch allein nutzbar. Verwenden bei: Abbildungen prüfen, Diagramme nachmessen, Werte aus Abbildung ablesen, Figure check."
 metadata:
-  version: "1.2.0"
+  version: "1.3.0"
 ---
 
 # Abbildungen prüfen
diff -ru aB/science-review-abbildungen/references/pruefliste-abbildungen.md aD/science-review-abbildungen/references/pruefliste-abbildungen.md
--- aB/science-review-abbildungen/references/pruefliste-abbildungen.md	2026-10-16 16:20:10.000000000 +0000
+++ aD/science-review-abbildungen/references/pruefliste-abbildungen.md	2026-10-17 14:35:12.000000000 +0000
@@ -25,7 +25,7 @@
 
 **Vorgehen:**
 1. Beschriftungen gegen Unterschrift und Text: Namen, Nummern, Einheiten, Schreibweisen.
-2. Zählen: Balken, Segmente, Marker, Punkte, Fälle. Gezählt wird mit `messen.py flecken` oder am vergrößerten Ausschnitt, nicht im Überblick.
+2. Zählen: Balken, Segmente, Marker, Punkte, Fälle. Gezählt wird mit `messen.py flecken` oder am vergrößerten Ausschnitt, nicht im Überblick. Eine Aufteilung nach Farbe, Form oder Kategorie wird gegen eine unabhängig gezählte Gesamtzahl gehalten; Bereich, Grundlage und gezählte Elemente stehen im Befund (`science-review-gutachten`, `references/befundformat.md`, Formulierung 13).
 3. Messen: Werte, die der Text oder eine Tabelle nennt, an der Abbildung nachmessen, nach `messverfahren.md`. Eine Abweichung über der ausgewiesenen Unsicherheit ist ein Befund.
 4. Farben: jede verwendete Farbe gegen das Legendenfeld messen (`messen.py farben`), nicht nach Eindruck zuordnen.
 5. Lage: Marker, Beschriftungen und Pfeile gegen die Achse, auf die sie zeigen.
```

Befehl: `diff -ru` über die entpackten Pakete, Ordner gB, gD (Gutachten B, D) und aB, aD (Abbildungen B, D).
