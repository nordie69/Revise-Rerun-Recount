"""Wandelt das verblindete Einstufungsblatt (Markdown) in ein Word-Dokument mit Eingabefeldern:
je Eintrag ein Auswahlfeld (zutreffend, nicht zutreffend, Ansichtssache) und ein Textfeld für die Begründung.
Die Felder tragen die Kennung E<Nr> und B<Nr>, damit die Antworten per Skript zurückgelesen werden können.
Liest und druckt keine Befundinhalte; gibt nur Zählungen aus. Aufruf: einst_blatt_docx.py <md> <docx>"""
import re, sys, subprocess, tempfile, os, zipfile, shutil, html
SRC, DST = sys.argv[1], sys.argv[2]
lines = open(SRC, encoding='utf-8').read().split('\n')
ANLEITUNG = ('**So gehst du vor:** Prüfe jeden Eintrag am PDF des Manuskripts so weit, wie es für ein Urteil nötig ist. '
             'Unter jedem Eintrag steht ein grau hinterlegtes Feld "Einstufung": anklicken und zutreffend, nicht zutreffend oder Ansichtssache wählen. '
             'Darunter ist ein Feld für eine freiwillige Begründung. Bei einer Gruppe urteilst du über den gemeinsamen Gegenstand. '
             'Speichere das Dokument unter demselben Namen mit dem Zusatz "_ausgefuellt" und schick es zurück.')
out, offen, n_anl = [], None, 0
def schliessen():
    global offen
    if offen is not None:
        out.extend(['', f'FELDMARKE{offen}FELDMARKE', '']); offen = None
for l in lines:
    if l.startswith('**So gehst du vor:**'):
        out.append(ANLEITUNG); n_anl += 1; continue
    m = re.match(r'^(#{1,4}) ', l)
    if m:
        schliessen()
        k = re.match(r'^#### (\d+)\. ', l)
        if k: offen = int(k.group(1))
    out.append(l)
schliessen()
assert n_anl == 1
tmp = tempfile.mkdtemp()
md2 = os.path.join(tmp, 'blatt.md'); open(md2, 'w', encoding='utf-8').write('\n'.join(out) + '\n')
roh = os.path.join(tmp, 'roh.docx')
subprocess.run(['pandoc', md2, '-f', 'markdown-smart', '-o', roh], check=True)
z = zipfile.ZipFile(roh); doc = z.read('word/document.xml').decode('utf-8')
WAHL = ['zutreffend', 'nicht zutreffend', 'Ansichtssache']
def feld(nr):
    items = '<w:listItem w:displayText="bitte wählen" w:value=""/>' + ''.join(f'<w:listItem w:displayText="{w}" w:value="{w}"/>' for w in WAHL)
    shade = '<w:pPr><w:shd w:val="clear" w:color="auto" w:fill="E7E6E6"/><w:spacing w:before="60" w:after="60"/></w:pPr>'
    lab = lambda t: f'<w:r><w:rPr><w:b/></w:rPr><w:t xml:space="preserve">{t}</w:t></w:r>'
    dd = (f'<w:sdt><w:sdtPr><w:alias w:val="Einstufung {nr}"/><w:tag w:val="E{nr}"/><w:dropDownList>{items}</w:dropDownList></w:sdtPr>'
          f'<w:sdtContent><w:r><w:rPr><w:color w:val="2F5496"/></w:rPr><w:t>bitte wählen</w:t></w:r></w:sdtContent></w:sdt>')
    tx = (f'<w:sdt><w:sdtPr><w:alias w:val="Begründung {nr}"/><w:tag w:val="B{nr}"/><w:text w:multiLine="1"/></w:sdtPr>'
          f'<w:sdtContent><w:r><w:rPr><w:color w:val="808080"/></w:rPr><w:t>(freiwillig)</w:t></w:r></w:sdtContent></w:sdt>')
    return (f'<w:p>{shade}{lab(f"Einstufung zu Nr. {nr}: ")}{dd}</w:p>'
            f'<w:p>{shade}{lab("Begründung: ")}{tx}</w:p>')
cnt = 0
def ers(m):
    global cnt; cnt += 1; return feld(int(m.group(1)))
doc = re.sub(r'<w:p\b(?:(?!<w:p\b).)*?FELDMARKE(\d+)FELDMARKE.*?</w:p>', ers, doc, flags=re.S)
assert 'FELDMARKE' not in doc
neu = os.path.join(tmp, 'neu.docx')
with zipfile.ZipFile(roh) as zi, zipfile.ZipFile(neu, 'w', zipfile.ZIP_DEFLATED) as zo:
    for it in zi.infolist():
        zo.writestr(it, doc.encode('utf-8') if it.filename == 'word/document.xml' else zi.read(it.filename))
shutil.copy(neu, DST); shutil.rmtree(tmp)
print('Einträge im Markdown', sum(1 for l in lines if re.match(r'^#### \d+\. ', l)), 'Felder eingesetzt', cnt)
