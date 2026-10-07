# PLAN (ZWEIFELD-NACHBAU, Runde 17)

- Verfasst ab 2026-10-02 11:57:31 CEST (date), vor dem ersten .69-Lauf. Code-Agent, frischer Kontext, Start
  11:12:33 CEST, Zeitbox 120 min.
- Code: code/zweifeld.py (eigener Code). Saat der Hintergrundprofile mit code/beutel_v2.py (BEUTEL-1, unveraendert
  kopiert, sha256 6875e6e5...).
- Gelesen: KARTE.md; RUNDE-16/beutel-1: KARTE.md, ERGEBNIS.md, code/beutel_v2.py; RUNDE-16/log-nachbau: KARTE.md,
  HERLEITUNG.md, PLAN.md, ERGEBNIS.md, stille.py, Diff von stille_n1.py und stille_n2.py gegen stille.py;
  kleintest.sh (per ssh cat). Sonst nichts.

## 1 Herleitung (eigene)

### 1.1 Linearisierung
- Bewegungsgleichungen: psi_tt - lap psi + U_S psi = 0, chi_tt - lap chi + U_chi = 0 (S = |psi|^2).
- Hintergrund psi = f e^{iwt}, chi = g: lap f = (U_S - w^2) f, lap g = U_chi.
- Stoerung psi = e^{iwt}(f + eta), eta = a e^{i rho t} + b e^{-i rho t} (a, b reell), chi = g + c cos(rho t).
  - delta S = f (eta + eta*) = 2 f (a + b) cos(rho t).
  - Koeffizient von e^{i rho t} bzw. e^{-i rho t} in der psi-Gleichung, Koeffizient von cos(rho t) in der chi-Gleichung:
    - -lap a + [U_S + f^2 U_SS - (w + rho)^2] a + f^2 U_SS b + (f U_Schi / 2) c = 0
    - -lap b + [U_S + f^2 U_SS - (w - rho)^2] b + f^2 U_SS a + (f U_Schi / 2) c = 0
    - -lap c + [U_chichi - rho^2] c + 2 f U_Schi (a + b) = 0
- Selbstadjungiert erst mit ct = c/2: dann koppeln a, b und ct symmetrisch mit hh = f U_Schi. (Kopplung a <- c ist
  f U_Schi/2, c <- a ist 2 f U_Schi; Skala lambda mit lambda/2 = 2/lambda, also lambda = 2.)
- M2: U_S = 1 + g^2 - 2S + 1,5 S^2, U_SS = 3S - 2, U_Schi = 2g, U_chichi = 3g^2 - 1 + 2S.
  - Va = U_S + S U_SS = 1 + g^2 - 4S + 4,5 S^2, gs = S (3S - 2), hh = 2 f g, Wc = 3 g^2 - 1 + 2S.
  - Im Unendlichen Va -> 2, Wc -> 2, gs, hh -> 0: Schwellen (w + rho)^2, (w - rho)^2, rho^2 gegen 2.
- Mit u = r a, r b, r ct (l = 0): u'' = P(r) u, P = [[Va - Ea, gs, hh], [gs, Va - Eb, hh], [hh, hh, Wc - Ec]] symmetrisch,
  Ea = (w + rho)^2, Eb = (w - rho)^2, Ec = rho^2. Regulaer am Ursprung (keine 1/r-Terme).
- **Ein-Feld-Grenzfall (K1):** chi = 1 eingefroren, hh = 0, U = S - S^2 + S^3/2: Va = 1 - 4S + 4,5 S^2,
  gs = S (3S - 2), Schwelle 1. Das ist genau das System von LOG-NACHBAU (dort V = 1 - 4f^2 + 4,5 f^4,
  g = f^2 (3f^2 - 2)). K1 laeuft mit demselben Code, Kanaele a und b.
- **Probe der Selbstadjungiertheit:** Die Wronski-Form W[Y, Z] = Sum_i (u_i^Y u_i^Z' - u_i^Y' u_i^Z) ist nur fuer
  symmetrisches P konstant in r. Gemessen je Punkt: W zwischen regulaeren Loesungen (soll 0), zwischen den
  aeusseren Loesungen (soll 0 bzw. 1) und die Phase von W1 an zwei Anschlussradien r_m und r_m + 4 (soll gleich).

