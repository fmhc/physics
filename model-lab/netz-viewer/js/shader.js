// SPDX-License-Identifier: Apache-2.0
// SPDX-FileCopyrightText: 2026 Finn Malte Hinrichsen
// GLSL-Bausteine. Alle Ebenen holen Eckpositionen per texelFetch aus Float-Texturen (Vertex-Pulling):
// Geometrie liegt einmal auf der GPU, je Bild werden nur die Werte-Arrays der sichtbaren Groessen hochgeladen.
// Schreibweise GLSL1 (attribute/varying/gl_FragColor); three.js uebersetzt nach GLSL ES 3.00.

export const GEMEINSAM = /* glsl */ `
uniform sampler2D uLage;       // RGBA32F: Ruhelage xyz je Ecke
uniform sampler2D uVersch;     // RGBA32F: Anzeige-Verschiebung xyz je Ecke
uniform float uUeber;          // zusaetzliche Ueberhoehung (0 = Ruhelage)
uniform int uTexBreite;
uniform vec3 uBox;
uniform vec3 uUrsprung;
uniform vec4 uSchnitt;         // x: Achse (-1 aus), y: Lage, z: Dicke, w: 0 Scheibe / 1 behalte k <= Lage / 2 behalte k >= Lage
uniform float uSchleier;       // Tiefenschleier-Staerke
uniform vec2 uSchleierBereich; // nah, fern (Sichtabstand)
uniform float uHellFaktor;     // Ausgleich fuer duenne Scheiben (weniger Splats entlang des Sichtstrahls)

const vec4 WEG = vec4(2.0, 2.0, 2.0, 1.0);   // ausserhalb des Sichtvolumens: Primitive faellt weg

ivec2 texOrt(int i) { return ivec2(i % uTexBreite, i / uTexBreite); }
vec3 ruhelage(int i) { return texelFetch(uLage, texOrt(i), 0).xyz; }
vec3 versch(int i) { return texelFetch(uVersch, texOrt(i), 0).xyz * uUeber; }

// Mindestbild: kuerzester Abstandsvektor im periodischen Gitter
vec3 minimalBild(vec3 d) {
#ifdef PERIODISCH
  return d - uBox * floor(d / uBox + 0.5);
#else
  return d;
#endif
}
// Punkt in die Grundbox falten
vec3 inBox(vec3 p) {
#ifdef PERIODISCH
  return p - uBox * floor((p - uUrsprung) / uBox);
#else
  return p;
#endif
}
bool weg(vec3 p) {
  if (uSchnitt.x < -0.5) return false;
  vec3 q = p - uUrsprung;
  float k = uSchnitt.x < 0.5 ? q.x : (uSchnitt.x < 1.5 ? q.y : q.z);
  if (uSchnitt.w < 0.5) return abs(k - uSchnitt.y) > 0.5 * uSchnitt.z;
  if (uSchnitt.w < 1.5) return k > uSchnitt.y;
  return k < uSchnitt.y;
}
float schleier(float tiefe) {
  float f = clamp((tiefe - uSchleierBereich.x) / max(uSchleierBereich.y - uSchleierBereich.x, 1e-4), 0.0, 1.0);
  return 1.0 - uSchleier * f * f;
}
`;

export const WERT = /* glsl */ `
uniform sampler2D uLut;
uniform float uNeutral;
uniform float uSpanne;
uniform float uDivergent;
uniform float uSchwelle;
float staerke(float v) { return clamp(abs(v - uNeutral) / uSpanne, 0.0, 1.0); }
float lutPos(float v) {
  float r = (v - uNeutral) / uSpanne;
  return uDivergent > 0.5 ? 0.5 + 0.5 * clamp(r, -1.0, 1.0) : clamp(abs(r), 0.0, 1.0);
}
vec3 lut(float t) { return texture(uLut, vec2(0.5 / 256.0 + t * (255.0 / 256.0), 0.5)).rgb; }
`;

