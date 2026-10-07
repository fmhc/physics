# TT-GLAS-2: Plan (Code-Agent, Runde 46, Zweig Glas)

- Code-Agent fuer die Leitung claude-primary. Start 2026-10-05 06:47:39 CEST (date). Plantext ab 07:18:41 CEST (date),
  vor jeder Hauptrechnung und vor Sicht jedes Ergebniswerts. Zeitbox 150 min, also bis 09:17:39 CEST.
- Grundlage: KARTE.md (TG2-0 bis TG2-3; Wortlaut, Schwellen, Wahrscheinlichkeiten und Bedeutung unveraendert).
- Kennzeichen: [M] Mathematik (vorab ableitbar), [E] hier gerechnet, [P] Projektdatei, [F] eigene Festlegung,
  [H] Hypothese, [L] Gedaechtnis. Alles ist synthetische Gitterrechnung, keine Messdaten.

## 1. Ableitbarkeitsprobe

- **Vorab ableitbar [M]:**
  - omega^2(k) = omega^2(-k): Alle Operatoren (B, A, M, c) bei -k sind die komplex konjugierten derer bei k, also auch
    S und die reduzierten Matrizen. Je Paar (k, -k) reicht ein Vertreter.
  - Bei Gamma (k = 0) sind die sechs homogenen Verzerrungen a_e = n_e^T h n_e (h konstant) Nullmoden von B (flacher Torus
    bleibt flach); sie liegen nicht im Bild von M (nicht periodisch), sind zu allen c_v orthogonal (c_v = -B w_v) und
    bleiben daher nach der Projektion Nullmoden von B_red. Erwartet: 6 Nullmoden bei Gamma. Sie sind keine
    Eichnullmoden (die nimmt die Projektion heraus), sondern die k -> 0-Grenzen der akustischen Zweige.
  - Hinreichend fuer Stabilitaet bei einem k: A_red positiv definit und B_red ohne negative Richtung (dann sind alle
    omega^2 reell und >= 0; Sylvester) [M]. Ist A_red positiv definit, ist die Zahl negativer omega^2 gleich der Zahl
    negativer Eigenwerte von B_red.
  - Variante (e) unten ist vorab isotrop: a_h^+ K3 a_h = sum_t V_t / mittleres V |h|^2 (TT-ISO-1 Abschn. 6 [P]) und
    a_h^+ B a_h / k^2 = Kastenvolumen (TT-GLAS-1 Z1 [P, E auf 6 Netzen]). Sie ist nur Pruefung.
  - TG2-0 ist Kontrolle: Variante (a) rechnet dieselben Operatoren mit derselben Reduktion; nur der Weg zur Basis S
    (Householder-QR mit Anwendung auf [0; I] statt vollem Q) und die Bibliothek (torch statt numpy) sind anders. Erwartet
    sind Abweichungen weit unter 1e-3.
  - Fortsetzung des N-Gesetzes (Karte): Erwartung bei N = 1024 etwa 5,9 % [M].
- **Nicht ableitbar:** Vorzeichen der omega^2 bei endlichem k, Anteil von Masse und Relaxation an der Spanne, Verhalten
  des Doppelbrechungsanteils mit N.
- **Rohdaten-Abfrage:** TT-GLAS-1 enthaelt nur kleine k (16 Punkte je Netz) und ein Netz N = 512; keine Datei dort
  enthaelt Werte bei endlichem k, Ritz-Werte oder A3-Werte auf dem Glas.

## 2. Aufgabe 1: Stabilitaet ueber die Brillouin-Zone (code/bz.py)

- **Netze:** tg.zufallsnetz(N, saat), N = 128 und 256, Saaten 1 bis 12 (dieselben wie TT-GLAS-1). Modell unveraendert
  (tg.modell, tg.ops; J = 1, R1).
- **k-Gitter [F]:** k = (2 pi / L) m / 6, m in {0..5}^3 (Superzelle mit Kante L = N^(1/3)); je Paar {m, -m mod 6} ein
  Vertreter: 112 Klassen, davon Gamma und 7 weitere selbstkonjugierte Punkte (m_i in {0, 3}). Das ist das volle
  6^3-Gitter der Karte. Dazu je Netz der Kontrollpunkt [100], |k| = 1e-2.
- **Rechnung je k:** wie tg.punkt, alle Eigenwerte: S = Komplement von Bild[M, c] (ausser Gamma: Householder-QR, Rang aus
  |diag R| > 1e-9 max; bei Gamma oder Rangverlust volle SVD mit Schwelle 1e-9 wie tg); A_red, B_red; ist A_red positiv
  definit (Cholesky), omega^2 = Eigenwerte von L^+ B_red L, sonst allgemeine Eigenwerte von A_red B_red.
