# ROHR-DREHUNG-2: ERGEBNIS

- Rechen-Agent fuer die Leitung claude-primary, geschrieben ab 2026-10-09 17:16:19 CEST (date).
- Karte KARTE.md (sha256 06853026...), VORAB.md eingefroren 2026-10-09 16:50:05 CEST (sha256 b0a02889..., siehe
  EINGEFROREN-SHA256.txt). Synthetische Rechnung, keine Messdaten. Nichts hier ist eine Naturbestaetigung.
- Kennzeichen: [E] gerechnet, [M] vorab ableitbar, [L] Literatur aus dem Gedaechtnis, [H] Lesart, [H, nach Sicht] Lesart
  nach Sicht der Daten.

## Ergebnis zuerst

| Nr | Erwartung (Karte, Kurzform) | Ausgang | Kernzahl |
|---|---|---|---|
| G0 | Nach Reparatur alle Elemente der kleinen Gruppe von k0 lassen den fuehrenden Eigenraum auf < 1e-10 invariant | **eingetroffen** [E, nach Sicht] | max Rest 4,5e-15 (psi = 0: 48 Elemente Oh; psi = 2 pi/3: 24 Elemente O; je Eigenraum) |
| W1 | psi = 2 pi/3: Summe der Chiralitaeten der Weyl-Punkte jedes Niveaus = 0 | **nicht eingetroffen** [E, nach Sicht] | je Sektor genau ein Weyl-Punkt (Gamma): Summe +1 (Sektor +), -1 (Sektor -). Ueber beide Sektoren zusammen 0 |
| W2 | psi = 2 pi/3: am fuehrenden Niveau nur eine Chiralitaet, Partner auf tieferem Niveau | **nicht eingetroffen** [E, nach Sicht] | erster Teil ja (je Sektor nur chi = Helizitaet), zweiter Teil nein: das tiefere Niveau ist identisch null, kein Partner dort |
| P1 | psi = 0: lineare Aufspaltung am Vierfachpunkt in der Phase, abs(lambda) konstant bis O(q^2) | **eingetroffen** [E, nach Sicht] | Phasenverhaeltnis 2,0000 (Spanne 2,0000 bis 2,00005), Betragsverhaeltnis 4,0000; Betrag/Phase bei q = 1e-3: 4,5e-4 |
| V1 | V, psi = 0: kleinste geschlossene Schleifen (Dreiecke) geben -1 | **eingetroffen** [E, blind; M: Bauregel] | 232 von 232 gerichteten Dreiecksschleifen Phi = 2 pi (H = -1); kuerzere Schleifen gibt es nicht |
| V2 | V: am fuehrenden Niveau ein entarteter Punkt mit linearer Aufspaltung | **eingetroffen** [E, blind] | Sektor +, psi = 0: Zweifachpunkt bei Gamma, abs(lambda) = 9,7783 (Maximum), linear in 126 von 126 Richtungen (Verhaeltnis 2,0000), phasenartig, chi = +1. Lage Gamma: Isotropie zaehlt nicht |

Fassung 1 (RUNDE-37), im Wortlaut bewertet (Ernte der Laeufe vom 07.10. plus diese Laeufe):

| Nr | Ausgang | Begruendung |
|---|---|---|
| R1 | **eingetroffen** [E; M vorab] | V1: alle 232 gerichteten Dreiecke von V geben H = -1 |
| R2 | **nicht eingetroffen** [E; M vorab festgelegt, VORAB F1 2.3] | m1d: alle 8 Sessel-Sechsringe geben Phi = 2 pi, also H = -1 |
| R3 | **nicht eingetroffen** im Wortlaut ("bis auf Eichung eindeutig") [E] | m2d: Regel existiert und ist diskret (Stoerung 1e-3 bricht sie), aber mod 2 pi drei einheitliche Werte 0, 2 pi/3, 4 pi/3 (48 Tupel im pi/3-Raster = 3 x 16 Klassenverschiebungen um 2 pi). psi = 0 genuegt schon |
| R4 | **formal eingetroffen, Isotropie ohne Befundwert** [E; M] | Masselos (Entartung bei Gamma exakt), linear in 426 Richtungen, Tempo 0,144338, Streuung 3e-7. Die Isotropie ist bei Gamma durch die kubische Symmetrie erzwungen [M, IDEE-08] |
| R5 | **eingetroffen, aber vorab feststehend** [M, VORAB F1 2.5; E mit G0] | Alle 23 nichttrivialen Drehungen geben O^n = -1 auf jedem fuehrenden Eigenraum (Rest < 1e-15). Darstellung: zweidimensional zweiwertig (E1/2 bzw. E5/2), kein F3/2 |

