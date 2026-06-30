#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
zs_f35_T2_exact.py -- FULLY EXACT character-field obstruction (ZS-F35 v1.5)
===========================================================================
Everything below is exact (sympy Rational); no floating point, no rounding,
no kron/vec convention (the symbolic commutant avoids the v1.4 transpose bug).

Theorem T2.  For W = 3 (+) 3' (the rational Galois orbit of the two A5
triplets),  End_{QA5}(W) = Q(sqrt5), generated over Q by an INTEGER operator
s with s^2 = 5 I, Tr s = 0, det s = -125, and [s, R(g)] = 0 for all g in A5.
The duality involution star = (1/sqrt5) s requires the irrational coefficient
1/sqrt5, so NO A5-stable Q-form (hence no Z-lattice) makes star rational.
disc(A4) = 5 is one concrete lattice manifestation.
"""
import itertools
import sympy as sp

def sgn(p):
    n=len(p);seen=[False]*n;s=1
    for i in range(n):
        if not seen[i]:
            j=i;L=0
            while not seen[j]:seen[j]=True;j=p[j];L+=1
            if L%2==0:s=-s
    return s
def comp(a,b): return tuple(a[b[i]] for i in range(5))
S5=list(itertools.permutations(range(5))); A5=[p for p in S5 if sgn(p)==1]
gens=[(1,2,3,4,0),(1,2,0,3,4)]            # verified to generate A5 (order 60)

# ---- exact integer A4 root representation, columns alpha_i = e_i - e_{i+1} ----
B=sp.Matrix([[1,-1,0,0,0],[0,1,-1,0,0],[0,0,1,-1,0],[0,0,0,1,-1]]).T   # 5x4
Bp=(B.T*B).inv()*B.T                       # exact left inverse, 4x5
def Rroot(p):
    P=sp.zeros(5,5)
    for i in range(5): P[p[i],i]=1
    return sp.simplify(Bp*P*B)             # 4x4 exact (integer for A5)
PAIRS=[(0,1),(0,2),(0,3),(1,2),(1,3),(2,3)]
def wedge(M):
    W=sp.zeros(6,6)
    for a,(i,j) in enumerate(PAIRS):
        for b,(k,l) in enumerate(PAIRS):
            W[a,b]=M[i,k]*M[j,l]-M[i,l]*M[j,k]
    return W
R={g:wedge(Rroot(g)) for g in A5}
print("integer action on Lambda^2(root)?",
      all(all(x.is_integer for x in R[g]) for g in A5))

# ---- EXACT commutant: symbolic M, impose [M, R(g)] = 0 for the generators ----
m=sp.symbols('m0:36'); M=sp.Matrix(6,6,m)
eqs=[]
for g in gens:
    eqs+=list(M*R[g]-R[g]*M)               # 36 entries per generator
Amat=sp.Matrix([[sp.diff(e,mi) for mi in m] for e in eqs])   # 72 x 36, exact
rank=Amat.rank()
print(f"EXACT rank of commutant constraint = {rank}; nullity = {36-rank} "
      f"(=> dim_Q End_QA5(W) = {36-rank})")
ns=Amat.nullspace()
basis=[sp.Matrix(6,6,list(v)) for v in ns]

# identify the traceless generator s among the nullspace basis
I6=sp.eye(6); cand=[]
for Bk in basis:
    s=sp.simplify(Bk-(Bk.trace()/6)*I6)
    if not s.is_zero_matrix: cand.append(s)
s=cand[0]
# clear denominators to a primitive integer matrix
dens=[sp.nsimplify(x).q for x in s]; L=sp.ilcm(*dens) if dens else 1
sI=sp.simplify(L*s)
g=sp.igcd(*[abs(int(x)) for x in sI]); sI=sp.simplify(sI/g)
# fix sign/scale so s^2 = 5 I
sc=sp.sqrt(sp.Rational(5)/sp.simplify((sI*sI)[0,0]))
s=sp.simplify(sc*sI)

print("\n--- EXACT properties of s ---")
print("Tr s =", sp.simplify(s.trace()), "; s integer?", all(x.is_integer for x in s))
print("s^2 = 5 I ?", sp.simplify(s*s-5*I6).is_zero_matrix)
print("det s =", s.det())
allcomm=all(sp.simplify(s*R[g]-R[g]*s).is_zero_matrix for g in A5)
print("[s, R(g)] = 0 for ALL 60 g in A5 ?", allcomm, " <-- the transpose-catching check")

# ---- the obstruction: star = s/sqrt5 ----
star=s/sp.sqrt(5)
print("\n--- the duality involution star = (1/sqrt5) s ---")
print("star^2 = I ?", sp.simplify(star*star-I6).is_zero_matrix,
      "; Tr star =", sp.simplify(star.trace()))
rat=all(sp.nsimplify(x).is_rational for x in star)
print("star rational?", rat, " (False => no A5-stable Q-form makes star rational)")

print("\nTHEOREM T2 (fully exact): End_{QA5}(3+3') = Q[s]/(s^2-5) = Q(sqrt5).")
print("star = (1/sqrt5) s needs coeff 1/sqrt5 not in Q  =>  obstruction is exact.")
print("General form: for a Galois-conjugate pair with quadratic character field")
print("Q(sqrt m), the duality involution = (1/sqrt m) s with s^2 = m I -- never")
print("rational. A5 is the m=5 instance; disc(A4)=5 is one lattice realization.")
assert sp.simplify(s.trace())==0 and sp.simplify(s*s-5*I6).is_zero_matrix
assert allcomm and (36-rank)==2 and not rat
print("\nALL EXACT ASSERTIONS PASS.")
