# G2-03 Klein-Stufe: Ein Q-Ball neben einer ueberkritischen Potentialstufe waechst, statt zu zerfallen

- Hypothese: Koppelt man die Ladung eines ruhenden 1D-Q-Balls an ein statisches aeusseres Potential V(x), das im Abstand D
  auf V0 springt, so verliert der Ball Ladung durch die Stufe, wenn seine Frequenz dort in den Teilchenast faellt
  (V0 > 1 - omega), gewinnt aber Ladung, wenn sie in den Antiteilchenast faellt (V0 < -(1 + omega)); dazwischen bleibt er
  stabil, und in beiden offenen Faellen faellt die Rate wie exp(-2 sqrt(1 - omega^2) D) [H].
- Bezug zur Grundlagenphysik [H]: klassisches Gegenstueck zum Klein-Paradoxon und zur Paarerzeugung in ueberkritischen
  Feldern: Ein Zustand positiver Norm koppelt an ein Kontinuum negativer Norm, die Ladung des Balls waechst, Gegenladung
  laeuft davon.

- Papier vorab [S] (eigene Rechnung, von Hand):
  - Modell: L = |(d_t - i V(x)) psi|^2 - |psi_x|^2 - U(S), U = S - S^2 + S^3/2, eine Raumdimension.
    V(x) = V0 (1 + tanh((x - D)/w))/2, w = 1. Ball omega^2 = 0,70 (omega = 0,8367), ruhend bei x = 0, wo V ~ 0.
  - Mit psi ~ e^{-i Om t} gilt weit hinter der Stufe (Om + V0)^2 = k^2 + 1, also Om = -V0 +- sqrt(k^2 + 1). Das
    Vorzeichen von Om + V0 ist das Normvorzeichen des Zweigs (Teilchen +, Antiteilchen -).
  - Offene Kanaele bei Om = omega:
    - Teilchenast (Om + V0 >= 1): V0 >= 1 - omega = 0,163. Der Ball leckt gewoehnlich: Q_Ball faellt, positive Ladung
      laeuft davon.
    - Antiteilchenast (Om + V0 <= -1): V0 <= -(1 + omega) = -1,837. Negative Norm: Q_Ball waechst, negative Ladung laeuft
      davon; die Gesamtladung bleibt erhalten.
    - Dazwischen (-1,837 < V0 < 0,163): kein offener Kanal, der Ball ist stabil.
  - Zwischen Ball und Stufe faellt das Feld wie e^{-kappa x}, kappa = sqrt(1 - omega^2) = 0,5477. Die Kopplung an das
    Kontinuum geht wie e^{-kappa D}, die Rate wie e^{-2 kappa D}: Steigung von ln|dQ_Ball/dt| gegen D = -1,095. Der Anteil
    der Stufenzone ist ein fester Faktor und aendert die Steigung nicht.
  - Groessenordnung (Vorfaktor 0,1 bis 1, nicht bindend): |dQ/dt|/Q ~ 1e-5 bis 2e-4 bei D = 8, ~2e-7 bis 2e-6 bei D = 12.
  - Waechst der Ball, sinkt omega (1D-Familie: Q steigt zu omega^2 -> 0,5); die Schwelle 1 + omega sinkt mit, der
    Antiteilchenast bleibt offen. Gemessen wird nur die Anfangsrate (Q-Zuwachs unter 20 %).

- Kleiner Test:
  - Code-Basis: RUNDE-05/r5b/r5b.py (1D-Anker, Profil, Messhilfen) als Kopie; neuer Zeitschritt in Hamiltonform mit
    pi = D_t psi: psi_t = pi + i V psi, pi_t = psi_xx - U'(S) psi + i V pi; Strang-Teilung (V-Teil als exakte Drehung um
    V dt/2 vor und nach einem Verlet-Schritt). Der Schwamm daempft pi (eichkovariant), nicht psi_t. Neuer Code etwa 45 min.
  - Box +-150, Schwamm ab |x| = 120, dx = 0,1, dt = 0,02 (fein dx = 0,05, dt = 0,01), T = 1200.
  - Laeufe (omega^2 = 0,70, Ball ruhend bei x = 0):
    - Antiteilchenast: V0 = -2,0 bei D = 8 / 10 / 12
    - Teilchenast: V0 = +0,40 bei D = 8 / 10 / 12
    - Polung: V0 = +2,0 bei D = 10 (Teilchenast)
    - zwischen den Schwellen: V0 = -1,5 und V0 = +0,10 bei D = 8
    - Gegenproben: zwei Laeufe (unten); zusammen 11 Laeufe
  - Rechenort: .69 ueber kleintest.sh, p4000a (grob, Stapel), p4000b (fein fuer V0 = -2,0 und +0,40 bei D = 10);
    geschaetzt 3 bis 6 min.
  - Messgroessen: Q_Ball (Fenster |x| < 15); Q_fern (x > D + 5 bis zum Schwamm plus vom Schwamm geschluckte Ladung);
    Ladungsfluss j(x = D + 5, t); dQ_Ball/dt aus einem Geradenfit auf t = 200 bis 800; omega(t) in der Ballmitte.