## 1. Ernte Fassung 1 (lauf-69-alt/)

- m1d bis m4d, Logs, v4.log und rohr.py von der .69 geholt; sha256 auf der .69 erzeugt, lokal mit `sha256sum -c`
  geprueft: alle OK (lauf-69-alt/SHA256SUMS-ernte-20261009.txt, lokale Fassung SHA256SUMS-lokal.txt).
- m1d [E]: psi = 0: Laenge 6: 8 mal 2 pi; Laenge 8: 12 mal 2 pi; Laenge 10: 4/3 pi, 2 pi, 8/3 pi; Laenge 12: alle
  sechs Vielfachen von 2/3 pi. Die VORAB-F1-Erwartung "auch Phasen ausser +-1" (60 %) ist eingetreten. Mit psi =
  2 pi/3 werden **nicht** alle Schleifen +-1 (Laenge 12 unveraendert gemischt); die F1-Erwartung dazu (45 %) trat nicht ein.
- m3d [E]: max abs(lambda) = Wurzel 6 genau bei Gamma (ein Gitterpunkt, top_k = (0, 0, 0)).
- **Korrekturen an IDEE-08 (Pruefung, nicht Uebernahme):**
  - "Vierfach entartet" gilt im vollen T fuer einen festen Eigenwert (-Wurzel 6 vierfach, +Wurzel 6 vierfach).
    abs(lambda) = Wurzel 6 ist achtfach, weil der Diamant zweigeteilt ist (lambda -> -lambda) [E, M].
  - "Bei psi ungleich 0 spaltet es in 1 + 2": Das ist eine Fehllesung. Die "Entartung 1" in m3d kommt vom
    Nelder-Mead-Punkt, der 1e-8 neben Gamma liegt. Bei Gamma bleibt jeder Helizitaetssektor zweifach. Die beiden Sektoren
    trennen sich nur in der Phase: Sektor + bei lambda = Wurzel 6 e^{-i pi/3}, Sektor - bei Wurzel 6 e^{+i pi/3} [E].
  - Die M4-Ursache war keine falsche Darstellung, keine falsche Lage von k0 und keine Eichung (Abschnitt 2).
- Tempo [E]: 0,144338 = 1/(4 Wurzel 3) auf 6 Stellen; det c = +-0,0030070 = (1/(4 Wurzel 3))^3 [E, Zahlgleichheit; nicht
  hergeleitet].

## 2. M4 repariert (G0) und Charaktere

- **Ursache [E]:** m4() nahm `V[:, :deg]` nach Sortierung nach abs(lambda). Wegen lambda -> -lambda liegen +Wurzel 6 und
  -Wurzel 6 gleichauf; die Auswahl mischte zwei Eigenraeume. Alle Kommutatoren waren schon 1e-16. Derselbe Fehler sass
  in pauli_test(). Reparatur: Eigenraum = Kern von (T - l0) per SVD. Die Gruppe ist jetzt die volle Raumgruppe bei Gamma
  (48 Elemente inkl. Schraubungen und Inversion am Bindungsmittelpunkt). Erster Reparaturversuch reichte.
- **G0 [E]:**

| psi | kleine Gruppe | Eigenwert | dim (geom = alg) | max Rest | Zerlegung |
|---|---|---|---|---|---|
| 0 | 48 (Oh) | +Wurzel 6 | 4 | 2,3e-15 | E1/2g + E1/2u |
| 0 | 48 (Oh) | -Wurzel 6 | 4 | 9,4e-16 | E5/2g + E5/2u |
| 2 pi/3 | 24 (O), die 24 Spiegel-/Inversionselemente vertauschen nicht (Kommutator 1,73) | Wurzel 6 e^{-i pi/3} (Sektor +) | 2 | 6,7e-16 | E1/2 |
| 2 pi/3 | 24 | Wurzel 6 e^{-2i pi/3} (Sektor -) | 2 | 9,9e-16 | E5/2 |
| 2 pi/3 | 24 | Wurzel 6 e^{+2i pi/3} (Sektor +) | 2 | 4,5e-15 | E5/2 |
| 2 pi/3 | 24 | Wurzel 6 e^{+i pi/3} (Sektor -) | 2 | 6,5e-16 | E1/2 |

