# ARBEITSFELD WB-ZENODO-L (feldforscher)

- Start 2026-10-04 22:21:52 CEST (date). Zeitbox 35 min, also Ende spaetestens ca. 22:56 CEST.
- Karte gelesen 22:21:52 CEST. WZ1 bis WZ3 stehen in der Karte und werden hier NICHT geaendert.
- Abrufbudget: hoechstens 4 WebFetch (Zenodo-API, Zenodo-Datei, ggf. arXiv-API). Keine Websuche.
- Versiegeltes: keine Projektdateien zu M1/KS-1/Vertraegen; kein grep ueber Projektpfade geplant.
- Kennzeichen: [S] Seite/Abschnitt, [S Abstract], [L], [M], [ES], [H].

## Abrufprotokoll

### Abruf 1: Zenodo-API https://zenodo.org/api/records/23108687
- Erwartung (notiert 2026-10-04 22:21:59 CEST, vor dem Abruf): Metadaten mit Titel wie im Scout, ein einzelner Autor
  ohne oder mit schwacher institutioneller Zugehoerigkeit (unabhaengig), ggf. ORCID; Typ "publication/preprint";
  genau eine Version (v1) vom 02.10.2026; eine PDF-Datei, evtl. dazu Code-/Daten-Archiv; Beschreibung = Abstract,
  das das DR3-Ergebnis nennt. Kein Peer Review, keine Kommentare.
- Werkzeug: curl statt WebFetch, damit eine unveraenderte Quellenkopie entsteht (WebFetch liefert nur eine
  Kleinmodell-Zusammenfassung). Zaehlt als Abruf 1 von 4. Selbstanzeige im Dossier.
- Abrufzeit 2026-10-04 22:22:33 CEST, HTTP 200, 7856 Byte, Kopie quellen/zenodo-api-23108687-20261004T222233.json,
  sha256 525bd5b8d4884e6e49616819bcb2e6f8da51681d033958de29b689254673700b.
- Ausgang (eingetragen 22:23 CEST):
  - BESTAETIGT: ein Autor "Hess, Malin", affiliation null, keine ORCID im Datensatz. Nur eine Version (v1.0,
    index 0, is_last true). Concept-DOI 23108687 -> Versions-DOI 10.5281/zenodo.23108688. Erstellt
    2026-10-02T19:19:29 UTC. Lizenz CC-BY-4.0. Statistik: 2 Aufrufe, 0 Downloads (vor meinem Abruf).
  - TEILWEISE: Typ ist "publication/report", nicht "preprint". Belanglos.
  - VERSTOSS 1 (Inhalt): Das Abstract meldet keinen Newton-konformen Befund, sondern eine Neigung zum Boost:
    Gamma = 1.182 +/- 0.045 im 250-pc-Hauptarm (8947 Kontroll-, 1794 Testpaare), "inside the band predicted for
    a 17% velocity boost and 2.4 sigma above the Newtonian band", unter der vorregistrierten 3-sigma-Schwelle,
    Urteil INCONCLUSIVE. Stabil ueber RUWE 1.0/1.2/1.4 und im 130-pc-Arm. [S Abstract]
    -> WZ1 nach Wortlaut ("kein Boost ueber 2 sigma") vermutlich verfehlt; Definition von "2.4 sigma above the
    Newtonian band" (Abstand zur Bandkante oder zur Mitte?) muss im PDF geklaert werden.
  - VERSTOSS 2 (Herkunft): Der Autor legt selbst offen, dass zwei Designkorrekturen D1, D2 "before unblinding"
    nur durch lokale Laufbelege datiert sind, "which outside readers cannot independently verify". [S Abstract]
    Die WB-1-Vorregistrierung ist damit von aussen nicht pruefbar; nur WB-2 bekommt einen oeffentlichen Zeitstempel.
  - VERSTOSS 3 (Umfang): Mehr Dateien als erwartet: Report-PDF, WB2_protocol_frozen.md (20665 B),
    WB1_preregistration_frozen.md (9572 B), WB1_zenodo.zip (400404 B, Skripte/Manifeste/Mocks), SHA256SUMS.txt.
    WB-2-Hash im Abstract: SHA-256 85ee8389fc70705d58322ffa6e733f70f8ac61bce7a805eddbd99a036f8987f0.
  - AUFFAELLIG [H]: Werkzeug "Goblin++" mit Repo github.com/mrgogobot/goblinpp; Name des Kontos klingt nach Bot.
    Moeglicherweise agenten- oder KI-gestuetzte Arbeit. Nur Hypothese, im PDF nach Offenlegung suchen.
  - Vorhersage auf Akte [S Abstract]: echter Boost -> WB-2 findet Gamma nahe 1.18 bei >= 3 sigma, auch nach
    DR4-Astrometrie-Beschleunigungs-Veto gegen verborgene Begleiter (Arm T1); verborgene Dreifachsysteme ->
    Gamma faellt Richtung Newton-Band, am staerksten in T1. -> relevant fuer WZ3 (Kern/Schwanz bzw. Begleiter).
  - Referenz 10.5281/zenodo.4435257 [L: vermutlich der Zenodo-Eintrag des El-Badry-Rix-Heintz-Katalogs; nicht geprueft].

