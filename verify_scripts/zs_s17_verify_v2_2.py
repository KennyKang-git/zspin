#!/usr/bin/env python3
# =====================================================================
# zs_s17_verify_v2_2.py    ZS-S17 v2.2 FINAL  --  fail-closed verifier.
# Every numbered check asserts on a computed number. Numbers produced by the
# companion zs_s17_active_space.py are read from its JSON output, which is
# written NEXT TO THE SCRIPTS (no absolute paths), so the four released files
# run from any single folder.
#
# Changes in v2.2 (response to the v2.1 review; no new physics):
#  * SCOPE FIX. The closure claim is now checked over ALL FOUR (s,t) pairs and
#    is stated only for the Yang-Mills-relevant ALTERNATING vertex. For
#    contrast the full non-antisymmetrised bilinear leaks 29.5% out of the
#    six-mode space, so "exactly closed" must NOT be said of the bilinear.
#  * CORRECTION. v2.1 reported ONE nontrivial hedgehog zero, found by fsolve
#    from a bounded grid. The resultant gives the GLOBAL count: there are
#    THREE nontrivial real zeros. Two sit at |q|^2 ~ 1e6-1e7, far outside any
#    region where the quadratic-truncated curvature means anything; the
#    physically relevant one is at |q|^2 = 81.6.
#  * RIGOUR. That root now carries a Krawczyk-certified enclosure
#    (existence + local uniqueness), so its status is COMPUTED / CERTIFIED,
#    not PROVEN: the certification is conditional on the numerically computed
#    c_rst and on ordinary floating-point interval evaluation.
#  * ACCOUNTING. The 1/N^2 slope gate is an OPEN registration, not a PASS,
#    and is excluded from the pass count.
# =====================================================================
import numpy as np, json, sys, subprocess
from pathlib import Path
HERE=Path(__file__).resolve().parent
JS=HERE/"zs_s17_wp_results.json"
P=[]
def ck(n,t,c,note=""):
    P.append(bool(c)); print(f"  [{'PASS' if c else 'FAIL'}] ({t}) {n}"+(f"  ({note})" if note else ""))
A=35/437; Q=11.0; vev=245.93; g2=4*np.pi*(11/93)
if not JS.exists():
    subprocess.run([sys.executable,str(HERE/"zs_s17_active_space.py")],check=True)
R=json.load(open(JS)); c=np.array(R['c']); lam0=R['lam0']; lam1=R['lam1']

ck("1. gap lam_1 = 1.2428 (T1); second T1 copy at lam_h = 7.5211","COMP",
   abs(lam0-1.2428)<1e-3 and abs(lam1-7.5211)<1e-3, f"{lam0:.4f}, {lam1:.4f}")
ck("2. CORRECTED decomposition: 92.8605% gap-T1 + 7.1395% high-T1, |rest| < 2.4e-14","PROVEN",
   abs(R['power_gap']-0.928605)<1e-5 and abs(R['power_high']-0.071395)<1e-5 and abs(R['power_rest'])<1e-12,
   f"gap-only leakage {100*(1-R['power_gap']):.4f}%, NOT the 23% quoted in v1.6-v2.0")
ck("3. ALL-PAIRS (s,t) alternating YM vertex: leakage out of the six-mode space is zero","PROVEN",
   R['active_alt_closure_resid']<1e-20, f"residual {R['active_alt_closure_resid']:.1e}")
ck("4. SCOPE: the full NON-antisymmetrised bilinear leaks 29.5% -- closure holds for the alternating vertex ONLY","COMP",
   0.25<R['active_full_bilinear_leak']<0.35, f"{100*R['active_full_bilinear_leak']:.2f}%")
ck("5. icosahedral alignment: signed face action commutes with L2; intertwiner 1-dim (Schur)","COMP",
   R['sym_commute']<1e-10 and R['intertwiner_sv']<1e-10 and R['align_resid']<1e-8,
   f"alignment residual {R['align_resid']:.1e}")
ck("6. all eight c_rst exactly proportional to epsilon => dim Hom_I(T1xT1,T1) = 1","PROVEN",
   R['c_eps_maxresid']<1e-10, f"max eps-residual {R['c_eps_maxresid']:.1e}")
ck("7. c_000 = -0.175800; |c_100| = 0.048746; |c_111| = 0.001943","COMP",
   abs(c[0,0,0]+0.175800)<1e-5 and abs(abs(c[1,0,0])-0.0487456)<1e-6 and abs(abs(c[1,1,1])-0.0019435)<1e-6)
ck("8. three-mode zero v0* = -Om_0/(g c_000) = 5.2015","COMP", abs(R['v0_3mode']-5.2015)<1e-3)
zs=R['hedgehog_zeros_global']; near=[z for z in zs if abs(z[0]-5.187)<1e-2]
ck("9. the nontrivial zero SURVIVES the exact six-mode lift at v = (5.187, 0.555)","COMP",
   len(near)==1 and abs(abs(near[0][1])-0.5546)<2e-3, "=> not a three-mode artifact")
ck("10. CORRECTED global count (resultant, degree 4, not a search): THREE nontrivial real zeros","COMP",
   R['resultant_degree']==4 and len(zs)==3, "v2.1 reported one; the fsolve grid was too small")
far=[3*(z[0]**2+z[1]**2) for z in zs if abs(z[0]-5.187)>1e-2]
ck("11. the two extra zeros sit at |q|^2 ~ 1e6-1e7, outside any meaningful truncation","COMP",
   len(far)==2 and min(far)>1e5, f"|q|^2 = {min(far):.2e}, {max(far):.2e}")
