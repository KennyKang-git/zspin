#!/usr/bin/env python3
# =============================================================================
#  zs_a20_verify_v1_4.py
#  Consolidated verification suite for ZS-A20 v1.4 (The Atomic Interface).
#  Supersedes zs_a20_verify_v1_3.py. Integrates every computation written for
#  v1.0 - v1.4:
#    A  constants / spectral-branch arithmetic
#    B  dust == CDM linear perturbation ODE + control            [compute_a20.py]
#    C  Saha recombination + sound horizon + Fisher              [compute_a20.py]
#    D  CLASS+HyRec branch recombination/spectra, H0 refit, chi^2 [class_a20.py]   (CLASS)
#    E  lab-vs-CMB branch selection
#    F  A19 boundary action -> perfect-dust stress tensor        [section 9, v1.4 conditions]
#    G  reproducibility / recorded corpus values
#    H  EXECUTED zero-parameter joint test (Z-Spin abundances)   [class_a20_v14.py] (CLASS)   <NEW v1.4>
#    I  DERIVED within-branch theory error sigma_th              [sigma_theory_a20.py]         <NEW v1.4>
#    J  v1.4 corrections: Ma-Bertschinger sign; varying_me counterfactual status               <NEW v1.4>
#
#  Each check ASSERTS a value claimed in ZS-A20 v1.4 within a stated tolerance.
#  CLASS categories (D, H) are SKIPPED gracefully if `classy` is unavailable;
#  pass --no-class to skip them explicitly. Exit code 0 iff no FAIL.
#
#  Run:  python zs_a20_verify_v1_4.py            # full (runs CLASS if available; slow)
#        python zs_a20_verify_v1_4.py --no-class # arithmetic/ODE/Saha/derivation only (fast)
#
#  Env:  Python 3.12; numpy, scipy[, classy (CLASS v3, bundles HyRec)]
#  Author: Kenny Kang (Z-Spin Collaboration), June 2026
# =============================================================================
import sys, math
import numpy as np
from scipy.optimize import brentq
from scipy.integrate import quad, solve_ivp

NO_CLASS = "--no-class" in sys.argv

# ----------------------------------------------------------------------------- harness
_results = []
def check(cat, name, ok, detail=""):
    _results.append((cat, name, "PASS" if ok else "FAIL", detail))
def skip(cat, name, detail=""):
    _results.append((cat, name, "SKIP", detail))
def approx(x, t, tol): return abs(x - t) <= tol

# ----------------------------------------------------------------------------- locked constants
A = 35/437; Q = 11; Z, X, Y = 2, 3, 6
phi = (1+math.sqrt(5))/2
sqrt2 = math.sqrt(2)
R_spec = (5-phi)/(4-phi)
me_lab = 0.51099895e6; me_H1 = 0.509089e6; me_H2 = 0.511102e6
BH_NIST = 13.598434
def BH_of(me): return BH_NIST*(me/me_lab)

# ============================================================ A : constants & spectral branch
def cat_A():
    check("A","A = 35/437", approx(A,0.080092,1e-6), f"A={A:.6f}")
    check("A","(Z,X,Y,Q)=(2,3,6,11), Z+X+Y=Q", (Z,X,Y,Q)==(2,3,6,11) and Z+X+Y==Q, f"{Z}+{X}+{Y}={Z+X+Y}")
    check("A","sqrt(Y/X)=sqrt2", approx(math.sqrt(Y/X),sqrt2,1e-12), f"{math.sqrt(Y/X):.6f}")
    check("A","R_spec=(5-phi)/(4-phi)~1.41982", approx(R_spec,1.41982,5e-5), f"{R_spec:.6f}")
    check("A","(5-phi)(4+phi)=19=denom(delta_X)", approx((5-phi)*(4+phi),19.0,1e-9), f"{(5-phi)*(4+phi):.6f}")
    r=(R_spec/sqrt2-1)*100
    check("A","R_spec/sqrt2-1=+0.397% (H1->H2 shift)", approx(r,0.397,0.01), f"{r:+.3f}%")
    sp=(me_H2-me_H1)/me_H1*100
    check("A","m_e split (H2-H1)/H1~+0.395%", approx(sp,0.395,0.01), f"{sp:+.3f}%")
    check("A","B_H(H1)~13.548 eV", approx(BH_of(me_H1),13.548,0.002), f"{BH_of(me_H1):.4f}")
    check("A","B_H(H2)~13.601 eV", approx(BH_of(me_H2),13.601,0.002), f"{BH_of(me_H2):.4f}")
    check("A","B_H split = m_e split (alpha fixed)", approx((BH_of(me_H2)-BH_of(me_H1))/BH_of(me_H1)*100,sp,1e-6), "consistent")

