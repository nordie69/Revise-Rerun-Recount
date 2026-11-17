#!/usr/bin/env python3
"""Erzeugt die Zeilen der Vorstudie für hauptstudie/Laufregister.md.

Aufruf aus dem Projektordner: python3 hauptstudie/tools/laufregister_vorstudie.py
Liest die Ordner unter erprobung/ und rechnet SHA-256 von PDF, Gutachten und Paketen
frisch. Feste Angaben (Datum, Aufbau, Agentenzahl, Verifikation) stammen aus dem Log
L-10 bis L-24 und stehen unten in LAEUFE.
"""
import glob
import hashlib
import os

P = {
    "1.0.0": ("paket/science-review-gutachten_v1_20261015.skill",
              "abbildungen/paket/science-review-abbildungen_v1_20261015.skill",
              "studiendesign/paket/science-review-studiendesign_v1_20261015.skill"),
    "1.1.0": ("paket/science-review-gutachten_v1_20261016.skill",
              "abbildungen/paket/science-review-abbildungen_v1_20261016.skill",
              "studiendesign/paket/science-review-studiendesign_v1_20261016.skill"),
    "1.3.0/1.2.0/1.2.0": ("paket/science-review-gutachten_v1_20261016_3.skill",
              "abbildungen/paket/science-review-abbildungen_v1_20261016_2.skill",
              "studiendesign/paket/science-review-studiendesign_v1_20261016_2.skill"),
}
# Kennung, Durchgang, Ordner, Manuskript, Wiederholung, Datum, Version, Aufbau, Agenten, Verifikation
LAEUFE = [
    ("V1-LAM-1", 1, "durchgang1/LAM1", "LAM", 1, "2026-10-15", "1.0.0", "nacheinander", "1", "verifikation1/LAM1_verifikation.md"),
    ("V1-LAM-2", 1, "durchgang1/LAM2", "LAM", 2, "2026-10-15", "1.0.0", "nacheinander", "1", "keine"),
    ("V1-TCD-1", 1, "durchgang1/TCD", "TCD", 1, "2026-10-15", "1.0.0", "nacheinander", "1", "verifikation1/TCD_verifikation.md"),
    ("V1-HOR-1", 1, "durchgang1/HOR", "HOR", 1, "2026-10-15", "1.0.0", "nacheinander", "1", "verifikation1/HOR_verifikation.md"),
    ("V2-LAM-1", 2, "durchgang2/LAM", "LAM", 1, "2026-10-15", "1.0.0", "getrennt", "8", "verifikation2/LAM_verifikation.md"),
    ("V2-TCD-1", 2, "durchgang2/TCD", "TCD", 1, "2026-10-15", "1.0.0", "getrennt", "8", "verifikation2/TCD_verifikation.md"),
    ("V2-HOR-1", 2, "durchgang2/HOR", "HOR", 1, "2026-10-15", "1.0.0", "getrennt", "8", "verifikation2/HOR_verifikation.md"),
    ("V3-LAM-1", 3, "durchgang3/LAM_A", "LAM", 1, "2026-10-16", "1.1.0", "getrennt", "8", "verifikation3/LAM_A_verifikation.md"),
    ("V3-LAM-2", 3, "durchgang3/LAM_B", "LAM", 2, "2026-10-16", "1.1.0", "getrennt", "8", "verifikation3/LAM_B_verifikation.md"),
    ("V3-TCD-1", 3, "durchgang3/TCD", "TCD", 1, "2026-10-16", "1.1.0", "getrennt", "8", "verifikation3/TCD_verifikation.md"),
    ("V3-HOR-1", 3, "durchgang3/HOR", "HOR", 1, "2026-10-16", "1.1.0", "getrennt", "8", "verifikation3/HOR_verifikation.md"),
    ("V4-LAM-1", 4, "durchgang4/LAM_A", "LAM", 1, "2026-10-16", "1.3.0/1.2.0/1.2.0", "getrennt", "8", "verifikation4/LAM_A_verifikation.md"),
    ("V4-LAM-2", 4, "durchgang4/LAM_B", "LAM", 2, "2026-10-16", "1.3.0/1.2.0/1.2.0", "getrennt", "8", "verifikation4/LAM_B_verifikation.md"),
    ("V4-TCD-1", 4, "durchgang4/TCD", "TCD", 1, "2026-10-16", "1.3.0/1.2.0/1.2.0", "getrennt", "8", "verifikation4/TCD_verifikation.md"),
    ("V4-HOR-1", 4, "durchgang4/HOR", "HOR", 1, "2026-10-16", "1.3.0/1.2.0/1.2.0", "getrennt", "8", "verifikation4/HOR_verifikation.md"),
]


def sha(pfad, n=12):
    with open(pfad, "rb") as fh:
        return hashlib.sha256(fh.read()).hexdigest()[:n]


def main():
    for k, dg, ordner, ms, wdh, datum, ver, aufbau, agenten, verif in LAEUFE:
        o = os.path.join("erprobung", ordner)
        pdf = glob.glob(os.path.join(o, "*.pdf"))
        gut = glob.glob(os.path.join(o, "*_Gutachten_*.md"))
        assert len(pdf) == 1 and len(gut) == 1, (o, pdf, gut)
        pakete = ", ".join(sha(p) for p in P[ver])
        if verif != "keine":
            assert os.path.isfile(os.path.join("erprobung", verif)), verif
            verif = f"`erprobung/{verif}`"
        print(f"| {k} | {datum} | Vorstudie D{dg} | {ms} | {wdh} | {ver} | {pakete} | {aufbau} | "
              f"claude-opus-5-5 konfiguriert, bedienendes Modell nicht festgehalten | nicht festgehalten | {agenten} | "
              f"`erprobung/{ordner}/` | {sha(pdf[0])} | {sha(gut[0])} | {verif} |")


if __name__ == "__main__":
    main()
