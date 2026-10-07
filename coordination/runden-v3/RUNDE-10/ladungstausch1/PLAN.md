# LADUNGSTAUSCH-1 (Runde 10): Plan und Vorab-Erwartungen

- **Schreibbeginn: 2026-09-30 10:30:36 CEST (date), vor jedem Lauf dieser Karte.** Ende: letzte Zeile.
- Bearbeiter: derselbe Agent wie die ZUS-10-Pruefung (Fable). Auftrag: Leitung claude-primary, 10:26 CEST.
- Anlass: ZUS-10 Idee 7 (pruefung/ERGEBNIS.md): Das Q/Anti-Q-Paar bei d = 4 (omega^2 = 0,7, 1D) behaelt 48 % seiner
  Energie in |x| < 15 bis T = 3000, Feldfrequenz 0,80, 127 Vorzeichenwechsel der linken Ladung in t = 1000 bis 3000.
- Code: RUNDE-10/ladungstausch1/t5k_ladungstausch.py (Kopie der reparierten t5k_zus7.py; neu: --w2, d-Raster,
  gleichphasiges Q/Q-Kontrollpaar, Tauschfrequenz aus dem Spektrum von Q_links, spaete Verlustrate Gamma_E aus
  ln E15 ueber das letzte Drittel, t_halb). tests1d_r3.py unveraendert importiert (Profile nur fuer omega^2 = 0,60 /
  0,70 / 0,80 / 0,85 vorgerechnet).
- Rechenort: .69, /home/fmh/fmhc-physics-remote/runde10-ladungstausch1/; Rauchtest cpu6 (CPU, T = 60, grob), Hauptlaeufe
  p4000a, je hoechstens 10 min, zwei Gitterstufen grob (dx 0,1, dt 0,05) und fein (dx 0,05, dt 0,025), T = 3000.
- Quelle gelesen (PDF, Seiten 1 bis 5): Copeland, Saffin, Zhou, PRL 113, 231603 (2014), arXiv 1409.3232 [L]:
  laufende Masse V = m^2 phi^2/2 [1 + K ln(phi^2/2M^2)], K = -0,1, 2+1 Dimensionen; CSQ durch Ueberlagerung von Q- und
  Anti-Q-Ball mit |d_1 - d_2| = 1,6/m bei sigma = 3,16/m; empirische Bedingung |d_1 - d_2| <~ 2 sigma (Gl. 4, ueberlappende
  Kerne); Tauschperiode ~55/m gegen Eigenperiode 2 pi/(1,1 m) = 5,7/m; Lebensdauer mindestens O(10^4) Eigenperioden;
  Energiedichte wie ein einzelner Q-Ball; Anfangsphase unerheblich (Fig. 4); Mechanismus: 2 Phi + 2 Phi-quer -> Phi + Phi-quer
  im dichten Kern, phi_2 schwingt etwas schneller als phi_1, die langsame Phasendrift gibt die Tauschfrequenz.

## Laeufe (Reihenfolge)

- R0 Rauchtest cpu6: `--geraet cpu --kurz --w2 0.7 --d 4 --d-gleich 4`.
- R1 p4000a: `--w2 0.7 --d 3,4,5,6 --d-gleich 4 --d-theta 4 --T 3000` (7 Laeufe: Paare, Q/Q, theta = pi/2, Einzelball).
- R2 p4000a: `--w2 0.6 --d 3,4,5,6 --d-gleich 4 --T 3000`.
- R3 p4000a: `--w2 0.8 --d 3,4,5,6 --d-gleich 4 --T 3000`.
- R4 p4000a: `--w2 0.7 --d 4 --d-gleich 0 --kein-einzel --stufen fein --T 9000` (Lebensdauer ueber 3000 hinaus).
- Kosten (aus z7gpu: 5 Laeufe x 2 Stufen x T = 3000 in 209 s): R1 ~290 s, R2/R3 ~250 s, R4 ~80 s.

## Vorab-Erwartungen (Hand, [H]) und Scheiterregeln

