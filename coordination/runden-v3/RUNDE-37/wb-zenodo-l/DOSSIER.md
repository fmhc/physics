# DOSSIER WB-ZENODO-L: Was legt "WB-1 / WB-2" (Hess, Zenodo, 02.10.2026) für Gaia DR4 fest?

- Feldforscher für claude-primary. Start 2026-10-04 22:21:52 CEST, Dossier begonnen 22:32:24 CEST (date).
- Grundlage: der Zenodo-Eintrag und alle fünf Dateien darin, lokal per Hash geprüft, dazu eine arXiv-API-Abfrage zu acht zitierten bzw. bekannten Arbeiten.
  Abrufe: 3 von 4. Arbeitsprotokoll mit Erwartungen vor jedem Abruf: `ARBEITSFELD.md`.
- Kennzeichen: [S …] an der Quelle gelesen, [S Abstract], [L] Gedächtnis, [M] eigene Rechnung von Hand, [ES] eigener Schluss, [H] Hypothese.
- Versiegeltes wurde nicht berührt. Ich habe keine Projektdatei außerhalb von `RUNDE-37/wb-zenodo-l/` geöffnet und keinen grep über Projektpfade gemacht.

## Ergebnis zuerst (5 Punkte)

1. **DR3-Ergebnis: eine Neigung zum Boost, kein Newton-Befund.** Im 250-pc-Hauptarm ist Γ = 1.182 ± 0.045 (8947 Kontroll- und 1794 Testpaare).
   Das liegt im Band für einen 17-%-Geschwindigkeitsboost und 2.36 σ über der *Oberkante* des Newton-Bands. Die vorregistrierte Schwelle war 3 σ, das Urteil lautet deshalb INCONCLUSIVE.
   [S WB2 Z. 179–186; S PDF S. 4; Ergebnis-JSON per jq geprüft]
2. **Die 2.4 σ entstehen erst durch einen Umbau vor der Entblindung.** Der Umbau D2 hat das Exzentrizitätsband von α = 0.8–1.6 auf α = 1.16–1.50 verengt.
   Mit dem ursprünglich eingefrorenen Band läge Γ nur etwa 0.4 σ über der Kante [M, mit dem synthetischen Band aus S WB2 Z. 149].
   Vorregistrierung, beide Umbauten (D1, D2), Entblindung und Upload fanden alle am 02.10. statt. Dass D1 und D2 vor der Entblindung lagen, ist laut Autor von außen nicht prüfbar.
   [S Abstract; S PDF S. 5]
3. **WB-2 bindet viel, aber nicht alles.** Für DR4 eingefroren sind:
   - die Skripte (per Hash),
   - alle Schnitte, die Statistik und die Bins,
   - das α-Band,
   - die Seeds, die Entscheidungsschwellen (3 σ / 2 σ), die Mindestzahl von 300 Testpaaren und die Laufreihenfolge.

   Der SHA-256 der Protokolldatei stimmt mit dem Abstract überein (lokal geprüft), Zenodo-Zeitstempel ist 2026-10-02T19:19:29 UTC.
   **Offen bleiben:** welcher DR4-Weitdoppelsternkatalog benutzt wird, die DR4-Größe für das Begleiter-Veto T1, die Version des Goblin++-Interpreters und eine Portierungsklausel mit anderem Zufallsgenerator.
4. **Einordnung: WB-1 steht methodisch im Chae-Lager und findet Chaes Zahl.** Chae 2024 nennt einen projizierten Boost von γ_vp = 1.20 ± 0.06 ± 0.05 [S Abstract 2309.10404]; WB-1 misst Γ = 1.182 ± 0.045.
   Die von WB-1 selbst zitierte Arbeit Boufourou 2026 zeigt aber an synthetischen Katalogen, dass die *Median-Schätzerfamilie*, die WB-1 benutzt, bei Newton plus 20–30 % Rest-Dreifachsystemen schon von sich aus ein Scheinsignal liefert.
   Schätzer mit abgeschnittenem Schwanz oder Mischmodell tun das nicht [S Abstract 2608.24556].
5. **Herkunft: transparent, aber ungeprüft.** Malin Hess ist "Independent researcher" und Einzelperson, ohne Zugehörigkeit und ohne ORCID im Datensatz. Gerechnet wurde in der eigenen Alpha-Sprache Goblin++, der Bericht entstand mit offengelegter Hilfe von Claude (Anthropic).
   Alle Skripte, Manifeste, Mocks und Ergebnisse liegen bei, 20 von 20 Hashes stimmen. Es gibt kein Peer Review, eine Version, 2 Aufrufe und 0 Downloads vor meinem Abruf.
   Es gibt außerdem eine *zweite*, ältere öffentliche DR4-Vorregistrierung (Boufourou, Zenodo 10.5281/zenodo.22073431), die ich nicht gelesen habe.

