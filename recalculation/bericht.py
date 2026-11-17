#!/usr/bin/env python3
"""Erzeugt Nachrechnung_6-1_Bericht.md aus ergebnis.json, pruefungen.json und vergleich.json."""
import json, os, re, hashlib, collections

OUT = os.path.dirname(os.path.abspath(__file__))
E = json.load(open(os.path.join(OUT, 'ergebnis.json')))
K, JG = E['kennzahlen'], E['je_gutachten']
C = json.load(open(os.path.join(OUT, 'pruefungen.json')))
V = json.load(open(os.path.join(OUT, 'vergleich.json')))
BED = 'ABCD'


def f(x, n=2):
    if x is None:
        return 'nicht vorhanden'
    if isinstance(x, (int,)) or (isinstance(x, float) and x == int(x) and n == 0):
        return str(int(x))
    return f'{x:.{n}f}'.replace('.', ',')


def pp(x, n=1):
    return f(100 * x, n)


L = []
w = L.append
w('# Nachrechnung der Kennzahlen der Hauptstudie (Workplan Paper 3, Schritt 6.1)')
w('')
w('Unabhängige Nachrechnung aller Kennzahlen aus den Rohdaten der Lieferung `lieferung_hauptstudie_20261115` nach den Definitionen des Studienprotokolls (Fassung mit drei Nachträgen, SHA-256 93d2e122...f859, gleich der Prüfsummendatei). Die Skripte unter `hauptstudie/tools/` wurden weder benutzt noch gelesen; die Quellen wurden nur gelesen. Je Bedingung Mittelwert und Spannweite über die drei Wiederholungen, je Wiederholung die vier Manuskripte gepoolt (Summe der Treffer durch Summe der Sollbefunde; Zählgrößen als Mittel je Gutachten). Ein Wert gilt als gleich, wenn er um höchstens 0,05 Prozentpunkte beziehungsweise 0,05 Fälle je Gutachten vom gelieferten Wert abweicht (die Lieferung rundet auf 0,1 Prozentpunkte beziehungsweise 0,01 Fälle).')
w('')

# ------------------------------------------------------------ Ergebnis in Zahlen
H = V
w('## 1. Ergebnis in Zahlen')
w('')
w('| Messgröße | Wert |')
w('|---|---|')
w(f"| verglichene Werte der Trefferbilanz (ohne Doppelzählung) | {H['zahl']} |")
w(f"| davon gleich | {H['gleich']} |")
w(f"| davon abweichend (> 0,05) | {len(H['abweichungen'])} |")
w(f"| abweichende Werte, die mit der Definition der Lieferung exakt reproduziert werden | {sum(1 for x in H['abweichungen'] if x['kennzahl'].startswith(('K5', 'K7')))} |")
w(f"| abweichende Werte mit belegbarem Fehler in der Lieferung | {sum(1 for x in H['abweichungen'] if x['kennzahl'].startswith('K9'))} (K9) |")
w(f"| Werte je Gutachten aus `kennzahlen_je_gutachten.json` verglichen, davon abweichend | {H['je_gutachten']['werte']}, {H['je_gutachten']['abweichend']} |")
w(f"| K4 und F1 bis F7 je Gutachten aus `k8/mehrheit.json` verglichen, davon abweichend | {H['k8_mehrheit_je_gutachten']['werte']}, {H['k8_mehrheit_je_gutachten']['abweichend']} |")
w(f"| Zellen von `kennzahlen_teil1.md` und `kennzahlen_k4_k8.md` gleich der Trefferbilanz | {H['kennzahlen_dateien_gleich_trefferbilanz']['gleich']} von {H['kennzahlen_dateien_gleich_trefferbilanz']['zellen']} |")
w(f"| Urteile der Effektregel (RQ1 bis RQ3, mit und ohne G03) gleich | {sum(x['gleich'] for x in H['effektregel_urteile'])} von {len(H['effektregel_urteile'])} |")
w(f"| Übereinstimmung der Stichprobe (K7, Schwelle 80 %) | {C['stichprobe_ziehung']['tsv_teil1']} Einzelbefunde, {pp(C['schwelle']['anteil'])} %, Schwelle erreicht |")
w('')

