# Ergebnisabbildungen Paper 3 (Workplan 6.2, Wahl C-142): Fig. 2 Vorstudie, Fig. 3 K1 je Bedingung, Fig. 4 Fehlerklassen.
# Zahlen: DAT-60, hauptstudie/auswertung/Trefferbilanz_Hauptstudie_v1_20261115.md, nachgerechnet in DAT-63 (nachrechnung_6-1).
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"font.family":"DejaVu Sans","pdf.fonttype":42,"svg.fonttype":"none","font.size":6.5,"axes.labelsize":6.5,
 "xtick.labelsize":6.0,"ytick.labelsize":6.0,"legend.fontsize":6.0,"axes.titlesize":6.5,"axes.spines.top":False,"axes.spines.right":False,
 "axes.linewidth":0.6,"xtick.major.width":0.6,"ytick.major.width":0.6})
COL={"A":"#999999","B":"#0072B2","C":"#E69F00","D":"#009E73"}
def save(f,n):
    for ext,kw in (("png",{"dpi":300}),("pdf",{}),("svg",{})): f.savefig(f"{n}.{ext}",**kw)
    plt.close(f)
def rng(ax,x,m,lo,hi,c,mk="o",open_=False,lw=2.4,cap=0):
    ax.plot([x,x],[lo,hi],color=c,lw=lw,alpha=0.55,solid_capstyle="butt")
    if cap:  # Endstriche, nur Fig. 5 (WV-28, A2)
        for yv in (lo,hi): ax.plot([x-cap,x+cap],[yv,yv],color=c,lw=0.9)
    ax.plot(x,m,mk,color=c,ms=3.8,mfc="white" if open_ else c,mew=0.9)

# Fig. 2 Vorstudie: Hauptmaß, inhaltliche Sollbefunde getroffen, je Gutachten (DAT-63, Vorstudie K1 getrennt nach Art)
V=[1,2,3,4]
pts={"Mohr (2026a)":{1:[42.5,47.5],2:[60.0],3:[52.5,65.0],4:[57.5,52.5]},"Mohr (2026b)":{1:[50.0],2:[72.0],3:[68.0],4:[76.0]},"egusphere-2025-2248":{1:[47.1],2:[50.0],3:[64.7],4:[58.8]}}
allv=[47.0,62.1,62.8,62.2]
f,ax=plt.subplots(figsize=(3.27,2.5),constrained_layout=True)
for (k,d),c,mk,dx in zip(pts.items(),["#222222","#222222","#222222"],["o","s","^"],[-0.08,0.0,0.08]):
    xs=[];ys=[]
    for v in V:
        for y in d[v]: ax.plot(v+dx,y,mk,color=c,ms=3.0,mfc="white",mew=0.7)
        xs.append(v+dx); ys.append(sum(d[v])/len(d[v]))
    ax.plot(xs,ys,color=c,lw=0.7,ls=":",marker=mk,ms=3.4,label=k)
ax.plot(V,allv,color="#000000",lw=1.6,label="all reviews of a round")
for x,t_ in ((1.5,"set-up:\none context\n→ separate"),(2.5,"version:\n1.0.0 → 1.1.0"),(3.5,"version:\n1.1.0 →\nbase version B")):
    ax.text(x,36.5,t_,ha="center",va="bottom",fontsize=6.0,color="#444444")
ax.set_xticks(V); ax.set_xticklabels(["V1","V2","V3","V4"]); ax.set_xlabel("review round of the pilot"); ax.set_xlim(0.7,4.3); ax.set_ylim(35,90)
ax.set_ylabel("substantive reference issues hit (%)")
ax.legend(frameon=False,ncol=1,loc="upper left",handlelength=2.2)
save(f,"fig02_pilot")

# Fig. 3 K1 Hauptmaß je Bedingung
K1={"mit":{"A":(29.1,23.8,33.6),"B":(28.7,25.2,30.8),"C":(21.9,21.7,22.4),"D":(27.7,25.9,30.8)},
    "ohne":{"A":(28.5,23.4,32.3),"B":(26.3,24.2,28.2),"C":(21.2,21.0,21.8),"D":(25.3,23.4,28.2)}}
