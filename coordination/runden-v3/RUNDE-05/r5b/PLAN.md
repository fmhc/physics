# R5-B: 1D-Einzelball, Laufplan und Vorhersagen (Bio 3, 36, 38, 20/37, 45, 22 und Chemie 10)

Bearbeiter: Agent R5-B (Anthropic, Opus). Auftrag: ../AUFTRAG-R5.md, Abschnitt R5-B. Beginn 2026-09-30 01:43:45 CEST
(gemessen), Ende in der letzten Zeile. Status: Code geschrieben, **ungetestet, nicht gerechnet**. Explorativ.

## Kurzfassung

- **Code:** r5b.py, PyTorch, float64 bzw. complex128, `--geraet cuda|cpu`. Auf der CPU laeuft genau ein Thread
  (kleintest.sh setzt CPUQuota 100 %).
  - Ein Unterbefehl je Idee: `fuettern`, `photo`, `winterschlaf`, `rauschen`, `pumpe`, `mi`. Dazu `rauch`: alle sechs mit
    Laufzeit x 0,05; er druckt je Befehl die Hochrechnung fuer die volle Laenge.
  - Jeder Befehl rechnet grob (dx = 0,1, dt = 0,05) und fein (dx/2, dt/2) und prueft L3 im Code.
  - Er schreibt `<befehl>_bericht.txt`, `<befehl>_ergebnis.json`, `<befehl>_zeitreihen.pt` und `<befehl>_zeiten.txt`
    nach `--out`. Ein Fehler in einem Befehl bricht beim Rauchtest die anderen nicht ab.
- **Aus RUNDE-02/tests1d/tests1d.py unveraendert:** Gitter [-150, 150], dx = 0,1, dt = 0,05; Daempfungsschicht ab
  |x| = 110 (quadratisch, sigma0 = 1); Velocity-Verlet-Schritt und Kraft; Anker-Formeln; Auswerte-Hilfen (entfalten,
  breite_s, spektrum, l3); Wellenpaket.
- **Geaendert, mit Grund:**
  - Profile kommen direkt aus dem analytischen 1D-Anker statt aus dem Schiessen. Runde 2 hat beide auf dem Gitter
    verglichen (K0: 1,5e-10), und ohne Brechungsfeld ist der Anker exakt. Das spart 80 s je Aufruf.
  - Der Verlet-Schritt kann zusaetzlich drei Dinge, jeweils nur im genannten Befehl:
    - gleichmaessige Daempfung gamma je Lauf (pumpe)
    - Antrieb F(x, t) je Lauf (photo, pumpe)
    - periodischer Rand ohne Daempfungsschicht (mi, weil ein homogenes Kondensat keinen absorbierenden Rand vertraegt)
- **Rechnen:** nicht selbst. Die Leitung startet ueber kleintest.sh (Abschnitt 2).
- **Kernvorhersagen (Abschnitt 4):**
  - Ein Ball "frisst" linear nur oberhalb nu = 2 omega + 1: Er schluckt ein Teilchen und stoesst ein Antiteilchen aus.
    Grosse Baelle fressen viel (C_Q ~ 5 %), kleine fast nichts. Antiteilchen-Wellen lassen ihn schrumpfen.
  - Die Stossantwort schwingt an der Kontinuumskante 1 - omega.
  - Kleine Baelle schmelzen im Rauschen zuerst.
  - Mit Pumpe und Daempfung entsteht ab h_min = gamma Q*/(2F) = 3,3e-3 ein stabiler, eingerasteter Ball. Ohne Pumpe
    zerfaellt er wie exp(-gamma t).
  - Das Kondensat verklumpt genau fuer S0 < 2/3, mit der linearen Wellenlaenge. Die "Uebersaettigung" ist also
    umgekehrt: Instabil ist die duenne Seite.

## 1. Aufbau je Befehl (vor dem Lauf festgelegt)

Modell wie im Auftrag. rho = 2 Im(psi conj psi_t), e = |psi_t|^2 + |psi_x|^2 + U, j = -2 Im(psi conj psi_x). Alle Baelle
ruhen bei x = 0 mit psi = f(x), psi_t = -i omega f. Messfenster |x| < 20. Endwerte sind das Mittel der letzten 10 % der
Proben. omega kommt aus dem Phasenzuwachs am Maximum von |psi|^2 im Endviertel.

**Hintergruende und Stabilitaet (Auftrag: nur linear stabile Dichten):**
- Homogen gilt omega_bg^2 = 1 - 2 S + 1,5 S^2.
- Linearisiert: (k^2 + M^2 - Om^2)(k^2 - Om^2) = 4 omega^2 Om^2 mit M^2 = 2 U''(S) S = 2 S (3 S - 2).
  - Instabil genau fuer S < 2/3, im Band k^2 < 2 S (2 - 3 S).
  - Fuer kleines S ist die Rate hoechstens etwa S.
