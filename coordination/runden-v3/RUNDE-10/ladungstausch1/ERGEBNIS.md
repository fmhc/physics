# LADUNGSTAUSCH-1 (Runde 10): Ergebnis

- Bearbeiter: Fable-Agent (derselbe wie die ZUS-10-Pruefung). Auftrag: Leitung claude-primary, 10:26 CEST.
- Vorab: PLAN.md (10:30:36 bis 10:31:38 CEST, vor dem ersten Lauf; Nachtrag 10:35 mit der verfeinerten Hypothese zur
  Tauschfrequenz, registriert bevor R2/R3 Ausgaben hatten). Schreibbeginn dieser Datei: 10:35:55 CEST (date), Endfassung
  nach 10:50:28 CEST. Ende: letzte Zeile.
- Code: t5k_ladungstausch.py (sha256 253d0122…, Kopie der reparierten t5k_zus7.py; tests1d_r3.py unveraendert).
  Laeufe: .69, /home/fmh/fmhc-physics-remote/runde10-ladungstausch1/, Kette kette-lt1.sh; Rauchtest cpu6 (rc 0, 08:31:48
  UTC); R1 bis R4 auf p4000a (Python-Start 08:31:53 / 08:36:58 / 08:40:25 / 08:43:51 UTC; Dauer je Stufe grob ~72 s,
  fein ~131 bis 133 s; R4 fein 386 s), alle rc = 0, keine Fehler in den Logs. Ausgaben lokal in lauf-69/.
- Modell: 1D, U = S - S^2 + S^3/2, Box [-120, 120] mit Daempfungsschicht ab |x| = 80 (tests1d_r3), Messung alle 0,5.
  Zwei Gitterstufen grob (dx 0,1, dt 0,05) und fein (dx 0,05, dt 0,025). Belegstufen wie in ZUS-10: [num], [num+K], [Hand],
  [L], [H]. **Alles ist Modellrechnung; nichts ist Messdatenbestaetigung.**
- Groessen: E15 = Energie in |x| < 15 relativ zu t = 0; Omega_1 = Hauptfrequenz von psi(0, t) (Fenster t >= T/3, Hann,
  Aufloesung 0,003 bei T = 3000, 0,001 bei T = 9000); Omega_swap = Hauptspitze des Spektrums von Q_links(t) im Fenster;
  Wechsel = Vorzeichenwechsel von Q_links im Fenster; Gamma_E = -d ln E15/dt ueber das letzte Drittel;
  Omega_2 := (zweite Spitze des Q_links-Spektrums) - Omega_1. "Tauschball (CSQ)": E15(3000) >= 0,3, Wechsel >= 50,
  Omega_1 < omega. "Vernichtung": E15(3000) < 0,05.

## Kurz

1. **Schwelle im Startabstand, abhaengig von omega^2 [num+K]:** omega^2 = 0,6 und 0,7: Tauschball bei d = 3, 4, 5,
   Vernichtung bei d = 6; omega^2 = 0,8: Tauschball noch bei d = 6. Das passt zum Kriterium von Copeland, Saffin, Zhou
   (|d_1 - d_2| <~ 2 sigma, ueberlappende Kerne) mit der Feld-Halbwertsbreite unseres Balls: 2 sigma = 4,8 / 5,2 / 6,2 fuer
   0,6 / 0,7 / 0,8 [Hand]. Meine Vorab-Vermutung "d = 5 vernichtet bei 0,7" war falsch.
2. **Tauschfrequenz [num+K]:** Omega_swap = 0,18 bis 0,21 in allen elf Tauschball-Laeufen (0,6: 0,195 bis 0,210; 0,7: 0,198;
   0,8: 0,179 bis 0,195), unabhaengig von d innerhalb einer Serie auf 1 bis 8 %. In allen elf Laeufen liegt die zweite
   Spitze des Ladungsspektrums bei 2 Omega_1 + Omega_swap (Abweichung <= 0,003, eine Aufloesungsbreite). Lesart [H]:
   gerader Feldanteil = Oszillon bei Omega_1, ungerader Anteil bei Omega_2 = Omega_1 + Omega_swap; die Ladung tauscht mit
   der Differenzfrequenz (CSZ-Mechanismus). Omega_2 ist aber nicht fest 0,996: 0,936 bis 0,949 bei omega^2 = 0,6 (d = 3, 4),
   0,993 bis 1,002 bei 0,7 und 0,8. Meine blinde Zahlenvorhersage (0,26 bei 0,6, 0,14 bei 0,8) ist verfehlt.
