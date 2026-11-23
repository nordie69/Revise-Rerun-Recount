"""Gruppe B der Abarbeitung (7.3-B, C-305): Zuordnungsprüfung für K8 und K6, frühe Läufe, Trennschärfe mit Streuung von A,
Unterschied B gegen C je Manuskript in Prozentpunkten, Anteil der Einträge mit Treffer (A, B), F6 bei berührenden Spannen."""
exec(open('gruppe1_3.py').read().split('# 2 B minus C')[0])
import itertools, statistics, json, collections
from scipy import stats, integrate
out = {}
K8 = json.load(open(f'{HS}/auswertung/k8/mehrheit.json'))
KZ = json.load(open(f'{HS}/auswertung/kennzahlen_je_gutachten.json'))
FK = ['F1', 'F2', 'F3', 'F4', 'F5', 'F6', 'F7']
def wert(b, M, w, f):
    v = [x for x in K8.values() if x['bed'] == b and x['M'] == M and x['wdh'] == w]; assert len(v) == 1; return v[0][f]
def perms():
    for p2 in itertools.permutations(range(3)):
        for p3 in itertools.permutations(range(3)):
            for p4 in itertools.permutations(range(3)):
                yield {MS[0]: (0, 1, 2), MS[1]: p2, MS[2]: p3, MS[3]: p4}
PERM = list(perms()); assert len(PERM) == 216
def bereiche_f(b, f):
    h = {M: [wert(b, M, w, f) for w in (1, 2, 3)] for M in MS}
    res = []
    for p in PERM:
        s = [sum(h[M][p[M][w]] for M in MS) / 4 for w in range(3)]
        res.append((min(s), max(s)))
    return res
# 1 K8 je Klasse: D unter B (Erwartung RQ3) über alle Zuordnungspaare
k8 = {}
for f in FK + ['F_summe']:
    rb, rd = bereiche_f('B', f), bereiche_f('D', f)
    unter = sum(1 for p in rd for q in rb if p[1] < q[0]); ueber = sum(1 for p in rd for q in rb if p[0] > q[1])
    ber = sum(1 for p in rd for q in rb if p[1] == q[0])
    fb = {M: [wert('B', M, w, f) for w in (1, 2, 3)] for M in MS}
    fd = {M: [wert('D', M, w, f) for w in (1, 2, 3)] for M in MS}
    k8[f] = {'D_unter_B_Prozent': round(100 * unter / len(rb) ** 2, 1), 'D_ueber_B_Prozent': round(100 * ueber / len(rb) ** 2, 1),
             'beruehrend_Prozent': round(100 * ber / len(rb) ** 2, 1), 'B_je_Gutachten': fb, 'D_je_Gutachten': fd}
out['K8_alle_Zuordnungen'] = k8
# 2 K8 ohne frühe Läufe (nur Wiederholungen 2 und 3, wie für K1)
k8_23 = {}
for f in FK + ['F_summe']:
    v = {b: [sum(wert(b, M, w, f) for M in MS) / 4 for w in (2, 3)] for b in 'BD'}
    k8_23[f] = {b: [min(v[b]), max(v[b])] for b in 'BD'}
    k8_23[f]['D_unter_B'] = max(v['D']) < min(v['B'])
out['K8_nur_Wdh_2_3'] = k8_23
# 3 K6 für B über alle Zuordnungen
def k6(M, w):
    x = [v for v in KZ.values() if v['bed'] == 'B' and v['M'] == M and v['wdh'] == w][0]
    return round(x['K6'] * x['K6_zutreffend']), x['K6_zutreffend']
h6 = {M: [k6(M, w) for w in (1, 2, 3)] for M in MS}
mins = []; maxs = []
for p in PERM:
    s = [100 * sum(h6[M][p[M][w]][0] for M in MS) / sum(h6[M][p[M][w]][1] for M in MS) for w in range(3)]
    mins.append(min(s)); maxs.append(max(s))
out['K6_B_alle_Zuordnungen'] = {'kleinstes_Minimum': round(min(mins), 1), 'groesstes_Maximum': round(max(maxs), 1), 'Erwartung_mindestens_20_in_allen': min(mins) >= 20}
out['K6_B_nur_Wdh_2_3'] = [round(100 * sum(h6[M][w - 1][0] for M in MS) / sum(h6[M][w - 1][1] for M in MS), 1) for w in (2, 3)]
# 4 B gegen C je Manuskript in Prozentpunkten je Paar aus Sollbefund und Gutachten
T = {}
for L in R:
    T[(R[L]['bed'], R[L]['M'], R[L]['wdh'])] = treffer(L)
