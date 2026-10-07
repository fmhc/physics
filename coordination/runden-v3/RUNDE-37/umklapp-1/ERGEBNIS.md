# UMKLAPP-1: Ergebnis (Code-Agent fuer die Leitung claude-primary, Runde 46, Finn-Auftrag "Try it")

- Finn (05.10.2026), woertlich: "Meine Tetraeder können zufällig und unregelmäßig sein. Zellen umklappen - wie und mit
  welchem Mechanismus? Try it."
- Alle Zahlen sind synthetische Gitterrechnungen auf der .69 (numpy 2.4.4, scipy 1.18.0, 1 Thread), keine Messdaten.
- **Kennzeichen:** [E] hier gerechnet, [M] Mathematik (vorab ableitbar), [P] Projektdatei, [F] Festlegung im Plan,
  [H] Hypothese oder Lesart, [L] Literatur aus dem Gedaechtnis (nicht an der Quelle geprueft).
- **Begriffe:**
  - "Netz" = periodisches 3D-Poisson-Delaunay-Netz aus TT-GLAS-1 (N Punkte, Dichte 1, mittlere Kantenlaenge 1,26 bis
    1,31).
  - "2-3-Zug" = zwei Tetraeder abcd, abce mit gemeinsamer Flaeche werden zu abde, bcde, cade um die neue Kante d-e;
    erlaubt nur bei konvexer Doppelpyramide, jedes neue Volumen >= 1e-3 des Mittels, ohne doppelte Kante (PLAN 2).
  - "f" = Zahl der zufaelligen 2-3-Zuege geteilt durch die Zahl der Flaechen des Ausgangsnetzes.
  - "a" = Effektivwert der Eckverschiebung geteilt durch die mittlere Kantenlaenge.
  - "phi_T" = Anteil der Tetraeder, die nach der Verschiebung im neu berechneten Delaunay-Netz fehlen.
  - "Spanne" = max/min - 1 ueber 26 Werte omega^2/k^2 (13 Richtungen x 2 TT-Zweige, |k| = 1e-2), wie TT-GLAS-1.
  - "regulaer" = an allen 16 Punkten genau zwei masselose Moden, beide positiv, nichts waechst, nichts unklar,
    TT-Anteil >= 0,99, linear (TT-GLAS-1).
  - "wachsend" = Mode mit negativem omega^2 oder komplexem omega^2, also eine Instabilitaet.

## 1. Zeiten und Laeufe

- **Ablauf (Zeiten per date; .69 in UTC, CEST = UTC + 2):**
  - Start 2026-10-05 05:54:29 CEST. Code ab 06:07:34 CEST, Plantext ab 06:14:02 CEST, vor jeder Hauptrechnung.
  - Rauchtests r1 bis r3 04:11:08 bis 04:13:30 UTC (--rauch), r4 04:16:02 bis 04:18:10 UTC (Rauchsaaten 901, 902;
    Absturzprobe). Gelesen nur Rueckgabewerte, Laufzeiten, Speicher, Schluessel (Selbstanzeige 2).
  - Eingefroren 2026-10-05 06:19:02 CEST: PLAN.md.eingefroren-20261005-061902 (sha256 a943ee93...), code/uk.py
    (f52df743...), code/uk_auswertung.py (a5e55f88...), code/uk_bild.py (d6c506af...), kette-cpu3.sh (5e799c8d...),
    kette-cpu4.sh (21e7011e...); tg.py, tg_auswertung.py, ew.py, tp.py unveraendert aus TT-GLAS-1 (ec48a258...,
    88cbd2ce..., fa7b6417..., 419d7da6...). Auf der .69 dieselben Summen (EINGEFROREN-SHA256-69.txt); nach den Laeufen
    lokal und auf der .69 erneut alle gleich.
  - Laufketten 04:19:08 bis 05:01:07 UTC, Spuren cpu3 und cpu4, alle 21 Laeufe rc = 0, der laengste 368,0 s.
    End-Auswertung, Bild und Nachtrag-Tabelle 05:01:09 bis 05:01:11 UTC, rc = 0. lauf-69/PRUEFSUMMEN.txt (48 Dateien) und
    nachtrag-69/PRUEFSUMMEN.txt (8 Dateien, auf der .69 erzeugt) stimmen lokal.
  - Hinweis der Leitung 06:20 CEST (HODGE-L) -> Nachtrag V 04:39:12 UTC (4.4); Nachtrag-Bild 05:02:46 UTC.
  - Text ab 06:27:07 CEST. Abschluss siehe Dateiende.