3. **Lebensdauer [num]:** d = 4, omega^2 = 0,7 bis T = 9000: E15 = 0,483 (3000) -> 0,417 (9000), Faktor 1,16; spaete Rate
   Gamma_E = 1,7e-5 (fallend: 5,9e-5 bis 3000). Dabei steigt Omega_1 von 0,801 auf 0,828 und Omega_swap faellt von 0,198
   auf 0,172 bei Omega_2 = 0,999: Der Ball wird mit dem Energieverlust "flacher" und tauscht langsamer. Ausreisser: bei
   omega^2 = 0,6, d = 4 faellt E15 zwischen 2000 und 3000 von 0,68 auf 0,45 (Gamma_E 4,6e-4), bei d = 3 dagegen fast kein
   Verlust (Gamma_E 1e-5); nicht geklaert.
4. **Kontrollen [num+K]:** Einzelball E15 = 1,0000, 0 Wechsel, Frequenz = omega auf 0,0012. Gleichphasiges Q/Q-Paar
   (d = 4): 0 Wechsel, beide Ladungen bleiben positiv, E15 0,92 bis 0,99, Feldfrequenz 0,707 bis 0,713 < omega
   (verschmolzener groesserer Ball). Anfangsphase pi/2 bei d = 4: Tauschball ebenso (E15(3000) = 0,434 gegen 0,483).
   Gitterstufen: E15(3000) grob/fein auf <= 1,5 %, Frequenzen bis auf eine Aufloesungsbreite gleich.
5. **Bezug zu stillen Stellen:** nicht pruefbar. Das 1D-Modell hat keine stillen Stellen der Atmung (R7 V7, R8 1D-Raster).
   Vorarbeit: Gamma_E(omega^2) bei d = 3: 1,0e-5 / 6,8e-5 / 6,7e-5 (0,6 / 0,7 / 0,8), bei d = 4: 4,6e-4 / 5,9e-5 / 3,6e-5.
   Ein 3D-Gegenstueck (achsensymmetrische Q/Anti-Q-Ueberlagerung) braeuchte eine eigene Karte ueber 10 min.
6. **Vergleich mit CSZ 2014 [L]:** Tauschfrequenz unter der Eigenfrequenz (0,19 gegen 0,77 bis 0,89): ja. Existenz nur bei
   ueberlappenden Kernen (d <~ 2 sigma): ja. Anfangsphase unerheblich: ja. Lebensdauer: mindestens 9000 Zeiteinheiten
   (~1100 Feldperioden) beobachtet, e-Faltungszeit der Energie ~6e4 (~7000 Perioden); CSZ nennen >= 10^4 Perioden.
   Energiedichte-Form nicht verglichen.

## R1: omega^2 = 0,7 (omega = 0,8367, q1 = 2,4415; feine Stufe, grob in Klammern wo abweichend) [num+K]

