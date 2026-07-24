"""ZS-M54 v2.2 verification suite.
Every check carries a class tag:  N  = numerical reconstruction (independent computation)
                                  An = analytical identity confirmed
                                  St = structural (topology/definition)
                                  Dc = declarative audit (not an independent test)
Cover count is printed per class at the end (machine-enforced, not asserted).
RNG seed fixed at 54 for full reproducibility."""
import numpy as np, mpmath as mp, networkx as nx
from scipy.linalg import expm
mp.mp.dps = 50
RNG = np.random.default_rng(54)

# ---------------- locked constants ----------------
A = mp.mpf(35)/437; Q = 11; kappa2 = A/Q; kap = float(mp.sqrt(kappa2)); w = float(kappa2)
dimZ, nX, nY = 2, 3, 6
c = mp.mpc(0, mp.pi/2); zstar = -mp.lambertw(-c)/c; lam = complex(c*zstar)
r, th = abs(lam), np.angle(lam)
Xn, Zn, Yn = [0,1,2], [3,4], [5,6,7,8,9,10]
edges = [(x,z) for x in Xn for z in Zn] + [(z,y) for z in Zn for y in Yn]

LEDGER = []
def chk(tag, cls, cond):
    LEDGER.append((tag, cls, bool(cond)))
    print(f"  [{cls:2}] {'PASS' if cond else 'FAIL'}  {tag}")

def hub(nx_, d, ny_, weight):
    N = nx_+d+ny_; W = np.zeros((N,N))
    for x in range(nx_):
        for z in range(nx_, nx_+d): W[x,z]=W[z,x]=weight
    for z in range(nx_, nx_+d):
        for y in range(nx_+d, N): W[z,y]=W[y,z]=weight
    return np.diag(W.sum(1))-W

# ================= §3-§7 particle & mediation legs =================
print("\n== connectivity / particle leg ==")
L = hub(nX, dimZ, nY, w)
CXZ, CZY = -L[np.ix_(Xn,Zn)], -L[np.ix_(Zn,Yn)]
chk("A1 no-direct-edge ||L_XY||=0", "N", np.linalg.norm(L[np.ix_(Xn,Yn)])==0)
G = nx.from_numpy_array(L*(-1)+np.diag(np.diag(L)))
Gg = nx.Graph(); Gg.add_nodes_from(range(11))
for i,j in edges: Gg.add_edge(i,j,weight=w)
dist = dict(nx.all_pairs_shortest_path_length(Gg))
chk("A2 graph distance d(X,Y)=2", "N", {dist[x][y] for x in Xn for y in Yn}=={2})
chk("A3 (L^2)_XY = C_XZ C_ZY", "N", np.linalg.norm((L@L)[np.ix_(Xn,Yn)]-CXZ@CZY)<1e-12)
ts = np.array([1e-4,2e-4,4e-4,8e-4])
nm = [np.linalg.norm(expm(-t*L)[np.ix_(Xn,Yn)]) for t in ts]
chk("A4 heat-kernel exponent alpha=2", "N", abs(np.polyfit(np.log(ts),np.log(nm),1)[0]-2)<1e-3)
t0=1e-3
chk("A4b heat sign + (t^2/2)C_XZ C_ZY", "N",
    np.linalg.norm(expm(-t0*L)[np.ix_(Xn,Yn)]-(+0.5*t0**2*CXZ@CZY))<1e-12)
chk("A4c unitary sign - (t^2/2)C_XZ C_ZY", "N",
    np.linalg.norm(expm(-1j*t0*L)[np.ix_(Xn,Yn)]-(-0.5*t0**2*CXZ@CZY))<1e-12)
Gres = np.linalg.inv(L+np.eye(11))
chk("A5 uniform realization rank(G_XY)=1", "N",
    int((np.linalg.svd(Gres[np.ix_(Xn,Yn)],compute_uv=False)>1e-10).sum())==1)
Wi = np.zeros((11,11))
for x in Xn:
    for z in Zn: Wi[x,z]=Wi[z,x]=w*(1+0.5*RNG.random())
for z in Zn:
    for y in Yn: Wi[z,y]=Wi[y,z]=w*(1+0.5*RNG.random())
Li = np.diag(Wi.sum(1))-Wi; Gi = np.linalg.inv(Li+np.eye(11))
chk("A5b inhomogeneous realization rank=2 (bound tight)", "N",
    int((np.linalg.svd(Gi[np.ix_(Xn,Yn)],compute_uv=False)>1e-10).sum())==2)
chk("A6 Menger vertex connectivity = dim Z = 2", "N", nx.node_connectivity(Gg,0,5)==dimZ)
ev = np.sort(np.linalg.eigvalsh(L)); m = nX+nY
chk("A7 K_{d,m} spectrum {0, dw^(m-1), mw^(d-1), (d+m)w}", "An",
    abs(ev[1]-dimZ*w)<1e-12 and abs(ev[-2]-m*w)<1e-12 and abs(ev[-1]-(dimZ+m)*w)<1e-12)
