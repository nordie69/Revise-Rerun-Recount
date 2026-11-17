"""7.11.E Schritt 3 und 4: zieht die Stichprobe (15 Einzelbefunde je Bedingung, nur aus Gruppen mit KI-Mehrheit
zutreffend, nicht zutreffend oder Ansichtssache) und baut das verblindete Einstufungsblatt für den Auftraggeber
(Stichprobe und Gruppen ohne Mehrheit). Das Blatt nennt weder Bedingung noch Lauf, Instanz oder KI-Urteil.
Aufruf: einst_stichprobe.py <Startwert> <Ausgabename>. Gibt nur Zählungen aus."""
import json, re, random, sys, os, collections
HS = '/home/claude/gutachten-skill/hauptstudie'
SP = '/tmp/claude-0/-home-claude/388bb276-2a71-5718-a623-841ee1533b2f/scratchpad/einst'
SEED = int(sys.argv[1]); NAME = sys.argv[2]; JE = 15
OUT = f'{HS}/einstufung/auftraggeber'; os.makedirs(OUT, exist_ok=True)
gc = json.load(open(f'{HS}/einstufung/gruppen_codes.json'))
m2g = gc if isinstance(gc, dict) else None
kenn = json.load(open(f'{HS}/einstufung/kennungen.json'))
plan = {r['code']: r for r in json.load(open(f'{HS}/laeufe/laufplan.json', encoding='utf-8'))}
mehr = json.load(open(f'{HS}/einstufung/mehrheit.json', encoding='utf-8'))
b2g, gzeile = {}, {}
for M, G in m2g.items():
    for l in open(f'{HS}/einstufung/gruppen/{G}/gruppen.md', encoding='utf-8'):
        m = re.match(r'^\|\s*(BG-\d{3})\s*\|([^|]*)\|([^|]*)\|([^|]*)\|', l)
        if not m: continue
        bg = m.group(1); ids = re.findall(r'B[0-9a-f]{5}', m.group(2))
        gzeile[(G, bg)] = (ids, m.group(3).strip(), m.group(4).strip())
        for b in ids: b2g[b] = (G, bg)
assert set(b2g) == set(kenn), (len(b2g), len(kenn))
# Texte der Einzelbefunde je Manuskript
text = {}
for M, G in m2g.items():
    s = open(f'{SP}/{G}/befunde_voll.md', encoding='utf-8').read()
    for m in re.finditer(r'^## (B[0-9a-f]{5})\b([^\n]*)\n(.*?)(?=^## B[0-9a-f]{5}\b|\Z)', s, re.M | re.S):
        text[m.group(1)] = ((m.group(2).strip() + '\n\n') if m.group(2).strip() else '') + m.group(3).strip()
assert set(text) == set(kenn), (len(text), len(kenn))
# Ziehung
pool = collections.defaultdict(list)
for b in sorted(kenn):
    G, bg = b2g[b]
    if mehr[G][bg]['mehrheit'] in ('zutreffend', 'nicht zutreffend', 'ansichtssache'):
        pool[plan[kenn[b]['code']]['bedingung']].append(b)
rnd = random.Random(SEED); zug = []
for c in 'ABCD':
    zug += rnd.sample(pool[c], JE)
print('Pool je Bedingung', {c: len(pool[c]) for c in 'ABCD'}, 'gezogen', len(zug), 'verschieden', len(set(zug)))
json.dump(sorted(zug), open(f'{OUT}/{NAME}_gezogen.json', 'w'), indent=1)
hitl = sorted((G, bg) for G in mehr for bg, v in mehr[G].items() if v['hitl'])
# Blatt: je Manuskript, Einträge nach Kennung sortiert (zufällige Kennungen, keine Ordnung nach Bedingung)
nr = 0; md = []; tsv = ['Nr\tArt\tManuskript\tKennung\tEinstufung\tMinuten\tBegründung (freiwillig)']
md += ['# Einstufung strittiger Befunde durch den Auftraggeber', '',
       'Arbeitsdokument zu 7.11.E (Studienprotokoll Abschnitt 7, Einstufung, Punkt 3 und 4). Die Einträge stammen aus Gutachten der Hauptstudie. Angaben zu Bedingung, Fassung, Lauf und Instanz sind entfernt, ebenso das Urteil der KI. Verweise auf andere Einträge desselben Gutachtens stehen als [Eintrag].', '',
       f'Teil 1 sind {len(zug)} zufällig gezogene Einzelbefunde. Teil 2 sind {len(hitl)} Befundgruppen, bei denen die drei Einstufungsläufe keine Mehrheit ergaben oder die Mehrheit "unklar" lautete; dort gilt dein Urteil für die ganze Gruppe. Beide Teile sind je Manuskript geordnet, damit du jedes Manuskript nur einmal einlesen musst.', '',
       '**So gehst du vor:** Prüfe jeden Eintrag am PDF des Manuskripts so weit, wie es für ein Urteil nötig ist. Trage in die Erfassungsdatei (TSV) die Einstufung ein: zutreffend, nicht zutreffend oder Ansichtssache. Dazu die Minuten je Eintrag; eine Begründung ist freiwillig. Bei einer Gruppe urteilst du über den gemeinsamen Gegenstand.', '']
for M in sorted(m2g):
    G = m2g[M]
    eintr = sorted(b for b in zug if b2g[b][0] == G)
    gr = [x for x in hitl if x[0] == G]
    if not eintr and not gr: continue
    md += [f'## Manuskript egusphere-2025-{M}', '']
    if eintr:
        md += ['### Teil 1: Einzelbefunde', '']
        for b in eintr:
            nr += 1; md += [f'#### {nr}. {b}', '', text[b], '']
            tsv.append(f'{nr}\tEinzelbefund\t{M}\t{b}\t\t\t')
    if gr:
        md += ['### Teil 2: Befundgruppen ohne Mehrheit', '']
        for G_, bg in gr:
            ids, fund, geg = gzeile[(G_, bg)]
            nr += 1; md += [f'#### {nr}. Gruppe {bg} ({len(ids)} Einzelbefunde)', '', f'Fundort: {fund}', '', f'Gegenstand: {geg}', '']
            for b in ids: md += [f'##### {b}', '', text[b], '']
            tsv.append(f'{nr}\tGruppe\t{M}\t{bg}\t\t\t')
open(f'{OUT}/{NAME}.md', 'w', encoding='utf-8').write('\n'.join(md) + '\n')
open(f'{OUT}/{NAME}_Erfassung.tsv', 'w', encoding='utf-8').write('\n'.join(tsv) + '\n')
print('Einträge', nr, 'davon Einzelbefunde', len(zug), 'Gruppen', len(hitl),
      'je Manuskript', {M: sum(1 for b in zug if b2g[b][0] == G) for M, G in m2g.items()},
      'Gruppen je Manuskript', {M: sum(1 for x in hitl if x[0] == G) for M, G in m2g.items()})
