# CHIRAL-IDEEN-1: Dossier. Links-/Rechtshaendigkeit im Rohrgang und der Weg zur schwachen Kraft

- Rechen- und Forschungs-Agent fuer die Leitung claude-primary. Text ab 2026-10-09 19:49:51 CEST (date).
- Auftrag: Finn 09.10. abends ("noch mal weiter aufbereiten, Ideen sammeln und ausprobieren").
- **Kennzeichen:**
  - [E] gerechnet (Projekt)
  - [M] vorab ableitbar (Bauweise, Symmetrie, eigene Algebra; nicht gegengelesen, wo vermerkt)
  - [L] Literatur aus dem Gedaechtnis
  - [S Abstract] bzw. [S] an der Quelle gelesen (Abstract bzw. Volltextabschnitt), Abruf 09.10.2026
  - [P] Projektdatei, dort an der Quelle gelesen, von mir nicht neu geprueft
  - [H] Lesart
- Synthetische Rechnungen sind keine Naturbestaetigung. Nichts hier "erklaert die schwache Kraft".

## 0. Stand auf einer Seite

| Aussage | Status | Fundstelle |
|---|---|---|
| Der Rohrgang (2-Spinor je gerichteter Kante, kein Ruecklauf, Tangenten-Mitdrehung R, Verdrillung W(psi)) erhaelt die Helizitaet exakt; T zerfaellt in T_+ und T_- | [M] Bauweise (R dreht t_i auf t_j, W dreht um t_j); [E] Kommutator 1e-16 | ROHR-DREHUNG-2, VORAB F1 2.1 |
| In jedem Helizitaetssektor ist T_h eine **nicht-ruecklaeufige Huepfmatrix mit Betrag-1-Phasen** (Hashimoto-Matrix mit U(1)-Verbindung auf den gerichteten Kanten). Die Phase eines Uebergangs ist die Berry-Phase der Tangentendrehung | [M] (Spinor-Eigenzustand von t.sigma wird von R auf den von t_j abgebildet, bis auf eine Phase) | neu, aus rohr2.py abgelesen |
| Gleichmaessiges psi ist in jedem Sektor nur ein fester Faktor: T_h(psi) = e^{-i h psi/2} T_h(0). psi verschiebt die beiden Sektoren gegenlaeufig in der Phase, also wie ein **chirales chemisches Potential mu_5** | [M] (W = cos(psi/2) - i sin(psi/2) t.sigma, auf h = +-1 also e^{-+i psi/2}); [E] passt: lambda_+ = Wurzel 6 e^{-i pi/3} bei psi = 2 pi/3 | ROHR-DREHUNG-2 Abschn. 2 |
| Je Sektor ein phasenartiger Weyl-Punkt bei Gamma, chi = h (Diamant psi = 0, 2 pi/3, 4 pi/3; V psi = 0 Sektor +) | [E] | ROHR-DREHUNG-2 Abschn. 4, 5 |
| **Die Sektoren sind durch eine exakte antiunitaere Symmetrie Theta = i sigma_y K verbunden: lambda_-(-k) = conj(lambda_+(k)), chi_- = -chi_+.** Das gilt fuer jedes Netz, jedes psi, jede Verdrillungsbelegung und jedes SU(2)-Kantenfeld, denn sigma_y U* sigma_y = U fuer alle U in SU(2) | [M] (eigene Algebra, nicht gegengelesen; im Test B numerisch mitgeprueft) | neu |
| Daraus: Der "Partner" jedes Weyl-Punkts ist erzwungen und sitzt im anderen Sektor bei -k mit konjugiertem Eigenwert, gleichem Betrag. Die Gesamtchiralitaet ueber beide Sektoren ist 0 | [M] | erklaert W1/W2-Befund in ROHR-DREHUNG-2 |
| Je Sektor ist die Chiralitaetssumme ungleich 0. Nielsen-Ninomiya (NN) greift je Sektor nicht, weil T_h nicht hermitesch ist (Ausnahmepunkte bei abs(lambda) = 1, Nullbaender, nicht phasenartige X-Punkte) | [E] Befund, Grund [H, mit L] | ROHR-DREHUNG-2 Abschn. 4 |
| Eine U(1) nur am Sektor + ist eichinvariant und gibt ein gerichtetes Landau-Niveau +N_phi; die Bilanz liegt nahe dem Nullraum und ist nicht konvergent | [E]; Eichinvarianz [M] | CHIRAL-KOPPLUNG-1 |
| Achiraler Rohrgang auf Diamant: Inversion bzw. Spiegel bilden h auf -h ab; der Sektor allein hat nur die Drehgruppe O | [E] G0: 24 Elemente bei psi = 2 pi/3 | ROHR-DREHUNG-2 Abschn. 2 |
| Literatur: NN, GW/Overlap, Domaenenwand, Spiegel-Fermionen, Floquet- und nicht-hermitesche Erweiterungen | [L], [S Abstract], [P] | Abschn. 5; CHIRAL-L-Dossier (RUNDE-37) |