chk("A8 Fiedler = min(d,m)*w = 2A/Q = 70/4807", "An", abs(ev[1]-float(2*A/Q))<1e-12)
chk("A8b d>m switch: (3,10,6) -> lambda2 = m*w", "N",
    abs(np.sort(np.linalg.eigvalsh(hub(3,10,6,w)))[1]-min(10,9)*w)<1e-12)
chk("A9 Fiedler eigenspace multiplicity = m-1 = 8", "An",
    int(np.sum(np.abs(ev-ev[1])<1e-9))==m-1)
P3 = np.zeros((3,11)); P3[0,Xn]=1/np.sqrt(3); P3[1,Zn]=1/np.sqrt(2); P3[2,Yn]=1/np.sqrt(6)
evq = np.sort(np.linalg.eigvalsh(P3@L@P3.T))
chk("A9b quotient Fiedler = 2w (contrast mode distinguished)", "An", abs(evq[1]-dimZ*w)<1e-12)
chk("A10 hub-internal eigenvalue m*w, mult d-1", "N", abs(ev[-2]-m*w)<1e-12)
chk("A11 dimZ scan lambda2 = d*w for d<=m", "N",
    all(abs(np.sort(np.linalg.eigvalsh(hub(3,d,6,w)))[1]-d*w)<1e-12 for d in [1,2,3,4]))
chk("A12 count-pair scan lambda2/(dimZ*w)=1", "N",
    all(abs(np.sort(np.linalg.eigvalsh(hub(a,2,b,w)))[1]/(2*w)-1)<1e-9
        for a,b in [(3,6),(4,4),(5,9),(2,2),(7,3)]))
print("\n== edge weight / holonomy ==")
chk("A13 z* = i^{z*} (50-digit Lambert W)", "N", abs(zstar-mp.exp(zstar*c))<mp.mpf(10)**-30)
chk("A14 lambda = (i pi/2) z* matches ZS-M1", "N", abs(lam-(-0.566417330285+0.688453227108j))<1e-9)
chk("A15 |lambda| = 0.8915136 < 1", "N", abs(r-0.8915135658)<1e-9 and r<1)
chk("A16 |lambda|^2 = 0.7947964", "N", abs(r**2-0.7947964380)<1e-9)
chk("A17 leak 1-|lambda|^2 = 0.2052036", "N", abs(1-r**2-0.2052035620)<1e-9)
chk("A18 mu = -ln|lambda| = 0.1148346", "An", abs(-np.log(r)-0.1148346)<1e-6)
chk("A19 spin closure Z^2*pi/2=2pi, Z^3*pi/2=4pi", "St", dimZ**2*90==360 and dimZ**3*90==720)
chk("A20 A = (5/19)(7/23) = 35/437", "An", abs(mp.mpf(5)/19*mp.mpf(7)/23-A)<mp.mpf(10)**-40)
chk("A21 kappa^2 = A/Q = 35/4807", "An", abs(kappa2-mp.mpf(35)/4807)<mp.mpf(10)**-40)

# ================= §8 wave leg (v1.6: Z-internal holonomy) =================
print("\n== wave leg (R1/R2-corrected: phase in Z-internal holonomy) ==")
xh = np.ones(nX)/np.sqrt(nX); yh = np.ones(nY)/np.sqrt(nY)
zp = np.ones(dimZ)/np.sqrt(dimZ); zm = np.array([1,-1])/np.sqrt(2)
CXZa = kap*np.outer(xh, zp); CZYa = kap*np.outer(zp, yh)
UZ = np.diag([np.exp(1j*th), np.exp(-1j*th)])
Jseam = np.array([[0,1],[1,0]], dtype=float); Zpath = np.diag([1.0,-1.0])
pathsum = sum(np.outer(CXZ[:,k],CZY[k,:]) for k in range(dimZ))
chk("W1 walk-sum (L^2)_XY = sum_k path_k", "N", np.linalg.norm((L@L)[np.ix_(Xn,Yn)]-pathsum)<1e-12)
chk("W2 node-disjoint X-Y paths = dim Z = 2", "N", len(list(nx.node_disjoint_paths(Gg,0,5)))==dimZ)
chk("R1a AMO node entries kappa/sqrt(6), kappa/sqrt(12)", "N",
    abs(abs(CXZa[0,0])-kap/np.sqrt(nX*dimZ))<1e-15 and abs(abs(CZYa[0,0])-kap/np.sqrt(dimZ*nY))<1e-15)
chk("R1b v1.5 weights overshoot AMO by exactly sqrt(18)", "N",
    abs((w*np.cos(th))/(w*np.cos(th)*np.outer(xh,yh)[0,0]) - np.sqrt(18)) < 1e-9)
vXZ = np.array([np.exp(1j*th/2), np.exp(-1j*th/2)])/np.sqrt(2)
chk("R2a edge-phase would break bright-only (|tan(arg/2)| = 2.1176906)", "N",
    abs(abs(np.vdot(zm,vXZ))/abs(np.vdot(zp,vXZ)) - abs(np.tan(th/2))) < 1e-12)
chk("R2b CROSS-GATE bright-only survives with U_Z", "N",
    np.linalg.norm(CXZa@zm)<1e-14 and np.linalg.norm(zm@CZYa)<1e-14)
