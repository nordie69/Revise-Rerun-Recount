"""Zuordnung (7.5): Mehrheit zwei von drei je Sollbefund und Eintrag. Aufruf: python3 zuordnung_mehrheit.py <N-Code> [...]
Schreibt nach laeufe/zuordnung/<N>/: zuordnung1..3.md (Kopien), mehrheit.md (Sollbefund, drei Antworten, Mehrheit,
Einträge mit Mehrheit) und hitl.md (ohne Mehrheit oder Mehrheit unklar, für den Auftraggeber). Gibt nur Zählungen aus."""
import collections, os, re, shutil, sys
HS = '/home/claude/gutachten-skill/hauptstudie'
SP = '/tmp/claude-0/-home-claude/388bb276-2a71-5718-a623-841ee1533b2f/scratchpad/nach'
ART = {'getroffen', 'teilweise', 'verfehlt', 'unklar'}
def tab(p):
    return [[x.strip() for x in l.strip().strip('|').split('|')] for l in open(p, encoding='utf-8')
            if l.startswith('|') and not re.match(r'^\|\s*(Sollbefund|Kennung|-)', l)]
for N in sys.argv[1:]:
    R = f'{SP}/{N}'; Z = f'{HS}/laeufe/zuordnung/{N}'; os.makedirs(Z, exist_ok=True)
    soll = [r[0] for r in tab(f'{R}/sollbefunde.md')]
    laeufe = []
    for k in (1, 2, 3):
        p = f'{R}/zu{k}/zuordnung.md'; shutil.copy2(p, f'{Z}/zuordnung{k}.md')
        d = {}
        for r in tab(p):
            if len(r) >= 3 and r[0] in soll:
                a = r[1].lower().strip()
                e = set(re.findall(r'\b(?:GB|KK)-\d+\b', r[2]))
                d[r[0]] = (a if a in ART else 'ungültig', e)
        print(N, f'Lauf {k}:', len(d), 'Antworten; fehlend', len(set(soll) - set(d)), '; ungültig', sum(v[0] == 'ungültig' for v in d.values()))
        laeufe.append(d)
    zeilen = ['| Sollbefund | Lauf 1 | Lauf 2 | Lauf 3 | Mehrheit | Einträge mit Mehrheit |', '|---|---|---|---|---|---|']
    hitl = ['| Sollbefund | Lauf 1 | Lauf 2 | Lauf 3 |', '|---|---|---|---|']
    z = collections.Counter(); gleich = 0
    for s in soll:
        a = [l.get(s, ('fehlt', set())) for l in laeufe]
        c = collections.Counter(x[0] for x in a); top, n = c.most_common(1)[0]
        gleich += (n == 3)
        if n >= 2 and top in ('getroffen', 'teilweise', 'verfehlt'):
            m = top
        else:
            m = 'Auftraggeber'; hitl.append(f"| {s} | {' | '.join(x[0] + (' (' + ', '.join(sorted(x[1])) + ')' if x[1] else '') for x in a)} |")
        if m in ('getroffen', 'teilweise'):
            ec = collections.Counter(e for x in a if x[0] in ('getroffen', 'teilweise') for e in x[1])
            em = sorted(e for e, k in ec.items() if k >= 2)
        else:
            em = []
        z[m] += 1
        zeilen.append(f"| {s} | {a[0][0]} | {a[1][0]} | {a[2][0]} | {m} | {', '.join(em)} |")
    open(f'{Z}/mehrheit.md', 'w', encoding='utf-8').write('\n'.join(zeilen) + '\n')
    open(f'{Z}/hitl.md', 'w', encoding='utf-8').write('\n'.join(hitl) + '\n')
    print(N, len(soll), 'Sollbefunde; alle drei gleich', gleich, ';', dict(z))
