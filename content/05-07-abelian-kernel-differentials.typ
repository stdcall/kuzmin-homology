#import "main-defs.typ": *
#import "statements.typ": *
#import "diagrams/05-07-abelian-kernel-differentials.typ": (
  chi-r0-diagram, dk-inclusion-diagram, exterior-pg-diagram,
  pk0-inclusion-diagram, rk-pk0-diagram,
)

#section[О дифференциалах $d^2_(m thin k)$ расширения с абелевым
  ядром] <sec:abelian-kernel-differentials>

Рассмотрим расширение
$ 1 -> A -> G -> B -> 1, $ <eq:torsion-free-kernel-extension>
в котором $A$~— абелева группа без кручения. В этом параграфе мы исследуем
дифференциалы $d^2_(m thin k)$ спектральной последовательности, сходящейся к
гомологиям $H_n G$. Читателю полезно предварительно просмотреть материал
§~@sec:group-module-extensions. Напомним, что там было построено каноническое
вложение произвольного расширения с абелевым ядром в расщепляющееся расширение.
Пусть
$ P_G = Delta_G \/ Delta_G Delta_A, $
где $Delta_A$~— идеал кольца $ZZ G$, порождённый элементами вида $a - 1$
$(a in A)$. Рассмотрим полупрямое произведение $W_G = B P_G$. Тогда отображение
$ g -> b((g - 1) + Delta_G Delta_A) $
($b$~— образ элемента $g in G$ в группе $B$) определяет вложение $nu: G -> W_G$.
Элемент $a in A$ переходит в $((a - 1) + Delta_G Delta_A) in P_G$. Мы будем
отождествлять группу $A$ с её образом в $P_G$. Имеет место точная
последовательность
$ 0 -> A -> P_G -> Delta_B -> 0. $ <eq:pg-exact-sequence>
Сращивая её с последовательностью $0 -> Delta_B -> ZZ B -> ZZ -> 0$, получим
$ 0 -> A -> P_G -> ZZ B -> ZZ -> 0. $ <eq:characteristic-class-sequence>
Класс эквивалентности этой точной последовательности в группе
$Ext_(B)^(2)(ZZ, A)$ называют _характеристическим классом расширения_.

#source(285)Домножим характеристический класс тензорно над $ZZ$ на внешнюю
степень $Lambda^(k)(A)$. Так как $A$~— абелева группа без кручения, имеет место
точная последовательность
$
  0 -> Lambda^(k)(A) times.o A -> Lambda^(k)(A) times.o P_G
  -> Lambda^(k)(A) times.o Delta_B -> 0.
$
Обозначим через $Lambda^(k)(A) and P_G$ факторгруппу тензорного произведения
$Lambda^(k)(A) times.o P_G$ по соотношениям
$ a_1 and dots and a_k times.o a_k = 0 quad (a_i in A). $
Вводя эти соотношения, получим
$
  0 -> Lambda^(k+1)(A) -> Lambda^(k)(A) and P_G
  -> Lambda^(k)(A) times.o Delta_B -> 0.
$ <eq:exterior-pg-sequence>
Композиция с
$
  0 -> Lambda^(k)(A) times.o Delta_B -> Lambda^(k)(A) times.o ZZ B
  -> Lambda^(k)(A) -> 0
$ <eq:exterior-group-ring-sequence>
даёт последовательность
$
  chi_k: 0 -> Lambda^(k+1)(A) -> Lambda^(k)(A) and P_G
  -> Lambda^(k)(A) times.o ZZ B -> Lambda^(k)(A) -> 0.
$ <eq:higher-characteristic-class>
Класс эквивалентности $chi_k$ в группе
$Ext_(B)^(2)(Lambda^(k)(A), Lambda^(k+1)(A))$ назовём _характеристическим
классом $k$-ого порядка_. При $k = 0$ получается обычный характеристический
класс.

Умножение на $chi_k$ определяет гомоморфизмы
$
  chi_(m thin k): H_(m)(B, Lambda^(k)(A)) -> H_(m-2)(B, Lambda^(k+1)(A)).
