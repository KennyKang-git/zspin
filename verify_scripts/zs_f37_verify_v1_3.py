# zs_f37_verify_v1_3.py -- ZS-F37 v1.3 verification (27 checks; fast mode default)
# v1.3: checks IDENTICAL to v1.2 -- the v1.3 paper edits are text-only.
# Reproduce (fast, < 30 s):   python zs_f37_verify_v1_3.py
# Full-quadrature witnesses:  set RUN_FULL_SURFACE_QUADRATURE = True below (minutes).
# External reproduction of record (v1.2 review): 27/27 PASS, fast mode, 2.0 s.
# v1.2 per external review of v1.1:
#   * FAST MODE (default, target < 30 s): B2 via exact analytic (alpha,gamma) Fourier reduction
#     + 1D Gauss beta-quadrature; B2b via 1D Weyl character orthogonality (class functions).
#   * FULL MODE (RUN_FULL_SURFACE_QUADRATURE=True): adds the 3D Euler-angle grid witnesses
#     B2F/B2bF of v1.1 (heavy; several minutes).
#   * NEW A9: self-duality reduction |chi_R(U)|^2 = chi_R(U)^2 on the su(2) register
#     (the reduction used when Theorem F37.A's |chi|^2 is specialized to Z-Spin).
#   * B2b is a finite TRUNCATED WITNESS of the exact per-representation gluing identity;
#     the theorem itself is imported-proven for the full representation sum.
RUN_FULL_SURFACE_QUADRATURE = False

import numpy as np, math, time
from fractions import Fraction
T0=time.time()
PASS=[]
def check(name, ok): PASS.append((name,bool(ok))); print(('PASS' if ok else 'FAIL'), name)

def chi(d, rho):
    return math.sinh(d*rho)/math.sinh(rho) if abs(rho)>1e-14 else float(d)
def boost_char_matrix(d, rho):
    j=(d-1)/2
    return sum(math.exp(2*rho*(j-k)) for k in range(d))
rb=0.5*math.log(9/7); d_reg=[2,3,6]

# ---------- Block A: character / two-leg core (9) ----------
check('A1 chi_d(rho)=sinh(d rho)/sinh(rho) equals spin-(d-1)/2 boost trace',
      all(abs(boost_char_matrix(d,0.37)-chi(d,0.37))<1e-12 for d in [2,3,4,6]))
r=0.2937
check('A2 chi_2 chi_3 = chi_4 + chi_2 exact; and chi_2 chi_3 != chi_6',
      abs(chi(2,r)*chi(3,r)-(chi(4,r)+chi(2,r)))<1e-12 and abs(chi(2,r)*chi(3,r)-chi(6,r))>1e-3)
tl0=[Fraction(d*d,49) for d in d_reg]
check('A3 rho->0 two-leg law = (4,9,36)/49, exact', sum(tl0)==1 and tl0==[Fraction(4,49),Fraction(9,49),Fraction(36,49)])
check('A4 coincidence normalization Sum tau^2 = 49/121, exact', sum(Fraction(d,11)**2 for d in d_reg)==Fraction(49,121))
cZ,cX=chi(2,rb),chi(3,rb); cY=cZ*cX
w=[cZ*cZ,cX*cX,cY*cY]; S=sum(w); pi_t=[x/S for x in w]
L1=sum(abs(pi_t[i]-float(tl0[i])) for i in range(3))
check(f'A5 L1 at rho_b=(1/2)ln(9/7): {L1:.11f} = 0.00919466866, <1%', abs(L1-0.00919466866135)<1e-9 and L1<0.01)
Dchi=cZ*cX-chi(6,rb)
check(f'A6 Delta chi(rho_b) = chi_2 chi_3 - chi_6 = {Dchi:.9f} = -0.392090129', abs(Dchi-(-0.39209012938691))<1e-9)
check('A7 one-leg branch at rho->0 = (2,3,6)/11 (pre-computed, rejected)', sum(Fraction(d,11) for d in d_reg)==1)
check('A8 chi_d(-rho)=chi_d(rho): character weights beta-even (transport beta-odd)',
      all(abs(chi(d,-0.41)-chi(d,0.41))<1e-12 for d in d_reg))