# ------------------------------------------------------------ Pruefung der Zwischendateien
w('## 2. Prüfung der Eingaben und Mehrheiten')
w('')
lp = C['laufplan']
zm = C['zuordnung_mehrheit_gegen_mehrheit_md']
ki = C['ki_mehrheit']
w('| Prüfung | Ergebnis |')
w('|---|---|')
w(f"| Laufplan: Läufe, je Bedingung und Manuskript Wiederholungen 1 bis 3 | {lp['zahl']} Läufe, alle 16 Zellen mit 1, 2, 3; keine Kennung doppelt, keine Nachverarbeitungskennung doppelt |")
w(f"| Fassungen und Pakete je Bedingung | je Bedingung genau eine Kombination, gleich Protokoll Abschnitt 2 und 4 (A 1.0.0, B und C 1.3.0/1.2.0/1.2.0, D 1.4.0/1.3.0/1.2.0; Paketprüfsummen gleich den ersten 12 Stellen im Protokoll) |")
w(f"| Sollbefunde | {C['soll']['einwaende']} Einwände, {C['soll']['bestaetigt']} bestätigt ({C['soll']['inhaltlich']} inhaltlich, {C['soll']['kleinkorrektur']} Kleinkorrekturen), {C['soll']['nicht_bestaetigt']} nicht bestätigt, {C['soll']['auftraggeber']} vom Auftraggeber entschieden; G03: {C['soll']['G03_bestaetigt']} bestätigte Sollbefunde; Mehrheit der drei Prüfer aus `mehrheit.md` für alle Kennungen nachvollzogen, {len(C['soll_mehrheit_abweichungen'])} Abweichungen |")
w(f"| Einzelbefunde gegen Gutachtendateien | {C['einzelbefunde_gegen_gutachten']['zahl']} Einzelbefunde, Kennungen GB und KK in allen 48 Gutachten gleich ({len(C['einzelbefunde_gegen_gutachten']['ungleich'])} Abweichungen); Feld Source in allen erkannt, {C['source_ohne_instanz'][0][1] if C['source_ohne_instanz'] else 0} Einträge nennen nur ZF |")
w(f"| Zuordnungsmehrheit aus den drei Zuordnungsläufen (alle 48 Gutachten, alle Sollbefunde, 7128 Einzelantworten) | Mehrheitsantwort in jeder Zeile gleich `mehrheit.md`; keine Zeile ohne Mehrheit, kein \"unklar\". In {zm['zahl']} Zeilen listet `mehrheit.md` unter \"Einträge mit Mehrheit\" zusätzlich einen Eintrag, den nur ein Lauf als getroffen und ein zweiter als teilweise nennt (L01 4695-RC1-07 GB-14, L18 4733-RC1-13 GB-22, L45 5046-RC2-03 GB-39); ohne Folge, weil diese Einträge über andere Sollbefunde ohnehin zutreffend sind |")
w(f"| zutreffend nach Zuordnung (von mindestens 2 Läufen für denselben Sollbefund als getroffen genannt) | {C['zutreffend_nach_zuordnung']['zahl']} Einzelbefunde; strittig {C['zutreffend_nach_zuordnung']['strittig_eigen']}, gleich der Kennzeichnung in `einzelbefunde.json` ({len(C['zutreffend_nach_zuordnung']['differenz'])} Unterschiede) |")
w(f"| Befundgruppen | {C['gruppen']['zahl']} Gruppen, {C['gruppen']['einzelbefunde_in_gruppen']} Einzelbefunde je genau einmal, jede Zufallskennung auf einen strittigen Befund des richtigen Manuskripts |")
w(f"| KI-Mehrheit aus den drei Einstufungsläufen (alle 896 Gruppen) | gleich `mehrheit.json` in Urteilen und Mehrheit ({len(ki['abweichungen_gegen_mehrheit_json'])} Abweichungen); {ki['ohne_mehrheit']} ohne Mehrheit, {ki['mehrheit_unklar']} mit Mehrheit \"unklar\" |")
sz = C['stichprobe_ziehung']
w(f"| Ziehung der Stichprobe | mit `random.Random(202610221)`, je Bedingung `sample(sortierte Kennungen, 15)` aus einem Generator nachgezogen: gleich `gezogen.json` ({'ja' if sz['nachgezogen_ein_generator'] else 'nein'}); 15 je Bedingung; alle aus Gruppen mit Mehrheit zutreffend, nicht zutreffend oder Ansichtssache; Teil 2 der Erfassung gleich den 6 Gruppen ohne Mehrheit oder mit \"unklar\" |")
eg = C['endgueltig_gegenprobe']
w(f"| endgültige Urteile (KI-Mehrheit, Auftraggeber für 6 Gruppen, Abweichungen der Stichprobe für die ganze Gruppe) | eigene Ableitung gleich `endgueltig_einzelbefunde.json` ({eg['einzelbefunde_abweichend']} Abweichungen bei 4418) und `endgueltig_gruppen.json` ({eg['gruppen_abweichend']} bei 896) |")
w(f"| K8-Mehrheit (Fall zählt, wenn mindestens 2 von 3 Zählern ihn nennen) | gleich `k8/mehrheit.json` in allen 384 Werten; der Median der drei Zählungen je Klasse ergäbe nur in L33 (A, 4506, Lauf 3) einen Fall weniger (8 statt 9; A Lauf 3: 6,50 statt 6,75 je Gutachten) |")
w(f"| K4 aus der Schlusszeile des Prüfberichts | in {C['k4_schlusszeile']['lesbar']} Prüfberichten maschinell lesbar, dort gleich der Zählermehrheit |")
w('')