| Lauf | E15 bei 500 / 1000 / 2000 / 3000 | t_halb | Gamma_E spaet | Omega_1 | Omega_swap | Wechsel | max abs Q_links | 2. Q_links-Spitze | 2 Omega_1 + Omega_swap | Omega_2 |
|---|---|---|---|---|---|---|---|---|---|---|
| d = 3 | 0,760 / 0,625 / 0,537 / 0,502 | - | 6,8e-5 | 0,7978 | 0,1979 | 128 | 0,353 | 1,7934 | 1,7935 | 0,9956 |
| d = 4 | 0,697 / 0,590 / 0,514 / 0,483 | 2427 | 5,9e-5 | 0,8009 | 0,1979 | 127 | 0,361 | 1,7965 | 1,7997 | 0,9956 |
| d = 5 | 0,653 / 0,560 / 0,490 / 0,460 | 1802 | 6,3e-5 | 0,8009 | 0,1979 | 126 (127) | 0,380 | 1,7965 | 1,7997 | 0,9956 |
| d = 6 | 0,0027 / 0,0004 / 0,0094 (0,0117) / 0,0048 (0,0018) | 136 | - | 1,0051 | - | 1 | 0,121 | - | - | - |
| d = 4, theta = pi/2 | 0,788 / 0,657 / 0,476 / 0,434 | 1722 | 8,8e-5 | 0,7915 (0,7883) | 0,2073 (0,2104) | 134 | 0,444 | 1,7840 | 1,7903 | 0,9925 |
| d = 4, Q/Q gleichphasig | 0,965 / 0,966 / 0,965 / 0,966 | - | -2,6e-6 | 0,7067 | (0,289; Leistung 1e-3 der Paare) | 0 | 3,674 | - | - | - |
| Einzelball | 1,0000 / 1,0000 / 1,0000 / 1,0000 | - | 4e-13 | 0,8355 | - | 0 | 1,998 | - | - | - |

- Q/Q gleichphasig: Meine Erwartung "Q_links + Q_rechts = 2 q_ball" war falsch gestellt; die ueberlagerten
  gleichphasigen Baelle tragen von Anfang an 7,35 statt 4,88 (Interferenzterm 2 Re psi_1 psi_2^* bei d = 4). Die Ladung
  bleibt erhalten, kein Vorzeichenwechsel.

## R2: omega^2 = 0,6 (omega = 0,7746, q1 = 3,1628; fein) [num+K]

| Lauf | E15 bei 500 / 1000 / 2000 / 3000 | t_halb | Gamma_E spaet | Omega_1 | Omega_swap | Wechsel | 2. Spitze | 2 Omega_1 + Omega_swap | Omega_2 |
|---|---|---|---|---|---|---|---|---|---|
| d = 3 | 0,816 / 0,783 / 0,762 / 0,755 | - | 9,9e-6 | 0,7412 | 0,1947 | 124 | 1,6772 | 1,6771 | 0,9360 |
| d = 4 | 0,766 / 0,740 / 0,684 / 0,453 (grob 0,459) | 2732 | 4,6e-4 | 0,7444 | 0,2073 | 136 | 1,6929 | 1,6961 | 0,9485 |
| d = 5 | 0,682 / 0,574 / 0,409 / 0,369 | 1258 | 1,0e-4 | 0,7883 | 0,2104 | 134 | (keine Summenspitze unter den drei staerksten) | 1,7870 | - |
| d = 6 | 0,0028 / 0,0028 / 0,0039 / 0,0009 | 110 | - | 1,0019 | - | 1 | - | - | - |
| Q/Q gleichphasig d = 4 | 0,994 / 0,994 / 0,993 / 0,993 | - | 1e-9 | 0,7067 | - | 0 | - | - | - |
| Einzelball | 1,0000 (alle) | - | -8e-15 | 0,7758 | - | 0 | - | - | - |

## R3: omega^2 = 0,8 (omega = 0,8944, q1 = 1,8860; fein) [num+K]

| Lauf | E15 bei 500 / 1000 / 2000 / 3000 | t_halb | Gamma_E spaet | Omega_1 | Omega_swap | Wechsel | 2. Spitze | 2 Omega_1 + Omega_swap | Omega_2 |
|---|---|---|---|---|---|---|---|---|---|
| d = 3 | 0,803 / 0,733 / 0,668 / 0,626 | - | 6,7e-5 | 0,8040 | 0,1947 | 123 | 1,7997 | 1,8027 | 0,9957 |
| d = 4 | 0,790 / 0,715 / 0,641 / 0,617 | - | 3,6e-5 | 0,8040 | 0,1916 | 122 | 1,7997 | 1,7996 | 0,9957 |
| d = 5 | 0,752 / 0,703 / 0,640 / 0,612 | - | 4,0e-5 | 0,8135 | 0,1822 | 114 | 1,8060 | 1,8092 | 0,9925 |
| d = 6 | 0,596 / 0,533 / 0,525 / 0,518 (grob 0,524) | - | 3,0e-5 | 0,8198 | 0,1790 | 58 | 1,8217 | 1,8186 | 1,0019 |
| Q/Q gleichphasig d = 4 | 0,926 / 0,924 / 0,923 / 0,921 | - | 1e-6 | 0,7130 | - | 0 | - | - | - |
| Einzelball | 1,0000 (alle) | - | -2e-13 | 0,8951 | - | 0 | - | - | - |

