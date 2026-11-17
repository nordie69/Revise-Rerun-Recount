"""7.10, SB-74: liest jedes PDF des Testkorpus mit einlesen.py aller Fassungen 1.0.0 bis 1.5.0 und hält fest,
ob Randzeilen erkannt werden, wie viele Randnummern als Anker dienen und ob text.json gleich der Fassung 1.4.0 ist.
Schreibt rueckschreiben/Randzeilen_Fassungen_v1_20261115.md. Arbeitsordner im Scratchpad."""
import hashlib, json, os, subprocess, sys
P = '/home/claude/gutachten-skill'
SP = '/tmp/claude-0/-home-claude/388bb276-2a71-5718-a623-841ee1533b2f/scratchpad/randzeilen'
FASS = ['1.0.0', '1.1.0', '1.2.0', '1.3.0', '1.4.0', '1.5.0']
PDF = sorted(f for f in os.listdir(f'{P}/hauptstudie/korpus/testkorpus') if f.endswith('.pdf'))
erg = {}
for f in PDF:
    for v in FASS:
        o = f'{SP}/{v}/{f[:-4]}'
        r = subprocess.run([sys.executable, f'{P}/build_{v}/science-review-gutachten/scripts/einlesen.py',
                            f'{P}/hauptstudie/korpus/testkorpus/{f}', o, '--dpi', '20'], capture_output=True, text=True, check=True)
        fa = json.load(open(f'{o}/fassung.json', encoding='utf-8'))
        t = open(f'{o}/text.json', 'rb').read()
        tj = json.loads(t)
        erg[(f, v)] = (fa['randzeilen'], sum(1 for z in tj if z['zeile_sicher'] and z['zeile'] is not None and z['zeile'] % 5 == 0),
                       hashlib.sha256(t).hexdigest())
T = ['# Erkennung der Randzeilen je Fassung', '',
     'Jedes PDF des Testkorpus, gelesen mit `einlesen.py` der Fassungen 1.0.0 bis 1.5.0 von `science-review-gutachten`. "ja" heißt: Randzeilen erkannt, `text.json` folgt den gedruckten Randnummern; "nein" heißt: Zeilen je Seite gezählt. Bedingung A las mit 1.0.0, B und C mit 1.3.0, D mit 1.4.0; der zweite Teil zeigt, ob die Fassungen dieselbe `text.json` liefern. Gerechnet mit `tools/randzeilen_vergleich.py`.', '',
     '| Datei | ' + ' | '.join(FASS) + ' |', '|---|' + '---|' * len(FASS)]
for f in PDF:
    T.append(f'| {f} | ' + ' | '.join(('ja' if erg[(f, v)][0] else 'nein') for v in FASS) + ' |')
T += ['', '| Datei | `text.json` von 1.0.0 bis 1.4.0 gleich | `text.json` 1.5.0 gleich 1.4.0 |', '|---|---|---|']
for f in PDF:
    alt = {erg[(f, v)][2] for v in FASS[:5]}
    T.append(f'| {f} | {"ja" if len(alt) == 1 else "nein"} | {"ja" if erg[(f, "1.5.0")][2] == erg[(f, "1.4.0")][2] else "nein"} |')
out = '\n'.join(T) + '\n'
assert '—' not in out and '–' not in out
os.makedirs(f'{P}/hauptstudie/rueckschreiben', exist_ok=True)
open(f'{P}/hauptstudie/rueckschreiben/Randzeilen_Fassungen_v1_20261115.md', 'w', encoding='utf-8').write(out)
print(out)