$
Это~— композиция двух связывающих гомоморфизмов, соответствующих
последовательностям~@eq:exterior-group-ring-sequence и~@eq:exterior-pg-sequence.
Отметим, что первый является изоморфизмом, так как
$Lambda^(k)(A) times.o ZZ B$~— свободный $B$-модуль. В спектральной
последовательности расширения~@eq:torsion-free-kernel-extension, сходящейся к
$H_n G$,
$ E^2_(m thin k) = H_(m)(B, H_(k)(A)) = H_(m)(B, Lambda^(k)(A)), $
поэтому $chi_(m thin k)$ можно переписать в виде
$ chi_(m thin k): E^2_(m thin k) -> E^2_(m-2 thin k+1). $
Сформулируем основной результат этого параграфа.

#theorem[
  #source(286)Пусть $A$~— абелева группа без кручения. Дифференциалы
  $d^2_(m thin k)$ спектральной последовательности
  расширения~@eq:torsion-free-kernel-extension, сходящейся к гомологиям $H_n G$,
  можно представить в виде суммы
  $ d^2_(m thin k) = chi_(m thin k) + overline(d)^2_(m thin k), $
  где $chi_(m thin k)$~— умножение на характеристический класс $k$-ого порядка
  $chi_k$, а $overline(d)^2_(m thin k)$~— дифференциалы спектральной
  последовательности полупрямого произведения $B A$.
] <th:abelian-kernel-d2>

В предыдущем параграфе дифференциалы $overline(d)^2_(m thin k)$ были описаны в
терминах умножения на некоторую точную последовательность. Было доказано, что
образ аннулируется умножением на 2, поэтому, если присоединить $1\/2$, то второе
слагаемое пропадает.

#corollary[
  Дифференциалы $d^2_(m thin k)$ спектральной последовательности, сходящейся к
  $H_(n)(G, ZZ[1\/2])$, совпадают с умножением на $chi_k$.
] <cor:d2-half-coefficients>

Если расширение центрально, то нет надобности присоединять $1\/2$, так как
соответствующее полупрямое произведение превращается в прямое произведение, а в
этом случае дифференциалы $d^r_(m thin k)$ тривиальны.

Пусть $A$~— свободная абелева группа, имеющая базу, инвариантную относительно
действия группы $B$. Тогда дифференциалы $d^2_(m thin k)$ спектральной
последовательности, сходящейся к $H_n G$, также совпадают с умножением на
$chi_k$. Это следует из упражнения~@exc:invariant-basis-splitting
к~§~@sec:split-differentials и теоремы~@th:abelian-kernel-d2.

По предложению~@prop:base-differentials-vanish для полупрямого произведения
дифференциалы, идущие с базы, тривиальны, поэтому частным случаем теоремы
является следующее утверждение.

#corollary[
  Дифференциалы $d^2_(m thin 0)$ спектральной последовательности, сходящейся к
  $H_n G$, совпадают с умножением на характеристический
  класс~@eq:characteristic-class-sequence.
] <cor:d2-base-characteristic-class>

В последнем следствии можно отказаться от предположения о том, что $A$ не имеет
кручения, но мы на этом останавливаться не будем.

Теорема~@th:abelian-kernel-d2~— это версия результата М.~Андре [@bib:Andre1965].
У него, правда, не было подробной информации о втором слагаемом. Описание
первого слагаемого у Андре даётся в терминах $inter$-произведения. Это
эквивалентно нашему подходу, однако для дальнейшего более удобен вариант,
использующий точную последовательность~@eq:higher-characteristic-class.
Изложение следует работе [@bib:Kuzmin1987].

