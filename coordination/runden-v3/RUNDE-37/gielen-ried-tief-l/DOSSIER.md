# GIELEN-RIED-TIEF-L: Dossier zu Gielen/Ried, "Unimodular boundary time for Regge calculus" (arXiv 2610.03479v1)

## 1. Kopf

- Karte: KARTE.md in diesem Ordner (Vorhersagen GR1 bis GR7 geschrieben ab 12:23:53, hier unveraendert beurteilt).
- Start 2026-10-05 12:24:50 CEST (date, erster Befehl). Dossier begonnen 12:47:04 CEST (date). Endzeit: letzte Zeile.
- **Abrufe: 11 von 15** (Abruf 1 = Volltext). Erwartung vor jedem Abruf und Ausgang stehen in ARBEITSFELD.md, ebenso
  Gegensweep, Offenes und Regelverstoesse. Quellenkopien in quellen/.
- **Kennzeichen:** [S] an der Quelle gelesen, mit Abschnitt, Gleichung oder Seite (Seite = PDF-Seite); [S Abstract];
  [S Treffer] nur Suchtreffer bzw. Werkzeug-Zusammenfassung; [L] Gedaechtnis; [L?] unsicher; [P] Projektdatei; [M]
  Handrechnung, im Text gezeigt; [ES] eigener Schluss; [H] Hypothese.
- Literatur und Schreibtisch, keine Messdatenbestaetigung. Die Zahlen der Arbeit sind Rechnungen, keine Messungen.
- **Projektlage vorab [P]:** Die Leitung hat den Volltext schon am 05.10. um 04:38:04 gelesen und G1 bis G4 geurteilt
  (ARBEITSFELD-claude-primary.md); WELTKRISTALL-L hat die Abschnitte III bis V gelesen. Was dort steht, fuehre ich nicht
  als neu (Liste in 6.4).

## 2. Ergebnis zuerst

1. **Was die Arbeit ist [S]:** eine klassische, euklidische Machbarkeitsstudie. Sie schreibt eine Henneaux-Teitelboim-
   Regge-Wirkung (Gl. 27) mit einem globalen Paar (Lambda, unimodulare Randzeit T) auf und rechnet zwei sehr grobe Modelle
   zwischen zwei 5-Zellen. Kein Pfadintegral, keine Lorentz-Rechnung, keine Materie, keine Wellen, keine raeumliche
   Verfeinerung; das Wort "clock" kommt nicht vor. Der "Kontinuumslimes" ist ein Zeitlimes (DeltaT -> dT) bei grober
   5-Zelle, mit Abweichungen der Groessenordnung 1 (Tab. I, II).
2. **Finns Takt kann die unimodulare Zeit sein, aber nur global [S + M].** In HTR ist T exakt global: Die Variablen
   je Tetraeder bilden einen Fluss mit Eichfreiheit (Gl. 28 bis 31); physikalisch ist nur die Summe ueber eine ganze
   Randflaeche. Nach Kuchar 1991 etikettiert T nur Klassen von Hyperflaechen gleichen 4-Volumens [S Abstract]; Gielen/Ried
   sagen das in einem Satz ("presupposes a fixed choice of foliation [44]", II A). In Kuchars Form (Isham 1992, Gl. 4.4.4)
   gehoert zu T ein raeumlich gleicher Lapse. Diskret sind das gleiche Zeltstangen mit festem Gesamtzuwachs, und genau das
   rechnet REGIME-K-1 im periodischen Fall schon [P + M].
3. **Die oertliche Fassung "jeder Zeltzug fuegt dasselbe 4-Volumen hinzu" ist schlecht gestellt [M, Kriterium S].** Sie
   heisst h_v = 4 dT / Vol3(Stern v), im Kontinuum N sqrt(q) = 1, also Bona-Masso-Scheibung mit f = -1. Fuer f < 0 ist die
   Eichgleichung "elliptic instead of hyperbolic" (Alcubierre u. a. 2003, Gl. 2.3). Im Lorentz-Fall wachsen Beulen der
   Scheibung wie exp(|k| t). Die Takt-Regeln, bei denen die Zeltstange vom Zellvolumen abhaengt, liegen auf einer Linie f:
   oertlich unimodular -1, gleiche Zeltstangen 0 (geodaetisch), harmonisch +1, maximale Scheibung K = 0 als Grenzfall
   f -> unendlich (Regel 6). Meint "Schritt" den ganzen Takt statt des einzelnen Zuges, ist die Regel die globale Fassung
   und unbedenklich.
4. **Torus, K = 0 und periodische Rechnungen [S + M]:** T^3 mal Zeitintervall ist erlaubt. Periodische Zeit (T^4) zwingt
   in der HT-Fassung alle 4-Simplizes auf Volumen null (II A S. 5; Gl. 33). Bloch-Rechnungen auf dem unendlichen periodischen Gitter
   (REGIME-K-1) sind fuer k != 0 nicht betroffen. Der Erhalt von K = 0 und eine laufende unimodulare Uhr schliessen sich auf
   dem Torus jenseits linearer Ordnung aus: K = 0 erzwingt N = 0, also T' = 0.
5. **Groesster Erwartungsverstoss:** Unruh/Wald 1989 sind nicht Gegner, sondern Urheber des Vorschlags (Minisuperraum gut,
   allgemeine Raumzeiten vermutlich zu wenige Observablen) [S Abstract]. Der Einwand stammt von Kuchar. Es gibt zwei Regime,
   der Moderator ist die Homogenitaet: Im Minisuperraum traegt T als Uhr. Dort rechnen alle neun Treffer 2024 bis 2026, die
   T als Uhr nutzen (Minisuperraum, Kugelsymmetrie, 2D-JT; die uebrigen drei der zwoelf Treffer sind formal), und beide
   Modelle der Arbeit. Auf einem inhomogenen Netz wie Finns braucht T eine zweite Regel, die festlegt, wo der Zuwachs
   hinkommt.

## 3. Inhalt des Artikels, Abschnitt fuer Abschnitt [S]

Gielen, S.; Ried, S. (2026), Sheffield. arXiv:2610.03479v1 [gr-qc], 02.10.2026, 30 Seiten. Abruf 1 ist bytegleich mit der
Projektkopie in RUNDE-45/quellen-leitung (sha256 22853a56...965d), also v1. Ganz gelesen; Tabellen und Gl. (27) im
-layout-Text nachgeprueft. Einheiten c = hbar = 8 pi G = 1 (S. 3).

**Abstract und I (S. 1-3).**
- HT-Gravitation ist "locally equivalent to general relativity but includes an extra boundary variable, unimodular time,
  whose difference between hypersurfaces measures the enclosed 4-volume".
- Methode: "we discretise Henneaux-Teitelboim gravity using the methods of Euclidean Regge calculus".
- Ergebnisse laut Abstract: In einem symmetriereduzierten Modell der Regge-Kosmologie werden fruehere Ergebnisse
  reproduziert, und "the continuum limit can be naturally defined using unimodular time rather than proper time". Ausserdem
  soll der Ansatz "the comparison of general simplicial triangulations, beyond highly symmetric discretisations, to the
  continuum" erlauben.
- I begruendet die euklidische Wahl mit "for simplicity" (S. 1). Motivation: In einer Quantenfassung waere T ein Operator auf
  einem Rand-Hilbertraum (S. 2).

**II A (S. 3-5): HT-Wirkung und unimodulare Zeit.**
- Gl. (1): sqrt|g| = d_mu T^mu.
- Gl. (2): S = (1/16 pi G) Int [sqrt|g| R - 2 Lambda (sqrt|g| - d_mu T^mu)] plus GHY-Randterm. Lambda ist hier ein
  Lagrange-Multiplikator-Feld.
- Gl. (3): Eichfreiheit T^mu -> T^mu + omega^mu mit d_mu omega^mu = 0, "instead of four new degrees of freedom, we really
  only have one". Bei periodischem t ist die Eichung T^i = 0 "generally not possible".
- Gl. (4): T_i = Int_Sigma_i d^3x n_mu T^mu. Gl. (5): Das 4-Volumen zwischen zwei Hyperflaechen ist T_(i+1) - T_i.
- Im Euklidischen messe T_i keine Zeit, sei aber "a preferred evolution parameter"; "the definition of unimodular time
  presupposes a fixed choice of foliation [44]" ([44] = Kuchar 1991).
- Gl. (6): Ein kompaktes Gebiet ohne Rand hat Volumen null, "the metric must be degenerate everywhere". S. 5: Auch Sigma x
  S^1 ("periodic in 'time'") ist ueberall entartet, Gl. (7). Nicht entartet geht nur "as long as there is at least one
  non-compact direction. In that case, the total volume is infinite and unimodular time is not well-defined."

