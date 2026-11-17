#!/usr/bin/env python3
"""Schritt 3: Vergleich der nachgerechneten Werte (ergebnis.json) mit den gelieferten
(Trefferbilanz_Hauptstudie_v1_20261115.md, kennzahlen_teil1.md, kennzahlen_k4_k8.md,
kennzahlen_je_gutachten.json). Schreibt vergleich.json."""
import json, re, os, collections

OUT = os.path.dirname(os.path.abspath(__file__))
AUS = '/home/claude/Paper3/quellen/lieferung_hauptstudie_20261115/hauptstudie/auswertung'
E = json.load(open(os.path.join(OUT, 'ergebnis.json')))
K, JG = E['kennzahlen'], E['je_gutachten']
BED = 'ABCD'
TOL = 0.05 + 1e-9


def tabellen(path):
    """liefert {(abschnitt, zeile, spalte): text}"""
    out = collections.OrderedDict(); sek = []; head = None
    for l in open(path, encoding='utf-8'):
        l = l.rstrip('\n')
        m = re.match(r'^(#+) (.*)', l)
        if m:
            lvl = len(m.group(1)); sek = sek[:lvl - 1] + [m.group(2)]; head = None; continue
        if l.startswith('|'):
            c = [x.strip() for x in l.strip().strip('|').split('|')]
            if set(l) <= set('|-: '):
                continue
            if head is None:
                head = c; continue
            for h, v in zip(head[1:], c[1:]):
                out[(' / '.join(sek), c[0], h)] = v
        else:
            head = None if l.strip() == '' else head
    return out


def zahl(s):
    return float(s.replace(',', '.'))


def drei(s):
    m = re.match(r'^\s*(-?[\d,]+) \((-?[\d,]+) bis (-?[\d,]+)\)', s)
    return tuple(zahl(x) for x in m.groups()) if m else None


V = []   # Vergleichszeilen


def cmp(name, eigen, geliefert, einheit, quelle, variante=False):
    d = abs(eigen - geliefert) if eigen is not None and geliefert is not None else None
    V.append({'kennzahl': name, 'eigen': eigen, 'geliefert': geliefert, 'einheit': einheit,
              'differenz': d, 'gleich': d is not None and d <= TOL, 'quelle': quelle, 'variante': variante})


def cmp3(name, erg, cell, faktor, einheit, quelle):
    t = drei(cell)
    for i, part in enumerate(('Mittel', 'min', 'max')):
        e = [erg['mittel'], erg['min'], erg['max']][i]
        cmp(f'{name}, {part}', None if e is None else e * faktor, t[i] if t else None, einheit, quelle)


TB = tabellen(os.path.join(AUS, 'Trefferbilanz_Hauptstudie_v1_20261115.md'))
S1 = 'Trefferbilanz der Hauptstudie / Kennzahlen K1, K2, K3, K5, K6, K7'
zeilen = [('K1 inhaltlich, getroffen (Hauptmaß)', 'K1 inhaltlich getroffen ({v} G03)', 100, 'pp'),
          ('K1 inhaltlich, teilweise', 'K1 inhaltlich teilweise ({v} G03)', 100, 'pp'),
          ('K1 Kleinkorrekturen, getroffen', 'K1 Kleinkorrekturen getroffen ({v} G03)', 100, 'pp'),
          ('K1 Kleinkorrekturen, teilweise', 'K1 Kleinkorrekturen teilweise ({v} G03)', 100, 'pp'),
          ('K2 nicht zutreffend, Anteil an allen Einträgen', 'K2 nicht zutreffend', 100, 'pp'),
          ('K2 ergänzend: Ansichtssache, Anteil', 'K2 Nebenwert Ansichtssache', 100, 'pp'),
          ('K3 Zusatzbefunde je Gutachten (Anzahl)', 'K3 Zusatzbefunde je Gutachten, Variante b ({v} G03)', 1, 'Fälle'),
          ('K7 Zuordnung, drei Läufe gleich', 'K7 Zuordnung drei Laeufe gleich ({v} G03)', 100, 'pp')]
