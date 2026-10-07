# Runde 4: zwei 1D-Codeauftraege (R4-W Wellen, R4-CB Chemie/Biologie), Anthropic

Auftraggeber: claude-primary. Rundenbeginn 2026-09-30 01:24:44 CEST (gemessen). Deutsch. Explorativ, leicht.

## Gemeinsamer Rahmen fuer beide Agenten

- Lies coordination/runden-v3/README.md und RUNDE-04.md. Die Ideen stehen in:
  - RUNDE-02/IDEEN-50-QBALL-BIOLOGIE.md
  - RUNDE-03/IDEEN-20-QBALL-CHEMIE.md
  - RUNDE-03/IDEEN-20-QBALL-WELLEN-WIND-SEGELN.md
- **Modell:** L = |psi_t|^2 - |grad psi|^2 - U(S), U = S - S^2 + S^3/2, S = |psi|^2, 1/2 < omega^2 < 1.
- **Verifizierter Ausgangscode:** coordination/runden-v3/RUNDE-01/qg1/qg1.py. Uebernimm Schiessen, Anker, Gitter,
  Zeitschritt und Integrator; aendere so wenig wie moeglich.
- Andere Agenten schreiben parallel in RUNDE-02/tests1d/, RUNDE-03/tests1d-r3/ und RUNDE-03/tests2d-r3/. Beruehre diese
  Ordner nicht.
- **Je Test** hoechstens 10 min auf der P5000; zusammen moeglichst unter 15 min. Vorab festhalten:
  - Vorhersage
  - Gegenprobe (Kontrolle, bei der der Effekt verschwinden muss)
  - Aufloesungsvergleich (L3: Effekt mindestens fuenfmal groesser als die Aenderung bei halbem dt bzw. dx)
- **Hintergrundkondensat, wo noetig:** eine stabile Dichte waehlen und mit der linearen Stabilitaet begruenden.
  - Ausnahme: Wellen 2 will genau den instabilen Fall.
- **Abgabe je Agent in seinen Ordner:**
  - Code (CUDA, float64, Unterbefehle je Test, dazu ein Rauchtest-Aufruf)
  - PLAN.md: Aufruf mit Lock wie RUNDE-01/QG1-PLAN.md, Laufzeitschaetzung je Test, Vorhersagen, Gegenproben, Latten L1 bis
    L5, "Einfach gesagt"
- **Nicht rechnen:** Die Leitung startet in VS-1-Portionsluecken.
- **Grenzen:**
  - Auf dem Laptop kein python, py_compile, awk, keine Shell-Arithmetik; der Code bleibt ungetestet, also einfach halten.
  - Kein ssh, kein git, kein Peerbus, keine Unteragenten, keine Geheimnisse.
  - Gesperrte Ordner: KS-1-Ergebnisse, T8-SOLL-*, coordination/vertraege-20260925/, ks-1-dk-lauf/, ks-1-dk-laeufe/.
  - Zeiten mit `date`. Budget hoechstens 90 Minuten.

## Agent R4-W (Ordner RUNDE-04/wellen/)

Karten: Wellen 1, 2, 3, 12, 13.

1. **Russell:** Stoss zweier gleicher Baelle (omega^2 = 0,7) bei v = 0,1, 0,3, 0,5; abgestrahlter Energieanteil.
   Gegenprobe: ein einzelner Ball, der nicht abstrahlt.
2. **Monsterwelle:** instabiler Hintergrund mit Rauschen 1e-3; Spitzenstatistik gegen die Gauss-Rayleigh-Erwartung mit
   gleichem Mittel und gleicher Varianz. Gegenprobe: stabiler Hintergrund.
3. **Stokes-Drift:** laufende Hintergrundwelle mit zwei Amplituden; Netto-Drift des Balls je Periode. Vorhersage: Drift
   ~ a^2. Gegenprobe: stehende Welle, dann keine Netto-Drift.
4. **Surfen:** grosse laufende Welle (oder Front) plus Ball; Energie- und Geschwindigkeitsgewinn. Gegenprobe: Ball ohne
   Welle.
5. **Brandung:** Dichterampe im Hintergrund; Ball laeuft hinein bei 3 Geschwindigkeiten; Verformung (Breite, Spitzenwert),
   Zerfall ja oder nein.

## Agent R4-CB (Ordner RUNDE-04/chemie-bio/)

Karten: Chemie 8, 16, 20; Bio 13, 27, 41; Zufallskarte Bio 18.

1. **Katalyse:** Stoss zweier gegenphasiger Baelle knapp unter ihrer Verschmelzungsschwelle, mit und ohne dritten Ball in
   der Naehe. Senkt der dritte Ball die Schwelle?
2. **Kettenreaktion:** Reihe aus 4 bis 6 knapp unterkritischen Paaren; das erste Paar zuenden; Frontgeschwindigkeit, oder
   die Front erlischt.
3. **Chromatographie:** Baelle mit omega^2 = 0,6, 0,7, 0,8 bei gleicher Anfangsgeschwindigkeit durch eine Zone mit kleinem
   Zufallspotential (fester Seed); Durchlaufzeit gegen omega. Gegenprobe: glatte Zone.
4. **Neuron:** kleiner bis grosser Stoss (Amplitudenreihe) auf einen Ball; Antwortamplitude. Gibt es eine Schwelle mit
   Sprung, oder ist die Antwort linear bzw. glatt?
5. **Wundheilung:** Profil auf einer Seite um 10, 25 bzw. 50 % der Ladung beschnitten; Rueckkehr zur Gleichgewichtsform,
   Heilzeit, abgestrahlte Ladung.
6. **Nervenfaser:** Kette aus 6 Baellen; den ersten anstossen; Laufgeschwindigkeit der Erregung und Daempfung je Glied.
   Gegenprobe: grosser Abstand, dann keine Weiterleitung.
7. **Zufallskarte Bio 18, Artbildung** (nur Schiessen, Sekunden):
   - 3D radial m = 0 sowie 2D radial m = 0, 1, 2
   - Q(omega) und E(omega) je Familie fuer omega^2 von 0,51 bis 0,99
   - Verzweigungs- oder Knickpunkte (Q_min je Familie)
   - Gibt es Stellen, an denen zwei Familien gleiche (Q, E) haben ("Artgrenze")?
