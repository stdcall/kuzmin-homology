"""Exact checks of Chapter 1, §§ 1-7 (printed pp. 13-41) of Yu. V. Kuzmin,
"Гомологическая теория групп" (Moscow: Factorial Press, 2006).

Run from the project root: sage -python checks/sage/chapter-1a.py
(plain asserts; do not use -O).  The last line is "ok chapter-1a: N checks".
Pages are the printed pages; labels are those of content/01-*.typ.
Conventions of the book: right modules, a^g = g^(-1) a g, [x, y] =
x^(-1) y^(-1) x y, right derivations phi(g1 g2) = phi(g1) g2 + phi(g2).

Finite groups come from GAP (libgap, SmallGroups library) as multiplication
tables; modules are Z_m^k with G acting on row vectors by integer matrices
from the right; group rings are integer vectors indexed by the elements.
Cohomology of finite groups is computed from inhomogeneous cochains (the
coboundaries of §§ 7-8): over GF(p) by ranks of sparse matrices, for Z_m by
elementary divisors over ZZ.  Extensions are built from normalised
2-cocycles as groups of pairs (§ 8), turned into permutation groups for GAP.
Expected values are the book's statements; a printed reading that is wrong
is kept as a refuted check (`refuted`) beside the corrected one.

What is checked, by section:

section_1 (pp. 13-17): the decomposition of Delta_H at the end of § 1
  (correction of p. 16): for every subgroup 1 < H < G of S_3 and D_8 the
  elements (h - 1) g_i (h != 1, g_i right coset representatives) form a
  Z-basis of the right ideal Delta_H, and the printed Delta_G is not
  spanned by them; Delta_H is two-sided and equals Ker(ZG -> Z[G/H]) for
  normal H; exc:norm-element: sigma g = sigma and sigma (g - 1) = 0 with
  g - 1 != 0 for 8 groups of order 2-12, while for G = 1 sigma = 1 is no
  zero divisor (printed statement without G != 1 refuted, corrected one
  checked); exc:group-ring-units: g^2 - g + 1 is a unit for |g| = 5 (its
  inverse computed), and f(g) = g^(p-1) - ... - g + 1 is a unit of Z[C_n]
  with inverse q(g), f(x^n) = f(x) q(x), for all 45 pairs n odd <= 21,
  p in {3, 5, 7, 11, 13}, p not dividing n; the hypotheses are needed
  ((n, p) = (3, 3), (2, 3), (4, 5): a norm Res(Phi_d, f) != +-1);
  exc:tensor-coinvariants: (A (x) A)_G and A (x)_G A have equal dimension
  for the regular F_p-modules of S_3 (p = 2, 3) and Z_4 (p = 2).
section_2 (pp. 17-21): the two G-module structures on A (x) ZG of p. 19 are
  isomorphic by a (x) g -> a g (x) g (S_3 on F_2^2, all elements);
  cor:coinduced-embedding (a -> phi_a, phi_a(g) = a g, is a G-monomorphism;
  S_3 on F_2^2, Z_4 on Z_5); exc:coinduced-diagonal (f -> phi, phi(g) =
  f(g) g^(-1), is an isomorphism from the coinduced to the diagonal module,
  exhaustively over all functions G -> A in both cases); exc:normal-basis:
  GF(p^n) has a normal basis over GF(p) for p^n <= 2^8, 3^5, 5^4, 7^3.
section_3 (pp. 21-24): for all 586 groups of order <= 64 the nilpotency
  class read from the lower and from the upper central series agree,
  gamma_n is central and G^((n-1)) abelian (the extension descriptions of
  nilpotent and solvable groups).
section_4 (pp. 24-29): for all 460 non-abelian metabelian groups of order
  <= 64, with A = G-bar' and G = G-bar / A: A Delta_G^n computed in the
  module equals the iterated commutator subgroup [A, G-bar, ..., G-bar]
  (n <= 8; bars restored in the proof of th:metabelian-residually-nilpotent,
  p. 26) and gamma_(n+2) <= A Delta^n <= gamma_(n+1); for those with
  |A| <= 16, eq:lower-central-annihilator: the intersection of the lower
  central series is {a : a(1 + r) = 0 for some r in Delta_G} (Delta_G
  realised as the additive group of endomorphisms of A spanned by all
  g - 1); the equation of the proof, v(a, c) = a^(1+r) with sigma(v) = 1.
  exc:lower-central-equations (p. 29): the printed "x = prod [x, c_i]" is
  refuted by G-bar = Z^2 x| Z, t acting by M = [[0, -1], [1, 1]] (order 6,
  M - 1 invertible): the intersection of the gamma_n is A = Z^2, but
  tr(M^k - 1) <= 0 for all k, so tr(sum (M^(k_i) - 1)) <= 0 < 2 and in the
  field Q[M] = Q(zeta_6) x(1 - s) = 0 forces x = 0; all equations with at
  most 6 factors have only x = 1; with exponents +-1 (corrected) the
  equation x = [x, t]^(-1) [x, t^(-1)]^(-1) holds on a box of Z^2.
section_5 (pp. 29-31): the pair multiplication of the semidirect product is
  associative and (g^-1, 1)(1, a)(g, 1) = (1, a^g) (S_3 on F_2^2, Z_4 on
  Z_5); exc:free-metabelian-derived: in G A with G = Z^2 = <s, t>, A = ZG,
  x -> (s, 1), y -> (t, 0), the commutator [x, y] goes to (1, t - 1) (formula
  (1.22)), a non-zero element of the domain ZG.
section_6 (pp. 32-34): the matrices of G_n for 0 < |n| <= 7 ([X, Y] = Z^n,
  Z central, Z = 1 + N with N^2 = 0, N != 0, hence of infinite order);
  G_n / G_n' = Z^2 + Z_|n| (GAP, |n| <= 8; G_0 = Z^3; correction of p. 33
  "свободной абелевой": the printed free group of rank 2 is not abelian);
  f: G_n -> G_(-n) and the corrections by central c, d (n = 1, 2, 3, -2, 5);
  the factor system -n a' b of E_n for the transversal x^a y^b (cocycle,
  linear in n, so E_n + E_m = E_(n+m), alternation n (a b' - a' b)), also in
  the matrices; exc:generator-swap-isomorphism; exc:central-extensions-of-
  free-abelian: H^2(Z^2, Z) = Z (cubical torus); exc:cyclic-p-extensions:
  |H^2(Z_p, Z_p)| = p, the carry cocycles c [i + j >= p] are pairwise not
  cohomologous, class 0 gives Z_p x Z_p and the p - 1 others Z_(p^2)
  (p = 2, 3, 5); exc:weak-equivalence: Aut(Z_p) has 2 orbits on the classes.
section_7 (pp. 34-41): for 19 extensions built from cocycles (G of order
  2, 3, 4, 6, 8; modules F_2, F_3, F_2^2, Z_4 with inversion; split and
  non-split): Aut E computed in GAP (images x -> x u of the generators that
  extend to automorphisms) is abelian with |Aut E| = |Der(G, A)|, the inner
  automorphisms by A are a^(-1) g-bar a = g-bar a^(1 - g), |B^1| = |A / A^G|,
  |Aut E / Inn E| = |H^1|, phi(r t) = phi(r) t + eps(r) phi(t) on ZG, the
  principal derivations extend as a(eps(r) - r), prop:h1-finite-exponent
  (n phi(g - 1) = a (g - 1) with a = phi(n - sigma)) and, for central
  extensions, cor:central-extension-automorphisms (|Aut E| =
  |Hom(G_ab, A)|); prop:coinduced-kernel-automorphisms (H^1(G, Hom(ZG, F_p))
  = 0, p = 2, 3, for Z_2, Z_3, Z_2^2, S_3, D_8, and the identity
  (alpha o (1 - g))(g') = -phi(g)(g') of the proof); cor:zassenhaus (4
  examples); th:coprime-complements-conjugate: all 3081 pairs (G, N),
  |G| <= 200 (orders 128, 192 skipped), N a normal Hall subgroup, have
  exactly one class of complements; exc:centralizer-quotient and
  exc:extension-automorphisms-abelian for all 406 pairs (G, A), |G| <= 24,
  |Aut G| <= 2000, A normal (abelian or not); exc:series-stability-group:
  the stability groups of 44 normal series (lower and upper central,
  chief, derived) of 11 p-groups of order <= 27 have class <= n;
  exc:torsion-free-kernel: the reading "additive group without torsion"
  refuted by Z x Z_3 with f = id x (-1); exc:automorphisms-over-quotient:
  |Aut_G G-bar| = |Aut E| |Aut_G A| for the split S_3 F_2^2 and Z_4 Z_5;
  exc:induced-automorphism-of-h1 with alpha_x(y) = x^(-1) y x: alpha_x^* phi
  = phi - phi_a, a = phi(x) (all derivations, all x); exc:inversion-action:
  |H^1(Z_2, A)| = |A / 2A| for 9 finite abelian groups A;
  exc:cyclic-quotient: phi -> phi(g) is a bijection Der -> {a : a N = 0}
  and Inn E = A(1 - g) for 26 cyclic modules (orders 2-6);
  exc:trace-kernel and exc:norm-variant: Ker T = {a - a^p} and
  Ker N = {a^(1-p)} in GF(p^n) for p^n <= 2^10, 3^6, 5^4, 7^3, 11^2, 13^2,
  including p | n (the hypothesis "p и n взаимно просты" is not needed);
  exc:additive-galois-cohomology and exc:multiplicative-galois-cohomology:
  by brute force for GF(4), GF(8), GF(9), GF(16), GF(27), GF(25) every
  derivation into L^+ and every crossed homomorphism into L^* is principal,
  the hint a = sum f(g_i) x^(g_i) gives f(g) a^g = a and a != 0 for some x,
  and the automorphisms are linearly independent as characters
  S = L^* -> L^* (corrected Artin lemma, p. 41); exc:hilbert-90:
  Ker T = {a - a^q} and Ker N = {a^(1-q)} for GF(q^n) / GF(q),
  (q, n) = (4, 2), (4, 3), (8, 2), (9, 2), (2, 6), (3, 4), (4, 4), (16, 2),
  (27, 2), (25, 2).

What these checks do NOT establish.  Every check is an exact computation for
the listed groups, modules, fields and parameters, exhaustive only where so
stated, or an identity of polynomials; none proves a general theorem of the
book.  The infinite groups of §§ 4-6 are handled through exact integer and
rational matrices, GAP's finitely presented groups, or the cubical torus
(a K(Z^2, 1)) for Z^2 only.
Random elements are drawn with a fixed seed.  Nothing here compares our
text with the printed book.
"""

