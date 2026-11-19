"""Paper 3, Anfrage zu Entscheidung 38: Sucht in Dateien wörtliche Wiedergaben aus den Gutachten des
KI-Peer-Review-Dienstes zu LAM und TCD (korpus/Review_*.md und .txt).

Aufruf: python3 dienst_wortlaut.py <n> <datei> [<datei> ...]

Verfahren: Wörter in Kleinschreibung nach NFKC (Ligaturen aufgelöst; Buchstaben, Ziffern, Apostroph, Bindestrich im Wort). Eine Fundstelle
ist eine längste Folge von Wörtern einer Zieldatei, in der jede Gruppe von n aufeinanderfolgenden Wörtern
auch in einem Gutachten des Dienstes steht. Steht jede dieser Gruppen auch im Text eines der drei Manuskripte
(LAM, TCD, Fall 3; pdftotext, Randnummern entfernt, Silbentrennung am Zeilenende aufgelöst), ist die Folge Manuskriptwortlaut, den
beide zitieren, und zählt nicht als Wortlaut des Dienstes. Ausgabe je Fundstelle: Datei, Zeile(n), Länge in
Wörtern, Wortlaut. Liest nur; ändert nichts.
"""
import re
import subprocess
import unicodedata
import sys

P = '/home/claude/gutachten-skill'
DIENST = [f'{P}/korpus/Review_Listen-Feedback-Memorize.md', f'{P}/korpus/Review_Listen-Feedback-Memorize.txt',
          f'{P}/korpus/Review_Talk-Check-Decide.md', f'{P}/korpus/Review_Talk-Check-Decide.txt']
MANUS = [f'{P}/korpus/Listen_Answer_Memorize_Copernicus.pdf', f'{P}/korpus/Talk_Check_Decide_A_Skill-Based_Workflow.pdf',
         f'{P}/korpus/egusphere-2025-2248.pdf']
WORT = re.compile(r"[0-9a-zäöüßà-ÿ]+(?:['’\-][0-9a-zäöüßà-ÿ]+)*")


def woerter(text):
    # NFKC löst Ligaturen (fi, fl) und Sonderformen auf; Bindestriche und Apostrophe vereinheitlicht
    t = unicodedata.normalize('NFKC', text).lower()
    t = re.sub('[\u2010\u2011\u2012\u00ad]', '-', t).replace('’', "'")
    return WORT.findall(t)


def gruppen(ws, n):
    return {tuple(ws[i:i + n]) for i in range(len(ws) - n + 1)}


def pdftext(p):
    t = subprocess.run(['pdftotext', p, '-'], capture_output=True, text=True, check=True).stdout
    t = re.sub(r'(?m)^\s*\d{1,4}\s*$\n?', '', t)  # Randnummern als eigene Zeilen entfernen
    return re.sub(r'(\w)-\n(\w)', r'\1\2', t)


def main():
    n = int(sys.argv[1])
    dienst = set()
    for d in DIENST:
        dienst |= gruppen(woerter(open(d, encoding='utf-8').read()), n)
    manus = set()
    for m in MANUS:
        manus |= gruppen(woerter(pdftext(m)), n)
    gesamt = 0
    for datei in sys.argv[2:]:
        ws, zeile = [], []
        for nr, l in enumerate(open(datei, encoding='utf-8'), 1):
            w = woerter(l)
            ws += w
            zeile += [nr] * len(w)
        treffer = [tuple(ws[i:i + n]) in dienst for i in range(len(ws) - n + 1)]
        i = 0
        funde = []
        while i < len(treffer):
            if not treffer[i]:
                i += 1
                continue
            j = i
            while j + 1 < len(treffer) and treffer[j + 1]:
                j += 1
            gr = [tuple(ws[k:k + n]) for k in range(i, j + 1)]
            if not all(g in manus for g in gr):
                funde.append((zeile[i], zeile[j + n - 1], j + n - i, ' '.join(ws[i:j + n])))
            i = j + 1
        gesamt += len(funde)
        print(f'## {datei}: {len(funde)} Fundstellen')
        for a, b, laenge, txt in funde:
            print(f'Z. {a}' + (f' bis {b}' if b != a else '') + f' | {laenge} Wörter | {txt}')
    print(f'zusammen {gesamt} Fundstellen bei n = {n}')


if __name__ == '__main__':
    main()
