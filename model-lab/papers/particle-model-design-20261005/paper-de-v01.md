# Ein geometrisches Feldmodell für lokalisierte Teilchenzustände

## Entwurf einer gemeinsamen Dynamik mit offenen Nachweisen

**Finn Malte Hinrichsen, Hamburg**  
Arbeitsfassung 0.1 · 5. Oktober 2026

### Zusammenfassung

Wir entwerfen ein Teilchenmodell, in dem lokalisierte Materiezustände, elektromagnetische Wellen und dynamische Geometrie auf einer gemeinsamen simplicialen Raumzeit beschrieben werden. Ausgangspunkt ist eine Wirkung mit geometrischem, elektromagnetischem und komplexem skalarem Sektor. Teilchen sollen als lokalisierte Anregungen oder gebundene Zustände dieser Dynamik identifiziert werden. Innere Schwingungen, Phasenrotationen und räumliche Texturen liefern mögliche Freiheitsgrade; ihre Zuordnung zu Masse, Spin und Ladung wird durch getrennte Nachweise festgelegt. Vorliegende Projektrechnungen stützen einzelne Bausteine: lokalisierte skalare Zustände, eine im langwelligen Grenzfall konsistente gemeinsame Uhr für Licht und geometrische Wellen sowie stark verringerte Energiefehler bei ausgewählten Netzumbauten, wenn die Trägheit aus der vierdimensionalen Wirkung gewonnen wird. Diese Befunde ergeben noch keine vollständige Teilchentheorie. Insbesondere fehlen ein abgeschlossener nichtlinearer Zwangsformalismus, kontrollierter Energietransfer bei dynamischen Umbauten, ein quantisiertes Teilchenspektrum, Fermionenstatistik und eine Herleitung nichtabelscher Ladungen. Der Beitrag formuliert eine zusammenhängende Modellarchitektur und eine Folge unterscheidender Prüfungen, an denen sie scheitern kann.

## 1. Ziel und Gegenstand

Die Leitfrage lautet: Kann eine gemeinsame lokale Dynamik von Geometrie und Feldern sowohl langlebige lokalisierte Objekte als auch ihre Wechselwirkungen hervorbringen? Ein geeignetes Modell muss erklären, warum manche Anregungen frei propagieren, andere räumlich gebunden bleiben und wieder andere nur als Bestandteile eines Verbunds auftreten. Es muss außerdem festlegen, welche Eigenschaften beim Zusammenstoß, bei Bindung und bei Zerfall erhalten bleiben.

Wir verfolgen diesen Ansatz als Konstruktion eines effektiven Teilchenmodells. Die Tetraeder der räumlichen Diskretisierung werden zunächst als geometrische Bausteine behandelt, nicht als bereits identifizierte Elementarteilchen. Ebenso ist ein lokalisierter Feldklumpen zunächst ein klassischer Zustand. Erst ein quantisiertes Spektrum, definierte Streukanäle und eine Messabbildung können daraus eine Zuordnung zu beobachteten Teilchen begründen.

Das Modell hat zwei mögliche physikalische Lesarten. In der ersten ist das Netz eine Diskretisierung einer kontinuierlichen Theorie; Aussagen müssen beim Verfeinern konvergieren. In der zweiten ist eine endliche Netzskala physikalisch. Dann sind Dispersion, Richtungsabhängigkeit und bevorzugte Zeitstruktur messbare Konsequenzen. Beide Lesarten werden getrennt geprüft. Eine erfolgreiche Kontinuumsnäherung belegt keine fundamentale Körnigkeit des Raums.

## 2. Zustandsraum und gemeinsame Wirkung

### 2.1 Geometrie und Felder

Eine räumliche Schicht besteht aus einem ausgefüllten Tetraedernetz. Kantenlängen beschreiben seine intrinsische Geometrie. Durch lokale Fortschreibung von Ecken entstehen vierdimensionale Simplizes zwischen benachbarten Schichten. Die zeitlichen Verbindungen dienen als gemeinsamer geometrischer Zeitmaßstab.

Zum minimalen Zustand gehören:

| Bestandteil | Variable | Vorgesehene Funktion |
|---|---|---|
| Geometrie | Kantenlängen und Triangulierung | Abstände, Krümmung und geometrische Wellen |
| Elektromagnetischer Sektor | diskrete Einsform A auf Kanten | abelsche Wellen und gegebenenfalls elektrische Kopplung |
| Materiesektor | komplexes Feld φ auf Ecken | lokalisierte Zustände mit globaler Phasenladung |
| Erweiterung | weitere Felder oder Orientierungen | nur bei konkret nachgewiesenem Bedarf |

Mehrere Feldkomponenten sind keine zusätzlichen Raumdimensionen. Auch eine innere Phase ist keine weitere geometrische Koordinate. Diese Unterscheidung gilt für sämtliche vorgeschlagenen Erweiterungen.

### 2.2 Wirkungsansatz

Die Architektur lautet

\[
S[\ell,A,\phi]=S_{\mathrm{geom}}[\ell]+S_{\mathrm{em}}[\ell,A]+S_{\mathrm{mat}}[\ell,\phi].
\]

Der geometrische Anteil folgt dem Regge-Ansatz: Krümmung wird über Dreiecksflächen und zugehörige Fehlwinkel erfasst. Der elektromagnetische Anteil verwendet die diskrete Feldstärke F=dA und geometrieabhängige Hodge- beziehungsweise Whitney-Matrizen. Für den komplexen Skalar dient als Kontinuumsziel bei Signatur (−,+,+,+)

\[
S_{\mathrm{mat}}=\int d^4x\sqrt{-g}\left[-g^{\mu\nu}\partial_\mu\phi^*\partial_\nu\phi-U(|\phi|^2)\right],
\qquad U(S)=m^2S-\lambda S^2+\beta S^3.
\]

Die bisher häufig untersuchte dimensionslose Wahl ist m²=λ=1 und β=1/2. Diese Parameter sind Modellannahmen, keine aus Beobachtungen bestimmten Naturkonstanten.

Die Summe der drei Sektoren ist das Designziel. Dass einzelne Module schon auf derselben Geometrie rechnen, ersetzt weder eine vollständig implementierte gekoppelte Variation noch ihre dynamische Prüfung. Gegenwärtige geometrische Rechnungen verwenden insbesondere eine euklidische Ausgangswirkung und eine formale Fortsetzung zur Zeitentwicklung. Eine kontrollierte lorentzsche Formulierung bleibt erforderlich.

