# LADUNG-MONOPOL-L: Dossier (Literaturkarte, Runde 37)

- Feldforscher fuer die Leitung claude-primary. Start 2026-10-04 05:31:18 CEST, Dossier geschrieben ab 05:53:23 CEST,
  berichtigt ab 05:58:08 CEST nach Gegensweep G7 (alle Zeiten per date). Arbeitsstand und Abrufprotokoll:
  ARBEITSFELD.md (gleicher Ordner).
- 15 von 15 WebFetch-Abrufen verbraucht, keine Websuche, keine Rechnung, lokal kein Interpreter.
- **Kennzeichen:**
  - [S] an der Quelle gelesen (Abstract bzw. Werkzeugauszug aus dem Volltext); [S?] Quelle gelesen, Fundstelle unsicher
  - [P] Projektdatei gelesen
  - [L] Literatur aus dem Gedaechtnis; [L?] unsicher
  - [ES] eigener Schluss; [H] Hypothese

## 1. Ergebnis zuerst

0. **Das Projekt hatte den Q-Ball-Teil von H2 schon** [P].
   - RUNDE-09/spin1/SPIN1.md vom 30.09.2026, "Weg B (Ladung plus Monopol)", zusammengefasst in RUNDE-10.md Z. 300
     bis 330.
   - Dort stehen schon: Q/2-Regel, Bai/Lu/Orlofsky, "binden ohne Zusatzpotential nicht", PDG-Drehimpulsformel.
   - SPIN-1 wurde dort geparkt (RUNDE-10.md Z. 552).
   - Neu ist hier der Eis-Teil: Woerterbuch, Regime, 2+1-D-Abschirmung, Kato-Strenge, Gitterkarte.
1. **Ladung + Monopol = Fermion aus zwei Bosonen ist Literatur** [S].
   - Goldhaber 1976: spinlose Ladung + spinloser Monopol "may bear net half-integer spin"; dazu der uebliche
     Spin-Statistik-Zusammenhang.
   - Hasenfratz/'t Hooft 1976 und Jackiw/Rebbi 1976 zeigen dasselbe in der nicht-abelschen Fassung.
   - Im Festkoerper: Metlitski/Kane/Fisher 2013, "statistical Witten effect".
2. **In Finns Netz fehlt der Partner** [P, S, ES].
   - Die FLUSS-1-Defekte sind Quellen des Pfeilfeldes. Sie entsprechen strukturell den "Monopolen" von
     Castelnovo/Moessner/Sondhi und zugleich der "electric gauge charge" von Hermele/Fisher/Balents, dort aber auf
     einem anderen Gitter: eine Sorte mit zwei Namen.
   - Der Q-Ball ist laut QBALL-LADUNG-1-Karte dieselbe Sorte.
   - Den eigentlichen Monopol (topologischer Defekt des konjugierten, kompakten Feldes) gibt es erst im Quanten-Eis.
     Das klassische Eis von FLUSS-1 hat ihn nicht.
3. **Ein Q-Ball ist der falsche Partner fuer Spin 1/2** [ES, deckt sich mit SPIN1.md B-V3, also nicht neu].
   - Mit kleinster Dirac-Bedingung liegt sein Drehimpuls in Q/2 + ganze Zahl. Er ist ein Fermion nur bei
     ungeradem Q.
   - Spin 1/2 gibt nur die Einheitsladung (Q = 1).
   - Ueber das Eichfeld allein haftet er nicht; das ist vorab ableitbar (Kato-Ungleichung).
   - Haftung braucht eine Zusatzkopplung, wie im "Q-Monopole-Ball" von Bai/Lu/Orlofsky 2022 [S]; dort ist der Ball
     aber neutral und darum bosonisch.
4. **Vorschlag:** Rechenkarte LADUNG-MONOPOL-1 (Abschnitt 9). Ein spinloses Teilchen der Ladung q auf einem
   kubischen Gitter um einen Gitter-Monopol: Bei q = 1 sollte die tiefste gebundene Stufe ein Dublett sein, bei q = 2
   ein Triplett. Die Projektiv-Kontrollen sind vorab ableitbar, die Gitterstufen nicht.

## 2. Erwartungsverstoesse (das Wichtigste zuerst)

0. **Gegensweep G7: Die Karte war im Q-Ball-Teil schon beantwortet** [P].
   - RUNDE-09/spin1/SPIN1.md (30.09.2026) hatte zu "Weg B":
     - Bai/Lu/Orlofsky gelesen und als Verletzung der eigenen Erwartung verbucht
     - B-V3: Felddrehimpuls Q/2, Fermion nur bei ungeradem Q
     - B-V2: ohne Zusatzpotential keine Bindung
     - E10c: PDG 2025, Rev. 94, Gl. (94.3), Drehimpuls mit Term -(1/4 pi) Q_E Q_M r-hat
     - E11: 0 Treffer fuer "gauged Q-ball" AND monopole (Metadatensuche)
   - Die Karten-Erwartung E4 ("nicht beschrieben") war damit seit 30.09. im Projekt verletzt.
   - Meine Punkte 1 und 6 unten sind fuer das Projekt nicht neu, sondern eine unabhaengige Bestaetigung.
   - Selbstanzeige: Mein grep um 05:35 hatte die Treffer, ich habe sie erst im Gegensweep gelesen.
1. **E4, Abruf A8/A14: Ein an Monopolen haftender Q-Ball ist beschrieben** [S; fuer das Projekt nicht neu, siehe 0].
   - Quelle: Bai/Lu/Orlofsky, JHEP 01 (2022) 109, arXiv:2111.10360.
   - Die Haftung kommt aus einer "portal coupling" (1/2 lambda_phiS |S|^2 phi^a phi^a, Gl. 2): S wird im Monopolkern
     leichter (Abschn. 2.3).
   - Das Objekt ist "more stable than an isolated Q-ball" [S].
   - S ist Eich-Singulett. Spin und Statistik werden nicht behandelt [S, Werkzeugauszug].
   - Korrektur: Die Haftung gibt es, aber nur ueber eine Zusatzkraft. Das stuetzt E5. Ein *geeichter*
     Q-Monopol-Ball mit Feld-Drehimpuls wurde nicht gefunden; ohne Suche ist das nicht pruefbar.
