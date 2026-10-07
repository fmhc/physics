# REGGE-4D-SCHIEF-1: Ergebnis (Runde 37, Code-Agent)

- Code-Agent fuer die Leitung claude-primary.
- **Zeiten (date; .69 in UTC, CEST = UTC + 2):**
  - Start 2026-10-04 04:01:00 CEST.
  - Rauchlauf 0 (nur Geometrie von A) 02:19:06 bis 02:19:09 UTC.
  - Plantext ab 04:22:44 CEST.
  - Rauchlauf 1 02:24:34 bis 02:27:44 UTC.
  - Eingefroren 04:28:32 CEST: PLAN.md.eingefroren-20261004-042832 und Code-Kopien *.eingefroren-20261004-042832;
    Pruefsummen in EINGEFROREN-SHA256.txt.
  - Hauptlaeufe: Teil 1 02:28:42 bis 02:30:23 UTC. Teil 2 02:30:50 bis 02:31:20 UTC (s = 0) und 02:30:50 bis
    02:32:12 UTC (s = 0,2). Auswertung 02:32:23 bis 02:32:27 UTC. Alle rc = 0; Fehlstart siehe Selbstanzeige 1.
  - Nachtraegliche Diagnose 02:34:56 bis 02:35:13 UTC. Text ab 04:36:46 CEST.
- Der eingefrorene Code ist unveraendert; Pruefsummen auf der .69 (lauf-69/PRUEFSUMMEN.txt) und lokal stimmen ueberein.
- Alle Zahlen sind linearisierte, euklidische Gitterrechnungen auf der .69 (reines numpy, float64, Spuren cpu und cpu6),
  keine Messdaten. G = M = 1.
- **Kennzeichen:**
  - [S] an der Quelle gelesen (hier nur ueber REGGE-4D-1)
  - [L] Literatur aus dem Gedaechtnis, [L?] unsicher
  - [M] eigene Mathematik
  - [E] hier gerechnet
  - [H] Hypothese
  - [F] Festlegung im Plan

## 1. Ergebnis zuerst

1. **Die tote Hyperdiagonale verschwindet im schiefen Netz, und Einsteins lange-Wellen-Form bleibt erhalten [E].**
   - Bei s = 0,1 und 0,2 gibt es bei k = 0 genau 10 Nullmoden (affin), an allen 144 allgemeinen Punkten genau 4
     (Eichung). Kuhn (s = 0) hat 11 bzw. 5.
   - In physikalischen Koordinaten ist die Form bei s = 0,2 und abs(k_phys) <= 0,1 Einsteins (1/4) k^2 (P2 - 2 P0s), je
     physikalischem Volumen:
     - Spin 2 fuenffach gleich auf 0,31 %;
     - c0s/c2 = -1,9989 bis -2,0047;
     - c2 ueber 16 Richtungen gleich auf 0,11 %;
     - c2/(1/4) = 0,9990 bis 0,9998 im Mittel.
2. **Aber die Hyperdiagonale wird nicht harmlos, sondern eine negative Gittermode [E].**
   - Ihr Eigenwert bei k = 0 waechst linear mit s: 0,084 / 0,17 / 0,34 / 0,52 / 0,68 mal Mittel bei s = 0,025 / 0,05 /
     0,1 / 0,15 / 0,2. Er ist in H (Vorzeichen der euklidischen Einstein-Wirkung) **negativ**: -0,38 (s = 0,1) und
     -0,93 (s = 0,2).
   - Signatur bei allgemeinem k: 9 positiv, 2 negativ (Kuhn: 9 positiv, 1 negativ).
   - Bei s = 0,2 wechselt zusaetzlich eine Gittermode nahe dem Zonenrand das Vorzeichen: 544 von 4096 BZ-Punkten haben
     3 negative Eigenwerte; dort kommt ein Eigenwert bis 2,4e-5 x Mittel an null heran.
   - [M, erste Ordnung, nicht gerechnet] Das Vorzeichen haengt an der Richtung der Schiefe: Mit -B kehrten sich die
     Winkel an der Hyperdiagonale (stumpf gegen spitz) und damit das Vorzeichen in erster Ordnung um.
