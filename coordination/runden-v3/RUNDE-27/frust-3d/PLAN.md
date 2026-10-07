# FRUST-3D: Plan (Code-Agent fuer die Leitung claude-primary, Runde 27)

- Abschnitte 1 bis 5 (Modell, Laeufe, Messgroessen, Urteile, Kontrollen) geschrieben ab 2026-10-03 05:28:38 CEST (date).
  Die Rauchlaeufe (Abschnitt 6) wurden um 03:28:22 UTC (05:28:22 CEST) gestartet, kurz vor diesem Text; ihre Ausgaben
  habe ich erst nach dem Schreiben der Abschnitte 1 bis 5 gelesen. Abschnitt 6 und die Pruefsummen (7) kommen danach,
  vor dem Einfrieren.
- Karte: KARTE.md (unveraendert). Die Vorhersagen F0 bis F3 und ihre Bedeutung stehen dort fest.
- Code: code/frust_3d.py (Modell und Loeser, nach RUNDE-26/tetra-kette/code/tetra_kette.py), code/auswertung.py
  (mechanische Urteile).

## 1. Modell

- **Geometrie:** Achse A = (0, 0, 1/2), B = (0, 0, -1/2); Ring r_0 bis r_4 in der Ebene z = 0, Radius
  R = 1/(2 sin 36 Grad) = 0,85065 (Ringstaebe 1). Staebe: Achse AB (1), Speichen A-r_k und B-r_k (10), Ring r_k-r_(k+1)
  (5). Alle Ruhelaengen 1. Am Start sind die Speichen-Sehnen 0,98673, also gedrueckt; spannungsfrei waere die Achse
  1,05146.
- **Stab:** wie TETRA-STAB/TETRA-KETTE, B = 1, L = 1, Ks = 25600, N Segmente, keine Torsion. Dehnung
  (Ks/2) Summe (|e| - l0)^2/l0, Biegung (B/l0) Summe (1 - t_i . t_(i+1)).
- **(G) Gelenke:** Die Verbinder sind Punkte (nur Lage). Die Stabenden sind frei drehbar, es gibt keine Einspannterme.
  - Lager: A fest, B in x und y, r_0 in y. Das sind sechs Komponenten, die nur die Starrkoerperbewegung nehmen
    (statisch bestimmt). Ihre Reaktionen muessen null sein (Kontrolle).
- **(E) Einspannung:** Die Verbinder sind starre Koerper (Lage plus Drehvektor, exp(schief(r)) als Potenzreihe 24.
  Ordnung) und frei drehbar. Jedes Stabende ist in seiner Wunschrichtung eingespannt, Term (2B/l0)(1 -+ d . t) wie
  TETRA-STAB. Lager: A fest (Lage und Drehung).
- **Wunschrichtungen (gewertet: M = Mittel der regulaeren Tetraeder):**
  - Fuenf regulaere Tetraeder (A, B, c_k, d_k) stehen in 72-Grad-Schritten um AB. Jedes ueberstreicht 70,53 Grad; die
    7,36-Grad-Luecke ist damit gleichmaessig auf die fuenf Fugen verteilt (je 1,47 Grad).
  - Die Ringecke r_k hat zwei Bilder: c_k (in Tetraeder k) und d_(k-1) (in Tetraeder k-1), bei 72 k +- 0,74 Grad.
  - Einspannrichtung je Stabende = normiertes Mittel der Kantenrichtungen in allen Tetraedern, die den Stab enthalten.
    Die Achse liegt in allen fuenf, eine Speiche in zwei, ein Ringstab in einem.
  - Ergebnis: Bei A stehen die Speichen 60 Grad gegen die Achse und in gleichen 72-Grad-Schritten. Benachbarte Speichen
    bilden 61,2 statt 60 Grad. Am Ring liegen die Ringstaebe in der Ringebene mit dem Fuenfeckwinkel 108 Grad.
  - Fuer offene Anordnungen (1 und 4 Tetraeder, Schritt = Diederwinkel) liefert dieselbe Regel die exakten Kanten.
  - Nur berichtet (nicht gewertet), Variante K: Kantenrichtungen der geschlossenen Bipyramide mit Achse 1,05146
    (Speichen und Ring 1). Dort sind die Einspannungen mit geraden Staeben vertraeglich, nur die Achse ist zu kurz.
