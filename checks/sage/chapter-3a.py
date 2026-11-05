"""Exact checks of Chapter 3 "Cohomology and the functor Ext", §§ 1-5 (Sage).

Run from the project root: sage -python checks/sage/chapter-3a.py (plain
asserts; do not use -O).  The last line is "ok chapter-3a: N checks".

Book: Yu. V. Kuzmin, Homological group theory (Factorial Press, Moscow,
2006), chapter 3, printed pp. 117-149.  Pages are printed pages; labels are
those of content/03-*.typ.  Expected values are the book's; where the book
is wrong the printed reading is kept as a refuted check (`refuted`) beside
the corrected one.  Exact arithmetic only: integers, integer matrices and
Sage's ChainComplex over ZZ (Smith normal form), Laurent polynomials over
ZZ, the free associative algebra over ZZ, GAP through libgap (finitely
presented groups, abelian invariants, finite permutation groups).

What is checked, by section:

section_1 (pp. 118-125): exc:bar-resolution-modules (p. 124): the module
  bar complex X_n = B (x) R^(x)n (x) R on generic tensors of the free
  associative ring (B = R free; a multilinear identity there holds in every
  ring and module): with the last sign (-1)^n (C180, C179) eps d_1 = 0,
  d_(n-1) d_n = 0 and d s + s d = id for the contracting homotopy
  s(b (x) ... (x) r) = b (x) ... (x) r (x) 1, n <= 5; the printed sign "+"
  refuted (eps d_1 != 0, d d != 0).  The same exercise needs the additive
  group of R free: R = Z x Z_2, B = Z = R e_1 is additively free but
  e_1 X_1 = Z + Z_2 has torsion, so X_1 is not projective (refuted
  reading; source corrected).  Ext(Z_n, Z_m) = Z_(n, m) from
  0 -> Z -n-> Z (n, m <= 12) and Ext(B, Z_m) from random presentation
  matrices of finite B against the cyclic decomposition (p. 123);
  exc:non-isomorphic-morphism: exactness of the rows and the chain map.
section_2_3 (pp. 125-136): the right R-module Hom(R, A) of p. 126 (C183):
  (f r)(x) = f(r x) is a right action on Hom(Z S_3, Z), (f r)(x) = f(x r)
  is not; prop:injective-dimension-shift and the k-step shift (C188, C189)
  on R = Z_4 (Z_4 injective over itself): Ext^n_(Z_4)(Z_2, Z_2) = Z_2,
  Ext^n(Z_2, Z_4) = 0, Ext^1(Z_2, Z_2) = Coker(Hom(Z_2, Z_4) ->
  Hom(Z_2, Z_2)), Ext^1(Z_4, Z_2) = 0 = the corresponding cokernel;
  exc:residue-ring-projective-not-free: Z_n has a non-trivial idempotent
  exactly when n is not a prime power (n <= 200), and e Z_n is not free;
  prop:projective-to-free-resolution with n = 0 refuted by B = 3 Z_6
  (source corrected to n > 0); exc:trivial-summand-of-group-algebra:
  Q G = Delta + Q s for S_3, A_4, Z_5.
section_4 (pp. 136-141): cor:amalgam-cohomology-sequence computed exactly
  as the mapping cone of res_1 - res_2 on the cochains of the periodic
  resolutions (Z_k: coboundaries 0, k; restriction to the subgroup of index
  s: 1 in even, s in odd degrees), for all Z_k *_Z_l Z_m with
  k = l s, m = l t, l, s, t <= 4, degrees <= 8: H^n = 0 for odd n,
  H^n = the coamalgam {(a, b) : a = b mod l} for even n > 0
  (exc:cyclic-amalgam-cohomology), the free products (l = 1) as
  cor:free-product-cohomology; independently, H^2 = Ext(G_ab, Z) is dual
  to G_ab, and G_ab from GAP has the invariants of the coamalgam; the
  homology cone gives H_odd = G_ab, H_even = 0.  exc:sl2z-cohomology:
  H^n(SL_2(Z)) = Z_12 (n > 0 even), 0 (n odd) for n <= 12; the two
  matrices have orders 6 and 4, M6^3 = M4^2 = -1, M4^-1 M6 = T^-1, and
  <a, b | a^4, a^2 = b^3> maps onto SL_2(Z/N), N = 2..7.  HNN extensions
  (cor:hnn-cohomology-sequence): the cone of r - r' for the
  Baumslag-Solitar groups BS(m, n), 1 <= |m| <= |n| <= 4, agrees with the
  Lyndon resolution of t^-1 a^m t a^-n (exponent sums computed from the
  word), and with G_ab from GAP (Z + Z_|m - n|) through universal
  coefficients; exc:hnn-semidirect-product for Z^2 x|_A Z, ten matrices
  A: H^1 rank and H^2 torsion against G*_ab from GAP, H^3 = Z/(det A - 1).
section_5 (pp. 141-149): the cocycle identity extended to Z G (C214) for
  the carry cocycle of Z_n (n <= 6) and for a coboundary of S_3 with values
  in Z S_3, on random elements; (3.22) and its printed "(a + 1)" (C216,
  refuted), in the free algebra and in Z S_3; lem:kernel-identification:
  Delta_A / Delta_Gbar Delta_A = A for nine finite Gbar with a normal
  abelian A (lattice computation in Z Gbar); th:group-module-extensions for
  G = Z_2: the module extension 0 -> A -> Delta_Gbar / I -> Delta_G -> 0
  splits exactly when Gbar splits over A (Gbar = Z_4, Z_8, Q_8 do not;
  Z_2^2, S_3, D_8 do); lem:unique-roots-extension:
  (g a)^n = g^n a^(s_n(g)) in Z x| Z^2 for three matrices, n <= 6;
  exc:q-group-extension at n = 0 and the definition of p. 146 at n = 0
  refuted (sources corrected to natural n, n != 0); the coinduced module
  of prop:unique-roots-split-embedding: c(x) = (-1)^x satisfies
  c s_2(g) = 0, so G C need not satisfy uniqueness of roots;
  exc:adjoining-p-th-root: the projection of s_n(x^j) (p not dividing j)
  to A (x) 1 is s_k(x^(j p)) with n = p k - r (C223; p <= 7, |j| <= 2p,
  n <= 30), the printed n = p k + r refuted at p = 2, n = 3; the identities
  s_n(g) s_m(g^n) = s_n(g^m) s_m(g) (n, m <= 12), t^k s_p(t) = s_p(t) and
  s_p(t)^l = p^(l-1) s_p(t) in Z[t]/(t^p - 1) (p <= 7, l <= 6).

What this does NOT establish: the general theorems (only the listed
groups, rings, ranks and degrees are covered); the exactness of the
mapping cones for amalgams and HNN extensions is the book's
lem:amalgam-augmentation and lem:hnn-augmentation, assumed, not checked
(only H^2 is compared with an independent computation); the bar complex
is checked only for n <= 5.  Nothing here compares our text with the
printed book.
"""

