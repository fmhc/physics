# CHIRAL-L: Dossier (Feldforscher fuer die Leitung, Runde 41)

- **Zeiten (date):** Start 2026-10-04 14:20:02 CEST; Abrufe 14:24:25 bis 14:29:31; Text dieser Datei ab 14:38:40 CEST.
  Zeitbox 60 min.
- **Arbeitsdatei:** ARBEITSFELD.md (Erwartung vor jedem Abruf, Ausgang, Abschn. 2b Projektdaten, Gegensweep).
- **Abrufe:** 12 von 12 (zwei davon ohne Inhalt, einer mit falscher Nummer; Selbstanzeigen 2 und 3). Keine Websuche.
  Lokale Kopien in quellen/.
- **Kennzeichen:** [S] selbst an der Quelle gelesen (Volltext per pdftotext, Zeile angegeben); [S Abstract] nur der
  Abstract (arXiv-Seite oder API-Antwort); [P] Projektdatei, dort als gelesen gefuehrt, von mir nicht an der
  Primaerquelle geprueft; [L] Gedaechtnis; [L?] unsicher; [M] eigene Algebra, nicht gegengelesen; [ES] eigener
  Schluss; [H] Hypothese.
- **Art:** Literatur und Schreibtisch. Keine Rechnung auf der .69, keine Messdaten.

## 1. Ergebnis zuerst

Kein Kandidat traegt das Standardmodell, und kein Weg dahin ist in 3+1D gebaut. Nielsen/Ninomiya (NN) verbietet
nicht chirale Fermionen schlechthin, sondern sie fuer **lokale, freie, statische Gittermodelle mit on-site-Symmetrie**.
Die tiefere Form ist ein Anomalie-Satz, der fuer jede Regularisierung mit endlich vielen Freiheitsgraden gilt.
Alle bekannten Auswege verschieben die Anomalie an einen anderen Ort: Extra-Dimension, nicht-on-site-Symmetrie,
stark gekoppelte Spiegel, Nichtlokalitaet, periodischer Antrieb. Exakt gezeigt ist das nur in 1+1D; in 3+1D gibt es
abelsche Vorschlaege (U(1)-Hyperladung, mit Extra-Dimension) und den unbewiesenen SO(10)-Vorschlag von Wang/Wen.
**Nichtabelsche chirale Eichtheorien in 3+1D sind offen.** Die Erwartung der Leitung trifft **nur teils** zu:
K-A und K-M stossen an diese Frage, jeder mit einem eigenen Weg; K-B steht davor, weil es noch keinen
Dirac-Operator gibt. Keiner hat einen strukturellen Vorteil, der das nichtabelsche Problem loest.

1. **Was NN genau verbietet [S]:** Kaplan (2012, Abschn. 3.1): Eine bilineare Fermion-Wirkung kann nicht zugleich
   (1) lokal (periodisch-analytisch in p), (2) im Kontinuum ein Dirac-Fermion, (3) ohne weitere Nullstellen und
   (4) chiral symmetrisch ({Gamma, D} = 0) sein. Der Grund ist die Anomalie: "any symmetry that is exact on the
   lattice will be exact in the continuum limit, while any symmetry anomalous in the continuum limit must be broken
   explicitly on the lattice" (Z. 1325-1327). Thorngren/Preskill/Fidkowski (TPF, 2026): "lattice models with strictly
   local interactions and strictly on-site symmetries generically produce fermions in vector-like pairs" (Z. 90-92).
2. **Stand fuer das volle SM [S]:** Kaplan 2012: "no practical way to regulate general nonabelian chiral gauge
   theories on the lattice" (Z. 2324-2334). TPF 2026: "a complete Hamiltonian realization of the full Standard Model
   has not yet been achieved" (Z. 230-231). Der SMG-Weg (Spiegel durch starke Kopplung ohne Symmetriebruch entfernen)
   ist umstritten: Golterman/Shamir finden in einem effektiven Lagrange-Ansatz Geister und Verlust der Unitaritaet (2023/24) und formulieren ein verallgemeinertes
   No-go unter Bedingungen (2025) [S Abstract].
3. **Bosonische lokale Netze [S, S Abstract]:** Nichtabelsche Eichbosonen und (vektorartige) Fermionen aus
   String-Netzen gibt es im Prinzip (Levin/Wen). Chiral: 2005/07 "we do not know ... much less a local bosonic
   model"; seit 2018 schlaegt Wen ein Qubit-Gitter fuer das SO(10)-SM vor; seit 2026 sind Bosonen das bevorzugte
   Werkzeug gegen NN, exakt aber nur in 1+1D.
4. **Kausalmengen [S Abstract]:** Kein Abstract mit "chiral" (0 von 25 Treffern). Nichtabelsche Eichfelder als
   Vorschlag ueber Holonomien je Punktpaar (Sverdlov 2008). Spinoren nur mit Zusatzstruktur (SPIN-KAUSAL-L [P]).
5. **Folge je Kandidat [ES]:** Jeder braucht zusaetzlich zu inneren Zustaenden einen **Ort fuer die Anomalie**
   (Abschn. 7). K-A: 4. Raumrichtung als Platte, starke Spiegelkopplung, Rotoren mit nicht-on-site-Symmetrie oder
   Windung der QCA; dazu nichtabelsche String-Netz-Marken statt Pfeilen. K-M: 5. Dimension oder Kaehler-Dirac plus
   SMG (Catterall), Eichlinks eingesetzt. K-B: erst Rahmen je Element und ein Dirac-Operator; NN greift dort formal
   nicht (nichtlokal), der Anomalie-Satz schon.

## 2. Erwartungsverstoesse (das Wichtigste zuerst)

