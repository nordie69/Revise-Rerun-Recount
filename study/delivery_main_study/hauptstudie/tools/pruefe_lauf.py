"""Prüft einen fertigen Lauf der Hauptstudie und trägt ihn in laeufe/status.json ein.

Aufruf: python3 pruefe_lauf.py <Code> [--modell <bedienendes Modell>]
Prüft: Gutachten vorhanden; Formatprüfung des Skills der Fassung meldet 0 Fehler; jede Zugriffsdatei
nennt nur Pfade im eigenen Laufordner und keine verbotenen URLs. Kopiert das Gutachten nach
laeufe/ergebnis/<Code>/ (schreibgeschützt) und schreibt Datum, SHA-256 und Gültigkeit in status.json.
Gibt nur Messwerte aus, keinen Inhalt des Gutachtens.
"""
import datetime, hashlib, json, os, re, shutil, subprocess, sys

HS = '/home/claude/gutachten-skill/hauptstudie'
SP = '/tmp/claude-0/-home-claude/388bb276-2a71-5718-a623-841ee1533b2f/scratchpad/haupt'
VERBOTEN = re.compile(r'copernicus|egusphere\.|unpaywall|/home/claude|/root/|/mnt/skills', re.I)

code = sys.argv[1]
modell = sys.argv[sys.argv.index('--modell') + 1] if '--modell' in sys.argv else ''
plan = {r['code']: r for r in json.load(open(f'{HS}/laeufe/laufplan.json', encoding='utf-8'))}
r = plan[code]; R = f'{SP}/{code}'
g = f"{R}/egusphere-2025-{r['manuskript']}_Gutachten.md"
gruende = []
if not os.path.exists(g):
    gruende.append('kein Gutachten')
    fehler = None
else:
    out = subprocess.run(['python3', f'{R}/skills/science-review-gutachten/scripts/formatpruefung.py', g], capture_output=True, text=True)
    txt = out.stdout + out.stderr
    m = re.search(r'(\d+)\s+Fehler', txt)
    fehler = int(m.group(1)) if m else None
    if fehler != 0:
        gruende.append(f'Formatprüfung {fehler if fehler is not None else "ohne Ergebnis"} Fehler')
zug = [f for f in os.listdir(R) if f.startswith('zugriff_')]
erwartet = {'C'} if r['aufbau'] == 'nacheinander' else {'VB', 'S1', 'S2', 'S3', 'S4', 'AB', 'SD', 'ZF'}
fehlt = sorted(erwartet - {f[8:-4] for f in zug})
if fehlt:
    gruende.append('Zugriffsdatei fehlt: ' + ' '.join(fehlt))
ausserhalb = []
for f in zug:
    for n, l in enumerate(open(f'{R}/{f}', encoding='utf-8', errors='replace'), 1):
        pfade = re.findall(r'(/[^\s`\'"(),;]+)', l)
        for p in pfade:
            if p.startswith('/') and not p.startswith(R) and not p.startswith('/tmp/claude-0/-home-claude/388bb276-2a71-5718-a623-841ee1533b2f/tasks') and '/tool-results/' not in p and not p.startswith(('/usr/', '/bin/', '/proc/', '/dev/')):
                if re.match(r'^/[a-zA-Z]', p) and not re.match(r'^/(abs|doi|articles?|content|pdf|wiki|search|en|de)\b', p):
                    ausserhalb.append(f'{f}:{n}')
                    break
        if VERBOTEN.search(l) and not re.search(r'nicht (gelesen|geöffnet)|verboten|nicht lesen', l, re.I):
            ausserhalb.append(f'{f}:{n} (verbotene Quelle)')
if ausserhalb:
    gruende.append('Zugriffe prüfen: ' + ', '.join(sorted(set(ausserhalb))[:10]))
st_p = f'{HS}/laeufe/status.json'
st = json.load(open(st_p, encoding='utf-8')) if os.path.exists(st_p) else {}
e = {'datum': datetime.date.today().isoformat(), 'modell': modell}
if os.path.exists(g):
    os.makedirs(f'{HS}/laeufe/ergebnis/{code}', exist_ok=True)
    ziel = f'{HS}/laeufe/ergebnis/{code}/' + os.path.basename(g)
    if os.path.exists(ziel):
        os.chmod(ziel, 0o644)
    shutil.copy2(g, ziel); os.chmod(ziel, 0o444)
    e['gutachten_sha'] = hashlib.sha256(open(ziel, 'rb').read()).hexdigest()[:12]
e['gueltig'] = 'gültig' if not gruende else 'prüfen: ' + '; '.join(gruende)
st[code] = e
json.dump(st, open(st_p, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(code, r['kennung'], '|', e['gueltig'], '| Formatprüfung Fehler:', fehler, '| Zugriffsdateien:', len(zug), '| SHA:', e.get('gutachten_sha', ''))
