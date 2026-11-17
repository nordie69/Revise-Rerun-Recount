"""Erzeugt ein Auslagerungspaket: python3 auslagerung.py <Paketnummer> <Code> [<Code> ...]"""
import sys, os, subprocess, hashlib, json
N = sys.argv[1]; codes = sys.argv[2:]
SP = '/tmp/claude-0/-home-claude/388bb276-2a71-5718-a623-841ee1533b2f/scratchpad'
OUT = '/home/claude/gutachten-skill/hauptstudie/laeufe/auslagerung'
HS = '/home/claude/gutachten-skill/hauptstudie'
name = f'Paket{N}_{codes[0]}' + (f'-{codes[-1]}' if len(codes) > 1 else '')
liste = ', '.join(codes); und = codes[0] if len(codes) == 1 else ', '.join(codes[:-1]) + ' und ' + codes[-1]
t = open(f'{OUT}/ANLEITUNG_Paket2.md', encoding='utf-8').read()
t = t.replace('Läufe L04, L05, L06', ('Lauf ' if len(codes) == 1 else 'Läufe ') + liste)
t = t.replace('die drei Laufordner', 'den Laufordner' if len(codes) == 1 else f'die {len(codes)} Laufordner')
t = t.replace('Ordner L04, L05, L06', ('Ordner ' if len(codes) == 1 else 'Ordner ') + liste)
t = t.replace('Für jeden Ordner L04, L05, L06:', f'Für jeden Ordner ({liste}):')
t = t.replace('Wenn alle drei Läufe fertig sind', 'Wenn der Lauf fertig ist' if len(codes) == 1 else f'Wenn alle {len(codes)} Läufe fertig sind')
t = t.replace('Paket2_L04-L06', name).replace('SHA256_Paket2', f'SHA256_Paket{N}').replace('Paket 2', f'Paket {N}')
rel = SP.lstrip('/') + '/haupt'
t = t.replace(f'{rel}/L04 {rel}/L05 {rel}/L06', ' '.join(f'{rel}/{c}' for c in codes))
assert 'L04' not in t and 'L05' not in t and 'L06' not in t and 'Paket2' not in t, 'Reste'
open(f'{OUT}/ANLEITUNG_Paket{N}.md', 'w', encoding='utf-8').write(t)
sha = []
for c in codes:
    for root, _, files in os.walk(f'{SP}/haupt/{c}'):
        for f in sorted(files):
            p = os.path.join(root, f); sha.append(f'{hashlib.sha256(open(p,"rb").read()).hexdigest()}  {p}')
open(f'{SP}/haupt/SHA256_Paket{N}.txt', 'w').write('\n'.join(sorted(sha, key=lambda x: x[66:])) + '\n')
z = f'{OUT}/{name}_v1_20261017.zip'
if os.path.exists(z): os.remove(z)
subprocess.run(['zip', '-qrX', z] + [f'{rel}/{c}' for c in codes] + [f'{rel}/SHA256_Paket{N}.txt'], cwd='/', check=True)
subprocess.run(['zip', '-qX', z, f'ANLEITUNG_Paket{N}.md'], cwd=OUT, check=True)
os.remove(f'{SP}/haupt/SHA256_Paket{N}.txt')
inhalt = subprocess.run(['unzip', '-Z1', z], capture_output=True, text=True).stdout
verboten = sum(1 for l in inhalt.split('\n') if any(w in l.lower() for w in ('soll', 'laufplan', 'status.json', 'spinoff')))
st = json.load(open(f'{HS}/laeufe/status.json', encoding='utf-8'))
for c in codes: st[c] = {'gueltig': f'ausgelagert (Paket {N}, anderer Chat, 2026-10-17)'}
json.dump(st, open(f'{HS}/laeufe/status.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(os.path.basename(z), f'{os.path.getsize(z)/1e6:.0f} MB', hashlib.sha256(open(z,'rb').read()).hexdigest()[:16], len(sha), 'Dateien; verbotene Namen', verboten)