- **Laeufe** (Aufruf jeweils `kleintest.sh <Spur> <Name> code/uk.py ...`; Start = Beginn am Lock):

  | Lauf | Spur | Aufruf (Kurzform) | Start | Ende | Laufzeit | rc |
  |---|---|---|---|---|---|---|
  | uk-ko128 | cpu3 | kontrolle --N 128 --saaten 1-4 | 04:19:08 | 04:19:31 | 21,8 s | 0 |
  | uk-ko256 | cpu3 | kontrolle --N 256 --saaten 1-4 | 04:19:31 | 04:20:53 | 81,2 s | 0 |
  | uk-mb128 | cpu3 | mb --N 128 --saaten 1-48 --zieh 8 | 04:20:53 | 04:23:27 | 153,5 s | 0 |
  | uk-tt128-f0 | cpu3 | tt --N 128 --saaten 1,2,3,4 --f 0 | 04:23:27 | 04:25:52 | 144,5 s | 0 |
  | uk-aw1 | cpu3 | uk_auswertung.py (Zwischenstand) | 04:25:52 | 04:25:53 | ~1 s | 0 |
  | uk-tt128-f02a | cpu3 | tt --N 128 --saaten 1,2 --f 0.2 | 04:25:52 | 04:30:18 | 264,5 s | 0 |
  | uk-tt128-f02b | cpu3 | tt --N 128 --saaten 3,4 --f 0.2 | 04:30:18 | 04:34:34 | 254,7 s | 0 |
  | uk-tt256-s1-f02-A/B/C | cpu3 | tt --N 256 --saaten 1 --f 0.2 --ridx 0-3 / 4-8 / 9-12 | 04:34:34 | 04:50:51 | 366,6 / 303,4 / 305,2 s | 0 |
  | uk-tt256-s3-f02-A/B | cpu3 | tt --N 256 --saaten 3 --f 0.2 --ridx 0-3 / 4-8 | 04:50:51 | 05:01:07 | 338,9 / 275,8 s | 0 |
  | uk-mb256a | cpu4 | mb --N 256 --saaten 1-24 --zieh 8 | 04:19:10 | 04:21:06 | 115,0 s | 0 |
  | uk-mb256b | cpu4 | mb --N 256 --saaten 25-48 --zieh 8 | 04:21:06 | 04:22:57 | 110,5 s | 0 |
  | uk-tt256-s2-f02-A/B/C | cpu4 | tt --N 256 --saaten 2 --f 0.2 --ridx 0-3 / 4-8 / 9-12 | 04:22:57 | 04:39:11 | 368,0 / 305,3 / 299,0 s | 0 |
  | uk-nt-v (Nachtrag) | cpu4 | nachtrag_v.py | 04:39:12 | 04:39:12 | 0,3 s | 0 |
  | uk-tt128-f005 | cpu4 | tt --N 128 --saaten 1,2,3,4 --f 0.05 | 04:39:12 | 04:42:22 | 188,6 s | 0 |
  | uk-tt256-f0p | cpu4 | tt --N 256 --saaten 1,2,3 --f 0 --ridx 0 | 04:42:22 | 04:44:13 | 110,6 s | 0 |
  | uk-nt-tab0 (Probe) | cpu4 | nachtrag_tabelle.py auf dem Zwischenstand | 04:44:13 | 04:44:13 | < 1 s | 0 |
  | uk-tt256-s1-f005-A/B | cpu4 | tt --N 256 --saaten 1 --f 0.05 --ridx 0-5 / 6-12 | 04:44:13 | 04:50:17 | 184,0 / 178,0 s | 0 |
  | uk-tt256-s3-f02-C | cpu4 | tt --N 256 --saaten 3 --f 0.2 --ridx 9-12 | 04:50:17 | 04:55:00 | 282,0 s | 0 |
  | uk-aw | cpu3 | uk_auswertung.py --lauf lauf --ttglas .../tt-glas-1/lauf | 05:01:09 | 05:01:09 | < 1 s | 0 |
  | uk-bild | cpu3 | uk_bild.py | 05:01:09 | 05:01:11 | ~2 s | 0 |
  | uk-nt-tab (Nachtrag) | cpu4 | nachtrag_tabelle.py | 05:01:11 | 05:01:11 | < 1 s | 0 |
  | uk-nt-bild (Nachtrag) | cpu3 | nachtrag_bild.py | 05:02:43 | 05:02:46 | ~3 s | 0 |

## 2. Ergebnis zuerst

1. **Ein flacher Umklapp kostet keine Regge-Energie (UK0 eingetroffen) [E; vorab ableitbar].** 16 Netzzustaende mit 85
   bis 696 zufaelligen 2-3-Zuegen: |Delta S| <= 3,6e-12, relativ <= 1,5e-16. Die Zuege fuellen den Kasten richtig
   (Volumensumme auf 4,4e-16, alle Fehlwinkel <= 5,4e-13). Die Regge-Energie kann Zuege also weder antreiben noch bremsen.
2. **Delaunay-Umklappen (M-B) waechst im Mittel ueber Netze etwa proportional zur Amplitude, ohne Schwelle im Mittel
   (UK1 eingetroffen) [E; weitgehend vorab ableitbar].** phi_T ~ 7,5 a (8,1 a bei a = 1e-4, 6,4 a bei 3e-2); Steigung
   0,95, zwischen 1e-4 und 1e-3 lokal 0,97. Je einzelnes Netz gibt es eine Schwelle (sein kleinster Randabstand); bei
   a = 1e-4 klappt in mindestens 72 % (N = 128) bzw. 42 % (N = 256) der Ziehungen nichts um [Kopfrechnung].
   Bei kleinem a sind fast alle Aenderungen einzelne 2-3- oder 3-2-Zuege (96 % bei a = 1e-3), beide etwa gleich oft.
   Grund: Die Randabstaende zur Kugel-Entartung sind vertraeglich mit einer endlichen Dichte bei null (etwa 2). Eine
   lange TT-Welle (affine Dehnung a) verletzt etwa 1,2 a der Flaechen.
3. **Zufaellige 2-3-Zuege (nur Verfeinerung, Volumenschwelle 1e-3) machen Finns Netz instabil (UK2 verfehlt) [E].**
   Keines der 7 Netze mit f = 0,2 ist regulaer; an allen 16 k-Punkten gibt es wachsende Moden, hoechstens 68 bis 79 je
   Netz (N = 128) bzw. 139 bis 154 (N = 256), je Punkt um bis zu 3 verschieden. Schon bei f = 0,05 (85 bis 174 Zuege)
   sind es 14 bis 30. Quelle sind negative Richtungen der reduzierten Regge-Matrix; auf fuenf Zuege kommt etwa eine
   (Verhaeltnis der Zaehlungen 0,16 bis 0,22); bei f = 0,2 ist auch die reduzierte Bewegungsmatrix nicht mehr positiv
   definit. Die Zahl haengt kaum von k ab, es sind wohl lokale Instabilitaeten [H]. Die zwei TT-Zweige bleiben bei
   f = 0,05 erhalten (TT-Anteil 1,000000); bei f = 0,2 fehlt an einzelnen Punkten einer (N = 128 Saat 2, N = 256
   Saaten 1 und 2). Gemischte 2-3/3-2-Folgen und strengere Formschwellen sind nicht gerechnet.
