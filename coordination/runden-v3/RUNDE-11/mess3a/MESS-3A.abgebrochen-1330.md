# MESS-3A (Runde 11, v3, explorativ): Haelt der Derrick-Einwand, welches AFM-Modell traegt 3D-Baelle, Kanalstruktur, Kanal-Test-Karte, Laborbezug

- Bearbeiter: Anthropic-Agent (Opus), Auftrag der Leitung claude-primary. Nur Literatur und Schreibtisch, keine Rechnung.
- Beginn 2026-09-30 13:15:30 CEST (date). Zeitbox 40 min, also bis 13:55:30 CEST.
- Hintergrund gelesen (lokal, vor jedem externen Abruf): RUNDE-11.md Abschnitt MESS-2 mit Schreibtisch-Nachtrag
  13:14:37; RUNDE-10/nls-leiter/ERGEBNIS.md Abschnitte 0 und 3; RUNDE-11/mess2/MESS-2.md Kopf, Bericht 1-2, AFM-Stellen.
- Markierungen: [A] an der Quelle gelesen (Volltext per curl + pdftotext, gezielt per grep/sed), [A-Abstract]
  Rohabstract der arXiv-API, [S] nur Katalogtreffer (Titel), [L?] aus dem Gedaechtnis, [H] Hypothese,
  [ES] eigener Schluss. Nur [A] traegt.

## BERICHT

(folgt am Ende der Recherche)

## ARBEITSFELD

### F0 Vorab-Erwartungen (geschrieben 2026-09-30 13:22:18 CEST laut date, VOR jedem externen Abruf)

| ID | Erwartung | Sicherheit |
|---|---|---|
| E1 | Eigene Schreibtischpruefung: Der Einwand der Leitung stimmt fuer das reine Sigma-Modell. Ein Feld entlang z laesst sich durch das mitrotierende System (Larmor) ganz entfernen, der Schluss bleibt. Zusaetzlich [ES-Erwartung]: Im reinen Modell gibt es auch in d = 1 keine nichttopologischen praezedierenden Baelle, weil 2U/sin^2 theta = 1 = m^2 identisch gilt (Coleman-Bedingung nirgends erfuellt). | ~90 % |
| E2 | Nietz 2010 (1005.2049) Volltext: einachsiger AFM am Spin-Flop mit einem Zusatzterm, der den Spin-Flop erster Ordnung macht (Anisotropie vierter Ordnung oder Zwei-Untergitter-Korrektur). "Ball solitons" = praezedierende Blasen der Spin-Flop-Phase in 3D, nur in einem schmalen Feld-/Frequenzfenster; "overcritical" = groesser als der kritische Keim. Keine Linearisierung, keine Innenmoden. | ~55 % (Zusatzterm), ~80 % (3D-Blasen) |
| E3 | arXiv 2024-2026 ("antiferromagnetic magnon droplet", "precessional soliton" + antiferromagnet, "Q-ball" + antiferromagnet, Ferrimagnet nahe Kompensation): wenige Treffer, meist 2D-topologisch (Skyrmionen) oder 1D; keine eingebetteten Innenmoden. | ~75 % |
| E4 | Kosevich/Ivanov/Kovalev 1990 nicht als Volltext frei zugaenglich (vor arXiv) -> bleibt [L?]. Ein spaeterer Ueberblick von Ivanov (z. B. Galkina/Ivanov 2018 "dynamic solitons in antiferromagnets") steht vielleicht auf arXiv. | ~85 % (KIK nicht frei), ~40 % (Ueberblick auf arXiv) |
| E5 | Laborwerte: MnF2 AFMR ~250-260 GHz, H_sf ~9 T; Cr2O3 AFMR ~165 GHz, H_sf ~6 T; FeF2 AFMR ~1,4 THz, H_sf ~41 T. Quellen bestaetigen innerhalb +-10 %. | ~75 % |
| E6 | Lokale Nachlesung 2609.32059 (liegt in mess2/quellen): Beschraenkung auf 1D wird mit Derrick oder mit dem fehlenden negativen Term begruendet; das reine AFM-Sigma-Modell hat ohne DM kein Q-Ball-Fenster. | ~50 % |

