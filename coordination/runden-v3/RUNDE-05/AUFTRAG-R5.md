# Runde 5: vier 1D-Codeauftraege (R5-A, R5-B, R5-C, R5-D), Anthropic

Auftraggeber: claude-primary. Rundenbeginn 2026-09-30 01:42:38 CEST (gemessen). Deutsch. Explorativ, leicht.

## Gemeinsamer Rahmen

- Lies coordination/runden-v3/README.md, RUNDE-05.md und die Ideen in:
  - RUNDE-02/IDEEN-50-QBALL-BIOLOGIE.md
  - RUNDE-03/IDEEN-20-QBALL-CHEMIE.md
  - RUNDE-03/IDEEN-20-QBALL-WELLEN-WIND-SEGELN.md
- **Modell:** L = |psi_t|^2 - |grad psi|^2 - U(S), U = S - S^2 + S^3/2, S = |psi|^2, 1/2 < omega^2 < 1.
- **Homogener Hintergrund:** omega_bg^2 = 1 - 2 S_bg + 1,5 S_bg^2. Waehle nur Dichten, die linear stabil sind, und
  begruende das. Ausnahme ist, wo die Instabilitaet selbst gemessen wird.
- **Verifizierte Code-Grundlage:** coordination/runden-v3/RUNDE-02/tests1d/tests1d.py. Er ist gelaufen und zeigt:
  - Schiessen gegen Anker 1,5e-10
  - bewegte und platzierte Baelle
  - Radialcode 3D (Test 4) mit Q(omega)-Tabelle
  Die Ergebnisse stehen in RUNDE-02/tests1d/lauf-69/ausgabe/.
- **Ablauf:** Uebernimm, was du brauchst, in deine eigene Datei; aendere Schiessen, Gitter, Zeitschritt und Integrator
  moeglichst nicht. Andere Agenten arbeiten in anderen Ordnern; beruehre nur deinen.
- **Geraet:** CUDA und CPU unterstuetzen (Argument --geraet cuda oder cpu, float64 in beiden Faellen). Dann kann die
  Leitung auf vier Spuren rechnen: p4000a, p4000b, cpu, cpu2.
  - Speicher auf der GPU hoechstens 1,5 GB.
  - Je Aufruf hoechstens 10 min auf einer Quadro P4000 oder einem CPU-Kern.
  - Ein Unterbefehl je Idee, dazu ein Rauchtest.
- **Je Idee vorab festhalten:**
  - Vorhersage
  - Gegenprobe (Kontrolle, bei der der Effekt verschwinden muss)
  - Aufloesungsvergleich (L3: Effekt mindestens fuenfmal groesser als die Aenderung bei halbem dt bzw. dx)
  - Latten L1 bis L5
  Ist eine Idee in 1D nicht sinnvoll pruefbar, sag das mit einem Satz Grund und schlage die kleinste sinnvolle Form vor.
- **Abgabe in deinen Ordner:**
  - Code
  - PLAN.md: Aufrufe ueber `cd <Remote-Ordner> && bash /home/fmh/fmhc-physics-remote/kleintests/kleintest.sh <spur>
    <kurzname> <skript> ...`, Remote-Ordner /home/fmh/fmhc-physics-remote/runde5-<paket>/, Laufzeit je Unterbefehl,
    Vorhersagen, Gegenproben, Latten, "Einfach gesagt"
- **Nicht rechnen:** Die Leitung startet.
- **Grenzen:**
  - Auf dem Laptop kein python, py_compile, awk, keine Shell-Arithmetik; der Code bleibt ungetestet, also einfach halten.
  - Kein ssh, kein git, kein Peerbus, keine Unteragenten, keine Geheimnisse.
  - Gesperrt: KS-1-Ergebnisse, T8-SOLL-*, coordination/vertraege-20260925/, ks-1-dk-lauf/, ks-1-dk-laeufe/.
  - Zeiten mit `date`. Budget hoechstens 90 Minuten.

## R5-A radial 3D (Ordner RUNDE-05/r5a/)

Ideen:
- **Bio 1, Membran:** Spannungstensor des Radialprofils; Wandspannung sigma; Young-Laplace Delta P = 2 sigma/R an drei Q.
- **Bio 4, Tod unter Q_min:** kugelsymmetrische Zeitentwicklung in r (1D-PDE); schwacher Ladungsabfluss am Rand; Zerfall
  schlagartig oder allmaehlich?
