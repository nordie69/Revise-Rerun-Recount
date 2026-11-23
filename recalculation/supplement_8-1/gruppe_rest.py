"""Rest der Gruppen (C-310): Zusammensetzung der drei vom Autor ersetzten Gruppenurteile (G4-GB-26)."""
import json, collections
HS = '/home/claude/revise-rerun-recount/study/delivery_main_study/hauptstudie'
E = json.load(open(f'{HS}/einstufung/endgueltig_einzelbefunde.json')); M = json.load(open(f'{HS}/einstufung/mehrheit.json'))
plan = {r['code']: r for r in json.load(open(f'{HS}/laeufe/laufplan.json'))}
mg = {f'{man}/{g}': v['mehrheit'] for man, gs in M.items() for g, v in gs.items()}
ers = collections.defaultdict(list)
for e in E:
    if e.get('gruppe') in mg and mg[e['gruppe']] is not None and e['urteil'] != mg[e['gruppe']]:
        ers[e['gruppe']].append(e)
out = {'ersetzte_Gruppen': {g: {'Mehrheit': mg[g], 'Autor': es[0]['urteil'], 'Eintraege': len(es),
        'je_Bedingung': dict(sorted(collections.Counter(plan[x['code']]['bedingung'] for x in es).items()))} for g, es in ers.items()}}
out['Eintraege_zusammen'] = sum(len(es) for es in ers.values())
json.dump(out, open('gruppe_rest.json', 'w'), ensure_ascii=False, indent=1); print(json.dumps(out, ensure_ascii=False, indent=1))
# ER1-07: Weglassen je Instanz auch in C; ER1-10: F1 und F2 nach Leseweg für alle Bedingungen
src = open('gruppe1_3.py').read()
exec(src.split('# 2 B minus C')[0])
exec('INST' + src.split('INST', 1)[1].split('\n')[0]) if 'INST =' in src.split('# 7 B ohne')[0] else None
import re
INST = re.compile(r'\b(S1|S2|S3|S4|AB|SD)\b') if 'INST' not in dir() else INST
loioC = {}
for weg in ('S1', 'S2', 'S3', 'S4', 'AB', 'SD'):
    vals = []
    for w in (1, 2, 3):
        H = N_ = 0
        for L in R:
            if R[L]['bed'] != 'C' or R[L]['wdh'] != w: continue
            for x in R[L]['mh']:
                if SOLL[x[0]]['art'] != 'inhaltlich': continue
                N_ += 1
                if x[4] != 'getroffen': continue
                ids = re.findall(r'\b(?:GB|KK)-\d+\b', x[5] if len(x) > 5 else '')
                bleibt = any(set(INST.findall(R[L]['quelle'].get(i, ''))) - {weg} or not INST.findall(R[L]['quelle'].get(i, '')) for i in ids)
                H += bleibt
        vals.append(100 * H / N_)
    loioC[f'C ohne {weg}'] = rng(vals)
out['C_ohne_je_eine_Instanz'] = loioC
K8 = json.load(open(f'{HS}/auswertung/k8/mehrheit.json'))
weg = {}
for b in 'ABCD':
    for pfad, Ms in (('Seitenbilder', ('4506', '5046')), ('Skript', ('4733', '4695'))):
        for f in ('F1', 'F2'):
            weg[f'{b} {f} {pfad}'] = sum(v[f] for v in K8.values() if v['bed'] == b and v['M'] in Ms)
out['F1_F2_Leseweg'] = weg
json.dump(out, open('gruppe_rest.json', 'w'), ensure_ascii=False, indent=1)
print(json.dumps({k: out[k] for k in ('C_ohne_je_eine_Instanz', 'F1_F2_Leseweg')}, ensure_ascii=False))
# G4-GB-25: Modellurteile der 60 gezogenen Befunde; G4-GB-30: einstimmige Gruppen; G4-GB-29: Treffer nur einer Instanz; G3-GB-08: Läufe mit markierten Zugriffen
G60 = set(json.load(open(f'{HS}/einstufung/auftraggeber/Einstufung_Auftraggeber_v1_20261022_gezogen.json')))
Eall = json.load(open(f'{HS}/einstufung/endgueltig_einzelbefunde.json')); Mh = json.load(open(f'{HS}/einstufung/mehrheit.json'))
mg = {f'{m}/{g}': v for m, gs in Mh.items() for g, v in gs.items()}
modell = collections.Counter(mg[e['gruppe']]['mehrheit'] for e in Eall if e.get('zufallskennung') in G60)
out['Stichprobe_Modellurteil'] = dict(modell)
nc = modell.get('zutreffend', 0)
out['Stichprobe_einseitige_Grenze_Modell_zutreffend_Autor_nicht'] = round(100 * (1 - 0.05 ** (1 / (nc))), 1) if nc else None
out['Gruppen_einstimmig'] = [sum(1 for v in mg.values() if v.get('einstimmig')), len(mg)]
ex = {}
for b in ('B', 'D'):
    for weg in ('S1', 'S2', 'S3', 'S4', 'AB', 'SD'):
        verlust = 0
        for L in R:
            if R[L]['bed'] != b: continue
            for x in R[L]['mh']:
                if SOLL[x[0]]['art'] != 'inhaltlich' or x[4] != 'getroffen': continue
                ids = re.findall(r'\b(?:GB|KK)-\d+\b', x[5] if len(x) > 5 else '')
                bleibt = any(set(INST.findall(R[L]['quelle'].get(i, ''))) - {weg} or not INST.findall(R[L]['quelle'].get(i, '')) for i in ids)
                verlust += not bleibt
        ex[f'{b} {weg}'] = verlust
    ex[f'{b} Treffer'] = sum(1 for L in R if R[L]['bed'] == b for x in R[L]['mh'] if SOLL[x[0]]['art'] == 'inhaltlich' and x[4] == 'getroffen')
out['Treffer_nur_eine_Instanz'] = ex
st = json.load(open(f'{HS}/laeufe/status.json'))
mark = collections.Counter(plan_[c]['bedingung'] for c, v in st.items() if 'markiert' in v.get('gueltig', '')) if False else None
P_ = {r['code']: r for r in json.load(open(f'{HS}/laeufe/laufplan.json'))}
out['Laeufe_mit_markierten_Zugriffen'] = dict(sorted(collections.Counter(P_[c]['bedingung'] for c, v in st.items() if 'markiert' in v.get('gueltig', '')).items()))
out['Laeufe_mit_Verbrauch'] = sorted(c for c, v in st.items() if 'verbrauch' in v)
json.dump(out, open('gruppe_rest.json', 'w'), ensure_ascii=False, indent=1)
print(json.dumps({k: out[k] for k in ('Stichprobe_Modellurteil', 'Stichprobe_einseitige_Grenze_Modell_zutreffend_Autor_nicht', 'Gruppen_einstimmig', 'Treffer_nur_eine_Instanz', 'Laeufe_mit_markierten_Zugriffen', 'Laeufe_mit_Verbrauch')}, ensure_ascii=False))
