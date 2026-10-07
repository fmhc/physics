# Zwei Seiten des Feldes – Formeln und Arbeitsmodell

**Stand:** 2. Oktober 2026  
**Status:** Exploratives mathematisches Spielzeugmodell. Etablierte Mathematik wird mit unbestätigten Modellhypothesen kombiniert.

## Leitidee

Geometrie → Feld → Schnittpunkte → stabile Moden → Teilchen → Raumzeit

Ziel ist zu testen, ob aus einfachen lokalen geometrischen Regeln langlebige Strukturen, charakteristische Frequenzen, Schnitt-Ereignisse („Ticks“) und effektive Wechselwirkungen emergieren.

## 1. Kontinuierliches Feld

$$
\mathcal L=\frac12\partial_\mu\Phi\,\partial^\mu\Phi-V(\Phi)
$$

Mögliches sextisches Potential:

$$
V(\Phi)=m^2|\Phi|^2-\lambda|\Phi|^4+g|\Phi|^6
$$

Feldgleichung:

$$
\partial_\mu\partial^\mu\Phi+\frac{\partial V}{\partial\Phi^*}=0
$$

## 2. Diskrete Geometrie

Zellkomplex:

$$
K=(V,E,F,C)
$$

mit Knoten, Kanten, Flächen und Volumenzellen.

Zustand:

$$
\Psi_i(t)=A_i(t)e^{i\theta_i(t)}
$$

Dynamik:

$$
\ddot\Psi_i+\omega_i^2\Psi_i-\sum_jJ_{ij}(\Psi_j-\Psi_i)+\lambda|\Psi_i|^2\Psi_i=0
$$

Zu testen: Tetraeder, 6er, 8er, geschlossene N-Ketten, 11+1, 19+1, freie und rotierende Varianten.

## 3. Schnittmengen

$$
I_{ab}=M_a\cap M_b
$$

$$
I_S=\bigcap_{i\in S}M_i
$$

Für transversale Schnitte:

$$
\dim(A\cap B)=\dim A+\dim B-\dim X
$$

In 3D gilt generisch etwa:

- 2D ∩ 2D → 1D
- 2D ∩ 1D → 0D
- zwei 1D-Kurven schneiden sich in 3D nicht generisch.

Zu messen sind Schnittzahl $N_I(t)$, Dimension $d_I$, Lebensdauer $\tau_I$, Geburt/Vernichtung und räumliche Verteilung.

## 4. Ticks aus Schnitt-Ereignissen

Operationale Definition:

$$
N_{tick}(t)=\sum_S \mathbf 1[I_S(t-\Delta t)\neq I_S(t)]
$$

Lokale Ereignisrate:

$$
\nu(x)=\lim_{\Delta t\to0}\frac{N_{events}(x,\Delta t)}{\Delta t}
$$

Zu testende Hypothese:

$$
d\tau(x)\propto\nu(x)dt
$$

Das ist keine etablierte physikalische Beziehung. Entscheidend ist, ob die Tickrate bei kleiner werdender numerischer Schrittweite konvergiert und gegenüber Störungen robust bleibt.

## 5. Kanten-, Flächen- und Volumenenergie

$$
E=\alpha_E\sum_{e\in E}L_e+\alpha_F\sum_{f\in F}A_f+\alpha_V\sum_{c\in C}V_c+E_{field}+E_{intersection}
$$

Daraus:

$$
F_i=-\nabla_iE
$$

bzw.

$$
m_i\ddot x_i=-\frac{\partial E}{\partial x_i}
$$

Eine mögliche Schnittenergie:

$$
E_{intersection}=\sum_S\beta_S\mathcal M(I_S)
$$

wobei $\mathcal M$ je nach Schnittdimension Punktzahl, Länge oder Fläche bezeichnet.

## 6. Rotierende N+1-Systeme

$$
\theta_j(t)=\frac{2\pi j}{N}+\Omega t
$$