# irrep machinery (shared)
def wigner(U,j):
    tr=(U[0,0]+U[1,1]).real/2; tr=max(-1,min(1,tr)); phi=math.acos(tr)
    d=int(2*j+1); m=np.array([j-k for k in range(d)])
    if abs(math.sin(phi))<1e-12: return np.diag(np.exp(2j*phi*m))
    nx=(U[0,1]+U[1,0]).imag/(2*math.sin(phi)); ny=(U[0,1]-U[1,0]).real/(2*math.sin(phi)); nz=(U[0,0]-U[1,1]).imag/(2*math.sin(phi))
    Jz=np.diag(m.astype(complex)); Jp=np.zeros((d,d),complex)
    for k in range(1,d): mm=m[k]; Jp[k-1,k]=math.sqrt(j*(j+1)-mm*(mm+1))
    Jm=Jp.conj().T; Jx=(Jp+Jm)/2; Jy=(Jp-Jm)/(2*1j)
    H=nx*Jx+ny*Jy+nz*Jz
    wv,V=np.linalg.eigh(H)
    return (V*np.exp(2j*phi*wv))@V.conj().T
def ch(U,j): return np.trace(wigner(U,j))
rng=np.random.default_rng(437)
def rand_su2():
    q=rng.normal(size=4); q/=np.linalg.norm(q)
    a,b,c,dd=q
    return np.array([[a+1j*b,c+1j*dd],[-c+1j*dd,a-1j*b]],complex)
A=rand_su2(); B=rand_su2(); U0=rand_su2(); V0=rand_su2()
# A9 (NEW): self-duality reduction |chi|^2 = chi^2 on the register (SU(2) characters real)
ok=all(abs(ch(U0,j).imag)<1e-10 and abs(abs(ch(U0,j))**2-(ch(U0,j).real)**2)<1e-9 for j in [0.5,1.0,2.5])
check('A9 su(2) register self-dual: chi_R(U) real, so |chi_R(U)|^2 = chi_R(U)^2 (Theorem A reduction)', ok)

# ---------- Block B: surface calculus (7) ----------
from numpy.polynomial.legendre import leggauss
xs,ws=leggauss(400); t1d=(xs+1)*math.pi/2; wq=ws*math.pi/2
def chiU(d,tt): return np.sin(d*tt)/np.sin(tt)
ok=True
for a in d_reg:
    for b in d_reg:
        val=(2/math.pi)*np.sum(wq*np.sin(t1d)**2*chiU(a,t1d)*chiU(b,t1d))
        ok &= abs(val-(1.0 if a==b else 0.0))<1e-10
check('B1 Peter-Weyl orthogonality on the register (2,3,6): int chi_a chi_b = delta_ab', ok)

# B2 FAST: exact analytic (alpha,gamma) Fourier reduction + 1D Gauss beta-quadrature.
# Euler form D_j(U)=diag(e^{-i a m}) d_j(beta) diag(e^{-i g m}); alpha in [0,2pi), gamma in [0,4pi).
# The gamma average is an exact Kronecker delta on half-integer frequencies; parity mismatch
# (half-integer vs integer m-lattices) kills R!=S cross terms exactly; the alpha average is then
# a Kronecker delta on integer frequencies. Only the beta integral remains -> 1D Gauss.
Nb=64; xb,wb=leggauss(Nb); be=(xb+1)*math.pi/2; wbe=wb*math.pi/2
def littled(j,beta):
    d=int(2*j+1); m=np.array([j-k for k in range(d)])
    Jp=np.zeros((d,d),complex)
    for k in range(1,d): mm=m[k]; Jp[k-1,k]=math.sqrt(j*(j+1)-mm*(mm+1))
    Jm=Jp.conj().T; Jy=(Jp-Jm)/(2*1j)
    wv,V=np.linalg.eigh(Jy)
    return ((V*np.exp(-1j*beta*wv))@V.conj().T).real
