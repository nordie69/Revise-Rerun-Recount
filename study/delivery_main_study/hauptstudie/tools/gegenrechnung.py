"""7.8, Gegenrechnung: rechnet die Kernzahlen der Trefferbilanz unabhängig aus den Rohdateien nach,
ohne Code aus auswertung.py, k8_mehrheit.py oder trefferbilanz.py. Vergleicht danach jede Zahl mit der Trefferbilanz.
Rohdateien: laeufe/laufplan.json, laeufe/nachverarbeitung.json, soll/<M>/sollbefunde.md, laeufe/zuordnung/<N>/zuordnung1..3.md,
einstufung/endgueltig_einzelbefunde.json, laeufe/ergebnis/<L>/*_Gutachten.md, auswertung/k8/<N>/zaehlung1..3.md."""
import csv, glob, io, itertools, json, re, statistics
from collections import Counter, defaultdict
HS = '/home/claude/gutachten-skill/hauptstudie'

def md_rows(path):
    """Markdown-Tabellenzeilen als Zelllisten, ohne Trennzeilen; Kopfzeilen bleiben, der Aufrufer filtert."""
    out = []
    for line in open(path, encoding='utf-8').read().splitlines():
        line = line.strip()
        if not (line.startswith('|') and line.endswith('|')): continue
        cells = [c.strip() for c in line[1:-1].split('|')]
        if all(re.fullmatch(r':?-{3,}:?', c) for c in cells): continue
        out.append(cells)
    return out

laufplan = json.load(open(f'{HS}/laeufe/laufplan.json', encoding='utf-8'))
nmap = json.load(open(f'{HS}/laeufe/nachverarbeitung.json', encoding='utf-8'))

# 1. Sollbefunde je Manuskript: Art und Herkunft
soll = {}
for p in glob.glob(f'{HS}/soll/*/sollbefunde.md'):
    M = p.split('/')[-2]
    for c in md_rows(p):
        if re.fullmatch(r'\d{4}-RC\d-\d+', c[0]) and c[4] == 'bestätigt':
            soll[c[0]] = dict(M=M, inh=(c[2] == 'inhaltlich'), g03=(M == '4506' and c[1].split(',')[0].strip() == 'RC3'))
print('Sollbefunde', len(soll), 'inhaltlich', sum(v['inh'] for v in soll.values()), 'G03', sum(v['g03'] for v in soll.values()))

# 2. Mehrheit je Sollbefund direkt aus den drei Zuordnungen
def antworten(N, k):
    d = {}
    for c in md_rows(f'{HS}/laeufe/zuordnung/{N}/zuordnung{k}.md'):
        if c[0] in soll and len(c) >= 2:
            d[c[0]] = (c[1].strip().lower(), set(re.findall(r'(?:GB|KK)-\d+', c[2] if len(c) > 2 else '')))
    return d
gut = {}
for r in laufplan:
    L, N, M = r['code'], nmap[r['code']], r['manuskript']
    A = [antworten(N, k) for k in (1, 2, 3)]
    ids = [s for s in soll if soll[s]['M'] == M]
    maj, gleich, eintr = {}, 0, defaultdict(int)
    for s in ids:
        a = [x.get(s, ('fehlt', set()))[0] for x in A]
        top = Counter(a).most_common(1)[0]
        maj[s] = top[0] if top[1] >= 2 else 'ohne'
        gleich += len(set(a)) == 1
    gut[L] = dict(bed=r['bedingung'], wdh=r['wdh'], M=M, maj=maj, A=A, ids=ids)

def k1(L, inh=True, art='getroffen', ohne_g03=False):
    ids = [s for s in gut[L]['ids'] if soll[s]['inh'] == inh and not (ohne_g03 and soll[s]['g03'])]
    return sum(gut[L]['maj'][s] == art for s in ids), len(ids)

def lauf_werte(fn):
    out = {}
    for b in 'ABCD':
        v = []
        for w in (1, 2, 3):
            Ls = [L for L in gut if gut[L]['bed'] == b and gut[L]['wdh'] == w]
            z = [fn(L) for L in Ls]
            v.append(sum(x for x, _ in z) / sum(y for _, y in z))
        out[b] = v
    return out