To = {}
for L in R:
    To[(R[L]['bed'], R[L]['M'], R[L]['wdh'])] = treffer(L, ohne=True)
dif = {}
for M in MS:
    hb = sum(T[('B', M, w)][0] for w in (1, 2, 3)); hc = sum(T[('C', M, w)][0] for w in (1, 2, 3)); n = T[('B', M, 1)][1]
    hbo = sum(To[('B', M, w)][0] for w in (1, 2, 3)); hco = sum(To[('C', M, w)][0] for w in (1, 2, 3)); no = To[('B', M, 1)][1]
    dif[M] = {'Treffer_B_C': [hb, hc], 'Paare': 3 * n, 'Differenz_pp': round(100 * (hb - hc) / (3 * n), 1),
              'ohne_RC3_Treffer': [hbo, hco], 'ohne_RC3_Paare': 3 * no, 'ohne_RC3_Differenz_pp': round(100 * (hbo - hco) / (3 * no), 1)}
out['B_gegen_C_je_Manuskript'] = dif
out['Summe_Paare'] = sum(d['Paare'] for d in dif.values())
# 5 Anteil der Einträge mit Treffer (Präzision im Sinn von D'Arcy et al.)
E = json.load(open(f'{HS}/einstufung/endgueltig_einzelbefunde.json'))
pr = {}
for b in 'AB':
    je = []
    for w in (1, 2, 3):
        Ls = [L for L in R if R[L]['bed'] == b and R[L]['wdh'] == w]
        n = sum(KZ[L]['n_eintraege'] for L in Ls); z = sum(1 for e in E if e['code'] in Ls and e['quelle'].startswith('Zuordnung'))
        je.append((z, n))
    zs = sum(x[0] for x in je); ns = sum(x[1] for x in je)
    pr[b] = {'gesamt': [zs, ns, round(100 * zs / ns, 1)], 'je_Wiederholung': [round(100 * z / n, 1) for z, n in je]}
out['Anteil_Eintraege_mit_Treffer'] = pr
# 6 Trennschärfe der Spannenregel, numerisch integriert
def pw(sa, sb, d):
    f = lambda x: 3 * stats.norm.pdf(x, 0, sa) * stats.norm.cdf(x, 0, sa) ** 2 * (1 - stats.norm.cdf(x, d, sb)) ** 3
    return round(100 * integrate.quad(f, -80, 80)[0], 1)
kA = [100 * sum(T[('A', M, w)][0] for M in MS) / sum(T[('A', M, w)][1] for M in MS) for w in (1, 2, 3)]
kB = [100 * sum(T[('B', M, w)][0] for M in MS) / sum(T[('B', M, w)][1] for M in MS) for w in (1, 2, 3)]
sa, sb = statistics.stdev(kA), statistics.stdev(kB)
out['Trennschaerfe'] = {'SD_A': round(sa, 2), 'SD_B': round(sb, 2), 'gleiche_Streuung_B': {d: pw(sb, sb, d) for d in (5, 7)}, 'A_mit_eigener_Streuung': {d: pw(sa, sb, d) for d in (5, 7)}}
json.dump(out, open('gruppe_b.json', 'w'), ensure_ascii=False, indent=1)
print(json.dumps({k: v for k, v in out.items() if k != 'K8_alle_Zuordnungen'}, ensure_ascii=False, indent=1))
print(json.dumps({f: {k: v for k, v in x.items() if 'Gutachten' not in k} for f, x in k8.items()}, ensure_ascii=False))
print({f: (k8[f]['B_je_Gutachten'], k8[f]['D_je_Gutachten']) for f in ('F1', 'F6')})
# 7 Simulation wie in gutachten3.py (Seed 20261119, 200000 Sätze), A mit eigener Streuung
import random
random.seed(20261119); sim = {}
for d in (5, 7):
    t = 0
    for _ in range(200000):
        a = [random.gauss(0, sa) for _ in range(3)]; c = [random.gauss(d, sb) for _ in range(3)]; t += min(c) > max(a)
    sim[d] = round(100 * t / 200000, 1)
out['Trennschaerfe']['Simulation_A_eigene_Streuung'] = sim
json.dump(out, open('gruppe_b.json', 'w'), ensure_ascii=False, indent=1); print('Simulation', sim)