#proof(head: [Доказательство теоремы.], qed: false)[
  #source(287)Дифференциалы $overline(d)^2_(m thin k)$ реализуются как умножение
  на последовательность
  $
    sigma_k: 0 -> Lambda^(k+1)(A) ->^2 Lambda^(k+1)(A) -> D^(k)(A)
    -> Lambda^(k)(A) -> 0,
  $
  — композицию двух коротких точных последовательностей
  теоремы~@th:split-d2-bockstein. Напомним, что $B$-модуль $D^k = D^(k)(A)$
  получается из $Lambda^(k+1)(A) times.o ZZ_2$ добавлением образующих
  $a_1 inter.sq dots inter.sq a_k$, которые знакопеременны, удовлетворяют
  соотношению квазилинейности и на которые $B$ действует диагонально
  (см.~§~@sec:split-differentials). Мы начнём с того, что построим
  последовательность $rho_k$, конгруэнтную сумме $chi_k + sigma_k$. Положим для
  краткости $Lambda^(k)(A) = Lambda^k$ и пусть
  $L_k = Lambda^k and P_G \/ 2 Lambda^(k+1)$. Очевидно, имеют место точные
  последовательности
  $
    & 0 -> Lambda^(k+1) ->^2 Lambda^k and P_G -> L_k -> 0, \
    & 0 -> Lambda^(k+1) times.o ZZ_2 -> L_k -> Lambda^k times.o Delta_B -> 0.
  $
  Определим $B$-модуль $R^k = R^(k)(A)$. Как абелева группа $R^k$ равен прямой
  сумме аддитивных групп модулей $D^k$ и $L_k$ с объединённой подгруппой
  $Lambda^(k+1) times.o ZZ_2$. Будем считать, что $L_k$~— подмодуль в $R^k$, а
  действие группы $B$ на элементы $a_1 inter.sq dots inter.sq a_k in D^k$
  зададим формулой
  $
    (a_1 inter.sq dots inter.sq a_k) b
    = a_1 b inter.sq dots inter.sq a_k b
    + 2 a_1 b and dots and a_k b times.o (b - 1).
  $ <eq:rk-action>
  Второе слагаемое требует пояснений. Имеется естественный эпиморфизм
  $L_k -> Lambda^k times.o Delta_B$. Прообраз
  $a_1 b and dots and a_k b times.o (b - 1)$ в $L_k$ определён с точностью до
  слагаемого из $Lambda^(k+1) times.o ZZ_2$. После умножения на 2 получается
  корректно определённый элемент. Мы оставляем читателю проверку того, что левая
  и правая часть тождества квазилинейности в результате действия $b$ дают одно и
  то же, то есть, что формула~@eq:rk-action согласована с определяющими
  соотношениями. Проверим равенство
  $
    ((a_1 inter.sq dots inter.sq a_k) b) b'
    = (a_1 inter.sq dots inter.sq a_k)(b b').
  $
  Левая часть:
  $
    (a_1 b inter.sq dots inter.sq a_k b
      + 2 a_1 b and dots and a_k b times.o (b - 1)) b' = \
    = a_1 b b' inter.sq dots inter.sq a_k b b'
    + 2 a_1 b b' and dots and a_k b b' times.o (b' - 1) + \
    + 2 a_1 b b' and dots and a_k b b' times.o (b - 1) b'.
  $
  Правая часть:
  $
    a_1 b b' inter.sq dots inter.sq a_k b b'
    + 2 a_1 b b' and dots and a_k b b' times.o (b b' - 1).
  $
  #source(288)Нужное равенство следует из тождества
  $ (b' - 1) + (b - 1) b' = (b b' - 1) quad (b, b' in B). $
  По построению имеет место точная последовательность
  $
    rho_k: 0 -> Lambda^(k+1) ->^2 Lambda^k and P_G -> R^k -> Lambda^k -> 0.
  $
]

#lemma[
  Последовательность $rho_k$ эквивалентна сумме $chi_k + sigma_k$.
] <lem:rho-equivalent-sum>

#proof[
  Рассмотрим модуль $D^k_0$, который получается из $R^k$, если отбросить второе
  слагаемое в равенстве~@eq:rk-action. Можно описать $D^k_0$ как прямую сумму
  $D^k$ и $L_k$ с объединённым подмодулем $Lambda^(k+1) times.o ZZ_2$. В
  частности, $D^k$ содержится в $D^k_0$ в качестве подмодуля. Рассмотрим
  коммутативную диаграмму
  $ #dk-inclusion-diagram $
  где $D^k -> D^k_0$~— вложение. Эта диаграмма устанавливает эквивалентность
  верхней и нижней строки. Рассмотрим также модуль $R^k_0$, который получается
  из $R^k$, если тождество квазилинейности заменить на тождество линейности.
  Аддитивная группа модуля $R^k_0$ представляется в виде прямой суммы
  $Lambda^k plus.o L_k$. Можно построить коммутативную диаграмму
  $ #chi-r0-diagram $
  Гомоморфизм $Lambda^k times.o ZZ B -> R^k_0$ продолжает тождественное
  отображение $Lambda^k times.o 1 -> Lambda^k subset.eq R^k_0$. Продолжение
  существует, поскольку $Lambda^k times.o ZZ B$~— индуцированный модуль.
  Обозначим $sigma'_k$ и $chi'_k$ нижние строки построенных диаграмм. Нам
  достаточно доказать, что $chi'_k + sigma'_k = rho_k$. Рассмотрим короткие
  точные последовательности
  $
     e_k & : Lambda^(k+1) -> Lambda^k and P_G -> L_k, \
     r_k & : L_k -> R^k -> Lambda^k, \
    d'_k & : L_k -> D^k_0 -> Lambda^k, \
    r'_k & : L_k -> R^k_0 -> Lambda^k
  $
  #source(289)\(нули на концах подразумеваются). Докажем, что
  $r_k = r'_k + d'_k$. Сумма определяется как точная последовательность
  $ 0 -> L_k -> hat(R)^k -> Lambda^k -> 0, $
  где $hat(R)^k$ получается из $R^k_0 plus.o D^k_0$ переходом к подмодулю,
  состоящему из пар $(c, d)$ таких, что образы $c$ и $d$ в $Lambda^k$ совпадают,
  и отождествлением подмодулей $L_k subset.eq R^k_0$, $L_k subset.eq D^k_0$.
  Изоморфизм $R^k -> hat(R)^k$ определяется следующим образом. Элемент
  $a_1 inter.sq dots inter.sq a_k$ переходит в пару
  $ (a_1 and dots and a_k, a_1 inter.sq dots inter.sq a_k), $
  а подмодуль $L_k$ отображается тождественно. Наконец, $chi'_k = e_k r'_k$~—
  композиция $e_k$ и $r'_k$. Аналогично, $sigma'_k = e_k d'_k$, поэтому
  $
    chi'_k + sigma'_k = e_k r'_k + e_k d'_k = e_k lr((r'_k + d'_k))
    = e_k r_k = rho_k.
  $
]

Теперь, чтобы доказать теорему, нам достаточно убедиться, что $d^2_(m thin k)$
совпадает с умножением на $rho_k$. Для построения спектральной
последовательности используем вложение
$ G -> W_G = B P_G. $
Если $X -> ZZ$~— произвольная свободная резольвента группы $B$, а
$frak(R)(P_G) -> ZZ$~— стандартная резольвента, то
$X times.o frak(R)(P_G) -> ZZ$~— свободная резольвента для $W_G$, и,
следовательно, для $G$. Группы $H_n G$ изоморфны группам гомологий комплекса
$
  (X times.o (frak(R)(P_G) times.o_A ZZ)) times.o_B ZZ
  tilde.equiv X times.o_B Y,
$
где $Y = frak(R)(P_G) times.o_A ZZ$. Подобную выкладку мы уже несколько раз
проводили в двух предыдущих параграфах. Тензорное произведение $X times.o_B Y$
определяет спектральную последовательность, сходящуюся к $H_n G$. Её
дифференциалы по предложению~@prop:d2-sequence-multiplication можно вычислять
как умножение на последовательность
$
  0 -> H_(k+1)(Y) -> Y_(k+1) \/ B_(k+1) -> C_k -> H_(k)(Y) -> 0
$ <eq:y-boundaries-cycles-sequence>
($C_k, B_k$~— группы циклов и границ комплекса $Y$). Нам достаточно доказать,
что эта последовательность эквивалентна последовательности $rho_k$.

В доказательстве будут нужны некоторые соотношения, выполненные в комплексе $Y$.
Пусть $V_(n)(P_G)$~— свободная абелева группа с базой из элементов
$(c_1, dots, c_n)$, где $c_i in P_G$. Тогда
$frak(R)(P_G) = V(P_G) times.o ZZ P_G$. Так как $P_G \/ A tilde.equiv Delta_B$
(последовательность~@eq:pg-exact-sequence), то
$ Y = frak(R)(P_G) times.o_A ZZ = V(P_G) times.o ZZ Delta_B. $
#source(290)Используем для элементов $c in Delta_B subset.eq ZZ Delta_B$
экспоненциальную форму записи $e^c$. Так как при вложении $G -> B P_G$ элемент
$g$ переходит в $b((g - 1) + Delta_G Delta_A)$ ($b$~— образ $g$ в $B$), то при
индуцированном вложении $B -> B Delta_B$ элемент $b$ переходит в $b e^(b-1)$.
Отсюда следует, что в комплексе $Y$ имеет место равенство
$
  ((c_1, dots, c_n) times.o e^c) b
  = (c_1 b, dots, c_n b) times.o e^(c b + (b - 1)).
$ <eq:y-exponential-action>

#lemma[
  Для любых $a_1, dots, a_n in A, b in B$ в комплексе $Y$
  $
    alt(a_1, dots, a_n) b = alt(a_1 b, dots, a_n b)
    + d(alt(a_1 b, dots, a_n b, a)),
  $
  где $a$~— прообраз элемента $b - 1 in Delta_B$ в модуле $P_G$ ($alt$~—
  альтернирование).
] <lem:alt-action-correction>

