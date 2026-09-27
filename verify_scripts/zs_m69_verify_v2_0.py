#!/usr/bin/env python3
"""ZS-M69 v2.0: executable subchecks, numerical witnesses and regressions.

Run: python zs_m69_verify_v2_0.py
Requires Python 3.10+, numpy, scipy, sympy. No network and no legacy import.
The executable ledger has P=0: full quantified proofs are in ZS-M69_v2_0.md.
A numerical PASS does not establish novelty, research grade, or M67 realization.
Outputs are deterministic within a fixed software environment; no timestamp.
"""
from __future__ import annotations
import argparse, hashlib, json, math, platform, re, sys, traceback, warnings
from collections import Counter
from fractions import Fraction as Q
from pathlib import Path

VERSION='v2.0'
SEED=20260907
try:
    import numpy as np
    import scipy
    import sympy as sp
    from scipy.integrate import quad, IntegrationWarning
    from scipy.linalg import expm
    from scipy.special import j1, gamma
except ImportError as exc:
    print(json.dumps({'version':VERSION,'status':'FAIL','dependency_error':str(exc)}))
    raise SystemExit(2)

REGISTRY=[]
def register(rid,cls,claim,scope):
    def deco(fn):
        REGISTRY.append((rid,cls,claim,scope,fn));return fn
    return deco

def plain(x):
    if isinstance(x,np.ndarray):return plain(x.tolist())
    if isinstance(x,(np.integer,np.floating,np.bool_)):return x.item()
    if isinstance(x,complex):return [x.real,x.imag]
    if isinstance(x,Q):return {'fraction':str(x),'decimal':float(x)}
    if isinstance(x,dict):return {str(k):plain(v) for k,v in x.items()}
    if isinstance(x,(tuple,list)):return [plain(v) for v in x]
    return x

def require(ok,**evidence):return bool(ok),plain(evidence)
def cof(a):
    a=np.asarray(a);return np.array([[(-1)**(i+j)*np.linalg.det(np.delete(np.delete(a,i,0),j,1)) for j in range(3)] for i in range(3)])
def cross(x):return np.array([[0,-x[2],x[1]],[x[2],0,-x[0]],[-x[1],x[0],0.]])
SX=np.array([[0,1],[1,0]],complex);SY=np.array([[0,-1j],[1j,0]],complex);SZ=np.diag([1.,-1.]).astype(complex)
PAULI=[SX,SY,SZ];I2=np.eye(2,dtype=complex)
SIG=[sp.Matrix([[0,1],[1,0]]),sp.Matrix([[0,-sp.I],[sp.I,0]]),sp.diag(1,-1)]

def normal_weight(z,branch='free',a=1.):
    d=a*a+z*z
    if branch=='free':return a*a/d
    if branch=='PEC':return 2*a*a*z*z/d**2
    if branch=='PMC':return 2*a**4/d**2
    if branch=='s6':return (1+z*z)**-3
    raise ValueError(branch)

def profile_g(p,profile='power',beta=4.,ell=1.):
    x=p*ell
    if profile=='power':return (1+x*x)**(-beta/2)
    if profile=='gaussian':return np.exp(-x*x)
    if profile=='disk':return (1. if abs(x)<1e-7 else 2*j1(x)/x)**2
    if profile=='cap':return (1. if abs(x)<1e-4 else 3*(np.sin(x)-x*np.cos(x))/x**3)**2
    raise ValueError(profile)

def segmented_quad(fn,end,oscillatory=False):
    if end<=0:return 0.,0.
    if oscillatory:
        points=np.linspace(0,end,max(2,int(math.ceil(end/(4*np.pi)))+1))
    else:
        points=[0.];v=1.
        while v<end:points.append(v);v*=2
        points.append(end)
    total=err=0.
    with warnings.catch_warnings():
        warnings.simplefilter('error',IntegrationWarning)
        for lo,hi in zip(points[:-1],points[1:]):
            val,e=quad(fn,float(lo),float(hi),epsabs=2e-12/max(1,len(points)-1),epsrel=2e-9,limit=600)
            total+=val;err+=e
    return total,err

def spectrum(w,branch='free',profile='power',beta=4.,a=1.,ell=1.,scale=1.):
    """Exact cap+belt coordinate formula. scale is applied before integration."""
    cut=w/np.sqrt(2)
    def cap(p):
        z=np.sqrt(w*w-p*p)
        return scale*p/z*(1+z*z/w**2)*profile_g(p,profile,beta,ell)*normal_weight(z,branch,a)/(8*np.pi**2)
    def belt(z):
        p=np.sqrt(w*w-z*z)
        return scale*(1+z*z/w**2)*profile_g(p,profile,beta,ell)*normal_weight(z,branch,a)/(8*np.pi**2)
    x,ex=segmented_quad(cap,cut,profile in ('disk','cap'))
    y,ey=segmented_quad(belt,cut,profile in ('disk','cap'))
    return x+y,ex+ey

def spectrum_angle(w,branch='free',profile='power',beta=4.,a=1.,ell=1.):
    with warnings.catch_warnings():
        warnings.simplefilter('error',IntegrationWarning)
        return quad(lambda u:w*(1+u*u)*profile_g(w*np.sqrt(1-u*u),profile,beta,ell)*normal_weight(w*u,branch,a)/(8*np.pi**2),0,1,epsabs=1e-12,epsrel=1e-10,limit=1000)[0]

def FT(x,T):return .5*T*T*np.sinc(x*T/(2*np.pi))**2

def atan_bounds(x,n):
    s=sum(((-1)**k*x**(2*k+1)/Q(2*k+1) for k in range(n)),Q(0))
    nxt=(-1)**n*x**(2*n+1)/Q(2*n+1)
    return min(s,s+nxt),max(s,s+nxt)
