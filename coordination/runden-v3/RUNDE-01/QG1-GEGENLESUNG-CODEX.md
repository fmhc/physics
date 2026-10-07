# QG-1: stimmt mit Präzisierungen


c0=1, W=omega² I, I=int f², G=int |grad f|², V=int U, E=W+G+V. Für L=A|dt psi|²-B|grad psi|²-CU mit A=1+a Phi, B=1+b Phi, C=1+c Phi gilt bei festem Q:

E_Q=Q²/(4 A I)+B G+C V; dE_Q/dPhi=-a W+b G+c V.

Stationarität entfernt die implizite Profilvariation. Die träge Masse ist E aus dem Lorentz-Boost, NICHT 2G/d aus einer bloßen Profilverschiebung ohne räumliche Phasenänderung. Normierung: a_Newton=-grad Phi. Daher R=a/a_Newton=(-a W+b G+c V)/E.

## Dimension und Gradientenabschluss

Fest-Q-Skalierung liefert d W-(d-2)G-d V=0, somit E=2W+2G/d. Die angegebene 3D-Identität stimmt. Der geplante 1D-Lauf braucht W+G-V=0.


## Volle Metrik

Für ds²=(1+2Phi)dt²-(1-2gamma Phi)dx²: a=-(1+d gamma), b=1-(d-2)gamma, c=1-d gamma. Damit dE/dPhi=E+gamma[dW-(d-2)G-dV]=E und R=1. Das ist minimale Metrikkopplung plus integrierte Stressbilanz; KEIN Nachweis der Einsteingleichungen oder ihrer Eindeutigkeit. Anisotrope räumliche Metriken benötigen die entsprechende tensorielle Stressbilanz.

## 1D-Papieranker

U(S)=S-S²+S³/2; a0=1-omega², b0=sqrt(1-2a0), 1/2<omega²<1:
f²=2a0/[1+b0 cosh(2sqrt(a0)x)], I=sqrt(2) arcosh(1/b0), G=sqrt(a0)/2-b0² I/4, W=omega² I. Daraus E=2(W+G), R_A=4G/E. Dieser Abschluss ist über die Familie nicht universell: R_A geht an beiden Frequenzrändern gegen null. Die Sollwerte sind ableitbare Kontrollen.

Vor dem Codeabschluss Phi, Gradientenabschluss und Dimension ausdrücklich festlegen. Universeller Fall gilt führend für lokalisierte stationäre, langsam bewegte Testkörper im schwachen, räumlich langsam variierenden Hintergrund. Endliche Größe, Gezeiten, Anregung, Strahlung und Gitterfehler bleiben zu kontrollieren; eine endliche Abweichung ist nicht automatisch ein Codefehler.
