# DOSSIER BOUFOUROU-DR4-L: Was bindet die ältere DR4-Vorregistrierung von Boufourou (Zenodo 22073431), und wie behandelt sie Kern und Schwanz?

- Feldforscher für claude-primary. Start 2026-10-05 00:27:55 CEST, Dossier begonnen 00:39 CEST (date).
- Grundlage:
  - Zenodo-API zu 22073431 und die einzige Datei des Eintrags (ZIP, 26,7 MB, md5 lokal = Zenodo),
  - darin das DR4-Protokoll, das Manuskript-PDF, README, Code und Daten (nur gelesen, nichts ausgeführt),
  - die Zenodo-Versionsliste,
  - der arXiv-Abstract 2608.24556v1 aus der lokalen Kopie von WB-ZENODO-L.
- Web-Abrufe: 4 von 4, davon einer durch meinen Parameterfehler fehlgeschlagen. Das Protokoll mit Erwartungen vor jedem Abruf steht in `ARBEITSFELD.md`.
- Kennzeichen:
  - [S …] an der Quelle gelesen, mit Zeile bzw. Seite. Zeilennummern des Manuskripts beziehen sich auf `quellen/Boufourou_2026_PaperI_pdftotext-layout.txt`.
  - [S WB-ZENODO-L] aus dem Dossier von WB-ZENODO-L übernommen, von mir nicht an der Urquelle geprüft.
  - [L] Gedächtnis, [M] eigene Rechnung von Hand, [ES] eigener Schluss, [H] Hypothese.
- Versiegeltes wurde nicht berührt. Geöffnet habe ich nur Dateien in `RUNDE-37/boufourou-dr4-l/` und `RUNDE-37/wb-zenodo-l/`. Einen Projekt-grep gab es nicht.

## Ergebnis zuerst (5 Punkte)

1. **22073431 ist keine eingefrorene Vorregistrierung, sondern die v1.0-Release eines GitHub-Reproduktionspakets mit einem Protokollentwurf darin.**
   - Zenodo-Zeitstempel 2026-08-24T00:06:54 UTC, also etwa 37,6 h vor der arXiv-Einreichung [S Zenodo-API; S arXiv-API].
   - Zenodo nennt das Protokoll "draft v0.95". Die Datei sagt "Version 1.0 — rédigé le 15/07/2026" und zugleich "À geler" (noch einzufrieren). Ein Hash des Protokolls oder des Codes steht nirgends.
   - Eine "version gelée v1.0 du 2026-07-15" ist erst für eine Release "avant le 2026-12-02" angekündigt.
   - Die spätere Version v2.0 vom 26.08. enthält gar kein Protokoll [S Versionsliste].
2. **Inhaltlich bindet der Entwurf ausdrücklich Kern und Schwanz.**
   - E2 (primär): Median, abgeschnitten bei ṽ < √2, mit verrauschten Zonenschablonen.
   - E3 (sekundär): Mischlikelihood (γ, f_trip) mit generativer Dreifach-Schablone.
   - Ein Urteil verlangt **beide** Schätzer.
   - Schwellen: D1 STOP, wenn die Validierungszone um ≥ 2 % vom Newton-Wert abweicht. D2 Newton: beide < 1,15, dazu 1,35 mit > 5σ_stat ausgeschlossen und außerhalb des Systematikbands. D3 Anomalie: beide > 1,20, dazu 1,00 mit > 5σ ausgeschlossen und außerhalb des Bands. D4 Grauzone.
   - [S PREREGISTRATION_DR4.md Z. 39–60]
3. **Offen bleiben:**
   - der DR4-Katalog ("type El-Badry+ … ou reconstruction équivalente"), wie bei WB-2,
   - Code-Hash und Seeds,
   - die Zahl hinter dem "vollen Systematikband": Im Code ist es nur das f(e)-Band,
   - die DR4-Entscheidungsregel als Code.
   - Der DR3-Eichwert im Protokoll ist ein älterer Rechenstand als im Papier (Tiefbin 0,97 ohne gegen 1,11 ± 0,07 mit Perspektivkorrektur; Δln L 138 gegen 129).
4. **BF3 verfehlt im Wortlaut.** Boufourous DR3-Messung liegt statistisch über Newton:
   - E2 = 1,045 [1,025; 1,068] (68 %), also 2,25 σ über 1,00 [M].
   - Mischfit 1,05 [1,04; 1,07] mit Δln L(γ=1) = 4,8, also ≈ 3,1 σ [M].
   - Mit 1,00 verträglich ist das nur über das f(e)-Systematikband {0,957; 0,958; 1,045} und im Tiefbin [S Papier S. 3–4].
   - Die Einordnung von WB-ZENODO-L ("Regime B … alle mit Newton") stimmt für die Verwerfung von 1,4 (≈ 16 σ), nicht für γ = 1,00.
