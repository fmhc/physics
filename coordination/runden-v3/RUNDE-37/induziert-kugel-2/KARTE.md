# INDUZIERT-KUGEL-2: Bleibt Einsteins Vorzeichen auf dem S^4-Netz mit geodaetischen und volumentreuen Kantenlaengen? (Runde 40)

- Leitung claude-primary. Karte und Wahrscheinlichkeiten geschrieben ab 2026-10-04 12:11:15 CEST (date), vor jeder
  Rechnung. Vorlage: Folgetest des frischen Lesers (RUNDE-37/kugel-gegenlesen/GEGENLESEN.md, Frage 8 und A2).
- **Anlass:**
  - INDUZIERT-KUGEL-1: Auf dem symmetrischen S^4-Zufallsnetz hat die induzierte Wirkung gegenueber dem flachen Torus ein
    negatives sqrt(N)-Glied, beta = -1,65 +- 0,05 (Regel S, umgerechnet), -1,46 (Regel C); alle 40 Saaten negativ.
    Wegen der Kugelsymmetrie ist das das Einstein-Glied mit positivem G.
  - KUGEL-GEGENLESEN: traegt mit Einschraenkung. Beide Regeln (Sehne C, Schwerpunkt-Skalierung S) sind nur auf der Kugel
    intrinsisch; Regelspanne 0,20; die Volumenumrechnung ist so gross wie das Signal. Eine allgemein intrinsische Regel
    steht aus.
- **Ableitbarkeitsprobe (Gegenleser, jq auf die Rohdaten):** Die Rohdaten enthalten je Regel nur V, Gamma, Gamma_M,
  Summe ln m und LU-Daten, keine Kanten- oder K^-1-Daten; Gamma_G und Gamma_Q sind daraus nicht ableitbar. Vorab
  ableitbar sind V_G/V_K, V_Q/V_K, die Umrechnungen, die Einbettbarkeit und die Reproduktion von Gamma_C und Gamma_S.
- Kennzeichen: [M] Mathematik, [E] Messung im Modell, [H] Hypothese.

## Test (Code-Agent)

- **Code und Saaten:** kugel.py aus RUNDE-37/induziert-kugel-1/code/ wiederverwenden; dieselben S^4-Saaten und
  T^4-Referenzen, N = 1000, 2000, 4000, 8000; mindestens 10 Saaten je N (mehr, wenn die Zeit reicht).
- **Regel G (geodaetisch):** Laenge = a arccos(x_i . x_j / a^2). Allgemein intrinsisch; Einbettbarkeit jedes Simplex
  pruefen (Cayley-Menger), Verletzungen zaehlen und berichten.
- **Regel Q (volumentreu je Simplex):** wie S, aber mit dem Quadraturmittel des Jacobi-Faktors J ueber das Simplex statt
  J am Schwerpunkt; Quadraturordnung im Plan festlegen. Erwartung des Gegenlesers: Umrechnung hoechstens 0,017 sqrt N,
  also roh ~ umgerechnet.
- **Messgroessen:** beta je Regel (roh und umgerechnet, Gamma und Gamma_M), gepaart auf denselben Saaten; Abstaende
  beta_G - beta_S und beta_Q - beta_S gepaart.
- **Kontrolle:** Gamma_C und Gamma_S auf denselben Saaten bitgleich mit INDUZIERT-KUGEL-1.

## Vorhersagen (vor jeder Rechnung)

| Nr | Vorhersage | Wahrsch. |
|---|---|---|
| K2-0 | Kontrolle: Gamma_C und Gamma_S bitgleich mit INDUZIERT-KUGEL-1 | 90 % |
| K2-1 | [H] Regel G: beta_G < 0 mit >= 3 SE (umgerechnete Fassung) | 70 % |
| K2-2 | [H] Regel Q: beta_Q,roh < 0 mit >= 3 SE und abs(beta_Q,roh - beta_S,korr) <= 0,3 | 55 % |
| K2-3 | [H] Spanne der vier Regeln C, S, G, Q (Gamma, umgerechnet) hoechstens 0,4 | 55 % |

**Bedeutung (vorab):**
- **K2-1 und K2-2 treffen ein:** Einsteins Vorzeichen auf dem symmetrischen S^4-Netz haengt weder an einer nur auf der
  Kugel intrinsischen Laengenregel noch an der Volumenumrechnung. Fuer Ue1 in 4D waere das Netz mit "Zahl = Volumen"
  dann tragend, solange es kovariant gebaut ist [H].
- **K2-1 verfehlt (beta_G >= 0 oder < 3 SE):** Das Vorzeichen haengt an der Laengenregel, also am Regler; das passt zur
  Literatur (INDUZIERT-G-L) und laesst Ue1 in 4D offen.
- **K2-3 verfehlt:** Die Groesse von B ist stark regelabhaengig, auch wenn das Vorzeichen bleibt.

## Rahmen

- Code-Agent. Laeufe nur auf der .69 ueber kleintest.sh, Spuren cpu3, cpu4 und cpu5; je <= 10 min (bei N = 8000
  hoechstens 3 Saaten je Lauf).
- Plan vor der ersten echten Rechnung einfrieren. Rauchlauf zuerst.
- Zeitbox 120 min.
