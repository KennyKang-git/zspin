#!/usr/bin/env python3
"""ZS-M75 v1.3.1: inherited and added finite checks of the repaired and extended seed,
the v1.1 additions (sharp local return law, sublattice hidden blindness,
blind-set line dichotomy, time-symmetric-without-gauge family), and the v1.2
additions (N<=3 minimality of hidden blindness, negated-mirror return-blind
sites, unitary-block hidden blindness on K_{n,n}, forced resonance of the
4-cycle family and its Lambda obstruction on a time grid).

Run: python zs_m75_verify_v1_3_1.py --out zs_m75_verify_v1_3_1.json
Requires Python >=3.11, numpy, scipy, sympy. No input files or network.
Inherited checks use density jets and amplitude powers; new audit checks use
separately written amplitude convolution and exact symbolic subidentities.
Universal theorems are proved in the manuscript; these finite tests are not
formal proofs, novelty verdicts, grade certificates, or physical experiments.
Fault modes mutate calculations and must produce nonzero exit status.
"""
from __future__ import annotations

import argparse
from collections import deque
import json
import math
from pathlib import Path
import platform
import sys

import numpy as np
import scipy
from scipy.linalg import expm
import sympy as s

VERSION = '1.3.1'
SEED = 75260927
I = s.I


def iszero(matrix):
    return all(s.simplify(z) == 0 for z in matrix)


def graph(n, edges):
    K = s.zeros(n)
    for a, b, weight in edges:
        K[b, a] = s.sympify(weight)
        K[a, b] = s.conjugate(weight)
    return K


def cycle(n, phase=1):
    return graph(n, [(a, (a+1) % n, phase if a == 0 else 1)
                     for a in range(n)])


def diag_site(n, x, value=1):
    V = s.zeros(n)
    V[x, x] = value
    return V


def density_series(H, a, order):
    """Coefficients L_H^k(P_a)/k!, L_H=-i[H, .]."""
    rho = diag_site(H.rows, a)
    out = [rho]
    for k in range(1, order+1):
        rho = (-I*(H*rho-rho*H)/k).applyfunc(s.expand)
        out.append(rho)
    return out


def contrast_series(K, V, a, order):
    plus = density_series(K+V, a, order)
    minus = density_series(K-V, a, order)
    return [p-m for p, m in zip(plus, minus)]


def pulse_series(Hs, a, order):
    """All pulses have duration t; combine density-superoperator series."""
    out = [diag_site(Hs[0].rows, a)]+[s.zeros(Hs[0].rows) for _ in range(order)]
    for H in Hs:
        new = [s.zeros(H.rows) for _ in range(order+1)]
        for k, rho in enumerate(out):
            term = rho
            new[k] += term
            for r in range(1, order-k+1):
                term = (-I*(H*term-term*H)/r).applyfunc(s.expand)
                new[k+r] += term
        out = new
    return out


def pop_diagonal_zero(rho):
    return all(s.simplify(rho[a, a]) == 0 for a in range(rho.rows))


def rooted_odd_length(K, x, inject=None):
    """Shortest odd CLOSED WALK, using the graph's parity double cover."""
    n = K.rows
    neighbors = [[b for b in range(n) if K[b, a] != 0] for a in range(n)]
    if inject == 'rooted_cycle':
        # Deliberately reproduce the seed's wrong SIMPLE-cycle restriction.
        found = []
        def dfs(path):
            for b in neighbors[path[-1]]:
                if b == x and len(path) >= 3 and len(path) % 2:
                    found.append(len(path))
                elif b not in path:
                    dfs(path+[b])
        dfs([x])
        return min(found) if found else None
    q = deque([(x, 0, 0)])
    visited = {(x, 0)}
    while q:
        a, parity, dist = q.popleft()
        for b in neighbors[a]:
            nxt = (b, 1-parity)
            if nxt == (x, 1):
                return dist+1
            if nxt not in visited:
                visited.add(nxt)
                q.append((b, 1-parity, dist+1))
    return None


