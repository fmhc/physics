import LeanPilot.NetData
import Mathlib.Tactic.NormNum
import Mathlib.Tactic.FinCases

namespace LeanPilot.Net
set_option maxRecDepth 10000
set_option maxHeartbeats 2000000

/-- Quotient by a common lattice translation. Input vertex order is increasing. -/
def normalize (xs : List Lift) : List Lift :=
  match xs with
  | [] => []
  | a :: _ => xs.map fun b => ⟨b.v, b.x-a.x, b.y-a.y, b.z-a.z⟩

def tetEdges : List Lift → List (List Lift)
  | [a,b,c,d] => [[a,b],[a,c],[a,d],[b,c],[b,d],[c,d]].map normalize
  | _ => []

def tetFaces : List Lift → List (List Lift)
  | [a,b,c,d] => [[a,b,c],[a,b,d],[a,c,d],[b,c,d]].map normalize
  | _ => []

def edgeIncidence (e : List Lift) : Nat := (tetrahedra.flatMap tetEdges).count e

def expectedIncidence : List Lift → Nat
  | [a,b] => if b.v < 4 then 7 else if a.v < 4 then
      (if b.v < 6 then 5 else 4) else 6
  | _ => 0

/-- Class labels: PP=0, CP=1, HP=2, CH=3. -/
def edgeClass : List Lift → Nat
  | [a,b] => if b.v < 4 then 0 else if a.v < 4 then
      (if b.v < 6 then 1 else 2) else 3
  | _ => 4

theorem cell_counts : vertices.length = 10 ∧ edges.length = 68 ∧
    triangles.length = 116 ∧ tetrahedra.length = 58 := by decide

theorem no_duplicate_cells : vertices.Nodup ∧ edges.Nodup ∧
    triangles.Nodup ∧ tetrahedra.Nodup := by decide

theorem tetrahedron_validity : ∀ t ∈ tetrahedra,
    t.length = 4 ∧ (t.map Lift.v).Pairwise (· < ·) ∧
    (∀ a ∈ t, a.v < 10) ∧ normalize t = t := by decide

theorem exact_edge_set : (tetrahedra.flatMap tetEdges).toFinset = edges.toFinset := by decide

theorem exact_triangle_set : (tetrahedra.flatMap tetFaces).toFinset = triangles.toFinset := by decide

/-- Each quotient face is incident to exactly two tetrahedra. -/
theorem face_incidence_two : ∀ f ∈ triangles,
    (tetrahedra.flatMap tetFaces).count f = 2 := by decide

/-- Euler sum of the explicit cell lists; not a homeomorphism theorem. -/
theorem euler_zero : (vertices.length : ℤ) - edges.length + triangles.length -
    tetrahedra.length = 0 := by decide

theorem class_sizes :
    (edges.filter (fun e => edgeClass e == 0)).length = 12 ∧
    (edges.filter (fun e => edgeClass e == 1)).length = 24 ∧
    (edges.filter (fun e => edgeClass e == 2)).length = 24 ∧
    (edges.filter (fun e => edgeClass e == 3)).length = 8 := by decide

theorem incidence_by_class : ∀ e ∈ edges, edgeIncidence e = expectedIncidence e := by decide

theorem incidence_total : (edges.map edgeIncidence).sum = 348 := by decide

theorem incidence_mean : ((edges.map edgeIncidence).sum : ℚ) / edges.length = 87 / 17 := by
  rw [incidence_total]
  norm_num [edges]

/-- The cochain endpoint list really is the endpoint list of the shifted edges. -/
theorem edge_table_matches : ∀ e : Fin 68,
    (edges[e.val]!).map Lift.v = [(edgeVertices e).1.val, (edgeVertices e).2.val] := by decide

/-- Every row uses the three actual shifted edges of that triangle. -/
theorem face_table_matches : ∀ f : Fin 116,
    let t := triangles[f.val]!
    normalize [t[0]!,t[1]!] = edges[(faceEdges f).1.val]! ∧
    normalize [t[1]!,t[2]!] = edges[(faceEdges f).2.1.val]! ∧
    normalize [t[0]!,t[2]!] = edges[(faceEdges f).2.2.val]! := by decide

theorem face_endpoints : ∀ f : Fin 116,
    (edgeVertices (faceEdges f).1).1 = (edgeVertices (faceEdges f).2.2).1 ∧
    (edgeVertices (faceEdges f).1).2 = (edgeVertices (faceEdges f).2.1).1 ∧
    (edgeVertices (faceEdges f).2.1).2 = (edgeVertices (faceEdges f).2.2).2 := by decide

def d0 (x : Fin 10 → ℤ) (e : Fin 68) : ℤ :=
  x (edgeVertices e).2 - x (edgeVertices e).1

def d1 (y : Fin 68 → ℤ) (f : Fin 116) : ℤ :=
  y (faceEdges f).1 + y (faceEdges f).2.1 - y (faceEdges f).2.2

theorem d1_d0 (x : Fin 10 → ℤ) : d1 (d0 x) = 0 := by
  funext f
  obtain ⟨h₀, h₁, h₂⟩ := face_endpoints f
  dsimp [d1, d0]
  rw [h₀, h₁, h₂]
  omega

#print axioms cell_counts
#print axioms no_duplicate_cells
#print axioms tetrahedron_validity
#print axioms exact_edge_set
#print axioms exact_triangle_set
#print axioms face_incidence_two
#print axioms euler_zero
#print axioms class_sizes
#print axioms incidence_by_class
#print axioms incidence_total
#print axioms incidence_mean
#print axioms edge_table_matches
#print axioms face_table_matches
#print axioms face_endpoints
#print axioms d1_d0
end LeanPilot.Net
