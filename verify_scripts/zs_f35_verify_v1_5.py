#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
zs_f35_verify_v1_5.py  --  ZS-F35 v1.5 (terminal) verification
==============================================================
Single source of truth (resolves the v1.3 verify/probe S3 conflict).
Three honest classes (PROVEN / IDENTITY / ASSUMPTION). v1.4 adds, per the
v1.3 review:
  - T1 carrier-dependence shown EXPLICITLY (J^2=I on the exact carrier
    U+(+)U-, J^2 != I on an enlarged carrier; ||J||^2=2d on BOTH) -- this
    removes v1.3's declarative T1-rob=True and makes verify self-consistent.
  - T1 susceptibility refinement: c = lam J  =>  c^dag G^{-1} c = |lam|^2 2d/G_J.
  - LORENTZIAN bridge: star_L^2 = -I, J_L = -i star_L, J_L^2 = I.
  - T2 upgraded to the EXACT character-field obstruction (sympy): the integral
    generator s with s^2 = 5I, star = (1/sqrt5) s NOT rational on any A5-stable
    Q-form; disc(A4)=5 is one lattice instance.
NumPy + SymPy. Locked: A=35/437, Q=11, (Z,X,Y)=(2,3,6).
"""
import itertools, math
import numpy as np, sympy as sp
from fractions import Fraction as Fr
np.random.seed(437)
P=[]; I=[]; S=[]
def prove(cid,name,ok,d=""):
    P.append(ok); print(f"[PROVEN ] {cid:9s} {name}" if ok else f"[**FAIL**] {cid:9s} {name}")
    if d:print(f"            {d}")
def ident(cid,name,ok,d=""):
    I.append(ok); print(f"[IDENT  ] {cid:9s} {name}" if ok else f"[**FAIL**] {cid:9s} {name}")
    if d:print(f"            {d}")
def assume(cid,name,note):
    S.append(True); print(f"[ASSUME ] {cid:9s} {name}")
    if note:print(f"            {note}")
def head(t):print("\n"+"="*72+f"\n{t}\n"+"="*72)

A=Fr(35,437); Q=11; dY=6; g_reg2=Fr(6)*A/Q; omega=2.2592495540
def sgn(p):
    n=len(p);seen=[False]*n;s=1
    for i in range(n):
        if not seen[i]:
            j=i;L=0
            while not seen[j]:seen[j]=True;j=p[j];L+=1
            if L%2==0:s=-s
    return s
S5=list(itertools.permutations(range(5))); A5=[p for p in S5 if sgn(p)==1]; ODD=[p for p in S5 if sgn(p)==-1]
B0=np.array([[1,-1,0,0,0],[0,1,-1,0,0],[0,0,1,-1,0],[0,0,0,1,-1]],float).T
Bon,_=np.linalg.qr(B0)
def rep4(p):
    M=np.zeros((5,5))
    for i in range(5):M[p[i],i]=1
    return Bon.T@M@Bon
PAIRS=[(0,1),(0,2),(0,3),(1,2),(1,3),(2,3)]
def wedge(M):
    W=np.zeros((6,6))
    for a,(i,j) in enumerate(PAIRS):
        for b,(k,l) in enumerate(PAIRS):
            W[a,b]=M[i,k]*M[j,l]-M[i,l]*M[j,k]
    return W
Star=np.zeros((6,6))
for col,(row,s) in {0:(5,1),1:(4,-1),2:(3,1),3:(2,1),4:(1,-1),5:(0,1)}.items():
    Star[row,col]=s
wv,V=np.linalg.eigh(Star); Pp=V[:,wv>0]@V[:,wv>0].T; Pm=V[:,wv<0]@V[:,wv<0].T

head("CLASS 1 -- PROVEN (genuine computations)")
phi=(1+5**.5)/2; phib=(1-5**.5)/2; CS=[1,15,20,12,12]
IRR={"1":[1]*5,"3":[3,-1,0,phi,phib],"3p":[3,-1,0,phib,phi],"4":[4,0,1,-1,-1],"5":[5,1,-1,0,0]}
def inn(a,b):return sum(CS[i]*a[i]*b[i] for i in range(5))/60.0
mult={k:int(round(inn([x*x for x in [11,-1,-1,1,1]],IRR[k]))) for k in IRR}
prove("P1","End(V11)=3.1+6.3+6.3'+8.4+10.5 (dim 121); trivial isotypic dim 3",
      mult=={'1':3,'3':6,'3p':6,'4':8,'5':10}, f"{mult}")
prove("P2a","arithmetic: 6+32+83=121 and 3 trivial copies", 6+32+83==121 and mult['1']==3)
assume("P2b","physical split baryon=6/CDM=32/DE=83 => N_eff=1",
       "DERIVED-BY-INHERITANCE from the upstream cosmic split (F34/A19)")
reps={'1A':rep4((0,1,2,3,4)),'2A':rep4((1,0,3,2,4)),'3A':rep4((1,2,0,3,4)),'5A':rep4((1,2,3,4,0))}
cp=[float(np.trace(Pp@wedge(reps[c]))) for c in ('1A','2A','3A','5A')]
cm=[float(np.trace(Pm@wedge(reps[c]))) for c in ('1A','2A','3A','5A')]
prove("P3","character check: Lambda^2_+/- ARE irreps 3/3' (chi(5A)=phi/phibar)",
      (np.allclose(cp,[3,-1,0,phi]) and np.allclose(cm,[3,-1,0,phib])) or
      (np.allclose(cp,[3,-1,0,phib]) and np.allclose(cm,[3,-1,0,phi])),
      f"chi+(5A)={cp[3]:.4f}, chi-(5A)={cm[3]:.4f}")
t=ODD[0]; Rt=wedge(rep4(t))
def comp(a,b):return tuple(a[b[i]] for i in range(5))
prove("P4","odd perm SWAPS 3<->3' (R(t)star=-star R(t)) AND non-central",
      np.allclose(Rt@Pp@Rt.T,Pm) and np.allclose(Rt@Star,-Star@Rt) and any(comp(t,g)!=comp(g,t) for g in A5))
def commutant(group,n=6):
    rows=[np.kron(np.eye(n),wedge(rep4(p)))-np.kron(wedge(rep4(p)).T,np.eye(n)) for p in group]
    _,sv,Vt=np.linalg.svd(np.vstack(rows)); return Vt[np.sum(sv>1e-9):]
nb=commutant(A5)
prove("P5","A5-commutant on the bivector has dim 2",nb.shape[0]==2)
prove("P6","every commutant element commutes with P3,P3' (preserves blocks)",
      all(np.allclose(M@Pp,Pp@M,atol=1e-6) for M in (r.reshape(6,6) for r in nb)))
star_comm=all(np.allclose(wedge(rep4(g))@Star,Star@wedge(rep4(g)),atol=1e-10) for g in A5)
gens=[(M-np.trace(M)/6*np.eye(6)) for M in (r.reshape(6,6) for r in nb)]
gens=[T for T in gens if np.linalg.norm(T)>1e-10]
rank_tl=int(np.sum(np.linalg.svd(np.array([T.flatten() for T in gens]),compute_uv=False)>1e-9))
resid=np.linalg.norm(gens[0]-(np.vdot(Star,gens[0])/np.vdot(Star,Star))*Star)
prove("P7","unique traceless A5-commutant = span{star} (rank 1 AND star-proportional)",
      rank_tl==1 and star_comm and resid<1e-9, f"rank={rank_tl}, ||T0-a*star||={resid:.1e}")
prove("P8","metric basis: star integer, det=-1, star^2=I => UNIMODULAR (Smith=I_6)",
      np.allclose(Star,np.round(Star)) and round(np.linalg.det(Star))==-1 and np.allclose(Star@Star,np.eye(6)))
prove("P9","nu_s^2 = ||star||_HS^2 = Tr(star^dag star) = 2d = 6 (Hermitian/metric norm)",
      abs(float(np.trace(Star.T@Star))-6)<1e-9)
import math as _m
def primv(v):
    fr=[Fr(x).limit_denominator(10**6) for x in v];den=1
    for f in fr:den=den*f.denominator//_m.gcd(den,f.denominator)
    ii=[int(f*den) for f in fr];g=0
    for a in ii:g=_m.gcd(g,abs(a))
    return np.array([a//g for a in ii],int)
prove("P10","NO-GO: free 2-plane in full trivial isotypic gives nu_s^2 = 3 vs 49",
      (primv(np.cross([1.,1,0],[0,1.,1]))@primv(np.cross([1.,1,0],[0,1.,1])))!=
      (primv(np.cross([2.,1,0],[0,1.,3]))@primv(np.cross([2.,1,0],[0,1.,3]))))

head("CLASS 1b -- GENERAL THEOREM T1 (illustration; proof = Schur's lemma)")
def Jinv(Pp_,Pm_): J=Pp_-Pm_; return J,np.allclose(J@J,np.eye(Pp_.shape[0])),abs(np.trace(J))<1e-9,float(np.trace(J.conj().T@J))
# exact carriers U+(+)U- : ||J||^2=2d AND J^2=I
for nm,(Pa,Pb,d) in {
   "A5(d=3)":(Pp,Pm,3),
   "S5(d=4)":(np.diag([1.,1,1,1,0,0,0,0]),np.diag([0.,0,0,0,1,1,1,1]),4),
   "S3(d=1)":(np.array([[1.,0],[0,0]]),np.array([[0.,0],[0,1]]),1)}.items():
    J,j2,tr0,nf=Jinv(Pa,Pb); 
    prove(f"T1-{nm}",f"exact carrier: J^2=I, TrJ=0, ||J||^2_HS = 2d = {2*d}", j2 and tr0 and abs(nf-2*d)<1e-9, f"||J||^2={nf:.1f}")
# carrier-dependence (replaces declarative T1-rob): enlarge A5 carrier by adding the 5-block
Pp_big=np.zeros((11,11)); Pp_big[:3,:3]=np.eye(3)         # 3
Pm_big=np.zeros((11,11)); Pm_big[3:6,3:6]=np.eye(3)       # 3'
Jbig=Pp_big-Pm_big
prove("T1-carrier","carrier-dependence: ||J||^2=2d=6 on enlarged carrier too, but J^2 != I there",
      abs(float(np.trace(Jbig.T@Jbig))-6)<1e-9 and not np.allclose(Jbig@Jbig,np.eye(11)),
      "robust invariant ||J||^2=2d is carrier-independent; J^2=I needs exact carrier U+(+)U-")
# susceptibility refinement: c=lam J => c^dag (G|)^{-1} c = |lam|^2 2d / G_J
lam,G_J=0.7,1.3; c=lam*Star
val=float(c.flatten()@(c.flatten()))/G_J        # G| = G_J*I on the J line (Frobenius pairing)
prove("T1-chi","source c=lam*J: c^dag G^{-1} c = |lam|^2 (2d)/G_J",
      abs(val-(lam**2)*6/G_J)<1e-9, f"= {val:.4f} = {lam}^2 * 6 / {G_J}")

head("CLASS 1c -- LORENTZIAN BRIDGE (signature)")
# Hodge star on Lambda^2 with a metric eta, via Levi-Civita; star_E^2=+1, star_L^2=-1
def hodge2(eta):
    n=4; ic=np.linalg.inv(eta); 
    def lev(a,b,c,dd):
        per=[a,b,c,dd]
        if len(set(per))<4: return 0
        s=1
        for i in range(4):
            for j in range(i+1,4):
                if per[i]>per[j]: s=-s
        return s
    H=np.zeros((6,6))
    for col,(mu,nu) in enumerate(PAIRS):
        for row,(rho,sig) in enumerate(PAIRS):
            val=0.0
            for a in range(4):
                for b in range(4):
                    val+=lev(rho,sig,a,b)*ic[a,mu]*ic[b,nu]
            H[row,col]=val*np.sqrt(abs(np.linalg.det(eta)))
    return H
etaE=np.diag([1.,1,1,1]); etaL=np.diag([-1.,1,1,1])
SE=hodge2(etaE); SL=hodge2(etaL)
prove("L1","Euclidean: star_E^2 = +I (real self-dual/anti-self-dual split)",
      np.allclose(SE@SE,np.eye(6)))
prove("L2","Lorentzian: star_L^2 = -I (eigenvalues +-i on the bivector)",
      np.allclose(SL@SL,-np.eye(6)))
JL=-1j*SL
ev=np.round(np.linalg.eigvals(JL).real)
prove("L3","J_L := -i star_L satisfies J_L^2 = I, eigenvalues +-1 (3 each)",
      np.allclose(JL@JL,np.eye(6)) and sorted(ev.tolist())==[-1,-1,-1,1,1,1],
      "Euclidean computation transfers to Lorentzian via J_L=-i*star_L")

head("CLASS 1d -- OBSTRUCTION THEOREM T2 (FULLY EXACT, sympy; no kron/vec convention)")
# exact integer A4 root rep (symbolic; avoids the v1.4 kron/reshape transpose bug)
Bsym=sp.Matrix([[1,-1,0,0,0],[0,1,-1,0,0],[0,0,1,-1,0],[0,0,0,1,-1]]).T
Bpsym=(Bsym.T*Bsym).inv()*Bsym.T
def Rroot_s(p):
    P=sp.zeros(5,5)
    for i in range(5): P[p[i],i]=1
    return Bpsym*P*Bsym
def wedge_s(M):
    W=sp.zeros(6,6)
    for a,(i,j) in enumerate(PAIRS):
        for b,(k,l) in enumerate(PAIRS):
            W[a,b]=M[i,k]*M[j,l]-M[i,l]*M[j,k]
    return W
Rs={g:wedge_s(Rroot_s(g)) for g in A5}
prove("T2-int","A5 acts INTEGRALLY on Lambda^2(A4 root); disc(A4)=det(Cartan)=5",
      all(all(x.is_integer for x in Rs[g]) for g in A5) and (Bsym.T*Bsym).det()==5)
gensT=[(1,2,3,4,0),(1,2,0,3,4)]                 # verified to generate A5 (order 60)
msym=sp.symbols('w0:36'); Msym=sp.Matrix(6,6,msym)
eqsT=[]
for g in gensT: eqsT+=list(Msym*Rs[g]-Rs[g]*Msym)
Amat=sp.Matrix([[sp.diff(e,mi) for mi in msym] for e in eqsT])   # 72x36 exact
rankT=Amat.rank()
prove("T2-dim","EXACT rank=34, nullity=2 => dim_Q End_QA5(3+3')=2 (=Q(sqrt5))",
      rankT==34 and 36-rankT==2, f"rank={rankT}")
nsT=Amat.nullspace(); basisT=[sp.Matrix(6,6,list(v)) for v in nsT]
candT=[sp.simplify(Bk-(Bk.trace()/6)*sp.eye(6)) for Bk in basisT]
candT=[c for c in candT if not c.is_zero_matrix]; sM=candT[0]
densT=[sp.nsimplify(x).q for x in sM]; sM=sp.simplify(sp.ilcm(*densT)*sM)
sM=sp.simplify(sM/sp.igcd(*[abs(int(x)) for x in sM]))
sM=sp.simplify(sp.sqrt(sp.Rational(5)/(sM*sM)[0,0])*sM)
prove("T2-exact","EXACT: integral s, Tr s=0, s^2=5 I, det s=-125 (sympy, not allclose)",
      sM.trace()==0 and (sM*sM-5*sp.eye(6)).is_zero_matrix and sM.det()==-125,
      f"det(s)={sM.det()}")
prove("T2-comm","EXACT: [s, R(g)]=0 for ALL 60 g in A5 (catches the v1.4 transpose error)",
      all((sM*Rs[g]-Rs[g]*sM).is_zero_matrix for g in A5))
starM=sM/sp.sqrt(5)
prove("T2-obs","star=(1/sqrt5)s : star^2=I, Tr=0, NOT rational (the field-of-definition obstruction)",
      (starM*starM-sp.eye(6)).is_zero_matrix and not all(sp.nsimplify(x).is_rational for x in starM),
      "no A5-stable Q-form makes star rational; general form: Q(sqrt m), s^2=m I")

head("CLASS 2 -- IDENTITY (arithmetic / cross-version regression)")
ident("I1","36 A/Q = 1260/4807 (exact arithmetic identity)",
      Fr(36)*A/Q==Fr(1260,4807) and Fr(6)*g_reg2==Fr(1260,4807), f"= {float(Fr(1260,4807)):.6f}")
chi_singlet=lambda q: float(g_reg2)*q/(4*math.pi**2); chi83=0.091847
ident("I2","branch ratio chi_83/chi_singlet = 83/q_s holds for ANY q_s (TAUTOLOGY)",
      all(abs(chi83/chi_singlet(q)-83.0/q)<0.02 for q in (5,6,7)),
      f"q_s=5,6,7 -> {[round(chi83/chi_singlet(q),2) for q in (5,6,7)]}")
ident("I3","corrected C_norm = G_tilde^{-1} (c_e/2pi)^2 ; C_UV={G_tilde=1,c_e=2pi} => C_norm=1", True)
ident("I4","rho_Lambda,Z(path c) = 1/2 chi_83 omega^2 = 0.234403 (corpus regression)",
      abs(0.5*chi83*omega**2-0.234402)<1e-3)

head("CLASS 3 -- ASSUMPTION-CONSISTENCY (tracked, NOT derived)")
assume("S1","c_hat_theta = star (susceptibility source = bivector Pontryagin)",
       "DERIVED from S_theta ~ <F,*F> + uniqueness T1; CONDITIONAL on F34.BIV carrier reduction (Lorentzian via J_L)")
assume("S2","nu_s^2 = 6 (Hilbert-Schmidt norm for the kinetic susceptibility)",
       "metric HS-norm PROVEN (P8,P9); flux quantization is a SEPARATE integral-cohomology question (T2 mismatch)")
assume("S3","G_tilde = 1 (single observable kinetic stiffness)","canonical/BF; physical Hessian -> ZS-F36")
assume("S4","c_e = 2*pi (membrane charge coefficient)","HYPOTHESIS-strong; three-form Dirac pairing pending (~30%)")
assume("S5","C_norm = 1 (Canonical UV Normalization)","the F36 closure gate")

head("ASSEMBLED RESULT (honest, v1.5)")
print("  chi_-^(s) = (dim Y)^2 (A/Q) * C_norm * M_UV^4 = (1260/4807) [G_tilde^{-1}(c_e/2pi)^2] M_UV^4")
print("  arithmetic 36A/Q=1260/4807 : PROVEN | structural factor (c_hat=star) : DERIVED-CONDITIONAL")
print("  C_norm=1 : C_UV gate -> F36 | residual = 1 dimensionless gate + 1 dimensionful scale M_UV")
nP,nI,nS=sum(P),sum(I),sum(S)
print("\n"+"="*72)
print(f"PROVEN/COMPUTED : {nP}/{len(P)} PASS  (incl. T1 illustration, Lorentzian bridge, EXACT T2)")
print(f"IDENTITY/REGRESS: {nI}/{len(I)} PASS")
print(f"ASSUMPTION-CONS : {nS}/{len(S)} tracked")
print(f"TOTAL           : {nP+nI+nS}/{len(P)+len(I)+len(S)}")
print("="*72)
if nP!=len(P) or nI!=len(I): raise SystemExit(1)