## 1. Was "je Sektor ein Weyl-Punkt" bedeutet und was nicht

**Es bedeutet:**
- Innerhalb des Rechenmodells gibt es einen Sektor (Helizitaet +), dessen fuehrendes Niveau genau einen
  Weyl-Kegel einer Haendigkeit traegt. Ein hermitesches Gitter mit erhaltener Ladung koennte das nicht [L, NN 1981].
- Der Kegel ist "phasenartig": lambda = lambda0 (1 + i v q.sigma + O(q^2)). Liest man T wie einen Zeitschritt, ist die
  Phase die Schwingung und der Betrag die Daempfung. Der Kegel verhaelt sich also wie ein **Floquet-Kegel in der
  Quasienergie** [E, P1], nicht wie ein euklidischer Massen-Kegel.
- Die lokale Chiralitaet ist eine robuste Zahl. Kleine Stoerungen, die die Helizitaet erhalten, koennen den Punkt nur
  verschieben [M, Standardargument des lokalen Abbildungsgrads].

**Es bedeutet nicht:**
- Kein netto-chirales Modell: Theta erzwingt den Gegenpartner im anderen Sektor mit gleichem Betrag [M].
  Ueber den ganzen Zustandsraum ist das Spektrum vektoriell, wie bei einem masselosen Dirac-Teilchen, dessen zwei
  Weyl-Haelften entkoppelt sind.
- "chi = Helizitaet" ist keine Netzeigenschaft. Es ist die Kopplung von Spin an Laufrichtung, die der Bau einsetzt
  (Mitdrehung). Sie gilt fuer jedes Netz [M; E auf Diamant und V]. Auch ein chirales Netz kann sie nicht umdrehen
  (Abschn. 3).