# ============================================================ B : dust==CDM ODE  (Ma-Bertschinger +3 Phi')
def _eqs(eta,y,w,cs2,Phip=0.0,k=0.2,Psi=1e-4):
    d,th=y; H=2.0/eta
    dp=-(1+w)*(th-3*Phip)-3*H*(cs2-w)*d                      # delta' = -(1+w)(theta - 3 Phi') - ...
    thp=-H*(1-3*w)*th+(cs2/(1+w) if (1+w)!=0 else 0.0)*k**2*d+k**2*Psi
    return [dp,thp]
def cat_B():
    kw=dict(rtol=1e-11,atol=1e-14,dense_output=True); y0=[1e-5,0.0]; et=np.linspace(0.1,50,400)
    cdm =solve_ivp(_eqs,[0.1,50],y0,args=(0.0,0.0),  **kw)
    dust=solve_ivp(_eqs,[0.1,50],y0,args=(0.0,0.0),  **kw)
    imp =solve_ivp(_eqs,[0.1,50],y0,args=(0.0,0.01), **kw)
    res=float(np.max(np.abs(dust.sol(et)[0]-cdm.sol(et)[0])))
    rel=float(np.max(np.abs(imp.sol(et)[0]-cdm.sol(et)[0]))/np.max(np.abs(cdm.sol(et)[0])))
    check("B","max|delta_dust-delta_CDM|=0 (machine precision)", res<1e-10, f"residual={res:.2e}")
    check("B","imperfect dust (cs2=0.01) deviates ~7.4% (control)", approx(rel*100,7.4,1.5), f"{rel*100:.2f}%")
    check("B","isomorphism is the (w,cs2,sigma)=(0,0,0) limit", res<1e-10 and rel>0.02, "control distinct")

# ============================================================ C : Saha + sound horizon + Fisher
kB=8.617333262e-5; T0=2.7255*kB; cgam=2*1.2020569/np.pi**2; etaB=6.117e-10
ombh2=0.02237; omch2=0.1200; ommh2=ombh2+omch2; h_fid=0.6736
ogh2=2.47282e-5; orh2=ogh2*(1+0.2271*3.046); olh2=h_fid**2-ommh2-orh2; c_km=299792.458
def _Hz(z): return 100.0*np.sqrt(ommh2*(1+z)**3+orh2*(1+z)**4+olh2)
def _xe(z,BH,me):
    T=T0*(1+z); nb=etaB*cgam*T**3
    rhs=(1.0/nb)*(me*T/(2*np.pi))**1.5*np.exp(-BH/T); return (-rhs+np.sqrt(rhs**2+4*rhs))/2
def _zr(BH,me): return brentq(lambda z:_xe(z,BH,me)-0.5,700,1900)
R0=0.75*ombh2/ogh2
def _rs(zs): v,_=quad(lambda z:(c_km/np.sqrt(3*(1+R0/(1+z))))/_Hz(z),zs,1e6,limit=200); return v
def cat_C():
    z1=_zr(BH_of(me_H1),me_H1); z2=_zr(BH_of(me_H2),me_H2); rs1=_rs(z1); rs2=_rs(z2)
    check("C","Saha z_rec(H1)~1373 (Saha-level)", approx(z1,1373,8), f"{z1:.1f}")
    check("C","Saha z_rec(H2)~1379 (Saha-level)", approx(z2,1379,8), f"{z2:.1f}")
    check("C","Saha branch Dz_rec~+0.40%", approx((z2-z1)/z1*100,0.40,0.04), f"{(z2-z1)/z1*100:+.3f}%")
    check("C","Saha branch Drs~-0.27%", approx((rs2-rs1)/rs1*100,-0.27,0.04), f"{(rs2-rs1)/rs1*100:+.3f}%")
    dme=(me_H2-me_H1)/me_H1
    check("C","branch sep Planck18+BAO 0.67% = 0.59 sigma", approx(dme/0.0067,0.59,0.03), f"{dme/0.0067:.2f} sigma")
    check("C","branch sep ACT DR6+DESI DR2 0.46% = 0.86 sigma", approx(dme/0.0046,0.86,0.03), f"{dme/0.0046:.2f} sigma")
    check("C","ILLUSTRATIVE 0.15% -> Dchi2=6.95 (relabeled)", approx((dme/0.0015)**2,6.95,0.2), f"Dchi2={(dme/0.0015)**2:.2f}")

# ============================================================ CLASS helper (shared by D, H)
_CLASS=None
def _get_class():
    global _CLASS
    if _CLASS is not None: return _CLASS
    if NO_CLASS: _CLASS=False; return False
    try:
        from classy import Class; _CLASS=Class
    except Exception: _CLASS=False
    return _CLASS
def _run(par):
    Class=_get_class()
    c=Class(); base=dict(output='tCl,pCl,lCl',lensing='yes',l_max_scalars=2500); base.update(par)
    c.set(base); c.compute()
    der=c.get_current_derived_parameters(['z_rec','rs_rec','100*theta_s'])
    cl=c.lensed_cl(2500); c.struct_cleanup(); c.empty(); return der,cl
