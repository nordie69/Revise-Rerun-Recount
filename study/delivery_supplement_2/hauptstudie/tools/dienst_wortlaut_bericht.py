"""Paper 3, Entscheidung 38 und 42: Bericht über Wortgleichheiten zwischen den Dateien der Freigabe zu V4 und den
Gutachten des KI-Peer-Review-Dienstes zu LAM und TCD. Ruft dienst_wortlaut.py mit n = 6 und n = 8 auf und hängt
je Fundstelle die Einordnung an (EINORD, Lesart des Assistenten nach Sichtung von Gutachtenzeile, Dienststelle
und Manuskript). Der Bericht nennt Datei, Zeile, Länge und Einordnung, nicht den Wortlaut, damit er selbst
keinen Wortlaut des Dienstes enthält. Schreibt freigabe_e42/Pruefung_Dienstwortlaut_V4_v1_20261119.md."""
import collections, re, subprocess, sys
P = '/home/claude/gutachten-skill'
DATEIEN = ['erprobung/durchgang4/LAM_A/Listen_Answer_Memorize_Copernicus_Gutachten_20261016.md',
           'erprobung/durchgang4/LAM_B/Listen_Answer_Memorize_Copernicus_Gutachten_20261016.md',
           'erprobung/durchgang4/TCD/Talk_Check_Decide_A_Skill-Based_Workflow_Gutachten_20261016.md',
           'erprobung/durchgang4/HOR/egusphere-2025-2248_Gutachten_20261016.md',
           'erprobung/verifikation4/LAM_A_verifikation.md', 'erprobung/verifikation4/LAM_B_verifikation.md',
           'erprobung/verifikation4/TCD_verifikation.md', 'erprobung/verifikation4/HOR_verifikation.md']
MS, WE = 'Manuskript', 'Wendung'
LIT, ZIT, ABB, NAM, VER = ('Literaturangaben des Manuskripts', 'Zitat oder Satz des Manuskripts',
                           'Text oder Werte aus Abbildung oder Tabelle des Manuskripts',
                           'Modell-, Versions-, Abschnitts- oder Tabellenbezeichnungen des Manuskripts mit Bindewörtern',
                           'Abschnittstitel des Manuskripts')
# (Datei-Kurzform, Zeile, Länge): (Klasse, Begründung)
EINORD = {
 ('LAM_A', 44, 11): (MS, LIT), ('LAM_A', 222, 6): (MS, NAM), ('LAM_A', 562, 6): (MS, ABB),
 ('LAM_A', 580, 9): (MS, LIT), ('LAM_A', 580, 8): (MS, LIT), ('LAM_A', 593, 6): (MS, ZIT), ('LAM_A', 690, 6): (MS, VER),
 ('LAM_A', 496, 7): (WE, 'Satz des Manuskripts gekürzt ("; it found" zu "found"), in Gutachten und Dienst gleich gekürzt'),
 ('LAM_B', 174, 10): (MS, LIT), ('LAM_B', 176, 6): (MS, LIT),
 ('LAM_B', 486, 6): (WE, 'Zahlen und Begriffe des Manuskripts in einer Fügung, die das Manuskript nicht hat'),
 ('TCD', 14, 6): (WE, 'Wendung zu "written procedures" und "skills", im Manuskript anders gefügt'),
 ('TCD', 14, 10): (WE, 'Aufzählung der sechs Prüfachsen des Manuskripts in einer Reihenfolge, die das Manuskript nicht hat'),
 ('TCD', 108, 6): None,  # zwei Fundstellen gleicher Länge in Zeile 108, siehe ZWEI
 ('TCD', 114, 6): (WE, 'Beschreibung des Nenners einer Quote, im Manuskript nicht so formuliert'),
 ('TCD', 196, 8): (MS, ABB), ('TCD', 204, 6): (MS, NAM), ('TCD', 379, 7): (MS, ABB), ('TCD', 408, 8): (MS, NAM),
 ('TCD', 431, 8): (MS, ZIT), ('TCD', 431, 6): (MS, ABB), ('TCD', 431, 9): (MS, NAM), ('TCD', 432, 6): (MS, NAM),
 ('TCD', 445, 8): (MS, ABB), ('TCD', 470, 6): None, ('TCD', 496, 6): (MS, ABB),
 ('TCD', 509, 6): (WE, 'Wendung zur Zahl der Einträge mit DOI; das Manuskript nennt nur die Einträge'),
 ('TCD', 510, 6): (WE, 'Wendung zur Zahl der Einträge mit DOI; das Manuskript nennt nur die Einträge'),
 ('TCD', 616, 6): (MS, ABB), ('TCD', 617, 6): (MS, ABB), ('TCD', 623, 7): (MS, ABB), ('TCD', 623, 6): (MS, ABB),
 ('TCD', 626, 6): (MS, ABB), ('TCD', 641, 8): (MS, NAM), ('TCD', 680, 12): (MS, ZIT), ('TCD', 707, 6): (MS, VER),
 ('TCD', 823, 6): (MS, NAM), ('TCD', 865, 6): (MS, ABB),
 ('TCD_verifikation', 34, 6): (MS, ABB), ('TCD_verifikation', 36, 6): (MS, ABB), ('TCD_verifikation', 64, 8): (MS, ABB),
}
# Zeilen mit zwei Fundstellen gleicher Länge: Einordnung in Reihenfolge der Ausgabe
ZWEI = {('TCD', 108, 6): [(MS, NAM), (WE, 'Wendung zu den Vergleichsmodellen, im Manuskript anders gefügt')],
        ('TCD', 470, 6): [(WE, 'Begriffe einer Abbildungsunterschrift des Manuskripts mit angehängtem "are reported"'), (MS, ABB)]}