import itertools

from sage.all import (
    QQ, ZZ, ChainComplex, FreeAlgebra, FreeModule, LaurentPolynomialRing,
    PolynomialRing, gcd, libgap, matrix, set_random_seed, vector,
)
import random

SCOPE = 'chapter-3a'
COUNT = [0]


def check(cond, what):
    assert bool(cond), 'FAILED: ' + what
    COUNT[0] += 1


def refuted(cond, what):
    assert not bool(cond), 'printed reading unexpectedly holds: ' + what
    COUNT[0] += 1


def gap(src):
    return libgap.eval(src)


def prime_power_invariants(invs):
    """Abelian invariants in GAP's form: prime powers and zeros, sorted."""
    out = []
    for d in invs:
        d = abs(ZZ(d))
        if d == 0:
            out.append(0)
        elif d > 1:
            out.extend(p ** e for p, e in d.factor())
    return sorted(out)


def gap_invariants(G):
    return sorted(ZZ(x) for x in G.AbelianInvariants())


def homology_invariants(C, n):
    return prime_power_invariants(C.homology(n).invariants())


# ---------------------------------------------------------------------------
# Finite groups as multiplication tables (elements 0..N-1, sorted as in GAP)
# ---------------------------------------------------------------------------

class TGroup:
    """A finite group given by GAP, with its multiplication table."""

    def __init__(self, G):
        self.G = G
        self.elts = G.AsSSortedList()
        tab = gap('function(e) return List(e, g -> List(e, h -> '
                  'PositionSorted(e, g*h))); end')(self.elts)
        self.mul = [[int(x) - 1 for x in row] for row in tab]
        self.n = len(self.mul)
        self.one = [i for i in range(self.n)
                    if all(self.mul[i][j] == j for j in range(self.n))][0]
        self.inv = [[j for j in range(self.n) if self.mul[i][j] == self.one][0]
                    for i in range(self.n)]

    def index(self, g):
        return int(self.elts.PositionSorted(g)) - 1

    def unit(self, i):
        v = [0] * self.n
        v[i] = 1
        return vector(ZZ, v)

    def rmul(self, v, h):
        """v * h in ZG (right multiplication by the element h)."""
        w = [0] * self.n
        for g in range(self.n):
            if v[g]:
                w[self.mul[g][h]] += v[g]
        return vector(ZZ, w)

    def lmul(self, h, v):
        """h * v in ZG."""
        w = [0] * self.n
        for g in range(self.n):
            if v[g]:
                w[self.mul[h][g]] += v[g]
        return vector(ZZ, w)

    def prod(self, u, v):
        w = [0] * self.n
        for a in range(self.n):
            if u[a]:
                for b in range(self.n):
                    if v[b]:
                        w[self.mul[a][b]] += u[a] * v[b]
        return vector(ZZ, w)


# ---------------------------------------------------------------------------
# Section 1: Ext as sequences (pp. 118-125)
# ---------------------------------------------------------------------------

def tensor_add(acc, key, c):
    if c:
        acc[key] = acc.get(key, 0) + c
        if acc[key] == 0:
            del acc[key]


def bar_d(x, sign_last):
    """Differential of exc:bar-resolution-modules on a linear combination.

    x is a dict {(b, r_1, ..., r_n, r): coeff}; the entries are words of the
    free associative ring (tuples of letters), b a word of the free module
    B = R, r the coefficient of the last (module) factor.  sign_last is the
    sign of the last summand as a function of n.
    """
    out = {}
    for key, c in x.items():
        b, rs, r = key[0], list(key[1:-1]), key[-1]
        n = len(rs)
        if n == 0:
            continue
        # b (x) r_1 (x) ... (x) r_(n-1) (x) r_n  (then times r)
        tensor_add(out, tuple([b] + rs[:-1] + [rs[-1] + r]), c)
        for i in range(n - 1, 0, -1):
            merged = rs[:i - 1] + [rs[i - 1] + rs[i]] + rs[i + 1:]
            tensor_add(out, tuple([b] + merged + [r]), (-1) ** (n - i) * c)
        tensor_add(out, tuple([b + rs[0]] + rs[1:] + [r]),
                   sign_last(n) * c)
    return out


def bar_eps(x):
    """X_0 -> B, b (x) r -> b r."""
    out = {}
    for key, c in x.items():
        b, r = key
        tensor_add(out, (b + r,), c)
    return out


def bar_s(x):
    """Contracting homotopy b (x) r_1 ... (x) r_n (x) r -> ... (x) r (x) 1."""
    out = {}
    for key, c in x.items():
        tensor_add(out, tuple(list(key) + [()]), c)
    return out