- Welche Hintergruende auftreten:
  - fuettern, winterschlaf, rauschen: Vakuum (S = 0), stabil.
  - photo: Die Dauerwelle hat S = eps^2 = 0,0025.
    - MI-Rate im Ruhesystem der Welle etwa 0,0025, im Labor durch nu geteilt, also unter 1e-3.
    - Ueber T = 360 waechst sie hoechstens um den Faktor e^0,36. Vernachlaessigbar.
  - pumpe:
    - Der getriebene Hintergrund hat S_bg = |h/(1 - Om^2 - i gamma Om)|^2 <= 1,9e-3.
    - Die MI-Rate von hoechstens 1,9e-3 liegt unter der Daempfung gamma/2 = 5e-3. Dadurch ist der Hintergrund stabil.
    - Im Lauf ohne Daempfung ist S_bg = 4,8e-4; das gibt ueber T = 600 den Faktor e^0,29.
  - rauschen:
    - Das Rauschen liegt im Band 0,5 <= |k| <= 2,5, fast ganz ausserhalb des MI-Bands k < 0,58 (bei S = 0,1).
    - Bei eps >= 0,3 kann es trotzdem selbst verklumpen. Das misst die Gegenprobe "nur Rauschen".
  - mi: Hier ist die Instabilitaet die Messgroesse (Ausnahme laut Auftrag).

**fuettern (Bio 3).** 49 Laeufe, T = 250, Messung alle 0,5.
- Baelle omega^2 = 0,55 / 0,70 / 0,90. Schwellen 2 omega + 1 = 2,483 / 2,673 / 2,897.
- Paket wie Runde 2: eps exp(-(x + 55)^2 / 128) exp(i k (x + 55)), nach rechts.
  - nu = 1,6 / 2,2 / 2,6 / 2,8 / 3,0; eps = 0,01 und 0,05.
  - eps = 0,05 bleibt unter der Solitonschwelle: Flaeche eps sigma sqrt(2 pi) = 1,0 < pi/2.
- Antiteilchen-Pakete (komplex konjugiert, eps = 0,01) auf 0,55 und 0,70 bei nu = 2,2 und 3,0.
- Laeufe: Paket allein (12) und Ball allein (3).
- Kenngroessen:
  - C_Q = [Q_Fenster(Ball+Paket) - Q_Fenster(Ball) - Q_Fenster(Paket)] / |Q_Paket|
  - C_E, dasselbe mit der Energie
  - dE/dQ gegen omega
  - d omega gegen (d omega/dQ)_Anker x dQ
  - Born-Schaetzung je Lauf (Kopplung U''(S) S, im Code)
  - Sprungfaktor an der Schwelle; C_Q(0,05)/C_Q(0,01)

**photo (Bio 36).** 33 Laeufe, T = 360, Messung alle 0,5.
- Quelle F0 exp(-(x + 60)^2 / 0,18) exp(-i nu t), Anlauf sin^2 ueber 30.
  - F0 ist so gewaehlt, dass sie eine Welle mit Amplitude 0,05 abstrahlt; die linke Haelfte laeuft in die
    Daempfungsschicht.
  - Der Einstrom wird im Lauf "Welle allein" bei x = -20 gemessen, mit Sollwert 2 k eps^2.
- nu je Ball:
  - 0,55: 2,0 / 2,3 / 2,45 / 2,52 / 2,6 / 2,8 / 3,1
  - 0,70: 2,0 / 2,3 / 2,6 / 2,64 / 2,71 / 2,8 / 3,1
  - 0,90: 3,1
- Dazu drei Laeufe auf 0,55: eps = 0,025 bei 2,3 und 2,8, Antiteilchen-Welle bei 2,3. Welle allein (12), Ball allein (3).
- Kenngroessen:
  - Wachstum G = Steigung von Q(Ball+Welle) - Q(Ball) - Q(Welle) in [T/2, T]
  - Gamma = G/|Einstrom| (Fangquote)
  - G_E/G_Q gegen omega
  - d omega/dt gegen (d omega/dQ) G

**winterschlaf (Bio 38).** 19 Laeufe, T = 600, Messung alle 0,5.
- Baelle omega^2 = 0,55 / 0,62 / 0,70 / 0,78 / 0,85 / 0,90.
- Fester Stoss psi -> psi + A exp(-x^2/2) mit A = 0,01 und 0,03, fuer alle Baelle gleich.
- Dazu der relative Stoss aus Runde 2 (x 1,01) bei 0,70. Er ist eine Reproduktionsprobe: Runde 2 fand die Spitze 0,1702.
- Alles wird als Differenz zum ungestossenen Ball gemessen.
- Kenngroessen:
  - Hauptfrequenz der Breite (FFT ab T/8, Aufloesung 0,012) gegen die Kante 1 - omega
  - Antwort = Spannweite der Breite in [T/4, T] / Breite / A
  - Abklingfaktor = rms spaet / rms frueh
  - Rest = Anregungsenergie am Ende (E - E_Anker(Q), Ball abgezogen) / Stossenergie