- **Klassen je k [F]:** s = max |omega^2|.
  - Nullmode: |omega^2| <= 1e-9 s (Schwelle von ew.py). Erwartet nur bei Gamma (6, siehe 1).
  - wachsend (negativ bzw. wachsend): keine Nullmode und (Re omega^2 < -1e-12 s oder |Im omega^2| > 1e-12 s), wie tg.
  - "Kleinster Eigenwert ohne die Eichnullmoden": min Re omega^2 ueber alle Moden ausser den Nullmoden. Die
    Eichrichtungen (Bild M) und die Regelrichtungen (Bild c) sind durch die Projektion schon entfernt.
  - Dazu je k: Rang von [M, c], Zahl negativer Eigenwerte von B_red (Schwelle -1e-9 max), A_red positiv definit ja/nein.
- **Ort:** m, |k| und Werte jeder wachsenden Mode werden gespeichert.
- **Vollstaendigkeit:** Ein Netz ist vollstaendig, wenn alle 112 Klassen gerechnet sind. Laeufe haben eine Frist von
  540 s (keine neue k-Rechnung danach); fehlende Klassen werden gemeldet.

## 3. Aufgabe 2: Zerlegung der Spanne (code/dk.py), Definition vor der Rechnung

Alle Varianten bei |k| = 1e-2 in den 13 Wuerfelachsen (wie TT-GLAS-1), je zwei TT-Werte omega^2/k^2. P = Komplement von
Bild[M, c] (Basis S), a_h1, a_h2 = die zwei affinen TT-Wellen (h in der TT-Ebene, Frobenius-Norm 1, wie tg.affin),
z = S^+ a_h (die auf P projizierten affinen Wellen, Koordinaten in S).

- **(a) voll:** wie TT-GLAS-1 (R1, A1 mit J = 1): die zwei masselosen positiven Moden von A_red B_red.
- **(b) affin eingefrorene Relaxation, nur Bewegungsenergie [F]:** Rayleigh-Ritz des R1-Modells auf dem Raum der zwei
  projizierten affinen TT-Wellen. Die Lage ist auf die affine Welle eingefroren; Steifigkeit z^+ B_red z, Traegheit mit
  der Lagrange-Masse des R1-Modells z^+ A_red^-1 z (Legendre zu H = 1/2 p^+ A_red p). omega^2_b = Eigenwerte von
  (z^+ A_red^-1 z)^-1 (z^+ B_red z). Die affine Steifigkeit ist isotrop (Z1, hier mitgemessen als z^+ B_red z / (k^2 V));
  die Spanne von (b) misst also die Richtungsabhaengigkeit der Masse der affinen Welle. [M]: Die zwei Ritz-Werte liegen
  ueber den zwei kleinsten Eigenwerten von (a) (Cauchy), soweit (a) sie als TT-Moden fuehrt.
- **(c) isotrope Ersatzmasse, nur Relaxation [F]:** Lagrange-Masse A3 aus EINE-WELT-LOCH-1/TT-ISO-1 je Tetraeder,
  K3_t = (V_t / mittleres V) Phi_t^-T (1 - TR TR^T) Phi_t^-1 (Phi_t: Kantendehnungen aus h, Basis tp.B6), Bloch-assembliert
  wie B. Reduktion R2 (Lage in P, Masse S^+ K3 S). omega^2_c = Paar (B_red, K3_red): mu = Eigenwerte von R^-1 K3_red R^-+
  (B_red = R R^+), omega^2 = 1/mu; die zwei kleinsten positiven masselosen Werte. Fuer die unprojizierte affine TT-Welle
  ist diese Masse exakt isotrop [M], die Steifigkeit auch; Richtungsabhaengigkeit entsteht dann nur durch die Relaxation
  (und durch den Projektionsanteil, siehe d).
  - Warum A3 und R2: Mit der Euklidischen R1-Paarung haengt die affine Traegheit immer an der Kantenrichtungsverteilung;
    eine quadratische lokale Ersatzmasse kann sie dort nicht isotrop machen [M, Kopfrechnung]. A3 mit R2 ist die
    Projektvariante, deren affine Masse auf jeder Triangulierung isotrop ist (TT-ISO-1 Abschn. 6 [P]).
  - Grenze [H]: (c) misst die Relaxation unter der Ersatzmasse und mit R2, nicht dieselbe Relaxation wie in (a).
- **(d) Kontrolle zu (c):** Rayleigh-Ritz von (c) auf z (projizierte affine Wellen). Ihre Spanne zeigt, wie isotrop die
  Ersatzmasse nach der Projektion noch ist (Restanisotropie, die (c) nicht der Relaxation zuschreiben darf).
