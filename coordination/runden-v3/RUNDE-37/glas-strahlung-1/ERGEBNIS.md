# GLAS-STRAHLUNG-1: Ergebnis (Code-Agent fuer die Leitung claude-primary, Runde 48, Glas-Zweig)

- **Ablauf (Zeiten per date; .69 in UTC, CEST = UTC + 2):**
  - Start 2026-10-05 09:03:22 CEST. Code kopiert 09:15:37 CEST. Rauchtests r1 bis r6 07:23:02 bis 07:26:11 UTC
    (Rauchsaaten 901, 902; gelesen nur rc, Laufzeiten, Speicher, Schluessel). Plantext ab 09:23:55 CEST.
  - **Eingefroren 09:28:35 CEST:** PLAN.md.eingefroren-20261005-092835 (sha256 e2491831...), code/gs.py (b95f74dd...),
    dazu tg.py, dz.py, ew.py, tp.py, pn.py, mn.py, inz.py, nachtrag_iso.py, nachtrag_umkreis.py, dk.py (unveraendert aus
    TT-GLAS-1/2 und IMPULS-NETZ-1, gleiche Summen wie dort) und die vier Laufketten. Liste EINGEFROREN-SHA256.txt; auf der
    .69 besteht sha256sum -c fuer alle 15 Code-Dateien (EINGEFROREN-SHA256-69.txt).
  - Laufketten 07:28:47 bis 07:51:08 UTC, alle 14 Laeufe rc = 0. **Erste Sicht auf Werte 09:34:02 CEST** (Zwischen-
    auswertung V, N = 128, 256 mit dem eingefrorenen Code). Endauswertung AUS 07:51:23 bis 07:51:33 UTC.
  - Nachtraege nach Sicht (beschreibend, aendern kein Urteil): code/nachtrag_ikosaeder.py (sha256 4853151d...; exaktes
    Lagenmittel), code/nachtrag_v_j1.py (9069312e...; Netz V mit J = 1), nach dem Gegenlesen code/nachtrag_v_kl.py
    (a6079e59...; Netz V, kl = 0,005 bis 0,04).
  - Text ab 09:58:26 CEST (date). Frischer Gegenleser 10:02:54 bis 10:12:50 CEST (Abschnitt 9).
- Alles ist synthetische Gitterrechnung (numpy 2.4.4, torch 2.5.1+cu121; Quadro P4000 complex128 bzw. 1 CPU-Kern), keine
  Messdaten. Messzahlen (Doppelpulsar, GW170817) nur in Abschnitt 5, aus Projektdateien [P].
- **Kennzeichen:** [E] gerechnet, [M] eigene Mathematik (vorab), [P] Projektdatei, [ES] eigener Schluss, [H] Hypothese,
  [F] Festlegung im Plan, [Kopfrechnung].
- **Begriffe:** G = G_rad/G_N einer Kreisbahn (V1+S+J, Materie-Gewichte P1, Goldene Regel bei linearer Dispersion je
  TT-Mode, PLAN 1.4). Lage = Bahnnormale m (24 feste, PLAN 1.5). Streuung = Standardabweichung von G ueber die 24 Lagen
  je Netz. Glasnetze = TT-GLAS-Netze (gleiche Saaten), Bewegungsgewichte J = 1; Netz V mit J_iso.

## 1. Zeiten und Laeufe

Arbeitsordner /home/fmh/fmhc-physics-remote/glas-strahlung-1/, alle Laeufe ueber kleintest.sh (1 Thread, RuntimeMaxSec 600).
Start = Aufruf von kleintest.sh (einschliesslich Wartezeit auf den Spur-Lock), Laufzeit = Dienstlaufzeit.

| Lauf | Spur | Aufruf (code/gs.py ...) | Start bis Ende (UTC) | Laufzeit | rc |
|---|---|---|---|---|---|
| r1 | cpu | code-r1: netz --N 0 --nt 2 --nphi 4 (Rauch) | 07:23:02 bis 07:23:06 | 3,9 s | 0 |
| r2 | cpu | code-r1: netz --N 128 --saaten 901,902 --nt 2 --nphi 4 (Rauch) | 07:23:06 bis 07:23:24 | 17,5 s | 0 |
| r3 | p4000a | code-r1: netz --N 512 --saaten 901 --nt 2 --nphi 4 (Rauch) | 07:23:02 bis 07:23:43 | 40,1 s | 0 |
| r4 | p4000b | code-r1: netz --N 256 --saaten 901 --nt 2 --nphi 4 (Rauch) | 07:23:02 bis 07:23:13 | 10,6 s | 0 |
| r5, r6 | cpu | code-r1 bzw. code-r2: aus auf den Rauchdateien | 07:23:43 bis 07:23:49; 07:26:05 bis 07:26:11 | 6,3 s; 6,3 s | 0; 0 |
| GV | cpu | netz --N 0 --nt 10 --nphi 20 --out lauf/v.json (GS0) | 07:28:47 bis 07:28:55 | 7,5 s | 0 |
| GV6 | cpu | netz --N 0 --nt 6 --nphi 12 (Quadratur, beschreibend) | 07:28:55 bis 07:29:00 | 5,1 s | 0 |
| C128a | cpu | netz --N 128 --saaten 1,2,3,4 | 07:29:00 bis 07:33:04 | 243,5 s | 0 |
| C128b | cpu7 | netz --N 128 --saaten 5,6,7,8 | 07:28:47 bis 07:32:50 | 242,9 s | 0 |
| Q128 | cpu | netz --N 128 --saaten 1 --nt 8 --nphi 16 (beschreibend) | 07:33:04 bis 07:34:52 | 108,2 s | 0 |
| K128 | cpu7 | netz --N 128 --saaten 1 --kabs 0.02 (beschreibend) | 07:32:50 bis 07:33:53 | 62,8 s | 0 |
| A256 | p4000a | netz --N 256 --saaten 1,2,3,4 | 07:28:47 bis 07:32:25 | 217,9 s | 0 |
| B256 | p4000b | netz --N 256 --saaten 5,6,7,8 | 07:28:47 bis 07:32:33 | 225,3 s | 0 |
| A512-1, -3, -5 | p4000a | netz --N 512 --saaten 1 bzw. 3, 5 | 07:32:25 bis 07:51:08 | 360,0 s; 382,8 s; 380,2 s | 0 |
| B512-2, -4, -6 | p4000b | netz --N 512 --saaten 2 bzw. 4, 6 | 07:32:33 bis 07:50:09 | 354,5 s; 349,5 s; 351,8 s | 0 |
| ZW | cpu7 | aus auf V, N = 128, 256 (Zwischenauswertung, nicht in der Laufliste) | 07:33:25 bis 07:34:02 | 8,5 s | 0 |
| AUSK | cpu | aus --v lauf/kontrolle/v-6x12.json --ein q8x16, k002 (beschreibend) | 07:35:52 bis 07:35:56 | 3,6 s | 0 |
| **AUS** | cpu | aus --v lauf/v.json --ein lauf/gs-N*.json (22 Netze) | 07:51:23 bis 07:51:33 | 9,4 s | 0 |
| NI | cpu | nachtrag-code/nachtrag_ikosaeder.py (Nachtrag) | 07:51:33 bis 07:51:38 | 5,0 s | 0 |
| NVJ1 | cpu | nachtrag-code2/nachtrag_v_j1.py (Nachtrag) | 07:56:25 bis 07:56:32 | 7,3 s | 0 |
| NVKL | cpu | nachtrag-code3/nachtrag_v_kl.py (Nachtrag nach dem Gegenlesen) | 08:19:09 bis 08:19:29 | 20,1 s | 0 |

