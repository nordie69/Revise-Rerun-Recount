#!/usr/bin/env python3
"""Unabhaengige Nachrechnung der Kennzahlen der Hauptstudie (Schritt 6-1).

Liest nur die Rohdaten der Lieferung (keine Skripte unter hauptstudie/tools/),
rechnet die Kennzahlen direkt aus den Definitionen des Studienprotokolls und
schreibt ergebnis.json und pruefungen.json in den Ordner dieses Skripts.
"""
import json, re, os, glob, itertools, random, collections, statistics

ROOT = '/home/claude/Paper3/quellen/lieferung_hauptstudie_20261115/hauptstudie'
OUT = os.path.dirname(os.path.abspath(__file__))
P = lambda *a: os.path.join(ROOT, *a)
MS = ['4506', '4695', '4733', '5046']
BED = ['A', 'B', 'C', 'D']
INSTANZEN = {'S1', 'S2', 'S3', 'S4', 'AB', 'SD'}
CHK = collections.OrderedDict()   # Pruefergebnisse


def zellen(l):
    return [x.strip() for x in l.strip().strip('|').split('|')]


def norm(u):
    u = u.strip().lower()
    return {'ansichtssache': 'ansichtssache', 'zutreffend': 'zutreffend',
            'nicht zutreffend': 'nicht zutreffend', 'unklar': 'unklar'}.get(u, u)


def mehrheit(vals):
    c = collections.Counter(vals)
    v, n = c.most_common(1)[0]
    return v if n >= 2 else None


# ---------------------------------------------------------------- Laufplan
plan = json.load(open(P('laeufe', 'laufplan.json')))
l2n = json.load(open(P('laeufe', 'nachverarbeitung.json')))
lauf = {x['code']: x for x in plan}
for c, x in lauf.items():
    x['N'] = l2n[c]
CHK['laufplan'] = {
    'zahl': len(plan),
    'je_bed_ms': {f'{b}-{m}': sorted(x['wdh'] for x in plan if x['bedingung'] == b and x['manuskript'] == m)
                  for b in BED for m in MS},
    'kennungen_doppelt': [k for k, n in collections.Counter(x['kennung'] for x in plan).items() if n > 1],
    'N_doppelt': [k for k, n in collections.Counter(l2n.values()).items() if n > 1],
    'fassung_je_bed': {b: sorted({(x['fassung'], tuple(x['pakete']), x['aufbau']) for x in plan if x['bedingung'] == b}) for b in BED},
}

# ---------------------------------------------------------------- Sollbefunde
soll = {}   # kennung -> dict(art, ergebnis, ms)
for m in MS:
    for l in open(P('soll', m, 'sollbefunde.md')):
        if re.match(r'^\| \d{4}-RC', l):
            c = zellen(l)
            soll[c[0]] = {'ms': m, 'art': c[2], 'ergebnis': c[4], 'durch': c[5]}
best = {k: v for k, v in soll.items() if v['ergebnis'] == 'bestätigt'}
G03 = {k for k in best if k.startswith('4506-RC3-')}
CHK['soll'] = {
    'einwaende': len(soll), 'bestaetigt': len(best),
    'inhaltlich': sum(v['art'] == 'inhaltlich' for v in best.values()),
    'kleinkorrektur': sum(v['art'] == 'Kleinkorrektur' for v in best.values()),
    'nicht_bestaetigt': len(soll) - len(best), 'auftraggeber': sum(v['durch'] == 'Auftraggeber' for v in soll.values()),
    'G03_bestaetigt': len(G03),
    'je_ms': {m: [sum(1 for v in best.values() if v['ms'] == m and v['art'] == a) for a in ('inhaltlich', 'Kleinkorrektur')] for m in MS},
}
# Mehrheit der Bestaetigung aus den drei Pruefern (Stichprobe: alle)
abw = []
for m in MS:
    for l in open(P('soll', m, 'mehrheit.md')):
        if re.match(r'^\| \d{4}-RC', l):
            c = zellen(l)
            mh = mehrheit(c[2:5])
            erw = c[5]
            if (mh or 'ohne') != erw and not (mh is None or mh == 'unklar'):
                abw.append(c)
            if mh in (None, 'unklar') and soll[c[0]]['durch'] != 'Auftraggeber':
                abw.append(['ohne Mehrheit, nicht beim Auftraggeber'] + c)
CHK['soll_mehrheit_abweichungen'] = abw

# ---------------------------------------------------------------- Einzelbefunde
eb = json.load(open(P('einstufung', 'einzelbefunde.json')))
befunde = {}   # (code, kennung) -> dict
for x in eb:
    befunde[(x['code'], x['kennung'])] = x


def source(text, kennung):
    if kennung.startswith('GB'):
        m = re.search(r'^\| Source \| (.*?) \|\s*$', text, re.M)
        return m.group(1) if m else None
    for l in text.split('\n'):
        if l.startswith('| ' + kennung + ' '):
            c = zellen(l)
            return c[-1]
    return None


def severity(text):
    m = re.search(r'^\| Severity \| (.*?) \|\s*$', text, re.M)
    return m.group(1).strip().lower() if m else None


for k, x in befunde.items():
    x['source'] = source(x['text'], k[1])
    x['inst'] = sorted(set(re.findall(r'\b(S[1-4]|AB|SD)\b', x['source'] or '')))
    x['sev'] = severity(x['text']) if k[1].startswith('GB') else None

