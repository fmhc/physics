# ARBEITSFELD DOPPELSPALT-L (feldforscher)

- Start (date): 2026-10-05 05:06:38 CEST. Zeitbox 60 min, also Ende spaetestens ~06:06.
- Karte gelesen ganz: KARTE.md (DS1 bis DS5 unveraendert uebernommen, Bedeutung nicht angetastet).
- Gestrichenes bleibt stehen (~~so~~). Offene Rueckfragen stehen unten unter "Offen" und wandern mit.

## 0. Projektkontext (gelesen 05:06 bis 05:08, nur lokal)

- THEORIE-VFW.md Abschn. 4.5 (Z. 336-350) [S]: CHSH-Beweis fuer lokales Medium; Papatryfonos u. a. 2024 statischer
  Pilotwellen-Bell-Test erlaubt Wellenkommunikation; Urteil "Interferenzanalogien ja, lokale messunabhaengige
  Volltheorie nein". Q3 (Z. 448) [S]: Couder/Fort 2006 nur Abstract, "Kein hier reproduzierter Doppelspaltbefund".
  Q6: de Broglie Doppelloesung (Rueckblick 1987, AFLB). -> Nicht wiederholen, nur anknuepfen.
    fuer Materie. Z. 253-259 (Abschn. 2.3.4): Dilatation "caused by internal oscillations within elementary
    particles", "postulated by Louis de Broglie in 1924 [2] and was deduced by Erwin Schroedinger in 1930 [3] from
    the Dirac function"; "internal oscillation is assumed to be circular in order to explain the spin and also the
    magnetic moment".
  - QUELLEN-DOSSIER.md W9 "Interferenz" = LEP-Kontaktwechselwirkung (Bourilkov 2000), nicht Doppelspalt.
- Q-Ball-Modell des Projekts [S]: PAPIER-I-ROBUSTHEIT-ENTWURF.md Z. 31-37 und Pruefzeile Z. 64: Potential
  U(S) = S - S^2 + beta S^3 (S = |phi|^2), Hauptmodell beta = 1/2, Vakuum nu^2 = 1 + q^2 (Masse m = 1).
  RUNDE-09.md Z. 341 [S]: omega_min^2 = 1 - 1/(4 beta) = 0,5 -> omega in (0,707; 1). RUNDE-16.md Z. 175, 299 [S]:
  grosse Ladung = Tropfen mit Innendichte S = 1, E -> 0,707 Q.
- Gorard Double-Slit-Bulletin: SEITENKARTE.md Z. 74 [S]: nur Titel, "vermutlich ebenso unerreichbar, nicht geprueft".

## 1. Arbeitshypothesen vor dem ersten Abruf [ES]

- Zwei Regime (Feldregel 1): (R-lin) Interferenz als Eigenschaft einer linearen Amplitude mit Born-Regel; (R-nl)
  Interferenz als Folge klassischer nichtlinearer Wellen-Teilchen-Dynamik (Pilotwelle, Soliton, Doppelloesung).
  Kandidaten-Moderatoren: Kopplungsgrad Teilchen-Welle (Gedaechtnis, Antrieb), Verhaeltnis Spaltabstand zu
  Reichweite des Teilchenfelds, Masse vs. innere Frequenz (welche Laenge setzt die Streifen).
- Vorueberlegung (Papier, [ES], noch ohne Quelle): Ein geboosteter Q-Ball phi = f(gamma(x - v t))
  exp(-i omega gamma (t - v x)) traegt eine Phasenwelle der Laenge 2 pi/(gamma omega v). Fuer M = E ~ omega Q
  (Tropfengrenze) ist das etwa Q-mal die de-Broglie-Laenge 2 pi/(gamma M v) des ganzen Balls. Molekuel-
  Interferometrie misst h/(M v) mit der Gesamtmasse -> moeglicher scharfer Unterscheidungspunkt.
- Vorueberlegung 2 [ES]: Ein stabiler Q-Ball strahlt nicht (omega < m, Schwanz ~ exp(-kappa r), kappa =
  sqrt(m^2 - omega^2)). Ohne Antrieb hat er keine eigene Fernwelle, die durch den anderen Spalt laufen koennte.
  Couder-Tropfen brauchen das angetriebene Bad. -> Moderator "Reichweite 1/kappa gegen Spaltabstand d".
- Vorueberlegung 3 [ES]: Die Karte setzt "lineare Wellen geben I3 = 0" als entschieden. Erinnerung [L?]: Bei echten
  Spalten (Randbedingungen) gibt schon lineare Maxwell-Theorie I3 != 0 durch nicht-klassische Pfade (De Raedt u. a.
  2012; Sawant u. a. 2014). Nicht neu herleiten, nur pruefen, ob das stimmt; es betrifft die Kontrolle jeder
  QBALL-DOPPELSPALT-Rechnung.

## 2. Abrufplan (hoechstens 10 Abrufe, hoechstens 2 Websuchen)