- Keine Verletzung eines Satzes: NN setzt Hermitizitaet voraus. Fuer nicht hermitesche bzw. Floquet-Operatoren gilt
  die erweiterte Form von Bessho/Sato: Die Netto-Ladung der Weyl-Punkte ist eine Volumen-Windungszahl w3 [S, im Projekt
  gelesen: QCA-WINDUNG-1 PLAN F2, arXiv:2006.04204v3 Theorem 2 und 3']. Die Rechnung zu dieser Windungszahl fehlte
  bisher (ROHR-DREHUNG-2 Abschn. 6, letzter Punkt). Test B dieser Karte holt sie nach.
- Kein Befund zur Natur: Es gibt keinen Messwert, an dem das hier etwas pruefen wuerde.

## 2. Warum die chirale Kopplung bisher gesetzt und nicht emergent ist

- Die Helizitaet ist durch den Bau erhalten. Also ist **jede** Kantenphase der Form e^{i(theta_V + h theta_A)}
  eichinvariant: Die axiale U(1) (Phase e^{i h alpha_v} je Ecke) ist eine exakte, auf den gerichteten Kanten lokale
  Symmetrie [M].
- CHIRAL-KOPPLUNG-1 hat "nur Sektor +" gewaehlt, also theta_A = theta_V. Das Netz verbietet die Wahl nicht, aber es
  waehlt sie auch nicht. Jede Mischung theta_V, theta_A ist gleich erlaubt [M].
- Neu [M]: **Die Verdrillung psi_e je Kante ist bereits eine axiale Kantenphase** mit theta_A = -psi_e/2 (Abschn. 0,
  Zeile 3). Eine chirale Kopplung "nur an +" ist damit Kantenphase theta plus Verdrillung psi_e = -2 theta. Die Lesart
  [H]: Wenn psi ein dynamisches Feld waere (IDEE (5)), traegt das Netz schon ein axiales Eichfeld. Ein Prinzip, das
  psi_e an die Kantenphase bindet, haette die Kopplung "nur an eine Haendigkeit" erzeugt statt gesetzt. Ein solches
  Prinzip ist nicht in Sicht.
- Fuer die schwache Kraft reicht U(1) nicht: Gebraucht ist SU(2) nur am Sektor - (links). Das geht im Rohrgang
  formal genauso (Projektor P_- U P_- mit U in SU(2) in einem inneren Raum), ist aber genauso gesetzt [M].
- Kurz: Emergent waere die Kopplung erst, wenn eine Groesse des Netzes (Rahmen, Eckfeld, Zeitrichtung) h = +1 und
  h = -1 verschieden behandelt **und** dabei nicht unter Theta liegt. Jede SU(2)-Regel liegt unter Theta [M]. Brechen
  koennen das nur (i) Phasen, die von h abhaengen (U(1) bzw. Verdrillung, also wieder gesetzt), (ii) nicht unitaere
  Faktoren mit h-Abhaengigkeit, etwa ein Lorentz-Schub e^{eps t.sigma/2} statt einer Drehung (SL(2,C) statt SU(2)),
  (iii) eine Kopplung, die h mischt (Masse, Abschn. 4 und Test A).

## 3. Netz-Haendigkeit und Td: was die Symmetrie schon festlegt [M]

- Ein Spiegel M bildet ein Netz N auf sein Spiegelbild N' ab, h auf -h und einen Weyl-Punkt chi auf -chi. Also hat
  N' im Sektor + die Chiralitaet -chi_-(N) = chi_+(N) (mit Theta). **Netz und Spiegelnetz haben je Sektor dieselbe
  Chiralitaet.** Die Haendigkeit eines chiralen Netzes (srs bzw. K4, I4_1 32; P2_1 3) kann also nicht entscheiden,
  welche Helizitaet koppelt [M, nicht gegengelesen].
- Was ein chirales Netz aendert [M]: Die Sektoren + und - sind am selben k durch keine Raumsymmetrie mehr verbunden,
  nur noch ueber Theta (k -> -k, lambda -> conj lambda). Betragsspektren gleich bis auf k -> -k; das groesste
  abs(lambda) ist in beiden Sektoren gleich.
- Td bzw. F-43m (gebrochene Inversion, achiral): Ohne Inversion kann abs(lambda_+(k)) - abs(lambda_-(k)) ungerade in
  k sein; der niedrigste Td-invariante ungerade Term ist kubisch (Dresselhaus-Form k_x(k_y^2 - k_z^2) + zykl.)
  [M mit L, Dresselhaus 1955]. Das ist eine helizitaetsabhaengige Richtungsasymmetrie, keine Netto-Chiralitaet.
- Grenze: Der Rohrgang nutzt keine Potenzgewichte; er sieht nur Ecken und Tangenten. F-43m-Gewichte aus
  REGULAER-V-1 N2 wirken auf den Rohrgang erst, wenn man gewichtete Uebergaenge einfuehrt (IDEE (4)).

## 4. Wohin die Anomalie muesste

- Kontinuum [L]: Ein einzelnes geladenes Weyl-Teilchen hat in E parallel B eine nicht erhaltene Ladung
  (Adler-Bell-Jackiw). Gitter mit endlich vielen Freiheitsgraden haben keine Anomalie; was im Kontinuum anomal ist,
  muss auf dem Gitter woanders sitzen [P: Kaplan 0912.2560, Z. 1325-1327, im CHIRAL-L-Dossier gelesen].
- Moegliche Orte im Rohrgang:
  - (a) im anderen Sektor (vektoriell): ausgeschlossen, wenn die Kopplung nur an + geht; der Sektor - ist dann feldfrei
    [E, CK1].
  - (b) in der Nicht-Unitaritaet: Zustaende verlassen das Niveau abs(lambda) gleich dem fuehrenden. CK1 fand keinen
    Ausnahmepunkt auf den gerichteten Bahnen, aber eine nicht konvergente Bilanz nahe dem Nullraum.
  - (c) in einer Volumen-Windungszahl: Nach Bessho/Sato traegt eine Punktluecke mit w3 ungleich 0 die Netto-Chiralitaet
    [S, P]. Fuer T_+ ist das die natuerliche Buchhaltung: Unterhalb des Weyl-Punkts (gleiche Phase, kleinerer Betrag)
    liegt lokal eine Punktluecke [M, Abschn. 6 von IDEEN]. Die Netto-Ladung +1 muss dann dort sitzen, wo diese Luecke
    sich schliesst. Ob das an der Ausnahmeflaeche abs(mu) = 1 oder am Nullraum passiert, ist die offene Frage, die
    CK1 nicht aufloesen konnte. Test B rechnet sie.
- Physikalisch (Lesart [H]): Ort (b) und (c) bedeuten, dass die Anomalie im **Verlust der Wahrscheinlichkeit** sitzt.
  Ein Zeitschritt, der Norm verliert, ist kein unitaeres Quantensystem. Nach Golterman/Shamir ist "eichinvariant, aber
  nicht unitaer" genau die bekannte Scheiterform anderer Wege [S Abstract 2311.12790, ueber CHIRAL-L].

## 5. Literatur, kurz (Abruf 09.10.2026, sonst aus dem Projekt)

| Thema | Kernaussage | Quelle |
|---|---|---|
| Nielsen-Ninomiya | Lokal, hermitesch, translationsinvariant, erhaltene Ladung: gleich viele L- und R-Weyl-Punkte | Nielsen, Ninomiya, Nucl. Phys. B185 (1981) 20 und B193 (1981) 173 [L]. Kaplan, arXiv:0912.2560, Abschn. 3.1: vier Bedingungen (lokal, richtiger Limes, keine weiteren Nullstellen, chirale Symmetrie) [P, S in CHIRAL-L] |
| Grund hinter NN | Anomalie: "any symmetry anomalous in the continuum limit must be broken explicitly" | Kaplan 0912.2560, Z. 1325-1327 [P] |
| Ginsparg-Wilson / Luescher | GW-Relation "implies an exact symmetry of the fermion action"; NN nicht verletzt, weil Chiralsymmetrie anders verwirklicht | Luescher, arXiv:hep-lat/9802011, Abstract [S Abstract] |
| Domaenenwand | "A method for simulating chiral gauge theories on the lattice"; Nullmoden auf einem Defekt | Kaplan, arXiv:hep-lat/9206013, PLB 288 (1992) 342 [S Abstract] |
| Spiegel-Fermionen (Eichten-Preskill) | Fermionen Dirac-artig im ganzen Phasendiagramm, "no room for undoubled Weyl fermions" | Golterman, Petcher, Rivas, arXiv:hep-lat/9206010, NPB 395 (1993) [S Abstract]; Eichten, Preskill, NPB 268 (1986) 179 [L] |
| SMG-Kritik | "unitarity of the gauge theory is lost" (auch bei anomaler Zieltheorie) | Golterman, Shamir, arXiv:2311.12790 [P, S Abstract in CHIRAL-L]; 2505.20436, 2603.15985 [P] |
| Floquet/nicht hermitesch | Erweiterter NN-Satz: Netto-Ladung = Volumenzahl w3; "duality enabling a unified treatment of periodically driven systems and non-Hermitian ones" | Bessho, Sato, arXiv:2006.04204, PRL 127, 196404 (2021) [S Abstract; S Theorem 2/3' laut QCA-WINDUNG-1 PLAN F2] |
| Einzelnes Floquet-Weyl | Einzelner Weyl-Punkt im getriebenen 3D-Gitter mit nichttrivialer Floquet-Unitaeren | Higashikawa, Nakagawa, Ueda, arXiv:1806.06868, PRL 123, 066403 [P, S Abstract]; im Projekt nachgebaut, Partner im abgetrennten Bandraum (QCA-WINDUNG-1 Teil 2) [P] |
| Streng lokaler Takt | Jede endlichreichweitige Unitaere in 3D hat W3 = 0 | QCA-WINDUNG-1 Teil 2, Ergebnis 2 [P, M mit L]. **Achtung [M]:** Das gilt fuer unitaere Operatoren. Ein endlichreichweitiger nicht unitaerer Operator kann w3 ungleich 0 haben; Beispiel ist der Wilson-Dirac-Operator (m + Summe cos k) + i Summe sin k_j sigma_j mit Abbildungsgrad 1 fuer 1 < abs(m) < 3 [L, Grundlage der Domaenenwand] |
| Nicht hermitesche Gitterfermionen | "By abandoning Hermiticity, the non-Hermitian formulation circumvents the Nielsen-Ninomiya theorem." Bau: einseitige Differenzen, e^{ipa} statt i sin(pa), halbe Polzahl; Preis u. a. "absence of non-trivial topological charge", Abhaengigkeit von a | Ma, Zhang, arXiv:2411.09886v3, Abstract und Abschn. 4.5, Abschn. 1 [S Abstract, S Abschn.] |
| Weyl-Punkte nicht hermitesch | Nicht-Hermitizitaet verformt einen Weyl-Punkt zu einem Ring von Ausnahmepunkten; "topological dumbbell of exceptional points" in 3D | Kawabata, Bessho, Sato, arXiv:1902.08479, PRL 123, 066405 (2019) [S Abstract]; Weyl-Ausnahmeringe: Xu, Wang, Duan, PRL 118, 045701 (2017) [L] |
| Chirale Kristalle (I4_1 32 u. a.) | Fuer einige Raumgruppen ist die Existenz chiraler Volumen-Fermionen "not only possible but unavoidable"; Beispiel I4_1 32 mit vier Atomen je Zelle, drei Nachbarn (srs-Netz) | Manes, arXiv:1109.2581, PRB 85, 155118 (2012) [S Abstract] |
| Mehrfach-Fermionen | Durch Raumgruppen stabilisierte 3-, 6-, 8-fach-Kreuzungen; Fermi-Boegen ohne Weyl | Bradlyn u. a., arXiv:1603.03093, Science 2016 [S Abstract]; CoSi-Familie mit "non-zero Berry flux": Tang, Zhou, Zhang, arXiv:1706.03817, PRL 119, 206402 [S Abstract]. Partner bei Gamma und R mit entgegengesetzter Chern-Zahl [L]; NN gilt dort |
| Dresselhaus | Td ohne Inversion: kubische Spinaufspaltung | Dresselhaus, Phys. Rev. 100, 580 (1955) [L] |

- **Nicht hermitesch und NN, letzte 5 Jahre (Suche 09.10.):** Eine Arbeit mit ungepaartem Weyl-Punkt in einem
  statischen nicht hermiteschen 3D-Bandmodell habe ich in einer Websuche nicht gefunden. Gefunden sind die
  Bessho/Sato-Buchhaltung (Netto-Ladung = w3) und Ausnahmeringe aus Weyl-Punkten. Lesart [H]: Der Rohrgang ist ein
  Beispiel der Bessho/Sato-Art, wenn seine Punktluecke w3 = +-1 traegt. Das prueft Test B.
- Weiteres Literaturbild (Moderatoren Lokalitaet, Kopplung, on-site, Zeit, Dimension, Gruppe) steht im
  CHIRAL-L-Dossier (RUNDE-37/chiral-l/DOSSIER.md, Abschn. 4 bis 5) und wird hier nicht wiederholt.

## 6. Was das fuer das Gesamtmodell heisst [H]

- Der Rohrgang ist ein Ort, an dem der NN-Satz je Sektor nicht greift, ohne Extra-Dimension. Er bezahlt das mit
  Nicht-Hermitizitaet bzw. Nicht-Unitaritaet. Das ist die Ma/Zhang-Klasse (gerichtete, einseitige Schritte), nicht
  die Kaplan-Klasse.
- Die schwache Kraft verlangt mehr als einen einseitigen Sektor: Die Kopplung muss eine Haendigkeit auswaehlen. Im
  Rohrgang waehlt nichts; Theta verbindet die Sektoren exakt. Der einzige Hebel ohne Setzung waere ein Prinzip, das
  die Verdrillung psi (axiale Kantenphase) an die Eichphase bindet, oder ein Lorentz-Rahmen (SL(2,C)), der Schub und
  Drehung unterscheidet.
- Ehrliche Lage: Die schwache Kraft bleibt im Gesamtmodell ein ausgewiesenes Loch (Ausweg (d) des Entwurfs). Das
  Rohrgang-Ergebnis verschiebt das Loch: Statt "Doppler ueberall" ist es jetzt "einseitig je Sektor moeglich, aber die
  Auswahl ist gesetzt und die Anomalie sitzt im Normverlust".

## Einfach gesagt

Im Rohrnetz-Modell laufen Teilchen, deren Spin fest an die Laufrichtung gekoppelt ist. Dadurch zerfallen sie in
links- und rechtsdrehende Sorten, die nie ineinander uebergehen. Jede Sorte allein sieht "einseitig" aus, was auf
einem normalen Gitter verboten waere. Moeglich wird das nur, weil der Rechenschritt Wahrscheinlichkeit verlieren
kann. Eine exakte Spiegel-Regel sorgt aber dafuer, dass es zu jeder linken Sorte die gleich starke rechte gibt. Dass
die schwache Kraft nur die linke Sorte anfasst, muss man deshalb bisher von Hand einsetzen.

## Nachtrag nach den Tests (2026-10-09 20:16:21 CEST, nach dem Einfrieren dieser Datei angefuegt; Stand vor dem Nachtrag: sha256 7348c924...)

- **Test A (ERGEBNIS-UMKEHR-MASSE):** Die spin-erhaltende Kehrtwende ist die Dirac-Masse des Rohrgangs. Bei psi = 0
  spaltet sie das Gamma-Quartett genau in Wurzel 6 +- r. Reelles r: Masse im Betrag mit Ausnahmeflaeche (PT-Bruch) bei
  q* (auf 1 %); imaginaeres r: echte Luecke in der Phase. Bei psi = 2 pi/3 bleiben beide Weyl-Punkte bis r = 0,3
  erhalten: Verdrillung (mu_5) und Masse stehen sich im Weg [E].
- **Test B (ERGEBNIS-PUNKTLUECKE-W3):** Die Netto-Chiralitaet je Sektor ist eine ganzzahlige Punktluecken-Windung
  w3 = +1 (Sektor -: -1, 161 von 161 Paaren). Das Gebiet mit w3 = +1 ist ein Keil vom Weyl-Punkt bis an den Ursprung;
  die Ausnahmeflaeche abs(mu) = 1 aendert nichts. Die Gegenladung sitzt bei lambda = 0 [E; Lesart H]. B1 bis B3 im
  Wortlaut nicht eingetroffen (Aufloesung am Weyl-Punkt bzw. Folge davon).
- **Test C (ERGEBNIS-HERMITESCH):** Die erste hermitesche Fassung war ungeeignet (H_s(Gamma) = 0). Die Mischform H_m
  hat im obersten Bandpaar Gamma (+1), vier L-Punkte (-1, gleiche Energie Wurzel 6) und drei X-Punkte (+1): NN kehrt
  zurueck, die Partner liegen genau dort, wo T Nullstellen (L) bzw. nicht phasenartige Punkte (X) hat [E].
- **Zusammen [H]:** Der Rohrgang ist je Sektor chiral, weil der nicht-ruecklaeufige, nicht unitaere Transfer die
  L-Doppler auf lambda = 0 drueckt. Das ist "Doppler schwer machen" im euklidischen Sinn, ohne Wilson-Term. Fuer die
  schwache Kraft bleibt: Theta paart die Sektoren exakt, die Auswahl einer Haendigkeit ist gesetzt, und die Anomalie
  sitzt im Ausloeschen von Zustaenden, also nicht in einem unitaeren Bild. Die schwache Kraft bleibt ein ausgewiesenes
  Loch.
