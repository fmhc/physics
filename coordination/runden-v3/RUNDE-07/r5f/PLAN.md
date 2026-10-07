# R5F (Runde 7): Folge-Tests zu Tod, Fuettern und Kavitation aus Runde 5

Bearbeiter: Agent R5F (Anthropic, Opus). Auftrag: Karte R5F in ../../RUNDE-07.md. Beginn 2026-09-30 04:01:55 CEST
(gemessen), Ende in der letzten Zeile. Explorativ nach v3, keine formale Bestaetigung.

Status: Code geschrieben; lokaler Rauchtest bestanden (Laptop-CPU, 1 Faden, nice 19, timeout 120, rc = 0, 15,9 s;
Vorschau, kein Ergebnis). Auf der .69 ist nichts gerechnet.

## Kurzfassung

- **Dateien** (Remote-Ordner /home/fmh/fmhc-physics-remote/runde7-r5f/; die drei .py-Dateien dorthin kopieren):
  - r5f.py: neu, Unterbefehle `tod`, `fuettern`, `kavitation`, `rauch` (sha256 3a823515f9593b3f5b9d1493e098c89140cb864ce166b3851d03350c60d5173b)
  - r5a.py und r5b.py: unveraenderte Kopien aus RUNDE-05, werden importiert
    - r5a.py sha256 e51b4172d90615e55ba16ac5cc478e41a37bdfa5df65f44b8f76458c08cd843b
    - r5b.py sha256 11ae4d46b93a0bacac0cf8a68c61b877e02cd7943692df524f084e5f2fae1fac
  - lauf-lokal/: Rauchtest vom Laptop (nicht auswerten)
- **Uebernommen aus r5a** (3D radial): Schiessen `familie`/`fam_zeile`, `ball_radial` und `entwickeln_radial`
  (Verlet fuer chi = r psi, Schwamm ab r = 110, Abfluss -gamma psi_t bis t_stop), Auswertehilfen.
- **Uebernommen aus r5b** (1D): Anker-Ball, `stapel`, `entwickeln` (Schwamm oder periodisch), Messhilfen, `spektrum`,
  `rausch_basis`, `born_aq`.
- **Neu in r5f.py, in den Bausteinen nichts geaendert:**
  - eigene Messfunktionen mit mehr Spalten
  - `paket_sigma`: r5b.paket mit sigma und x0 als Argument
  - Delle mit Tiefe d (r5b.mi kannte nur d = 1)
  - Box-Konstanten von r5b werden je Befehl umgestellt und danach zurueckgesetzt: L_BOX/X_SPONGE fuer fuettern, M_L fuer
    kavitation
- **Technik:**
  - float64 bzw. complex128; `--geraet cuda|cpu`, CPU mit einem Faden
  - `--stufe grob|fein|beide`
  - Rohdaten nach jeder Stufe: `<name>_<stufe>_roh.pt`, noch vor der Auswertung
  - `--nur-auswertung` wertet vorhandene Rohdaten aus, auch L3, wenn grob und fein getrennt liefen
  - `kavitation --nur-vorhersage` druckt die Vorhersagetabelle aus den Anfangsfeldern
  - Budget 540 s: `tod` kuerzt die Zeitentwicklung selbst; die feine Stufe entfaellt, wenn die Restzeit nicht reicht
    (Faktor 3 bzw. 4,5 der groben Laufzeit)
- **Ausgaben je Aufruf:** `<name>_bericht.txt` (auch auf stdout), `<name>_ergebnis.json`, Rohdaten `.pt`.

## 1. Aufrufe (Leitung, auf der .69 ueber kleintest.sh)

Erst die Rauchtests. Beide drucken am Ende eine Hochrechnung fuer die Hauptaufrufe (Schritt = c0 + c1 B N). Liegt ein
Hauptaufruf ueber 9 min, nicht starten, sondern Spur wechseln (GPU) oder teilen (`--stufe`, `--s0`).

```
cd /home/fmh/fmhc-physics-remote/runde7-r5f && bash /home/fmh/fmhc-physics-remote/kleintests/kleintest.sh p4000a r5f-rauch r5f.py rauch --geraet cuda --out /home/fmh/fmhc-physics-remote/runde7-r5f/rauch-cuda
cd /home/fmh/fmhc-physics-remote/runde7-r5f && bash /home/fmh/fmhc-physics-remote/kleintests/kleintest.sh cpu r5f-rauchcpu r5f.py rauch --geraet cpu --out /home/fmh/fmhc-physics-remote/runde7-r5f/rauch-cpu
```

**(a) tod**, zwei CPU-Spuren parallel, danach die L3-Auswertung:

