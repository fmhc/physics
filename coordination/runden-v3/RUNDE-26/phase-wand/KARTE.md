# PHASE-WAND: Sagt die ebene Wand auch die Lage der Sprossen voraus, nicht nur den Abstand? (Runde 26)

- Leitung: claude-primary. Karte und Vorhersagen geschrieben ab 2026-10-03 03:54:00 CEST (date), vor jeder Rechnung.
- Finn, ~03:53: "Mach weiter".
- **Herkunft:**
  - WAND-BETA, LEITER-BETA und LEITER-1D: Die ebene Wandnullstelle rho_z sagt den Grenzschritt der Leiter ohne Eichung
    voraus, in 3D (1/eps) und in 1D (ln(1/eps)).
  - Das Papier (Abschnitt "thin-wall phase-matching") fuehrt die Wandphase theta und die Niveauverschiebung c als geeicht.
    "The coupled planar wall problem has not been solved here to predict both functions independently."
  - c_inf = rho_z - omega_min ist jetzt aus der Ebene bekannt. Offen ist die **Wandphase**.
- **Schreibtisch der Leitung [H]:**
  - An der ebenen Wand hat die total reflektierte Loesung (aussen nur abklingend, innen ohne wachsende Mode) im Plateau die
    Form e1 cos(k_in (x - x_w) + phi) plus abklingend.
    - x_w ist die Wandlage mit S(x_w) = S_c/2.
    - phi ist die Reflexionsphase bei rho_z.
  - In 1D (Waende bei +-x_w(eps)) folgt fuer gerade Moden cos(k x) und ungerade sin(k x):
    - k_in x_w(eps_n) = n pi - phi (gerade bzw. n pi + pi/2 - phi, ungerade; Vorzeichenkonvention im Plan festlegen)
    - x_w(eps) folgt aus dem exakten 1D-Profil (erste Integralform)
    - Daraus ergeben sich die absoluten Lagen eps_n ohne freien Parameter.
  - In 1D gilt fuer beta = 1: S_c = 1/2, lambda^2 = 2 S_c U''(S_c) = 1, k_in(rho_z(1)) = 2,39943. Der Grenzschritt ist also
    Delta ln(1/eps) = lambda pi/k_in = 1,3093.
- **Ableitbarkeitspruefung:**
  - Die fuenf 1D-Sprossen bei beta = 1/2 sind bekannt (RUNDE-25/leiter-1d); die Formel ist neu und wird nicht an sie
    angepasst. Die Phase kommt nur aus der ebenen Rechnung.
  - 1D-Sprossen bei beta = 1 sind nirgends gerechnet.

## Test (Code-Agent)

1. **Phase phi(beta)** fuer beta = 1/2 und 1, aus der ebenen Rechnung (Vorlage RUNDE-24/wand-beta/code/wand_beta.py).
   - Bei rho_z die aussen abklingende Loesung nach innen integrieren und im Plateau auf e1 projizieren:
     A cos(k x) + B sin(k x).
   - Daraus die Phase bezueglich x_w, sauber definiert und im Plan festgehalten.
2. **Formel** fuer die 1D-Lagen eps_n (beide Paritaeten), aus phi, k_in und dem exakten Profil x_w(eps). Herleitung und
   Vorzeichen stehen im Plan, vor jedem Vergleich.
3. **Pruefung an bekannten Daten:** beta = 1/2, Vergleich mit den fuenf Sprossen aus RUNDE-25/leiter-1d.
4. **Echte Vorhersage:** beta = 1, die ersten Sprossen in eps [1e-8; 0,05] aus der Formel.
   - Die Zahlen werden **vor** der 1D-Leiterrechnung bei beta = 1 eingefroren.
   - Danach die 1D-Leiter bei beta = 1 rechnen (Code RUNDE-25/leiter-1d/code/leiter_1d.py, auf beta verallgemeinert, neue
     Fassung) und vergleichen.

## Vorhersagen (vor jeder Rechnung)

| Nr | Vorhersage | Wahrsch. |
|---|---|---|
| PW1 | beta = 1/2: Die Formel trifft die bekannten Sprossen 3 bis 5 (eps < 1e-4) innerhalb +-2 % in ln(1/eps) und mit der richtigen Paritaet | 60 % |
| PW2 | beta = 1: Es gibt 1D-Sprossen; die zwei kleinsten-eps-Schritte liegen innerhalb +-5 % von 1,3093 | 60 % |
| PW3 | beta = 1: Die eingefrorene Formel trifft jede Sprosse mit eps < 1e-3 innerhalb +-3 % in ln(1/eps), mit richtiger Paritaet | 45 % |

**Bedeutung (vorab):**
- PW1 und PW3 treffen ein: Die ebene Wand liefert Abstand **und** Lage der Leiter ohne Eichung (in 1D).
  - Damit sind theta und c des Papiers im Duennwandgrenzfall berechnet statt geeicht [H, 1D].
- PW1 trifft ein, PW3 nicht: Die Formel ist bei beta = 1/2 brauchbar, aber nicht uebertragbar. Beschreiben, z. B.
  Endlichkeitskorrekturen oder eine falsche Phasenkonvention.
- PW2 trifft nicht ein: Die 1D-Leiter bei beta = 1 fehlt oder liegt ausserhalb. Beschreiben.

## Rahmen

- Code-Agent. Laeufe nur auf der .69 ueber kleintest.sh (CPU-Spuren; je <= 10 min, 4 GB).
- Plan mit Formel und Konventionen vor dem ersten Vergleich einfrieren. Die beta-1-Vorhersagezahlen werden getrennt
  eingefroren, bevor die beta-1-Leiter gerechnet wird.
- **Zielwerte nie als Befehlszeilen-Argumente auf der .69** (Memory: feedback-blind-angebot-ohne-zahlen). Startwerte und
  Kandidaten ueber Dateien.
- Zeitbox 120 min.
