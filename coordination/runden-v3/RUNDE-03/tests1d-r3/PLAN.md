# Runde 3, 1D-Tests: Laufplan und Vorhersagen

Bearbeiter: Anthropic-Agent (Opus), Auftrag RUNDE-03/AUFTRAG-1D.md, dazu die zwei Nachrichten der Leitung (neuer
Rechenort P4000 um 01:31; Fable-Hinweis zu Wellen 5 um etwa 02:00). Beginn 2026-09-30 01:20:28 CEST (gemessen), Ende in
der letzten Zeile. Status: Code geschrieben, **ungetestet, nicht gerechnet**. Explorativ.

**Version 2 (30.09., ab 02:50:57 CEST):** Auf der .69 liefen t1 und t3 bis t6 mit rc 0; t2 brach mit "Relaxation
instabil" ab. Nur test2 ist neu geschrieben; Ursache, Aenderung und Nachlauf in Abschnitt 12. Die Vorhersagen bleiben
unveraendert.

## Kurzfassung

- **Code:** tests1d_r3.py (PyTorch, float64 bzw. complex128, nur CUDA), Unterbefehle profil, t1 bis t6, alle.
  - Schiessen, Gitter, Zeitschritt und Integrator sind aus RUNDE-01/qg1/qg1.py uebernommen.
  - Jeder Test rechnet grob (dx = 0,1, dt = 0,05) und fein (halbiert); der Vergleich ist Latte L3.
- **Laufzeit auf der P4000 (geschaetzt):** zusammen etwa 10 min (6 bis 15), je Test hoechstens 3 min.
- **Wellen 5 (Rumpfgeschwindigkeit) ist im Ein-Feld-Modell nicht umsetzbar.** t6 rechnet nur die Dispersionstabelle,
  keine Zeitentwicklung (Abschnitt 8).
- **Vorhersagen in einem Satz je Karte:**
  - Chemie 1: Ladung pendelt, die Richtung folgt der Anfangsphase; im Phasenmittel fliesst nichts von klein nach gross.
  - Chemie 2/3: Gleichphasig gibt es kein Molekuel; das einzige Minimum ist der verschmolzene Ball.
  - Chemie 7: Gleichphasige verschmelzen langsam und laufen schnell durch; gegenphasige verschmelzen bei keinem v.
  - Chemie 15: Die Anfangssteigung faellt nicht exponentiell mit der Brueckenzahl.
  - Chemie 14: Q und Anti-Q vernichten sich in T = 1000 nicht zur Haelfte; nah beieinander bleibt ein
    ladungstauschendes Gebilde.
- Alle Vorhersagen sind meine Hypothesen, nicht Messungen; Handrechnungen ohne Interpreter.

## 1. Aufruf (Leitung, .69, Spur p4000a)

Vorschlag: tests1d_r3.py nach /home/fmh/fmhc-physics-remote/r3-tests1d-20260930/ kopieren. kleintest.sh setzt Lock, Unit,
CUDA_VISIBLE_DEVICES, RuntimeMaxSec 600 und das Arbeitsverzeichnis. Das Programm braucht nur torch und schreibt nur in
--out.

1. Profile schiessen, einmal (etwa 2 bis 3 min):

   ```
   cd /home/fmh/fmhc-physics-remote/r3-tests1d-20260930 && bash /home/fmh/fmhc-physics-remote/kleintests/kleintest.sh p4000a r3t1d-profil tests1d_r3.py profil --out ausgabe
   ```

2. Rauchtest, alle Tests mit Laufzeiten x 0,1 (etwa 1 bis 2 min):

   ```
   cd /home/fmh/fmhc-physics-remote/r3-tests1d-20260930 && bash /home/fmh/fmhc-physics-remote/kleintests/kleintest.sh p4000a r3t1d-rauch tests1d_r3.py alle --kurz --out rauchtest --profil ausgabe/profile_r3.pt
   ```

3. Hauptlauf, je Test eine Unit (die Profile liegen dann in ausgabe/):

   ```
   cd /home/fmh/fmhc-physics-remote/r3-tests1d-20260930 && bash /home/fmh/fmhc-physics-remote/kleintests/kleintest.sh p4000a r3t1d-t1 tests1d_r3.py t1 --out ausgabe
   ```

   ebenso mit `r3t1d-t2 ... t2`, `r3t1d-t3 ... t3`, `r3t1d-t4 ... t4`, `r3t1d-t5 ... t5`, `r3t1d-t6 ... t6`.

- Der Rauchtest zeigt nur, ob das Programm durchlaeuft; seine Zahlen gelten nicht.
- Hochrechnung: Hauptlauf eines Tests etwa zehnmal seine Rauchtestdauer (Zeile "Dauer" im Bericht). Ergibt das mehr als
  8 min, diesen Test nicht starten; die Leitung entscheidet.
- `alle` ohne `--kurz` wuerde die 600 s einer Unit wahrscheinlich reissen; deshalb im Hauptlauf eine Unit je Test.
- Speicher: alle Felder zusammen unter 0,3 GB (groesster Stapel 26 x 4801 complex128), weit unter 2,5 GB.

**Ausgaben** (im --out-Ordner, Rauchtest mit Endung _kurz):
- profile_r3.pt: Schiessbahnen fuer omega^2 = 0,6 / 0,7 / 0,8 / 0,85
- profil_bericht.txt und profil_ergebnis.json: f(0)^2 gegen den Anker, Kontrolle K0
- tN_bericht.txt (auch auf stdout) und tN_ergebnis.json: alle Zahlen, Zeitreihen ausgeduennt

