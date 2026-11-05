#import "../main-defs.typ": *
// After main-defs: its operator `cd` must not shadow the diagram helper.
#import "common.typ": ladder

// Proof of Theorem 7.1, p. 163: the presentation 1 → N → F → G → 1 mapped
// into 1 → N* → F* → G* → 1; all maps unlabelled, the vertical maps under
// N, F and G only.
#let one-relator-extension-diagram = ladder(
  ($1$, $N$, $F$, $G$, $1$),
  ($1$, $N^*$, $F^*$, $G^*$, $1$),
  (none, [], [], [], none),
)