| Nr | Ziel | Bezug |
|---|---|---|
| A1 | arXiv-API: Tropfen + Spalt, nach Datum | DS1, 24-Monats-Fenster |
| A2 | arXiv-API: third-order/higher-order interference, Sorkin, nach Datum | DS2, DS4, 24 Monate |
| A3 | arXiv-API: Q-ball bzw. soliton + slit/interference | DS3 |
| A4 | arXiv-API: self-interfering clock (Margalit) | DS5 |
| A5 | arXiv-API: Dagan/Bush HQFT bzw. Compton-Uhr | innere Uhr, Laengenfrage |
| A6 | arXiv-API: nicht-klassische Pfade (Sawant/De Raedt) | I3-Kontrolle |
| A7-A10 | Reserve fuer Erwartungsverstoesse | |
| W1-W2 | Websuche Reserve (24-Monats-Pruefung) | |

## 3. Abrufprotokoll (Erwartung VOR dem Abruf, Ausgang danach)

### A1 (Erwartung 05:09:32 CEST, vor dem Abruf)

- Ziel: export.arxiv.org/api/query, all:droplet AND all:slit, sortiert nach Einreichdatum absteigend, 30 Treffer.
- Erwartung: Treffer Andersen u. a. 2015 (kein klares quantenartiges Muster, Abhaengigkeit von Details),
  Pucci u. a. 2018 (Doppelspalt ohne QM-Muster), vielleicht Ellegaard/Levinsen 2020 (gewisse Beugungsmerkmale).
  In den letzten 24 Monaten kein Papier, das ein QM-artiges Tropfen-Doppelspaltmuster bestaetigt. Moeglich:
  Numerik (Nachbin u. a.), die in einem Regime mit Rauschen Streifen meldet.
- Ausgang A1 (05:10:13): FEHLSCHLAG. curl http -> 0 Byte; curl https -> HTTP 429 "Rate exceeded."
  (quellen/A1-arxiv-droplet-slit-20261005-050947.xml, 14 Byte). Zaehlt als ein verbrauchter Abruf.
  Ausweg: arxiv.org-Suchseite per WebFetch (in der Karte erlaubt), gleiche Erwartung.

### A2 (Erwartung 05:10:13 CEST, vor dem Abruf)

- Ziel: arxiv.org/search, "walking droplets slit", neueste zuerst (WebFetch).
- Erwartung: wie A1. Zusaetzlich: falls ein 2024-2026-Papier auftaucht, dann eher Modellrechnung (stochastisch,
  Gedaechtnis) als Experiment mit QM-Muster.
- Ausgang A2 (05:11:12), 23 Treffer (WebFetch-Zusammenfassung der Suchseite, Abstracts gekuerzt) [S Abstract,
  ueber Zusammenfassung]:
  - Ellegaard, Levinsen 2020, arXiv:2005.12335 "Interaction of Wave-Driven Particles with Slit Structures":
    "the answer is no, but that the classical system exhibits rich and fascinating structures" -> bestaetigt DS1-Richtung.
  - Richardson u. a. 2014, arXiv:1410.1373: Numerik gibt Spaltmuster, die dem Experiment aehneln, aber "evident
    differences from quantum mechanics".
  - **Darrow, Bush 2025, arXiv:2509.25574 "Single-particle Fraunhofer diffraction in a classical pilot-wave model"**:
    "agreement with both single- and double-slit Fraunhofer patterns" (Lagrange-Pilotwellenmodell). -> VERSTOSS
    gegen meine A1/A2-Erwartung (innerhalb 24 Monate, Modell meldet Uebereinstimmung mit Fraunhofer). Voller Zyklus:
    Abstract lesen (A3).
  - Dunn, Keshavarz, Dowell 2025, arXiv:2510.25073: ueberkritisches Faraday-Regime, erwaehnt Spaltexperimente
    "previously studied in the subcritical Faraday regime" -> Hinweis auf Regime-Moderator (unter-/ueberkritisch).
  - Hung, Hsieh, Hong 2024, arXiv:2409.11934: Tunnelzeit, Aehnlichkeit zu Bohm-Teilchen.
  - Andersen u. a. 2015 und Pucci u. a. 2018 NICHT in der Trefferliste (vermutlich nicht auf arXiv) -> bleiben [L?].
- Korrigierte Erwartung: Das Feld hat sich gespalten: Experimente (2015-2020) "nein", ein Lagrange-Modell 2025 "ja,
  Fraunhofer". Kandidaten-Moderator: Nah- gegen Fernfeld, Gedaechtnis, Barrierengeometrie, Rauschen.

### A3 (Erwartung 05:11:12 CEST, vor dem Abruf)

- Ziel: arxiv.org/abs/2509.25574 (Darrow, Bush 2025), Abstract.
- Erwartung: Modellrechnung (keine neue Messung), Uebereinstimmung nur im Fernfeld bzw. in einem bestimmten
  Parameterfenster (Gedaechtnis, Spaltbreite); Streifenabstand gesetzt durch die Faraday-Wellenlaenge, nicht durch
  eine Tropfenmasse; die Autoren grenzen sich ab von "das ist Quantenmechanik".