$$
x_j(t)=R(\cos\theta_j,\sin\theta_j,0)
$$

Zentraler Zustand:

$$
x_{N+1}=0
$$

Besonders zu testen:

$$
11+1,\qquad19+1
$$

Parameter: $\Omega,J,R,N,\lambda,\alpha_E,\alpha_F,\alpha_V$, Phasenoffsets, Kopplungsreichweite, Dämpfung und Störungen.

## 7. Stabilität

$$
\Psi=\Psi_0+\delta\Psi
$$

Linearisiert:

$$
\delta\ddot\Psi=-\mathbf H\delta\Psi
$$

$$
H_{ij}=\frac{\partial^2E}{\partial\Psi_i\partial\Psi_j}
$$

Eigenwertproblem:

$$
\mathbf H v_n=\lambda_n v_n
$$

Im einfachen konservativen Fall sind positive Eigenwerte lokal oszillatorisch/stabil; negative können instabile Richtungen anzeigen. Nullmoden können Symmetrien entsprechen. Für rotierende periodische Lösungen sollte zusätzlich eine Floquet-Analyse erfolgen.

## 8. Gemeinsame Wirkung

$$
S=\int dt\left[\sum_i\frac{m_i}{2}|\dot x_i|^2+\sum_i\frac12|\dot\Psi_i|^2-E(K,x,\Psi)\right]
$$

mit

$$
E=E_{edge}+E_{face}+E_{volume}+E_{intersection}+E_{field}
$$

und

$$
\delta S=0
$$

Ziel: Kräfte möglichst aus einer konsistenten Wirkung ableiten und nicht nachträglich für gewünschte Effekte hinzufügen.

## 9. Teilchen als stabile Mode

Arbeitsdefinition: Ein „Teilchen“ wäre eine robuste, lokalisierte dynamische Mode des Systems.

$$
\Psi(x,t)\approx\phi(x)e^{i\omega t}
$$

bzw. diskret

$$
\Psi_i(t)=A_i e^{i(\omega t+\theta_i)}
$$

Eine teilchenähnliche Mode sollte lokalisiert sein, Energie tragen, viele Perioden überleben, Störungen tolerieren und reproduzierbar wechselwirken.

## 10. Frequenzen und Dimension

Normalmoden:

$$
\omega_n^2=\lambda_n
$$

Vergleich:

$$
P(\omega|D=1),\quad P(\omega|D=2),\quad P(\omega|D=3)
$$

Gesuchte empirische Beziehung:

$$
\nu_{tick}=f(\omega_n,N_I,d_I,E,D)
$$

Diese Funktion darf nicht vorausgesetzt werden.

## 11. Dimensionswahrscheinlichkeiten

Zeitbasiert:

$$
P(d=k)=\frac{T_{d=k}}{T_{total}}
$$

Ereignisbasiert:

$$
P(d=k)=\frac{N_{d=k}}{\sum_jN_{d=j}}
$$

Gemeinsam:

$$
P(d,\omega,\tau_I|N,\Omega,J,\ldots)
$$

## 12. Schnittstabilität

$$
\tau_k=t_{death}-t_{birth}
$$

$$
\sigma_I=\frac1{N_I}\sum_k\frac{\tau_k}{T_{sim}}
$$

Zusätzlich die Überlebensfunktion:

$$
P(\tau_I>\tau)
$$

Interessant wäre eine robuste Trennung zwischen kurzlebigen Zufallsschnitten und langlebigen gebundenen Schnittstrukturen.

## 13. Korrelationen

$$
C_{I,\nu}(\Delta t)=\langle\delta N_I(t)\delta\nu(t+\Delta t)\rangle
$$

$$
C_{E,\nu}=corr(E,\nu_{tick})
$$

$$
C_{\omega,\nu}=corr(\omega_{dominant},\nu_{tick})
$$

## 14. 11+1 und 19+1 sauber testen