2. **E2, Abrufe A9/A15: Die Klassifikation ordnet nach E und M, nicht nach dem Dyon; schon das Pyrochlor-Eis hat
   zwei Kandidaten-Regime** [S, S?].
   - Wang/Senthil, Tabelle I, sieben Familien:
     - theta = 0: E_b M_b, E_bT M_b, E_f M_b, E_fT M_b, E_b M_f, E_bT M_f
     - theta = pi: (E_fT M_f)_theta
   - Abschn. III.B: in strikt 3D-bosonischen Systemen "E and M cannot simultaneously be fermionic" [S].
   - Abschn. II (9): Pyrochlor-Eis mit Kramers-Dubletts entweder E_b M_b (Eich-Mittelfeld) oder (E_fT M_f)_theta
     (Partonen) [S?, nur Zusammenfassung].
   - Einen ausdruecklichen Satz "E_b und M_b gebunden ergeben ein Fermion" fand das Werkzeug nicht. Es las den Text
     aber nur bis Abschn. IV (Gegensweep G5). Urteil: im gelesenen Teil nicht belegt, nicht "fehlt".
3. **E3, Abruf A11: Die Benennung ist in der Literatur nicht einheitlich** [S].
   - Benton/Sikora/Shannon 2012 nennen Spin-Eis "a beautiful realisation of classical magnetostatics, complete with
     magnetic monopole excitations". Die Photonen sind dort "magnetic excitations".
   - Hermele/Fisher/Balents 2004 nennen dieselben Defekte "spinons carrying the U(1) 'electric' gauge charge".
   - Folge: Das Woerterbuch muss strukturell definiert werden, nicht ueber die Namen (Abschnitt 5).
4. **A10: Der statistische Witten-Effekt kommt ohne gebundenes Ladungsteilchen aus** [S].
   - MKF 2013: Ein Monopol im bosonischen topologischen Isolator "can remain electrically neutral", seine Statistik
     werde "transmuted from bosonic to fermionic".
   - Die Ladung liefert das Medium. Das ist ein dritter Weg zum selben Fermion (Regel 6, Abschnitt 6).
5. **A1: Die Kandidatennummer arXiv:1505.05141 ist falsch** [S].
   - Sie gehoert zu Wang/Senthil, "Dual Dirac liquid on the surface of the electron topological insulator",
     PRX 5, 041031 (2015).
   - Die gemeinte Arbeit ist PRX 6, 011034 (2016); geholt ueber die DOI.
6. **Schreibtisch gegen die Leitidee (keine Quelle verletzt, sondern die stillschweigende Annahme in E4)** [ES]:
   - "Q-Ball haftet und wird dadurch fermionisch" gilt nur fuer ungerades Q.
   - Die Erwartung "Spin 1/2" gilt nur fuer Q = 1 (Abschnitt 9, D1).
   - Das stand schon in SPIN1.md B-V3 [P].

## 3. Erwartungen mit Ausgang

| Nr | Erwartung (Karte, vor jedem Abruf) | Ausgang | Fundstelle |
|---|---|---|---|
| E1 | Spinlose Ladung + spinloser Monopol mit q g/(4 pi) = 1/2: halbzahliger Drehimpuls, Fermi-Statistik | **eingetroffen** | Goldhaber, PRL 36, 1122 (1976), Abstract [S]: "may bear net half-integer spin", "implies the usual connection between spin and statistics". Hasenfratz/'t Hooft, PRL 36, 1119, Abstract [S]: halbzahliger Isospin gibt halbzahligen Gesamtdrehimpuls, "fermions ... in a theory that started off with bosons only". Jackiw/Rebbi, PRL 36, 1116 [S]: "isospinor degrees of freedom are converted into spin degrees of freedom" (nicht-abelsche Fassung, nicht der spinlose Einzelfall) |
| E2 | In U(1)-Quanten-Spinfluessigkeiten ist das Dyon aus bosonischer Ladung und bosonischem Monopol ein Fermion; Phasen nach Statistik von e, m und Dyon geordnet | **teilweise** | Wang/Senthil, PRX 6, 011034 (2016) [S]: "seven families ... distinguished by the properties of their emergent electric or magnetic charges"; Tabelle I. Ordnung nach E und M (Statistik, Kramers, theta), nicht nach dem Dyon. Dyon-Fermion-Satz im gelesenen Teil (bis Abschn. IV) nicht gefunden; er folgt aus Goldhaber [S] plus Kuerzel-Logik [ES] |
| E3 | CMS-"Monopole" sind in der emergenten Elektrodynamik elektrische Ladungen; die emergenten Monopole sind eigene Anregungen | **teilweise** | Struktur eingetroffen: HFB, PRB 69, 064404 (2004), Abstract [S]: Spinonen tragen die "electric" Ladung, dazu "a gapped topological point defect or 'magnetic' monopole". Wortlaut nicht allgemein: BSS, PRB 86, 075154 (2012) [S] behalten "magnetic monopole" fuer die Eisdefekte |
| E4 | Q-Ball am Monopol, dadurch fermionisch: nicht beschrieben; dyonische Q-Baelle koennte es geben | **teilweise** | Haftung beschrieben: Bai/Lu/Orlofsky, JHEP 01 (2022) 109 [S], ueber Portal-Kopplung, Ball neutral, Spin/Statistik nicht behandelt; im Projekt seit 30.09. bekannt (SPIN1.md E5) [P]. "Fermionisch durch Haftung": nicht gefunden; Projekt-Metadatensuche "gauged Q-ball" AND monopole: 0 Treffer (SPIN1.md E11) [P]. Fermionisch nur fuer ungerades Q (SPIN1.md B-V3 [P]; hier unabhaengig D1 [ES]) |
| E5 | Ruhende Ladung und Monopol ohne Coulomb-Kraft; Bindung braucht Zusatzkraft; Drehimpuls unabhaengig vom Abstand (Thomson) | **eingetroffen** | Kraftfreiheit: Lorentz-Kraft und Energiedichte ohne Kreuzterm [ES, L]. Zusatzkraft: BLO-Portal [S]; SPIN1.md B-V2 [P]; Kato-Ungleichung (D3) [ES]. Abstandsunabhaengigkeit: PDG 2025, Rev. 94, Gl. (94.3), Term -(1/4 pi) Q_E Q_M r-hat ohne Abstand (im Projekt gelesen, SPIN1.md E10c) [P]; Dimensionsanalyse [ES]; Thomson 1904 [L] |

