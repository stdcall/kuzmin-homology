import Mathlib.NumberTheory.LegendreSymbol.QuadraticChar.Basic
import Mathlib.GroupTheory.Coset.Card

/-!
# Proposition 7.7 of Chapter 4: `x₁² + x₂²` takes a non-zero non-square value in `F_q`

Kuzmin, *Гомологическая теория групп* (Homological Group Theory), Chapter 4, § 7,
proof of Proposition 7.7 (`prop:psl-irreducible-c-group`), case `m = 1`, printed
p. 229.  The proof reduces `det c = -1` for a matrix `c` of the form
(`eq:negacyclic-matrix`) to a product of factors `α_k² - b_k² β_k²` with
independent `α_k, β_k ∈ F_q` and `b_k² ∈ F_q^*`, and says that it suffices to show:
for every fixed non-zero `e ∈ F_q` the quadratic form `x₁² + e x₂²` takes every
value in `F_q` (here `q` is odd).  With `x₂ = 0` one gets the squares; if `e` is
not a square, `x₁ = 0` gives the non-squares; if `e` is a square, the form reduces
to `x₁² + x₂²`.  If every `x₁² + x₂²` were a square, the squares together with
zero would form a subfield with `(q + 1)/2` elements, which is impossible since
`q` and `(q + 1)/2` are coprime.  Hence `x₁² + x₂² ∈ F_q^* ∖ (F_q^*)²` for some
pair (as corrected; printed: `x₁² + x₂² ∉ (F_q^*)²`), and proportional pairs give
the rest of the coset `F_q^* ∖ (F_q^*)²`.

Notation: the field `F_q` is `F` with `Fintype.card F = q`, and "`q` odd" is
`Odd (Fintype.card F)`.  "`a` is a square in `F_q`" is `IsSquare a`
(`a = r * r` for some `r : F`, so `0` is a square); `(F_q^*)²` is
`{a | a ≠ 0 ∧ IsSquare a}`, and `F_q^* ∖ (F_q^*)²` is `{a | a ≠ 0 ∧ ¬IsSquare a}`.

Formalised here, for a finite field `F`:

* `ringChar_ne_two`: `q` odd implies that the characteristic is not `2`;
* `nsmul_isSquare` and `squaresSubfield`: if every sum of two squares is a
  square, then the squares (with `0`) are closed under addition, hence under
  negation (`-a = (q - 1) • a`), and form a subfield of `F`;
* `two_mul_card_squares`: for `q` odd there are exactly `(q + 1)/2` squares
  (with `0`), stated as `2 * #squares = q + 1`;
* `coprime_half_succ`: for `q` odd, `(q + 1)/2` and `q` are coprime;
* `exists_sq_add_sq_not_isSquare`: for `q` odd some `x₁² + x₂²` is not a square
  (the book's argument: otherwise `squaresSubfield` has `(q + 1)/2` elements, its
  order divides `q` by Lagrange's theorem for the additive groups, and the
  coprimality forces `q = 1`);
* `exists_sq_add_sq_ne_zero_not_isSquare`: the corrected statement,
  `x₁² + x₂² ∈ F_q^* ∖ (F_q^*)²` for some `x₁, x₂`;
* `isSquare_mul_of_not_isSquare`: the product of two non-squares is a square;
* `exists_sq_add_sq_eq_of_not_isSquare`: proportional pairs give every element of
  `F_q^* ∖ (F_q^*)²` as `x₁² + x₂²`;
* `sq_add_mul_sq_surjective`: for `q` odd and `e ≠ 0` the form `x₁² + e x₂²`
  takes every value in `F_q`, by the three cases of the book;
* `exists_sq_sub_mul_sq_eq_neg_one`: the form in the shape used for the factors
  of `det c`: for `d ≠ 0` (in the book `d = b_k²`) there are `α, β` with
  `α² - d β² = -1`;
* `isSquare_sq_add_sq_of_char_two`: for `q` even every `x₁² + x₂²` is a square,
  so the hypothesis "`q` odd" cannot be dropped.

The printed condition `x₁² + x₂² ∉ (F_q^*)²` is too weak for the next step:

* `exists_sq_add_sq_eq_zero`: for `q ≡ 1 (mod 4)` (then `-1` is a square) there
  are non-zero `x₁, x₂` with `x₁² + x₂² = 0`;
* `printed_condition_insufficient`: such a pair satisfies the printed condition
  (`0 ∉ (F_q^*)²`), but all pairs proportional to it give the value `0`, so they
  do not give the coset `F_q^* ∖ (F_q^*)²`;
* `zmod_five_example`: the instance `q = 5`: `1² + 2² = 0` in `F_5`, every pair
  `(t, 2 t)` gives `0`, while `2 ∈ F_5^* ∖ (F_5^*)²`.

Not covered: the reduction of `det c = -1` to these forms (the eigenvectors
`u_k`, the `2 × 2` blocks, the formula `det c = ∏ (α_k² - b_k² β_k²)`, the
independence of `α_k, β_k`), the case of odd `m > 1` and the rest of the proof of
Proposition 7.7; these steps are checked numerically for small `q` in
`checks/sage/chapter-4b.py` (`section_7_psl_construction`, `section_7_negacyclic`),
where `section_7_forms` also checks the statements formalised here for odd
`q ≤ 49`.
-/

namespace KuzminHomology.FiniteFieldNonsquare

variable {F : Type*} [Field F] [Fintype F]

/-- For `q` odd the characteristic of `F_q` is not `2`. -/
theorem ringChar_ne_two (hq : Odd (Fintype.card F)) : ringChar F ≠ 2 := fun h =>
  by simpa [FiniteField.even_card_iff_char_two.mp h] using Nat.odd_iff.mp hq

omit [Fintype F] in
/-- If every sum of two squares is a square, then every multiple `n • a` of a
square `a` is a square. -/
theorem nsmul_isSquare (h : ∀ x₁ x₂ : F, IsSquare (x₁ ^ 2 + x₂ ^ 2)) {a : F}
    (ha : IsSquare a) (n : ℕ) : IsSquare (n • a) := by
  induction n with
  | zero => simp
  | succ n ih =>
    obtain ⟨r, hr⟩ := ih
    obtain ⟨u, hu⟩ := ha
    rw [succ_nsmul, hr, hu]
    simpa [sq] using h r u

/-- The book's subfield: if every `x₁² + x₂²` is a square, then the squares of
`F_q` together with zero form a subfield. -/
def squaresSubfield (h : ∀ x₁ x₂ : F, IsSquare (x₁ ^ 2 + x₂ ^ 2)) : Subfield F where
  carrier := {a | IsSquare a}
  mul_mem' ha hb := ha.mul hb
  one_mem' := IsSquare.one
  add_mem' := by
    rintro a b ⟨r, rfl⟩ ⟨u, rfl⟩
    simpa [sq] using h r u
  zero_mem' := IsSquare.zero
  neg_mem' := by
    intro a ha
    have hq : 1 ≤ Fintype.card F := Fintype.card_pos
    have key : -a = (Fintype.card F - 1) • a := by
      rw [neg_eq_iff_add_eq_zero, add_comm, ← succ_nsmul, Nat.sub_add_cancel hq, nsmul_eq_mul,
        FiniteField.cast_card_eq_zero, zero_mul]
    rw [key]
    exact nsmul_isSquare h ha _
  inv_mem' := by
    rintro a ⟨r, rfl⟩
    exact ⟨r⁻¹, by rw [mul_inv]⟩

