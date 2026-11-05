#import "../main-defs.typ": source

#let front-page(body) = page(header: none, footer: none, {
  set par(first-line-indent: 0pt, justify: false)
  body
})

// Page 1: the series page.
#let series-page() = front-page[
  #source(1)
  #align(center)[
    #v(10mm)
    #text(size: 11.5pt, tracking: 0.04em)[
      ADVANCED STUDIES IN MATHEMATICS AND MECHANICS
    ]
    #v(4mm)
    _Series Editors_
    #v(4mm)
    #text(size: 11.5pt, tracking: 0.04em)[A. T. FOMENKO#h(1.2em)A. V. MIKHALEV]
    #v(9mm)
    Vol.#h(0.8em)1.
    #v(12mm)
    _Yu. V. Kuzmin_#h(2.5em)Homological Group Theory [_Russian ed._]
  ]
]

// Page 3: the title page.
#let title-page() = front-page[
  #source(3)
  #align(center)[
    #v(14mm)
    #text(size: 11pt, tracking: 0.04em)[
      ADVANCED STUDIES IN MATHEMATICS AND MECHANICS
    ]
    #v(4mm)
    _Выпуск_ 1.
    #v(42mm)
    #text(size: 18pt)[Ю. В. Кузьмин]
    #v(1mm)
    #line(length: 45mm, stroke: 0.6pt)
    #v(10mm)
    #text(size: 25pt, weight: "bold")[ГОМОЛОГИЧЕСКАЯ\ ТЕОРИЯ ГРУПП]
    #v(1fr)
    #text(size: 12pt)[Москва\ ФАКТОРИАЛ ПРЕСС\ 2006]
    #v(8mm)
  ]
]

// Page 5: the dedication.
#let dedication-page() = front-page[
  #source(5)
  #v(42mm)
  #align(right, text(size: 13pt, style: "italic")[Памяти моих родителей])
]