```
cd /home/fmh/fmhc-physics-remote/runde7-r5f && bash /home/fmh/fmhc-physics-remote/kleintests/kleintest.sh cpu r5f-tod-grob r5f.py tod --geraet cpu --stufe grob --T 4000 --out /home/fmh/fmhc-physics-remote/runde7-r5f/ausgabe-tod
cd /home/fmh/fmhc-physics-remote/runde7-r5f && bash /home/fmh/fmhc-physics-remote/kleintests/kleintest.sh cpu2 r5f-tod-fein r5f.py tod --geraet cpu --stufe fein --T 2000 --out /home/fmh/fmhc-physics-remote/runde7-r5f/ausgabe-tod
cd /home/fmh/fmhc-physics-remote/runde7-r5f && bash /home/fmh/fmhc-physics-remote/kleintests/kleintest.sh cpu3 r5f-tod-l3 r5f.py tod --geraet cpu --nur-auswertung --out /home/fmh/fmhc-physics-remote/runde7-r5f/ausgabe-tod
```

Statt der beiden CPU-Aufrufe geht auch ein Aufruf auf einer GPU mit beiden Stufen:
`tod --geraet cuda --T 3000 --out .../ausgabe-tod`.

**(b) fuettern**, nur GPU (auf der CPU ueber 10 min, siehe Abschnitt 2):

```
cd /home/fmh/fmhc-physics-remote/runde7-r5f && bash /home/fmh/fmhc-physics-remote/kleintests/kleintest.sh p4000a r5f-fu-mech r5f.py fuettern --teil mechanik --geraet cuda --out /home/fmh/fmhc-physics-remote/runde7-r5f/ausgabe-fuettern
cd /home/fmh/fmhc-physics-remote/runde7-r5f && bash /home/fmh/fmhc-physics-remote/kleintests/kleintest.sh p4000a r5f-fu-r55 r5f.py fuettern --teil raster55 --geraet cuda --out /home/fmh/fmhc-physics-remote/runde7-r5f/ausgabe-fuettern
cd /home/fmh/fmhc-physics-remote/runde7-r5f && bash /home/fmh/fmhc-physics-remote/kleintests/kleintest.sh p4000b r5f-fu-r70 r5f.py fuettern --teil raster70 --geraet cuda --out /home/fmh/fmhc-physics-remote/runde7-r5f/ausgabe-fuettern
```

**(c) kavitation**, GPU:

```
cd /home/fmh/fmhc-physics-remote/runde7-r5f && bash /home/fmh/fmhc-physics-remote/kleintests/kleintest.sh p4000b r5f-kav-raster r5f.py kavitation --teil raster --geraet cuda --out /home/fmh/fmhc-physics-remote/runde7-r5f/ausgabe-kavitation
cd /home/fmh/fmhc-physics-remote/runde7-r5f && bash /home/fmh/fmhc-physics-remote/kleintests/kleintest.sh p4000a r5f-kav-box r5f.py kavitation --teil box --sehrfein --geraet cuda --out /home/fmh/fmhc-physics-remote/runde7-r5f/ausgabe-kavitation
```

CPU-Ausweg fuer (c), falls beide GPUs belegt sind:
- Je S0 und Stufe ein Aufruf, S0 = 0.70 / 0.72 / 0.75 / 0.80 auf cpu bis cpu4.
- Beide Stufen mit `--T 400`, damit fein unter 10 min bleibt.
- Beispiel fuer 0,72:

```
cd /home/fmh/fmhc-physics-remote/runde7-r5f && bash /home/fmh/fmhc-physics-remote/kleintests/kleintest.sh cpu r5f-kav072g r5f.py kavitation --teil raster --s0 0.72 --stufe grob --T 400 --geraet cpu --out /home/fmh/fmhc-physics-remote/runde7-r5f/ausgabe-kavitation
cd /home/fmh/fmhc-physics-remote/runde7-r5f && bash /home/fmh/fmhc-physics-remote/kleintests/kleintest.sh cpu2 r5f-kav072f r5f.py kavitation --teil raster --s0 0.72 --stufe fein --T 400 --geraet cpu --out /home/fmh/fmhc-physics-remote/runde7-r5f/ausgabe-kavitation
cd /home/fmh/fmhc-physics-remote/runde7-r5f && bash /home/fmh/fmhc-physics-remote/kleintests/kleintest.sh cpu3 r5f-kav072l r5f.py kavitation --teil raster --s0 0.72 --nur-auswertung --geraet cpu --out /home/fmh/fmhc-physics-remote/runde7-r5f/ausgabe-kavitation
```

Die Vorhersagetabelle (c) ohne Rechnung, Sekunden: `kavitation --nur-vorhersage --geraet cpu` (steht schon im lokalen
Rauchbericht, Abschnitt 4).

Ausgaben danach nach RUNDE-07/r5f/lauf-69/ holen.

## 2. Laufzeiten (Schaetzung, nicht auf der .69 gemessen)

Grundlagen:
- **.69-CPU** (R5-A, LAUF2.log): radial 1,67 ms je Schritt bei 6 x 1501 und 2,70 ms bei 6 x 3001, also etwa 0,63 ms
  plus 115 ns je Punkt und Schritt.
- **P4000** (R5-B, LAUF.log): 1,24 ms je Schritt bei 49 x 3001 und 1,6 ms bei 49 x 6001, also etwa 0,9 ms plus 2,4 ns je
  Punkt und Schritt.