def section_1():
    """Exercise 6 (p. 124): the module bar resolution; C179, C180."""
    corrected = lambda n: (-1) ** n
    printed = lambda n: 1
    for n in range(1, 6):
        gen = {tuple([('b',)] + [('r%d' % i,) for i in range(1, n + 1)]
                     + [('r',)]): 1}
        dd = bar_d(bar_d(gen, corrected), corrected) if n >= 2 else None
        if n >= 2:
            check(dd == {}, 'ex. 3.1.6: d_(n-1) d_n = 0, n = %d' % n)
            refuted(bar_d(bar_d(gen, printed), printed) == {},
                    'ex. 3.1.6 with last sign +: d d = 0, n = %d' % n)
        else:
            check(bar_eps(bar_d(gen, corrected)) == {},
                  'ex. 3.1.6: eps d_1 = 0')
            refuted(bar_eps(bar_d(gen, printed)) == {},
                    'ex. 3.1.6 with last sign +: eps d_1 = 0')
        # d s + s d = id on X_n (n >= 1), so the augmented complex is exact
        lhs = bar_d(bar_s(gen), corrected)
        for k, c in bar_s(bar_d(gen, corrected)).items():
            tensor_add(lhs, k, c)
        check(lhs == gen, 'ex. 3.1.6: d s + s d = id on X_%d' % n)
    gen0 = {(('b',), ('r',)): 1}
    lhs = bar_d(bar_s(gen0), corrected)
    # on X_0: d_1 s_0 + s_(-1) eps = id, with s_(-1)(b) = b (x) 1
    s_eps = {}
    for key, c in bar_eps(gen0).items():
        tensor_add(s_eps, (key[0], ()), c)
    for k, c in s_eps.items():
        tensor_add(lhs, k, c)
    check(lhs == gen0, 'ex. 3.1.6: d_1 s_0 + s_(-1) eps = id on X_0')

    # Ex. 6 needs the additive group of R free: R = Z x Z_2, B = Z = R e_1
    # (additively free).  e_1 X_1 = (B (x) R) (x) e_1 R = (Z + Z_2) (x) Z has
    # torsion, while e_1 P is free abelian for every projective R-module P
    # (a summand of e_1 R^k = Z^k): X_1 is not projective.
    def tensor_invariants(a, b):
        out = []
        for x in a:
            for y in b:
                out.append(gcd(x, y))
        return prime_power_invariants(out)
    BR = tensor_invariants([0], [0, 2])           # B (x) R, additively
    e1X1 = tensor_invariants(BR, [0])              # (B (x) R) (x) e_1 R
    check(BR == [0, 2] and e1X1 == [0, 2],
          'ex. 3.1.6: e_1 X_1 = Z + Z_2 for R = Z x Z_2, B = Z')
    refuted(all(x == 0 for x in e1X1),
            'ex. 3.1.6 without R additively free: X_1 projective')

    # Ext(Z_n, A) = A / n A (p. 123) and the decomposition for finitely
    # generated B: Ext(B, Z_m) from any presentation matrix of B.
    for n in range(1, 13):
        for m in range(1, 13):
            # resolution 0 -> Z -n-> Z -> Z_n; Hom(-, Z_m): Z_m -n-> Z_m
            image = set((n * a) % m for a in range(m))
            check(m // len(image) == gcd(n, m),
                  'Ext(Z_%d, Z_%d) = Z_%d' % (n, m, gcd(n, m)))
    set_random_seed(31)
    random.seed(31)
    for trial in range(30):
        R = matrix(ZZ, 3, 3, [random.randint(-6, 6) for _ in range(9)])
        if R.det() == 0:
            continue
        D = R.smith_form()[0]
        B = [abs(D[i, i]) for i in range(3)]
        for m in range(2, 9):
            # Ext(B, Z_m) = Coker(Hom(Z^3, Z_m) -R^T-> Hom(Z^3, Z_m))
            Rt = R.transpose()
            img = set()
            for v in itertools.product(range(m), repeat=3):
                img.add(tuple(x % m for x in Rt * vector(ZZ, v)))
            order = m ** 3 // len(img)
            expected = 1
            for b in B:
                expected *= gcd(b, m)
            check(order == expected,
                  'Ext(B, Z_%d) from a presentation of B = %s' % (m, B))

    # Exercise 3 (pp. 123-124): the rows Z -2-> Z -> Z_2 and
    # Z -2-> Z -2-> Z_4 -1-> Z_2 are exact and the vertical maps commute.
    bottom_ker = [a for a in range(-8, 9) if (2 * a) % 4 == 0]
    check(bottom_ker == [a for a in range(-8, 9) if a % 2 == 0],
          'ex. 3.1.3: Ker(Z -> Z_4) = 2Z')
    check(sorted(set((2 * a) % 4 for a in range(4))) == [0, 2]
          and [x for x in range(4) if x % 2 == 0] == [0, 2],
          'ex. 3.1.3: Im(Z -> Z_4) = Ker(Z_4 -> Z_2)')
    check(all((2 * a) % 4 == (1 * (2 * a)) % 4 for a in range(-5, 6))
          and all((a % 4) % 2 == a % 2 for a in range(-5, 6)),
          'ex. 3.1.3: the vertical maps 1 form a chain map')


# ---------------------------------------------------------------------------
# Section 2: injective modules (pp. 125-132); Section 3 examples
# ---------------------------------------------------------------------------

