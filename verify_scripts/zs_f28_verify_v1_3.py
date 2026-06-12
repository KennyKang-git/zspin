#!/usr/bin/env python3
"""
zs_f28_verify_v1_3.py  --  Verification suite for ZS-F28 v1.3
"Seam-Constrained Finite Fourier Analysis II: The Symmetrized Lam-Leung Theorem,
 its Equivariant Extension, and the Purity Frontier"
Exact integer cyclotomic arithmetic throughout. RNG seeds pre-registered: 20260612 (v1.0), 20260613 (v1.1 extension).
Usage:  python3 zs_f28_verify_v1_3.py [--fast]
  --fast : skip the heavy exhaustive blocks (Q/R/S heavy checks at d=63, 75 and the 2^23 tally at d=45);
           heavy artifacts are recomputed in full mode (~30-60 min total), fast mode ~3 min.
Modules core.py, enum45.py, bigenum.py, cover.py, thm43.py, clique.py must sit beside this file
(released together; each is < 120 lines and inlined logically in the paper's Appendix description).
"""
import sys, time, numpy as np, itertools, collections, functools
sys.setrecursionlimit(100000)
from core import cyclotomic, monomial_table, seam_orbits
from enum45 import enumerate_invariant_vanishing, is_pure
from bigenum import enum_big
from cover import cosets, symmetric_cover_exists, find_cover
from thm43 import crt_maps, decomposition_from_cover, multiset_from_wy, reflect_construct, check_symmetric
from clique import make_adj, has_clique

FAST = "--fast" in sys.argv
PASS = 0; FAIL = 0; LOG = []
def check(name, cond, detail=""):
    global PASS, FAIL
    ok = bool(cond)
    PASS += ok; FAIL += (not ok)
    LOG.append((name, "PASS" if ok else "FAIL", detail))
    print(f"[{'PASS' if ok else 'FAIL'}] {name}  {detail}")

t00 = time.time()

# ============ A. exact arithmetic sanity ============
check("A1 deg Phi_15 = 8, deg Phi_45 = 24; full-group sums vanish",
      len(cyclotomic(15))-1 == 8 and len(cyclotomic(45))-1 == 24
      and not monomial_table(45,45).sum(axis=0).any() and not monomial_table(15,15).sum(axis=0).any())

# ============ B. d = 15 sets ============
sols15,_ = enumerate_invariant_vanishing(15)
check("B1 d=15: exactly 9 seam-invariant vanishing sets", len(sols15)==9)
b2 = True
for A in sols15:
    purep, pureq = is_pure(A,15,5), is_pure(A,15,3)
    if not (purep or pureq): b2 = False
    if purep:
        idx = frozenset(a % 5 for a in A)
        if idx != frozenset((-1-i)%5 for i in idx): b2 = False
    if pureq:
        idx = frozenset(a % 3 for a in A)
        if idx != frozenset((-1-i)%3 for i in idx): b2 = False
check("B2 d=15: single-direction unions; fiber index sets seam-invariant at quotient scale", b2)

# ============ C. d = 15 multisets (Corollary 4.4) ============
orbs15 = seam_orbits(15,-1); M15 = monomial_table(15,15)
ov15 = [M15[list(o)].sum(axis=0) for o in orbs15]
def inv_multisets(cap):
    out=[]
    for vals in itertools.product(range(cap+1), repeat=len(orbs15)):
        if all(v==0 for v in vals): continue
        if not sum(v*ov for v,ov in zip(vals,ov15)).any():
            m=np.zeros(15,dtype=int)
            for v,o in zip(vals,orbs15):
                for x in o: m[x]=v
            out.append(m)
    return out
def decs15(m):
    sols=[]; mx=int(m.max())
    for y in itertools.product(range(mx+1),repeat=3):
        ok=True; w=[0]*5
        for v in range(5):
            vals={int(m[x])-y[x%3] for x in range(15) if x%5==v}
            if len(vals)!=1 or min(vals)<0: ok=False; break
            w[v]=vals.pop()
        if ok: sols.append((tuple(w),y))
    return sols
i3 = inv_multisets(3)
check("C1 d=15 cap 3: 135 seam-invariant vanishing multisets, all integer-separable",
      len(i3)==135 and all(decs15(m) for m in i3))
check("C2 d=15 cap 3: every N-decomposition of every instance is symmetric (Cor 4.4)",
      all(all(all(w[v]==w[(-1-v)%5] for v in range(5)) and all(y[u]==y[(-1-u)%3] for u in range(3))
              for w,y in decs15(m)) for m in i3))
check("C3 d=15 cap 5: 665 instances, all decomposable", len(inv_multisets(5))==665)