| Nr | Erwartet | Gefunden | Fundstelle |
|---|---|---|---|
| V1 | E3: Bosonische Netze sind fuer chirale Fermionen die schwerere Ausgangslage (Levin/Wen 2005: "much less a local bosonic model") | **Umgekehrt seit 2018/2026:** Bosonen bzw. Rotoren sind der Hebel gegen NN. Wang/Wen 2018: SM aus SO(10) "via a 3+1D local lattice model of bosons or qubits" (Vorschlag). Lu/Seifnashri/Shao 2026: "Nielsen-Ninomiya-type no-go theorems are evaded by using lattice bosons rather than fermions" (3+1D, Kontinuum = kompakter Boson mit Axion-Kopplung, keine Weyl-Fermionen). Baig u. a. 2026 (2D): Bosonen-Modell ultralokal, rekonstruierter Dirac-Operator ohne Doppler, aber nichtlokal. TPF 2026: Rotoren, 1+1D exakt, 3+1D nur U(1) | Levin/Wen hep-th/0507118 Z. 1433-1444 [S]; 1809.11171, 2604.06307, 2607.09935 [S Abstract]; 2601.04304 Z. 163-191 [S] |
| V2 | E2: SMG umstritten | **Schaerfer:** Golterman/Shamir 2023/24: Nullstellen der Spiegel-Propagatoren wirken als gekoppelte Geister; "gauge invariance will always be maintained in an SMG phase, in fact, even if the target chiral gauge theory is anomalous, but unitarity of the gauge theory is lost." 2025 (publiziert): verallgemeinertes No-go, "If these conditions are satisfied, the massless fermion spectrum must be vector-like", und 2D-Lehren nur begrenzt auf 4D uebertragbar | 2311.12790, 2505.20436v3, 2603.15985 [S Abstract] |
| V3 | stillschweigend: Anomaliefreiheit des SM reicht im Prinzip fuer ein Gitter | **Nein:** "there are obstructions to gauging symmetries on the lattice that have no analogue in the continuum ... anomaly cancellation in quantum field theory does not, in general, guarantee the existence of a corresponding lattice construction". Auch TPF brauchen in 3+1D eine "D+1-dimensional slab", und das Lueckenschliessen ist dort nur "plausibly" | TPF 2601.04304v2 Z. 127-128, 170-191 [S] |
| V4 | R1: NN gilt fuer unsere QCA (diskrete Zeit) wie fuer Hamilton-Gitter | **Nicht in derselben Form:** "In static lattice systems, the Nielsen-Ninomiya theorem enforces the pairing ... Periodic driving provides a viable route to circumvent this no-go constraint" (Netto-Chiralitaet je Quasienergie-Sektor). **Aber** der D'Ariano/Perinotti-Automat, Grundlage unserer QCA, ist bei Quasienergie 0 vektorartig: Gamma und P' haben entgegengesetzte Chiralitaet (Abbildungsgrad 0) [M]. Der QCA-Preprint, der die schwache Wechselwirkung aufs Gitter bringen will, hat einen vektorartigen Zustandsraum mit abgekoppeltem Zuschauer (g_R = 0, psi_R = 0 als Anfangsbedingung) | 2602.11935 [S Abstract]; ARBEITSFELD Abschn. 2b [M]; QCA-TETRA-1 ERGEBNIS Z. 166-172 [P]; 2505.07900v3 Z. 2141-2252 [S] |
| V5 | E4/F8: Eichfelder auf Kausalmengen hoechstens abelsch oder skizziert | Nichtabelsche Vorschlaege existieren: "charged scalar field coupled to a SU(n) Yang-Mills field ... in terms of holonomies between pairs of points, causal relations, and volumes"; Sverdlov/Bombelli 2009 "Yang-Mills gauge fields". Chiral: nichts | 0807.2066, 0905.1506 [S Abstract]; F8: 0 von 25 Abstracts mit "chiral" [S] |
| V6 | F2: SMG fuer das SM verlangt 16 Weyl-Fermionen je Generation | Wang/You: alle lokalen und globalen Anomalien verschwinden fuer 15Nf- und 16Nf-SM, "such that the SMG is possible in either cases"; nur wenn U(1)_{B-L} erhalten bleiben soll, "the SMG preserving an additional U(1)B−L only works for the 16Nf -SM" | 2204.14271 Fluss-Text Z. 3246-3303 [S] |
| V7 (Methode) | Kaplan/Sen "Weyl fermions on a finite lattice" unter 2312.04501 | Die Nummer gehoert zu einer fachfremden Arbeit (Graph Metanetworks). Kaplan/Sen 2024 und Kroth/Sen 2025 kamen ueber die API-Abfrage | F6, Selbstanzeige 2 |

## 3. Erwartungen der Karte mit Ausgang

| Nr | Erwartung | Ausgang | Fundstelle |
|---|---|---|---|
| E1 | NN: lokaler, hermitescher, translationsinvarianter Gitter-Hamiltonian mit erhaltener Ladung hat gleich viele links- wie rechtshaendige Weyl-Fermionen [L] | **eingetroffen, Form korrigiert.** Kaplans Fassung ist euklidisch und hat vier Bedingungen (lokal, richtiger Limes, keine weiteren Nullstellen, chirale Symmetrie); Hermitezitaet steht nicht darin. NN 1981 im Wortlaut (zitiert bei Bakircioglu u. a.): "the appearance of equally many right- and left-handed species ... is an unavoidable consequence of a lattice theory under some mild assumptions". Belastbar ist die Anomalie-Form (Z. 1325-1327); sie braucht keine Translationsinvarianz [ES]. Liu 2026: "fundamental algebraic incompatibility between anomaly data and the dimension of local Hilbert spaces" | Kaplan 0912.2560v2 Z. 1294-1327 [S]; 2505.07900v3 Z. 2093-2096 [S, Sekundaerzitat]; 2602.13948 [S Abstract] |
| E2 | Auswege GW/Overlap, Domain-Wall, Spiegel mit SMG; volles SM ungeloest [L] | **eingetroffen.** Overlap/Domain-Wall: "a way to represent any global chiral symmetry without fine tuning" (Z. 2322-2323); nichtabelsch chiral: "no practical way". SMG: Numerik in 3+1D nur fuer vektorartige Spielmodelle (so(4) Higgs-Yukawa, su(4)); chirale Erfolge in 1+1D (DMRG; Domain-Wall-SMG 2026). Volles SM: nirgends gebaut (TPF Z. 230-231). Das Feld ist 2025-2026 sehr aktiv (84 Treffer in 24 Monaten) | Kaplan Z. 2322-2334 [S]; Wang/You Z. 207-223, Tab. II (Fluss-Text Z. 1213) [S]; 2608.29963 [S Abstract]; TPF [S] |
| E3 | Emergente nichtabelsche Eichfelder aus lokalen bosonischen Netzen ja; chirale Fermionen in 3+1D hoechstens Spezialfaelle [L?] | **teils verletzt (V1).** Nichtabelsch: Levin/Wen "gauge bosons with any gauge group", SU(3) "one should be able to" (Behauptung, kein Bau in dieser Arbeit). Chiral in 3+1D: Vorschlag (Wang/Wen), abelsch mit Platte (TPF), chirale *Symmetrie* aus Bosonen (Lu u. a.). Gebaut und geloest: nur 1+1D | hep-th/0507118 Z. 1417-1444 [S]; Abstracts wie V1 |
| E4 | Keine chiralen Fermionen auf Kausalmengen; schon Spinoren brauchen Zusatzstruktur [L?] | **eingetroffen fuer chiral; zu Eichfeldern verletzt (V5).** 0 von 25 Abstracts. Spinoren: Rahmen bzw. Clifford-Struktur eingesetzt (SPIN-KAUSAL-L) | F8 [S]; SPIN-KAUSAL-L DOSSIER Abschn. 1 [P] |
| E5 | Zufallsgitter heben die Verdopplung nicht auf; gespalten; mit Eichfeld kehren Doppler zurueck [L?] | **ohne Abruf aus dem Projekt beantwortet: gespalten.** Griffin/Kieu 1992 ("revived for random lattices" mit Eichfeld), Kieu u. a. 1994, Cohen 2006; im Projekt das raue Band statt Kegeln (SPIN-ZUFALLSNETZ-1) | SPIN-KAUSAL-L DOSSIER Abschn. 4 [P, dort S Abstract]; SPIN-ZUFALLSNETZ-1 [P] |