R = {}
for og in (False, True):
    t = 'ohne' if og else 'mit'
    R[f'K1 inh getroffen {t}'] = lauf_werte(lambda L: k1(L, True, 'getroffen', og))
    R[f'K1 inh teilweise {t}'] = lauf_werte(lambda L: k1(L, True, 'teilweise', og))
    R[f'K1 kk getroffen {t}'] = lauf_werte(lambda L: k1(L, False, 'getroffen', og))
    R[f'K1 kk teilweise {t}'] = lauf_werte(lambda L: k1(L, False, 'teilweise', og))
    R[f'K7 zuordnung {t}'] = lauf_werte(lambda L: (sum(len({x.get(s, ("fehlt",))[0] for x in gut[L]['A']}) == 1 for s in gut[L]['ids'] if not (og and soll[s]['g03'])),
                                                   sum(1 for s in gut[L]['ids'] if not (og and soll[s]['g03']))))

# 3. K2 aus den endgültigen Urteilen
ein = json.load(open(f'{HS}/einstufung/endgueltig_einzelbefunde.json', encoding='utf-8'))
jeL = defaultdict(list)
for e in ein: jeL[e['code']].append(e)
R['K2'] = lauf_werte(lambda L: (sum(e['urteil'] == 'nicht zutreffend' for e in jeL[L]), len(jeL[L])))
R['Einträge je Gutachten'] = lauf_werte(lambda L: (len(jeL[L]), 1))

# 4. K6: Quelle je zutreffendem Eintrag direkt aus dem Gutachten
def quellen(L):
    p = glob.glob(f'{HS}/laeufe/ergebnis/{L}/*_Gutachten.md')[0]; txt = open(p, encoding='utf-8').read()
    q = {}
    for m in re.finditer(r'\*\*(GB-\d+)\b.*?(?=\*\*GB-\d+|\n#{1,4} |\Z)', txt, re.S):
        s = re.search(r'\|\s*Source\s*\|\s*([^|\n]*)\|', m.group(0)); q[m.group(1)] = s.group(1) if s else ''
    kopf = None
    for line in txt.splitlines():
        if line.startswith('|'):
            c = [x.strip() for x in line.strip().strip('|').split('|')]
            if 'Source' in c: kopf = c; continue
            if c and re.fullmatch(r'KK-\d+', c[0]) and kopf and len(c) == len(kopf):
                q[c[0]] = c[kopf.index('Source')]
        else:
            if not line.strip(): pass
    return q
def k6(L):
    q = quellen(L); z = [e for e in jeL[L] if e['urteil'] == 'zutreffend']
    return sum(len(set(re.findall(r'\b(?:S[1-4]|AB|SD)\b', q.get(e['kennung'], '')))) == 1 for e in z), len(z)
R['K6'] = lauf_werte(k6)

# 5. K8 direkt aus den drei Zählungen
def k8(L, klassen):
    N = nmap[L]; c = Counter()
    for k in (1, 2, 3):
        f = set()
        for z in md_rows(f'{HS}/auswertung/k8/{N}/zaehlung{k}.md'):
            m = re.match(r'(K4|F[1-7])', z[0])
            if not m: continue
            ids = tuple(sorted(set(re.findall(r'(?:GB|KK)-\d+', z[1]))))
            if not ids: continue
            if m.group(1) in ('K4', 'F7'): f.add((m.group(1), ids))
            else: f |= {(m.group(1), (i,)) for i in ids}
        c.update(f)
    return sum(1 for (kl, _), n in c.items() if n >= 2 and kl in klassen), 1
R['F1 bis F7'] = lauf_werte(lambda L: k8(L, {f'F{i}' for i in range(1, 8)}))
for kl in ['K4'] + [f'F{i}' for i in range(1, 8)]:
    R[kl] = lauf_werte(lambda L, kl=kl: k8(L, {kl}))

# 6. Vergleich mit der Trefferbilanz
tb = open(f'{HS}/auswertung/Trefferbilanz_Hauptstudie_v1_20261115.md', encoding='utf-8').read()
def fmt(v, p, d):
    g = lambda x: f'{(100 if p else 1)*x:.{d}f}'.replace('.', ',')
    return f'{g(statistics.mean(v))} ({g(min(v))} bis {g(max(v))})'