## Erwartungsverstöße (das Wichtigste zuerst)

| Nr | Erwartet | Gefunden | Beleg |
|---|---|---|---|
| V9 | Die zitierte Literatur stützt das Design oder ist neutral | Boufourou 2026, von WB-1 selbst zitiert: "a full-median estimator, even with a perfect eccentricity correction, recovers gamma = 1.08–1.13 from purely Newtonian universes containing 20–30% residual triples"; Schwanz-abgeschnittene bzw. Misch-Schätzer liefern ≤ 1.04 bzw. 1.00. Ein injizierter Boost wird von allen dreien gefunden (≥ 1.26). Auf der Chae-(2024)-Stichprobe ergibt sich γ = 1.045 [1.025, 1.068]. WB-1 nutzt den Median und zieht diese Folgerung für sich nicht. | [S Abstract arXiv 2608.24556v1] |
| V1/V6 | DR3 ist mit Newton verträglich (WZ1, 55 %) | Neigung von 2.36 σ zum Boost. Die Signifikanz hängt am Umbau D2: mit dem ursprünglichen α-Band sind es ≈ 0.36 σ. | [S WB2 Z. 147–186] [M] |
| V8 | Bericht und Protokoll stimmen überein | Das PDF sagt, bei "Hidden triples or eccentricity" falle Γ Richtung Newton. Das gehashte Protokoll sagt für die Exzentrizität das Gegenteil: "Γ stays elevated … the one case WB-2 cannot fully separate from a boost". Das PDF überzeichnet die Trennschärfe von WB-2. | [S PDF S. 5 Par. 7; S WB2 Z. 229–235] |
| V7 | Keine KI-Erwähnung (60 %) | "Analysis assistance, code drafting and report preparation by Claude (Anthropic)". Die Läufe hat nach eigener Angabe der Autor ausgeführt. | [S PDF S. 6] |
| V10 | Chae 2026 wird korrekt wiedergegeben | Der Abstract sagt: γ = 1.60, "dominated by two systems … exceeding their estimated Newtonian escape velocities". Die Anomalie sitzt dort im Schwanz. WB-1 nennt nur "anomaly in 36 systems" und zitiert v2 als Einzelautor; v3 hat 7 Autoren. | [S Abstract arXiv 2601.21728v3] |
| V4/V5 | Ein schlankes WB-2-Protokoll | Die "WB-2"-Datei ist das ganze WB-1-Arbeitsdokument: Vorregistrierung, Laufprotokoll, D1/D2, Ergebnisse und angehängter WB-2-Teil. Alles trägt das Datum 02.10.2026. | [S WB2 Z. 1–3, 139–237] |
| V-G2 | (aus dem Gegensweep) | Der beobachtete Kontrollmedian 0.2970 trifft den Mock bei α = 1.16 (0.2972), nicht bei α = 1.50 (0.2800). Der ganze Überschuss sitzt im Testbin: 0.3510 gegen höchstens 0.3014 im Mock. | [M aus wb1_mock_250pc.json, wb1_result_250pc.json] |
| gestrichen | [L] Der Titel des Pittordis-2025-Zitats gehöre zur Arbeit von 2023 | ~~Fehlzuordnung~~: 2504.07569v2 trägt genau diesen Titel. Mein Gedächtnis war falsch. | [S arXiv-API] |

## WZ1 bis WZ3 (Erwartungen der Karte, unverändert) mit Urteil

| Nr | Erwartung (Karte) | Urteil | Beleg |
|---|---|---|---|
| WZ1 | [H] DR3 mit Newton verträglich, kein Boost über 2 σ (55 %) | **Verfehlt.** Γ = 1.182 ± 0.045 liegt 2.36 σ über der Oberkante des Newton-Bands und 3.69 σ über der Bandmitte [M]. Die Newton-Bedingung des Papiers (Γ ≤ Kante + 2σ = 1.166) ist nicht erfüllt, die Boost-Bedingung (≥ 1.211) auch nicht, also INCONCLUSIVE. Der S1-Arm (RUWE < 1.4) liegt bei 2.9 σ. Einschränkung: Die Überschreitung von 2 σ entsteht erst durch D2 (≈ 0.36 σ mit dem ursprünglichen Band [M]). | [S WB2 Z. 179–198; S PDF S. 4; jq: z_above_newton_hi = 2.3588] |
| WZ2 | [H] WB-2 bindet Schnitte, Statistik und Schwellen zahlenmäßig, mit Zeitstempel oder Hash (70 %) | **Eingetroffen, mit Lücken.** Alles Zahlenmäßige ist gebunden (Tabelle unten). Die Protokolldatei hat SHA-256 `85ee8389…87f0` (lokal nachgerechnet = Abstract), der öffentliche Zenodo-Zeitstempel ist 2026-10-02T19:19:29 UTC. Ungebunden sind der DR4-Katalog, die T1-Größe, die Interpreter-Version und die Portierung. | [S WB2 Z. 202–237; S API created; sha256sum] |
| WZ3 | [H] Das Papier trennt ausdrücklich Kern und Schwanz (40 %) | **Eingetroffen, aber nur über die Wahl des Schätzers.** "median instead of tail" gegen Dreifachsysteme; der Anteil v~ > 1.2 dient "as a secondary diagnostic only, because hidden triples dominate that tail" (2.1 % gegen 2.6 %). Es gibt kein Kern/Schwanz-Modell und keine Dreifachsysteme im Mock. Laut Boufourou 2026 ist gerade der Median nicht schwanzfest (V9). | [S WB2 Z. 94, 119, 184; S PDF S. 4, S. 13–14] |