# Abgleich mit den Gutachtendateien: Zahl der GB und KK je Lauf
gz = {}
for c in lauf:
    g = open(glob.glob(P('laeufe', 'ergebnis', c, '*_Gutachten.md'))[0]).read()
    gb = set(re.findall(r'^\*\*(GB-\d+)\b', g, re.M))
    kk = set(re.findall(r'^\| (KK-\d+) \|', g, re.M))
    e_gb = {k for (cc, k) in befunde if cc == c and k.startswith('GB')}
    e_kk = {k for (cc, k) in befunde if cc == c and k.startswith('KK')}
    gz[c] = {'gb': len(gb), 'kk': len(kk), 'gleich': gb == e_gb and kk == e_kk}
CHK['einzelbefunde_gegen_gutachten'] = {'zahl': len(befunde), 'ungleich': [c for c, v in gz.items() if not v['gleich']]}
CHK['source_nicht_erkannt'] = sum(1 for x in befunde.values() if not x['source'])
CHK['source_ohne_instanz'] = collections.Counter(x['source'] for x in befunde.values() if not x['inst']).most_common(10)

# ---------------------------------------------------------------- Zuordnung
zu = {}   # code -> soll -> dict
zu_abw = []
for c, x in lauf.items():
    N = x['N']; m = x['manuskript']
    runs = []
    for i in (1, 2, 3):
        d = {}
        for l in open(P('laeufe', 'zuordnung', N, f'zuordnung{i}.md')):
            if re.match(r'^\| \d{4}-RC', l):
                cc = zellen(l)
                d[cc[0]] = (cc[1], [t for t in re.split(r'[,;]\s*', cc[2]) if t])
        runs.append(d)
    zu[c] = {}
    for s in best:
        if best[s]['ms'] != m:
            continue
        a = [r[s][0] for r in runs]
        mh = mehrheit(a)
        # Befund zutreffend: von >= 2 Laeufen fuer denselben Sollbefund als getroffen genannt
        cnt = collections.Counter(e for r in runs if r[s][0] == 'getroffen' for e in set(r[s][1]))
        tr = sorted(e for e, n in cnt.items() if n >= 2)
        cnt2 = collections.Counter(e for r in runs if r[s][0] in ('getroffen', 'teilweise') for e in set(r[s][1]))
        tr2 = sorted(e for e, n in cnt2.items() if n >= 2)
        zu[c][s] = {'a': a, 'mh': mh, 'gleich': len(set(a)) == 1, 'treffer': tr, 'genannt2': tr2}
    # Gegenprobe mit mehrheit.md
    for l in open(P('laeufe', 'zuordnung', N, 'mehrheit.md')):
        if re.match(r'^\| \d{4}-RC', l):
            cc = zellen(l)
            z = zu[c][cc[0]]
            if (z['mh'] or '') != cc[4]:
                zu_abw.append((c, cc[0], 'Mehrheit', z['mh'], cc[4]))
            liste = sorted(t for t in re.split(r'[,;]\s*', cc[5]) if t)
            if cc[4] == 'getroffen' and liste != z['treffer']:
                zu_abw.append((c, cc[0], 'Eintraege', z['treffer'], liste))
    # fehlende Sollbefunde in Laeufen
    for i, r in enumerate(runs):
        fehl = [s for s in best if best[s]['ms'] == m and s not in r]
        if fehl:
            zu_abw.append((c, 'Lauf %d' % (i + 1), 'fehlt', fehl, ''))
CHK['zuordnung_mehrheit_gegen_mehrheit_md'] = {'abweichungen': zu_abw[:20], 'zahl': len(zu_abw),
                                               'ohne_mehrheit': sum(1 for c in zu for s in zu[c] if zu[c][s]['mh'] is None)}

# zutreffend nach Zuordnung
zutr_zu = set()
zutr_zu_ohneG03 = set()
mit_soll = set()       # genannt von >= 2 Laeufen fuer einen Sollbefund (getroffen oder teilweise)
mit_soll_ohneG03 = set()
for c in zu:
    for s, z in zu[c].items():
        for e in z['treffer']:
            zutr_zu.add((c, e))
            if s not in G03:
                zutr_zu_ohneG03.add((c, e))
        for e in z['genannt2']:
            mit_soll.add((c, e))
            if s not in G03:
                mit_soll_ohneG03.add((c, e))
unbekannt = sorted(k for k in zutr_zu if k not in befunde)
strittig_eigen = {k for k in befunde if k not in zutr_zu}
strittig_geliefert = {k for k, x in befunde.items() if x['strittig']}
CHK['zutreffend_nach_zuordnung'] = {'zahl': len(zutr_zu), 'nicht_im_gutachten': unbekannt[:10],
                                    'strittig_eigen': len(strittig_eigen), 'strittig_geliefert': len(strittig_geliefert),
                                    'differenz': sorted(strittig_eigen ^ strittig_geliefert)[:20]}

# ---------------------------------------------------------------- Einstufung
kenn = json.load(open(P('einstufung', 'kennungen.json')))          # zufallskennung -> code, kennung
gcode = json.load(open(P('einstufung', 'gruppen_codes.json')))     # ms -> G
ms_g = {v: k for k, v in gcode.items()}
gruppe_von = {}
gruppen = collections.defaultdict(list)
for G in gcode.values():
    for l in open(P('einstufung', 'gruppen', G, 'gruppen.md')):
        if l.startswith('| BG-'):
            c = zellen(l)
            for z in [t for t in re.split(r'[,;]\s*', c[1]) if t]:
                if z in gruppe_von:
                    CHK.setdefault('zufallskennung_doppelt', []).append(z)
                gruppe_von[z] = (G, c[0])
                gruppen[(G, c[0])].append(z)