// ---------- Kanten: je Instanz zwei Halbkanten, damit periodische Randkanten nicht quer durch die Box laufen ----------
export const KANTEN_VS = /* glsl */ `
attribute vec2 aKante;
attribute float aWert;
uniform float uMitWert;
uniform float uGrund;
uniform vec3 uGrundFarbe;
uniform float uGamma;
varying vec3 vFarbe;

void main() {
  int ia = int(aKante.x + 0.5);
  int ib = int(aKante.y + 0.5);
  vec3 pa = ruhelage(ia);
  vec3 pb = ruhelage(ib);
  vec3 d = minimalBild(pb - pa);
  float s = uMitWert > 0.5 ? staerke(aWert) : 0.0;
  float k = position.x;
  // jede Halbkante dort pruefen, wo sie gezeichnet wird (periodische Randkanten liegen an zwei Boxseiten)
  vec3 pruef = k < 1.5 ? pa + 0.25 * d : pb - 0.25 * d;
  if (weg(pruef) || (uMitWert > 0.5 && (s < uSchwelle || isnan(aWert)))) { gl_Position = WEG; return; }
  vec3 xa = versch(ia);
  vec3 xb = versch(ib);
  vec3 p;
  if (k < 0.5) p = pa + xa;
  else if (k < 1.5) p = pa + 0.5 * d + 0.5 * (xa + xb);
  else if (k < 2.5) p = pb - 0.5 * d + 0.5 * (xa + xb);
  else p = pb + xb;
  vec4 mv = modelViewMatrix * vec4(p, 1.0);
  gl_Position = projectionMatrix * mv;
  vec3 basis = uGrundFarbe * uGrund;
  vec3 c = uMitWert > 0.5 ? mix(basis, lut(lutPos(aWert)), pow(s, uGamma)) : basis;
  vFarbe = c * schleier(-mv.z);
}
`;

export const LINIE_FS = /* glsl */ `
varying vec3 vFarbe;
void main() { gl_FragColor = vec4(vFarbe, 1.0); }
`;

// ---------- Splats: Gauss-Sprites (additiv) oder Kugel-Imposter (deckend), an Ecken oder Dreiecksmitten ----------
export const SPLAT_VS = /* glsl */ `
attribute float aWert;
#ifdef ORT_DREIECK
attribute vec3 aDreieck;
#endif
uniform float uRadius;
uniform float uMinAnteil;
uniform float uHell;
uniform float uGamma;
uniform float uModus;
varying vec2 vUv;
varying vec3 vFarbe;

void main() {
  float s = staerke(aWert);
  if (s < uSchwelle || isnan(aWert)) { gl_Position = WEG; return; }
#ifdef ORT_DREIECK
  int i0 = int(aDreieck.x + 0.5);
  int i1 = int(aDreieck.y + 0.5);
  int i2 = int(aDreieck.z + 0.5);
  vec3 p0 = ruhelage(i0);
  vec3 c = p0 + (minimalBild(ruhelage(i1) - p0) + minimalBild(ruhelage(i2) - p0)) / 3.0;
  vec3 ruhe = inBox(c);
  vec3 p = ruhe + (versch(i0) + versch(i1) + versch(i2)) / 3.0;
#else
  int i = gl_InstanceID;
  vec3 ruhe = ruhelage(i);
  vec3 p = ruhe + versch(i);
#endif
  if (weg(ruhe)) { gl_Position = WEG; return; }
  float r = uRadius * mix(uMinAnteil, 1.0, sqrt(s));
  vec4 mv = modelViewMatrix * vec4(p, 1.0);
  mv.xy += position.xy * r;
  gl_Position = projectionMatrix * mv;
  vUv = position.xy;
  float hell = uModus < 0.5 ? uHell * uHellFaktor * pow(s, uGamma) : 1.0;
  vFarbe = lut(lutPos(aWert)) * hell * schleier(-mv.z);
}
`;

export const SPLAT_FS = /* glsl */ `
uniform float uModus;
varying vec2 vUv;
varying vec3 vFarbe;
void main() {
  float r2 = dot(vUv, vUv);
  if (r2 > 1.0) discard;
  if (uModus < 0.5) {
    // Quad-Rand = 3 sigma
    gl_FragColor = vec4(vFarbe * exp(-4.5 * r2), 1.0);
  } else {
    vec3 n = vec3(vUv, sqrt(1.0 - r2));
    float licht = 0.28 + 0.72 * max(dot(n, normalize(vec3(-0.45, 0.55, 0.70))), 0.0);
    gl_FragColor = vec4(vFarbe * licht, 1.0);
  }
}
`;