**Bedeutung nach Karte:** WZ2 ist eingetroffen. Damit gibt es einen fremden, vorab gebundenen Maßstab für DR4. [ES] Dazu kommen drei Punkte:
- Es gibt mindestens noch einen zweiten, älteren Maßstab (Boufourou, Zenodo 22073431, ungelesen).
- Die primäre WB-2-Entscheidung "Boost" würde einen Boost nicht von der Exzentrizitäts-Systematik trennen. Das sagt der Autor selbst.
- [M] Bleibt Γ ≈ 1.18, reicht schon σ ≤ (1.18 − 1.076)/3 ≈ 0.035 für "BOOST FAVOURED". So viel hatte S1 schon auf DR3 (0.035). DR4 dürfte also ein Boost-Urteil liefern, sobald die Neigung bleibt, gleich aus welcher Ursache.

## Daten und Statistik (WB-1, DR3)

- **Katalog** [S WB2 Z. 16–27; S PDF S. 1]
  - El-Badry, Rix & Heintz (2021), eDR3-Weitdoppelsternkatalog, Zenodo 4435257, `all_columns_catalog.fits`.
  - 1 817 594 Paare, per SHA-256 `619db1f5…bc80` eingefroren. Den Hash habe ich nicht nachgeprüft.
- **Katalogschnitte für den Hauptarm 250 pc** [S Manifest 250pc, jq; S WB2 Z. 35–43]
  - Parallaxe ≥ 4.0 mas: 214 936 Paare.
  - ϖ/σ ≥ 20 für beide Sterne: 161 827.
  - Parallaxen innerhalb 3 σ gleich: 153 210.
  - R_chance_align < 0.01: 148 217.
  - RUWE < 1.2 für beide: 92 086.
  - ipd_frac_multi_peak ≤ 2: 81 369.
  - MSMS: 67 875.
  - Nicht dupliziert: 65 241.
  - 1000 ≤ sep_AU < 30 000: 38 135, 0 Zeilen verworfen.
- **Abgeleitete Schnitte in Goblin++** [S WB2 Z. 44, 166; S PDF S. 11–12]
  - 4 ≤ M_G ≤ 12 für beide Sterne.
  - Rauschschnitt σ_blind < 0.20 (D2; ursprünglich 0.10).
  - Der Perspektivschnitt ist durch D1 entfallen.
  - Massen nach Pittordis & Sutherland 2019: M/M☉ = 10^(0.0725(4.76 − M_G)).
- **Statistik** [S WB2 Z. 73–94, 213–216; S PDF S. 3]
  - v~_⊥ ist der Betrag der Relativgeschwindigkeit senkrecht zur Himmelsseparation (gebildet in einem gemeinsamen 3D-Rahmen), geteilt durch v_c = √(G M_tot / r_p).
  - Γ = Median v~_⊥ im Testbin (g_N ≤ 1e-10 m/s²) geteilt durch den Median im Kontrollbin (g_N ≥ 2e-9 m/s²).
  - Der Fehler kommt aus 10 000 Bootstrap-Ziehungen je Bin.
- **Newton-Mock** [S PDF S. 13–14, wb1_mock.py]
  - Kepler-Bahnen mit f(e) ∝ e^α und α ∈ {1.16, 1.24, 1.32, 1.41, 1.50}, je Bin unabhängig (5×5-Gitter). Das Band ist [min, max].
  - Jedes Paar bekommt sein eigenes Gauß-Rauschen.
  - Halbachsenverteilung dN/da ∝ a^-1.6 als nicht vorregistrierte "implementation choice, logged".
  - Der Mock enthält **keine** Dreifachsysteme, Vorbeiflüge oder Zufallspaare.
- **Dreifachsysteme** [S WB2 Z. 119; S PDF S. 5]
  - Behandelt nur über RUWE- und Mehrfachpeak-Schnitte, den Median sowie die Arme S1 (RUWE < 1.4) und E1 (RUWE < 1.0).
