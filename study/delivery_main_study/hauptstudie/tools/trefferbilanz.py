"""7.8: setzt die Trefferbilanz der Hauptstudie aus den Skriptergebnissen zusammen (keine Zahl von Hand).
Quellen: auswertung/kennzahlen_je_gutachten.json, auswertung/k8/mehrheit.json, auswertung/kennzahlen_teil1.md,
auswertung/kennzahlen_k4_k8.md, vorstudie/Nachzaehlung_Vorstudie_v1_20261115.md, rq3/Regelvorschlaege_RQ3.md,
rq3/Entscheidungen_RQ3.md, rq3/R2/k9_ergebnis.txt. Schreibt auswertung/Trefferbilanz_Hauptstudie_v1_20261115.md."""
import json, re, statistics, hashlib, collections
HS = '/home/claude/gutachten-skill/hauptstudie'; A = f'{HS}/auswertung'
G = json.load(open(f'{A}/kennzahlen_je_gutachten.json', encoding='utf-8'))
K8 = json.load(open(f'{A}/k8/mehrheit.json', encoding='utf-8'))
f = lambda x, d=1: f'{x:.{d}f}'.replace('.', ',')

def je_lauf(b, z, n, quelle=G):
    return [sum(z(quelle[L]) for L in quelle if quelle[L]['bed'] == b and quelle[L]['wdh'] == k) /
            sum(n(quelle[L]) for L in quelle if quelle[L]['bed'] == b and quelle[L]['wdh'] == k) for k in (1, 2, 3)]
def mr(v, p=100, d=1): return f'{f(p*statistics.mean(v), d)} ({f(p*min(v), d)} bis {f(p*max(v), d)})'
def getrennt(a, b): return min(a) > max(b) or min(b) > max(a)
k1 = lambda s: (lambda d: round(d[f'K1_inh_getroffen{s}'] * d[f'n_soll_inh{s}']), lambda d: d[f'n_soll_inh{s}'])
k6 = (lambda d: round(d['K6'] * d['K6_zutreffend']), lambda d: d['K6_zutreffend'])
fs = (lambda d: d['F_summe'], lambda d: 1)

# K9
s = open(f'{HS}/rq3/Regelvorschlaege_RQ3.md', encoding='utf-8').read().split('## Fälle')[1].split('\n## ')[0]
rows = [[x.strip() for x in l.split('|')[1:-1]] for l in s.split('\n') if re.match(r'\|\s*\d+\s*\|', l)]
n_faelle = len(rows); n_kl = sum(1 for r in rows if re.match(r'F[1-7]$', r[-1]))
ent = open(f'{HS}/rq3/Entscheidungen_RQ3.md', encoding='utf-8').read()
n_regeln = len(re.findall(r'^\| F[1-7] \|', ent, re.M)); n_best = len(re.findall(r'^\| F[1-7] \| bestätigt \|', ent, re.M))
k9 = open(f'{HS}/rq3/R2/k9_ergebnis.txt', encoding='utf-8').read()
m = re.search(r'gemeinsam (\d+).*?gleich gruppiert: (\d+) von (\d+)', k9, re.S)

T = ['# Trefferbilanz der Hauptstudie', '',
     'Ergebnis der Auswertung (Studienprotokoll Abschnitt 8 und 9). 48 Gutachten: vier Bedingungen, vier Manuskripte, je drei Läufe. Je Bedingung Mittelwert und Spannweite über die drei Läufe; je Lauf sind die vier Manuskripte gepoolt. Ein Unterschied gilt als Effekt, wenn sich die Spannweiten nicht überlappen (Abschnitt 9, Regel 2). Alle Zahlen sind mit den Skripten in `tools/` gerechnet.', '',
     '## Forschungsfragen', '',
     '| Frage | Vergleich | Maß | Werte | Spannweiten | Erwartung |', '|---|---|---|---|---|---|']
