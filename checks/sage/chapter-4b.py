"""Exact checks of Chapter 4 "Homology and the functor Tor", §§ 5-8 (Sage).

Run from the project root: sage -python checks/sage/chapter-4b.py (plain
asserts; do not use -O).  The last line is "ok chapter-4b: N checks".

Book: Yu. V. Kuzmin, Homological group theory (Factorial Press, Moscow,
2006), chapter 4, §§ 5-8, printed pp. 203-241; §§ 1-4 are checked in
chapter-4a.py.  Pages are printed pages; labels are those of
content/04-*.typ.  Expected values are the book's; where the book is wrong
the printed reading is kept as a refuted check (`refuted`) beside the
corrected one.  Exact arithmetic only: integer matrices and Sage's f.g.
modules over ZZ (Smith normal form), Laurent polynomials over ZZ, finite
fields GF(q) with matrices handled as lists (no dense matrix products over
finite fields), GAP through libgap (core library only: Schur multipliers,
Schur covers, finitely presented groups, matrix groups).

Finite groups are used through their multiplication tables.  For a free
group F mapping onto a finite group G the relation module M = N_ab
(N = Ker(F -> G)) is the cycle space of the Cayley graph of G, with basis
the fundamental cycles of a spanning tree, and conjugation by F acts on it
by left translations (`Cayley`); so N / [N, F] = M_G and
N' / [F, N'] = (M ^ M)_G (lem:relation-module-exterior-square) are
computed without the Magnus embedding.

What is checked, by section:

section_5 (pp. 203-213, H_2 and central extensions):
  * the kernel K of Delta (x)_G Delta -> Delta (s (x) t -> s t) has the
    invariants of GAP's Schur multiplier, and Delta (x)_G Delta = K + Z^(n-1),
    for all groups of order <= 16 and S_4, SL(2, 3), A_4 x Z_2
    (exc:h2-linearized-resolution, the exact sequence of p. 205);
  * exc:h2-free-abelian-basis on the finite analogues Z_m^2 (m = 2, 3, 4),
    Z_2^3, Z_2^4: the elements (x_i - 1) (x) (x_j - 1) - (x_j - 1) (x) (x_i - 1)
    (i < j) generate K = H_2;
  * exc:hopf-fox-isomorphism (Fox derivatives with the book's convention
    d(u v) = d(u) v + d(v), checked by the Fox identity on random words):
    for v in F' cap N the element h = sum (g_i - 1) (x) dv/dg_i lies in K,
    and for the listed v these h generate K (Z_2^2, Z_2^3, Z_4 x Z_2, D_8,
    Z_3^2, Q_8); with v in F' outside N (S_3, v = [x, y]) h is not in K:
    the printed condition "v in F'" refuted, the corrected "v in F' cap N"
    confirmed; the printed first factor x_i - 1 is not in Delta_G;
  * C348: the linear extension of the coboundary of a function phi is
    phi(s) t - phi(s t) + eps(s) phi(t) (random s, t in Z G, G = S_3, D_8,
    values in Z and in Z G); the printed eps(t) phi(s) refuted;
  * the extended cocycle identity of p. 203 for the cocycles (of sections
    that are not homomorphisms) of four extensions: Q_8 and Z_4 over their
    centres, Z_3 x| Z_4 over Z_3, A_4 over V_4, on random s, r, t in Z G;
    (4.23) f(s r, t) = f(s, r t) (s, t in Delta) holds for the central ones
    and fails for the two others;
  * prop:ext-extensions-description: for (G, B) = (S_3, Z_4), (A_4, Z_9),
    (D_8, Z_4 x Z_2), (Z_3 x| Z_4, Z_8), Gbar = {(g, b) : g G' = b A} has
    order |G| |A|, Gbar' maps onto G' isomorphically and Gbar_ab = B; the
    pairs (g, 1) in Gbar are exactly g in G' (C352; the printed "g in G"
    refuted);
  * prop:standard-central-extension: for the presentation with free
    generators x_g (g != 1) the kernel N / [F, N] has the invariants of
    Delta (x)_G Delta (all groups of order <= 8);
  * prop:perfect-universal-criterion: for A_5, PSL(2, 7), PSL(2, 8) GAP's
    Schur cover is perfect, has trivial multiplier and
    order |G| |H_2 G|; prop:perfect-central-preimage: for the perfect
    group SL(2, 9) (non-trivial centre, H_2 = Z_3) the preimage of
    the centre in the Schur cover is central;
  * exc:burnside-lemma: in all groups of order 16 and 27, 300 random tuples
    whose images generate G_ab generate G.
section_6 (pp. 213-223, knotted surface groups):
  * the Wirtinger presentation of the trefoil (p. 216): all generators are
    conjugate, G_ab = Z, eliminating z gives the relator x y x (y x y)^(-1)
    twice (up to cyclic permutation and inversion), whose exponent sums are
    not both 0 (H_2 = 0 by p. 195), Alexander polynomial t^2 - t + 1 (Fox
    calculus); the trefoil of our Рис. 2 (the heights of the points in
    content/diagrams/04-06-knotted-surface-groups.typ): three crossings,
    alternating, and its Wirtinger group has Alexander polynomial
    t^2 - t + 1 and G_ab = Z;
  * the 2-knot group <x, y | x^(-1) y x = y^(-1), y^3> (p. 217): y has order
    3, G_ab = Z, G is the normal closure of x, H_2 G = 0 from the HNN
    sequence (x acts on H_1 <y> = Z_3 by -1);
  * the inequality d (d - 1) / 2 <= d iff d <= 3 (p. 217), and groups
    Z^n x|_A Z (n = 3..6, A a companion matrix with det(A - 1) = +-1 and
    det(Lambda^2 A - 1) = +-1, found by search) with conditions 1-3 and
    commutator Z^n (for n = 2 impossible: Lambda^2 Z^2 = Z, H_2 != 0);
  * (4.32) and exm:gn-irreducible: for G_n, n = 2..12: G_n / G_n' = Z (GAP),
    G_n is the normal closure of g (GAP), g - 1 has the printed matrix and
    det 1 on M = Z_n^2, acts on M ^ M by -2, C(g) = <g> (no fixed points
    of g on M), H_2 G_n = Z_n / 2 Z_n: an irreducible C-group exactly for
    odd n (C372: the question is about G_n);
  * exc:simple-group-direct-product: for N = Z_p (p = 2, 3, 5, 7) the group
    Z x N has G_ab = Z + Z_p, not an irreducible C-group (printed "simple"
    refuted); for N = A_5, PSL(2, 7), PSL(2, 8) the Schur
    cover Nhat is perfect with trivial multiplier (so H_2(Z x Nhat) = 0),
    and for a non-central x the conjugates of t x generate Z x Nhat.
section_7 (pp. 223-230, irreducible C-groups):
  * cor:derived-quotient-not-even-cyclic: no unit u of Z_n with u - 1 a unit
    for even n <= 60 (u = 2 works for odd n);
  * exc:semidirect-eigenvalue-criterion: for all A in GL_2(p), p = 2, 3, 5,
    all A in GL_3(2), and 150 random A in GL_3(3): the eigenvalue condition
    (lambda_i != 1, lambda_i lambda_j != 1, i != j, over the splitting field)
    holds iff det(A - 1) != 0 and det(Lambda^2 A - 1) != 0, i.e. iff
    G_ab = Z and H_2 = 0 for <g> M (th:metabelian-irreducible-c-groups);
  * prop:psl-irreducible-c-group: for all (n, q) with 2 <= n <= 6 and
    q <= 32 (q a prime power, (n, q) not one of the seven exceptions) the
    construction of the proof: y in SL(n, q); w = diag(a^(n-1), ..., 1)
    satisfies y w = a w y; the determinants det w (n odd, char 2, m even,
    m odd), det(b w) = 1 for l even; for l odd a is not a square; the
    negacyclic matrices commute with y; for m = 1 the eigenvectors u_k, the
    corrected v_k, w_k (C383) and the 2 x 2 blocks (alpha_k, beta_k;
    b_k^2 beta_k, alpha_k) with the corrected beta_k (C384), det c as the
    product of alpha_k^2 - b_k^2 beta_k^2, the invertibility of
    (c_i) -> (alpha_k, beta_k); for m odd det(c) = det(c')^m; finally a
    matrix w' with det w' = 1 and y w' = a w' y; the forms x_1^2 + e x_2^2
    (e != 0) take all values of F_q (odd q <= 49), the squares with 0 are
    not closed under addition, and x_1^2 + x_2^2 is a non-zero non-square
    for some pair (the corrected reading of p. 229); for q = 1 mod 4 the
    value 0 also occurs at a pair (x_1, x_2) != 0, so "not in (F_q^*)^2"
    alone does not give a non-square (printed reading);
    in GAP: AbelianInvariantsMultiplier(PSL(n, q)) = Z_d for 9 small
    non-exceptional (n, q) and differs from Z_d for the five exceptions with
    PSL simple, and for (n, q) = (2, 5), (2, 7), (2, 11), (2, 13), (2, 17),
    (3, 7), (4, 3) the commutators [y, w] with w in the preimage of C_N(x)
    generate the centre of SL(n, q);
  * exc:c-direct-product-derived (C386): G = <w, a | w^(-1) a w = a^(-1),
    a^3>, X = {w, w a, w a^2}; G x_C G given by the corrected relations has
    (modulo the central t^k, t = (w, w), k = 6, 12) derived subgroup of
    order 27, non-abelian of class 2 (Heisenberg group mod 3), while
    G' x G' has order 9.
section_8 (pp. 231-241, F / [F, N']):
  * th:free-central-torsion-orders on finite groups: the torsion of
    (M ^ M)_G = N' / [F, N'] has exponent dividing 4 for all groups of order
    <= 12 (two generators) and nine groups with three generators; for groups
    of odd order it is 0 (cor:periodic-part-without-involutions,
    exc:odd-order-torsion-free);
  * prop:order-four-element and prop:squares-commutator-identity in the
    Cayley model of G = Z_2^2 = F / N, N = <<x^2, y^2, [x, y]>>: the class
    of [x, y] ^ y^2 has order exactly 4;
  * the computation of prop:squares-commutator-identity with the Magnus
    embedding: (P ^ P)_G = Z^4 + Z_2^6, the first summand of
    nu((s ^ t) (x) 1) is 0, the second equals the corrected
    (e_2 ^ e_2 a b + e_2 a ^ e_2 - e_2 ^ e_2 b) (x) 1 and not
    +-(e_2 ^ e_2 a b) (x) 1 (C398, printed reading refuted), nu((s ^ t) (x) 1)
    has order 2; prop:order-four-element: (I ^ I)_G = Z_4 generated by c_1,
    the relations c_2 = 2 c_1, c_3 = -c_1, c_2 = 2 c_3, and f(s ^ t) = -c_1
    (C402, printed +c_1 refuted only as a sign: both have order 4);
  * lem:exterior-involution-order-two on Z H (H = Z_2, Z_2^2, S_3, D_8),
    every m of a small box and every involution c;
  * exc:exterior-square-free-cyclic, exc:exterior-square-coinvariants:
    (P ^ P)_G = Z^f + Z_2^(r i) with basis (e_j ^ e_j g) (x) 1 of the
    2-part (i the number of involutions), r = 1, 2, eight groups;
    lem:symmetric-square-free-cyclic: (R o R)_G is free of rank
    1 + (|G| - 1 - i) / 2 + i, the number of orbits of G on the unordered
    pairs {g, h} (the stabilizer is <g^-1 h> when (g^-1 h)^2 = 1);
    lem:augmentation-symmetric-square-homology: 0 -> Delta o Delta ->
    R o R -> R -> Z_2 -> 0 is exact (image Delta + 2 Z) for six groups.

What this does NOT establish: the general theorems (only the listed groups,
fields, ranks and degrees are covered); nothing about knots beyond the two
presentations and the figure's crossing data, about Kervaire's and Gordon's
theorems, about the claims of pp. 235-237 on the free centre-by-metabelian
group (Gupta's word) or the results of Stöhr; th:free-central-torsion-orders
only for the listed finite groups, where the torsion is computed but not
compared with H_4(G, Z_2) for groups with involutions.  Nothing here
compares our text with the printed book.
"""