- Ausgang A3 (05:11:45) [S Abstract]: "Walking oil droplets offer a qualitative, classical analog of single-particle
  diffraction. Making this analog quantitative has proven challenging, leading recent authors to conjecture that no
  classical pilot-wave model could exhibit Fraunhofer diffraction. We revisit the problem with the recent, Lagrangian
  pilot-wave model of Darrow and Bush [Symmetry 16, 149 (2024)], and find agreement with both single- and
  double-slit Fraunhofer patterns. We identify two distinct dynamical features that enable our model to capture
  Fraunhofer diffraction and distinguish it from previous classical pilot-wave models." PRR 7, 033288 (2025), 8 S.
  - Modellrechnung, keine Messung: bestaetigt. Laengenfrage und Regime: im Abstract NICHT beantwortet.
  - Neu: "recent authors ... conjecture that no classical pilot-wave model could exhibit Fraunhofer diffraction"
    (vermutlich Ellegaard/Levinsen 2020) -> durch Modell-Gegenbeispiel 2025 angefochten.
  - Bedeutung: Die Frage "kann eine klassische Pilotwelle Fraunhofer?" ist Stand 2025 im Modell mit "ja" beantwortet,
    im Experiment (Tropfen) mit "nein" (2015-2020). Zwei Regime: abstraktes Lagrange-Modell gegen reale Faraday-Wellen.
    Volltext noetig fuer: welche Laenge, welche zwei Merkmale (A4).

### A4 (Erwartung 05:11:45 CEST, vor dem Abruf)

- Ziel: arxiv.org/html/2509.25574 (Volltext HTML), gezielte Fragen.
- Erwartung: Das Lagrange-Modell ist de-Broglie-artig (Teilchen mit innerer Schwingung bei einer Compton-artigen
  Frequenz, gekoppelt an ein Klein-Gordon-artiges Feld). Streifenabstand folgt einer emergenten de-Broglie-Laenge aus
  innerer Frequenz und Teilchengeschwindigkeit, nicht einer Badlaenge. Die zwei Merkmale: (i) Geschwindigkeit des
  Teilchens nicht fest (Beschleunigen/Abbremsen), (ii) Phasenkopplung Teilchen-Welle ("harmony of phases").
  Statistik aus deterministischem Chaos mit gleichverteilten Anfangsorten. Kein I3, keine Aussage zu Mehrteilchen.
- Ausgang A4a (05:12): arxiv.org/html/2509.25574 -> HTTP 404 (zaehlt als Abruf). A4b (05:12:09): PDF per curl,
  quellen/A4-arxiv-2509.25574-darrow-bush-20261005-051209.pdf (1 774 697 Byte, PRR-Satz), S. 1-8 gelesen (05:13).
- Befunde A4 [S]:
  - Modell (Abschn. II, Wirkung und Gl. 1): reelles Klein-Gordon-Feld phi mit Masse m; relativistisches
    Punktteilchen gleicher Masse in 2D; Kopplung b > 0, einziger freier Parameter. Gl. (1):
    (d_t^2 - nabla^2 + V^2) phi = gamma^-1 b delta^2(q - q_p); d_t(gamma u) = gamma^-1 b grad phi(q_p,t). Gueltig b <~ 25.
  - Abschn. II: Teilchen zeigt "emergent particle vibrations at the redshifted Compton frequency gamma^-1 omega_c,
    consistent with the Zitterbewegung imagined by de Broglie"; erfuellt p = hbar k am Teilchenort; "harmony of
    phases"; "The particle radiates energy only upon acceleration".
  - Gl. (3): lambda_eff(b) ~ (b/68,0)^2 lambda_dB. Also NICHT lambda_dB selbst; fuer b = 25 etwa 0,135 lambda_dB.
    Fig. 7(b): Proportionalitaet lambda_eff ~ lambda_dB "holds only for slow-moving particles" (gruen ~0,12-0,27 c),
    "falls off faster than lambda_dB for fast-moving particles".
  - Doppelspalt Fig. 3(d): 2500 Laeufe, nur N_good = 1296 durchqueren (Rest reflektiert); w2 = 2,03 lambda_c,
    d = 3,66 lambda_c, b = 25; Stossparameter gaussgewichtet (sigma 0,41 lambda_c), Glaettung Gl. (4) an Einzelspalt
    angepasst. chi^2/nu: Fraunhofer 1,36 (Pearson) bzw. 0,89 (Yates), Gauss 17,6 bzw. 11,0; 37 Bins.
  - Zwei Merkmale (Abschn. IV): (1) Lorentz-kovariante Abstrahlung nur bei Beschleunigung -> umgeht "Conjecture 1"
    von Andersen u. a. [13] und Bohr u. a. [14]; (2) Proposition A1: glatte Beugungsbilder brauchen entweder
    nicht kreuzende Bahnen (Bohm) oder nicht differenzierbare Abbildung (Chaos). Ihr Modell: Chaos.
  - Zu den Experimenten (Einleitung, Abschn. IV, Anh. A): Couder/Fort schwer reproduzierbar; statistisch bestritten
    [13,14]; "more refined, repeatable experiments [15,16] reveal quantitatively different diffraction patterns";
    "While coherent double-slit diffraction patterns have been observed with walking droplets [15,16]"; "both studies
    reported diffraction patterns with relatively sharp peaks". [15] = Pucci u. a. JFM 835 (2018), [16] = Ellegaard,
    Levinsen PRE 102 (2020).
  - Abschn. V: "we do not expect its long-term statistics to converge to 'quantumlike' results"; ohne Nichtlokalitaet
    "no way for any classical pilot-wave model to capture multiparticle entanglement".
  - Fussnote [26]: Darrow, Found. Phys. 55, 13 (2025): Kopplung an die komplexe Phase -> im Grenzfall u << c exakt
    Bohm-Mechanik, aber Wellengeschwindigkeit -> unendlich, "not a compelling example of local ... diffraction".
  - Neue Tropfen-Arbeiten im 24-Monats-Fenster (nur Titel, [L]): Primkulov u. a. PRR 7, 013226 (2025); Pucci u. a.
    PRE 111, L033101 (2025).
