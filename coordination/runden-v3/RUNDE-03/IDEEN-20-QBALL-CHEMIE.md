# 20 Q-Ball-Ideen aus der Chemie (Eingang fuer Runde 3)

Leitung claude-primary, Zeit vor dem Schreiben gemessen: 2026-09-30 01:12:59 CEST.

Finn woertlich: "gib mir 20 weitere q-ball ideen, diesmal aus der chemie".

## Grundlage

- **Status:** Alles sind Hypothesen, nichts ist gerechnet.
- **Modell:** unser Q-Ball, U = S - S^2 + S^3/2.
- **Uebersetzung aus der Chemie:**
  - Ladung Q entspricht der Teilchenzahl.
  - omega = dE/dQ ist das chemische Potential. Kleine Q-Baelle haben ein hohes omega, grosse ein niedriges.
  - Die duenne Wand verhaelt sich wie ein Fluessigkeitstropfen.
- **Zwei Q-Baelle im Abstand d:** Lehrbuchform fuer Solitonen [aus dem Gedaechtnis]:
  - Wechselwirkung etwa -cos(Delta phi) * exp(-kappa d) mit kappa = sqrt(1 - omega^2)
  - gleichphasig ziehen sie sich an, gegenphasig stossen sie sich ab
- Je Idee: Analogie, Hypothese (H), kleinster Test (T), [L4] vermutlich bekannt.

## Ideen

1. **Elektronegativitaet = omega.**
   - H: Beruehren sich zwei Q-Baelle, fliesst Ladung vom hoeheren omega (klein) zum niedrigeren (gross), wie Elektronen
     zum elektronegativeren Atom. Es entsteht eine "Partialladung".
   - T: 1D, zwei nahe Baelle mit omega^2 = 0,8 und 0,6; Richtung und Menge des Ladungsflusses.
2. **Kovalente Bindung und Antibindung.**
   - H: Gleichphasige Ueberlappung senkt die Energie (bindend), gegenphasige hebt sie (antibindend), wie bindende und
     antibindende Orbitale.
   - T: E(d, Delta phi) fuer ein Paar bei fester Ladung.
   - [L4 asymptotisch bekannt]
3. **Bindungskurve = Morse-Potential.**
   - H: E(d) des gleichphasigen Paars laesst sich mit einem Morse- oder Kratzer-Potential beschreiben.
   - T: E(d) messen und mit unserem Rechenkern coordination/evolution/evolution_potential.py anpassen; Anharmonizitaet
     angeben.
   - Das ist eine Bruecke zu unserer HCl/Morse-Arbeit vom 12.09.
4. **Molekuelschwingung (IR-Spektrum).**
   - H: Ein gebundenes Paar schwingt im Abstand mit einer Frequenz aus der Kruemmung von E(d).
   - T: 1D-Paar leicht auslenken; FFT des Abstands gegen die Vorhersage aus Nr. 3.
5. **Isomere.**
   - H: Drei Q-Baelle als Kette oder Dreieck haben bei gleicher Gesamtladung verschiedene Energien und Lebensdauern.
   - T: 2D, beide Anordnungen, Energie und Zusammenhalt.
6. **Puffer (pH-Puffer).**
   - H: Ein grosser Q-Ball haelt das chemische Potential des umgebenden Mediums fast konstant. Gibt man Ladung ins Medium,
     schluckt er sie.
   - T: 3D-Box mit grossem Ball und Hintergrund; Ladungspulse hinzufuegen; Hintergrund-omega mit und ohne Ball.
7. **Aktivierungsenergie.**
   - H: Gegenphasige Baelle verschmelzen erst ab einer Mindestgeschwindigkeit (Barriere), gleichphasige immer. Die Barriere
     haengt von Delta phi ab.
   - T: 1D-Stoesse; Phasendiagramm verschmelzen/abprallen in (v, Delta phi).
   - [L4 teilweise: Battye und Sutcliffe 2000]
8. **Katalyse.**
   - H: Ein dritter Ball in der Naehe senkt die Verschmelzungsbarriere zweier anderer.
   - T: 1D-Dreierstoss; Barriere mit und ohne Katalysator-Ball.
9. **Massenwirkungsgesetz.**
   - H: Freie Quanten im Medium und im Q-Ball gebundene Ladung stellen ein Gleichgewicht ein. Im Gleichgewicht ist das
     omega des Balls gleich dem chemischen Potential des Mediums.
   - T: 3D-Box; Endverteilung der Ladung bei drei Startmischungen.
10. **Uebersaettigung und Ausfaellung.**
    - H: Ein Hintergrundkondensat oberhalb einer Dichte ist "uebersaettigt" und faellt Q-Baelle aus.
    - T: Einsatzdichte der Verklumpung gegen die lineare Instabilitaetsgrenze. Codex' Verdichtung ist genau so eine
      Ausfaellung.