3. **Nahe der Masse wird es nicht besser, sondern richtungsabhaengig [E].**
   - Die Fehlwinkel sind ohne Festlegung eindeutig: an allen statischen k genau 4 Nullmoden.
   - gamma(r = 6) betraegt auf der Achse A e_x 1,056, auf A e_y 1,308 und auf A e_z 1,113. Kuhn: 1,087 auf allen Achsen.
   - Weit weg geht gamma auf allen drei Achsen gegen 1: L = 48, r ~ 18 bis 22: 1,007 / 1,006 / 0,997.
   - Der 1/r^2-Schwanz ist richtungsabhaengig: (gamma - 1) r^2 -> +1,65 (A e_x, A e_y), -1,1 (A e_z); Kuhn +2,2 auf der
     Achse.
   - Auf A e_y und A e_z kommt nahe der Masse ein kurzreichweitiger Zusatz dazu. Auf A e_y faellt (gamma - 1) r^2 von
     11,1 (r = 6) etwa wie exp(-r/2,7) auf den Schwanz [E]. Dass er von der gehobenen Diagonalmode stammt, ist eine [H].
4. **Urteile:** SC0, SC1 und SC2 eingetroffen; SC3 nicht eingetroffen.
   - Teil (a) von SC3 ist erfuellt (eindeutig).
   - Teil (b) ist verfehlt: 0,056 > 0,044 auf der geurteilten Achse, auf den beiden anderen deutlicher.
5. **Bedeutung:** Die tote Diagonale war ein Kunstprodukt der rechten Winkel, wie die Karte vermutet. Das schiefe Netz
   tauscht sie aber gegen eine Gittermode mit negativer Steifigkeit und gegen eine richtungsabhaengige Nahzone. Fuer
   lange Wellen ist es so gut wie der Kristall, nahe der Masse schlechter.

## 2. Urteile

Mechanisch nach PLAN.md Abschnitt 7 durch code/regge_schief_auswertung.py. Die Werte stehen in lauf-69/auswertung.json.
Die Felder "vermerk" sind per jq nachgetragen; Urteile und Werte sind per diff identisch mit auswertung.maschine.json.

| Nr | Vorhersage (Karte) | Wahrsch. | Urteil | Kennzahlen |
|---|---|---|---|---|
| SC0 | flach <= 1e-12 fuer alle s; M(k) hermitesch <= 1e-10; s = 0: 11 Nullmoden bei k = 0, 5 bei allgemeinem k | 85 % | **eingetroffen** | flach 1,8e-15 / 2,7e-15 / 4,4e-15; hermitesch 3,3e-12 / 3,1e-12 / 3,9e-12; s = 0: 11 (bis 6,8e-12 x Mittel, dann 2,14) und 5 an allen 144 Punkten |
| SC1 | s = 0,1 und 0,2: k = 0 genau 10, allgemein genau 4 (Schwelle 1e-6 x Mittel) | 65 % | **eingetroffen** | k = 0: 10 / 10, 11. Eigenwert 0,345 / 0,677 x Mittel; allgemein 4 an allen 144 Punkten, kleinster Nicht-Eich-Eigenwert 3,2e-5 / 1,8e-5 x Mittel (k^2-Mode bei abs(k) = 0,05); Eichresiduum <= 1,0e-12 |
| SC2 | s = 0,2, abs(k_phys) = 0,05 bis 0,1: fuenf Spin-2-Werte gleich auf 1 %, c0s/c2 = -2 +- 0,02, Richtungsstreuung <= 1 % | 60 % | **eingetroffen** | Entartung <= 0,31 %; abs(c0s/c2 + 2) <= 0,0047; c2-Streuung 0,027 / 0,060 / 0,107 % (0,05 / 0,075 / 0,1); alle 80 Spin-2-Werte <= 0,37 % |
| SC3 | [H] s = 0,2: Fehlwinkel ohne Festlegung eindeutig, und abs(gamma(6) - 1) < 0,044 | 40 % | **nicht eingetroffen** | (a) erfuellt: 4 Nullmoden an allen 32767 statischen k (L = 32), Eichmoden aendern Fehlwinkel <= 5,5e-13; (b) gamma(6) = 1,0563 (A e_x, Stuetzpunkte r = 5,90: 1,0587 und 6,75: 1,0411), zeilennormierte Kondition 1,56 |

