"""7.8 Auswertung der Hauptstudie, Teil 1: K1, K2, K3, K5, K6, K7 je Gutachten und je Bedingung, mit und ohne G03.
Quellen: laeufe/laufplan.json, laeufe/nachverarbeitung.json, soll/<M>/sollbefunde.md, laeufe/zuordnung/<N>/,
laeufe/ergebnis/<L>/*_Gutachten.md, einstufung/endgueltig_einzelbefunde.json, einstufung/mehrheit.json,
einstufung/k7_stichprobe_20261115.json. Schreibt auswertung/kennzahlen_je_gutachten.json und auswertung/kennzahlen_teil1.md.
G03 ist das Gutachten egusphere-2025-4506-RC3 (spinoff_ki_herkunft/Kennzeichnung_KI_Herkunft_20261017.md)."""
import collections, glob, itertools, json, os, re, statistics
HS = '/home/claude/gutachten-skill/hauptstudie'
OUT = f'{HS}/auswertung'; os.makedirs(OUT, exist_ok=True)
plan = {r['code']: r for r in json.load(open(f'{HS}/laeufe/laufplan.json', encoding='utf-8'))}
nv = json.load(open(f'{HS}/laeufe/nachverarbeitung.json', encoding='utf-8'))
ein = json.load(open(f'{HS}/einstufung/endgueltig_einzelbefunde.json', encoding='utf-8'))
roh = {(e['code'], e['kennung']): e for e in json.load(open(f'{HS}/einstufung/einzelbefunde.json', encoding='utf-8'))}

def tab(p):
    return [[x.strip() for x in l.strip().strip('|').split('|')] for l in open(p, encoding='utf-8')
            if l.startswith('|') and not re.match(r'^\|\s*(Sollbefund|Kennung|-)', l)]

# Sollbefunde: Art und G03
SOLL = {}
for M in ('4506', '4695', '4733', '5046'):
    for c in tab(f'{HS}/soll/{M}/sollbefunde.md'):
        if len(c) >= 7 and c[4] == 'bestätigt':
            SOLL[c[0]] = {'M': M, 'art': c[2], 'g03': M == '4506' and c[1].startswith('RC3')}
assert collections.Counter((v['art'], v['g03']) for v in SOLL.values()) == collections.Counter(
    {('inhaltlich', False): 124, ('Kleinkorrektur', False): 54, ('inhaltlich', True): 19, ('Kleinkorrektur', True): 1})

def feld(text, name):
    m = re.search(rf'^\|\s*{name}\s*\|\s*(.*?)\s*\|\s*$', text, re.M | re.I)
    return m.group(1).strip() if m else ''

def kk_source(text):
    zeilen = text.split('\n')
    if len(zeilen) < 2: return ''
    h = [x.strip().lower() for x in zeilen[0].strip().strip('|').split('|')]
    r = [x.strip() for x in zeilen[-1].strip().strip('|').split('|')]
    return r[h.index('source')] if 'source' in h and h.index('source') < len(r) else ''