**rauschen (Bio 20/37).** 51 Laeufe, T = 220, Messung alle 0,5.
- Baelle omega^2 = 0,55 / 0,70 / 0,90 (Q = 3,81 / 2,44 / 1,29).
- Rauschen:
  - Zufallsfeld aus ebenen Wellen 0,5 <= |k| <= 2,5, Gewicht 1/sqrt(nu); Teilchen und Antiteilchen, beide Richtungen.
  - |x| < 90, weicher Rand bis 100.
  - RMS eps = 0,025 / 0,05 / 0,1 / 0,2 / 0,3 / 0,4; Saaten 11 und 12.
  - Auf jedem Gitter und Geraet ist es dieselbe Funktion.
- Laeufe: Rauschen allein (12), Ball allein (3).
- Ballverfolgung per Mean-shift (Schwerpunkt von |psi|^2 in +-4).
- Kenngroessen:
  - R_Q = Ladung in +-8 um die Mitte am Ende / Anfang
  - R_S = Spitzenwert Ende / Anfang
  - "lebt" = R_Q >= 0,5 und R_S >= 0,5
  - Schmelzschwelle eps_c: Mittel ueber die Saaten, geometrisch interpoliert bei R_Q = 0,5
  - Scheinball im Lauf "nur Rauschen"

**pumpe (Bio 45).** 20 Laeufe, T = 600, Messung alle 0,5.
- Gleichung psi_tt = psi_xx - U' psi - gamma psi_t + h g(x) exp(-i Omega_d t).
  - Omega_d^2 = 0,70, gamma = 0,01; g = 1 fuer |x| < 90, weich bis 100.
  - Start: Ball plus stationaerer Hintergrund h/(1 - Omega_d^2 - i gamma Omega_d).
- Schwelle aus der Ladungsbilanz dQ/dt = -gamma Q - 2 h F sin(theta) mit F = Int f dx = 3,70:
  h_min = gamma Q*/(2F) = 3,30e-3 (im Code nachgerechnet).
- Laeufe:
  - Ball 0,70 bei h/h_min = 0 / 0,5 / 0,8 / 1,25 / 2 / 4
  - Startbaelle 0,55 / 0,60 / 0,80 / 0,90 bei 2 h_min, und 0,60 / 0,80 bei 0,5 h_min
  - Treiber allein (5)
  - ohne Daempfung: Ball mit Treiber 2 h_min und Treiber allein
  - freier Ball
- "stabil dissipativ": gamma > 0 und im letzten Viertel
  - Q_Ende >= 0,5 Q*
  - |omega - Omega_d| <= 0,005
  - |dQ/dt| <= 0,01 gamma Q

**mi (Bio 22, Chemie 10).** 18 Laeufe, periodische Box L = 200 (2000 bzw. 4000 Punkte), T = 400, Messung alle 1,0.
- Kondensat sqrt(S0) (1 + delta(x)) exp(-i omega_bg t).
  - S0 = 0,15 / 0,35 / 0,55 / 0,63 (instabil) und 0,72 / 0,85 (stabil).
  - delta ist bandbegrenztes Rauschen (|k| <= 1,5) mit RMS 1e-6, Saaten 21 und 22.
- Dazu delta = 1e-3 bei 0,35 und 0,63.
- Dazu metastabile Probe (Hypothese "Kavitation"): volle Delle Breite 2 und 8 bei 0,72 und 0,85.
- Kenngroessen:
  - t_lin: rms(dS) = 0,01 S0
  - k_dom: Spitze des Modenspektrums bei t_lin
  - gemessene Rate aus rms und je Mode gegen die Theoriekurve
  - t_klumpen: Kontrast (S_max - S_min)/S0 >= 1
  - Klumpenzahl am Ende
  - Leerlaenge (S < S0/2) am Anfang, in der Mitte und am Ende
  - Q- und E-Drift

## 2. Aufrufe (Leitung, auf der .69)

Remote-Ordner /home/fmh/fmhc-physics-remote/runde5-r5b/ mit r5b.py darin. Das Programm braucht nur torch. Es schreibt nur
nach `--out`; die Pfade stehen absolut.

**Rauchtest**, zuerst und am besten auf beiden Geraetearten, weil er die echten Teilzeiten liefert:

```
cd /home/fmh/fmhc-physics-remote/runde5-r5b && bash /home/fmh/fmhc-physics-remote/kleintests/kleintest.sh p4000a r5b-rauch r5b.py rauch --geraet cuda --out /home/fmh/fmhc-physics-remote/runde5-r5b/rauch-cuda
cd /home/fmh/fmhc-physics-remote/runde5-r5b && bash /home/fmh/fmhc-physics-remote/kleintests/kleintest.sh cpu r5b-rauchcpu r5b.py rauch --geraet cpu --out /home/fmh/fmhc-physics-remote/runde5-r5b/rauch-cpu
```

**Hauptlaeufe**, ein Aufruf je Idee, nur nach Rauchtest mit rc = 0. Die Spur ist frei waehlbar: `--geraet cuda` auf
p4000a/p4000b, `--geraet cpu` auf cpu/cpu2. Vorschlag nach Laufzeit:

```
cd /home/fmh/fmhc-physics-remote/runde5-r5b && bash /home/fmh/fmhc-physics-remote/kleintests/kleintest.sh p4000a r5b-fuettern r5b.py fuettern --geraet cuda --out /home/fmh/fmhc-physics-remote/runde5-r5b/fuettern
cd /home/fmh/fmhc-physics-remote/runde5-r5b && bash /home/fmh/fmhc-physics-remote/kleintests/kleintest.sh p4000a r5b-photo r5b.py photo --geraet cuda --out /home/fmh/fmhc-physics-remote/runde5-r5b/photo
cd /home/fmh/fmhc-physics-remote/runde5-r5b && bash /home/fmh/fmhc-physics-remote/kleintests/kleintest.sh p4000a r5b-rauschen r5b.py rauschen --geraet cuda --out /home/fmh/fmhc-physics-remote/runde5-r5b/rauschen
cd /home/fmh/fmhc-physics-remote/runde5-r5b && bash /home/fmh/fmhc-physics-remote/kleintests/kleintest.sh cpu r5b-mi r5b.py mi --geraet cpu --out /home/fmh/fmhc-physics-remote/runde5-r5b/mi
cd /home/fmh/fmhc-physics-remote/runde5-r5b && bash /home/fmh/fmhc-physics-remote/kleintests/kleintest.sh cpu2 r5b-winter r5b.py winterschlaf --geraet cpu --out /home/fmh/fmhc-physics-remote/runde5-r5b/winterschlaf
cd /home/fmh/fmhc-physics-remote/runde5-r5b && bash /home/fmh/fmhc-physics-remote/kleintests/kleintest.sh cpu r5b-pumpe r5b.py pumpe --geraet cpu --out /home/fmh/fmhc-physics-remote/runde5-r5b/pumpe
```

- **Regel:** Liegt die Hochrechnung aus `rauch-cpu/rauch_zeiten.txt` fuer einen Befehl ueber 9 min, diesen auf eine
  P4000-Spur legen. Auf der GPU liegt jeder Befehl nach Schaetzung unter 1,5 min.
- Die Zahlen des Rauchtests gelten nicht, denn die Laeufe sind dort zu kurz: Wellen erreichen den Ball zum Teil noch
  nicht.

## 3. Erwartete Laufzeit (Schaetzung, nicht gemessen)

**Grundlage:**
- Runde 2 auf der P4000 brauchte 1,0 bis 1,4 ms je Verlet-Schritt bei bis zu 26 x 6001 Punkten (begrenzt durch
  Kernelstarts).
- Groessere Stapel sind durch den Speicher begrenzt, geschaetzt etwa 2 ms bei 300 000 komplexen Punkten.
- CPU, ein Kern, etwa 30 elementweise Operationen je Schritt: 40 bis 90 ns je Punkt und Schritt. Die Schaetzung ist um
  etwa den Faktor 2 unsicher, weil der CPU-Typ der .69 hier unbekannt ist.

| Befehl | Laeufe x Punkte (fein) | Schritte grob + fein | P4000 | CPU, 1 Kern |
|---|---|---|---|---|
| rauch (alle, x 0,05) | wie unten | 5 % | 0,5 bis 1 min | 1 bis 2 min |
| fuettern | 49 x 6001 | 5000 + 10000 | 0,5 bis 1 min | 2,7 bis 6,1 min |
| photo | 33 x 6001 | 7200 + 14400 | 0,5 bis 1 min | 2,6 bis 5,9 min |
| winterschlaf | 19 x 6001 | 12000 + 24000 | 0,8 bis 1,2 min | 2,5 bis 5,7 min |
| rauschen | 51 x 6001 | 4400 + 8800 | 0,5 bis 1 min | 2,6 bis 6,1 min |
| pumpe | 20 x 6001 | 12000 + 24000 | 0,8 bis 1,2 min | 2,7 bis 6,2 min |
| mi | 18 x 4000 (periodisch) | 8000 + 16000 | 0,5 bis 0,8 min | 1,1 bis 2,5 min |

- Speicher: alle Felder unter 0,1 GB; auf der GPU mit CUDA-Kontext unter 0,6 GB. Der Code deckelt den Torch-Speicher auf
  1,5 GB und meldet den Hoechststand.
- mi speichert 41 Schnappschuesse von S (float32), zusammen etwa 18 MB.

## 4. Vorhersagen (vor dem Rechnen, von Hand)

### Bio 3, Fuettern

**Papierbild:** Linearisiert um den Ball koppelt eine einfallende Welle nu an den Partnerkanal 2 omega - nu. Die
Kopplung ist V2 = U''(S) S. Der Partnerkanal ist offen, wenn |2 omega - nu| > 1, fuer Teilchen also bei nu > 2 omega + 1.
- Erhalten bleibt E - omega Q; darum gilt fuer die Quantenzahlen N_ein = N_+ + N_-.
- Jedes umgewandelte Teilchen verlaesst den Ball als Antiteilchen (Energie nu - 2 omega). Der Ball gewinnt dabei genau
  2 Ladungen und 2 omega Energie.
