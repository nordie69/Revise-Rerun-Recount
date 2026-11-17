# Erkennung der Randzeilen je Fassung

Jedes PDF des Testkorpus, gelesen mit `einlesen.py` der Fassungen 1.0.0 bis 1.5.0 von `science-review-gutachten`. "ja" heißt: Randzeilen erkannt, `text.json` folgt den gedruckten Randnummern; "nein" heißt: Zeilen je Seite gezählt. Bedingung A las mit 1.0.0, B und C mit 1.3.0, D mit 1.4.0; der zweite Teil zeigt, ob die Fassungen dieselbe `text.json` liefern. Gerechnet mit `tools/randzeilen_vergleich.py`.

| Datei | 1.0.0 | 1.1.0 | 1.2.0 | 1.3.0 | 1.4.0 | 1.5.0 |
|---|---|---|---|---|---|---|
| egusphere-2025-4506.pdf | nein | nein | nein | nein | nein | ja |
| egusphere-2025-4695.pdf | ja | ja | ja | ja | ja | ja |
| egusphere-2025-4733.pdf | ja | ja | ja | ja | ja | ja |
| egusphere-2025-5046-supplement.pdf | nein | nein | nein | nein | nein | nein |
| egusphere-2025-5046.pdf | nein | nein | nein | nein | nein | ja |

| Datei | `text.json` von 1.0.0 bis 1.4.0 gleich | `text.json` 1.5.0 gleich 1.4.0 |
|---|---|---|
| egusphere-2025-4506.pdf | nein | nein |
| egusphere-2025-4695.pdf | nein | ja |
| egusphere-2025-4733.pdf | nein | ja |
| egusphere-2025-5046-supplement.pdf | ja | ja |
| egusphere-2025-5046.pdf | nein | nein |
