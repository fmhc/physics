# G1-09 Blase im Tropfen: Eine Leere im duennwandigen Q-Ball kollabiert nach Rayleigh, im endlichen Ball schneller

- **Hypothese:** Eine kugelfoermige Leere (S = 0) im Innern eines grossen duennwandigen 3D-Q-Balls kollabiert wie eine
  leere Kavitationsblase in einem Fluessigkeitstropfen: getrieben nur von der Wandspannung sigma der Innen- und der
  Aussenwand, gebremst von der Traegheit rho = 2 omega^2 S_c; ihre Kollapszeit folgt ohne freien Parameter der
  Energiebilanz der inkompressiblen Kugelschale und ist wegen der endlichen Ballgroesse kuerzer als in unbegrenzter
  Q-Materie.
- **Papier vorab [S]:**
  - Energiebilanz (Leere R, Aussenradius R_d, Volumen fest: R_d^3 = R_d0^3 - R0^3 + R^3):
    2 pi rho R^3 (dR/dt)^2 (1 - R/R_d) = 4 pi sigma [(R0^2 - R^2) + (R_d0^2 - R_d^2)].
  - Unbegrenzt und ohne Aussenwand: t bis R = 0 ist 0,618 sqrt(rho R0^3/sigma), bis R = 0,7 R0 davon 77,7 %, also
    t_70 = 0,480 sqrt(rho R0^3/sigma).
  - omega^2 = 0,52 (Duennwandschaetzung, das Programm rechnet genau): S_c = 1,019, rho = 1,060, sigma ~ 0,354,
    Druck p = 0,0202, R_d ~ 2 sigma/p ~ 35, Schall in Q-Materie c_Q ~ 0,71.
  - Fuer R0 = 8 / 12 / 18 (R0/R_d = 0,23 / 0,34 / 0,51): t_70 unbegrenzt 18,8 / 34,5 / 63,5; mit Aussenwand und
    Schalenfaktor grob x 0,80 / 0,71 / 0,58, also etwa 15 / 25 / 37. Die Wand erreicht bei 0,7 R0 unbegrenzt etwa
    0,35 / 0,29 / 0,24, mit Endlichkeit etwa 0,4 bis 0,45, also Mach 0,3 bis 0,6 gegen c_Q; der groesste Teil der Zeit
    vergeht langsam, bis t_70 also ueberwiegend inkompressibel. Kompressibilitaet macht den Kollaps eher langsamer.
- **Kleiner Test:**
  - Code-Basis: RUNDE-05/r5a/r5a.py (3D radial: Profil, sigma = Int 2 f'^2 dr, Innendruck, Zeitentwicklung mit
    Daempfungsschicht); schafft das Schiessen dort omega^2 = 0,52 nicht, das Profil aus RUNDE-06/resonanz3d/resonanz3d.py
    nehmen (dort bei 0,52 gerechnet). Neu (hoechstens 45 min): Anfangszustand psi(r, 0) = f(r) w(r) mit
    w(r) = f(R_d - (r - R0))/f(0) (gespiegelte Aussenwand als Innenwand), psi_t = i omega psi (keine Anfangsstroemung);
    Verfolgung von R_v(t) (innerer Radius mit S = S_c/2), R_d(t), Ladung und Energie.
  - Vor dem Lauf: T_E(R0) = Zeit bis R = 0,7 R0 aus der Energiebilanz mit sigma, rho, R_d0 des gerechneten Profils
    (Quadratur, Sekunden). Diese drei Zahlen sind die bindende Vorhersage und stehen in der Ausgabe vor den Laufwerten.
  - Laeufe: omega^2 = 0,52; R0 = 8 / 12 / 18; Kontrolle R0 = 0; T = 120; grob und mit halbem dr und dt.
  - Rechenort: Laptop-CPU (1 Thread, nice 19) oder .69 cpu; geschaetzt unter 2 min.
- **Vorhersage vorab:**
  - V1: gemessenes t_70 liegt fuer alle drei R0 innerhalb +- 15 % von T_E.
  - V2 (Endlichkeit, wie Blasen in Tropfen): t_70/t_70(unbegrenzt) faellt von R0 = 8 nach R0 = 18 um mindestens 0,10
    (grob erwartet 0,80 -> 0,58).
  - V3: R_v faellt bis 0,7 R0 monoton; kein Stillstand und kein Rueckprall vorher.
  - **Scheitert, wenn** ein t_70 mehr als 15 % von T_E abweicht, oder die Verkuerzung durch die Endlichkeit fehlt
    (Abfall < 0,10), oder die Leere vor 0,7 R0 stehen bleibt oder sich wieder oeffnet (dann haelt etwas anderes als
    Traegheit gegen die Wandspannung, z. B. Phasenmoden).
- **Gegenprobe (Effekt muss verschwinden):** R0 = 0 (Ball ohne Leere): kein Kollaps, R_d(t) bleibt auf 0,2 genau,
  S(0) auf 1e-3 konstant, radiale Stroemung im Innern < 1e-4.
- **Plausibilitaetsschranke:** Ladung und Energie in der Box erhalten (1e-4 relativ, bis Strahlung die Daempfung
  erreicht); Wandgeschwindigkeit < c_Q < 1 bis t_70; Inkompressibilitaet R_d^3 - R_v^3 konstant auf 5 % bis t_70.
- **Latten erwartet:** L1 ja (drei Ausgaenge: Rayleigh mit Endlichkeit, Rayleigh ohne Endlichkeit, anderer Mechanismus);
  L2 R0 = 0; L3 halbes dr und dt, t_70 auf 2 % gleich; L4 teilweise (Blasen in Q-Ball-Stoessen und die
  Rayleigh-Plateau-Instabilitaet von Q-Faeden sind Literatur, der Kollaps einer Leere in Q-Materie nicht gefunden);
  L5 nein (Analogon: Kavitationsblasen in Wassertropfen unter Schwerelosigkeit leben kuerzer als in grossem Volumen;
  deren Zahl rechnen wir hier nicht nach).
- **Einfach gesagt:** Ein grosser Q-Ball verhaelt sich wie ein Wassertropfen. Stanzt man in seine Mitte ein kugelrundes
  Loch, sollte es zuklappen wie eine Luftblase im Wasser, und die Zeit dafuer laesst sich aus Oberflaechenspannung und
  Dichte vorher ausrechnen. In einem kleinen Tropfen klappt die Blase schneller zu als im grossen See, weil weniger
  Fluessigkeit mitbewegt werden muss. Stimmen beide Zahlen, ist das Tropfenbild auch fuer heftige Bewegungen richtig.
- Karte geschrieben: 2026-09-30 07:41:43 CEST

- Vorhersage geschrieben: 2026-09-30 07:58:24 CEST
