# QG-1: Laufplan fuer den 1D-Code (Runde 1)

Bearbeiter: Anthropic-Agent (Opus), Auftrag AUFTRAG-QG1-CODE.md. Beginn 2026-09-30 00:01:36 CEST (gemessen), Ende in der
letzten Zeile. Status: Code geschrieben, **ungetestet, nicht gerechnet**. Explorativ. Nach der Gegenlesung von Codex
(QG1-GEGENLESUNG-CODEX.md) und der Nachricht der Leitung (ca. 00:25) auf deren Parametrisierung ausgerichtet.

## Kurzfassung

- **Code:** qg1/qg1.py (PyTorch, float64 bzw. complex128, nur CUDA). Ein Aufruf rechnet alles: Profil durch Schiessen,
  27 Laeufe grob, dieselben 27 Laeufe fein, Auswertung.
- **Laufzeit auf der P5000:** etwa 1 Minute erwartet, Schaetzung 0,5 bis 3 Minuten. Grenze laut Auftrag 10 Minuten.
- **Vorhersage:** In A haengt der Fall stark von omega ab (R = 0,32 / 0,22 / 0,07), in B schwaecher (1,68 / 1,78 / 1,93).
  C ist universell (R = 1), die Zusatzkontrolle C2 ebenfalls (R = 2).
- **Bedeutung:** Der Lauf prueft ableitbare Sollwerte (Latte L4). Messen kann er nur Abweichungen durch endliche Groesse,
  Gezeiten, Anregung, Strahlung und Gitter.

## 1. Festlegungen (vor dem Lauf)

- **Modell:** L = |psi_t|^2 - |psi_x|^2 - U(S) mit S = |psi|^2 und U = S - S^2 + S^3/2, ein Kanal, d = 1.
  - Atlas und Codex meinen dasselbe Potential mit derselben Normierung. Geprueft habe ich zweierlei:
    - Das Atlasprofil erfuellt f'^2 = U(f^2) - omega^2 f^2. Das gilt nur ohne Faktor 1/2 vor den Ableitungstermen.
      Eingesetzt folgt genau b0^2 = 2 omega^2 - 1.
    - Codex' pde3d-Code rechnet dieselbe Gleichung psi_tt = Laplace psi - (1 - 2S + 1,5 S^2) psi.
- **Feld:** c(x) = 1 + g x mit g = 2e-4. Nach der Gegenlesung gilt Phi = g x / 2 (c = 1 + 2 Phi) und
  a_Newton = -dPhi/dx = -g/2.
- **Kopplung:** L = A |psi_t|^2 - B |psi_x|^2 - C U mit A = 1 + a Phi, B = 1 + b Phi, C = 1 + c Phi.
  Die Koeffizienten sind linear in Phi (schwaches Feld). Alle vier Varianten haben in erster Ordnung dieselbe
  Lichtgeschwindigkeit sqrt(B/A) = 1 + 2 Phi = c(x).

| Variante | a | b | c | Bedeutung | Soll R = a/a_Newton |
|---|---|---|---|---|---|
| B | -4 | 0 | 0 | nur Zeitterm (A = 1/c^2) | 4 W/E |
| C | -2 | 2 | 0 | volle Metrik (1+2 Phi) dt^2 - (1-2 Phi) dx^2, d = 1, gamma_PPN = 1 | 1 |
| C2 | -2 | 2 | 2 | Zusatzkontrolle: volle Metrik c^2 dt^2 - dx^2, gamma_PPN = 0 | 2 |

- **Warum C2:** A, B und C haben alle c = 0. Nur C2 prueft den Potentialkoeffizienten im Code. Das Licht ist dasselbe wie
  in C, der konforme Faktor ein anderer. Deshalb ist sein eigenes Newtonpotential 2 Phi, und es gilt R = 2 fuer alle omega.
- **Sollformel (Gegenlesung):** R = (-a W + b G + c V) / E.
  - Dabei ist W = omega^2 Int f^2, G = Int f'^2, V = Int U und E = W + G + V.
  - Das 1D-Virial W + G - V = 0 gibt E = 2 (W + G).
  - Analytischer Anker: I = sqrt(2) arcosh(1/b0), G = sqrt(a0)/2 - b0^2 I/4, W = omega^2 I, mit a0 = 1 - omega^2 und
    b0 = sqrt(2 omega^2 - 1).
  - Der Code rechnet R_soll aus dem Anker und zusaetzlich aus den Gittersummen des geschossenen Profils.