for v, sek in (('mit', 'Mit den Sollbefunden aus G03'), ('ohne', 'Ohne die Sollbefunde aus G03')):
    for row, key, f, ein in zeilen:
        for b in BED:
            cmp3(f'{row} ({v} G03), {b}', K[key.format(v=v)][b], TB[(S1 + ' / ' + sek, row, b)], f, ein, 'Trefferbilanz')
    for m in ('4506', '4695', '4733', '5046'):
        for b in BED:
            cmp3(f'K1 inhaltlich getroffen {m} ({v} G03), {b}', K[f'K1 inhaltlich getroffen je Manuskript ({v} G03)'][f'{m}-{b}'],
                 TB[(S1 + ' / ' + sek, m, b)], 100, 'pp', 'Trefferbilanz')
um = S1 + ' / Umfang und Herkunft'
for row, key, f, ein in (('Einträge je Gutachten', 'Eintraege je Gutachten', 1, 'Fälle'),
                         ('davon inhaltliche Befunde', 'davon inhaltliche Befunde je Gutachten', 1, 'Fälle'),
                         ('davon Kleinkorrekturen', 'davon Kleinkorrekturen je Gutachten', 1, 'Fälle'),
                         ('K6 zutreffende Einträge aus nur einer Prüfinstanz', 'K6 Anteil aus nur einer Instanz', 100, 'pp')):
    for b in BED:
        cmp3(f'{row}, {b}', K[key][b], TB[(um, row, b)], f, ein, 'Trefferbilanz')
k5 = S1 + ' / K5 Streuung'
for m in ('4506', '4695', '4733', '5046'):
    for b in BED:
        cmp(f'K5 Spannweite K1 {m}, {b}', 100 * K['K1 inhaltlich getroffen je Manuskript (mit G03)'][f'{m}-{b}']['spannweite'],
            zahl(TB[(k5, m, b)]), 'pp', 'Trefferbilanz')
for b in BED:
    cell = TB[(k5, 'gleiche Schweregrade', b)]
    mm = re.match(r'([\d,]+) \((\d+) von (\d+) Paaren\)', cell)
    x = K['K5 Anteil gleicher Schweregrade'][b]
    cmp(f'K5 gleiche Schweregrade, {b} (eigene Hauptdefinition: nur getroffen)', 100 * x['getroffen']['anteil'], zahl(mm.group(1)), 'pp', 'Trefferbilanz')
    cmp(f'K5 gleiche Schweregrade, Paare, {b} (eigene Hauptdefinition: nur getroffen)', x['getroffen']['paare'], int(mm.group(3)), 'Fälle', 'Trefferbilanz')
    cmp(f'K5 gleiche Schweregrade, {b} (Variante getroffen oder teilweise)', 100 * x['getroffen_oder_teilweise']['anteil'], zahl(mm.group(1)), 'pp', 'Trefferbilanz', True)
    cmp(f'K5 gleiche Schweregrade, Paare, {b} (Variante getroffen oder teilweise)', x['getroffen_oder_teilweise']['paare'], int(mm.group(3)), 'Fälle', 'Trefferbilanz', True)
txt = open(os.path.join(AUS, 'Trefferbilanz_Hauptstudie_v1_20261115.md'), encoding='utf-8').read()
m = re.search(r'KI: (\d+) von (\d+) \(([\d,]+) %\)', txt)
cmp('K7 Einstufung, Anteil Gruppen mit KI-Mehrheit (Mehrheit "unklar" mitgezählt)', 100 * K['K7 Einstufung Gruppen mit KI-Mehrheit']['gesamt'], zahl(m.group(3)), 'pp', 'Trefferbilanz')
cmp('K7 Einstufung, Anteil Gruppen mit KI-Mehrheit (Variante: Mehrheit "unklar" nicht als Mehrheit)', 100 * K['K7 Einstufung Gruppen mit KI-Mehrheit ausser unklar'], zahl(m.group(3)), 'pp', 'Trefferbilanz', True)
m = re.search(r'Stichprobe Auftraggeber gegen Gruppe: (\d+) von (\d+) \(([\d,]+) %\); A (\d+) von 15, B (\d+) von 15, C (\d+) von 15, D (\d+) von 15', txt)
st = K['K7 Stichprobe Auftraggeber gegen Gruppe']
cmp('K7 Stichprobe gesamt', 100 * st['gesamt']['anteil'], zahl(m.group(3)), 'pp', 'Trefferbilanz')
for i, b in enumerate(BED):
    cmp(f'K7 Stichprobe {b}, gleiche Urteile', st[b]['gleich'], int(m.group(4 + i)), 'Fälle', 'Trefferbilanz')