## 2. Laufzeit je Test (Schaetzung, nicht gemessen)

Grundlage ist der QG-1-Lauf auf der P5000: etwa 1,2 ms je Verlet-Schritt fuer 27 x 4801 Punkte, begrenzt durch die Zahl
der kleinen GPU-Aufrufe, nicht durch die Arithmetik. Fuer die P4000 habe ich alles mit 1,7 multipliziert (obere Schaetzung).

| Unterbefehl | Arbeit (grob + fein) | P4000 erwartet |
|---|---|---|
| profil | Schiessen wie qg1 (4 omega gleichzeitig), P5000 84 s | 1,5 bis 3 min |
| t1 Elektronegativitaet | 21 Laeufe, T = 400: 8000 + 16000 Schritte | 0,5 bis 1,5 min |
| t2 Bindungskurve | 26 Relaxationen, tau = 600: 12000 + 24000 Schritte, je etwa doppelt so viele Aufrufe | 1 bis 3 min |
| t3 Stoesse | 24 Laeufe, T = 800: 16000 + 32000 Schritte | 1 bis 2,5 min |
| t4 Bruecke | 12 Laeufe, T = 400 | 0,5 bis 1,5 min |
| t5 Q und Anti-Q | 16 Laeufe, T = 1000, Messung alle 0,5: 20000 + 40000 Schritte | 1 bis 3 min |
| t6 Wellen 5 | nur Dispersionstabelle, keine Zeitentwicklung | unter 0,5 min |
| **zusammen** | dazu je Unit etwa 10 s Start | **etwa 10 min (6 bis 15)** |

## 3. Gemeinsame Festlegungen

- **Modell:** L = |psi_t|^2 - |psi_x|^2 - U(S), U = S - S^2 + S^3/2, eine Raumdimension.
  - Ball psi = f exp(-i omega t), Anti-Ball psi = f exp(+i omega t).
  - Ladungsdichte rho = 2 Im(psi conj(psi_t)).
- **Profile:** Schiessen wie qg1 (RK4, h = 0,01, bis x = 80, 4 x 4096 Kandidaten), einmal fuer alle vier omega.
  - Auswertung an beliebiger Stelle: lineare Interpolation der Bahn; die Ableitung kommt aus dem ersten Integral.
  - Kontrolle K0 wie qg1: max |f_Schuss - f_Anker| <= 1e-6 auf beiden Gittern; bei mehr als 1e-5 bricht das Programm ab.
- **Bewegte Baelle:** exakter Lorentz-Boost, denn das Modell ist Lorentz-invariant.
- **Mehrere Baelle:** Summe der Einzelloesungen. Bei ueberlappenden Auslaeufern ist das keine exakte Loesung; der
  Anfangsruck ist Teil jedes Laufs.
- **Box, Rand, Integrator:** wie qg1: [-120, 120], Daempfungsschicht ab |x| = 80, Velocity-Verlet.
  - Messbereich |x| < 75, vor der Schicht.
- **Latte L3:** Effekt fein geteilt durch |fein - grob|; bestanden ab 5. Jeder Bericht nennt diese Quote.

Bezugszahlen aus dem 1D-Anker (von Hand, a0 = 1 - omega^2, b0 = sqrt(2 omega^2 - 1), kappa = sqrt(a0),
Schwanz f ~ A exp(-kappa |x|) mit A = 2 kappa / sqrt(b0)):

| omega^2 | omega | Q | E | kappa | A |
|---|---|---|---|---|---|
| 0,60 | 0,7746 | 3,1628 | | 0,6325 | 1,892 |
| 0,70 | 0,8367 | 2,4415 | 2,2986 | 0,5477 | 1,377 |
| 0,80 | 0,8944 | 1,8859 | | 0,4472 | 1,016 |
| 0,85 | 0,9220 | 1,604 | | 0,3873 | 0,847 |

## 4. Test 1, Chemie 1 (Elektronegativitaet)

**Aufbau:** Zwei ruhende Baelle, links omega^2 = 0,8 (klein), rechts 0,6 (gross), Abstand d = 8, 10, 12. T = 400.
- Ladung links und rechts von x = 0 (Mitte der Startorte). Gemessen wird die Verschiebung z = (dQ_rechts - dQ_links)/2;
  sie ist unempfindlich gegen gleichmaessigen Abstrahlverlust. Berichtet wird dQ_klein = -z.
- Anfangsphase phi0 des grossen Balls: 0 (gleichphasig, wie im Auftrag), dazu pi/2, pi und 3pi/2. Die drei weiteren
  Phasen sind ein **Zusatz der Bearbeitung**.
- Gegenproben:
  - Auftrag: gleiche omega (0,8/0,8 und 0,6/0,6). Kein Nettofluss aus Symmetrie; das prueft nur Code und Messung.
  - Zusatz der Bearbeitung: Spiegelbild (gross links); es muss dieselben Zahlen geben.
- **Messgroessen:**
  - Mittel der Ladungsaenderung des kleinen Balls auf [T/2, T], je phi0
  - halbe Schwankungsbreite auf [T/8, T] (Amplitude)
  - Periode aus der FFT
  - Phasenmittel ueber die vier phi0 (der richtungsfeste Anteil)
