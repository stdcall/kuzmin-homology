import Mathlib.GroupTheory.FreeGroup.Basic
import Mathlib.Algebra.MonoidAlgebra.MapDomain
import Mathlib.Algebra.BigOperators.Ring.Finset
import Mathlib.Tactic.NoncommRing

/-!
# Fox derivatives and the Fox identity

Chapter 1, § 9, pp. 50–51: the partial (Fox) derivatives `∂v/∂x_i` of an
element `v` of the free group `F` with free generators `x_1, …, x_n`, defined
through the semidirect product `F P` by
`v(x_1 e_1, …, x_n e_n) = v(x_1, …, x_n) e_1^(∂v/∂x_1) ⋯ e_n^(∂v/∂x_n)`;
the formulas (1.23)–(1.26), the derivation rule (1.28)
`∂(vw)/∂x_i = (∂v/∂x_i) w + ∂w/∂x_i`, the Fox identity (1.29)
`v − 1 = Σ (x_i − 1) ∂v/∂x_i` with the book's proof (both sides are
derivations that agree on the generators), and its image (1.30)
`v(g_1, …, g_n) − 1 = Σ (g_i − 1) ∂v/∂g_i` under `x_i ↦ g_i`.  Chapter 3,
§ 6, p. 153: the unnumbered display `Σ (y_i − 1) ∂v/∂y_i = v − 1` after the
Magnus criterion (3.28) is (1.30) for the images `y_i` of the free generators.

Sides.  The book's modules are right modules (`a^g`), the product of the
semidirect product is `(g a)(h b) = (g h)(a^h b)`, and the derivatives are
right derivations, `d(uv) = d(u) v + d(v)`.  With this convention the factors
`x_i − 1` of (1.29) stand on the left of the derivatives; with them on the
right the identity fails.

Notation.  `α` indexes the free generators (`Fin n` for `x_1, …, x_n`; the
identities need `[Fintype α]` only for the finite sums); `F = FreeGroup α`,
`x_i = FreeGroup.of i`; `ZF α = MonoidAlgebra ℤ F` is the group ring `ℤF` and
`ι : F →* ℤF` the inclusion `g ↦ g`.  The free right `ℤF`-module `P` with
free generators `e_i` is `α → ℤF` (`a = Σ e_i t_i` is the vector `(t_i)`,
`e_i = Pi.single i 1`), and `SemiProd α` is the semidirect product `F P`: the
pair `⟨g, a⟩` is the element `g a`.  `fox i v` is `∂v/∂x_i`;
`IsDerivation d` says `d (u v) = d u · v + d v` for `d : F → ℤF`.  The
commutator is `[a, b] = a⁻¹ b⁻¹ a b`, as in the book.

* `ZF`, `ι`, `SemiProd` with `SemiProd.mul_grp`, `SemiProd.mul_vec`,
  `SemiProd.one_grp`, `SemiProd.one_vec`, `SemiProd.inv_grp`,
  `SemiProd.inv_vec` (the defining equations, by `rfl`), `SemiProd.grpHom`
  (the projection `F P → F`): the objects above.
* `SemiProd.instGroup`: `F P` is a group with `(g a)(h b) = (g h)(a h + b)`,
  unit `1 0` and `(g a)⁻¹ = g⁻¹ (−a g⁻¹)`.
* `embed`: the homomorphism `F → F P` extending `x_i ↦ x_i e_i`.
* `embed_grp`: its `F`-component is the identity, so `embed v` is
  `v(x_1 e_1, …, x_n e_n) = v(x_1, …, x_n) a` with `a ∈ P`.
* `fox`: `∂v/∂x_i`, the `i`-th coordinate of this `a`.
* `embed_apply`: `v(x_1 e_1, …, x_n e_n) = v Σ e_i ∂v/∂x_i`.
* `fox_mul`: (1.28), for all `u, v ∈ F`.
* `isDerivation_fox`: `∂/∂x_i` is a derivation (the same statement).
* `fox_of`, `fox_of_self`, `fox_of_ne`: (1.25), `∂x_i/∂x_i = 1`,
  `∂x_j/∂x_i = 0` for `i ≠ j`.
* `fox_one`: `∂1/∂x_i = 0`.
* `fox_inv`: `∂(u⁻¹)/∂x_i = −(∂u/∂x_i) u⁻¹` for all `u ∈ F`.
* `fox_of_inv_self`, `fox_of_inv_ne`: (1.26), `∂x_i⁻¹/∂x_i = −x_i⁻¹`,
  `∂x_j⁻¹/∂x_i = 0` for `i ≠ j`.
