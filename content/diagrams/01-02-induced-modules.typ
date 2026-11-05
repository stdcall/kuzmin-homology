#import "../main-defs.typ": *
// After main-defs: its operator `cd` must not shadow the diagram helper.
#import "common.typ": cd, edge, node

// Proposition 2.1: the embedding of A into the induced module A ⊗ ZG and
// the homomorphism f: A → A' of abelian groups; the G-module homomorphism
// A ⊗ ZG → A' makes the triangle commute.
#let induced-universal = cd(
  spacing: (9mm, 4mm),
  node((1, 0), $A$),
  node((0, 1), $A times.o ZZ G$),
  node((1, 2), $A'$),
  edge((1, 0), (0, 1), "->"),
  edge((0, 1), (1, 2), "->"),
  edge((1, 0), (1, 2), $f$, "->", label-side: left),
)

// Proposition 2.3: the epimorphism Hom(ZG, A) → A (the value at 1) and the
// homomorphism f: A' → A of abelian groups; the G-module homomorphism
// A' → Hom(ZG, A) makes the triangle commute.
#let coinduced-universal = cd(
  spacing: (9mm, 4mm),
  node((1, 0), $A$),
  node((0, 1), $Hom(ZZ G, A)$),
  node((1, 2), $A'$),
  edge((0, 1), (1, 0), "->"),
  edge((1, 2), (0, 1), "->"),
  edge((1, 2), (1, 0), $f$, "->", label-side: right),
)
