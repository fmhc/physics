# GUERTEL-FINN-NETZ-1: Gelingt der Guertel-Trick auch auf Finns Tetraeder-Netz statt auf dem Wuerfelgitter? (Runde 43)

- Leitung claude-primary. Karte und Wahrscheinlichkeiten geschrieben ab 2026-10-04 19:37:53 CEST (date), vor jeder Rechnung.
- **Herkunft:** GUERTEL-FELD-STAB-1 (RUNDE-37/guertel-feld-stab-1/).
  - Ein Einheitsquaternion-Feld (SU(2), Energie haengt nur von q_a . q_b ueber Nachbarn ab) auf einer Z^3-Kugel mit
    Kern (Phi = theta/2) und festem Rand.
  - Auf (12, 24) fuehrt ein Stoss bei 420 bzw. 450 Grad ohne Gittersprung in die umgekehrte Verdrillung,
    E -> E(720 - theta).
  - Robustheit auf (8, 16) und (16, 32) laeuft (GUERTEL-FELD-STAB-2).
- **Finn:** "der Raum ist das Netz" (19:28 bis 19:31); Guertel als Basis kleinster Bewegungen; halber Spin.
- **Frage:** Dasselbe Feld auf Finns Netz: Diamant-Knoten = Tetraedermitten, Nachbarn ueber die geteilten Ecken, also 4
  je Knoten. Gelingt der Guertel-Trick dort ebenso glatt? Wo springt das Feld?
- **Regel Dimensionsvergleich (AGENTS.md):** 3D-Netz; SO(2)-Kontrolle auf demselben Netz.
- Kennzeichen: [M], [E], [L], [H].

## Ableitbarkeitsprobe

**Vorab ableitbar [M]:**
- Im Kontinuum pi_1(SO(3)) = Z_2: 720 Grad lassen sich glatt ablegen, 360 Grad nicht. Fuer SO(2) geht es nie.
- Die Gleichheit E_min = E(720 - theta) folgt aus der Symmetrie q -> -q im Kern (laut GUERTEL-FELD-STAB-1 PLAN, Z. 28 bis
  29), wenn die Energie nur von q_a . q_b abhaengt. Das gilt auch auf Finns Netz.

**Nicht ableitbar:**
- Ob auf dem Diamant-Netz (nur 4 Nachbarn, groessere Bindungswinkel je Ring) der Vorwaertsast bis 450 Grad ueberhaupt ohne
  Sprung existiert.
- Ob der Stoss ohne Gittersprung durchlaeuft.
- Wie die Sprunggrenze theta_max gegen das Wuerfelgitter gleicher Knotenzahl liegt.

## Auftrag (Code-Agent)

1. Code aus guertel-feld-stab-1/code/ (und guertel-2/code/) kopieren und auf einen allgemeinen Nachbargraphen umstellen.
   Dort nichts aendern.
2. **Netz:** Diamant-Knoten in einer Kugel, Kern- und Randradius so gewaehlt, dass die Knotenzahl der Kugel (12, 24) auf
   Z^3 nahekommt; im Plan begruenden.
3. **Kontrolle K0:** derselbe Code auf Z^3 (12, 24) reproduziert GUERTEL-FELD-STAB-1 bei 450 Grad (Energie auf 1e-6
   relativ).
4. **Teil A:** Vorwaertsast auf dem Diamant-Netz in 30-Grad-Schritten bis zum ersten Gittersprung (theta_max).
5. **Teil B:** Stossprotokoll wie GUERTEL-FELD-STAB-1 (eps = 0,01, 0,1, 0,3; Sinusprofil) bei 420 und 450 Grad, sofern
   theta_max > 450 Grad; sonst beim groessten gueltigen theta ueber 360 Grad.
6. **Teil C:** SO(2)-Kontrolle auf dem Diamant-Netz (keine Entdrillung).

## Vorhersagen (vor jeder Rechnung)

| Nr | Vorhersage | Wahrsch. |
|---|---|---|
| GF0 | Kontrollen: K0 auf 1e-6; SO(2) auf dem Diamant-Netz entdrillt nicht | 85 % |
| GF1 | [H] Auf dem Diamant-Netz existiert der Vorwaertsast ohne Sprung bis mindestens 450 Grad (theta_max > 450) | 45 % |
| GF2 | [H] Bei 420 bzw. 450 Grad (oder dem groessten gueltigen theta > 360) fuehren mindestens 2 von 3 Stoessen ohne Gittersprung in die umgekehrte Verdrillung (E auf E(720 - theta) auf 1e-6 relativ) | 50 % |

**Bedeutung (vorab):**
- **GF2 trifft ein:** Der Guertel-Trick gelingt auch auf Finns Tetraeder-Netz. Ein Drehfeld auf seinem Netz kann zwei
  volle Umdrehungen glatt ablegen, eine nicht; das ist die Grundlage fuer halben Spin auf Finns Netz [H].
- **GF2 verfehlt:** Das Diamant-Netz mit nur 4 Nachbarn ist zu grob; der Trick braucht dichtere Netze oder feinere
  Unterteilung.

## Rahmen

- Code-Agent.
- Laeufe nur auf der .69 ueber kleintest.sh, Spuren cpu6 und cpu7 (frei seit ATEM-NETZ-1). Je Lauf <= 10 min
  (Laufzeit vorab messen), 1 Thread. Zeitbox 120 min.
