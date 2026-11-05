"""Exact checks of Chapter 1, §§ 8-10 (printed pp. 41-60) of Yu. V. Kuzmin,
"Гомологическая теория групп" (Moscow: Factorial Press, 2006).

Run from the project root: sage -python checks/sage/chapter-1b.py
(plain asserts; do not use -O).  The last line is "ok chapter-1b: N checks".
Pages are the printed pages; labels are those of content/01-*.typ.
Conventions as in chapter-1a.py (right modules, a^g = g^(-1) a g, [x, y] =
x^(-1) y^(-1) x y); Fox derivatives are the book's right derivations,
d(v w) = (dv) w + dw (1.28).  Finite groups come from GAP (libgap; packages
no GAP packages), modules are Z_m^k with integer matrices
acting from the right, extensions are groups of pairs built from 2-cocycles
(§ 8).  The 16 standard extensions are all classes of Z_2^2 by Z_2 (8),
Z_2 by Z_4 with inversion (D_8, Q_8), Z_4 by Z_2 (2), S_3 by F_2^2 (split),
S_3 by Z_3 (1) and S_3 by Z_2 (2), with normalised cocycles.  Fox
derivatives are computed in two independent ways: by the sum over the
letters of a word, and from the definition through the semidirect product
F P of § 9.  Expected values are the book's statements; printed readings
that are wrong are kept as refuted checks beside the corrected ones.

What is checked, by section:

section_8 (pp. 41-49): for all functions h: G x G -> A of 4 small (G, A),
  associativity of the pair multiplication on the elements (g, 1) <=>
  eq:cocycle-identity, and every cocycle gives a group; a change of
  transversal g -> g-bar phi(g) adds eq:coboundary (11 extensions);
  cohomologous cocycles give equivalent extensions; classes of extensions
  <-> H^2: the 8 extensions of Z_2^2 by Z_2 are Z_2^3, Z_4 x Z_2 (3),
  D_8 (3), Q_8 (1), and H^2(Z_2, Z_4 with inversion) gives D_8 and Q_8;
  eq:cocycle-identity-ring, h(r, t) = h(r - eps r, t - eps t),
  eq:cocycle-identity-augmentation, eq:coboundary-ring and
  eq:coboundary-augmentation for random r, s, t in ZG (16 extensions);
  prop:cocycles-augmentation-homs: the solutions of (1.17) on
  Delta (x) Delta have the dimension of the normalised cocycles and (1.19)
  gives the normalised coboundaries (8 pairs (G, F_p-module));
  prop:central-cocycles-tensor for all 23 groups of order 2-12 and
  A = Z_2, Z_3, Z_4, Z_6: |Hom(Delta (x)_G Delta, A)| |Hom(G_ab, A)| /
  |Hom(Delta, A)| = |H^2(G, A)| from cocycles = |Hom(M(G), A)|
  |Ext(G_ab, A)| from GAP's Schur multiplier M(G); the kernel of
  Delta (x)_G Delta -> Delta is M(G); prop:coinduced-kernel-splits
  (H^2(G, Hom(ZG, F_p)) = 0 for Z_2, Z_3, Z_4, Z_2^2, S_3, p = 2, 3, and
  h + delta(-phi) = 0 for phi(g)(g') = h(g, g')(1), "с изменённым знаком");
  prop:embedding-into-wreath with exc:wreath-embedding-explicit (a -> f_a,
  g-bar -> g f_g is an injective homomorphism into A Wr G, 10 extensions);
  prop:h2-finite-exponent: for 12 pairs (G, A) the proof's
  phi(t) = h(sigma - n, t) gives delta phi = n h on generators of the
  normalised cocycles (Smith form, any m), the bound is attained for
  H^2(Z_n, Z_n); cor:h2-divisible-vanishes (5 examples); th:schur, proof:
  for all groups of order <= 120 (64, 96 skipped), every normal Hall
  subgroup H and every p dividing |H|, the Sylow p-subgroups of G-bar are
  those of H (correction of p. 46: not of G = G-bar / H) and the two index
  identities hold; exc:abelian-extensions-ext (5 abelian G: G-bar abelian
  <=> h symmetric, coboundaries symmetric, the abelian classes form a
  subgroup); exc:h2-free-abelian-rank-two: G_1 with z = [x, y] eliminated
  is UT_3(Z) (normal form y^b x^a c^k, distinct images; class 2, Hirsch
  length 3); exc:commutator-form: [g1-bar, g2-bar] = h(g1, g2) - h(g2, g1),
  bilinear and alternating (5 abelian G); exc:h2-free-abelian-lambda:
  dim H^2(Z^n, F_2) = C(n, 2) = the dimension of the alternating forms,
  while the forms with f(x, y) = -f(y, x) have dimension C(n, 2) + n
  (n <= 4, cubical torus T^n = K(Z^n, 1); refuted for that reading), H^2(Z^n, Z) = Z^C(n,2), the
  counts of forms (n <= 3), bilinear functions are cocycles and symmetric
  ones are coboundaries (polynomial identities, n = 2, 3);
  exc:ext-lambda-sequence for all 24 abelian groups of order 2-16 and
  A = Z_2, Z_3, Z_4: |H^2| = |Ext| |Alt|, Ext = classes of symmetric
  cocycles of order prod gcd(n_i, m), the image of alpha is the group of
  alternating forms; the reading with f(x, y) = -f(y, x) refuted wherever
  the two kinds of forms differ; the counterexample of the proposed note
  (H^2(Z_2, Z_2) = Ext); the same family in ch. 5: Z^n (x) Z^n modulo
  x (x) y + y (x) x is Z^C(n,2) + Z_2^n, modulo the alternating relations
  Lambda^2 Z^n (n <= 4); exc:automorphism-factor-system (for all
  automorphisms f of G-bar with f(A) = A, at most 400 per group, of 10
  extensions: f^* h is the factor system of g -> f(f^-1(g)-bar) and is
  cohomologous to h); exc:inner-automorphism-coboundary (alpha_x^* h =
  h + delta phi, phi(g) = h(x g x^-1, x) - h(x, g), alpha_x(y) = x^-1 y x,
  x in G-bar, 10 extensions).
section_9 (pp. 49-57): eq:power-semidirect (correction g -> g^n; printed
  reading refuted) and eq:commutator-semidirect in S_3 x| F_2^2 and
  Z_4 x| Z_5; eq:fox-power, eq:fox-commutator (correction x^2 -> x_2;
  printed reading refuted), eq:fox-generators, eq:fox-inverses; the two
  computations of the derivatives agree, eq:fox-derivation and
  eq:fox-identity (300 random words); eq:word-values-semidirect and
  eq:fox-identity-values (60 random words each); prop:word-values-extension
  with 1-bar = 1 (16 extensions, 25 random words each) and refuted for a
  transversal with 1-bar != 1 (correction p. 52); exm:nilpotent-semidirect
  (gamma_(n+1)(G A) = gamma_(n+1)(G) (A Delta^n), n <= 5, 7 pairs);
  d c_(n+1)(G) = Delta_G^n (n <= 3; n <= 2 for A_4) and d c^((2))(G) =
  Delta_G Delta_(G') for Z_4, S_3, D_8, Q_8, A_4, as lattices in ZG;
  exc:fox-product-rule (V = {[x1, x2]}, W = {x3}); exc:fox-commutator-with-
  variable (V = {x^2}); exc:centrally-metabelian-semidirect for S_3, D_8,
  Q_8 (G'' = 1 only); prop:verbal-semidirect (3 semidirect products,
  v = x^2, x^4, [x1, x2]); prop:identities-in-extension, exhaustive over all
  normalised cocycles of 6 small (G, A) and 6 words; exc:derivative-values-
  not-defined; exc:fox-chain-rule: the corrected order holds on 200 random
  substitutions and the example v = y^2, w = x1 x2, the printed order is
  refuted; exc:fox-commutator-powers; exc:trefoil-figure-eight: Alexander
  polynomials x^2 - x + 1 and x^2 - 3x + 1, G_ab = Z, columns of the
  Alexander matrix summing to 0, minors equal up to sign; the Wirtinger
  relations of p. 55: none of the 64 presentations with 4 generators and
  relations x_(k(i))^(-1) x_i x_(k(i)) = x_(i+1) has the Alexander
  polynomial of the figure-eight knot (printed form refuted), with
  exponents +-1 it occurs; the 84 prime knots with at most 9 crossings:
  the Alexander polynomials of Sage's knot table (braid closures) agree
  with the printed table of D. Rolfsen, Knots and Links (1976),
  Appendix C, pp. 391-399, copied below; exactly 5 pairs share a
  polynomial, (6_1, 9_46), (7_4, 9_2), (8_14, 9_8), (8_18, 9_24),
  (9_28, 9_29) (printed "три пары" refuted).
section_10 (pp. 57-60): exm:nilpotent-class-two-endomorphisms and
  lem:central-quotient-identity (all endomorphisms x -> x a, a in G', of 6
  groups of class 2 fix G'); th:endomorphism-extension by brute force (11
  extensions, all G-module endomorphisms f: an extension exists <=>
  (f^* - 1) h_E = 0, then there are |Der(G, A)| of them and f-bar_2 =
  phi f-bar_1 with phi(x) = x u_2(x) u_1(x)^-1 in Aut E; the printed
  f-bar_2 = f-bar_1 phi refuted on Z_2 x Z_2, f = 0);
  lem:endomorphism-combination (6 extensions); prop:central-power-extension
  in the corrected form (eps(r) - 1) h_E = 0 for the 12 extensions with
  abelian G and all r with coefficients in [-1, 2]; the printed "finite
  order dividing eps(r) - 1" refuted by G = Z^2, A = Z, E_1, r = 1 (m h_(E_1)
  = h_(E_m) != 0); eq:inner-endomorphism and exc:inner-endomorphism-
  representatives (corrected a = prod a_i^(n_i), 6 extensions; the printed
  a = prod a_i refuted on D_8 with r = 2 g - 1); exc:inner-endomorphisms-
  semigroup and exc:inner-endomorphisms-metabelian (7 extensions);
  exc:homomorphism-lifting (all homomorphisms from 8 groups B of order <= 8
  into G, 8 extensions: f lifts <=> f^* h = 0 in H^2(B, A)).

What these checks do NOT establish.  Every check is an exact computation for
the listed groups, modules, words and parameters, exhaustive only where so
stated, or a polynomial identity; none proves a general theorem of the
book.  Random words and elements are drawn with a fixed seed.  The knot
table: the 84 polynomials are compared with the copy of Rolfsen's
table kept in this script (checked by eye against the printed pages for the
ten knots of the five pairs); the identification of the knots of Sage's
table with Rolfsen's names rests on that agreement.  Nothing here compares
our text with the printed book.
"""

import itertools
import random

from sage.all import (
    GF, QQ, ZZ, Integer, LaurentPolynomialRing, PolynomialRing, binomial,
    cubical_complexes, gcd, identity_matrix, libgap, matrix, prod, vector,
)

SCOPE = 'chapter-1b'
COUNT = [0]


def check(cond, what):
    assert bool(cond), 'FAILED: ' + what
    COUNT[0] += 1


def refuted(cond, what):
    assert not bool(cond), 'printed reading unexpectedly holds: ' + what
    COUNT[0] += 1


def gap(src):
    return libgap.eval(src)


GIN = gap('function(x, N) return x in N; end')


# ---------------------------------------------------------------------------
# Finite groups as multiplication tables, modules, group rings, cochains
# (as in chapter-1a.py)
# ---------------------------------------------------------------------------

class TGroup:
    """A finite group of GAP with its multiplication table (0-based)."""

    def __init__(self, G, name):
        self.G = G
        self.name = name
        el = G.AsSSortedList()
        self.gelts = el
        self.n = int(len(el))
        tab = gap('function(e) return List(e, g -> List(e, h -> '
                  'PositionSorted(e, g*h))); end')(el)
        self.mul = [[int(x) - 1 for x in row] for row in tab.sage()]
        self.e = [i for i in range(self.n)
                  if all(self.mul[i][j] == j for j in range(self.n))][0]
        self.inv = [[j for j in range(self.n) if self.mul[i][j] == self.e][0]
                    for i in range(self.n)]
        self.gens = [self.index(x) for x in G.GeneratorsOfGroup()]
        if not self.gens:
            self.gens = [self.e]

    def index(self, x):
        return int(gap('PositionSorted')(self.gelts, x)) - 1

    def conj(self, g, x):
        """x^(-1) g x"""
        return self.mul[self.mul[self.inv[x]][g]][x]

    def power(self, g, k):
        r = self.e
        if k < 0:
            g, k = self.inv[g], -k
        for _ in range(k):
            r = self.mul[r][g]
        return r


def small(o, i):
    return TGroup(gap('SmallGroup(%d,%d)' % (o, i)), 'SmallGroup(%d,%d)' % (o, i))


def cyclic(n):
    return TGroup(gap('CyclicGroup(IsPermGroup, %d)' % n) if n > 1
                  else gap('Group(())'), 'Z_%d' % n)


class Mod:
    """Z_m^k with a right action of a TGroup by integer matrices."""

    def __init__(self, T, m, k, act, name):
        self.T, self.m, self.k, self.name = T, m, k, name
        self.mats = [[[int(c) % m for c in row] for row in act(g)]
                     for g in range(T.n)]
        self.elts = list(itertools.product(range(m), repeat=k))
        self.zero = tuple([0] * k)
        for g in range(T.n):
            for h in range(T.n):
                gh = T.mul[g][h]
                assert all(self.act(self.act(a, g), h) == self.act(a, gh)
                           for a in self.basis())

    def basis(self):
        return [tuple(1 if i == j else 0 for i in range(self.k))
                for j in range(self.k)]

    def act(self, a, g):
        M, m = self.mats[g], self.m
        return tuple(sum(a[j] * M[j][i] for j in range(self.k)) % m
                     for i in range(self.k))

    def actr(self, a, r):
        """a r for r in ZG (a list of integer coefficients)."""
        out = [0] * self.k
        for g, c in enumerate(r):
            if c:
                b = self.act(a, g)
                for i in range(self.k):
                    out[i] += c * b[i]
        return tuple(x % self.m for x in out)

    def add(self, a, b):
        return tuple((x + y) % self.m for x, y in zip(a, b))

    def sub(self, a, b):
        return tuple((x - y) % self.m for x, y in zip(a, b))

    def smul(self, c, a):
        return tuple((c * x) % self.m for x in a)


def trivial(T, m, k=1):
    return Mod(T, m, k, lambda g: identity_matrix(ZZ, k).rows(),
               'trivial Z_%d^%d' % (m, k))


def zg_unit(T, g):
    r = [0] * T.n
    r[g] = 1
    return r


def zg_mul(T, r, s):
    out = [0] * T.n
    for g, c in enumerate(r):
        if c:
            row = T.mul[g]
            for h, d in enumerate(s):
                if d:
                    out[row[h]] += c * d
    return out


def zg_add(r, s, c=1):
    return [x + c * y for x, y in zip(r, s)]