Abruf-Erwartungen F1 bis F12 mit Ausgang stehen in ARBEITSFELD.md Abschn. 2: bestaetigt F1, F3, F5, F12 (F12 mit
Ergaenzung Platte), F8 fuer chiral; verletzt F2 (15 statt 16), F4 (Qubit-Gitter), F7 (Art der Arbeiten), F8 fuer
Eichfelder, F11 nur in der Begruendung; F6 Fehlabruf.

## 4. Literaturstand (kurz)

### 4.1 Was NN verbietet und wann nicht

- **Annahmen** (Kaplan Z. 1301-1309 [S]; TPF Z. 90-92 [S]; Hamilton-Form NN 1981 [L]): lokal; on-site wirkende
  Symmetrie; frei (bilinear); statisch; hermitesch; endlich-dimensionale lokale Raeume (Liu 2026 [S Abstract]).
- **Tiefer Grund** (Kaplan Z. 1319-1327 [S]): Bei endlich vielen Freiheitsgraden gibt es keine Anomalie; was im
  Kontinuum anomal ist, muss auf dem Gitter explizit gebrochen oder anders verwirklicht sein.
- **Wo es nicht gilt (je eine Annahme faellt):**
  - nichtlokal: SLAC-Ableitung; Preis: QED-Ward-Identitaet, Vertex "infinite at the BZ boundary" (Kaplan Z.
    1310-1314 [S]). Gegenbeispiel 2D: ultralokales Bosonen-Modell, Dirac-Operator nichtlokal, Eichung der nicht
    anomalen Symmetrien moeglich (Baig u. a. 2026 [S Abstract]). Kontinuum: nichtlokale QFT ohne Doppler, wenn der
    Formfaktor nirgends verschwindet (Kouroshnia/Moffat/Thompson 2026 [S Abstract])
  - nicht on-site: Overlap/Ginsparg-Wilson (modifizierte chirale Symmetrie; "does not provide an explicitly local
    Hamiltonian", TPF Z. 101-106 [S]); Disentangler (TPF); Bosonen (Lu u. a. 2026)
  - nicht frei: SMG (umstritten, V2)
  - nicht statisch: periodischer Antrieb, ungepaarte Weyl-Punkte je Quasienergie (Lin/Zhang/Zhang 2026 [S Abstract])
  - nicht hermitesch: Ma/Zhang 2024 [S Abstract]
  - Extra-Dimension: Domain-Wall, Anomalie im Volumen (Kaplan Abschn. 3.2-3.4, nicht gelesen; TPF Z. 93-99 [S])

### 4.2 Auswege und Stand fuer das volle SM

| Weg | gezeigt | 3+1D | nichtabelsch chiral | Quelle |
|---|---|---|---|---|
| Overlap/GW, Domain-Wall | globale chirale Symmetrie, Gitter-QCD-Praxis | ja | "no practical way" (2012) | Kaplan Z. 2322-2334 [S] |
| Domain-Wall auf endlichem Gitter, Platte mit Gradientenfluss | ungepaarter Weyl auf Achsen-String (n = 1); Fluss mit Hintergrundfeld (2D) | Vorschlag (Kaplan/Sen 2024: 4D als Rand von 5D, "may be realized on a finite lattice") | offen | 2412.02024, 2506.04324, 2606.05306 [S Abstract] |
| SMG (Spiegel stark gekoppelt) | 1+1D (3-4-5-0, DMRG); Domain-Wall-SMG 2D (2026); 3+1D nur vektorartige Spielmodelle | Vorschlag Wang/Wen (SO(10), 16 Weyl) | umstritten (Golterman/Shamir) | 2204.14271 [S]; 1809.11171, 2608.29963, 2311.12790, 2505.20436 [S Abstract] |
| Kaehler-Dirac/reduziert gestaffelt + SMG | "may be capable of yielding free Weyl fermions"; Numerik 2D | Vorschlag | nicht behandelt | Catterall 2010.02290 [S Abstract] |
| Disentangler, Rotoren (Hamilton) | 3450 in 1+1D exakt loesbar | U(1) mit Platte, SM-Hyperladung "argued" | "non-abelian": 0 Treffer im Text | TPF 2601.04304v2 [S] |
| Bosonisierung | 2D abelsch exakt (Seifnashri), 2D nichtabelsch (Onoda: Kontinuumslimes "open problem") | chirale Symmetrie aus Bosonen (Lu u. a.), nicht Fermionen | 2D | 2601.14359, 2606.12358, 2604.06307 [S Abstract] |

### 4.3 Lokale bosonische Netze

- Levin/Wen (hep-th/0507118v2, lokale Kopie [S]): Rotor-Modell auf kubischem Gitter mit masselosen Photonen und
  masselosen Dirac-Fermionen; "part of a much more general construction [5] that can produce gauge bosons with any
  gauge group" (Z. 1417-1424); "we can produce photons, gluons, leptons and quarks, but we do not know how to produce
  neutrinos or SU (2) gauge bosons ... we do not know how to obtain chiral fermions and chiral gauge theories from any
  local lattice model, much less a local bosonic model" (Z. 1433-1444). Masse ohne Feinabstimmung, "when bosonic
  models contain emergent non-Abelian gauge bosons" (Z. 1385-1389).
- Wang/Wen 2018/2020 [S Abstract]: Vorschlag ueber Kobordismus-Klassifikation und symmetrische gappe Raender; SM
  aus 16n-SO(10) ueber ein lokales Bosonen- bzw. Qubit-Gitter in 3+1D. Keine Rechnung im Abstract.
- 2026 [S Abstract, S]: Bosonen als Werkzeug (V1); nur 1+1D exakt; 3+1D abelsch.

### 4.4 Kausalmengen

- Chiral: nichts (F8). Spinoren: Sverdlov 2008, Noldus 2013, Gudder 2015 mit Zusatzstruktur; kein lokaler
  Tangentialraum (Surya 2019) [P, SPIN-KAUSAL-L].
- Eichfelder: Sverdlov 2008 SU(n) ueber Holonomien je Punktpaar, alternativ Kaluza-Klein-artig; Sverdlov/Bombelli
  2009 "Yang-Mills gauge fields" [S Abstract]. Keine Rechnung dazu gefunden.

## 5. Regime und Moderatoren

Die Literatur wirkt widerspruechlich ("NN verbietet" gegen "chirales Gitter gebaut"). Sie hat verschiedene Regime
gesampelt; keine Seite irrt [ES]:

| Moderator | Regime 1 (NN gilt) | Regime 2 (NN umgangen) | Quelle |
|---|---|---|---|
| **Lokalitaet** (Leitung: lokal/nichtlokal) | lokal | nichtlokal: SLAC (Eichung leidet), Kontinuum-nichtlokal, Kausalmenge (formal) | Kaplan [S]; 2607.05485, 2607.09935 [S Abstract] |
| **Kopplung** (Leitung: schwach/stark) | frei/schwach | stark (SMG); laut Golterman/Shamir auch dort vektorartig, *wenn* Nullstellen kinematisch sind und ihre Bedingungen gelten | 2505.20436 [S Abstract] |
| Ort der Symmetrie | on-site | nicht on-site (GW, Disentangler, Bosonen) | TPF [S] |
| Zeit | statisch | periodisch getrieben, QCA | 2602.11935 [S Abstract] |
| Dimension | 3+1D: nur Vorschlaege | 1+1D: exakt geloest | 2505.20436 [S Abstract]; Abschn. 4.2 |
| Gruppe | nichtabelsch: offen | abelsch: Luescher 1999 [L]; TPF U(1) in 1+1D gebaut, in 3+1D mit Platte vorgeschlagen | Kaplan Literaturliste [S Titel]; TPF [S] |

**Kopplungsgroesse (Regel 6) [ES]:** Sechs verschiedene Wege fuehren zu Chiralitaet ohne Doppler. Keiner ist "die
Loesung"; gemeinsam ist die Frage, **wo die 't-Hooft-Anomalie sitzt**: im Volumen einer Extra-Dimension, in einer
nicht-on-site-Symmetrie, in nichtlokalen Operatoren, in der Quasienergie-Windung oder in stark gekoppelten Spiegeln.
Liu 2026 und TPF Z. 127-128 sagen das von der Gitterseite. Deshalb vergleicht Abschn. 7 die Kandidaten danach und
nicht nach dem Fermion-Bauteil.

## 6. Unterscheidungspunkte

| Paar | Wo sie messbar auseinanderlaufen | Zugaenglich? |
|---|---|---|
| SMG gegen Golterman/Shamir | 4D mit dynamischem Eichfeld: Vorzeichen des Ein-Schleifen-Beitrags zur Beta-Funktion (Nullstelle gegen Pol), Unitaritaet; 2D abelsch: negativer Beitrag zum Photon-Massenquadrat [S Abstract 2311.12790] | 2D ja; 4D von niemandem gerechnet [ES] |
| Floquet/QCA gegen statisch | Netto-Chiralitaet je Quasienergie-Sektor (Windungszahl W3 von U(k)) | ja, klein (Kartenvorschlag) |
| K-A gegen K-M (chiral) | reale diskrete Zeit mit unitaerem Schritt (K-A als QCA: W3 kann ungleich 0 sein) gegen euklidisches Pfadintegral (K-M: NN in Kaplans Form) [ES] | nur die K-A-Seite klein pruefbar |
| K-B gegen lokale Netze | Hat ein nichtlokaler Dirac-Operator auf einer Kausalmenge Doppler, und haelt die Ward-Identitaet mit Eichfeld? | nein: kein 3+1D-Dirac-Operator auf Kausalmengen [P] |
| Wang/Wen gegen No-go | 3+1D-SMG-Modell mit 16 Weyl und dynamischer Eichung: masselose Spektren beider Chiralitaeten | praktisch nein (Vorzeichenproblem, Kaplan Z. 2340-2342 [S]) |

## 7. Projektbezug je Kandidat

Leitfrage je Kandidat: **Wo koennte die Anomalie sitzen, und was muss dafuer dazukommen?** Ueberall zusaetzlich
noetig: innere Fermion-Zustaende (16 Weyl je Generation bzw. 15, V6), nichtabelsche Eichgruppe, drei Generationen
(L11, ausser Reichweite).

| | K-A Finns Pfeil-Eis-Netz (lokal, festes Netz, aeussere Uhr; QCA) | K-B Kausalmenge (nichtlokal, ohne Ruhesystem) | K-M Regge-Gitter in Raum und Zeit (lokal) |
|---|---|---|---|
| Gilt NN? | ja, in der Hamilton-Form voll fuer freie Fermionen [ES]; im Projekt bestaetigt: Doppler, vektorartige Masse (QCA-TETRA-1, QCA-BCC-RUECK-1, QCA-DIRAC-T-1) [P]. Als QCA nicht in derselben Form (V4) | NN-Annahme Lokalitaet faellt (unendliche Valenz [P]); keine Brillouin-Zone. Der Anomalie-Satz gilt trotzdem: endlich viele Freiheitsgrade je Volumen [ES aus Kaplan Z. 1323-1327] | ja, in Kaplans euklidischer Form bzw. als Anomalie-Satz auf unregelmaessigen Komplexen [ES]; Zufallsgitter helfen nicht sicher (E5) |
| Ort der Anomalie, moeglich | (a) Platte in einer 4. Raumrichtung (Domain-Wall, TPF); (b) stark gekoppelter Spiegelsektor (SMG); (c) nicht-on-site-Symmetrie mit Disentangler, wohl mit Rotoren statt Pfeilen [H]; (d) Quasienergie-Windung der QCA | Nichtlokalitaet [H]; sonst unbekannt (Platte ohne Randbegriff unklar [H]) | (a) 5. Dimension (Simplizialplatte); (b) Kaehler-Dirac/gestaffelt plus SMG (Catterall); (c) Overlap auf dem Komplex [L?] |
| Nichtabelsch | Pfeil-Eis gibt U(1); nichtabelsch braucht String-Netz-Marken einer nichtabelschen Gruppe (Levin/Wen: behauptet, nicht gebaut) [S/ES] | Holonomie je Punktpaar (Sverdlov 2008, Vorschlag) [S Abstract]; das sind O(N^2) Variablen [ES] | Eichlinks je Kante wie in der Gittereichtheorie: eingesetzt, nicht entstanden [ES] |
| Mindest-Zusatzstruktur [ES] | innere Zustaende (>= 2 je Knoten, TWIST-SPIN-1), ein Anomalie-Ort (a bis d), nichtabelsche Marken; das Tempo-Problem (L1) bleibt unberuehrt | Rahmen bzw. Spin-Struktur je Element, Dirac-Operator, Holonomien je Paar, eine Antwort auf die Anomalie | Fermionen je Simplex (Rahmen je Simplex sind natuerlich [L]), 5. Dimension oder SMG-Wechselwirkung, Eichlinks |
| Klein pruefbar (<= 10 min) | Windung W3 der vorhandenen Automaten (Kartenvorschlag); 1+1D-Spielmodell nach TPF (ja, aber Literatur) | nichts Sinnvolles, solange kein Dirac-Operator existiert | Kaehler-Dirac plus FK-Wechselwirkung in 2D (ja, weitgehend Literatur) |
| Nicht klein pruefbar | SMG in 3+1D; nichtabelsche String-Netze in 3+1D; Eichung chiraler Fermionen | alles Chirale | 4D-SMG; 5D-Platte mit dynamischer Eichung |

**Pruefung der Leitungs-Erwartung "alle drei stossen an dieselbe offene Frage" [ES]: teils.**

- **Gemeinsamer Kern ja:** Nichtabelsche chirale Eichtheorie mit endlich vielen Freiheitsgraden je Volumen in 3+1D ist
  fuer jeden Kandidaten offen, weil der Anomalie-Satz nicht an Lokalitaet haengt.
- **Nicht gleich weit:** K-A und K-M stehen je in einem aktiven Programm mit eigenem Weg. K-A ist das Setting der
  Arbeiten von 2025/26 (Hamilton-Gitter, Bosonen/Rotoren, U(1)) und ist im Projekt als einziger mit unitaerem
  Zeitschritt gerechnet (QCA); ob K-M auf einem lorentzschen Regge-Netz auch so gebaut werden kann, ist offen [H]. K-M hat den
  Kaehler-Dirac-Weg auf Simplizes. K-B steht **vor** der Frage: Ihm fehlt der Dirac-Operator. Sein formaler Vorteil
  ist, dass NNs Lokalitaetsannahme nicht greift; bebaut ist dieser Vorteil nicht.
- **Struktureller Vorteil:** keiner, der das nichtabelsche Problem loest. Der Anschlussvorteil von K-A gilt nur
  abelsch (TPF: U(1)_Y, 3+1D mit Platte), und fuer den DP-Automaten ist die QCA-Option nicht verwirklicht (W3 = 0,
  [M]). Er beruehrt das Tempo- und Ruhesystem-Problem von K-A (Review L1) nicht.

## 8. Gegensweep (Was war so selbstverstaendlich, dass ich es nicht geprueft habe?)

1. **"Unsere QCA-Doppler sind gewoehnliche NN-Paare bei gleicher Energie." Geprueft (Projektdaten, DP 2014 lokal,
   ohne Abruf):** Die Kegel liegen bei zwei Quasienergien: A^+ hat Gamma und P' bei W = +I, P und H bei W = -I
   (QCA-TETRA-1, Tabelle QT3 [P]). Mit DP Gl. (27)-(28) [S, lokale Kopie Z. 560-609] ist A^+ = R_z(c) R_y(-b) R_x(a),
   R_j(t) = exp(-i sigma_j t), a = k_x/√3 usw. [M]. Probe an der Tabelle: P -> -I, H -> -I, P' -> +I, stimmt.
   Jacobi-Determinanten: Gamma -1, P' +1. Der Wuerfel [0, 2pi)^3 ueberdeckt die Zone vierfach, Abbildungsgrad 0.
   **Gamma und P' sind also bei Quasienergie 0 ein Paar entgegengesetzter Chiralitaet [M, nicht gegengelesen].** Die
   Selbstverstaendlichkeit haelt fuer den 2-Zustands-Automaten, aber nur durch Rechnung. Mit Inversion ist W3 = 0
   erzwungen [M]; mit der reinen Drehgruppe T nicht. Fuer die 17 Acht-Zustands-Treffer ohne Inversion ist das
   offen: "Die Chiralitaeten der vier Kegel heben sich auf" summiert ueber die vier Kegel bei k = 0 (QCA-BCC-RUECK-1
   Z. 206-207 [P]). Laut Rohdaten liegen diese vier Kegel bei vier verschiedenen Quasienergien (Abschn. 9); die
   Summe ist also keine Aussage je Luecke.
2. **"Bosonisch ist schwerer als fermionisch." Geprueft (F7):** umgekehrt (V1).
3. **"Ein Weltmodell braucht eine nichtperturbative Gitterdefinition des SM."** Kaplan: "we think perturbation theory
   suffices for understanding the Standard Model in the real world" (Z. 2333-2334 [S]). [ES]: Fuer ein Netz als
   Fundament (K-A, K-M; K-B, wenn Fermionen auf der Kausalmenge leben) reicht das nicht; das SM muss als Grenzfall des
   Netzes folgen. Die Luecke L6 ist dort echt.
4. **"Die Doppler muessen weg."** Nicht an Quellen geprueft. [ES/L]: Unter derselben SU(2) x U(1) bekaemen
   Spiegelteilchen Masse nur aus der elektroschwachen Brechung, also hoechstens auf der TeV-Skala, wie eine vierte,
   gespiegelte Generation [L]. Sollen die Doppler als schwere Spiegelteilchen bleiben, geht das ohne Symmetriebruch
   nur ueber eine SMG-artige starke Kopplung bei hoher Skala [ES].
5. **"Finns Pfeile (Spin 1/2 je Kante) tragen dasselbe wie Rotoren."** Nicht geprueft. TPF brauchen "infinite-
   dimensional rotor degrees of freedom" (Z. 165-166 [S]); Liu 2026 bindet NN-artige Saetze an die lokale Dimension
   [S Abstract]. Ob endliche Pfeile reichen, ist offen [H].

## 9. Kartenvorschlag (einer): QCA-WINDUNG-1

- **Frage:** Tragen die vorhandenen T-kovarianten Automaten ohne Inversion eine Netto-Chiralitaet in den
  Quasienergie-Luecken (W3 ungleich 0)? Gemeint sind die 17 Rueck-Treffer aus QCA-BCC-RUECK-1, die Einbahn-Treffer
  aus QCA-DIRAC-T-1 (Formen N, O) und Konstruktion R3.
- **Hintergrund [M, Skizze, nicht gegengelesen; L?]:** Bei einem Floquet- bzw. QCA-Operator U(k) muessen alle Luecken
  zwischen benachbarten Quasienergie-Baendern dieselbe Netto-Chiralitaet chi tragen (die Chern-Zahl eines Bandes auf
  der Ebene k_z = const kehrt nach einem Umlauf in k_z zurueck); chi ist die Windungszahl W3. Statisch ist die
  unterste Luecke nach unten offen, also chi = 0; das ist NN.
- **Messgroessen:** chi_{n,n+1} je Bandpaar aus allen Kegeln der Zone (Vorzeichen der Jacobi-Determinante), nicht nur
  an Gamma, H, P, P'; dazu W3 = (1/24 pi^2) Int tr (U^-1 dU)^3 als Kontrolle (k-Gitter verfeinern, ganzzahlig auf
  1e-3). Ein Lauf auf der Kleintest-Spur.