- **Nach dem Kartenwortlaut** (ohne meine Festlegungen) faellt SC3 ebenso aus:
  - Am Gitterpunkt x0 = 6 der Achse ist gamma = 1,0916 (r = 5,06).
  - Auf den anderen Achsen ist gamma(6) = 1,308 bzw. 1,113.
  - Die Haelfte der Kuhn-Abweichung meiner s = 0-Kontrolle ist 0,0436, also gleich der Kartengrenze 0,044.
- **SC2 nach anderer Lesart:** Auch mit der Streuung aller 80 Werte (Art von G3) und mit den Varianten "orth" und
  "direkt" bleiben alle Kennzahlen unter 0,5 %.
- **Bedeutung, wie vorab auf der Karte festgelegt:**
  - "SC1 und SC2 treffen ein" ist ausgeloest: Die tote Hyperdiagonale ist ein Kunstprodukt der rechten Winkel; das
    schiefe Netz zeigt Einsteins Fingerabdruck.
  - Den Zusatz "ein ungeordnetes Netz ist eher besser als ein Kristall [H]" schraenkt dieser Lauf ein (Abschnitt 6).
  - "SC3 verfehlt" ist ausgeloest: Die Naehe der Masse ist ein allgemeiner Gittereffekt, nicht die Diagonale. Im
    schiefen Netz ist die Abweichung auf zwei von drei Achsen sogar groesser.

**Agenten-Vorhersagen** (PLAN Abschnitt 8, vor jeder Rechnung mit Spektrum, Form oder Quelle)

| Nr | Vorhersage | Ergebnis |
|---|---|---|
| A1 (90 %) | SC0 eingetroffen, flach <= 1e-14, hermitesch <= 1e-11 | **eingetroffen** (4,4e-15; 3,9e-12) |
| A2 (70 %) | 11. Eigenwert bei k = 0 linear in s (Verhaeltnis 0,2/0,1 in 1,6 bis 2,4), bei s = 0,2 zwischen 0,05 und 1 x Mittel | **eingetroffen**: 0,677/0,345 = 1,96; 0,677. Das Vorzeichen (negativ) war nicht vorhergesagt |
| A3 (75 %) | SC1 eingetroffen | **eingetroffen** |
| A4 (60 %) | SC2 eingetroffen; Schur-Korrektur der leichten Mode bei 0,1 unter 0,5 % | **eingetroffen**: Schur gegen direkt hoechstens 0,3 % in c0s/c2 und 0,1 % in c2 bei 0,1 (das Mass war im Plan nicht genau festgelegt) |
| A5 (75 %) | SC3 (a) eindeutig | **eingetroffen** |
| A6 (25 %) | SC3 (b) erfuellt | **nicht eingetroffen** |
| A7 (85 %) | Kontrolle s = 0 trifft REGGE-ZEIT-1 auf <= 1e-4 | **eingetroffen**: 1,08722717 gegen 1,08722700 (1,7e-7) |
| A8 (80 %) | Drehung wie s = 0 auf 1e-9; Streckung c2 und c0s/c2 auf 0,1 % | **teilweise**: Streckung eingetroffen (0,04 %). Drehung nur in der Zeitrichtung vergleichbar (5e-9); sonst trifft die feste physikalische Richtung im gedrehten Gitter eine andere Gitterrichtung (Planfehler, Selbstanzeige 3). In Teil 2 gibt die Drehung dieselbe gamma-Reihe auf 5e-8 |

## 3. Tabellen

### 3.1 Netz und Nullmoden je s [E]