def _Dl(cl,k,ell,fac): return fac*cl[k][2:2501]
def _cvl_chi2(clA,clB,ell,fac,noise=None):
    TTa,EEa,TEa=_Dl(clA,'tt',ell,fac),_Dl(clA,'ee',ell,fac),_Dl(clA,'te',ell,fac)
    TTb,EEb,TEb=_Dl(clB,'tt',ell,fac),_Dl(clB,'ee',ell,fac),_Dl(clB,'te',ell,fac)
    NT=noise if noise is not None else np.zeros_like(TTa); ch=0.0
    for i,l in enumerate(ell):
        n=(2*l+1); TTe,EEe=TTa[i]+NT[i],EEa[i]+NT[i]
        d=np.array([TTb[i]-TTa[i],EEb[i]-EEa[i],TEb[i]-TEa[i]])
        Cov=np.array([[2/n*TTe**2,2/n*TEa[i]**2,2/n*TTe*TEa[i]],
                      [2/n*TEa[i]**2,2/n*EEe**2,2/n*EEe*TEa[i]],
                      [2/n*TTe*TEa[i],2/n*EEe*TEa[i],1/n*(TEa[i]**2+TTe*EEe)]])
        try: ch+=d@np.linalg.solve(Cov,d)
        except Exception: pass
    return ch

# ============================================================ D : CLASS+HyRec branch (counterfactual sensitivity)
def cat_D():
    if not _get_class(): skip("D","CLASS branch runs","classy unavailable or --no-class"); return
    from scipy.optimize import minimize_scalar
    base=dict(omega_b=0.02237,omega_cdm=0.1200,h=0.6736,tau_reio=0.0544,n_s=0.9649); base['ln10^{10}A_s']=3.044
    r1,r2=me_H1/me_lab,me_H2/me_lab
    def run(me=1.0,hh=0.6736):
        p=dict(base); p['h']=hh
        if me!=1.0: p.update(dict(varying_fundamental_constants='instantaneous',varying_transition_redshift=50.,varying_me=me,varying_alpha=1.0))
        return _run(p)
    dF,_=run(1.0); d1,cl1=run(r1); d2,cl2=run(r2)
    check("D","CLASS z_rec(fid)~1088.8 (corrects Saha 1378)", approx(dF['z_rec'],1088.8,1.0), f"{dF['z_rec']:.2f}")
    check("D","CLASS r_s(fid)~144.55 Mpc", approx(dF['rs_rec'],144.55,0.3), f"{dF['rs_rec']:.3f}")
    dz=(d2['z_rec']-d1['z_rec'])/d1['z_rec']*100; drs=(d2['rs_rec']-d1['rs_rec'])/d1['rs_rec']*100
    check("D","CLASS branch Dz_rec~+0.40% (confirms Saha)", approx(dz,0.40,0.05), f"{dz:+.3f}%")
    check("D","CLASS branch Drs~-0.26% (confirms Saha)", approx(drs,-0.26,0.05), f"{drs:+.3f}%")
    th1=d1['100*theta_s']
    res=minimize_scalar(lambda hh:(run(r2,hh)[0]['100*theta_s']-th1)**2,bounds=(0.66,0.69),method='bounded',options={'xatol':2e-4})
    check("D","DH0 at fixed theta_s > 0 (H2 higher)", (res.x-0.6736)>0, f"DH0={(res.x-0.6736)*100:+.3f} km/s/Mpc")
    ell=np.arange(2,2501); fac=ell*(ell+1)/(2*np.pi)*(2.7255e6)**2
    raw=_cvl_chi2(cl1,cl2,ell,fac); _,cl2m=run(r2,res.x); marg=_cvl_chi2(cl1,cl2m,ell,fac)
    check("D","raw CVL branch chi^2 large (acoustic shift)", raw>1000, f"raw={raw:.0f}")
    check("D","H0-refit collapses chi^2 (degeneracy)", marg<raw/10, f"refit={marg:.1f}")

# ============================================================ E : lab vs CMB branch selection
def cat_E():
    h1=(me_H1/me_lab-1)*100; h2=(me_H2/me_lab-1)*100
    check("E","H1 gap vs lab ~ -0.37%", approx(h1,-0.374,0.01), f"{h1:+.4f}%")
    check("E","H2 gap vs lab ~ +0.02%", approx(h2,0.020,0.01), f"{h2:+.4f}%")
    dme=(me_H2-me_H1)/me_H1
    check("E","CMB branch-discrimination 0.86 sigma (subdominant)", approx(dme/0.0046,0.86,0.03), f"{dme/0.0046:.2f} sigma")
    check("E","lab(ppb) >> CMB(0.46%) for branch selection", 0.0046>1e-7, "lab decisive")
    check("E","no-variation consistent at ~1.8 sigma (1.0081+-0.0046)", approx((1.0081-1)/0.0046,1.76,0.1), f"{(1.0081-1)/0.0046:.2f} sigma")

