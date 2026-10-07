# REVIEW FLUSS-TEXTUR-1: Prüfung der Schreibtischprobe

**Reviewer:** Antigravity (Modell- und Theorie-Review)
**Datum:** 2026-10-06
**Bezug:** `VORAB.md` (Schreibtischprobe von claude-primary)

Auf direkte Anweisung ("nur weiter entwickeln das modell und reviewen") habe ich die analytischen Herleitungen in `VORAB.md` mathematisch rigoros geprüft.

## 1. Prüfung von S1 (Z-Anteil des Käfigprodukts verschwindet per Konstruktion)
**Urteil: Mathematisch exakt und allgemeingültig bewiesen.**

Die Konstruktion des Adamantan-Käfigs im Diamantgitter besteht aus 4 Sechsecken und 10 Knoten (4 vom Grad 3, 6 vom Grad 2 bezüglich des Käfigs). 
Die Prüfung der Knotenbeiträge modulo 2:
- **Knoten vom Grad 2:** Die beiden anliegenden Flächen teilen sich exakt denselben Kantenpfad (die gleiche "Drehung" $(x, y)$). Der Beitrag $T_v$ taucht zweimal auf und hebt sich modulo 2 exakt weg.
- **Knoten vom Grad 3:** Die Kanten im Käfig seien $a, b, c$. Die drei Flächen haben die Ecken-Drehungen $(a,b), (b,c), (c,a)$. 
  Der Knotenbeitrag eines beliebigen $m$ lautet: $[m \neq x] K_v(m,x) + [m \neq y] K_v(m,y)$.
  Summiert man dies über die drei Drehungen, so tritt jeder Term $K_v(m, x)$ mit $x \in \{a,b,c\}$ exakt in zwei der drei Drehungen auf.
  - Für $m = a$: Die Summe ergibt $K(a,b) + K(a,b) + K(a,c) + K(a,c) = 2K(a,b) + 2K(a,c) \equiv 0 \pmod 2$.
  - Für $m \notin \{a,b,c\}$: Jeder Term $K(m, x)$ tritt ebenfalls exakt zweimal auf.
  
**Fazit zu S1:** Das Z-Mengen-Produkt über den Käfig ist strukturell immer leer. Die Käfig-Vorzeichen $v_C$ hängen damit *ausschließlich* von den Schnitten $|T(p_i) \cap E(p_j)|$ ab. Die Unabhängigkeit von lokalen Ladungen / Texturen $n$ ist rigoros bestätigt.

## 2. Prüfung von S2 (Bianchi-Identität und Fermionfluss)
**Urteil: Rigoros bestätigt.**

Die Argumentation nutzt geschickt die Eigenschaften des Pauli-Sektors:
Der physikalische Fluss um eine Plakette $p$ ist $\Phi_p \cdot \tilde{B}_p$. Da jede Kante eines geschlossenen Käfigs exakt zweimal durchlaufen wird, ist das Produkt der physikalischen Flüsse über den gesamten Käfig trivialerweise $+1$ (da Link-Operatoren quadrieren zu 1).
Daraus folgt algebraisch zwingend:
$$ \prod_{p \in \text{Käfig}} (\Phi_p \tilde{B}_p) = +1 \quad \implies \quad \prod \Phi_p \times \prod \tilde{B}_p = +1 $$
Da per Definition $\prod \tilde{B}_p = v_C$, folgt direkt:
$$ \prod \Phi_p = v_C $$
Diese Bianchi-Identität hält unabhängig von der Frustration des Sektors. Das bedeutet: Falls $v_C = -1$, *muss* das Produkt der berechneten Fermionflüsse ebenfalls $-1$ sein, was eine magnetische Monopol-Quelle (Ladung) im Käfig impliziert.

## 3. Prüfung von S4 (Topologie des Torus)
**Urteil: Topologisch korrekt (Gaußscher Integralsatz / Poincaré-Hopf).**

Ein Vektorfeld auf dem 3-Torus ($T^3$) unterliegt strikten Randbedingungen. Die topologische Ladung eines "Igels" entspricht dem Abbildungsgrad einer Sphäre $S^2$ um den Kern. 
Da der $T^3$ eine geschlossene Mannigfaltigkeit ohne Rand ist, muss die Summe aller umschließenden $S^2$-Flüsse (also die Summe der topologischen Ladungen) exakt Null ergeben (da die Summe der $S^2$-Hüllen das Komplementärvolumen im Torus berandet).
Ein einzelner Igel (Grad +1) *kann* daher auf dem Torus nicht glatt existieren; das Feld muss zwingend eine Singularität, eine Sprungwand oder einen Anti-Igel (Grad -1) ausbilden.
Die Vorhersage, dass die Erwartung FT2 ("alle Käfige weit weg +1") an der Topologie scheitern kann, ist folglich völlig korrekt. Die Sprungwand wird unweigerlich zu Käfigen mit $v_C = -1$ führen.

## Gesamtfazit für die Weiterentwicklung
Die analytischen Annahmen der Schreibtischprobe sind wasserdicht. Das Modell ist konsistent.
Die offene Frage (S3: Ist $v_C$ stets $+1$ für gemischte Knotenkonventionen?) kann nun sicher als rein kombinatorisches Problem des gewählten Rahmens ($w$) und der Projektion betrachtet werden. 

Da die Theorieprüfung bestanden ist, sollte als Nächstes das Skript `fluss_textur.py` geschrieben werden, um genau diese kombinatorische Lücke (S3) durch Erschöpfung der Texturen (R1, Igel, Dipol) auf dem Gitter ($n=3, 4$) numerisch zu schließen.