- **Ast und Anstoss:**
  - Die gerade Lage ist bei gedrueckten Staeben eine Verzweigung. Am Start bekommt jeder der 16 Staebe eine halbe
    Sinuswelle quer zur Sehne, Amplitude 1e-3 L.
  - "aus" (gewertet fuer G): Speichen in ihrer Meridianebene von der Achse weg, Ringstaebe in der Ringebene nach aussen,
    Achse in +x.
  - "ein" (nur berichtet): alles umgekehrt. Bei Gelenken ist die Knickrichtung jeder Speiche frei (Drehung um die
    Sehne kostet nichts). "ein" muss daher dieselbe Energie und dieselben Kraefte liefern (Kontrolle).
  - Bei E waehlen die Einspannungen den Ast selbst. Gerechnet wird E ohne Anstoss ("keine") und mit "aus".
    Gewertet wird je N der Zustand mit der kleineren Energie unter den stabilen (kleinster Hesse-Eigenwert > -1e-6).
- **Loeser:**
  - Energie, Gradient und Hesse-Matrix je Stab gebuendelt (torch.func.vmap, grad, hessian), global dicht.
  - Gedaempfter Newton: Cholesky von H + mu I mit einer kleinen Grundverschiebung mu = 1e-10 max|diag H|, bei
    Fehlschlag x10. Armijo-Rueckschritt; findet er keinen Abstieg, wird mu vergroessert.
  - Abbruch bei |grad| < 1e-13 oder am Rundungsboden (kein Fortschritt mehr bei |grad| < 1e-8). Hoechstens 300
    Schritte je Phase.
  - Die Grundverschiebung ist neu gegen TETRA-KETTE. Grund: Bei G hat die Hesse-Matrix im geknickten Zustand exakte
    Nullrichtungen (Drehung jeder geknickten Speiche um ihre Sehne).
  - **Sattelflucht (nach dem Rauchlauf ergaenzt, Abschnitt 6):** Ist der kleinste Hesse-Eigenwert am Ende einer Phase
    < -1e-6, ist das Gleichgewicht ein Sattel. Dann folgt ein Stoss entlang des zugehoerigen Eigenvektors (groesste
    Komponente 1e-2, sonst 3e-3, 1e-3, 3e-4, 1e-4; Vorzeichen und Groesse: die erste, die die Energie senkt) und eine
    neue Newton-Phase. Hoechstens 6 Stoesse. Eine interne Zeitgrenze von 480 s schreibt vor dem Abbruch der Spur.
  - "Stabil" heisst: kleinster Hesse-Eigenwert > -1e-6. Das gilt fuer G und E.
- **Kraefte und Momente** je Stabende wie TETRA-STAB: F = -dE_Stab/dX, tau = -d x dE_Stab/dd (nur E). Axialkraft
  entlang der Sehne, positiv = Zug. Moment im Stab: (B/l0) sin theta am inneren Knoten (Wendewinkel theta).

## 2. Laeufe (echt)

| Lauf | Tetraeder | N | Lagerung | Wunsch | Anstoss | Zweck |
|---|---|---|---|---|---|---|
| k1_G_12, k1_G_20 | 1 | 12, 20 | G | M | aus 1e-3 | F0 |
| k1_E_12, k1_E_20 | 1 | 12, 20 | E | M | aus 1e-3 | F0 |
| k4_G_12, k4_G_20 | 4 offen | 12, 20 | G | M | aus 1e-3 | F0 |
| k4_E_12, k4_E_20 | 4 offen | 12, 20 | E | M | aus 1e-3 | F0 |
| g_12, g_20 | 5 | 12, 20 | G | M | aus 1e-3 | F1, F2, F3 |
| g_ein_20 | 5 | 20 | G | M | ein 1e-3 | Kontrolle (Knickrichtung frei) |
| e_12, e_20 | 5 | 12, 20 | E | M | keine | F3 |
| e_aus_12, e_aus_20 | 5 | 12, 20 | E | M | aus 1e-3 | F3 (Astprobe) |
| ek_12, ek_20 | 5 | 12, 20 | E | K | keine | nur berichtet (Variante K) |

- Alle mit Hesse-Eigenwerten. Achse-Ruhelaenge 1 in allen echten Laeufen.
- Das feine Gitter war vor dem Rauchlauf N = 24. Ich habe es nach dem Rauchlauf wegen der Laufzeit auf N = 20 gesetzt
  (Abschnitt 6).
- Jeder Lauf ueber kleintest.sh (Spuren cpu, cpu2, cpu3, cpu4, cpu6), Laufordner
  /home/fmh/fmhc-physics-remote/runde27-frust-3d/lauf/. Danach auswertung.py ueber eine Spur.
- Die Spur bricht nach 600 s ab. Ein abgebrochener Lauf wird offengelegt und nicht gewertet; fehlt ein gewerteter Lauf,
  ist das betroffene Urteil "nicht entscheidbar".

## 3. Messgroessen