- **Urteilsregel (fest):**
  - |Phasenmittel| >= 0,2 x Amplitude und negativ: "Nettofluss klein -> gross" (H bestaetigt).
  - Dasselbe, aber positiv: "gegen H".
  - Sonst: "kein Nettofluss, Pendeln".

**Warum die Phasen:** Zwei schwach gekoppelte Kondensate mit verschiedenem chemischem Potential zeigen den
Wechselstrom-Josephson-Effekt.
- Die Relativphase dreht mit omega1 - omega2, der Strom ist J sin(Relativphase).
- Die Ladung pendelt also mit der Periode 2 pi/(omega1 - omega2), ohne Gleichanteil.
- Nur der Anfangswert legt fest, ob der kleine Ball im Mittel etwas abgibt: dQ_klein(t) = (J/Dw)[cos(Dw t + phi0) - cos phi0],
  mit Dw = omega1 - omega2.
- Gleichphasig gibt er also im Mittel J/Dw ab und saehe wie H aus. Gegenphasig nimmt er auf.
- Die gleichphasige Einzelmessung allein kann H deshalb nicht pruefen.

**Vorhersage (vor dem Rechnen):**
- Periode 2 pi/(0,8944 - 0,7746) = 52,4, bei d = 8 durch die Nichtlinearitaet merklich verschoben.
- Amplitude J/Dw aus dem Strom am Mittelpunkt, J = 2 (k1 + k2) A1 A2 exp(-(k1 + k2) d/2):
  - etwa 0,46 / 0,16 / 0,05 bei d = 8 / 10 / 12, Faktor 2 unsicher
  - das sind 24 / 8 / 3 Prozent von Q_klein = 1,886
  - von Abstand zu Abstand Faktor exp(-(k1 + k2) x 2) = 0,34
- Mittelwerte je phi0 etwa -A cos phi0: bei 0 gibt der kleine Ball im Mittel ab, bei pi nimmt er auf, bei pi/2 und
  3pi/2 nahe null.
- **Phasenmittel:** In erster Ordnung null. In zweiter Ordnung (meine Rechnung, Hypothese) gibt es einen kleinen
  Gleichanteil **zum kleinen Ball hin, also gegen H**.
  - Grund: Die Phase dreht langsamer, wenn die omega sich annaehern; dort verweilt das System laenger.
  - Groesse etwa (U/Dw) A^2 mit U = d(Dw)/dQ = 0,15 und U/Dw = 1,2.
  - Das ist rund 25 Prozent von A bei d = 10 und 7 Prozent bei d = 12. Bei d = 8 (A = 0,46) gilt die Naeherung nicht
    mehr; dort ist starkes, unregelmaessiges Pendeln oder Verschmelzen moeglich.
- **Urteil erwartet:**
  - d = 12: "kein Nettofluss"
  - d = 10: nahe der Schwelle, eher "gegen H"
  - d = 8: offen
  - In keinem Fall erwarte ich "klein -> gross". H in der Fassung "Ladung fliesst von selbst vom kleinen zum grossen
    Ball" scheitert nach dieser Vorhersage.
- Gleiche omega: Mittel unter 1e-10 (Symmetrie). Spiegel: Unterschied unter 1e-10.
- Die gleichphasigen Kontrollpaare mit gleichem omega ziehen sich dauerhaft an und verschmelzen, grob geschaetzt nach
  einigen zehn (d = 8) bis etwa hundert (d = 12) Zeiteinheiten; an der Symmetrie aendert das nichts. Die ungleichen Paare
  verschmelzen nicht, weil die Kraft mit der Periode 52 das Vorzeichen wechselt (bei d = 8 unsicher).

## 5. Test 2, Chemie 2/3 (Bindungskurve und Morse)

**Wahl des Verfahrens: Relaxation bei fester Ladung.** Eine stationaere Paarloesung gibt es bei gleichem omega nicht:
Gleichphasige Baelle ziehen sich an, gegenphasige stossen sich ab.
- Relaxiert wird mit gedaempfter Dynamik (Verlet, Daempfung 1, Pseudozeit 600) das Funktional bei fester Gesamtladung:
  E_Q[phi] = Q^2/(4N) + Int phi_x^2 + Int U(phi^2), N = Int phi^2, omega = Q/(2N). Dabei ist phi reell.
- Delta phi = 0 heisst phi symmetrisch, Delta phi = pi heisst phi antisymmetrisch; die Symmetrie wird jeden Schritt
  erzwungen.
  - Das haelt die Ladung **je Ball** fest.
  - Ohne das liefe die Relaxation zum Ostwald-Zustand, weil E(Q) in 1D konkav ist (d omega/dQ < 0). Ladung wanderte dann
    zu einem Ball.
- Der Abstand d = 2X (X = Schwerpunkt von phi^2 auf x > 0) wird gehalten:
  - Die Kraftkomponente, die X aendert, wird entfernt.
  - Eine schwache Feder (K = 5) faengt die Drift zweiter Ordnung.
  - Ausgewertet wird das gemessene d.
- Nullpunkt: dasselbe Paar bei d = 40 auf demselben Gitter; das ist ein Zusatz der Bearbeitung. E(40) - 2 E1 wird als
  Kontrolle berichtet.