- **Laptop, Rauchtest:** radial 0,31 ms plus 39 ns, 1D 71 ns je Punkt und Schritt. Die .69-CPU war in Runde 5 etwa 2,5-
  bis 3-mal langsamer.

| Aufruf | Spur | Laeufe x Punkte (grob) | Schritte grob + fein | Schaetzung |
|---|---|---|---|---|
| rauch | p4000a / cpu | klein | - | unter 1 min |
| tod grob T = 4000 | cpu | 8 x 1501 | 80000 | 3 bis 4 min (plus 20 s Schiessen) |
| tod fein T = 2000 | cpu2 | 8 x 3001 | 80000 | 5 bis 6 min |
| tod nur-auswertung | cpu3 | - | - | unter 30 s |
| tod beide T = 3000 (Alternative) | p4000 | 8 x 1501 | 60000 + 120000 | etwa 5 min (plus 40 s Schiessen) |
| fuettern mechanik | p4000a | 43 x 6401 | 12000 + 24000 | 1,5 bis 2 min |
| fuettern raster55 | p4000a | 149 x 6401 | 12000 + 24000 | 3 bis 4 min |
| fuettern raster70 | p4000b | 149 x 6401 | 12000 + 24000 | 3 bis 4 min |
| kavitation raster | p4000b | 100 x 2000 | 12000 + 24000 | 1,5 bis 2,5 min |
| kavitation box --sehrfein | p4000a | 10 x 2000 / 4000 | L200: 12000 + 24000 + 48000; L400: 12000 + 24000 | 2 bis 3 min |
| kavitation raster je S0 und Stufe, T = 400 (CPU-Ausweg) | cpu... | 25 x 2000 | 8000 bzw. 16000 | grob 1,5 min, fein 5 bis 6 min |

- **Speicher:** Das groesste Feld hat raster fein 149 x 12801 complex128, also 30 MB je Feld und etwa 0,6 bis 0,8 GB
  insgesamt. Der Code deckelt den Torch-Speicher auf 1,5 GB.
- Fuer p4000b gilt wie bisher: nur, solange WM-1-MB nicht laeuft.

## 3. Aufbau je Frage (vor dem Lauf festgelegt)

### (a) tod: Ist der Rest unter Q_min ein Oszillon?

- **Geometrie:** 3D radial wie r5a (r bis 150, Schwamm ab 110). Fenster r < 25 (wie R5), dazu der Kern r < 10.
- **Messung** alle 0,5:
  - Q und E gesamt, im Fenster und im Kern
  - psi im Zentrum, komplex
  - max |psi|^2
  - Energieradius
- **Laeufe** (Start omega^2 = 0,80, Q = 186,1, gamma = 1e-3; t_stop aus Q_erw = Faktor x Q_min):
  1. Stopp bei 1,05 Q_min (t = 461)
  2. Stopp bei 0,95 Q_min (t = 561)
  3. Stopp bei 0,9 Q_min (t = 615, wie R5)
  4. Stopp bei 0,8 Q_min (t = 733)
  5. Dauerabfluss 1e-3 (Reproduktion R5)
  6. Gegenprobe ohne Abfluss, omega^2 = 0,80
  7. Gegenprobe ohne Abfluss, omega^2 = 0,90 (knapp ueber Q_min, stabiler Ast)
  8. Klumpen: Profil bei omega^2 = 0,927 (Q ~ Q_min), psi und psi_t mal 0,95, also Q ~ 0,90 Q_min, ohne Abfluss
- **Kenngroessen:**
  - t90 / t50 / t10 wie R5 (q_rel = Q_in/Q_erw), dazu dieselben Zeiten fuer den Kern
  - omega vor dem Tod: Phase wie R5, dazu das komplexe Spektrum in [t90 - 210, t90 - 10]
  - E_in/E_ref mit E_ref = E_in bei t90 - 10: nach t10 + 100 / + 500 / + 1000 und bei T
  - Fenster frueh [t10 + 100, t10 + 500] und spaet [max(t10 + 100, T - 1000), T]:
    - Spektrum von psi im Zentrum, Hann-Fenster
    - Omega > 0 heisst exp(-i Omega t), also Teilchen
    - Leistungsanteil unter der Luecke (|Omega| < 1 - 2 dOmega)
    - Asymmetrie (P+ - P-)/P: Q-Ball +1, reelles Oszillon 0
  - S_max im Fenster, Abklingrate lambda_E
  - Laufzeitbild: v_g = sqrt(omega^2 - 1)/omega aus omega vor dem Tod, Dauer-Vorhersage (25 - R_E)/v_g
- **Klassen (vorab):**
  - **Oszillon:** E_spaet >= 0,1 E_ref, E_spaet >= 0,5 E_frueh, Hauptlinie unter 1 und S_max spaet >= 0,01
  - **zerlaeuft:** E_spaet < 0,02 E_ref oder S_max spaet < 1e-3
  - sonst **unklar**
  - Merkmal **Plateau frueh:** dieselben Bedingungen im fruehen Fenster, fuer ein kurzes Oszillon
  - Beim Dauerabfluss steht der Vermerk "Abfluss laeuft weiter", weil der Abfluss dort auch ein Oszillon daempft.

