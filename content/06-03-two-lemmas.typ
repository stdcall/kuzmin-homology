#import "main-defs.typ": *
#import "statements.typ": *

#section[Две леммы] <sec:two-lemmas>

Мы сохраним обозначения предыдущего параграфа. Остались недоказанными
леммы~@lem:torsion-in-image и~@lem:tor-circle-product.

Докажем лемму~@lem:tor-circle-product. Формулировка:
$s^2 Tor_(m)^(B)(D, Delta^(s-1) compose Delta) = 0$ для любого $B$-модуля $D$
$(m > 0, s > 1)$.

Как и раньше, пусть $R = ZZ B$. Рассмотрим точную последовательность
$ 0 -> Delta^(s-1) compose Delta -> R^(s-1) compose R -> L_s -> 0 $
(по определению $L_s$~— коядро соответствующего отображения). Нам достаточно
доказать следующие два утверждения.

#enum(numbering: "(i)")[
  $ s Tor_(m)^(B)(D, R^(s-1) compose R) = 0, $
][
  $ Tor_(m)^(B)(D, L_s) tilde.equiv Tor_(m)^(B)(D, Delta^(s-1) times.o ZZ_s). $
]

#proof(head: none, continued: true)[
  Докажем (i). По определению модуля $R^(s-1) compose R$ имеет место точная
  последовательность
  $ 0 -> R^s -> R^(s-1) times.o R -> R^(s-1) compose R -> 0. $
  Так как $R^(s-1) times.o R$~— свободный $B$-модуль, то для $m > 1$
  $ Tor_(m)^(B)(D, R^(s-1) compose R) tilde.equiv Tor_(m-1)^(B)(D, R^s) $
  и можно воспользоваться предложением~@prop:exterior-power-induced (с заменой
  $P$ на $R$ и $k$ на $s$). При $m = 1$
  $
    Tor_(1)^(B)(D, R^(s-1) compose R) tilde.equiv
    Ker(R^s times.o_B D ->^(alpha times.o 1) (R^(s-1) times.o R) times.o_B D),
  $
  где $alpha$~— альтернирование. Определён гомоморфизм $beta times.o 1$, идущий
  в обратном направлении, где $beta: R^(s-1) times.o R -> R^s$~— естественное
  отображение. Композиция этих отображений совпадает с умножением на $s$,
  поэтому $s Ker alpha = 0$.
]

