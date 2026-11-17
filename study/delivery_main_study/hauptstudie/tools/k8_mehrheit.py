"""7.8, K4 und K8: Mehrheit zwei von drei je Fall aus den drei Zählläufen je Prüfbericht.
Ein Fall ist bei F1 bis F6 (Klasse, Kennung), bei K4 und F7 (Klasse, Menge der Kennungen).
Schreibt auswertung/k8/<N>/zaehlung1..3.md (Kopien), auswertung/k8/mehrheit.json und auswertung/kennzahlen_k4_k8.md."""
import collections, json, os, re, shutil, statistics
HS = '/home/claude/gutachten-skill/hauptstudie'
SP = '/tmp/claude-0/-home-claude/388bb276-2a71-5718-a623-841ee1533b2f/scratchpad/k8'
OUT = f'{HS}/auswertung'
plan = {r['code']: r for r in json.load(open(f'{HS}/laeufe/laufplan.json', encoding='utf-8'))}
nv = json.load(open(f'{HS}/laeufe/nachverarbeitung.json', encoding='utf-8'))
G = json.load(open(f'{OUT}/kennzahlen_je_gutachten.json', encoding='utf-8'))
KL = ['K4', 'F1', 'F2', 'F3', 'F4', 'F5', 'F6', 'F7']

def faelle(p):
    s = set(); fehler = 0
    for l in open(p, encoding='utf-8'):
        if not l.startswith('|') or re.match(r'^\|\s*(Klasse|-)', l): continue
        c = [x.strip() for x in l.strip().strip('|').split('|')]
        m = re.match(r'(K4|F[1-7])\b', c[0]) if c else None
        ids = sorted(set(re.findall(r'\b(?:GB|KK)-\d+\b', c[1]))) if len(c) > 1 else []
        if not m or not ids: fehler += 1; continue
        k = m.group(1)
        if k in ('K4', 'F7'): s.add((k, tuple(ids)))
        else:
            for i in ids: s.add((k, (i,)))
    return s, fehler

res = {}; fehl_ges = 0; gleich = vereinigt = 0
for L, r in sorted(plan.items()):
    N = nv[L]; Z = f'{OUT}/k8/{N}'; os.makedirs(Z, exist_ok=True)
    runs = []
    for k in (1, 2, 3):
        p = f'{SP}/{N}/z{k}/zaehlung.md'; shutil.copy2(p, f'{Z}/zaehlung{k}.md')
        f, e = faelle(p); fehl_ges += e; runs.append(f)
    c = collections.Counter(x for f in runs for x in f)
    mehr = sorted(x for x, n in c.items() if n >= 2)
    vereinigt += len(c); gleich += sum(1 for n in c.values() if n == 3)
    zahl = collections.Counter(k for k, _ in mehr)
    res[L] = {'N': N, 'bed': r['bedingung'], 'M': r['manuskript'], 'wdh': r['wdh'],
              **{k: zahl[k] for k in KL}, 'F_summe': sum(zahl[k] for k in KL if k != 'K4'),
              'faelle': [[k, list(i)] for k, i in mehr]}
json.dump(res, open(f'{OUT}/k8/mehrheit.json', 'w', encoding='utf-8'), indent=1, ensure_ascii=False)

def je_lauf(b, key, norm=False):
    out = []
    for k in (1, 2, 3):
        ds = [L for L, d in res.items() if d['bed'] == b and d['wdh'] == k]
        v = sum(res[L][key] for L in ds)
        out.append(v / (sum(G[L]['n_eintraege'] for L in ds) / 100) if norm else v / len(ds))
    return out
fm = lambda x: f'{x:.2f}'.replace('.', ',')
def zeile(name, key, norm=False):
    z = [name]
    for b in 'ABCD':
        v = je_lauf(b, key, norm); z.append(f'{fm(statistics.mean(v))} ({fm(min(v))} bis {fm(max(v))})')
    return '| ' + ' | '.join(z) + ' |'
def effekt(key, a, b, norm=False):
    A = je_lauf(a, key, norm); B = je_lauf(b, key, norm)
    if max(A) < min(B): return f'{a} unter {b}, Spannweiten getrennt'
    if max(B) < min(A): return f'{b} unter {a}, Spannweiten getrennt'
    return 'Spannweiten überlappen, kein Effekt'
T = ['# Kennzahlen der Hauptstudie, Teil 2 (K4, K8)', '',
     'Arbeitsdokument zu 7.8. Je Prüfbericht drei unabhängige, verblindete Zähler nach `auswertung/k8/zaehlregeln.md`; ein Fall zählt, wenn mindestens zwei Zähler ihn nennen. Je Bedingung Mittelwert und Spannweite über die drei Wiederholungen, je Wiederholung Mittel der Fälle je Gutachten über die vier Manuskripte. Die Sollbefunde aus G03 berühren K4 und K8 nicht; die Werte gelten mit und ohne G03 gleich. Gerechnet mit `tools/k8_mehrheit.py`.', '',
     '## Fälle je Gutachten', '', '| Klasse | A | B | C | D |', '|---|---|---|---|---|']
T += [zeile(k, k) for k in KL]
T += [zeile('F1 bis F7 zusammen', 'F_summe'), zeile('F1 bis F7 je 100 Einträge (ergänzend)', 'F_summe', True), '',
      'Effektregel für RQ3, B gegen D (F1 bis F7 zusammen, je Gutachten): ' + effekt('F_summe', 'B', 'D') + '; je 100 Einträge: ' + effekt('F_summe', 'B', 'D', True) + '.', '',
      '| Klasse, B gegen D | Ergebnis |', '|---|---|']
T += [f'| {k} | {effekt(k, "B", "D")} |' for k in KL]
T += ['', f'Übereinstimmung der Zähler: {gleich} von {vereinigt} genannten Fällen von allen drei Zählern genannt ({100*gleich/vereinigt:.1f} %).'.replace('.', ',', 1) if False else f'Übereinstimmung der Zähler: {gleich} von {vereinigt} genannten Fällen von allen drei Zählern genannt ({f"{100*gleich/vereinigt:.1f}".replace(".", ",")} %). Nicht auswertbare Tabellenzeilen: {fehl_ges}.', '']
open(f'{OUT}/kennzahlen_k4_k8.md', 'w', encoding='utf-8').write('\n'.join(T) + '\n')
print('\n'.join(T))