4. **UK3 ist nicht entscheidbar [E].** Die Regel verlangt regulaere Netze bei f = 0 und 0,2; es gibt keines bei
   f = 0,2. Beschreibend bei f = 0,05: Die Spanne aendert sich je Netz um +41, +41, -3, -4 % (N = 128) und +29 %
   (N = 256), omega^2/k^2 faellt um 15 bis 18 %. Das Zufallsniveau zweier unabhaengiger Netze liegt bei 24 % (N = 128)
   bzw. 16 % (N = 256); die Aenderungen gelten zudem fuer instabile Netze.
5. **Mechanismus [H]:** Die Regge-Energie ist blind fuer Umklappungen, und zufaellige 2-3-Zuege zerstoerten hier die
   Stabilitaet. Das spricht fuer eine Auswahlregel. Delaunay-Netze waren bei kleinem k stabil: f = 0 hier, 48 von 48 in
   TT-GLAS-1 [P], und V nach seinen 12 Delaunay-Zuegen je Zelle (Nachtrag 4.4: vorher nicht Delaunay, nachher schon,
   weiter regulaer, Spanne 15,4 % statt 6,3 %). Noetig ist Delaunay dafuer nicht: V selbst ist nicht Delaunay und
   trotzdem regulaer. Fuer Finns Takt passt: Umklappen als Zeitschritt (M-C, Zeltstangen), Delaunay als Auswahlregel;
   ein solcher Takt ist nicht gerechnet.

## 3. Urteile

Mechanisch durch code/uk_auswertung.py (eingefroren 06:19:02 CEST), lauf-69/auswertung.json; Regeln PLAN Abschnitt 5.

| Nr | Vorhersage (Kurzform) | Wahrsch. | nach Plan | nach Kartenwortlaut | tragende Zahlen [E] |
|---|---|---|---|---|---|
| UK0 | Kontrolle [vorab ableitbar]: flache 2-3-Zuege aendern die Regge-Wirkung auf <= 1e-10 nicht | 90 % | **eingetroffen** | **eingetroffen** | 16 Netzzustaende (N = 128 und 256, je 4 Saaten, f = 0,05 und 0,2): max \|Delta S\| = 3,6e-12 (Plan: relativ 1,5e-16) |
| UK1 | [H] M-B-Anteil waechst ohne Schwelle linear (log-log-Steigung 1 +- 0,2 zwischen 1e-3 und 3e-2) | 60 % | **eingetroffen** | **eingetroffen** | Steigung 0,945 (N = 128), 0,960 (N = 256), 0,953 (alle 96 Netze); lokal 1e-4 bis 1e-3: 0,967; phi_T(1e-4) = 7,8e-4 bzw. 8,4e-4 > 0 |
| UK2 | [H] Nach f = 0,2 hat jedes Netz bei kleinem k genau zwei masselose TT-Moden und ist stabil | 65 % | **verfehlt** | **verfehlt** | 0 von 7 Netzen (N = 128: Saaten 1-4; N = 256: Saaten 1-3) regulaer, 0 von 7 nach Wortlaut; an allen 16 Punkten wachsende Moden (Hoechstwert je Netz 68-79 bzw. 139-154); an einzelnen Punkten nur 1 masselose Mode (N = 128 Saat 2; N = 256 Saaten 1, 2; Saat 2 auch 3); dazu "unklar" in 5 von 7 Netzen und "nicht linear" (N = 128 Saaten 3, 4) |
| UK3 | [H] Zuege aendern die Spanne je Netz um mehr als 20 % | 50 % | **nicht entscheidbar** | **nicht entscheidbar** | kein Paar: kein Netz mit f = 0,2 ist regulaer (Regel PLAN 5 verlangt beide regulaer); beschreibend 4.2. Vermerk: Der Plantext regelt den Fall "kein Paar" nicht ausdruecklich (woertlich waere "jedes \|r\| > 0,2" auf leerer Menge erfuellt); das Urteil folgt dem eingefrorenen Code (uk_auswertung.py: ohne Paar "nicht entscheidbar") |

- **Vorab ableitbar:** UK0 ganz [M]; UK1 weitgehend [M, mit Annahme endlicher Randdichte bei null, PLAN 1]. Die
  Daten sind mit der Annahme vertraeglich: Der Anteil der Flaechen mit Randabstand unter x waechst wie x^0,958, etwa
  2 x (4.1). Beide Urteile sind daher keine Entdeckung; gemessen sind der Vorfaktor (phi_T ~ 7,5 a) und der Bereich.
- **Bedeutung, wie auf der Karte vorab festgelegt:**
  - "UK1 trifft ein: In einem Glas loest jede Welle Umklappungen aus. Mit M-B gehoeren sie dann zur Dynamik, ohne
    Schwelle." **Ausgeloest.**
  - "UK0 und UK2 treffen ein, UK3 verfehlt" (neutrale Umdiskretisierung, Isotropie bleibt): **nicht ausgeloest**, weil
    UK2 verfehlt ist.
  - "UK3 trifft ein" (Kopplung wie Phasonen): **nicht ausgeloest** (nicht entscheidbar).
  - Fuer "UK2 verfehlt" hat die Karte keinen Satz. Lesart [H]: Zufaellige 2-3-Zuege (Verfeinerung, Volumenschwelle
    1e-3) waren in Finns Hamilton-Netz keine neutrale Umdiskretisierung; sie brachten negative Richtungen und damit
    wachsende Moden. Das spricht dafuer, dass ein Mechanismus die Zuege auswaehlen muss (Abschnitt 5); gemischte
    2-3/3-2-Folgen und strengere Formschwellen sind nicht geprueft.
- **Agenten-Vorhersagen** (PLAN 6, kein Urteil):
  - A1 (30 bis 70 % der Flaechen zu Beginn erlaubt): eingetroffen, 33,1 bis 36,8 %.
  - A2 (f = 0,2 in allen Netzen erreicht): eingetroffen, in allen 8 Netzen mit Zuegen (N = 128 und 256, Saaten 1 bis
    4) die volle Zielzahl; am Ende waren noch 3,6 bis 4,4 % der Flaechen erlaubt.
  - A3 (omega^2/k^2 bei f = 0,2 mehr als 10 % hoeher): verfehlt, es faellt (4.2).
  - A4 (phi_T / a bei 1e-3 zwischen 1 und 10): eingetroffen, 7,5.
  - A5 (mindestens 90 % Einzelzuege bei a = 1e-3): eingetroffen, 96,2 %.