- Lesart [M, VORAB 1]: E1/2 <-> E5/2 wechselt zwischen lambda und -lambda, weil die Schraubungen die Untergitter
  tauschen. Netzunabhaengig ist nur: **zweidimensionale zweiwertige Darstellung (Dublett), kein Quartett F3/2**.
- Projektivitaet [E]: Fuer jede eigentliche Drehung h der Ordnung n gilt Q^+ O^n Q = -1 (Rest < 1e-15). Bei den
  S6-Elementen und der Inversion ist O^n die Inversion; deren Spur auf den psi = 0-Raeumen ist 0 (g plus u).
- Pauli-Test repariert [E]: Antikommutatoren der effektiven Matrizen < 4,2e-11, gleiche Quadrate (psi = 0: -0,125 je
  Richtung), det c = +0,0030070 (Sektor +) bzw. -0,0030070 (Sektor -), bei psi = 0 und 2 pi/3.
- **Wortlaut der Regel "Spin 1/2 nur bei G0 und projektiver Darstellung":** Beides ist belegt. In diesem synthetischen
  Modell tragen die fuehrenden Moden bei Gamma ein zweiwertiges Dublett der Doppelgruppe O' (spin-1/2-artig). Dass die
  Darstellung projektiv ist, folgt schon aus dem Aufbau [M, F1 2.5]; neu ist nur "Dublett statt Quartett".

## 3. P1: Phase gegen Betrag [E, nach Sicht]

| psi | Raum | Entartung | Phase D(2q)/D(q) min..max | Betrag D(2q)/D(q) min..max | Betrag/Phase bei q = 1e-3 |
|---|---|---|---|---|---|
| 0 | voller T, +Wurzel 6 | 4 | 2,0000 .. 2,00005 | 3,99992 .. 4,00003 | 4,5e-4 |
| 0 | Sektor + | 2 | 2,0000 .. 2,00005 | 3,99992 .. 4,00003 | 4,5e-4 |
| 2 pi/3 | voller T, Wurzel 6 e^{-2i pi/3} | 2 | 2,0000 .. 2,00005 | 3,99992 .. 4,00003 | 4,5e-4 |
| 2 pi/3 | Sektor + | 2 | wie oben | wie oben | 4,5e-4 |

- Lesart [H, nach Sicht]: lambda = lambda0 (1 + i v q.sigma + O(q^2)). Als euklidischer Transfer gelesen ist das eine
  Schwingung mit linearer Dispersion, also ein Kegel in der Phase. Die Daempfung (Betrag) aendert sich erst quadratisch.

## 4. W1, W2 (Diamant, psi = 2 pi/3; Zusatz 4 pi/3) [E, nach Sicht]

- Groesse nach VORAB 3: mu = lambda^2 je Helizitaetssektor, Chiralitaet einer phasenartigen Zweifachstelle =
  Vorzeichen von Re det c der Ableitung von -i ln(mu/mu0), Gegenprobe Fukui-Hatsugai (RR und LR) auf einem Wuerfel.
- Bauart [E]: In jedem Sektor sind zwei der vier mu-Baender identisch null (abs < 2e-14 im ganzen Gitter). Das
  fuehrende Niveau ist das Paar der beiden anderen. Deren Betraege sind in 66,3 % der Gitterpunkte gleich (< 1e-8);
  in den uebrigen 33,7 % spalten sie im Betrag auf (bis 0,67 von max abs mu).

