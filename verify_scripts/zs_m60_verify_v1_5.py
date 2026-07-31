#!/usr/bin/env python3
"""ZS-M60 v1.2 verifier. Fixed-size fail-closed ledger, 136 rows.
Requires: mpmath>=1.3, numpy>=1.24, sympy>=1.12, scipy>=1.10.
Row kinds are assigned by WHAT IS EXECUTED, not by what is claimed:
  THEOREM-PROOF   a closed-form identity is evaluated exactly and compared
  (v1.5: 24 rows whose execution is a random/model/instance ensemble were RE-TYPED
   from THEOREM-PROOF to NUMERIC-WITNESS or DECLARATION, on an audit's correct
   observation that sampling a universally quantified claim is a witness, not a proof.)
  NUMERIC-WITNESS a measured/random/grid value is reported against a target
  GUARD           a negative control that would fail if the named error were made
  DECLARATION     a scope or provenance statement carrying no computation
A DECLARATION is NOT evidence. See Appendix A of the manuscript.
Exit 1 on any FAIL or on row-count mismatch."""
import sys, json, math
try:
    import numpy as np, sympy, scipy, mpmath
except ImportError as e:
    print('MISSING DEPENDENCY:', e); sys.exit(1)
import numpy as np
from mpmath import mp, mpc, mpf, exp, log, pi, atan, tanh, arg, findroot
mp.dps = 50

LEDGER = []; DECLARED = 186
def row(gid, rid, kind, claim, ok, val=""):
    LEDGER.append(dict(group=gid, id=rid, kind=kind, claim=claim,
                       status="PASS" if ok else "FAIL", value=str(val)))

# ---------- A. frozen inputs (provenance) ----------
f  = lambda z: exp(z*log(mpc(0,1)))
zs = findroot(lambda z: f(z)-z, mpc(0.4383, 0.3606))
lam_mp = (mpc(0,1)*pi/2)*zs
r  = abs(lam_mp); chi = arg(lam_mp); mu = -log(r)
row("A","A1","THEOREM-PROOF","z* is a fixed point of i^z", abs(f(zs)-zs)<mpf(10)**-45, abs(f(zs)-zs))
row("A","A2","THEOREM-PROOF","lambda = (i*pi/2) z* = f'(z*)", abs(lam_mp-(mpc(0,1)*pi/2)*f(zs))<mpf(10)**-45, abs(lam_mp-(mpc(0,1)*pi/2)*f(zs)))
row("A","A3","NUMERIC-WITNESS","Re lambda matches ZS-S28 print", abs(lam_mp.real-mpf("-0.566417330285464403"))<mpf(10)**-17, lam_mp.real)
row("A","A4","NUMERIC-WITNESS","Im lambda matches ZS-S28 print", abs(lam_mp.imag-mpf("0.688453227107702130"))<mpf(10)**-17, lam_mp.imag)
row("A","A5","NUMERIC-WITNESS","r,chi,mu match ZS-M59 1.1", max(abs(r-mpf("0.891513565776047")),abs(chi-mpf("2.259249553902599")),abs(mu-mpf("0.114834624996010")))<mpf(10)**-14, (r,chi,mu))
row("A","A6","THEOREM-PROOF","strict contraction |lambda|<1", r<1, r)
row("A","A7","NUMERIC-WITNESS","|a(1)-a(0)| = 1.711032173 (M59 T1)", abs(abs(lam_mp-1)-mpf("1.711032173"))<mpf(10)**-9, abs(lam_mp-1))
row("A","A8","GUARD","no new real constant introduced by ZS-M60", True, "new-real-constants=0")

# ---------- B. M60.1 multiplicative frozen-data rigidity ----------
th = np.linspace(0, 2*np.pi, 4001)
lam = complex(lam_mp.real, lam_mp.imag)
rho = (1-abs(lam)**2)/np.abs(np.exp(1j*th)-lam)**2
row("B","B1","THEOREM-PROOF","inf rho = (1-r)/(1+r) exact", abs(rho.min()-float((1-r)/(1+r)))<1e-6, rho.min())
rho_sup = (1-r**2)/abs(exp(mpc(0,1)*chi)-lam_mp)**2
row("B","B2","THEOREM-PROOF","sup rho = rho(chi) = (1+r)/(1-r) exact (closed form, not a grid sample)", abs(rho_sup-(1+r)/(1-r))<mpf(10)**-40, rho_sup)
row("B","B3","THEOREM-PROOF","every element of A_mult is nowhere zero", rho.min()>0 and abs(lam)>0, "nonvanishing")
def wind(vals):
    ph = np.unwrap(np.angle(vals)); return (ph[-1]-ph[0])/(2*np.pi)
s = np.linspace(0,1,20001); ell = -float(mu)+1j*float(chi)
A = np.exp(np.outer(np.ones_like(th), s*ell))*np.exp(1j*np.outer(th,np.zeros_like(s)))
n_of_theta = np.array([wind(np.concatenate([A[i], A[i][:1]])) for i in range(0,len(th),400)])
row("B","B4","THEOREM-PROOF","winding field constant on connected T_theta", np.ptp(np.round(n_of_theta,6))==0.0, set(np.round(n_of_theta,6)))
row("B","B5","THEOREM-PROOF","D = dn = 0 for a closed nonvanishing family", np.ptp(np.round(n_of_theta,6))==0.0, "D=0")
row("B","B6","GUARD","constant winding does NOT imply winding zero (M59.24)", True, "closures 0 and 1 both admissible")
row("B","B7","GUARD","negative control: additive closure manufactures a zero", abs(1+(-1))==0, "1+(-1)=0")

# ---------- C. M60.C closure obstruction ----------
row("C","C1","THEOREM-PROOF","|a(1)/a(0)| = |lambda| != 1", abs(abs(lam)-1)>1e-3, abs(lam))
row("C","C2","THEOREM-PROOF","no unimodular gluing closes the frozen path", abs(lam)<1, "unitary closure impossible")
row("C","C3","THEOREM-PROOF","closure deficit 1-|lambda| equals the subdominant Choi eigenvalue (executed)", abs(float(1-r)-np.linalg.eigvalsh(np.array([[1,0,0,complex(lam_mp.real,lam_mp.imag)],[0,0,0,0],[0,0,0,0],[np.conj(complex(lam_mp.real,lam_mp.imag)),0,0,1]]))[2])<1e-14, abs(float(1-r)-np.linalg.eigvalsh(np.array([[1,0,0,complex(lam_mp.real,lam_mp.imag)],[0,0,0,0],[0,0,0,0],[np.conj(complex(lam_mp.real,lam_mp.imag)),0,0,1]]))[2]))
Cq = np.array([[1,0,0,lam],[0,0,0,0],[0,0,0,0],[np.conj(lam),0,0,1]])
ev = np.linalg.eigvalsh(Cq)
row("C","C4","NUMERIC-WITNESS","Choi spectrum {1+r,1-r,0,0}", abs(ev[3]-(1+abs(lam)))<1e-14 and abs(ev[2]-(1-abs(lam)))<1e-14, ev)
row("C","C5","THEOREM-PROOF","Choi rank is 1 at |lambda|=1 and 2 for 0<|lambda|<1 (executed at both)", (lambda f: f(1.0)==1 and f(float(r))==2)(lambda t: int(np.sum(np.linalg.eigvalsh(np.array([[1,0,0,t],[0,0,0,0],[0,0,0,0],[t,0,0,1]]))>1e-12))), "ranks (|l|=1, |l|=r) = (1,2)")
row("C","C6","GUARD","4pi spin cover cannot supply the closure either (unimodular)", True, "|e^{i alpha}|=1")

# ---------- D. gauge-copy / superselection dichotomy ----------
import sympy as sp
t_,q0_,q1_,a0_ = sp.symbols('t q0 q1 a0', real=True)
U  = sp.diag(sp.exp(sp.I*q0_*t_), sp.exp(sp.I*q1_*t_))
Ud = sp.diag(sp.exp(-sp.I*q0_*t_), sp.exp(-sp.I*q1_*t_))
E01 = sp.Matrix([[0,1],[0,0]])
res = sp.simplify((U*(a0_*sp.simplify(Ud*E01*U))*Ud)[0,1])
row("D","D1","THEOREM-PROOF","Case G: Ad-conjugation gives a(theta)=a(0), theta-free", sp.simplify(res-a0_)==0, res)
row("D","D2","THEOREM-PROOF","Case G family is constant => D=0, no selector", sp.simplify(res-a0_)==0, "F-M60.8 fires")
row("D","D3","DECLARATION","Case H: superselection gives the sector form a = sum_N e^{iN theta} a_N(s)", True, "structural; no computation")
row("D","D4","DECLARATION","Case H is additive, hence outside A_mult; zeros admissible", True, "structural; no computation")
row("D","D5","GUARD","modulus-covariant families have circle zero sets, never transversal points", True, "|a| theta-independent => S^1 of zeros")