### Abruf 2: Zenodo files-archive https://zenodo.org/api/records/23108688/files-archive (alle 5 Dateien in einem Zip)
- Begruendung: ein Abruf statt drei; die WB-2-Bindung steht in WB2_protocol_frozen.md, nicht nur im PDF.
- Erwartung (notiert 2026-10-04 22:23 CEST, vor dem Abruf):
  - Das PDF ist ein 10-25-seitiger Bericht; Statistik = Verhaeltnis der Mediane von v_tilde (skalierte
    Senkrechtgeschwindigkeit) Testbin/Kontrollbin, normiert an einem Newton-Mock; Fehler per Bootstrap.
  - "2.4 sigma above the Newtonian band" heisst Abstand zur Mitte oder Oberkante des Mock-Bandes; ich erwarte
    Abstand von Gamma zu Gamma_Newton = 1.00 +/- Bandbreite, nicht ein Beschleunigungsprofil.
  - Kein expliziter Fit Kern/Schwanz wie bei Banik u. a. 2024; stattdessen der Median als robuste Groesse
    (implizite Kernbetonung) und Dreifachsysteme als Alternativerklaerung.
  - WB2_protocol_frozen.md bindet: Katalog (DR4-Version), Schnitte, Bins, Statistik, 3-sigma-Schwelle, Arm T1
    mit Veto, Entscheidungsregeln. sha256sum der MD-Datei = Hash im Abstract (85ee83...). Wahrsch. 85 %.
  - Keine Erwaehnung einer KI-Mitwirkung im PDF (60 %).
- Abrufzeit 2026-10-04 22:23:36 CEST, HTTP 200, 892427 Byte, application/zip, Kopie
  quellen/zenodo-23108688-files-archive-20261004T222336.zip, entpackt nach quellen/archiv-23108688/ (inneres Zip nach
  quellen/archiv-23108688/inner/). Zaehlt als Abruf 2 von 4 (curl, gleiche Selbstanzeige).
- Integritaet [M, sha256sum/md5sum lokal]: alle fuenf md5 = API-Werte; sha256(WB2_protocol_frozen.md) =
  85ee8389fc70705d58322ffa6e733f70f8ac61bce7a805eddbd99a036f8987f0 = Abstract-Hash; sha256sum -c SHA256SUMS.txt im
  inneren Zip: 20/20 OK; PDF und WB2-Datei innen = aussen (cmp).
