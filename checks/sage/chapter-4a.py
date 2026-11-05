"""Exact checks of Chapter 4 "Homology and the functor Tor", §§ 1-4 (Sage).

Run from the project root: sage -python checks/sage/chapter-4a.py (plain
asserts; do not use -O).  The last line is "ok chapter-4a: N checks".

Book: Yu. V. Kuzmin, Homological group theory (Factorial Press, Moscow,
2006), chapter 4, §§ 1-4, printed pp. 171-203; §§ 5-8 are checked in
chapter-4b.py.  Pages are printed pages; labels are those of
content/04-*.typ.  Expected values are the book's; where the book is wrong
the printed reading is kept as a refuted check (`refuted`) beside the
corrected one.  Exact arithmetic only: integer matrices, Sage's f.g. modules
over ZZ (Smith normal form), GAP through libgap (core library only).

Free resolutions of finite groups are built here (`FreeResolution`): the
generators of X_(k+1) are chosen in the kernel lattice of d_k until their
G-translates span it over Z (index 1), so exactness holds by construction.
The homology of a complex of f.g. abelian groups C_n = Z^(a_n) / L_n with
maps given by integer matrices D_n is computed as
{x : D_n x in L_(n-1)} / (D_(n+1) Z^(a_(n+1)) + L_n) (`fg_homology`); with
L_n = 0 this is the integral homology, with L_n = m Z^(a_n) the homology
with coefficients in Z_m.

What is checked, by section:

section_1 (pp. 171-181, Tor):
  * the tensor product of complexes (4.5): with the sign (-1)^i the total
    differential squares to zero, without it not (random complexes over Z
    of length 2); the transposition x (x) y -> (-1)^(ij) y (x) x is a chain
    map, without the sign it is not;
  * lem:tensor-resolutions-homology over Z: for 30 pairs of finite abelian
    groups B, A given by random non-diagonal presentation matrices,
    H_n(X (x) Y) = H_n(X (x) A) = H_n(B (x) Y) = B (x) A, Tor(B, A), 0 for
    n = 0, 1, 2 (X -> B, Y -> A the presentations), against the cyclic
    decompositions; in particular Tor(B, Z_n) is the n-torsion of B
    (p. 180);
  * exc:tensor-homotopy: for complexes X, Y of length 2 over Z (X != Y),
    chain maps f, f' : X -> X and phi, phi' : Y -> Y with homotopies
    f - f' = d s + s d, phi - phi' = d t + t d, the map
    D(x (x) y) = s(x) (x) phi(y) + (-1)^k f'(x) (x) t(y) satisfies
    d D + D d = f (x) phi - f' (x) phi' (20 random cases); without (-1)^k
    it fails.  So the formula holds for maps X -> X', Y -> Y' as used on
    p. 176 (our corrected typing of the exercise);
  * exc:tor-diagonal-counterexample (C302): Tor_1(Z (x) Z_n, Z_n) = Z_n,
    Tor_1(Z, Z_n (x) Z_n) = 0, n = 2..12;
  * exc:flat-extensions-converse: 0 -> Z -2-> Z -> Z_2 -> 0 with
    Tor_1(Z_2, Z_2) = Z_2 != 0.
section_2 (pp. 181-190, homology of groups):
  * H_n(Z_m) = Z_m (n odd), 0 (n even > 0) from the periodic resolution,
    m <= 12, n <= 9, and from the resolution built here, m <= 8, n <= 5;
  * prop:induced-module-homology-vanishes: H_n(G, Z G (x) Z_k) = 0, n > 0
    (Z_m with the periodic resolution, m, k <= 6, n <= 5; S_3, Q_8, Z_2^2,
    k = 2, 3, 4, n <= 3); with trivial Z_k it is not 0;
  * prop:homology-induced-from-subgroup (Shapiro) for ten pairs S <= G of
    order <= 10: H_n(G, Z[G/S]) = H_n(S, Z), n <= 3 (two independent
    resolutions, of G and of S);
  * prop:finite-group-homology-exponent: the exponent of H_n(G, Z) divides
    |G| for all groups of order <= 12, n <= 3; there also H_1 G = G_ab
    (exc:h1-standard-complex) and H_2 G = GAP's AbelianInvariantsMultiplier;
  * exc:restriction-transfer and exc:sylow-restriction-injective: the
    transfer V(g) = prod_i h_i(g) (t_i g = h_i(g) t_j) is a homomorphism
    G -> S_ab, its composite with S_ab -> G_ab is g -> g^[G:S], and for a
    Sylow p-subgroup S it is injective on the p-part of G_ab (twelve groups,
    all subgroups up to conjugacy, resp. all Sylow subgroups);
  * exc:cyclic-chain-equivalence: the printed f(e_n) is a chain map from
    the periodic resolution of Z_m (C316) to the standard resolution of
    § 2.1, which is normalized ((g_1, ..., g_n) = 0 if some g_i = 1), and
    also to the unnormalized bar resolution (m <= 6, n <= 6);
  * exc:cyclic-inversion-action: the hint (C319, a^i not a_i) for k = 1:
    the boundary of the printed chain is c_1 o x - c_1 exactly in the
    normalized standard complex (in the unnormalized one only up to a
    degenerate cycle); with a chain map g from the standard resolution to
    the periodic one (built from a contracting homotopy, checked to be a
    chain map), x acts on H_(2k+1) = Z_m by (-1)^(k+1) (k <= 3, m = 3..7),
    and an automorphism a -> a^r by r^(k+1);
  * exc:inverting-extension-homology: with this action the HNN sequence of
    p. 184 gives H_n(Z_m x| Z) = Z_m for n = 0, 3 mod 4 (n > 0) and 0 for
    n = 1, 2 mod 4 (n > 1) for odd m <= 15, n <= 12, and H_1 = Z; G_ab
    from GAP agrees;
  * exc:dyadic-rationals-cd: the printed hint x_(i+1)^2 = x_i e gives a
    split extension (x_i -> 1, e -> 1 is a retraction onto <e>): refuted;
    the corrected x_(i+1)^2 = x_i e^((-1)^i) gives an extension of Z[1/2]
    by Z = <e> that does not split: a retraction would need an integer n_0
    with 3 n_0 = -1 (mod 2^k) for all k (checked k <= 64 from the
    recursion 2 n_(i+1) = n_i + eps_i), i.e. n_0 = -1/3; split exactly
    when the 2-adic number sum eps_i 2^i is an integer (checked on twelve
    periodic sign patterns).
section_3 (pp. 190-193, universal coefficients): for ten groups of order
  <= 12 (resolutions built here, H_1 and H_2 checked against GAP) and
  m in {2, 3, 4, 6, 8, 9, 12}, n <= 4:
  H_n(G, Z_m) = H_n G (x) Z_m + Tor(H_(n-1) G, Z_m)
  (th:universal-coefficients-homology), H^n(G, Z_m) = Ext(H_(n-1) G, Z_m)
  + Hom(H_n G, Z_m) (th:universal-coefficients-cohomology), H^n(G, Z_m) =
  H^n G (x) Z_m + Tor(H^(n+1) G, Z_m) for n <= 3
  (exc:cohomology-universal-coefficients-finite-type), and
  dim H^n(G, F_p) = dim H_n(G, F_p).
section_4 (pp. 193-203, H_2 and relations):
  * prop:hopf-formula computed independently of the book's proof: for
    G = F / N with F free on a generating set of G, N_ab is the cycle space
    of the Cayley graph, conjugation is the translation action, so
    N / [N, F] = (cycle space)_G and its map to F / F' counts the edge
    labels; the kernel (N cap F') / [N, F] has the invariants of GAP's
    AbelianInvariantsMultiplier for all groups of order <= 31 and for A_5,
    SL(2, 5), PSL(2, 7), A_6, and N / [N, F] = H_2 G + Z^r (C332); the
    images of the relators of a presentation generate N / [N, F]
    (prop:relations-number-bound) for all groups of order <= 24;
  * the five-term sequence (prop:five-term-sequence): for every group of
    order <= 24 and every normal subgroup N,
    |N / [G, N]| = |Coker(H_2 G -> H_2(G / N))| |Ker(G_ab -> (G/N)_ab)|,
    the map H_2 G -> H_2(G / N) computed on the Cayley graphs with one free
    group F;
  * basic commutators (p. 195): the basic commutators of weight n on r
    generators by Hall's definition are M_r(n) in number (Witt's formula)
    and their Lie elements in the free associative ring over Z form a
    Z-basis of the lattice spanned by all left-normed brackets of degree n
    (r = 1, n <= 6; r = 2, n <= 7; r = 3, n <= 5; r = 4, n <= 4); weight 3
    is [[x_i, x_j], x_k], i > j <= k, (r^3 - r) / 3 in number; the printed
    recursive definition (u > v <= w only) admits [[y, x], [y, x]] = 1 and
    gives too many commutators at weight 4 and 5 (refuted); the corrected
    one ([u, v] basic and [u, v] > w >= v) gives exactly Hall's commutators
    (r = 2, 3, n <= 5).  The identification gamma_n F / gamma_(n+1) F =
    L_n (Magnus, Witt) is cited, not checked;
  * the commutator identities of exc:free-nilpotent-class-two-relations
    (C347) in the free group: [a, b]^(-1) = [b, a], [a b, c] = [a, c]^b
    [b, c], [a, b, c^a][c, a, b^c][b, c, a^b] = 1;
  * exc:metabelian-h2-zero: <x, y | x^(-1) y x = y^2> has G_ab = Z and its
    relator is not in F' (H_2 = 0, p. 195);
  * the remark after prop:free-solvable-infinitely-related (C341, p. 199):
    for G = 1 = F / F (F free of rank 2, orderable G) the free abelian
    extension F / F' = Z^2 = <x, y | [x, y]> is finitely presented, and so
    is F / N' = F for N = 1: the statement needs G != 1 and N != 1 (our
    correction); lem:ordered-exterior-square-free on boxes of Z and Z^2
    (lexicographic order): every pair {u, v} is {g h, h} for exactly one
    g > 1, so the (g ^ 1) h form a basis.

What this does NOT establish: the general theorems (only the listed groups,
complexes, ranks and degrees are covered); the Hopf formula and the
five-term sequence only for the listed finite groups; Stallings' theorem
and the theorem on lifted relations not at all; basic commutators only for
the listed ranks and weights, and on the Lie side; nothing about the free
product formula of p. 183, the amalgam and HNN sequences (used, not
checked), hd and cd beyond exc:dyadic-rationals-cd, or Lemma 4.4 beyond
finite boxes.  Nothing here compares our text with the printed book.
"""