def eps(r):
    return sum(r)


# ---------------------------------------------------------------------------
# Inhomogeneous cochains (book's coboundary, right action)
# ---------------------------------------------------------------------------

def tup_index(tup, N):
    r = 0
    for x in tup:
        r = r * N + x
    return r


def delta_dict(A, n):
    """Entries of delta: C^n -> C^(n+1), C^n = A^(G^n), with
    (delta f)(g_1..g_(n+1)) = f(g_1..g_n) g_(n+1)
        + sum_(i=1)^n (-1)^(n+1-i) f(.., g_i g_(i+1), ..)
        + (-1)^(n+1) f(g_2, .., g_(n+1));
    n = 1, 2 give the book's formulas (1.10) and (1.12), (1.13)."""
    T, k = A.T, A.k
    N = T.n
    d = {}

    def put(r, c, v):
        d[(r, c)] = d.get((r, c), 0) + v

    for tup in itertools.product(range(N), repeat=n + 1):
        ri = tup_index(tup, N)
        src = tup_index(tup[:n], N)
        M = A.mats[tup[n]]
        for i in range(k):
            for j in range(k):
                if M[j][i]:
                    put(ri * k + i, src * k + j, M[j][i])
        for i in range(1, n + 1):
            s = (-1) ** (n + 1 - i)
            t = list(tup[:i - 1]) + [T.mul[tup[i - 1]][tup[i]]] + list(tup[i + 1:])
            ci = tup_index(t, N)
            for j in range(k):
                put(ri * k + j, ci * k + j, s)
        ci = tup_index(tup[1:], N)
        for j in range(k):
            put(ri * k + j, ci * k + j, (-1) ** (n + 1))
    return d, N ** (n + 1) * k, N ** n * k


def is_prime_m(m):
    return Integer(m).is_prime()


def delta_matrix(A, n, ring):
    d, r, c = delta_dict(A, n)
    if ring is ZZ:
        return matrix(ZZ, r, c, {kk: v for kk, v in d.items() if v}, sparse=False)
    return matrix(ring, r, c, {kk: ring(v) for kk, v in d.items() if ring(v) != 0},
                  sparse=True)


