"""Exact checks of Chapter 5, §§ 5-7 "Гомологии расширений" (Sage).

Run from the project root: sage -python checks/sage/chapter-5b.py (plain
asserts; do not use -O).  The last line is "ok chapter-5b: N checks".

Book: Ю. В. Кузьмин, «Гомологическая теория групп» (Факториал Пресс, 2006),
printed pp. 270-292.  Pages are the printed pages; labels are those of
content/05-05-*.typ ... 05-07-*.typ.  Modules are right modules, as in the
book (a b = b^-1 a b in a semidirect product B A, A written additively;
matrices act on row vectors).  Everything is exact: integer lattices and
their quotients (Sage free modules over ZZ), polynomials over ZZ, linear
algebra over F_p written out in Python, finite groups from GAP (libgap,
GAP core only).  Nothing here compares our text with the printed book.

Notation of the scripts.  For a finite group B the homology H_m(B, M) is
computed from an explicit free resolution X of Z (the periodic resolution
of a cyclic group, the tensor product of two periodic resolutions for
Z_2 x Z_2, prop:direct-product-resolution) as the homology of
X (x)_B M = M^(rank X_m).  "The standard complex" is Y = R(A) (x)_A Z of
the book (basis: tuples (a_1, ..., a_n), d as on p. 251 with the first
term's group ring factor sent to 1), B acting diagonally on the tuples.

What is checked, by section, and where the expected values come from:

section_5 (pp. 269-275).  For nine extensions 1 -> N -> G -> B -> 1 of
  finite groups and F_p-modules L (Q_8, D_8, D_16, Q_16 over their centres,
  Z_4 over Z_2, Z_2^2 over Z_2 (split), S_3 over A_3 with the sign module
  F_3, A_4 over V_4 with F_2[G/N], D_8 over its cyclic subgroup Z_4 with
  F_2[C\\G] for a reflection subgroup C): the computation of p. 271 (for
  g in N, f g - f is the principal derivation of f(g), so N acts trivially on
  H^1(N, L)); lem:invariant-class-function: phi built from a right
  transversal as in the proof satisfies eq:invariant-class-function for
  every g in G (the step the proof leaves to the reader) and both
  identities eq:invariant-class-function-properties; d phi takes values in
  L^N, is constant on cosets in both arguments and gives a 2-cocycle of B;
  its class does not depend on the choice of phi(b-bar) and vanishes for
  principal f (p. 273); the five-term sequence (p. 271) is exact at every
  term (t^1 injective, Im t^1 = Ker r^1, Im r^1 = Ker delta,
  Im delta = Ker t^2) and delta != 0 for the four non-split central
  extensions.  The printed "h in H" of the proof (corrected to h in N) is the
  N of these checks.  For D_8 over Z_4 with F_2[C\\G] the subgroup N moves
  1-cocycles (f h - f = principal derivation of f(h) != 0), so B acts on
  H^1(N, L) but not on the cocycles: E_2^(0 n) of p. 269 consists of
  invariant classes (corrected wording).
section_6 (pp. 275-284).
  D^k(A) (p. 276-277) for A = Z^r: the group presented by the generators
  a_1 ⊓ ... ⊓ a_k (all a_i in {0,1}^r) and Lambda^(k+1)(A) (x) Z_2 with the
  quasilinearity relations among these generators and relation 1) read as
  alternation (a_1 ⊓ ... ⊓ a_k = 0 when a_i = a_j) is isomorphic, by the
  map of lem:dk-direct-sum, to Lambda^(k+1) (x) Z_2 (+) Lambda^k
  ((r, k) = (1, 1), (1, 2), (2, 1), (2, 2), (2, 3), (3, 1), (3, 2), (3, 3),
  (4, 2)); since quasilinearity reduces every generator of D^k(Z^r) to
  these and f respects all relations (below), D^k(Z^r) is that group and
  (eq:dk-exact-sequence) holds for these r, k; read as a mere change of sign
  (the printed «кососимметричность») the same presentation has extra
  2-torsion (A = Z, k = 2: Z_2 instead of 0), and for every r >= 1, k >= 2
  the function "product of the first coordinates mod 2" satisfies the
  sign-change and quasilinearity relations, kills Lambda^(k+1) (x) Z_2 and
  is 1 on e_1 ⊓ ... ⊓ e_1, while e_1 ^ ... ^ e_1 = 0, so lem:dk-exact-sequence
  fails for that reading (relations checked on all argument tuples with
  entries in {-1, 0, 1, 2} for (r, k) = (1, 2), (1, 3), (2, 2) and on 3000
  random such tuples for r <= 3, k <= 3 otherwise).
  lem:dk-direct-sum: in U(A) the product a_1 ... a_k (a_1 + ... + a_k) has
  even coefficients, eq:tau-quasilinearity holds before division by 2 as an
  identity of polynomials in the coordinates, and the function f of the
  lemma is alternating (Boolean reduction of the polynomials), r <= 4,
  k <= 3; the printed formula for the action of b on the direct sum
  (p. 279) and the answer of exc:d1-action agree with the linear extension
  of the action on the basis (random arguments); exc:base-differential-
  splitting (as corrected: D^0 = A (x) Z_2 (+) Z; the printed A (+) Z is
  not even isomorphic as a group); exc:invariant-basis-splitting (the
  correction term vanishes for signed permutation matrices, k <= 3);
  exc:u-not-module (the ideal (e_1^2, e_2^2) is not invariant under
  e_1 -> e_1 + e_2).
  lem:alt-linearity-defect in the universal case a_i = e_i in Z^(n+1),
  n <= 5 (which implies it for every abelian A and that n by
  functoriality); exc:alt-identity-n2 (12 terms, 6 of them cancel);
  cor:alt-exterior-iso: alt(e_I) is a cycle, f_n(alt) = n! wedge, f_n
  vanishes on boundaries (n <= 5; as corrected, the printed last term
  (-1)^(n+1) a_2 ^ ... ^ a_n refuted); phi(y) = (1/2)(k+1)! a_1 ^ ... ^
  a_(k+1) for the element y of the proof of eq:pk-quasilinearity (the
  number of permutations is (1/2)(k+1)!, k <= 5).
  th:split-d2-bockstein on split extensions B A with B = Z_2 x Z_2 (and
  Z_4) acting on lattices A = Z^r: the differential d^2_(m k) is computed
  directly in the bicomplex X (x)_B Y by prop:bicomplex-d2 (a_(m-1, k+1)
  is found explicitly, the result is read through cor:alt-exterior-iso),
  and compared with the composite of the connecting homomorphism of
  (eq:dk-exact-sequence) (D^k with the B-action transported by
  lem:dk-direct-sum) and the Bockstein homomorphism, on every generator of
  H_m(B, Lambda^k(A)): k = 1 for the point groups mm2 and 222 on the
  F- and I-centred lattices (r = 3; m <= 6 for F(mm2), m <= 5 for the
  others) and for Z_4 on the I-lattice (m <= 6), k = 2 for the same lattices
  and for F(mm2) (+) Z with two actions on Z (r = 4), k = 3 for
  F(mm2) (+) Z[Z_2] (r = 5), m from 2 to 5.  They agree everywhere; d^2 is
  nonzero for F(mm2) at k = 1, 2, 3 (so the differentials of a split
  extension do not vanish, p. 276), and 2 d^2 = 0 (prop:d2-image-two-
  torsion).  D^1 splits for every action on Z^2 (an invariant quadratic
  refinement exists), so rank 3 is the smallest where this test can bite.
section_7 (pp. 284-292).
  The module P_G of p. 284 for G = Z (A = mZ, m = 2, 3, 4), the Klein
  bottle group (A = Z^2, B = Z_2) and the space group Fdd2 (A the F-centred
  lattice, B = mm2, a non-split extension): P_G is built as the universal
  B-module with a derivation from G (A + Z^(B - 1) with the action given
  by the factor set), checked to be a module; (eq:pg-exact-sequence);
  for G = Z it is Z[Z_m] with A = Z N.  The relation defining
  Lambda^k(A) ^ P_G (p. 285): with the printed sign-change relation the
  left term of (eq:exterior-pg-sequence) acquires 2-torsion (A = Z, k = 1:
  Z_2 instead of Lambda^2 = 0; A = Z^2: Z (+) Z_2^2 instead of Z), with
  the corrected relation a_1 ^ ... ^ a_k (x) a_k = 0 it is Lambda^(k+1)(A)
  and Lambda^k(A) ^ P_G is free.  th:abelian-kernel-d2 and
  cor:d2-base-characteristic-class: the differentials d^2_(m 0) and
  d^2_(m 1) are computed directly in the bicomplex X (x)_B Y with
  Y = R(P_G) (x)_A Z and the action eq:y-exponential-action (checked to
  commute with d), and compared with multiplication by chi_k (the two
  connecting homomorphisms of eq:exterior-group-ring-sequence and
  eq:exterior-pg-sequence) plus the split differential of section_6:
  d^2 = chi + d-bar^2 on every generator, m <= 6 for Z, m <= 5 otherwise.
  For Fdd2 at k = 1 both chi and d-bar^2 are nonzero and cancel (d^2 = 0),
  so neither summand alone is the differential.  For the Klein bottle group
  and G = Z the multiplications forced by the known homology (H_n = 0 for
  n >= 2) are isomorphisms.  lem:alt-action-correction in the
  three models (n <= 3, every b); the formula of the proof of
  lem:alt-action-correction (as corrected: d(alt(c_1..c_n)) = sum (-1)^(n-i) alt(..^c_i..)
  (x) (e^(c_i) - 1)) in the universal case, n <= 4; f(alt) = n! wedge in Y.
  The last diagram of the proof of th:abelian-kernel-d2: an exact sequence
  0 -> Lambda^(k+1) -> M -> P^k_0 -> Lambda^k -> 0 forces
  rank M = rank(Lambda^k ^ P_G); for G = Z, A = 3Z, k = 1 and for Fdd2,
  k = 1, 2, 3, rank Lambda^(k+1)(P_G) is larger, so the printed top row with
  Lambda^(k+1)(P_G) is not exact, while the corrected one (Lambda^k ^ P_G)
  passes the count; the left square commutes since 2 (1/2)(k+1)! =
  (k+1)! (k >= 1).  For k = 0 the module P^0_0 (generated by L''_0 =
  P_G / A = Delta_B and an element u with u b = u + (b - 1)) is Z B with
  u = 1, so the corresponding row is chi_0 (case k = 0 of the corrected
  text).

What is NOT established: the theorems are checked on the finite list of
groups, lattices, degrees and arguments above, not proved; the identity
lemmas (lem:alt-linearity-defect, cor:alt-exterior-iso, the evenness in
U(A)) are proved for the stated n, r, k only; the spectral-sequence
comparison uses one bicomplex model for each group and the identification
of E^2 by cor:alt-exterior-iso; the modules P^k, R^k of the proofs (of
infinite rank) are not computed; signs of the identifications are not
pinned down where the values have order 2.
"""

import random
from itertools import combinations, permutations, product