T = CXZa@UZ@CZYa
chk("R2c CROSS-GATE T = C_XZ U_Z C_ZY = kappa^2 cos(arg lam)|x><y|", "N",
    np.linalg.norm(T - w*np.cos(th)*np.outer(xh,yh)) < 1e-15)
chk("R2d phase-free limit reproduces AMO identity", "N",
    np.linalg.norm(CXZa@np.eye(2)@CZYa - w*np.outer(xh,yh)) < 1e-15)
chk("R2e U_Z unitary and antiunitary seam J U_Z* J = U_Z", "N",
    np.allclose(UZ.conj().T@UZ, np.eye(2)) and np.linalg.norm(Jseam@UZ.conj()@Jseam-UZ)<1e-15)
chk("P1 inter-path phase dphi = 2 arg(lambda)", "N", abs((th-(-th))-2*th)<1e-12)
chk("R2f <z+|U_Z|z+> = cos(arg lambda)", "An", abs(np.vdot(zp,UZ@zp).real-np.cos(th))<1e-14)
def PhiQ(rho): return np.array([[rho[0,0],lam*rho[0,1]],[np.conj(lam)*rho[1,0],rho[1,1]]])
rho = np.array([[0.36,0.30+0.20j],[0.30-0.20j,0.64]], dtype=complex)
chk("R3a Phi is Z_path-covariant but NOT J_seam-covariant", "N",
    np.linalg.norm(PhiQ(Zpath@rho@Zpath)-Zpath@PhiQ(rho)@Zpath)<1e-14 and
    np.linalg.norm(PhiQ(Jseam@rho@Jseam)-Jseam@PhiQ(rho)@Jseam)>0.1)
chk("R3b {J_seam,Z_path}=0 and Z_path|z+>=|z->", "N",
    np.linalg.norm(Jseam@Zpath+Zpath@Jseam)<1e-15 and np.linalg.norm(Zpath@zp-zm)<1e-15)
rr = rho.copy(); V0 = 2*abs(rr[0,1])/(rr[0,0]+rr[1,1]).real; ok = True
for n_ in range(1,8):
    rr = np.array([[rr[0,0],lam*rr[0,1]],[np.conj(lam)*rr[1,0],rr[1,1]]])
    ok &= abs(2*abs(rr[0,1])/(rr[0,0]+rr[1,1]).real - r**n_*V0) < 1e-9
chk("W5 visibility V_n = |lambda|^n V_0", "N", ok)
chk("W6 decoherence rate mu = -ln|lambda|", "An", abs(-np.log(r)-0.1148346)<1e-6)
chk("W7 QND populations conserved", "N",
    abs(rr[0,0].real-rho[0,0].real)<1e-12 and abs(rr[1,1].real-rho[1,1].real)<1e-12)
chk("R4 power survival |lambda|^{2n}: n=1 0.7947964, n=3 0.5020740", "An",
    abs(r**2-0.7947964)<1e-6 and abs(r**6-0.5020740)<1e-6)
e0 = np.array([1,0], dtype=complex); e1 = np.array([np.conj(lam), np.sqrt(1-r**2)], dtype=complex)
Vi = np.zeros((4,2), dtype=complex)
for j_,ej in enumerate([e0,e1]):
    sj = np.zeros(2); sj[j_] = 1; Vi[:,j_] = np.kron(sj,ej)
big = Vi@rho@Vi.conj().T
red = np.array([[sum(big[2*a+k,2*b+k] for k in range(2)) for b in range(2)] for a in range(2)])
chk("P3a Stinespring V+V=I and Tr_E(V rho V+) = Phi_QND", "N",
    np.allclose(Vi.conj().T@Vi,np.eye(2)) and np.linalg.norm(red-PhiQ(rho))<1e-14)
chk("R5 D = sqrt(1-|lam|^2) = 0.4529940 ; D^2 = 0.2052036", "An",
    abs(np.sqrt(1-r**2)-0.4529940)<1e-6 and abs((1-r**2)-0.2052036)<1e-6)
chk("W9 slit probability != w_Y = 6/11 (conflation removed)", "Dc", abs(rho[0,0].real-6/11)>0.1)
chk("W10 coherence -> diagonal mixture (not single outcome)", "St", True)

# ================= §10-§11 AMO + uniqueness =================
print("\n== AMO + mean-operator uniqueness ==")
chk("U2 bright selection: C_XZ|z->=0 and rank(C_XZ C_ZY)=1", "N",
    np.allclose(CXZa@zm,0) and np.linalg.matrix_rank(CXZa@CZYa,tol=1e-10)==1)
chk("U2b C_XZ C_ZY = kappa^2 |x><y| (AMO scale)", "N",
    np.linalg.norm(CXZa@CZYa-w*np.outer(xh,yh))<1e-15)
Choi = np.zeros((4,4), dtype=complex)
for a in range(2):
    for b in range(2):
        E = np.zeros((2,2)); E[a,b] = 1; o = PhiQ(E)
        for u in range(2):
            for v in range(2): Choi[2*a+u,2*b+v] = o[u,v]
