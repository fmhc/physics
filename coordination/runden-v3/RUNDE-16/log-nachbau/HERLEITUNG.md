# HERLEITUNG (LOG-NACHBAU, Runde 16)

- Verfasst: 2026-10-02 ab 08:02:50 CEST (date), vor der ersten Codezeile. Eigene Herleitung des Code-Agenten.
- Status: Methode. Keine Ergebnisse.

## 1 Profil

- Lagrangedichte |d_t phi|^2 - |grad phi|^2 - U(|phi|^2). Bewegungsgleichung: phi_tt - lap phi + U'(|phi|^2) phi = 0.
- Ansatz phi = f(r) e^{i w t}: f'' + (2/r) f' = (U'(f^2) - w^2) f. Randbedingungen f'(0) = 0, f -> 0, f > 0 ohne Knoten.
- Teilchenbild: f'' = -dPhi/df - (2/r) f' mit Phi(f) = (w^2 f^2 - U(f^2))/2. Bei U'(0) = 1 und w < 1 ist f = 0 ein
  Hochpunkt von Phi. Start bei Ruhe in f0, Reibung 2/r. Ein Q-Ball braucht Phi(f0) > 0.
  - Log: U(S)/S = ln(1+S)/S faellt von 1 gegen 0, also gibt es fuer jedes 0 < w^2 < 1 ein f0 mit Phi(f0) > 0.
  - Kontrolle: U(S)/S = 1 - S + S^2/2 hat das Minimum 1/2, also w^2 > 1/2. Der Hochpunkt liegt bei
    U'(x) = w^2, x_top = (2 + sqrt(6 w^2 - 2))/3, f0 < sqrt(x_top).
