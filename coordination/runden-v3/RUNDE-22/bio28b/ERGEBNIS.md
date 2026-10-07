# Runde 22, bio28b: Ergebnis

Code-Agent (Opus 5.5) fuer claude-primary. Karte KARTE.md, Plan PLAN.md.eingefroren-20261002-192006 (eingefroren
19:20:06 CEST, vor jedem echten Lauf; davor nur der dokumentierte Rauchlauf). Laeufe auf der .69 von 17:20:18 bis
17:30:35 UTC (19:20:18 bis 19:30:35 CEST), alle rc 0. Bericht begonnen 19:32:44 CEST (date). Explorativ (v3), [H].

## 1. Ergebnis

1. **D0 eingetroffen, Box-Pruefung bestanden.**
   - K0 traf in allen acht Zeilen exakt: Verschmelzen bei 1,5 bzw. 2,0, Teilung bei 7,0 bis 14,0, genau wie in R21.
   - Die Box hat dreifache Kantenlaenge (L = 115,2). Die doppelte haette nach den R21-Bahnen nicht gereicht.
   - Kein Maskenpixel kam bis T = 300 tiefer als 79,5; die Randschicht beginnt bei 107,2.
2. **D1 eingetroffen (grob und fein, 4 von 4 Laeufen).** Bei T = 300 hat jeder Lauf zwei getrennte Stuecke. Jedes
   traegt 91 bis 99 % seiner Ladung zur Teilungszeit. Die Stuecke laufen mit |v| = 0,16 bis 0,30 auseinander.
3. **D2 eingetroffen.** Drei Stuecke sind bei T = 300 auf beiden Gittern "auf" und "rund":
   - beide Stuecke von w75_nachbarn1, dQ +0,03 % und -3,5 %
   - das kleinere Stueck von w60_nachbarn1, dQ -3,0 %

   Die uebrigen fuenf Stuecke sind "nicht rund" (w60_nachbarn2, rmax/R_A 1,39 bis 1,40) oder "unentschieden"
   (w75_nachbarn2, w60_nachbarn1 gross). Die Gegenprobe des Klassifikators auf dem R5-Gitter ergab 12 von 12 "auf".
4. **Bedeutung nach Karte (D1 und D2):** Der gefuetterte Drehball zerfaellt in Q-Ball-Toechter ohne Windung. Das ist
   eine Teilung, aber keine Groessengrenze im Sinn von Bio 28 [H]. Alle Stuecke tragen bei T = 100 bis 300 Windung 0,
   mit S_min_kreis 0,49 bis 0,90. Das ist nur berichtet.
5. **Vorbehalte:**
   - "auf" heisst: Q passt auf 10 % zu omega (KF-EICH). Es heisst nicht "unangeregt".
   - Die Geschwindigkeitskorrektur des Klassifikators (omega_ruhe = omega_rot x gamma) war nur bei v = 0,05 geeicht.
     Hier bewegen sich die "auf"-Stuecke mit v = 0,22 bis 0,28. Eine nachtraegliche Gegenrechnung mit omega_geo stimmt
     auf 5e-4 (Abschnitt 3).
   - Nur 3 von 8 Stuecken sind "auf". Ob die anderen spaeter auf die Familie kommen, ist offen.

## 2. K0, Box-Pruefung, Familie und Klassifikator

**K0** (dichte Reihe bis t = 30, Wortlaut R21, Toleranz +-1; PLAN 4.1). Grob und fein gleich:

| Lauf | t_V R21 / R22 | t_T R21 / R22 | bestanden (grob, fein) |
|---|---|---|---|
| w60_nachbarn1 | 2,0 / 2,0 | 14,0 / 14,0 | ja, ja |
| w60_nachbarn2 | 2,0 / 2,0 | 9,0 / 9,0 | ja, ja |
| w75_nachbarn1 | 1,5 / 1,5 | 12,5 / 12,5 | ja, ja |
| w75_nachbarn2 | 1,5 / 1,5 | 7,0 / 7,0 | ja, ja |