- **Projektionseffekte** [S WB2 Z. 147; S PDF S. 3]
  - Erst über einen Perspektivschnitt behandelt; der hätte 7 Testpaare übrig gelassen.
  - D1 stellt deshalb auf die Senkrechtkomponente um, die der Radialgeschwindigkeits-Perspektivterm nicht erreicht.

### DR3-Ergebnis mit Fehlern [S WB2 Z. 179–198; S PDF S. 4; JSON per jq gleich]

| Arm | Kontrolle | Test | Γ | Newton-Band | über Kante | Urteil |
|---|---|---|---|---|---|---|
| 250 pc, RUWE < 1.2 (primär) | 8 947 | 1 794 | 1.182 ± 0.045 | 0.960–1.076 | 2.4 σ | INCONCLUSIVE |
| 130 pc (sekundär) | 1 214 | 434 | 1.248 ± 0.104 | 0.957–1.083 | 1.6 σ | inconclusive |
| S1 RUWE < 1.4 (vorregistriert) | 10 000 | 2 011 | 1.177 ± 0.035 | 0.961–1.075 | 2.9 σ | inconclusive |
| E1 RUWE < 1.0 (explorativ) | 1 173 | 248 | 1.308 ± 0.125 | 0.956–1.068 | 1.9 σ | inconclusive (< 300) |

- Die Mediane im Hauptarm sind 0.2970 (Kontrolle) und 0.3510 (Test). Der Schwanzanteil v~_⊥ > 1.2 liegt bei 2.1 % bzw. 2.6 %.
- [M] 0.3510/0.2970 = 1.1818. 1.182² = 1.397 ist das G-Äquivalent.

## Was WB-2 für DR4 genau bindet [S WB2 Z. 202–237]

| Element | Gebunden? | Wert / Bemerkung |
|---|---|---|
| Skripte | ja, per SHA-256 | wb1_pairs.gbl v3 `d43b90b6…efaa2`, wb1_mock.py `915ca319…a80e`, wb1_stats.py `a0aa7b2d…77cb`. Alle drei habe ich lokal nachgerechnet (SHA256SUMS 20/20 OK). |
| Katalogschnitte | ja, zahlenmäßig | ϖ ≥ 4.0 mas; ϖ/σ ≥ 20; Parallaxen innerhalb 3σ gleich; Zufallspaar-Wahrscheinlichkeit < 1 %; RUWE < 1.2; Mehrfachpeak ≤ 2; Hauptreihenpaare; nicht dupliziert; 1000–30 000 AU |
| Abgeleitete Schnitte | ja | 4 ≤ M_G ≤ 12; σ_blind < 0.20 |
| Statistik, Bins | ja | Γ = Median-Verhältnis von v~_⊥; Kontrolle g_N ≥ 2e-9, Test g_N ≤ 1e-10 m/s² |
| Newton-Band | ja | α = 1.16–1.50 je Bin; Seed 20261002 |
| Entscheidung | ja | Boost: Γ ≥ Kante + 3σ. Newton: Γ ≤ Kante + 2σ **und** ≤ 1.17 × Unterkante − 3σ. Sonst inconclusive. Mindestens 300 Testpaare. Bootstrap 10 000, Seed 20261003. Nur der Primärarm entscheidet. |
| Laufreihenfolge | ja | einfrieren, extrahieren, blind laufen, Mock versiegeln, entblinden, Statistik |
| Vorhersage | ja, als Tabelle | Boost: Γ ≈ 1.18, ≥ 3σ, T1 gleich. Dreifachsysteme: Γ fällt, am stärksten in T1. Exzentrizität: Γ bleibt hoch und driftet, "cannot fully separate from a boost". |
| Erlaubte Änderungen | begrenzt | (1) SHA-256 des DR4-Katalogs, (2) Abbildung der Spaltennamen ("No cut values may change"), (3) Dateiaufteilung. Jede Änderung wird vor der Extraktion protokolliert. |
| **DR4-Katalog** | **nein** | Welcher Katalog, wer ihn baut und wie R_chance_align und binary_type entstehen, bleibt offen. [ES] Ein El-Badry-Katalog für DR4 ist mir nicht bekannt [L]. Hier liegt der größte Freiheitsgrad. |
| **T1-Veto** | **halb** | Beschleunigung ≥ 5σ in der DR4-Epochenastrometrie. Welche DR4-Größe das ist, wird erst nach Erscheinen "fixed and logged before extraction, without looking at velocities". Sekundärarm, ändert das Urteil nicht. |
| Interpreter / Umgebung | nein | Die Version von Goblin++ (0.1.0-alpha.19 laut PDF) und die Versionen von Python/numpy sind nicht im WB-2-Block gebunden. |
| Portierung | Klausel | Wenn Goblin++ Median und Zufallszahlen kann, ist ein Umzug erlaubt. Die CSVs müssen bitgleich sein, das Band nur "within its Monte Carlo error" (anderer Zufallsgenerator). Das schwächt die Seed-Bindung. |
| Zeitnachweis | ja für WB-2 | Öffentlicher Zenodo-Zeitstempel. Für die WB-1-Reihenfolge (D1/D2 vor der Entblindung) gibt es nur lokale Belege, "which outside readers cannot independently verify". |