from sage.all import (QQ, ZZ, PolynomialRing, block_diagonal_matrix,
                      block_matrix, diagonal_matrix, factorial,
                      identity_matrix, libgap, matrix, vector)

SCOPE = 'chapter-5b'
COUNT = [0]


def check(cond, what):
    assert bool(cond), 'FAILED: ' + what
    COUNT[0] += 1


def refuted(cond, what):
    assert not bool(cond), 'printed reading unexpectedly holds: ' + what
    COUNT[0] += 1


def addto(d, k, c):
    if c:
        v = d.get(k, 0) + c
        if v:
            d[k] = v
        else:
            del d[k]


def dadd(d, e, s=1):
    for k, v in e.items():
        addto(d, k, s * v)


def vadd(x, y):
    return tuple(a + b for a, b in zip(x, y))


def vneg(x):
    return tuple(-a for a in x)


def perm_sign(p):
    s = 1
    p = list(p)
    for i in range(len(p)):
        for j in range(i + 1, len(p)):
            if p[i] > p[j]:
                s = -s
    return s


def unit(r, j):
    return tuple(1 if i == j else 0 for i in range(r))


# ---------------------------------------------------------------------------
# Linear algebra over F_p (pure Python; rows are lists)
# ---------------------------------------------------------------------------

def ech(rows, p):
    basis, piv = [], []
    for v in rows:
        v = [x % p for x in v]
        for b, pc in zip(basis, piv):
            if v[pc]:
                c = v[pc]
                v = [(x - c * y) % p for x, y in zip(v, b)]
        nz = next((i for i, x in enumerate(v) if x), None)
        if nz is None:
            continue
        iv = pow(v[nz], -1, p)
        v = [(x * iv) % p for x in v]
        for i, b in enumerate(basis):
            if b[nz]:
                c = b[nz]
                basis[i] = [(x - c * y) % p for x, y in zip(b, v)]
        basis.append(v)
        piv.append(nz)
    return basis, piv


def in_span(v, E, p):
    basis, piv = E
    v = [x % p for x in v]
    for b, pc in zip(basis, piv):
        if v[pc]:
            c = v[pc]
            v = [(x - c * y) % p for x, y in zip(v, b)]
    return not any(v)


def kernel(images, length, p):
    """Coefficient vectors x with sum x_i images_i = 0."""
    n = len(images)
    aug = [list(img) + [1 if j == i else 0 for j in range(n)]
           for i, img in enumerate(images)]
    basis, piv = ech(aug, p)
    return [b[length:] for b, pc in zip(basis, piv) if pc >= length]


def combine(coeffs, vecs, p):
    out = [0] * len(vecs[0])
    for c, v in zip(coeffs, vecs):
        if c:
            out = [(x + c * y) % p for x, y in zip(out, v)]
    return out


# ---------------------------------------------------------------------------
# Section 5: the five-term sequence for finite groups
# ---------------------------------------------------------------------------

class FG:
    """A finite group from GAP with a multiplication table."""

    def __init__(self, G):
        if not G.IsPermGroup():
            G = G.IsomorphismPermGroup().Image()
        self.gap = G
        deg = max(1, int(G.LargestMovedPoint()))
        els = list(G.AsSSortedList())
        self.perms = [tuple(int(v) - 1 for v in libgap.ListPerm(x, deg))
                      for x in els]
        self.index = {q: i for i, q in enumerate(self.perms)}
        self.deg = deg
        n = len(els)
        self.n = n
        self.mul = [[self.index[tuple(q[a[k]] for k in range(deg))]
                     for q in self.perms] for a in self.perms]
        self.e = self.index[tuple(range(deg))]
        self.inv = [next(j for j in range(n) if self.mul[i][j] == self.e)
                    for i in range(n)]

    def elt(self, x):
        return self.index[tuple(int(v) - 1
                                for v in libgap.ListPerm(x, self.deg))]

    def gens(self):
        return [self.elt(x) for x in self.gap.GeneratorsOfGroup()]


def matmul_p(a, b, p):
    return [[sum(a[i][k] * b[k][j] for k in range(len(b))) % p
             for j in range(len(b[0]))] for i in range(len(a))]


def vecmat(v, m, p):
    return [sum(v[k] * m[k][j] for k in range(len(v))) % p
            for j in range(len(m[0]))]


