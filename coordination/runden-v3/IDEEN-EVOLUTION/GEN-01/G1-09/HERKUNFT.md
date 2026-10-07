# G1-09 Herkunft

- Operator: analogie. Eltern: Wel 16 (Tropfenschwingung nach Rayleigh). Arm E, Generation 1.
- Bearbeiter: Operator-Agent "aussen" (Anthropic, Opus 5.5). Beginn (date, Gesamtauftrag): 2026-09-30 07:18:19 CEST.

## Erwartung vor dem ersten Suchabruf (geschrieben 2026-09-30 07:27:34 CEST, date)

Die Rayleigh-Plateau-Instabilitaet eines Fluessigkeitsstrahls (schnellstes Wachstum bei k R = 0,697, Grenze k R = 1)
ist Standard. Fuer Q-Baelle erwarte ich keine Arbeit, die einen zylindrischen "Q-Schlauch" mit Rayleigh-Plateau
quantitativ vergleicht; fuer Quantentroepfchen (Bose-Mischungen) und kubisch-quintische NLS ("fluessiges Licht") gibt es
vermutlich Arbeiten zum Zerfall von Faeden in Troepfchen.

Nachtrag nach der Suche: Die Erwartung zu Q-Baellen war falsch, siehe Kandidat 1.

## Elternbefund (an den Projektdateien gelesen)

- [A] RUNDE-03/ERGEBNISSE-R3.md, "Tropfen, Wellen 16": 2D-Rayleigh Omega_l^2 = (l^3 - l) sigma/(rho R^3) mit
  rho = w = 2 omega^2 S_c; Omega/P1 = 0,9416 / 0,9312 (l = 2 / 3, omega^2 = 0,52), 0,8822 / 0,8688 (0,55).
- [A] RUNDE-06/ERGEBNISSE-R6-B.md, V9: 3D l = 2 bei 0,52 bis 0,55 im Band, Verhaeltnis zu Rayleigh 0,968 bis 0,931;
  V8: 0,0741 bei 0,6 gebunden (Rayleigh-Band 0,0730 bis 0,0909).
- [A] RUNDE-05.md (R5-A radial 3D): Young-Laplace auf 1 bis 4 %; Code RUNDE-05/r5a/r5a.py mit sigma = Int 2 f'^2 dr,
  Innendruck und Zeitentwicklung.

## Kandidaten (je eine Zeile, verschiedene Felder)

1. **Stroemung, Rayleigh-Plateau-Zerfall eines Strahls:** Q-Schlauch zerfaellt bei k R < 1, schnellste Mode k R = 0,697.
   Verworfen als bekannt: [L] Qian Chen, "Hydrodynamic and Rayleigh-Plateau instabilities of Q-strings", Phys. Rev.
   Lett. 134, 211603 (2025), arXiv 2412.09815 (Abstract gelesen): zylindrische Q-Strings sind fuer lambda > lambda_c
   instabil, im Duennwandgrenzfall mit lambda_c = 2 pi R; "Q-strings resemble low-viscosity fluids with surface
   tension". Fuer Quantentroepfchen ebenfalls Literatur: [L] Ancilotto, Modugno, Fort, arXiv 2507.11223 (15.07.2025,
   Abstract gelesen): Querfalle unterdrueckt die Kapillarinstabilitaet eines Quantenfluessigkeitsfadens; laut Text
   "Recent experiments have demonstrated Rayleigh-Plateau instability in elongated droplets confined in an optical
   waveguide" (Experiment dort nicht benannt).
2. **Blasen, Kavitation: leere Blase in einem Tropfen** (Rayleigh-Kollaps, im endlichen Tropfen verkuerzt). Gewaehlt.
3. **Akustik, Faraday-Anregung eines Tropfens:** parametrischer Antrieb bei 2 Omega_2 laesst die l = 2-Mode in einer
   Mathieu-Zunge wachsen; Breite ~ Modulationstiefe. Moeglich, aber die Modulationstiefe braucht eine eigene Herleitung
   (dsigma/dm^2), und die gleichzeitig angetriebene Atmung stoert.
4. **Clusterphysik, Heliumtroepfchen:** Oberflaechenmoden oberhalb der Verdampfungsschwelle sind ungebunden
   (Selbstverdampfung). Verworfen: Das waere bei Q-Baellen die Frage, wann l = 2 ueber 1 - omega liegt; das beruehrt die
   laufende Karte zu l = 1 und l = 2.
5. **Physikalische Chemie, Tolman-Laenge:** Kruemmungskorrektur der Wandspannung sigma(R) = sigma_inf/(1 + 2 delta/R)
   koennte die Rayleigh-Reste von 3 bis 12 % erklaeren. Zurueckgestellt: Die Groessen im Tropfentest sind schon am
   endlichen Ball definiert, ein sauberer Vorab-Test braucht erst eine eindeutige Definition der Trennflaeche.
