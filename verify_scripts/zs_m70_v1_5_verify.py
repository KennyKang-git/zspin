#!/usr/bin/env python3
"""M70 v1.5 companion, verifier v1.5.0. Deterministic, offline, no input mutation.

Run: python m70_v1_5_verify.py --paper m70_v1_5.md
     python m70_v1_5_verify.py --math-only
     python m70_v1_5_verify.py --paper m70_v1_5.md --self-test
Requires Python >=3.10, numpy, scipy, sympy, mpmath. Tested versions are in paper.
JSON goes to stdout; exit 0=registered checks pass, 1=check failure, 2=dependency
or invocation error. A missing paper fails closed; --math-only explicitly skips G.
C rows certify only the displayed algebra, V finite numerical cases, W witnesses,
R regressions, G package controls, X diagnostics (non-evidence); D is SKIP. P=0.
No novelty/grade is computed; G04/G05 only check that the declared status strings
use the Mission vocabulary and agree across paper, manifest and script.
Quad epsrel=3e-11 (outer Gaussian 2e-10); moving sector: analytic-angle route with
adaptive z-quad epsrel=1e-11 (route 3, angular reduction from the v1.2 audit,
re-derived and certified in C15), covariant half-angle route with 128 fixed
Gauss-Legendre nodes (route 2) and photon-polar 400x96 route (route 1); outer quadrature binary64;
mpmath=50 dps for the entire analytic angular average; no RNG. Warnings are captured per row, never silenced globally.
v1.5 integrates the two v1.4 parents: bound 18, photon half-energy lower bound,
repaired soft denominator, and LM-Q fixed-frequency limit.
A-parent v1.4 additions retained: LM-D/L/P, KRS mapping, transport suffix guard.
Inherited v1.3 changes: F01 (PEC moment condition, LM-A' E^2 theorem: C15, V17, W06, X01),
F03 (Mission vocabulary + audit-round registry: G04), F05 (angular convergence:
V14 analytic route, V16 three-route/node-doubling), CPN11 version guard (G05).
--fault changes an implementation/input, never the test's expected answer.
--self-test runs a passing baseline first, then checks the designated failing row
for each mutation in a fresh explicit single-row process, missing-document behavior, math-only, dependency failure and
two byte-identical runs from an isolated directory containing only the two files.
It uses the same installed dependencies, not an independently provisioned machine.
"""
from __future__ import annotations
import argparse
from concurrent.futures import ThreadPoolExecutor
import os
import warnings
from collections import Counter
from functools import lru_cache
import hashlib
import json
import math
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile

VERSION = "1.5.0"
PAPER_VERSION = "1.5"
REGISTRY = {
    "C01": ("C", "LC-K", "full rest spinor tensor and transverse contraction"),
    "C02": ("C", "LC-U", "actual moving large-momentum tensor and angular integral"),
    "C03": ("C", "LC-K", "shell and delta-Jacobian reduction identities"),
    "C04": ("C", "LC-I", "rescaled IR coefficient integrals"),
    "C05": ("C", "LC-T", "photon shell bounds and fixed-z UV ratio"),
    "C06": ("C", "LB", "canonical initial-state resolvent and polynomial"),
    "C07": ("C", "LB", "rational witness polynomial, stationary points, exact max"),
    "C08": ("C", "LA", "two-parity boundary determinant"),
    "C09": ("C", "LA", "small-x recurrence coefficient and onset slope algebra"),
    "C10": ("C", "LC-T", "Gaussian moments giving tau powers"),
    "C11": ("C", "LM-K", "Pauli-trace current identity and moving tensor decomposition"),
    "C12": ("C", "LM-S", "soft angular integrals, closed forms, azimuthal average and log-gamma identity"),
    "C13": ("C", "LM-R", "massless ellipse kinematics, integrand reduction, exact plateau values, stable form of Phi"),
    "C14": ("C", "LM-B", "two-body kinematic identities and half-angle Jacobian used in the uniform bound"),
    "C15": ("C", "LM-A", "analytic angular reduction (route 3) and the E^2-moment PEC bound constants"),
    "V01": ("V", "LC-K", "27 shell/polar coordinate comparisons"),
    "V02": ("V", "LC-U", "exponential-profile Plancherel constants"),
    "V03": ("V", "LC-U", "finite-UV plateau and photon/total ratios"),
    "V04": ("V", "LC-I", "finite-IR three-family coefficients"),
    "V05": ("V", "LC-T", "Gaussian table by two coordinate routes"),
    "V06": ("V", "LC-T", "sharp-switch cutoff doubling, total and photon"),
    "V07": ("V", "LB", "spectral amplitude versus matrix exponential and envelope"),
    "V08": ("V", "LB", "resonance-layer and far-detuning samples"),
    "V09": ("V", "LA", "SciPy roots versus 50-digit Bessel route"),
    "V10": ("V", "LA", "energy ordering, monotonicity and threshold slope samples"),
    "V11": ("V", "LM-K", "moving photon-polar route versus covariant two-body route versus analytic-angle route; rest reduction"),
    "V12": ("V", "LM-S", "moving soft IR coefficients, three families, two routes"),
    "V13": ("V", "LM-R", "plateau closed form versus ellipse quadrature and large-momentum spectra"),
    "V14": ("V", "LM-B", "uniform-bound grid (analytic-angle route with quadrature error estimates)"),
    "V15": ("V", "LM-A", "single-momentum Gaussian adiabatic limits"),
    "V16": ("V", "LM-K", "angular convergence: 128/256-node covariant route against the analytic-angle route on the grid extremum and printed table"),
    "V17": ("V", "LM-A", "E^2-moment PEC dominating function holds on a momentum/frequency grid"),
    "W01": ("W", "LC-K", "normalized compact packet: zero exclusive overlap, positive inclusive current"),
    "W02": ("W", "LB", "retired v1.0 first-state counterexample and corrected endpoint"),
    "W03": ("W", "LB", "rational even/odd gap maximum strictly below envelope"),
    "W04": ("W", "LM-E", "moving photon energy exceeds the excitation mismatch, pointwise and integrated"),
    "W05": ("W", "LM-A", "normalized Gaussian packet violates the rest-sector adiabatic law"),
    "W06": ("W", "LM-A", "finite-energy heavy-tail packet: finite log-moment, infinite E^2-moment, divergent PEC tau^2 coefficient"),
    "R01": ("R", "LC-T", "photon energy cannot be replaced by total excitation"),
    "R02": ("R", "LC-T", "PEC Gaussian normalization uses tau^4"),
    "R03": ("R", "LA", "threshold equality does not create a subgap branch"),
    "R04": ("R", "LM-A", "packet long-time response follows moving soft law, not rest law"),
    "R05": ("R", "LM-R", "large-momentum plateau is not the rest plateau"),
    "X01": ("X", "LM-A", "diagnostic: tau^2 R_tau of the heavy-tail packet grows with tau (PEC); not a proof of divergence"),
    "G01": ("G", "PACKAGE", "paired file identity and companion hash"),
    "G02": ("G", "PACKAGE", "equation labels and critical displayed objects"),
    "G03": ("G", "PACKAGE", "numeric tables agree with recomputation and mode-specific denominator"),
    "G04": ("G", "PACKAGE", "ledger, Mission-vocabulary status fields, audit-round registry and commands"),
    "G05": ("G", "PACKAGE", "internal version consistency: no stale version commands or superseded status strings live in the text"),
    "D01": ("D", "NOVELTY", "external nontrivial novelty: not executable"),
    "D02": ("D", "MISSION", "full dynamics, physical instrument and research grade: not executable"),
    "D03": ("D", "PROOF", "universal analytic proofs: no formal proof object in this script"),
}
REGISTRY.update({'C16': ('C', 'LM-D', 'Dini integral and profile cutoff constants'), 'C17': ('C', 'LM-L', 'boundary-layer kernel, positivity endpoint and closed normal integrals'), 'C18': ('C', 'LM-P', 'energy-density scaling Jacobian and Gaussian Mellin factors'), 'C19': ('C', 'KRS-MAP', 'commutator algebra and finite-time Fourier weight ratio'), 'V18': ('V', 'LM-D', '288-point momentum-uniform PEC soft bound'), 'V19': ('V', 'LM-L', 'full finite-energy spectrum vs boundary-layer closed form at 10 points'), 'V20': ('V', 'LM-L/P', 'closed normal integral vs quadrature and Mellin coefficients with analytic tails'), 'W07': ('W', 'LM-D/P', 'normalized infinite-log packet and finite-energy power-tail packet'), 'W08': ('W', 'KRS-MAP', 'identity-projector cancellation vs positive external-pulse response')})
REGISTRY.update({
    "C20": ("C", "LM-B/E", "CM denominator identity, Lipschitz dispersion and integrated bound constants"),
    "C21": ("C", "LM-Q", "fixed-frequency high-energy kernel and exact PMC lower bound 64/(5 pi)"),
    "V21": ("V", "LM-E", "2268 on-shell points and 96 photon-weighted spectra in all three families"),
    "V22": ("V", "LM-Q", "fixed-frequency high-energy spectrum against the limiting integral"),
    "W09": ("W", "LM-B/Q", "finite PMC witness above 4 and the analytic nonoptimal lower bound"),
    "W10": ("W", "LM-B", "exact counterexample to the rejected soft denominator and the repaired inner bound"),
    "X02": ("X", "LM-B", "diagnostic: a nonuniform soft estimate does not certify a uniform bound"),
})
CLASS_ORDER = "PCVWRXGD"
REGISTRY = dict(sorted(REGISTRY.items(), key=lambda kv: (CLASS_ORDER.index(kv[0][0]), kv[0])))
LABELS = [f"LC{i}" for i in range(1, 13)] + [f"LA{i}" for i in range(1, 6)] + [f"LB{i}" for i in range(1, 6)] + [f"LM{i}" for i in range(1, 21)]
FAULT_TARGETS = {
    "transverse-projector": "C01", "packet-formfactor": "W01",
    "lb-initial-state": "C06", "lb-middle-residue": "V07",
    "photon-as-total": "R01", "pec-tau-power": "R02",
    "la-threshold": "R03", "doc-hash": "G01",
    "doc-equation": "G02", "doc-table": "G03", "doc-ledger": "G04",
    "moving-current-identity": "C11", "rest-ir-for-packet": "R04",
    "uniform-plateau": "R05", "photon-total-moving": "W04",
    "pec-logmoment-only": "W06", "angular-nodes-8": "V16",
    "doc-vocabulary": "G04", "doc-round": "G04", "doc-version": "G05",
}
FAULT_TARGETS.update({"pec-dini-factor":"C16", "layer-scale":"V19", "tail-power":"C18", "measurement-delete-before":"W08"})
FAULT_TARGETS.update({"uniform-prefactor":"C20", "photon-half-weight":"V21",
                      "soft-denominator":"W10", "doc-constant":"G02",
                      "fixed-frequency-kernel":"C21"})
QUALIFICATION = "PASS"
RESEARCH_GRADE = "3"
CANDIDATE_GRADE = "NONE"
TARGET_GRADE = "4"
NOVELTY = "PER-CLAIM: LM-D/LM-L/LM-P NEW; LM-B/LM-T/LM-A/LM-R EXTENDED; LM-Q EXTENDED; LM-K/LM-S/LM-E/LC SPECIALIZED; LA OPEN-NOVELTY (appendix only)"
ROLE = "RESEARCH PAPER / SUPPORT-METHOD"
AUDIT_ROUNDS = [
    {"round": 1, "audited_version": "1.0", "response_version": "1.1", "prefix": "A", "findings": 8, "kind": "external audit"},
    {"round": 2, "audited_version": "1.1", "response_version": "1.2", "prefix": "S", "findings": 6, "kind": "author-side scope corrections"},
    {"round": 3, "audited_version": "1.2", "response_version": "1.3", "prefix": "F", "findings": 5, "kind": "external audit"},
    {"round": 4, "audited_version": "1.2-audit", "response_version": "1.3", "prefix": "M", "findings": 8, "kind": "meta-audit of the v1.2 audit"},
]
AUDIT_ROUNDS.append({"round":5,"audited_version":"1.3","response_version":"1.4","prefix":"Q","findings":4,"kind":"targeted audit and research integration"})
AUDIT_ROUNDS.append({"round":6,"audited_version":"1.4-A/B","response_version":"1.5","prefix":"U","findings":7,"kind":"cross-lineage B comparison; low-independence A integration review"})
ALLOWED = {"qualification": {"PASS", "HOLD", "FAIL"}, "research_grade": {"1", "2", "3", "4", "5", "UNASSESSED"},
           "candidate_grade": {"3", "4", "5", "NONE"}, "target_grade": {"1", "2", "3", "4", "5"}}
STALE_TOKENS = ["PENDING-INDEPENDENT-AUDIT", "4-CANDIDATE-NOT-CERTIFIED", "EXTENDED-CANDIDATE"]
STALE_EXEMPT = ["v1.2", "v1.1", "v1.0", "철회", "대체", "superseded", "SUPERSEDED", "이전", "과거", "STALE", "G05"]
FAULT = None
PAPER = None
TESTS = {}


def test(row):
    def register(fn):
        TESTS[row] = fn
        return fn
    return register


def dependencies():
    global np, sp, mp, quad, expm, brentq, ive
    import numpy as np
    import sympy as sp
    import mpmath as mp
    from scipy.integrate import quad
    from scipy.linalg import expm
    from scipy.optimize import brentq
    from scipy.special import ive
    mp.mp.dps = 50


def weight(z, family, a=1.0):
    c, s = a*a/(a*a+z*z), a*z/(a*a+z*z)
    return {"free": c*c+s*s, "PEC": 2*s*s, "PMC": 2*c*c}[family]


def photon_frequency(om, z, mass=1.0):
    return om if FAULT == "photon-as-total" else (om*(om+2*mass)+z*z)/(2*(om+mass))


@lru_cache(maxsize=8192)
def spectrum(om, family, mass=1.0, a=1.0, photon=False):
    """J or J_gamma, e_ch=1; normal exponential density a exp(-a y)."""
    if om <= 0:
        return 0.0
    w = om+mass
    def f(z):
        physical_frequency = (om*(om+2*mass)+z*z)/(2*w)
        val = (om*om-z*z)*weight(z, family, a)*(1+z*z/physical_frequency**2)
        return val*(photon_frequency(om,z,mass) if photon else 1)
    return quad(f,0,om,epsabs=0,epsrel=3e-11,limit=300)[0]/(16*math.pi**2*w*w)


def polar_spectrum(om, family, mass=1.0, a=1.0):
    """Independent photon-radius/angular coordinate route; shares declared model."""
    w, aa = om+mass, om*(om+2*mass)
    def f(u):
        r = aa/(w+math.sqrt(w*w-aa*u*u))
        p2 = r*r*(1-u*u)
        ef = math.sqrt(mass*mass+p2)
        tensor = p2/(2*ef*(ef+mass))*(1+u*u)
        jac = 1+r*(1-u*u)/ef
        return r*weight(r*u,family,a)*tensor/jac
    return quad(f,-1,1,epsabs=0,epsrel=3e-11,limit=300)[0]/(8*math.pi**2)


