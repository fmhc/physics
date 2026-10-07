# BAG-DIM: Misst ein Beutel-Teilchen die Dimension seines Raums? (Runde 24)

- Leitung: claude-primary. Karte und Vorhersagen geschrieben ab 2026-10-03 00:31:55 CEST (date), vor jeder Rechnung.
- Herkunft: Finns Frage "basic verbindung logik -> teilchenmodell"; RUNDE-23/IDEEN-LOGIK-TEILCHEN.md, Befund 3b; Pool-Eintrag
  BAG-DIM.
- **Schreibtisch der Leitung:**
  - Beutel-Q-Ball (Friedberg-Lee-Sirlin, FLS): Im Beutel ist das geladene Feld masselos, der Beutel kostet B je Volumen.
  - Auf einem Raum mit Volumenwachstum V ~ R^(d_f) und Dirichlet-Eigenwert lambda_1 ~ R^(-d_w) gilt
    E(R) = Q sqrt(lambda_1) + B V = Q R^(-d_w/2) + B R^(d_f).
  - Minimum ueber R: **E ~ Q^p mit p = d_f/(d_f + d_w/2) = d_s/(d_s + 1)**, mit der spektralen Dimension
    d_s = 2 d_f/d_w.
  - Erwartete Exponenten:
    - 2D-Gitter: p = 2/3
    - 3D-Gitter: p = 3/4 (FLS [L])
    - Sierpinski-Dreieck (d_f = log3/log2 = 1,585, d_w = log5/log2 = 2,322, d_s = 1,365): p = 0,577. Mit der
      Hausdorff-Dimension waere es 0,613.
  - Ohne Dimension (Zufallsgraph, Kleine-Welt): Das Volumen waechst exponentiell, lambda_1 sinkt kaum. Dann geht p gegen 1,
    das Teilchen wird "massig" ohne Beutelgesetz.
- Ableitbarkeitspruefung:
  - Im Projekt gibt es keine Beutel-Q-Baelle auf Graphen.
  - Die Exponenten folgen aus dem Skalenargument; ob ein echter Feld-Q-Ball mit endlicher Wand ihnen folgt (bei
    erreichbaren Groessen, mit Oberflaechenkorrekturen und auf dem Fraktal mit log-periodischen Schwankungen), ist offen.
- Explorativ (v3), Hypothesen [H].

## Test

- **Modell FLS, zwei Felder:** phi komplex, chi reell, U = (lam/4)(chi^2 - 1)^2 + g^2 chi^2 |phi|^2 mit lam = 1, g = 1.
  - Vakuum chi = +-1.
  - Im Beutel chi ~ 0: phi masselos, Beutelkonstante 1/4.
- **Auf einem Graphen** (Knotengewicht 1, Kantengewicht 1, Graph-Laplace):
  - E[f, chi] = Q^2/(4 Sum f^2) + Sum ueber Kanten [(f_i - f_j)^2 + (chi_i - chi_j)^2] + Sum ueber Knoten U(f_i^2, chi_i)
  - Minimieren bei festem Q, z. B. L-BFGS mit analytischem Gradienten.
  - Start: Beutel um einen Mittelknoten. Pruefen, dass das Minimum ein einzelner kompakter Beutel ist.
- **Graphen:**
  - 2D-Quadratgitter (offener Rand, gross genug)
  - 3D-Wuerfelgitter
  - Sierpinski-Dreieck Stufe 8 (9843 Knoten) oder hoeher. Mittelpunkt: ein Knoten weit weg von den drei Ecken.
  - Kontrolle Z: zufaelliger 6-regulaerer Graph mit N ~ 1e4, Erzeuger wie RUNDE-22/ursuppe-1/code/ursuppe.py
- **K0:**
  - Die spektrale Dimension jedes Graphen per Waermeleitungskern (wie URSUPPE-1). Das Sierpinski-Dreieck soll ein Plateau
    nahe 1,365 zeigen.
  - Am 2D-Gitter: Ein grosser Beutel hat innen chi ~ 0 und eine Wand von wenigen Gitterschritten.
- **Messgroesse:** E(Q) ueber mindestens 1,5 Dekaden in Q im Beutelbereich (Radius etwa 6 bis 60 Graphschritte).
  - Oertlicher Exponent p(Q) = d ln E/d ln Q.
  - Auf dem Fraktal ueber volle log-periodische Perioden mitteln (Faktor 2 im Radius).
- Laeufe je <= 10 min auf CPU-Spuren.

## Vorhersagen (vor jeder Rechnung)

| Nr | Vorhersage | Wahrsch. |
|---|---|---|
| BD0 | K0: d_s-Plateau des Sierpinski-Dreiecks innerhalb 1,365 +- 0,08; Gitter 2 und 3 je +- 0,15 | 75 % |
| BD1 | 2D-Gitter: p am grossen Ende innerhalb 2/3 +- 0,03 | 70 % |
| BD2 | 3D-Gitter: p am grossen Ende innerhalb 3/4 +- 0,03 | 60 % |
| BD3 | Sierpinski-Dreieck: p (ueber volle Perioden gemittelt) innerhalb 0,577 +- 0,03 und naeher an 0,577 als an 0,613 | 45 % |
| BD4 | Zufallsgraph: p am grossen Ende > 0,85 | 55 % |

**Bedeutung (vorab):**
- BD1 bis BD3 treffen ein: Die Masse-Ladungs-Beziehung eines Beutel-Teilchens misst die spektrale Dimension seines Raums,
  auch auf einem Fraktal [H, Modell FLS].
  - Ein solches Teilchen ist ein "Dimensionsmesser" fuer entstandene Graphen (Anschluss an URSUPPE und CDT).
- BD3 trifft nicht ein, BD1 und BD2 schon: Auf Fraktalen bestimmen andere Groessen den Exponenten, etwa die Wand oder
  die log-Periodik. Beschreiben.
- BD4 trifft ein: Ohne endliche Dimension gibt es kein Beutelgesetz.

## Rahmen

- Code-Agent. Laeufe nur auf der .69 ueber kleintest.sh (CPU-Spuren cpu, cpu2, cpu3, cpu4, cpu6; je <= 10 min, 4 GB).
- Plan vor der ersten echten Rechnung einfrieren. Rauchlauf vorher erlaubt, mit Parametern, die in keinem echten Lauf
  vorkommen.
- Zeitbox 120 min.
- Literatur danach (L4): FLS 1976, Q-Baelle und NLS auf Fraktalen (Strichartz u. a.), Weyl-Gesetz auf Fraktalen
  (Kigami/Lapidus).