### (b) fuettern: Warum nimmt der grosse Ball unter der Schwelle Ladung auf?

- **Hypothesen:**
  - **H1 (Spektrum):** Der Auslaeufer des Pakets ueber der Schwelle 2 omega + 1 = 2,483 wird gefressen. Das waere
    Paket-Numerik, keine Physik.
  - **H2 (Resonanz):** Das Paket fuellt die innere Resonanz des 1D-Balls, einen Feshbach-Zustand des geschlossenen
    Partnerkanals.
    - Der Pol ist aus RUNDE-06 bekannt (1D, Bruecke dims 1, zwei Haeuser bei 0,70): rho = 1,3767 - 5,1e-3 i bei 0,55
      und 1,4938 - 6,7e-5 i bei 0,70.
    - Das gibt nu_r = omega + Re rho = 2,1183 bzw. 2,3305.
    - Die gefangene Ladung sitzt am Ball, traegt die Energie nu je Ladung und laeuft mit 2 Gamma wieder aus.
    - Das passt zu R5: dE/dQ = 2,15 statt 0,74, und C_Q ist linear in eps.
  - **H3 (nichtlinear):** Zwei-Quanten-Einfang, dann dQ ~ eps^4.
- **Geometrie:** Box +-320 (Schwamm ab 280), Paketmitte startet bei x0 = -150, T = 600, Messung alle 0,5.
  - Reflexe vom Schwamm kaemen erst nach t ~ 745 zurueck.
- **Messung:**
  - Q und E in |x| < 10 / 20 / 40
  - Ladungs- und Energiefluss bei x = -40 und +40
  - Phase und Ort des Maximums, Breite, Q und E gesamt
- **Teile:**
  - **mechanik** (43 Laeufe):
    - Amplitude: eps = 0,0025 / 0,005 / 0,01 / 0,02 / 0,05 bei nu = 2,2 und 2,8, sigma = 8
    - Breite: sigma = 4 / 8 / 16 / 32 bei nu = 2,125 (Resonanz), 2,2 (R5) und 2,4 (zwischen Resonanz und Schwelle),
      eps = 0,01
  - **raster55 / raster70** (je 149 Laeufe): nu = 1,90 bis 2,80 in 0,025 (37 Werte), sigma = 8 (wie R5) und 32
    (spektrale Breite 0,02), eps = 0,01
  - Jeder Ball+Paket-Lauf hat seinen Paket-allein-Lauf; je Ball gibt es einen Ball-allein-Lauf.
- **Kenngroessen:**
  - C_nach = [Q20(Ball+Paket) - Q20(Ball) - Q20(Paket)] / |Q_Paket| in [t_nach, t_nach + 20]
    - t_nach = Ankunft der Paketmitte + (4 sigma + 20)/v_g + 10
  - C_R5: dasselbe im Fenster der Runde 5, 163 bis 188 nach Ankunft
  - C_Ende
  - kappa: Abklingrate von dQ20 in [t_nach, t_nach + 200]
  - C_ankunft = C_nach exp(kappa (t_nach + 10 - Ankunft)), weil breite Pakete spaeter gemessen werden
  - dE/dQ
  - Ort 10/20 und 40/20
  - R und T aus den Flussintegralen
  - Atmung: Spektrum von S_max (Ball+Paket minus Ball) nach dem Durchgang
  - x_Ende (Rueckstoss), d omega, Born-Schaetzung
- **Zusammenfassungen:**
  - Exponent p in dQ ~ eps^p
  - C(sigma) je nu
  - im Raster: Spitze unter der Schwelle (Parabel), FWHM, kleinstes C zwischen Spitze + 0,1 und Schwelle, erster Wert
    ueber der Schwelle, Abweichung der Spitze von nu_r

### (c) kavitation: Zerfaellt das dichte Kondensat wirklich?

- **Papier vorab** (von Hand, im Code nachgerechnet):
  - Das homogene Kondensat hat omega^2 = U'(S0) und den Druck P0 = omega^2 S0 - U(S0) = S0^2 (S0 - 1) < 0:
    - -0,147 / -0,145 / -0,141 / -0,128 bei S0 = 0,70 / 0,72 / 0,75 / 0,80
  - Zwischen der Spinodale 2/3 und S0 = 1 ist es linear stabil, steht aber unter Zug, ist also metastabil.
  - Bei festem omega hat g(S) = omega^2 S - U(S) die Form g(S) - g(S0) = -(S - S0)^2 (S - S_t)/2 mit S_t = 2 - 2 S0.
  - Daraus folgt ein statischer kritischer Keim (1D-Bounce, Sattel) mit kleinster Dichte S_t:
    - S_t = 0,60 / 0,56 / 0,50 / 0,40 fuer S0 = 0,70 / 0,72 / 0,75 / 0,80
    - Halbbreite bei halber Tiefe etwa 5,0 / 4,05 / 3,3 / 2,87
    - Barriere F_b = sqrt 2 Int_{S_t}^{S0} (S0 - S) sqrt((S - S_t)/S) dS: etwa 1,5e-3 / 4,88e-3 / 1,5e-2 / 5,10e-2
    - Die Werte fuer 0,72 und 0,80 stammen aus dem Code, die fuer 0,70 und 0,75 sind von Hand.
  - F = H - omega Q bleibt bei der Rechnung erhalten. Liegt die Delle unterhalb der Barriere mit dem homogenen
    Zustand verbunden, kann sie nicht kavitieren.
  - Geprueft wird das mit dem groessten dF entlang der Familie d' = 0 ... d (dF_Pfad_max < F_b).
  - Ein negatives dF allein heisst nichts: volle Dellen liegen schon jenseits der Barriere.
