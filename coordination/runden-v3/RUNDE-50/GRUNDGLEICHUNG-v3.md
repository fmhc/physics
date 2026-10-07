# Grundgleichung Fassung 3: Eine 4D-Wirkung auf Finns gefuelltem Netz (Runde 50, Leitung)

- Leitung claude-primary, geschrieben ab 2026-10-05 16:40:25 CEST (date). Arbeitsfassung; ersetzt die Architektur von
  v2.5 (RUNDE-49/GRUNDGLEICHUNG-SKIZZE-v2.5.md) dort, wo die Rechnungen vom 05.10. nachmittags sie ueberholt haben.
- Kennzeichen: [E] im Projekt gerechnet (Karte genannt), [N] Nachtrag nach Sicht, nicht geurteilt, [M] vorab ableitbar,
  [H] Hypothese, [W] gewaehlt (Architektur), [L] Literatur aus dem Gedaechtnis. Alles synthetisch, linear um flach, keine
  Messdaten.
- Anlass: Finn, "o wie kommen wir weiter" (05.10.): eine Gleichung statt vieler Teile, gemessen an den bekannten Tests
  (RUNDE-49/GR-PRUEFLISTE-v2.md mit Nachtrag).

## 1. Was neu ist gegenueber v2.5

- Kern ist nicht mehr ein 3D-Hamiltonian mit gesetzter Traegheit (Form A, B), sondern **eine 4D-Wirkung auf dem
  Zeltnetz**. Traegheit, Lapse und Shift folgen daraus (UEBERLEITUNG-KH-1, UEBERLEITUNG-V-1/-2) [E, N].
- Die gesetzte gemeinsame Zeiteinheit (N0 = Wurzel 8 fuer alle Sektoren, v2.5 Abschn. 3.1) entfaellt: Alle Sektoren
  benutzen dieselben Zeltstangen. Licht und Schwerewellen sind damit bei langen Wellen gleich schnell (LICHT-GLEICHE-UHR)
  [E; folgt aus dem Aufbau].
- Das Netz muss gefuellt sein: V und S tragen die stetige Zeit, das ungefuellte B1 nicht (UEBERLEITUNG-V-2) [E].

## 2. Zustand und Wirkung [W]

- **Raum:** periodisches, gefuelltes Tetraedernetz (Finns V; S als Gegenprobe), gewichtete Hodge-Sterne mit Hebehoehe in
  der Kammer (HOEHE-ISOTROP-1, REGULAER-V-1). Ungewichtet ist V nicht Delaunay.
- **Zeit:** Zeltstangen auf jeder Ecke; ein Takt klebt 4-Simplizes auf die Schicht. Raumzeit = V mal Zeit als 4D-Netz
  (146 Kanten je Zelle).
- **Wirkung:** S = S_Regge(4D) + S_Maxwell(4D) + S_Skalar(4D) auf demselben 4D-Netz.
  - S_Regge: Summe ueber Dreiecke von Flaeche mal Fehlwinkel, euklidisch gerechnet und formal in echte Zeit fortgesetzt.
  - S_Maxwell: Feld A auf den 4D-Kanten, F = dA auf den 4D-Dreiecken, Whitney- bzw. DEC-Sterne aus derselben
    4D-Geometrie. Gelesen als Fluss-Eis: Fluss durch die Dreiecke, Eisregel (Gauss) je Tetraeder.
  - S_Skalar: komplexes Feld auf den Ecken (Q-Ball-Sektor, Papier I), Bewegung ueber die zeitartigen und schraegen
    4D-Kanten.

## 3. Stetige Grenze: die Gleichung, mit der gerechnet wird [E, N]

- Fuer Zeltstangen h -> 0 entsteht eine ADM-artige Hamiltonform (UEBERLEITUNG-V-1, Nachtrag; UEBERLEITUNG-V-2):
  - H = Summe_v N_v H_v + Shift-Terme + H_Licht + H_Skalar.
  - Potential = 3D-Regge-Form B (auf 4e-7).
  - Lapse N_v = reiner Multiplikator mit der Eckenregel R1 (Kopplung C = -c/2).
  - Traegheit M_eff aus der 4D-Wirkung: auf V und S ohne statische Richtung, mit genau einer negativen Richtung je Ecke
    (V 10, S 6 je Zelle). Lesart [H]: die konforme Richtung der ART (DeWitt); 88 % (V) bzw. 95 % (S) davon liegen in
    den Eckdehnungen.
- Ergebnisse dieser Form auf V:
  - Schwerewellen richtungsgleich (auf h -> 0 extrapoliert 5,1e-10; bei h = 2^-10 ein h^2-Rest von 1e-6) und ohne wachsende Mode an 1562 k (UEBERLEITUNG-V-2) bzw. 591 k (Nachtrag V-1).
  - Licht mit derselben Uhr gleich schnell: DEC 1 +- 1,5e-10, Maxwell auf dem 4D-Netz 1 +- 1,5e-7.
  - Bei kurzen Wellen: Schwerewellen -0,018 (kl)^2, Licht -0,016 bis -0,018 (kl)^2, Unterschied etwa 0,002 (kl)^2,
    Doppelbrechung Licht bis 8e-4 (kl)^2, Schwerewellen bis 5,7e-3 (kl)^2.

## 4. Der Takt [E, ES]