- **Bilder:** lauf-69/bild-umklapp.png (eingefroren; rechts lineare Achse, dort von den instabilen Netzen mit Spannen
  bis 3 456 % beherrscht) und nachtrag-69/bild-nachtrag.png (Nachtrag: logarithmische Achse, offene Symbole =
  instabil; rechts wachsende Moden gegen die Zugzahl). Beide auf der .69 erzeugt.

## 4. Tabellen

### 4.1 Umklappanteil gegen a (M-B; 48 Netze je N, je 8 Ziehungen) [E]

| a | phi_T N = 128 (+- SE) | phi_T N = 256 (+- SE) | phi_T alle 96 | phi_T / a | phi_F alle (verletzte Flaechen) | Bereiche 2-3 / 3-2 / sonst (alle) | Anteil Einzelzuege | phi_F affine TT-Dehnung |
|---|---|---|---|---|---|---|---|---|
| 1e-4 | 7,83e-4 +- 1,5e-4 | 8,44e-4 +- 0,8e-4 | 8,13e-4 | 8,1 | 3,20e-4 | 167 / 161 / 1 | 99,7 % | 1,15e-4 |
| 1e-3 | 7,64e-3 +- 0,53e-3 | 7,44e-3 +- 0,32e-3 | 7,54e-3 | 7,5 | 2,97e-3 | 1 446 / 1 363 / 112 | 96,2 % | 1,28e-3 |
| 1e-2 | 6,96e-2 +- 0,16e-2 | 7,09e-2 +- 0,10e-2 | 7,02e-2 | 7,0 | 2,69e-2 | 8 710 / 8 734 / 4 928 | 78,0 % | 1,20e-2 |
| 3e-2 | 0,1886 +- 0,0023 | 0,1929 +- 0,0016 | 0,1908 | 6,4 | 7,04e-2 | 10 990 / 11 044 / 16 893 | 56,6 % | 3,27e-2 |
| 1e-1 | 0,4857 +- 0,0036 | 0,4916 +- 0,0022 | 0,4887 | 4,9 | 0,174 | 3 251 / 3 266 / 5 836 | 52,8 % | 9,25e-2 |

- SE = Standardfehler ueber die 48 Netze. Bereiche = zusammenhaengende Aenderungsgebiete, Summe ueber alle Netze und
  Ziehungen; "Anteil Einzelzuege" = (2-3 + 3-2) / alle Bereiche [Kopfrechnung]. Die affine TT-Dehnung ist der
  Grenzfall einer langen Welle (Zusatz W, Mittel ueber [100], [110], [111] und beide Polarisationen).
- Steigungen (Gerade ueber a = 1e-3, 1e-2, 3e-2): phi_T 0,945 (N = 128), 0,960 (N = 256), 0,953 (alle); lokal zwischen
  1e-4 und 1e-3: 0,967 (alle); ueber alle fuenf a: 0,936. phi_F: 0,935; Dehnung: 0,956.
- Randabstaende im Ausgangsnetz (Anteil der Flaechen mit mu0 < x, alle 96 Netze): 1,96e-4 (x = 1e-4), 1,82e-3 (1e-3),
  1,73e-2 (1e-2), 4,91e-2 (3e-2), 0,142 (0,1); Steigung 0,958. Das ist vertraeglich mit einer endlichen Dichte bei
  null, etwa 2 je Einheit mu [E]; Anteil/x steigt zu kleinem x leicht (1,42 bis 1,96), und bei x = 1e-4 sind es nur
  rund 49 Flaechen (Zufallsfehler ~14 %) [Kopfrechnung]. Kleinster Randabstand 1,2e-6, kein negativer (alle
  Ausgangsnetze sind Delaunay).
- **Schwelle je Netz:** Ein endliches Netz hat einen kleinsten Randabstand (je Netz bis hinab zu 1,2e-6); darunter
  klappt nichts um. Bei a = 1e-4 gab es 108 (N = 128) bzw. 221 (N = 256) Aenderungsbereiche auf je 384 Ziehungen, also
  in mindestens 72 % bzw. 42 % der Ziehungen keinen Umklapp [Kopfrechnung]. "Ohne Schwelle" gilt fuer das Mittel ueber
  Netze, nicht fuer das einzelne Netz [M, PLAN 1].
- Proben: Ohne Verschiebung entsteht in allen 96 Netzen genau die Ausgangsmenge; keine Umkugel ragt ueber den Saum.

### 4.2 TT-Wellen gegen f [E]

Quelle: lauf-69/auswertung.json (Zaehlung, Stabilitaet, Urteile) und nachtrag-69/tabelle.json (Mittel ueber alle
vollstaendigen Netze, auch nicht regulaere; Nachtrag, Selbstanzeige 5). Werte je Netz in der Reihenfolge der Saaten.

