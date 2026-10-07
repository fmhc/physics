# G2-04 Gleiten haengt an der Masse der Mediumsquanten: Im masselosen Medium bricht die Bremskraft erst bei u ~ 0,9 ein

- Hypothese: Ueber der Schallschwelle haengt die Bremskraft auf einen gehaltenen Q-Ball im stroemenden Zwei-Feld-Medium
  von der Stroemungsgeschwindigkeit u nur ueber die Bugwellenzahl k'(u) = sqrt((2 omega0 gamma u)^2 - 2g) ab
  (Formfaktor des Balls bei dieser Wellenzahl); macht man die Mediumsquanten leichter (mc2 = 1 -> 0,25 -> 0), rutscht der
  Einbruch der Kraft deshalb von u = 0,53 auf 0,74 und 0,90 [H].

- Papier vorab [S] (eigene Rechnung, von Hand):
  - Modell wie RUNDE-06/medium1d (Ball in der Falle, Medium adiabatisch auf u hochgefahren, Lorentz-Impuls):
    V = U(S) + mc2 C + g4 C^2 + lam S C, U = S - S^2 + S^3/2; C0 = 0,1, g4 = 0,5, lam = 0,1, Ball omega^2 = 0,7.
    Damit g = 2 g4 C0 = 0,1 und omega0^2 = mc2 + g.
  - Stehende Bugwelle: Om(k) = u k im Mediumsystem, im Ballsystem k' = k/gamma. Aus der Dispersion
    (k^2 - Om^2)(k^2 - Om^2 + 2g) = 4 omega0^2 Om^2 folgt geschlossen k'^2 = (2 omega0 gamma u)^2 - 2g (gleich der Funktion
    kielwelle() im Code). Fuer grosse u ist k' ~ 2 p mit p = omega0 gamma u, dem Impuls eines Mediumsquants
    (Rueckstreuung).
  - Schallgeschwindigkeit c_s^2 = g/(2 omega0^2 + g): mc2 = 1: 0,2085; mc2 = 0,25: 0,3536; mc2 = 0: 1/sqrt(3) = 0,5774
    (im masselosen Medium unabhaengig von der Dichte).
  - Bekannte Kurve bei mc2 = 1 (u; k'; F): 0,30; 0,485; 1,33e-3 (groesster Wert) / 0,50; 1,126; 2,23e-4 /
    0,60; 1,508; 3,92e-5 / 0,70; 2,007; 2,82e-6 / 0,80; 2,761; 2,44e-7 / 0,90; 4,308; 4,6e-9.
    - F faellt auf ein Zehntel des groessten Werts bei k'_10 = 1,24 (log-linear zwischen u = 0,50 und 0,60), also bei
      u_10 = 0,53.
  - Ist F = P(u) Phi(k') mit langsam veraenderlichem Vorfaktor P, liegt u_10 fuer jedes mc2 bei k' = 1,24:
    - mc2 = 0,25: u_10 = 0,744; mc2 = 0: u_10 = 0,902.
    - Spanne fuer einen Vorfaktor bis Faktor 3 (k'_10 zwischen 0,9 und 1,6): u_10 = 0,65 bis 0,815 (mc2 = 0,25) und
      0,85 bis 0,935 (mc2 = 0).
  - Zwei Gegenbilder mit anderem Ausgang:
    - G-u: Der Einbruch haengt nur an u (etwa ueber die Lorentz-Kontraktion des Balls). Dann u_10 = 0,53 fuer alle mc2.
    - G-Mach: Der Einbruch haengt an u/c_s (bekannt 0,53/0,2085 = 2,55). Dann u_10 = 0,90 bei mc2 = 0,25 und kein
      Einbruch unter u = 1 bei mc2 = 0.

- Kleiner Test:
  - Code-Basis: Kopie von RUNDE-06/medium1d/medium1d.py mit einem neuen Unterbefehl nach dem Muster von test_gleiten;
    mc2 je Lauf ueber lauf(..., mc2=...) gesetzt (die Hilfsfunktionen om0, schall, k_stroemung, c_start, kielwelle nehmen
    mc2 schon als Argument). Sonst unveraendert: periodische Box 600, Rampen, Falle, Messfenster [370, 570], grob dx 0,1 /
    dt 0,05 und fein dx 0,05 / dt 0,025. Neuer Code unter 30 min.
  - Laeufe (lam = 0,1, C0 = 0,1, Lorentz-Stroemung):
    - mc2 = 0: u = 0,20 / 0,30 / 0,40 / 0,55 / 0,65 / 0,75 / 0,82 / 0,86 / 0,90 / 0,93 / 0,96
    - mc2 = 0,25: u = 0,30 / 0,40 / 0,50 / 0,60 / 0,66 / 0,72 / 0,78 / 0,84 / 0,90
    - mc2 = 1 (Anschluss an die bekannte Kurve): u = 0,30 / 0,50 / 0,60
    - Gegenproben: drei Laeufe (unten); zusammen 26 Laeufe
  - Rechenort: .69 ueber kleintest.sh, p4000a (grob) und p4000b (fein), je Aufruf als Stapel etwa 2 bis 4 min.
  - Umlaufprobe: Schall aus dem Einschalten (t < 100) laeuft hoechstens mit Lichtgeschwindigkeit und braucht fuer den
    Umlauf in der Box 600 mindestens 600 > 570 Zeiteinheiten, auch bei c_s = 0,577.
  - Messgroessen: F = stationaere Kraft des Mediums auf den Ball (Hann-Mittel wie im Original); F_max je mc2 = groesster
    Rasterwert; u_10 = erster Schnitt von F/F_max = 0,1 oberhalb des Maximums (log-linear zwischen Rasterpunkten).

- Vorhersage vorab:
  - V1 (Kern): u_10(mc2 = 0) = 0,90 (Spanne 0,85 bis 0,935); u_10(mc2 = 0,25) = 0,74 (Spanne 0,65 bis 0,815).
  - V2: Im masselosen Medium gilt F(0,90)/F_max = 0,10 (Spanne 0,03 bis 0,3); bei mc2 = 1 ist es 3,5e-6.
  - V3: Das Gleiten kommt zurueck, nur spaeter: mc2 = 0: F(0,96)/F_max = 1e-4 bis 1e-2 (k' = 2,12); mc2 = 0,25:
    F(0,90)/F_max = 1,2e-4 bis 3e-3 (k' = 2,40).
  - V4 (Anschluss): mc2 = 1 gibt F(0,30), F(0,50), F(0,60) auf 15 % wie die bekannte Kurve (1,33e-3 / 2,23e-4 / 3,92e-5).
  - V5: mc2 = 0, u = 0,20 (0,35 c_s): |F| < F_MIN = 2e-6.
  - **Scheitert, wenn** eines davon eintritt:
    - u_10(mc2 = 0) liegt ausserhalb 0,85 bis 0,935 oder u_10(mc2 = 0,25) ausserhalb 0,65 bis 0,815
    - bei mc2 = 0 faellt F bis u = 0,96 nicht unter F_max/10 (Gegenbild G-Mach)
    - u_10 ist bei allen drei mc2 gleich auf 0,05 (Gegenbild G-u)
  - Nicht entscheidbar, wenn V4 reisst (Aufbau weicht vom bekannten ab) oder die Fallenbilanz an den beiden
    Rasterpunkten um u_10 um mehr als 30 % reisst.

- Gegenprobe:
  - lam = 0, mc2 = 0, u = 0,90: |F| < 1e-10. Ohne Kopplung verschwindet die Kraft.
  - Spiegel mc2 = 0, u = -0,90: F(-u) = -F(u) auf 2 %.
  - Medium allein mc2 = 0, u = 0,90: C raeumlich konstant (Spanne < 1e-9), am Ende C0 auf 1e-3.
  - Sammelprobe: Traegt man F/F_max ueber k' auf, liegen die drei mc2-Kurven oberhalb ihres Maximums bis
    F/F_max = 1e-3 innerhalb eines Faktors 3 zusammen. Ueber u aufgetragen liegen sie nicht zusammen.

- Plausibilitaetsschranke:
  - Fallenbilanz |F_med + F_Falle| <= max(0,2 |F_med|, F_MIN) im Messfenster
  - Ladung beider Felder auf 1e-6 relativ erhalten; "S gehalten" auf 1 %; u < 1; c_start > 0
  - F >= 0 in Stroemungsrichtung (u > 0)

- Latten erwartet:
  - L1 ja: u_10 bei zwei mc2 und das Verhaeltnis bei u = 0,9 koennen einzeln scheitern; zwei benannte Gegenbilder.
  - L2: lam = 0, Spiegel, Medium allein; mc2 = 1 als Anschluss.
  - L3: dx/2 und dt/2; u_10 auf 0,01, F auf 10 %.
  - L4 teilweise: Die Bremskraft auf ein schwaches Hindernis im 1D-Kondensat folgt dem Betrag der Fourier-Transformierten
    bei der Cherenkov-Wellenzahl [L?: Astrakharchik und Pitaevskii 2004; Pavloff 2002; aus dem Gedaechtnis, nicht
    nachgelesen]. Den Umzug des Einbruchs mit der Masse der Mediumsquanten im relativistischen Medium kenne ich nicht [H].
  - L5 Analogie: c_s^2 = 1/3 ist die Schallgeschwindigkeit eines Strahlungsgases (fruehes Universum,
    Quark-Gluon-Plasma) [L?]; Bezug nur als Hypothese, kein Zahlvergleich.

- Einfach gesagt: Ein festgehaltener Q-Ball in einer stroemenden Feldsuppe wird gebremst, bei sehr schneller Stroemung
  aber kaum noch, weil er die dann sehr kurzen Wellen nicht mehr anregen kann. Wie kurz diese Wellen sind, haengt davon ab,
  wie schwer die Teilchen der Suppe sind. Wir sagen voraus: Mit leichteren Suppenteilchen setzt dieses "Gleiten" erst bei
  hoeherer Geschwindigkeit ein, bei masselosen erst bei etwa 90 % der Lichtgeschwindigkeit statt bei 53 %. Haengt das
  Gleiten dagegen nur an der Geschwindigkeit selbst, ist die Idee falsch.

- Karte geschrieben: 2026-09-30 10:55:55 CEST
- Vorhersage geschrieben: 2026-09-30 11:16:14 CEST