- Alle 22 Glasnetze vollstaendig (36 von 36 Richtungen, keine Frist). N = 512: GPU-Spitze 0,70 bis 0,73 GB, RAM 1,1 GB,
  8,7 bis 10 s je k. Keine Abweichung von der Laufliste ausser der Zwischenauswertung ZW (Selbstanzeige 3).

## 2. Ergebnis zuerst

1. **Die Lagenabhaengigkeit faellt mit N [E]: GS1 eingetroffen.** Streuung von G ueber die 24 Bahnlagen im Mittel
   1,71 % (N = 128), 1,16 % (256), 0,62 % (512); Steigung im Bereich N = 128 bis 512 -0,71 (alle 22 Netze; Bootstrap-95 %:
   -0,90 bis -0,52), durch die Mittel -0,74. Bei N = 512 ist die Streuung noch rund 47-mal die Doppelpulsar-Schranke
   1,3e-4; die Gerade erreicht sie bei N ~ 1e5 (mit N^-0,5: ~1e6) [Kopfrechnung].
2. **Der Mittelwert ist bei N = 512 innerhalb 1e-3 bei 1 [E]: GS2 eingetroffen.** Planmass (24 Lagen, 6 Netze):
   1,000058 (Standardfehler 3,4e-4). Das exakte Lagenmittel (Nachtrag, 6 Ikosaeder-Achsen, Polynom vom Grad 4) ist
   1,00051 +- 0,00006 und faellt wie ~N^-1 (1,00217 / 1,00112 / 1,00051). Es liegt also unter 1e-3, aber noch ueber 1,3e-4.
3. **Ein isotroper V1-Rest ist bis N = 512 nicht nachweisbar [E]: GS3 nicht eingetroffen**, wie aus Symmetrie und
   Zentralem Grenzwertsatz vorab erwartet (PLAN 4). Der V1-Zuwachs des exakten Mittels ist bei allen N mit null
   vertraeglich (-7,5e-5 +- 9,0e-5; -5,0e-5 +- 4,7e-5; +0,07e-5 +- 1,4e-5; bei N = 512 also betragsmaessig unter 3e-5,
   2 Standardfehler). Die Mittelwert-Abweichung faellt von 2,95e-3 auf 5,8e-5 (Plan) bzw. von 2,17e-3 auf 5,1e-4 (exakt).
   Der Rest des exakten Mittels bei N = 512 sitzt im Laengs-Quer-Kanal L (57 %), im TT-Kanal (30 %; vertraeglich mit dem
   Jensen-Anteil der anisotropen Tempi) und im nn-Kanal (13 %).
4. **Kontrolle GS0 eingetroffen [E]:** Auf V gibt der Glas-Code 1,029655 / 1,004000 / 0,967463 (IMPULS-NETZ-1:
   1,029661 / 1,004005 / 0,967468), Abweichung <= 6,4e-6. G_N = G auf dem Glas auf 1,8e-5 (vorab abgeleitet).
5. **Nebenbefund auf V (Kontrolllauf GV, beschreibend, noch ohne eigenen Gegenleser des Nachtrags) [E]:** Mit dem
   Energiekanal V1 heben sich fuer Kreisbahnen nn-Leck und V1 auf V (J_iso) fast ganz auf: G = 0,999985 bis 1,000003
   ueber 24 Lagen (Streuung 4,8e-6), statt 0,998498 bis 1,001216 ohne V1 (Streuung 7,2e-4; IMPULS-NETZ-1 rechnete Bahnen
   ohne V1). Der Lagengang ist k-konvergiert (Spanne 1,8e-5 bis 1,9e-5 bei kl = 0,005 bis 0,02; Nachtrag NVKL); der groesste Betrag
   abs(G - 1) ist 1,5e-5 bei kl = 0,01 und 1,2e-5 bei kl = 0,005, also 9- bis 11-mal unter 1,3e-4. Mit J = 1 auf V
   (Nachtrag) gilt das nicht mehr (Streuung 1,25e-3), und auf dem Glas (J = 1) auch nicht: Dort koppeln L und nn+V1.

## 3. Urteile

Mechanisch durch code/gs.py aus (eingefroren 09:28:35 CEST), aus-69/auswertung.json; Regeln PLAN 5.

| Nr | Vorhersage (Karte) | Wahrsch. | nach Plan | nach Kartenwortlaut | tragende Zahlen [E] |
|---|---|---|---|---|---|
| GS0 | Kontrolle: Code gibt auf V 1,030 / 1,004 / 0,967 auf 1e-3 wieder | 90 % | **eingetroffen** | **eingetroffen** | 1,0296546 / 1,0039999 / 0,9674632; gegen h1.json -6,4e-6 / -5,2e-6 / -5,2e-6; gegen Karte -3,5e-4 / -6,5e-8 / +4,6e-4 |
| GS1 | [H] Streuung ueber die Bahnlagen faellt mindestens wie N^-0,4 (N = 128 bis 512) | 60 % | **eingetroffen** | **eingetroffen** | Steigung -0,705 (22 Netze), -0,736 (durch die drei Mittel 0,01711 / 0,01165 / 0,00617) |
| GS2 | [H] Mittel ueber Lagen und Saaten bei N = 512 innerhalb 1e-3 bei 1 | 45 % | **eingetroffen** | **eingetroffen** | 1,0000583 (6 Netze x 24 Lagen); Standardfehler 3,4e-4 |
| GS3 | [H] V1 traegt einen isotropen Rest, der mit N nicht faellt (Mittelwert-Abweichung bei N = 128 und 512 gleich auf 30 %) | 40 % | **nicht eingetroffen** | **nicht eingetroffen** | D_128 = +2,95e-3, D_512 = +5,8e-5 (Quotient 0,02); V1-Zuwachs -4,5e-4 und +1,6e-4 (Quotient -0,35, Standardfehler bei 512: 5,2e-4) |

- **Bedeutung, wie auf der Karte vorab festgelegt:**
  - "GS1 trifft ein: Im Glas-Zweig verschwindet die Lagenabhaengigkeit der Abstrahlung von selbst. GW170817 und die
    Lagen-Schranke des Doppelpulsars waeren dann ohne Abstimmung erfuellt [H]." **Ausgeloest.** Einschraenkung: Bei
    gerechnetem N liegt die Streuung noch 47-mal ueber der Schranke; "von selbst" heisst hier: ueber die Punktzahl
    (Abschnitt 5).
  - "GS2 trifft ein: Auch der Betrag passt im Rahmen der Rechengenauigkeit. Der Doppelpulsar-Betrag (1,3e-4) braucht dann
    groessere N." **Ausgeloest.** Das exakte Mittel (5,1e-4) bestaetigt den zweiten Satz.
  - "GS3 trifft ein: Es bleibt ein isotroper Rest ..." **Nicht ausgeloest.**
- **Ableitbarkeit:**
  - GS0 war vorab ableitbar (PLAN 2: gleiche Physik, andere Auswertung; erwartet <= 1e-4). Keine Messung.
  - G_N = G war vorab abgeleitet (PLAN 4: lineare Praezision des umkreisbasierten Laplace). Gerechnet: 1 + 1,2e-5 bis
    1 + 1,8e-5 (O(k^2), mit kabs = 0,02 viermal so gross: 5,7e-5). Keine Messung.
  - GS1 war nach der Kette (PLAN 4) wahrscheinlich, aber nicht abgeleitet. Die Steigung -0,7 liegt zwischen den beiden
    vorab genannten Faellen (-0,5 linear, -1 quadratisch).
  - GS3: Die Kette (Helizitaet plus Zentraler Grenzwertsatz) sagte "verfehlt" voraus; so ist es gekommen. GS3 war damit
    weitgehend vorab ableitbar; die Rechnung bestaetigt die Kette, sie misst keinen neuen Effekt. Berichtigung der Kette
    (Gegenleser C2): Ueber die Lagen fallen nur die Kreuzterme von V1 mit TT und L exakt weg; der Kreuzterm mit dem
    nn-Teil bleibt (beide ~ n.S.n). Er faellt nach demselben Argument wie ~N^-1; gemessen ist die Korrelation nn/V1 etwa
    -0,87 (4.4). Der Schluss aendert sich nicht.
  - GS2 war nicht ableitbar. Das Planmass ist verrauscht (Stichprobenfehler der 24 Lagen, Abschnitt 4.3); das Urteil haengt
    daran nicht, weil auch das exakte Mittel unter 1e-3 liegt.
