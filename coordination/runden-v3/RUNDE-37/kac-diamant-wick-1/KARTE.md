# KAC-DIAMANT-WICK-1: Ergibt die Wick-rotierte Kantenwahl auf Finns Diamantnetz ein isotropes massives Dirac-Teilchen? (Runde 47, Folgekarte zu UNSCHAERFE-KANTE-L)

- Leitung claude-primary. Karte und Wahrscheinlichkeiten geschrieben ab 2026-10-05 07:53:33 CEST (date), vor jeder Rechnung.
- **Finn (05.10.):** "Kann Heisenberg unschärfe durch Kantenfindung in Dimensionen in unserem Modell erklärt werden"
- **Herkunft:** Kartenvorschlag aus UNSCHAERFE-KANTE-L (RUNDE-37/unschaerfe-kante-l/DOSSIER.md, Abschnitt 10). Dort steht der Befund: Unschaerfe folgt aus der Kantenwahl nur als Amplitude, also als Welle.
  - Ghose, arXiv 2609.29248: Kac-Kantenwahl und Dirac per Wick-Rotation [S].
  - Luecke T1 (Quantenmechanik selbst) im Lueckenabgleich 1.1 [P].
- Kennzeichen: [M], [E], [P], [S], [L], [H].

## Frage (aus dem Vorschlag)

- Zustand = gerichtete Kante: Knoten A oder B, dazu eine der 4 Tetraederrichtungen e_i. Auf A ist der Transport c e_i . k, auf B -c e_i . k.
- Gemischt wird zwischen den Richtungen mit Rate lambda, nach zwei Regeln:
  - gleichverteilt: P = J/4;
  - ohne Ruecksprung: P = (J - I)/3.
  - Jeder Schritt wechselt das Untergitter, M = [[0, P], [P, 0]], Erzeuger lambda (M - I).
- Wick-Rotation nach Ghose: t -> i t, v -> -i v (Ghose Gl. 66 bis 77) [S].
- **Gefragt:** Hat das 8x8-Bloch-Spektrum ein isotropes Bandpaar der massiven Dirac-Form E = E0 +- Wurzel(Delta^2 + c_eff^2 k^2), mit einer Masse aus hbar lambda?

## Ableitbarkeitsprobe (Leitung, vor der Karte)

- **Vorab ableitbar [M]:**
  - **k = 0-Niveaus von lambda (M - I):**
    - gleichverteilt: 0, -2 lambda, -lambda (6-fach);
    - ohne Ruecksprung: 0, -2 lambda, -2 lambda/3 (3-fach), -4 lambda/3 (3-fach).
  - **Reelle Fassung:**
    - Der langsamste Zweig ist diffusiv.
    - Er ist isotrop, weil die Tetraederrichtungen ein 2-Design sind: Summe e_i e_i^T = (4/3) I.
  - **Kopplungen in erster Ordnung in k:**
    - Die Singuletts koppeln nicht untereinander, denn Summe e_i = 0.
    - Singulett und Triplett koppeln isotrop mit Betrag c k/Wurzel(3).
    - Der Triplett-Block ist anisotrop, die Matrix [[0, k_z, k_y], [k_z, 0, k_x], [k_y, k_x, 0]], mit Vorzeichenwechsel zwischen A und B.
- **Schreibtisch je Untergitter, 4x4, gleichverteilt** [M, Leitung, nur Hinweis]:
  - Laengs [100] entsteht ein exaktes massives Dirac-Paar mit c_eff = c/Wurzel(3).
  - Laengs [111] ist das Paar gekippt: Die Mitte wandert linear in k.
  - Der Singulett-Zweig ist in zweiter Ordnung isotrop, E ~ c^2 k^2/(4 lambda).
  - Ob die Kopplung von A und B im 8x8-Erzeuger die Kippung aufhebt, ist **nicht ableitbar**. Das ist der Kern der Karte.
- **Abgrenzung [P]:**
  - DUNKEL-FLIP-L (Foster/Jacobson): Schachbrett auf fcc bzw. bcc, nicht Diamant.
  - QCA-TETRA-1: unitaerer Automat mit 2 Zustaenden je Knoten, auf Diamant nicht isotrop.
  - DIAMANT-FERMION-L: W-D-Operator, Dirac-Punkt bei Gamma, Knotenschleifen.
  - Neu ist der Kac-Erzeuger mit 4 Richtungszustaenden auf Finns Diamantnetz.

## Vorhersagen (vor jeder Rechnung)

| Nr | Vorhersage | Wahrsch. |
|---|---|---|
| KW0 | Kontrolle, vorab ableitbar: k = 0-Niveaus wie oben (beide Regeln, auf 1e-12); reelle Fassung mit isotropem diffusivem Zweig (Richtungsstreuung des k^2-Koeffizienten < 1e-9) | 90 % |
| KW1 | [H] Wick-rotiert gibt es fuer mindestens eine Mischregel ein Bandpaar der Form E0 +- Wurzel(Delta^2 + c_eff^2 k^2), dessen Richtungsstreuung bei \|k\| = 0,05 (in Einheiten der Gitterkonstante) unter 2,8e-3 liegt; das ist die Eichung aus QCA-TETRA-1 | 20 % |
| KW2 | [H] Die Mischregel ohne Ruecksprung gibt eine kleinere Richtungsstreuung des besten Bandpaars als die gleichverteilte | 50 % |
| KW3 | [H] Gilt KW1: Delta ist ein rationales Vielfaches von hbar lambda, und m = Delta/c_eff^2 stimmt auf 1e-6 mit dem Schreibtischwert des Agenten (vor der Rechnung im Plan) | 15 % (unbedingt) |

**Bedeutung (vorab):**
- **KW1 trifft ein:** Finns Kantenwahl ergibt nach der Wick-Rotation auf dem Diamantnetz eine relativistische Teilchenwelle mit Masse aus der Umklapp- bzw. Wahlrate. Das waere ein Baustein fuer Luecke T1. Spin 1/2 folgt daraus noch nicht, denn die Dirac-Form ist keine Spinor-Darstellung.
- **KW1 verfehlt:** Auf Finns Diamantnetz liefert die Kantenwahl keine isotrope Dirac-Welle. Die Unschaerfe bleibt eine Wellen-Eigenschaft ohne Teilchenbild (UNSCHAERFE-KANTE-L). Foster/Jacobson-artige Konstruktionen brauchen andere Netze.
- **KW2:** zeigt, ob Gedaechtnis (kein Ruecksprung) die Richtungsabhaengigkeit mindert.

## Rahmen

- Code-Agent, Schreibtisch und Kleintest: Eigenwerte einer 8x8-Matrix ueber mindestens 26 Richtungen und mehrere \|k\|.
- Laeufe nur auf der .69 ueber kleintest.sh, Spuren cpu7 bzw. cpu. Je Lauf hoechstens 10 min, ein Thread. Zeitbox 75 min.
- Vor der Rechnung: Ghose 2609.29248 Gl. 66 bis 77 lesen (quellen in unschaerfe-kante-l/quellen, sonst arXiv per WebFetch). Die Wick-Vorschrift und KW3-Schreibtischwerte in PLAN.md binden.
- Plan und Code vor den Hauptlaeufen einfrieren (sha256).