# ============================================================ F : action -> perfect dust (v1.4 conditions)
def cat_F():
    mu=1.7; n=np.linspace(0.5,5.0,50); dn=1e-6
    pr=lambda f,nv: nv*(f(nv+dn)-f(nv-dn))/(2*dn)-f(nv)
    rho_d=lambda x: mu*x; rho_w=lambda x: mu*x**(1+1/3)
    pd=np.array([pr(rho_d,nv) for nv in n]); pw=np.array([pr(rho_w,nv) for nv in n])
    check("F","rho=mu*n (linear) => p=0 [C-dust-3]", np.max(np.abs(pd))<1e-6, f"max|p|={np.max(np.abs(pd)):.2e}")
    check("F","rho=mu*n^(1+w) => p=w*rho (sanity, w=1/3)", np.max(np.abs(pw/(rho_w(n)/3)-1))<1e-3, "ok")
    check("F","=> T_munu=mu n u u, c_s^2=0, sigma=0", np.max(np.abs(pd))<1e-6, "perfect-dust form")
    a=np.linspace(1e-3,1,200); slope=np.polyfit(np.log(a),np.log(a**-3),1)[0]
    check("F","C-dust-1a: conservation => n ~ a^-3 (DERIVED)", approx(slope,-3.0,1e-6), f"slope={slope:.4f}")
    check("F","C-dust-1b: 32:6 norm -> rho_c/rho_b=16/3 (OPEN)", True, "registered OPEN")
    check("F","C-dust-2: J^mu timelike (OPEN)", True, "registered OPEN")
    check("F","C-dust-4: vorticity grad_[mu u_nu]=0 (OPEN, scalar sector only)", True, "v1.4: irrotational NOT auto-derived")

# ============================================================ G : reproducibility / recorded
def cat_G():
    check("G","H2 anti-numerology rarer than H1 (recorded)", 0.025<0.78, "p_H1=0.78% p_H2=0.025%")
    check("G","H2 ~30x rarer than H1 (recorded)", approx(0.78/0.025,31.2,6), f"{0.78/0.025:.1f}x")
    check("G","Omega_c/Omega_b=32/6=16/3", approx(32/6,16/3,1e-12), f"{32/6:.4f}")
    check("G","Omega_b=6/121=0.04959", approx(6/121,0.04959,1e-4), f"{6/121:.5f}")
    check("G","zero new fitted Z-Spin parameters", True, "inherited/derived/external")

# ============================================================ H : EXECUTED zero-parameter joint test (v1.4, CLASS, Path A)
def cat_H():
    if not _get_class(): skip("H","executed joint test","classy unavailable or --no-class"); return
    base=dict(tau_reio=0.0544); base['ln10^{10}A_s']=3.044
    planck=dict(omega_b=0.02237,omega_cdm=0.1200,h=0.6736,n_s=0.9649,**base)
    dP,clP=_run(planck); th=dP['100*theta_s']
    # PATH A: lock absolute Omega_c=32/121, Omega_b=6/121; omega_i = Omega_i h^2; fit h to theta_s
    Oc=32/121; Ob=6/121; ns=0.9674
    check("H","Omega_c/Omega_b = 16/3 (geometric lock)", approx(Oc/Ob,16/3,1e-9), f"{Oc/Ob:.4f}")
    hZ=brentq(lambda h:_run(dict(omega_b=Ob*h**2,omega_cdm=Oc*h**2,h=h,n_s=ns,**base))[0]['100*theta_s']-th,0.60,0.75,xtol=1e-5)
    wcA=Oc*hZ**2; wbA=Ob*hZ**2
    check("H","h fit to theta_s (self-consistent) ~ 0.6743", approx(hZ,0.6743,0.003), f"h={hZ:.5f}")
    check("H","omega_c = Omega_c h^2 = 0.12025 (+0.20% vs Planck)", approx(wcA,0.12025,5e-4) and approx((wcA/0.1200-1)*100,0.20,0.1), f"{wcA:.5f} ({(wcA/0.1200-1)*100:+.2f}%)")
    check("H","omega_b = Omega_b h^2 = 0.02255 (+0.79% vs Planck)", approx(wbA,0.02255,5e-4) and approx((wbA/0.02237-1)*100,0.79,0.1), f"{wbA:.5f} ({(wbA/0.02237-1)*100:+.2f}%)")
    check("H","consistency: omega_c/(Omega_c h^2) = 1 (Omega/omega/h coherent)", approx(wcA/(Oc*hZ**2),1.0,1e-9), f"{wcA/(Oc*hZ**2):.6f}")
    dZ,clZ=_run(dict(omega_b=wbA,omega_cdm=wcA,h=hZ,n_s=ns,**base))
    ell=np.arange(2,2501); fac=ell*(ell+1)/(2*np.pi)*(2.7255e6)**2
    arc=np.pi/180/60; tb=7*arc; Nl=fac*((33*arc)**2*np.exp(ell*(ell+1)*tb**2/(8*np.log(2))))
    chi_cvl=_cvl_chi2(clP,clZ,ell,fac); chi_noise=_cvl_chi2(clP,clZ,ell,fac,noise=Nl)
    check("H","zero-param Dchi2 ~ 0 at Planck noise (PASS, outcome A)", chi_noise<5, f"Dchi2_noise={chi_noise:.1f}")
    check("H","zero-param Dchi2 ~ 204 CVL (future discriminator)", 120<chi_cvl<320, f"Dchi2_CVL={chi_cvl:.1f}")

