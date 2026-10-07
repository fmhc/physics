# Runde 9, Karte SD-1: Gegen-Schwappen (Spin-Dipol) im gemischten Ball (Ergebnis)

- Bearbeiter: Anthropic-Code-Agent (Opus). Explorativ, v3.
- Zeiten (CEST, gemessen):
  - Beginn 08:16:07; Plan 08:22:10; Freigabe der Leitung 08:28:19
  - Pause (Nutzungslimit der Leitung) etwa 08:37 bis 09:51; weiter ab 09:56:04
  - Diese Datei ab 10:12:12
- Code: RUNDE-09/sd1/sd1.py (Pruefbelege in PRUEFBELEGE.md, Diff sd1-gegen-gfbic_umlauf.diff).
- Rechenort: .69, runde9-sd1/, Spuren cpu, cpu2 und cpu5, h = 0,02. Ausgaben in lauf-69/.
- Gerechneter Ast: Gegentakt des gemischten Balls (Kanal "anti": dp = U'(S) + g S, sp = -g S/2, natives Profil).
  Gemeint ist der gegenlaeufige l = 1-Partner bei nu ~ omega + sqrt(E), wie in der Freigabe.
- "exakt" heisst: Umlaufzahl +-1 von W auf einem Rechteck um die Stelle, groesster Phasensprung < 0,4 rad. Das ist
  numerische Evidenz im radialen linearen Modell, kein Beweis.
- u' = 1/(omega^2 - omega_c^2); omega_c^2 = 0,44875 bei g = 0,2 und 0,494988 bei g = 0,02 [Hand, bc].

## Kurzfassung

- **Der gegenlaeufige l = 1-Ast hat bei g = 0,2 eine Leiter aus sieben exakten stillen Stellen.** Alle Umlaufzahlen
  sind aufgeloest und wechseln von Stelle zu Stelle das Vorzeichen:
  - 0,505096 (-1) / 0,512706 (+1) / 0,522705 (-1) / 0,536436 (+1) / 0,556504 (-1) / 0,588716 (+1) / 0,649310 (-1)
  - Schritt in u': 2,11 / 2,11 / 2,12 / 2,12 / 2,14 / 2,16
- **Der Ast existiert bis omega^2 ~ 0,674 (g = 0,2) bzw. ~0,742 (g = 0,02).** Oberhalb 0,56 gibt es schmale Pole
  (Gamma 2e-7 bis 5e-6) mit zwei stillen Stellen.
- **Spin-Dipol-Gegenprobe bestanden:** Der gleichlaeufige Partner ist an allen gerechneten Punkten ein reeller,
  gebundener Zustand. D ist dort reell, |D| an der Nullstelle 4e-14 bis 2e-17 relativ.
- **Proben:**
  - l = 0 gibt die zweite Leiter von GF-BIC wieder (Z1, Z2 in Lage und Umlauf).
  - l = 1 im psi_1-Kanal gibt SP-1 wieder.
  - "anti" bei l = 0 gibt ROT-2 wieder.
- Die drei vorhergesagten Stellen (0,515 / 0,525 / 0,539) liegen in ihren Balken. Existenzschwelle, Re nu* und die
  Gegenprobe bei g = 0,02 liegen weit daneben (Abschnitt 5).

## 1. Stille Stellen des gegenlaeufigen l = 1-Asts, g = 0,2

| Stelle | omega*^2 (A_out-Nullstelle) | nu* (W-Fit) | u' | Schritt | Umlauf (+-5e-4 / +-1e-4) | groesster Sprung (rad) | Belegstufe | Laeufe |
|---|---|---|---|---|---|---|---|---|
| 1 | 0,5050963 | 1,587877 | 17,747 | - | -1 / -1 | 0,278 / 0,300 | exakt (Umlauf) | x3; kurve s1 |
| 2 | 0,5127061 | 1,598031 | 15,636 | 2,112 | +1 / +1 | 0,278 / 0,286 | exakt (Umlauf) | t1; kurve s1 |
| 3 | 0,5227046 | 1,611688 | 13,522 | 2,114 | -1 / -1 | 0,295 / 0,279 (neu gelegt) | exakt (Umlauf) | u1; kurve s1 |
| 4 | 0,5364362 | 1,630964 | 11,404 | 2,118 | +1 / +1 | 0,293 / 0,279 (neu gelegt) | exakt (Umlauf) | t2; kurve s1 |
| 5 | 0,5565041 | 1,659970 | 9,280 | 2,124 | -1 / -1 | 0,286 / 0,292 | exakt (Umlauf) | x1 (zentriert); v4 (-1 / Rechteck ohne Stelle 0); kurve s1, r2 |
| 6 | 0,5887158 | 1,707484 | 7,145 | 2,136 | +1 / +1 | 0,289 / 0,289 | exakt (Umlauf) | u2; kurve r2 |
| 7 | 0,6493098 | 1,792567 | 4,986 | 2,159 | -1 / -1 | 0,255 / 0,257 (--u-n 6000) | exakt (Umlauf) | x2 (zentriert); t3 (-1, Sprung 0,404, nicht aufgeloest) |

- Gegenproben je Stelle: A_out-Nullstelle, W-Fit und s(x) = 0 im selben Lauf stimmen auf <= 3e-6 ueberein.
  - d_min/|A'| liegt bei 1e-14 bis 3e-9 (in omega^2).
  - Wo kurve verfeinert hat (Stellen 1, 2, 6; ebenfalls h = 0,02, anderes Gitter), weicht es um <= 2e-7 ab.
- Zwischen den Stellen ist die Breite 1e-7 bis 5e-6 (kurve r2, r3, s1). Oberhalb von Stelle 7 ist s negativ und
  waechst bis zur Schwelle (v3), dort ist keine weitere Stelle gesehen.
- Bei 0,505 und 0,51 gibt es einen zweiten gebundenen l = 1-Zustand (E = 0,988 bei 0,51) und damit einen zweiten
  Ast. Er ist nicht untersucht.
- Stufe: nur h = 0,02. Fuer l = 0 im psi_2-Kanal lag der Unterschied zwischen h = 0,02 und 0,01 laut R9 (VE1) bei
  1e-8 in omega^2. Fuer l = 1 im Gegentakt ist das nicht geprueft.

## 2. Existenzschwelle des Asts

- Kriterium: Der l = 1-Hohlraumzustand ist gebunden (E < 1). Gleichwertig: Der gleichlaeufige Partner liegt unter der
  Kante 1 - omega, der Gegenlaeufer unter 1 + omega.

| g | letzter Punkt mit Zustand (E) | erster ohne | Schwelle [Hand, E linear bis 1] | aus kurve (Fenster bis 1 + omega - 0,002) |
|---|---|---|---|---|
| 0,2 | 0,673 (E = 0,99878) | 0,674 | 0,6743 +- 0,0005 | Kandidat bei 0,668, keiner ab 0,670 |
| 0,02 | 0,74 (E = 0,99703) | 0,75 | 0,742 +- 0,002 | Kandidat bei 0,72, keiner ab 0,74 |

- Bei 0,674 kann ein Zustand noch knapp unter der Kante liegen, weil das nu-Raster 5e-4 vor der Kante endet. Die
  Schwelle steht deshalb als Intervall da.
- E(omega^2) bei g = 0,2 (gebunden, v1 und w1):
  - 0,51: 0,762 / 0,52: 0,774 / 0,54: 0,802 / 0,56: 0,832 / 0,60: 0,896 / 0,64: 0,958 / 0,66: 0,985 / 0,665: 0,991 /
    0,67: 0,996 / 0,671: 0,997 / 0,672: 0,998 / 0,673: 0,999
- E bei g = 0,02 (v2 und w2):
  - 0,60: 0,701 / 0,65: 0,818 / 0,70: 0,930 / 0,71: 0,949 / 0,72: 0,967 / 0,73: 0,983 / 0,74: 0,997
- Abstand der Schwelle ueber omega_c^2: 0,226 (g = 0,2) und 0,247 (g = 0,02).

## 3. Schmale Pole oberhalb 0,56 (g = 0,2)

- Der Gegenlaeufer-Pol existiert an jedem gerechneten Punkt von 0,56 bis 0,668 (kurve r2, r3, v3).
- Gamma dort: 7,7e-7 (0,56) / 4,2e-6 / 1,6e-6 / 3,3e-8 (0,59) / 1,7e-6 / 3,1e-6 / 2,6e-6 / 1,3e-6 / 2,7e-7 (0,64) /
  ~0 (0,65, Pol-Im +7,7e-11) / 2,1e-7 (0,66) / 4,4e-7 (0,668)
- Re nu liegt bei omega + sqrt(E) plus 1e-3 bis 7e-3 Kopplungsverschiebung, zum Beispiel 1,72406 gegen 1,72101 bei 0,60.
- Stille Stellen oberhalb 0,56: 0,588716 (+1) und 0,649310 (-1), exakt.

## 4. Spin-Dipol-Gegenprobe (gleichlaeufiger Partner, nu = sqrt(E) - omega, gespiegelt omega - sqrt(E))

- An allen 12 Punkten mit g = 0,2 (0,51 bis 0,673) und allen 7 mit g = 0,02 (0,60 bis 0,74) gibt es genau eine reelle
  Nullstelle von D in (0, 1 - omega); bei 0,51 zusaetzlich eine zweite. Oberhalb der Schwelle (0,674; 0,75 / 0,80 /
  0,85) gibt es keine.
- Auf der reellen Achse ist D dort reell (|Im D|/|D| = 0). |D| an der Nullstelle betraegt 4e-14 bis 2e-17 des Maximums.
- Das ist ein reeller Eigenwert, also ohne Breite. Beide Kanaele sind geschlossen; das passt zur Kanalzaehlung.
- Grenze: Eine Konturzaehlung um die Nullstelle gibt es hier nicht (D ist unter der Kante fuer Im nu != 0 keine
  Fortsetzung, PLAN.md Nachtrag). Belegt ist also "reelle Nullstelle", nicht "kein Pol in der Naehe".

## 5. Eigener Vergleich mit VORHERSAGEN-SD1 (eingefroren 08:28:19)

Den massgeblichen Vergleich macht die Leitung. Hier die Messwerte je Regel, Wortlaut aus der Datei.

| Regel / Vorhersage | vorhergesagt | gemessen | nach Wortlaut |
|---|---|---|---|
| Stelle m = 8 | 0,515 +- 0,004 | 0,512706 (+1) | im Balken (2,3e-3 daneben) |
| Stelle m = 7 | 0,525 +- 0,004 | 0,522705 (-1) | im Balken (2,3e-3 daneben) |
| Stelle m = 6 | 0,539 +- 0,004, "nur falls der Ast dort existiert" | 0,536436 (+1) | im Balken (2,6e-3 daneben) |
| Re nu* | 1,684 / 1,706 / 1,722, je +- 0,01 | 1,598031 / 1,611688 / 1,630964 | ausserhalb (0,086 bis 0,094 zu tief; E um ~0,17 zu hoch angesetzt) |
| Umlauf: Nachbarn entgegengesetzt | ja | alle sieben abwechselnd | erfuellt |
| Existenz nur unter 0,540 bis 0,548 | Schwelle 0,5395 bis 0,548 | 0,6743 +- 0,0005 | verfehlt |
| Regel 1a: schmaler Pol oberhalb 0,56 widerlegt die Plateauverschiebung Delta | kein solcher Pol | viele (Abschnitt 3) | ausgeloest |
| Regel 1b: kein Pol unter 0,535 widerlegt das Hohlraumbild | Pol vorhanden | Pole ab 0,505 | nicht ausgeloest |
| Regel 2a: keine Nullstelle in 0,51 bis 0,545 | Nullstellen | drei, exakt | nicht ausgeloest |
| Regel 2b: eine gefundene Stelle mehr als 0,012 von der naechsten vorhergesagten widerlegt die Lommel-Formel | - | 0,556504 (0,0175 von 0,539), 0,588716, 0,649310 | nach Wortlaut ausgeloest; die Stellen liegen oberhalb der vorhergesagten Schwelle. Ob die Regel dort gilt, entscheidet die Leitung |
| Regel 3: Schritt in 1/(x - 0,44875) ausserhalb 1,6 bis 2,5 | 2,00 und 2,13 (Hand) | 2,11 bis 2,16 | nicht ausgeloest |
| Regel 4: zwei benachbarte aufgeloeste Stellen mit gleicher Umlaufzahl | - | keine | nicht ausgeloest |
| Regel 5 (optional): l = 1 in der Mitte zwischen l = 0-Stellen, Abweichung < 0,25 pi | - | Anteil 0,55 bis 0,71 des Schritts, also 0,05 bis 0,21 Schritt neben der Mitte (Tabelle unten) | nicht ausgeloest, schwach belegt |
| Gegenprobe (a): Schwelle bei g = 0,02 | 0,629 +- 0,01 | 0,742 +- 0,002 | verfehlt; der Fall "nur 0,09 bis 0,10 ueber omega_c^2" tritt nicht ein (0,247) |
| Gegenprobe (a): Breiten ~ g^2 | ja | g = 0,02: 1e-9 bis 2e-8; g = 0,2: 1e-7 bis 5e-6 | Groessenordnung passt, kein sauberer Test (E und Lage der Nullstellen verschieben sich mit g) |
| Gegenprobe (b): Spin-Dipol reell | ja | reell (Abschnitt 4) | bestanden |
| "Kandidat Delta = 0 (kuenstlich)": 0,5924 / 0,5567 / 0,5350, Schwelle 0,600 | nur zur Einordnung | 0,588716 / 0,556504 / 0,536436, Schwelle 0,674 | Lagen nahe; nicht als Vorhersage gewertet |

**Regel 5, Tabelle.** l = 0-Gegenlaeufer des Gegentakts bei g = 0,2 (kurve y1, y2); fein = Feinverfahren, sonst
lineare Interpolation des Grobrasters (|s| < 1e-4, unsicher):

| l = 0 (u') | 18,905 fein | 16,809 fein | 14,760 | 12,682 | 10,576 | 8,485 | 6,426 fein | ~4,40 (Rand) |
|---|---|---|---|---|---|---|---|---|
| l = 1 dazwischen (u') | 17,747 | 15,636 | 13,522 | 11,404 | 9,280 | 7,145 | 4,986 | |
| Anteil des Schritts vom oberen l = 0-Punkt | 0,55 | 0,57 | 0,60 | 0,61 | 0,62 | 0,65 | 0,71 | |

## 6. Meine eigene Vorab-Erwartung (PLAN.md, 08:22) gegen den Ausgang

- E1 bis E4 galten dem psi_2-Kanal um den einkomponentigen Ball; psi_2 mit l = 1 ist nicht gerechnet.
- E1 (Schwelle x_c = 0,66 +- 0,04): Der Gegentakt geht fuer g -> 0 in den psi_2-Kanal ueber. Seine Schwelle liegt bei
  g = 0,02 bei 0,742 und laeuft von g = 0,2 nach 0,02 um +0,068. Linear nach g = 0 fortgesetzt ergibt sich ~0,75
  [Hand]. **Damit ist E1 verfehlt** (das hergeleitete Fenster reichte bis 0,70).
- E2 bis E4: nicht geprueft.
- E5 (Proben): getroffen (Q0 bis Q3, dazu Q5).

## 7. Grenzen

- Alles linear, radiales Modell mit abgeschnittenem Rand, nur Stufe h = 0,02.
- Ob eine m = +-1-Anregung an einer stillen Stelle nichtlinear lange lebt, ist nicht gerechnet. Ein langlebiger
  ganzzahliger innerer Drehimpuls bleibt Hypothese [H].
- Die Stellen 1 bis 4 liegen im Duennwandbereich (R_halb bis ~13). Kernwachstum dort bis 2e5; alle Umlaeufe blieben
  aufloesbar.
- Das Grobraster-Vorzeichen von s taugte bei |s| < 1e-4 nur als Hinweis. Die Lagen 3 und 4 aus kurve (lineare Interpolation) lagen um
  4e-4 bzw. 2e-4 daneben; exakt hat sie selbst gefunden (neu gelegt).
- Der zweite l = 1-Ast unter 0,51 und die Stellen des l = 0-Gegentakts sind nur gestreift.
- Werkzeug: Der erste gebunden-Lauf mit 12 Profilen brauchte ueber 10 min und wurde von der Unit beendet (r1, keine
  Ausgabe). Die Fassung e4b52881 bisektiert alle Klammern gemeinsam. Ausserdem scheiterte s2 am Profil bei 0,52, zu
  nahe an omega_c^2(0,02) = 0,495.

## 8. Laeufe (.69, Zeiten UTC aus den Berichten)

| Lauf | Zweck | Start | Ende |
|---|---|---|---|
| q0 | Probe punkt Z1, l = 0 | 06:31:23 | 06:36:53 |
| q2 | Probe kurve psi2, l = 0 | 06:36:55 | 06:42:58 |
| s1 | kurve anti g 0,2 l 1, 0,505 bis 0,555 | 06:43:01 | 06:45:34 |
| q1 | Probe exakt psi2 Z2 | 06:46:59 | 06:49:21 |
| s2 | gebunden g 0,02 (Profil 0,52 scheiterte) | 06:49:24 | 06:49:24 |
| s3 | kurve anti g 0,02 l 1, 0,56 bis 0,70 | 06:49:33 | 06:50:17 |
| q5 | Probe anti l = 0 gegen ROT-2 | 06:50:23 | 06:51:14 |
| q3 | Probe psi1 l = 1 gegen SP-1 | 06:50:29 | 06:51:47 |
| r1 | gebunden g 0,2, 12 Profile | (Unit nach 10 min beendet) | 06:50:26 |
| r2 | kurve anti g 0,2 l 1, 0,56 bis 0,64 | 06:55:25 | 06:56:43 |
| r3 | kurve anti g 0,2 l 1, 0,65 bis 0,73 | 07:05:21 | 07:06:04 |
| v1 | gebunden g 0,2, 10 Punkte | 07:59:20 | 08:01:15 |
| t1 / u1 / t2 | exakt 0,5127 / 0,5227 / 0,5364 | 08:00:43 / 08:01:37 / 08:02:12 | 08:02:08 / 08:03:17 / 08:03:47 |
| v2 | gebunden g 0,02 | 08:01:27 | 08:03:08 |
| v3 | kurve Schwelle g 0,2 | 08:03:11 | 08:04:07 |
| u2 / t3 / v4 | exakt 0,5887 / 0,6493 / 0,5565 | 08:03:21 / 08:03:50 / 08:04:11 | 08:04:34 / 08:04:55 / 08:05:32 |
| u3 | kurve anti g 0,02, 0,70 bis 0,84 | 08:04:48 | 08:05:34 |
| w1 / w2 | gebunden Schwelle g 0,2 / 0,02 | 08:04:59 / 08:06:22 | 08:06:10 / 08:07:40 |
| x1 / x2 / x3 | exakt zentriert 0,5565 / 0,6493 / 0,5051 | 08:06:32 / 08:07:48 / 08:09:03 | 08:07:40 / 08:08:59 / 08:10:26 |
| y1 / y2 | kurve anti l = 0, g 0,2 | 08:06:36 / 08:09:40 | 08:09:37 / 08:11:00 |

- Alle Laeufe bis auf r1 (Zeitgrenze) und s2 (Profil) endeten mit rc = 0; jeder blieb unter 10 min.

## Einfach gesagt

In einem Ball aus zwei Feldsorten koennen die beiden Sorten gegeneinander schwappen, die eine nach vorn, die andere nach
hinten. Eine dieser Schwingungen verliert normalerweise langsam Energie nach aussen. Wir haben sieben Ballgroessen
gefunden, bei denen dieser Verlust genau verschwindet; der Zaehltest dreht sich dort abwechselnd links- und rechtsherum,
wie bei der einfachen Atmung. Die drei vorhergesagten Stellen trafen, aber die Schwingung existiert in viel kleineren
Baellen als vorhergesagt, und ihre Frequenz lag deutlich tiefer. Ob sie im vollen Modell wirklich lange weiterschwingt,
ist noch offen.