| N | f | Netze (Saaten) | Zuege je Netz | regulaer | wachsende Moden je Punkt (max je Netz) | B_red negativ | A_red pos. def. | masselos je Punkt | TT-Anteil min | Spanne je Netz % | omega^2/k^2 Mittel | Tempo Mittel | kleinste Luecke omega^2 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 128 | 0 | 4 (1-4) | 0 | 4 von 4 | 0 | 0 | alle | 2 | 1,000000 | 10,9 / 11,4 / 23,7 / 12,5 | 4,850 +- 0,026 | 2,202 | 4,82 |
| 128 | 0,05 | 4 (1-4) | 86 / 87 / 87 / 85 | 0 von 4 | 15 / 19 / 15 / 14 | 15 / 19 / 15 / 14 | alle | 2 | 1,000000 | 15,4 / 16,0 / 23,1 / 11,9 | 4,046 +- 0,061 | 2,011 | 0,050 |
| 128 | 0,2 | 4 (1-4) | 345 / 347 / 349 / 340 | 0 von 4 | 74 / 68 / 75 / 79 | 70 / 64 / 71 / 75 | keins | 2 (Saat 2 an einem Punkt 1) | nicht berechnet | 66 / - / 489 / 3 456 | 3,30 +- 0,79 (3 Netze) | 1,75 | 0,012 |
| 256 | 0 | 3 (1-3), aus TT-GLAS-1 | 0 | 3 von 3 | 0 | 0 | alle | 2 | 1,000000 | 12,3 / 10,7 / 11,9 | 4,991 +- 0,068 | 2,234 | 3,42 |
| 256 | 0,05 | 1 (1) | 174 | 0 von 1 | 30 | 30 | ja | 2 | 1,000000 | 15,9 | 4,047 | 2,011 | 0,164 |
| 256 | 0,2 | 3 (1-3) | 696 / 692 / 681 | 0 von 3 | 151 / 139 / 154 | 142 / 131 / 147 | keins | 1 bis 2 / 1 bis 3 / 2 | nicht berechnet | - / - / 477 | 3,79 (Saat 3) | 1,91 | 0,011 |

- "-" = Spanne nicht definiert (an einem Punkt keine zwei positiven masselosen Moden). Spannen und Tempi der
  instabilen Netze sind nur beschreibend; bei f = 0,2 mischen weiche lokale Moden mit den TT-Zweigen (Einzelwerte
  omega^2/k^2 von 0,56 bis 20), daher die Spannen von 66 bis 3 456 %.
- **Probe f = 0:** N = 128, Saaten 1 bis 4, selbst gerechnet: alle 26 Werte je Netz bitgleich mit TT-GLAS-1
  (Abweichung 0). N = 256: Richtung [100] fuer Saaten 1 bis 3 selbst gerechnet, ebenfalls Abweichung 0.
- **Polarisationsaufspaltung / Richtungsspanne der Zweigmittel (Mittel):** N = 128: 12,8 / 5,3 % (f = 0), 15,6 /
  5,4 % (f = 0,05); N = 256: 10,6 / 4,0 % (f = 0), 14,6 / 7,2 % (f = 0,05).
- **Aenderung je Netz gegenueber f = 0 (beschreibend, Nachtrag):** f = 0,05: Spanne +41,1 / +41,0 / -2,5 / -4,3 %
  (N = 128) und +29,4 % (N = 256), Median |r| 29,4 %; omega^2/k^2 -16,5 / -16,8 / -18,1 / -14,9 % und -17,6 %, Tempo
  -7,8 bis -9,5 %. Zufallsniveau (TT-GLAS-1, Median |s_j / s_i - 1| ueber Paare verschiedener Netze): 24,0 % bei
  N = 128 (62 % der Paare ueber 20 %), 15,6 % bei N = 256 (37 %).
- **Die Luecke schrumpft:** Die naechste Mode ueber den zwei TT-Zweigen liegt bei f = 0 bei omega^2 >= 3,4, bei
  f = 0,05 bei 0,05 bis 0,39 (kleinster Wert je N: 0,050 bzw. 0,164) und bei f = 0,2 bei 0,011 bis 0,012 (kleinste
  Werte je N). Die Zuege bringen also auch weiche Moden in die Naehe der Schallwellen [E].
- **Je Zug:** Das Verhaeltnis negativer Richtungen der reduzierten Regge-Matrix zur Zugzahl liegt bei 0,165 bis 0,221
  (14/85 bis 75/340) [Kopfrechnung]; das ist ein Verhaeltnis von Zaehlungen an 16 Punkten, keine Zuordnung je Zug. Die
  Zahl waechst etwa proportional zur Zugzahl (nachtrag-69/bild-nachtrag.png, rechts; abgelesen, ohne Ausgleichsgerade).

### 4.3 Kontrolle UK0 je Netz [E]

| N | Saat | Zuege bei f = 0,05 / 0,2 | erlaubte Flaechen zu Beginn / am Ende | max \|Delta S\| | max \|Delta S\| / (2 pi sum l) | groesster Fehlwinkel | affine TT-Steifigkeit vorher -> nach f = 0,2 (min bis max) |
|---|---|---|---|---|---|---|---|
| 128 | 1 | 86 / 345 | 36,1 % / 4,4 % | 4,8e-13 | 4,0e-17 | 1,0e-13 | 0,999996-0,999999 -> 1,000035-1,000135 |
| 128 | 2 | 87 / 347 | 34,7 % / 4,4 % | 2,3e-13 | 2,1e-17 | 2,7e-13 | 0,999996-1,000002 -> 1,000043-1,000137 |
| 128 | 3 | 87 / 349 | 34,7 % / 4,3 % | 1,6e-13 | 1,3e-17 | 1,0e-13 | 0,999996-1,000000 -> 1,000033-1,000248 |
| 128 | 4 | 85 / 340 | 36,6 % / 4,4 % | 9,5e-14 | 1,1e-17 | 1,2e-13 | 0,999996-0,999998 -> 1,000031-1,000119 |
| 256 | 1 | 174 / 696 | 34,1 % / 3,6 % | 1,4e-12 | 5,6e-17 | 2,5e-13 | 0,999996-0,999998 -> 1,000037-1,000095 |
| 256 | 2 | 173 / 692 | 33,1 % / 4,2 % | 1,4e-12 | 6,0e-17 | 5,4e-13 | 0,999996-1,000008 -> 1,000044-1,000091 |
| 256 | 3 | 170 / 681 | 36,8 % / 4,0 % | 1,4e-13 | 7,7e-18 | 2,3e-13 | 0,999996-0,999999 -> 1,000043-1,000649 |
| 256 | 4 | 173 / 694 | 34,7 % / 4,4 % | 3,6e-12 | 1,5e-16 | 3,3e-13 | 0,999996-0,999999 -> 1,000042-1,000190 |

- Die Zielzahl round(f F0) wurde in allen Kontrollnetzen erreicht. Die Volumensumme bleibt der Kasten (Abweichung
  <= 4,4e-16), die Regge-Wirkung vor den Zuegen ist schon null (|S0| <= 5,7e-13). Die Volumenschwelle schloss zu Beginn
  hoechstens 0,24 Prozentpunkte aller Flaechen aus (konvex, aber unter der Volumenschwelle), die Kantenbedingung keine.