- Abgleich mit Erwartung A4: Modell de-Broglie-artig (Compton-Zitterbewegung, KG-Feld): ja. Streifenlaenge = emergente
  de-Broglie-Laenge: NEIN (Faktor (b/68)^2, nur langsam). Zwei Merkmale: anders (Abstrahlung nur bei Beschleunigung;
  Chaos). Kein I3, keine Welcher-Weg-Aussage: ja (nicht gefunden auf S. 1-8).
- Korrigierte Erwartung: "Innere Uhr + Harmonie der Phasen" legt die Streifenlaenge NICHT fest; sie folgt dem
  Impulsuebertrag Feld->Teilchen (~ b^2). Fuer den Q-Ball heisst das [ES]: die Laengenfrage der Karte (omega oder M)
  ist ohne Rechnung nicht entscheidbar; es kann eine dritte, kopplungsabhaengige Laenge sein.

### A5 (Erwartung 05:13:38 CEST, vor dem Abruf)

- Ziel: arxiv.org/search "third-order interference", neueste zuerst, 50 Treffer (WebFetch).
- Erwartung: Sinha u. a. 2010 (kappa < 1e-2, Photonen), Kauten u. a. 2017 (5-Pfad, Schranken 1e-3 bis 1e-4),
  Cotter u. a. 2017 (Molekuele, ~1e-2), Jin u. a. 2017 (Spin), NMR 2012; nicht-klassische Pfade (Sawant 2014,
  Magana-Loaiza 2016) als Stoerterm. Im 24-Monats-Fenster hoechstens Einzelarbeiten, beste Schranke 1e-4 bis 1e-5,
  also schaerfer als DS2s "<= 1e-3". Theorie: Ududec/Barnum/Emerson, nichtlineare QM -> I3 != 0 (DS4).