# ------------------------------------------------------------ Tabellen je Kennzahl
w('## 3. Tabellen je Kennzahl')
w('')
w('Spalten: nachgerechnet, geliefert (Trefferbilanz), gleich. Anteile in Prozent, Zählgrößen in Fällen je Gutachten.')
w('')
w('Festlegungen, wo das Protokoll eine Zählung nicht ausschreibt: Ein Sollbefund ist getroffen oder teilweise, wenn mindestens zwei der drei Zuordnungsläufe das sagen. Ein Befund ist zutreffend nach Zuordnung, wenn mindestens zwei Läufe ihn für denselben Sollbefund als getroffen nennen; alle übrigen sind strittig und übernehmen das Urteil ihrer Gruppe. K2 und K6 beziehen sich auf alle Einträge (Befunde und Kleinkorrekturen) mit endgültigem Urteil. K3: Befund ohne Sollbefund heißt, kein Sollbefund mit Mehrheit getroffen oder teilweise, für den mindestens zwei Läufe diesen Befund nennen (Variante b; Variante a steht unten). Ohne G03 entfallen die Sollbefunde 4506-RC3-nn aus Zähler, Nenner und Zuordnung; die Einstufung der Befunde bleibt. K6 zählt Einträge, deren Feld Source genau eine der Instanzen S1 bis S4, AB, SD nennt; Einträge nur mit ZF stehen im Nenner. K4 und K8: Fall zählt, wenn mindestens zwei der drei Zähler ihn nennen. Zählgrößen je Lauf als Mittel über die vier Gutachten.')
w('')
grp = collections.OrderedDict()
for x in H['vergleiche']:
    if x['variante']:
        continue
    name = x['kennzahl']
    g = re.sub(r', (Mittel|min|max)$', '', name)
    g2 = re.sub(r', ([ABCD])$', '', g)
    teil = name[len(g2):].lstrip(', ')
    grp.setdefault(g2, []).append((teil or '', x))
def txt(x):
    n = 1 if x['einheit'] == 'pp' else 2
    ge, ei = x['geliefert'], x['eigen']
    ganz = abs(ei - round(ei)) < 1e-9 and float(ge) == int(ge)
    gtxt = str(int(ge)) if ganz else f(ge, n)
    etxt = str(int(round(ei))) if ganz else f(ei, 2 if x['einheit'] == 'pp' else 3)
    return etxt, gtxt


einzel = []
for g, rows in grp.items():
    if len(rows) == 1:
        einzel.append((g, rows[0][1]))
        continue
    w(f'### {g}')
    w('')
    w('| Bedingung, Größe | nachgerechnet | geliefert | gleich |')
    w('|---|---|---|---|')
    for teil, x in rows:
        e_, g_ = txt(x)
        w(f"| {teil} | {e_} | {g_} | {'ja' if x['gleich'] else 'nein'} |")
    w('')
w('### Einzelwerte (K5 Schweregrade, K7, K8 Zähler, K9, Vorstudie)')
w('')
w('| Kennzahl | nachgerechnet | geliefert | gleich |')
w('|---|---|---|---|')
for g, x in einzel:
    e_, g_ = txt(x)
    w(f"| {g} | {e_} | {g_} | {'ja' if x['gleich'] else 'nein'} |")