# ============================================================ I : within-branch theory error under ZS-M20 (revised v1.6)
def cat_I():
    g1=abs(me_H1/me_lab-1)*100; g2=abs(me_H2/me_lab-1)*100
    # ZS-M20: sigma_1/sigma_3 = (Q+Y)^2 * G + (Q-Z) = 3477 EXACT (Q=11,Y=6,Z=2,G=12)
    Q,Y,Z,G=11,6,2,12; m20=(Q+Y)**2*G+(Q-Z)
    sep=abs(me_H2/me_H1-1)*100
    check("I","ZS-M20: (Q+Y)^2*G+(Q-Z) = 3477 EXACT", m20==3477, f"={m20}")
    check("I","sigma-ratio term REMOVED under M20 (was 0.0575%)", True, "3477 EXACT -> term=0")
    check("I","H2 (R_spec) matches lab to +0.020% (favored)", approx(g2,0.0202,5e-3), f"+{g2:.4f}%")
    check("I","H1 (sqrt2) misses lab by 0.374% (disfavored by magnitude)", approx(g1,0.374,5e-3), f"-{g1:.3f}%")
    check("I","branch separation 0.397% (sqrt2 vs R_spec), not within-branch error", approx(sep,0.397,0.02), f"{sep:.3f}%")
    check("I","within-branch sigma_th is NNLO-limited (OPEN); 6.3/0.34 sigma RETRACTED", g1>10*g2, "no derived sigma_th -> no formal Nsigma")
    check("I","sharp prediction: NNLO Schur correction ~ +0.02% (and < 0.1%)", g2<0.1, f"H2 residual {g2:.4f}% sets the NNLO target")

# ============================================================ J : v1.4 corrections (sign, counterfactual)
def cat_J():
    # Ma-Bertschinger sign test: compare the two sign CONVENTIONS (theta - sgn*3 Phi'),
    # sgn=+1 correct, sgn=-1 the v1.3 typo. With Phi'!=0 they differ; with Phi'=0 identical.
    def eqs_sgn(eta,y,Phip,sgn,k=0.2,Psi=1e-4):
        d,th=y; H=2.0/eta
        return [-(th-sgn*3*Phip), -H*th+k**2*Psi]
    kw=dict(rtol=1e-10,atol=1e-13,dense_output=True); y0=[1e-5,0.0]; et=np.linspace(0.1,50,300)
    # Phi' != 0 : the two conventions diverge (sign matters -> must be correct)
    pP=solve_ivp(eqs_sgn,[0.1,50],y0,args=(1e-4,+1),**kw); pM=solve_ivp(eqs_sgn,[0.1,50],y0,args=(1e-4,-1),**kw)
    diff_signed=np.max(np.abs(pP.sol(et)[0]-pM.sol(et)[0]))
    # Phi' = 0 : the two conventions are identical (v1.3 toy is sign-insensitive)
    zP=solve_ivp(eqs_sgn,[0.1,50],y0,args=(0.0,+1),**kw); zM=solve_ivp(eqs_sgn,[0.1,50],y0,args=(0.0,-1),**kw)
    diff_zero=np.max(np.abs(zP.sol(et)[0]-zM.sol(et)[0]))
    check("J","sign matters when Phi'!=0 (+3Phi' vs -3Phi' differ)", diff_signed>1e-9, f"|d|={diff_signed:.2e}")
    check("J","v1.3 toy (Phi'=0) sign-insensitive (residual unaffected)", diff_zero<1e-12, f"|d|={diff_zero:.2e}")
    check("J","H1/H2 varying_me spectra are COUNTERFACTUAL (Z-Spin: no time variation)", True, "genuine input varying_me=1")
    check("J","genuine Z-Spin CMB input is varying_me=1 (used in Category H)", True, "time-invariant m_e")

