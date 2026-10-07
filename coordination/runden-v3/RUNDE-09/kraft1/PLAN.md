# KRAFT-1 Plan: drei Analogkraefte aus dem Q-Ball-Modell, dazu Teilkarte TET-1

- Runde 9 (v3), Karte KRAFT-1. Bearbeiter: Code-Agent (Anthropic, Opus). Auftrag der Leitung claude-primary; Finn:
  "können wir daraus andere kräfte ableiten?". Zusaetze der Leitung: Einordnung (08:04), Teilkarte TET-1 (08:12).
- **Plan geschrieben ab 2026-09-30 08:20:23 CEST (date), vor jeder Rechnung dieser Karte.**
- Explorativ. Alles unten ist Hypothese [H] oder Schreibtischrechnung [Hand], bis ein Lauf es belegt.
- Kein Anspruch auf Elektromagnetik oder Gravitation: skalares Feld, keine Eichfelder, kein Spin 2
  (art-grenzen-20260921/WARUM-SPIN-2.md).
- **Vorher gelesen:** RUNDE-07.md, RUNDE-08.md, RUNDE-09.md, koll1/PLAN.md, koll1/ERGEBNIS.md, KOLL-1-Logs (cmt, voll),
  koll1.py (Teile), medium1d.py (Teile) und PLAN.md, RUNDE-03/ERGEBNISSE-R3.md (t2).
- **Schon gesehen, also nicht blind:**
  - KOLL-1 cmt: E_int aus der Mittelebenen-Spannung gegen 8 pi A^2 e^{-k0 d}/d (0,1 bis 3 % bei d >= 12) und die
    Drift gegenphasiger Baelle (d(50) = 16,38 gegen 16,56).
  - R3 t2 (1D): E_int(0) = -0,0817 / -0,0273 / -0,0091 bei d = 6 / 8 / 10, Fit C = 2,236, kappa 0,5542; die
    R3-Vorhersage war C = 4,1569.
  - medium1d windschatten bei u = 0 (Kraft des Mediums, zwei Baelle in Fallen, C0 = 0,1, lam = 0,1):
    9,5e-4 / ~1e-4 (unsymmetrisch) / 2,85e-6 / -1,0e-7 bei d = 6 / 10 / 16 / 24.

## 1. Modell

- L = |phi_t|^2 - |grad phi|^2 - U(S), U = S - S^2 + beta S^3, beta = 0,5, S = |phi|^2. Ball phi = f(r) e^{i omega t}.
- Schwanz: 3D f -> A e^{-k0 r}/r, 1D f -> A_1 e^{-k0 |x|}, k0 = sqrt(1 - omega^2).
- Atmung: phi = e^{i omega t}[f + eps (u e^{i rho t} + v e^{-i rho t})].
  - offener Kanal: Omega = omega + rho, q = sqrt(Omega^2 - 1)
  - geschlossener Kanal: kappa_c = sqrt(1 - (omega - rho)^2)
  - Normierung wie KOLL-1: max |u + v| = 1
- Kraefte als Impulsfluss: T^{ij} = d_i phi* d_j phi + c.c. + delta_ij L. Kraft auf Ball B = Impulsfluss durch eine
  Flaeche, die B vom Partner trennt.
- Quellenbild [Hand]:
  - Ein Schwanz, der eine freie Gleichung (-lap + k^2) F = 0 bzw. die Helmholtz-Gleichung loest, ist ausserhalb des
    Balls dasselbe Feld wie das einer Punktquelle j.
  - Fuer L_Quelle = J* phi + J phi* gilt: Kraft auf die Quelle = 2 Re Int J* grad phi.
  - Wechselwirkungsenergie zweier statischer Quellen: E_int = -2 Re(j_B* j_A) G(d).

## 2. Kraft 1: Yukawa-Typ ueber die Raender (Manton-artig)

### Herleitung [Hand]

