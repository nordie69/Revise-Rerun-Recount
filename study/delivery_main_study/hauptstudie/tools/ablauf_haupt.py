"""Erzeugt laeufe/Ablauf_Hauptstudie.md: Ablauf, Pakete und Stand je Lauf (aus laufplan.json und status.json).
Nach jedem geprüften Lauf neu erzeugen."""
import json, os
HS = '/home/claude/gutachten-skill/hauptstudie'
plan = json.load(open(f'{HS}/laeufe/laufplan.json', encoding='utf-8'))
st = json.load(open(f'{HS}/laeufe/status.json', encoding='utf-8')) if os.path.exists(f'{HS}/laeufe/status.json') else {}
pakete = []
for w in (1, 2, 3):
    codes = [r['code'] for r in plan if r['welle'] == w]
    for i in range(0, len(codes), 3):
        pakete.append((w, len(pakete) + 1, codes[i:i + 3]))
pk = {c: n for w, n, cs in pakete for c in cs}
fertig = sum(1 for r in plan if str(st.get(r['code'], {}).get('gueltig','')).startswith('gültig'))
offen = [r['code'] for r in plan if not str(st.get(r['code'], {}).get('gueltig','')).startswith('gültig')]
z = ['# Ablauf der Hauptstudie (Workplan-Schritt 7.7)', '',
 'Arbeitsdokument. Hält fest, wie die 48 Läufe gefahren werden und wo jeder Lauf steht, damit die Arbeit nach jeder Unterbrechung an derselben Stelle weitergeht. Erzeugt von `tools/ablauf_haupt.py`; maßgeblich bleiben Studienprotokoll (DAT-54), Laufplan (`laeufe/laufplan.md`) und Laufregister (DAT-30).', '',
 f'Stand: {fertig} von 48 Läufen gültig. Nächster offener Lauf: {offen[0] if offen else "keiner"} (Paket {pk[offen[0]] if offen else "-"}).', '',
 '## Dateien', '',
 '| Datei | Zweck |', '|---|---|',
 '| `laeufe/laufplan.md`, `laufplan.json` | 48 Läufe, Code, Kennung, Welle, Bedingung, Manuskript, Fassung, Prüfsummen |',
 '| `laeufe/auftraege/<Code>/auftrag_<Rolle>.txt`, `auftraege_SHA256.txt` | gesicherte Aufträge je Rolle, schreibgeschützt |',
 '| Scratchpad `haupt/<Code>/` | Laufordner: Manuskript, Skills der Fassung, Auftragskopien, Ergebnisse der Agenten |',
 '| `laeufe/status.json` | Datum, Gutachten-SHA, Gültigkeit je Lauf, geschrieben von `tools/pruefe_lauf.py` |',
 '| `laeufe/ergebnis/<Code>/` | Gutachten nach der Prüfung, schreibgeschützt |',
 '| `Laufregister.md`, Abschnitt Hauptstudie | 48 Zeilen, erzeugt von `tools/laufregister_haupt.py` |', '',
 '## Ablauf je Lauf', '',
 '1. Getrennter Aufbau (A, B, D): Vorbereiter VB, nach dessen Ende die sechs Instanzen S1 bis S4, AB, SD gleichzeitig, nach deren Ende der Zusammenführer ZF. Nacheinander (C): ein Agent C.',
 '2. Aufruf jedes Agenten, Effort "high", Typ general-purpose: "Dein Auftrag steht wörtlich in der Datei `<Laufordner>/auftrag_<Rolle>.txt`. Lies diese Datei zuerst vollständig und führe den Auftrag genau so aus. Lies keine anderen Dateien als die dort erlaubten. Deine Schlussantwort an mich enthält nur Zahlen, keine Befunde, Titel oder Inhalte des Manuskripts." (Satz ab L02 ergänzt, SB-55)',
 '3. Nach dem Lauf: `python3 tools/pruefe_lauf.py <Code>` (Gutachten vorhanden, Formatprüfung 0 Fehler, Zugriffe nur im Laufordner), dann `tools/laufregister_haupt.py` und `tools/ablauf_haupt.py`. Meldet die Prüfung "prüfen", sieht der Assistent die genannten Zeilen der Zugriffsdatei an (nicht das Gutachten) und entscheidet nach Regel 5 des Protokolls, ob der Lauf ungültig ist.',
 '4. Ungültig: Grund ins Register, Lauf nach 7.7.5 neu fahren (höchstens zwei Wiederholungen). Abbruch durch ein Limit: Agent mit derselben Kennung fortsetzen, sonst neu.',
 '5. Der Assistent liest keine Gutachten und Instanzdateien vor der Auswertung; gemeldet werden nur Zahlen.', '',
 '## Pakete', '',
 'Ein Paket sind bis zu drei aufeinanderfolgende Läufe einer Welle; so laufen höchstens 18 Instanzen und 2 weitere Agenten gleichzeitig (Grenze 20).', '',
 '| Paket | Welle | Läufe |', '|---|---|---|']
for w, n, cs in pakete:
    z.append(f'| {n} | {w} | {", ".join(cs)} |')
z += ['', '## Stand je Lauf', '', '| Code | Kennung | Welle | Paket | Datum | Gutachten SHA-256 | Gültigkeit |', '|---|---|---|---|---|---|---|']
for r in plan:
    s = st.get(r['code'], {})
    z.append(f"| {r['code']} | {r['kennung']} | {r['welle']} | {pk[r['code']]} | {s.get('datum', '')} | {s.get('gutachten_sha', '')} | {s.get('gueltig', 'geplant')} |")
open(f'{HS}/laeufe/Ablauf_Hauptstudie.md', 'w', encoding='utf-8').write('\n'.join(z) + '\n')
print('Ablauf geschrieben;', fertig, 'gültig; nächster', offen[0] if offen else '-')