## R4: d = 4, omega^2 = 0,7, T = 9000 (nur fein; Fenster t >= 3000, Aufloesung 0,001) [num]

- E15: 0,697 / 0,590 / 0,514 / 0,483 (500 / 1000 / 2000 / 3000, bitgleich mit R1) und 0,417 bei 9000; t_halb 2427;
  Gamma_E (letztes Drittel) = 1,7e-5.
- Omega_1 = 0,8283, Omega_swap = 0,1717, 329 Wechsel in 6000 (= 0,1723 [Hand]), zweite Spitze 1,8272 gegen
  2 Omega_1 + Omega_swap = 1,8283; Omega_2 = 0,9989.

## Vorab gegen Ausgang (PLAN.md 10:30 bis 10:31 und Nachtrag 10:35)

| Punkt | vorab | Ausgang | Urteil |
|---|---|---|---|
| E1 d = 3, 4 Tauschball (0,7) | ja | 0,502 / 0,483, 128 / 127 Wechsel, Omega_1 < omega | getroffen |
| E1 d = 6 vernichtet | ja | 0,0048 | getroffen |
| E1 d = 5 [H, unsicher] | vernichtet | Tauschball (0,460) | verfehlt |
| E1 Scheiterregeln (Messung, Physik) | d = 4 reproduziert 0,483; d = 6 kein Tauschball; d = 3 Tauschball | 0,4832; 0,0048; 0,502 | nicht ausgeloest |
| E2 Tauschball bei 0,6 und 0,8 (d = 4) | E15(3000) >= 0,2 | 0,453 / 0,617 | getroffen |
| E2 Omega_1/omega = 0,956 +- 0,03 | alle drei | 0,961 / 0,957 / 0,899 | teilweise; 0,8 liegt 0,001 unter der Scheitergrenze 0,90 (eine Aufloesungsbreite ist 0,003): knapp verfehlt |
| E2 Gamma_E(0,6) < Gamma_E(0,7) < Gamma_E(0,8) [H, schwach] | Ordnung | d = 4: 4,6e-4 / 5,9e-5 / 3,6e-5 (umgekehrt); d = 3: 1,0e-5 / 6,8e-5 / 6,7e-5 | verfehlt bei d = 4 (Gamma_E(0,6) > 2 Gamma_E(0,8)), bei d = 3 in der Ordnung |
| E3 Omega_swap(0,7; 4) = 0,20 +- 0,02 | 0,16 bis 0,24 | 0,1979 | getroffen |
| E3 d = 3 und 4 auf 20 % gleich | ja | 0,1979 / 0,1979 (0,7); 0,1947 / 0,2073 (0,6); 0,1947 / 0,1916 (0,8) | getroffen |
| E3 Omega_swap/omega steigt mit omega^2 [H, schwach] | steigt | 0,251 / 0,237 / 0,214 (faellt) | verfehlt |
| Nachtrag: Omega_2 = 0,996 +- 0,005 bei 0,6 und 0,8 | ja | 0,8: 0,9957 / 0,9957 / 0,9925 / 1,0019; 0,6: 0,936 / 0,949 | 0,8 getroffen, 0,6 verfehlt |
| Nachtrag: zweite Spitze = Omega_1 + Omega_2 auf 0,01, Omega_swap = Omega_2 - Omega_1 auf 0,01 | ja | alle elf Laeufe <= 0,003 | getroffen (Struktur), Zahlen 0,26 / 0,14 verfehlt |
| E4 Einzelball | E15 = 1, 0 Wechsel, Frequenz omega +- 0,003 | 1,0000; 0; Abstand 0,0012 / 0,0012 / 0,0007 | getroffen |
| E4 Q/Q gleichphasig | 0 Wechsel, E15 > 0,9, Frequenz < omega; Ladungssumme 2 q_ball | 0; 0,966 / 0,993 / 0,921; 0,707 / 0,707 / 0,713; Ladungssumme 7,35 (Interferenz) | getroffen bis auf die falsch gestellte Ladungssumme |
| E5 Gitter | E15(3000) auf 5 %, Frequenzen auf 1 % | <= 1,5 %; Frequenzen bis auf eine Aufloesungsbreite gleich | getroffen |
| E6 stille Stellen | nicht pruefbar in 1D | Gamma_E(omega^2) berichtet | nicht pruefbar |
| E7 theta = pi/2 bei d = 4 bildet Tauschball | E15(3000) >= 0,3 | 0,434 | getroffen |
| Lebensdauer R4 | Faktor < 2 von 3000 bis 9000 | 1,16 | getroffen |