CHK['gruppen'] = {'zahl': len(gruppen), 'einzelbefunde_in_gruppen': len(gruppe_von),
                  'kennungen_json': len(kenn), 'ohne_gruppe': sorted(set(kenn) - set(gruppe_von))[:10],
                  'gruppe_ohne_kennung': sorted(set(gruppe_von) - set(kenn))[:10]}
# Zufallskennung muss auf einen strittigen Befund zeigen
zk_von = {}
falsch_ms = 0
for z, v in kenn.items():
    k = (v['code'], v['kennung'])
    zk_von[k] = z
    if z in gruppe_von and ms_g[gruppe_von[z][0]] != lauf[v['code']]['manuskript']:
        falsch_ms += 1
CHK['gruppen']['falsches_manuskript'] = falsch_ms
CHK['gruppen']['strittig_ohne_zufallskennung'] = len([k for k in strittig_eigen if k not in zk_von])
CHK['gruppen']['zufallskennung_nicht_strittig'] = len([k for k in zk_von if k not in strittig_eigen])

# KI-Laeufe
ek = collections.defaultdict(lambda: [None, None, None])
ek_dup = []
for f in glob.glob(P('einstufung', 'ek', '*', 'e*_t*', 'einstufung.md')):
    G = f.split('/')[-3]; e = int(f.split('/')[-2][1]) - 1
    for l in open(f):
        if l.startswith('| BG-'):
            c = zellen(l)
            if ek[(G, c[0])][e] is not None:
                ek_dup.append((G, c[0], e))
            ek[(G, c[0])][e] = norm(c[1])
mh_ki = {}
for g in gruppen:
    u = ek[g]
    mh_ki[g] = mehrheit(u) if None not in u else 'fehlt'
mj = json.load(open(P('einstufung', 'mehrheit.json')))
mh_abw = [(g, mh_ki[g], mj[g[0]][g[1]]) for g in gruppen
          if (mh_ki[g] if mh_ki[g] not in (None, 'unklar') else None) != mj[g[0]][g[1]]['mehrheit']
          or list(ek[g]) != [norm(x) for x in mj[g[0]][g[1]]['urteile']]]
CHK['ki_mehrheit'] = {'gruppen': len(mh_ki), 'mehrheit': sum(1 for v in mh_ki.values() if v not in (None, 'fehlt')),
                      'ohne_mehrheit': sum(1 for v in mh_ki.values() if v is None),
                      'mehrheit_unklar': sum(1 for v in mh_ki.values() if v == 'unklar'),
                      'fehlende_urteile': sum(1 for v in mh_ki.values() if v == 'fehlt'),
                      'abweichungen_gegen_mehrheit_json': mh_abw[:10], 'doppelte_zeilen': ek_dup[:5],
                      'verteilung': dict(collections.Counter(mh_ki.values()))}

# Auftraggeber
tsv = [l.rstrip('\n').split('\t') for l in open(P('einstufung', 'auftraggeber', 'Einstufung_Auftraggeber_v1_20261022_ausgefuellt_20261115.tsv'))][1:]
stich = {}
ag_gruppe = {}
for r in tsv:
    if r[3] == '1':
        stich[r[1]] = norm(r[4])
    else:
        m = r[2].split('-')[-1]
        ag_gruppe[(gcode[m], r[1])] = norm(r[4])
gezogen = json.load(open(P('einstufung', 'auftraggeber', 'Einstufung_Auftraggeber_v1_20261022_gezogen.json')))
# Ziehung nachvollziehen
pool = collections.defaultdict(list)
for z, v in kenn.items():
    g = gruppe_von.get(z)
    if g and mh_ki[g] in ('zutreffend', 'nicht zutreffend', 'ansichtssache'):
        pool[lauf[v['code']]['bedingung']].append(z)
ziehung = {}
rng = random.Random(202610221)
v1 = []
for b in BED:
    v1 += rng.sample(sorted(pool[b]), 15)
v2 = []
for b in BED:
    v2 += random.Random(202610221).sample(sorted(pool[b]), 15)
CHK['stichprobe_ziehung'] = {
    'gezogen_zahl': len(gezogen), 'tsv_teil1': len(stich), 'tsv_teil2': len(ag_gruppe),
    'gleich_gezogen_tsv': sorted(gezogen) == sorted(stich),
    'je_bedingung': dict(collections.Counter(lauf[kenn[z]['code']]['bedingung'] for z in stich)),
    'alle_aus_zulaessigen_gruppen': all(mh_ki[gruppe_von[z]] in ('zutreffend', 'nicht zutreffend', 'ansichtssache') for z in stich),
    'nachgezogen_ein_generator': sorted(v1) == sorted(gezogen),
    'nachgezogen_generator_je_bedingung': sorted(v2) == sorted(gezogen),
    'teil2_gleich_gruppen_ohne_mehrheit': sorted(ag_gruppe) == sorted(g for g, v in mh_ki.items() if v in (None, 'unklar')),
}
# K7 Stichprobe
k7s = {'gesamt': [0, 0]}
abw_st = []
for z, u in stich.items():
    b = lauf[kenn[z]['code']]['bedingung']
    g = gruppe_von[z]
    gl = u == mh_ki[g]
    k7s.setdefault(b, [0, 0])
    k7s[b][0] += gl; k7s[b][1] += 1
    k7s['gesamt'][0] += gl; k7s['gesamt'][1] += 1
    if not gl:
        abw_st.append({'zufallskennung': z, 'gruppe': '/'.join(g), 'ki': mh_ki[g], 'auftraggeber': u, 'groesse': len(gruppen[g])})