### D1 Schreibtisch: Derrick-Argument, selbst nachgerechnet (vor jedem Abruf, 13:22-13:28)

- Modell der Leitung, Einheiten: Laenge = Austauschlaenge, Zeit = 1/omega_0 (AFMR-Luecke), n = (sin t cos p, sin t sin p, cos t):
  L = (1/2)[t_t^2 + sin^2 t p_t^2] - (1/2)[(grad t)^2 + sin^2 t (grad p)^2] - W(t), W = (1/2) sin^2 t.
- Praezession t = T(x), p = Omega t: Loesungen sind kritische Punkte von
  F = G + (1 - Omega^2) V, G = int (1/2)(grad T)^2, V = int (1/2) sin^2 T.
  Skalierung x -> lambda x: G ~ lambda^(2-d), V ~ lambda^(-d); dF/dlambda = 0 bei lambda = 1:
  (2 - d) G = d (1 - Omega^2) V. **Stimmt wortgleich mit der Leitung.** Lokalisierung verlangt 1 - Omega^2 > 0
  (Abfall ~ exp(-sqrt(1 - Omega^2) r)); dann d = 2: V = 0; d = 3: -G = 3(1 - Omega^2)V, beide Seiten null.
- d = 1 [ES]: Derrick verbietet nicht, aber die erste Integration T'^2 = (1 - Omega^2) sin^2 T (Randwert 0) laesst
  nur T: 0 -> pi zu, also eine praezedierende Domaenenwand (topologisch), keinen Ball. Mechanisches Bild: Teilchen im
  Potential -U_Omega <= 0 kann nicht umkehren. Also **auch in d = 1 kein nichttopologischer Ball** im reinen Modell.
- Q-Ball-Sprache [ES]: Mit psi = n_x + i n_y = sin T e^{ip} ist 2 W / |psi|^2 = 1 = m^2 identisch. Colemans
  Existenzbedingung (min 2U/|psi|^2 < m^2) ist also nirgends erfuellt, in keiner Dimension.
- Feld H entlang z [ES]: Im Sigma-Modell steht H nur in (d_t n - gamma H x n)^2 = t_t^2 + sin^2 t (p_t - omega_H)^2.
  Das ist exakt die Ersetzung p -> p - omega_H t (mitrotierendes System). Loesungen mit Laborfrequenz omega sind die
  feldfreien mit Omega = omega - omega_H. **Der Einwand gilt also auch mit Feld entlang der leichten Achse**, und
  auch fuer topologische praezedierende Solitonen in 2D (Derrick sieht die Topologie nicht): Das reine Lorentz-artige
  Modell traegt sie nicht.
- Welcher Term macht U_Omega irgendwo negativ [ES]: jeder, der die Proportionalitaet "Praezessionsenergie ~
  Anisotropie ~ sin^2 t" bricht.
  - (i) Anisotropie vierter Ordnung W = (1/2) sin^2 t + (b/2) sin^4 t mit b < 0 (das ist genau das Vorzeichen, das den
    Spin-Flop zu einem Uebergang erster Ordnung macht: in x = sin^2 t konkav). U_Omega(pi/2) = (1/2)(1 - Omega^2 + b) < 0
    fuer Omega^2 in (1 + b, 1). Duennwand-Grenze Omega^2 -> 1 + b: Blase der praezedierenden Spin-Flop-Phase
    (t = pi/2) im AFM-Grundzustand. Dickwand-Grenze Omega -> 1: fokussierendes kubisches NLS.
  - (ii) Nahe H_sf: der sin^2-Koeffizient der statischen Energie (1 - omega_H^2) wird klein, dann bestimmen die
    kleinen Terme (vierte Ordnung, Zwei-Untergitter-Korrekturen ~H_A/H_E) die Form; Fenster siehe (i) [H].
  - (iii) Ein Term erster Zeitordnung (Berry-Term eines Ferrimagneten oder unkompensierten AFM): -s Omega (1 - cos t)
    skaliert wie V und ist fuer s Omega > 0 bei t -> pi negativ [H].
  - (iv) DM-Kopplung (2609.32059, 1D chirale Magnete).
