# TETRA-KETTE: Plan (Code-Agent fuer die Leitung claude-primary, Runde 26)

- Auswerteregeln (Abschnitte 1 bis 5) geschrieben ab 2026-10-03 04:06:35 CEST (date), vor dem Rauchlauf und vor jeder
  echten Rechnung. Der Rauchlauf-Abschnitt (6) und die Pruefsummen (7) kommen danach, vor dem Einfrieren.
- Karte: KARTE.md (unveraendert). Die Vorhersagen TKe0 bis TKe3 und ihre Bedeutung stehen dort fest.
- Code: code/tetra_kette.py (Modell und Loeser), code/auswertung.py (mechanische Urteile).

## 1. Modell (wie Karte und TETRA-STAB)

- Tetrahelix nach Boerdijk und Coxeter mit Kantenlaenge 1: v_n = (rho cos n th, rho sin n th, n h), th = arccos(-2/3),
  rho = 3 sqrt(3)/10, h = 1/sqrt(10). Je vier aufeinanderfolgende Ecken bilden ein regulaeres Tetraeder; alle Staebe
  (i, i+1), (i, i+2), (i, i+3) haben Laenge 1. Der Code prueft das (Kantenabweichung, Volumen je Tetraeder gegen
  1/(6 sqrt 2)).
- M = 12: 15 Ecken, 39 Staebe. B = 1, L = 1, Ks = 25600, Energieformen wie TETRA-STAB.
- Verbinder: Lage plus Drehvektor, Drehung exp(schief(r)) als Potenzreihe 24. Ordnung (glatt fuer die Hesse-Matrix).
- Einspannrichtungen im Bezug: gerade Kantenrichtungen (alpha_0 = 0). Defekt: Stab (v_0, v_1) an beiden Enden um
  alpha_d = 10 Grad zur Mitte von v_0 bis v_3 geneigt (Neigungsebene wie TETRA-STAB: Kante und Mitte).
- Lagerung: v_14 fest (Lage und Drehung), alle anderen Verbinder frei.
- Loeser: Energie, Gradient und Hesse-Matrix je Stab gebuendelt (torch.func.vmap, grad, hessian), global dicht
  zusammengesetzt. Gedaempfter Newton ab dem geraden Bezugszustand (Cholesky, bei Bedarf verschoben, Armijo-Rueckschritt),
  Abbruch bei |grad| < 1e-13 oder am Rundungsboden (kein Fortschritt mehr bei |grad| < 1e-8). Kein L-BFGS noetig.
- Kraefte und Momente je Stabende wie TETRA-STAB: F = -dE_Stab/dX, tau = -d x dE_Stab/dd. Axialkraft entlang der Sehne,
  positiv = Zug.

## 2. Laeufe (echt)

| Lauf | M | N | alpha_d | alpha_0 | fest | Zweck |
|---|---|---|---|---|---|---|
| k0_10 | 12 | 10 | 0 | 0 | v_14 | TKe0 |
| k0_16 | 12 | 16 | 0 | 0 | v_14 | TKe0 |
| d_10 | 12 | 10 | 10 | 0 | v_14 | TKe1 bis TKe3, Hesse-Eigenwerte |
| d_16 | 12 | 16 | 10 | 0 | v_14 | TKe1 bis TKe3, Hesse-Eigenwerte |
| d_10_m16 | 16 | 10 | 10 | 0 | v_18 | Randkontrolle (Einfluss des festen Endes) |
| g_20 | 1 | 20 | 10 | 5 | v_0 | Gegenprobe: exakt der TETRA-STAB-Defektfall d_20 |

- Gegenprobe g_20: Ein Tetraeder (M = 1) hat dieselben sechs Staebe in derselben Reihenfolge wie TETRA-STAB (AB AC AD BC
  BD CD = (0,1) (0,2) (0,3) (1,2) (1,3) (2,3)), Grundneigung 5 Grad, Defekt AB 10 Grad, Verbinder A = v_0 fest, N = 20.
  Die Loesung haengt nicht von der Startgeometrie ab (dort Kante a_soll, hier 1).