| | s = 0 | s = 0,1 | s = 0,2 |
|---|---|---|---|
| det A; Kondition A_raum | 1; 1 | 0,910; 1,32 | 0,802; 1,76 |
| Simplexvolumen (alle gleich) | 0,04167 | 0,03793 | 0,03343 |
| Dieder- / Dreieckswinkel (Grad) | 45-90 / 30-90 | 35,5-100,5 / 26,0-100,6 | 27,5-111,4 / 22,0-112,0 |
| rechte Winkel an der Hyperdiagonale | 14/14 | 2/14 | 2/14 |
| Nullmoden k = 0 | 11 | 10 | 10 |
| 11. abs(Eigenwert)/Mittel bei k = 0 | 6,8e-12 | 0,345 (Eigenwert -0,381) | 0,677 (Eigenwert -0,934) |
| Anteil e_top am 11. Eigenvektor | 0,04 | 0,60 | 0,58 |
| Nullmoden allgemein (144 Punkte) | 5 | 4 | 4 |
| kleinster Nicht-Eich-Eigenwert/Mittel | 3e-20 (Hyperdiagonale) | 3,2e-5 | 1,8e-5 |
| Signatur allgemein (pos/neg) | 9/1 | 9/2 | 9/2, an einzelnen Punkten 8/3 |
| BZ 8^4 (null/pos/neg) | 11/4/0 (q = 0); 5/9/1 (4095) | 10/4/1; 4/9/2 (4095) | 10/4/1; 4/9/2 (3551); 4/8/3 (544) |
| kleinster 5. Eigenwert in der BZ / Mittel | 7e-13 | 0,013 | 2,4e-5 |

- Die zwei rechten Winkel, die bleiben, gehoeren zu a = 1000 und a = 0111. A laesst die Zeitachse senkrecht zum Raum.
  Die anderen 12 Winkel werden stumpf (bis 107,9 Grad bei s = 0,2), dA/ds_top = -0,0057 bis -0,081.
- Kurve gegen s (Bild lauf-69/bild-eigenwerte-s.png): 11. Eigenwert / Mittel = 0,084 / 0,170 / 0,345 / 0,515 / 0,677
  bei s = 0,025 / 0,05 / 0,1 / 0,15 / 0,2, immer negativ.
  - Der kleinste Nicht-Eich-Eigenwert bei (1,2,3,4), 0,1 bleibt bei 7e-4 bis 1,1e-3 x Mittel (k^2-Mode).
  - Der kleinste unter 64 Zufalls-k faellt erst bei s = 0,2 auf 1,1e-3.

### 3.2 Form in physikalischen Koordinaten, Schur mit C = [e_top, C4] [E]

| s | Entartung Spin 2 max (bis 0,1) | c0s/c2 (bis 0,1) | c2-Streuung 0,05 / 0,1 | alle 80 Spin-2-Werte 0,1 | c2/(1/4) Mittel 0,05 / 0,1 |
|---|---|---|---|---|---|
| 0 | 0,12 % | -1,9996 bis -2,0018 | 0,016 / 0,065 % | 0,15 % | 0,9998 / 0,9992 |
| 0,1 | 0,18 % | -1,9993 bis -2,0026 | 0,020 / 0,081 % | 0,23 % | 0,9998 / 0,9992 |
| 0,2 | 0,31 % | -1,9989 bis -2,0047 | 0,027 / 0,107 % | 0,37 % | 0,9998 / 0,9990 |

- s = 0,2, Varianten: "orth" c0s/c2 bis -2,0041, Entartung 0,35 %; direkte Form c0s/c2 -1,9985 bis -1,9999,
  Entartung 0,21 %.
- Bei 0,2 und 0,4 (beschreibend, s = 0,2): c2/(1/4) = 0,992 bis 1,0003 bzw. c0s/c2 = -1,996 bis -2,019 (0,2) und
  -1,983 bis -2,073 (0,4).
- Spinmischung <= 1,2e-3 und Abweichung von (1/4) k^2 (P2 - 2 P0s) <= 0,32 % bei 0,1 (s = 0,2). Kontinuums-Eichmoden:
  Rest <= 4,3e-4 bei 0,05.