#proof[
  В стандартной резольвенте $frak(R)(P_G)$
  $
    d(alt(c_1, dots, c_n))
    = sum_i (-1)^(n-i) alt(c_1, dots, hat(c)_i, dots, c_n)
    times.o (e^(c_i) - 1).
  $
  Это (в других обозначениях)~— равенство~@eq:alt-differential-last-factor,
  справедливое в стандартной резольвенте любой абелевой группы. Из него следует,
  что
  $
    d(alt(a_1 b, dots, a_n b, a))
    = alt(a_1 b, dots, a_n b) times.o (e^(b-1) - 1)
  $
  — все остальные слагаемые сократятся, так как $a_i in A$. Полученный элемент,
  благодаря формуле~@eq:y-exponential-action (при $c = 0$), равен
  $ alt(a_1, dots, a_n) b - alt(a_1 b, dots, a_n b). $
]

#proof(head: none, continued: true)[
  Вернёмся к доказательству теоремы~@th:abelian-kernel-d2. Оно сходно с
  доказательством теоремы~@th:split-d2-bockstein. Прежде всего заменим
  в~@eq:y-boundaries-cycles-sequence гомологии $H_n Y$ на внешние степени
  $ 0 -> Lambda^(k+1) -> Y_(k+1) \/ B_(k+1) -> C_k -> Lambda^k -> 0. $
  Так же, как в следствии~@cor:alt-exterior-iso, при отображении
  $Lambda^(k+1) -> Y_(k+1) \/ B_(k+1)$ произведение $a_1 and dots and a_(k+1)$
  переходит в $alt(a_1, dots, a_(k+1)) + B_(k+1)$.

  Как мы знаем, аддитивную базу группы $Y_n = frak(R)(P_G) times.o_A ZZ$
  образуют элементы
  $ (c_1, dots, c_n) times.o e^c, "где" c_i in P_G, c in Delta_B. $
  Рассмотрим отображение $f: Y -> Lambda(P_G)$, при котором
  $(c_1, dots, c_n) times.o e^c$ переходит в $c_1 and dots and c_n$. Очевидно,
  $ f(alt(c_1, dots, c_n) times.o e^c) = n! c_1 and dots and c_n. $
  #source(291)Это аналог отображения $f$, введённого
  в~§~@sec:split-differentials после следствия~@cor:alt-exterior-iso. Точно так
  же проверяется, что $f$ равно 0 на границах, поэтому имеется индуцированный
  гомоморфизм
  $ phi: Y_(k+1) \/ B_(k+1) -> Lambda^(k+1)(P_G). $
  Аналогом диаграммы~@eq:pk-diagram служит диаграмма
  $ #exterior-pg-diagram $ <eq:exterior-pg-diagram>
  Модуль $P^k$ определяется как фактормодуль $C_k$ по подмодулю $d(Q^(k+1))$,
  где $Q^(k+1) = phi^(-1) lr(((k + 1)! Lambda^(k+1)))$, а
  $psi = phi.alt d phi^(-1)$. Именно такие определения делают диаграмму
  коммутативной. Мы доказали, что $d^2_(m thin k)$ совпадает с умножением на
  последовательность
  $
    0 -> Lambda^(k+1) ->^((k+1)!) Lambda^(k+1)(P_G) ->^psi P^k -> Lambda^k
    -> 0.
  $
  По построению имеет место точная последовательность
  $ 0 -> L'_k -> P^k -> Lambda^k -> 0, $
  где $L'_k = Lambda^(k+1)(P_G) \/ (k + 1)! Lambda^(k+1)$. Точно так же, как
  в~§~@sec:split-differentials, доказывается, что элементы
  $ a_1 inter.sq dots inter.sq a_k = phi.alt(alt(a_1, dots, a_k)) $
  удовлетворяют соотношению
  $
    a_1 inter.sq dots inter.sq (a_i + a'_i) inter.sq dots inter.sq a_k
    = a_1 inter.sq dots inter.sq a_i inter.sq dots inter.sq a_k + \
    + a_1 inter.sq dots inter.sq a'_i inter.sq dots inter.sq a_k
    + (1\/2)(k + 1)! a_1 and dots and a_i and a'_i and dots and a_k.
  $ <eq:pk-pg-quasilinearity>
  Докажем, что
  $
    (a_1 inter.sq dots inter.sq a_k) b = a_1 b inter.sq dots inter.sq a_k b
    + (k + 1)! a_1 b and dots and a_k b times.o (b - 1).
  $ <eq:pk-pg-action>
  Так как $phi.alt$~— гомоморфизм $B$-модулей, достаточно вычислить элемент
  $alt(a_1, dots, a_k) b$. По лемме~@lem:alt-action-correction он равен сумме
  двух слагаемых. Значение $phi.alt$ на первом равно
  $a_1 b inter.sq dots inter.sq a_k b$. Вычислим значение $phi.alt$ на втором,
  учитывая коммутативность диаграммы~@eq:exterior-pg-diagram,
  $
    phi.alt(d(alt(a_1 b, dots, a_k b, a)))
    = psi(phi(alt(a_1 b, dots, a_k b, a))) = \
    = psi((k + 1)! a_1 b and dots and a_k b and a)
    = (k + 1)! a_1 b and dots and a_k b times.o (b - 1)
  $
  (напомним, что $a$~— прообраз $(b - 1)$ в $P_G$)
]

