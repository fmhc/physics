# ISO-ATEM-1: Plan des Code-Agenten (Runde 42)

- Code-Agent fuer die Leitung claude-primary. Start 2026-10-04 18:54:13 CEST (date), Zeitbox 75 min.
  Plan geschrieben ab 19:06:30 CEST (date), vor jeder Rechnung.
- Gelesen: KARTE.md (ganz); dreieck-pumpe-l/DOSSIER.md (ganz, Abschnitt 6 bindend); kopplung-tetra-1 (KARTE,
  ERGEBNIS, Geometrie in code/tp.py und code/kt.py); Laufform aus paar-regge-1 (PLAN, Logs).
- Ordner: lokal RUNDE-37/iso-atem-1/; .69: /home/fmh/fmhc-physics-remote/iso-atem-1/ (code/, quellen/, rauch/, lauf/).
- Kennzeichen: [E] gerechnet (.69), [M] eigene Mathematik von Hand (nicht gegengelesen), [S] an der Quelle gelesen,
  [L] Gedaechtnis, [L?] unsicher, [P] Projektdatei, [H] Hypothese, [F] Festlegung dieses Plans (nicht aus der Karte),
  [D] Diagnose, beschreibend, ohne Urteil.
- Vorhersagen und Wahrscheinlichkeiten der Karte (IA1 95 %, IA2 60 %, IA3 50 %) bleiben unveraendert.

## 1. Schritt 0: Literatur (2 von 2 Abrufen, beide per curl auf der .69, Kopien in quellen/)

| Abruf | Zeit (UTC, date) | Inhalt | Befund |
|---|---|---|---|
| A1 | 2026-10-04T17:03:30Z | arXiv-API: abs:cristobalite AND (P2_13 OR rigid OR tetrahedra), 2 Treffer | Saito/Ono 2010 (GeO2/SiO2 unter Druck), CS2 unter Druck; nichts zu P2_13 |
| A2 | 2026-10-04T17:04:06Z | arXiv-API: abs:cristobalite, alle 29 Treffer | Coh/Vanderbilt 2008 (arXiv:0806.3737, PRB 78, 054117): Abstract nennt P4_12_12, I-42d und Mannigfaltigkeiten mit P2_12_12_1, **nicht P2_13** [S Abstract]. Borcea/Streinu 2011 (arXiv:1110.4661): "deformation space ... for frameworks modelled on quartz, cristobalite and tridymite" [S Abstract]; Volltext nicht gelesen (kein Abruf mehr) |

- **Urteil Schritt 0:** In den zwei Abrufen steht nirgends "P2_13 = stetige Schar starrer Tetraeder mit schrumpfender
  kubischer Zelle". Literatur: **nicht belegt** (nur Abstracts). [L?] O'Keeffe/Hyde 1976 (Acta Cryst. B32, 2923) und
  das P2_13-Modell nach Barth 1932 bleiben Gedaechtnis.
- **Aber Schreibtisch [M] (Abschnitt 2):** Die P2_13-Schar laesst sich von Hand in geschlossener Form herleiten. Damit
  sind IA2 und IA3 (Kartenwortlaut) **vorab ableitbar [M]**, IA1 ebenfalls. Gemessen werden nur die Zahlen und Teil C.

## 2. Schreibtisch vor der Rechnung [M] (nicht gegengelesen; die Rechnung prueft ihn als Kontrolle K_M)

**Geometrie [F]:** Kante 1 PU, Umkugelradius s = sqrt(3/8) = 0,61237. Ideale Zelle a0 = 2 sqrt 2 = 2,82843 PU
(Mitten = Diamantgitter, Ecken = Pyrochlor). A-Mitten (oben) auf F-Plaetzen, B-Mitten bei A + a0 (1/4, 1/4, 1/4).
A-Ecken bei c + s d_k, B-Ecken bei c - s d_k, d_k aus (1,1,1), (1,-1,-1), (-1,1,-1), (-1,-1,1) durch sqrt 3.

**IA1, Gamma-Ansatz:** Alle A gleich gedreht (R_A), alle B gleich (R_B). Die Eckbedingungen ergeben F = (R_A + R_B)/2
(wie SP8 im Dossier). Mit erzwungenem F = lambda I bleibt je Ecke der Fehlpass (R_A + R_B - 2 lambda I) t_k - delta.
Mit Summe t_k t_k^T = (4 s^2/3) I und der Polarzerlegung von R_A + R_B gilt min ||R_A + R_B - 2 lambda I||_F^2 =
4 (1 - lambda)^2. Also min r_rms = (2 s / sqrt 3)(1 - lambda) = (1 - lambda)/sqrt 2, bei lambda = 0,97: 0,02121 > 1e-3.
Teil A ist exakt: R_A = R_z(phi), R_B = R_z(-phi), F = diag(cos phi, cos phi, 1), Mitten c = F c0.