5. **Gegen WB-2:**
   - Die beiden Protokolle messen nicht dasselbe:
     - γ in G-Skala gegen Γ als Geschwindigkeitsverhältnis,
     - 2D-Betrag mit Perspektivkorrektur gegen 1D-Senkrechtkomponente,
     - Zonen in s gegen Bins in g_N.
   - [H] Wiederholt DR4 die DR3-Lage, urteilen sie entgegengesetzt: WB-2 "BOOST FAVOURED", Boufourou "Newton" (D2).
   - Treiber ist laut Boufourous Karte der Rest-Dreifach-Schwanz am vollen Median. Nach derselben Karte deckt er aber höchstens etwa die Hälfte des WB-1-Überschusses (1,06–1,10 gegen 1,18 in der Geschwindigkeit) [M].

## Erwartungsverstöße (das Wichtigste zuerst)

| Nr | Erwartet | Gefunden | Beleg |
|---|---|---|---|
| V-A1a / V-A2a / V-L1a / V-A4b | Eine eingefrorene, zeitgestempelte Vorregistrierung | Der Status ist an fünf Stellen verschieden. Datei: "Version 1.0 — rédigé le 15/07/2026" und "À geler : dépôt horodaté (Zenodo) du présent document + code (hash SHA-256) avant DR4". Zenodo: "draft v0.95", "Le protocole gelé (v1.0) fera l'objet d'une release ultérieure avant le 2026-12-02". README: "the frozen, pre-registered protocol". Manuskript: "The protocol document and code hash will be deposited on Zenodo prior to DR4". arXiv-Abstract: "time-stamped on Zenodo". **Öffentlich zeitgestempelt ist nur der Entwurf vom 24.08.** | [S Protokoll Z. 2–3; S Zenodo-API description; S README Z. 24; S Papier S. 4–5 Z. 187–193; S Abstract 2608.24556v1] |
| V-L0a / V-A2c | BF3: DR3 mit Newton innerhalb 2 σ | E2 1,045 [1,025; 1,068] (68 %-Bootstrap): 2,25 σ. E3 1,05 [1,04; 1,07], Δln L(γ=1) = 4,8: ≈ 3,1 σ. Newton liegt nur im f(e)-Band, und die empirische Exzentrizität hebt γ um ~9 %. Protokoll: "γ_test = 1,04-1,05 ± 0,01 (stat)". | [S Papier S. 3 Z. 145–151; S phase_H.py Z. 172 "68%[…]" und Z. 206 "68% profil"; S Protokoll Z. 68–70] [M] |
| V-L1d | Das Protokoll trägt die Zahlen des Papiers | Protokoll: Δln L(1,4) = 138, f_trip 0,14, f(e)-Band [0,955; 1,042], Tiefbin 0,97 ± 0,13. Papier: 129, 0,15, 0,957–1,045, Tiefbin 1,11 ± 0,07 mit Perspektivkorrektur. Der Protokoll-Tiefbin ist der *unkorrigierte* Wert, obwohl das Protokoll die perspektivkorrigierte Observable bindet. | [S Protokoll Z. 17–18, 68–70; S Papier S. 4 Z. 161–165] |
| V-A4a | Die spätere Version enthält das Protokoll | v2.0 (22114321, 26.08.) hat nur 8 flache Dateien: kein `protocole/`, kein `paperI_mnras.tex`, keinen Code außer `etape_E_seuil.py`. Die Beschreibung verspricht alle Ordner. | [S Versionsliste files[]; description] |
| V-L2a | Die Entscheidungskriterien liegen als Code bei | `etape_D_verdict.py` (README: "pre-registered decision criteria applied to the data") ist ein älteres DR3-Skript mit rauschfreien Schablonen und Kriterien "C2/C4". 1,15, 1,20, 5σ und STOP kommen darin nicht vor. Die finale DR3-Messung steht in `phase_H.py`. | [S Code etape_D_verdict.py Z. 1–11, 56–68; phase_H.py Z. 1–10] |
| V-A2b | Mischfit primär, Median nur Diagnose | Umgekehrt: E2 (abgeschnittener Median) ist primär, E3 (Mischung) sekundär. D2 und D3 verlangen aber beide. | [S Protokoll Z. 39–47, 55–58] |
| V-L1b | Der DR3-Eichwert ist mit dem DR4-Schnittsatz gerechnet | DR3 fiduziell mit RUWE < 1,4, d < 200 pc, ohne ipd-, \|b\|- und G-Schnitt. Das Protokoll bindet RUWE < 1,2, ipd ≤ 2, \|b\| > 15°, G < 18, d < 300 pc. Die Variante RUWE < 1,2 gibt 1,047. | [S Papier S. 2 Z. 88–92; S phase_H.py Z. 100–102; S Protokoll Z. 22–26] |
| V-L1c | Ein robustes Injection-Recovery-Gitter | "Single-seed grid; statistical jitter ≈ ±0.02". E1 unter Newton mit f_trip 0,2–0,3 liegt laut CSV bei 1,065–1,129, das Papier sagt "1.08–1.13". Der Abstand zu E2 (≤ 1,044) beträgt nur 1–4 Jitter-Einheiten. Es gibt nur eine Familie von Dreifachmodellen ("one family"). | [S Papier S. 3 Z. 132, S. 5 Z. 206; S phase_G_resultats.csv Z. 4–5, 11–12, 20–21] |
| V-A1b | 22073431 ist die einzige oder neueste Fassung | is_last = false. Es gibt die Concept-DOI 10.5281/zenodo.22073430 und v2.0. | [S Zenodo-API relations] |
| (Selbst) | A3 liefert die Versionsliste | HTTP 400 wegen size=50, mein Fehler. Wiederholt in A4. | [S Kopie A3] |