- Die affine TT-Steifigkeit (Regge allein, glatte Welle, |k| = 1e-2) bleibt nach den Zuegen 1 auf <= 6,5e-4 und
  richtungsfrei auf <= 6,1e-4. Die kleine Verschiebung nach oben passt zu Dispersion bei endlichem k ueber die laengeren
  neuen Kanten (k^2 l^2 ~ 1e-4) [H, nicht getrennt geprueft].

### 4.4 Nachtrag V (nach dem Einfrieren, auf Hinweis der Leitung 06:20; beschreibend, kein Urteil) [E]

- Code code/nachtrag_v.py (neu, sha256 a5dff790...; uk.py, tg.py, tg_auswertung.py unveraendert importiert), Lauf
  uk-nt-v auf cpu4 (gerechnet 04:39:12 UTC, 0,3 s, rc = 0), Ergebnis nachtrag-69/nachtrag-v.json.
- **Ist V Delaunay?** Nein. Von 116 Flaechen je Zelle verletzen genau 12 die Delaunay-Bedingung, alle gleich stark
  (mu = -0,3902 = -16/41 [Kopfrechnung fuer den Bruch]). Keine Flaeche ist kugel-entartet (|mu| <= 1e-9: 0). Die
  Handrechnung der Leitung (HODGE-L) trifft also zu, und der Kartensatz "auf regelmaessigen Netzen mit Kugel-Entartung
  gilt M-B nicht" passt fuer V nicht: V hat keine Entartung, M-B wuerde dort umklappen.
- **Delaunay-gesteuerte Zuege:** An allen 12 Flaechen ist der 2-3-Zug erlaubt (staerkste Verletzung zuerst, Regeln wie
  PLAN 2). Danach: 70 Tetraeder, 80 Kanten, 140 Flaechen je Zelle, keine Verletzung mehr, kleinster Randabstand
  mu = 0,220. **V ist nach den 12 Zuegen je Zelle Delaunay.** Regge-Wirkung vorher 9,1e-16, nachher -5,3e-15.
  Diederwinkel nachher 19,5 bis 146,4 Grad (vorher 35,3 bis 90).
- **TT-Wellen (gleicher Code wie die Kontrolle TG-G0):**

  | Netz | regulaer | masselos je Punkt | wachsend | A_red pos. def. | B_red negativ | TT-Anteil min | Spanne | omega^2/k^2 Mittel | Polarisations-Aufspaltung max | Richtungsspanne der Zweigmittel |
  |---|---|---|---|---|---|---|---|---|---|---|
  | V | ja | 2 | 0 | ja | 0 | 1,000000 | 6,339 % | 0,1218 | 6,34 % | 1,03 % |
  | V nach 12 Zuegen je Zelle | ja | 2 | 0 | ja | 0 | 1,000000 | 15,43 % | 0,0907 | 15,43 % | 2,45 % |

  - Die Werte von V stimmen mit TT-GLAS-1 (6,3389 % [P]) ueberein.
  - Die Wuerfelsymmetrie bleibt: Innerhalb jeder Klasse ([100], [110], [111]) sind die Zweige gleich auf <= 3,3e-9,
    [111] bleibt entartet. Die 12 Zuege je Zelle erhalten also die Symmetrie, soweit die TT-Spektren das zeigen.
  - Lesart [H]: Delaunay-gesteuertes Umklappen laesst V stabil und mit genau zwei TT-Moden, macht die Richtungsspanne
    aber 2,4-mal so gross und das Tempo^2 um 25,5 % kleiner [Kopfrechnung]. Fuer die Isotropie von Finns Kristall
    waere M-B also unguenstig.

## 5. Welcher Mechanismus waere fuer Finns Takt logisch? [H]

- **Was die Rechnung beitraegt:**
  - Energie: Ein flacher 2-3-Zug kostet keine Regge-Energie (UK0 [E]). Nach PLAN 1 [M] gilt das auch gekruemmt, wenn
    die neue Kante die Laenge aus der flachen Doppelpyramide bekommt (nicht gerechnet); das Volumen bleibt ohnehin.
    PONZANO-1 zeigte die Quantenform: Biedenharn-Elliott exakt, das Profil der 2-3-Summe hat sein Maximum an einer
    flachen Einbettung [P].
  - Geometrie: Folgen die Verbindungen den Ecken (Delaunay), klappt im Mittel ueber Netze ein Anteil etwa proportional
    zur Amplitude um, phi_T ~ 7,5 a, ohne Schwelle im Mittel (je Netz mit Schwelle, 4.1); eine lange TT-Welle (affine
    Dehnung) verletzt etwa 1,2 a der Flaechen [E].
  - Wellen: Zufaellige 2-3-Zuege (nur Verfeinerung, Volumenschwelle 1e-3) machten Finns Hamilton-Netz instabil, schon
    bei f = 0,05: auf etwa fuenf Zuege kam eine negative Richtung der reduzierten Regge-Matrix, also eine wachsende
    Mode an allen 16 gerechneten k (4.2) [E]. Die Delaunay-Netze waren bei kleinem k stabil (f = 0 hier und 48 von 48
    in TT-GLAS-1 [P]); V nach seinen 12 Delaunay-Zuegen je Zelle auch (4.4, Nachtrag) [E]. Delaunay ist dafuer aber
    nicht noetig: V selbst ist nicht Delaunay und trotzdem regulaer (4.4).
