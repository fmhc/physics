# Q-STERN-2: Herleitung (Newton-Grenzfall, volle Rechnung erster Ordnung mit delta Phi)

- Code-Agent, Runde 14. Geschrieben ab 2026-10-01 23:41:21 CEST (date), vor der ersten Codezeile.
- Markierungen: [ES] eigener Schluss, [H] Hypothese, [L?] aus dem Gedaechtnis. Einheiten wie qstern.py (Masse 1).
- Grundlage: RUNDE-13/q-stern/HERLEITUNG.md (Wirkung, Hintergrund, Cowling-Kanaele, Quelle rho_E). Dort Geprueftes
  wird hier nicht wiederholt.

## 1 Ausgangspunkt

- L = (1 - 4 Phi)|d_t phi|^2 - |grad phi|^2 - (1 - 2 Phi) U(|phi|^2), U = S - S^2 + S^3/2 (Karte, bindend).
- Euler-Lagrange nach phi* mit **zeitabhaengigem** Phi:
  lap phi = d_t[(1 - 4 Phi) d_t phi] + (1 - 2 Phi) U'(|phi|^2) phi.
  - Neu gegenueber Q-STERN ist nur, dass d_t nicht mehr an Phi vorbeigeht: d_t[(1 - 4 Phi) d_t phi] =
    (1 - 4 Phi) d_t^2 phi - 4 (d_t Phi) d_t phi.
- Poisson (Karte, bindend, instantan): lap Phi = alpha rho_E, rho_E = |d_t phi|^2 + |grad phi|^2 + U(|phi|^2).
  - Hintergrund: rho_E = omega^2 f^2 + f'^2 + U(f^2), wie Q-STERN. Die Quelle ist die flache Energiedichte; ihre
    Phi-Korrekturen waeren O(alpha Phi), also zweiter Ordnung in der Kopplung [ES].

## 2 Ansatz

- phi = e^{i omega t}(f + a e^{i rho t} + b e^{-i rho t}), a, b reell (Funktionen von r).
  - a schwingt mit omega + rho: offener Kanal (rho > 1 - omega). b mit omega - rho: geschlossener Kanal
    (rho < 1 + omega). Im Code: y2 = r a (Kanal 2, offen), y1 = r b (Kanal 1, geschlossen), wie qstern.py.
  - Q-STERN schrieb e^{-i omega t}; das ist dieselbe Entwicklung mit konjugierter Zeit [ES].
- Phi = Phi0(r) + psi(r) cos(rho t).
  - Das passt: Die Dichtestoerung ist |phi|^2 = f^2 + 2 f (a + b) cos(rho t) + O(2), also reell und phasengleich mit
    cos(rho t). Bei reellen a, b gibt es keinen sin-Anteil in der Quelle [ES].

## 3 delta rho_E in erster Ordnung

- Zeitterm: d_t phi = i e^{i omega t}[omega f + (omega + rho) a e^{i rho t} + (omega - rho) b e^{-i rho t}], also
  |d_t phi|^2 = omega^2 f^2 + 2 omega f [(omega + rho) a + (omega - rho) b] cos(rho t).
