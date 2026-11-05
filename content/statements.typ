#import "numbering.typ": series-counter
#import "numbering.typ": (
  exercise-numbers, family-counter, formula-number, formula-primes,
  object-number, printed-number, record,
)
#import "main-defs.typ": reference-rules
#let sequence = [].func()
#let join-pieces(pieces) = sequence(
  pieces
    .map(it => if it.func() == sequence and not it.has("label") {
      it.children
    } else { (it,) })
    .flatten(),
)
#let keep-label(original, rebuilt) = {
  if original.has("label") [#rebuilt#original.label] else { rebuilt }
}

// Put `head` at the start of the first paragraph of `body`.
#let prepend-heading(body, head) = {
  if (
    body.func() in (table, grid, figure, list, enum, terms)
      or (
        body.func() == math.equation and body.block
      )
  ) {
    (
      block(above: 0pt, below: 0.95em, sticky: true, {
        set par(first-line-indent: 0pt)
        par(head)
      })
        + body
    )
  } else if body.func() == block {
    let fields = body.fields()
    let inner = fields.remove("body")
    block(prepend-heading(inner, head), ..fields)
  } else if body.func() == sequence and body.children.len() > 0 {
    let children = body.children
    let first = children.position(it => (
      it.func()
        not in (
          [ ].func(),
          parbreak,
        )
    ))
    if first == none { join-pieces((head, body)) } else {
      keep-label(body, join-pieces((
        ..children.slice(0, first),
        prepend-heading(children.at(first), head),
        ..children.slice(first + 1),
      )))
    }
  } else { head + body }
}

// Put `ending` after the last word or formula of `body`.
#let append-ending(body, ending) = {
  if body.func() == math.equation and body.block {
    // A display does not span the line by itself; widen it so that the mark
    // stands at the right margin on the display's last line.
    // The display keeps room at the right for the mark, as for a formula
    // number (unnumbered-display), so that a wide formula does not run
    // into it.
    // The wrapper takes the spacing of a display (book-style.typ).
    block(width: 100%, above: 0.9em, below: 0.9em, {
      place(bottom + right, ending)
      math.equation(block: true, [#metadata((kind: "qed-display"))#body.body])
    })
  } else if body.func() in (block, box) {
    let fields = body.fields()
    let inner = fields.remove("body")
    body.func()(append-ending(inner, ending), ..fields)
  } else if body.func() == sequence and body.children.len() > 0 {
    let children = body.children
    let last = children
      .rev()
      .position(it => it.func() not in ([ ].func(), parbreak))
    if last == none { join-pieces((body, ending)) } else {
      let index = children.len() - last - 1
      keep-label(body, join-pieces((
        ..children.slice(0, index),
        append-ending(children.at(index), ending),
        ..children.slice(index + 1),
      )))
    }
  } else { body + ending }
}

// A statement or a proof is a run of ordinary paragraphs, not a block of its
// own, so that Typst's paragraph indent works as in the book. Its first
// paragraph starts at the left margin, as printed ("Предложение 2.3.",
// "Доказательство."); later paragraphs of the statement and the paragraph
// after it are indented as usual, and text that continues a sentence after a
// display stays flush left.
#let flush-first(body, indent: 0pt) = {
  let styled(it) = {
    set par(first-line-indent: (amount: indent, all: true))
    it
  }
  let breaks(it) = (
    it.func() in (parbreak, block, grid, table, figure, list, enum, terms)
      or (it.func() == math.equation and it.block)
  )
  if body.func() == sequence and body.children.len() > 0 {
    let end = body.children.position(breaks)
    if end == none { styled(body) } else {
      join-pieces((
        styled(join-pieces(body.children.slice(0, end))),
        ..body.children.slice(end),
      ))
    }
  } else { styled(body) }
}