### 1.2 Bereich E1 und Loesungsraeume
- w = sqrt(w^2) im Fenster 0,911 bis 0,954. E1: (w + rho)^2 > 2, (w - rho)^2 < 2, rho^2 < 2, also
  sqrt(2) - w < rho < sqrt(2). Je Punkt geprueft: k^2 = (w + rho)^2 - 2 > 0, kb^2 = 2 - (w - rho)^2 > 0,
  kc^2 = 2 - rho^2 > 0.
- Regulaere Loesungen R = span(Y_a, Y_b, Y_c), u(0) = 0, u'(0) = Einheitsvektor. dim R = 3, W[Y, Y'] = 0
  (u = 0 bei r = 0), also R Lagrange-Raum im 6-dimensionalen Loesungsraum: R^perp = R.
- D = span(Z_b, Z_c): Loesungen ohne Welle im offenen Kanal a und mit abklingendem b bzw. c (Z_j ~ e^{-kappa_j r} im
  Kanal j). D ist isotrop.
- **Stille Stelle <=> R geschnitten D ungleich 0 <=> G = (W[Y_x, Z_j]) (3 x 2) hat Rang <= 1.**
  - z in D liegt in R genau dann, wenn W[Y_x, z] = 0 fuer alle x (R^perp = R). Mit z = Sum beta_j Z_j: G beta = 0.
- Kofaktoren c_x von G (c^T G = 0): c = (m_a, -m_b, m_c) mit m_x = Minor ohne Zeile x. Y_phys = Sum c_x Y_x ist die
  regulaere Loesung mit abklingenden geschlossenen Kanaelen.
- **Abstrahlamplitude W1 = Sum_x c_x (k W[Y_x, Z_2] - i W[Y_x, Z_1])** mit Z_1, Z_2 = Loesungen mit
  u_a(R) = 1, u_a'(R) = 0 bzw. 0, 1 und ruhenden geschlossenen Kanaelen bei R = R_lin.
  - Fuer Y_phys mit u_a ~ alpha sin kr + beta cos kr gilt W1 = k (beta + i alpha) e^{-ikR}: die komplexe Wellenamplitude
    im offenen Kanal, mal einem glatten Faktor ungleich 0.
  - W1 = 0 <=> stille Stelle: W1 = 0 und c^T G = 0 heisst W[Y_phys, Z] = 0 fuer alle nicht wachsenden Z, also
    Y_phys in D (D' = span(Z_b, Z_c, Z_1, Z_2), D'^perp = D). Y_phys ungleich 0 in R und D ist unmoeglich
    (sonst Rang G <= 1 und c = 0). Also W1 = 0 <=> c = 0 <=> Rang G <= 1.
- **Geschlossene Bedingung:** m_a = det B = 0, B = Block der Zeilen b, c von G. Bedeutung: Y_b, Y_c haben eine
  Kombination mit abklingenden Kanaelen b und c (Zustand des geschlossenen Teilsystems, von a mitgekoppelt).
  Bei zwei Kanaelen (K1) ist das G_bb = 0 wie in LOG-NACHBAU.
- **Kenngroesse s** an Nullstellen von m_a: eta = Einheits-Nullvektor von B (B eta = 0), s = Zeile a von G mal eta,
  also s = W[Y_a, z] mit z = eta_b Z_b + eta_c Z_c (abklingend, ohne Welle, regulaer in b und c). s ist der singulaere
  a-Anteil von z, die Ueberlappung mit der offenen Welle. Auf m_a = 0 (Rang B = 1) gilt: stille Stelle <=> s = 0.
  - Das Vorzeichen von eta ist bei zwei geschlossenen Kanaelen nicht kanonisch. Es wird entlang jeder Kurve stetig
    gefuehrt: Ausrichtung an der gepaarten Nullstelle der Vorzeile (eta . eta_vor > 0). Erste Zeile bzw. ungepaarte
    Nullstelle: groesste Komponente positiv. Bei K1 ist eta = 1 (kanonisch, gleich LOG-NACHBAU).