- **Profil:** Schiessen mit RK4 (h = 0,01, bis x = 80).
  - Vier Einschachtelungsrunden mit je 4096 Kandidaten, alle omega gleichzeitig.
  - Danach gespiegelt, unterhalb von 1e-3 f(0) exponentieller Schwanz.
  - Kontrolle gegen das Ankerprofil f^2 = 2 a0 / (1 + b0 cosh(2 sqrt(a0) x)).
- **Zeitentwicklung:** Velocity-Verlet, Box [-120, 120] mit Dirichlet-Rand, quadratische Daempfungsschicht ab |x| = 80
  (sigma0 = 1).
  - grob: dx = 0,1 und dt = 0,05; fein: dx = 0,05 und dt = 0,025.
  - Start: ruhendes geschossenes Profil bei x = 0 (psi = f, psi_t = -i omega f), das Feld wirkt ab t = 0.
- **Laeufe je Aufloesung (27):** vier Varianten mal drei omega mal (+g, -g), dazu g = 0 fuer jedes omega. Die Varianten
  sind bei g = 0 identisch. Alle Laeufe laufen als ein Stapel.
- **Messung** (alle 1,0 Zeiteinheiten, im Fenster +-40 um den Ladungsschwerpunkt):
  - Schwerpunkt X der erhaltenen Ladungsdichte rho = 2 A Im(psi conj(psi_t))
  - Ladung und Killing-Energie im Fenster, Ladung in der Box
  - Breite (Standardabweichung der Ladung) und max |psi|^2
- **Auswertung:**
  - Parabelfit von X(t) auf [T/16, T] = [25, 400].
  - R ist der ungerade Anteil (a(+g) - a(-g))/2, geteilt durch a_Newton.
  - Spaetfenster [200, 400] als Einschwingprobe.
  - Abstrahlung: 1 - Q_Fenster(T)/Q_Fenster(0), ebenso fuer die Energie.
  - Atmung: halbe Spannweite des Rests von Breite und max |psi|^2 um eine Parabel, relativ zum Mittel.

## 2. Aufruf (Leitung, auf der .69, nach VS-1 oder in einer Portionsluecke)

Vorschlag: qg1/qg1.py nach /home/fmh/fmhc-physics-remote/qg1-20260930/ kopieren. GPU-UUID und venv sind aus VS-1
(hauptlauf-kette.sh) uebernommen; bitte vor dem Start pruefen. Das Programm braucht nur torch und schreibt nur in --out.

Rauchtest mit T = 40:

```
flock -w 45 /home/fmh/fmhc-physics-remote/gauntlet-gpu.lock \
  systemd-run --user --collect --wait --pipe --unit=fmhc-physics-qg1-rauch-<HHMM> \
  -p CPUQuota=100% -p MemoryMax=4G -p RuntimeMaxSec=300 \
  -E CUDA_VISIBLE_DEVICES=GPU-127dc217-5693-98a2-3209-573ba346484f -E PYTHONDONTWRITEBYTECODE=1 \
  /home/fmh/fmhc-physics-gpu-venv/bin/python /home/fmh/fmhc-physics-remote/qg1-20260930/qg1.py \
  --T 40 --out /home/fmh/fmhc-physics-remote/qg1-20260930/rauchtest
```

Hauptlauf: derselbe Befehl mit `--unit=fmhc-physics-qg1-haupt-<HHMM>`, `RuntimeMaxSec=600`, ohne `--T` und mit
`--out /home/fmh/fmhc-physics-remote/qg1-20260930/ausgabe`.

- Der Rauchtest zeigt nur, ob das Programm durchlaeuft. Seine Zahlen gelten nicht, weil das Fitfenster zu kurz ist.
- Hochrechnung: Hauptlauf etwa gleich Schiessen plus zehnmal (Entwicklung grob + fein) aus dem Rauchtest. Das Programm
  gibt die Teilzeiten aus. Ergibt das mehr als 9 Minuten, nicht starten; die Leitung entscheidet.

## 3. Erwartete Laufzeit je Teil (Schaetzung fuer die P5000, nicht gemessen)

| Teil | Arbeit | erwartet |
|---|---|---|
| Start (Python, CUDA) | | 5 bis 15 s |
| Schiessen | 4 Runden x 8000 RK4-Schritte mit 3 x 4096 Kandidaten, dazu 8000 Schritte fuer die Profilbahn | 15 bis 60 s |
| Entwicklung grob | 8000 Verlet-Schritte, 27 Laeufe x 2401 Punkte | 5 bis 20 s |
| Entwicklung fein | 16000 Schritte, 27 x 4801 Punkte | 10 bis 60 s |
| Auswertung, Dateien | Fits auf CUDA, JSON, Zeitreihen | unter 5 s |
| **zusammen** | | **etwa 1 min, erwartet hoechstens 3 min** |