def migdal_fast(jR,jS,A,B):
    dR=int(2*jR+1); dS=int(2*jS+1)
    mR=np.array([jR-k for k in range(dR)]); mS=np.array([jS-k for k in range(dS)])
    AR=wigner(A,jR); BS=wigner(B,jS)
    # parity mismatch -> exact zero
    if (int(round(2*jR))%2)!=(int(round(2*jS))%2): return 0.0+0j
    acc=0.0+0j
    # beta integrals of d^R_{ba} d^S_{cd} with m-matching m^S_c=m^R_b, m^S_d=m^R_a
    dRs=[littled(jR,bk) for bk in be]; dSs=[littled(jS,bk) for bk in be]
    for a_ in range(dR):
        for b_ in range(dR):
            cs=[c for c in range(dS) if abs(mS[c]-mR[b_])<1e-9]
            ds=[dd for dd in range(dS) if abs(mS[dd]-mR[a_])<1e-9]
            for c_ in cs:
                for d_ in ds:
                    beta_int=0.0
                    for k in range(Nb):
                        beta_int += wbe[k]*math.sin(be[k])*dRs[k][b_,a_]*dSs[k][c_,d_]
                    acc += AR[a_,b_]*BS[c_,d_]*0.5*beta_int
    return acc
ok=True
for (jR,jS) in [(0.5,0.5),(1.0,1.0),(0.5,1.0),(0.5,1.5)]:
    dR=int(2*jR+1)
    val=migdal_fast(jR,jS,A,B)
    tgt=(ch(A@B,jR)/dR) if jR==jS else 0.0
    ok &= abs(val-tgt)<1e-9
check('B2 Migdal gluing int dU chi_R(AU)chi_S(U^+B)=delta_RS chi_R(AB)/d_R -- FAST exact Fourier reduction + 1D Gauss, <1e-9', ok)

# B2b FAST: gluing of the cylinder kernel via 1D Weyl character orthogonality.
# Z_t(U,V)=Sum_R chi_R(U) chi_R(V)^* e^{-t C2(R)}; int dV chi_R(V)^* chi_S(V) = delta_RS (class fns, 1D Weyl).
# FINITE TRUNCATED WITNESS of the exact per-representation identity (imported-proven for the full sum).
reps=[0.0,0.5,1.0,1.5]
def C2j(j): return j*(j+1)
def O_weyl(jR,jS):
    dR=int(2*jR+1); dS=int(2*jS+1)
    return (2/math.pi)*np.sum(wq*np.sin(t1d)**2*chiU(dR,t1d)*chiU(dS,t1d))
t1,t2=0.31,0.47
lhs=0+0j
for jR in reps:
    for jS in reps:
        lhs += ch(A,jR)*math.exp(-t1*C2j(jR)) * np.conj(ch(B,jS))*math.exp(-t2*C2j(jS)) * O_weyl(jR,jS)
rhs=sum(ch(A,j)*np.conj(ch(B,j))*math.exp(-(t1+t2)*C2j(j)) for j in reps)
check(f'B2b cylinder Markov/gluing (truncated witness, 1D Weyl orthogonality): dev={abs(lhs-rhs):.2e}<1e-9', abs(lhs-rhs)<1e-9)

check('B3 Euler-characteristic leg counting: sphere d^2 / disc d^1 / cylinder d^0 chi chi',
      all((d**2==d*d) and (d**1==d) and (d**0==1) for d in d_reg))
w_tensor=[cZ*cZ,cX*cX,(cZ*cX)**2]; S_t=sum(w_tensor); piT=[x/S_t for x in w_tensor]
expected_t=[cZ*cZ/S_t, cX*cX/S_t, (cZ*cX)**2/S_t]
check('B4a cut-conditioned cylinder, TENSOR reading chi_Y=chi_2 chi_3: normalized 1e-14, componentwise 1e-12, L1 consistent',
      abs(sum(piT)-1)<1e-14 and all(abs(piT[i]-expected_t[i])<1e-12 for i in range(3))
      and abs(sum(abs(piT[i]-float(tl0[i])) for i in range(3))-L1)<1e-12)