* `IsDerivation.map_one`, `IsDerivation.map_inv`: every derivation `d`
  satisfies `d(1) = 0` and `d(u⁻¹) = −d(u) u⁻¹` (the remark of p. 51 that
  (1.28) with (1.25), (1.26) computes the derivatives by induction on the
  length of a word).
* `IsDerivation.ext`: two derivations with the same values on the generators
  coincide (the last step of the proof of (1.29)).
* `IsDerivation.sum_mul_left`: a linear combination `Σ r_k d_k` of
  derivations with coefficients `r_k ∈ ℤF` on the left is a derivation.
* `isDerivation_sub_one`: `v ↦ v − 1` is a derivation,
  `vw − 1 = (v − 1) w + (w − 1)`.
* `eq_fox`: `∂/∂x_i` is the unique derivation with the values (1.25) on the
  generators.
* `fox_identity`: (1.29), `v − 1 = Σ_i (x_i − 1) ∂v/∂x_i` in `ℤF`.
* `fox_identity_values`: (1.30) and the display of p. 153: for a
  homomorphism `f : F → G`, `g_i = f(x_i)`, and `∂v/∂g_i` the image of
  `∂v/∂x_i` under the ring homomorphism `ℤF → ℤG` induced by `f`,
  `f(v) − 1 = Σ_i (g_i − 1) ∂v/∂g_i`.
* `fox_pow`: (1.23), `∂x^n/∂x = x^(n−1) + ⋯ + x + 1` for `x = x_i`, `n ≥ 0`.
* `fox_commutator_left`, `fox_commutator_right`: (1.24),
  `∂[x_1, x_2]/∂x_1 = x_2 − [x_1, x_2]` and
  `∂[x_1, x_2]/∂x_2 = 1 − x_2⁻¹ x_1 x_2` for distinct generators (the second
  in its corrected form; the original prints `x^2` for the last `x_2`).

Not covered: the formula (1.27) for the values of a word in an arbitrary
semidirect product `G A`, Proposition 9.1 and the remaining propositions of
§ 9, the exercises; that the augmentation ideal `Δ_F` is free on the `x_i − 1`
(so that the derivatives are the unique coefficients in (1.29)); the Magnus
embedding and the criteria (3.27), (3.28) of chapter 3, § 6, of which only
the identity of p. 153 is formalized here.  The same formulas, and the two
computations of the derivatives (from the semidirect product and letter by
letter), are checked on random words in `checks/sage/chapter-1b.py`; the
identity on the free generators of subgroups in `checks/sage/chapter-2a.py`.
-/

noncomputable section

namespace KuzminHomology.FoxFundamental

open MonoidAlgebra

variable {α : Type*}

/-- The integral group ring `ℤF` of the free group `F` on `α`. -/
abbrev ZF (α : Type*) := MonoidAlgebra ℤ (FreeGroup α)

/-- The inclusion `F → ℤF`, `g ↦ g`. -/
abbrev ι : FreeGroup α →* ZF α := MonoidAlgebra.of ℤ (FreeGroup α)

/-- The semidirect product `F P` of `F` with the free right `ℤF`-module
`P = α → ℤF` (free generators `e_i = Pi.single i 1`): `⟨g, a⟩` is `g a`. -/
@[ext] structure SemiProd (α : Type*) where
  /-- The component `g ∈ F` of `g a`. -/
  grp : FreeGroup α
  /-- The component `a ∈ P` of `g a`, as its coordinates in the basis `e_i`. -/
  vec : α → ZF α

namespace SemiProd

instance : Mul (SemiProd α) :=
  ⟨fun x y => ⟨x.grp * y.grp, fun i => x.vec i * ι y.grp + y.vec i⟩⟩
instance : One (SemiProd α) := ⟨⟨1, 0⟩⟩
instance : Inv (SemiProd α) := ⟨fun x => ⟨x.grp⁻¹, fun i => -(x.vec i * ι x.grp⁻¹)⟩⟩

@[simp] lemma mul_grp (x y : SemiProd α) : (x * y).grp = x.grp * y.grp := rfl
@[simp] lemma mul_vec (x y : SemiProd α) (i : α) :
    (x * y).vec i = x.vec i * ι y.grp + y.vec i := rfl
