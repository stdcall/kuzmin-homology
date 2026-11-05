#import "../main-defs.typ": *
// After main-defs: its operator `cd` must not shadow the diagram helper.
#import "common.typ": grid-diagram

// §7, uniqueness of the pull-back: an extension E'_2 of G_2 by A mapped to
// E_1 over f: G_2 → G_1. The names of the rows stand on their left; μ, σ,
// μ_1, σ_1 are labelled above the arrows, id, φ, f on the right of the
// vertical maps; the comma ends the clause.
#let pullback-uniqueness = grid-diagram(
  (
    ($E'_2:$, $1$, $A$, $overline(G)$, $G_2$, $1$),
    ($E_1:$, $1$, $A$, $overline(G)_1$, $G_1$, $1,$),
  ),
  across: (
    (none, "->", (label: $mu$), (label: $sigma$), "->"),
    (none, "->", (label: $mu_1$), (label: $sigma_1$), "->"),
  ),
  down: ((none, none, (label: $id$), (label: $phi$), (label: $f$), none),),
  gap: 6mm,
  row: 11mm,
)

// Formula (2.42): the extension E_2 of G by B over the extension E_1 of G by
// A; the names of the rows on their left, the vertical maps f, (unlabelled),
// id labelled on their right.
#let pullback-module-diagram = grid-diagram(
  (
    ($E_2:$, $1$, $B$, $overline(G)_2$, $G$, $1$),
    ($E_1:$, $1$, $A$, $overline(G)_1$, $G$, $1.$),
  ),
  across: ((none, "->", "->", "->", "->"), (none, "->", "->", "->", "->")),
  down: ((none, none, (label: $f$), "->", (label: $id$), none),),
  gap: 6mm,
  row: 7mm,
)

// §7, the pull-back E_ϕ of the extension Θ along the outer action ϕ: G → Φ;
// the names of the rows on their left, the vertical maps id, (unlabelled),
// ϕ labelled on their right.
#let outer-action-pullback = grid-diagram(
  (
    ($E_phi.alt:$, $1$, $Inn A$, $overline(G)_phi.alt$, $G$, $1$),
    ($Theta:$, $1$, $Inn A$, $overline(Phi)$, $Phi$, $1.$),
  ),
  across: ((none, "->", "->", "->", "->"), (none, "->", "->", "->", "->")),
  down: ((none, none, (label: $id$), "->", (label: $phi.alt$), none),),
  gap: 6mm,
  row: 7mm,
)

// §7, the extension Ḡ/Z(A) of G by Inn A over Θ; the vertical maps id,
// (unlabelled), ϕ labelled on their right.
#let center-quotient-diagram = grid-diagram(
  (
    ($1$, $Inn A$, $overline(G) \/ Z(A)$, $G$, $1$),
    ($1$, $Inn A$, $overline(Phi)$, $Phi$, $1$),
  ),
  down: ((none, (label: $id$), "->", (label: $phi.alt$), none),),
  gap: 6mm,
  row: 7mm,
)
