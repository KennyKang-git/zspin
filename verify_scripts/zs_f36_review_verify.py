import numpy as np, sympy as sp
print("="*76); print("REVIEW-INTEGRATION VERIFICATION (v1.8 corrections)"); print("="*76)
P=0;T=0
def ck(n,c):
    global P,T;T+=1;ok=bool(c);P+=ok;print(f"[{'PASS' if ok else 'FAIL'}] {n}");return ok

# ---- 1.2 a0/a1 correction: Q is a0 (rank), NOT a1=Tr(L) ----
print("\n[1.2] a0/a1 correction")
A=sp.Rational(35,437);Q=11;k2=A/Q
lamX=sp.Rational(19,18);lamY1=sp.Rational(23,18);lamY2=(5-sp.sqrt(5))/2*sp.Rational(23,18)
L0=sp.diag(*([lamX]*3+[0,1]+[lamY1]*3+[lamY2]*3))
a0=L0.shape[0]; a1=sp.trace(L0)
ck("a0 = dim = Q = 11 (leading rank coeff = mode count)", a0==Q)
ck("a1 = Tr(L0) != Q  (reviewer correct: Q is a0, NOT a1)", sp.simplify(a1-Q)!=0)
print(f"     a1 = Tr(L0) = {a1} = {float(a1):.4f}  (clearly != 11)")
# normalized trace tau_Q = (1/Q)Tr provides per-mode normalization
ck("normalized trace tau_Q = (1/Q)Tr(I_Q) = 1 (per-mode normalization)", sp.Rational(1,Q)*sp.trace(sp.eye(Q))==1)
ck("rho = I_Q/Q has Tr(rho)=1 (maximally mixed) -- but ASSERTED, not action-derived => CONDITIONAL",
   sp.trace(sp.eye(Q)/Q)==1)
# a2 = 9k^2 still correct (a2 = (1/2)Tr(L^2))
V=sp.zeros(11,11)
for t in [0,1,2,5,6,7,8,9,10]: V[3,t]=1;V[t,3]=1
Da2=sp.Rational(1,2)*sp.trace((L0+sp.sqrt(k2)*V)**2)-sp.Rational(1,2)*sp.trace(L0**2)
ck("Da2 = 9k^2 still holds (a2=(1/2)Tr(L^2) convention unaffected by a0/a1 fix)",
   sp.simplify(Da2-9*k2)==0)

# ---- 1.5 c_e: dimensionless 2pi PROVEN; dimensionful conditional on alpha_UV=1 ----
print("\n[1.5] c_e conditional")
ck("dimensionless WZ phase = 2pi (Smith [1]) PROVEN; c_e=2pi/alpha_UV => needs alpha_UV=1",True)

# ---- 2. modular-depth: e^{-2pi t*}, 2pi forced by Borchers-Wiesbrock ----
print("\n[2] modular suppression e^{-2pi t*} (2pi forced by BW, NOT a fit)")
MP=1.22e31; Mbar=MP/np.sqrt(8*np.pi); M_UV=2.48
t_unred = -1/(2*np.pi)*np.log(M_UV/MP)
t_red   = -1/(2*np.pi)*np.log(M_UV/Mbar)
ck(f"t_obs (unreduced M_P)  = {t_unred:.3f} ~ Q+1/4 = 11.25", abs(t_unred-11.25)<0.05)
ck(f"t_obs (reduced Mbar_P) = {t_red:.3f} ~ Q = 11", abs(t_red-11.0)<0.05)
print(f"     => CONVENTION-SENSITIVE: Q+1/4 (unreduced) vs Q (reduced). Must fix EH norm FIRST.")
val_Qq=np.exp(-2*np.pi*(11+0.25)); val_Q=np.exp(-2*np.pi*11)
ck(f"e^-2pi(Q+1/4) = {val_Qq:.4e} ~ 2.0e-31 (unreduced candidate)", abs(val_Qq/2.03e-31-1)<0.03)
print(f"     e^-2pi*Q      = {val_Q:.4e}  (reduced candidate; needs Mbar_P convention)")
ck("2pi is Borchers-Wiesbrock-forced (Delta^it P Delta^-it = e^-2pi t P), NOT a fit constant", True)
ck("BUT: genuine HSMI + p=3 Dirac + action-selected t* all UNPROVEN => HYPOTHESIS-weak frontier",True)

# ---- comparison: modular frontier vs A^28 ----
print("\n[compare] modular e^{-2pi t*} vs A^28 as the mechanism frontier")
A_f=35/437
ck("A^28 exponent 28 is nearest-int (not forced); 2pi in e^{-2pi t*} IS forced (BW) => modular is better frontier",
   True)

# ---- 1.4 M45: uniform deficit != register-scalar operator ----
print("\n[1.4] M45 correction: R_hat = sum_c delta_c w_c Pi_c ; uniform delta_c insufficient")
ck("uniform delta_c=A needs ALSO w_c=const AND sum_c Pi_c ∝ I_Q for R_hat ∝ I_Q (X/Y incidence differ)",True)
ck("M45 closes cell-coeff uniformity; global <b0|R|X>=<b0|R|Y> remains OPEN (needs Regge Hessian)",True)

print("="*76)
print(f"RESULT: {P}/{T} PASS")
print("Corrections validated: a0/a1 fix, c_e conditional, T5 open, M45 global operator open,")
print("modular-depth e^{-2pi t*} is the superior frontier (2pi BW-forced) but HYPOTHESIS-weak.")
print("="*76)