- **Rohdatenprobe (jq, nur gelesen, qca-bcc-rueck-1/lauf-69/haupt_8Na.json):** Je Treffer stehen bei Gamma vier
  Zweifach-Kegel mit "phase" und "chiral_det". Im ersten nichttrivialen Eintrag liegen sie bei vier verschiedenen
  Phasen (0,551; -0,234; 1,613; -3,117) mit den Vorzeichen +, +, -, - [P]. An H, P, P' stehen nur "phase", "m",
  "typ", "lin_min/max", keine Chiralitaet; Kegel ausserhalb der Hochsymmetriepunkte sind nicht gespeichert. Die
  Antwort steht also nicht in den Daten. Die Schluessel "spruenge" und "A" sind vorhanden, ihr Inhalt ist nicht
  geprueft.
- **Ableitbarkeitsprobe:**
  - 2-Zustands-DP-Automat: **ableitbar**, W3 = 0 [M, Abschn. 8 Punkt 1] -> nur Kontrolle, kein Ergebnis.
  - Automaten mit Inversion: **ableitbar**, W3 = 0 [M] -> Kontrolle.
  - Konstruktion R3 (Hin- und Rueck-Sektor): vorab am Schreibtisch versuchen (Rueck-Sektor als gespiegelter
    Hin-Sektor); gelingt das, nur Kontrolle.
  - 17 Such-Treffer ohne Inversion: **nicht ableitbar.** T verbietet W3 ungleich 0 nicht, und die vorhandene
    Kennzahl mischt die Sektoren. Nur dafuer lohnt die Rechnung.