- **(e) Pruefung [M]:** Rayleigh-Ritz mit B und K3 auf den unprojizierten a_h. Vorab isotrop; nur Kontrolle.
- **Kennzahlen je Netz und Variante:** Spanne = max/min - 1 ueber 26 Werte; Aufspaltung = max_d (w_d2 / w_d1 - 1);
  Richtungsspanne der Zweigmittel = max_d wbar_d / min_d wbar_d - 1; Doppelbrechungsanteil = Aufspaltung / Spanne.
  Dazu je Netz der Projektionsanteil |a_h - S z| / |a_h| und z^+ B_red z / (k^2 V).
- **Gueltigkeit:** (a) regulaer wie TT-GLAS-1 ohne TT-Anteil: an allen 16 Punkten genau 2 masselose positive Moden,
  nichts wachsend oder unklar, linear (|omega^2(2e-2) / (4 omega^2(1e-2)) - 1| <= 0,01). (c) gilt je Netz, wenn an allen
  13 Richtungen genau 2 positive masselose Werte gefunden sind; negative omega^2 von (c) (moeglich, K3 ist indefinit)
  werden gezaehlt und gemeldet. Spannen nur ueber gueltige Netze.
- **Netze:** N = 128 und 256, Saaten 1 bis 12 (dieselben 24 Netze wie Aufgabe 1). Beschreibend auch N = 512 (Aufgabe 3).

## 4. Aufgabe 3: groessere Netze (code/dk.py), Abweichung von der Karte [F]

- **Kein duennbesetzter Loeser:** Rauchtest r1 (05:07 bis 05:09 UTC, nur Laufzeiten) mit Shift-Invert ueber
  KKT-Systeme [[H, X], [X^+, 0]] und splu (code/sz.py): Faktorisierung 7,8 s (N = 256) bzw. 50 s (N = 512) je Matrix,
  Fuellung 6e6 bzw. 2,3e7 Eintraege, also fast dicht (die Spalten c = -B W koppeln Zweitnachbarn). N = 512 haette ~110 s
  je k-Punkt gebraucht, N = 1024 geschaetzt ~8-mal mehr. Stattdessen derselbe dichte Weg wie (a) auf der GPU
  (P4000, complex128): Rauchtest r3 gab 11,4 s je Richtung bei N = 512 (alle Varianten) und 40,8 s bei N = 1024 (nur a),
  GPU-Speicher 0,7 bzw. 2,1 GB. sz.py bleibt als Rauchcode im Ordner und geht in nichts ein.
- **N = 512:** Saaten 1 bis 4, alle Varianten, mit Linearitaet. **N = 1024:** Saaten 1 bis 4, nur (a), ohne
  Linearitaet (Speicher, Zeit), je Netz zwei Laeufe (Richtungen 0 bis 6 und 7 bis 12). Weitere Saaten nur, wenn Zeit
  bleibt (Nachtrag, beschreibend).
- **Kennzahlen:** Spanne, Doppelbrechungsanteil, Richtungsspanne je Netz; Mittel und SD je N; Exponent (Abschn. 6).

## 5. Kontrolle TG2-0

- Verglichen werden (a)-Werte omega^2/k^2 von dk.py (13 Richtungen x 2 Zweige, |k| = 1e-2) fuer N = 128 und 256,
  Saaten 1 bis 12, mit TT-GLAS-1 lauf-69/auswertung.json (sha256 b0d875d6..., netze[].w2k2), und der Kontrollpunkt [100]
  von bz.py (2 Werte je Netz) mit netze[].w2k2[0]. Groesse: max |neu / alt - 1| ueber alle verglichenen Werte.
- Beschreibend: N = 512, Saat 1 gegen TT-GLAS-1 Nachtrag (nachtrag-69/n512/auswertung-n512.json, sha256 5928b5cb...).

## 6. Urteilsregeln (mechanisch in code/tg2_auswertung.py)

- **TG2-0:** nach Plan eingetroffen genau dann, wenn fuer beide N alle 12 Netze verglichen sind (dk.py) und die groesste
  relative Abweichung ueber alle verglichenen Werte (dk.py und bz.py) <= 1e-3 ist; sonst verfehlt; fehlen Netze und ist
  nichts ueber 1e-3, nicht entscheidbar. Nach Kartenwortlaut: groesste Abweichung <= 1e-3 ueber alle verglichenen Werte
  (mindestens ein Netz je N).