import itertools
import random

from sage.all import (
    GF, QQ, ZZ, Integer, PolynomialRing, cubical_complexes, gcd,
    identity_matrix, libgap, matrix, prod, vector,
)

SCOPE = 'chapter-1a'
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
# Finite groups as multiplication tables, modules, group rings
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


# ---------------------------------------------------------------------------
# section 1
# ---------------------------------------------------------------------------

def lattice(vecs, n):
    M = matrix(ZZ, vecs) if vecs else matrix(ZZ, 0, n)
    H = M.echelon_form()
    return H.matrix_from_rows([i for i in range(H.nrows()) if not H.row(i).is_zero()])


def section_1():
    # p. 16, decomposition of Delta_H (correction: Delta_G -> Delta_H)
    for (o, i) in [(6, 1), (8, 3)]:
        T = small(o, i)
        subs = gap('function(G) return List(ConjugacyClassesSubgroups(G), Representative); end')(T.G)
        for H in subs:
            Hs = [T.index(x) for x in H.AsSSortedList()]
            if len(Hs) in (1, T.n):
                continue
            # right cosets H g
            reps, seen = [], set()
            for g in range(T.n):
                if g not in seen:
                    reps.append(g)
                    seen.update(T.mul[h][g] for h in Hs)
            basis = [zg_add(zg_unit(T, T.mul[h][g]), zg_unit(T, g), -1)
                     for h in Hs if h != T.e for g in reps]
            ideal = [zg_mul(T, zg_add(zg_unit(T, h), zg_unit(T, T.e), -1), zg_unit(T, g))
                     for h in Hs for g in range(T.n)]
            LB, LI = lattice(basis, T.n), lattice(ideal, T.n)
            check(matrix(ZZ, basis).rank() == len(basis) and LB == LI,
                  'p. 16: the (h - 1) g_i (h in H, h != 1) form a basis of Delta_H, '
                  '%s, |H| = %d' % (T.name, len(Hs)))
            augG = [zg_add(zg_unit(T, g), zg_unit(T, T.e), -1) for g in range(T.n)]
            refuted(lattice(augG, T.n) == LB,
                    'p. 16 printed: Delta_G spanned by the (h - 1) g_i, %s, |H| = %d'
                    % (T.name, len(Hs)))
            if bool(gap('IsNormal')(T.G, H)):
                two = [zg_mul(T, zg_unit(T, g), v) for g in range(T.n) for v in ideal]
                check(lattice(two + ideal, T.n) == LI,
                      'p. 16: Delta_H two-sided for normal H (%s)' % T.name)
                # kernel of ZG -> Z[G/H]
                cos = {}
                for g in range(T.n):
                    cos[g] = frozenset(T.mul[h][g] for h in Hs)
                classes = sorted(set(cos.values()), key=lambda s: min(s))
                Mmap = matrix(ZZ, [[1 if g in c else 0 for c in classes] for g in range(T.n)])
                K = Mmap.left_kernel().basis_matrix()
                check(lattice(list(K.rows()), T.n) == LI,
                      'p. 16: Delta_H = Ker(ZG -> Z[G/H]) (%s)' % T.name)
    # exc:norm-element
    for (o, i) in [(2, 1), (3, 1), (4, 1), (4, 2), (6, 1), (8, 3), (8, 4), (12, 3)]:
        T = small(o, i)
        sigma = [1] * T.n
        check(all(zg_mul(T, sigma, zg_unit(T, g)) == sigma for g in range(T.n)),
              'exc:norm-element: sigma g = sigma, %s' % T.name)
        g = T.gens[0]
        z = zg_mul(T, sigma, zg_add(zg_unit(T, g), zg_unit(T, T.e), -1))
        check(all(x == 0 for x in z) and g != T.e,
              'exc:norm-element: sigma (g - 1) = 0 with g - 1 != 0, %s' % T.name)
    T1 = TGroup(gap('Group(())'), 'trivial')
    sigma = [1]
    refuted(any(zg_mul(T1, sigma, [c])[0] == 0 for c in range(-5, 6) if c),
            'exc:norm-element printed for G = 1: sigma = 1 a zero divisor')
    check(T1.n == 1 and sigma == [1],
          'exc:norm-element corrected (G != 1): for G = 1, sigma = 1 is a unit')
    # exc:group-ring-units
    R = PolynomialRing(ZZ, 'x')
    x = R.gen()
    f5 = x ** 2 - x + 1
    q5 = (f5(x ** 5)) // f5
    check(f5 * q5 == f5(x ** 5) and (f5 * q5) % (x ** 5 - 1) == 1,
          'exc:group-ring-units: g^2 - g + 1 is a unit for |g| = 5, inverse %s' % (q5 % (x ** 5 - 1)))
    cnt = 0
    for n in range(1, 22, 2):
        for p in [3, 5, 7, 11, 13]:
            if gcd(p, n) != 1:
                continue
            f = sum((-1) ** i * x ** i for i in range(p))
            q, r = f(x ** n).quo_rem(f)
            ok = r == 0 and (f * q) % (x ** n - 1) == 1 and f(1) == 1
            check(ok, 'exc:group-ring-units: f(g) invertible in Z[C_%d], p = %d' % (n, p))
            cnt += 1
    check(cnt == 45, "exc:group-ring-units: all %d pairs (n odd <= 21, p in {3, 5, 7, 11, 13}, p not dividing n)" % cnt)
    # the hypotheses cannot be dropped: a unit of Z[C_n] maps to units of all Z[zeta_d], d | n,
    # so a norm Res(Phi_d, f) != +-1 shows that f(g) is not a unit
    for (n, p) in [(3, 3), (2, 3), (4, 5)]:
        f = sum((-1) ** i * x ** i for i in range(p))
        norms = [R.cyclotomic_polynomial(d).resultant(f) for d in Integer(n).divisors()]
        check(any(abs(N) != 1 for N in norms),
              'exc:group-ring-units: f(g) is not a unit in Z[C_%d] for p = %d (norms %s): '
              'the hypotheses "n нечётно", "(p, n) = 1" are needed' % (n, p, norms))
    # exc:tensor-coinvariants (A (x) A')_G = A (x)_G A' (dimensions over F_p)
    for (T, p) in [(small(6, 1), 2), (small(6, 1), 3), (cyclic(4), 2)]:
        A = Mod(T, p, T.n, lambda g: [[1 if T.mul[i][g] == j else 0 for j in range(T.n)]
                                      for i in range(T.n)], 'regular')
        F = GF(p)
        k = A.k
        # (A (x) A')_G : quotient of A (x) A by (a g (x) b g - a (x) b)
        rel1 = []
        rel2 = []
        for g in range(T.n):
            M = matrix(F, A.mats[g])
            K = M.tensor_product(M) - identity_matrix(F, k * k)
            rel1 += list(K.rows())
            # A (x)_G A': a g (x) b = a (x) b g^(-1) (left module g b = b g^(-1))
            Minv = matrix(F, A.mats[T.inv[g]])
            K2 = M.tensor_product(identity_matrix(F, k)) - identity_matrix(F, k).tensor_product(Minv)
            rel2 += list(K2.rows())
        d1 = k * k - matrix(F, rel1).rank()
        d2 = k * k - matrix(F, rel2).rank()
        check(d1 == d2, 'exc:tensor-coinvariants: dim (A (x) A)_G = dim A (x)_G A = %d '
              '(%s, regular module over F_%d)' % (d1, T.name, p))