w('')

# Werte ohne Gegenstueck
w('### Nachgerechnete Werte ohne Gegenstück in der Lieferung')
w('')
w('| Kennzahl | Wert |')
w('|---|---|')
k7e = K['K7 Einstufung Gruppen mit KI-Mehrheit']
w(f"| K7 Einstufung, Gruppen mit KI-Mehrheit je Bedingung (Gruppen mit mindestens einem Befund der Bedingung) | A {pp(k7e['A'], 2)} % von {k7e['A_n']}, B {pp(k7e['B'], 2)} % von {k7e['B_n']}, C {pp(k7e['C'], 2)} % von {k7e['C_n']}, D {pp(k7e['D'], 2)} % von {k7e['D_n']} |")
for v in ('mit', 'ohne'):
    t = K[f'K3 Zusatzbefunde je Gutachten, Variante a ({v} G03)']
    w(f"| K3 Variante a ({v} G03): Zusatzbefund = kein Treffer nach Zuordnungsmehrheit, auch \"teilweise\" genannte, Einstufung zutreffend | " + '; '.join(f"{b} {f(t[b]['mittel'])} ({f(t[b]['min'])} bis {f(t[b]['max'])})" for b in BED) + ' |')
for v in ('mit', 'ohne'):
    t = K[f'K5 Spannweite K1 inhaltlich getroffen ({v} G03)']
    w(f"| K5 Spannweite K1 Hauptmaß, gepoolt ({v} G03), Prozentpunkte | " + '; '.join(f"{b} {pp(t[b]['wert'])}" for b in BED) + ' |')
k9 = K['K9']
w(f"| K9 Fallpaare gleich gruppiert, nur Fälle, die beide Läufe einer Klasse zuordnen | {k9['paare_beide_klassiert_gleich']} von {k9['paare_beide_klassiert']} ({pp(k9['anteil_paare_beide_klassiert'])} %), {k9['in_beiden_klassiert']} Fälle |")
w(f"| K9 Fälle R und R2 | R {k9['faelle_R']} gesammelt, {k9['klassiert_R']} klassiert; R2 {k9['faelle_R2']} gesammelt, {k9['klassiert_R2']} klassiert; nur in R2: Nr. {', '.join(map(str, k9['nur_R2_liste']))} (LAM_B GB-08 und GB-42, Literatur bereits im Verzeichnis) |")
w('')
w('Vorstudie, K1 getrennt nach Art (Protokoll Abschnitt 8: inhaltlich und Kleinkorrekturen getrennt; die Trefferbilanz berichtet nur beide zusammen):')
w('')
w('| Lauf | inhaltlich getroffen | inhaltlich teilweise | Kleinkorrekturen getroffen | Kleinkorrekturen teilweise | drei Läufe gleich |')
w('|---|---|---|---|---|---|')
VO = K['Vorstudie']
for Lk in sorted(VO['gutachten']):
    r = VO['gutachten'][Lk]
    w(f"| {Lk} | {r['getr_inh']} von {r['n_inh']} ({pp(r['k1_inh_getr'])} %) | {r['teil_inh']} ({pp(r['k1_inh_teil'])} %) | {r['getr_kk']} von {r['n_kk']} ({pp(r['k1_kk_getr'])} %) | {r['teil_kk']} | {r['k7_gleich']} von {r['k7_n']} |")
w('')
w('| Durchgang | Gutachten | K1 inhaltlich getroffen, gepoolt | Mittel der Gutachten | K1 inhaltlich teilweise, gepoolt | K1 Kleinkorrekturen getroffen, gepoolt | K7 Zuordnung gleich |')
w('|---|---|---|---|---|---|---|')
for D, r in VO['durchgang'].items():
    w(f"| {D} | {r['gutachten']} | {pp(r['k1_inh_getr_gepoolt'])} % | {pp(r['k1_inh_getr_mittel'])} % | {pp(r['k1_inh_teil_gepoolt'])} % | {pp(r['k1_kk_getr_gepoolt'])} % | {pp(r['k7_gepoolt'])} % |")
w('')
w(f"Sollbefunde der Vorstudie: {VO['soll']['einwaende']} Einwände, {VO['soll']['bestaetigt']} bestätigt ({VO['soll']['inhaltlich']} inhaltlich, {VO['soll']['kleinkorrektur']} Kleinkorrekturen), gleich Nachtrag 3 vom 2026-10-17. Zuordnungsmehrheit in allen 15 Gutachten gleich `mehrheit.md` ({len(VO['mehrheit_md_abweichungen'])} Abweichungen), keine Zeile ohne Mehrheit.")
w('')