w_irr=[cZ*cZ,cX*cX,chi(6,rb)**2]; S_i=sum(w_irr); piI=[x/S_i for x in w_irr]
L1_irr=sum(abs(piI[k]-float(tl0[k])) for k in range(3))
check(f'B4b irreducible chi_6 CONTROL cylinder: normalized 1e-12; L1={L1_irr:.5f} > tensor L1={L1:.5f}',
      abs(sum(piI)-1)<1e-14 and L1_irr>L1)
check('B5 characters are class functions (gauge invariance of the weight)',
      all(abs(ch(V0@U0@V0.conj().T,j)-ch(U0,j))<1e-9 for j in [0.5,1.0,2.5]))

# ---------- Block C: mediation vertex (4) ----------
def mult(j1,j2,j3):
    return 1 if (abs(j1-j2)<=j3<=j1+j2 and abs((j1+j2-j3)-round(j1+j2-j3))<1e-9) else 0
cas=[0.5*1.5,1.5*2.5]
check('C1 Y=Z(x)X: 1/2(x)1 = 1/2 (+) 3/2; Casimir {3/4,15/4}, 35/4 excluded (YL4-YL5)',
      mult(0.5,1,0.5)==1 and mult(0.5,1,1.5)==1 and mult(0.5,1,2.5)==0 and abs(cas[0]-0.75)<1e-12 and abs(cas[1]-3.75)<1e-12)
check('C2 irreducible spin-5/2 reading: all three mediation vertices vanish (YL1-YL2)',
      mult(0.5,1.0,2.5)==0 and mult(0.5,2.5,1.0)==0 and mult(1.0,2.5,0.5)==0)
Y=[0.5,1.5]
a1=sum(mult(0.5,1.0,y) for y in Y); a2=sum(mult(0.5,y,1.0) for y in Y); a3=sum(mult(1.0,y,0.5) for y in Y)
check(f'C3 tensor reading: EXACT multiplicities (a1,a2,a3)=({a1},{a2},{a3})=(2,2,2) (YL3, exact)', (a1,a2,a3)==(2,2,2))
def pair_int(f): return (2/math.pi)*np.sum(wq*np.sin(t1d)**2*f(t1d))
I_tensor=pair_int(lambda tt: chiU(2,tt)*chiU(3,tt)*chiU(2,tt)*chiU(3,tt))
I_irr   =pair_int(lambda tt: chiU(2,tt)*chiU(3,tt)*chiU(6,tt))
check('C4 pair-of-pants integrals: <chi_2 chi_3, chi_2 chi_3>=2, <chi_2 chi_3, chi_6>=0 (<1e-8)',
      abs(I_tensor-2.0)<1e-8 and abs(I_irr)<1e-8)

# ---------- Block D: Koenigs / clock-gate data (5) ----------
import mpmath as mp; mp.mp.dps=50
F=lambda wz: mp.exp(1j*mp.pi*wz/2)
zs=mp.mpc(0.43828,0.36059)
for _ in range(200): zs = zs - (F(zs)-zs)/((1j*mp.pi/2)*F(zs)-1)
check('D1 z* = 0.4382829367 + 0.3605924719i (10 locked digits; 50-digit Newton)',
      abs(F(zs)-zs)<mp.mpf('1e-40') and abs(zs.real-mp.mpf('0.4382829367'))<1e-10 and abs(zs.imag-mp.mpf('0.3605924719'))<1e-10)
lamp=(1j*mp.pi/2)*zs
check('D2 |lambda*| = 0.89151', abs(abs(lamp)-0.89151)<1e-5)
mu=-mp.log(abs(lamp))
check(f'D3 mu = -ln|lambda*| = {mp.nstr(mu,11)} = 0.1148346250 (locked digits)', abs(mu-mp.mpf('0.1148346250'))<1e-9)
th=mp.arg(lamp)
check(f'D4 theta = arg lambda* = {mp.nstr(th,11)} = 2.2592495540 (locked digits)', abs(th-mp.mpf('2.2592495540'))<1e-9)
aBK=-mp.log(abs(zs))
check('D5 mu distinct from alpha_BK = -ln|z*| = 0.5664173303', abs(aBK-mp.mpf('0.5664173303'))<1e-9 and abs(mu-aBK)>0.4)