- Der Rauchtest dauert 25 bis 80 s; das Schiessen dominiert.
- Begruendung: Die Zeit bestimmen etwa 3,5 Millionen kleine GPU-Operationen, nicht die Arithmetik.

## 4. Ausgabedateien (im --out-Ordner)

- `qg1_bericht.txt`: lesbare Tabellen (Profil, R je Variante und omega, Kontrollen, Abweichungen), auch auf stdout
- `qg1_ergebnis.json`: alle Zahlen
  - Parameter, Profile mit Anker, Gittersummen je Aufloesung
  - je Variante und omega: R grob, R fein, R spaet, Sollwerte, Abstrahlung, Atmung, Fallweg
  - Kontrollen K0 bis K4, Abweichungen vom Soll
- `qg1_zeitreihen.pt`: Zeitreihen aller Laeufe (X, Q_Fenster, Q_Box, E_Fenster, Breite, S_max), Zeiten, Laufliste

## 5. Vorhersage (vor dem Rechnen)

Aus dem Anker von Hand gerechnet (ohne Interpreter); der Lauf rechnet sie nach. Q = 2 omega Int f^2.

| omega^2 | f(0)^2 = 1 - b0 | W/E | G/E | Q | E/Q | R_A = 4G/E | R_B = 4W/E | R_C | R_C2 |
|---|---|---|---|---|---|---|---|---|---|
| 0,55 | 0,683772 | 0,4196 | 0,0804 | 3,814 | 0,884 | 0,3217 | 1,6783 | 1 | 2 |
| 0,70 | 0,367544 | 0,4443 | 0,0557 | 2,441 | 0,941 | 0,2227 | 1,7773 | 1 | 2 |
| 0,90 | 0,105573 | 0,4827 | 0,0173 | 1,291 | 0,983 | 0,0694 | 1,9306 | 1 | 2 |

- **Spannweite ueber omega:** A 0,252, B 0,252 (in 1D gilt R_A + R_B = 2), C 0, C2 0.
- **In Worten:** In A faellt ein Q-Ball mit omega^2 = 0,55 etwa 4,6-mal so schnell wie einer mit omega^2 = 0,9.
- **Eoetvoes-Parameter** zwischen 0,55 und 0,9, eta = 2 |R1 - R2| / (R1 + R2): A 1,29, B 0,14.
  MICROSCOPE erlaubt 1e-15. Das ist nur Rahmen, denn unsere 1D-Q-Baelle sind keine Testmassen des Experiments.
- **Fallweg bis T = 400** (etwa 8 R): A 2,6 / 1,8 / 0,55; B 13 bis 15; C 8; C2 16. Hoechste Geschwindigkeit 0,04 R,
  also hoechstens 0,08.
- **Erwartete Abweichung vom Soll:** 1e-3 bis 1e-2 in R. Quellen:
  - Gitter, O(dx^2), etwa 1e-3
  - Einschwingen nach dem ploetzlichen Start
  - O(g x) und O(v^2), je hoechstens 0,3 Prozent
- **Abstrahlung:** unter 1e-4 der Ladung im Fenster.
- **Atmung** (relative Schwingung der Breite): 1e-4 bis 1e-3. Ein Teil davon stammt schon bei g = 0 aus dem Gitterabgleich;
  den Anteil des Feldes zeigt der Vergleich mit g = 0.
- **Profil:** max |f_Schuss - f_Anker| unter 1e-6.

## 6. Kontrollen (fest vor dem Lauf)

- **K0 Profil:** max |f_Schuss - f_Anker| <= 1e-6 auf beiden Gittern.
- **K1 C universell:** max |R_C - 1| <= 0,02 und max |R_C2/2 - 1| <= 0,02 (fein).
- **K2 g = 0:** |a| / |a_Newton| <= 1e-3.
- **K3 -g:** |a(+g) + a(-g)| <= 0,05 |a(+g) - a(-g)|. Die Laeufe +g und -g sind exakte Spiegelbilder; K3 prueft nur die
  Symmetrie des Codes.
- **K4 (Latte L3):** Die omega-Spannweite von R_A (fein) ist mindestens fuenfmal so gross wie die groesste Aenderung
  |R_fein - R_grob| ueber alle Varianten und omega.