# ------------------------------------------------------------ Abweichungen
w('## 4. Abweichungen über 0,05')
w('')
w('| Nr. | Kennzahl | nachgerechnet | geliefert | Ursache |')
w('|---|---|---|---|---|')
urs = {
    'K5': 'Definition "gemeinsame Befunde" nicht im Protokoll festgelegt. Eigene Hauptdefinition: gleicher Sollbefund nur bei Mehrheit "getroffen" (oder gleiche Befundgruppe). Die Lieferung nimmt auch Sollbefunde mit Mehrheit "teilweise" und die dort von 2 Läufen genannten Einträge hinzu; mit dieser Variante reproduziert die Nachrechnung alle 8 Werte exakt (Abschnitt 5).',
    'K7': 'Die Lieferung zählt die 3 Gruppen mit Mehrheit "unklar" als Gruppen ohne Mehrheit (890 von 896). Das Protokoll (Abschnitt 8, K7) misst den Anteil der Gruppen "mit Mehrheit"; eine Mehrheit "unklar" ist eine Mehrheit (893 von 896). Mit der Lesart der Lieferung exakt gleich.',
    'K9 F': 'Der Fallabgleich R gegen R2 vergleicht die Kennungen als Zeichenkette: Zusätze wie "GB-34 (1)" in R und das Komma in "GB-09, GB-41" (R Nr. 49) gegen "GB-09 / GB-41" (R2 Nr. 51) verhindern 6 Zuordnungen (R Nr. 35 bis 39 und 49), und Fälle mit gleichem Lauf und gleicher Kennung werden zusammengelegt (R Nr. 8 und 46, 47 und 48; daher 50 statt 52 Fälle in R). Mit normierten Kennungen sammeln beide Läufe alle 52 Fälle von R; R2 hat 2 Fälle mehr. Fehler in der Lieferung.',
}
erste = {}
for i, x in enumerate(H['abweichungen'], 1):
    k = x['kennzahl']
    typ = 'K5' if k.startswith('K5') else 'K7' if k.startswith('K7') else 'K9 F'
    if typ in erste:
        u = f'wie Nr. {erste[typ]}'
        if typ == 'K9 F':
            u += f" (mit normierten Kennungen {K['K9']['paare_gleich']} von {K['K9']['paare']} Fallpaaren gleich gruppiert)"
    else:
        erste[typ] = i
        u = urs[typ]
    n = 2 if x['einheit'] == 'pp' else 0
    w(f"| {i} | {k} | {f(x['eigen'], n) if n else int(x['eigen'])} | {f(x['geliefert'], 1) if n else int(x['geliefert'])} | {u} |")
w('')
w('## 5. Gegenprobe mit der Definition der Lieferung')
w('')
w('| Kennzahl (Variante) | nachgerechnet | geliefert | gleich |')
w('|---|---|---|---|')
for x in H['varianten']:
    n = 2 if x['einheit'] == 'pp' else 0
    w(f"| {x['kennzahl']} | {f(x['eigen'], n) if n else int(x['eigen'])} | {f(x['geliefert'], 1) if n else int(x['geliefert'])} | {'ja' if x['gleich'] else 'nein'} |")
w('')

# ------------------------------------------------------------ Effektregel
EF = K['Effektregel']


def bereich(e, b, fak=100, n=1):
    k = [kk for kk in e if kk.startswith('bereich_' + b)][0]
    return f"{f(e[k][0] * fak, n)} bis {f(e[k][1] * fak, n)}"


w('## 6. Effektregel je Forschungsfrage')
w('')
w('Effekt heißt: die Spannweiten der beiden Bedingungen überlappen sich nicht (Abschnitt 9, Regel 2; Nachtrag 2 vom 2026-10-17).')
w('')
w('| Frage | Maß | Spannweiten | Effektregel | Urteil nachgerechnet | Urteil geliefert |')
w('|---|---|---|---|---|---|')
gel = {x['rq']: x['geliefert'] for x in H['effektregel_urteile']}
for v, i in (('mit', 0), ('ohne', 1)):
    e = EF['RQ1'][i]
    w(f"| RQ1 ({v} G03) | K1 inhaltlich getroffen, A gegen B | A {bereich(e, 'A')}; B {bereich(e, 'B')} | überlappen, kein Effekt | nicht erfüllt | {gel[f'RQ1 ({v} G03)']} |")