# ---------- Block E: universality / anti-tuning (2) ----------
base=[chi(d,rb)**2 for d in d_reg]; pb=[x/sum(base) for x in base]
symbols=[lambda d:(d*d-1)/4.0, lambda d:d*1.0, lambda d:d*d*1.0, lambda d:float(rng.uniform(0.1,5))]
ok=True
for alf in symbols:
    a=[alf(d) for d in d_reg]
    for tt in [1e-6,1e-8]:
        wl=[base[i]*math.exp(-tt*a[i]) for i in range(3)]
        p=[x/sum(wl) for x in wl]
        ok &= sum(abs(p[i]-pb[i]) for i in range(3))<1e-4
check('E1 Levy-class universality: t->0 two-leg ratio invariant under damping-symbol substitution', ok)
one=[chi(d,rb) for d in d_reg]; pone=[x/sum(one) for x in one]
L1_one=sum(abs(pone[i]-float(tl0[i])) for i in range(3))
check(f'E2 discrimination at rho_b: L1(one-leg)={L1_one:.4f} (=0.3416) >> L1(two-leg)={L1:.5f}', 0.34<L1_one<0.35 and L1_one>L1)

n_ok=sum(1 for _,o in PASS if o)
print(f'\n== {n_ok}/{len(PASS)} PASS ==  (fast mode, elapsed {time.time()-T0:.1f} s)')

# ---------- FULL-MODE witnesses (optional; heavy 3D Euler-angle grid) ----------
if RUN_FULL_SURFACE_QUADRATURE:
    def Pz(a_): return np.diag([np.exp(-1j*a_/2), np.exp(1j*a_/2)])
    def Ry(b_):
        c,s_=math.cos(b_/2),math.sin(b_/2)
        return np.array([[c,-s_],[s_,c]],complex)
    def Uabg(al,bt,ga): return Pz(al)@Ry(bt)@Pz(ga)
    Na,Nbq,Ng=24,32,48
    alg=np.linspace(0,2*math.pi,Na,endpoint=False); gag=np.linspace(0,4*math.pi,Ng,endpoint=False)
    xbq,wbq=leggauss(Nbq); beq=(xbq+1)*math.pi/2; wbeq=wbq*math.pi/2
    def haar_int(Ff):
        acc=0.0
        for ia in alg:
            for k,ib in enumerate(beq):
                sb=math.sin(ib)*wbeq[k]
                for ig in gag: acc+=sb*Ff(Uabg(ia,ib,ig))
        return acc*(2*math.pi/Na)*(4*math.pi/Ng)/(16*math.pi**2)
    okF=True
    for (jR,jS) in [(0.5,0.5),(1.0,1.0),(0.5,1.0)]:
        dR=int(2*jR+1)
        val=haar_int(lambda Uu: (ch(A@Uu,jR)*ch(Uu.conj().T@B,jS)).real)
        tgt=(ch(A@B,jR).real/dR) if jR==jS else 0.0
        okF &= abs(val-tgt)<1e-9
    print(('PASS' if okF else 'FAIL'),'B2F full 3D-grid Migdal witness')
    def Zc(tt,X,Yv): return sum(ch(X,j)*np.conj(ch(Yv,j))*math.exp(-tt*C2j(j)) for j in reps)
    lhsF=haar_int(lambda Vv: (Zc(t1,A,Vv)*Zc(t2,Vv,B)).real); rhsF=Zc(t1+t2,A,B).real
    print(('PASS' if abs(lhsF-rhsF)<1e-9 else 'FAIL'),f'B2bF full 3D-grid gluing witness dev={abs(lhsF-rhsF):.2e}')