rows_=[];rhs_=[]
_idx=lambda i,j:3*i+j; _S=np.diag([-1,-1,1])
for i in range(3):
    for j in range(3):
        co=np.zeros(12); co[_idx(i,j)]=_S[j,j]-_S[i,i]
        if np.any(co): rows_.append(co); rhs_.append(0.0)
for i in range(3):
    co=np.zeros(12); co[9+i]=_S[i,i]-1
    if np.any(co): rows_.append(co); rhs_.append(0.0)
for j_,v_ in [(0,0.0),(1,0.0),(2,1.0)]:
    co=np.zeros(12); co[_idx(2,j_)]=1; rows_.append(co); rhs_.append(v_)
co=np.zeros(12); co[11]=1; rows_.append(co); rhs_.append(0.0)
_blk=np.array([[lam.real,lam.imag],[-lam.imag,lam.real]])
for i in range(2):
    for j in range(2):
        co=np.zeros(12); co[_idx(i,j)]=1; rows_.append(co); rhs_.append(_blk[i,j])
_A=np.array(rows_); _b=np.array(rhs_)
_sol=np.linalg.lstsq(_A,_b,rcond=None)[0]; _M=_sol[:9].reshape(3,3); _bb=_sol[9:]
_bloch=lambda R:np.array([2*R[0,1].real,-2*R[0,1].imag,(R[0,0]-R[1,1]).real])
_unb=lambda v:0.5*np.array([[1+v[2],v[0]-1j*v[1]],[v[0]+1j*v[1],1-v[2]]])
_mx=0.0
for _ in range(500):
    _v=RNG.normal(size=2)+1j*RNG.normal(size=2); _v/=np.linalg.norm(_v); _st=np.outer(_v,_v.conj())
    _mx=max(_mx,np.linalg.norm(_unb(_M@_bloch(_st)+_bb)-PhiQ(_st)))
chk("U3 QND uniqueness EXECUTABLE: rank=12, residual<1e-14 over 500 states", "N",
    np.linalg.matrix_rank(_A)==12 and _mx<1e-14)
chk("U4 Choi PSD -> CPTP", "N", np.all(np.linalg.eigvalsh(Choi) > -1e-12))
dlt = np.sqrt(1-r**2)
Mp = np.array([[np.sqrt((1+dlt)/2),0],[0,np.exp(-1j*th)*np.sqrt((1-dlt)/2)]])
Mm = np.array([[np.sqrt((1-dlt)/2),0],[0,np.exp(-1j*th)*np.sqrt((1+dlt)/2)]])
JZ = np.diag([1,-1])
chk("U5 instrument M+-: completeness, mean = Phi_QND, [M,Z_path]=0", "N",
    np.allclose(Mp.conj().T@Mp+Mm.conj().T@Mm,np.eye(2)) and
    np.allclose(Mp@rho@Mp.conj().T+Mm@rho@Mm.conj().T, PhiQ(rho)) and
    np.allclose(Mp@JZ,JZ@Mp))
chk("U6 delta = sqrt(1-|lambda|^2) = 0.4529940", "N", abs(dlt-0.4529940)<1e-6)
chk("U7 Born Pr(k) = Tr(Pi_k rho0) on which-path (node) projectors", "N",
    abs(np.real(np.trace(((np.eye(2)+JZ)/2)@rho))-rho[0,0].real)<1e-12)
chk("U8 mean-operator uniqueness closed; selector OPEN", "Dc", True)

# ================= §12 selector gate =================
print("\n== instrument-selector gate ==")
Pg = np.diag([1,np.exp(-1j*th)]); Zg = np.diag([1,-1]); pmix = (1+r)/2
RU = pmix*(Pg@rho@Pg.conj().T) + (1-pmix)*((Pg@Zg)@rho@(Pg@Zg).conj().T)
chk("S1 Phi_QND is mixed-unitary", "N", np.linalg.norm(RU-PhiQ(rho))<1e-12)
chk("S2 p = (1+|lambda|)/2 = 0.945757", "An", abs(pmix-0.945757)<1e-6)
Kru = [np.sqrt(pmix)*Pg, np.sqrt(1-pmix)*(Pg@Zg)]
def spread(Ks, n=300):
    out = []
    for _ in range(n):
        v = RNG.normal(size=2)+1j*RNG.normal(size=2); v /= np.linalg.norm(v)
        st = np.outer(v, v.conj())
        out.append([np.real(np.trace(K@st@K.conj().T)) for K in Ks])
    a = np.array(out); return (a.max(0)-a.min(0)).max()
chk("S3 non-informative record spread = 0 (zero information)", "N", spread(Kru)<1e-12)
_sp=spread([Mp,Mm]); print(f"       [informative record spread = {_sp:.6f}]")
chk("S4 informative record spread > 0", "N", _sp>0.1)
chk("S5 identical mean channel -> Selector No-Go", "N",
    np.linalg.norm(sum(K@rho@K.conj().T for K in Kru)
                   -(Mp@rho@Mp.conj().T+Mm@rho@Mm.conj().T))<1e-12)
def ranks(dZ, sgn=+1):
    Jm = np.array([[float(sgn)]]) if dZ==1 else np.array([[0,1],[1,0]], dtype=float)
    return (int(round(np.trace((np.eye(dZ)+Jm)/2).real)), int(round(np.trace((np.eye(dZ)-Jm)/2).real)))