### 2.3 Globale und elektrische Ladung

Der minimale Skalar besitzt eine globale U(1)-Symmetrie. Für einen stationären Ansatz φ=f(x)e^{iωt} ist in der verwendeten Normierung

\[
Q=2\omega\int f^2\,d^3x.
\]

Diese Ladung ist zunächst eine interne Erhaltungsgröße. Sie wird nicht mit elektrischer Ladung gleichgesetzt. Dazu müsste der Skalar explizit durch Dμφ=(∂μ−ieAμ)φ an das Eichfeld gekoppelt werden. Diese Erweiterung verändert Energie, Randbedingungen und mögliche gebundene Lösungen; vorhandene Ergebnisse des globalen Modells dürfen nicht unverändert übernommen werden.

### 2.4 Vollständiger derzeit dokumentierter Formelaufbau nach Claude

Maßgeblich ist Claudes Grundgleichung Fassung 3 vom 5. Oktober 2026. Sie ersetzt die zuvor gesetzte geometrische Trägheit und den separaten gemeinsamen Zeitfaktor durch die 4D-Wirkung. Die expliziten neutralen Materieterme werden ergänzend aus Fassung 2.5 übernommen. Diese Darstellung umfasst alle dort benannten Sektoren; sie behauptet keine bereits geschlossene nichtlineare Theorie. Insbesondere sind die folgenden ausgeschriebenen geometrischen Ausdrücke eine deklarierte Notationskonvention, kein Nachweis ihrer vollständigen Codeimplementierung.

**Vierdimensionale Ausgangsform.** Mit Dreiecken τ, 4-Simplizes σ, Flächen Aτ, Fehlwinkeln ετ und Volumina Vσ schreiben wir den Regge-Baustein in der Konvention der Einstein-Hilbert-Wirkung schematisch als

\[
S_{\rm geom}=\frac{1}{8\pi G}\left(\sum_{\tau\subset\mathrm{int}\mathcal T_4}A_\tau\epsilon_\tau-\Lambda\sum_{\sigma\in\mathcal T_4}V_\sigma\right)+S_{\partial}.
\tag{1}
\]

Der Randterm S∂ hängt von den gewählten Randdaten ab. Lorentzsche Winkel, kausale Simplextypen und die Fortsetzung der euklidischen Rechenkonvention sind gesondert festzulegen. Ohne diese Angaben ist (1) ein Wirkungsansatz, keine vollständige lorentzsche Implementierung.

Der elektromagnetische und skalare euklidische Baustein lassen sich in einer kompatiblen Normalisierung so ausdrücken:

\[
F=d_1A,\qquad S_{{\rm em},E}=\frac12 F^T\star^{(4)}_2F,
\qquad S_{{\rm mat},E}=(d_0\phi)^\dagger\star^{(4)}_1(d_0\phi)+\sum_v V^{(4)}_v U(|\phi_v|^2).
\tag{2}
\]

Hier sind d₀ und d₁ orientierte Inzidenzmatrizen mit d₁d₀=0. Die Hodge-Matrizen hängen von der Geometrie ab. Whitney-Matrizen sind im Allgemeinen nicht diagonal; Vᵥ⁽⁴⁾ bezeichnet hier ausdrücklich eine gewählte diagonale Volumenquadratur für den Potentialterm. Die genaue Wahl von Quadratur, Dual und Gewichtung gehört zur Modelldefinition und muss vor einem gekoppelten Lauf gebunden werden. Insbesondere ist eine räumliche Hodge-Matrix nicht mit ihrem 4D-Gegenstück austauschbar.

**Kanonische Zielstruktur.** Auf einer räumlichen Schicht seien qₑ=ℓₑ² und pᵉ ein geometrisches kanonisches Paar. Für Maxwell heißen die Paare Aₑ und Eᵉ, für den komplexen Skalar φᵥ und πᵥ. Die projektseitige Phasenraumkonvention lautet

\[
S_{\rm can}=\int dt\left[\sum_e p^e\dot q_e+\sum_e E^e\dot A_e+\sum_v(\pi_v\dot\phi_v+\pi_v^*\dot\phi_v^*)-H_{\rm tot}\right],
\tag{3}
\]

\[
H_{\rm tot}=\sum_v N_v\mathcal H_v+\sum_v\boldsymbol s_v\!\cdot\!\boldsymbol{\mathcal D}_v+\sum_v A_{0v}\mathcal G_v,
\quad \mathcal G_v=(d_0^TE)_v-\rho_v.
\tag{4}
\]

N bezeichnet Lapse, s Shift und A₀ den elektrischen Multiplikator. Im neutralen Arm ist ρᵥ=0. Die vollständige nichtlineare Form von Dᵥ und der Abschluss der Zwangsalgebra sind im dokumentierten Stand offen. Eine lineare Lapse-Abhängigkeit allein beweist nicht, dass sämtliche Bedingungen erster Klasse sind. Die Form (4) ist daher außerhalb des geprüften linearen Grenzfalls eine Anforderung.

**Ausgeschriebene Materie- und Lichtenergie.** Für die räumliche diagonale DEC-Variante und verschwindenden Shift sind die in der Vorgängerfassung dokumentierten Terme

\[
H_\phi=\sum_v N_v\left[\frac{|\pi_v|^2}{Z_t\star_{0v}}+\star_{0v}U(|\phi_v|^2)\right]+\sum_{e=(a,b)}N_eZ_s\star_{1e}|\phi_a-\phi_b|^2,
\tag{5}
\]

\[
H_{\rm em}=\frac12\sum_eN_e\frac{(E^e)^2}{\star_{1e}}+\frac12\sum_fN_f\star_{2f}(d_1A)_f^2.
\tag{6}
\]