## BF1 bis BF3 (Erwartungen der Karte, unverändert) mit Urteil

| Nr | Erwartung (Karte) | Urteil | Beleg |
|---|---|---|---|
| BF1 | [H] Die Vorregistrierung bindet einen Schätzer, der den Schwanz bzw. die Dreifachsysteme ausdrücklich modelliert, nicht nur den Median (60 %) | **Eingetroffen.** E3 ist eine gemeinsame Poisson-Likelihood (γ, f_trip) auf dem ṽ-Histogramm [0; 2,4] mit "(1−f)·binaires_γ + f·gabarit de triples génératives (Offner/Tokovinin/photocentre/moyennage ΔT_DR4/biais de masse, coupures simulées)". E2 schneidet den Schwanz bei ṽ < √2 ab, mit gleicher Abschneidung in den Schablonen. Beide sind entscheidungspflichtig. Ein voller Median kommt im Protokoll nicht vor. **Vorbehalte:** E3 ist nur sekundär; die Dreifach-Schablone ist nur über Code ohne Hash festgelegt; die Entartung γ↔f bei f → 0 ist vermerkt. | [S Protokoll Z. 39–49, 55–58] |
| BF2 | [H] Sie legt zahlenmäßige Entscheidungsschwellen für DR4 mit Zeitstempel oder Hash fest (70 %) | **Eingetroffen mit großem Vorbehalt.** Zahlen gibt es: 2 %, 1,15, 1,20, 1,35, 1,00, 5σ, Zonen, Schnitte. Der öffentliche Zeitstempel ist 2026-08-24T00:06:54 UTC, der einzige Hash die Zenodo-md5 des ganzen ZIP (52fa6640…edb44, lokal bestätigt). Der Autor erklärt die Fassung aber selbst zum Entwurf ("draft v0.95", "à geler") und kündigt eine gefrorene Fassung an. In dieser Zenodo-Versionsreihe ist sie bis 05.10. 00:34 CEST nicht erschienen; andere Ablageorte wie GitHub-Tags oder ein eigener Datensatz sind ungeprüft. Bindend ist heute nur, was am 24.08. öffentlich war. Ob die spätere v1.0 davon abweicht, ist erst nach ihrem Erscheinen prüfbar. Mein SHA-256 der Protokolldatei: `9d56c2409735d4bd80745210fe67a7e81093d7331dbcf61557137a5bfcafdeff`. | [S Zenodo-API; S Protokoll Z. 2–3, 53–60; S Versionsliste; sha256sum] |
| BF3 | [H] Boufourous eigener Befund auf echten DR3-Daten ist mit Newton innerhalb 2 σ verträglich (60 %) | **Im Wortlaut verfehlt** (statistisch 2,25 σ bzw. ≈ 3,1 σ). Nur unter Einschluss der Systematik ist er verträglich: Das f(e)-Band {0,957; 0,958; 1,045} umschließt 1,00, der Tiefbin liegt bei 1,11 ± 0,07 (1,6 σ), seine Klammer [0,97; 1,19]. Der Autor liest das als "Newtonian" und "γ = 1.00–1.05". [M] Das Profilintervall des Mischfits liegt auf einem γ-Gitter der Stufe 0,01 und ist deshalb grob. Maßgeblich ist Δln L = 4,8. | [S Papier S. 3 Z. 145–151, S. 4 Z. 161–165, S. 5 Z. 213–215; S phase_H.py Z. 19, 195] |

**Bedeutung nach Karte:** BF1 ist eingetroffen, BF2 nur formal. [ES] Es gibt einen zweiten fremden, schwanzfesten Maßstab für DR4, aber mit schwächerer Bindung als WB-2:
- Er ist ein öffentlicher, zeitgestempelter Entwurf.
- Einen Autor-Hash gibt es nicht.
- Die gefrorene Fassung ist angekündigt, aber nicht erschienen.

Nach dem 2.12. lassen sich zwei verschiedene Schätzerfamilien vergleichen, wenn Boufourou seinen Entwurf wirklich anwendet. Die Abweichungen der späteren v1.0 vom Stand des 24.08. muss man dann selbst prüfen. An unserem versiegelten Vertrag ändert das nichts.

## Was der Entwurf für DR4 bindet und was nicht [S PREREGISTRATION_DR4.md]