- Je Stab: Axialkraft (beide Enden), Querkraft, |tau| an beiden Enden (E), groesstes Moment im Stab, Stich (groesster
  Abstand der inneren Knoten von der Sehne), Sehne, Bogenlaenge, Abweichung von der Einspannrichtung (E), Verhaeltnis
  Druck / Euler-Last pi^2 B/L^2, Energie (Dehnung, Biegung innen, Einspannung).
- Je Stabart (Achse, Speichen, Ring): dieselben Groessen als Mittel, Kleinst- und Groesstwert.
- Gesamt: Energie, Anteile; Achsenlaenge |AB|; Ringradius = Abstand jeder Ringecke von der Geraden AB.
- **Biegung** = Biegung innen + Einspannterm (beides Kruemmungsenergie des Stabs). Dehnung = der Rest.
- **Messschwelle s** je Lauf: max(1e-9, 100 x groesster Gleichgewichtsrest der freien Komponenten (Kraft oder Moment)).

## 4. Urteile (mechanisch, auswertung.py)

- **F0:** In allen acht Kontrolllaeufen (k1, k4; G und E; N = 12 und 20) gilt fuer beide Enden aller Staebe |F| < 1e-8
  und |tau| < 1e-8. Alle muessen gelten.
- **F1** (g_12, g_20): Achse Axialkraft > s (Zug) und alle 10 Speichen < -s und alle 5 Ringstaebe < -s (Druck).
- **F2** (g_12, g_20): Es gibt eine Stabart, deren Staebe alle gedrueckt sind (Axialkraft < -s) und deren Stich bei
  allen Staeben dieser Art > 0,01 L ist. Berichtet wird auch die schwaechere Lesart "ein Stab".
- **F3** (je N): E_E = Energie des gewerteten E-Zustands (Abschnitt 1, Ast), E_G = kleinste Energie der G-Laeufe bei
  diesem N (N = 20: g_20 und g_ein_20). Eingetroffen, wenn E_E > E_G und der Biegeanteil von E_E > 0,80 ist.
- **Gitter:** Jedes Urteil F1 bis F3 wird bei N = 12 und N = 20 gefaellt. Gleich: dieses Urteil. Verschieden:
  "uneinheitlich (Gitter)", keine Bedeutung ausgeloest.
- Trifft F1 nicht ein, wird nach Karte das Vorzeichenmuster beschrieben, mit dem gemessenen Eigenspannungsvektor
  (Axialkraft je Art durch die Achsenkraft) und dem Gelenkwerk-Gleichgewicht als Formel:
  t_Speiche/t_Achse = -2 l_s/(5 h), t_Ring/t_Achse = 2 l_r/(5 h (1 - cos 72 Grad)), mit h, l_s, l_r aus dem Lauf.

## 5. Kontrollen (berichtet)

- F0-Laeufe (1 und 4 Tetraeder): Diese Anordnungen sind spannungsfrei moeglich; der Anstoss muss verschwinden.
- Gleichgewicht je Verbinder (freie Komponenten) und Reaktionen an den Lagern (muessen null sein: in sich
  ausgeglichen).
- G: Querkraft an den Stabenden (Gelenk heisst Endkraft entlang der Sehne).
- Gitter N = 12 gegen 20: relative Abweichung von Energie, Axialkraft je Art, Stich je Art, Achse, Ringradius.
- Knickrichtung: g_ein_20 gegen g_20 (Energie, Kraefte). Ast: e gegen e_aus.
- Hesse-Matrix: kleinste Eigenwerte. Bei G werden bis zu 10 Nullrichtungen erwartet (Drehung der geknickten Speichen).
- Schreibtisch des Code-Agenten (vor jeder Rechnung, kein Kriterium):
  - Gelenkwerk-Gleichgewicht (Achse, Speiche, Ring) ~ (1; -0,395; +0,579) bei h = 1. Danach waere der Ring unter Zug,
    nicht unter Druck.
  - Bei G knicken die Speichen, ihr Druck bleibt nahe der Euler-Last 9,9 B/L^2. Erwartet: Achse ~ +25, Ring ~ +15,
    Speichen-Sehne ~ 0,987, Stich ~ 0,07 L.
  - Energie ~ 1,26 B/L, davon ~ 96 % Biegung.

## 6. Rauchlauf (vor dem Einfrieren, Parameter in keinem echten Lauf), ab 05:34 CEST eingetragen