- 3D: G = e^{-k0 r}/(4 pi r), j = 4 pi A, also **E_int = -8 pi A^2 cos(Delta theta) e^{-k0 d}/d** und
  F = -dE/dd = -8 pi A^2 cos(Delta theta) (k0 + 1/d) e^{-k0 d}/d.
  - Delta theta ist die Phasendifferenz der Baelle; F < 0 bedeutet Anziehung.
  - Gleichphasig ziehen sich die Baelle an, gegenphasig stossen sie sich ab, bei Delta theta = pi/2 ist die Kraft in
    fuehrender Ordnung null.
- 1D: G = e^{-k0|x|}/(2 k0), j = 2 k0 A_1: **E_int = -4 k0 A_1^2 cos(Delta theta) e^{-k0 d}**,
  F = -4 k0^2 A_1^2 cos(Delta theta) e^{-k0 d}.
  - Exakt fuer den 1D-Ball (Quadratur): A_1^2 = 4 k0^2/b0 mit b0 = sqrt(1 - 4 beta k0^2).
  - Bei omega^2 = 0,7 gilt k0 = 0,54772, b0 = 0,63246, A_1^2 = 1,8974, also 4 k0 A_1^2 = 4,1569. Das ist genau die
    R3-Vorhersage C = 16 k0^3/b0.
- Dieselbe Formel ergibt sich aus der Mittelebenen-Spannung der Ueberlagerung der Schwaenze:
  T^{xx}-Kreuzterm = 2 cos(Delta theta)(f_A' f_B' - k0^2 f_A f_B).
- Bei festen Ladungen gilt dieselbe Energie in erster Ordnung, weil delta E|_Q = delta(E - omega Q)|_omega.

### Spannung zu R3 [Hand]

- R3 t2 hat E_int bei d = 6, 8 und 10 gemessen: das 0,53-, 0,52- bzw. 0,52-Fache der Formel.
- Entweder stimmt der Vorfaktor in 1D nicht, oder die Relaxation mit Punktzwang in R3 misst etwas anderes.
- In 3D stuetzt die freie KOLL-1-Drift die Formel auf etwa 10 %; das ist keine unabhaengige Rechnung zur
  Spannungsrechnung, wohl aber zur Dynamik.

### Test K1 (neu)

- **K1-1D:** zwei freie Baelle, omega^2 = 0,7, im Vakuum (Kopie von medium1d.py, C0 = 0, ohne Falle).
  - Delta theta = 0, pi/2, pi bei d0 = 10, 12, 14, 16.
  - Gemessen wird die Anfangsbeschleunigung d''(0) aus dem Schwerpunktabstand (quadratischer Fit, kurzes Fenster).
  - Vorhersage: d''(0) = 2F/E_1 = -1,9812 cos(Delta theta) e^{-k0 d0} (E_1 = 2,2985), also bei Delta theta = 0:
    -8,28e-3 / -2,77e-3 / -9,27e-4 / -3,10e-4 bei d0 = 10 / 12 / 14 / 16.
  - **Entscheidung:** Das Verhaeltnis gemessen/Formel bei d0 = 12 bis 16 liegt entweder in [0,85; 1,15]; dann gilt die
    Formel, und R3 t2 hatte eine systematische Abweichung. Oder es liegt in [0,45; 0,6]; dann bestaetigt sich R3, und die
    Formel ist in 1D um den Faktor ~2 falsch.
  - Delta theta = pi/2: |d''(0)| < 0,1 des gleichphasigen Werts. Delta theta = pi: Verhaeltnis -1 +- 0,15.
- **K1-3D:** im selben GPU-Stapel wie K2 (Abschnitt 3).
  - Paare bei d0 = 12 ohne Atmung, Delta theta = 0, pi/3, pi/2, 2 pi/3, pi, fuer beide omega.
  - Formelwerte bei d = 12:
    - still (A = 7,5183, k0 = 0,44980, E = 184,62): F = 0,2857, also d''(0) = -3,10e-3 cos(Delta theta)
    - 0,76 (A = 11,331, k0 = 0,48990, E = 241,90): F = 0,4313, also d''(0) = -3,57e-3 cos(Delta theta)
  - Kriterien:
    - d''(0) gleichphasig innerhalb 10 % der Formel
    - Verhaeltnisse zu Delta theta = 0: 0,5 +- 0,05 (pi/3), 0 +- 0,05 (pi/2), -0,5 +- 0,05 (2 pi/3), -1 +- 0,1 (pi)