- **Aufbau** wie r5b.mi:
  - periodische Box L = 200, Rauschen 1e-6 (Saat 21)
  - Delle psi -> psi (1 - d exp(-x^2/2w^2)), psi_t = -i omega psi
  - T = 600, Messung alle 1, Schnappschuesse alle 25
- **Teil raster** (100 Laeufe): S0 = 0,70 / 0,72 / 0,75 / 0,80.
  - Tiefe als kleinste Dichte S_min:
    - "flach": halbe Strecke zwischen S0 und 2/3
    - "knapp": 0,637
    - "mittel": 0,5
    - "tief": 0,3
    - "sehr tief": 0,1
    - "voll": 0, wie R5
  - Breite w = 1 / 2 / 4 / 8, je S0 dazu eine Kontrolle ohne Delle.
- **Teil box:** S0 = 0,72 und 0,80, je Kontrolle, voll w = 2, tief w = 4, knapp w = 8, flach w = 8.
  - Gerechnet bei L = 200 und 400, jeweils grob und fein.
  - Mit `--sehrfein` zusaetzlich dx = 0,025 und dt = 0,0125.
- **Messung:**
  - rms(dS), S_max, S_min, Q und E
  - Leerlaenge (S < S0/2) und Zahl der Luecken
  - Klumpen (Definition R5)
  - S in der Dellenmitte, Laenge mit S < 2/3
- **Klassen:**
  - **heilt:** keine Stelle mit S < S0/2 in [T/2, T]
  - **zerfaellt:** mindestens 3 Luecken (Median der letzten 10 %)
  - sonst **Kaverne**
  - t_kav: Zeitpunkt, ab dem die Leerlaenge >= max(10, Anfang + 5) ist

## 4. Vorhersagen (vor dem Rechnen)

### (a) tod

- **V-a1 Reproduktion R5** (Dauerabfluss 1e-3):
  - t90 = 652 +- 5, t10 = 852 +- 10
  - omega vor dem Tod (Phase) 1,007 +- 0,002
  - Q_in(t90)/Q_min = 0,775 +- 0,01
  - Stopp 0,9: t90 = 652 +- 5
- **V-a2 Laufzeitbild (neu, kann scheitern):**
  - Die langsame Aufloesung ist das Auslaufen eines ungebundenen Klumpens mit omega knapp ueber 1. Seine Wellen haben
    v_g = sqrt(omega^2 - 1)/omega ~ 0,12.
  - Dauer t10 - t90 (Fenster r < 25) = (25 - R_E)/v_g auf 30 %.
  - Der Kern r < 10 leert sich frueher: Dauer_Kern <= 0,5 x Dauer_Fenster.
  - Gegenhypothese: Kern und Fenster leeren sich gleich schnell (Zerfall an Ort und Stelle).
- **V-a3 Spektrum vor dem Tod:** Hauptlinie bei Omega = +1,000 bis +1,015, also ueber der Luecke, mit Asym > 0,9. Der
  Klumpen hat dann noch positive Frequenz (Ladung), ist aber nicht mehr gebunden. Das erklaert omega = 1,007 aus R5.
- **V-a4 Hauptfrage:** Der Rest zerlaeuft (Klasse "zerlaeuft", kein fruehes Plateau).
  - Gilt fuer Stopp 0,95 / 0,9 / 0,8 und den Klumpen 0,927 x 0,95.
  - Stuetze: R5, Stopp 0,9, hatte bei T = 1500 S_c = 2,4e-5 und q_rel = 0,003. Ein kugeliges Oszillon haette im
    Zentrum meist |psi|^2 ~ 0,1 bis 0,5.
  - Sicherheit maessig: Die Literatur (L4) kennt ein Oszillon-Stadium nach dem Zerfall zusammengesetzter Q-Baelle in
    sextischen U(1)-Modellen.
  - **Gegenhypothese (L1), Oszillon:** E_spaet >= 0,1 E_ref, Linie bei |Omega| 0,85 bis 0,99, Asym nahe 0,
    S_max spaet >= 0,01.
- **V-a5:**
  - Stopp 0,95 stirbt auch: t50 - t_stop zwischen 50 und 500.
  - Stopp 1,05 lebt bis T: q_rel(T) > 0,9, Linie bei +0,93 bis +0,96, Asym > 0,95.