def five_term_case(name, Ggap, Ngap, p, module, expect_delta_nonzero,
                   expect_n_moves_cocycles=False):
    if not Ggap.IsPermGroup():
        iso = Ggap.IsomorphismPermGroup()
        Ggap, Ngap = iso.Image(), iso.Image(Ngap)
    G = FG(Ggap)
    N = sorted(set(G.elt(x) for x in Ngap.AsSSortedList()))
    Nset = set(N)
    # right transversal: g = h t (h in N); B indexed by transversal
    trans, coset = [], {}
    for g in range(G.n):
        if g in coset:
            continue
        ti = len(trans)
        trans.append(g)
        for h in N:
            coset[G.mul[h][g]] = ti
    nB = len(trans)
    # make the identity the representative of N itself
    i0 = coset[G.e]
    trans[i0] = G.e
    hpart = {}
    for g in range(G.n):
        t = trans[coset[g]]
        hpart[g] = G.mul[g][G.inv[t]]        # g = h t
        assert hpart[g] in Nset
    Bmul = [[coset[G.mul[trans[i]][trans[j]]] for j in range(nB)]
            for i in range(nB)]
    Be = coset[G.e]
    # module L = F_p^d with matrices rho[g] (row convention)
    rho, d = module(G, N, coset, p)
    for a in range(G.n):
        for b in range(G.n):
            assert matmul_p(rho[a], rho[b], p) == rho[G.mul[a][b]]

    def act(v, g):
        return vecmat(v, rho[g], p)

    def sub(u, v):
        return [(x - y) % p for x, y in zip(u, v)]

    def add(u, v):
        return [(x + y) % p for x, y in zip(u, v)]

    # L^N: basis and coordinates
    fixN = kernel([sum((sub([1 if j == i else 0 for j in range(d)],
                             act([1 if j == i else 0 for j in range(d)], h))
                        for h in N), []) for i in range(d)], d * len(N), p)
    dN = len(fixN)
    # cochains on a group (elements 0..n-1) with values in a module of dim k
    #   C^1: index g*k + i ; C^2: index (g*n + h)*k + i

    def coboundary1(mul, n, k, actf):
        # (d f)(g, h) = f(g) h - f(g h) + f(h)
        imgs = []
        for g0 in range(n):
            for i in range(k):
                img = [0] * (n * n * k)
                ei = [1 if j == i else 0 for j in range(k)]
                for h in range(n):
                    v = actf(ei, h)
                    for j in range(k):
                        img[(g0 * n + h) * k + j] += v[j]
                for g in range(n):
                    for h in range(n):
                        if mul[g][h] == g0:
                            img[(g * n + h) * k + i] -= 1
                for g in range(n):
                    img[(g * n + g0) * k + i] += 1
                imgs.append([x % p for x in img])
        return imgs

    def coboundary2(mul, n, k, actf):
        # (d c)(g1,g2,g3) = c(g2,g3) - c(g1 g2,g3) + c(g1,g2 g3) - c(g1,g2) g3
        imgs = []
        for a in range(n):
            for b in range(n):
                for i in range(k):
                    img = [0] * (n ** 3 * k)
                    ei = [1 if j == i else 0 for j in range(k)]
                    for g1 in range(n):
                        img[((g1 * n + a) * n + b) * k + i] += 1
                    for g1 in range(n):
                        for g2 in range(n):
                            if mul[g1][g2] == a:
                                img[((g1 * n + g2) * n + b) * k + i] -= 1
                    for g2 in range(n):
                        for g3 in range(n):
                            if mul[g2][g3] == b:
                                img[((a * n + g2) * n + g3) * k + i] += 1
                    for g3 in range(n):
                        v = actf(ei, g3)
                        for j in range(k):
                            img[((a * n + b) * n + g3) * k + j] -= v[j]
                    imgs.append([x % p for x in img])
        return imgs

    def coboundary0(n, k, actf):
        imgs = []
        for i in range(k):
            ei = [1 if j == i else 0 for j in range(k)]
            img = []
            for g in range(n):
                img += sub(actf(ei, g), ei)
            imgs.append(img)
        return imgs

    def vec_from_cochain(rows, coeffs, length):
        return combine(coeffs, rows, p) if rows else [0] * length

    # groups: G, N (as its own table), B
    Nidx = {h: i for i, h in enumerate(N)}
    Nmul = [[Nidx[G.mul[a][b]] for b in N] for a in N]
    actG = act

    def actN(v, i):
        return act(v, N[i])
    # L^N as B-module, basis fixN (vectors in L)
    fixE = ech(fixN, p)

    def coordsN(v):
        # coordinates of v in L^N w.r.t. fixN
        sol = kernel([list(f) for f in fixN] + [list(v)], d, p)
        sol = [s for s in sol if s[-1] % p]
        assert sol, 'not in L^N'
        s = sol[0]
        c = (-pow(s[-1], -1, p)) % p
        return [(x * c) % p for x in s[:-1]]

    def actB(vN, bi):
        v = combine(vN, fixN, p) if dN else []
        return coordsN(act(v, trans[bi])) if dN else []

    nG, nN = G.n, len(N)
    # Der(G, L), B^1(G, L)
    dG1 = coboundary1(G.mul, nG, d, actG)
    ZG1 = kernel(dG1, nG * nG * d, p)
    BG1 = coboundary0(nG, d, actG)
    dN1 = coboundary1(Nmul, nN, d, actN)
    ZN1 = kernel(dN1, nN * nN * d, p)
    ZN1v = [vec_from_cochain([[1 if j == i else 0 for j in range(nN * d)]
                              for i in range(nN * d)], z, nN * d)
            for z in ZN1]
    BN1 = coboundary0(nN, d, actN)
    BN1E = ech(BN1, p)
    # p. 271: for g in N, f g - f is the principal derivation of f(g)
    for f in ZN1v:
        for gi, g in enumerate(N):
            for hi, h in enumerate(N):
                lhs = sub(act(f[Nidx[G.mul[G.mul[g][h]][G.inv[g]]] * d:
                                Nidx[G.mul[G.mul[g][h]][G.inv[g]]] * d + d],
                              g), f[hi * d:hi * d + d])
                rhs = sub(act(f[gi * d:gi * d + d], h), f[gi * d:gi * d + d])
                check(lhs == rhs, '%s p. 271: (f g - f)(h) = f(g)(h - 1), '
                      'g, h in N' % name)

    def fg(f, g):
        # (f g)(h) = f(g h g^-1) g
        out = []
        for h in N:
            c = G.mul[G.mul[g][h]][G.inv[g]]
            out += act(f[Nidx[c] * d:Nidx[c] * d + d], g)
        return out
    # p. 269: B acts on H^n(N, L), not on cocycles: N moves cocycles when it
    # acts nontrivially on L (f h - f is the principal derivation of f(h))
    moves = any(fg(f, h) != f for f in ZN1v for h in N)
    check(moves == expect_n_moves_cocycles,
          '%s: N acts %s on the 1-cocycles of N' % (
              name,
              'nontrivially' if expect_n_moves_cocycles else 'trivially'))
    # Der^inv: f with f g - f principal for all g in G (generators suffice)
    gens = G.gens()
    k1 = len(ZN1v)
    blocks = []
    for f in ZN1v:
        row = []
        for g in gens:
            row += sub(fg(f, g), f)
        blocks.append(row)
    nb = len(BN1)
    imgs = [list(b) for b in blocks]
    for gi in range(len(gens)):
        for b in BN1:
            imgs.append([0] * (gi * nN * d) + list(b)
                        + [0] * ((len(gens) - gi - 1) * nN * d))
    ker = kernel(imgs, len(gens) * nN * d, p)
    Dinv = ech([combine(x[:k1], ZN1v, p) for x in ker if any(x[:k1])], p)[0]
    # check invariance for all g, not only generators
    for f in Dinv:
        for g in range(nG):
            check(in_span(sub(fg(f, g), f), BN1E, p),
                  '%s: class of f is G-invariant' % name)
    # delta: construct phi by lem:invariant-class-function

    def solve_phi(f, t, choice):
        # phi(t) with (f t - f)(h) = phi(t)(h - 1) for h in N
        target = sub(fg(f, t), f)
        imgs_ = []
        for i in range(d):
            ei = [1 if j == i else 0 for j in range(d)]
            img = []
            for h in N:
                img += sub(act(ei, h), ei)
            imgs_.append(img)
        sol = kernel(imgs_ + [target], nN * d, p)
        sol = [s for s in sol if s[-1] % p]
        assert sol, 'no phi(t)'
        s = sol[0]
        c = (-pow(s[-1], -1, p)) % p
        base = [(x * c) % p for x in s[:-1]]
        # the solutions differ by L^N; 'choice' adds an element of L^N
        if choice and dN:
            base = add(base, combine(choice, fixN, p))
        return base

    def build_phi(f, choice=None):
        phi = {}
        phit = {}
        for ti, t in enumerate(trans):
            phit[ti] = ([0] * d if t == G.e
                        else solve_phi(f, t, choice[ti] if choice else None))
        for g in range(nG):
            h = hpart[g]
            t = trans[coset[g]]
            phi[g] = add(act(f[Nidx[h] * d:Nidx[h] * d + d], t),
                         phit[coset[g]])
        return phi

    def dphi(phi, g1, g2):
        return add(sub(act(phi[g1], g2), phi[G.mul[g1][g2]]), phi[g2])

    def delta_cocycle(f, choice=None):
        phi = build_phi(f, choice)
        # (5.16) for all g in G
        for g in range(nG):
            lhs = sub(fg(f, g), f)
            rhs = []
            for h in N:
                rhs += sub(act(phi[g], h), phi[g])
            check(lhs == rhs, '%s: phi satisfies (5.16) for all g' % name)
        for h in N:
            check(phi[h] == f[Nidx[h] * d:Nidx[h] * d + d],
                  '%s: phi = f on N' % name)
            for g in range(nG):
                check(phi[G.mul[h][g]] == add(act(phi[h], g), phi[g]),
                      '%s: phi(h g) = phi(h) g + phi(g)' % name)
                check(phi[G.mul[g][h]] == add(act(phi[g], h), phi[h]),
                      '%s: phi(g h) = phi(g) h + phi(h)' % name)
        beta = {}
        for g1 in range(nG):
            for g2 in range(nG):
                v = dphi(phi, g1, g2)
                for h in N:
                    assert act(v, h) == v
                    assert dphi(phi, G.mul[g1][h], g2) == v
                    assert dphi(phi, g1, G.mul[g2][h]) == v
        COUNT[0] += 1        # d phi in L^N, constant on cosets (all pairs)
        for b1 in range(nB):
            for b2 in range(nB):
                beta[(b1, b2)] = coordsN(dphi(phi, trans[b1], trans[b2]))
        vec = []
        for b1 in range(nB):
            for b2 in range(nB):
                vec += beta[(b1, b2)]
        return vec
    # cochains on B with values in L^N
    dB1 = coboundary1(Bmul, nB, dN, actB) if dN else []
    BB2 = dB1
    BB2E = ech(BB2, p)
    dB2 = coboundary2(Bmul, nB, dN, actB) if dN else []
    ZB2 = kernel(dB2, nB ** 3 * dN, p) if dN else []
    ZB2v = [combine(z, [[1 if j == i else 0 for j in range(nB * nB * dN)]
                        for i in range(nB * nB * dN)], p) for z in ZB2]
    deltas = []
    for f in Dinv:
        vec = delta_cocycle(f)
        if dN:
            check(not any(combine(vec, dB2, p)),
                  '%s: delta(f) is a 2-cocycle of B' % name)
            # another choice of phi(t) (add an element of L^N) gives the
            # same class
            choice = {ti: [1] + [0] * (dN - 1) for ti in range(nB)}
            vec2 = delta_cocycle(f, choice)
            check(in_span(sub(vec, vec2), BB2E, p),
                  '%s: delta does not depend on phi(t)' % name)
        deltas.append(vec)
    # delta of principal derivations is zero in H^2(B, L^N)
    for b in BN1:
        if dN:
            check(in_span(delta_cocycle(b), BB2E, p),
                  '%s: delta(principal) = 0' % name)
    # maps t^1, r^1, t^2
    ZG1v = [combine(z, [[1 if j == i else 0 for j in range(nG * d)]
                        for i in range(nG * d)], p) for z in ZG1]
    BG1E = ech(BG1, p)
    # Der(B, L^N)
    ZB1 = kernel(dB1, nB * nB * dN, p) if dN else []
    BB1 = coboundary0(nB, dN, actB) if dN else []

    def t1(fB):
        out = []
        for g in range(nG):
            out += combine(fB[coset[g] * dN:coset[g] * dN + dN], fixN, p)
        return out

    def r1(fG):
        out = []
        for h in N:
            out += fG[h * d:h * d + d]
        return out

    def t2(alpha):
        out = []
        for g1 in range(nG):
            for g2 in range(nG):
                i = (coset[g1] * nB + coset[g2]) * dN
                out += combine(alpha[i:i + dN], fixN, p) if dN else [0] * d
        return out
    BG2 = coboundary1(G.mul, nG, d, actG)       # images of C^1 = B^2(G, L)
    BG2E = ech(BG2, p)
    # exactness at H^1(B, L^N): t^1 injective on classes
    if dN and ZB1:
        ZB1v = [combine(z, [[1 if j == i else 0 for j in range(nB * dN)]
                            for i in range(nB * dN)], p) for z in ZB1]
        BB1E = ech(BB1, p)
        for x in kernel([t1(z) for z in ZB1v] + BG1, nG * d, p):
            fB = combine(x[:len(ZB1v)], ZB1v, p)
            check(in_span(fB, BB1E, p), '%s: t^1 injective' % name)
        # Im t^1 subset Ker r^1
        for z in ZB1v:
            check(in_span(r1(t1(z)), BN1E, p), '%s: r^1 t^1 = 0' % name)
    else:
        ZB1v = []
    # Ker r^1 subset Im t^1 + B^1(G)
    imt1E = ech([t1(z) for z in ZB1v] + BG1, p)
    for x in kernel([r1(z) for z in ZG1v] + BN1, nN * d, p):
        fG = combine(x[:len(ZG1v)], ZG1v, p)
        check(in_span(fG, imt1E, p), '%s: Ker r^1 = Im t^1' % name)
    # Im r^1 = Ker delta (in Der^inv / B^1(N))
    imr1E = ech([r1(z) for z in ZG1v] + BN1, p)
    DinvE = ech(Dinv + BN1, p)
    for z in ZG1v:
        check(in_span(r1(z), DinvE, p),
              '%s: Im r^1 consists of invariant classes' % name)
        if dN:
            check(in_span(delta_cocycle(r1(z)), BB2E, p),
                  '%s: delta r^1 = 0' % name)
    if dN and Dinv:
        for x in kernel(deltas + BB2, nB * nB * dN, p):
            f = combine(x[:len(Dinv)], Dinv, p)
            check(in_span(f, imr1E, p), '%s: Ker delta = Im r^1' % name)
    # Im delta = Ker t^2 (in H^2(B, L^N))
    if dN:
        for v in deltas:
            check(in_span(t2(v), BG2E, p), '%s: t^2 delta = 0' % name)
        imdE = ech(deltas + BB2, p)
        for x in kernel([t2(z) for z in ZB2v] + BG2, nG * nG * d, p):
            alpha = combine(x[:len(ZB2v)], ZB2v, p)
            check(in_span(alpha, imdE, p), '%s: Ker t^2 = Im delta' % name)
    nonzero = any(not in_span(v, BB2E, p) for v in deltas) if dN else False
    if expect_delta_nonzero is not None:
        check(nonzero == expect_delta_nonzero,
              '%s: delta %s' % (name, 'nonzero' if expect_delta_nonzero
                                else 'zero'))


def trivial_module(G, N, coset, p):
    return {g: [[1]] for g in range(G.n)}, 1


def sign_module(G, N, coset, p):
    rho = {}
    for g in range(G.n):
        s = int(libgap.SignPerm(libgap.PermList(
            [v + 1 for v in G.perms[g]])))
        rho[g] = [[s % p]]
    return rho, 1


def coset_module(G, N, coset, p):
    nB = max(coset.values()) + 1
    reps = {}
    for g in range(G.n):
        reps.setdefault(coset[g], g)
    rho = {}
    for g in range(G.n):
        m = [[0] * nB for _ in range(nB)]
        for c in range(nB):
            m[c][coset[G.mul[reps[c]][g]]] = 1
        rho[g] = m
    return rho, nB


def subgroup_coset_module(Cgap):
    def module(G, N, coset, p):
        C = set(G.elt(x) for x in Cgap.AsSSortedList())
        cos = {}
        reps = []
        for g in range(G.n):
            if g in cos:
                continue
            reps.append(g)
            for c in C:
                cos[G.mul[c][g]] = len(reps) - 1
        k = len(reps)
        rho = {}
        for g in range(G.n):
            m = [[0] * k for _ in range(k)]
            for i, r_ in enumerate(reps):
                m[i][cos[G.mul[r_][g]]] = 1
            rho[g] = m
        return rho, k
    return module


def section_5():
    S = libgap.eval
    G = S('DihedralGroup(IsPermGroup, 8)')
    N = [H for H in G.NormalSubgroups()
         if int(H.Size()) == 4 and H.IsCyclic()][0]
    c = [x for x in G.AsSSortedList()
         if int(x.Order()) == 2 and x not in N][0]
    five_term_case('D_8/Z_4 (F_2[C\\G])', G, N, 2,
                   subgroup_coset_module(G.Subgroup([c])), None,
                   expect_n_moves_cocycles=True)
    for nm, src in [('Q_8/Z', 'SmallGroup(8, 4)'),
                    ('D_8/Z', 'SmallGroup(8, 3)'),
                    ('D_16/Z', 'SmallGroup(16, 7)'),
                    ('Q_16/Z', 'SmallGroup(16, 9)')]:
        G = S(src)
        five_term_case(nm, G, G.Centre(), 2, trivial_module, True)
    G = S('CyclicGroup(IsPermGroup, 4)')
    five_term_case('Z_4/Z_2', G, G.Subgroup([G.GeneratorsOfGroup()[0] ** 2]),
                   2, trivial_module, True)
    G = S('Group((1,2), (3,4))')
    five_term_case('Z_2^2/Z_2', G, G.Subgroup([S('(1,2)')]), 2,
                   trivial_module, False)
    G = S('SymmetricGroup(3)')
    five_term_case('S_3/A_3 (F_3 sign)', G, S('AlternatingGroup(3)'), 3,
                   sign_module, False)
    G = S('AlternatingGroup(4)')
    five_term_case('A_4/V_4 (F_2[G/N])', G,
                   G.Subgroup([S('(1,2)(3,4)'), S('(1,3)(2,4)')]), 2,
                   coset_module, False)


