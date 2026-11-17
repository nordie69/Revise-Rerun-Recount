"""7.11.E Schritt 1: Befundgruppen vorbereiten. Je Manuskript ein neutraler Ordner scratchpad/einst/<G>/ mit den strittigen
Einzelbefunden unter zufälligen Kennungen (ohne Lauf, Bedingung, Fassung, Instanz, Wiederholung; Herkunftsfeld entfernt),
dem Manuskript und dem Auftrag GR. Zuordnung Kennung zu Lauf und Eintrag nur in einstufung/kennungen.json. Gibt nur Zählungen aus."""
import hashlib, json, os, random, re, shutil
HS='/home/claude/gutachten-skill/hauptstudie'; SP='/tmp/claude-0/-home-claude/388bb276-2a71-5718-a623-841ee1533b2f/scratchpad'
START=20261022
a=[x for x in json.load(open(f'{HS}/einstufung/einzelbefunde.json',encoding='utf-8')) if x['strittig']]
rnd=random.Random(START); ids=set(); ken={}; gcode={}
def neutral(t):
    out=[]
    for l in t.split('\n'):
        if re.match(r'^\|\s*Source\s*\|',l): continue
        out.append(l)
    t='\n'.join(out)
    if t.startswith('|') and 'Replacement' in t.split('\n')[0]:  # Kleinkorrektur: Herkunftsspalte entfernen
        rows=[[c for c in r.strip().strip('|').split('|')] for r in t.split('\n') if r.startswith('|')]
        rows=[r[:-1] if len(r)>=5 else r for r in rows]
        t='\n'.join('|'+'|'.join(r)+'|' for r in rows)
    t=re.sub(r'\b(GB|KK)-\d+\b','[Eintrag]',t)
    return t
def kurz(x,t):
    if x['kennung'].startswith('GB'):
        titel=t.split('\n')[0][:200]
        loc=next((l for l in t.split('\n') if re.match(r'^\|\s*Location\s*\|',l)),'')
        loc=loc.strip().strip('|').split('|',1)[-1].strip()[:150]
        return 'Befund',loc,titel
    r=[c.strip() for c in t.split('\n')[-1].strip().strip('|').split('|')]
    return 'Kleinkorrektur',(r[1] if len(r)>1 else '')[:150],('Zitat: '+(r[2] if len(r)>2 else '')[:120]+' / Ersatz: '+(r[3] if len(r)>3 else '')[:120])
for M in sorted({x['manuskript'] for x in a}):
    G='G'+hashlib.sha256(f'einst{M}{START}'.encode()).hexdigest()[:6]; gcode[M]=G
    R=f'{SP}/einst/{G}'
    if os.path.exists(R): shutil.rmtree(R)
    os.makedirs(f'{R}/gr')
    xs=[x for x in a if x['manuskript']==M]; rnd.shuffle(xs)
    voll=[f'# Strittige Einzelbefunde','']; kz=['| Kennung | Art | Fundort | Kurzfassung |','|---|---|---|---|']
    for x in xs:
        while True:
            b='B'+''.join(rnd.choice('0123456789abcdef') for _ in range(5))
            if b not in ids: ids.add(b); break
        ken[b]={'code':x['code'],'kennung':x['kennung'],'manuskript':M}
        t=neutral(x['text']); art,loc,k=kurz(x,t)
        voll+= [f'## {b} ({art})','',t,'']
        kz.append(f"| {b} | {art} | {loc.replace('|','/')} | {k.replace('|','/')} |")
    open(f'{R}/befunde_voll.md','w',encoding='utf-8').write('\n'.join(voll)+'\n')
    open(f'{R}/befunde_kurz.md','w',encoding='utf-8').write('\n'.join(kz)+'\n')
    src=f'{SP}/haupt/'+next(c for c,v in ken.items() if v['manuskript']==M and False) if False else None
    code=next(x['code'] for x in xs); S=f'{SP}/haupt/{code}'
    pdf=f'egusphere-2025-{M}.pdf'; shutil.copy2(f'{S}/{pdf}',R); shutil.copy2(f'{S}/text.json',R); shutil.copytree(f'{S}/seiten',f'{R}/seiten')
    if M=='5046':
        shutil.copy2(f'{S}/egusphere-2025-{M}-supplement.pdf',R)
        if os.path.isdir(f'{S}/supplement'): shutil.copytree(f'{S}/supplement',f'{R}/supplement')
    print(M,'->',G,'| strittige Einzelbefunde:',len(xs))
json.dump(ken,open(f'{HS}/einstufung/kennungen.json','w',encoding='utf-8'),indent=0)
json.dump(gcode,open(f'{HS}/einstufung/gruppen_codes.json','w',encoding='utf-8'),indent=1)
print('Kennungen gesamt',len(ken),'Startwert',START)