| Element | Gebunden? | Wert / Bemerkung |
|---|---|---|
| Hypothesen, Skala | ja | γ = G_eff/G_N. H0 γ = 1,00; H1 (MOND-AQUAL + EFE) γ ≈ 1,35–1,40 (Z. 14–16) |
| Observable | ja | ṽ = Δv_⊥/√(G_N M_tot/s_2D), Δv_⊥ transversal, "perspective corrigée via les vitesses radiales" (Z. 17–18) |
| Katalog | **nein** | "type El-Badry+ mis à jour DR4 (ou reconstruction équivalente documentée)" (Z. 22–23) |
| Schnitte | ja, zahlenmäßig | d < 300 pc; G < 18; \|b\| > 15°; RUWE < 1,2 (beide); ipd_frac_multi_peak ≤ 2; R_chance < 0,01; HRD/"lobster" (\|Δlobster\| ≤ 0,25, Überhelligkeit < 0,4 mag); σ_ṽ < 0,10 (Z. 23–26) |
| Schablonen-Regel | ja, als Regel | Jede Katalogselektion wird in den Schablonen identisch angewendet, das Rauschen je Zone neu gezogen ("N2", Rice-Bias) (Z. 27–29) |
| Zonen | ja | Validierung s_2D 0,2–2 kau; Test 2–30 kau; Tiefbin g_N/a0 ∈ [0,03; 0,3] (Z. 33–35) |
| Schätzer | ja, als Beschreibung | E2 primär: abgeschnittener Median, ṽ < √2. E3 sekundär: Mischfit auf [0; 2,4]. Bias-Angaben: E2 ≤ +0,04, E3 0,00 (Z. 39–47) |
| Systematik | halb | f(e)-Band {empirisch je Zone, thermisch, superthermisch α = 1,3} ist Pflicht und wird "comme fourchette" veröffentlicht. Das "volle" Band für D2/D3 hat keine Zahl. Im Code (`phase_H.py`) ist es nur f(e); Dreifachmodell und Perspektive nennt §7 nur. (Z. 48–49, 66–67) |
| Entscheidung | ja | D1 STOP, D2 Newton, D3 Anomalie, D4 Grauzone (Z. 53–60). Nicht als Code. |
| Eichwert DR3 | ja, aber älterer Stand | γ_test 1,04–1,05 ± 0,01; f(e)-Band [0,955; 1,042]; Tiefbin 0,97 ± 0,13; f_trip 0,14; Δln L(1,4) = 138 (Z. 68–70). Weicht vom Papier ab (V-L1d). |
| Code, Seeds | **nein** | Code-Hash "à geler". Seeds stehen nicht im Protokoll; im Code 42/7/8/9 bzw. 77. Ein Mindest-N gibt es nicht. |
| Lieferung | Zusage | Rohhistogramme je Zone, Code, Schablonen, DR4-Injection-Grid, "présent document inchangé" (Z. 74–75) |
| Zeitnachweis | ja, für den Entwurf | Zenodo 2026-08-24T00:06:54 UTC (v1.0, GitHub-Release, Commit b16c019, auch bei Software Heritage). "15/07/2026" ist nur Selbstangabe. |

## WB-2 gegen Boufourou

WB-2-Angaben nach [S WB-ZENODO-L], Boufourou nach [S] oben.

