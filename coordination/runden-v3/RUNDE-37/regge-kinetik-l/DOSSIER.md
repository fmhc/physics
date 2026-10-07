# REGGE-KINETIK-L: Dossier (feldforscher fuer die Leitung claude-primary, Runde 48, Literatur zu HODGE-MASSE-1)

- Karte: KARTE.md (RK1 bis RK5 und Bedeutung unveraendert). Arbeitsfeld: ARBEITSFELD.md. Abrufprotokoll: ABRUFE.md.
  Abgerufene Texte: quellen/ (PDF und pdftotext-Fassung).
- **Kennzeichen:** [E] Messung oder Rechnung (hier keine); [M] Mathematik (Schreibtisch, mit Herleitung); [S] an der
  Quelle gelesen (S. = PDF-Seite, per Seitenextraktion geprueft; [S Abstract] = nur Abstract); [L] Lehrbuch/Gedaechtnis;
  [H] Hypothese; [P] Projektbefund mit Fundstelle; [ES] eigener Schluss.
- Keine Messdaten. Alles Literatur oder Schreibtisch. Regime: **H** = stetige Zeit, 3+1/Hamilton (Lund/Regge,
  Piran/Williams, Friedman/Jack, Hartle/Miller/Williams, unser Netz); **K** = diskrete Zeit, 4D bzw. Pfadintegral,
  oder statischer Operator (Dittrich/Hoehn, Feinberg/Friedberg/Lee/Ren, Christiansen).

## 1. Zeiten und Abrufzahl

- Start 2026-10-05 09:35:24 CEST (date). Karte und Vorarbeiten gelesen bis 09:41:19. Netzabrufe 09:42:02 bis
  09:57:48. Projektcode ew.py gelesen (nicht ausgefuehrt) zwischen 09:54:24 und 09:56:15. Text ab 10:03:28 CEST
  (date). Abgabe: Zeile am Dateiende (date).
- **15 von 15 Netzabrufen:** 9 API-Abfragen (arXiv F1a leer, F1, F4 Fehlsuche, F5, F8, F11, F13; OpenAlex F3;
  INSPIRE F10), 4 PDF-Volltexte (F2 Hartle/Miller/Williams 1997, F6 Dittrich/Hoehn 2013, F7 Hoehn 2015,
  F14 Christiansen 2011), 2 Websuchen (F9, F12; nur Trefferlisten, nie als Quelle verwendet).

## 2. Ergebnis zuerst

1. **Die Standardform ist volumengewichtet, aber sie sitzt auf der Geschwindigkeitsseite.** Die Lund-Regge-Supermetrik
   ist G_mn dt^m dt^n = Summe_tau V(tau) {dh_ab dh^ab - (dh^a_a)^2} = -Summe_tau (1/V) d^2 V^2/dt^m dt^n
   (Quadrat-Kantenlaengen t, Lapse N = 1; Hartle/Miller/Williams 1997, Gl. 3.5 und 3.13 [S]). Friedman/Jack 1986
   gewinnen sie aus der Einstein-Wirkung [S Abstract]. Unser Code legt je Tetraeder die inverse DeWitt-Form auf die
   **Impulse**. Je Tetraeder ist das (mit Gewicht 1/V) genau das Inverse des Lund-Regge-Elements; ueber geteilte
   Kanten summiert aber nicht: Summe der Inversen != Inverse der Summe [M]. **Folge: HM0 ist nur fuer die Lund-Regge-
   Form eine Identitaet, nicht fuer A2 auf der Impulsseite** [M].
2. **R1 ist schon die richtige Reduktion** [M, vorab ableitbar; am Code gelesen]. R1 ist die Dirac-Reduktion des
   Paars (c^H q, c^H p) plus Quotient nach den Eckverschiebungen M. Seine Frequenzen haengen nicht von der Eichflaeche
   ab, solange B M = 0 und c^H M = 0 gelten (laut IMPULS-NETZ-1 bis 1e-15 [P]). Der HM1-Arm "R1 weicht um mehr als
   1e-4 ab" ist daher nicht zu erwarten. Der "Projektionsanteil" aus TT-GLAS-2 ist dann die echte reduzierte
   Bewegungsenergie der gewaehlten Form, kein Artefakt der Reduktion [ES].
3. **Zwei Regime bei der Isotropie.** Im Regime K naehern sich Regge-Gitter dem Kontinuum, und zwar auf "any lattice,
   regular or irregular", mit Korrekturen in l^2 (Feinberg/Friedberg/Lee/Ren 1984 [S Abstract]). Fuer den statischen
   linearisierten 3D-Regge-Operator konvergieren die Eigenpaare auf quasi-uniformen Netzen (Christiansen 2011, Satz 4.7
   [S]). Unser Hamilton-Netz mit gesetzter Bewegungsenergie zeigt dagegen langwellig O(1)-Anisotropie [P].
   Moderator: die Bauart der Bewegungsenergie [ES]. Unterscheidungspunkt: TT-Spanne gegen kl mit Lund-Regge-Masse.
4. **Umklappen:** In diskreter Zeit erhalten 1-4 und 2-3 die auf die Nachbedingungen eingeschraenkte Symplektik; 3-2
   und 4-1 senken ihren Rang (Dittrich/Hoehn 2013, Satz 4.1 [S]). Die Zustandsabbildung dort ist eine
   Impulsaktualisierung ueber die Hamilton-Hauptfunktion; die neue Kante ist a priori frei (Hoehn 2015 [S]). Energie
   kommt in diesem Rahmen nicht vor. Fuer stetige Zeit mit Umklappen fand ich keine Arbeit, auch nicht in den letzten
   24 Monaten. Symplektik und Energieerhalt sind getrennte Forderungen [ES].
5. **Bedingungen in stetiger Zeit:** Friedman/Jack: Die Bedingungen sind "not conserved if the lapse and shift are
   chosen a priori". Erhalten bleiben sie nur, wenn man Lapse und Shift je Drei-Simplex aus ihnen loest [S Abstract].
   Unsere zweite Klasse ist damit eine Eigenschaft des Regimes H, nicht nur des Codes [ES]. **Urteile:** RK1 teilweise,
   RK2 eingetroffen, RK3 teilweise, RK4 teilweise, RK5 teilweise.

## 3. Erwartungsverstoesse (das eigentliche Ergebnis; wichtigste zuerst)