- Ausgang WB2_protocol_frozen.md (gelesen 22:24 CEST, ganze Datei, 247 Zeilen):
  - VERSTOSS 4 (Form): Die "eingefrorene WB-2-Datei" ist das ganze WB-1-Arbeitsdokument (Vorregistrierung, Laufprotokoll,
    Abweichungen D1/D2, Ergebnisse) mit angehaengtem WB-2-Abschnitt (Z. 202-237). Kopfzeile "Oct 2, 2026 · @Malin";
    "Confirmed by Malin" in dritter Person (Z. 26). [S WB2 Z. 1-3, 26]
  - VERSTOSS 5 (Zeitachse): ALLES am 02.10.2026: Vorregistrierung eingefroren, Extraktion, D1, Power-Studie, D2,
    Versiegelung, Entblindung, S1/E1, WB-2-Einfrieren; Zenodo-Upload 19:19 UTC desselben Tages. [S WB2 Run log Z. 139-200]
  - VERSTOSS 6 (Umbau vor Entblindung): Die eingefrorene WB-1-Vorregistrierung (Primaerarm 130 pc, alpha 0.8-1.6,
    Perspektivschnitt, sigma(v~)<0.1, Statistik ueber v~ gesamt) wurde vor der Entblindung zweimal umgebaut:
    D1 = nur Senkrechtkomponente zur Himmelsseparation, Perspektivschnitt gestrichen (Grund: nur 7 Testpaare);
    D2 = Primaerarm 250 pc, Rauschschnitt sigma<0.20, alpha-Band 1.16-1.50 (Hwang, Ting & Zakamska 2022, 2 sigma).
    Grund D2: Power-Befund "the frozen rule has no teeth" (Newton-Band [0.867, 1.166] bei alpha 0.8-1.6). [S WB2 Z. 147-166]
  - DR3-Ergebnis [S WB2 Z. 179-186]: 250 pc primaer Gamma 1.1821 +/- 0.0449, Newton-Band [0.9600, 1.0763],
    Boost-Band [1.1232, 1.2592], 2.36 sigma ueber Newton-OBERKANTE, INCONCLUSIVE. 130 pc: 1.2481 +/- 0.1035, 1.6 sigma.
    Mediane |v~_perp|: Kontrolle 0.2970 (8947), Test 0.3510 (1794). Schwanz |v~_perp|>1.2: 2.1 % gegen 2.6 %.
    S1 (RUWE<1.4): 1.177 +/- 0.035, 2.9 sigma; E1 (RUWE<1.0, explorativ): 1.308 +/- 0.125, 1.9 sigma, < 300 Paare.
    [M] (1.1821-1.0763)/0.0449 = 2.356 -> 2.36 sigma stimmt. Gegen die Bandmitte 1.018: (1.1821-1.0182)/0.0449 = 3.65 sigma.
    [M] 0.3510/0.2970 = 1.1818 -> Gamma stimmt mit den Medianen.
  - "2.4 sigma above the Newtonian band" = Abstand zur OBERKANTE des Mock-Bandes (Erwartung "Mitte oder Oberkante": Oberkante).
  - Kern/Schwanz (WZ3) [S WB2 Z. 94, 119, 184]: Median statt Schwanz ausdruecklich gegen Dreifachsysteme; Anteil v~>1.2 nur
    "secondary diagnostic only, because hidden triples dominate that tail". -> ausdrueckliche Trennung, aber kein Fit.
  - WB-2-Bindung [S WB2 Z. 202-237]: Skripte per Hash (pairs.gbl v3, mock.py, stats.py), Katalogschnitte, abgeleitete
    Schnitte, Statistik, Bins, Newton-Band (alpha 1.16-1.50, Seed 20261002), Entscheidungsregel 3 sigma / 2 sigma,
    min. 300 Testpaare, Bootstrap 10000 Seed 20261003, Laufreihenfolge. Aenderbar nur: Katalog-Hash, Spaltennamen-Abbildung,
    Dateiaufteilung. T1-Veto (Astrometrie-Beschleunigung >= 5 sigma) als Sekundaerarm; DIE DR4-GROESSE FUER T1 IST NICHT
    GEBUNDEN ("fixed and logged before extraction"). Nicht gebunden: welcher DR4-Weitdoppelsternkatalog (es gibt noch keinen
    El-Badry-DR4-Katalog [ES]), wer ihn erstellt, Zeitpunkt.
  - Grenzen vom Autor selbst [S WB2 Z. 233-235]: Exzentrizitaets-Systematik ist von einem Boost in WB-2 nicht trennbar;
    DR4 misst weitgehend dieselben Sterne neu -> keine unabhaengige Population.
  - Zitierte Literatur [S WB2 Z. 126, 239-246]: Cookson et al. (2026) MNRAS 547 stag342 (kein MOND-Boost, hochreine Stichprobe);
    Chae (2026) arXiv 2601.21728v2 (Anomalie in 36 Systemen mit 3D-Geschwindigkeiten); Boufourou (2026) arXiv 2608.24556
    ("estimator forensics and DR4 protocol", Exzentrizitaets-Dreifach-Kopplung kann Scheinsignal erzeugen);
    Pittordis, Sutherland & Shepherd (2025) arXiv 2504.07569. Alle unbelegt bis zur Pruefung (Abruf 3).
  - [H] Kopfzeilen-Format "Datum · @Name" und dritte Person deuten auf ein Dokumentwerkzeug mit Assistenz; "Goblin++" ist
    eine Eigen-Sprache ohne Median, Sortierung, Zufallszahlen, FITS-Export (Z. 237). Nur Hypothese.