- omega^2 = 0,7 je Ball, q = 2,4415. d = 1,5 / 2 / 2,5 / 3 / 3,5 / 4 / 5 / 6 / 7 / 8 / 10 / 12, also 12 Abstaende.
- **Auswertung:**
  - Morse-Anpassung E = D (1 - exp(-a (d - d0)))^2 + const fuer Delta phi = 0. Dafuer a im Raster 0,05 bis 3, der Rest
    linear.
  - Exponentialanpassung ln|E_int| = ln C - kappa d fuer d >= 6, fuer 0 und pi.
  - Minimum mit Parabel durch drei Punkte, daraus die Schwingungsfrequenz omega_vib = sqrt(E''/mu), mu = E1/2.

**Vorhersage (vor dem Rechnen):**
- **Asymptotik (meine Herleitung ueber den Spannungstensor am Mittelpunkt):** E_int ~ -4 kappa A^2 cos(Delta phi)
  exp(-kappa d) = -4,16 cos(Delta phi) exp(-0,548 d).
  - E_int(0) bei d = 8 / 10 / 12: -0,052 / -0,0174 / -0,0058; E_int(pi) mit umgekehrtem Vorzeichen.
  - Die Anpassung fuer d >= 6 trifft kappa auf 10 Prozent.
  - E_int(pi)/E_int(0) liegt bei d = 10 und 12 zwischen -1,2 und -0,8.
- **Delta phi = 0:** E_int < 0 bei allen d, faellt zu kleinen d hin. Das einzige Minimum ist der **verschmolzene Ball**
  mit Ladung 2q (omega^2 etwa 0,516).
  - Lage d0 = 2X = 2,6 (Handintegration des Ankers), Tiefe D = 2 E1(q) - E1(2q) = 4,597 - 4,149 = 0,448.
  - Beides folgt aus dem Anker; die Zahlen sind vorab ableitbar (L4).
  - Ein Minimum bei getrennten Baellen (ein "Molekuel") erwarte ich nicht. Das stimmt mit dem Fable-Review ueberein.
- **Delta phi = pi:** E_int > 0 bei allen d, monoton fallend, kein Minimum.
- **Morse:** passt mit einem Rest unter 5 Prozent von D; a liegt zwischen 0,4 und 0,9 (kappa = 0,548).
  - Schwanzkoeffizient 2 D exp(a d0) in der Groesse von C = 4,16 (Faktor 2).
- **Schwingung (Idee 4, Nebenprodukt):** omega_vib = sqrt(2 D a^2/mu) etwa 0,5 (0,4 bis 0,75).
  - Das liegt ueber 1 - omega_verschmolzen = 0,28. Die Schwingung des verschmolzenen Balls strahlt also ab; eine
    scharfe "IR-Linie" erwarte ich nicht.
- **Kontrollen:**
  - |E(40) - 2 E1| unter 1e-4, klein gegen |E_int(12)| = 0,0058 (Gitterversatz des geschossenen Profils)
  - Konvergenz |E(600) - E(480)| unter 1e-3 |E_int| bei allen d <= 10
  - |d_ist - d_soll| unter 0,01
- **Scheitern von H (Morse-Bindung):**
  - Morse-Rest ueber 10 Prozent von D, oder a ausserhalb 0,4 bis 0,9
  - oder ein zweites Minimum bei getrennten Baellen (das waere ein Befund-Kandidat gegen den Review)

## 6. Test 3, Chemie 7 (Aktivierungsenergie, Stoesse)

**Aufbau:** Zwei gleiche Baelle omega^2 = 0,7 bei -8 und +8, Geschwindigkeit +v und -v, Phase des rechten Balls
Delta phi = 0, pi/2, pi. Dazu -pi/2 als Spiegel-Gegenprobe (**Zusatz der Bearbeitung**). v = 0,05 / 0,1 / 0,2 / 0,3 /
0,45 / 0,6; T = 800.
- **Klassen:**
  - "getrennt": Der Abstand der Schwerpunkte von |psi|^2 in beiden Halbraeumen steigt nach der engsten Annaeherung ueber 30.
  - "verschmolzen": sonst, wenn am Ende mehr als die Haelfte der Ladung in |x| < 6 liegt und der Abstand unter 10 ist.
  - sonst "gebunden/unklar"
- Bei Delta phi = 0 und pi ist Durchlaufen von Abprallen nicht zu unterscheiden: Die Anordnung ist spiegel(anti)symmetrisch,
  |psi|^2 bleibt symmetrisch. Beides heisst dort "getrennt".
- Bei +-pi/2 entscheidet die Relativphase der beiden Maxima beim Trennen:
  - Beim Abprallen behaelt sie das Vorzeichen von Delta phi, beim Durchlaufen dreht es sich (die Boost-Phasen heben sich
    auf).
  - Das ist eine Heuristik; Ladungsuebertrag verfaelscht sie.
- "Barriere": kleinstes v mit "verschmolzen" je Delta phi; berichtet wird auch das groesste.

**Vorhersage (vor dem Rechnen):**
- **Delta phi = 0:** verschmolzen bei v <= 0,2, getrennt bei v >= 0,45, der Uebergang dazwischen.
  - Es gibt keine Barriere (schon v = 0,05 verschmilzt), sondern eine **obere** Grenze.
  - Grund: Schnelle Baelle haben mit 2 (gamma - 1) E1 mehr Bewegungsenergie als die Bindungstiefe D = 0,45, zum Beispiel
    1,15 bei v = 0,6.