#proof(head: none, continued: true)[
  #source(310)Чтобы доказать (ii), рассмотрим модуль
  $R^(s-1) times.o R \/ Delta^(s-1) times.o Delta$. Как абелева группа он
  представляется в виде прямой суммы трёх слагаемых
  $
    (Delta^(s-1) times.o ZZ) plus.o (Delta^(s-2) times.o ZZ times.o Delta)
    plus.o (Delta^(s-2) times.o ZZ times.o ZZ).
  $ <eq:tensor-quotient-decomposition>
  Интересующий нас модуль $L_s$ получается из этого модуля введением соотношений
  альтернирования
  $
    sum_(t=s)^(1) (-1)^(s-t) r_1 and dots and hat(r_t) and dots and r_s
    times.o r_t = 0 quad (r_i in R).
  $ <eq:alternation-relations>
  Это соотношение линейно, поэтому его достаточно ввести в следующих случаях,
  соответствующих разложению~@eq:tensor-quotient-decomposition
  #enum(numbering: "1)")[
    $r_1, dots, r_(s-1) in Delta, r_s = 1$;
  ][
    $r_1, dots, r_(s-2) in Delta, r_(s-1) = 1, r_s in Delta$;
  ][
    $r_1, dots, r_(s-2) in Delta, r_(s-1) = r_s = 1$.
  ]
  Для элементов типа 3) все слагаемые в~@eq:alternation-relations равны нулю,
  кроме двух, которые соответствуют значениям $t = s$ и $t = s - 1$. Соотношение
  превращается в равенство
  $
    r_1 and dots and r_(s-2) and 1 times.o 1
    - r_1 and dots and r_(s-2) and 1 times.o 1 = 0,
  $
  выполненное тождественно. Элементы типов 1) и 2) отличаются перестановкой двух
  последних аргументов. Но левая часть соотношения~@eq:alternation-relations
  кососимметрична, поэтому мы можем ограничиться лишь элементами первого типа.
  Для них в~@eq:alternation-relations одно слагаемое имеет тип 1), а все
  остальные~— тип 2), то есть это соотношение удаляет прямое слагаемое
  $Delta^(s-1) times.o ZZ$. Мы видим, что
  $
    L_s tilde.equiv (Delta^(s-2) times.o ZZ times.o Delta)
    plus.o (Delta^(s-2) times.o ZZ times.o ZZ)
  $
  — изоморфизм абелевых групп. Нетрудно проверить, что соответствующая точная
  последовательность
  $
    0 -> Delta^(s-2) times.o ZZ times.o Delta -> L_s
    -> Delta^(s-2) times.o ZZ times.o ZZ -> 0
  $ <eq:ls-sequence>
  является последовательностью $B$-модулей. Например, в $L_s$
  $
    (r_1 and dots and r_(s-2) times.o 1 times.o r_s) b
    = r_1 b and dots and r_(s-2) b times.o 1 times.o r_s b,
  $
  то есть $Delta^(s-2) times.o ZZ times.o Delta$~— подмодуль. Рассмотрим точную
  последовательность
  $
    0 -> Delta^(s-2) times.o Delta -> Delta^(s-2) times.o R -> Delta^(s-2)
    -> 0.
  $ <eq:delta-induced-sequence>
  #source(311)В~@eq:ls-sequence и~@eq:delta-induced-sequence подмодули изоморфны
  и фактормодули изоморфны. В то же время средний член
  последовательности~@eq:delta-induced-sequence~— индуцированный модуль.
  Естественно рассмотреть отображение $f: Delta^(s-2) times.o R -> L_s$,
  продолжающее изоморфизм абелевых групп
  $Delta^(s-2) -> Delta^(s-2) times.o ZZ times.o ZZ$. Легко проверить, что $f$
  индуцирует изоморфизм фактормодулей
  $Delta^(s-2) tilde.equiv Delta^(s-2) times.o ZZ times.o ZZ$. Вычислим $f$ на
  подмодуле $Delta^(s-2) times.o Delta$. Пусть $r_i in Delta$
  $(i = 1, dots, s - 1)$. Докажем, что
  $f(r_1 and dots and r_(s-2) times.o r_(s-1))$ является образом в $L_s$
  следующего элемента модуля $R^(s-1) times.o R \/ Delta^(s-1) times.o Delta$
  $
    r_1 and dots and r_(s-2) and r_(s-1) times.o 1
    + r_1 and dots and r_(s-2) and 1 times.o r_(s-1).
  $ <eq:f-preimage-element>
  В силу линейности достаточно рассмотреть случай $r_(s-1) = b - 1$ $(b in B)$.
  Тогда
  $
    & r_1 and dots and r_(s-2) times.o (b - 1) = \
    & quad = (r_1 b^(-1) and dots and r_(s-2) b^(-1) times.o 1) b
      - r_1 and dots and r_(s-2) times.o 1 ->^f \
    & quad quad ->^f (r_1 b^(-1) and dots and r_(s-2) b^(-1)
        times.o 1 times.o 1) b
      - r_1 and dots and r_(s-2) times.o 1 times.o 1.
  $
  Этот элемент является образом в $L_s$ элемента
  $
    r_1 and dots and r_(s-2) and b times.o b
    - r_1 and dots and r_(s-2) and 1 times.o 1,
  $
  что по модулю $Delta^(s-1) times.o Delta$ сводится к
  $
    r_1 and dots and r_(s-2) and (b - 1) times.o 1
    + r_1 and dots and r_(s-2) and 1 times.o (b - 1).
  $
  Благодаря соотношению альтернирования образ в $L_s$ первого
  слагаемого~@eq:f-preimage-element можно переписать в виде
  $
    sum_(t=s-1)^(1) (-1)^((s-1)-t) r_1 and dots and hat(r_t) and dots
    and r_(s-1) times.o 1 times.o r_t.
  $
  Отождествим абелевы группы $Delta^(s-2) times.o Delta$ и
  $Delta^(s-2) times.o ZZ times.o Delta$, опуская $ZZ$. Мы доказали, что если
  $a in Delta^(s-2) times.o Delta$, то $f(a) = alpha(a) + a$, где $alpha$~—
  композиция естественного отображения
  $Delta^(s-2) times.o Delta -> Delta^(s-1)$ и альтернирования
  $Delta^(s-1) -> Delta^(s-2) times.o Delta$. Если $a in Ker f$, то
  $a = -alpha(a)$. Так как элемент $alpha(a)$ кососимметричен, то и элемент $a$
  кососимметричен, но тогда $alpha(a) = (s - 1) a$. Таким образом, из равенства
  $alpha(a) + a = 0$ следует, что $s a = 0$. Поскольку
  $Delta^(s-2) times.o Delta$~— абелева группа без кручения, то $a = 0$, поэтому
  $f$~— мономорфизм. Пусть $N_s$~— коядро отображения $f$. Так как
  $Delta^(s-2) times.o R$~— свободный модуль, то
  $ Tor_(m)^(B)(D, L_s) tilde.equiv Tor_(m)^(B)(D, N_s). $
  #source(312)Так как $f$ индуцирует изоморфизм фактормодулей, то $N_s$~— это
  коядро ограничения $f$ на $Delta^(s-2) times.o Delta$. Таким образом, $N_s$
  получается из $Delta^(s-2) times.o Delta$ как фактормодуль по соотношениям
  $alpha(a) + a = 0$. Из этих соотношений следует, что элементы модуля $N_s$
  кососимметричны, поэтому $N_s$~— фактормодуль модуля $Delta^(s-1)$. Подгруппа,
  порождённая в $Delta^(s-1)$ элементами $alpha(a) + a = 0$, совпадает с
  $s Delta^(s-1)$, следовательно, $N_s tilde.equiv Delta^(s-1) times.o ZZ_s$.
]

Перейдём к лемме~@lem:torsion-in-image. Достаточно доказать следующий локальный
вариант.