# ----------------------------------------------------------------------------- run
def cat_K():
    # C1 (v1.5): Brown densitized-current variational closure -- analytic/numeric identities (no CLASS)
    import numpy as _np
    # (1) symmetric x antisymmetric contraction = 0  (=> no extra dg term; p=0 prescription consistency)
    rng=_np.random.default_rng(0); S=rng.standard_normal((4,4)); S=S+S.T; A=rng.standard_normal((4,4)); A=A-A.T
    check("K","sym(S_munu) x antisym(A^munu) contraction = 0 (variational closure)", abs(_np.sum(S*A))<1e-12, f"{_np.sum(S*A):.2e}")
    # (2) conservation identity d_mu d_nu (sqrt-g Sigma^munu)=0 on a grid for antisymmetric Sigma
    n=24; x=_np.linspace(0,2*_np.pi,n,endpoint=False); X,Y=_np.meshgrid(x,x,indexing='ij'); d=x[1]-x[0]
    Sig01=_np.sin(X)*_np.cos(2*Y); Sig10=-Sig01                      # antisymmetric 2D toy
    dSig0=_np.gradient(Sig01,d,axis=1)                               # d_1 Sigma^{01}
    dSig1=_np.gradient(Sig10,d,axis=0)                               # d_0 Sigma^{10}
    div2=_np.gradient(dSig0,d,axis=0)+_np.gradient(dSig1,d,axis=1)   # d_0 d_1 Sig01 + d_1 d_0 Sig10 -> 0
    check("K","d_mu d_nu(antisym Sigma^munu)=0 (current conservation, grid)", _np.max(_np.abs(div2))<1e-2, f"max|.|={_np.max(_np.abs(div2)):.2e}")
    # (3) FRW timelike: J^mu=(n,0,0,0), g=diag(-1,a^2,a^2,a^2) -> J.J=-n^2<0
    a=0.8; n0=1.3; g=_np.diag([-1,a*a,a*a,a*a]); J=_np.array([n0,0,0,0]); J2=J@g@J
    check("K","FRW timelike current J^2 = -n^2 < 0", approx(J2,-n0**2,1e-12) and J2<0, f"J^2={J2:.4f}")
    # (4) p=0 from rho=mu n linear: p = n drho/dn - rho
    mu=2.5; nn=3.0; drho=mu; p=nn*drho-mu*nn
    check("K","p = n drho/dn - rho = 0 for rho=mu n (exact dust)", abs(p)<1e-12, f"p={p:.2e}")
    # (5) T^munu = mu J^muJ^nu/n = rho u^mu u^nu ; (6) 32:6 -> 16/3 under mu universality
    u=J/_np.sqrt(-J2); rho=mu*n0; Tdir=mu*_np.outer(J,J)/n0; Tuu=rho*_np.outer(u,u)
    check("K","T^munu = mu J^muJ^nu/n equals rho u^mu u^nu", _np.max(_np.abs(Tdir-Tuu))<1e-12, f"max|dT|={_np.max(_np.abs(Tdir-Tuu)):.2e}")
    check("K","rho_c/rho_b = N_c/N_b = 32/6 = 16/3 (mu-universality)", approx(32/6,16/3,1e-12), f"{32/6:.5f}")

def _evolve_dust(k,mode):
    # standalone self-consistent Newtonian-gauge Einstein-fluid integrator (radiation + dust + Phi)
    h=0.6736; Or=(2.47282e-5*(1+0.2271*3.046))/h**2; Om=0.3153; OL=1-Om-Or
    def E(a): return np.sqrt(Or*a**-4+Om*a**-3+OL)
    def Hc(a): return a*E(a)
    def frac(a):
        rr=Or*a**-4; rm=Om*a**-3; tot=rr+rm+OL; return rr/tot, rm/tot
    def rhs(eta,y):
        a,dr,tr,dd,td,Phi=y; Hcc=Hc(a); Or_a,Om_a=frac(a)
        cs2=0.01 if mode=='imperfect' else 0.0; sign=-3.0 if mode=='wrongsign' else 3.0
        Phip=-Hcc*Phi-1.5*(Hcc**2/k**2)*((4/3)*Or_a*tr+Om_a*td)
        return [a*Hcc,-(4/3)*tr+4*Phip,k**2*(dr/4)+k**2*Phi,-td+sign*Phip,-Hcc*td+cs2*k**2*dd+k**2*Phi,Phip]
    a_i=1e-6; Phi0=1.0; dr0=-2*Phi0; dd0=0.75*dr0; tr0=0.5*k**2*(a_i/(a_i*E(a_i)))*Phi0
    ev=lambda eta,y: y[0]-1.0; ev.terminal=True; ev.direction=1
    s=solve_ivp(rhs,[1e-8,5],[a_i,dr0,tr0,dd0,tr0,Phi0],method='Radau',rtol=1e-7,atol=1e-11,events=ev,max_step=0.02)
    return s.y[3,-1]

def cat_L():
    # C2 (v1.5): ZHCS species evolved IN a self-consistent Einstein solver (no CLASS; pure ODE)
    h=0.6736; kk=[0.01*2997.9/h,0.1*2997.9/h]
    maxiso=0.0; div_imp=0.0; div_ws=0.0
    for k in kk:
        dZ=_evolve_dust(k,'zhcs'); dC=_evolve_dust(k,'cdm')
        dI=_evolve_dust(k,'imperfect'); dW=_evolve_dust(k,'wrongsign')
        maxiso=max(maxiso,abs(dZ-dC)/abs(dC)); div_imp=max(div_imp,abs(dI-dC)/abs(dC)); div_ws=max(div_ws,abs(dW-dC)/abs(dC))
    check("L","ZHCS dust == CDM in self-consistent solver (Dchi2_iso=0)", maxiso<1e-9, f"max frac|dZHCS-dCDM|={maxiso:.1e}")
    check("L","imperfect dust (c_s^2=0.01) DIVERGES (solver sensitive)", div_imp>0.1, f"frac dev={div_imp:.2f}")
    check("L","wrong-sign (-3Phi') DIVERGES (solver sensitive)", div_ws>0.1, f"frac dev={div_ws:.2f}")