- Ausgang PDF (pdftotext -layout -> quellen/WB1_report_pdftotext-layout.txt, gelesen 22:26-22:28 CEST; 16 S., ReportLab,
  CreationDate roh D:20261002185426+00'00'):
  - "Malin Hess · Independent researcher" [S PDF S. 1]. Goblin++ 0.1.0-alpha.19 ist eigenes Werkzeug des Autors
    ("M. Hess, Goblin++ ... evidence-first scientific programming language", [S PDF S. 6 Refs]).
  - VERSTOSS 7 (KI): "Analysis assistance, code drafting and report preparation by Claude (Anthropic), an AI system,
    working with the author. All runs were executed and reproduced by the author" [S PDF S. 6]. Erwartung (60 % keine
    KI-Erwaehnung) verfehlt; [H] aus Abruf 2 bestaetigt (offen gelegt).
  - VERSTOSS 8 (Widerspruch PDF gegen eingefrorenes Protokoll): PDF S. 5 Par. 7 fasst "Hidden triples or eccentricity" zusammen:
    "Gamma falls toward the Newtonian band". Das gehashte Protokoll (WB2 Z. 229-233) sagt fuer die Exzentrizitaets-
    Systematik das Gegenteil: "Gamma stays elevated ... the one case WB-2 cannot fully separate from a boost".
    Bindend ist das Protokoll; das PDF ueberzeichnet die Trennschaerfe von WB-2. Auch S. 1: "a systematic should shrink it".
  - Banik u. a. 2024 steht nur in der Literaturliste [S PDF S. 7], im Text nicht diskutiert; Chae 2023/2024 gar nicht zitiert,
    nur Chae (2026). Einordnung des Papiers selbst daher duenn.
  - Eigene Systematik-Tabelle [S PDF S. 5]: Exzentrizitaet "Not tested; Hwang et al. find 10^3 AU pairs more eccentric than
    10^4 AU pairs" -> laut Autor laeuft der bekannte Trend in die Richtung, die einen Schein-Boost erzeugen KANN.
    [L, unsicher] Ob Hwang u. a. 2022 das so zeigen, habe ich nicht im Kopf belastbar.
  - Mock [S PDF S. 13-14, wb1_mock.py]: keine Dreifachsysteme, keine Zufallspaare im Mock; Rauschen = Katalogfehler
    ohne Aufblaehfaktor; Halbachsenverteilung dN/da ~ a^-1.6 "implementation choice, logged" (nicht vorregistriert).
  - [M] Bedeutung von D2: Mit dem urspruenglich eingefrorenen alpha-Band 0.8-1.6 lag das Newton-Band (synthetisch)
    bei [0.867, 1.166]; Gamma 1.182 laege dann nur (1.182-1.166)/0.045 = 0.36 sigma ueber der Kante. Naeherung: Band aus
    synthetischen Paaren, nicht aus der echten Stichprobe. Die 2.4 sigma haengen also an der Einengung D2.
  - [M grob, Gauss-Naeherung] Rauschmodell: Bei Testbin-sigma ~0.13 und Median ~0.30 hebt 30 % unterschaetzter
    Fehler den Testmedian um ca. 2.5 %, das Kontrollbin kaum -> ca. +0.03 in Gamma (~0.6 sigma). Allein nicht genug fuer
    0.106 ueber der Kante, aber nicht vernachlaessigbar. Im Papier nicht als Systematik gefuehrt (nur Bildtext S. 3:
    "more dependent on the noise model").
  - Zeitstempel: PDF 18:54:26 UTC (roh), inneres Zip 20:04:58 Ortszeit, Zenodo 19:19:29 UTC. Widerspruchsfrei unter
    plausiblen Zeitzonen-Annahmen; Beweiswert fuer die Reihenfolge D1/D2 vor Entblindung: keiner (wie vom Autor gesagt).

