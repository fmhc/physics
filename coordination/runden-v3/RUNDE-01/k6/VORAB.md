# K-6: begrenzter Vergleich, vor dem Lauf

30.09.2026. Kein VFW-P1-Lauf: dessen Fremdreview rät vom bisherigen Parameterarm ab. Hier ausschließlich eine zusätzlich angenommene überdämpfte Nahfeld-Reduktion ohne Amplituden, Retardierung oder Energieerhaltung. Kein Gravitationsbefund.

VFW: C=rho omega² v_i v_j/(8pi); F_ij=C cos(delta) (xj-xi)/r³. Mit Reibung zeta, Länge ell, Zeit t0 und Mittelwertnormierung 1/N gilt Jv=N C t0/(zeta ell³). Falls man zusätzlich Adler Kij=kappa/r annimmt: K=N kappa t0/ell. Dieses dissipative K folgt NICHT aus der konservativen Zusatzmasse; es wird als unabhängiger Parameter angenommen. Ein freier Standard-Swarmalator-J kann den anderen Abstandsexponenten nicht global ersetzen.

Primärquelle gelesen: O'Keeffe/Hong/Strogatz, https://arxiv.org/html/1701.05670, Gleichungen 3/4. Standard dx=mean[d/r*(1+J cos delta)-d/r²], dtheta=K mean[sin delta/r]. Hier in 1D als Einschränkung auf eine Linie, nicht als periodisches 1D-Ringmodell. Numerische Regularisierung überall r->sqrt(r²+eps²), eps=.15. VFW-Proxy dx=mean[J cos delta*d/r³ - .05*d/r⁴]. Zweiter Term künstlicher repulsiver Kern, keine VFW-Ableitung.

N=50 einschließlich einer markierten mitbewegten Probe, 49 Positionen uniform [-1,1]^d, Probe bei (3,0); Phasen uniform [-pi,pi], gleiche Eigenfrequenz im rotierenden System null. Seeds31,73, d=1,2. Beide Modelle mit (J,K)=(.8,.8),(.8,0),(-.8,.8),(.8,.8) mit allen Phasen null. Heun T=4, dt=.02 und .01; 64 Läufe. Keine Parameter-Nachsuche. Keine reale ungetriebene Testfeder: auch die Probe besitzt die angenommene Phase mit konstanter Amplitude.

Metriken: R=|mean exp(i theta)|, mittlerer Paarabstand D, S+-=|mean exp(i(arg(x-centroid)+/-theta))| nur in 2D, Probe: radial zur restlichen Population gerichteter phasenabhängiger Geschwindigkeits-/Kraftproxy, getrennt vom Kern. Anfang/Ende und Zeitspuren speichern. Keine Umrechnung in Newton ohne zeta.

Kontrollen: K=0 friert Phasen ein, NICHT unbedingt Kräfte nach räumlicher Sortierung. Die Kartenforderung 'K=0 im Mittel kraftfrei' gilt nur für unabhängige Phasen bei festem Ort. Prüfe deshalb gleichmäßig über 64 Probenphasen gemittelten Kraftproxy am fixierten Snapshot (auch am Ende); Soll null <=1e-12. Paar gleicher Phase zieht im Phasenterm an, Gegenphase stößt ab; J-Umkehr kehrt diesen Term um. Synchronstart R=1 bleibt1. Schwerpunkt erhalten <=1e-10. Fehler -> Lauf technisch nicht verwendbar.

Voraberwartung: K>0 erhöht R relativ K=0; J-Umkehr verändert Raumordnung. Unbekannt ist Effektgröße bis T=4 für diese Präparationen. L2 als explorativer gepaarter End-R-Kontrast >=.05 in jedem Seed/Dimension; L3 Kontrast >=5x größter zugehöriger dt-Halbierungsänderung von R. Keine Signifikanz- oder Attraktorbehauptung aus zwei Seeds. D/S/Probe bleiben Diagnosen. L4: qualitative Synchronisation bekannt; L5: keine kalibrierte experimentelle Abbildung. Höchstens mittlere methodische Nützlichkeit.

TS440: ein Thread CPU0 nice19, gleicher bereits freigegebener CPU-Pool0,1,4,5 der Nachtkampagne; keine zusätzliche exklusive Pacht. Speicher512MiB, CPU-Hardlimit600s, äußeres Walllimit600s. Es werden keine fremden Dienste geändert. Kein .69-GPU-Zugriff.