import itertools
import random

from sage.all import (
    GF, QQ, ZZ, binomial, divisors, gcd, identity_matrix, libgap, matrix,
    moebius, vector, zero_matrix,
)

SCOPE = 'chapter-4a'
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
    """Abelian invariants as sorted prime powers and zeros."""
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


def fg_homology(n, D_out, D_in, rel_n=None, rel_prev=None):
    """H of a complex of f.g. abelian groups at a term Z^n / rel_n.

    D_out: the matrix of the outgoing map (rows: the previous term), or None;
    D_in: the matrix of the incoming map (columns land in Z^n), or None;
    rel_n, rel_prev: matrices whose columns span the relation lattices.
    """
    if n == 0:
        return []
    V = ZZ ** n
    if D_out is None or D_out.nrows() == 0:
        Kgens = identity_matrix(ZZ, n).rows()
    else:
        B = D_out
        if rel_prev is not None and rel_prev.ncols() > 0:
            B = D_out.augment(-rel_prev)
        Kgens = [row[:n] for row in B.right_kernel_matrix().rows()]
    K = V.submodule(Kgens)
    Igens = []
    if D_in is not None and D_in.ncols() > 0:
        Igens += D_in.columns()
    if rel_n is not None and rel_n.ncols() > 0:
        Igens += rel_n.columns()
    I = V.submodule(Igens)
    return canon((K / I).invariants())


def complex_homology(ranks, D, n, rel=None):
    """H_n of sum_n Z^(ranks[n]) / rel[n] with D[n]: C_n -> C_(n-1)."""
    rel = rel or {}
    return fg_homology(ranks[n], D.get(n), D.get(n + 1), rel.get(n),
                       rel.get(n - 1))


# Operations on cyclic decompositions (lists of prime powers and zeros).

def cyc_tensor(A, B):
    return canon([gcd(a, b) for a in A for b in B])


def cyc_tor(A, B):
    return canon([gcd(a, b) for a in A for b in B if a and b])


def cyc_hom(A, B):
    out = []
    for a in A:
        for b in B:
            if a == 0:
                out.append(b)
            elif b != 0:
                out.append(gcd(a, b))
    return canon(out)


def cyc_ext(A, B):
    out = []
    for a in A:
        if a == 0:
            continue
        for b in B:
            out.append(a if b == 0 else gcd(a, b))
    return canon(out)


def cyc_sum(*args):
    return canon([x for a in args for x in a])


def smith_invariants(P):
    """Invariants of Z^k / P Z^k."""
    return canon([d for d in P.smith_form()[0].diagonal()]
                 + [0] * (P.nrows() - P.ncols()))


# ---------------------------------------------------------------------------
# Section 1: Tor (pp. 171-181)
# ---------------------------------------------------------------------------

def random_complex(rng, ranks):
    """A complex Z^(r_2) -> Z^(r_1) -> Z^(r_0) with random maps, d d = 0."""
    a0, a1, a2 = ranks
    d2 = matrix(ZZ, a1, a2, [rng.randint(-3, 3) for _ in range(a1 * a2)])
    left = d2.transpose().right_kernel_matrix()      # rows v with v d2 = 0
    c = matrix(ZZ, a0, left.nrows(),
               [rng.randint(-2, 2) for _ in range(a0 * left.nrows())])
    d1 = c * left
    assert d1 * d2 == 0
    return {'r': list(ranks), 'd': {1: d1, 2: d2}}


def tot_basis(X, Y, n):
    out = []
    for i in range(len(X['r'])):
        j = n - i
        if 0 <= j < len(Y['r']):
            out.extend((i, j, p, q) for p in range(X['r'][i])
                       for q in range(Y['r'][j]))
    return out


def tot_d(X, Y, n, sign=True):
    src, dst = tot_basis(X, Y, n), tot_basis(X, Y, n - 1)
    idx = {b: k for k, b in enumerate(dst)}
    M = zero_matrix(ZZ, len(dst), len(src))
    for col, (i, j, p, q) in enumerate(src):
        if i >= 1:
            d = X['d'][i]
            for r in range(d.nrows()):
                if d[r, p]:
                    M[idx[(i - 1, j, r, q)], col] += d[r, p]
        if j >= 1:
            d = Y['d'][j]
            s = (-1) ** i if sign else 1
            for r in range(d.nrows()):
                if d[r, q]:
                    M[idx[(i, j - 1, p, r)], col] += s * d[r, q]
    return M


def tensor_map(X, Y, u, du, v, dv, n, koszul=True):
    """(u (x) v)(x (x) y) = (-1)^(dv i) u(x) (x) v(y) on Tot_n -> Tot_(n+du+dv).

    u[i]: matrix X_i -> X_(i+du), v[j]: Y_j -> Y_(j+dv); missing = 0."""
    src, dst = tot_basis(X, Y, n), tot_basis(X, Y, n + du + dv)
    idx = {b: k for k, b in enumerate(dst)}
    M = zero_matrix(ZZ, len(dst), len(src))
    for col, (i, j, p, q) in enumerate(src):
        U, W = u.get(i), v.get(j)
        if U is None or W is None:
            continue
        s = (-1) ** (dv * i) if koszul else 1
        for r in range(U.nrows()):
            if U[r, p]:
                for t in range(W.nrows()):
                    if W[t, q]:
                        M[idx[(i + du, j + dv, r, t)], col] += s * U[r, p] * W[t, q]
    return M


def complex_maps(X, h):
    """f = id + d h + h d (a chain map X -> X) for h: X_i -> X_(i+1)."""
    L = len(X['r'])
    d = X['d']
    f = {}
    for i in range(L):
        M = identity_matrix(ZZ, X['r'][i])
        if i + 1 < L:
            M += d[i + 1] * h[i]
        if i >= 1:
            M += h[i - 1] * d[i]
        f[i] = M
    return f


def random_homotopy(rng, X):
    L = len(X['r'])
    return {i: matrix(ZZ, X['r'][i + 1], X['r'][i],
                      [rng.randint(-2, 2) for _ in range(X['r'][i + 1] * X['r'][i])])
            for i in range(L - 1)}


