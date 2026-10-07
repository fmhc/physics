# TT-GRUND-1: Plan (Code-Agent fuer die Leitung claude-primary, Runde 44, Fast Lane)

- Start 2026-10-04 22:45:23 CEST (date). Plantext ab 23:00:53 CEST (date), vor jedem Spannenwert dieser Karte.
- Gesehen vor dem Plan: KARTE.md; TT-ISO-1 (KARTE, PLAN, ERGEBNIS, tti.py) und aus verf-V-A1R1.json nur den
  symmetrischen Bestpunkt (tb1_symm_best) und Laufzeiten; EINE-WELT-LOCH-1 PLAN und ew.py. Rauchtests r1 bis r8
  (rauch-69/) nur mit Schluesseln und Laufzeiten (Option --rauch); ihre Rohdaten (*.roh) habe ich nicht gelesen und
  auf der .69 geloescht.
- Kennzeichen: [M] eigene Mathematik bzw. Codelesung, [P] Projektdatei, [E] Rechnung, [H] Hypothese, [F] Festlegung.
- Code: code/tti.py, ew.py, nachtrag_kinetik.py, tp.py unveraendert aus TT-ISO-1 (sha256 6d6b6f7b..., fa7b6417...,
  fd0d17b9..., 419d7da6...). Neu: code/tg.py, code/kette-cpu5.sh, code/kette-cpu10.sh.

## 1. Ableitbarkeitsprobe (vor jeder Rechnung)

### 1.1 Schreibtischaussage der Leitung [M, ungeprueft in der Karte]

- Aussage: "Kein einfaches Potenzgesetz der Volumina trifft 0,090; 1,25^p = 1/0,090 verlangt p ~ 10,8."
- **Rechnung stimmt:** p = ln(1/0,0901) / ln 1,25 = 2,407 / 0,2231 = 10,79 [M].
- **Sie ist sogar zu schwach:** Ein Potenzgesetz m_t ~ V_t^p gibt J_t = (V_F/V_t)^p, also in der Ebene
  y = (log10 J_Kegel, log10 J_Sechs) = p (log10 4/5, log10 4/3) = p (-0,09691; +0,12494). Fuer J_Sechs = 1,00 braucht es
  p = 0, fuer J_Kegel = 0,090 p = 10,8. **Kein p trifft den TT-ISO-1-Punkt** [M].
- **Grenze der Aussage:** Sie setzt voraus, dass die isotrope Menge nur dieser Punkt ist. Ist sie eine Kurve, kann die
  Potenzgesetz-Gerade sie anderswo schneiden. Das ist nicht ableitbar; die Karte rechnet die Gerade beschreibend mit
  (p in [-16; 16], Schritt 0,05, innerhalb des Kastens), ohne Urteil.

### 1.2 Freie Verhaeltnisse im Code [M, Codelesung]

- Netz V hat 6 Code-Arten (finn_auf, finn_ab, kegel_T1, kegel_T2, sechs_T1, sechs_T2), also 5 freie Verhaeltnisse der
  Bewegungsgewichte J; S hat 5 Arten (achse statt sechs), 4 Verhaeltnisse.
- Symmetrische Ebene (Fd-3m): finn_auf = finn_ab = 1, kegel_T1 = kegel_T2 = J_Kegel, sechs_T1 = sechs_T2 = J_Sechs
  (tti.sym_J). **Zwei freie Verhaeltnisse**, beide auf der Massenseite.
- Steifigkeitsseite: B (lineare Regge-Wirkung) hat keinen freien Parameter. Das Regelgewicht g (3 Verhaeltnisse in V)
  bleibt 1; TT-ISO-1 fand jedes g != 1 um >= 0,05 Dekaden ungueltig [P].
- Weil B und die Zwangsflaeche S nicht von J abhaengen, sind der weiche 2D-Raum von B_red und seine Eigenwerte
  lam(n) ~ k^2 von J unabhaengig. Langwellig gilt omega^2 = Eig(Ms^-1 Lam) mit Ms = U2^+ A_red^-1 U2 [M]. J wirkt nur
  ueber Ms (Masse).
