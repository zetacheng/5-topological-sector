import numpy as np
from itertools import permutations
from scripts.common.euclidean_gamma import g, g5
G5=g5.astype(complex)
GM=[g[1],g[2],g[3],g[4]]
rng=np.random.default_rng(11)
NMC=800_000; CH=100_000; LAM=1.0; VOL=np.pi**2/2
pts=rng.normal(size=(NMC,4)); pts/=np.linalg.norm(pts,axis=1,keepdims=True)
P=pts*(rng.uniform(size=NMC)**0.25)[:,None]

def Sb(Pc,k,m):
    q=Pc+k; q2=np.einsum('ni,ni->n',q,q)
    sl=q[:,0,None,None]*GM[0]+q[:,1,None,None]*GM[1]+q[:,2,None,None]*GM[2]+q[:,3,None,None]*GM[3]
    return (-1j*sl+m*np.eye(4))/(q2+m*m)[:,None,None]

def box(kk,m):
    orders=[((0,1,2,3),-2.0),((0,1,3,2),2.0),((0,2,1,3),2.0)]
    tot=0.0
    for od,fl in orders:
        k1,k2,k3,k4=[kk[i] for i in od]
        acc=0.0
        for s in range(0,NMC,CH):
            Pc=P[s:s+CH]
            S1=Sb(Pc,np.zeros(4),m);S2=Sb(Pc,k1,m);S3=Sb(Pc,k1+k2,m);S4=Sb(Pc,k1+k2+k3,m)
            M=np.einsum('ab,nbc,cd,nde,ef,nfg,gh,nha->n',G5,S2,G5,S3,G5,S4,G5,S1,optimize=True)
            acc+=np.sum(M.real)
        tot+=fl*(-1.0)*(acc/NMC)*VOL/(2*np.pi)**4
    return tot

def op_vertex(kk,which):
    tot=0.0
    for perm in permutations(range(4)):
        l=[kk[i] for i in perm]; fl=[0,1,0,1]; f=[fl[i] for i in perm]
        if which=='O1' and f[0]==f[1] and f[2]==f[3]: tot+=(l[0]@l[1])*(l[2]@l[3])
        if which=='O2' and f[0]==f[1] and f[2]==f[3]: tot+=(l[0]@l[2])*(l[1]@l[3])
    return tot

def a4(cfg,m,lams=(0.4,0.55,0.7,0.85,1.0)):
    vals=[box([lam*k for k in cfg],m) for lam in lams]
    L=np.array(lams); X=np.vstack([L**2,L**4,L**6]).T
    c,_,_,_=np.linalg.lstsq(X,np.array(vals),rcond=None)
    return c[0],c[1]

e=0.18
cfgA=[np.array([e,0,0,0]),np.array([0,e,0,0]),np.array([-e,0,0,0]),np.array([0,-e,0,0])]
cfgB=[np.array([e,0,0,0]),np.array([0.7*e,0.71*e,0,0]),np.array([-e,0,0,0]),np.array([-0.7*e,-0.71*e,0,0])]
import sys
m=float(sys.argv[1])
rows=[]
for cfg in [cfgA,cfgB]:
    A2,A4=a4(cfg,m)
    rows.append((A4,op_vertex(cfg,'O1'),op_vertex(cfg,'O2'),A2))
Mx=np.array([[rows[0][1],rows[0][2]],[rows[1][1],rows[1][2]]])
b=np.array([rows[0][0],rows[1][0]])
c1,c2=np.linalg.solve(Mx,b); kap=(c1-c2)/2
print(f"m={m}: A4_A={rows[0][0]:+.6e} A4_B={rows[1][0]:+.6e} V=(A:{rows[0][1]:.4e},{rows[0][2]:.4e} B:{rows[1][1]:.4e},{rows[1][2]:.4e})")
print(f"m={m}: c1={c1:+.6f} c2={c2:+.6f} kappa_Skyrme={kap:+.6f}  A2(cfgA)={rows[0][3]:+.6f}")
# Z_pi anchor
def Sb1(Pc,k,mm):
    q=Pc+k;q2=np.einsum('ni,ni->n',q,q)
    sl=q[:,0,None,None]*GM[0]+q[:,1,None,None]*GM[1]+q[:,2,None,None]*GM[2]+q[:,3,None,None]*GM[3]
    return (-1j*sl+mm*np.eye(4))/(q2+mm*mm)[:,None,None]
def twopt(mm,km):
    k=np.array([km,0,0,0]);acc=0.0
    for s in range(0,NMC,CH):
        Pc=P[s:s+CH];S1=Sb1(Pc,np.zeros(4),mm);S2=Sb1(Pc,k,mm)
        acc+=np.sum(np.einsum('ab,nbc,cd,nda->n',G5,S2,G5,S1,optimize=True).real)
    return (acc/NMC)*VOL/(2*np.pi)**4
Zpi=(twopt(m,1e-4)-twopt(m,0.15))/0.15**2
print(f"m={m}: Z_pi = {Zpi:+.6f} (anchor: healthy kinetic term requires >0)")