# ---------------------------------------------------------------------------
# section 2
# ---------------------------------------------------------------------------

def mod_s3_f2():
    T = small(6, 1)
    # the 2-dimensional irreducible F_2 S_3-module: S_3 = GL_2(2)
    iso = libgap.IsomorphismGroups(T.G, gap('GL(2,2)'))
    mats = [[[int(c) for c in row] for row in gap('function(i,x) return List(Image(i,x), r -> List(r, IntFFE)); end')(iso, gx).sage()]
            for gx in T.gelts]
    # GL acts on row vectors from the right: v -> v M
    return T, Mod(T, 2, 2, lambda g: mats[g], 'F_2^2 natural for GL_2(2) = S_3')


def section_2():
    T, A = mod_s3_f2()
    # A (x) ZG with (a (x) r) g = a (x) r g and with the diagonal action; the map
    # a (x) g -> a g (x) g is an isomorphism of G-modules
    def act1(x, g):
        a, h = x
        return (a, T.mul[h][g])

    def act2(x, g):
        a, h = x
        return (A.act(a, g), T.mul[h][g])

    def F(x):
        a, h = x
        return (A.act(a, h), h)
    dom = [(a, h) for a in A.elts for h in range(T.n)]
    check(len(set(F(x) for x in dom)) == len(dom) and
          all(F(act1(x, g)) == act2(F(x), g) for x in dom for g in range(T.n)),
          'p. 19: a (x) g -> a g (x) g is an isomorphism of the two G-modules A (x) ZG (S_3, F_2^2)')
    # cor:coinduced-embedding: a -> phi_a, phi_a(g) = a g; (f g)(r) = f(g r)
    for (TT, AA) in [(T, A), mod_z4_on_z5()]:
        def phi(a):
            return tuple(AA.act(a, g) for g in range(TT.n))

        def coact(f, g):   # (f g)(h) = f(g h)
            return tuple(f[TT.mul[g][h]] for h in range(TT.n))
        ok = all(phi(AA.act(a, g)) == coact(phi(a), g) for a in AA.elts for g in range(TT.n))
        inj = len(set(phi(a) for a in AA.elts)) == len(AA.elts)
        check(ok and inj, 'cor:coinduced-embedding: a -> phi_a, phi_a(g) = a g, is a '
              'G-monomorphism A -> Hom(ZG, A) (%s, %s)' % (TT.name, AA.name))
        # exc:coinduced-diagonal: Phi(f)(g) = f(g) g^(-1) from coinduced to diagonal
        # diagonal: (f o g)(h) = f(g h) g  (ex. 1.10 with ZG a left module)
        funcs = list(itertools.product(AA.elts, repeat=TT.n)) if len(AA.elts) ** TT.n <= 5000 else \
            [tuple(random.choice(AA.elts) for _ in range(TT.n)) for _ in range(400)]

        def Phi(f):
            return tuple(AA.act(f[h], TT.inv[h]) for h in range(TT.n))

        def diag(f, g):
            return tuple(AA.act(f[TT.mul[g][h]], g) for h in range(TT.n))
        ok = all(Phi(coact(f, g)) == diag(Phi(f), g) for f in funcs for g in range(TT.n))
        check(ok and len(set(Phi(f) for f in funcs)) == len(funcs),
              'exc:coinduced-diagonal: f -> phi, phi(g) = f(g) g^(-1), is an isomorphism '
              'Hom(ZG, A) (coinduced) -> Hom(ZG, A) (diagonal), %s, %s, %d functions'
              % (TT.name, AA.name, len(funcs)))
    # exc:normal-basis: GF(p^n) has a normal basis over GF(p)
    for (p, nmax) in [(2, 8), (3, 5), (5, 4), (7, 3)]:
        for n in range(2, nmax + 1):
            K = GF(p ** n, 'z')
            V, from_V, to_V = K.vector_space(map=True)
            found = None
            for e in K:
                M = matrix(GF(p), [to_V(e ** (p ** i)) for i in range(n)])
                if M.det() != 0:
                    found = e
                    break
            check(found is not None, 'exc:normal-basis: GF(%d^%d) has a normal basis over GF(%d)'
                  % (p, n, p))


def mod_z4_on_z5():
    T = cyclic(4)
    g = T.gens[0]
    # generator acts by multiplication by 2 (order 4 mod 5)
    mats = {}
    for k in range(4):
        mats[T.power(g, k)] = [[pow(2, k, 5)]]
    return T, Mod(T, 5, 1, lambda h: mats[h], 'Z_5, generator acting by 2')


# ---------------------------------------------------------------------------
# section 3
# ---------------------------------------------------------------------------

def section_3():
    # p. 23: class n (gamma_(n+1) = 1 != gamma_n) <=> Z_n = G != Z_(n-1), and the
    # extension descriptions of solvable / nilpotent groups (G^((n-1)) abelian,
    # gamma_n central), for all groups of order <= 64
    fun = gap('''function(G)
      local L, U, D, c, d;
      L := LowerCentralSeriesOfGroup(G);
      U := UpperCentralSeriesOfGroup(G);
      D := DerivedSeriesOfGroup(G);
      if IsNilpotentGroup(G) then
        c := Length(L) - 1;
        if not (Length(U) - 1 = c and IsAbelian(L[Maximum(c, 1)]) and
                (c = 0 or IsSubgroup(Centre(G), L[c]))) then return false; fi;
      fi;
      if IsSolvableGroup(G) then
        d := Length(D) - 1;
        if not (d = 0 or IsAbelian(D[d])) then return false; fi;
      fi;
      return true;
    end''')
    tot = 0
    for o in range(1, 65):
        for i in range(1, int(gap('NumberSmallGroups(%d)' % o)) + 1):
            check(bool(fun(gap('SmallGroup(%d,%d)' % (o, i)))),
                  'p. 23: nilpotency class from the lower and upper central series agree, '
                  'gamma_n central and G^((n-1)) abelian, SmallGroup(%d,%d)' % (o, i))
            tot += 1
    check(tot == int(gap('Sum([1..64], NumberSmallGroups)')),
          'p. 23: all %d groups of order <= 64' % tot)


# ---------------------------------------------------------------------------
# section 4
# ---------------------------------------------------------------------------

