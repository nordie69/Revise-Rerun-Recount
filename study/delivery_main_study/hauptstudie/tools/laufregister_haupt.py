"""Erzeugt den Abschnitt "Hauptstudie" im Laufregister aus laeufe/laufplan.json und laeufe/status.json.
Zeilen werden vor dem Start angelegt (Stand geplant) und nach dem Lauf ergänzt; der Abschnitt wird jedes Mal ganz neu erzeugt."""
import json, os
HS = '/home/claude/gutachten-skill/hauptstudie'
plan = json.load(open(f'{HS}/laeufe/laufplan.json', encoding='utf-8'))
st = json.load(open(f'{HS}/laeufe/status.json', encoding='utf-8')) if os.path.exists(f'{HS}/laeufe/status.json') else {}
kopf = ('## Hauptstudie\n\nZeilen nach Studienprotokoll Abschnitt 6: vor dem Start angelegt, nach dem Lauf ergänzt; erzeugt von `tools/laufregister_haupt.py` aus `laeufe/laufplan.json` und `laeufe/status.json`. '
        'Modell: Sitzung konfiguriert für `claude-opus-5-5`, Agenten erben es; Effort "high", in jedem Agentenaufruf gesetzt. Ordner: Code im Scratchpad unter `haupt/`, Gutachten nach dem Lauf in `laeufe/ergebnis/<Code>/`.\n\n'
        '| Kennung | Datum | Bedingung | Manuskript | Wdh. | Version | Pakete SHA-256 | Aufbau | Modell | Effort | Agenten | Ordner | PDF SHA-256 | Gutachten SHA-256 | Verifikation | Gültigkeit |\n'
        '|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|\n')
zeilen = []
for r in plan:
    s = st.get(r['code'], {})
    zeilen.append(f"| {r['kennung']} | {s.get('datum','')} | {r['bedingung']} | {r['manuskript']} | {r['wdh']} | {r['fassung']} | {', '.join(r['pakete'])} | {r['aufbau']} | claude-opus-5-5 konfiguriert{(', bedient: ' + s['modell']) if s.get('modell') else ''} | high | {1 if r['aufbau']=='nacheinander' else 8} | {r['code']} | {r['pdf_sha']} | {s.get('gutachten_sha','')} | {s.get('verifikation','')} | {s.get('gueltig','geplant')} |")
p = f'{HS}/Laufregister.md'; t = open(p, encoding='utf-8').read()
i = t.index('## Hauptstudie'); j = t.find('\n## ', i + 1)
rest = t[j + 1:] if j >= 0 else ''
t = t[:i] + kopf + '\n'.join(zeilen) + '\n' + ('\n' + rest if rest else '')
open(p, 'w', encoding='utf-8').write(t)
print(len(zeilen), 'Zeilen')