INST = re.compile(r'\b(S[1-4]|AB|SD)\b')
G = {}
for L, r in sorted(plan.items()):
    N = nv[L]; M = r['manuskript']
    mh = tab(f'{HS}/laeufe/zuordnung/{N}/mehrheit.md')
    rows = [x for x in mh if x[0] in SOLL]
    assert len(rows) == sum(1 for v in SOLL.values() if v['M'] == M), L
    laeufe = [{x[0]: x[1].lower() for x in tab(f'{HS}/laeufe/zuordnung/{N}/zuordnung{k}.md') if len(x) >= 2 and x[0] in SOLL} for k in (1, 2, 3)]
    d = {'L': L, 'N': N, 'bed': r['bedingung'], 'M': M, 'wdh': r['wdh']}
    for ohne in (False, True):
        sfx = '_ohneG03' if ohne else ''
        use = [x for x in rows if not (ohne and SOLL[x[0]]['g03'])]
        for art, key in (('inhaltlich', 'inh'), ('Kleinkorrektur', 'kk')):
            u = [x for x in use if SOLL[x[0]]['art'] == art]
            d[f'K1_{key}_getroffen{sfx}'] = sum(x[4] == 'getroffen' for x in u) / len(u)
            d[f'K1_{key}_teilweise{sfx}'] = sum(x[4] == 'teilweise' for x in u) / len(u)
            d[f'n_soll_{key}{sfx}'] = len(u)
        # K7 Zuordnung: Anteil der Sollbefunde mit drei gleichen Antworten
        d[f'K7_zuordnung_gleich{sfx}'] = sum(1 for x in use if len({l.get(x[0]) for l in laeufe}) == 1) / len(use)
        # Einträge mit Sollbefund (Mehrheit getroffen oder teilweise, Einträge mit mindestens zwei Nennungen)
        mit = set()
        for x in use:
            if x[4] in ('getroffen', 'teilweise') and len(x) > 5:
                mit |= set(re.findall(r'\b(?:GB|KK)-\d+\b', x[5]))
        E = [e for e in ein if e['code'] == L]
        d['n_eintraege'] = len(E); d['n_gb'] = sum(e['kennung'].startswith('GB') for e in E); d['n_kk'] = d['n_eintraege'] - d['n_gb']
        d[f'K2{sfx}'] = sum(e['urteil'] == 'nicht zutreffend' for e in E) / len(E)
        d[f'K2_ansichtssache{sfx}'] = sum(e['urteil'] == 'ansichtssache' for e in E) / len(E)
        d[f'K3{sfx}'] = sum(1 for e in E if e['urteil'] == 'zutreffend' and e['kennung'] not in mit)
        d[f'_mit{sfx}'] = sorted(mit)
    # K6: zutreffende Einträge, deren Herkunft nur eine Prüfinstanz nennt.
    # Quelle direkt aus dem Gutachten: GB-Blöcke (Zeile Source), KK-Tabellen über die Kopfzeile mit Spalte Source
    # (Kopfzeilen heißen je Gutachten ID, Code oder Kennung; Fehler der ersten Fassung, gefunden in der Gegenrechnung).
    gtxt = open(glob.glob(f'{HS}/laeufe/ergebnis/{L}/*_Gutachten.md')[0], encoding='utf-8').read()
    quelle = {}
    for mm in re.finditer(r'\*\*(GB-\d+)\b.*?(?=\*\*GB-\d+|\n#{1,4} |\Z)', gtxt, re.S):
        sq = re.search(r'\|\s*Source\s*\|\s*([^|\n]*)\|', mm.group(0)); quelle[mm.group(1)] = sq.group(1) if sq else ''
    kopf = None
    for zl in gtxt.splitlines():
        if zl.startswith('|'):
            zc = [x.strip() for x in zl.strip().strip('|').split('|')]
            if 'Source' in zc: kopf = zc; continue
            if zc and re.fullmatch(r'KK-\d+', zc[0]) and kopf and len(zc) == len(kopf): quelle[zc[0]] = zc[kopf.index('Source')]
    zutr = [e for e in ein if e['code'] == L and e['urteil'] == 'zutreffend']
    eins = 0; bekannt = 0
    for e in zutr:
        inst = set(INST.findall(quelle.get(e['kennung'], '')))
        if e['kennung'] in quelle: bekannt += 1
        if len(inst) == 1: eins += 1
    d['K6'] = eins / len(zutr) if zutr else None; d['K6_herkunft_bekannt'] = bekannt; d['K6_zutreffend'] = len(zutr)
    G[L] = d

# K5 Schweregrade: gemeinsame Befunde zweier Läufe derselben Bedingung am selben Manuskript
SEV = {}
for e in ein:
    if e['kennung'].startswith('GB'):
        SEV[(e['code'], e['kennung'])] = feld(roh[(e['code'], e['kennung'])]['text'], 'Severity').lower()
def schwere_paare(bed, M):
    Ls = sorted(L for L, d in G.items() if d['bed'] == bed and d['M'] == M)
    # Gegenstand eines Eintrags: Sollbefunde (Mehrheit) oder Befundgruppe der Einstufung
    geg = {}
    for L in Ls:
        for x in tab(f"{HS}/laeufe/zuordnung/{G[L]['N']}/mehrheit.md"):
            if x[0] in SOLL and x[4] in ('getroffen', 'teilweise') and len(x) > 5:
                for k in re.findall(r'\bGB-\d+\b', x[5]): geg.setdefault((L, k), set()).add('S:' + x[0])
    for e in ein:
        if e['code'] in Ls and e.get('gruppe') and e['kennung'].startswith('GB'):
            geg.setdefault((e['code'], e['kennung']), set()).add('G:' + e['gruppe'])
    gleich = n = 0
    for a, b in itertools.combinations(Ls, 2):
        A = [(k, g) for (L, k), g in geg.items() if L == a]; B = [(k, g) for (L, k), g in geg.items() if L == b]
        for ka, ga in A:
            for kb, gb in B:
                if ga & gb and SEV.get((a, ka)) and SEV.get((b, kb)):
                    n += 1; gleich += SEV[(a, ka)] == SEV[(b, kb)]
    return gleich, n

