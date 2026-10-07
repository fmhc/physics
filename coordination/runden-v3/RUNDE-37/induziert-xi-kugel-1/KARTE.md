# INDUZIERT-XI-KUGEL-1: Kippt das Einstein-Vorzeichen auf dem S^4-Netz bei der konformen Kopplung xi = 1/6, wie im Kontinuum? (Runde 40/41)

- Leitung claude-primary. Karte und Wahrscheinlichkeiten geschrieben ab 2026-10-04 13:08:35 CEST (date), vor jeder
  Rechnung.
- **Anlass:**
  - INDUZIERT-KUGEL-1 und -2: Auf dem symmetrischen S^4-Netz gibt ein P1-Skalar ein negatives sqrt(N)-Glied (Einsteins
    Vorzeichen), beta = -1,65 (Regel S, umgerechnet), -1,613 (Regel Q, ohne Umrechnung), robust in der Familie gleicher
    Simplexform.
  - INDUZIERT-G-L: Bei freien Feldern setzt der Regler das Vorzeichen; im Kontinuum mit Eigenzeit-Regler ist der
    Vorfaktor des induzierten R-Glieds proportional zu (1/6 - xi) mal Lambda^2 [S Visser 2002, Tab. 1]. Das Dossier sagt
    voraus [ES]: Auf dem Gitter tragen O(h^2 R)-Anteile des Operators in derselben Ordnung bei, ein "xi_eff" ist dann
    keine Kopplung, sondern die Summe dieser Gitteranteile.
- **Frage:** Fuegt man dem Netz-Skalar ein Kruemmungsglied xi R phi^2 hinzu (auf S^4 ist R = 12/a^2 konstant, also eine
  Masse m^2 = xi R), wo kippt beta das Vorzeichen? Im Kontinuum mit Eigenzeit-Regler bei xi* = 1/6. Liegt xi* auf dem Netz
  nahe 1/6, verhaelt sich der Gitter-Regler wie ein "natuerlicher" Regler; liegt es weit weg, ist das Netz-B
  gitterspezifisch.
- **Ableitbarkeitsprobe (Leitung):** beta(xi) = beta(0) + xi gamma + ...; gamma haengt an der Spur Tr'(K^-1 M) auf den
  S^4-Netzen. Die Rohdaten von KUGEL-1/-2 enthalten keine K^-1-Daten (KUGEL-GEGENLESEN, jq keys); gamma und xi* sind
  daraus nicht ableitbar. Projekt-grep "xi R phi", "konforme Kopplung", "nicht-minimal": nur INDUZIERT-G-L (Literatur)
  und Weichenstaende; keine Rechnung.
- Kennzeichen: [M] Mathematik, [E] Messung im Modell, [S] Literatur an der Quelle, [H] Hypothese.

## Test (Code-Agent)

- **Code, Netze, Saaten:** kugel.py aus RUNDE-37/induziert-kugel-2/code/ (Regel Q, volumentreu, keine Umrechnung noetig);
  dieselben S^4-Saaten und T^4-Referenzen, N = 1000, 2000, 4000, 8000; mindestens 20 Saaten je N.
- **Operator:** K + xi R M auf S^4 (M wie in KUGEL-1 die Massenmatrix bzw. die P1-Volumengewichte; Wahl im Plan begruenden),
  R = 12/a^2. Auf T^4 ist R = 0, die Referenz bleibt unveraendert. xi = 0, 1/12, 1/6, 1/4, vorab gebunden, kein fuenfter
  Wert nach Befund.
- **Nullmode:** Fuer xi > 0 ist K + xi R M regulaer; der Beitrag der frueheren Nullmode (~ ln N) im Fit mit gamma ln N
  aufnehmen; im Plan begruenden.
- **Messgroessen:** beta(xi) je Saat (Fit wie KUGEL-1), Steigung gamma = d beta/d xi gepaart je Saat, xi* = -beta(0)/gamma
  mit SE; Linearitaet von beta(xi).
- **Kontrolle:** beta(0) bitgleich mit KUGEL-2 (Regel Q, Gamma) auf denselben Saaten.

## Vorhersagen (vor jeder Rechnung)

| Nr | Vorhersage | Wahrsch. |
|---|---|---|
| XI0 | Kontrolle: beta(0) bitgleich mit KUGEL-2 (Regel Q) | 90 % |
| XI1 | beta(xi) steigt mit xi (gamma > 0 mit >= 3 SE) und ist ueber die vier Werte linear (Rest der Geraden <= 2 SE je Punkt) | 75 % |
| XI2 | [H] xi* liegt in [0,10; 0,25] | 40 % |
| XI3 | [H] xi* liegt innerhalb 20 % von 1/6 (in [0,133; 0,200]) | 25 % |

**Bedeutung (vorab):**
- **XI3 trifft ein:** Der Gitter-Regler auf dem S^4-Netz verhaelt sich beim R-Glied wie ein Eigenzeit-Regler: Das
  Einstein-Vorzeichen des minimalen Skalars und sein Kippen bei konformer Kopplung folgen dem Kontinuum [H].
- **XI2 verfehlt:** Das Netz-B ist gitterspezifisch; das Vorzeichen fuer einen Materietyp ist eine Eigenschaft dieses
  Netzes, nicht des Kontinuums (wie INDUZIERT-G-L allgemein erwartet).
- **XI1 verfehlt:** Das R-Glied auf dem Netz reagiert nicht wie erwartet auf eine Masse; dann ist schon die Lesart von
  beta als R-Koeffizient zu pruefen.

## Rahmen

- Code-Agent. Laeufe nur auf der .69 ueber kleintest.sh, Spuren cpu3, cpu4 und cpu5; je <= 10 min.
- Plan vor der ersten echten Rechnung einfrieren. Rauchlauf zuerst.
- Zeitbox 120 min.