6. **Kernphysik und Astrophysik, rotierende Tropfen (Bohr-Wheeler, Maclaurin/Jacobi):** starre Rotation passt nicht zu
   einem Suprafluid mit quantisierter Windung; drehende Q-Baelle und Ringe laufen schon in anderen Karten.

## Gewaehlte Analogie und L4-Pruefung

- Mechanismus: Eine leere Kavitationsblase kollabiert nach Rayleigh traegheitsgetrieben; in einem Tropfen muss weniger
  Fluessigkeit mitbewegt werden, dazu gibt die schrumpfende Aussenflaeche Energie frei, also ist die Kollapszeit kuerzer.
  Uebertragen: Leere (S = 0) im duennwandigen Q-Ball, sigma und rho aus dem Profil, Energiebilanz der Kugelschale.
- Messbare Groesse, die anders ausfallen kann: t_70 gegen die Energiebilanz (Zahl) und die Verkuerzung mit R0/R_d
  (Vorzeichen und Groesse). Andere Ausgaenge: kein Rayleigh-Kollaps (anderer Fuellmechanismus), Rayleigh ohne
  Endlichkeitskorrektur, Stillstand der Leere.
- [L] Obreschkow, Kobel, Dorsaz, de Bosset, Nicollier, Farhat, "Cavitation bubble dynamics inside liquid drops in
  microgravity", Phys. Rev. Lett. 97, 094502 (2006), arXiv physics/0610166 (Abstract gelesen): "Bubble lifetimes in
  drops are shorter than in extended volumes in remarkable agreement with herein derived corrective terms for the
  Rayleigh-Plesset equation." [L?] Kollapsfaktor 0,915 im unbegrenzten Volumen und seine Abnahme mit Blase/Tropfen nur
  laut Suchtreffer; die Formel der Karte ist eigene Papierrechnung [S] (kinetische Energie der Schale
  2 pi rho R^3 Rdot^2 (1 - R/R_d), Wandenergie innen und aussen).
- [L] Canillas Martinez, Dorey, Romanczukiewicz, Saffin, Slawinska, Wereszczynski, "Oscillons and bubbles in Q-ball
  dynamics", arXiv 2509.03192 (3.09.2025; Abstract gelesen; JHEP-Angabe nur laut Suchtreffer [L?]): In Q-Anti-Q-Stoessen
  sind "Blasen des falschen gebrochenen Vakuums" (ladungsfreie Q-Materie) Zwischenzustaende; Goldstone-Moden koennen sie
  zeitweise am Kollaps hindern. Das ist das umgekehrte Objekt (Materie ohne Ladung statt Leere in Materie), zeigt aber,
  dass Phasenmoden einen Kollaps aufhalten koennen: daher der Ausgang "Stillstand" in der Karte.
- [L] Paredes, Feijoo, Michinel, "Coherent cavitation in the liquid of light", Phys. Rev. Lett. 112, 173901 (2014),
  arXiv 1605.02515 (nur Suchtreffer-Zusammenfassung, [L?]): Hohlraeume (Verduennungspulse, Wirbelpaare) in
  Flachkopf-Solitonen der kubisch-quintischen NLS; verwandt, aber keine Rayleigh-Kollapszeit.
- Nicht gefunden (zwei Suchen): Kollaps einer Leere in Q-Materie mit Rayleigh-Plesset-Vergleich.

## Papierwerte der Karte [S]

- omega^2 = 0,52: S_c = (2 + sqrt(6 omega^2 - 2))/3 = 1,0194; U(S_c) = 0,5099; p = omega^2 S_c - U = 0,0202;
  rho = 2 omega^2 S_c = 1,060; sigma ~ sqrt(2)/4 = 0,354 (ebene Wand bei omega_min); R_d ~ 2 sigma/p ~ 35;
  c_Q^2 = S/(S + omega dS/domega) = 0,509, c_Q = 0,71.
- Unbegrenzt: Int_0^1 x^(3/2) (1 - x^2)^(-1/2) dx = B(5/4, 1/2)/2 = 0,874, also t_Kollaps = 0,618 sqrt(rho R0^3/sigma);
  bis 0,7 R0 vergehen 77,7 % davon (Reihe bis x^10,5).
- Die Endlichkeitsfaktoren 0,80 / 0,71 / 0,58 sind grobe Schaetzungen (Schalenfaktor sqrt(1 - R0/R_d) mal
  Energiezuschlag der Aussenwand bei R = 0,85 R0); bindend ist die Quadratur T_E des Test-Agenten.

## Quellenliste (URLs)

- https://arxiv.org/abs/2412.09815
- https://arxiv.org/abs/2507.11223
- https://arxiv.org/abs/physics/0610166
- https://arxiv.org/abs/2509.03192
- https://arxiv.org/abs/1605.02515 (nur Suchtreffer)

## Zeiten

- Karte geschrieben 2026-09-30 07:41:43 CEST; Schreibbeginn der Herkunftsdateien 2026-09-30 07:42:58 CEST (date).
- Ende (date): 2026-09-30 07:45:15 CEST. Beginn 07:18:19, also 27 min fuer alle drei Karten.
