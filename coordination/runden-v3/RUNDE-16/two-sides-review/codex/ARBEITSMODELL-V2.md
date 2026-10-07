# Zwei gekoppelte Felder auf einer beweglichen Geometrie — Arbeitsmodell v2

2. Oktober 2026. Überarbeitung des Downloads, Original unverändert.
Status: explizites klassisches Spielzeugmodell und prüfbare Hypothesen.
Keine Herleitung von Elementarteilchen, Eigenzeit oder Gravitation.

## 1. Was das Modell wirklich enthält

Drei Ebenen bleiben getrennt:

1. **Träger:** ein fester Graph mit beweglichen Knoten x_i in R³.
2. **Dynamik:** ein komplexes skalares Feld ψ_i und ein reelles skalares Feld χ_i.
3. **Messung:** passive Ebenen bzw. Detektoren lesen Geometrie und Felder aus.

Das komplexe Feld allein besteht bereits aus zwei reellen Komponenten. Das
ist weder eine zweite Raumseite noch Antimaterie. χ ist hier eine zusätzliche,
physikalisch anders gekoppelte Variable. Beide leben zunächst im selben Raum.
Raum und Zeit werden vorausgesetzt, nicht durch diese Gleichungen erzeugt.

Die im Bundle rekonstruierte 12-/20-Knoten-Tetraederkette und ein planarer
11+1-/19+1-Ring sind VERSCHIEDENE Graphen. Sie erhalten getrennte IDs und
Koordinatendateien. Die Bedeutung des ursprünglichen „+1“ bleibt ungeklärt.

## 2. Ein konsistenter, dimensionsloser Wirkungskern

Für ungerichtete Kanten e={i,j}, jede genau einmal:

\[
L=\sum_i\left[\frac{m_i}{2}|\dot x_i|^2+|\dot\psi_i|^2+
\frac12\dot\chi_i^2\right]-\mathcal V(x,\psi,\chi),\qquad m_i>0,
\]
\[
\mathcal V=\sum_{e}\frac{k_e}{2}(r_e-\ell_e)^2+
\sum_i U(S_i,\chi_i)+\sum_e\left[J(r_e)|\psi_i-\psi_j|^2+
\frac{K(r_e)}2(\chi_i-\chi_j)^2\right],\quad S_i=|\psi_i|^2.
\]

Ein konkreter Zweifeld-Kandidat, Anschluss an FADEN-KERN-1:

\[
U(S,\chi)=\frac14(\chi^2-1)^2+(1+\chi^2)S-S^2+\frac12S^3.
\]

Er ist nach unten beschränkt, denn exakt:

\[
U=\frac14(\chi^2-1+2S)^2+\frac12 S(S-2)^2\ge0.
\]

Für S≥0 sind die Vakuua S=0, χ=±1. Für einen einzelnen Sektor wählen wir
χ→+1 am Fernrand. Auf einem endlichen Graphen wird dieser Rand NICHT still
angenommen: freie Randknoten und fixierte Vakuumrandknoten sind verschiedene
Versuche. Eine endliche Kette hat zunächst kein räumliches Strahlungskontinuum.

Zulässige glatte Kopplungen sind beispielsweise
J(r)=J_0 exp[-(r/ℓ_J)²], K(r)=K_0 exp[-(r/ℓ_K)²], alle Parameter positiv.
Konstante J,K sind die entkoppelte Geometrie-Kontrolle: Dann beeinflusst die
Geometrie die Feldgleichungen dieses Graphmodells überhaupt nicht.
Abstandsabhängige J,K sind eine zusätzliche Modellannahme, keine Ableitung
aus der Geometrie. Der Federterm hält eine endliche Referenzgröße, erlaubt
aber keinen Bindungsbruch. Ohne Kontaktterm dürfen fremde Kanten passieren.

## 3. Bewegungsgleichungen und Bilanzen

Mit obiger Kinetik und Wirtinger-Ableitung ergeben sich:

\[
\ddot\psi_i+\sum_{j:\{i,j\}\in E}J(r_{ij})(\psi_i-\psi_j)
 +(1+\chi_i^2-2S_i+\tfrac32S_i^2)\psi_i=0,
\]
\[
\ddot\chi_i+\sum_j K(r_{ij})(\chi_i-\chi_j)
 +\chi_i(\chi_i^2-1)+2\chi_i S_i=0.
\]