- **Lesart je Mechanismus [H]:**
  - **M-A energetisch:** Die Regge-Energie sieht Umklappungen nicht. Ohne Zusatzterm waeren die Zuege frei, also nur
    entropisch; zufaellige 2-3-Zuege machten das Netz hier instabil (ob gemischte 2-3/3-2-Folgen oder eine strengere
    Formschwelle das aendern, ist offen). Ein energetischer Mechanismus braeuchte einen eigenen Term, der schlechte
    Zerlegungen bestraft; Delaunay ist das Minimum eines solchen geometrischen Guetemasses (Rajan 1994 [L]). Die
    Bewegungsenergie (J je Tetraeder) kann im ruhenden Netz nichts auswaehlen.
  - **M-B Delaunay:** Haelt das Netz in einer Klasse, die bei kleinem k stabil war, und bindet die Zuege an die Ecken.
    Sie sind dann keine eigenen Freiheitsgrade, also keine frei laufenden "Phasonen" (DANZER-L: dort hiesse das
    gepinnt, Isotropie traegt) [H]. Preis: Im Mittel loest jede Amplitude Zuege aus, etwa proportional zu ihr. Im
    flachen Netz sind Eckverschiebungen Eichung (Matrix M in tg.py [P]); die Verbindungen haengen dann an den
    Ecklagen, nicht an der Kruemmung. Das ist sinnvoll, wenn die Ecken echte Orte sind (Uhren, Teilchen). Fuer V macht
    M-B die Richtungsspanne groesser (4.4).
  - **M-C taktgesteuert:** Jedes angeklebte 4-Simplex ist auf der Raumschicht genau ein Pachner-Zug
    (TICK-SCHNITT-SCHREIBTISCH [P]). PACHNER-TAKT-1 fand: Diagonalwechsel ergeben nur mit Zeltstangen gesteuert einen
    Takt, vorwaerts genau dann, wenn die neue Diagonale hoeher liegt [P]. Dann ist Umklappen der Zeitschritt selbst.
    Neu ist hier eine Bedingung an diesen Takt [H]: Er sollte so gesteuert sein, dass jede Raumschicht in einer stabilen
    Klasse bleibt; zufaellig gewaehlte 2-3-Zuege taten das hier nicht [E].
  - **M-D quantenmechanisch:** In 3D ist der 2-3-Zug in der Ponzano-Regge-Summe eine exakte Identitaet (PONZANO-1
    [P]). Eine Raumschicht allein "sieht" das Umklappen dort nicht; sichtbar wird es erst als 4D-Schritt. In
    4D-Spinschaeumen gilt die Invarianz nicht; CDT nutzt die Zuege als Monte-Carlo-Schritte, nicht als Zeit [L].
- **Vorschlag [H]:** M-C als Mechanismus (Umklappen = Takt), M-B als Auswahlregel: Dran ist die Flaeche, deren
  Delaunay-Bedingung kippt. Das ist lokal und im Mittel ohne Schwelle. Gerechnet sind nur statische Delaunay-Netze und
  V mit 12 Zuegen je Zelle, kein Delaunay-gesteuerter Takt. M-A traegt im Vakuum nicht; M-D ordnet ein. Pruefbar ist
  das mit einem Takt, der nur Delaunay-erhaltende Zuege macht: Bleiben die Schichten stabil, und ueberleben die zwei
  TT-Moden? Gegenprobe: gemischte 2-3/3-2-Zufallsfolgen bei fester Tetraederzahl und mit strengerer Formschwelle.

## 6. Selbstanzeigen

1. **Projektsuche im Plan behauptet, aber erst nach dem Einfrieren ausgefuehrt.** PLAN 1 nennt eine grep-Suche ueber
   RUNDE-37. Ausgefuehrt habe ich sie erst um 06:21:31 CEST (Einfrieren 06:19:02), mit den vorgeschriebenen
   Ausschluessen. Ergebnis: keine Datei mit zufaelligen Pachner-Zuegen auf Zufallsnetzen und TT-Auswertung; Treffer
   waren PACHNER-TAKT-1, PONZANO-1 (Biedenharn-Elliott), RUNDE-42/TICK-SCHNITT-SCHREIBTISCH und RAUMZEIT-NETZ. Der
   Plansatz war inhaltlich richtig, aber beim Schreiben nicht belegt.
2. **Rauchtest r4 verriet eine Struktur:** Die Schluessel der r4-Auswertung zeigten, dass bei Rauchsaat 901 (N = 128)
   kein UK3-Paar entstand, also mindestens ein Rauchnetz nicht regulaer war. Das war nach dem Plantext der Abschnitte 1
   bis 6 und vor den Hauptlaeufen; im Plan vermerkt (Abschnitt 8), Regeln unveraendert.
3. **Ueberschreiben an Ort und Stelle:** code/kette-cpu3.sh und kette-cpu4.sh habe ich auf der .69 ein zweites Mal per
   scp ueberschrieben (gleicher Inhalt, kein Lauf aktiv, kurz nach 06:19 CEST). Alle anderen Dateien kamen neu dazu.
4. **Zwischenauswertung:** uk-aw1 (eingefrorenes Skript, 04:25:52 bis 04:25:53 UTC) lief auf Teildaten. Danach habe ich
   UK0 und UK1 sowie die TT-Rohwerte bei N = 128 gelesen, bevor alle TT-Laeufe fertig waren. Keine Regel geaendert.
5. **Nachtraege nach dem Einfrieren** (beschreibend, eigene Dateien): code/nachtrag_v.py (Hinweis der Leitung 06:20,
   4.4), code/nachtrag_tabelle.py (Mittel ueber alle vollstaendigen Netze, auch nicht regulaere; uk_auswertung
   mittelt Spanne und Tempo nur ueber regulaere) und code/nachtrag_bild.py (lesbares Bild, nachdem das eingefrorene Bild
   rechts unlesbar war). Alle drei habe ich nach Sicht der ersten instabilen Netze angelegt.
6. **Nur 2-3-Zuege (Karte):** Bei f = 0,2 waechst die Zahl der Tetraeder um 40 % und die der Kanten um 35 %
   [Kopfrechnung aus lauf-69/auswertung.json, tabelle_tt T und E]. Umklappen und Verfeinern sind dadurch vermengt.
   Gemischte 2-3/3-2-Folgen mit fester Tetraederzahl habe ich nicht gerechnet.