- **Scheitern und Bestehen moeglich:** W3 = 0 bei allen: Der Floquet-Weg ist in unseren Automaten nicht
  verwirklicht; dann bleibt K-A auf (a) bis (c). W3 ungleich 0 bei einem: erste netto-chirale Fermion-Regel im
  Projekt, die Gegenhaendigkeit sitzt bei Quasienergie pi (Planck-Energie). Die Folgefrage waere dann die Eichkopplung
  (Anomalie pumpt zwischen den Sektoren [H]).
- **Grenzen:** Ein-Teilchen-Bild. Sagt nichts zu Eichung, nichtabelscher Gruppe, SM oder Messdaten.

## 10. Kalibrierung

- **(a) Gemessen:** nichts in dieser Karte. In der Literatur gerechnet: SMG in 1+1D und Domain-Wall-SMG in 2D;
  vektorartige 3+1D-SMG-Spielmodelle. Im Projekt gerechnet: QCA-Doppler und Kegelpunkte, das raue Band.
- **(b) Nuetzlich verdichtet:** "Wo sitzt die Anomalie?" als gemeinsame Groesse; die Moderatoren-Tabelle; die
  Kandidaten-Tabelle; der Abbildungsgrad 0 des DP-Automaten [M, ungegengelesen].
- **(c) Gewachsene Gewissheit ohne neue Evidenz (Warnzeichen):** Waehrend der Recherche wuchs mein Eindruck, K-A habe
  einen "Anschlussvorteil", waehrend die Frage zerfiel (abelsch gegen nichtabelsch, 1+1D gegen 3+1D, mit oder ohne
  Platte). Belegt ist nur, dass die neuen Arbeiten im Hamilton-Setting stehen; dass sie fuer SU(2) tragen, ist von
  niemandem gezeigt. Die meisten Arbeiten von 2025/26 kenne ich nur als Abstract; Woerter wie "argue", "propose",
  "plausibly" sind die der Autoren.