Dabei ist πᵥ=Zₜ⋆₀ᵥ\dot φᵥ* bei N=1. Für die skalaren Formeln in Abschnitten 2.2, 2.3 und 3.1 setzen wir ausdrücklich Zₜ=Zₛ=1; allein Zₛ/Zₜ=1 würde nur das Geschwindigkeitsverhältnis festlegen. Bei allgemeinem Zₜ lautet die stationäre klassische Ladung Q=2ZₜωI und der Festladungs-Zeitanteil Q²/(4ZₜI). Die zusätzliche Quanten-Wirkungsnormierung ζ in Abschnitt 4.4 wird nicht mit Zₜ gleichgesetzt. Kanten- und Flächen-Lapse werden in dieser räumlichen Form aus den Eckwerten interpoliert. Der 4D-Whitney-Arm muss stattdessen mit seinen assemblierten Matrizen behandelt werden; die Quotienten in (6) sind keine Formel für eine beliebige nichtdiagonale Matrix. Bei verschwindenden oder negativen Gewichten ist die angegebene positive elektrische Energie nicht ohne Weiteres definiert.

**Geometrische Trägheit aus der Wirkung.** Sei K₄ der quadratische Operator der linearisierten 4D-Wirkung, aufgeteilt in beibehaltene Variablen u und eliminierte Gittervariablen z. Soweit Kzz invertierbar ist, gilt

\[
K_{\rm eff}(w)=K_{uu}(w)-K_{uz}(w)K_{zz}(w)^{-1}K_{zu}(w),
\qquad K_{\rm eff}(w)=K_0+wK_1+w^2K_2+\cdots.
\tag{7}
\]

Die Entwicklung (7) verlangt eine reguläre Kleinfrequenzumgebung ohne Pol des eliminierten Blocks; an einem Schur-Pol ist sie nicht anwendbar. Der Rechenbericht verwendet die Fortsetzung w=iω. Der geometrische K₂-Block wird in dessen euklidischer Expansion als M_eff ausgewertet; nach der Fortsetzung wechselt der quadratische Frequenzterm sein Vorzeichen. Die dortigen Störvariablen sind lineare Metrikanteile; ihr Bezug zu δq muss vor einer Verwendung in (3) explizit transformiert werden. Für einen linearen Koordinatenwechsel ξ=Tδq lautet die zugehörige kinetische Matrix in q-Koordinaten TᵀM_effT.

Die frequenzabhängige Elimination kann zeitlich nichtlokal sein. K₂ beschreibt nur die lokale Zeitkinetik der hier verwendeten niederfrequenten Ableitungsnäherung, nicht den vollständigen effektiven Operator. Der Fundort der Fortsetzungskonvention ist der Methodenkopf von `ueberleitung-v-1/ERGEBNIS.md` (Absatz „Alles synthetische, linearisierte Gitterrechnung“).

Schreibt man diese Matrix als Mq und den Impulsunterraum als p=Πp_red, so ist die in der Umbauprobe verwendete inverse kinetische Form

\[
H_{\rm kin,red}=\frac12p_{\rm red}^T A_{\rm red}p_{\rm red},
\qquad A_{\rm red}=\Pi^TM_q^{-1}\Pi.
\tag{8}
\]

Gleichung (8) setzt die Invertierbarkeit von Mq auf dem angegebenen Raum voraus. Die Einschränkung p=Πp_red allein beweist noch nicht, dass p_red ein kanonischer Impuls ist: Dafür müssen auch die konjugierten reduzierten Koordinaten und die reduzierte symplektische Form festgelegt werden. Die Reduktion und die Inversion dürfen nicht still vertauscht werden: (ΠᵀMqΠ)⁻¹ ist im Allgemeinen eine andere Matrix. Ob die gewählte Reduktion die vollständige Dynamik mit Zwangsbedingungen am Umbau repräsentiert, gehört zu den offenen Nachweisen.

Für den räumlichen Krümmungsanteil bei konstantem N=1 ist die dokumentierte ADM-Vorzeichenkonvention

\[
H_{\rm curv}=-\frac{1}{8\pi G}\sum_e\ell_e\epsilon_e+\frac{\Lambda}{8\pi G}\sum_tV_t.
\tag{9}
\]

Bei ortsabhängigem Lapse treten zusätzliche Beiträge durch die Variation der gewichteten Fehlwinkel auf. Sie dürfen bei der Ableitung von Kräften nicht weggelassen werden. Die alte Summe gesetzter lokaler kinetischer Inversen wird durch (7)–(8) nicht nochmals addiert.

**Dynamik und Kopplung.** Soweit die kanonische Form definiert ist, folgen alle Evolutionsgleichungen aus

\[
\dot q_e=\frac{\partial H_{\rm tot}}{\partial p^e},\quad
\dot p^e=-\frac{\partial H_{\rm tot}}{\partial q_e},\quad
\dot A_e=\frac{\partial H_{\rm tot}}{\partial E^e},\quad
\dot E^e=-\frac{\partial H_{\rm tot}}{\partial A_e},\quad
\dot\phi_v=\frac{\partial H_{\rm tot}}{\partial\pi_v},\quad
\dot\pi_v=-\frac{\partial H_{\rm tot}}{\partial\phi_v},
\tag{10}
\]

ergänzt um die komplex konjugierten Gleichungen und die Multiplikatorbedingungen. Der Rückstoß der Materie auf die Geometrie ist insbesondere −∂(Hφ+Hem)/∂qₑ bei festgehaltenen kanonischen Variablen. Damit muss auch die Variation sämtlicher geometrischer Gewichte eingehen.

Für feste Geometrie, N=1 und Shift null reduziert sich der neutrale Skalar zu

\[
Z_t\star_0\ddot\phi=-Z_s d_0^T\star_1d_0\phi-\star_0U'(|\phi|^2)\phi,
\qquad U'(S)=m^2-2\lambda S+3\beta S^2.
\tag{11}
\]

Bei zeitabhängiger Geometrie lautet der linke Ausdruck stattdessen ∂t(Zₜ⋆₀\dot φ), soweit dieselben Zeit- und Shiftannahmen gelten. Der alte projektinterne Operator 8d₀ᵀ⋆₁d₀ ist eine frühere Zeitnormierung; der Faktor 8 wird in Fassung 3 nicht zusätzlich nur in einen Sektor eingesetzt. Die gemeinsame Uhr folgt dort aus denselben zeitlichen Geometrieverbindungen.

**Übergabe und Randbedingungen.** Die Formel benötigt zusätzlich eine Regel, wenn sich die Triangulierung ändert. Im bisher geprüften P-Verfahren behalten gemeinsame Kanten ihre Impulse, die neue Kante erhält zunächst p_neu=0; danach wird projiziert. Gauss-Bedingung, Ladung, Symplektik und Energie müssen dabei getrennt geprüft werden. Die Periodizität der numerischen Box ist keine bereits bewiesene kosmologische Randbedingung. Insbesondere wird eine maximale Scheibung K=0 nicht ohne Prüfung als allgemeine nichtlineare Regel für einen geschlossenen Raum mit Materie übernommen.

