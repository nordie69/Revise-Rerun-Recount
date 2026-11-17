"""7.V Nachzählung der Vorstudie: Zuordnung der 15 Gutachten V1 bis V4 zu den neu bestätigten Sollbefunden.

Aufruf: python3 vorstudie_zuordnung.py
Legt je Gutachten einen neutralen Ordner im Scratchpad an (vor/<V-Code>/) mit Manuskript, Einlesedateien,
Gutachten unter dem Namen gutachten.md (Skillnamen und Versionsnummern neutralisiert), der Liste der bestätigten
Sollbefunde des Falls und den Aufträgen ZU1 bis ZU3. Der V-Code verrät weder Durchgang noch Lauf; die Zuordnung
V-Code zu Lauf steht nur in vorstudie/plan.json. Gibt nur Zählungen aus.
"""
import hashlib, json, os, re, shutil

ROOT = '/home/claude/gutachten-skill'
HS = f'{ROOT}/hauptstudie'
SP = '/tmp/claude-0/-home-claude/388bb276-2a71-5718-a623-841ee1533b2f/scratchpad'
OUT = f'{HS}/vorstudie'
LAEUFE = [  # Laufregister-Kennung, Ordner, Fall
    ('V1-LAM-1', 'durchgang1/LAM1', 'LAM'), ('V1-LAM-2', 'durchgang1/LAM2', 'LAM'), ('V1-TCD-1', 'durchgang1/TCD', 'TCD'), ('V1-HOR-1', 'durchgang1/HOR', 'HOR'),
    ('V2-LAM-1', 'durchgang2/LAM', 'LAM'), ('V2-TCD-1', 'durchgang2/TCD', 'TCD'), ('V2-HOR-1', 'durchgang2/HOR', 'HOR'),
    ('V3-LAM-1', 'durchgang3/LAM_A', 'LAM'), ('V3-LAM-2', 'durchgang3/LAM_B', 'LAM'), ('V3-TCD-1', 'durchgang3/TCD', 'TCD'), ('V3-HOR-1', 'durchgang3/HOR', 'HOR'),
    ('V4-LAM-1', 'durchgang4/LAM_A', 'LAM'), ('V4-LAM-2', 'durchgang4/LAM_B', 'LAM'), ('V4-TCD-1', 'durchgang4/TCD', 'TCD'), ('V4-HOR-1', 'durchgang4/HOR', 'HOR')]

SICHER = ("Sicherheitsregeln: Keine Netzabrufe aus der Shell (kein curl, wget, requests). Nichts veröffentlichen, keine Unteragenten, keine Memory-Werkzeuge, "
          "keine persönlichen Daten (Name, E-Mail-Adresse, Konto) in Abfragen, keine Dienste, die eine E-Mail-Adresse verlangen. Keine Gedankenstriche. "
          "Eigene Hilfsdateien (Skripte, Notizen, Zwischenstände) nur im eigenen Ausgabeordner, nie im Scratchpad-Ordner oder in einem anderen Ordner. "
          "Quellen und Links nur ins Zugriffsprotokoll, nicht in die Schlussantwort.")

def tabelle(p):
    return [[x.strip() for x in l.strip().strip('|').split('|')] for l in open(p, encoding='utf-8')
            if l.startswith('| ') and not re.match(r'^\|\s*(Kennung|-)', l)]

def sollliste(F, ziel):
    e = {r[0]: r for r in tabelle(f'{HS}/soll_vorstudie/{F}/extraktion/einwaende.md') if len(r) == 8}
    out = ['# Bestätigte Sollbefunde des Manuskripts', '',
           'Einwände der öffentlichen Gutachten, am Manuskript von drei unabhängigen Prüfern bestätigt. "teilweise" im Vermerk: nur ein Teil des Einwands trifft zu.', '',
           '| Kennung | Art | Einwand | Zitat aus dem Gutachten | Fundort | Supplement | Vermerk |', '|---|---|---|---|---|---|---|']
    n = 0
    for r in tabelle(f'{HS}/soll_vorstudie/{F}/sollbefunde.md'):
        if len(r) >= 7 and r[4] == 'bestätigt':
            x = e[r[0]]
            out.append(f'| {r[0]} | {x[2]} | {x[3]} | {x[4]} | {x[5]} | {x[6]} | {r[6]} |'); n += 1
    open(ziel, 'w', encoding='utf-8').write('\n'.join(out) + '\n')
    return n

NEUTRAL = re.compile(r'science-review-[a-z]+(?:\s+(?:v|Version\s+|Fassung\s+)?\d+\.\d+\.\d+)?', re.I)