@lru_cache(maxsize=32)
def gaussian(tau, family, route="reduced"):
    fn = spectrum if route == "reduced" else polar_spectrum
    # x>10 omitted; paper supplies an analytic tail bound for these parameters.
    return 2*math.pi*tau*quad(lambda x: fn(x/tau,family)*math.exp(-x*x),
                            0,10,epsabs=0,epsrel=2e-10,limit=150)[0]


def leading(tau, family):
    if family == "PEC":
        return 1/(21*math.pi*tau**(2 if FAULT == "pec-tau-power" else 4))
    return (2 if family == "PMC" else 1)/(20*math.pi*tau*tau)


def lb_matrix(v,w,d):
    return np.array([[0.,v,0.],[v,0.,w],[0.,w,d]])


def lb_initial():
    return 1 if FAULT == "lb-initial-state" else 0


def lb_data(v,w,d):
    eig, vec = np.linalg.eigh(lb_matrix(v,w,d))
    residues = vec[2,:]*vec[lb_initial(),:]
    if FAULT == "lb-middle-residue":
        residues[1] *= -1
    gaps = np.diff(eig)
    return eig,residues,4*v*v*w*w/(gaps[0]*gaps[1])**2


def la_exists(l,s):
    return s >= l+1.5 if FAULT == "la-threshold" else s > l+1.5


def la_h(l,x):
    if x == 0:
        return l+1.5
    nu = l+.5
    return nu+1+x/2*(ive(nu+1,x)/ive(nu,x)+ive(nu+2,x)/ive(nu+1,x))


def la_root(l,s):
    if not la_exists(l,s):
        return None
    return brentq(lambda x: la_h(l,x)-s,0,s,xtol=2e-13,rtol=1e-14)


def la_energy(l,s,c=1.):
    x = la_root(l,s)
    return None if x is None else math.sqrt(1-(c*x/s)**2)  # m=1


@test("C01")
def rest_tensor():
    px,py,z,m,ef = sp.symbols("px py z m ef",real=True)
    sx,sy,sz = sp.Matrix([[0,1],[1,0]]),sp.Matrix([[0,-sp.I],[sp.I,0]]),sp.diag(1,-1)
    pi, pf = (sp.eye(2)+sz)/2,(sp.eye(2)+(-px*sx-py*sy+m*sz)/ef)/2
    sig,p = [sx,sy],[px,py]
    t = sp.Matrix(2,2,lambda a,b:sp.simplify(sp.trace(pf*sig[a]*pi*sig[b])))
    if FAULT == "transverse-projector":
        proj = sp.Matrix(2,2,lambda a,b:1-p[a]*p[b]/(px*px+py*py))
    else:
        proj = sp.Matrix(2,2,lambda a,b:int(a==b)-p[a]*p[b]/(px*px+py*py+z*z))
    contraction = sum(proj[a,b]*t[a,b] for a in range(2) for b in range(2))
    target = (1-m/ef)/2*(1+z*z/(px*px+py*py+z*z))
    exact = (1-m/ef)/2*sp.Matrix([[1,-sp.I],[sp.I,1]])
    return (t-exact).applyfunc(sp.simplify)==sp.zeros(2) and sp.simplify(contraction-target)==0, {"tensor":str(t),"difference":str(sp.factor(contraction-target))}


@test("C02")
def moving_tensor():
    th = sp.symbols("th",real=True)
    vx,vy,vz = sp.symbols("vx vy vz",real=True)
    sig = [sp.Matrix([[0,1],[1,0]]),sp.Matrix([[0,-sp.I],[sp.I,0]]),sp.diag(1,-1)]
    n = [sp.cos(th),sp.sin(th)]
    pi = (sp.eye(2)+vx*sig[0]+vy*sig[1]+vz*sig[2])/2
    pf = (sp.eye(2)-n[0]*sig[0]-n[1]*sig[1])/2
    t = sum((int(a==b)-n[a]*n[b])*sp.trace(pf*sig[a]*pi*sig[b]) for a in range(2) for b in range(2))
    target = (1+vx*n[0]+vy*n[1])/2
    diff = sp.trigsimp(sp.expand(t-target))
    integ = sp.integrate(sp.expand_trig(sp.simplify(t)),(th,0,2*sp.pi))
    return diff==0 and sp.simplify(integ-sp.pi)==0, {"contracted_limit":str(target),"angular_integral":str(integ)}


@test("C03")
def shell_identities():
    om,m,z = sp.symbols("om m z",positive=True)
    w = om+m
    ef, photon = (w*w+m*m-z*z)/(2*w),(w*w-m*m+z*z)/(2*w)
    p2 = ef*ef-m*m
    # Original p integral divided by |d(E_f+omega)/dp| = p W/(E_f omega).
    reduced = sp.simplify((1-m/ef)/2*ef/w)
    target = (om*om-z*z)/(4*w*w)
    diffs = [sp.factor(ef+photon-w),sp.factor(photon**2-p2-z*z),sp.factor(reduced-target)]
    return all(x==0 for x in diffs), {"identity_residuals":list(map(str,diffs))}


@test("C04")
def ir_integrals():
    u = sp.symbols("u",real=True)
    free = sp.integrate((1-u*u)*(1+u*u),(u,-1,1))/32
    pec = sp.integrate(2*u*u*(1-u*u)*(1+u*u),(u,-1,1))/32
    return free==sp.Rational(1,20) and pec==sp.Rational(1,42), {"free_coefficient_without_e2_pi2_M2":str(free),"PEC_without_d2":str(pec)}


@test("C05")
def photon_algebra():
    om,m,z = sp.symbols("om m z",positive=True)
    f = photon_frequency(om,z,m)
    low = sp.factor(f-om/2)
    high = sp.factor(om-f)
    limit = sp.limit(f/om,om,sp.oo)
    return sp.simplify(low-(om*m+z*z)/(2*(om+m)))==0 and sp.simplify(high-(om*om-z*z)/(2*(om+m)))==0 and limit==sp.Rational(1,2), {"omega_minus_half":str(low),"Omega_minus_omega":str(high),"fixed_z_limit":str(limit)}


@test("C06")
def lb_resolvent():
    v,w,d,z = sp.symbols("v w d z")
    h = sp.Matrix([[0,v,0],[v,0,w],[0,w,d]])
    p = (z*sp.eye(3)-h).det()
    ans = (z*sp.eye(3)-h).inv()[2,lb_initial()]
    expected = z**3-d*z*z-(v*v+w*w)*z+d*v*v
    return sp.expand(p-expected)==0 and sp.simplify(ans-v*w/p)==0, {"basis":"(e,g,l)","initial_index":lb_initial(),"resolvent":str(sp.factor(ans)),"polynomial":str(p)}


@test("C07")
def lb_polynomial():
    x = sp.symbols("x",real=True)
    # Residues for eigenvalues (-2,1,3): sqrt(6)*(1/15,-1/6,1/10).
    a = [sp.sqrt(6)/15,-sp.sqrt(6)/6,sp.sqrt(6)/10]
    lam = [-2,1,3]
    pol = sum(q*q for q in a)+sum(2*a[i]*a[j]*sp.chebyshevt(abs(lam[i]-lam[j]),x) for i in range(3) for j in range(i+1,3))
    fact = sp.Rational(2,75)*(x-1)**2*(48*x**3+96*x*x+64*x+17)
    roots = [-1,1,sp.Rational(-1,2),(-1-sp.sqrt(5))/4,(-1+sp.sqrt(5))/4]
    vals = [sp.simplify(pol.subs(x,r)) for r in roots]
    maximum = (5+sp.sqrt(5))/12
    ok = sp.expand(pol-fact)==0 and sp.expand(sp.diff(pol,x)-sp.Rational(4,5)*(x-1)*(2*x+1)*(4*x*x+2*x-1))==0
    ok = ok and any(sp.simplify(v-maximum)==0 for v in vals) and all(sp.simplify(maximum-v).is_nonnegative for v in vals)
    return ok, {"polynomial":str(fact),"critical_and_endpoint_values":list(map(str,vals)),"max":str(maximum)}


@test("C08")
def la_determinant():
    f,g,r,b,s = sp.symbols("f g r b s")
    k = sp.Matrix([[-s*f,b*r*f+g],[f-b*r*g,-s*g]])
    expected = -b*(b*(1-r*r)*f*g+r*(f*f-g*g))
    residual = sp.expand(k.det()-expected).subs(s*s,1-b*b).expand()
    return residual==0, {"boundary_matrix":str(k),"determinant_factor":str(expected),"residual":str(residual)}


@test("C09")
def la_onset_algebra():
    l,m,c = sp.symbols("l m c",positive=True)
    coeff = sp.simplify((1/(2*l+3)+1/(2*l+5))/2)
    expected = (2*l+4)/((2*l+3)*(2*l+5))
    threshold = (l+sp.Rational(3,2))/(m*c)
    slope = sp.simplify(c/(2*coeff*threshold**2))
    target = m*m*c**3*(2*l+5)/((2*l+3)*(l+2))
    return sp.simplify(coeff-expected)==0 and sp.simplify(slope-target)==0, {"x2_coefficient":str(coeff),"onset_minus_E_prime":str(slope),"scope":"recurrence small-x algebra; not a global Bessel inequality proof"}


@test("C10")
def gaussian_moments():
    x = sp.symbols("x",positive=True)
    vals = [sp.integrate(x**n*sp.exp(-x*x),(x,0,sp.oo)) for n in [3,5]]
    return vals==[sp.Rational(1,2),sp.Integer(1)], {"moments":list(map(str,vals))}


@test("V01")
def coordinate_comparison():
    errors=[]
    for mass,a in [(1.,1.),(.7,1.9),(2.3,.4)]:
        for om in [.07,.8,4.2]:
            for family in ["free","PEC","PMC"]:
                j = spectrum(om,family,mass,a)
                errors.append(abs(j-polar_spectrum(om,family,mass,a))/j)
    return max(errors)<2e-9, {"points":len(errors),"max_relative_error":max(errors),"tolerance":2e-9}


@test("V02")
def weight_integrals():
    vals = {f:2*quad(lambda z:weight(z,f),0,np.inf,epsabs=0,epsrel=3e-11)[0] for f in ["free","PEC","PMC"]}
    return max(abs(v/math.pi-1) for v in vals.values())<2e-10, {"integrals":vals,"expected":math.pi,"scope":"a=1 exponential only"}


@test("V03")
def uv_samples():
    plateau = 1/(32*math.pi)
    vals = {f:spectrum(1000.,f)/plateau for f in ["free","PEC","PMC"]}
    ratios = {str(om):spectrum(om,"free",photon=True)/(om*spectrum(om,"free")) for om in [1.,10.,100.,1000.]}
    return max(abs(x-1) for x in vals.values())<.004 and abs(ratios["1000.0"]-.5)<.002, {"plateau_ratios_at_1000":vals,"photon_total_ratios":ratios,"finite_sample_tolerance":.004}


@test("V04")
def ir_samples():
    om=1e-4
    expected={"free":om**3/(20*math.pi**2),"PEC":om**5/(42*math.pi**2),"PMC":om**3/(10*math.pi**2)}
    ratios={f:spectrum(om,f)/v for f,v in expected.items()}
    return max(abs(v-1) for v in ratios.values())<4e-4, {"Omega":om,"ratios":ratios,"tolerance":4e-4}


def numeric_table():
    return {f:[spectrum(1.,f),gaussian(1.,f),gaussian(1000.,f),gaussian(1000.,f)/leading(1000.,f)] for f in ["free","PEC","PMC"]}


@test("V05")
def gaussian_table():
    data=numeric_table()
    errors=[abs(gaussian(1.,f)-gaussian(1.,f,"polar"))/gaussian(1.,f) for f in data]
    return max(errors)<2e-8 and all(v[1]>0 and .99<v[3]<1.01 for v in data.values()), {"table":data,"route_max_relative_error":max(errors),"tolerance":2e-8}


@test("V06")
def sharp_doubling():
    cutoff=1000.
    values={}
    expected={"total":2/(32*math.pi)*math.log(2),"photon":1/(32*math.pi)*math.log(2)}
    for name in expected:
        def f(om):
            return 2*(spectrum(om,"free",photon=True)/om**2 if name=="photon" else spectrum(om,"free")/om)
        mean=quad(f,cutoff,2*cutoff,epsabs=1e-11,epsrel=2e-9)[0]
        oscillatory=quad(f,cutoff,2*cutoff,weight="cos",wvar=1.,epsabs=1e-10,epsrel=2e-9)[0]
        values[name]=mean-oscillatory
    errors={k:abs(values[k]/expected[k]-1) for k in values}
    return max(errors.values())<.006, {"T":1,"Lambda":cutoff,"increments":values,"asymptotic_increments":expected,"relative_errors":errors,"tolerance":.006}


@test("V07")
def lb_cross_route():
    errors,excess=[],[]
    for v,w,d in [(1.,2.,0.),(math.sqrt(3),math.sqrt(2),2.),(1.,.1,1.),(.7,1.3,-2.)]:
        eig,a,bound=lb_data(v,w,d)
        for t in [0.,.17,1.,2.7,7.3]:
            amp=np.sum(a*np.exp(-1j*eig*t))
            exact=expm(-1j*lb_matrix(v,w,d)*t)[2,0]
            errors.append(float(abs(amp-exact)))
            excess.append(float(abs(exact)**2-bound))
    return max(errors)<1e-12 and max(excess)<1e-12, {"points":len(errors),"max_amplitude_error":max(errors),"max_bound_excess":max(excess),"tolerance":1e-12}


@test("V08")
def lb_asymptotics():
    resonance={str(z):lb_data(1.,1e-5,1+z*1e-5)[2]*(z*z+2) for z in [-2.,0.,2.]}
    far=lb_data(1.,.7,1000.)[2]*1000.**2/.7**2
    return max(abs(x-1) for x in resonance.values())<2e-4 and abs(far-1)<.005, {"resonance_ratios":resonance,"far_detuned_ratio":float(far),"scope":"finite points; uniform asymptotics are proved in paper"}


@test("V09")
def la_cross_route():
    errors=[]
    for l,s in [(0,2.),(0,5.),(1,3.),(2,7.),(4,8.)]:
        x=la_root(l,s)
        nu=mp.mpf(l)+mp.mpf("0.5")
        def f(xx):
            r=mp.besseli(nu+1,xx)/mp.besseli(nu,xx)
            return xx/2*(r+1/r)-s
        root=mp.findroot(f,(mp.mpf(x)*mp.mpf("0.98"),mp.mpf(x)*mp.mpf("1.02")))
        errors.append(abs(x-float(root)))
    return max(errors)<2e-11, {"points":len(errors),"mpmath_dps":mp.mp.dps,"max_absolute_root_error":max(errors),"tolerance":2e-11}