json.dump(G, open(f'{OUT}/kennzahlen_je_gutachten.json', 'w', encoding='utf-8'), indent=1, ensure_ascii=False)

def mr(vals):
    vals = [v for v in vals if v is not None]
    return statistics.mean(vals), min(vals), max(vals)
f = lambda x, p=True: (f'{100*x:.1f}' if p else f'{x:.1f}').replace('.', ',')
def je_lauf(b, zaehler, nenner):
    """Wert je Wiederholung k (1 bis 3), über die vier Manuskripte gepoolt: Summe Zähler durch Summe Nenner."""
    out = []
    for k in (1, 2, 3):
        ds = [d for d in G.values() if d['bed'] == b and d['wdh'] == k]
        out.append(sum(zaehler(d) for d in ds) / sum(nenner(d) for d in ds))
    return out
def zeile(name, zaehler, nenner, p=True):
    out = [name]
    for b in 'ABCD':
        m, lo, hi = mr(je_lauf(b, zaehler, nenner)); out.append(f'{f(m,p)} ({f(lo,p)} bis {f(hi,p)})')
    return '| ' + ' | '.join(out) + ' |'
def effekt(zaehler, nenner, a, b):
    A = je_lauf(a, zaehler, nenner); B = je_lauf(b, zaehler, nenner)
    if min(A) > max(B): return f'{a} über {b}, Spannweiten getrennt'
    if min(B) > max(A): return f'{b} über {a}, Spannweiten getrennt'
    return 'Spannweiten überlappen, kein Effekt'
def anteil(key, nkey): return (lambda d: round(d[key] * d[nkey])), (lambda d: d[nkey])
T = ['# Kennzahlen der Hauptstudie, Teil 1 (K1, K2, K3, K5, K6, K7)', '',
     'Arbeitsdokument zu 7.8. Je Bedingung Mittelwert und Spannweite (kleinster bis größter Wert) über die drei Wiederholungen; je Wiederholung sind die vier Manuskripte gepoolt (Summe der Treffer durch Summe der Sollbefunde). Anteile in Prozent. Gerechnet mit `tools/auswertung.py`.', '']
for ohne in (False, True):
    s = '_ohneG03' if ohne else ''
    ki = anteil(f'K1_inh_getroffen{s}', f'n_soll_inh{s}')
    T += [f"## {'Ohne die Sollbefunde' if ohne else 'Mit den Sollbefunden'} aus G03", '', '| Kennzahl | A | B | C | D |', '|---|---|---|---|---|',
          zeile('K1 inhaltlich, getroffen (Hauptmaß)', *ki), zeile('K1 inhaltlich, teilweise', *anteil(f'K1_inh_teilweise{s}', f'n_soll_inh{s}')),
          zeile('K1 Kleinkorrekturen, getroffen', *anteil(f'K1_kk_getroffen{s}', f'n_soll_kk{s}')), zeile('K1 Kleinkorrekturen, teilweise', *anteil(f'K1_kk_teilweise{s}', f'n_soll_kk{s}')),
          zeile('K2 nicht zutreffend, Anteil an allen Einträgen', *anteil(f'K2{s}', 'n_eintraege')), zeile('K2 ergänzend: Ansichtssache, Anteil', *anteil(f'K2_ansichtssache{s}', 'n_eintraege')),
          zeile('K3 Zusatzbefunde je Gutachten (Anzahl)', lambda d: d[f'K3{s}'], lambda d: 1, False),
          zeile('K7 Zuordnung, drei Läufe gleich', *anteil(f'K7_zuordnung_gleich{s}', f'n_soll_inh{s}') if False else (lambda d: round(d[f'K7_zuordnung_gleich{s}'] * (d[f'n_soll_inh{s}'] + d[f'n_soll_kk{s}'])), lambda d: d[f'n_soll_inh{s}'] + d[f'n_soll_kk{s}'])), '',
          'Effektregel (Abschnitt 9, Regel 2) für das Hauptmaß: RQ1 A gegen B: ' + effekt(*ki, 'A', 'B') + '; RQ2 B gegen C: ' + effekt(*ki, 'B', 'C') + '; RQ3 B gegen D (ohne weniger zu treffen): ' + effekt(*ki, 'B', 'D') + '.', '',
          '| K1 inhaltlich, getroffen, je Manuskript | A | B | C | D |', '|---|---|---|---|---|']
    for M in ('4506', '4695', '4733', '5046'):
        z = [M]
        for b in 'ABCD':
            v = [G[L][f'K1_inh_getroffen{s}'] for L in G if G[L]['bed'] == b and G[L]['M'] == M]
            z.append(f'{f(statistics.mean(v))} ({f(min(v))} bis {f(max(v))})')
        T.append('| ' + ' | '.join(z) + ' |')
    T.append('')