- **Agenten-Erwartungen (PLAN 7, kein Urteil):** A1 (GS0 auf <= 1e-4) eingetroffen (6,4e-6). A2 (G_N/G in [0,999; 1,001])
  eingetroffen. A3 (Steigung zwischen -0,7 und -0,3) knapp verfehlt (-0,705). A4 (V1-Zuwachs bei 512 betragsmaessig
  kleiner als halb so gross wie bei 128) eingetroffen (1,6e-4 gegen 4,5e-4; exakt 0,07e-5 gegen 7,5e-5).

## 4. Tabellen

### 4.1 G_rad/G_N je N, Saat und Lage (V1+S+J, P1; Punkt als Dezimalzeichen; mit jq auf der .69 aus aus/auswertung.json formatiert, jq-69/tabelle-lagen.md)

N = 128:

| Lage | Summe m^4 | s1 | s2 | s3 | s4 | s5 | s6 | s7 | s8 |
|---|---|---|---|---|---|---|---|---|---|
| 001 | 1 | 1.01772 | 1.00085 | 1.03471 | 1.00764 | 1.00487 | 1.00379 | 0.99836 | 0.99378 |
| 111 | 0.333 | 1.01448 | 1.00647 | 0.99558 | 0.97858 | 0.98531 | 1.05495 | 1.0233 | 0.99006 |
| 110 | 0.5 | 1.00173 | 0.9956 | 0.9731 | 0.99241 | 0.99643 | 1.01162 | 1.0097 | 1.00106 |
| 123 | 0.5 | 1.01164 | 0.99763 | 1.01999 | 0.97531 | 0.98988 | 1.0496 | 1.01962 | 0.9818 |
| z0 | 0.467 | 0.98921 | 0.97216 | 1.01922 | 0.98497 | 1.00515 | 1.00086 | 0.99414 | 1.01497 |
| z1 | 0.487 | 0.98371 | 0.99578 | 0.99836 | 0.99584 | 1.0175 | 0.99688 | 0.99598 | 1.0209 |
| z2 | 0.531 | 1.0304 | 1.0255 | 1.01558 | 1.00453 | 0.98954 | 1.04479 | 1.0172 | 0.9926 |
| z3 | 0.427 | 0.97925 | 0.96918 | 1.01434 | 0.97157 | 0.99994 | 1.00782 | 0.99921 | 1.0051 |
| z4 | 0.363 | 0.97901 | 0.97578 | 1.0106 | 0.98098 | 1.00808 | 1.00009 | 0.99506 | 1.01637 |
| z5 | 0.68 | 1.01161 | 1.03341 | 0.97932 | 1.01805 | 1.01112 | 1.01883 | 1.01017 | 1.01976 |
| z6 | 0.457 | 0.99642 | 0.98689 | 0.99948 | 0.9669 | 0.98626 | 1.04512 | 1.01835 | 0.98353 |
| z7 | 0.988 | 1.01596 | 0.99976 | 1.03408 | 1.01037 | 1.00648 | 0.99698 | 0.9957 | 0.99575 |
| y0 | 0.801 | 1.02705 | 1.02127 | 1.03164 | 1.01727 | 0.9995 | 1.01804 | 1.0051 | 0.99177 |
| y1 | 0.453 | 1.01421 | 1.00788 | 0.975 | 0.9855 | 0.98977 | 1.04101 | 1.02129 | 1.00269 |
| y2 | 0.545 | 1.01415 | 1.00886 | 0.9693 | 0.98968 | 0.9936 | 1.03264 | 1.02022 | 1.00793 |
| y3 | 0.569 | 0.98942 | 0.98904 | 0.98869 | 1.00418 | 1.01604 | 0.98072 | 0.99635 | 1.02852 |
| y4 | 0.671 | 1.01308 | 0.99514 | 1.0288 | 0.98031 | 0.99419 | 1.03956 | 1.01426 | 0.98374 |
| y5 | 0.48 | 0.99906 | 1.01959 | 1.0329 | 1.02621 | 1.00447 | 0.9751 | 0.98588 | 0.98362 |
| y6 | 0.542 | 0.99851 | 0.97938 | 1.02435 | 0.96849 | 0.99374 | 1.03514 | 1.01221 | 0.98767 |
| y7 | 0.477 | 1.02081 | 1.00995 | 1.01743 | 0.98504 | 0.98846 | 1.05213 | 1.02065 | 0.98451 |
| y8 | 0.491 | 1.00185 | 1.00713 | 1.03522 | 1.02621 | 1.00312 | 0.96253 | 0.98243 | 0.98667 |
| y9 | 0.372 | 0.99725 | 0.99483 | 1.00238 | 1.01605 | 1.00431 | 0.96824 | 0.98985 | 0.99678 |
| y10 | 0.344 | 0.98173 | 0.97276 | 1.01317 | 0.98204 | 1.00732 | 1.00043 | 0.9943 | 1.02018 |
| y11 | 0.429 | 0.99876 | 0.98936 | 0.99899 | 0.96794 | 0.9861 | 1.04729 | 1.01934 | 0.98386 |
| Mittel | | 1.00363 | 0.99809 | 1.00884 | 0.99317 | 0.99922 | 1.01601 | 1.00578 | 0.9989 |
| Streuung (SD) | | 0.01493 | 0.01723 | 0.02077 | 0.01893 | 0.00957 | 0.02812 | 0.01277 | 0.01454 |

N = 256:

| Lage | Summe m^4 | s1 | s2 | s3 | s4 | s5 | s6 | s7 | s8 |
|---|---|---|---|---|---|---|---|---|---|
| 001 | 1 | 0.98909 | 0.98439 | 0.99281 | 0.98557 | 1.01589 | 0.99578 | 1.01111 | 1.00006 |
| 111 | 0.333 | 0.98871 | 0.9972 | 1.01577 | 1.00773 | 1.00493 | 0.99193 | 1.00569 | 1.00574 |
| 110 | 0.5 | 0.97709 | 0.98175 | 1.01275 | 1.00873 | 1.00599 | 1.01729 | 0.97802 | 1.00949 |
| 123 | 0.5 | 0.99195 | 0.99804 | 1.01025 | 0.99474 | 1.00758 | 0.98604 | 1.01909 | 1.00906 |
| z0 | 0.467 | 1.00034 | 0.99716 | 0.99707 | 0.98649 | 1.00152 | 1.01365 | 1.01857 | 0.99115 |
| z1 | 0.487 | 1.03125 | 1.02804 | 0.99313 | 1.00649 | 0.98313 | 1.00312 | 1.01372 | 0.98825 |
| z2 | 0.531 | 0.99624 | 1.00025 | 1.00269 | 1.00306 | 1.00656 | 0.98169 | 1.0132 | 0.99265 |
| z3 | 0.427 | 1.01492 | 1.01768 | 1.0007 | 0.99271 | 0.99644 | 0.9958 | 1.02405 | 1.00189 |
| z4 | 0.363 | 1.02127 | 1.02138 | 0.99689 | 0.9966 | 0.99041 | 1.00354 | 1.02123 | 0.99166 |
| z5 | 0.68 | 1.02755 | 1.02307 | 0.99277 | 1.02141 | 0.98499 | 0.99117 | 1.00411 | 0.98668 |
| z6 | 0.457 | 0.99273 | 0.99811 | 1.01617 | 1 | 1.00711 | 0.98887 | 1.00955 | 1.01697 |
| z7 | 0.988 | 0.98924 | 0.98298 | 0.99194 | 0.9858 | 1.01621 | 0.9984 | 1.00819 | 1.00038 |
| y0 | 0.801 | 0.99588 | 0.99399 | 0.99478 | 0.99471 | 1.01254 | 0.98325 | 1.0116 | 0.99337 |
| y1 | 0.453 | 0.98377 | 0.99342 | 1.01443 | 1.01359 | 1.00198 | 1.00562 | 0.99159 | 1.00206 |
| y2 | 0.545 | 0.9834 | 0.99285 | 1.01204 | 1.01398 | 0.99991 | 1.01109 | 0.98704 | 0.99999 |
| y3 | 0.569 | 1.00231 | 0.99468 | 0.99435 | 0.99336 | 0.99263 | 1.02945 | 0.9931 | 0.98533 |
| y4 | 0.671 | 0.99087 | 0.99513 | 1.00489 | 0.9892 | 1.00954 | 0.98825 | 1.02187 | 1.00664 |
| y5 | 0.48 | 1.01198 | 1.01451 | 1.0022 | 1.00705 | 0.99824 | 0.98759 | 0.99645 | 1.0109 |
| y6 | 0.542 | 0.99595 | 1.00055 | 1.00666 | 0.98873 | 1.0064 | 0.99095 | 1.02494 | 1.00974 |
| y7 | 0.477 | 0.99156 | 0.99802 | 1.00916 | 0.99882 | 1.00726 | 0.9848 | 1.01594 | 1.00314 |
| y8 | 0.491 | 0.99331 | 0.99127 | 1.00244 | 0.99994 | 1.0086 | 1.00503 | 0.98254 | 1.01497 |
| y9 | 0.372 | 0.98189 | 0.97714 | 1.00402 | 1.0005 | 1.00863 | 1.02217 | 0.97135 | 1.01444 |
| y10 | 0.344 | 1.01254 | 1.01121 | 0.99737 | 0.99219 | 0.99346 | 1.01186 | 1.02006 | 0.98749 |
| y11 | 0.429 | 0.99172 | 0.9975 | 1.01657 | 1.00109 | 1.00704 | 0.98938 | 1.0089 | 1.01586 |
| Mittel | | 0.99815 | 0.9996 | 1.00341 | 0.99927 | 1.00279 | 0.99903 | 1.00633 | 1.00158 |
| Streuung (SD) | | 0.01448 | 0.01335 | 0.00838 | 0.00962 | 0.00885 | 0.01318 | 0.01525 | 0.01006 |

N = 512:

| Lage | Summe m^4 | s1 | s2 | s3 | s4 | s5 | s6 |
|---|---|---|---|---|---|---|---|
| 001 | 1 | 0.98822 | 1.00281 | 0.99985 | 0.98711 | 1.00348 | 0.99983 |
| 111 | 0.333 | 1.00548 | 1.00353 | 1.00153 | 1.00476 | 0.99196 | 1.0036 |
| 110 | 0.5 | 1.01105 | 0.99382 | 1.00826 | 1.00957 | 0.98949 | 0.99997 |
| 123 | 0.5 | 0.99852 | 1.0038 | 0.99798 | 0.99958 | 0.99682 | 1.00054 |
| z0 | 0.467 | 0.99458 | 1.00246 | 0.99015 | 1.00105 | 1.00943 | 0.988 |
| z1 | 0.487 | 1.0001 | 0.99869 | 0.99117 | 1.00774 | 1.00756 | 1.00127 |
| z2 | 0.531 | 1.00122 | 1.01023 | 1.00068 | 0.99435 | 0.99455 | 1.00958 |
| z3 | 0.427 | 0.99779 | 1.00097 | 0.99284 | 1.00681 | 1.00802 | 0.992 |
| z4 | 0.363 | 0.99802 | 1.00046 | 0.99044 | 1.00727 | 1.00881 | 0.99403 |
| z5 | 0.68 | 1.00586 | 1.00565 | 0.99796 | 1.00388 | 1.00147 | 1.01128 |
| z6 | 0.457 | 1.00376 | 1 | 0.99997 | 1.00569 | 0.99479 | 0.99978 |
| z7 | 0.988 | 0.9873 | 1.00209 | 1.00042 | 0.98615 | 1.00399 | 0.99912 |
| y0 | 0.801 | 0.99353 | 1.00785 | 1.00145 | 0.98707 | 0.99855 | 1.00923 |
| y1 | 0.453 | 1.01021 | 1.00126 | 1.00531 | 1.00982 | 0.99144 | 1.00177 |
| y2 | 0.545 | 1.01152 | 1.00079 | 1.00643 | 1.01099 | 0.99222 | 1.00045 |
| y3 | 0.569 | 1.00395 | 1.00132 | 0.9949 | 1.0034 | 1.00579 | 0.98995 |
| y4 | 0.671 | 0.99496 | 1.00374 | 0.99697 | 0.9968 | 1 | 0.9987 |
| y5 | 0.48 | 0.99442 | 0.99834 | 1.0026 | 0.99484 | 1.00427 | 1.00786 |
| y6 | 0.542 | 0.99568 | 1.00249 | 0.99516 | 1.0014 | 1.00282 | 0.99359 |
| y7 | 0.477 | 1.00013 | 1.00609 | 0.99929 | 0.998 | 0.99473 | 1.00445 |
| y8 | 0.491 | 0.99089 | 0.99623 | 1.00781 | 0.98736 | 0.99885 | 1.00242 |
| y9 | 0.372 | 1.00144 | 0.99179 | 1.00956 | 0.99583 | 0.99225 | 0.99822 |
| y10 | 0.344 | 0.99741 | 1.00216 | 0.98897 | 1.00547 | 1.00918 | 0.99056 |
| y11 | 0.429 | 1.00396 | 1.00025 | 1.00017 | 1.00559 | 0.99413 | 1.00038 |
| Mittel | | 0.99958 | 1.00153 | 0.99916 | 1.00044 | 0.99978 | 0.99986 |
| Streuung (SD) | | 0.00664 | 0.00406 | 0.00587 | 0.00776 | 0.00647 | 0.00622 |

- Ein Gang mit Summe m^4 wie auf V (kubisch, l = 4) ist auf dem Glas nicht zu sehen; die Lagenabhaengigkeit ist je Netz
  verschieden (Netzanisotropie) [E, Sichtpruefung der Tabellen].

### 4.2 Mittelwerte und Streuungen je N [E]

| N | Netze | Mittel ueber 24 Lagen und Saaten (Plan) | SD der Netzmittel | mittlere Lagenstreuung | exaktes Lagenmittel +- SE (Nachtrag) | SD der exakten Netzmittel |
|---|---|---|---|---|---|---|
| 128 | 8 | 1,002954 | 0,00720 | 0,01711 | 1,002174 +- 0,000418 | 0,00118 |
| 256 | 8 | 1,001269 | 0,00278 | 0,01165 | 1,001119 +- 0,000124 | 0,00035 |
| 512 | 6 | 1,000058 | 0,00083 | 0,00617 | 1,000511 +- 0,000055 | 0,00014 |