schwelle = k7s['gesamt'][0] / k7s['gesamt'][1]

# endgueltige Gruppenurteile
g_end = {}
for g in gruppen:
    v = mh_ki[g]
    g_end[g] = v if v not in (None, 'unklar', 'fehlt') else ag_gruppe.get(g, 'OFFEN')
for a in abw_st:
    G, bg = a['gruppe'].split('/')
    g_end[(G, bg)] = a['auftraggeber']
urteil = {}
for k in befunde:
    if k in zutr_zu:
        urteil[k] = 'zutreffend'
    else:
        urteil[k] = g_end[gruppe_von[zk_von[k]]]
# Gegenprobe endgueltig_einzelbefunde.json
ee = json.load(open(P('einstufung', 'endgueltig_einzelbefunde.json')))
ee_abw = [(x['code'], x['kennung'], x['urteil'], urteil.get((x['code'], x['kennung']))) for x in ee
          if urteil.get((x['code'], x['kennung'])) != x['urteil']]
eg = json.load(open(P('einstufung', 'endgueltig_gruppen.json')))
eg_abw = [(g, g_end[g], eg[g[0]][g[1]]['urteil']) for g in g_end if eg[g[0]][g[1]]['urteil'] != g_end[g]]
CHK['endgueltig_gegenprobe'] = {'einzelbefunde_abweichend': len(ee_abw), 'beispiele': ee_abw[:10],
                                'gruppen_abweichend': len(eg_abw), 'beispiele_gruppen': eg_abw[:10],
                                'verteilung_eigen': dict(collections.Counter(urteil.values())),
                                'offen': sum(1 for v in g_end.values() if v == 'OFFEN')}

# ---------------------------------------------------------------- K8, K4
K8 = {}
k8_bsp = {}
for c, x in lauf.items():
    N = x['N']
    zs = []
    for i in (1, 2, 3):
        fa = set()
        for l in open(P('auswertung', 'k8', N, f'zaehlung{i}.md')):
            if re.match(r'^\| (F[1-7]|K4) \|', l):
                cc = zellen(l)
                ks = tuple(sorted(t.strip() for t in re.split(r'[,/;]\s*', cc[1]) if t.strip()))
                fa.add((cc[0], ks))
        zs.append(fa)
    cnt = collections.Counter(f for z in zs for f in z)
    maj = {f for f, n in cnt.items() if n >= 2}
    r = {}
    for kl in ['K4'] + ['F%d' % i for i in range(1, 8)]:
        r[kl] = sum(1 for f in maj if f[0] == kl)
        r[kl + '_median'] = statistics.median([sum(1 for f in z if f[0] == kl) for z in zs])
        r[kl + '_z'] = [sum(1 for f in z if f[0] == kl) for z in zs]
    r['F'] = sum(r['F%d' % i] for i in range(1, 8))
    r['F_median'] = sum(r['F%d_median' % i] for i in range(1, 8))
    r['einstimmig'] = sum(1 for f, n in cnt.items() if n == 3)
    r['faelle_gesamt'] = len(cnt)
    K8[c] = r
# K4 aus dem Pruefbericht direkt (Schlusszeile "Doppelungen: n")
k4_vf = {}
for c, x in lauf.items():
    t = open(P('laeufe', 'verifikation', x['N'], 'verifikation.md')).read()
    m = re.findall(r'Doppelungen: (\d+)', t)
    if re.search(r'Doppelungen: (keine|0)\b', t) and not m:
        m = ['0']
    k4_vf[c] = int(m[-1]) if m else None

# ---------------------------------------------------------------- Kennzahlen je Gutachten
jg = {}
for c, x in lauf.items():
    m = x['manuskript']; b = x['bedingung']
    r = {'bed': b, 'ms': m, 'wdh': x['wdh']}
    for var, excl in (('mit', set()), ('ohne', G03)):
        for art, kz in (('inhaltlich', 'inh'), ('Kleinkorrektur', 'kk')):
            ss = [s for s in zu[c] if best[s]['art'] == art and s not in excl]
            r[f'n_{kz}_{var}'] = len(ss)
            r[f'getr_{kz}_{var}'] = sum(zu[c][s]['mh'] == 'getroffen' for s in ss)
            r[f'teil_{kz}_{var}'] = sum(zu[c][s]['mh'] == 'teilweise' for s in ss)
        ss = [s for s in zu[c] if s not in excl]
        r[f'k7z_gleich_{var}'] = sum(zu[c][s]['gleich'] for s in ss)
        r[f'k7z_n_{var}'] = len(ss)
        ztz = zutr_zu if var == 'mit' else zutr_zu_ohneG03
        ms_ = mit_soll if var == 'mit' else mit_soll_ohneG03
        bf = [k for k in befunde if k[0] == c]
        r['n_bef'] = len(bf)
        r['n_nz'] = sum(urteil[k] == 'nicht zutreffend' for k in bf)
        r['n_ans'] = sum(urteil[k] == 'ansichtssache' for k in bf)
        r['n_zutr'] = sum(urteil[k] == 'zutreffend' for k in bf)
        # K3 Variante a: Befund nicht zutreffend nach Zuordnung (kein Treffer) und Einstufung zutreffend
        r[f'k3a_{var}'] = sum(1 for k in bf if k not in ztz and urteil[k] == 'zutreffend')
        # K3 Variante b: von keiner Mehrheit fuer einen Sollbefund genannt (weder getroffen noch teilweise)
        r[f'k3b_{var}'] = sum(1 for k in bf if k not in ms_ and urteil[k] == 'zutreffend')
        zt = [k for k in bf if urteil[k] == 'zutreffend']
        r['k6_eine'] = sum(1 for k in zt if len(befunde[k]['inst']) == 1)
        r['k6_n'] = len(zt)
        r['k6_ohne_instanz'] = sum(1 for k in zt if len(befunde[k]['inst']) == 0)
    r.update({k: K8[c][k] for k in K8[c] if not k.endswith('_z')})
    r['K4_vf'] = k4_vf[c]
    r['n_gb'] = sum(1 for k in befunde if k[0] == c and k[1].startswith('GB'))
    r['n_kk'] = sum(1 for k in befunde if k[0] == c and k[1].startswith('KK'))
    jg[c] = r