**IA2/IA3, P2_13-Schar:** Raumgruppe P2_13 (Tabelle der International Tables, 12 Operationen). A1 auf (x,x,x) mit
Abstand u_A vom Ursprung, gedreht um n = (1,1,1)/sqrt 3 um phi_A; B1 auf derselben Achse bei u_B, gedreht um phi_B.
Die Ecke O1 liegt auf der Achse (u_B - u_A = 2 s), die Ecke O2 von A1 trifft die Ecke von B2 = (2_1-Schraube)(B1).
Aus den drei O2-Komponenten folgt von Hand:
- cos(phi_A + 60 Grad) + cos(phi_B - 60 Grad) = 1
- lambda = a/a0 = (1 + cos phi_A + cos phi_B)/3
- Tangente bei 0: phi_B = phi_A (+ phi_A^2/sqrt 3), lambda = 1 - phi^2/3 + ...
- Mit phi_A = phi - delta, phi_B = phi + delta: 2 cos phi cos(60 Grad - delta) = 1 und
  lambda = (1 + 2 cos phi cos delta)/3. Bei lambda = 0,97: delta = 1,56 Grad, phi = 17,2 Grad, also phi_A ~ 15,7 Grad,
  phi_B ~ 18,8 Grad.
- Folge: Es gibt eine glatte Schar (Jacobi-Matrix des Ansatzes am Start Rang 4 bei 5 Unbekannten), die von phi = 0
  ausgeht und die kubische Zelle isotrop schrumpfen laesst. Ob die Tetraeder dabei ineinander laufen, ist von Hand
  nicht geprueft.
- **Meine Erwartung (vor der Rechnung):** Teil B bestaetigt die Formeln auf 1e-12; IA2 und IA3 (Kartenwortlaut)
  treffen ein. Offen sind Beruehrwinkel und Teil C.

## 3. Modell und Restgroesse [F, Dossier woertlich: starre regulaere Tetraeder, Kante 1, Kugelgelenke, 8 Tetraeder]

- 8 starre Tetraeder je Zelle: Mitte c_j, Drehung R_j (gegen die Ideallage). Zelle F a0 (Gittervektoren F a0 e_i).
- 16 geteilte Ecken (Topologie aus der Ideallage, Gitterversatz n_p): Delta_p = c_j + R_j t_k - c_j' - R_j' t_k' -
  F a0 n_p.
- **Rest:** r_max = max_p |Delta_p| (PU), r_rms = sqrt(mittel_p |Delta_p|^2). Schwellen "Rest < x" werden mit r_max
  geprueft, "Rest > x" mit r_rms (r_max >= r_rms, beides also vorsichtig).

## 4. Teile und Laeufe

**Lauf "kontrolle" (Teil A und Gamma-Ansatz):**
- K0: Ideallage invariant unter allen 12 P2_13-Operationen; r_max(ideal) <= 1e-12.
- Teil A: phi in {1, 5, 10, 20, 30} Grad, r_max <= 1e-12 gefordert; Volumen cos^2 phi.
- Gamma-Ansatz mit F = lambda I: Unbekannte w_A, w_B (Drehvektoren), delta (Versatz der B), Levenberg-Marquardt (LM)
  aus 200 Starts je lambda (Haar-Zufallsdrehungen, Saat 21), lambda in {0,99; 0,97; 0,95; 0,90}. Ausgabe min r_rms,
  min r_max und die Formel (1 - lambda)/sqrt 2.

**Lauf "ast" (Teil B):**
- Unbekannte (phi_A, phi_B, u_A, u_B, lambda); Struktur aus den 12 P2_13-Operationen; Gleichungen = alle 48
  Komponenten von Delta (nicht nur die 4 reduzierten).
- Pseudo-Bogenlaenge ab der Ideallage, Schritt h = 0,002 (Norm in rad, PU, lambda), Tangente aus dem Nullraum der
  48 x 5-Jacobi-Matrix, Korrektor Gauss-Newton bis r_max < 1e-13 (hoechstens 30 Schritte), beide Richtungen, je bis
  lambda < 0,6 oder 2500 Schritte.