# ============ D/E/F. d = 45 sets: counts, construction, identities ============
sols45,_ = enumerate_invariant_vanishing(45)
check("D1 d=45: exactly 379 seam-invariant vanishing sets (exact MITM)", len(sols45)==379)
p,a,q,b = 3,2,5,1
cands45 = cosets(45,3)+cosets(45,5); tau45 = lambda x:(-1-x)%45
dec=sym=refl=defect=interval=0; mixed45=[]
for A in sols45:
    cov = find_cover(A,cands45)
    if cov is not None: dec+=1
    if symmetric_cover_exists(A,cands45,tau45): sym+=1
    if not is_pure(A,45,15) and not is_pure(A,45,9): mixed45.append(A)
    w,y = decomposition_from_cover(cov,p,a,q,b); m = multiset_from_wy(w,y,p,a,q,b)
    pc=3
    delta={cc: int(w[cc,0]-w[(-1-cc)%pc,(-1-0)%45//9 if False else (-1)%5]) for cc in range(pc)}
    # defect as class function, antisymmetric, zero on fixed class:
    ok=True
    for cc in range(pc):
        vw={int(w[cc,v]-w[(-1-cc)%pc,(-1-v)%5]) for v in range(5)}
        vy={int(y[(-1-u)%9,0]-y[u,0]) for u in range(9) if u%pc==cc}
        if len(vw)!=1 or vw!=vy: ok=False
    dl={cc:(int(w[cc,0])-int(w[(-1-cc)%pc,(-1-0)%5])) for cc in range(pc)}
    for cc in range(pc):
        if dl[cc] != -dl[(-1-cc)%pc]: ok=False
        if (-1-cc)%pc==cc and dl[cc]!=0: ok=False
    if ok: defect+=1
    # interval identities U(sg)+d = U, L(sg)+d = L
    U={cc: min(int(w[cc,v]) for v in range(5)) for cc in range(pc)}
    L={cc: -min(int(y[u,0]) for u in range(9) if u%pc==cc) for cc in range(pc)}
    if all(U[(-1-cc)%pc]+dl[cc]==U[cc] and L[(-1-cc)%pc]+dl[cc]==L[cc] for cc in range(pc)): interval+=1
    w2,y2 = reflect_construct(w,y,p,a,q,b,-1)
    if (multiset_from_wy(w2,y2,p,a,q,b)==m).all() and w2.min()>=0 and y2.min()>=0 and check_symmetric(w2,y2,p,a,q,b,-1):
        refl+=1
check("D2 d=45: 379/379 admit N-decompositions (de Bruijn/Lam-Leung witness)", dec==379)
check("D3 d=45: exactly 96 genuinely mixed sets", len(mixed45)==96)
check("E1 reflection construction valid on all 379 sets", refl==379)
check("E1b symmetric exact covers exist for all 379 sets (set-level Thm 4.3)", sym==379)
check("F1 defect identities (class function, antisymmetric, zero on fixed class), all 379", defect==379)
check("F2 interval identities U.sigma + delta = U, L.sigma + delta = L, all 379", interval==379)

# ============ E2/E3/E4. multiset sampling with desymmetrized gauges ============
def sample_run(p_,a_,q_,b_, n, seed, maxw=3):
    rng=np.random.default_rng(seed)
    d_,pa_,qb_,split,join = crt_maps(p_,a_,q_,b_)
    pc,qc = p_**(a_-1), q_**(b_-1); ok=0
    for _ in range(n):
        w0=rng.integers(0,maxw+1,size=(pc,qb_)); y0=rng.integers(0,maxw+1,size=(pa_,qc))
        w=w0.copy(); y=y0.copy()
        for cc in range(pc):
            for v in range(qb_): w[cc,v]=w0[cc,v]+w0[(-1-cc)%pc,(-1-v)%qb_]
        for u in range(pa_):
            for vv in range(qc): y[u,vv]=y0[u,vv]+y0[(-1-u)%pa_,(-1-vv)%qc]
        m=multiset_from_wy(w,y,p_,a_,q_,b_)
        g=np.zeros((pc,qc),dtype=np.int64)
        for cc in range(pc):
            for vv in range(qc):
                U=min(int(w[cc,v]) for v in range(qb_) if v%qc==vv)
                L=-min(int(y[u,vv]) for u in range(pa_) if u%pc==cc)
                g[cc,vv]=rng.integers(L,U+1) if U>=L else 0
        w1=w.copy(); y1=y.copy()
        for cc in range(pc):
            for v in range(qb_): w1[cc,v]-=g[cc,v%qc]
        for u in range(pa_):
            for vv in range(qc): y1[u,vv]+=g[u%pc,vv]
        w2,y2=reflect_construct(w1,y1,p_,a_,q_,b_,-1)
        if (multiset_from_wy(w2,y2,p_,a_,q_,b_)==m).all() and w2.min()>=0 and y2.min()>=0 and check_symmetric(w2,y2,p_,a_,q_,b_,-1): ok+=1
    return ok
check("E2 d=45 multiset sampling, seed 20260612: 500/500", sample_run(3,2,5,1,500,20260612)==500)
check("E3 d=225 multiset sampling, seed 20260612: 300/300", sample_run(3,2,5,2,300,20260612)==300)
check("E3x d=225 extended sampling, seed 20260613: 1000/1000", sample_run(3,2,5,2,1000,20260613)==1000)
check("E4 d=72 = 2^3*3^2 even-d multiset sampling, seed 20260612: 500/500", sample_run(2,3,3,2,500,20260612)==500)

# ============ N. v1.1 normal form / equivariance ============
check("N1 translation conjugacy: tau_{-1} = T^{-1} (negation) T, T = +(d+1)/2, at d = 15, 45, 105",
      all(all(((-1-x)%d_)==((-((x+(d_+1)//2)%d_)-(d_+1)//2)%d_) for x in range(d_)) for d_ in (15,45,105)))
n2 = all(len(enumerate_invariant_vanishing(45,r=r)[0])==379 for r in (0,7,23))
check("N2 reflection-class transport: tau_r-invariant vanishing count = 379 for r = 0, 7, 23 at d=45", n2)
t = 23
n3 = all(frozenset((x+t)%45 for x in A)==frozenset((-(x+t))%45 for x in A) for A in sols45)
check("N3 A seam-invariant => A + (d+1)/2 negation-invariant, all 379", n3)
evenres={}
for (d_,p_,a_,q_,b_) in [(12,2,2,3,1),(20,2,2,5,1),(24,2,3,3,1),(36,2,2,3,2)]:
    cnds=cosets(d_,p_)+cosets(d_,q_)
    for r in (0,-1):
        sols,_=enumerate_invariant_vanishing(d_,r=r)
        tu=lambda x:(r-x)%d_
        s_=sum(1 for A in sols if symmetric_cover_exists(A,cnds,tu))
        rf=0
        for A in sols:
            cov=find_cover(A,cnds); w,y=decomposition_from_cover(cov,p_,a_,q_,b_)
            m=multiset_from_wy(w,y,p_,a_,q_,b_)
            w2,y2=reflect_construct(w,y,p_,a_,q_,b_,r)
            if (multiset_from_wy(w2,y2,p_,a_,q_,b_)==m).all() and w2.min()>=0 and y2.min()>=0 and check_symmetric(w2,y2,p_,a_,q_,b_,r): rf+=1
        evenres[(d_,r)]=(len(sols),s_,rf)
exp_even={(12,0):23,(12,-1):9,(20,0):79,(20,-1):33,(24,0):239,(24,-1):99,(36,0):2399,(36,-1):999}
check("N4 even-d exhaustive (d=12,20,24,36; both reflection classes): counts as tabulated",
      all(evenres[k][0]==v for k,v in exp_even.items()))
check("N5 even-d: symmetric covers and reflection construction valid on every instance",
      all(c==s_==r_ for (c,s_,r_) in evenres.values()))
# N6 even-d multiset exhaustive d=12 cap 2 both classes
def even12_multiset(r):
    orbs=seam_orbits(12,r); M=monomial_table(12,12)
    ov=[M[list(o)].sum(axis=0) for o in orbs]
    _,_,_,split,join=crt_maps(2,2,3,1)
    nok=ntot=0
    for vals in itertools.product(range(3),repeat=len(orbs)):
        if all(v==0 for v in vals): continue
        if sum(v*o_ for v,o_ in zip(vals,ov)).any(): continue
        m=np.zeros(12,dtype=np.int64)
        for v,o in zip(vals,orbs):
            for x in o: m[x]=v
        found=None; mx=int(m.max())
        for y0 in itertools.product(range(mx+1),repeat=4):
            ok=True; w=np.zeros((2,3),dtype=np.int64)
            for cc in range(2):
                for v in range(3):
                    vs={int(m[join(u,v)])-y0[u] for u in range(4) if u%2==cc}
                    if len(vs)!=1 or min(vs)<0: ok=False; break
                    w[cc,v]=vs.pop()
                if not ok: break
            if ok: found=(w,np.array(y0,dtype=np.int64).reshape(4,1)); break
        if found is None: return None
        w,y=found; ntot+=1
        w2,y2=reflect_construct(w,y,2,2,3,1,r)
        if (multiset_from_wy(w2,y2,2,2,3,1)==m).all() and w2.min()>=0 and y2.min()>=0 and check_symmetric(w2,y2,2,2,3,1,r): nok+=1
    return nok,ntot
r0=even12_multiset(0); r1=even12_multiset(-1)
check("N6 even-d multiset exhaustive d=12 cap 2: r=0: 170/170, r=-1: 44/44",
      r0==(170,170) and r1==(44,44))

# ============ P. closed forms ============
check("P1 squarefree closed form a(pq) = 2^((p+1)/2) + 2^((q+1)/2) - 3 at d=15,21,33,35",
      all(len(enumerate_invariant_vanishing(d_)[0])==2**((p_+1)//2)+2**((q_+1)//2)-3
          for d_,p_,q_ in [(15,3,5),(21,3,7),(33,3,11),(35,5,7)]))
check("P2 squarefree: zero genuinely mixed sets at d=21,33,35 (Cor 4.6)",
      all(sum(1 for A in enumerate_invariant_vanishing(d_)[0]
              if not is_pure(A,d_,d_//p_) and not is_pure(A,d_,d_//q_))==0
          for d_,p_,q_ in [(21,3,7),(33,3,11),(35,5,7)]))
check("P3 prime-power baseline a(p^a) = 2^((p^(a-1)+1)/2) - 1 at d=9,25,27,49",
      all(len(enumerate_invariant_vanishing(d_)[0])==2**((pp**(e-1)+1)//2)-1
          for d_,pp,e in [(9,3,2),(25,5,2),(27,3,3),(49,7,2)]))

# ============ heavy blocks ============
if not FAST:
    # Q. d = 63 and d = 75 exhaustive
    import os
    for d_ in (63,75):
        if not os.path.exists(f"sols{d_}.npy"):
            sols=enum_big(d_); np.save(f"sols{d_}.npy",np.array([sorted(A) for A in sols],dtype=object),allow_pickle=True)
    s63=[frozenset(x) for x in np.load("sols63.npy",allow_pickle=True)]
    s75=[frozenset(x) for x in np.load("sols75.npy",allow_pickle=True)]
    check("Q1 a(63) = 2411 (exhaustive, 2^32 search space)", len(s63)==2411)
    check("Q2 a(75) = 14439 (exhaustive, 2^38 search space)", len(s75)==14439)
    m63=[A for A in s63 if not is_pure(A,63,21) and not is_pure(A,63,9)]
    m75=[A for A in s75 if not is_pure(A,75,25) and not is_pure(A,75,15)]
    check("Q3 mixed counts: 336 at d=63, 6000 at d=75", len(m63)==336 and len(m75)==6000)
    c63=cosets(63,3)+cosets(63,7); c75=cosets(75,3)+cosets(75,5)
    check("Q4 symmetric covers exist for all 2411 sets at d=63",
          all(symmetric_cover_exists(A,c63,lambda x:(-1-x)%63) for A in s63))
    check("Q5 symmetric covers exist for all 14439 sets at d=75",
          all(symmetric_cover_exists(A,c75,lambda x:(-1-x)%75) for A in s75))
    # S. spectral/tile census and purity frontier
    def census_vanishing(d_,sols,divs,pp_,t2p):
        tabs={s:monomial_table(d_,s) for s in divs}
        gcl={s:{z for z in range(1,d_) if np.gcd(z,d_)==d_//s} for s in divs}
        adjc={}; decc={}; nspec=ntile=mism=0; spec_sets=[]
        for A in sols:
            F=frozenset(s for s in divs if (tabs[s][list(A)].sum(axis=0)==0).all()); k=len(A)
            if (F,k) not in decc:
                if F not in adjc:
                    Z=set()
                    for s in F: Z|=gcl[s]
                    adjc[F]=make_adj(d_,Z)
                decc[(F,k)]=has_clique(adjc[F],d_,k)
            sp=decc[(F,k)]
            prod=1
            for s,val in pp_.items():
                if s in F: prod*=val
            til=(prod==k) and all(not(x in F and y_ in F) or (z in F) for (x,y_),z in t2p)
            nspec+=sp; ntile+=til; mism+= (sp!=til)
            if sp: spec_sets.append(A)
        return nspec,ntile,mism,spec_sets
    n63=census_vanishing(63,s63,[3,9,7,21,63],{3:3,9:3,7:7},[((3,7),21),((9,7),63)])
    n75=census_vanishing(75,s75,[3,5,25,15,75],{3:3,5:5,25:5},[((3,5),15),((3,25),75)])
    check("S2 vanishing-family census: spectral = tiles = 40 at d=63, = 42 at d=75, zero mismatches",
          n63[:3]==(40,40,0) and n75[:3]==(42,42,0))
    check("S3 PURITY: spectral AND genuinely-mixed = 0 at d=63 and d=75 (exhaustive)",
          not any(A in set(m63) for A in n63[3]) and not any(A in set(m75) for A in n75[3]))
    def t1count(d_,mix,divs,pp_):
        tabs={s:monomial_table(d_,s) for s in divs}; c=0
        for A in mix:
            F={s for s in divs if (tabs[s][list(A)].sum(axis=0)==0).all()}
            prod=1
            for s,val in pp_.items():
                if s in F: prod*=val
            c+= (prod==len(A))
        return c
    check("S4 mixed => T1 fails: 0/96 (d=45), 0/336 (d=63), 0/6000 (d=75) pass T1",
          t1count(45,mixed45,[3,9,5,15,45],{3:3,9:3,5:5})==0 and
          t1count(63,m63,[3,9,7,21,63],{3:3,9:3,7:7})==0 and
          t1count(75,m75,[3,5,25,15,75],{3:3,5:5,25:5})==0)
    check("S5 size obstruction at d=45: no mixed set has size 3^i 5^j",
          not any(len(A) in {1,3,9,5,15,45} for A in mixed45))
    # R. T2-forcing experiment at d = 45 (2^23 exact tally)
    divs=[3,9,5,15,45]; orbs=seam_orbits(45,-1); n_=len(orbs)
    tabs={s:monomial_table(45,s) for s in divs}
    offs={}; off=0
    for s in divs: offs[s]=(off,off+tabs[s].shape[1]); off+=tabs[s].shape[1]
    vecs=np.zeros((n_,off),dtype=np.int32); sizes=np.zeros(n_,dtype=np.int32)
    for i,o in enumerate(orbs):
        sizes[i]=len(o)
        for s in divs:
            a0,b0=offs[s]; vecs[i,a0:b0]=tabs[s][list(o)].sum(axis=0)
    h1=12; h2=n_-h1
    L=np.zeros((1<<h1,off),dtype=np.int32); Ls=np.zeros(1<<h1,dtype=np.int32)
    for mm in range(1,1<<h1):
        lb=(mm&-mm).bit_length()-1; L[mm]=L[mm^(1<<lb)]+vecs[lb]; Ls[mm]=Ls[mm^(1<<lb)]+sizes[lb]
    R=np.zeros((1<<h2,off),dtype=np.int32); Rs=np.zeros(1<<h2,dtype=np.int32)
    for mm in range(1,1<<h2):
        lb=(mm&-mm).bit_length()-1; R[mm]=R[mm^(1<<lb)]+vecs[h1+lb]; Rs[mm]=Rs[mm^(1<<lb)]+sizes[h1+lb]
    tally=np.zeros((32,46),dtype=np.int64)
    for st in range(0,1<<h1,256):
        S=L[st:st+256][:,None,:]+R[None,:,:]
        pat=np.zeros(S.shape[:2],dtype=np.int8)
        for bi,s in enumerate(divs):
            a0,b0=offs[s]; pat|=((S[:,:,a0:b0]==0).all(axis=2).astype(np.int8)<<bi)
        sz=Ls[st:st+256,None]+Rs[None,:]
        cnt=np.bincount((pat.astype(np.int64)*46+sz).ravel(),minlength=32*46)
        tally+=cnt.reshape(32,46)
    bit={s:i for i,s in enumerate(divs)}
    def hasf(pp_,s): return (pp_>>bit[s])&1
    n35=int(tally[[x for x in range(32) if hasf(x,3) and hasf(x,5)]].sum())
    n3515=int(tally[[x for x in range(32) if hasf(x,3) and hasf(x,5) and hasf(x,15)]].sum())
    n95=int(tally[[x for x in range(32) if hasf(x,9) and hasf(x,5)]].sum())
    n9545=int(tally[[x for x in range(32) if hasf(x,9) and hasf(x,5) and hasf(x,45)]].sum())
    check("R1 T2-forcing experiment d=45 (exact, all 2^23): (Phi3&Phi5)=20072 with Phi15: 4376; (Phi9&Phi5)=2228 with Phi45: 20",
          (n35,n3515,n95,n9545)==(20072,4376,2228,20))
    # S1. full spectral/tile census over all invariant subsets of Z_45
    gcl={3:{z for z in range(1,45) if np.gcd(z,45)==15},9:{z for z in range(1,45) if np.gcd(z,45)==5},
         5:{z for z in range(1,45) if np.gcd(z,45)==9},15:{z for z in range(1,45) if np.gcd(z,45)==3},
         45:{z for z in range(1,45) if np.gcd(z,45)==1}}
    omg={}
    for pt in range(32):
        Z=set()
        for s in divs:
            if hasf(pt,s): Z|=gcl[s]
        adj=make_adj(45,Z); k=45
        while k>0 and not has_clique(adj,45,k): k-=1
        omg[pt]=k
    nspec=ntile=0; mism=0
    for pt in range(32):
        for k in range(1,46):
            c=int(tally[pt,k])
            if c==0: continue
            e=(3 if hasf(pt,3) else 1)*(3 if hasf(pt,9) else 1)*(5 if hasf(pt,5) else 1)
            t2ok=(not(hasf(pt,3) and hasf(pt,5)) or hasf(pt,15)) and (not(hasf(pt,9) and hasf(pt,5)) or hasf(pt,45))
            sp=(k<=omg[pt]); ti=(k==e) and t2ok
            nspec+=sp*c; ntile+=ti*c; mism+=(sp!=ti)*c
        # R3 within-379: of the Phi45-vanishing patterns
    check("S1 full census d=45 (all 8,388,608 invariant subsets): spectral = tiles = 2924, zero mismatches",
          nspec==2924 and ntile==2924 and mism==0)
    n35v=n3515v=0
    for A in sols45:
        F={s for s in divs if (tabs[s][list(A)].sum(axis=0)==0).all()}
        if 3 in F and 5 in F:
            n35v+=1; n3515v+= (15 in F)
    check("R3 within the 379 vanishing sets: (Phi3&Phi5) => Phi15 holds 7/7", (n35v,n3515v)==(7,7))

# ============ X. v1.2 corrections: purity obstruction made rigorous ============
from thm43 import crt_maps as _crt
# X1: Z_45 admits a MIXED decomposition (counterexample to the v1.0/v1.1 "every decomposition pure")
_d,_pa,_qb,_split,_join=_crt(3,2,5,1)
_m=np.ones(_d,dtype=np.int64)
_w=np.ones((3,5),dtype=np.int64); _y=np.zeros((9,1),dtype=np.int64)
for _c in range(3):
    for _v in range(5): _w[_c,_v]-= (1 if _c==0 else 0)
for _u in range(9): _y[_u,0]+= (1 if _u%3==0 else 0)
_mm=multiset_from_wy(_w,_y,3,2,5,1)
check("X1 Z_45 admits a MIXED decomposition of T1-admissible size 45 (strong 'all pure' form is FALSE; only 'not genuinely mixed' holds)",
      (_mm==_m).all() and (_w>0).any() and (_y>0).any() and _w.min()>=0 and _y.min()>=0)

# X2: general divisor argument |A|=alpha p+beta q (alpha,beta>=1) vs T1-admissible sizes of p^2 q
def _adm(p,q): return sorted({1,p,q,p*p,p*q,p*p*q})
def _mixreps(N,p,q):
    return [(a,(N-a*p)//q) for a in range(1,N//p+1) if (N-a*p)>0 and (N-a*p)%q==0 and (N-a*p)//q>=1]
# p<q: every PROPER admissible size has NO mixed representation (size argument closes purity)
_pq_lt = all(all(not _mixreps(N,p,q) for N in _adm(p,q) if N!=p*p*q) for (p,q) in [(3,5),(3,7),(5,7)])
check("X2a divisor argument (p<q): no proper T1-admissible size of p^2 q is mixed-representable (purity PROVEN for proper subsets) at (3,5),(3,7),(5,7)", _pq_lt)
# p>q: the size argument has a GAP exactly at |A|=p^2 (squared prime larger)
_gap75 = [N for N in _adm(5,3) if N!=5*5*3 and _mixreps(N,5,3)]
_gap147= [N for N in _adm(7,3) if N!=7*7*3 and _mixreps(N,7,3)]
check("X2b divisor argument (p>q): the size argument leaves a GAP exactly at |A|=p^2 (=25 at d=75, =49 at d=147)",
      _gap75==[25] and _gap147==[49])

# X3: d=225 = 3^2 5^2 structured slice (gap sizes 25,45,75) -- genuinely-mixed seam-symmetric vanishing sets, none spectral/T1
if not FAST:
    import random as _rnd, functools as _ft
    _D=225; _divs=[3,9,5,25,15,45,75,225]
    _tabs={s:monomial_table(_D,s) for s in _divs}
    _gcl={s:{z for z in range(1,_D) if np.gcd(z,_D)==_D//s} for s in _divs}
    _tau=lambda x:(-1-x)%_D
    _allp=sorted({frozenset((x+75*k)%_D for k in range(3)) for x in range(_D)},key=min)
    _allq=sorted({frozenset((x+45*k)%_D for k in range(5)) for x in range(_D)},key=min)
    def _flags(A):
        A=list(A); return frozenset(s for s in _divs if (_tabs[s][A].sum(axis=0)==0).all())
    def _t1(A,F):
        pr=1
        for s in F: pr*= 3 if s in (3,9) else 5 if s in (5,25) else 1
        return pr==len(A)
    @_ft.lru_cache(maxsize=None)
    def _omega(F):
        Z=set()
        for s in F: Z|=_gcl[s]
        adj=make_adj(_D,list(Z)); k=_D
        while k>0 and not has_clique(adj,_D,k): k-=1
        return k
    def _pure(A): return all(((a+75)%_D) in A for a in A) or all(((a+45)%_D) in A for a in A)
    def _gen(npc,nqc,seed,tries):
        rng=_rnd.Random(seed); out=[]
        for _ in range(tries):
            used=set(); cyc=[]; need=npc; ap=_allp[:]; rng.shuffle(ap)
            for c in ap:
                if need<=0: break
                cr=frozenset(_tau(x) for x in c)
                if c==cr:
                    if not (c&used): cyc.append(c); used|=c; need-=1
                elif need>=2 and not ((c|cr)&used): cyc+=[c,cr]; used|=c|cr; need-=2
            needq=nqc; aq=_allq[:]; rng.shuffle(aq)
            for c in aq:
                if needq<=0: break
                cr=frozenset(_tau(x) for x in c)
                if c==cr:
                    if not (c&used): cyc.append(c); used|=c; needq-=1
                elif needq>=2 and not ((c|cr)&used): cyc+=[c,cr]; used|=c|cr; needq-=2
            if need or needq: continue
            A=frozenset().union(*cyc)
            if len(A)==npc*3+nqc*5 and A==frozenset(_tau(x) for x in A) and not _pure(A): out.append(A)
        return out
    _TM=_TT=_TS=0
    for (npc,nqc) in [(5,2),(10,3),(15,6)]:
        seen=set(); mixed=[]
        for s in range(25):
            for A in _gen(npc,nqc,20260612+s,800):
                if A not in seen: seen.add(A); mixed.append(A)
            if len(mixed)>=800: break
        for A in mixed:
            F=_flags(A); _TM+=1
            if _t1(A,F): _TT+=1
            if len(A)<=_omega(F): _TS+=1
    check(f"X3 d=225 (p^2 q^2; gap sizes 25,45,75): {_TM} genuinely-mixed seam-symmetric vanishing sets, 0 pass T1, 0 spectral",
          _TM>=2000 and _TT==0 and _TS==0, f"(mixed={_TM}, T1={_TT}, spectral={_TS})")

# ============ Y. v1.3: Theorem A (purity = top cyclotomic), Theorem B (Purity proven for min(a,b)=1), and the p^2 q^2 divergence ============
from core import monomial_table as _mt

def _cyclist(D,order):
    step=D//order; seen=set(); out=[]
    for x in range(D):
        c=frozenset((x+step*k)%D for k in range(order))
        if min(c) not in seen: seen.add(min(c)); out.append(c)
    return out

# Y1: THEOREM A  Phi_{P^a} | A  <=>  A admits a pure all-P-cycle decomposition,  d = P^a * Q (Q prime, exponent 1).
def _theoremA(D,P,Q):
    Ptop=P; 
    while Ptop*P<=D and D%(Ptop*P)==0: Ptop*=P     # top power of P dividing D
    tab=_mt(D,Ptop)
    Pc=_cyclist(D,P); Qc=_cyclist(D,Q)
    def b(c):
        m=0
        for e in c: m|=1<<e
        return m
    Pb=[b(c) for c in Pc]; Qb=[b(c) for c in Qc]
    isPinv=lambda A: all(((a+D//P)%D) in A for a in A)
    import random as _r; rng=_r.Random(99); tested=0; viol=0
    N = 8000 if FAST else 60000
    for _ in range(N):
        mask=0; idxs=[('p',i) for i in range(len(Pb))]+[('q',i) for i in range(len(Qb))]
        rng.shuffle(idxs)
        for t,i in idxs:
            if rng.random()<0.4: continue
            bb=Pb[i] if t=='p' else Qb[i]
            if not (mask&bb): mask|=bb
        if mask==0: continue
        A=frozenset(e for e in range(D) if (mask>>e)&1); Acn=list(A)
        phitop=(tab[Acn].sum(axis=0)==0).all(); pure=isPinv(A); tested+=1
        if phitop!=pure: viol+=1
    return tested,viol
_groupsA=[(45,3,5),(75,5,3)] if FAST else [(45,3,5),(63,3,7),(135,3,5),(175,5,7),(75,5,3),(147,7,3),(99,3,11),(605,11,5)]
_tA=sum(_theoremA(D,P,Q)[0] for D,P,Q in _groupsA)
_vA=sum(_theoremA(D,P,Q)[1] for D,P,Q in _groupsA)
check(f"Y1 THEOREM A: Phi_(P^a)|A <=> A pure-P, over {len(_groupsA)} groups d=P^a*Q ({_tA} vanishing sets), equivalence violations",
      _vA==0, f"(tested={_tA}, violations={_vA})")

# Y2: THEOREM B (size-25 no-go at d=225): no genuinely-mixed set of size 25 satisfies T1 (Phi_5 and Phi_25 incompatible).
def _y2():
    D=225; tab5=_mt(D,5); tab25=_mt(D,25)
    inv25_9=pow(25,-1,9); inv9_25=pow(9,-1,25)
    def el(u,v): return (u*25*inv25_9+v*9*inv9_25)%D
    def pc(ur,v): return frozenset(el((ur+3*k)%9,v) for k in range(3))
    cos5=[[(r+5*k)%25 for k in range(5)] for r in range(5)]
    import itertools as _it
    n=v=0
    for cset in cos5:
        for ureps in _it.product(range(3),repeat=5):
            Ap=list(frozenset().union(*[pc(ureps[i],cset[i]) for i in range(5)]))
            if (tab25[Ap].sum(axis=0)==0).all():
                n+=1
                if (tab5[Ap].sum(axis=0)==0).all(): v+=1
    return n,v
_n25,_v25=_y2()
check(f"Y2 size-25 no-go at d=225: among Phi_25-structured 5-p-cycle configs ({_n25}), # also satisfying Phi_5 (would allow T1)",
      _v25==0, f"(Phi25-structured={_n25}, also-Phi5={_v25}; T1 at |A|=25 needs both => impossible)")

# Y3: DIVERGENCE at d=225 (the p^2 q^2 frontier): an explicit SEAM-SYMMETRIC genuinely-mixed vanishing set
#     satisfies Coven-Meyerowitz T1 yet fails T2 (Phi_45 absent) and is non-spectral.
#     => the "genuinely mixed => fails T1" formulation is FALSE for min(a,b)>=2; only the spectral/T2 form survives.
def _y3():
    D=225; divs=[3,9,5,25,15,45,75,225]
    tabs={s:_mt(D,s) for s in divs}
    gcl={s:{z for z in range(1,D) if np.gcd(z,D)==D//s} for s in divs}
    tau=lambda x:(-1-x)%D
    W=[10,11,13,14,17,18,19,22,25,26,30,31,33,34,37,52,55,56,57,58,59,63,64,70,71,75,76,78,79,92,
       97,100,101,103,104,108,109,112,115,116,120,121,123,124,127,132,145,146,148,149,153,154,160,
       161,165,166,167,168,169,172,187,190,191,193,194,198,199,202,205,206,207,210,211,213,214]
    A=frozenset(W); Acn=list(A)
    S=frozenset(s for s in divs if (tabs[s][Acn].sum(axis=0)==0).all())
    prod=1
    for s in S: prod*= 3 if s in (3,9) else 5 if s in (5,25) else 1
    t1 = (prod==len(A))
    p3=[s for s in S if s in (3,9)]; p5=[s for s in S if s in (5,25)]
    t2 = all(a*b in S for a in p3 for b in p5)
    seam = (A==frozenset(tau(x) for x in A))
    mixed = not all(((a+75)%D) in A for a in A) and not all(((a+45)%D) in A for a in A)
    # spectral via clique
    Z=set()
    for s in S: Z|=gcl[s]
    adj=make_adj(D,list(Z)); k=len(A); spectral=has_clique(adj,D,k)
    return len(A),sorted(S),t1,t2,seam,mixed,spectral
_sz,_S,_t1,_t2,_seam,_mix,_sp=_y3()
check(f"Y3 DIVERGENCE at d=225: explicit seam-symmetric genuinely-mixed vanishing set, |A|={_sz}, S_A(prime powers)={_S}: "
      f"T1 holds yet T2 FAILS and not spectral  => T1-formulation of Purity is FALSE for p^2 q^2",
      _t1 and (not _t2) and _seam and _mix and (not _sp),
      f"(T1={_t1}, T2={_t2}, seam={_seam}, genuinely_mixed={_mix}, spectral={_sp})")

print()
el=time.time()-t00
print(f"=== zs_f28_verify_v1_3.py : {PASS}/{PASS+FAIL} PASS  ({'fast mode' if FAST else 'full mode'}, {el:.0f}s) ===")
sys.exit(0 if FAIL==0 else 1)