def t_zu(R, pdf, k):
    return (f"Du bist Zuordner {k} von drei unabhängigen Zuordnern. Du kennst keine Skills, keine Gutachten-Werkzeuge und weißt nicht, wie das Gutachten entstanden ist; du sollst nichts darüber suchen. Die Urteile der anderen Zuordner kennst du nicht.\n\n"
            "AUFGABE: Stelle für jeden bestätigten Sollbefund fest, ob das Gutachten ihn trifft.\n\n"
            "EINGABEN (nur lesend):\n"
            f"- Sollbefundliste: `{R}/sollbefunde.md`\n- Gutachten: `{R}/gutachten.md`\n"
            f"- Manuskript, nur um einen Fundort nachzusehen: `{R}/{pdf}`, mit text.json und seiten/ im selben Ordner\n\n"
            f"AUSGABEORDNER: `{R}/zu{k}/`\n\n"
            "REGELN:\n"
            "1. Antwort je Sollbefund genau eine: getroffen (ein Befund oder eine Kleinkorrektur des Gutachtens nennt denselben Mangel an derselben Stelle oder für dieselbe Sache), teilweise (ein Befund trifft einen Teil des Sollbefunds oder nur den Gegenstand ohne den Kern), verfehlt (kein Eintrag des Gutachtens trifft ihn), unklar (nicht sicher entscheidbar; Grund nennen).\n"
            "2. Bei getroffen und teilweise nennst du die Kennung jedes treffenden Eintrags (GB-nn, KK-nn), mehrere mit Komma.\n"
            "3. Ein Eintrag des Gutachtens darf mehrere Sollbefunde treffen; mehrere Einträge dürfen denselben Sollbefund treffen.\n"
            "4. Maßgeblich ist der Inhalt, nicht der Wortlaut: Ein Eintrag trifft auch, wenn er den Mangel anders begründet oder eine andere Änderung vorschlägt, solange er denselben Mangel benennt.\n"
            "5. Du urteilst nicht, ob der Sollbefund oder der Befund zutrifft; beides ist hier nicht die Frage.\n\n"
            f"AUSGABE (genau zwei Dateien, dazu höchstens eigene Hilfsdateien im selben Ordner):\n1. `{R}/zu{k}/zuordnung.md`, nur diese Tabelle, jede Kennung der Sollbefundliste genau einmal:\n"
            "| Sollbefund | Antwort | Einträge des Gutachtens | Begründung (ein Satz) |\n|---|---|---|---|\n"
            f"2. `{R}/zu{k}/zugriff_ZU.txt` mit jeder gelesenen und geschriebenen Datei.\n\n"
            f"VERBOTEN: alle anderen Dateien und Ordner, insbesondere die Ordner der anderen Zuordner, `/home/claude/`, `/root/`, `/mnt/skills/`, andere Ordner im Scratchpad; Websuche und Webseiten (nicht nötig). " + SICHER + "\n\n"
            "Deine Schlussantwort an mich enthält NUR \"Fertig\" und die Zahl der Antworten je Art. Keine Inhalte, keine Quellen, keine Links.")

os.makedirs(f'{OUT}/auftraege', exist_ok=True)
plan = {}; ersetzt_ges = 0
for lauf, ordner, F in LAEUFE:
    src = f'{ROOT}/erprobung/{ordner}'
    g = [f for f in os.listdir(src) if '_Gutachten_' in f and f.endswith('.md')]; assert len(g) == 1, src
    pdf = [f for f in os.listdir(src) if f.endswith('.pdf')]; assert len(pdf) == 1, src
    V = 'V' + hashlib.sha256(f'vor{lauf}20261115'.encode()).hexdigest()[:6]
    plan[V] = {'lauf': lauf, 'ordner': f'erprobung/{ordner}', 'fall': F, 'gutachten': g[0],
               'sha256_gutachten': hashlib.sha256(open(f'{src}/{g[0]}', 'rb').read()).hexdigest()}
    R = f'{SP}/vor/{V}'
    assert not os.path.exists(R), R
    os.makedirs(R)
    shutil.copy2(f'{src}/{pdf[0]}', f'{R}/{pdf[0]}'); shutil.copy2(f'{src}/text.json', f'{R}/text.json')
    shutil.copytree(f'{src}/seiten', f'{R}/seiten')
    t, n_ers = NEUTRAL.subn('[Werkzeug]', open(f'{src}/{g[0]}', encoding='utf-8').read())
    ersetzt_ges += n_ers; plan[V]['neutralisiert'] = n_ers
    open(f'{R}/gutachten.md', 'w', encoding='utf-8').write(t)
    n = sollliste(F, f'{R}/sollbefunde.md'); plan[V]['sollbefunde'] = n
    os.makedirs(f'{OUT}/auftraege/{V}', exist_ok=True)
    for k in (1, 2, 3):
        os.makedirs(f'{R}/zu{k}')
        a = t_zu(R, pdf[0], k)
        assert '—' not in a and '–' not in a and '--' not in a.replace('|---', '')
        for p in (f'{R}/auftrag_ZU{k}.txt', f'{OUT}/auftraege/{V}/auftrag_ZU{k}.txt'):
            open(p, 'w', encoding='utf-8').write(a)
    print(V, F, 'Sollbefunde', n, 'neutralisiert', n_ers)
json.dump(plan, open(f'{OUT}/plan.json', 'w', encoding='utf-8'), indent=1)
print('Gutachten', len(plan), 'Codes verschieden', len(set(plan)), 'Neutralisierungen gesamt', ersetzt_ges)