## 11. Offene Fragen

- O1: Ist Golterman/Shamirs verallgemeinertes No-go auf Wang/Wen und auf TPF anwendbar? (nur Abstracts gelesen)
- O2: Kaplans eigene neuere Arbeit ("Kap24" bei TPF) und Kaplan/Sen 2023: Inhalt nicht gelesen (F6 Fehlabruf).
- O3: Reichen Finns endlich-dimensionale Pfeile fuer nicht-on-site-Konstruktionen, oder braucht es Rotoren? [H]
- O4: Gibt es auf Kausalmengen einen Ort fuer die Anomalie (Nichtlokalitaet als "Volumen")? Keine Quelle gefunden.
- O5: Wie verhalten sich Floquet-chirale Fermionen (W3 ungleich 0) bei Eichkopplung, und koennte anomaliefreier
  SM-Inhalt dort ohne Spiegel auskommen? Keine Quelle gelesen [H].

## 12. Selbstanzeigen

1. **Zeitangaben geschaetzt:** In ARBEITSFELD.md standen zuerst vier geschaetzte Uhrzeiten, zwei davon in der
   Zukunft ("14:37", "14:38" vor der Messung 14:36:37); drei Erwartungsbloecke trugen geschaetzte Zeiten nach dem
   Abrufbeginn ("14:25" bei Abruf 14:24:25, "14:27" bei 14:26:14, "14:30" bei 14:29:30). Berichtigt auf date-Grenzen.
   Die Reihenfolge Erwartung vor Abruf ist im Ablauf eingehalten; die alten Etiketten waren falsch.
