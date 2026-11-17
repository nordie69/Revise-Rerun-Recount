"""7.10: Analyse der F3-Fälle (falsche Zählung im Einwand) in B und D. Zahlen aus mehrheit.json und den Gutachten;
die Einordnung je Fall (Art, Ursache) ist Lesart des Assistenten aus dem Prüfbericht und steht in EINORD.
Schreibt rueckschreiben/Analyse_F3_v1_20261115.md."""
import json, os, re, collections, statistics, hashlib
HS = '/home/claude/gutachten-skill/hauptstudie'
K = json.load(open(f'{HS}/auswertung/k8/mehrheit.json', encoding='utf-8'))
f = lambda x, d=1: f'{x:.{d}f}'.replace('.', ',')
# (Lauf, Kennung): (Art, Ursache)
KERN, BELEG = 'Zählung ist Kern oder Teil der Aussage', 'Belegzählung oder Suchangabe als Nachweis'
EINORD = {
 ('L02','GB-21'): (KERN, 'Allaussage "most" an Abbildungswerten nicht gegengezählt'),
 ('L03','KK-26'): (BELEG, 'Elemente am Seitenbild falsch gezählt (9 statt 8 Semikolons)'),
 ('L10','GB-40'): (BELEG, 'Treffer der Suche falsch gedeutet (alle 6 Trefferzeilen als Eingabe gewertet)'),
 ('L20','GB-01'): (BELEG, 'Suche nach einer Wortform, andere Form und Teilwort übersehen ("one hit")'),
 ('L20','KK-04'): (BELEG, 'Suche nach Stämmen unvollständig, eine Form fehlt ("6 -ize forms")'),
 ('L29','GB-06'): (BELEG, 'Fehlanzeige "0 hits", Treffer über Silbentrennung am Zeilenende'),
 ('L29','GB-22'): (BELEG, 'Trefferstelle falsch angegeben ("2 hits ... p. 17, l. 533")'),
 ('L29','GB-33'): (BELEG, 'Fehlanzeige "0 hits", Treffer in Abbildungslegende außerhalb des Suchbereichs'),
 ('L34','GB-12'): (KERN, 'Abbildungselemente falsch gezählt ("two" statt drei)'),
 ('L36','GB-14'): (BELEG, 'Trefferzahl "22 occurrences", ein Treffer über Zeilenumbruch fehlt'),
 ('L48','GB-13'): (BELEG, 'Trefferzahl "1 hit", zweiter Treffer im Nachbarabsatz übersehen'),
 ('L48','GB-28'): (BELEG, 'Gesamtzahl "nine names", Namen in Bildunterschriften nicht mitgezählt'),
 ('L48','KK-02'): (BELEG, 'Trefferzahl "10 hits", ein Treffer im Fließtext übersehen'),
 ('L48','KK-28'): (BELEG, 'Elemente am Seitenbild falsch gezählt (9 statt 8 Semikolons)'),
 ('L04','GB-36'): (KERN, 'Allaussage über vier Punkte einer Abbildung, ein Punkt widerspricht'),
 ('L08','GB-36'): (KERN, 'Zahl unterscheidbarer Tracer nach eigener Regel falsch'),
 ('L26','GB-10'): (KERN, 'Zahl der Ziele mit dem Begriff falsch (drei statt zwei)'),
 ('L44','GB-51'): (KERN, 'Teilzählung einer Schreibweisenmischung falsch (3 statt 4)'),
 ('L45','GB-24'): (KERN, 'Zahl der Proben falsch, Bereich mit Nachbarzeilen vermischt (22 statt 20)'),
}
faelle = []
for L, d in sorted(K.items()):
    for k, i in d['faelle']:
        if k == 'F3' and d['bed'] in 'BD': faelle.append((d['bed'], L, d['M'], d['wdh'], i[0]))
assert len(faelle) == len(EINORD) and all((L, i) in EINORD for _, L, _, _, i in faelle)
# Trefferangaben je Gutachten (Muster "n hits", "one hit", ": 0 hits")
tr = collections.defaultdict(list)
for L, d in K.items():
    g = [x for x in os.listdir(f'{HS}/laeufe/ergebnis/{L}') if x.endswith('_Gutachten.md')][0]
    G = open(f'{HS}/laeufe/ergebnis/{L}/{g}', encoding='utf-8').read()
    tr[d['bed']].append(len(re.findall(r'\b\d+ hits?\b|\b(?:one|no|zero) hits?\b', G)))