def image_order(A, n):
    """|delta_n(C^n)| inside C^(n+1)."""
    m = A.m
    if is_prime_m(m):
        return Integer(m) ** delta_matrix(A, n, GF(m)).rank()
    D = delta_matrix(A, n, ZZ)
    return prod(Integer(m) // gcd(s, m) for s in D.elementary_divisors() if s)


def cochain_order(A, n):
    return Integer(A.m) ** (A.k * A.T.n ** n)


def h_order(A, n):
    """|H^n(G, A)| for n >= 1."""
    z = cochain_order(A, n) // image_order(A, n)
    b = image_order(A, n - 1)
    assert z % b == 0
    return z // b


def z1_list(A):
    """All derivations (brute force over values on generators, then
    verified on all pairs).  Returns dicts g -> a."""
    T = A.T
    out = []
    for vals in itertools.product(A.elts, repeat=len(T.gens)):
        # extend along words: BFS from identity
        phi = {T.e: A.zero}
        frontier = [T.e]
        ok = True
        while frontier and ok:
            new = []
            for g in frontier:
                for s, v in zip(T.gens, vals):
                    h = T.mul[g][s]
                    val = A.add(A.act(phi[g], s), v)
                    if h in phi:
                        if phi[h] != val:
                            ok = False
                            break
                    else:
                        phi[h] = val
                        new.append(h)
                if not ok:
                    break
            frontier = new
        if not ok or len(phi) != T.n:
            continue
        if all(phi[T.mul[g][h]] == A.add(A.act(phi[g], h), phi[h])
               for g in range(T.n) for h in range(T.n)):
            out.append(phi)
    return out


# ---------------------------------------------------------------------------
# Extensions from cocycles
# ---------------------------------------------------------------------------

def cocycle_ok(A, h):
    T = A.T
    return all(
        A.add(A.sub(A.act(h[(a, b)], c), h[(a, T.mul[b][c])]),
              A.sub(h[(T.mul[a][b], c)], h[(b, c)])) == A.zero
        for a in range(T.n) for b in range(T.n) for c in range(T.n))


def zero_cocycle(A):
    T = A.T
    return {(a, b): A.zero for a in range(T.n) for b in range(T.n)}


class Ext:
    """The group of pairs (g, a) with (g1, a1)(g2, a2) =
    (g1 g2, h(g1, g2) + a1 g2 + a2) (§ 8), as a permutation group."""

    def __init__(self, A, h):
        self.A, self.h, self.T = A, h, A.T
        T = A.T
        self.el = [(g, a) for g in range(T.n) for a in A.elts]
        self.ix = {x: i for i, x in enumerate(self.el)}
        perms = []
        for y in self.el:
            perms.append(libgap.PermList([self.ix[self.mul(x, y)] + 1 for x in self.el]))
        self.perm = perms
        self.P = libgap.Group(perms)

    def mul(self, x, y):
        (g1, a1), (g2, a2) = x, y
        A, T = self.A, self.T
        return (T.mul[g1][g2], A.add(A.add(self.h[(g1, g2)], A.act(a1, g2)), a2))

    def p(self, x):
        return self.perm[self.ix[x]]

    def one(self):
        T, A = self.T, self.A
        return (T.e, A.sub(A.zero, self.h[(T.e, T.e)]))

    def inverse(self, x):
        if not hasattr(self, '_inv'):
            one = self.one()
            self._inv = {}
            for u in self.el:
                for v in self.el:
                    if self.mul(u, v) == one:
                        self._inv[u] = v
                        break
        return self._inv[x]


ONPOINTS = libgap.eval('function(i, p) return i^p; end')


def perm_to_el(E, p):
    """The element y of E with p = (x -> x y): y = one * y."""
    one = E.ix[E.one()]
    return E.el[int(ONPOINTS(one + 1, p)) - 1]


def normalise(A, h):
    """h + delta(phi) with phi = -h(1, 1): h(1, g) = h(g, 1) = 0."""
    T = A.T
    c = h[(T.e, T.e)]
    return {(a, b): A.sub(h[(a, b)], A.act(c, b)) for (a, b) in h}


def endo_images(E, gimgs, f):
    """The group homomorphism of E.P sending (g_j, 0) -> gimgs[j] and
    (1, b) -> (1, f(b)) for basis vectors b, or fail (h normalised)."""
    T, A = E.T, E.A
    gens, imgs = [], []
    for g, im in zip(T.gens, gimgs):
        gens.append(E.p((g, A.zero)))
        imgs.append(E.p(im))
    for b in A.basis():
        gens.append(E.p((T.e, b)))
        imgs.append(E.p((T.e, f(b))))
    return libgap.GroupHomomorphismByImages(E.P, E.P, gens, imgs)

def h2_reps(A):
    """Representatives of H^2(G, A) over GF(p): list of cocycle dicts."""
    T, p, k = A.T, A.m, A.k
    F = GF(p)
    D2 = delta_matrix(A, 2, F)
    D1 = delta_matrix(A, 1, F)
    Z = D2.right_kernel().basis_matrix()
    B = D1.column_space().basis_matrix() if D1.rank() else matrix(F, 0, D2.ncols())
    # complement of B in Z
    cur = B
    comp = []
    for z in Z.rows():
        test = cur.stack(matrix(F, [z])) if cur.nrows() else matrix(F, [z])
        if test.rank() > cur.rank():
            cur = test
            comp.append(z)
    reps = []
    for coeffs in itertools.product(range(p), repeat=len(comp)):
        v = sum((c * z for c, z in zip(coeffs, comp)), vector(F, D2.ncols()))
        h = {}
        N = T.n
        for a in range(N):
            for b in range(N):
                base = (a * N + b) * k
                h[(a, b)] = tuple(int(v[base + j]) for j in range(k))
        h = normalise(A, h)
        assert cocycle_ok(A, h)
        reps.append(h)
    return reps


def coboundary_cocycle(A, phi):
    T = A.T
    return {(a, b): A.add(A.sub(A.act(phi[a], b), phi[T.mul[a][b]]), phi[b])
            for a in range(T.n) for b in range(T.n)}


def h2_reps_bruteforce(A):
    """All cohomology classes for tiny (T, A) by brute force over normalised
    cochains."""
    T = A.T
    pairs = [(a, b) for a in range(T.n) for b in range(T.n) if a != T.e and b != T.e]
    cocs = []
    for vals in itertools.product(A.elts, repeat=len(pairs)):
        h = {(a, b): A.zero for a in range(T.n) for b in range(T.n)}
        h.update(dict(zip(pairs, vals)))
        if cocycle_ok(A, h):
            cocs.append(h)
    bnd = set()
    for vals in itertools.product(A.elts, repeat=T.n - 1):
        phi = {T.e: A.zero}
        phi.update(dict(zip([g for g in range(T.n) if g != T.e], vals)))
        d = coboundary_cocycle(A, phi)
        bnd.add(tuple(d[q] for q in sorted(d)))
    reps, seen = [], []
    for h in cocs:
        key = tuple(h[q] for q in sorted(h))
        if any(tuple(A.sub(x, y) for x, y in zip(key, s)) in bnd for s in seen):
            continue
        seen.append(key)
        reps.append(h)
    return reps




def mod_s3_f2():
    T = small(6, 1)
    iso = libgap.IsomorphismGroups(T.G, gap('GL(2,2)'))
    conv = gap('function(i, x) return List(Image(i, x), r -> List(r, IntFFE)); end')
    mats = [[[int(c) for c in row] for row in conv(iso, gx).sage()] for gx in T.gelts]
    return T, Mod(T, 2, 2, lambda g: mats[g], 'F_2^2 natural for GL_2(2) = S_3')


def mod_z4_on_z5():
    T = cyclic(4)
    g = T.gens[0]
    mats = {T.power(g, k): [[pow(2, k, 5)]] for k in range(4)}
    return T, Mod(T, 5, 1, lambda h: mats[h], 'Z_5, generator acting by 2')


def inversion(T, m):
    """Z_2 (or a group with a sign) acting on Z_m by inversion."""
    return Mod(T, m, 1, lambda g: [[1 if g == T.e else -1]], 'Z_%d, inversion' % m)


def normalised_cocycles(A, limit=None):
    """All normalised 2-cocycles over GF(p) (or a random sample of `limit`)."""
    T, p, k = A.T, A.m, A.k
    F = GF(p)
    D2 = delta_matrix(A, 2, F)
    N = T.n
    # restrict to normalised coordinates: (a, b) with a, b != e
    keep = [((a * N + b) * k + j) for a in range(N) for b in range(N) if a != T.e and b != T.e
            for j in range(k)]
    D = D2.matrix_from_columns(keep)
    Z = D.right_kernel().basis_matrix()
    dim = Z.nrows()
    out = []
    if limit is None or p ** dim <= limit:
        coeff_iter = itertools.product(range(p), repeat=dim)
    else:
        coeff_iter = (tuple(random.randrange(p) for _ in range(dim)) for _ in range(limit))
    for coeffs in coeff_iter:
        v = sum((c * z for c, z in zip(coeffs, Z.rows())), vector(F, len(keep)))
        h = zero_cocycle(A)
        idx = 0
        for a in range(N):
            for b in range(N):
                if a != T.e and b != T.e:
                    h[(a, b)] = tuple(int(v[idx + j]) for j in range(k))
                    idx += k
        out.append(h)
    return out, dim


def normalised_cocycle_gens(A):
    """Generators of the group of normalised 2-cocycles with values in Z_m^k
    (any m), from the Smith form D = U S V of the cocycle condition on the
    normalised coordinates: x = V y with S y = 0 mod m."""
    T, m, k = A.T, A.m, A.k
    N = T.n
    D2 = delta_matrix(A, 2, ZZ)
    keep = [((a * N + b) * k + j) for a in range(N) for b in range(N) if a != T.e and b != T.e
            for j in range(k)]
    D = D2.matrix_from_columns(keep)
    S, U, V = D.smith_form()
    gens = []
    for i in range(D.ncols()):
        s = S[i, i] if i < min(S.nrows(), S.ncols()) else 0
        c = m // gcd(s, m) if s else 1
        y = vector(ZZ, D.ncols())
        y[i] = c
        x = V * y
        if all(v % m == 0 for v in x):
            continue
        h = zero_cocycle(A)
        idx = 0
        for a in range(N):
            for b in range(N):
                if a != T.e and b != T.e:
                    h[(a, b)] = tuple(int(x[idx + j]) % m for j in range(k))
                    idx += k
        assert cocycle_ok(A, h)
        gens.append(h)
    return gens


def in_b2(A, diff):
    """Is the 2-cochain diff (dict) a coboundary? (GF(p))"""
    T, p, k = A.T, A.m, A.k
    F = GF(p)
    D1 = delta_matrix(A, 1, F)
    v = vector(F, [diff[(a, b)][j] for a in range(T.n) for b in range(T.n) for j in range(k)])
    M = D1.augment(matrix(F, v).transpose())
    return M.rank() == D1.rank()


def hsum(A, h, g, r):
    """h(g, r) for r in ZG (bilinear extension in the second argument)."""
    out = A.zero
    for x, c in enumerate(r):
        if c:
            out = A.add(out, A.smul(c, h[(g, x)]))
    return out


def hbil(A, h, r, t):
    out = A.zero
    for x, c in enumerate(r):
        if c:
            out = A.add(out, A.smul(c, hsum(A, h, x, t)))
    return out


def rand_zg(T, lo=-2, hi=2):
    return [random.randint(lo, hi) for _ in range(T.n)]


_EXT_CACHE = []


def pick(examples, per_label):
    """At most per_label examples of each kind (label), in order."""
    out, seen = [], {}
    for e in examples:
        k = e[3]
        if seen.get(k, 0) < per_label:
            seen[k] = seen.get(k, 0) + 1
            out.append(e)
    return out


def ext_examples():
    if not _EXT_CACHE:
        _EXT_CACHE.extend(_ext_examples())
    return _EXT_CACHE


def _ext_examples():
    """Normalised extensions used in §§ 8-10: (T, A, h, label)."""
    out = []
    T = small(4, 2)
    A = trivial(T, 2)
    for h in h2_reps(A):
        out.append((T, A, h, 'Z_2^2 by Z_2'))
    T = cyclic(2)
    A = inversion(T, 4)
    for h in h2_reps_bruteforce(A):
        out.append((T, A, h, 'Z_2 by Z_4 (inversion)'))
    T = cyclic(4)
    A = trivial(T, 2)
    for h in h2_reps(A):
        out.append((T, A, h, 'Z_4 by Z_2'))
    T, A = mod_s3_f2()
    out.append((T, A, zero_cocycle(A), 'S_3 by F_2^2'))
    T = small(6, 1)
    A = trivial(T, 3)
    for h in h2_reps(A):
        out.append((T, A, h, 'S_3 by Z_3'))
    T = small(6, 1)
    A = trivial(T, 2)
    for h in h2_reps(A):
        out.append((T, A, h, 'S_3 by Z_2'))
    return out


# ---------------------------------------------------------------------------
# section 8
# ---------------------------------------------------------------------------

def section_8():
    # associativity on (g, 1) <=> (1.12); every cocycle gives a group
    cases = [(cyclic(2), trivial(cyclic(2), 2)), (cyclic(3), trivial(cyclic(3), 2)),
             (cyclic(2), None), (cyclic(2), trivial(cyclic(2), 3))]
    T2 = cases[2][0]
    cases[2] = (T2, inversion(T2, 3))
    for (T, A) in cases:
        pairs = [(a, b) for a in range(T.n) for b in range(T.n)]
        nco = 0
        allok = True
        for vals in itertools.product(A.elts, repeat=len(pairs)):
            h = dict(zip(pairs, vals))

            def mul(x, y):
                (g1, a1), (g2, a2) = x, y
                return (T.mul[g1][g2], A.add(A.add(h[(g1, g2)], A.act(a1, g2)), a2))
            gen = [(g, A.zero) for g in range(T.n)]
            assoc = all(mul(mul(x, y), z) == mul(x, mul(y, z)) for x in gen for y in gen for z in gen)
            coc = cocycle_ok(A, h)
            allok = allok and (assoc == coc)
            if coc:
                nco += 1
                el = [(g, a) for g in range(T.n) for a in A.elts]
                full = all(mul(mul(x, y), z) == mul(x, mul(y, z)) for x in el for y in el for z in el)
                one = (T.e, A.sub(A.zero, h[(T.e, T.e)]))
                ident = all(mul(one, x) == x and mul(x, one) == x for x in el)
                inv = all(any(mul(x, y) == one for y in el) for x in el)
                allok = allok and full and ident and inv
        check(allok and nco > 0, 'p. 43: associativity on the (g, 1) <=> (1.12), and each of the %d '
              'cocycles gives a group (all functions h, %s, %s)' % (nco, T.name, A.name))
    # change of transversal adds delta phi (1.13)
    for (T, A, h, lab) in pick(ext_examples(), 3):
        E = Ext(A, h)
        for _ in range(3):
            phi = {g: random.choice(A.elts) for g in range(T.n)}
            new = {}
            for a in range(T.n):
                for b in range(T.n):
                    x = E.mul((a, phi[a]), (b, phi[b]))      # g1'' g2''
                    # = (g1 g2)'' * c, (g, phi(g)) (1, c) = (g, phi(g) + c)
                    assert x[0] == T.mul[a][b]
                    new[(a, b)] = A.sub(x[1], phi[T.mul[a][b]])
            d = coboundary_cocycle(A, phi)
            check(all(new[q] == A.add(h[q], d[q]) for q in h),
                  'p. 42: transversal g -> g-bar phi(g) has factor system h + delta phi (1.13) (%s)' % lab)
    # classes of extensions <-> H^2: Z_2^2 by Z_2 and Z_2 by Z_4
    T = small(4, 2)
    A = trivial(T, 2)
    reps = h2_reps(A)
    check(len(reps) == h_order(A, 2) == 8, 'p. 43: |H^2(Z_2^2, Z_2)| = 8 classes')
    ids = sorted(tuple(int(c) for c in gap('IdGroup')(Ext(A, h).P)) for h in reps)
    check(ids == sorted([(8, 5)] + [(8, 2)] * 3 + [(8, 3)] * 3 + [(8, 4)]),
          'p. 43: the 8 extensions of Z_2^2 by Z_2 are Z_2^3, Z_4 x Z_2 (3), D_8 (3), Q_8 (1)')
    T = cyclic(2)
    A = inversion(T, 4)
    reps = h2_reps_bruteforce(A)
    ids = sorted(tuple(int(c) for c in gap('IdGroup')(Ext(A, h).P)) for h in reps)
    check(ids == [(8, 3), (8, 4)] and h_order(A, 2) == 2,
          'p. 43: H^2(Z_2, Z_4 with inversion) = Z_2: D_8 (split) and Q_8')
    # cohomologous cocycles give equivalent extensions: (g, 1) -> (g, phi(g)) is an isomorphism
    for (T, A, h, lab) in pick(ext_examples(), 2):
        phi = {g: random.choice(A.elts) for g in range(T.n)}
        phi[T.e] = A.zero
        d = coboundary_cocycle(A, phi)
        h2 = {q: A.add(h[q], d[q]) for q in h}
        E1, E2 = Ext(A, h), Ext(A, h2)
        # isomorphism E2 -> E1 : (g, a) -> (g, phi(g) + a), identity on A and on G
        F = {x: (x[0], A.add(phi[x[0]], x[1])) for x in E2.el}
        ok = all(F[E2.mul(x, y)] == E1.mul(F[x], F[y]) for x in E2.el for y in E2.el)
        check(ok, 'p. 43: h + delta phi gives an equivalent extension, (g, 1) -> (g, phi(g)) (%s)' % lab)
    # (1.16), normalisation, (1.17), (1.18), (1.19)
    for (T, A, h, lab) in ext_examples():
        for _ in range(4):
            r, s, t = rand_zg(T), rand_zg(T), rand_zg(T)
            lhs = A.add(A.sub(A.actr(hbil(A, h, r, s), t), hbil(A, h, r, zg_mul(T, s, t))),
                        A.sub(hbil(A, h, zg_mul(T, r, s), t), A.smul(eps(r), hbil(A, h, s, t))))
            check(lhs == A.zero, 'eq:cocycle-identity-ring for random r, s, t (%s)' % lab)
            r0 = zg_add(r, zg_unit(T, T.e), -eps(r))
            t0 = zg_add(t, zg_unit(T, T.e), -eps(t))
            check(hbil(A, h, r, t) == hbil(A, h, r0, t0),
                  'p. 43: h(r, t) = h(r - eps(r), t - eps(t)) for normalised h (%s)' % lab)
            lhs = A.add(A.sub(A.actr(hbil(A, h, r0, s), t), hbil(A, h, r0, zg_mul(T, s, t))),
                        hbil(A, h, zg_mul(T, r0, s), t))
            check(lhs == A.zero, 'eq:cocycle-identity-augmentation, r in Delta (%s)' % lab)
            phi = {g: random.choice(A.elts) for g in range(T.n)}
            phi[T.e] = A.zero
            d = coboundary_cocycle(A, phi)

            def phis(x):
                out = A.zero
                for g, c in enumerate(x):
                    out = A.add(out, A.smul(c, phi[g]))
                return out
            lhs = hbil(A, d, r, t)
            rhs = A.add(A.sub(A.actr(phis(r), t), phis(zg_mul(T, r, t))), A.smul(eps(r), phis(t)))
            check(lhs == rhs, 'eq:coboundary-ring (%s)' % lab)
            lhs = hbil(A, d, r0, t0)
            rhs = A.sub(A.actr(phis(r0), t0), phis(zg_mul(T, r0, t0)))
            check(lhs == rhs, 'eq:coboundary-augmentation, r, t in Delta (%s)' % lab)
    # prop:cocycles-augmentation-homs: solutions of (1.17) on Delta (x) Delta vs normalised cocycles
    pairs8 = [(small(4, 2), trivial(small(4, 2), 2)), (cyclic(4), trivial(cyclic(4), 2)),
              (small(6, 1), trivial(small(6, 1), 3)), mod_s3_f2(), (cyclic(3), trivial(cyclic(3), 3)),
              mod_z4_on_z5(), (cyclic(2), inversion(cyclic(2), 3)), (small(8, 3), trivial(small(8, 3), 2))]
    for (T, A) in pairs8:
        p, k, N = A.m, A.k, T.n
        F = GF(p)
        nz = [g for g in range(N) if g != T.e]
        pos = {g: i for i, g in enumerate(nz)}

        def coords(x):     # x in Delta (eps = 0) -> coordinates on the basis g - 1
            return {g: x[g] for g in nz if x[g]}
        b = {g: zg_add(zg_unit(T, g), zg_unit(T, T.e), -1) for g in nz}
        nv = len(nz) * len(nz) * k

        def var(gi, gj, c):
            return (pos[gi] * len(nz) + pos[gj]) * k + c
        rows = []
        for gr in nz:
            for gs in nz:
                for gt in nz:
                    r, s, t = b[gr], b[gs], b[gt]
                    st, rs = zg_mul(T, s, t), zg_mul(T, r, s)
                    for c in range(k):          # output coordinate c
                        row = {}

                        def add(key, val):
                            row[key] = row.get(key, 0) + val
                        # h(r (x) s) t : coordinate c of (h(r,s) as vector) * M_t
                        for x, cx in enumerate(t):
                            if cx:
                                M = A.mats[x]
                                for j in range(k):
                                    if M[j][c]:
                                        add(var(gr, gs, j), cx * M[j][c])
                        for g2, cc in coords(st).items():
                            add(var(gr, g2, c), -cc)
                        for g1, cc in coords(rs).items():
                            add(var(g1, gt, c), cc)
                        rows.append(row)
        Msys = matrix(F, len(rows), nv, {(i, kk): F(v) for i, row in enumerate(rows)
                                          for kk, v in row.items() if F(v) != 0}, sparse=True)
        dim_sol = nv - Msys.rank()
        cocs, dim_norm = normalised_cocycles(A, limit=0)
        check(dim_sol == dim_norm, 'prop:cocycles-augmentation-homs: dim of solutions of (1.17) on '
              'Delta (x) Delta = dim of normalised 2-cocycles = %d (%s, %s)' % (dim_norm, T.name, A.name))
        # coboundaries: (1.19) on phi in Hom(Delta, A) = normalised coboundaries (1.13)
        ok = True
        for _ in range(5):
            phi = {g: random.choice(A.elts) for g in range(N)}
            phi[T.e] = A.zero
            d = coboundary_cocycle(A, phi)
            for gr in nz:
                for gt in nz:
                    r, t = b[gr], b[gt]
                    rt = zg_mul(T, r, t)
                    val = A.sub(A.actr(phi[gr], t), sum_phi(A, phi, rt))
                    ok = ok and val == d[(gr, gt)]
        check(ok, 'prop:cocycles-augmentation-homs: delta phi(r (x) t) = phi(r) t - phi(r t) on the '
              'basis g - 1 equals the normalised coboundary (1.13) (%s, %s)' % (T.name, A.name))
    # prop:central-cocycles-tensor and the Schur multiplier
    ng = 0
    for o in range(2, 13):
        for i in range(1, int(gap('NumberSmallGroups(%d)' % o)) + 1):
            T = small(o, i)
            N = T.n
            nz = [g for g in range(N) if g != T.e]
            pos = {g: j for j, g in enumerate(nz)}
            M = len(nz)

            def dcoords(x):
                return {g: x[g] for g in nz if x[g]}
            b = {g: zg_add(zg_unit(T, g), zg_unit(T, T.e), -1) for g in nz}
            rel = []
            for gi in nz:
                for gj in nz:
                    for g in range(N):
                        if g == T.e:
                            continue
                        left = dcoords(zg_mul(T, b[gi], zg_unit(T, g)))
                        right = dcoords(zg_mul(T, zg_unit(T, g), b[gj]))
                        v = [0] * (M * M)
                        for g1, c in left.items():
                            v[pos[g1] * M + pos[gj]] += c
                        for g2, c in right.items():
                            v[pos[gi] * M + pos[g2]] -= c
                        rel.append(v)
            R = matrix(ZZ, rel)
            ed = [d for d in R.elementary_divisors() if d != 1]
            free = M * M - R.rank()
            tors = [d for d in ed if d != 0]
            # multiplication mu: Delta (x)_G Delta -> Delta, kernel = K / R
            mu = matrix(ZZ, M * M, M)
            for gi in nz:
                for gj in nz:
                    for g, c in dcoords(zg_mul(T, b[gi], b[gj])).items():
                        mu[pos[gi] * M + pos[gj], pos[g]] += c
            K = mu.left_kernel().basis_matrix()
            coeffs = K.solve_left(R).change_ring(ZZ)      # R rows in the (integral) basis of K
            kinv = [int(d) for d in coeffs.elementary_divisors() if d not in (0, 1)]
            mult = sorted(int(c) for c in gap('AbelianInvariantsMultiplier')(T.G))
            kinv_std = sorted(int(c) for c in gap('AbelianInvariants(AbelianGroup(%s))' % kinv))
            check(kinv_std == mult and coeffs.rank() == K.nrows(),
                  'Schur multiplier: Ker(Delta (x)_G Delta -> Delta) = M(G) = %s (%s)' % (mult, T.name))
            gab = [int(c) for c in T.G.AbelianInvariants()]
            for m in [2, 3, 4, 6]:
                homQ = Integer(m) ** free * prod(gcd(d, m) for d in tors)
                homGab = prod(gcd(d, m) if d else m for d in gab)
                prop = homQ * homGab // Integer(m) ** M
                coc = h_order(trivial(T, m), 2)
                uct = prod(gcd(d, m) for d in mult) * prod(gcd(d, m) if d else m for d in gab)
                check(prop == coc == uct,
                      'prop:central-cocycles-tensor: |H^2(%s, Z_%d)| = |Hom(Delta (x)_G Delta, Z_%d)| '
                      '|Hom(G_ab, Z_%d)| / |Hom(Delta, Z_%d)| = %d (cocycles; UCT with M(G))'
                      % (T.name, m, m, m, m, coc))
            ng += 1
    check(ng == int(gap('Sum([2..12], NumberSmallGroups)')),
          'prop:central-cocycles-tensor: all %d groups of order 2..12' % ng)
    # prop:coinduced-kernel-splits
    for (o, i) in [(2, 1), (3, 1), (4, 1), (4, 2), (6, 1)]:
        T = small(o, i)
        for p in [2, 3]:
            A = Mod(T, p, T.n, lambda g: [[1 if j == T.mul[g][hh] else 0 for hh in range(T.n)]
                                          for j in range(T.n)], 'Hom(ZG, F_%d)' % p)
            check(h_order(A, 2) == 1, 'prop:coinduced-kernel-splits: H^2(%s, Hom(ZG, F_%d)) = 0' % (T.name, p))
            cocs, dim = normalised_cocycles(A, limit=6)
            ok = True
            for h in cocs:
                # phi(g)(g') = h(g, g')(1); then h + delta(-phi) = 0
                phi = {g: tuple((-h[(g, g1)][T.e]) % p for g1 in range(T.n)) for g in range(T.n)}
                d = coboundary_cocycle(A, phi)
                ok = ok and all(A.add(h[q], d[q]) == A.zero for q in h)
            check(ok, 'prop:coinduced-kernel-splits, proof: with phi(g)(g\') = h(g, g\')(1) and the sign '
                  'changed, h + delta(-phi) = 0 (%s, F_%d)' % (T.name, p))
    # prop:embedding-into-wreath, exc:wreath-embedding-explicit
    for (T, A, h, lab) in pick(ext_examples(), 2):
        E = Ext(A, h)

        def fa(a):
            return tuple(A.act(a, g) for g in range(T.n))

        def fg(g):
            return tuple(h[(g, g1)] for g1 in range(T.n))

        def wmul(x, y):     # A Wr G = G Hom(ZG, A): (g1, f1)(g2, f2) = (g1 g2, f1 g2 + f2)
            (g1, f1), (g2, f2) = x, y
            return (T.mul[g1][g2], tuple(A.add(f1[T.mul[g2][g3]], f2[g3]) for g3 in range(T.n)))

        def mu(x):          # g-bar a -> (g, f_g + f_a)
            g, a = x
            return (g, tuple(A.add(u, v) for u, v in zip(fg(g), fa(a))))
        ok = all(mu(E.mul(x, y)) == wmul(mu(x), mu(y)) for x in E.el for y in E.el)
        inj = len(set(mu(x) for x in E.el)) == len(E.el)
        check(ok and inj, 'prop:embedding-into-wreath, exc:wreath-embedding-explicit: a -> f_a, '
              'g-bar -> g f_g is an embedding into A Wr G inducing the identity on G (%s)' % lab)
    # prop:h2-finite-exponent: delta psi = n h, psi(g) = h(sigma - n, g - 1) = sum_x h(x, g)
    pairs = [(small(4, 2), trivial(small(4, 2), 2)), (cyclic(4), trivial(cyclic(4), 2)),
             (cyclic(4), trivial(cyclic(4), 4)), (cyclic(2), inversion(cyclic(2), 4)),
             (small(6, 1), trivial(small(6, 1), 3)), (small(6, 1), trivial(small(6, 1), 2)),
             mod_s3_f2(), (small(8, 3), trivial(small(8, 3), 2)), (small(8, 4), trivial(small(8, 4), 2)),
             (cyclic(3), trivial(cyclic(3), 9)), (cyclic(9), trivial(cyclic(9), 3)),
             (small(8, 3), trivial(small(8, 3), 4))]
    for (T, A) in pairs:
        n = T.n
        cocs = normalised_cocycle_gens(A)       # generators: the identity is linear in h
        ok = True
        for h in cocs:
            psi = {g: A.zero for g in range(n)}
            for g in range(n):
                tot = A.zero
                for x in range(n):
                    tot = A.add(tot, A.sub(h[(x, g)], h[(x, T.e)]))
                tot = A.sub(tot, A.smul(n, A.sub(h[(T.e, g)], h[(T.e, T.e)])))
                psi[g] = tot
            d = coboundary_cocycle(A, psi)
            ok = ok and all(d[q] == A.smul(n, h[q]) for q in h)
        check(ok, 'prop:h2-finite-exponent: phi(t) = h(sigma - n, t) gives delta phi = n h on %d generators '
              'of the normalised cocycles, so n H^2 = 0 (%s, %s)' % (len(cocs), T.name, A.name))
        order = h_order(A, 2)
        check(all(n % p == 0 for p in Integer(order).prime_divisors()),
              'prop:h2-finite-exponent: |H^2(%s, %s)| = %d has only prime divisors of n = %d'
              % (T.name, A.name, order, n))
    # exponent exactly: H^2(Z_n, Z_n) = Z_n has an element of order n (carry cocycle)
    for nn in [2, 3, 4, 6]:
        T = cyclic(nn)
        A = trivial(T, nn)
        g = T.gens[0]
        carry = {(T.power(g, i), T.power(g, j)): (1 if i + j >= nn else 0,) for i in range(nn) for j in range(nn)}
        check(h_order(A, 2) == nn and cocycle_ok(A, carry),
              'prop:h2-finite-exponent: |H^2(Z_%d, Z_%d)| = %d, the bound n is attained' % (nn, nn, nn))
    # cor:h2-divisible-vanishes
    for (T, A) in [mod_z4_on_z5(), (cyclic(2), inversion(cyclic(2), 3)), (small(6, 1), trivial(small(6, 1), 5)),
                   (cyclic(3), trivial(cyclic(3), 4)), (small(4, 2), trivial(small(4, 2), 9))]:
        check(h_order(A, 2) == 1, 'cor:h2-divisible-vanishes: H^2(%s, %s) = 0' % (T.name, A.name))
    # th:schur: Sylow subgroups (correction p. 46) and the index identity
    fun = gap('''function(o)
      local res, i, G, H, p, S, N;
      res := [0, 0];
      for i in [1..NumberSmallGroups(o)] do
        G := SmallGroup(o, i);
        for H in NormalSubgroups(G) do
          if Size(H) > 1 and Size(H) < o and Gcd(Size(H), o / Size(H)) = 1 then
            for p in Set(Factors(Size(H))) do
              S := SylowSubgroup(H, p);
              N := Normalizer(G, S);
              res[1] := res[1] + 1;
              if Set(List(ConjugacyClassSubgroups(G, S), x -> x)) = Set(List(ConjugacyClassSubgroups(H, S), x -> x))
                 and Index(G, N) = Index(H, Intersection(H, N))
                 and Index(N, Intersection(H, N)) = Index(G, H)
                 and Size(SylowSubgroup(G / H, p)) = 1 then
                res[2] := res[2] + 1;
              fi;
            od;
          fi;
        od;
      od;
      return res;
    end''')
    tot = [0, 0]
    for o in range(2, 121):
        if o in (64, 96):
            continue
        r = fun(o).sage()
        tot = [x + y for x, y in zip(tot, r)]
    check(tot[0] == tot[1] and tot[0] > 500,
          'th:schur, proof: for all %d (G-bar, H, p), |G-bar| <= 120 (64, 96 skipped), H a normal Hall '
          'subgroup: the Sylow p-subgroups of G-bar are those of H (not of G = G-bar / H, which has none), '
          '|G-bar : N| = |H : H cap N| and |N : H cap N| = |G-bar : H|' % tot[0])
    # exc:abelian-extensions-ext
    for (T, m) in [(small(4, 2), 2), (cyclic(4), 2), (small(8, 2), 2), (small(9, 2), 3), (small(8, 5), 2)]:
        A = trivial(T, m)
        reps = h2_reps(A)
        # coboundaries of an abelian G with trivial A are symmetric, so a class contains a
        # symmetric cocycle iff each of its cocycles is symmetric
        bas = [{g: A.elts[(g * 7 + s) % len(A.elts)] for g in range(T.n)} for s in range(5)]
        check(all(all(d[(a, b)] == d[(b, a)] for a in range(T.n) for b in range(T.n))
                  for d in [coboundary_cocycle(A, phi) for phi in bas]),
              'exc:abelian-extensions-ext: coboundaries are symmetric (%s, Z_%d)' % (T.name, m))
        abel = []
        for h in reps:
            E = Ext(A, h)
            sym = all(h[(a, b)] == h[(b, a)] for a in range(T.n) for b in range(T.n))
            isab = bool(E.P.IsAbelian())
            check(isab == sym, 'exc:abelian-extensions-ext: G-bar abelian <=> h(g1, g2) = h(g2, g1) (%s, Z_%d)'
                  % (T.name, m))
            abel.append(isab)
        nab = sum(abel)
        check(len(reps) % nab == 0, 'exc:abelian-extensions-ext: the %d abelian classes form a subgroup of '
              'H^2 (%d classes) (%s, Z_%d)' % (nab, len(reps), T.name, m))
        closed = True
        abreps = [h for h, a in zip(reps, abel) if a]
        for h1 in abreps:
            for h2 in abreps:
                hs = {q: A.add(h1[q], h2[q]) for q in h1}
                closed = closed and bool(Ext(A, hs).P.IsAbelian())
        check(closed, 'exc:abelian-extensions-ext: sums of abelian classes are abelian (%s, Z_%d)' % (T.name, m))
    # exc:h2-free-abelian-rank-two: G_1 = <x, y | [x, [x, y]], [y, [x, y]]>
    # (z = [x, y] eliminated).  As c = [x, y] is central and x y = y x c,
    # every element of G_1 is y^b x^a c^k; X, Y below satisfy the relators
    # in UT_3(Z) and the images of these normal forms are distinct, so
    # G_1 = UT_3(Z): nilpotent of class 2, Hirsch length 3.
    X = matrix(ZZ, [[1, 1, 0], [0, 1, 0], [0, 0, 1]])
    Y = matrix(ZZ, [[1, 0, 0], [0, 1, 1], [0, 0, 1]])
    C = X.inverse() * Y.inverse() * X * Y
    one = identity_matrix(ZZ, 3)
    check(C != one and C * X == X * C and C * Y == Y * C,
          'exc:h2-free-abelian-rank-two: the relators of G_1 hold in UT_3(Z), '
          '[x, y] != 1')
    images = {tuple((Y ** b * X ** a * C ** k).list())
              for a in range(-3, 4) for b in range(-3, 4) for k in range(-3, 4)}
    check(len(images) == 7 ** 3,
          'exc:h2-free-abelian-rank-two: normal forms y^b x^a c^k of G_1 have '
          'distinct images in UT_3(Z) (|a|, |b|, |k| <= 3)')
    check(all((X ** a * Y ** b * C ** k) * (X ** a2 * Y ** b2 * C ** k2)
              == (X ** a2 * Y ** b2 * C ** k2) * (X ** a * Y ** b * C ** k)
              * C ** (a * b2 - a2 * b)
              for a, b, k, a2, b2, k2 in [(1, 0, 0, 0, 1, 0), (2, 1, 0, 1, 3, 2),
                                          (-1, 2, 1, 3, -2, 0)]),
          'exc:h2-free-abelian-rank-two: class 2, commutators central')
    # exc:commutator-form: h(g1, g2) - h(g2, g1) = [g1-bar, g2-bar]; bilinear, alternating
    for (T, m) in [(small(4, 2), 2), (cyclic(4), 2), (small(8, 2), 2), (small(9, 2), 3), (small(8, 5), 2)]:
        A = trivial(T, m)
        cocs, dim = normalised_cocycles(A, limit=64)
        ok = True
        for h in cocs:
            E = Ext(A, h)
            for a in range(T.n):
                for b in range(T.n):
                    xa, xb = (a, A.zero), (b, A.zero)
                    ia, ib = E.inverse(xa), E.inverse(xb)
                    com = E.mul(E.mul(ia, ib), E.mul(xa, xb))
                    hm = A.sub(h[(a, b)], h[(b, a)])
                    ok = ok and com == (T.e, hm)
            hm = {(a, b): A.sub(h[(a, b)], h[(b, a)]) for a in range(T.n) for b in range(T.n)}
            bil = all(hm[(T.mul[a][b], c)] == A.add(hm[(a, c)], hm[(b, c)])
                      for a in range(T.n) for b in range(T.n) for c in range(T.n))
            ok = ok and bil and all(hm[(a, a)] == A.zero for a in range(T.n))
        check(ok, 'exc:commutator-form: [g1-bar, g2-bar] = h(g1, g2) - h(g2, g1), bilinear and '
              'alternating, %d cocycles (%s, Z_%d)' % (len(cocs), T.name, m))
    # exc:h2-free-abelian-lambda (cubical torus T^n = K(Z^n, 1)) and the
    # "skew-symmetric" reading
    circle = cubical_complexes.Sphere(1)
    torus = circle
    for n in range(1, 5):
        if n > 1:
            torus = torus.product(circle)
        dimH = torus.cohomology(2, base_ring=GF(2)).dimension()
        alt = binomial(n, 2)
        skew = binomial(n, 2) + n          # f(x, y) = -f(y, x) leaves f(x_i, x_i) in Z_2 free
        check(dimH == alt, 'exc:h2-free-abelian-lambda: dim H^2(Z^%d, F_2) = %d = dim Alt(Z^%d, F_2) (torus)'
              % (n, dimH, n))
        refuted(dimH == skew, 'exc:h2-free-abelian-lambda read with f(x, y) = -f(y, x): '
                'dim H^2(Z^%d, F_2) = %d would be %d' % (n, dimH, skew))
        Hz = torus.cohomology(2, base_ring=ZZ)
        check(Hz.invariants() == (0,) * alt,
              'exc:h2-free-abelian-lambda: H^2(Z^%d, Z) = Z^%d (torus)' % (n, alt))
    # enumerate forms on Z^n with values in Z_2: alternating vs skew-symmetric (bilinear forms <-> matrices)
    for n in range(1, 4):
        nalt = nskew = 0
        for M in itertools.product(range(2), repeat=n * n):
            C = [M[i * n:(i + 1) * n] for i in range(n)]
            sk = all((C[i][j] + C[j][i]) % 2 == 0 for i in range(n) for j in range(n))
            al = sk and all(C[i][i] == 0 for i in range(n))
            nskew += sk
            nalt += al
        check(nalt == 2 ** binomial(n, 2) and nskew == 2 ** (binomial(n, 2) + n),
              'exc:h2-free-abelian-lambda: on Z^%d with values in Z_2 there are %d alternating and %d '
              'skew-symmetric bilinear forms' % (n, nalt, nskew))
    # the hint cocycle on Z^n and symmetric cocycles are coboundaries (polynomial identities)
    for n in [2, 3]:
        R = PolynomialRing(ZZ, ['u%d' % i for i in range(n)] + ['v%d' % i for i in range(n)] +
                           ['w%d' % i for i in range(n)] + ['c%d%d' % (i, j) for i in range(n) for j in range(n)])
        U = R.gens()[:n]
        V = R.gens()[n:2 * n]
        W = R.gens()[2 * n:3 * n]
        Cc = [[R.gen(3 * n + i * n + j) for j in range(n)] for i in range(n)]

        def hb(p, q):       # bilinear h(p, q) = sum c_ij p_i q_j
            return sum(Cc[i][j] * p[i] * q[j] for i in range(n) for j in range(n))
        add = lambda p, q: [a + b for a, b in zip(p, q)]
        coc = hb(U, V) - hb(U, add(V, W)) + hb(add(U, V), W) - hb(V, W)
        check(coc == 0, 'exc:h2-free-abelian-lambda: bilinear functions are 2-cocycles of Z^%d (trivial A)' % n)
        # hint: x_1^m_1 .. x_n^m_n -> x-bar_1^m_1 ..; [x_l, x_k] = a: h(m, m') = a m_l m'_k
        for (k, l) in [(0, 1), (0, n - 1)]:
            hint = U[l] * V[k]
            alt = hint - U[k] * 0 - (V[l] * U[k])
            check(alt.subs({U[l]: 1, V[k]: 1, U[k]: 0, V[l]: 0}) == 1,
                  'exc:h2-free-abelian-lambda, hint: h^-(x_l, x_k) = a (l > k)')
        # symmetric bilinear: h = delta phi with phi(m) = -sum_i c_ii C(m_i, 2) - sum_(i<j) c_ij m_i m_j
        sym = {Cc[j][i]: Cc[i][j] for i in range(n) for j in range(n) if i < j}

        def hs(p, q):
            return hb(p, q).subs(sym)

        def phi(p):
            return -sum(Cc[i][i] * p[i] * (p[i] - 1) / 2 for i in range(n)) - \
                sum(Cc[i][j] * p[i] * p[j] for i in range(n) for j in range(n) if i < j)
        d = phi(U) - phi(add(U, V)) + phi(V)
        check(R.fraction_field()(d) == R.fraction_field()(hs(U, V)),
              'exc:h2-free-abelian-lambda: a symmetric bilinear cocycle of Z^%d is delta phi with an '
              'integer-valued phi (binomials)' % n)
    # exc:ext-lambda-sequence: all abelian groups of order <= 16, A = Z_2, Z_3, Z_4
    nab = 0
    for o in range(2, 17):
        for i in range(1, int(gap('NumberSmallGroups(%d)' % o)) + 1):
            G = gap('SmallGroup(%d,%d)' % (o, i))
            if not bool(G.IsAbelian()):
                continue
            T = TGroup(G, 'SmallGroup(%d,%d)' % (o, i))
            inv = [int(c) for c in G.AbelianInvariants()]
            for m in [2, 3, 4]:
                A = trivial(T, m)
                zord = cochain_order(A, 2) // image_order(A, 2)
                bord = image_order(A, 1)
                h2 = zord // bord
                # symmetric cocycles: add rows h(a, b) - h(b, a)
                d, r, c = delta_dict(A, 2)
                extra = {}
                N = T.n
                rr = r
                for a in range(N):
                    for b in range(N):
                        if a < b:
                            extra[(rr, a * N + b)] = 1
                            extra[(rr, b * N + a)] = -1
                            rr += 1
                d2 = dict(d)
                d2.update(extra)
                if Integer(m).is_prime():
                    Ms = matrix(GF(m), rr, c, {kk: GF(m)(v) for kk, v in d2.items() if GF(m)(v)}, sparse=True)
                    symord = Integer(m) ** (c - Ms.rank())
                else:
                    Ms = matrix(ZZ, rr, c, {kk: v for kk, v in d2.items() if v})
                    im = prod(Integer(m) // gcd(s, m) for s in Ms.elementary_divisors() if s)
                    symord = Integer(m) ** c // im
                ext = symord // bord
                # bilinear forms on G = prod Z_(n_i): values c_ij in Z_m with n_i c_ij = n_j c_ij = 0
                k = len(inv)
                nalt = nskew = 0
                choices = []
                for a in range(k):
                    for b in range(k):
                        choices.append([v for v in range(m) if (inv[a] * v) % m == 0 and (inv[b] * v) % m == 0])
                for vals in itertools.product(*choices):
                    C = [vals[a * k:(a + 1) * k] for a in range(k)]
                    sk = all((C[a][b] + C[b][a]) % m == 0 for a in range(k) for b in range(k))
                    al = sk and all(C[a][a] == 0 for a in range(k))
                    nskew += sk
                    nalt += al
                check(h2 == ext * nalt and zord // symord == nalt,
                      'exc:ext-lambda-sequence: |H^2| = %d = |Ext| %d * |Alt| %d, image of alpha = Alt '
                      '(G = %s, A = Z_%d)' % (h2, ext, nalt, inv, m))
                check(ext == prod(gcd(n_, m) for n_ in inv),
                      'exc:ext-lambda-sequence: Ext(G, Z_%d) = classes of symmetric cocycles, order %d (G = %s)'
                      % (m, ext, inv))
                if nskew != nalt:
                    refuted(h2 == ext * nskew,
                            'exc:ext-lambda-sequence read with f(x, y) = -f(y, x): |H^2| = %d would be '
                            '|Ext| %d * |Skew| %d (G = %s, A = Z_%d)' % (h2, ext, nskew, inv, m))
            nab += 1
    check(nab == int(gap('Sum([2..16], o -> Number([1..NumberSmallGroups(o)], i -> IsAbelian(SmallGroup(o, i))))')),
          'exc:ext-lambda-sequence: all %d abelian groups of order 2..16' % nab)
    # the counterexample of the proposed note: G = Z_2 (finite) and G = Z (torus above), A = Z_2
    T = cyclic(2)
    A = trivial(T, 2)
    check(h_order(A, 2) == 2 and all(bool(Ext(A, h).P.IsAbelian()) for h in h2_reps(A)),
          'note: H^2(Z_2, Z_2) = Z_2 = Ext(Z_2, Z_2) (both extensions abelian), Alt(Z_2, Z_2) = 0, '
          'while f(x, y) = x y is skew-symmetric and non-zero')
    # ch. 5 family: Z^n (x) Z^n / <x (x) y + y (x) x> vs Lambda^2 Z^n
    for n in range(1, 5):
        rels = []
        for i in range(n):
            for j in range(n):
                v = [0] * (n * n)
                v[i * n + j] += 1
                v[j * n + i] += 1
                rels.append(v)
        Ms = matrix(ZZ, rels)
        ed = Ms.elementary_divisors()
        free = n * n - Ms.rank()
        two = len([d for d in ed if d == 2])
        rels_alt = [r for r in rels] + [[1 if q == i * n + i else 0 for q in range(n * n)] for i in range(n)]
        Ma = matrix(ZZ, rels_alt)
        free_a = n * n - Ma.rank()
        tors_a = [d for d in Ma.elementary_divisors() if d not in (0, 1)]
        check(free == binomial(n, 2) and two == n and free_a == binomial(n, 2) and not tors_a,
              'note (ch. 5 family): Z^%d (x) Z^%d modulo x (x) y + y (x) x is Z^%d + Z_2^%d, modulo the '
              'alternating relations it is Lambda^2 Z^%d = Z^%d' % (n, n, free, two, n, free_a))
    # exc:automorphism-factor-system and exc:inner-automorphism-coboundary
    for (T, A, h, lab) in pick(ext_examples(), 2):
        E = Ext(A, h)
        Agens = [E.p((T.e, b)) for b in A.basis()]
        Nn = libgap.Group(Agens) if Agens else None
        auts = list(gap('AutomorphismGroup')(E.P).AsList())
        if len(auts) > 400:
            auts = auts[:400]
        cnt = 0
        for f in auts:
            if not bool(f.Image(Nn) == Nn):
                continue
            img = {x: perm_to_el(E, f.Image(E.p(x))) for x in E.el}
            fG = {g: img[(g, A.zero)][0] for g in range(T.n)}       # induced on G
            fGi = {v: k for k, v in fG.items()}
            fA = lambda a: img[(T.e, a)][1]
            # transversal g -> f(f^-1(g)-bar)
            trans = {g: img[(fGi[g], A.zero)] for g in range(T.n)}
            fh = {(a, b): fA(h[(fGi[a], fGi[b])]) for a in range(T.n) for b in range(T.n)}
            ok = True
            for a in range(T.n):
                for b in range(T.n):
                    lhs = E.mul(trans[a], trans[b])
                    rhs = E.mul(trans[T.mul[a][b]], (T.e, fh[(a, b)]))
                    ok = ok and lhs == rhs
            diff = {q: A.sub(fh[q], h[q]) for q in h}
            ok = ok and (in_b2(A, diff) if Integer(A.m).is_prime() else in_b2_brute(A, diff))
            check(ok, 'exc:automorphism-factor-system: f^* h is the factor system of g -> f(f^-1(g)-bar) and '
                  'is cohomologous to h (%s)' % lab)
            cnt += 1
        check(cnt > 0, 'exc:automorphism-factor-system: %d automorphisms with f(A) = A (%s)' % (cnt, lab))
        # inner automorphisms alpha_x(y) = x^-1 y x, x = (x0, c) in G-bar
        ok = True
        for x0 in range(T.n):
            for cA in A.elts[:3]:
                xx = (x0, cA)
                xi = E.inverse(xx)
                alpha = lambda y: E.mul(E.mul(xi, y), xx)
                aG = {g: alpha((g, A.zero))[0] for g in range(T.n)}
                aGi = {v: k for k, v in aG.items()}
                aA = lambda a: alpha((T.e, a))[1]
                ah = {(a, b): aA(h[(aGi[a], aGi[b])]) for a in range(T.n) for b in range(T.n)}
                phi = {g: A.sub(h[(T.mul[T.mul[x0][g]][T.inv[x0]], x0)], h[(x0, g)]) for g in range(T.n)}
                d = coboundary_cocycle(A, phi)
                ok = ok and all(ah[q] == A.add(h[q], d[q]) for q in h)
        check(ok, 'exc:inner-automorphism-coboundary: alpha_x^* h = h + delta phi with phi(g) = '
              'h(x g x^-1, x) - h(x, g), alpha_x(y) = x^-1 y x, all x in G-bar (%s)' % lab)


def sum_phi(A, phi, r):
    out = A.zero
    for g, c in enumerate(r):
        if c:
            out = A.add(out, A.smul(c, phi[g]))
    return out


# ---------------------------------------------------------------------------
# Free groups and Fox derivatives
# ---------------------------------------------------------------------------

def freduce(w):
    out = []
    for l in w:
        if out and out[-1] == -l:
            out.pop()
        else:
            out.append(l)
    return tuple(out)


def winv(w):
    return tuple(-l for l in reversed(w))


def wmul(u, v):
    return freduce(tuple(u) + tuple(v))


def zf_add(a, b, c=1):
    out = dict(a)
    for w, x in b.items():
        out[w] = out.get(w, 0) + c * x
        if out[w] == 0:
            del out[w]
    return out


def zf_mul(a, b):
    out = {}
    for u, x in a.items():
        for v, y in b.items():
            w = wmul(u, v)
            out[w] = out.get(w, 0) + x * y
            if out[w] == 0:
                del out[w]
    return out


def fox(w, i):
    """Right Fox derivative d w / d x_i: sum over the letters of w."""
    out = {}
    for k, l in enumerate(w):
        if l == i:
            out = zf_add(out, {w[k + 1:]: 1})
        elif l == -i:
            out = zf_add(out, {w[k:]: -1})
    return out


def fox_semidirect(w, n):
    """Fox derivatives from the definition: v(x_1 e_1, ..., x_n e_n) in F P."""
    def gen(l):
        i = abs(l)
        p = [dict() for _ in range(n)]
        if l > 0:
            p[i - 1] = {(): 1}
            return ((l,), p)
        # (x e)^(-1) = (x^-1, -e x^-1)
        p[i - 1] = {(l,): -1}
        return ((l,), p)

    def mul(x, y):
        (w1, p1), (w2, p2) = x, y
        return (wmul(w1, w2), [zf_add(zf_mul(a, {w2: 1}), b) for a, b in zip(p1, p2)])
    cur = ((), [dict() for _ in range(n)])
    for l in w:
        cur = mul(cur, gen(l))
    assert cur[0] == freduce(w)
    return cur[1]


def rand_word(n, length):
    return freduce(tuple(random.choice([1, -1]) * random.randint(1, n) for _ in range(length)))


def subst(w, ws):
    out = ()
    for l in w:
        out = wmul(out, ws[l - 1] if l > 0 else winv(ws[-l - 1]))
    return out


def zf_subst(a, ws):
    out = {}
    for w, c in a.items():
        out = zf_add(out, {subst(w, ws): c})
    return out


def comm(u, v):
    return freduce(winv(u) + winv(v) + tuple(u) + tuple(v))


def weval(T, w, vals):
    r = T.e
    for l in w:
        r = T.mul[r][vals[l - 1] if l > 0 else T.inv[vals[-l - 1]]]
    return r


def zf_eval(T, a, vals):
    out = [0] * T.n
    for w, c in a.items():
        out[weval(T, w, vals)] += c
    return out


def lattice(vecs, n):
    vecs = [v for v in vecs if any(v)]
    if not vecs:
        return matrix(ZZ, 0, n)
    H = matrix(ZZ, vecs).echelon_form()
    return H.matrix_from_rows([i for i in range(H.nrows()) if not H.row(i).is_zero()])


def right_ideal(T, gens):
    return lattice([zg_mul(T, r, zg_unit(T, g)) for r in gens for g in range(T.n)], T.n)


def fox_ideal(T, v, nvar):
    """d V(G): the right ideal generated by all values of d v / d x_i."""
    ders = [fox(v, i) for i in range(1, nvar + 1)]
    vals = set()
    for tup in itertools.product(range(T.n), repeat=nvar):
        for d in ders:
            vals.add(tuple(zf_eval(T, d, tup)))
    return right_ideal(T, [list(x) for x in vals])


def aug_ideal_sub(T, Hs):
    """Delta_H: right ideal of ZG generated by h - 1, h in H."""
    return right_ideal(T, [zg_add(zg_unit(T, h), zg_unit(T, T.e), -1) for h in Hs])


def ideal_product(T, L1, L2):
    """the additive span of products x y (x in L1, y in L2) -- a right ideal if L2 is one."""
    return lattice([zg_mul(T, list(a), list(b)) for a in L1.rows() for b in L2.rows()], T.n)


def ideal_sum(L1, L2, n):
    return lattice(list(L1.rows()) + list(L2.rows()), n)


# ---------------------------------------------------------------------------
# section 9
# ---------------------------------------------------------------------------

ROLFSEN = [
    ("3_1", [1, -1]), ("4_1", [3, -1]), ("5_1", [1, -1, 1]), ("5_2", [3, -2]), ("6_1", [5, -2]),
    ("6_2", [3, -3, 1]), ("6_3", [5, -3, 1]), ("7_1", [1, -1, 1, -1]), ("7_2", [5, -3]),
    ("7_3", [3, -3, 2]), ("7_4", [7, -4]), ("7_5", [5, -4, 2]), ("7_6", [7, -5, 1]),
    ("7_7", [9, -5, 1]), ("8_1", [7, -3]), ("8_2", [3, -3, 3, -1]), ("8_3", [9, -4]),
    ("8_4", [5, -5, 2]), ("8_5", [5, -4, 3, -1]), ("8_6", [7, -6, 2]), ("8_7", [5, -5, 3, -1]),
    ("8_8", [9, -6, 2]), ("8_9", [7, -5, 3, -1]), ("8_10", [7, -6, 3, -1]), ("8_11", [9, -7, 2]),
    ("8_12", [13, -7, 1]), ("8_13", [11, -7, 2]), ("8_14", [11, -8, 2]), ("8_15", [11, -8, 3]),
    ("8_16", [9, -8, 4, -1]), ("8_17", [11, -8, 4, -1]), ("8_18", [13, -10, 5, -1]),
    ("8_19", [1, 0, -1, 1]), ("8_20", [3, -2, 1]), ("8_21", [5, -4, 1]), ("9_1", [1, -1, 1, -1, 1]),
    ("9_2", [7, -4]), ("9_3", [3, -3, 3, -2]), ("9_4", [5, -5, 3]), ("9_5", [11, -6]),
    ("9_6", [5, -5, 4, -2]), ("9_7", [9, -7, 3]), ("9_8", [11, -8, 2]), ("9_9", [7, -6, 4, -2]),
    ("9_10", [9, -8, 4]), ("9_11", [7, -7, 5, -1]), ("9_12", [13, -9, 2]), ("9_13", [11, -9, 4]),
    ("9_14", [15, -9, 2]), ("9_15", [15, -10, 2]), ("9_16", [9, -8, 5, -2]), ("9_17", [9, -9, 5, -1]),
    ("9_18", [13, -10, 4]), ("9_19", [17, -10, 2]), ("9_20", [11, -9, 5, -1]), ("9_21", [17, -11, 2]),
    ("9_22", [11, -10, 5, -1]), ("9_23", [15, -11, 4]), ("9_24", [13, -10, 5, -1]),
    ("9_25", [17, -12, 3]), ("9_26", [13, -11, 5, -1]), ("9_27", [15, -11, 5, -1]),
    ("9_28", [15, -12, 5, -1]), ("9_29", [15, -12, 5, -1]), ("9_30", [17, -12, 5, -1]),
    ("9_31", [17, -13, 5, -1]), ("9_32", [17, -14, 6, -1]), ("9_33", [19, -14, 6, -1]),
    ("9_34", [23, -16, 6, -1]), ("9_35", [13, -7]), ("9_36", [9, -8, 5, -1]), ("9_37", [19, -11, 2]),
    ("9_38", [19, -14, 5]), ("9_39", [21, -14, 3]), ("9_40", [23, -18, 7, -1]), ("9_41", [19, -12, 3]),
    ("9_42", [1, -2, 1]), ("9_43", [1, -2, 3, -1]), ("9_44", [7, -4, 1]), ("9_45", [9, -6, 1]),
    ("9_46", [5, -2]), ("9_47", [5, -6, 4, -1]), ("9_48", [11, -7, 1]), ("9_49", [7, -6, 3]),
]
"""D. Rolfsen, Knots and Links (Publish or Perish, 1976; reprint 2003),
Appendix C, pp. 391-399: Alexander polynomials of the prime knots 3_1-9_49 in
Rolfsen's abbreviation [a + b + c ...] = a + b (x + 1/x) + c (x^2 + 1/x^2) + ..."""


def alexander_from_presentation(rels, n):
    """Generator of the ideal of (n - 1)-minors of the Alexander matrix, all
    generators mapped to t (knot groups); normalised (t-power, sign)."""
    L = LaurentPolynomialRing(ZZ, 't')
    t = L.gen()

    def ev(a):
        return sum((c * t ** sum(1 if l > 0 else -1 for l in w) for w, c in a.items()), L(0))
    M = matrix(L, [[ev(fox(r, j)) for j in range(1, n + 1)] for r in rels])
    return M


def normalise_poly(a):
    R = PolynomialRing(ZZ, 't')
    if a == 0:
        return R(0)
    e = min(a.exponents())
    p = R({k - e: c for k, c in zip(a.exponents(), a.coefficients())})
    if p.leading_coefficient() < 0:
        p = -p
    return p


def section_9():
    # (1.21), (1.22) in semidirect products
    for (T, A) in [mod_s3_f2(), mod_z4_on_z5()]:
        E = Ext(A, zero_cocycle(A))
        ok = True
        for g in range(T.n):
            for a in A.elts:
                for n in range(1, 6):
                    x = (g, a)
                    pw = (T.e, A.zero)
                    for _ in range(n):
                        pw = E.mul(pw, x)
                    r = [0] * T.n
                    for k in range(n):
                        r[T.power(g, k)] += 1
                    ok = ok and pw == (T.power(g, n), A.actr(a, r))
        check(ok, 'eq:power-semidirect: (g a)^n = g^n a^(g^(n-1) + ... + 1) (corrected g -> g^n), n <= 5 (%s)' % A.name)
        def printed_cube(g, a):
            r = [0] * T.n
            for k in range(3):
                r[T.power(g, k)] += 1
            return (g, A.actr(a, r))
        refuted(all(E.mul(E.mul((g, a), (g, a)), (g, a)) == printed_cube(g, a)
                    for g in range(T.n) for a in A.elts),
                'eq:power-semidirect printed: (g a)^3 = g a^(g^2 + g + 1) (g instead of g^n), %s' % A.name)
        ok = True
        for g1 in range(T.n):
            for g2 in range(T.n):
                for a1 in A.elts[:5]:
                    for a2 in A.elts[:5]:
                        x, y = (g1, a1), (g2, a2)
                        com = E.mul(E.mul(E.inverse(x), E.inverse(y)), E.mul(x, y))
                        c12 = T.mul[T.mul[T.inv[g1]][T.inv[g2]]][T.mul[g1][g2]]
                        e1 = zg_add(zg_unit(T, g2), zg_unit(T, c12), -1)
                        e2 = zg_add(zg_unit(T, T.e), zg_unit(T, T.mul[T.mul[T.inv[g2]][g1]][g2]), -1)
                        ok = ok and com == (c12, A.add(A.actr(a1, e1), A.actr(a2, e2)))
        check(ok, 'eq:commutator-semidirect: [g1 a1, g2 a2] = [g1, g2] a1^(g2 - [g1, g2]) a2^(1 - g2^-1 g1 g2) (%s)' % A.name)
    # (1.23)-(1.26), (1.24) corrected
    for n in range(1, 7):
        check(fox((1,) * n, 1) == {(1,) * k: 1 for k in range(n)}, 'eq:fox-power: d x^%d / d x = x^%d + ... + 1' % (n, n - 1))
    c = comm((1,), (2,))
    check(fox(c, 1) == zf_add({(2,): 1}, {c: -1}), 'eq:fox-commutator: d[x1, x2]/dx1 = x2 - [x1, x2]')
    check(fox(c, 2) == zf_add({(): 1}, {(-2, 1, 2): -1}),
          'eq:fox-commutator: d[x1, x2]/dx2 = 1 - x2^-1 x1 x2 (corrected from x^2)')
    refuted(fox(c, 2) == zf_add({(): 1}, {(-2, 1, 2, 2): -1}),
            'eq:fox-commutator printed: 1 - x2^-1 x1 x2^2')
    check(fox((1,), 1) == {(): 1} and fox((2,), 1) == {} and fox((-1,), 1) == {(-1,): -1} and fox((-2,), 1) == {},
          'eq:fox-generators, eq:fox-inverses')
    # two computations agree; derivation property; Fox identity
    ok = ok2 = ok3 = True
    for _ in range(300):
        n = random.randint(1, 3)
        v = rand_word(n, random.randint(0, 12))
        w = rand_word(n, random.randint(0, 12))
        sd = fox_semidirect(v, n)
        ok = ok and all(sd[i - 1] == fox(v, i) for i in range(1, n + 1))
        for i in range(1, n + 1):
            ok2 = ok2 and fox(wmul(v, w), i) == zf_add(zf_mul(fox(v, i), {w: 1}), fox(w, i))
        rhs = {}
        for i in range(1, n + 1):
            rhs = zf_add(rhs, zf_mul(zf_add({(i,): 1}, {(): -1}), fox(v, i)))
        ok3 = ok3 and rhs == zf_add({v: 1}, {(): -1})
    check(ok, 'p. 50: the explicit derivatives agree with the definition through F P (300 random words)')
    check(ok2, 'eq:fox-derivation: d(v w) = (dv) w + dw (300 random pairs)')
    check(ok3, 'eq:fox-identity: v - 1 = sum (x_i - 1) dv/dx_i (300 random words)')
    # (1.27) and (1.30) in semidirect products
    for (T, A) in [mod_s3_f2(), mod_z4_on_z5()]:
        E = Ext(A, zero_cocycle(A))
        ok = ok2 = True
        for _ in range(60):
            n = random.randint(1, 3)
            v = rand_word(n, random.randint(1, 10))
            gs = [random.randrange(T.n) for _ in range(n)]
            as_ = [random.choice(A.elts) for _ in range(n)]
            elts = [(g, a) for g, a in zip(gs, as_)]
            val = (T.e, A.zero)
            for l in v:
                val = E.mul(val, elts[l - 1] if l > 0 else E.inverse(elts[-l - 1]))
            rhs = A.zero
            for i in range(n):
                rhs = A.add(rhs, A.actr(as_[i], zf_eval(T, fox(v, i + 1), gs)))
            ok = ok and val == (weval(T, v, gs), rhs)
            lhs = zg_add(zg_unit(T, weval(T, v, gs)), zg_unit(T, T.e), -1)
            r = [0] * T.n
            for i in range(n):
                r = zg_add(r, zg_mul(T, zg_add(zg_unit(T, gs[i]), zg_unit(T, T.e), -1), zf_eval(T, fox(v, i + 1), gs)))
            ok2 = ok2 and lhs == r
        check(ok, 'eq:word-values-semidirect: v(g_i a_i) = v(g_i) prod a_i^(dv/dg_i) (60 random words, %s)' % A.name)
        check(ok2, 'eq:fox-identity-values: v(g) - 1 = sum (g_i - 1) dv/dg_i (%s)' % A.name)
    # prop:word-values-extension, normalised transversal
    for (T, A, h, lab) in ext_examples():
        E = Ext(A, h)
        ok = True
        for _ in range(25):
            n = random.randint(1, 3)
            v = rand_word(n, random.randint(1, 8))
            gs = [random.randrange(T.n) for _ in range(n)]
            as_ = [random.choice(A.elts) for _ in range(n)]
            elts = [(g, a) for g, a in zip(gs, as_)]
            val = (T.e, A.zero)
            for l in v:
                val = E.mul(val, elts[l - 1] if l > 0 else E.inverse(elts[-l - 1]))
            rhs = A.zero
            for i in range(n):
                dv = zf_eval(T, fox(v, i + 1), gs)
                rhs = A.add(rhs, A.add(A.actr(as_[i], dv), hsum(A, h, gs[i], dv)))
            ok = ok and val == (weval(T, v, gs), rhs)
        check(ok, 'prop:word-values-extension with 1-bar = 1: v(g_i-bar a_i) = v(g)-bar sum (a_i dv/dg_i + '
              'h(g_i, dv/dg_i)) (25 random words, %s)' % lab)
    T = cyclic(2)
    A = trivial(T, 2)
    h = {(a, b): (1,) for a in range(2) for b in range(2)}       # cocycle with h(1, 1) != 0
    assert cocycle_ok(A, h)
    E = Ext(A, h)
    # transversal g -> (g, 0) with 1-bar = (1, 0) != 1 = (1, 1); A embedded by a -> (1, a + 1)
    g0 = T.gens[0]
    emb = lambda a: (T.e, A.sub(a, h[(T.e, T.e)]))
    ok_all = True
    for a in A.elts:
        lhs = E.mul((g0, A.zero), emb(a))                      # v(g-bar a) for v = x
        dv = zf_eval(T, fox((1,), 1), [g0])                    # = 1
        rhs = E.mul((g0, A.zero), emb(A.add(A.actr(a, dv), hsum(A, h, g0, dv))))
        ok_all = ok_all and lhs == rhs
    refuted(ok_all, 'prop:word-values-extension without 1-bar = 1: for v = x the right-hand side has the '
            'extra factor h(g, 1) = 1-bar != 0 (G = A = Z_2, h = 1)')
    # exm:nilpotent-semidirect: gamma_(n+1)(G A) = gamma_(n+1)(G) (A Delta^n)
    cases = [(cyclic(2), trivial(cyclic(2), 2))]
    for (o, i, sub) in [(4, 1, 1), (4, 2, 1), (8, 3, 2), (8, 4, 2), (8, 2, 2)]:
        T = small(o, i)
        H = [x for x in gap('function(G, k) return First(AllSubgroups(G), S -> Size(S) = k); end')(T.G, sub).AsSSortedList()]
        cases.append((T, perm_module(T, [T.index(x) for x in H], 2)))
    cases.append((cyclic(3), Mod(cyclic(3), 3, 1, lambda g: [[1]], 'trivial Z_3')))
    for (T, A) in cases:
        E = Ext(A, zero_cocycle(A))
        lcs = list(E.P.LowerCentralSeriesOfGroup())
        lcsG = list(T.G.LowerCentralSeriesOfGroup())
        ADn = set(A.elts)
        for n in range(1, 6):
            ADn = closure_add(A, [A.actr(a, zg_add(zg_unit(T, g), zg_unit(T, T.e), -1)) for a in ADn for g in range(T.n)])
            gam = lcs[min(n, len(lcs) - 1)]
            gG = lcsG[min(n, len(lcsG) - 1)]
            gGi = [T.index(x) for x in gG.AsSSortedList()]
            pred = libgap.Group([E.p((g, A.zero)) for g in gGi] + [E.p((T.e, a)) for a in ADn] + [E.p((T.e, A.zero))])
            check(bool(pred == gam), 'exm:nilpotent-semidirect: gamma_%d(G A) = gamma_%d(G) (A Delta^%d) (%s, %s)'
                  % (n + 1, n + 1, n, T.name, A.name))
    # d c_(n+1)(G) = Delta^n, d c^((2))(G) = Delta_G Delta_(G')
    for (o, i) in [(4, 1), (6, 1), (8, 3), (8, 4), (12, 3)]:
        T = small(o, i)
        D1 = aug_ideal_sub(T, list(range(T.n)))
        Dn = D1
        c = (1,)
        for n in range(1, 4 if T.n <= 8 else 3):
            c = comm(c, (n + 1,))
            if n > 1:
                Dn = ideal_product(T, Dn, D1)
            check(fox_ideal(T, c, n + 1) == Dn, 'p. 53: d c_%d(G) = Delta_G^%d (%s)' % (n + 1, n, T.name))
        Gd = [T.index(x) for x in T.G.DerivedSubgroup().AsSSortedList()]
        c2 = comm(comm((1,), (2,)), comm((3,), (4,)))
        pred = ideal_product(T, D1, aug_ideal_sub(T, Gd))
        check(fox_ideal(T, c2, 4) == pred, 'p. 53: d c^((2))(G) = Delta_G Delta_(G\') (%s)' % T.name)
        # exc:fox-product-rule with V = {[x1, x2]}, W = {x3}: d[V, W] = dV Delta_W(G) + dW Delta_V(G)
        pr = ideal_sum(ideal_product(T, D1, D1), aug_ideal_sub(T, Gd), T.n)
        check(fox_ideal(T, comm(comm((1,), (2,)), (3,)), 3) == pr,
              'exc:fox-product-rule: d[[x1, x2], x3](G) = Delta_G Delta_G + ZG Delta_(G\') (%s)' % T.name)
        # exc:fox-commutator-with-variable: V = {x^2} (dV invariant under the involution)
        Vi = fox_ideal(T, (1, 1), 1)
        check(fox_ideal(T, comm((1, 1), (2,)), 2) == ideal_product(T, Vi, D1),
              'exc:fox-commutator-with-variable: d[x^2, x](G) = d{x^2}(G) Delta_G (%s)' % T.name)
    # exc:centrally-metabelian-semidirect (metabelian G only: G'' = 1)
    for (o, i) in [(6, 1), (8, 3), (8, 4)]:
        T = small(o, i)
        D1 = aug_ideal_sub(T, list(range(T.n)))
        Gd = [T.index(x) for x in T.G.DerivedSubgroup().AsSSortedList()]
        w = comm(comm(comm((1,), (2,)), comm((3,), (4,))), (5,))
        pred = ideal_product(T, ideal_product(T, D1, aug_ideal_sub(T, Gd)), D1)
        check(fox_ideal(T, w, 5) == pred, 'exc:centrally-metabelian-semidirect: d[[[x1,x2],[x3,x4]],x5](G) = '
              'Delta_G Delta_(G\') Delta_G (G\'\' = 1, %s)' % T.name)
    # prop:verbal-semidirect: V(G A) = V(G) (A dV(G))
    for (T, A) in [mod_s3_f2(), mod_z4_on_z5(), (small(8, 3), trivial(small(8, 3), 2))]:
        E = Ext(A, zero_cocycle(A))
        for (v, nv) in [((1, 1), 1), (comm((1,), (2,)), 2), ((1, 1, 1, 1), 1)]:
            vals = set()
            for tup in itertools.product(E.el, repeat=nv):
                val = (T.e, A.zero)
                for l in v:
                    val = E.mul(val, tup[l - 1] if l > 0 else E.inverse(tup[-l - 1]))
                vals.add(val)
            VGA = libgap.Group([E.p(x) for x in vals])
            VG = set(weval(T, v, tup) for tup in itertools.product(range(T.n), repeat=nv))
            dV = set()
            for tup in itertools.product(range(T.n), repeat=nv):
                for i in range(1, nv + 1):
                    dV.add(tuple(zf_eval(T, fox(v, i), tup)))
            AdV = closure_add(A, [A.actr(a, zg_mul(T, list(r), zg_unit(T, g))) for a in A.elts for r in dV for g in range(T.n)])
            pred = libgap.Group([E.p((g, A.zero)) for g in VG] + [E.p((T.e, a)) for a in AdV])
            check(bool(pred == VGA), 'prop:verbal-semidirect: V(G A) = V(G) (A dV(G)), v = %s (%s)' % (v, A.name))
    # prop:identities-in-extension, exhaustive over the normalised cocycles
    words = [((1, 1), 1), ((1, 1, 1, 1), 1), ((1, 1, 1), 1), (comm((1,), (2,)), 2), (comm(comm((1,), (2,)), (3,)), 3),
             (wmul((1, 1), (2, 2)), 2)]
    pairs = [(cyclic(2), trivial(cyclic(2), 2)), (cyclic(2), inversion(cyclic(2), 4)),
             (small(4, 2), trivial(small(4, 2), 2)), (cyclic(4), trivial(cyclic(4), 2)),
             (cyclic(3), trivial(cyclic(3), 3)), (cyclic(2), trivial(cyclic(2), 4))]
    for (T, A) in pairs:
        if Integer(A.m).is_prime():
            cocs, dim = normalised_cocycles(A, limit=64)
        else:
            cocs = all_normalised_bruteforce(A)
        for (v, nv) in words:
            if T.n ** nv * len(A.elts) ** nv > 40000:
                continue
            agree = True
            for h in cocs:
                E = Ext(A, h)
                ident = True
                for tup in itertools.product(E.el, repeat=nv):
                    val = (T.e, A.zero)
                    for l in v:
                        val = E.mul(val, tup[l - 1] if l > 0 else E.inverse(tup[-l - 1]))
                    if val != (T.e, A.zero):
                        ident = False
                        break
                c1 = all(weval(T, v, tup) == T.e for tup in itertools.product(range(T.n), repeat=nv))
                c2 = all(A.actr(a, zf_eval(T, fox(v, i), tup)) == A.zero for a in A.basis()
                         for tup in itertools.product(range(T.n), repeat=nv) for i in range(1, nv + 1))
                c3 = True
                for tup in itertools.product(range(T.n), repeat=nv):
                    s = A.zero
                    for i in range(1, nv + 1):
                        s = A.add(s, hsum(A, h, tup[i - 1], zf_eval(T, fox(v, i), tup)))
                    c3 = c3 and s == A.zero
                agree = agree and (ident == (c1 and c2 and c3))
            check(agree, 'prop:identities-in-extension: v = %s holds in G-bar <=> conditions 1-3, all %d '
                  'normalised cocycles (%s, %s)' % (v, len(cocs), T.name, A.name))
    # exc:derivative-values-not-defined
    T = cyclic(2)
    g = T.gens[0]
    check(weval(T, (1, 1), [g]) == T.e and zf_eval(T, fox((1, 1), 1), [g]) == [1 if q in (T.e, g) else 0 for q in range(2)],
          'exc:derivative-values-not-defined: x^2 is an identity in Z_2 but d(x^2)/dx (g) = 1 + g != 0')
    T = cyclic(3)
    check(zf_eval(T, fox(comm((1,), (2,)), 1), [T.gens[0], T.gens[0]]) != [0] * 3,
          'exc:derivative-values-not-defined: [x1, x2] is an identity in Z_3, d[x1, x2]/dx1 (g, g) = g - 1 != 0')
    # exc:fox-chain-rule
    ok = True
    bad = 0
    for _ in range(200):
        n, m = random.randint(1, 3), random.randint(1, 3)
        ws = [rand_word(n, random.randint(1, 5)) for _ in range(m)]
        v = rand_word(m, random.randint(1, 6))
        comp = subst(v, ws)
        for i in range(1, n + 1):
            lhs = fox(comp, i)
            corr, prnt = {}, {}
            for j in range(1, m + 1):
                dvj = zf_subst(fox(v, j), ws)
                dwj = fox(ws[j - 1], i)
                corr = zf_add(corr, zf_mul(dwj, dvj))
                prnt = zf_add(prnt, zf_mul(dvj, dwj))
            ok = ok and lhs == corr
            bad += lhs != prnt
    check(ok, 'exc:fox-chain-rule: dv/dx_i = sum_j (dw_j/dx_i)(dv/dw_j) on 200 random substitutions')
    refuted(bad == 0, 'exc:fox-chain-rule printed order sum_j (dv/dw_j)(dw_j/dx_i) (fails in %d cases)' % bad)
    v, w = (1, 1), (1, 2)          # v = y^2, w = x1 x2
    check(fox(subst(v, [w]), 1) == {(2, 1, 2): 1, (2,): 1},
          'exc:fox-chain-rule: v = y^2, w = x1 x2: dv/dx1 = x2 x1 x2 + x2')
    # exc:fox-commutator-powers: [x1, x2]^n and [x1^m, x2^n] by the chain rule
    for n in range(1, 5):
        c = comm((1,), (2,))
        for i in (1, 2):
            lhs = fox(c * n, i) if False else fox(freduce(c * n), i)
            rhs = zf_mul(fox(c, i), zf_subst(fox((1,) * n, 1), [c]))
            check(lhs == rhs, 'exc:fox-commutator-powers: d[x1, x2]^%d/dx%d = (d[x1,x2]/dx%d)(1 + c + ... + c^%d)'
                  % (n, i, i, n - 1))
        for m in range(1, 4):
            cm = comm((1,) * m, (2,) * n)
            for i in (1, 2):
                rhs = {}
                for j, wj in ((1, (1,) * m), (2, (2,) * n)):
                    rhs = zf_add(rhs, zf_mul(fox(wj, i), zf_subst(fox(comm((1,), (2,)), j), [(1,) * m, (2,) * n])))
                check(fox(cm, i) == rhs, 'exc:fox-commutator-powers: d[x1^%d, x2^%d]/dx%d by the chain rule' % (m, n, i))
    # exc:trefoil-figure-eight
    G1 = [freduce((-3, 1, 3, -2)), freduce((-1, 2, 1, -3))]
    G2 = [freduce((-4, 1, 4, -2)), freduce((1, 2, -1, -3)), freduce((-2, 3, 2, -4))]
    for (rels, n, expect, name) in [(G1, 3, [1, -1, 1], 'trefoil'), (G2, 4, [1, -3, 1], 'figure-eight')]:
        M = alexander_from_presentation(rels, n)
        colsum = [sum(M[r, j] for j in range(n)) for r in range(M.nrows())]
        minors = [M.delete_columns([j]).det() for j in range(n)]
        polys = [normalise_poly(mm) for mm in minors]
        R = PolynomialRing(ZZ, 't')
        check(all(cs == 0 for cs in colsum), 'p. 55: the columns of the Alexander matrix sum to 0 (%s)' % name)
        check(all(mm == minors[0] or mm == -minors[0] for mm in minors),
              'p. 55: the %d minors of order %d agree up to sign (%s)' % (n, n - 1, name))
        check(polys[0] == R(expect), 'exc:trefoil-figure-eight: Alexander polynomial of %s = %s' % (name, polys[0]))
        Fn = gap('FreeGroup(%d)' % n)
        ab = [int(c) for c in (Fn / [word_to_gap(Fn, r) for r in rels]).AbelianInvariants()]
        check(ab == [0], 'exc:trefoil-figure-eight: G_ab = Z (%s)' % name)
    # Wirtinger relations: the "+" form cannot give the figure-eight group with 4 generators
    R = PolynomialRing(ZZ, 't')
    fig8 = R([1, -3, 1])
    found_plus = []
    for ks in itertools.product(range(1, 5), repeat=3):
        rels = [freduce((-ks[i], i + 1, ks[i], -(i + 2))) for i in range(3)]
        M = alexander_from_presentation(rels, 4)
        p = normalise_poly(M.delete_columns([0]).det())
        if p == fig8:
            found_plus.append(ks)
    refuted(found_plus, 'p. 55 printed: a presentation x_(k(i))^-1 x_i x_(k(i)) = x_(i+1) (i = 1, 2, 3) of the '
            'figure-eight group (none of the 64 maps k gives x^2 - 3x + 1)')
    found_pm = []
    for ks in itertools.product(range(1, 5), repeat=3):
        for es in itertools.product([1, -1], repeat=3):
            rels = [freduce((-es[i] * ks[i], i + 1, es[i] * ks[i], -(i + 2))) for i in range(3)]
            M = alexander_from_presentation(rels, 4)
            if normalise_poly(M.delete_columns([0]).det()) == fig8:
                found_pm.append((ks, es))
    check(found_pm and any(es != (1, 1, 1) for ks, es in found_pm),
          'p. 55 corrected: with exponents +-1 the figure-eight polynomial occurs (%d presentations, e.g. %s)'
          % (len(found_pm), found_pm[0]))
    # p. 55: 84 knots, pairs with equal Alexander polynomials
    from sage.all import Knots
    from sage.knots.knot_table import small_knots_table
    keys = [k for k in sorted(small_knots_table) if 3 <= k[0] <= 9]
    check(len(keys) == 84 == len(ROLFSEN) and
          [('%d_%d' % k) for k in keys] == [nm for nm, _ in ROLFSEN],
          'p. 55: there are 84 prime knots with at most 9 crossings (1+1+2+3+7+21+49), Sage table = Rolfsen')
    polys = {}
    for (n, k), (nm, coeffs) in zip(keys, ROLFSEN):
        p = normalise_poly(Knots().from_table(n, k).alexander_polynomial())
        m = len(coeffs) - 1
        t = R.gen()
        q = coeffs[0] * t ** m + sum(coeffs[i] * (t ** (m + i) + t ** (m - i)) for i in range(1, m + 1))
        if q.leading_coefficient() < 0:
            q = -q
        check(p == q, 'p. 55: Alexander polynomial of %s from its braid = Rolfsen\'s table' % nm)
        polys.setdefault(p, []).append(nm)
    pairs = sorted(v for v in polys.values() if len(v) > 1)
    check(pairs == [['6_1', '9_46'], ['7_4', '9_2'], ['8_14', '9_8'], ['8_18', '9_24'], ['9_28', '9_29']],
          'p. 55: exactly 5 pairs of the 84 knots share an Alexander polynomial: %s' % pairs)
    refuted(len(pairs) == 3, 'p. 55 printed: "лишь три пары узлов не различаются с помощью многочленов Александера"')


def perm_module(T, Hs, p):
    """F_p[H \\ G]: the permutation module on the right cosets H g."""
    cos = []
    seen = {}
    for g in range(T.n):
        c = frozenset(T.mul[h][g] for h in Hs)
        if c not in seen:
            seen[c] = len(cos)
            cos.append(c)
    k = len(cos)

    def act(g):
        M = [[0] * k for _ in range(k)]
        for i, c in enumerate(cos):
            x = min(c)
            j = seen[frozenset(T.mul[T.mul[h][x]][g] for h in Hs)]
            M[i][j] = 1
        return M
    return Mod(T, p, k, act, 'F_%d[H\\G], |H| = %d' % (p, len(Hs)))


def word_to_gap(F, w):
    gens = F.GeneratorsOfGroup()
    out = F.One()
    for l in w:
        out = out * (gens[abs(l) - 1] if l > 0 else gens[abs(l) - 1] ** -1)
    return out


def closure_add(A, gens):
    S = {A.zero}
    frontier = [A.zero]
    gens = list(set(gens))
    while frontier:
        new = []
        for x in frontier:
            for g in gens:
                y = A.add(x, g)
                if y not in S:
                    S.add(y)
                    new.append(y)
        frontier = new
    return S


def all_normalised_bruteforce(A):
    T = A.T
    pairs = [(a, b) for a in range(T.n) for b in range(T.n) if a != T.e and b != T.e]
    out = []
    for vals in itertools.product(A.elts, repeat=len(pairs)):
        h = zero_cocycle(A)
        h.update(dict(zip(pairs, vals)))
        if cocycle_ok(A, h):
            out.append(h)
    return out


# ---------------------------------------------------------------------------
# section 10
# ---------------------------------------------------------------------------

def section_10():
    # exm:nilpotent-class-two-endomorphisms, lem:central-quotient-identity
    for (o, i) in [(8, 3), (8, 4), (16, 3), (16, 4), (27, 3), (32, 2)]:
        G = gap('SmallGroup(%d,%d)' % (o, i))
        assert int(G.NilpotencyClassOfGroup()) == 2
        fun = gap('''function(G)
          local A, gens, el, ims, hom, res, tup;
          A := DerivedSubgroup(G);
          gens := MinimalGeneratingSet(G);
          el := AsList(A);
          res := [0, 0];
          for tup in Cartesian(List(gens, g -> el)) do
            ims := List([1..Length(gens)], j -> gens[j] * tup[j]);
            hom := GroupHomomorphismByImages(G, G, gens, ims);
            if hom <> fail then
              res[1] := res[1] + 1;
              if ForAll(el, a -> Image(hom, a) = a) then res[2] := res[2] + 1; fi;
            fi;
          od;
          return res;
        end''')
        r = fun(G).sage()
        check(r[0] >= 1 and r[0] == r[1], 'exm:nilpotent-class-two-endomorphisms: all %d endomorphisms '
              'x -> x a (a in G\') are the identity on A = G\' (SmallGroup(%d,%d))' % (r[0], o, i))
    # th:endomorphism-extension by brute force
    exs = pick(ext_examples(), 3)
    for (T, A, h, lab) in exs:
        E = Ext(A, h)
        der = z1_list(A)
        # G-module endomorphisms of A
        endos = []
        for M in itertools.product(range(A.m), repeat=A.k * A.k):
            Mm = [list(M[r * A.k:(r + 1) * A.k]) for r in range(A.k)]

            def fa(a, Mm=Mm):
                return tuple(sum(a[j] * Mm[j][c] for j in range(A.k)) % A.m for c in range(A.k))
            if all(fa(A.act(a, g)) == A.act(fa(a), g) for a in A.basis() for g in range(T.n)):
                endos.append(fa)
        for fa in endos:
            exts = []
            for us in itertools.product(A.elts, repeat=len(T.gens)):
                imgs = [(g, u) for g, u in zip(T.gens, us)]
                hom = endo_images(E, imgs, fa)
                if hom != gap('fail'):
                    exts.append(hom)
            diff = {q: A.sub(fa(h[q]), h[q]) for q in h}
            obstr = in_b2(A, diff) if Integer(A.m).is_prime() else in_b2_brute(A, diff)
            check(bool(exts) == obstr, 'th:endomorphism-extension: f extends <=> (f^* - 1) h_E = 0 (%s)' % lab)
            if exts:
                # total number of extensions (all u: G -> A, not only on generators) = |Der|
                check(len(exts) == len(der), 'th:endomorphism-extension: %d extensions = |Der(G, A)| (%s)'
                      % (len(exts), lab))
                f1 = exts[0]
                for f2 in exts:
                    # phi(x) = x u2(x) u1(x)^-1 lies in Aut E and f2 = phi f1
                    ims = {}
                    for x in E.el:
                        y1 = perm_to_el(E, f1.Image(E.p(x)))
                        y2 = perm_to_el(E, f2.Image(E.p(x)))
                        # f_i(x) = x u_i(x) = (g, a + u_i); phi(x) = x u2(x) u1(x)^-1
                        ims[x] = (x[0], A.add(x[1], A.sub(y2[1], y1[1])))
                    ok_aut = all(ims[E.mul(x, y)] == E.mul(ims[x], ims[y]) for x in E.el for y in E.el) and \
                        all(ims[(T.e, a)] == (T.e, a) for a in A.elts)
                    ok_comp = all(ims[perm_to_el(E, f1.Image(E.p(x)))] == perm_to_el(E, f2.Image(E.p(x))) for x in E.el)
                    check(ok_aut and ok_comp, 'th:endomorphism-extension: f-bar_2 = phi f-bar_1 with phi in Aut E (%s)' % lab)
    # the printed f-bar_2 = f-bar_1 phi refuted: split extension, f = 0
    T = cyclic(2)
    A = trivial(T, 2)
    E = Ext(A, zero_cocycle(A))
    t = T.gens[0]
    f1 = endo_images(E, [(t, (0,))], lambda a: (0,))
    f2 = endo_images(E, [(t, (1,))], lambda a: (0,))
    autE = aut_e(E)
    check(f1 != gap('fail') and f2 != gap('fail') and len(autE) == 2, 'p. 58: Z_2 x Z_2, f = 0 has 2 extensions')
    refuted(any(all(f1.Image(phi.Image(E.p(x))) == f2.Image(E.p(x)) for x in E.el) for phi in autE),
            'th:endomorphism-extension printed: f-bar_2 = f-bar_1 phi for some phi in Aut E')
    check(any(all(phi.Image(f1.Image(E.p(x))) == f2.Image(E.p(x)) for x in E.el) for phi in autE),
          'th:endomorphism-extension corrected: f-bar_2 = phi f-bar_1')
    # lem:endomorphism-combination: x -> x prod u_i(x)^(n_i)
    for (T, A, h, lab) in pick(ext_examples(), 1):
        E = Ext(A, h)
        endos = []
        for us in itertools.product(A.elts, repeat=len(T.gens)):
            hom = endo_images(E, [(g, u) for g, u in zip(T.gens, us)], lambda b: b)
            if hom != gap('fail'):
                endos.append({x: perm_to_el(E, hom.Image(E.p(x))) for x in E.el})
        ok = True
        for _ in range(10):
            ch = random.sample(endos, min(3, len(endos)))
            ns = [random.randint(-2, 2) for _ in ch]
            phi = {}
            for x in E.el:
                u = A.zero
                for f, nn in zip(ch, ns):
                    u = A.add(u, A.smul(nn, A.sub(f[x][1], x[1])))
                phi[x] = (x[0], A.add(x[1], u))
            ok = ok and all(phi[E.mul(x, y)] == E.mul(phi[x], phi[y]) for x in E.el for y in E.el)
        check(ok, 'lem:endomorphism-combination: x -> x prod u_i(x)^(n_i) is an endomorphism (%s)' % lab)
    # prop:central-power-extension (corrected) for abelian G (Z(G) = G)
    for (T, A, h, lab) in [e for e in ext_examples() if bool(e[0].G.IsAbelian())]:
        E = Ext(A, h)
        for r in itertools.product(range(-1, 3), repeat=T.n):
            r = list(r)
            fa = lambda a, r=r: A.actr(a, r)
            ext = any(endo_images(E, [(g, u) for g, u in zip(T.gens, us)], fa) != gap('fail')
                      for us in itertools.product(A.elts, repeat=len(T.gens)))
            k = eps(r) - 1
            kh = {q: A.smul(k, h[q]) for q in h}
            cond = in_b2(A, kh) if Integer(A.m).is_prime() else in_b2_brute(A, kh)
            check(ext == cond, 'prop:central-power-extension: f_r extends <=> (eps(r) - 1) h_E = 0, r = %s (%s)' % (r, lab))
    # printed reading refuted: G = Z^2, A = Z trivial, E = E_1 of § 6, r = 1 (eps(r) - 1 = 0): the
    # identity of G_1 extends f_1 = id, so the printed statement would give h_(E_1) a finite order m.
    # But m h_(E_1) = h_(E_m) (the factor system -m a' b of E_m is m times that of E_1, polynomial
    # identity below) and E_m does not split: a split central extension of the abelian G is abelian,
    # while in G_m (matrices of p. 32, z = 1 + N/m) the commutator [x, y] is the same matrix C != 1.
    X = matrix(QQ, [[1, 1, 0], [0, 1, 0], [0, 0, 1]])
    Y = matrix(QQ, [[1, 0, 0], [0, 1, 1], [0, 0, 1]])
    C = X.inverse() * Y.inverse() * X * Y
    Rm = PolynomialRing(ZZ, 'm,a,b,a1,b1')
    mm, a_, b_, a1_, b1_ = Rm.gens()
    linear = (-mm * a1_ * b_) == mm * (-1 * a1_ * b_)
    nonabelian = C != identity_matrix(QQ, 3) and all(
        matrix(QQ, [[1, 0, QQ(1) / k], [0, 1, 0], [0, 0, 1]]) ** k == C for k in range(1, 30))
    finite_order = not (linear and nonabelian)
    refuted(finite_order,
            'prop:central-power-extension printed: r = 1 (eps(r) - 1 = 0) extends for every E, so h_(E_1) '
            'would have a finite order; but m h_(E_1) = h_(E_m) != 0 for all m != 0 (G = Z^2, A = Z)')
    # eq:inner-endomorphism, exc:inner-endomorphism-representatives, semigroup
    for (T, A, h, lab) in pick([e for e in ext_examples() if bool(e[0].G.IsAbelian())], 2):
        E = Ext(A, h)

        def comm_el(x, y):
            return E.mul(E.mul(E.inverse(x), E.inverse(y)), E.mul(x, y))

        def inner_endo(gbars, ns):
            out = {}
            for x in E.el:
                y = x
                for gb, nn in zip(gbars, ns):
                    c = comm_el(x, gb)
                    for _ in range(abs(nn)):
                        y = E.mul(y, c if nn > 0 else E.inverse(c))
                out[x] = y
            return out
        for _ in range(6):
            gs = random.sample(range(T.n), min(3, T.n))
            ns = [random.randint(-2, 2) for _ in gs[:-1]]
            ns.append(1 - sum(ns))            # eps(r) = 1
            gbars = [(g, A.zero) for g in gs]
            phi = inner_endo(gbars, ns)
            r = [0] * T.n
            for g, nn in zip(gs, ns):
                r[g] += nn
            ok = all(phi[E.mul(x, y)] == E.mul(phi[x], phi[y]) for x in E.el for y in E.el) and \
                all(phi[(T.e, a)] == (T.e, A.actr(a, r)) for a in A.elts)
            check(ok, 'eq:inner-endomorphism: x -> x prod [x, g_i-bar]^(n_i) is an endomorphism with a -> a r (%s)' % lab)
            # replace g_i-bar by g_i-bar a_i
            as_ = [random.choice(A.elts) for _ in gs]
            phi2 = inner_endo([(g, a) for g, a in zip(gs, as_)], ns)
            acorr = A.zero
            aprnt = A.zero
            for a, nn in zip(as_, ns):
                acorr = A.add(acorr, A.smul(nn, a))
                aprnt = A.add(aprnt, a)

            def alpha(a, y):     # a^-1 y a
                return E.mul(E.mul((T.e, A.sub(A.zero, a)), y), (T.e, a))
            check(all(phi2[x] == alpha(acorr, phi[x]) for x in E.el),
                  'exc:inner-endomorphism-representatives: the new endomorphism is alpha_a phi with a = prod a_i^(n_i) (%s)' % lab)
    # printed a = prod a_i refuted: G = Z_2 acting on Z_4 by inversion (D_8), r = 2 g - 1
    T = cyclic(2)
    A = inversion(T, 4)
    E = Ext(A, h2_reps_bruteforce(A)[0])
    g = T.gens[0]

    def comm_el2(x, y):
        return E.mul(E.mul(E.inverse(x), E.inverse(y)), E.mul(x, y))

    def endo2(gb):
        out = {}
        for x in E.el:
            c = comm_el2(x, gb)
            ci = comm_el2(x, (T.e, A.zero))
            out[x] = E.mul(E.mul(E.mul(x, c), c), E.inverse(ci))
        return out
    a1 = (1,)
    phi = endo2((g, A.zero))
    phi2 = endo2((g, a1))

    def alpha2(a, y):
        return E.mul(E.mul((T.e, A.sub(A.zero, a)), y), (T.e, a))
    check(all(phi2[x] == alpha2(A.smul(2, a1), phi[x]) for x in E.el),
          'exc:inner-endomorphism-representatives: r = 2 g - 1, g-bar -> g-bar a: alpha_(a^2) (D_8)')
    refuted(all(phi2[x] == alpha2(a1, phi[x]) for x in E.el),
            'exc:inner-endomorphism-representatives printed: a = prod a_i (here a instead of a^2, D_8)')
    # exc:inner-endomorphisms-semigroup / -metabelian: composition <-> product of r-bar
    for (T, A, h, lab) in pick([e for e in ext_examples() if bool(e[0].G.IsAbelian())], 3):
        E = Ext(A, h)

        def comm_el(x, y):
            return E.mul(E.mul(E.inverse(x), E.inverse(y)), E.mul(x, y))

        def endo_of(rbar):          # rbar: dict element of G-bar -> coefficient, eps = 1
            out = {}
            for x in E.el:
                y = x
                for gb, nn in rbar.items():
                    c = comm_el(x, gb)
                    for _ in range(abs(nn)):
                        y = E.mul(y, c if nn > 0 else E.inverse(c))
                out[x] = y
            return out

        def rand_rbar():
            gs = random.sample(E.el, 2)
            n1 = random.randint(-2, 2)
            return {gs[0]: n1, gs[1]: 1 - n1}

        def rmul(r1, r2):
            out = {}
            for x, a in r1.items():
                for y, b in r2.items():
                    z = E.mul(x, y)
                    out[z] = out.get(z, 0) + a * b
            return out
        ok_rs = ok_sr = ok_comm = True
        for _ in range(8):
            r1, r2 = rand_rbar(), rand_rbar()
            p1, p2 = endo_of(r1), endo_of(r2)
            comp = {x: p1[p2[x]] for x in E.el}          # p1 after p2
            ok_rs = ok_rs and comp == endo_of(rmul(r1, r2))
            ok_sr = ok_sr and comp == endo_of(rmul(r2, r1))
            comp2 = {x: p2[p1[x]] for x in E.el}
            # modulo inner automorphisms by A
            ok_comm = ok_comm and any(all(comp[x] == E.mul(E.mul((T.e, A.sub(A.zero, a)), comp2[x]), (T.e, a))
                                          for x in E.el) for a in A.elts)
        check(ok_rs or ok_sr, 'exc:inner-endomorphisms-semigroup: the composition of the endomorphisms of '
              'r-bar and s-bar is that of a product of r-bar and s-bar in Z G-bar (%s)' % lab)
        check(ok_comm, 'exc:inner-endomorphisms-metabelian: phi_r phi_s and phi_s phi_r differ by an inner '
              'automorphism by an element of A (%s)' % lab)
    # exc:homomorphism-lifting
    Bs = [gap('SmallGroup(%d,%d)' % oi) for oi in [(2, 1), (3, 1), (4, 1), (4, 2), (6, 1), (8, 3), (8, 4), (8, 2)]]
    for (T, A, h, lab) in pick([e for e in ext_examples() if Integer(e[1].m).is_prime()], 2):
        E = Ext(A, h)
        for B in Bs:
            TB = TGroup(B, str(B))
            for f in gap('AllHomomorphisms')(B, T.G):
                fl = [T.index(f.Image(x)) for x in TB.gelts]
                # lifting: images of generators of B in f(b) A
                lift = False
                for us in itertools.product(A.elts, repeat=len(TB.gens)):
                    gens = [x for x in B.GeneratorsOfGroup()]
                    ims = [E.p((fl[TB.index(x)], u)) for x, u in zip(gens, us)]
                    hom = libgap.GroupHomomorphismByImages(B, E.P, gens, ims)
                    if hom != gap('fail'):
                        lift = True
                        break
                # f^* h in H^2(B, A), A a B-module through f
                AB = Mod(TB, A.m, A.k, lambda b: A.mats[fl[b]], A.name + ' via f')
                fh = {(a, b): h[(fl[a], fl[b])] for a in range(TB.n) for b in range(TB.n)}
                check(lift == in_b2(AB, fh), 'exc:homomorphism-lifting: f lifts <=> f^* h = 0 in H^2(B, A) '
                      '(B = %s, %s)' % (B, lab))


def in_b2_brute(A, diff):
    T = A.T
    target = tuple(diff[q] for q in sorted(diff))
    for vals in itertools.product(A.elts, repeat=T.n):
        phi = dict(zip(range(T.n), vals))
        d = coboundary_cocycle(A, phi)
        if tuple(d[q] for q in sorted(d)) == target:
            return True
    return False


def aut_e(E):
    T, A = E.T, E.A
    auts = []
    for us in itertools.product(A.elts, repeat=len(T.gens)):
        imgs = [E.mul((g, A.zero), (T.e, u)) for g, u in zip(T.gens, us)]
        hom = endo_images(E, imgs, lambda b: b)
        if hom != gap('fail') and bool(hom.IsBijective()):
            auts.append(hom)
    return auts


def main():
    random.seed(20261105)
    section_8()
    section_9()
    section_10()
    print('ok %s: %d checks' % (SCOPE, COUNT[0]))


if __name__ == '__main__':
    main()