- Die n-Folgen der dichten Reihe bis t = 20 sind in allen acht Laeufen dieselben wie in R21. Dazu gehoert auch die
  Phase mit n 4 in w75_nachbarn2.
- Die Schwellen sind gleich, z. B. S_glatt 0,51104763 (w60_nachbarn1).

**Box** (PLAN 2 und 4.6):
- r5_2d_a.py nimmt die Box nicht als Aufrufparameter, r5.Gitter(L, dx) aber schon. bio28b.py setzt L = 3 x 38,4 =
  115,2, also n 768 bzw. 1152. Die Randschicht beginnt bei Tiefe 107,2. r5_2d_a.py ist unveraendert.
- Doppelte Kantenlaenge reichte nach den R21-Bahnen nicht. Die Hochrechnung gab Tiefe etwa 77 bei T = 300 fuer das
  kleine Stueck von w75_nachbarn1, die Randschicht laege bei 68,8. Gemessen: (26,8; -76,8) bei T = 300.

| Lauf | groesste Masken-Tiefe bis 300 (grob / fein) | Q_box(300)/Q_box(0) (grob / fein) |
|---|---|---|
| w60_nachbarn1 | 72,6 / 72,6 | 0,981 / 0,981 |
| w60_nachbarn2 | 51,0 / 51,0 | 0,979 / 0,979 |
| w75_nachbarn1 | 79,5 / 79,4 | 0,960 / 0,961 |
| w75_nachbarn2 | 51,6 / 51,4 | 0,898 / 0,898 |

- Grenze 107,2: bestanden in allen acht Laeufen. Der Q_box-Verlust ist Strahlung, die die ferne Randschicht schluckt.
  Die Stuecke selbst verlieren hoechstens 9 % (Abschnitt 3).