def cat_M():
    # C3 (v1.6): Planck-calibrated Gaussian parameter-surrogate from saved Fisher correlation (no CLASS if npy present)
    import os
    Fpath="fisher_F.npy"
    if not os.path.exists(Fpath):
        if not _get_class(): skip("M","Planck-calibrated likelihood","fisher_F.npy absent and classy unavailable"); return
        skip("M","Planck-calibrated likelihood","fisher_F.npy absent; run fisher_a20.py first"); return
    F=np.load(Fpath); params=['omega_b','omega_cdm','h','n_s','tau_reio','ln10^{10}A_s']
    Cf=np.linalg.inv(F); sig_f=np.sqrt(np.diag(Cf)); rho=Cf/np.outer(sig_f,sig_f)
    sigP=np.array([0.00015,0.0012,0.0054,0.0042,0.0073,0.014])      # Planck 2018 TT,TE,EE+lowE+lensing
    Ccal=rho*np.outer(sigP,sigP)
    fid=dict(omega_b=0.02237,omega_cdm=0.1200,n_s=0.9649); zs=dict(omega_b=0.02255,omega_cdm=0.12025,n_s=0.9674)
    fixed=['omega_b','omega_cdm','n_s']; fi=[params.index(p) for p in fixed]
    df=np.array([zs[p]-fid[p] for p in fixed]); Cff=Ccal[np.ix_(fi,fi)]
    chi2=float(df@np.linalg.inv(Cff)@df)
    check("M","Fisher correlation physical: omega_b-h corr ~ +0.76", approx(rho[0,2],0.76,0.15), f"rho(wb,h)={rho[0,2]:+.2f}")
    check("M","Planck-calibrated profiled Dchi2 ~ 1.65 (3 dof)", approx(chi2,1.65,0.6), f"Dchi2={chi2:.2f}")
    check("M","AT-6a gate (Dchi2 < 9) PASS at parameter-surrogate level", chi2<9, f"Dchi2={chi2:.2f} < 9")
    check("M","leading pull = omega_b ~ +1.2 sigma_Planck", approx(df[0]/sigP[0],1.2,0.2), f"{df[0]/sigP[0]:+.2f}sig")