pruef = [('K1 inh getroffen mit', 'K1 inhaltlich, getroffen (Hauptmaß)', 0, True, 1), ('K1 inh teilweise mit', 'K1 inhaltlich, teilweise', 0, True, 1),
         ('K1 kk getroffen mit', 'K1 Kleinkorrekturen, getroffen', 0, True, 1), ('K1 kk teilweise mit', 'K1 Kleinkorrekturen, teilweise', 0, True, 1),
         ('K1 inh getroffen ohne', 'K1 inhaltlich, getroffen (Hauptmaß)', 1, True, 1), ('K1 inh teilweise ohne', 'K1 inhaltlich, teilweise', 1, True, 1),
         ('K1 kk getroffen ohne', 'K1 Kleinkorrekturen, getroffen', 1, True, 1), ('K1 kk teilweise ohne', 'K1 Kleinkorrekturen, teilweise', 1, True, 1),
         ('K7 zuordnung mit', 'K7 Zuordnung, drei Läufe gleich', 0, True, 1), ('K7 zuordnung ohne', 'K7 Zuordnung, drei Läufe gleich', 1, True, 1),
         ('K2', 'K2 nicht zutreffend, Anteil an allen Einträgen', 0, True, 1), ('Einträge je Gutachten', 'Einträge je Gutachten', 0, False, 1),
         ('K6', 'K6 zutreffende Einträge aus nur einer Prüfinstanz', 0, True, 1), ('F1 bis F7', 'F1 bis F7 zusammen', 0, False, 2)] + \
        [(k, k, 0, False, 2) for k in ['K4'] + [f'F{i}' for i in range(1, 8)]]
ok = abw = 0
for key, label, nr, p, d in pruef:
    zeilen = [l for l in tb.splitlines() if l.startswith(f'| {label} |')]
    if len(zeilen) <= nr: print('nicht gefunden:', label, nr); abw += 1; continue
    tbz = [x.strip() for x in zeilen[nr].strip('|').split('|')][1:5]
    neu = [fmt(R[key][b], p, d) for b in 'ABCD']
    for b, x, y in zip('ABCD', tbz, neu):
        if x == y: ok += 1
        else: abw += 1; print('ABWEICHUNG', key, b, 'Trefferbilanz', x, 'Gegenrechnung', y)
# Effektregel unabhängig
def eff(v1, v2): return 'getrennt' if min(v1) > max(v2) or min(v2) > max(v1) else 'überlappen'
for t in ('mit', 'ohne'):
    k = R[f'K1 inh getroffen {t}']
    print(t, 'G03: RQ1', eff(k['A'], k['B']), '| RQ2', eff(k['B'], k['C']), 'B>C', min(k['B']) > max(k['C']), '| RQ3 K1', eff(k['B'], k['D']))
f = R['F1 bis F7']; print('RQ3 F1 bis F7', eff(f['B'], f['D']), 'D<B', max(f['D']) < min(f['B']), '| K6 B min', round(min(R['K6']['B']), 3))
print('Werte gleich', ok, 'Abweichungen', abw)

# 7. Zusatz: K3 (zutreffende Einträge ohne Sollbefund) und K5 (Spannweite K1 je Manuskript) unabhängig
def k3(L, og):
    mit = set()
    for s in gut[L]['ids']:
        if og and soll[s]['g03']: continue
        if gut[L]['maj'][s] in ('getroffen', 'teilweise'):
            n = Counter(e for x in gut[L]['A'] if x.get(s, ('', set()))[0] in ('getroffen', 'teilweise') for e in x[s][1])
            mit |= {e for e, k in n.items() if k >= 2}
    return sum(1 for e in jeL[L] if e['urteil'] == 'zutreffend' and e['kennung'] not in mit), 1
abw2 = 0
for og, nr in ((False, 0), (True, 1)):
    z = [l for l in tb.splitlines() if l.startswith('| K3 Zusatzbefunde je Gutachten (Anzahl) |')][nr]
    tbz = [x.strip() for x in z.strip('|').split('|')][1:5]
    v = lauf_werte(lambda L: k3(L, og))
    for b, x in zip('ABCD', tbz):
        y = fmt(v[b], False, 1)
        if x != y: abw2 += 1; print('ABWEICHUNG K3', og, b, x, y)
for M in ('4506', '4695', '4733', '5046'):
    z = [l for l in tb.splitlines() if l.startswith(f'| {M} |')]
    k5z = [x.strip() for x in z[-1].strip('|').split('|')][1:5]   # letzte Zeile mit dem Manuskript ist die K5-Tabelle
    for b, x in zip('ABCD', k5z):
        w = [k1(L)[0] / k1(L)[1] for L in gut if gut[L]['bed'] == b and gut[L]['M'] == M]
        y = f'{100*(max(w)-min(w)):.1f}'.replace('.', ',')
        if x != y: abw2 += 1; print('ABWEICHUNG K5', M, b, x, y)
print('Zusatz K3 (8 Werte) und K5 (16 Werte): Abweichungen', abw2)
