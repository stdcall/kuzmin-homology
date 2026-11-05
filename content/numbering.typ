// Chapters and sections are headings of levels 1 and 2: counter(heading)
// gives (chapter, section). As in the book, the statements of all kinds
// share one counter in a section (Предложение 2.3, Следствие 2.4), the
// formulas count through a chapter ((1.1), (1.2)), and the exercises
// restart in each section. chapter() and section() of main-defs.typ reset
// them.
#let statements = counter("book-statement")
#let formulas = counter("book-formula")
#let exercise-numbers = counter("book-exercise")
#let series-counter = counter("book-series")
#let statement-families = (
  "th",
  "lem",
  "prop",
  "cor",
  "def",
  "exm",
  "rem",
  "con",
  "q",
)
#let family-counter(family) = if family in statement-families {
  statements
} else if family == "eq" { formulas } else if family == "exc" {
  exercise-numbers
} else { counter("numbered:" + family) }
// (chapter, section) at a location; 0 before the first section.
#let place-key(location) = {
  let levels = counter(heading).at(location)
  (levels.at(0, default: 0), levels.at(1, default: 0))
}
// Primed formulas, "(3.24′)": the label of the primed formula maps to the
// label of its base formula.
#let formula-primes = (:)
// A record keeps the chapter in every number; the printed number of a
// statement is section.number (2.3), of a formula chapter.number (1.1), of an
// exercise its number in the section.
#let object-number(family, location, tag: none, prime: none) = {
  let own = if tag != none { tag } else {
    family-counter(family).at(location).first()
  }
  if prime != none and prime != false {
    let base = query(selector(<numbered>).within(prime))
    assert(base.len() == 1, message: "A prime formula needs its base formula")
    own = str(base.first().value.number.last()) + "′"
  }
  let (chapter, section) = place-key(location)
  if family in ("bib", "tab", "fig") { (own,) } else if family == "eq" {
    (chapter, own)
  } else { (chapter, section, own) }
}
// The number as the book prints it.
#let printed-number(family, number) = if type(number.last()) == str {
  number.last()
} else if family in statement-families {
  number.slice(-2).map(str).join(".")
} else if family in ("exc", "bib", "tab", "fig") { str(number.last()) } else {
  number.map(str).join(".")
}
// The number of a formula as printed, "1.1" (without the parentheses).
#let formula-number(location, prime: none) = {
  object-number("eq", location, prime: prime).map(str).join(".")
}
#let record-number(record) = record.value.number
#let numbered-record(target) = {
  let found = query(target)
  if found.len() != 1 { return none }
  query(selector(<numbered>).within(target)).at(0, default: none)
}
#let record(family, ..flags) = context [#metadata((
  kind: "numbered",
  family: family,
  number: object-number(family, here(), ..flags.named()),
))<numbered>]
