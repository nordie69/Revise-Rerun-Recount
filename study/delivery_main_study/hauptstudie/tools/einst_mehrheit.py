"""7.11.E Schritt 2/3: prüft die 72 einstufung.md (jede Gruppe je Lauf genau einmal, gültiges Urteil),
bildet die Mehrheit 2 von 3 je Gruppe und schreibt einstufung/mehrheit.json. Gibt nur Zählungen aus."""
import json, os, re, collections
HS = '/home/claude/gutachten-skill/hauptstudie'
SP = '/tmp/claude-0/-home-claude/388bb276-2a71-5718-a623-841ee1533b2f/scratchpad/einst'
GUELTIG = {'zutreffend', 'nicht zutreffend', 'ansichtssache', 'unklar'}
gc = json.load(open(f'{HS}/einstufung/gruppen_codes.json'))
codes = list(gc.values()) if isinstance(gc, dict) else gc
ROW = re.compile(r'^\|\s*(BG-\d{3})\s*\|\s*([^|]+?)\s*\|')
erg = {}; fehler = 0
for G in codes:
    soll = set(re.findall(r'^\|\s*(BG-\d{3})\s*\|', open(f'{HS}/einstufung/gruppen/{G}/gruppen.md', encoding='utf-8').read(), re.M))
    urteile = {}
    for k in (1, 2, 3):
        teile = sorted(d for d in os.listdir(f'{SP}/{G}') if re.fullmatch(fr'e{k}_t\d+', d))
        seen = collections.Counter(); u = {}
        for d in teile:
            f = f'{SP}/{G}/{d}/einstufung.md'
            if not os.path.exists(f):
                print(G, d, 'einstufung.md fehlt'); fehler += 1; continue
            for line in open(f, encoding='utf-8'):
                m = ROW.match(line)
                if not m: continue
                gid, ur = m.group(1), m.group(2).strip().strip('*').strip().lower()
                seen[gid] += 1
                if ur not in GUELTIG:
                    print(G, d, 'ungültiges Urteil in einer Zeile'); fehler += 1; continue
                u[gid] = ur
        doppelt = sum(1 for v in seen.values() if v > 1)
        fehlt = len(soll - set(seen)); fremd = len(set(seen) - soll)
        print(G, f'Lauf {k}', 'Teile', len(teile), 'Gruppen', len(u), 'fehlend', fehlt, 'doppelt', doppelt, 'fremd', fremd)
        fehler += fehlt + doppelt + fremd
        urteile[k] = u
    gr = {}
    for gid in sorted(soll):
        tri = [urteile[k].get(gid) for k in (1, 2, 3)]
        c = collections.Counter(x for x in tri if x)
        top, n = (c.most_common(1)[0] if c else (None, 0))
        mehr = top if n >= 2 and top != 'unklar' else None
        gr[gid] = {'urteile': tri, 'mehrheit': mehr, 'hitl': mehr is None,
                   'einstimmig': n == 3}
    erg[G] = gr
    z = collections.Counter(v['mehrheit'] or 'HITL' for v in gr.values())
    print(G, 'Gruppen', len(gr), 'einstimmig', sum(v['einstimmig'] for v in gr.values()), dict(z))
json.dump(erg, open(f'{HS}/einstufung/mehrheit.json', 'w', encoding='utf-8'), indent=1, ensure_ascii=False)
alle = [v for g in erg.values() for v in g.values()]
z = collections.Counter(v['mehrheit'] or 'HITL' for v in alle)
print('GESAMT Gruppen', len(alle), 'einstimmig', sum(v['einstimmig'] for v in alle), dict(z), 'Fehler', fehler)
