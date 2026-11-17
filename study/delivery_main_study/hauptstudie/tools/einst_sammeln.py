"""7.11.E Schritt 1 (Vorbereitung): sammelt je Gutachten alle Einträge (GB, KK) und bestimmt die strittigen.
Zutreffend ist ein Eintrag, den die Mehrheit (>=2) der drei Zuordnungsläufe für denselben Sollbefund als getroffen nennt
(Studienprotokoll Abschnitt 7). Alle übrigen sind strittig. Schreibt einstufung/einzelbefunde.json (Code, Kennung, Text,
strittig). Gibt nur Zählungen aus."""
import collections, glob, json, re, sys
HS='/home/claude/gutachten-skill/hauptstudie'
plan={r['code']:r for r in json.load(open(f'{HS}/laeufe/laufplan.json',encoding='utf-8'))}
nv=json.load(open(f'{HS}/laeufe/nachverarbeitung.json',encoding='utf-8'))
def tab(p):
    return [[x.strip() for x in l.strip().strip('|').split('|')] for l in open(p,encoding='utf-8') if l.startswith('|') and not re.match(r'^\|\s*(Sollbefund|Kennung|-)',l)]
def eintraege(f):
    L=open(f,encoding='utf-8').read().split('\n'); out={}; i=0; kkhead=None
    while i<len(L):
        l=L[i]
        m=re.match(r'^\*\*(GB-\d+)',l)
        if m:
            j=i+1
            while j<len(L) and not re.match(r'^(\*\*(GB|KK)-\d+|#{1,4} )',L[j]): j+=1
            out[m.group(1)]='\n'.join(L[i:j]).strip(); i=j; continue
        if l.startswith('|') and re.search(r'\bKennung\b|\bID\b',l,re.I): kkhead=l
        m=re.match(r'^\|\s*(KK-\d+)\s*\|',l)
        if m: out[m.group(1)]=((kkhead+'\n') if kkhead else '')+l
        i+=1
    return out
alle=[]; z=collections.Counter()
for code,r in sorted(plan.items()):
    f=glob.glob(f'{HS}/laeufe/ergebnis/{code}/*_Gutachten.md')[0]; E=eintraege(f); N=nv[code]
    cnt=collections.Counter()
    for k in (1,2,3):
        for row in tab(f'{HS}/laeufe/zuordnung/{N}/zuordnung{k}.md'):
            if len(row)>=3 and row[1].lower().strip()=='getroffen':
                for e in set(re.findall(r'\b(?:GB|KK)-\d+\b',row[2])): cnt[(row[0],e)]+=1
    zutr={e for (s,e),n in cnt.items() if n>=2}
    for k,t in E.items():
        alle.append({'code':code,'manuskript':r['manuskript'],'kennung':k,'text':t,'strittig':k not in zutr})
    z[(r['manuskript'],'alle')]+=len(E); z[(r['manuskript'],'strittig')]+=sum(k not in zutr for k in E)
    z[(r['manuskript'],'zeichen_strittig')]+=sum(len(t) for k,t in E.items() if k not in zutr)
    unbek=zutr-set(E)
    if unbek: print(code,'Zuordnung nennt unbekannte Kennungen:',len(unbek))
json.dump(alle,open(f'{HS}/einstufung/einzelbefunde.json','w',encoding='utf-8'),ensure_ascii=False)
for M in sorted({r['manuskript'] for r in plan.values()}):
    print(M,'Einträge',z[(M,'alle')],'strittig',z[(M,'strittig')],'Zeichen strittig',z[(M,'zeichen_strittig')])
print('gesamt Einträge',len(alle),'strittig',sum(a['strittig'] for a in alle))