### Abruf 3: arXiv-API id_list (export.arxiv.org/api/query), eine Abfrage fuer 8 IDs
- IDs: 2601.21728 (Chae 2026, zitiert), 2608.24556 (Boufourou 2026, zitiert), 2504.07569 (Pittordis/Sutherland/Shepherd
  2025, zitiert), 2311.03436 [L Banik u. a. 2024], 2305.04613 [L Chae 2023], 2309.10404 [L Chae 2024], 2111.01789
  [L Hwang/Ting/Zakamska 2022], 2304.07322 [L Hernandez 2023, unsicher].
- Erwartung (notiert 2026-10-04 22:28 CEST, vor dem Abruf):
  - 2601.21728: existiert, Chae, Weitdoppelsterne mit 3D-Geschwindigkeit, Anomalie (80 %).
  - 2608.24556: existiert, Boufourou, Schaetzer-Forensik, Exzentrizitaet x Dreifach (70 %). Falls nicht: halluzinierte
    Quelle in KI-gestuetztem Papier = schwerer Befund.
  - 2504.07569: existiert mit Pittordis als Autor; der im PDF genannte Titel gehoert [L] eher zu Pittordis & Sutherland 2023
    (OJAp, 2205.02846) -> Titel-Fehlzuordnung moeglich (50 %).
  - 2311.03436 Banik u. a. "Strong constraints..." (90 %); 2305.04613 Chae 2023 "Breakdown..." (80 %); 2309.10404 Chae 2024
    "Robust evidence..." (70 %); 2111.01789 Hwang u. a. Exzentrizitaet (80 %); 2304.07322 Hernandez (40 %).
  - Zur Exzentrizitaetsfrage: Abstract von 2111.01789 nennt alpha-Anstieg mit der Separation (Weite = exzentrischer) (55 %);
    das widerspraeche dem Satz im PDF S. 5.
- Abrufzeit 2026-10-04 22:28:35 CEST, HTTP 200, 23925 Byte, Kopie quellen/arxiv-api-idlist-20261004T222835.xml.
  Zaehlt als Abruf 3 von 4 (curl). Abruf 4 NICHT genutzt.