Beschreibende Varianten (Mittel / mittlere Lagenstreuung, 24 Lagen):

| Groesse | N = 128 | N = 256 | N = 512 |
|---|---|---|---|
| V1+S+J, P1 (Hauptgroesse) | 1,00295 / 0,01711 | 1,00127 / 0,01165 | 1,00006 / 0,00617 |
| Kopplungsmass K (ohne c0/c_j, V1 mit eps = 1) | 1,00251 / 0,01926 | 1,00105 / 0,01324 | 0,99973 / 0,00695 |
| S+J (ohne V1) | 1,00340 / 0,01085 | 1,00176 / 0,00630 | 0,99990 / 0,00435 |
| nur TT-Anteil der Quelle | 1,00039 / 0,00257 | 1,00022 / 0,00180 | 1,00033 / 0,00098 |
| ohne J (V1+S) | 1,00136 / 0,02147 | 1,00086 / 0,01941 | 0,99995 / 0,00880 |
| umkreisbasiert, V1+S+J (Nebenarm) | 1,00296 / 0,01711 | 1,00127 / 0,01165 | 1,00006 / 0,00617 |
| G_N/G (Mittel; Spanne der Netze 1,0000117 bis 1,0000184) | 1,0000137 | 1,0000158 | 1,0000145 |
| TT-Tempo-Spanne om2/k^2 (36 Richtungen) | 15,4 % +- 4,2 | 12,0 % +- 2,3 | 8,0 % +- 1,8 |

- Direkte Newton-Antwort m^H P^-1 m (beschreibend): 1,00022 / 1,00034 / 1,00054; der Zuwachs mit N passt zu einem
  O((k L)^2)-Beitrag der zurueckgefalteten Takt-Moden [ES]; das Planmass (weichster Eigenwert) ist 1 + O(k^2).

### 4.3 Exponent [E]

| Groesse | Steigung von ln(Lagenstreuung) gegen ln N (22 Netze) |
|---|---|
| **Hauptgroesse V1+S+J** | **-0,705** (Bootstrap 68 %: -0,80 bis -0,61; 95 %: -0,90 bis -0,52); durch die drei Mittel -0,736 |
| Kopplungsmass K | -0,702 |
| S+J | -0,674 |
| nur TT-Anteil | -0,650 |
| umkreisbasiert | -0,705 |
| TT-Tempo-Spanne | -0,460 (TT-GLAS: -0,47 bis -0,56 [P]) |

- Lesart [ES]: Die Lagenstreuung faellt steiler als die Tempo-Spanne. Zwischen N = 128 und 256 ist die Steigung -0,55,
  zwischen 256 und 512 -0,92 [Kopfrechnung aus den Mitteln]; ein Gemisch aus linearen (N^-1/2) und quadratischen (N^-1)
  Leckbeitraegen passt dazu, bewiesen ist es nicht.
- Stichprobenfehler des Planmittels [M, nach Sicht]: Die Leistung einer Kreisbahn ist eine quadratische Form in S(m),
  also ein gerades Polynom vom Grad 4 in m. Das Mittel ueber 24 Lagen hat deshalb einen Fehler von etwa
  Lagenstreuung/sqrt(24); daher die grosse SD der Netzmittel im Planmass (0,0072 gegen 0,0012 exakt bei N = 128). Probe:
  zwei gegeneinander gedrehte Ikosaeder geben dasselbe Mittel auf 4,4e-16.

### 4.4 Kanalanteile (Zuwaechse in der Reihenfolge TT, L, nn, V1; PLAN 1.6) [E]

Mittel ueber Lagen und Saaten; Plan = 24 Lagen (in Klammern SD ueber die Netze), exakt = Nachtrag (+- Standardfehler).

| N | TT (Plan / exakt) | L (laengs-quer) | nn | V1 | Summe = Mittel - 1 |
|---|---|---|---|---|---|
| 128 | +3,9e-4 (9,1e-4) / +6,3e-4 +- 1,4e-4 | +2,05e-3 (6,1e-3) / +1,24e-3 +- 0,25e-3 | +9,6e-4 (3,2e-3) / +3,8e-4 +- 0,8e-4 | -4,5e-4 (5,3e-3) / -7,5e-5 +- 9,0e-5 | +2,95e-3 / +2,17e-3 |
| 256 | +2,2e-4 (5,1e-4) / +3,2e-4 +- 0,5e-4 | +8,4e-4 (2,1e-3) / +6,3e-4 +- 0,7e-4 | +7,0e-4 (2,0e-3) / +2,2e-4 +- 0,5e-4 | -4,9e-4 (3,0e-3) / -5,0e-5 +- 4,7e-5 | +1,27e-3 / +1,12e-3 |
| 512 | +3,3e-4 (1,7e-4) / +1,5e-4 +- 0,2e-4 | -3,5e-4 (1,0e-3) / +2,9e-4 +- 0,3e-4 | -7,1e-5 (1,3e-3) / +6,8e-5 +- 1,0e-5 | +1,6e-4 (1,3e-3) / +0,07e-5 +- 1,4e-5 | +5,8e-5 / +5,1e-4 |

Lagenstreuung der Zuwaechse (SD ueber alle Lagen und Netze je N; jq auf der .69, jq-69/kanal-streuung.json):

| N | TT | L | nn | V1 | nn + V1 | gesamt |
|---|---|---|---|---|---|---|
| 128 | 0,0028 | 0,0153 | 0,0092 | 0,0140 | 0,0075 | 0,0188 |
| 256 | 0,0018 | 0,0090 | 0,0082 | 0,0113 | 0,0055 | 0,0120 |
| 512 | 0,0010 | 0,0052 | 0,0042 | 0,0049 | 0,0031 | 0,0062 |

- Der TT-Zuwachs ist vertraeglich mit dem vorab abgeschaetzten Jensen-Anteil der anisotropen Tempi (PLAN 1.4: 6e-4 bei
  128, 1,5e-4 bei 512 [Kopfrechnung]; exakt 6,3e-4 und 1,5e-4) [ES]. Er kann auch eine Abweichung der TT-Kopplung selbst
  enthalten; eine Probe Netz fuer Netz (TT-Zuwachs gegen Varianz der Tempi) fehlt.
- Nach Sicht [M, Gegenleser bestaetigt]: Im exakten Lagenmittel fallen die Kreuzterme zwischen TT-Teil und Lecks weg (das
  Lagenmittel von S x S^* ist isotrop, Lambda_n[nn] = 0, TT orthogonal zu L). Damit sind die exakten Zuwaechse von L und
  nn Betragsquadrate der Lecks (>= 0, gemessen positiv, ~N^-1); der V1-Zuwachs ist Betragsquadrat plus Kreuzterm mit nn
  und kann beide Vorzeichen haben.
- nn und V1 sind stark gegenlaeufig (Korrelation etwa -0,87 bei N = 128 [Kopfrechnung aus den SD]), heben sich aber auf
  dem Glas nicht auf. Der groesste Einzelkanal ist L.

### 4.5 Nebenarm: umkreisbasierte Gewichte (beschreibend, ohne Urteil) [E]

- Kreisbahnen: umkreisbasiert gleich P1 auf <= 2,8e-6 (128), 3,6e-6 (256), 1,7e-6 (512) je Lage (jq-69/umkreis-diff.json);
  Kanaele ebenso (z. B. V1 bei 512: +1,556049e-4 gegen +1,556050e-4). Exponent -0,705 wie P1. Wie auf V (IMPULS-NETZ-1
  5.6 [P]) unterscheiden die beiden Formen eine glatte, kompakte Quelle praktisch nicht, obwohl die P1-Gewichte auf dem Glas
  oft negativ sind (TAKT-UMKLAPP-1 4.5 a [P]). Lesart offen [H].