## 4. Literaturstand (kurz)

- **Ladung-Monopol-Komposite (Hochenergie, 1976)** [S]:
  - Drei aufeinanderfolgende PRL in Band 36, alle vom 10. Mai 1976 (Seiten 1116, 1119, 1122).
  - Halbzahliger Drehimpuls aus Bosonen im Monopolfeld; Goldhaber zeigt, dass die Relativbewegung zweier Komposite
    die uebliche Spin-Statistik-Verbindung ergibt.
- **U(1)-Spinfluessigkeiten (Festkoerper)** [S]:
  - HFB 2004: Das S = 1/2-Pyrochlor-Modell mit starker Achsenanisotropie hat eine U(1)-Phase mit Photon, gapped
    Spinonen (elektrisch) und gapped Monopolen. Diese Phase sei "stable to ALL zero-temperature perturbations".
  - Wang/Senthil 2016: sieben Familien zeitumkehrsymmetrischer U(1)-Fluessigkeiten. Pyrochlor-Kandidaten: E_b M_b
    oder (E_fT M_f)_theta [S?].
  - In (E_fT M_f)_theta sind die Grundteilchen Dyonen mit (q_e, q_m) = (+-1/2, +-1) [S, Abschn. II].
  - MKF 2013: Ein neutraler Monopol wird im bosonischen topologischen Isolator zum Fermion [S].
- **Gitter-Monopole** [S]: DeGrand/Toussaint 1980:
  - "operational definition of a monopole" im kompakten Gitter-U(1).
  - In 3 Dimensionen (2+1) und bei starker Kopplung "monopoles screen external magnetic fields".
  - Schwach gekoppelt in 4D: "massless photon".
  - Die 2-pi-n-Zerlegung der Plakettenwinkel steht nicht im Abstract [L].
- **Q-Baelle und Monopole** [S]: Bai/Lu/Orlofsky 2022, Q-Monopole-Ball mit Portal-Kopplung; bindet sogar
  gleichnamige Monopole; kugelsymmetrische Loesung nur fuer q = 2, fuer q > 2 nicht (Abschn. 3).
- **Stringnetz-Weg** [S]: Levin/Wen 2005, RMP 77, 871: Photonen und Fermionen aus "string-net condensation". Ob die
  Fermionen dort Stringenden oder Dyonen sind, sagt das Abstract nicht.

## 5. Woerterbuch Ladung/Monopol: Spin-Eis gegen unser Netz

Die Namen sind Konvention. Massgeblich ist die Spalte "Struktur".

| Struktur | Klassisches Spin-Eis (CMS 2008; BSS 2012) | Quanten-Spin-Eis (HFB 2004; Wang/Senthil 2016) | Unser Netz (FLUSS-1, QBALL-LADUNG-1) |
|---|---|---|---|
| Groesse auf der Kante | Spin = magnetisches Moment; BSS: "magnetostatics" [S] | S^z = emergentes *elektrisches* Feld [S, HFB] | Pfeil auf Pyrochlor-*Kante* (Grad 6) [P]; nicht das Spin-Eis-Gitter (Pyrochlor-Ecken = Diamant-Kanten) |
| Erhaltungsregel | 2 rein / 2 raus je Tetraeder [L] | Gauss-Gesetz [S, HFB] | 3 rein / 3 raus je Ecke [P] |
| Quelle des Kantenfeldes (Regelverletzung) | "magnetic monopole" [S, CMS, BSS] | "spinon", "electric gauge charge" [S, HFB]; E in Wang/Senthil | "Ladung" q = +-2, zieht mit ~1/r an [P]; der Q-Ball soll dieselbe Sorte sein ("Q-Baelle als elektrische Ladung im Pfeil-Eis", Karte QBALL-LADUNG-1 Z. 6) [P] |
| Konjugiertes kompaktes Feld (Vektorpotential), Fluss auf kleinsten Schleifen | gibt es nicht (klassisch) | entsteht durch Ringaustausch [L]; "lattice version of electric-magnetic duality" [S, HFB] | fehlt (klassisch). Im Quantennetz laege der Fluss auf Dreiecken und Sechsecken [H] |
| Topologischer Punktdefekt dieses Feldes | gibt es nicht | "gapped topological point defect or 'magnetic' monopole" [S, HFB]; M in Wang/Senthil | fehlt. Im Quantennetz saesse er in einer Zelle, also Tetraeder oder abgestumpftes Tetraeder [H] |
| Photon | keines; nur Pinch-Punkte [L] | "gapless photon" [S, HFB]; "ghostly ... magnetic excitations" [S, BSS] | keines; FLUSS-1 zeigt die klassische Coulomb-Phase (1/r, r^-3, Pinch-Fliege) [P] |
| Dyon (Quelle + Defekt gebunden) | gibt es nicht | bei E_b M_b ein Fermion [ES aus Goldhaber S]; in (E_fT M_f)_theta Grundteilchen (+-1/2, +-1) [S] | fehlt. Kandidat: FLUSS-1-Defekt + Monopol des Quantennetzes [H] |
| Q-Ball + Monopol | gibt es nicht | nicht behandelt | Drehimpuls in Q/2 + Z; Fermion nur bei ungeradem Q; keine Haftung ohne Zusatzkopplung [ES] |