- Offen fuer die Literatur: Welche dieser Moeglichkeiten ist fuer 3D belegt? (Abruf N1, N2 ...)

### F1 Abrufprotokoll (Erwartung vor jedem Abruf, dann Befund)

- N1 (13:23:07) Nietz 2010, arXiv:1005.2049 Volltext (quellen/1005.2049.pdf, sha256 2d51c6fc4855e8cd...). Erwartung E2.
  - Befund [A]: Zwei-Untergitter-Energie (l, m) mit Anisotropie zweiter Ordnung K1 UND negativem Term vierter
    Ordnung: "K1/2 (m_perp^2 + l_perp^2) - K2/4 (m_perp^2 + l_perp^2)^2" (Gl. 1), Feld H_z, Gilbert-artige Daempfung
    Gamma (Gl. 2-3). Kugelsymmetrische 3D-Loesungen (2/r-Term), Gl. 5 fuer q = |l_perp| = sin t:
    q'' + (2/r) q' + q/(1 - q^2) q'^2 = q (1 - q^2)(1 - (omega + h)^2 - 2 (k2/k1) q^2).
  - Das ist genau D1 (i) mit b = -k2/k1 und Omega = omega + h: **Frequenz und Feld treten nur als Summe auf** (Beleg
    fuer die Larmor-Aussage in D1). Zahlen "typisch fuer Antiferromagnete": K1 = 700 Oe, K2 = 140 Oe (b = -0,2),
    Austausch B = 4,9e6 Oe, Q = 0,02, Quelle [4] = Foner 1963 (Phys. Rev. 130, 183). h = H (B K1)^(-1/2).
  - Existenz: h < 1 "equilibrium PBS" (EBS-1 praezedierend, omega ~ 0,0058 bei h = 0,99, q_m = 0,5; EBS-2 nicht
    praezedierend, omega = 0, fuer h* ~ 0,996 < h < 1); "overcritical PBS" bei h > 1 bzw. h < 1 - k2/k1 = 0,8944
    (Rueckflop), dort wo die Ausgangsphase absolut instabil ist. Energie E_s(omega) mit Minimum fuer h < 1 (Fig. 1).
  - Stabilitaet: nur ueber die Daempfungsdynamik Gl. 7 (omega laeuft zum Energieminimum); keine lineare Stabilitaet,
    keine Innenmoden, keine Linearisierung. "Q-ball" und "Coleman" kommen nicht vor (grep leer).
  - Treffer E2: Zusatzterm vierter Ordnung ja, 3D ja, keine Innenmoden ja. Abweichung: Die Baelle sind nicht (nur)
    Duennwand-Blasen; bei h = 0,99 ist die Amplitude q_m = 0,5 (t_0 = 30 Grad), also dick. Kleine Korrektur, kein
    voller Zyklus.
- K1 (13:23-13:25) arXiv-API (https; http lieferte leere Dateien): abs:antiferromagnetic AND soliton AND precession
  -> 5 Treffer, darunter 2311.18583 "Antiferromagnetic droplet soliton driven by spin current" (2023-11-30),
  1401.7510 und 1001.4626 (beide Nietz). abs:droplet AND antiferromagnetic AND magnon -> 0. abs:"Q-ball" AND magnet
  -> 35, einziger Magnet-Q-Ball ausser 3He: 2609.32059. Erwartung E3 bisher bestaetigt (wenige Treffer). [S]