def section_4():
    n_groups = 0
    fun = gap('''function(Gb)
      local A, gens, S, out, k, Snew, lcs, inter, Dbar, comm;
      A := DerivedSubgroup(Gb);
      gens := GeneratorsOfGroup(Gb);
      lcs := LowerCentralSeriesOfGroup(Gb);
      out := [];
      S := A;
      comm := A;
      for k in [1..8] do
        Snew := Subgroup(Gb, Concatenation([One(Gb)], List(Cartesian(AsList(S), gens), p -> Comm(p[1], p[2]))));
        comm := CommutatorSubgroup(comm, Gb);
        Add(out, [Snew = comm,
                  IsSubgroup(Snew, lcs[Minimum(k+2, Length(lcs))]),
                  IsSubgroup(lcs[Minimum(k+1, Length(lcs))], Snew)]);
        S := Snew;
      od;
      return out;
    end''')
    krull = gap('''function(Gb)
      local A, G, hom, el, gens, acts, Delta, new, x, y, s, inter, S, lcs;
      A := DerivedSubgroup(Gb);
      lcs := LowerCentralSeriesOfGroup(Gb);
      inter := lcs[Length(lcs)];
      el := AsSSortedList(A);
      gens := GeneratorsOfGroup(Gb);
      # endomorphisms of A as lists of positions; a -> a^(g - 1) = Comm(a, g), all g:
      # Delta_G is spanned additively by all g - 1
      acts := Set(List(AsList(Gb), g -> List(el, a -> Position(el, Comm(a, g)))));
      # additive closure: (f + f')(a) = f(a) f'(a)
      Delta := Set(acts);
      new := ShallowCopy(Delta);
      while Length(new) > 0 do
        s := [];
        for x in new do for y in acts do
          AddSet(s, List([1..Length(el)], i -> Position(el, el[x[i]] * el[y[i]])));
          AddSet(s, List([1..Length(el)], i -> Position(el, el[x[i]] * el[y[i]]^-1)));
        od; od;
        new := Difference(s, Delta);
        Delta := Union(Delta, new);
      od;
      # {a : a(1 + r) = 1 for some r in Delta}: a * r(a) = 1
      S := Filtered([1..Length(el)], i -> ForAny(Delta, r -> el[i] * el[r[i]] = One(Gb)));
      return [Set(el{S}) = AsSSortedList(inter), Length(Delta), Size(inter)];
    end''')
    for o in range(2, 65):
        ng = int(gap('NumberSmallGroups(%d)' % o))
        for i in range(1, ng + 1):
            Gb = gap('SmallGroup(%d,%d)' % (o, i))
            if int(Gb.DerivedLength()) > 2 or bool(Gb.IsAbelian()):
                continue
            res = fun(Gb).sage()
            check(all(r[0] for r in res),
                  'p. 26: A Delta_G^n = [A, G-bar, ..., G-bar] (n <= 8), SmallGroup(%d,%d)' % (o, i))
            check(all(r[1] and r[2] for r in res),
                  'p. 26: gamma_(n+2) <= A Delta^n <= gamma_(n+1), SmallGroup(%d,%d)' % (o, i))
            if int(gap('Size(DerivedSubgroup(SmallGroup(%d,%d)))' % (o, i))) <= 16:
                kr = krull(Gb).sage()
                check(kr[0], 'eq:lower-central-annihilator: cap gamma_n = {a : a(1 + r) = 0, '
                      'r in Delta}, SmallGroup(%d,%d) (|Delta-bar| = %d)' % (o, i, kr[1]))
            n_groups += 1
    check(n_groups == int(gap('Sum([2..64], o -> Number([1..NumberSmallGroups(o)], '
                              'i -> not IsAbelian(SmallGroup(o,i)) and '
                              'DerivedLength(SmallGroup(o,i)) <= 2))')),
          'p. 26: all %d non-abelian metabelian groups of order <= 64 covered' % n_groups)
    # the equation of the proof: v(x, c) = x prod c_i^(-1) x^(k_i) c_i, v(a, c) = a^(1 + r)
    T, A = mod_s3_f2()
    E = Ext(A, zero_cocycle(A))
    a = (T.e, (1, 0))
    r = {T.gens[0]: 2, T.gens[1]: -1, T.e: -1}
    val = a
    for g, k in r.items():
        c = (g, A.zero)
        cinv = (T.inv[g], A.zero)
        pw = E.one()
        for _ in range(abs(k)):
            pw = E.mul(pw, a if k > 0 else (T.e, A.sub(A.zero, a[1])))
        val = E.mul(val, E.mul(E.mul(cinv, pw), c))
    rr = [0] * T.n
    for g, k in r.items():
        rr[g] += k
    check(val == (T.e, A.actr(a[1], zg_add(zg_unit(T, T.e), rr))) and eps(rr) == 0,
          'th:metabelian-residually-nilpotent, proof: v(a, c) = a^(1 + r) with sigma(v) = 1')
    # exc:lower-central-equations: Z^2 x| <t>, t acting by M of order 6
    M = matrix(ZZ, [[0, -1], [1, 1]])
    I2 = identity_matrix(ZZ, 2)
    check(M ** 6 == I2 and M ** 2 - M + I2 == 0 and (M - I2).det() == 1,
          'p. 29: M has order 6, M^2 - M + 1 = 0, M - 1 invertible over Z')
    # gamma_2 = A (M - 1) = A, hence gamma_n = A for n >= 2 and cap gamma_n = A = Z^2
    check((M - I2).inverse().base_ring() is QQ and all(c in ZZ for c in (M - I2).inverse().list()),
          'p. 29: [A, t] = A (M - 1) = A, so the intersection of the gamma_n is A = Z^2')
    R = PolynomialRing(QQ, 'u')
    check(R([1, -1, 1]).is_irreducible(), 'p. 29: Q[M] = Q(zeta_6) is a field')
    tr = [(M ** k - I2).trace() for k in range(6)]
    check(all(t <= 0 for t in tr) and tr[0] == 0,
          'p. 29: tr(M^k - 1) <= 0 for all k, so tr(sum (M^(k_i) - 1)) <= 0 < 2 = tr(1): '
          'x(1 - s) = 0 forces x = 0 (traces %s)' % tr)
    # printed: x = prod [x, c_i] has only x = 1 -- check every multiset of exponents of length <= 6
    sols = 0
    for L in range(1, 7):
        for ks in itertools.combinations_with_replacement(range(6), L):
            S = sum((M ** k - I2 for k in ks), matrix(ZZ, 2, 2))
            if (I2 - S).det() == 0:
                sols += 1
    refuted(sols > 0, 'exc:lower-central-equations printed: some equation x = prod [x, c_i] '
            '(<= 6 factors) has a solution x != 1 in Z[zeta_6] x| Z')
    # corrected: x = [x, t]^(-1) [x, t^(-1)]^(-1) for all x
    ok = True
    for v in itertools.product(range(-4, 5), repeat=2):
        xv = vector(ZZ, v)
        c1 = xv * (M - I2)          # [x, t] = x^(t - 1)
        c2 = xv * (M.inverse() - I2)
        ok = ok and (-c1 - c2 == xv)
    check(ok, 'exc:lower-central-equations corrected: x = [x, t]^(-1) [x, t^(-1)]^(-1) on a box of Z^2')


# ---------------------------------------------------------------------------
# section 5
# ---------------------------------------------------------------------------

def section_5():
    for (T, A) in [mod_s3_f2(), mod_z4_on_z5()]:
        def mul(x, y):
            (g1, a1), (g2, a2) = x, y
            return (T.mul[g1][g2], A.add(A.act(a1, g2), a2))
        el = [(g, a) for g in range(T.n) for a in A.elts]
        check(all(mul(mul(x, y), z) == mul(x, mul(y, z)) for x in el for y in el for z in el[:12]),
              'p. 30: (g1, a1)(g2, a2) = (g1 g2, a1^(g2) a2) is associative (%s, %s)' % (T.name, A.name))
        check(all(mul(mul((T.inv[g], A.zero), (T.e, a)), (g, A.zero)) == (T.e, A.act(a, g))
                  for g in range(T.n) for a in A.elts),
              'p. 30: (g^-1, 1)(1, a)(g, 1) = (1, a^g) (%s)' % T.name)
    # exc:free-metabelian-derived: G = <s, t> = Z^2, A = ZG; x -> (s, 1), y -> (t, 0)
    from sage.all import LaurentPolynomialRing
    L = LaurentPolynomialRing(ZZ, 's,t')
    s, t = L.gens()
    # element (g, a) with g a monomial and a in ZG; (g1, a1)(g2, a2) = (g1 g2, a1 g2 + a2)

    def mul(x, y):
        return (x[0] * y[0], x[1] * y[0] + y[1])

    def inv(x):
        return (x[0] ** -1, -x[1] * x[0] ** -1)
    X, Y = (s, L(1)), (t, L(0))
    c = mul(mul(inv(X), inv(Y)), mul(X, Y))
    check(c[0] == 1 and c[1] == t - 1 and L.is_integral_domain(),
          'exc:free-metabelian-derived: [x, y] -> (1, t - 1) (formula (1.22)), non-zero in the domain ZG, G = Z^2 '
          '(so r [x, y] = 1 only for r = 0)')