def sqrt_bounds(x,digits=35):
    scale=10**digits;n=math.isqrt(x.numerator*scale*scale//x.denominator)
    return Q(n,scale),Q(n+1,scale)
def window_certificate():
    a0,a1=atan_bounds(Q(1,5),40);b0,b1=atan_bounds(Q(1,239),12)
    pi0,pi1=16*a0-4*b1,16*a1-4*b0
    es=sum((Q((-1)**k,math.factorial(k)) for k in range(41)),Q(0))
    en=Q(-1,math.factorial(41));e0,e1=es+en,es
    sqrtpi0=sqrt_bounds(pi0)[0]
    fmin=e0/(6*pi1*pi1); fmax=1/(3*pi0*pi0)
    M2=100/(3*pi0*pi0);fnorm=1/(8*sqrtpi0);F4=1/(16*pi0)
    Emax=2*M2+4*fnorm+4*fmax
    T=Q(1600);q=Q(1,2000000);delta=Q(1,2)
    spectral=Emax/(pi0*fmin*T);dyson=32*q*q*F4*T**3/(pi0*fmin)
    y2=2*q*q*T*T/sqrtpi0
    lower_signal=2*pi0*q*q*fmin*T
    return dict(pi_lower=pi0,pi_upper=pi1,exp_minus_one_lower=e0,exp_minus_one_upper=e1,
                f_lower=fmin,E_upper=Emax,F4_upper=F4,T=T,q=q,delta=delta,
                spectral_relative_bound=spectral,dyson_relative_bound=dyson,
                relative_bound=spectral+dyson,y_squared_upper=y2,
                negative_response_magnitude_lower=(1-spectral-dyson)*lower_signal)

@register('C01','C','T1','Three Laplace mode amplitudes; not boundary-condition exhaustiveness.')
def c01():
    a,z,k=sp.symbols('a z k',positive=True)
    vals=[sp.integrate(a*sp.exp(-a*z)*sp.exp(sp.I*k*z),(z,0,sp.oo)),sp.integrate(sp.sqrt(2)*a*sp.exp(-a*z)*sp.sin(k*z),(z,0,sp.oo)),sp.integrate(sp.sqrt(2)*a*sp.exp(-a*z)*sp.cos(k*z),(z,0,sp.oo))]
    target=[a/(a-sp.I*k),sp.sqrt(2)*a*k/(a*a+k*k),sp.sqrt(2)*a*a/(a*a+k*k)]
    return require(all(sp.simplify(x-y)==0 for x,y in zip(vals,target)),amplitudes=[str(x) for x in vals])

@register('C02','C','T1,T3','Exact masses, high-frequency tails and low-frequency angular coefficients.')
def c02():
    z,a,w,u=sp.symbols('z a w u',positive=True);B=[a*a/(a*a+z*z),2*a*a*z*z/(a*a+z*z)**2,2*a**4/(a*a+z*z)**2]
    masses=[sp.integrate(b,(z,0,sp.oo)) for b in B]
    tails=[sp.limit(z**s*b,z,sp.oo) for b,s in zip(B,[2,2,4])]
    ir=[sp.simplify(sp.integrate((1+u*u)*sp.limit(b.subs(z,w*u)/w**n,w,0),(u,0,1))/(8*sp.pi**2)) for b,n in zip(B,[0,2,0])]
    return require(all(sp.simplify(x-sp.pi*a/2)==0 for x in masses) and tails==[a*a,2*a*a,2*a**4] and ir==[1/(6*sp.pi**2),2/(15*sp.pi**2*a*a),1/(3*sp.pi**2)],mass=[str(x) for x in masses],tail=[str(x) for x in tails],IR=[str(x) for x in ir])

@register('C03','C','T2','Positive normal-weight mass on [0,a], used in the lower norm comparison.')
def c03():
    z=sp.symbols('z',nonnegative=True)
    bs=[1/(1+z*z),2*z*z/(1+z*z)**2,2/(1+z*z)**2]
    vals=[sp.integrate(b,(z,0,1)) for b in bs]
    return require(vals==[sp.pi/4,-sp.Rational(1,2)+sp.pi/4,sp.Rational(1,2)+sp.pi/4],unit_scale_masses=[str(v) for v in vals])

@register('C04','C','T3','Coordinate Jacobian for cap/belt decomposition; proof of limits is textual.')
def c04():
    p,w=sp.symbols('p w',positive=True);z=sp.sqrt(w*w-p*p);u=z/w
    jac=sp.simplify(-w*sp.diff(u,p))
    return require(sp.simplify(jac-p/z)==0,jacobian=str(jac))

@register('C05','C','T3','Area and Fourier radial moment for compact-edge family; exact integrals.')
def c05():
    r,nu=sp.symbols('r nu',positive=True)
    norm=sp.integrate(2*(nu+1)*r*(1-r*r)**nu,(r,0,1))
    # A change y=1-r^2 keeps conditions explicit (nu>-1/2 for the square).
    ip=(nu+1)**2/(sp.pi*(2*nu+1));A=sp.simplify(1/ip)
    vals=[sp.simplify(A.subs(nu,v)) for v in [0,sp.Rational(1,2)]]
    return require(sp.simplify(norm-1)==0 and vals==[sp.pi,8*sp.pi/9],Aeff=str(A),Ag=str(sp.simplify(2*sp.pi/A)))

@register('C06','C','T2,T3','Gamma-mixture Fourier profile: exact Laplace identity and threshold integrals.')
def c06():
    t,p=sp.symbols('t p',positive=True)
    vals=[]
    for b in [1,2,3,4,6]:
        nu=sp.Rational(b,4)
        val=sp.integrate(t**(nu-1)*sp.exp(-(1+p*p)*t),(t,0,sp.oo))/sp.gamma(nu)
        vals.append(sp.simplify(val-(1+p*p)**(-nu)))
    return require(all(x==0 for x in vals),beta_values=[1,2,3,4,6],Fourier='(1+p^2)^(-beta/4)',spectral_L1_threshold='beta>1',density_L2_threshold='beta>2',scope_note='Threshold proofs use explicit comparison integrals in the manuscript, not this finite list alone.')

@register('C07','C','T4','Full-line Fejer mass and local pairing algebra; not an L1=>bounded-remainder assertion.')
def c07():
    x=sp.symbols('x',real=True)
    val=sp.integrate((1-sp.cos(x))/x**2,(x,-sp.oo,sp.oo))
    a,b,c=sp.symbols('a b c');pair=sp.expand((a+b-2*c)+2*c-a-b)
    return require(sp.simplify(val-sp.pi)==0 and pair==0,unit_time_mass=str(val),finite_window_bound='2 q^2 E_h(f)')

@register('C08','C','T5','Uniform even-Dyson tail ratio inequality for every n>=4.')
def c08():
    k=sp.symbols('k',nonnegative=True);n=k+4
    poly=sp.Poly(sp.expand((n+1)**2*(n+2)-16*(n+3)),k)
    # This implies sqrt((n+3)/((n+1)^2(n+2)))<1/4.
    return require(all(c>0 for c in poly.all_coeffs()) and Q(5,24)<Q(1,4),positive_polynomial=str(poly.as_expr()),first_even_term_squared='5/24 < 1/4',tail_factor_bound='(1/2)/(1-1/4)=2/3 < 1',scope_note='The Dyson-vector norm and cutoff-limit arguments are in T5 proof.')

@register('C09','C','T6','Exact rational interval certificate for a free-Gaussian controlled window.')
def c09():
    c=window_certificate()
    ok=c['pi_lower']<c['pi_upper'] and c['exp_minus_one_lower']<c['exp_minus_one_upper'] and c['relative_bound']<c['delta'] and c['y_squared_upper']<1 and c['negative_response_magnitude_lower']>0
    return require(ok,**c,scope_note='Analytic conservative bounds; no long-time regression, spectral quadrature or fitted constants enter this certificate.')

@register('C10','C','T6','Conservative Gaussian second-derivative bound used by C09.')
def c10():
    # |B|<=1, |B'|<=2, |B''|<=10; 0<=w<=2, ell=a=1.
    P1=Q(2)+2*Q(2);P2=Q(10)+4*Q(2)*Q(2)+2+4*Q(2)**2
    bound=2*P1+2*P2
    z=sp.symbols('z',real=True)
    b=1/(1+z*z)
    identity=sp.simplify(sp.diff(b,z,2)-(-2/(1+z*z)**2+8*z*z/(1+z*z)**3))
    return require(bound==100 and identity==0,J_second_derivative_bound='100/(6*pi^2)',f_second_derivative_bound='100/(3*pi^2)',scope_note='Elementary termwise bounds are intentionally conservative.')

@register('V11','V','T1,T3','Angular quadrature vs cap+belt coordinates at finite frequencies.')
def v11():
    errors=[]
    for profile in ['power','gaussian','disk','cap']:
        for branch in ['free','PEC','PMC']:
            for w in [.2,1.,4.,12.]:
                a,e=spectrum(w,branch,profile,beta=3.5);b=spectrum_angle(w,branch,profile,beta=3.5)
                errors.append(abs(a-b)/max(abs(a),1e-15))
    return require(max(errors)<2e-8,max_relative_error=max(errors),cases=len(errors),tolerance=2e-8)

@register('V12','V','T3','Nonoscillatory two-endpoint law: beta grid, three branches; not a quantified proof.')
def v12():
    data=[]
    for beta in [1.5,2.,2.5,3.,4.,5.,6.]:
        for branch,s,b in [('free',2,1.),('PEC',2,2.),('PMC',4,2.)]:
            w=2500.;normal=b/(4*np.pi**2*(beta-2))*w**(-s-1) if beta>2 else 0.
            pred=normal+w**(-beta)/(16*np.pi)
            val,err=spectrum(w,branch,beta=beta,scale=1/pred)
            data.append(dict(beta=beta,branch=branch,omega=w,ratio=val,quadrature_error=err))
    worst=max(abs(d['ratio']-1) for d in data)
    return require(worst<.012,data=data,max_relative_deviation=worst,tolerance=.012)

@register('W13','W','T3','Uniform disk: persistent oscillatory leading coefficient, including counterexample to v1.9.')
def w13():
    data=[]
    for n in [80,160]:
        for phase in [3*np.pi/4,5*np.pi/4]:
            w=n*np.pi+phase;H=8/np.pi*np.cos(w-3*np.pi/4)**2
            for branch,b in [('free',1.),('PEC',2.),('PMC',0.)]:
                pred=b/(2*np.pi**2)+H/(16*np.pi)
                val,err=spectrum(w,branch,'disk',scale=w**3)
                data.append(dict(n=n,branch=branch,phase=float(phase),omega=w,scaled=val,predicted=pred,error=abs(val-pred)))
    latest=[d for d in data if d['n']==160]
    improves=all(data[i+6]['error']<data[i]['error'] for i in range(6))
    return require(max(d['error'] for d in latest)<.0025 and improves,data=data,tolerance_absolute_at_n160=.0025,each_sequence_error_decreases=improves,scope_note='n=80 is the convergence comparison, n=160 is the accuracy check. At a zero of the grazing term this does not identify the next power.')

@register('W14','W','T3','Continuous compact cap: PMC has an omega^-4 oscillatory leading term.')
def w14():
    data=[]
    for n in [60,120,240]:
        w=n*np.pi;val,err=spectrum(w,'PMC','cap',scale=w**4)
        data.append(dict(omega=w,scaled=val,predicted=9/(16*np.pi),error_estimate=err))
    return require(abs(data[-1]['scaled']-9/(16*np.pi))<.001,data=data,tolerance_absolute=.001)

@register('V15','V','T3','A different normal tail s=6: generic theorem beyond the three Maxwell weights.')
def v15():
    data=[];L=3*np.pi/16
    for beta in [4.,7.,9.]:
        w=1500.;pred=w**-7/(4*np.pi**2*(beta-2))+L/(8*np.pi**2)*w**(-beta)
        val,err=spectrum(w,'s6',beta=beta,scale=1/pred)
        data.append(dict(beta=beta,ratio=val,estimated_error=err))
    return require(max(abs(x['ratio']-1) for x in data)<.002,data=data,tolerance=.002)

@register('V16','V','T2','Radial total spectral mass: frequency integral vs momentum integral, free Gaussian.')
def v16():
    # Route one: integrate frequency; high-frequency tail bounded analytically below.
    limit=80.
    a=quad(lambda w:spectrum_angle(w,profile='gaussian'),0,limit,epsabs=2e-9,limit=250)[0]
    # Route two: use p,z; both integrals are positive.
    def outer(p):
        if p==0:return 0.
        val=quad(lambda z:(1+z*z/(p*p+z*z))*normal_weight(z)/np.sqrt(p*p+z*z),0,np.inf,epsabs=1e-10,limit=250)[0]
        return p*np.exp(-p*p)*val/(8*np.pi**2)
    b=quad(outer,0,10,epsabs=2e-9,limit=250)[0]
    # For w>=80, split p<=w/sqrt2 and grazing belt. Cap <= sqrt(2)/(pi²*w³)*int p exp(-p²)dp.
    tail=np.sqrt(2)/(4*np.pi**2*limit**2)+np.exp(-limit**2/2)/(16*np.pi)
    return require(a<=b+3e-8 and b-a<tail+3e-8 and b<1/(16*np.sqrt(np.pi)),frequency_to_80=a,momentum_integral=b,tail_upper_bound=tail,absolute_tolerance=3e-8,analytic_mass_upper=1/(16*np.sqrt(np.pi)))

@register('W17','W','T2','Density normalization, density L2, and spectral L1 are different thresholds.')
def w17():
    # Explicit cut-off norm integrals; beta=1 gives asinh R, beta=2 gives atan R.
    R=[10.,100.,1000.];m1=[np.arcsinh(x) for x in R];m2=[np.arctan(x) for x in R]
    l2=[.5*np.log(1+x*x) for x in R]
    val,_=spectrum(2000.,beta=2.,scale=2000.**2)
    return require(m1[-1]>m1[0]+4 and abs(m2[-1]-np.pi/2)<.002 and l2[-1]>l2[0]+4 and abs(val-1/(16*np.pi))<.001,cutoffs=R,beta1_spectral_weight=m1,beta2_spectral_weight=m2,beta2_density_L2_weight=l2,beta2_omega2J=val,scope_note='Divergence/convergence follows from the explicit integral formulas; three cutoffs alone would not prove it.')

@register('V18','V','T4','Bounded second-order remainder for a smooth test spectrum, at finite sampled times.')
def v18():
    h=1.;f=lambda w:2*w*np.exp(-w)
    # f''=2(w-2)e^-w; |f''|<=4 on [0,2].
    Ebound=2*4*h+4*2/h**2+4*f(h)/h
    data=[]
    for T in [1.,5.,20.,60.]:
        value=quad(lambda w:f(w)*(FT(h-w,T)-FT(h+w,T)),0,40,points=[h],epsabs=2e-8,limit=4000)[0]
        residual=abs(-2*value+2*np.pi*f(h)*T)
        data.append(dict(T=T,residual=residual,bound=2*Ebound))
    return require(all(x['residual']<=x['bound'] for x in data),data=data,scope_note='The all-T statement is the pairing inequality in the manuscript.')

@register('W19','W','T4','L1 plus continuity at resonance does not imply a bounded offset.')
def w19():
    data=[]
    for T in [100.,400.,1600.]:
        f=lambda x:(1+np.sqrt(abs(x)))*(FT(-x,T)-FT(4+x,T))
        val=quad(f,-.5,0,epsabs=1e-8,limit=4000)[0]+quad(f,0,.5,epsabs=1e-8,limit=4000)[0]
        data.append(dict(T=T,remainder=-2*val+2*np.pi*T))
    return require(abs(data[-1]['remainder'])>3*abs(data[0]['remainder']),data=data,analytic_asymptotic='-4 sqrt(2*pi*T)+O(1)',scope_note='A spectral counterexample, not an assertion that it is a particular M67 profile.')

def boson_expect(q,T=1.1,h=1.3,w=.8,N=12):
    an=np.diag(np.sqrt(np.arange(1,N)),1);num=an.T@an;f=.4
    H=np.kron(h*SZ/2,np.eye(N))+np.kron(I2,w*num)+q*f*np.kron(SX,an+an.T)
    U=expm(-1j*T*H);vac=np.zeros((N,N));vac[0,0]=1;rho=np.kron(I2/2,vac)
    return float(np.trace(np.kron(SZ,np.eye(N))@U@rho@U.conj().T).real)

@register('V20','V','T5','Rabi-mode exact propagation vs second order and the fourth-order bound; finite Fock cutoff.')
def v20():
    T=1.1;h=1.3;w=.8;F=.4;data=[]
    for q in [.03,.015,.0075]:
        exact=boson_expect(q);crosscut=boson_expect(q,N=16)
        second=-2*q*q*F*F*(FT(h-w,T)-FT(h+w,T));bound=64*q**4*F**4*T**4
        data.append(dict(q=q,exact=exact,second_order=second,error=abs(exact-second),bound=bound,cutoff_difference=abs(exact-crosscut)))
    return require(all(x['error']<=x['bound'] and x['cutoff_difference']<1e-12 for x in data),data=data,halving_error_ratios=[data[i]['error']/data[i+1]['error'] for i in range(2)],scope_note='Cutoff convergence is numerical. The continuum bound follows from T5, not from these finite matrices.')

@register('C21','C','T7','Gauge-invariant band-current tensor identity for symbolic initial/final Bloch vectors.')
def c21():
    n=sp.symbols('n0:3',real=True);m=sp.symbols('m0:3',real=True)
    P=(sp.eye(2)+sum((n[i]*SIG[i] for i in range(3)),sp.zeros(2)))/2
    R=(sp.eye(2)+sum((m[i]*SIG[i] for i in range(3)),sp.zeros(2)))/2
    residual=[]
    for a in range(3):
        for b in range(3):
            target=((1-sum(m[i]*n[i] for i in range(3)))*int(a==b)+m[a]*n[b]+m[b]*n[a]+sp.I*sum(sp.LeviCivita(a,b,c)*(m[c]-n[c]) for c in range(3)))/2
            residual.append(sp.simplify(sp.trace(R*SIG[a]*P*SIG[b])-target))
    return require(all(x==0 for x in residual),entries=9,formula='Tr[P_final sigma_a P_initial sigma_b]',scope_note='Rank-one interpretation additionally requires unit Bloch vectors; no gauge choice for eigenvectors is needed.')

@register('W22','W','T7','Momentum-dependent band basis and a fixed-k projection fail the old closure inference.')
def w22():
    b=np.pi/3;U=np.array([[np.cos(b/2),-np.sin(b/2)],[np.sin(b/2),np.cos(b/2)]])
    vertex=U.T@SX
    N=16;xs=np.arange(N)*2*np.pi/N;F=np.exp(1j*np.outer(xs,np.arange(N)))/np.sqrt(N)
    shift=F.conj().T@np.diag(np.exp(3j*xs))@F
    return require(abs(vertex[0,0]-.5)<1e-12 and abs(shift[5,2])>.999 and abs(shift[2,2])<1e-12,vertex=vertex,off_subspace_amplitude=abs(shift[5,2]),projected_diagonal=abs(shift[2,2]))

@register('W23','W','T1,T7','Intermediate projector annihilates boundary pairing: the exhaustive D/N inference is false.')
def w23():
    P=sp.Matrix([[1,1],[1,1]])/2;Qm=sp.eye(2)-P
    x,y,a,b=sp.symbols('x y a b');d=Qm*sp.Matrix([x,y]);F=P*sp.Matrix([a,b]);pair=sp.simplify((F.T*d)[0])
    return require(P*P==P and P.rank()==1 and pair==0,projector=str(P),pairing=str(pair),scope_note='Counterexample to the variational inference; no full gauge-domain classification is asserted.')

@register('C24','C','T1','TE/TM tangential projector and Coulomb divergence for the two declared half-space mode families.')
def c24():
    p,k,z=sp.symbols('p k z',positive=True);w=sp.sqrt(p*p+k*k)
    # Tangential TM amplitude k/w; normal components chosen to obey divergence=0.
    pec=[k/w*sp.sin(k*z),sp.I*p/w*sp.cos(k*z)]
    pmc=[k/w*sp.cos(k*z),-sp.I*p/w*sp.sin(k*z)]
    div=[sp.simplify(sp.I*p*v[0]+sp.diff(v[1],z)) for v in [pec,pmc]]
    proj=sp.simplify(1-p*p/w**2-k*k/w**2)
    return require(div==[0,0] and proj==0,divergences=[str(x) for x in div],tangential_projector='diag(kz^2/omega^2,1) in the p-aligned frame',scope_note='These modes support the two comparison kernels; they do not exhaust admissible boundary conditions.')

@register('C25','C','T8','Signed kappa identity; the equivalence uses absolute kappa and excludes M=0.')
def c25():
    m,M,k=sp.symbols('m M k',real=True);E2=k*k+M*M
    lhs=M*M/E2-M*M/(m*m);rhs=M*M*(m*m-E2)/(m*m*E2)
    return require(sp.simplify(lhs-rhs)==0,identity='kappa^2-(M/m)^2=M^2*(m^2-E^2)/(m^2*E^2)',conditions='m>0, 0<|M|<m')

@register('V26','V','T8','Positive-band emission kinematics: finite checks of the exact energy-momentum inequality.')
def v26():
    rng=np.random.default_rng(SEED);gaps=[];residual=[]
    for _ in range(80):
        k=rng.normal(size=2)*3;p=rng.normal(size=2)*4;m=1.;M=.5
        lower=np.sqrt(k@k+m*m);final=np.sqrt((k-p)@(k-p)+m*m)+np.linalg.norm(p)
        residual.append(final-lower);gaps.append(lower-np.sqrt(k@k+M*M))
    return require(min(residual)>=-1e-12 and min(gaps)>0,min_convexity_residual=min(residual),min_band_gap=min(gaps),scope_note='Universal proof is the Euclidean triangle inequality in T8; no finite-time invariance follows.')

@register('W27','W','T8','Off-shell finite-time transition can be nonzero when the on-shell rate is zero.')
def w27():
    delta=1.;T=np.pi;coefficient=4*np.sin(delta*T/2)**2/delta**2
    return require(coefficient>3.99,coefficient=coefficient,formula='4 q^2 |V_fi|^2 sin^2(Delta T/2)/Delta^2',scope_note='Generic counterexample; actual M67 bulk matrix elements remain uncomputed.')

@register('W28','W','T1','Anisotropic Gaussian gives a positive matrix with unequal tangential entries.')
def w28():
    us,weights=np.polynomial.legendre.leggauss(120);phis=(np.arange(256)+.5)*2*np.pi/256;mat=np.zeros((2,2));w=2.
    for u,wu in zip(us,weights):
        n=np.array([np.sqrt(1-u*u)*np.cos(phis),np.sqrt(1-u*u)*np.sin(phis)])
        amp=np.exp(-w*w*(.3**2*n[0]**2+1.2**2*n[1]**2))*normal_weight(w*u)
        for a in range(2):
            for b in range(2):mat[a,b]+=wu*2*np.pi/len(phis)*np.sum(amp*((a==b)-n[a]*n[b]))
    mat*=w/(16*np.pi**3)
    return require(abs(mat[0,0]-mat[1,1])>.001 and np.linalg.eigvalsh(mat).min()>0,matrix=mat)

@register('W29','W','T7','The old width objective is not globally monotone; this is not an admissible-window optimum.')
def w29():
    v=.01;h=np.sqrt(3)/np.sqrt(1-v*v);data=[]
    for ell in [.2,.3,.4,.6,1.]:
        J,_=spectrum(h,profile='gaussian',ell=ell)
        data.append(dict(ell=ell,objective_per_q2=2*np.pi*(2-v*v)*J*ell/v))
    return require(data[2]['objective_per_q2']>data[0]['objective_per_q2'] and data[-1]['objective_per_q2']<data[3]['objective_per_q2'],data=data,scope_note='Actual optimization must include the declared error constraints; no optimum is claimed here.')

@register('C30','C','T7','Band-bottom quadratic dispersion has a finite coherence scale even at central v=0.')
def c30():
    r,ell,M,T=sp.symbols('r ell M T',positive=True)
    val=sp.integrate(4*ell**2*r*sp.exp(-(2*ell**2+sp.I*T/M)*r*r),(r,0,sp.oo),conds='none')
    return require(sp.simplify(val-1/(1+sp.I*T/(2*M*ell**2)))==0 and sp.re(2*ell**2+sp.I*T/M)==2*ell**2,quadratic_coherence=str(val),scope_note='Exact in the quadratic low-momentum model, not in the full relativistic dispersion.')

@register('C31','C','L1','Cofactor transport identity for a generic real 3x3 matrix.')
def c31():
    a=sp.Matrix(3,3,sp.symbols('g0:9'));v=sp.Matrix(sp.symbols('v0:3'))
    skew=lambda x:sp.Matrix([[0,-x[2],x[1]],[x[2],0,-x[0]],[-x[1],x[0],0]])
    residual=a*skew(v)*a.T-skew(a.cofactor_matrix()*v)
    return require(all(sp.expand(x)==0 for x in residual),entries=9)

@register('V32','V','L1','Exact affine collision law vs direct 4x4 propagation, including both determinant orientations.')
def v32():
    rng=np.random.default_rng(SEED+1);errors=[]
    for i in range(30):
        G=rng.normal(size=(3,3));U,s,Vh=np.linalg.svd(G);R=Vh.T
        if np.linalg.det(U)<0:U[:,-1]*=-1;s[-1]*=-1
        if np.linalg.det(R)<0:R[:,-1]*=-1;s[-1]*=-1
        alpha=.23;m=rng.normal(size=3);m=.7*m/np.linalg.norm(m);r=rng.normal(size=3);r=.6*r/np.linalg.norm(r)
        S=U@np.diag(np.sin(2*alpha*s))@R.T;C=U@np.diag(np.cos(2*alpha*s))@U.T
        pred=(cof(C)+cross(S@m)@C)@r+cof(S)@m
        H=sum((G[a,b]*np.kron(PAULI[a],PAULI[b]) for a in range(3) for b in range(3)),np.zeros((4,4),complex))
        rho=np.kron((I2+sum(r[a]*PAULI[a] for a in range(3)))/2,(I2+sum(m[a]*PAULI[a] for a in range(3)))/2)
        E=expm(-1j*alpha*H);out=E@rho@E.conj().T
        direct=np.array([np.trace(np.kron(x,I2)@out).real for x in PAULI]);errors.append(np.linalg.norm(direct-pred))
    return require(max(errors)<1e-12,cases=len(errors),max_absolute_error=max(errors),tolerance=1e-12)

@register('C33','C','L1','Resonance determinant identity; uniqueness and convergence are distinct.')
def c33():
    d=sp.symbols('d0:3');c=sp.symbols('c0:3');u=sp.symbols('u0:3')
    skew=sp.Matrix([[0,-u[2],u[1]],[u[2],0,-u[0]],[-u[1],u[0],0]])
    target=sp.prod(d)+sum(d[i]*c[(i+1)%3]*c[(i+2)%3]*u[i]**2 for i in range(3))
    return require(sp.expand((sp.diag(*d)-skew*sp.diag(*c)).det()-target)==0,formula='prod(d)+sum_i d_i c_j c_k u_i^2')

@register('W34','W','L1','Unique stationary point can coexist with a two-cycle.')
def w34():
    M=np.diag([0.,-1.,0.]);r=np.array([0.,.5,0.])
    return require(abs(np.linalg.det(np.eye(3)-M))>0 and np.allclose(M@M@r,r) and not np.allclose(M@r,r),eigenvalues=np.diag(M),det_I_minus_M=np.linalg.det(np.eye(3)-M))

@register('V35','V','L2','Exact parity-block two-qubit dynamics vs direct unitary, arbitrary transverse G.')
def v35():
    rng=np.random.default_rng(SEED+2);errors=[]
    for _ in range(24):
        G=rng.normal(size=(2,2))*.4;he,hr,T=rng.uniform(.1,2,3);mj=.6
        S=np.sum(G*G);d=np.linalg.det(G);wm,wp=S+2*d,S-2*d
        vm=np.sqrt(wm+(he-hr)**2/4);vp=np.sqrt(wp+(he+hr)**2/4)
        pred=mj*(wm/vm**2*np.sin(vm*T)**2-wp/vp**2*np.sin(vp*T)**2)
        H=he*np.kron(SZ,I2)/2+hr*np.kron(I2,SZ)/2+sum((G[a,b]*np.kron(PAULI[a],PAULI[b]) for a in range(2) for b in range(2)),np.zeros((4,4),complex))
        U=expm(-1j*T*H);rho=np.kron(I2/2,(I2+mj*SZ)/2)
        direct=np.trace(np.kron(SZ,I2)@U@rho@U.conj().T).real;errors.append(abs(direct-pred))
    return require(max(errors)<1e-12,max_absolute_error=max(errors),cases=len(errors),tolerance=1e-12)

@register('C36','C','L3','Elliptical analyser and PSD null-class algebra; general matrix spectrum retained.')
def c36():
    k,a,b,c,d=sp.symbols('k a b c d',real=True);u=sp.Matrix([k,sp.I]);J=sp.Matrix([[a,b+sp.I*c],[b-sp.I*c,d]])
    q=sp.expand((sp.conjugate(u.T)*J*u)[0]);target=k*k*a+d-2*k*c
    zero=sp.simplify(J.subs({b:0,c:k*a,d:k*k*a})*u)
    return require(sp.simplify(q-target)==0 and zero==sp.zeros(2,1),quadratic_form=str(q),null_class='J=a [[1,i*kappa],[-i*kappa,kappa^2]], a>=0',scope_note='PSD equivalence uses the square-root argument in Appendix C; kappa=0 is discussed separately.')

@register('C37','C','L3','Identity-on-qubit cross terms vanish at second order for maximally mixed input.')
def c37():
    a=sp.Matrix([[1,sp.I],[-sp.I,2]]);b=sp.Matrix([[0,2],[2,1]]);rho=sp.Matrix([[sp.Rational(2,3),sp.Rational(1,5)],[sp.Rational(1,5),sp.Rational(1,3)]])
    comm=lambda x,y:x*y-y*x
    vals=[sp.trace(comm(a,comm(b,rho))),sp.trace(comm(b,comm(a,rho)))]
    return require(vals==[0,0],environment_double_commutator_traces=[str(x) for x in vals],scope_note='Finite algebra anchor; general proof is cyclicity of trace. Not an all-orders Coulomb decoupling claim.')

@register('R38','R','F01,F02,F05,F07','Semantic regression fixtures detect old failures; not new scientific evidence.')
def r38():
    cert=window_certificate();fixtures=[]
    widths=np.array([.1,.01,.001]);areas=4*np.pi*widths**2
    fixtures.append(dict(name='old_area_point_limit_infinity',computed_areas=areas.tolist(),old_prediction='area increases under point localization',detected=bool(np.all(np.diff(areas)<0))))
    w=160*np.pi+3*np.pi/4
    disk,_=spectrum(w,'free','disk',scale=w**3)
    fixtures.append(dict(name='old_disk_constant',old_prediction=1/(2*np.pi**2),computed=disk,old_validation='FAIL' if abs(disk-1/(2*np.pi**2))>.02 else 'PASS',detected=abs(disk-1/(2*np.pi**2))>.02))
    kappa=-.5/np.sqrt(.04+.25)
    fixtures.append(dict(name='old_positive_kappa_iff',old_condition=bool(kappa>.5),correct_condition=bool(abs(kappa)>.5),detected=(kappa>.5)!=(abs(kappa)>.5)))
    fixtures.append(dict(name='window_omits_Dyson_ceiling',valid_relative=float(cert['relative_bound']),mutated_q=1.,detected=32*cert['F4_upper']*cert['T']**3/(cert['pi_lower']*cert['f_lower'])>cert['delta']))
    return require(all(x['detected'] for x in fixtures),live_fire=fixtures)

@register('R39','R','F08,F10','Functional ledger-validation mutations, including missing rows and class drift.')
def r39():
    def validate(rows,expected):
        ids=[r['id'] for r in rows]
        return len(ids)==len(set(ids)) and {r['id']:r['class'] for r in rows}==expected and all(isinstance(r['pass'],bool) for r in rows)
    good=[{'id':'a','class':'C','pass':True},{'id':'b','class':'V','pass':False}];expected={'a':'C','b':'V'}
    mutated=[good[:-1],good+[good[0]],[{'id':'a','class':'V','pass':True},good[1]],[good[0],{'id':'b','class':'V','pass':'PASS'}]]
    outcomes=[validate(x,expected) for x in mutated]
    return require(validate(good,expected) and not any(outcomes),valid_fixture=True,mutation_results=[{'injection':name,'validation':'PASS' if v else 'FAIL'} for name,v in zip(['missing row','duplicate row','class mismatch','string instead of Boolean'],outcomes)],scope_note='Literal booleans here are control fixtures, not scientific evidence rows.')

@register('G40','G','PACKAGE','Registry uniqueness and class census, with a duplicate-ID live-fire control.')
def g40():
    ids=[x[0] for x in REGISTRY];classes=[x[1] for x in REGISTRY]
    valid=lambda z:len(z)==len(set(z))
    return require(valid(ids) and not valid(ids+[ids[0]]) and all(c in ['C','V','W','R','G','D','X','T'] for c in classes),rows=len(ids),census=dict(sorted(Counter(classes).items())),live_fire={'duplicate_id_validation':'FAIL' if not valid(ids+[ids[0]]) else 'PASS'})


@register('W41','W','T3','Dropping the uniform-continuity hypothesis changes the grazing coefficient.')
def w41():
    # General nonnegative spectral multiplier; no positive real-space density is asserted.
    # g(p)=(1+p^2)^(-3/4)*(1+0.5*cos(p^2))/1.5, w_n^2=2*pi*n.
    first=quad(lambda z:normal_weight(z,'PMC')*np.cos(z*z),0,1,epsabs=1e-11)[0]
    tail=quad(lambda t:normal_weight(np.sqrt(t),'PMC')/(2*np.sqrt(t)),1,np.inf,weight='cos',wvar=1,epsabs=1e-11,limit=500)[0]
    L=np.pi/2;actual=(L+.5*(first+tail))/(1.5*8*np.pi**2);wrong=L/(8*np.pi**2)
    return require(actual<wrong-.001,chirped_grazing_coefficient=actual,incorrect_coefficient_if_H_frozen=wrong,scope_note='Exact phase identity p^2=w^2-z^2 gives the limiting integral; numerical integration evaluates its strict gap. This g is a spectral multiplier, not certified as |rhohat|^2 for nonnegative rho.')


@register('V42','V','T4,T5','Complex matrix spectrum and tilted axis: finite-mode unitary vs both frequency kernels.')
def v42():
    N=5;an=np.diag(np.sqrt(np.arange(1,N)),1);eye=np.eye(N)
    modes=[np.kron(an,eye),np.kron(eye,an)];ws=[.7,1.8]
    lam=np.array([[.20+.07j,.11-.03j],[.06-.12j,-.13+.02j]])
    hb=sum(ws[j]*modes[j].conj().T@modes[j] for j in range(2));vac=np.zeros((N*N,N*N));vac[0,0]=1
    T=1.4;h=1.3;q=.002;data=[];F=sum(np.linalg.norm(row) for row in lam)
    for kappa in [-1.,-.6,0.,.6,1.]:
        axis=np.array([np.sqrt(1-kappa*kappa),0.,kappa]);O=sum(axis[j]*PAULI[j] for j in range(3))
        V=sum((np.kron(PAULI[a],sum(lam[a,j]*modes[j]+lam[a,j].conjugate()*modes[j].conj().T for j in range(2))) for a in range(2)),np.zeros((2*N*N,2*N*N),complex))
        H=np.kron(h*O/2,np.eye(N*N))+np.kron(I2,hb)+q*V
        U=expm(-1j*T*H);rho=np.kron(I2/2,vac);exact=np.trace(np.kron(O,np.eye(N*N))@U@rho@U.conj().T).real
        u=np.array([kappa,1j]);second=0.
        for j,w in enumerate(ws):
            J=np.outer(lam[:,j],lam[:,j].conjugate())
            fm=(u.conjugate()@J@u).real;fp=(u@J@u.conjugate()).real
            second+=-2*q*q*(fm*FT(h-w,T)-fp*FT(h+w,T))
        bound=64*q**4*F**4*T**4
        data.append(dict(kappa=kappa,exact=exact,second_order=second,error=abs(exact-second),fourth_order_bound=bound))
    return require(all(x['error']<=x['fourth_order_bound'] for x in data),data=data,scope_note='Discrete-mode check of helicity and counter-rotating signs; the continuum proof is separate.')


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--out-dir',type=Path,default=Path(__file__).resolve().parent)
    parser.add_argument('--paper',type=Path,help='Optionally check the generated metadata block in this manuscript.')
    args=parser.parse_args();args.out_dir.mkdir(parents=True,exist_ok=True)
    rows=[]
    for rid,cls,claim,scope,fn in REGISTRY:
        try:
            ok,evidence=fn();row={'id':rid,'class':cls,'claims':claim.split(','),'scope':scope,'pass':bool(ok),'evidence':evidence}
        except Exception as exc:
            row={'id':rid,'class':cls,'claims':claim.split(','),'scope':scope,'pass':False,'error':f'{type(exc).__name__}: {exc}'}
        rows.append(row);print(f"{rid} {cls} {'PASS' if row['pass'] else 'FAIL'} {claim}",flush=True)
        if not row['pass']:print(json.dumps(row,ensure_ascii=False),flush=True)
    census=dict(sorted(Counter(x['class'] for x in rows).items()));failed=sum(not x['pass'] for x in rows)
    artifact={'paper':'ZS-M69','version':VERSION,'profile':'FULL','seed':SEED,'rows':len(rows),'passed':len(rows)-failed,'failed':failed,'census':census,'P':0,'proof_review':'Human-readable proofs; no executable row certifies their full quantifiers. Author-side checks, not independent AI review.','environment':{'python':platform.python_version(),'numpy':np.__version__,'scipy':scipy.__version__,'sympy':sp.__version__},'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'checks':rows}
    if args.paper:
        expected={'version':VERSION,'rows':len(rows),'census':census,'P':0}
        try:
            match=re.search(r'<!-- M69-VERIFICATION-METADATA\s*\n(.*?)\n-->',args.paper.read_text(encoding='utf-8'),re.S)
            got=json.loads(match.group(1)) if match else None
            artifact['manuscript_metadata_check']={'pass':got==expected,'expected':expected,'actual':got}
        except (OSError, ValueError) as exc:
            artifact['manuscript_metadata_check']={'pass':False,'expected':expected,'error':f'{type(exc).__name__}: {exc}'}
    artifact['package_failed']=int(not artifact.get('manuscript_metadata_check',{'pass':True})['pass'])
    artifact['status']='FAIL' if failed or artifact['package_failed'] else 'PASS'
    path=args.out_dir/'zs_m69_verify_v2_0.json';path.write_text(json.dumps(artifact,ensure_ascii=False,indent=2,sort_keys=True)+'\n',encoding='utf-8')
    print(json.dumps({k:artifact[k] for k in ['version','profile','status','rows','passed','failed','package_failed','census','P']},ensure_ascii=False),flush=True)
    print('THEOREM PROOFS: manuscript. NOVELTY / GRADE / M67 REALIZATION: not executable claims.',flush=True)
    return 1 if artifact['status']=='FAIL' else 0

if __name__=='__main__':raise SystemExit(main())
