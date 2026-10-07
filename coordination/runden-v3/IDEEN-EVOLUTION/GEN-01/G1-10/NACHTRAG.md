# G1-10 Nachtrag (Test-Agent T-2)

- 2026-09-30 08:10:20 CEST (date). KARTE.md geprueft, nicht geaendert; nur die Zeile "Vorhersage geschrieben:
  2026-09-30 07:58:24 CEST" angehaengt. Vorhersage V1 bis V4, "scheitert, wenn", Gegenprobe R_c = 1e4 und
  Plausibilitaetsschranke waren vollstaendig.
- **Geparkt wegen der Zeitbox (45 min fuer fuenf Karten).** Kein Code, keine Formprobe, kein LAUF.txt. Der Umbau
  braucht nach meiner Schaetzung etwa 1 h, fuer einen Bearbeiter ohne Vorkenntnis von bic2_v2.py eher mehr. Damit liegt
  er an der 1-h-Grenze der Leitung.
- Beruehrte Stellen in RUNDE-07/bic2/bic2_v2.py (2364 Zeilen, nur als Kopie):
  - Profil: profil / profil_allg und rk4_u. (dim - 1)/r wird zu (2/R_c) coth(r/R_c); der Schwanz faellt wie
    e^{-sqrt(1 + 1/R_c^2 - omega^2) r} / sinh(r/R_c).
  - Linearer Operator: lin_aufbau / lin_multi, derselbe Radialterm.
  - Auslaufende Randbedingung: hankel und jost_start. Im flachen Raum Hankel-Funktionen; in H^3 fuer chi = sigma f
    ebene Wellen e^{i k r} mit k^2 = (omega + nu)^2 - 1 - 1/R_c^2.
  - Pol- und Umlaufteil (det, newton, kontur, umlauf) bleiben.
  - Arm (A): flacher Operator plus Massenterm 1/R_c^2. Arm (C): gebrochene Dimension ueber den vorhandenen
    dim-Parameter ("bruecke").
- Rechenort laut Karte: .69 cpu-Spuren, je R_c ein Aufruf unter 10 min.
