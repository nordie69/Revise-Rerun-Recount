"""Werte für IG-GB der Gruppen 1 bis 3 (DAT-89) aus dem Repositorium und der Nachrechnung 6-1."""
import json, re, glob, collections, itertools, math
HS = '/home/claude/revise-rerun-recount/study/delivery_main_study/hauptstudie'
NR = json.load(open('/home/claude/Paper3/nachrechnung_6-1/ergebnis.json'))['kennzahlen']
def tab(p):
    out = []
    for l in open(p, encoding='utf-8'):
        if l.startswith('|') and not re.match(r'^\|\s*-', l):
            out.append([x.strip() for x in l.strip().strip('|').split('|')])
    return out[1:]
plan = {r['code']: r for r in json.load(open(f'{HS}/laeufe/laufplan.json'))}
nv = json.load(open(f'{HS}/laeufe/nachverarbeitung.json'))
SOLL = {}
for M in ('4506', '4695', '4733', '5046'):
    for c in tab(f'{HS}/soll/{M}/sollbefunde.md'):
        if len(c) >= 7 and c[4] == 'bestätigt':
            SOLL[c[0]] = {'M': M, 'art': c[2], 'g03': M == '4506' and c[1].startswith('RC3')}
R = {}
INST = re.compile(r'\b(S[1-4]|AB|SD)\b')
for L, r in plan.items():
    N = nv[L]; M = r['manuskript']
    mh = [x for x in tab(f'{HS}/laeufe/zuordnung/{N}/mehrheit.md') if x[0] in SOLL]
    g = open(glob.glob(f'{HS}/laeufe/ergebnis/{L}/*_Gutachten.md')[0], encoding='utf-8').read()
    quelle = {}
    for mm in re.finditer(r'\*\*(GB-\d+)\b.*?(?=\*\*GB-\d+|\n#{1,4} |\Z)', g, re.S):
        sq = re.search(r'\|\s*Source\s*\|\s*([^|\n]*)\|', mm.group(0)); quelle[mm.group(1)] = sq.group(1) if sq else ''
    kopf = None
    for zl in g.splitlines():
        if zl.startswith('|'):
            zc = [x.strip() for x in zl.strip().strip('|').split('|')]
            if 'Source' in zc: kopf = zc; continue
            if zc and re.fullmatch(r'KK-\d+', zc[0]) and kopf and len(zc) == len(kopf): quelle[zc[0]] = zc[kopf.index('Source')]
    R[L] = {'bed': r['bedingung'], 'M': M, 'wdh': r['wdh'], 'N': N, 'mh': mh, 'quelle': quelle}
E = json.load(open(f'{HS}/einstufung/endgueltig_einzelbefunde.json'))
out = {}
BED = 'ABCD'; MS = ('4733', '4506', '4695', '5046')
def rng(v): return [round(sum(v) / len(v), 4), round(min(v), 4), round(max(v), 4)]
# 1 Treffer je Manuskript, Bedingung, Wiederholung (inhaltlich)
def treffer(L, ohne=False, art='inhaltlich', mit_teil=False):
    u = [x for x in R[L]['mh'] if SOLL[x[0]]['art'] == art and not (ohne and SOLL[x[0]]['g03'])]
    h = sum(x[4] == 'getroffen' or (mit_teil and x[4] == 'teilweise') for x in u)
    return h, len(u)
# 2 B minus C je Manuskript
bc = {}
for ohne in (False, True):
    for M in MS:
        hb = sum(treffer(L, ohne)[0] for L in R if R[L]['bed'] == 'B' and R[L]['M'] == M)
        hc = sum(treffer(L, ohne)[0] for L in R if R[L]['bed'] == 'C' and R[L]['M'] == M)
        n = treffer([L for L in R if R[L]['M'] == M][0], ohne)[1]
        bc[f"{M}{'_ohne' if ohne else ''}"] = {'n': n, 'B': hb, 'C': hc, 'B-C': hb - hc}
out['B_minus_C'] = bc
# 3 Manuskript als Einheit: Mittel der vier Manuskriptquoten je Wiederholung
mu = {}
for ohne in (False, True):
    for b in BED:
        vals = []
        for w in (1, 2, 3):
            q = []
            for M in MS:
                L = [L for L in R if R[L]['bed'] == b and R[L]['M'] == M and R[L]['wdh'] == w][0]
                h, n = treffer(L, ohne); q.append(h / n)
            vals.append(sum(q) / 4)
        mu[f"{b}{'_ohne' if ohne else ''}"] = rng([100 * v for v in vals])