Damit stehen der gesamte dokumentierte Formelaufbau und seine noch fehlenden Definitionen im Manuskript. Eine abgeschlossene Teilchentheorie würde darüber hinaus die bislang offenen Operatoren, Randterme, Reduktionen und Übergaberegeln eindeutig liefern müssen.

## 3. Teilchen als Zustände der Dynamik

### 3.1 Lokalisierter Träger

Als erster Kandidat dient ein räumlich lokalisierter, zeitlich phasenrotierender Skalarzustand. Seine zeitunabhängige Energiedichte kann mit einer nichttrivialen inneren Dynamik koexistieren. Die Phase ist jedoch nur dann eine auslesbare Uhr, wenn eine konkrete relative Phasenmessung oder Kopplung angegeben wird. Eine freie globale Phase ist noch kein beobachtbarer Takt.

Die Festladungsreduktion lautet für I[f]=∫f²d³x

\[
E_Q[f]=\frac{Q^2}{4I[f]}+\int\left(|\nabla f|^2+U(f^2)\right)d^3x.
\]

Ein stationärer Punkt dieses Funktionals liefert einen Hintergrundkandidaten. Für einen Teilchenträger verlangen wir zusätzlich: Existenz unter kontrollierten Randbedingungen, Stabilität gegen relevante Störungen, eine definierte Energie-Impuls-Beziehung und reproduzierbare Wechselwirkungen. Ein Minimum innerhalb eines radialen Ansatzes reicht dafür nicht aus.

### 3.2 Innere Moden und Strahlung

Lineare Störungen um einen Träger können radiale, winkelabhängige und gemischte Feldmoden bilden. Sie beschreiben mögliche innere Anregungen. Projektbefunde zu stillen Moden motivieren die Hypothese, dass bestimmte Anregungen wegen verschwindender Kopplung an einen offenen Strahlungskanal besonders langlebig sind.

Eine solche Nullstelle bedeutet nicht, dass das ganze Objekt bewegungslos oder energetisch abgeschlossen ist. Höhere Harmonische, zusätzliche Felder, nichtlineare Prozesse und äußere Störungen können andere Abstrahlungskanäle öffnen. Für das Teilchenmodell ist deshalb die gesamte Zerfallsrate relevant, nicht allein eine lineare Kanalnullstelle. Die Zertifikate und Grenzen des gesonderten Modenpapers werden hier nicht erneut bewiesen.

### 3.3 Verbünde

Ein Verbund ist energetisch gebunden, wenn seine Energie bei denselben Gesamtladungen und Erhaltungsgrößen unter allen relevanten Zerfallsschwellen liegt:

\[
E_{\mathrm{Verbund}}(Q,J,\ldots)<\min_{\mathrm{zulässige\ Zerfälle}}\sum_a E_a.
\]

Das ist eine notwendige Vergleichsprüfung für energetische Bindung, noch kein vollständiger dynamischer Stabilitätssatz. Mögliche Konkurrenten sind getrennte Kerne, ein verschmolzener Kern, ringförmige Zustände und Strahlung. Eine anziehende Kraft allein kann auch nur Verschmelzung bewirken.

Unsere mechanischen und hybriden Tetraedermodelle zeigen, wie innere Formfreiheitsgrade geprüft werden können. Ihre vorgegebenen Bindungsterme gehören jedoch nicht automatisch zur gemeinsamen geometrischen Feldwirkung. Eine lokale stabile Folgeform dieses Hilfsmodells wird deshalb nicht als Teilchenbefund des neuen Modells gezählt.

Ein begrenzter Vergleich liegt für das statisch feldeliminierte dreidimensionale Vierquellenmodell vor: Bei vier geprüften Quellenbreiten koexistieren reguläre und verformte lokale Minima. Eine analytische Abschätzung aller asymptotischen Fragmentpartitionen liefert in dessen eigenen Einheiten eine Trennschwelle von mindestens −3,602; die numerisch bestimmten Kandidatenenergien liegen unter −4. Ein expliziter Testtetraeder hat ebenfalls analytisch Energie unter −4. Zusammen mit Stetigkeit und Kompaktheit minimierender Folgen modulo Translation folgt für jede feste Quellenbreite zwischen 0,55 und 0,75 die Existenz eines kollisionsfreien globalen statischen Minimums. Seine Form ist damit nicht bestimmt. Die Argumente setzen vier Quellen und ihre Breiten voraus; sie erklären keine Entstehung von Teilchen und beweisen keine Stabilität der vollständigen Feldwirkung. Herleitung, numerische Daten und getrennte Nichtautor-Lektüren stehen unter `coordination/particle-lenia-review-20261004/shape-competition/branch-width/`.

Für zwei explizit durch Dezimaldaten festgelegte Verbindungspfade zwischen den numerisch gefundenen Formen lässt sich außerdem die gesamte statische Pfadenergie unter −3,99996 begrenzen. Die endlichen Voraussetzungen der analytischen Schranke wurden mit Intervallarithmetik eingeschlossen und unabhängig gelesen. Damit liegen diese geometrischen Wege durchgehend unter der Fragmentationsschwelle. Das belegt weder exakt stationäre Endpunkte noch eine minimale Formbarriere oder eine tatsächlich ablaufende Zeitentwicklung. Es trennt aber zwei Anforderungen: Ein Verbund kann energetisch gegen vollständige Trennung geschützt sein, ohne auf eine einzige Form festgelegt zu sein. Die Aussage betrifft ausschließlich das Vierquellen-Hilfsmodell; Belege stehen unter `shape-competition/transition-path/` im oben genannten Projektpfad.

