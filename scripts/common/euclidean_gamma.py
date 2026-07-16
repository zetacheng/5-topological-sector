"""Euclidean gamma matrices used by the migrated Paper 5 calculations.

Extracted from legacy fierz_verify.py at
e4f65785f408ab7e8645c181f692f08503ff718f. Fierz-channel calculations below
the extraction boundary are deliberately excluded as Paper 3-owned.
"""

import numpy as np
np.set_printoptions(precision=4, suppress=True, linewidth=140)

# ---------- Euclidean gamma matrices (hermitian, chiral rep) ----------
s0=np.eye(2); s1=np.array([[0,1],[1,0]],dtype=complex)
s2=np.array([[0,-1j],[1j,0]]); s3=np.array([[1,0],[0,-1]],dtype=complex)
def kron(a,b): return np.kron(a,b)
# gamma_mu hermitian, {gmu,gnu}=2delta
g=[None]*5
g[1]=kron(s1,s1*0+np.array([[0,1],[1,0]]))  # placeholder; build canonical set below
# canonical Euclidean chiral: gamma_i = [[0, -i sigma_i],[i sigma_i, 0]], gamma_4=[[0,1],[1,0]]
def blk(a,b,c,d): return np.block([[a,b],[c,d]])
Z=np.zeros((2,2),dtype=complex)
g[1]=blk(Z,-1j*s1,1j*s1,Z)
g[2]=blk(Z,-1j*s2,1j*s2,Z)
g[3]=blk(Z,-1j*s3,1j*s3,Z)
g[4]=blk(Z,s0,s0,Z)
g5=g[1]@g[2]@g[3]@g[4]
# checks
for mu in range(1,5):
    for nu in range(1,5):
        assert np.allclose(g[mu]@g[nu]+g[nu]@g[mu], 2*(mu==nu)*np.eye(4)), (mu,nu)
    assert np.allclose(g[mu].conj().T, g[mu])
assert np.allclose(g5.conj().T, g5) and np.allclose(g5@g5, np.eye(4))