- Kww (C^T H C) hat bei s = 0,2 den kleinsten Betrag 0,36: die gehobene Hyperdiagonale. Nichts wurde verworfen.
- Bild: lauf-69/bild-spin2-richtung.png.

### 3.3 Ruhende Masse, s = 0,2, Achse A e_x [E]

abs(A e_x) = 0,8434, also r = 0,8434 x0.

| r | 4,22 | 5,06 | 5,90 | 6,75 | 7,59 | 8,43 | 9,28 | 10,12 | 10,96 | 11,81 | 12,65 | 13,49 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| gamma L = 32 | 1,1558 | 1,0916 | 1,0587 | 1,0411 | 1,0308 | 1,0244 | 1,0202 | 1,0174 | 1,0158 | 1,0152 | 1,0159 | - |
| gamma L = 48 | 1,1558 | 1,0915 | 1,0586 | 1,0409 | 1,0305 | 1,0239 | 1,0193 | 1,0161 | 1,0136 | 1,0117 | 1,0102 | 1,0091 |
| alpha L = 32 | 0,969 | 0,978 | 0,982 | 0,985 | 0,988 | 0,989 | 0,991 | 0,991 | 0,992 | 0,992 | 0,992 | - |
| gamma_kin L = 32 (Bericht) | 1,089 | 0,987 | 0,936 | 0,908 | 0,892 | 0,882 | 0,875 | 0,871 | 0,868 | 0,867 | 0,868 | - |

- gamma(6), interpoliert in 1/r^2: 1,0570 (L = 24), 1,0563 (L = 32), 1,0562 (L = 48). alpha(6) = 0,983.
- Kuhn (REGGE-ZEIT-1 und meine Kontrolle, L = 32): 1,0872 (6), 1,0564 (7), 1,0397 (8), 1,0234 (10), 1,0163 (12).
  Auf A e_x liegt das schiefe Netz also bei etwa 0,65- bis 0,75-facher Kuhn-Abweichung.
- **Andere Achsen (beschreibend):**

| Achse | abs(A e) | gamma(6) L = 32 / 48 | alpha(6) | (gamma - 1) r^2 bei r ~ 6 / Schwanz (L = 48) |
|---|---|---|---|---|
| A e_x | 0,843 | 1,0563 / 1,0562 | 0,983 | 2,0 / +1,65 |
| A e_y | 0,855 | 1,3078 / 1,3079 | 1,189 | 11,1 / +1,65 |
| A e_z | 1,206 | 1,1131 / 1,1132 | 1,106 | 3,9 / -1,1 |

- Auf A e_y faellt der Zusatz ueber dem Schwanz mit etwa dem Faktor 1,38 je 0,86 Gitterabstaende, also etwa wie
  exp(-r/2,7). Auf A e_z schiesst gamma bei r ~ 8 unter 1 und naehert sich von unten (0,991 bei r = 10,9).
- Zeilennormierte Kondition des 2x2-Systems 1,53 bis 1,58 auf allen Achsen.
- Bild: lauf-69/bild-gamma.png (links gamma, rechts alpha).

### 3.4 Kalibrierung (schiefe Dreiecke) [E]

- Versklavungssystem C^T M0 C (5 Gittermoden, Vorzeichen von M): -12,07; -3,61; -2,21; -1,74; **+0,360**. Kondition
  33,5. Bei s = 0 (4 Moden): -8; -2; -2; -2.
- Versklavungsanteil 72 % (N) bzw. 51 % (S); s = 0: 59 % bzw. 44 %.
- Antwort der Quadrate auf die Kruemmung der Punktmasse auf der Achse (Einheit 2 G M/r^3, versklavt):

| Achse | Zeit-Quadrate N / S | Quer-Quadrate N / S |
|---|---|---|
| A e_x | -0,582 / 1,473 | 0,966 / -0,050 |
| A e_y | -0,183 / 0,715 | 1,802 / -0,290 |
| A e_z | -0,344 / 0,843 | 1,672 / -0,090 |

