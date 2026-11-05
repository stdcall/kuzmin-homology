#import "../main-defs.typ": *
// After main-defs: its operator `cd` must not shadow the diagram helper.
#import "common.typ": grid-diagram

// Definition 6.1: the extensions E_1, E_2 of G by A joined by an isomorphism
// f of the middle groups; the vertical maps id_A, f, id_G, their labels on
// the right.
#let equivalence-diagram = grid-diagram(
  (
    ($1$, $A$, $overline(G)_1$, $G$, $1$),
    ($1$, $A$, $overline(G)_2$, $G$, $1$),
  ),
  down: ((none, (label: $id_A$), (label: $f$), (label: $id_G$), none),),
  gap: 7mm,
)

// Formula (1.9): the isomorphism f: G_n -> G_(-n) of §6 between the
// extensions E_n and E_(-n), with tau(a) = a^(-1) on the kernel; the maps
// mu_(+-n), sigma_(+-n) labelled above the arrows of both rows, the vertical
// maps tau, f, id_G on the right.
#let inversion-diagram = grid-diagram(
  (
    ($1$, $A$, $G_n$, $G$, $1$),
    ($1$, $A$, $G_(-n)$, $G$, $1,$),
  ),
  across: (
    ("->", (label: $mu_n$), (label: $sigma_n$), "->"),
    ("->", (label: $mu_(-n)$), (label: $sigma_(-n)$), "->"),
  ),
  down: ((none, (label: $tau$), (label: $f$), (label: $id_G$), none),),
  gap: 7mm,
  row: 10mm,
)