/-- For `q` odd, `F_q` has `(q + 1)/2` squares (zero included). -/
theorem two_mul_card_squares (hq : Odd (Fintype.card F)) :
    2 * Nat.card {a : F // IsSquare a} = Fintype.card F + 1 := by
  classical
  have hF := ringChar_ne_two hq
  set T := Finset.univ.filter (fun a : F => IsSquare a) with hT
  set U := Finset.univ.filter (fun a : F => ¬IsSquare a) with hU
  have hcard : Nat.card {a : F // IsSquare a} = T.card := by
    rw [Nat.card_eq_fintype_card, Fintype.card_subtype]
  -- the quadratic character sums to zero: `(#T - 1) - #U = 0`
  have hsum := quadraticChar_sum_zero hF
  rw [← Finset.sum_filter_add_sum_filter_not Finset.univ (fun a : F => IsSquare a), ← hT,
    ← hU] at hsum
  have h0T : (0 : F) ∈ T := Finset.mem_filter.mpr ⟨Finset.mem_univ _, IsSquare.zero⟩
  have h1 : ∑ a ∈ T, quadraticChar F a = (T.card : ℤ) - 1 := by
    have : ∑ a ∈ T, quadraticChar F a = ∑ a ∈ T, (1 - if a = 0 then 1 else 0) := by
      refine Finset.sum_congr rfl fun a ha => ?_
      by_cases h0 : a = 0
      · simp [h0]
      · simp only [h0, ite_false, sub_zero]
        exact (quadraticChar_one_iff_isSquare h0).mpr (Finset.mem_filter.mp ha).2
    rw [this, Finset.sum_sub_distrib]
    simp [h0T]
  have h2 : ∑ a ∈ U, quadraticChar F a = -(U.card : ℤ) := by
    have : ∑ a ∈ U, quadraticChar F a = ∑ a ∈ U, (-1 : ℤ) := by
      refine Finset.sum_congr rfl fun a ha => ?_
      exact quadraticChar_neg_one_iff_not_isSquare.mpr (Finset.mem_filter.mp ha).2
    rw [this]
    simp
  have hc : T.card + U.card = Fintype.card F := by
    rw [hT, hU, Finset.card_filter_add_card_filter_not, Finset.card_univ]
  rw [h1, h2] at hsum
  rw [hcard]
  omega

/-- For `q` odd, `(q + 1)/2` and `q` are coprime. -/
theorem coprime_half_succ {q : ℕ} (hq : Odd q) : Nat.Coprime ((q + 1) / 2) q := by
  obtain ⟨k, rfl⟩ := hq
  have hk : (2 * k + 1 + 1) / 2 = k + 1 := by omega
  rw [hk, Nat.Coprime, ← Nat.dvd_one]
  have h1 : Nat.gcd (k + 1) (2 * k + 1) ∣ 2 * (k + 1) :=
    (Nat.gcd_dvd_left _ _).mul_left 2
  have h2 : Nat.gcd (k + 1) (2 * k + 1) ∣ 2 * k + 1 := Nat.gcd_dvd_right _ _
  have h3 : 2 * (k + 1) = (2 * k + 1) + 1 := by ring
  rw [h3] at h1
  exact (Nat.dvd_add_right h2).mp h1

/-- The book's argument: for `q` odd not every `x₁² + x₂²` is a square in `F_q`. -/
theorem exists_sq_add_sq_not_isSquare (hq : Odd (Fintype.card F)) :
    ∃ x₁ x₂ : F, ¬IsSquare (x₁ ^ 2 + x₂ ^ 2) := by
  by_contra! h
  let K := squaresSubfield h
  have hK : 2 * Nat.card K = Fintype.card F + 1 := two_mul_card_squares hq
  have hdvd : Nat.card K ∣ Fintype.card F := by
    rw [← Nat.card_eq_fintype_card]
    exact AddSubgroup.card_addSubgroup_dvd_card K.toAddSubgroup
  have hK' : Nat.card K = (Fintype.card F + 1) / 2 := by omega
  have h1 : Nat.card K = 1 :=
    Nat.Coprime.eq_one_of_dvd (hK' ▸ coprime_half_succ hq) hdvd
  have h2 : 1 < Fintype.card F := Fintype.one_lt_card
  omega

/-- The corrected statement of p. 229: for `q` odd,
`x₁² + x₂² ∈ F_q^* ∖ (F_q^*)²` for some pair `(x₁, x₂)`. -/
theorem exists_sq_add_sq_ne_zero_not_isSquare (hq : Odd (Fintype.card F)) :
    ∃ x₁ x₂ : F, x₁ ^ 2 + x₂ ^ 2 ≠ 0 ∧ ¬IsSquare (x₁ ^ 2 + x₂ ^ 2) := by
  obtain ⟨x₁, x₂, h⟩ := exists_sq_add_sq_not_isSquare hq
  exact ⟨x₁, x₂, fun h0 => h (h0 ▸ IsSquare.zero), h⟩

/-- In a finite field the product of two non-squares is a square. -/
theorem isSquare_mul_of_not_isSquare {a b : F} (ha : ¬IsSquare a) (hb : ¬IsSquare b) :
    IsSquare (a * b) := by
  classical
  have ha0 : a ≠ 0 := fun h => ha (h ▸ IsSquare.zero)
  have hb0 : b ≠ 0 := fun h => hb (h ▸ IsSquare.zero)
  refine (quadraticChar_one_iff_isSquare (mul_ne_zero ha0 hb0)).mp ?_
  rw [map_mul, quadraticChar_neg_one_iff_not_isSquare.mpr ha,
    quadraticChar_neg_one_iff_not_isSquare.mpr hb]
  norm_num

/-- Proportional pairs: for `q` odd every element of `F_q^* ∖ (F_q^*)²` is a
value of `x₁² + x₂²`; the pair is `λ (y₁, y₂)` for the pair `(y₁, y₂)` of
`exists_sq_add_sq_ne_zero_not_isSquare`. -/
theorem exists_sq_add_sq_eq_of_not_isSquare (hq : Odd (Fintype.card F)) {c : F}
    (hc : ¬IsSquare c) : ∃ x₁ x₂ : F, x₁ ^ 2 + x₂ ^ 2 = c := by
  obtain ⟨y₁, y₂, hs0, hs⟩ := exists_sq_add_sq_ne_zero_not_isSquare hq
  obtain ⟨r, hr⟩ := isSquare_mul_of_not_isSquare hc hs
  set s := y₁ ^ 2 + y₂ ^ 2 with hsdef
  refine ⟨r * y₁ / s, r * y₂ / s, ?_⟩
  have : (r * y₁ / s) ^ 2 + (r * y₂ / s) ^ 2 = r * r * s / (s * s) := by
    rw [hsdef]; field_simp
  rw [this, ← hr]
  field_simp

/-- The claim the case `m = 1` is reduced to: for `q` odd and `e ≠ 0` the
quadratic form `x₁² + e x₂²` takes every value in `F_q`. -/
theorem sq_add_mul_sq_surjective (hq : Odd (Fintype.card F)) {e : F} (he : e ≠ 0) (c : F) :
    ∃ x₁ x₂ : F, x₁ ^ 2 + e * x₂ ^ 2 = c := by
  -- `x₂ = 0` gives the squares
  by_cases hc : IsSquare c
  · obtain ⟨r, rfl⟩ := hc
    exact ⟨r, 0, by ring⟩
  -- `e` a square: reduction to `x₁² + x₂²`
  by_cases he' : IsSquare e
  · obtain ⟨u, rfl⟩ := he'
    have hu : u ≠ 0 := fun h => he (by rw [h, mul_zero])
    obtain ⟨y₁, y₂, hy⟩ := exists_sq_add_sq_eq_of_not_isSquare hq hc
    refine ⟨y₁, y₂ / u, ?_⟩
    rw [← hy]
    field_simp
  -- `e` not a square: `x₁ = 0` gives the non-squares
  · obtain ⟨r, hr⟩ := isSquare_mul_of_not_isSquare hc he'
    refine ⟨0, r / e, ?_⟩
    have : (0 : F) ^ 2 + e * (r / e) ^ 2 = r * r / e := by
      rw [zero_pow two_ne_zero, zero_add]
      field_simp
    rw [this, ← hr]
    field_simp

/-- The form as it occurs in the factors `α_k² - b_k² β_k²` of `det c`: for `q` odd
and `d ≠ 0` there are `α, β ∈ F_q` with `α² - d β² = -1`. -/
theorem exists_sq_sub_mul_sq_eq_neg_one (hq : Odd (Fintype.card F)) {d : F} (hd : d ≠ 0) :
    ∃ α β : F, α ^ 2 - d * β ^ 2 = -1 := by
  obtain ⟨α, β, h⟩ := sq_add_mul_sq_surjective hq (neg_ne_zero.mpr hd) (-1)
  exact ⟨α, β, by rw [← h]; ring⟩

/-- For `q` even every element of `F_q` is a square, so the hypothesis "`q` odd"
is needed. -/
theorem isSquare_sq_add_sq_of_char_two (hF : ringChar F = 2) (x₁ x₂ : F) :
    IsSquare (x₁ ^ 2 + x₂ ^ 2) :=
  FiniteField.isSquare_of_char_two hF _

/-- For `q ≡ 1 (mod 4)` the value `0` is taken at a pair of non-zero elements. -/
theorem exists_sq_add_sq_eq_zero (h4 : Fintype.card F % 4 = 1) :
    ∃ x₁ x₂ : F, x₁ ≠ 0 ∧ x₂ ≠ 0 ∧ x₁ ^ 2 + x₂ ^ 2 = 0 := by
  obtain ⟨r, hr⟩ := FiniteField.isSquare_neg_one_iff.mpr (by omega : Fintype.card F % 4 ≠ 3)
  have hr0 : r ≠ 0 := by
    rintro rfl
    simp at hr
  exact ⟨1, r, one_ne_zero, hr0, by rw [one_pow, pow_two r, ← hr]; ring⟩

/-- The printed condition `x₁² + x₂² ∉ (F_q^*)²` does not give the coset
`F_q^* ∖ (F_q^*)²`: for `q ≡ 1 (mod 4)` it holds for a pair of non-zero elements
all of whose proportional pairs give the value `0`. -/
theorem printed_condition_insufficient (h4 : Fintype.card F % 4 = 1) :
    ∃ x₁ x₂ : F, x₁ ≠ 0 ∧ x₂ ≠ 0 ∧ ¬(x₁ ^ 2 + x₂ ^ 2 ≠ 0 ∧ IsSquare (x₁ ^ 2 + x₂ ^ 2)) ∧
      ∀ t : F, (t * x₁) ^ 2 + (t * x₂) ^ 2 = 0 := by
  obtain ⟨x₁, x₂, h₁, h₂, h0⟩ := exists_sq_add_sq_eq_zero h4
  refine ⟨x₁, x₂, h₁, h₂, fun h => h.1 h0, fun t => ?_⟩
  rw [mul_pow, mul_pow, ← mul_add, h0, mul_zero]

/-- The instance `q = 5`: `1² + 2² = 0` in `F_5`, the pairs `(t, 2 t)` give only
`0`, and `2` is a non-zero non-square of `F_5`. -/
theorem zmod_five_example :
    (1 : ZMod 5) ^ 2 + 2 ^ 2 = 0 ∧ (∀ t : ZMod 5, (t * 1) ^ 2 + (t * 2) ^ 2 = 0) ∧
      (2 : ZMod 5) ≠ 0 ∧ ¬IsSquare (2 : ZMod 5) := by
  refine ⟨by decide, by decide, by decide, ?_⟩
  unfold IsSquare
  decide

end KuzminHomology.FiniteFieldNonsquare

#print axioms KuzminHomology.FiniteFieldNonsquare.ringChar_ne_two
#print axioms KuzminHomology.FiniteFieldNonsquare.nsmul_isSquare
#print axioms KuzminHomology.FiniteFieldNonsquare.squaresSubfield
#print axioms KuzminHomology.FiniteFieldNonsquare.two_mul_card_squares
#print axioms KuzminHomology.FiniteFieldNonsquare.coprime_half_succ
#print axioms KuzminHomology.FiniteFieldNonsquare.exists_sq_add_sq_not_isSquare
#print axioms KuzminHomology.FiniteFieldNonsquare.exists_sq_add_sq_ne_zero_not_isSquare
#print axioms KuzminHomology.FiniteFieldNonsquare.isSquare_mul_of_not_isSquare
#print axioms KuzminHomology.FiniteFieldNonsquare.exists_sq_add_sq_eq_of_not_isSquare
#print axioms KuzminHomology.FiniteFieldNonsquare.sq_add_mul_sq_surjective
#print axioms KuzminHomology.FiniteFieldNonsquare.exists_sq_sub_mul_sq_eq_neg_one
#print axioms KuzminHomology.FiniteFieldNonsquare.isSquare_sq_add_sq_of_char_two
#print axioms KuzminHomology.FiniteFieldNonsquare.exists_sq_add_sq_eq_zero
#print axioms KuzminHomology.FiniteFieldNonsquare.printed_condition_insufficient
#print axioms KuzminHomology.FiniteFieldNonsquare.zmod_five_example