- Bekannt [L?, noch an der Quelle zu lesen]: Q-Ball-Wechselwirkung mit Phasenabhaengigkeit (Axenides u. a. 2000;
  Bowcock, Foster, Sutcliffe 2009).

## 3. Kraft 2: Bjerknes-Typ ueber die Abstrahlung

### Herleitung [Hand]

- **Quellenbild:**
  - Der atmende Ball strahlt im offenen Kanal eine auslaufende Kugelwelle C e^{i(Omega t - q r)}/r ab. Das ist
    aussen das Feld einer Punktquelle j = 4 pi eps C bei der Frequenz Omega.
  - Abgestrahlte Leistung: P = 8 pi Omega q |eps C|^2 (Energiefluss -(phi_t* d_r phi + c.c.)).
- **Kraft auf B**, zeitgemittelt; nur Kreuzterme gleicher Frequenz ueberleben:
  - Punktquelle: F_B = 2 Re[j_B* j_A G'(d)], G = e^{-iqr}/(4 pi r).
  - Ausgedehnter Ball B: Er streut die einfallende l = 1-Welle von A. Der Kreuzfluss "einlaufend x auslaufend" von
    ebenfalls l = 0-Emission verschwindet im Fernfeld. Deshalb wird nur der auslaufende l = 1-Anteil mit
    S_1 = e^{-2 i delta_1} multipliziert. delta_1 ist die l = 1-Streuphase von B im offenen Kanal
    (U_1 ~ sin(q r - pi/2 + delta_1)).
  - Ergebnis, mit Delta = Phasendifferenz der abgestrahlten Wellen (gleichphasige Atmung: Delta = 0; + heisst
    Abstossung):

    **F_B(d) = -[sqrt(P_A P_B)/(Omega q d^2)] [cos(q d - Delta + 2 delta_1) + q d sin(q d - Delta + 2 delta_1)]**

  - Fernfeld (q d >> 1): F_B ~ -[sqrt(P_A P_B)/(Omega d)] sin(q d - Delta + 2 delta_1). Die Kraft faellt also wie 1/d,
    wechselt mit der Periode 2 pi/q das Vorzeichen und kehrt sich mit der Atmungsphase um.
  - Grenzfall q d << 1: [cos + qd sin] -> 1, F -> -sqrt(P_A P_B)/(Omega q d^2). Gleichphasige Pulsation zieht an,
    gegenphasige stoesst ab, wie die sekundaere Bjerknes-Kraft bei Blasen [L?].
  - Bei uns ist q d ~ 70, wir sind also tief im Fernfeld-Regime.
- **Gegenprobe im Modenbild:** Die Strahlungskopplung J_rad = (Gamma/2) e^{-iqd}/(qd) (Dicke-artig; KOLL-1 schreibt
  |J_rad| = Gamma/(qd)) gibt ueber -d/dd Re J_rad dieselbe Form cos(qd)/(qd) -> sin(qd)/d.
- **Kraftschalter [H]:** An einer stillen Stelle ist die offene Aussenamplitude C = 0 (KOLL-1: 1,6e-7 bei max|u+v| = 1),
  also P = 0 und F_Bj = 0 in linearer Ordnung.
  - Es bleibt der geschlossene Kanal: Yukawa mit kappa_c = 0,524, bei d = 30 etwa 1e-8, vernachlaessigbar.
  - Dazu kommen nichtlineare Oberwellen (zweite Harmonische, Fluss ~ eps^4). Deren Kreuzterm haengt von 2 Delta ab und
    faellt in der Differenz Delta = 0 minus Delta = pi heraus.

### Zahlen [Hand]

| Punkt | omega | rho | Omega | q | 2 pi/q | Gamma (Amplitude) | P/eps^2 |
|---|---|---|---|---|---|---|---|
| 0,76 | 0,87178 | 1,72815 | 2,59993 | 2,39993 | 2,6181 | 1,99e-3 | ~4,2 (+-1) |
| still 0,7976768 | 0,893128 | 1,7446175 | 2,637746 | 2,44084 | 2,5742 | 0 (linear) | 0 |

- P/eps^2 ~ 4,2 stammt aus dem KOLL-1-Fluss 3,166 (Mittel ueber t = 100 bis 200), zurueckgerechnet mit a(t).

### Test K2

- Kopie von koll1.py (kraft12.py, Unterbefehl bj), volle nichtlineare Rechnung, achsensymmetrisch, Stapel:
  - je Abstand d_i: Paar mit gleichphasiger Atmung (+eps, +eps) und Paar mit gegenphasiger Atmung (+eps, -eps). Beide
    Baelle sind gleichphasig (Delta theta = 0), eps = 0,05.
  - d_1 = 30, d_2 = 30 + lambda/4, d_3 = 30 + lambda/2 mit lambda = 2 pi/q (0,76: 30 / 30,654 / 31,309; still
    ebenso).
  - Kontrollen: Paar ohne Atmung bei d_1 (statische Drift, gerader Anteil); Einzelball mit Atmung (liefert P(t) ueber
    den Fluss durch einen Zylinder und dient als Driftkontrolle); Einzelball ohne Atmung.
  - dazu die K1-3D-Glieder (Abschnitt 2)
- Messgroesse:
  - Delta d(t) = d_{+,+}(t) - d_{+,-}(t), mit d = Abstand der S-gewichteten Schwerpunkte der beiden Haelften.
  - Nur der ungerade Anteil in Delta ueberlebt: Delta d'' = 4 F_B,+/M, M = E_Ball.
  - Mit Abklingen: Delta d(t) = (4 F_0/M) D(t), D(t) = Int_0^t Int_0^t' e^{-2 Gamma s} ds dt'. Fuer 0,76 ist
    D(300) = 31374.
- **Vorhersagen (0,76, eps = 0,05, P(0) ~ 0,0105):**
  - Kraftamplitude bei d = 30: sqrt(P_A P_B)/(Omega d) ~ 1,35e-4.
  - |Delta d(300)| <= ~0,07, mit dem Faktor sin(q d_i + 2 delta_1).
  - Vorzeichenwechsel zwischen d_1 und d_3 (halbe Wellenlaenge): Delta d(d_1) Delta d(d_3) < 0.
  - Amplitude: sqrt(F(d_1)^2 + F(d_2)^2), mit Fit von F_0 je d aus Delta d(t) und P aus dem Einzelball, innerhalb 30 %
    von sqrt(P_A P_B)/(Omega d) (mit 1/d^2-Term).
  - Phase: Mit delta_1 aus einer Einzelball-Rechnung (l = 1, reelles rho, geschlossener Kanal ohne Wachstum) sind die
    Vorzeichen aller drei d vorhergesagt und die Werte innerhalb 30 % der Amplitude. delta_1 wird vor den Paarlaeufen
    gerechnet und als Nachtrag hier eingetragen.
- **Kraftschalter (still):** |Delta d(300)| < 0,01 max_i |Delta d_0,76(300)|. Meine Erwartung ist <= 1e-4, begrenzt durch
  die Restbreite auf dem Gitter.
- **Widerlegt,** wenn eines davon eintritt:
  - still gibt mehr als 10 % des 0,76-Werts (Schalter)
  - 0,76 zeigt keinen Vorzeichenwechsel ueber lambda/2
  - die Amplitude weicht um mehr als Faktor 2 ab (Formel)

## 4. Kraft 3: Schall im Kondensat (Goldstone)

### Herleitung [Hand]

- Medium wie medium1d: chi = e^{-i omega0 t}(sqrt(C0) + delta), omega0^2 = mc2 + 2 g4 C0; Kopplung lam S C.
- Statisch linearisiert: delta'' - M^2 delta = lam sqrt(C0) S mit **M^2 = 4 g4 C0** (M = 1/Heillaenge, wie
  medium1d "1/sqrt(2g)"). Grenzfall Thomas-Fermi: delta C = -lam S/(2 g4), wie im medium1d-Plan.
- Die Phase (Goldstone-Mode) wird statisch **nicht** angeregt:
  - Kontinuitaet d_t(Ladung) + div(C grad theta) = 0 erlaubt statisch nur theta = const.
  - Die statische Antwort laeuft allein ueber die Dichte, und die ist massiv.
- **Vorhersage [H], gegen die Karten-Hypothese:** Die statische Kraft zwischen zwei Baellen oder Dellen ist Yukawa mit
  der Heillaenge, **nicht** |x| (1D), ln r (2D) oder 1/r (3D). Sie ist anziehend fuer gleiche Kopplung und ~lam^2:
  - 1D: F_B = -lam^2 C0 s~^2 e^{-M d}, s~ = Int S(y) cosh(M y) dy
  - 2D: F_B = -(lam^2 C0 s~^2/pi) M K_1(M d)
  - 3D: F_B = -(lam^2 C0 s~^2/(2 pi)) (M + 1/d) e^{-M d}/d
- Wo die masselose Mode wirklich weit reicht [H]:
  - (a) Quellen oder Senken von Mediumladung (eps-Austausch, Osmose): Stroemung ~ 1/r^{D-1}, Kraft 1/r^2 (3D), 1/r (2D),
    konstant (1D); gleichnamige ziehen sich an (hydrodynamisches Bild von Bjerknes und Challis [L?]).
  - (b) bewegte Baelle: Dipolstroemung, Kraefte ~ 1/r^4 in 3D.
  - (c) atmende Baelle: Schallabstrahlung, Bjerknes wie Kraft 2, jetzt masselos.
  - (d) Wirbel: ln r in 2D (siehe Einordnung).
  - (e) Quanten- oder thermische Fluktuationen (Casimir) [L?]; in einer klassischen Rechnung bei T = 0 nicht vorhanden.
- Zahlen, mit s~ vorlaeufig aus dem Vakuumprofil [Hand]: s~ ~ 2,1 (M = 0,447) bzw. ~5 (M = 0,775, empfindlich auf
  den Schwanz). Das Skript rechnet s~ vor den Laeufen genau; Nachtrag hier.
  - C0 = 0,1 (M = 0,4472, lam = 0,1): F ~ -4,4e-3 e^{-0,447 d}, also 1,2e-4 / 2,1e-5 / 3,4e-6 / 5,7e-7 bei
    d = 8 / 12 / 16 / 20.
  - C0 = 0,3 (M = 0,7746): F ~ -0,075 e^{-0,775 d}, also 1,5e-4 / 6,9e-6 / 1,5e-6 bei d = 8 / 12 / 14.

### Test K3

- Kopie von medium1d.py (kraft3m1d.py, Unterbefehl kraft3): zwei Baelle (omega^2 = 0,7) in Fallen bei +-d/2,
  Medium in Ruhe, eps = 0. lam wird von 0 bis 100 eingeschaltet; Messfenster [250, 570], Hann-Mittel von F_med.
- Laeufe:
  - C0 = 0,1, lam = 0,1: d = 8, 10, 12, 14, 16, 18, 20
  - C0 = 0,1, lam = -0,1: d = 10, 14, 18
  - C0 = 0,3, lam = 0,1: d = 6, 8, 10, 12, 14
  - Kontrollen: Einzelball (C0 = 0,1 und 0,3), Paar mit lam = 0 (d = 12); grob und fein (L3)
- **Kriterien:**
  - (a) Die lokale Abklingrate aus Nachbarpaaren (C0 = 0,1: d >= 12; C0 = 0,3: d >= 8) liegt innerhalb 15 % von M. Eine
    konstante Kraft (1D-|x|-Gesetz) ist widerlegt, wenn F ueber Delta d = 6 um mehr als das Zehnfache faellt.
    - Nicht blind: Das zeigen schon die windschatten-Daten.
  - (b) Die Kraft ist anziehend fuer lam = +0,1 und -0,1, mit |F(-0,1)|/|F(+0,1)| in [0,7; 1,4].
  - (c) Der Vorfaktor lam^2 C0 s~^2 trifft bei d >= 12 (C0 = 0,1) auf Faktor 2.
  - (d) Einzelball und lam = 0: |F_med| < 1e-9.
- 2D: Keine Zeitrechnung; medium2d.py hat keinen Zweiballaufbau, und der Umbau passt nicht ins Budget. Die 2D-Form
  K_1(M d) bleibt Schreibtisch.
  - Brechungs- oder Medienbild: Ein ruhendes Medium mit statischen Dellen gibt kurzreichweitige Kraefte. Weit reichen
    sie nur mit Quellfluss.
  - kein Spin 2

## 5. Teilkarte TET-1 (Zusatz der Leitung, 08:12)

### Aufbau

- Drei Baelle auf einem gleichseitigen Dreieck (Kante d) mit Phasen 0, 2 pi/3, 4 pi/3; Spitze eines regulaeren
  Tetraeders mit Phase phi; omega^2 = 0,76.
- E_int(phi) = E[Ueberlagerung] - Summe E[einzeln] aus den Profilen, ohne Zeitentwicklung.

### Symmetrie [Hand]

- C3-Drehung plus globale Phase ergibt E(phi) = E(phi - 2 pi/3). Spiegelung plus komplexe Konjugation ergibt
  E(phi) = E(-phi).
- Also E(phi) = c0 + c3 cos 3 phi + c6 cos 6 phi + ...; die Harmonischen 1 und 2 verschwinden exakt.
- Die Ladung Q = 2 omega Int |Phi|^2 hat nur erste Harmonische, und die heben sich beim 120-Grad-Dreieck auf. Deshalb
  ist c3 fuer E und fuer E - omega Q gleich.
- Zweite Ordnung der Relaxation (~e^{-2 k0 d}) haengt nicht von phi ab: Das Dreiecksfeld nahe der Spitze hat den
  Drehimpuls m = -1 mod 3 um die Achse.

### Fuehrender cos-3-phi-Term [Hand]

- Nur beta S^3 = beta |Phi|^6 enthaelt Phi_Spitze^3.
- Paaranteil: 2 beta f_a^3 f_k^3 cos 3(phi - theta_k) = 2 beta f_a^3 f_k^3 cos 3 phi, summiert also
  c3 ~ 6 beta J_33(d), J_33 = Int f^3(x) f^3(x - d e) d^3x > 0.
  - c3 > 0: Die Energie ist am kleinsten bei phi = pi/3 (mod 2 pi/3), wenn die Spitze gegenphasig zu einer Ecke steht.
- Echte Dreikoerperterme (Phi_a^3 Phi_1* Phi_2* Phi_3* usw.) liegen an der Spitze, wo das Dreiecksfeld auf der Achse
  exakt null ist; sie sind nur durch Potenzen unterdrueckt.
- Asymptotik: J_33 ~ 2 A^3 W e^{-3 k0 d}/d^3, also lokale log-Steigung **-d ln c3/dd ~ 3 k0 + 3/d** minus eine kleine
  Kruemmungskorrektur.
  - Bei d = 8 bis 14 erwarte ich 3,3 bis 3,8 k0 [Hand].
  - Das kann oberhalb des Fensters der Leitung liegen; die 3/d-Potenz war dort nicht eingerechnet.

### Vorab-Kriterien

| Kriterium | Wortlaut | Herkunft |
|---|---|---|
| (i) | Harmonische 1 und 2 beim 120-Grad-Dreieck auf Rundungsniveau (Code-Kontrolle). Die Quadratur ist C3-symmetrisch, also \|c1\|, \|c2\| < 1e-9 \|c0\| | Vorgabe der Leitung |
| (ii) | log-Steigung von c3 gegen d zwischen 2,5 und 3,5 k0, sonst verfehlt | Vorgabe der Leitung |
| (ii') | Steigung zwischen Nachbarabstaenden = 3 k0 + 3 ln(d2/d1)/(d2 - d1) +- 0,3 k0; c3 > 0 | eigene Vorhersage, getrennt markiert |
| (iii) | Gegenprobe 0/0/0: Steigung der ersten Harmonischen nahe k0 | Vorgabe der Leitung |
| (iii') | Steigung = k0 + ln(d2/d1)/(d2 - d1) +- 0,1 k0 | eigene Vorhersage |

- Zusatz: c3 der vollen Ueberlagerung gegen 6 beta J_33(d), also Paaranteil gegen echte Dreikoerperterme.
  - Erwartung: Verhaeltnis in [0,7; 1,3] bei d >= 10.
  - Nicht unabhaengig: dieselben Profile; das ist nur eine Zerlegung.
- Abstaende d = 8, 10, 12, 14; phi = 0, 30, ..., 330 Grad (12 Werte).
- Quadratur: Zylinderkoordinaten um die C3-Achse; der Azimut hat N = 3 x 128 gleiche Schritte, deshalb ist die
  C3-Symmetrie auf dem Gitter exakt. Energiedichte analytisch aus den Profiltabellen (f, f'), keine Differenzen.
  Zwei Aufloesungen.
- Zeitlauf (Drift der Spitze): nur wenn Zeit bleibt; wahrscheinlich nicht.

## 6. Kontrollen und Gitterstufen

- K1-1D: dx = 0,1 und 0,05. K2 und K1-3D: h = 0,1 und h = 0,15. K3: grob und fein, eingebaut. TET-1: zwei
  Quadraturstufen.
- Einzelball ohne Partner in jedem Stapel (Drift, Kraft null).
- Abstandsskalierung: drei bis sieben Abstaende je Kraft.

## 7. Kostenplan

- Lokal nur Rauchtests (CPU, 1 Faden, nice 19, timeout 120, CUDA_VISIBLE_DEVICES leer), Ausgaben nach lauf-lokal/.
- .69 ueber kleintest.sh aus /home/fmh/fmhc-physics-remote/runde9-kraft1/, Spuren p4000a/p4000b, je Aufruf <= 10 min.
- Schaetzung:
  - K2 + K1-3D je omega (13 Glieder x 158 000 Punkte, h = 0,1, T = 300, ~17 ms je Schritt): ~3 min; grob ~1 min
  - K3: ~2 min (grob und fein)
  - K1-1D: < 1 min
  - TET-1: ~1 bis 3 min
  - Summe ~15 GPU-Minuten, 6 bis 8 Aufrufe
- Rechnen etwa 08:45 bis 10:15, Bericht bis 11:15 (Zeitrahmen plus 45 min fuer TET-1).

## 8. Einordnung (Zusatz der Leitung 08:04; nur Papier, in ERGEBNIS.md)

- Teilchen-Wirbel-Dualitaet in 2+1D und Kalb-Ramond in 3+1D [L?]
- Akustische Metrik (Unruh 1981; Barcelo, Liberati, Visser) [L?]
- Zitate werden an der Quelle gelesen oder bleiben [L?].

## 9. Nachtrag 1 (2026-09-30 08:27:48 CEST, date; vor jedem Paarlauf auf der .69)

- **Rauchtests lokal** (CPU, 1 Faden, nice 19, h = 0,3, Zahlen der Paare ungueltig): lauf-lokal/rauch-bj/bericht.txt.
- **Streuphase l = 1** aus der Einzelball-Rechnung (streuphase_l1, Profil h = 0,01; Kontrolle ohne Ball -7e-7 rad):
  - 0,76 (rho_r = 1,7281501): **delta_1 = +0,2568 rad**
  - still (rho* = 1,7446175): delta_1 = +0,3643 rad; spielt keine Rolle, weil P = 0
- **Zusatz der Bearbeitung:** vierter Abstand d_4 = 30 + 3 lambda/4 = 31,9635. Damit liegen zwei Abstaende nahe den
  Baeuchen (d_2 und d_4, entgegengesetztes Vorzeichen); d_1 und d_3 liegen nahe einem Knoten.
- **Vorhersage K = F_B/P** (0,76, gleichphasige Atmung, + heisst Abstossung) und Delta d(300) mit P0 ~ 0,0105
  (Hand, +-30 %) und Retardierung:

| d | K vorhergesagt | Delta d(300) grob [Hand] |
|---|---|---|
| 30,0000 | +3,40e-3 | +0,015 |
| 30,6540 | +1,210e-2 | +0,052 |
| 31,3090 | -3,25e-3 | -0,014 |
| 31,9635 | -1,161e-2 | -0,050 |

- Kriterien, verschaerft durch den festen delta_1 (vorher so nicht moeglich):
  - Vorzeichen: d_2 positiv, d_4 negativ.
  - Verhaeltnis K_gemessen/K_vorhergesagt an d_2 und d_4 in [0,7; 1,3].
  - Phasenfit ueber alle vier Abstaende: chi innerhalb +-0,4 rad von 2 delta_1 = 0,514.
- **Kraftschalter:** still |Delta d(300)| < 5e-4 an allen vier Abstaenden, also 1 % von 0,05.

## 10. Nachtrag 2 (2026-09-30 08:34:28 CEST, date): Methodenwechsel K1-1D nach Rauchtest, Rauchtest-Befunde offengelegt

- **K1-1D, Methode geaendert nach dem ersten Rauchtest** (08:30, lauf-lokal/rauch-k1vak, grob, T = 15):
  - Die Anfangsbeschleunigung aus dem Schwerpunkt ist vom Einschwingen der Ueberlagerung verdorben: Grad-3- und
    Grad-4-Fits widersprechen sich, und Delta theta = 90 Grad gibt d'' != 0.
  - Neu ist eine integrale Messgroesse: Abstossende Paare (Delta theta = 180 und 120 Grad) laufen aus der Ruhe auseinander,
    **d'_inf = sqrt(4 E_int(d0)/E_1)**, gemessen als Steigung von d(t) auf [150, 200].
  - Die Entscheidungsregel bleibt:
    - Formel: Verhaeltnis d'_inf in [0,92; 1,07], entsprechend E_int in [0,85; 1,15]
    - R3: Verhaeltnis in [0,67; 0,77], entsprechend E_int in [0,45; 0,6]
- **Nicht mehr blind:** Der zweite Rauchtest (08:31, grob, T = 100, verkuerzt) zeigte schon d'_inf/Formel = 0,98 bei
  d0 = 10 und 12 fuer 180 Grad. Die Rechnung auf der .69 (T = 200, grob und fein) ist deshalb nur noch die Bestaetigung
  mit voller Laufzeit und zwei Gittern.
  - Nebenbefund des Rauchtests: Bei 90 und 120 Grad fliesst Ladung zwischen den Baellen (N rechts/links bis 1,45). Die
    Phase bleibt nicht fest, das cos-Gesetz gilt nur im Augenblick. Diese Laeufe sind nur beschreibend.
- **K1-3D:** Dieselbe Einschwingstoerung ist auch fuer die d''(0)-Fits der K1-3D-Glieder zu erwarten.
  - Massgeblich wird der gegenphasige K1-3D-Lauf (d0 = 12, T = 300): d'_inf = sqrt(4 E_int/M), Formel still 0,1078
    und 0,76 0,1115.
  - Die d''(0)-Werte bei 60, 90 und 120 Grad sind nur beschreibend.
- **TET-1, Rauchtest** (08:34, h = 0,3, N_alpha = 48, d = 8/10/12; Zahlen grob):
  - c1 und c2 beim 120-Grad-Dreieck ~1e-14 (Kriterium (i) funktioniert)
  - c3 > 0
  - Steigung 3,1 bis 3,3 k0
  - c3/c3_paar = 0,46 / 0,57 / 0,62
  - Damit ist meine eigene Vorhersage (ii') (3,56 bis 3,68 k0) auf grobem Gitter schon verfehlt, und das
    Zusatzkriterium "[0,7; 1,3]" auch. Beide bleiben unveraendert stehen. Die feine Rechnung entscheidet; blind ist sie
    nicht mehr.
- Versehen: Um 08:24 lief lokal einmal ein leerer Aufruf `python3 -` (Heredoc ohne Inhalt, keine Rechnung). Das ist ein
  Verstoss gegen die Regel "keine lokalen Interpreterstarts ausser Rauchtests"; vermerkt.