def rate(c, num, den):
    return jg[c][num] / jg[c][den] if jg[c][den] else None


# K5 Teil 2: Schweregrade gemeinsamer Befunde
def k5_schwere(b):
    """Paare inhaltlicher Befunde (GB, nur sie haben Severity) aus zwei verschiedenen
    Wiederholungen derselben Bedingung und desselben Manuskripts, die gemeinsam sind:
    gleiche Befundgruppe der Einstufung oder gleicher Sollbefund nach Mehrheit.
    Variante 'getroffen': Sollbefund mit Mehrheit getroffen, Befund von >= 2 Laeufen als getroffen genannt.
    Variante 'getroffen_oder_teilweise': Mehrheit getroffen oder teilweise, Befund von >= 2 Laeufen genannt.
    Jedes Paar zaehlt einmal (dedupliziert)."""
    res = {}
    for var, key in (('getroffen', 'treffer'), ('getroffen_oder_teilweise', 'genannt2')):
        gl = n = 0
        for m in MS:
            cs = {lauf[c]['wdh']: c for c in lauf if lauf[c]['bedingung'] == b and lauf[c]['manuskript'] == m}
            items = collections.defaultdict(set)
            for k in befunde:
                if k[0] in cs.values() and k[1].startswith('GB') and k in zk_von:
                    items[('g', gruppe_von[zk_von[k]])].add(k)
            for w, c in cs.items():
                for s, z in zu[c].items():
                    if var == 'getroffen' and z['mh'] != 'getroffen':
                        continue
                    if var != 'getroffen' and z['mh'] not in ('getroffen', 'teilweise'):
                        continue
                    for e in z[key]:
                        if e.startswith('GB'):
                            items[('s', s)].add((c, e))
            seen = set()
            for v in items.values():
                for a, bb in itertools.combinations(sorted(v), 2):
                    if lauf[a[0]]['wdh'] == lauf[bb[0]]['wdh'] or (a, bb) in seen:
                        continue
                    seen.add((a, bb))
                    n += 1; gl += befunde[a]['sev'] == befunde[bb]['sev']
        res[var] = {'paare': n, 'gleich': gl, 'anteil': gl / n if n else None}
    return res


# ---------------------------------------------------------------- Aggregation je Bedingung
def je_lauf(b, fn):
    """fn(liste der 4 Codes einer Wiederholung) -> Wert; gibt Liste der drei Werte zurueck"""
    out = []
    for w in (1, 2, 3):
        cs = [c for c in lauf if lauf[c]['bedingung'] == b and lauf[c]['wdh'] == w]
        assert len(cs) == 4, (b, w, cs)
        out.append(fn(cs))
    return out


def gepoolt(num, den):
    return lambda cs: sum(jg[c][num] for c in cs) / sum(jg[c][den] for c in cs)


def je_gutachten(key):
    return lambda cs: sum(jg[c][key] for c in cs) / len(cs)


def summe(key):
    return lambda cs: sum(jg[c][key] for c in cs)


KENN = collections.OrderedDict()
for var in ('mit', 'ohne'):
    KENN[f'K1 inhaltlich getroffen ({var} G03)'] = ('quote', gepoolt(f'getr_inh_{var}', f'n_inh_{var}'))
    KENN[f'K1 inhaltlich teilweise ({var} G03)'] = ('quote', gepoolt(f'teil_inh_{var}', f'n_inh_{var}'))
    KENN[f'K1 Kleinkorrekturen getroffen ({var} G03)'] = ('quote', gepoolt(f'getr_kk_{var}', f'n_kk_{var}'))
    KENN[f'K1 Kleinkorrekturen teilweise ({var} G03)'] = ('quote', gepoolt(f'teil_kk_{var}', f'n_kk_{var}'))
KENN['K2 nicht zutreffend'] = ('quote', gepoolt('n_nz', 'n_bef'))
KENN['K2 Nebenwert Ansichtssache'] = ('quote', gepoolt('n_ans', 'n_bef'))
for var in ('mit', 'ohne'):
    KENN[f'K3 Zusatzbefunde je Gutachten, Variante a ({var} G03)'] = ('zahl', je_gutachten(f'k3a_{var}'))
    KENN[f'K3 Zusatzbefunde je Gutachten, Variante b ({var} G03)'] = ('zahl', je_gutachten(f'k3b_{var}'))