// ---------- Fluss auf Dreiecken: leuchtende Flaechen, an der Kante etwas heller ----------
export const FLUSS_VS = /* glsl */ `
attribute vec3 aDreieck;
attribute float aWert;
uniform float uHell;
uniform float uGamma;
uniform float uSchrumpf;
varying vec3 vFarbe;
varying vec3 vBary;

void main() {
  float s = staerke(aWert);
  if (s < uSchwelle || isnan(aWert)) { gl_Position = WEG; return; }
  int i0 = int(aDreieck.x + 0.5);
  int i1 = int(aDreieck.y + 0.5);
  int i2 = int(aDreieck.z + 0.5);
  vec3 p0 = ruhelage(i0);
  vec3 d1 = minimalBild(ruhelage(i1) - p0);
  vec3 d2 = minimalBild(ruhelage(i2) - p0);
  vec3 c = p0 + (d1 + d2) / 3.0;
  vec3 schub = inBox(c) - c;
  if (weg(c + schub)) { gl_Position = WEG; return; }
  vec3 q0 = p0 + schub + versch(i0);
  vec3 q1 = p0 + d1 + schub + versch(i1);
  vec3 q2 = p0 + d2 + schub + versch(i2);
  vec3 m = (q0 + q1 + q2) / 3.0;
  float k = position.x;
  vec3 q = k < 0.5 ? q0 : (k < 1.5 ? q1 : q2);
  vBary = k < 0.5 ? vec3(1.0, 0.0, 0.0) : (k < 1.5 ? vec3(0.0, 1.0, 0.0) : vec3(0.0, 0.0, 1.0));
  q = m + (q - m) * uSchrumpf;
  vec4 mv = modelViewMatrix * vec4(q, 1.0);
  gl_Position = projectionMatrix * mv;
  vFarbe = lut(lutPos(aWert)) * uHell * uHellFaktor * pow(s, uGamma) * schleier(-mv.z);
}
`;

export const FLUSS_FS = /* glsl */ `
uniform float uKante;
varying vec3 vFarbe;
varying vec3 vBary;
void main() {
  float b = min(min(vBary.x, vBary.y), vBary.z);
  float rand = 1.0 - smoothstep(0.0, 0.11, b);
  gl_FragColor = vec4(vFarbe * (0.6 + uKante * rand), 1.0);
}
`;

// ---------- Drehrahmen: kleines Achsenkreuz je Ecke, Quaternion (w, x, y, z) ----------
export const RAHMEN_VS = /* glsl */ `
attribute float aIdx;
attribute vec4 aQuat;
uniform float uLaenge;
uniform float uGrund;
varying vec3 vFarbe;

vec3 dreh(vec4 q, vec3 v) { vec3 u = q.yzw; return v + 2.0 * cross(u, cross(u, v) + q.x * v); }

void main() {
  int i = int(aIdx + 0.5);
  vec3 ruhe = ruhelage(i);
  if (weg(ruhe)) { gl_Position = WEG; return; }
  float qq = dot(aQuat, aQuat);
  vec4 q = qq > 1e-12 ? aQuat * inversesqrt(qq) : vec4(1.0, 0.0, 0.0, 0.0);
  float achse = position.x;
  float ende = position.y;
  vec3 e = achse < 0.5 ? vec3(1.0, 0.0, 0.0) : (achse < 1.5 ? vec3(0.0, 1.0, 0.0) : vec3(0.0, 0.0, 1.0));
  vec3 p = ruhe + versch(i) + dreh(q, e) * (ende * uLaenge);
  vec4 mv = modelViewMatrix * vec4(p, 1.0);
  gl_Position = projectionMatrix * mv;
  float winkel = 2.0 * acos(clamp(abs(q.x), 0.0, 1.0)) / 3.14159265;
  vec3 farbe = achse < 0.5 ? vec3(1.0, 0.43, 0.37) : (achse < 1.5 ? vec3(0.46, 0.92, 0.52) : vec3(0.42, 0.66, 1.0));
  vFarbe = farbe * mix(uGrund, 1.0, winkel) * schleier(-mv.z);
}
`;