@[simp] lemma one_grp : (1 : SemiProd α).grp = 1 := rfl
@[simp] lemma one_vec (i : α) : (1 : SemiProd α).vec i = 0 := rfl
@[simp] lemma inv_grp (x : SemiProd α) : x⁻¹.grp = x.grp⁻¹ := rfl
@[simp] lemma inv_vec (x : SemiProd α) (i : α) : x⁻¹.vec i = -(x.vec i * ι x.grp⁻¹) := rfl

/-- `F P` is a group: `(g a)(h b) = (g h)(a h + b)`, `(g a)⁻¹ = g⁻¹ (−a g⁻¹)`. -/
instance instGroup : Group (SemiProd α) where
  mul_assoc x y z := by
    ext i
    · simp [mul_assoc]
    · simp [map_mul, add_mul, mul_assoc, add_assoc]
  one_mul x := by ext i <;> simp
  mul_one x := by ext i <;> simp
  inv_mul_cancel x := by
    ext i
    · simp
    · simp only [mul_vec, inv_vec, one_vec, neg_mul, mul_assoc, ← map_mul,
        inv_mul_cancel, map_one, mul_one, neg_add_cancel]

/-- The projection `F P → F`, `g a ↦ g`. -/
def grpHom : SemiProd α →* FreeGroup α where
  toFun := SemiProd.grp
  map_one' := rfl
  map_mul' _ _ := rfl

end SemiProd

/-- A (right) derivation `d : F → ℤF`: `d(uv) = d(u) v + d(v)`. -/
def IsDerivation (d : FreeGroup α → ZF α) : Prop :=
  ∀ u v, d (u * v) = d u * ι v + d v

namespace IsDerivation

variable {d d₁ d₂ : FreeGroup α → ZF α}

/-- `d(1) = 0` for a derivation. -/
theorem map_one (hd : IsDerivation d) : d 1 = 0 := by
  have h := hd 1 1
  rw [mul_one, _root_.map_one, mul_one] at h
  exact left_eq_add.mp h

/-- `d(u⁻¹) = −d(u) u⁻¹` for a derivation. -/
theorem map_inv (hd : IsDerivation d) (u : FreeGroup α) : d u⁻¹ = -(d u * ι u⁻¹) := by
  have h := hd u u⁻¹
  rw [mul_inv_cancel, hd.map_one] at h
  exact eq_neg_of_add_eq_zero_right h.symm

/-- Two derivations with the same values on the free generators coincide. -/
theorem ext (h₁ : IsDerivation d₁) (h₂ : IsDerivation d₂)
    (h : ∀ j, d₁ (FreeGroup.of j) = d₂ (FreeGroup.of j)) : d₁ = d₂ := by
  funext v
  induction v with
  | one => rw [h₁.map_one, h₂.map_one]
  | of x => exact h x
  | inv_of x _ => rw [h₁.map_inv, h₂.map_inv, h x]
  | mul x y hx hy => rw [h₁, h₂, hx, hy]

/-- `Σ r_k d_k` is a derivation if the `d_k` are (coefficients on the left). -/
theorem sum_mul_left {κ : Type*} (s : Finset κ) (r : κ → ZF α)
    (d : κ → FreeGroup α → ZF α) (hd : ∀ k ∈ s, IsDerivation (d k)) :
    IsDerivation fun v => ∑ k ∈ s, r k * d k v := by
  intro u v
  rw [Finset.sum_mul, ← Finset.sum_add_distrib]
  refine Finset.sum_congr rfl fun k hk => ?_
  rw [hd k hk, mul_add, mul_assoc]

end IsDerivation

/-- `v ↦ v − 1` is a derivation: `vw − 1 = (v − 1) w + (w − 1)`. -/
theorem isDerivation_sub_one : IsDerivation fun v : FreeGroup α => ι v - 1 := by
  intro u v
  simp only [map_mul]
  noncomm_ring

variable [DecidableEq α]

/-- The homomorphism `F → F P` extending `x_i ↦ x_i e_i`. -/
def embed : FreeGroup α →* SemiProd α :=
  FreeGroup.lift fun i => ⟨FreeGroup.of i, Pi.single i 1⟩

/-- `v(x_1 e_1, …, x_n e_n) = v(x_1, …, x_n) a` with `a ∈ P`. -/
theorem embed_grp (v : FreeGroup α) : (embed v).grp = v := by
  have h : SemiProd.grpHom.comp (embed (α := α)) = MonoidHom.id _ :=
    FreeGroup.ext_hom _ _ fun a => by simp [embed, SemiProd.grpHom]
  exact congrArg (fun f => f v) h

