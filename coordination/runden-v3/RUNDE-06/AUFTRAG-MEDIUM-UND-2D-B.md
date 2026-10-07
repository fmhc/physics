# Runde 6: Medium-Karten (1D und 2D) und Paket 2D-B (Kollektiv und Kristall), drei Anthropic-Agenten

Auftraggeber: claude-primary. Zeit vor dem Schreiben gemessen: 2026-09-30 02:51:40 CEST. Deutsch. Explorativ.
Finn: "rechne auch hier kleine erste runs und beschleunige das alles parallel mit mehr agents".

## Gemeinsamer Rahmen

- **Arbeitsweise:** coordination/runden-v3/README.md (v3, Latten L1 bis L5). Explorativ und leicht, keine formale
  Bestaetigung.
- **Ideen:** RUNDE-02/IDEEN-50-QBALL-BIOLOGIE.md, RUNDE-03/IDEEN-20-QBALL-CHEMIE.md,
  RUNDE-03/IDEEN-20-QBALL-WELLEN-WIND-SEGELN.md (die Nummern unten beziehen sich darauf).
- **Modell:** U(S) = S - S^2 + S^3/2, S = |psi|^2, L = |psi_t|^2 - |grad psi|^2 - U.
- **Warum ein zweites Feld:** Ein duennes, ruhiges Medium gibt es im Ein-Feld-Modell nicht. Der homogene Hintergrund ist
  fuer 0 < S < 2/3 modulationsinstabil (REVIEW-FABLE-20260930/REVIEW-FABLE.md, Z. 39-45).
  - Das stabile Medium ist ein zweites Feld chi mit U_chi = C + g4 C^2, C = |chi|^2, g4 > 0. Es ist bei jeder Dichte
    linear stabil.
  - Herleitung: RUNDE-05/r5d/PLAN.md, Abschnitt 1.3.
  - Schall: c_s^2 = g/(2 omega0^2 + g), mit g = 2 g4 C0 und omega0^2 = 1 + 2 g4 C0.
  - Fuer C0 = 0,1 und g4 = 0,5 ist c_s = 0,2085.
  - Kopplung an psi ueber lam S C (Dichte); Ladungsaustausch ueber eps (conj(psi) chi + c.c.), Vakuum stabil fuer
    mc2 >= eps^2.
- **Verifizierter Zwei-Feld-Code:** RUNDE-05/r5d/r5d.py. Er lief auf der .69, alle 7 Aufrufe rc 0; Ergebnisse in
  RUNDE-05/r5d/lauf-69/.
  - Im Lauf "kreuzen" (Ball ruhend im stroemenden Medium, periodische Box, L3 12 von 12) bewegt sich der Ball auch
    unter c_s: u/c_s = 0,48 gibt eine Verschiebung von +1,27 und v_Ende = 5,2e-3.
  - Die Vorhersage war "unter c_s keine Kraft". Ungeklaert ist, ob das ein Einschwing-Stoss ist (der Anfangszustand
    Ball-im-Medium ist keine exakte Loesung) oder eine echte Kraft.
- **Verifizierte 2D-Codes:** RUNDE-03/tests2d-r3/tests2d_r3.py (spektraler Laplace, radiales Schiessen m = 0/1,
  Tropfen- und Brechungstest gelaufen, Ergebnisse in lauf-69/). Paket 2D-A (RUNDE-05/r5-2d-a/) wird parallel gebaut.
  Nicht darauf warten.
- **Neu seit 02:42 (Finn im Chat an die Leitung):** Kleine lokale Rauchtests auf dem Laptop sind erlaubt:
  - Muster: `cd <dein Ordner> && mkdir -p lauf-lokal && CUDA_VISIBLE_DEVICES= OMP_NUM_THREADS=1 MKL_NUM_THREADS=1
    nice -n 19 timeout 120 python3 <skript> --geraet cpu <unterbefehl> <klein>`
  - Erlaubt sind python3 -m py_compile und Rauchtests, je hoechstens 120 s, nur CPU, 1 Thread, keine Laptop-GPU.
  - Die Messlaeufe startet die Leitung auf der .69.
  - Wenn du dir bei dieser Freigabe unsicher bist, lass es; die Leitung macht den lokalen Rauchtest dann selbst.