for s_, lab in (('', 'mit G03'), ('_ohneG03', 'ohne G03')):
    a, b, c, d = (je_lauf(x, *k1(s_)) for x in 'ABCD')
    T.append(f'| RQ1 ({lab}) | A gegen B | K1 inhaltlich, getroffen, % | A {mr(a)}; B {mr(b)} | {"getrennt" if getrennt(a, b) else "überlappen"} | {"erfüllt" if min(b) > max(a) else "nicht erfüllt"} |')
    k6b = je_lauf('B', *k6)
    T.append(f'| RQ2 ({lab}) | B gegen C | K1 inhaltlich, getroffen, %; K6 in B | B {mr(b)}; C {mr(c)}; K6 B {mr(k6b)} | {"getrennt" if getrennt(b, c) else "überlappen"} | {"erfüllt" if min(b) > max(c) and min(k6b) >= 0.2 else "nicht erfüllt"} |')
    fb, fd = je_lauf('B', *fs, quelle=K8), je_lauf('D', *fs, quelle=K8)
    T.append(f'| RQ3 ({lab}) | B gegen D | F1 bis F7 je Gutachten; K1 inhaltlich, getroffen, % | F: B {mr(fb, 1, 2)}; D {mr(fd, 1, 2)}; K1: B {mr(b)}; D {mr(d)} | F {"getrennt" if getrennt(fb, fd) else "überlappen"}; K1 {"getrennt" if getrennt(b, d) else "überlappen"} | {"erfüllt" if max(fd) < min(fb) and not min(b) > max(d) else "nicht erfüllt"} |')
T += ['', 'Erwartungen (Abschnitt 1): RQ1, B trifft mehr als A; RQ2, B trifft mehr als C und mindestens ein Fünftel der zutreffenden Befunde in B stammt aus nur einer Prüfinstanz; RQ3, D zeigt weniger Fälle der Klassen F1 bis F7 als B, ohne weniger Sollbefunde zu treffen. Ob eine Erwartung erfüllt ist, entscheidet die Effektregel (Nachtrag vom 2026-10-17).', '']
t1 = open(f'{A}/kennzahlen_teil1.md', encoding='utf-8').read().split('\n', 3)[3]
t2 = open(f'{A}/kennzahlen_k4_k8.md', encoding='utf-8').read().split('\n', 3)[3]
T += ['## Kennzahlen K1, K2, K3, K5, K6, K7', '', re.sub(r'^## ', '### ', t1, flags=re.M).strip(), '',
      '## Kennzahlen K4 und K8', '', re.sub(r'^## ', '### ', t2, flags=re.M).strip(), '',
      '## K9 Regelvorschläge', '', '| Größe | Wert |', '|---|---|',
      f'| vorgeschlagene Regeln | {n_regeln} |', f'| vom Auftraggeber bestätigt | {n_best} von {n_regeln} ({f(100*n_best/n_regeln)} %) |',
      f'| Fälle aus den Prüfberichten einer Klasse zugeordnet | {n_kl} von {n_faelle} ({f(100*n_kl/n_faelle)} %) |',
      f'| Fälle, die beide Vorschlagsläufe R und R2 sammeln | {m.group(1)} |',
      f'| Fallpaare, die R und R2 gleich gruppieren | {m.group(2)} von {m.group(3)} ({f(100*int(m.group(2))/int(m.group(3)))} %) |', '']
v = open(f'{HS}/vorstudie/Nachzaehlung_Vorstudie_v1_20261115.md', encoding='utf-8').read().split('\n', 3)[3]
T += ['## Vorstudie (getrennt berichtet)', '', re.sub(r'^## ', '### ', v, flags=re.M).strip(), '']
out = '\n'.join(T) + '\n'
assert '—' not in out and '–' not in out
open(f'{A}/Trefferbilanz_Hauptstudie_v1_20261115.md', 'w', encoding='utf-8').write(out)
print(out[:3500]); print('Zeilen', out.count('\n'), 'SHA', hashlib.sha256(out.encode()).hexdigest()[:16])
