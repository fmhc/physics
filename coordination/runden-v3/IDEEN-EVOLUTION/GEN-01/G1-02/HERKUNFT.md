# G1-02 Herkunft

- Operator: research. Eltern: WEBER (geparkte Teilchenschwelle an der Stufe). Arm E, Generation 1.
- Bearbeiter: Operator-Agent "aussen" (Anthropic, Opus 5.5). Beginn (date, Gesamtauftrag): 2026-09-30 07:18:19 CEST.

## Erwartung vor dem ersten Suchabruf (geschrieben 2026-09-30 07:27:34 CEST, date)

Die Literatur zu NLS-Solitonen an Barrieren und Stufen kennt zwei Regime: langsame, breite Solitonen verhalten sich wie
klassische Teilchen (scharfe Energieschwelle, keine Spaltung), schnelle oder schmale spalten sich wie lineare Wellen in
einen durchgelassenen und einen reflektierten Teil (Holmer/Marzuola/Zworski 2007). Unser Weber-Befund liegt vermutlich
ganz im Teilchenregime und ist damit bekannt; neu waere nur die Lage der Grenze fuer Q-Baelle.

## Elternbefund (an den Projektdateien gelesen)

- [A] RUNDE-06.md, Abschnitt "Weber-Zerspritzen": 144 Laeufe ohne Zerfall bis We = 4,12; Feinscan: zurueck bis
  0,98 v_cl (0,994 bis 0,996), "haengt" bei 1,00, durch ab 1,02; keine Spaltung; Schwelle nur auf Rasterbreite.
- [A] RUNDE-06/ERGEBNISSE-R6-A.md, W-1 und W-2 sowie "Aufloesung, Raster, vorab Ableitbares": v50/v_cl = 1,0100 ist die
  Rastermitte; das We50-Verhaeltnis 1,85 folgte vorab aus dem Papier.
- [A] RUNDE-06/weber/PLAN.md: Modell U = S - S^2 + S^3/2, Stufe V2 (1 + tanh(x/B))/2 mit B = 1, v_cl ~ sqrt(V2)/omega,
  Spaltkosten zweier gleicher Haelften 0,203 / 0,105 / 0,051 (omega^2 = 0,6 / 0,7 / 0,8), Klassen und Fragmentregeln.
- Abweichung der Quellen: Der Auftrag nennt "Teilchenschwelle auf Rasterbreite"; die Ernte schreibt ausdruecklich, ein
  Spaltfenster schmaler als das 2-%-Raster sei nicht ausgeschlossen. Beides stimmt; die Karte uebernimmt das Raster.

## L4-Notiz zur Elternkarte: teilweise bekannt

- [L] Holmer, Marzuola, Zworski, "Soliton splitting by external delta potentials", J. Nonlinear Sci. 17, 349 (2007),
  arXiv math/0608510 (Abstract gelesen): Ein Soliton an einem Delta-Potential spaltet in zwei Solitonen und Strahlung;
  die Naeherung gilt "for all but very slow solitons"; die durchgelassene Masse folgt der quantenmechanischen
  Transmissionsrate.
- [L] Wang, Hong, Lee, Wang, "Particle-wave duality in quantum tunneling of a bright soliton", Opt. Express 20, 22675
  (2012), arXiv 1206.1606 (Abstract gelesen): klassisches Teilchen bei kleiner, Materiewelle bei grosser
  Einfallsgeschwindigkeit; dazwischen "a finite (but not full) discontinuity in the tunneling transmission coefficient".
  Das ist genau die Groesse dT der Karte.