// The space around a statement is the paragraph spacing and a little more.
// It is weak and collapses with the paragraph spacing and with the space of
// a neighbouring statement, so two statements in a row are as far apart as
// a statement and a paragraph, not twice as far. A proof follows its
// statement at this distance; the text after a proof goes on at the usual
// paragraph spacing, as printed.
#let statement-space = context v(par.spacing + 0.45em, weak: true)
// After a statement the book goes on at the left margin («Обычно
// расширение…» after Определение 3.1); a block of no size ends the chain
// of paragraphs without space of its own. After a proof the next
// paragraph is indented as usual.
// A statement is a block: its space collapses with that of its
// neighbours (a statement, a proof, a display at its end), and the
// paragraph after it begins at the margin. A proof stays a run of
// paragraphs, so that the text after it is indented.
#let statement-gap = 0.58em + 0.45em
#let statement-block(body, after: true) = {
  if after {
    block(
      width: 100%,
      above: statement-gap,
      below: statement-gap,
      breakable: true,
      flush-first(body),
    )
  } else {
    statement-space
    flush-first(body)
    parbreak()
  }
}

// Whether `body` ends with a display formula.
#let ends-with-display(body) = {
  if body.func() == math.equation { return body.block }
  if body.func() == sequence {
    let rest = body.children.filter(it => (
      it.func()
        not in (
          [ ].func(),
          parbreak,
          metadata,
        )
    ))
    return rest.len() > 0 and ends-with-display(rest.last())
  }
  if body.has("child") { return ends-with-display(body.child) }
  false
}
// Typst does not indent a paragraph after a display; the book indents the
// paragraph after a proof that ends with one («Естественно считать…» on
// p. 36). An empty paragraph without spacing restores the chain.
#let paragraph-resume = {
  par(spacing: 0pt)[]
  context v(-par.spacing)
}

// An italic statement: also the words inside its formulas («где», «и»)
// are italic, as printed; they take the text face, STIX Two Math has no
// Cyrillic italic.
#let italic-body(body) = {
  show math.equation: it => {
    show regex("\p{Cyrillic}+"): t => text(
      font: "Libertinus Serif",
      style: "italic",
      t,
    )
    it
  }
  text(style: "italic", body)
}

#let statement(
  kind,
  family,
  body,
  numbered: true,
  title: none,
  italic: true,
  spaced: false,
  series: false,
) = {
  // `series: true`: a separate series of the section («Пример 1.» …
  // «Пример 4.» of § 5.3) outside the common counter; a reference prints
  // the number of the series.
  if series { series-counter.step() } else if numbered {
    family-counter(family).step()
  }
  // `spaced: true`: the head letterspaced and light, «П р и м е р.», as the
  // book prints some unnumbered examples and remarks.
  // A spaced head letterspaces the word only: «П р и м е р 1.».
  let word = if spaced { text(tracking: 0.22em, kind) } else { kind }
  let shape(body) = if spaced { body } else { strong(body) }
  let head = context {
    let number = if series {
      let n = str(series-counter.get().first())
      record(family, tag: n)
      n
    } else if numbered {
      record(family)
      printed-number(family, object-number(family, here()))
    }
    shape[
      #word#if number != none [ #number]#if title != none [ (#title)].
    ]
    [ ]
  }
  if italic { body = italic-body(body) }
  statement-block(prepend-heading(body, head))
}
// A claim the book prints as an italic block of its own, without a head.
#let claim(body) = statement-block(italic-body(body))
#let theorem(body, ..args) = statement("Теорема", "th", body, ..args)
#let lemma(body, ..args) = statement("Лемма", "lem", body, ..args)
#let proposition(body, ..args) = statement(
  "Предложение",
  "prop",
  body,
  ..args,
)
#let corollary(body, ..args) = statement("Следствие", "cor", body, ..args)
#let definition(body, ..args) = statement("Определение", "def", body, ..args)
#let example(body, ..args) = statement("Пример", "exm", body, ..args)
#let remark(body, ..args) = statement(
  "Замечание",
  "rem",
  body,
  italic: false,
  ..args,
)