| Achse | WB-2 (Hess, Zenodo 23108688) | Boufourou (Zenodo 22073431, Entwurf) | Folge [ES] |
|---|---|---|---|
| Skala | Γ = Verhältnis der Mediane von v~_⊥ (Geschwindigkeit) | γ = G_eff/G (G-Skala; ṽ skaliert mit √γ, Papier S. 2 Z. 77–78) | [M] γ ≈ Γ². WB-1 1,182 entspricht ≈ 1,40 in G |
| Observable | 1D-Komponente senkrecht zur Himmelsseparation (D1, perspektivfrei gewählt) | 2D-Betrag Δv_⊥ mit Winkel-Perspektivkorrektur über RV | Verschiedene Größen. Boufourous Tiefbin ist perspektivempfindlich (0,97 → 1,11) |
| Bins | Kontrolle g_N ≥ 2e-9, Test g_N ≤ 1e-10 m/s² | Validierung 0,2–2 kau, Test 2–30 kau, Tiefbin g_N 3,6e-12 bis 3,6e-11 m/s² [M] | Test- und Tiefbin überlappen nur teilweise |
| Schätzer | voller Median, Verhältnis Test/Kontrolle | E2 abgeschnittener Median **und** E3 Mischfit | Kern-Median gegen Kern plus modellierter Schwanz |
| Dreifachsysteme | nur über Schnitte (RUWE, ipd), Mock ohne Dreifachsysteme. Anteil v~ > 1,2 nur Nebendiagnose | Dreifach-Schablone im Fit (f_trip frei), Abschneidung in Daten und Schablone gleich | genau Boufourous Scheinsignal-Achse |
| Newton-Referenz | Mock-Band aus α = 1,16–1,50 (je Bin) | Zonen-Schablonen mit Rauschen und Selektion, f(e)-Band aus drei Modellen | beide hängen am Exzentrizitäts-Prior |
| Schnitte | ϖ ≥ 4 mas (250 pc), ϖ/σ ≥ 20, RUWE < 1,2, ipd ≤ 2, R_chance < 0,01, Hauptreihe, 1–30 kAU, σ_blind < 0,20, 4 ≤ M_G ≤ 12 | d < 300 pc, G < 18, \|b\| > 15°, RUWE < 1,2, ipd ≤ 2, R_chance < 0,01, lobster, σ_ṽ < 0,10 | RUWE, ipd und R_chance gleich. Der Rauschschnitt ist bei Boufourou nominell doppelt so streng (0,10 gegen 0,20), die Größen sind aber verschieden definiert |
| Schwelle "Effekt" | Γ ≥ Bandkante + 3σ. [M] Mit DR3-Kante 1,076 und σ = 0,02: Γ ≥ 1,136, also G ≥ 1,29 | E2 (Tiefbin) **und** E3 > 1,20, 1,00 mit > 5σ ausgeschlossen **und** außerhalb des Bands | Boufourou verlangt Einigkeit zweier Schätzer und Systematikfreiheit |
| Schwelle "Newton" | Γ ≤ Kante + 2σ **und** ≤ 1,17 × Unterkante − 3σ | beide < 1,15, 1,35 mit > 5σ ausgeschlossen und außerhalb des Bands | — |
| Kontrolle / STOP | Mindestens 300 Testpaare, nur der Primärarm entscheidet | D1: Validierung auf < 2 % genau, sonst STOP (DR3: +1,4 %) | [ES] Boufourous D1 hat auf DR3 nur 0,6 Prozentpunkte Rand |
| Grauzone | inconclusive | D4 mit neuer DR4-Injection-Karte | — |
| Katalog DR4 | nicht gebunden | nicht gebunden ("ou reconstruction équivalente") | gemeinsamer größter Freiheitsgrad |
| Bindung | SHA-256 von Protokoll und Skripten, Seeds, Zenodo 2026-10-02T19:19:29 UTC | Zenodo 2026-08-24T00:06:54 UTC, md5 des ZIP, kein Autor-Hash, keine Seeds im Protokoll, Status Entwurf | WB-2 ist fester gebunden, Boufourou älter und schwanzfester |
| DR3-Ergebnis | Γ = 1,182 ± 0,045 (G ≈ 1,40), INCONCLUSIVE | γ = 1,045 [1,025; 1,068] (E2), 1,05 [1,04; 1,07] (E3), 1,4 bei ≈ 16σ verworfen | gleiche Elternquelle (El-Badry 2021), andere Stichproben (250 pc gegen 200 pc Chae) |

**Wo beide bei gleichem DR4 verschieden urteilen könnten** ([H], auf Grundlage von Boufourous Injection-Gitter, CSV `phase_G_resultats.csv`):

| Wahrer Zustand in DR4 | WB-2 (erwartet) | Boufourou (erwartet) | Übereinstimmung |
|---|---|---|---|
| Newton, sauberer Schwanz (f_trip → 0) | Newton (Bandmitte) | Newton (E1 ≈ E2 ≈ E3 ≈ 1,00; Gitter E1 0,986–1,005) | ja |
| Newton + 20–30 % Rest-Dreifachsysteme | voller Median gehoben (E1-artig 1,065–1,129 in G, also 1,03–1,06 in v [M]), Newton oder inconclusive | Newton (E2 ≤ 1,044, E3 0,98–1,02) | teils |
| DR3-Lage wiederholt sich (WB-1 1,18; Boufourou 1,05) | "BOOST FAVOURED", sobald σ ≤ 0,035 [S WB-ZENODO-L, M] | D2 Newton, sobald E2-Tiefbin < 1,15 und 1,35 mit > 5σ ausgeschlossen | **nein, entgegengesetzt** |
| Echter Boost γ = 1,4 | Boost | D3 (alle Schätzer ≥ 1,26 im Gitter) | ja |
| Newton, aber Exzentrizitäts-Prior falsch | kann Boost nicht trennen (Hess selbst) | f(e)-Band fängt das auf, Newton oder D4 | eher nein |

## Regime und Moderatoren (Regel 1)

- **[ES] Zwei Regime statt "einer irrt":** WB-2 sitzt im Regime "Kern-Median ohne Schwanzmodell", Boufourou im Regime "abgeschnittener Kern plus modellierter Schwanz". Auf denselben Sternen können beide richtig rechnen und verschieden urteilen.
- **Moderator 1, Rest-Dreifachanteil × Schätzerfamilie:** synthetisch gemessen. Unter Newton ist E1 ohne Dreifachsysteme unverzerrt, mit f_trip 0,2–0,3 liegt es bei 1,065–1,129 [S CSV].
- **Moderator 2, Exzentrizitäts-Prior:** Bei Boufourou verschiebt die empirische Exzentrizität (Chae) γ um ~9 % (0,957 → 1,045) [S Papier S. 3]. Das ist das 17-Fache der erwarteten DR4-Statistik von 0,005 [M]. Bei WB-1 machte die Verengung des α-Bands aus 0,36 σ 2,36 σ [S WB-ZENODO-L].
- **Moderator 3, Rauschmodell (Rice-Bias):** Ohne zonengleich verrauschte Schablonen gab selbst E2 auf reinem Newton γ = 1,18 [S Papier S. 3 Z. 139–141]. WB-1 verrauscht seinen Mock je Paar [S WB-ZENODO-L]. Ob dessen Rauschmodell stimmt, ist offen.
- **Moderator 4, Perspektive und Observable:** Boufourous Tiefbin springt durch die Perspektivkorrektur von 0,97 auf 1,11. WB-2 umgeht das mit der 1D-Senkrechtkomponente.

