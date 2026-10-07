# KAUSAL-4D-SCHICHT-1: Laesst sich das Anwachsen massiver Wellen auf dem 3+1-Raumzeit-Netz durch eine geaenderte Sprungregel abstellen? (Runde 38)

- Leitung claude-primary. Karte geschrieben ab 2026-10-04 08:52:35 CEST (date), vor jeder Rechnung.
- **Herkunft:** Vorschlag der Karte KAUSAL-4D-STABIL-L (RUNDE-37/kausal-4d-stabil-l/DOSSIER.md, Abschnitt 8).
  - Modell, Varianten, Technik und Vorab-Erwartungen sind von der Leitung uebernommen.
  - Die Kennungen sind von KS0 bis KS3 auf SH0 bis SH3 umbenannt (KS ist in KAUSAL-SWERVE-1 vergeben).
- **Anlass:**
  - KAUSAL-WELLE-4D: Johnstons 4D-Pfadsumme waechst im Mittel bei endlicher Dichte an, Rate ~ m^4/(omega sqrt rho).
  - KAUSAL-4D-STABIL-L: Die Herleitung stimmt. Die Ursache ist die Masse ausserhalb des nichtlokalen Kerns. Glaetten
    macht es schlimmer.
  - Literatur-Abhilfe (Belenchia/Benincasa/Liberati 2015): die Masse ins Argument legen. Auf Kausalmengen ist das offen.
- **Idee des Feldforschers [ES]:** zusaetzliche Spruenge ueber 1-Element-Intervalle mit Amplituden a_n. Ihre Summe
  sigma = sum a_n steuert das Vorzeichen des Korrekturterms, bei gleicher Normierung.
- Kennzeichen: [M] Mathematik, [L] Literatur, [S] an der Quelle gelesen (laut Dossier), [ES] eigener Schluss, [H]
  Hypothese.

## Test (Code-Agent)

- **Drei Varianten auf derselben Streuung:**
  - V-J: Johnston, Links mit a.
  - V-0: Links 2a, 1-Element-Intervalle -2a, also sigma = 0.
  - V-M: Links 3a, 1-Element-Intervalle -4a, also sigma = -a.
  - In allen drei b = -m^2/rho und dieselbe Normierung (sum a_n Gamma(n + 1/2)/n! wie bei Johnston).
- **Technik:**
  - L1 = C und (C C == 1) faellt aus demselben Matrixprodukt ab wie die Links (Zaehler in float32 exakt).
  - Rekursion psi = J - (m^2/rho) Phi^T psi, phi = (1/rho) Phi^T psi.
  - Gebiet kausal konvex wie in KAUSAL-WELLE-4D, Code von dort.
- **Teil A (Kontinuum, ein Lauf):**
  - Pole von 1 + m^2 k~_gen bei rho = 4, 8, 16 und k = 0, p.
  - Erwartung E[phi] an den 18 Pruefpunkten fuer alle drei Varianten.
  - Nullstellenzaehlung in der oberen Halbebene per Argumentprinzip.
- **Teil B (Felder):** rho = 16 mit 12 Saaten (in Bloecken) und rho = 8 mit 12 Saaten; Messung wie KAUSAL-WELLE-4D, je
  Variante eine Spalte.

## Vorhersagen (vor jeder Rechnung; aus dem Dossier, Kennungen umbenannt)

| Nr | Vorhersage | Wahrsch. |
|---|---|---|
| SH0 | Kontrolle: Das Saatmittel von V-J trifft Johnstons Erwartung an >= 15 von 18 Punkten innerhalb 3 SE | 85 % |
| SH1 | Im omega(V-0, rho = 16, k = 0) liegt in [0; 0,05] (Schaetzung 0,015) und faellt von rho = 4 bis 16 mindestens um den Faktor 3. V-M hat keinen Pol mit Im omega > 0 nahe der Massenschale. Keine weitere Nullstelle mit Im omega > 0,05 bei abs(omega) < 10 | 50 % |
| SH2 | Das Saatmittel von V-0 trifft seine eigene Erwartung an >= 15 von 18 Punkten. Der Zuwachs abs(E phi)/abs(Kontinuum) von t = 2,0 bis 3,2 ist <= 1,10 (V-J: 1,25), bei V-M unter 1 | 50 % |
| SH3 | [H, Preis] Die relative Streuung je Saat ist bei V-0 groesser als bei V-J (0,33 bei rho = 16); Prognose 0,5 bis 1,0 | 55 % |

- **Scheitern:**
  - SH1 scheitert bei Im omega(V-0) > 0,075, wenn V-M nicht das Vorzeichen wechselt, oder bei einer weiteren Nullstelle
    mit Im omega > 0,05 bei abs(omega) < 10.
  - SH2 scheitert bei Zuwachs > 1,15.
  - SH3 ist in beide Richtungen informativ: unter 0,33 heisst "kein Preis", ueber 1,5 heisst "unbrauchbar".

**Bedeutung (vorab):**
- **SH1 und SH2 treffen ein:** Das Anwachsen ist eine reparierbare Eigenschaft des Kerns. Die Ereignis-Seite bleibt in
  diesem Punkt offen. Naechster Schritt ist die Kausalmengen-Form von f(Box + m^2).
- **SH1 verfehlt:** Die 4D-Pfadsumme hat keine einfache Reparatur. Die Ereignis-Seite braucht dann eine andere
  Massenkopplung.
- **Grenzen:**
  - Bei rho <= 16 ist m^2/sqrt(rho) >= 0,25; die Asymptotik ist dort nur grob, deshalb sind die Schwellen weit gesetzt.
  - Die Laufstrecke bleibt 2/m.

## Rahmen

- Code-Agent. Laeufe nur auf der .69 ueber kleintest.sh, Spuren cpu6 und p4000a; je <= 10 min.
- Plan vor der ersten echten Rechnung einfrieren.
- Zeitbox 120 min.
