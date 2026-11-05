import Mathlib.Data.ZMod.Basic
import Mathlib.GroupTheory.QuotientGroup.Defs
import Mathlib.GroupTheory.Subgroup.Center
import Mathlib.Tactic.Abel
import Mathlib.Tactic.Group
import Mathlib.Tactic.Ring

/-!
# The commutator pairing of a central extension

Chapter 1, § 8, exercise 3, p. 47: for a central extension `Ḡ` of an abelian
group `G` by an abelian group `A`, a system of representatives `g ↦ ḡ` and
its factor system `h`, `h(g₁, g₂) - h(g₂, g₁) = [ḡ₁, ḡ₂]`; hence
`h⁻(g₁, g₂) = h(g₁, g₂) - h(g₂, g₁)` is bilinear, and `h ↦ h⁻` defines a
homomorphism `α : H²(G, A) → Λ²(G, A)` to the group of bilinear alternating
functions.  The hint is the identity `[x y, z] = [x, z]^y [y, z]`, valid in
every group.  The text (as corrected) says «знакопеременных» (alternating,
`f(g, g) = 0`) where the book said «кососимметричных» (`f(g₁, g₂) =
-f(g₂, g₁)`); the same correction is made in Chapter 2, § 4, Corollary 4.2,
p. 96 (cohomology of a free abelian group with trivial coefficients).

