# TWIST-SPIN-1: Haben die Fadenend-Fermionen auf Finns Netz Spin 1/2 unter den Tetraeder-Drehungen? (Runde 41)

- Leitung claude-primary. Karte und Wahrscheinlichkeiten geschrieben ab 2026-10-04 13:13:02 CEST (date), vor jeder
  Rechnung.
- **Anlass:**
  - TWIST-PYRO-1: Mit Levin/Wens verdrehten Stringoperatoren (Rahmung lokal gelesen) ist ein Fadenende auf Finns Netz in
    beiden Lesarten (Diamant "durch", Pyrochlor-Kanten "entlang") algebraisch ein Fermion (Austauschvorzeichen -1);
    vorab ableitbar. Nicht gezeigt: Spin 1/2 unter Drehungen.
  - Die Rahmung haengt an einer gewaehlten Projektionsrichtung (Ebene); eine Gitterdrehung bildet sie auf eine andere ab.
    Ob die Drehungen dann ueberhaupt als Symmetrie auf den verdrehten Operatoren wirken, ist offen.
  - Finns Frage "Haben wir ein Teilchenmodell?" und seine Idee "Spins mit Raumzeit-Symmetrien": Spin 1/2 hiesse hier,
    dass die Fermion-Operatoren eine projektive (doppelwertige) Darstellung der Tetraedergruppe tragen, also z. B. eine
    Dreierdrehung dreimal angewandt -1 gibt bzw. die Doppelgruppe 2T statt T wirkt.
- **Ableitbarkeitsprobe (Leitung, vor der Karte) [H, ungeprueft]:** Verdrehte Strings sind gerahmte Strings (Baender);
  dreht man ein Fadenende um 2 pi, bekommt das Band eine volle Verdrillung, und fuer Fermionen gehoert dazu nach dem
  Spin-Statistik-Bild der Faktor -1 ("topologischer Spin") [L?]. Das waere fuer eine kontinuierliche Drehung ableitbar.
  Nicht ableitbar ist, ob die diskreten Gitterdrehungen von Finns Netz mit der festen Projektion vertraeglich wirken und
  welche Darstellung (T oder 2T) die Fermion-Operatoren dann tragen. Projekt-grep: TWIST-PYRO-1, STRINGENDE-1 (2-pi-Drehung
  von epsilon in 2D: -1, "derselbe Mechanismus wie SE2"), KITAEV-DIAMANT-1; keine Rechnung zur Punktgruppe auf
  verdrehten Strings.
- Kennzeichen: [M] Mathematik, [G] Rechnung, [L] Literatur, [H] Hypothese.

## Test (Code-Agent; Schreibtisch zuerst)

- **Quelle zuerst:** Levin/Wen (Quantum ether, hep-th/0507118; lokale Kopie in RUNDE-37/twist-pyro-1/quellen/) zu
  Drehungen, Rahmung und Spin der Fermionen; hoechstens 3 weitere gezielte Abrufe (z. B. zu "framed strings" bzw.
  topologischem Spin emergenter Fermionen in 3D); Fundstellen nur aus selbst gelesenem Text.
- **Algebra (exakt, ganzzahlig, Code aus RUNDE-37/twist-pyro-1/code/):**
  - Fuer jede Gitterdrehung g der Punktgruppe am Knoten (Diamant: T_d am Knoten; Pyrochlor-Kanten: D_3d bzw. die
    Tetraederdrehungen am Tetraeder) die verdrehten Huepfer W~(g C) mit g W~(C) g^-1 vergleichen: gleich bis auf welches
    Vorzeichen bzw. welchen lokalen Eichfaktor?
  - Gibt es lokale Eichfaktoren (Vorzeichen je Kante bzw. Knoten), mit denen die Drehungen als Symmetrie wirken? Welche
    Gruppe erzeugen sie auf den Fermion-Operatoren: T (ganzzahlig) oder 2T (projektiv, Spin 1/2)?
  - Pruefgroessen: (C3)^3, (C2)^2 und (C2 C3)^3 auf einem Fermion-Paarerzeuger, als exaktes Vorzeichen.
- **Kontrolle:** ungedrehte Strings (Bosonen): alle Vorzeichen +1. Kubischer LW-Nachbau mit Vierteldrehungen als zweite
  Kontrolle (Vorzeichen im Plan vorab angeben, falls ableitbar).

## Vorhersagen (vor jeder Rechnung)

| Nr | Vorhersage | Wahrsch. |
|---|---|---|
| TS0 | Kontrolle: ungedrehte Strings tragen eine echte (nicht projektive) Darstellung, alle Pruefvorzeichen +1 | 90 % |
| TS1 | [H] Auf dem Diamantnetz wirken die Tetraederdrehungen mit lokalen Eichfaktoren als Symmetrie der verdrehten Huepfer | 55 % |
| TS2 | [H] falls TS1: Die Fermion-Operatoren tragen eine projektive Darstellung (Spin 1/2, mindestens ein Pruefvorzeichen -1, wie in 2T) | 45 % |
| TS3 | [H] Auf den Pyrochlor-Kanten gilt dasselbe wie auf dem Diamant (TS1 und TS2 gleich) | 40 % |

**Bedeutung (vorab):**
- **TS1 und TS2 treffen ein:** Auf Finns Netz traegt das Ende eines verdrehten Pfeilfadens Fermion-Statistik und Spin
  1/2 unter den Tetraeder-Drehungen: Spin und Statistik kommen aus derselben Verdrehung [H]. Das waere der erste Weg im
  Projekt, auf dem halber Spin aus Finns Netz selbst entsteht statt eingesetzt zu werden.
- **TS1 verfehlt:** Die Rahmung bricht die Drehsymmetrie; das Fermion hat dann keinen wohldefinierten Spin unter
  Gitterdrehungen, und die Projektion ist eine echte Zusatzstruktur.
- **TS2 verfehlt (ganzzahlig):** Fermion-Statistik ohne Spin 1/2 unter Gitterdrehungen; der Spin-Statistik-Zusammenhang
  gilt dann auf Finns Netz nicht von selbst.

## Rahmen

- Code-Agent. Laeufe nur auf der .69 ueber kleintest.sh, Spur cpu6; je <= 10 min.
- Plan vor der ersten echten Rechnung einfrieren. Rauchlauf zuerst.
- Zeitbox 120 min.