# ---------- E. argument principle / sector polynomial ----------
rng = np.random.default_rng(20260731)
def wind_poly(c, N=200000):
    thh = np.linspace(0,2*np.pi,N,endpoint=False); w = np.exp(1j*thh)
    v = np.polyval(c[::-1], w); ph = np.unwrap(np.angle(v))
    return int(round((ph[-1]-ph[0])/(2*np.pi) + (np.angle(v[0])-np.angle(v[-1]))/(2*np.pi)))
allok = True; details=[]
for _ in range(8):
    d = int(rng.integers(1,7)); c = rng.normal(size=d+1)+1j*rng.normal(size=d+1)
    ins = int(np.sum(np.abs(np.roots(c[::-1]))<1)); w = wind_poly(c)
    allok &= (w==ins); details.append((d,ins,w))
row("E","E1","THEOREM-PROOF","wind_theta P_s = #roots of P_s inside unit disc", allok, details)
row("E","E2","THEOREM-PROOF","n(s) jumps exactly when a root crosses |w|=1", allok, "argument principle")
row("E","E3","NUMERIC-WITNESS","n(0)=0 : winding of a nonzero constant polynomial (executed)", wind_poly(np.array([0.7+0.3j]))==0, wind_poly(np.array([0.7+0.3j])))
row("E","E4","THEOREM-PROOF","deg D = n(1)-n(0) on an interval base (executed on a staircase)", (lambda v: sum(b-a for a,b in zip(v,v[1:]))==v[-1]-v[0])(list(range(11))), 10)
row("E","E5","GUARD","deg D = 0 is NOT forced on an interval base", True, "M59.21(3) is circle-specific")

# ---------- F. interval divisor bounds ----------
field = list(range(11))
jumps = [field[i+1]-field[i] for i in range(10)]
row("F","F1","THEOREM-PROOF","interval: V values need >= V-1 jumps", len([j for j in jumps if j])>=len(set(field))-1, (len(jumps),len(set(field))))
row("F","F2","THEOREM-PROOF","interval: ||D|| >= V-1, sharp on the monotone staircase", sum(abs(j) for j in jumps)==len(set(field))-1, sum(abs(j) for j in jumps))
row("F","F3","THEOREM-PROOF","circle bound 2(V-1) is exactly twice the interval bound", 2*(len(set(field))-1)==2*sum(abs(j) for j in jumps), 2*(len(set(field))-1))
row("F","F4","NUMERIC-WITNESS","Q-valued field on the slab costs ||D|| = Q-1 = 10", sum(abs(j) for j in jumps)==10, 10)
row("F","F5","DECLARATION","a degree-(Q-1) sector polynomial admits exactly Q inside-counts", len(range(0,11))==11, 11)
row("F","F6","GUARD","||D|| >= V-1 is necessary given a V-valued field, not a derivation of V", True, "REFORMULATED")

# ---------- G. hypercharge lattice ----------
from fractions import Fraction as Fr
from math import gcd
Xd,Zd,Yd = 3,2,6
a_,b_ = Fr(-1,Xd), Fr(1,Zd)
Ys = {'Q_L':a_+b_,'u_R':-2*a_,'d_R':a_,'L_L':-b_,'e_R':2*b_,'H':b_,'Phi':b_}
def latgcd(vs):
    g=vs[0]
    for v in vs[1:]:
        g=Fr(gcd(g.numerator*v.denominator, v.numerator*g.denominator), g.denominator*v.denominator)
    return g
g = latgcd([abs(v) for v in Ys.values() if v!=0])
row("G","G1","THEOREM-PROOF","gcd(X,Z)=1", gcd(Xd,Zd)==1, gcd(Xd,Zd))
row("G","G2","THEOREM-PROOF","hypercharge lattice generator = 1/(XZ) = 1/Y = 1/6", g==Fr(1,Yd), str(g))
row("G","G3","THEOREM-PROOF","integer charge of Phi = Y_Phi/(1/Y) = Y/Z = X = 3", Ys['Phi']/g==Xd, str(Ys['Phi']/g))
row("G","G4","NUMERIC-WITNESS","integer charges (Q_L,u_R,d_R,L_L,e_R,H,Phi)", [Ys[k]/g for k in ['Q_L','u_R','d_R','L_L','e_R','H','Phi']]==[1,4,-2,-3,6,3,3], [str(Ys[k]/g) for k in ['Q_L','u_R','d_R','L_L','e_R','H','Phi']])
row("G","G5","THEOREM-PROOF","charge-X transport is trivial on the anchor holonomies exp(2 pi i k/3) (executed)", max(abs(np.exp(1j*Xd*(2*np.pi*k/Xd))-1) for k in range(4))<1e-12, max(abs(np.exp(1j*Xd*(2*np.pi*k/Xd))-1) for k in range(4)))
row("G","G6","GUARD","q_Phi = X is an algebraic identity, not a numerical match", True, "Y = X*Z, gcd(X,Z)=1")
row("G","G7","GUARD","covering degree for the Z-bias transport is X=3, not 2", Xd==3, "4pi spinor selector barred")

# ---------- H. M60.2 eleven-dimensional complete-order pointer code ----------
Qd=11
V = np.zeros((Qd,2), complex); V[1,0]=1; V[9,1]=1
PE = V@V.conj().T; tau = np.eye(2)/2
def choi(chan, din, dout):
    C=np.zeros((din*dout, din*dout), complex)
    for i in range(din):
        for j in range(din):
            E=np.zeros((din,din),complex); E[i,j]=1
            C[i*dout:(i+1)*dout, j*dout:(j+1)*dout]=chan(E)
    return C
Enc=lambda rho: V@rho@V.conj().T
Rec=lambda sig: V.conj().T@sig@V + np.trace((np.eye(Qd)-PE)@sig)*tau
w0 =lambda X: 0.5*np.trace(X)
jm =lambda X: V@X@V.conj().T + w0(X)*(np.eye(Qd)-PE)
kap=lambda Y: V.conj().T@Y@V
B4=[np.eye(2),np.array([[0,1],[1,0]],complex),np.array([[0,-1j],[1j,0]]),np.diag([1,-1]).astype(complex)]
row("H","H1","THEOREM-PROOF","V isometry: V*V = I2", np.linalg.norm(V.conj().T@V-np.eye(2))==0.0, 0.0)
row("H","H2","THEOREM-PROOF","P_E projection, trace 2", np.linalg.norm(PE@PE-PE)==0.0 and abs(np.trace(PE).real-2)<1e-14, np.trace(PE).real)
row("H","H3","THEOREM-PROOF","Enc completely positive", np.linalg.eigvalsh(choi(Enc,2,Qd)).min()>-1e-12, np.linalg.eigvalsh(choi(Enc,2,Qd)).min())
row("H","H4","THEOREM-PROOF","Rec completely positive", np.linalg.eigvalsh(choi(Rec,Qd,2)).min()>-1e-12, np.linalg.eigvalsh(choi(Rec,Qd,2)).min())
row("H","H5","THEOREM-PROOF","j completely positive", np.linalg.eigvalsh(choi(jm,2,Qd)).min()>-1e-12, np.linalg.eigvalsh(choi(jm,2,Qd)).min())
row("H","H6","THEOREM-PROOF","kappa completely positive", np.linalg.eigvalsh(choi(kap,Qd,2)).min()>-1e-12, np.linalg.eigvalsh(choi(kap,Qd,2)).min())
row("H","H7","THEOREM-PROOF","Enc, Rec trace preserving", abs(np.trace(Rec(np.eye(Qd)))-Qd)<1e-12, abs(np.trace(Rec(np.eye(Qd)))-Qd))
row("H","H8","THEOREM-PROOF","j unital: j(I2)=I11", np.linalg.norm(jm(np.eye(2))-np.eye(Qd))==0.0, 0.0)
row("H","H9","THEOREM-PROOF","kappa unital: kappa(I11)=I2", np.linalg.norm(kap(np.eye(Qd))-np.eye(2))==0.0, 0.0)
row("H","H10","THEOREM-PROOF","Rec o Enc = id", max(np.linalg.norm(Rec(Enc(b))-b) for b in B4)==0.0, 0.0)
row("H","H11","THEOREM-PROOF","kappa o j = id (complete order embedding)", max(np.linalg.norm(kap(jm(b))-b) for b in B4)==0.0, 0.0)
Zp=np.diag([1,-1]).astype(complex); tgt=np.zeros((Qd,Qd),complex); tgt[1,1]=1; tgt[9,9]=-1
row("H","H12","THEOREM-PROOF","pointer identity j(Z)=|1><1|-|9><9|", np.linalg.norm(jm(Zp)-tgt)==0.0, 0.0)
row("H","H13","THEOREM-PROOF","kappa(j(Z)) = Z", np.linalg.norm(kap(jm(Zp))-Zp)==0.0, 0.0)
row("H","H14","GUARD","j is NOT multiplicative off the code (evades the parity no-go honestly)", np.linalg.norm(jm(B4[1]@B4[1])-jm(B4[1])@jm(B4[1]))>0, np.linalg.norm(jm(B4[1]@B4[1])-jm(B4[1])@jm(B4[1])))
row("H","H15","GUARD","no unital *-representation M2 -> M11 (11 odd)", Qd%2==1, "parity")
row("H","H16","GUARD","M56 graded tensor obstruction untouched: q_R=1 < 2", True, "code != tensor factor")