@test("V10")
def la_samples():
    monotonic=[];order=[];slopes={}
    for c in [.4,1.]:
        for l in [0,1,2]:
            es=[la_energy(l,s,c) for s in [l+2.,l+3.,l+5.]]
            monotonic.append(es[0]>es[1]>es[2])
            order.append(la_energy(l,l+4.,c)<la_energy(l+1,l+4.,c))
            eps=1e-5
            slope=(1-la_energy(l,l+1.5+eps,c))/(eps/c)
            predicted=c**3*(2*l+5)/((2*l+3)*(l+2))
            slopes[f"{l},{c}"]=slope/predicted
    return all(monotonic+order) and max(abs(v-1) for v in slopes.values())<2e-5, {"minus_E_prime_ratios_m1":slopes,"scope":"six branch/c samples; no global proxy proof"}


def packet_inclusive():
    sig=[np.array([[0,1],[1,0]],complex),np.array([[0,-1j],[1j,0]],complex),np.diag([1.,-1.])]
    def proj(k):
        ef=math.sqrt(1+k[0]**2+k[1]**2)
        return (np.eye(2)+(k[0]*sig[0]+k[1]*sig[1]+sig[2])/ef)/2
    p=np.array([3.,0.]);trans=np.eye(2)-np.outer(p,p)/10. # z=1, omega^2=10
    def f(y,x):
        initial=proj([x,y]);final=proj(np.array([x,y])-p)
        return float(sum(trans[a,b]*np.trace(final@sig[a]@initial@sig[b]) for a in range(2) for b in range(2)).real)/4
    val=quad(lambda x:quad(lambda y:f(y,x),-1,1,epsabs=1e-11)[0],-1,1,epsabs=1e-11)[0]
    # Compact support [-1,1]^2 and shift (3,0) have zero overlap.
    overlap_area=max(0.,min(1.,1.+3)-max(-1.,-1.+3))*2
    return val*(overlap_area/4)**2 if FAULT=="packet-formfactor" else val


@test("W01")
def packet_witness():
    x,y=sp.symbols("x y")
    norm=sp.integrate(sp.Rational(1,4),(x,-1,1),(y,-1,1))
    shifted=sp.integrate(sp.Rational(1,4),(x,-4,-2),(y,-1,1))
    overlap=sp.Rational(1,4)*max(0,min(1,-2)-max(-1,-4))*2
    val=packet_inclusive()
    return norm==1 and shifted==1 and overlap==0 and val>0.01, {"packet":"phi(k)=1/2 on [-1,1]^2; zero elsewhere","p":[3,0],"z":1,"norm2":str(norm),"shifted_norm2":str(shifted),"exclusive_overlap":str(overlap),"inclusive_current_weight":val}


@test("W02")
def retired_basis_witness():
    h=np.array([[0.,1.,2.],[1.,0.,0.],[2.,0.,0.]])
    wrong=float(abs(expm(-1j*h*math.pi/(2*math.sqrt(5)))[2,0])**2)
    corrected=float(abs(expm(-1j*lb_matrix(1,2,0)*math.pi/math.sqrt(5))[2,0])**2)
    return wrong>16/25 and abs(wrong-.8)<1e-13 and abs(corrected-16/25)<1e-13, {"retired_statement_probability":wrong,"retired_bound":16/25,"corrected_endpoint_probability":corrected}


@test("W03")
def rational_witness():
    t=math.acos((-1+math.sqrt(5))/4)
    val=float(abs(expm(-1j*lb_matrix(math.sqrt(3),math.sqrt(2),2)*t)[2,0])**2)
    exact=(5+math.sqrt(5))/12
    return abs(val-exact)<1e-13 and exact<2/3, {"time":t,"P":val,"max_from_C07":exact,"envelope":2/3,"gap_ratio":"3/2"}


@test("R01")
def photon_regression():
    ratio=spectrum(1000.,"free",photon=True)/(1000*spectrum(1000.,"free"))
    return .500<ratio<.502, {"spectral_energy_ratio":ratio,"acceptance_interval":[.500,.502]}


@test("R02")
def pec_regression():
    raw=gaussian(1000.,"PEC");ratio=raw/leading(1000.,"PEC")
    return .99<ratio<1.01, {"raw_R":raw,"R_over_mode_leading_term":ratio}


@test("R03")
def threshold_regression():
    rejected=[la_root(l,l+1.5) is None for l in [0,1,4]]
    return all(rejected), {"threshold_equality_rejected":rejected,"l":[0,1,4]}


# ---------------------------------------------------------------- moving-packet sector (LM)
_NODES = {}


def gl_nodes(n):
    if FAULT == "angular-nodes-8" and n == 128:
        n = 8
    if n not in _NODES:
        _NODES[n] = np.polynomial.legendre.leggauss(n)
    return _NODES[n]


def weight_array(z, family, a=1.0):
    c, s = a*a/(a*a+z*z), a*z/(a*a+z*z)
    return {"free": c*c+s*s, "PEC": 2*s*s, "PMC": 2*c*c}[family]


def j0_numerator(e, ef, kk, m):
    """4 e ef |j0|^2 / 2 ; fault flips the sign of the mass term."""
    return e*ef+kk+(-m*m if FAULT == "moving-current-identity" else m*m)


def tensor_trace(kx, px, py, z, m):
    """Symmetric Pauli-trace contraction for k=(kx,0); does not use LM1."""
    e = np.sqrt(kx*kx+m*m); fx, fy = kx-px, -py; ef = np.sqrt(fx*fx+fy*fy+m*m)
    w2 = px*px+py*py+z*z; bx = kx/e; cx, cy = fx/ef, fy/ef
    cb = cx*bx+m*m/(e*ef)
    cpb = cx*bx-(cx*px+cy*py)*(px*bx)/w2
    return 0.5*((1-cb)*(2-(px*px+py*py)/w2)+2*cpb)


def tensor_cov(kx, px, py, z, m):
    """LM1: (K.Kf-3M^2)/(2EEf) + |j0|^2 Omega(2 omega-Omega)/omega^2."""
    e = np.sqrt(kx*kx+m*m); fx, fy = kx-px, -py; ef = np.sqrt(fx*fx+fy*fy+m*m)
    w = np.sqrt(px*px+py*py+z*z); om = ef+w-e; kk = kx*fx
    return (e*ef-kk-3*m*m)/(2*e*ef)+j0_numerator(e, ef, kk, m)/(2*e*ef)*om*(2*w-om)/(w*w)


def moving_polar(om, kap, family, mass=1.0, a=1.0, nt=400, nphi=96):
    """Route 1: LM2 photon-polar route, closed-form photon root, e_ch=1, k=(kap,0)."""
    e = math.hypot(kap, mass); n = om*(2*e+om)
    xt, wt = gl_nodes(nt); t = (xt+1)/2; wt = wt/2
    mu = 1-2*t*t; jac = 4*t*wt
    xp, wp = gl_nodes(nphi); phi = (xp+1)*math.pi/4; wphi = wp*math.pi/4
    MU, PH = np.meshgrid(mu, phi, indexing="ij"); W = np.outer(jac, wphi)
    st = np.sqrt(np.clip(1-MU*MU, 0, None)); ny = st*np.cos(PH); u = st*np.sin(PH)
    d = e+om-kap*MU; rd = np.sqrt(d*d-u*u*n)
    w = n/(d+rd); px, py, z = w*MU, w*ny, w*u; ef = e+om-w
    f = w*weight_array(z, family, a)*tensor_trace(kap, px, py, z, mass)*ef/rd
    return float(4*np.sum(W*f)/(16*math.pi**3))


def tensor_stable(e, ef, w, om, z, m):
    """LM1 written with |Q^2|/2 = omega Omega-(Omega^2+z^2)/2 = K.K_f-M^2 (no large cancellations)."""
    q2h = w*om-(om*om+z*z)/2
    num = 2*e*ef-q2h+(-2*m*m if FAULT == "moving-current-identity" else 0.)
    return (q2h-2*m*m)/(2*e*ef)+num/(2*e*ef)*om*(2*w-om)/(w*w)


@lru_cache(maxsize=16384)
def moving_cov(om, kap, family, mass=1.0, a=1.0, photon=False, nodes=128):
    """Route 2: LM3 covariant two-body route; half-angle map; fixed Gauss-Legendre nodes in psi."""
    e = math.hypot(kap, mass); n = om*(2*e+om); s = mass*mass+n; rs = math.sqrt(s)
    g = (e+om)/rs; beta = kap/(e+om); zmax = n/(rs+mass)
    xp, wp = gl_nodes(nodes); psi = (xp+1)*math.pi/2; wpsi = wp*math.pi/2
    c2, s2 = np.cos(psi/2)**2, np.sin(psi/2)**2
    def inner(z):
        ws = (n+z*z)/(2*rs)
        ps = math.sqrt(max(0., (n-z*(2*mass+z))*(n+z*(2*mass-z))))/(2*rs)
        gap = g*g*z*z+ps*ps
        apb = g*(ws+beta*ps)
        w = apb/(c2+s2*apb*apb/gap)
        ef = e+om-w
        val = ef*tensor_stable(e, ef, w, om, z, mass)*w
        if photon:
            val = val*(om if FAULT == "photon-total-moving" else w)
        return 2*float(np.sum(wpsi*val))/math.sqrt(gap)
    edges = [0.]+[a*10.**j for j in range(-2, 9) if a*10.**j < zmax]+[zmax]
    total = sum(quad(lambda z: weight_array(z, family, a)*inner(z), lo, hi, epsabs=0, epsrel=1e-10, limit=400)[0]
                for lo, hi in zip(edges[:-1], edges[1:]))
    return 2*total/(16*math.pi**3*rs)


def angular_mean(om, kap, z, mass=1.0, photon=False):
    """Route 3 kernel: <E_f T>_theta* (or <omega E_f T>) in closed form.

    omega = a0 + b0 cos(theta*), <1/omega> = 1/sqrt(a0^2-b0^2), <1/omega^2> = a0/(a0^2-b0^2)^{3/2},
    <omega^2> = a0^2 + b0^2/2, a0^2-b0^2 = gamma_c^2 z^2 + p*^2. Reduction from the v1.2 audit
    (Appendix B), re-derived; the identity E_f T = reduced form is certified symbolically in C15.
    """
    O, k, Z, M = map(mp.mpf, (om,kap,z,mass))
    E = mp.sqrt(k*k+M*M); W = E+O; N = O*(2*E+O); s = M*M+N; rs = mp.sqrt(s); g = W/rs
    ws = (N+Z*Z)/(2*rs); p2 = ((N-Z*(2*M+Z))*(N+Z*(2*M-Z)))/(4*s)
    a0 = g*ws; b2 = (k*k/s)*p2; gap = g*g*Z*Z+p2
    C = (O*O+Z*Z)/2; A = 2*E*W+C; B0 = 2*E+O
    mm = -M*M if FAULT == "moving-current-identity" else M*M
    if photon:
        half = mp.mpf("0.5") if FAULT == "photon-half-weight" else mp.mpf(1)
        return float(half*(O*(a0*a0+b2/2)-(C+2*mm+2*B0*O)*a0+2*A*O+B0*O*O-A*O*O/mp.sqrt(gap))/(2*E))
    return float((O*a0-C-2*mm-2*B0*O+(2*A*O+B0*O*O)/mp.sqrt(gap)-A*O*O*a0/gap**mp.mpf("1.5"))/(2*E))


@lru_cache(maxsize=16384)
def moving_analytic(om, kap, family, mass=1.0, a=1.0, photon=False):
    """Route 3: analytic theta* average, adaptive quad in theta with z = a tan(theta). Returns (J, error_estimate)."""
    E = math.hypot(kap, mass); N = om*(2*E+om); rs = math.sqrt(mass*mass+N)
    zmax = N/(rs+mass); limit = math.atan(zmax/a)
    def integrand(theta):
        z = a*math.tan(theta)
        wdz = {"free": a, "PEC": 2*a*math.sin(theta)**2, "PMC": 2*a*math.cos(theta)**2}[family]
        return wdz*angular_mean(om, kap, z, mass, photon)
    ans, err = quad(integrand, 0, limit, epsabs=0, epsrel=1e-11, limit=400)
    return ans/(4*math.pi**2*rs), err/(4*math.pi**2*rs)


def uniform_constant():
    return 17 if FAULT == "uniform-prefactor" else 18


def softform_bound(om, E, mass=1.0, a=1.0):
    return om*(uniform_constant()*plateau(a)/mass+math.log(14*E/mass)/math.pi**2)


def plateau(a=1.0):
    return a/2/(16*math.pi)


def soft_coefficient(v, family, d=1.0):
    """LM6: (power, coefficient) with e_ch=1."""
    L = math.atanh(v)
    if family == "PEC":
        return 3, d*d*(3*v-2*v**3-3*(1-v*v)*L)/(3*math.pi**2*v**3*(1-v*v))
    return 1, (2 if family == "PMC" else 1)*(L/v-1)/(2*math.pi**2)


def adiabatic_prediction(v, family, tau):
    """LM7 single-momentum Gaussian limit (M=a=d=1)."""
    if FAULT == "rest-ir-for-packet":
        return leading(tau, family)
    power, c = soft_coefficient(v, family)
    return math.pi*c if power == 1 else math.pi*c/tau**2


def pec_dominator(E, mass=1.0, a=1.0):
    """H(k) of LM-A' (e_ch=1, d=1/a): J_PEC(Omega;k)/Omega^3 <= H(k) for all Omega>0."""
    d = 1/a
    return 3*d*d*E*E/(2*math.pi**2*mass*mass)+uniform_constant()*plateau(a)/mass**3


def phi_closed(lam):
    return 1.0 if FAULT == "uniform-plateau" else 4*(1+lam)-(4*lam+7)*math.sqrt(lam/(lam+2))


def ellipse_integral(lam):
    def f(al):
        c = math.cos(al); r1 = lam*(2+lam)/(2*(1+lam-c)); r2 = 1+lam-r1
        return (0.5+(1-2*c*c+r1*c)/(2*r2))*r2/(1+lam-c)
    return 4*quad(f, 0, math.pi, epsabs=0, epsrel=1e-13, limit=400)[0]/math.pi


@lru_cache(maxsize=512)
def gaussian_moving(tau, kap, family, route="analytic"):
    x, wx = gl_nodes(64); x = (x+1)*3.5; wx = wx*3.5
    fn = (lambda om: moving_analytic(om, kap, family)[0]) if route == "analytic" else (lambda om: moving_cov(om, kap, family))
    return 2*math.pi*tau*sum(float(wi)*fn(float(xi)/tau)*math.exp(-float(xi)**2) for xi, wi in zip(x, wx))


@lru_cache(maxsize=8)
def packet_response(tau, sigma, family):
    """|phi(k)|^2=exp(-k^2/sigma^2)/(pi sigma^2); Gauss-Laguerre in y=k^2/sigma^2."""
    y, wy = np.polynomial.laguerre.laggauss(24)
    resp = sum(float(wi)*gaussian_moving(tau, sigma*math.sqrt(float(yi)), family, "covariant") for yi, wi in zip(y, wy))
    pred = sum(float(wi)*adiabatic_prediction(sigma*math.sqrt(float(yi))/math.hypot(sigma*math.sqrt(float(yi)), 1.), family, tau) for yi, wi in zip(y, wy))
    return resp, pred