- **V-a6 Gegenproben ohne Abfluss:**
  - |dQ_in|, |dE_in| < 1e-3 bis T
  - Linie bei +0,8944 bzw. +0,9487 (auf 2 dOmega), Anteil > 0,5, Asym > 0,95

### (b) fuettern

- **V-b1 Amplitude:** dQ ~ eps^p mit p = 2,0 +- 0,15, bei nu = 2,2 (unter der Schwelle) und bei 2,8 (darueber). Beides
  ist linear; p ~ 4 hiesse Zwei-Quanten-Einfang (H3).
- **V-b2 Ort und Energie:**
  - Unter der Schwelle sitzt die Zusatzladung am Ball: Ort 10/20 >= 0,8.
  - Sie traegt nu je Ladung: dE/dQ = nu auf 10 %, nicht omega.
  - Ueber der Schwelle gilt dE/dQ = omega auf 10 % (wie R5).
- **V-b3 Lebensdauer:**
  - 0,55 nahe nu_r: dQ20 klingt mit kappa = 2 Gamma = 0,0102 ab (auf 30 %).
  - 0,70 nahe nu_r: kappa < 1e-3.
- **V-b4 Raster:**
  - Die Spitze unter der Schwelle liegt bei nu_r = 2,118 (0,55) bzw. 2,330 (0,70), auf +-0,03 (sigma 32) bzw. +-0,05
    (sigma 8).
  - Zwischen Spitze + 0,1 und Schwelle faellt C_nach (sigma 32) um mindestens den Faktor 10.
  - Ueber der Schwelle springt C auf die Born-Hoehe (0,55: etwa 0,04 bis 0,07).
  - Die Atmungslinie liegt bei Omega = Re rho (1,377 bzw. 1,494) auf 0,03.
- **V-b5 Breite:**
  - nu = 2,4: C faellt von sigma 8 auf 32 um mindestens den Faktor 10. Das ist der Auslaeufer ueber der Schwelle, also
    Paket-Spektrum, keine Physik.
  - nu = 2,125: C_ankunft faellt von sigma 8 auf 32 hoechstens um den Faktor 3.
  - nu = 2,2: C(sigma 4)/C(sigma 8) liegt zwischen 0,3 und 3; H1 verlangt etwa 100.
- **V-b6 Reproduktion R5:** C_R5(0,55; 2,2; eps 0,01; sigma 8) = 0,024 +- 0,005.
- **V-b7 Bilanz:** |Bilanz_Q| < 1e-3; unter der Schwelle 0 <= R, T <= 1.
- Liegt die Spitze nicht bei nu_r, oder ist p ~ 4, ist H2 widerlegt. Faellt C bei nu = 2,2 mit sigma wie H1 verlangt,
  ist der R5-Befund ein Paket-Artefakt.

### (c) kavitation

- **Regel (vorab, im Code `ka_vorhersage`):**
  - S_min > 2/3 oder dF_Pfad_max < F_b: **heilt**
  - sonst S_min < S_t: **kavitiert**
    - S0 <= 0,75: Zerfall in Klumpen (>= 3 Luecken). Grund: groesserer Energiegewinn je Ladung (0,053 / 0,048 / 0,039
      gegen 0,026 bei 0,80) und die Naehe zur Spinodale.
    - S0 = 0,80: eine Kaverne (<= 2 Luecken)
  - sonst **unklar**
- **Tabelle aus den Anfangsfeldern** (lauf-lokal/rauch-cpu.log, Abschnitt "Vorhersage vorab"), 100 Laeufe:
  35 heilt (davon 4 Kontrollen), 48 zerfaellt, 12 Kaverne, 5 unklar.
  - "flach": alle 16 heilen (Leitungsvorhersage).
  - "knapp" (S_min 0,637 < 2/3):
    - **Widerspruch zur einfachen Spinodalregel:** 13 von 16 heilen, obwohl das Minimum unter 2/3 liegt.
    - Der Keim reicht tiefer (S_t), und dF bleibt unter der Barriere.
    - unklar: 0,70 w = 1 und w = 8, 0,80 w = 8
    - Grenzfall: 0,72 w = 8 mit dF/F_b = 1,00
  - "mittel" (0,5):
    - 0,70 / 0,72 / 0,75: zerfaellt
    - 0,80: w 1 und 2 heilen, w 4 und 8 unklar (S_t = 0,4 < 0,5)
  - "tief", "sehr tief", "voll": zerfaellt (0,70 bis 0,75), Kaverne (0,80)
- **V-c1:** Die Kontrollen ohne Delle bleiben homogen: rms/S0 < 1e-3 bei allen S0.
- **V-c2:** Die Vorhersage trifft mindestens 80 % der Laeufe ohne "unklar" in der groben Frage heilt/heilt nicht.
  Bei der feinen Frage (Klumpen gegen Kaverne) mindestens 60 %.
