"""Nachrechnung zu Gruppe 4 des internen Gutachtens DAT-89 (IG-GB-18, 19, 20, 21, 27, 30), Schritt 8.1, C-249.
Liest nur Dateien des Repositoriums (Stand main 48f8c99) und schreibt gruppe4.json."""
import json, re, collections, statistics, sys
R='/home/claude/revise-rerun-recount/study/delivery_main_study/hauptstudie'
def tab(p):
    return [[x.strip() for x in l.strip().strip('|').split('|')] for l in open(p,encoding='utf-8') if l.startswith('| ') and not re.match(r'^\|\s*(Kennung|Sollbefund|Klasse|Lauf|-)',l)]
plan={r['code']:r for r in json.load(open(f'{R}/laeufe/laufplan.json'))}
nv=json.load(open(f'{R}/laeufe/nachverarbeitung.json'))
K=json.load(open(f'{R}/auswertung/kennzahlen_je_gutachten.json'))
E=json.load(open(f'{R}/einstufung/endgueltig_einzelbefunde.json'))
BED='ABCD'; out={}
def art(M,folder='soll'):
    return {r[0]:r[2] for r in tab(f'{R}/{folder}/{M}/sollbefunde.md') if len(r)>4 and r[4].startswith('bestätigt')}
def mehrheit(p):
    d={}
    for r in tab(p):
        if len(r)>=6: d[r[0]]=(r[4],sorted(set(re.findall(r'\b(?:GB|KK)-\d+\b',r[5]))))
    return d
# ---------- GB-19: RC3 von egusphere-2025-4506
rc3={}
for b in BED:
    rows=[]
    for L,k in K.items():
        if k['bed']!=b or k['M']!='4506': continue
        mit=round(k['K1_inh_getroffen']*k['n_soll_inh']); ohne=round(k['K1_inh_getroffen_ohneG03']*k['n_soll_inh_ohneG03'])
        rows.append((k['wdh'],mit-ohne,k['n_soll_inh']-k['n_soll_inh_ohneG03']))
    n=rows[0][2]; h=[x[1] for x in sorted(rows)]
    # übrige 124: Summe über alle vier Manuskripte ohne RC3
    rest=[]
    for w in (1,2,3):
        hit=sum(round(k['K1_inh_getroffen_ohneG03']*k['n_soll_inh_ohneG03']) for k in K.values() if k['bed']==b and k['wdh']==w)
        nn=sum(k['n_soll_inh_ohneG03'] for k in K.values() if k['bed']==b and k['wdh']==w); rest.append(100*hit/nn)
    rc3[b]={'n_rc3':n,'treffer_je_lauf':h,'quote_mittel':100*sum(h)/(3*n),'quote_min':100*min(h)/n,'quote_max':100*max(h)/n,'uebrige_mittel':statistics.mean(rest),'uebrige_min':min(rest),'uebrige_max':max(rest),'n_uebrige':nn}
out['GB-19']=rc3
# ---------- Zuordnungsmehrheiten Hauptstudie
treffer_ok={}; teil={}; hitrefs={}; mehrfach={}
for L,r in plan.items():
    M=r['manuskript']; A=art(M); mh=mehrheit(f'{R}/laeufe/zuordnung/{nv[L]}/mehrheit.md')
    g=set(); t=set(); hr=collections.Counter(); hits=0; hits_mit=0
    for sid,(m,ids) in mh.items():
        if sid not in A: continue
        if m=='getroffen':
            hits+=1; hits_mit+= bool(ids); g|=set(ids)
            for i in ids: hr[i]+=1
        if m=='teilweise': t|=set(ids)
    treffer_ok[L]=g; teil[L]=t-g; hitrefs[L]=(hits,hits_mit,sum(1 for i,n in hr.items() if n>1),len(g))
# ---------- GB-20 und GB-27: Einträge nach Herkunft und Urteil
ent=collections.defaultdict(list)
for e in E: ent[e['code']].append(e)
t20={}
for b in BED:
    c=collections.Counter(); per=[]
    for L,r in plan.items():
        if r['bedingung']!=b: continue
        for e in ent[L]:
            if e['quelle'].startswith('Zuordnung'): c['richtig durch Zuordnung']+=1; continue
            src='teilweise' if e['kennung'] in teil[L] else 'ohne Sollbefund'
            c[(src,e['urteil'])]+=1
    n=sum(c.values()); t20[b]={str(k):v for k,v in c.items()}; t20[b]['summe']=n; t20[b]['je_gutachten']=n/12