def heavy_tail_packet_response(tau, family="PEC", nodes=24):
    """|phi(k)|^2 = 1/[pi(1+|k|^2)^2] (M=1): energy density 2/E^3 on E>=1; substitute E=1/t, t in (0,1)."""
    x, w = gl_nodes(nodes); t = (x+1)/2; wt = w/2
    total = 0.
    for ti, wi in zip(t, wt):
        E = 1/float(ti); kap = math.sqrt(max(E*E-1., 0.))
        total += float(wi)*2*float(ti)*gaussian_moving(tau, kap, family)
    return total


def moving_table():
    out = {}
    for kap, lam in [(1e3, 1.0), (1e4, 0.01), (1e5, 1e-3)]:
        e = math.hypot(kap, 1.)
        out[f"{kap:g},{lam:g}"] = [moving_analytic(lam*e, kap, "free")[0]/plateau(), phi_closed(lam)]
    return out


GRID = [((1., .1), (1., 1.), (1., 10.), (.3, 1.)), (0., .3, 1., 3., 10., 100., 1e3, 1e4, 1e5), (1e-3, 1e-2, .1, 1., 10., 100., 1e3, 1e4)]


@test("C11")
def moving_current_identity():
    kx, ky, px, py, m, e, ef, om, w = sp.symbols("kx ky px py m e ef om w", real=True)
    sx, sy, sz = sp.Matrix([[0, 1], [1, 0]]), sp.Matrix([[0, -sp.I], [sp.I, 0]]), sp.diag(1, -1)
    fx, fy = kx-px, ky-py; kk = kx*fx+ky*fy
    pi4 = e*sp.eye(2)+kx*sx+ky*sy+m*sz     # 2E P_i
    pf4 = ef*sp.eye(2)+fx*sx+fy*sy+m*sz    # 2E_f P_f
    first = sp.expand((pf4*sx*pi4*sx).trace()+(pf4*sy*pi4*sy).trace()-(pf4*pi4).trace()-2*(e*ef-kk-3*m*m))
    pdot = px*sx+py*sy
    second = sp.expand((pf4*pdot*pi4*pdot).trace()-(ef-e)**2*(pf4*pi4).trace())
    second = sp.expand(sp.rem(second, e**2-(kx*kx+ky*ky+m*m), e))
    second = sp.expand(sp.rem(second, ef**2-(fx*fx+fy*fy+m*m), ef))
    third = sp.expand((pf4*pi4).trace()/2-j0_numerator(e, ef, kk, m))
    decomposition = sp.simplify(1-(om-w)**2/w**2-om*(2*w-om)/w**2)
    ok = first == 0 and second == 0 and third == 0 and decomposition == 0
    return ok, {"sum_trace_minus_density_residual": str(first), "current_conservation_residual": str(second),
                "j0_numerator_residual": str(third), "decomposition_residual": str(decomposition),
                "scope": "trace identities with unnormalized projectors 2E P; E^2 and E_f^2 relations reduced by polynomial remainder"}


@test("C12")
def soft_integrals():
    v, x, mu, ph = sp.symbols("v x mu ph", positive=True)
    L = (sp.log(1+v)-sp.log(1-v))/2
    q = v*v-1+2*x-x*x
    sub2 = sp.simplify(((1-mu**2)/(1-v*mu)**2*(-1/v)).subs(mu, (1-x)/v)-(-q/(v**3*x**2)))
    sub4 = sp.simplify(((1-mu**2)**2/(1-v*mu)**4*(-1/v)).subs(mu, (1-x)/v)-(-q**2/(v**5*x**4)))
    G2 = sp.integrate(sp.expand(-q/(v**3*x**2)), x); G4 = sp.integrate(sp.expand(-q**2/(v**5*x**4)), x)
    I2 = G2.subs(x, 1-v)-G2.subs(x, 1+v); I4 = G4.subs(x, 1-v)-G4.subs(x, 1+v)
    c2 = 4*(L-v)/v**3; c4 = 8*(3*v-2*v**3-3*(1-v*v)*L)/(3*v**5*(1-v*v))
    d2 = sp.simplify(sp.expand_log(I2-c2, force=True)); d4 = sp.simplify(sp.expand_log(I4-c4, force=True))
    free = sp.simplify(v*v*c2/(8*sp.pi**2)-(L/v-1)/(2*sp.pi**2))
    pec = sp.simplify(v*v*c4/(8*sp.pi**2)-(3*v-2*v**3-3*(1-v*v)*L)/(3*sp.pi**2*v**3*(1-v*v)))
    azimuth = sp.integrate(sp.sin(ph)**2, (ph, 0, 2*sp.pi))
    lim2, lim4 = sp.limit(c2, v, 0), sp.limit(c4, v, 0)
    gam = sp.simplify(sp.expand_log(L-sp.log((1+v)/(sp.sqrt(1-v)*sp.sqrt(1+v))), force=True))
    ok = all(t == 0 for t in [sub2, sub4, d2, d4, free, pec, gam]) and azimuth == sp.pi and lim2 == sp.Rational(4, 3) and lim4 == sp.Rational(16, 15)
    return ok, {"I2": "4(artanh v - v)/v^3", "I4": "8[3v-2v^3-3(1-v^2)artanh v]/(3v^5(1-v^2))",
                "residuals": list(map(str, [sub2, sub4, d2, d4, free, pec, gam])), "azimuthal_sin2": str(azimuth),
                "v_to_0": [str(lim2), str(lim4)], "scope": "antiderivative evaluation for 0<v<1; DCT limit is manuscript proof"}


@test("C13")
def plateau_exact():
    t, lam, r = sp.symbols("t lam r", positive=True)
    co = (1-t**2)/(1+t**2); si = 2*t/(1+t**2)
    r1 = lam*(2+lam)/(2*(1+lam-co)); r2 = 1+lam-r1
    focal = sp.simplify(r2**2-(1+r1**2-2*r1*co))
    jac = sp.simplify((1+(r1-co)/r2)-(1+lam-co)/r2)
    cb = (1-r1*co)/r2; cp = (co-r1)/r2
    tensor = sp.Rational(1, 2)+(1-2*co**2+r1*co)/(2*r2)
    trace = sp.simplify(sp.Rational(1, 2)*(1-cb)+cb-cp*co-tensor)
    f = sp.simplify(tensor*r2/(1+lam-co)*2/(1+t**2))
    target = (lam*t**2+lam+4*t**2)**2/((t**2+1)**2*(lam*t**2+lam+2*t**2)**2)
    reduction = sp.simplify(f-target)
    phi = 4*(1+lam)-(4*lam+7)*sp.sqrt(lam/(lam+2))
    exact = {}
    for qv, val in [(sp.Rational(1, 4), sp.Rational(7, 3)), (sp.Rational(1, 12), sp.Rational(43, 15))]:
        integ = sp.integrate(target.subs(lam, qv), (t, -sp.oo, sp.oo))
        exact[str(qv)] = [sp.simplify(2*integ/sp.pi-val) == 0, sp.simplify(phi.subs(lam, qv)-val) == 0]
    lim0 = sp.limit(phi, lam, 0, "+"); liminf = sp.limit(lam*(phi-1), lam, sp.oo)
    # stable form (v1.2 audit): with r = sqrt(lam/(lam+2)) in (0,1), Phi = r - 4 + 8/(1+r), strictly decreasing from 4 to 1.
    lam_r = 2*r*r/(1-r*r)
    stable = sp.simplify((4*(1+lam_r)-(4*lam_r+7)*r)-(r-4+8/(1+r)))
    dstable = sp.simplify(sp.diff(r-4+8/(1+r), r))   # 1 - 8/(1+r)^2 < 0 on (0,1)
    monotone = sp.simplify(dstable.subs(r, 1)) == -1 and sp.simplify(dstable.subs(r, 0)) == -7 and sp.solve(sp.Eq(dstable, 0), r) == [2*sp.sqrt(2)-1]
    ok = all(rr == 0 for rr in [focal, jac, trace, reduction, stable]) and all(all(v) for v in exact.values()) and lim0 == 4 and liminf == 1 and monotone
    return ok, {"residuals": list(map(str, [focal, jac, trace, reduction, stable])), "exact_lambda_checks": {k: list(map(bool, v)) for k, v in exact.items()},
                "Phi_0+": str(lim0), "lambda(Phi-1)_inf": str(liminf), "stable_form": "Phi = r-4+8/(1+r), r=sqrt(lam/(lam+2)); dPhi/dr=1-8/(1+r)^2 vanishes only at r=2sqrt2-1>1",
                "scope": "massless z=0 ellipse integral; the E->infinity limit is a manuscript proof; the range 1<Phi<4 is a property of the fixed-lambda limit, not a global finite-momentum bound"}


@test("C14")
def bound_kinematics():
    E, Om, M, z, dl, B, D, t = sp.symbols("E Om M z dl B D t", positive=True)
    s = M*M+2*E*Om+Om*Om; rs = sp.sqrt(s); N = Om*(2*E+Om); kap2 = E*E-M*M
    ids = {
        "P2_equals_s": sp.expand((E+Om)**2-kap2-s),
        "K_dot_P": sp.expand(E*(E+Om)-kap2-(M*M+E*Om)),
        "p0_over_gamma": sp.simplify((N/(2*rs))/((E+Om)/rs)-Om/2-E*Om/(2*(E+Om))),
        "zmax_value": sp.simplify((rs-M)-N/(rs+M)),
        "zmax_square": sp.expand(N-(rs-M)**2-(2*M*rs-2*M*M)),
        "gamma2_one_minus_beta2": sp.simplify(((E+Om)**2/s)*(1-kap2/(E+Om)**2)-1),
    }
    A = B+D; rho = sp.sqrt((A+B)/(A-B))
    cth = (1-rho**2*t**2)/(1+rho**2*t**2)
    ids["half_angle_jacobian"] = sp.simplify((2*rho/(1+rho**2*t**2))/(2/(1+t**2))*sp.sqrt(A**2-B**2)-(A+B*cth))
    positivity = sp.Poly(sp.expand((4*s-(M+Om)**2).subs(E, M+dl)), M, dl, Om).coeffs()
    # inner-half lower bound of the first Kallen factor (v1.2 audit check): for z=(R-M)/2, R^2-(M+z)^2-(R^2-M^2)/2 = (R-M)^2/4 >= 0
    R = sp.symbols("R", positive=True)
    inner = sp.expand((R*R-(M+(R-M)/2)**2)-(R*R-M*M)/2-(R-M)**2/4)
    ok = all(v == 0 for v in ids.values()) and all(c > 0 for c in positivity) and inner == 0
    return ok, {"residuals": {k: str(v) for k, v in ids.items()}, "4s-(M+Omega)^2_coefficients_E=M+dl": list(map(str, positivity)),
                "inner_half_shell_residual": str(inner),
                "scope": "local identities; the lower bound on p*(z) and the integrated inequalities are manuscript proofs"}


@test("C15")
def analytic_reduction_and_e2_bound():
    """Route-3 integrand identity and the rational constants of the LM-A' (E^2-moment) PEC bound."""
    E, W, O, w, z, M = sp.symbols("E W O w z M", positive=True)
    q = O*w-(O*O+z*z)/2; ef = W-w; A = 2*E*W+(O*O+z*z)/2; B0 = 2*E+O
    # E_f T with T from LM1 (stable form): T1=(q-2M^2)/(2EE_f), |j0|^2=(2EE_f-q)/(2EE_f)
    direct = (q-2*M*M)/(2*E)+(2*E*ef-q)/(2*E)*O*(2*w-O)/(w*w)
    reduced = (O*w-(O*O+z*z)/2-2*M*M-2*B0*O+(2*A*O+B0*O*O)/w-A*O*O/(w*w))/(2*E)
    identity = sp.factor(sp.simplify(direct-reduced))
    # angular means for omega=a0(1+t cos theta), 0<=t<1: <1/omega>=1/(a0 sqrt(1-t^2)), <1/omega^2>=1/(a0^2 (1-t^2)^{3/2}), <omega^2>=a0^2(1+t^2/2)
    # certified termwise: exact <cos^k> moments against the binomial series of the closed forms, through order t^12.
    t, th = sp.symbols("t th", positive=True)
    cosk = [sp.integrate(sp.cos(th)**k, (th, 0, 2*sp.pi))/(2*sp.pi) for k in range(13)]
    lhs1 = sum((-1)**k*t**k*cosk[k] for k in range(13)); lhs2 = sum((-1)**k*(k+1)*t**k*cosk[k] for k in range(13))
    rhs1 = sp.series(1/sp.sqrt(1-t*t), t, 0, 13).removeO(); rhs2 = sp.series((1-t*t)**sp.Rational(-3, 2), t, 0, 13).removeO()
    msq = sp.integrate((1+t*sp.cos(th))**2, (th, 0, 2*sp.pi))/(2*sp.pi)
    means = [sp.expand(lhs1-rhs1), sp.expand(lhs2-rhs2), sp.simplify(msq-(1+t*t/2))]
    # E^2-moment bound constants (LM-A'): B_PEC<=2d^2 z^2; T1<=omega Omega/(2EE_f); integrals over |z|<=z_m
    d, zm, u, v = sp.symbols("d zm u v", positive=True)
    i1 = sp.integrate(2*d*d*u*u, (u, -zm, zm))                     # 4 d^2 zm^3/3
    i2 = 2*sp.integrate(2*d*d*u*u*(O/u), (u, 0, zm))               # 2 d^2 Omega zm^2
    c1 = sp.Rational(1, 16)*sp.Rational(4, 3)                       # J1 <= e^2 d^2 Omega gamma_c N zm^3/(12 pi^2 E s)
    total = sp.Rational(1, 6)+sp.Rational(1, 2)                     # J1+J2 <= (2/3) e^2 d^2 Omega zm^2/pi^2
    final = total*sp.Rational(9, 4)                                 # zm <= 3 E Omega/(2M)  ->  (3/2) e^2 d^2 E^2 Omega^3/(pi^2 M^2)
    zm_gap = sp.factor(3*E*O-O*(2*E+O))                             # = Omega (E-Omega) >= 0 for Omega<=E
    q_gap = sp.simplify(O*w-q)                                       # = (Omega^2+z^2)/2 >= 0  (T1 <= omega Omega/(2EE_f))
    # Fatou side: (1-v^2) c_PEC(v) -> d^2/(3 pi^2), so c_PEC ~ d^2 E^2/(3 pi^2 M^2)
    cpec = d*d*(3*v-2*v**3-3*(1-v*v)*sp.atanh(v))/(3*sp.pi**2*v**3*(1-v*v))
    lim = sp.limit((1-v*v)*cpec, v, 1, dir="-")
    ok = identity == 0 and all(x == 0 for x in means) and sp.simplify(i1-sp.Rational(4, 3)*d*d*zm**3) == 0 and sp.simplify(i2-2*d*d*O*zm**2) == 0
    ok = ok and c1 == sp.Rational(1, 12) and total == sp.Rational(2, 3) and final == sp.Rational(3, 2) and zm_gap == O*(E-O) and q_gap == (O*O+z*z)/2 and lim == d*d/(3*sp.pi**2)
    return ok, {"EfT_identity_residual": str(identity), "angular_mean_residuals": list(map(str, means)),
                "z_integrals": [str(i1), str(i2)], "constants": {"J1_prefactor": str(c1), "J1+J2": str(total), "final": str(final)},
                "3EOmega-N": str(zm_gap), "omegaOmega-q": str(q_gap), "(1-v^2)c_PEC_limit": str(lim),
                "scope": "symbolic constants and identities of the LM-A' proof; the inequality chain itself is the manuscript proof (Section 5.6)"}