for v, i in (('mit', 0), ('ohne', 1)):
    e = EF['RQ2'][i]; k6 = EF['RQ2'][2]
    w(f"| RQ2 ({v} G03) | K1 inhaltlich getroffen, B gegen C; K6 in B | B {bereich(e, 'B')}; C {bereich(e, 'C')}; K6 B {pp(k6['K6_B_mittel'])} % (kleinster Lauf {pp(k6['K6_B_min'])} %) | getrennt, B über C; K6 über einem Fünftel in jedem Lauf | erfüllt | {gel[f'RQ2 ({v} G03)']} |")
e = EF['RQ3'][0]; k1 = EF['RQ3'][-1]
for v in ('mit', 'ohne'):
    kb = K[f'K1 inhaltlich getroffen ({v} G03)']
    w(f"| RQ3 ({v} G03) | F1 bis F7 je Gutachten, B gegen D; K1 inhaltlich getroffen | F: B {bereich(e, 'B', 1, 2)}; D {bereich(e, 'D', 1, 2)}; K1: B {pp(kb['B']['min'])} bis {pp(kb['B']['max'])}; D {pp(kb['D']['min'])} bis {pp(kb['D']['max'])} | F getrennt, D unter B; K1 überlappen, D nicht weniger | erfüllt | {gel[f'RQ3 ({v} G03)']} |")
w('')
w('RQ3 je Fehlerklasse (B gegen D, Fälle je Gutachten):')
w('')
w('| Klasse | B | D | Ergebnis |')
w('|---|---|---|---|')
for e in EF['RQ3'][1:8]:
    kl = e['kennzahl'].split()[1]
    erg = 'D unter B, getrennt' if e['effekt'] else ('B unter D, getrennt (umgekehrt)' if e['umgekehrter_effekt'] else 'überlappen, kein Effekt')
    w(f"| {kl} | {bereich(e, 'B', 1, 2)} | {bereich(e, 'D', 1, 2)} | {erg} |")
w('')
w('Die Erwartung von RQ3 ist für die Summe F1 bis F7 erfüllt, aber nicht in jeder Klasse: F1, F2 und F7 sinken mit Effekt, F4 bis F6 ohne Effekt, F3 steigt mit Effekt (B 0,25 bis 0,50, D 0,75 bis 1,50). Die Trefferbilanz nennt das in der Klassentabelle; Nachtrag 1 zur Lieferung, Hinweis 1, führt den Anstieg auf die neuen Regeln zu F3 und F4 zurück. Das Protokoll legt nicht fest, ob die Erwartung für die Summe oder je Klasse gilt.')
w('')

# ------------------------------------------------------------ Schwelle
st = K['K7 Stichprobe Auftraggeber gegen Gruppe']
w('## 7. Schwelle der Stichprobe (Protokoll Abschnitt 7, Punkt 5)')
w('')
w(f"Übereinstimmung Auftraggeber gegen Gruppenurteil auf {st['gesamt']['n']} Einzelbefunden: {st['gesamt']['gleich']} gleich, {pp(st['gesamt']['anteil'])} %; je Bedingung A {st['A']['gleich']}, B {st['B']['gleich']}, C {st['C']['gleich']}, D {st['D']['gleich']} von 15. Die Schwelle von 80 % ist erreicht; eine Erweiterung auf 120 war nicht nötig. Die drei Abweichungen:")
w('')
w('| Zufallskennung | Gruppe | Gruppengröße | KI-Mehrheit | Auftraggeber |')
w('|---|---|---|---|---|')
for a in K['K7 Stichprobe Abweichungen']:
    w(f"| {a['zufallskennung']} | {a['gruppe']} | {a['groesse']} | {a['ki']} | {a['auftraggeber']} |")
w('')
w('Nach Punkt 4 gilt das Urteil des Auftraggebers für die ganze Gruppe; das ist in `endgueltig_gruppen.json` so umgesetzt (19 Einzelbefunde betroffen).')
w('')