Für r_ij>0 ist die Kraft auf i durch die Kante ij:

\[
F_{ij}=-\left[k_{ij}(r_{ij}-\ell_{ij})+
J'(r_{ij})|\psi_i-\psi_j|^2+
\frac12K'(r_{ij})(\chi_i-\chi_j)^2\right]
\frac{x_i-x_j}{r_{ij}},\qquad F_{ji}=-F_{ij}.
\]

Die Wahl abnehmender J,K erzeugt durch die Feld-Differenzterme bei gegebenen
Feldwerten einen abstoßenden mechanischen Beitrag, NICHT automatisch eine
Anziehung. Induzierte Kräfte nach Feldrelaxation sind eine andere Frage.
Die Formeln gelten kollisionsfern; r=0 erfordert eigenes Kontakt-/Kollisionsmodell.

Erhalten bei autonomer, freier, geschlossener Dynamik:

\[
E=T+\mathcal V,\quad Q=2\sum_i\operatorname{Im}(\psi_i^*\dot\psi_i),
\quad P=\sum_i m_i\dot x_i,\quad L_{\rm mech}=\sum_i x_i\times m_i\dot x_i.
\]

Hier sind die Felder knotengebundene interne Oszillatoren ohne separat
modellierten Translationsimpuls. Dies ist kein relativistisch bewegtes
Kontinuumsfeld. Bei fixierten Rändern, Antrieb, Dämpfung oder Absorbern sind
deren Energie-, Ladungs- und Impulsflüsse zu protokollieren. Ω ist bei freier
Dynamik eine Anfangsbedingung/ausgewertete Bewegung, kein erzwungener Takt.
Ein vorgeschriebener Ringumlauf ist nur ein kinematischer Kontrollarm.

## 4. Korrektur des Einfeld-Anschlusses

Für ein komplexes Kontinuumsfeld passt zur Gleichung □Φ+∂V/∂Φ*=0 die Kinetik
\(\partial_\mu\Phi^*\partial^\mu\Phi\), ohne Faktor1/2. Bei Kinetik1/2
steht stattdessen 2∂V/∂Φ* in der Gleichung. Ohne Konjugation ist die Kinetik
im Allgemeinen nicht einmal reell. Konventionen müssen durchgängig gelten.

Bei V(S)=m²S−λS²+gS³, λ,g>0:

\[
V'(S)=m^2-2\lambda S+3gS^2,\qquad
\min_{S>0}V(S)/S=m^2-\lambda^2/(4g).
\]

Für nichtnegatives V ist m²≥λ²/(4g) hinreichend. Das übliche
Q-Ball-Frequenzfenster in dieser Normierung lautet
\(m^2-\lambda^2/(4g)<\omega^2<m^2\). Das ist ein Kontinuums-Ansatzkriterium, KEIN Existenz-/Stabilitätsbeweis
für den endlichen beweglichen Graphen. Die ursprüngliche positive kubische
Nichtlinearität in Abschnitt2 allein ist nicht dasselbe sextische Modell.

Primäranker: Battye/Sutcliffe, hep-th/0003252v1, §2, Gl.(2.1)–(2.6), am
HTML-Original gelesen: https://arxiv.org/html/hep-th/0003252v1 . Dort gilt die
HALBE Kinetik und entsprechend ein anderer Potential-/Frequenzfaktor.
Keine numerischen Q-Ball-Werte ohne Umrechnung übernehmen.

## 5. Was „zweite Seite“ mechanistisch bedeuten kann

χ ist kein Spiegelraum, sondern ein dynamischer Antwortkanal. Bei gegebenem
S minimiert lokal χ²=max(0,1−2S). Größere ψ-Dichte kann χ absenken und damit
den ψ-Massenterm verändern. Das ist eine konkrete Rückkopplung.

Für χ=1+η nahe dem Vakuum ist die führende durch ψ erzwungene Antwort:

\[
\ddot\eta+(L_K+2I)\eta=-2S+\text{höhere Terme}.
\]

Die Quelle S=|ψ|² ist quadratisch: In der strikt linearen gemeinsamen
Vakuumtheorie sind ψ und η entkoppelt. Der Green-Operator hier setzt für
diese Näherung außerdem die Geometrie und damit L_K fest voraus.

Wird η formal eliminiert, hängt seine Lösung über den retardierten Green-
Operator von früheren S-Werten UND den Anfangsdaten des η-Kanals ab.
So entsteht in der reduzierten Beschreibung ein Gedächtniskern. Im vollen
Zweifeldmodell gibt es keine willkürlich eingesetzte Verzögerung und keine
kostenlose Energie. Ein verlustfreier endlicher Graph hat diskrete Moden
und Rückkehrphänomene, keine automatisch irreversible Dämpfung.
Im Vakuum haben beide Kanäle in diesen Modelleinheiten Masse√2; eine große
Hierarchie ist damit noch nicht eingebaut oder hergeleitet.

## 6. Ereignisse statt Vergleich bewegter Mengen

Die alte Definition I(t−Δt)≠I(t) zählt schon kontinuierlich wandernde Punkte
als neue Ereignisse. Deshalb definieren wir IDs und Inzidenzen:

- Eine Kante ist geschnitten, wenn ihre Endpunkte auf verschiedenen Seiten
  einer Ebene liegen. Ein geometrischer Vertex-Tick ist eine transversale
  Nullstelle von g_i(t)=n(t)·x_i(t)−b(t).
- Zeitlokalisierung durch Nullstellensuche; gleichzeitige Ereignisse als
  Gruppe. Anzahl-Tick nur, wenn sich der gewählte Zähler ändert.
- Schnittkomponenten mit fortgeführten IDs; Aufspaltungen/Verschmelzungen
  sind eigene Ereignisse, nicht jeder Positionswechsel.

Für Ereigniszeiten t_e ist N(t)=Σ_e1[t_e≤t]. Die Ableitung ist ein Maß mit
Dirac-Spitzen. Eine endliche Rate benötigt ein explizites Fenster:

\[
\nu_\Delta(t)=\frac{N(t+\Delta/2)-N(t-\Delta/2)}{\Delta}.
\]

Δ ist eine Messauflösung, nicht die Integratorschrittweite. Raumlokale Raten
brauchen zusätzlich ein festgelegtes Messvolumen. Das Fenster Δ→0 liefert
bei einzelnen deterministischen Ereignissen keine glatte endliche Rate.

Eine vorgeschlagene Uhr \(d\tau=(\nu_\Delta/\nu_0)dt\) wäre zunächst nur
zählbasierte Zeit mit Referenzrateν0. Sie hängt von Detektor, Fenster und
Orientierung ab. Keine physikalische Eigenzeit ohne weiteren Invarianztest.

## 7. Messblinde Bewegung und endliche Detektoren

Für zentrale Ebenen und x_i=a(t)v_i, a>0, bleibt die Schnittpunktzahl N_cut konstant, aber
A(t)=a(t)²A(0). Beide Größen messen! Das wurde im Tetraeder-Folgelauf als
Messkontrolle bestätigt; gleichmäßiges Atmen ist dort keine einzelne Eigenmode.

Ein endlicher Detektor kann Offsetantwort w_δ(s) mit Integral1 besitzen:
\(A_δ(t)=\int w_δ(s)N_{cut}(t;s)ds\). Diese geglättete Punktzahl ist nicht notwendig
ganzzahlig und nicht die geometrische Schnittfläche A(t). Eindeutige Namen
im Code: point_count, section_area, smoothed_count.

Exakte Schnittpunktzahl als Energie ist generisch stückweise konstant und
springt bei Ereignissen. Ihre gewöhnliche Ableitung liefert keine reguläre
Kraft. Daher zunächst rein passive Messung. Eine physikalische Schnitt-
wechselwirkung verlangt eine eigene glatte, objektive Kontaktenergie oder
eine konsistente Stoßregel samt Energiebilanz. Keine passive Beobachtungsebene
in die autonome Energie schmuggeln.

## 8. Stabilität und Auswertung

Benutze reelle Koordinaten q=(x,Reψ,Imψ,χ). Bei obiger Konvention hat die
Massenmatrix Einträge m_i für x,2 für Reψ/Imψ und1 für χ. Am statischen
Gleichgewicht gilt H v=ω² M v. Symmetrien herausprojizieren; das Minimum
aller Eigenwerte ist sonst häufig die triviale Null.

Bei phasenrotierenden Lösungen ψ=e^{iωt}f ist das gewöhnliche Potential-
Hessian nicht der vollständige Stabilitätsoperator. Erforderlich sind die
Ladungsnebenbedingung und das gekoppelte lineare System im mitrotierenden
Rahmen, einschließlich gyroskopischer Terme. Periodische Bahnen zusätzlich
mit Floquet-Multiplikatoren prüfen. Endliche Lebensdauer ist kein Beweis
asymptotischer Stabilität; positive Lyapunov-Schätzung kann auch eine lokale
Instabilität statt stationären Chaos anzeigen.

Energieerhaltung: skalierter absoluter Fehler mit festgelegter positiver
Bezugsenergie, kein Quotient durch möglicherweise null werdendes E.
Korrelation corr(E,ν) ist bei konstantem E undefiniert: lokale Energien oder
vorab definierte Ensembles verschiedener Energien verwenden. Zensierte
Lebensdauern gesondert behandeln, N_I=0 nicht dividieren. Ereignis- und
zeitgewichtete Wahrscheinlichkeiten getrennt berichten.

## 9. Begrenzte Testfolge vor einem großen Sweep

1. Ein Knoten / zwei gekoppelte Knoten: Gradienten, Q und E; positive und
   absichtlich falsche Vorzeichenkontrolle. Keine Geometriebewegung.
2. Freie Geometrie mit ψ=0,χ=1: bereits geprüften Federketten-Grenzfall
   reproduzieren, keine neue komplette historische Rechnung nötig.
3. Geometrie fest, beide Felder dynamisch: Frequenzen und Antwort auf einen
   kleinen ψ-Dichtepuls; voller χ-Kanal gegen reduzierte Antwort vergleichen.
4. Erst dann J(r),K(r) aktivieren: Gegenseitige Arbeit und Gesamtenergie
   schließen; keine einseitige Kopplung.
5. Stationäre lokalisierte Kandidaten bei festem Q suchen; mit verteilten
   Zuständen und getrennten Verdichtungen vergleichen. Optimierung ist nicht
   Bildung. Bildung erst danach aus frei entwickelten Startpaketen testen.
6. Kandidaten mit dt/dt2/dt4, größeren Netzen, offenen/geschlossenen Rändern
   und endlicher Detektorbreite prüfen. Erst dann N- und Parameterstudien.

Dieser Plan ist noch nicht ausgeführt. Das v2-Modell ist neu; die früheren
BIC- und Q-Ball-Beweise werden nicht darauf übertragen.

## 10. Zehn prüfbare Anschlussideen

| Idee | Messgröße und Gegenprobe | Was sie entscheiden kann |
|---|---|---|
| 1. Verzögerung aus χ | Impulsantwort/Phasenlage voll vs eliminierter Kanal | Gedächtnis aus definierter Dynamik statt freier Delayparameter |
| 2. Innere Uhr vs Detektortakt | Gleicher Zustand, andere Ebene/δ/Δ | Detektorabhängigkeit widerlegt universelle Uhrdeutung |
| 3. Dunkle Messmode | point_count UND section_area UND Feldenergie | Messblindheit von physikalischer Ruhe trennen |
| 4. Energieaustausch zweier Kanäle | E_total konstant, Energieanteile gegenphasig | Konservativer Austausch; keine Energiequelle |
| 5. Selbstgestützter dichter Kern | χ-Absenkung, Q-Lokalisierung, Vergleich mit χ=1 | Nutzen der Rückkopplung gegen Gradientenkosten |
| 6. Resonantes Gedächtnis | Frequenzen √eig(L_K+2I), Anregung nahe/fern Resonanz | Dauer und Stärke der Nachwirkung; Randreflexionen kontrollieren |
| 7. Mechanische Rückwirkung | J'=K'=0 gegen variable Kopplung, Arbeit je Kanal | Wirkung darf nur im gekoppelten Arm auftreten |
| 8. Phasenfrustration im Ring | Energie vs Windung bei gleicher Q, Nachbar-N | Ganzzahlige Windung statt vorschneller Primzahldeutung |
| 9. Lokalisierung durch Defekt oder spontan | homogener Graph vs einzelner geänderter Parameter | Eingebaute Falle von selbstorganisiertem Kern trennen |
| 10. Kanalöffnung zerstört Stille | getrennte auslaufende Energieflüsse an großem/offenem Rand | Mehrkanalrobustheit; endlicher Reflexionskasten reicht nicht |

Bei jedem Test: vorher erwartetes positives und negatives Ergebnis, eine
Nullkontrolle und eine konkrete Größe, die scheitern kann. Kein großer
Sweep, bevor Wirkung, Bilanzen und Messdefinitionen geschlossen sind.