- Gradiententerm: |grad phi|^2 = f'^2 + 2 f' (a' + b') cos(rho t).
- Potentialterm: U(|phi|^2) = U(f^2) + 2 U'(f^2) f (a + b) cos(rho t).
- **delta rho_E = sigma(r) cos(rho t)**, sigma = 2 [omega f ((omega + rho) a + (omega - rho) b) + f' (a' + b')
  + U'(f^2) f (a + b)]. Alle drei Terme erster Ordnung sind enthalten (Karte: legt die Herleitung fest) [ES].
- psi-Gleichung: psi'' + (2/r) psi' = alpha sigma. Mit u = r psi, y = r w (l = 0):
  u'' = 2 alpha [(Pa - Pb rho) y1 + (Pa + Pb rho) y2 + f' (y1' + y2')],
  Pa = (omega^2 + U'(f^2)) f - f'/r, Pb = omega f.
  - Herkunft von -f'/r: r (a' + b') = (y1' + y2') - (y1 + y2)/r [ES].
  - Am Ursprung ist f'/r endlich: f'/r -> f''(0) = G(f(0), Phi0(0))/3 (aus f'' + (2/r) f' = G) [ES].

## 4 psi-Terme in den Kanalgleichungen

- Aus -4 d_t[psi cos(rho t) d_t(f e^{i omega t})] = 2 omega f psi [(omega + rho) e^{i(omega + rho)t} +
  (omega - rho) e^{i(omega - rho)t}] und aus -2 psi cos(rho t) U'(f^2) f e^{i omega t} = -U' f psi [e^{i(omega+rho)t}
  + e^{i(omega-rho)t}] [ES]:
  - offen:       y2'' = C y1 + (A - B rho - D rho^2) y2 + (Ea + Eb rho) u
  - geschlossen: y1'' = (A + B rho - D rho^2) y1 + C y2 + (Ea - Eb rho) u
  - Ea = f (2 omega^2 - U'(f^2)), Eb = 2 omega f; also E_offen = f [2 omega (omega + rho) - U'],
    E_geschlossen = f [2 omega (omega - rho) - U'].
  - A, B, C, D wie Q-STERN: A = (1 - 2 Phi0) dp - (1 - 4 Phi0) omega^2, B = 2 omega (1 - 4 Phi0),
    C = (1 - 2 Phi0) sp, D = 1 - 4 Phi0.
- **Pruefung der Karte: psi kommt nur mit f multipliziert vor** (Ea, Eb ~ f). Ebenso die Quelle von u (Pa, Pb, f').
  Beides faellt mit f exponentiell ab, e^{-kappa0 r} r^(eta - 1). Die Kanalasymptotik (Schwellen 1 -+ omega,
  Coulomb-Schwanz von Phi0) bleibt dieselbe wie in Q-STERN. **Bestaetigt** [ES].

## 5 Randbedingungen fuer psi

- Regulaer bei 0: u(0) = 0 (u = r psi).
- psi(inf) = 0: Aussen ist die Quelle exponentiell klein, also u'' = 0, u = c0 + c1 r. psi(inf) = 0 verlangt c1 = 0,
  also u'(R) = 0 und psi = c0/r aussen [ES].
  - c0 ist frei (eine schwingende Monopol-Masse). [H] In der ART verbietet Birkhoff ein schwingendes aeusseres
    Monopolfeld; im Newton-Modell mit Quelle rho_E ist c0 nicht erzwungen null. Grenze, Abschnitt 8.

## 6 Kein Wronski-Satz mehr; Auslesen von W und s

- Mit psi ist das System nicht mehr reell-symmetrisch [ES]:
  - y <- u: E = f [2 omega (omega -+ rho) - U']
  - u <- y: 2 alpha [(omega (omega -+ rho) + U') f - f'/r] plus der Ableitungsterm f' y'
  - Grund: Die Quelle rho_E ist nicht die Variation der Wirkung nach Phi. Die waere 4 |d_t phi|^2 - 2 U
    (rho + 3 p, Vermerk Q-STERN). Mit ihr waere die Kopplung symmetrisch.
- Folge:
  - Die Wronski-Summe ist nicht erhalten.
  - "La = Lb = 0" ist nicht mehr gleichbedeutend mit einer stillen Stelle.
  - In Q-STERN folgte die Gleichwertigkeit daraus, dass die regulaeren Loesungen einen Lagrange-Unterraum bilden.
- **Wahl: erweiterter Loesungsraum am Ursprung und am Rand, exakte Abhaengigkeitsbedingung** [ES]:
  - Innen: drei regulaere Loesungen, Start y2' = 1 (Ya), y1' = 1 (Yb), u' = 1 (Yu), alle anderen Startwerte 0.
    Integration nach aussen bis r_m.
  - Aussen: zwei stille Loesungen, integriert von R nach innen bis r_m:
    - Z1: y1 = 1, y1' = -kappa_c + eta_c/R (wie Q-STERN), y2 = y2' = u = u' = 0
    - Z2: u = 1, sonst alles 0 (psi = c0/r aussen)
  - Stille Stelle = es gibt eine Loesung, die innen regulaer und aussen still ist. Das heisst: die fuenf
    6-Vektoren (y1, y2, u, y1', y2', u') bei r_m sind linear abhaengig.
  - Elimination von u: Zu X in {Ya, Yb, Z1} bilde X^ = X + p Yu + q Z2 mit u(r_m) = u'(r_m) = 0. Das 2x2-System
    [Yu, Z2] in (u, u') ist regulaer (Yu ~ (r_m, 1), Z2 ~ (1, 0)). Dann gilt exakt:
    - Abhaengigkeit der fuenf 6-Vektoren <=> Abhaengigkeit der drei 4-Vektoren (y1, y2, y1', y2') von Ya^, Yb^, Z1^.
    - Beweis in beide Richtungen ueber die u-Komponenten [ES].
  - V = span(Ya^, Yb^), Z_perp = euklidischer Anteil von Z1^ senkrecht zu V.
    **W = Omega(Ya^, Z_perp) + i Omega(Yb^, Z_perp)**, Omega(y, z) = y1 z1' - y1' z1 + y2 z2' - y2' z2.
    - W = 0 <=> Z1^ in V <=> stille Stelle, solange P_perp J^T V den Raum V_perp aufspannt (in der Naehe von
      alpha = 0 gegeben).
    - **Bei alpha = 0 gleich dem alten W:**
      - u bleibt fuer Ya, Yb, Z1 identisch null (Quelle ~ alpha), also Ya^ = Ya, Z1^ = Z1.
      - V ist Lagrange, also ist Omega(Y, Z1 - Z_perp) = 0.
      - Damit W = Omega(Ya, Z1) + i Omega(Yb, Z1) = La + i Lb wie qstern.py, bis auf den Diskretisierungsrest der
        Lagrange-Eigenschaft. Umlauf und Lage gehen stetig aus Q-STERN hervor; K1 prueft das.
    - s = Re W an den Nullstellen von Im W, wie bisher.
    - Die Lage der Stelle haengt nicht von r_m ab. Die Phase von W haengt fuer alpha > 0 schwach (O(alpha)) von r_m
      ab; jedes Profil nutzt sein eigenes r_m = Km h.
  - Warum nicht einfacher:
    - "Abklingende Kombination, dann offener Anteil" hat Scheinnullstellen, wo beide regulaeren Loesungen schon
      abklingen. Bei alpha = 0 entartet die Nullstelle dort.
    - "La = Lb = 0" ist im unsymmetrischen System eine andere Bedingung; sie verfehlt die Stelle um O(alpha), also um
      die Groesse des gesuchten Effekts.
- Coulomb-Phase: Der offene Kanal von Z1, Z2 ist bei R exakt null, und aussen koppelt nichts in ihn ein. Die Kopplungen
  C ~ f^2 und E ~ f sind bei R relativ kleiner als 1e-6. Die Coulomb-Phase geht darum wie in Q-STERN nicht in W ein.
  Der Rest O(f(R)) ist die Groesse, die K3 prueft.
- Cowling-Vergleich (psi = 0, --psi null): derselbe Code mit dem unveraenderten Q-STERN-Pfad (W_reell, W_multi aus
  qstern.py). K4 prueft ihn gegen Q-STERN.

## 7 K5 (Restpruefung der psi-Gleichung)

- An der lokalisierten Stelle: Nullvektor der 6x5-Anpassungsmatrix, daraus die Loesung auf [0, R] zusammengesetzt.
- u_G aus der Integralform der Poisson-Gleichung mit derselben Quelle und denselben Randbedingungen:
  u_G' = -int_r^R g, u_G = int_0^r u_G', mit g = 2 alpha [...] aus Abschnitt 3.
  - Kumulatives Trapez mit Euler-Maclaurin-Korrektur wie qstern.cum_int.
- Rest = max |u - u_G| / max |u|. Er enthaelt den RK4-Fehler O(h^4) und den Lagefehler der Lokalisierung. Mitgeteilt
  wird auch sigma_min/sigma_max der Anpassungsmatrix.

## 7a Nachtrag (2026-10-01 23:59:14 CEST, date): Vertreter von Z2

- Der Rauchtest rauch-a2-voll (23:48, erste Codefassung) zeigte Pole von W bei rho ~0,36 und ~1,57 .. 1,61.
  - Dort sind Nullstellen von Im W mit |s|/median bis 4e5, und s wechselt "durch unendlich".
  - Ursache: Z2 (u = 1 aussen) nimmt nach innen einen grossen, nach innen wachsenden geschlossenen Anteil auf. Der ist
    Z1-artig. Ueber 2 alpha f y1 wandert er in u, und der u-Block von (Yu, Z2) bei r_m wird singulaer (det = 0).
- Behebung im Code vor dem Einfrieren:
  - Z2 wird durch Z2 - gamma Z1 ersetzt, gamma = (Z2_y1 Z1_y1 + Z2_y1' Z1_y1')/(Z1_y1^2 + Z1_y1'^2) bei r_m.
  - Das ist eine Spaltenoperation innerhalb des stillen Raums. Der Raum und damit die Lage der Stelle bleiben exakt
    gleich; nur die Parametrisierung von W aendert sich.
  - Bei alpha = 0 aendert sich nichts, weil Ya, Yb, Z1 dort keinen u-Anteil haben.
  - rauch-a2-voll-b: Pole weg, Lage ziffergleich (0,78364321 / 1,72975971).

## 8 Grenzen

- Newton-Grenzfall, instantanes Potential, ein Potential (Phi = Psi), Quelle rho_E (nicht rho + 3 p), erste Ordnung
  in Phi und in der Schwingung.
- Schwingende Monopolmasse c0 aussen erlaubt (kein Birkhoff).
- Nur l = 0, Grundzustand.