- **Falle [ES]:** Wer die CMS-Namen benutzt ("Regelverletzungen verhalten sich wie magnetische Monopole", so auch
  RUNDE-34/TETRAEDER-ANALYSE.md Z. 60 [P]), koennte "geladener Q-Ball + FLUSS-1-Defekt" fuer Ladung + Monopol halten.
  - Beides sind aber Quellen desselben Feldes. Das Paar ist Ladung + Ladung, mit Coulomb-Kraft und ohne
    Thomson-Drehimpuls.
  - Gegenstueck im Projekt: In STRINGENDE-1 war der Zweilagen-Verbund ein Boson (808 von 808), weil Ladung und Fluss
    aus verschiedenen Lagen keine gegenseitige Statistik hatten [P]. Ebenso gibt Ladung aus dem einen U(1) und Monopol
    aus einem anderen keinen Feld-Drehimpuls [ES].

## 6. Regime und Moderatoren (Feld-Regel 1)

| Moderator | Regime A | Regime B | Beleg |
|---|---|---|---|
| Raumdimension | 3+1: Coulomb-Phase mit Photon, Monopole gapped | 2+1: Monopole schirmen ab, kein freies Photon | DeGrand/Toussaint [S]; Polyakov 1977 [L] |
| Klassisch / quanten | klassisches Eis: nur Quellen des Kantenfeldes | Quanten-Eis: Quellen, Monopole, Photon | FLUSS-1 [P]; HFB [S] |
| Phase der U(1)-Fluessigkeit | E_b M_b: reine Ladung Boson, Dyon (1,1) Fermion | E_f M_b oder (E_fT M_f)_theta: reine Ladung selbst Fermion | Wang/Senthil Tabelle I [S]; Dyon-Regel [ES] |
| Ladung des gebundenen Objekts | Q ungerade: Fermion | Q gerade: Boson | Goldhaber [S] + Monopol-Kugelfunktionen [L] -> [ES] |
| Art der Haftung | nur Eichkopplung: nie gebunden | Zusatzkopplung (Portal): gebunden | D3 [ES]; BLO [S] |
| Q-Ball-Groesse gegen Eindringtiefe ~ 1/(e phi_0) | Feld dringt ein, Nullinie | Fluss in einen Schlauch gedraengt (Meissner-artig) | [H]; bei e <= 0,05 (QBALL-LADUNG-1) Eindringtiefe >= 20 |
| Benennung | HFB: Eisdefekt = elektrisch | CMS/BSS: Eisdefekt = magnetisch | [S] beide |