KENN['K4 Doppelungen je Gutachten (Mehrheit der Zaehler)'] = ('zahl', je_gutachten('K4'))
KENN['K6 Anteil aus nur einer Instanz'] = ('quote', gepoolt('k6_eine', 'k6_n'))
for var in ('mit', 'ohne'):
    KENN[f'K7 Zuordnung drei Laeufe gleich ({var} G03)'] = ('quote', gepoolt(f'k7z_gleich_{var}', f'k7z_n_{var}'))
for i in range(1, 8):
    KENN[f'K8 F{i} je Gutachten'] = ('zahl', je_gutachten(f'F{i}'))
KENN['K8 F1 bis F7 je Gutachten'] = ('zahl', je_gutachten('F'))
KENN['K8 F1 bis F7 je Gutachten (Median der Zaehler)'] = ('zahl', je_gutachten('F_median'))
KENN['K8 F1 bis F7 je 100 Eintraege'] = ('zahl', lambda cs: 100 * sum(jg[c]['F'] for c in cs) / sum(jg[c]['n_bef'] for c in cs))
KENN['Eintraege je Gutachten'] = ('zahl', je_gutachten('n_bef'))
KENN['davon inhaltliche Befunde je Gutachten'] = ('zahl', je_gutachten('n_gb'))
KENN['davon Kleinkorrekturen je Gutachten'] = ('zahl', je_gutachten('n_kk'))

ERG = collections.OrderedDict()
for name, (typ, fn) in KENN.items():
    ERG[name] = {}
    for b in BED:
        try:
            v = je_lauf(b, fn)
        except ZeroDivisionError:
            v = [None] * 3
        if None in v:
            ERG[name][b] = {'laeufe': v, 'mittel': None, 'min': None, 'max': None}
            continue
        ERG[name][b] = {'laeufe': v, 'mittel': sum(v) / 3, 'min': min(v), 'max': max(v), 'spannweite': max(v) - min(v), 'typ': typ}
# K5 Streuung: Spannweite von K1 Hauptmass
ERG['K5 Spannweite K1 inhaltlich getroffen (mit G03)'] = {b: {'wert': ERG['K1 inhaltlich getroffen (mit G03)'][b]['spannweite'], 'typ': 'quote'} for b in BED}
ERG['K5 Spannweite K1 inhaltlich getroffen (ohne G03)'] = {b: {'wert': ERG['K1 inhaltlich getroffen (ohne G03)'][b]['spannweite'], 'typ': 'quote'} for b in BED}
ERG['K5 Anteil gleicher Schweregrade'] = {b: dict(k5_schwere(b), typ='quote') for b in BED}
# K1 je Manuskript und K5 Spannweite je Manuskript
for var in ('mit', 'ohne'):
    t = {}
    for m in MS:
        for b in BED:
            v = [jg[c][f'getr_inh_{var}'] / jg[c][f'n_inh_{var}'] for c in sorted(lauf, key=lambda c: lauf[c]['wdh'])
                 if lauf[c]['bedingung'] == b and lauf[c]['manuskript'] == m]
            t[f'{m}-{b}'] = {'laeufe': v, 'mittel': sum(v) / 3, 'min': min(v), 'max': max(v), 'spannweite': max(v) - min(v)}
    ERG[f'K1 inhaltlich getroffen je Manuskript ({var} G03)'] = t
# K4 aus der Schlusszeile des Pruefberichts, nur zur Gegenprobe der Mehrheit der Zaehler
CHK['k4_schlusszeile'] = {'lesbar': sum(1 for c in lauf if k4_vf[c] is not None),
                          'gleich_mehrheit': sum(1 for c in lauf if k4_vf[c] is not None and k4_vf[c] == K8[c]['K4']),
                          'ungleich': [(c, k4_vf[c], K8[c]['K4']) for c in lauf if k4_vf[c] is not None and k4_vf[c] != K8[c]['K4']]}
CHK['k8_zaehler'] = {'faelle_genannt': sum(K8[c]['faelle_gesamt'] for c in lauf), 'von_allen_drei': sum(K8[c]['einstimmig'] for c in lauf)}

# K7 Einstufung KI-Mehrheit, gesamt und je Bedingung (Anteil der Gruppen mit Mehrheit; je Bedingung: Gruppen mit Befunden der Bedingung)
k7e = {'gesamt': sum(1 for v in mh_ki.values() if v is not None) / len(mh_ki)}
k7e_nicht_unklar = sum(1 for v in mh_ki.values() if v not in (None, 'unklar')) / len(mh_ki)
for b in BED:
    gs = {gruppe_von[zk_von[k]] for k in zk_von if lauf[k[0]]['bedingung'] == b}
    k7e[b] = sum(1 for g in gs if mh_ki[g] is not None) / len(gs)
    k7e[b + '_n'] = len(gs)
ERG['K7 Einstufung Gruppen mit KI-Mehrheit'] = k7e
ERG['K7 Einstufung Gruppen mit KI-Mehrheit ausser unklar'] = k7e_nicht_unklar
ERG['K7 Stichprobe Auftraggeber gegen Gruppe'] = {k: {'gleich': v[0], 'n': v[1], 'anteil': v[0] / v[1]} for k, v in k7s.items()}
ERG['K7 Stichprobe Abweichungen'] = abw_st