- **Abgabe je Agent:**
  - Code mit --geraet cuda|cpu, float64, Unterbefehle, Rauchtest mit Laufzeitfaktor
  - Rohdaten nach jeder Stufe sichern, damit eine abgestuerzte Auswertung nicht die Rechnung kostet (Lehre aus R5-C)
  - PLAN.md mit Vorhersagen vor dem Rechnen, Gegenproben, Aufloesungsvergleich (L3), Latten L1 bis L5, "Einfach gesagt"
  - PLAN.md mit Aufrufen ueber `cd /home/fmh/fmhc-physics-remote/<remote-ordner> && bash
    /home/fmh/fmhc-physics-remote/kleintests/kleintest.sh <spur> <kurzname> <skript> ...` (Spuren p4000a, p4000b, cpu,
    cpu2), je Aufruf hoechstens 10 min auf einer Quadro P4000 bzw. einem CPU-Kern
- **Grenzen:**
  - Kein ssh, kein git, kein Peerbus, keine Unteragenten, keine Geheimnisse.
  - Gesperrt: KS-1-Ergebnisse, T8-SOLL-*, coordination/vertraege-20260925/, ks-1-dk-lauf/, ks-1-dk-laeufe/.
  - Zeiten mit `date`. Budget hoechstens 80 Minuten.

## Agent M1: Medium-Karten in 1D (Ordner RUNDE-06/medium1d/, Remote runde6-medium1d)

Baue auf r5d.py auf (Medium-Rolle: kc = 0, g4 > 0; Kopplung lam; fuer Austausch eps). Karten:

1. **Wellen 5, Rumpfgeschwindigkeit und Landau-Schwelle:** Der psi-Ball bewegt sich mit v durch ruhendes Medium.
   - Gemessen wird die stationaere Bremskraft gegen v, getrennt vom Einschwingen. Dazu die Geschwindigkeit bzw. die
     Stroemung langsam hochfahren (adiabatisch) und die Kraft erst nach dem Abklingen messen.
   - Zu klaeren ist, ob die Kraft unter c_s verschwindet. Das ist auch die Klaerung des "kreuzen"-Befunds.
   - Zwei Mediendichten, damit sich c_s verschiebt: Wandert die Schwelle mit c_s mit?
2. **Wellen 6, Gleiten:** wie 1, bis v ~ 0,9. Hat die Bremskraft ueber der Schwelle ein Maximum?
3. **Wellen 7, Windschatten:** zwei psi-Baelle hintereinander, Abstand d in etwa 4 Werten. Kraft auf den hinteren mit und
   ohne Vordermann, ueber und unter c_s.
4. **Wellen 11, Fahrtwind:** bewegter Ball im ruhenden Medium gegen ruhender Ball im stroemenden Medium.
   - Wegen der Lorentz-Invarianz wird Gleichheit erwartet. Das ist eine Codeprobe.
   - Achtung: Die Lorentz-Transformation des Mediums ist nicht der Galilei-Shift; baue beide Zustaende korrekt auf.
5. **Wellen 3, Stokes im Medium:** Ball in einer laufenden Schallwelle des Mediums, zwei bis drei Amplituden. Drift je
   Periode gegen a (erwartet ~ a^2).
   - Anlass: Im Ein-Feld-Modell (Runde 4) ging die Drift linear mit a. Vermutlich lag die Welle bei t = 0 schon auf dem
     Ball. Deshalb die Welle von weit weg einlaufen lassen.
6. **Bio 2, Osmose:** Ladungsfluss zwischen Ball und Medium ueber eps. Zu messen:
   - Richtung und Rate gegen die Mediendichte
   - Gibt es eine Gleichgewichtsdichte, bei der kein Netto-Fluss fliesst ("isoton")?
7. **Chemie 9, Massenwirkung:** zwei bis drei Baelle im Medium mit eps. Stellt sich ein Gleichgewicht der Ladungen ein,
   das von der Mediendichte abhaengt wie ein Massenwirkungsgesetz?
8. **Bio 21, Nische:** Medium mit sanftem Dichtegefaelle. Wohin driftet ein Ball, und bleibt er bei einer bestimmten
   Dichte stehen?

Gegenproben:
- lam = 0 (keine Kraft)
- Medium allein (C bleibt konstant auf 1e-9)
- Spiegelung v -> -v
- zwei Aufloesungen

## Agent M2: Medium-Karten in 2D (Ordner RUNDE-06/medium2d/, Remote runde6-medium2d)

Baue einen 2D-Zwei-Feld-Code aus tests2d_r3.py (Laplace, Integrator, radiales Schiessen fuer psi) und dem chi-Medium
aus r5d.py (C0 = 0,1, g4 = 0,5, lam = 0,1 als Start; periodische Box fuer Stroemung). Karten:

1. **Wellen 8/9, Magnus und Flettner:** psi-Ball mit Windung m = +1 bzw. -1 bzw. 0 im stroemenden Medium. Querdrift
   gegen Stroemungsgeschwindigkeit und Vorzeichen von m. Gegenprobe: m = 0 ohne Querdrift.
2. **Wellen 4, Kielwasser:** Ball bewegt durch ruhendes Medium, unter und ueber c_s.
   - Muster der Schallwellen im Medium: Machkegel ueber c_s, Winkel gegen arcsin(c_s/v).
   - Bogoliubov-Dispersion beachten; ein Kelvin-Winkel ist nicht zu erwarten, begruende das kurz.
3. **Wellen 18, Wirbelstrasse:** Ball als Hindernis in schneller Stroemung des Mediums.
   - Loest er Wirbel (Phasenwindungen in chi) ab? Zahl und Takt gegen die Geschwindigkeit.
   - Literatur (aus dem Gedaechtnis, als [L] markieren): Wirbelablösung in BECs.
4. **Wellen 14, Brechung im Medium:** Ball schraeg durch eine Dichtestufe des Mediums. Wird er gebrochen, und wie haengt
   der Winkel von der Stufe ab?
   - Bezug: Runde 3 (Ein-Feld, Potentialstufe) folgte Snellius auf 0,01 Grad; steil verlor der Ball 92 bis 94 % seiner
     Ladung.
5. **Wellen 15, Linse** (wenn die Zeit reicht): Reihe paralleler Baelle durch eine linsenfoermige Dichtezone des
   Mediums; Brennweite.
6. **Wellen 17, Kelvin-Helmholtz** (wenn die Zeit reicht): grosser psi-Ball in tangentialer Stroemung. Wachsen
   Oberflaechenwellen ab einer Schwelle?

Gegenproben:
- lam = 0
- Medium allein (Stroemung bleibt exakt)
- m -> -m spiegelt die Querdrift
- zwei Aufloesungen

## Agent B: Paket 2D-B, Kollektiv und Kristall (Ordner RUNDE-05/r5-2d-b/, Remote runde5-2d-b)

Ein-Feld-Modell in 2D, Code aus tests2d_r3.py. Kein Medium noetig; wo eine Karte eines braucht, markiere sie
("braucht chi-Medium, siehe M2") und lass sie aus. Karten:

- **Bio 25/42, Gitter und Wabe:** Quadrat- und Dreiecksgitter aus 9 bis 16 Baellen mit Phasenmustern (alle gleich,
  schachbrettartig wechselnd, Windungsmuster). Haelt das Gitter, verschmilzt es, oder laeuft es auseinander?
- **Chemie 13, Wechselphasen-Kristall:** Gegenphasige Nachbarn stossen sich ab, gleichphasige ziehen sich an (bekannt,
  [L]). Gibt es eine stabile Anordnung mit gemischten Phasen?
- **Bio 11, Gluehwuermchen:** Synchronisieren die inneren Phasen bzw. Atmungen in einem Ring aus 6 bis 8 Baellen?
  Anschluss an den 1D-Synchronisationstest aus Runde 2.
- **Bio 46, Kapsid:** Ring aus N Baellen (N = 5 bis 8) mit Windung 2 pi/N als Ringanalogon. Stabil?
- **Bio 47, Haendigkeit:** Windung +1 gegen -1 in einem Gitter. Bevorzugt die Dynamik eine Haendigkeit?
- **Chemie 5, Isomere:** Gleiche Ballzahl, zwei Anordnungen (Kette gegen Dreieck). Energieunterschied und Umwandlung?
- **Chemie 19, Aromatizitaet:** Ring aus 6 Baellen mit gleicher gegen wechselnder Phase. Ist einer deutlich stabiler?
- **Bio 26, Schleimpilz, und Bio 40, Schwarm:** nur, wenn es eine einfache Umsetzung ohne Medium gibt; sonst kurz
  begruenden, warum nicht.
- **Wellen 19, Auge des Tornados:** m = 1-Profile bei drei Q. Kernradius gegen Q; welche Regel?

Hinweis: Die 1D-Bindungskurve E(d, Delta phi) (Runde 3, Chemie 2/3) ist abgestuerzt und wird gerade repariert. Ob Paare
binden, ist also offen. Deine Gittertests sollen das selbst sichtbar machen, statt es vorauszusetzen.
