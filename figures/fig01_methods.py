# Fig. 1, Paper 3: design and measurement procedure (Skizze A mit den Vergleichen aus Skizze B; Fassung 7 nach WV-28, A1: Pfeil disputed findings unter der Box 48 reviews)
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
plt.rcParams.update({"font.family":"DejaVu Sans","pdf.fonttype":42,"svg.fonttype":"none"})
L,M,S=7.7,6.9,6.7
def box(ax,x,y,w,h,text,c,fs=M,bold=False,lw=1.1,ls="-"):
    ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle="round,pad=0.02,rounding_size=0.08",ec=c,fc="white",lw=lw,ls=ls))
    ax.text(x+w/2,y+h/2,text,ha="center",va="center",fontsize=fs,weight="bold" if bold else "normal",linespacing=1.15)
def arr(ax,x1,y1,x2,y2,c="#444",head=True,lw=0.9):
    ax.annotate("",xy=(x2,y2),xytext=(x1,y1),arrowprops=dict(arrowstyle="-|>" if head else "-",color=c,lw=lw,shrinkA=0,shrinkB=0,mutation_scale=7))
def note(x,y,t,ha="center",va="center"): ax.text(x,y,t,fontsize=S,ha=ha,va=va,color="#444")
W=10.6
f,ax=plt.subplots(figsize=(6.69,4.62)); f.subplots_adjust(0,0,1,1); ax.set_xlim(0,W); ax.set_ylim(0,7.15); ax.axis("off")
# bands
ax.add_patch(plt.Rectangle((0,5.55),W,1.6,fc="#E0E0E0",ec="none"))
ax.text(0.1,6.95,"Development (pilot): no rule taken from the test material",fontsize=M,weight="bold",color="#333333")
ax.add_patch(plt.Rectangle((0,0.0),W,5.4,fc="white",ec="none"))
ax.text(0.1,5.2,"Main study (test material)",fontsize=M,weight="bold",color="#333333")
# development
box(ax,0.2,5.7,2.45,1.05,"Pilot V1 to V4 on\ndevelopment material;\n149 confirmed\nreference issues, matched\nlike the main study","#333333",fs=S,ls="--")
box(ax,2.95,5.7,2.1,1.05,"V4 tests base version B\n(1.3.0 / 1.2.0 / 1.2.0);\ncheck reports of V4","#333333",fs=S,ls="--")
box(ax,5.35,5.7,2.1,1.05,"Agent R proposes\nrules F1 to F7\n→ version D","#333333",fs=S,ls="--")
box(ax,7.95,5.7,1.8,1.05,"Agent R2:\nsame input,\nindependent run","#333333",fs=S,ls="--")
arr(ax,2.65,6.22,2.95,6.22,c="#333333"); arr(ax,5.05,6.22,5.35,6.22,c="#333333")
arr(ax,7.45,6.22,7.95,6.22,c="#333333",head=False,lw=1.2); note(7.7,6.3,"K9",va="bottom")
arr(ax,4.0,5.7,4.0,4.95,c="#333333"); arr(ax,6.4,5.7,6.4,4.95,c="#333333")
# test material
box(ax,0.2,2.95,1.85,1.3,"Test material:\n4 EGUsphere\npreprints","#333333")
box(ax,0.2,0.6,1.85,0.95,"Public referee\nreports of the\n4 preprints","#333333",fs=S)
# reviews with embedded comparisons
box(ax,2.35,2.25,5.15,2.7,"","#333333",lw=1.3)
ax.text(4.925,4.7,"48 reviews",ha="center",va="center",fontsize=L,weight="bold")
ax.text(4.925,4.4,"4 conditions × 4 manuscripts × 3 repetitions",ha="center",va="center",fontsize=M)
cw,ch=1.4,0.72
CC={"A":"#999999","B":"#0072B2","C":"#E69F00","D":"#009E73"}
def cond(x,y,t): box(ax,x,y,cw,ch,t,CC[t.strip()[0]],fs=S,lw=1.4)
cond(2.5,3.35,"A  first version\n1.0.0/1.0.0/1.0.0"); cond(4.225,3.35,"B  base version\n1.3.0/1.2.0/1.2.0")
cond(5.95,3.35,"D  new rules\n1.4.0/1.3.0/1.2.0"); cond(4.225,2.4,"C  as B,\none context,\nin sequence")
for x1,x2,lab in ((3.9,4.225,"RQ1"),(5.625,5.95,"RQ3")):
    arr(ax,x1,3.71,x2,3.71,head=False,lw=1.2); ax.text((x1+x2)/2,4.1,lab,ha="center",va="bottom",fontsize=S)
arr(ax,4.925,3.35,4.925,3.12,head=False,lw=1.2); ax.text(5.0,3.235,"RQ2",fontsize=S,va="center")
note(3.2,2.75,"each line:\ndesigned to\nchange one factor")
# verification, rating, measures
box(ax,7.85,4.15,1.9,0.8,"Verification\n(check report)","#333333",fs=S)
box(ax,7.6,2.15,2.15,1.75,"Rating of disputed findings:\nfinding groups; rating agent,\n3 runs, majority; author:\nno majority or unclear, and\nblinded sample of 60\n(below 80 %: +60, then all)","#333333",fs=S)
box(ax,7.6,0.35,2.15,1.15,"Measures K1 to K9\n→ RQ1 to RQ3","#333333",fs=L,bold=True)
# reference issues, matching
box(ax,2.35,0.2,2.45,1.75,"Reference issues\n205 objections, 198 confirmed\n(143 substantive);\n3 checking agents, majority;\nsecond extraction: none missing","#333333",fs=S)
box(ax,5.05,0.35,1.4,1.55,"Matching\n3 runs, majority\nhit / partial /\nmissed / unclear","#333333")
# flows
arr(ax,2.05,3.6,2.35,3.6)
arr(ax,2.05,1.08,2.35,1.08)
arr(ax,5.85,2.25,5.75,1.9)
arr(ax,4.8,1.12,5.05,1.12)
arr(ax,7.5,4.55,7.85,4.55)
arr(ax,9.75,4.55,10.15,4.55,head=False); arr(ax,10.15,4.55,10.15,0.92,head=False); arr(ax,10.15,0.92,9.75,0.92)
ax.text(10.25,2.7,"K4, K8",fontsize=S,rotation=90,ha="left",va="center",color="#444")
arr(ax,6.45,1.75,8.05,1.75,head=False); arr(ax,8.05,1.75,8.05,2.15); note(7.05,1.5,"disputed\nfindings",ha="center",va="center")
arr(ax,6.45,0.5,7.6,0.5); note(7.025,0.58,"hit / partial\nper reference\nissue; correct\nfindings",va="bottom")
arr(ax,8.675,2.15,8.675,1.5)
f.savefig("fig01_methods.pdf"); f.savefig("fig01_methods.png",dpi=300); f.savefig("fig01_methods.svg"); plt.close(f); print("ok")