- Jeder Lauf ueber kleintest.sh (CPU-Spuren cpu, cpu2, cpu3, cpu4, cpu6), Laufordner auf der .69:
  /home/fmh/fmhc-physics-remote/runde26-tetra-kette/lauf/. Danach auswertung.py ueber eine Spur.

## 3. Messgroessen und Zuordnung

- Je Stabende: |tau|, |F|, Axialkraft. Im Bezugszustand sind alle null, also ist "Aenderung gegen den Bezug" der Betrag
  selbst.
- **Zuordnung Stab -> Tetraeder (gewertet): eindeutig, kleinstes k, das beide Ecken enthaelt, k = max(0, j - 3).**
  - Tetraeder 0 bekommt seine sechs Staebe (mit dem Defektstab), Tetraeder k >= 1 die drei Staebe zur neu
    hinzukommenden Ecke v_(k+3): (k, k+3), (k+1, k+3), (k+2, k+3). Jeder Stab zaehlt genau einmal (6 + 3 x 11 = 39).
  - Grund: Bei der Mitgliedschafts-Zuordnung (jeder Stab in allen Tetraedern, die ihn enthalten) kann dasselbe Stabende
    das Maximum zweier Nachbartetraeder liefern. Dann gibt es Gleichstaende, und "streng monoton" waere kuenstlich
    verletzt.
- T_k = groesstes |tau| ueber beide Enden der zugeordneten Staebe; F_k = groesstes |F| ebenso.
- Nicht gewertet, nur berichtet: T_k nach Mitgliedschaft (alle sechs Staebe von v_k bis v_(k+3)), T je Ecke, Fit der
  Kraefte, log-log-Fit, dominante Axialkraft je Tetraeder, Reaktion am festen Verbinder, Hesse-Eigenwerte.
- **Messschwelle s** je Lauf: max(1e-9, 100 x groesster Gleichgewichtsrest (Kraft- oder Momentsumme) der freien
  Verbinder). Werte unter s gelten als nicht gemessen.

## 4. Urteile (mechanisch, auswertung.py)

- **TKe0:** in k0_10 und k0_16 alle |tau| und |F| (beide Enden aller 39 Staebe) < 1e-8. Beide muessen gelten.
- **TKe1:** T_0 > T_1 > ... streng fallend ab k = 0, alle Werte ueber s; die Laenge dieser Folge (Anzahl Tetraeder) muss
  >= 6 sein (also mindestens T_0 > ... > T_5).
- **TKe2:** Kleinste Quadrate fuer ln T_k = a + b k ueber k = 2 bis 8 (nur Werte ueber s; mindestens 5 Punkte, sonst
  "nicht entscheidbar"). Eingetroffen, wenn R^2 > 0,95 und das Verhaeltnis je Tetraeder q = exp(-b) zwischen 2 und 30
  liegt. Abklinglaenge = 1/ln q (in Tetraedern).
- **TKe3:** Je Stabfamilie f = 1, 2, 3 (Staebe (i, i+f)) die Axialkraefte der Staebe ausserhalb von Tetraeder 0
  (k >= 1, also j >= 4), nach i geordnet, nur |Axialkraft| > s. Eingetroffen, wenn in mindestens einer Familie zwei
  aufeinanderfolgende Werte verschiedenes Vorzeichen haben.
  - Grund fuer "ausserhalb von Tetraeder 0": Schon in TETRA-STAB hatte das Defekt-Tetraeder Zug (AB, CD) und Druck
    (Nachbarn) in derselben Familie. Mit Tetraeder 0 waere TKe3 fast sicher und "entlang der Kette" nicht geprueft.
