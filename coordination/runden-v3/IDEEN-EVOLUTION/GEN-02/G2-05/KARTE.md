# G2-05 Einfang ist nicht geometrisch: Kugelwelle (l = 0) auf einen 3D-Q-Ball

- **Hypothese [H]:** Ein 3D-Q-Ball faengt Quanten seines eigenen Feldes nicht geometrisch ein (Wahrscheinlichkeit etwa 1
  fuer jedes Quant, das ihn trifft), wie es Rechnungen zum Wachstum durch Ladungsaufsammeln vereinfachend annehmen.
  Dauerhaft gefangen wird nur ueber den Umwandlungskanal Teilchen -> Antiteilchen (nu > 2 omega + 1), und dort
  nur zu Prozenten, wie in 1D.

- **Papier vorab [S]:**
  - Linear koppelt die Welle bei nu an den Partner bei 2 omega - nu. Offen ist er nur fuer |2 omega - nu| > 1, fuer
    einlaufende Teilchen also bei nu > 2 omega + 1: 2,483 (omega^2 = 0,55), 2,673 (0,70), 2,897 (0,90).
  - Aus der Erhaltung der Teilchenzahl der beiden gekoppelten Moden folgt je Umwandlung:
    - ein Teilchen (Ladung +1, Energie nu) hinein, ein Antiteilchen (Ladung -1, Energie nu - 2 omega) hinaus
    - der Ball gewinnt also Ladung 2 und Energie 2 omega, dE/dQ = omega exakt
    - unter der Schwelle kann linear keine Ladung dauerhaft bleiben; gespeicherte Ladung laeuft wieder aus
  - 1D (vorhandene Rechnung, gleiches Potential U = S - S^2 + S^3/2):
    - ueber der Schwelle bei 0,55: C_Q = 0,060 / 0,052 / 0,042 (nu = 2,6 / 2,8 / 3,0), Born-Rechnung 0,070 / 0,054 /
      0,044
    - bei 0,70 um 7e-4, bei 0,90 null
    - dE/dQ = 0,742 bis 0,759 bei omega = 0,7416
  - 3D-Ball bei 0,55 nahe der Duennwand: R_halb = 14,4 (vorhandene 3D-Radialrechnung). Bei nu = 2,6 ist k = 2,4, also
    k R um 35; geometrisch waere die s-Welle dort voll absorbiert.
  - Die s-Welle laeuft durch die Mitte und ueber zwei Wandstellen. Die Born-Amplitude kommt bei grossem Delta k vor
    allem von den Waenden [S]. Daher erwarte ich dieselbe Groessenordnung wie in 1D, mit Faktor 5 Spielraum.

- **Kleiner Test:**
  - Code-Basis:
    - Paket, Fenster, Partnerlaeufe und Born-Schaetzung (Kopplung U''(S) S) aus RUNDE-07/r5f/r5f.py, Befehl fuettern
    - 3D-Profil aus dem radialen Schiessen in RUNDE-05/r5a/r5a.py (dm1 = 2)
  - Neu, unter 1 h:
    - radiale 3D-Zeitentwicklung fuer u = r psi mit u(0) = 0 und Schwamm aussen
    - einlaufendes Kugelschalen-Paket (sigma = 32, eps = 0,01), Start ausserhalb des Ballschwanzes
    - Born-Schaetzung der s-Welle im Code vor der Zeitentwicklung
  - Laeufe:
    - omega^2 = 0,55 bei nu = 1,2 / 2,0 (unter der Schwelle) und 2,6 / 2,8 / 3,1 (darueber)
    - omega^2 = 0,70 bei nu = 2,0 (unter) und 2,8 / 3,1 (ueber)
    - Gegenproben: Paket allein (0,55-Box, nu = 2,8); omega^2 = 0,90 bei nu = 3,1
  - Messung: C_Q = dauerhafter Ladungsgewinn im Ballfenster (Ball plus Paket minus Ball allein) je einlaufender
    Paketladung, nachdem die auslaufenden Wellen das Fenster verlassen haben; dazu gespeicherte Ladung gegen t, dE/dQ,
    Spektrum der auslaufenden Welle (Linie bei nu - 2 omega).
  - Rechenort: .69, Spur cpu oder p4000a (radial, 1D-Gitter), zwei Aufrufe grob und fein (dr/2, dt/2), je unter 10 min.