out['Manuskript_als_Einheit'] = mu
# 4 Gepoolt ohne je ein Manuskript, B und C
lomo = {}
for ohne in (False, True):
    for weg in MS:
        for b in 'BC':
            vals = []
            for w in (1, 2, 3):
                H = N_ = 0
                for M in MS:
                    if M == weg: continue
                    L = [L for L in R if R[L]['bed'] == b and R[L]['M'] == M and R[L]['wdh'] == w][0]
                    h, n = treffer(L, ohne); H += h; N_ += n
                vals.append(100 * H / N_)
            lomo[f"ohne {weg}{' ohne RC3' if ohne else ''} {b}"] = rng(vals)
out['ohne_je_ein_Manuskript'] = lomo
# 5 K1 getroffen oder teilweise (Sensitivität), gepoolt
sens = {}
for b in BED:
    vals = []
    for w in (1, 2, 3):
        H = N_ = 0
        for L in R:
            if R[L]['bed'] == b and R[L]['wdh'] == w:
                h, n = treffer(L, mit_teil=True); H += h; N_ += n
        vals.append(100 * H / N_)
    sens[b] = rng(vals)
out['K1_getroffen_oder_teilweise'] = sens
# 6 K6 Zähler und Nenner, Verteilung je Instanz, Mehrfachnennung
k6 = {}
for b in BED:
    zutr = eins = mehr = keine = 0; jeinst = collections.Counter()
    for L in R:
        if R[L]['bed'] != b: continue
        for e in E:
            if e['code'] == L and e['urteil'] == 'zutreffend':
                zutr += 1
                inst = set(INST.findall(R[L]['quelle'].get(e['kennung'], '')))
                if len(inst) == 1: eins += 1; jeinst[next(iter(inst))] += 1
                elif len(inst) > 1: mehr += 1
                else: keine += 1
    k6[b] = {'zutreffend': zutr, 'eine_Instanz': eins, 'mehrere': mehr, 'keine': keine, 'je_Instanz': dict(sorted(jeinst.items()))}
out['K6'] = k6
# 7 B ohne je eine Instanz: K1 gepoolt (Sollbefund bleibt getroffen, wenn ein genannter Eintrag eine andere Instanz oder keine nennt)
loio = {}
for weg in ('S1', 'S2', 'S3', 'S4', 'AB', 'SD'):
    for b in ('B', 'D'):
        vals = []
        for w in (1, 2, 3):
            H = N_ = 0
            for L in R:
                if R[L]['bed'] != b or R[L]['wdh'] != w: continue
                for x in R[L]['mh']:
                    if SOLL[x[0]]['art'] != 'inhaltlich': continue
                    N_ += 1
                    if x[4] != 'getroffen': continue
                    ids = re.findall(r'\b(?:GB|KK)-\d+\b', x[5] if len(x) > 5 else '')
                    bleibt = any(set(INST.findall(R[L]['quelle'].get(i, ''))) - {weg} or not INST.findall(R[L]['quelle'].get(i, '')) for i in ids)
                    H += bleibt
            vals.append(100 * H / N_)
        loio[f'{b} ohne {weg}'] = rng(vals)
out['ohne_je_eine_Instanz'] = loio
# 8 Urteile der Verifikation je Bedingung
ver = {}
for b in BED:
    c = collections.Counter()
    for L in R:
        if R[L]['bed'] != b: continue
        for x in tab(f"{HS}/laeufe/verifikation/{R[L]['N']}/verifikation.md"):
            if len(x) >= 2 and re.fullmatch(r'(GB|KK)-\d+', x[0]):
                c[x[1].lower()] += 1
    ver[b] = dict(c)
out['Verifikation'] = ver
# 9 K8 je Klasse, Summe ohne F7, F1/F2 je Weg
K8 = json.load(open(f'{HS}/auswertung/k8/mehrheit.json'))
k8 = {}
for b in BED:
    s = {f: sum(v[f] for v in K8.values() if v['bed'] == b) for f in ['F1', 'F2', 'F3', 'F4', 'F5', 'F6', 'F7']}
    weg = {}
    for pfad, Ms in (('Seitenbilder', ('4506', '5046')), ('Skript', ('4733', '4695'))):
        for f in ('F1', 'F2'):
            weg[f'{f} {pfad}'] = sum(v[f] for v in K8.values() if v['bed'] == b and v['M'] in Ms)
    ohneF7 = []
    for w in (1, 2, 3):
        vs = [v for v in K8.values() if v['bed'] == b and v['wdh'] == w]
        ohneF7.append(sum(v['F_summe'] - v['F7'] for v in vs) / len(vs))
    k8[b] = {'Fälle': s, 'Summe': sum(s.values()), 'ohne_F7_je_Gutachten': rng(ohneF7), 'Weg': weg}