def section_1():
    rng = random.Random(4001)
    # (4.5): d^2 = 0 with the sign (-1)^i; the transposition tau.
    for trial in range(10):
        X = random_complex(rng, (2, 3, 2))
        Y = random_complex(rng, (2, 2, 3))
        ok = all(tot_d(X, Y, n - 1) * tot_d(X, Y, n) == 0 for n in range(2, 5))
        check(ok, '(4.5): d^2 = 0 on X (x) Y with the sign (-1)^i')
        refuted(all(tot_d(X, Y, n - 1, False) * tot_d(X, Y, n, False) == 0
                    for n in range(2, 5)), '(4.5) without the sign (-1)^i')
        for n in range(1, 5):
            # tau(x (x) y) = (-1)^(ij) y (x) x as a matrix Tot(X,Y)_n -> Tot(Y,X)_n
            for sgn in (True, False):
                src, dst = tot_basis(X, Y, n), tot_basis(Y, X, n)
                idx = {b: k for k, b in enumerate(dst)}
                T = zero_matrix(ZZ, len(dst), len(src))
                for col, (i, j, p, q) in enumerate(src):
                    T[idx[(j, i, q, p)], col] = (-1) ** (i * j) if sgn else 1
                src1, dst1 = tot_basis(X, Y, n - 1), tot_basis(Y, X, n - 1)
                idx1 = {b: k for k, b in enumerate(dst1)}
                T1 = zero_matrix(ZZ, len(dst1), len(src1))
                for col, (i, j, p, q) in enumerate(src1):
                    T1[idx1[(j, i, q, p)], col] = (-1) ** (i * j) if sgn else 1
                comm = tot_d(Y, X, n) * T == T1 * tot_d(X, Y, n)
                if sgn:
                    check(comm, 'p. 178: tau with (-1)^(ij) is a chain map, n = %d' % n)
                elif n == 2:
                    refuted(comm, 'p. 178: tau without the sign is a chain map')

    # lem:tensor-resolutions-homology over Z; Tor(B, Z_n) = n-torsion of B.
    def rand_pres(k):
        while True:
            P = matrix(ZZ, k, k, [rng.randint(-4, 4) for _ in range(k * k)])
            if P.det() != 0 and abs(P.det()) <= 60:
                return P
    for trial in range(30):
        kb, ka = rng.randint(1, 3), rng.randint(1, 2)
        PB = rand_pres(kb)
        if trial < 8:
            PA = matrix(ZZ, 1, 1, [trial + 2])          # A = Z_n
            ka = 1
        else:
            PA = rand_pres(ka)
        Binv, Ainv = smith_invariants(PB), smith_invariants(PA)
        X = {'r': [kb, kb], 'd': {1: PB}}
        Y = {'r': [ka, ka], 'd': {1: PA}}
        ranks = [len(tot_basis(X, Y, n)) for n in range(3)]
        D = {n: tot_d(X, Y, n) for n in (1, 2)}
        H_XY = [complex_homology(ranks, D, n) for n in range(3)]
        # X (x) A: terms (Z^kb (x) Z^ka) / (I (x) PA), map PB (x) I.
        IA, IB = identity_matrix(ZZ, ka), identity_matrix(ZZ, kb)
        relXA = IB.tensor_product(PA)
        DXA = {1: PB.tensor_product(IA)}
        H_XA = [complex_homology([kb * ka] * 2, DXA, n, {0: relXA, 1: relXA})
                for n in range(2)]
        relBY = PB.tensor_product(IA)
        DBY = {1: IB.tensor_product(PA)}
        H_BY = [complex_homology([kb * ka] * 2, DBY, n, {0: relBY, 1: relBY})
                for n in range(2)]
        expect = [cyc_tensor(Binv, Ainv), cyc_tor(Binv, Ainv), []]
        check(H_XY == expect, 'lem 1.2: H(X (x) Y) = B (x) A, Tor(B, A), 0')
        check(H_XA == expect[:2], 'lem 1.2: H(X (x) A) = B (x) A, Tor(B, A)')
        check(H_BY == expect[:2], 'lem 1.2: H(B (x) Y) = B (x) A, Tor(B, A)')
        if trial < 8:
            n = trial + 2
            ntors = canon([gcd(b, n) for b in Binv])
            check(H_XA[1] == ntors, 'p. 180: Tor(B, Z_%d) = %d-torsion of B' % (n, n))

    # exc:tensor-homotopy: d D + D d = f (x) phi - f' (x) phi'.
    for trial in range(20):
        X = random_complex(rng, (2, 3, 2))
        Y = random_complex(rng, (3, 2, 2))
        f = complex_maps(X, random_homotopy(rng, X))
        phi = complex_maps(Y, random_homotopy(rng, Y))
        s, t = random_homotopy(rng, X), random_homotopy(rng, Y)
        dX, dY = X['d'], Y['d']
        f2 = {}
        for i in range(3):
            M = f[i]
            if i + 1 < 3:
                M = M - dX[i + 1] * s[i]
            if i >= 1:
                M = M - s[i - 1] * dX[i]
            f2[i] = M
        phi2 = {}
        for j in range(3):
            M = phi[j]
            if j + 1 < 3:
                M = M - dY[j + 1] * t[j]
            if j >= 1:
                M = M - t[j - 1] * dY[j]
            phi2[j] = M
        for koszul in (True, False):
            good = True
            for n in range(0, 5):
                Dn = (tensor_map(X, Y, s, 1, phi, 0, n)
                      + tensor_map(X, Y, f2, 0, t, 1, n, koszul))
                lhs = tot_d(X, Y, n + 1) * Dn if n + 1 <= 4 else 0
                if n >= 1:
                    Dn1 = (tensor_map(X, Y, s, 1, phi, 0, n - 1)
                           + tensor_map(X, Y, f2, 0, t, 1, n - 1, koszul))
                    lhs = lhs + Dn1 * tot_d(X, Y, n)
                rhs = (tensor_map(X, Y, f, 0, phi, 0, n)
                       - tensor_map(X, Y, f2, 0, phi2, 0, n))
                good = good and (lhs == rhs)
            if koszul:
                check(good, 'exc. 4.1.7: dD + Dd = f(x)phi - f\'(x)phi\'')
            else:
                refuted(good, 'exc. 4.1.7 without the sign (-1)^k')

    # exc:tor-diagonal-counterexample (C302) and exc:flat-extensions-converse.
    for n in range(2, 13):
        X = {1: matrix(ZZ, [[n]])}
        rel = {0: matrix(ZZ, [[n]]), 1: matrix(ZZ, [[n]])}
        t1 = complex_homology([1, 1], X, 1, rel)       # Tor_1(Z_n, Z_n)
        check(t1 == canon([n]), 'exc. 4.1.8: Tor_1(Z (x) Z_n, Z_n) = Z_n')
        t0 = complex_homology([1, 0], {1: matrix(ZZ, 1, 0)}, 1,
                              {0: matrix(ZZ, [[n]])})  # resolution of Z
        check(t0 == [], 'exc. 4.1.8: Tor_1(Z, Z_n (x) Z_n) = 0')
    check(complex_homology([1, 1], {1: matrix(ZZ, [[2]])}, 1,
                           {0: matrix(ZZ, [[2]]), 1: matrix(ZZ, [[2]])}) == [2],
          'exc. 4.1.6: Tor_1(Z_2, Z_2) != 0, Z_2 not flat although Z, Z are')


# ---------------------------------------------------------------------------
# Resolutions: periodic resolution of Z_m; free resolutions of finite groups
# ---------------------------------------------------------------------------

def periodic_complex(m, R, N, rel=None):
    """X (x)_G A for the periodic resolution of G = <a> = Z_m, A = Z^k, a -> R."""
    k = R.nrows()
    Nm = sum((R ** i for i in range(m)), zero_matrix(ZZ, k))
    D = {n: (R - 1 if n % 2 else Nm) for n in range(1, N + 2)}
    ranks = [k] * (N + 2)
    rels = {n: rel for n in range(N + 2)} if rel is not None else None
    return ranks, D, rels


class FinGroup:
    """A finite group from GAP with its multiplication table (indices 0..n-1)."""

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

    def index(self, g):
        return int(libgap.Position(self.elts, g)) - 1