- Affine Probe KP1 (Summe sigma n n^T = -V T): umkreisbasiert auf <= 6,4e-12 absolut, P1 auf <= 3,1e-8 absolut
  (1,2e-10 relativ, Netz N = 256 Saat 2 mit dem flachsten Splitter 0,083 Grad). Fuer umkreisbasierte Gewichte gilt die
  Identitaet nur ueber die ganze Voronoi-Zerlegung, nicht je Tetraeder (PLAN 4) [M, E].
- phi-Quadrupol (gittergross, je N Mittel und SD ueber die Saaten, V1+S+J):

| N | P1: [001] / [111] / (1,2,3) | umkreisbasiert: [001] / [111] / (1,2,3) |
|---|---|---|
| 128 | 5,4 (9,9) / 8,7 (15,8) / 2,0 (2,7) | 0,98 (0,26) / 1,05 (0,39) / 1,00 (0,32) |
| 256 | 2,8 (2,8) / 26,1 (29,4) / 12,7 (12,6) | 1,20 (0,38) / 1,29 (0,40) / 1,20 (0,47) |
| 512 | 123 (250) / 145 (340) / 121 (281) | 1,35 (0,63) / 0,97 (0,57) / 1,07 (0,60) |

  - Je Netz liegen die P1-Werte zwischen 0,41 und 838 (N = 512, Saat 4: 626 / 838 / 694; umkreisbasiert dort 0,21 / 0,05 /
    0,06). Lesart [H, nach Sicht]: Ein Klumpen von Kantengroesse ist auf dem Glas nicht affin je Tetraeder; die P1-Form
    reagiert an flachen Splitter-Tetraedern sehr stark, die umkreisbasierte nicht. Die Werte sind lokale Eigenschaften der
    Umgebung von pos[0] und zeigen keinen N-Gang (vorab, PLAN 1.3). Fuer Urteile wird der phi-Quadrupol nicht benutzt.

### 4.6 Kontrollen [E]

| Kontrolle | Wert | Soll (PLAN 6) |
|---|---|---|
| GS0 (V, 10 x 20) | Abweichung <= 6,4e-6; ohne J 1,184398 / 0,908770 / 0,976959 (IN0: 1,184405 / 0,908775 / 0,976965) | <= 1e-3 |
| V umkreisbasiert, phi V1+S+J | 1,071675 / 0,951114 / 0,939092 (IMPULS-NETZ-1 NU: 1,0717 / 0,9511 / 0,9391 [P]) | beschreibend |
| V Kreisbahnen S+J | 0,998498 / 1,001216 / 1,000537 / 1,000537 (IMPULS-NETZ-1: 0,998504 / 1,001221 / 1,000542 / 1,000542; Unterschied = G_N/G) | beschreibend |
| KP1 affin | P1 <= 1,2e-10 relativ (ein Netz ueber 1e-10), umkreisbasiert <= 6,4e-12 absolut | <= 1e-10 relativ |
| KF (M^H B), KR (c^H M), erstes k je Netz | <= 4,6e-15; <= 2,7e-14 | <= 1e-10 |
| KJ (M^H P_M sigma = M^H sigma) | <= 4,4e-11 | <= 1e-8 |
| Cholesky A_red, voller Rang [M, c] | alle 22 x 36 + 100 Punkte; QR-Weg ueberall | alle |
| Luecke om2_3/om2_2 | >= 4 778 | >> 1 |
| KN: G_N/G | 1,0000117 bis 1,0000184 (vorab 1 + O(k^2)) | 1 auf 1e-3 |
| Quadratur 8 x 16 gegen 6 x 12 (N = 128, Saat 1) | Mittel 7e-7, Lagenstreuung 9e-7, Bahn [001] 3e-6, phi 2,5e-5 | beschreibend |
| kabs 0,02 gegen 0,01 (N = 128, Saat 1) | Mittel -6,1e-5, Bahn [001] -6,6e-5, G_N/G 1,000057 | beschreibend |
| V mit 6 x 12 gegen 10 x 20 | GS0-Werte gleich auf 1,3e-6 | beschreibend |

### 4.7 Nebenbefund: Kreisbahnen auf V mit Energiekanal V1 (aus Lauf GV und Nachtrag NVJ1, beschreibend) [E]

| Groesse (24 Lagen) | V, J_iso, S+J | V, J_iso, V1+S+J | V, J = 1, S+J | V, J = 1, V1+S+J |
|---|---|---|---|---|
| Bereich | 0,998498 bis 1,001216 | 0,999985 bis 1,000003 | 0,999712 bis 1,001721 | 0,998608 bis 1,003323 |
| Lagenstreuung (SD; jq auf der .69, jq-69/v-streuung.json, v-j1-bahnen.md) | 7,2e-4 | 4,8e-6 | 5,3e-4 | 1,25e-3 |
| exaktes Lagenmittel | 1,000129 | 0,999996 | nicht gerechnet | nicht gerechnet |

- Auf V mit J_iso gilt je Lage: nur TT = 0,999996 (TT-Kopplung 1 + 1,5e-6 [P], geteilt durch G_N/G = 1,000005; Streuung
  9e-8), TT+L gleich (L-Zuwachs: Streuung 6e-8, also null wie IMPULS-NETZ-1), S (mit nn) = 1 + 0,004077 (0,6331 -
  Summe m^4) wie IMPULS-NETZ-1 [P], **und S+V1 wieder 0,999996 - 2,7e-5 (Summe m^4 - 0,60)** [E; Koeffizienten aus den
  Lagen [001] und [111], an [110] und z5 auf 1e-7 bestaetigt]: Der V1-Kanal hebt das nn-Leck einer kompakten Kreisbahn
  zu etwa 99 % auf. Spanne ueber Summe m^4 = 1/3 bis 1: 1,8e-5; groesster Betrag abs(G - 1) 1,5e-5 (kl = 0,01), also
  rund 9-mal unter 1,3e-4.
- Mit J = 1 auf V (Nachtrag; TT-Tempo-Spanne 6,0 %) kehrt das L-Leck zurueck (L-Zuwachs: Streuung 1,7e-3, bis 4,2e-3;
  jq-69/v-j1-streuung.json), und V1 hebt nn nicht mehr auf (Streuung nn 4,2e-4, V1 7,2e-4, zusammen mit L 1,25e-3). Der phi-Quadrupol mit J = 1: 1,02585 / 0,99194 / 0,97273 (IMPULS-NETZ-1, J = 1 naeherungsweise:
  1,02617 / 0,99224 / 0,97303 [P]; Unterschied 3e-4, Definition von c0).
- **k-Konvergenz (Nachtrag NVKL nach dem Gegenlesen, nachtrag-69/v-kl.json), V mit J_iso, V1+S+J ueber 24 Lagen:**

| kl | Bereich G | Spanne | Streuung (SD) | G_N/G | S+J: Streuung |
|---|---|---|---|---|---|
| 0,005 | 0,999988 bis 1,000006 | 1,80e-5 | 4,78e-6 | 1,0000013 | 7,210e-4 |
| 0,01 | 0,999985 bis 1,000003 | 1,81e-5 | 4,80e-6 | 1,0000051 | 7,210e-4 |
| 0,02 | 0,999973 bis 0,999992 | 1,87e-5 | 4,96e-6 | 1,0000204 | 7,212e-4 |
| 0,04 | 0,999924 bis 0,999945 | 2,10e-5 | 5,58e-6 | 1,0000814 | 7,218e-4 |

  - Der Lagengang ist bei kleinem kl konstant (Spanne 1,8e-5); die Lage des ganzen Bandes wandert wie O(kl^2) mit G_N/G.
    Der Rest ist also ein k -> 0-Befund, kein Effekt endlicher Wellenzahl [E].