# ---------------------------------------------------------------------------
# Finite abelian groups B with free resolutions; homology X (x)_B M
# ---------------------------------------------------------------------------

class Cyclic:
    def __init__(self, n):
        self.n = n
        self.els = list(range(n))
        self.e = 0
        self.nonid = list(range(1, n))

    def mul(self, a, b):
        return (a + b) % self.n

    def inv(self, a):
        return (-a) % self.n

    def resdiff(self, m):
        if m % 2:
            return [0], [0], {(0, 0): {1 % self.n: 1, 0: -1}}
        return [0], [0], {(0, 0): {j: 1 for j in range(self.n)}}

    def rank(self, m):
        return 1


class Klein4:
    """Z_2 x Z_2 with the tensor product of two periodic resolutions."""

    def __init__(self):
        self.els = [(0, 0), (1, 0), (0, 1), (1, 1)]
        self.e = (0, 0)
        self.nonid = self.els[1:]

    def mul(self, a, b):
        return ((a[0] + b[0]) % 2, (a[1] + b[1]) % 2)

    def inv(self, a):
        return a

    @staticmethod
    def _u(i, g):
        if i % 2:
            return {g: 1, (0, 0): -1}
        return {(0, 0): 1, g: 1}

    def resdiff(self, m):
        src = [(i, m - i) for i in range(m + 1)]
        tgt = [(i, m - 1 - i) for i in range(m)]
        D = {}
        for a, (i, j) in enumerate(src):
            if i > 0:
                D[(a, tgt.index((i - 1, j)))] = self._u(i, (1, 0))
            if j > 0:
                s = (-1) ** i
                D[(a, tgt.index((i, j - 1)))] = {
                    g: s * c for g, c in self._u(j, (0, 1)).items()}
        return src, tgt, D

    def rank(self, m):
        return m + 1


def dmat(B, rho, m):
    """Differential X_m (x)_B M -> X_(m-1) (x)_B M (rows)."""
    N = rho[B.e].nrows()
    if m == 0:
        return matrix(ZZ, N * B.rank(0), 0)
    src, tgt, D = B.resdiff(m)
    big = matrix(ZZ, N * len(src), N * len(tgt))
    for (a, b), r in D.items():
        big.set_block(a * N, b * N, sum(c * rho[B.inv(g)]
                                        for g, c in r.items()))
    return big


def homology(B, rho, m):
    N = rho[B.e].nrows()
    V = ZZ ** (N * B.rank(m))
    if m > 0:
        Z = V.span(dmat(B, rho, m).left_kernel().basis())
    else:
        Z = V
    Dn = dmat(B, rho, m + 1)
    Bd = V.span([v * Dn for v in (ZZ ** (N * B.rank(m + 1))).basis()])
    return Z, Bd


def check_resolution(B, rho, mmax, name):
    for m in range(2, mmax + 1):
        check((dmat(B, rho, m) * dmat(B, rho, m - 1)).is_zero(),
              '%s: d d = 0 in X (x)_B M, m = %d' % (name, m))


def inbasis(P, D):
    M = P * D * P.inverse()
    assert all(x in ZZ for x in M.list())
    return M.change_ring(ZZ)


def diag(*s):
    return diagonal_matrix(QQ, s)


BCC = matrix(QQ, [[1, 0, 0], [0, 1, 0], [QQ(1) / 2, QQ(1) / 2, QQ(1) / 2]])
FCC = matrix(QQ, [[0, QQ(1) / 2, QQ(1) / 2], [QQ(1) / 2, 0, QQ(1) / 2],
                  [QQ(1) / 2, QQ(1) / 2, 0]])


def lamk(M, k):
    r = M.nrows()
    basis = list(combinations(range(r), k))
    L = matrix(ZZ, len(basis), len(basis))
    for a, I in enumerate(basis):
        rows = M.matrix_from_rows(list(I))
        for b, J in enumerate(basis):
            L[a, b] = rows.matrix_from_columns(list(J)).det() if k else 1
    return L


# ---------------------------------------------------------------------------
# U(A), the function f of lem:dk-direct-sum and the model of D^k
# ---------------------------------------------------------------------------

def uprod(vecs, r, one=1):
    """Product of linear forms in U(A) = S(A)/(e_i^2): frozenset -> coeff."""
    cur = {frozenset(): one}
    for v in vecs:
        new = {}
        for S, c in cur.items():
            for j in range(r):
                if v[j] and j not in S:
                    key = S | {j}
                    new[key] = new.get(key, 0) + c * v[j]
        cur = {k: c for k, c in new.items() if c}
    return cur