class FreeResolution:
    """A free resolution of the trivial module Z over Z G, built here.

    X_k = (Z G)^(a_k) as left modules, written as Z^(a_k n) with the basis
    g b_i (index i n + g).  X_(k+1) maps onto Ker(X_k -> X_(k-1)): Z G-module
    generators are chosen among elements of the kernel lattice until their G
    translates span it over Z (equality of lattices is asserted), so the
    resolution is exact by construction; d d = 0 is asserted too."""

    def __init__(self, FG, N, seed=1):
        rng = random.Random(seed)
        self.FG = FG
        n = FG.n
        self.dims = [1]
        self.d = {0: matrix(ZZ, 1, n, [1] * n)}
        for k in range(N):
            dk = self.d[k]
            K = dk.right_kernel_matrix().echelon_form()
            rK = K.rank()
            K = K[:rK]
            dim = dk.ncols()
            piv = K.pivots()
            KPinv = K.matrix_from_columns(piv).inverse()
            gens = []
            Lmat = matrix(ZZ, 0, dim)
            rank = 0
            while True:
                rows = list(range(rK))
                rng.shuffle(rows)
                if rank == rK:
                    # L = C K with C integral; the lattices are equal iff
                    # det C = +-1; K row i lies in L iff row i of C^-1 is integral
                    C = Lmat.matrix_from_columns(piv) * KPinv
                    assert C.denominator() == 1
                    if abs(C.det()) == 1:
                        break
                    Cinv = C.inverse()
                    bad = [i for i in rows if Cinv.row(i).denominator() != 1]
                    cands = [K.row(bad[0])]
                else:
                    cands = []
                    for _ in range(4):
                        co = [rng.randint(-1, 1) for _ in range(rK)]
                        v = sum((c * K.row(i) for i, c in enumerate(co) if c),
                                vector(ZZ, dim))
                        if v != 0:
                            cands.append(v)
                    cands += [K.row(i) for i in rows[:4]]
                best = None
                for v in cands:
                    M2 = Lmat.stack(matrix(ZZ, [self.lmul(h, v) for h in range(n)]))
                    score = M2.rank()
                    if best is None or score > best[0]:
                        best = (score, v, M2)
                    if score == rank + n:
                        break
                gens.append(best[1])
                M2 = best[2].echelon_form()
                rank = M2.rank()
                Lmat = M2[:rank]
            cols = [self.lmul(h, v) for v in gens for h in range(n)]
            self.d[k + 1] = matrix(ZZ, cols).transpose()
            assert self.d[k] * self.d[k + 1] == 0
            self.dims.append(len(gens))

    def lmul(self, h, v):
        n = self.FG.n
        w = [0] * len(v)
        mul = self.FG.mul[h]
        for idx, c in v.dict().items():
            i, g = divmod(idx, n)
            w[i * n + mul[g]] += c
        return vector(ZZ, w)

    def complex(self, act, k):
        """X (x)_G A for a left module A = Z^k; act(h) = matrix of h on A.

        X is made a right module by x g = g^(-1) x, so that
        (g b_i) (x) a = b_i (x) g^(-1) a."""
        n = self.FG.n
        one = self.FG.one
        D = {}
        cache = {}
        for m in range(1, len(self.dims)):
            dm = self.d[m]
            M = zero_matrix(ZZ, self.dims[m - 1] * k, self.dims[m] * k)
            for j in range(self.dims[m]):
                col = dm.column(j * n + one)
                for idx, c in col.dict().items():
                    i, g = divmod(idx, n)
                    ginv = self.FG.inv[g]
                    if ginv not in cache:
                        cache[ginv] = act(ginv)
                    M.set_block(i * k, j * k,
                                M.submatrix(i * k, j * k, k, k) + c * cache[ginv])
            D[m] = M
        return [a * k for a in self.dims], D

    def integral(self):
        return self.complex(lambda h: identity_matrix(ZZ, 1), 1)


def coset_action(FG, S_idx):
    """The left module Z[G/S] (left cosets x S, h . xS = hxS): h -> matrix."""
    S = set(S_idx)
    coset_of = {}
    reps = []
    for x in range(FG.n):
        if x in coset_of:
            continue
        c = len(reps)
        reps.append(x)
        for s in S:
            coset_of[FG.mul[x][s]] = c
    k = len(reps)

    def act(h):
        M = zero_matrix(ZZ, k, k)
        for c, x in enumerate(reps):
            M[coset_of[FG.mul[h][x]], c] = 1
        return M
    return act, k


RES_CACHE = {}

UCT_GROUPS = ['CyclicGroup(4)', 'SmallGroup(4,2)', 'SymmetricGroup(3)', 'SmallGroup(8,2)',
              'SmallGroup(8,3)', 'SmallGroup(8,4)', 'AlternatingGroup(4)', 'SmallGroup(9,2)',
              'SmallGroup(10,1)', 'SmallGroup(12,4)']


def resolution(name, G, N):
    """A free resolution of length >= N of the group G (cached by name)."""
    for (nm, M), R in RES_CACHE.items():
        if nm == name and M >= N:
            return R
    RES_CACHE[(name, N)] = FreeResolution(FinGroup(G), N)
    return RES_CACHE[(name, N)]


def group_homology(name, G, n):
    """H_n(G, Z) from the resolution built here."""
    R = resolution(name, G, n + 1)
    ranks, D = R.integral()
    return complex_homology(ranks, D, n)


# ---------------------------------------------------------------------------
# Standard resolution of Z_m (normalized, as in § 2.1, or unnormalized)
# ---------------------------------------------------------------------------

def bar_d(chain, m, normalized):
    """d on R(G) for G = Z_m, elements a^i written i; keys (g_1..g_n, h)."""
    out = {}
    for key, c in chain.items():
        g, h = key[:-1], key[-1]
        n = len(g)
        terms = [(g[:-1] + ((g[-1] + h) % m,), 1)]
        for i in range(n - 2, -1, -1):          # i = n-1 .. 1 (1-based)
            sgn = (-1) ** (n - (i + 1))
            terms.append((g[:i] + ((g[i] + g[i + 1]) % m,) + g[i + 2:] + (h,), sgn))
        terms.append((g[1:] + (h,), (-1) ** n))
        for k2, s in terms:
            if normalized and any(x == 0 for x in k2[:-1]):
                continue
            out[k2] = out.get(k2, 0) + s * c
    return {k2: c for k2, c in out.items() if c}


def bar_clean(chain, normalized):
    if not normalized:
        return {k: c for k, c in chain.items() if c}
    return {k: c for k, c in chain.items() if c and all(x != 0 for x in k[:-1])}


def bar_rmul(chain, ring_elt, m):
    """chain * r for r = {exponent: coefficient} in Z G."""
    out = {}
    for key, c in chain.items():
        for e, r in ring_elt.items():
            k2 = key[:-1] + ((key[-1] + e) % m,)
            out[k2] = out.get(k2, 0) + c * r
    return {k: c for k, c in out.items() if c}


def f_periodic(n, m):
    """f(e_n) of exc:cyclic-chain-equivalence (as a chain with h = 1 = a^0)."""
    k = n // 2
    out = {}
    for idx in itertools.product(range(1, m + 1), repeat=k):
        g = []
        for i in idx:
            g += [1 % m, i % m]
        if n % 2:
            g.append(1 % m)
        key = tuple(g) + (0,)
        out[key] = out.get(key, 0) + 1
    return out