- **Messgroessen:** E15 = Energie in |x| < 15 relativ zu t = 0; Feldfrequenz |Omega| aus psi(0, t) (Fenster t >= T/3,
  Aufloesung 2 pi/(2T/3) = 0,003 bei T = 3000); Tauschfrequenz Omega_swap = Hauptspitze des Spektrums von Q_links(t) im
  selben Fenster; Wechsel = Vorzeichenwechsel von Q_links im Fenster; Gamma_E = -d ln E15/dt ueber das letzte Drittel.
- **Definition "Ladungstausch-Ball (CSQ)":** E15(3000) >= 0,3, Wechsel >= 50 und |Omega| < omega. "Vernichtung":
  E15(3000) < 0,05.
- **E1 Schwelle in d (omega^2 = 0,7):** d = 3 und 4 bilden einen CSQ; d = 6 vernichtet; d = 5 [H, unsicher]: vernichtet.
  Aus CSZ Gl. 4 mit der Feld-Halbwertsbreite unseres Balls (f = f0/sqrt 2 bei x = 2,6, Hand aus f^2 = 2 a0/(1 + b0 cosh(2 sqrt(a0) x)),
  a0 = 0,3, b0 = 0,632): 2 sigma ~ 5, also Schwelle zwischen 4 und 6.
  - Scheitert (Messung): d = 4 reproduziert E15(3000) = 0,483 nicht auf 10 %.
  - Scheitert (Physik): d = 6 bildet einen CSQ (E15(3000) > 0,1) oder d = 3 bildet keinen (E15(3000) < 0,3).
- **E2 omega^2-Abhaengigkeit (d = 4):** CSQ auch bei 0,6 und 0,8 (E15(3000) >= 0,2); Feldfrequenz |Omega|/omega =
  0,956 +- 0,03 fuer alle drei (aus 0,80/0,837); Verlustrate Gamma_E(0,6) < Gamma_E(0,7) < Gamma_E(0,8) [H, schwach].
  - Scheitert: kein CSQ bei 0,6 oder 0,8 (E15(3000) < 0,1), oder |Omega|/omega ausserhalb 0,90 bis 1,00.
  - Die Ratenordnung ist nur eine Erwartung: verfehlt, wenn Gamma_E(0,6) > 2 Gamma_E(0,8).
- **E3 Tauschfrequenz:** Omega_swap(0,7; d = 4) = 0,20 +- 0,02 (aus 127 Wechseln in 2000 Zeiteinheiten:
  2 pi x 63,5/2000 = 0,1995); Omega_swap ist eine Eigenschaft des gebundenen Objekts: d = 3 und d = 4 stimmen auf 20 %.
  Modellbezug [H, schwach]: Omega_swap/omega steigt mit omega^2 (duennere Baelle, schwaechere Bindung).
  - Scheitert: Omega_swap(d = 3) und Omega_swap(d = 4) weichen um mehr als 30 % voneinander ab (dann ist es keine
    Eigenschaft des Objekts, sondern der Anfangsbedingung), oder Omega_swap(0,7; 4) ausserhalb 0,16 bis 0,24.
- **E4 Kontrollen:** Einzelball: E15 = 1 +- 1e-3, 0 Wechsel, |Omega| = omega +- 0,003. Q/Q gleichphasig d = 4: 0 Wechsel
  (beide Ladungen bleiben positiv), Q_links + Q_rechts am Ende = 2 q_ball +- 2 % (Ladung in |x| < 75), E15(3000) > 0,9,
  Feldfrequenz unter omega (verschmolzener groesserer Ball) [H].
  - Scheitert: Einzelball verliert Energie (E15 < 0,99) oder das Q/Q-Paar zeigt Vorzeichenwechsel.
- **E5 Gitter:** grob und fein stimmen fuer E15(3000) auf 5 % (relativ), fuer |Omega| und Omega_swap auf 1 % bzw. eine
  Aufloesungsbreite. Sonst nur die feine Stufe berichten und die Groesse als "unsicher" markieren.