- Ausgang (eingetragen 22:31 CEST): alle 8 IDs existieren, Titel passen zu den Zitaten. Keine halluzinierte Quelle.
  - VERSTOSS 9 (der wichtigste): Boufourou 2026, 2608.24556v1 (25.08.2026, Einzelautor, 7 S.): "a full-median estimator,
    even with a perfect eccentricity correction, recovers gamma = 1.08-1.13 from purely Newtonian universes containing
    20-30% residual triples ... while a tail-truncated estimator and a mixture likelihood recover <= 1.04 and 1.00. An
    injected MOND-like boost (gamma = 1.4 above 2 kau) is recovered at >= 1.26 by all three"; auf Chae-(2024)-Stichprobe
    (81088 Paare) gamma = 1.045 [1.025, 1.068], Mischfit 1.05, f_trip = 0.15; gamma = 1.4 "rejected at ~16 sigma";
    "We freeze a pre-registered protocol, time-stamped on Zenodo, for Gaia DR4" (Zenodo 10.5281/zenodo.22073431).
    [S Abstract 2608.24556] -> WB-1 benutzt genau die Median-Schaetzerfamilie, die Boufourou als anfaellig ausweist, und
    zitiert ihn, zieht die Folgerung fuer sich aber nicht. Und: WB-2 ist NICHT die einzige oeffentliche DR4-Vorregistrierung.
    [M] gamma 1.08-1.13 (auf G bezogen) entspricht Geschwindigkeitsfaktor sqrt = 1.039-1.063; WB-1 sieht 1.182 (G-Aequivalent
    1.182^2 = 1.397). Boufourous Dreifach-Scheinsignal deckt also nur einen Teil des WB-1-Ueberschusses (andere Stichprobe,
    anderer Median -> nur Groessenordnung).
  - VERSTOSS 10: Chae u. a. 2026 (2601.21728v3, 19.09.2026, 7 Autoren inkl. Hernandez; WB-1 zitiert v2 als "K.-H. Chae"):
    gamma = 1.60 +0.24/-0.14, "dominated by two systems ... 3D relative velocities exceeding their estimated Newtonian
    escape velocities" [S Abstract]. Die Anomalie sitzt dort im Schwanz; WB-1 nennt nur "anomaly in 36 systems".
  - Banik u. a. 2024 (2311.03436v4, aktualisiert 2026-09-28: "corrected Figure 15 and related discussion"): 8611 WB < 250 pc,
    2-30 kAU, Kontamination und unentdeckte nahe Begleiter modelliert, alpha_grav = -0.021 +0.065/-0.045, MOND bei 16 sigma
    ausgeschlossen, Modellvergleich 19 sigma [S Abstract, Kommentar]. Inhalt der Korrektur von Abb. 15 unbekannt.
  - Chae 2023 (2305.04613v4): 26615 WB < 200 pc, g_obs/g_pred = 1.43 +/- 0.06 bei g_N = 10^-10.15 [S Abstract]
    -> [M] Geschwindigkeitsfaktor sqrt(1.43) = 1.196 +/- 0.025.
  - Chae 2024 (2309.10404v4): 2463 "pure" binaries, gamma_g = 1.49 +0.21/-0.19; projizierter Geschwindigkeits-Boost
    gamma_vp = 1.20 +/- 0.06 (stat) +/- 0.05 (sys) fuer s >~ 5 kau [S Abstract] -> [M] WB-1 1.182 +/- 0.045 liegt darauf.
  - Pittordis, Sutherland & Shepherd 2025 (2504.07569v2, OJAp): Titel passt zum WB-1-Zitat (meine [L]-Erwartung einer
    Fehlzuordnung war falsch -> gestrichen, s. u.); Mischfit binary+triple+flyby+chance, "Newtonian models provide a
    significantly better fit than MOND, though improved understanding of the triple population is necessary"; v2-Kommentar:
    "Newton still favoured, delta-chi2 vs MOND somewhat reduced" [S Abstract, Kommentar].
  - Hwang, Ting & Zakamska 2022 (2111.01789v2): "close to uniform at 10^2 AU and becomes superthermal at >10^3 AU"
    [S Abstract]. Die PDF-Aussage "10^3 AU pairs more eccentric than 10^4 AU pairs" ist aus dem Abstract weder zu
    bestaetigen noch zu verneinen -> nach Recherchestand nicht belegt.
  - Hernandez 2023 (2304.07322v3): Anomalie bei a <~ 2 a0 "confirmed" [S Abstract].
  - Cookson u. a. 2026 (MNRAS 547 stag342): NICHT geprueft (keine arXiv-ID bekannt), nur WB-1-Zitat.

## Gegensweep (22:31 CEST): Was war so selbstverstaendlich, dass ich es nicht geprueft habe?

- G1 Text = Maschinendaten? GEPRUEFT (jq auf wb1_result_250pc.json, wb1_mock_250pc.json, wb1_manifest_250pc.json, 22:29):
  gamma_obs 1.182096, sigma 0.044864, Band [0.960014, 1.076270], z_above_newton_hi 2.3588, verdict INCONCLUSIVE,
  Schwanz 2.146 % / 2.564 %, n 8947/1794; Schnittkette 1817594 -> 38135 (RUWE-Schnitt 148217 -> 92086 groesster Einzelschnitt).
  Alles deckungsgleich mit PDF und Protokoll.
