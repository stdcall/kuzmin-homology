#import "../main-defs.typ": *
// After main-defs: its operator `cd` must not shadow the diagram helper.
#import "common.typ": cd, edge, ladder, node

// Proof of Proposition 4.1 (the Hopf formula), p. 194: N/[N, F] → F/F' on
// top, M ⊗_G Z → P ⊗_G Z below; the left map goes down, the right one up;
// all maps unlabelled, as printed.
#let hopf-formula-square = cd(
  spacing: (9mm, 6mm),
  node((0, 0), $N \/ [N, F]$),
  node((1, 0), $F \/ F'$),
  node((0, 1), $M times.o_G ZZ$),
  node((1, 1), $P times.o_G ZZ$),
  edge((0, 0), (1, 0), "->"),
  edge((0, 0), (0, 1), "->"),
  edge((1, 1), (1, 0), "->"),
  edge((0, 1), (1, 1), "->"),
)

// Proof of Theorem 4.7, p. 201: the extensions 0 → C' → E_k/E_(k+1) → K' → 0
// and 0 → C → G_k/G_(k+1) → K → 0; the vertical maps under C', E_k/E_(k+1)
// and K', induced by E → G, unlabelled. The comma after the last 0 as
// printed.
#let stallings-ladder = ladder(
  ($0$, $C'$, $E_k \/ E_(k+1)$, $K'$, $0$),
  ($0$, $C$, $G_k \/ G_(k+1)$, $K$, $0,$),
  (none, [], [], [], none),
)
