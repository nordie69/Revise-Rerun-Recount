"""7.11.E Schritt 2: Einstufung der Befundgruppen durch die KI, drei unabhängige Läufe. Je Manuskript werden die Gruppen in
Teile zu höchstens 40 Gruppen geteilt (Umfang je Agent); je Teil und Lauf ein Agent mit eigenem Ausgabeordner e<Lauf>_t<Teil>/.
Schreibt teil<t>.md (Gruppen mit Fundort, Gegenstand und Volltext ihrer Einzelbefunde) und die Aufträge EK. Gibt nur Zählungen aus."""
import json, os, re, hashlib
HS='/home/claude/gutachten-skill/hauptstudie'; SP='/tmp/claude-0/-home-claude/388bb276-2a71-5718-a623-841ee1533b2f/scratchpad'
MAX=40
SICHER=("Sicherheitsregeln: Literatur nur über WebSearch und WebFetch, Open Access zuerst; keine Netzabrufe aus der Shell (kein curl, wget, requests). Nichts veröffentlichen, keine Unteragenten, "
        "keine Memory-Werkzeuge, keine persönlichen Daten (Name, E-Mail-Adresse, Konto) in Abfragen, keine Dienste, die eine E-Mail-Adresse verlangen. "
        "Eigene Hilfsdateien ausschließlich in deinem Ausgabeordner, niemals im Scratchpad-Wurzelordner oder anderswo. Keine Gedankenstriche.")
gc=json.load(open(f'{HS}/einstufung/gruppen_codes.json')); plan={}
for M,G in gc.items():
    R=f'{SP}/einst/{G}'
    voll={}; cur=None; buf=[]
    for l in open(f'{R}/befunde_voll.md',encoding='utf-8'):
        m=re.match(r'^## (B[0-9a-f]{5}) ',l)
        if m:
            if cur: voll[cur]=''.join(buf).strip()
            cur=m.group(1); buf=[l]
        elif cur: buf.append(l)
    if cur: voll[cur]=''.join(buf).strip()
    rows=[[x.strip() for x in l.strip().strip('|').split('|')] for l in open(f'{R}/gr/gruppen.md',encoding='utf-8') if re.match(r'^\|\s*BG-\d+',l)]
    n=(len(rows)+MAX-1)//MAX; size=(len(rows)+n-1)//n; teile=[rows[i:i+size] for i in range(0,len(rows),size)]
    pdf=f'egusphere-2025-{M}.pdf'; supp=f'egusphere-2025-{M}-supplement.pdf' if M=='5046' else ''
    for t,tr in enumerate(teile,1):
        out=[f'# Befundgruppen, Teil {t} von {len(teile)}','']
        for r in tr:
            out+=[f'## {r[0]}','',f'Fundort: {r[2]}','',f'Gegenstand: {r[3]}','',f'Einzelbefunde ({len(re.findall(r"B[0-9a-f]{5}",r[1]))}):','']
            for b in re.findall(r'\bB[0-9a-f]{5}\b',r[1]): out+=[voll[b].replace('## '+b,'### '+b,1),'']
        open(f'{R}/teil{t}.md','w',encoding='utf-8').write('\n'.join(out)+'\n')
        for k in (1,2,3):
            O=f'{R}/e{k}_t{t}'; os.makedirs(O,exist_ok=True)
            a=(f"Du bist Einstufer {k} von drei unabhängigen Einstufern. Du stufst Befunde eines Gutachtens zu einem wissenschaftlichen Manuskript am Manuskript ein. Du kennst weder die Werkzeuge noch die Verfahren, mit denen die Befunde entstanden sind, und sollst nichts darüber suchen. Die Urteile der anderen Einstufer kennst du nicht.\n\n"
               f"EINGABEN (nur lesend):\n- Befundgruppen: `{R}/teil{t}.md` ({len(tr)} Gruppen; jede Gruppe fasst Einzelbefunde mit gleichem Fundort und Gegenstand zusammen)\n"
               f"- Manuskript: `{R}/{pdf}`{(' und Supplement `'+R+'/'+supp+'` (Einlesedateien in `supplement/`)') if supp else ''}, mit text.json und seiten/ im selben Ordner; Zeilennummern an den gedruckten Randnummern der Seitenbilder bestätigen, text.json kann bei Tabellen, Seitenzahlen und Seitenenden verschoben sein\n"
               "- für Aussagen über Literatur: die Quelle selbst über WebFetch und WebSearch, wo lesbar\n\n"
               f"AUSGABEORDNER: `{O}/`\n\n"
               "URTEIL je Gruppe, genau eines:\n"
               "- zutreffend: Der beanstandete Mangel besteht am Manuskript, und der Einwand ist berechtigt (eine Autorin oder ein Autor müsste darauf reagieren).\n"
               "- nicht zutreffend: Die Prämisse stimmt nicht (Fundort, Zitat, Zahl, Abbildung oder Quelle sagt es nicht so), oder der Einwand ist sachlich unbegründet.\n"
               "- Ansichtssache: Die Beobachtung stimmt, aber ob es ein Mangel ist, hängt von Vorlieben, Stil oder fachlichem Ermessen ab.\n"
               "- unklar: nicht sicher entscheidbar; Grund nennen.\n"
               "Maßgeblich ist der gemeinsame Gegenstand der Gruppe. Weichen Einzelbefunde einer Gruppe im Kern voneinander ab, urteile über den gemeinsamen Kern und vermerke die Abweichung in der Begründung. Prüfe jede Prämisse am Manuskript (Fundort, Zitat wörtlich, Zahlen mit Python, Abbildungen am Seitenbild). Schweregrad und Vorschlag beurteilst du nicht.\n\n"
               f"AUSGABE (genau zwei Dateien):\n1. `{O}/einstufung.md`, nur diese Tabelle, jede Gruppe des Teils genau einmal:\n| Gruppe | Urteil | Begründung (ein Satz mit Seite und Zeile) |\n|---|---|---|\n"
               f"2. `{O}/zugriff_EK.txt` mit jeder gelesenen und geschriebenen Datei und jeder URL.\n\n"
               f"VERBOTEN: alle anderen Dateien und Ordner, insbesondere andere Teile, die Ordner der anderen Einstufer (e1_*, e2_*, e3_* außer deinem), gr/, befunde_kurz.md, befunde_voll.md, `/home/claude/`, `/root/`, `/mnt/skills/`, andere Ordner im Scratchpad; die Verlagsseite, Diskussionsseite, Gutachten, Autorenantworten oder spätere Fassungen dieses Manuskripts (egusphere.copernicus.org und Folgezeitschrift). "+SICHER+"\n\n"
               "Deine Schlussantwort an mich enthält NUR \"Fertig\" und die Zahl der Urteile je Art. Keine Inhalte.")
            assert '—' not in a and '–' not in a and '--' not in a.replace('|---','')
            os.makedirs(f'{HS}/einstufung/auftraege/{G}',exist_ok=True)
            for p in (f'{O}/auftrag_EK.txt',f'{HS}/einstufung/auftraege/{G}/auftrag_EK{k}_t{t}.txt'): open(p,'w',encoding='utf-8').write(a)
            plan.setdefault(k,[]).append(f'{O}/auftrag_EK.txt')
    print(M,G,'Gruppen',len(rows),'Teile',len(teile),'je Teil',[len(x) for x in teile])
json.dump(plan,open(f'{HS}/einstufung/ek_plan.json','w'),indent=1)
print('Agenten je Lauf',len(plan[1]),'gesamt',sum(len(v) for v in plan.values()))