- [L] Hansen, Nygaard, Moelmer, "Scattering of matter wave solitons on localized potentials", arXiv 1210.1681
  (Abstract gelesen; Schluss laut Abruf: Streuung "resembles that of classical or quantum mechanical scattering
  depending on the height and width of the barrier"): niedrige breite Barrieren klassisch, hohe schmale quantenhaft.
  Grundlage der Gegenprobe B = 25.
- [L] Helm, Rooney, Weiss, Gardiner, Phys. Rev. A 89, 033610 (2014), arXiv 1401.7202 (Abstract gelesen): analytisch
  bestimmtes Gebiet, in dem ein Soliton an einer Barriere nicht gespalten werden kann.
- [L] Al-Alawi, Zakrzewski, "Q-ball scattering on barriers and holes in 1 and 2 spatial dimensions", J. Phys. A 42,
  245201 (2009), arXiv 0902.4358 (Abstract gelesen): In 1+1 Dimensionen verhalten sich stabile Q-Baelle an Barrieren
  und Loechern sehr aehnlich wie topologische Solitonen. [L?] Laut Suchtreffer (nicht an der Quelle geprueft) tritt
  dort auch Ladungsspaltung auf; in welchem Regime, ist ungeprueft.
- Laboranaloga: [L] Wales u. a., "Splitting and recombination of bright-solitary-matter waves", Commun. Phys. 3, 51
  (2020), arXiv 1906.06083 (Abstract gelesen): Spaltung und Wiedervereinigung an einer schmalen abstossenden Barriere.
  [L?] Marchant u. a., Nat. Commun. 4, 1865 (2013): Reflexion eines 85Rb-Solitons an einer breiten Gauss-Barriere nur
  laut Suchtreffer der Verlagsfassung; die gelesene arXiv-Fassung 1301.5759 nennt nur Bildung und Ausbreitung.
- Neu fuer Q-Baelle nicht gefunden (drei Suchen): die Grenze zwischen Teilchen- und Wellenregime an einer Massenstufe
  als Funktion der Stufenhoehe je Ladung gegen die Bindung je Ladung. Aus 24 Monaten fand ich keine einschlaegige Arbeit.

## Papierrechnung zur Elternkarte [S]: das leere Spaltfenster war energetisch vorgegeben

- Ein Spalt mit dem Anteil f auf der Plateauseite kostet grob f Q (1 - omega); an der Schwelle steht nur ~ V2 Q/(2 omega)
  zur Verfuegung. Also f <= Pi/(1 + Pi) mit Pi = V2/(2 omega (1 - omega)) (Naeherung ohne Kruemmung von M(Q); die
  Kruemmung macht den Spalt etwas billiger).
- Die sechs Feinscan-Faelle: Pi = 0,029 / 0,057 (0,6), 0,037 / 0,073 (0,7), 0,053 / 0,106 (0,8) fuer V2 = 0,01 / 0,02.
  Groesstes f = 0,096 bei (0,8; +0,02). Ein Spalt mit q_durch > 0,1 war also in allen sechs Faellen bis 1,02 v_cl
  energetisch nicht moeglich (Grenzfall (0,8; +0,02)).
- Folge fuer die Elternkarte: Der Teil "keine Spaltung" konnte nicht scheitern (L1 dafuer schwach, Memory "Vorab
  ableitbare Kennzahl ist keine Messung"). Messung bleibt nur "Umschlag im Intervall 0,98 bis 1,02 v_cl".
- Die Karte verlegt den Test deshalb dorthin, wo Spaltung erlaubt ist (Pi bis 2), und behaelt einen Punkt im alten
  Regime (Pi = 0,10) als Anschluss.

## Quellenliste (URLs)

- https://arxiv.org/abs/math/0608510v1
- https://arxiv.org/abs/1206.1606
- https://arxiv.org/abs/1210.1681 und https://arxiv.org/html/1210.1681
- https://arxiv.org/abs/1401.7202
- https://arxiv.org/abs/0902.4358
- https://arxiv.org/abs/1906.06083
- https://arxiv.org/abs/1301.5759

## Zeiten

- Karte geschrieben 2026-09-30 07:37:34 CEST; Schreibbeginn der Herkunftsdateien 2026-09-30 07:42:58 CEST (date).
- Ende (date): 2026-09-30 07:45:15 CEST. Beginn 07:18:19, also 27 min fuer alle drei Karten.
