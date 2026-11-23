# Abbildung Ablauf science-review-gutachten (SB-44, Wahl C-146): Skizze A mit den Trennwänden aus Skizze B, Hausstil wie Fig. 1; Fassung 3 nach Prüfdurchgang 2 (SB-53, C-148)
# Grundlage: Methodendokument science-review-gutachten 1.3.0 (DAT-58), Kapitel 4; Manuskript Sect. 3.1 und 3.3, Table 2
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
plt.rcParams.update({"font.family":"DejaVu Sans","pdf.fonttype":42,"svg.fonttype":"none"})
K="#333333"; L,M,S=7.7,6.9,6.7
def box(ax,x,y,w,h,t,fs=M,bold=False,lw=1.1,fc="white"):
    ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle="round,pad=0.02,rounding_size=0.08",ec=K,fc=fc,lw=lw))
    ax.text(x+w/2,y+h/2,t,ha="center",va="center",fontsize=fs,weight="bold" if bold else "normal",linespacing=1.15)
def arr(ax,x1,y1,x2,y2,head=True,lw=0.9):
    ax.annotate("",xy=(x2,y2),xytext=(x1,y1),arrowprops=dict(arrowstyle="-|>" if head else "-",color="#444",lw=lw,shrinkA=0,shrinkB=0,mutation_scale=7))
def note(x,y,t,ha="center",va="center"): ax.text(x,y,t,fontsize=S,ha=ha,va=va,color="#444",linespacing=1.15)
W,H=10.6,5.6
f,ax=plt.subplots(figsize=(6.69,6.69*(H+0.45)/W)); f.subplots_adjust(0,0,1,1); ax.set_xlim(0,W); ax.set_ylim(-0.15,H+0.3); ax.axis("off")
ym=2.8
box(ax,0.15,ym-0.45,0.95,0.9,"Manuscript\n(PDF)")
box(ax,1.4,ym-0.5,1.75,1.0,"Preparing agent\nreads and segments\nthe manuscript",fs=S)
arr(ax,1.1,ym,1.4,ym)
# six instances with walls
INST=[("S1","segment 1"),("S2","segment 2"),("S3","segment 3"),("S4","segment 4"),("AB","figures (own skill)"),("SD","study design (own skill)")]
x0,w,h,gap=4.05,1.85,0.52,0.2
ys=[4.35-i*(h+gap) for i in range(6)]
for (k,t),y in zip(INST,ys):
    box(ax,x0,y,w,h,f"{k}\n{t}",fs=S)
    arr(ax,3.17,ym,x0-0.02,y+h/2)
    arr(ax,x0+w+0.02,y+h/2,6.33,ym)
for y in ys[:-1]:
    ax.plot([x0-0.08,x0+w+0.08],[y-gap/2,y-gap/2],color=K,lw=1.6,solid_capstyle="butt")
ax.text(x0+w/2,5.68,"six separate agents in parallel",ha="center",va="bottom",fontsize=M,weight="bold")
note(x0+w/2,5.6,"thick lines: instructed not to access each other;\nevery instance: its own instructions, no reference issues",va="top")
# shared checks as text: brackets would cross the arrows
note(x0+w/2,ys[5]-0.1,"overlapping items on purpose:\nS2 and AB, S4 and AB, S4 and SD",va="top")
# merger and output
box(ax,6.35,ym-1.2,1.75,2.4,"Merging agent\n(no reference issues)\n\nremoves duplicates,\nchecks contested\npassages against\nthe manuscript",fs=S)
box(ax,8.45,3.15,1.95,1.2,"Merged review:\nfindings, minor\ncorrections, summary\n(4 strengths,\n4 weaknesses)",fs=S)
box(ax,8.45,2.15,1.95,0.75,"Format check\n(script): must pass",fs=S)
box(ax,8.45,0.75,1.95,0.85,"Review handed over;\nno recommendation\non acceptance",fs=S,fc="#E6E6E6")
arr(ax,8.1,3.75,8.45,3.75); arr(ax,9.425,3.13,9.425,2.92); arr(ax,9.425,2.15,9.425,1.6)
for ext,kw in (("png",{"dpi":300}),("pdf",{}),("svg",{})): f.savefig(f"fig_ablauf_skill.{ext}",**kw)
print("ok")