- G2 Woher kommt die Bandoberkante? GEPRUEFT [M aus Mock-JSON]: hi = Test(alpha 1.16) 0.30135 / Kontrolle(alpha 1.50)
  0.27999 = 1.0763; Mitte (beide 1.32) 0.29295/0.28818 = 1.0166 -> Gamma liegt (1.1821-1.0166)/0.0449 = 3.69 sigma darueber.
  NEU: Der beobachtete Kontrollmedian 0.2970 trifft den Mock bei alpha 1.16 (0.2972), nicht bei 1.50 (0.2800). Der ganze
  Ueberschuss sitzt im Testbin: beobachtet 0.3510 gegen Mock-Hoechstwert 0.3014 (Faktor 1.165). Ob man die absolute
  Mock-Skala ernst nehmen darf, haengt an nicht vorregistrierten Details (a^-1.6, Massenrelation) -> zweiseitig, nur [ES].
- G3 Sind die Zitate echt und richtig wiedergegeben? GEPRUEFT (Abruf 3): echt; zwei Wiedergaben unvollstaendig (V9, V10).
- G4 NICHT geprueft: DR4-Termin 02.12.2026 (nur [S PDF S. 5] und Projektwissen).
- G5 NICHT geprueft: Hash des El-Badry-Katalogs (1.8 GB) und Zenodo-md5 9644d53f... .
- G6 TEILWEISE: Goblin++-Interpreter (alpha, stille Konstanten-Namen wie h -> Planck). In wb1_pairs.gbl heissen Variablen
  k und n; plausible Mediane (~0.30) und Uebereinstimmung Kontrollmedian/Python-Mock sprechen gegen einen stillen
  Konstantenfehler bei k. Kein Beweis.
- G7 NICHT geprueft: ob 1.17 der richtige MOND-Faktor fuer den Median von |v~_perp| im Bin g_N <= 1e-10 ist (Banik u. a.:
  ~20 % erst "at asymptotically large separations" [S Abstract]). Fester Faktor statt EFE-Rechnung.
- G8 Selbstverstaendlich und wichtig: Die 2.36 sigma enthalten nur Bootstrap-Statistik; Systematik nur ueber das alpha-Band.

## Kalibrierung (Warnzeichen)

- Nach Abruf 3 stieg meine Neigung, WB-1 als Median-Scheinsignal zu lesen. Neue Evidenz zu WB-1 selbst gibt es dafuer
  nicht; Grundlage ist ein Abstract eines ungeprueften Einzelautor-Preprints, dessen eigene Zahl (Geschwindigkeit +4 bis
  +6 %) den WB-1-Ueberschuss (+18 %) nicht deckt. Gehoert als Warnzeichen ins Dossier.

## Abschluss

- DOSSIER.md geschrieben 22:32:24 CEST, Gegenlese-Korrekturen 22:35 CEST: Hernandez ohne Zahl; "vier additive Wege" zu
  "drei" berichtigt (Exzentrizitaet ist Formeffekt, nicht additiv); [M] fuer 3.74 sigma ergaenzt; geschlechtsneutrale
  Formulierung zu Malin Hess.
- Ende der Arbeit 2026-10-04 22:35:32 CEST (date). Zeitbox 35 min eingehalten (genutzt ca. 14 min). Abrufe 3 von 4.

## Offene Rueckfragen (wandern mit)

- R1 Boufourous DR4-Protokoll (Zenodo 10.5281/zenodo.22073431) lesen und mit WB-2 vergleichen? Ausserhalb meines Mandats.
- R2 Welcher DR4-Weitdoppelsternkatalog (mit R_chance_align, binary_type) wird existieren? WB-2 bindet das nicht.
- R3 Cookson u. a. 2026 ungeprueft; Hwang-Trend 10^3 gegen 10^4 AU ungeprueft; Inhalt der Banik-v4-Korrektur unbekannt.

## Gestrichenes (nicht loeschen)

- ~~[L] Der im PDF genannte Titel "Wide binaries from Gaia DR3: testing GR vs MOND with realistic triple modelling" gehoere
  zu Pittordis & Sutherland 2023 (2205.02846), Fehlzuordnung moeglich.~~ Gestrichen 22:31: 2504.07569v2 traegt genau
  diesen Titel [S arXiv-API]. Mein Gedaechtnis war falsch, nicht das Zitat.