Grenzen, die der Autor selbst nennt [S WB2 Z. 235]:
- DR4 misst überwiegend dieselben Sterne neu und ist damit keine unabhängige Population.
- Gegen die Exzentrizitäts-Systematik hilft erst eine von der Geschwindigkeit unabhängige Exzentrizitätsmessung, etwa v–r-Winkel mit Radialgeschwindigkeiten.

## Einordnung gegen Chae, Banik u. a. (Literaturstand)

| Arbeit | Daten | Schätzer / Dreifachsysteme | Ergebnis | Beleg |
|---|---|---|---|---|
| Chae 2023, ApJ 952, 128 | DR3, 26 615 WB < 200 pc | deprojizierte Beschleunigungsrelation; Mehrfachanteil bei 10^-8 m/s² geeicht | g_obs/g_pred = 1.43 ± 0.06 bei g_N = 10^-10.15 → [M] v-Faktor 1.196 ± 0.025 | [S Abstract 2305.04613] |
| Chae 2024, ApJ | 2 463 "statistisch reine" Paare | strenge Schnitte; gestapeltes projiziertes Geschwindigkeitsprofil | γ_g = 1.49 +0.21/−0.19; γ_vp = 1.20 ± 0.06 ± 0.05 (s ≳ 5 kau) | [S Abstract 2309.10404] |
| Hernandez 2023, MNRAS | DR3 | ΔV-Skalierungen, Kontaminanten über Gaia-Binärwahrscheinlichkeiten und RV ausgeschlossen | Anomalie bei a ≲ 2 a0 "confirmed" | [S Abstract 2304.07322] |
| Banik u. a. 2024, MNRAS 527, 4573 | DR3, 8 611 WB < 250 pc, 2–30 kAU | volle Verteilung, EFE-Bahnen; Sichtlinien-Kontamination und unentdeckte Begleiter modelliert | α_grav = −0.021 +0.065/−0.045; MOND bei 16σ ausgeschlossen (Modellvergleich 19σ). v4 vom 28.09.2026 korrigiert Abb. 15. | [S Abstract, Kommentar 2311.03436v4] |
| Pittordis, Sutherland & Shepherd 2025, OJAp | DR3, neue Schnitte, FLAME-Massen | Mischfit aus Doppel-, Dreifach-, Vorbeiflug- und Zufallspopulation | Newton besser; v2: "delta-chi2 vs MOND somewhat reduced"; Dreifachpopulation noch nicht voll verstanden | [S Abstract, Kommentar 2504.07569v2] |
| Boufourou 2026, arXiv | Synthetik + Chae-(2024)-Stichprobe, 81 088 Paare | drei Schätzerfamilien an Katalogen mit bekannter Wahrheit validiert | Median: Scheinsignal 1.08–1.13 bei Newton plus 20–30 % Dreifachsystemen; real gemessen γ = 1.045 [1.025, 1.068]; DR4-Protokoll auf Zenodo | [S Abstract 2608.24556v1] |
| Chae u. a. 2026, arXiv v3 | 36 WB < 150 pc mit RV-Fehler < 100 m/s | 3D-Geschwindigkeiten, viele Kontaminations-Diagnosen | γ = 1.60 +0.24/−0.14, "dominated by two systems" über Newtons Fluchtgeschwindigkeit | [S Abstract 2601.21728v3] |
| Cookson u. a. 2026, MNRAS 547 stag342 | ? | ? | "no evidence for MOND", nur laut WB-1-Zitat, **nicht geprüft** | [S WB2 Z. 126; S PDF S. 6] |
| **WB-1, Hess 2026** | El-Badry eDR3, 250 pc | Median-Verhältnis v~_⊥ Test/Kontrolle, Mock ohne Dreifachsysteme, α-Band verengt | Γ = 1.182 ± 0.045 (G-Äquivalent 1.40) | [S, oben] |

- **Gleiche Statistik oder neue?** [ES] Die Variante ist neu: ein Medianverhältnis der Senkrechtkomponente zwischen zwei g_N-Bins, geeicht an einem Mock-Band. Familiär ist sie Chaes gestapeltem projiziertem Profil (γ_vp) am nächsten, nicht Banik/Pittordis (volle Verteilung mit Schwanzmodell).
  WB-1 findet numerisch Chaes Wert: 1.182 ± 0.045 gegen 1.20 ± 0.06 ± 0.05 [M].