- **Bio 17, Mutanten:** radial angeregte Profile mit 1 bzw. 2 Knoten; Existenz, E(Q) gegen den Grundzustand, Lebensdauer in
  der Radialdynamik.
- **Bio 19/34, Fitness und Waehrung:** aus der vorhandenen Q(omega)-Tabelle E/Q, gespeicherte freie Energie je Ladung
  (1 - omega) und Q-Fenster; nur Auswertung.
- **Chemie 11, Keimbildung:** Ball verschiedener Groesse in einem Hintergrund mit festem omega_bg; waechst er oder
  schrumpft er? Kritischer Radius gegen eine Vorhersage aus sigma und Druckdifferenz.
- **Chemie 18, magische Zahlen:** Ist E/Q(Q) glatt, oder gibt es Knicke oder Stufen?

## R5-B 1D Einzelball (Ordner RUNDE-05/r5b/)

Ideen:
- **Bio 3, Fuettern:** Wellenpakete verschiedener Frequenz und Amplitude auf einen Ball; eingefangener Anteil, Ladungs- und
  Energiebilanz, Aenderung von omega.
- **Bio 36, Photosynthese:** Dauerwelle statt Paket; Wachstumsrate gegen Frequenz.
- **Bio 38, Winterschlaf:** Antwort auf einen festen Stoss gegen omega^2 (0,55 bis 0,9).
- **Bio 20/37, Rauschen:** Rauschbad verschiedener Staerke; Ueberleben und Schmelzschwelle gegen Q.
- **Bio 45, angetriebener Ball:** Pumpe plus Daempfung; Gibt es eine stabile dissipative Struktur, die ohne Pumpe
  zerfaellt?
- **Bio 22 und Chemie 10, Modulationsinstabilitaet:** Hintergrund mit Rauschen bei 3 bis 4 Dichten; dominante
  Wellenlaenge gegen die lineare Vorhersage; Einsatz der Verklumpung ("Uebersaettigung").

## R5-C 1D mehrere Baelle und Hintergrund (Ordner RUNDE-05/r5c/)

Ideen:
- **Bio 2, Osmose:** Ball im Hintergrund mit omega_bg ueber bzw. unter seinem omega; dQ/dt.
- **Bio 12, Ladungspendeln:** nahes Paar; periodischer Ladungsaustausch? Periode gegen Abstand.
- **Bio 16, Symbiose:** gebundenes Paar gegen zwei Einzelbaelle; Energiebilanz.
- **Bio 39, Quorum:** viele Baelle (8 bis 16) in einer periodischen Box bei drei Dichten; gemeinsames Atmen?
- **Bio 50, Lawinen:** lange Kette, zufaellige kleine Stoesse; Groessenverteilung der Atem-Ereignisse.
- **Chemie 4, IR-Schwingung:** gebundenes Paar leicht auslenken; Abstandsschwingung per FFT.
- **Chemie 9, Massenwirkung:** Box mit Ball und Hintergrund bei drei Startmischungen; Endverteilung, omega gleich omega_bg?
- **Wellen 6, Gleiten:** Bremskraft bei hoher Geschwindigkeit; nicht monoton?
- **Wellen 7, Windschatten:** zwei Baelle hintereinander durch den Hintergrund; Bremskraft des hinteren.
- **Wellen 11, Fahrtwind:** Ball bewegt im ruhenden Hintergrund gegen ruhender Ball im bewegten Hintergrund; gleiche
  Bremskraft?

## R5-D 1D zwei Felder (Ordner RUNDE-05/r5d/)

Ein zweites komplexes Feld chi mit einer einfachen, begruendeten Kopplung, etwa lambda |psi|^2 |chi|^2 mit eigenem
Potential bzw. masselos, wo verlangt. Ideen:
- **Bio 8, Zellkern:** zwei Kanaele mit verschiedenen Massen; Kern-Huelle-Profil?
- **Bio 15, Raeuber-Beute:** zwei Arten mit Ladungsaustausch in einer Box; Oszillieren die Bestaende?
- **Bio 35, Mitochondrium:** kleiner chi-Ball in einem grossen psi-Ball; stabil?
- **Bio 48, Altern:** schwache Kopplung an einen masselosen Kanal; Q(t), Verdampfungsrate gegen Groesse.
- **Chemie 17, Tensid:** chi sitzt an der psi-Wand und senkt die Wandenergie; Q_min oder Wandspannung mit und ohne chi.
- **Wellen 10, Kreuzen:** zwei Hintergruende mit Gegenstroemung; Nettobewegung eines Balls, der an beide koppelt.