def section_2():
    # H_n(Z_m) from the periodic resolution and from the resolution built here.
    for m in range(2, 13):
        D = {n: matrix(ZZ, [[0 if n % 2 else m]]) for n in range(1, 12)}
        for n in range(1, 10):
            H = complex_homology([1] * 12, D, n)
            check(H == (canon([m]) if n % 2 else []),
                  'p. 182: H_%d(Z_%d)' % (n, m))
    for m in range(2, 9):
        for n in range(1, 6):
            check(group_homology('Z%d' % m, libgap.CyclicGroup(libgap.IsPermGroup, m), n)
                  == (canon([m]) if n % 2 else []), 'H_%d(Z_%d), free resolution' % (n, m))

    # prop:induced-module-homology-vanishes.
    for m in range(2, 7):
        P = matrix(ZZ, m, m, lambda i, j: 1 if i == (j + 1) % m else 0)  # a on ZG
        for k in range(2, 7):
            ranks, D, rels = periodic_complex(m, P, 6, k * identity_matrix(ZZ, m))
            for n in range(1, 6):
                check(complex_homology(ranks, D, n, rels) == [],
                      'prop 2.1: H_%d(Z_%d, ZG (x) Z_%d) = 0' % (n, m, k))
            check(complex_homology(ranks, D, 0, rels) == canon([k]),
                  'prop 2.1: H_0 = Z_k')
            ranks, D, rels = periodic_complex(m, identity_matrix(ZZ, 1), 6,
                                              matrix(ZZ, [[k]]))
            if gcd(m, k) > 1:
                refuted(complex_homology(ranks, D, 1, rels) == [],
                        'trivial Z_k: H_1(Z_%d, Z_%d) = 0' % (m, k))
    for name in ['SymmetricGroup(3)', 'SmallGroup(8,4)', 'SmallGroup(4,2)']:
        G = gap(name)
        R = resolution(name, G, 4)
        act, kk = coset_action(R.FG, [R.FG.one])
        ranks, D = R.complex(act, kk)
        for k in (2, 3, 4):
            rels = {n: k * identity_matrix(ZZ, ranks[n]) for n in range(len(ranks))}
            for n in range(1, 4):
                check(complex_homology(ranks, D, n, rels) == [],
                      'prop 2.1: H_%d(%s, ZG (x) Z_%d) = 0' % (n, name, k))

    # prop:homology-induced-from-subgroup (Shapiro).
    pairs = [
        ('SymmetricGroup(3)', 'Group((1,2))'),
        ('SymmetricGroup(3)', 'Group((1,2,3))'),
        ('AlternatingGroup(4)', 'Group((1,2)(3,4),(1,3)(2,4))'),
        ('AlternatingGroup(4)', 'Group((1,2,3))'),
        ('AlternatingGroup(4)', 'Group((1,2)(3,4))'),
        ('Group((1,2,3,4),(1,3))', 'Group((1,2,3,4))'),
        ('Group((1,2,3,4),(1,3))', 'Group((1,3))'),
        ('Group((1,2,3,4,5),(2,5)(3,4))', 'Group((2,5)(3,4))'),
        ('Group((1,2,4,7)(3,6,8,5),(1,3,4,8)(2,5,7,6))', 'Group((1,2,4,7)(3,6,8,5))'),
        ('Group((1,2),(3,4),(5,6))', 'Group((1,2),(3,4))'),
    ]
    for Gs, Ss in pairs:
        G = gap(Gs)
        S = gap(Ss)
        R = resolution(Gs, G, 4)
        S_idx = [R.FG.index(s) for s in libgap.AsList(S)]
        act, k = coset_action(R.FG, S_idx)
        ranks, D = R.complex(act, k)
        for n in range(1, 4):
            check(complex_homology(ranks, D, n) == group_homology(Ss, S, n),
                  'prop 2.2: H_%d(%s, Z[G/S]) = H_%d(%s)' % (n, Gs, n, Ss))

    # prop:finite-group-homology-exponent; exc:h1-standard-complex; H_2 = M(G).
    for order in range(2, 13):
        for i in range(1, int(libgap.NumberSmallGroups(order)) + 1):
            G = libgap.SmallGroup(order, i)
            name = 'SmallGroup(%d,%d)' % (order, i)
            for n in range(1, 4):
                H = group_homology(name, G, n)
                check(all(h != 0 and order % h == 0 for h in H),
                      'prop 2.3: exp H_%d(%s) | %d' % (n, name, order))
            check(group_homology(name, G, 1) == gap_invariants(G),
                  'exc. 4.2.1: H_1 G = G_ab, %s' % name)
            check(group_homology(name, G, 2)
                  == canon([ZZ(x) for x in libgap.AbelianInvariantsMultiplier(G)]),
                  'H_2 G = GAP multiplier, %s' % name)

    # exc:restriction-transfer, exc:sylow-restriction-injective.
    transfer_checks = gap('''function(G, S)
      local T, phi, phiG, V, idx, ok, g, h, x, y, els;
      T := RightTransversal(G, S);
      phi := NaturalHomomorphismByNormalSubgroup(S, DerivedSubgroup(S));
      phiG := NaturalHomomorphismByNormalSubgroup(G, DerivedSubgroup(G));
      idx := Index(G, S);
      V := function(g) local p, t;
        p := One(Range(phi));
        for t in T do
          p := p * Image(phi, t * g * Inverse(T[PositionCanonical(T, t * g)]));
        od;
        return p;
      end;
      els := AsList(G);
      if Size(G) > 60 then els := List([1..60], i -> Random(G)); fi;
      ok := [];
      for x in GeneratorsOfGroup(G) do for y in els do
        Add(ok, V(x * y) = V(x) * V(y));
      od; od;
      for g in els do
        Add(ok, Image(phiG, PreImagesRepresentative(phi, V(g))) = Image(phiG, g^idx));
      od;
      return ok;
    end''')
    sylow_check = gap('''function(G, p)
      local S, T, phi, phiG, V, g, ok, o;
      S := SylowSubgroup(G, p);
      T := RightTransversal(G, S);
      phi := NaturalHomomorphismByNormalSubgroup(S, DerivedSubgroup(S));
      phiG := NaturalHomomorphismByNormalSubgroup(G, DerivedSubgroup(G));
      V := function(g) local q, t;
        q := One(Range(phi));
        for t in T do
          q := q * Image(phi, t * g * Inverse(T[PositionCanonical(T, t * g)]));
        od;
        return q;
      end;
      ok := [];
      for g in G do
        o := Order(Image(phiG, g));
        if o > 1 and IsPrimePowerInt(o) and o mod p = 0 then
          Add(ok, V(g) <> One(Range(phi)));
        fi;
      od;
      return ok;
    end''')
    groups = ['SymmetricGroup(3)', 'SymmetricGroup(4)', 'AlternatingGroup(4)',
              'SmallGroup(12,1)', 'SmallGroup(20,3)', 'SmallGroup(18,3)',
              'SmallGroup(24,3)', 'SmallGroup(24,8)', 'SmallGroup(36,9)',
              'SmallGroup(16,3)', 'SmallGroup(48,30)', 'SmallGroup(21,1)']
    for Gs in groups:
        G = gap(Gs)
        if not bool(libgap.IsPermGroup(G)):
            G = libgap.Image(libgap.IsomorphismPermGroup(G))
        for cl in libgap.ConjugacyClassesSubgroups(G):
            S = libgap.Representative(cl)
            if int(libgap.Size(S)) in (1, int(libgap.Size(G))):
                continue
            res = transfer_checks(G, S)
            check(all(bool(x) for x in res),
                  'exc. 4.2.3: transfer homomorphism, cor res = index, %s' % Gs)
        for p, _ in ZZ(int(libgap.Size(G))).factor():
            res = sylow_check(G, p)
            check(all(bool(x) for x in res),
                  'exc. 4.2.8: res injective on the %d-part of G_ab, %s' % (p, Gs))

    # exc:cyclic-chain-equivalence: f is a chain map (C316).
    for m in range(2, 7):
        Nm = {i: 1 for i in range(m)}
        for normalized in (True, False):
            for n in range(1, 7):
                if m ** (n // 2) > 300:
                    continue
                lhs = bar_d(bar_clean(f_periodic(n, m), normalized), m, normalized)
                de = {1: 1, 0: -1} if n % 2 else Nm
                rhs = bar_clean(bar_rmul(f_periodic(n - 1, m), de, m), normalized)
                check(lhs == rhs, 'exc. 4.2.5: d f(e_%d) = f(d e_%d), m = %d, %s'
                      % (n, n, m, 'normalized' if normalized else 'unnormalized'))

    # exc:cyclic-inversion-action.
    def coinv(chain):
        out = {}
        for key, c in chain.items():
            out[key[:-1]] = out.get(key[:-1], 0) + c
        return {k: c for k, c in out.items() if c}

    def act(chain, r, m):
        return {tuple((r * x) % m for x in key[:-1]) + (key[-1],): c
                for key, c in chain.items()}
    for m in range(3, 8):
        for normalized in (True, False):
            c1 = f_periodic(3, m)
            c1x = act(c1, -1, m)
            hint = {}
            for i in range(1, m + 1):
                for key, s in [((1, m - 1, i % m, m - 1, 0), 1),
                               ((1, i % m, 1, m - 1, 0), -1)]:
                    hint[key] = hint.get(key, 0) + s
            bd = coinv(bar_d(bar_clean(hint, normalized), m, normalized))
            diff = coinv(bar_clean(c1x, normalized))
            for key, c in coinv(bar_clean(c1, normalized)).items():
                diff[key] = diff.get(key, 0) - c
            diff = {k: c for k, c in diff.items() if c}
            neg = {k: -c for k, c in bd.items()}
            if normalized:
                check(diff == bd or diff == neg,
                      'exc. 4.2.6 hint (C319): c_1 o x - c_1 = boundary, m = %d' % m)
            else:
                rest = {k: diff.get(k, 0) - bd.get(k, 0) for k in set(diff) | set(bd)}
                rest = {k: c for k, c in rest.items() if c}
                check(all(0 in k for k in rest),
                      'exc. 4.2.6 unnormalized: difference degenerate, m = %d' % m)

    # g: R(G) -> X (normalized standard -> periodic), via a contracting homotopy.
    def s_per(n, v, m):
        """contracting homotopy of the periodic resolution: X_n -> X_(n+1)."""
        w = [0] * m
        if n % 2 == 0:
            for j in range(m):
                for l in range(j):
                    w[l] += v[j]
        else:
            w[0] += v[m - 1]
        return w

    def d_per(n, v, m):
        w = [0] * m
        if n % 2:
            for j in range(m):
                w[(j + 1) % m] += v[j]
                w[j] -= v[j]
        else:
            tot = sum(v)
            w = [tot] * m
        return w
    for m in range(2, 8):
        for n in range(0, 6):
            for j in range(m):
                v = [0] * m
                v[j] = 1
                lhs = [0] * m
                ds = d_per(n + 1, s_per(n, v, m), m)
                sd = s_per(n - 1, d_per(n, v, m), m) if n >= 1 else [1 if l == 0 else 0
                                                                       for l in range(m)]
                lhs = [ds[l] + sd[l] for l in range(m)]
                check(lhs == v, 'contracting homotopy of the periodic resolution')
    for m in range(3, 8):
        memo = {}

        def g_basis(key, m=m, memo=memo):
            """g(sigma) for a normalized generator sigma = key (h = 0)."""
            if key in memo:
                return memo[key]
            n = len(key)
            if n == 0:
                res = [1] + [0] * (m - 1)
            else:
                dsig = bar_d({key + (0,): 1}, m, True)
                acc = [0] * m
                for k2, c in dsig.items():
                    gk = g_basis(k2[:-1])
                    h = k2[-1]
                    for j in range(m):
                        acc[(j + h) % m] += c * gk[j]
                res = s_per(n - 1, acc, m)
            memo[key] = res
            return res

        def g_val(chain):
            return sum(c * sum(g_basis(k[:-1])) for k, c in chain.items()) % m
        for n in range(1, 5):
            for key in itertools.product(range(1, m), repeat=n):
                dg = d_per(n, g_basis(key), m)
                acc = [0] * m
                for k2, c in bar_d({key + (0,): 1}, m, True).items():
                    gk = g_basis(k2[:-1])
                    for j in range(m):
                        acc[(j + k2[-1]) % m] += c * gk[j]
                check(dg == acc, 'g is a chain map, m = %d' % m)
                break
        for k in range(0, 4):
            ck = bar_clean(f_periodic(2 * k + 1, m), True)
            if len(ck) > 2500:
                continue
            check(g_val(ck) == 1, 'exc. 4.2.6: g f = id on H_%d(Z_%d)' % (2 * k + 1, m))
            for r in range(1, m):
                if gcd(r, m) != 1:
                    continue
                val = g_val(bar_clean(act(ck, r, m), True))
                check(val == pow(r, k + 1, m),
                      'a -> a^r acts on H_%d(Z_%d) by r^(k+1)' % (2 * k + 1, m))
            val = g_val(bar_clean(act(ck, -1, m), True))
            check(val == (-1) ** (k + 1) % m,
                  'exc. 4.2.6: x acts on H_%d(Z_%d) by (-1)^(k+1)' % (2 * k + 1, m))

    # exc:inverting-extension-homology via the HNN sequence of p. 184.
    for m in range(3, 16, 2):
        def Hcyc(n):
            if n == 0:
                return 0      # Z
            return m if n % 2 else 1

        def xact(n):
            return 1 if n == 0 else (-1) ** ((n - 1) // 2 + 1)
        for n in range(1, 13):
            parts = []
            h = Hcyc(n)
            if h != 1:                           # Coker(1 - x) on H_n
                parts.append(gcd(h, 1 - xact(n)) if h else (0 if xact(n) == 1 else None))
            h1 = Hcyc(n - 1)
            if h1 != 1:                          # Ker(1 - x) on H_(n-1)
                c = 1 - xact(n - 1)
                parts.append(gcd(h1, c) if h1 else (0 if c == 0 else 1))
            got = canon([p for p in parts if p is not None])
            if n == 1:
                expect = [0]
            elif n % 4 in (0, 3):
                expect = canon([m])
            else:
                expect = []
            check(got == expect, 'exc. 4.2.7: H_%d(Z_%d x| Z)' % (n, m))
        Fax = libgap.FreeGroup(['a', 'x'])
        a_, x_ = libgap.GeneratorsOfGroup(Fax)
        G = Fax / libgap([a_ ** m, x_ ** -1 * a_ * x_ * a_])
        check(gap_invariants(G) == [0], 'exc. 4.2.7: H_1 = Z for odd m')

    # exc:dyadic-rationals-cd.
    def retraction(eps, n0, steps):
        """n_(i+1) = (n_i + eps_i) / 2 must stay integral."""
        n = QQ(n0)
        for i in range(steps):
            n = (n + eps(i)) / 2
            if n.denominator() != 1:
                return False
        return True
    refuted(not retraction(lambda i: 1, 1, 200),
            'exc. 4.2.12: the printed extension (x_(i+1)^2 = x_i e) does not split')
    check(all(2 * 1 == 1 + 1 for _ in range(1)),
          'exc. 4.2.12: x_i -> 1, e -> 1 respects x_(i+1)^2 = x_i e')
    eps = lambda i: (-1) ** i
    check(not any(retraction(eps, n0, 12) for n0 in range(-2 ** 10, 2 ** 10 + 1)),
          'exc. 4.2.12 corrected: no retraction with |n_0| <= 2^10')
    for k in range(1, 65):
        forced = -sum(eps(i) * 2 ** i for i in range(k))   # n_0 mod 2^k
        check((3 * forced + 1) % 2 ** k == 0,
              'exc. 4.2.12 corrected: 3 n_0 = -1 mod 2^%d' % k)
    check(QQ(-1) / 3 not in ZZ, 'n_0 = -1/3 is not an integer')
    # split iff sum eps_i 2^i (2-adic) is an integer; periodic patterns.
    for pattern in [(1,), (0,), (1, 0), (0, 1), (1, -1), (-1,), (1, 1, 0), (1, 0, 0),
                    (2,), (1, -1, 1, 0), (3, 1), (0, 0, 1)]:
        p = len(pattern)
        val = QQ(sum(pattern[i] * 2 ** i for i in range(p))) / (1 - 2 ** p)
        splits = val in ZZ
        n0 = -val if splits else None
        # a retraction forces n_0 = -S_k (mod 2^k), S_k = sum_(i<k) eps_i 2^i,
        # and S_k = val (mod 2^k) in Z_2: so n_0 = -val, an integer iff val is
        ok = all(((sum(pattern[i % p] * 2 ** i for i in range(k)) - val)
                  / 2 ** k).denominator() % 2 == 1 for k in range(1, 61))
        check(ok, 'dyadic: S_k = sum eps_i 2^i (mod 2^k), pattern %s' % (pattern,))
        if splits:
            check(retraction(lambda i: pattern[i % p], n0, 60),
                  'dyadic: split pattern %s has a retraction' % (pattern,))


# ---------------------------------------------------------------------------
# Section 3: universal coefficients (pp. 190-193)
# ---------------------------------------------------------------------------

def section_3():
    for Gs in UCT_GROUPS:
        G = gap(Gs)
        R = resolution(Gs, G, 5)
        ranks, D = R.integral()
        Hn = [complex_homology(ranks, D, n) for n in range(5)]
        check(Hn[0] == [0], 'H_0 G = Z')
        check(Hn[1] == gap_invariants(G), 'H_1 G = G_ab, %s' % Gs)
        check(Hn[2] == canon([ZZ(x) for x in libgap.AbelianInvariantsMultiplier(G)]),
              'H_2 G = GAP multiplier, %s' % Gs)
        # cochains: C^n = Z^(ranks[n]), delta^n = D_(n+1)^T: C^n -> C^(n+1)
        DT = {n: D[n + 1].transpose() for n in range(0, 5)}

        def cohom(n, rel=None):
            rel_n = rel(ranks[n]) if rel else None
            rel_next = rel(ranks[n + 1]) if rel else None
            return fg_homology(ranks[n], DT.get(n), DT.get(n - 1), rel_n, rel_next)
        Hc = [cohom(n) for n in range(5)]
        for m in [2, 3, 4, 6, 8, 9, 12]:
            relm = lambda a, m=m: m * identity_matrix(ZZ, a)
            for n in range(1, 5):
                rels = {j: relm(ranks[j]) for j in range(len(ranks))}
                Hm = complex_homology(ranks, D, n, rels)
                check(Hm == cyc_sum(cyc_tensor(Hn[n], [m]), cyc_tor(Hn[n - 1], [m])),
                      'th 3.1: H_%d(%s, Z_%d)' % (n, Gs, m))
                Hcm = cohom(n, relm)
                check(Hcm == cyc_sum(cyc_ext(Hn[n - 1], [m]), cyc_hom(Hn[n], [m])),
                      'th 3.3: H^%d(%s, Z_%d)' % (n, Gs, m))
                if n + 1 < len(Hc):
                    check(Hcm == cyc_sum(cyc_tensor(Hc[n], [m]), cyc_tor(Hc[n + 1], [m])),
                          'exc. 4.3.2: H^%d(%s, Z_%d) = H^n (x) Z_m + Tor(H^(n+1), Z_m)'
                          % (n, Gs, m))
                if ZZ(m).is_prime():
                    check(len(Hcm) == len(Hm), 'H^n(G, F_p) dual to H_n(G, F_p)')


# ---------------------------------------------------------------------------
# Section 4: H_2 and relations (pp. 193-203)
# ---------------------------------------------------------------------------

class Cayley:
    """The Cayley graph of a finite group G for generators x_1..x_r (images of
    the free generators of F).  N = Ker(F -> G) is pi_1 of the graph, N_ab its
    cycle space (basis: fundamental cycles of the non-tree edges of a BFS tree
    from 1), and conjugation by F acts on N_ab by left translations."""

    def __init__(self, G, gens):
        self.G = G
        self.gens = list(gens)
        self.r = len(self.gens)
        elts = libgap.AsList(G)
        self.n = int(libgap.Size(G))
        pos = gap('function(e, s) return List(e, g -> Position(e, g * s)); end')
        lpos = gap('function(e, s) return List(e, g -> Position(e, s * g)); end')
        self.right = [[int(x) - 1 for x in pos(elts, s)] for s in self.gens]
        self.left = [[int(x) - 1 for x in lpos(elts, s)] for s in self.gens]
        self.elts = elts
        self.one = int(libgap.Position(elts, libgap.One(G))) - 1
        self.inv_right = []
        for j in range(self.r):
            inv = [0] * self.n
            for v in range(self.n):
                inv[self.right[j][v]] = v
            self.inv_right.append(inv)
        # BFS tree
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
        assert len(parent) == self.n, 'generators do not generate'
        self.tree = tree
        self.nontree = [(v, j) for v in range(self.n) for j in range(self.r)
                        if (v, j) not in tree]
        self.coord = {e: i for i, e in enumerate(self.nontree)}
        self.k = len(self.nontree)
        assert self.k == 1 + self.n * (self.r - 1)
        # tree paths from 1: dict edge -> coefficient
        self.path = {self.one: {}}
        for v in order[1:]:
            u, j = parent[v]
            p = dict(self.path[u])
            p[(u, j)] = p.get((u, j), 0) + 1
            self.path[v] = p
        # fundamental cycles as edge dicts
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
        """left translation of an edge dict by the generator index h."""
        return {(self.left[h][v], j): c for (v, j), c in z.items()}

    def action_matrices(self):
        """T_h (rows: coordinates of h . z_i) for the generators h."""
        return [matrix(ZZ, [self.coords(self.translate(h, z)) for z in self.cycles])
                for h in range(self.r)]

    def labels(self):
        """k x r matrix: the image in F / F' = Z^r of the basis cycles."""
        Phi = zero_matrix(ZZ, self.k, self.r)
        for i, z in enumerate(self.cycles):
            for (v, j), c in z.items():
                Phi[i, j] += c
        return Phi

    def trace(self, word):
        """edge dict of the path of a word [(j, +-1), ...] from 1."""
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

    def coinvariant_relations(self):
        T = self.action_matrices()
        return matrix(ZZ, [row for t in T for row in (t - 1).rows()])

    def hopf(self):
        """(invariants of N/[N,F], invariants of (N cap F')/[N,F])."""
        Rel = self.coinvariant_relations()
        V = ZZ ** self.k
        W = V.submodule(Rel.rows())
        C = canon((V / W).invariants())
        Phi = self.labels()
        K = V.submodule(Phi.left_kernel_matrix().rows())
        H2 = canon((K / W).invariants())
        return C, H2, V, W


def word_from_gap(w, r):
    letters = [int(x) for x in libgap.LetterRepAssocWord(w)]
    return [(abs(x) - 1, 1 if x > 0 else -1) for x in letters]


def hall_basic(r, nmax):
    """Hall basic commutators (as nested tuples) by weight, Hall's ordering."""
    by_w = {1: [('x', i) for i in range(r)]}
    order = list(by_w[1])
    pos = {c: i for i, c in enumerate(order)}
    for n in range(2, nmax + 1):
        new = []
        for wa in range(1, n):
            wb = n - wa
            for a in by_w.get(wa, []):
                for b in by_w.get(wb, []):
                    if not pos[a] > pos[b]:
                        continue
                    if a[0] == 'c' and pos[a[2]] > pos[b]:
                        continue
                    new.append(('c', a, b))
        by_w[n] = new
        for c in new:
            pos[c] = len(order)
            order.append(c)
    return by_w


def printed_basic(r, nmax, corrected=False):
    """The recursive definition of p. 195: [[u, v], w] basic if u > v <= w
    (u, v, w basic, total weight n); corrected: also [u, v] basic, [u, v] > w."""
    by_w = {1: [('x', i) for i in range(r)]}
    order = list(by_w[1])
    pos = {c: i for i, c in enumerate(order)}
    by_w[2] = [('c', ('x', i), ('x', j)) for i in range(r) for j in range(r) if i > j]
    for c in by_w[2]:
        pos[c] = len(order)
        order.append(c)
    basic = set(order)
    for n in range(3, nmax + 1):
        new = []
        trip = []
        for wu in range(1, n):
            for wv in range(1, n - wu):
                ww = n - wu - wv
                for u in by_w.get(wu, []):
                    for v in by_w.get(wv, []):
                        for w in by_w.get(ww, []):
                            trip.append((u, v, w))
        for u, v, w in trip:
            if not (pos[u] > pos[v] and pos[v] <= pos[w]):
                continue
            uv = ('c', u, v)
            if corrected and not (uv in basic and pos[uv] > pos[w]):
                continue
            c = ('c', uv, w)
            if c not in new:
                new.append(c)
        by_w[n] = new
        for c in new:
            pos[c] = len(order)
            order.append(c)
            basic.add(c)
    return by_w


def lie_bracket(a, b):
    """[a, b] = a b - b a in the free associative ring (dicts word -> coeff)."""
    out = {}
    for u, c in a.items():
        for v, d in b.items():
            out[u + v] = out.get(u + v, 0) + c * d
            out[v + u] = out.get(v + u, 0) - c * d
    return {k: c for k, c in out.items() if c}


def lie_element(c, memo):
    """The Lie element of a commutator (nested tuple) in the free ring."""
    if c not in memo:
        if c[0] == 'x':
            memo[c] = {(c[1],): 1}
        else:
            memo[c] = lie_bracket(lie_element(c[1], memo), lie_element(c[2], memo))
    return memo[c]


def lie_vector(e, idx):
    v = [0] * len(idx)
    for w, c in e.items():
        v[idx[w]] = c
    return vector(ZZ, v)


def witt(r, n):
    return sum(moebius(d) * r ** (n // d) for d in divisors(n)) // n


def section_4():
    # Hopf formula from the Cayley graph, against GAP's multiplier.
    cases = []
    for order in range(1, 32):
        for i in range(1, int(libgap.NumberSmallGroups(order)) + 1):
            cases.append(('SmallGroup(%d,%d)' % (order, i), libgap.SmallGroup(order, i)))
    for name in ['AlternatingGroup(5)', 'SL(2,5)', 'PSL(2,7)', 'AlternatingGroup(6)']:
        cases.append((name, gap(name)))
    for name, G in cases:
        P = libgap.Image(libgap.IsomorphismPermGroup(G))
        gens = libgap.MinimalGeneratingSet(P) if int(libgap.Size(P)) <= 31 else \
            libgap.GeneratorsOfGroup(P)
        if int(libgap.Size(P)) == 1:
            gens = [libgap.One(P)]
        cay = Cayley(P, gens)
        C, H2, _, _ = cay.hopf()
        mult = canon([ZZ(x) for x in libgap.AbelianInvariantsMultiplier(P)])
        check(H2 == mult, 'prop 4.1 (Hopf): (N cap F\')/[N,F] = H_2 %s' % name)
        check(C == canon(mult + [0] * cay.r),
              'C332: N/[N,F] = H_2 G + Z^r, %s' % name)
    # the relators generate N/[N,F] (prop 4.2).
    for order in range(2, 25):
        for i in range(1, int(libgap.NumberSmallGroups(order)) + 1):
            G = libgap.SmallGroup(order, i)
            iso = libgap.IsomorphismFpGroup(G)
            Fp = libgap.Range(iso)
            rels = libgap.RelatorsOfFpGroup(Fp)
            gens = [libgap.PreImagesRepresentative(iso, g)
                    for g in libgap.GeneratorsOfGroup(Fp)]
            P = libgap.Image(libgap.IsomorphismPermGroup(G))
            perm = libgap.IsomorphismPermGroup(G)
            pg = [libgap.Image(perm, g) for g in gens]
            if any(bool(libgap.IsOne(g)) for g in pg):
                continue
            cay = Cayley(P, pg)
            _, _, V, W = cay.hopf()
            vecs = []
            for w in rels:
                z, end = cay.trace(word_from_gap(w, cay.r))
                check(end == cay.one, 'relators are closed paths')
                vecs.append(cay.coords(z))
            S = V.submodule(list(W.gens()) + vecs)
            check(S == V, 'prop 4.2: relators generate N/[N,F], SmallGroup(%d,%d)'
                  % (order, i))
    # five-term sequence: |N/[G,N]| = |Coker(H_2 G -> H_2 G/N)| |Ker(G_ab -> (G/N)_ab)|
    for order in range(2, 25):
        for i in range(1, int(libgap.NumberSmallGroups(order)) + 1):
            G = libgap.SmallGroup(order, i)
            P = libgap.Image(libgap.IsomorphismPermGroup(G))
            gens = libgap.MinimalGeneratingSet(P)
            cayG = Cayley(P, gens)
            _, H2G, VG, WG = cayG.hopf()
            for Nn in libgap.NormalSubgroups(P):
                n_size = int(libgap.Size(Nn))
                if n_size in (1, order):
                    continue
                hom = libgap.NaturalHomomorphismByNormalSubgroup(P, Nn)
                Q = libgap.Image(hom)
                Qp = libgap.Image(libgap.IsomorphismPermGroup(Q))
                iso2 = libgap.IsomorphismPermGroup(Q)
                qg = [libgap.Image(iso2, libgap.Image(hom, g)) for g in gens]
                if any(bool(libgap.IsOne(g)) for g in qg):
                    continue      # a generator dies: skip (F would change)
                cayQ = Cayley(Qp, qg)
                _, H2Q, VQ, WQ = cayQ.hopf()
                # image of H_2 G: the basis cycles of G pushed down to Q
                qpos = gap('function(e1, h, iso, e2) return List(e1, g -> '
                           'Position(e2, Image(iso, Image(h, g)))); end')(
                               libgap.AsList(P), hom, iso2, libgap.AsList(Qp))
                qpos = [int(x) - 1 for x in qpos]
                Phi = cayG.labels()
                Kg = Phi.left_kernel_matrix()
                imgs = []
                for row in Kg.rows():
                    z = {}
                    for idx, c in enumerate(row):
                        if c:
                            for (v, j), cc in cayG.cycles[idx].items():
                                key = (qpos[v], j)
                                z[key] = z.get(key, 0) + c * cc
                    imgs.append(cayQ.coords(z))
                PhiQ = cayQ.labels()
                KQ = VQ.submodule(PhiQ.left_kernel_matrix().rows())
                Im = VQ.submodule(list(WQ.gens()) + imgs)
                coker = (KQ / Im).cardinality() if (KQ / Im).invariants() else 1
                comm = int(libgap.Size(libgap.CommutatorSubgroup(P, Nn)))
                lhs = n_size // comm
                ab_g = libgap.Size(libgap.DerivedSubgroup(P))
                kerab = int(libgap.Size(libgap.ClosureGroup(libgap.DerivedSubgroup(P), Nn))) \
                    // int(ab_g)
                check(lhs == coker * kerab,
                      'prop 4.4 (five terms): SmallGroup(%d,%d), |N| = %d' % (order, i, n_size))

    # basic commutators: Hall's definition, Witt's formula, the free Lie ring.
    for r, nmax in [(1, 6), (2, 7), (3, 5), (4, 4)]:
        hb = hall_basic(r, nmax)
        memo = {}
        for n in range(1, nmax + 1):
            check(len(hb[n]) == witt(r, n), 'Hall basic count = Witt, r=%d n=%d' % (r, n))
            words = list(itertools.product(range(r), repeat=n))
            idx = {w: i for i, w in enumerate(words)}
            H = matrix(ZZ, [lie_vector(lie_element(cc, memo), idx) for cc in hb[n]]) \
                if hb[n] else matrix(ZZ, 0, len(words))
            check(H.rank() == len(hb[n]),
                  'Hall basic Lie elements independent, r=%d n=%d' % (r, n))
            V = ZZ ** len(words)
            LH = V.submodule(H.rows())
            ok = True
            for w in words:
                e = {(w[0],): 1}
                for i in w[1:]:
                    e = lie_bracket(e, {(i,): 1})
                if e and lie_vector(e, idx) not in LH:
                    ok = False
                    break
            check(ok, 'left-normed brackets in the Z-span of the Hall basis, '
                  'r=%d n=%d' % (r, n))
        check(len(hb[3]) == (r ** 3 - r) // 3, 'weight 3: (r^3 - r)/3')
        check(set(hb[3]) == {('c', ('c', ('x', i), ('x', j)), ('x', k))
                             for i in range(r) for j in range(r) for k in range(r)
                             if i > j <= k},
              'p. 195: weight 3 basic commutators [[x_i,x_j],x_k], i > j <= k')
        if r >= 2 and nmax >= 5:
            pb = printed_basic(r, 5)
            pc = printed_basic(r, 5, corrected=True)
            for n in range(1, 6):
                check(set(pc[n]) == set(hb[n]),
                      'p. 195 corrected definition = Hall basic, r=%d n=%d' % (r, n))
            refuted(all(len(pb[n]) == witt(r, n) for n in (4, 5)),
                    'p. 195 printed definition gives M_r(n) commutators, r = %d' % r)
            y, x = ('x', 1), ('x', 0)
            yx = ('c', y, x)
            check(('c', yx, yx) in pb[4] and not lie_element(('c', yx, yx), memo),
                  'printed definition admits [[y,x],[y,x]] = 1')
    # commutator identities (book's convention [a,b] = a^-1 b^-1 a b), C347.
    F3 = libgap.FreeGroup(3)
    a, b, c = libgap.GeneratorsOfGroup(F3)
    comm = lambda u, v: u ** -1 * v ** -1 * u * v
    conj = lambda u, v: v ** -1 * u * v
    check(comm(a, b) ** -1 == comm(b, a), '[a,b]^-1 = [b,a]')
    check(comm(a * b, c) == conj(comm(a, c), b) * comm(b, c), '[ab,c] = [a,c]^b [b,c]')
    check(comm(comm(a, b), conj(c, a)) * comm(comm(c, a), conj(b, c))
          * comm(comm(b, c), conj(a, b)) == libgap.One(F3), 'Hall-Witt identity')
    # exc:metabelian-h2-zero
    Fx = libgap.FreeGroup(2)
    x, y = libgap.GeneratorsOfGroup(Fx)
    BS = Fx / libgap([x ** -1 * y * x * y ** -2])
    check(gap_invariants(BS) == [0], 'exc. 4.4.3: G_ab = Z')
    rel = word_from_gap(x ** -1 * y * x * y ** -2, 2)
    expsum = [sum(e for j, e in rel if j == i) for i in range(2)]
    check(expsum != [0, 0], 'exc. 4.4.3: relator not in F\', so H_2 = 0 (p. 195)')
    # C341: the remark of p. 199 needs G != 1 and N != 1: G = 1 = F/F gives
    # F/F' = <x, y | [x, y]> (one relator, abelian since the generators commute).
    Z2 = Fx / libgap([comm(x, y)])
    check(gap_invariants(Z2) == [0, 0] and len(libgap.RelatorsOfFpGroup(Z2)) == 1,
          'p. 199, G = 1: F/F\' = Z^2 has a presentation with one relator')
    # lem:ordered-exterior-square-free on boxes of Z and Z^2 (lexicographic order):
    # every unordered pair {u, v}, u != v, is {g h, h} for exactly one g > 1.
    for dimn in (1, 2):
        box = list(itertools.product(range(-3, 4), repeat=dimn))
        zero = tuple([0] * dimn)
        ok = True
        for u in box:
            for v in box:
                if u >= v:
                    continue
                reps = []
                for (p, q) in ((u, v), (v, u)):
                    g = tuple(p[i] - q[i] for i in range(dimn))
                    if g > zero:
                        reps.append((g, q))
                ok = ok and len(reps) == 1
        check(ok, 'lem 4.4: (g ^ 1) h, g > 1, is a basis of Z G ^ Z G (box, rank %d)'
              % dimn)


def main():
    section_1()
    section_2()
    section_3()
    section_4()
    print('ok %s: %d checks' % (SCOPE, COUNT[0]))


if __name__ == '__main__':
    main()
