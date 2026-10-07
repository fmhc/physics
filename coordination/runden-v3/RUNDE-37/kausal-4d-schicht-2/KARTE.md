# KAUSAL-4D-SCHICHT-2: Laesst sich auch der Rest des Anwachsens Ordnung fuer Ordnung abstellen, und was kostet es? (Runde 39)

- Leitung claude-primary. Karte und Vorhersagen geschrieben ab 2026-10-04 09:59:10 CEST (date), vor jeder Rechnung.
- **Anlass:**
  - KAUSAL-4D-SCHICHT-1 plus Gegenlesen: Mit Links 2a und 1-Element-Intervallen -2a (sigma = 0) verschwindet der
    1/sqrt(rho)-Term. Der Rest folgt 3M^6/(16 rho omega).
    - Gegenleser, B1: "im Mittel um eine Ordnung in m^2/sqrt(rho) unterdrueckt, nicht abgestellt".
    - B4: sigma = 0 muss exakt gelten (Feinabstimmung).
  - Herleitung (RUNDE-37/kausal-4d-stabil-l/ARBEITSFELD.md, Schritte B bis D):
    - k~ = 1/Z^2 + eps [ln(Z^2/sqrt c) + C'] + O(eps Z^2/sqrt c).
    - Der ln-Term traegt den Faktor sigma = sum a_n. Die naechste Ordnung haengt an einem weiteren Moment der
      Schichtgewichte.
- **Frage:** Kann man mit einer dritten Schicht (2-Element-Intervalle) eine zweite Bedingung erfuellen, so dass auch der
  Rest 3M^6/(16 rho omega) wegfaellt? Und waechst der Rauschpreis mit jeder abgestellten Ordnung?
- Kennzeichen: [M] Mathematik, [L] Literatur, [ES] eigener Schluss, [H] Hypothese.

## Test (Code-Agent)

- **Schreibtisch zuerst:**
  - Die Momentbedingungen der Schichtkoeffizienten a_0 (Links), a_1 (1-Element-Intervalle) und a_2 (2-Element-
    Intervalle) fuer drei Forderungen herleiten:
    - gleiche Normierung
    - sigma = 0
    - Verschwinden der naechsten Ordnung
  - Das gibt die Variante V-00 mit eindeutigen Koeffizienten. Die Restformel von V-00 vorab angeben.
- **Teil A (Erwartung und Pole):** V-J, V-0 und V-00 bei rho = 4, 8, 16, k = 0 und p; Nullstellenzaehlung wie in
  SCHICHT-1.
- **Teil B (Felder):** rho = 16, 12 Saaten, alle drei Varianten auf derselben Streuung. 2-Element-Intervalle aus
  (C C == 2), wie die 1-Element-Intervalle aus demselben Matrixprodukt.
- Code aus RUNDE-37/kausal-4d-schicht-1/code/ wiederverwenden.

## Vorhersagen (vor jeder Rechnung)

| Nr | Vorhersage | Wahrsch. |
|---|---|---|
| S2-0 | Kontrolle: V-0 gibt den Pol aus SCHICHT-1 wieder (Im omega = 0,0147 bei rho = 16, k = 0, auf 1e-3) | 90 % |
| S2-1 | [H] V-00: Massenschalen-Pol bei rho = 16 mit Im omega < 0,004 (oder kein Pol mit Im omega > 0 nahe der Massenschale), und der Wert faellt von rho = 4 bis 16 schneller als bei V-0 | 45 % |
| S2-2 | [H] Preis: Die relative Streuung je Saat ist bei V-00 groesser als bei V-0 (0,636 bei rho = 16) | 70 % |
| S2-3 | Keine weitere Nullstelle mit Im omega > 0,05 bei abs(omega) < 10 fuer V-00 | 60 % |

**Bedeutung (vorab):**
- **S2-1 trifft ein:** Das Anwachsen laesst sich Ordnung fuer Ordnung abstellen, mit je einer exakten Bedingung an die
  Schichtgewichte (Feinabstimmung je Ordnung, B4).
  - Mit S2-2 waere das der Preis: mehr Rauschen je abgestellter Ordnung. Er bestimmt, wie weit man gehen kann.
- **S2-1 verfehlt:** Die naechste Ordnung haengt nicht nur an den Schichtgewichten, und das Schema ist begrenzt.

## Rahmen

- Code-Agent. Laeufe nur auf der .69 ueber kleintest.sh, Spuren cpu6 und p4000a; je <= 10 min.
- Plan vor der ersten echten Rechnung einfrieren.
- Zeitbox 120 min.