7. **Stabilitaet nur bei kleinem k** (16 Punkte je Netz). Die gefundenen Instabilitaeten haengen kaum von k ab (bei
   f = 0,05 gleiche Zahl wachsender Moden an allen Punkten eines Netzes, bei f = 0,2 je Punkt um bis zu 3
   verschieden); das spricht fuer lokale Moden [H].
8. **TT-Anteil bei f = 0,2 nicht berechnet:** Ist A_red nicht positiv definit, liefert tg.punkt keine Eigenvektoren,
   also keinen TT-Anteil. Bei f = 0,05 ist er berechnet (>= 0,999999).
9. **jq auf der .69 mit Rundung:** Zum Lesen habe ich in jq auf der .69 Werte gerundet (round) und ausgewaehlt; lokal
   kein jq, python, awk oder perl. Zahlen dieses Berichts stammen aus auswertung.json, den Nachtrag-Dateien oder
   einzeln gelesenen Rohwerten; markierte Kopfrechnungen sind von Hand.
10. **Laeufe zwischen die Ketten geschoben:** uk-aw1, uk-nt-v und uk-nt-tab0 warteten am Lock von cpu3 bzw. cpu4 und
    liefen zwischen zwei Kettenlaeufen (je wenige Sekunden); die Startzeile im Log ist der Beginn des Wartens, nicht
    der Start. Dadurch warteten auch die Kettenlaeufe danach kurz (z. B. uk-tt128-f005: Log-Start 04:39:11, am Lock ab
    04:39:12; uk-tt128-f02a ~1 s). In der Tabelle von Abschnitt 1 steht der Beginn am Lock; Laufzeiten sind die der
    Rechnung (laufzeit_s), bei den kurzen Laeufen Wanduhr.
11. **Volumenschwelle 1e-3 [F]:** Sie schloss zu Beginn hoechstens 0,24 Prozentpunkte der konvexen Flaechen aus. Ob eine
    strengere Formschwelle die Instabilitaet verhindert, ist nicht geprueft.
12. **Vorab-Aussagen nicht gerechnet:** Die Invarianz der Regge-Wirkung unter 2-3-Zuegen im gekruemmten Netz (PLAN 1)
    ist nur Schreibtisch [M].
13. **Gegenlesen:** Ein frischer Leser (pruefer-opus, nur lesend; 07:06:09 bis 07:13:23 CEST nach seiner Messung)
    pruefte rund 450 Zahlen und fand die Urteilszuordnung korrekt. Er meldete 4 A-Befunde (zu starke Woerter "ohne
    Schwelle", "jede", "genau"; Spanne der wachsenden Moden je Punkt und Selbstanzeige 7; falsche Lueckenspanne bei
    f = 0,05; Verallgemeinerung ueber die gerechneten 2-3-Zuege hinaus), 5 B- und 7 C-Befunde. Ich habe alle
    uebernommen; kein Urteil hat sich geaendert. Die letzte Fassung hat kein Leser mehr gesehen.

## 7. Einfach gesagt

Wir haben in Finns Zufallsnetz ausprobiert, was beim Umklappen passiert (zwei Tetraeder werden zu drei, die Ecken
bleiben stehen); Schwerkraft-Energie kostet das nicht. Laesst man die Ecken etwas wackeln und haelt das Netz dabei
"ordentlich" (Delaunay), klappt im Mittel ein Anteil um, der etwa im gleichen Mass wie die Wackelstaerke waechst:
Wackeln um ein Tausendstel der Kantenlaenge klappt etwa 7 bis 8 von 1000 Tetraedern um. Klappt man dagegen an 5 % der
Flaechen zufaellig um, wird das Netz instabil, kleine Stoerungen wachsen dann von selbst an. Wir vermuten deshalb, dass
Umklappen in Finns Netz einer Regel folgen muss, am ehesten als Teil des Takts, der die Zellen ordentlich haelt; ob
nur das Verfeinern (aus zwei mach drei) oder schlechte Zellformen schuld sind, ist noch offen. Das alles sind
Rechnungen an kleinen Modellnetzen, keine Messungen.

## 8. Dateien

- PLAN.md, PLAN.md.eingefroren-20261005-061902, EINGEFROREN-SHA256.txt (lokal), auf der .69 EINGEFROREN-SHA256-69.txt.
- code/: uk.py (Zuege, Kontrolle, M-B, TT-Laeufe), uk_auswertung.py (Urteile), uk_bild.py (Bild), kette-cpu3.sh,
  kette-cpu4.sh, je mit .eingefroren-20261005-061902; tg.py, tg_auswertung.py, ew.py, tp.py unveraendert aus
  TT-GLAS-1. Nachtrag nach dem Einfrieren: nachtrag_v.py (sha256 a5dff790...), nachtrag_tabelle.py (65cbda57...),
  nachtrag_bild.py (a79a812f...).
- lauf-69/: kontrolle-N128.json, kontrolle-N256.json, mb-N128.json, mb-N256-a.json, mb-N256-b.json, tt-*.json,
  auswertung.json (End-Auswertung), auswertung-zwischen.json (Zwischenstand, Selbstanzeige 4), bild-umklapp.png, Logs,
  PRUEFSUMMEN.txt (48 Dateien).
- nachtrag-69/: nachtrag-v.json, tabelle.json, tabelle-zwischen.json (Absturzprobe), bild-nachtrag.png, Logs,
  PRUEFSUMMEN.txt.
- rauch-69/: r1 bis r3 (--rauch) und r4 (Rauchsaaten 901, 902; Absturzprobe von Auswertung und Bild).
- kette-cpu3.out, kette-cpu4.out: Ausgaben der Laufketten (lokal mitgeschrieben).
- Auf der .69: /home/fmh/fmhc-physics-remote/umklapp-1/ (code/, rauch/, lauf/, nachtrag/).

Abschluss der Datei 2026-10-05 07:18:13 CEST (date). Zeitbox 120 min ab 05:54:29 CEST (bis 07:54:29) eingehalten; kein Lauf mehr aktiv (letzter Lauf 05:02:46 UTC). Journal, Peerbus und Commit uebernimmt die Leitung.
