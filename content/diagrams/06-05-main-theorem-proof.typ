#import "../main-defs.typ": *
// After main-defs: its operator `cd` must not shadow the diagram helper.
#import "common.typ": edge, grid-diagram

// Proof of the claims (a)–(c), n = p, p. 333: the Frobenius map of the
// sequence 0 → Δ → R → Z_p → 0 into 0 → R^p_1 → R^p → Z_p → 0.; all
// arrows unlabelled, the vertical maps down under Δ and R, a two-headed
// vertical arrow ↕ between the two copies of Z_p.
#let frobenius-augmentation-diagram = grid-diagram(
  (
    ($0$, $Delta$, $R$, $ZZ_p$, $0$),
    ($0$, $R^p_1$, $R^p$, $ZZ_p$, $0.$),
  ),
  down: ((none, "->", "->", "<->", none),),
  gap: 6mm,
  row: 9mm,
)

// Second case n/p = 1 mod p, p. 334: the exact sequence
// 0 → Δ^(n-p+1) → R^n_(n-2p+1)/R^n_(n-p+2) → R^(n-p)_(n-2p+1) → 0 above the
// split sequence 0 → Δ^(n-p+1) → Δ^(n-p+1) ⊕ φ(Δ^(n/p-1)) → φ(Δ^(n/p-1))
// → 0.; all arrows unlabelled; a two-headed vertical arrow ↕ between the
// copies of Δ^(n-p+1), the other vertical maps upwards.
#let second-case-diagram = grid-diagram(
  (
    (
      $0$,
      $Delta^(n-p+1)$,
      $R^n_(n-2p+1) \/ R^n_(n-p+2)$,
      $R^(n-p)_(n-2p+1)$,
      $0$,
    ),
    (
      $0$,
      $Delta^(n-p+1)$,
      $Delta^(n-p+1) plus.o phi(Delta^(n\/p-1))$,
      $phi(Delta^(n\/p-1))$,
      $0.$,
    ),
  ),
  down: ((none, "<->", "<-", "<-", none),),
  gap: 6mm,
  row: 9mm,
)

// Proof of (c), third case, p. 336: the Frobenius map of the sequence
// 0 → R^(n/p)_((n-p^s)/p+1) → R^(n/p) → R^(n/p)/R^(n/p)_((n-p^s)/p+1) → 0.
// (bottom row) into 0 → R^n_(n-p^s+1) → R^n → R^n/R^n_(n-p^s+1) → 0 (top
// row); all arrows unlabelled, the vertical maps upwards.
#let frobenius-section-diagram = grid-diagram(
  (
    (
      $0$,
      $R^n_(n-p^s+1)$,
      $R^n$,
      $R^n \/ R^n_(n-p^s+1)$,
      $0$,
    ),
    (
      $0$,
      $R^(n\/p)_((n-p^s)\/p+1)$,
      $R^(n\/p)$,
      $R^(n\/p) \/ R^(n\/p)_((n-p^s)\/p+1)$,
      $0.$,
    ),
  ),
  down: ((none, "<-", "<-", "<-", none),),
  gap: 6mm,
  row: 9mm,
)

// Proof of Lemma 5.15, p. 337: the long exact sequences of (6.30) (top)
// and (6.31) (bottom) around the connecting homomorphisms; each row begins
// with an arrow from nothing and ends with an arrow to nothing, all row
// arrows unlabelled. Vertical maps down: α and β with their labels on the
// right, the third one unlabelled.
#let connecting-mod-p-diagram = grid-diagram(
  (
    (
      none,
      $H_(m+1)(B, A'')$,
      $H_(m)(B, A')$,
      $H_(m)(B, A)$,
      none,
    ),
    (
      none,
      $H_(m+1)(B, A'' times.o ZZ_p)$,
      $H_(m)(B, A' times.o ZZ_p)$,
      $H_(m)(B, A times.o ZZ_p)$,
      none,
    ),
  ),
  down: ((none, (label: $alpha$), (label: $beta$), "->", none),),
  extra: (
    edge((0, 0), (1, 0), "->"),
    edge((0, 1), (1, 1), "->"),
    edge((3, 0), (4, 0), "->"),
    edge((3, 1), (4, 1), "->"),
  ),
  gap: 6mm,
  row: 9mm,
)