- **Welcher Teil traegt die Spanne:** TT-ISO-1 fand die affine TT-Steifigkeit isotrop (1/4, Spanne <= 2,5e-8) [P]. Das
  ist die unrelaxierte Steifigkeit. Neu und beschreibend (Kontrolle c unten): die relaxierte Steifigkeit je metrischer
  Amplitude kappa = Eig(G^-1 Lam) und die Masse je metrischer Amplitude mu = Eig(G^-1 Ms), G = Gram-Matrix der
  TT-Anteile H_TT der weichen Eigenvektoren (ew.tensor_fit), an 13 Richtungen bei |k| = 1e-3, fuer N1 und den
  TT-ISO-1-Punkt. Erwartung [M, H]: kappa isotrop (Spanne < 1e-4), mu traegt die 6,34 % bei N1.

### 1.3 Was schon bekannt ist und was nicht

- N1: 6,34 % (TT-ISO-1, max/min - 1 an 13 Richtungen x 2 |k|) [P].
- N2 = Variante A2 des EINE-WELT-LOCH-1-Nachtrags = TT-ISO-1 "A2R1, J = 1": 5,92 % [P]. **TG2 ist fuer N2 vorab
  bekannt (nicht unter 0,1 %).** Fuer N3 bis N6 gibt es keine Rechnung [P, Suche in TT-ISO-1 und EINE-WELT-LOCH-1].
- Form der Menge: TT-ISO-1 fand symmetrisch zwei getrennte Minima derselben Familie: (0,090; 0,998) mit 1,1e-5 (A1R1)
  und (5,90; 0,916) in A1-Einheiten mit 3,3e-4 (A2R1-Lauf) [P]. Beide liegen nahe J_Sechs ~ 1. Das deutet auf ein
  ausgedehntes Tal, entscheidet aber nichts (3,3e-4 > 1e-4; Nelder-Mead nicht konvergiert).
- Das TT-ISO-1-Gitter (9^5 Punkte) enthaelt die symmetrische Ebene in 9 x 9 Halbdekaden-Punkten [P]. Ich habe sie nicht
  herausgezogen (Indexrechnung). Die Karte reproduziert sie als Kontrolle (d).
- TG0 nach Kartenwortlaut nennt den gerundeten Punkt (0,090; 1,00). Er liegt 4,8e-4 bzw. 1,0e-3 Dekaden neben dem
  TT-ISO-1-Bestpunkt (log10 0,090 = -1,04576 gegen -1,04533; 0 gegen -0,00101). Ob die Spanne dort <= 2e-5 bleibt, haengt
  an der Steigung des Tals und ist nicht ableitbar. Nach Plan zaehlt der exakte Punkt (1.4).

### 1.4 Regeln N1 bis N6, aus der Geometrie (vorab, Koordinaten ew.geometrie, Einheiten 1/8) [M]

- Finn (finn_auf): Ecken R8 = (1,1,1), (1,-1,-1), (-1,1,-1), (-1,-1,1); regelmaessig, Kante^2 = 8; Volumen 8/3 (in
  1/512) = 4/768.
- Kegel (kegel_T1, a = 0): C1 = (-2,-2,-2) und (1,-1,-1), (-1,1,-1), (-1,-1,1), also Kegel ueber einer Dreiecksflaeche
  von Finns Auf-Tetraeder. Kanten^2: 3 x 8 (Grunddreieck), 3 x 11 (C zu P). Hoehe 5/sqrt3, Volumen 10/3 = 5/768.
- Sechseck-Tetraeder (sechs_T1, a = 0): C1, H = (-3,-3,-3) und zwei benachbarte Sechseckecken, z. B. (-1,-3,-5),
  (-1,-5,-3). Das Sechseck liegt in x+y+z = -9, Mitte H, Umkreis 2 sqrt2; C-H steht senkrecht, Laenge sqrt3.
  Kanten^2: C-H 3; H-v, H-v', v-v' je 8; C-v, C-v' je 11. Volumen (1/3)(2 sqrt3)(sqrt3) = 2 = 3/768.
- Achsen-Tetraeder (S, beschreibend): C1, C2' = (-4,-4,-4), v, v'. Kanten^2: C1-C2' 12; vier mal 11; v-v' 8.
  Volumen 4 = 6/768.
- **Netzecken** (Untergitter s < 4 in ew, Pyrochlor-Plaetze R + r_a; geprueft: (-1,-3,-5) = (0,-4,-4) + r_2):
  Finn 4, Kegel 3, Sechseck-Tetraeder 2, Achsen-Tetraeder 2.