import itertools
import random
import re

from sage.all import (
    GF, QQ, ZZ, LaurentPolynomialRing, PolynomialRing, gcd, identity_matrix,
    libgap, matrix, vector, zero_matrix,
)

SCOPE = 'chapter-4b'
COUNT = [0]


def check(cond, what):
    assert bool(cond), 'FAILED: ' + what
    COUNT[0] += 1


def refuted(cond, what):
    assert not bool(cond), 'printed reading unexpectedly holds: ' + what
    COUNT[0] += 1


def gap(src):
    return libgap.eval(src)


def canon(invs):
    out = []
    for d in invs:
        d = abs(ZZ(d))
        if d == 0:
            out.append(0)
        elif d > 1:
            out.extend(p ** e for p, e in d.factor())
    return sorted(out)


def gap_invariants(G):
    return canon([ZZ(x) for x in G.AbelianInvariants()])


def quotient_invariants(dim, rels):
    V = ZZ ** dim
    return canon((V / V.submodule(rels)).invariants())


class FinGroup:
    """A finite group from GAP with its multiplication table."""

    def __init__(self, G):
        if not bool(libgap.IsPermGroup(G)):
            G = libgap.Image(libgap.IsomorphismPermGroup(G))
        self.G = G
        self.elts = libgap.AsList(G)
        self.n = len(self.elts)
        tab = gap('function(e) return List(e, g -> List(e, h -> '
                  'Position(e, g * h))); end')(self.elts)
        self.mul = [[int(x) - 1 for x in row] for row in tab]
        self.one = [i for i in range(self.n)
                    if all(self.mul[i][j] == j for j in range(self.n))][0]
        self.inv = [[j for j in range(self.n) if self.mul[i][j] == self.one][0]
                    for i in range(self.n)]
        self.gens = [self.index(g) for g in libgap.GeneratorsOfGroup(G)]

    def index(self, g):
        return int(libgap.Position(self.elts, g)) - 1

    def involutions(self):
        return [g for g in range(self.n) if g != self.one and self.mul[g][g] == self.one]


# ---------------------------------------------------------------------------
# Section 5: H_2 and central extensions (pp. 203-213)
# ---------------------------------------------------------------------------

class DeltaTensor:
    """Delta (x)_G Delta with the Z-basis u_g (x) u_h (u_g = g - 1, g != 1)."""

    def __init__(self, FG):
        self.FG = FG
        n = FG.n
        self.nz = [g for g in range(n) if g != FG.one]
        self.pos = {g: i for i, g in enumerate(self.nz)}
        self.dim = len(self.nz) ** 2
        rels = []
        for k in FG.gens:
            for g in self.nz:
                for h in self.nz:
                    v = {}
                    # (u_g k) (x) u_h - u_g (x) (k u_h), u_g k = u_gk - u_k, k u_h = u_kh - u_k
                    for a, c in self.u(FG.mul[g][k]).items():
                        self.add(v, a, h, c)
                    for a, c in self.u(k).items():
                        self.add(v, a, h, -c)
                    for b, c in self.u(FG.mul[k][h]).items():
                        self.add(v, g, b, -c)
                    for b, c in self.u(k).items():
                        self.add(v, g, b, c)
                    rels.append(self.vec(v))
        self.rels = rels

    def u(self, g):
        return {} if g == self.FG.one else {g: 1}

    def add(self, v, a, b, c):
        key = self.pos[a] * len(self.nz) + self.pos[b]
        v[key] = v.get(key, 0) + c

    def vec(self, v):
        w = [0] * self.dim
        for k, c in v.items():
            w[k] += c
        return vector(ZZ, w)

    def elem(self, pairs):
        """sum c u_a (x) u_b for pairs (a, b, c) (terms with a or b = 1 vanish)."""
        v = {}
        for a, b, c in pairs:
            if a != self.FG.one and b != self.FG.one:
                self.add(v, a, b, c)
        return self.vec(v)

    def mu_matrix(self):
        """s (x) t -> s t in Delta (basis u_g): (g-1)(h-1) = u_gh - u_g - u_h."""
        m = len(self.nz)
        M = zero_matrix(ZZ, m, self.dim)
        for g in self.nz:
            for h in self.nz:
                col = self.pos[g] * m + self.pos[h]
                gh = self.FG.mul[g][h]
                if gh != self.FG.one:
                    M[self.pos[gh], col] += 1
                M[self.pos[g], col] -= 1
                M[self.pos[h], col] -= 1
        return M

    def whole_invariants(self):
        """Invariants of Delta (x)_G Delta = Z^dim / (relations)."""
        R = matrix(ZZ, self.rels)
        ed = [d for d in R.elementary_divisors() if d != 0]
        return canon(ed + [0] * (self.dim - len(ed)))

    def kernel_and_whole(self):
        V = ZZ ** self.dim
        W = V.submodule(self.rels)
        whole = canon((V / W).invariants())
        Kgens = self.mu_matrix().right_kernel_matrix().rows()
        K = V.submodule(list(Kgens) + list(W.gens()))
        return canon((K / W).invariants()), whole, V, W, K


def fox(word, i, FG, imgs):
    """d word / d x_i evaluated in Z G (dict element -> coeff), book convention
    d(u v) = d(u) v + d(v), d x_i = 1, d x_i^(-1) = -x_i^(-1).  Also returns the
    value of the word."""
    # process from the right: d(w_1 ... w_k) = sum_l d(w_l) w_(l+1) ... w_k
    res = {}
    suffix = FG.one
    for (j, e) in reversed(word):
        g = imgs[j]
        if j == i:
            if e > 0:
                key = FG.mul[FG.one][suffix]          # 1 * suffix
                res[key] = res.get(key, 0) + 1
            else:
                key = FG.mul[FG.inv[g]][suffix]
                res[key] = res.get(key, 0) - 1
        suffix = FG.mul[g if e > 0 else FG.inv[g]][suffix]
    return {k: c for k, c in res.items() if c}, suffix


def schur_cover(G):
    """GAP's Schur cover as a permutation group with its epimorphism onto G."""
    epi = libgap.EpimorphismSchurCover(G)
    iso = libgap.IsomorphismPermGroup(libgap.Source(epi))
    iso = libgap.CompositionMapping(
        libgap.SmallerDegreePermutationRepresentation(libgap.Image(iso)), iso)
    Ghat = libgap.Image(iso)
    return Ghat, libgap.CompositionMapping(epi, libgap.InverseGeneralMapping(iso))


def word_from_gap(w):
    return [(abs(int(x)) - 1, 1 if int(x) > 0 else -1)
            for x in libgap.LetterRepAssocWord(w)]


def section_5_delta_tensor():
    # K = Ker(Delta (x)_G Delta -> Delta) = H_2 G; Delta (x)_G Delta = K + Z^(n-1).
    cases = []
    for order in range(2, 17):
        for i in range(1, int(libgap.NumberSmallGroups(order)) + 1):
            cases.append(('SmallGroup(%d,%d)' % (order, i), libgap.SmallGroup(order, i)))
    cases += [('SymmetricGroup(4)', gap('SymmetricGroup(4)')), ('SL(2,3)', gap('SL(2,3)')),
              ('A4 x Z2', gap('DirectProduct(AlternatingGroup(4), CyclicGroup(IsPermGroup, 2))'))]
    for name, G in cases:
        FG = FinGroup(G)
        DT = DeltaTensor(FG)
        mult = canon([ZZ(x) for x in libgap.AbelianInvariantsMultiplier(G)])
        if FG.n <= 8:
            K, whole, _, _, _ = DT.kernel_and_whole()
            check(K == mult, 'p. 205: Ker(Delta (x)_G Delta -> Delta) = H_2 %s' % name)
        else:
            # the image Delta^2 of Delta (x)_G Delta in Delta is free, so the
            # kernel is the torsion of Delta (x)_G Delta
            whole = DT.whole_invariants()
            check([d for d in whole if d] == mult,
                  'p. 205: torsion of Delta (x)_G Delta = H_2 %s' % name)
        check(whole == canon(mult + [0] * (FG.n - 1)),
              'p. 205: Delta (x)_G Delta = H_2 + Delta^2, %s' % name)