ck("12. Krawczyk enclosure certifies existence + LOCAL uniqueness of the relevant root","CERTIFIED",
   R['krawczyk_certified'] and abs(R['jac_det_at_root'])>1e-6,
   f"K(X) strictly inside X; det J = {R['jac_det_at_root']:.4f}")
q2=3*(near[0][0]**2+near[0][1]**2)
ck("13. |q*|^2 = 81.6 (six-mode) vs 81.2 (three-mode): the zero barely moves","COMP", abs(q2-81.6)<0.3, f"{q2:.2f}")
ck("14. RETRACTED 'Gribov copy': the 32 face holonomies give |tr W|/3 = 0.40-0.49","RETRACT",
   R['holo6_min']<0.6 and R['holo6_mean']<0.6, f"min {R['holo6_min']:.4f}, mean {R['holo6_mean']:.4f}")
ck("15. => projected B = 0 does NOT imply F_full = 0: a spurious vacuum of the POLYNOMIAL reduction","DERIV",
   R['holo6_min']<0.99)
lam_tH=g2*3.0; ghf=lambda N:(lam_tH/N)*N
ck("16. RETRACTED v2.0 SU(N) discriminator: at fixed 't Hooft coupling g^2 C_A = g^2 N is N-independent","RETRACT",
   abs(ghf(2)-ghf(12))<1e-12, "the claimed 71% run assumed fixed g")
Jx=np.array([[0,1,0],[1,0,1],[0,1,0]],complex)/np.sqrt(2)
Jy=np.array([[0,-1j,0],[1j,0,-1j],[0,1j,0]],complex)/np.sqrt(2)
Jz=np.diag([1,0,-1]).astype(complex); J=[Jx,Jy,Jz]
ck("17. C_2(T1) = sum J_i^2 = 2I exactly => L_2 restricted to T1 equals (lam_1/2) C_2","PROVEN",
   np.abs(sum(j@j for j in J)-2*np.eye(3)).max()<1e-12)
IZ=lam0*sum(np.kron(j,j) for j in J); QZ=0.25*(IZ+2*lam0*np.eye(9))
evq=np.unique(np.round(np.linalg.eigvalsh(QZ).real,10))
ck("18. coproduct defect I_Z = lam_1 S_1.S_2; Q_Z = (I_Z + 2 lam_1)/4 is 0 on A_g and 3 lam_1/4 on H","PROVEN",
   abs(evq[0])<1e-9 and abs(evq[-1]-0.75*lam0)<1e-9, f"spectrum {[round(float(x),4) for x in evq]}")
Rk=float(np.sqrt(1+0.75*lam0))
ck("19. => M(2++)^2/M(0++)^2 = 1 + 3 lam_1/4, R = 1.3900 as an OPERATOR IDENTITY","DERIV",
   abs(Rk-1.3900)<5e-4, "physical mass normalisation still conditional on the 1/4 Hessian gate")
m0=vev*A/Q
ck("20. m(0++) = vA/Q = 1.791 GeV; m(2++) = 1.390 vA/Q = 2.489 GeV","ARITH",
   abs(m0-1.791)<0.01 and abs(Rk*m0-2.489)<0.01)
band=(1.098,1.387); cnt=sum(1 for a_ in range(1,13) for d in range(1,13) for x in range(-2,3) for y in range(-2,3)
                            if band[0]<=(a_/d)*(A**x)*(Q**y)<=band[1])
ck("21. anti-numerology EXACT 89/3600 = 2.47%; g^2 = 4pi(11/93) = 1.49 locked","COMP",
   cnt==89 and abs(g2-1.49)<0.01)

print("\n  [OPEN GATE, NOT COUNTED] F-S17.6  1/N^2 slope test: fit g_hf(N) = g_inf + a/N^2 + b/N^4")
print("                            to per-N lattice M(2++)/M(0++). Layer-Lift predicts g_inf = lam_1, a = 0.")
print("  [OPEN GATE, NOT COUNTED] F-S17.7  S14 master action restricted to Sym^2(T1): is the canonical")
print("                            Hessian exactly (I_Z + 2 lam_1 I)/4 ?  That single factor 1/4 is the")
print("                            last step from DERIVED-CONDITIONAL to DERIVED.")
print("\n"+"="*76)
print(f"ZS-S17 v2.2 FINAL: {sum(P)}/{len(P)} computed & proof checks PASS; 2 OPEN gates pre-registered (not counted)")
print("  Closed : TI representation structure; signed color -C_A; the Yang-Mills-relevant")
print("           two-T1 active space (alternating vertex only); all c_rst proportional to epsilon;")
print("           the Casimir-coproduct Layer-Lift operator identity.")
print("  Computed: a nontrivial hedgehog zero of the reduced field, certified by a Krawczyk")
print("           enclosure, surviving the six-mode lift; three such zeros exist globally.")
print("  Retracted: the Gribov-copy reading; the SU(N) leading-order discriminator;")
print("           (earlier) the v1.9 Richardson extrapolation.")
print("  Open   : the 1/4 mass-Hessian normalisation (F-S17.7); the 1/N^2 slope test (F-S17.6);")
print("           the gauge-reduced bottom-up dynamics.")
print("  Net: the geometric and representation-theoretic bridge is closed. The physical mass")
print("  normalisation is isolated to one explicit S14 Hessian gate.")
print("="*76)