@test("V11")
def moving_routes():
    errs = []; errs3 = []
    for mass, a in [(1., 1.), (.7, 1.9)]:
        for kap in [.5, 2., 5.]:
            for om in [.05, 1., 8.]:
                for fam in ["free", "PEC", "PMC"]:
                    r2 = moving_cov(om, kap, fam, mass, a); r1 = moving_polar(om, kap, fam, mass, a); r3 = moving_analytic(om, kap, fam, mass, a)[0]
                    errs.append(abs(r2/r1-1)); errs3.append(max(abs(r3/r1-1), abs(r3/r2-1)))
    rest = [abs(moving_cov(om, 0., fam)/spectrum(om, fam)-1) for om in [.07, .8, 4.2] for fam in ["free", "PEC", "PMC"]]
    rest3 = [abs(moving_analytic(om, 0., fam)[0]/spectrum(om, fam)-1) for om in [.07, .8, 4.2] for fam in ["free", "PEC", "PMC"]]
    return max(errs) < 2e-9 and max(errs3) < 2e-9 and max(rest) < 2e-9 and max(rest3) < 2e-9, {
        "moving_points": len(errs), "max_relative_route1_vs_route2": max(errs), "max_relative_route3_vs_routes12": max(errs3),
        "rest_points": len(rest), "max_rest_reduction_difference_route2": max(rest), "max_rest_reduction_difference_route3": max(rest3), "tolerance": 2e-9}


@test("V12")
def moving_soft_samples():
    ratios = {}; ratios3 = {}
    for kap in [.5, 2.]:
        v = kap/math.hypot(kap, 1.)
        for fam in ["free", "PEC", "PMC"]:
            power, c = soft_coefficient(v, fam)
            ratios[f"{kap},{fam}"] = moving_cov(1e-4, kap, fam)/(c*1e-4**power)
            ratios3[f"{kap},{fam}"] = moving_analytic(1e-4, kap, fam)[0]/(c*1e-4**power)
    ok = max(abs(r-1) for r in ratios.values()) < 1e-3 and max(abs(r-1) for r in ratios3.values()) < 1e-3
    return ok, {"Omega": 1e-4, "ratios_route2": ratios, "ratios_route3": ratios3, "tolerance": 1e-3, "M=a=d": 1}


@test("V13")
def plateau_samples():
    closed = {str(l): abs(phi_closed(l)/ellipse_integral(l)-1) for l in [1e-4, 1e-2, .25, 1., 10., 1e3]}
    table = moving_table()
    large = {k: v[0]/v[1] for k, v in table.items()}
    return max(closed.values()) < 1e-10 and max(abs(r-1) for r in large.values()) < 3e-3, {
        "closed_vs_quadrature_relative_error": closed, "large_momentum_J_over_Jinf_over_Phi": large, "tolerances": [1e-10, 3e-3]}


@test("V14")
def uniform_grid():
    worst = (-1., None); minimum = 1.; count = 0; maxerr = 0.; soft = (-1., None)
    for mass, a in GRID[0]:
        for kap in GRID[1]:
            E = math.hypot(kap, mass)
            for om in GRID[2]:
                for fam in ["free", "PEC", "PMC"]:
                    j, err = moving_analytic(om, kap, fam, mass, a); r = j/plateau(a); count += 1
                    minimum = min(minimum, r); maxerr = max(maxerr, err/max(j, 1e-300))
                    if r > worst[0]:
                        worst = (r, [mass, a, kap, om, fam])
                    # soft form of LM-B(iv) used by LM-A: J <= Omega [18 J_inf/M + (||B||_inf/(2 pi^2)) log(14E/M)], ||B||_inf <= 2
                    rs = j/(om*(uniform_constant()*plateau(a)/mass+(2/(2*math.pi**2))*math.log(14*E/mass)))
                    if rs > soft[0]:
                        soft = (rs, [mass, a, kap, om, fam])
    return worst[0] <= uniform_constant() and minimum >= 0 and maxerr < 1e-8 and soft[0] <= 1, {"samples": count, "max_J_over_Jinf": worst[0], "argmax_[M,a,kappa,Omega,family]": worst[1],
                                                                 "min_J_over_Jinf": minimum, "max_relative_quadrature_error_estimate": maxerr, "proved_bound": uniform_constant(),
                                                                 "max_J_over_softform_bound": soft[0], "argmax_softform": soft[1],
                                                                 "scope": "finite grid (four (M,a) pairs x 9 momenta x 8 frequencies x 3 families); route 3; bounds are proved in manuscript; not an optimal-constant certificate"}


@test("V15")
def adiabatic_single():
    kap = 1.; v = kap/math.hypot(kap, 1.); out = {}
    for fam in ["free", "PMC", "PEC"]:
        for tau in [300., 3000.]:
            out[f"{fam},{tau:g}"] = gaussian_moving(tau, kap, fam)/adiabatic_prediction(v, fam, tau)
    ok = all(abs(out[f"{f},3000"]-1) < 2e-3 for f in ["free", "PMC", "PEC"])
    return ok, {"kappa": kap, "R_over_prediction": out, "tolerance_tau3000": 2e-3, "prediction": "pi c_B(v) (free/PMC), pi c_PEC(v)/tau^2", "route": "analytic"}


@test("V16")
def angular_convergence():
    """F05 repair: fixed-node route against node doubling and the analytic route at the grid extremum and printed table."""
    points = [(.1, 1e5, "PMC", 1., .1)]+[(lam*math.hypot(kap, 1.), kap, "free", 1., 1.) for kap, lam in [(1e3, 1.), (1e4, .01), (1e5, 1e-3)]]
    points += [(1e-2, 1e5, "PMC", 1., .1), (1e-3, 1e4, "free", 1., 1.)]   # two of the worst grid points found in the v1.4 meta-audit
    rows = {}; worst128 = 0.; worst256 = 0.; worstdbl = 0.
    for om, kap, fam, mass, a in points:
        r3, err = moving_analytic(om, kap, fam, mass, a)
        r128 = moving_cov(om, kap, fam, mass, a, nodes=128); r256 = moving_cov(om, kap, fam, mass, a, nodes=256)
        e128 = abs(r128/r3-1); e256 = abs(r256/r3-1); dbl = abs(r128/r256-1)
        worst128 = max(worst128, e128); worst256 = max(worst256, e256); worstdbl = max(worstdbl, dbl)
        rows[f"{om:g},{kap:g},{fam},{mass:g},{a:g}"] = {"route3": r3, "route3_error_estimate": err, "nodes128": r128, "nodes256": r256,
                                                        "rel_128_vs_route3": e128, "rel_256_vs_route3": e256, "node_doubling_estimate": dbl}
    ok = worst256 < 5e-8 and worst128 < 1e-5 and worstdbl < 1e-5
    return ok, {"points": rows, "max_rel_128_vs_route3": worst128, "max_rel_256_vs_route3": worst256, "max_node_doubling_estimate": worstdbl,
                "tolerances": {"256_vs_route3": 5e-8, "128_vs_route3": 1e-5, "node_doubling": 1e-5},
                "scope": "the 128-node route is accurate to ~1e-6 at large momentum/small frequency; printed 6-digit values are unaffected; route 3 supplies the printed table"}


@test("V17")
def pec_dominator_grid():
    """LM-A': J_PEC(Omega;k)/Omega^3 <= H(k) on a grid (evidence that the proved dominating function is not violated numerically)."""
    worst = (-1., None); worst_small = (-1., None); count = 0
    for mass, a in GRID[0]:
        for kap in GRID[1]:
            E = math.hypot(kap, mass); H = pec_dominator(E, mass, a); d = 1/a
            for om in [1e-3, 1e-2, .1, .3, 1., 3., 10., 100., 1e3, 1e4]:
                j = moving_analytic(om, kap, "PEC", mass, a)[0]; count += 1
                r = j/(om**3*H)
                if r > worst[0]:
                    worst = (r, [mass, a, kap, om])
                if om <= mass:
                    rs = j/(om**3*3*d*d*E*E/(2*math.pi**2*mass*mass))
                    if rs > worst_small[0]:
                        worst_small = (rs, [mass, a, kap, om])
    return worst[0] <= 1 and worst_small[0] <= 1, {"samples": count, "max_J_over_Omega3_H": worst, "max_J_over_Omega3_smallOmega_bound": worst_small,
                                                     "scope": "finite grid; H(k)=3 d^2 E^2/(2 pi^2 M^2)+18 J_inf/M^3 with e_ch=1; the bound is proved in Section 5.6"}


@test("W04")
def photon_exceeds_mismatch():
    e, ef, w = math.sqrt(10.), math.sqrt(5.), 1.
    om = ef+w-e
    tens = float(tensor_trace(3., 1., 0., 0., 1.))
    kap, small = 2., 1e-3
    ratio = moving_cov(small, kap, "free", photon=True)/(small*moving_cov(small, kap, "free"))
    ratio3 = moving_analytic(small, kap, "free", photon=True)[0]/(small*moving_analytic(small, kap, "free")[0])
    v = kap/math.hypot(kap, 1.)
    soft = quad(lambda m: (1-m*m)/(1-v*m)**3, -1, 1, epsrel=1e-12)[0]/quad(lambda m: (1-m*m)/(1-v*m)**2, -1, 1, epsrel=1e-12)[0]
    ok = w/om > 13 and tens > 0 and ratio > 1.2 and abs(ratio/soft-1) < 5e-3 and abs(ratio3/ratio-1) < 1e-8
    return ok, {"point": {"k": [3, 0], "p": [1, 0], "z": 0, "M": 1, "Omega": om, "omega": w, "omega_over_Omega": w/om, "tensor": tens},
                "integrated_kappa2_Omega0.001_Jgamma_over_OmegaJ": ratio, "route3_same_ratio": ratio3, "soft_prediction": soft,
                "consequence": "rest inequality E_gamma<=E_total fails for narrowband switching at this momentum"}


@test("W05")
def packet_rest_law_failure():
    resp, pred = packet_response(1000., .3, "free")
    rest = leading(1000., "free")
    return resp > 0 and resp/rest > 1e3, {"sigma": .3, "tau": 1000, "packet_R": resp, "rest_law_LC12": rest, "R_over_rest_law": resp/rest,
                                         "moving_prediction_pi_mean_c": pred}


@test("W06")
def heavy_tail_counterexample():
    """F01: phi(k)=1/(sqrt(pi)(1+|k|^2)), M=d=1: normalized, finite mean energy and log-moment, infinite E^2-moment;
    hence pi*int |phi|^2 c_PEC = +infinity and (Fatou) tau^2 R_tau -> infinity, although R_tau -> 0 by LM-B."""
    E, v = sp.symbols("E v", positive=True)
    dens = 2/E**3                                   # energy density of |phi|^2 d^2k on E>=1
    norm = sp.integrate(dens, (E, 1, sp.oo)); mean = sp.integrate(dens*E, (E, 1, sp.oo))
    logm = sp.integrate(dens*sp.log(E), (E, 1, sp.oo)); sec = sp.integrate(dens*E*E, (E, 1, sp.oo))
    cpec = (3*v-2*v**3-3*(1-v*v)*sp.atanh(v))/(3*sp.pi**2*v**3*(1-v*v))
    # lower bound c_PEC >= kappa E^2 for E>=2 (kappa from the value at E=2, monotone growth) -> divergent integral
    ratio = lambda x: float(cpec.subs(v, sp.sqrt(1-sp.Rational(1, x*x))))/(x*x)
    kappa = ratio(2)
    grows = all(ratio(x) >= kappa for x in [2, 3, 5, 10, 100, 1000])
    lower = sp.integrate(dens*kappa*E*E, (E, 2, sp.oo))
    # the fault replaces the E^2-moment test by a log-moment test, which wrongly passes this packet
    moment_ok = sec == sp.oo if FAULT != "pec-logmoment-only" else logm == sp.oo
    ok = norm == 1 and mean == 2 and logm == sp.Rational(1, 2) and moment_ok and lower == sp.oo and grows
    return ok, {"packet": "|phi|^2 = 1/[pi(1+|k|^2)^2], energy density 2/E^3 on E>=1 (M=1)", "norm": str(norm), "mean_energy": str(mean),
                "mean_log_energy": str(logm), "mean_energy_squared": str(sec), "c_PEC_lower_bound_kappa_E2_from_E2": kappa,
                "pi_int_w_cPEC_lower_bound": str(lower), "consequence": "tau^2 R_tau(phi) -> infinity for PEC; R_tau(phi) -> 0 still holds (finite log-moment)",
                "source": "counterexample from the v1.2 audit (F01), adopted; sympy moments"}


@test("R04")
def packet_regression():
    resp, pred = packet_response(1000., .3, "free")
    return abs(resp/pred-1) < 2e-2, {"packet_R_over_prediction": resp/pred, "tolerance": 2e-2}


@test("R05")
def plateau_regression():
    kap, lam = 1e4, .01
    r = moving_analytic(lam*math.hypot(kap, 1.), kap, "free")[0]/plateau()
    return r > 3 and abs(r/phi_closed(lam)-1) < 1e-3, {"J_over_Jinf": r, "Phi": phi_closed(lam), "rest_plateau": 1}


@test("X01")
def heavy_tail_growth():
    vals = {}
    for tau in [10., 30., 100.]:
        r = heavy_tail_packet_response(tau, "PEC"); vals[f"{tau:g}"] = {"R": r, "tau2R": tau*tau*r}
    seq = [vals[k]["tau2R"] for k in ["10", "30", "100"]]
    return seq[0] < seq[1] < seq[2], {"tau2R": vals, "increments_per_factor_3": [seq[1]-seq[0], seq[2]-seq[1]],
                                       "scope": "finite tau diagnostic of W06; monotone growth is consistent with, but does not prove, the analytic divergence"}


# New v1.4 research checks. These local identities and finite samples are not
# machine proofs of the universal dominated-convergence arguments in the paper.

def pec_dini_integral(a=1.0):
    return 1.0 if FAULT == "pec-dini-factor" else 2.0


def pec_soft_constant(mass=1.0, a=1.0):
    return uniform_constant()*plateau(a)/mass + pec_dini_integral(a)/(4*math.pi**2)


def layer_closed(eta, mass=1.0, a=1.0):
    """Exponential-profile LM-L. Closed normal integral, 50-digit arithmetic.

    This is NOT the full finite-energy spectrum. It is the E*Omega=eta limit.
    """
    h, m, q = map(mp.mpf, (eta,mass,a))
    if FAULT == "layer-scale":
        h *= 2
    s=m*m+2*h; r=mp.sqrt(s); b=2*h/(r+m)
    i1=b*b/(q*q+b*b)
    i0=q*mp.atan(b/q)-q*q*b/(q*q+b*b)
    i2=2*q*q*b-3*q**3*mp.atan(b/q)+q**4*b/(q*q+b*b)
    return float((4*h*r*i1+(-2*s+h*h/s)*i0-(m*m+h)*i2/(2*s))/(8*mp.pi**2*r*h))