- Lesart [H]: Die Aufhebung haengt an isotropen Bewegungsgewichten (J_iso). Auf dem Glas (J = 1, je Probe anisotrop)
  fehlt sie; dort traegt L den groessten Teil der Lagenstreuung. Physikalisch ist eine Aufhebung zu erwarten, weil der
  Erhaltungssatz nn-Spannung und Energie verknuepft (Gegenleser); warum sie mit J = 1 ausbleibt, ist offen.

## 5. Bedeutung fuer den Glas-Zweig, den Doppelpulsar und GW170817 [H]

- **Glas-Zweig:** Ohne jede Abstimmung wird die Abstrahlung einer Kreisbahn mit wachsender Punktzahl lagenunabhaengig
  (Streuung ~N^-0,7 im Bereich N = 128 bis 512) und ihr Betrag einsteinsch (Abweichung ~N^-1, exakt +5,1e-4 bei
  N = 512). Der abgestimmte Kristall V ist mit nur 10 Ecken je Zelle viel isotroper: Lagenstreuung (SD) 4,8e-6 mit V1
  bzw. 7,2e-4 ohne V1, gegen 6,2e-3 auf dem Glas mit 512 Punkten. Das Glas gewinnt nur ueber die Groesse.
- **Doppelpulsar (1,3e-4 [P], Kramer u. a. 2021 ueber PUMPE-NETZ-1):**
  - Gerechnet bei N <= 512: Lagenstreuung 47-mal, exakter Mittelwert 4-mal ueber der Schranke.
  - Hochrechnung [Kopfrechnung]: Die Lagenstreuung erreicht 1,3e-4 bei N ~ 1,2e5 (Steigung -0,705) bzw. ~1,2e6 (-0,5);
    der Mittelwert bei N ~ 2e3 (Steigung ~ -1).
  - Physikalisch zaehlt vermutlich die Punktzahl in einem Wellenlaengen-Volumen (die Kreisbahn ist hier der Grenzfall
    k -> 0, der die ganze Superzelle mittelt). Bei einem Netz im Planck- oder auch Femtometer-Massstab und
    Wellenlaengen von 1e12 m waere N astronomisch gross; beide Abweichungen waeren dann unmessbar klein, sofern das
    N-Gesetz weiter gilt [H]. Geprueft ist das nur bis N = 512.
- **GW170817 (~1e-15 [P], SKALAR-SEKTOR-L):** Die Quadrate der TT-Tempi einer Probe (om2/k^2) streuen um 8 % bei N = 512,
  die Tempi selbst um etwa 4 %, und die Spanne faellt wie N^-0,46; 1e-15 waere bei N ~ 2e32 erreicht [Kopfrechnung]. Fuer
  ein Netz weit unter der Wellenlaenge waere das erfuellt, falls das N-Gesetz weiter gilt [H]. Ob das mittlere TT-Tempo
  gleich der Lichtgeschwindigkeit ist, prueft diese Rechnung nicht (kein Licht im Modell).
- **Fuer den Kristall-Zweig (Nebenbefund 4.7):** Die Aussage "Kreisbahnen rund 12-mal ueber dem Doppelpulsar"
  (IMPULS-NETZ-1, SKALAR-SEKTOR-L, Karte) beruht auf Bahnen ohne V1. Mit V1 (wie bei der phi-Quelle schon gerechnet)
  liegt V mit J_iso fuer kompakte Bahnen 9- bis 11-mal unter der Schranke (groesster Betrag abs(G - 1), k-konvergiert).
  Das haengt an den abgestimmten Gewichten J_iso (mit J = 1 nicht) und sollte vor weiterer Nutzung eigens gegengelesen
  werden; die Kartenquelle (Klumpen von Kantengroesse) bleibt bei 3 % (GS0).
- **Energie-Regel (skalarer Sektor):** Ein isotroper Rest im V1-Kanal ist auf dem Glas bis N = 512 nicht nachweisbar
  (GS3; bei N = 512 betragsmaessig unter 3e-5). Die Energie-Regel ist fuer Zufallsnetze danach nicht die naechste
  Baustelle; offen bleibt das L-Leck mit J = 1, das auf V mit J_iso verschwindet [ES].

## 6. Selbstanzeigen

1. **Rauchtest r6 nach Beginn des Plantexts:** r1 bis r5 liefen vor dem Plantext (09:23:02 bis 09:23:49 CEST), r6 (Absturz-
   probe der geaenderten Urteilsregeln "nicht entscheidbar") um 09:26 CEST waehrend des Plantexts, vor dem Einfrieren.
   PLAN 8 sagt "vor dem Plantext und vor dem Einfrieren"; genau ist "vor dem Einfrieren". Gelesen nur rc und Schluessel.
2. **Rauchlaeufe r1 bis r4 rechneten vollstaendig** (grobes Gitter, Rauchsaaten, r1 auf V). Gelesen nur Laufzeiten,
   Speicher, Schluessel; die Rauch-JSON-Dateien sind nicht kopiert.
3. **Zwischenauswertung ZW nicht in der Laufliste:** 09:33:25 bis 09:34:02 CEST mit dem eingefrorenen Code auf V,
   N = 128, 256, damit bei Abbruch der GPU-Laeufe ein Teilbericht moeglich war. Erste Sicht 09:34:02 CEST. Am Plan und an
   den Laeufen danach hat sie nichts geaendert (alles lief schon).
4. **Ableitbarkeitsprobe unvollstaendig:** Dass die Kreisbahn-Leistung ein Polynom vom Grad 4 in m ist und ein exaktes
   Lagenmittel mit 6 Achsen moeglich ist, habe ich erst nach Sicht gesehen. Das Planmittel ueber 24 Lagen ist dadurch
   verrauscht (SD der Netzmittel 6- bis 8-mal groesser als exakt). GS2 bleibt mit beiden Massen eingetroffen; GS3 bleibt mit
   beiden nicht eingetroffen (exakter Quotient D_512/D_128 = 0,23). Die GS3-Kette im Plan war unvollstaendig formuliert
   (Kreuzterm V1 x nn, Abschnitt 3); das Ergebnis aendert das nicht.
5. **Nachtraege nach Sicht** (beschreibend, kein Urteil): nachtrag_ikosaeder.py (exaktes Lagenmittel) und nachtrag_v_j1.py
   (V mit J = 1, Anlass Nebenbefund 4.7). Beide importieren gs.py unveraendert und ersetzen nur im eigenen Prozess eine
   Funktion bzw. die J-Tabelle; Code-Summen in EINGEFROREN-SHA256-69.txt nicht enthalten, siehe Abschnitt 1.
6. **jq lokal zum Rechnen benutzt:** Die Streuungen der Kanalzuwaechse und die Differenz P1/umkreisbasiert habe ich zuerst
   lokal mit jq gerechnet (Mittel, Varianz, Maximum). Danach dieselben Befehle auf der .69 wiederholt
   (jq-69/, Pruefsummen dort erzeugt); im Text stehen die .69-Werte (gleich). Ebenso die Lagen-Tabellen 4.1 und die
   Streuungen auf V (4.7) (jq auf der .69). Kein lokales python, awk oder perl.
7. **KP1 knapp ueber der Plan-Schranke:** P1 auf N = 256, Saat 2: 1,2e-10 relativ (Splitter 0,083 Grad); kein Urteil
   haengt daran.
8. **Lokale Bearbeitung:** gs.py vor dem Einfrieren mit dem Edit-Werkzeug geaendert und einmal per sed in eine neue Datei
   mit mv ersetzt. Auf der .69 lag jede Fassung in einem neuen Ordner (code-r1, code-r2, code, nachtrag-code,
   nachtrag-code2), nie in place.
