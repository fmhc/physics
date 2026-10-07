# QB-BS-2D: Bleibt ein Q-Ball an einem Baby-Skyrmion haengen? Erster Rechenschritt zum Spin-1/2-Weg (Runde 37)

- Leitung claude-primary. Karte und Vorhersagen geschrieben ab 2026-10-04 04:50:06 CEST (date), vor jeder Rechnung.
- **Anlass:**
  - Finn: "Haben wir ein Teilchenmodell?" und "Ideate zu 1/2". IDEEN-EVOLUTION/GEN-04-SPIN-HALB.md, H6.
  - Literaturkarte SPIN-HOPF-L (RUNDE-37/spin-hopf-l/DOSSIER.md, Abschnitt 7, Vorschlag QB-BS-2D): Codex' Modell B.5
    (C x S^2, coordination/literatur-20260923/SPIN-KONSTRUKTION-codex.md) in 2+1.
    - Der Rand haelt den Knoten (Baby-Skyrmion, B = 1) fest; in 3D wickelte er sich auf dem Gitter ab (HOPF-1).
  - Projektvorarbeit: RUNDE-03/tests2d-r3/KNOTEN-PAPIER.md, CX-1 (kappa = 1/4), qball-hopf-3d, astras Pruefschranken.
  - Codex informiert (Peerbus 78c45e2a, Plan; CX-1 unberuehrt).
- Kennzeichen: [M] Mathematik, [L] Literatur, [S] an der Quelle gelesen (laut Dossier), [ES] eigener Schluss, [H] Hypothese.
- **Ehrlich vorab:** Der Spin 1/2 selbst kaeme hier aus dem bekannten Finkelstein-Rubinstein-Mechanismus (eingesetzt).
  Gefragt ist nur, ob die Q-Ball-Ladung am Knoten gebunden bleibt. Das ist offen; ein Vorbild fand die Literaturkarte
  nicht.

## Modell (aus dem Dossier, Abschnitt 7; im Plan gegen Codex' B.5 pruefen)

- L = |d phi|^2 + (v^2/4) dn.dn - U(|phi|^2 + |b|^2) + G Re[(phi^* b)^2] - mu^2 v^2 (1 - n3) - (kappa/4) H_mn H^mn
  - b = (v/2)(n1 + i n2), U(s) = s - s^2 + s^3/2.
- Parameter vorab gebunden, keine Nachwahl: v = mu = 1; kappa in {1; 1/4}; G = gJ in {0; 1}.
- **Igel-Ansatz:**
  - n = (sin f cos(theta + Omega t), sin f sin(theta + Omega t), cos f).
  - G = 0: phi = h(r) e^(i omega t) (l = 0).
  - G = 1: phi = h(r) e^(i (theta + Omega t)) (l = 1, h(0) = 0).
- Festladungsreduktion E_q = V + q^2/(2 Lambda) nach astra, sinngemaess fuer 2D [ES].

## Test (Code-Agent; nur die radialen Stufen S0 bis S2 aus dem Dossier)

- **S0 Eichproben:**
  - statisches B = 1-Profil (Energie ueber der topologischen Schranke, Konvergenz bei Verdopplung von N_r)
  - 2D-Q-Ball-Profile bei drei omega in (1/sqrt 2, 1)
- **S1 Referenzaeste:**
  - E_H(q): isorotierendes B = 1 mit phi = 0, bis Omega^2 = 0,95 v^2/(2 kappa) oder bis der Loeser versagt; je Profil
    chi_max
  - E_Q(q) fuer l = 0 und l = 1
  - E_sep(q) = min_u [E_H(u) + E_Q(q - u)] einschliesslich der Raender
- **S2 Gebundene Aeste:**
  - G = 0: ruhende Textur plus phi, Scan in q
  - G = 1: gekoppelter l = 1-Ast
  - Je q: Omega(q), Bindung D(q) = (E_sep - E_mix)/E_sep, chi_max(q), J
- S3 (volle 2D-Relaxation) und S4 (2D-Zeitlauf) gehoeren nicht zu dieser Karte; sie sind Folgekarten.

## Vorhersagen (vor jeder Rechnung)

| Nr | Vorhersage | Wahrsch. |
|---|---|---|
| QB0 | S0: B = 1-Energie ueber der topologischen Schranke, Profil konvergent (relative Energieaenderung bei Verdopplung von N_r <= 1e-6); 2D-Q-Ball-Energien bei Verdopplung <= 1e-6 | 85 % |
| QB1 | [H] G = 1, kappa = 1: Es gibt ein q mit Bindung D(q) > 0, auf mindestens drei aufeinanderfolgenden Rasterpunkten | 50 % |
| QB2 | [H] Auf diesem gebundenen Ast faellt Omega^2 unter 1/2 (unter die Sicherheitsgrenze des freien Knotens) | 35 % |
| QB3 | [H] G = 1, kappa = 1/4: ebenfalls D(q) > 0 auf mindestens drei aufeinanderfolgenden Rasterpunkten | 45 % |
| QB4 | G = 0 (ohne Paarkopplung): keine Bindung, D(q) <= 0 fuer alle q (die Felder sehen sich nur ueber U) | 55 % |

**Bedeutung (vorab):**
- **QB1 und QB3 treffen ein:** Im 2D-Gegenstueck bleibt die Q-Ball-Ladung am Knoten. Damit waere der Weg Spin 1/2 =
  Knoten + gebundene Ladung (C x S^2) rechnerisch offen. Der Spin selbst bleibt eingesetzt.
  - Folge: S3/S4 (volle 2D-Relaxation und Zeitlauf), dann die Frage in 3D.
- **QB4 verfehlt (Bindung schon ohne Paarkopplung):** Die Felder binden ueber U allein; das waere einfacher als gedacht.
- **QB1 verfehlt:** Die Ladung loest sich vom Knoten. Der Spin-1/2-Weg C x S^2 braucht dann eine andere Kopplung.

## Rahmen

- Code-Agent. Laeufe nur auf der .69 ueber kleintest.sh, Spuren cpu und cpu6; je <= 10 min.
- Plan vor der ersten echten Rechnung einfrieren.
- Zeitbox 120 min.
- Codex' Dateien und CX-1 nicht anfassen; nur lesen.