Nicht nur 11 und 19 untersuchen, sondern mindestens:

$$
N=8,9,10,11,12,\ldots,18,19,20
$$

Mögliche Kennzahlen:

$$
Q(N)=\frac{\tau_{life}}{\tau_{rotation}}
$$

$$
S(N)=\min_n\lambda_n
$$

$$
T(N)=\frac{N_{stable\ intersections}}{N_{possible\ intersections}}
$$

Falls Primzahllängen besondere Resonanz- oder Frustrationseigenschaften haben, sollte dies aus dem Scan entstehen und nicht in die Modellregeln eingebaut werden.

## 15. Perturbations- und Chaostest

$$
x_i\to x_i+\epsilon_i
$$

$$
\theta_i\to\theta_i+\delta_i
$$

Abstand zweier Trajektorien:

$$
\|\delta X(t)\|
$$

Bei

$$
\|\delta X(t)\|\sim e^{\Lambda t}
$$

ist $\Lambda>0$ ein Hinweis auf empfindliche/chaotische Dynamik.

## 16. Messgrößen pro Run

| Größe | Bedeutung |
|---|---|
| N | Zahl äußerer Elemente |
| D | geometrische/effektive Dimension |
| Ω | Rotationsfrequenz |
| E(t) | Gesamtenergie |
| N_I(t) | Schnittzahl |
| d_I | Schnittdimension |
| ν_tick | Ereignis-/Tickrate |
| ω_n | Eigenfrequenzen |
| λ_n | Stabilitätseigenwerte |
| τ_life | Modenlebensdauer |
| R(t) | charakteristische Ausdehnung |
| ΔE/E | numerischer Energiefehler |

Zusätzlich: Floquet-Multiplikatoren, Lyapunov-Exponent, Phasenkohärenz, Schnitt-Geburts-/Sterberate und Spektraldichte.

## 17. Run-Plan

### A – Baseline
Tetraeder → 6er → 8er → 11+1 → 19+1. Jeweils statisch, frei und rotierend.

### B – N-Scan
Mindestens N=4…32, damit vermeintliche Sonderfälle mit ihren Nachbarn verglichen werden.

### C – Parameter-Sweep
Variation von $\Omega,J,R,\lambda,\alpha_E,\alpha_F,\alpha_V$.

### D – Perturbation
Jede stabile Kandidatenlösung mit vielen kleinen zufälligen Störungen erneut simulieren.

### E – Schnittanalyse
Schnittzahl, Schnittdimension, Persistenz, Tickrate, Frequenzspektrum und Stabilität gemeinsam auswerten.

### F – Skalierung
Abhängigkeit von N, Systemgröße und numerischer Auflösung untersuchen.

## 18. Kontrollen gegen Scheineffekte

**Numerische Konvergenz:** Runs mit $\Delta t$, $\Delta t/2$ und $\Delta t/4$. Ein fundamentaler Tick darf nicht nur die Integrationsschrittweite abbilden.

**Energieerhaltung:** In konservativen Varianten muss $\Delta E/E$ klein bleiben.

**Nullmodelle:** Dieselbe Analyse auf zufälligen Geometrien durchführen.

**Einheitenanalyse:** Alle Terme einer Wirkung müssen dimensionsmäßig kompatibel sein.

**Seeds:** Viele Anfangsbedingungen verwenden. Ein Effekt, der nur in einer handgewählten Konfiguration erscheint, ist schwach.

## 19. Status der Ideen

### Mathematisch etablierte Werkzeuge
- Graphen/Zellkomplexe
- diskrete Laplace-Operatoren
- Variationsprinzip
- Schnittmengen und transversale Dimensionszählung
- Eigenwertanalyse
- Floquet-Analyse
- Lyapunov-/Perturbationstests