- Kuhn: -0,25 / 1,25 und 1,25 / -0,25. Fuer Einstein (N + S) ergibt sich im schiefen Netz nicht mehr 1,000; die
  Quadrate sehen die Kruemmung ihrer schiefen Normalebene samt Uebersprechen.

### 3.5 Nachtraegliche Diagnose (nach dem Einfrieren, nicht geurteilt) [E]

- Statisches Gitter L = 32, s = 0,2, code/diagnose_statisch.py.
- Kleinster 5. Eigenwert: 1,26e-5 x Mittel bei k_lat = (0; 2,945; +-0,196; +-0,393), also nahe dem Zonenrand in x.
  - Eigenwert +1,9e-5; h-Anteil 0,86; e_top-Anteil 0,18; Ueberlapp mit der Quelle 1,3e-5.
- 31 der 32767 statischen Punkte haben 3 negative Eigenwerte, die uebrigen 2. 56 Punkte liegen unter 1e-3 x Mittel,
  2 unter 1e-4.
- **Folge:** Eine kurzwellige Gittermode geht bei s = 0,2 durch null. Die Loesung ist dort fast singulaer. Wegen des
  kleinen Quellueberlapps und der Paarmittelung bleibt gamma(6) davon unberuehrt (L = 24/32/48 gleich auf 8e-4).

## 4. Kontrollen

- **Geometrie:**
  - flach 1,8e-15 / 2,7e-15 / 4,4e-15 (s = 0 / 0,1 / 0,2), skaliert (l x 1,3) 1,8e-15 / 3,6e-15 / 5,3e-15.
  - Weg T gegen J 1,9e-12 bis 2,6e-12, T gegen K 3,8e-12 bis 6,4e-12; Richardson-Fehler <= 5,8e-11.
  - Schlaefli je Simplex <= 1,4e-15, global <= 3,6e-11.
- **M(k):** Imaginaerteil <= 1,7e-12; Affinmoden bei k = 0 im Kern (<= 1,0e-12); Eichmoden (<= 1,0e-12);
  rang(B_phys) = 10, rang ohne top-Zeile = 10.
- **Codeproben:**
  - s = 0 gleich REGGE-4D-1 (c2 und c0s/c2 in den 8 alten Richtungen; BZ 11/4/0 und 5/9/1).
  - Drehung: 11/5 Nullmoden; Zeitrichtung c2 auf 5e-9; Teil 2 dieselbe gamma-Reihe auf 5e-8.
  - Streckung diag(1,15; 0,9; 1,05): 11/5 Nullmoden (rechte Winkel bleiben); c2/(1/4) >= 0,9996, c0s/c2 -1,99997 bis
    -2,0005 bei 0,05.
- **Teil 2:**
  - Quelle auf dem Nullraum <= 6,5e-16; Gleichungsresiduum <= 5,3e-10; Nullraumresiduum 1,2e-12.
  - Fehlwinkel der Eichmoden <= 5,5e-13; Imaginaerteil der Felder <= 7,9e-15.
  - RNC gegen statisch 4,8e-12 bzw. 1,3e-11; Ursprungsverschiebung 1,4e-10.
  - Hintergrund-Richardson: kappa-Differenz 2,1e-4 bei max abs(F0) 16,3; s = 0: 5,1e-5 bei 7,5. Bilder: 21376 in der
    physikalischen Kugel.
  - Kontrolle s = 0 (gleicher Code, Kugelbilder): gamma(6) = 1,08722717 (L = 32) und 1,0874 (L = 24) gegen REGGE-ZEIT-1
    1,08722700 bzw. 1,0874.
- **Latten (v3):**
  - L1 (kann scheitern): ja.
    - SC3 ist gescheitert.
    - SC1 haette an einer durch null gehenden Mode scheitern koennen; die BZ zeigt, dass es sie bei s = 0,2 gibt,
      nur nicht an den 144 Punkten.
    - SC2 haette an der leichten Mode scheitern koennen.
  - L2 (Gegenprobe): s = 0 mit demselben Code; Drehung und Streckung; Schur, orth und direkt; drei Achsen;
    L = 24/32/48; Wege T, J und K.
  - L3 (Numerik): 1e-12 bis 1e-15.
  - L4 (schon bekannt): Regge-Konvergenz fuer dicke Simplizes [L, Cheeger/Mueller/Schrader]; die fuenfte Nullmode bei
    Rocek/Williams [S, ueber REGGE-4D-1]. Ob die negative Diagonalmode im schiefen Gitter in der Literatur steht, habe
    ich nicht geprueft.
  - L5 (Messbezug): keiner.