- Unter der Schwelle gibt es in linearer Ordnung keinen Einfang.
- Born-Schaetzung P = |V2^(k_ein -+ k_aus)|^2 / (4 k_ein k_aus). Die Fouriertransformierte ist von Hand aus den Polen des
  Profils abgeschaetzt; der Code rechnet sie numerisch nach.

**Vorhersagen:**

| Ball | C_Q ueber der Schwelle (Born, Faktor 3 unsicher) | unter der Schwelle, eps = 0,01 |
|---|---|---|
| 0,55 | 2,6: 0,07; 2,8: 0,05; 3,0: 0,04 | < 1e-3 |
| 0,70 | 2,8: 1,3e-3; 3,0: 9e-4 | < 1e-3, ausser nahe nu ~ 2,3 (Runde-2-Spitze, dort L3 offen) |
| 0,90 | 3,0: ~1e-8 (praktisch 0) | < 1e-4 |

- **V-F1 (Sprung):** Fuer 0,55 liegt C_Q beim ersten nu ueber der Schwelle mindestens 5-mal ueber dem groessten |C_Q|
  darunter. Fuer 0,70 ebenso, falls die Runde-2-Spitze bei 2,2 unter 3e-4 liegt. Fuer 0,90 gibt es keinen Sprung, der
  Kanal ist zu schwach gekoppelt: Kleine Baelle fressen nicht.
- **V-F2 (linear ueber der Schwelle):** C_Q(0,05)/C_Q(0,01) liegt zwischen 0,7 und 1,4 bei 0,55 fuer nu = 2,6 / 2,8 / 3,0.
- **V-F3 (nichtlinear darunter):** Wo C_Q(0,05) > 1e-4 und nu unter der Schwelle liegt, betraegt das Verhaeltnis
  C_Q(0,05)/C_Q(0,01) 10 bis 40 (eps^2-Gesetz, Zwei-Quanten-Einfang). Ist C_Q(0,05) ueberall < 1e-4, heisst das: kein
  messbarer nichtlinearer Einfang.
- **V-F4 (erster Hauptsatz):** Wo |C_Q| >= 1e-3, ist dE/dQ = omega auf 10 % (0,742 / 0,837). d omega folgt
  (d omega/dQ) dQ mit -0,036 / -0,101 / -0,078 auf 30 %, sofern |d omega| > 1e-4.
- **V-F5 (Vorzeichenprobe):** Antiteilchen-Pakete lassen den Ball schrumpfen (Q-Ball-Superradianz):
  - 0,55: C_Q(2,2) ~ -0,024, C_Q(3,0) ~ -0,015
  - 0,70: C_Q(2,2) ~ -4e-4, C_Q(3,0) ~ -2e-4

**Gegenprobe:**
- 0,90 ueber seiner Schwelle (Effekt muss verschwinden)
- alle Laeufe unter der Schwelle bei eps = 0,01
- Paket allein und Ball allein (abgezogen)

### Bio 36, Photosynthese

Dasselbe Bild mit scharfer Frequenz: Gamma(nu) ist die Fangquote des Einstroms, G = Gamma x 2 k eps^2.
- **V-P1:** Gamma < 1e-3 fuer alle nu unter der Schwelle: 0,55 bei 2,0 / 2,3 / 2,45; 0,70 bis 2,64.
- **V-P2:** Gamma springt zwischen 2,45 und 2,52 (0,55) bzw. 2,64 und 2,71 (0,70), jeweils mindestens um den Faktor 5.
  Die Hoehe folgt der Born-Schaetzung auf einen Faktor 3:
  - 0,55: 2,52: bis 0,09, nahe der Schwelle eher kleiner; 2,6: 0,07; 2,8: 0,05; 3,1: 0,04
  - 0,70: 2,71: 1,6e-3; 2,8: 1,3e-3; 3,1: 8e-4
  - 0,90 bei 3,1: < 1e-5
- **V-P3:** Ueber der Schwelle gleiches Gamma bei eps = 0,025 und 0,05 (auf 30 %).
- **V-P4:** G_E/G_Q = omega auf 10 %.
- **V-P5:** Die Antiteilchen-Welle bei 2,3 auf 0,55 gibt Gamma ~ -0,023: Der Ball schrumpft.
- **V-P6:** Die Wachstumsraten sind klein, "Photosynthese" bleibt langsam.
  - 0,55 bei 2,6: G ~ 8e-4 je Zeiteinheit, also etwa 4 % der Ladung in [T/2, T].
  - Der Ball waechst dabei nicht beschleunigt (Rueckkopplung ueber omega < 1 %).

**Gegenprobe:**
- 0,90 bei 3,1 (Effekt muss verschwinden)
- Welle allein (Einstrom 2 k eps^2 auf 5 %; sonst ist die Quelle falsch normiert)
- Ball allein

### Bio 38, Winterschlaf