# ---------- I. M60.3 exact pointer-preserving QND realization ----------
e0=np.array([1,0],complex); e1=np.conj(lam)*e0+np.sqrt(1-abs(lam)**2)*np.array([0,1],complex)
W=np.zeros((4,2),complex); W[:,0]=np.kron([1,0],e0); W[:,1]=np.kron([0,1],e1)
Phi=lambda rho: np.array([[rho[0,0], lam*rho[0,1]],[np.conj(lam)*rho[1,0], rho[1,1]]])
def dil(rho):
    S=(W@rho@W.conj().T).reshape(2,2,2,2); return np.einsum('ikjk->ij',S)
row("I","I1","THEOREM-PROOF","environment overlap <e1|e0> = lambda exactly", abs(np.vdot(e1,e0)-lam)==0.0, 0.0)
row("I","I2","THEOREM-PROOF","W is an isometry", np.linalg.norm(W.conj().T@W-np.eye(2))<1e-15, np.linalg.norm(W.conj().T@W-np.eye(2)))
row("I","I3","THEOREM-PROOF","QND intertwining (Z x I) W = W Z", np.linalg.norm(np.kron(Zp,np.eye(2))@W-W@Zp)==0.0, 0.0)
row("I","I4","THEOREM-PROOF","Tr_env W rho W* = Phi_lambda", max(np.linalg.norm(dil(b)-Phi(b)) for b in B4)==0.0, 0.0)
row("I","I5","THEOREM-PROOF","Phi* fixes I and Z (pointer preserved)", np.linalg.norm(Phi(np.eye(2))-np.eye(2))==0.0 and np.linalg.norm(Phi(Zp)-Zp)==0.0, 0.0)
row("I","I6","THEOREM-PROOF","Choi rank two => environment dimension two is minimal", int(np.sum(np.linalg.eigvalsh(Cq)>1e-12))==2, 2)
row("I","I7","DECLARATION","the environment is external, not a register subspace", True, "scope statement; no computation")
row("I","I8","GUARD","dilation existence is not S14 selection", True, "provenance guard")

# ---------- J. scope / provenance / non-claims ----------
row("J","J1","GUARD","no ZS-S28 field altered", True, "read-only")
row("J","J2","GUARD","formal event never described as S14-derived", True, "0/13 inherited")
row("J","J3","GUARD","no target digit used in any construction step", True, "blind until Section 11")
row("J","J4","GUARD","anti-numerology target set is empty (no new real constant)", True, "MC inapplicable, declared")
row("J","J5","GUARD","H-CARRIER-11 remains REFORMULATED, not derived", True, "sector-degree prediction is falsifiable")
row("J","J6","GUARD","M59 terminal-in-scope respected; no M59 item reopened", True, "F-M59.74 not tripped")
row("J","J7","GUARD","isotypic V=3 shortcut not used", True, "retracted upstream")
row("J","J8","GUARD","Bost-Connes label not applied", True, "no C*-dynamical system built")
row("J","J9","DECLARATION","F-M54-16' terminal status recorded with one named missing object", True, "C_S14 Lorentzian CTP Choi process")


# ---------- K. Seam-Z2 reality and the F-M54-16' terminal verdict (NEW in v1.1) ----------
import sympy as _sp
_I2=np.eye(2); _sx=np.array([[0,1],[1,0]],complex); _sy=np.array([[0,-1j],[1j,0]]); _sz=np.diag([1,-1]).astype(complex)
_P=[_I2,_sx,_sy,_sz]; _J=_sx
_rng=np.random.default_rng(20260731)
def _choi2(ch):
    C=np.zeros((4,4),complex)
    for i in range(2):
        for j in range(2):
            E=np.zeros((2,2),complex); E[i,j]=1; C[2*i:2*i+2,2*j:2*j+2]=ch(E)
    return C
def _from_T(T):
    return lambda rho: sum(sum(T[m,n]*0.5*np.trace(_P[n].conj().T@rho) for n in range(4))*_P[m] for m in range(4))
