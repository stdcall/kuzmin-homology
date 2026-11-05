#import "../main-defs.typ": *
// After main-defs: its operator `cd` must not shadow the diagram helper.
#import "common.typ": ladder

// Exercise 3.4: a morphism f: F_1 → F_2 of the copresentations G = F_1/N_1
// and G = F_2/N_2. The rows are the exact sequences 1 → N_i → F_i → G → 1;
// the vertical maps stand under N, F and G (the one under N unlabelled, then
// f and id_G), labelled on their right as printed.
#let copresentation-morphism = ladder(
  ($1$, $N_1$, $F_1$, $G$, $1$),
  ($1$, $N_2$, $F_2$, $G$, $1$),
  (none, [], $f$, $id_G$, none),
  down-side: right,
)