- **TG2-1:** nach Plan eingetroffen genau dann, wenn alle 24 Netze vollstaendig sind (112 Klassen) und an keinem Punkt eine
  wachsende Mode liegt; verfehlt, sobald an irgendeinem gerechneten Punkt eines der 24 Netze eine wachsende Mode liegt;
  sonst nicht entscheidbar. Nach Kartenwortlaut ("im ganzen k-Gitter", das die Karte auf "so viele, wie in 10 min
  passen" begrenzt): eingetroffen, wenn fuer alle 24 Netze Laeufe vorliegen und an keinem gerechneten Punkt eine wachsende
  Mode liegt; verfehlt wie nach Plan. Nullmoden bei Gamma zaehlen nicht als wachsend; Nullmoden ausserhalb von Gamma
  werden gemeldet.
- **TG2-2:** Grundlage: Netze mit gueltigem (b) und (c), N = 128 und 256.
  - Nach Plan: eingetroffen genau dann, wenn die mittlere Spanne von (b) bei N = 128 und bei N = 256 jeweils kleiner ist als
    die von (c); verfehlt, wenn sie bei beiden groesser ist; sonst nicht eindeutig (nicht entscheidbar).
  - Nach Kartenwortlaut ("Relaxation traegt mehr als die Haelfte der Spanne (b kleiner als c)"): Mittel ueber alle
    gueltigen Netze beider N: Spanne(b) < Spanne(c) eingetroffen, sonst verfehlt.
  - Beschreibend: Anteil Spanne(c) / (Spanne(b) + Spanne(c)) je Netz; Spanne von (d) und (e).
- **TG2-3:** Grundlage: Netze N = 1024 mit allen 13 Richtungen und regulaerem (a) (ohne Linearitaet). Nach Plan und
  Wortlaut: bei mindestens 4 solchen Netzen eingetroffen genau dann, wenn die mittlere Spanne < 0,07 ist, sonst verfehlt;
  bei weniger als 4 nicht entscheidbar.
- **Exponent (beschreibend):** Gerade ln(Spanne) gegen ln N ueber alle regulaeren (a)-Netze dieses Laufs (N = 128 bis
  1024); dazu mit den TT-GLAS-1-Netzen N = 32, 64 (auswertung.json). Bootstrap ueber Netze je N (2000 Ziehungen, Saat 17).
- Bricht ein Lauf ab oder fehlt ein Netz, gehen nur vorhandene vollstaendige Netze ein.

## 7. Laeufe auf der .69 (kleintest.sh, je Lauf <= 600 s, Frist 540 s in den Skripten)

- Rauchtests vor dem Einfrieren (nur Schluessel und Laufzeiten, Rauchsaat 901): r1 (cpu6, 05:06 bis 05:09 UTC: bz N = 128,
  sz N = 256 und 512), r2 (cpu6, 05:14 bis 05:15: bz N = 128 und 256, dk N = 128 und 256), r3 (p4000a und p4000b,
  05:16 bis 05:17: bz N = 256, dk N = 256, 512, 1024). Laufzeiten je k-Punkt: bz N = 128 CPU 1,3 s, N = 256 CPU 10,9 s,
  GPU 1,25 s (Gamma 12 s, SVD); dk N = 128 CPU 1,8 s, N = 256 GPU 3,4 s, N = 512 GPU 11,4 s, N = 1024 GPU 40,8 s (nur a).
- **Kette A (p4000a):** bz N = 256, Saaten 1 bis 6 (je ein Lauf, ~2,7 min); dk N = 256, Saaten 1 bis 6 (ein Lauf, ~5 min);
  dk N = 512, Saaten 1, 2 (ein Lauf, ~5,5 min); dk N = 1024, Saaten 1, 3 (je zwei Laeufe, ~5 min). Summe ~47 min.
- **Kette B (p4000b):** wie A mit Saaten 7 bis 12 (bz, dk N = 256), 3, 4 (N = 512), 2, 4 (N = 1024). Summe ~47 min.
- **Kette C (cpu6):** bz N = 128, Saaten 1 bis 12 (je ein Lauf, ~2,6 min); dk N = 128, Saaten 1 bis 12 (zwei Laeufe zu
  6 Saaten, ~3 min). Summe ~37 min.
- Schlusszeit aller Ketten: nach 06:50:00 UTC (08:50 CEST) startet kein neuer Lauf. Danach Auswertung
  (tg2_auswertung.py, Bild auf der .69) auf cpu6.
- Ketten werden per ssh im Vordergrund gestartet (kein Dienst, kein Timer, kein nohup); Skripte auf der .69 nur als neue
  Datei und mv.

## 8. Agenten-Vorhersagen (vorab; gehen in kein Urteil ein)

| Nr | Vorhersage | Wahrsch. |
|---|---|---|
| B1 | Auf allen 24 Netzen keine wachsende Mode im 6^3-Gitter | 65 % |
| B2 | Mittlere Spanne (b) kleiner als (c) bei beiden N | 40 % |
| B3 | Mittlere Spanne bei N = 1024 zwischen 4 % und 7 % | 60 % |
| B4 | Doppelbrechungsanteil (Mittel) bei N = 1024 innerhalb +-0,1 des Werts bei N = 256 | 55 % |