**Papierbild:** Ein 1D-Ball hat in der Luecke 0 < Om < 1 - omega hoechstens eine schwache innere Mode. Runde 2 fand die
Stossantwort knapp oberhalb der Kante: 0,1702 bei 0,70 (Kante 0,1633), 0,2615 bei 0,55 (Kante 0,2584). Die innere Uhr
omega tickt nahe der duennen Wand am langsamsten (0,74 gegen 0,95). Die Antwortfrequenz 1 - omega ist dort aber am
hoechsten.

- **V-W1:** Die Hauptfrequenz liegt bei allen sechs Baellen zwischen 0,9 und 1,15 x (1 - omega):
  0,258 / 0,213 / 0,163 / 0,117 / 0,078 / 0,051.
  - Eine Spitze deutlich unter der Kante (< 0,9 x Kante, L3 bestanden) waere eine echte innere Mode. Das waere ein Befund.
  - Der relative Stoss bei 0,70 reproduziert 0,170 +- 0,012.
- **V-W2:** Die relative Antwort je A steigt mit omega^2 (in mindestens 4 von 5 Schritten). Das Verhaeltnis 0,90/0,55
  ist mindestens 2.
  - Grund: f(0) = 0,83 gegen 0,33, weichere Luecke.
  - Stoerungen "perlen" also an grossen Baellen besser ab, im Sinne kleiner relativer Antwort.
- **V-W3 (unsicher):** Der Rest an Anregungsenergie am Ende liegt bei allen unter 50 % der Stossenergie. Er steigt mit
  omega^2, weil eine kleinere Luecke langsamer abstrahlt.
- **V-W4:** Die Antwort ist linear: Antwort je A bei A = 0,01 und 0,03 gleich auf 20 %.

**Gegenprobe:** Differenz zum ungestossenen Ball (der numerische Grundatmer faellt heraus); A-Verdopplung bzw.
-Verdreifachung.

**Was "Winterschlaf bestaetigt" heisst (vorab):** Antwort und Rest sind beide bei 0,55 am kleinsten und steigen mit
omega^2 (mindestens 4 von 5 Schritten), in beiden Stufen.

**1D-Grenze:** Die "duenne Wand" ist in 1D kein echter Duenne-Wand-Grenzfall; es gibt kein Q_min und keinen
Oberflaechenterm. Die kleinste sinnvolle Form fuer die Wand-Aussage ist die radiale 3D-Zeitentwicklung (Paket R5-A,
Bio 4) mit demselben Stoss.

### Bio 20/37, Rauschen und Schmelzen

**Papierbild:**
- Im linearen Regime ist der Ball fuer Wellen unter der Schwelle durchsichtig. Kleine Baelle sind fast NLS-Solitonen,
  also fast integrabel. Rauschen laeuft deshalb meist durch.
- Schmelzen braucht nichtlineare Staerke: Rausch-Amplitude vergleichbar mit der Ballamplitude f(0) = 0,83 / 0,61 / 0,33.
- Die Antiteilchen-Anteile ziehen ueber Superradianz langsam Ladung ab. Das wirkt nur bei grossen Baellen merklich.

**Vorhersagen:**
- **V-R1:** Alle drei ueberleben eps <= 0,1 (R_Q >= 0,9).
- **V-R2 (Hauptaussage, kann scheitern):** Die Schmelzschwellen sind nach Q geordnet: eps_c(0,55) > eps_c(0,70) >
  eps_c(0,90). Schaetzung:
  - eps_c(0,90) in [0,07; 0,25]
  - eps_c(0,70) in [0,15; 0,4]
  - eps_c(0,55) >= 0,25, moeglicherweise kein Schmelzen bis 0,4
- **V-R3:** Die Schwelle skaliert eher mit f(0) als mit der Bindungsenergie Q - E = 0,443 / 0,143 / 0,022.
  - Das Verhaeltnis eps_c(0,70)/eps_c(0,90) liegt naeher bei 1,9 (f(0)) als bei 2,5 (Wurzel der Bindung).
  - Nur pruefbar, wenn beide Schwellen im Raster liegen.
- **V-R4 (unsicher):** Bei eps <= 0,1 ist das mittlere dQ/Q fuer 0,55 negativ (Abzug durch Antiteilchen) und waechst
  ~eps^2. Fuer 0,90 gibt es keinen systematischen Abzug.

**Gegenprobe:**
- Rauschen allein: Scheinball R_Q < 0,5 bei eps <= 0,2. Bei eps >= 0,3 darf das Rauschen selbst verklumpen; dann gilt die
  Schwelle dort nur mit Vermerk.
- Ball allein: R_Q = 1.

### Bio 45, angetriebener Ball

**Papierbild:** Relativistisches Gegenstueck zum getriebenen, gedaempften NLS-Soliton. Die Ladungs- und Phasenbilanz
ist ein gedaempftes, vorgespanntes Pendel fuer die Phase theta zum Treiber. Es gibt einen eingerasteten Zustand genau
fuer h >= h_min = gamma Q*/(2F) = 3,30e-3.

- **V-PU1:** Ohne Pumpe (h = 0) zerfaellt der Ball als exp(-gamma t). Gemessene Rate d ln Q/dt = -0,0100 auf 2 %. Das
  ist zugleich eine Codeprobe, denn dQ/dt = -gamma Q gilt exakt.