- **Gitter:** Jedes Urteil TKe1 bis TKe3 wird an d_10 und an d_16 gefaellt. Gleich: dieses Urteil. Verschieden:
  "uneinheitlich (Gitter)", keine Bedeutung ausgeloest.

## 5. Kontrollen

- TKe0 (ohne Defekt) bei N = 10 und 16.
- Gitter: groesste relative Abweichung von T_k zwischen N = 10 und 16 fuer k = 0 bis 8 (erwartet < 1e-2; berichtet).
- Randkontrolle: T_k von M = 12 gegen M = 16 (N = 10) fuer k = 0 bis 8 (erwartet < 1e-2; berichtet). Weicht es mehr ab,
  wirkt das feste Ende bis in den Fitbereich hinein.
- Gleichgewicht je Verbinder: Kraft- und Momentsumme der freien Verbinder; Reaktion am festen Verbinder.
- Gegenprobe g_20 gegen TETRA-STAB d_20: groesste absolute Abweichung von |tau| (beide Enden), Axialkraft und
  Sehnenlaenge der sechs Staebe; "reproduziert", wenn < 1e-6.
- Hesse-Matrix (d_10, d_16): kleinste Eigenwerte; positiv heisst stabiles Gleichgewicht.

## 6. Rauchlauf (vor dem Einfrieren, Parameter in keinem echten Lauf), ab 04:08:50 CEST eingetragen

- 02:07:31 bis 02:07:49 UTC, Spuren cpu und cpu2, beide rc = 0, je ~12 s. Daten in rauch-69/.
- **rauch1:** M = 4, N = 6, alpha_d = 7 Grad, v_6 fest, mit Hesse-Matrix.
  - Newton in 7 Schritten bis zum Rundungsboden, |grad| 9,6e-11, Verschiebung mu nie noetig.
  - Gleichgewichtsrest der freien Verbinder: Kraft <= 2,2e-11, Moment <= 1,2e-14. Kantenabweichung 2,2e-16, Volumen
    7e-16 relativ.
  - Kleinster Hesse-Eigenwert 0,064 (positiv).
  - T_k (k = 0 bis 3): 0,221; 0,0835; 0,0115; 0,0075. Damit kenne ich den Verlauf nahe am Defekt in einer kurzen Kette
    mit festem Ende bei v_6 schon vor den echten Laeufen (offengelegt). Die Auswerteregeln (Abschnitte 1 bis 5) standen
    vorher fest und bleiben unveraendert.
- **rauch2 (Code-Pruefung):** M = 1, N = 40, Grundneigung 3 Grad, Defekt 6 Grad, v_0 fest: dieselben Parameter wie der
  TETRA-STAB-Rauchlauf r3c.
  - Alle sechs Staebe stimmen ueberein: |tau| auf <= 6,3e-10, Axialkraft auf <= 3e-9, Sehnenlaenge auf <= 8e-12.
  - Der gebuendelte Code rechnet also dasselbe Modell wie tetra_stab.py.
- Keine Aenderung an Modell, Code oder Regeln nach dem Rauchlauf. Die Spur bricht jeden Lauf nach 600 s ab; ein
  abgebrochener Lauf wird offengelegt und nicht gewertet.

## 7. Einfrieren

- Code-Pruefsummen (sha256), lokal und auf der .69 gleich:
  - code/tetra_kette.py: 665af77b75e63700bc8913b52453acabfd741fc640428a6ec0077ff1b1beb024
  - code/auswertung.py: 1e4ee4e0d98210ffba41178ac65d23ef34df2e0a81210bf67c33865baaf406e8
  - Referenz lauf/ref_tetra_stab_d_20.json (= RUNDE-24/tetra-stab/lauf-69/d_20.json):
    582cbd88afb6cf7fd631f9f61c5d3981929f1f9cca6c1246ab6f66d13428037b
- Eingefroren als PLAN.md.eingefroren-<Zeit> und code/*.eingefroren-<Zeit>, schreibgeschuetzt, vor dem ersten echten Lauf.