Eine weitere Grenze betrifft die dynamische Feldanbindung dieses Hilfsmodells. Für endlich viele verschiedene Zentren mit identischen starren Gaußprofilen, festen nichtverschwindenden reellen Quellenladungen und einem freien homogenen massiven Skalarfeld kann eine nichttriviale lineare Verschiebungsschwingung in drei Raumdimensionen oberhalb der Feldschwelle nicht exakt strahlungsfrei sein. Der gemeinsame Gaußfaktor lässt sich aus der Fernamplitude kürzen; das verbleibende Punktdipolproblem hat nach dem Rellich- und Singularitätsargument keine nichttriviale Quelle mit verschwindendem Fernfeld. Unterhalb der Schwelle liegende Moden und sehr schwache Abstrahlung bleiben möglich. Die entsprechende Aussage trägt auch in zwei Raumdimensionen; in einer Dimension können bereits die zwei Abstrahlrichtungen gleichzeitig ausgelöscht werden, ohne dass damit eine freie Eigenmode konstruiert wäre. Diese Grenze gilt für den starren Quellenansatz, nicht für Q-Bälle mit veränderlichem Feldhintergrund. Herleitung und Prüfbericht: `coordination/particle-lenia-review-20261004/GAUSSIAN-DIPOLE-NO-GO.txt` und `GAUSSIAN-DIPOLE-REVIEW.txt`.

## 4. Masse, Spin und Ladungen als Nachweisaufgaben

### 4.1 Masse

Die Ruheenergie eines lokalisierten Zustands ist ein erster Massenskalenkandidat. Träge Masse wird dagegen über seine Impulsabhängigkeit oder seine Antwort auf eine schwache äußere Kraft bestimmt. Aktive gravitative Masse beschreibt die erzeugte Ferngeometrie; passive gravitative Masse die Antwort auf ein äußeres Gravitationsfeld.

Das Design verlangt, diese Größen aus derselben Wirkung zu gewinnen. Werden Energiedichte und gravitative Quelle bereits identifiziert, ist die Wiedergewinnung von M=E aus dem Fernfeld zunächst eine Konsistenzkontrolle. Ein unabhängiger Vergleich benötigt zusätzlich die Bewegungs- und Fallantwort eines gebundenen Zustands einschließlich seiner Feldenergie.

### 4.2 Spin

Klassischer Bahndrehimpuls, zirkulierende Formmoden und ein Zweimoden-Pseudospin sind verschiedene Größen. Keine davon begründet allein Spin ½. Dafür muss die quantisierte Zustandsstruktur eine entsprechende Rotationsdarstellung tragen; Fermionenstatistik verlangt einen weiteren konsistenten Nachweis.

Das unveränderte komplexe Skalarfeld wird nicht durch die Benennung einer inneren Rotation zu einem Fermion. Ein möglicher Erweiterungsweg verwendet topologische oder gerahmte Defekte. Dafür wären jedoch ein geeigneter Konfigurationsraum, endliche stabile Träger und eine zulässige Quantisierung explizit anzugeben. Wachsende numerische Obergrenzen für Entknotungsbarrieren beweisen keinen topologischen Schutz.

### 4.3 Farbladung und Quarks

Drei Raumrichtungen, drei Phasen oder ein dreifach entartetes Schwingungsniveau sind keine Herleitung der lokalen SU(3)-Eichsymmetrie. Eine räumliche Rotation verändert zudem keine beobachtbare Farbladung in der behaupteten einfachen Weise.

Ein Quarkanschluss benötigt mindestens eine definierte innere SU(3)-Darstellung, lokale Eichkopplung mit acht Generatoren, korrekte Spin- und elektrische Quantenzahlen sowie eine Dynamik, die farbige Einzelzustände und farbneutrale Verbünde unterscheidet. Das Minimalmodell enthält diesen Sektor nicht. Er ist eine zu begründende Erweiterung, kein Resultat der bisherigen Geometrie.

### 4.4 Wirkungsnormierung und quantisierte Ladungssektoren

Die dimensionslose klassische Feldgleichung bestimmt nicht die Stärke der Quantenfluktuationen. Multipliziert man die gesamte klassische Wirkung mit einer Konstanten, bleiben ihre stationären Gleichungen gleich, während sich ihre Gewichtung im Pfadintegral ändert. Für den Anschluss an ein Quantenteilchenspektrum muss deshalb eine zusätzliche Normierung gebunden werden.

Als explizite Konvention sei

\[
\frac{S_{\rm phys}}{\hbar}=\frac{1}{\zeta}S_{\rm dim},\qquad \zeta>0.
\tag{12}
\]

Bei einer kompakt normierten globalen U(1)-Phase mit elementarer Ladungseinheit eins entspricht der klassische Noetherwert in dieser Konvention dem dimensionslosen physikalischen Generator Q_dim/ζ. Erst im quantisierten Ladungseigenzustand wird dessen Eigenwert als ganzzahliges n bezeichnet. Für das semiklassische Matching gilt daher

\[
Q_{\rm dim}=\zeta n,\qquad
\frac{E_{\rm phys}}{m}=\frac{E_{\rm dim}}{\zeta}\quad(\hbar=c=1),
\tag{13}
\]

wobei m die für die Entdimensionierung gewählte Massenskala ist, nicht automatisch die renormierte Einteilchenmasse. Eine klassische Lösung trägt dadurch noch keine exakt bestimmte quantisierte Ladung. Ebenso liefert (13) keine Fluktuationskorrekturen und keine quantenmechanische Bindungsenergie.

Ein Vergleich eines quantisierten Sektors n mit einer klassischen Familie muss folglich E_dim(Q_dim=ζn)/ζ verwenden. Die direkte Gegenüberstellung mit E_dim(Q_dim=n) setzt ζ=1 voraus. Ein semiklassischer Grenzfall bei kleinem ζ und festem klassischen Profil entspricht dagegen großen n; er ist nicht automatisch ein kontrollierter Vergleich für n=1, 2 oder 3.

Die kanonische Ausarbeitung auf einem festen räumlichen Gitter liegt inzwischen als eigener Arbeitsentwurf vor: ein skalarer Hamiltonoperator, ganzzahlige Ladungssektoren und die kollektive Phasenquantisierung. Ein stationärer klassischer Ast ist dabei nicht automatisch der Grundzustand seines quantisierten Ladungssektors. Quantisierte Massen, Bindungsenergien und Lebensdauern wurden in dieser Ausarbeitung nicht berechnet. Die gemeinsame Normierung mit dem dynamischen geometrischen und elektromagnetischen Sektor sowie die tatsächliche HMC-Konvention müssen vor einem Zahlenvergleich ausdrücklich abgeglichen werden.

### 4.5 Freie Kontrolle vor einer quantisierten Bindungsaussage