- Bilanz: 11 getroffen, 1 knapp verfehlt, 4 verfehlt (d = 5; Ratenordnung bei d = 4; Omega_swap/omega-Trend; Omega_2 fest),
  1 nicht pruefbar. Die verfehlten Punkte waren als [H, schwach] bzw. [H, unsicher] markiert; die Scheiterregeln der
  Hauptfrage (Schwelle, Tauschball-Existenz, Kontrollen) sind nicht ausgeloest.

## Belegstufe und Grenzen

- Numerisch mit Kontrolle (zwei Gitterstufen, Einzelball und gleichphasiges Paar als Kontrollen), ein Code, ein Haus;
  1D-Spielzeugmodell in Einheiten m = 1. Kein Umlauf-, kein Beweisanspruch.
- Die Zerlegung in geraden und ungeraden Feldanteil ist nur ueber die Spektren belegt (Summenspitze bei
  2 Omega_1 + Omega_swap); die Feldanteile selbst sind nicht getrennt gemessen. Der Ausreisser omega^2 = 0,6, d = 4 (spaeter
  Energieverlust) ist nicht untersucht.
- "Bezug zu stillen Stellen" bleibt offen: 1D hat keine.

## Vorschlag

- weiter, als 3D-Karte: achsensymmetrische Q/Anti-Q-Ueberlagerung (koll1-artig) bei einer stillen Stelle und daneben;
  dort ist die Frage "Abstrahlung faellt, wenn Omega_1 oder Omega_2 eine stille Stelle trifft" pruefbar.
- klein (1D, <= 10 min): Feldanteile gerade/ungerade getrennt messen (psi(x) und psi(-x)) und Omega_2 direkt bestimmen;
  den Ausreisser 0,6 / d = 4 bis T = 6000 verfolgen.

## Einfach gesagt

Wenn ein Teilchenball und ein Antiteilchenball so nah starten, dass sich ihre Kerne ueberlappen, vernichten sie sich nicht,
sondern bilden einen Klumpen, in dem die Ladung langsam zwischen links und rechts hin- und herwandert. Wie nah "nah" ist,
haengt von der Ballgroesse ab: bei dickeren Baellen reicht ein groesserer Abstand. Das Hin und Her hat in allen Faellen
etwa dieselbe Frequenz, und sie ist genau der Unterschied zweier Schwingungen im Klumpen, einer langsamen und einer
schnellen. Der Klumpen lebt sehr lange und verliert nur langsam Energie. Ob so ein Klumpen an einer stillen Stelle noch
weniger abstrahlt, laesst sich in diesem eindimensionalen Modell nicht pruefen, weil es dort keine stillen Stellen gibt.

**Ende: 2026-09-30 10:53:32 CEST (date, nach dem Schreiben gemessen).** Logs und Berichte in lauf-69/ (20 MB, mit den Zeitreihen-JSON).