- **Wo der Unterschied entsteht.** [S Abstract 2608.24556, synthetisch belegt] Laut Boufourou liegt er in der Kopplung von Schätzer und Rest-Dreifachanteil. Der Median wird schon unter Newton angehoben, abgeschnittene oder Mischschätzer nicht, ein echter Boost erscheint in allen dreien.
  [ES] WB-1 hat keinen Mischschätzer und keinen abgeschnittenen Schätzer gerechnet und deshalb diese Probe nicht.
  [M] Boufourous Median-Scheinsignal entspricht nur +4 bis +6 % in der Geschwindigkeit (√1.08 bis √1.13). Der WB-1-Überschuss ist +18 %. Bei anderer Stichprobe und anderem Median ist das ein Größenordnungsvergleich, kein Urteil.

## Regime und Moderatoren (Regel 1)

- **[ES] Regime A, "Kern-Median":** Kern-Median, feste schmale Exzentrizität, Dreifachsysteme nur über Schnitte. Dazu gehören Chae 2023/2024 und WB-1 mit Boost ≈ 1.2 in der Geschwindigkeit. Hernandez 2023 meldet ebenfalls eine Anomalie, im Abstract aber ohne Zahl.
- **[ES] Regime B, "volle Verteilung":** volle Verteilung, Schwanz als Dreifach-, Vorbeiflug- und Zufallspopulation modelliert. Dazu gehören Banik 2024, Pittordis 2023/2025 und Boufourou 2026, alle mit Newton.
- **Vermuteter Hauptmoderator:** Schätzerfamilie × Rest-Dreifachanteil. Synthetisch getestet hat das Boufourou [S Abstract]; auf WB-1 ist es nicht geprüft.
- **Zweiter Moderator: das Exzentrizitäts-Prior.** WB-1 zeigt seine Hebelwirkung selbst: ≈ 0.36 σ mit α 0.8–1.6, 2.36 σ mit α 1.16–1.50 [M].
- **Dritter Moderator: das Rauschmodell.** Katalogfehler werden ohne Aufblähfaktor übernommen, im Testbin liegt σ bis 0.20 bei einem Median von ≈ 0.30.
  [M grob, Gauß-Näherung] 30 % unterschätzte Fehler heben Γ um ≈ 0.03, also ≈ 0.6 σ. Allein reicht das nicht, ist aber nicht vernachlässigbar. Im Papier steht es nicht als Systematik.
- **Drittes Regime:** kleine 3D-Stichproben (Chae u. a. 2026) mit einem Signal, das an zwei Systemen über der Fluchtgeschwindigkeit hängt, also ein Schwanz-Signal [S Abstract].

## Kopplung statt Bauteil (Regel 6)

[ES] Γ > 1 hat mindestens fünf Wege:
- echter Boost,
- unentdeckte Begleiter,
- Exzentrizitätsunterschied zwischen den Bins,
- unterschätztes Rauschen,
- Vorbeiflüge und Zufallspaare.

Drei davon (Begleiter, Rauschen, Vorbeiflüge/Zufallspaare) addieren eine Störgeschwindigkeit δv, die von v_c nahezu unabhängig ist. In v~ = v/v_c wird sie mit 1/v_c verstärkt, also am stärksten im Testbin. Die gemeinsame Größe ist **δv/v_c**.
Die Exzentrizität wirkt anders: Sie verändert die Form der Verteilung, nicht über δv. Ein MOND-Boost wirkt *multiplikativ* und hängt nur von g_N ab.

## Unterscheidungspunkte (Regel 2)

| Paar | Wo sie messbar auseinanderlaufen | Zugänglich? |
|---|---|---|
| Boost gegen unentdeckte Begleiter | T1-Veto mit DR4-Epochenastrometrie: Begleiter lassen Γ in T1 fallen, ein Boost hält Γ [S WB2]. Schwanz-abgeschnittene bzw. Mischschätzer: Newton plus Dreifachsysteme ≤ 1.04, Boost ≥ 1.26 (G-Skala) [S Abstract Boufourou]. | DR4 bzw. heute schon auf DR3 |
| Boost gegen additive Störungen (δv/v_c) | [ES/H] Γ getrennt nach Gesamtmasse bei *festem* g_N (v_c ∝ (G M g_N)^¼). Additive Störungen heben Γ für massearme Paare, ein Boost bleibt flach. Γ als Funktion des Rauschschnitts (0.10 gegen 0.20): Rauschfehler wachsen mit, ein Boost nicht. | heute auf DR3, explorativ |
| Boost gegen Exzentrizitäts-Systematik | Nur über eine geschwindigkeitsunabhängige Exzentrizität (v–r-Winkel mit RV) [S WB2 Z. 235]. **Innerhalb von WB-2 empirisch nicht unterscheidbar**, das sagt der Autor selbst. | Zusatzdaten nötig |
| Kontrollbin-Absolutlage | [ES] Der beobachtete Kontrollmedian passt zu α ≈ 1.16. Trägt die absolute Mock-Skala, liegt Γ ≈ 3.7σ über dem passenden Newton-Wert ([M] 0.30135/0.29716 = 1.0141, (1.1821 − 1.0141)/0.0449 = 3.74). Trägt sie nicht (a^-1.6 und Massenrelation sind nicht vorregistriert), sagt die Lage nichts. | zweiseitig, nur Hinweis |