def section_2_3():
    # C183: Hom(R, A) is a right R-module by (f r)(x) = f(r x).  R = Z S_3,
    # A = Z; f is given by its values on S_3 (Z-linear on R).
    T = TGroup(gap('SymmetricGroup(3)'))
    random.seed(7)

    def rand_elt():
        return vector(ZZ, [random.randint(-3, 3) for _ in range(T.n)])

    def act_corrected(f, r):      # (f r)(x) = f(r x): values on basis x = g
        return vector(ZZ, [f.dot_product(T.prod(r, T.unit(g)))
                           for g in range(T.n)])

    def act_other(f, r):          # (f r)(x) = f(x r)
        return vector(ZZ, [f.dot_product(T.prod(T.unit(g), r))
                           for g in range(T.n)])
    ok_c = ok_o = True
    for _ in range(20):
        f, r, s = rand_elt(), rand_elt(), rand_elt()
        ok_c &= act_corrected(act_corrected(f, r), s) == \
            act_corrected(f, T.prod(r, s))
        ok_o &= act_other(act_other(f, r), s) == act_other(f, T.prod(r, s))
    check(ok_c, 'p. 126: (f r)(x) = f(r x) is a right action on Hom(Z S_3, Z)')
    refuted(ok_o, 'p. 126: (f r)(x) = f(x r) is a right action')

    # C188, C189 on R = Z_4 (Z_4 is injective over itself):
    # 0 -> Z_2 -> Z_4 -> Z_2 -> 0;  Ext^n_(Z_4)(Z_2, Z_2) = Z_2 from the
    # periodic resolution ... -2-> Z_4 -2-> Z_4 -> Z_2;
    # Ext^1(B, A'') = Coker(Hom(B, A) -> Hom(B, A')).
    def hom_cyclic(a, b):          # Hom_Z(Z_a, Z_b): images of 1
        return [y for y in range(b) if (a * y) % b == 0]
    # Hom(Z_2, Z_2) = Z_2 and the maps of the resolution are 2 = 0 there
    homs = hom_cyclic(4, 2)        # Hom(Z_4, Z_2) = Z_2
    ext_orders = []
    for n in range(1, 6):
        ker = [y for y in homs if (2 * y) % 2 == 0]
        im = set((2 * y) % 2 for y in homs)
        ext_orders.append(len(ker) // len(im))
    check(ext_orders == [2] * 5, 'Ext^n_(Z_4)(Z_2, Z_2) = Z_2 (n <= 5)')
    homs4 = hom_cyclic(4, 4)       # Hom(Z_4, Z_4) = Z_4
    ker = [y for y in homs4 if (2 * y) % 4 == 0]
    im = set((2 * y) % 4 for y in homs4)
    check(len(ker) == len(im), 'Ext^n_(Z_4)(Z_2, Z_4) = 0 (Z_4 injective)')
    # Coker(Hom(Z_2, Z_4) -> Hom(Z_2, Z_2)), the map induced by Z_4 -> Z_2
    H_BA = hom_cyclic(2, 4)        # [0, 2]
    H_BAp = hom_cyclic(2, 2)       # [0, 1]
    image = set(y % 2 for y in H_BA)
    check(len(H_BAp) // len(image) == 2,
          'prop:injective-dimension-shift: Ext^1(Z_2, Z_2) = '
          'Coker(Hom(Z_2, Z_4) -> Hom(Z_2, Z_2)) = Z_2')
    H_BA = hom_cyclic(4, 4)
    H_BAp = hom_cyclic(4, 2)
    image = set(y % 2 for y in H_BA)
    check(len(H_BAp) // len(image) == 1,
          'Ext^1(Z_4, Z_2) = 0 = Coker(Hom(Z_4, Z_4) -> Hom(Z_4, Z_2))')

    # Ex. 3.3.2: Z_n has a non-trivial idempotent (a projective, non-free
    # summand) exactly when n is not a prime power (n <= 200).
    for n in range(2, 201):
        idem = [e for e in range(2, n) if (e * e - e) % n == 0]
        if n == 6:
            # prop:projective-to-free-resolution needs n > 0: B = 3 Z_6 is
            # projective (0 -> B -> B is a projective resolution of length 0)
            # but |B| = 2 is not a power of 6, so B is not free.
            check(3 in idem, 'Z_6 = 3 Z_6 + 4 Z_6, 3 idempotent')
            refuted(any(6 ** j == 2 for j in range(5)),
                    'prop:projective-to-free-resolution with n = 0 '
                    '(B = 3 Z_6 free)')
        check(bool(idem) == (len(ZZ(n).factor()) > 1),
              'ex. 3.3.2: idempotents of Z_%d' % n)
        for e in idem:
            k = n // gcd(e, n)
            # e Z_n has order n / gcd(e, n), not a power of n: not free
            check(k < n and k > 1, 'ex. 3.3.2: e Z_%d is not free' % n)

    # Ex. 3.3.1: K G = Delta (+) K s, s = sum of g, char K prime to |G|
    for name in ['SymmetricGroup(3)', 'AlternatingGroup(4)',
                 'CyclicGroup(IsPermGroup, 5)']:
        T = TGroup(gap(name))
        s = vector(QQ, [1] * T.n)
        vecs = [vector(QQ, T.unit(g) - T.unit(T.one)) for g in range(T.n)
                if g != T.one] + [s]
        check(matrix(QQ, vecs).rank() == T.n and
              all(T.rmul(vector(ZZ, s), g) == vector(ZZ, s)
                  for g in range(T.n)),
              'ex. 3.3.1: Q G = Delta + Q s for %s' % name)


# ---------------------------------------------------------------------------
# Section 4: free products, amalgams and HNN extensions (pp. 136-141)
# ---------------------------------------------------------------------------

def cyclic_cochains(k, N):
    """Coboundaries of Hom_(Z_k)(P, Z) for the periodic resolution P."""
    return [matrix(ZZ, 1, 1, [0 if (j + 1) % 2 else k]) for j in range(N)]


def cyclic_restriction(s, N):
    """Restriction to the subgroup of index s, cochain level, degrees 0..N."""
    return [matrix(ZZ, 1, 1, [1 if j % 2 == 0 else s]) for j in range(N + 1)]


def amalgam_cone(k, l, m, N):
    """Cochain cone of res1 - res2: C(Z_k) + C(Z_m) -> C(Z_l)."""
    s, t = k // l, m // l
    d1, d2, dS = cyclic_cochains(k, N), cyclic_cochains(m, N), \
        cyclic_cochains(l, N)
    r1, r2 = cyclic_restriction(s, N), cyclic_restriction(t, N)
    diffs = {}
    for n in range(N):
        # C^n = C^n(G1) + C^n(G2) + C^(n-1)(S); C^(-1)(S) = 0
        a, b, c, e = d1[n][0, 0], d2[n][0, 0], r1[n][0, 0], r2[n][0, 0]
        if n == 0:
            diffs[n] = matrix(ZZ, [[a, 0], [0, b], [c, -e]])
        else:
            diffs[n] = matrix(ZZ, [[a, 0, 0], [0, b, 0],
                                   [c, -e, -dS[n - 1][0, 0]]])
    C = ChainComplex(diffs, degree=1)
    for n in range(N - 1):
        check(diffs[n + 1] * diffs[n] == 0, 'amalgam cone D D = 0')
    return C


def amalgam_chain_cone(k, l, m, N):
    """Chain cone of C(Z_l) -> C(Z_k) + C(Z_m), x -> (f1 x, -f2 x)."""
    s, t = k // l, m // l

    def bd(q, j):          # boundary C_j -> C_(j-1) of Z_q (tensored with Z)
        return 0 if j % 2 else q

    def f(idx, j):         # chain map of the inclusion, tensored with Z
        return 1 if j % 2 == 0 else idx
    diffs = {}
    for n in range(1, N + 1):
        # Cone_n = C_n(G1) + C_n(G2) + C_(n-1)(S), with
        # d(x1, x2, z) = (d x1 + f1 z, d x2 - f2 z, -d z)
        rows = [[bd(k, n), 0, f(s, n - 1)], [0, bd(m, n), -f(t, n - 1)]]
        if n >= 2:
            rows.append([0, 0, -bd(l, n - 1)])
        diffs[n] = matrix(ZZ, rows)
    for n in range(2, N + 1):
        check(diffs[n - 1] * diffs[n] == 0, 'amalgam chain cone d d = 0')
    return ChainComplex(diffs, degree=-1)


def coamalgam_invariants(k, l, m):
    """{(a, b) in Z_k + Z_m : a = b mod l} = L / (kZ + mZ)."""
    # L has basis u = (1, 1), v = (0, l); (k, 0) = k u - (k/l) v,
    # (0, m) = (m/l) v.
    M = matrix(ZZ, [[k, -(k // l)], [0, m // l]])
    D = M.smith_form()[0]
    return prime_power_invariants([D[0, 0], D[1, 1]])


def amalgam_gap(k, l, m):
    s, t = k // l, m // l
    gap('F2 := FreeGroup("a", "b")')
    return gap('F2 / [F2.1^%d, F2.2^%d, F2.1^%d * F2.2^-%d]' % (k, m, s, t))


def section_4():
    N = 10
    cases = [(k, l, m) for l in range(1, 5) for s in range(1, 5)
             for t in range(1, 5) for (k, m) in [(l * s, l * t)]
             if k > 1 and m > 1 and k <= m]
    for (k, l, m) in cases:
        C = amalgam_cone(k, l, m, N)
        coam = coamalgam_invariants(k, l, m)
        G = amalgam_gap(k, l, m)
        ab = gap_invariants(G)
        check(homology_invariants(C, 0) == [0],
              'H^0(Z_%d *_Z_%d Z_%d) = Z' % (k, l, m))
        for n in range(1, N - 1):
            h = homology_invariants(C, n)
            if n % 2:
                check(h == [], 'ex. 3.4.6: H^%d(Z_%d *_Z_%d Z_%d) = 0'
                      % (n, k, l, m))
            else:
                check(h == coam, 'ex. 3.4.6: H^%d(Z_%d *_Z_%d Z_%d) = '
                      'coamalgam %s' % (n, k, l, m, coam))
        # independent: H^2 = Ext(G_ab, Z) (rational H_2 = 0 for virtually
        # free G), so H^2 is dual to G_ab (GAP)
        check(coam == ab, 'H^2(Z_%d *_Z_%d Z_%d) = dual of G_ab (GAP %s)'
              % (k, l, m, ab))
        if l == 1:
            fp = prime_power_invariants([k, m])
            check(coam == fp, 'cor:free-product-cohomology: Z_%d * Z_%d'
                  % (k, m))
        # homology: H_odd = amalgamated sum = G_ab, H_even = 0 (n >= 2)
        CC = amalgam_chain_cone(k, l, m, N)
        check(homology_invariants(CC, 0) == [0], 'H_0 = Z')
        for n in range(1, N - 1):
            h = homology_invariants(CC, n)
            check(h == (ab if n % 2 else []),
                  'H_%d(Z_%d *_Z_%d Z_%d)' % (n, k, l, m))
    # Ex. 7: SL_2(Z) = Z_4 *_Z_2 Z_6; H^n = Z_12 (n > 0 even), 0 (n odd)
    C = amalgam_cone(4, 2, 6, 14)
    for n in range(1, 13):
        h = homology_invariants(C, n)
        check(h == ([] if n % 2 else [3, 4]),
              'ex. 3.4.7: H^%d(SL_2(Z)) = %s' % (n, 'Z_12' if n % 2 == 0
                                                 else '0'))
    S6 = matrix(ZZ, [[0, 1], [-1, 1]])
    S4 = matrix(ZZ, [[0, 1], [-1, 0]])
    I2 = matrix.identity(ZZ, 2)
    check(S6 ** 6 == I2 and S6 ** 3 == -I2 and S6 ** 2 != I2,
          'ex. 3.4.7: the first matrix has order 6, cube -1')
    check(S4 ** 4 == I2 and S4 ** 2 == -I2, 'ex. 3.4.7: the second matrix '
          'has order 4, square -1')
    check(S4.inverse() * S6 == matrix(ZZ, [[1, -1], [0, 1]]),
          'ex. 3.4.7: S4^-1 S6 = T^-1, so S4, S6 generate SL_2(Z) with S, T')
    G = amalgam_gap(4, 2, 6)
    libgap.set_global('Gsl', G)
    for N in range(2, 8):
        hom = gap('GroupHomomorphismByImages(Gsl, SL(2, Integers mod %d), '
                  'GeneratorsOfGroup(Gsl), [[[0,1],[-1,0]], [[0,1],[-1,1]]]'
                  ' * One(Integers mod %d))' % (N, N))
        check(hom != gap('fail') and
              hom.Image().Size() == gap('SL(2, Integers mod %d)' % N).Size(),
              'ex. 3.4.7: a -> S4, b -> S6 maps <a, b | a^4, a^2 = b^3> '
              'onto SL_2(Z/%d)' % N)

    # HNN extensions: Baumslag-Solitar groups BS(m, n) = <a, t | t^-1 a^m t
    # = a^n>, base Z, S = <a^m>, S' = <a^n>.  Cone of r - r' versus the
    # Lyndon resolution (Fox derivatives, sec:one-relator-cohomology) versus
    # G_ab from GAP.
    for m in range(-4, 5):
        for n in range(-4, 5):
            if m == 0 or n == 0 or abs(m) > abs(n) or \
                    (abs(m) == abs(n) and m < 0 and n < 0):
                continue
            # cochains of Z: C^0 = C^1 = Z, zero coboundary
            # cone: C^q(G) + C^(q-1)(S), D(x, z) = (0, (r - r') x)
            # C^0 = C^0(G) -> C^1 = C^1(G) + C^0(S) -> C^2 = C^1(S)
            D0 = matrix(ZZ, [[0], [1 - 1]])
            D1 = matrix(ZZ, [[m * 1 - n * 1, 0]])
            C = ChainComplex({0: D0, 1: D1}, degree=1)
            hnn = [homology_invariants(C, q) for q in range(3)]
            # Lyndon: Hom of 0 -> ZG -> ZG^2 -> ZG; the coboundary Z^2 -> Z
            # is given by the exponent sums (= augmented Fox derivatives) of
            # the relator t^-1 a^m t a^-n, computed from the word
            word = [(1, -1)] + [(0, 1 if m > 0 else -1)] * abs(m) + \
                [(1, 1)] + [(0, -1 if n > 0 else 1)] * abs(n)
            sig = [sum(e for (g, e) in word if g == i) for i in range(2)]
            L1 = matrix(ZZ, [[0], [0]])
            L2 = matrix(ZZ, [sig])
            L = ChainComplex({0: L1, 1: L2}, degree=1)
            lyn = [homology_invariants(L, q) for q in range(3)]
            check(hnn == lyn, 'cor:hnn-cohomology-sequence: BS(%d, %d) '
                  'agrees with the Lyndon resolution' % (m, n))
            gap('Fbs := FreeGroup("a", "t")')
            G = gap('Fbs / [Fbs.2^-1 * Fbs.1^%d * Fbs.2 * Fbs.1^%d]'
                    % (m, -n))
            ab = gap_invariants(G)
            exp = prime_power_invariants([0, m - n])
            check(ab == exp, 'BS(%d, %d)_ab = Z + Z_|m - n| (GAP)' % (m, n))
            # H^1 rank = rank of G_ab, torsion of H^2 = torsion of G_ab
            check(hnn[1].count(0) == ab.count(0) and
                  [x for x in hnn[2] if x] == [x for x in ab if x],
                  'BS(%d, %d): H^1, H^2 against UCT and GAP' % (m, n))

    # Ex. 9: S = S' = G = Z^2, G* = Z^2 x| Z with x acting by A.  H^n(G*) is
    # an extension of Ker t_n by Coker t_(n-1), t_n = Lambda^n(A)^T - 1.
    mats = [[[2, 1], [1, 1]], [[1, 1], [0, 1]], [[0, -1], [1, 0]],
            [[-1, 0], [0, -1]], [[0, 1], [1, 0]], [[1, 0], [0, -1]],
            [[2, 1], [1, 0]], [[1, 0], [0, 1]], [[-1, 1], [0, -1]],
            [[3, 2], [1, 1]]]
    for A in mats:
        A = matrix(ZZ, A)
        dA = A.det()
        I2 = matrix.identity(ZZ, 2)
        t0 = matrix(ZZ, [[0]])
        t1 = A.transpose() - I2
        t2 = matrix(ZZ, [[dA - 1]])
        # cone: C^q = Lambda^q + Lambda^(q-1), D(x, z) = (0, t_q x)
        # C^0 = L0 -> C^1 = L1 + L0 -> C^2 = L2 + L1 -> C^3 = L2
        D0 = matrix(ZZ, [[0], [0], [t0[0, 0]]])
        D1 = matrix(ZZ, [[0, 0, 0], [t1[0, 0], t1[0, 1], 0],
                         [t1[1, 0], t1[1, 1], 0]])
        D2 = matrix(ZZ, [[t2[0, 0], 0, 0]])
        C = ChainComplex({0: D0, 1: D1, 2: D2}, degree=1)
        H = [homology_invariants(C, q) for q in range(4)]
        gap('Fsd := FreeGroup("a", "b", "x")')
        a, b = 'Fsd.1', 'Fsd.2'
        rel = ['Comm(Fsd.1, Fsd.2)',
               'Fsd.3^-1 * %s * Fsd.3 * (%s^%d * %s^%d)^-1'
               % (a, a, A[0, 0], b, A[1, 0]),
               'Fsd.3^-1 * %s * Fsd.3 * (%s^%d * %s^%d)^-1'
               % (b, a, A[0, 1], b, A[1, 1])]
        G = gap('Fsd / [%s]' % ', '.join(rel))
        ab = gap_invariants(G)
        D = (A - I2).smith_form()[0]
        check(ab == prime_power_invariants([0, D[0, 0], D[1, 1]]),
              'ex. 3.4.9: G*_ab = Z + Coker(A - 1) for A = %s' % list(A))
        check(H[1].count(0) == ab.count(0) and
              [x for x in H[2] if x] == [x for x in ab if x],
              'ex. 3.4.9: H^1 rank and H^2 torsion against G*_ab, A = %s'
              % list(A))
        check(H[3] == ([0] if dA == 1 else [2]),
              'ex. 3.4.9: H^3(G*) = Coker t_2 = Z/(det A - 1), A = %s'
              % list(A))


# ---------------------------------------------------------------------------
# Section 5: group extensions and module extensions (pp. 141-149)
# ---------------------------------------------------------------------------

def section_5():
    # C214: the cocycle identity extended to ZG,
    # f(r1, r2) r3 - f(r1, r2 r3) + f(r1 r2, r3) - eps(r1) f(r2, r3) = 0.
    random.seed(5)
    # (a) G = Z_n, A = Z trivial, the carry cocycle f(i, j) = [(i + j) / n]
    for n in range(2, 7):
        f = lambda i, j: (i + j) // n

        def F(r1, r2):
            return sum(r1[i] * r2[j] * f(i, j) for i in range(n)
                       for j in range(n))

        def mul(r1, r2):
            w = [0] * n
            for i in range(n):
                for j in range(n):
                    w[(i + j) % n] += r1[i] * r2[j]
            return w
        ok = all(f(a, b) - f(a, (b + c) % n) + f((a + b) % n, c) - f(b, c)
                 == 0 for a in range(n) for b in range(n) for c in range(n))
        check(ok, 'carry cocycle of Z_%d satisfies the cocycle identity' % n)
        for _ in range(20):
            r1, r2, r3 = [[random.randint(-3, 3) for _ in range(n)]
                          for _ in range(3)]
            e1 = sum(r1)
            val = F(r1, r2) * sum(r3) - F(r1, mul(r2, r3)) + \
                F(mul(r1, r2), r3) - e1 * F(r2, r3)
            check(val == 0, 'C214: extended identity, Z_%d, trivial A' % n)
    # (b) G = S_3 acting on A = Z S_3 (regular), f = coboundary of a random
    # 1-cochain phi: f(g, h) = phi(g) h - phi(g h) + phi(h).
    T = TGroup(gap('SymmetricGroup(3)'))
    phi = [vector(ZZ, [random.randint(-3, 3) for _ in range(T.n)])
           for _ in range(T.n)]

    def fg(g, h):
        return T.rmul(phi[g], h) - phi[T.mul[g][h]] + phi[h]
    ok = all(T.rmul(fg(a, b), c) - fg(a, T.mul[b][c]) + fg(T.mul[a][b], c)
             - fg(b, c) == 0 for a in range(T.n) for b in range(T.n)
             for c in range(T.n))
    check(ok, 'S_3: the coboundary is a 2-cocycle')

    def Fr(r1, r2):
        out = vector(ZZ, [0] * T.n)
        for a in range(T.n):
            for b in range(T.n):
                if r1[a] and r2[b]:
                    out += r1[a] * r2[b] * fg(a, b)
        return out

    def act(x, r):
        out = vector(ZZ, [0] * T.n)
        for g in range(T.n):
            if r[g]:
                out += r[g] * T.rmul(x, g)
        return out
    for _ in range(15):
        r1, r2, r3 = [vector(ZZ, [random.randint(-2, 2) for _ in range(T.n)])
                      for _ in range(3)]
        val = act(Fr(r1, r2), r3) - Fr(r1, T.prod(r2, r3)) + \
            Fr(T.prod(r1, r2), r3) - sum(r1) * Fr(r2, r3)
        check(val == 0, 'C214: extended identity, S_3 acting on Z S_3')

    # C216, (3.22): g a - 1 = (g - 1)(a - 1) + (g - 1) + (a - 1) in any ring
    Rfree = FreeAlgebra(ZZ, 2, 'g, a')          # non-commutative
    gg, aa = Rfree.gens()
    check((gg - 1) * (aa - 1) + (gg - 1) + (aa - 1) == gg * aa - 1,
          '(3.22): g a - 1 = (g - 1)(a - 1) + (g - 1) + (a - 1)')
    refuted((gg - 1) * (aa - 1) + (gg - 1) + (aa + 1) == gg * aa - 1,
            '(3.22) with (a + 1)')
    # the identity in a non-commutative group ring: S_3, all g, a
    ok = True
    for g in range(T.n):
        for a in range(T.n):
            lhs = T.unit(T.mul[g][a]) - T.unit(T.one)
            g1, a1 = T.unit(g) - T.unit(T.one), T.unit(a) - T.unit(T.one)
            rhs = T.prod(g1, a1) + g1 + a1
            ok &= lhs == rhs
    check(ok, '(3.22) in Z S_3 for all g, a')

    # lem:kernel-identification: Delta_A / I = A, I = Delta_Gbar Delta_A, and
    # th:group-module-extensions for G = Z_2: the module extension
    # 0 -> A -> Delta_Gbar / I -> Delta_G -> 0 splits iff Gbar splits over A.
    exts = [  # (Gbar, generators of A, split over A?)
        ('CyclicGroup(IsPermGroup, 4)', 'a -> [a[1]^2]', False),
        ('DirectProduct(CyclicGroup(IsPermGroup, 2), '
         'CyclicGroup(IsPermGroup, 2))', 'a -> [a[1]]', True),
        ('CyclicGroup(IsPermGroup, 8)', 'a -> [a[1]^2]', False),
        ('SymmetricGroup(3)', 'a -> [(1,2,3)]', True),
        ('Group((1,2,3,4), (1,3))', 'a -> [(1,2,3,4)]', True),
        ('QuaternionGroup(IsPermGroup, 8)', 'a -> [a[1]]', False),
        ('AlternatingGroup(4)', 'a -> [(1,2)(3,4), (1,3)(2,4)]', True),
        ('CyclicGroup(IsPermGroup, 9)', 'a -> [a[1]^3]', False),
        ('DirectProduct(CyclicGroup(IsPermGroup, 3), '
         'CyclicGroup(IsPermGroup, 3))', 'a -> [a[1]]', True),
    ]
    for name, agens, split in exts:
        Gb = gap(name)
        gens = Gb.GeneratorsOfGroup()
        Agens = gap(agens)(gens)
        A = Gb.Subgroup(Agens)
        check(A.IsNormal(Gb) and A.IsAbelian(), name + ': A normal abelian')
        T = TGroup(Gb)
        Aidx = [T.index(x) for x in A.AsSSortedList()]
        e = T.unit(T.one)
        V = FreeModule(ZZ, T.n)
        DeltaA = V.span([T.rmul(T.unit(a) - e, h) for a in Aidx
                         for h in range(T.n)])
        I = V.span([T.prod(T.unit(g) - e, T.rmul(T.unit(a) - e, h))
                    for g in range(T.n) for a in Aidx for h in range(T.n)])
        Q = DeltaA.quotient(I)
        check(prime_power_invariants(Q.invariants()) ==
              gap_invariants(A),
              'lem:kernel-identification: Delta_A / I = A for ' + name)
        quotient_order = T.n // len(Aidx)
        if quotient_order != 2 or split is None:
            continue
        # G = Z_2 = <g>; d = gbar - 1 + (a - 1); split iff some
        # d (gbar + 1) lies in I (A acts trivially modulo I)
        gbar = [x for x in range(T.n) if x not in Aidx][0]
        found = False
        for a in Aidx:
            d = T.unit(gbar) - e + T.unit(a) - e
            if (T.rmul(d, gbar) + d) in I:
                found = True
        check(found == split, 'th:group-module-extensions: the module '
              'extension of %s splits iff the group extension does' % name)

    # Lemma 5.5: (gbar a)^n = gbar^n a^(s_n(g)); G = Z acting on A = Z^2 by
    # a matrix, the semidirect product with (g, a)(h, b) = (g h, a h + b).
    for M in [[[2, 1], [1, 1]], [[0, -1], [1, 0]], [[1, 1], [0, 1]]]:
        M = matrix(ZZ, M)
        for _ in range(5):
            a = vector(ZZ, [random.randint(-5, 5) for _ in range(2)])
            x = (0, a)
            p = (0, vector(ZZ, [0, 0]))
            for n in range(1, 7):
                p = (p[0] + 1, p[1] * M + a)   # p * (g, a), g = generator
                s = sum((M ** j for j in range(n)), matrix.zero(ZZ, 2))
                check(p[0] == n and p[1] == a * s,
                      'lem:unique-roots-extension: (g a)^%d = g^%d a^s_n' %
                      (n, n))
    # exc:q-group-extension: s_0(g) = 0, so c s_0(g) = a has no solution for
    # a != 0: the printed "for any n in Z" fails at n = 0 (C221).
    refuted(any(c * 0 == 1 for c in range(-5, 6)),
            'ex. 3.5.5 with n = 0: c s_0(g) = a solvable for a = 1')
    # p. 146: "for any n in Z the equation x^n = g has at most one solution"
    # fails at n = 0, g = 1 in every non-trivial group (here Z_2).
    refuted(len([x for x in range(2) if (0 * x) % 2 == 0]) <= 1,
            'p. 146: x^0 = 1 has at most one solution in Z_2')

    # prop:unique-roots-split-embedding: with C the coinduced module
    # Hom(Z G, A) the semidirect product G C need not satisfy uniqueness of
    # roots: G = Z = <g>, A = Z trivial (Gbar = Z^2 does), c(x) = (-1)^x
    # satisfies c s_2(g) = 0, (c r)(x) = c(r x).
    window = range(-20, 20)
    c = {x: (-1) ** (x % 2) for x in range(-21, 22)}
    check(all(c[x] + c[x + 1] == 0 for x in window),
          'coinduced C: c s_2(g) = 0 for c(x) = (-1)^x, c != 0')

    # exc:adjoining-p-th-root, first bullet (C223): Ghat = <x>, G = <x^p>,
    # A = Z G, B = Z[x, x^-1], A (x) 1 = span of x^(p i).  For g = x^j with
    # p not dividing j the projection of s_n(g) to A (x) 1 is s_k(g^p) with
    # n = p k - r, 0 <= r < p.
    L = LaurentPolynomialRing(ZZ, 'x')
    x = L.gen()

    def s(n, y):
        return sum((y ** i for i in range(n)), L(0))

    def proj(f, p):
        return sum((c * x ** e for e, c in f.dict().items() if e % p == 0),
                   L(0))
    for p in [2, 3, 5, 7]:
        for j in [j for j in range(-2 * p, 2 * p + 1) if j % p]:
            g = x ** j
            for n in range(1, 31):
                k = -(-n // p)                 # n = p k - r, 0 <= r < p
                r = p * k - n
                check(0 <= r < p and proj(s(n, g), p) == s(k, g ** p),
                      'ex. 3.5.6: projection of s_%d(x^%d), p = %d'
                      % (n, j, p))
    # the printed n = p k + r (0 <= r < p) gives s_k(g^p) with k = n div p:
    p, n = 2, 3
    refuted(proj(s(n, x), p) == s(n // p, x ** p),
            'ex. 3.5.6 with n = p k + r: p = 2, n = 3')
    # third bullet: s_n(g) s_m(g^n) = s_n(g^m) s_m(g); second bullet:
    # t^k s_p(t) = s_p(t), s_p(t)^l = p^(l-1) s_p(t) in Z[t]/(t^p - 1)
    for n in range(1, 13):
        for m in range(1, 13):
            check(s(n, x) * s(m, x ** n) == s(n, x ** m) * s(m, x),
                  'ex. 3.5.6: s_n(g) s_m(g^n) = s_n(g^m) s_m(g), n = %d, '
                  'm = %d' % (n, m))
    P = PolynomialRing(ZZ, 't')
    t = P.gen()
    for p in [2, 3, 5, 7]:
        Rq = P.quotient(t ** p - 1, 'u')
        u = Rq.gen()
        sp = sum((u ** i for i in range(p)), Rq(0))
        check(all(u ** k * sp == sp for k in range(2 * p)),
              'ex. 3.5.6: t^k s_p(t) = s_p(t), p = %d' % p)
        check(all(sp ** l == p ** (l - 1) * sp for l in range(1, 7)),
              'ex. 3.5.6: s_p(t)^l = p^(l-1) s_p(t), p = %d' % p)


def main():
    section_1()
    section_2_3()
    section_4()
    section_5()
    print('ok %s: %d checks' % (SCOPE, COUNT[0]))


if __name__ == '__main__':
    main()
