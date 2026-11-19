"""Werte zum Gutachten DAT-103 (Fassung v9) aus Repositorium (main 48f8c99)."""
import json, re, glob, collections
exec(open('gruppe1_3.py').read().split('# 1 Treffer')[0])
out = {}
def rng(v): return [round(sum(v)/len(v), 4), round(min(v), 4), round(max(v), 4)]
# alle bestätigten Sollbefunde (inhaltlich und Kleinkorrektur), nur getroffen, gepoolt je Wiederholung
alle = {}; summen = {}
for b in 'ABCD':
    v = []; tot = 0
    for w in (1, 2, 3):
        H = N_ = 0
        for L in R:
            if R[L]['bed'] == b and R[L]['wdh'] == w:
                H += sum(x[4] == 'getroffen' for x in R[L]['mh']); N_ += len(R[L]['mh'])
        v.append(100*H/N_); tot += H
    alle[b] = rng(v); summen[b] = tot
out['K1_alle_198'] = alle; out['Treffer_summe_alle'] = summen
# egusphere-2025-4506 ohne RC3, inhaltlich, über drei Wiederholungen
e = {}
for b in 'ABCD':
    H = N_ = 0
    for L in R:
        if R[L]['bed'] == b and R[L]['M'] == '4506':
            u = [x for x in R[L]['mh'] if SOLL[x[0]]['art'] == 'inhaltlich' and not SOLL[x[0]]['g03']]
            H += sum(x[4] == 'getroffen' for x in u); N_ += len(u)
    e[b] = [H, N_, round(100*H/N_, 2)]
out['4506_ohne_RC3'] = e
# K8: Einträge je Fall, A F1 F2 je Weg, F1+F2 je 100 Einträge je Weg
K8 = json.load(open(f'{HS}/auswertung/k8/mehrheit.json'))
KG = json.load(open(f'{HS}/auswertung/kennzahlen_je_gutachten.json'))
ef = {}
for b in 'ABCD':
    c = collections.Counter(); ids = set()
    for L, v in K8.items():
        if v['bed'] != b: continue
        for f, ks in v['faelle']:
            if f.startswith('F'): c[len(ks)] += 1; ids |= {(L, k) for k in ks}
    ef[b] = {'Fälle nach Zahl der Einträge': dict(sorted(c.items())), 'Einträge': len(ids)}
out['Eintraege_je_Fall'] = ef
weg = {}
for b in 'ABCD':
    for pfad, Ms in (('Seitenbilder', ('4506', '5046')), ('Skript', ('4733', '4695'))):
        f12 = sum(v['F1'] + v['F2'] for v in K8.values() if v['bed'] == b and v['M'] in Ms)
        n = sum(KG[L]['n_eintraege'] for L in KG if KG[L]['bed'] == b and KG[L]['M'] in Ms)
        weg[f'{b} {pfad}'] = {'F1': sum(v['F1'] for v in K8.values() if v['bed'] == b and v['M'] in Ms), 'F2': sum(v['F2'] for v in K8.values() if v['bed'] == b and v['M'] in Ms), 'Einträge': n, 'F1+F2 je 100': round(100*f12/n, 2)}
for pfad, Ms in (('Seitenbilder', ('4506', '5046')), ('Skript', ('4733', '4695'))):
    f12 = sum(v['F1'] + v['F2'] for v in K8.values() if v['M'] in Ms); n = sum(KG[L]['n_eintraege'] for L in KG if KG[L]['M'] in Ms)
    weg[f'alle {pfad}'] = {'F1+F2': f12, 'Einträge': n, 'je 100': round(100*f12/n, 2)}
out['K8_Weg'] = weg
json.dump(out, open('gutachten2.json', 'w'), ensure_ascii=False, indent=1)
print(json.dumps(out, ensure_ascii=False, indent=1))
