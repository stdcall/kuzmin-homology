// The front board of the cloth binding: gold lettering on navy cloth, the
// author in red, the publisher's script mark at the foot.
#let cover() = {
  let navy = rgb("223150")
  let gold = rgb("d2ad60")
  let red = rgb("d23c30")
  let line-at(dy, body) = place(top + center, dy: dy, block(
    width: 140mm,
    align(center, body),
  ))
  page(
    width: 170mm,
    height: 240mm,
    margin: 0mm,
    fill: navy,
    numbering: none,
    header: none,
    footer: none,
  )[
    #set text(
      font: "Libertinus Serif",
      fill: gold,
      lang: "ru",
      hyphenate: false,
    )
    #set par(first-line-indent: 0pt, spacing: 0pt, justify: false)
    #line-at(29mm, text(size: 11.5pt, weight: "semibold", tracking: 0.02em)[
      #smallcaps[Advanced Studies in Mathematics and Mechanics]
    ])
    #line-at(40mm, text(size: 33pt, weight: "bold", tracking: 0.01em)[
      ГОМОЛОГИЧЕСКАЯ
    ])
    #line-at(57mm, text(size: 33pt, weight: "bold", tracking: 0.01em)[
      ТЕОРИЯ ГРУПП
    ])
    #place(top + center, dy: 77mm, line(length: 132mm, stroke: 0.9pt + gold))
    #line-at(86mm, text(
      size: 18pt,
      weight: "bold",
      tracking: 0.06em,
      fill: red,
    )[Ю. В. КУЗЬМИН])
    #line-at(199mm, text(size: 30pt, style: "italic")[Факториал])
  ]
}