# ------------------------------------------------------------ Protokollabweichungen
w('## 8. Abweichungen vom Protokoll und Nachträge in Abschnitt 13')
w('')
w('Abschnitt 13 des gelieferten Protokolls enthält drei Nachträge, alle vom 2026-10-17 (Zählung der Vorstudie nur in der Zuordnung; Effektregel entscheidet; Neubestätigung der Sollbefunde der Vorstudie). Nach dem ersten Lauf steht kein Nachtrag.')
w('')
w('| Nr. | Abweichung | Beleg in den Daten | datierter Nachtrag in Abschnitt 13 |')
w('|---|---|---|---|')
rows = [
    ('In allen 24 Läufen zu egusphere-2025-4506 und egusphere-2025-5046 (je Bedingung A bis D, je 3 Läufe) erkannte `einlesen.py` die Randzeilen nicht; die Fundorte wurden am Seitenbild abgezählt. Bei 4695 und 4733 folgte `text.json` den Randnummern. Das Einlesen und damit die Grundlage der Fundorte war in der Hälfte der Läufe ein anderes als vorgesehen; F1 und F2 können dort häufiger sein, alle Bedingungen sind gleich betroffen.',
     'Laufplan: genau 24 Läufe zu 4506 und 5046 (12 und 12, je Bedingung 6). Laufregister: kein Vermerk in diesen Zeilen und keine Korrekturzeile. Beschrieben nur in Nachtrag 1 zur Lieferung, Hinweis 3, und `Randzeilen_Fassungen_v1_20261115.md` (Fassungen 1.0.0 bis 1.4.0: "nein" für 4506, 5046 und das Supplement). Die Prüfberichte nennen in allen vier Manuskripten fast durchweg die Bestätigung an den gedruckten Randnummern der Seitenbilder (4506: 12 von 12, 5046: 11 von 12, 4695 und 4733: je 12 von 12); an ihnen allein ist die Abweichung nicht erkennbar.', 'nein'),
    ('Spalte Verifikation im Laufregister (Pflichtangabe nach Abschnitt 6) ist in allen 48 Zeilen der Hauptstudie leer, obwohl zu jedem Lauf ein Prüfbericht vorliegt.', 'Laufregister, Spalte 15, 48 von 48 leer; `laeufe/verifikation/` hat 48 Prüfberichte, Zuordnung über `nachverarbeitung.json`.', 'nein'),
    ('Die Prüfung der Dateigleichheit des entpackten Skillordners mit dem Paket vor jedem Lauf soll im Laufregister vermerkt werden (Abschnitt 2); das Laufregister hat dafür keine Spalte und keinen Vermerk.', 'Laufregister; `status.json` enthält ein Feld `paket` (Werte 2 bis 18, in L01 bis L03 fehlend) ohne Erläuterung.', 'nein'),
    ('Bedienendes Modell nicht festgehalten: alle 48 Zeilen "claude-opus-5-5 konfiguriert", `status.json` Feld `modell` in allen 48 leer. Das Protokoll verlangt den Vermerk nur, soweit feststellbar (Abschnitt 4); Regel 7 (Modellwechsel) ist damit nicht prüfbar.', 'Laufregister Spalte Modell; `status.json`.', 'nicht nötig, als Grenze offen'),
    ('Verblindung der Gruppierung und Einstufung: In 81 der 1917 Kleinkorrekturen blieb die Spalte mit der Prüfinstanz stehen (Abschnitt 7, Punkt 1: Befunde "ohne ... Instanz").', 'Lieferschein, Hinweis 3. In `einzelbefunde.json` tragen alle 1917 Kleinkorrekturen die Spalte Source; welche 81 Texte so an die Agenten gingen, ist aus der Lieferung nicht nachprüfbar, weil die Eingabedateien `befunde_kurz.md` und `befunde_voll.md` nicht geliefert sind.', 'nein'),
    ('Der Assistent sah die Urteile des Auftraggebers zur Stichprobe (60 Einzelbefunde, 6 Gruppen) vor der Auswertung.', 'Lieferschein, Hinweis 2.', 'nein'),
    ('Auswertungsregel 9 (Gegenrechnung mit zweitem Skript) wurde nach der Auswertung ins Studienhandbuch aufgenommen und steht nicht im Protokoll.', 'Nachtrag 1 zur Lieferung, Hinweis 2.', 'nein'),
    ('Neutralisierung von drei Skillnamen und einer Versionsnummer in zwei Gutachten der Vorstudie vor der Nachzählung.', 'Lieferschein, Hinweis 4; `vorstudie/plan.json` Feld `neutralisiert`.', 'nein'),
    ('Erste Fassung der Auswertung unterschätzte K6 (Instanz bei 90 zutreffenden Kleinkorrekturen nicht erkannt); korrigiert.', 'Lieferschein, Hinweis 1. Die Nachrechnung bestätigt die korrigierten Werte.', 'nicht nötig (Rechenfehler, behoben)'),
    ('Die Trefferbilanz berichtet K1 der Vorstudie nur für inhaltliche Sollbefunde und Kleinkorrekturen zusammen; Abschnitt 8 verlangt die getrennte Angabe, Hauptmaß ist K1 inhaltlich getroffen.', 'Trefferbilanz, Abschnitt Vorstudie; die getrennten Werte stehen hier in Abschnitt 3.', 'nein (Berichtsfehler)'),
    ('K7 je Bedingung: Für die Einstufung durch die KI nennt die Trefferbilanz nur den Gesamtwert; Abschnitt 8 verlangt K7 "gesamt und je Bedingung".', 'Trefferbilanz, K7; die Werte je Bedingung stehen hier in Abschnitt 3.', 'nein (Berichtsfehler)'),
    ('Belege zur Vollständigkeit der Extraktion (`soll/<M>/extraktion2/`, `soll/<M>/abgleich/`), auf die Abschnitt 7 verweist, fehlen in der Lieferung; ebenso die im Protokoll genannte `Herkunft_der_Regeln_v1_20261017.md` und `Dateivergleich_D_gegen_B_20261017.md` (sie liegen nur in den Ordnern des Studienprotokolls unter `quellen/`).', 'Verzeichnis `hauptstudie/soll/` enthält je Manuskript nur `extraktion/`, `hitl.md`, `mehrheit.md`, `sollbefunde.md`.', 'nicht nötig (Lieferumfang)'),
]
for i, r in enumerate(rows, 1):
    w(f'| P{i} | {r[0]} | {r[1]} | {r[2]} |')
