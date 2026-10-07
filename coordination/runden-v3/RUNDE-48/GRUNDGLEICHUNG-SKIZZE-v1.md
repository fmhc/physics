# Grundgleichung fuer Finns Netz: Was muss hinein? (Skizze der Leitung, Fassung 1)

- Leitung claude-primary, geschrieben ab 2026-10-05 10:17:41 CEST (date).
- **Finn (05.10.):**
  - "Überleg mal was in die Grundgleichung rein muss"
  - vorher: "Es kann sein das einige Sachen einfach emergent sind und diese Dynamiken müssen wir finden" und "Self organized criticality und so"
- **Status:** Entwurf, Schreibtisch [ES]. Kein frischer Leser. Codex' Gegenblick ist angefragt. Alle Projektbezuege sind Modellrechnungen, keine Messdaten.
- **Leitgedanke [H]:**
  - So wenig wie moeglich hineinschreiben. Was entstehen kann, soll entstehen: Richtungsgleichheit, ein gemeinsames Tempo, Newton, Mitfuehrung.
  - In die Gleichung gehoeren nur der Zustand, **eine** Hodge-Struktur, **ein** Takt mit Verschiebung, die einfachsten oertlichen Terme jedes Feldes und eine Umklapp-Regel.

## 1. Zustand (was das Netz "ist")

| Groesse | sitzt auf | Bemerkung |
|---|---|---|
| Kantenlaengen l_e bzw. q_e = l_e^2 | Kanten | Geometrie = Raum (Finn) |
| Zerlegung T (welche Tetraeder) | ganzes Netz | aendert sich nur durch Umklappen |
| Takt N_v (Lapse) und Verschiebung s_v (Shift) | Ecken | keine eigene Dynamik; Lagrange-Multiplikatoren, die die Regeln erzeugen |
| Materiefeld phi_v (komplex, Q-Ball) | Ecken | Teilchen als Solitonen [P] |
| Lichtfeld A_e (U(1)-Phase) | Kanten | Feldstaerke auf Dreiecken |
| spaeter: Fermionen | Koketten aller Stufen | Kaehler-Dirac (d - delta) mit denselben Hodge-Sternen; im Projekt auf Zufallsnetzen schon angefasst (INDUZIERT-WILSON-2D) [P] |
| spaeter: Kleber | Kanten | SU(3) bzw. Rishons (L7, geparkt) |

## 2. Eine Wirkung aus einer Hodge-Struktur (Kern der Gleichung)

**Schema [ES]:** S = Integral dt [ K_Geometrie - N V_Geometrie + L_Licht + L_Materie ]. Alle Gewichte kommen aus den umkreisbasierten Hodge-Sternen *0, *1, *2, *3 des aktuellen Netzes, alle Terme tragen denselben Takt N und dieselbe Verschiebung s.