- **Vorhersage vorab:**
  - V1 (nicht geometrisch, ueber der Schwelle):
    - 0,55: C_Q bei nu = 2,6 / 2,8 / 3,1 je in [0,005; 0,2]
    - 0,70: C_Q bei nu = 2,8 / 3,1 je in [1e-4; 0,02]
    - geometrischer Einfang gaebe etwa 1
  - V2 (unter der Schwelle): C_Q am Laufende < 0,01 bei 0,55 (nu = 1,2 und 2,0) und 0,70 (nu = 2,0). Gespeicherte
    Ladung, die am Ende noch am Ball sitzt, wird getrennt berichtet.
  - V3 (Born): gemessen durch Born in [0,5; 1,5] bei 0,55 fuer nu = 2,8 und 3,1.
  - **Scheitert, wenn** ein V1-Wert ausserhalb seines Bandes liegt, V2 an einer Stelle reisst oder V3 verfehlt ist.
    Ein C_Q nahe 1 an irgendeiner Stelle hiesse: geometrischer Einfang ist moeglich; das wird als Befund benannt.

- **Gegenprobe (Effekt muss verschwinden):**
  - Paket allein: Ladungsgewinn im Ballfenster < 1e-6 der Paketladung.
  - omega^2 = 0,90 bei nu = 3,1 (ueber seiner Schwelle, fast NLS-Grenzfall): C_Q < 1e-4.

- **Plausibilitaetsschranke:**
  - 0 <= C_Q <= 2 fuer einlaufende Teilchen (hoechstens jedes Quant umgewandelt, je Umwandlung Ladung 2)
  - dE/dQ = omega auf 10 %, wo C_Q >= 1e-3
  - Q und E der Box erhalten auf 1e-4, bis Wellen den Schwamm erreichen; danach Bilanz mit den Randfluessen
  - auslaufende Antiteilchenlinie bei nu - 2 omega auf 0,02

- **Latten erwartet:**
  - L1 ja: Die Baender koennen verfehlt werden, nach oben (bis geometrisch) und nach unten.
  - L2: Paket allein; omega^2 = 0,90.
  - L3: dr/2, dt/2: C_Q-Aenderung hoechstens ein Fuenftel des Effekts.
  - L4 teilweise: Zwei-Moden-Streuung an Q-Baellen mit dieser Schwelle ist bekannt (2+1 D). Der geometrische Einfang
    steht in Arbeiten zur Entstehung als ausdruecklich modellabhaengige Vereinfachung.
  - L5 nein: Die Vergleichsgroesse ist eine Modellannahme, keine Messung.

- **Einfach gesagt:** Rechnungen zur Entstehung von Q-Baellen im fruehen Weltall nehmen oft an, dass ein Ball jedes
  Teilchen verschluckt, das ihn trifft. In unserem Modell ist der Ball fuer seine eigenen Teilchen fast durchsichtig:
  Ein Teilchen bleibt nur haengen, wenn es genug Energie hat, um dafuer ein Antiteilchen auszustossen, und selbst dann
  nur zu wenigen Prozent. Das haben wir bisher nur in einer Dimension gesehen. Jetzt pruefen wir es fuer eine
  Kugelwelle in drei Dimensionen, so wie Teilchen im Raum auf einen Ball treffen.

- Karte geschrieben: 2026-09-30 10:56:30 CEST

- Vorhersage geschrieben: 2026-09-30 11:06:31 CEST