- Ausgang A5 (05:14:55), 16 Treffer [S Abstract, ueber WebFetch-Zusammenfassung, Zahlen woertlich zitiert]:
  - Vogl u. a. 2021, arXiv:2103.17209 (Einzelphotonen, hBN): "tight bound on the third-order interference term of
    3.96(523)x10^-4".
  - Conlon u. a. 2023, arXiv:2308.03446 (kohaerente Zustaende, Homodyn): "kappa = 0.002 +- 0.004".
  - Kanthak u. a. 2024, arXiv:2409.04163 (Vorschlag, BEC-Atominterferometrie): "upper bound of 5.7x10^-3 on the
    statistical deviation" (Status Vorschlag/Messung unklar -> pruefen nur falls Budget).
  - De Raedt, Michielsen, Hess 2011, arXiv:1103.0121 "Multi-order interference is generally nonzero" (Maxwell,
    realistische Dreifachspalte) -> bestaetigt Vorueberlegung 3: I3 = 0 gilt nur fuer die idealisierte Pfadsumme.
  - Theorie: Niestegge 2011-2014, Dakic/Paterek/Brukner 2013 (Dichtewuerfel), Henson 2014 ("lack of third-order
    interference bounds violation of the CHSH-Bell inequality to 2.883"): I3 != 0 gehoert zu verallgemeinerten
    (post-quantischen) Wahrscheinlichkeitstheorien.
  - Sinha 2010, Kauten 2017, Cotter 2017, Sawant 2014, Ududec 2011 NICHT in dieser Trefferliste (anderer Wortlaut).
- Abgleich: beste Schranke 24-Monats-Fenster: keine schaerfere als 4e-4 gefunden; Erwartung "1e-4 bis 1e-5" nicht
  belegt (eher 1e-3-Niveau, Vogl 2021 ~4e-4 +- 5e-4). DS4-Literatur liegt bei GPTs, nicht bei "nichtlinearer QM"
  -> DS4 noch offen.

### A6 (Erwartung 05:15:17 CEST, vor dem Abruf)

- Ziel: arxiv.org/search "Sorkin parameter", neueste zuerst (WebFetch).
- Erwartung: Sawant u. a. 2014 und Magana-Loaiza u. a. 2016 (nicht-klassische/geschleifte Pfade geben kappa != 0
  in Standard-QM, Groesse ~1e-3 bis 1e-2 je nach Geometrie); Sinha u. a. 2015; vielleicht Rengaraj u. a. 2018
  (Nichtlinearitaet bzw. Detektor-Nichtlinearitaet erzeugt kappa != 0); Kauten 2017. Im 24-Monats-Fenster wenig.
- Ausgang A6 (05:16:15), 8 Treffer [S Abstract, ueber WebFetch-Zusammenfassung]:
  - Sinha, Vijay, Sinha 2014, arXiv:1412.2198 "On the superposition principle in interference experiments":
    analytische Formel fuer den Sorkin-Parameter fuer klassische Wellen und Schroedinger-Gleichung, "deviation from
    the application of the principle" (naive Anwendung, Randbedingungen).
  - Vieira u. a. 2017, arXiv:1705.07156 (Materiewellen, Doppelspalt mit geschleiften Bahnen): "maximum Sorkin
    parameter of the order of |kappa_max| ~ 0.2, which is the value of the fringe visibility" (spezielle Groesse,
    nicht ungeprueft auf Dreifachspalt-Experimente uebertragen).
  - da Paz u. a. 2015 arXiv:1510.04186 (Gouy-Phase aendert kappa); Quach 2016 arXiv:1610.06401 (zweiter Detektor
    wirkt bei nicht-klassischen Pfaden).
  - Pleinert, von Zanthier, Lutz 2018, arXiv:1810.08221: fuer M Teilchen verschwinden alle Terme der Ordnung
    >= 2M+1; "exponentially more sensitive to deviations from Born's rule".
  - Im 24-Monats-Fenster: nur Sassoli de Bianchi 2025 (Kognition, nicht Physik).
  - KEIN Treffer, der "nichtlineare QM -> kappa != 0" ausspricht. Sawant 2014, Magana-Loaiza 2016, Rengaraj 2018
    nicht in der Liste.
- Abgleich: nicht-klassische Pfade bestaetigt (andere Autoren als erwartet). DS4 in der Form "nichtlineare
  Abwandlungen" bleibt unbelegt -> Websuche W1 (24-Monats-Pruefung, Feldregel 7).

### W1 (Erwartung 05:16:31 CEST, vor der Websuche 1 von 2)

- Suche: nonlinear Schroedinger / interacting condensate + third-order interference / Sorkin parameter.
- Erwartung: hoechstens indirekte Treffer (BEC-Wechselwirkung als Stoerquelle bei Born-Tests, z. B. Kanthak 2024;
  allgemeine Aussagen "Born rule / linearity"). Keine Arbeit, die fuer ein klassisches Soliton I3 berechnet.
  Moeglicher Fehlschlag (Suche war zuletzt erschoepft).
- Ausgang W1 (05:16:59): Suche lief (kein Fehlschlag). Treffer u. a.: "Experimental Higher-Order Interference in a
  Nonlinear Triple Slit" (arXiv:2112.06965), Radonjic 2023 PRA (scl.rs), Kanthak u. a. 2024 (arXiv:2409.04163),
  "Interference in Quantum Mechanics" (arXiv:2508.12940), Pleinert 2018. Zusammenfassung der Suchmaschine (nur
  Hinweis, nicht zitierfaehig [L?]): drei Mechanismen fuer I3 != 0 innerhalb der QM: (1) Nahfeld-"looped paths",
  (2) Mehrteilchen-Interferenz mit Koinzidenzmessung, (3) nichtlineare Evolution (nicht-quadratische Hamilton-
  funktionen, optische Nichtlinearitaet, Teilchen-Teilchen-Wechselwirkung); Kanthak 2024 berechnet fuer GPE-BEC
  einen nicht verschwindenden Sorkin-Parameter "under the assumption that the modulo-square rule holds".
- VERSTOSS gegen W1-Erwartung: Es gibt ein EXPERIMENT mit I3 != 0 durch Nichtlinearitaet (2112.06965). Voller
  Zyklus: Abstract A7.

### A7 (Erwartung 05:16:59 CEST, vor dem Abruf)

- Ziel: arxiv.org/abs/2112.06965.
- Erwartung: Photonen-Dreifachspalt mit nichtlinearem Element (Kerr bzw. Mehrphotonen-Prozess); gemessenes kappa
  deutlich != 0, skaliert mit der Staerke der Nichtlinearitaet (Leistung); Autoren aus Wien (Walther/Rozema/Dakic);
  Aussage: kein Born-Regel-Bruch, sondern Nichtlinearitaet der Evolution.