- **E6 Bezug zu stillen Stellen:** Im 1D-Modell gibt es keine stillen Stellen der Atmung (R7 V7, R8: 1D bei 0,53 bis 0,88
  ohne Nullstelle). Die Frage "faellt die Abstrahlung, wenn eine Frequenz des Tauschballs eine stille Stelle trifft" ist
  hier **nicht pruefbar**; berichtet wird nur Gamma_E(omega^2) als Vorarbeit. Ein 3D-Gegenstueck (achsensymmetrische
  Q/Anti-Q-Ueberlagerung, koll1-artig) uebersteigt 10 min und diese Karte.
- **E7 Vergleich mit CSZ:** Tauschfrequenz unter der Eigenfrequenz (ja, 0,20 gegen 0,84); Schwelle im Abstand bei etwa
  2 sigma (Erwartung: zwischen 4 und 6); Anfangsphase unerheblich: das Paar d = 4 mit theta = pi/2 bildet ebenfalls einen
  CSQ (E15(3000) >= 0,3) [H]. Scheitert (fuer die Uebertragung von CSZ): theta = pi/2 bei d = 4 vernichtet.
- **Lebensdauer (R4):** E15 faellt von 3000 bis 9000 um weniger als den Faktor 2 (Gamma_E < 1,2e-4) [H, aus 0,590 -> 0,483
  zwischen 1000 und 3000, Rate 1,0e-4]. Scheitert: Faktor > 2.

**Ende des Plans: siehe date-Zeile unten.**

**Ende des Plans: 2026-09-30 10:31:38 CEST (date, nach dem Schreiben gemessen, vor dem ersten Lauf).**

## Nachtrag 2026-09-30 10:35:33 CEST (date): verfeinerte Hypothese zur Tauschfrequenz, vor den Ergebnissen R2/R3 (omega^2 = 0,6 / 0,8)

- Grundlage: nur die grobe Stufe von R1 (omega^2 = 0,7, Ausgabe um 10:34 CEST gelesen); R2 und R3 hatten zu diesem Zeitpunkt noch keine Ausgabedatei (ls auf der .69, siehe Zeile darueber im Terminalprotokoll).
- Beobachtung R1 grob: Omega_swap = 0,1979 bei d = 3, 4, 5; zweite Spitze des Q_links-Spektrums bei 1,7934 / 1,7965 / 1,7965; Feldfrequenz am Ursprung Omega_1 = 0,7978 / 0,8009 / 0,8009. Damit Omega_1 + Omega_2 = zweite Spitze gibt Omega_2 = 0,9956 in allen drei Faellen und Omega_2 - Omega_1 = 0,1978 / 0,1947 / 0,1947 = Omega_swap bis auf eine Aufloesungsbreite (0,003). Auch theta = pi/2: 0,7883 + 0,9957 = 1,7840, Differenz 0,2074 gegen gemessen 0,2104.
- **Hypothese [H] (CSZ-Mechanismus mit Zahlen):** Der gerade Feldanteil (Q plus Anti-Q in Phase) ist ein Oszillon bei Omega_1 < omega, der ungerade Anteil schwingt bei Omega_2 = 0,996 knapp unter der Masse; die Ladung tauscht mit Omega_swap = Omega_2 - Omega_1.
- **Vorhersage fuer R2/R3 (d = 4):** Omega_2 = 0,996 +- 0,005 auch bei omega^2 = 0,6 und 0,8; Omega_swap = 0,996 - Omega_1. Mit Omega_1 = 0,956 omega aus E2: Omega_swap(0,6) = 0,26 +- 0,03 und Omega_swap(0,8) = 0,14 +- 0,03. Das **widerspricht** meiner Erwartung E3 (Omega_swap/omega steigt mit omega^2); ich lasse E3 stehen und werte beide.
- Scheitert: |Omega_1 + Omega_2 - zweite Spitze| > 0,01 oder |Omega_swap - (Omega_2 - Omega_1)| > 0,01 bei 0,6 oder 0,8.