- **Traegheitsmoment** um den Schwerpunkt bei gleicher Dichte: Spur des Traegheitstensors = 2 int |x - x_s|^2 dV; als
  Skalar nehme ich das polare Moment Ipol = int |x - x_s|^2 dV = (V/20) sum_i |w_i|^2 = (V/80) sum_Kanten l^2
  (w_i Ecken relativ zum Schwerpunkt). Jede Spur-Groesse (Ipol, tr I, tr I/3) gibt dasselbe Verhaeltnis; der
  Traegheitstensor der Kegel und Sechseck-Tetraeder ist nicht kugelfoermig, die Spur ist die festgelegte Wahl [F].
  - Finn: (8/3)(48)/80 = 8/5. Kegel: (10/3)(57)/80 = 19/8. Sechseck: 2 x 49/80 = 49/40. Achse: 4 x 64/80 = 16/5.
- **J = m_Finn / m_t:**

| Regel | Masse | J_Kegel | J_Sechs (V) | J_Achse (S, beschreibend) |
|---|---|---|---|---|
| N1 | alle gleich | 1 | 1 | 1 |
| N2 | ~ Volumen | 4/5 = 0,8 | 4/3 = 1,33333 | 4/6 = 0,66667 |
| N3 | ~ 1/Volumen | 5/4 = 1,25 | 3/4 = 0,75 | 6/4 = 1,5 |
| N4 | ~ Volumen^2 | 16/25 = 0,64 | 16/9 = 1,77778 | 16/36 = 0,44444 |
| N5 | ~ Netzecken n | 4/3 = 1,33333 | 4/2 = 2 | 4/2 = 2 |
| N6 | ~ Ipol | (8/5)/(19/8) = 64/95 = 0,673684 | (8/5)/(49/40) = 64/49 = 1,306122 | (8/5)/(16/5) = 1/2 |

- Kontrolle im Lauf (a): tg.py rechnet Volumen, Netzecken und Ipol aus den Code-Koordinaten je Zelle und vergleicht die
  daraus folgenden J mit dieser Tabelle (Abweichung erwartet <= 1e-12; T1 = T2 je Art).

## 2. Messgroesse und Verfahren [F]

- Paarung A1R1, g = 1, Zwangsflaeche und Z-Verfahren wie TT-ISO-1 (tti.prep, tti.auswerten, unveraendert).
- **Spanne(y)** = max/min - 1 ueber 52 Werte omega^2/k^2 (13 Richtungen von tti.richtungen13 x 2 Zweige x |k| = 1e-3,
  2e-3), y = (log10 J_Kegel, log10 J_Sechs), Finn = 1.
- **Plan-gueltig** wie TT-ISO-1: an allen 26 k-Punkten Klassifikation eindeutig (zwei masselose positiv, Luecke < 1e-2)
  und keine negative Mode (neg_26 = 0). **Wortlaut-gueltig:** jeder endliche Wert.
- **Karte V:** Raster 161 x 161 auf [-2; 2]^2, Schritt 0,025 Dekaden (enthaelt die Halbdekaden-Punkte). Ausgegeben
  werden Spanne (plan und wort), w_min, Zahl der Rasterpunkte unter 1e-2, 1e-3, 1e-4, 1e-5, 1e-6, Zahl der 3 x 3-Bloecke
  ganz unter 1e-4, Zusammenhangskomponenten (4er-Nachbarschaft, beschreibend), Minimum.
- **Karte S (beschreibend):** 81 x 81, Schritt 0,05; y2 = log10 J_Achse.
- **Lokale Verfeinerung entlang der Menge (Talboden-Profile, V):**
  - Profil S: fuer 81 Werte yS in [-2; 2] (Schritt 0,05) die kleinste Spanne ueber yK. Profil K: ebenso fuer 81 Werte yK,
    Minimum ueber yS.
  - Je Profilwert: Abtastung der Querachse mit 161 Punkten (Schritt 0,025); aus den bis zu 3 besten lokalen Minima der
    plan-gueltigen Abtastung je ein Goldener Schnitt im Nachbarintervall (Breite 0,05) bis 1e-7 Dekaden; der kleinere
    Wert von Verfeinerung und Rasterpunkt zaehlt.
  - Wortlaut: Liegt ein ungueltiger Punkt der Abtastung tiefer als der beste gueltige, wird er ebenso verfeinert
    (Zielgroesse ohne Gueltigkeit); sonst gilt der Plan-Wert.
  - Zeitschranke im Lauf: kein neuer Profilwert nach Prozessstart + 540 s (Feld abbruch).