2. **F6 Fehlabruf:** arXiv-Nummer fuer Kaplan/Sen aus dem Gedaechtnis, falsch (fachfremde Arbeit).
3. **F7/F8 zuerst ohne Inhalt:** http statt https, 0 Byte; als zwei Abrufe mitgezaehlt, dann per https wiederholt.
4. **Nur Abstracts:** Die meisten Quellen von 2025/26 (Abschn. 4.2) nur als API-Abstract; Volltext gelesen nur
   Kaplan 2012, Wang/You 2022 (Ausschnitte), Bakircioglu u. a. (Abschn. 6.2), TPF (Einleitung).
5. **Eigene Algebra [M]:** Faktorisierung des DP-Automaten und Abbildungsgrad 0 nicht gegengelesen; die Probe an
   der TETRA-1-Tabelle stuetzt sie. Erste Kopfrechnung mit falscher Faktorreihenfolge; relative Vorzeichen gleich.
   Die Floquet-Aussage "alle Luecken tragen dieselbe Netto-Chiralitaet W3" ist meine Skizze, an keiner Quelle
   gelesen.
6. **Zeilennummern:** Kaplan-Zeilen im ARBEITSFELD zuerst aus dem Gedaechtnis der grep-Ausgabe; im
   Rueckwaertsdurchgang per grep berichtigt, dazu TPF (129-133 -> 127-128; 176-191 -> 170-191), Bakircioglu u. a.
   (2160-2229 -> 2141-2252; Fussnote 17 -> 2122-2125) und Levin/Wen (1418/1436 -> 1417/1433). Im selben Durchgang zu
   starke Stellen abgeschwaecht: "Golterman/Shamir zeigen" -> "finden in einem effektiven Lagrange-Ansatz"; "TPF U(1)
   gebaut" -> "1+1D gebaut, 3+1D vorgeschlagen"; "es bleibt nur SMG" -> nur fuer Doppler als schwere Spiegelteilchen;
   V6 mit dem B-L-Satz der Quelle statt meiner Umschreibung.
7. **Ersatz fuer Regel 7:** Die 24-Monats-Pruefung war eine arXiv-API-Abfrage mit vier Phrasen, keine Websuche;
   Arbeiten ohne diese Phrasen im Abstract fehlen.
8. **Lokale Fremdkopie:** DP 2014 aus qca-tetra-1/quelle/ per pdftotext in meinen quellen/-Ordner extrahiert (kein
   Abruf).
9. **Fremder Laufordner:** In qca-bcc-rueck-1/lauf-69/ per jq nur gelesen (Schluessel und drei Eintraege, Abschn. 9);
   nichts geschrieben. Das ist Datenlesen, keine Rechnung; die Vorzeichen +, +, -, - sind abgelesen, nicht
   ausgewertet.

## 13. Quellenliste (Abrufstand 2026-10-04)

**Abgerufen (lokale Kopien in quellen/):**

- D. B. Kaplan, "Chiral Symmetry and Lattice Fermions", Les-Houches-Vorlesung, arXiv:0912.2560v2 (18.01.2012).
  https://arxiv.org/abs/0912.2560 - F1, 14:24:25, PDF, Abschn. 3.1 und 4.3 gelesen [S]
- J. Wang, Y.-Z. You, "Symmetric Mass Generation", arXiv:2204.14271v1 (29.04.2022). https://arxiv.org/abs/2204.14271 -
  F2, 14:24:25, PDF, Einleitung, SM-Abschnitt, Tab. II, Schluss [S]
- M. Golterman, Y. Shamir, "Propagator zeros and lattice chiral gauge theories", arXiv:2311.12790v2 (13.02.2024).
  https://arxiv.org/abs/2311.12790 - F3, 14:24:25 [S Abstract]
- J. Wang, X.-G. Wen, "A Non-Perturbative Definition of the Standard Models", arXiv:1809.11171v3 (03.04.2020).
  https://arxiv.org/abs/1809.11171 - F4, 14:24:25 [S Abstract]
- S. Catterall, "Chiral Lattice Fermions From Staggered Fields", arXiv:2010.02290v4 (15.06.2021); PRD 104, 014503
  (2021) laut Wang/You. https://arxiv.org/abs/2010.02290 - F5, 14:26:14 [S Abstract]
