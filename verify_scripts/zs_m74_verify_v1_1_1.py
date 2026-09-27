#!/usr/bin/env python3
"""M74 v1.1.1: unchanged scientific suite plus correction-only regressions.
P=0. R rows are regressions, not additional scientific evidence or grade scores.
Exit 0: all selected rows pass; 1: failed row; 2: missing dependency.
Faults: --only-regression --inject old-path-gauge|sharp-sign must exit 1.
"""
import argparse, importlib.util, json, math, platform, sys, hashlib
from pathlib import Path
from fractions import Fraction as F
from collections import Counter
ROOT=Path(__file__).resolve().parent
def module(name,path):
    spec=importlib.util.spec_from_file_location(name,path)
    m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);return m
try:
    base=module('m74_v11',ROOT/'provenance/m74_verify_v1_1.py')
    gr=module('m74_auditor_gr',ROOT/'evidence/auditor_original/gr.py')
except ImportError as exc:
    print('DEPENDENCY MISSING:',exc,file=sys.stderr);sys.exit(2)
def sha(path):return hashlib.sha256(path.read_bytes()).hexdigest()

def regressions(inject=''):
    rows=[];gauge_cases=[];jet_cases=[]
    for d in range(2,7):
        for mask in range(2**(d-1)):
            weights=[(-1)**j*(j+2) for j in range(d-1)]
            edges=[(j,j+1,0,w) if mask>>j&1 else (j,j+1,w,0) for j,w in enumerate(weights)]
            chi=F(-2);eps=F(3)
            u=[1];a=[1]
            for j in range(d-1):
                isv=(mask>>j)&1;u.append(u[-1]*(-1 if isv else 1));a.append(a[-1]*(1 if isv else -1))
            if inject=='old-path-gauge': u=[1]*d;a=[(-1)**j for j in range(d)]
            hp0,hm0=gr.build(d,edges,{d-1:eps},{})
            hp1,hm1=gr.build(d,edges,{}, {0:chi})
            U=all(u[i]*u[j]*hp0[i][j]==hm0[i][j] for i in range(d) for j in range(d))
            A=all(a[i]*a[j]*hp1[i][j]==-hm1[i][j] for i in range(d) for j in range(d))
            gauge_cases.append(dict(d=d,mask=mask,U=U,A=A))
            hp,hm=gr.build(d,edges,{d-1:eps},{0:chi})
            jets=gr.delta_jets_all(hp,hm,2*d)
            below=all(v.iszero() for cs in jets.values() for v in cs[:2*d])
            pred=F(8*(d-1)*(-1)**(d-1),math.factorial(2*d))*chi*eps*math.prod(w*w for w in weights)
            if inject=='sharp-sign':pred=-pred
            got=jets[(0,0)][2*d]
            jet_cases.append(dict(d=d,mask=mask,lower_all_zero=below,coefficient=str(got),expected=str(pred),passed=below and got==pred))
    rows.append(dict(id='R01',cls='R',claim='F12-03: U/A gauges for every coloured path, d=2..6',passed=all(x['U'] and x['A'] for x in gauge_cases),cases=gauge_cases,arithmetic='exact Gaussian rational; 62 colourings'))
    rows.append(dict(id='R02',cls='R',claim='F12-03: all-entry lower jets and (6.1) for the same 62 paths',passed=all(x['passed'] for x in jet_cases),cases=jet_cases,arithmetic='exact Liouvillian recurrence; chi=-2, epsilon=3, w_j=(-1)^j(j+2)'))
    parity=[]
    for aa,bb,ell,c2 in [(1,4,0,'VVLL'),(3,4,0,'LLLL'),(1,6,1,'LLLLLL')]:
        edges=[];diag={};nxt=max(aa,1)
        if aa==1:diag[0]=F(7)
        else:
            for j in range(aa):
                w=(-1)**j*(j+2);edges.append((j,(j+1)%aa,0,w) if j==0 else (j,(j+1)%aa,w,0))
        at=0
        for j in range(ell):edges.append((at,nxt,5+j,0));at=nxt;nxt+=1
        cyc=[at]+list(range(nxt,nxt+bb-1));nxt+=bb-1
        for j,col in enumerate(c2):
            w=gr.G((-1)**j*(j+2))*(gr.G(F(3,5),F(4,5)) if j==0 else 1)
            edges.append((cyc[j],cyc[(j+1)%bb],w,0) if col=='L' else (cyc[j],cyc[(j+1)%bb],0,w))
        hp,hm=gr.build(nxt,edges,{},diag);N=aa+bb+2*ell
        coeff=gr.delta_jets_all(hp,hm,N+1)[(0,cyc[1])]
        ok=all(x.iszero() for x in coeff[:N]) and not coeff[N].iszero() and coeff[N+1].iszero()
        parity.append(dict(a=aa,b=bb,ell=ell,cycle=c2,leading=str(coeff[N]),next=str(coeff[N+1]),passed=ok))
    rows.append(dict(id='R03',cls='R',claim='Explicit next-order parity computation for the three auditor declaration cases',passed=all(x['passed'] for x in parity),cases=parity,arithmetic='exact Gaussian rational; finite instances, not a universal proof'))
    sp=base.sp;D,b,beta=sp.symbols('D b beta',real=True)
    chi=D+b
    det=lambda z,s:sp.expand(chi*(2*s-1)+(z-1)*chi+beta)
    exprs=[sp.expand(det(1,0)+D-(beta-b)),sp.expand(det(1,1)-D-(beta+b)),sp.expand(det(-1,0)+2*chi+D-(beta-b)),sp.expand(det(-1,1)+D-(beta-b))]
    # beta in [-b,b], D>0 makes these four affine endpoint bounds rigorous.
    correlated=[];p=F(1,10)
    for n in [3,5,7,9]:
        dist={(0,)*n:1-p,(1,)*n:p}
        marg=[sum(pr for es,pr in dist.items() if es[j]) for j in range(n)]
        maj=sum(pr for es,pr in dist.items() if sum(es)>n//2)
        independent=sum(F(math.comb(n,k))*p**k*(1-p)**(n-k) for k in range(n//2+1,n+1))
        ok=all(x==p for x in marg) and maj==p and maj>independent
        correlated.append(dict(R=n,majority=str(maj),independent_tail=str(independent),passed=ok))
    rows.append(dict(id='R04',cls='R',claim='Calculate the two operational claims previously represented by declarations',passed=all(x==0 for x in exprs) and all(x['passed'] for x in correlated),endpoint_residuals=list(map(str,exprs)),domain='D=chi-b>0, b>=0, -b<=beta<=b; four affine endpoint identities',correlated=correlated))
    return rows

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',default='m74_verify_v1_1_1.json')
    parser.add_argument('--only-regression',action='store_true')
    parser.add_argument('--inject',choices=['old-path-gauge','sharp-sign'],default='')
    args=parser.parse_args()
    rows=[] if args.only_regression else base.run()
    rows+=regressions(args.inject)
    census={k:sum(r['cls']==k for r in rows) for k in ['P','C','V','W','R','G','X','D','T']}
    out=dict(paper='ZS-M74 v1.1.1',profile='REGRESSION' if args.only_regression else 'FULL',inject=args.inject,rows=rows,census=census,passed=sum(bool(r['passed']) for r in rows),failed=sum(not r['passed'] for r in rows),scientific_rows=sum(census[k] for k in ['P','C','V','W']),control_rows=census['R']+census['G'],environment=dict(python=platform.python_version(),numpy=base.np.__version__,scipy=base.scipy.__version__,sympy=base.sp.__version__),source_sha256={str(p.relative_to(ROOT)):sha(p) for p in [ROOT/'ZS-M74_v1_1_1.md',ROOT/'provenance/m74_verify_v1_1.py',ROOT/'evidence/auditor_original/gr.py',Path(__file__).resolve()]},limitations='No universal formal proof, independent review, novelty or grade inference; original 18 classes unchanged; R rows are regressions.')
    Path(args.output).write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({k:out[k] for k in ['profile','passed','failed','scientific_rows','control_rows','census']}))
    return 1 if out['failed'] else 0
if __name__=='__main__':sys.exit(main())