out['GB-20']=t20
out['GB-27']={b:{'nicht_zutreffend':sum(1 for L,r in plan.items() if r['bedingung']==b for e in ent[L] if e['urteil']=='nicht zutreffend'),'eintraege':sum(len(ent[L]) for L,r in plan.items() if r['bedingung']==b)} for b in BED}
# Gegenprobe K3 (ohne Sollbefund, zutreffend, je Gutachten) gegen kennzahlen_je_gutachten
out['K3_gegenprobe']={b:{'eigen':t20[b].get("('ohne Sollbefund', 'zutreffend')",0)/12,'geliefert':statistics.mean(K[L]['K3'] for L in K if K[L]['bed']==b)} for b in BED}
# ---------- GB-30
out['GB-30']={b:{k:sum(hitrefs[L][i] for L,r in plan.items() if r['bedingung']==b) for i,k in enumerate(['getroffene_sollbefunde','davon_mit_eintrag_mit_mehrheit','eintraege_fuer_mehrere_sollbefunde','richtige_eintraege_aus_treffern'])} for b in BED}
out['GB-30']['alle']={k:sum(out['GB-30'][b][k] for b in BED) for k in out['GB-30']['A']}
out['GB-30']['richtig_durch_zuordnung_einstufung']=sum(1 for e in E if e['quelle'].startswith('Zuordnung'))
# ---------- GB-21: Zähler
def faelle(p):
    s=set()
    for l in open(p,encoding='utf-8'):
        if not l.startswith('|') or re.match(r'^\|\s*(Klasse|-)',l): continue
        c=[x.strip() for x in l.strip().strip('|').split('|')]
        m=re.match(r'(K4|F[1-7])\b',c[0]) if c else None
        ids=sorted(set(re.findall(r'\b(?:GB|KK)-\d+\b',c[1]))) if len(c)>1 else []
        if not m or not ids: continue
        k=m.group(1)
        if k in ('K4','F7'): s.add((k,tuple(ids)))
        else:
            for i in ids: s.add((k,(i,)))
    return s
cnt=collections.Counter()
for L in plan:
    runs=[faelle(f'{R}/auswertung/k8/{nv[L]}/zaehlung{k}.md') for k in (1,2,3)]
    c=collections.Counter(x for f in runs for x in f)
    for n in c.values(): cnt[n]+=1
out['GB-21']={'pruefberichte':len(plan),'genannt':sum(cnt.values()),'von_drei':cnt[3],'von_zwei':cnt[2],'von_einem':cnt[1],
 'K5_paare':re.search(r'\| gleiche Schweregrade \|(.*)\|',open(f'{R}/auswertung/kennzahlen_teil1.md',encoding='utf-8').read()).group(1).strip()}
# ---------- GB-18: Vorstudie inhaltliche Sollbefunde
vp=json.load(open(f'{R}/vorstudie/plan.json'))
va={F:art(F,'soll_vorstudie') for F in ('LAM','TCD','HOR')}
vinh={F:sum(1 for x in va[F].values() if x=='inhaltlich') for F in va}
runde=collections.defaultdict(dict)
for V,p in vp.items():
    rd,F,w=p['lauf'].split('-'); mh=mehrheit(f'{R}/vorstudie/zuordnung/{V}/mehrheit.md')
    runde[rd][(F,w)]=sum(1 for s,(m,_) in mh.items() if va[F].get(s)=='inhaltlich' and m=='getroffen')
v18={}
for rd in sorted(runde):
    d=runde[rd]; pooled=100*sum(d.values())/sum(vinh[F] for F,_ in d)
    per={F:statistics.mean(h for (G,_),h in d.items() if G==F) for F in vinh}
    like=100*sum(per.values())/sum(vinh.values())
    v18[rd]={'gutachten':len(d),'treffer':{f'{F}-{w}':h for (F,w),h in sorted(d.items())},'gepoolt':pooled,'LAM_einmal':like,'mittel_drei_manuskripte':statistics.mean(100*per[F]/vinh[F] for F in vinh)}
out['GB-18']={'inhaltliche_sollbefunde':vinh,'runden':v18}
json.dump(out,open('/home/claude/Paper3/nachrechnung_8-1/gruppe4.json','w'),indent=1,ensure_ascii=False,default=str)
print(json.dumps(out,indent=1,ensure_ascii=False,default=str))