/-- The Fox derivative `∂v/∂x_i`: the coefficient of `e_i` in `a`, where
`v(x_1 e_1, …, x_n e_n) = v a`. -/
def fox (i : α) (v : FreeGroup α) : ZF α := (embed v).vec i

/-- `v(x_1 e_1, …, x_n e_n) = v Σ e_i ∂v/∂x_i`. -/
theorem embed_apply (v : FreeGroup α) : embed v = ⟨v, fun i => fox i v⟩ := by
  ext i
  · exact embed_grp v
  · rfl

/-- (1.28): `∂(uv)/∂x_i = (∂u/∂x_i) v + ∂v/∂x_i`. -/
theorem fox_mul (i : α) (u v : FreeGroup α) : fox i (u * v) = fox i u * ι v + fox i v := by
  simp only [fox, map_mul, SemiProd.mul_vec, embed_grp]

/-- `∂/∂x_i` is a derivation. -/
theorem isDerivation_fox (i : α) : IsDerivation (fox i) := fox_mul i

/-- (1.25): `∂x_j/∂x_i = δ_ij`. -/
theorem fox_of (i j : α) : fox i (FreeGroup.of j) = if i = j then 1 else 0 := by
  simp [fox, embed, Pi.single_apply]

/-- (1.25): `∂x_i/∂x_i = 1`. -/
theorem fox_of_self (i : α) : fox i (FreeGroup.of i) = 1 := by simp [fox_of]

/-- (1.25): `∂x_j/∂x_i = 0` for `i ≠ j`. -/
theorem fox_of_ne {i j : α} (h : i ≠ j) : fox i (FreeGroup.of j) = 0 := by simp [fox_of, h]

/-- `∂1/∂x_i = 0`. -/
theorem fox_one (i : α) : fox i (1 : FreeGroup α) = 0 := (isDerivation_fox i).map_one

/-- `∂(u⁻¹)/∂x_i = −(∂u/∂x_i) u⁻¹`. -/
theorem fox_inv (i : α) (u : FreeGroup α) : fox i u⁻¹ = -(fox i u * ι u⁻¹) := by
  simp only [fox, map_inv, SemiProd.inv_vec, embed_grp]

/-- (1.26): `∂x_i⁻¹/∂x_i = −x_i⁻¹`. -/
theorem fox_of_inv_self (i : α) : fox i (FreeGroup.of i)⁻¹ = -ι (FreeGroup.of i)⁻¹ := by
  rw [fox_inv, fox_of_self, one_mul]

/-- (1.26): `∂x_j⁻¹/∂x_i = 0` for `i ≠ j`. -/
theorem fox_of_inv_ne {i j : α} (h : i ≠ j) : fox i (FreeGroup.of j)⁻¹ = 0 := by
  rw [fox_inv, fox_of_ne h, zero_mul, neg_zero]

/-- `∂/∂x_i` is the only derivation with the values (1.25) on the generators. -/
theorem eq_fox {i : α} {d : FreeGroup α → ZF α} (hd : IsDerivation d)
    (hgen : ∀ j, d (FreeGroup.of j) = if i = j then 1 else 0) : d = fox i :=
  hd.ext (isDerivation_fox i) fun j => by rw [hgen, fox_of]

/-- (1.29), the Fox identity: `v − 1 = Σ_i (x_i − 1) ∂v/∂x_i`. -/
theorem fox_identity [Fintype α] (v : FreeGroup α) :
    ι v - 1 = ∑ i, (ι (FreeGroup.of i) - 1) * fox i v := by
  have h : (fun v : FreeGroup α => ι v - 1)
      = fun v => ∑ i, (ι (FreeGroup.of i) - 1) * fox i v :=
    isDerivation_sub_one.ext
      (IsDerivation.sum_mul_left Finset.univ (fun i => ι (FreeGroup.of i) - 1)
        (fun i => fox i) fun i _ => isDerivation_fox i)
      fun j => by simp [fox_of]
  exact congrFun h v