## Gegensweep (Regel 4)

Was war so selbstverständlich, dass ich es nicht geprüft habe?

- **G1, geprüft.** Stimmen Text und Maschinendaten überein? Ja. Ergebnis-, Mock- und Manifest-JSON (per jq) sind in allen Zahlen deckungsgleich mit PDF und Protokoll. Die Schnittkette 1 817 594 → 38 135 ist vollständig dokumentiert.
- **G2, geprüft.** Woher kommt die Bandoberkante? Aus Test-α = 1.16 gegen Kontroll-α = 1.50 (0.30135/0.27999 = 1.0763 [M]).
  Die Daten im Kontrollbin passen aber zu α ≈ 1.16 und nicht zu 1.50. Die Oberkante ist damit sehr konservativ gewählt, wenn man der absoluten Mock-Skala traut (V-G2).
- **G3, geprüft.** Sind die Zitate echt? Ja, alle 8 IDs existieren. Zwei Wiedergaben sind unvollständig (V9, V10). Keine Halluzination.
- **G4, nicht geprüft.** DR4-Termin 02.12.2026: nur laut PDF S. 5 und [L].
- **G5, nicht geprüft.** Der Hash des Katalogs (1.8 GB).
- **G6, teilweise.** Goblin++ ist Alpha-Software mit stillen Namensfallen ("h" wird zur Planck-Konstante). Im Skript heißen Variablen k und n. Plausible Mediane (≈ 0.30) und die Übereinstimmung von Kontrollmedian und Python-Mock sprechen gegen einen stillen Konstantenfehler. Beweis ist das keiner.
- **G7, nicht geprüft.** Ist 1.17 der richtige MOND-Faktor für den Median von v~_⊥ im Bin g_N ≤ 1e-10? Banik u. a. nennen ≈ 20 % erst "at asymptotically large separations" [S Abstract]. WB-1 setzt einen festen Faktor statt einer EFE-Rechnung.
- **G8.** Die σ enthalten nur die Bootstrap-Statistik. Systematik geht allein über das α-Band ein.
- **Kritik oder Antworten zum Papier:** nach Recherchestand keine. Das Papier ist 2 Tage alt, hat eine Version, 2 Aufrufe und 0 Downloads [S Zenodo-API]. Zenodo hat keine Kommentarfunktion. Eine Websuche war nicht zugelassen.

## Kalibrierung

- **(a) Gemessen bzw. geprüft:**
  - alle Zahlen von WB-1 aus den beigelegten Dateien,
  - die Hashes (20/20 und der WB-2-Hash),
  - die Existenz und die Abstracts der 8 arXiv-Arbeiten.
- **(b) Verdichtet:** das Zwei-Regime-Bild (Schätzerfamilie), die Größe δv/v_c, die Abhängigkeit der 2.4σ von D2 [M].
- **(c) Gewachsene Gewissheit ohne neue Evidenz (Warnzeichen):** Nach dem Boufourou-Abstract wuchs meine Neigung, WB-1 als Median-Scheinsignal zu lesen.
  Dahinter steht nur der Abstract eines ungeprüften Einzelautor-Preprints. Dessen eigene Zahl (+4 bis +6 %) deckt die +18 % von WB-1 nicht.
  WB-1 ist deshalb **nach Recherchestand nicht als Scheinsignal belegt und nicht widerlegt**.

## Offene Fragen

1. Boufourous DR4-Protokoll (Zenodo 10.5281/zenodo.22073431) lesen und mit WB-2 vergleichen? Das lag außerhalb meines Mandats (nur Zenodo 23108687).
2. Welcher DR4-Weitdoppelsternkatalog wird mit R_chance_align und binary_type existieren, und von wem? WB-2 hängt daran, bindet es aber nicht.
3. Cookson u. a. 2026 ist ungeprüft. Ebenso ungeprüft ist die PDF-Aussage, Hwang u. a. fänden 10³-AU-Paare exzentrischer als 10⁴-AU-Paare; der Abstract sagt nur "superthermal at >10^3 AU".
4. Was korrigiert Banik u. a. v4 (28.09.2026) an Abb. 15?
5. [H] Prüfbar schon auf DR3, explorativ: Γ nach Masse bei festem g_N, Γ beim Rauschschnitt 0.10, und ein Schwanz-abgeschnittener bzw. Mischschätzer auf denselben WB-1-Paaren.