def return_coefficient(K, x, gamma, chi=1):
    return (4*(-1)**((gamma+1)//2)*(1-gamma)
            * (K**gamma)[x, x]*chi/s.factorial(gamma+1))


def common_gauge(Ks, inject=None):
    """Exact spanning-forest test for algebraic inputs; no floating tolerance."""
    n = Ks[0].rows
    adj = [[] for _ in range(n)]
    sign = 1 if inject == 'gauge_sign' else -1
    for j, K in enumerate(Ks):
        if K.shape != (n, n) or not iszero(K-K.conjugate().T):
            raise ValueError('Hermitian matrices of equal size required')
        if any(K[a, a] != 0 for a in range(n)):
            raise ValueError('Zero diagonal required')
        for a in range(n):
            for b in range(n):
                if a != b and K[b, a] != 0:
                    r = s.simplify(sign*K[b, a]/s.conjugate(K[b, a]))
                    adj[a].append((b, r, j))
    phases = [None]*n
    for root in range(n):
        if phases[root] is not None:
            continue
        phases[root] = s.Integer(1)
        q = deque([root])
        while q:
            a = q.popleft()
            for b, r, j in adj[a]:
                candidate = s.simplify(r*phases[a])
                if phases[b] is None:
                    phases[b] = candidate
                    q.append(b)
                elif s.simplify(phases[b]-candidate) != 0:
                    return dict(balanced=False, failed_edge=[a, b, j])
    return dict(balanced=True, phases=phases)


def cycle_leading(K, V, arc1, arc2, inject=None):
    def path_product(arc):
        return s.prod(K[b, a] for a, b in zip(arc[:-1], arc[1:]))
    n1, n2 = len(arc1)-1, len(arc2)-1
    h = s.conjugate(path_product(arc1))*path_product(arc2)
    bracket = (sum(V[a, a] for a in arc2)/(s.factorial(n1)*s.factorial(n2+1))
               - sum(V[a, a] for a in arc1)/(s.factorial(n1+1)*s.factorial(n2)))
    factor = I if inject == 'cycle_phase' else -I
    return s.simplify(4*s.re(factor*I**n1*(-I)**n2*h*bracket))


def arr(M):
    return np.array(M, dtype=complex)


def norm(M):
    return float(np.linalg.norm(M, 2))


def population_contrast(K, V, t):
    return abs(expm(-1j*t*(K+V)))**2-abs(expm(-1j*t*(K-V)))**2


def detuning_bound(A, C, B, t, R):
    b = norm(B)
    return b*b*(2*t+(norm(C)+norm(A)+b)*t*t/2)/abs(R)


def trotter(Ks, V, alpha, t, n, z, inject=None):
    step = np.eye(len(V), dtype=complex)
    for a, K in zip(alpha, Ks):
        # Wrong n scaling is a live calculation fault, not a metadata guard.
        divisor = 1 if inject == 'trotter_step' else n
        step = expm(-1j*a*t/divisor*(K+z*V))@step
    return np.linalg.matrix_power(step, n)



def theoremF_blind(K, V, kmax=None, mask=None):
    """M74 Theorem F certificate: populations of K+V and K-V agree for all t iff
    the derivatives 0..2d(d-1) agree. mask(b,a) restricts the checked entries.
    Returns (all_zero, first_witness)."""
    d = K.rows; kmax = 2*d*(d-1) if kmax is None else kmax
    for a in range(d):
        rp = diag_site(d, a); rm = diag_site(d, a)
        for k in range(kmax+1):
            for b in range(d):
                if mask is None or mask(b, a):
                    if s.simplify(rp[b, b]-rm[b, b]) != 0:
                        return False, (a, b, k, str(s.simplify(rp[b, b]-rm[b, b])))
            rp = (-I*((K+V)*rp-rp*(K+V))).applyfunc(s.expand)
            rm = (-I*((K-V)*rm-rm*(K-V))).applyfunc(s.expand)
    return True, None


def return_contrast_jets(K, x, chi, order):
    """Taylor coefficients of Delta M_xx for V = chi P_x via density jets."""
    V = diag_site(K.rows, x, chi)
    return [s.simplify(j[x, x]) for j in contrast_series(K, V, x, order)]


def moment_law(K, x, chi, inject=None):
    """Predicted first branch-odd return coefficient: degree 2k+2 where 2k+1 is
    the least odd n with (K^n)_xx != 0; value 8k(-1)^k m_{2k+1} chi/(2k+2)!."""
    n = 1
    while n <= 2*K.rows*K.rows:
        m = s.simplify((K**n)[x, x])
        if m != 0:
            k = (n-1)//2
            const = 8*k*(-1)**k if inject != 'moment_constant' else 8*k*(-1)**(k+1)
            return n+1, s.simplify(const*m*chi/s.factorial(n+1))
        n += 2
    return None, s.Integer(0)


def sublattice_blocks(K, A, inject=None):
    """Return (Bmat, GA, GB) for a bipartite K with parts A and complement."""
    n = K.rows; Bidx = [i for i in range(n) if i not in A]
    Bm = s.Matrix([[K[a, b] for b in Bidx] for a in A])   # A x B block, entries K_{ab}
    Bt = Bm.T if inject == 'sublattice_formula' else Bm.conjugate().T
    return Bm, (Bm*Bt).applyfunc(s.expand), (Bt*Bm).applyfunc(s.expand), Bidx


def run_legacy(inject=None):
    rows = []
    def row(rid, cls, claim, passed, **data):
        item = dict(id=rid, cls=cls, claim=claim, passed=bool(passed), data=data)
        rows.append(item)
        print(rid, cls, 'PASS' if passed else 'FAIL', claim, flush=True)

    observations = []
    ok = True
    for n in range(3, 8):
        K = cycle(n, 1 if n % 2 else I)
        V = diag_site(n, 2)
        jets = contrast_series(K, V, 0, n+1)
        predicted = cycle_leading(K, V, [0, 1], [0]+list(range(n-1, 0, -1)), inject)
        actual = s.simplify(jets[n+1][1, 1])
        low_zero = all(pop_diagonal_zero(jets[k]) for k in range(n+1))
        ok &= low_zero and s.simplify(actual-predicted) == 0 and actual != 0
        observations.append(dict(length=n, coefficient=str(actual), prediction=str(predicted)))
    row('C01', 'C', 'Induced C3..C7: girth barrier and nonzero cycle coefficient', ok, cases=observations)

    leaf = graph(4, [(0,1,1),(1,2,1),(2,3,1),(3,1,1)])
    attached = graph(10, [(a,(a+1)%7,1) for a in range(7)]
                     +[(0,7,1),(7,8,1),(8,9,1),(9,7,1)])
    data=[]; ok=True
    for name, K in [('leaf_triangle',leaf),('C7_attached_triangle',attached)]:
        gamma = rooted_odd_length(K, 0, inject)
        jets = contrast_series(K, diag_site(K.rows,0),0,8)
        actual = s.simplify(jets[6][0,0])
        predicted = return_coefficient(K,0,gamma) if gamma == 5 else s.Integer(0)
        ok &= gamma == 5 and actual == predicted == s.Rational(2,45)
        data.append(dict(graph=name, gamma=gamma, coefficient_t6=str(actual),
                         coefficient_t8=str(jets[8][0,0])))
    row('C02','C','Exact counterexamples to the seed SIMPLE-cycle return law',ok,cases=data)

    ok=True; data=[]
    for distance in range(4):
        n=distance+3
        edges=[(a,a+1,1) for a in range(distance)]
        edges += [(distance,distance+1,2),(distance+1,distance+2,-1),(distance+2,distance,3)]
        K=graph(n,edges); gamma=rooted_odd_length(K,0,inject)
        expected=2*distance+3; jets=contrast_series(K,diag_site(n,0,2),0,expected+1)
        c=jets[expected+1][0,0]
        ok &= gamma == expected and all(jets[k][0,0] == 0 for k in range(expected+1))
        ok &= s.simplify(c-return_coefficient(K,0,expected,2)) == 0 and c != 0
        data.append(dict(distance=distance,gamma=gamma,coefficient=str(c)))
    row('C03','C','Rooted odd-walk law with signed weights and roots outside the cycle',ok,cases=data)

    balanced=graph(3,[(0,1,I),(1,2,1),(2,0,1)])
    cert=common_gauge([balanced],inject)
    verified=False
    if cert['balanced']:
        g=s.diag(*cert['phases'])
        verified=iszero(balanced+g*balanced.conjugate()*g.conjugate().T)
    row('C04','C','Nonbipartite imaginary-holonomy triangle has an exact A gauge',verified,
        gauge=[str(x) for x in cert.get('phases',[])])

    cases=[('signed_tree',graph(4,[(0,1,-2),(1,2,3),(1,3,-1)]),True),
           ('real_triangle',cycle(3),False),('flux_C4',cycle(4,I),False),
           ('real_C4',cycle(4),True),('one_vertex',s.zeros(1),True)]
    found=[(name,common_gauge([K],inject)['balanced'],truth) for name,K,truth in cases]
    row('C05','C','Exact gain tests cover signed, complex, disconnected-free and trivial boundaries',
        all(got==truth for _,got,truth in found),cases=found)

    X=s.Matrix([[0,1],[1,0]]);Y=s.Matrix([[0,-I],[I,0]]);Z=s.diag(1,-1)
    plus=pulse_series([X+Z,Y+Z],0,3);minus=pulse_series([X-Z,Y-Z],0,3)
    c=s.simplify(plus[3][1,1]-minus[3][1,1])
    row('C06','C','Unbalanced parallel modes: cubic contrast 8 and no common gauge',
        c==8 and not common_gauge([X,Y],inject)['balanced'],coefficient=str(c))

    Ks=[graph(3,[(a,b,1)]) for a,b in [(0,1),(1,2),(2,0)]]
    individually=all(common_gauge([K],inject)['balanced'] for K in Ks)
    union=common_gauge(Ks,inject)['balanced']
    effective=sum(Ks,s.zeros(3))/3
    effective_blind=common_gauge([effective],inject)['balanced']
    row('C07','C','Three individually blind real modes have an unbalanced union and positive mixture',
        individually and not union and not effective_blind,
        individual_balance=individually,union_balance=union)

    K=graph(4,[(0,1,1),(0,2,1),(1,2,1),(0,3,1),(1,3,-1)])
    d0=contrast_series(K,diag_site(4,0),0,4)[4][1,1]
    d2=contrast_series(K,diag_site(4,2),0,4)[4][1,1]
    row('C08','C','Signed-cycle cancellation at one readout is not universal blindness',
        d0==0 and d2 == -s.Rational(2,3),P0_edge01=str(d0),P2_edge01=str(d2))

    v=s.symbols('v0:4',real=True);K=cycle(4,I);V=s.diag(*v)
    jets=contrast_series(K,V,0,5)
    predicted=cycle_leading(K,V,[0,1],[0,3,2,1],inject)
    row('C09','C','Symbolic diagonal on flux C4: exact arc functional; scalar potentials lie in its kernel',
        s.simplify(jets[5][1,1]-predicted)==0 and predicted.subs(dict.fromkeys(v,1))==0,
        coefficient=str(s.factor(jets[5][1,1])))

    K=cycle(3);V=2*s.eye(3)
    row('W01','W','A fixed scalar V stays blind even when the universal gain test fails',
        not common_gauge([K])['balanced'] and iszero(K*V-V*K) and iszero((K+V)-(K-V)-4*s.eye(3)),
        mechanism='Scalar branch phase; all times, by the displayed matrix identity')

    D=s.diag(1,0);V=D;d=contrast_series(X+D,V,0,4)
    row('W02','W','Nonconstant branch-even diagonal defeats the zero-diagonal gauge criterion',
        common_gauge([X])['balanced'] and d[4][1,1] == -s.Rational(1,3),coefficient=str(d[4][1,1]))

    eig=X.eigenvects();energies=sorted([e[0] for e in eig])
    profiles=[]
    for _,_,vectors in eig:
        q=vectors[0];norm2=(q.conjugate().T*q)[0]
        profiles.append([s.simplify(abs(a)**2/norm2) for a in q])
    row('W03','W','N=2 spectral counterexample: distinct ordered nonzero gaps but equal modulus profiles',
        energies==[-1,1] and profiles[0]==profiles[1],gaps=[-2,2],profiles=[[str(a) for a in p] for p in profiles])

    cases=[];ok=True
    for name,K,csize in [
        ('signed_triangles',graph(4,[(0,1,1),(0,2,1),(1,2,1),(0,3,1),(1,3,-1)]),3),
        ('complex_C4_with_exterior',graph(5,[(0,1,I),(1,2,1),(2,3,1),(3,0,1),
                                          (0,4,1+I),(2,4,s.Rational(1,2))]),4)]:
        Kn=arr(K);W=np.zeros((csize,csize));W[2,2]=1;t=.7
        A0=Kn[:csize,:csize];C=Kn[csize:,csize:];B=Kn[:csize,csize:]
        ideal=float(population_contrast(A0,W,t)[1,0]); errors=[]
        for R in [20.,100.,500.]:
            V=np.zeros(Kn.shape,complex);V[:csize,:csize]=W;V[csize:,csize:]=R*np.eye(len(C))
            actual=float(population_contrast(Kn,V,t)[1,0]); branch_errors=[];bounds=[]
            for z in (1,-1):
                block=expm(-1j*t*(Kn+z*V))[:csize,:csize]
                branch_errors.append(norm(block-expm(-1j*t*(A0+z*W))))
                bounds.append(detuning_bound(A0+z*W,C,B,t,R))
            ok &= all(e <= b+1e-11 for e,b in zip(branch_errors,bounds))
            ok &= abs(actual-ideal) <= 2*sum(bounds)+1e-11
            errors.append(dict(R=R,contrast=actual,operator_errors=branch_errors,bounds=bounds))
        ok &= abs(ideal)>1e-4 and abs(errors[-1]['contrast']-ideal)<abs(ideal)/2
        cases.append(dict(name=name,ideal_contrast=ideal,observations=errors))
    row('V01','V','Exterior detuning isolates signed and complex cycles; explicit norm bounds hold',ok,cases=cases)

    kns=[arr(K) for K in Ks];V=np.diag([0.,0.,1.]);alpha=[1/3]*3;t=.8
    K=sum(kns)/3;exact={z:expm(-1j*t*(K+z*V)) for z in (1,-1)}
    delta=float(abs(exact[1][1,0])**2-abs(exact[-1][1,0])**2)
    observations=[];ok=True
    for n in [1,2,4,16,64,256]:
        U={z:trotter(kns,V,alpha,t,n,z,inject) for z in (1,-1)}
        contrast=float(abs(U[1][1,0])**2-abs(U[-1][1,0])**2)
        errs=[norm(U[z]-exact[z]) for z in (1,-1)]
        bounds=[]
        for z in (1,-1):
            hs=[A+z*V for A in kns]
            comm=sum(alpha[p]*alpha[q]*norm(hs[p]@hs[q]-hs[q]@hs[p])
                     for p in range(3) for q in range(p+1,3))
            bounds.append(t*t*comm/(2*n))
        ok &= all(e<=b+1e-12 for e,b in zip(errs,bounds))
        observations.append(dict(repetitions=n,pulses=3*n,contrast=contrast,errors=errs,bounds=bounds))
    ok &= abs(observations[-1]['contrast']-delta)<abs(delta)/100
    ok &= abs(observations[1]['contrast'])>1e-3
    row('V02','V','Positive-duration Trotter witnesses from individually blind modes, with commutator bounds',
        ok,effective_contrast=delta,observations=observations)

    rng=np.random.default_rng(SEED);n=6
    q=np.diag(np.exp(1j*rng.uniform(-math.pi,math.pi,n)))
    modes=[]
    for _ in range(3):
        A=rng.normal(size=(n,n));A=A-A.T;modes.append(q@(1j*A)@q.conj().T)
    V=np.diag(rng.normal(size=n));tms=[.03,.12,.04,.15,.08];word=[0,2,1,0,2]
    us=[]
    for z in (1,-1):
        U=np.eye(n,dtype=complex)
        for j,t in zip(word,tms):U=expm(-1j*t*(modes[j]+z*V))@U
        us.append(U)
    err=float(np.max(abs(abs(us[0])**2-abs(us[1])**2)))
    row('V03','V','A common imaginary-skew gauge preserves populations for an ordered complex mode word',
        err<2e-12,max_population_error=err,seed=SEED)

    n=7;csize=3;t=.6;R=70.
    A=rng.normal(size=(n,n))+1j*rng.normal(size=(n,n));A=(A+A.conj().T)/2
    W=np.diag([-.4,.3,1.2]);B=A[:csize,csize:];C=A[csize:,csize:];checks=[]
    for z in (1,-1):
        H=A.copy();H[:csize,:csize]+=z*W;H[csize:,csize:]+=z*R*np.eye(n-csize)
        effective=A[:csize,:csize]+z*W
        error=norm(expm(-1j*t*H)[:csize,:csize]-expm(-1j*t*effective))
        bound=detuning_bound(effective,C,B,t,R);checks.append(dict(error=error,bound=bound))
    row('V04','V','General rectangular-block detuning estimate works for both signs and nonzero block diagonals',
        all(c['error']<=c['bound']+1e-11 for c in checks),checks=checks)

    # An explicit strictly positive mixture avoiding cancellation on every edge.
    A=graph(3,[(0,1,1),(1,2,1)]);B=graph(3,[(0,1,-1),(2,0,1)])
    good=s.Rational(1,3)*A+s.Rational(2,3)*B
    bad=(A+B)/2
    row('C10','C','Positive mixing must avoid edge-cancellation hyperplanes',
        good[1,0]!=0 and bad[1,0]==0 and not common_gauge([good])['balanced']
        and common_gauge([bad])['balanced'],good_edge=str(good[1,0]),bad_edge=str(bad[1,0]))


    # ---------------- v1.1 additions ----------------
    chi = s.symbols('chi', real=True)
    # C11: sharp local return law on a Jacobi path with alpha=(0,0,a2): degree 2k+2=6, linear in chi
    a2, b1, b2, b3 = s.symbols('a2 b1 b2 b3', real=True)
    Jm = s.Matrix([[0, b1, 0, 0], [b1, 0, b2, 0], [0, b2, a2, b3], [0, 0, b3, 0]])
    jets = return_contrast_jets(Jm, 0, chi, 7)
    deg, pred = moment_law(Jm, 0, chi, inject)
    ok = deg == 6 and all(j == 0 for j in jets[:6]) and s.simplify(jets[6]-pred) == 0 and s.degree(s.expand(jets[6]), chi) == 1
    row('C11', 'C', 'Sharp return law: first nonzero odd moment fixes degree 2k+2 and the linear-in-chi coefficient (Jacobi k=2)',
        ok, coefficient_t6=str(s.factor(jets[6])), prediction=str(s.factor(pred)))
    # C12: complex K and signed cancellation: moment law with gamma_x < 2k+1
    K = graph(5, [(0, 1, 1), (1, 2, 1), (2, 0, 1), (0, 3, 1), (3, 4, -1), (4, 0, 1)])   # bow-tie (+,-) at 0
    odd = [s.simplify((K**n)[0, 0]) for n in (1, 3, 5, 7, 9, 11)]
    rj = return_contrast_jets(K, 0, chi, 10)
    tr = [s.simplify(j[1, 1]) for j in contrast_series(K, diag_site(5, 0, chi), 0, 4)]
    blind_line, wit = theoremF_blind(K, diag_site(5, 0, 1), mask=lambda b, a: a == 0 and b == 0)
    ok = all(o == 0 for o in odd) and all(j == 0 for j in rj) and blind_line and s.simplify(tr[4]-chi/3) == 0 \
        and rooted_odd_length(K, 0) == 3 and not common_gauge([K])['balanced']
    row('C12', 'C', 'Symmetric local spectral measure: return at x blind for every chi although gamma_x=3 and K is unbalanced; transfer 0->1 visible at t^4',
        ok, odd_moments=[str(o) for o in odd], transfer_t4=str(tr[4]), full_return_certificate=blind_line)
    Kc = graph(4, [(0, 1, s.Rational(3, 5)+s.Rational(4, 5)*I), (1, 2, 1), (2, 0, 1), (0, 3, 1)])   # complex triangle + pendant
    rj = return_contrast_jets(Kc, 0, chi, 5)
    deg, pred = moment_law(Kc, 0, chi, inject)
    ok = deg == 4 and all(j == 0 for j in rj[:4]) and s.simplify(rj[4]-pred) == 0 and s.simplify(pred.subs(chi, 1)) == -s.Rational(2, 5)
    row('C13', 'C', 'Moment law with complex weights: coefficient -(K^3)_xx chi/3 = -(2/5) chi', ok, coefficient=str(rj[4]))
    # C14: sublattice hidden blindness on the flux 4-cycle: exact Theorem-F certificate; unbalanced support
    w = s.Rational(3, 5)+s.Rational(4, 5)*I
    C4 = graph(4, [(0, 1, w), (1, 2, 1), (2, 3, 1), (3, 0, 1)])
    stag = s.diag(1, -1, 1, -1)
    Bm, GA, GB, Bidx = sublattice_blocks(C4, [0, 2], inject)
    # explicit mechanism check: Sigma(K+V)Sigma = -(K-V), and intertwining B f(B^dag B) = f(B B^dag) B on a power
    mech = iszero(stag*(C4+stag)*stag+(C4-stag)) and iszero(Bm*GB**2-GA**2*Bm)
    blind, wit = theoremF_blind(C4, 2*stag)
    ok = mech and blind and not common_gauge([C4])['balanced'] and not theoremF_blind(C4, diag_site(4, 0))[0]
    row('C14', 'C', 'Flux 4-cycle: sublattice potential is fully blind (exact certificate) though the gain graph is unbalanced; P_0 is visible',
        ok, mechanism=mech, certificate=blind, gain_balanced=common_gauge([C4])['balanced'])
    # C15: |A|=2, |B|=3: within-A and cross-sublattice blind, within-B visible; C6 flux staggered visible but cross blind
    K23 = graph(5, [(0, 2, 1+I), (0, 3, 2), (0, 4, 1), (1, 2, 1), (1, 3, I), (1, 4, -1)])
    Vst = s.diag(1, 1, -1, -1, -1)
    inA = lambda b, a: a < 2 and b < 2
    cross = lambda b, a: (a < 2) != (b < 2)
    inB = lambda b, a: a >= 2 and b >= 2
    okA, _ = theoremF_blind(K23, Vst, mask=inA); okX, _ = theoremF_blind(K23, Vst, mask=cross); okB, witB = theoremF_blind(K23, Vst, mask=inB)
    C6 = graph(6, [(a, (a+1) % 6, w if a == 0 else 1) for a in range(6)])
    V6 = s.diag(1, -1, 1, -1, 1, -1)
    cross6 = lambda b, a: (a % 2) != (b % 2)
    okX6, _ = theoremF_blind(C6, V6, mask=cross6); okAll6, wit6 = theoremF_blind(C6, V6)
    ok = okA and okX and not okB and okX6 and not okAll6
    row('C15', 'C', 'Sublattice potentials: cross-sublattice populations always blind; within-part blindness holds for |A|=2 and fails for a 3-part (K_{2,3}, C6)',
        ok, K23=dict(withinA=okA, cross=okX, withinB=okB, witnessB=str(witB)), C6=dict(cross=okX6, all=okAll6, witness=str(wit6)))
    # W04: blind set of the flux 4-cycle along two lines: P_0 line visible at every tested chi, Sigma line blind
    ok = True; obs = []
    for c in (s.Rational(1, 7), 1, 3):
        v_line = not theoremF_blind(C4, c*diag_site(4, 0), kmax=8)[0]
        s_line = theoremF_blind(C4, c*stag)[0]
        obs.append(dict(chi=str(c), P0_visible=v_line, Sigma_blind=s_line)); ok &= v_line and s_line
    row('W04', 'W', 'Line dichotomy on the flux 4-cycle: P_0 line visible, sublattice line blind, scalar shifts irrelevant', ok, observations=obs)
    # V05: time-symmetric propagator without any diagonal Lambda (Biamonte-Turner sentence): numeric
    Kn = arr(C4); Sg = np.diag([1., -1., 1., -1.]); H = Kn+0.7*Sg; ok = True; data = []
    for t in (0.37, 1.1, 2.3):
        U = expm(-1j*t*H); P = abs(U)**2
        sym = float(np.max(abs(P-P.T)))
        cyc = [(0, 1), (1, 2), (2, 3), (3, 0)]
        ratioT = np.prod([U[b, a]/U[a, b] for a, b in cyc])          # Lambda U Lambda^dag = U^T needs product 1
        ratioD = np.prod([U[b, a]/np.conj(U[a, b]) for a, b in cyc])  # Lambda U Lambda^dag = U^dag needs product 1 ...
        diagIm = float(np.max(abs(U.diagonal().imag)))                  # ... and real diagonal entries U_aa
        data.append(dict(t=t, population_asymmetry=sym, cycle_ratio_T=abs(ratioT-1), cycle_ratio_dag=abs(ratioD-1), diagonal_imag_part=diagIm))
        ok &= sym < 1e-12 and abs(ratioT-1) > 1e-6 and (abs(ratioD-1) > 1e-6 or diagIm > 1e-6)
    row('V05', 'V', 'Flux 4-cycle with sublattice potential: populations time-symmetric at every t, yet no diagonal Lambda gives U^T (cycle ratio) or U^dag (non-real diagonal)',
        ok, data=data)
    # V06: within-A contrast formula 4 chi Im(conj(C) S) on a random |A|=3 bipartite network; zero when G_A is gauge-real
    rng2 = np.random.default_rng(SEED+1)
    Bn = rng2.normal(size=(3, 3))+1j*rng2.normal(size=(3, 3)); ok = True; data = []
    for label, Bx in (('generic', Bn), ('gauge_real', np.diag(np.exp(1j*rng2.uniform(0, 6, 3)))@rng2.normal(size=(3, 3)))):
        Kb = np.zeros((6, 6), complex); Kb[:3, 3:] = Bx; Kb[3:, :3] = Bx.conj().T
        GA = Bx@Bx.conj().T; chi_n = 0.8; t = 1.3
        ev, Q = np.linalg.eigh(GA); nu = np.sqrt(ev+chi_n**2)
        Cm = Q@np.diag(np.cos(nu*t))@Q.conj().T; Sm = Q@np.diag(np.sin(nu*t)/nu)@Q.conj().T
        formula = 4*chi_n*np.imag((Cm if inject == 'sublattice_formula' else np.conj(Cm))*Sm)  # dropping the conjugate is a live fault
        Vb = chi_n*np.diag([1, 1, 1, -1, -1, -1.])
        direct = (abs(expm(-1j*t*(Kb+Vb)))**2-abs(expm(-1j*t*(Kb-Vb)))**2)[:3, :3]
        err = float(np.max(abs(formula-direct))); size = float(np.max(abs(direct)))
        data.append(dict(case=label, formula_error=err, within_A_contrast=size))
        ok &= err < 1e-10 and ((size > 1e-3) if label == 'generic' else (size < 1e-12))
    row('V06', 'V', 'Within-sublattice contrast equals 4 chi Im(conj C . S); it vanishes for a gauge-real G_A and not for a generic |A|=3 block', ok, data=data)


    # ---------------- v1.2 additions ----------------
    # C16: N=3 minimality. On an unbalanced triangle the quartic coefficient (7.1) is Re(h)(v_a+v_b-2v_c)/3 for every
    # transition; the three conditions force V scalar. Hence B(K) is the scalar line for every unbalanced K with N<=3.
    k1r, k1i, k2r, k2i, k3r, k3i, v0, v1, v2 = s.symbols('k1r k1i k2r k2i k3r k3i v0 v1 v2', real=True)
    Kt = graph(3, [(0, 1, k1r+I*k1i), (1, 2, k2r+I*k2i), (2, 0, k3r+I*k3i)])
    Vt = s.diag(v0, v1, v2)
    ht = s.expand(Kt[1, 0]*Kt[2, 1]*Kt[0, 2])
    ok = True; data = {}
    for (a, b, cc_) in [(0, 1, 2), (1, 2, 0), (0, 2, 1)]:
        jets = contrast_series(Kt, Vt, a, 4)
        c4 = s.simplify(jets[4][b, b])
        pred = s.Rational(1, 3)*s.re(ht)*(Vt[a, a]+Vt[b, b]-2*Vt[cc_, cc_])
        ok &= all(s.simplify(jets[k][b, b]) == 0 for k in range(4)) and s.simplify(s.expand(c4-pred)) == 0
        data[f'{a}->{b}'] = str(s.factor(c4))
    sol = s.solve([v0+v1-2*v2, v1+v2-2*v0, v0+v2-2*v1], [v0, v1], dict=True)
    ok &= sol == [{v0: v2, v1: v2}]
    row('C16', 'C', 'N=3 minimality: unbalanced triangle quartic coefficient Re(h)(v_a+v_b-2v_c)/3 for all three transitions; the conditions force V scalar (Prop 8.6)',
        ok, coefficients=data, forced_solution=str(sol))
    # C17: negated mirror gluing at x=0 of a complex K4 block: all odd moments at 0 vanish, return at 0 exactly blind for
    # V=P_0 (Theorem-F certificate on the (0,0) entry), support unbalanced (real part of a triangle nonzero), transfer visible.
    K1e = [(0, 1, 1+I), (0, 2, 2), (0, 3, s.Rational(1, 2)-I), (1, 2, 1), (1, 3, I), (2, 3, 1-2*I)]
    Km = s.zeros(7); mp = {0: 0, 1: 4, 2: 5, 3: 6}
    sgn = 1 if inject == 'mirror_sign' else -1     # gluing +K1 instead of -K1 is a live fault: odd moments no longer cancel
    for a, b, wgt in K1e:
        Km[b, a] = wgt; Km[a, b] = s.conjugate(wgt)
        Km[mp[b], mp[a]] = sgn*wgt; Km[mp[a], mp[b]] = sgn*s.conjugate(wgt)
    oddm = [s.simplify((Km**m)[0, 0]) for m in range(1, 15, 2)]
    blind_ret, _ = theoremF_blind(Km, diag_site(7, 0), mask=lambda b, a: a == 0 and b == 0)
    tr4 = s.simplify(contrast_series(Km, diag_site(7, 0), 0, 4)[4][1, 1])
    unb = s.simplify(s.re(Km[1, 0]*Km[2, 1]*Km[0, 2])) != 0
    ok = all(o == 0 for o in oddm) and blind_ret and tr4 != 0 and unb and not common_gauge([Km])['balanced']
    row('C17', 'C', 'Negated mirror gluing (Prop 6.3): complex unbalanced 7-site support with all odd moments at 0 zero, exact return blindness for chi P_0, transfer 0->1 visible at t^4',
        ok, odd_moments=[str(o) for o in oddm], return_certificate=blind_ret, transfer_t4=str(tr4))
    # C18: Fourier K_{3,3}: B unitary => G_A=G_B=I => every sublattice potential completely blind (exact 60-derivative certificate);
    # the support is unbalanced (non-real 4-cycle product).
    om = (-1+I*s.sqrt(3))/2
    Fm = s.Matrix(3, 3, lambda a, b: om**(a*b))/s.sqrt(3)
    Kf = s.zeros(6); Kf[:3, 3:] = Fm; Kf[3:, :3] = Fm.conjugate().T
    Kf = Kf.applyfunc(s.expand)
    cyc = s.simplify(Kf[3, 0]*Kf[1, 3]*Kf[4, 1]*Kf[0, 4])
    Vf = s.Rational(3, 2)*s.diag(1, 1, 1, -1, -1, -1)
    blindF, witF = theoremF_blind(Kf, Vf)
    two_eig = s.simplify((Kf*Kf)-s.eye(6)) == s.zeros(6)
    ok = blindF and s.simplify(s.im(cyc)) != 0 and two_eig and not common_gauge([Kf])['balanced']
    row('C18', 'C', 'Fourier K_{3,3} (Prop 8.7): unitary coupling block, K^2=I, sublattice potential completely blind by exact certificate although the support is unbalanced',
        ok, cycle_product=str(cyc), certificate=blindF, K_squared_identity=two_eig)
    # C19: random Gaussian-rational flux 4-cycles with random chi and nonzero scalar shift c: exact certificate of complete
    # blindness; unbalanced; P_0 visible on 1->2 at t^5 with the Lemma 3.2 value (fault cycle_phase flips that prediction).
    rng3 = np.random.default_rng(SEED+2); ok = True; data = []
    def gr():
        return s.Rational(int(rng3.integers(-2, 3)), int(rng3.integers(1, 3)))+I*s.Rational(int(rng3.integers(-2, 3)), int(rng3.integers(1, 3)))
    for trial in range(2):
        wts = [gr() for _ in range(4)]; wts = [x if x != 0 else s.Integer(1) for x in wts]
        K4 = graph(4, [(0, 1, wts[0]), (1, 2, wts[1]), (2, 3, wts[2]), (3, 0, wts[3])])
        hol = K4[1, 0]*K4[2, 1]*K4[3, 2]*K4[0, 3]
        ch = s.Rational(int(rng3.integers(1, 5)), int(rng3.integers(1, 4))); cs = s.Rational(int(rng3.integers(1, 4)), 2)
        V4 = ch*s.diag(1, -1, 1, -1)+cs*s.eye(4)
        blind4, _ = theoremF_blind(K4, V4)
        jets = contrast_series(K4, diag_site(4, 0), 1, 5)
        pred = cycle_leading(K4, diag_site(4, 0), [1, 2], [1, 0, 3, 2], inject)
        vis = all(pop_diagonal_zero(jets[k]) for k in range(5)) and jets[5][2, 2] != 0 and s.simplify(jets[5][2, 2]-pred) == 0
        ok &= s.simplify(s.im(hol)) != 0 and blind4 and vis
        data.append(dict(weights=[str(x) for x in wts], chi=str(ch), c=str(cs), blind=blind4, P0_t5=str(jets[5][2, 2])))
    row('C19', 'C', 'Random flux 4-cycles with random chi and scalar shift: exact complete-blindness certificate of the sublattice potential; unbalanced; P_0 visible with the Lemma 3.2 coefficient',
        ok, cases=data)
    # V07: forced resonance and Lambda obstruction on a time grid for the flux 4-cycle family (unit weights, flux 0.9, chi 0.7).
    phi = 0.9; chin = 0.7
    Kn4 = np.zeros((4, 4), complex)
    for a, b, wgt in [(0, 1, 1.0), (1, 2, 1.0), (2, 3, 1.0), (3, 0, np.exp(1j*phi))]:
        Kn4[b, a] = wgt; Kn4[a, b] = np.conj(wgt)
    Hn = Kn4+chin*np.diag([1., -1, 1, -1]); ev, Qe = np.linalg.eigh(Hn)
    paired = float(abs(ev+ev[::-1]).max())
    Ep = [np.outer(Qe[:, r], Qe[:, r].conj()) for r in range(4)]
    Xrs = {(r, q): np.imag(Ep[r]*Ep[q].conj()) for r in range(4) for q in range(r+1, 4)}
    gaps = {(r, q): float(ev[q]-ev[r]) for r in range(4) for q in range(r+1, 4)}
    coincide = abs(gaps[(0, 1)]-gaps[(2, 3)]) < 1e-12 and abs(gaps[(0, 2)]-gaps[(1, 3)]) < 1e-12
    indiv = float(max(abs(Xrs[(0, 1)]).max(), abs(Xrs[(0, 2)]).max()))
    merged = float(max(abs(Xrs[(0, 1)]+Xrs[(2, 3)]).max(), abs(Xrs[(0, 2)]+Xrs[(1, 3)]).max()))
    minentry = float(min(abs(E).min() for E in Ep))
    distinct4 = len(set(np.round(ev, 10))) == 4
    ts = np.linspace(0.05, 6, 200); asym = []; ratio = []; dimag = []
    for tt in ts:
        U = expm(-1j*tt*Hn); P = abs(U)**2; asym.append(abs(P-P.T).max())
        ratio.append(abs(np.prod([U[b, a]/U[a, b] for a, b in [(0, 1), (1, 2), (2, 3), (3, 0)]])-1))
        dimag.append(abs(U.diagonal().imag).max())
    asym = np.array(asym); ratio = np.array(ratio); dimag = np.array(dimag)
    ok = paired < 1e-12 and coincide and indiv > 1e-3 and merged < 1e-12 and minentry > 1e-3 and distinct4 \
        and asym.max() < 1e-12 and (ratio < 1e-3).mean() < 0.05 and (dimag < 1e-3).mean() < 0.05
    row('V07', 'V', 'Flux 4-cycle family: four distinct eigenvalues paired +/-nu, gaps coincide in pairs, individual Im(E_r o conj E_s) nonzero but merged coefficients vanish, projectors without zero entries; on a 200-point time grid populations are symmetric while the cycle ratio and the diagonal of U obstruct any diagonal Lambda',
        ok, eigenvalues=[float(x) for x in ev], individual_X=indiv, merged_X=merged, min_projector_entry=minentry,
        max_population_asymmetry=float(asym.max()), fraction_ratio_near_one=float((ratio < 1e-3).mean()), fraction_diag_real=float((dimag < 1e-3).mean()))

    counts={c:sum(r['cls']==c for r in rows) for c in ['P','C','V','W','R','G','X','D','T']}
    return dict(paper='ZS-M75',version=VERSION,random_seed=SEED,injected_fault=inject,
                scope='Finite exact certificates and numerical cross-checks; universal proofs are in the manuscript.',
                environment=dict(python=platform.python_version(),sympy=s.__version__,numpy=np.__version__,scipy=scipy.__version__),
                counts=dict(total=len(rows),passed=sum(r['passed'] for r in rows),
                            failed=sum(not r['passed'] for r in rows),classes=counts),rows=rows)


# ---------------- v1.3 independent amplitude and power tests ----------------
def amplitude_coefficient(H, a, b, degree):
    powers = [s.eye(H.rows)]
    for _ in range(degree):
        powers.append((powers[-1]*H).applyfunc(s.expand))
    return s.simplify(s.expand(sum(
        (-I)**k * I**(degree-k) * powers[k][b,a]
        * s.conjugate(powers[degree-k][b,a])
        / (s.factorial(k)*s.factorial(degree-k))
        for k in range(degree+1))))


def amplitude_contrast(K, V, a, b, degree):
    return s.simplify(amplitude_coefficient(K+V,a,b,degree)
                      - amplitude_coefficient(K-V,a,b,degree))


def phase_alignment(G):
    """Finite exact certificate; returns earliest nonaligned power pair if any."""
    m=G.rows; powers=[s.eye(m)]
    for _ in range(1,m):
        powers.append((powers[-1]*G).applyfunc(s.expand))
    witnesses=[]
    for a in range(m):
        for b in range(m):
            r=next((k for k in range(m) if s.simplify(powers[k][b,a])!=0),None)
            if r is None: continue
            for q in range(r+1,m):
                wedge=s.simplify(s.im(s.conjugate(powers[r][b,a])*powers[q][b,a]))
                if wedge!=0:
                    witnesses.append((a,b,r,q,wedge)); break
    return not witnesses, witnesses


def block_network(B):
    m,n=B.shape; K=s.zeros(m+n)
    K[:m,m:]=B;K[m:,:m]=B.conjugate().T
    return K, s.diag(*([1]*m+[-1]*n))


def run_additions(inject=None):
    rows=[]
    def row(rid,cls,claim,passed,**data):
        rows.append(dict(id=rid,cls=cls,claim=claim,passed=bool(passed),data=data))
        print(rid,cls,'PASS' if passed else 'FAIL',claim,flush=True)

    K=cycle(4,I);V=diag_site(4,0)
    c13=amplitude_contrast(K,V,1,3,5)
    c12=amplitude_contrast(K,V,1,2,5)
    row('C20','C','Corrected Cor8.4: opposite neighbours 1->3 have -1/3; adjacent 1->2 have 1/6',
        c13==-s.Rational(1,3) and c12==s.Rational(1,6),
        opposite=str(c13),adjacent=str(c12),old_wrong_coefficient='-1/6')

    records=[];ok=True
    for n in range(3,11):
        vs=s.symbols('v:'+str(n));A=[]
        for a in range(n):
            for k in range(1,n):
                arc1=[(a+j)%n for j in range(k+1)]
                arc2=[(a-j)%n for j in range(n-k+1)]
                f=s.expand((k+1)*sum(vs[i] for i in arc2)
                           -(n-k+1)*sum(vs[i] for i in arc1))
                A.append([f.coeff(v) for v in vs])
        A=s.Matrix(A);rank=A.rank();dim=2 if n==4 else 1
        ok &= rank==n-dim and iszero(A*s.ones(n,1))
        if n==4: ok &= iszero(A*s.Matrix([1,-1,1,-1]))
        records.append(dict(length=n,rank=rank,nullity=n-rank))
    row('C21','C','Bare-cycle leading-coefficient kernels C3..C10: C4 dimension 2, all others dimension 1',ok,cases=records)

    ok=True;records=[]
    for n in range(3,9):
        weights=[s.Integer(j%3+1)*(-1 if j%2 else 1) for j in range(n)]
        weights[-1]*=(1+I if n%2 else I)
        K=graph(n,[(a,(a+1)%n,weights[a]) for a in range(n)])
        V=s.diag(*[s.Integer((j*j+2*j)%5) for j in range(n)])
        # Independent amplitude coefficient compared with two arc paths.
        for a in (0,1):
            for k in (1,2):
                b=(a+k)%n
                arc1=[(a+j)%n for j in range(k+1)]
                arc2=[(a-j)%n for j in range(n-k+1)]
                direct=amplitude_contrast(K,V,a,b,n+1)
                pred=cycle_leading(K,V,arc1,arc2)
                ok &= s.simplify(direct-pred)==0
                records.append(dict(n=n,a=a,b=b,coefficient=str(direct)))
    row('C22','C','Weighted complex cycle coefficients: independent amplitude powers match arc law C3..C8',ok,cases=records)

    ok=True;records=[]
    for n in (4,6,8):
        K=cycle(n,I);V=s.diag(*[(-1)**j for j in range(n)])
        c=amplitude_contrast(K,V,0,2,n+1)
        should_blind=n==4
        if inject=='cycle_exception': should_blind=True
        ok &= (c==0)==should_blind
        records.append(dict(n=n,coefficient=str(c)))
    row('C23','C','Alternating potentials are blind on C4 but visible at order length+1 on unbalanced C6,C8',ok,cases=records)

    chi=s.symbols('chi',real=True)
    B=s.Matrix([[1,1,0],[0,1,1],[I,0,1]])
    K,Sigma=block_network(B);G=B*B.conjugate().T
    aligned,wits=phase_alignment(G);a,b,r,q,w=wits[0]
    degree=2*(r+q)+1
    pred=s.simplify(8*chi*(r-q)*(-1)**(r+q)*w/(s.factorial(2*r+1)*s.factorial(2*q+1)))
    if inject=='wronskian_sign': pred=-pred
    actual=amplitude_contrast(K,chi*Sigma,a,b,degree)
    low=[amplitude_contrast(K,chi*Sigma,a,b,d) for d in range(degree)]
    row('C24','C','Sharp Gram-power response: first nonaligned powers r=1,s=2 give exact chi-linear t^7 coefficient',
        not aligned and r==1 and q==2 and all(z==0 for z in low) and s.simplify(pred-actual)==0,
        pair=[a,b],power_pair=[r,q],wedge=str(w),degree=degree,coefficient=str(actual),prediction=str(pred))

    # A second example has a zero G entry: first nonzero r=2, next nonaligned s=3.
    B=s.zeros(4,8)
    for j in range(4):
        B[j,j]=1;B[(j+1)%4,j]=(I if j==3 else 1)
        B[j,4+j]=j+1
    K,Sigma=block_network(B);G=(B*B.conjugate().T).applyfunc(s.expand)
    pw=[s.eye(4),G,G**2,G**3];a,b=0,2;r,q=2,3
    w=s.simplify(s.im(s.conjugate(pw[r][b,a])*pw[q][b,a]));degree=11
    pred=s.simplify(8*(r-q)*(-1)**(r+q)*w/(s.factorial(2*r+1)*s.factorial(2*q+1)))
    jets=contrast_series(K,Sigma,a,degree)
    actual=s.simplify(jets[degree][b,b])
    row('C25','C','Sharp Gram-power response with absent direct Gram edge: r=2,s=3, first order t^11',
        G[b,a]==0 and pw[r][b,a]!=0 and w!=0
        and all(s.simplify(jets[d][b,b])==0 for d in range(degree)) and actual==pred,
        Gram=[[str(z) for z in G.row(j)] for j in range(4)],wedge=str(w),coefficient=str(actual),prediction=str(pred))

    # Zero mass is always blind although Gram projectors need not align.
    B=s.Matrix([[1,1,0],[0,1,1],[I,0,1]]);K,Sigma=block_network(B)
    aligned,_=phase_alignment(B*B.conjugate().T)
    zero_blind=all(pop_diagonal_zero(d) for d in contrast_series(K,s.zeros(6),0,7))
    if inject=='zero_mass': zero_blind=zero_blind and aligned
    row('W05','W','chi=0 boundary refutes unqualified phase-alignment necessity',zero_blind and not aligned,
        zero_mass_blind=zero_blind,Gram_aligned=aligned)

    A=s.Matrix([[0,1,1,1],[-1,0,-1,1],[-1,1,0,-1],[-1,-1,1,0]])
    B=2*s.eye(4)+I*A;K,Sigma=block_network(B);G=B*B.conjugate().T
    aligned,wits=phase_alignment(G)
    triangle=s.simplify(G[0,1]*G[1,2]*G[2,0])
    poly=iszero(G*G-14*G+s.eye(4))
    row('C26','C','Nongauge-real Gram matrices can be phase-aligned: exact quadratic minimal polynomial',
        aligned and poly and s.im(triangle)!=0,triangle=str(triangle),minimal_polynomial='x^2-14x+1',aligned=aligned)

    B=s.eye(3);K,Sigma=block_network(B)
    edges=sum(K[b,a]!=0 for a in range(6) for b in range(a+1,6))
    row('W06','W','A unitary coupling block need not have K_n,n support: B=I3 has three edges',
        edges==3 and phase_alignment(B*B.conjugate().T)[0],support_edges=edges,complete_support_edges=9)

    # Deliberate resonant positive frequencies 1,2,3 at chi=1, including a singular Gram matrix.
    omega=np.exp(2j*np.pi/3);F=np.array([[omega**(a*b)/np.sqrt(3) for b in range(3)] for a in range(3)])
    B=F@np.diag(np.sqrt([0.,3.,8.]))
    K=np.zeros((6,6),complex);K[:3,3:]=B;K[3:,:3]=B.conj().T
    Sg=np.diag([1.,1.,1.,-1.,-1.,-1.]);G=B@B.conj().T
    nonaligned=float(np.max(abs(np.imag(np.conj(G)*(G@G)))))
    observations=[];ok=nonaligned>1e-3
    for mass in (-2.,-1.,-.2,.2,1.,2.):
        maximum=0.;error=0.
        ev,Q=np.linalg.eigh(G);ev=np.maximum(ev,0);nu=np.sqrt(ev+mass*mass)
        for t in (.11,.37,.71,1.3):
            C=Q@np.diag(np.cos(nu*t))@Q.conj().T
            S=Q@np.diag(np.sin(nu*t)/nu)@Q.conj().T
            direct=population_contrast(K,mass*Sg,t)[:3,:3]
            formula=4*mass*np.imag(np.conj(C)*S)
            maximum=max(maximum,float(np.max(abs(direct))))
            error=max(error,float(np.max(abs(direct-formula))))
        ok &= maximum>1e-5 and error<1e-11
        observations.append(dict(mass=mass,maximum_contrast=maximum,formula_error=error))
    row('V08','V','Resonant and singular Gram test: nonaligned projectors remain visible at every sampled nonzero mass',
        ok,chi1_frequencies=[1,2,3],wedge=nonaligned,cases=observations,tolerance=1e-11)

    rng=np.random.default_rng(75260928);ok=True;records=[]
    for shape in [(2,4),(3,3),(3,5),(4,4)]:
        B=rng.normal(size=shape)+I*rng.normal(size=shape)
        B=np.array(B,complex);m,n=shape
        K=np.zeros((m+n,m+n),complex);K[:m,m:]=B;K[m:,:m]=B.conj().T
        Sg=np.diag([1.]*m+[-1.]*n)
        for part,G in [('A',B@B.conj().T),('B',B.conj().T@B)]:
            mass=.8;t=.9;ev,Q=np.linalg.eigh(G);nu=np.sqrt(np.maximum(ev,0)+mass*mass)
            C=Q@np.diag(np.cos(nu*t))@Q.conj().T
            S=Q@np.diag(np.sin(nu*t)/nu)@Q.conj().T
            # Central finite difference is solely a numerical check of C=S'.
            eps=1e-6
            def smat(tt):return Q@np.diag(np.sin(nu*tt)/nu)@Q.conj().T
            err=float(np.max(abs((smat(t+eps)-smat(t-eps))/(2*eps)-C)))
            ok &= err<1e-8
            records.append(dict(shape=list(shape),part=part,derivative_error=err))
    row('V09','V','Wronskian reduction C=S derivative checked on rectangular complex blocks',ok,cases=records,tolerance=1e-8)

    # Direct expm checks the phase-aligned, nongauge-real example, independent of the exact power test.
    A=np.array([[0,1,1,1],[-1,0,-1,1],[-1,1,0,-1],[-1,-1,1,0]],float)
    B=2*np.eye(4)+1j*A;K=np.block([[np.zeros((4,4)),B],[B.conj().T,np.zeros((4,4))]])
    Sg=np.diag([1.]*4+[-1.]*4);maximum=0.
    for mass in (-2.,-.7,.1,1.4):
        for t in (.01,.2,.7,1.7):maximum=max(maximum,float(abs(population_contrast(K,mass*Sg,t)).max()))
    row('V10','V','Aligned nongauge-real Gram example: direct all-population blindness across nonzero masses',maximum<1e-11,max_residual=maximum,tolerance=1e-11)
    return rows


"""Targeted checks written for the v1.3 audit; no inherited helper imports.
Exact algebra/finite matrices only, not proof-assistant or grade certificates.
"""
import sympy as sp

def audit_checks(inject=None):
    rows = []
    def put(rid, cls, claim, ok, **evidence):
        rows.append(dict(id=rid, cls=cls, claim=claim, passed=bool(ok), **evidence))
    def z(M):
        return all(sp.simplify(x)==0 for x in M)
    def coefficients(H, order):
        # Direct matrix-amplitude convolution, no density recursion or Gram helper.
        n=H.rows
        aa=[sp.eye(n)]
        for k in range(1,order+1):
            aa.append((-sp.I*H*aa[-1]/k).applyfunc(sp.expand))
        return [sp.Matrix(n,n,lambda b,a:sp.expand(sum(aa[j][b,a]*sp.conjugate(aa[d-j][b,a]) for j in range(d+1)))) for d in range(order+1)]

    # A symbolic identity for arbitrary formal leading indices; this checks the
    # coefficient sign in the written analytic proof, not the entire theorem.
    r,ss=sp.symbols('r s',integer=True,positive=True)
    t=sp.symbols('t',positive=True)
    ar,ai,br,bi=sp.symbols('ar ai br bi',real=True)
    a=ar+sp.I*ai; b=br+sp.I*bi
    f=a*t**(2*r+1)+b*t**(2*ss+1)
    w=sp.expand(sp.im(sp.conjugate(sp.diff(f,t))*f))
    expected=2*(r-ss)*(ar*bi-ai*br)*t**(2*(r+ss)+1)
    if inject=='audit_pair_sign':expected=-expected
    put('C27','C','Formal two-leading-term Wronskian coefficient has sign 2(r-s)',sp.simplify(w-expected)==0,identity=str(sp.factor(w)))

    m,alpha,beta=sp.symbols('m alpha beta',real=True)
    arc=3*(m*alpha+(m-1)*beta)-(2*m-1)*(2*alpha+beta)
    put('C28','C','Even-cycle remaining constraint is exactly (m-2)(beta-alpha)',sp.expand(arc-(m-2)*(beta-alpha))==0,residual=str(sp.factor(arc)))

    # Both orientations of a rectangular block: a 2x2 Gram is automatically
    # aligned, whereas the 3x3 Gram below is not. All entries are checked.
    B0=sp.Matrix([[1,1,1],[1,sp.I,2]])
    cases=[];ok=True
    for B in (B0,B0.conjugate().T):
        na,nb=B.shape
        K=sp.BlockMatrix([[sp.zeros(na),B],[B.conjugate().T,sp.zeros(nb)]]).as_explicit()
        sig=sp.diag(*([1]*na+[-1]*nb));chi=sp.Rational(2);offset=sp.Rational(3)
        pp=coefficients(K+chi*sig+offset*sp.eye(na+nb),7)
        mm=coefficients(K-chi*sig-offset*sp.eye(na+nb),7)
        contrast=[x-y for x,y in zip(pp,mm)]
        target=sp.zeros(na+nb)
        wedges=[]
        for start,G,sign in ((0,B*B.conjugate().T,1),(na,B.conjugate().T*B,-1)):
            for a0 in range(G.rows):
                for b0 in range(G.rows):
                    wedge=sp.simplify(sp.im(sp.conjugate(G[b0,a0])*(G**2)[b0,a0]))
                    target[start+b0,start+a0]=sign*chi*wedge/90
                    if wedge:wedges.append(str(wedge))
        ok=ok and all(z(c) for c in contrast[:7]) and z(contrast[7]-target) and bool(wedges)
        cases.append(dict(shape=list(B.shape),nonzero_wedges=wedges,coefficient_matrix=str(target)))
    put('C29','C','Rectangular blocks and their adjoints: exact A/B seventh-order signs, lower-order zeros and scalar-shift invariance',ok,cases=cases)

    # Exact resonant-frequency algebra: sum 1+2 equals 3, difference 3-1 equals 2.
    # These coefficients test the Wronskian sublemma, not an invented quantum Gram.
    coeff=[1,sp.I,-1-sp.I];nu=[1,2,3]
    vand=sp.Matrix([[(-x*x)**k for x in nu] for k in range(3)])
    moments=sp.Matrix([sum(coeff[j]*(-nu[j]**2)**k for j in range(3)) for k in range(3)])
    f=sum(coeff[j]*sp.sin(nu[j]*t)/nu[j] for j in range(3))
    w=sp.im(sp.conjugate(sp.diff(f,t))*f).expand(complex=True)
    leading=sp.simplify(sp.diff(w,t,7).subs(t,0)/sp.factorial(7))
    put('C30','C','Exact resonant sine family remains independent and its nonalignment gives a nonzero Wronskian',vand.det()!=0 and vand.inv()*moments==sp.Matrix(coeff) and leading!=0,determinant=str(vand.det()),wronskian_t7=str(leading),scope='Exact analytic sublemma instance; no Gram realization claimed')

    # This is the already-issued M74 matrix, not a new counterexample.
    A=sp.Matrix([[0,1,1,1],[-1,0,-1,1],[-1,1,0,-1],[-1,-1,1,0]])
    c,d=sp.symbols('c d',real=True)
    U=c*sp.eye(4)+d*A
    symmetric=all(sp.expand(U[j,k]**2-U[k,j]**2)==0 for j in range(4) for k in range(4))
    obstruction=sp.prod(A[j,k]/A[k,j] for j,k in [(0,1),(1,2),(2,0)])
    H=sp.I*A
    put('W07','W','Imported M74 zero-diagonal K4: symmetric populations and inconsistent diagonal transpose/adjoint gauge on a triangle',z(A*A+3*sp.eye(4)) and symmetric and obstruction==-1 and all(H[j,j]==0 for j in range(4)),triangle_ratio=str(obstruction),H_triangle=str(H[0,1]*H[1,2]*H[2,0]),source='M74 v1.1.1 section 7.1; not a novelty claim')

    # Distinguish a single coefficient kernel from the full blind plane, the
    # exact ambiguity in inherited row C09's human-readable label.
    vs=sp.symbols('v0:4',real=True)
    K=sp.zeros(4)
    for j in range(4):
        value=sp.I if j==0 else sp.Integer(1)
        K[(j+1)%4,j]=value;K[j,(j+1)%4]=sp.conjugate(value)
    V=sp.diag(*vs)
    p=coefficients(K+V,5)[5][1,0];q=coefficients(K-V,5)[5][1,0]
    func=sp.factor(p-q)
    one=sp.Matrix([[sp.diff(func,v) for v in vs]])
    alt={vs[j]:(1 if j%2==0 else -1) for j in range(4)}
    put('C31','C','C09 certifies one arc functional and scalar containment, not a scalar-only kernel',one.rank()==1 and sp.simplify(func.subs(alt))==0 and func.subs(dict.fromkeys(vs,1))==0,functional=str(func),single_functional_nullity=4-one.rank(),full_blind_plane_dimension=2)
    return rows


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--out',type=Path,default=Path(__file__).with_suffix('.json'))
    parser.add_argument('--profile',choices=['full','additions','audit'],default='full')
    parser.add_argument('--inject',choices=['rooted_cycle','cycle_phase','gauge_sign','trotter_step','moment_constant','sublattice_formula','mirror_sign','cycle_exception','wronskian_sign','zero_mass','audit_pair_sign'])
    args=parser.parse_args()
    if args.profile=='full':result=run_legacy(args.inject)
    else:result=dict(paper='ZS-M75',version=VERSION,random_seed=SEED,rows=[],environment=dict(python=platform.python_version(),sympy=s.__version__,numpy=np.__version__,scipy=scipy.__version__))
    if args.profile in ('full','additions'):result['rows']+=run_additions(args.inject)
    if args.profile in ('full','audit'):result['rows']+=audit_checks(args.inject)
    rows=result['rows'];classes={c:sum(r['cls']==c for r in rows) for c in ['P','C','V','W','R','G','X','D','T']}
    result['counts']=dict(total=len(rows),passed=sum(r['passed'] for r in rows),failed=sum(not r['passed'] for r in rows),classes=classes)
    result.update(profile=args.profile,injected_fault=args.inject,extension_seed=75260928,
        scope='Finite exact certificates and numerical checks only; universal analytic proofs, novelty, research grade and physical reality are not certified by row counts.')
    args.out.parent.mkdir(parents=True,exist_ok=True)
    args.out.write_text(json.dumps(result,ensure_ascii=False,indent=2,sort_keys=True)+'\n',encoding='utf-8')
    print(json.dumps(result['counts'],sort_keys=True))
    return 1 if result['counts']['failed'] else 0


if __name__=='__main__':sys.exit(main())