- Vorhersage vorab:
  - V1 (Kern): V0 = -2,0: dQ_Ball/dt > 0 bei allen drei D; der Fluss j(D + 5) zeigt nach aussen und traegt negative
    Ladung, Q_fern < 0. (Dass Q_fern dem Zuwachs von Q_Ball entspricht, ist Ladungserhaltung und gehoert zur
    Plausibilitaet, nicht zur Vorhersage.)
  - V2: V0 = +0,40 und V0 = +2,0: dQ_Ball/dt < 0; der Fluss j(D + 5) traegt positive Ladung nach aussen, Q_fern > 0.
  - V3: Die Steigung von ln|dQ_Ball/dt| gegen D ist -1,095 +- 0,16 (+- 15 %), fuer V0 = -2,0 und fuer V0 = +0,40.
  - V4: V0 = -1,5 und V0 = +0,10: |dQ_Ball/dt|/Q < 1e-8 (auf dem Raster kein Fluss).
  - **Scheitert, wenn** eines davon eintritt:
    - bei V0 = -2,0 faellt Q_Ball, oder der Fluss bleibt bei D = 8 unter der Aufloesung
    - die Steigung nach V3 liegt ausserhalb -0,93 bis -1,26
    - zwischen den Schwellen fliesst mehr als 1e-8 Q pro Zeiteinheit
  - Nicht entscheidbar, wenn die Plausibilitaetsschranke reisst.

- Gegenprobe:
  - V0 = 0, D = 8: Q_Ball konstant auf 1e-9 Q pro Zeiteinheit. Ohne Stufe verschwindet der Effekt.
  - Ohne Ball, V0 = -2,0, Anfangsrauschen 1e-8: max|psi| bleibt bis T unter 1e-6. Die Stufe allein erzeugt kein Wachstum.

- Plausibilitaetsschranke:
  - Noether-Ladung (Ball + fern + vom Schwamm geschluckt) auf 1e-8 relativ erhalten; Energie mit statischem V bis zum
    ersten Schwammkontakt auf 1e-6
  - Q_Ball > 0; |Q_fern| <= |Delta Q_Ball| + 1e-6; omega(t) in der Mitte bleibt unter 1

- Latten erwartet:
  - L1 ja: Vorzeichen, Schwellen und Steigung koennen je einzeln scheitern.
  - L2: V0 = 0, Stufe ohne Ball, die zwei Werte zwischen den Schwellen.
  - L3: dx/2 und dt/2: dQ/dt auf 10 %, Steigung auf 0,05.
  - L4 teilweise: Klein-Paradoxon und Superradianz an einer Stufe fuer Bosonen (Klein 1929; Manogue 1988) sowie
    ueberkritische Bindung mit Paarerzeugung (Greiner, Mueller, Rafelski) [L?, aus dem Gedaechtnis, nicht nachgelesen].
    Eine Rechnung, in der ein nichtlinearer Q-Ball dabei waechst, kenne ich nicht [H].
  - L5: nein. Ueberkritische Schwerionenstoesse ohne klaren Befund [L?]; kein Zahlvergleich.

- Einfach gesagt: Ein Q-Ball liegt ruhig neben einer Stufe in einem aeusseren elektrischen Potential. Ist die Stufe klein,
  passiert nichts. Ist sie sehr hoch und richtig gepolt, kann das Feld des Balls durch die Luecke "tunneln" und jenseits der
  Stufe als Gegenladung davonfliegen; weil die Gesamtladung erhalten bleibt, wird der Ball dabei groesser statt kleiner.
  Das ist das klassische Gegenstueck dazu, wie in sehr starken Feldern Teilchen-Antiteilchen-Paare entstehen. Wir sagen
  voraus: Wachstum nur bei der einen Polung, Schrumpfen bei der anderen, und je weiter der Ball von der Stufe weg liegt,
  desto langsamer, nach einer festen Formel.

- Karte geschrieben: 2026-09-30 10:59:40 CEST
- Vorhersage geschrieben: 2026-09-30 11:16:14 CEST