# K4, K8
s8 = 'Trefferbilanz der Hauptstudie / Kennzahlen K4 und K8 / Fälle je Gutachten'
for row, key in [('K4', 'K4 Doppelungen je Gutachten (Mehrheit der Zaehler)')] + [(f'F{i}', f'K8 F{i} je Gutachten') for i in range(1, 8)] + \
        [('F1 bis F7 zusammen', 'K8 F1 bis F7 je Gutachten'), ('F1 bis F7 je 100 Einträge (ergänzend)', 'K8 F1 bis F7 je 100 Eintraege')]:
    for b in BED:
        cmp3(f'{row}, {b}', K[key][b], TB[(s8, row, b)], 1, 'Fälle', 'Trefferbilanz')
m = re.search(r'Übereinstimmung der Zähler: (\d+) von (\d+)', txt)
C = json.load(open(os.path.join(OUT, 'pruefungen.json')))
cmp('K8 Zähler, Fälle von allen drei genannt', C['k8_zaehler']['von_allen_drei'], int(m.group(1)), 'Fälle', 'Trefferbilanz')
cmp('K8 Zähler, genannte Fälle', C['k8_zaehler']['faelle_genannt'], int(m.group(2)), 'Fälle', 'Trefferbilanz')
# K9
k9 = K['K9']; s9 = 'Trefferbilanz der Hauptstudie / K9 Regelvorschläge'
cmp('K9 vorgeschlagene Regeln', k9['regeln_vorgeschlagen'], zahl(TB[(s9, 'vorgeschlagene Regeln', 'Wert')]), 'Fälle', 'Trefferbilanz')
cmp('K9 Anteil bestätigt', 100 * k9['anteil_bestaetigt'], zahl(re.search(r'\(([\d,]+) %\)', TB[(s9, 'vom Auftraggeber bestätigt', 'Wert')]).group(1)), 'pp', 'Trefferbilanz')
cmp('K9 Anteil der Fälle einer Klasse zugeordnet', 100 * k9['anteil_klassiert_R'], zahl(re.search(r'\(([\d,]+) %\)', TB[(s9, 'Fälle aus den Prüfberichten einer Klasse zugeordnet', 'Wert')]).group(1)), 'pp', 'Trefferbilanz')
cmp('K9 Fälle, die R und R2 beide sammeln', k9['gemeinsam'], zahl(TB[(s9, 'Fälle, die beide Vorschlagsläufe R und R2 sammeln', 'Wert')]), 'Fälle', 'Trefferbilanz')
cmp('K9 Anteil Fallpaare gleich gruppiert', 100 * k9['anteil_paare_gleich'], zahl(re.search(r'\(([\d,]+) %\)', TB[(s9, 'Fallpaare, die R und R2 gleich gruppieren', 'Wert')]).group(1)), 'pp', 'Trefferbilanz')
# Vorstudie
VO = K['Vorstudie']; sv = 'Trefferbilanz der Hauptstudie / Vorstudie (getrennt berichtet) / K1 je Gutachten'
for L, r in VO['gutachten'].items():
    n = r['n_inh'] + r['n_kk']; g = r['getr_inh'] + r['getr_kk']; t = r['teil_inh'] + r['teil_kk']
    cmp(f'Vorstudie {L} Sollbefunde', n, zahl(TB[(sv, L, 'Sollbefunde')]), 'Fälle', 'Trefferbilanz')
    cmp(f'Vorstudie {L} getroffen (alle Arten)', g, zahl(TB[(sv, L, 'getroffen')]), 'Fälle', 'Trefferbilanz')
    cmp(f'Vorstudie {L} teilweise (alle Arten)', t, zahl(TB[(sv, L, 'teilweise')]), 'Fälle', 'Trefferbilanz')
    cmp(f'Vorstudie {L} getroffen in % (alle Arten)', 100 * g / n, zahl(TB[(sv, L, 'getroffen in %')]), 'pp', 'Trefferbilanz')
    cmp(f'Vorstudie {L} getroffen oder teilweise in %', 100 * (g + t) / n, zahl(TB[(sv, L, 'getroffen oder teilweise in %')]), 'pp', 'Trefferbilanz')
    cmp(f'Vorstudie {L} drei Läufe gleich', r['k7_gleich'], zahl(TB[(sv, L, 'drei Läufe gleich')].split(' von ')[0]), 'Fälle', 'Trefferbilanz')