- **V-PU2:** Stabil dissipativ bei h/h_min = 1,25 / 2 / 4, nicht bei 0 / 0,5 / 0,8. Die Schwelle liegt zwischen 0,8
  und 1,25.
- **V-PU3 (Attraktor):** Bei 2 h_min enden die Startbaelle 0,55 / 0,60 / 0,70 / 0,80 bei gleichem Q_Ende (auf 2 %,
  nahe Q* = 2,44) und omega = Omega_d.
  - Das Einzugsgebiet schaetze ich mit dem Pendelkriterium |omega_0 - Omega_d| < 2 sqrt(2 h |d omega/dQ| F) = 0,14.
  - Der Startball 0,90 (Abstand 0,112) liegt am Rand. Vorhersage mit geringer Sicherheit: nicht eingefangen, er
    zerfaellt.
- **V-PU4:** Bei 0,5 h_min zerfallen die Startbaelle 0,60 und 0,80.
- **V-PU5:** Der Treiber allein bildet keine Struktur: S_max bleibt unter 10 x S_bg.
- **V-PU6:** Ohne Daempfung (gamma = 0, 2 h_min) bleibt der Ball erhalten, rastet aber nicht zu einem Attraktor ein
  (konservativ; Q schwingt).

**Gegenprobe:** h = 0 (muss zerfallen); Treiber allein (keine Struktur); gamma = 0 (kein Attraktor).

### Bio 22 und Chemie 10, Modulationsinstabilitaet und Uebersaettigung

Lineare Theorie aus Abschnitt 1, von Hand ausgewertet:

| S0 | k_max | lambda_max | g_max | t_lin (etwa 10,3/g) | t_klumpen (etwa t_lin + 3,9/g) |
|---|---|---|---|---|---|
| 0,15 | 0,464 | 13,5 | 0,136 | 76 | 105 |
| 0,35 | 0,529 | 11,9 | 0,239 | 43 | 59 |
| 0,55 | 0,412 | 15,2 | 0,162 | 64 | 88 |
| 0,63 | 0,257 | 24,5 | 0,060 | 172 | 237 |
| 0,72 / 0,85 | stabil | - | 0 | - | - |

- **V-M1 (Einsatz):** Verklumpung genau fuer S0 < 2/3: ja bei 0,15 / 0,35 / 0,55 / 0,63, nein bei 0,72 / 0,85 (Kontrast
  bleibt < 1e-3).
  - Die Chemie-Hypothese "oberhalb einer Dichte uebersaettigt" ist damit umgekehrt: Das duenne Kondensat ist spinodal
    instabil.
  - Zwischen 2/3 und 1 ist es nur metastabil. Dort ist der Druck omega^2 S - U negativ, -0,145 bei 0,72 und -0,108
    bei 0,85.
- **V-M2:** k_dom bei t_lin liegt innerhalb 2 Modenabstaenden (0,063) bei k_max.
- **V-M3:** Die gemessene Rate stimmt mit g_max auf 15 %; die Raten je Mode im Band auf 0,02.
- **V-M4:** Staerkeres Rauschen (1e-3) verklumpt frueher um ln(1000)/g: 29 (0,35) bzw. 115 (0,63).
- **V-M5:** Am Ende gibt es weniger Klumpen als L/lambda_max (17 / 15 / 13 / 8), weil sie verschmelzen.
- **V-M6 (Hypothese "Kavitation", geringe Sicherheit):**
  - Im metastabilen Bereich waechst eine volle Delle der Breite 8 zu einem Vakuumloch: Die Leerlaenge am Ende liegt
    mindestens 5 ueber dem Anfang.
  - Eine Delle der Breite 2 heilt: Leerlaenge am Ende < 0,5 x Anfang.
  - Kritische Breite etwa 2 sigma/|P| mit der Wandspannung sigma = 0,354: 5 (0,72) bzw. 6,5 (0,85).

**Gegenprobe:**
- stabile Dichten 0,72 / 0,85 mit demselben Rauschen (Effekt muss verschwinden)
- Q-Drift < 1e-10, denn Verlet erhaelt die Ladung im periodischen Kasten exakt

## 5. Latten (Vorschlag, die Leitung entscheidet)