## Selbstanzeigen

- **Werkzeug:** curl statt WebFetch für alle drei Abrufe. So entstehen unveränderte Quellenkopien; WebFetch liefert nur eine Zusammenfassung eines Kleinmodells. Jeder curl zählt als ein Abruf, das Budget von 4 ist eingehalten (3 genutzt).
- **Zweiter Abruf:** Statt nur der PDF habe ich das Zenodo-files-archive geholt, also alle 5 Dateien des Eintrags in einem Abruf. Das ist "die Datei des Eintrags", nur vollständig.
- **arXiv:** Die eine arXiv-Abfrage enthielt 8 IDs. Neben den 3 von WB-1 zitierten waren 5 zur Prüfung meiner [L]-Angaben dabei.
- **Lokale Werkzeuge:** unzip, sha256sum, md5sum, cmp, pdfinfo, pdftotext, jq (nur lesend), grep, sed und tr (nur Anzeige). Kein python, awk oder perl.
- **Tiefe:** Die Code-Abschnitte habe ich gelesen, aber nicht ausgeführt. Ein Nachrechnen der Pipeline fand nicht statt.
- **[M]-Werte:** von Hand bzw. aus JSON-Zahlen. Die Rauschabschätzung ist eine grobe Gauß-Näherung.
- **Zeitbox:** eingehalten (Start 22:21:52; Ende siehe ARBEITSFELD.md).

## Quellen

- Hess, M. (2026): "WB-1: A Preregistered Gaia Wide-Binary Test of Low-Acceleration Gravity, with the Frozen WB-2 Protocol for Gaia DR4". Zenodo, Concept-DOI 10.5281/zenodo.23108687, Version 10.5281/zenodo.23108688, v1.0, 02.10.2026. https://zenodo.org/records/23108688
  - Kopien: `quellen/zenodo-api-23108687-20261004T222233.json` (Abruf 22:22:33 CEST) und `quellen/zenodo-23108688-files-archive-20261004T222336.zip` (Abruf 22:23:36 CEST), entpackt in `quellen/archiv-23108688/`.
  - Textfassung: `quellen/WB1_report_pdftotext-layout.txt`.
- arXiv-API, id_list-Abfrage, 22:28:35 CEST, Kopie `quellen/arxiv-api-idlist-20261004T222835.xml`. Enthalten:
  - Boufourou, H. (2026), arXiv:2608.24556v1. https://arxiv.org/abs/2608.24556
  - Chae, K.-H. u. a. (2026), arXiv:2601.21728v3. https://arxiv.org/abs/2601.21728
  - Pittordis, C., Sutherland, W., Shepherd, P. (2025), arXiv:2504.07569v2, OJAp. https://arxiv.org/abs/2504.07569
  - Banik, I. u. a. (2024), MNRAS 527, 4573, arXiv:2311.03436v4. https://arxiv.org/abs/2311.03436
  - Chae, K.-H. (2023), ApJ 952, 128, arXiv:2305.04613v4. https://arxiv.org/abs/2305.04613
  - Chae, K.-H. (2024), ApJ, arXiv:2309.10404v4. https://arxiv.org/abs/2309.10404
  - Hwang, H.-C., Ting, Y.-S., Zakamska, N. L. (2022), MNRAS 512, 3383, arXiv:2111.01789v2. https://arxiv.org/abs/2111.01789
  - Hernandez, X. (2023), MNRAS, arXiv:2304.07322v3. https://arxiv.org/abs/2304.07322
- Nur zitiert, nicht geprüft: Cookson, S. A. u. a. (2026), MNRAS 547, stag342; El-Badry, Rix & Heintz (2021), MNRAS 506, 2269; Zenodo 4435257.

## Einfach gesagt

Eine unabhängige Einzelperson hat mit KI-Hilfe getestet, ob weit getrennte Doppelsterne schneller umeinander kreisen, als Newton erlaubt. In den heutigen Gaia-Daten zeigt sich etwa 18 % mehr Tempo. Das reicht aber nicht über die selbst gesetzte Messlatte, und sichtbar wird es erst, nachdem am selben Tag die Annahme über die Bahnformen enger gestellt wurde.

Für die nächste Gaia-Datenausgabe sind Rechenweg und Schwellen vorab öffentlich festgeschrieben, nur welcher Sternkatalog dann benutzt wird, steht noch nicht fest. Eine andere Arbeit, die das Papier selbst zitiert, zeigt: Genau diese Art zu mitteln kann durch versteckte dritte Sterne ein Scheinsignal liefern, allerdings ein kleineres als die 18 %.