**II B (S. 5-7): FLRW-Minisuperraum.**
- Gl. (8) bis (11) fuer beide Signaturen (s = +-1). Gl. (15) T' = V0 N a^3, Gl. (16) Lambda' = 0.
- Setzt man (15) in die Wirkung ein, verschwindet Lambda; das sei falsch. Richtig sei (15) als Eichfixierung mit T als
  Parameter: N = 1/(V0 a^3), Gl. (18) S_gf = 3 Int dT [k/a^2 + s V0^2 a'^2 a^4], "a fully gauge-fixed theory with no
  remaining coordinate freedom".
- Gl. (21) bis (23): euklidische Loesungen. Fuer Lambda > 0 gibt es zu gegebenen Randwerten zwei Loesungen.

**III A (S. 7-9): Regge.**
- Gl. (24): Regge-Wirkung mit Hartle-Sorkin-Randterm; Gl. (25): Bewegungsgleichungen (Schlaefli).
- Konformfaktor-Problem: Bei Volumen null skaliert die Wirkung wie l^2 und wird "arbitrarily negative" (S. 9).

**III B (S. 9-12): Henneaux-Teitelboim-Regge (HTR).**
- Gl. (27): S_HTR = Summe_(t innen) a_t eps_t - Summe_sigma Lambda_sigma [V_sigma(l) - Summe_(tau in sigma) T_sigma^tau]
  + Summe_(tau innen) mu_tau Summe_(sigma um tau) T_sigma^tau + Summe_(t Rand) a_t eps*_t.
- Variablen: zwei Variablen je Tetraeder, T_sigma^tau = -T_sigma'^tau.
- Variation:
  - (28): Summe_sigma T_sigma^tau = 0.
  - (29): Lambda_sigma + mu_tau = 0, also ist Lambda je Zusammenhangskomponente global.
  - (30): V_sigma = Summe_tau T_sigma^tau.
  - (31): Eichfreiheit xi mit verschwindenden Summen.
  - (32): die Regge-Gleichungen mit globalem Lambda.
- (33): Ein geschlossener Komplex hat Gesamtvolumen null, "every 4-simplex then has a vanishing volume".
- (34): T_i = (-1)^i Summe_(tau in Sigma_i) T_sigma^tau.
- (35): Kleben zweier Komplexe definiert T auch auf inneren Hyperflaechen, "particularly relevant if we want to add more
  and more intermediate time steps".
- "The definition of unimodular time is independent of the discrete structure in between the hypersurfaces"; (36) V_T =
  T2 - T1.
- S. 12: EDT mit fester S^4 "seems incompatible" mit HTR; CDT habe eine eingebaute Blaetterung und Eigenzeit. Weil T auf
  den Raendern lebt, "one can impose a boundary condition of how much time elapses between two hypersurfaces".

**IV (S. 13): Zwei Modelle mit gleichem Rand.**
- Rand dDelta4 u dDelta4: zwei 5-Zellen mit je gleichen Kantenlaengen l1 bzw. l2.
- T_cos: 5 Frusta sigma = tau x I, wie bei Liu/Williams 2016b [33] (euklidisch) und Dittrich/Gielen/Schander 2022 [5]
  (Lorentz).
- T_sim: echte 4-Simplizes. x_i wird mit allen y_j ausser y_i verbunden.

**IV A (S. 13-19): Frustum-Modell.**
- Eine Innenlaenge m, Hoehe h; Gl. (38): V44 = h (l1^3 + l1^2 l2 + l1 l2^2 + l2^3)/(24 sqrt2).
- Zeitlimes nach [5] (Gl. 48): l2 -> l + l' dt, T2 -> T + T' dt, h -> N dt. Raeumlich wird nicht verfeinert ("Spatially,
  we do not take the limit of a finer triangulation", S. 16).
- Skalenfaktor ueber das Volumen (l = 3,224 a_V) oder die Kruemmung (l = 2,286 a_R), Gl. (49).
- Lagrange-Funktion (51)/(52): wie [5] bis auf das Vorzeichen von l'^2 (euklidisch) und den neuen Term Lambda T'.
- Tab. I (S. 17), Koeffizienten c~1 / c~2 / c~3 / c~4 des Kontinuums 1 / 1 / 1/3 / 1/(6 pi^2):
  - a_V: 1,410 / 1,916 / 1/3 / 1/(6 pi^2)
  - a_R: 1 / 0,683 / 0,119 / 1/(6 pi^2)
  - "Our 5-cell model is not a very good approximation, as the difference between the continuum factors and ours is of
    the same order as the factors"; Verweis auf Tab. 3 von [5] (600-Zelle).
- Gl. (55) Hamilton-Bedingung wie [33] (bis auf Vorzeichen); Gl. (56) "does not seem to agree with the result in [33]"
  (S. 17).
- Gl. (57)/(58): Nur die Randgroesse DeltaT bleibt. Anfangs- und Endflaeche lassen sich nur fuer l1 = l2 = 0 identifizieren
  (S. 18).
- Unimodularer Zeitlimes (59)/(60): DeltaT -> dT gibt h = 6 sqrt2 dT/(5 l^3), "equivalent to gauge fixing ... using N =
  6 sqrt2/(5l^3)". Gl. (61) L = 3 [c1/a^2 + c2 a^4 a'^2].
- Tab. II (S. 18), c1 / c2: Kontinuum 1 / 4 pi^4 = 389,636; a_V 1,410 / 746,470; a_R 2,804 / 94,964.
- Gl. (62): dieselbe Vorschrift in den Kantenlaengen m, ohne Hoehe.
- Lorentz-Bemerkung (S. 19): Bei Nullkanten heisst Laenge null nicht 4-Volumen null; das 4-Volumen "could alleviate some
  of these subtleties".

**IV B (S. 19-26): Simpliziales Modell.**
- Tab. III/IV: Zaehlung und Inzidenzen; 5 + 10 + 10 + 5 = 30 4-Simplizes (sigma41, sigma32, sigma23, sigma14).
- Eine Innenlaenge m; T je Simplextyp gleich angenommen (S. 21). Gl. (77): T2 = T1 + 5 V41 + 10 V32 + 10 V23 + 5 V14.
- Die Hoehen der vier Simplextypen (78) koennen nicht zugleich verschwinden, daher "no straightforward continuum limit".
- Abb. 6 (Lambda = 0; 0,1; 1; l1 = 1; Umrechnung a_V): "Both ... clearly differ from the continuum solution"; das
  simpliziale Modell "agrees a bit better".
- Untergrenzen: l_min = 4 l1 bei Lambda = 0, Gl. (79), Ursache ist ein entartendes sigma14 (2D-Analogon Abb. 7: l2 = 2 l1).
  Bei Lambda = 0,1 liegt l_min bei etwa 2,8, bei Lambda = 1 bei etwa 2,4; dort ist die Grenze "not a hard cut off".
- l_max etwa 5,35 gegen 5,583 im Kontinuum (Lambda = 1).
- Von zwei Kontinuumsloesungen (Lambda > 0) findet die Numerik nur eine: "the discretisation eliminates one of the two
  solutions".
- Abb. 9: Mit zwei Innenlaengen m1, m2 gibt es (in 2D) kein Minimum und einen Kontinuumslimes.

**V (S. 26-28): Schluss und Ausblick.**
- Klassisch "mostly the same as the ones of standard Regge calculus". Unterschiede: Rolle von Lambda und "compact
  spacetimes without boundary must have zero 4-volume".
- Das simpliziale Modell sei ein "proof of concept that unimodular Regge calculus works in a general simplicial setting
  without the need to impose symmetries" (S. 27). Gerechnet wurde es aber mit symmetrischen Laengen und T je Typ [ES].
- "the use of unimodular time as a notion of time does not correspond to a gauge fixing ... diffeomorphism invariance is
  broken ([58, 59]). The boundary unimodular time gives us a diffeomorphism-invariant way of talking about time, which
  survives in the discrete setting."
- Ausblick:
  - Quanten: Ueberlagerung von Lambda, T als Operator.
  - Lorentz: "the strictly positive 4-volume provides a well-defined, monotonic evolution parameter".
  - Flaechen-Regge [60], Simplizes konstanter Kruemmung [61].
  - feinere Triangulierungen "perhaps along the lines of [5]".
- Literatur: Unruh 1989 [39] und Sorkin 1994 [40] stehen nur als Formulierungen in der Liste, Kuchar 1991 als [44].
  Unruh/Wald 1989 fehlt. Dank an B. Dittrich.

**Gegenprobe an der Quelle [M].** Die Umrechnungen und Grenzen der Arbeit stimmen:
- l = (12 sqrt2 pi^2/5)^(1/3) a_V = 3,2235 a_V
- l = 12 pi^2/(20 (2 pi - 3 arccos(1/3))) a_R = 118,435/51,806 a_R = 2,2861 a_R
- l_max = 3,224 sqrt(3) = 5,584 bei Lambda = 1
- Gl. (79): sin(theta/2) = sqrt(3/8) = sqrt6 l1/l2, also l2 = 4 l1
- Tab. II: Kontinuum c2 = V0^2 = (2 pi^2)^2 = 4 pi^4
- Tab. I stimmt Zahl fuer Zahl mit DGS 2022 Tab. III (S. 28) ueberein. Dort steht fuer die 600-Zelle 1,020 / 1,027 / 1/3
  (a_V) und 1 / 0,967 / 0,314 (a_R) [S].

## 4. Urteile GR1 bis GR7 (gegen den unveraenderten Wortlaut der Karte)

| Nr | Vorhersage (woertlich) | Wahrsch. | Urteil | Beleg |
|---|---|---|---|---|
| GR1 | [S Abstract] Die Arbeit diskretisiert Henneaux-Teitelboim-Gravitation mit euklidischem Regge; die unimodulare Zeit ist eine Randgroesse, zu Lambda konjugiert, und ihr Unterschied ist das eingeschlossene 4-Volumen (Summe der 4-Simplex-Volumina) | 90 % | **eingetroffen** | Abstract: "using the methods of Euclidean Regge calculus", "extra boundary variable, unimodular time, whose difference between hypersurfaces measures the enclosed 4-volume" [S Abstract]; III B Gl. (34), (36): V_T = Summe_sigma V_sigma = T2 - T1 (S. 11-12) [S]. Das Wort "konjugiert" steht nicht im Text (grep "conjugat": 0); es folgt aus dem Term Lambda (T2 - T1), Gl. (47), bzw. Lambda T', Gl. (11), (50) [M] und steht fuer HT allgemein bei Kuchar 1991 [S Abstract] und Isham 1992 Gl. (4.4.2) [S] |
| GR2 | [P] Getestet wird nur in symmetriereduzierten Modellen aus 5-Zellen-Schichten; die Ergebnisse stimmen mit frueherer Literatur ueberein | 80 % | **im Kern eingetroffen**, zweiter Halbsatz nur teilweise | Beide Modelle: eine Schicht zwischen zwei 5-Zellen, gleiche Laengen l1, l2, m (IV, S. 13); im simplizialen Modell T je Simplextyp gleich (S. 21) [S]. Uebereinstimmung: Lagrange-Funktion wie [5] bis auf die erwarteten Unterschiede, Tab. I = DGS Tab. III [S], Hamilton-Bedingung wie [33]. Abweichungen: Gl. (56) "does not seem to agree with the result in [33]" (S. 17); bei Lambda > 0 fehlt eine der zwei Kontinuumsloesungen (S. 24); fuer das simpliziale Modell gibt es keine Vergleichsliteratur |
| GR3 | [H] Die Arbeit behandelt weder Lorentz-Signatur noch Materie noch ausbreitende Schwerewellen | 80 % | **eingetroffen** (fuer den diskreten Teil) | Diskret nur euklidisch (III A S. 8; V S. 26) [S]. Lorentz nur im Kontinuumsteil II (s = +-1, S. 4-6) und als Ausblick (S. 19, 28). "matter" nur in einem Literaturtitel ([29]), "wave" 0 Treffer; beide Modelle homogen [S, grep] |
| GR4 | [H] Die Bedingung "geschlossene Raumzeit ohne Rand hat 4-Volumen null" macht zeitlich periodische (euklidisch geschlossene) Zerlegungen in der unimodularen Fassung zu Sonderfaellen ohne Volumen; die Arbeit sagt das so oder gleichwertig | 60 % | **eingetroffen** | II A Gl. (6), S. 4; S. 5: Sigma x S^1, "periodic in 'time'; such spacetimes must have a metric that is degenerate everywhere", Gl. (7); III B Gl. (33), S. 11: "every 4-simplex then has a vanishing volume"; IV A S. 18: Schliessen nur fuer l1 = l2 = 0 [S]. Zusatz: Mit einer nicht kompakten Richtung ist Periodizitaet erlaubt, nur ist T dann "not well-defined" (S. 5). Die "Bedeutung" der Karte trifft daher nur ein kompakt geschlossenes T^4, nicht die Bloch-Rechnung auf dem unendlichen Gitter (Abschn. 5, Frage 3) [M] |
| GR5 | [H] Der Kontinuumslimes wird bei festem Unterschied der unimodularen Zeit (festem 4-Volumen zwischen den Raendern) definiert, und die Konvergenz ist nur im reduzierten Modell gezeigt | 70 % | **nicht eingetroffen** | Der Limes ist ein Zeitlimes mit DeltaT -> dT, Gl. (59), nicht festes DeltaT; raeumlich keine Verfeinerung (S. 16). Konvergenz wird nirgends gezeigt: Abweichungen "of the same order as the factors" (S. 17, Tab. I, II). Das simpliziale Modell hat keinen Limes (S. 22, 24, 27) [S] |
| GR6 | [H] Die Arbeit gibt ein Rezept, mit dem man auf einer allgemeinen, nicht symmetrischen Zerlegung die unimodulare Zeit als Uhr verwenden kann (nicht nur als Randdatum im Pfadintegral) | 40 % | **teilweise** | Ja: Definition fuer beliebige Komplexe, Gl. (27), (34)-(36); Kleben ergibt T auf Zwischenflaechen, Gl. (35); "independent of the discrete structure in between" (S. 12); alles klassisch, kein Pfadintegral [S]. Nein: kein Test auf einer unsymmetrischen Zerlegung (T_sim mit einer Laenge m, T je Typ gleich, S. 20-21); kein Rezept, wo der Zuwachs hinkommt; "clock" 0 Treffer. Nach Kuchar legt T allein keine Hyperflaeche fest [S Abstract] |
| GR7 | [L] Die Einwaende von Unruh/Wald 1989 bzw. Kuchar 1991 (unimodulare Zeit loest das Zeitproblem der Quantengravitation nicht) werden in der Arbeit erwaehnt | 50 % | **teilweise**; die Klammer ist fuer Unruh/Wald sachlich falsch | Kuchar 1991 steht als [44] im Text, und zwar mit seinem Kernpunkt in einem Satz: "the definition of unimodular time presupposes a fixed choice of foliation [44]" (II A, S. 4). Die Folgerung "loest das Zeitproblem nicht" fehlt, ebenso jede Diskussion [S]. Unruh/Wald 1989 fehlt im Literaturverzeichnis. Unruh/Wald sind Urheber des Vorschlags, nicht Gegner: "we make a proposal ... general relativity with an arbitrary, unspecified cosmological constant. In minisuperspace models, this proposal yields a quantum theory with satisfactory interpretive properties" [S Abstract, Abruf 2]; ebenso Smolin 2010 ("the proposal of Unruh, Wald and Sorkin") [S Abstract] und Isham 1992 S. 62 [S] |

Bilanz: 3 eingetroffen (GR1, GR3, GR4), 1 im Kern eingetroffen (GR2), 2 teilweise (GR6, GR7), 1 nicht eingetroffen (GR5). Gemessen an den
Wahrscheinlichkeiten: Die hoch angesetzten GR1 bis GR4 halten. GR5 (70 %) faellt, weil die Arbeit keine Verfeinerung rechnet.
Die Praemisse von GR7 war falsch.

## 5. Antworten auf die Fragen der Karte

**Frage 1: Was wird definiert und gerechnet? Lambda, Randdaten, diskrete Wirkung.**
- Wirkung: Gl. (27), siehe Abschn. 3.
- Lambda: je 4-Simplex ein Multiplikator Lambda_sigma; durch Gl. (29) global, also eine Integrationskonstante [S].
- Randdaten:
  - Kantenlaengen der Randflaechen (in den Modellen l1, l2) und die Rand-T.
  - Nur DeltaT ist eichinvariant. Ein Eichfluss von Sigma1 nach Sigma2 verschiebt T1 und T2 gleich, ein Fluss innerhalb
    einer Randflaeche verteilt ihre T um [M aus Gl. 31].
  - Die Rand-T werden nicht variiert, sonst folgte Lambda = 0 [M].
- In den Modellen schrumpft der T-Teil auf -Lambda V_gesamt + Lambda (T2 - T1), Gl. (47).
- Gerechnet werden nur klassische Loesungen (Abschn. 3, IV).

**Frage 2: Modelle und Ergebnisse.**
- Zwei Modelle mit 5-Zellen-Raendern: Frusta und 30 echte 4-Simplizes.
- Frustum-Modell:
  - Zeitlimes ueber die Hoehe oder ueber DeltaT, beide mit gleichem Ergebnis (S. 19).
  - Koeffizienten um Faktoren daneben (Tab. I: 1,410 und 1,916 statt 1; Tab. II: 746,5 statt 389,6 bei a_V).
- Simpliziales Modell:
  - kein Limes; l_min = 4 l1 bei Lambda = 0
  - "agrees a bit better" (Abb. 6); l_max 5,35 statt 5,583
  - eine von zwei Loesungen verloren
- Konvergenz wird nicht gezeigt. Die 600-Zelle liegt bei DGS 2022 auf 2 bis 3 % beim Volumenabgleich und bis 6 % beim
  Kruemmungsabgleich (Tab. III, S. 28) [S]. Eine unimodulare 600-Zellen-Fassung ist damit klassisch vorab ableitbar [M].

**Frage 3: "4-Volumen null fuer geschlossene Raumzeiten": Herleitung und Folgen.**
- Herleitung [S]:
  - Kontinuum: V = Int sqrt|g| = Int d_mu T^mu, und nach Stokes ist das Randintegral bei leerem Rand null (Gl. 6).
  - Diskret: Jedes Tetraeder kommt in Summe_sigma Summe_tau T_sigma^tau zweimal mit entgegengesetztem Vorzeichen vor
    (Gl. 33).
- Kern [M]: HT verlangt, dass die Volumenform exakt ist (sqrt|g| d^4x = d(3-Form)). Auf einer geschlossenen 4-Mannigfaltigkeit
  integriert eine exakte 4-Form zu null, eine nicht entartete Volumenform aber nie. Darum bleibt nur Entartung.
- Folgen laut Arbeit [S]:
  - Metrik ueberall entartet, jedes 4-Simplex mit Volumen null.
  - Sigma x S^1 (periodische Zeit) ebenso.
  - EDT mit fester S^4 "seems incompatible".
  - Frustum-Modell: Schliessen nur fuer l1 = l2 = 0.
  - Periodisch mit einer nicht kompakten Richtung ist erlaubt, nur ist T dann nicht definiert.
- Folgen fuer uns [M/ES]:
  - **T^3 mal Zeitintervall** (Grundgleichung, PACHNER-TAKT-1-Schichten) ist erlaubt.
  - **T^4** als echtes HTR-Modell hat keine nicht entartete Loesung.
  - **Bloch-Rechnungen** (REGIME-K-1: periodisch in der Zeit, Bloch-Phasen in allen vier Richtungen [P]) stellen das
    unendliche periodische Gitter dar. Dort sind die HTR-Gleichungen fuer k != 0 die Regge-Gleichungen mit globalem
    Lambda (Gl. 32), also unveraendert. Das Paar (Lambda, T) haengt nur an der Nullmode. Als Uhr dient dort die Rate:
    4-Volumen je Zelle und Takt, V_c = tau [P].

**Frage 4: Lorentz, Materie, Schwerewellen, kanonisch/Zeltstangen.**
- Lorentz:
  - nur im Kontinuumsteil II und als Ausblick (S. 19: Nullkanten; S. 28: "strictly positive 4-volume provides a
    well-defined, monotonic evolution parameter") [S].
  - Ob das 4-Volumen in Lorentz-Regge tatsaechlich monoton ist, wird nicht gezeigt; mit gekippten Zeltstangen
    (Rueckwaertszuege) sind die Beitraege vorzeichenbehaftet [M].
- Materie: nein. Schwerewellen: nein; beide Modelle sind homogen [S].
- Kanonisch:
  - Nur der Vergleich der Hamilton-Bedingung mit [33] (S. 17). Es gibt keine kanonische Fassung von HTR, keine Zeltzuege,
    keine Pachner-Zuege (Treffer nur im Literaturtitel [7]) [S].
  - Die kanonische HT-Form steht bei Isham 1992, Gl. (4.4.2) [S]: lambda + |g|^(-1/2) H_perp(x) = 0.

**Frage 5: Einwaende und Gegenpositionen.**
- **Kuchar 1991** [S Abstract]: "the cosmological time labels only equivalence classes formed by hypersurfaces separated by a
  zero four-volume, while individual spacelike hypersurfaces within an equivalence class are physically irrelevant ...
  unless complemented by a hypertime variable, cosmological time does not uniquely set the conditions for measuring
  geometric variables either in the classical or in the quantum theory."
- **Isham 1992**, Abschn. 4.4, S. 62-63 [S], Kuchars Ergebnis im Einzelnen:
  - Die richtige Schroedinger-Gleichung ist (4.4.4) mit dem gemittelten Hamilton-Operator.
  - Dazu bleiben die Zwangsbedingungen (4.4.5) [|g|^(-1/2) H_perp(x)]_a Psi = 0, mit denen der Operator der 3-Geometrie
    nicht vertauscht. Daher ist "the interpretation of Psi(tau, g] as a probability distribution for g ... not tenable".
  - Geometrischer Grund: Zwei Einbettungen, die sich um ein 4-Volumen null unterscheiden, trennt tau nicht, "something
    that can happen easily in a spacetime with a Lorentzian signature".
- **Unruh/Wald 1989** [S Abstract]: Sie sind die Befuerworter, mit Vorbehalt: "unlikely that this theory will admit
  sufficiently many observables for general spacetimes". Ihr Uhren-Satz richtet sich gegen dynamische Zeitvariablen: "no
  dynamical variable can correlate monotonically with the Schroedinger time parameter t".
- **Neuere Arbeiten 10/2024 bis 10/2026** (Abruf 4, 5; 12 bzw. 2 Treffer) [S Abstract]:
  - Neun der zwoelf Treffer nutzen T als Uhr, alle in symmetriereduzierten oder zweidimensionalen Modellen: Kosmologie,
    kugelsymmetrische Schwarze Loecher, 2D-JT, die Arbeit selbst. Die uebrigen drei sind formal (2412.16139,
    2512.18753) bzw. Supergravitation (2412.05365).
  - Gielen/Neves 2412.01907: "the fundamental clash between general covariance and unitarity" (der de-Sitter-Horizont
    wird durch die flache Scheibung zum Sonderort).
  - Nesterov/Lyamkina 2412.16139: HT-Form verallgemeinerter unimodularer Gravitation mit "spatial nonlocality".
  - Keine Arbeit beantwortet Kuchar fuer inhomogene Raumzeiten; keine nutzt T als Uhr auf einem Gitter. Urteil: **nach
    Recherchestand nicht belegt**, nicht "widerlegt".
- **Die Arbeit selbst:** ein Satz mit [44], keine Diskussion; im Gegenteil wirbt V fuer T als
  "diffeomorphism-invariant way of talking about time" [S].

**Frage 6: Finns Netz.** Ausfuehrlich in Abschn. 6. Kurz:
- Der Takt kann die unimodulare Zeit sein, global, und in REGIME-K-1 ist er es schon.
- Oertlich nicht: Die oertliche Regel ist f = -1, die Teil-T sind Eichung, und T legt die Flaeche nicht fest.
- Grundgleichung: Lambda wird ein globales Paar mit T; K = 0 und laufende T schliessen sich auf dem Torus aus.
- Billiger Netztest: Karte K1.

## 6. Einordnung fuer Finns Netz [ES/H, mit M wo gerechnet]

### 6.1 Takt als unimodulare Zeit: global ja, oertlich nein

- **Zeltzug und 4-Volumen [M]:**
  - Wird Ecke v um die Hoehe h_v gehoben (flach, senkrecht), entsteht je Tetraeder ihres Sterns ein 4-Simplex mit
    Volumen (1/4) h_v V_tet (so auch REGIME-K-1, PLAN 2.2 [P]). Ein Zug fuegt also dV_v = (1/4) h_v Vol3(Stern v) hinzu.
  - Jedes Tetraeder hat 4 Ecken, also Summe_v Vol3(Stern v) = 4 V_Sigma. Heben alle Ecken einmal um h, waechst das Volumen
    um h V_Sigma; das ist das Kontinuum N dt Int sqrt q.
- **Global [S + M]:**
  - T ist die Summe der Fluesse durch eine ganze Randflaeche (Gl. 34). Die einzelnen T_sigma^tau sind ein Fluss auf dem
    dualen Graphen: Quelle V_sigma je Simplex (Gl. 30), Erhaltung auf inneren Tetraedern (Gl. 28). Kreisfluesse sind
    Eichung (Gl. 31).
  - In T_sim: 30 Simplizes, 70 innere und 10 Randtetraeder (5 x 30 = 2 x 70 + 10), Zyklenrang 70 - 30 + 1 = 41 [M aus
    Tab. III; Euler 10 - 40 + 80 - 80 + 30 = 0].
  - **Die unimodulare Zeit ist in HTR exakt global; keine oertliche Teilsumme der T ist eichinvariant** (nur Summen ueber
    ganze Randflaechen, Gl. 31, 34) [M aus S].
- **Kuchars Form = gleiche Zeltstangen [S + M]:**
  - Isham Gl. (4.4.4) entspricht einer Entwicklung mit raeumlich gleichem Lapse N = 1/V, damit dtau = Int N sqrt g = 1
    [M aus S].
  - Diskret sind das gleiche Zeltstangen h = dT/V_Sigma. REGIME-K-1 ("Ein Takt hebt jede Ecke einmal um tau", 4-Volumen
    V_c = tau je Zelle und Takt [P]) rechnet damit im periodischen Fall schon die globale unimodulare Zeit.
  - Neu ist hier nur die Benennung, keine Rechnung.
- **Oertlich: drei Gruende dagegen:**
  1. Die Teil-T sind Eichung (oben) [M aus S].
  2. T legt die Hyperflaeche nicht fest (Kuchar [S Abstract]): Alle Zeltstangen-Verteilungen mit gleichem Gesamtzuwachs
     liegen in derselben Klasse.
  3. Die Regel "jeder Zug gleiches 4-Volumen" ist schlecht gestellt (6.2) [M, Kriterium S].
- **Im Diskreten verschaerft [ES]:**
  - Im Kontinuum sind Flaechen derselben Klasse nach Kuchar "physically irrelevant".
  - Auf dem gekruemmten Netz sind Eckverschiebungen keine exakte Eichung mehr (Bahr/Dittrich [P]). Dann sind
    verschiedene Zeltstangen-Verteilungen gleicher Klasse schwach physikalisch verschieden.
  - PACHNER-TAKT-1 hat genau so etwas gemessen: Der Kommutator AB gegen BA (gleiche Raender, verschiedene
    Zwischenflaechen) faellt wie eps (a/L)^2,25 [P]. Ob die Uhr DeltaT selbst ebenso reihenfolgeabhaengig ist, prueft Karte
    K2.

### 6.2 Eine Linie fuer die Takt-Regeln mit volumenabhaengiger Zeltstange (Regel 6: Kopplung statt Bauteil)

- **Herleitung [M]:**
  - Shift null, ADM: d(ln sqrt q)/dt = -N K. Fuer N = C q^p folgt dN/dt = -2p N^2 K. Das ist Bona-Masso
    dN/dt = -N^2 f K mit **f = 2p**.
  - Probe: harmonisch, N = h(x) gamma^(1/2), ist f = 1 (Alcubierre u. a. 2003, Gl. 3.9 [S]).
- **Linearisierung um den flachen ruhenden Raum (Lorentz, Vakuum, Lambda = 0) [M]:**
  - sqrt q = 1 + s, ds/dt = -K, dK/dt = -Laplace(dN).
  - Oertlich unimodular (N = 1/sqrt q, dN = -s): d2s/dt2 = -Laplace(s), je Mode d2s/dt2 = +k^2 s, also **s ~ exp(|k| t)**.
    Die Kontinuumsformel gibt bei k = pi/a die Rate pi/a; den Gitterwert misst erst K1.
  - Harmonisch (dN = +s): Wellengleichung.
  - Gleiche Zeltstangen (dN = 0): ds/dt konstant, also hoechstens lineares Wachstum.
  - Probe ueber eine reine Eichstoerung des flachen Raums (Zeitverschiebung phi mit Gegenshift): gleiches Ergebnis,
    d2phi/dt2 = -Laplace(phi). Alle Zwangsbedingungen bleiben dabei erfuellt (reine Eichung).
- **Kriterium [S]:** Alcubierre u. a. 2003, Gl. (2.3): v_g = alpha sqrt(f gamma^ii); fuer f < 0 "the wave speed would not be
  real and the equation would be elliptic instead of hyperbolic".
- **Die Linie [M; Fokussierung der geodaetischen Scheibung L]:**

| Takt-Regel (Zeltstange h_v) | Kontinuum | f | Verhalten |
|---|---|---|---|
| h_v ~ 1/Vol3(Stern v): jeder Zug gleiches 4-Volumen (oertlich unimodular) | N sqrt q = 1 | -1 | elliptisch, Anfangswertproblem schlecht gestellt (exp(\|k\| t)) |
| h_v gleich (REGIME-K-1, PACHNER-TAKT-1 G) | N = 1, geodaetisch | 0 | linear-sekulaer; nichtlinear Fokussierung [L] |
| h_v ~ Vol3(Stern v) | N = sqrt q, harmonisch | +1 | hyperbolisch, Eichgeschwindigkeit 1 |
| K = 0 erhalten (maximal) | Laplace N = W N | -> unendlich (bei beschraenktem dN/dt erzwingt f -> unendlich K -> 0 [M, heuristisch]) | elliptisch, instantan; auf dem Torus N = 0 (GRUNDGLEICHUNG Abschn. 4 [P]) |
| York, K = tau(t) | CMC | (eigene Bedingung) | braucht sich aenderndes Volumen [P] |

- **Folge [ES]:**
  - Die unimodulare Zeit steht senkrecht zu dieser Linie: Sie legt nur die Nullmode des Lapse fest (Summe_v dV_v = dT je
    Takt), nicht seine Verteilung.
  - Finns Takt braucht daher zwei Angaben: wie viel (global, unimodular) und wo (eine Regel auf der f-Linie, gut gestellt
    fuer f > 0).
  - Dass "die unimodulare Zeit den Kontinuumslimes ermoeglicht", ist kein Ursachensatz: Die Arbeit erreicht denselben Limes
    auf drei Wegen (Hoehe h -> N dt, DeltaT -> dT, Vorschrift (62) in m; S. 19). Gemeinsame Groesse ist der Lapse je Schritt
    [S + ES].

### 6.3 Folgen fuer die Grundgleichung (Lambda, K = 0, York-Zeit, Torus, Regime K)

- **Lambda als Integrationskonstante [S + M]:**
  - Kanonisch ersetzt HT die Hamilton-Bedingung durch lambda + |g|^(-1/2) H_perp(x) = 0 mit globalem lambda, konjugiert zu
    T (Isham Gl. 4.4.2).
  - Diskret fuer Fassung 2.2 [M]: H_v^(Lambda = 0) + Lambda Summe_t w_vt V_t = 0 an jeder Ecke mit **einem** Lambda.
    Gleichwertig: N0 - 1 oertliche Bedingungen (H_v / V_v gleich fuer alle Ecken, Kuchars 4.4.5) plus eine globale.
  - HT nimmt also genau die Nullmode der Hamilton-Bedingungen heraus und fuegt ein Paar (Lambda, T) hinzu. Das bestaetigt
    den Satz in Fassung 2.2, Abschn. 7 ("zusaetzliche Variablen, Zwangsbedingungen und Randdaten") [P].
  - Eine kleine Zahl sagt HT nicht vorher [P, S].
  - Auf dem flachen ruhenden Torus erzwingt die Hamilton-Bedingung Lambda = 0 [M].
- **K = 0 [M, aus P]:** Erhalt von K = 0 gibt -Int |grad N|^2 = Int W N^2. Fuer W >= 0, nicht ueberall null, folgt N = 0,
  also T' = Int N sqrt q = 0. **Maximale Scheibung und laufende unimodulare Uhr schliessen sich auf dem Torus jenseits
  linearer Ordnung aus.** Mit HT ist Lambda > 0 als Konstante der Daten moeglich; dann geht N != 0 nur, wenn 0 Eigenwert von
  Laplace - W ist. Lambda ist durch die Daten festgelegt und nicht dafuer abstimmbar, also nicht generisch [ES].
- **York-Zeit gegen unimodulare Zeit [P, Karte]:** Die York-Zeit ist auf dem ruhenden Torus konstant null; T laeuft dort
  mit Volumen mal Eigenzeit. Das steht schon in der Ableitbarkeitsprobe der Karte und ist nicht neu.
- **Torus [S + M]:** T^3 mal Intervall ist erlaubt (zwei Raender), T^4 in der HT-Fassung nicht (Volumen null). Fuer Finns Netz heisst das:
  Die Uhr braucht einen Anfang, oder sie wird als Rate je Zelle gelesen (periodisches Gitter).
- **Regime K (REGIME-K-1) [M]:** nicht betroffen (k != 0, siehe Frage 3).
  - Seine Zeltstangen sind f = 0 und global unimodular normiert.
  - RK3 (Hoehe mal 1,5) prueft nur die Skala, nicht die Verteilung.
  - Eine nach Eckenklassen verschiedene Hoehe waere die naechste Probe. Ob die vier Eckenklassen der B1-Kopie gleiche
    Sternvolumina haben, habe ich nicht geprueft.

### 6.4 Schon im Projekt gegen neu

- **Schon im Projekt [P], nicht neu:**
  - G1 bis G4 und "Neu fuer uns" der Leitung (04:38): Gl. 27, 29, 30, 36; zwei Modelle; Gl. 33; nur euklidisch; Randzeit
    keine Eichfixierung; Limes "analogous to fixing the lapse"; "Takt zaehlt Zellen" waere unsere Erweiterung.
  - WELTKRISTALL-L: volume time, 600-Zelle besser, "mostly the same".
  - Karte: T monoton auf dem ruhenden Torus, York null.
  - GRUNDGLEICHUNG 2.2: K = 0 auf dem Torus, unimodulares Lambda braucht Zusatzvariablen.
  - Bahr/Dittrich: flach exakt, gekruemmt gebrochen.
- **Neu durch diese Karte:**
  1. Unruh/Wald sind Befuerworter; Kuchars Einwand im Wortlaut und nach Isham, Gl. (4.4.4) und (4.4.5) [S].
  2. T ist im Diskreten exakt global, mit Flusseichung und Zyklenrang [M aus S].
  3. Die f-Linie der Takt-Regeln: oertlich unimodular f = -1, schlecht gestellt; gleiche Zeltstangen f = 0 und
     zugleich Kuchars Form [M, Kriterium S].
  4. Periodisch mit nicht kompakter Richtung ist erlaubt, daher ist REGIME-K-1 nicht betroffen [S + M].
  5. K = 0 und laufende T schliessen sich aus [M].
  6. Zahlen: Tab. I/II, l_min = 4 l1, l_max, verlorene zweite Loesung, DGS-600-Zelle 1,020/1,027 [S].
  7. Der "Kontinuumslimes" ist ein Zeitlimes ohne Verfeinerung [S].
  8. Die Behauptung "without the need to impose symmetries" steht gegen den gerechneten Ansatz [S + ES].
  9. Die 24-Monats-Lage: alle neun Uhr-Arbeiten symmetriereduziert oder 2D, keine Gitter-Uhr; Gielen/Neves "clash
     between general covariance and unitarity" [S Abstract].

### 6.5 Regime und Moderatoren (Regel 1)

| Widerspruch | Moderator | Regime A | Regime B |
|---|---|---|---|
| "T loest das Zeitproblem" (Unruh/Wald, Gielen-Kreis) gegen "nicht" (Kuchar) | Homogenitaet: Zahl der Hyperflaechen je T-Wert | Minisuperraum, eine Flaeche je T: T traegt (Unruh/Wald; die neun Uhr-Arbeiten 2024-26; beide Modelle der Arbeit) | inhomogen, unendlich viele Flaechen je T: T braucht Hyperzeit (Kuchar, Isham 4.4.5) |
| "Flaechen gleicher Klasse irrelevant" (Kuchar, Kontinuum) gegen "Zeitwahl im Diskreten nicht frei" (Gielen/Ried V) | Kruemmung und Diskretheit (Diffeomorphismen exakt oder gebrochen) | flach oder Kontinuum: reine Eichung | gekruemmtes Netz: schwach physikalisch (PACHNER-TAKT-1 D ~ eps (a/L)^2,25 [P]) |
| oertlich unimodulare Zeltregel gut oder schlecht | Signatur | euklidisches Zwei-Rand-Problem: Eichsektor wird zur Wellengleichung in tau, Resonanzen moeglich [M, H] | Lorentz-Anfangswertproblem: elliptisch, exp(\|k\| t) [M] |
| T existiert, ist null oder ist undefiniert | Topologie | mit Raendern: DeltaT = 4-Volumen | geschlossen kompakt: null (entartet); nicht kompakt periodisch: undefiniert, nur Rate [S] |
| 5-Zelle weit daneben, 600-Zelle gut | raeumliche Verfeinerung | 5-Zelle: Abweichungen bis etwa Faktor 4 (Tab. I, II) | 600-Zelle: 2 bis 6 % (DGS Tab. III) [S] |

### 6.6 Unterscheidungspunkte (Regel 2)

- **T reicht als Uhr (Unruh/Wald) gegen T braucht Hyperzeit (Kuchar):**
  - Sie laufen auseinander, sobald es mindestens zwei unabhaengige oertliche Lapse-Freiheiten gibt, also bei
    ungleichmaessigen Zeltstangen.
  - Im Minisuperraum sind sie empirisch nicht unterscheidbar. Auf Finns Netz ist die Stelle im Modell zugaenglich.
- **Randzeit diffeomorphismeninvariant im Diskreten (Gielen/Ried) gegen Uhr erbt die gebrochene Eichung:**
  - Sie laufen nur auf gekruemmten Randdaten auseinander, an der Reihenfolgeabhaengigkeit D_T von DeltaT (Karte K2).
  - Flach sind sie ununterscheidbar (D_T = 0 exakt [M]).
- **Oertlich gegen global unimodularer Takt:**
  - Auseinander nur bei kurzen Wellen im Lorentz-Fall: exp(|k| t) gegen beschraenkt (Karte K1).
  - In homogenen Modellen sind beide gleich; Gl. (60) der Arbeit ist beides zugleich.
- **HTR gegen Standard-Regge:**
  - Klassisch nur bei geschlossenen Komplexen (S^4, T^4, No-Boundary) und ueber die Rolle von Lambda; sonst gleiche
    Loesungen (V) [S].
  - Quantenmechanisch (Ueberlagerung von Lambda) nicht gerechnet. Fuer offene Komplexe sind sie klassisch empirisch nicht
    unterscheidbar.

## 7. Kartenvorschlaege (zwei)

### K1: UNIMODULAR-ZELT-1 (billiger Netztest): Welche Zeltstangen-Regel haelt die Scheibung stabil?

- **Frage:**
  - Wird jede Ecke um h_v ~ Vol3(Stern v)^(2p) gehoben, bleibt dann eine leicht verbeulte Scheibung des flachen
    Lorentz-Netzes stabil?
  - Geprueft werden p = -1/2 (jeder Zug gleiches 4-Volumen, oertlich unimodular), p = 0 (gleiche Stangen, wie REGIME-K-1)
    und p = +1/2 (harmonisch). Alle drei Regeln werden auf denselben Gesamtzuwachs dT je Takt normiert (global
    unimodular).
- **Aufbau:**
  - Netz: B1-Kopie aus PACHNER-TAKT-1/REGIME-K-1, raeumlich periodisch (L = 4 und 8 Zellen), eingebettet in den
    Minkowski-Raum.
  - Anfangsscheibe: t_v = eps cos(k x_v) mit eps = 1e-3 a und k = 2 pi n/L.
  - Ablauf: Takt = Durchlauf der vier Eckenklassen; jede Ecke wandert entlang der Normalen ihres Sterns um h_v. 50 Takte,
    mittlerer Hub 0,1 a.
- **Ob die Regge-Gleichungen das zulassen [M, vorab]:**
  - Im flachen Raum ist jede Eckenlage eine exakte Regge-Loesung mit Lambda = 0, denn alle Fehlwinkel verschwinden. Das
    gilt fuer alle drei Regeln.
  - Die Karte prueft also nur die Stabilitaet der Regel. Bei Kruemmung sind Zeltstangen nur noch schwach frei (Bahr/Dittrich
    [P]); dieser Teil gehoert zu K2 bzw. zur offenen Frage O3.
- **Ableitbarkeitsprobe:**
  - Vorab ableitbar [M, Abschn. 6.2]: Im Kontinuum, linear, gilt fuer p = -1/2 Wachstum exp(|k| t), fuer p = 0 hoechstens
    lineares Wachstum, fuer p = +1/2 eine Schwingung mit Eichgeschwindigkeit 1.
  - Nicht ableitbar und damit das Messziel: Gitterwerte bei k nahe pi/a, Einfluss der Reihenfolge der Eckenklassen, Zahl
    der Takte bis zur ersten nicht raumartigen Scheibenkante (nichtlinear).
  - Projekt-grep (pachner-takt-1, regime-k-1, takt-rand-4d-1, takt-umbenennung-l; Begriffe Sternvolumen, volumenabh,
    Vol3, harmonisch, unimodul): 0 Treffer. Gerechnet sind nur L (N_A = 0,3, N_B = 0,5) und G (gleich) in
    PACHNER-TAKT-1 sowie gleiches tau in REGIME-K-1 [P].
  - Lesart des Auftrags: Meint "jeder Schritt" den ganzen Takt, ist die Regel die globale Fassung (p beliebig, Summe
    normiert) und unbedenklich. Die Karte prueft beide Lesarten, weil p = -1/2 genau die Zug-Lesart ist.
- **Vorhersagen-Entwurf (vor jeder Rechnung zu bestaetigen):**

| Nr | Vorhersage | Wahrsch. |
|---|---|---|
| UZ1 | [M] p = -1/2: Die Beulenamplitude waechst exponentiell; bei k a <= 0,5 liegt die Rate je Eigenzeit innerhalb 20 % von k | 85 % |
| UZ2 | [H] p = -1/2: Bei k = pi/a liegt die Rate zwischen 0,3 pi/a und 1,0 pi/a | 55 % |
| UZ3 | [M] p = +1/2: Die Amplitude bleibt beschraenkt (Verhaeltnis groesster zu Anfangswert <= 1,5 ueber 50 Takte); die Schwingungsfrequenz liegt bei k a <= 0,5 innerhalb 20 % von k | 80 % |
| UZ4 | [M] p = 0: Die Amplitude waechst hoechstens linear in der Taktzahl | 80 % |
| UZ5 | [H] Die Reihenfolge der Eckenklassen aendert die Rate bei p = -1/2 um weniger als 10 % | 50 % |

- **Kontrollen:**
  - Bei eps = 0 bleibt die Scheibe fuer alle p flach (Amplitude <= 1e-12), und je Takt kommt genau dT hinzu (<= 1e-12).
  - Die Formel dV_v = (1/4) h_v Vol3(Stern v) wird gegen die direkte Summe der Simplexvolumina geprueft.
  - Fehlwinkel <= 1e-12.
- **Bedeutung:**
  - Trifft UZ1 ein, darf Finns Takt nicht "jeder Zug gleiches 4-Volumen" sein. Dann gilt "global unimodular plus
    Verteilung mit f > 0", am besten harmonisch.
  - Verfehlt UZ1, daempft das Gitter die Instabilitaet. Das waere ein echter Gitterbefund und braeuchte eine Erklaerung.
- **Aufwand:** reine Geometrie ohne Regge-Loeser, Kleintest-Spur (<= 10 min, cpu bzw. p4000 auf der .69).

### K2: UNIMODULAR-KOMMUTATOR-1: Haengt die unimodulare Uhr weniger von der Zugreihenfolge ab als die Randimpulse?

- **Frage:**
  - PACHNER-TAKT-1 misst fuer zwei Zeltzuege A, B in den Reihenfolgen AB und BA (gleiche Randlaengen, gekruemmte
    Randdaten) den Kommutator der Randimpulse: D ~ eps^0,998 (a/L)^2,25 [P].
  - Wie verhaelt sich dazu D_T = |DeltaT(AB) - DeltaT(BA)| / DeltaT mit DeltaT = Summe_sigma V_sigma (bis erste Ordnung in
    eps)?
- **Aufbau:**
  - vorhandener Code (linearisiertes euklidisches 4D-Regge, Schicht mit 48 Simplizes und 3 Innenkanten);
  - zusaetzlich die Volumensumme aus den geloesten Kantenlaengen;
  - Laeufe fuer L/a = 4, 8, 16, 32, beide Takte L und G, eps = 1e-3 und 1e-4.
- **Ableitbarkeitsprobe:**
  - Vorab [M]: Bei eps = 0 ist D_T = 0 exakt, denn AB und BA kacheln dieselbe Region des R^4. Das sieht auch PACHNER-TAKT-1
    so ("zwei Triangulierungen derselben flachen Region" [P]).
  - Eine innere Eckverschiebung aendert das Gesamtvolumen in erster Ordnung nicht [M]; D_T ist also eichfest.
  - Zusammenhang [M]: Auf der Loesung gilt V_gesamt = -dS/dLambda (Lambda geht nur ueber -Lambda Summe V_sigma ein,
    Gl. 24/27). D_T ist also die Lambda-Ableitung des Unterschieds der Hamilton-Jacobi-Funktionen von AB und BA, also die
    Antwort der Randimpulse auf Lambda. Darum ist D_T allgemein erster Ordnung in eps, ausser eine Symmetrie hebt es auf.
  - Nicht ableitbar: der Exponent von D_T in a/L.
  - Projekt-grep: In pachner-takt-1 ist das 4-Volumen nur als Realisierbarkeit ausgewertet ("kleinstes 4-Volumen"), nie als
    Differenz AB gegen BA [P].
- **Vorhersagen-Entwurf:**

| Nr | Vorhersage | Wahrsch. |
|---|---|---|
| UK1 | [H] D_T faellt mit (a/L)^q, q >= 2,75 (schneller als D): Die Uhr ist reihenfolgefester als die Impulse | 40 % |
| UK2 | [H] 1,75 <= q < 2,75 (wie D): Die Uhr erbt die gebrochene Eichung | 45 % |
| UK3 | [H] q < 1,75 | 15 % |
| UK4 | [H] D_T ist linear in eps (Verhaeltnis der Werte bei eps = 1e-3 und 1e-4 zwischen 9 und 11). Verfehlt heisst: D_T ist zweiter Ordnung, die Uhr also schon in erster Ordnung reihenfolgefest (staerker als UK1) | 75 % |

- **Kontrollen:** eps = 0 gibt D_T <= 1e-13; DeltaT stimmt mit dem analytischen Schichtvolumen ueberein; die bekannten
  Werte von D werden reproduziert.
- **Bedeutung:**
  - UK1 stuetzt auf unserem Netz Gielen/Rieds Satz, die Randzeit sei "a diffeomorphism-invariant way of talking about time,
    which survives in the discrete setting".
  - UK2 heisst: Kuchars Flaechen gleicher Klasse sind diskret physikalisch verschieden, und die Uhr selbst traegt den
    Fehler.
- **Aufwand:** Zusatzauswertung am eingefrorenen Code, nach der Kopie-Regel (Skript nie in place aendern).

## 8. Erwartungsverstoesse, Gegensweep, Negativliste, Kalibrierung, Offenes, Selbstanzeigen, Quellen

### 8.1 Erwartungsverstoesse (das Wichtigste zuerst)

1. **Unruh/Wald 1989 sind Befuerworter, nicht Gegner** (gegen die GR7-Klammer, die Ableitbarkeitsprobe der Karte und meine
   Erwartung vor Abruf 2).
   - Sie schlagen die Lambda-Zeit vor; im Minisuperraum sei sie zufriedenstellend, fuer allgemeine Raumzeiten gebe es
     vermutlich zu wenige Observablen [S Abstract]. Smolin 2010 [S Abstract] und Isham 1992 [S] bestaetigen das.
   - Der Einwand ist Kuchars: T etikettiert nur Klassen von Flaechen gleichen 4-Volumens.
   - Daraus folgen die zwei Regime mit dem Moderator Homogenitaet (6.5).
2. **"Jeder Schritt fuegt dasselbe 4-Volumen hinzu" ist als oertliche Regel schlecht gestellt.** Der Auftrag nennt die
   Regel "unimodulare Eichung" und fragt nur, ob die Regge-Gleichungen sie zulassen; im Flachen tun sie das exakt [M]. Meint
   "Schritt" den einzelnen Zeltzug, ist die Regel f = -1; meint er den ganzen Takt, ist sie die unbedenkliche globale Fassung.
   - Die Regel ist Bona-Masso mit f = -1; im Lorentz-Fall gilt exp(|k| t) [M]. Das Kriterium f > 0 steht bei Alcubierre
     u. a. 2003 [S].
   - Sauber ist nur die globale Fassung (fester Gesamtzuwachs je Takt) mit einer Verteilung f >= 0, gut gestellt fuer f > 0.
3. **Die Projektlage war groesser als die Karte** (L3): Die Leitung hatte den Volltext schon um 04:38 gelesen (G1 bis G4).
   Neu ist darum nur, was in 6.4 steht.
4. **Die Arbeit ist rein klassisch** (gegen meine Erwartung vor Abruf 1: Pfadintegral, Fourier-Paar Lambda/T, Sattelpunkte,
   No-Boundary). No-Boundary wird nicht behandelt, sondern ausgeschlossen (Volumen null; S^4 "seems incompatible").
5. **Euklidisch** (gegen meine Erwartung "Lorentz" vor Abruf 1; die Karte, GR1, lag richtig).
6. **Der "Kontinuumslimes" im Abstract ist ein Zeitlimes ohne raeumliche Verfeinerung**, mit Abweichungen der
   Groessenordnung 1. Deshalb faellt GR5.
7. **REGIME-K-1 rechnet schon die globale unimodulare Zeit in Kuchars Form** (gleiche Zeltstangen, V_c je Zelle und Takt).
   Die Gleichsetzung "Takt = unimodulare Zeit" ist im periodischen Fall eine Umbenennung, keine neue Physik [M, P].
8. **Die Arbeit behauptet mehr Allgemeinheit, als sie rechnet:** "without the need to impose symmetries" (V), gerechnet aber
   mit einer Innenlaenge m und T je Typ gleich.
9. Kleiner: Kuchar steht doch im Text, mit seinem Kernsatz als Voraussetzung (deshalb GR7 "teilweise" statt meines
   Zwischenurteils "nicht"). Abruf 3 brachte fast nur alte Treffer, systematisch half erst die arXiv-API. Abruf 6 fand eine
   Arbeit mit allgemeinem Exponenten des verdichteten Lapse; die unimodulare Form behandelt aber auch sie nicht.

### 8.2 Gegensweep-Befunde (Regel 4; Einzelheiten ARBEITSFELD Abschn. 2)

- **Geprueft:**
  - Rolle von Unruh/Wald: falsch angenommen.
  - Lesart der verstuemmelten Gl. (27): stimmt (-layout).
  - Zahlen der Arbeit: stimmen (Handproben, DGS Tab. III).
  - Fassung v1: gueltig.
  - Volumen-null-Zwang gegen Bloch-Rechnungen: nicht betroffen fuer k != 0 [S + M].
  - "Gleiche Zeltstangen = unimodular": nur global [M].
- **Nicht geprueft:**
  - Zeltstange (Kante) gegen Hoehe (Abstand): gleich nur senkrecht im Flachen.
  - f = 2p mit Shift != 0.
  - Reihenfolgeabhaengigkeit der oertlichen Regel.
  - Freiheit der Zeltstange bei Kruemmung (Barrett u. a. 1997 nur Abstract).

### 8.3 Negativliste (gesucht, nicht gefunden; nichts davon heisst "widerlegt")

- **In der Arbeit:** "clock", "conjugate", Materie, Wellen, diskrete Lorentz-Rechnung, Pfadintegral, raeumliche
  Verfeinerung, Zelt- oder Pachner-Zuege, Torus, No-Boundary-Rechnung, Unruh/Wald 1989 [S, grep].
- **Literatur 10/2024 bis 10/2026** (Abruf 4, 5):
  - keine weitere unimodulare Arbeit zu diskreter Gravitation in gr-qc;
  - keine Antwort auf Kuchar fuer inhomogene Raumzeiten;
  - keine Gitter- oder Zeltstangen-Uhr.
  - Urteil: nach Recherchestand nicht belegt.
- **Keine Quelle zur Lapse-Wahl N = 1/sqrt(q)** (Abruf 6, 7, 11). Die f = -1-Aussage ist meine Rechnung mit einem
  Kriterium aus der Quelle.
- **Kuchar 1991 Volltext** nicht gelesen (APS, nicht frei); Inhalt ueber Abstract und Isham.

### 8.4 Kalibrierung

- **(a) Gemessen:** nichts. Literatur und Schreibtisch; die Zahlen der Arbeit sind Rechnungen an zwei Spielzeugmodellen.
- **(b) Nuetzlich verdichtet:**
  - HTR = Regge plus ein globales Paar (Lambda, T) plus Flusseichung, T exakt global.
  - Kuchars Form = gleiche Zeltstangen.
  - Takt-Regeln mit volumenabhaengiger Zeltstange auf einer f-Linie.
  - Zwei Regime nach Homogenitaet.
- **(c) Gewachsene Gewissheit ohne neue Evidenz:**
  - "Finns Takt zaehlt Volumen" (WELTKRISTALL-L): Fuer "zaehlt" gibt es weiter keine Quelle; Volumina folgen aus
    Kantenlaengen, Zaehlen gilt nur bei gleichen Volumina [P G3].
  - "Global ja" stuetzt sich auf eine Umbenennung der REGIME-K-1-Konstruktion, nicht auf eine neue Rechnung.
  - Die f = -1-Aussage traegt den Kartenvorschlag K1 und ist nur eigene Handrechnung.
- **Warnzeichen:** Meine Sicherheit, dass die unimodulare Zeit Finns Takt "ist", sank im Lauf, waehrend sich die Frage
  verfeinerte (global/oertlich, Lorentz/euklidisch, homogen/inhomogen). Sie stieg also nicht; das ist das unbedenkliche
  Muster. Die Sicherheit in der f-Linie stieg allerdings nur durch eigene Rechnung.

### 8.5 Offene Fragen (wandern mit)

- O1: Gilt die f-Zuordnung mit Shift != 0 (Alcubierre u. a. Gl. 3.11-3.13)?
- O2: Haengt die oertlich unimodulare Zeltregel von der Zugreihenfolge ab (das Sternvolumen aendert sich mit den
  Nachbarzuegen)?
- O3: Bleibt die Zeltstange bei Kruemmung frei, oder legen die Regge-Gleichungen sie schwach fest (Bahr/Dittrich [P])?
- O4: Gibt es im euklidischen Zwei-Rand-Problem Resonanzen der oertlichen Regel [H]?
- O5: Kuchar 1991 im Volltext lesen.
- O6: Abb. 6 der Arbeit nur ueber Unterschrift und Text gelesen.
- O7: Haben die vier Eckenklassen der B1-Kopie gleiche Sternvolumina? Wenn nein, ist der REGIME-K-1-Takt oertlich nicht
  unimodular.
- O8: Ist das 4-Volumen einer Lorentz-Regge-Schicht mit gekippten Zeltstangen monoton, wie die Arbeit fuer Lorentz in
  Aussicht stellt?

### 8.6 Selbstanzeigen und Regelverstoesse

- **R1:** ein lokaler awk-Aufruf, als leerer Filter `awk 'NR<0'` hinter einem grep auf die DGS-Textdatei nach Abruf 9. Er
  gab nichts aus und aenderte nichts. Verstoss gegen "lokal keine python-, awk- oder perl-Aufrufe".
- **R2:** L1/L2 (Grundgleichung, Skalar-Sektor) vor dem Anlegen der Arbeitsdatei gelesen, ohne vorab notierte Erwartung.
- **R3:** Eine Zeitangabe stand kurz von Hand in ARBEITSFELD.md (R1-Zeile); sie wurde durch "nach Abruf 9" ersetzt und der
  Ersatz mit date protokolliert.
- **S1:** Werkzeug-Zusammenfassungen der WebSearch (Abrufe 3, 6, 11) sind nur [S Treffer]. Verwendet habe ich davon nur den
  Hinweis auf gr-qc/0303069; diese Arbeit habe ich dann an der Quelle gelesen.
- **S2:** Die f-Linie, die euklidischen Resonanzen und "K = 0 schliesst laufende T aus" sind Handrechnungen [M]; die
  Resonanzen sind nur [H].
- **S3:** Die Liste "neu" in 6.4 stuetzt sich auf greps nach "unimodul", "Bahr" und Zelt-Begriffen. Ein Befund unter
  anderem Wortlaut kann mir entgangen sein.
- Geschrieben nur in diesem Kartenordner. Keine Interpreter- oder Teststarts, kein VPN, kein Kontakt.

### 8.7 Quellen

**Gelesen [S]:**
- Gielen, S.; Ried, S. (2026): Unimodular boundary time for Regge calculus. arXiv:2610.03479v1.
  https://arxiv.org/abs/2610.03479. Kopie quellen/gielen-ried-2610.03479-abruf-20261005-122632.pdf (Abruf 1).
- Isham, C. J. (1992): Canonical quantum gravity and the problem of time. arXiv:gr-qc/9210011, Abschn. 4.4, S. 62-63.
  https://arxiv.org/abs/gr-qc/9210011 (Abruf 10).
- Alcubierre, M.; Corichi, A.; Gonzalez, J. A.; Nunez, D.; Salgado, M. (2003): A hyperbolic slicing condition adapted to
  Killing fields and densitized lapses. arXiv:gr-qc/0303069v2, Abschn. II, III. https://arxiv.org/abs/gr-qc/0303069
  (Abruf 7).
- Dittrich, B.; Gielen, S.; Schander, S. (2022): Lorentzian quantum cosmology goes simplicial. Class. Quant. Grav. 39,
  035012. arXiv:2109.00875, Tab. III (S. 28), Tab. IV (S. 36). https://arxiv.org/abs/2109.00875 (Abruf 9).

**Abstracts [S Abstract]:**
- Kuchar, K. V. (1991): Does an unspecified cosmological constant solve the problem of time in quantum gravity? Phys. Rev.
  D 43, 3332-3344. doi:10.1103/PhysRevD.43.3332. Ueber INSPIRE (Abruf 2, Datei quellen/A2-...json).
- Unruh, W. G.; Wald, R. M. (1989): Time and the interpretation of canonical quantum gravity. Phys. Rev. D 40, 2598.
  doi:10.1103/PhysRevD.40.2598. Ueber INSPIRE (Abruf 2).
- Smolin, L. (2010): Unimodular loop quantum gravity and the problems of time. arXiv:1008.1759 (PRD 84, 044047, 2011).
  https://arxiv.org/abs/1008.1759 (Abruf 8).
- Smolin, L. (2009): The quantization of unimodular gravity and the cosmological constant problem. arXiv:0904.4841 (PRD
  80, 084003). https://arxiv.org/abs/0904.4841 (Abruf 8).
- 24-Monats-Fenster (Abruf 4, quellen/A4-...xml):
  - Gielen, S.; Neves, R. B.: 2412.01907 (2024), https://arxiv.org/abs/2412.01907; 2607.27344 (2026),
    https://arxiv.org/abs/2607.27344.
  - Gielen, S.; Ried, S.: 2502.10104 (2025), https://arxiv.org/abs/2502.10104; 2509.18273 (2025),
    https://arxiv.org/abs/2509.18273.
  - Ried, S.: 2508.20794 (2025), https://arxiv.org/abs/2508.20794.
  - Alexandre, B.; Etkin, A.; Rassouli, F.-S.: 2501.17213 (2025), https://arxiv.org/abs/2501.17213.
  - Etkin, A.; Rassouli, F.-S.: 2601.07911 (2026), https://arxiv.org/abs/2601.07911.
  - Nesterov, D.; Lyamkina, K.: 2412.16139 (2024), https://arxiv.org/abs/2412.16139.
  - Smirnov, A. L.: 2512.18753 (2025), https://arxiv.org/abs/2512.18753.
  - Davies, P. C. W.; Magueijo, J. (erste zwei Namen der API-Antwort): 2606.02514 (2026),
    https://arxiv.org/abs/2606.02514.
  - Bossard, G.; Kleinschmidt, A.; Sezgin, E.: 2412.05365 (2024, Supergravitation, nur Namensgleichheit HT).
- 2607.03272 "Dark energy genesis" (2026, Abruf 5), https://arxiv.org/abs/2607.03272.
- Barrett, J. W.; Galassi, M.; Miller, W. A.; Sorkin, R. D.; Tuckey, P. A.; Williams, R. M. (1997): A parallelizable
  implicit evolution scheme for Regge calculus. Int. J. Theor. Phys. 36, 815. arXiv:gr-qc/9411008 (Abstract aus der
  Projektdatei kegel-4d-l/quellen/A1, kein Abruf).

**Suchtreffer [S Treffer]:**
- Abruf 3: https://arxiv.org/pdf/1008.1759, https://arxiv.org/pdf/gr-qc/9210011, https://arxiv.org/pdf/1007.0735,
  https://journals.aps.org/prd/pdf/10.1103/cmbb-cwlj, https://eprints.soton.ac.uk/499963/1/2501.17213v2.pdf.
- Abruf 6: https://arxiv.org/pdf/gr-qc/0210050, https://arxiv.org/pdf/gr-qc/0303069, https://ar5iv.arxiv.org/html/gr-qc/9609015.
- Abruf 11: https://arxiv.org/pdf/0710.4425, https://arxiv.org/pdf/gr-qc/0111023v1, https://arxiv.org/pdf/gr-qc/0603069v2,
  https://arxiv.org/abs/gr-qc/0601124.

**Projekt [P]:**
- ARBEITSFELD-claude-primary.md (Eintrag 04:38:04)
- RUNDE-37/weltkristall-l/{DOSSIER,ARBEITSFELD}.md
- RUNDE-49/GRUNDGLEICHUNG-SKIZZE-v2.2.md (Abschn. 2.2, 4, 7, 8)
- RUNDE-37/skalar-sektor-l/DOSSIER.md (Abschn. 4)
- RUNDE-37/regime-k-1/{KARTE,PLAN}.md
- RUNDE-37/pachner-takt-1/{PLAN,ERGEBNIS}.md
- gamma-netz-l, hodge-l (Bahr/Dittrich)
- RUNDE-45/quellen-leitung

## 9. Einfach gesagt

Gielen und Ried bauen die Schwerkraft aus kleinen vierdimensionalen Bausteinen und geben ihr eine Uhr: Die "unimodulare
Zeit" zaehlt, wie viel Raumzeit-Volumen zwischen zwei Momentaufnahmen liegt. Fuer Finns Netz heisst das: Der Takt kann
ein Zaehler sein, der sagt, wie viel Volumen pro Takt dazukommt, und unsere bisherigen Rechnungen mit gleich hohen
Zeltstangen tun genau das schon. Die Uhr sagt aber nicht, an welcher Ecke das Volumen dazukommt; diese Luecke hat Kuchar
1991 benannt. Die naheliegende Regel "jede Ecke bekommt gleich viel Volumen" waere nach meiner Rechnung instabil: Kleine
Beulen in der Zeitscheibe wuerden immer schneller wachsen. Eine billige Probe (Karte K1) kann das am Netz pruefen.

- Dossier abgeschlossen 12:52:55 CEST (date). Abrufe 11 von 15.
- Nach dem Gegenlesen ueberarbeitet (Absolutaussagen "alle zwoelf", "alle Takt-Regeln" eingeschraenkt; 600-Zelle 2 bis 6 %;
  Lesart "Schritt"; Projekt-grep in K1), abgeschlossen 12:56:21 CEST (date).
