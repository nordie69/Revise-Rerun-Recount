"""7.8, K4 und K8: Zählaufträge je Prüfbericht. Aufruf: python3 k8_auftraege.py
Legt je Gutachten (N-Code) im Scratchpad k8/<N>/ an: verifikation.md (Prüfbericht), gutachten.md, zaehlregeln.md
(Klassen F1 bis F7 nur mit Beschreibung und Zählregel, ohne Regelwortlaut, Ziel und Fallzahlen aus dem Baumaterial)
und drei Aufträge Z1 bis Z3. Kopien der Aufträge nach auswertung/k8/auftraege/<N>/. Gibt nur Zählungen aus."""
import hashlib, json, os, re, shutil
HS = '/home/claude/gutachten-skill/hauptstudie'
SP = '/tmp/claude-0/-home-claude/388bb276-2a71-5718-a623-841ee1533b2f/scratchpad/k8'
OUT = f'{HS}/auswertung/k8'
plan = {r['code']: r for r in json.load(open(f'{HS}/laeufe/laufplan.json', encoding='utf-8'))}
nv = json.load(open(f'{HS}/laeufe/nachverarbeitung.json', encoding='utf-8'))

s = open(f'{HS}/rq3/Regelvorschlaege_RQ3.md', encoding='utf-8').read()
teil = s.split('## Fehlerklassen und Regeln')[1].split('\n## ')[0]
regeln = ['# Zählregeln K4 und F1 bis F7', '',
          'Grundlage ist allein der Prüfbericht (verifikation.md); das Gutachten (gutachten.md) wird nur gelesen, um bei F6 den Status eines Befunds und bei F7 Querverweise zwischen Kennungen festzustellen.', '',
          '## K4 Volle Doppelungen', '',
          'Gezählt wird jedes Paar oder jede Gruppe, die der Prüfbericht im Abschnitt Doppelungen als volle Doppelung führt, also gleicher Fundort und gleicher Gegenstand. Teilüberschneidungen, nahe Überschneidungen und Paare, die der Prüfer ausdrücklich nicht als Doppelung wertet, zählen hier nicht. Eine Gruppe aus drei Kennungen zählt einmal.', '']
n_kl = 0
for blk in re.split(r'\n(?=### F\d )', teil):
    m = re.match(r'### (F\d) (.+)', blk.strip())
    if not m: continue
    def feld(name):
        x = re.search(rf'^\|\s*{name}\s*\|\s*(.*?)\s*\|\s*$', blk, re.M); return x.group(1) if x else ''
    regeln += [f'## {m.group(1)} {m.group(2).strip()}', '', f'Beschreibung: {feld("Klasse")}', '', f'Zählregel: {feld("Zählregel")}', '']
    n_kl += 1
assert n_kl == 7
REGELN = '\n'.join(regeln) + '\n'
assert '—' not in REGELN and '–' not in REGELN

SICHER = ("Sicherheitsregeln: Keine Netzabrufe, keine Websuche, nichts veröffentlichen, keine Unteragenten, keine Memory-Werkzeuge. Keine Gedankenstriche. "
          "Eigene Hilfsdateien nur im eigenen Ausgabeordner. Quellen und Links nur ins Zugriffsprotokoll, nicht in die Schlussantwort.")

def auftrag(R, k):
    return (f"Du bist Zähler {k} von drei unabhängigen Zählern. Du weißt nicht, wie das Gutachten entstanden ist, und sollst nichts darüber suchen. Die Ergebnisse der anderen Zähler kennst du nicht.\n\n"
            "AUFGABE: Zähle in einem Prüfbericht die Fälle der Klassen K4 und F1 bis F7 genau nach den Zählregeln.\n\n"
            f"EINGABEN (nur lesend):\n- Zählregeln: `{R}/zaehlregeln.md`\n- Prüfbericht: `{R}/verifikation.md`\n- Gutachten, nur für F6 (Status) und F7 (Querverweise): `{R}/gutachten.md`\n\n"
            f"AUSGABEORDNER: `{R}/z{k}/`\n\n"
            "REGELN:\n1. Lies die Zählregeln vollständig, dann den ganzen Prüfbericht, auch Anmerkungen und Fußzeilen der Tabellen.\n"
            "2. Je Fall eine Zeile. Bei F1 bis F6 ist ein Fall eine Kennung (GB-nn oder KK-nn), bei K4 und F7 ein Paar oder eine Gruppe (alle Kennungen, aufsteigend, mit Komma).\n"
            "3. Eine Kennung kann in mehreren Klassen vorkommen, wenn die Zählregeln das zulassen; die Vorrangregeln in den Zählregeln (etwa F1 vor F2, F3 vor F4) gelten.\n"
            "4. Kein Fall ohne Stelle im Prüfbericht, die ihn trägt.\n\n"
            f"AUSGABE (genau zwei Dateien, dazu höchstens eigene Hilfsdateien im selben Ordner):\n1. `{R}/z{k}/zaehlung.md`, nur diese Tabelle (eine Zeile je Fall; gibt es keinen Fall, nur die Kopfzeilen):\n"
            "| Klasse | Kennungen | Stelle im Prüfbericht (kurzes Zitat) |\n|---|---|---|\n"
            f"2. `{R}/z{k}/zugriff_Z.txt` mit jeder gelesenen und geschriebenen Datei.\n\n"
            "VERBOTEN: alle anderen Dateien und Ordner, insbesondere die Ordner der anderen Zähler, `/home/claude/`, `/root/`, `/mnt/skills/`, andere Ordner im Scratchpad. " + SICHER + "\n\n"
            "Deine Schlussantwort an mich enthält NUR \"Fertig\" und die Zahl der Fälle je Klasse. Keine Inhalte, keine Quellen, keine Links.")

os.makedirs(f'{OUT}/auftraege', exist_ok=True)
open(f'{OUT}/zaehlregeln.md', 'w', encoding='utf-8').write(REGELN)
n = 0
for L in sorted(plan):
    N = nv[L]; R = f'{SP}/{N}'
    assert not os.path.exists(R), R
    os.makedirs(R)
    shutil.copy2(f'{HS}/laeufe/verifikation/{N}/verifikation.md', f'{R}/verifikation.md')
    g = [f for f in os.listdir(f'{HS}/laeufe/ergebnis/{L}') if f.endswith('_Gutachten.md')]; assert len(g) == 1
    shutil.copy2(f'{HS}/laeufe/ergebnis/{L}/{g[0]}', f'{R}/gutachten.md')
    open(f'{R}/zaehlregeln.md', 'w', encoding='utf-8').write(REGELN)
    os.makedirs(f'{OUT}/auftraege/{N}', exist_ok=True)
    for k in (1, 2, 3):
        os.makedirs(f'{R}/z{k}')
        a = auftrag(R, k); assert '—' not in a and '–' not in a and '--' not in a.replace('|---', '')
        for p in (f'{R}/auftrag_Z{k}.txt', f'{OUT}/auftraege/{N}/auftrag_Z{k}.txt'):
            open(p, 'w', encoding='utf-8').write(a)
        n += 1
print('Gutachten', len(plan), 'Aufträge', n, 'Klassen in den Zählregeln', n_kl)