def layer_quad(eta, mass=1.0, a=1.0):
    """Independent normal quadrature of the limiting angular kernel."""
    s=mass*mass+2*eta; r=math.sqrt(s); b=2*eta/(r+mass)
    def f(t):
        z=a*math.tan(t)
        bracket=4*eta*r/z-2*s+eta*eta/s-(mass*mass+eta)*z*z/(2*s)
        return 2*a*math.sin(t)**2*bracket
    val,err=quad(f,0,math.atan(b/a),epsabs=0,epsrel=2e-11,limit=250)
    return val/(8*math.pi**2*r*eta),err/(8*math.pi**2*r*eta)


def tail_power(alpha):
    return 2.0 if FAULT == "tail-power" else alpha


def tail_coefficient(alpha, mass=1.0, a=1.0, e0=1.0):
    """Mellin coefficient with explicit analytic integration-tail bounds.

    e_ch=1. Quadrature estimates are not interval arithmetic certificates.
    """
    lo,hi=1e-12,1e10
    val,err=quad(lambda y: math.exp(-alpha*y)*layer_closed(math.exp(y),mass,a),
                 math.log(lo),math.log(hi),epsabs=0,epsrel=3e-10,limit=250)
    small=3/(2*math.pi**2*a*a*mass*mass)*lo**(2-alpha)/(2-alpha)
    large=pec_soft_constant(mass,a)*hi**(-alpha)/alpha
    pref=math.pi*alpha*e0**alpha*math.gamma(1+alpha/2)
    return dict(value=pref*val,quad_error_estimate=pref*err,
                analytic_tail_bound=pref*(small+large),eta_interval=[lo,hi])


def measurement_amplitude(after, projector):
    before = 0*after if FAULT == "measurement-delete-before" else -after
    return after@projector + projector@before


@test("C16")
def dini_algebra():
    z,a,b,d=sp.symbols("z a b d", positive=True)
    B=2*a*a*z*z/(a*a+z*z)**2
    exact=sp.integrate(2*B/z,(z,0,sp.oo))
    low=sp.integrate(4*d*d*z,(z,0,b))
    return exact==2 and low==2*d*d*b*b and float(exact)==pec_dini_integral(), {
        "I_exponential":str(exact),"low_frequency_Dini_bound":str(low),
        "C_rho_M1_a1":pec_soft_constant(),
        "scope":"Dini integral and cutoff constant only; the global current bound is proved in LM-D"}


@test("C17")
def layer_algebra():
    r,m,z,a=sp.symbols("r m z a",positive=True)
    h=(r*r-m*m)/2
    # Leading terms of E <E_f T>, reconstructed before the normal integral.
    direct=(h*(2*h+z*z)/(2*r*r)-z*z/2-2*m*m-4*h+4*h*r/z)/2
    bracket=4*h*r/z-2*r*r+h*h/(r*r)-(m*m+h)*z*z/(2*r*r)
    difference=sp.factor(2*direct-bracket)
    endpoint=sp.factor(bracket.subs(z,r-m))
    endpoint_expected=m*(m*m-2*m*r+5*r*r)/(2*r)
    B=2*a*a*z*z/(a*a+z*z)**2
    primitives=[z*z/(a*a+z*z),a*sp.atan(z/a)-a*a*z/(a*a+z*z),
                2*a*a*z-3*a**3*sp.atan(z/a)+a**4*z/(a*a+z*z)]
    residuals=[sp.factor(sp.diff(f,z)-g) for f,g in zip(primitives,[B/z,B,B*z*z])]
    t=sp.symbols("t",positive=True)
    # z=eta*t/M as eta->0: K->4M^2/t-2M^2.
    small=sp.integrate(2*t*t*(4/t-2),(t,0,1))/(8*sp.pi**2)
    return difference==0 and sp.factor(endpoint-endpoint_expected)==0 and all(x==0 for x in residuals) and small==1/(3*sp.pi**2), {
        "leading_kernel_residual":str(difference),"endpoint":str(endpoint),
        "primitive_derivative_residuals":list(map(str,residuals)),
        "small_eta_coefficient_Mdcharge1":str(small),
        "scope":"fixed-z angular limit algebra, positivity endpoint, three antiderivatives and rescaled small-eta integral"}


@test("C18")
def mellin_scaling():
    u,t,al=sp.symbols("u t al",positive=True)
    # Direct E=t*u substitution in alpha*E0^alpha*E^(-1-alpha)*dE.
    jacobian=sp.simplify((t*u)**(-1-al)*t/(t**(-al)*u**(-1-al)))
    values=[]
    for alpha in [.5,1.,1.5]:
        g,err=quad(lambda x: x**(1+alpha)*math.exp(-x*x),0,math.inf,epsabs=1e-13,epsrel=2e-12)
        values.append(dict(alpha=alpha,integral=g,gamma_half=math.gamma(1+alpha/2)/2,
                           exponent=tail_power(alpha),error=err))
    ok=jacobian==1 and all(abs(v["integral"]/v["gamma_half"]-1)<1e-10 and v["exponent"]==v["alpha"] for v in values)
    return ok,{"density_Jacobian_ratio":str(jacobian),"Gaussian_Mellin_samples":values,
               "integrability_domain":"0<alpha<2: u^(1-alpha) at zero, u^(-1-alpha) at infinity"}


@test("C19")
def measurement_algebra():
    A,D=sp.symbols("A D",commutative=False)
    residual=sp.expand(A*D+D*(-A)-(A*D-D*A))
    h=sp.symbols("h",positive=True)
    # |T_h|^2 / |T_lambda|^2 = Omega^2 away from Omega=0,
    # when h=-lambda' and hat(lambda)=hat(h)/(i*Omega).
    O=sp.symbols("O",positive=True)
    ratio=sp.simplify(abs(h)**2/abs(h/(sp.I*O))**2)
    return residual==0 and ratio==O**2,{"commutator_residual":str(residual),"temporal_weight_ratio":str(ratio),
        "scope":"algebra after the on-shell no-emission premise; no construction of a detector"}


@test("V18")
def uniform_pec_soft_samples():
    data=[]
    for mass,a in [(1,.1),(1,1),(1,10),(.3,1)]:
        for kap in [0,.3,1,3,10,100,1e3,1e4,1e5]:
            for om in [.001,.01,.1,1,10,100,1e3,1e4]:
                val,err=moving_analytic(om,kap,"PEC",mass,a)
                data.append((val/(om*pec_soft_constant(mass,a)),mass,a,kap,om))
    maximum=max(data)
    return min(d[0] for d in data)>=-1e-12 and maximum[0]<=1+1e-10, {
        "points":len(data),"maximum_ratio_M_a_k_Omega":maximum,
        "bound":"J_PEC/(C_rho*Omega)<=1, e_ch=1","uses_cached_V14_values":True}


@test("V19")
def layer_full_spectrum_comparison():
    rows=[]
    for eta in [.01,.1,1.,10.,100.]:
        energies=[1e3,1e4] if eta<100 else [1e4,1e5]
        for E in energies:
            j,err=moving_analytic(eta/E,math.sqrt(E*E-1),"PEC")
            predicted=layer_closed(eta)
            rows.append(dict(eta=eta,E=E,L=predicted,J_over_Omega=j*E/eta,relative_difference=abs(j*E/(eta*predicted)-1),quad_error=err*E/eta))
    ok=all(rows[i+1]["relative_difference"]<rows[i]["relative_difference"] and rows[i+1]["relative_difference"]<3e-5 for i in range(0,len(rows),2))
    return ok,{"samples":rows,"last_energy_tolerance":3e-5,
        "scope":"full finite-energy analytic-angle integral vs a separately derived asymptotic closed form; convergence samples, not uniform remainder theorem"}


@test("V20")
def layer_quadrature_and_mellin():
    diffs=[]
    for mass,a in [(1,1),(.3,2.)]:
        for eta in [1e-4,.01,1.,100.,1e4]:
            c=layer_closed(eta,mass,a);v,err=layer_quad(eta,mass,a)
            diffs.append(abs(c/v-1))
    small=layer_closed(1e-5)/(1e-10/(3*math.pi**2))
    large=layer_closed(1e6)/(2/(4*math.pi**2))
    coeff={str(alpha):tail_coefficient(alpha) for alpha in [.5,1.,1.5]}
    return max(diffs)<1e-8 and abs(small-1)<2e-5 and abs(large-1)<.002 and all(v["value"]>v["analytic_tail_bound"] for v in coeff.values()), {
        "normal_integral_routes_max_relative_difference":max(diffs),"small_eta_ratio":small,"large_eta_ratio":large,
        "tail_coefficients_M_a_E0_charge1":coeff,
        "norm_lower_bound":pec_dini_integral()/(4*math.pi),
        "scope":"closed form vs quadrature; Mellin quadrature includes analytic tails, ordinary error estimates are not enclosures"}


@test("W07")
def infinite_log_and_finite_energy_packets():
    t,E=sp.symbols("t E",positive=True)
    norm=sp.integrate(1/t**2,(t,1,sp.oo));logmom=sp.integrate(1/t,(t,1,sp.oo))
    alpha=sp.Rational(3,2)
    n2=sp.integrate(alpha/E**(1+alpha),(E,1,sp.oo))
    mean=sp.integrate(alpha/E**alpha,(E,1,sp.oo))
    second=sp.integrate(alpha*E**(1-alpha),(E,1,sp.oo))
    return norm==n2==1 and logmom==second==sp.oo and mean==3, {
        "infinite_log_packet":{"energy_density":"1/(E*(log E)^2), E>=exp(1), M=1","norm":str(norm),"log_moment":str(logmom)},
        "finite_energy_packet":{"alpha":"3/2","energy_density":"(3/2)*E^(-5/2), E>=1","norm":str(n2),"mean_E":str(mean),"mean_E2":str(second),"PEC_decay_power":tail_power(1.5)},
        "scope":"moments are checked; the response conclusions also use LM-D and LM-P"}


@test("W08")
def measurement_identity_witness():
    A=np.array([[0.,1.+2.j],[3.-1.j,0.]],dtype=complex)
    I=np.eye(2);D=np.diag([1.,0.])
    identity_norm=float(np.linalg.norm(measurement_amplitude(A,I))**2)
    projector_norm=float(np.linalg.norm(measurement_amplitude(A,D))**2)
    current,_=moving_analytic(.7,1.,"PEC")
    return identity_norm==0 and projector_norm>0 and current>0, {
        "no_measurement_amplitude_norm2":identity_norm,"noncommuting_projector_amplitude_norm2":projector_norm,
        "M70_J_PEC_Omega0.7_k1":current,
        "scope":"finite matrix cancellation witness and a positive M70 spectral sample; not a physical detector realization"}



@test("C20")
def sharp_bound_certificates():
    """v1.4: the exact lemmas behind J_B <= 18 J_inf and Omega <= 2 omega."""
    E, Om, M, z, pp, k = sp.symbols("E Om M z pp k", positive=True)
    N = Om*(2*E+Om); s = M*M+N
    p2 = ((N-z*(2*M+z))*(N+z*(2*M-z)))/(4*s)          # p*^2
    q2 = sp.simplify(p2*s/(E+Om)**2)                   # q^2 = p*^2/gamma_c^2
    q02 = sp.simplify(q2.subs(z, 0))
    target = z*z*(4*(E*E-M*M)+4*E*Om+2*Om*Om+z*z)/(4*(E+Om)**2)
    monotone = sp.simplify(sp.expand(z*z+q2-q02-target))          # 0 => z^2+q^2 >= q(0)^2
    q0 = sp.simplify(sp.sqrt(q02)); G0 = sp.simplify(Om/q0)
    g0_form = sp.simplify(G0-2*(E+Om)/(2*E+Om))
    g0_le2 = sp.simplify(2-G0); g0_ge1 = sp.simplify(G0-1)
    s_gap = sp.factor(sp.expand(s-(M+Om)**2))                      # 2 Om (E-M) >= 0
    lip = sp.simplify(sp.expand((sp.sqrt(k*k+M*M)+pp)**2-((k+pp)**2+M*M))-2*pp*(sp.sqrt(k*k+M*M)-k))
    # constants: J1/J_inf = 2(M+Om)/sqrt(s) <= 2 ; J2/J_inf = 8 G0 <= 16 ; total 18
    ech, rho2 = sp.symbols("ech rho2", positive=True)
    Jinf = ech**2*rho2/(16*sp.pi)
    J1 = ech**2*rho2*(M+Om)/(8*sp.pi*sp.sqrt(s))
    J2 = (ech**2/(4*sp.pi**2))*G0*2*sp.pi*rho2
    c1 = sp.simplify(J1/Jinf-2*(M+Om)/sp.sqrt(s)); c2 = sp.simplify(J2/Jinf-8*G0)
    total = sp.simplify(2+8*2-uniform_constant())
    # T2 = |j0|^2 (1-(1-Om/w)^2) <= 1 : the bracket is x(2-x) with x=Om/w
    w, x = sp.symbols("w x", positive=True)
    bracket = sp.simplify(Om*(2*w-Om)/w**2-(x*(2-x)).subs(x, Om/w))
    bracket_max = sp.maximum(x*(2-x), x, sp.Interval(0, 2))
    ok = all(v == 0 for v in [monotone, g0_form, s_gap-2*Om*(E-M), lip, c1, c2, total, bracket]) and bracket_max == 1
    ok = ok and sp.simplify(g0_le2-2*E/(2*E+Om)) == 0 and sp.simplify(g0_ge1-Om/(2*E+Om)) == 0
    return ok, {"monotonicity_residual": str(monotone), "q0": str(q0), "G0": str(G0), "G0_upper_gap": str(g0_le2), "G0_lower_gap": str(g0_ge1),
                "s_minus_(M+Omega)^2": str(s_gap), "lipschitz_residual": str(lip),
                "J1_over_Jinf": "2(M+Omega)/sqrt(s) <= 2", "J2_over_Jinf": "8 G0 <= 16", "total": str(uniform_constant()),
                "T2_bracket_max": str(bracket_max),
                "scope": "exact identities and the rational constants of Section 5.3; the integrated inequalities are the manuscript proof"}