- Ordner rauch-69/. Fehlpass anders als in den echten Laeufen: Achse-Ruhelaenge 1,03 (statt 1), dazu N = 8 bzw. 20.
- **Runde 1** (03:28:21 bis 03:29:30 UTC, Spuren cpu, cpu2, cpu3, alle rc = 0, erste Codefassung ohne Sattelflucht):
  - rauchG (5 Tetraeder, N = 8, G, aus): 38 Newton-Schritte, Gradient 1e-10, stabil, 5,9 s. Achse +25,0, Ring +14,1
    (Zug), Speichen gedrueckt. **Nur die fuenf Speichen an B sind geknickt** (Stich 0,061, -9,78); die fuenf an A
    bleiben gerade (Stich 0, -9,54, knapp unter der diskreten Euler-Last). Der Ring sitzt nicht mittig (Hoehe 0,524 ab A
    bei Achse 1,031). Das gilt nur fuer diesen Fehlpass; die echten Laeufe koennen anders ausgehen.
  - rauchE (N = 8, E, M, ohne Anstoss): 252 Schritte, 64,5 s. Newton lief zuerst in einen **Sattel** (Energie 1,0487,
    Verschiebung mu ~ 49 bis zum Ende). Erst Rundungsrauschen trieb ihn nach ~200 Schritten heraus in ein stabiles
    Gleichgewicht (0,7945, kleinster Eigenwert 0,043, symmetrisch: alle Speichen -16,5, Stich 0,039).
  - rauchk4 (4 Tetraeder offen, N = 8, E, aus): spannungsfrei, |tau| <= 1,7e-14, Axialkraft <= 1,1e-11, Stich 7e-16.
  - Wunschwinkel M wie geplant: bei A Achse-Speiche 59,998 Grad, Speiche-Speiche 61,198; bei r_0 Speiche-Speiche 60,004,
    Speiche-Ring 59,401, Ring-Ring 108,000.
- **Aenderungen nach Runde 1** (vor dem Einfrieren, offengelegt):
  - Sattelflucht in den Loeser (Abschnitt 1). Grund: rauchE. Ohne sie haengt das Ergebnis am Rundungsrauschen.
  - Feines Gitter N = 20 statt 24. Grund: Laufzeit; E brauchte bei N = 8 schon 65 s, die Spur bricht bei 600 s ab.
  - **Nicht geaendert:** die F2-Regel ("alle Staebe der Art geknickt"). Sie stand vor dem Lesen von rauchG fest. Dass
    rauchG nur eine Speichenfamilie knicken liess, haette sie dort scheitern lassen. Eine Lockerung nach diesem Befund
    waere eine Lockerung nach Befund; die schwache Lesart "ein Stab" bleibt nur berichtet.
- **Runde 2** (03:33:39 bis 03:35:22 UTC, Code mit Sattelflucht, Spuren cpu bis cpu4, alle rc = 0):
  - rauchG20 (N = 20, G, aus): 32 Schritte, kein Stoss, stabil, 4,6 s. Wieder nur die Speichen an B geknickt
    (Stich 0,060), die an A gerade.
  - rauchE2 (N = 8, E, ohne Anstoss): wie rauchE, 252 Schritte in einer Phase, kein Stoss noetig (das Rauschen trieb
    Newton innerhalb der Phase aus dem Sattel), stabil, 0,7945, 63 s.
  - rauchE20 (N = 20, E, ohne Anstoss): 136 Schritte, kein Stoss, stabil (kleinster Eigenwert 0,018), symmetrisch
    (alle Speichen -17,0, Stich 0,039), Energie 0,8158, 53,7 s.
  - auswertung.py an den Rauchdateien (umbenannt per Verweis in rauch-69/test/; nur Codepruefung): laeuft. Fuer
    diesen kleineren Fehlpass ergaebe sie F1 nicht, F2 streng nicht (schwach ja), F3 ja mit Biegeanteil 0,81 bis 0,82.
    Das kenne ich damit vor den echten Laeufen (offengelegt). Die Regeln bleiben unveraendert.
  - Nach Runde 2 habe ich auswertung.py nur robust gegen fehlende Schluessel gemacht (.get fuer "stabil" und
    "anzahl_stoesse", die die erste Codefassung nicht schrieb). Keine Regel geaendert.

## 7. Einfrieren

- Code-Pruefsummen (sha256), lokal und auf der .69 gleich (geprueft 05:35:45 CEST):
  - code/frust_3d.py: 0b9cee169dbc13173f98710bac781714d962e94278bc66b8c61605f8dd91e8e2
  - code/auswertung.py: 7d766fad390d897d9dc49f2613cc9462356e542c974a15798bfb72e3667d7c3c
- Eingefroren als PLAN.md.eingefroren-<Zeit> und code/*.eingefroren-<Zeit>, schreibgeschuetzt, vor dem ersten echten
  Lauf. Die Fassung vor dem Lesen der Rauchlaeufe liegt als PLAN.md.bak-vor-rauch daneben.