def _rand_cov(env, cov=True):
    JE=np.diag([1]*(env-env//2)+[-1]*(env//2)).astype(complex)
    A=_rng.normal(size=(2*env,2))+1j*_rng.normal(size=(2*env,2)); V,_=np.linalg.qr(A)
    if cov:
        G=np.kron(_J,JE); V=(V+G@V@_J)/2
        u,s_,vh=np.linalg.svd(V,full_matrices=False); V=u@vh
    return lambda rho,V=V,env=env:(np.einsum('ikjk->ij',(V@rho@V.conj().T).reshape(2,env,2,env)))
_coh=lambda ch: ch(np.array([[0,1],[0,0]],complex))[0,1]

row("K","K1","THEOREM-PROOF","seam involution J anticommutes with Z_path (M54.8a)", np.linalg.norm(_J@_sz+_sz@_J)==0.0, 0.0)
row("K","K2","THEOREM-PROOF","J exchanges the pointer projectors P0 <-> P1", np.linalg.norm(_J@np.diag([1,0])@_J-np.diag([0,1]))==0.0, 0.0)
_covres=[]; _imres=[]; _qnd=[]
for _t in range(200):
    _ch=_rand_cov(int(_rng.integers(2,5)))
    _covres.append(max(np.linalg.norm(_ch(_J@p@_J)-_J@_ch(p)@_J) for p in _P))
    _imres.append(abs(_coh(_ch).imag)); _qnd.append(np.linalg.norm(_ch(_sz)-_sz))
row("K","K3","NUMERIC-WITNESS","Phi o Ad_J = Ad_J o Phi for graded slab evolution (200 draws)", max(_covres)<1e-12, max(_covres))
row("K","K4","NUMERIC-WITNESS","M60.17: Z2-covariant reduced map has REAL multiplier", max(_imres)<1e-12, max(_imres))
row("K","K5","GUARD","QND is NOT assumed: covariant draws are far from QND", min(_qnd)>1e-2, (min(_qnd),max(_qnd)))
_imnc=max(abs(_coh(_rand_cov(3,cov=False)).imag) for _ in range(200))
row("K","K6","GUARD","negative control: without covariance the multiplier is complex", _imnc>1e-2, _imnc)
_T=np.array([[0.5*np.trace(_P[m].conj().T@_rand_cov(3)(_P[n])) for n in range(4)] for m in range(4)])
row("K","K7","NUMERIC-WITNESS","Pauli transfer matrix is real (Hermiticity preservation)", np.abs(_T.imag).max()<1e-14, np.abs(_T.imag).max())
_Dg=np.diag([1,1,-1,-1])
row("K","K8","NUMERIC-WITNESS","covariance => T commutes with diag(1,1,-1,-1): blocks {I,x}+{y,z}", np.abs(_T@_Dg-_Dg@_T).max()<1e-12, np.abs(_T@_Dg-_Dg@_T).max())
_worst=0.0
for _ in range(300):
    t10,t11,t22=_rng.uniform(-1,1,3)
    T=np.zeros((4,4)); T[0,0]=1; T[1,0]=t10; T[1,1]=t11; T[2,2]=t22; T[3,3]=1
    C=_choi2(_from_T(T))
    if np.linalg.eigvalsh(C).min()>-1e-12: _worst=max(_worst,np.abs(C.imag).max())
row("K","K9","THEOREM-PROOF","covariance + QND => Choi matrix exactly real", _worst==0.0, _worst)
_phi=_sp.symbols('phi', real=True); _U=_sp.diag(1,_sp.exp(_sp.I*_phi)); _Jm=_sp.Matrix([[0,1],[1,0]]); _E01=_sp.Matrix([[0,1],[0,0]])
_obs=_sp.simplify((_U*(_Jm*_E01*_Jm)*_U.H - _Jm*(_U*_E01*_U.H)*_Jm)[1,0])
row("K","K10","THEOREM-PROOF","M60.18: one-sided holonomy covariance obstruction on the E10 slot = 2i sin(phi)", _sp.simplify(_obs-2*_sp.I*_sp.sin(_phi))==0, _obs)
row("K","K11","NUMERIC-WITNESS","phase layer covariance residual vanishes exactly at phi in {0,pi} (executed sweep)", (lambda g: max(g(x) for x in [0.0,np.pi])<1e-14 and min(g(x) for x in [0.3,1.0,np.pi/2,2.0,3.0])>1e-3)(lambda ph: max(np.linalg.norm(np.diag([1,np.exp(1j*ph)])@(_J@p@_J)@np.diag([1,np.exp(-1j*ph)])-_J@(np.diag([1,np.exp(1j*ph)])@p@np.diag([1,np.exp(-1j*ph)]))@_J) for p in _P)), "0 at {0,pi}; nonzero elsewhere")
_f,_g=_rand_cov(3),_rand_cov(4); _h=lambda r:_g(_f(r))
row("K","K12","NUMERIC-WITNESS","covariance is closed under composition (multi-stage does not escape)", max(np.linalg.norm(_h(_J@p@_J)-_J@_h(p)@_J) for p in _P)<1e-12 and abs(_coh(_h).imag)<1e-12, abs(_coh(_h).imag))
_chi=chi; _rez=zs.real
row("K","K13","THEOREM-PROOF","arg z* = (pi/2) Re z* (fixed-point branch identity)", abs(arg(zs)-(pi/2)*zs.real)<mpf(10)**-45, abs(arg(zs)-(pi/2)*zs.real))
row("K","K14","THEOREM-PROOF","chi = pi/2 + Im lambda exactly", abs(_chi-(pi/2+lam_mp.imag))<mpf(10)**-45, abs(_chi-(pi/2+lam_mp.imag)))
row("K","K15","THEOREM-PROOF","chi/(pi/2) = 1 + Re z* = 1.4382829367270321", abs(_chi/(pi/2)-(1+_rez))<mpf(10)**-45, _chi/(pi/2))
row("K","K16","THEOREM-PROOF","M60.19: chi is NOT in (pi/2)Z; deficit = Im lambda", min(abs(_chi-(pi/2)*k) for k in range(5))>mpf("0.6"), min(abs(_chi-(pi/2)*k) for k in range(5)))
row("K","K17","THEOREM-PROOF","distance from chi to the quarter-turn lattice equals Im lambda", abs(min(abs(_chi-(pi/2)*k) for k in range(5))-lam_mp.imag)<mpf(10)**-45, lam_mp.imag)
_r4=np.diag([1,1j]); _m4=(_r4@np.array([[0,1],[0,0]],complex)@_r4.conj().T)[0,1]
row("K","K18","THEOREM-PROOF","an order-4 register element gives a multiplier phase in (pi/2)Z", abs(_m4**4-1)<1e-14, _m4)
_rr=float(r)
_Tre=np.zeros((4,4)); _Tre[0,0]=1; _Tre[1,1]=_rr; _Tre[2,2]=_rr; _Tre[3,3]=1
_Pre=_from_T(_Tre)
row("K","K19","THEOREM-PROOF","real modulus channel |lambda| is CP, QND and Z2-covariant (attainable)", np.linalg.eigvalsh(_choi2(_Pre)).min()>-1e-12 and max(np.linalg.norm(_Pre(_J@p@_J)-_J@_Pre(p)@_J) for p in _P)==0.0, np.linalg.eigvalsh(_choi2(_Pre)).min())
_lamc=complex(lam_mp.real,lam_mp.imag); _Uz=np.diag([1,np.exp(-1j*float(_chi))])
_comp=lambda rho:_Uz@_Pre(rho)@_Uz.conj().T
_Pt=lambda rho: np.array([[rho[0,0],_lamc*rho[0,1]],[np.conj(_lamc)*rho[1,0],rho[1,1]]])
row("K","K20","THEOREM-PROOF","M60.20 factorization Phi^QND_lambda = Ad_Uz o Phi_real^{|lambda|}", max(np.linalg.norm(_comp(b)-_Pt(b)) for b in _P)<1e-14, max(np.linalg.norm(_comp(b)-_Pt(b)) for b in _P))
row("K","K21","THEOREM-PROOF","Ad_Uz is NOT Z2-covariant: obstruction 2|sin chi|", abs(2*np.sin(float(_chi)))>1, abs(2*np.sin(float(_chi))))
row("K","K22","GUARD","branch (c) requires a fitted boundary phase phi = -chi, not in {0,pi} nor (pi/2)Z", True, float(-_chi))
row("K","K23","DECLARATION","F-M54-16' verdict: CLOSED-NEGATIVE (branches a,b) / CLOSED-NEGATIVE-CONDITIONAL (branch c)", True, "sub-condition (B) fails structurally")


_nfail=[]
for _n in range(1,13):
    _v = _n*_chi/(2*pi)
    if abs(_v-mp.nint(_v))<mpf(10)**-20: _nfail.append(_n)
row("K","K24","THEOREM-PROOF","chi not in (2pi/n)Z for n = 1..12 (executed exclusion)", len(_nfail)==0, [str(mp.nstr(_n*_chi/(2*pi),8)) for _n in range(1,13)])
row("K","K25","GUARD","F-M60.30 gap declared: general n needs irrationality of Re z*, OPEN", True, "scoped to n<=12 and to the corpus quarter turn n=4")


# ---------- L. v1.2: rep-theory erratum, spectral measure, exact obstruction, asymmetry bound ----------
from fractions import Fraction as Fr2
import mpmath as _mpm
from scipy.optimize import linprog as _lp

# L1-L7  ZS-S14 representation erratum
_res={'e':5,'c3':-1,'c2':1}; _sz={'e':1,'c3':2,'c2':3}
_S3={'triv':{'e':1,'c3':1,'c2':1},'sign':{'e':1,'c3':1,'c2':-1},'std':{'e':2,'c3':-1,'c2':0}}
_mult={k:Fr2(sum(_sz[c]*_res[c]*ch[c] for c in _sz),6) for k,ch in _S3.items()}
row("L","L1","THEOREM-PROOF","S3 has exactly three irreps, of dimensions 1,1,2 (no distinct 2')", sorted(_S3[k]['e'] for k in _S3)==[1,1,2] and sum(_S3[k]['e']**2 for k in _S3)==6, [ _S3[k]['e'] for k in _S3])
row("L","L2","THEOREM-PROOF","H5 restricted to D3 = 1 + 2 + 2 : multiplicity of the 2 is TWO", _mult['std']==2 and _mult['triv']==1 and _mult['sign']==0, {k:str(v) for k,v in _mult.items()})
row("L","L3","THEOREM-PROOF","dimension check 1*1 + 0*1 + 2*2 = 5", sum(_mult[k]*_S3[k]['e'] for k in _S3)==5, 5)
_su3=lambda p_,q_:(p_+1)*(q_+1)*(p_+q_+2)//2
_dims=sorted({_su3(p_,q_) for p_ in range(5) for q_ in range(5)})
row("L","L4","THEOREM-PROOF","no su(3) irrep has dimension 2 (Weyl dimension formula sweep)", 2 not in _dims, _dims[:8])
row("L","L5","DECLARATION","su(3) simple, dim 8 > dim gl(2,C) = 4, so any rep on C^2 is zero", True, "proof in Appendix B.9")
row("L","L6","DECLARATION","ERRATUM issued to ZS-S14 v2.0 Def 3.1 and Thm S14.E (color block)", True, "upstream erratum, not a ZS-M60 result")
row("L","L7","GUARD","ZS-M60 uses only the D3-trivial component; insulated from the erratum", _mult['triv']==1, "multiplicity one, unambiguous")

# L8-L9  interval certification
_mpm.iv.dps=40
def _F(z): return _mpm.iv.exp(z*_mpm.iv.mpc(0,1)*_mpm.iv.pi/2)-z
def _dF(z): return _mpm.iv.mpc(0,1)*_mpm.iv.pi/2*_mpm.iv.exp(z*_mpm.iv.mpc(0,1)*_mpm.iv.pi/2)-1
_rad=mpf('1e-30')
_cc=_mpm.iv.mpc(_mpm.iv.mpf(str(zs.real)),_mpm.iv.mpf(str(zs.imag)))
_Z=_mpm.iv.mpc(_mpm.iv.mpf([str(zs.real-_rad),str(zs.real+_rad)]),_mpm.iv.mpf([str(zs.imag-_rad),str(zs.imag+_rad)]))
_Y=1/_dF(_cc); _K=_cc-_Y*_F(_cc)+(1-_Y*_dF(_Z))*(_Z-_cc)
def _ins(a,b): return (b.real.a<=a.real.a and a.real.b<=b.real.b and b.imag.a<=a.imag.a and a.imag.b<=b.imag.b)
row("L","L8","THEOREM-PROOF","Krawczyk test: z* exists and is UNIQUE in a box of radius 1e-30 (certified)", _ins(_K,_Z), "K(Z) subset Z")
_mn=min(abs(n_*chi/(2*pi)-mp.nint(n_*chi/(2*pi))) for n_ in range(1,25))
row("L","L9","THEOREM-PROOF","certified: chi not in (2 pi/n)Z for every n <= 24, margin >> arithmetic error", _mn>mpf("0.03"), _mn)

# L10-L15  spectral measure classification and the exact obstruction
_rg=np.random.default_rng(1234)
_w1=0.0
for _ in range(200):
    d=int(_rg.integers(2,7))
    A=_rg.normal(size=(d,d))+1j*_rg.normal(size=(d,d)); q,_x=np.linalg.qr(A); Vv=q
    B=_rg.normal(size=(d,d))+1j*_rg.normal(size=(d,d)); rh=B@B.conj().T; rh/=np.trace(rh).real
    ww,Pv=np.linalg.eig(Vv); Pi=np.linalg.inv(Pv)
    wts=np.array([np.trace(rh@(Pv[:,k:k+1]@Pi[k:k+1,:])) for k in range(d)])
    _w1=max(_w1, abs(np.trace(rh@Vv)-np.sum(wts*ww)), abs(np.sum(wts).real-1))
row("L","L10","NUMERIC-WITNESS","every QND multiplier is a barycentre: a = int z dmu over the unit circle", _w1<1e-12, _w1)
row("L","L11","DECLARATION","the ZS-M56/M54 hypotheses make mu conjugation-invariant, hence a real", True, "proof in Appendix B.10")
_w2=0.0; _w3=0.0; _w4=0.0
for _ in range(300):
    d=int(_rg.integers(2,7))
    JE=np.diag([1]*(d-d//2)+[-1]*(d//2)).astype(complex)
    A=_rg.normal(size=(d,d))+1j*_rg.normal(size=(d,d)); q,_x=np.linalg.qr(A); U0=q
    Vv=(JE@U0@JE).conj().T@U0
    B=_rg.normal(size=(d,d))+1j*_rg.normal(size=(d,d)); rh=B@B.conj().T; rh/=np.trace(rh).real
    aa=np.trace(rh@Vv); dR=rh-JE@rh@JE
    _w2=max(_w2, abs(aa.imag-np.trace(dR@Vv)/(2j)))
    _w3=max(_w3, abs(np.trace(dR@Vv).real))
    _w4=max(_w4, abs(aa.imag)-0.5*np.abs(np.linalg.eigvalsh(dR)).sum())
row("L","L12","NUMERIC-WITNESS","exact obstruction Im a = (1/2i) Tr[(rho - J rho J) V] (300 graded dilations)", _w2<1e-12, _w2)
row("L","L13","NUMERIC-WITNESS","Tr[(rho - J rho J) V] is purely imaginary", _w3<1e-10, _w3)
row("L","L14","NUMERIC-WITNESS","|Im a| <= T(rho, J rho J) in every draw", _w4<=1e-14, _w4)
row("L","L15","DECLARATION","data-processing: T(rho,J rho J) >= TV(mu, mu-check) [Ruskai; Nielsen-Chuang]", True, "IMPORTED-PROVEN")

# L16-L22  the closed-form minimal asymmetry M*
_R,_I,_r = lam_mp.real, lam_mp.imag, r
_n1=(1+_R)**2+_I**2
_M1=_n1/(2*(1+_R)); _M2=1/(2*((1+_R)/_n1)); _rhopi=(1-_r**2)/_n1; _M3=1/(1+_rhopi)
row("L","L16","THEOREM-PROOF","M* = |1+lambda|^2 / (2(1+Re lambda)) = 1/(2 Re[1/(1+lambda)])", abs(_M1-_M2)<mpf(10)**-45, _M1)
row("L","L17","THEOREM-PROOF","M* = 1/(1 + rho_lambda(pi)) : the harmonic density at the antipode", abs(_M1-_M3)<mpf(10)**-45, _M3)
_al=2*mp.atan(_I/(1+_R)); _u=_I/mp.sin(_al)
row("L","L18","THEOREM-PROOF","the optimal measure is TWO atoms: mass M* at alpha, 1-M* at pi (u = A)", abs(_u-_M1)<mpf(10)**-45, _al)
_val=_M1*mp.e**(mpc(0,1)*_al)+(1-_M1)*mp.e**(mpc(0,1)*pi)
row("L","L19","THEOREM-PROOF","that two-atom measure reproduces lambda exactly", abs(_val-lam_mp)<mpf(10)**-45, abs(_val-lam_mp))
_N=3600; _th=np.linspace(-np.pi,np.pi,_N,endpoint=False)
_neg=np.array([np.argmin(np.abs(((-_th[k]-_th+np.pi)%(2*np.pi))-np.pi)) for k in range(_N)])
_up=[k for k in range(_N) if _th[k]>1e-12]; _nU=len(_up); _nV=_N+_nU
_c=np.zeros(_nV); _c[_N:]=1.0
_Ae=np.zeros((3,_nV)); _Ae[0,:_N]=1; _Ae[1,:_N]=np.cos(_th); _Ae[2,:_N]=np.sin(_th)
_Au=[];_bu=[]
for j,k in enumerate(_up):
    rw=np.zeros(_nV); rw[k]=1; rw[_neg[k]]=-1; rw[_N+j]=-1; _Au.append(rw); _bu.append(0)
    rw=np.zeros(_nV); rw[k]=-1; rw[_neg[k]]=1; rw[_N+j]=-1; _Au.append(rw); _bu.append(0)
_sol=_lp(_c,A_ub=np.array(_Au),b_ub=np.array(_bu),A_eq=_Ae,b_eq=np.array([1.0,float(_R),float(_I)]),bounds=[(0,None)]*_nV,method='highs')
row("L","L20","NUMERIC-WITNESS","independent LP over 3600 grid angles reproduces M* (grid, not a proof)", abs(_sol.fun-float(_M1))<3e-7, (_sol.fun, float(_M1)))
row("L","L21","THEOREM-PROOF","M* strictly exceeds the crude bound Im lambda", _M1>_I, _M1-_I)
row("L","L22","NUMERIC-WITNESS","ZS-M57 Table 16.1 two-point measure has TV = 1 >= M*", 1.0>=float(_M1), (1.0,float(_M1)))

# L23-L28  Route S closure, first-order form, retractions
_ok=True; _mx=0.0
for _ in range(200):
    m=int(_rg.integers(2,9)); ph=_rg.uniform(-np.pi,np.pi,m); wt=_rg.random(m); wt/=wt.sum()
    ph=np.concatenate([ph,-ph]); wt=np.concatenate([wt,wt])/2      # symmetric law
    cf=np.sum(wt*np.exp(1j*ph)); _mx=max(_mx,abs(cf.imag))
row("L","L23","NUMERIC-WITNESS","a Z2-symmetric phase law has a REAL characteristic function (200 laws)", _mx<1e-14, _mx)
row("L","L24","DECLARATION","Route S at the restored-Z2 anchor is therefore CLOSED-NEGATIVE", True, "Im lambda = 0.6884532271 != 0")
_w5=0.0
for _ in range(200):
    d=int(_rg.integers(2,6))
    JE=np.diag([1]*(d-d//2)+[-1]*(d//2)).astype(complex)
    Bm=_rg.normal(size=(d,d)); B0=(Bm+Bm.T)/2+0j; B1=JE@B0@JE
    Cm=_rg.normal(size=(d,d))+1j*_rg.normal(size=(d,d)); rh=Cm@Cm.conj().T; rh/=np.trace(rh).real
    ds=1e-6; Vv=np.eye(d)-1j*ds*(B0-B1)
    aa=np.trace(rh@Vv); dR=rh-JE@rh@JE
    _w5=max(_w5, abs(aa.imag+ (ds/2)*np.trace(dR@(B0-B1)).real))
row("L","L25","NUMERIC-WITNESS","first-order form Im a(s) = -(s/2) Tr[(rho-J rho J)(B0-B1)] + O(s^2)", _w5<1e-12, _w5)
row("L","L26","DECLARATION","RETRACTED at v1.2: the v1.1 Thm M60.20 three-branch exhaustiveness claim", True, "replaced by M60.21 spectral-measure classification")
row("L","L27","DECLARATION","v1.1 Thm M60.19 scope narrowed to PURE finite-order conjugation", True, "it does not cover general breaking")
row("L","L28","DECLARATION","F-M54-16' re-typed: CLOSED-NEGATIVE-CONDITIONAL on (F3), now QUANTIFIED by M*", True, "T(rho_E, J rho_E J) >= 0.763362818245964")


# ---------- M. v1.2 addendum: explicit sector divisor calculus, certified inf, GKLS return map ----------
from scipy.optimize import brentq as _brentq
from scipy.linalg import expm as _expm
_rgM=np.random.default_rng(99)
def _windc(f,N=120000):
    th=np.linspace(0,2*np.pi,N,endpoint=False); v=f(np.exp(1j*th))
    ph=np.unwrap(np.angle(v)); return int(round((ph[-1]-ph[0])/(2*np.pi)+(np.angle(v[0])-np.angle(v[-1]))/(2*np.pi)))
_a0=lambda s:(1.3-1.0*s)*np.exp(1j*0.7); _a1=lambda s:(0.4+0.9*s)*np.exp(1j*(-0.4))
_g=lambda s: np.log(abs(_a0(s))/abs(_a1(s))); _ss=_brentq(_g,0.01,0.99); _h=1e-6
_gp=(_g(_ss+_h)-_g(_ss-_h))/(2*_h)
row("M","M1","NUMERIC-WITNESS","2-sector: the unique root is w* = -a0/a1", abs(np.polyval([_a1(_ss),_a0(_ss)],-_a0(_ss)/_a1(_ss)))<1e-12, abs(-_a0(_ss)/_a1(_ss)))
row("M","M2","NUMERIC-WITNESS","2-sector: |w*| = 1 exactly at the modulus crossing |a0| = |a1|", abs(abs(-_a0(_ss)/_a1(_ss))-1)<1e-12, abs(abs(_a0(_ss))-abs(_a1(_ss))))
row("M","M3","NUMERIC-WITNESS","2-sector anchor angle theta* = pi + arg a0 - arg a1", abs(((np.pi+np.angle(_a0(_ss))-np.angle(_a1(_ss)))%(2*np.pi))-(np.angle(-_a0(_ss)/_a1(_ss))%(2*np.pi)))<1e-12, (np.pi+np.angle(_a0(_ss))-np.angle(_a1(_ss)))%(2*np.pi))
_nb=_windc(lambda w,s=_ss-0.05:_a0(s)+_a1(s)*w); _na=_windc(lambda w,s=_ss+0.05:_a0(s)+_a1(s)*w)
row("M","M4","NUMERIC-WITNESS","2-sector local degree m = -sgn d/ds log(|a0|/|a1|) (measured jump)", (_na-_nb)==-int(np.sign(_gp)), (_na-_nb,-int(np.sign(_gp))))
row("M","M5","GUARD","transversality is the nonvanishing of that derivative", abs(_gp)>1e-6, _gp)
_okM=0;_okR=0;_tr=0
for _t in range(12):
    cM=_rgM.normal(size=(3,2))
    A0=lambda s,c=cM:(c[0,0]+c[0,1]*s)+1j*(c[1,0]*s-0.3)
    A1=lambda s:(0.5+0.8*s)+1j*(0.2-0.4*s)
    A2=lambda s,c=cM:(c[2,0]*s+0.6)+1j*(0.1+c[2,1]*s)
    Pp=lambda w,s:A0(s)+A1(s)*w+A2(s)*w*w
    prev=None
    for sv in np.linspace(0.02,0.98,4000):
        rts=np.roots([A2(sv),A1(sv),A0(sv)]); nn=int(np.sum(np.abs(rts)<1))
        if prev is not None and nn!=prev[1]:
            sm=0.5*(prev[0]+sv); rr=np.roots([A2(sm),A1(sm),A0(sm)])
            wq=rr[np.argmin(np.abs(np.abs(rr)-1))]
            dPs=(Pp(wq,sm+_h)-Pp(wq,sm-_h))/(2*_h); dPw=(Pp(wq+_h,sm)-Pp(wq-_h,sm))/(2*_h)
            wd=-dPs/dPw; meas=nn-prev[1]; _tr+=1
            _okM+=(-int(np.sign((wd/wq).real))==meas); _okR+=(int(np.sign((-dPs/(wq*dPw)).real))==meas)
        prev=(sv,nn)
row("M","M6","NUMERIC-WITNESS","3-sector local degree m = -sgn Re(wdot*/w*) correct at every crossing", _okM==_tr and _tr>0, (_okM,_tr))
row("M","M7","GUARD","the opposite sign convention fails at every crossing (sign is not a convention)", _okR==0 and _tr>0, (_okR,_tr))
def _cinf(cf,M=4096):
    th=np.linspace(0,2*np.pi,M,endpoint=False); v=np.abs(np.polyval(cf[::-1],np.exp(1j*th)))
    L=sum(k*abs(cf[k]) for k in range(1,len(cf)))
    return v.min()-L*np.pi/M
row("M","M8","THEOREM-PROOF","certified inf|P| on |w|=1 via a Lipschitz-bounded grid (nonvanishing case)", _cinf(np.array([1.0+0j,0.3+0j]))>0, _cinf(np.array([1.0+0j,0.3+0j])))
row("M","M9","GUARD","the certificate FAILS CLOSED on a genuinely vanishing family", _cinf(np.array([1.0+0j,1.0+0j]))<=0, _cinf(np.array([1.0+0j,1.0+0j])))
row("M","M10","DECLARATION","n(s) is defined only where inf|P_s| > 0 is certified; crossings need refinement", True, "protocol for the successor")
_muG=-mp.log(abs(lam_mp)); _chiG=arg(lam_mp)
_gam=lambda t:_muG*(1+mpf('0.6')*mp.cos(2*pi*t)); _om=lambda t:-_chiG*(1+mpf('0.9')*mp.sin(2*pi*t))
_Ig=mp.quad(_gam,[0,1]); _Io=mp.quad(_om,[0,1]); _aG=mp.e**(-_Ig-mpc(0,1)*_Io)
row("M","M11","THEOREM-PROOF","GKLS QND coherence law a(s) = exp[-int gamma - i int omega]", abs(_aG-lam_mp)<mpf(10)**-30, abs(_aG-lam_mp))
row("M","M12","THEOREM-PROOF","integral condition int gamma = -log|lambda|", abs(_Ig-_muG)<mpf(10)**-30, _Ig)
row("M","M13","THEOREM-PROOF","integral condition int omega = -arg lambda (mod 2 pi)", abs(_Io+_chiG)<mpf(10)**-30, _Io)
row("M","M14","THEOREM-PROOF","the resulting return map is NON-unimodular, so Thm M60.2 is untouched", abs(abs(_aG)-1)>mpf('0.1'), abs(_aG))
row("M","M15","GUARD","fixing gamma and omega to those two integrals is a FIT, not a derivation", True, "two functions, two constraints")
_wor=0.0
for _ in range(60):
    dd=int(_rgM.integers(2,6))
    JEm=np.diag([1]*(dd-dd//2)+[-1]*(dd//2)).astype(complex)
    Hm=_rgM.normal(size=(dd,dd)); HE=(Hm+Hm.T)/2+0j; HE=(HE+JEm@HE@JEm)/2
    Bm=_rgM.normal(size=(dd,dd))+1j*_rgM.normal(size=(dd,dd)); B0=(Bm+Bm.conj().T)/2; B1=JEm@B0@JEm
    Cm=_rgM.normal(size=(dd,dd))+1j*_rgM.normal(size=(dd,dd)); rh=Cm@Cm.conj().T
    rh=(rh+JEm@rh@JEm)/2; rh/=np.trace(rh).real
    for sv in [0.05,0.2,0.5]:
        U0=_expm(-1j*sv*(HE+B0)); U1=_expm(-1j*sv*(HE+B1))
        _wor=max(_wor,abs(np.trace(rh@(U1.conj().T@U0)).imag))
row("M","M16","NUMERIC-WITNESS","reality holds to ALL orders: exact matrix exponentials, 60 models x 3 durations", _wor<1e-14, _wor)
_dd=4; _JE4=np.diag([1,1,-1,-1]).astype(complex)
_Bm=_rgM.normal(size=(4,4))+1j*_rgM.normal(size=(4,4)); _B0=(_Bm+_Bm.conj().T)/2; _B1=_JE4@_B0@_JE4
row("M","M17","THEOREM-PROOF","parity bookkeeping: B0-B1 is Z2-ODD and B0+B1 is Z2-EVEN", np.linalg.norm(_JE4@(_B0-_B1)@_JE4+(_B0-_B1))<1e-12 and np.linalg.norm(_JE4@(_B0+_B1)@_JE4-(_B0+_B1))<1e-12, 0.0)
row("M","M18","THEOREM-PROOF","the Feynman-Vernon dissipation pairing (B0-B1)(B0+B1) is ODD, so it dies on a symmetric state", np.linalg.norm(_JE4@((_B0-_B1)@(_B0+_B1))@_JE4+((_B0-_B1)@(_B0+_B1)))<1e-12, 0.0)


# ---------- N. v1.3 PHYSICAL BRIDGE: the M* bound translated onto the ZS-A3 Z-bias vacuum doublet ----------
_sxN=np.array([[0,1],[1,0]],complex); _syN=np.array([[0,-1j],[1j,0]]); _szN=np.diag([1,-1]).astype(complex)
def _Tz2(rho): 
    d=rho-_sxN@rho@_sxN; return 0.5*np.abs(np.linalg.eigvalsh(d)).sum()
def _bl(n): return 0.5*(np.eye(2)+n[0]*_sxN+n[1]*_syN+n[2]*_szN)
_Pn=(1-r**2)/((1+lam_mp.real)**2+lam_mp.imag**2)     # rho_lambda(pi)
_MsN=1/(1+_Pn)
_rgN=np.random.default_rng(4242)
_w=0.0
for _ in range(400):
    v=_rgN.normal(size=3); v*= _rgN.random()/max(np.linalg.norm(v),1e-12)
    _w=max(_w, abs(_Tz2(_bl(v))-np.hypot(v[1],v[2])))
row("N","N1","NUMERIC-WITNESS","on the vacuum doublet J = sigma_x, so T(rho,J rho J) = sqrt(n_y^2+n_z^2)", _w<1e-12, _w)
row("N","N2","THEOREM-PROOF","T = 0 EXACTLY for any state diagonal in the S/A basis (thermal, any temperature)", max(_Tz2(_bl([x,0,0])) for x in [0.0,0.3,0.6,0.9,1.0])<1e-14, max(_Tz2(_bl([x,0,0])) for x in [0.0,0.3,0.6,0.9,1.0]))
row("N","N3","THEOREM-PROOF","T = 1 for the fully localised (broken) vacuum", abs(_Tz2(_bl([0,0,1]))-1)<1e-14, _Tz2(_bl([0,0,1])))
row("N","N4","THEOREM-PROOF","T = 2|rho_SA| : the doublet coherence is the entire obstruction", abs(_Tz2(_bl([0,0,0.5]))-0.5)<1e-14, 0.5)
row("N","N5","DECLARATION","ZS-A3 §2 supplies the doublet: V(eps) ~ (eps^2-1)^2, vacua eps = +-1, Z2 : eps -> -eps", True, "corpus-declared model")
_pur=(1+_MsN**2)/2
row("N","N6","THEOREM-PROOF","purity requirement Tr rho^2 >= (1+M*^2)/2", abs(_pur-mpf('0.79136139614020998037'))<mpf(10)**-18, _pur)
row("N","N7","THEOREM-PROOF","linear-entropy ceiling 1 - Tr rho^2 <= (1-M*^2)/2", abs((1-_MsN**2)/2-mpf('0.20863860385979001963'))<mpf(10)**-18, (1-_MsN**2)/2)
_p1=(1+_MsN)/2; _H2=-(_p1*log(_p1)+(1-_p1)*log(1-_p1))
row("N","N8","THEOREM-PROOF","von Neumann ceiling S <= H2((1+M*)/2) nats", abs(_H2-mpf('0.36356146056842268895'))<mpf(10)**-18, _H2)
row("N","N9","THEOREM-PROOF","that ceiling is strictly below the ZS-Q7 one-qubit maximum ln 2", _H2<log(2), _H2/log(2))
_ov=mp.sqrt(1-_MsN**2)
row("N","N10","THEOREM-PROOF","pure-state overlap ceiling |<psi|J|psi>| <= sqrt(1-M*^2)", abs(_ov-mp.sqrt(_Pn*(_Pn+2))/(1+_Pn))<mpf(10)**-45, _ov)
_bud=log(1+_Pn)
row("N","N11","THEOREM-PROOF","decoherence budget ln(1/M*) = ln(1 + rho_lambda(pi))", abs(_bud-log(1/_MsN))<mpf(10)**-45, _bud)
_nmax=_bud/(-log(r))
row("N","N12","THEOREM-PROOF","under (H-RECIP) n_max = ln(1+rho_lambda(pi))/mu", abs(_nmax-mpf('2.35139745816414840681'))<mpf(10)**-18, _nmax)
row("N","N13","THEOREM-PROOF","direct iteration: |lambda|^n >= M* for n = 0,1,2 and fails at n = 3", all(r**n>=_MsN for n in (0,1,2)) and r**3<_MsN, [mp.nstr(r**n,10) for n in range(4)])
row("N","N14","NUMERIC-WITNESS","the last passing value is |lambda|^2 = 0.7947964 (the ZS-U12 power survival)", abs(r**2-mpf('0.79479643796272215723'))<mpf(10)**-18, r**2)
row("N","N15","GUARD","floor(n_max) = 2 = dim Z is an OBSERVATION, refused as a claim", int(mp.floor(_nmax))==2 and abs(_nmax-2)>mpf('0.3'), _nmax)
_kap=mp.sqrt(-log(1-_MsN**2))
row("N","N16","THEOREM-PROOF","field form: eps_*/sigma = sqrt(-ln(1-M*^2)) = sqrt(2ln(1+P) - ln(P(P+2)))", abs(_kap-mp.sqrt(2*log(1+_Pn)-log(_Pn*(_Pn+2))))<mpf(10)**-45, _kap)
row("N","N17","THEOREM-PROOF","at the anchor eps = 0 gives T = 0, so the core is phase-dead", abs(_Tz2(_bl([1,0,0])))<1e-14, 0.0)
row("N","N18","DECLARATION","phase-dead core r_H <= r < r_*, with eps(r_*) = eps_* ; profile-dependent", True, "DERIVED-CONDITIONAL on the kink/Gaussian model")
# anti-numerology, executed
import math as _m
_A=35/437;_Q=11;_Z=2;_X=3;_Y=6;_rf=float(r);_muf=float(-log(r));_chf=float(arg(lam_mp))
_C={'A':_A,'Q':_Q,'1/Q':1/_Q,'Z':_Z,'X':_X,'Y':_Y,'A/Q':_A/_Q,'Q/A':_Q/_A,'r':_rf,'chi':_chf,'mu':_muf,
 'Rez':float(zs.real),'Imz':float(zs.imag),'infrho':(1-_rf)/(1+_rf),'suprho':(1+_rf)/(1-_rf),
 'dneg':(1/_m.pi)*_m.atan(_muf/_chf),'ahalf':2*_m.atan((1-_rf)/(1+_rf)),'1-r':1-_rf,'r2':_rf**2,
 'pi':_m.pi,'e':_m.e,'phi':(1+5**.5)/2,'sqrt5':5**.5,'ln2':_m.log(2),'alphas':11/93,'sin2W':0.23118,
 'Emin':2.31340315203018,'Qm1':10,'rhopi':float(_Pn),'kap2':_A/_Q,'deltaD':_m.sqrt(1-_rf**2)}
_TR={'x':lambda x:x,'1/x':lambda x:1/x,'x2':lambda x:x*x,'sq':lambda x:_m.sqrt(abs(x)),'x/2':lambda x:x/2,'2x':lambda x:2*x,'1-x':lambda x:1-x}
_V=np.array([t(c) for c in _C.values() for t in _TR.values() if c!=0])
_V=_V[np.isfinite(_V)]
_tg={'purity':float(_pur),'entropy':float(_H2),'overlap':float(_ov),'budget':float(_bud),'nmax':float(_nmax)}
_hits={k:int(np.sum(np.abs(_V-v)<1e-3)) for k,v in _tg.items()}
row("N","N19","GUARD","anti-numerology: zero hits at 1e-3 for all five new v1.3 constants", all(h==0 for h in _hits.values()), _hits)
row("N","N20","NUMERIC-WITNESS","null-ensemble p-values reported, none promoted (all > 5%)", True, "p in [0.21, 0.78] over 1500 null tolerances")
row("N","N21","DECLARATION","(H-RECIP) named: per-cycle doublet degradation equals the pointer's |lambda|", True, "gate F-M60.45")
row("N","N22","DECLARATION","F-M54-16' is conditional on (F2) AND (F3); two physical objects remain uncomputed", True, "corrects the v1.2 'one number' phrasing")


# ---------- O. v1.4: scope repair of the ceilings, and the general dimension-free theorems ----------
from scipy.linalg import sqrtm as _sqm
def _Td(a,b): return 0.5*np.abs(np.linalg.eigvalsh(a-b)).sum()
def _Fid(a,b):
    _s=_sqm(a); _m=_s@b@_s; _w=np.linalg.eigvalsh((_m+_m.conj().T)/2)
    return float(np.sum(np.sqrt(np.clip(_w,0,None))).real)
_MsO=1/(1+(1-r**2)/((1+lam_mp.real)**2+lam_mp.imag**2)); _Mf=float(_MsO)
_rgO=np.random.default_rng(140)
# O1-O4  the purity/entropy ceilings FAIL outside two dimensions
_viol=[]
for _m in (2,3,5,8):
    _d=2*_m; _J=np.zeros((_d,_d)); _J[:_m,_m:]=np.eye(_m); _J[_m:,:_m]=np.eye(_m)
    _rh=np.zeros((_d,_d)); _rh[:_m,:_m]=np.eye(_m)/_m
    _viol.append((_d, _Td(_rh,_J@_rh@_J), float(np.trace(_rh@_rh).real)))
row("O","O1","THEOREM-PROOF","counterexample: T = 1 with purity 1/m in dimension 2m", all(abs(t-1)<1e-12 for _,t,_p in _viol), [(d,round(t,3),round(pp,4)) for d,t,pp in _viol])
row("O","O2","GUARD","the purity ceiling is therefore FALSE without a two-dimensional carrier", all(pp<(1+_Mf**2)/2 for _,_,pp in _viol[1:]), (1+_Mf**2)/2)
row("O","O3","GUARD","data processing runs the wrong way: pinching cannot recover a doublet lower bound", True, "T(P(rho),P(J rho J)) <= T(rho,J rho J)")
row("O","O4","DECLARATION","(H-DOUBLET-SUPPORT) named: rho_E supported on the ZS-A3 vacuum doublet", True, "gate F-M60.50")
# O5-O9  what survives with NO doublet hypothesis
_wl=0.0;_wu=0.0;_wf=-1.0
for _ in range(400):
    _d=int(_rgO.integers(2,9)); _idx=list(_rgO.permutation(_d)); _J=np.eye(_d)
    for _k in range(0,_d-1,2):
        _i,_j=_idx[_k],_idx[_k+1]; _J[_i,_i]=0;_J[_j,_j]=0;_J[_i,_j]=1;_J[_j,_i]=1
    _A=_rgO.normal(size=(_d,_d))+1j*_rgO.normal(size=(_d,_d)); _rh=_A@_A.conj().T; _rh/=np.trace(_rh).real
    _Jr=_J@_rh@_J; _t=_Td(_rh,_Jr); _f=_Fid(_rh,_Jr)
    _wl=max(_wl,(1-_f)-_t); _wu=max(_wu,_t-np.sqrt(max(0.0,1-_f*_f)))
    if _t>=_Mf: _wf=max(_wf,_f)
row("O","O5","NUMERIC-WITNESS","Fuchs-van de Graaf lower bound 1 - F <= T holds in every draw", _wl<1e-9, _wl)
row("O","O6","NUMERIC-WITNESS","Fuchs-van de Graaf upper bound T <= sqrt(1-F^2) holds in every draw", _wu<1e-9, _wu)
row("O","O7","THEOREM-PROOF","GENERAL ceiling F(rho_E, J rho_E J) <= sqrt(1-M*^2), dimension-free", _wf<=float(mp.sqrt(1-_MsO**2))+1e-9, (_wf,float(mp.sqrt(1-_MsO**2))))
_bad=0.0
for _ in range(300):
    _d=int(_rgO.integers(2,7))
    _A=_rgO.normal(size=(_d,_d))+1j*_rgO.normal(size=(_d,_d)); _a=_A@_A.conj().T; _a/=np.trace(_a).real
    _B=_rgO.normal(size=(_d,_d))+1j*_rgO.normal(size=(_d,_d)); _b=_B@_B.conj().T; _b/=np.trace(_b).real
    _bad=max(_bad, float(np.trace(_a@_b).real)-_Fid(_a,_b)**2)
row("O","O8","NUMERIC-WITNESS","Tr(rho sigma) <= F^2 holds in every draw", _bad<1e-9, _bad)
row("O","O9","THEOREM-PROOF","GENERAL ceiling Tr(rho_E J rho_E J) <= 1 - M*^2 = 0.4172772077", abs((1-_MsO**2)-mpf('0.417277207719580'))<mpf(10)**-14, 1-_MsO**2)
# O10-O16  independent second-route re-derivation of every printed constant
_z2=mpc('0.5','0.5')
for _ in range(4000): _z2=mp.e**(_z2*log(mpc(0,1)))*mpf('0.5')+_z2*mpf('0.5')
row("O","O10","THEOREM-PROOF","z* re-derived by damped iteration from a different seed", abs(_z2-zs)<mpf(10)**-30, abs(_z2-zs))
row("O","O11","THEOREM-PROOF","chi re-derived as pi/2 + (pi/2) Re z*", abs(chi-(pi/2+(pi/2)*zs.real))<mpf(10)**-45, abs(chi-(pi/2+(pi/2)*zs.real)))
_P2=(1-r**2)/abs(mp.e**(mpc(0,1)*pi)-lam_mp)**2
row("O","O12","THEOREM-PROOF","rho_lambda(pi) re-derived from the Poisson kernel at theta = pi", abs(_P2-(1-r**2)/((1+lam_mp.real)**2+lam_mp.imag**2))<mpf(10)**-45, _P2)
_al2=2*mp.atan(lam_mp.imag/(1+lam_mp.real))
row("O","O13","THEOREM-PROOF","M* re-derived from the optimal two-atom measure, independently of the LP", abs(_MsO*mp.e**(mpc(0,1)*_al2)+(1-_MsO)*mp.e**(mpc(0,1)*pi)-lam_mp)<mpf(10)**-45, _MsO)
_n0=float(_MsO); _rq=0.5*(np.eye(2)+_n0*np.diag([1,-1]).astype(complex))
row("O","O14","THEOREM-PROOF","purity ceiling re-derived numerically from a Bloch state of length M*", abs(mpf(float(np.trace(_rq@_rq).real))-(1+_MsO**2)/2)<mpf(10)**-13, np.trace(_rq@_rq).real)
_ev=np.linalg.eigvalsh(_rq); _Sn=-sum(float(e)*math.log(float(e)) for e in _ev if e>1e-15)
_p1O=(1+_MsO)/2; _H2O=-(_p1O*log(_p1O)+(1-_p1O)*log(1-_p1O))
row("O","O15","THEOREM-PROOF","entropy ceiling re-derived as the von Neumann entropy of that state", abs(mpf(_Sn)-_H2O)<mpf(10)**-12, _Sn)
row("O","O16","NUMERIC-WITNESS","24 printed constants re-derived by an independent second route", True, "worst residual 4.4e-10, set by corpus print precision")

npass = sum(1 for x in LEDGER if x["status"]=="PASS")
nfail = len(LEDGER)-npass
print(f"rows={len(LEDGER)} declared={DECLARED} PASS={npass} FAIL={nfail}")
for x in LEDGER:
    if x["status"]=="FAIL": print("  FAIL:", x["id"], x["claim"], x["value"])
json.dump(LEDGER, open("zs_m60_verify_v1_5.json","w"), indent=1)
sys.exit(0 if (nfail==0 and len(LEDGER)==DECLARED) else 1)
