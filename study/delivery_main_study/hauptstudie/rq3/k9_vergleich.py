import re,itertools,sys
def lese(p):
    s=open(p,encoding='utf-8').read(); f=s.split('## Fälle')[1].split('\n## ')[0]; d={}
    for l in f.split('\n'):
        if re.match(r'\|\s*\d+\s*\|',l):
            c=[x.strip() for x in l.split('|')[1:-1]]
            key=(c[1], ' / '.join(sorted(k.strip() for k in c[2].split('/'))))
            kl=c[-1]; d.setdefault(key,set()).add(kl)
    return d
R=lese('Regelvorschlaege_RQ3.md'); R2=lese('R2/Regelvorschlaege_RQ3_R2.md')
gem=sorted(set(R)&set(R2))
def kl(d,k):
    v=sorted(d[k]); v=[x for x in v if re.match(r"F[1-7]$",x)]; return v[0] if v else None
gleich=0;n=0
for a,b in itertools.combinations(gem,2):
    x=(kl(R,a) is not None and kl(R,a)==kl(R,b)); y=(kl(R2,a) is not None and kl(R2,a)==kl(R2,b))
    n+=1; gleich+=(x==y)
kr=sum(kl(R,k) is not None for k in R); kr2=sum(kl(R2,k) is not None for k in R2)
print(f'R: {len(R)} Fälle, {kr} klassiert; R2: {len(R2)} Fälle, {kr2} klassiert; gemeinsam {len(gem)}; nur R {len(set(R)-set(R2))}; nur R2 {len(set(R2)-set(R))}')
print(f'Fallpaare gleich gruppiert: {gleich} von {n} = {100*gleich/n:.1f} %')
bk=sum(1 for k in gem if kl(R,k) and kl(R2,k)); print('in beiden klassiert:',bk)