## 5. Selbstanzeigen

1. **Zwei Fehlstarts durch Shell-Klammerung.**
   - Rauchlauf 1: Nur r1 lief; die anderen Starts brachen vor dem Programmstart ab.
   - Hauptlauf: Teil 2 startete zuerst im falschen Arbeitsordner und endete nach 23 ms mit rc = 2 ("can't open file").
     Es wurde nichts gerechnet. Neu gestartet um 02:30:50 UTC.
   - Kein Einfluss auf Daten.
2. **Vor dem Einfrieren unbeabsichtigt gesehen:** die Eigenwerte des Versklavungssystems bei s = 0,2 (+0,360 in M, also
   eine negative Mode in H) und die Flachheit bei s = 0,2. Sie standen in der Logzeile von Rauchlauf r1-s02.
   - A2 stand vorher im Plan; Schwellen und Regeln blieben unveraendert.
   - Nullmodenzahlen und gamma fuer s != 0 habe ich vor dem Einfrieren nicht gesehen.
3. **A8 schlecht formuliert:** Eine feste physikalische Richtung trifft im gedrehten Gitter eine andere Gitterrichtung.
   "Gleich s = 0" galt deshalb nur fuer die Zeitrichtung. Als "teilweise" beurteilt; nichts umgeschrieben.
4. **Festlegungen mit Gewicht:**
   - [F6] Lesart der SC2-Teile. Andere Lesarten (alle 80 Werte, orth, direkt) aendern das Urteil nicht (alle < 0,5 %).
   - [F9] Achse A e_x und Interpolation in 1/r^2. Am Gitterpunkt und auf den anderen Achsen ist die Abweichung groesser;
     das Urteil SC3 ist davon unabhaengig.
   - Die Achse A e_x ist zufaellig die mildeste der drei Achsen. Ausgewaehlt war sie vor jeder Rechnung.
5. **Nachtraegliche Diagnose:** code/diagnose_statisch.py ist nach dem Einfrieren neu geschrieben. Es importiert den
   eingefrorenen Code unveraendert, ist beschreibend und nicht geurteilt.
6. **Lokale Werkzeuge:** Ausser jq, ssh, scp, sha256sum, date, grep und sed habe ich lokal ls, cp, mkdir, cat, head, rm
   und tr benutzt (Auflisten, Kopieren, Formatieren; rm nur fuer die zwei Zwischendateien *.json.teil in lauf-69). Kein
   python, awk oder perl lokal.
7. **auswertung.json nachbearbeitet:** Die Vermerke sind per jq eingetragen. Die Maschinenfassung ist
   lauf-69/auswertung.maschine.json; Urteile und Werte sind identisch (diff).
8. **A4:** "Schur-Korrektur der leichten Mode" war im Plan nicht als Zahl definiert. Beurteilt habe ich nach dem
   Unterschied Schur gegen direkt.
9. **Reichweite:**
   - Linear, euklidisch, statisch (Teil 2), eine feste Matrix B.
   - Andere B, insbesondere -B (Vorzeichen der Diagonalmode), sind nicht gerechnet.
   - "Ungeordnet" ist hier nur "schief": Das Netz ist weiter periodisch mit gleichen Zellen. Ein zufaelliges Netz kann
     sich anders verhalten [H].
10. **Zeitbox:** Start 04:01:00, Text ab 04:36:46 CEST, innerhalb von 120 min.

## 6. Bedeutung