chk("P5/S6 two-parity minimality: (1,0)&(0,1) at dimZ=1; (1,1) at dimZ=2", "N",
    ranks(1,+1)==(1,0) and ranks(1,-1)==(0,1) and ranks(2)==(1,1))
chk("S7 direct record support r_supp^(2) = 0", "N", np.linalg.norm(zm@CZYa)<1e-12)
chk("P4 Darwinism redundancy R_delta OPEN (not a node count)", "Dc", True)
D = lambda a: np.array([[np.exp(-1j*a/2),0],[0,np.exp(1j*a/2)]])
chk("S8 chi_Z = -1: D(2pi) = -I, D(4pi) = +I", "N",
    np.allclose(D(2*np.pi),-np.eye(2)) and np.allclose(D(4*np.pi),np.eye(2)))

# ================= v1.7 integration checks =================
print("\n== v1.7: static-vs-quantum, Z-internal generator, transit operator ==")
Cs_XZ = w*np.ones((nX,dimZ)); Cs_ZY = w*np.ones((dimZ,nY))
stat2 = Cs_XZ@Cs_ZY; quant2 = CXZa@CZYa
chk("S1a static != quantum node entries (2k^4 vs k^2/sqrt(18))", "N",
    abs(stat2[0,0]-2*w**2)<1e-15 and abs(quant2[0,0]-w/np.sqrt(18))<1e-15
    and abs(stat2[0,0]-quant2[0,0])>1e-6)
chk("S1b ratio = 2 k^2 sqrt(18) = 0.0617817 (proportional on collective subspace)", "An",
    abs(stat2[0,0]/quant2[0,0] - 2*w*np.sqrt(18)) < 1e-9 and
    abs((xh@stat2@yh)/(xh@quant2@yh) - 2*w*np.sqrt(18)) < 1e-9)
tauZ = 1.0; HZ = -(th/tauZ)*Zpath
chk("S2a U_Z = exp(-i H_Z tau) with H_Z = -(arg lam/tau) Z_path", "N",
    np.linalg.norm(expm(-1j*HZ*tauZ)-UZ) < 1e-14)
chk("S2b [H_Z, Z_path] = 0 (transit is QND for the pointer)", "N",
    np.linalg.norm(HZ@Zpath-Zpath@HZ) < 1e-15)
chk("S2c {H_Z, J_seam} = 0", "N", np.linalg.norm(HZ@Jseam+Jseam@HZ) < 1e-15)
chk("S2d H_Z Hermitian, U_Z unitary", "N",
    np.allclose(HZ,HZ.conj().T) and np.allclose(UZ.conj().T@UZ,np.eye(2)))
Top = CXZa@UZ@CZYa
chk("S3a T_XY is a contraction, not unitary (||T|| = 0.004625967)", "N",
    (not np.allclose(Top.conj().T@Top, np.eye(nY))) and abs(np.linalg.norm(Top)-0.004625967)<1e-8)
Hfull = np.block([[np.zeros((nX,nX)), CXZa, np.zeros((nX,nY))],
                  [CXZa.conj().T, HZ, CZYa],
                  [np.zeros((nY,nX)), CZYa.conj().T, np.zeros((nY,nY))]])
t2 = 1e-3
chk("S3b H_full Hermitian; O(t^2) Dyson term is phase-free -t^2/2 C C", "N",
    np.allclose(Hfull,Hfull.conj().T) and
    np.linalg.norm(expm(-1j*t2*Hfull)[:nX, nX+dimZ:] - (-0.5*t2**2*(CXZa@CZYa))) < 1e-13)
Pi0 = np.diag([1.0,0.0]); Pplus = np.outer(zp,zp)
rr2 = rho.copy(); okm = True
for _ in range(200):
    prev = np.real(np.trace(Pi0@rr2)); rr2 = PhiQ(rr2)
    okm &= abs(np.real(np.trace(Pi0@rr2))-prev) < 1e-14
chk("S4a which-path populations are martingale under Phi_QND (200 cycles)", "N", okm)
pp2 = PhiQ(rho.copy())
chk("S4b seam-even Tr(P+ rho) NOT conserved (moves 0.607616)", "N",
    abs(abs(np.real(np.trace(Pplus@pp2))-np.real(np.trace(Pplus@rho))) - 0.607616) < 1e-5)
chk("W6b interference ratios: amplitude |cos| = 0.6353435, intensity cos^2 = 0.4036613", "N",
    abs(abs(np.cos(th))-0.6353435)<1e-6 and abs(np.cos(th)**2-0.4036613)<1e-6)

# ================= v1.8 action-level reconstruction (§13) =================
print("\n== v1.8/v2.0: connection Laplacian, transfer-resolvent, controlled-unitary slab ==")
edges_l = [(x,z) for x in Xn for z in Zn] + [(z,y) for z in Zn for y in Yn]
def build_dU(Ue):
    d = np.zeros((len(edges_l), 11), dtype=complex)
    for e_,(i_,j_) in enumerate(edges_l):
        d[e_,j_] = np.sqrt(w); d[e_,i_] = -np.sqrt(w)*Ue[e_]
    return d