sd = 'Trefferbilanz der Hauptstudie / Vorstudie (getrennt berichtet) / K1 je Durchgang'
for D in ('V1', 'V2', 'V3', 'V4'):
    gs = [r for L, r in VO['gutachten'].items() if L.startswith(D + '-')]
    n = sum(r['n_inh'] + r['n_kk'] for r in gs); g = sum(r['getr_inh'] + r['getr_kk'] for r in gs); t = sum(r['teil_inh'] + r['teil_kk'] for r in gs)
    cmp(f'Vorstudie {D} getroffen in % (alle Arten, gepoolt)', 100 * g / n, zahl(TB[(sd, D, 'getroffen in %')]), 'pp', 'Trefferbilanz')
    cmp(f'Vorstudie {D} getroffen oder teilweise in %', 100 * (g + t) / n, zahl(TB[(sd, D, 'getroffen oder teilweise in %')]), 'pp', 'Trefferbilanz')
m = re.search(r'\(K7\): (\d+) von (\d+) Sollbefunden mit drei gleichen Antworten \(([\d,]+) %\)', txt)
cmp('Vorstudie K7 gesamt', 100 * VO['k7_gesamt'], zahl(m.group(3)), 'pp', 'Trefferbilanz')

# Abgleich kennzahlen_teil1.md und kennzahlen_k4_k8.md gegen Trefferbilanz (gleiche Tabellen)
T1 = tabellen(os.path.join(AUS, 'kennzahlen_teil1.md'))
T2 = tabellen(os.path.join(AUS, 'kennzahlen_k4_k8.md'))
gleich_dateien = []
for T, praefix_alt, praefix_tb in ((T1, 'Kennzahlen der Hauptstudie, Teil 1 (K1, K2, K3, K5, K6, K7)', S1),
                                   (T2, 'Kennzahlen der Hauptstudie, Teil 2 (K4, K8)', 'Trefferbilanz der Hauptstudie / Kennzahlen K4 und K8')):
    for (s, r, c), v in T.items():
        s2 = s.replace(praefix_alt, praefix_tb)
        gleich_dateien.append(((s, r, c), TB.get((s2, r, c)) == v))
# je Gutachten
JD = json.load(open(os.path.join(AUS, 'kennzahlen_je_gutachten.json')))
jg_abw = []
n_jg = 0
for c, d in JD.items():
    e = JG[c]
    paare = [('K1_inh_getroffen', e['getr_inh_mit'] / e['n_inh_mit']), ('K1_inh_teilweise', e['teil_inh_mit'] / e['n_inh_mit']),
             ('K1_kk_getroffen', e['getr_kk_mit'] / e['n_kk_mit']), ('K1_kk_teilweise', e['teil_kk_mit'] / e['n_kk_mit']),
             ('K1_inh_getroffen_ohneG03', e['getr_inh_ohne'] / e['n_inh_ohne']), ('K1_inh_teilweise_ohneG03', e['teil_inh_ohne'] / e['n_inh_ohne']),
             ('K1_kk_getroffen_ohneG03', e['getr_kk_ohne'] / e['n_kk_ohne']), ('K1_kk_teilweise_ohneG03', e['teil_kk_ohne'] / e['n_kk_ohne']),
             ('K7_zuordnung_gleich', e['k7z_gleich_mit'] / e['k7z_n_mit']), ('K7_zuordnung_gleich_ohneG03', e['k7z_gleich_ohne'] / e['k7z_n_ohne']),
             ('n_eintraege', e['n_bef']), ('n_gb', e['n_gb']), ('n_kk', e['n_kk']),
             ('K2', e['n_nz'] / e['n_bef']), ('K2_ansichtssache', e['n_ans'] / e['n_bef']),
             ('K3', e['k3b_mit']), ('K3_ohneG03', e['k3b_ohne']), ('K6', e['k6_eine'] / e['k6_n']), ('K6_zutreffend', e['k6_n'])]
    for k, ev in paare:
        n_jg += 1
        if abs(ev - d[k]) > 1e-9:
            jg_abw.append((c, k, ev, d[k]))