# ---------------------------------------------------------------------------
# section 6
# ---------------------------------------------------------------------------

def section_6():
    for n in [k for k in range(-7, 8) if k]:
        X = matrix(QQ, [[1, 1, 0], [0, 1, 0], [0, 0, 1]])
        Y = matrix(QQ, [[1, 0, 0], [0, 1, 1], [0, 0, 1]])
        Z = matrix(QQ, [[1, 0, QQ(1) / n], [0, 1, 0], [0, 0, 1]])
        ok = X.inverse() * Y.inverse() * X * Y == Z ** n and X * Z == Z * X and Y * Z == Z * Y
        I3 = identity_matrix(QQ, 3)
        # Z = 1 + N with N^2 = 0, N != 0: Z^k = 1 + k N != 1 for k != 0
        check(ok and (Z - I3) ** 2 == 0 and Z != I3,
              'p. 32: matrices of G_%d: [X, Y] = Z^n, Z central, Z of infinite order' % n)
    for n in range(-8, 9):
        Fg = gap('FreeGroup(3)')
        x, y, z = Fg.GeneratorsOfGroup()
        rels = [x * z * x ** -1 * z ** -1, y * z * y ** -1 * z ** -1,
                x ** -1 * y ** -1 * x * y * z ** (-n)]
        Gn = Fg / rels
        ab = sorted(int(c) for c in Gn.AbelianInvariants())
        exp = sorted(int(c) for c in gap('AbelianInvariants(AbelianGroup([0, 0, %d]))' % abs(n)))
        check(ab == exp, 'p. 33: G_%d / G_%d\' = Z^2 + Z_%d, invariants %s (corrected '
              '"свободной абелевой"; n = 0: Z^3)' % (n, n, abs(n), ab))
    refuted(bool(gap('IsAbelian(FreeGroup(2))')),
            'p. 33 printed: the abelian group G_n / G_n\' is a direct product of a free group of rank 2 '
            'and Z_|n| (the free group of rank 2 is not abelian)')
    # f: G_n -> G_(-n), x -> x, y -> y, z -> z^(-1): relators go to 1 (matrices of G_(-n))
    for n in [1, 2, 3, -2, 5]:
        X = matrix(QQ, [[1, 1, 0], [0, 1, 0], [0, 0, 1]])
        Y = matrix(QQ, [[1, 0, 0], [0, 1, 1], [0, 0, 1]])
        Zm = matrix(QQ, [[1, 0, QQ(1) / (-n)], [0, 1, 0], [0, 0, 1]])
        Zi = Zm.inverse()
        ok = X * Zi == Zi * X and Y * Zi == Zi * Y and X.inverse() * Y.inverse() * X * Y == Zi ** n
        check(ok, 'p. 33: x_n -> x_(-n), y_n -> y_(-n), z_n -> z_(-n)^(-1) respects the relations, n = %d' % n)
        # corrections by central c, d do not change the commutator
        for (a, b) in [(1, 0), (2, -3), (0, 5)]:
            C, D = Zm ** a, Zm ** b
            Xc, Yd = X * C, Y * D
            check(Xc.inverse() * Yd.inverse() * Xc * Yd == Zm ** (-n),
                  'p. 33: [x_(-n) c, y_(-n) d] = z_(-n)^(-n), n = %d, c = z^%d, d = z^%d' % (n, a, b))
        # exc:generator-swap-isomorphism: x -> y_(-n), y -> x_(-n), z -> z_(-n)
        ok = X * Zm == Zm * X and Y.inverse() * X.inverse() * Y * X == Zm ** n
        check(ok, 'exc:generator-swap-isomorphism: x_n -> y_(-n), y_n -> x_(-n), z_n -> z_(-n) '
              'respects the relations, n = %d' % n)
    # factor systems of E_n: normal form x^a y^b z^c; y^b x^a' = x^a' y^b z^(-n a' b)
    R = PolynomialRing(ZZ, 'a,b,a1,b1,a2,b2,n,m')
    a, b, a1, b1, a2, b2, n, m = R.gens()

    def h(nn, u, v):
        return -nn * v[0] * u[1]
    # cocycle identity for the trivial module (polynomial identity)
    u, v, w = (a, b), (a1, b1), (a2, b2)

    def add(p, q):
        return (p[0] + q[0], p[1] + q[1])
    coc = h(n, u, v) - h(n, u, add(v, w)) + h(n, add(u, v), w) - h(n, v, w)
    check(coc == 0, 'p. 33: h_n((a,b),(a\',b\')) = -n a\' b is a 2-cocycle of Z^2 (polynomial identity)')
    check(h(n, u, v) + h(m, u, v) == h(n + m, u, v),
          'p. 33: factor systems add: E_n + E_m = E_(n+m)')
    alt = h(n, u, v) - h(n, v, u)
    check(alt == n * (a * b1 - a1 * b),
          'p. 33: h_n(g1, g2) - h_n(g2, g1) = n (a b\' - a\' b), bilinear alternating, '
          'non-zero for n != 0 while coboundaries are symmetric')
    # matrices realise the normal form: X^a Y^b X^a' Y^b' = X^(a+a') Y^(b+b') Z^(h)
    for nn in [1, 2, -3]:
        X = matrix(QQ, [[1, 1, 0], [0, 1, 0], [0, 0, 1]])
        Y = matrix(QQ, [[1, 0, 0], [0, 1, 1], [0, 0, 1]])
        Z = matrix(QQ, [[1, 0, QQ(1) / nn], [0, 1, 0], [0, 0, 1]])
        ok = all(X ** p * Y ** q * X ** p1 * Y ** q1 ==
                 X ** (p + p1) * Y ** (q + q1) * Z ** (-nn * p1 * q)
                 for p in range(-2, 3) for q in range(-2, 3)
                 for p1 in range(-2, 3) for q1 in range(-2, 3))
        check(ok, 'p. 33: factor system of E_%d in the matrices of G_%d' % (nn, nn))
    # exc:central-extensions-of-free-abelian: H^2(Z^2, Z) = Z from the
    # cubical torus, a K(Z^2, 1)
    H2 = cubical_complexes.Torus().cohomology(2, base_ring=ZZ)
    check(H2.ngens() == 1 and H2.invariants() == (0,),
          'exc:central-extensions-of-free-abelian: H^2(Z^2, Z) = Z (torus)')
    # exc:cyclic-p-extensions, exc:weak-equivalence
    for p in [2, 3, 5]:
        T = cyclic(p)
        A = trivial(T, p)
        check(h_order(A, 2) == p, 'exc:cyclic-p-extensions: |H^2(Z_%d, Z_%d)| = %d' % (p, p, p))
        g = T.gens[0]
        # cocycles h_c(g^i, g^j) = c [i + j >= p] represent the classes
        ids = []
        for c in range(p):
            h = {}
            for i in range(p):
                for j in range(p):
                    h[(T.power(g, i), T.power(g, j))] = (c if i + j >= p else 0,)
            assert cocycle_ok(A, h)
            E = Ext(A, h)
            ids.append(tuple(int(x) for x in gap('IdGroup')(E.P)))
        cyc = tuple(int(x) for x in gap('IdGroup(CyclicGroup(%d))' % (p * p)))
        el = tuple(int(x) for x in gap('IdGroup(ElementaryAbelianGroup(%d))' % (p * p)))
        check(ids[0] == el and all(t == cyc for t in ids[1:]),
              'exc:cyclic-p-extensions: class 0 gives Z_%d^2, the %d others Z_%d' % (p, p - 1, p * p))
        # the classes c are distinct: h_c - h_c' not a coboundary (the extension groups differ
        # for c = 0; for c != c' use the coboundary space)
        B = set()
        for vals in itertools.product(range(p), repeat=p):
            B.add(tuple((vals[i] - vals[(i + j) % p] + vals[j]) % p for i in range(p) for j in range(p)))
        reps = [tuple(c if i + j >= p else 0 for i in range(p) for j in range(p)) for c in range(p)]
        distinct = all(tuple((x - y) % p for x, y in zip(reps[c1], reps[c2])) not in B
                       for c1 in range(p) for c2 in range(p) if c1 != c2)
        check(distinct, 'exc:cyclic-p-extensions: the p cocycles h_c are pairwise not cohomologous (p = %d)' % p)
        orbits = set()
        for c in range(p):
            orbits.add(frozenset((u * c) % p for u in range(1, p)))
        check(len(orbits) == 2, 'exc:weak-equivalence: Aut(Z_%d) has 2 orbits on H^2(Z_%d, Z_%d)' % (p, p, p))


