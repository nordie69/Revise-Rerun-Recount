"""Paper 3, Entscheidung 42: gleicht die Zugriffsprotokolle der Regelvorschlagsagenten R und R2 mit den acht
Dateien von Prüfdurchgang 4 ab. Schreibt freigabe_e42/Abgleich_Zugriffe_R_R2_v1_20261119.md."""
import hashlib, os, re, datetime
P = '/home/claude/gutachten-skill'
DATEIEN = ['erprobung/verifikation4/LAM_A_verifikation.md', 'erprobung/verifikation4/LAM_B_verifikation.md',
           'erprobung/verifikation4/TCD_verifikation.md', 'erprobung/verifikation4/HOR_verifikation.md',
           'erprobung/durchgang4/LAM_A/Listen_Answer_Memorize_Copernicus_Gutachten_20261016.md',
           'erprobung/durchgang4/LAM_B/Listen_Answer_Memorize_Copernicus_Gutachten_20261016.md',
           'erprobung/durchgang4/TCD/Talk_Check_Decide_A_Skill-Based_Workflow_Gutachten_20261016.md',
           'erprobung/durchgang4/HOR/egusphere-2025-2248_Gutachten_20261016.md']
LOG = {'R': f'{P}/hauptstudie/rq3/zugriff_R.txt', 'R2': f'{P}/hauptstudie/rq3/R2/zugriff_R2.txt'}
START = {'R': f'{P}/hauptstudie/rq3/auftrag_R.txt', 'R2': f'{P}/hauptstudie/rq3/R2/auftrag_R2.txt'}
iso = lambda p: datetime.datetime.utcfromtimestamp(os.stat(p).st_mtime).strftime('%Y-%m-%d %H:%M UTC')

def abschnitte(text):
    teil, aktuell = {}, None
    for l in text.split('\n'):
        w = l.strip().split(' ')[0] if l.strip() else ''
        if w and '/' not in l and w.isupper() and len(w) >= 3:
            aktuell = l.strip(); teil[aktuell] = []
        elif aktuell and l.strip():
            teil[aktuell].append(l.strip())
    return teil

T = ['# Abgleich der Zugriffsprotokolle von R und R2 mit den Dateien zu Prüfdurchgang 4', '',
     'Die Regelvorschlagsagenten R und R2 (RQ3, Fassung D) durften laut Auftrag die vier Prüfberichte und die vier Gutachten von Prüfdurchgang 4 lesen, dazu die damals installierten Skills. Abgeglichen ist, unter welcher Angabe ihr Zugriffsprotokoll jede der acht Dateien führt. Gerechnet mit `tools/abgleich_zugriffe_r.py`.', '',
     '| Datei | SHA-256 (Anfang) | zuletzt geändert | R | R2 |', '|---|---|---|---|---|']
logs = {k: open(v, encoding='utf-8').read() for k, v in LOG.items()}
for d in DATEIEN:
    zellen = []
    for k in ('R', 'R2'):
        ab = abschnitte(logs[k]); wo = [s for s, ls in ab.items() if any(d in l for l in ls)]
        zellen.append(', '.join(w.lower() for w in wo) if wo else 'nicht genannt')
    sha = hashlib.sha256(open(f'{P}/{d}', 'rb').read()).hexdigest()[:16]
    T.append(f'| `{d}` | {sha} | {iso(f"{P}/{d}")} | {zellen[0]} | {zellen[1]} |')
T += ['', 'Beide lasen die Prüfberichte ganz und die Gutachten in Teilen: R führt die Gutachten unter "nur Ausschnitte", R2 unter "Inhalt" mit den gelesenen Teilen in Klammern (Überschriften und einzelne Befundblöcke). Jede der acht Dateien wurde zuletzt vor dem Start von R geändert; Prüfsummen vom Zeitpunkt des Lesens sind nicht festgehalten.', '']
T += ['', '| Agent | Auftrag geschrieben | Protokoll zuletzt geschrieben |', '|---|---|---|']
T += [f'| {k} | {iso(START[k])} | {iso(LOG[k])} |' for k in ('R', 'R2')]
T += ['', 'Weitere Zeilen der Protokolle mit Pfaden unter dem Projektordner, außer den acht Dateien und dem eigenen Ausgabeordner unter `hauptstudie/rq3/` (Abschnitt in Klammern):', '']
for k in ('R', 'R2'):
    rest = []
    for sec, ls in abschnitte(logs[k]).items():
        if sec.startswith('NICHT'):
            continue
        for l in ls:
            if P in l and not any(d in l for d in DATEIEN) and '/hauptstudie/rq3/' not in l:
                rest.append(f'{l} ({sec.lower()})')
    T.append(f'- {k}: ' + ('; '.join(f'`{x}`' for x in rest) if rest else 'keine'))
T += ['', 'Zeilen mit Pfaden außerhalb des Projektordners (Abschnitt in Klammern):', '']
for k in ('R', 'R2'):
    rest = [f'{l} ({sec.lower()})' for sec, ls in abschnitte(logs[k]).items() if not sec.startswith('NICHT')
            for l in ls if re.search(r'/(mnt|root|tmp)/', l)]
    T.append(f'- {k}: ' + '; '.join(f'`{x}`' for x in rest))
out = '\n'.join(T) + '\n'
assert '—' not in out and '–' not in out
open(f'{P}/hauptstudie/freigabe_e42/Abgleich_Zugriffe_R_R2_v1_20261119.md', 'w', encoding='utf-8').write(out)
print(out)