T += ['## Umfang und Herkunft', '', '| Größe | A | B | C | D |', '|---|---|---|---|---|',
      zeile('Einträge je Gutachten', lambda d: d['n_eintraege'], lambda d: 1, False), zeile('davon inhaltliche Befunde', lambda d: d['n_gb'], lambda d: 1, False), zeile('davon Kleinkorrekturen', lambda d: d['n_kk'], lambda d: 1, False),
      zeile('K6 zutreffende Einträge aus nur einer Prüfinstanz', lambda d: round(d['K6'] * d['K6_zutreffend']), lambda d: d['K6_zutreffend']), '',
      'K6 zählt eine Prüfinstanz (S1 bis S4, AB, SD) im Feld Source; Einträge ohne erkennbare Instanz (etwa nur "ZF") zählen nicht als Einzelinstanz, bleiben aber im Nenner. In C stehen alle Schritte in einem Kontext; der Wert dort ist nicht mit B vergleichbar.', '']
# K5
T += ['## K5 Streuung', '', 'Spannweite von K1 (inhaltlich, getroffen) über die drei Wiederholungen je Manuskript, in Prozentpunkten; daneben der Anteil gleicher Schweregrade bei gemeinsamen Befunden zweier Läufe (gleicher Sollbefund nach Mehrheit oder gleiche Befundgruppe der Einstufung).', '',
      '| Manuskript | A | B | C | D |', '|---|---|---|---|---|']
for M in ('4506', '4695', '4733', '5046'):
    z = [M]
    for b in 'ABCD':
        v = [G[L]['K1_inh_getroffen'] for L in G if G[L]['bed'] == b and G[L]['M'] == M]
        z.append(f(max(v) - min(v)))
    T.append('| ' + ' | '.join(z) + ' |')
z = ['gleiche Schweregrade']
for b in 'ABCD':
    gl = n = 0
    for M in ('4506', '4695', '4733', '5046'):
        a, c = schwere_paare(b, M); gl += a; n += c
    z.append(f'{f(gl/n)} ({gl} von {n} Paaren)')
T += ['| ' + ' | '.join(z) + ' |', '']
# K7 übrige Teile
k7 = json.load(open(f'{HS}/einstufung/k7_stichprobe_20261115.json'))
mh = json.load(open(f'{HS}/einstufung/mehrheit.json', encoding='utf-8'))
ng = sum(len(g) for g in mh.values()); nm = sum(1 for g in mh.values() for v in g.values() if v['mehrheit'] and v['mehrheit'] != 'unklar')
T += ['## K7 Übereinstimmung der Urteilenden', '',
      f'Befundgruppen mit Mehrheit in den drei Einstufungsläufen der KI: {nm} von {ng} ({f(nm/ng)} %); die Gruppen umfassen alle Bedingungen.',
      f"Stichprobe Auftraggeber gegen Gruppe: {k7['uebereinstimmung']} von {k7['stichprobe']} ({f(k7['anteil'])} %); A {k7['je_bedingung']['A'][0]} von 15, B {k7['je_bedingung']['B'][0]} von 15, C {k7['je_bedingung']['C'][0]} von 15, D {k7['je_bedingung']['D'][0]} von 15.", '']
open(f'{OUT}/kennzahlen_teil1.md', 'w', encoding='utf-8').write('\n'.join(T) + '\n')
print('\n'.join(T))
