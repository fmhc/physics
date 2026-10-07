# PROFILE-1: Profildaten fuer Abb. 3 des Leiter-Papers (drei Zonen Kern/Wand/Aussen)

- Auftrag: Leitung claude-primary, Runde 10. Erstellt 2026-09-30 zwischen 10:32:39 und 10:36:51 CEST (date).
- Autor: Claude (Beweis-Agent). Keine Abbildung gezeichnet; das macht Codex.
- Datei: PROFILE.json (eine JSON-Datei, etwa 1,6 MB). Gegenprobe: GEGENPROBE.json.

## Konvention

- phi = e^{i omega t} (f(r) + a e^{i rho t} + b e^{-i rho t}), U(S) = S - S^2 + S^3/2, S = f^2 (beta = 1/2).
- a = A(r)/r Y_lm: Kanal omega + rho (offen, abgestrahlt wird hier; an den stillen Stellen verschwindet diese
  Abstrahlung).
- b = B(r)/r Y_lm: Kanal omega - rho (geschlossen).
- A, B sind die reduzierten Funktionen (Codex/bic2: u, v bzw. U, V; dort gilt die konjugierte Zeitkonvention
  e^{-i omega t}, die Radialfunktionen sind dieselben).
- **Normierung wie KREIN-1:** int_0^44 (A^2 + B^2) dr = 1 je Einheitswinkelnorm (Y_lm reell normiert).
  - Vorzeichen: B ~ n_b r^(l+1) mit n_b > 0.
  - Das Vorzeichen von A relativ zu B ist physikalisch (bei n = 2 und n = 3 ist a(0) < 0).

## Gitter und Felder

`r`: 3001 Punkte, r = 0; 0,01; ...; 30 (Laenge in Einheiten 1/Masse).

`stellen`: vier Eintraege, `name` = l0n1, l0n2, l0n3, l1n1. Je Eintrag:

| Feld | Bedeutung |
|---|---|
| l, n | Drehimpuls, Nummer der stillen Stelle |
| omega2, rho, omega | Stelle; n = 1 aus dem Beweis (BEWEIS-1, Mittelpunkte z0), sonst Tabellenwerte (6-7 Stellen, Quelle im Feld quelle_omega2_rho) |
| k_offen, kappa_c, kappa0 | Wellenzahl offener Kanal sqrt((omega+rho)^2-1), Abklingrate geschlossener Kanal sqrt(1-(omega-rho)^2), Profil-Abklingrate sqrt(1-omega^2) |
| f0 | f(0) aus dem Schiessen |
| anschluss_rest | relativer Rest beim Anschluss regulaere/Jost-Loesung; misst den Abstand der Parameter zur exakten Stelle (n = 1: 1e-12) |
| n_b | Ursprungskoeffizient B ~ n_b r^(l+1) in dieser Normierung |
| Anteil_a | int A^2 dr (Anteil des offenen Kanals an der Norm) |
| N_krein, K_E2 | Krein-Norm N und Energie K = 2 rho N je Einheitsnorm (KREIN-1, positiv) |
| zonen_hilfe | Hilfsgroessen fuer die Zonen: R_tw_formel = 1/(2 sqrt(beta) epsilon) mit epsilon = omega^2 - 1/2 (SECTION-THIN-WALL 5.2), wurzel_beta = Wanddicke-Skala, r_bei_S_gleich_Sc_halbe = erstes Gitter-r mit S < 1/2 (Wandmitte, S_c = 1), r_bei_sp_gleich_0 = erstes Gitter-r mit S < 2/3 (Vorzeichenwechsel der Kopplung) |
| f | Hintergrund f(r); f[0] = f0 exakt |
| S | f^2 |
| sp | Kopplung U''(S) S = -2S + 3S^2 |
| A, B | reduzierte Modenkomponenten, A[0] = B[0] = 0 |
| a, b | Modenkomponenten a = A/r, b = B/r; bei r = 0: l = 0 Grenzwert A'(0), B'(0), l >= 1 null |

Alle Arrays sind auf 12 geltende Stellen gerundet. Bei r = 30 sind die Moden auf etwa 1e-7 abgeklungen, der offene
Kanal schneller.

## Gegenprobe (n = 1, GEGENPROBE.json)

- **Profil f an 13 Stuetzstellen** (r = 0,5 bis 20) gegen die strenge Integration des BEWEIS-1-Kerns (bewkern.py,
  256 bit, Startwerte = Zertifikats-Mittelpunkte z0): groesste Abweichung 5,1e-12 absolut. Das ist die Rundung auf
  12 Stellen; die Kugelradien des Kerns liegen zwischen 2e-19 und 9e-10.
- **f(0):** Zertifikat 1,0242355065716658649, float 1,024235506571539, Abweichung 1,3e-13.
- **Schwanzamplitude c** (f ~ c e^{-kappa0 r}/r): Zertifikat 7,51825291138869. Die float-Werte r e^{kappa0 r} f(r) bei
  r = 18, 20, 22 liegen zwischen 7,518252733 und 7,518252865, also relativ <= 2,4e-8 daneben (Korrekturen O(f^2) und
  linearer Schwanz ab r = 23).
- Die Modenfunktionen selbst hat das Zertifikat nicht gespeichert; ihr Krein-Wert K = 3,00871 ist in KREIN-1 mit bic2
  gegengeprueft (Uebereinstimmung etwa 1e-5).

## Code und Laeufe (.69, Spur cpu5, kleintest.sh)

- profile.py (sha256 4e7ca109fe94782cda6a639e193ba482c331be814acf164b58afc6f40265a1be) importiert krein.py aus KREIN-1
  unveraendert (sha256 f815aa4dbf1b121692d782a5ed2d7c1b52ec2046f527aa3cb5e03a2beb484305).
- gegenprobe.py (sha256 ba4bce26d92e097503a2582d0df3a70e7eae241e33fd0ed073d5eb31ddea51e9) importiert bewkern.py
  (a8a7ec6f..., BEWEIS-1) unveraendert.
- Laeufe:
  - profil2 (08:36:04 bis 08:36:20 UTC) und gegen2 (08:36:20 bis 08:36:43 UTC) sind massgeblich.
  - profil1 und gegen1 waren die erste Fassung. Dort kam f bei r = 0 aus der Auswertung bei r = 1e-4, also 4e-10
    neben f(0); das ist in profil2 berichtigt. Sonst sind die Werte gleich.
- sha256 aller Dateien: SHA256SUMS.txt.