def kurz(d):
    if 'verifikation4' in d:
        b = d.split('/')[-1].replace('_verifikation.md', '')
        return 'TCD_verifikation' if b == 'TCD' else b + '_verifikation'
    return d.split('/')[-2]

def lauf(n):
    out = subprocess.run([sys.executable, f'{P}/hauptstudie/tools/dienst_wortlaut.py', str(n)] + [f'{P}/{d}' for d in DATEIEN],
                         capture_output=True, text=True, check=True).stdout
    funde, datei = [], None
    for l in out.split('\n'):
        if l.startswith('## '):
            datei = l[3:].rsplit(':', 1)[0].replace(P + '/', ''); continue
        m = re.match(r'Z\. (\d+)(?: bis (\d+))? \| (\d+) Wörter \|', l)
        if m:
            funde.append((datei, int(m.group(1)), int(m.group(3))))
    return funde

f6, f8 = lauf(6), lauf(8)
zaehl = collections.Counter(); zeilen = []
benutzt = collections.Counter()
for d, z, n in f6:
    k = (kurz(d), z, n)
    if k in ZWEI:
        e = ZWEI[k][benutzt[k]]; benutzt[k] += 1
    else:
        e = EINORD[k]
    zeilen.append((d, z, n, e)); zaehl[(kurz(d).split('_')[-1] == 'verifikation', e[0])] += 1
assert len(zeilen) == len(f6) and all(EINORD.get(k) is not None or k in ZWEI for k in {(kurz(d), z, n) for d, z, n in f6})
e8 = [x for x in zeilen if (x[0], x[1], x[2]) in set(f8)]
assert len(e8) == len(f8)
we6 = [x for x in zeilen if x[3][0] == WE]; we8 = [x for x in e8 if x[3][0] == WE]
T = ['# Prüfung auf Wortlaut des KI-Peer-Review-Dienstes in den Dateien zu Prüfdurchgang 4', '',
     'Geprüft sind die vier Gutachten und die vier Prüfberichte von Prüfdurchgang 4 gegen die beiden Gutachten des KI-Peer-Review-Dienstes zu LAM und TCD (Entscheidung 38). Eine Fundstelle ist eine längste Wortfolge von mindestens n Wörtern, die in einer geprüften Datei und in einem Gutachten des Dienstes gleich steht; Groß- und Kleinschreibung und Satzzeichen zählen nicht. Folgen, die auch im Text eines der drei Manuskripte stehen, zählt das Skript nicht mit. Jede verbliebene Fundstelle ist danach an Gutachtenzeile, Dienststelle und Manuskript gesichtet und eingeordnet:', '',
     '- **Manuskript:** Beide geben Wortlaut oder Inhalt des Manuskripts wieder, den das Skript nicht als Manuskripttext erkennt, weil er in einer Abbildung steht, über Zeilen mit Randnummern läuft oder nur aus Literaturangaben, Zahlen und Bezeichnungen besteht.',
     '- **Wendung:** Gutachten und Dienst haben dieselbe Formulierung, die das Manuskript so nicht hat. Das ist eine wörtliche Übereinstimmung mit dem Dienst; ob sie übernommen oder unabhängig entstanden ist, lässt sich nicht feststellen.', '',
     'Der Bericht nennt Datei, Zeile und Länge, nicht den Wortlaut, damit er selbst keinen Wortlaut des Dienstes enthält. Nichts wurde entfernt. Gerechnet mit `tools/dienst_wortlaut.py` und `tools/dienst_wortlaut_bericht.py`; die Einordnung ist Lesart des Assistenten.', '',
     '## Zählung', '', '| Schwelle | Fundstellen | davon Manuskript | davon Wendung | in Gutachten | in Prüfberichten |', '|---|---|---|---|---|---|']
for n, lst in ((6, zeilen), (8, e8)):
    T.append(f'| ab {n} Wörtern | {len(lst)} | {sum(1 for x in lst if x[3][0] == MS)} | {sum(1 for x in lst if x[3][0] == WE)} | {sum(1 for x in lst if "verifikation4" not in x[0])} | {sum(1 for x in lst if "verifikation4" in x[0])} |')
T += ['', 'Im Gutachten und im Prüfbericht zu Fall 3 (egusphere-2025-2248) und in den Prüfberichten zu LAM gibt es keine Fundstelle. Die längste Fundstelle der Art Wendung hat ' + str(max(x[2] for x in we6)) + ' Wörter.', '',
      '## Fundstellen der Art Wendung', '', '| Datei | Zeile | Wörter | ab 8 Wörtern | Einordnung |', '|---|---|---|---|---|']
T += [f'| `{d}` | {z} | {n} | {"ja" if n >= 8 else "nein"} | {e[1]} |' for d, z, n, e in we6]
T += ['', '## Fundstellen der Art Manuskript', '', '| Datei | Zeile | Wörter | Einordnung |', '|---|---|---|---|']
T += [f'| `{d}` | {z} | {n} | {e[1]} |' for d, z, n, e in zeilen if e[0] == MS]
T += ['', '## Grenzen', '', '- Übereinstimmungen unter sechs Wörtern sind nicht erfasst.',
      '- Sinngemäße Übernahmen ohne wörtliche Gleichheit erfasst das Verfahren nicht.',
      '- Die Einordnung beruht auf einer Sichtung durch den Assistenten, nicht auf einer unabhängigen zweiten Zählung.']
out = '\n'.join(T) + '\n'
assert '—' not in out and '–' not in out
open(f'{P}/hauptstudie/freigabe_e42/Pruefung_Dienstwortlaut_V4_v1_20261119.md', 'w', encoding='utf-8').write(out)
print(out)