- **Bester Punkt:** kleinste plan-gueltige Spanne unter allen verfeinerten Profilminima und dem exakten TT-ISO-1-Punkt,
  danach Nelder-Mead (tti.nelder_mead, Schritt 0,01 dann 0,001, je maxit 150); der bessere von beiden zaehlt.
- **Stabilitaet:** tti.stabil an den 511 k des Gitters L = 8 (ohne k = 0): Zahl der k mit Re omega^2 < -1e-9 s bzw.
  |Im| > 1e-9 s. **Stabil ja** = plan-gueltig (keine negative Mode an den 26 kleinen k) und 0 negative und 0 komplexe
  k an den 511 k. Fuer jede Regel N1 bis N6 (V und S) und fuer den besten Punkt; beschreibend zusaetzlich fuer bis zu 5
  gleichmaessig verteilte Profilminima unter 1e-4 (nach yK sortiert).
- Beschreibend: Spanne an den 23 Hauptlauf-Richtungen (ew.richtungen) fuer Regeln und besten Punkt; Abstand jeder Regel
  (in Dekaden) zum naechsten Profilminimum unter 1e-4; Potenzgesetz-Gerade (1.1).

### 2.1 Kurve, Punkt, Gebiet [F]

- Grundlage: die zwei Profile (je 81 Werte, Schritt 0,05) und die Karte V. "Lauf" = zusammenhaengende Folge von
  Profilwerten < 1e-4; Ausdehnung = (Zahl der Werte - 1) x 0,05 Dekaden. R_max = groesste Ausdehnung ueber beide Profile.
- **Gebiet:** Die Karte V hat mindestens einen 3 x 3-Block von Rasterpunkten (Seite 0,05 Dekaden) ganz unter 1e-4.
- **Kurve:** kein Gebiet und R_max >= 0,25 Dekaden (mindestens 6 aufeinanderfolgende Profilwerte unter 1e-4).
- **Punkt:** kein Gebiet, die Menge ist nicht leer (ein Profilwert, ein Rasterpunkt oder der exakte TT-ISO-1-Punkt unter
  1e-4), R_max <= 0,05 Dekaden (hoechstens 2 aufeinanderfolgende Profilwerte) und beide Profile vollstaendig.
- **Unklar:** alles andere (0,05 < R_max < 0,25, leere Menge, unvollstaendiges Profil ohne Kurve).
- Beschreibend: Boden (kleinster und groesster Profilwert) je Lauf; Laeufe >= 0,25 Dekaden mit Boden durchweg < 1e-6
  ("Kurve exakter Isotropie"); Zahl der Laeufe je Profil (mehrere Aeste oder Punkte).

## 3. Kontrollen (Lauf kontrolle, vor allem anderen auf cpu5)

- a) Geometrie: Volumen x 768, Netzecken, Ipol x 8^5 je Art aus den Code-Koordinaten; J der Regeln gegen 1.4.
- b) N1 (V) und der TT-ISO-1-Punkt: exakt y = (-1,0453267293; -0,0010098244) aus verf-V-A1R1.json und gerundet
  (log10 0,090; 0).
- c) Steifigkeit gegen Masse (1.2) bei N1 und am exakten TT-ISO-1-Punkt (V), bei N1 auch in S: Spanne von kappa, mu,
  omega^2 (weich) und omega^2 (Z-Verfahren); Abweichung weich gegen Z.
- d) Im Kartenlauf: 81 symmetrische Punkte des TT-ISO-1-Gitters (ref/gitter-V-A1R1.json, sha256 d00b8c9d...) gegen die
  Karte (alt auf 7 Stellen gerundet; erwartet <= 1e-7 absolut, gleiche Gueltigkeit).

## 4. Vorhersagen und Urteilsregeln (Karte unveraendert; Regeln hier vor jeder Rechnung)