def ftau(vecs, r):
    """tau((1/2) a_1 ... a_k (a_1 + ... + a_k)) as a set of (k+1)-subsets."""
    s = tuple(sum(v[j] for v in vecs) for j in range(r))
    P = uprod(list(vecs) + [s], r)
    out = set()
    for S, c in P.items():
        assert c % 2 == 0
        if (c // 2) % 2:
            out.add(tuple(sorted(S)))
    return out


def wedge_coords(vecs, r):
    k = len(vecs)
    M = matrix(ZZ, [list(v) for v in vecs]) if k else None
    out = {}
    for I in combinations(range(r), k):
        v = M.matrix_from_columns(list(I)).det() if k else 1
        if v:
            out[I] = v
    return out


def rho_D(M, k):
    """B-action on D^k = Lambda^(k+1) (x) Z_2 (+) Lambda^k (lem:dk-direct-sum),
    integral lift; the first block is read mod 2."""
    r = M.nrows()
    Bk = list(combinations(range(r), k))
    Bk1 = list(combinations(range(r), k + 1))
    C = matrix(ZZ, len(Bk), len(Bk1))
    for a, I in enumerate(Bk):
        vecs = [vector(ZZ, unit(r, j)) * M for j in I]
        for S in ftau(vecs, r):
            C[a, Bk1.index(S)] = 1
    top = matrix(ZZ, len(Bk1), len(Bk))
    return block_matrix([[lamk(M, k + 1), top], [C, lamk(M, k)]],
                        subdivide=False), len(Bk1), len(Bk)


# ---------------------------------------------------------------------------
# The standard complex Y = R(A) (x)_A Z (split case)
# ---------------------------------------------------------------------------

def dY(y):
    out = {}
    for tup, c in y.items():
        k = len(tup)
        if k == 0:
            continue
        addto(out, tup[:-1], c)
        for i in range(k - 1):
            addto(out, tup[:i] + (vadd(tup[i], tup[i + 1]),) + tup[i + 2:],
                  c * (-1) ** (k - 1 - i))
        addto(out, tup[1:], c * (-1) ** k)
    return out


def act_t(t, M):
    return tuple(int(v) for v in vector(ZZ, t) * M)


def yact(y, M):
    out = {}
    for tup, c in y.items():
        addto(out, tuple(act_t(t, M) for t in tup), c)
    return out


def alt(ts):
    out = {}
    for q in permutations(range(len(ts))):
        addto(out, tuple(ts[i] for i in q), perm_sign(q))
    return out


def ycorr(c, u, v):
    """The element y of lem:alt-linearity-defect: sum of sign(w) (a_w(1),
    ..., a_w(n+1)) over w with n before n + 1, a = (c, u, v)."""
    a = list(c) + [u, v]
    n = len(a) - 1
    out = {}
    for q in permutations(range(n + 1)):
        if q.index(n - 1) < q.index(n):
            addto(out, tuple(a[i] for i in q), perm_sign(q))
    return out


def lin_last(c, y, r):
    """alt(c, y) = sum_j coeff_j alt(c, e_j) + d(W)."""
    z = tuple([0] * r)
    coeffs, W = {}, {}
    dadd(W, ycorr(c, z, z))
    s = z
    for j in range(r):
        e = unit(r, j)
        for _ in range(abs(y[j])):
            if y[j] > 0:
                addto(coeffs, j, 1)
                dadd(W, ycorr(c, s, e), -1)
                s = vadd(s, e)
            else:
                sm = vadd(s, vneg(e))
                addto(coeffs, j, -1)
                dadd(W, ycorr(c, sm, e), 1)
                s = sm
    return coeffs, W


def is_unit(t):
    return sum(1 for x in t if x) == 1 and all(x in (0, 1) for x in t)


def lin_alt(ts, r):
    """alt(ts) = sum c_I alt(e_I) + d(W) (I increasing)."""
    n = len(ts)
    for p_ in range(n):
        if not is_unit(ts[p_]):
            break
    else:
        idx = [t.index(1) for t in ts]
        if len(set(idx)) < n:
            return {}, {}
        sg = perm_sign(sorted(range(n), key=lambda i: idx[i]))
        return {tuple(sorted(idx)): sg}, {}
    sw = list(ts)
    sgn = 1
    if p_ != n - 1:
        sw[p_], sw[n - 1] = sw[n - 1], sw[p_]
        sgn = -1
    coeffs, W = lin_last(tuple(sw[:-1]), sw[-1], r)
    outc, outW = {}, {}
    dadd(outW, W, sgn)
    for j, cf in coeffs.items():
        nt = list(ts)
        nt[p_] = unit(r, j)
        c2, W2 = lin_alt(tuple(nt), r)
        for kk, v in c2.items():
            addto(outc, kk, cf * v)
        dadd(outW, W2, cf)
    return outc, outW


def dprime(B, slots, m, act_slot):
    src, tgt, D = B.resdiff(m)
    out = [{} for _ in tgt]
    for (a, b), r in D.items():
        for g, c in r.items():
            dadd(out[b], act_slot(slots[a], B.inv(g)), c)
    return out


def split_d2_actual(B, Ms, z, m, k, r):
    """d^2_(m k) of X (x)_B Y on the class of the cycle z by
    prop:bicomplex-d2; returns the element of X_(m-2) (x)_B Lambda^(k+1)."""
    Bk = list(combinations(range(r), k))
    nb = len(Bk)
    s = B.rank(m)
    sym = [[(int(z[nb * sl + a]), tuple(unit(r, j) for j in I))
            for a, I in enumerate(Bk) if z[nb * sl + a]] for sl in range(s)]
    src, tgt, D = B.resdiff(m)
    out = [[] for _ in tgt]
    for (a, b), rr in D.items():
        for g, c in rr.items():
            Mi = Ms[B.inv(g)]
            for cf, ts in sym[a]:
                out[b].append((c * cf, tuple(act_t(t, Mi) for t in ts)))
    W = []
    for sl in out:
        tot, Wt, ex = {}, {}, {}
        for cf, ts in sl:
            c2, W2 = lin_alt(ts, r)
            for kk, v in c2.items():
                addto(tot, kk, cf * v)
            dadd(Wt, W2, cf)
            dadd(ex, alt(ts), cf)
        assert tot == {}
        assert dY(Wt) == ex
        W.append({t: c * (-1) ** m for t, c in Wt.items()})
    v = dprime(B, W, m - 1, lambda y, g: yact(y, Ms[g]))
    res = []
    Bk1 = list(combinations(range(r), k + 1))
    f = factorial(k + 1)
    for vs in v:
        assert dY(vs) == {}
        acc = {}
        for ts, c in vs.items():
            for I, val in wedge_coords(ts, r).items():
                addto(acc, I, c * val)
        vec = [acc.get(I, 0) for I in Bk1]
        assert all(x % f == 0 for x in vec)
        res += [x // f for x in vec]
    return vector(ZZ, res)


def split_d2_predicted(B, Ms, z, m, k):
    """Bockstein of the connecting map of (5.20) (D^k model)."""
    rho = {}
    for g in B.els:
        rho[g], n1, n0 = rho_D(Ms[g], k)
    lift = []
    for sl in range(B.rank(m)):
        lift += [0] * n1 + list(z[n0 * sl:n0 * sl + n0])
    y = vector(ZZ, lift) * dmat(B, rho, m)
    yx = []
    for sl in range(B.rank(m - 1)):
        blk = y[(n1 + n0) * sl:(n1 + n0) * (sl + 1)]
        assert all(v == 0 for v in blk[n1:])
        yx += list(blk[:n1])
    ww = vector(ZZ, yx) * dmat(B, {g: lamk(Ms[g], k + 1) for g in B.els},
                               m - 1)
    assert all(v % 2 == 0 for v in ww)
    return vector(ZZ, [v // 2 for v in ww])


def split_case(name, B, Ms, k, mmax, expect_nonzero=None):
    r = Ms[B.e].nrows()
    for g in B.els:
        for h in B.els:
            assert Ms[g] * Ms[h] == Ms[B.mul(g, h)]
    rk = {g: lamk(Ms[g], k) for g in B.els}
    rk1 = {g: lamk(Ms[g], k + 1) for g in B.els}
    check_resolution(B, rk, mmax, name)
    nonzero = False
    for m in range(2, mmax + 1):
        Zk, Bk_ = homology(B, rk, m)
        Q = Zk / Bk_
        Z1, B1 = homology(B, rk1, m - 2)
        Q1 = Z1 / B1
        for g in Q.gens():
            z = g.lift()
            act_ = split_d2_actual(B, Ms, z, m, k, r)
            pred = split_d2_predicted(B, Ms, z, m, k)
            check(act_ in Z1 and pred in Z1,
                  '%s k=%d m=%d: values are cycles' % (name, k, m))
            check(Q1(act_) == Q1(pred),
                  'th:split-d2-bockstein %s k=%d m=%d' % (name, k, m))
            check(2 * Q1(act_) == 0,
                  'prop:d2-image-two-torsion %s k=%d m=%d' % (name, k, m))
            nonzero = nonzero or Q1(act_) != 0
    if expect_nonzero is not None:
        check(nonzero == expect_nonzero,
              '%s k=%d: d^2 %s' % (name, k, 'nonzero' if expect_nonzero
                                   else 'zero'))
    return nonzero


# ---------------------------------------------------------------------------
# Section 6
# ---------------------------------------------------------------------------

def dk_presentation(r, k, reading):
    """The group presented by the box generators of D^k(Z^r) (entries in
    {0,1}); returns (FGP module, generator list, relation rows)."""
    S = [tuple(v) for v in product((0, 1), repeat=r)]
    syms = list(product(S, repeat=k))
    sidx = {s: i for i, s in enumerate(syms)}
    Bk1 = list(combinations(range(r), k + 1))
    n1 = len(Bk1)
    ngen = len(syms) + n1
    rels = []

    def wedge_mod2(vecs):
        row = [0] * ngen
        for I, v in wedge_coords(vecs, r).items():
            row[len(syms) + Bk1.index(I)] += v
        return row
    for i in range(n1):
        row = [0] * ngen
        row[len(syms) + i] = 2
        rels.append(row)
    for s in syms:
        for i in range(k):
            for j in range(i + 1, k):
                row = [0] * ngen
                if reading == 'alt':
                    if s[i] == s[j]:
                        row[sidx[s]] = 1
                        rels.append(row)
                else:
                    t = list(s)
                    t[i], t[j] = t[j], t[i]
                    row[sidx[s]] += 1
                    row[sidx[tuple(t)]] += 1
                    rels.append(row)
    for i in range(k):
        for u in S:
            for v in S:
                w = vadd(u, v)
                if w not in S:
                    continue
                for rest in product(S, repeat=k - 1):
                    def put(x):
                        return tuple(rest[:i]) + (x,) + tuple(rest[i:])
                    row = [0] * ngen
                    row[sidx[put(w)]] += 1
                    row[sidx[put(u)]] -= 1
                    row[sidx[put(v)]] -= 1
                    vecs = list(rest[:i]) + [u, v] + list(rest[i:])
                    corr = wedge_mod2(vecs)
                    row = [a - b for a, b in zip(row, corr)]
                    rels.append(row)
    R = matrix(ZZ, rels)
    return invariants_of(R, ngen), syms, Bk1, R


def invariants_of(R, ngen):
    """Invariants of Z^ngen / (row space of R), as FGP_Module.invariants()."""
    ed = [int(x) for x in R.elementary_divisors() if x != 0]
    tors = tuple(x for x in ed if x != 1)
    return tors + (0,) * (ngen - len(ed))


def section_6():
    random.seed(4)
    # --- D^k: alternating reading gives (5.20); sign-change reading fails
    for r, k in [(1, 1), (1, 2), (2, 1), (2, 2), (2, 3), (3, 1), (3, 2),
                 (3, 3), (4, 2)]:
        Qinv, syms, Bk1, rels = dk_presentation(r, k, 'alt')
        Bk = list(combinations(range(r), k))
        n1, n0 = len(Bk1), len(Bk)
        T = (ZZ ** (n1 + n0)) / (ZZ ** (n1 + n0)).span(
            [vector(ZZ, unit(n1 + n0, i)) * 2 for i in range(n1)])

        def fimg(s):
            v = [0] * (n1 + n0)
            for S in ftau(s, r):
                v[Bk1.index(S)] = 1
            for I, c in wedge_coords(s, r).items():
                v[n1 + Bk.index(I)] += c
            return vector(ZZ, v)
        images = [fimg(s) for s in syms] + [vector(ZZ, unit(n1 + n0, i))
                                            for i in range(n1)]
        Fm = matrix(ZZ, images)
        RF = rels * Fm
        check(all(RF[i, j] % 2 == 0 for i in range(RF.nrows())
                  for j in range(n1))
              and RF.matrix_from_columns(list(range(n1, n1 + n0))).is_zero(),
              'lem:dk-direct-sum: f kills all %d relations (r=%d, k=%d)'
              % (RF.nrows(), r, k))
        check(T.V().span([T(im).lift() for im in images]
                         + list(T.W().basis())) == T.V(),
              'f onto Lambda^(k+1) (x) Z_2 (+) Lambda^k (r=%d, k=%d)'
              % (r, k))
        check(Qinv == T.invariants(),
              'lem:dk-exact-sequence (alternating): D^k(Z^%d) = %s, k=%d'
              % (r, T.invariants(), k))
        if k >= 2:
            Qs, _, _, _ = dk_presentation(r, k, 'sign')
            refuted(Qs == T.invariants(),
                    'box presentation with relation 1) as a sign change is '
                    'Lambda^(k+1) (x) Z_2 (+) Lambda^k (r=%d, k=%d): %s'
                    % (r, k, Qs))
            check(sum(1 for x in Qs if x == 2)
                  > sum(1 for x in T.invariants() if x == 2),
                  'sign-change reading: extra 2-torsion (r=%d, k=%d)'
                  % (r, k))
    Qs, _, _, _ = dk_presentation(1, 2, 'sign')
    check(Qs == (2,), 'D^2(Z) with sign change only: Z_2')
    # g = product of first coordinates mod 2: sign-change + quasilinear,
    # not alternating; (5.20) would force it to factor through Lambda^k
    box = (-1, 0, 1, 2)
    for r in (1, 2, 3):
        for k in (2, 3):
            if r ** k * 4 ** (r * (k + 1)) > 300000:
                vecs = [tuple(v) for v in product(box, repeat=r)]
                sample = [tuple(random.choice(vecs) for _ in range(k + 1))
                          for _ in range(3000)]
            else:
                vecs = [tuple(v) for v in product(box, repeat=r)]
                sample = list(product(vecs, repeat=k + 1))

            def g(ts):
                out = 1
                for t in ts:
                    out *= t[0]
                return out % 2
            ok = True
            for tup in sample:
                a, a2, rest = tup[0], tup[1], tup[2:]
                for i in range(k):
                    full = list(rest[:i]) + [a] + list(rest[i:])
                    full2 = list(rest[:i]) + [a2] + list(rest[i:])
                    fsum = list(rest[:i]) + [vadd(a, a2)] + list(rest[i:])
                    ok = ok and (g(fsum) - g(full) - g(full2)) % 2 == 0
                full = (a, a2) + tuple(rest[:k - 2])
                sw = (a2, a) + tuple(rest[:k - 2])
                ok = ok and (g(full) + g(sw)) % 2 == 0
            check(ok, 'g satisfies sign change and quasilinearity (r=%d, k=%d)'
                  % (r, k))
            e1 = unit(r, 0)
            check(g([e1] * k) == 1 and wedge_coords([e1] * k, r) == {},
                  'g(e_1, ..., e_1) = 1 but e_1 ^ ... ^ e_1 = 0 (r=%d, k=%d)'
                  % (r, k))
    # --- lem:dk-direct-sum symbolically
    for r in (1, 2, 3, 4):
        for k in (1, 2, 3):
            names = ['x%d_%d' % (i, j) for i in range(k + 1)
                     for j in range(r)]
            R = PolynomialRing(ZZ, names)
            X = R.gens()
            vs = [[X[i * r + j] for j in range(r)] for i in range(k + 1)]

            def P(vecs):
                s = [sum(v[j] for v in vecs) for j in range(r)]
                return uprod(list(vecs) + [s], r, R(1))
            P0 = P(vs[:k])
            check(all(all(c % 2 == 0 for c in poly.coefficients())
                      for poly in P0.values()),
                  'U(A): a_1..a_k(a_1+..+a_k) has even coefficients '
                  '(r=%d, k=%d)' % (r, k))
            # (5.21)/(5.22): before division by 2
            a1p = [vs[0][j] + vs[k][j] for j in range(r)]
            lhs = P([a1p] + vs[1:k])
            rhs = {}
            for D_ in (P(vs[:k]), P([vs[k]] + vs[1:k]),
                       uprod([vs[0], vs[k]] + vs[1:k], r, R(2))):
                for S, c in D_.items():
                    rhs[S] = rhs.get(S, 0) + c
            check({S: c for S, c in lhs.items() if c}
                  == {S: c for S, c in rhs.items() if c},
                  'eq:tau-quasilinearity before division (r=%d, k=%d)'
                  % (r, k))
            # alternation of f: put a_i = a_j, reduce (1/2)P mod 2 as a
            # Boolean function
            for i in range(k):
                for j in range(i + 1, k):
                    sub_ = {X[j * r + t]: X[i * r + t] for t in range(r)}
                    Pij = P([[v.subs(sub_) for v in vec] for vec in vs[:k]])
                    for S, c in Pij.items():
                        half = R(c / 2)
                        boolean = {}
                        for mon, cf in zip(half.monomials(),
                                           half.coefficients()):
                            key = tuple(1 if e else 0 for e in mon.degrees())
                            boolean[key] = (boolean.get(key, 0) + cf) % 2
                        check(all(v == 0 for v in boolean.values()),
                              'f alternating: tau part vanishes for a_%d = '
                              'a_%d (r=%d, k=%d)' % (i, j, r, k))
    # --- the action formula of p. 279 and exc:d1-action
    random.seed(5)
    Ms_test = [inbasis(FCC, diag(-1, 1, 1)), inbasis(BCC, diag(1, -1, -1)),
               matrix(ZZ, [[1, 1, 0], [0, 1, 0], [0, 0, 1]]),
               matrix(ZZ, [[0, 1, 0], [0, 0, 1], [1, 0, 0]])]
    for M in Ms_test:
        r = 3
        for k in (1, 2):
            rho, n1, n0 = rho_D(M, k)
            Bk = list(combinations(range(r), k))
            Bk1 = list(combinations(range(r), k + 1))
            for _ in range(40):
                vecs = [tuple(random.randint(-3, 3) for _ in range(r))
                        for _ in range(k)]
                w = wedge_coords(vecs, r)
                elt = vector(ZZ, [0] * n1 + [w.get(I, 0) for I in Bk])
                img = elt * rho
                bv = [act_t(v, M) for v in vecs]
                printed = [0] * n1
                for S in ftau(bv, r):
                    printed[Bk1.index(S)] += 1
                fa = [0] * n1
                for S in ftau(vecs, r):
                    fa[Bk1.index(S)] += 1
                fab = vector(ZZ, fa) * lamk(M, k + 1)
                printed = [(x + y) % 2 for x, y in zip(printed, fab)]
                wb = wedge_coords(bv, r)
                check([x % 2 for x in img[:n1]] == printed
                      and list(img[n1:]) == [wb.get(I, 0) for I in Bk],
                      'p. 279 action formula / exc:d1-action (k=%d)' % k)
    # exc:base-differential-splitting: D^0 = A (x) Z_2 (+) Z
    for M in Ms_test:
        rho, n1, n0 = rho_D(M, 0)
        check(n1 == 3 and n0 == 1 and all(x == 0 for x in rho.row(n1)[:n1])
              and rho[n1, n1] == 1,
              'exc:base-differential-splitting: D^0 = A (x) Z_2 (+) Z as '
              'B-modules')
    D0 = (ZZ ** 4) / (ZZ ** 4).span([vector(ZZ, unit(4, i)) * 2
                                       for i in range(3)])
    check(D0.invariants() == (2, 2, 2, 0), 'D^0(Z^3) = Z_2^3 (+) Z')
    refuted(D0.invariants() == (0, 0, 0, 0),
            'exc:base-differential-splitting: printed D^0 = A (+) Z, '
            'A = Z^3')
    # exc:invariant-basis-splitting (signed permutations: no correction)
    for perm in permutations(range(3)):
        for signs in product((1, -1), repeat=3):
            M = matrix(ZZ, 3, 3)
            for i in range(3):
                M[i, perm[i]] = signs[i]
            for k in (1, 2, 3):
                rho, n1, n0 = rho_D(M, k)
                check(all(rho[n1 + a, b] == 0 for a in range(n0)
                          for b in range(n1)),
                      'exc:invariant-basis-splitting (signed permutation, '
                      'k=%d)' % k)
    # D^1 splits for every action on Z^2: an invariant quadratic
    # refinement q(a) = a_1 + a_1 a_2 + a_2 (mod 2) of det(a, a') mod 2
    for M in [matrix(ZZ, 2, 2, list(t)) for t in product((0, 1), repeat=4)]:
        if M.det() % 2 == 0:
            continue
        def q(v):
            return (v[0] + v[0] * v[1] + v[1]) % 2
        for a in product((0, 1), repeat=2):
            for a2 in product((0, 1), repeat=2):
                s = vadd(a, a2)
                check((q(s) - q(a) - q(a2)
                       - (a[0] * a2[1] - a[1] * a2[0])) % 2 == 0,
                      'q refines det mod 2')
            aM = act_t(a, M)
            check(q(aM) == q(a), 'q invariant under GL_2(F_2)')
    # exc:u-not-module: (e_1^2, e_2^2) not invariant under e_1 -> e_1 + e_2
    Rp = PolynomialRing(ZZ, ['e1', 'e2'])
    e1, e2 = Rp.gens()
    I_ = Rp.ideal([e1 ** 2, e2 ** 2])
    check((e1 + e2) ** 2 not in I_,
          'exc:u-not-module: (e_1 + e_2)^2 not in (e_1^2, e_2^2)')
    # --- lem:alt-linearity-defect, universal case, n <= 5
    for n in range(1, 6):
        r = n + 1
        a = [unit(r, j) for j in range(r)]
        lhs = alt(tuple(a[:n]))
        dadd(lhs, alt(tuple(a[:n - 1]) + (a[n],)))
        rhs = alt(tuple(a[:n - 1]) + (vadd(a[n - 1], a[n]),))
        dadd(rhs, dY(ycorr(tuple(a[:n - 1]), a[n - 1], a[n])))
        check(lhs == rhs, 'lem:alt-linearity-defect, n = %d' % n)
    # exc:alt-identity-n2: 12 terms, 6 cancel
    a = [unit(3, j) for j in range(3)]
    terms = []
    for q in permutations(range(3)):
        if q.index(1) < q.index(2):
            tup = tuple(a[i] for i in q)
            for t, c in dY({tup: perm_sign(q)}).items():
                terms.append((t, c))
    check(len(terms) == 12, 'exc:alt-identity-n2: 12 terms')
    tot = {}
    for t, c in terms:
        addto(tot, t, c)
    cancelled = len(terms) - sum(abs(c) for c in tot.values())
    check(cancelled == 6, 'exc:alt-identity-n2: 6 of them cancel')
    # cor:alt-exterior-iso ingredients
    for n in range(1, 6):
        r = n + 1
        a = [unit(r, j) for j in range(r)]
        check(dY(alt(tuple(a[:n]))) == {}, 'alt(e_1..e_n) is a cycle, n=%d'
              % n)
        acc = {}
        for ts, c in alt(tuple(a[:n])).items():
            for I, v in wedge_coords(ts, r).items():
                addto(acc, I, c * v)
        check(acc == {tuple(range(n)): factorial(n)},
              'f_n(alt) = n! a_1 ^ ... ^ a_n, n = %d' % n)
        acc = {}
        for ts, c in dY({tuple(a[:n + 1]): 1}).items():
            for I, v in wedge_coords(ts, r).items():
                addto(acc, I, c * v)
        check(acc == {}, 'f_n vanishes on boundaries, n = %d' % n)
        # the printed last term (-1)^(n+1) a_2 ^ ... ^ a_n (degree n - 1)
        if n >= 2:
            printed = {}
            for ts, c in dY({tuple(a[:n + 1]): 1}).items():
                if ts == tuple(a[1:n + 1]):
                    ts = tuple(a[1:n])
                for I, v in wedge_coords(ts, r).items():
                    addto(printed, (len(ts),) + I, c * v)
            refuted(printed == {}, 'printed f_n(d(..)) with last term '
                    'a_2 ^ ... ^ a_n, n = %d' % n)
        # phi(y) = (1/2)(n+1)! a_1 ^ ... ^ a_(n+1)
        y = ycorr(tuple(a[:n - 1]), a[n - 1], a[n])
        check(sum(abs(c) for c in y.values()) == factorial(n + 1) // 2,
              'number of permutations with n before n + 1 is (1/2)(n+1)!')
        acc = {}
        for ts, c in y.items():
            for I, v in wedge_coords(ts, r).items():
                addto(acc, I, c * v)
        check(acc == {tuple(range(n + 1)): factorial(n + 1) // 2},
              'phi(y) = (1/2)(k+1)! a_1 ^ ... ^ a_(k+1), k = %d' % n)
    # --- th:split-d2-bockstein on lattices
    K4 = Klein4()

    def k4(s, t):
        return {(0, 0): identity_matrix(ZZ, s.nrows()), (1, 0): s,
                (0, 1): t, (1, 1): s * t}
    mm2F = k4(inbasis(FCC, diag(-1, 1, 1)), inbasis(FCC, diag(1, -1, 1)))
    s222F = k4(inbasis(FCC, diag(1, -1, -1)), inbasis(FCC, diag(-1, 1, -1)))
    mm2I = k4(inbasis(BCC, diag(-1, 1, 1)), inbasis(BCC, diag(1, -1, 1)))
    s222I = k4(inbasis(BCC, diag(1, -1, -1)), inbasis(BCC, diag(-1, 1, -1)))
    split_case('F(mm2)', K4, mm2F, 1, 6, expect_nonzero=True)
    split_case('F(222)', K4, s222F, 1, 5)
    split_case('I(mm2)', K4, mm2I, 1, 5)
    split_case('I(222)', K4, s222I, 1, 5)
    for nm, Ms in [('F(mm2)', mm2F), ('F(222)', s222F), ('I(mm2)', mm2I),
                   ('I(222)', s222I)]:
        split_case(nm, K4, Ms, 2, 5)
    s3, t3 = mm2F[(1, 0)], mm2F[(0, 1)]
    for es, et in [(1, 1), (-1, -1)]:
        Ms = k4(block_diagonal_matrix(s3, matrix(ZZ, [[es]])),
                block_diagonal_matrix(t3, matrix(ZZ, [[et]])))
        split_case('F(mm2)+Z(%d,%d)' % (es, et), K4, Ms, 2, 5,
                   expect_nonzero=True)
    Ms = k4(block_diagonal_matrix(s3, matrix(ZZ, [[0, 1], [1, 0]])),
            block_diagonal_matrix(t3, identity_matrix(ZZ, 2)))
    split_case('F(mm2)+Z[Z_2]', K4, Ms, 3, 4, expect_nonzero=True)
    # Z_4 acting on the I-lattice (D^1 does not split, d^2 vanishes)
    C4 = Cyclic(4)
    R4 = inbasis(BCC, matrix(QQ, [[0, 1, 0], [-1, 0, 0], [0, 0, 1]]))
    Ms = {j: R4 ** j for j in range(4)}
    split_case('I(4)', C4, Ms, 1, 6, expect_nonzero=False)


# ---------------------------------------------------------------------------
# Section 7: P_G, chi_k, the bicomplex for non-split extensions
# ---------------------------------------------------------------------------

class PGModel:
    """P_G for an extension given by point-group matrices Ms[b] (on A) and
    translation parts tau[b] (in lattice coordinates):
    s(b) = (M_b, tau_b), x . (M, t) = x M + t."""

    def __init__(self, B, Ms, tau):
        self.B, self.Ms, self.tau = B, Ms, tau
        r = Ms[B.e].nrows()
        self.r = r
        self.nonid = B.nonid
        nw = len(B.nonid)
        self.nw = nw
        self.NP = r + nw
        self.rP = {c: self._rho(c) for c in B.els}
        self.Wb = {c: self.rP[c].matrix_from_rows_and_columns(
            list(range(r, self.NP)), list(range(r, self.NP)))
            for c in B.els}
        self.delta = {c: tuple(1 if (c != B.e and B.nonid.index(c) == i)
                               else 0 for i in range(nw)) for c in B.els}
        self.Z0 = tuple([0] * nw)

    def f(self, b, c):
        B = self.B
        bc = B.mul(b, c)
        v = (self.tau[b] * self.Ms[c] + self.tau[c] - self.tau[bc]) \
            * self.Ms[bc].inverse()
        assert all(x in ZZ for x in v)
        return vector(ZZ, v)

    def _rho(self, c):
        B, r = self.B, self.r
        R = matrix(ZZ, self.NP, self.NP)
        R.set_block(0, 0, self.Ms[c])
        for i, b in enumerate(B.nonid):
            row = vector(ZZ, [0] * self.NP)
            bc = B.mul(b, c)
            row[:r] = self.f(b, c) * self.Ms[bc]
            if bc != B.e:
                row[r + B.nonid.index(bc)] += 1
            if c != B.e:
                row[r + B.nonid.index(c)] -= 1
            R.set_row(r + i, row)
        return R

    def pact(self, c, g):
        return tuple(int(v) for v in vector(ZZ, c) * self.rP[g])

    def xact(self, x, g):
        return tuple(int(v) + d_ for v, d_ in
                     zip(vector(ZZ, x) * self.Wb[g], self.delta[g]))

    def proj(self, c):
        return tuple(c[self.r:])

    def lift(self, x):
        return tuple([0] * self.r + list(x))

    def yact(self, y, g):
        out = {}
        for (cs, x), c in y.items():
            addto(out, (tuple(self.pact(cc, g) for cc in cs),
                        self.xact(x, g)), c)
        return out

    def dY(self, y):
        out = {}
        for (cs, x), c in y.items():
            n = len(cs)
            if n == 0:
                continue
            addto(out, (cs[:-1], vadd(x, self.proj(cs[-1]))), c)
            for i in range(n - 1):
                addto(out, (cs[:i] + (vadd(cs[i], cs[i + 1]),) + cs[i + 2:],
                            x), c * (-1) ** (n - 1 - i))
            addto(out, (cs[1:], x), c * (-1) ** n)
        return out

    def bnd0(self, y):
        W = {}
        for ((), x), n in y.items():
            addto(W, ((self.lift(x),), self.Z0), n)
        assert self.dY(W) == y
        return W

    def bnd1(self, y):
        Z0, W, T = self.Z0, {}, {}
        for ((c,), x), n in y.items():
            if any(x):
                xh = self.lift(x)
                addto(T, vadd(c, xh), n)
                addto(T, xh, -n)
                addto(W, ((c, xh), Z0), n)
            else:
                addto(T, c, n)
        T2 = {}
        for c, n in T.items():
            x = self.proj(c)
            if any(x):
                xh = self.lift(x)
                a = vadd(c, vneg(xh))
                addto(T2, xh, n)
                addto(T2, a, n)
                addto(W, ((xh, a), Z0), -n)
            else:
                addto(T2, c, n)
        assert all(not any(self.proj(c)) for c in T2)
        s = tuple([0] * self.NP)
        addto(W, ((s, s), Z0), -1)
        for a, c in T2.items():
            for _ in range(abs(c)):
                if c > 0:
                    addto(W, ((s, a), Z0), 1)
                    s = vadd(s, a)
                else:
                    sm = vadd(s, vneg(a))
                    addto(W, ((sm, a), Z0), -1)
                    s = sm
        assert not any(s)
        addto(W, ((s, s), Z0), 1)
        assert self.dY(W) == y
        return W

    def actual_d2(self, z, m, k):
        B, r = self.B, self.r
        s = B.rank(m)
        if k == 0:
            a = [{((), self.Z0): int(z[sl])} if z[sl] else {}
                 for sl in range(s)]
            u = dprime(B, a, m, self.yact)
            W = [self.bnd0(us) for us in u]
        else:
            a = [{((tuple(list(z[r * sl:r * sl + r]) + [0] * self.nw),),
                   self.Z0): 1} for sl in range(s)]
            u = dprime(B, a, m, self.yact)
            W = [self.bnd1(us) for us in u]
        a2 = [{t: c * (-1) ** m for t, c in w.items()} for w in W]
        v = dprime(B, a2, m - 1, self.yact)
        res = []
        BA = list(combinations(range(r), k + 1))
        fk = factorial(k + 1)
        for vs in v:
            assert self.dY(vs) == {}
            acc = {}
            for (cs, x), c in vs.items():
                for I, val in wedge_coords(cs, self.NP).items():
                    addto(acc, I, c * val)
            assert all(all(i < r for i in I) for I in acc)
            vec = [acc.get(I, 0) for I in BA]
            assert all(x_ % fk == 0 for x_ in vec)
            res += [x_ // fk for x_ in vec]
        return vector(ZZ, res)

    def wedgeP_rho(self, k, b):
        """B-action on Lambda^k(A) ^ P_G with basis Lambda^(k+1)(A) (+)
        Lambda^k(A) (x) W (W = the w-coordinates)."""
        r, nw = self.r, self.nw
        Bk = list(combinations(range(r), k))
        Bk1 = list(combinations(range(r), k + 1))
        n1, nk = len(Bk1), len(Bk)
        L = lamk(self.Ms[b], k)

        def pi(I, p_):
            v = [0] * (n1 + nk * nw)
            for j in range(r):
                if p_[j]:
                    J = I + (j,)
                    if len(set(J)) == k + 1:
                        sg = perm_sign(sorted(range(k + 1),
                                              key=lambda t: J[t]))
                        v[Bk1.index(tuple(sorted(J)))] += sg * p_[j]
            for i in range(nw):
                v[n1 + Bk.index(I) * nw + i] += p_[r + i]
            return vector(ZZ, v)
        R = matrix(ZZ, n1 + nk * nw, n1 + nk * nw)
        R.set_block(0, 0, lamk(self.Ms[b], k + 1))
        for ii, I in enumerate(Bk):
            for i in range(nw):
                p_ = [0] * self.NP
                p_[r + i] = 1
                pb = self.pact(tuple(p_), b)
                v = vector(ZZ, [0] * (n1 + nk * nw))
                for jj, J in enumerate(Bk):
                    if L[ii, jj]:
                        v += L[ii, jj] * pi(J, pb)
                R.set_row(n1 + ii * nw + i, v)
        return R, n1, nk

    def chi(self, z, m, k):
        B, r, nw = self.B, self.r, self.nw
        nB = len(B.els)
        Bk = list(combinations(range(r), k))
        nk = len(Bk)
        L = {b: lamk(self.Ms[b], k) for b in B.els}

        def rhoLZB(b):
            R = matrix(ZZ, nk * nB, nk * nB)
            for gi, g in enumerate(B.els):
                R.set_block(gi * nk, B.els.index(B.mul(g, b)) * nk, L[b])
            return R
        rZB = {b: rhoLZB(b) for b in B.els}
        rAP = {}
        for b in B.els:
            rAP[b], n1, _ = self.wedgeP_rho(k, b)
        for b in B.els:
            for c in B.els:
                assert rAP[b] * rAP[c] == rAP[B.mul(b, c)]
        lz = []
        for sl in range(B.rank(m)):
            lz += list(z[nk * sl:nk * sl + nk]) + [0] * (nk * (nB - 1))
        y = vector(ZZ, lz) * dmat(B, rZB, m)
        lifted = []
        e_i = B.els.index(B.e)
        assert e_i == 0
        for sl in range(B.rank(m - 1)):
            blk = y[nB * nk * sl:nB * nk * (sl + 1)]
            for ii in range(nk):
                assert sum(blk[gi * nk + ii] for gi in range(nB)) == 0
            v = [0] * (n1 + nk * nw)
            for ii in range(nk):
                for i, g in enumerate(B.nonid):
                    v[n1 + ii * nw + i] = blk[B.els.index(g) * nk + ii]
            lifted += v
        y2 = vector(ZZ, lifted) * dmat(B, rAP, m - 1)
        res = []
        for sl in range(B.rank(m - 2)):
            blk = y2[(n1 + nk * nw) * sl:(n1 + nk * nw) * (sl + 1)]
            assert all(x_ == 0 for x_ in blk[n1:])
            res += list(blk[:n1])
        return vector(ZZ, res)


def nonsplit_case(name, model, mmax, forced_iso=None, expect=None):
    B, Ms, r = model.B, model.Ms, model.r
    # P_G is a B-module; A is a submodule with quotient Delta_B
    for b in B.els:
        for c in B.els:
            check(model.rP[b] * model.rP[c] == model.rP[B.mul(b, c)],
                  '%s: P_G is a B-module' % name)
        check(model.rP[b].matrix_from_rows_and_columns(
            list(range(r)), list(range(r, model.NP))).is_zero(),
            '%s: A is a submodule of P_G' % name)
        for i, g in enumerate(B.nonid):
            # (g - 1) b = (g b - 1) - (b - 1) in Delta_B
            want = [0] * model.nw
            gb = B.mul(g, b)
            if gb != B.e:
                want[B.nonid.index(gb)] += 1
            if b != B.e:
                want[B.nonid.index(b)] -= 1
            check(list(model.Wb[b].row(i)) == want,
                  '%s: P_G / A = Delta_B (eq:pg-exact-sequence)' % name)
    # eq:y-exponential-action commutes with d
    random.seed(11)
    for _ in range(25):
        n = random.randint(1, 3)
        y = {(tuple(tuple(random.randint(-2, 2) for _ in range(model.NP))
                    for _ in range(n)),
              tuple(random.randint(-2, 2) for _ in range(model.nw))): 1}
        for g in B.els:
            check(model.dY(model.yact(y, g)) == model.yact(model.dY(y), g),
                  '%s: eq:y-exponential-action commutes with d' % name)
    # lem:alt-action-correction, n <= min(3, r)
    for n in range(1, min(3, r) + 1):
        for _ in range(5):
            avs = [tuple(random.randint(-2, 2) for _ in range(r))
                   + model.Z0 for _ in range(n)]
            for b in B.els:
                if b == B.e:
                    continue
                lhs = model.yact({k_: c for k_, c in
                                  ((((t), model.Z0), c) for t, c in
                                   alt(tuple(avs)).items())}, b)
                ab = [model.pact(t, b) for t in avs]
                rhs = {(t, model.Z0): c for t, c in alt(tuple(ab)).items()}
                a_ = model.lift(model.delta[b])
                corr = {}
                for t, c in alt(tuple(ab) + (a_,)).items():
                    addto(corr, (t, model.Z0), c)
                dadd(rhs, model.dY(corr))
                check(lhs == rhs, '%s: lem:alt-action-correction, n=%d'
                      % (name, n))
    # th:abelian-kernel-d2
    results = {}
    for k in (0, 1):
        if k == 1 and r < 2:
            continue
        rk = {g: lamk(Ms[g], k) for g in B.els}
        rk1 = {g: lamk(Ms[g], k + 1) for g in B.els}
        for m in range(2, mmax + 1):
            Zk, Bk_ = homology(B, rk, m)
            Q = Zk / Bk_
            Z1, B1 = homology(B, rk1, m - 2)
            Q1 = Z1 / B1
            vals = []
            for g in Q.gens():
                z = g.lift()
                ad = Q1(model.actual_d2(z, m, k))
                ch = Q1(model.chi(z, m, k))
                db = Q1(split_d2_predicted(B, Ms, z, m, k)) if k else Q1(0)
                vals.append((ad, ch, db))
            check(all(a_ == c_ + d_ for a_, c_, d_ in vals)
                  or all(a_ == -c_ + d_ for a_, c_, d_ in vals),
                  'th:abelian-kernel-d2 %s k=%d m=%d: d^2 = chi + d-bar^2'
                  % (name, k, m))
            results[(k, m)] = (Q, Q1, vals)
    if forced_iso:
        for (k, m) in forced_iso:
            Q, Q1, vals = results[(k, m)]
            images = [v[0] for v in vals]
            check(len(Q.invariants()) == len(Q1.invariants())
                  and Q.cardinality() == Q1.cardinality()
                  and Q1.submodule(images).cardinality()
                  == Q1.cardinality(),
                  '%s: d^2_(%d %d) is an isomorphism %s -> %s (forced by '
                  'the homology of G)' % (name, m, k, Q.invariants(),
                                          Q1.invariants()))
    if expect:
        expect(results)
    return results


def section_7():
    # --- G = Z, A = mZ, B = Z_m (central extension)
    for mm in (2, 3, 4):
        B = Cyclic(mm)
        Ms = {j: identity_matrix(ZZ, 1) for j in range(mm)}
        tau = {j: vector(QQ, [QQ(j) / mm]) for j in range(mm)}
        model = PGModel(B, Ms, tau)
        # P_G = Z[Z_m] with A = Z N: a -> N, w_b -> 1 + b + ... + b^(j-1)
        F = matrix(ZZ, model.NP, mm)
        F[0] = vector(ZZ, [1] * mm)
        for i, b in enumerate(B.nonid):
            # w_b = u(t^b) = t^b - 1 = (t - 1)(1 + t + ... + t^(b-1))
            for j in range(b):
                F[1 + i, j] = 1
        check(F.det() in (1, -1), 'G = Z, A = %dZ: P_G = Z[Z_m] (lattice)'
              % mm)
        perm = {b: matrix(ZZ, mm, mm, lambda i, j: 1 if j == (i + b) % mm
                          else 0) for b in B.els}
        for b in B.els:
            check(model.rP[b] * F == F * perm[b],
                  'G = Z, A = %dZ: P_G = Z[Z_m], A = Z N' % mm)
        forced = [(0, m) for m in range(3, 7, 2)]
        nonsplit_case('G=Z/A=%dZ' % mm, model, 6, forced_iso=forced)
    # --- Klein bottle group: A = <x^2, y> = Z^2, B = Z_2
    B = Cyclic(2)
    Ms = {0: identity_matrix(ZZ, 2), 1: matrix(ZZ, [[1, 0], [0, -1]])}
    tau = {0: vector(QQ, [0, 0]), 1: vector(QQ, [QQ(1) / 2, 0])}
    model = PGModel(B, Ms, tau)
    check(model.f(1, 1) == vector(ZZ, [1, 0]),
          'Klein bottle: s(t)^2 = x^2 (the factor set)')
    # forced by H_n(K) = 0 (n >= 2): d^2_(2j+3, 0) and d^2_(2j, 1) iso
    nonsplit_case('Klein', model, 5,
                  forced_iso=[(0, 3), (0, 5), (1, 2), (1, 4)])
    # --- Fdd2: B = mm2 on the F-lattice, d-glides
    K4 = Klein4()
    q4 = QQ(1) / 4
    Ds = {(0, 0): diag(1, 1, 1), (1, 0): diag(-1, 1, 1),
          (0, 1): diag(1, -1, 1), (1, 1): diag(-1, -1, 1)}
    ts = {(0, 0): vector(QQ, [0, 0, 0]), (1, 0): vector(QQ, [q4, q4, q4]),
          (0, 1): vector(QQ, [q4, q4, q4]), (1, 1): vector(QQ, [0, 0, 0])}
    Ms = {g: inbasis(FCC, D) for g, D in Ds.items()}
    tau = {g: t * FCC.inverse() for g, t in ts.items()}
    model = PGModel(K4, Ms, tau)

    def fdd2_expect(results):
        both = False
        for m in range(2, 6):
            Q, Q1, vals = results[(1, m)]
            for a_, c_, d_ in vals:
                if c_ != 0 and d_ != 0:
                    both = True
                    refuted(a_ == c_, 'Fdd2: d^2_(%d 1) = chi alone' % m)
                    refuted(a_ == d_, 'Fdd2: d^2_(%d 1) = d-bar^2 alone' % m)
        check(both, 'Fdd2: chi and d-bar^2 both nonzero at k = 1')
        check(any(v[0] != 0 for m in range(2, 6)
                  for v in results[(0, m)][2]),
              'Fdd2: d^2_(m 0) = chi_(m 0) is nonzero (non-split)')
    nonsplit_case('Fdd2', model, 5, expect=fdd2_expect)
    # --- the relation defining Lambda^k(A) ^ P_G (p. 285), k = 1
    for r in (1, 2, 3):
        gens = [(i, j) for i in range(r) for j in range(r)]
        idx = {g: n for n, g in enumerate(gens)}
        printed, corrected = [], []
        for i in range(r):
            for j in range(r):
                row = [0] * len(gens)
                row[idx[(i, j)]] += 1
                row[idx[(j, i)]] += 1
                printed.append(row)
        for v in product((-1, 0, 1), repeat=r):
            row = [0] * len(gens)
            for i in range(r):
                for j in range(r):
                    row[idx[(i, j)]] += v[i] * v[j]
            corrected.append(row)
        V = ZZ ** len(gens)
        lam2 = tuple([0] * (r * (r - 1) // 2))
        refuted((V / V.span(printed)).invariants() == lam2,
                'p. 285 printed relation: A (x) A / (sign change) = '
                'Lambda^2(A), r = %d (got %s)'
                % (r, (V / V.span(printed)).invariants()))
        check((V / V.span(corrected)).invariants() == lam2,
              'p. 285 corrected relation a (x) a = 0: Lambda^1 (x) A / rel '
              '= Lambda^2(A), r = %d' % r)
    # --- the last diagram of the proof (ranks)
    for nm, B, Ms, tau in [
            ('G=Z/A=3Z', Cyclic(3), {j: identity_matrix(ZZ, 1)
                                     for j in range(3)},
             {j: vector(QQ, [QQ(j) / 3]) for j in range(3)}),
            ('Fdd2', K4, Ms, tau)]:
        model = PGModel(B, Ms, tau)
        r = model.r
        for k in range(1, r + 1):
            rk_l1 = binomial_(r, k + 1)
            rk_lk = binomial_(r, k)
            rk_wedgeP = rk_l1 + rk_lk * model.nw
            rk_l1P = binomial_(model.NP, k + 1)
            # exact 0 -> L^(k+1) -> M -> P^k_0 -> L^k -> 0 with
            # 0 -> L''_k -> P^k_0 -> L^k -> 0,
            # L''_k = (L^k ^ P_G) / (k+1)! L^(k+1)
            rk_P0 = (rk_wedgeP - rk_l1) + rk_lk
            forced = rk_l1 + rk_P0 - rk_lk
            check(forced == rk_wedgeP,
                  '%s k=%d: corrected top row (Lambda^k ^ P_G) passes the '
                  'rank count' % (nm, k))
            if rk_l1P != rk_wedgeP:
                refuted(forced == rk_l1P,
                        '%s k=%d: printed top row with Lambda^(k+1)(P_G) '
                        '(rank %d, forced %d)' % (nm, k, rk_l1P, forced))
            check(2 * (factorial(k + 1) // 2) == factorial(k + 1),
                  'left square: 2 (1/2)(k+1)! = (k+1)!')
    refuted(factorial(1) % 2 == 0, '(1/2)(k+1)! is an integer at k = 0')
    # k = 0: P^0_0 = Z u (+) Delta_B with u b = u + (b - 1) is Z B
    for B in (Cyclic(2), Cyclic(3), K4):
        nB = len(B.els)
        # basis u, (g - 1) for g != 1; map Z B -> P^0_0, g -> u g
        F = matrix(ZZ, nB, nB)
        for i, g in enumerate(B.els):
            F[i, 0] = 1
            if g != B.e:
                F[i, 1 + B.nonid.index(g)] = 1
        check(F.det() in (1, -1), 'k = 0: Z B -> P^0_0, g -> u g, is onto '
              'and injective')
    # d(alt(c_1..c_n)) in R(P) (proof of lem:alt-action-correction)
    for n in range(1, 5):
        r = n
        c = [unit(r, j) for j in range(r)]
        # R(P) = V (x) Z P: elements {(tuple, exponent): coeff}
        lhs = {}
        for t, s in alt(tuple(c)).items():
            n_ = len(t)
            addto(lhs, (t[:-1], t[-1]), s)
            for i in range(n_ - 1):
                addto(lhs, (t[:i] + (vadd(t[i], t[i + 1]),) + t[i + 2:],
                            tuple([0] * r)), s * (-1) ** (n_ - 1 - i))
            addto(lhs, (t[1:], tuple([0] * r)), s * (-1) ** n_)
        rhs = {}
        for i in range(n):
            rest = tuple(c[:i] + c[i + 1:])
            for t, s in alt(rest).items():
                addto(rhs, (t, c[i]), s * (-1) ** (n - 1 - i))
                addto(rhs, (t, tuple([0] * r)), -s * (-1) ** (n - 1 - i))
        check(lhs == rhs, 'lem:alt-action-correction proof: d alt(c) = '
              'sum (-1)^(n-i) alt(..) (x) '
              '(e^(c_i) - 1), n = %d' % n)


def binomial_(n, k):
    from sage.all import binomial
    return int(binomial(n, k))


def main():
    section_5()
    section_6()
    section_7()
    print('ok %s: %d checks' % (SCOPE, COUNT[0]))


if __name__ == '__main__':
    main()