- **V-c3 "echt oder Numerik":**
  - Die Klassen stimmen grob gegen fein in mindestens 90 % der Laeufe.
  - t_kav besteht L3.
  - L = 400 gibt dieselbe Klasse und dieselbe Lueckendichte je 100 (auf Faktor 1,5).
  - sehrfein aendert keine Klasse.
  - Dann ist der Zerfall bei 0,72 echt: eine nichtlineare Instabilitaet (Kavitation ueber den Keim), keine Numerik.
- **Gegenhypothese (L1):**
  - Flache oder knappe Dellen zerfallen.
  - Oder tiefe, breite Dellen (dF_Pfad_max deutlich ueber F_b) heilen.
  - Oder die Klasse haengt von dx oder L ab.

## 5. Gegenproben, L3 und Plausibilitaet

| Frage | Gegenprobe (Effekt muss fehlen bzw. stimmen) | L3 (Aufloesung) | Plausibilitaetsschranken |
|---|---|---|---|
| (a) | ohne Abfluss 0,80 und 0,90; Stopp 1,05 lebt; Dauerabfluss reproduziert R5 | dr/2, dt/2: grob T = 4000, fein T = 2000, verglichen bis 2000: t50, Dauer, E_spaet/E_ref, Omega spaet, Klasse | 0 <= E_in <= E_tot (Zaehlung); E_tot steigt nach dem Stopp nicht (Schwamm nimmt nur): Anstieg <= 1e-4 rel.; q_rel <= 1,02; Spektralanteile in [0, 1], Asym in [-1, 1]; Gegenproben-Drift < 1e-3 |
| (b) | Paket allein und Ball allein (abgezogen); ueber der Schwelle (Born, R5); zweiter Ball 0,70 mit eigenem nu_r; nu = 2,4 als Auslaeufer-Probe | dx/2, dt/2: C_nach, kappa, nu_peak | -1 <= C <= 1; Ladungsbilanz \|Int (j(-40) - j(+40)) dt - dQ40\| / Q_Paket < 1e-3 (Energie ebenso berichtet); unter der Schwelle 0 <= R, T <= 1 (Code: -0,2 bis 1); Paket allein im Fenster < 1e-3 |
| (c) | Kontrollen ohne Delle; flache Dellen; Box 400 | dx/2, dt/2 (raster, box); box zusaetzlich dx/4, dt/4 | Q-Drift < 1e-10 (periodisch, Verlet exakt); E-Drift < 1e-3; 0 <= Leerlaenge <= L; S_min >= 0; Kontrollen rms/S0 < 1e-3 |

Der Code prueft L3 als "Effekt >= 5 x Aenderung grob -> fein" (r5b.l3), dazu die Gleichheit der Klassen. Die
Plausibilitaet steht je Lauf als "plaus ok/NEIN" im Bericht.

## 6. Latten (Vorschlag, die Leitung entscheidet)

| Latte | (a) tod | (b) fuettern | (c) kavitation |
|---|---|---|---|
| L1 kann scheitern | ja: Klassen vorab; Laufzeitbild v_g; Kern gegen Fenster | ja: Spitzenlage nu_r aus RUNDE-06 vorab; p = 2 gegen 4; kappa = 2 Gamma | ja: Vorhersagetabelle fuer 100 Laeufe aus Keim und Barriere |
| L2 Gegenprobe | ohne Abfluss 0,80/0,90; Stopp 1,05 | Paket/Ball allein; ueber der Schwelle; 0,70 | Kontrollen; flache Dellen; Box 400 |
| L3 Numerik | dr/2, dt/2 im Code | dx/2, dt/2 im Code | dx/2, dt/2; box dx/4 |
| L4 schon bekannt | teilweise: Oszillon-Stadium nach Zerfall von Charge-Swapping-Q-Baellen in 3+1D (Xie, Saffin, Zhou 2021); Tod bei kritischer Ladung nur als Suchtreffer | teilweise: Resonanzstreuung und Zeitverzug sind Standard; der 1D-Pol ist aus RUNDE-06 zweihaeusig bekannt; Anwendung aufs Fuettern vermutlich neu | vermutlich: Spinodale, Binodale und kritischer Blasenkeim sind Lehrbuch; "bubble of the false broken vacuum" in Q-Ball-Dynamik (Canillas Martinez u. a. 2025) |
| L5 Messbezug | nein | nein | nur Analogie: Kavitation in Fluessigkeiten unter Zug, Blasen in Quantenfluessigkeiten |

**L4-Kurzrecherche** (zwischen 04:34:01 und 04:35:22; Grenzen mit date gemessen):
- **An der Quelle gelesen (Abstract):**
  - Xie, Saffin, Zhou, "Charge-Swapping Q-balls and Their Lifetimes", JHEP07(2021)062, arXiv:2101.06988: 2+1D und
    3+1D; Stadien "initial relaxation, first plateau (CSQ stage), fast decay and second plateau (oscillon stage)".
  - Mukaida, Takimoto, Yamada, "On Longevity of I-ball/Oscillon", JHEP 1703 (2017) 122, arXiv:1612.07750:
    Langlebigkeit ueber naeherungsweise U(1).
  - Canillas Martinez, Dorey, Romanczukiewicz, Saffin, Slawinska, Wereszczynski, "Oscillons and bubbles in Q-ball
    dynamics", arXiv:2509.03192: geladene Oszillonen und Blasen des falschen Vakuums als Zwischenzustaende.
