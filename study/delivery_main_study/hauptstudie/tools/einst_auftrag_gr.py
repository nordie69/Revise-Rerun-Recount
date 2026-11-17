"""7.11.E Schritt 1: Auftrag GR (Befundgruppen) je Manuskript schreiben, in den Ordner und nach einstufung/auftraege/<G>/."""
import json, os, hashlib
HS='/home/claude/gutachten-skill/hauptstudie'; SP='/tmp/claude-0/-home-claude/388bb276-2a71-5718-a623-841ee1533b2f/scratchpad'
SICHER=("Sicherheitsregeln: Keine Websuche, keine Webseiten, keine Netzabrufe aus der Shell. Nichts veröffentlichen, keine Unteragenten, keine Memory-Werkzeuge, "
        "keine persönlichen Daten in Abfragen. Eigene Hilfsdateien ausschließlich im Ordner gr/, niemals im Scratchpad oder anderswo. Keine Gedankenstriche.")
for M,G in json.load(open(f'{HS}/einstufung/gruppen_codes.json')).items():
    R=f'{SP}/einst/{G}'; pdf=f'egusphere-2025-{M}.pdf'
    t=(f"Du fasst strittige Einzelbefunde zu einem wissenschaftlichen Manuskript zu Befundgruppen zusammen. Du kennst weder die Werkzeuge noch die Verfahren, mit denen die Befunde entstanden sind, und sollst nichts darüber suchen.\n\n"
       f"EINGABEN (nur lesend):\n- Kurzliste aller Einzelbefunde: `{R}/befunde_kurz.md` (Kennung, Art, Fundort, Kurzfassung)\n- Volltext aller Einzelbefunde: `{R}/befunde_voll.md` (für Zweifelsfälle)\n"
       f"- Manuskript, nur um einen Fundort nachzusehen: `{R}/{pdf}` mit text.json und seiten/ im selben Ordner\n\nAUSGABEORDNER: `{R}/gr/`\n\n"
       "REGELN:\n1. Eine Befundgruppe umfasst Einzelbefunde mit gleichem Fundort und gleichem Gegenstand, also denselben Mangel an derselben Stelle oder für dieselbe Sache, auch wenn Wortlaut, Begründung, Vorschlag oder Schweregrad verschieden sind. Befunde und Kleinkorrekturen dürfen in einer Gruppe stehen, wenn sie dasselbe beanstanden.\n"
       "2. Jeder Einzelbefund gehört zu genau einer Gruppe. Ein Befund ohne Gegenstück bildet eine eigene Gruppe.\n"
       "3. Verschiedene Mängel an derselben Stelle sind verschiedene Gruppen; derselbe Mangel an mehreren Stellen ist eine Gruppe nur, wenn die Befunde dieselben Stellen nennen.\n"
       "4. Du urteilst nicht, ob ein Befund zutrifft; das ist hier nicht die Frage.\n\n"
       f"AUSGABE (genau zwei Dateien):\n1. `{R}/gr/gruppen.md`, nur diese Tabelle, jede Kennung der Kurzliste genau einmal:\n| Gruppe | Einzelbefunde | Fundort | Gegenstand (ein Satz) |\n|---|---|---|---|\n"
       "Gruppen heißen BG-001, BG-002 usw. in der Reihenfolge der Fundorte; Einzelbefunde mit Komma getrennt.\n"
       f"2. `{R}/gr/zugriff_GR.txt` mit jeder gelesenen und geschriebenen Datei.\n\nPrüfe am Ende mit Python, dass jede Kennung der Kurzliste genau einmal in gruppen.md steht (Hilfsdateien nur in gr/).\n\n"
       f"VERBOTEN: alle anderen Dateien und Ordner, `/home/claude/`, `/root/`, `/mnt/skills/`, andere Ordner im Scratchpad. "+SICHER+"\n\n"
       "Deine Schlussantwort an mich enthält NUR \"Fertig\", die Zahl der Einzelbefunde und die Zahl der Gruppen. Keine Inhalte.")
    assert '—' not in t and '–' not in t and '--' not in t.replace('|---','')
    os.makedirs(f'{HS}/einstufung/auftraege/{G}',exist_ok=True)
    for p in (f'{R}/auftrag_GR.txt',f'{HS}/einstufung/auftraege/{G}/auftrag_GR.txt'): open(p,'w',encoding='utf-8').write(t)
    print(G, hashlib.sha256(t.encode()).hexdigest()[:16])
