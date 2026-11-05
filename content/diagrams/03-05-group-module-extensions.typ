#import "../main-defs.typ": *
// After main-defs: its operator `cd` must not shadow the diagram helper.
#import "common.typ": cd, edge, node

// Proposition 5.4, p. 145: the split homomorphism α: Ḡ → GC factors
// through the embedding ν: Ḡ → GΔ̄_G of Proposition 5.3 by β: GΔ̄_G → GC.
// ν on the upper left of the rising arrow, α on the lower left of the
// falling one, β on the right of the vertical arrow, as printed.
#let split-factorization = cd(
  spacing: (9mm, 4mm),
  node((0, 1), $overline(G)$),
  node((1, 0), $G overline(Delta)_G$),
  node((1, 2), $G C.$),
  edge((0, 1), (1, 0), $nu$, "->", label-side: left),
  edge((0, 1), (1, 2), $alpha$, "->", label-side: right),
  edge((1, 0), (1, 2), $beta$, "->", label-side: left),
)