#source(292)Рассмотрим в $P^k$ подгруппу $P^k_0$, порождённую образом
$Lambda^k and P_G$ при отображении $psi$ и элементами
$a_1 inter.sq dots inter.sq a_k$. Из~@eq:pk-pg-action следует, что $P^k_0$
является $B$-подмодулем. Имеется коммутативная диаграмма
$ #pk0-inclusion-diagram $
где средние вертикальные стрелки~— естественные вложения. Таким образом,
последовательность~@eq:y-boundaries-cycles-sequence эквивалентна нижней строке
построенной диаграммы. Имеет место точная последовательность
$ 0 -> L''_k -> P^k_0 -> Lambda^k -> 0, $ <eq:pk0-sequence>
где $L''_k = Lambda^k and P_G \/ (k + 1)! Lambda^(k+1)$. На данный момент наш
результат отличается от требуемого множителем $(k + 1)!$ вместо 2. Рассмотрим в
$P^k_0$ подгруппу $R^k$, порождённую элементами $a_1 inter.sq dots inter.sq a_k$
и $(1\/2)(k + 1)! psi_(0)(Lambda^k and P_G)$. Из~@eq:pk-pg-action следует, что
$R^k$~— подмодуль, а из~@eq:pk-pg-quasilinearity, @eq:pk-pg-action
и~@eq:pk0-sequence, что имеет место точная последовательность
$ 0 -> L_k -> R^k -> Lambda^k -> 0, $
где $L_k = (1\/2)(k + 1)! L''_k
= (1\/2)(k + 1)! Lambda^k and P_G \/ (k + 1)! Lambda^(k+1)$. Так как
$Lambda^k and P_G$ и
$Lambda^k and P_G \/ Lambda^(k+1) = Lambda^k times.o Delta_B$~— группы без
кручения, то для любых $s != 0$ и $t$
$
  s Lambda^k and P_G \/ s t Lambda^(k+1)
  tilde.equiv Lambda^k and P_G \/ t Lambda^(k+1),
$
поэтому $L_k tilde.equiv Lambda^k and P_G \/ 2 Lambda^(k+1)$. Учитывая этот
изоморфизм, получим коммутативную диаграмму
$ #rk-pk0-diagram $
где левая из средних вертикальных стрелок~— умножение на $(1\/2)(k + 1)!$.
Нижняя строка совпадает с нужной последовательностью $rho_k$.
Теорема~@th:abelian-kernel-d2 доказана.#ed-note[При $k = 0$ множитель
  $(1\/2)(k + 1)!$ не целый, и последний шаг доказательства не годится. В этом
  случае по формуле~@eq:pk-pg-action пустое произведение $u in P^0_0$
  удовлетворяет равенству $u b = u + (b - 1)$, поэтому $P^0_0 tilde.equiv ZZ B$
  и нижняя строка первой диаграммы совпадает с $chi_0$; класс $sigma_0$ равен
  нулю, так как $D^0 = A times.o ZZ_2 plus.o ZZ$~— прямая сумма $B$-модулей
  (упражнение~@exc:base-differential-splitting к~§~@sec:split-differentials), и
  по лемме~@lem:rho-equivalent-sum $rho_0$ эквивалентна $chi_0$.]