- **Diagnose ohne Schwelle:** |R_spaet - R| (Einschwingen), Zittern der Bahn um die Parabel, Ladungsverlust der Box.
- **Befund-Kandidat:** |R_fein - R_soll| > 0,03; der Bericht listet solche Faelle.

## 7. Was welches Ergebnis bedeuten wuerde

- **Alle Kontrollen bestanden, alle R innerhalb 0,03 vom Soll:** Die Papierrechnung gilt in unserem 1D-Modell.
  - Neu ist das nicht (L4: vorab ableitbar). Neu sind nur die Zahlen zu Abstrahlung und Atmung.
- **K1 scheitert, K0 und K2 bis K4 bestehen:**
  - Zuerst den Code verdaechtigen (Koeffizienten A, B, C, Messung).
  - Bleibt die Abweichung im Spaetfenster und auf dem feinen Gitter, ist sie ein Befund-Kandidat gegen die
    Papierrechnung. Dann liest ein zweites Haus.
- **A kommt universell heraus** (Spannweite unter dem Fuenffachen der Aenderung): widerspricht der Papierrechnung;
  Befund-Kandidat.
- **R_A oder R_B weicht um mehr als 0,03 ab, C besteht:** Ein nicht adiabatischer Effekt wirkt (Strahlung, innere Moden,
  endliche Groesse). Befund-Kandidat; zuerst Spaetfenster, T und g variieren.
- **|R_spaet - R| > 0,03:** Das Einschwingen nach dem ploetzlichen Start zaehlt; die Zahlen sind dann nur grob.
- **K0, K2 oder K3 scheitert:** Codefehler, keine Aussage.
- **K4 scheitert:** Die Numerik reicht nicht, keine Aussage; feiner neu rechnen.
- **Abstrahlung ueber 1e-3 oder Atmung ueber 1e-2 in A oder B, nicht aber in C und bei g = 0:** Die nicht metrische
  Kopplung regt den Q-Ball an. Das ist zweitrangig, aber eine echte Messung des Laufs.

## 8. Grenzen

- **Ableitbarkeit:** Der numerische Lauf prueft ableitbare Sollwerte (Latte L4). Er misst nur Abweichungen durch endliche
  Groesse, Gezeiten, Anregung, Strahlung und Gitter.
- **Aufbau:** 1D, ein Kanal, Testkoerper in einem schwachen linearen Feld, das von aussen vorgegeben ist (keine Quelle,
  keine Rueckwirkung).
  universell" bliebe gleich.
- **Andere Gradientenabschluesse:** B = 1 + beta Phi gibt R = beta G/E. Die Skala aendert sich, die omega-Abhaengigkeit
  bleibt.
  einen universellen Fall braucht.
- **Erste Ordnung:** C und C2 sind nur bis zur ersten Ordnung in Phi Metriken (lineare Koeffizienten). Am Q-Ball ist
  Phi hoechstens 0,002, die zweite Ordnung also vernachlaessigbar.
- **Ungetestet:** Der Code ist nicht gelaufen, deshalb zuerst der Rauchtest.

## Latten (Vorschlag, die Leitung entscheidet)

| Latte | Einschaetzung |
|---|---|
| L1 kann scheitern | ja: C kann R = 1 verfehlen, A kann universell herauskommen |
| L2 Gegenprobe | ja: C, C2, g = 0, -g |
| L3 Numerik | geplant: fein gegen grob, Faktor 5 |
| L4 schon bekannt | weitgehend: Sollwerte ableitbar; Literatur zu Solitonen in inhomogenen Medien ist wahrscheinlich, nicht gesucht |
| L5 Messbezug | nur mittelbar: MICROSCOPE 1e-15 als Rahmen |

## Einfach gesagt

Wir lassen am Rechner einen kleinen Feldklumpen, einen Q-Ball, in einem "Brechungsfeld" fallen, in dem Licht zu einer
Seite hin langsamer wird. Wir probieren drei Arten, wie das Feld auf den Klumpen wirkt: nur auf seine raeumliche Form
fallen die Klumpen nur im dritten Fall alle gleich schnell; im ersten Fall faellt einer je nach Innentakt fast fuenfmal
so schnell wie ein anderer. Der Rechenlauf kontrolliert vor allem diese Zahlen, die man schon vorher ausrechnen kann;
spannend wird er nur, wenn er davon abweicht. Gerechnet ist noch nichts; der Lauf soll etwa eine Minute dauern.

Ende der Bearbeitung: 2026-09-30 00:29:38 CEST (gemessen mit date).