- Exakte Loesungen bei lambda in {0,99; 0,97; 0,95; 0,90} (lambda fest, 4 Unbekannte, Start am naechsten Astpunkt),
  beide Richtungen.
- Je Astpunkt: r_max, lambda, V/V0 = lambda^3, phi_A, phi_B, Kippwinkel phi_m = (phi_A + phi_B)/2 [F], Winkel an der
  geteilten Ecke (Mitte-Ecke-Mitte, "Si-O-Si") fuer O1 (4 Ecken) und O2 (12 Ecken), Beruehrung (unten),
  kleinster Abstand nichtgebundener Ecken d_OO.
- **Beruehrung [F]:** Paare (j, j', Bildzelle) mit Mittenabstand < 2 s. Ohne gemeinsame Ecke: Trennachsentest (4 + 4
  Flaechennormalen, 36 Kantenkreuzprodukte), Abstand entlang der besten Achse g. Mit gemeinsamer Ecke: Kegeltest am
  Gelenk (Trennebene durch die Ecke; Kandidaten aus Kantenpaaren der beiden Kegel), g. Beruehrwinkel = erster Astpunkt
  mit g <= 0 bei einem Paar (ohne die gemeinsame Ecke selbst).
- K_M: Abweichung der Astpunkte von den Formeln in Abschnitt 2 (max ueber den Ast).

**Lauf "zufall" (Teil C, Dossier woertlich: Zielwerte lambda in {0,99; 0,97; 0,95; 0,90}, viele Zufallsstarts):**
- Alle 8 Tetraeder frei (45 Unbekannte; Mitte von A1 als Eichung fest), F = lambda I fest, 48 Gleichungen, eigenes LM
  mit analytischer Jacobi-Matrix, hoechstens 400 Iterationen, Abbruch bei r_max < 1e-13.
- Starts je lambda [F]: 300 "nah" (Drehvektor gleichverteilt in der Kugel |w| <= 0,5 rad, Mitten lambda c0 + N(0;
  0,05^2)) und 300 "weit" (Haar-Zufallsdrehung, Mitten lambda c0 + N(0; 0,2^2)). Saaten 31 (nah) und 32 (weit) plus
  Index von lambda. Diese Zahlen duerfen nach dem Rauchlauf nur wegen Laufzeit (<= 10 min je Lauf) sinken, vor dem
  Einfrieren, mit Nachtrag.
- Klassen: "Loesung" r_max < 1e-10; "fast" 1e-10 <= r_max < 1e-6; "keine" sonst.
- Je Loesung: P2_13-Test, Platztest, Zahl der Drehteile aus O (24) mit passender Verschiebung, Nullitaet der
  48 x 45-Jacobi-Matrix (Schwelle 1e-8 relativ zum groessten Singulaerwert), Ueberlappung (wie Beruehrung).

**P2_13-Test [F]:** Fuer jede der 12 Drehungen Q aus T und jedes Bild j' der Mitte 1: tau = c_j' - Q c_1. Die
Abbildung x -> Q x + tau muss alle 8 Mitten und alle 16 Ecken (modulo Gitter) auf Mitten bzw. Ecken bringen,
Abweichung <= 1e-7 PU. P2_13 = alle 12 Q haben ein passendes tau, und fuer die drei Zweier ist die Verschiebung
laengs der Achse 1/2 (Schraube, Toleranz 1e-6). **Platztest:** Jedes Tetraeder liegt auf einer Dreierachse (eine
Dreier-Operation fixiert seine Mitte modulo Gitter); die 4 A haben paarweise verschiedene Achsen, ebenso die 4 B.

**Lauf "auswertung":** Urteile nach Abschnitt 5 aus den drei JSON-Dateien, mechanisch. **Lauf "bild":** V/V0 gegen
Kippwinkel (Teil B, mit Teil A cos^2 phi zum Vergleich), Si-O-Si-Winkel, Beruehrwinkel markiert.

## 5. Urteile