## Kopplung statt Bauteil (Regel 6)

[ES] Boufourous Titel sagt es selbst: "the eccentricity–triple coupling manufactures a pseudo-signal".
- Bei γ > 1 wirken mindestens vier Wege zusammen: Dreifach-Schwanz, Exzentrizitäts-Prior, Rauschen (Rice) und Perspektive.
- Nach Boufourou addieren sich Schwanzhebel und e-Modell-Fehler ("additive with e-model mismatch", S. 5 Z. 198–200).
- Die gemeinsame Größe ist damit nicht "der Median", sondern **die Kopplung von Exzentrizitäts-Prior und Schwanzbehandlung**.
- Beide Autoren erwarten, dass bei DR4 diese Systematik entscheidet und nicht die Statistik: Hess "cannot fully separate from a boost", Boufourou "estimator systematics fully dominant".

## Unterscheidungspunkte (Regel 2)

| Paar | Wo sie messbar auseinanderlaufen | Zugänglich? |
|---|---|---|
| WB-2-Urteil gegen Boufourou-Urteil | Bei hohem Rest-Schwanzanteil (f_trip ≳ 0,2): voller Median gehoben, E2/E3 nicht. Bei sauberem Schwanz oder echtem Boost laufen sie zusammen. | Heute schon auf DR3, explorativ: E2/E3 auf den 250-pc-Paaren von WB-1 bzw. Γ von WB-1 auf der 41 760er-Stichprobe von Boufourou |
| "WB-1 = Dreifach-Scheinsignal" gegen "WB-1 hat weitere Ursachen" | Boufourous eigene Rückrechnung: voller Median auf seiner Stichprobe γ ≈ 1,12–1,20, also 1,058–1,095 in v [M], gegen 1,182 bei WB-1. Der Rest muss aus Exzentrizitätsband, Rauschen, Bins oder Observable kommen oder echt sein. | gleicher Test wie oben |
| γ = 1,00 gegen γ ≈ 1,05 (Boufourous Rest) | Nur über eine geschwindigkeitsunabhängige Exzentrizität: v–r-Winkel mit RV, wie bei WB-2. **Innerhalb des Boufourou-Protokolls nicht unterscheidbar**, solange das f(e)-Band 0,957–1,045 umfasst. | Zusatzdaten nötig |
| D2 gegen D4 bei Boufourou | Hängt an D1 (+1,4 % gegen 2 % auf DR3) und an σ des Tiefbins (DR3 0,07 bei N = 341). [M] Bei 3–5-mal mehr Paaren ≈ 0,03–0,04, dann liegt 1,35 bei γ ≈ 1,1 rund 6–8 σ entfernt. | DR4 |

## Herkunft und Seriosität (nüchtern)

- **Autor:** Hicham Boufourou, "Independent Researcher, Brussels, Belgium", Einzelautor. Auf Zenodo nur das GitHub-Handle "HBoufourou", ohne Affiliation und ohne ORCID. Ein MNRAS-Einreichungscode MN-26-2659-P ist nur Selbstangabe [S README; Zenodo-API].
- **Paket:** Code, abgeleitete Daten mit 81 088 Zeilen (gezählt), Abbildungen und Injection-CSV liegen offen bei. Die Papierzahlen zum Gitter stimmen mit der CSV bis auf eine Randzahl überein [M]. Die Methoden-Nebenbefunde (Rice-Bias, Sentinel-Werte in RV-Spalten, Parallaxenrauschen in der Perspektivkorrektur) wirken sachkundig [ES].
- **Schwächen:**
  - Injection-Gitter mit einem Seed und einer Dreifach-Modellfamilie,
  - Statusangaben zum Protokoll widersprechen sich,
  - die v2.0-Beschreibung verspricht Dateien, die fehlen,
  - die README beschreibt `etape_D_verdict.py` falsch.
- "Paper I of a series"; die Papers II/III betreffen "elasticity of the dark sector" und "superfluid dark matter" [S Papier S. 5 Z. 220–222].
- [H, Randnotiz] Codekommentare wie "Colle TOUTE la sortie" deuten auf einen Arbeitsablauf, in dem Ausgaben an einen Gesprächspartner zurückgegeben werden. Das Papier sagt dazu nichts. Für die Sache ist das nicht entscheidend.
- Peer Review gibt es nicht. Kritik oder Antworten Dritter sind nach Recherchestand keine bekannt (eine Websuche war nicht zugelassen). Statistik: 62 Aufrufe und 34 Downloads über beide Versionen.