f,ax=plt.subplots(figsize=(3.27,2.5),constrained_layout=True)
for i,c in enumerate("ABCD"):
    rng(ax,i-0.13,*K1["mit"][c],COL[c])
    rng(ax,i+0.13,*K1["ohne"][c],COL[c],mk="D",open_=True)
for a,b,t,y in ((0,1,"RQ1: not met",35.2),(1,2,"RQ2: met (pooled)",33.0),(1,3,"RQ3, K1 part: met (all runs)",37.4)):
    ax.plot([a,b],[y,y],color="#444444",lw=0.6); ax.plot([a,a],[y-0.4,y],color="#444444",lw=0.6); ax.plot([b,b],[y-0.4,y],color="#444444",lw=0.6)
    ax.text((a+b)/2,y+0.25,t,ha="center",va="bottom",fontsize=6.0)
ax.set_xticks(range(4)); ax.set_xticklabels(["A\nfirst version","B\nbase version","C\none context","D\nnew rules"])
ax.set_ylim(15,39.5); ax.set_xlim(-0.5,3.5); ax.set_ylabel("substantive reference issues hit (%)")
save(f,"fig03_k1_conditions")

# Fig. 4 Fehlerklassen B gegen D
# Schrift größer für den Druck (Gutachten 3, AB-GB-01): mindestens 6 pt bei voller Satzbreite
plt.rcParams.update({"font.size":7.2,"axes.labelsize":7.2,"xtick.labelsize":6.7,"ytick.labelsize":6.7,"axes.titlesize":7.2})
F={"F1":((0.33,0.25,0.50),(0.00,0.00,0.00),"D lower"),"F2":((0.92,0.75,1.25),(0.25,0.00,0.50),"D lower"),"F3":((0.42,0.25,0.50),(1.17,0.75,1.50),"D higher"),
   "F4":((0.50,0.25,1.00),(0.75,0.50,1.00),""),"F5":((0.33,0.00,0.50),(0.42,0.25,0.50),""),"F6":((0.08,0.00,0.25),(0.00,0.00,0.00),""),"F7":((3.08,1.50,4.75),(0.33,0.00,1.00),"D lower")}
f,(a1,a2)=plt.subplots(1,2,figsize=(6.69,2.6),gridspec_kw={"width_ratios":[5,1.2]},constrained_layout=True)
for i,(k,(b,d,eff)) in enumerate(F.items()):
    rng(a1,i-0.15,*b,COL["B"],cap=0.09); rng(a1,i+0.15,*d,COL["D"],cap=0.09)
    if eff: a1.text(i,5.05,eff,ha="center",va="bottom",fontsize=6.7,color="#000000" if eff=="D higher" else "#444444",weight="bold" if eff=="D higher" else "normal")
NAMES=["F1\npage of a\nline range","F2\nline number\noffset","F3\nwrong\ncount","F4\nclaim on\nseveral places\nunchecked","F5\nevidence\nmoved to\nneighbour","F6\nsource detail\nclaimed as\nverified","F7\nneighbours\nnot linked"]
a1.set_xticks(range(7)); a1.set_xticklabels(NAMES); a1.set_ylim(-0.2,5.6); a1.set_ylabel("cases per review")
rng(a2,0,5.67,5.25,6.25,COL["B"],cap=0.18); rng(a2,1,2.92,2.50,3.50,COL["D"],cap=0.18)
a2.set_xticks([0,1]); a2.set_xticklabels(["B","D"]); a2.set_xlim(-0.6,1.6); a2.set_ylim(0,7.4); a2.set_title("all classes"); a2.set_ylabel("cases per review")
a2.text(0.5,6.55,"D lower",ha="center",va="bottom",fontsize=6.7,color="#444444")
save(f,"fig04_error_classes")
print("ok")