Eine niedrige aus einem Korrelator angepasste Energie ist erst nach passenden Nullkontrollen als Bindung interpretierbar. Für ein freies, zentriertes komplexes Gaußfeld mit ungebrochener U(1)-Symmetrie und derselben linear verschmierten Feldvariable Φ_s gilt für O_n=Φ_s^n/√(n!) durch Wick-Kontraktion

\[
C_n(t)=\langle O_n(t)O_n^\dagger(0)\rangle=G_s(t)^n,
\qquad G_s(t)=\langle\Phi_s(t)\Phi_s^*(0)\rangle.
\tag{14}
\]

Wenn ein einzelner freier Modenbeitrag auf einer periodischen euklidischen Zeitachse der Länge T dominiert, ist G_s(t)=a[e^{-Et}+e^{-E(T-t)}]. Damit folgt

\[
C_n(t)=a^n\sum_{j=0}^n\binom nj e^{-E[(n-j)t+j(T-t)]}.
\tag{15}
\]

Bereits bei n=2 enthält dies einen zeitunabhängigen Kreuzterm. Ein einzelner cosh-Ansatz mit Energie nE ist deshalb bei endlichem T im Allgemeinen nicht die korrekte freie Vergleichsfunktion. Ohne Zeitvolumenprüfung und passende Fitfenster könnte ein solcher Ansatz eine scheinbare Bindungsenergie erzeugen. Bei mehreren freien Moden bleibt (14) richtig, während die Einmodenform von (15) durch die entsprechende Modensumme zu ersetzen ist.

Diese analytische Kontrolle wurde von ag-phy-lat als Methodenhinweis eingebracht und hier ausgeschrieben. Sie ist kein Befund über den Ausgang der laufenden HMC-Rechnung. Vor einer Teilchenzuordnung verlangen wir eine freie Wick-Kontrolle, Autokorrelations- und Zeitvolumenprüfung sowie den Vergleich gleicher Ladungssektoren in der gebundenen Wirkungsnormierung.

## 5. Bisherige numerische Anhaltspunkte

Die folgenden Zahlen stammen aus explorativen Projektberichten vom 5. Oktober 2026. Sie wurden für diesen Entwurf gelesen, nicht unabhängig nachgerechnet. Mehrere Auswertungen und Kriterien entstanden nach Beginn der Rechnungen. Die Zahlen sind daher deskriptive Befunde, keine vorab bestandenen Gesamtprüfungen einer Teilchentheorie.

### 5.1 Energie beim Netzumbau

Bei ausgewählten einzelnen 2→3-Umbauten eines flachen dreidimensionalen Glasnetzes mit 128 Ecken wurde eine gesetzte kinetische Form mit einer aus der 4D-Wirkung gewonnenen effektiven Trägheit verglichen. Bei dem projektintern definierten Geometrieparameter μ=−10⁻³ ergeben sich über 24 Umbauten:

| Übergabe | Median relativer Energiesprung mit bisheriger Form | Mit effektiver 4D-Trägheit |
|---|---:|---:|
| R, Fortsetzung der Längenraten | 4,77×10⁻⁴ | 3,94×10⁻⁸ |
| P, Fortsetzung gemeinsamer Impulse | 8,74×10⁻⁴ | 1,15×10⁻⁶ |

Das Potential bleibt im Test praktisch stetig; der Fehler betrifft die kinetische Energie. Die Formen wurden jeweils mit ihren eigenen Moden geprüft. Die Ergebnisse belegen deshalb keine kleine Abweichung für jeden zulässigen Zustand.

Im P-Verfahren sind sämtliche 56 berichteten Sprünge positiv. Eine wiederholte Anwendung könnte Energie akkumulieren. Außerdem folgt auf die Übergabe eine Projektion auf die neue Zwangsfläche; eine Impulsidentität vor dieser Projektion beweist noch keine kanonische Gesamtentwicklung. Ein langfristig energieverträglicher Umbaualgorithmus bleibt ein zentrales fehlendes Glied.

### 5.2 Gemeinsame Wellengeschwindigkeit

Für die untersuchte periodische Netzgeometrie wurden Licht und geometrische Wellen mit derselben Uhr verglichen. Im langwelligen Grenzfall liegt c_Licht/c_Geometrie beim räumlich diskretisierten Maxwell-Verfahren etwa innerhalb 1±1,5×10⁻¹⁰, bei der vierdimensionalen Whitney-Formulierung innerhalb 1±1,5×10⁻⁷. Die Genauigkeiten charakterisieren diese numerischen Vergleiche, keine experimentellen Vertrauensintervalle.

Die Gleichheit ist aus der gemeinsamen geometrischen Konstruktion erwartet. Bei endlicher Wellenzahl bleiben richtungs- und zweigabhängige Dispersionsunterschiede. Dies motiviert eine gemeinsame relativistische Näherung, beweist aber weder exakte Lorentzsymmetrie bei endlicher Netzskala noch ihre nichtlineare Gültigkeit.

### 5.3 Gravitative Quelle gebundener Materie

Zehn stationäre skalare Gitterzustände wurden als Quellen untersucht. Bei direkt eingesetzter Energiedichte ergibt der Fernfit M/E=0,999999 bis 1,000023. Das prüft primär die numerische Rückgewinnung der vorgegebenen Quelle.

Eine projektseitige schwachfeldige Herleitung metrischer Kopplung liefert zusätzlich einen integrierten Spannungsterm Σ=∫Tⁱᵢd³x. In der dortigen Normierung lautet die aktive Quelle E+Σ. Auf dem Gitter bleibt ein Virialrest; zwei untersuchte Familien liefern beschreibende Exponenten 2,05 und 1,83 für dessen Abnahme mit der Gitterweite. Diese Herleitung und ihre Diskretisierung benötigen weitere unabhängige Prüfung. Passive und träge Masse wurden in dieser Untersuchung nicht berechnet.

## 6. Räumliche Dimension und innere Struktur

Die Konstruktion wird zunächst in drei Raumdimensionen plus Zeit formuliert. Vergleichsmodelle in einer und zwei Raumdimensionen können Mechanismen isolieren, müssen aber eigenständig normiert werden. Insbesondere ändern sich das Volumenelement, Strahlungsschwellen, Fernfelder, topologische Möglichkeiten und verfügbare Zerfallskanäle.