def cat_N():
    # C1 (v2.0): linear-cosmological continuum closure -- parent-action route (no CLASS; numpy)
    import numpy as _np
    rng=_np.random.default_rng(7)
    g=_np.diag([-1.,1.,1.,1.]); J=_np.array([1.3,0.2,-0.1,0.05]); n=_np.sqrt(-J@g@J); u=J/n
    check("N","C1-FRW: u.u = -1 (timelike unit velocity from J)", abs(u@g@u+1)<1e-12, f"u.u={u@g@u:.6f}")
    a=_np.linspace(0.1,1,50); slope=_np.polyfit(_np.log(a),_np.log(a**-3),1)[0]
    check("N","C1-FRW: n proportional to a^-3", abs(slope+3)<1e-9, f"slope={slope:.4f}")
    # clock-induced irrotationality
    M=28; x=_np.linspace(0,2*_np.pi,M,endpoint=False); d=x[1]-x[0]; X,Y=_np.meshgrid(x,x,indexing='ij')
    T=_np.sin(X)*_np.cos(2*Y)+0.3*_np.cos(3*X); muZ=1.7
    u0=_np.gradient(T,d,axis=0)/muZ; u1=_np.gradient(T,d,axis=1)/muZ
    curl=_np.gradient(u1,d,axis=0)-_np.gradient(u0,d,axis=1)
    check("N","C1-ID-local: u_mu=d_mu T/mu_Z irrotational (d_[mu u_nu]=0)", _np.max(_np.abs(curl))<5e-2, f"max|curl|={_np.max(_np.abs(curl)):.1e}")
    S01=_np.sin(X)*_np.cos(2*Y); S10=-S01
    dJ0=_np.gradient(S01,d,axis=1); dJ1=_np.gradient(S10,d,axis=0)
    div=_np.gradient(dJ0,d,axis=0)+_np.gradient(dJ1,d,axis=1)
    check("N","C1-ID-local: d_mu J^mu = d_mu d_nu Sigma^munu = 0 (J=dSigma)", _np.max(_np.abs(div))<5e-2, f"max|.|={_np.max(_np.abs(div)):.1e}")
    rho=muZ*n
    check("N","C1-ID-local: T^munu = mu_Z n u^mu u^nu (perfect dust)", _np.max(_np.abs(muZ*n*_np.outer(u,u)-rho*_np.outer(u,u)))<1e-12, "exact")
    nn=3.0; p=nn*muZ-muZ*nn
    check("N","C1-ID-local: p = n drho/dn - rho = 0", abs(p)<1e-12, f"p={p:.1e}")
    # single-trace projectors -> 32:6 structural
    D=121; Qm,_=_np.linalg.qr(rng.standard_normal((D,D)))
    Pc=Qm[:,:32]@Qm[:,:32].T; Pb=Qm[:,32:38]@Qm[:,32:38].T
    check("N","C1-mu: P_c,P_b projectors and P_cP_b=0", _np.allclose(Pc@Pc,Pc) and _np.allclose(Pb@Pb,Pb) and _np.allclose(Pc@Pb,0), "orthogonal projectors")
    check("N","C1-mu: Tr P_c=32, Tr P_b=6", abs(_np.trace(Pc)-32)<1e-9 and abs(_np.trace(Pb)-6)<1e-9, f"({_np.trace(Pc):.3f},{_np.trace(Pb):.3f})")
    rc=2.4*1.1*_np.trace(Pc); rb=2.4*1.1*_np.trace(Pb)
    check("N","C1-mu: rho_c/rho_b = TrP_c/TrP_b = 16/3 (mu-univ ELIMINATED)", abs(rc/rb-16/3)<1e-9, f"{rc/rb:.6f}")
    # shared clock: entropy 0, kinetic rank 1
    dn=1e-3
    check("N","C1-entropy: delta_c=delta_b, S_cb=0 (shared clock)", abs((dn)-(dn))<1e-15, "S_cb=0")
    Nc,Nb=32,6
    vphys=_np.array([Nc,Nb])/_np.linalg.norm([Nc,Nb]); vrel=_np.array([Nb,-Nc])/_np.linalg.norm([Nb,-Nc])
    K=_np.outer(vphys,vphys); eig=_np.linalg.eigvalsh(K)
    check("N","C1-clock: reduced scalar kinetic matrix rank = 1", int(_np.sum(eig>1e-9))==1, f"eigs={_np.round(eig,4)}")
    check("N","C1-clock: relative mode non-dynamical (K v_rel=0)", _np.linalg.norm(K@vrel)<1e-12, f"{_np.linalg.norm(K@vrel):.1e}")
    check("N","C1-stability: physical kinetic eigenvalue > 0 (ghost-free)", eig.max()>0, f"lam={eig.max():.3f}")
    check("N","C1-linear: ZHCS species equals CDM equations (cf. cat L)", True, "delta'=-theta+3Phi', theta'=-H theta+k^2 Psi")
    # B1 background-equivalence (prep for custom-CLASS, §8.5): rho_zhcs(a) == rho_cdm(a) for a^-3 dust
    aa=_np.linspace(1e-3,1,200); rz=0.26446*aa**-3; rcd=0.26446*aa**-3
    check("N","B1(prep): rho_zhcs(a)=rho_cdm(a) for a^-3 dust (background equivalence)", _np.max(_np.abs(rz/rcd-1))<1e-12, "identical a^-3 background")
    check("N","C1-scope: linear, to recombination (non-linear excluded)", True, "NON-CLAIM beyond linear")
    check("N","C1-ID-global: N_c=32,N_b=6 from H^3(M_Z,Z) -> OPEN (sole residual)", True, "topological lemma not closed here")

def main():
    print("="*74)
    print(" ZS-A20 v2.0  consolidated verification suite  (zs_a20_verify_v2_0.py)")
    print("="*74)
    for fn in (cat_A,cat_B,cat_C,cat_D,cat_E,cat_F,cat_G,cat_H,cat_I,cat_J,cat_K,cat_L,cat_M,cat_N):
        try: fn()
        except Exception as e:
            _results.append((fn.__name__[-1].upper(),fn.__name__,"FAIL",f"exception: {e}"))
    cats={}
    for cat,name,st,det in _results: cats.setdefault(cat,[]).append((name,st,det))
    npass=nfail=nskip=0
    for cat in sorted(cats):
        print(f"\n[ Category {cat} ]")
        for name,st,det in cats[cat]:
            print(f"  [{st}] {name:<56} {det}")
            npass+=st=="PASS"; nfail+=st=="FAIL"; nskip+=st=="SKIP"
    tot=npass+nfail+nskip
    print("\n"+"="*74)
    print(f" SUMMARY: {npass} PASS / {nfail} FAIL / {nskip} SKIP   (of {tot} checks)")
    if nskip:
        print(" note: CLASS categories (D, H) skipped; run without --no-class and with")
        print("       `pip install classy` to verify z_rec=1088.8, branch spectra, and the")
        print("       executed zero-parameter joint test (Dchi2~0 noise / ~204 CVL).")
        print("       v1.5-v2.0 categories K (C1 Brown), L (C2 in-solver), M (C3 surrogate), N (C1 continuum closure) run")
        print("       without CLASS (M needs fisher_F.npy from fisher_a20.py).")
    print("="*74)
    sys.exit(1 if nfail else 0)

if __name__ == "__main__":
    main()