## Gegensweep (Regel 4)

Was war so selbstverständlich, dass ich es nicht geprüft habe?

- **GS1, geprüft:** Ist Boufourous DR3-Befund "Newton"? Nur mit dem Systematikband, statistisch nicht (BF3).
- **GS2, geprüft:** Zeigt das arXiv-Papier auf genau diese Zenodo-Version? Ja, der Kommentar nennt 10.5281/zenodo.22073431 (v1.0), nicht die Concept-DOI.
- **GS3, geprüft:** Messen γ und Γ dasselbe? Nein (Skala, Observable, Bins), siehe Tabelle.
- **GS4, geprüft:** Stimmen die Papierzahlen mit `phase_G_resultats.csv`? Ja. Ausnahme: E1 super/f_trip 0,2 = 1,065 statt "≥ 1,08".
- **GS5, geprüft:** Sind D1–D4 als Code umgesetzt, und ist der DR3-Eichwert mit den DR4-Schnitten gerechnet? Beides nein (V-L2a, V-L1b; `phase_H.py` Z. 100–102).
- **GS6, nicht geprüft:** Was zeigt die Schwellenstudie T ∈ [1,2; 1,8] in v2.0? Sie betrifft genau die gebundene √2-Abschneidung von E2.
- **GS7, nicht geprüft:**
  - Gibt es ein arXiv-v2?
  - Existieren die zitierten 2026-Arbeiten? Gemeint sind Chae & Yoon 2607.14450, Banik u. a. 2602.24035, Saad & Ting 2603.11015 und Pasquini u. a. 2602.04661.
  - Wie steht es um das GitHub-Repo (spätere Tags)?
- **GS8, nicht geprüft:** Der DR4-Termin 02.12.2026 steht in zwei Fremdquellen übereinstimmend.
- **GS9, nicht geprüft:** Ob die 81 088 Paare wirklich Chaes öffentliche Stichprobe sind, ist Selbstangabe (Dateiname `Newton_dr3_MSMS_d200pc_5.csv`).

## Kalibrierung

- **(a) Gemessen bzw. geprüft:**
  - Zenodo-Metadaten beider Versionen, md5 des ZIP,
  - Wortlaut von Protokoll, Papier und README,
  - Zeilenzahlen und Injection-CSV,
  - Codeinhalte (gelesen, nicht ausgeführt).
- **(b) Verdichtet:** das Zwei-Regime-Bild "Kern-Median gegen Kern plus Schwanz", das Szenario entgegengesetzter DR4-Urteile [H] und die Kopplung von Exzentrizität und Schwanz [ES].
- **(c) Gewachsene Gewissheit ohne neue Evidenz (Warnzeichen):** Vom Abstract her wirkt Boufourou wie ein fertiger, robuster Newton-Maßstab. Das hatte auch WB-ZENODO-L übernommen. Am Volltext ist das nicht gedeckt:
  - Das Protokoll ist ein Entwurf.
  - Die DR3-Messung liegt statistisch 2–3 σ über 1,00.
  - Das Scheinsignal-Gitter hat einen Seed.
  - Unabhängig nachgerechnet ist nichts.

  Boufourous These "voller Median plus Dreifach-Schwanz ergibt ein Scheinsignal" ist **synthetisch belegt, an echten Daten nicht unabhängig geprüft und für WB-1 nach Recherchestand nicht belegt**.

## Offene Fragen

1. Erscheint die "version gelée v1.0" vor dem 02.12.? Stimmt sie mit der Datei vom 24.08. überein (SHA-256 `9d56c240…afdeff`)? Abweichungen wären nachträgliche Änderungen.
2. Was ergibt die Abschneidungsstudie T ∈ [1,2; 1,8] (v2.0, `etape_E_seuil_resultats.csv`, 308 B)?
3. Was gilt als "volles Systematikband" in D2/D3 neben f(e)?
4. Welcher DR4-Weitdoppelsternkatalog wird gebaut? Das ist für beide Protokolle offen.
5. [H] Explorativ schon auf DR3 prüfbar: E2/E3 auf den WB-1-Paaren und Γ (WB-1) auf Boufourous Stichprobe. Erst das trennt Schätzer- von Stichprobeneffekt.
6. Ungeprüft: arXiv-v2, MNRAS-Status, die zitierten 2026-Arbeiten.

## Selbstanzeigen