11. **Keimbildung.**
    - H: Wie in der klassischen Nukleationstheorie gibt es einen kritischen Keim: Kleinere Q-Baelle loesen sich im Medium
      auf, groessere wachsen. Der kritische Radius folgt aus Wandspannung gegen Potentialgewinn.
    - T: 3D, Baelle verschiedener Groesse in ein Medium setzen; Wachsen oder Schrumpfen gegen den vorhergesagten Radius.
12. **Phasendiagramm.**
    - H: Je nach mittlerer Dichte und Rauschenergie ("Temperatur") endet eine Box als Gas aus Wellen, als Tropfen
      (Q-Materie) oder als Kondensat. Gibt es einen Tripelpunkt?
    - T: 3D-Box-Raster aus 3 x 3 Laeufen; Endzustand klassifizieren.
13. **Kristall mit wechselnder Phase (Kochsalz-Analogie).**
    - H: Ein Gitter mit abwechselnder Phase (0, pi, 0, pi) ist stabil; gleichphasige Nachbarn verschmelzen.
    - T: 2D-Gitter mit beiden Phasenmustern; Zusammenhalt ueber die Zeit.
14. **Ionenkristall aus Q-Ball und Anti-Q-Ball.**
    - H: Entgegengesetzt geladene Baelle vernichten sich teilweise, aber auf Abstand koennten sie ein geordnetes Gitter bilden.
    - T: Q/Anti-Q-Paar; Vernichtungszeit gegen Abstand.
15. **Redox ueber eine Bruecke.**
    - H: Ladung wandert von einem Spender-Ball (hohes omega) ueber Bruecken-Baelle zum Empfaenger (niedriges omega). Die Rate
      faellt exponentiell mit der Brueckenlaenge, wie beim Elektronentransfer (Marcus, Superaustausch).
    - T: 1D-Kette D-B-...-B-A mit 0 bis 3 Bruecken; Transferrate.
16. **Kettenreaktion und Flammenfront.**
    - H: Eine Verschmelzung setzt Energie frei, die Nachbarn zum Verschmelzen anstoesst. Es entsteht eine Front mit fester
      Geschwindigkeit.
    - T: 1D-Reihe metastabiler Paare knapp unter der Schwelle; ersten zuenden, Frontgeschwindigkeit.
17. **Tensid (Seife).**
    - H: Ein zweites Feld, das an der Wand sitzt, senkt die Wandspannung. Dann gibt es kleinere Q-Baelle, und die
      Ostwald-Reifung wird gebremst, wie bei Emulsionen und in Zellen.
    - T: Zwei-Feld-Modell mit Wandkopplung; Q_min und Reifungsrate mit und ohne Tensid.
18. **Periodensystem und magische Zahlen.**
    - H: Die Familien (kugelig, drehend m = 1, 2 und radial angeregt) sind "Elemente". Bei bestimmten Q gibt es besonders
      stabile, "magische" Baelle wie Edelgase oder magische Kerne.
    - T: E/Q(Q) je Familie; Suche nach nicht-monotonen Stellen. Wahrscheinlich glatt, das ist die L1-Probe.
19. **Aromatizitaet.**
    - H: Ein Ring aus N Q-Baellen mit einer Phasenwindung 2 pi k traegt einen Kreisstrom. Bestimmte Kombinationen aus N und
      k sind besonders stabil, wie die Hueckel-Regel 4n+2.
    - T: 2D-Ringe mit N = 4 bis 8 und k = 0 und 1; Energie je Ball.
20. **Chromatographie.**
    - H: Q-Baelle verschiedener Groesse durchqueren ein raues Medium unterschiedlich schnell; das trennt sie nach omega.
    - T: 1D, Baelle mit verschiedenem omega durch eine Zone mit kleinem Zufallspotential; Durchlaufzeit gegen omega.

## Vorschlag der Leitung fuer Runde 3

Alles in 1D, billig, jeweils mit einer Vorhersage, die scheitern kann.

| Nr | Warum |
|---|---|
| 1 Elektronegativitaet | klare Richtungsvorhersage (hohes omega -> niedriges omega); verbindet Ostwald-Reifung und Chemie |
| 2/3 Bindungskurve und Morse | misst das Paarpotential unseres Modells; Anschluss an den Morse/Kratzer-Kern von 12.09. |
| 7 Aktivierungsenergie | Phasendiagramm verschmelzen/abprallen; zugleich Test von Antwort B zum Fuettern |
| 15 Redox ueber Bruecke | Exponentialgesetz, das scheitern kann |

Dazu eine Zufallskarte aus den uebrigen 15. Der 1D-Code aus Runde 2 laesst sich dafuer weiterverwenden.

## Einfach gesagt

Q-Baelle verhalten sich in vielem wie Atome und Molekuele. Gleichphasige ziehen sich an wie eine chemische Bindung,
gegenphasige stossen sich ab. Ladung fliesst vom kleinen zum grossen Ball wie Elektronen zum "gierigeren" Atom, und ein
Keim muss eine Mindestgroesse haben, um zu wachsen. Wir haben 20 solche Vergleiche aufgeschrieben. Vier davon testen wir als
Naechstes mit dem kleinen 1D-Programm, jeweils mit einer Vorhersage, die auch falsch sein kann.
