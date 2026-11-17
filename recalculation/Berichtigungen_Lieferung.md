# Paper3: Berichtigungen zur Lieferung der Hauptstudie

Stand 2026-11-15, Auftrag C-135. Die gelieferten Dateien (DAT-60, DAT-61) bleiben nach Entscheidung 3 unverändert und schreibgeschützt; die Berichtigungen gelten für Paper 3 und gehen als Rückmeldung an den Review-Chat. Workplan SB-47; BL-3 nach der Nachrechnung 6.1 (SB-48, C-140).

## 1. Berichtigungen

| Nr | Datei und Stelle | Gelieferter Wortlaut | Berichtigt | Beleg |
|---|---|---|---|---|
| BL-1 | DAT-60, hauptstudie/auswertung/Trefferbilanz_Hauptstudie_v1_20261115.md, Abschnitt "Vergleich mit der bisherigen Trefferbilanz" | "Die neue Zählung nutzt die Einwände der öffentlichen Gutachten, von drei Prüfern bestätigt" | Die neue Zählung nutzt für LAM und TCD die Einwände aus den Gutachten des KI-Peer-Review-Dienstes und für HOR (egusphere-2025-2248) die Einwände aus den öffentlichen Gutachten RC1 und RC2 der ersten Runde, jeweils von drei Prüfern bestätigt | Auskunft des Review-Chats C-114; Sollbefundlisten in DAT-60, hauptstudie/soll_vorstudie/LAM und TCD, Spalte Herkunft im Format des Dienstes ("High-Level Summary, Weaknesses", "Potential Mistakes") |
| BL-2 | DAT-60, hauptstudie/Laufregister.md, Läufe der Hauptstudie | kein Vermerk zur Zählung der Fundorte | In 24 der 48 Läufe (H-A-4506-1 bis -3, H-A-5046-1 bis -3, H-B-4506-1 bis -3, H-B-5046-1 bis -3, H-C-4506-1 bis -3, H-C-5046-1 bis -3, H-D-4506-1 bis -3, H-D-5046-1 bis -3) erkannte einlesen.py die Randzeilen nicht; die Fundorte wurden am Seitenbild abgezählt. Alle Bedingungen sind gleich betroffen | DAT-61, Lieferschein Nachtrag 1, Hinweis 3, und Randzeilen_Fassungen_v1_20261115.md; Review-Projekt SB-56 (SB-43 hier) |
| BL-3 | DAT-60, hauptstudie/auswertung/Trefferbilanz_Hauptstudie_v1_20261115.md, Abschnitt "K9 Regelvorschläge" | "Fälle, die beide Vorschlagsläufe R und R2 sammeln: 44"; "Fallpaare, die R und R2 gleich gruppieren: 897 von 946 (94,8 %)" | 52 Fälle; 1241 von 1326 Fallpaaren (93,6 %) | DAT-63, Nachrechnung 6.1: der Abgleich in rq3/k9_vergleich.py vergleicht Kennungen als reine Zeichenkette, Zusätze wie "GB-34 (1)" und ein Komma statt "/" verhindern sechs Zuordnungen, Fälle mit gleichem Lauf und gleicher Kennung werden zusammengelegt |

## 2. Rückmeldung an den Review-Chat

```
Rückmeldung aus Paper 3 zur Lieferung der Hauptstudie vom 2026-11-15:

1. Trefferbilanz, Abschnitt "Vergleich mit der bisherigen Trefferbilanz":
   Der Satz "Die neue Zählung nutzt die Einwände der öffentlichen
   Gutachten" stimmt nur für HOR. Für LAM und TCD stammen die Einwände
   aus den Gutachten des KI-Peer-Review-Dienstes (eure Auskunft vom
   2026-10-17; Spalte Herkunft der Sollbefundlisten). Bitte berichtigen.

2. Laufregister: In 24 der 48 Läufe (alle Läufe zu egusphere-2025-4506
   und egusphere-2025-5046, Bedingungen A bis D) wurden die Fundorte am
   Seitenbild abgezählt, weil einlesen.py die Randzeilen nicht erkannte
   (Nachtrag 1, Hinweis 3). Bitte als Korrekturzeilen nach der Regel des
   Laufregisters vermerken.

3. K9 (Trefferbilanz, Abschnitt "K9 Regelvorschläge"): Die unabhängige
   Nachrechnung ergibt 52 statt 44 Fälle, die R und R2 beide sammeln, und
   1241 von 1326 gleich gruppierte Fallpaare (93,6 %) statt 897 von 946
   (94,8 %). Ursache: k9_vergleich.py gleicht Kennungen als reine
   Zeichenkette ab; Zusätze wie "GB-34 (1)" und ein Komma statt "/"
   verhindern sechs Zuordnungen, und Fälle mit gleichem Lauf und gleicher
   Kennung werden zusammengelegt. Paper 3 arbeitet mit 52 und 93,6 %.

4. Laufregister: Die Spalte Verifikation ist in allen 48 Zeilen der
   Hauptstudie leer, und das bedienende Modell ist nicht vermerkt.

5. Lieferumfang: Die Belege zur zweiten, unabhängigen Extraktion
   (extraktion2/, abgleich/) fehlen in der Lieferung.

6. Die Abzählung am Seitenbild in 24 Läufen steht nicht als Nachtrag im
   Studienprotokoll, Abschnitt 13.
```