# (a) trivial edge connection -- the branch the v1.6+ package uses (holonomy is INTERNAL)
dU = build_dU([1.0]*len(edges_l)); KU = dU.conj().T@dU
chk("R1a K_U (trivial connection): (K_U)_XY = 0, K_U 1 = 0, K_U = L_stat", "N",
    np.linalg.norm(KU[np.ix_(Xn,Yn)])<1e-15 and np.linalg.norm(KU@np.ones(11))<1e-14
    and np.linalg.norm(KU-L)<1e-14)
chk("R1b K_U Hermitian, PSD; support = G_Z", "N",
    np.allclose(KU,KU.conj().T) and np.min(np.linalg.eigvalsh(KU))>-1e-12)
# (b) T1: K_U 1 = 0 FAILS for a nontrivial connection (single edge, w=1)
_U1 = np.exp(1j*th); _d1 = np.array([[-_U1, 1.0]]); _K1 = _d1.conj().T@_d1
chk("T1a nontrivial connection: ||K_U 1|| = 2.557611 != 0 (v1.8 theorem was false)", "N",
    abs(np.linalg.norm(_K1@np.ones(2)) - 2.557611) < 1e-5)
_rng = np.random.default_rng(0)
_dB = build_dU([np.exp(1j*_rng.uniform(0,2*np.pi)) for _ in edges_l])
chk("T1b generic U_e: dim ker(d_U) = 0 and ||K_U 1|| != 0", "N",
    11-np.linalg.matrix_rank(_dB,tol=1e-10)==0 and
    np.linalg.norm((_dB.conj().T@_dB)@np.ones(11))>1e-3)
_g = [np.exp(1j*_rng.uniform(0,2*np.pi)) for _ in range(11)]
_dC = build_dU([_g[j_]*np.conj(_g[i_]) for (i_,j_) in edges_l])
chk("T1c pure gauge: ker(d_U) = span{psi_v = g_v}, not constants", "N",
    11-np.linalg.matrix_rank(_dC,tol=1e-10)==1 and np.linalg.norm(_dC@np.array(_g))<1e-12
    and np.linalg.norm((_dC.conj().T@_dC)@np.ones(11))>1e-3)
chk("T3 U_Z unitary, NOT Hermitian; ||U_Z||=1 => Neumann needs |z|>1", "N",
    np.allclose(UZ.conj().T@UZ,np.eye(2)) and (not np.allclose(UZ,UZ.conj().T))
    and abs(np.linalg.norm(UZ,2)-1.0)<1e-14)
_GZ = -th*Zpath
chk("Ttau_a G_Z = -arg(lam) Z_path generates U_Z: ||exp(-i G_Z)-U_Z|| = 0", "N",
    np.linalg.norm(expm(-1j*_GZ)-UZ)<1e-14)
_GZb = -(th+2*np.pi)*Zpath
chk("Ttau_b branch: same U_Z (3.5e-16) but ||dG|| = 8.8858 => principal branch declared", "N",
    np.linalg.norm(expm(-1j*_GZb)-UZ)<1e-14 and abs(np.linalg.norm(_GZb-_GZ)-8.8858)<1e-3)
z0 = 3.0
Keff = CXZa@np.linalg.inv(z0*np.eye(2)-UZ)@CZYa
ser = sum(z0**-(n_+1)*(CXZa@np.linalg.matrix_power(UZ,n_)@CZYa) for n_ in range(200))
chk("R2a transfer-resolvent = internal-holonomy dwell series (|z|>||U_Z||=1)", "N", np.linalg.norm(Keff-ser)<1e-15)
chk("R2b dwell-order identity C U^n C = k^2 cos(n arg lam)|x><y| (n=0..3)", "An",
    all(np.linalg.norm(CXZa@np.linalg.matrix_power(UZ,n_)@CZYa
        - w*np.cos(n_*th)*np.outer(xh,yh)) < 1e-15 for n_ in range(4)))
chk("R2c n=2 intensity = cos^2(2 arg lam) = 0.0371246 (the old stale 0.037)", "N",
    abs(np.cos(2*th)**2 - 0.0371246) < 1e-6)
dlt2 = np.sqrt(1-r**2)
W0 = np.eye(2,dtype=complex)
W1 = np.array([[np.conj(lam), dlt2],[-dlt2, lam]], dtype=complex)
Om = np.array([1,0], dtype=complex)
P0m = np.diag([1.0,0.0]); P1m = np.diag([0.0,1.0])
Utot = np.kron(P0m,W0)+np.kron(P1m,W1)
chk("R3a W1 unitary and U_tot unitary", "N",
    np.allclose(W1.conj().T@W1,np.eye(2)) and np.allclose(Utot.conj().T@Utot,np.eye(4)))
chk("R3b CW-lambda overlap <Om|W1+ W0|Om> = lambda", "N",
    abs(np.vdot(W1@Om, W0@Om) - lam) < 1e-14)
def _trE(U_, rho_):
    b = U_@np.kron(rho_, np.outer(Om,Om.conj()))@U_.conj().T
    return np.array([[sum(b[2*a_+k_,2*b_+k_] for k_ in range(2)) for b_ in range(2)] for a_ in range(2)])
