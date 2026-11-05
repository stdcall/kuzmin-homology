#import "../main-defs.typ": *
// After main-defs: its operator `cd` must not shadow the diagram helper.
#import "common.typ": edge, grid-diagram

// §5, the connecting homomorphisms do not depend on the resolution: the
// connecting maps ∂'_(n-1), ∂_(n-1) of the resolutions X', X labelled above
// the rows, the isomorphisms γ_(n-1), γ_n on the right of the vertical maps;
// the period after the last object ends the sentence.
#let connecting-naturality = grid-diagram(
  (
    ($H^(n-1)(Hom(X', A''))$, $H^(n)(Hom(X', A'))$),
    ($H^(n-1)(Hom(X, A''))$, $H^(n)(Hom(X, A')).$),
  ),
  across: ((label: $partial'_(n-1)$), (label: $partial_(n-1)$)),
  down: (((label: $gamma_(n-1)$), (label: $gamma_n$)),),
  gap: 9mm,
  row: 7mm,
)

// §5, a morphism of short exact sequences of G-modules A → B; the arrows
// are unlabelled.
#let coefficient-morphism = grid-diagram(
  (
    ($0$, $A'$, $A$, $A''$, $0$),
    ($0$, $B'$, $B$, $B''$, $0.$),
  ),
  down: ((none, "->", "->", "->", none),),
  gap: 7mm,
  row: 7mm,
)

// §5, the induced morphism of the long exact sequences: each row begins and
// ends with an arrow from and to an empty place, as printed; the arrows are
// unlabelled.
#let long-sequence-morphism = grid-diagram(
  (
    (none, $H^(n-1)(G, A'')$, $H^(n)(G, A')$, $H^(n)(G, A)$, $H^(n)(G, A'')$),
    (none, $H^(n-1)(G, B'')$, $H^(n)(G, B')$, $H^(n)(G, B)$, $H^(n)(G, B'')$),
  ),
  down: ((none, "->", "->", "->", "->"),),
  extra: (0, 1)
    .map(y => (
      edge((0, y), (1, y), "->"),
      edge((4, y), (5, y), "->"),
    ))
    .flatten(),
  gap: 5mm,
  row: 7mm,
)

// §5, the commutative diagram of cochain complexes Hom_G(X, -) with exact
// rows; the vertical maps are unlabelled, the comma ends the clause.
#let hom-complex-morphism = grid-diagram(
  (
    ($0$, $Hom_(G)(X, A')$, $Hom_(G)(X, A)$, $Hom_(G)(X, A'')$, $0$),
    ($0$, $Hom_(G)(X, B')$, $Hom_(G)(X, B)$, $Hom_(G)(X, B'')$, $0,$),
  ),
  down: ((none, "->", "->", "->", none),),
  gap: 6mm,
  row: 7mm,
)