# K8 und K4 je Gutachten gegen k8/mehrheit.json
K8M = json.load(open(os.path.join(AUS, 'k8', 'mehrheit.json')))
k8_abw = [(c, k, JG[c][k], K8M[c][k]) for c in K8M for k in ['K4'] + ['F%d' % i for i in range(1, 8)] if JG[c][k] != K8M[c][k]]
# Urteile der Effektregel
RQV = []
for (s, r, c), val in TB.items():
    if s.endswith('Forschungsfragen') and c == 'Erwartung':
        RQV.append((r, val))
EF = K['Effektregel']
eig = {'RQ1 (mit G03)': EF['RQ1'][0]['effekt'], 'RQ1 (ohne G03)': EF['RQ1'][1]['effekt'],
       'RQ2 (mit G03)': EF['RQ2'][0]['effekt'] and EF['RQ2'][2]['mindestens_ein_fuenftel_mittel'],
       'RQ2 (ohne G03)': EF['RQ2'][1]['effekt'] and EF['RQ2'][2]['mindestens_ein_fuenftel_mittel'],
       'RQ3 (mit G03)': EF['RQ3'][0]['effekt'] and EF['RQ3'][-1]['K1_D_nicht_weniger_mit'],
       'RQ3 (ohne G03)': EF['RQ3'][0]['effekt'] and EF['RQ3'][-1]['K1_D_nicht_weniger_ohne']}
rq_vgl = [{'rq': r, 'geliefert': val, 'eigen': 'erfüllt' if eig[r] else 'nicht erfüllt', 'gleich': (val == ('erfüllt' if eig[r] else 'nicht erfüllt'))} for r, val in RQV]
HV = [x for x in V if not x['variante']]
res = {'vergleiche': V, 'zahl': len(HV), 'gleich': sum(x['gleich'] for x in HV),
       'abweichungen': [x for x in HV if not x['gleich']],
       'varianten': [x for x in V if x['variante']],
       'k8_mehrheit_je_gutachten': {'werte': len(K8M) * 8, 'abweichend': len(k8_abw), 'beispiele': k8_abw[:10]},
       'effektregel_urteile': rq_vgl,
       'kennzahlen_dateien_gleich_trefferbilanz': {'zellen': len(gleich_dateien), 'gleich': sum(g for _, g in gleich_dateien),
                                                    'ungleich': [k for k, g in gleich_dateien if not g]},
       'je_gutachten': {'werte': n_jg, 'abweichend': len(jg_abw), 'beispiele': jg_abw[:20]}}
json.dump(res, open(os.path.join(OUT, 'vergleich.json'), 'w'), ensure_ascii=False, indent=1)
print(res['zahl'], res['gleich'], len(res['abweichungen']))
for x in res['abweichungen']:
    print(x['kennzahl'], round(x['eigen'], 3) if x['eigen'] is not None else None, x['geliefert'], x['einheit'])
print(res['kennzahlen_dateien_gleich_trefferbilanz']['zellen'], res['kennzahlen_dateien_gleich_trefferbilanz']['gleich'], res['kennzahlen_dateien_gleich_trefferbilanz']['ungleich'][:10])
print(res['je_gutachten']); print(res['k8_mehrheit_je_gutachten']); print(rq_vgl)
print('Varianten', [(x['kennzahl'], round(x['eigen'], 2), x['geliefert'], x['gleich']) for x in res['varianten']])