### Offene Modellhypothesen
- Schnitt-Ereignisse als fundamentale Ticks
- Eigenzeit proportional zur Ereignisrate
- Teilchen als stabile Schnitt-/Feldmoden
- besondere Stabilität bestimmter N+1-Ketten
- Zusammenhang zwischen Dimension, Schnittwahrscheinlichkeit und Frequenz
- effektive Anziehung aus Kanten-, Flächen- und Volumenenergie

### Noch nicht gezeigt
- Reproduktion realer Elementarteilchen
- Entstehung bekannter Quantenzahlen
- emergente Lorentz-Invarianz
- korrekter Gravitations-/Einstein-Grenzfall
- Vorhersage beobachteter Massen oder Kopplungen
- fundamentale Auszeichnung von 11 oder 19
- Identität von Tickrate und physikalischer Zeit

## 20. Minimaler Simulationskern

Zustandsvektor:

$$
X=(x_1,\ldots,x_N,\dot x_1,\ldots,\dot x_N,\Psi_1,\ldots,\Psi_N,\dot\Psi_1,\ldots)
$$

Dynamik:

$$
\dot X=F(X;\Theta)
$$

mit

$$
\Theta=(N,\Omega,J,R,\lambda,\alpha_E,\alpha_F,\alpha_V,\ldots)
$$

Pro Zeitschritt:

1. Geometrie aktualisieren.
2. Schnittmengen bestimmen.
3. Schnittstruktur mit vorherigem Schritt vergleichen.
4. Ereignisse/Ticks registrieren.
5. Energie berechnen.
6. Phasen- und Modendaten speichern.
7. Stabilitätsdiagnostik aktualisieren.

## 21. Kernfragen

1. Wie viele Schnittkomponenten können gleichzeitig stabil bestehen?
2. Welche Schnittdimensionen dominieren für welche Geometrien?
3. Gibt es charakteristische Ereignisfrequenzen?
4. Skalieren sie mit N oder Dimension?
5. Erzeugen Kanten-, Flächen- und Volumenterme unterschiedliche Stabilitätsklassen?
6. Gibt es langlebige rotierende N+1-Moden?
7. Sind 11+1 oder 19+1 gegenüber benachbarten N tatsächlich außergewöhnlich?
8. Bleiben Resultate bei kleinerem Zeitschritt bestehen?
9. Überleben Kandidaten zufällige Perturbationen?
10. Existiert ein sinnvolles Kontinuumslimit?

## 22. Kompakte Formelkarte

$$
K=(V,E,F,C)
$$

$$
\Psi_i=A_i e^{i\theta_i}
$$

$$
\ddot\Psi_i+\omega_i^2\Psi_i-\sum_jJ_{ij}(\Psi_j-\Psi_i)+\lambda|\Psi_i|^2\Psi_i=0
$$

$$
I_S=\bigcap_{i\in S}M_i
$$

$$
\dim(A\cap B)=\dim A+\dim B-\dim X
$$

$$
\nu=\lim_{\Delta t\to0}\frac{N_{events}}{\Delta t}
$$

$$
d\tau\propto\nu dt \quad \text{(Hypothese)}
$$

$$
E=\alpha_E\sum L+\alpha_F\sum A+\alpha_V\sum V+E_{field}+E_{intersection}
$$

$$
F_i=-\nabla_iE
$$

$$
\mathbf H v_n=\lambda_n v_n
$$

$$
S=\int dt\,(T-E)
$$

$$
\delta S=0
$$

---

## Nächster konkreter Schritt

Der nächste belastbare Schritt ist kein weiteres Interpretieren, sondern ein reproduzierbarer numerischer Benchmark:

**Tetraeder → 6/8 → vollständiger N-Scan → 11+1/19+1 Detailanalyse → Schnittpersistenz → Eigenwert/Floquet-Stabilität → Tick-Spektrum → Perturbation → Konvergenztest.**

Erst danach sollte geprüft werden, ob robuste emergente Strukturen Analogien zu bekannten physikalischen Systemen besitzen.
