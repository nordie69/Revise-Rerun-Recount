"""Werte für Gutachten 3 (DAT-113) aus dem Repositorium: Zuordnung zu Wiederholungen, frühe Läufe, Trennschärfe der Effektregel."""
exec(open('gruppe1_3.py').read().split('# 2 B minus C')[0])
import random, statistics
out = {}
lr = {}
for l in open(f'{HS}/Laufregister.md', encoding='utf-8'):
    c = [x.strip() for x in l.strip().strip('|').split('|')]
    if len(c) > 3 and c[0].startswith('H-'): lr[c[0]] = c[1]
frueh = sorted([k for k, d in lr.items() if d < '2026-10-22'], key=lambda k: lr[k])
out['fruehe_Laeufe'] = [[k, lr[k]] for k in frueh]
out['Welle_gleich_Wiederholung'] = all(plan[L]['welle'] == plan[L]['wdh'] for L in plan)
# Treffer je Gutachten
T = {}
for L in R:
    h, n = treffer(L); T[(R[L]['bed'], R[L]['M'], R[L]['wdh'])] = (h, n)
N = {M: T[('B', M, 1)][1] for M in MS}; NT = sum(N.values())
# K1 je Bedingung ohne die frühen Läufe: nur Wiederholungen 2 und 3
fr = {(k.split('-')[1], k.split('-')[2], int(k.split('-')[3])) for k in frueh}
out['frueh_je_Bedingung'] = dict(collections.Counter(b for b, m, w in fr))
k1_23 = {}
for b in BED:
    v = [100 * sum(T[(b, M, w)][0] for M in MS) / NT for w in (2, 3)]
    k1_23[b] = [round(x, 2) for x in v]
out['K1_nur_Wdh_2_3'] = k1_23
# alle Zuordnungen der drei Gutachten je Manuskript zu Wiederholungen
def bereiche(b):
    h = {M: [T[(b, M, w)][0] for w in (1, 2, 3)] for M in MS}
    res = []
    fest = MS[0]
    for p2 in itertools.permutations(range(3)):
        for p3 in itertools.permutations(range(3)):
            for p4 in itertools.permutations(range(3)):
                perm = {MS[0]: (0, 1, 2), MS[1]: p2, MS[2]: p3, MS[3]: p4}
                s = [sum(h[M][perm[M][w]] for M in MS) for w in range(3)]
                res.append((min(s), max(s)))
    return res
BR = {b: bereiche(b) for b in BED}
def anteil(x, y):
    a = sum(1 for p in BR[x] for q in BR[y] if p[0] > q[1]); n = len(BR[x]) * len(BR[y]); return [a, n, round(100 * a / n, 1)]
out['Zuordnungen_je_Bedingung'] = len(BR['A'])
out['getrennt_ueber_alle_Zuordnungen'] = {'B ueber C': anteil('B', 'C'), 'C ueber B': anteil('C', 'B'), 'A ueber B': anteil('A', 'B'), 'B ueber A': anteil('B', 'A'), 'B ueber D': anteil('B', 'D'), 'D ueber B': anteil('D', 'B')}
gem = {b: (min(sum(T[(b, M, w)][0] for M in MS) for w in (1, 2, 3)), max(sum(T[(b, M, w)][0] for M in MS) for w in (1, 2, 3))) for b in BED}
out['berichtete_Bereiche_Treffer'] = gem
out['berichtete_Bereiche_erreicht_von'] = {b: sum(1 for p in BR[b] if p == gem[b]) for b in BED}
# Trennschärfe der Effektregel: drei gegen drei, Normalverteilung mit der Streuung von B
kB = [100 * sum(T[('B', M, w)][0] for M in MS) / NT for w in (1, 2, 3)]
sd = statistics.stdev(kB); out['K1_B_Wiederholungen'] = [round(x, 2) for x in kB]; out['SD_B'] = round(sd, 2)
random.seed(20261119); n = 200000; pw = {}
for d in (5, 7, 10):
    t = 0
    for _ in range(n):
        a = [random.gauss(0, sd) for _ in range(3)]; c = [random.gauss(d, sd) for _ in range(3)]
        t += min(c) > max(a)
    pw[d] = round(100 * t / n, 1)
out['Trennschaerfe_Prozent'] = pw
out['Fehlerrate_ohne_Unterschied'] = {k: round(100 * 2 / math.comb(2 * k, k), 4) for k in (3, 5, 10)}
json.dump(out, open('gutachten3.json', 'w'), ensure_ascii=False, indent=1)
print(json.dumps(out, ensure_ascii=False, indent=1))
# Manuskript als Einheit über alle Zuordnungen, B gegen C
def mu_bereiche(b):
    q = {M: [100 * T[(b, M, w)][0] / N[M] for w in (1, 2, 3)] for M in MS}
    res = []
    for p2 in itertools.permutations(range(3)):
        for p3 in itertools.permutations(range(3)):
            for p4 in itertools.permutations(range(3)):
                perm = {MS[0]: (0, 1, 2), MS[1]: p2, MS[2]: p3, MS[3]: p4}
                s = [sum(q[M][perm[M][w]] for M in MS) / 4 for w in range(3)]
                res.append((min(s), max(s)))
    return res
MB, MC = mu_bereiche('B'), mu_bereiche('C')
a = sum(1 for p in MB for q in MC if p[0] > q[1]); out['Einheit_Manuskript_B_ueber_C'] = [a, len(MB) * len(MC), round(100 * a / (len(MB) * len(MC)), 1)]
# Leave-out-Tabelle mit Rundung halb auf
from decimal import Decimal, ROUND_HALF_UP
def r1(x): return str(Decimal(str(x)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP))
G13 = json.load(open('gruppe1_3.json'))
tab_ = {}
for k, v in list(G13['ohne_je_ein_Manuskript'].items()) + list(G13['ohne_je_eine_Instanz'].items()):
    tab_[k] = f'{r1(v[0])} ({r1(v[1])} to {r1(v[2])})'
out['Tabelle_C2'] = tab_
json.dump(out, open('gutachten3.json', 'w'), ensure_ascii=False, indent=1)
print(out['Einheit_Manuskript_B_ueber_C']); print(json.dumps(tab_, indent=0, ensure_ascii=False))