9. **c0 und Leistungsmass sind Festlegungen** (PLAN 1.4): Raumwinkel-RMS der TT-Tempi, Faktor c0/c_j je Mode. Das
   Kopplungsmass K zeigt dieselben Gesetze (Steigung -0,70); der Mittelwert haengt am c0 auf etwa 1e-4 (TT-Zuwachs).
10. **Werkzeug-Protokolle im Scratchpad:** Warteschleifen und ein Monitor legten ihre Ausgaben automatisch unter
    /tmp/claude-1000/.../tasks/ ab. Selbst geschrieben habe ich dort nichts.
11. **Gegenlesen nur einmal:** Ein frischer Leser hat die Fassung von 10:02 CEST gelesen (Abschnitt 9). Die danach
    eingearbeiteten Aenderungen, der Nachtrag NVKL und diese letzte Textschicht sind nicht frisch gegengelesen; ebenso nicht
    der Code der Nachtraege. Der Nebenbefund 4.7 sollte vor weiterer Nutzung eigens gegengelesen werden.
12. **Nachtrag NVKL nach dem Gegenlesen** (Auflage B2): V bei kl = 0,005 bis 0,04 durch Ersetzen von gs.LP im eigenen
    Prozess; die phi-Werte dieses Laufs sind dadurch verschoben und nicht ausgegeben.

## 7. Einfach gesagt

Wir haben in Finns Zufallsnetzen am Computer zwei Sterne umeinander kreisen lassen und gemessen, wie stark sie
Schwerewellen abstrahlen, fuer 24 verschiedene Bahnlagen. Bei 128 Punkten haengt die Abstrahlung noch um etwa 2 % von der
Lage ab, bei 512 Punkten nur noch um gut ein halbes Prozent; mit mehr Punkten wird das Netz gleichmaessiger, bei 512
Punkten ist es aber noch rund 47-mal zu ungleich fuer den Doppelpulsar. Im Mittel weicht die Abstrahlung bei 512 Punkten
nur noch um ein halbes Promille von Einstein ab, und auch das wird mit mehr Punkten kleiner; einen bleibenden Rest aus der
Energie-Regel haben wir bis 512 Punkte nicht gefunden. Nebenbei zeigte sich, noch ungeprueft: Im regelmaessigen Netz V
verschwindet die Lagenabhaengigkeit fast ganz, wenn man die Energie der Sterne mitrechnet.

## 8. Dateien

- KARTE.md (unveraendert), PLAN.md, PLAN.md.eingefroren-20261005-092835, EINGEFROREN-SHA256.txt, EINGEFROREN-SHA256-69.txt.
- code/: gs.py (neu); tg.py, dz.py, dk.py, ew.py, tp.py, pn.py, mn.py, inz.py, nachtrag_iso.py, nachtrag_umkreis.py
  (unveraendert); kette-cpu.sh, kette-cpu7.sh, kette-p4000a.sh, kette-p4000b.sh; je mit .eingefroren-20261005-092835;
  rauch1.sh, rauch2.sh; nachtrag_ikosaeder.py, nachtrag_v_j1.py (nach Sicht), nachtrag_v_kl.py (nach dem Gegenlesen).
- lauf-69/: v.json, gs-N128-s1..8.json, gs-N256-s1..8.json, gs-N512-s1..6.json, kontrolle/ (v-6x12, q8x16-N128-s1,
  k002-N128-s1), Logs, kette-*.ausgabe.txt, PRUEFSUMMEN.txt.
- aus-69/: auswertung.json, **bild-glas-strahlung.png** (links G_rad/G_N je Bahnlage und Netz fuer N = 128, 256, 512 mit V;
  Mitte Lagenstreuung gegen N doppellogarithmisch mit Gerade und N^-0,4; rechts Kanalzuwaechse, Planmass), kontrolle.json,
  zwischen-128-256.json und .png, Logs, PRUEFSUMMEN.txt.
- nachtrag-69/: nachtrag-ikosaeder.json, v-j1.json, v-kl.json, Logs, PRUEFSUMMEN.txt. jq-69/: kanal-streuung.json,
  umkreis-diff.json, v-streuung.json, v-j1-streuung.json, tabelle-lagen.md, v-bahnen.md, v-j1-bahnen.md, PRUEFSUMMEN.txt.
  rauch-69/: Logs r1 bis r6.
- Alle PRUEFSUMMEN.txt auf der .69 erzeugt; sha256sum -c besteht lokal.
- Auf der .69: /home/fmh/fmhc-physics-remote/glas-strahlung-1/ (code/, code-r1/, code-r2/, nachtrag-code/, nachtrag-code2/,
  nachtrag-code3/, rauch/, lauf/, aus/, nachtrag/, jq-69/).

## 9. Gegenlesen

- Ein frischer Leser (pruefer-opus, nur lesend, keine Dateien geschrieben) las 10:02:54 bis 10:12:50 CEST (seine
  date-Angaben) die Fassung von 10:02:17 CEST. Er pruefte rund 170 Zahlen vorwaerts gegen die JSON-Dateien, die Urteile
  rueckwaerts aus PLAN 5 und gs.py, die Herleitungen (a) bis (f) und die Bloch-Phasen und den V1-Term im Code.
- **Kein A-Befund.** Eingearbeitet ab 10:19 CEST (date): B1 Vergleich Glas/V im selben Mass (SD) und ohne "gleiche
  Punktzahl" (5); B2 k-Konvergenz des V-Nebenbefunds offen, Mass "groesster Betrag" statt Spanne: Nachtrag NVKL gerechnet
  (4.7), "9- bis 11-mal" statt "7-mal" (2, 5); B3 V1-Rest "bis N = 512 nicht nachweisbar, unter 3e-5" statt absolut
  (2, 5, 7); B4 TT-Zuwachs als [ES] "vertraeglich mit" (2, 4.4); B5 Steigung nur fuer N = 128 bis 512, ohne "steiler als
  N^-0,5" (2); B6 "Einfach gesagt" ohne "von selbst", mit Abstand zur Schranke und "noch ungeprueft" (7); C1 Quotient
  0,23 (6); C2 GS3-Kette berichtigt (3, 6); C3 GW170817: Tempo statt Tempo-Quadrat, N ~ 2e32, Konjunktiv (5); C4
  Rundung des V1-Zuwachses einheitlich.
- **Bestaetigt** (Leser): Urteile GS0 bis GS3 nach Plan und Wortlaut, alle Exponenten, Tabellen 4.2 bis 4.4 und 4.7,
  Kopfrechnungen; Herleitungen (a) Voronoi-Identitaet, (c) Polynomgrad und 5-Design, (d) Faktor c0/c_j und V1-Faktor,
  (e) Normierung, (f) untere Halbkugel; Bloch-Phasen und V1-Term der Kreisbahn wie bei der phi-Quelle (durch GS0
  wirksam geprueft).
- **Nicht gegengelesen:** Abschnitt 1 und Tabelle 4.1 im Einzelnen, die phi-Tabelle 4.5, der Code der Nachtraege und die
  Bausteine tg.py, dz.py, pn.py, inz.py, das Bild, der Nachtrag NVKL und diese letzte Textschicht.

Abschluss des Textes 2026-10-05 10:21:23 CEST (date, vor dem letzten Einarbeiten gemessen). Zeitbox 150 min ab 09:03:22 CEST,
also bis 11:33:22 CEST: eingehalten. Kein Lauf mehr aktiv (letzter Lauf NVKL endete 08:19:29 UTC). Journal, Peerbus und
Commit uebernimmt die Leitung.