1. **Geometrie, Bewegung:**
   - Lund-Regge-Supermetrik Summe_t V_t [h':h' - (tr h')^2], volumengewichtet, auf den Geschwindigkeiten, lambda = 1 [S, REGGE-KINETIK-L].
   - Unser bisheriger Code setzt eine DeWitt-Form je Tetraeder auf die Impulse. Ob das die Richtungsprobleme macht, prueft LUND-REGGE-MASSE-1 (laeuft).
2. **Geometrie, Kruemmung:** Regge-Glied Summe_e l_e eps_e (Fehlwinkel an den Kanten), dazu ein Volumenglied Lambda Summe_t V_t. Fuer Lambda gibt es zwei Wege:
   - fest
   - unimodular als Integrationskonstante (Henneaux/Teitelboim; Gielen/Ried 2026) [S]
   - Der unimodulare Weg macht Lambda zur Ausgabe, erklaert aber noch nicht, warum es klein ist.
3. **Licht:** elektrische Energie Summe_e (*1_e)^-1 E_e^2, magnetische Summe_f *2_f (dA)_f^2, dazu die Gauss-Regel d0^T E = rho als Zwangsbedingung.
4. **Materie (Q-Ball-Feld):**
   - Bewegung Summe_v *0_v \|D_t phi\|^2 / N
   - Gradient Summe_e *1_e \|phi_a - phi_b\|^2. Das ist Finns Takt-Operator, der 8-fache Hodge-Laplace [P, TAKT-UMKLAPP-1].
   - Potential Summe_v *0_v U(\|phi\|) (Papier I)
   - Ladung ueber die Kopplung an A_e
5. **Kopplung "von selbst":** Weil alle Materieterme die Hodge-Sterne des Netzes benutzen und diese von den Kantenlaengen abhaengen, entsteht die Spannungskopplung automatisch als Ableitung nach l. Die Impulskopplung entsteht ueber die Verschiebung s. Kopplung und Rueckwirkung stammen aus demselben Term [ES; im Vektor-Sektor gezeigt in IMPULS-NETZ-1].
   - Das ist die diskrete Form des Aequivalenzprinzips: Alles spuert dieselbe Geometrie und denselben Takt.

**Was das schon liefert [P]:**
- Licht und Skalar haben mit diesen Gewichten langwellig auf jedem periodischen Netz exakt dasselbe richtungsgleiche Tempo (DANZER-NAEHERUNG-2). Das gemeinsame c ist damit eine Folge der einen Hodge-Struktur, nicht eine Setzung.
- Fuer Schwerewellen ist das offen, denn Rang 2 erzwingt nicht Rang 4 (Codex, nachgerechnet). Genau das prueft LUND-REGGE-MASSE-1.

## 3. Takt und Regeln (Zwangsbedingungen)

- Aus N_v folgt die Hamilton-Regel H_v = 0 je Ecke, aus s_v die Verschiebungsregel D_v = 0 je Ecke.
- Finns Takt entspricht maximalen Zeitscheiben (K = 0), also der einzigen datenvertraeglichen Horava-Ecke [S, SKALAR-SEKTOR-L].
- Ein einziger globaler Takt scheidet nach heutigem Stand aus.
- **Pflicht:** Die Regeln muessen erster Klasse sein, wenigstens linear um das flache Netz. Die Impulsregel ist es (IMPULS-NETZ-1); die skalare Regel ist es auf dem gefuellten Netz noch nicht. Entscheidend ist eine Passbedingung auf dem Gitter (SKALAR-SEKTOR-L).
  - Regge selbst bricht die Umbenennungs-Symmetrie, ausser nahe flach (Bahr/Dittrich) [S].
  - Wege: Regeln als zweite Klasse mit Dirac-Klammer hinnehmen, verbesserte Wirkungen durch Vergroebern (Dittrich), oder kovariante 4D-Zeit mit Zeltstangen (Regime K).

## 4. Umklappen (Zerlegung T aendert sich)

- **Wann:** Delaunay waehlt die Zelle. Eine fremde Ecke in der Umkugel loest den Zug aus [P, TAKT-UMKLAPP-1].
  - Damit bleiben alle umkreisbasierten Hodge-Sterne positiv (HKV 2013).
  - Am Zug ist das duale Mass der klappenden Kante bzw. Flaeche beim 2-3-Zug null, also springen Licht- und Materieterme nicht [M, TAKT-DYNAMIK-1].
- **Wie:** eine kanonische Uebergabe von Lagen und Impulsen auf einem gemeinsamen reduzierten Raum. Beim 2-3-Zug in flacher Geometrie gibt es beidseitig 9 geometrische Freiheitsgrade, also mit Abgleichsbedingungen [M]. Bisher fehlt sie; daher der Energiesprung (TAKT-DYNAMIK-1; Codex Ideation 3, Rang 2).
- 1-4- und 4-1-Zuege aendern die Zahl der Ecken. Sie brauchen neue bzw. wegfallende Zwangsbedingungen (Dittrich/Hoehn) [S].

## 5. Was NICHT hinein soll (soll entstehen) und was noch fehlt

**Soll entstehen [H]:**
- Richtungsgleichheit aller Wellen und ein gemeinsames c
- Newton und Lichtablenkung (MATERIE-NETZ-1)
- Mitfuehrung (IMPULS-NETZ-1)
- Finns Takt als Hodge-Laplace (schon gezeigt)
- Traegheit aus der Geometrie (Lund-Regge)
- vielleicht ein kleines Lambda durch Selbstorganisation (SOC-RAUM-L laeuft)
- Ob das Netz von selbst in einen kritischen Zustand laeuft, ist eine Frage an die Umklapp-Dynamik (SOC-UMKLAPP-1 geplant).

**Konstanten, die drinbleiben (so wenige wie moeglich):**
- Kantenlaenge l (Planck-Skala, setzt G)
- Lambda (oder Integrationskonstante)
- die Q-Ball-Parameter (m, Kopplungen)
- die Licht-Kopplung e
- spaeter die Kleber-Kopplung
- Alles andere muss folgen.

**Noch nicht drin, aber noetig:**
- **Fermionen und Spin 1/2:** Kaehler-Dirac auf den Koketten ist der natuerliche Kandidat, mit denselben Hodge-Sternen. Er bringt aber mehrere "Geschmaecker" mit, die in 4D nicht automatisch drei Generationen sind [L].
- **Quantenmechanik:** Die Gleichung ist klassisch. Ein Pfadintegral ueber Laengen und Zerlegungen mit e^{iS} (Regge/CDT-artig) setzt das i ein. Dass es aus der Umklapp-Statistik entsteht, ist offen und stoesst an Bell bzw. Wallstrom.
- **Grundlagen (L11):**
  - Die reduzierte Energie muss nach unten beschraenkt sein. Die lambda = 1-Form ist indefinit; positiv kann nur die reduzierte Energie sein, wie beim Positiv-Energie-Satz.
  - kausales Anfangswertproblem
  - kontrollierter Kontinuumsbereich

## 6. Reihenfolge der naechsten Schritte (Vorschlag)

1. **Traegheit richtig:** LUND-REGGE-MASSE-1 (laeuft), HODGE-MASSE-1 (laeuft).
2. **Kanonische Umklapp-Uebergabe:** Karte nach (1), Codex Rang 2 und 4.
3. **Erste Klasse der skalaren Regel:** Passbedingung auf dem Gitter, gegebenenfalls Regime K.
4. **Materie und Licht in dieselbe Wirkung:** Q-Ball und Maxwell mit Netz-Hodge-Sternen, dazu ein Test, ob ein Q-Ball die richtige schwere Masse hat (Bindungsenergie, Codex Rang 8).
5. **Selbstorganisation:** SOC-UMKLAPP-1.
6. **Fermionen:** Kaehler-Dirac auf dem 3D-Netz mit Takt.

## Einfach gesagt

Die Grundgleichung soll aus wenigen Zutaten bestehen: Kantenlaengen als Raum, eine Uhr je Ecke, Licht auf den Kanten und das Materiefeld auf den Ecken, alle gemessen mit demselben Massstab, den Hodge-Gewichten des Netzes. Dazu kommt die Regel, dass Zellen umklappen, sobald eine fremde Ecke zu nahe rueckt, und dass dabei nichts verloren geht. Weil alles denselben Massstab benutzt, folgen gleiche Lichtgeschwindigkeit und gleiche Schwerkraft fuer alle von selbst. Noch fehlen die halbzahligen Teilchen und die Quantenmechanik. Hineinschreiben will man moeglichst wenig, der Rest soll entstehen.
