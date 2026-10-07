# TWIST-PYRO-1: Laesst sich der Levin/Wen-Twist (Fermionen als Pfeilenden) auf Finns Netz uebertragen, "durch" (Diamant) und "entlang" (Pyrochlor-Kanten)? (Runde 40)

- Leitung claude-primary. Karte und Wahrscheinlichkeiten geschrieben ab 2026-10-04 11:33:28 CEST (date), vor jeder
  Rechnung. Vorlage: Abschnitt 8 von RUNDE-37/dyon-statistik-l/DOSSIER.md (Vorschlag des feldforschers, mit
  Ableitbarkeitsprobe); Modell, Messgroessen und Vorhersagen von dort uebernommen, Bedeutungssaetze von der Leitung.
- **Anlass:**
  - DYON-STATISTIK-L: Das Dyon (1,1) im Quanten-Eis ist ein Fermion mit halbem Drehimpuls, koppelt aber stark ans Licht
    (alpha >= 1,45 im Quanten-Spin-Eis gegen <= 0,2 fuer die einfache Ladung). Ein elektronartiges, schwach gekoppeltes
    Fermion verlangt, dass schon das Pfeilende selbst ein Fermion ist (H1); bei Levin/Wen geht das nur mit "verdrehten"
    Stringoperatoren.
  - Finns Konzept (RUNDE-34/tetra-konzept/ANALYSE.md): Die Krafteinheiten "muessten eigentlich dadurch oder daran entlang
    fliessen". Das Projekt hat beide Lesarten: "durch" = Diamant-Kanten (Spin-Eis-Gitter, KITAEV-DIAMANT-1), "entlang" =
    Pyrochlor-Kanten (FLUSS-1).
- **Projekt-grep (feldforscher und Leitung):** STRINGENDE-1 (Z_2, LW-2003-Spin-3/2-Modell), KITAEV-DIAMANT-1 (Z_2,
  Majoranas auf Diamant); ein U(1)-Twist auf Diamant- oder Pyrochlor-Kanten wurde nicht gerechnet. "quantum ether",
  "rotor model", "twisted string" nur in GEN-04-SPIN-HALB.md und im Dossier.
- Kennzeichen: [M] Mathematik, [S] an der Quelle gelesen, [H] Hypothese.

## Modell und Messgroessen (aus dem Dossier)

- Pfeile als Spin 1/2 auf den Kanten, periodische Zellen: Diamant 2 x 2 x 2 und 3 x 3 x 3 kubische Zellen; Pyrochlor-Kanten
  1 x 1 x 1 und 2 x 2 x 2.
- Ladung Q_I = rein - raus je Knoten (orientierte Kanten statt der LW-Staffelung (-1)^I).
- Stringoperator W(C) = Produkt der sigma^+/sigma^- entlang C; gedreht: W~(C) = W(C) mal Produkt von sigma^z ueber die
  Kanten, die die Rahmung C' kreuzen (LW Gl. 8; Projektion auf eine Ebene, drei Projektionsrichtungen).
- Exakt und ganzzahlig, wie STRINGENDE-1:
  - T1: Vertauschen alle gedrehten kleinsten Schleifenoperatoren paarweise und mit allen Q_I? (Diamant: Sechsecke;
    Pyrochlor-Kanten: Dreiecke und Sechsecke)
  - T2: Vorzeichen der Huepfalgebra nach LW Gl. (12) fuer alle geordneten Kantentripel an einem Knoten (Diamant 24,
    Pyrochlor-Kanten 120)
  - T3, Kontrolle: ungedreht, Vorzeichen +1
  - T4, Kontrolle: kubisches Gitter mit LW-Projektion (Nachbau der Quelle), Vorzeichen -1
- Quelle zuerst lesen: Levin/Wen (Quantum ether, PRB 73, 035122 (2006) bzw. arXiv-Fassung; Fundstellen nur aus selbst
  gelesenem Text, hoechstens 3 Abrufe; die lokale Kopie des feldforschers in RUNDE-37/dyon-statistik-l/quellen/ zuerst
  pruefen).

## Vorhersagen (vor jeder Rechnung)

| Nr | Vorhersage | vorab ableitbar? | Wahrsch. |
|---|---|---|---|
| TP0 | T3 = +1 und T4 = -1 in allen Tripeln; T1 auf dem kubischen Gitter erfuellt | ja (prueft Code und Nachbau) | 90 % |
| TP1 | [H] Teil A (Diamant): T1 erfuellt fuer mindestens eine Projektion, T2 = -1 an allen Knoten | teilweise | 65 % |
| TP2 | [H] Teil B (Pyrochlor-Kanten): T1 erfuellt fuer mindestens eine Projektion | nein | 40 % |
| TP3 | [H] falls TP2: T2 = -1 an allen Knoten und unabhaengig von der Projektionsrichtung | nein | 50 % |

**Bedeutung (vorab):**
- **TP1 trifft ein:** In der Lesart "durch" (Spin-Eis-Gitter) laesst sich ein Pfeilende algebraisch zum Fermion machen;
  ein elektronartiges Fermion ist auf diesem Netz baubar. Ob die Phase existiert und wie stark sie ans Licht koppelt,
  bleibt offen.
- **TP2 scheitert:** In der Lesart "entlang" traegt der einfache LW-Twist nicht; dort bleibt das Netz ohne andere
  Knotenbauweise im Dyon-Regime (Fermionen nur stark gekoppelt).
- **TP2 und TP3 treffen ein:** Beide Lesarten von Finns Bild tragen schwach koppelbare Fermionen als Pfeilenden [H].

## Rahmen

- Code-Agent. Laeufe nur auf der .69 ueber kleintest.sh, Spur cpu6; je <= 10 min.
- Plan vor der ersten echten Rechnung einfrieren. Rauchlauf zuerst.
- Zeitbox 120 min.
