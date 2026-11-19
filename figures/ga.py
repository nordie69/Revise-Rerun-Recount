# Graphical Abstract Paper 3, Neufassung (Fassung 7 nach WV-28 E4 (b) und (c), C-245 und C-246: "review skills", "reference issues"; Fassung 6: Fassung 5 aus C-192, dazu Befund 19 der Konsistenzprüfung vom 2026-11-17, C-199): eine Hauptaussage in der Mitte, Gegenstand links, zwei weitere Änderungen rechts.
# Werte aus DAT-60/DAT-63: K1 Mittel der drei Läufe A 29.1 %, B 28.7 %, Spannweiten A 23.8-33.6, B 25.2-30.8 als Streubalken; Fehler je Gutachten, alle Klassen B 5.67, D 2.92; Klasse F3 (wrong count) B 0.42, D 1.17.
# Farben wie in Fig. 4 und 5: A grau, B blau, C orange, D grün.
H='<?xml version="1.0" encoding="UTF-8"?>\n<svg xmlns="http://www.w3.org/2000/svg" width="1328" height="531" viewBox="0 0 1328 531" font-family="Arial, Helvetica, \'Liberation Sans\', sans-serif">\n<defs><marker id="pf" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="5" markerHeight="5" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="#555555"/></marker><clipPath id="cl"><circle cx="160" cy="345" r="88"/></clipPath></defs>\n<rect width="1328" height="531" fill="#FFFFFF"/>\n'
def t(x,y,s,fs=28,a="middle",w="normal",c="#333333"): return f'<text x="{x}" y="{y}" font-size="{fs}" fill="{c}" text-anchor="{a}" font-weight="{w}">{s}</text>\n'
def box(x,y,w,h,c="#999999",sw=4): return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="12" fill="#FFFFFF" stroke="{c}" stroke-width="{sw}"/>\n'
def arrow(x1,y1,x2,y2): return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="#555555" stroke-width="3" marker-end="url(#pf)"/>\n'
s=H
# links: Gegenstand
s+=box(24,24,380,483)
s+='<rect x="179" y="44" width="70" height="88" rx="4" fill="#FFFFFF" stroke="#555555" stroke-width="3"/>'+''.join(f'<line x1="191" y1="{y}" x2="237" y2="{y}" stroke="#999999" stroke-width="3"/>' for y in (62,78,94,110))+'\n'
s+=t(214,162,"preprint",24,c="#555555")+arrow(196,174,150,208)+arrow(232,174,278,208)
s+=t(118,238,"AI review",24,c="#555555")+t(296,238,"human referees",24,c="#555555")
s+='<circle cx="160" cy="345" r="88" fill="#E6E6E6"/><circle cx="268" cy="345" r="88" fill="#E6E6E6"/><circle cx="268" cy="345" r="88" fill="#333333" clip-path="url(#cl)"/><circle cx="160" cy="345" r="88" fill="none" stroke="#555555" stroke-width="3"/><circle cx="268" cy="345" r="88" fill="none" stroke="#555555" stroke-width="3"/>\n'
s+='<line x1="214" y1="400" x2="214" y2="452" stroke="#333333" stroke-width="3"/>\n'+t(214,484,"issues hit",28,w="bold")
# Mitte: Hauptbefund
s+=box(424,24,480,483,"#0072B2",6)
s+=t(664,66,"Revising the AI's",28,w="bold")+t(664,100,"review skills",28,w="bold")+t(664,136,"substantive reference issues hit",24,c="#555555")
Y0=384
for cx,v,c,lab,lo,hi in ((574,29.1,"#999999","first",23.8,33.6),(754,28.7,"#0072B2","revised",25.2,30.8)):
    h=v*5.8; s+=f'<path d="M{cx},{Y0-lo*5.8:.1f} L{cx},{Y0-hi*5.8:.1f} M{cx-14},{Y0-lo*5.8:.1f} L{cx+14},{Y0-lo*5.8:.1f} M{cx-14},{Y0-hi*5.8:.1f} L{cx+14},{Y0-hi*5.8:.1f}" stroke="#333333" stroke-width="3" fill="none"/>\n' if False else ""; s+=f'<rect x="{cx-58}" y="{Y0-h:.1f}" width="116" height="{h:.1f}" rx="4" fill="{c}"/>\n'+t(cx,Y0-hi*5.8-12,f"{v} %",30,w="bold")+f'<path d="M{cx},{Y0-lo*5.8:.1f} L{cx},{Y0-hi*5.8:.1f} M{cx-14},{Y0-lo*5.8:.1f} L{cx+14},{Y0-lo*5.8:.1f} M{cx-14},{Y0-hi*5.8:.1f} L{cx+14},{Y0-hi*5.8:.1f}" stroke="#333333" stroke-width="3" fill="none"/>\n'+t(cx,Y0+30,lab,24,c="#555555")
s+=f'<line x1="474" y1="{Y0}" x2="854" y2="{Y0}" stroke="#999999" stroke-width="3"/>\n'
s+=t(664,484,"no gain",44,w="bold")
# rechts: zwei weitere Änderungen
s+=t(1114,46,"Further comparisons",24,w="bold",c="#555555")
s+=box(924,60,380,206)+t(1114,98,"Separate agents",28,w="bold")
s+='<rect x="990" y="118" width="70" height="70" rx="6" fill="#E69F00"/>'+arrow(1076,153,1118,153)+''.join(f'<rect x="{x}" y="133" width="34" height="40" rx="5" fill="#0072B2"/>' for x in (1134,1176,1218))+'\n'
s+=t(1114,240,"more issues hit",28,w="bold")
s+=box(924,281,380,226)+t(1114,318,"New rules",28,w="bold")
YB,SC=420,12
for x0,(b,d),l1,l2 in ((965,(5.67,2.92),"sum of classes:","about halved"),(1150,(0.42,1.17),"wrong counts:","rose")):
    s+=f'<rect x="{x0}" y="{YB-b*SC:.1f}" width="40" height="{b*SC:.1f}" rx="2" fill="#0072B2"/><rect x="{x0+84}" y="{YB-d*SC:.1f}" width="40" height="{d*SC:.1f}" rx="2" fill="#009E73"/>'
    s+=arrow(x0+48,YB-28 if b>d else YB-22,x0+78,YB-28 if b>d else YB-22)
    s+=f'<line x1="{x0-6}" y1="{YB}" x2="{x0+130}" y2="{YB}" stroke="#999999" stroke-width="3"/>\n'
    s+=t(x0+62,YB+30,l1,24,c="#555555")+t(x0+62,YB+60,l2,26,w="bold")
open("ga.svg","w").write(s+"</svg>\n")