- **Nur Suchtreffer, nicht an der Quelle gelesen:**
  - Q-Baelle und Oszillonen verschwinden ploetzlich bei einer kritischen Ladung.
  - Die sextische Kopplung 1/2 der CSQ-Arbeiten entspricht womoeglich genau unserem U. Die Normierung ist nicht
    geprueft.
- Frage an die Leitung: Volltext Xie u. a. lesen, ob dort ein Q-Ball unter Q_min (ohne Ladungsverletzung) gerechnet ist.

## 7. Grenzen

- **Radial nur l = 0** (a): nichtkugelige Oszillonen und Charge-Swapping-Paare sind unsichtbar. "zerlaeuft" heisst nur:
  kein kugeliger Rest.
- **Abfluss:** Er ist gleichmaessig und phaenomenologisch (-gamma psi_t) wie in R5, kein Feld.
- **Energiekriterium (c):** Es gilt streng nur fuer das unendliche System mit einem einzigen Sattel (Bergpass-Bild).
  - In der periodischen Box kehrt Schall nach L/c_s ~ 300 bis 600 zurueck. Das kann in einem nahezu stabilen
    Kondensat spaet nachkeimen.
  - Deshalb gibt es den Box-Vergleich 200 gegen 400.
  - Die Unterscheidung Klumpen gegen Kaverne ist geraten (geringe Sicherheit).
- **Zahlen aus RUNDE-06** (b): Die 1D-Pole stammen aus RUNDE-06.md (Tabelle "1D zum Vergleich", lokal gerechnet; der
  Pol bei 0,70 ist zweihaeusig bestaetigt). Die Vorhersage nu_r haengt an diesen Zahlen.
- **C_nach** haengt vom Messzeitpunkt ab: Die gefangene Ladung laeuft bei 0,55 mit etwa 1 % je Zeiteinheit aus.
  Deshalb gibt es kappa und C_ankunft.
- **Nicht gerechnet:** Die Laufzeiten fuer die .69 sind hochgerechnet (Abschnitt 2); die Rauchtests dort liefern die
  echten Werte.

## 8. Lokaler Rauchtest (Laptop)

- **Freigabe:** Finn, 30.09. 02:42, laut Projekt-Memory "feedback-lokale-pruefung-ohne-python" (CPU, 1 Faden,
  nice 19, timeout 120).
- **Befehl:**

```
cd /home/fmh/fmhc-physics/coordination/runden-v3/RUNDE-07/r5f && CUDA_VISIBLE_DEVICES= OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 nice -n 19 timeout 120 python3 r5f.py rauch --geraet cpu --out lauf-lokal/rauch-cpu > lauf-lokal/rauch-cpu.log 2>&1
```

- **Ergebnis (letzter Lauf 04:35:22 bis 04:35:40):** rc = 0, 15,9 s, keine Ausnahme.
  - Alle drei Befehle liefen mit grob und fein, dazu der `--nur-auswertung`-Pfad; der Bericht war gleich lang.
  - Plausibilitaet ok.
  - Kontrollen der Kavitation: rms/S0 1e-6 bis 2e-5 bei T = 30.
  - Gegenproben (a): dQ_in, dE_in 1e-5 bis 1e-4 bei T = 40.
- **Synthetische Probe der Auswertung** (lauf-lokal/synth.log, zwischen 04:32:42 und 04:33:45; Grenzen gemessen):
  - Aus bekannten Kurven wurden zurueckgewonnen: Spitze 2,1197 bei Vorgabe 2,118; kappa 0,0102; dE/dQ = nu; p = 2.
  - Die Klassen "Oszillon" (Asym 0) und "zerlaeuft" wurden richtig vergeben.
- Die Zahlen sind eine Vorschau, kein Ergebnis.

## Einfach gesagt

Wir pruefen drei Ueberraschungen aus Runde 5 genauer. Ein Ball unter seiner Mindestgroesse ist vermutlich schon tot und
nur ein loser Klumpen, dessen Wellen sehr langsam davonlaufen; die Rechnung kann aber auch einen langlebigen,
pulsierenden Rest zeigen. Dass ein grosser Ball "verbotene" Wellen schluckt, erklaeren wir mit einer Eigenschwingung,
die Wellen genau einer Frequenz kurz festhaelt und langsam wieder abgibt, wie eine angeschlagene Glocke. Das dichte
Medium steht unter Zug wie Wasser in einer Pumpe: Eine flache Delle heilt, eine tiefe reisst eine Blase auf, und wie
tief "tief genug" ist, haben wir vorher ausgerechnet. Gerechnet wird auf der .69, jeder Teil in hoechstens zehn Minuten.

Beginn 2026-09-30 04:01:55 CEST, Ende 2026-09-30 04:40:24 CEST (beide mit date gemessen).