Für einen radialen Skalaransatz in d Raumdimensionen gilt etwa

\[
I_d=\Omega_{d-1}\int_0^\infty r^{d-1}f(r)^2\,dr,
\qquad \Delta_df=f''+\frac{d-1}{r}f'.
\]

Ein radialer 3D-Lauf behält dieses Volumenmaß und ist keine eindimensionale Feldtheorie. Winkelabhängige Störungen werden durch ihn nicht geprüft. Ebenso unterscheiden sich geometrische Gravitation und ihre lokalen Freiheitsgrade mit der Raumzeitdimension; 3+1-Befunde dürfen nicht unverändert übertragen werden.

Fäden, Flächen und Kerne können als unterschiedlich ausgedehnte Strukturen in demselben 3D-Raum auftreten. Ob ein Faden eine stabile Querschnittsstruktur, eine longitudinale Bindung oder eine pumpende Mode trägt, muss jeweils aus Feldgleichungen und Energievergleich folgen. Seine Gestalt liefert noch keine neue Kraft oder zusätzliche Dimension.

## 7. Prüfprogramm und fehlende Nachweise

| Frage | Bisheriger Stand | Entscheidender nächster Nachweis |
|---|---|---|
| Gemeinsame Dynamik | Wirkungsarchitektur und einzelne abgeleitete Module | vollständig gekoppelte Variation samt konsistenten Rand- und Zwangsbedingungen |
| Energieübertragung | kleine Fehler bei einzelnen Umbauten | Langzeitbilanz vieler Umbauten, Vergleich ohne Umbau und Verfeinerung |
| Teilchenträger | klassische lokalisierte Kandidaten | volles Störspektrum und dynamische Stabilität einschließlich Winkelmoden |
| Bildung | ausgewählte Bildungsbefunde in getrennten Modellen | Bildung im tatsächlich gekoppelten Modell ohne künstliches Festhalten |
| Verbundbindung | Teilbefunde in Hilfsmodellen | Energie unter sämtlichen konkurrierenden Zerfallsschwellen |
| Masse | Ruheenergie und Quellenantwort | träge, passive und aktive Masse desselben Zustands |
| Quantenteilchen | Quantisierung als begonnenes Programm | kontrollierte Korrelatoren, endliche-Volumen- und Kontinuumsprüfung, Spektralinterpretation |
| Spin ½ | keine Herleitung im Minimalmodell | Rotationsdarstellung und Austauschstatistik eines quantisierten Zustands |
| Quarks und Farbladung | kein SU(3)-Sektor | lokale Eichdynamik, Quantenzahlen und unterscheidende Einschlussprüfung |
| Messkontakt | synthetische dimensionslose Resultate | feste Skalenabbildung und mindestens eine unabhängige Vorhersage |

Die Reihenfolge ist sachlich: Zunächst muss die Dynamik selbst konsistent sein. Danach sind Träger und Verbünde zu bestimmen. Erst anschließend ist eine Teilchenzuordnung durch dimensionslose Massenverhältnisse, Streuung und Quantenzahlen sinnvoll.

Ein euklidisches Pfadintegral ist ein möglicher Quantisierungsansatz. Seine Verwendung setzt quantenmechanische Struktur ein; sie erklärt deren Entstehung nicht. Auch ein gefittetes Massenspektrum wäre ohne unabhängige Parameterbindung und Gegenproben noch keine Herleitung des Standardmodells.

## 8. Unterscheidende Vorhersagen

**Energiebilanz.** Wenn die gemeinsame Wirkung einen konsistenten Umbau trägt, müssen kumulative Bilanzfehler unter einem festgelegten Verfeinerungsverfahren kontrollierbar werden. Ein positiver Drift, der bei Verfeinerung bestehen bleibt, widerlegt die betreffende Übergaberegel.

**Universelle Bewegung.** Unterschiedlich gebundene Zustände sollen nach Festlegung derselben äußeren Geometrie dieselbe gravitative Beschleunigung im entsprechenden Grenzfall zeigen. Eine verbleibende zusammensetzungsabhängige Abweichung ist ein Modellbefund, der gegen Messungen zu prüfen wäre.

**Teilchenspektrum.** Nach Fixierung der Modellparameter müssen neue dimensionslose Energien oder Streueigenschaften außerhalb der Kalibrierungsmenge vorhergesagt werden. Bloße Ähnlichkeit von Formen oder Frequenzverhältnissen genügt nicht.

**Endliche Netzskala.** Wird sie als physikalisch verstanden, müssen Dispersions- und Richtungsreste gemeinsam mit der Materiedynamik berechnet werden. Eine separat gewählte Uhr oder Kopplung für jeden Sektor würde gerade den zu prüfenden Zusammenhang aufheben.

## 9. Diskussion und Schluss

Das vorgeschlagene Modell verbindet Geometrie und Materie durch eine gemeinsame Wirkung und behandelt Teilchen als dynamische Zustände. Sein derzeit stärkster Anhaltspunkt ist die numerische Verbesserung geometrischer Energieübergaben durch eine abgeleitete statt gesetzte Trägheit. Hinzu kommt die konsistente langwellige Ausbreitung elektromagnetischer und geometrischer Wellen im untersuchten Aufbau.

Diese Ergebnisse rechtfertigen die weitere Untersuchung des Modells. Sie rechtfertigen noch keine Identifikation mit Quarks, Elektronen oder einer vollständigen Quantengravitation. Der entscheidende nächste Schritt ist die Schließung der gemeinsamen Dynamik: Energieübertragung, Zwangsstruktur und metrische Materiekopplung müssen in derselben Entwicklung gelten. Erst auf dieser Grundlage kann ein quantisiertes Spektrum zeigen, ob die lokalisierten Gebilde mehr sind als langlebige klassische Feldzustände.

### 9.1 Verhältnis zu bestehenden Modellen

Die Summe aus Gravitation, elektromagnetischem Feld und selbstwechselwirkendem komplexem Skalar ist keine neue Wirkungsfamilie. Brihaye, Caebergs und Delsate behandeln bereits 2009 geladene, rotierende und gravitierende Q-Bälle mit einem sextischen Potential [4]. Ihre Gleichungen (1)–(4) enthalten den kontinuierlichen Wirkungsaufbau unseres geladenen Erweiterungsarms, bei anderer Parameterwahl. Unser neutraler Minimalarm entspricht bezüglich der direkten elektromagnetischen Kopplung dem entkoppelten Grenzfall. Die Tetraederdiskretisierung und unsere Übergabeverfahren sind damit noch nicht festgelegt.