# ---------------------------------------------------------------- K9
def lese_faelle(p):
    s = open(p, encoding='utf-8').read()
    f = s.split('## Fälle')[1].split('\n## ')[0]
    out = []
    for l in f.split('\n'):
        if re.match(r'\|\s*\d+\s*\|', l):
            c = zellen(l)
            ks = frozenset(re.sub(r'\s*\(\d+\)', '', t).strip() for t in re.split(r'[/,]', c[2]) if t.strip())
            kl = c[-1] if re.match(r'F[1-7]$', c[-1]) else None
            out.append({'nr': int(c[0]), 'lauf': c[1], 'ks': ks, 'kl': kl, 'urteil': c[3]})
    return out


R = lese_faelle(P('rq3', 'Regelvorschlaege_RQ3.md'))
R2 = lese_faelle(P('rq3', 'R2', 'Regelvorschlaege_RQ3_R2.md'))
ent = [zellen(l) for l in open(P('rq3', 'Entscheidungen_RQ3.md')) if re.match(r'^\| F[1-7] \|', l)]


def schluessel(f):
    return (f['lauf'], f['ks'])


# gleiche Schluessel innerhalb eines Laufs (z. B. zwei Faelle zur selben Kennung) nach Reihenfolge durchnummerieren
def mit_index(L):
    seen = collections.Counter(); out = {}
    for f in L:
        k = schluessel(f); seen[k] += 1
        out[k + (seen[k],)] = f
    return out


RI, R2I = mit_index(R), mit_index(R2)
gem = sorted(set(RI) & set(R2I), key=lambda k: RI[k]['nr'])
paare = list(itertools.combinations(gem, 2))
gleich_alle = sum(((RI[a]['kl'] is not None and RI[a]['kl'] == RI[b]['kl']) ==
                   (R2I[a]['kl'] is not None and R2I[a]['kl'] == R2I[b]['kl'])) for a, b in paare)
beide = [k for k in gem if RI[k]['kl'] and R2I[k]['kl']]
pb = list(itertools.combinations(beide, 2))
gleich_beide = sum(((RI[a]['kl'] == RI[b]['kl']) == (R2I[a]['kl'] == R2I[b]['kl'])) for a, b in pb)
ERG['K9'] = {
    'regeln_vorgeschlagen': len({f['kl'] for f in R if f['kl']}),
    'regeln_bestaetigt': sum(1 for e in ent if e[1] == 'bestätigt'),
    'anteil_bestaetigt': sum(1 for e in ent if e[1] == 'bestätigt') / len({f['kl'] for f in R if f['kl']}),
    'faelle_R': len(R), 'klassiert_R': sum(1 for f in R if f['kl']),
    'anteil_klassiert_R': sum(1 for f in R if f['kl']) / len(R),
    'faelle_R2': len(R2), 'klassiert_R2': sum(1 for f in R2 if f['kl']),
    'gemeinsam': len(gem), 'nur_R': len(set(RI) - set(R2I)), 'nur_R2': len(set(R2I) - set(RI)),
    'nur_R_liste': sorted((RI[k]['nr']) for k in set(RI) - set(R2I)),
    'nur_R2_liste': sorted((R2I[k]['nr']) for k in set(R2I) - set(RI)),
    'paare': len(paare), 'paare_gleich': gleich_alle, 'anteil_paare_gleich': gleich_alle / len(paare),
    'in_beiden_klassiert': len(beide), 'paare_beide_klassiert': len(pb), 'paare_beide_klassiert_gleich': gleich_beide,
    'anteil_paare_beide_klassiert': gleich_beide / len(pb) if pb else None,
}

# ---------------------------------------------------------------- Vorstudie
vplan = json.load(open(P('vorstudie', 'plan.json')))
vsoll = {}
for m in ('HOR', 'LAM', 'TCD'):
    for l in open(P('soll_vorstudie', m, 'sollbefunde.md')):
        c = zellen(l)
        if len(c) > 5 and c[0].startswith(m + '-'):
            vsoll[c[0]] = {'ms': m, 'art': c[2], 'ergebnis': c[4]}
vbest = {k: v for k, v in vsoll.items() if v['ergebnis'] == 'bestätigt'}
VOR = {'soll': {'einwaende': len(vsoll), 'bestaetigt': len(vbest),
                'inhaltlich': sum(v['art'] == 'inhaltlich' for v in vbest.values()),
                'kleinkorrektur': sum(v['art'] == 'Kleinkorrektur' for v in vbest.values())},
       'gutachten': {}, 'durchgang': {}}