- **Delta phi = pi:** getrennt bei allen sechs v, keine Verschmelzung.
  - Die Antisymmetrie erzwingt einen Knoten in der Mitte; ein einzelner Ball dort ist unmoeglich.
  - Bei v = 0,05 prallen sie schon bei d etwa 12 ab, ohne sich zu beruehren (Abstossung 4,16 exp(-0,548 d) gegen
    Bewegungsenergie 0,0057).
  - H ("gegenphasig erst ab einer Mindestgeschwindigkeit") scheitert damit im gerechneten Bereich.
- **Delta phi = +-pi/2:** Beim Annaehern wandert Ladung (Josephson-Strom maximal), die Baelle werden ungleich.
  - Langsam: verschmolzen (v <= 0,2). Schnell: getrennt, mit Ladungsasymmetrie ueber 10 Prozent.
- **Gegenproben:** +pi/2 und -pi/2 geben dieselben Klassen und entgegengesetzte Asymmetrie.
  - L3: hoechstens eine Klasse wechselt zwischen grob und fein, und nur an einer Uebergangsstelle.
- **L4:** Battye und Sutcliffe (2000) und Axenides u. a. (2000) haben Q-Ball-Stoesse mit Phasenabhaengigkeit in 2D/3D
  gerechnet [aus dem Gedaechtnis, nicht nachgelesen]; das Muster "gleichphasig verschmilzt, gegenphasig prallt ab,
  pi/2 tauscht Ladung" steht dort sinngemaess.

## 7. Test 4, Chemie 15 (Redox ueber eine Bruecke)

**Aufbau:** Kette Spender omega^2 = 0,85 - n Bruecken 0,7 - Empfaenger 0,6, Abstand 10, n = 0 bis 3; T = 400.
- **Varianten:**
  - D0: alle gleichphasig (Hauptmessung laut Auftrag)
  - D90: Spender um pi/2 gedreht, **Zusatz der Bearbeitung**
  - ohne Spender, **Zusatz der Bearbeitung**: Kontrolle, zeigt, was die Bruecken allein am Empfaenger tun
- Transferrate = Anfangssteigung: Geradenfit der Empfaengerladung (Zelle jenseits der Mitte zur letzten Bruecke) auf
  t = 2 bis 15.
  - Spendereffekt = dieselbe Steigung fuer die Differenz zum Lauf ohne Spender.
- **Regel "exponentiell" (fest):** Die Betraege fallen je Bruecke, alle drei Verhaeltnisse s(n+1)/s(n) liegen unter 0,5,
  und das groesste ist hoechstens doppelt so gross wie das kleinste.

**Vorhersage (vor dem Rechnen):**
- **Rohe Anfangssteigung (D0), die Messung des Auftrags:** kein exponentieller Abfall; **H scheitert**.
  - n = 0: Der Empfaenger koppelt direkt an den Spender. J = 0,020, Dw = 0,147, Steigung auf [2, 15] etwa 0,016.
  - n >= 1: Der Empfaenger tauscht zuerst mit seinem Nachbarn, der letzten Bruecke. J = 0,017, Dw = 0,062, Steigung
    etwa 0,008, fast unabhaengig von n.
  - Verhaeltnisse etwa 0,5 / 1 / 1. Die Messgroesse misst den Nachbarn, nicht den Spender.
- **Spendereffekt (Differenz ohne Spender):** faellt steil mit n, grob exp(-(k_D + k_A) x 10/2) je Bruecke, also
  Faktor 0,01 bis 0,05 je Bruecke.
  - Bei n = 3 wird er so klein (unter 1e-6), dass L3 dort wahrscheinlich reisst. Das Urteil "exponentiell" ist dann
    offen, nicht bestaetigt.
- D90 wie D0, nur bei n = 0 mit linearem Anfang (Steigung etwa J = 0,02).

## 8. Wellen 5 (Rumpfgeschwindigkeit): im Ein-Feld-Modell nicht umsetzbar

