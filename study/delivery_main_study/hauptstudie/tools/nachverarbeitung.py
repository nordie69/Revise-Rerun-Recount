"""Nachverarbeitung je Lauf (Workplan 7.11): Verifikation und Zuordnung vorbereiten.

Aufruf: python3 nachverarbeitung.py <Lauf-Code> [...]
Legt je Lauf einen neutralen Ordner im Scratchpad an (nach/<N-Code>/) mit Manuskript, Einlesedateien,
Gutachten unter dem Namen gutachten.md, der Liste der bestätigten Sollbefunde des Manuskripts und den
Aufträgen VF (Verifikation) und ZU1 bis ZU3 (Zuordnung). Der N-Code verrät weder Lauf noch Bedingung;
die Zuordnung N-Code zu Lauf steht nur in laeufe/nachverarbeitung.json. Gibt nur Zählungen aus.
"""
import hashlib, json, os, re, shutil, sys

HS = '/home/claude/gutachten-skill/hauptstudie'
SP = '/tmp/claude-0/-home-claude/388bb276-2a71-5718-a623-841ee1533b2f/scratchpad'
plan = {r['code']: r for r in json.load(open(f'{HS}/laeufe/laufplan.json', encoding='utf-8'))}
mp = f'{HS}/laeufe/nachverarbeitung.json'
zuo = json.load(open(mp, encoding='utf-8')) if os.path.exists(mp) else {}

SICHER = ("Sicherheitsregeln: Keine Netzabrufe aus der Shell (kein curl, wget, requests); Literatur nur über WebSearch und WebFetch, Open Access zuerst. "
          "Nichts veröffentlichen, keine Unteragenten, keine Memory-Werkzeuge, keine persönlichen Daten (Name, E-Mail-Adresse, Konto) in Abfragen, keine Dienste, die eine E-Mail-Adresse verlangen. Keine Gedankenstriche.")

def tabelle(p):
    return [[x.strip() for x in l.strip().strip('|').split('|')] for l in open(p, encoding='utf-8')
            if l.startswith('| ') and not re.match(r'^\|\s*(Kennung|-)', l)]

def sollliste(M, ziel):
    e = {r[0]: r for r in tabelle(f'{HS}/soll/{M}/extraktion/einwaende.md') if len(r) == 8}
    out = [f'# Bestätigte Sollbefunde egusphere-2025-{M}', '',
           'Einwände der öffentlichen Gutachten der ersten Runde, am Manuskript von drei unabhängigen Prüfern bestätigt. "teilweise" im Vermerk: nur ein Teil des Einwands trifft zu.', '',
           '| Kennung | Art | Einwand | Zitat aus dem Gutachten | Fundort | Supplement | Vermerk |', '|---|---|---|---|---|---|---|']
    n = 0
    for r in tabelle(f'{HS}/soll/{M}/sollbefunde.md'):
        if len(r) >= 7 and r[4] == 'bestätigt':
            x = e[r[0]]
            out.append(f'| {r[0]} | {x[2]} | {x[3]} | {x[4]} | {x[5]} | {x[6]} | {r[6]} |'); n += 1
    open(ziel, 'w', encoding='utf-8').write('\n'.join(out) + '\n')
    return n