| psi | Sektor | lokale Minima / verfeinert | Weyl (phasenartig) | chi | FH RR/LR (2 Radien) | diabolisch, nicht phasenartig | Ausnahmepunkte (defekt) | Nullpunkte mu = 0 |
|---|---|---|---|---|---|---|---|---|
| 2 pi/3 | + | 134 / 134 | 1: Gamma, mu0 = 6 e^{-2i pi/3} | +1 | +1/+1, +1/+1, 0 Konflikte | 3: X, det-Vorzeichen +1 | 126, alle bei abs(mu) = 1 (+-3e-7) | 4: L |
| 2 pi/3 | - | 138 / 138 | 1: Gamma, mu0 = 6 e^{+2i pi/3} | -1 | -1/-1, -1/-1, 0 Konflikte | 3: X, det-Vorzeichen -1 | 126, alle bei abs(mu) = 1 | 4: L |
| 4 pi/3 | + | 134 / 60 | 1: Gamma | +1 | +1/+1, +1/+1 | 3: X, +1 | 52, abs(mu) = 1 | 4: L |
| 4 pi/3 | - | 137 / 60 | 1: Gamma | -1 | -1/-1, -1/-1 | 3: X, -1 | 52, abs(mu) = 1 | 4: L |

- Die X-Punkte sind zweifach und nicht defekt, aber Q(n) wird in manchen Richtungen negativ (arg Q bis 180 Grad). Dort
  spaltet es im Betrag auf, und auf einem Kegel von Richtungen ist Q = 0. Nach VORAB 3.3 sind das keine Weyl-Punkte. Die
  FH-Gegenprobe dort ist nicht bestimmbar (Verfolgungskonflikte 138 bis 392).
- Die Ausnahmepunkte spalten wurzelartig auf (bei 2 pi/3 mindestens 28 von 52 im Lauf w mit Verhaeltnis 1,38 bis 1,45
  in allen Richtungen). Lesart [H, nach Sicht]: Sie liegen auf einer Ausnahmeflaeche bei abs(lambda) = 1, die die
  Bereiche gleicher Betraege von den Bereichen gleicher Phasen trennt.
- **W1:** S = +1 (Sektor +) und S = -1 (Sektor -) bei 2 pi/3; dasselbe bei 4 pi/3. Das naechste Niveau ist identisch
  null und hat keine Weyl-Punkte. **Nicht eingetroffen.** Ueber beide Sektoren zusammen ist die Summe 0.
  - **Verletzte Nielsen-Ninomiya-Voraussetzung (Karte verlangt sie zu benennen):** Hermitizitaet. T ist ein euklidischer,
    nicht hermitescher, nicht unitaerer Transfer. Das fuehrende Paar bildet kein ueberall getrenntes glattes Bandbuendel
    ueber der Zone: Es hat Ausnahmepunkte (defekt) bei abs(lambda) = 1, Nullstellen bei L und nicht phasenartige
    diabolische Punkte bei X [E]. Dazu [L, aus dem Gedaechtnis]: In nicht hermiteschen bzw. Floquet-Systemen kann die
    Chiralitaetssumme ungleich 0 sein; sie wird dann durch eine Windungszahl bestimmt (Bessho und Sato 2021). Das habe ich
    nicht nachgerechnet.
- **W2:** Je Sektor liegt am fuehrenden Niveau nur eine Chiralitaet: chi = Helizitaetsvorzeichen. Partner auf einem
  tieferen Niveau gibt es nicht, denn das tiefere Niveau ist null. Die Gegenchiralitaet sitzt im anderen
  Helizitaetssektor, bei Gamma, mit gleichem abs(lambda) = Wurzel 6. Liest man W2 ueber beide Sektoren, ist die
  Scheiterbedingung der Karte erfuellt ("beide Chiralitaeten am fuehrenden Niveau"). Liest man je Sektor (VORAB 3.4),
  fehlt der zweite Teil. **Nicht eingetroffen**, in beiden Lesarten.
- Lesart [H, nach Sicht]: Chiralitaet = Helizitaet bei allen drei psi (auch psi = 0, Pauli-Test det c). Das ist
  dieselbe Kopplung wie bei einem masselosen Weyl-Teilchen. Hier ist sie eingebaut, denn der Spin des Laeufers ist an
  seine Laufrichtung gekoppelt (Helizitaet erhalten, VORAB F1 2.1). Bei psi = 0 liegen beide Sektoren bei demselben
  lambda (Dirac-artig: zwei Weyl-Punkte mit entgegengesetzter Chiralitaet). psi ungleich 0 trennt sie nur in der Phase,
  nicht im Betrag. Fuer die schwache Kraft folgt daraus keine einseitige Chiralitaet: Die Huepfregel koppelt keine
  Helizitaet bevorzugt. Ein chirales Spektrum braeuchte einen Mechanismus, der einen Sektor im Betrag unterdrueckt.