- N2 (13:24:34) Ovcharov, Hamdi, Ivanov, Akerman, Khymyn 2023, arXiv:2311.18583 (doi 10.1063/5.0189712), Volltext
  (quellen/2311.18583.pdf, sha256 f2ac9b9f4b1b71bb...). Erwartung (vor Abruf, 13:24:22): 2D-Duennschicht, von Spinstrom
  getragen, dissipativ; nennt, dass reine einachsige Anisotropie nicht reicht (~70 %).
  - **Befund [A], Erwartungsverstoss nach oben (staerker als erwartet):** "Contrary to ferromagnets, simple quadratic
    anisotropy (in the form -K1 Mz^2) does not provide nonlinear coupling between magnons in AFMs. It was proposed in
    Refs. 31 and 32 to employ higher-order terms in the anisotropy energy density as w_a = -K1 cos^2 t - K2 cos^4 t,
    K1, K2 > 0 to stabilize droplets" (S. 2). Ref. 31 = Kosevich/Ivanov/Kovalev 1990; Ref. 32 = I. V. Bar'yakhtar,
    B. A. Ivanov, "Dynamic solitons in a uniaxial antiferromagnet", JETP 58, 190 (1983). Das ist der Einwand der
    Leitung in Worten, von Ivanov mitgezeichnet.
  - Existenzfenster [A]: omega_c < omega < omega_AFMR mit omega_AFMR = gamma sqrt(H_ex (K1 + 2 K2)/M_s),
    omega_SF = gamma sqrt(H_ex K1/M_s), omega_c = sqrt((omega_AFMR^2 + omega_SF^2)/2). Gegen D1 (i) nachgerechnet
    [ES]: -K2 cos^4 = -K2 + 2 K2 sin^2 - K2 sin^4, also b = -K2/(K1 + 2 K2) und 1 + b = (K1 + K2)/(K1 + 2 K2) =
    (omega_c/omega_AFMR)^2. **Stimmt mit D1 (i) ueberein.** (Eigener Rechenfehler waehrend der Pruefung: zuerst
    b = -2 K2/(K1 + 2 K2) notiert, das gaebe omega_SF statt omega_c; berichtigt.)
  - Innenraum [A]: "in this central area t ~ pi/2 and it can be treated as a local region of a spin-flop state, for
    which the magnon spectrum has a gapless branch. Thus, for omega < omega_AFMR these SWs are localized inside the
    soliton". Das ist fuer Frage 3 zentral: Der Ballinnenraum ist fuer Wellen unterhalb der Luecke ein Hohlraum.
  - Material [A]: Gl. 1 "is reported to describe magnetic anisotropies in hematite" (Ref. 42, Morrish 1995); Ru/Rh-
    Dotierung erhoeht K1 und K2 (Ref. 43, Hayashi u. a.); Beispiel omega_AFMR/2pi = 213 GHz, omega_c/2pi = 192 GHz;
    Haematit-Daempfung alpha = 1,1e-5 (Ref. 50, zitiert), in der Simulation 1e-3. Dimension: 2D-Film (7 nm),
    Nanokontakt; Soliton dissipativ (Gewinn = Verlust, Gl. 2), im daempfungsfreien Fall konservativ (Gl. vor 2).
  - Zweitbefund: Nietz nennt h_cr = 1 - k2/k1 "~0,8944"; die Zahl ist sqrt(1 - k2/k1) = sqrt(0,8). Die Zahl passt zu
    D1, die Formel in seinem Text nicht (Druckfehler oder Konvention, nicht geklaert).
- N3 (13:25:33) arXiv-API au:Galkina AND au:Ivanov: 8 Treffer, der Ueberblick "Dynamic solitons in antiferromagnets"
  (Low Temp. Phys. 44, 618, 2018) ist NICHT auf arXiv. Erwartung E4: KIK 1990 und Ueberblick bleiben [L?]; nur als
  Zitat in 2311.18583 belegt. Bestaetigt, eine Zeile.