# ---------------------------------------------------------------------------
# section 7
# ---------------------------------------------------------------------------

def coboundary_cocycle(A, phi):
    T = A.T
    return {(a, b): A.add(A.sub(A.act(phi[a], b), phi[T.mul[a][b]]), phi[b])
            for a in range(T.n) for b in range(T.n)}


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


def examples_7():
    """(T, A, h) extensions for the checks of §§ 7, 10."""
    out = []
    for (o, i) in [(2, 1), (3, 1), (4, 1), (4, 2), (6, 1)]:
        T = small(o, i)
        for p in [2, 3]:
            A = trivial(T, p)
            for h in h2_reps(A)[:2]:
                out.append((T, A, h))
    T, A = mod_s3_f2()
    out.append((T, A, zero_cocycle(A)))
    T = cyclic(2)
    A = Mod(T, 4, 1, lambda h: [[1 if h == T.e else -1]], 'Z_4, inversion')
    for h in h2_reps_bruteforce(A):
        out.append((T, A, h))
    T = small(8, 3)
    A = trivial(T, 2)
    out.append((T, A, h2_reps(A)[3]))
    return out


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


def aut_e(E):
    """Aut E: automorphisms x -> x u with u in A on the generators of G,
    identity on A (GAP decides which choices extend)."""
    T, A = E.T, E.A
    auts = []
    for us in itertools.product(A.elts, repeat=len(T.gens)):
        imgs = [E.mul((g, A.zero), (T.e, u)) for g, u in zip(T.gens, us)]
        hom = endo_images(E, imgs, lambda b: b)
        if hom != gap('fail') and bool(hom.IsBijective()):
            auts.append(hom)
    return auts