def section_5_free_abelian():
    # exc:h2-free-abelian-basis on finite analogues Z_m^r.
    for m, r in [(2, 2), (3, 2), (4, 2), (2, 3), (2, 4)]:
        G = gap('AbelianGroup(IsPermGroup, %s)' % ([m] * r))
        FG = FinGroup(G)
        gens = [FG.index(g) for g in libgap.GeneratorsOfGroup(G)]
        DT = DeltaTensor(FG)
        Kinv, _, V, W, K = DT.kernel_and_whole()
        els = [DT.elem([(gens[i], gens[j], 1), (gens[j], gens[i], -1)])
               for i in range(r) for j in range(i + 1, r)]
        S = V.submodule(list(W.gens()) + els)
        check(S == K and Kinv == canon([m] * (r * (r - 1) // 2)),
              'exc. 4.5.1: (x_i-1)(x)(x_j-1) - (x_j-1)(x)(x_i-1) generate K, Z_%d^%d'
              % (m, r))


def section_5_hopf_fox():
    # exc:hopf-fox-isomorphism.
    rng = random.Random(4005)
    F2 = libgap.FreeGroup(2)
    x, y = libgap.GeneratorsOfGroup(F2)
    F3 = libgap.FreeGroup(3)
    x3, y3, z3 = libgap.GeneratorsOfGroup(F3)
    comm = lambda u, v: u ** -1 * v ** -1 * u * v
    cases = [
        ('Z2^2', gap('Group((1,2),(3,4))'), 2, [comm(x, y)]),
        ('Z4xZ2', gap('Group((1,2,3,4),(5,6))'), 2, [comm(x, y)]),
        ('Z3^2', gap('Group((1,2,3),(4,5,6))'), 2, [comm(x, y)]),
        ('D8', gap('Group((1,2),(1,3)(2,4))'), 2, [comm(x, y) ** 2]),
        ('Q8', gap('Group((1,2,4,7)(3,6,8,5),(1,3,4,8)(2,5,7,6))'), 2, [comm(x, y) ** 2]),
        ('Z2^3', gap('Group((1,2),(3,4),(5,6))'), 3,
         [comm(x3, y3), comm(x3, z3), comm(y3, z3)]),
    ]
    for name, G, r, vs in cases:
        FG = FinGroup(G)
        imgs = [FG.index(g) for g in libgap.GeneratorsOfGroup(G)]
        assert len(imgs) == r
        DT = DeltaTensor(FG)
        Kinv, _, V, W, K = DT.kernel_and_whole()
        mu = DT.mu_matrix()
        hs = []
        for v in vs:
            word = word_from_gap(v)
            pairs = []
            value = None
            for i in range(r):
                d, value = fox(word, i, FG, imgs)
                check(sum(d.values()) == 0, 'v in F\': dv/dx_i in Delta')
                for k, c in d.items():
                    pairs.append((imgs[i], k, c))     # (g_i - 1) (x) c (k - 1)
            check(value == FG.one, 'v in N')
            h = DT.elem(pairs)
            check(mu * h == 0, 'exc. 4.5.3: h in K for v in F\' cap N, %s' % name)
            hs.append(h)
        S = V.submodule(list(W.gens()) + hs)
        check(S == K, 'exc. 4.5.3: the h generate K = H_2 %s' % name)
    # Fox identity v(g) - 1 = sum (g_i - 1) dv/dg_i on random words (S_4, 2 generators)
    G = gap('SymmetricGroup(4)')
    FG = FinGroup(G)
    imgs = [FG.index(g) for g in libgap.GeneratorsOfGroup(G)]
    for _ in range(40):
        word = [(rng.randint(0, 1), rng.choice([1, -1])) for _ in range(rng.randint(1, 12))]
        total = {}
        val = None
        for i in range(2):
            d, val = fox(word, i, FG, imgs)
            for k, c in d.items():
                gk = FG.mul[imgs[i]][k]
                total[gk] = total.get(gk, 0) + c
                total[k] = total.get(k, 0) - c
        total = {k: c for k, c in total.items() if c}
        expect = {} if val == FG.one else {val: 1, FG.one: -1}
        check(total == expect, 'Fox identity (book convention)')
    # printed "v in F'": v = [x, y] in S_3 is in F' but not in N.
    G = gap('SymmetricGroup(3)')
    FG = FinGroup(G)
    imgs = [FG.index(g) for g in libgap.GeneratorsOfGroup(G)]
    DT = DeltaTensor(FG)
    word = word_from_gap(comm(x, y))
    pairs = []
    for i in range(2):
        d, value = fox(word, i, FG, imgs)
        pairs += [(imgs[i], k, c) for k, c in d.items()]
    refuted(DT.mu_matrix() * DT.elem(pairs) == 0,
            'exc. 4.5.3 printed: v in F\' (not in N) gives h in K')


def section_5_coboundary():
    # C348: delta phi(s, t) = phi(s) t - phi(s t) + eps(s) phi(t).
    rng = random.Random(4006)
    for name in ['SymmetricGroup(3)', 'Group((1,2),(1,3)(2,4))']:
        FG = FinGroup(gap(name))
        n = FG.n
        for module in ('trivial', 'regular'):
            dim = 1 if module == 'trivial' else n

            def act(vec_, g):          # right action of g on the module
                if module == 'trivial':
                    return vec_
                w = [0] * n
                for a, c in enumerate(vec_):
                    if c:
                        w[FG.mul[a][g]] += c
                return w
            phi = {g: [rng.randint(-3, 3) for _ in range(dim)] for g in range(n)}
            phi[FG.one] = [0] * dim

            def dphi(g1, g2):
                a = act(phi[g1], g2)
                return [a[i] - phi[FG.mul[g1][g2]][i] + phi[g2][i] for i in range(dim)]
            printed_always = True
            for _ in range(10):
                s = {g: rng.randint(-2, 2) for g in range(n)}
                t = {g: rng.randint(-2, 2) for g in range(n)}
                lhs = [0] * dim
                for g1, a in s.items():
                    for g2, b in t.items():
                        d = dphi(g1, g2)
                        for i in range(dim):
                            lhs[i] += a * b * d[i]
                phis = [sum(a * phi[g][i] for g, a in s.items()) for i in range(dim)]
                phist = [0] * dim
                phis_t = [0] * dim
                for g1, a in s.items():
                    for g2, b in t.items():
                        for i in range(dim):
                            phist[i] += a * b * phi[FG.mul[g1][g2]][i]
                        aa = act(phi[g1], g2)
                        for i in range(dim):
                            phis_t[i] += a * b * aa[i]
                eps_s, eps_t = sum(s.values()), sum(t.values())
                phit = [sum(b * phi[g][i] for g, b in t.items()) for i in range(dim)]
                corrected = [phis_t[i] - phist[i] + eps_s * phit[i] for i in range(dim)]
                printed = [phis_t[i] - phist[i] + eps_t * phis[i] for i in range(dim)]
                check(lhs == corrected, 'C348: delta phi(s,t) with eps(s) phi(t), %s' % name)
                printed_always = printed_always and lhs == printed
            refuted(printed_always, 'C348 printed eps(t) phi(s), %s, %s' % (name, module))


def section_5_cocycle():
    # the extended cocycle identity (p. 203) and (4.23).
    rng = random.Random(4006)
    exts = [
        ('Q8 / centre', 'SmallGroup(8,4)', 'Centre', True),
        ('Z4 / 2Z4', 'CyclicGroup(IsPermGroup, 4)', 'Centre-2', True),
        ('Dic12 / Z3', 'SmallGroup(12,1)', 'Sylow3', False),
        ('A4 / V4', 'AlternatingGroup(4)', 'Group((1,2)(3,4),(1,3)(2,4))', False),
    ]
    for name, Es, As, central in exts:
        E = gap(Es)
        if not bool(libgap.IsPermGroup(E)):
            E = libgap.Image(libgap.IsomorphismPermGroup(E))
        if As == 'Centre':
            A = libgap.Centre(E)
        elif As == 'Centre-2':
            A = libgap.Subgroup(E, [libgap.GeneratorsOfGroup(E)[0] ** 2])
        elif As == 'Order4':
            A = libgap.Subgroup(E, [next(g for g in libgap.AsList(E) if int(libgap.Order(g)) == 4)])
        elif As == 'Sylow3':
            A = libgap.SylowSubgroup(E, 3)
        else:
            A = gap(As)
        FE = FinGroup(E)
        hom = libgap.NaturalHomomorphismByNormalSubgroup(E, A)
        Q = libgap.Image(hom)
        Qelts = libgap.AsList(Q)
        nQ = len(Qelts)
        qidx = lambda e: int(libgap.Position(Qelts, libgap.Image(hom, FE.elts[e]))) - 1
        # section: first preimage times a fixed a_0 != 1 of A (so that the
        # cocycle is not identically 0), identity for the identity
        qone = qidx(FE.one)
        a0 = next(e for e in range(FE.n) if e != FE.one and qidx(e) == qone)
        sec = [None] * nQ
        for e in range(FE.n):
            q = qidx(e)
            if sec[q] is None:
                sec[q] = FE.mul[e][a0]
        sec[qone] = FE.one
        qmul = [[qidx(FE.mul[sec[a]][sec[b]]) for b in range(nQ)] for a in range(nQ)]
        # A additively: Z_(o_1) + ...
        indep = libgap.IndependentGeneratorsOfAbelianGroup(A)
        orders = [int(libgap.Order(g)) for g in indep]
        coords = lambda e: [int(c) for c in libgap.IndependentGeneratorExponents(A, FE.elts[e])]
        # f(a, b): sec(a) sec(b) = sec(ab) f(a, b)
        f = {}
        for a in range(nQ):
            for b in range(nQ):
                ab = qmul[a][b]
                e = FE.mul[FE.inv[sec[ab]]][FE.mul[sec[a]][sec[b]]]
                f[(a, b)] = coords(e)
        # right action of q on A: a -> sec(q)^-1 a sec(q)
        Aelts = [e for e in range(FE.n) if qidx(e) == qone]

        def actA(vec_, q):
            # find the element with these coordinates, conjugate it, coordinates back
            for e in Aelts:
                if [c % o for c, o in zip(coords(e), orders)] == [c % o for c, o in zip(vec_, orders)]:
                    s = sec[q]
                    return coords(FE.mul[FE.mul[FE.inv[s]][e]][s])
            raise AssertionError
        actcache = {}

        def act(vec_, q):
            key = (tuple(c % o for c, o in zip(vec_, orders)), q)
            if key not in actcache:
                actcache[key] = actA(vec_, q)
            return actcache[key]

        def red(vec_):
            return tuple(c % o for c, o in zip(vec_, orders))

        def addv(u, v, c=1):
            return [a + c * b for a, b in zip(u, v)]

        def fZ(s, r):
            out = [0] * len(orders)
            for a, ca in s.items():
                for b, cb in r.items():
                    out = addv(out, f[(a, b)], ca * cb)
            return out

        def actZ(vec_, t):
            out = [0] * len(orders)
            for q, c in t.items():
                out = addv(out, act(vec_, q), c)
            return out

        def mulZ(s, r):
            out = {}
            for a, ca in s.items():
                for b, cb in r.items():
                    out[qmul[a][b]] = out.get(qmul[a][b], 0) + ca * cb
            return out
        ok_cocycle = True
        ok_central = True
        for _ in range(12):
            s = {q: rng.randint(-2, 2) for q in range(nQ)}
            r = {q: rng.randint(-2, 2) for q in range(nQ)}
            t = {q: rng.randint(-2, 2) for q in range(nQ)}
            eps = sum(s.values())
            lhs = addv(addv(actZ(fZ(s, r), t), fZ(s, mulZ(r, t)), -1), fZ(mulZ(s, r), t))
            lhs = addv(lhs, fZ(r, t), -eps)
            ok_cocycle = ok_cocycle and red(lhs) == tuple([0] * len(orders))
            # s, t in Delta: subtract the augmentation at the identity
            s[qone] -= sum(s.values())
            t[qone] -= sum(t.values())
            ok_central = ok_central and red(fZ(mulZ(s, r), t)) == red(fZ(s, mulZ(r, t)))
        check(ok_cocycle, 'p. 203: the cocycle identity over Z G, %s' % name)
        if central:
            check(ok_central, '(4.23): f(s r, t) = f(s, r t), central %s' % name)
        else:
            refuted(ok_central, '(4.23) for the non-central extension %s' % name)


def section_5_ext():
    # prop:ext-extensions-description; C352.
    pairs = [('SymmetricGroup(3)', 'CyclicGroup(IsPermGroup, 4)', 2),
             ('AlternatingGroup(4)', 'CyclicGroup(IsPermGroup, 9)', 3),
             ('Group((1,2),(1,3)(2,4))', 'AbelianGroup(IsPermGroup, [4, 2])', 2),
             ('SmallGroup(12,1)', 'CyclicGroup(IsPermGroup, 8)', 2)]
    for Gs, Bs, a in pairs:
        G = gap(Gs)
        if not bool(libgap.IsPermGroup(G)):
            G = libgap.Image(libgap.IsomorphismPermGroup(G))
        B = gap(Bs)
        piG = libgap.NaturalHomomorphismByNormalSubgroup(G, libgap.DerivedSubgroup(G))
        Gab = libgap.Image(piG)
        epis = [e for e in libgap.GQuotients(B, Gab)]
        check(len(epis) > 0, 'B maps onto G_ab')
        piB = epis[0]
        check(int(libgap.Size(libgap.Kernel(piB))) == a, '|A| = %d' % a)
        Gbar = libgap.SubdirectProduct(G, B, piG, piB)
        check(int(libgap.Size(Gbar)) == int(libgap.Size(G)) * a, '|Gbar| = |G| |A|')
        p1 = libgap.Projection(Gbar, 1)
        p2 = libgap.Projection(Gbar, 2)
        D = libgap.DerivedSubgroup(Gbar)
        check(libgap.Image(p1, D) == libgap.DerivedSubgroup(G)
              and libgap.Size(D) == libgap.Size(libgap.DerivedSubgroup(G)),
              'prop 5.4: Gbar\' = G\', %s' % Gs)
        check(gap_invariants(Gbar) == gap_invariants(B), 'prop 5.4: Gbar_ab = B, %s' % Gs)
        # the g with (g, 1) in Gbar: the projection to G of Ker(Gbar -> B)
        S = libgap.Image(p1, libgap.Kernel(p2))
        check(S == libgap.DerivedSubgroup(G), 'C352: (g, 1) in Gbar iff g in G\', %s' % Gs)
        refuted(S == G, 'printed: (g, 1) in Gbar for all g in G, %s' % Gs)


def section_5_standard():
    # prop:standard-central-extension: generators x_g (g != 1).
    for order in range(2, 9):
        for i in range(1, int(libgap.NumberSmallGroups(order)) + 1):
            G = libgap.SmallGroup(order, i)
            P = libgap.Image(libgap.IsomorphismPermGroup(G))
            gens = [g for g in libgap.AsList(P) if not bool(libgap.IsOne(g))]
            cay = Cayley(P, gens)
            C = quotient_invariants(cay.k, cay.coinvariant_relations().rows())
            _, whole, _, _, _ = DeltaTensor(FinGroup(P)).kernel_and_whole()
            check(C == whole, 'prop 5.5: N/[F,N] = Delta (x)_G Delta, SmallGroup(%d,%d)'
                  % (order, i))


def section_5_perfect():
    # prop:perfect-universal-criterion, prop:perfect-central-preimage.
    for name in ['AlternatingGroup(5)', 'PSL(2,7)', 'PSL(2,8)']:
        G = gap(name)
        Ghat, epi = schur_cover(G)
        mult = canon([ZZ(x) for x in libgap.AbelianInvariantsMultiplier(G)])
        order_m = 1
        for q in mult:
            order_m *= q
        check(int(libgap.Size(Ghat)) == int(libgap.Size(G)) * order_m
              and bool(libgap.IsPerfectGroup(Ghat))
              and canon(libgap.AbelianInvariantsMultiplier(Ghat)) == []
              and bool(libgap.IsSubset(libgap.Centre(Ghat), libgap.Kernel(epi))),
              'prop 5.10: the universal central extension of %s' % name)
    perfect = [('SL(2,9)', gap('SL(2,9)'))]
    for name, G in perfect:
        if not bool(libgap.IsPermGroup(G)):
            G = libgap.Image(libgap.IsomorphismPermGroup(G))
        Ghat, epi = schur_cover(G)
        pre = libgap.PreImage(epi, libgap.Centre(G))
        check(bool(libgap.IsPerfectGroup(G)) and int(libgap.Size(libgap.Centre(G))) > 1
              and bool(libgap.IsSubset(libgap.Centre(Ghat), pre)),
              'prop 5.8: the preimage of the centre is central, %s' % name)


def section_5_burnside():
    # exc:burnside-lemma.
    for order in (16, 27):
        for i in range(1, int(libgap.NumberSmallGroups(order)) + 1):
            G = libgap.SmallGroup(order, i)
            ok = gap('''function(G, N) local hom, A, k, t, ok, i;
              hom := NaturalHomomorphismByNormalSubgroup(G, DerivedSubgroup(G));
              A := Image(hom);
              k := Length(MinimalGeneratingSet(G));
              ok := true;
              for i in [1..N] do
                t := List([1..k], j -> Random(G));
                if Subgroup(A, List(t, x -> Image(hom, x))) = A then
                  ok := ok and Subgroup(G, t) = G;
                fi;
              od;
              return ok; end''')(G, 300)
            check(bool(ok), 'exc. 4.5.7 (Burnside): SmallGroup(%d,%d)' % (order, i))


def section_5():
    section_5_delta_tensor()
    section_5_free_abelian()
    section_5_hopf_fox()
    section_5_coboundary()
    section_5_cocycle()
    section_5_ext()
    section_5_standard()
    section_5_perfect()
    section_5_burnside()


# ---------------------------------------------------------------------------
# Cayley graphs: the relation module as the cycle space
# ---------------------------------------------------------------------------

class Cayley:
    """Cayley graph of a finite permutation group for generators x_1..x_r."""

    def __init__(self, G, gens):
        self.gens = list(gens)
        self.r = len(self.gens)
        elts = libgap.AsList(G)
        self.n = int(libgap.Size(G))
        pos = gap('function(e, s) return List(e, g -> Position(e, g * s)); end')
        lpos = gap('function(e, s) return List(e, g -> Position(e, s * g)); end')
        self.right = [[int(x) - 1 for x in pos(elts, s)] for s in self.gens]
        self.left = [[int(x) - 1 for x in lpos(elts, s)] for s in self.gens]
        self.one = int(libgap.Position(elts, libgap.One(G))) - 1
        self.inv_right = []
        for j in range(self.r):
            inv = [0] * self.n
            for v in range(self.n):
                inv[self.right[j][v]] = v
            self.inv_right.append(inv)
        parent = {self.one: None}
        order = [self.one]
        tree = set()
        for v in order:
            for j in range(self.r):
                w = self.right[j][v]
                if w not in parent:
                    parent[w] = (v, j)
                    tree.add((v, j))
                    order.append(w)
        assert len(parent) == self.n
        self.nontree = [(v, j) for v in range(self.n) for j in range(self.r)
                        if (v, j) not in tree]
        self.coord = {e: i for i, e in enumerate(self.nontree)}
        self.k = len(self.nontree)
        assert self.k == 1 + self.n * (self.r - 1)
        self.path = {self.one: {}}
        for v in order[1:]:
            u, j = parent[v]
            p = dict(self.path[u])
            p[(u, j)] = p.get((u, j), 0) + 1
            self.path[v] = p
        self.cycles = []
        for (v, j) in self.nontree:
            w = self.right[j][v]
            z = dict(self.path[v])
            z[(v, j)] = z.get((v, j), 0) + 1
            for e, c in self.path[w].items():
                z[e] = z.get(e, 0) - c
            self.cycles.append({e: c for e, c in z.items() if c})

    def coords(self, z):
        v = [0] * self.k
        for e, c in z.items():
            if e in self.coord:
                v[self.coord[e]] += c
        return vector(ZZ, v)

    def translate(self, h, z):
        return {(self.left[h][v], j): c for (v, j), c in z.items()}

    def action_matrices(self):
        return [matrix(ZZ, [self.coords(self.translate(h, z)) for z in self.cycles])
                for h in range(self.r)]

    def coinvariant_relations(self):
        return matrix(ZZ, [row for t in self.action_matrices() for row in (t - 1).rows()])

    def h2(self):
        """(N cap F') / [N, F] (the Hopf formula): kernel of N/[N,F] -> F/F'."""
        Phi = zero_matrix(ZZ, self.k, self.r)
        for i, z in enumerate(self.cycles):
            for (v, j), c in z.items():
                Phi[i, j] += c
        V = ZZ ** self.k
        W = V.submodule(self.coinvariant_relations().rows())
        K = V.submodule(Phi.left_kernel_matrix().rows())
        return canon((K / W).invariants())

    def trace(self, word):
        v = self.one
        z = {}
        for j, e in word:
            if e > 0:
                z[(v, j)] = z.get((v, j), 0) + 1
                v = self.right[j][v]
            else:
                u = self.inv_right[j][v]
                z[(u, j)] = z.get((u, j), 0) - 1
                v = u
        return z, v


def wedge(s, t):
    k = len(s)
    return vector(ZZ, [s[p] * t[q] - s[q] * t[p]
                       for p, q in itertools.combinations(range(k), 2)])


def compound2(T):
    k = T.nrows()
    pairs = list(itertools.combinations(range(k), 2))
    return matrix(ZZ, [[T[i, p] * T[j, q] - T[i, q] * T[j, p] for (p, q) in pairs]
                       for (i, j) in pairs])


def wedge_coinvariants(cay):
    """(M ^ M)_G: the module Z^C(k,2) and the relation submodule."""
    T = cay.action_matrices()
    D = len(list(itertools.combinations(range(cay.k), 2)))
    rels = []
    for t in T:
        C2 = compound2(t)
        rels.extend((C2 - 1).rows())
    V = ZZ ** D
    return V, V.submodule(rels), T


# ---------------------------------------------------------------------------
# Section 6: knotted surface groups (pp. 213-223)
# ---------------------------------------------------------------------------

def fox_laurent(word, i, t):
    """d word / d x_i (book convention) with every generator -> t."""
    res = 0
    suffix = 1
    for (j, e) in reversed(word):
        if j == i:
            res += suffix if e > 0 else -t ** -1 * suffix
        suffix = (t if e > 0 else t ** -1) * suffix
    return res


def alexander(relators, ngens):
    L = LaurentPolynomialRing(ZZ, 't')
    t = L.gen()
    J = matrix(L, [[fox_laurent(r, i, t) for i in range(ngens)] for r in relators])
    minor = J.matrix_from_rows_and_columns(list(range(ngens - 1)), list(range(ngens - 1)))
    d = minor.determinant()
    # normalize up to +-t^k
    P = PolynomialRing(ZZ, 's')
    if d == 0:
        return P(0)
    ex = d.exponents()
    lo = min(ex)
    poly = P({e - lo: c for e, c in zip(ex, d.coefficients())})
    if poly.leading_coefficient() < 0:
        poly = -poly
    return poly


def cyclic_forms(word):
    """all cyclic permutations of a word and of its inverse."""
    inv = [(j, -e) for (j, e) in reversed(word)]
    out = set()
    for w in (word, inv):
        for k in range(len(w)):
            out.add(tuple(w[k:] + w[:k]))
    return out


def free_reduce(word):
    out = []
    for le in word:
        if out and out[-1][0] == le[0] and out[-1][1] == -le[1]:
            out.pop()
        else:
            out.append(le)
    while len(out) > 1 and out[0][0] == out[-1][0] and out[0][1] == -out[-1][1]:
        out = out[1:-1]
    return out


def trefoil_from_figure(path):
    """Wirtinger relators of the trefoil drawn in Рис. 2 (points and heights)."""
    src = open(path).read()
    block = src[src.index('#let trefoil = spline('):]
    block = block[:block.index(').map(')]
    pts = [tuple(float(a) for a in m) for m in
           re.findall(r'\(([-\d.]+), ([-\d.]+), ([-\d.]+)\)', block)]
    n = len(pts)
    marks = [i for i, p in enumerate(pts) if p[2] != 0.12]
    # pair an over-point (0.2) with an under-point (0.04) at the same place
    crossings = []
    for i in marks:
        if pts[i][2] == 0.2:
            j = min((j for j in marks if pts[j][2] == 0.04),
                    key=lambda j: (pts[i][0] - pts[j][0]) ** 2 + (pts[i][1] - pts[j][1]) ** 2)
            crossings.append((i, j))
    seq = sorted(marks)
    kinds = ['O' if pts[i][2] == 0.2 else 'U' for i in seq]
    under = sorted(j for _, j in crossings)
    # arcs: arc a runs from under-point under[a-1] to under[a] (cyclically)

    def arc_of(i):
        for a in range(len(under)):
            lo, hi = under[a - 1], under[a]
            if lo < hi:
                if lo < i < hi:
                    return a
            elif i > lo or i < hi:
                return a
        raise AssertionError

    def direction(i):
        p, q = pts[(i - 1) % n], pts[(i + 1) % n]
        return (q[0] - p[0], q[1] - p[1])
    rels = []
    for i, j in crossings:
        k = arc_of(i)                          # over arc
        a_in = under.index(j)                  # arc ending at j
        a_out = (a_in + 1) % len(under)        # arc starting at j
        do, du = direction(i), direction(j)
        sign = 1 if do[0] * du[1] - do[1] * du[0] > 0 else -1
        # x_out = x_k^(-sign) x_in x_k^(sign)
        rels.append(free_reduce([(k, -sign), (a_in, 1), (k, sign), (a_out, -1)]))
    return len(crossings), kinds, len(under), rels


def section_6():
    F3 = libgap.FreeGroup(['x', 'y', 'z'])
    x, y, z = libgap.GeneratorsOfGroup(F3)
    rels = [y ** -1 * x * y * z ** -1, z ** -1 * y * z * x ** -1, x ** -1 * z * x * y ** -1]
    G = F3 / libgap(rels)
    check(gap_invariants(G) == [0], 'p. 216: trefoil G_ab = Z')
    words = [word_from_gap(r) for r in rels]
    # eliminate z = y^-1 x y
    sub = {0: [(0, 1)], 1: [(1, 1)], 2: [(1, -1), (0, 1), (1, 1)]}

    def substitute(w):
        out = []
        for j, e in w:
            piece = sub[j] if e > 0 else [(a, -b) for (a, b) in reversed(sub[j])]
            out += piece
        return free_reduce(out)
    target = free_reduce([(0, 1), (1, 1), (0, 1), (1, -1), (0, -1), (1, -1)])
    forms = cyclic_forms(target)
    reduced = [substitute(w) for w in words]
    check(reduced[0] == [] and all(tuple(r) in forms for r in reduced[1:]),
          'p. 216: eliminating z leaves x y x = y x y twice')
    check([sum(e for j, e in target if j == i) for i in range(2)] == [1, -1],
          'trefoil relator not in F\': H_2 = 0 (p. 195)')
    P = PolynomialRing(ZZ, 's')
    s = P.gen()
    check(alexander(words, 3) == s ** 2 - s + 1, 'trefoil: Alexander polynomial t^2 - t + 1')
    path = 'content/diagrams/04-06-knotted-surface-groups.typ'
    ncross, kinds, narcs, frels = trefoil_from_figure(path)
    check(ncross == 3 and narcs == 3, 'Рис. 2: three crossings, three arcs')
    check(all(kinds[i] != kinds[(i + 1) % len(kinds)] for i in range(len(kinds))),
          'Рис. 2: the diagram is alternating')
    check(alexander(frels, 3) == s ** 2 - s + 1,
          'Рис. 2: Alexander polynomial of the drawn knot is t^2 - t + 1')
    Ffig = libgap.FreeGroup(3)
    gens = libgap.GeneratorsOfGroup(Ffig)
    gw = [libgap.Product([gens[j] ** e for j, e in r]) for r in frels]
    check(gap_invariants(Ffig / libgap(gw)) == [0], 'Рис. 2: G_ab = Z')

    # the 2-knot group <x, y | x^-1 y x = y^-1, y^3>
    F2 = libgap.FreeGroup(['x', 'y'])
    x, y = libgap.GeneratorsOfGroup(F2)
    rels2 = [x ** -1 * y * x * y, y ** 3]
    G2 = F2 / libgap(rels2)
    check(gap_invariants(G2) == [0], 'p. 217: G_ab = Z')
    check(int(libgap.Size(F2 / libgap(rels2 + [x]))) == 1,
          'p. 217: G is the normal closure of x')
    hom = libgap.GroupHomomorphismByImages(G2, gap('SymmetricGroup(3)'),
                                           libgap.GeneratorsOfGroup(G2),
                                           [gap('(1,2)'), gap('(1,2,3)')])
    check(hom != libgap.fail and int(libgap.Order(libgap.Image(hom, libgap.GeneratorsOfGroup(G2)[1]))) == 3,
          'p. 217: y has order 3 (torsion)')
    # H_2 = Coker(1 - x on H_2 Z_3 = 0) + Ker(1 - x on H_1 Z_3), x = -1
    check(gcd(3, 1 - (-1)) == 1, 'p. 217: H_2 G = Ker(2 on Z_3) = 0')

    # d(d-1)/2 <= d iff d <= 3; Z^n x|_A Z with conditions 1-3.
    check(all((d * (d - 1) // 2 <= d) == (d <= 3) for d in range(0, 30)),
          'p. 217: dim (G\' ^ G\') <= dim G\' iff dim G\' <= 3')
    # n = 2 is impossible: Lambda^2 Z^2 = Z with g acting by det A = +-1, so
    # H_2 contains Coker(det A - 1) = Z or Z_2.
    check(all(quotient_invariants(1, [vector(ZZ, [dA - 1])]) != [] for dA in (1, -1)),
          'Z^2 x| Z always has H_2 != 0')
    for n in range(3, 7):
        found = None
        for coeffs in itertools.product(range(-2, 3), repeat=n - 1):
            cs = list(coeffs) + [1]           # constant term +-1: det A = +-1
            for c0 in (1, -1):
                cs[-1] = c0
                A = matrix(ZZ, n, n)
                for i in range(n - 1):
                    A[i + 1, i] = 1
                for i in range(n):
                    A[i, n - 1] = -cs[n - 1 - i] if i < n - 1 else -cs[0]
                if abs(A.det()) != 1:
                    continue
                if abs((A - 1).det()) != 1:
                    continue
                if abs((compound2(A) - 1).det()) != 1:
                    continue
                found = A
                break
            if found is not None:
                break
        check(found is not None, 'p. 217: Z^%d x| Z with conditions 1-3 exists' % n)
        A = found
        # G_ab = Z + Coker(A - 1) = Z; H_2 = Coker(Lambda^2 A - 1) + Ker(A - 1) = 0
        check(quotient_invariants(n, (A - 1).columns()) == []
              and quotient_invariants(n * (n - 1) // 2, (compound2(A) - 1).columns()) == []
              and (A - 1).right_kernel().rank() == 0,
              'Z^%d x| Z: G_ab = Z, H_2 = 0, normal closure of t, G\' = Z^%d' % (n, n))

    # (4.32), exm:gn-irreducible.
    for n in range(2, 13):
        Fg = libgap.FreeGroup(['g', 'a', 'b'])
        g, a, b = libgap.GeneratorsOfGroup(Fg)
        rels = [a * b * a ** -1 * b ** -1, a ** n, b ** n, g ** -1 * a * g * b ** -1,
                g ** -1 * b * g * (a * b ** -1) ** -1]
        Gn = Fg / libgap(rels)
        check(gap_invariants(Gn) == [0], '(4.32): G_%d / G_%d\' = Z' % (n, n))
        check(int(libgap.Size(Fg / libgap(rels + [g]))) == 1,
              '(4.32): G_%d is the normal closure of g' % n)
        Gm1 = matrix(ZZ, [[-1, 1], [1, -2]])            # rows: a(g-1), b(g-1)
        A = Gm1 + 1                                      # a -> b, b -> a - b
        check(A == matrix(ZZ, [[0, 1], [1, -1]]) and Gm1.det() == 1,
              'exm 7.6: g - 1 has the printed matrix, det 1')
        check(A.det() == -1, 'exm 7.6: g acts on M ^ M by det = -1, g - 1 by -2')
        Mn = ZZ ** 2
        fixed = [v for v in itertools.product(range(n), repeat=2)
                 if all((vector(ZZ, v) * Gm1)[i] % n == 0 for i in range(2)) and any(v)]
        check(fixed == [], 'C(g) = <g>: g - 1 has no kernel on Z_%d^2' % n)
        H2 = canon([gcd(n, 2)])
        check((H2 == []) == (n % 2 == 1), 'exm 7.6: H_2 G_%d = Z_%d / 2: '
              'irreducible iff n odd' % (n, n))

    # exc:simple-group-direct-product.
    for p in (2, 3, 5, 7):
        Ftc = libgap.FreeGroup(['t', 'c'])
        tt, cc = libgap.GeneratorsOfGroup(Ftc)
        G = Ftc / libgap([tt ** -1 * cc ** -1 * tt * cc, cc ** p])   # Z x Z_p = Z x Nhat
        check(gap_invariants(G) == canon([0, p]), '(Z x Z_%d)_ab = Z + Z_%d' % (p, p))
        refuted(gap_invariants(G) == [0],
                'exc. 4.6.3 printed for N = Z_%d: G_ab = Z' % p)
    for name in ['AlternatingGroup(5)', 'PSL(2,7)', 'PSL(2,8)']:
        N = gap(name)
        Nhat, _ = schur_cover(N)
        check(bool(libgap.IsPerfectGroup(Nhat))
              and canon(libgap.AbelianInvariantsMultiplier(Nhat)) == [],
              'exc. 4.6.3: Nhat perfect with H_2 = 0, %s' % name)
        ok = gap('''function(H) local x, cl;
          x := First(AsList(H), y -> not y in Centre(H));
          return NormalClosure(H, Subgroup(H, List(GeneratorsOfGroup(H),
                                                   h -> x^-1 * x^h))) = H; end''')(Nhat)
        check(bool(ok), 'exc. 4.6.3: conjugates of t x generate Z x Nhat, %s' % name)


# ---------------------------------------------------------------------------
# Section 7: irreducible C-groups (pp. 223-230)
# ---------------------------------------------------------------------------

def mmul(A, B):
    n, m, l = len(A), len(B), len(B[0])
    return [[sum((A[i][k] * B[k][j] for k in range(m)), A[0][0] * 0) for j in range(l)]
            for i in range(n)]


def mdet(A):
    """determinant by Gaussian elimination (field elements, lists)."""
    M = [row[:] for row in A]
    n = len(M)
    det = M[0][0] ** 0
    for c in range(n):
        piv = next((r for r in range(c, n) if M[r][c] != 0), None)
        if piv is None:
            return M[0][0] * 0
        if piv != c:
            M[c], M[piv] = M[piv], M[c]
            det = -det
        det *= M[c][c]
        inv = M[c][c] ** -1
        for r in range(c + 1, n):
            f = M[r][c] * inv
            if f != 0:
                for k in range(c, n):
                    M[r][k] -= f * M[c][k]
    return det


def negacyclic(cs, K):
    n = len(cs)
    return [[cs[(j - i) % n] * (1 if j >= i else -1) for j in range(n)] for i in range(n)]


def y_matrix(n, K):
    Y = [[K(0)] * n for _ in range(n)]
    Y[0][n - 1] = K((-1) ** (n - 1))
    for i in range(1, n):
        Y[i][i - 1] = K(1)
    return Y


def section_7_cyclic():
    # cor:derived-quotient-not-even-cyclic
    for n in range(2, 61):
        units = [u for u in range(n) if gcd(u, n) == 1]
        exists = any(gcd(u - 1, n) == 1 for u in units)
        check(exists == (n % 2 == 1), 'cor 7.3: g - 1 onto Z_%d possible iff n odd' % n)


def section_7_eigen():
    # exc:semidirect-eigenvalue-criterion.
    rng = random.Random(4007)

    def criterion(A, p):
        """eigenvalue condition over the splitting field."""
        K = GF(p)
        R = PolynomialRing(K, 'X')
        f = R(A.change_ring(K).charpoly().list())
        deg = 1
        for fac, _ in f.factor():
            deg = deg * fac.degree() // gcd(deg, fac.degree())
        L = GF(p ** deg, 'z')
        roots = []
        for r, e in f.change_ring(L).roots():
            roots += [r] * e
        k = len(roots)
        return all(r != 1 for r in roots) and all(
            roots[i] * roots[j] != 1 for i in range(k) for j in range(i + 1, k))

    def detcond(A, p):
        k = A.nrows()
        d1 = (A - 1).det() % p
        d2 = (compound2(A) - 1).det() % p if k > 1 else 1
        return d1 != 0 and d2 != 0
    mats = []
    for p in (2, 3, 5):
        for entries in itertools.product(range(p), repeat=4):
            A = matrix(ZZ, 2, 2, list(entries))
            if A.det() % p:
                mats.append((A, p))
    for entries in itertools.product(range(2), repeat=9):
        A = matrix(ZZ, 3, 3, list(entries))
        if A.det() % 2:
            mats.append((A, 2))
    count = 0
    while count < 150:
        A = matrix(ZZ, 3, 3, [rng.randint(0, 2) for _ in range(9)])
        if A.det() % 3:
            mats.append((A, 3))
            count += 1
    for A, p in mats:
        check(criterion(A, p) == detcond(A, p),
              'exc. 4.7.1: eigenvalue criterion = g - 1 invertible on M, M ^ M')


def section_7_psl_construction():
    # prop:psl-irreducible-c-group: the construction over F_q.
    exceptions = {(2, 2), (2, 3), (2, 4), (2, 9), (3, 2), (3, 4), (4, 2)}
    qs = [q for q in range(2, 33) if ZZ(q).is_prime_power()]
    for n in range(2, 7):
        for q in qs:
            if (n, q) in exceptions:
                continue
            K = GF(q, 'z')
            p = K.characteristic()
            d = gcd(n, q - 1)
            zeta = K.multiplicative_generator()
            a = zeta ** ((q - 1) // d)
            check(a ** d == 1 and all(a ** e != 1 for e in range(1, d)),
                  'a primitive d-th root of 1')
            Y = y_matrix(n, K)
            check(mdet(Y) == 1, 'prop 7.7: y in SL(%d, %d)' % (n, q))
            W = [[a ** (n - 1 - i) if i == j else K(0) for j in range(n)] for i in range(n)]
            aW = [[a * e for e in row] for row in W]
            check(mmul(Y, W) == mmul(aW, Y), 'prop 7.7: y w = a w y, (n, q) = (%d, %d)' % (n, q))
            detw = mdet(W)
            check(detw == a ** (n * (n - 1) // 2), 'det w = a^(n(n-1)/2)')
            m = n // d
            l = (q - 1) // d
            if n % 2 == 1 or p == 2:
                check(detw == 1, 'det w = 1 (n odd or char 2)')
                final = W
            elif m % 2 == 0:
                check(detw == 1 and detw == (a ** d) ** ((m // 2) * (n - 1)),
                      'det w = 1 (m even)')
                final = W
            else:
                check(detw == -1, 'det w = -1 (m odd)')
                if l % 2 == 0:
                    b = a.sqrt()
                    check(b ** 2 == a, 'a = b^2 for l even')
                    final = [[b * e for e in row] for row in W]
                    check(mdet(final) == 1 and -b ** n == -a ** (n // 2) == 1,
                          'det(b w) = -b^n = -a^(n/2) = 1')
                else:
                    check(not a.is_square(), 'l odd: a is not a square')
                    # c with det c = -1: search over the c'_i (d x d) and embed
                    final = None
                    cands = itertools.product(list(K), repeat=d) if q ** d <= 4000 else \
                        (tuple(K.random_element() for _ in range(d)) for _ in range(4000))
                    for cs1 in cands:
                        C1 = negacyclic(list(cs1), K)
                        if mdet(C1) == -1:
                            cs = [K(0)] * n
                            for i in range(d):
                                cs[i * m] = cs1[i]
                            C = negacyclic(cs, K)
                            check(mdet(C) == mdet(C1) ** m, 'det c = det(c\')^m')
                            check(mmul(C, Y) == mmul(Y, C), 'c commutes with y')
                            final = mmul(W, C)
                            break
                    check(final is not None, 'prop 7.7: c with det c = -1 exists')
            check(mdet(final) == 1 and mmul(Y, final) == mmul([[a * e for e in row]
                                                                 for row in final], Y),
                  'prop 7.7: w\' in SL(%d, %d), y w\' = a w\' y' % (n, q))


def section_7_negacyclic():
    # negacyclic matrices commute with y; m = 1 eigen-structure (C383, C384).
    printed_beta_ok = True
    for (n, q) in [(2, 7), (2, 11), (2, 19), (4, 13), (6, 19), (4, 29), (6, 31)]:
        K = GF(q, 'z')
        d = gcd(n, q - 1)
        if d != n:
            continue
        zeta = K.multiplicative_generator()
        a = zeta ** ((q - 1) // d)
        if a.is_square():
            continue
        L = GF(q ** 2, 'w')
        emb = K.hom([L(K.gen())]) if K.degree() > 1 else (lambda e: L(e))
        aL = emb(a)
        bL = aL.sqrt()
        Y = y_matrix(n, K)
        for _ in range(5):
            cs = [K.random_element() for _ in range(n)]
            C = negacyclic(cs, K)
            check(mmul(C, Y) == mmul(Y, C), 'negacyclic c commutes with y')
            CL = [[emb(e) for e in row] for row in C]
            bk = [bL * aL ** k for k in range(n)]
            prod = L(1)
            for b_k in bk:
                check(b_k ** n == -1, 'b_k is an n-th root of -1')
                u = [b_k ** i for i in range(n)]
                lam = sum(emb(cs[i]) * b_k ** i for i in range(n))
                cu = [sum(u[j] * CL[j][i] for j in range(n)) for i in range(n)]
                # row vector u times c (c acts on row vectors) or c times column
                cu2 = [sum(CL[i][j] * u[j] for j in range(n)) for i in range(n)]
                check(cu == [lam * e for e in u] or cu2 == [lam * e for e in u],
                      'u_k is an eigenvector with eigenvalue lambda_k')
                prod *= lam
            check(prod == emb(mdet(C)), 'det c = prod lambda_k')
            prod2 = L(1)
            for k in range(n // 2):
                b_k = bk[k]
                v = [b_k ** i if i % 2 == 0 else L(0) for i in range(n)]
                w = [b_k ** (i - 1) if i % 2 == 1 else L(0) for i in range(n)]
                u = [b_k ** i for i in range(n)]
                check([v[i] + b_k * w[i] for i in range(n)] == u, 'C383: u_k = v_k + b_k w_k')
                check(all((b_k ** 2) ** j in [emb(e) for e in K] for j in range(n)),
                      'C383: b_k^2 in F_q')
                alpha = sum(emb(cs[2 * j]) * b_k ** (2 * j) for j in range(n // 2))
                beta = sum(emb(cs[2 * j + 1]) * b_k ** (2 * j) for j in range(n // 2))
                lam = sum(emb(cs[i]) * b_k ** i for i in range(n))
                check(alpha + b_k * beta == lam, 'C384: lambda_k = alpha_k + b_k beta_k')
                if n >= 4 and k != 2:
                    # printed: beta_k = c_1 + c_3 b_3^2 + ... (b_3 = bk[2])
                    beta_printed = beta - emb(cs[3]) * b_k ** 2 + emb(cs[3]) * bk[2] ** 2
                    printed_beta_ok = printed_beta_ok and alpha + b_k * beta_printed == lam
                cv = [sum(CL[i][j] * v[j] for j in range(n)) for i in range(n)]
                cw = [sum(CL[i][j] * w[j] for j in range(n)) for i in range(n)]
                vr = [sum(v[j] * CL[j][i] for j in range(n)) for i in range(n)]
                wr = [sum(w[j] * CL[j][i] for j in range(n)) for i in range(n)]
                blk = ([alpha * v[i] + b_k ** 2 * beta * w[i] for i in range(n)],
                       [beta * v[i] + alpha * w[i] for i in range(n)])
                check((vr, wr) == blk or (cv, cw) == blk,
                      'the block (alpha, beta; b^2 beta, alpha) on <v_k, w_k>')
                prod2 *= alpha ** 2 - b_k ** 2 * beta ** 2
            check(prod2 == emb(mdet(C)), 'det c = prod (alpha_k^2 - b_k^2 beta_k^2)')
        # (c_i) -> (alpha_k, beta_k) is invertible over F_q
        rows = []
        for k in range(n // 2):
            b2 = (bL * aL ** k) ** 2
            rows.append([b2 ** (i // 2) if i % 2 == 0 else L(0) for i in range(n)])
            rows.append([b2 ** (i // 2) if i % 2 == 1 else L(0) for i in range(n)])
        check(mdet(rows) != 0, '(c_i) -> (alpha_k, beta_k) invertible')
    refuted(printed_beta_ok, 'C384 printed: beta_k with c_3 b_3^2')


def section_7_forms():
    # quadratic forms over F_q, q odd.
    for q in [q for q in range(3, 50) if ZZ(q).is_prime_power() and q % 2]:
        K = GF(q, 'z')
        els = list(K)
        sq = {e * e for e in els}
        for e in els:
            if e != 0:
                vals = {x1 * x1 + e * x2 * x2 for x1 in els for x2 in els}
                check(vals == set(els), 'x_1^2 + %s x_2^2 takes all values, q = %d' % (e, q))
        check(any(s1 + s2 not in sq for s1 in sq for s2 in sq),
              'squares with 0 are not closed under addition, q = %d' % q)
        nonsq = {e for e in els if e != 0 and e not in sq}
        check(any(x1 * x1 + x2 * x2 in nonsq for x1 in els for x2 in els),
              'p. 229 corrected: x_1^2 + x_2^2 in F_q^* \\ (F_q^*)^2 for some pair, q = %d' % q)
        zero_pair = any(x1 * x1 + x2 * x2 == 0 for x1 in els for x2 in els if x1 != 0)
        check(zero_pair == (q % 4 == 1), 'x_1^2 + x_2^2 = 0 with x != 0 iff q = 1 mod 4')


def section_7_psl_gap():
    # GAP: multipliers of PSL(n, q) and the commutators [y, w].
    for (n, q) in [(2, 5), (2, 7), (2, 8), (2, 11), (2, 13), (2, 16), (2, 17), (2, 19),
                   (3, 3)]:
        M = canon([ZZ(x) for x in libgap.AbelianInvariantsMultiplier(gap('PSL(%d,%d)' % (n, q)))])
        check(M == canon([gcd(n, q - 1)]), 'H_2 PSL(%d,%d) = Z_d' % (n, q))
    for (n, q) in [(2, 4), (2, 9), (3, 2), (3, 4), (4, 2)]:
        M = canon([ZZ(x) for x in libgap.AbelianInvariantsMultiplier(gap('PSL(%d,%d)' % (n, q)))])
        check(M != canon([gcd(n, q - 1)]), 'exception (%d,%d): H_2 != Z_d' % (n, q))
    comm_check = gap('''function(n, q)
      local N, Z, y, i, hom, xb, C, W;
      N := SL(n, q);
      Z := Centre(N);
      y := NullMat(n, n, GF(q));
      y[1][n] := (-1)^(n-1) * One(GF(q));
      for i in [2..n] do y[i][i-1] := One(GF(q)); od;
      hom := NaturalHomomorphismByNormalSubgroup(N, Z);
      xb := Image(hom, y);
      C := Centralizer(Image(hom), xb);
      W := PreImage(hom, C);
      return Subgroup(N, List(GeneratorsOfGroup(W), w -> Comm(y, w))) = Z;
    end''')
    for (n, q) in [(2, 5), (2, 7), (2, 11), (2, 13), (2, 17), (3, 7), (4, 3)]:
        check(bool(comm_check(n, q)),
              'prop 7.7: [y, w] (w over C_N(x)) generate Z(SL(%d,%d))' % (n, q))


def section_7_c_product():
    # exc:c-direct-product-derived (C386).
    names = ['u%d%d' % (i, j) for i in range(3) for j in range(3)]
    F9 = libgap.FreeGroup(names)
    gg = libgap.GeneratorsOfGroup(F9)
    gen = lambda i, j: gg[3 * (i % 3) + (j % 3)]
    rels = []
    for i in range(3):
        for j in range(3):
            for k in range(3):
                for l in range(3):
                    # (u_k, v_l)^-1 (u_i, v_j) (u_k, v_l) = (u_k^-1 u_i u_k, v_l^-1 v_j v_l)
                    rels.append(gen(k, l) ** -1 * gen(i, j) * gen(k, l)
                                * gen(2 * k - i, 2 * l - j) ** -1)
    for kk in (6, 12):
        Q = F9 / libgap(rels + [gen(0, 0) ** kk])
        size = int(libgap.Size(Q))
        D = libgap.DerivedSubgroup(Q)
        check(size == 27 * kk and int(libgap.Size(D)) == 27
              and not bool(libgap.IsAbelian(D)) and int(libgap.NilpotencyClassOfGroup(D)) == 2,
              'exc. 4.7.3: (G x_C G)\' of order 27, class 2 (t^%d = 1)' % kk)
        check(libgap.IdGroup(D) == libgap([27, 3]), '(G x_C G)\' = Heisenberg mod 3')
    Fw = libgap.FreeGroup(['w', 'a'])
    w, a = libgap.GeneratorsOfGroup(Fw)
    Gw = Fw / libgap([w ** -1 * a * w * a, a ** 3, w ** 6])
    check(int(libgap.Size(libgap.DerivedSubgroup(Gw))) == 3,
          'G\' = Z_3, so |G\' x G\'| = 9 != 27')
    # the conjugation rule used above: (w a^j)^-1 (w a^i) (w a^j) = w a^(2j - i)
    wG, aG = libgap.GeneratorsOfGroup(Gw)
    for i in range(3):
        for j in range(3):
            lhs = (wG * aG ** j) ** -1 * (wG * aG ** i) * (wG * aG ** j)
            check(lhs == wG * aG ** ((2 * j - i) % 3), 'conjugation rule on X')


def section_7():
    section_7_cyclic()
    section_7_eigen()
    section_7_psl_construction()
    section_7_negacyclic()
    section_7_forms()
    section_7_psl_gap()
    section_7_c_product()


# ---------------------------------------------------------------------------
# Section 8: F / [F, N'] (pp. 231-241)
# ---------------------------------------------------------------------------

class GroupRingModules:
    """Free G-module P = (Z G)^r, its exterior and symmetric squares."""

    def __init__(self, FG, r):
        self.FG = FG
        self.r = r
        self.N = FG.n * r
        self.basis = [(j, g) for j in range(r) for g in range(FG.n)]   # e_j g
        self.idx = {b: i for i, b in enumerate(self.basis)}

    def act(self, i, h):
        j, g = self.basis[i]
        return self.idx[(j, self.FG.mul[g][h])]

    def wedge_space(self):
        pairs = list(itertools.combinations(range(self.N), 2))
        return pairs, {p: k for k, p in enumerate(pairs)}

    def wedge_coinv(self):
        pairs, pidx = self.wedge_space()
        rels = []
        for h in self.FG.gens:
            for (i, j) in pairs:
                v = [0] * len(pairs)
                v[pidx[(i, j)]] -= 1
                a, b = self.act(i, h), self.act(j, h)
                if a != b:
                    if a < b:
                        v[pidx[(a, b)]] += 1
                    else:
                        v[pidx[(b, a)]] -= 1
                rels.append(vector(ZZ, v))
        V = ZZ ** len(pairs)
        return V, V.submodule(rels), pairs, pidx

    def wedge_vec(self, s, t, pidx, dim):
        """s ^ t for s, t in P given as dicts index -> coeff."""
        v = [0] * dim
        for i, a in s.items():
            for j, b in t.items():
                if i < j:
                    v[pidx[(i, j)]] += a * b
                elif j < i:
                    v[pidx[(j, i)]] -= a * b
        return vector(ZZ, v)


def section_8():
    # th:free-central-torsion-orders on finite groups (Cayley model).
    cases = []
    for order in range(2, 13):
        for i in range(1, int(libgap.NumberSmallGroups(order)) + 1):
            G = libgap.SmallGroup(order, i)
            P = libgap.Image(libgap.IsomorphismPermGroup(G))
            mg = list(libgap.MinimalGeneratingSet(P))
            gens = mg + [libgap.One(P)] * (2 - len(mg)) if len(mg) < 2 else mg
            if len(mg) == 1:
                gens = [mg[0], mg[0] ** 2] if int(libgap.Order(mg[0])) > 2 else [mg[0], mg[0]]
            cases.append(('SmallGroup(%d,%d)' % (order, i), P, gens, order))
    for name in ['SmallGroup(4,2)', 'SmallGroup(8,5)', 'SmallGroup(8,3)', 'SmallGroup(6,1)',
                 'SmallGroup(9,2)', 'SmallGroup(3,1)', 'SmallGroup(8,4)', 'SmallGroup(12,3)',
                 'SmallGroup(7,1)']:
        G = gap(name)
        P = libgap.Image(libgap.IsomorphismPermGroup(G))
        mg = list(libgap.MinimalGeneratingSet(P))
        gens = mg + [mg[0] ** 2] * (3 - len(mg)) if len(mg) < 3 else mg
        cases.append((name + ' (3 generators)', P, gens, int(libgap.Size(P))))
    for name, P, gens, order in cases:
        cay = Cayley(P, gens)
        V, W, _ = wedge_coinvariants(cay)
        tors = [d for d in canon((V / W).invariants()) if d]
        check(all(4 % d == 0 for d in tors),
              'th 8.1: torsion of N\'/[F,N\'] has exponent | 4, %s' % name)
        if order % 2 == 1:
            check(tors == [], 'cor 8.6 / exc. 4.8.5: no torsion for odd order, %s' % name)
    # prop:order-four-element in the Cayley model of Z_2^2.
    P = gap('Group((1,2),(3,4))')
    cay = Cayley(P, list(libgap.GeneratorsOfGroup(P)))
    V, W, T = wedge_coinvariants(cay)
    s_word = [(0, -1), (1, -1), (0, 1), (1, 1)]          # [x, y]
    t_word = [(1, 1), (1, 1)]                            # y^2
    zs, end1 = cay.trace(s_word)
    zt, end2 = cay.trace(t_word)
    check(end1 == cay.one and end2 == cay.one, 's, t in N')
    st = wedge(cay.coords(zs), cay.coords(zt))
    Q = V / W
    check(Q(st).additive_order() == 4, 'prop 8.9: [[x,y], y^2] has order 4 in F/[F,N\']')
    # compound2 is the action on wedges
    for t in T:
        a, b = cay.coords(zs), cay.coords(zt)
        check(wedge(a * t, b * t) == st * compound2(t), 'Lambda^2 of the action')

    # the Magnus embedding computation (C398, C402).
    G = gap('Group((1,2),(3,4))')
    FG = FinGroup(G)
    A_, B_ = [FG.index(g) for g in libgap.GeneratorsOfGroup(G)]
    one = FG.one
    ab = FG.mul[A_][B_]
    PM = GroupRingModules(FG, 2)
    V, W, pairs, pidx = PM.wedge_coinv()
    dim = len(pairs)
    Q = V / W
    check(canon(Q.invariants()) == canon([0] * 4 + [2] * 6), '(P ^ P)_G = Z^4 + Z_2^6')
    e = lambda j, g: PM.idx[(j, g)]

    def el(*terms):
        out = {}
        for c, j, g in terms:
            out[e(j, g)] = out.get(e(j, g), 0) + c
        return out
    s_img = el((1, 0, B_), (-1, 0, one), (-1, 1, A_), (1, 1, one))   # e1(b-1) - e2(a-1)
    t_img = el((1, 1, B_), (1, 1, one))                              # e2(b+1)
    first = PM.wedge_vec(el((1, 0, B_), (-1, 0, one)), t_img, pidx, dim)
    second = PM.wedge_vec(el((1, 1, A_), (-1, 1, one)), t_img, pidx, dim)
    nu = PM.wedge_vec(s_img, t_img, pidx, dim)
    check(Q(first) == 0, 'C398: (e1(b-1) ^ e2(b+1)) (x) 1 = 0')
    corrected = PM.wedge_vec(el((1, 1, one)), el((1, 1, ab)), pidx, dim) \
        + PM.wedge_vec(el((1, 1, A_)), el((1, 1, one)), pidx, dim) \
        - PM.wedge_vec(el((1, 1, one)), el((1, 1, B_)), pidx, dim)
    printed = PM.wedge_vec(el((1, 1, one)), el((1, 1, ab)), pidx, dim)
    check(Q(second) == Q(corrected), 'C398: the second summand = corrected expression')
    refuted(Q(second) == Q(printed) or Q(second) == -Q(printed),
            'C398 printed: second summand = (e2 ^ e2 ab) (x) 1')
    check(Q(nu).additive_order() == 2, 'prop 8.7: nu((s ^ t) (x) 1) has order 2')
    # (I ^ I)_G with I = <a - 1, b + 1>: basis b+1, a-1, (b+1)a.
    n = FG.n

    def ring(*terms):
        v = [0] * n
        for c, g in terms:
            v[g] += c
        return vector(ZZ, v)
    B1 = ring((1, B_), (1, one))
    A1 = ring((1, A_), (-1, one))
    BA = ring((1, FG.mul[B_][A_]), (1, A_))
    basis = matrix(ZZ, [B1, A1, BA])

    def rmul(v, h):
        w = [0] * n
        for g, c in enumerate(v):
            if c:
                w[FG.mul[g][h]] += c
        return vector(ZZ, w)

    def coords(v):
        sol = basis.solve_left(v)
        assert all(c in ZZ for c in sol)
        return [ZZ(c) for c in sol]
    # I is a Z-lattice of rank 3 closed under the action
    for v in (B1, A1, BA):
        for h in (A_, B_):
            coords(rmul(v, h))
    # wedge basis c1 = (a-1)^(b+1), c2 = (b+1)a ^ (b+1), c3 = (a-1) ^ (b+1)a
    wpairs = {(1, 0): ('c1', 1), (0, 1): ('c1', -1), (2, 0): ('c2', 1), (0, 2): ('c2', -1),
              (1, 2): ('c3', 1), (2, 1): ('c3', -1)}

    def wedgeI(u, v):
        cu, cv = coords(u), coords(v)
        out = {'c1': 0, 'c2': 0, 'c3': 0}
        for i in range(3):
            for j in range(3):
                if i != j:
                    name, sg = wpairs[(i, j)]
                    out[name] += sg * cu[i] * cv[j]
        return vector(ZZ, [out['c1'], out['c2'], out['c3']])
    check(rmul(B1, B_) == B1 and rmul(A1, A_) == -A1 and rmul(A1, B_) == BA - A1 - B1,
          'p. 239: (b+1)b = b+1, (a-1)a = 1-a, (a-1)b = (b+1)a - (a-1) - (b+1)')
    gensI = [B1, A1, BA]
    rels6 = []
    rels_all = []
    for h in (A_, B_):
        for i in range(3):
            for j in range(3):
                # (m_1 ^ m_2) h = m_1 h ^ m_2 h; with h^2 = 1: m_1 h ^ m_2 = m_1 ^ m_2 h
                r = wedgeI(rmul(gensI[i], h), rmul(gensI[j], h)) - wedgeI(gensI[i], gensI[j])
                rels_all.append(r)
                if i < j:
                    rels6.append(wedgeI(rmul(gensI[i], h), gensI[j])
                                 - wedgeI(gensI[i], rmul(gensI[j], h)))
    VI = ZZ ** 3
    QI = VI / VI.submodule(rels_all)
    QI6 = VI / VI.submodule(rels6)
    check(canon(QI.invariants()) == [4], 'p. 240: (I ^ I)_G = Z_4')
    check(canon(QI6.invariants()) == [4], 'p. 240: the six relations already give Z_4')
    c1, c2, c3 = VI.basis()
    check(QI(c1).additive_order() == 4, 'c_1 generates (I ^ I)_G')
    check(QI(c2) == QI(2 * c1) and QI(c3) == QI(-c1) and QI(c2) == QI(2 * c3),
          'p. 240: c_2 = 2 c_1, c_3 = -c_1, c_2 = 2 c_3')
    check(wedgeI(rmul(A1, B_), B1) == c2 - c1 and wedgeI(A1, rmul(B1, B_)) == c1,
          'p. 239: (a-1)b ^ (b+1) = c_2 - c_1, (a-1) ^ (b+1)b = c_1')
    f_st = wedgeI(-A1, B1)                                 # (1 - a) ^ (b + 1)
    check(QI(f_st) == QI(-c1) and QI(f_st).additive_order() == 4,
          'C402: f(s ^ t) = -c_1, of order 4')
    refuted(QI(f_st) == QI(c1), 'C402 printed: f(s ^ t) = c_1')

    # lem:exterior-involution-order-two.
    for name in ['CyclicGroup(IsPermGroup, 2)', 'Group((1,2),(3,4))', 'SymmetricGroup(3)',
                 'Group((1,2),(1,3)(2,4))']:
        FG = FinGroup(gap(name))
        PM = GroupRingModules(FG, 1)
        V, W, pairs, pidx = PM.wedge_coinv()
        Q = V / W
        rng = random.Random(4008)
        for c in FG.involutions():
            for _ in range(15):
                m = {i: rng.randint(-2, 2) for i in range(FG.n)}
                mc = {}
                for i, a in m.items():
                    mc[PM.act(i, c)] = mc.get(PM.act(i, c), 0) + a
                x = PM.wedge_vec(m, mc, pidx, len(pairs))
                check(Q(2 * x) == 0, 'lem 8.8: 2 (m ^ m c) (x) 1 = 0, %s' % name)

    # exc:exterior-square-free-cyclic / -coinvariants; lem:symmetric-square-free-cyclic.
    for name in ['CyclicGroup(IsPermGroup, 2)', 'Group((1,2),(3,4))', 'CyclicGroup(IsPermGroup, 4)',
                 'SymmetricGroup(3)', 'Group((1,2),(1,3)(2,4))', 'SmallGroup(8,4)',
                 'CyclicGroup(IsPermGroup, 6)', 'AlternatingGroup(4)']:
        FG = FinGroup(gap(name))
        invs = FG.involutions()
        for r in (1, 2):
            PM = GroupRingModules(FG, r)
            V, W, pairs, pidx = PM.wedge_coinv()
            Q = V / W
            inv = canon(Q.invariants())
            two = [d for d in inv if d]
            check(two == [2] * (r * len(invs)),
                  'exc. 4.8.2: torsion Z_2^(r i), %s, r = %d' % (name, r))
            els = [Q(PM.wedge_vec({PM.idx[(j, FG.one)]: 1}, {PM.idx[(j, g)]: 1},
                                  pidx, len(pairs))) for j in range(r) for g in invs]
            check(all(x.additive_order() == 2 for x in els), 'basis elements of order 2')
            # independence of the classes: the subgroup they generate has order 2^(r i)
            sub = Q.submodule(els) if els else None
            if els:
                check(sub.cardinality() == 2 ** len(els),
                      'exc. 4.8.2: (e_j ^ e_j g) (x) 1 independent, %s' % name)
        # (R o R)_G free of rank #orbits of unordered pairs {g, h} (with g = h)
        n = FG.n
        spairs = [(i, j) for i in range(n) for j in range(i, n)]
        sidx = {p: k for k, p in enumerate(spairs)}
        rels = []
        for h in FG.gens:
            for (i, j) in spairs:
                v = [0] * len(spairs)
                v[sidx[(i, j)]] -= 1
                a, b = FG.mul[i][h], FG.mul[j][h]
                v[sidx[(min(a, b), max(a, b))]] += 1
                rels.append(vector(ZZ, v))
        inv_ror = canon(((ZZ ** len(spairs)) / (ZZ ** len(spairs)).submodule(rels)).invariants())
        orbits = 1 + (n - 1 - len(invs)) // 2 + len(invs)
        check(inv_ror == [0] * orbits,
              'lem 8.3: (R o R)_G = Z^(#orbits) (free + induced from <g>, g^2 = 1), %s' % name)
    # lem:augmentation-symmetric-square-homology: the exact sequence (4.?)
    for name in ['SymmetricGroup(3)', 'CyclicGroup(IsPermGroup, 4)', 'SmallGroup(8,4)',
                 'Group((1,2),(3,4))', 'CyclicGroup(IsPermGroup, 3)', 'AlternatingGroup(4)']:
        FG = FinGroup(gap(name))
        n = FG.n
        spairs = [(i, j) for i in range(n) for j in range(i, n)]
        # R o R -> R: g o h -> eps(g) h + g eps(h) = g + h
        M = zero_matrix(ZZ, n, len(spairs))
        for k, (i, j) in enumerate(spairs):
            M[i, k] += 1
            M[j, k] += 1
        img = (ZZ ** n).submodule(M.columns())
        L = (ZZ ** n).submodule([vector(ZZ, [1 if t == g else (-1 if t == FG.one else 0)
                                             for t in range(n)]) for g in range(n) if g != FG.one]
                                + [vector(ZZ, [2 if t == FG.one else 0 for t in range(n)])])
        check(img == L, 'lem 8.5: image = Delta + 2 Z, %s' % name)
        check(canon(((ZZ ** n) / img).invariants()) == [2], 'lem 8.5: cokernel Z_2')
        # kernel = Delta o Delta: (g-1) o (h-1) = g o h - g o 1 - 1 o h + 1 o 1
        ker = M.right_kernel()
        dd = []
        for g in range(n):
            for h in range(n):
                if g == FG.one or h == FG.one:
                    continue
                v = [0] * len(spairs)
                for (a, b, c) in [(g, h, 1), (g, FG.one, -1), (FG.one, h, -1),
                                  (FG.one, FG.one, 1)]:
                    v[sidx_lookup(a, b, n)] += c
                dd.append(vector(ZZ, v))
        DD = (ZZ ** len(spairs)).submodule(dd)
        check(DD == ker, 'lem 8.5: kernel = Delta o Delta, %s' % name)


def sidx_lookup(a, b, n):
    i, j = min(a, b), max(a, b)
    # index of (i, j) in [(i, j) for i in range(n) for j in range(i, n)]
    return i * n - i * (i - 1) // 2 + (j - i)


def main():
    section_5()
    section_6()
    section_7()
    section_8()
    print('ok %s: %d checks' % (SCOPE, COUNT[0]))


if __name__ == '__main__':
    main()
