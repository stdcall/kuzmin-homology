#set document(
  title: "Гомологическая теория групп",
  author: "Ю. В. Кузьмин",
  date: none,
)
#import "book-style.typ": book-style
#import "main-defs.typ": unnumbered-chapter
#import "frontmatter/cover.typ": cover
#cover()
#show: book-style
#counter(page).update(1)
#import "frontmatter/title.typ": dedication-page, series-page, title-page
#series-page()
#page(header: none, footer: none)[]
#title-page()
#import "frontmatter/publication.typ": publication-page
#publication-page()
#dedication-page()
#unnumbered-chapter(outlined: false)[Оглавление]
#outline(title: none, depth: 2)
#include "00-preface.typ"
#include "01-00-abelian-kernel-extensions.typ"
#include "01-01-group-ring-modules.typ"
#include "01-02-induced-modules.typ"
#include "01-03-modules-and-extensions.typ"
#include "01-04-two-examples.typ"
#include "01-05-split-extensions.typ"
#include "01-06-extension-equivalence.typ"
#include "01-07-automorphisms.typ"
#include "01-08-extension-group.typ"
#include "01-09-fox-derivatives.typ"
#include "01-10-endomorphism-extension.typ"
#include "02-00-group-cohomology.typ"
#include "02-01-cohomology-definition.typ"
#include "02-02-cohomology-resolutions.typ"
#include "02-03-resolutions-presentations.typ"
#include "02-04-free-abelian-cohomology.typ"
#include "02-05-long-exact-sequence.typ"
#include "02-06-dimension-shifting.typ"
#include "02-07-h3-obstructions.typ"
#include "03-00-cohomology-ext.typ"
#include "03-01-ext-sequences.typ"
#include "03-02-injective-resolutions.typ"
#include "03-03-projective-modules.typ"
#include "03-04-free-constructions.typ"
#include "03-05-group-module-extensions.typ"
#include "03-06-free-abelian-kernel-extensions.typ"
#include "03-07-one-relator-cohomology.typ"
#include "03-08-euler-characteristic.typ"
#include "04-00-homology-tor.typ"
#include "04-01-tor-functors.typ"
#include "04-02-homology-definition.typ"
#include "04-03-universal-coefficients.typ"
#include "04-04-h2-relations.typ"
#include "04-05-h2-central-extensions.typ"
#include "04-06-knotted-surface-groups.typ"
#include "04-07-irreducible-c-groups.typ"
#include "04-08-free-quotient-groups.typ"
#include "05-00-extension-homology.typ"
#include "05-01-direct-product-homology.typ"
#include "05-02-semidirect-resolutions.typ"
#include "05-03-spectral-sequences.typ"
#include "05-04-extension-spectral-sequence.typ"
#include "05-05-five-term-sequence.typ"
#include "05-06-split-differentials.typ"
#include "05-07-abelian-kernel-differentials.typ"
#include "06-00-free-abelian-extensions.typ"
#include "06-01-rational-homology.typ"
#include "06-02-free-abelian-spectral-sequence.typ"
#include "06-03-two-lemmas.typ"
#include "06-04-polynomials.typ"
#include "06-05-main-theorem-proof.typ"
#include "80-bibliography.typ"
#include "89-notation.typ"
#include "90-index.typ"