Auch simpliciale Geometrie mit skalarer Materie [5], elektromagnetische Felder auf simplicialen Netzen [6] und kanonische Entwicklungen bei Netzumbauten [2] sind etablierte Ansätze. Miković untersucht darüber hinaus Regge-Geometrie mit skalaren, Yang-Mills- und fermionischen Materiesektoren in einer gemeinsamen stückweise linearen Konstruktion [7]. Dort werden diese Materiesektoren eingesetzt; daraus folgt keine Herleitung von Quarks aus unseren lokalisierten Skalarzuständen.

Ein besonders enger Architekturvorläufer ist McDonald und Miller [8]: Regge-Geometrie wird dort mit diskreten Differentialformen und einem umkreisbasierten Dualnetz verbunden; skalare und elektromagnetische Wirkungen werden geometrisch diskretisiert. Unsere Kombination aus Netz, Hodge-Gewichten und Materiefeldern ist deshalb für sich kein Neuheitsanspruch. Die Quelle ersetzt insbesondere keinen Nachweis der nichtlinearen Zwangsalgebra oder einer kanonischen Übergabe bei unseren Netzumbauten.

Der mögliche Beitrag dieses Projekts liegt daher in der konkreten Diskretisierung, ihrer kontrollierten Dynamik und gegebenenfalls neuen Spektral- oder Verbundbefunden. Die vorliegende Literaturrecherche begründet keine Prioritätsbehauptung für diese Einzelresultate. Der Entwurf ist als Design- und Methodenarbeit zu lesen, nicht als erstmalige Vereinigung der drei Wirkungssektoren.

## Literaturanschlüsse

Die folgenden Originalarbeiten dienen als methodische Anschlüsse. Für [1]–[3], [5] und [6] wurden Abstracts und bibliografische Angaben geprüft; [4] wurde selektiv in §§2–3, [7] selektiv in Einleitung, §4 und §6 und [8] selektiv in §§2–4 gelesen. Eine vollständige Neuheits- und Beweisprüfung steht aus. Die Quellen belegen keine Resultate unseres konkreten Netzes.

1. B. Dittrich und P. A. Höhn, *From covariant to canonical formulations of discrete gravity*, arXiv:0912.1817. Anschluss: linearisierte Regge-Dynamik und Zwangsbedingungen auf flachem Hintergrund. https://arxiv.org/abs/0912.1817
2. B. Dittrich und P. A. Höhn, *Canonical simplicial gravity*, arXiv:1108.1974. Anschluss: kanonische Beschreibung simplicialer Entwicklung mit veränderlicher Triangulierung. https://arxiv.org/abs/1108.1974
3. A. Stern, Y. Tong, M. Desbrun und J. E. Marsden, *Geometric Computational Electrodynamics with Variational Integrators and Discrete Differential Forms*, arXiv:0707.4470. Anschluss: variationale elektromagnetische Diskretisierung. https://arxiv.org/abs/0707.4470
4. Y. Brihaye, Th. Caebergs und T. Delsate, *Charged-spinning-gravitating Q-balls* (2009), arXiv:0907.0913. https://arxiv.org/abs/0907.0913
5. H. W. Hamber und R. M. Williams, *Simplicial Gravity Coupled to Scalar Matter* (Preprint 1993), arXiv:hep-th/9308099. https://arxiv.org/abs/hep-th/9308099
6. R. Sorkin, *The electromagnetic field on a simplicial net* (1975; Erratum 1978). https://authors.library.caltech.edu/records/nvwen-vw836
7. A. Miković, *Finiteness of quantum gravity with matter on a PL spacetime* (2023), arXiv:2306.15484; hier PDF-v1 selektiv gelesen. https://arxiv.org/abs/2306.15484
8. J. R. McDonald und W. A. Miller, *Coupling Non-Gravitational Fields with Simplicial Spacetimes*, Classical and Quantum Gravity 27, 095011 (2010), arXiv:1002.5001v2. https://arxiv.org/abs/1002.5001

## Anhang zur internen Nachprüfbarkeit

Alle Pfade beziehen sich auf die Projektwurzel. Die Zahlen in Abschnitt 5 sind auf die nachstehenden Berichte beschränkt. Neue Resultate nach diesem Lesestand sind nicht Bestandteil dieser Fassung.

- Architektur: `coordination/runden-v3/RUNDE-50/GRUNDGLEICHUNG-v3.md`.
- Energieübergabe: `coordination/runden-v3/RUNDE-37/umklapp-4d-1/ERGEBNIS.md`, insbesondere Abschnitte 2–6.
- Gemeinsame Uhr: `coordination/runden-v3/RUNDE-37/ueberleitung-v-1/LICHT-GLEICHE-UHR.md`.
- Masse und Spannung: `coordination/runden-v3/RUNDE-37/schwere-masse-v/ERGEBNIS.md`, insbesondere Abschnitte 1–3.
- Lesende Gegenprüfung: `coordination/particle-lenia-review-20261004/CLAUDE-R50-GEGENBLICK-20261005.txt`.
- Quantisierungsanschluss von ag-phy-lat: `model-lab/papers/qball-quantization-20261005-en-codex/main.tex`, Ergebnis und unabhängige Lektüre unter `coordination/resonance-20260930/ag-phy-lat-quantisierung-20261005/`; kanonische Ausarbeitung für den skalaren Sektor auf festem Gitter, kein berechnetes Quantenspektrum.

Die zugrunde liegenden numerischen Rechnungen stammen aus dem Projektteam unter claude-primary; dieser Entwurf wurde mit Codex strukturiert. Ein Manuskriptentwurf ersetzt kein unabhängiges Replikat. Für eine einreichbare Fassung fehlen insbesondere die vollständige Definition der verwendeten Netze, sämtliche Normalisierungen und Reduktionsoperatoren, ein gebundenes Daten- und Codemanifest, Abbildungen aus diesen Daten sowie die Primärlektüre und fachliche Gegenprüfung. Die Autorangabe folgt der Vorgabe des Autors; eine detaillierte Beitrags- und Werkzeugerklärung ist vor Veröffentlichung zu ergänzen.