def t_vf(N, R, pdf, supp):
    return ("Prüfe jeden Befund eines Gutachtens am Manuskript nach. Du hast das Gutachten nicht geschrieben und kennst seine Entstehung nicht.\n\n"
            f"Manuskript: `{R}/{pdf}`{(chr(10) + 'Supplement: `' + R + '/' + supp + '` (Einlesedateien in `supplement/`)') if supp else ''}\n"
            f"Gutachten: `{R}/gutachten.md`\n"
            "Hilfsdateien im selben Ordner (text.json, seiten/) darfst du nutzen; Zeilennummern bitte an den gedruckten Randnummern der Seitenbilder bestätigen, text.json kann bei Tabellen, Seitenzahlen und Seitenenden verschoben sein. "
            f"Eigene Hilfsdateien nur in `{R}/vf/`. Ergebnis nach `{R}/vf/verifikation.md`.\n\n"
            f"Zugriffsregeln: Lies nur die genannten Dateien und den Ordner `{R}/` ohne seine Unterordner zu1/, zu2/, zu3/ und ohne `sollbefunde.md`, dazu für Literaturbefunde Webseiten über WebFetch und WebSearch. "
            "Nicht lesen: `/home/claude/`, `/root/`, `/mnt/skills/`, andere Ordner im Scratchpad, die Verlagsseite, Diskussionsseite, Gutachten, Autorenantworten oder spätere Fassungen dieses Manuskripts (egusphere.copernicus.org und Folgezeitschrift). " + SICHER + "\n\n"
            "Auftrag:\n"
            "1. Für jeden inhaltlichen Befund (GB-nn) und jede Kleinkorrektur (KK-nn): Trifft die Prämisse am Manuskript zu? Fundort, Zitat (wörtlich vorhanden?), Zahlen (mit Python), Abbildungen am Seitenbild, Literatur an der Quelle, wo lesbar. Prüfe auch eingebettete Zitate und Angaben im Einwand, nicht nur das Feld Zitat. Urteil je Kennung: echt, teilweise echt (welcher Teil nicht), falsch, nicht prüfbar (mit Grund).\n"
            "2. Literaturvorschläge: Steht eine vorgeschlagene Arbeit bereits im Literaturverzeichnis? Je Vorschlag ja oder nein.\n"
            "3. Doppelungen: zwei Kennungen (auch Befund und Kleinkorrektur) mit gleichem Fundort und gleichem Gegenstand.\n"
            "4. Fundorte: wie viele genau, wie viele um 1 bis 2 Zeilen daneben, wie viele weiter daneben.\n\n"
            "Ausgabe als Tabelle je Kennung | Kennung | Urteil | Beleg (ein Satz mit Seite und Zeile) |, danach die Zählungen. "
            f"Schreibe jeden gelesenen und jeden geschriebenen Pfad sowie jede URL als Zeile in `{R}/vf/zugriff_VF.txt`. Antworte am Ende nur mit den Zählungen je Urteil.")

def t_zu(N, R, pdf, supp, k):
    return (f"Du bist Zuordner {k} von drei unabhängigen Zuordnern. Du kennst keine Skills, keine Gutachten-Werkzeuge und weißt nicht, wie das Gutachten entstanden ist; du sollst nichts darüber suchen. Die Urteile der anderen Zuordner kennst du nicht.\n\n"
            "AUFGABE: Stelle für jeden bestätigten Sollbefund fest, ob das Gutachten ihn trifft.\n\n"
            "EINGABEN (nur lesend):\n"
            f"- Sollbefundliste: `{R}/sollbefunde.md`\n- Gutachten: `{R}/gutachten.md`\n"
            f"- Manuskript, nur um einen Fundort nachzusehen: `{R}/{pdf}`{(' und Supplement `' + R + '/' + supp + '`') if supp else ''}, mit text.json und seiten/ im selben Ordner\n\n"
            f"AUSGABEORDNER: `{R}/zu{k}/`\n\n"
            "REGELN:\n"
            "1. Antwort je Sollbefund genau eine: getroffen (ein Befund oder eine Kleinkorrektur des Gutachtens nennt denselben Mangel an derselben Stelle oder für dieselbe Sache), teilweise (ein Befund trifft einen Teil des Sollbefunds oder nur den Gegenstand ohne den Kern), verfehlt (kein Eintrag des Gutachtens trifft ihn), unklar (nicht sicher entscheidbar; Grund nennen).\n"
            "2. Bei getroffen und teilweise nennst du die Kennung jedes treffenden Eintrags (GB-nn, KK-nn), mehrere mit Komma.\n"
            "3. Ein Eintrag des Gutachtens darf mehrere Sollbefunde treffen; mehrere Einträge dürfen denselben Sollbefund treffen.\n"
            "4. Maßgeblich ist der Inhalt, nicht der Wortlaut: Ein Eintrag trifft auch, wenn er den Mangel anders begründet oder eine andere Änderung vorschlägt, solange er denselben Mangel benennt.\n"
            "5. Du urteilst nicht, ob der Sollbefund oder der Befund zutrifft; beides ist hier nicht die Frage.\n\n"
            f"AUSGABE (genau zwei Dateien):\n1. `{R}/zu{k}/zuordnung.md`, nur diese Tabelle, jede Kennung der Sollbefundliste genau einmal:\n"
            "| Sollbefund | Antwort | Einträge des Gutachtens | Begründung (ein Satz) |\n|---|---|---|---|\n"
            f"2. `{R}/zu{k}/zugriff_ZU.txt` mit jeder gelesenen und geschriebenen Datei.\n\n"
            f"VERBOTEN: alle anderen Dateien und Ordner, insbesondere `{R}/vf/` und die Ordner der anderen Zuordner, `/home/claude/`, `/root/`, `/mnt/skills/`, andere Ordner im Scratchpad; Websuche und Webseiten (nicht nötig). " + SICHER + "\n\n"
            "Deine Schlussantwort an mich enthält NUR \"Fertig\" und die Zahl der Antworten je Art. Keine Inhalte.")