## 5. V (Finns Netz V) [E, blind]

- Groessen: 10 Untergitter, 68 Kanten, nd = 136 gerichtete Kanten, 1928 Uebergaenge, Kantenlaengen 0,2165 / 0,3536 /
  0,4146.
- Ursache der Zeitueberschreitung von v4 (Fassung 1): `np.einsum('ai,mab,bj->mij')` ohne optimize, bei nd = 136 etwa
  8,6 s je k-Punkt. In rohr2.py durch matmul ersetzt (gleiche Rechnung, VORAB 4). Danach 12^3 Gitter in zwei Stuecken
  zu je 33 s.
- **V1:** 232 gerichtete Dreiecksschleifen (116 Dreiecke, beide Umlaufrichtungen), alle Phi = 2 pi (Abweichung <
  7e-16), H = -1. Keine Schleife kuerzer als 3. psi = 4 pi/3: ebenfalls alle -1 (3 psi = 4 pi = 0 mod 4 pi [M]).
- **V2 (Sektor +, psi = 0, Gitter 12^3):** max abs(lambda) = 9,778299 bei Gamma (ein Gitterpunkt), zweifach (Luecke
  6,7e-16). Aufspaltung linear in allen 126 Richtungen (Verhaeltnis 1,9999999 bis 2,0000), phasenartig (arg Q < 1e-9
  Grad), chi = +1 (det c = +0,0018683; FH RR/LR = +1 bei beiden Radien, 0 Konflikte). **Eingetroffen.** Weil k0 = Gamma,
  zaehlt Isotropie nicht (sie wurde auch nicht gemessen).
- Weitere Zweifachpunkte des Paares 1-2 auf V: X (abs(lambda) = 6,246) und (1/2, 1/4, 3/4) reziprok (W-Punkt, 5,640).
  Beide sind diabolisch und nicht phasenartig (arg Q etwa 95 Grad). Ihre Linearitaet ist **nicht bestimmt**: Die
  Paarauswahl "zwei betragsgroesste" griff dort Eigenwerte aus dem konjugierten Paar (Abstand 0,91 max abs). Das ist ein
  Auswertefehler, betrifft aber nicht den Gamma-Punkt.
- Auf V haben Band 1 und 2 im ganzen Gitter gleichen Betrag (Anteil 1,0) [E].
- W1 auf V (nur gemeldet): ein Weyl-Punkt (Gamma, chi = +1) unter 3 verfeinerten Kandidaten; Sektor - und psi = 4 pi/3
  nicht gerechnet (Laufbudget).

## 6. Grenzen

- Synthetisch; kappa = 1; Helizitaetssektoren sind durch den Aufbau entkoppelt. Chiralitaet = Helizitaet ist damit
  wahrscheinlich eine Aufbaufolge [H].
- Weyl-Zaehlung: nur Punkte nahe lokaler Gitterminima (24^3 bzw. 12^3) mit Luecke < 0,35. Bei psi = 2 pi/3 wurden alle
  lokalen Minima verfeinert (Lauf w plus Nachtrag wrest), bei 4 pi/3 nur 60. Ein Weyl-Punkt weit weg von jedem
  Gitterminimum kann fehlen.
- Die Einordnung "phasenartig" haengt an der Schwelle arg Q < 1 Grad. Der Abstand ist gross: Gamma 1e-8 Grad, X 180 Grad.
- Ausnahmepunkte: viele Fundstellen derselben Flaeche bzw. Linie, nicht einzeln gezaehlt. "Flaeche" ist Lesart.
- V: nur Sektor +, psi = 0, Gitter 12^3; nur 3 Kandidaten unter der Schwelle.
- Die Windungszahl, die die Chiralitaetssumme im nicht hermiteschen Fall festlegen wuerde, ist nicht gerechnet.

## 7. Regelabweichungen

