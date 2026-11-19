"""Paper 3, Entscheidung 42: vergleicht die Einteilung "inhaltlich" und "Kleinkorrektur" zwischen Extraktion 1
und Extraktion 2 der Sollbefunde (soll/<M>/extraktion/, extraktion2/) über die Zuordnung im Abgleich
(soll/<M>/abgleich/abgleich.md). Eine Zeile von Extraktion 2 gilt als gleich eingeteilt, wenn jede Zeile von
Extraktion 1, der sie im Abgleich entspricht ("gleich" oder "Teil von"), dieselbe Art trägt.
Schreibt freigabe_e42/Artvergleich_Extraktionen_v1_20261119.md."""
import collections, re
HS = '/home/claude/gutachten-skill/hauptstudie'
M = ['4506', '4695', '4733', '5046']

def tab(text):
    return [[c.strip() for c in l.strip().strip('|').split('|')] for l in text.split('\n')
            if l.startswith('|') and not re.match(r'^\|\s*(Kennung|-)', l)]

T = ['# Einteilung der Einwände in Extraktion 1 und Extraktion 2', '',
     'Beide Extraktionen teilten jeden Einwand in "inhaltlich" oder "Kleinkorrektur" ein (Auftrag, Regel 3). Verglichen wird je Zeile von Extraktion 2 mit den Zeilen von Extraktion 1, denen sie im Abgleich entspricht. Gerechnet mit `tools/art_vergleich.py`.', '',
     '| Manuskript | Extraktion 1: inhaltlich, Kleinkorrektur | Extraktion 2: inhaltlich, Kleinkorrektur | Zeilen E2 im Abgleich (gleich, Teil von, nur in E2) | gleich eingeteilt | abweichend |',
     '|---|---|---|---|---|---|']
ges = collections.Counter(); abw = []
for m in M:
    e1 = {r[0]: r[2] for r in tab(open(f'{HS}/soll/{m}/extraktion/einwaende.md', encoding='utf-8').read())}
    e2 = {r[0]: r[2] for r in tab(open(f'{HS}/soll/{m}/extraktion2/einwaende.md', encoding='utf-8').read())}
    s = open(f'{HS}/soll/{m}/abgleich/abgleich.md', encoding='utf-8').read().split('## Extraktion 2 gegen 1')[1].split('\n## ')[0]
    z = collections.Counter(); g = 0; n = 0
    for c in tab(s):
        z[c[2]] += 1; n += 1
        ks = re.findall(r'\d{4}-RC\d-\d+', c[1])
        assert c[0] in e2 and all(k in e1 for k in ks), (m, c)
        if ks and all(e1[k] == e2[c[0]] for k in ks):
            g += 1
        else:
            abw.append((m, c[0], e2[c[0]], ', '.join(f'{k} ({e1[k]})' for k in ks), c[2]))
    assert n == len(e2)
    c1, c2 = collections.Counter(e1.values()), collections.Counter(e2.values())
    T.append(f'| {m} | {c1["inhaltlich"]}, {c1["Kleinkorrektur"]} | {c2["inhaltlich"]}, {c2["Kleinkorrektur"]} | {n} ({z["gleich"]}, {z["Teil von"]}, {z["nur in E2"]}) | {g} | {n - g} |')
    for k, v in (('i1', c1['inhaltlich']), ('k1', c1['Kleinkorrektur']), ('i2', c2['inhaltlich']), ('k2', c2['Kleinkorrektur']), ('n', n), ('g', g)):
        ges[k] += v
T.append(f'| zusammen | {ges["i1"]}, {ges["k1"]} | {ges["i2"]}, {ges["k2"]} | {ges["n"]} | {ges["g"]} ({100*ges["g"]/ges["n"]:.1f} %) | {ges["n"] - ges["g"]} |'.replace('.', ',', 1) if False else
         f'| zusammen | {ges["i1"]}, {ges["k1"]} | {ges["i2"]}, {ges["k2"]} | {ges["n"]} | {ges["g"]} ({f"{100*ges["g"]/ges["n"]:.1f}".replace(".", ",")} %) | {ges["n"] - ges["g"]} |')
T += ['', 'In keinem Abgleich gibt es Zeilen, die nur in einer der beiden Extraktionen stehen.', '', '## Abweichende Einteilungen', '',
      '| Manuskript | Kennung E2 | Art in E2 | entsprechende Zeile E1 (Art) | Entsprechung |', '|---|---|---|---|---|']
T += [f'| {a} | {b} | {c} | {d} | {e} |' for a, b, c, d, e in abw]
out = '\n'.join(T) + '\n'
assert '—' not in out and '–' not in out
open(f'{HS}/freigabe_e42/Artvergleich_Extraktionen_v1_20261119.md', 'w', encoding='utf-8').write(out)
print(out)
