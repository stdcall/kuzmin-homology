#import "main-defs.typ": reference-rules
#import "statements.typ": numbered-display, unnumbered-display

// The page: 70×100/16 as printed, with the type area of the book.
#let body-margin = (left: 21mm, right: 21mm, top: 25mm, bottom: 21mm)
#let paragraph-indent = 1.5em
#let head-font = "Liberation Sans"

// Chapters, the preface, the contents and the lists at the end begin on a
// right-hand (odd) page, as printed. The cover precedes page 1, so an odd
// page of the book is an even page of the file. A page left empty by the
// break carries neither running head nor folio.
#let recto-break() = {
  metadata((kind: "recto-break", side: "before"))
  pagebreak(weak: true, to: "even")
  metadata((kind: "recto-break", side: "after"))
}
#let blank-page() = {
  let marks(side) = query(metadata.where(value: (
    kind: "recto-break",
    side: side,
  )))
  let befores = marks("before")
  let afters = marks("after")
  let page = here().page()
  range(befores.len()).any(i => {
    let before = befores.at(i).location()
    let after = afters.at(i).location()
    (
      page < after.page()
        and (
          before.page() < page
            or (
              before.page() == page
                and before.position().y <= body-margin.top + 1pt
            )
        )
    )
  })
}
// A page that opens a chapter has neither running head nor folio.
#let opening-page() = {
  query(heading.where(level: 1))
    .map(it => it.location().page())
    .contains(here().page())
}

// "Глава 1. Расширения с абелевым ядром" on even pages with the folio
// outside; "§ 2. Индуцированные модули" on odd pages: the first section
// that begins on the page, or else the section in force. Unnumbered
// chapters (Предисловие, Список литературы) give their title on both.
#let running-header = context {
  if opening-page() or blank-page() { return }
  let here-page = here().page()
  let chapters = query(heading.where(level: 1).before(here()))
  if chapters.len() == 0 { return }
  let chapter = chapters.last()
  let chapter-number = str(counter(heading).at(chapter.location()).first())
  let chapter-head = if chapter.numbering == none { chapter.body } else [
    Глава #chapter-number. #chapter.body
  ]
  let even = calc.even(counter(page).get().first())
  let middle = if even { chapter-head } else {
    let sections = query(heading.where(level: 2)).filter(it => (
      it.location().page() >= chapter.location().page()
        and it.location().page() <= here-page
    ))
    let on-page = sections.find(it => it.location().page() == here-page)
    let section = if on-page != none { on-page } else if sections.len() > 0 {
      sections.last()
    }
    if section == none { chapter-head } else {
      let number = str(counter(heading).at(section.location()).at(1))
      [§~#number. #section.body]
    }
  }
  let folio = counter(page).display()
  set text(font: head-font, size: 8.5pt)
  set par(first-line-indent: 0pt, justify: false)
  block(width: 100%, inset: (bottom: 2.5pt), stroke: (bottom: 0.5pt), grid(
    columns: (2.5em, 1fr, 2.5em),
    align: (left + bottom, center + bottom, right + bottom),
    if even { folio }, middle, if not even { strong(folio) },
  ))
}

// An inline formula taller than the text line takes the room it needs, so
// that it does not run into the neighbouring lines; also used by the
// corrections list.
#let inline-equation(it) = context {
  // Inside a diagram (cd sets the full bounds of the text) a formula keeps
  // its full height, so that arrows meet its indices, not run into them.
  if text.top-edge == "bounds" and text.bottom-edge == "bounds" {
    return box(it)
  }
  // As in TeX, a line is opened up only where the formula would otherwise
  // reach into the lines above or below: above about 0.85em (a fraction, a
  // tall superscript) or more than 0.38em below the baseline.
  let ink = measure({
    set text(top-edge: "bounds", bottom-edge: "bounds")
    it
  })
  let above = measure({
    set text(top-edge: "bounds", bottom-edge: "baseline")
    it
  }).height
  let tall = above > 0.85em.to-absolute()
  let deep = ink.height - above > 0.38em.to-absolute()
  let equation = if tall or deep {
    text(
      top-edge: if tall { "bounds" } else { "cap-height" },
      bottom-edge: if deep { "bounds" } else { "baseline" },
      it,
    )
  } else { it }
  // Keep short inline relations intact at line/page boundaries; long
  // equations retain native mathematical line breaking. Letters joined to
  // a formula ("$G$-модуль") stay on its line.
  if ink.width <= 6em.to-absolute() { box(equation) } else { equation }
  sym.wj
}