for code in sys.argv[1:]:
    r = plan[code]; M = r['manuskript']
    src = f'{SP}/haupt/{code}'
    g = f'{src}/egusphere-2025-{M}_Gutachten.md'
    assert os.path.exists(g), code
    N = zuo.get(code) or 'N' + hashlib.sha256(f'nach{code}20261018'.encode()).hexdigest()[:6]
    zuo[code] = N
    R = f'{SP}/nach/{N}'
    if os.path.exists(R):
        print(code, 'schon angelegt als', N); continue
    os.makedirs(R)
    pdf = f'egusphere-2025-{M}.pdf'; supp = f'egusphere-2025-{M}-supplement.pdf' if M == '5046' else ''
    for f in [pdf, supp, 'text.json']:
        if f: shutil.copy2(f'{src}/{f}', f'{R}/{f}')
    shutil.copytree(f'{src}/seiten', f'{R}/seiten')
    if supp and os.path.isdir(f'{src}/supplement'):
        shutil.copytree(f'{src}/supplement', f'{R}/supplement')
    shutil.copy2(g, f'{R}/gutachten.md')
    assert hashlib.sha256(open(g, 'rb').read()).digest() == hashlib.sha256(open(f'{R}/gutachten.md', 'rb').read()).digest()
    n = sollliste(M, f'{R}/sollbefunde.md')
    for sub in ('vf', 'zu1', 'zu2', 'zu3'):
        os.makedirs(f'{R}/{sub}')
    texte = {'VF': t_vf(N, R, pdf, supp), 'ZU1': t_zu(N, R, pdf, supp, 1), 'ZU2': t_zu(N, R, pdf, supp, 2), 'ZU3': t_zu(N, R, pdf, supp, 3)}
    os.makedirs(f'{HS}/laeufe/nachauftraege/{N}', exist_ok=True)
    for rolle, t in texte.items():
        assert '—' not in t and '–' not in t and '--' not in t.replace('|---', '')
        for p in (f'{R}/auftrag_{rolle}.txt', f'{HS}/laeufe/nachauftraege/{N}/auftrag_{rolle}.txt'):
            open(p, 'w', encoding='utf-8').write(t)
    print(code, '->', N, '| bestätigte Sollbefunde:', n, '| Aufträge:', len(texte))
json.dump(zuo, open(mp, 'w', encoding='utf-8'), indent=1)