- Ausgang A7 (05:17:43) [S Abstract]: Namdar, Jenke, Alonso Calafell, Trenti, Radonjic, Dakic, Walther, Rozema,
  arXiv:2112.06965v1 (13.12.2021). Woertlich: "Quantum mechanics is often said to only exhibit second-order
  interference. However, this is only true under specific assumptions, typically single-particles undergoing linear
  evolution. Here we experimentally show that nonlinear evolution can in fact lead to higher-order interference. The
  higher-order interference in our experiment has a simple quantum mechanical description; namely, optical coherent
  states interacting in a nonlinear medium. Our work shows that nonlinear evolution could open a loophole for
  experiments attempting to verify Born's rule by ruling out higher-order interference."
  Keine Zahlen im Abstract; Zeitschrift auf der Abs-Seite nicht angegeben.
- Abgleich: Erwartung getroffen (Wien, kohaerente Zustaende, nichtlineares Medium, kein Born-Bruch). Zahlen offen.
- Bedeutung: DS4 inhaltlich bestaetigt, aber mit anderen Quellen als in der Karte genannt (Namdar 2021 Experiment;
  Kanthak 2024 GPE-Rechnung). Sorkin 1994 und Ududec 2011 sind Mass-/GPT-Rahmen, nicht "nichtlineare QM".

### A8 (Erwartung 05:17:43 CEST, vor dem Abruf)

- Ziel: arxiv.org/search "self-interfering clock" (WebFetch).
- Erwartung: Margalit, Zhou, Machluf, Rohrlich, Japha, Folman 2015 (Science 349, 1205): Atomuhr aus zwei
  Spinzustaenden im raeumlichen Ueberlagerungszustand; laufen die Uhren auf beiden Wegen verschieden schnell
  (simulierte Gravitations-Zeitverschiebung), sinkt die Sichtbarkeit, weil die Uhrzeit Welcher-Weg-Information
  traegt; Wiederkehr der Sichtbarkeit bei vollem Umlauf der relativen Uhrphase. Vielleicht Folgearbeiten (Zhou 2018).
- Ausgang A8 (05:18:27) [S Abstract, ueber WebFetch-Zusammenfassung]: Margalit, Zhou, Machluf, Rohrlich, Japha,
  Folman, arXiv:1505.05765 (Mai 2015) "A self-interfering clock as a 'which path' witness": "We split a clock into
  two spatially separated wave packets, and observe an interference pattern with a stable phase ... the clock was in
  two places simultaneously"; "entanglement between the clock's time and its path yields 'which path' information,
  which affects the visibility of the clock's self-interference." Wiederkehr und Zahlen: in der Zusammenfassung
  nicht enthalten; Folgearbeiten nicht in der Trefferliste.
- Abgleich: Erwartung getroffen (eine Zeile). DS5 bestaetigt.

### A9 (Erwartung 05:18:27 CEST, vor dem Abruf, letzter von 10)

- Ziel: arxiv.org/search "soliton double slit", neueste zuerst (WebFetch).
- Erwartung: wenige Treffer, eher Optik (raeumliche Solitonen, Beugung am Spalt) oder BEC (Soliton am Doppeltopf,
  Soliton-Interferometer); KEIN Q-Ball-Doppelspalt, KEIN Vergleich Streifenlaenge innere Frequenz gegen Masse.
- Ausgang A9 (05:19:19) [S Abstract, ueber WebFetch-Zusammenfassung, nur 3 von 5 Treffern beschrieben]:
  - Nakamura, Nakazono, Ando 2005, cond-mat/0508210 "Dynamics of Macroscopic Wave Packet Passing through Double
    Slits: Role of Gravity and Nonlinearity" (GPE-Wellenpaket, "soliton showing a head-on collision with a
    hard-walled obstacle"; "peak-to-peak distance in the fringe pattern ... proportional to g^(-1/2)"; Bedeutung von
    g im Auszug unklar, vermutlich Schwere).
  - Ngek, Dikande, Moubissi 2016, arXiv:1610.07860 "Matter-Wave Fields for Double-Slit Atom Interferometry:
    Variational Versus Exact Solitons" ("splitting a single-hump Bose-Einstein condensate into two ... pulses").
  - Sivashinsky 2009, arXiv:0912.5156 (Hamilton-Jacobi, Doppelspalt diskutiert).
- Abgleich: Erwartung im Kern getroffen (kein Q-Ball, kein omega-gegen-M-Vergleich), aber naeher als erwartet:
  nichtlineare klassische Feld-Wellenpakete (GPE) im Doppelspalt sind gerechnet (2005, 2016). Dort sind die
  Streifen Feld-Dichtestreifen, keine Einzelteilchen-Statistik. -> DS3 nur mit Einschraenkung.
- Abrufbudget: 10 von 10 verbraucht (A1 Fehlschlag, A4a 404 mitgezaehlt). Ab jetzt nur noch W2 (Websuche 2 von 2).

### W2 (Erwartung 05:19:19 CEST, vor der Websuche 2 von 2)