- **Kopplung statt Bauteil (Feld-Regel 6) [ES]:** Fuenf Wege fuehren zum Fermion aus Bosonen:
  1. Ladung + Monopol (Goldhaber)
  2. Isospin im Monopolfeld (Jackiw/Rebbi, Hasenfratz/'t Hooft)
  3. Medium mit theta = 2 pi (MKF; theta-Wert [L])
  4. e x m im Z_2-Torus-Code (STRINGENDE-1 [P])
  5. besondere Knotenbauweise (Levin/Wen [P, ueber STRINGENDE-1])

  Gemeinsam ist die gegenseitige Paarung von Ladung und Fluss, im U(1)-Fall die Phase e^{i q g/2}, im Z_2-Fall -1.
  Das Bauteil ist nicht die Ursache. STRINGENDE-1 fand dasselbe: "Das ganze Minuszeichen ... kommt aus dem
  e-m-Kreuzanteil" [P]. Fuer einen Q-Ball heisst die Groesse (-1)^Q.

## 7. Unterscheidungspunkte (Feld-Regel 2)

| Erklaerungspaar | Wo sie messbar auseinanderlaufen | Zugang |
|---|---|---|
| H1 (Fermion = Stringende, U(1)-Fassung) gegen H2 (Fermion = Dyon) | Statistik bzw. Drehklasse der *reinen* Einheitsladung: H1 -1 (E_f), H2 +1 (E_b). Zusaetzlich: Traegt das leichteste Fermion magnetischen Fluss durch eine umschliessende Flaeche? | im Modell messbar (Austauschmessung wie STRINGENDE-1). Energie: Das H1-Fermion kostet die Ladungsluecke, das H2-Fermion mindestens Ladungs- plus Monopol-Luecke [ES]; welche Luecke groesser ist, ist modellabhaengig (im Quanten-Spin-Eis vermutlich die Ladungsluecke [L?]) |
| Dyon ist Fermion (E_b M_b) gegen Monopol selbst ist Fermion (E_b M_f) | elektrische Ladung des leichtesten Fermions: 1 gegen 0 (Gauss-Fluss um das Teilchen) | im Modell messbar; beide stehen in Tabelle I bei theta = 0 [S] |
| Spin 1/2 (Leitidee) gegen Spin Q/2 (D1) | Entartung der tiefsten gebundenen Stufe: 2 gegen Q + 1, schon bei Q = 2 (Triplett) | LADUNG-MONOPOL-1, Vorhersage LM3 |
| Haftung durch Eichfeld gegen Haftung durch Zusatzkopplung | Grenzfall Portal -> 0: ohne Zusatzkopplung keine Bindung | vorab ableitbar (D3); Messung nur mit Portal sinnvoll |
| Benennung HFB gegen BSS | nirgends, reine Konvention | empirisch nicht unterscheidbar, also gleichwertig |

## 8. Projektbezug

- **FLUSS-1 (RUNDE-34/fluss-1)** [P]:
  - Ladung: q = rein - raus an einer Ecke, kleinste Verletzung +-2. Das Paar zieht entropisch mit ~1/r an
    (p = 0,963 +- 0,070).
  - Fluss: die Pfeile selbst, divergenzfrei (Pinch-Fliege, r^-3).
  - Ein "Monopol" kommt im Ergebnis nicht vor. Im Woerterbuch entspricht der FLUSS-1-Defekt dem CMS-Monopol und der
    HFB-Ladung.
  - Ein Monopol des konjugierten Feldes existiert dort nicht, weil das Modell klassisch ist [ES].
- **SPIN-1, Weg B (RUNDE-09/spin1/SPIN1.md; RUNDE-10.md Z. 300 bis 330 und 552)** [P]:
  - Ergebnis dort: "Bindung ja, Spin nein". Q/2-Regel, Bai/Lu/Orlofsky und die PDG-Drehimpulsformel stehen dort.
  - Fehlende Strukturen dort: Eichfeld, nichtabelsche Gruppe, adjungiertes Higgs.
  - Diese Karte ersetzt das nicht. Sie ergaenzt die Eis-Seite: Woher kaeme im Netz der Monopol, und welches Objekt ist
    das Fermion?
- **QBALL-LADUNG-1** [P]: Delta E ~ e^2 (Steigung 1,998) bei Q = 300 und 1000. Die Karte meint den Q-Ball als Ladung
  im Pfeil-Eis (Gegensweep G2). Fuer H2 gilt dann J in Q/2 + Z: Q = 300 waere ein Boson, Q = 1000 auch [ES].
- **QB-BS-2D** [P]: 2D-Rechnung. Eine 2D-Fassung von H2 laege im abschirmenden Regime (DeGrand/Toussaint [S]).
  QB-BS-2D hat dieselbe Lehre wie D3: Kopplung ueber Gleichtakt allein bindet nicht, Haftung bleibt klein oder
  ableitbar.
- **STRINGENDE-1** [P]: H2 ist die U(1)-Fassung in 3+1 D desselben Mechanismus (e x m mit gegenseitiger Paarung). Sie
  braucht keine besondere Knotenbauweise, aber das Quanten-Eis mit Monopolen [ES].
- **Ue2 ("ohne besondere Stringoperatoren")** [ES]:
  - Im Regime E_b M_b richtig, was die Knotenbauweise angeht.
  - Der Monopol selbst ist aber ein nichtlokales Objekt; sein Dirac-String ist nur wegen der Kompaktheit unsichtbar.
  - Das Dyon kostet mindestens Ladungs- plus Monopol-Luecke.
- **Projekt-grep** (runden-v3, ohne versiegelte und KS-1-Pfade) [P]:
  - Treffer: SPIN-1 Weg B (RUNDE-09/10, s. o.), Spin-Eis-Analogie (RUNDE-34), Monopolmode bzw. Monopolmasse in
    anderem Sinn (RUNDE-06, -14, -15, -23), Monopol-Einschluss (RUNDE-10/alt1).
  - Ein geladenes Teilchen im Gitter-Monopolfeld wurde nie gerechnet.

## 9. Vorschlag: Rechenkarte LADUNG-MONOPOL-1

**Frage:** Wird ein spinloses geladenes Teilchen auf dem Gitter um einen Gitter-Monopol zu einem Spin-1/2-Dublett
(q = 1) bzw. zu einem Spin-1-Triplett (q = 2)? Das ist der H2-Mechanismus (Spin = q/2) auf dem Netz, im
Einteilchen-Bild.

### Modell (Teil A, kubisch)

- **Gitter:** offene Box L^3, L in {12, 16, 24}. Einheitsmonopol (Fluss 2 pi) im Mittelwuerfel.
- **Fluss je Plakette:** Phi_p = Omega_p/2, wobei Omega_p der Raumwinkel der Plakette vom Monopol aus ist.
  - Das ist exakt wuerfelsymmetrisch und quellenfrei in jedem Wuerfel ausser dem Mittelwuerfel. Dort 6 x pi/3 = 2 pi,
    jeder Wert in (-pi, pi], also ein zulaessiger kompakter Gitter-Monopol.
- **Peierls-Phasen:**
  - A mit rot A = Phi_p - 2 pi [Plakette vom Dirac-String durchstossen], String entlang +z zum Rand.
  - Loesung etwa mit lsqr; Rest <= 1e-10.
- **Hamilton:** H = -sum_<ij> (e^{i q A_ij} c_i^+ c_j + h.c.) - V0 sum_{i in 8 Ecken des Mittelwuerfels} n_i.
  - q in {0 (ohne Monopol), 1, 2}; V0 in {0, 1, 2, 3, 4, 6, 8, 12} (der Kern-Topf ist die Zusatzkraft aus E5).
- **Messgroessen:**
  - tiefste 12 Eigenwerte
  - gebunden: E < -6 - 1e-3 und Gewicht in r <= 3 mindestens 0,9
  - Entartung: relativer Abstand <= 1e-8
  - Kommutatorzeichen s = <U_x U_y U_x^-1 U_y^-1> auf der tiefsten Stufe. U ist eine pi-Drehung um x bzw. y durch den
    Wuerfelmittelpunkt mal der passenden Eichtransformation. s haengt nicht von Phasenwahlen ab.
  - Schwelle V0c je q (Bisektion auf 1e-3)
- **Laufzeit:** duenn besetzte Matrizen bis 13 824 Zeilen, Sekunden je Fall; der Gesamtlauf liegt deutlich unter
  10 min auf der .69 (kleintest.sh, CPU-Spur).

### Vorhersagen (vor jeder Rechnung festzulegen; Vorschlag)

| Nr | Vorhersage | ableitbar? | Wahrsch. |
|---|---|---|---|
| LM0 | Kontrolle: q = 0: s = +1, tiefste gebundene Stufe einfach. Eichkonstruktion: Rest <= 1e-10; Spektrum unabhaengig von der String-Richtung (+z, -z, +x) auf 1e-10 | ja | 95 % |
| LM1 | Kontrolle: q = 1: s = -1 auf allen Stufen, jede Stufe gerade entartet; q = 2: s = +1 | ja (Paritaet des Gesamtflusses, [ES/L?]) | 90 % |
| LM2 | q = 1, L = 24, jedes V0 ueber der Schwelle: tiefste gebundene Stufe genau 2-fach (Dublett), nicht 4-fach | nein (Gitterkern) | 80 % |
| LM3 | q = 2, gleiche Bedingungen: tiefste gebundene Stufe genau 3-fach (Triplett, j = 1) | nein | 70 % |
| LM4 | V0c(q=1) > V0c(q=0) (ableitbar, Kato); Verhaeltnis V0c(1)/V0c(0) in [1,3; 3,0] | Vorzeichen ja, Groesse nein | 60 % |
| LM5 | gebundene Eigenwerte L = 16 gegen 24 auf 1e-6 gleich | nein (Endlichkeit) | 85 % |

### Bedeutung (vorab)

- **LM2 und LM3 treffen ein:** Auf dem Gitter wird ein spinloses Teilchen am Monopol zu Spin q/2. Das zeigt den
  H2-Mechanismus und die Q/2-Regel (D1) im Netz.
  - Es zeigt *nicht* die Austauschstatistik (dafuer Goldhaber [S]).
  - Es zeigt nicht, dass das Quanten-Pfeil-Eis Monopole hat.
- **LM2 trifft nicht ein** (Quartett unten): Der Gitterkern kehrt die Reihenfolge um. Dann beschreiben, ab welchem
  Kernradius bzw. L das Dublett unten liegt.
- **LM4 ausserhalb des Bandes:** Die Kontinuumsabschaetzung D4 traegt auf Kernradius ~1 nicht. Nur beschreiben.

### Schreibtischrechnung: was ohne Rechnung folgt, was die Rechnung kippen kann

- **Ohne Rechnung** [ES]:
  - s = -1 fuer ungerades q und Mindestentartung 2. Ein projektives Paar mit Kommutator -1 hat keine eindimensionale
    Darstellung.
  - Schwellenvorzeichen LM4 (Kato).
  - Kontinuumswerte: j_min = q/2, also Entartung 2 bzw. 3 [L Wu/Yang 1976].
  - Kontinuums-Schwellenverhaeltnis grob 1,9 (D4): Nullstelle von J_{-0,134} etwa 2,2 gegen pi/2. Die Zahl 2,2 ist
    interpoliert, nicht gerechnet.
- **Kann kippen:**
  - die Stufenordnung auf dem Gitter (Dublett gegen Quartett bei q = 1; Triplett gegen anderes bei q = 2)
  - das Schwellenverhaeltnis
  - die Groessenkonvergenz
- **Ehrlich:** LM0 und LM1 pruefen den Code, nicht die Physik. LM2 und LM3 sind Literatur-Erwartung (Kontinuum) auf
  einem neuen Gitter, aehnlich wie F1/F2 in FLUSS-1.

### Folgestufen (nur nach Teil A)

- **Teil B, Finns Netz:** dasselbe auf dem Pyrochlor-Kanten-Netz von FLUSS-1, Monopol in einem Tetraeder (Punktgruppe
  T_d). Vorhersage: Dublett unten [H].
- **Teil C, eigene Karte:** geladener Q-Ball am Monopol mit Portal-Topf. Axialsymmetrische r-theta-Rechnung, weil die
  Kugelform verboten ist (D2).
  - Vorab ableitbar: ohne Portal keine Bindung (D3).
  - Offen [H]: Haftung bis zu einem groessten Q, weil die Nullinie im Ball ~ R kostet und der Kerngewinn fest ist (D5).

### Schreibtisch-Grundlagen (aus ARBEITSFELD.md, Abschnitt 6)

- **D1:** Monopol-Kugelfunktionen: j >= |mu| = e g/(4 pi) = 1/2 je Quant. Q Quanten in einer Mode ergeben J = Q/2;
  allgemein liegt J in Q/2 + Z.
- **D2:** Tiefstes Dublett |Y|^2 ~ 1 + cos(theta), Nullinie bei theta = pi (der Dirac-String als Wirbelfaden von phi);
  phi ~ r^0,366 am Monopol.
- **D3:** Kato |D phi| >= |grad |phi||. Der Kreuzterm B_mon . B_ball integriert zu 0. Darum
  E(am Monopol) - E_mon >= E_frei(Q), strikt.
- **D4:** l(l+1) = 1/2; Schwelle sqrt(V0) r_c = erste Nullstelle von J_{l-1/2}.
- **D5:** grosse Baelle: Fadenkosten ~ phi_0^2 R gegen festen Kerngewinn [H].

## 10. Gegensweep-Befunde (Feld-Regel 4)

| Nr | Selbstverstaendlich angenommen | geprueft | Befund |
|---|---|---|---|
| G1 | Spinonen des Quanten-Eises sind Bosonen | teilweise (A9) | regimeabhaengig: E_b M_b oder (E_fT M_f)_theta [S?] |
| G2 | Der Q-Ball koppelt an das U(1) des Pfeil-Eises | ja, Projektdatei | ja; damit ist er dieselbe Sorte wie die FLUSS-1-Defekte, also kein Monopol-Partner |
| G3 | Thomson q g/(4 pi) gilt auch fuer einen ausgedehnten Q-Ball | Schreibtisch | Gesamt-J in Q/2 + Z ja. Der klassische Feldanteil einer zentrierten Kugelladung waere 0, die Kugelform ist aber verboten (D2) |
| G4 | 2+1 D waere gleichwertig | ja (A12) | nein, dort schirmen Monopole ab [S] |
| G5 | Das Abrufwerkzeug liest lange Volltexte ganz | ja (A15) | **nein:** Kuerzung nach Abschn. IV. Ein Abschnittsverweis ("XIV") im ersten Auszug kann nicht gelesen worden sein und ist herabgestuft |
| G6 | Das Quanten-Pfeil-Eis auf Pyrochlor-*Kanten* (Grad 6) hat eine stabile U(1)-Phase | nein | offen; HFB rechnen Pyrochlor-Ecken und Oktaeder-Netze [S] |
| G7 | Das Projekt hat zu Weg B nichts Eigenes | ja, Projektdateien | **nein:** SPIN1.md (30.09.) hatte Q/2-Regel, Bai/Lu/Orlofsky, "keine Bindung ohne Zusatzpotential" und PDG (94.3). Groesster Befund dieser Karte (Abschnitt 2, Punkt 0) |
| G8 | Das Dyon ist schwer wegen der Monopol-Luecke | nein (Abrufe verbraucht) | abgeschwaecht: im Quanten-Spin-Eis ist eher die Ladungsluecke gross [L?] |

## 11. Kalibrierung

- **(a) Gemessen:** nichts in dieser Karte. Die Projektrechnungen (FLUSS-1, QBALL-LADUNG-1, STRINGENDE-1) sind
  synthetisch; keine Messdaten.
- **(b) Verdichtet:** Woerterbuch (Abschnitt 5), Regime-Tabelle, (-1)^Q-Regel (schon SPIN1.md), Kato-Argument,
  Schwellenabschaetzung.
- **Doppelarbeit:** Die Q/2-Regel habe ich unabhaengig neu hergeleitet. Das ist eine zweite Lesung, keine neue Evidenz.
- **(c) Gewachsene Gewissheit ohne neue Evidenz:** "Im Quanten-Eis ist das Dyon das Fermion."
  - Gestuetzt nur auf Goldhaber [S] und die Kuerzel von Wang/Senthil; einen ausdruecklichen Satz habe ich nicht
    gelesen.
  - **Warnzeichen:** Meine Sicherheit stieg, waehrend die Frage in Regime zerfiel. Welches Objekt das Fermion ist,
    haengt von der Phase ab, beim Q-Ball von der Paritaet von Q.

## 12. Offene Fragen und Rueckfragen

- **R1 (an die Leitung):** Meint H2 mit "Monopol" den FLUSS-1-Defekt (CMS-Sprache) oder den Defekt des konjugierten
  Feldes? Nur der zweite gibt Thomson-Drehimpuls mit einer Pfeil-Eis-Ladung.
- **R2 (an die Leitung):** Soll der Q-Ball an das Eis-U(1) koppeln (dann dieselbe Sorte wie die Defekte) oder an ein
  zweites U(1)? Im zweiten Fall braucht es dessen Monopol.
- **O1 [H]:** Hat das Quanten-Pfeil-Eis auf Pyrochlor-Kanten (Ringaustausch auf Dreiecken) eine stabile U(1)-Phase,
  und sitzen seine Monopole in den Tetraedern?
- **O2:** Welche Familie (E_b M_b oder eine mit fermionischem E) waehlt Finns Netz ohne besondere Knotenbauweise? Ich
  erwarte E_b M_b [H].
- **O3:** Gibt es geeichte Q-Monopol-Baelle? Ohne Suche nicht pruefbar.
- **O4:** Dyon-Statistik ausdruecklich an einer Quelle lesen.
  - Wang/Senthil ab Abschn. V
  - Wilczek 1982, "Remarks on dyons", PRL 48, 1146 [L?]
  - "All-fermion electrodynamics" (Kravec/McGreevy/Swingle) [L?]
- **O5:** Thomson-Formel an einer Quelle lesen (Jackson Abschn. 6.12) [L].

## 13. Quellenliste mit Abrufstand

Alle Abrufe am 2026-10-04 per WebFetch. Die Zeitfenster sind die date-Stempel vor und nach der jeweiligen Abrufrunde.

| Nr | Quelle | URL | Abruf (CEST) | gelesen |
|---|---|---|---|---|
| A1 | C. Wang, T. Senthil (2015), "Dual Dirac liquid on the surface of the electron topological insulator", PRX 5, 041031, arXiv:1505.05141 | https://arxiv.org/abs/1505.05141 | 05:41:14 bis 05:42:11 | Abstract (nicht einschlaegig) |
| A2 | C. Castelnovo, R. Moessner, S. L. Sondhi (2008), "Magnetic Monopoles in Spin Ice", Nature 451, 42-45, arXiv:0710.5515 | https://arxiv.org/abs/0710.5515 | 05:41:14 bis 05:42:11 | Abstract |
| A3 | M. Hermele, M. P. A. Fisher, L. Balents (2004), "Pyrochlore Photons: The U(1) Spin Liquid in a S=1/2 Three-Dimensional Frustrated Magnet", PRB 69, 064404, arXiv:cond-mat/0305401 | https://arxiv.org/abs/cond-mat/0305401 | 05:41:14 bis 05:42:11 | Abstract |
| A4 | A. S. Goldhaber (1976), "Connection of Spin and Statistics for Charge-Monopole Composites", PRL 36, 1122 | https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.36.1122 | 05:41:14 bis 05:42:11 | Abstract |
| A5 | C. Wang, T. Senthil (2016), "Time-Reversal Symmetric U(1) Quantum Spin Liquids", PRX 6, 011034 | https://journals.aps.org/prx/abstract/10.1103/PhysRevX.6.011034 | 05:42:11 bis 05:43:29 | Abstract |
| A6 | R. Jackiw, C. Rebbi (1976), "Spin from Isospin in a Gauge Theory", PRL 36, 1116 | https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.36.1116 | 05:42:11 bis 05:43:29 | Abstract |
| A7 | P. Hasenfratz, G. 't Hooft (1976), "Fermion-Boson Puzzle in a Gauge Theory", PRL 36, 1119 | https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.36.1119 | 05:42:11 bis 05:43:29 | Abstract |
| A8 | Y. Bai, S. Lu, N. Orlofsky (2022), "Q-Monopole-Ball: A Topological and Nontopological Soliton", JHEP 01 (2022) 109, arXiv:2111.10360 | https://arxiv.org/abs/2111.10360 | 05:42:11 bis 05:43:29 | Abstract |
| A9 | wie A5, Volltext | https://journals.aps.org/prx/fulltext/10.1103/PhysRevX.6.011034 | 05:43:29 bis 05:45:23 | Werkzeugauszug; Text bis Abschn. IV (siehe A15) |
| A10 | M. A. Metlitski, C. L. Kane, M. P. A. Fisher (2013), "Bosonic topological insulator in three dimensions and the statistical Witten effect", PRB 88, 035131, arXiv:1302.6535 | https://arxiv.org/abs/1302.6535 | 05:43:29 bis 05:45:23 | Abstract |
| A11 | O. Benton, O. Sikora, N. Shannon (2012), "Seeing the light: experimental signatures of emergent electromagnetism in a quantum spin ice", PRB 86, 075154, arXiv:1204.1325 | https://arxiv.org/abs/1204.1325 | 05:43:29 bis 05:45:23 | Abstract |
| A12 | T. A. DeGrand, D. Toussaint (1980), "Topological excitations and Monte Carlo simulation of Abelian gauge theory", PRD 22, 2478 | https://journals.aps.org/prd/abstract/10.1103/PhysRevD.22.2478 | 05:45:23 bis 05:47:39 | Abstract |
| A13 | M. Levin, X.-G. Wen (2005), "Photons and electrons as emergent phenomena", RMP 77, 871, arXiv:cond-mat/0407140 | https://arxiv.org/abs/cond-mat/0407140 | 05:45:23 bis 05:47:39 | Abstract |
| A14 | wie A8, Volltext (arXiv-HTML) | https://arxiv.org/html/2111.10360 | 05:45:23 bis 05:47:39 | Werkzeugauszug (Gl. 1-2, Abschn. 2.3, 3) |
| A15 | wie A5, Volltext, enge Wortsuche | https://journals.aps.org/prx/fulltext/10.1103/PhysRevX.6.011034 | 05:48:00 bis 05:51:24 | Werkzeugauszug, gekuerzt |

- **Nicht abgerufen, nur Gedaechtnis [L]:**
  - J. J. Thomson 1904 (Feld-Drehimpuls); J. D. Jackson, Classical Electrodynamics, Abschn. 6.12
  - T. T. Wu, C. N. Yang 1976, "Dirac monopole without strings: monopole harmonics", Nucl. Phys. B 107, 365
  - Kato-Ungleichung (diamagnetische Ungleichung); A. M. Polyakov 1977 (kompakte QED in 2+1 D)
  - Gingras/McClarty, Rep. Prog. Phys. 77, 056501 (2014) [L?], nicht abgerufen
- **Projektdateien [P]:**
  - RUNDE-37: ladung-monopol-l/KARTE.md, qball-ladung-1/ERGEBNIS.md und KARTE.md, qb-bs-2d/ERGEBNIS.md,
    stringende-1/ERGEBNIS.md, UEBERLEITUNGEN-EMERGENZ.md
  - IDEEN-EVOLUTION/GEN-04-SPIN-HALB.md
  - RUNDE-34: fluss-1/KARTE.md und ERGEBNIS.md, TETRAEDER-ANALYSE.md, eis-1/ERGEBNIS.md
  - RUNDE-09/spin1/SPIN1.md (Weg B; dort gelesen: PDG 2025 Rev. 94, Lee u. a. 1989, Bai/Lu/Orlofsky) und
    RUNDE-10.md Z. 300 bis 330, 552 (gelesen 05:57 bis 05:58 CEST)

## 14. Selbstanzeigen

1. **Werkzeugauszuege:** Volltextangaben (A9, A14, A15) stammen aus dem Auszug des Abrufwerkzeugs, nicht aus eigener
   Lektuere.
   - A9 nannte "Abschn. XIV", obwohl der Text nach A15 bei Abschn. IV endet. Diese Angabe ist herabgestuft [S?].
2. **Ein Abruf ging auf die falsche Kandidatennummer** (A1). Die Verwechslung ist als Befund verbucht.
3. **Der Dyon-Satz ist nicht an einer Quelle gelesen.** Wo ich "Dyon bei E_b M_b ist ein Fermion" schreibe, ist das
   [ES] aus Goldhaber [S].
4. **Die Schwellenzahl 2,2 (D4)** ist interpoliert, nicht gerechnet.
5. **Die Rechenkarte ist ein Vorschlag.** Ihre Zahlen sind nicht eingefroren. Die Ableitbarkeitsprobe steht in
   Abschnitt 9.
6. **Projekt-grep nur halb befolgt** (Memory-Regel vom 03.10.).
   - Der grep um 05:35 zeigte RUNDE-09.md und RUNDE-10.md; gelesen habe ich die Treffer erst um 05:57 im Gegensweep.
   - Zwei Abrufe (A8, A14) und die Herleitung D1 haben dadurch Bekanntes wiederholt.
   - Die Aussagen sind berichtigt, nicht geloescht.

## Einfach gesagt

Man kann aus zwei Teilchen, die sich selbst nicht drehen, ein Teilchen mit halbem Spin bauen, wie ein Elektron: Man
braucht eine elektrische Ladung und einen magnetischen Pol. Ihre beiden Felder speichern zusammen genau einen halben
Drehimpuls; das ist seit 1976 bekannt. In Finns Pfeil-Eis gibt es bisher nur die eine Sorte, die Ladungen. Die
magnetischen Pole entstehen erst, wenn das Eis quantenmechanisch wackeln darf. Ein geladener Q-Ball am Pol haette
nicht Spin 1/2, sondern die Haelfte seiner Ladungszahl, und er bleibt durch elektrische und magnetische Kraefte allein
nicht haengen; dafuer braucht es eine zusaetzliche Klebekraft. Eine kleine Gitterrechnung kann pruefen, ob ein
geladenes Teilchen um einen Gitter-Pol wirklich ein Halb-Spin-Paar bildet.