- **Orthonormierung (Godunov):** Grosse Baelle (Radius ~10 bis 20) lassen alle Y auf denselben wachsenden Modus
  kippen. Deshalb Gram-Schmidt im Zustandsraum (u, u') bei r = 1, 2, 3, ...:
  - Y in der Reihenfolge b, c, a (Dreiecksmatrix mit positiver Diagonale): m_a, s (auf m_a = 0) und W1 aendern sich nur
    um positive Faktoren; Vorzeichen, Nullstellen und Phase von W1 bleiben.
  - Z_b, Z_c orthonormiert (Faktor det > 0 auf c); Z_1, Z_2 nur um ihre D-Anteile bereinigt (aendert W1 nicht).

## 2 Numerik

- **Hintergrund:**
  - Saat: BEUTEL-1-Code (initial_profile, flow, newton_Q) bei Q = 3000 (M2) bzw. 300 (M1).
  - Danach eigener Newton fuer das Numerov-Schema (4. Ordnung) in u = r f, v = r (g - 1) mit u = v = 0 bei r = 0 und
    r = R. Abbruch bei Newtonschritt < 1e-13 (relativ zu max u).
  - Fortsetzung in w^2 in Schritten <= 0,005 (Halbierung bei Fehlschlag, knotenfrei verlangt).
  - Vorlauf auf R = 90 (hp = 0,01). Danach R_lin = 5 * ceil((R_half(w^2 min) + dR) / 5) mit dR = 35 (M2) bzw. 40 (M1),
    r_m = round(R_half(w^2 min)) + 3. Endprofile auf beiden Stufen auf [0, R_lin].
  - Beliebige w^2 (Newton, Rechteck): Newton aus dem naechsten Zeilenprofil.
- **Kanaele:** RK4 mit h = 2 hp, Profilwerte auf dem Gitter hp. Stufe 1: hp = 0,01; Stufe 2: hp = 0,005.
  - Y nach aussen von 0 bis r_m (und r_m + 4), Z_b, Z_c, Z_1, Z_2 nach innen von R_lin bis r_m.
  - Z_j startet mit e^{-kappa_j (R_lin - r_m)} und Ableitung -kappa_j mal davon.
  - W1, m_a, s, eta, G am Radius r_m; Kontrolle der Phase von W1 bei r_m + 4.
- **Zeilen:** w^2 = 0,830 + 0,002 j, j = 0..40 (41 Zeilen, Abstand 0,002), beide Stufen getrennt.
- **rho je Zeile (E1 vollstaendig):** 401 gleichmaessige Punkte von rho_lo + 0,002 bis rho_hi - 0,002, dazu an beiden
  Raendern rho_lo + d und rho_hi - d mit d = 1e-5, 2e-5, 5e-5, 1e-4, 2e-4, 5e-4, 1e-3, 1,5e-3 (417 Punkte).
  rho_lo = sqrt(2) - w, rho_hi = sqrt(2). Nicht abgetastet: je 1e-5 an den Schwellen.
- **Nullstellen von m_a:** jeder Vorzeichenwechsel zwischen Nachbarpunkten, Illinois-Regula-falsi bis Klammer
  < 1e-11 (hoechstens 30 Schritte). Dort s, eta, W1, G.
- **Detektor 1:** Nullstellen benachbarter Zeilen wechselseitig naechste und Abstand <= 0,03 werden gepaart. Kandidat,
  wenn s (mit ausgerichtetem eta) das Vorzeichen wechselt. Zusaetzlich Kandidat, wenn |eta . eta_vor| < 0,5
  (Ausrichtung unsicher).
- **Detektor 2:** Umlauf der Phase von W1 um jede Gitterzelle aus den vier Eckwerten; Zellen mit Umlauf ungleich 0.
- Kandidaten beider Stufen werden vereinigt (Abstand < 2e-3 in beiden Koordinaten zusammengelegt) und auf **jeder**
  Stufe geprueft.
- **Lokalisierung:** 2D-Newton auf (Re W1, Im W1) = 0, Differenzenquotient 1e-6, Schritt <= 0,01, in E1 gehalten,
  Abbruch bei Schritt < 1e-11, hoechstens 15 Iterationen. Doppelte Endpunkte (< 1e-7) zusammengelegt.
- **Umlauf:** Rechteck mit Halbbreite 1e-3 in w^2 und rho um den Newton-Punkt (nicht konvergiert: um den Startpunkt),
  gegen den Uhrzeigersinn in (x = w^2, y = rho), anfangs 16 Punkte je Kante.
  - Adaptive Verfeinerung: jeder Abschnitt mit Phasensprung >= 0,4 rad wird halbiert, bis aufgeloest, hoechstens
    40 Runden.
  - Begruendung der Obergrenze: Kantenstueck anfangs 2e-3/16 = 1,25e-4; nach 40 Halbierungen 1,1e-16. Das ist die
    Aufloesung von double bei w^2 und rho ~ 1; feiner gibt es keine neuen Parameterpunkte.
  - Lehre aus LOG-NACHBAU: kleine Abstrahlamplitude dreht die Phase auf kurzem Randstueck; 6 Runden waren dort zu
    wenig, 10 reichten.
  - Umlauf = Summe der auf (-pi, pi] gewickelten Zuwaechse / 2 pi.

## 3 Kontrollen (wortgleich zur Karte) und Lesart

- K1: "Mit chi eingefroren auf 1 und ohne chi-Kopplung, sowie U = S - S^2 + S^3/2 (Masse 1, Ein-Feld-Modell M1),
  findet der eigene Code die bewiesene Stelle omega^2 = 0,797677, rho = 1,744618 auf 1e-4, Umlauf aufgeloest."
  - Ausfuehrung: Zeilen w^2 = 0,786 + 0,002 j, j = 0..12, rho in (1 - w, 1 + w), sonst dasselbe Verfahren.
  - Lesart: auf beiden Stufen Abstand in w^2 und rho je <= 1e-4, Umlauf +-1 aufgeloest.
- K2: "Hintergrundprofile auf zwei Gittern; Q und E auf 1e-5 gleich und vertraeglich mit BEUTEL-1."
  - Ausfuehrung: w^2 = 0,83; 0,85; 0,87; 0,89; 0,91. Q, E Stufe 1 gegen Stufe 2 (relativ <= 1e-5).
  - Vertraeglich: BEUTEL-1-Code newton_w bei dr = 0,02 und 0,01 auf [0, R_lin], Richardson (4 X_0,01 - X_0,02)/3;
    eigene Stufe 2 gegen Richardson relativ <= 1e-5.
  - Informativ: Q und E aller 41 Zeilen auf beiden Stufen, Virial, Knoten.
- K3: "zwei Gitterstufen je Fund, Lagen auf 1e-5 gleich." Lesart: Abstand in w^2 und rho je <= 1e-5.
- Blinde Suche: "Gefunden ist jede Stelle mit aufgeloestem Umlauf +-1 auf beiden Stufen." Zusatz: Newton-Punkt im
  Fenster (0,83 <= w^2 <= 0,91) und in E1. Verworfene Kandidaten werden mit Grund berichtet.
- Mitlaufende Proben je Punkt: isoY, isoZ, |W[Z_1, Z_2] - 1|, Phasendifferenz r_m gegen r_m + 4, E1-Schwellen.

## 4 Laufliste (.69, kleintest.sh, Spuren cpu3 und cpu4; Dauer in ERGEBNIS.md)

- Vor dem ersten Lauf: py_compile auf der .69. Keine lokalen Interpreterstarts.
- L1 (cpu3): profile M1. L2 (cpu4): profile M2 mit K2.
- L3/L4: scan M1 Stufe 1 (cpu3) / Stufe 2 (cpu4). L5/L6: kand M1 Stufe 1 / 2.
- L7 ff.: scan M2 Stufe 1 (cpu3) und Stufe 2 (cpu4), in Bloecken zu 10 Zeilen; Schnitte nach gemessener Laufzeit so,
  dass jeder Aufruf unter 8 min bleibt (aendert nichts am Ergebnis).
- Danach kand M2 Stufe 1 (cpu3) und Stufe 2 (cpu4), jeweils mit den Zeilendateien beider Stufen.
- Jede Zeile wird nach ihrem Block sofort als JSON gespeichert (tmp + rename). Ausgaben nie ueberschreiben: neue
  Ordner je Lauf.
- Programmfehler (Abbruch mit Ausnahme) werden behoben, mit sha256 dokumentiert, und der Lauf wird wiederholt. Das
  Verfahren aendert sich dabei nicht.

## 5 Folgelaeufe

- Nur mit eingefrorenem Nachtrag (PLAN-NACHTRAG-*.md), als nachtraeglich gekennzeichnet; nach Laufbeginn.