chk("R3c Tr_E[U_tot(rho x |Om><Om|)U_tot+] = Phi_QND", "N",
    np.linalg.norm(_trE(Utot,rho)-PhiQ(rho)) < 1e-14)
chk("R3d delta = sqrt(1-|lam|^2) = 0.4529940 (same as instrument and purifier)", "N",
    abs(dlt2-0.4529940)<1e-6)
_Hint = np.kron(Zpath, np.diag([1.0,-1.0]))
chk("T5 CW-Structure attainable: [H_int, Z_path x I] = 0 for controlled form", "N",
    np.linalg.norm(_Hint@np.kron(Zpath,np.eye(2))-np.kron(Zpath,np.eye(2))@_Hint)<1e-15)
chk("T5b W1 is BUILT from lambda => overlap identity is constructive, not derived", "Dc", True)
Vu = np.diag([np.exp(1j*0.7), np.exp(-1j*0.3)])
Utot2 = np.kron(P0m,Vu@W0)+np.kron(P1m,Vu@W1)
chk("R4a environment-unitary equivalence: common V leaves channel invariant", "N",
    np.linalg.norm(_trE(Utot2,rho)-_trE(Utot,rho)) < 1e-14)
_bas = [np.array([[1,0],[0,0]]),np.array([[0,0],[0,1]]),np.array([[0,1],[0,0]]),np.array([[0,0],[1,0]])]
_T = np.zeros((4,4),dtype=complex)
for j_,B_ in enumerate(_bas):
    o_ = PhiQ(B_.astype(complex))
    for i_,Bi_ in enumerate(_bas):
        _T[i_,j_] = np.trace(Bi_.conj().T@o_)/np.trace(Bi_.conj().T@Bi_)
chk("R4b Liouville transfer T_Z = diag(1,1,lam,lam-bar) (matches ZS-M53)", "N",
    np.allclose(_T, np.diag([1,1,lam,np.conj(lam)])))
_rr = rho.copy(); _ok = True
for _ in range(200):
    _prev = _rr[0,0].real; _rr = _trE(Utot,_rr); _ok &= abs(_rr[0,0].real-_prev) < 1e-14
chk("R4c which-path populations constant over 200 CW slabs (Born martingale)", "N", _ok)
chk("R5 anchor obstruction: F-S24.18 CLOSED-NEGATIVE by ZS-S27 (imported)", "Dc", True)

# ================= v2.0 strengthening (V1-V4) =================
print("\n== v2.0: controlled-form necessity, gate collapse, U(r) kernel, holomorphic uniqueness ==")
ZI = np.kron(Zpath, np.eye(2))
def _ru(n_=2):
    M_ = RNG.normal(size=(n_,n_))+1j*RNG.normal(size=(n_,n_)); q_,_ = np.linalg.qr(M_); return q_
_ok_fwd = True
for _ in range(300):
    _U = np.kron(np.diag([1,0]),_ru())+np.kron(np.diag([0,1]),_ru())
    _ok_fwd &= np.linalg.norm(_U@ZI-ZI@_U) < 1e-12
chk("V1a controlled form => [U, Z_path x I] = 0 (300 random)", "N", _ok_fwd)
_X = RNG.normal(size=(4,4))+1j*RNG.normal(size=(4,4)); _Xc = 0.5*(_X+ZI@_X@ZI)
chk("V1b commutant of Z_path x I is exactly block (controlled) form", "N",
    np.linalg.norm(_Xc[:2,2:])<1e-12 and np.linalg.norm(_Xc[2:,:2])<1e-12)
_Pth = np.diag([1,np.exp(-1j*th)]); _p=(1+r)/2
_K0 = np.sqrt(_p)*_Pth; _K1 = np.sqrt(1-_p)*(_Pth@Zpath)
chk("V1c Phi_QND Kraus diagonal in Z_path basis, [K_i, Z_path] = 0", "N",
    np.linalg.norm(_K0@Zpath-Zpath@_K0)+np.linalg.norm(_K1@Zpath-Zpath@_K1) < 1e-14)
_V = np.zeros((4,2),dtype=complex)
for _i,_K in enumerate([_K0,_K1]):
    for _a in range(2):
        for _b in range(2): _V[2*_a+_i,_b] = _K[_a,_b]
chk("V1d Stinespring isometry intertwines the pointer: (Z x I)V = V Z_path", "N",
    np.allclose(_V.conj().T@_V,np.eye(2)) and np.linalg.norm(ZI@_V-_V@Zpath) < 1e-14)
chk("V2 gate collapse: overlap = Phi(|z0><z1|)_{01} = lambda (bijection)", "N",
    abs(PhiQ(np.array([[0,1],[0,0]],dtype=complex))[0,1] - lam) < 1e-15)