| Latte | fuettern (3) | photo (36) | winterschlaf (38) | rauschen (20/37) | pumpe (45) | mi (22, C10) |
|---|---|---|---|---|---|---|
| L1 kann scheitern | ja: kein Sprung bei 0,55, oder dE/dQ != omega, oder Antiteilchen fuettern | ja: Gamma unter der Schwelle >= 1e-3 oder kein Sprung | ja: Spitze unter 0,9 x Kante; Trend falsch herum | ja: grosser Ball schmilzt vor kleinem | ja: Schwelle nicht zwischen 0,8 und 1,25 h_min; kein gemeinsamer Endzustand | ja: Verklumpung bei S0 > 2/3 oder k_dom ausserhalb 0,063 |
| L2 Gegenprobe | 0,90; unter der Schwelle; Paket/Ball allein | 0,90; Welle allein; Ball allein | Differenz zum ungestossenen Ball; zwei A | Rauschen allein; Ball allein | h = 0; Treiber allein; gamma = 0 | S0 = 0,72 / 0,85 |
| L3 Numerik | im Code: C_Q | im Code: Gamma | im Code: Omega, Antwort, Rest | im Code: R_Q und eps_c | im Code: Q_Ende/Q* | im Code: k_dom, g, t_klumpen |
| L4 schon bekannt | weitgehend: Solitosynthese (Griest, Kolb 1989); Q-Ball-Superradianz (Saffin, Xie, Zhou 2023) | wie fuettern | teilweise: innere Moden (Kivshar, Pelinovsky u. a. 1998) | teilweise: Solitonen im Rauschen; Integrabilitaet der NLS | ja: getriebene, gedaempfte NLS-Solitonen (Barashenkov, Smirnov 1996) | ja: Benjamin-Feir/Zakharov; Spinodale bei U'' = 0 |
| L5 Messbezug | nein | nein | nein | nein | nur Analogie: Kerr-Resonator-Solitonen (Lugiato-Lefever) | nur Analogie: Solitonenzuege im BEC durch MI (2017) |

Literatur aus dem Gedaechtnis, nicht nachgelesen. L3 halbiert dx und dt zugleich (wie Runde 2), also auch den
Zeitschritt.

## 6. Grenzen

- **Ungetestet:** Das Programm ist nie gelaufen, daher zuerst der Rauchtest. Wahrscheinlichste Fehlerstellen:
  - Tensorformen in den Messfunktionen
  - komplexe Typumwandlung (Python-complex mal float64-Tensor)
  - die Mean-shift-Verfolgung (rauschen)
  - die Schnappschuesse (mi)
- **Laptop-Pruefung ohne Interpreter:** Nur die Klammern sind gezaehlt (ausgeglichen). f-Strings, Typen und Formen sind
  von Hand gelesen.
- **Rohdaten:** Scheitert nur die Auswertung, schreibt der Befehl die Rohzeitreihen trotzdem nach
  `<befehl>_zeitreihen.pt` (Schluessel `roh_ohne_auswertung`). Die Rechnung muss dann nicht wiederholt werden.
- **mi, Dellen-Laeufe:** t_klumpen und k_dom sind dort nicht sinnvoll, weil der Kontrast schon bei t = 0 gross ist. Es
  zaehlt nur die Leerlaenge.
- **Pakete (fuettern):** Die Frequenzbreite liegt bei etwa 0,08. Laeufe knapp unter der Schwelle (0,70 bei 2,6; 0,90
  bei 2,8) enthalten daher einen kleinen Anteil ueber der Schwelle; photo prueft die Schwelle scharf.
- **Born-Zahlen:** Sie sind eine Groessenordnung; nahe der Schwelle ueberschaetzt Born (1/k_aus).
- **Runde-2-Spitze bei nu ~ 2,3 (0,70):** Sie ist noch ungeklaert. Moeglich ist eine quasigebundene Mode im
  Partnerkanal. Sie kann in fuettern bei 2,2 wieder auftauchen und den Sprung verdecken.
- **rauschen:**
  - Nahe der Schwelle ist der Ausgang chaotisch empfindlich. L3 kann dort je Lauf scheitern, obwohl die Schwelle
    stabil ist.
  - Zwei Saaten sind eine duenne Statistik.
- **pumpe:** Das Pendelbild ist adiabatisch. Fuer weit entfernte Startbaelle ist es nur eine Schaetzung.
- **mi:**
  - Die Zahlen zu Einsatz und Klumpenzahl gelten fuer L = 200 und T = 400.
  - Die Kavitationsprobe ist eine Hypothese ohne Rechnung.
- **Allgemein:** 1D, ein Kanal, explorativ. Nichts davon sagt direkt etwas ueber 3D.

## Einfach gesagt

Wir pruefen sechs Ideen, bei denen ein Q-Ball sich wie ein Lebewesen verhalten soll: fressen, Licht tanken, Winterschlaf
halten, Hitze ueberleben, von einer Pumpe am Leben gehalten werden, und ob ein gleichmaessiger Nebel von selbst zu
Baellen zerfaellt. Nach der Papierrechnung frisst ein Ball Wellen nur oberhalb einer bestimmten Frequenz. Dabei schluckt
er ein Teilchen und spuckt ein Antiteilchen aus; grosse Baelle fressen viel, kleine fast nichts. Mit Pumpe und Bremse
lebt ein Ball dauerhaft, aber nur, wenn die Pumpe stark genug ist; ohne Pumpe verloescht er langsam. Und der Nebel
zerfaellt nur, wenn er duenn genug ist, in Klumpen mit einem vorhersagbaren Abstand. Gerechnet ist noch nichts; das
erledigt die Leitung mit dem Programm auf der .69, jeder Teil in wenigen Minuten.

Beginn 2026-09-30 01:43:45 CEST, Ende 2026-09-30 02:24:26 CEST (beide gemessen mit date); 41 min von 90.