| Nr | Karte (Wahrsch.) | nach Plan | nach Kartenwortlaut |
|---|---|---|---|
| TG0 | Kontrolle: N1 gibt 6,34 % und der TT-ISO-1-Punkt (0,090; 1,00) <= 2e-5, je auf 1e-3 relativ bzw. absolut (90 %) | **eingetroffen**, wenn \|Spanne(N1) - 0,0634\| <= 1e-3 x 0,0634 **und** am exakten TT-ISO-1-Punkt Spanne <= 2e-5 und plan-gueltig. Sonst verfehlt. | wie Plan, aber am gerundeten Punkt (0,090; 1,00): Spanne <= 2e-5 (ohne Gueltigkeitsbedingung). |
| TG1 | [H] Die Menge mit Spanne < 1e-4 ist eine Kurve, kein einzelner Punkt und kein Gebiet (65 %) | nach 2.1 mit plan-gueltigen Werten: **eingetroffen** bei "Kurve"; **verfehlt** bei "Gebiet" oder "Punkt"; **nicht entscheidbar** bei "unklar". | wie Plan mit Wortlaut-Werten (Gueltigkeit ignoriert; Karte "wort", Profile mit Wortlaut-Verfeinerung). |
| TG2 | [H] Keine der Regeln N2 bis N6 liegt unter 0,1 % Spanne (75 %) | **eingetroffen**, wenn keine Regel N2 bis N6 (V) Spanne < 1e-3 hat und zugleich plan-gueltig ist; **verfehlt**, wenn mindestens eine. | eingetroffen, wenn keine Regel N2 bis N6 (V) Spanne < 1e-3 hat, gleich ob gueltig. |

- Mechanisch in tg.py urteil (eingefroren). S, Potenzgesetz-Gerade, Steifigkeit/Masse, Stabilitaet entlang der Menge
  und Abstaende sind beschreibend und gehen in kein Urteil ein. Stabilitaet steht als eigene Spalte neben TG2.
- Agenten-Erwartung (vorab, kein Urteil) [H]: Die Gegenrechnung in TT-ISO-1 (zwei Bedingungen fuer isotrope Masse) und
  zwei freie Verhaeltnisse sprechen fuer isolierte Punkte. TG1 Kurve 35 %, Punkt 50 %, unklar 15 %. TG2 eingetroffen
  85 %.

## 5. Laeufe, Laufzeit, Abbruch

- **Rauchtests (vor dem Einfrieren, nur Schluessel und Laufzeiten, rauch-69/):** r1 kontrolle 6,6 s; r2 Karte V 9 x 9
  0,46 s fuer 81 Punkte (5,7 ms je Punkt), 5,0 s gesamt; r3/r4 Profile mit 3 Werten: 1,3 bis 3,2 s je Profilwert; r5
  regeln 23 s; r6 best 15 s (3 Stabilitaetspruefungen); r7 urteil 0,03 s; r8 bild 1,5 s (Bild aus Konstanten). Alle rc 0.
- **Schaetzung:** kontrolle ~7 s, regeln ~25 s, Karte V 161^2 = 25 921 Punkte ~150 s + 5 s, Karte S ~20 s (cpu5,
  zusammen ~4 min). Profile je 81 x ~2,3 s ~190 s, best ~30 bis 60 s, urteil und bild ~5 s (cpu10, ~7,5 min).
- **Spuren:** cpu5: kontrolle, regeln, Karte V, Karte S (code/kette-cpu5.sh). cpu10: Profil S, Profil K, best, dann
  (wartet auf kontrolle, regeln, Karte V) urteil, bild (code/kette-cpu10.sh). Jeder Lauf ueber kleintest.sh
  (<= 600 s, 1 Thread). Einmalige Laufliste, kein Dienst.
- **Abbruch:** kein neuer Lauf ab 2026-10-04 23:45:00 CEST (21:45:00 UTC; prueft die Liste vor jedem Lauf). Faellt ein
  Lauf an der 600-s-Grenze, wird er nicht wiederholt; betroffene Urteile sind dann "nicht entscheidbar" (TG1 ohne
  Profil oder Karte, TG2 ohne regeln, TG0 ohne kontrolle).
- **Auswertung:** mechanisch aus urteil.json und den JSON-Dateien des eingefrorenen tg.py (jq nur zum Lesen). Alles nach
  Sicht steht als gekennzeichneter Nachtrag in neuen Dateien.