**Familie** (PLAN 2, vor dem Einfrieren):
- Gleich sind das Modell (psi_tt = Lap psi - U'(S) psi, U = S - S^2 + S^3/2), die Ladungs- und Energiedichte und das
  Feldlayout.
- Die R5-Profile m = 0 liegen auf familie_2d_m0.json:
  - 0,60: Q -1,3e-6, E -1,1e-6 relativ
  - 0,75: Q -3,3e-6, E -2,5e-6 relativ
- Die Familiendatei gilt unveraendert. Eine neue Datei war nicht noetig, die Pflicht-K-Pruefung entfiel.
- kg.Gitter(2 L, dx) und r5.Gitter(L, dx) haben dieselben Gitterpunkte. Das Skript hat das in jedem Lauf mit
  torch.equal geprueft.

**Klassifikator-Kontrolle** (Gegenprobe auf dem R5-Gitter, PLAN 4.5): einzelner R5-m = 0-Ball im Ursprung der R5-Box,
Fenster [T - 40, T].

| Ball | Gitter | Urteil S0 0,3 bei T 100 / 200 / 300 | dQ | omega_ruhe (soll) | rmax/R_A |
|---|---|---|---|---|---|
| omega^2 0,60 | grob | auf / auf / auf | +0,08 % | 0,774638 (0,774597) | 0,991 |
| omega^2 0,60 | fein | auf / auf / auf | -0,002 % | 0,774607 | 0,995 |
| omega^2 0,70 | grob | auf / auf / auf | -0,15 % | 0,836698 (0,836660) | 0,954 |
| omega^2 0,70 | fein | auf / auf / auf | -0,18 % | 0,836670 | 0,987 |

- 12 von 12 "auf" und "rund": bestanden. S0 0,1 gibt ebenfalls 12 von 12 "auf".
- u liegt bei hoechstens 6e-7. Das grobe Gitter (dx 0,3) misst omega um 4e-5 zu hoch, also weit innerhalb des Bandes.

## 3. Tabelle je Lauf und Stueck

Legende:
- **Stueck:** Rang bei t_T (Q absteigend; bei Gleichstand das mit groesserem Y zuerst).
- **Q(t_T):** Ladung im Maskengebiet bei t_T, dazu die Windung bei t_T.
- **Anteil:** Q im Maskengebiet bei T / Q(t_T).
- **v:** |P|/E des Gebiets bei T = 300.
- **Windung bei 300:** nur berichtet, mit S_min_kreis in Klammern.
- **Rundheit:** rmax/R_A des Fenstertropfens am Fensterbeginn (T - 40). "rund" heisst hoechstens 1,3.
- **Urteil:** Klassifikator bei S0 = 0,3; "unent." heisst unentschieden.

| Gitter | Lauf | Stueck | t_T | Q(t_T) | Anteil T 100 / 200 / 300 | v (300) | Windung bei 300 | Rundheit 100 / 200 / 300 | Urteil 100 / 200 / 300 |
|---|---|---|---|---|---|---|---|---|---|
| grob | w60_nachbarn1 | 0 | 14,0 | 92,03 (w 0) | 0,976 / 0,98 / 0,955 | 0,187 | 0 (0,57) | 1,3 / 1,14 / 1,23 | unent. / unent. / unent. |
| grob | w60_nachbarn1 | 1 | 14,0 | 56,69 (w 1) | 0,958 / 0,977 / 0,958 | 0,256 | 0 (0,9) | 1,25 / 1,15 / 1,06 | unent. / unent. / auf |
| grob | w60_nachbarn2 | 0 | 9,0 | 100,45 (w 0) | 1,015 / 0,984 / 0,956 | 0,165 | 0 (0,56) | 1,31 / 1,42 / 1,39 | nicht rund / nicht rund / nicht rund |
| grob | w60_nachbarn2 | 1 | 9,0 | 100,45 (w 0) | 1,015 / 0,984 / 0,956 | 0,165 | 0 (0,56) | 1,31 / 1,42 / 1,39 | nicht rund / nicht rund / nicht rund |
| grob | w75_nachbarn1 | 0 | 12,5 | 36,09 (w 0) | 0,989 / 0,985 / 0,991 | 0,233 | 0 (0,64) | 1,17 / 1,15 / 1,09 | unent. / unent. / auf |
| grob | w75_nachbarn1 | 1 | 12,5 | 25,08 (w 1) | 0,946 / 0,944 / 0,94 | 0,296 | 0 (0,64) | 1,05 / 0,99 / 1,01 | auf / auf / auf |
| grob | w75_nachbarn2 | 0 | 7,0 | 41,29 (w 0) | 0,906 / 0,913 / 0,915 | 0,175 | 0 (0,64) | 1,2 / 1,15 / 1,14 | unent. / unent. / unent. |
| grob | w75_nachbarn2 | 1 | 7,0 | 41,29 (w 0) | 0,906 / 0,913 / 0,915 | 0,175 | 0 (0,64) | 1,2 / 1,15 / 1,14 | unent. / unent. / unent. |
| fein | w60_nachbarn1 | 0 | 14,0 | 92,08 (w 0) | 0,978 / 0,977 / 0,955 | 0,187 | 0 (0,57) | 1,3 / 1,15 / 1,23 | unent. / unent. / unent. |
| fein | w60_nachbarn1 | 1 | 14,0 | 56,4 (w 1) | 0,957 / 0,981 / 0,961 | 0,256 | 0 (0,9) | 1,25 / 1,17 / 1,08 | unent. / unent. / auf |
| fein | w60_nachbarn2 | 0 | 9,0 | 100,07 (w 0) | 1,022 / 0,989 / 0,96 | 0,165 | 0 (0,55) | 1,31 / 1,42 / 1,4 | nicht rund / nicht rund / nicht rund |
| fein | w60_nachbarn2 | 1 | 9,0 | 100,07 (w 0) | 1,022 / 0,989 / 0,96 | 0,165 | 0 (0,55) | 1,31 / 1,42 / 1,4 | nicht rund / nicht rund / nicht rund |
| fein | w75_nachbarn1 | 0 | 12,5 | 36,02 (w 0) | 0,993 / 0,99 / 0,99 | 0,233 | 0 (0,64) | 1,16 / 1,15 / 1,09 | unent. / unent. / auf |
| fein | w75_nachbarn1 | 1 | 12,5 | 25,3 (w 1) | 0,937 / 0,938 / 0,933 | 0,296 | 0 (0,65) | 1,06 / 1 / 1,03 | auf / auf / auf |
| fein | w75_nachbarn2 | 0 | 7,0 | 41,24 (w 0) | 0,909 / 0,913 / 0,914 | 0,175 | 0 (0,64) | 1,21 / 1,18 / 1,15 | unent. / unent. / unent. |
| fein | w75_nachbarn2 | 1 | 7,0 | 41,24 (w 0) | 0,909 / 0,913 / 0,914 | 0,175 | 0 (0,64) | 1,21 / 1,18 / 1,15 | unent. / unent. / unent. |

- Erzeugt mit hilfs/tabelle.jq aus lauf-69/ausgabe/bio28b_auswertung.json, Kopie in hilfs/tabelle.md.
- Rundheit 1,3 bei w60_nachbarn1, Stueck 0, T = 100 ist 1,299962, also "rund".
- Die Schwerpunkte bei T = 300 (grob) liegen bei:
  - w60_nachbarn1: (7,9; 50,7) und (1,2; -68,9)
  - w60_nachbarn2: +-(4,8; 45,8)
  - w75_nachbarn1: (13,7; 64,6) und (26,8; -76,8)
  - w75_nachbarn2: +-(15,6; 48,4)
- In jedem Lauf und zu jedem T gibt es genau zwei Gebiete, also keine Nebenstuecke. Kein Stueck ging verloren, keines
  verschmolz mit einem anderen.
- Nach R21 trug das ringseitige Stueck der Laeufe mit einem Nachbarn bei t_T noch kurz Windung 1 (S_min_kreis klein).
  Ab T = 100 tragen alle Stuecke Windung 0.

**Klassifikator bei T = 300 (S0 0,3, grob; fein in Klammern, wo verschieden):**
- Q_net ist die Ladung in der Scheibe R_A + 6. Sie liegt 21 bis 43 % ueber dem Masken-Q bei T = 300, weil die Scheibe den Schwanz
  mitzaehlt.
- omega_fam(Q) ist das omega der Familie bei diesem Q.
- E/Q ist auf die Familie bezogen.

| Lauf, Stueck | Klasse | Q_net | omega_ruhe +- u | omega_fam(Q) | dQ (Band) | v Fenster | E/Q gegen Familie |
|---|---|---|---|---|---|---|---|
| w60_nachbarn1, 1 | auf | 77,91 | 0,76805 +- 0,0010 | 0,76905 | -3,0 % (-6,0 bis +0,1 %) (fein -3,0 %) | 0,240 | +0,22 % |
| w60_nachbarn1, 0 | unent. | 119,18 | 0,7512 +- 0,022 | 0,7565 | -19 % (-78 bis +71 %) | 0,186 | +0,93 % |
| w60_nachbarn2, je | nicht rund | 128,26 | 0,74967 +- 0,0020 | 0,75464 | - | 0,159 | +1,28 % |
| w75_nachbarn1, 1 | auf | 31,08 | 0,81409 +- 0,0024 | 0,81407 | +0,03 % (-3,2 bis +3,3 %) (fein -0,02 %) | 0,277 | +0,03 % |
| w75_nachbarn1, 0 | auf | 43,70 | 0,79129 +- 0,0020 | 0,79310 | -3,5 % (-7,3 bis +0,4 %) (fein -3,6 %) | 0,223 | +0,51 % |
| w75_nachbarn2, je | unent. | 45,89 | 0,78808 +- 0,0033 | 0,79063 | -5,1 % (-11,6 bis +1,5 %) | 0,167 | +0,60 % |

- **Nachtraeglich, kein Kriterium:** omega_geo = sqrt(omega_rot x omega_inst) misst omega_ruhe ohne die
  gamma-Korrektur. Bei den drei "auf"-Stuecken stimmt es mit omega_ruhe auf 3e-5 bis 5e-4 ueberein (0,76808 / 0,81427 /
  0,79173). Ohne Korrektur laege omega_rot bei 0,746 / 0,782 / 0,771, die Stuecke waeren dann "neben" [S, Schreibtischrechnung mit der Familientabelle].
- **Nachtraeglich, kein Kriterium:** Bei t = 100 stimmen die Stuecke (grob) mit den R21-5er-Listen (alte Box) auf 0,12 % in Q
  und 0,005 in der Lage ueberein. Die groessere Box aendert die Bewegung vor dem alten Rand also nicht.

## 4. D0 bis D2

| Nr | Vorhersage (Karte) | Wahrsch. | Ausgang | Zahlen |
|---|---|---|---|---|
| D0 | K0 bestanden | 85 % | **eingetroffen** | 8 von 8 Zeilen: t_V und t_T gleich R21 (Abweichung 0). Vorab weitgehend ableitbar (PLAN 1) |
| D1 | In mindestens 3 der 4 gefuetterten Laeufe ueberleben bei T = 300 mindestens zwei Stuecke mit je >= 50 % ihrer Ladung zur Teilungszeit | 60 % | **eingetroffen** (grob und fein) | 4 von 4 Laeufen auf beiden Gittern; Anteile bei T = 300: 0,915 bis 0,991 (grob), 0,914 bis 0,990 (fein); je Lauf 2 getrennte Gebiete |
| D2 | Mindestens eines dieser Stuecke ist bei T = 300 "auf" und "rund" (auf beiden Gittern) | 45 % | **eingetroffen** | 3 Stuecke auf beiden Gittern: w75_nachbarn1 Stueck 0 und 1, w60_nachbarn1 Stueck 1. Kontrolle 12 von 12 "auf" (Bedingung aus PLAN 4.5 erfuellt) |

- Zusammenfassung nach PLAN 4.3 und 4.4: Grob und fein geben dieselben Ausgaenge.
- Bedeutung nach Karte siehe Abschnitt 1, Punkt 4.

## 5. Latten, Grenzen, Selbstanzeigen, Laufzeiten, sha256

**Latten (v3):**
- **L1 (kann scheitern): teilweise.**
  - D0 war weitgehend ableitbar, da gleiche Gitterpunkte und Startfelder, der Rand weit weg.
  - D1 war bis etwa T = 150 durch R21 vorgezeichnet (PLAN 0), bei T = 300 offen.
  - D2 konnte scheitern. 5 von 8 Stuecken sind nicht "auf".
- **L2 (Gegenprobe): ja.**
  - Die Klassifikator-Kontrolle auf dem R5-Gitter ergab 12 von 12 "auf".
  - Der Klassifikator trennt: "nicht rund" bei w60_nachbarn2, "unentschieden" bei w75_nachbarn2.
  - K0 wurde exakt reproduziert, die Box-Pruefung war in allen acht Laeufen bestanden.
- **L3 (Numerik): bestanden.**
  - Grob und fein geben dieselben Ausgaenge D0 bis D2 und dieselbe Klasse in allen 24 Paaren (Stueck x T).
  - Die Anteile weichen hoechstens um 0,009 ab, dQ der "auf"-Stuecke hoechstens um 0,001, omega_ruhe hoechstens um 4e-5.
- **L4 (schon bekannt): weitgehend.** Dass drehende Q-Baelle in nicht drehende Q-Baelle zerfallen und der Drehimpuls
  in die Bahnbewegung geht, ist bekannte Physik [L, nicht nachgelesen]. Neu, nur im Modell: Die Toechter liegen bei
  T = 300 zum Teil messbar auf der m = 0-Familie.
- **L5 (Messbezug): nein.**

**Grenzen:**
- **"auf" heisst "Q passt zu omega" auf 10 %, nicht "ruhig"** (KF-EICH, Satz A).
- **Geschwindigkeitskorrektur:** Sie war in KF-EICH nur bei v = 0,05 geeicht. Hier ist v = 0,16 bis 0,28 (gamma bis
  1,04). D2 haengt an dieser Korrektur. Fuer einen geboosteten Ball ist sie exakt [S]; omega_geo bestaetigt sie
  nachtraeglich auf 5e-4.
- **Zwei Ladungsmasse:** D1 misst die Ladung im Maskengebiet (Schwelle aus dem Original), der Klassifikator Q_net in der
  Scheibe. Sie unterscheiden sich bei T = 300 um 21 bis 43 %. Der Anteil vergleicht Maske mit Maske.
- **Verfolgung:** Sie geht ueber den naechsten Schwerpunkt, alle 5 Zeiteinheiten ab t = 30.
  - Ab t = 20 gab es in allen acht Laeufen in jeder Analyse genau zwei Gebiete.
  - Nur w75_nachbarn2 hatte von t = 13,5 bis 19,5 zwei kleine Nebenstuecke, wie in R21.
  - Die Zuordnung bei T = 100, 200 und 300 ist damit eindeutig.
- **Rest:** 2D, ein Feld, Futter statt Bad (wie R5). T = 300; was danach geschieht, ist offen. Die Stuecke von
  w60_nachbarn2 sind laenglich, ob sie rund werden, ist offen.
- **Radialtabelle:** Sie endet bei r = 100. In den Boxecken stand das Startfeld auf dem letzten Tabellenwert (< 1e-21).

**Selbstanzeigen:**
- Nicht blind: Ich kannte die R21-Bahnen bis t = 200 (PLAN 0). Sie bestimmten die Boxgroesse.
- Nach den Laeufen und vor dem Auswerteaufruf habe ich die Kontrolle und die grob-Rohdaten mit jq angesehen. Danach
  wurde nichts geaendert.
- Nachtraeglich und nicht im Plan, nur beschreibend: die Klassifikator-Zusatztabelle mit omega_geo und omega_rot sowie
  der R21-Vergleich bei t = 100 (Abschnitt 3).
- Reihenfolge: kontrolle und fein-w75 liefen auf p4000a, parallel zu grob und fein-w60 auf p4000b. Der Plan nannte
  p4000b "bei Belegung p4000a" und die Reihenfolge grob, fein-w60, fein-w75, kontrolle. Das hat keine Wirkung auf
  Zahlen.
- py_compile hat auf der .69 einen Ordner __pycache__ in meinem Ordner angelegt.
- Die Laufzeit-Hilfen meiner Umgebung (Hintergrundaufrufe, Monitor) haben Statusdateien unter /tmp/claude-1000/...
  angelegt. Es sind keine Projektdateien, ich habe dort nichts selbst geschrieben.
- Sonst keine Abweichung vom eingefrorenen Plan. r5_2d_a.py und kf5_geburt.py wurden nur importiert.

**Laufzeiten** (.69, kleintest.sh, rc 0 in allen Aufrufen; UTC):

| Aufruf | Spur | Zeit (UTC) | Dauer | Details | GPU max |
|---|---|---|---|---|---|
| Rauch | p4000b | 17:17:46 bis 17:19:39 | Unit 71 s, davor etwa 40 s Lock | - | 570 MB |
| grob | p4000b | 17:20:18 bis 17:25:32 | Unit 180 s, davor etwa 2 min Lock | Schiessen 62,7 s; Entwicklung 113,9 s (Analysen 11,1, Fenster 15,2); 14,60 ms je Schritt | 570 MB |
| kontrolle | p4000a | 17:20:21 bis 17:25:00 | Unit 98 s, davor etwa 3 min Lock | - | 80 MB |
| fein-w60 | p4000b | 17:25:32 bis 17:30:20 | Unit 288 s | Entwicklung 220,5 s; 16,25 ms je Schritt | 733 MB |
| fein-w75 | p4000a | 17:25:00 bis 17:30:00 | Unit 297 s | Entwicklung 231,5 s; 17,32 ms je Schritt | 733 MB |
| auswerten | cpu | 17:30:32 bis 17:30:35 | Unit 3 s | - | - |

- Waechter-Prognosen: 181 s, 284 s und 281 s, alle unter der Grenze von 570 s.

**sha256** (lokal und .69 gleich):
- bio28b.py c17d19516c27bc31f157ffed387c5dcf3849b2b3bf7037bd0c6219d58fe6d7e5
- r5_2d_a.py 4b7a00b22e427ab9889056057437fc2199ca0fe6fff0ccf4847c11f62892bc7b (wie R5/R21)
- kf5_geburt.py 9b895c9f39c2e2708636a1ae50e608fe8041c93cfce4da9a64ea7de32b9b6bc0 (wie R6/KF-EICH)
- familie_2d_m0.json f3446207490bb40298fe9d1d7fe347b3a69d6a175b4d657d32ddf6a01aa0f806 (wie R6/KF-EICH)
- PLAN.md.eingefroren-20261002-192006 b67dcae90acdd7c7f74be7785779227f665708e82cd52bc3563271d4f1d3b007
- lauf-69/ausgabe:
  - grob_roh.json 11970807af76767e65ead0412ea1521a7f4109c9bc807bfe25b518e1bcace1a9
  - fein-w60_roh.json df8ff48e0155d5ad68c4cf33a4f470ead509f6fab253df15d7a0b4498a8b46b4
  - fein-w75_roh.json abda53ce7ae8cfc8692ea751ce196917f82c37a05c5e64e3721f5b1b67ab0e64
  - kontrolle_roh.json 71823dad3c6670b2682e1b7cef98f82e48b23063abbd30e8fa6ae95301eb67a4
  - bio28b_auswertung.json 4bbaf66a0327043a6e0ec32f3e1ed307117f0aca0c46df70d00e126dc923e9ce
  - bio28b_auswertung.txt 9d8dbf2e5b9b569c56f1b03bb269e9660a355bd59eed71ecfa7bb362202cf6f9
- lauf-69/rauch/rauch_roh.json 155727a3f2a8784b64fe1294dd68e617946f12571d9002ece1fcc7ca5ea9bc4b
- Logs: RAUCH a9f3f994..., HAUPT-grob 337ec1dc..., HAUPT-kontrolle 7bc7fbdb..., HAUPT-fein-w60 402c9521...,
  HAUPT-fein-w75 08829d3e..., AUSWERTEN 7430909d... (voll in hilfs/sha256-69.txt und hilfs/sha256-lokal.txt)

**Dateien:**
- Kartenordner:
  - KARTE.md, PLAN.md (+ eingefrorene Fassung), bio28b.py, ERGEBNIS.md
  - hilfs/: tabelle.jq, tabelle.md, sha256-69.txt, sha256-lokal.txt
  - lauf-69/: Spiegel von /home/fmh/fmhc-physics-remote/runde22-bio28b/lauf-69, mit ausgabe/, rauch/ und Logs.
    Keine .pt-Dateien.

## 6. Einfach gesagt

In Runde 21 verschwanden die Bruchstuecke des gefuetterten Drehballs am Rand der Box. Wir wussten nicht, ob sie
einfach weitergelebt haetten. Diesmal war die Box dreimal so breit, und die Stuecke kamen bis zur Zeit 300 nicht an
den Rand. Ergebnis: Alle Stuecke leben weiter und behalten 91 bis 99 Prozent ihrer Ladung. Sie fliegen langsam
auseinander und drehen sich nicht mehr um sich selbst. Das gepruefte Messgeraet sagt bei drei von acht Stuecken: Das
ist ein echter Q-Ball, Ladung und Takt passen zusammen. Die anderen sind noch etwas laenglich oder zu unruhig fuer ein
klares Urteil. Der Drehball teilt sich also in Tochter-Baelle. Eine Groessengrenze, wie Bio 28 sie meinte, ist das aber
nicht.

Ende der Bearbeitung: 2026-10-02 19:35:58 CEST (date). Beginn 2026-10-02 19:02:45 CEST.