Notation.  The book's commutator is `[x, y] = x⁻¹ y⁻¹ x y` and `a^y = y⁻¹ a y`;
here `comm x y = x⁻¹ * y⁻¹ * x * y` (mathlib's `⁅x, y⁆ = x * y * x⁻¹ * y⁻¹`
is not used) and `a^y` is `y⁻¹ * a * y`.  The extension is a group `E`
(the book's `Ḡ`) with a subgroup `A ≤ Subgroup.center E`; `E ⧸ A` abelian
is the book's `Ḡ/A ≅ G` abelian.  For the factor system, `G` is a
commutative group, `s : G → E` is `g ↦ ḡ`, and `h : G → G → E` with values
in `A` satisfies `s g₁ * s g₂ = s (g₁ * g₂) * h g₁ g₂`, the book's
`ḡ₁ ḡ₂ = (g₁ g₂)‾ h(g₁, g₂)`; the additive `h(g₁, g₂) - h(g₂, g₁)` in `A` is
`hminus h g₁ g₂ = (h g₂ g₁)⁻¹ * h g₁ g₂`.

* `comm`: the book's commutator `[x, y] = x⁻¹ y⁻¹ x y`.
* `comm_mul_left`: the hint `[x y, z] = [x, z]^y [y, z]`, in every group.
* `comm_mul_right`: `[x, y z] = [x, z] [x, y]^z`, in every group.
* `comm_self`, `comm_inv`: `[x, x] = 1` and `[y, x]⁻¹ = [x, y]`, in every group.
* `conj_eq_of_commute`: `y⁻¹ c y = c` if `y c = c y`.
* `comm_mul_left_of_mem_center`, `comm_mul_right_of_mem_center`: the
  commutator is multiplicative in an argument when the commutators involved
  are central.
* `comm_mul_mem_center_left`, `comm_mul_mem_center_right`: `[x a, w] = [x, w]`
  and `[w, y b] = [w, y]` for central `a`, `b`.
* `quotient_comm_iff`: `E/A` is abelian iff every commutator lies in `A`.
* `comm_bilinear`: if `A` is central and `E/A` is abelian, `[x, y]` is
  multiplicative in each argument.
* `comm_mul_mem`: if `A` is central, `[x a, y b] = [x, y]` for `a, b ∈ A`, so
  the pairing depends only on the classes of `x` and `y` modulo `A`.
* `comm_transversal`: `[ḡ₁, ḡ₂] = h(g₁, g₂) - h(g₂, g₁)` for a commutative `G`
  (centrality is not needed here).
* `hminus_self`: `h⁻(g, g) = 0`, so `h⁻` is alternating.
* `transversal_mul`: `(g₁ g₂)‾ = ḡ₁ ḡ₂ h(g₁, g₂)⁻¹`.
* `comm_transversal_mem_center`: for a central extension `[ḡ₁, ḡ₂]` is central.
* `hminus_mul_left`, `hminus_mul_right`: for a central extension `h⁻` is
  bilinear, `h⁻(g₁ g₂, g₃) = h⁻(g₁, g₃) + h⁻(g₂, g₃)` and
  `h⁻(g₁, g₂ g₃) = h⁻(g₁, g₂) + h⁻(g₁, g₃)`.
* `coboundary_sub_swap`: with trivial action and commutative `G`, a coboundary
  `δφ(g₁, g₂) = φ(g₁) - φ(g₁ g₂) + φ(g₂)` satisfies `δφ⁻ = 0`, so `h ↦ h⁻`
  (additive in `h`) is defined on `H²(G, A)`.
* `neg_swap_of_alternating`: a biadditive alternating function changes sign
  when the arguments are exchanged.
* `form_skew_not_alternating`: the converse fails: `f(m, n) = m n mod 2` on
  `ℤ × ℤ` with values in `ℤ₂` is biadditive and `f(m, n) = -f(n, m)`, but
  `f(1, 1) ≠ 0`.  Here `G = ℤ` is free abelian, as in exercise 4 and
  Corollary 4.2 of Chapter 2, and `H²(ℤ, ℤ₂) = 0`.

Not covered: the construction of the extension from a cocycle and of the
groups `H²(G, A)`, `Λ²(G, A)`; the statement that `α` is a homomorphism
beyond `δφ⁻ = 0` and the additivity of `h ↦ h⁻`, which is evident; the
isomorphism `H²(G, A) ≅ Λ²(G, A)` of exercise 4 and Corollary 4.2 of
Chapter 2.  The identities `[ḡ₁, ḡ₂] = h(g₁, g₂) - h(g₂, g₁)`, the
bilinearity and alternation of `h⁻` are also checked for the normalised
cocycles of five groups in `checks/sage/chapter-1b.py` (section_8), and the
count of sign-changing and alternating forms on `ℤ²` with values in `ℤ₂` in
`checks/sage/chapter-2b.py`.
-/

namespace KuzminHomology.CommutatorPairing

section AnyGroup

variable {E : Type*} [Group E]

/-- The book's commutator `[x, y] = x⁻¹ y⁻¹ x y`. -/
def comm (x y : E) : E :=
  x⁻¹ * y⁻¹ * x * y

/-- The hint of exercise 3: `[x y, z] = [x, z]^y [y, z]` with `a^y = y⁻¹ a y`. -/
theorem comm_mul_left (x y z : E) : comm (x * y) z = y⁻¹ * comm x z * y * comm y z := by
  simp only [comm]
  group

/-- `[x, y z] = [x, z] [x, y]^z`. -/
theorem comm_mul_right (x y z : E) : comm x (y * z) = comm x z * (z⁻¹ * comm x y * z) := by
  simp only [comm]
  group

theorem comm_self (x : E) : comm x x = 1 := by
  simp only [comm]
  group

theorem comm_inv (x y : E) : (comm y x)⁻¹ = comm x y := by
  simp only [comm]
  group

/-- Conjugation fixes an element that commutes with the conjugating one. -/
theorem conj_eq_of_commute {y c : E} (h : y * c = c * y) : y⁻¹ * c * y = c := by
  rw [mul_assoc, ← h, ← mul_assoc, inv_mul_cancel, one_mul]

theorem comm_mul_left_of_mem_center (x y z : E) (h : comm x z ∈ Subgroup.center E) :
    comm (x * y) z = comm x z * comm y z := by
  rw [comm_mul_left, conj_eq_of_commute (Subgroup.mem_center_iff.mp h y)]

theorem comm_mul_right_of_mem_center (x y z : E) (h : comm x y ∈ Subgroup.center E) :
    comm x (y * z) = comm x y * comm x z := by
  rw [comm_mul_right, conj_eq_of_commute (Subgroup.mem_center_iff.mp h z),
    Subgroup.mem_center_iff.mp h (comm x z)]

theorem comm_mul_mem_center_left (x w : E) {a : E} (ha : a ∈ Subgroup.center E) :
    comm (x * a) w = comm x w := by
  have hw : comm a w = 1 := by
    have e : comm a w = a⁻¹ * (w⁻¹ * a) * w := by simp only [comm, mul_assoc]
    rw [e, Subgroup.mem_center_iff.mp ha w⁻¹]
    group
  rw [comm_mul_left, hw, mul_one,
    conj_eq_of_commute (Subgroup.mem_center_iff.mp ha (comm x w)).symm]

theorem comm_mul_mem_center_right (w y : E) {b : E} (hb : b ∈ Subgroup.center E) :
    comm w (y * b) = comm w y := by
  rw [← comm_inv, comm_mul_mem_center_left y w hb, comm_inv]

end AnyGroup

section Central

variable {E : Type*} [Group E] (A : Subgroup E)

/-- `E/A` is abelian iff every commutator `[x, y]` lies in `A`. -/
theorem quotient_comm_iff [A.Normal] :
    (∀ u v : E ⧸ A, u * v = v * u) ↔ ∀ x y : E, comm x y ∈ A := by
  have key : ∀ x y : E, ((x : E ⧸ A) * y = y * x ↔ comm y x ∈ A) := by
    intro x y
    rw [← QuotientGroup.mk_mul, ← QuotientGroup.mk_mul, QuotientGroup.eq]
    have e : (x * y)⁻¹ * (y * x) = comm y x := by
      simp only [comm]
      group
    rw [e]
  constructor
  · intro hq x y
    exact (key y x).mp (hq y x)
  · intro hc u v
    obtain ⟨x, rfl⟩ := QuotientGroup.mk_surjective u
    obtain ⟨y, rfl⟩ := QuotientGroup.mk_surjective v
    exact (key x y).mpr (hc y x)

variable {A}

/-- If `A` is central and `E/A` is abelian, the commutator is multiplicative in
each argument. -/
theorem comm_bilinear [A.Normal] (hA : A ≤ Subgroup.center E)
    (hq : ∀ u v : E ⧸ A, u * v = v * u) (x y z : E) :
    comm (x * y) z = comm x z * comm y z ∧ comm x (y * z) = comm x y * comm x z := by
  have hc := (quotient_comm_iff A).mp hq
  exact ⟨comm_mul_left_of_mem_center x y z (hA (hc x z)),
    comm_mul_right_of_mem_center x y z (hA (hc x y))⟩

/-- If `A` is central, `[x a, y b] = [x, y]` for `a, b ∈ A`. -/
theorem comm_mul_mem (hA : A ≤ Subgroup.center E) (x y : E) {a b : E} (ha : a ∈ A)
    (hb : b ∈ A) : comm (x * a) (y * b) = comm x y := by
  rw [comm_mul_mem_center_left x _ (hA ha), comm_mul_mem_center_right x y (hA hb)]

end Central

section Transversal

variable {E G : Type*} [Group E] [CommGroup G]

/-- `h⁻(g₁, g₂) = h(g₁, g₂) - h(g₂, g₁)`, written multiplicatively in `E`. -/
def hminus (h : G → G → E) (g₁ g₂ : G) : E :=
  (h g₂ g₁)⁻¹ * h g₁ g₂

/-- Exercise 3: `[ḡ₁, ḡ₂] = h(g₁, g₂) - h(g₂, g₁)` for an abelian `G`. -/
theorem comm_transversal (s : G → E) (h : G → G → E)
    (hs : ∀ g₁ g₂ : G, s g₁ * s g₂ = s (g₁ * g₂) * h g₁ g₂) (g₁ g₂ : G) :
    comm (s g₁) (s g₂) = hminus h g₁ g₂ := by
  have e : comm (s g₁) (s g₂) = (s g₂ * s g₁)⁻¹ * (s g₁ * s g₂) := by
    simp only [comm]
    group
  rw [e, hs g₂ g₁, hs g₁ g₂, mul_comm g₂ g₁, hminus]
  group

/-- `h⁻(g, g) = 0`: `h⁻` is alternating. -/
theorem hminus_self (s : G → E) (h : G → G → E)
    (hs : ∀ g₁ g₂ : G, s g₁ * s g₂ = s (g₁ * g₂) * h g₁ g₂) (g : G) : hminus h g g = 1 := by
  rw [← comm_transversal s h hs, comm_self]

theorem transversal_mul (s : G → E) (h : G → G → E)
    (hs : ∀ g₁ g₂ : G, s g₁ * s g₂ = s (g₁ * g₂) * h g₁ g₂) (g₁ g₂ : G) :
    s (g₁ * g₂) = s g₁ * s g₂ * (h g₁ g₂)⁻¹ := by
  rw [hs, mul_inv_cancel_right]

variable {A : Subgroup E} (hA : A ≤ Subgroup.center E) (s : G → E) (h : G → G → E)
  (hmem : ∀ g₁ g₂ : G, h g₁ g₂ ∈ A)
  (hs : ∀ g₁ g₂ : G, s g₁ * s g₂ = s (g₁ * g₂) * h g₁ g₂)
include hA hmem hs

theorem comm_transversal_mem_center (g₁ g₂ : G) : comm (s g₁) (s g₂) ∈ Subgroup.center E := by
  rw [comm_transversal s h hs]
  exact hA (A.mul_mem (A.inv_mem (hmem g₂ g₁)) (hmem g₁ g₂))

/-- `h⁻(g₁ g₂, g₃) = h⁻(g₁, g₃) + h⁻(g₂, g₃)`. -/
theorem hminus_mul_left (g₁ g₂ g₃ : G) :
    hminus h (g₁ * g₂) g₃ = hminus h g₁ g₃ * hminus h g₂ g₃ := by
  rw [← comm_transversal s h hs, ← comm_transversal s h hs, ← comm_transversal s h hs,
    transversal_mul s h hs g₁ g₂,
    comm_mul_mem_center_left _ _ (hA (A.inv_mem (hmem g₁ g₂))),
    comm_mul_left_of_mem_center _ _ _ (comm_transversal_mem_center hA s h hmem hs g₁ g₃)]

/-- `h⁻(g₁, g₂ g₃) = h⁻(g₁, g₂) + h⁻(g₁, g₃)`. -/
theorem hminus_mul_right (g₁ g₂ g₃ : G) :
    hminus h g₁ (g₂ * g₃) = hminus h g₁ g₂ * hminus h g₁ g₃ := by
  rw [← comm_transversal s h hs, ← comm_transversal s h hs, ← comm_transversal s h hs,
    transversal_mul s h hs g₂ g₃,
    comm_mul_mem_center_right _ _ (hA (A.inv_mem (hmem g₂ g₃))),
    comm_mul_right_of_mem_center _ _ _ (comm_transversal_mem_center hA s h hmem hs g₁ g₂)]

end Transversal

/-- With trivial action and commutative `G`, the coboundary
`δφ(g₁, g₂) = φ(g₁) - φ(g₁ g₂) + φ(g₂)` is symmetric: `δφ⁻ = 0`. -/
theorem coboundary_sub_swap {G B : Type*} [CommGroup G] [AddCommGroup B] (φ : G → B)
    (g₁ g₂ : G) :
    (φ g₁ - φ (g₁ * g₂) + φ g₂) - (φ g₂ - φ (g₂ * g₁) + φ g₁) = 0 := by
  rw [mul_comm g₂ g₁]
  abel

/-- A biadditive alternating function changes sign: `f(x, y) = -f(y, x)`. -/
theorem neg_swap_of_alternating {M B : Type*} [Add M] [AddCommGroup B] (f : M → M → B)
    (hl : ∀ x y z : M, f (x + y) z = f x z + f y z)
    (hr : ∀ x y z : M, f x (y + z) = f x y + f x z)
    (halt : ∀ x : M, f x x = 0) (x y : M) : f x y = -f y x := by
  have e := halt (x + y)
  rw [hl, hr, hr, halt x, halt y] at e
  rw [eq_neg_iff_add_eq_zero]
  simpa using e

/-- `f(m, n) = m n mod 2`, a bilinear function on `ℤ` with values in `ℤ₂`. -/
def form (m n : ℤ) : ZMod 2 :=
  ((m * n : ℤ) : ZMod 2)

/-- `f` is biadditive and changes sign, `f(m, n) = -f(n, m)`, but is not
alternating: `f(1, 1) ≠ 0`. -/
theorem form_skew_not_alternating :
    (∀ m m' n : ℤ, form (m + m') n = form m n + form m' n) ∧
      (∀ m n n' : ℤ, form m (n + n') = form m n + form m n') ∧
      (∀ m n : ℤ, form m n = -form n m) ∧ form 1 1 ≠ 0 := by
  refine ⟨fun m m' n => ?_, fun m n n' => ?_, fun m n => ?_, ?_⟩
  · simp only [form]
    push_cast
    ring
  · simp only [form]
    push_cast
    ring
  · rw [ZMod.neg_eq_self_mod_two, form, form, mul_comm]
  · simp only [form]
    decide

end KuzminHomology.CommutatorPairing

#print axioms KuzminHomology.CommutatorPairing.comm_mul_left
#print axioms KuzminHomology.CommutatorPairing.comm_mul_right
#print axioms KuzminHomology.CommutatorPairing.comm_self
#print axioms KuzminHomology.CommutatorPairing.comm_inv
#print axioms KuzminHomology.CommutatorPairing.quotient_comm_iff
#print axioms KuzminHomology.CommutatorPairing.comm_bilinear
#print axioms KuzminHomology.CommutatorPairing.comm_mul_mem
#print axioms KuzminHomology.CommutatorPairing.comm_transversal
#print axioms KuzminHomology.CommutatorPairing.hminus_mul_left
#print axioms KuzminHomology.CommutatorPairing.hminus_mul_right
#print axioms KuzminHomology.CommutatorPairing.hminus_self
#print axioms KuzminHomology.CommutatorPairing.coboundary_sub_swap
#print axioms KuzminHomology.CommutatorPairing.neg_swap_of_alternating
#print axioms KuzminHomology.CommutatorPairing.form_skew_not_alternating