- F6 arXiv:2312.04501 (14:26:14): fachfremd (Lim u. a., Graph Metanetworks), nicht verwendet; Datei quellen/FEHLABRUF-2312.04501-fachfremd-abs.html
- F7/F7b arXiv-API, Abstract-Phrasen "chiral gauge", "symmetric mass generation", "Nielsen-Ninomiya", "mirror
  fermions", eingereicht 2024-10-04 bis 2026-10-04, 84 Treffer (14:26:31). Daraus [S Abstract]:
  - R. Thorngren, J. Preskill, L. Fidkowski, "Chiral Lattice Gauge Theories from Symmetry Disentanglers",
    arXiv:2601.04304 (Volltext F12)
  - Z. Lu, S. Seifnashri, S.-H. Shao, "Lattice chiral symmetry from bosons in 3+1d", arXiv:2604.06307; PRD 114,
    034518 (2026)
  - S. U. Baig, S. Chen, A. Cherman, M. Neuzil, "Bosonization versus the Nielsen-Ninomiya theorem", arXiv:2607.09935
  - S. Seifnashri, "Exactly Solvable 1+1d Chiral Lattice Gauge Theories", arXiv:2601.14359
  - S. Onoda, "Lattice chiral non-Abelian gauge symmetry via bosonization", arXiv:2606.12358
  - M. Golterman, Y. Shamir, "Constraints on the symmetric mass generation paradigm for lattice chiral gauge
    theories", arXiv:2505.20436v3; "Symmetric mass generation and the Nielsen-Ninomiya theorem", arXiv:2603.15985
  - S. Araki, H. Fukaya, T. Onogi, S. Yamaguchi, "Symmetric Mass Generation for Domain-Wall Fermions",
    arXiv:2608.29963
  - D. B. Kaplan, S. Sen, "Regulated chiral gauge theory and the strong CP problem", arXiv:2412.02024
  - J. D. Kroth, S. Sen, "Unpaired Weyl fermion on an axion string in a finite lattice", arXiv:2506.04324
  - J. Dang, R. Karur, S. Sen, "Gauge field flow for chiral gauge theories on a slab", arXiv:2606.05306
  - X.-D. Lin, J. Zhang, L. Zhang, "Proposal for realizing unpaired Weyl points in a three-dimensional periodically
    driven optical Raman lattice", arXiv:2602.11935; PRA 113, 063303 (2026)
  - D. Bakircioglu, P. Arnault, P. Arrighi, "Fermion Doubling in Quantum Cellular Automata", arXiv:2505.07900v3
    (Volltext F11)
  - A. Kouroshnia, J. W. Moffat, E. J. Thompson, "An inquiry into the Absence of Fermion Doubling and why the
    Nielsen-Ninomiya Theorem Does Not Apply to Nonlocal Quantum Field Theory", arXiv:2607.05485v5
  - R. Liu, "Anomalies in quantum spin systems and Nielsen-Ninomiya type Theorems", arXiv:2602.13948
  - C.-T. Ma, H. Zhang, "Lattice Chiral Fermion without Hermiticity", arXiv:2411.09886
- F8/F8b arXiv-API, Abstract "causal set" und (gauge, fermion(s), Dirac, chiral, spinor, Yang-Mills), alle Jahre,
  25 Treffer (14:26:36). Daraus [S Abstract]: R. Sverdlov, "Gauge Fields in Causal Set Theory", arXiv:0807.2066
  (2008); R. Sverdlov, L. Bombelli, "Dynamics for causal sets with matter fields: A Lagrangian-based approach",
  arXiv:0905.1506 (2009)
- D. Bakircioglu, P. Arnault, P. Arrighi, arXiv:2505.07900v3 (17.01.2026). https://arxiv.org/abs/2505.07900 - F11,
  14:29:30, PDF, Abschn. 6.2 gelesen [S]
- R. Thorngren, J. Preskill, L. Fidkowski, arXiv:2601.04304v2 (12.06.2026). https://arxiv.org/abs/2601.04304 - F12,
  14:29:30, PDF, Einleitung und Abschn. 1.1 gelesen [S]

**Lokal im Projekt, ohne Abruf:**

- M. Levin, X.-G. Wen, "Quantum ether: photons and electrons from a rotor model", hep-th/0507118v2 (13.02.2007),
  RUNDE-37/twist-pyro-1/quellen/arxiv-hep-th-0507118.txt, Z. 1376-1476 [S]
- G. M. D'Ariano, P. Perinotti, "Derivation of the Dirac equation from principles of information processing",
  arXiv:1306.1934v2 (PRA 90, 062106 (2014)), RUNDE-37/qca-tetra-1/quelle/, Text nach
  quellen/lokal-dariano-perinotti-1306.1934v2.txt, Gl. (27)-(29), Z. 548-612 [S]
- Projektdateien [P]: RUNDE-37/weltmodell-review-1/REVIEW.md (Abschn. 3 bis 5, L6); RUNDE-40/WEICHE-STAND-v5.md;
  RUNDE-37/{qca-bcc-rueck-1, qca-dirac-t-1, qca-tetra-1, spin-zufallsnetz-1, twist-spin-1, induziert-wilson-2d}/
  ERGEBNIS.md; RUNDE-37/spin-kausal-l/DOSSIER.md; RUNDE-39.md Z. 312; RUNDE-40.md Z. 205;
  RUNDE-06/M-THEORIE-CALABI-YAU.md Z. 196 (Acharya/Witten: chirale Fermionen aus konischen Singularitaeten)

## Einfach gesagt

Die Natur behandelt links- und rechtsdrehende Teilchen verschieden, und genau das kann man auf einem gewoehnlichen
Gitter nicht nachbauen: Zu jedem linksdrehenden Teilchen erscheint ungewollt ein rechtsdrehendes Spiegelbild. Die
Forschung kennt Tricks, um diese Spiegelbilder loszuwerden, etwa eine zusaetzliche Raumrichtung, sehr starke Kraefte
zwischen den Spiegelbildern oder Bausteine, die selbst keine Fermionen sind. Fuer die einfache elektrische Ladung
klappt das teilweise, fuer die Kraefte des Standardmodells mit mehreren Ladungsarten aber noch nirgends. Unsere drei
Weltmodell-Kandidaten haben dieses Problem alle; Finns Netz und das Raumzeit-Gitter haben je einen Ansatzpunkt aus der
Forschung, die Kausalmenge muss zuerst ueberhaupt Teilchen mit halbem Spin tragen koennen.