art = collections.Counter((b, EINORD[(L, i)][0]) for b, L, _, _, i in faelle)
nD = sum(1 for x in faelle if x[0] == 'D'); nB = sum(1 for x in faelle if x[0] == 'B')
sumD = sum(tr['D'])
T = ['# Analyse der F3-Fälle in den Bedingungen B und D', '',
     'Arbeitsdokument zu Schritt 7.10. Anlass: F3 (falsche Zählung im Einwand) steigt von B nach D von 0,42 auf 1,17 Fälle je Gutachten, die Spannweiten sind getrennt. Grundlage sind die Mehrheitsfälle aus `auswertung/k8/mehrheit.json` und der Wortlaut der Prüfberichte. Die Einordnung je Fall ist Lesart des Assistenten; Zahlen gerechnet mit `tools/f3_analyse.py`.', '',
     '## Fälle nach Art', '', '| Art | B | D |', '|---|---|---|']
for a in (KERN, BELEG): T.append(f'| {a} | {art[("B", a)]} | {art[("D", a)]} |')
T += [f'| zusammen | {nB} | {nD} |', '',
      '## Mechanismus', '',
      '| Bedingung | Trefferangaben je Gutachten (Mittel) | kleinster bis größter Wert |', '|---|---|---|']
for b in 'ABCD': T.append(f'| {b} | {f(statistics.mean(tr[b]))} | {min(tr[b])} bis {max(tr[b])} |')
T += ['', f'Gezählt sind Angaben der Form "n hits", "one hit", "0 hits" im Gutachten. In D stehen {sumD} solche Angaben in 12 Gutachten; {art[("D", BELEG)]} Fälle von F3 in D gehen auf eine falsche Belegzählung oder Suchangabe zurück, also etwa {f(100*art[("D", BELEG)]/sumD)} % der Angaben. Die Regeln zu F3 (Zählbereich, Grundlage und Fundorte nennen) und F4 (Fehlanzeigen als Suche belegen) führen dazu, dass D fast jeden Einwand mit einer Suchangabe belegt. Diese Angaben sind eine neue Fehlerquelle. Fehler in Zählungen, die Kern oder Teil der Aussage sind, gehen dagegen von {art[("B", KERN)]} in B auf {art[("D", KERN)]} in D zurück.', '',
      '## Ursachen der Belegzählungen in D', '',
      '| Ursache | Fälle |', '|---|---|']
grp = collections.Counter()
for b, L, _, _, i in faelle:
    a, u = EINORD[(L, i)]
    if b == 'D' and a == BELEG:
        if 'Seitenbild' in u: grp['Elemente am Seitenbild von Hand gezählt'] += 1
        elif 'Silbentrennung' in u or 'Zeilenumbruch' in u or 'Wortform' in u or 'Stämmen' in u: grp['Suche verfehlt Wortformen, Teilwörter, Trennung oder Zeilenumbruch'] += 1
        elif 'legende' in u.lower() or 'bildunterschrift' in u.lower(): grp['Suchbereich ohne Abbildungen und Bildunterschriften'] += 1
        else: grp['Treffer übersehen, falsch verortet oder falsch gedeutet'] += 1
for k, v in grp.most_common(): T.append(f'| {k} | {v} |')
T += ['', '## Einzelfälle', '', '| Bedingung | Lauf | Manuskript | Wiederholung | Kennung | Art | Ursache |', '|---|---|---|---|---|---|---|']
for b, L, M, w, i in sorted(faelle, key=lambda x: (x[0] != 'D', x[1], x[4])):
    a, u = EINORD[(L, i)]; T.append(f'| {b} | {L} | {M} | {w} | {i} | {"Kern" if a == KERN else "Beleg"} | {u} |')
out = '\n'.join(T) + '\n'
assert '—' not in out and '–' not in out
open(f'{HS}/rueckschreiben/Analyse_F3_v1_20261115.md', 'w', encoding='utf-8').write(out)
print(out); print('SHA', hashlib.sha256(out.encode()).hexdigest()[:16])