Papierrechnung, vor jedem Lauf (auch Codex' Dispersionsrelation und der Fable-Review, REVIEW-FABLE.md Z. 39-45):
- **Hintergrund:** psi = sqrt(S) exp(-i omega_bg t) mit omega_bg^2 = U'(S) = 1 - 2S + 1,5 S^2.
- **Bogoliubov-Zweige** (linearisiert um den Hintergrund, von Hand hergeleitet):
  - Omega^2 = [B -+ sqrt(B^2 - 4 k^2 (k^2 + beta))]/2
  - mit B = 2k^2 + beta + 4 omega_bg^2 und beta = 2 S U''(S) = -4S + 6S^2
- **S < 2/3 (duenn):** beta < 0. Fuer k^2 < -beta ist Omega^2 < 0: modulationsinstabil, der Hintergrund klumpt zu
  Q-Baellen.
  - Die groesste Wachstumsrate ist etwa S (bei S = 1e-3 etwa 1e-3).
  - Weil Omega an der Bandkante k^2 = -beta durch null geht, ist v_c = min Omega/k = 0. Es gibt keine Landau-Schwelle,
    die Hypothese muss scheitern.
  - Eine Messung dort wuerde ein Modellartefakt zum Befund machen. Keine Scheinmessung: t6 rechnet keine Dynamik.
- **S >= 2/3:** stabil, Schallgeschwindigkeit c_s = sqrt(beta/(beta + 4 omega_bg^2)): 0,31 / 0,55 / 0,71 bei S = 0,7 /
  0,8 / 1,0. Landau gaebe v_c = c_s. Aber:
  - Dort ist omega_bg <= 0,707, kleiner als jedes Ball-omega. Der Ball hat das hoehere chemische Potential und loest sich
    auf.
  - Buckel gibt es auf einem stabilen Hintergrund nicht. Der zweite Umkehrpunkt der Profilgleichung liegt bei
    S = 2 - 2 S_bg < S_bg; es gibt nur Dellen ("Blasen"), bei S_bg = 0,8 bis S = 0,4 hinab.
  - Ein Q-Ball, der durch den Hintergrund faehrt, existiert also nicht.
- **t6:** Tabelle ueber S von 1e-3 bis 1,0 (Stabilitaet, Wachstumsrate, Verstaerkung in 400, v_c, c_s, Gegenpunkt
  2 - 2S). Das ist eine Papierprobe mit Rechner, keine Messung.
- **Mit einem zweiten Feld ginge es:** Ist das Medium ein eigenes Feld chi mit bei kleiner Dichte abstossender
  Selbstwechselwirkung und einer Kopplung g |psi|^2 |chi|^2, dann ist ein duenner Hintergrund stabil (c_s > 0), der Q-Ball
  ist darin ein Fremdkoerper, und das Landau-Kriterium sagt v_c = c_s voraus. Das ist von bewegten Hindernissen in
  Bose-Einstein-Kondensaten bekannt (L4; Raman u. a. 1999, [aus dem Gedaechtnis]).

## 9. Test 5, Chemie 14 (Zufallskarte): Q gegen Anti-Q

**Aufbau:** Ball exp(-i omega t) bei -d/2, Anti-Ball exp(+i omega t) bei +d/2, omega^2 = 0,7, in Ruhe, d = 3 / 5 / 8 /
12; Anfangsphase theta = 0 und pi.
- Kontrolle (**Zusatz der Bearbeitung**): Ball-Ball-Paar mit denselben d und theta.
- T = 1000, Messung alle 0,5.
- **Messgroessen:**
  - Betragsladung Q_abs = Int |rho| in |x| < 75
  - t50: das gleitende Maximum ueber 20 Zeiteinheiten faellt unter Q_abs(0)/2. Ladungstausch laesst Q_abs kurz
    einbrechen; der rohe Wert wird mitberichtet.
  - t10
  - Endzustand: Rest Q_abs, Rest-Energie im Messbereich, max |psi|^2, Zahl der Klumpen, Vorzeichenwechsel der Ladung
    rechts in den letzten 200

**Vorhersage (vor dem Rechnen):**
- Die Relativphase dreht mit 2 omega = 1,67. Die Wechselwirkung mittelt sich in erster Ordnung weg; eine schnelle
  Vernichtung erwarte ich nicht.
- **d = 3** (starke Ueberlappung):
  - Q_abs(0)/2q etwa 0,6 bis 0,8, weil sich rho am Anfang teilweise aufhebt.
  - Rasch ein Verlust von 10 bis 40 Prozent als Strahlung (t10 unter 100).
  - Danach ein langlebiges, ladungstauschendes Gebilde (Copeland, Saffin, Zhou 2014, "charge-swapping Q-balls", fuer
    genau diese Potentialklasse [aus dem Gedaechtnis]).
  - t50 (geglaettet) wird in T = 1000 nicht erreicht. Endzustand "Restgebilde mit Ladungstausch".
- **d = 5:** Verlust unter 10 Prozent, zwei Klumpen oder Tauschgebilde.
- **d = 8 und 12:** Rest Q_abs ueber 0,95 bzw. 0,99, Endzustand "Restbaelle".
- **Kontrolle Ball-Ball:** Q_abs = Q, Verlust nur durch abgestrahlte Ladung, unter 2 Prozent.
  - Gleichphasig verschmelzen sie bei d = 3 und 5; gegenphasig stossen sie sich ab.
- **H scheitert,** wenn t50 bei d = 8 oder 12 erreicht wird, oder wenn bei d = 3 nichts Lokalisiertes bleibt (dann
  vernichten sich Q und Anti-Q doch rasch).

## 10. Latten (Vorschlag, die Leitung entscheidet)

| Karte | L1 kann scheitern | L2 Gegenprobe | L3 Numerik | L4 schon bekannt | L5 Messbezug |
|---|---|---|---|---|---|
| Chemie 1 | ja: Regel fuer das Phasenmittel vorab fest; "klein -> gross" oder "gegen H" moeglich | ja: gleiche omega, Spiegel, vier Anfangsphasen | geplant: fein/grob, Faktor 5 | weitgehend: Wechselstrom-Josephson in Doppelmulden-BEC (Smerzi u. a. 1997, [G]) | mittelbar: Josephson-Messungen an BEC (Albiez u. a. 2005, [G]); Elektronegativitaet nur Analogie |
| Chemie 2/3 | ja: Morse-Rest, a gegen kappa, zweites Minimum | ja: Delta phi = pi, d = 40 | geplant | weitgehend: Asymptotik (Solitonen-Wechselwirkung), Tiefe und Lage aus dem Anker ableitbar | nein: Morse/HCl nur Analogie |
| Chemie 7 | ja: Verschmelzen bei pi oder kein Verschmelzen bei 0 | ja: Spiegel +-pi/2 | geplant: Klassen fein/grob | ja: Battye/Sutcliffe 2000 [G] | nein |
| Chemie 15 | ja: Regel "exponentiell" vorab fest | ja: ohne Spender | geplant; n = 3 vermutlich zu klein | teilweise: Schwanzabfall ableitbar | mittelbar: Abstandsgesetz des Elektronentransfers, keine Zahlenbruecke |
| Chemie 14 (Zufall) | ja: t50 bei grossem d, nichts Lokalisiertes bei d = 3 | ja: Ball-Ball-Paar | geplant | ja: Copeland/Saffin/Zhou 2014 [G] | nein |
| Wellen 5 | im Ein-Feld-Modell nein: v_c = 0 ist erzwungen | entfaellt | entfaellt | ja: Modulationsinstabilitaet, Landau fuer Hindernisse im BEC | mittelbar (BEC-Hindernis-Versuche), nur mit zweitem Feld |

[G] = aus dem Gedaechtnis, nicht nachgelesen.

## 11. Grenzen

- **Ungetestet:** Auf dem Laptop gilt das Interpreterverbot; zuerst der Rauchtest.
- **Anfangsbedingungen:** Summen von Einzelloesungen. Der Anfangsruck strahlt; Fenster und Glaettung sollen ihn
  ausblenden.
- **Klassifikation in Test 3:** Die Schwellen (30, 6, 0,5) sind feste Setzungen. Durchlaufen gegen Abprallen ist nur bei
  +-pi/2 und nur heuristisch bestimmt.
- **Test 4:** Die Zellgrenzen liegen in der Mitte zwischen den Baellen. Bewegen sich die Baelle, wandert Ladung scheinbar
  mit. Bei T = 400 und dem kurzen Steigungsfenster ist das klein.
- **Vorhersagen:** Die Josephson-Groessen in Test 1 und 4 kommen aus einer Punktformel fuer den Strom (Faktor 2
  unsicher). Die zweite Ordnung in Test 1 und die Asymptotik in Test 2 sind meine Herleitungen; kein zweites Haus hat sie
  gelesen.
- **Nutzen:** Alles ist 1D und ein Feld. Mehrere Ergebnisse sind vorab ableitbar (L4). Neu waeren vor allem ein
  Gleichanteil gegen H in Test 1, der Morse-Rest in Test 2 und die Grenzgeschwindigkeiten in Test 3.

## 12. Aenderung Version 2: test2 (30.09., ab 02:50:57 CEST)

**Befund auf der .69 (Version 1):**
- Die Unit fmhc-physics-klein-r3t1d-t2-002912 endete nach 30,7 s mit rc 1: "RuntimeError: Relaxation instabil", also
  nicht endliche Werte am Ende der groben Stufe.
- Profil und K0 waren in Ordnung (9,8e-11); der Rauchtest mit tau = 60 lief durch.

**Ursache** (aus dem Code und dem Rauchtest der Version 1 in lauf-69/LAUF.log):
- Version 1 hielt den Abstand ueber den Schwerpunkt X von phi^2 auf x > 0 fest. Die Zwangskraft wirkt mit dem Hebel
  (x - X) auf jeden Punkt bis an den Boxrand.
- Bei gleichphasigen Paaren (Anziehung) ist dieser Zwang schlecht gestellt:
  - Das Paar kann verschmelzen und den Schwerpunkt mit wenig, weit aussen geparkter Ladung halten.
  - Im Aussenfeld wirkt die Zwangskraft dann wie ein abfallendes lineares Potential. Das Aussenfeld waechst exponentiell,
    bis die Zahlen ueberlaufen.
- Der Rauchtest (tau = 60) zeigt schon den Anfang:
  - E_int(0) liegt bei d = 3 bis 8 bei -0,44 bis -0,31, fast der ganzen Verschmelzungstiefe 0,448.
  - omega betraegt dort 0,72, das omega des verschmolzenen Balls.
  - Die Konvergenz wird mit d schlechter, bis 0,26 bei d = 8.
  - Nur d = 10 und 12 (schwache Anziehung) blieben unberuehrt.
  - Rauchtestzahlen gelten nicht als Ergebnis; hier zeigen sie nur den Mechanismus.
- Zweiter Weg zum Ueberlauf: Gegenphasige Anfangsfelder bei kleinem d loeschen sich fast aus. Bei fester Ladung ist dann
  omega = Q/(2N) bis etwa 8; fuer omega > 1 ist das Vakuum im Relaxationsfluss instabil.
- Eine kleinere Schrittweite hilft nicht: dt sqrt(4/dx^2) = 1 liegt im stabilen Bereich des Verlet-Schemas. Instabil ist
  der Zwang selbst.

**Aenderung** (nur test2 samt Hilfsfunktion interpolieren, Zeilen 444 bis 671 von tests1d_r3.py; dazu die
Versionszeilen 4 bis 7 im Kopf):
- **Punktzwang in der Mitte statt Schwerpunktzwang:** symmetrisch phi(0) = c, antisymmetrisch phi(+-dx) = +-s dx.
  - Er wirkt nur an ein oder zwei Gitterpunkten.
  - Weit geparkte Ladung hilft nicht mehr: Zwischen den Baellen verknuepft die lineare Gleichung den Wert in der Mitte
    fest mit dem Abstand.
- **Belegung der Kurve:**
  - c und s kommen aus der Summe zweier Baelle bei d_start = 1,5 bis 13, das sind 17 Werte je Phase.
  - Dazu drei symmetrische Laeufe mit c = 0,95 / 1,05 / 1,2, ueber dem Scheitel 0,906 des verschmolzenen Balls; sie
    belegen die Seite links vom Minimum.
  - Dazu ein freier symmetrischer Lauf, der zum verschmolzenen Ball relaxiert: das Minimum.
  - Nullpunkt wie bisher: dasselbe Paar bei d = 40.
- **Anfangsfeld** auf N = 2 N1 normiert, also omega = omega_1 = 0,837 am Start.
- **Kein Abbruch mehr:**
  - Laeufe werden auf den letzten guten Stand eingefroren und als "ungebunden" gefuehrt, nicht gefittet, wenn sie nicht
    endlich bleiben, ihr Feld bei |x| > 80 ueber 1e-6 steigt oder omega 0,999 erreicht.
  - Erwartet ist das fuer gegenphasige Laeufe mit kleinem d_start. Dort liegt omega bei fester Ladung ueber 1; so ein
    Zustand ist nicht gebunden.
- **Auswertung:**
  - Gemessen wird d = 2X im Endzustand.
  - E_int an den 12 Sollabstaenden wird zwischen den gebundenen Laeufen linear interpoliert.
  - Morse, Asymptotik und Minimum werden auf allen gebundenen Punkten gefittet.
- **Unveraendert:** Funktional bei fester Ladung, Spiegelsymmetrie, gedaempfte Verlet-Relaxation (gamma = 1, tau = 600),
  Gitter grob und fein, Vorhersagen (Abschnitt 5).
- **Folge fuer die Deutung:**
  - Gleichphasig ist der Abstand jetzt ueber den Wert in der Mitte festgelegt. Links vom Minimum liegen hochgezogene
    verschmolzene Baelle statt zusammengedrueckter.
  - Gegenphasig ist die Kurve bei kleinem d nur so weit belegt, wie die Laeufe gebunden bleiben.

**Pruefung:** Ich habe nicht lokal gerechnet.
- Die Freigabe fuer lokale Probelaeufe kam als Weitergabe durch die Leitung. Das Verbot lokaler Interpreter steht aber in
  Finns CLAUDE.md, und eine weitergegebene Zustimmung reicht mir nicht, um davon abzuweichen.
- Geprueft habe ich durch Lesen:
  - diff gegen Version 1: nur test2, die neue Hilfsfunktion interpolieren und die Versionszeilen sind anders.
  - Die Schrittweite liegt im stabilen Bereich.
  - Den Ausweg ueber weit geparkte Ladung gibt es nicht mehr.
  - Abbrechen kann t2 nur noch durch einen echten Programmfehler.
- Deshalb bitte zuerst den Rauchtest unten.

**Nachlauf nur t2:** Die neue tests1d_r3.py nach /home/fmh/fmhc-physics-remote/runde3-tests1d/ kopieren; die Ergebnisse von
t1 und t3 bis t6 bleiben gueltig.

1. Rauchtest (etwa 10 s Rechnung, mit Start unter 1 min):

   ```
   cd /home/fmh/fmhc-physics-remote/runde3-tests1d && bash /home/fmh/fmhc-physics-remote/kleintests/kleintest.sh p4000a r3t1d-t2v2-rauch tests1d_r3.py t2 --kurz --out rauchtest-v2 --profil ausgabe/profile_r3.pt
   ```

2. Hauptlauf:

   ```
   cd /home/fmh/fmhc-physics-remote/runde3-tests1d && bash /home/fmh/fmhc-physics-remote/kleintests/kleintest.sh p4000a r3t1d-t2v2 tests1d_r3.py t2 --out ausgabe
   ```

- **Laufzeit (Schaetzung):** 1,5 bis 2 min auf der P4000, sicher unter 5 min. Grundlage: 2,3 ms je Schritt im Rauchtest
  von Version 1 (26 Laeufe) und 36000 Schritte grob und fein; die 40 Laeufe der Version 2 aendern daran wenig, weil die
  Zahl der GPU-Aufrufe zaehlt.
- **Abbruchregel:** Hauptlauf nicht starten, wenn im Rauchtest symmetrische Laeufe oder eine Referenz d = 40 als
  "ungebunden" erscheinen. Gegenphasige ungebundene Laeufe bei kleinem d_start sind erwartet.

## Einfach gesagt

Wir pruefen am Rechner fuenf Chemie-Vergleiche fuer Q-Baelle, die kleinen Feldklumpen unseres Modells. Beim Test zur
"Elektronegativitaet" erwarten wir, dass Ladung zwischen einem kleinen und einem grossen Ball hin- und herschwappt wie
Wasser zwischen zwei Becken, aber nicht dauerhaft in eine Richtung fliesst; welche Seite im Mittel mehr hat, haengt vom
Takt beim Start ab. Zwei Baelle bilden nach unserer Vorhersage kein Molekuel mit festem Abstand: Entweder verschmelzen sie
zu einem Ball, oder sie stossen sich ab. Die Idee mit der "Rumpfgeschwindigkeit" laesst sich in unserem Modell gar nicht
pruefen, weil ein duennes Hintergrundmedium darin von selbst zu Klumpen zerfaellt; mit einem zweiten Feld als Medium
ginge es. Gerechnet ist noch nichts; alles zusammen soll etwa zehn Minuten auf einer Grafikkarte dauern.

Ende der Bearbeitung: 2026-09-30 02:13:37 CEST (gemessen mit date).
Version 2 (nur test2): Beginn 2026-09-30 02:50:57 CEST, Ende 2026-09-30 02:58:01 CEST (gemessen mit date).
