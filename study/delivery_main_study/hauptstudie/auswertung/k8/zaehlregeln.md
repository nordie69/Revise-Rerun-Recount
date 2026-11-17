# Zählregeln K4 und F1 bis F7

Grundlage ist allein der Prüfbericht (verifikation.md); das Gutachten (gutachten.md) wird nur gelesen, um bei F6 den Status eines Befunds und bei F7 Querverweise zwischen Kennungen festzustellen.

## K4 Volle Doppelungen

Gezählt wird jedes Paar oder jede Gruppe, die der Prüfbericht im Abschnitt Doppelungen als volle Doppelung führt, also gleicher Fundort und gleicher Gegenstand. Teilüberschneidungen, nahe Überschneidungen und Paare, die der Prüfer ausdrücklich nicht als Doppelung wertet, zählen hier nicht. Eine Gruppe aus drei Kennungen zählt einmal.

## F1 Seitenangabe eines Zeilenbereichs passt nicht zur Seite der Zeilen

Beschreibung: Die Zeilen eines Fundorts stimmen, die Seitenangabe nicht, fast immer an einem Seitenwechsel: ein Bereich, der auf der Vorseite beginnt, wird nur mit der Folgeseite angegeben, oder ein Bereich auf einer Seite wird als "S. x bis y" angegeben.

Zählregel: Gezählt wird je Kennung einmal, wenn der Prüfbericht für irgendeinen ihrer Fundorte (Haupt- oder Nebenstelle, auch in einer Anmerkung "ohne Einfluss auf die Zählung") feststellt, dass die genannten Zeilen stimmen, aber auf einer anderen Seite stehen als angegeben, oder dass ein Seitenbereich angegeben ist, den die Zeilen nicht überschreiten. Stimmt außerdem die Zeile nicht, zählt die Kennung nur hier, nicht in F2.

## F2 Zeilennummer um eine oder zwei Zeilen versetzt

Beschreibung: Die Seite stimmt, die Zeile weicht um eine oder zwei Zeilen von der gedruckten Randnummer ab, typisch vor der ersten Randnummer einer Seite (Kopf, Autorenzeile), in Literaturverzeichnis und eingerückten Zitaten, an Stellen mit Verschiebung in `text.json`, oder weil der Beginn eines zitierten Satzes am Ende der Vorzeile übersehen wurde.

Zählregel: Gezählt wird je Kennung einmal, wenn der Prüfbericht für irgendeinen ihrer Fundorte oder für eine Zeilenangabe im Einwand feststellt, dass die Zeile bei richtiger Seite um mindestens eine Zeile von der gedruckten Randnummer abweicht, gleich ob in der Fundorttabelle oder in einer Anmerkung "ohne Einfluss". Ist zugleich die Seite falsch, zählt die Kennung in F1.

## F3 Falsche Zählung im Einwand

Beschreibung: Eine Häufigkeit oder Aufteilung im Einwand stimmt nicht: der Zählbereich ist unklar oder gemischt (Fließtext und Tabellen über `text.json`), und eine daran geknüpfte Allaussage ("nie", "immer") widerspricht den mitgezählten Stellen, oder bei einer Aufteilung nach Eigenschaften fehlt ein Element, weil die Summe der Teile nicht gegen eine unabhängige Gesamtzahl gehalten wurde.

Zählregel: Gezählt wird je Kennung einmal, wenn ihr Urteil "teilweise echt" oder "falsch" ist und der Prüfbericht als Grund nennt, dass eine Anzahl, Häufigkeit oder Aufteilung im Einwand (oder im Titel) nicht mit seiner eigenen Zählung übereinstimmt. Weicht nur ein Messwert ab (Länge, Farbe, Lage), zählt der Fall nicht hier.

## F4 Fehlanzeige oder Gleichheitsaussage über mehrere Stellen nicht an jeder Stelle geprüft

Beschreibung: Ein Befund oder eine Kleinkorrektur behauptet, etwas komme in einem Bereich nicht vor ("kein Kernbegriff wird aufgenommen") oder laute an mehreren Stellen gleich ("dieselbe Form wie in Z. a und Z. b"), und mindestens eine Stelle widerlegt das, weil nach einer Wortform gesucht wurde statt nach dem Begriff oder weil die zweite Stelle nicht zeichengenau verglichen wurde.

Zählregel: Gezählt wird je Kennung einmal, wenn ihr Urteil "teilweise echt" oder "falsch" ist und der Prüfbericht als Grund nennt, dass eine Aussage über das Fehlen ("kein", "nirgends", "nicht aufgenommen", "nur") oder über die Gleichheit mehrerer Stellen an mindestens einer Stelle des Manuskripts nicht zutrifft. Ist die widerlegte Aussage eine Anzahl, zählt der Fall in F3.

## F5 Beleg oder Angabe auf einen benachbarten Gegenstand übertragen

Beschreibung: Der Kern des Befunds stimmt, aber eine Teilaussage stützt sich auf eine Stelle, die einen anderen Gegenstand nennt (eine andere Größe, einen anderen Fall, einen anderen Zeitraum), oder ein Wert, den das Manuskript nur für einen Nachbarfall nennt, wird auf einen weiteren Fall übertragen und geht in eine Zählung ein.

Zählregel: Gezählt wird je Kennung einmal, wenn ihr Urteil "teilweise echt" oder "falsch" ist und der Prüfbericht als Grund nennt, dass eine angeführte Belegstelle einen anderen Gegenstand betrifft als die Teilaussage, oder dass ein Wert angegeben wird, den das Manuskript für diesen Gegenstand nicht nennt.

## F6 Quellendetail als verifiziert ausgewiesen, ohne nachprüfbaren Zugang

Beschreibung: Ein Befund gibt aus einer Quelle Einzelheiten wieder, die über Abstract und Verlagsseite hinausgehen (Seitenzahl, Tabelle, wörtliche Definition), mit Status verifiziert, aber ohne Angabe, über welchen Zugang der Volltext gelesen wurde; der Prüfer erreicht nur den Abstract und kann den Teil nicht prüfen.

Zählregel: Gezählt wird je Kennung einmal, wenn der Prüfbericht sie ganz oder für einen Teil als "nicht prüfbar" führt, weil die angeführte Quellenstelle nicht zugänglich war, und das Gutachten für diesen Teil den Status verifiziert ohne Angabe des Zugangs zum Volltext führt. Nennt das Gutachten für diesen Teil den Status erschlossen, zählt der Fall nicht.

## F7 Getrennt gebliebene Nachbarbefunde ohne Querverweis

Beschreibung: Zwei oder mehr Kennungen haben einen überlappenden Fundort oder einen eng verwandten Gegenstand, wurden zu Recht nicht zusammengelegt, nennen einander aber nicht; der Prüfer muss die Abgrenzung selbst herstellen. Dazu gehören auch zwei Kleinkorrekturen zur selben Wendung in derselben Tabellenzeile.

Zählregel: Gezählt wird jeder Eintrag (Paar oder Gruppe) im Abschnitt "Doppelungen" eines Prüfberichts, den der Prüfer als Teilüberschneidung oder nahe Überschneidung nennt und in dem keine der beteiligten Kennungen eine andere beteiligte Kennung im Gutachten nennt; eine Gruppe aus drei Kennungen zählt einmal. Einträge mit mindestens einem Verweis zählen nicht. Eine volle Doppelung (gleicher Fundort und gleicher Gegenstand) zählt nicht hier, sondern wird gesondert gezählt.