- Suche: Q-ball bzw. Soliton mit innerer Frequenz im Doppelspalt, 2024-2026 (24-Monats-Pruefung fuer DS3).
- Erwartung: kein Treffer mit Q-Ball im Doppelspalt; hoechstens Q-Ball-Streuung an Barrieren bzw. Potentialstufen
  oder Soliton-Interferometrie (BEC), oder Darrow/Bush-Umfeld (HQFT).
- Ausgang W2 (05:19 bis 05:20): Suche lief. Treffer u. a. arXiv:1508.06837 "Young's experiment scheme modification
  for a possible observation of 'soliton' interference model" (+ ar5iv-Spiegel), lettersonmaterials.com-PDF,
  arXiv:2603.15505, 2502.20519, 2502.09136, "Oscillons from Q-balls" (usal.es). Zusammenfassung der Suchmaschine
  (NICHT an der Quelle gelesen, [L?]): Im Soliton-Interferenzmodell teilt sich ein lokalisiertes "Soliton" an zwei
  Spalten in zwei, die sich wieder vereinen; die Verteilung der Bewegungsrichtungen kann ein Interferenzmuster
  bilden; Kennzeichen: Muster verschwindet, wenn der Spaltabstand groesser ist als die Solitonabmessung;
  Lorentz-invariante, atmende (breather-artige) Loesungen, Ausgangsrichtung haengt von Phase und
  Schwingungsfrequenz ab.
- VERSTOSS gegen W2-/DS3-Erwartung: Ein Soliton-Doppelspalt-Modell mit Frequenz-/Phasenabhaengigkeit existiert
  (2015). Ob es den Streifenabstand gegen innere Frequenz und Masse vergleicht: UNBEKANNT (Budget erschoepft, nicht
  gelesen). DS3 daher "nicht entschieden, Tendenz verfehlt". Pflicht vor jeder Q-Ball-Doppelspalt-Karte: 1508.06837
  an der Quelle lesen.
- Projekt-grep 05:21 (Gegensweep-Pruefung, siehe 6): dashboard-overview-20260909/snapshot/neue-theorie/
  gitter-checkliste.json Z. 35-39 [S]: W3 "Die Quantentheorie ist linear (Superposition, Born-Regel)", status hart,
  Herleitung Weinberg 1989 / Gisin 1990 / Polchinski 1991 (ueberlichtschnelle Signale), messung "Dreispalt-Test des
  Sorkin-Parameters: Abweichung unter 1e-2 bis 1e-3 (Sinha et al. 2010 und Nachfolger)", folge_kandidat "Ein inneres
  Uhren-Bild muss als unitaere Dynamik formulierbar sein", pruefung "Rabi-Runner ...", erledigt false.
  -> Die Karten-Zeile "Nicht im Projekt: Dreifachspalt bzw. Sorkin-Parameter" stimmt nicht ganz.
- Fluss-Eis [S]: RUNDE-37/RAUMZEIT-NETZ.md Z. 42 "Fluss-Eis-Pfeile: Eichfelder auf dem Netz, also Elektrizitaet
  [E: FLUSS-1]"; UEBERLEITUNGEN-EMERGENZ.md Z. 20 "Licht: Fluss-Eis auf Pyrochlor (FLUSS-1) [G]".

## 4. Erwartungsverstoesse (getrennt)

| Nr | Erwartung | Ausgang | Quelle |
|---|---|---|---|
| V1 | Kein 2024-26-Papier mit QM-artigem Tropfen-/Pilotwellen-Doppelspalt | Darrow/Bush 2025 (PRR 7, 033288): klassisches Lagrange-Pilotwellenmodell trifft Einzel- und Doppelspalt-Fraunhofer (chi^2/nu 1,36 bzw. 0,89) | A3, A4 [S] |
| V2 | Streifenlaenge im de-Broglie-artigen Modell = emergente lambda_dB | lambda_eff = (b/68)^2 lambda_dB, nur langsam (u <~ 0,25 c); innere Compton-Uhr legt die Streifen NICHT fest | A4 Gl. (3), Fig. 7 [S] |
| V3 | Zwei Merkmale = Geschwindigkeitsfreiheit, Phasenharmonie | Abstrahlung nur bei Beschleunigung (Lorentz-kovariant) und Chaos (Prop. A1) | A4 Abschn. IV [S] |
| V4 | Tropfen-Nachpruefungen: "kein Muster" | Kohaerente Doppelspaltmuster beobachtet [15,16], aber quantitativ anders, scharfe Spitzen | A4 Einl., Abschn. IV, Anh. A [S] |
| V5 | "Nichtlineare QM -> I3 != 0" nur Theorie (Sorkin/Ududec) | Experiment: Namdar u. a. 2021, nichtlineare Evolution gibt hoehere Interferenz; Kanthak 2024 GPE-Rechnung | A7 [S Abstract], W1 |
| V6 | Kein Soliton-Doppelspalt-Modell mit innerer Frequenz | arXiv:1508.06837 Soliton-Interferenzmodell (Teilen/Vereinen, Frequenz/Phase, d_max ~ Solitongroesse) | W2 [L?], nicht gelesen |
| V7 | Beste I3-Schranke im 24-Monats-Fenster 1e-4 bis 1e-5 | Nicht gefunden; bestes gefundenes 3,96(523)e-4 (2021); 2023 0,002 +- 0,004 | A5 [S Abstract] |
| V8 | Karte: Sorkin/Dreifachspalt nicht im Projekt | gitter-checkliste.json W3 (07.09.) fuehrt den Dreispalt-Test schon als harte Messung | Projekt-grep [S] |
| V9 | Nicht-klassische Pfade: kleiner Stoerterm | Vieira u. a. 2017: |kappa_max| ~ 0,2 in einem Materiewellen-Doppelspalt-Aufbau (Groesse anders definiert) | A6 [S Abstract] |