out['K8'] = k8
# 10 Clopper-Pearson 3 von 60
from math import comb
def cp(k, n, a=0.05):
    def cdf(p, kk): return sum(comb(n, i) * p**i * (1 - p)**(n - i) for i in range(kk + 1))
    lo, hi = 0.0, 1.0
    if k > 0:
        a_, b_ = 0.0, 1.0
        for _ in range(100):
            m = (a_ + b_) / 2
            if 1 - cdf(m, k - 1) < a / 2: a_ = m
            else: b_ = m
        lo = a_
    a_, b_ = 0.0, 1.0
    for _ in range(100):
        m = (a_ + b_) / 2
        if cdf(m, k) > a / 2: a_ = m
        else: b_ = m
    hi = a_
    return round(100 * lo, 1), round(100 * hi, 1)
out['CP_3_von_60'] = cp(3, 60)
# 11 Effektregel: Fehlerrate bei drei gegen drei
out['Effektregel'] = {'zweiseitig': 2 / comb(6, 3), 'gerichtet': 1 / comb(6, 3), 'vier': 2 / comb(8, 4), 'fuenf': 2 / comb(10, 5)}
# 12 Tabelle A2 aus der Nachrechnung
def nr(k, b, f=100, d=1):
    v = NR[k][b]; return f"{v['mittel']*f:.{d}f} ({v['min']*f:.{d}f} to {v['max']*f:.{d}f})"
out['A2'] = {b: {
    'K1 subst hit': nr('K1 inhaltlich getroffen (mit G03)', b), 'K1 subst partial': nr('K1 inhaltlich teilweise (mit G03)', b),
    'K1 minor hit': nr('K1 Kleinkorrekturen getroffen (mit G03)', b), 'K1 minor partial': nr('K1 Kleinkorrekturen teilweise (mit G03)', b),
    'K2': nr('K2 nicht zutreffend', b), 'K2 opinion': nr('K2 Nebenwert Ansichtssache', b),
    'K3': nr('K3 Zusatzbefunde je Gutachten, Variante b (mit G03)', b, 1), 'K4': nr('K4 Doppelungen je Gutachten (Mehrheit der Zaehler)', b, 1, 2),
    'K5 range': f"{NR['K5 Spannweite K1 inhaltlich getroffen (mit G03)'][b]['wert']*100:.1f}",
    'K5 sev': NR['K5 Anteil gleicher Schweregrade'][b]['getroffen_oder_teilweise'],
    'K6': nr('K6 Anteil aus nur einer Instanz', b), 'K7': nr('K7 Zuordnung drei Laeufe gleich (mit G03)', b),
    'K8': nr('K8 F1 bis F7 je Gutachten', b, 1, 2), 'entries': nr('Eintraege je Gutachten', b, 1)} for b in BED}
json.dump(out, open('/home/claude/Paper3/nachrechnung_8-1/gruppe1_3.json', 'w'), ensure_ascii=False, indent=1)
print(json.dumps(out, ensure_ascii=False, indent=1))

# 13 Urteile der Verifikation, nur erste Tabelle je Prüfbericht (Abschnitt "Urteil(e) je Kennung"), erste Nennung je Kennung
ver = {}
for b in BED:
    c = collections.Counter()
    for L in R:
        if R[L]['bed'] != b: continue
        s = open(f"{HS}/laeufe/verifikation/{R[L]['N']}/verifikation.md", encoding='utf-8').read()
        m = re.search(r'^## [^\n]*Urteile? je Kennung[^\n]*\n(.*?)(?=^## |\Z)', s, re.S | re.M)
        seen = set()
        for l in m.group(1).split('\n'):
            x = [y.strip() for y in l.strip().strip('|').split('|')]
            if len(x) >= 2 and re.fullmatch(r'(GB|KK)-\d+', x[0]) and x[0] not in seen:
                seen.add(x[0]); c[x[1].lower()] += 1
    ver[b] = dict(c)
out['Verifikation'] = ver
# 14 Endgültige Urteile der Einträge mit einem Fall F1 bis F7
U = {(e['code'], e['kennung']): e['urteil'] for e in E}
fu = {}
for b in BED:
    ids = {(L, k) for L, v in K8.items() if v['bed'] == b for f, ks in v['faelle'] if f.startswith('F') for k in ks}
    fu[b] = {'Einträge': len(ids), **collections.Counter(U.get(i, '?') for i in ids)}
out['Urteil_Eintraege_mit_Fall'] = fu
json.dump(out, open('/home/claude/Paper3/nachrechnung_8-1/gruppe1_3.json', 'w'), ensure_ascii=False, indent=1)
print('VER', json.dumps(ver, ensure_ascii=False)); print('FU', json.dumps(fu, ensure_ascii=False))
