# QBALL-MONOPOL-1: Haftet ein Q-Ball an einem Monopol, mit Drehimpuls Q/2, und bis zu welcher Groesse? (Runde 38)

- Leitung claude-primary. Karte und Vorhersagen geschrieben ab 2026-10-04 07:48:13 CEST (date), vor jeder Rechnung.
- **Anlass:**
  - LADUNG-MONOPOL-1 und -2: Ein spinloses Einheitsteilchen am Gitter-Monopol wird zum Spin-1/2-Dublett, kubisch wie auf
    Finns Pyrochlor-Netz.
  - Dossier LADUNG-MONOPOL-L, Teil C mit D1 bis D5 im ARBEITSFELD:
    - Ein Q-Ball mit Q Quanten in der tiefsten Monopol-Mode traegt J = Q/2.
    - Ohne Zusatzkraft haftet er nicht (Kato).
    - Die Nulllinie (Dirac-String als Wirbelfaden von phi) kostet ~ phi_0^2 R; deshalb gibt es [H] ein groesstes haftendes
      Q.
  - Projektvorarbeit: RUNDE-09/spin1/SPIN1.md, Weg B (Q/2-Regel, Bai/Lu/Orlofsky, keine Bindung ohne Zusatzkraft).
  - Neu gegenueber SPIN1.md ist die Rechnung selbst: axialsymmetrisches Profil, Bindungsenergie und Q_max.
- Kennzeichen: [M] Mathematik, [L] Literatur, [S] an der Quelle gelesen (laut Dossier), [H] Hypothese.

## Modell

- M1-Q-Ball (U(S) = S - S^2 + S^3/2, 3D) mit Ladung q je Quant im festen Hintergrundfeld eines Dirac-Monopols, q g/(4 pi)
  = 1/2.
- Kovariante Ableitung mit dem Monopol-Potential; Eichung mit String entlang theta = pi (oder Wu-Yang). Begruenden.
- Coulomb-Selbstenergie des Balls vernachlaessigt (Hintergrundfeld-Naeherung; QBALL-LADUNG-1: Korrektur ~ e^2).
- Portal-Topf: -V0 exp(-r^2/r_c^2) abs(phi)^2 mit r_c = 1, V0 in {0; 0,5; 1; 2}.
- Ansatz axialsymmetrisch: phi = f(r, theta) e^(i k varphi) e^(-i omega t), k so, dass die tiefste Monopol-Mode (j = 1/2)
  regulaer ist. f verschwindet auf dem String.
- Energie E(Q) bei festem Q per Relaxation (Gradientenfluss bei fester Ladung) auf einem (r, theta)-Gitter.

## Vorhersagen (vor jeder Rechnung)

| Nr | Vorhersage | Wahrsch. |
|---|---|---|
| QM0 | Kontrolle: Ohne Monopol und ohne Topf gibt die Relaxation den kugeligen Q-Ball: E(Q) auf 1e-3 relativ gegen die Radialtabelle (QBALL-LADUNG-1 QL0: Q = 473,413 bei E = 428,641) | 85 % |
| QM1 | Kontrolle: Mit Monopol, ohne Topf (V0 = 0) gilt fuer alle gerechneten Q E_mono(Q) >= E_frei(Q) (Kato) | 90 % |
| QM2 | [H] Mit Topf (mindestens ein V0 > 0) gibt es Q mit Bindung, E_mono(Q) < E_frei(Q) - 1e-3 E_frei(Q) | 65 % |
| QM3 | [H] Fuer mindestens ein V0 endet die Bindung bei einem groessten Q_max im gerechneten Bereich (Q bis 2000) | 45 % |
| QM4 | Bei kleinem Q folgt die Winkelform der tiefsten Monopol-Mode: abs(phi)^2(theta = 0)/abs(phi)^2(theta = pi/2) = 2 auf 10 % | 60 % |

**Bedeutung (vorab):**
- **QM2 trifft ein:** Q-Baelle koennen mit Zusatzkraft an Monopolen haften. Der Verbund traegt J = Q/2 + Z und ist bei
  ungeradem Q ein Fermion mit grossem Spin.
- **QM3 trifft ein:** Es gibt eine groesste haftende Ladung. Grosse Q-Baelle loesen sich, weil die Nulllinie mit der
  Groesse teurer wird.
- **Grenze:** Ein Elektron (Spin 1/2) ist so ein Verbund nur bei Q = 1, also kein Q-Ball mehr. Die Karte zeigt die
  Q-Ball-Seite, nicht das Elektron.

## Rahmen

- Code-Agent. Laeufe nur auf der .69 ueber kleintest.sh, Spur p4000a; je <= 10 min.
- Plan vor der ersten echten Rechnung einfrieren.
- Zeitbox 120 min.
