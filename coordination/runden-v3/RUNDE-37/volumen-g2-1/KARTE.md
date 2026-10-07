# VOLUMEN-G2-1: Haelt eine Volumen-Bedingung die Umklapp-Dynamik stabil, wenn sie im laufenden Integrator mitgefuehrt wird? (schlanke Karte)

- Leitung claude-primary, geschrieben ab 2026-10-07 03:30:56 CEST (date), vor jeder Rechnung. Finn 07.10.: "mach mit der volumen-bedingung in G2 weiter".
- **Herkunft [P]:**
  - ANTIGRAVITY-NACHBAU-1 (AG2): Ein festes Gesamt-4-Volumen beim Zug macht s2 kinetisch positiv. Von 10 000
    Zufallsbedingungen schafft das nur eine. In s1 und s3 hilft es nicht. Es war nur eine Momentaufnahme.
  - NETZ-NICHTLINEAR-1: G2 scheiterte technisch, weil die Kontrolle N4 sofort abbrach (steife Moden, Leapfrog-Grenze).
    Teil B: Die Buchhaltung schliesst.
  - Unimodulare Gravitation [L]: Das Gesamtvolumen als Zwangsbedingung ist bekannt (Henneaux/Teitelboim u. a.).
- **Modell:**
  - H(l, p) mit M_eff(l) und B(l) am mitbewegten Netz, dazu die Zwangsbedingung V4(l) = const (Lagrange-Multiplikator).
  - Integrator: RATTLE bzw. implizite Mitte mit Projektion, adaptiver Schritt fuer steife Moden.
  - Netze s1 bis s4, A = 1e-3, 10 Perioden; Arme mit und ohne Bedingung.

## Erwartungen (vor jeder Rechnung)

| Nr | Erwartung | So kann sie scheitern | Wahrsch. |
|---|---|---|---|
| V0 | Kontrolle ohne Zuege: Energie und Bedingung auf 1e-8 bzw. 1e-10 erhalten (Integrator traegt) | Abbruch oder Drift > 1e-6 | 65 % |
| V1 | Mit Bedingung bleibt s2 ueber 10 Perioden beschraenkt, \|H - H0\|/H0 < 1e-3; ohne Bedingung waechst es | s2 waechst auch mit Bedingung, oder es bleibt auch ohne beschraenkt | 45 % |
| V2 | In s1 und s3 aendert die Bedingung die Kaskade nicht (wie in der Momentaufnahme) | Die Bedingung stabilisiert auch s1 oder s3 | 60 % |
| V3 | Der Lagrange-Multiplikator bleibt klein (Zwangskraft < 10 % der Netzkraefte); keine kuenstliche Versteifung | Zwangskraft dominiert | 50 % |

- Echt offen: V1 bis V3. V0 ist die technische Voraussetzung; ohne V0 sind V1 bis V3 "nicht erreicht".
- Synthetisch, keine Messdaten.