## 6. Gegensweep (05:24): Was war so selbstverstaendlich, dass ich es nicht geprueft habe?

- G1 [geprueft, lokal]: "Das Projekt kennt Sorkin/Dreifachspalt nicht" (aus der Karte uebernommen). Projekt-grep:
  doch, gitter-checkliste.json W3 (siehe V8). Folge: Anstoss muss an W3 und den offenen "Rabi-Runner" anknuepfen.
- G2 [nicht geprueft, nur benannt]: "Ein Teilchen = ein Klick". Ein Soliton, das sich am Spalt teilt und NICHT
  wieder vereint, gaebe zwei Teilobjekte, also Doppelklicks bzw. Teilladungen. Antikorrelation einzelner Photonen
  (Grangier/Roger/Aspect 1986 [L]) und Ladungsquantelung sind harte Latten fuer jedes Teilungsmodell. Fuer Q-Baelle
  mit Q = Ladung: Teilung in Q1 + Q2 widerspraeche der Ladungsquantelung, ausser die Haelften vereinen sich immer.
- G3 [nicht geprueft]: "Photonen-I3-Schranken gelten fuer Teilchenmodelle". Photonen-Tests (besonders kohaerente
  Zustaende, Conlon 2023) pruefen die Linearitaet des Lichtfelds plus Detektor, nicht ein massives Soliton. Fuer
  massive Teilchenmodelle zaehlen nur massive I3-Tests (Molekuele Cotter u. a. 2017 [L?], Spins [L?]) -> Latte
  dort vermutlich nur ~1e-2 [L?].
- G4 [nicht geprueft]: "Molekuel-Interferometrie bestaetigt h/(M v) mit der Gesamtmasse" (Arndt 1999 C60, Fein u. a.
  2019 >25 kDa [L]) — in diesem Lauf nicht abgerufen.
- G5 [nicht geprueft]: Kovachy u. a. 2015 (Atome 54 cm getrennt [L]) als Latte gegen d_max-Modelle.

## 7. Abschluss

- DOSSIER.md geschrieben ab 05:27:22 CEST, Korrekturen bis 05:31:44 CEST (date): A2-Fehlergrenze auf +-0,05 bis 0,1
  und Schwelle 0,1 angehoben (vorher +-0,05 bzw. 0,05, zu optimistisch); Konvergenzbindung fuer V-Q1/V-Q3 ergaenzt;
  Darrow/Bush-Bezug auf Abschn. I-II praezisiert.
- Abrufbudget 10/10, Websuche 2/2. Zeitbox eingehalten (Start 05:06:38).

## 5. Offen (Stand 05:24:38)

- O2: Welche Laenge setzt Streifen beim klassischen Q-Ball (omega oder M)? -> Papier [ES]: Phasengradient des
  geboosteten Balls gibt 2 pi/(gamma omega v); QM des ganzen Balls 2 pi/(gamma M v); Verhaeltnis M/omega ~ Q
  (Projektmodell: E/Q zwischen 0,707 und 1, omega zwischen 0,707 und 1). ABER Darrow/Bush zeigen eine dritte,
  kopplungsabhaengige Laenge -> nur Rechnung entscheidet. Offen.
- ~~O3: Wie scharf sind I3-Schranken heute (24 Monate)?~~ -> beantwortet soweit gefunden: Photonen 3,96(523)e-4
  (2021), 0,002 +- 0,004 (2023); im 24-Monats-Fenster nur Vorschlag BEC (2024, 5,7e-3). Massive Teilchen offen (G3).
- O4 (neu): arXiv:1508.06837 an der Quelle lesen (Pflicht vor QBALL-DOPPELSPALT-1).
- O5 (neu): Zahlen aus Namdar u. a. (Volltext) und Zeitschriftenstatus; Kanthak 2024 Status (Vorschlag oder Messung).
- O6 (neu): I3 fuer klassische Pilotwellenmodelle (Darrow/Bush) — nach Recherchestand nicht belegt (nur eine Suche
  "droplet slit", kein Dreifachspalt-Treffer; keine gezielte 24-Monats-Suche mehr moeglich, Budget erschoepft).