vabw = []
for V, x in vplan.items():
    runs = []
    for i in (1, 2, 3):
        d = {}
        for l in open(P('vorstudie', 'zuordnung', V, f'zuordnung{i}.md')):
            if re.match(r'^\| (HOR|LAM|TCD)-', l):
                c = zellen(l); d[c[0]] = c[1]
        runs.append(d)
    m = x['fall']
    ss = [s for s in vbest if vbest[s]['ms'] == m]
    r = {'lauf': x['lauf'], 'fall': m}
    gleich = 0
    for art, kz in (('inhaltlich', 'inh'), ('Kleinkorrektur', 'kk')):
        sa = [s for s in ss if vbest[s]['art'] == art]
        mh = {s: mehrheit([rr.get(s, 'FEHLT') for rr in runs]) for s in sa}
        r[f'n_{kz}'] = len(sa)
        r[f'getr_{kz}'] = sum(v == 'getroffen' for v in mh.values())
        r[f'teil_{kz}'] = sum(v == 'teilweise' for v in mh.values())
        r[f'ohne_mh_{kz}'] = sum(v is None for v in mh.values())
    r['k7_gleich'] = sum(len({rr.get(s) for rr in runs}) == 1 for s in ss)
    r['k7_n'] = len(ss)
    r['fehlend'] = sum(1 for rr in runs for s in ss if s not in rr)
    # Gegenprobe mehrheit.md
    for l in open(P('vorstudie', 'zuordnung', V, 'mehrheit.md')):
        if re.match(r'^\| (HOR|LAM|TCD)-', l):
            c = zellen(l)
            if (mehrheit(c[1:4]) or '') != c[4]:
                vabw.append((V, c[0]))
            if [runs[0].get(c[0]), runs[1].get(c[0]), runs[2].get(c[0])] != c[1:4]:
                vabw.append((V, c[0], 'Einzellauf'))
    r['k1_inh_getr'] = r['getr_inh'] / r['n_inh']
    r['k1_inh_teil'] = r['teil_inh'] / r['n_inh']
    r['k1_kk_getr'] = r['getr_kk'] / r['n_kk'] if r['n_kk'] else None
    r['k1_kk_teil'] = r['teil_kk'] / r['n_kk'] if r['n_kk'] else None
    r['k7'] = r['k7_gleich'] / r['k7_n']
    VOR['gutachten'][x['lauf']] = r
for D in ('V1', 'V2', 'V3', 'V4'):
    gs = [r for r in VOR['gutachten'].values() if r['lauf'].startswith(D + '-')]
    VOR['durchgang'][D] = {
        'gutachten': len(gs),
        'k1_inh_getr_gepoolt': sum(r['getr_inh'] for r in gs) / sum(r['n_inh'] for r in gs),
        'k1_inh_getr_mittel': sum(r['k1_inh_getr'] for r in gs) / len(gs),
        'k1_inh_teil_gepoolt': sum(r['teil_inh'] for r in gs) / sum(r['n_inh'] for r in gs),
        'k1_kk_getr_gepoolt': sum(r['getr_kk'] for r in gs) / sum(r['n_kk'] for r in gs),
        'k7_gepoolt': sum(r['k7_gleich'] for r in gs) / sum(r['k7_n'] for r in gs),
    }
VOR['k7_gesamt'] = sum(r['k7_gleich'] for r in VOR['gutachten'].values()) / sum(r['k7_n'] for r in VOR['gutachten'].values())
VOR['mehrheit_md_abweichungen'] = vabw
ERG['Vorstudie'] = VOR


# ---------------------------------------------------------------- Effektregel
def eff(name, hoch, tief):
    a, b = ERG[name][hoch], ERG[name][tief]
    return {'kennzahl': name, 'hoeher_erwartet': hoch, 'bereich_' + hoch: [a['min'], a['max']],
            'bereich_' + tief: [b['min'], b['max']], 'effekt': a['min'] > b['max'],
            'umgekehrter_effekt': b['min'] > a['max']}


k6b = ERG['K6 Anteil aus nur einer Instanz']['B']
RQ = {
    'RQ1': [eff('K1 inhaltlich getroffen (mit G03)', 'B', 'A'), eff('K1 inhaltlich getroffen (ohne G03)', 'B', 'A')],
    'RQ2': [eff('K1 inhaltlich getroffen (mit G03)', 'B', 'C'), eff('K1 inhaltlich getroffen (ohne G03)', 'B', 'C'),
            {'K6_B_mittel': k6b['mittel'], 'K6_B_min': k6b['min'], 'mindestens_ein_fuenftel_mittel': k6b['mittel'] >= 0.2,
             'mindestens_ein_fuenftel_jeder_lauf': k6b['min'] >= 0.2}],
    'RQ3': [eff('K8 F1 bis F7 je Gutachten', 'B', 'D')] + [eff(f'K8 F{i} je Gutachten', 'B', 'D') for i in range(1, 8)] +
           [{'K1_D_nicht_weniger_mit': not (ERG['K1 inhaltlich getroffen (mit G03)']['D']['max'] < ERG['K1 inhaltlich getroffen (mit G03)']['B']['min']),
             'K1_D_nicht_weniger_ohne': not (ERG['K1 inhaltlich getroffen (ohne G03)']['D']['max'] < ERG['K1 inhaltlich getroffen (ohne G03)']['B']['min']),
             'K1_D_bereich_mit': [ERG['K1 inhaltlich getroffen (mit G03)']['D']['min'], ERG['K1 inhaltlich getroffen (mit G03)']['D']['max']],
             'K1_B_bereich_mit': [ERG['K1 inhaltlich getroffen (mit G03)']['B']['min'], ERG['K1 inhaltlich getroffen (mit G03)']['B']['max']]}],
}
ERG['Effektregel'] = RQ
CHK['schwelle'] = {'anteil': schwelle, 'erreicht': schwelle >= 0.8}

json.dump({'kennzahlen': ERG, 'je_gutachten': jg}, open(os.path.join(OUT, 'ergebnis.json'), 'w'), ensure_ascii=False, indent=1, default=str)
json.dump(CHK, open(os.path.join(OUT, 'pruefungen.json'), 'w'), ensure_ascii=False, indent=1, default=str)
print(json.dumps(CHK, ensure_ascii=False, indent=1, default=str)[:6000])