1. **Seite der Supermetrik (F2 und Code).**
   - Erwartet (Karte RK1, HM0): "volumengewichtete DeWitt-Form" ist eine eindeutige Groesse.
   - Gelesen: Lund-Regge ist eine Metrik auf Geschwindigkeiten mit Spurkoeffizient 1 (HMW Gl. 3.5). Unser A wirkt auf
     Impulse (x' = A p / kappa_g, IMPULS-NETZ-1 4.2 [P]); dort ist der Koeffizient 1/2, und die Summe laeuft ueber
     Tetraeder.
   - Korrigierte Erwartung: "volumengewichtet" ist ohne Angabe der Seite nicht eindeutig. HM0 haelt exakt nur auf der
     Geschwindigkeitsseite (Summe V_tau = V_tot).
2. **Kontinuumsnaehe auf unregelmaessigen Gittern ist Literatur (F10, F11, F14).**
   - Erwartet (RK5, 35 %; eigene Erwartung "keine Studie").
   - Gelesen: Feinberg/Friedberg/Lee/Ren 1984 behaupten den Kontinuumslimes auf jedem Gitter, mit Korrekturen in l^2
     und mit dem Graviton-Propagator als Beispiel [S Abstract]. Christiansen 2011 beweist die Eigenpaarkonvergenz des
     linearisierten 3D-Regge auf quasi-uniformen Netzen [S].
   - Korrigierte Erwartung: Die O(1)-Anisotropie unseres Netzes ist regime-spezifisch (Regime H mit gesetzter
     Bewegungsenergie), keine Eigenschaft von Regge-Gittern an sich [ES].
3. **Eine ausdrueckliche horizontale Zerlegung existiert (F14).**
   - Christiansen 2011 (S. 15, Gl. 89 bis 91): W = Kern der Regge-Form, V = sein orthogonales Komplement im
     L2-Skalarprodukt, X = V (+) W. Das Spektrum lebt auf V; eine Eichflaeche kommt nicht vor.
   - Das spricht fuer RK4. Einschraenkungen: statisch, L2-Masse (nicht DeWitt), kein Hamilton-Bild.
4. **Lund-Regge ist selbst nicht horizontal (F2).**
   - Erwartet: Die Lund-Regge-Metrik ist die horizontale Form.
   - Gelesen: Sie ist nur gegen Umeichungen im Inneren der Tetraeder extremal, ausdruecklich "not exactly 'horizontal'
     in the sense of the continuum" (HMW S. 10). Grund sind die Eckverschiebungen. Horizontale Begriffe fuer
     Eckverschiebungen nennen HMW eine Aufgabe fuer spaeter (S. 22 f.).
5. **Negative Richtungen: nicht eine je Ecke (F2).**
   - T^3 mit 3x3x3 Ecken (27 Ecken, 189 Kanten): 13 negative und 176 positive Eigenwerte; keine der 13 ist ein
     Diffeomorphismus (S. 21). Rand des 4-Simplex: genau eine negative (S. 14). 600-Zelle (vorlaeufig): 92 negative,
     628 positive (S. 22).
   - Schranke [ES aus Gl. 3.22/3.23]: hoechstens n3 (Tetraederzahl) negative Richtungen. Sie liegen im Spann der
     Volumengradienten der Tetraeder.
6. **Lapse und Shift je Drei-Simplex, nicht je Ecke (F3).**
   - Bei Friedman/Jack werden die Bedingungen erhalten, indem Lapse und Shift bestimmt werden. Die Multiplikatoren
     sind also festgelegt; der Sache nach ist das zweite Klasse [ES].
7. **Symplektik nur eingeschraenkt (F6).**
   - Die globale Entwicklung ist nur prae-symplektisch (DH 2013, Satz 3.1, S. 13).
   - Typ II (3-2, 4-1) senkt den Rang der Symplektik (S. 25, S. 41).
8. **R1 ist bereits korrekt (Schreibtisch).**
   - Erwartet (Kette der HODGE-MASSE-1-Karte): R1 koennte nicht horizontal sein.
   - Gezeigt [M]: R1 ist Dirac-Reduktion plus Quotient (Abschnitt 4.3).

**Bestaetigt, je eine Zeile:**
- Dittrich/Hoehn 2012: Pachner-Zuege als "canonical transformations on naturally extended phase spaces"
  [S Abstract].
- Hoehn 2015: 1-4 erzeugt vier Lapse/Shift-Variablen und vier Generatoren [S].
- Dittrich/Hoehn 2010: erste Klasse nur linearisiert um flach, sonst Pseudo-Bedingungen [S Abstract].
- Brewin/Gentle 2001: Regge-Loesungen sind "expected to be second order accurate" [S Abstract].
- 24-Monats-Suchen F8 und F13: leer.

## 4. Je Frage der Karte: Stand der Literatur

### 4.1 Simpliziale Supermetrik (Frage 1)

- **Herkunft:** Lund/Regge (unveroeffentlicht, HMW Ref. [10]). Untersucht von Piran/Williams 1986 und Friedman/Jack
  1986 (HMW S. 3) [S].
- **Kontinuum** (HMW S. 4, Gl. 2.1, 2.2) [S]:
  - (k', k) = Int d^3x N(x) G^abcd k'_ab k_cd mit G^abcd = 1/2 h^(1/2) [h^ac h^bd + h^ad h^bc - 2 h^ab h^cd].
  - Signatur je Punkt (-,+,+,+,+,+).
  - Horizontal = DeWitt-orthogonal zu D_(a xi_b); Konvention: minimaler Abstand; Eichbedingung
    D^b (k_ab - h_ab k^c_c) = 0 (S. 5, Gl. 2.5).
- **Simplizial** (S. 7 bis 9) [S]:
  - Eichung im Inneren: dh_ab konstant je Tetraeder (Gl. 3.4), N = 1.
  - G_mn dt^m dt^n = Summe_tau V(tau) {dh_ab dh^ab - (dh^a_a)^2} (Gl. 3.5), mit h_ab(tau) = 1/2 (t_0a + t_0b - t_ab)
    (Gl. 3.6).
  - G_mn = -Summe_tau (1/V(tau)) d^2 V^2(tau)/dt^m dt^n (Gl. 3.13)
    = -2 [d^2 V_TOT/dt^m dt^n + Summe_tau (1/V) dV/dt^m dV/dt^n] (Gl. 3.14).
  - **Signatur:** volumengewichtet ja; Geschwindigkeitsseite; Spurkoeffizient 1 (ART, lambda = 1).
- **Signatur** [S]:
  - Die konforme Richtung dt = dOmega^2 t ist immer zeitartig: G t t = -6 V_TOT (Gl. 3.19). Sie ist orthogonal zu jeder
    Eichrichtung (Gl. 3.21).
  - G = G~ - 4 Summe (1/V) dV dV mit G~ >= 0 (Gl. 3.22, 3.23, S. 11). Daraus folgen mindestens n1 - n3 raumartige
    Richtungen.
  - Zahlen siehe Erwartungsverstoss 5. Nahe flach gibt es auf T^3 Entartungen und Signaturwechsel (S. 21 f.).
  - Eckverschiebungs-Moden: Vorzeichen allgemein offen (Gl. 3.30). Auf T^3 in Sonderfaellen positiv, z. B. eine Ecke
    allein: dS^2 = 8 dr^2 (S. 20).
- **Weiterverwendung:** Hamber/Williams 2011 bauen darauf eine diskrete Wheeler-DeWitt-Gleichung [S Abstract]; ihre
  Formel ist nicht gelesen.
- **Regime:** nur H. Bruecke zu K: Friedman/Jack leiten die Lund-Regge-Wirkung aus der Einstein-Wirkung fuer
  stueckweise flache Schichten her [S Abstract].
- **Bezug zum Code [M]:**
  - Je Tetraeder, mit Kantenraten eps = T hdot: M_tau = V_tau T^-T G_v T^-1 und
    M_tau^-1 = (1/V_tau) [G_p(n_e n_e, n_f n_f)]_ef.
  - Dabei G_p = G_v^-1; in 3D ist G_p(X,Y) = X:Y - 1/2 trX trY, also das A0 aus ew.py, mit Gewicht 1/V gleich A2 je
    Element.
  - Global: A_LR = (Summe M_tau)^-1, dagegen A2 = Summe M_tau^-1.
  - Normierung der Kantenvariablen hier nicht abgeglichen; sie aendert nur einen gemeinsamen Faktor.

### 4.2 3+1-Regge mit Lapse und Shift (Frage 2)

- **Piran/Williams 1986** (PRD 33, 1622) [S Abstract]:
  - 3+1-Wirkung fuer allgemeine Raumzeiten nach Lund/Regge, in erster und zweiter Ordnung.
  - Anfangswerte ueber konforme Transformationen.
  - Wo Lapse und Shift sitzen: nicht im Abstract, nicht gelesen.
- **Friedman/Jack 1986** (JMP 27, 2973) [S Abstract]:
  - Die Einstein-Wirkung fuer stueckweise flache Dreimetriken gibt die Lund-Regge-Wirkung.
  - Mit a priori gewaehlter Lapse und Shift bleiben die Bedingungen nicht erhalten (anders als im Kontinuum).
  - Mit Shift != 0 und nicht konstanter Lapse bleiben sie erhalten. Den Hamilton-Formalismus erhaelt man ueber
    Bergmann-Dirac oder durch Loesen nach Lapse und Shift je Drei-Simplex.
  - Bei Shift = 0: eine Summe freier relativistischer Teilchen, eines je Tetraeder, gekoppelt ueber gemeinsame Kanten.
- **Sorkin-Schema** (Barrett u. a. 1997) [S Abstract]:
  - Ecken einzeln vorruecken, mit lokalen impliziten Gleichungen; Bezug zu den Bianchi-Identitaeten.
  - HMW (S. 23): 3 n0 naeherungsweise Diffeomorphismen ueber einen Shift-Vektor je Ecke (Miller 1986; Kheyfets/
    Miller/Wheeler 1988; nicht gelesen).
- **Regime K:**
  - Der 1-4-Zug erzeugt je neuer Ecke vier Lapse/Shift-Variablen und vier Eckverschiebungs-Generatoren; diese sind
    erster Klasse und abelsch, linearisiert um flach (Hoehn 2015, Abstract und S. 19 [S]).
  - Bei hoeherer Ordnung werden daraus Pseudo-Bedingungen (Dittrich/Hoehn 2010 [S Abstract]).
- **In beiden Regimen gleich [ES aus S]:** Exakt erste Klasse gibt es nur linearisiert um flach. Sonst werden entweder
  Lapse und Shift festgelegt (H) oder es bleiben Pseudo-Bedingungen (K).
- **Bezug zum Netz [ES]:** Unser Netz hat Lapse je Ecke und ein von Hand gesetztes Paar zweiter Klasse
  (SKALAR-SEKTOR-L 4 [P]). Laut Friedman/Jack erhaelt schon die Literaturform in stetiger Zeit die Hamilton-Bedingung
  nicht frei. Ob sie linearisiert um flach mit Lapse je Simplex erste Klasse erreicht, ist nicht gelesen.

### 4.3 Eich-Reduktion (Frage 3)

- **Literatur:**
  - **Christiansen 2011** (S. 15, Gl. 88 bis 91; S. 19; S. 20; Satz 4.7 S. 22) [S]:
    - Eigenproblem a(u, v) = lambda <u, v> auf Regge-Metriken.
    - W = Kern, V = L2-orthogonales Komplement von W.
    - Konvergenz der Eigenpaare auf quasi-uniformen Netzen des 3-Torus. Masse: kanonisches L2-Skalarprodukt
      (Frobenius).
  - **Hoehn 2015** (S. 15, 22) [S]:
    - Symplektische Reduktion in diskreter Zeit: abelsche Generatoren, eichinvariante Gitter-"Gravitonen".
    - Barretts Fundamentalsatz: Laengenstoerungen modulo Eckverschiebungen = linearisierte Fehlwinkel mit Bianchi-
      Identitaeten (topologisch trivial).
    - Kein Spektrum; der Bezug zum Kontinuum ist dort ausdruecklich offen.
  - **HMW 1997:** Lund-Regge ist gegen Eckverschiebungen nicht horizontal (S. 10); offene Aufgabe (S. 22 f.).
  - **Letzte 24 Monate (F8, F13):** nichts.
- **Schreibtisch fuer unser Netz [M, vorab ableitbar]:**
  - Lineares H = 1/2 p^H A p + 1/2 q^H B q.
  - Bedingungen: M^H p = 0 ist erster Klasse (B M = 0). Das Paar (c^H q, c^H p) ist zweiter Klasse (Klammer c^H c),
    mit c^H M = 0. Im Code ist c_v^H a = -Summe_{e an v} (B a)_e (ew.py, ops()).
  - Dirac-Klammer des c-Paars: {q, p}_D = P_c = 1 - c (c^H c)^-1 c^H. Mit q = S x, p = S y (S Orthonormalbasis des
    Komplements von Bild[M, c]) folgt x' = A_red y, y' = -B_red x. **Das ist woertlich R1** (ew.py, spektrum_punkt).
  - **Eichinvarianz:** p'' = -P_c B P_c A p auf ker[M, c]^H. Mit P_c = S S^H + P_M und S^H B P_M = 0 folgt
    S^H B P_c A S = B_red A_red. Eine andere Flaeche fuer M aendert die omega^2 nicht.
  - **Identitaet:** (S^H A S)^-1 = S^H Q S mit Q = A^-1 - A^-1 X (X^H A^-1 X)^-1 X^H A^-1, X = [M, c]. Die reduzierte
    Geschwindigkeitsmetrik ist also die horizontale.
  - Voraussetzungen: B M = 0 und c^H M = 0 exakt; A und X^H A^-1 X invertierbar.
- **Unterscheidungspunkt (Regel 2):**
  - Eine "nicht horizontale" Reduktion zeigt sich nur, wenn eine zweite Flaeche q = S' x mit S'^H S' != 1 ohne
    Korrektur der Symplektik eingesetzt wird; richtig waere x' = (S'^H S')^-1 ...
  - Eine solche Abweichung waere ein Implementierungsfehler, keine Physik.

### 4.4 Umklappen in kanonischer simplizialer Gravitation (Frage 4)

- **Dittrich/Hoehn 2012** [S Abstract]: Pachner-Zuege sind kanonische Transformationen auf natuerlich erweiterten
  Phasenraeumen. Manche Zuege bringen a priori freie Daten, die spaetere Bedingungen fixieren koennen.
- **Dittrich/Hoehn 2013** [S]:
  - Satz 3.1 (S. 13): Die globale Entwicklung ist nur prae-symplektisch:
    (iota_n^-)^* omega_n = H_n^* (iota_{n+1}^+)^* omega_{n+1}.
  - Typen: 1-4 und 2-3 (4D) sind Typ I (S. 22); 3-2 und 4-1 sind Typ II (S. 23).
  - Satz 4.1 (S. 25): Typ I/IV erhalten omega, eingeschraenkt auf die Nachbedingungsflaechen. Typ II/III erhalten es nur
    auf C_k^+ geschnitten mit K_k^-.
  - S. 41: Typ II/III senken den Rang um zwei je unabhaengiger, nicht zweitklassiger Vorbedingung.
  - Eichende Bedingungen sind zugleich Vor- und Nachbedingungen, also erster Klasse (S. 41).
  - Abstract: Nur bei translationsinvarianten Systemen kehrt die uebliche Unabhaengigkeit vom Zeitschritt zurueck.
- **Hoehn 2015** [S]:
  - Zaehlung (S. 19): 1-4 +4 Eichmoden; 2-3 +1 Graviton; 3-2 -1 Graviton und die einzige nichttriviale
    Bewegungsgleichung; 4-1 -4.
  - Linearisierter 2-3-Zug (S. 22): alte Laengen bleiben; Generatoren bleiben (11.3); alte Impulse
    pi_{k+1} = pi_k + S y; der Impuls der neuen Kante ist ueber die Nachbedingung pi_new = S y festgelegt (11.4). Der
    Fehlwinkel am neuen Bulk-Dreieck ist a priori frei.
  - Abstract: "Pachner moves preserve the vertex displacement generators".
- **Energie:** In diskreter Zeit gibt es kein erhaltenes H; der Rahmen sagt dazu nichts. Fuer stetige Zeit mit Umklappen
  fand ich keine Arbeit (F5, F8, F13).
- **Bezug zu TAKT-DYNAMIK-1 [ES]:**
  1. Der Verlust beim 3-2-Zug ist im Rahmen angelegt: Typ II; die Vorbedingung ist die Bewegungsgleichung an der
     wegfallenden Kante. Passend dazu zeigte TD0 einen Fehlwinkel an der wegfallenden Kante [P].
  2. Beim 2-3-Zug laesst die Literatur die neue Laenge frei und legt den neuen Impuls fest. Wir legen die neue Laenge
     auf Flachheit fest und die Rate (R) bzw. die Impulse (P). Keine der beiden Lesarten ist die Literaturabbildung.
  3. Die RK3-Bedeutung "Energiesprung = Fehler der Zustandsabbildung" folgt nicht. Symplektik erzwingt keinen
     Energieerhalt, und fuer das Regime H fehlt die Literatur.

### 4.5 TT-Isotropie auf unregelmaessigen Gittern (Frage 5)

- **Feinberg/Friedberg/Lee/Ren 1984** (NPB 245, 343) [S Abstract, Regime K]:
  - Kontinuumslimes fuer "any lattice, regular or irregular", unter allgemeinen Randbedingungen.
  - Abweichung als Potenzreihe in l^2; Beispiele darunter der Graviton-Propagator.
- **Christiansen 2011** [S, statischer Operator]: Die Eigenpaare des linearisierten 3D-Regge (Saint-Venant-Operator
  curl^T curl) konvergieren auf quasi-uniformen Netzen, mit L2-Masse.
- **Zwei Lager zur Konsistenz, mit Moderator:**
  - Brewin 2000 [S Abstract]: Residuen der Regge-Gleichungen auf Einstein-Loesungen trennen auf generischen Gittern
    nicht.
  - Brewin/Gentle 2001 [S Abstract]: Die Loesungen selbst sind zweiter Ordnung genau (Kasner).
  - Moderator: das Kriterium. Das Residuum versagt, Loesung und Spektrum konvergieren. Fuer uns zaehlt das Spektrum.
- **Weitere Treffer:** Hoehn 2015 (Kontinuumsbezug offen); Asante/Dittrich/Haggard 2018 (Randgravitonen, euklidisch);
  Gentle 2002 (Brill-Wellen); Zumbusch 2009 (FE/DG/FD-Zeitschritte) [S Abstract].
- **Ausdruecklicher Richtungsvergleich** langer Gravitonen auf unregelmaessigen Regge-Netzen: nicht gefunden (F5, F8,
  F13; F4 Fehlsuche).
- [ES] Im Regime K ist die Isotropie implizit behauptet (FFLR) bzw. fuer den statischen Operator bewiesen
  (Christiansen). Unser O(1)-Befund gehoert zum Regime H. Ob H mit Lund-Regge-Masse isotrop wird, ist weder gelesen
  noch gerechnet.

## 5. Urteile RK1 bis RK5 nach Kartenwortlaut

| Nr | Vorhersage (Kurzform) | Wahrsch. | Urteil | Beleg |
|---|---|---|---|---|
| RK1 | Supermetrik = volumengewichtete DeWitt-Metrik auf den Kantenlaengen; negative Richtungen an konformen Moden, etwa eine je Ecke | 55 % | **teilweise** | Teil 1 eingetroffen: HMW Gl. 3.5 und 3.13 (Quadrat-Kantenlaengen, Faktor V(tau), Geschwindigkeitsseite). Teil 2 in der Zahl verfehlt: 13 negative bei 27 Ecken (0,48 je Ecke, S. 21), 1 bei 5 Ecken (S. 14), vorlaeufig 92 bei 120 Ecken (S. 22); Schranke hoechstens n3. Die globale konforme Richtung ist immer negativ (Gl. 3.19). Die weiteren negativen sind horizontale Nicht-Eichrichtungen in den Volumenaenderungen (S. 21; Gl. 3.23), nicht "je Ecke". |
| RK2 | Im 3+1-Regge bleiben Impuls- und Hamilton-Bedingung nicht exakt erhalten bzw. brauchen Abaenderungen (FJ: erhaltene Impulsbedingung) | 60 % | **eingetroffen** | Friedman/Jack 1986 [S Abstract]: nicht erhalten bei a priori gewaehlter Lapse und Shift; erhalten mit Shift != 0 und nicht konstanter Lapse, geloest je Drei-Simplex. Zusatz: FJ erhalten **beide** Bedingungen, nicht nur die Impulsbedingung. |
| RK3 | Kanonische simpliziale Gravitation mit sich aendernden Gittern erhaelt die Symplektik ueber Pachner-Zuege; 1-4 bringt neue Bedingungen bzw. Eichfreiheit | 65 % | **teilweise** | Teil 2 eingetroffen: Hoehn 2015 (vier Lapse/Shift-Variablen und vier Generatoren je 1-4-Zug; S. 19, Abstract). Teil 1 nur eingeschraenkt: DH 2012 (kanonische Transformationen auf erweiterten Raeumen); DH 2013 Satz 3.1 (nur prae-symplektisch, S. 13). Nach Satz 4.1 erhalten 1-4 und 2-3 omega auf den Nachbedingungsflaechen, 3-2 und 4-1 senken den Rang (S. 25, 41). Gilt fuer Regime K. |
| RK4 | Ausdrueckliche horizontale Reduktion der Eckverschiebungs-Eichung mit Nachweis der Eichflaechen-Unabhaengigkeit des Spektrums steht in der Literatur | 40 % | **teilweise** | Vorhanden: ausdrueckliche massen-orthogonale Zerlegung X = V (+) W gegen den Kern, mit Spektralkonvergenz (Christiansen 2011, Gl. 89 bis 91, Satz 4.7; statisch, L2-Masse); symplektische Reduktion in diskreter Zeit (Hoehn 2015). Nicht gefunden: ein ausdruecklicher Eichflaechen-Vergleich des Spektrums und eine horizontale Lund-Regge-Form (HMW S. 10, S. 22 f.: offen). 24 Monate (F8, F13): nichts. Nach Recherchestand nicht belegt, nicht widerlegt. |
| RK5 | Isotropie langer Gravitonwellen auf unregelmaessigen Regge-Gittern ist untersucht | 35 % | **teilweise** | Implizit belegt: Feinberg/Friedberg/Lee/Ren 1984 (Kontinuumslimes auf beliebigen Gittern, l^2-Reihe, Graviton-Propagator als Beispiel; nur Abstract) und Christiansen 2011 (Eigenpaarkonvergenz auf quasi-uniformen Netzen). Ein ausdruecklicher Richtungsvergleich ist nicht gefunden (F5, F8, F13). Nach Recherchestand nicht belegt, nicht widerlegt. |

**Bedeutung, wie auf der Karte vorab festgelegt:**
- "RK1 und RK4 treffen ein: ... Abweichungen unseres Codes davon waeren dann zu berichtigen": **halb ausgeloest.**
  - Eine Standardform gibt es: Lund-Regge auf der Geschwindigkeitsseite, dazu die orthogonale Zerlegung gegen den Kern.
  - Die Abweichung unseres Codes ist die **Seite** der Bewegungsform (Impuls statt Geschwindigkeit), nicht die
    Reduktion [ES].
- "RK3 trifft ein: ... Energiesprung waere dann ein Fehler unserer Zustandsabbildung": **nicht ausgeloest.**
  RK3 trifft nur teilweise ein, und Symplektik sagt nichts ueber Energie.
- "RK5 verfehlt: eigener Projektbeitrag": **nicht ausgeloest.**
  - Im kovarianten bzw. statischen Regime ist Isotropie Literatur.
  - Ein Projektbeitrag waere hoechstens der Befund im Regime H: Die gesetzte Bewegungsenergie bricht die Isotropie
    [H].

## 6. Was folgt fuer HODGE-MASSE-1 und die Zustandsabbildung beim Umklappen [H, ES]

**HODGE-MASSE-1:**
1. **Rueckfrage vor dem Rechnen: Welche Seite meint "A2"?**
   - Wie in TT-ISO-1 (J_t -> J_t V_F/V_t auf der Impulsseite): Dann ist HM0 keine Identitaet [M]. Ein Verfehlen von
     HM0 waere kein Codefehler.
   - Auf der Geschwindigkeitsseite: Dann ist HM0 eine Identitaet (HMW Gl. 3.5, Summe V_tau = V_tot).
2. **HM1 als Identitaetsprobe fuehren, nicht als Messung.**
   - R1 ist schon Dirac plus horizontal (4.3). Zwei M-Flaechen muessen dieselben omega^2 bis Rundung geben.
   - Weicht eine zweite Flaeche ab, zuerst pruefen, ob deren Symplektik (S'^H S') beruecksichtigt ist.
3. **Literatur-Standardform einbauen:**
   - M_LR(k) = Summe_tau V_tau T_tau^-T G_v T_tau^-1, mit G_v(X, Y) = X:Y - trX trY und Bloch-Phasen wie in ops().
   - Dann A = M_LR(k)^-1 je k; R1 unveraendert.
   - Gleichwertig in Quadrat-Kantenlaengen: G_mn = -Summe_tau (1/V) d^2 V^2/dt^m dt^n (HMW Gl. 3.13).
4. **Vorsicht bei M_LR:**
   - M_LR ist indefinit, nahe flach teils entartet (Null-Eigenwerte auf dem rechtwinkligen Tetraedergitter, HMW
     S. 21). Erst die Traegheit von M_LR und A_red zaehlen.
   - Die globale konforme Richtung ist immer zeitartig und orthogonal zu allen Eichrichtungen (HMW Gl. 3.19, 3.21). Sie
     ueberlebt [M, c].
   - Das erklaert den TAKT-DYNAMIK-1-Rauchtest r1 (A_red indefinit bei k = 0) und die Abhilfe "Kastenvolumen fest"
     (TAKT-DYNAMIK-1, Selbstanzeige 1 [P]) [ES].
5. **Unterscheidungspunkt 1 (H_A Massenform gegen H_B Netz an sich):**
   - Messen: TT-Spanne gegen |k| (etwa 1e-2, 3e-2, 1e-1) mit M_LR auf V und Glas N = 128.
   - H_A sagt: Die Spanne faellt wie (kl)^2 gegen null. H_B sagt: Sie bleibt bei kl -> 0 endlich.
   - Mit der jetzigen Impulsform sagen beide eine endliche Spanne voraus. Dort sind sie nicht trennbar.
6. **HM2/HM3 [H]:** Gilt H_A, dann wird die Spanne mit M_LR ohne Abstimmung klein. Mit A2 auf der Impulsseite ist das
   nicht ableitbar.

**Zustandsabbildung beim Umklappen (TAKT-DYNAMIK-1):**
7. **Natuerliche Abbildung mit M_LR: Lesart R.** Laengen und Raten bleiben stetig; die neue Rate folgt kinematisch aus
   den Eckgeschwindigkeiten (das ist die linearisierte Cayley-Menger-Flachheit).
   - [M]: Die mittlere Verzerrungsrate der Doppelpyramide ist in beiden Zerlegungen gleich. Grund: Randintegral der
     P1-Geschwindigkeit ueber dieselben sechs Aussenflaechen.
   - Der Sprung ist daher Summe_neu V G_v(eps - eps_quer) - Summe_alt V G_v(eps - eps_quer). Er ist null bei affinen
     Eckgeschwindigkeiten und fuer lange Wellen unterdrueckt.
   - Bei kl ~ 1,5 (TAKT-DYNAMIK-1, Grenzen [P]) ist das keine kleine Zahl. HM4 (< 1e-4 H0) ist dort eher nicht zu
     erwarten [H].
   - Unterscheidungspunkt 2: Sprung je Zug gegen kl. Mit M_LR erwartet man (kl)^2-Unterdrueckung; mit A1 haengt der
     Sprung nur am Anteil der Zellen, nicht an kl.
8. **3-2-Zug:** Der Verlust ist im Rahmen angelegt (Typ II; die einzige Bewegungsgleichung). Zwei Anteile getrennt
   ausweisen:
   - die Fehlwinkel-Energie an der wegfallenden Kante (Delta V);
   - den kinetischen Schwankungsanteil.
9. **Symplektik ist nicht Energie [M]:**
   - Lesart P mit p_neu = 0 ist bis zur Einbettung symplektisch: omega_neu, zurueckgezogen, ist omega_alt.
   - Die anschliessende Projektion auf die neue Zwangsflaeche ist es nicht notwendig. H bleibt in keinem Fall erhalten.
   - Eine Abbildung, die in stetiger Zeit zugleich symplektisch ist und H erhaelt, fand ich in der Literatur nicht.

## 7. Kartenvorschlag (einer): LUND-REGGE-MASSE-1 (Kleintest, vorhandener Code, nur Literaturform)

- **Frage:** Wird die langwellige TT-Spanne klein, wenn die Bewegungsenergie die Lund-Regge-Form auf der
  Geschwindigkeitsseite ist? R1 bleibt unveraendert.
- **Bedingung:** Nur sinnvoll, wenn HODGE-MASSE-1 mit "A2" die Impulsseite rechnet. Daher zuerst die Rueckfrage aus
  6.1. Sonst entfaellt die Karte.
- **Aufbau:**
  - ew.py kopieren; A durch M_LR(k)^-1 ersetzen.
  - Netze V und Glas N = 128 (4 Saaten); |k| = 1e-2, 3e-2, 1e-1; 13 Richtungen.
  - Laeufe auf der .69 ueber kleintest.sh, je Lauf <= 10 min.
- **Vorhersagen (vor jeder Rechnung, Vorschlag):**
  - L0, Kontrolle, vorab ableitbar [M]: Gleichmaessige Rate gibt V_tot G_v(hdot) auf 1e-12 auf allen Netzen (90 %).
  - L1 [H]: A_red mit M_LR ist ausserhalb Gamma auf V und Glas positiv definit (50 %).
  - L2 [H]: Die Spanne auf V bei |k| = 1e-2 liegt unter 1e-3 (35 %).
  - L3 [H]: Die Spanne faellt von |k| = 1e-1 auf 1e-2 um mindestens den Faktor 10 (H_A) (40 %).
- **Ableitbarkeitsprobe (Bausteine verkettet):**
  - L0 ist vorab ableitbar (HMW Gl. 3.5); es ist eine Kontrolle, keine Messung.
  - L1 ist nicht ableitbar. HMW zaehlen negative Richtungen ohne Bedingungen (13 von 189), die Wirkung von [M, c] ist
    unbekannt.
  - L2 und L3 sind nicht ableitbar. Die Konvergenzsaetze gelten fuer die L2-Masse im statischen Fall (Christiansen)
    bzw. kovariant (FFLR, nur Abstract). Fuer die indefinite DeWitt-Masse mit Relaxation auf dem Zufallsnetz legt keine
    gelesene Identitaet das Ergebnis fest.
  - Projektbefunde machen L2/L3 plausibel, nicht zwingend: affine Steifigkeit isotrop auf 1,7e-5, nichtaffine
    Relaxation <= 1e-5 (TT-GLAS-2 [P]).
  - Maxwell-artige Zaehlung: Je Ecke sind 3 Eichrichtungen und 1 Skalarpaar unveraendert wie in R1. Neue Bedingungen
    kommen nicht hinzu.
- **Synthetisch, keine Messdatenbestaetigung.**

## 8. Negativliste (was dieses Dossier nicht sagt)

- Nicht: "Die Lund-Regge-Form beseitigt die Anisotropie." Das ist nicht gerechnet [H].
- Nicht: "R1 ist falsch." Das Gegenteil ist [M] gezeigt, unter B M = 0 und c^H M = 0.
- Kein "widerlegt". Die Luecken bei RK4 und RK5 heissen "nach Recherchestand nicht belegt".
- FFLR: nur das Abstract gelesen. Offen ist, ob dort die Isotropie ausdruecklich gerechnet ist und welche Gitterform
  genau gemeint ist.
- Nicht gelesen:
  - die Lapse/Shift-Lage bei Piran/Williams;
  - die Formel bei Hamber/Williams 2011;
  - Hamber/Williams "Gauge Invariance in Simplicial Gravity" (nur der Titel in F12).
- Keine Literaturaussage zur Energie beim Umklappen in stetiger Zeit. 6.7 ist [M] + [H], keine Literatur.
- Christiansens Satz gilt fuer L2-Masse und quasi-uniforme Netze, nicht fuer DeWitt-Masse oder beliebige Zufallsnetze.
- Keine Messdaten.

## 9. Selbstanzeigen

1. **Zeiten:** Viermal stand eine Zeit vor der Messung im Arbeitsfeld (F4-Kopf, F6-Kopf, Gegensweep-Kopf, Abschnitte
   3 bis 5). Sie sind gestrichen und durch date-Werte ersetzt.
2. **Seitenzahlen:** DH 2013, Hoehn 2015 und eine Christiansen-Stelle nahm ich zuerst aus den Fusszeilen der
   Textfassung; sie lagen um eins daneben. Per Seitenextraktion berichtigt und im Arbeitsfeld gestrichen.
3. **Leere Abrufe:** F1a (http ohne Weiterleitung, leer) und F4 (die Phrasensuche griff nicht) brachten nichts; beide
   sind gezaehlt.
4. **Zitate:** Im Arbeitsfeld standen anfangs mehrere woertliche Zitate je Quelle. Nach 10:00:35 (date) habe ich sie in
   Umschreibungen umgewandelt (Urheberrechtsregel).
5. **FJ-Abstract:** aus dem OpenAlex-Wortindex mit jq zusammengesetzt. Der Wortlaut ist gesichert, die Satzzeichen nicht.
6. **Code gelesen:** ew.py stand nicht auf der Leseliste; ich habe es nur gelesen, nicht ausgefuehrt. Der [M]-Befund
   zu R1 haengt an dieser Lesart und an den [P]-Werten fuer B M und c^H M.
7. **Geratene Seitenzahl:** Bei Williams 1986 stand "CQG 3, 1045?"; gestrichen.
8. **Nicht gegengelesen:** die [M]-Rechnungen (Dirac-Reduktion, Identitaet, A2 != Lund-Regge).
9. **Kalibrierung:** Meine Sicherheit, dass die Bewegungsform die Hauptursache der O(1)-Anisotropie ist, stieg im
   Lauf ohne neue Messung. Gestuetzt ist sie nur durch Konvergenzsaetze anderer Regime; das ist gewachsene Gewissheit
   (Abschnitt 11.4).

## 10. Einfach gesagt

Wir wollten wissen, wie Fachleute die Bewegungsenergie eines Tetraedernetzes fuer die Schwerkraft aufschreiben. Die
Standardform rechnet mit den Geschwindigkeiten, gewichtet jede Zelle mit ihrem Volumen und addiert. Unser Programm
macht etwas Aehnliches, aber mit den Impulsen, und im Netz ist das nicht dasselbe. Unser Weg, die Eichung herauszurechnen,
ist dagegen schon richtig; an ihm liegt die Richtungsabhaengigkeit nicht. Andere Arbeiten zeigen, dass solche Netze fuer
lange Wellen in alle Richtungen gleich schnell werden, wenn die Bewegungsenergie in der Standardform steht. Ob das bei
uns hilft und ob das Umklappen von Zellen dann weniger Energie kostet, muss eine Rechnung zeigen.

## 11. Regime, Unterscheidungspunkte, Gegensweep, Kalibrierung, offene Fragen

### 11.1 Regime und Moderatoren

| Aussage | Regime H (stetige Zeit) | Regime K (diskrete Zeit/4D/statisch) | in beiden? |
|---|---|---|---|
| Bewegungsform | Lund-Regge, Geschwindigkeitsseite, volumengewichtet (HMW) | implizit in der 4D-Wirkung; FJ verbinden beide | ja, ueber FJ |
| Erste Klasse der Hamilton-Bedingung | nein, ausser Lapse/Shift bestimmt (FJ) | nur flach-linear; sonst Pseudo-Bedingungen (DH 2010) | ja: nur flach-linear exakt |
| Symplektik ueber Zuege | keine Arbeit gefunden | Typ I erhalten (eingeschraenkt), Typ II Rangverlust (DH 2013) | nur K belegt |
| Isotropie langer Wellen | nicht belegt; unser Netz O(1) mit gesetzter Form [P] | FFLR (Abstract), Christiansen (statisch, L2) | nur K belegt |
| Konsistenz | - | Residuum versagt (Brewin), Loesung O(l^2) (Brewin/Gentle) | Moderator: Kriterium |

- **Moderatoren:**
  - Seite der Bewegungsform (Geschwindigkeit/Impuls).
  - Herkunft der Bewegungsform (aus 4D-Wirkung abgeleitet oder gesetzt; GAMMA-NETZ-L: "gesetzt und nicht aus einer
    4D-Wirkung abgeleitet" [P]).
  - Zeit (stetig/diskret).
  - Kriterium (Residuum/Loesung/Spektrum).

### 11.2 Unterscheidungspunkte (Regel 2)

1. **H_A Massenform gegen H_B Netz an sich:** TT-Spanne gegen kl bei festem Netz, gerechnet mit M_LR. H_A sagt
   (kl)^2 -> 0, H_B sagt endlich. Mit der jetzigen Impulsform nicht trennbar.
2. **Energiesprung aus Gewichten gegen aus Zustandsabbildung:** Sprung je Zug gegen kl. M_LR + Lesart R sagt
   (kl)^2-Unterdrueckung, A1 sagt keine kl-Abhaengigkeit. Bei kl ~ 1,5 nicht trennbar.
3. **Seite der Supermetrik:** gleichmaessige Rate auf einem unregelmaessigen Netz. M_LR gibt exakt den Kontinuumswert
   (Identitaet); A2 auf der Impulsseite im Allgemeinen nicht. Das ist HM0.
4. **FFLR gegen Brewin:** Residuum der Regge-Gleichungen auf exakten Kontinuumsloesungen (Brewin: trennt nicht) gegen
   Fehler der diskreten Loesung bzw. des Spektrums (O(l^2)). Fuer Dispersion und Abstrahlung zaehlt das Zweite.

### 11.3 Gegensweep (Regel 4)

- **Selbstverstaendlich und nicht geprueft waren:**
  1. Christiansens Netzannahme und Masse;
  2. ob FFLRs "lattice gravity" das Regge-Funktional im noetigen Sinn ist;
  3. ob die F4-Fehlsuche Einschlaegiges verdeckt;
  4. welche Seite HODGE-MASSE-1 mit "A2" meint;
  5. ob Piran/Williams Lapse und Shift auch je Simplex setzen.
- **Geprueft (F14):** Punkt 1. Christiansen setzt quasi-uniforme Netze und die L2-Masse voraus, nicht die DeWitt-
  Masse. Damit ist die Uebertragung auf unser Netz (DeWitt, Zufallsglas) eine [ES]-Kette, kein Satz.
- **Gegensuche "Verletzung von Energie oder Symplektik bei wechselnden Gittern":**
  - Gefunden: in diskreter Zeit (DH 2013, Typ II senkt den Rang) und fuer Bedingungen in stetiger Zeit (FJ 1986).
  - Letzte 24 Monate (F8, F13): 18 Treffer; einschlaegig nur Bruno/Colafranceschi/Mele/Rovelli 2026 (Kontinuumslimes
    von Spinschaum) und Khatsymovsky 2026 (Stoerungsreihe der diskreten Gravitation). Keiner betrifft Energie oder
    Symplektik beim Umklappen.
- **Offen:** Punkte 2, 3 und 5. Punkt 4 ist eine Rueckfrage an die Leitung.

### 11.4 Kalibrierung

- **(a) Gemessen bzw. an der Quelle gelesen:**
  - HMW Gl. 3.5, 3.13, 3.14, 3.19, 3.21 bis 3.23 und die Zaehlungen (S. 14, 21, 22);
  - FJ (Abstract);
  - DH 2013, Saetze 3.1 und 4.1 und die Typen;
  - Hoehn 2015, Zaehlung und 2-3-Abbildung;
  - FFLR (Abstract);
  - Christiansen, Gl. 89 bis 91, Netzannahme und Satz 4.7.
- **(b) Nuetzlich verdichtet [M, ES]:**
  - "Standardform = Geschwindigkeitsseite; unser A = Summe der Element-Inversen";
  - "R1 = Dirac + horizontal, eichflaechenfrei";
  - die Regime-Tabelle;
  - die Sprung-Zerlegung beim 2-3-Zug.
- **(c) Gewachsene Gewissheit ohne neue Evidenz:**
  - die Erwartung, dass M_LR die TT-Spanne und den Umklapp-Sprung stark senkt;
  - die Lesart der TT-GLAS-2-Projektionsanisotropie als nichtaffine Relaxation mit ~N^-1/2.
  - **Warnzeichen:** Die Frage loeste sich vom "gibt es eine Standardform" zum "welche Seite der Legendre-Abbildung"
    fein auf, und meine Sicherheit stieg dabei ohne Messung.

### 11.5 Offene Fragen und Rueckfragen

1. **Rueckfrage an die Leitung:** Meint HODGE-MASSE-1 mit "A2" die Impulsseite (wie TT-ISO-1)? Davon haengt ab, ob
   HM0 eine Identitaet ist (6.1).
2. Erreicht FJ mit Lapse/Shift je Simplex linearisiert um flach erste Klasse? Volltext nicht gelesen.
3. Ist die Gitter-Passbedingung "A c_v in Bild M" (GAMMA-NETZ-L [P]) mit M_LR erfuellt? Nicht ableitbar; ein Teil von
   LUND-REGGE-MASSE-1 koennte es mitmessen.
4. Gibt es fuer stetige Zeit eine Erzeugende fuer den 2-3-Zug, die zugleich symplektisch ist und H erhaelt? In der
   gelesenen Literatur nicht.
5. Verwandte Erfahrung aus der Numerik bewegter Netze (Remap mit Impuls- bzw. Energiefehler): nur Gedaechtnis [L],
   nicht geprueft; als Spur fuer einen spaeteren Abruf notiert.

## 12. Quellenliste mit Abrufstand

| Quelle | Gelesen | Abruf |
|---|---|---|
| Hartle, J.B.; Miller, W.A.; Williams, R.M. (1997): Signature of the simplicial supermetric. Class. Quantum Grav. 14, 2137-2155. https://arxiv.org/abs/gr-qc/9609028 | Volltext [S] | F1, F2 (quellen/F2-...pdf) |
| Friedman, J.L.; Jack, I. (1986): 3+1 Regge calculus with conserved momentum and Hamiltonian constraints. J. Math. Phys. 27, 2973. https://doi.org/10.1063/1.527224 | Abstract (OpenAlex) | F3 |
| Piran, T.; Williams, R.M. (1986): Three-plus-one formulation of Regge calculus. Phys. Rev. D 33, 1622. https://doi.org/10.1103/physrevd.33.1622 | Abstract (OpenAlex) | F3 |
| Dittrich, B.; Hoehn, P.A. (2012): Canonical simplicial gravity. Class. Quantum Grav. 29, 115009. https://arxiv.org/abs/1108.1974 | Abstract | F1 |
| Dittrich, B.; Hoehn, P.A. (2013): Constraint analysis for variational discrete systems. J. Math. Phys. 54, 093505. https://arxiv.org/abs/1303.4294 | Volltext [S] | F1, F6 |
| Hoehn, P.A. (2015): Canonical linearized Regge Calculus: counting lattice gravitons with Pachner moves. Phys. Rev. D 91, 124034. https://arxiv.org/abs/1411.5672 | Volltext [S] | F1, F5, F7 |
| Dittrich, B.; Hoehn, P.A. (2010): From covariant to canonical formulations of discrete gravity. Class. Quantum Grav. 27, 155001. https://arxiv.org/abs/0912.1817 | Abstract | F1 |
| Hoehn, P.A. (2014): Classification of constraints and degrees of freedom for quadratic discrete actions. J. Math. Phys. 55, 113506. https://arxiv.org/abs/1407.6641 | Abstract | F1 |
| Hamber, H.W.; Williams, R.M. (2011): Discrete Wheeler-DeWitt equation. Phys. Rev. D 84, 104033. https://arxiv.org/abs/1109.2530 | Abstract | F1 |
| Barrett, J.W.; Galassi, M.; Miller, W.A.; Sorkin, R.D.; Tuckey, P.A.; Williams, R.M. (1997): A parallelizable implicit evolution scheme for Regge calculus. Int. J. Theor. Phys. 36, 815. https://arxiv.org/abs/gr-qc/9411008 | Abstract | F1 |
| Gentle, A.P. (2002): Regge calculus: a unique tool for numerical relativity. Gen. Rel. Grav. 34, 1701. https://arxiv.org/abs/gr-qc/0408006 | Abstract | F1, F5 |
| Feinberg, G.; Friedberg, R.; Lee, T.D.; Ren, H.C. (1984): Lattice gravity near the continuum limit. Nucl. Phys. B 245, 343. https://doi.org/10.1016/0550-3213(84)90436-X | Abstract (INSPIRE) | F10 |
| Brewin, L. (2000): Is the Regge calculus a consistent approximation to general relativity? Gen. Rel. Grav. 32, 897. https://arxiv.org/abs/gr-qc/9502043 | Abstract | F11 |
| Brewin, L.C.; Gentle, A.P. (2001): On the convergence of Regge calculus to general relativity. Class. Quantum Grav. 18, 517. https://arxiv.org/abs/gr-qc/0006017 | Abstract | F11 |
| Christiansen, S.H. (2011): On the linearization of Regge calculus. https://arxiv.org/abs/1106.4266 (Zeitschrift nicht geprueft) | Volltext [S] | F11, F14 |
| Christiansen, S.H.; Lin, T. (2026): Regge metrics with enhanced trace. https://arxiv.org/abs/2603.13977 | Abstract | F11 |
| Christiansen, S.H.; Hu, K.; Lin, T. (2023): Extended Regge complex for linearized Riemann-Cartan geometry and cohomology. https://arxiv.org/abs/2312.11709 | Abstract | F11 |
| Brewin, L. (2015): A numerical study of the Regge Calculus and Smooth Lattice methods on a Kasner cosmology. https://arxiv.org/abs/1505.00067 | Abstract | F11 |
| Asante, S.K.; Dittrich, B.; Haggard, H.M. (2018): Holographic description of boundary gravitons in (3+1) dimensions. https://arxiv.org/abs/1811.11744 | Abstract | F5 |
| Zumbusch, G. (2009): Finite element, discontinuous Galerkin, and finite difference evolution schemes in spacetime. https://arxiv.org/abs/0901.0851 | Abstract | F5 |
| Williams, R.M. (1986): Quantum Regge calculus in the Lorentzian domain and its Hamiltonian formulation. Class. Quantum Grav. 3. https://doi.org/10.1088/0264-9381/3/5/015 | Abstract | F3 |
| Porter, J.R. (1987): A new approach to the Regge calculus: I. Formalism. Class. Quantum Grav. 4. https://doi.org/10.1088/0264-9381/4/2/017 | Abstract | F3 |
| Bruno, M.; Colafranceschi, E.; Mele, F.M.; Rovelli, C. (2026): The structure of the continuum limit of spin foams. https://arxiv.org/abs/2603.16999 | Abstract | F8 |
| Khatsymovsky, V.M. (2026): Towards the consistent perturbative expansion in discrete gravity. https://arxiv.org/abs/2601.02181 | Abstract | F13 |
| Websuchen F9, F12: nur Trefferlisten (u. a. https://arxiv.org/abs/gr-qc/0101028, https://arxiv.org/abs/gr-qc/9702006, https://arxiv.org/abs/hep-th/9607153); nicht als Quelle verwendet | - | F9, F12 |
| Projekt [P]: hodge-masse-1/KARTE.md; takt-dynamik-1/ERGEBNIS.md Abschn. 2, 5, 6; tt-glas-2/ERGEBNIS.md (Berichtigung, Abschn. 2, 4.2, 5); impuls-netz-1/ERGEBNIS.md Abschn. 2, 4; skalar-sektor-l/DOSSIER.md Abschn. 2 bis 5; RUNDE-36/REGEL.md Z. 29; takt-dynamik-1/code/ew.py (gelesen) | lokal | - |

---
Abgabe: 2026-10-05 10:09:30 CEST (date). 15 von 15 Netzabrufen. Geschrieben nur in RUNDE-37/regge-kinetik-l/.
