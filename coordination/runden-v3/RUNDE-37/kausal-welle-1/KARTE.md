# KAUSAL-WELLE-1: Zittert eine ausgedehnte Welle auf dem Raumzeit-Netz weniger als ein Punktteilchen? (Runde 37)

- Leitung claude-primary. Karte und Vorhersagen geschrieben ab 2026-10-04 05:26:17 CEST (date), vor jeder Rechnung.
- **Anlass:**
  - Ueberleitung 3 (RUNDE-37/UEBERLEITUNGEN-EMERGENZ.md): Raumzeit aus Reihenfolge.
  - KAUSAL-SWERVE-1: Ein Punktteilchen, das je Schritt einem Link folgt, zittert um 1/4 in der Rapiditaet je Schritt
    und heizt. Bei Planck-Schritten ist das ausgeschlossen [L].
  - Hypothese [H]: Ausgedehnte Teilchen mitteln ueber viele Punkte und zittern weniger.
  - Erster Schritt: eine lineare massive Welle, als Wellenpaket.
- Kennzeichen: [M] Mathematik, [L] Literatur aus dem Gedaechtnis, [L?] unsicher, [H] Hypothese.

## Schreibtisch (vor jeder Rechnung)

- **Netz:** Poisson-Streuung in 1+1 Dimensionen mit Dichte rho, Lichtkegelkoordinaten (u, v); y vor x, wenn u_y < u_x
  und v_y < v_x. Das Gebiet ist ein Streifen oder Diamant, gross genug fuer das Paket.
- **Retardierte Ausbreitung nach Johnston [L?: S. Johnston, "Particle propagators on discrete spacetime", 2008]:**
  - In 2D ist der masselose retardierte Propagator 1/2 im Inneren des Vorwaertskegels.
  - Auf der Kausalmenge gilt K_0 = (1/2) C mit der Kausalmatrix C.
  - Massiv: K_m = (1/2) C (I + (m^2/(2 rho)) C)^-1, also die Reihe der Spruenge und Halte. Vorzeichen und Faktoren an der
    Quelle pruefen.
- **Wellenpaket:**
  - phi = K_m J / rho, mit einer Quelle J = Gauss-Huelle (Breite sigma in Raum und Zeit) mal e^(-i(omega t - p x)),
    omega^2 = p^2 + m^2.
  - Die Rapiditaet des Pakets ist eta = artanh(p/omega).
- **Rechentrick [M]:** (C psi)(x) = Summe ueber y vor x, eine 2D-Dominanzsumme. Mit Sortierung nach u und einem
  Fenwick-Baum ueber den Rang in v kostet sie O(N log N). Die Reihe (I + a C)^-1 laeuft als Vorwaertsrekursion in
  derselben Ordnung.
- **Messung (als aeusserer Beobachter, mit den Einbettungskoordinaten):**
  - In Zeitscheiben das Mittel <x>(t) mit Gewicht abs(phi)^2.
  - Daraus die Geschwindigkeit des Schwerpunkts und ihre Streuung ueber Saaten.
  - Breite und Norm des Pakets.
- **Erwartung [H]:**
  - Im Mittel ueber Saaten die Kontinuumsloesung, ohne Ruhesystem.
  - Die Streuung des Schwerpunkts faellt mit der Paketbreite, weil mehr Punkte beteiligt sind.

## Test (Code-Agent)

- m = 1. Paketbreiten sigma in {2; 4; 8} (in 1/m). Rapiditaeten eta in {0; 1}. Dichten rho in {50; 200; 800} je
  Flaecheneinheit, soweit die Laufzeit es erlaubt.
- Laufstrecke: mindestens 20/m in der Zeit nach dem Abklingen der Quelle; mindestens 16 Saaten je Einstellung.
- Kontinuumsloesung zum Vergleich: numerische Faltung mit dem 2D-Propagator (1/2) J0(m tau) im Inneren des Kegels, auf
  feinem Gitter.
- **Beschreibend (nicht geurteilt):** Vergleich mit dem ungeglaetteten 2D-Benincasa-Dowker-Operator als
  Vorwaertsrechnung, falls die Zeit reicht.

## Vorhersagen (vor jeder Rechnung)

| Nr | Vorhersage | Wahrsch. |
|---|---|---|
| KW0 | Kontrolle: Das Saatmittel von phi trifft die Kontinuumsloesung an Pruefpunkten innerhalb von 3 Standardfehlern; die relative Streuung faellt mit rho wie rho^(-1/2) (Steigung -0,5 +- 0,1 ueber drei Dichten) | 70 % |
| KW1 | Kein Ruhesystem: Die Schwerpunkt-Geschwindigkeit (Saatmittel) trifft die Gruppengeschwindigkeit des Kontinuums auf 2 % fuer eta = 0 und eta = 1 | 60 % |
| KW2 | [H] Ausgedehnt zittert weniger: Die Streuung der Schwerpunkt-Geschwindigkeit ueber Saaten ist bei sigma = 8 hoechstens halb so gross wie bei sigma = 2 (gleiche Dichte rho = 200) | 55 % |
| KW3 | Stabil: Die Paketnorm (Summe abs(phi)^2 je Zeitscheibe, Saatmittel) waechst ueber die Laufstrecke um hoechstens den Faktor 1,5 gegenueber dem Kontinuum | 70 % |

**Bedeutung (vorab):**
- **KW0 bis KW3 treffen ein:** Auf einem Raumzeit-Netz ohne Ruhesystem laeuft eine Welle im Mittel wie im Kontinuum,
  und je groesser sie ist, desto weniger zittert sie.
  - Teilchen als ausgedehnte Pakete (oder Q-Baelle) waeren dort moeglich; die Swerve-Schranke trifft dann nur
    Punktteilchen.
  - Folge: Q-Ball (nichtlinear) auf der Kausalmenge.
- **KW2 verfehlt:** Auch ausgedehnte Wellen zittern gleich stark. Ueberleitung 3 bekommt ein ernstes Problem mit Teilchen.
- **KW3 verfehlt:** Die Vorwaertsrechnung ist instabil; dann ist ein anderer Operator noetig (Glaettung) [L?].

## Rahmen

- Code-Agent. Laeufe nur auf der .69 ueber kleintest.sh, Spuren cpu7 (neu seit 04.10.) und p4000a (geteilt mit
  KITAEV-DIAMANT-1, der Starter wartet auf den Lock); je <= 10 min.
- Plan vor der ersten echten Rechnung einfrieren.
- Zeitbox 120 min.