#lemma[
  Для любого простого $p != 2$
  $t_p H_(n)(Phi) subset.eq Im(M^n times.o_B ZZ_((p)))$.
] <lem:local-torsion-in-image>

#proof[
  Так как лемма~@lem:tor-circle-product уже доказана, мы можем пользоваться той
  частью теоремы~@th:free-abelian-extension-homology, которая касается ядра
  $K_n$ и коядра $C_n$. Следовательно, если $n != 1 mod p$, то
  $H_(n)(Phi) times.o ZZ_((p)) tilde.equiv M^n times.o_B ZZ_((p))$. Будем
  поэтому считать, что $n = 1 mod p$. Рассмотрим группу $W = B P$. Вложение
  Магнуса $Phi -> W$ (см.~§~@sec:free-abelian-kernel-extensions) индуцирует
  гомоморфизм
  $
    H_(n)(Phi) times.o ZZ_((p)) -> H_(n)(W) times.o ZZ_((p)).
  $ <eq:magnus-homology-map>
  Из предложения~@prop:invariant-basis-homology главы~@ch:extension-homology
  следует, что
  $ H_(n)(W) tilde.equiv plus.o.big_(m+k=n) H_(m)(B, P^k). $
  В правой части присутствует слагаемое $P^n times.o_B ZZ$ $(m = 0)$. Рассмотрим
  композицию $f$ отображения~@eq:magnus-homology-map и проекции
  $H_(n)(W) times.o ZZ_((p)) -> P^n times.o_B ZZ_((p))$. Так как $p != 2$, то по
  следствию~@cor:exterior-power-coinvariants $P^n times.o_B ZZ_((p))$~— группа
  без кручения. Нам достаточно доказать, что если
  $a in H_(n)(Phi) times.o ZZ_((p))$, но $a in.not Im(M^n times.o_B ZZ_((p)))$,
  то $f(a) != 0$, или, что композиция $f$ с естественным отображением
  $f': P^n times.o_B ZZ_((p)) -> (P^n \/ M^n) times.o_B ZZ_((p))$ индуцирует
  вложение коядра $C_n times.o ZZ_((p))$. Построенное отображение
  $
    H_(n)(Phi) times.o ZZ_((p)) ->^(f' f) (P^n \/ M^n) times.o_B ZZ_((p))
  $
  можно заменить следующей цепочкой
  $
    & H_(n)(Phi) times.o ZZ_((p)) ->^s H_(1)(B, M^(n-1)) times.o ZZ_((p))
      ->^(s') \
    & quad quad ->^(s') (M^(n-1) times.o Delta) times.o_B ZZ_((p))
      ->^(s'') (P^n \/ M^n) times.o_B ZZ_((p)).
  $
  Здесь $s$~— естественное отображение на коядро $C_n times.o ZZ_((p))$
  (напомним, что по теореме~@th:free-abelian-extension-homology с точностью до
  2-кручения $C_n tilde.equiv H_(1)(B, M^(n-1))$). Далее, $s'$~— связывающий
  гомоморфизм, определяемый последовательностью
  $ 0 -> Delta -> ZZ B -> ZZ -> 0. $
  #source(313)Наконец, $s''$~— гомоморфизм, индуцированный вложением
  $M^(n-1) times.o Delta -> P^n \/ M^n$ ($M^(n-1) times.o Delta$~— второй этаж
  модуля $P^n$). Очевидно, $Ker s' = 0$. Покажем, что $Ker s'' = 0$. Имеет место
  точная последовательность
  $
    dots.c -> H_(1)(B, P_(n-2 thin 0)^n) times.o ZZ_((p))
    -> (M^(n-1) times.o Delta) times.o_B ZZ_((p))
    ->^(s'') (P^n \/ M^n) times.o_B ZZ_((p)) -> dots.c
  $
  поэтому достаточно доказать, что
  $H_(1)(B, P_(n-2 thin 0)^n times.o ZZ_((p))) = 0$. Так как $n = 1 mod p$, то
  $P_(n-2 thin 0)^n times.o ZZ_((p))$~— последовательное расширение модулей
  $M^i times.o Delta^(n-i) times.o ZZ_((p))$, где $i != 0; 1 mod p$, и модулей
  $P_(i+1 thin i)^n times.o ZZ_((p))$, где $i = 0 mod p$. Из
  лемм~@lem:exterior-power-relations-flat и~@lem:section-flat следует, что
  $P_(n-2 thin 0)^n times.o ZZ_((p))$~— плоский $B$-модуль, поэтому
  $Ker s'' = 0$. Мы видим, что композиция $s, s'$ и $s''$ индуцирует вложение
  $C_n times.o ZZ_((p)) -> (P^n \/ M^n) times.o_B ZZ_((p))$, следовательно, это
  же верно для композиции $f$ и $f'$. В этом месте мы пользуемся эвристическим
  принципом: в гомологической алгебре все диаграммы коммутативны. На самом деле,
  коммутативность интересующей нас диаграммы доказывается не так просто. За
  подробностями мы отсылаем читателя к работе [@bib:Kuzmin1988].
]