- **Zu Finns Frage "Ist ein schiefes bzw. ungeordnetes Netz besser als ein Kristall?":**
  - Fuer lange Wellen gleich gut. Das schiefe Netz gibt Einsteins Form in physikalischen Koordinaten so genau wie der
    Kristall (Abweichungen 0,1 bis 0,4 % bei abs(k) = 0,1).
  - Der tote Strich verschwindet; man braucht keine Abmachung mehr, um Kruemmung abzulesen.
  - Aber der Strich wird zu einer Verformung mit negativer Steifigkeit, einer zweiten "Minus-Richtung" neben dem
    konformen Modus, diesmal auf Gitterlaenge. Bei s = 0,2 geht zudem eine kurzwellige Gittermode durch null.
  - Nahe der Masse ist das schiefe Netz nicht besser: Die Abweichung haengt stark von der Richtung ab (5,6 / 31 / 11 %
    bei r = 6). Kuhn hat auf allen drei Achsen 8,7 %.
- **[H]** Die negative Diagonalmode haengt in erster Ordnung am Vorzeichen der Schiefe. Ein ungeordnetes Netz mischt
  beide Vorzeichen, mittelt dann vermutlich die Anisotropie heraus und hat gleichzeitig Stellen mit Minus-Moden. Das ist
  ungeprueft.
- **Hineingesteckt** sind die Regge-Wirkung und die Eigenzeit-Kopplung (Regime A). Aus Punkten und Strichen allein folgt
  hier nichts.
- **Naechste Schritte [H]:**
  1. Dasselbe mit -B: Wird die Diagonalmode positiv, und wird die Nahzone ruhiger?
  2. Richtungsmittel von gamma(6) ueber viele physikalische Achsen.
  3. Ein wirklich zufaelliges (nicht periodisches) Netz, z. B. Delaunay aus Zufallspunkten; dann ohne Fourier, direkt
     im Ortsraum.

## 7. Dateien

- PLAN.md, PLAN.md.eingefroren-20261004-042832, EINGEFROREN-SHA256.txt
- code/:
  - regge_schief.py: Gitter X -> A X, Teil 1 (Moden, Form) und Teil 2 (Masse)
  - regge_schief_auswertung.py: Urteile und Bilder
  - regge4d.py, regge_zeit.py: unveraendert aus REGGE-4D-1 bzw. REGGE-ZEIT-1
  - jeweils mit Kopien *.eingefroren-20261004-042832
  - diagnose_statisch.py: nachtraeglich, nicht eingefroren
- lauf-69/:
  - teil1.json/.log, teil2-s0.json/.log, teil2-s02.json/.log
  - auswertung.json (mit Vermerken), auswertung.maschine.json, auswertung.log
  - bild-eigenwerte-s.png, bild-spin2-richtung.png, bild-gamma.png
  - diagnose-statisch.json/.log
  - PRUEFSUMMEN.txt (.69), PRUEFSUMMEN-lokal.txt
- rauch-69/: rauch0, r1 (Teil 1 s = 0 mit Codeproben), r1-s0, r1-rot, r1-s02, r1-s0L32, probe-teil1.json und
  probe/ (Auswertungsprobe)
- Auf der .69: /home/fmh/fmhc-physics-remote/runde37-schief/ (code/, rauch/, lauf/)

## 8. Einfach gesagt

Im Kristallnetz gab es einen "toten" Strich, die lange Wuerfeldiagonale: Er kostete nichts, weil alle Dreiecke an ihm
einen rechten Winkel hatten. Wir haben das ganze Netz schief gezogen, sodass diese rechten Winkel verschwinden. Der tote
Strich ist damit weg, und fuer lange Wellen verhaelt sich das Netz weiter genau wie Einsteins Schwerkraft. Dafuer bekommt
der Strich jetzt eine "verkehrte" Steifigkeit: Ihn zu verformen senkt die Energie, statt sie zu erhoehen. Nahe einer
Masse wird das Netz nicht genauer, sondern ungleichmaessiger: je nach Richtung 6, 31 oder 11 Prozent daneben statt
ueberall 9 Prozent. Ein schiefes Netz ist also nicht einfach besser als ein Kristall; es tauscht einen Fehler gegen
einen anderen.