// "Д о к а з а т е л ь с т в о." spaced out, and the end mark □ after the
// last word. A proof that the book opens without a head ("Действительно,
// …") passes `head: none`; `qed: false` leaves out the mark.
#let qed-mark = [~$square$]
#let proof-head = [Доказательство.]
// `continued: true`: the rest of a proof after an inserted lemma, an
// ordinary indented paragraph without the space of a statement
// («Закончим доказательство теоремы…»).
#let proof(body, head: proof-head, qed: true, continued: false) = {
  let display-end = ends-with-display(body)
  if qed { body = append-ending(body, qed-mark) }
  let body = prepend-heading(body, if head == none { [] } else {
    (
      {
        // Only the word «Доказательство» is letterspaced («Доказательство
        // леммы.»), as printed.
        show "Доказательство": it => text(tracking: 0.22em, it)
        head
      }
        + [ ]
    )
  })
  if continued {
    flush-first(body, indent: 1.5em)
    parbreak()
  } else { statement-block(body, after: false) }
  if display-end { paragraph-resume }
}

// A new paragraph after a display formula, indented as the book prints it;
// plain text after a display continues the sentence at the margin.
#let new-par(body) = {
  par(first-line-indent: (amount: 1.5em, all: true), body)
  parbreak()
}

// Exercises close a section: "Упражнения" and the numbered items, the
// number hanging in the left margin of the item. An exercise is labelled
// when the text refers to it.
#let exercises(body) = {
  block(above: 1.8em, below: 1.1em, sticky: true, strong[Упражнения])
  body
}
#let exercise-indent = 2.2em
#let exercise(body) = {
  exercise-numbers.step()
  let head = context {
    record("exc")
    box(width: 0pt, move(dx: -exercise-indent, box(
      width: exercise-indent - 0.5em,
      align(right)[#exercise-numbers.get().first().],
    )))
  }
  // Full width, so that short lines are justified; the paragraphs of an
  // exercise begin at its margin, as printed.
  block(
    width: 100%,
    above: 1.1em,
    below: 1.1em,
    breakable: true,
    inset: (left: exercise-indent),
    {
      set par(first-line-indent: 0pt)
      prepend-heading(body, head)
    },
  )
}

// A figure with its caption «Рис. 1.» under it; the figures are numbered
// through the book, a reference prints the number.
#let book-figure(body, caption: none) = {
  family-counter("fig").step()
  figure(
    [#record("fig")#body],
    caption: context [Рис.~#object-number("fig", here()).last().#if (
        caption != none
      ) [ #caption]],
    numbering: none,
    supplement: none,
    kind: "book-figure",
  )
}

#let bib-group(body) = heading(level: 2, numbering: none, outlined: false, body)
// "[12] Бурбаки Н. …": the number in a column of its own, the lines of the
// record after the first under its text, a little space between records.
#let bib-number-width = 2.4em
#let bib-entry(body) = {
  family-counter("bib").step()
  context block(width: 100%, above: 0.85em, below: 0.85em, par(
    first-line-indent: 0pt,
    hanging-indent: bib-number-width,
    [#record("bib")#box(
        width: bib-number-width,
      )[\[#object-number("bib", here()).last()\]]#body],
  ))
}

#let fit-display(body, numbered: false, prime: none) = layout(size => context {
  let tag = [(#formula-number(here(), prime: prime))]
  let reserve = if numbered { 2 * measure(tag).width + 10pt } else { 0pt }
  let available = size.width - reserve
  let formula = math.equation(block: false, math.display(body))
  let width = measure(reference-rules(formula, trace: false)).width
  metadata((kind: "equation-scale", factor: calc.min(1, available / width)))
  if width > available {
    scale(available / width * 100%, reflow: true, formula)
  } else { formula }
})

#let numbered-display(it) = {
  let prime = formula-primes.at(str(it.label), default: none)
  math.equation(
    block: true,
    numbering: _ => context [(#formula-number(here(), prime: prime))],
    [#metadata((kind: "fitted-equation"))#family-counter("eq").update(n => (
        n + (if prime != none { 0 } else { 1 })
      ))#record("eq", prime: prime)#fit-display(
        it.body,
        numbered: true,
        prime: prime,
      )],
  )
}

#let unnumbered-display(it) = {
  let parts = if it.body.has("children") { it.body.children } else {
    (it.body,)
  }
  let qed = parts.any(p => (
    p.func() == metadata and p.value.at("kind", default: none) == "qed-display"
  ))
  math.equation(
    block: true,
    [#metadata((kind: "fitted-equation"))#fit-display(
        it.body,
        numbered: qed,
      )],
  )
}