- **Werkzeug:** curl statt WebFetch für alle vier Abrufe, damit unveränderte Kopien entstehen. Jeder curl zählt als Abruf.
- **Abruf A3** schlug durch meinen Parameterfehler fehl (size=50, erlaubt sind 25). Dadurch fiel der arXiv-Abgleich der Zitate und eines möglichen v2 weg.
- **arXiv-Abstract:** nicht neu abgerufen, sondern aus der Kopie von WB-ZENODO-L vom 2026-10-04 22:28:35 CEST gelesen. Ein v2 nach diesem Zeitpunkt ist ungeprüft.
- **Tiefe:**
  - Der Code wurde gelesen bzw. per grep durchsucht, nicht ausgeführt.
  - `moteur_population.py`, `phase_G.py` und `phase_H.py` habe ich nur in Kopf und Stichworten gelesen.
  - Die Abbildungen habe ich nicht angesehen.
- **[M]-Werte:** von Hand. Die σ-Umrechnung aus Δln L nutzt die Wilks-Näherung mit einem Freiheitsgrad.
- **WB-2-Werte:** aus dem Dossier von WB-ZENODO-L übernommen, nicht an deren Urquelle geprüft.
- **Datenschutz:** Die private Mailadresse aus README und PDF gebe ich nicht wieder.
- **Lokale Werkzeuge:** curl, jq (nur lesend), unzip, md5sum, sha256sum, pdfinfo, pdftotext, grep, sed, cat, wc, head, tail, cut, ls, date. Kein python, awk oder perl.
- **Schreiben:** nur in `RUNDE-37/boufourou-dr4-l/`.

## Quellen

- Boufourou, H. (2026): "HBoufourou/paperI-wide-binaries: Paper I v1.0 — wide binaries + full reproducibility package". Zenodo, Software, MIT. Versions-DOI 10.5281/zenodo.22073431, Concept-DOI 10.5281/zenodo.22073430, angelegt 2026-08-24T00:06:54 UTC. https://zenodo.org/records/22073431
  - API-Kopie: `quellen/zenodo-api-22073431-20261005T002944.json` (Abruf 00:29:44 CEST).
  - ZIP: `quellen/zenodo-22073431-paperI-wide-binaries-v1.0-20261005T003037.zip` (Abruf 00:30:37 CEST, md5 52fa664092a605fae68ec448623edb44, SHA-256 5ff8a0f8…6472c0), entpackt in `quellen/archiv-22073431/`.
  - Darin `protocole/PREREGISTRATION_DR4.md` (SHA-256 9d56c240…afdeff), `README.md`, `Boufourou_2026_PaperI_wide_binaries.pdf` (Textfassung `quellen/Boufourou_2026_PaperI_pdftotext-layout.txt`), `code/`, `data/`.
- Boufourou, H. (2026): Paper I v2.0, "threshold scan, MNRAS version". Zenodo 10.5281/zenodo.22114321, angelegt 2026-08-26T16:11:22 UTC. https://zenodo.org/records/22114321
  - Nur die Metadaten gelesen: `quellen/zenodo-api-22073431-versions-20261005T003441.json` (Abruf 00:34:41 CEST).
  - Der Fehlabruf liegt in `quellen/zenodo-api-22073431-versions-20261005T003422.json`.
- Boufourou, H. (2026): "Estimator forensics for the wide-binary gravity test: the eccentricity–triple coupling manufactures a pseudo-signal, and a pre-registered protocol for Gaia DR4". arXiv:2608.24556v1, eingereicht 2026-08-25. https://arxiv.org/abs/2608.24556
  - Abstract aus `../wb-zenodo-l/quellen/arxiv-api-idlist-20261004T222835.xml`.
- Hess, M. (2026): "WB-1 … with the Frozen WB-2 Protocol for Gaia DR4". Zenodo 10.5281/zenodo.23108688. https://zenodo.org/records/23108688
  - Nur über `../wb-zenodo-l/DOSSIER.md`.
- Von Boufourou zitiert, von mir nicht geprüft:
  - Chae, K.-H. (2024), ApJ 960, 114,
  - Pittordis, C., Sutherland, W., Shepherd, P. (2025), arXiv:2504.07569 (PS25),
  - El-Badry, K., Rix, H.-W., Heintz, T. M. (2021), MNRAS 506, 2269,
  - Banik, I. u. a. (2026), arXiv:2602.24035,
  - Chae, K.-H., Yoon, Y. (2026), arXiv:2607.14450,
  - Saad, S. M., Ting, Y.-S. (2026), arXiv:2603.11015,
  - Pasquini, L. u. a. (2026), arXiv:2602.04661.

## Einfach gesagt

Der Forscher Boufourou hat schon im August öffentlich aufgeschrieben, wie er die nächsten Gaia-Daten auswerten will. Bei ihm müssen zwei Rechenwege übereinstimmen, die beide versteckte Dreifachsterne berücksichtigen. Allerdings nennt er seinen Plan selbst noch einen Entwurf, und die endgültige Fassung will er erst vor Dezember hochladen. Seine eigene Messung an den heutigen Daten liegt etwas über Newton und passt nur dann zu Newton, wenn man die Unsicherheit über die Bahnformen mitrechnet. Mit seinem Verfahren und dem von Hess könnten dieselben neuen Daten zu entgegengesetzten Urteilen führen: Ein Teil davon läge im verschiedenen Umgang mit Ausreißern, ob das alles erklärt, ist offen.