w('')
w('Ohne Befund geprüft: 48 Läufe, keiner fehlt, keiner doppelt, keine Wiederholung eines ungültigen Laufs, alle "gültig" mit geprüften Zugriffen; je Bedingung genau die Fassung, Paketprüfsummen und der Aufbau nach Abschnitt 2 und 4; Effort "high" in allen 48 Zeilen; Agentenzahl 8 bei getrennt, 1 bei nacheinander; Reihenfolge gemischt (drei Wellen zu je 16 Läufen); PDF-Prüfsumme je Manuskript einheitlich; Prüfsumme jedes Gutachtens gleich den ersten 12 Stellen in Laufregister und `status.json`; Startwerte der Stichprobe im Laufregister vermerkt und die Ziehung damit reproduzierbar.')
w('')

# ------------------------------------------------------------ Skripte
w('## 9. Skripte')
w('')
w('Ausführung mit `python3 -I` in dieser Reihenfolge; jedes Skript liest nur die Lieferung und die Ausgaben der vorherigen.')
w('')
w('| Datei | Zweck | SHA-256 |')
w('|---|---|---|')
for fn, zw in (('nachrechnung.py', 'Kennzahlen aus Rohdaten nachrechnen, Mehrheiten prüfen'),
               ('vergleich.py', 'Nachgerechnete gegen gelieferte Werte vergleichen'),
               ('bericht.py', 'diesen Bericht aus den Ergebnisdateien erzeugen')):
    h = hashlib.sha256(open(os.path.join(OUT, fn), 'rb').read()).hexdigest()
    w(f'| `{fn}` | {zw} | {h} |')
w('')
w('Ausgaben: `ergebnis.json` (alle Kennzahlen je Bedingung und je Gutachten), `pruefungen.json` (Prüfungen der Eingaben), `vergleich.json` (jeder Vergleich mit Differenz).')
w('')

text = '\n'.join(L)
for bad in ('–', '—'):
    assert bad not in text, 'Gedankenstrich im Bericht'
for l in L:
    if '--' in l and not re.fullmatch(r'\|(-{3}\|)+', l):
        raise SystemExit('doppelter Bindestrich: ' + l[:80])
open(os.path.join(OUT, 'Nachrechnung_6-1_Bericht.md'), 'w', encoding='utf-8').write(text)
print('geschrieben', len(L), 'Zeilen')