@test("V21")
def photon_energy_lower_half():
    """LM-E(a): Omega<=2omega pointwise on shell, and J_gamma >= Omega J/2 on the grid."""
    worst = (-1., None); count = 0
    for mass in [.3, 1., 3.]:
        for kap in [0., .3, 1., 10., 100., 1e3, 1e4]:
            E = math.hypot(kap, mass)
            for w in [1e-3, 1e-2, .1, 1., 10., 100.]:
                for mu in [-1., -.5, 0., .5, .9, 1.]:
                    for u in [0., .5, .9]:
                        st = math.sqrt(max(0., 1-mu*mu)); ny = st*math.sqrt(max(0., 1-u*u)); z = st*u
                        px, py = w*mu, w*ny
                        ef = math.sqrt((kap-px)**2+py*py+mass*mass)
                        om = w+(px*px+py*py-2*kap*px)/(ef+E); count += 1   # cancellation-free E_f+w-E
                        if om <= 0:
                            continue
                        r = om/(2*w)
                        if r > worst[0]:
                            worst = (r, [mass, kap, w, mu, u])
    ratio = (1., None)
    for mass, a in GRID[0][:2]:
        for kap in [0., 1., 100., 1e4]:
            for om in [1e-3, .1, 1., 100.]:
                for fam in ["free", "PEC", "PMC"]:
                    j = moving_analytic(om, kap, fam, mass, a)[0]
                    jg = moving_analytic(om, kap, fam, mass, a, True)[0]
                    r = jg/(om*j)
                    if r < ratio[0]:
                        ratio = (r, [mass, a, kap, om, fam])
    return worst[0] <= 1+1e-12 and ratio[0] >= .5, {"spectral_points": 96, "onshell_points": count, "max_Omega_over_2omega": worst[0], "argmax_[M,kappa,omega,mu,u]": worst[1],
            "min_Jgamma_over_OmegaJ": ratio[0], "argmin_[M,a,kappa,Omega,family]": ratio[1], "required_floor": 0.5,
            "scope": "finite on-shell sample (Omega computed in the cancellation-free form) and a 96-point three-family spectral grid; Omega<=2omega is proved in Section 5.8 from the 1-Lipschitz dispersion, with equality approached for backward collinear emission in the massless limit"}


@test("W09")
def above_four_witness():
    """A finite (k,Omega) with J/J_inf > 4: the fixed-lambda limit Phi<4 is not a global bound."""
    a, kap, lam, fam = 2.401, 1.4739e7, 2.56e-7, "PMC"
    E = math.hypot(kap, 1.); om = lam*E
    j, err = moving_analytic(om, kap, fam, 1., a)
    r = j/plateau(a); phi = phi_closed(lam)
    r2 = moving_cov(om, kap, fam, 1., a, nodes=256)/plateau(a)
    return r > 4 and phi < 4 and abs(r2/r-1) < 1e-6 and err/j < 1e-9, {
        "point_[a,kappa,lambda,family]": [a, kap, lam, fam], "J_over_Jinf_route3": r, "route3_relative_error_estimate": err/j,
        "J_over_Jinf_route2_256nodes": r2, "Phi(lambda)": phi, "excess_over_4": r-4,
        "analytic_lower_bound": 64/(5*math.pi),
        "consequence": "Numerical witness 4.1102159588 is not an interval certificate. LM-Q proves sup >= 64/(5 pi) > 4; LM-B proves sup <= 18. Exact optimum OPEN."}


@test("X02")
def softform_vacuity():
    """Diagnostic: at fixed Omega the soft-form (formation-time-type) bound diverges in E while J/J_inf stays bounded."""
    rows = {}
    om = .1
    for kap in [1., 100., 1e4, 1e6]:
        E = math.hypot(kap, 1.)
        j = moving_analytic(om, kap, "PMC", 1., 1.)[0]/plateau(1.)
        b = softform_bound(om, E, 1., 1.)/plateau(1.)
        rows[f"{kap:g}"] = {"E_over_M": E, "J_over_Jinf": j, "softform_bound_over_Jinf": b, "bound_over_J": b/j}
    js = [rows[k]["J_over_Jinf"] for k in rows]; bs = [rows[k]["softform_bound_over_Jinf"] for k in rows]
    ratios = [rows[k]["bound_over_J"] for k in rows]
    ok = max(js) < uniform_constant() and bs == sorted(bs) and bs[-1] > 3*bs[0] and bs[-1] > max(js) and ratios[1:] == sorted(ratios[1:])
    return ok, {
        "fixed_Omega": om, "rows": rows,
        "scope": "diagnostic, not evidence: it shows that a bound of the soft form alone cannot be uniform in k, which is why Section 5.3 (i)-(iii) is needed for LM-T"}



def soft_inner_floor(om, q0):
    return q0*q0 if FAULT == "soft-denominator" else om*om/16


@test("W10")
def rejected_soft_denominator():
    E=M=Om=sp.Integer(1); z=sp.Rational(1,2)
    N=Om*(2*E+Om)
    q2=((N-z*z)**2-4*M*M*z*z)/(4*(E+Om)**2)
    q0=N/(2*(E+Om))
    actual2=Om**2/(z*z+q2)
    rejected2=Om**2/(z*z+q0*q0)
    repaired2=Om**2/(z*z+soft_inner_floor(Om,q0))
    return actual2>rejected2 and actual2<=repaired2 and q2-q0*q0==-sp.Rational(39,256), {
        "point":"M=E=Omega=1, z=1/2, zmax=1",
        "q2":str(q2),"q0_squared":str(q0*q0),
        "q2_minus_q0_squared":str(q2-q0*q0),
        "actual_G":str(sp.sqrt(actual2)),"rejected_rhs":str(sp.sqrt(rejected2)),
        "repaired_rhs":str(sp.sqrt(repaired2)),
        "scope":"exact counterexample to parent B's intermediate inequality, not a counterexample to its final 18 bound"}


def fixed_frequency_kernel(om, z):
    coefficient=1 if FAULT == "fixed-frequency-kernel" else 2
    return om*(om*om+coefficient*z*z)/(om*om+z*z)**1.5


def fixed_frequency_limit(om, family, a=1.0):
    def f(t):
        z=a*math.tan(t)
        wdz={"free":a,"PEC":2*a*math.sin(t)**2,"PMC":2*a*math.cos(t)**2}[family]
        return wdz*fixed_frequency_kernel(om,z)
    j,err=quad(f,0,math.pi/2,epsabs=1e-13,epsrel=2e-12)
    return j/(4*math.pi**2),err/(4*math.pi**2)


@test("C21")
def fixed_frequency_algebra():
    O,z=sp.symbols("O z",positive=True)
    E,M=sp.symbols("E M",positive=True)
    N=O*(2*E+O); s=M*M+N
    a0=(E+O)*(N+z*z)/(2*s)
    p2=((N-z*z)**2-4*M*M*z*z)/(4*s)
    gap=(E+O)**2*z*z/s+p2
    A0=2*E*(E+O)+(O*O+z*z)/2
    ratios=[s/E,a0/E,gap/E,A0/E**2,(2*E+O)/E]
    expected_limits=[2*O,sp.Rational(1,2),(O*O+z*z)/(2*O),2,2]
    limit_residuals=[sp.simplify(sp.limit(sp.cancel(r),E,sp.oo)-target)
                     for r,target in zip(ratios,expected_limits)]
    # Leading orders: A0/E^2 -> 2, a0/E -> 1/2,
    # gap/E -> (O^2+z^2)/(2 O), sqrt(s)/sqrt(E) -> sqrt(2 O).
    d=(O*O+z*z)/(2*O)
    leading=(4*O/sp.sqrt(d)-O*O/d**sp.Rational(3,2))/(2*sp.sqrt(2*O))
    kernel=O*(O*O+2*z*z)/(O*O+z*z)**sp.Rational(3,2)
    residual=sp.simplify(leading-kernel)
    # At O=a, z=a tan(theta), u=sin(theta) gives
    # integral (1+u^2)(1-u^2) du = 4/5; normalization is 16/pi.
    u=sp.symbols("u",real=True)
    integral=sp.integrate((1+u*u)*(1-u*u),(u,0,1))
    coefficient=sp.simplify(16*integral/sp.pi)
    numeric=fixed_frequency_kernel(1.,.5)
    expected=float(kernel.subs({O:1,z:sp.Rational(1,2)}))
    return all(x==0 for x in limit_residuals) and residual==0 and coefficient==64/(5*sp.pi) and abs(numeric/expected-1)<1e-14, {
        "exact_kinematic_limit_residuals":list(map(str,limit_residuals)),
        "leading_kernel_residual":str(residual),"rational_integral":str(integral),
        "PMC_limit_over_Jinf":str(coefficient),"implemented_kernel":numeric,
        "strict_above_four_reason":"pi < 22/7 < 16/5",
        "scope":"exact leading-order algebra and normalized integral; the dominated-limit proof is in LM-Q"}


@test("V22")
def fixed_frequency_samples():
    rows=[]
    for family in ["free","PEC","PMC"]:
        for om in [1.,3.773184]:
            limit,_=fixed_frequency_limit(om,family)
            for E in [1e5,1e7]:
                j,err=moving_analytic(om,math.sqrt(E*E-1),family)
                rows.append({"family":family,"Omega":om,"E":E,"limit_over_Jinf":limit/plateau(),
                             "finite_over_Jinf":j/plateau(),"relative_difference":abs(j/limit-1),
                             "quadrature_error_estimate":err})
    asymptotic=[r["relative_difference"] for r in rows if r["E"]==1e7]
    return max(asymptotic)<.002, {"samples":rows,"last_energy_max_relative_difference":max(asymptotic),
                                 "tolerance":.002,"scope":"12 finite-energy samples; no universal numerical limit certificate"}


def paper_text():
    text=PAPER.read_text(encoding="utf-8")
    if FAULT=="doc-hash":
        text=re.sub(r'"script_sha256": "[0-9a-f]{64}"','"script_sha256": "'+'0'*64+'"',text)
    elif FAULT=="doc-equation":
        text=text.replace(r"\tag{LB1}",r"\tag{LB999}")
    elif FAULT=="doc-table":
        text=text.replace("R_tau1000 / leading_family(tau1000)","tau^2 R / coefficient_all_families")
    elif FAULT=="doc-ledger":
        text=text.replace('"qualification": "PASS"','"qualification": "FAIL"')
    elif FAULT=="doc-vocabulary":
        text=text.replace('"qualification": "PASS"','"qualification": "PENDING-INDEPENDENT-AUDIT"')
    elif FAULT=="doc-round":
        text=text.replace("(5 findings, F01–F05)","(4 findings, F01–F04)")
    elif FAULT=="doc-constant":
        text=text.replace(r"18\,J_\infty",r"36\,J_\infty")
    elif FAULT=="doc-version":
        text=text.replace("## 부록 D.","python m70_v1_2_verify.py --paper m70_v1_2.md\n\n## 부록 D.",1)
    return text


def metadata(text):
    match=re.search(r"<!-- M70-META\s*\n(.*?)\n-->",text,re.S)
    if not match:
        raise ValueError("M70-META block absent")
    return json.loads(match.group(1))


@test("G01")
def identity_guard():
    meta=metadata(paper_text())
    digest=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    ok=meta["script_sha256"]==digest and meta["paper_version"]==PAPER_VERSION and meta["script_version"]==VERSION
    normalize=lambda n:re.sub(r"\s*\(\d+\)(?=\.[^.]+$)","",n)
    names=meta["paper"]==normalize(PAPER.name) and meta["script"]==normalize(Path(__file__).name)
    return ok and names, {"script_sha256":digest,"declared_script_sha256":meta["script_sha256"],"file_names_match_after_transport_suffix":names,
                          "actual_names":[PAPER.name,Path(__file__).name],"declared_names":[meta["paper"],meta["script"]]}


@test("G02")
def equation_guard():
    text=paper_text()
    # Strip all fenced code before examining mathematics; old unfenced-code issue retired.
    mathtext=re.sub(r"(?ms)^```[^\n]*\n.*?^```\s*$","",text)
    labels=re.findall(r"\\tag\{([^}]+)\}",mathtext)
    blocks=re.findall(r"\\\[(.*?)\\\]",mathtext,re.S)
    def canonical(x): return re.sub(r"\s+","",x)
    bylabel={lab:canonical(b) for b in blocks for lab in re.findall(r"\\tag\{([^}]+)\}",b)}
    required={"LB1":[r"\begin{pmatrix}0&v&0\\v&0&w\\0&w&\delta\end{pmatrix}",r"(1,0,0)^T"],
              "LC7":[r"\mathcal E_{\rm total}",r"\Omega J_B(\Omega)",r"\mathcal E_\gamma",r"J_{\gamma,B}(\Omega)"],
              "LC9":[r"2J_\infty",r"J_\infty"],
              "LC1":[r"M>0",r"\rho\in L^1\cap L^2"],
              "LM1":[r"\frac{K\cdot K_f-3M^2}{2EE_f}",r"\frac{EE_f+k\cdot k_f+M^2}{2EE_f}"],
              "LM4":[r"18\,J_\infty"],
              "LM6":[r"\operatorname{artanh}"],
              "LM7":[r"E^2",r"c_{\rm PEC}"],
              "LM8":[r"4(1+\lambda)-(4\lambda+7)\sqrt{\frac{\lambda}{\lambda+2}}"],
              "LM10":[r"\frac{3e_{\rm ch}^2d^2E(k)^2}{2\pi^2M^2}",r"\Omega^3"],
              "LM11":[r"I_\rho",r"C_\rho",r"\forall k",r"\forall\Omega>0"],
              "LM14":[r"\frac{4\eta r_\eta}{z}",r"\frac{e_{\rm ch}^2}{8\pi^2r_\eta\eta}"],
              "LM17":[r"\tau^{-\alpha}",r"\Gamma(1+\alpha/2)",r"\eta^{-1-\alpha}"],
              "LM18":[r"G(0)",r"2(E+\Omega)",r"4|k|^2"],
              "LM19":[r"\Omega\le2\omega",r"\tfrac12\mathcal E_{\rm total}"],
              "LM20":[r"\Omega(\Omega^2+2z^2)",r"\frac{64}{5\pi}"]}
    critical=all(k in bylabel and all(canonical(x) in bylabel[k] for x in tokens) for k,tokens in required.items())
    return sorted(labels)==sorted(LABELS) and critical, {"actual_labels":labels,"expected_labels":LABELS,"critical_objects_match":critical,"scope":"selected displayed objects, not a proof parser"}


@test("G03")
def table_guard():
    text=paper_text()
    section=text.split("<!-- NUMERIC-TABLE -->")[1].split("<!-- /NUMERIC-TABLE -->")[0]
    header="R_tau1000 / leading_family(tau1000)"
    parsed={}
    for line in section.splitlines():
        cells=[c.strip() for c in line.strip().strip("|").split("|")]
        if cells and cells[0] in ["free","PEC","PMC"]:
            parsed[cells[0]]=[float(c) for c in cells[1:]]
    expected=numeric_table()
    errs=[abs(x/y-1) for fam,values in expected.items() for x,y in zip(parsed.get(fam,[]),values)]
    ok=header in section and set(parsed)==set(expected) and all(len(x)==4 for x in parsed.values()) and len(errs)==12 and max(errs)<2e-8
    msec=text.split("<!-- MOVING-TABLE -->")[1].split("<!-- /MOVING-TABLE -->")[0]
    mparsed={}
    for line in msec.splitlines():
        cells=[c.strip() for c in line.strip().strip("|").split("|")]
        try:
            key=f"{float(cells[0]):g},{float(cells[1]):g}"
            mparsed[key]=[float(c) for c in cells[2:]]
        except (ValueError,IndexError):
            continue
    mexp=moving_table()
    merrs=[abs(x/y-1) for k,vals in mexp.items() for x,y in zip(mparsed.get(k,[]),vals)]
    ok=ok and set(mparsed)==set(mexp) and len(merrs)==2*len(mexp) and max(merrs)<2e-9
    lsec=text.split("<!-- LAYER-TABLE -->")[1].split("<!-- /LAYER-TABLE -->")[0]
    layer_rows=[]
    for line in lsec.splitlines():
        cells=[c.strip() for c in line.strip().strip("|").split("|")]
        try:
            h,E,L,J=map(float,cells)
            actual,_=moving_analytic(h/E,math.sqrt(E*E-1),"PEC")
            layer_rows.append([h,E,abs(L/layer_closed(h)-1),abs(J/(actual*E/h)-1)])
        except ValueError:
            continue
    lerrs=[x for r in layer_rows for x in r[2:]]
    ok=ok and len(layer_rows)==5 and [(r[0],r[1]) for r in layer_rows]==[(.01,1e4),(.1,1e4),(1.,1e4),(10.,1e4),(100.,1e5)] and max(lerrs,default=1)<2e-8
    return ok, {"mode_specific_header":header in section,"parsed_cells":sum(map(len,parsed.values())),"max_relative_rounding_error":max(errs) if errs else None,"moving_table_cells":len(merrs),"moving_table_max_relative_error":max(merrs) if merrs else None,"layer_table_cells":len(lerrs),"layer_table_max_relative_error":max(lerrs,default=None),"tolerance":[2e-8,2e-9,2e-8]}