/-- (1.30) and p. 153: `v(g_1, …, g_n) − 1 = Σ_i (g_i − 1) ∂v/∂g_i` for
`g_i = f(x_i)`, the values `∂v/∂g_i` being the images of `∂v/∂x_i` in `ℤG`. -/
theorem fox_identity_values [Fintype α] {G : Type*} [Group G] (f : FreeGroup α →* G)
    (v : FreeGroup α) :
    MonoidAlgebra.of ℤ G (f v) - 1
      = ∑ i, (MonoidAlgebra.of ℤ G (f (FreeGroup.of i)) - 1)
          * mapDomainRingHom ℤ f (fox i v) := by
  have hι : ∀ g, mapDomainRingHom ℤ f (ι g) = MonoidAlgebra.of ℤ G (f g) := fun g => by
    simp [mapDomain_single]
  have h := congrArg (mapDomainRingHom ℤ f) (fox_identity v)
  simpa [map_sub, map_sum, map_mul, hι] using h

/-- (1.23): `∂x^n/∂x = x^(n−1) + ⋯ + x + 1`. -/
theorem fox_pow (i : α) (n : ℕ) :
    fox i (FreeGroup.of i ^ n) = ∑ k ∈ Finset.range n, ι (FreeGroup.of i) ^ k := by
  induction n with
  | zero => simp [fox_one]
  | succ n ih =>
    rw [pow_succ, fox_mul, ih, fox_of_self, Finset.sum_range_succ', Finset.sum_mul]
    simp [pow_succ]

/-- (1.24): `∂[x_1, x_2]/∂x_1 = x_2 − [x_1, x_2]`, `[a, b] = a⁻¹ b⁻¹ a b`. -/
theorem fox_commutator_left {a b : α} (hab : a ≠ b) :
    fox a ((FreeGroup.of a)⁻¹ * (FreeGroup.of b)⁻¹ * FreeGroup.of a * FreeGroup.of b)
      = ι (FreeGroup.of b)
        - ι ((FreeGroup.of a)⁻¹ * (FreeGroup.of b)⁻¹ * FreeGroup.of a * FreeGroup.of b) := by
  simp only [fox_mul, fox_of_inv_self, fox_of_inv_ne hab, fox_of_self, fox_of_ne hab, map_mul]
  noncomm_ring

/-- (1.24), corrected: `∂[x_1, x_2]/∂x_2 = 1 − x_2⁻¹ x_1 x_2`. -/
theorem fox_commutator_right {a b : α} (hab : a ≠ b) :
    fox b ((FreeGroup.of a)⁻¹ * (FreeGroup.of b)⁻¹ * FreeGroup.of a * FreeGroup.of b)
      = 1 - ι ((FreeGroup.of b)⁻¹ * FreeGroup.of a * FreeGroup.of b) := by
  simp only [fox_mul, fox_of_inv_self, fox_of_inv_ne hab.symm, fox_of_self, fox_of_ne hab.symm,
    map_mul]
  noncomm_ring

end KuzminHomology.FoxFundamental

end

#print axioms KuzminHomology.FoxFundamental.SemiProd.instGroup
#print axioms KuzminHomology.FoxFundamental.SemiProd.grpHom
#print axioms KuzminHomology.FoxFundamental.IsDerivation.map_one
#print axioms KuzminHomology.FoxFundamental.IsDerivation.map_inv
#print axioms KuzminHomology.FoxFundamental.IsDerivation.ext
#print axioms KuzminHomology.FoxFundamental.IsDerivation.sum_mul_left
#print axioms KuzminHomology.FoxFundamental.isDerivation_sub_one
#print axioms KuzminHomology.FoxFundamental.embed
#print axioms KuzminHomology.FoxFundamental.embed_grp
#print axioms KuzminHomology.FoxFundamental.fox
#print axioms KuzminHomology.FoxFundamental.embed_apply
#print axioms KuzminHomology.FoxFundamental.fox_mul
#print axioms KuzminHomology.FoxFundamental.isDerivation_fox
#print axioms KuzminHomology.FoxFundamental.fox_of
#print axioms KuzminHomology.FoxFundamental.fox_of_self
#print axioms KuzminHomology.FoxFundamental.fox_of_ne
#print axioms KuzminHomology.FoxFundamental.fox_one
#print axioms KuzminHomology.FoxFundamental.fox_inv
#print axioms KuzminHomology.FoxFundamental.fox_of_inv_self
#print axioms KuzminHomology.FoxFundamental.fox_of_inv_ne
#print axioms KuzminHomology.FoxFundamental.eq_fox
#print axioms KuzminHomology.FoxFundamental.fox_identity
#print axioms KuzminHomology.FoxFundamental.fox_identity_values
#print axioms KuzminHomology.FoxFundamental.fox_pow
#print axioms KuzminHomology.FoxFundamental.fox_commutator_left
#print axioms KuzminHomology.FoxFundamental.fox_commutator_right