- Ein Takt mit Zeltstangen von Kantengroesse ist auf V heftig instabil (REGIME-K-3: alle 52 bis 56 Gittermoden, Faktor
  bis e^pi je Takt).
- Mit kuerzeren Stangen wird er ruhig: ab h = 1/64 fuer kl >= 0,1 (h-Gang); fuer alle Wellenlaengen unter h* ~ 0,004
  der Bezugshoehe (UEBERLEITUNG-V-2, Nachtrag).
- Ein endlicher Takt hinterlaesst eine langwellige Richtungsabhaengigkeit der Wellengeschwindigkeit von etwa
  1,3 (h/h0)^2. Fuehrt man den Takt als echte Physik und trifft er das Licht nicht genauso, verlangt GW170817 grob
  h/h0 < 3e-8 [ES]. Die Zeit laeuft dann praktisch stetig.
- Die Reihenfolge der Zeltzuege zaehlt auf gekruemmten Daten (Spur nur in 3-3-Zuegen), auch fuer die 4-Volumen-Uhr
  (ZELT-KOMMUTATOR-2). Ein Takt braucht daher eine feste Reihenfolge oder kleine Schritte [H].

## 5. Licht und Materie [E, M]

- **Licht:** Maxwell auf V bzw. dem 4D-Netz, mit gewichteten Sternen. Fluss-Eis nur auf dem Diamant-Teil kann
  Eg-Verzerrungen nicht folgen (LICHT-SEKTOR-NOTIZ, L2) [M]; Bentons M-D bleibt Modell fuer flaches Licht ohne
  Doppelbrechung. Die Wellen kommen aus der Dynamik, nicht aus der Eisregel allein.
- **Materie:** Q-Ball-Skalar. Bei der Uebergabe beim Umklappen reicht P (Impulse stetig, kanonisch). R, P und K
  unterscheiden sich praktisch nicht (KANON-TRANSFER-1).

## 6. Offen (Reihenfolge)

1. Newton-Grenzfall und Lichtablenkung mit derselben Uhr auf V (laeuft, ohne Karte).
2. Umklappen als 4D-Schritt: Der Energiesprung beim Umklappen sitzt in der Geometrie (5e5- bis 2e6-mal der Skalar),
   unter Form A2 ohne Abnahme mit dem Ueberschuss. Im 4D-Bild ist der Umbau selbst ein angeklebter 4-Simplex [H].
3. Gleiche schwere und traege Masse mit Bindungsenergie; Shapiro; nichtlinear (Perihel).
4. Spin 1/2: Das Vorzeichen eines 360-Grad-Kerns ist auf dem Netz endlich geschuetzt; die Schwelle waechst bei festem Kern
   mit dem Netz (Z2-SCHUTZ-2); ein Fermion braucht zusaetzlich einen Phasenterm (Kandidat Levin/Wen-Twist, TWIST-PYRO-1).
   Grosse Netze laufen auf der GPU (ohne Karte).
5. Quantisierung, kleines Lambda, warum B1 scheitert.

## 7. Gesetzt [W] und zu pruefen

- Gesetzt: gefuelltes periodisches Netz V, Hebehoehe in der Kammermitte, Eckenregel R1, metrische Kopplung von Licht und
  Q-Ball, feste Topologie bis zum Umklappen-Schritt.
- Zu pruefen: alle Saetze in Abschnitt 3 bis 5 nur linear um flach; der Nachtrag-Teil von UEBERLEITUNG-V-1 ist durch
  UEBERLEITUNG-V-2 bestaetigt fuer V und S (Stabilitaet, Zahl der negativen Richtungen), nicht fuer B1.

## Einfach gesagt

Die Gleichung fuer Finns Netz ist jetzt eine einzige Regel fuer Raum und Zeit zusammen: Kanten haben Laengen, die Zeit
kommt als vierte Richtung dazu, und Licht und Materie wohnen im selben Netz. Wenn die Zeit in sehr kleinen Schritten
laeuft, kommen daraus Schwerewellen, die in alle Richtungen gleich schnell und stabil laufen, und Licht ist genauso schnell
wie die Schwerkraft. Grosse Zeitschritte machen das Netz instabil; deshalb laeuft die Zeit praktisch stetig. Offen sind vor
allem das Umklappen des Netzes, die Ablenkung von Licht an einer Masse und der halbe Spin.

## Nachtrag 17:25:45 (date)

- Schwere Masse (SCHWERE-MASSE-V, ohne Karte): Mit der heutigen Projektkopplung (Quelle = Energie) ist M_schwer = E durch den Aufbau. Fuer Tolman-Konsistenz (rho + 3p wie in der ART) muss der Q-Ball metrisch an die Kantenlaengen koppeln; dann bleibt auf dem Gitter ein Virialrest S/E von etwa 0,1 (a/R)^2 (fuer reale Teilchen < 1e-24). Abschnitt 5 und 7: metrische Kopplung mit Spannungsterm wird Pflicht.
- Umklappen (UMKLAPP-4D-1, ohne Karte, 17:48:41): Mit M_eff aus der 4D-Wirkung ist der Energiesprung beim 2-3-Zug 60- bis 1e7-mal kleiner als unter Form A2 und faellt wie der Ueberschuss mu; der A2-Sprung war ein Artefakt der gesetzten Traegheit. Uebergabe: P mit p_neu = 0 fuer die neue Kante. Linear, statische Einzelzuege.