def parse_rounds(text):
    """Audit-response round parser (VERIFY 12.1): heading, declared count, prefix range and actual table rows of each round."""
    found=[]
    heads=list(re.finditer(r"^### Round (\d+) — (.+?) \((\d+) findings, ([A-Z])(\d+)[–-]\4(\d+)\)",text,re.M))
    for i,h in enumerate(heads):
        end=heads[i+1].start() if i+1<len(heads) else text.find("### C.1",h.end())
        body=text[h.end():end if end>0 else None]
        prefix=h.group(4); declared=int(h.group(3)); lo,hi=int(h.group(5)),int(h.group(6))
        rows=re.findall(r"^\| ("+prefix+r"\d+) \|",body,re.M)
        found.append({"round":int(h.group(1)),"heading":h.group(2),"prefix":prefix,"declared":declared,"range":[lo,hi],"rows":rows})
    return found


@test("G04")
def ledger_guard():
    text=paper_text();meta=metadata(text)
    expected={row:[v[0],v[1]] for row,v in REGISTRY.items()}
    census=dict(sorted(Counter(v[0] for v in REGISTRY.values()).items()))
    commands=re.findall(r"^python (m70_v\S+_verify\.py) --paper (m70_v\S+\.md)(?: --self-test)?$",text,re.M)
    ok=meta["ledger"]==expected and meta["census"]==census and meta["rows"]==len(REGISTRY)
    # Mission vocabulary (F03): four separate fields with allowed values, equal in script, manifest and cover line
    fields={"qualification":QUALIFICATION,"research_grade":RESEARCH_GRADE,"candidate_grade":CANDIDATE_GRADE,"target_grade":TARGET_GRADE}
    vocab={k:(meta.get(k) in ALLOWED[k] and meta.get(k)==v) for k,v in fields.items()}
    cover=text[:4000]
    cover_ok=all(re.search(pat,cover) for pat in [r"PAPER QUALIFICATION[^\n]{0,40}\b"+re.escape(QUALIFICATION)+r"\b",
                                                   r"RESEARCH GRADE[^\n]{0,40}\b"+re.escape(RESEARCH_GRADE)+r"\b",
                                                   r"CANDIDATE GRADE[^\n]{0,40}\b"+re.escape(CANDIDATE_GRADE)+r"\b",
                                                   r"TARGET GRADE[^\n]{0,40}\b"+re.escape(TARGET_GRADE)+r"\b"])
    ok=ok and all(vocab.values()) and cover_ok and meta["novelty"]==NOVELTY and meta["role"]==ROLE
    # audit-round registry (CPN6–CPN8): manifest == script registry == parsed headings and table rows
    rounds=parse_rounds(text)
    rounds_ok=meta.get("audit_rounds")==AUDIT_ROUNDS and len(rounds)==len(AUDIT_ROUNDS)
    for r,exp in zip(rounds,AUDIT_ROUNDS):
        n=exp["findings"]; width=2 if exp["prefix"]=="F" else 1
        ids=[f"{exp['prefix']}{i:0{width}d}" for i in range(1,n+1)]
        rounds_ok=rounds_ok and r["round"]==exp["round"] and r["prefix"]==exp["prefix"] and r["declared"]==n and r["range"]==[1,n] and r["rows"]==ids and len(r["rows"])==n
    ok=ok and rounds_ok and text.startswith("# M70 v1.5") and len(commands)>=1 and all(a=="m70_v1_5_verify.py" and b=="m70_v1_5.md" for a,b in commands)
    return ok, {"census":census,"rows":len(REGISTRY),"vocabulary":vocab,"cover_fields_match":cover_ok,"rounds":[{k:v for k,v in r.items() if k!="rows"}|{"row_count":len(r["rows"])} for r in rounds],
                "rounds_consistent":rounds_ok,"command_pairs":commands,"scope":"declaration consistency and vocabulary only; does not establish novelty, grade or qualification"}


@test("G05")
def version_guard():
    """CPN11: no stale version commands or superseded status strings live in the current text."""
    text=paper_text()
    stale_cmds=[m.group(0) for m in re.finditer(r"^python m70_v\S+_verify\.py --paper m70_v\S+\.md.*$",text,re.M) if "m70_v1_5_verify.py --paper m70_v1_5.md" not in m.group(0)]
    live=[]
    for i,line in enumerate(text.splitlines(),1):
        if line.strip().startswith("<!--") or line.strip().startswith('"'):
            continue
        for tok in STALE_TOKENS:
            if tok in line and not any(mark in line for mark in STALE_EXEMPT):
                live.append((i,tok))
    summary=re.search(r"<!-- RUN-SUMMARY -->(.*?)<!-- /RUN-SUMMARY -->",text,re.S)
    census=dict(sorted(Counter(v[0] for v in REGISTRY.values()).items()))
    summary_ok=False; parsed=None
    if summary:
        row=re.search(r"^\| 등록 행 \|(.*)$",summary.group(1),re.M)
        head=re.search(r"^\| 분류 \|(.*)$",summary.group(1),re.M)
        if row and head:
            keys=[c.strip() for c in head.group(1).strip().strip("|").split("|")]
            vals=[c.strip() for c in row.group(1).strip().strip("|").split("|")]
            parsed={k:int(v) for k,v in zip(keys,vals) if v.isdigit()}
            summary_ok=all(parsed.get(k)==n for k,n in census.items()) and parsed.get("P",0)==0 and f"총 {len(REGISTRY)}행" in summary.group(1)
    ok=not stale_cmds and not live and summary_ok and text.count("# M70 v1.5")>=1
    return ok, {"stale_commands":stale_cmds,"live_stale_status_lines":live,"run_summary_census":parsed,"registry_census":census,"summary_consistent":summary_ok,
                "scope":"mutual consistency of version strings, commands and census (VERIFY 7.2 S3); quotations with a retraction marker are exempt"}


def run(args):
    global PAPER,FAULT
    PAPER=args.paper;FAULT=args.fault
    rows=[]
    for row,(cls,claim,scope) in REGISTRY.items():
        if args.only_row and row!=args.only_row:
            rows.append(dict(id=row,cls=cls,claim=claim,scope=scope,status="SKIP",data={"reason":"explicit single-row profile; not executed"}))
            continue
        if cls=="D" or (args.math_only and cls=="G"):
            rows.append(dict(id=row,cls=cls,claim=claim,scope=scope,status="SKIP",data={"reason":"declaration only" if cls=="D" else "explicit math-only profile"}))
            continue
        with warnings.catch_warnings(record=True) as caught:
            warnings.simplefilter("always")
            try:
                passed,data=TESTS[row]()
                status="PASS" if passed else "FAIL"
            except Exception as exc:
                # Continue all independently runnable rows, exposing the cause.
                data={"error_type":type(exc).__name__,"error":str(exc).replace(str(PAPER),PAPER.name)}; status="FAIL"
        data["warnings"]={"count":len(caught),"first":str(caught[0].message) if caught else None}
        rows.append(dict(id=row,cls=cls,claim=claim,scope=scope,status=status,data=data))
    census=dict(sorted(Counter(r["cls"] for r in rows).items()))
    statuses=dict(sorted(Counter(r["status"] for r in rows).items()))
    report={"script_version":VERSION,"paper_version":PAPER_VERSION,"profile":"single-row" if args.only_row else ("math-only" if args.math_only else "paired"),
            "fault":FAULT,"rows":rows,"summary":{"rows":len(rows),"classes":census,"statuses":statuses,
            "evidence_rows":sum(r["cls"] in "PCVW" for r in rows),"control_rows":sum(r["cls"] in "RG" for r in rows),"non_evidence_rows":sum(r["cls"] in "XDT" for r in rows),"P":0,
            "warnings_total":sum(r["data"].get("warnings",{}).get("count",0) for r in rows)},
            "status_fields":{"qualification":QUALIFICATION,"research_grade":RESEARCH_GRADE,"candidate_grade":CANDIDATE_GRADE,"target_grade":TARGET_GRADE,"novelty":NOVELTY,"role":ROLE,"basis":"declared in manuscript; not computed by this script"},
            "paper_sha256":None if args.math_only or not PAPER.is_file() else hashlib.sha256(PAPER.read_bytes()).hexdigest(),
            "script_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            "limitations":["C covers local identities; V finite points; analytic universal proofs remain in manuscript.","No independent human or external audit, novelty, research grade, or physical instrument certification.","Three moving-sector quadratures share the same declared band, vertex, profile and mode conventions; route 3 uses the angular reduction of the v1.2 audit.","Moving-sector rows sample finite momenta; the uniform bound, packet iff, E^2-moment dichotomy and adiabatic limits are analytic claims in the manuscript.","X01/X02 are diagnostics, not evidence; the finite PMC witness is not interval arithmetic."]}
    return report,1 if statuses.get("FAIL",0) else 0


def self_test(args):
    script=Path(__file__).resolve();paper=args.paper.resolve()
    def call(extra,where=None,isolated_script=None):
        cmd=[sys.executable,str(isolated_script or script),"--paper",str((Path(where)/paper.name) if where else paper),*extra]
        p=subprocess.run(cmd,cwd=where,capture_output=True,text=True,timeout=3600)
        data=json.loads(p.stdout)
        return p,data
    p,baseline=call([])
    if p.returncode:
        return {"kind":"self-test","status":"FAIL","reason":"baseline failed; mutation sensitivity not certified","baseline":baseline},1
    results=[]
    with ThreadPoolExecutor(max_workers=max(1,min(6,len(FAULT_TARGETS),os.cpu_count() or 1))) as pool:
        outcomes=list(pool.map(lambda f:call(["--fault",f,"--only-row",FAULT_TARGETS[f]]),list(FAULT_TARGETS)))
    for (fault,target),(p,data) in zip(FAULT_TARGETS.items(),outcomes):
        failed=[r["id"] for r in data["rows"] if r["status"]=="FAIL"]
        results.append({"fault":fault,"type":"structural" if fault.startswith("doc-") else "functional","expected_row":target,"failed_rows":failed,"execution_scope":"designated target row in a fresh process; other rows explicitly SKIP","exit":p.returncode,"status":"PASS" if p.returncode==1 and target in failed else "FAIL"})
    p,data=call(["--paper",str(paper.with_name("absent_m70_document.md"))])
    missing=p.returncode==1 and all(next(r for r in data["rows"] if r["id"]==g)["status"]=="FAIL" for g in ["G01","G02","G03","G04","G05"])
    results.append({"case":"missing-paper","exit":p.returncode,"failed_rows":[r["id"] for r in data["rows"] if r["status"]=="FAIL"],"status":"PASS" if missing else "FAIL"})
    p,data=call(["--math-only"])
    degraded=p.returncode==0 and all(r["status"]=="SKIP" for r in data["rows"] if r["cls"]=="G")
    results.append({"case":"math-only","summary":data["summary"],"exit":p.returncode,"status":"PASS" if degraded else "FAIL"})
    dep=subprocess.run([sys.executable,"-S",str(script),"--math-only"],capture_output=True,text=True,timeout=120)
    depdata=json.loads(dep.stdout)
    results.append({"case":"dependencies-hidden-with-python-S","exit":dep.returncode,"status":"PASS" if dep.returncode==2 and depdata.get("status")=="FAIL" else "FAIL","output":depdata})
    with tempfile.TemporaryDirectory(prefix="m70_reproduce_") as folder:
        local=Path(folder)/script.name
        shutil.copy2(script,local);shutil.copy2(paper,Path(folder)/paper.name)
        p1,d1=call([],folder,local);p2,d2=call([],folder,local)
        same=p1.returncode==p2.returncode==0 and p1.stdout==p2.stdout
        results.append({"case":"isolated-two-process","byte_identical":p1.stdout==p2.stdout,"exit_codes":[p1.returncode,p2.returncode],"status":"PASS" if same else "FAIL","scope":"same installed dependency environment; only two deliverable files copied"})
    with tempfile.TemporaryDirectory(prefix="m70_transport_") as folder:
        local=Path(folder)/(script.stem+"(1)"+script.suffix)
        doc=Path(folder)/(paper.stem+"(1)"+paper.suffix)
        shutil.copy2(script,local);shutil.copy2(paper,doc)
        p=subprocess.run([sys.executable,str(local),"--paper",str(doc)],capture_output=True,text=True,timeout=3600)
        out=json.loads(p.stdout)
        results.append({"case":"download-suffix-two-files","exit":p.returncode,"status":"PASS" if p.returncode==0 else "FAIL", "hashes_unchanged":out.get("script_sha256")==baseline["script_sha256"] and out.get("paper_sha256")==baseline["paper_sha256"]})
    ok=all(r["status"]=="PASS" for r in results)
    return {"kind":"self-test","status":"PASS" if ok else "FAIL","baseline_summary":baseline["summary"],"baseline_paper_sha256":baseline["paper_sha256"],"script_sha256":baseline["script_sha256"],"cases":results},0 if ok else 1


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--paper",type=Path,default=Path(__file__).with_name("m70_v1_5.md"))
    parser.add_argument("--math-only",action="store_true")
    parser.add_argument("--only-row",choices=list(REGISTRY),help="Explicit targeted check; all other rows are SKIP, never a full-paper run")
    parser.add_argument("--fault",choices=list(FAULT_TARGETS))
    parser.add_argument("--self-test",action="store_true")
    args=parser.parse_args()
    if args.self_test and (args.fault or args.math_only or args.only_row):
        parser.error("--self-test needs the normal paired profile")
    try:
        dependencies()
    except ImportError as exc:
        print(json.dumps({"status":"FAIL","phase":"dependencies","exit":2,"error":str(exc),"not_run":list(REGISTRY),"remedy":"Install numpy scipy sympy mpmath; no checks executed."},sort_keys=True,indent=2))
        return 2
    result,code=self_test(args) if args.self_test else run(args)
    print(json.dumps(result,ensure_ascii=False,sort_keys=True,indent=2,allow_nan=False))
    return code


if __name__=="__main__":
    raise SystemExit(main())