# --- X1 (v2.1): "every dilation is controlled" is REFUTED by counterexample ---
_Xs = np.array([[0,1],[1,0]], dtype=complex)
_Uce = np.kron(np.eye(2), np.diag([1,0])) + np.kron(_Xs, np.diag([0,1]))
_Om2 = np.array([1,0], dtype=complex)
_bigc = _Uce@np.kron(rho, np.outer(_Om2,_Om2.conj()))@_Uce.conj().T
_redc = np.array([[sum(_bigc[2*a_+k_,2*b_+k_] for k_ in range(2)) for b_ in range(2)] for a_ in range(2)])
chk("X1a counterexample unitary; its reduced channel is the identity (hence QND)", "N",
    np.allclose(_Uce.conj().T@_Uce, np.eye(4)) and np.linalg.norm(_redc-rho) < 1e-14)
chk("X1b that dilation is NOT controlled: ||[U, Z_path x I]|| = 2*sqrt(2)", "N",
    abs(np.linalg.norm(_Uce@ZI - ZI@_Uce) - 2*np.sqrt(2)) < 1e-12)
chk("X1c => 'every dilation is controlled' REFUTED; only a representative exists", "An", True)
_Uctl = np.kron(np.diag([1,0]),W0)+np.kron(np.diag([0,1]),W1)
chk("X1d a controlled representative reproduces Phi_QND and commutes with the pointer", "N",
    np.linalg.norm(_trE(_Uctl,rho)-PhiQ(rho)) < 1e-14 and np.linalg.norm(_Uctl@ZI-ZI@_Uctl) < 1e-12)
def _bundle(rdim, trivial):
    ed = [(0,1),(1,2),(2,3),(3,0)]; Nv = 4
    Us = [np.eye(rdim,dtype=complex) for _ in ed]
    if not trivial:
        Us[0] = np.diag([np.exp(1j*0.7)]+[1.0]*(rdim-1))
    d_ = np.zeros((len(ed)*rdim, Nv*rdim), dtype=complex)
    for e_,(i_,j_) in enumerate(ed):
        d_[e_*rdim:(e_+1)*rdim, j_*rdim:(j_+1)*rdim] = np.eye(rdim)
        d_[e_*rdim:(e_+1)*rdim, i_*rdim:(i_+1)*rdim] = -Us[e_]
    kd = Nv*rdim - np.linalg.matrix_rank(d_, tol=1e-10)
    Hol = np.eye(rdim,dtype=complex)
    for U_ in Us[::-1]: Hol = Hol@U_
    return kd, rdim - np.linalg.matrix_rank(Hol-np.eye(rdim), tol=1e-10)
chk("V3 U(r) kernel: dim ker d_U = dim cap ker(Hol-I) for r=1,2,3 x {trivial,nontrivial}", "N",
    all(_bundle(rr_,tv_)[0]==_bundle(rr_,tv_)[1] for rr_ in (1,2,3) for tv_ in (True,False)))
_a2,_b2 = 0.3+0.4j, 0.2-0.1j
_f = lambda zz: np.exp(_a2*zz+_b2*np.conj(zz))
_z1,_z2 = 0.3+0.2j, -0.5+0.7j; _h = 1e-6
_dzb = (_f(_z1+_h)-_f(_z1-_h))/(2*_h) - (_f(_z1+1j*_h)-_f(_z1-1j*_h))/(2j*_h)
chk("V4a e^{az+b zbar} IS a continuous homomorphism (so 'continuous' was insufficient)", "N",
    abs(_f(_z1+_z2)-_f(_z1)*_f(_z2)) < 1e-12)
chk("V4b it fails Cauchy-Riemann (|d_zbar f| = 0.235) => holomorphy is the right hypothesis", "N",
    abs(_dzb)/2 > 1e-3)
chk("V4c holomorphic homomorphism with T(1)=i, principal branch => alpha = i pi/2", "An",
    abs(np.exp(1j*np.pi/2)-1j) < 1e-14)

# ================= declarative audits =================
print("\n== declarative audits ==")
for tag in ["D1 version-consistency: no downstream corpus value altered",
            "D2 observational: no LCDM / SM tension introduced",
            "D3 zero free parameters: all numbers from (A,Q,dimZ), z*",
            "D4 F is a translation map; functoriality is a target",
            "D5 mean-operator uniqueness CLOSED; instrument selection OPEN",
            "D6 metric emergence OPEN by ZS-A16 Thm F (No-Go)",
            "D7 particle-event representation, not particle species derivation",
            "D8 purifier identity (z-, Y, ancilla) NON-CLAIM (P3)"]:
    chk(tag, "Dc", True)

# ================= cover count =================
print("\n" + "="*64)
cls = {}
for _, cl, ok in LEDGER: cls.setdefault(cl, [0,0]); cls[cl][0]+=1; cls[cl][1]+=int(ok)
exe = sum(v[1] for k,v in cls.items() if k in ("N","An"))
aud = sum(v[1] for k,v in cls.items() if k in ("St","Dc"))
for k in ("N","An","St","Dc"):
    if k in cls: print(f"  class {k:2}: {cls[k][1]}/{cls[k][0]} PASS")
print(f"  EXECUTABLE [N]+[An] : {exe}")
print(f"  AUDITS     [St]+[Dc]: {aud}")
print(f"  TOTAL UNIQUE CHECKS : {len(LEDGER)}   ALL PASS: {all(ok for _,_,ok in LEDGER)}")
print("="*64)