def section_7():
    exs = examples_7()
    check(len(exs) >= 16, 'section 7: %d extensions' % len(exs))
    for (T, A, h) in exs:
        E = Ext(A, h)
        auts = aut_e(E)
        der = z1_list(A)
        check(len(auts) == len(der),
              'prop:automorphisms-derivations: |Aut E| = |Der(G, A)| = %d (%s, %s)'
              % (len(der), T.name, A.name))
        if auts:
            Aut = libgap.Group(auts) if len(auts) > 0 else None
            check(bool(Aut.IsAbelian()) and int(Aut.Size()) == len(auts),
                  'sec:automorphisms: Aut E is an abelian group (%s, %s)' % (T.name, A.name))
        # inner automorphisms by A <-> principal derivations a(1 - g)
        princ = set(tuple(A.sub(a, A.act(a, g)) for g in range(T.n)) for a in A.elts)
        fixed = [a for a in A.elts if all(A.act(a, g) == a for g in range(T.n))]
        check(len(princ) == len(A.elts) // len(fixed) and
              all(tuple(d[g] for g in range(T.n)) in set(tuple(dd[g] for g in range(T.n)) for dd in der)
                  for d in [{g: x[g] for g in range(T.n)} for x in princ]),
              'prop:automorphisms-derivations: |Inn E| = |B^1| = |A / A^G| = %d (%s, %s)'
              % (len(princ), T.name, A.name))
        check(len(der) // len(princ) == h_order(A, 1),
              'sec:automorphisms: |Aut E / Inn E| = |H^1(G, A)| (%s, %s)' % (T.name, A.name))
        # the inner automorphism by a: g-bar -> a^(-1) g-bar a = g-bar a^(1 - g)
        ok = True
        for a in A.elts:
            ainv = (T.e, A.sub(A.zero, a))
            ael = (T.e, a)
            for g in range(T.n):
                x = (g, A.zero)
                y = E.mul(E.mul(ainv, x), ael)
                ok = ok and y == E.mul(x, (T.e, A.sub(a, A.act(a, g))))
        check(ok, 'p. 34: a^(-1) g-bar a = g-bar a^(1 - g) (%s, %s)' % (T.name, A.name))
        # phi(r t) = phi(r) t + eps(r) phi(t) on ZG and principal phi(r) = a(eps(r) - r)
        for d in der[:3]:
            def phis(r):
                out = A.zero
                for g, c in enumerate(r):
                    out = A.add(out, A.smul(c, d[g]))
                return out
            for _ in range(5):
                r = [random.randint(-2, 2) for _ in range(T.n)]
                t = [random.randint(-2, 2) for _ in range(T.n)]
                lhs = phis(zg_mul(T, r, t))
                rhs = A.add(A.actr(phis(r), t), A.smul(eps(r), phis(t)))
                check(lhs == rhs, 'p. 37: phi(r t) = phi(r) t + eps(r) phi(t) (%s, %s)' % (T.name, A.name))
        if T.n <= 6:
            a = A.elts[-1]
            r = [random.randint(-3, 3) for _ in range(T.n)]
            val = A.zero
            for g, c in enumerate(r):
                val = A.add(val, A.smul(c, A.sub(a, A.act(a, g))))
            check(val == A.sub(A.smul(eps(r), a), A.actr(a, r)),
                  'p. 37: the principal derivation extends as phi(r) = a(eps(r) - r)')
        # prop:h1-finite-exponent: n phi is principal with a = phi(n - sigma)
        n = T.n
        for d in der:
            a = A.zero
            for g in range(T.n):
                a = A.sub(a, d[g])          # phi(n - sigma) = -sum phi(g) (phi(1) = 0)
            # n phi(g - 1) = a (g - 1) for r = g - 1 in Delta
            ok2 = all(A.smul(n, d[g]) == A.sub(A.act(a, g), a) for g in range(T.n))
            check(ok2, 'prop:h1-finite-exponent: n phi(r) = a r with a = phi(n - sigma) (%s, %s)'
                  % (T.name, A.name))
        if all(all(A.act(a, g) == a for a in A.basis()) for g in range(T.n)):
            # cor:central-extension-automorphisms: |Aut E| = |Hom(G_ab, A)|
            hom = 0
            for vals in itertools.product(A.elts, repeat=len(T.gens)):
                # homomorphisms G -> A by brute force
                f = {T.e: A.zero}
                fr = [T.e]
                ok = True
                while fr and ok:
                    new = []
                    for g in fr:
                        for s, v in zip(T.gens, vals):
                            hh = T.mul[g][s]
                            val = A.add(f[g], v)
                            if hh in f:
                                ok = ok and f[hh] == val
                            else:
                                f[hh] = val
                                new.append(hh)
                    fr = new
                if ok and len(f) == T.n and all(f[T.mul[x][y]] == A.add(f[x], f[y])
                                                for x in range(T.n) for y in range(T.n)):
                    hom += 1
            check(hom == len(auts), 'cor:central-extension-automorphisms: |Aut E| = |Hom(G_ab, A)| = %d (%s)'
                  % (hom, T.name))
    # prop:coinduced-kernel-automorphisms: H^1(G, Hom(ZG, A)) = 0; Hom(ZG, A) = A^G with
    # (f g)(h) = f(g h): coordinates indexed by h, f g has coordinate h equal to f(g h)
    for (o, i) in [(2, 1), (3, 1), (4, 2), (6, 1), (8, 3)]:
        T = small(o, i)
        for p in [2, 3]:
            # matrix of f -> f g: new[h] = old[g h], so entry (g h, h) = 1
            A = Mod(T, p, T.n, lambda g: [[1 if j == T.mul[g][hh] else 0 for hh in range(T.n)]
                                          for j in range(T.n)], 'Hom(ZG, F_%d)' % p)
            check(h_order(A, 1) == 1,
                  'prop:coinduced-kernel-automorphisms: H^1(%s, Hom(ZG, F_%d)) = 0' % (T.name, p))
            # the proof: alpha(g) = phi(g)(1), then phi(g) = -alpha o (1 - g)
            F = GF(p)
            D1 = delta_matrix(A, 1, F)
            Z = D1.right_kernel().basis_matrix()
            ok = True
            for z in Z.rows()[:6]:
                phi = {g: [z[g * T.n + hh] for hh in range(T.n)] for g in range(T.n)}
                alpha = [phi[g][T.e] for g in range(T.n)]
                for g in range(T.n):
                    for g1 in range(T.n):
                        lhs = alpha[g1] - alpha[T.mul[g][g1]]       # (alpha o (1 - g))(g')
                        ok = ok and lhs == -phi[g][g1]
            check(ok, 'prop:coinduced-kernel-automorphisms, proof: (alpha o (1 - g))(g\') = '
                  '-phi(g)(g\') with alpha(g) = phi(g)(1) (%s, F_%d)' % (T.name, p))
    # cor:zassenhaus examples: H^1 = 0 when division by n is possible
    T2 = cyclic(2)
    zass = [mod_z4_on_z5(),
            (T2, Mod(T2, 3, 1, lambda g: [[1 if g == T2.e else -1]], 'Z_3, inversion')),
            (small(6, 1), trivial(small(6, 1), 5)),
            (small(6, 1), Mod(small(6, 1), 7, 2, lambda g: identity_matrix(ZZ, 2).rows(), 'trivial Z_7^2'))]
    for (T, A) in zass:
        check(h_order(A, 1) == 1, 'cor:zassenhaus: H^1(%s, %s) = 0 (|G| invertible on A)' % (T.name, A.name))
    # th:coprime-complements-conjugate: groups of order <= 200 with a normal Hall subgroup
    fun = gap('''function(o)
      local res, i, G, N, c;
      res := [0, 0];
      for i in [1..NumberSmallGroups(o)] do
        G := SmallGroup(o, i);
        for N in NormalSubgroups(G) do
          if Size(N) > 1 and Size(N) < o and Gcd(Size(N), o / Size(N)) = 1 then
            c := ComplementClassesRepresentatives(G, N);
            res[1] := res[1] + 1;
            if Length(c) = 1 then res[2] := res[2] + 1; fi;
          fi;
        od;
      od;
      return res;
    end''')
    tot = [0, 0]
    for o in range(2, 201):
        if o in (128, 192):
            continue
        r = fun(o).sage()
        tot[0] += r[0]
        tot[1] += r[1]
    check(tot[0] == tot[1] and tot[0] > 1000,
          'th:coprime-complements-conjugate (and th:schur): all %d pairs (G, N), |G| <= 200 '
          '(orders 128, 192 skipped), N a normal Hall subgroup: exactly one class of complements' % tot[0])
    # exc:centralizer-quotient and exc:extension-automorphisms-abelian (non-abelian kernels too)
    fun2 = gap('''function(G)
      local res, N, A, C, auts, aut, sub;
      res := [0, 0, 0];
      A := AutomorphismGroup(G);
      for N in NormalSubgroups(G) do
        if Size(N) > 1 and Size(N) < Size(G) then
          C := Centralizer(G, N);
          sub := Filtered(AsList(A), f -> ForAll(GeneratorsOfGroup(N), x -> Image(f, x) = x));
          res[1] := res[1] + 1;
          if ForAll(sub, f -> ForAll(GeneratorsOfGroup(G), g -> Image(f, g) / g in C)) then
            res[2] := res[2] + 1; fi;
          sub := Filtered(sub, f -> ForAll(GeneratorsOfGroup(G), g -> Image(f, g) / g in N));
          if IsAbelian(Group(Concatenation([IdentityMapping(G)], sub))) then res[3] := res[3] + 1; fi;
        fi;
      od;
      return res;
    end''')
    tot = [0, 0, 0]
    for o in range(4, 25):
        for i in range(1, int(gap('NumberSmallGroups(%d)' % o)) + 1):
            if int(gap('Size(AutomorphismGroup(SmallGroup(%d,%d)))' % (o, i))) > 2000:
                continue
            r = fun2(gap('SmallGroup(%d,%d)' % (o, i))).sage()
            tot = [x + y for x, y in zip(tot, r)]
    check(tot[0] == tot[1], 'exc:centralizer-quotient: %d pairs (G, A), |G| <= 24: automorphisms '
          'fixing A act trivially on G / C(A)' % tot[0])
    check(tot[0] == tot[2], 'exc:extension-automorphisms-abelian: Aut E abelian for all %d '
          'extensions (normal subgroups of groups of order <= 24, |Aut G| <= 2000)' % tot[0])
    # exc:series-stability-group: groups acting trivially on the factors of a normal series
    fun3 = gap('''function(G, S)
      local A, sub, k;
      A := AutomorphismGroup(G);
      sub := Filtered(AsList(A), f -> ForAll([1..Length(S)-1], k ->
               ForAll(GeneratorsOfGroup(S[k]), g -> Image(f, g) / g in S[k+1])));
      return NilpotencyClassOfGroup(Group(Concatenation([IdentityMapping(G)], sub)));
    end''')
    desc = gap('''function(S)
      local T, x;
      T := [];
      for x in S do if ForAll(T, y -> Size(y) <> Size(x)) then Add(T, x); fi; od;
      SortBy(T, x -> -Size(x));
      return T;
    end''')
    nser = 0
    for (o, i) in [(8, 1), (8, 2), (8, 3), (8, 4), (8, 5), (16, 2), (16, 3), (16, 6), (27, 3), (9, 2),
                   (27, 5)]:
        G = gap('SmallGroup(%d,%d)' % (o, i))
        if int(G.AutomorphismGroup().Size()) > 20000:
            continue
        for S in [G.LowerCentralSeriesOfGroup(), G.UpperCentralSeriesOfGroup(), G.ChiefSeries(),
                  G.DerivedSeriesOfGroup()]:
            S = list(desc(S))
            if len(S) < 2:
                continue
            assert int(S[0].Size()) == o and int(S[-1].Size()) == 1
            assert all(bool(gap('IsNormal')(G, X)) for X in S)
            nfac = len(S) - 1         # S: G = G_0 > ... > G_n > G_(n+1) = 1, n + 1 factors
            c = int(fun3(G, S))
            check(c <= nfac - 1, 'exc:series-stability-group: class %d <= n = %d for a normal series '
                  'of SmallGroup(%d,%d)' % (c, nfac - 1, o, i))
            nser += 1
    check(nser >= 20, 'exc:series-stability-group: %d series' % nser)
    # exc:torsion-free-kernel: additive torsion-freeness is not enough: G-bar = Z x Z_3, A = Z,
    # f = id x (inversion) fixes A and is not the identity on G = Z_3
    def f(x):
        return (x[0], (-x[1]) % 3)
    box = [(k, j) for k in range(-3, 4) for j in range(3)]
    ok = all(f(((x[0] + y[0]), (x[1] + y[1]) % 3)) == ((f(x)[0] + f(y)[0]), (f(x)[1] + f(y)[1]) % 3)
             for x in box for y in box)
    refuted(not (ok and all(f((k, 0)) == (k, 0) for k in range(-3, 4)) and f((0, 1)) != (0, 1)),
            'exc:torsion-free-kernel read with additive torsion-freeness: Z x Z_3, f = id x (-1)')
    # exc:automorphisms-over-quotient: split extensions, |Aut_G G-bar| = |Aut E| |Aut_G A|
    for (T, A) in [mod_s3_f2(), mod_z4_on_z5()]:
        E = Ext(A, zero_cocycle(A))
        der = z1_list(A)
        # Aut_G A: module automorphisms
        modaut = 0
        for M in itertools.product(range(A.m), repeat=A.k * A.k):
            Mm = [list(M[r * A.k:(r + 1) * A.k]) for r in range(A.k)]
            def fa(a, Mm=Mm):
                return tuple(sum(a[j] * Mm[j][i] for j in range(A.k)) % A.m for i in range(A.k))
            if len(set(fa(a) for a in A.elts)) != len(A.elts):
                continue
            if all(fa(A.act(a, g)) == A.act(fa(a), g) for a in A.basis() for g in range(T.n)):
                modaut += 1
        # Aut_G G-bar: automorphisms of G-bar inducing identity on G-bar / A
        Agap = gap('AutomorphismGroup')(E.P)
        Nn = libgap.Group([E.p((T.e, a)) for a in A.basis()])
        cnt = 0
        for fgap in Agap.AsList():
            if all(bool(GIN(fgap.Image(E.p((g, A.zero))) * E.p((g, A.zero)) ** -1, Nn)) for g in T.gens) and \
               bool(fgap.Image(Nn) == Nn):
                cnt += 1
        check(cnt == len(der) * modaut,
              'exc:automorphisms-over-quotient: |Aut_G G-bar| = |Aut E| |Aut_G A| = %d * %d (%s, %s)'
              % (len(der), modaut, T.name, A.name))
    # exc:induced-automorphism-of-h1: alpha_x(y) = x^(-1) y x; alpha_x^* phi = phi - phi_a, a = phi(x)
    for (T, A) in [mod_s3_f2(), mod_z4_on_z5()]:
        for d in z1_list(A):
            for x in range(T.n):
                a = d[x]
                new = {g: A.act(d[T.mul[T.mul[x][g]][T.inv[x]]], x) for g in range(T.n)}
                ok = all(new[g] == A.sub(d[g], A.sub(a, A.act(a, g))) for g in range(T.n))
                check(ok, 'exc:induced-automorphism-of-h1: alpha_x^* phi = phi - phi_a, a = phi(x) '
                      '(%s, %s)' % (T.name, A.name))
    # exc:inversion-action: H^1(Z_2, A) = A / 2A for A with inversion
    T = cyclic(2)
    for mods in [[2], [3], [4], [6], [8], [9], [2, 4], [3, 3], [2, 2, 2]]:
        # A = prod Z_m_i as Z_L^k with L = lcm, realised as a subgroup: use brute force on the product
        L = 1
        for m in mods:
            L = L * m // gcd(L, m)
        elts = list(itertools.product(*[range(m) for m in mods]))

        def act(a, g):
            return a if g == T.e else tuple((-x) % m for x, m in zip(a, mods))
        der = 0
        for v in elts:
            phi = {T.e: tuple(0 for _ in mods), T.gens[0]: v}
            if all(phi[T.mul[g][h]] == tuple((x + y) % m for x, y, m in zip(act(phi[g], h), phi[h], mods))
                   for g in range(T.n) for h in range(T.n)):
                der += 1
        princ = len(set(tuple((x - y) % m for x, y, m in zip(a, act(a, T.gens[0]), mods)) for a in elts))
        twoA = len(set(tuple((2 * x) % m for x, m in zip(a, mods)) for a in elts))
        check(der // princ == len(elts) // twoA,
              'exc:inversion-action: |H^1(Z_2, A)| = |A / 2A| = %d for A = %s' % (der // princ, mods))
    # exc:cyclic-quotient: Der = {a : a N = 0} via phi -> phi(g), Inn <-> A(1 - g)
    ncq = 0
    for n in [2, 3, 4, 5, 6]:
        T = cyclic(n)
        g = T.gens[0]
        for (m, mult) in [(2, 1), (3, 1), (4, 1), (5, 1), (7, 2), (7, 3), (9, 4), (13, 5)]:
            if pow(mult, n, m) != 1 % m:
                continue
            mats = {T.power(g, k): [[pow(mult, k, m)]] for k in range(n)}
            A = Mod(T, m, 1, lambda h: mats[h], 'Z_%d, g -> %d' % (m, mult))
            der = z1_list(A)
            Nn = [1] * T.n
            kerN = [a for a in A.elts if A.actr(a, Nn) == A.zero]
            vals = sorted(d[g] for d in der)
            check(vals == sorted(kerN), 'exc:cyclic-quotient: phi -> phi(g) is a bijection Der -> '
                  '{a : a N = 0} (Z_%d, %s)' % (n, A.name))
            imA = set(A.sub(a, A.act(a, g)) for a in A.elts)
            princ_vals = set(A.sub(a, A.act(a, g)) for a in A.elts)
            check(imA == princ_vals and len(der) // len(imA) == h_order(A, 1),
                  'exc:cyclic-quotient: Inn E = A(1 - g), H^1 = Ker N / A(1 - g) (Z_%d, %s)' % (n, A.name))
            ncq += 1
    check(ncq >= 12, 'exc:cyclic-quotient: %d modules' % ncq)
    # Galois cohomology of finite fields
    fields = [(2, n) for n in range(1, 11)] + [(3, n) for n in range(1, 7)] + \
             [(5, n) for n in range(1, 5)] + [(7, n) for n in range(1, 4)] + [(11, 2), (13, 2)]
    for (p, n) in fields:
        K = GF(p ** n, 'z')
        Tr = {a: sum(a ** (p ** i) for i in range(n)) for a in K}
        ker = set(a for a in K if Tr[a] == 0)
        im = set(a - a ** p for a in K)
        check(all(Tr[a] in GF(p) for a in K) and ker == im,
              'exc:trace-kernel: Ker T = {a - a^p} in GF(%d^%d) (p %s n)'
              % (p, n, '|' if n % p == 0 else 'coprime to'))
        Nm = {a: prod(a ** (p ** i) for i in range(n)) for a in K if a != 0}
        kerN = set(a for a in Nm if Nm[a] == 1)
        imN = set(a ** (1 - p) for a in Nm)
        check(kerN == imN, 'exc:norm-variant: Ker N = {a / a^p} in GF(%d^%d)' % (p, n))
    check(any(n % p == 0 and n > 1 for (p, n) in fields),
          'exc:trace-kernel: fields with p | n included (the hypothesis "p и n взаимно просты" is not needed)')
    # exc:additive-galois-cohomology: H^1(Gal, L^+) = 0 by brute force on derivations (small fields)
    for (p, n) in [(2, 2), (2, 3), (3, 2), (2, 4), (3, 3), (5, 2)]:
        K = GF(p ** n, 'z')
        els = list(K)
        G = list(range(n))           # g^i : a -> a^(p^i)

        def act(a, i):
            return a ** (p ** i)
        der, princ = 0, set()
        for vals in itertools.product(els, repeat=n - 1):
            phi = [K(0)] + list(vals)
            if all(phi[(i + j) % n] == act(phi[i], j) + phi[j] for i in G for j in G):
                der += 1
        for a in els:
            princ.add(tuple(a - act(a, i) for i in G))
        check(der == len(princ), 'exc:additive-galois-cohomology: H^1(Gal(GF(%d^%d)/GF(%d)), L^+) = 0 '
              '(|Der| = |B^1| = %d)' % (p, n, p, der))
        # multiplicative: crossed homomorphisms f(gh) = f(g)^h f(h)
        nz = [a for a in els if a != 0]
        crossed, princm = [], set()
        for vals in itertools.product(nz, repeat=n - 1):
            f = [K(1)] + list(vals)
            if all(f[(i + j) % n] == act(f[i], j) * f[j] for i in G for j in G):
                crossed.append(f)
        for a in nz:
            princm.add(tuple(a / act(a, i) for i in G))
        check(len(crossed) == len(princm) and all(tuple(f) in princm for f in crossed),
              'exc:multiplicative-galois-cohomology: every crossed homomorphism into GF(%d^%d)^* is '
              'principal f(g) = a / a^g (%d of them)' % (p, n, len(crossed)))
        ok = True
        for f in crossed:
            some = False
            for x in els:
                a = sum(f[i] * act(x, i) for i in G)
                ok = ok and all(f[j] * act(a, j) == a for j in G)
                some = some or a != 0
            ok = ok and some
        check(ok, 'exc:multiplicative-galois-cohomology, hint: a = sum f(g_i) x^(g_i) satisfies '
              'f(g) a^g = a, and a != 0 for some x (GF(%d^%d))' % (p, n))
        # Artin's lemma (corrected chi_i: S -> L^*): the n automorphisms are independent on S = L^*
        Mx = matrix(K, [[act(a, i) for a in nz] for i in G])
        check(Mx.rank() == n, 'exc:multiplicative-galois-cohomology: the automorphisms of GF(%d^%d), '
              'as characters L^* -> L^*, are linearly independent over L' % (p, n))
    # exc:hilbert-90: GF(q^n) / GF(q) with q a prime power
    for (q, n) in [(4, 2), (4, 3), (8, 2), (9, 2), (2, 6), (3, 4), (4, 4), (16, 2), (27, 2), (25, 2)]:
        K = GF(q ** n, 'z')
        ker = set(a for a in K if sum(a ** (q ** i) for i in range(n)) == 0)
        im = set(a - a ** q for a in K)
        kerN = set(a for a in K if a != 0 and prod(a ** (q ** i) for i in range(n)) == 1)
        imN = set(a ** (1 - q) for a in K if a != 0)
        check(ker == im and kerN == imN,
              'exc:hilbert-90: Ker T = {a - a^q}, Ker N = {a^(1-q)} for GF(%d^%d) / GF(%d)' % (q, n, q))


def main():
    random.seed(20261105)
    section_1()
    section_2()
    section_3()
    section_4()
    section_5()
    section_6()
    section_7()
    print('ok %s: %d checks' % (SCOPE, COUNT[0]))


if __name__ == '__main__':
    main()