// Headings print their formulas bold, as the book does («§ 1. Ext на
// языке последовательностей»); a chapter title is in capitals except its
// formulas («КОГОМОЛОГИИ И ФУНКТОР Ext»).
#let bold-math(body) = {
  show math.equation: it => {
    let parts = if it.body.has("children") { it.body.children } else {
      (it.body,)
    }
    if parts.any(p => p.func() == metadata and p.value == "bold-math") {
      it
    } else {
      math.equation(block: it.block, [#metadata("bold-math")#math.bold(
          it.body,
        )])
    }
  }
  body
}
#let upper-text(body) = {
  if body.func() == math.equation { body } else if body.func() == [].func() {
    body.children.map(upper-text).join()
  } else if body.func() == text { upper(body) } else { body }
}

// Rules of the text and of formulas, shared by the book and the
// corrections sheet.
#let text-math-rules(body) = {
  show regex("т\\. е\\.|т\\. д\\.|т\\. п\\."): it => box(it)
  // A text hyphen following inline math belongs to the preceding symbol.
  show regex("-"): it => [#text("\u{2060}")#it]
  // No line begins with a dash: «Нильсена—Шрайера», «$~— группа».
  show "—": it => [#sym.wj#it]
  // Words inside formulas («— подгруппа в») take the text face, italic
  // where emphasised; STIX Two Math has no Cyrillic.
  show math.equation: set text(font: ("STIX Two Math", "Libertinus Serif"))
  // As in TeX: delimiters keep their size around indices and fractions
  // unless a formula asks for growing ones (`lr(…, size: auto)`); the colon
  // of "f: A -> B" is punctuation; ≥ and ≤ are slanted, as printed.
  set math.lr(size: 1em)
  // An arrow with a label above or below («->^f», «->_(sigma)») stretches
  // under its label, as an extensible arrow in TeX. STIX Two Math assembles
  // ← soundly but → with too little connector overlap, so a long → is a
  // mirrored long ←, as wide as its label plus a little room.
  show math.attach: it => {
    let base = it.base
    let labelled = (
      base.has("text")
        and type(base.text) == str
        and (it.t != none or it.b != none)
    )
    if labelled and base.text == "←" {
      math.attach(math.stretch(base, size: 100% + 0.4em), t: it.t, b: it.b)
    } else if labelled and base.text == "→" {
      context {
        let width(label) = if label == none { 0pt } else {
          measure(math.equation(math.script(label))).width
        }
        let natural = measure(math.equation(sym.arrow.r)).width
        let size = calc.max(
          natural,
          calc.max(width(it.t), width(it.b)) + 0.4em.to-absolute(),
        )
        let arrow = box(scale(x: -100%, math.equation(
          math.stretch(sym.arrow.l, size: size),
        )))
        math.class("relation", math.attach(
          math.limits(arrow),
          t: it.t,
          b: it.b,
        ))
      }
    } else { it }
  }
  show math.equation: it => {
    show ":": math.class("punctuation", ":")
    show "≥": sym.gt.eq.slant
    show "≤": sym.lt.eq.slant
    // Emphasised words inside a formula («— _подгруппа в_») in the italic
    // of the text face; STIX Two Math has no Cyrillic italic.
    show emph: e => text(font: "Libertinus Serif", style: "italic", e.body)
    it
  }
  show math.equation.where(block: false): inline-equation
  body
}

#let book-style(body) = {
  set page(
    width: 170mm,
    height: 240mm,
    margin: body-margin,
    numbering: "1",
    header: running-header,
    header-ascent: 30%,
    footer: none,
  )
  set text(font: "Libertinus Serif", size: 11pt, lang: "ru")
  set par(
    justify: true,
    leading: 0.58em,
    spacing: 0.58em,
    first-line-indent: paragraph-indent,
  )
  set heading(numbering: (..numbers) => {
    let n = numbers.pos()
    if n.len() == 1 { "Глава " + str(n.first()) + "." } else {
      "§ " + str(n.last()) + "."
    }
  })
  show heading.where(level: 1): it => {
    recto-break()
    let numbered = it.numbering != none
    if numbered {
      context [#metadata((
        kind: "numbered",
        family: "heading",
        level: 1,
        number: (counter(heading).at(it.location()).first(),),
      ))<numbered>]
    }
    set par(first-line-indent: 0pt, justify: false)
    block(width: 100%, above: 28mm, below: 16mm, align(center, {
      if numbered {
        let number = context str(counter(heading).at(it.location()).first())
        text(size: 15pt, tracking: 0.45em, [ГЛАВА #number])
        v(2.5mm)
        line(length: 50mm, stroke: 0.6pt)
        v(7mm)
      }
      text(size: 16pt, weight: "bold", bold-math(upper-text(it.body)))
    }))
  }
  show heading.where(level: 2): it => {
    if it.numbering != none {
      context [#metadata((
        kind: "numbered",
        family: "heading",
        level: 2,
        number: counter(heading).at(it.location()).slice(0, 2),
      ))<numbered>]
    }
    set par(first-line-indent: 0pt, justify: false)
    block(
      width: 100%,
      above: 2.4em,
      below: 1.3em,
      sticky: true,
      align(center, text(size: 11.5pt, weight: "bold", {
        if it.numbering != none {
          let number = context str(counter(heading).at(it.location()).at(1))
          [§~#number.#h(0.5em)]
        }
        bold-math(it.body)
      })),
    )
  }
  show: text-math-rules
  show math.equation.where(block: true): set block(above: 0.9em, below: 0.9em)
  show math.equation.where(block: true): it => {
    let children = if it.body.has("children") { it.body.children } else {
      (it.body,)
    }
    let fitted = children.any(child => (
      child.func() == metadata
        and child.value.at("kind", default: none) == "fitted-equation"
    ))
    if fitted { it } else if (
      it.has("label") and str(it.label).starts-with("eq:")
    ) {
      numbered-display(it)
    } else { unnumbered-display(it) }
  }
  // Lists «1) … 2) …» as printed: upright numbers also inside italic
  // statements, the items indented.
  set enum(indent: 1.5em, numbering: (..n) => text(
    style: "normal",
    numbering("1)", ..n),
  ))
  set list(indent: 1.5em)
  // Figures stand apart from their neighbours; captions in smaller type.
  show figure: set block(above: 1.6em, below: 1.6em)
  show figure.caption: set text(size: 0.9em)
  // A list with its own pattern («1.», «а)») keeps upright numbers too.
  show enum: it => if type(it.numbering) == str {
    let fields = it.fields()
    let children = fields.remove("children")
    let pattern = fields.remove("numbering")
    enum(
      ..fields,
      numbering: (..n) => text(style: "normal", numbering(pattern, ..n)),
      ..children,
    )
  } else { it }
  show: reference-rules
  // The contents as printed: chapters in bold with their page, sections
  // indented under them with leaders.
  set outline(indent: 0pt)
  show outline.entry.where(level: 1): it => block(
    above: 1.2em,
    below: 0.5em,
    breakable: false,
    sticky: true,
    {
      set text(weight: "bold")
      link(it.element.location(), grid(
        columns: (1fr, auto),
        column-gutter: 1em,
        bold-math(if it.prefix() != none [#it.prefix()#h(
            0.5em,
          )#it.body()] else { it.body() }),
        it.page(),
      ))
    },
  )
  show outline.entry.where(level: 2): it => block(
    above: 0.45em,
    below: 0.45em,
    breakable: false,
    link(it.element.location(), pad(left: 1.4em, par(
      first-line-indent: 0pt,
      hanging-indent: 2.6em,
      justify: false,
      [#box(width: 2.6em, it.prefix())#it.body()#box(
          width: 1fr,
          it.fill,
        )#it.page()],
    ))),
  )
  body
}