- Asymptotik: f ~ A e^{-mu r}/r mit mu = sqrt(1 - w^2) (U'(0) = 1).
- Groesse im Fenster (Log): fuer w^2 -> 1 wird der Ball duenn (U'(S) ~ 1 - S, kubische NLS-Grenze), f0 ~ mu,
  Radius ~ 1/mu. Bei w^2 = 0,98 ist 1/mu = 7,1; bis f^2 < 1e-20 braucht es mu r ~ 25, also r ~ 180.
- Schiessverfahren (zweiseitig):
  - aussen-Zweig: von r = 0 mit f = f0, f' = 0; am Ursprung f''(0) = (U'(f0^2) - w^2) f0 / 3.
  - innen-Zweig: von R_in mit dem Yukawa-Schwanz f = A e^{-mu r}/r nach innen (dort stabil, die gesuchte Loesung
    waechst nach innen).
  - Anschluss bei r_p = 2,5/mu in f und f'; Newton in (f0, A). Startwert f0 aus Mehrfachbisektion
    (Ueberschuss f < 0, Unterschuss f' > 0).
  - R_in = r_p + 16/mu; dort ist f/f(r_p) ~ e^{-16} ~ 1e-7, f^2 ~ 1e-17. Dahinter gilt der Yukawa-Schwanz bis auf f^2.
- Ladung und Energie: Q = 8 pi w Int f^2 r^2 dr, E = 4 pi Int (w^2 f^2 + f'^2 + U(f^2)) r^2 dr.

## 2 Linearisierung l = 0

- phi = e^{i w t} (f + psi), psi = a(r) e^{i rho t} + b(r) e^{-i rho t}.
- Linear in psi: psi_tt + 2 i w psi_t - w^2 psi - lap psi + U'(f^2) psi + f^2 U''(f^2) (psi + psi*) = 0.
- Koeffizient von e^{i rho t} bzw. e^{-i rho t} (a, b reell; die Gleichungen sind reell, also gibt es reelle Loesungen):
  - -lap a + [V - (w + rho)^2] a + g b = 0
  - -lap b + [V - (w - rho)^2] b + g a = 0
  - V = U'(f^2) + f^2 U''(f^2), g = f^2 U''(f^2).
  - Kontrolle: V = 1 - 4 f^2 + 4,5 f^4, g = f^2 (3 f^2 - 2).
  - Log: V = 1/(1 + f^2)^2, g = -f^2/(1 + f^2)^2.
- Mit u = r a, v = r b (l = 0): u'' = [V - (w+rho)^2] u + g v, v'' = [V - (w-rho)^2] v + g u.
  Die Koeffizientenmatrix M ist symmetrisch und am Ursprung regulaer (keine 1/r-Terme in dieser Form).

### Asymptotik (r -> oo: V -> 1, g -> 0)

- a-Kanal: u'' = -k^2 u, k^2 = (w + rho)^2 - 1. b-Kanal: v'' = kappa^2 v, kappa^2 = 1 - (w - rho)^2.
- Im Fenster 1 - w < rho < 1 + w (0 < w < 1, rho > 0) gilt w + rho > 1 und |w - rho| < 1: a offen, b geschlossen.
- Offener Kanal: u ~ alpha sin kr + beta cos kr; auslaufend e^{ikr}. Geschlossener Kanal: v ~ gamma e^{kappa r}
  + delta e^{-kappa r}; physikalisch gamma = 0 (abfallend).

### Regulaere Loesungen am Ursprung (zwei)

- u(0) = v(0) = 0, a(0) und b(0) frei: Y_a mit (a(0), b(0)) = (1, 0), Y_b mit (0, 1), also u'(0) = a(0), v'(0) = b(0).
- Die singulaeren Loesungen (a ~ 1/r) sind ausgeschlossen.

## 3 Abstrahlamplitude W und Kenngroesse s

- Wronski-Form: W[Y, Z] = u_Y u_Z' - u_Y' u_Z + v_Y v_Z' - v_Y' v_Z. Weil M symmetrisch ist, haengt sie nicht von r ab.
- Raum der regulaeren Loesungen R = span(Y_a, Y_b): W[Y_a, Y_b] = 0 (bei r = 0 verschwinden u und v). R ist
  zweidimensional und isotrop im vierdimensionalen Loesungsraum mit nicht ausgearteter Form W, also Lagrange-Raum:
  R^perp = R.
- Z_d: die bis auf den Faktor eindeutige Loesung ohne Welle im offenen Kanal und mit abfallendem geschlossenem Kanal,
  normiert auf v ~ e^{-kappa r}. Sie ist die einzige zulaessige Aussenform eines gebundenen Zustands.
- **Stille Stelle** (gebundener Zustand im Kontinuum, keine Abstrahlung) <=> eine regulaere Loesung ist quadratintegrabel
  <=> Z_d liegt in R <=> G_a = G_b = 0 mit G_x = W[Y_x, Z_d].
  - "=>": liegt Z_d in R, ist W[Y, Z_d] = 0 fuer alle Y in R (Isotropie).
  - "<=": G_a = G_b = 0 heisst Z_d in R^perp = R (Lagrange).
- Auswertung: ausserhalb der Kopplung ist W[Y_x, Z_d] = -2 kappa gamma_x, also
  G_x = -e^{-kappa R}(kappa v_x(R) + v_x'(R)) am Aussenrand R. Nur der wachsende Anteil des geschlossenen Kanals geht ein;
  es wird keine Welle angepasst. Die Normierungen (Y_x am Ursprung, Z_d im Unendlichen) sind glatt und positiv, Nullstellen
  und Umlaufzahl haengen nicht davon ab.
- Bedeutung von G_a: in erster Ordnung in der Kopplung g ist G_a = -Int_0^oo g(r) u_a^0(r) v_d^0(r) dr (Green-Formel mit
  W' = 0). Das ist das Ueberlappintegral der Goldenen Regel: die Amplitude, mit der der Zustand des geschlossenen Kanals
  ueber g in die regulaere Welle des offenen Kanals abstrahlt. G_b = 0 ist die Quantisierungsbedingung des geschlossenen
  Kanals (ohne Kopplung genau die Bindungsbedingung des b-Kanals).
- **Definitionen:**
  - Abstrahlamplitude W(w^2, rho) = G_a + i G_b.
  - Geschlossene Bedingung: G_b(w^2, rho) = 0 (Kurven in der Ebene; je Zeile w^2 Nullstellen in rho).
  - Kenngroesse s = G_a an diesen Nullstellen: die Abstrahlamplitude des Zustands des geschlossenen Kanals.
  - Stille Stelle: W = 0. Jede gemeinsame Nullstelle von G_a und G_b ist nach dem Lagrange-Argument eine echte stille
    Stelle. Ein Vorzeichenwechsel von s entlang einer Kurve G_b = 0 zeigt eine an.
  - Umlauf: Phase von W auf einem kleinen Rechteck um die Stelle, Zuwaechse auf (-pi, pi] gewickelt, Summe / 2 pi.
    Bei nicht ausgearteter Jacobi-Matrix d(G_a, G_b)/d(w^2, rho) ist er +-1.
- Warum nicht die Jost-Determinante D = det[Y_a, Y_b, Z_d, Z_aus] (auslaufende Welle): D ist die Abstrahlamplitude der
  Loesung G_b Y_a - G_a Y_b. Nahe einer stillen Stelle gilt D ~ c (rho - rho_r(w^2) + i Gamma(w^2)/2) mit einer Breite
  Gamma >= 0, die quadratisch verschwindet. Die Phase von D macht deshalb keinen Umlauf (0). D verschwindet an der Stelle,
  taugt aber nicht fuer das Umlaufkriterium. Das ist eine Hypothese aus der Herleitung (Fano-Bild), nicht gemessen.

## 4 Phasenumlauf

- Rechteck mit Halbbreiten 1e-3 in w^2 und rho um die lokalisierte Stelle, gegen den Uhrzeigersinn in der
  (w^2, rho)-Ebene. Anfangs 16 Punkte je Kante. Jeder Abschnitt mit einem Phasensprung >= 0,4 rad wird halbiert,
  hoechstens 6 Runden. Aufgeloest heisst: groesster Sprung < 0,4 rad.