| Nr | nach Plan [F] | nach Kartenwortlaut [F] |
|---|---|---|
| IA1 | eingetroffen, wenn Teil A bei allen 5 phi r_max <= 1e-12 und Gamma-Ansatz bei lambda = 0,97 min r_rms > 1e-3 (200 Starts); sonst nicht eingetroffen | wie nach Plan, dazu "nie": min r_rms > 1e-6 bei allen vier lambda |
| IA2 | Dossier: "besteht mit Rest < 1e-10 auf einem zusammenhaengenden Ast" = Teil-B-Ast von phi = 0 bis lambda <= 0,97 mit r_max < 1e-10 an jedem Astpunkt (Schritt <= 0,002) und exakte Loesung bei 0,97 mit r_max < 1e-10: eingetroffen. "Scheitert, wenn kein Start fuer ein lambda < 1 unter Rest 1e-6 kommt" (B und C): nicht eingetroffen. Sonst uneindeutig | eingetroffen, wenn bei lambda = 0,97 eine Loesung (B oder C) mit r_max < 1e-10 existiert; sonst nicht eingetroffen |
| IA3 | eingetroffen: IA2 nach Plan eingetroffen, die B-Loesung bei 0,97 besteht P2_13- und Platztest, und **alle** C-Loesungen bei 0,97 bestehen den P2_13-Test. Teilweise: B besteht, aber C findet bei 0,97 auch Loesungen ohne P2_13 (Anteil wird genannt). Nicht eingetroffen: B besteht nicht oder IA2 nicht eingetroffen | eingetroffen, wenn die Loesung aus IA2 (B bei 0,97; ohne B die beste C-Loesung) P2_13- und Platztest besteht; sonst nicht eingetroffen |

- IA1, IA2 und IA3 nach Kartenwortlaut sind **vorab ableitbar [M]** (Abschnitt 2). Ihre Urteile pruefen meinen
  Schreibtisch und den Code. Messung im engeren Sinn sind: Teil C (weitere isotrope Loesungen), Beruehrwinkel,
  Si-O-Si-Winkel, d_OO und die Nullitaeten.
- Beschreibend [D], ohne Urteil: Volumen gegen Kippwinkel, Beruehrwinkel, Si-O-Si, Spiegelast, Klassen in Teil C bei
  allen lambda.

## 6. Laeufe und Ablauf

- Nur .69 ueber /home/fmh/fmhc-physics-remote/kleintests/kleintest.sh, Spuren cpu8 und cpu9 (beim Start frei), 1 Thread,
  je Lauf <= 10 min (RuntimeMaxSec = 600 im Starter). Logs mit absolutem Pfad.
- Reihenfolge: (1) Rauchlauf mit kleinen Zahlen (rauch/; ich lese nur Laufzeit, Schluessel und die Kontrolle K0).
  (2) Einfrieren: PLAN.md und code/ als Kopien mit sha256 in EINGEFROREN-SHA256.txt. (3) Hauptlaeufe kontrolle, ast,
  zufall. (4) auswertung, bild.
- Keine Aenderung von Schwellen, Startzahlen oder Code nach der Sicht auf Hauptergebnisse. Fehler danach nur als
  Selbstanzeige und, wenn noetig, als getrennt gekennzeichnete Diagnose.
- Lokal kein python, awk, perl; lokal nur jq, sed, grep, ssh/scp, sha256sum, date.

## 7. Nachtrag nach dem Rauchlauf (geschrieben ab 19:12:31 CEST, date; vor dem Einfrieren)

- Rauchlaeufe auf der .69 (UTC): kontrolle (n_gamma 5) 17:12:04 bis 17:12:07, cpu8; ast (30 Schritte je Richtung)
  17:12:04 bis 17:12:09, cpu9; zufall (lambda 0,97, 5 + 5 Starts) 17:12:21 bis 17:12:22, cpu8. Alle rc = 0.
- Gelesen habe ich: Laufzeiten, Schluessel, Punktzahlen, Iterationszahlen, K0 und die fuenf Teil-A-Reste (alle
  <= 7e-16; Kontrolle, vorab ableitbar). Nicht gelesen: Gamma-Werte, Astwerte, Klassen von Teil C.
- K0 bestanden: Ideallage r_max 3,9e-16; die P2_13-Tabelle bildet die Ideallage auf sich ab (alle 12 Drehteile,
  Schrauben ja, 24 von 24 Drehteilen aus O, Platztest "nein", weil jede Ideal-Mitte auf allen vier Dreierachsen liegt).
- Laufzeit: Ast etwa 70 ms je Schritt, Teil C etwa 0,1 s je Start. Daher [F]: Teil C laeuft in zwei Laeufen
  (lambda 0,99 und 0,97 auf cpu8; 0,95 und 0,90 auf cpu9), Startzahlen unveraendert (300 + 300 je lambda).
- Keine Aenderung an Code, Schwellen oder Urteilsregeln.