1. Rauchtests ueber 120 s: vgross 138 s (einsum-Ursache), Rauchtest vaus 158 s (Zeitwaechter im Rauchmodus zu weit).
2. W1/W2 waren laut Karte blind. Die W-Rauchtests (8^3, 6^3) haben sie vor der VORAB sichtbar gemacht. In VORAB 0
   vermerkt; Ausgaenge oben als [nach Sicht] gekennzeichnet.
3. Hauptlauf vaus-0-plus brach an der 600-s-Grenze ab (rc 1, 1,7 GB). Ursache: Wuerfel-FH auf V mit 870 k-Punkten auf
   einmal und zu schwache Zeitwaechter. Repariert nur die Ursache: Wuerfel 6 x 6 je Flaeche in Bloecken zu 40, Waechter
   250/200 s, nur Paar 1-2 (VORAB 4 verlangt nur dieses), hoechstens 4 Kandidaten, Nelder-Mead 300 Schritte. Neuer Code
   rohr2-nachtrag.py (sha256 1ff68017...); Wiederholung vaus-0-plus-b (rc 0, 261 s).
4. Nachtrag nach dem Einfrieren: Vollstaendigkeitslaeufe wrest (2 pi/3, beide Sektoren, lokale Minima ab Rang 61) mit
   neuem Modus in rohr2-nachtrag.py. Gleiche Kriterien; Wuerfel-FH dort nur fuer phasenartige Punkte. Ergebnis: 0
   weitere Weyl-Punkte, nur Ausnahmepunkte.
5. Laufzahl: 13 Hauptlaeufe (g0, p1, 4 x w, v1, 2 x vstueck, vaus (abgebrochen), vaus-b, 2 x wrest) von hoechstens 14.
   V bei psi = 4 pi/3 (VORAB 5, Laeufe 11 bis 13) nicht gerechnet.
6. Die in VORAB 4 genannte Auswahl fuer den Kegeltest auf V (zwei betragsgroesste) ist an X und W fehlerhaft (Abschnitt 5).

## 8. Dateien und Pruefsummen

- Karte, VORAB: KARTE.md 06853026ddc062f6...; VORAB.md b0a02889f89fc48b...; EINGEFROREN-SHA256.txt.
- Code (lokal code/, .69 .69:fmhc-physics-remote/rohr-drehung-2/code/; code/SHA256SUMS-69.txt, lokal geprueft OK):
  - rohr2.py a43b3318172fd088c1eb8973cd762703b0b32210d65afe5359f2cbb05324c43b (eingefroren; Laeufe g0, p1, w, v1, vstueck)
  - rohr2-nachtrag.py 1ff680174550f8cd81cb4f43aa6b952bbb529a7a8585356acc542e4fe7772adc (vaus-0-plus-b, wrest)
  - v/ew.py fa7b6417..., v/tp.py 419d7da6... (unveraendert)
  - Original RUNDE-37/.../rohr.py unveraendert: 7de4339f363dfb22...
- Laeufe: lauf/ (alle *.json, *.log, *.npz; lauf/SHA256SUMS.txt, sha256 11576a30..., lokal mit sha256sum -c OK).
- Rauchtests: rauch/ (rauch/SHA256SUMS.txt, sha256 51b168d4..., OK).
- Ernte Fassung 1: lauf-69-alt/ (SHA256SUMS-ernte-20261009.txt, OK).

## Einfach gesagt

Wir haben ein Teilchen simuliert, das durch ein Netz aus Rohren laeuft und sich dabei mitdreht. Der Fehler in der
alten Symmetriepruefung ist gefunden: Zwei Zustaende mit gleich grosser Zahl, aber entgegengesetztem Vorzeichen waren
vermischt worden. Jetzt zeigt sich sauber, dass die staerksten Zustaende im Rechenmodell (nicht in einer Messung) als Paar
auftreten und sich bei einer vollen Drehung wie ein Spin-1/2-Teilchen umkehren. Die Haendigkeit haengt
fest an der Drehrichtung des Spins zur Laufrichtung. Links- und rechtshaendige Varianten kommen gleich stark vor, also
erklaert das Modell die einseitige schwache Kraft noch nicht. Auf Finns Netz V gibt es denselben Kegel am Zonenmittelpunkt.
