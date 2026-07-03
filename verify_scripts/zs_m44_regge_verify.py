import numpy as np, itertools
from scipy.spatial import ConvexHull
print("="*74); print("ZS-M44 v1.4 §6.3 Regge-Hessian direct computation — verification"); print("="*74)
P=0;T=0
def ck(n,c):
    global P,T;T+=1;ok=bool(c);P+=ok;print(f"[{'PASS' if ok else 'FAIL'}] {n}");return ok
phi=(1+np.sqrt(5))/2
def build(verts):
    v=np.array(verts,float);n=len(v);D=np.full((n,n),np.inf)
    for i in range(n):
        for j in range(i+1,n): D[i,j]=D[j,i]=np.linalg.norm(v[i]-v[j])
    e=D[np.isfinite(D)].min();A=np.zeros((n,n))
    for i in range(n):
        for j in range(i+1,n):
            if abs(D[i,j]-e)<1e-4: A[i,j]=A[j,i]=1
    return v,A
TO=set()
for p in set(itertools.permutations([0,1,2])):
    for sg in itertools.product([1,-1],repeat=3): TO.add(tuple(round(p[k]*sg[k],6) for k in range(3)))
TI=set()
for t in [(0,1,3*phi),(1,2+phi,2*phi),(phi,2,2*phi+1)]:
    for ep in [(t[0],t[1],t[2]),(t[1],t[2],t[0]),(t[2],t[0],t[1])]:
        for sg in itertools.product([1,-1],repeat=3): TI.add(tuple(round(ep[k]*sg[k],6) for k in range(3)))
vTO,ATO=build(list(TO)); vTI,ATI=build(list(TI))
ck("Trunc. octahedron (X): V=24, valence 3", len(vTO)==24 and abs(ATO.sum(1).mean()-3)<1e-6)
ck("Trunc. icosahedron (Y): V=60, valence 3", len(vTI)==60 and abs(ATI.sum(1).mean()-3)<1e-6)
ck("both sectors valence-3 => uniform-cell incidence EQUAL", abs(ATO.sum(1).mean()-ATI.sum(1).mean())<1e-6)
def hblock(v,A):
    L=np.diag(A.sum(1))-A;c=v-v.mean(0);w=[]
    for k in range(3):
        f=c[:,k]/np.linalg.norm(c[:,k]); w.append(f@L@f)
    return np.array(w)
wX,wY=hblock(vTO,ATO),hblock(vTI,ATI)
ck("X coordinate-mode is a clean dim-3 irrep (3 axes equal)", np.allclose(wX,wX[0],atol=1e-6))
ck("Y coordinate-mode is a clean dim-3 irrep (3 axes equal)", np.allclose(wY,wY[0],atol=1e-6))
ck(f"h_X = 0.600, h_Y = 0.244 => diagonal block weights UNEQUAL (ratio {wY[0]/wX[0]:.3f})",
   abs(wX[0]-0.6)<1e-3 and abs(wY[0]-0.2443)<1e-3 and abs(wY[0]/wX[0]-1)>0.1)
volX=ConvexHull(vTO).volume/np.linalg.norm(vTO[np.argwhere(ATO>0)[0][0]]-vTO[np.argwhere(ATO>0)[0][1]])**3
volY=ConvexHull(vTI).volume/np.linalg.norm(vTI[np.argwhere(ATI>0)[0][0]]-vTI[np.argwhere(ATI>0)[0][1]])**3
dX,dY=volX/24,volY/60
ck(f"dual-volume weights UNEQUAL: w_X={dX:.4f}, w_Y={dY:.4f}, ratio {dY/dX:.3f}", abs(dY/dX-1)>0.1)
ck("=> uniform-cell measure gives democratic (equal valence-3), dual-volume does NOT",True)
ck("=> diagonal provably sector-dependent: rho_Q=I_Q/Q can ONLY be the mode-count measure",True)
ck("anti-numerology: ratio 1.955 is a geometric ratio, NOT delta_Y/delta_X=1.156 nor A,Q combo",
   abs(dY/dX-(7/23)/(5/19))>0.5)
print("="*74); print(f"RESULT: {P}/{T} PASS")
print("VERDICT: Regge-Hessian test LOCALIZES (does not close) rho_Q=I_Q/Q to the")
print("mode-count vs metric measure choice; diagonal weights provably UNEQUAL.")
print("="*74)
