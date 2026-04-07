"""Z-Sim v1.0 — Icosahedral Rotation Group I ≅ A₅ Representation Engine.

Canonical source: ZS-M9 v1.0 (McKay Correspondence)
                  ZS-M10 v1.0 (Explicit Yukawa CG Tensor)
                  ZS-M11 v1.0 (Icosahedral Yukawa Completion)

Constructs all 60 rotations of I ≅ A₅ and all 5 irreducible representations:
    dim 1  — trivial
    dim 3  — natural (icosahedral rotations on ℝ³)
    dim 3' — conjugate (from vertex permutation, Frobenius reciprocity)
    dim 4  — gauge (vector-like, Δ=0)
    dim 5  — Higgs (anti-chiral, Δ=−1), from traceless Sym²(ℝ³)

Chirality classification [ZS-M9]:
    Δ = +1: irreps 1, 3, 3' (fermion-like)
    Δ =  0: irrep 4 (gauge)
    Δ = −1: irrep 5 (Higgs)

The golden ratio φ = (1+√5)/2 controls the representation theory.
"""

from __future__ import annotations

import itertools
import math
from dataclasses import dataclass, field
from typing import Final

import numpy as np

Array = np.ndarray

# =====================================================================
# Golden ratio and icosahedral geometry
# =====================================================================

PHI: Final[float] = (1.0 + math.sqrt(5.0)) / 2.0  # φ = 1.618...
PHI_INV: Final[float] = PHI - 1.0                    # 1/φ = φ − 1 = 0.618...
_TOL: Final[float] = 1e-10


def _rotation_matrix(axis: Array, angle: float) -> Array:
    """Construct 3D rotation matrix from axis and angle (Rodrigues)."""
    axis = axis / np.linalg.norm(axis)
    K = np.array([
        [0, -axis[2], axis[1]],
        [axis[2], 0, -axis[0]],
        [-axis[1], axis[0], 0],
    ])
    return np.eye(3) + math.sin(angle) * K + (1 - math.cos(angle)) * (K @ K)


# =====================================================================
# Icosahedron geometry
# =====================================================================

def icosahedron_vertices() -> Array:
    """Return 12 vertices of a regular icosahedron (unit circumradius)."""
    verts = []
    for s1, s2 in itertools.product([1, -1], repeat=2):
        verts.append([0, s1, s2 * PHI])
        verts.append([s1, s2 * PHI, 0])
        verts.append([s2 * PHI, 0, s1])
    verts = np.array(verts, dtype=np.float64)
    # normalize to unit sphere
    norms = np.linalg.norm(verts, axis=1, keepdims=True)
    return verts / norms


# =====================================================================
# Generate all 60 rotations of I ≅ A₅
# =====================================================================

def generate_icosahedral_rotations() -> list[Array]:
    """Generate all 60 proper rotation matrices of the icosahedral group I.

    Strategy: Start with generators (C₅ around a vertex axis, C₃ around
    a face axis), then close the group under multiplication.

    Returns:
        List of 60 rotation matrices (3×3, SO(3)).
    """
    verts = icosahedron_vertices()

    # C₅ generator: rotation by 2π/5 around a vertex axis
    axis_c5 = verts[0] / np.linalg.norm(verts[0])
    R_c5 = _rotation_matrix(axis_c5, 2 * math.pi / 5)

    # C₃ generator: rotation by 2π/3 around a face center
    # Find 3 vertices that form a triangular face
    dists = np.linalg.norm(verts - verts[0], axis=1)
    neighbors = np.argsort(dists)[1:6]  # 5 nearest neighbors
    # Pick two adjacent neighbors
    v0 = verts[0]
    v1 = verts[neighbors[0]]
    # Find a third vertex adjacent to both v0 and v1
    d_from_v1 = np.linalg.norm(verts - v1, axis=1)
    edge_len = np.linalg.norm(v1 - v0)
    for idx in neighbors[1:]:
        if abs(np.linalg.norm(verts[idx] - v1) - edge_len) < 0.1:
            v2 = verts[idx]
            break
    face_center = (v0 + v1 + v2) / 3.0
    axis_c3 = face_center / np.linalg.norm(face_center)
    R_c3 = _rotation_matrix(axis_c3, 2 * math.pi / 3)

    # Close the group
    group: list[Array] = [np.eye(3)]
    seen = {_mat_key(np.eye(3))}

    generators = [R_c5, R_c3]
    queue = list(generators)

    while queue:
        g = queue.pop(0)
        key = _mat_key(g)
        if key in seen:
            continue
        seen.add(key)
        group.append(g.copy())
        for gen in generators:
            for new in [g @ gen, gen @ g, np.linalg.inv(g)]:
                nk = _mat_key(new)
                if nk not in seen:
                    queue.append(new)

    assert len(group) == 60, f"|I| = {len(group)}, expected 60"
    return group


def _mat_key(m: Array, decimals: int = 6) -> tuple:
    """Hashable key for a matrix (rounded)."""
    return tuple(np.round(m.ravel(), decimals))


# =====================================================================
# Conjugacy classes
# =====================================================================

@dataclass(frozen=True)
class ConjugacyClass:
    """A conjugacy class of I ≅ A₅."""
    name: str
    order: int     # element order
    size: int      # class size
    trace: float   # trace of 3-dim rep (character χ₃)


def classify_conjugacy(rotations: list[Array]) -> list[ConjugacyClass]:
    """Classify 60 rotations into 5 conjugacy classes by trace of the 3-rep.

    Expected classes:
        e:      size 1,  tr=3,    order 1
        C₂:     size 15, tr=-1,   order 2  [(12)(34) type]
        C₃:     size 20, tr=0,    order 3  [(123) type]
        C₅:     size 12, tr=φ,    order 5  [(12345) type]
        C₅²:    size 12, tr=1-φ,  order 5  [(13245) type]
    """
    traces = [np.trace(R) for R in rotations]
    # Round and bin
    bins: dict[float, list[int]] = {}
    for i, t in enumerate(traces):
        t_round = round(t, 4)
        found = False
        for key in bins:
            if abs(key - t_round) < 0.01:
                bins[key].append(i)
                found = True
                break
        if not found:
            bins[t_round] = [i]

    classes = []
    for trace_val, indices in sorted(bins.items(), key=lambda x: -x[0]):
        size = len(indices)
        # Determine element order from trace
        R = rotations[indices[0]]
        order = _element_order(R)
        name = _class_name(trace_val, order, size)
        classes.append(ConjugacyClass(name=name, order=order, size=size, trace=trace_val))

    assert sum(c.size for c in classes) == 60
    assert len(classes) == 5, f"Expected 5 conjugacy classes, got {len(classes)}"
    return classes


def _element_order(R: Array, max_order: int = 10) -> int:
    """Find the order of rotation matrix R."""
    power = np.eye(3)
    for n in range(1, max_order + 1):
        power = power @ R
        if np.allclose(power, np.eye(3), atol=1e-8):
            return n
    return -1


def _class_name(trace: float, order: int, size: int) -> str:
    if size == 1:
        return "e"
    if order == 2:
        return "C₂"
    if order == 3:
        return "C₃"
    if order == 5 and trace > 0.5:
        return "C₅"
    if order == 5:
        return "C₅²"
    return f"??(tr={trace:.3f},ord={order})"


# =====================================================================
# Irreducible representations
# =====================================================================

def character_table() -> dict[str, list[float]]:
    """Return the character table of I ≅ A₅.

    Columns: e(1), C₂(15), C₃(20), C₅(12), C₅²(12)
    Rows: irreps 1, 3, 3', 4, 5
    """
    return {
        "1":  [1, 1, 1, 1, 1],
        "3":  [3, -1, 0, PHI, 1 - PHI],
        "3'": [3, -1, 0, 1 - PHI, PHI],
        "4":  [4, 0, 1, -1, -1],
        "5":  [5, 1, -1, 0, 0],
    }


def rep_3(rotations: list[Array]) -> list[Array]:
    """Return the 3-dim natural representation (rotations themselves)."""
    return [R.copy() for R in rotations]


def rep_5_from_sym2(rotations: list[Array]) -> list[Array]:
    """Construct the 5-dim irrep as traceless Sym²(ℝ³).

    The symmetric square representation acts on symmetric 3×3 matrices
    via S → R S Rᵀ. The traceless subspace (dim=5) is the irrep.

    Uses the CORRECTED convention [ZS-M11 §2.1]:
        M[a,b] = ⟨b_a, g·b_b·gᵀ⟩ (homomorphism, NOT anti-homomorphism)
    """
    # Basis for 6-dim symmetric matrices (orthonormal)
    basis_6 = _sym_basis_6()

    # Project out trace to get 5-dim traceless subspace
    trace_vec = np.array([b.trace() for b in basis_6])
    trace_vec = trace_vec / np.linalg.norm(trace_vec)

    # Build projector onto traceless subspace
    P_traceless = np.eye(6) - np.outer(trace_vec, trace_vec)

    # Find 5-dim orthonormal basis of traceless subspace
    eigvals, eigvecs = np.linalg.eigh(P_traceless)
    idx_nonzero = np.where(eigvals > 0.5)[0]
    assert len(idx_nonzero) == 5, f"Expected 5 traceless modes, got {len(idx_nonzero)}"
    basis_5 = eigvecs[:, idx_nonzero]  # 6×5 matrix

    reps = []
    for R in rotations:
        # 6×6 representation on full Sym²
        M6 = np.zeros((6, 6))
        for a in range(6):
            for b in range(6):
                # Correct convention: M[a,b] = Tr(b_a · R · b_b · Rᵀ)
                M6[a, b] = np.trace(basis_6[a] @ R @ basis_6[b] @ R.T)
        # Project to 5-dim traceless subspace
        M5 = basis_5.T @ M6 @ basis_5
        reps.append(M5)

    # Verify homomorphism property
    _verify_homomorphism(rotations, reps, "5-dim")

    return reps


def rep_3prime_from_vertices(rotations: list[Array]) -> list[Array]:
    """Construct the 3'-dim irrep from vertex permutation representation.

    The 12-dim vertex permutation decomposes as: 12 = 1 ⊕ 3 ⊕ 3' ⊕ 5
    [Frobenius reciprocity with Z₅ vertex stabilizer].

    Extract 3' via character projection:
        P_{3'} = (3/60) Σ_g χ_{3'}(g) P_perm(g)
    """
    verts = icosahedron_vertices()
    n_verts = len(verts)
    assert n_verts == 12

    # Build permutation representation
    # CRITICAL CONVENTION [ZS-M11 §2.1]: P[j,i] = 1 when g maps v_i to v_j.
    # This gives P(g₁)P(g₂) = P(g₁g₂) (homomorphism).
    # The WRONG convention P[i,j]=1 gives anti-homomorphism P(g₁)P(g₂)=P(g₂g₁).
    perm_reps = []
    for R in rotations:
        P = np.zeros((n_verts, n_verts))
        rotated = (R @ verts.T).T
        for i in range(n_verts):
            dists = np.linalg.norm(verts - rotated[i], axis=1)
            j = np.argmin(dists)
            assert dists[j] < 1e-6, f"No vertex match for rotated vertex {i}"
            P[j, i] = 1.0  # g maps v_i → v_j
        perm_reps.append(P)

    # Character projection using trace of 3-rep to identify class
    # χ₃'(class) values mapped by trace of χ₃:
    #   tr(3)=3    → e    → χ₃'=3
    #   tr(3)=-1   → C₂   → χ₃'=-1
    #   tr(3)=0    → C₃   → χ₃'=0
    #   tr(3)=φ    → C₅   → χ₃'=1-φ  (conjugate swap!)
    #   tr(3)=1-φ  → C₅²  → χ₃'=φ    (conjugate swap!)
    trace_to_chi3p = {
        3.0: 3.0,
        -1.0: -1.0,
        0.0: 0.0,
        round(PHI, 4): round(1.0 - PHI, 4),
        round(1.0 - PHI, 4): round(PHI, 4),
    }

    projector = np.zeros((n_verts, n_verts))
    for g_idx, P in enumerate(perm_reps):
        tr3 = round(np.trace(rotations[g_idx]), 4)
        # Find matching trace key
        chi_val = None
        for key, val in trace_to_chi3p.items():
            if abs(tr3 - key) < 0.01:
                chi_val = val
                break
        assert chi_val is not None, f"No class match for trace {tr3}"
        projector += chi_val * P
    projector *= 3.0 / 60.0

    # Verify projector
    proj_err = np.max(np.abs(projector @ projector - projector))
    assert proj_err < 1e-4, \
        f"P² ≠ P, error = {proj_err}"
    rank = int(round(np.trace(projector)))
    assert rank == 3, f"Projector rank = {rank}, expected 3"

    # Extract 3-dim subspace
    eigvals, eigvecs = np.linalg.eigh(projector)
    idx = np.where(eigvals > 0.5)[0]
    assert len(idx) == 3
    basis = eigvecs[:, idx]  # 12×3

    # Project permutation matrices to 3-dim
    reps_3prime = []
    for P in perm_reps:
        M3 = basis.T @ P @ basis
        reps_3prime.append(M3)

    _verify_homomorphism(rotations[:10], reps_3prime[:10], "3'-dim")

    return reps_3prime


def _sym_basis_6() -> list[Array]:
    """Orthonormal basis for 6-dim real symmetric 3×3 matrices."""
    basis = []
    # Diagonal: e_ii
    for i in range(3):
        m = np.zeros((3, 3))
        m[i, i] = 1.0
        basis.append(m)
    # Off-diagonal: (e_ij + e_ji)/√2
    for i in range(3):
        for j in range(i + 1, 3):
            m = np.zeros((3, 3))
            m[i, j] = 1.0 / math.sqrt(2.0)
            m[j, i] = 1.0 / math.sqrt(2.0)
            basis.append(m)
    return basis


def _verify_homomorphism(rotations: list[Array], reps: list[Array],
                          name: str, n_checks: int = 10) -> None:
    """Verify ρ(g₁)ρ(g₂) = ρ(g₁g₂) for random pairs."""
    n = min(n_checks, len(rotations))
    max_err = 0.0
    for i in range(n):
        for j in range(n):
            # Find g₁g₂ in the group
            product = rotations[i] @ rotations[j]
            # Find closest group element
            for k, Rk in enumerate(rotations):
                if np.allclose(Rk, product, atol=1e-8):
                    err = np.max(np.abs(reps[i] @ reps[j] - reps[k]))
                    max_err = max(max_err, err)
                    break
    assert max_err < 1e-4, f"{name} homomorphism error = {max_err}"


# =====================================================================
# Yukawa tensor: unique invariant in 3 ⊗ 5 ⊗ 3'
# =====================================================================

def compute_yukawa_invariant(reps_3: list[Array],
                              reps_5: list[Array],
                              reps_3p: list[Array]) -> Array:
    """Compute the unique I-invariant tensor T in 3 ⊗ 5 ⊗ 3'.

    dim Hom_I(1, 3⊗5⊗3') = 1 [ZS-M10 Theorem 2.1, PROVEN]

    Uses group averaging: T = (1/|I|) Σ_g (ρ₃(g) ⊗ ρ₅(g) ⊗ ρ₃'(g)) · T₀
    where T₀ is any seed tensor.

    Returns:
        T: shape (3, 5, 3) — the unique (up to normalization) invariant tensor.
    """
    n_group = len(reps_3)
    d3, d5, d3p = 3, 5, 3

    # Random seed tensor
    rng = np.random.RandomState(42)
    T0 = rng.randn(d3, d5, d3p)

    # Group average
    T_avg = np.zeros_like(T0)
    for g in range(n_group):
        R3 = reps_3[g]
        R5 = reps_5[g]
        R3p = reps_3p[g]
        # Apply ρ₃ ⊗ ρ₅ ⊗ ρ₃' to T0
        T_rotated = np.einsum('ia,jb,kc,abc->ijk', R3, R5, R3p, T0)
        T_avg += T_rotated
    T_avg /= n_group

    # Normalize
    norm = np.sqrt(np.sum(T_avg**2))
    if norm < 1e-12:
        raise RuntimeError("Yukawa invariant projection gave zero — seed issue")
    T_avg /= norm

    # Verify I-invariance
    max_err = 0.0
    for g in range(n_group):
        R3 = reps_3[g]
        R5 = reps_5[g]
        R3p = reps_3p[g]
        T_rot = np.einsum('ia,jb,kc,abc->ijk', R3, R5, R3p, T_avg)
        err = np.max(np.abs(T_rot - T_avg))
        max_err = max(max_err, err)
    assert max_err < 1e-8, f"Yukawa tensor not I-invariant: err = {max_err}"

    return T_avg


def verify_uniqueness(reps_3: list[Array],
                       reps_5: list[Array],
                       reps_3p: list[Array],
                       n_seeds: int = 5) -> bool:
    """Verify dim Hom_I(1, 3⊗5⊗3') = 1 by projecting multiple random seeds.

    All seeds must produce the same invariant (up to sign/normalization).
    """
    tensors = []
    for seed in range(n_seeds):
        rng = np.random.RandomState(100 + seed)
        T0 = rng.randn(3, 5, 3)

        T_avg = np.zeros_like(T0)
        for g in range(len(reps_3)):
            T_rot = np.einsum('ia,jb,kc,abc->ijk', reps_3[g], reps_5[g], reps_3p[g], T0)
            T_avg += T_rot
        T_avg /= len(reps_3)
        norm = np.sqrt(np.sum(T_avg**2))
        if norm < 1e-12:
            continue  # degenerate seed
        T_avg /= norm
        tensors.append(T_avg)

    # Check all are proportional (up to sign)
    if len(tensors) < 2:
        return False
    for i in range(1, len(tensors)):
        overlap = np.sum(tensors[0] * tensors[i])
        if abs(abs(overlap) - 1.0) > 1e-6:
            return False
    return True


# =====================================================================
# Chirality index
# =====================================================================

def hodge_chirality_indices() -> dict[str, int]:
    """Return the Hodge chirality index Δ for each irrep [ZS-M9 §3.2].

    Δ = +1: chiral (fermion-like)
    Δ =  0: vector-like (gauge)
    Δ = −1: anti-chiral (Higgs)
    """
    return {"1": +1, "3": +1, "3'": +1, "4": 0, "5": -1}


# =====================================================================
# Top-level convenience
# =====================================================================

@dataclass
class IcosahedralGroup:
    """Complete representation data for I ≅ A₅."""
    rotations: list[Array]
    classes: list[ConjugacyClass]
    rep3: list[Array]
    rep5: list[Array]
    rep3p: list[Array]
    rep4: list[Array]
    yukawa_tensor: Array
    yukawa_unique: bool

    @property
    def order(self) -> int:
        return len(self.rotations)


def rep_4_from_tensor_product(rep3: list[Array], rep3p: list[Array]) -> list[Array]:
    """Construct the 4-dim irrep from 3⊗3' = 4 ⊕ 5.

    Uses the character projector P₄ = (4/60) Σ_g χ₄(g) (ρ₃(g)⊗ρ₃'(g))
    where χ₄ = {4, 0, 1, -1, -1} for {e, C₂, C₃, C₅, C₅²}.

    [STATUS: PROVEN — character projection from known irreps]
    """
    phi = (1.0 + np.sqrt(5.0)) / 2.0
    n = len(rep3)
    rep9 = [np.kron(g3, g3p) for g3, g3p in zip(rep3, rep3p)]

    P = np.zeros((9, 9))
    for i, R3 in enumerate(rep3):
        tr3 = np.trace(R3)
        if abs(tr3 - 3.0) < 0.01:     chi4 = 4    # e
        elif abs(tr3 + 1.0) < 0.01:    chi4 = 0    # C₂
        elif abs(tr3) < 0.1:            chi4 = 1    # C₃
        elif abs(tr3 - phi) < 0.01:     chi4 = -1   # C₅
        elif abs(tr3 - (1-phi)) < 0.01: chi4 = -1   # C₅²
        else:                           chi4 = 0
        P += chi4 * rep9[i]
    P *= 4.0 / 60.0

    ev, V = np.linalg.eigh(P)
    basis = V[:, ev > 0.5]
    assert basis.shape[1] == 4, f"rep4 projection gave dim={basis.shape[1]}, expected 4"

    return [basis.T @ M9 @ basis for M9 in rep9]


def build_icosahedral_group() -> IcosahedralGroup:
    """Construct the full icosahedral group with all representations.

    This is the main entry point for Phase 3.
    """
    print("  Building icosahedral group I ≅ A₅ ...")
    rotations = generate_icosahedral_rotations()
    print(f"    |I| = {len(rotations)} ✓")

    classes = classify_conjugacy(rotations)
    print(f"    Conjugacy classes: {[f'{c.name}({c.size})' for c in classes]}")

    print("    Constructing 3-dim natural representation ...")
    r3 = rep_3(rotations)

    print("    Constructing 5-dim Sym²(ℝ³) representation ...")
    r5 = rep_5_from_sym2(rotations)

    print("    Constructing 3'-dim vertex permutation representation ...")
    r3p = rep_3prime_from_vertices(rotations)

    print("    Computing unique Yukawa invariant tensor T ∈ 3⊗5⊗3' ...")
    T = compute_yukawa_invariant(r3, r5, r3p)

    print("    Constructing 4-dim irrep from 3⊗3' = 4 ⊕ 5 ...")
    r4 = rep_4_from_tensor_product(r3, r3p)
    print(f"    rep4 dim = {r4[0].shape[0]}, χ₄(e) = {np.trace(r4[0]):.0f} ✓")

    print("    Verifying uniqueness (dim Hom = 1) ...")
    unique = verify_uniqueness(r3, r5, r3p)
    print(f"    dim Hom_I(1, 3⊗5⊗3') = 1: {'PASS ✓' if unique else 'FAIL ✗'}")

    return IcosahedralGroup(
        rotations=rotations,
        classes=classes,
        rep3=r3,
        rep5=r5,
        rep3p=r3p,
        rep4=r4,
        yukawa_tensor=T,
        yukawa_unique=unique,
    )


# =====================================================================
# §9.5 — Lepton Channel: Singlet Yukawa Vanishing, Character Lift,
#        and Golden Ratio Spectral Quantization
# [ZS-M11 v1.0 §9.5.1–9.5.6, April 2026 first + second batch updates]
# =====================================================================

# A₅ character table — class structure: e(1), 2-fold(15), 3-fold(20),
# 5-fold(12), 5'-fold(12). |A₅| = 60.
_A5_CLASS_SIZES: Final[list[int]] = [1, 15, 20, 12, 12]
_PHI: Final[float] = (1.0 + math.sqrt(5.0)) / 2.0  # golden ratio

_A5_CHARACTERS: Final[dict[str, list[float]]] = {
    "1":  [1,  1,  1,  1,            1            ],
    "3":  [3, -1,  0,  _PHI,         1.0 - _PHI   ],
    "3'": [3, -1,  0,  1.0 - _PHI,   _PHI         ],
    "4":  [4,  0,  1, -1,           -1            ],
    "5":  [5,  1, -1,  0,            0            ],
}


def singlet_yukawa_vanishing() -> dict[str, object]:
    """Verify dim Hom_I(1, 3⊗5⊗X) = (0, 1, 1, 1, 1) for X ∈ {1, 3, 3', 4, 5}.

    [ZS-M11 v1.0 §9.5.4 Theorem 9.5.1, PROVEN]

    The trivial irrep '1' is uniquely the irrep that forbids the Yukawa
    coupling 3⊗5⊗X by character orthogonality. This is the structural
    origin of the singlet ν_R Yukawa vanishing m_{D,1} = 0 (ZS-M11 §9.5.3),
    realizing the minimal seesaw structure of Frampton–Glashow–Yanagida
    (2002) directly from icosahedral group theory.

    Returns
    -------
    dict with keys:
      multiplicities : tuple[int, ...]  — (m_1, m_3, m_3', m_4, m_5)
      expected       : tuple[int, ...]  — (0, 1, 1, 1, 1)
      pass           : bool             — True iff multiplicities == expected
      method         : str              — "character orthogonality on A₅"
    """
    chi3 = _A5_CHARACTERS["3"]
    chi5 = _A5_CHARACTERS["5"]
    mults = []
    for X in ("1", "3", "3'", "4", "5"):
        chiX = _A5_CHARACTERS[X]
        s = sum(_A5_CLASS_SIZES[k] * chi3[k] * chi5[k] * chiX[k] for k in range(5))
        mults.append(int(round(s / 60.0)))
    expected = (0, 1, 1, 1, 1)
    return {
        "multiplicities": tuple(mults),
        "expected": expected,
        "pass": tuple(mults) == expected,
        "method": "character orthogonality on A₅ (60-element class sum)",
    }


def lepton_character_lift() -> dict[str, object]:
    """Verify the Lepton-Channel Character Lift on V = 3 ⊗ 5 ⊗ 3'.

    [ZS-M11 v1.0 §9.5.5 Theorem 9.5.5, PROVEN by direct integer enumeration]

    For any 2-fold element σ ∈ I (15-element conjugacy class), decompose
    V into σ-eigenspaces V = V₊ ⊕ V₋. The result is dim V₊ = 23, dim V₋ = 22.
    The lepton channel L: ρ₂ ⊗ ρ₁ ⊗ ρ₂ under D₅ ⊂ I (norm² = 1/5,
    ZS-M10 §3.1 Table 2) has reflection parity (−1)·(+1)·(−1) = +1, hence
    L ⊂ V₊. Consequently any σ-antisymmetric Yukawa-tensor spurion δT ∈ V₋
    satisfies P_L(δT) ≡ 0 by self-adjoint eigenspace orthogonality.

    This closes the direct O(A) Yukawa Z₂-breaking spurion channel and
    forces ε_lepton(LO) = κ² = A/Q (T1-3, F-S2-IO3 closure, see ZS-S2
    v1.0 §8.1 second-batch update).

    Returns
    -------
    dict with keys:
      dim_V_plus   : int   — multiplicity of σ-eigenvalue +1 (= 23)
      dim_V_minus  : int   — multiplicity of σ-eigenvalue −1 (= 22)
      total        : int   — dim V = 45 = 3·5·3
      L_parity     : int   — +1 (so L ⊂ V₊)
      pass         : bool  — True iff structure matches Theorem 9.5.5
    """
    # χ_3(σ) = -1, χ_5(σ) = +1, χ_3'(σ) = -1 for any 2-fold σ ∈ A₅
    # ρ_X(σ) eigenvalues are ±1 with m_+ - m_- = trace, m_+ + m_- = dim
    def _mp_mm(trace: int, dim_rep: int) -> tuple[int, int]:
        m_minus = (dim_rep - trace) // 2
        return dim_rep - m_minus, m_minus

    m3p,  m3m  = _mp_mm(-1, 3)   # ρ_3(σ):  (1, 2)
    m5p,  m5m  = _mp_mm(+1, 5)   # ρ_5(σ):  (3, 2)
    m3pp, m3pm = _mp_mm(-1, 3)   # ρ_3'(σ): (1, 2)

    dim_Vp = 0
    dim_Vm = 0
    for s3 in (+1, -1):
        for s5 in (+1, -1):
            for s3p in (+1, -1):
                mult = ((m3p  if s3  == +1 else m3m ) *
                        (m5p  if s5  == +1 else m5m ) *
                        (m3pp if s3p == +1 else m3pm))
                if s3 * s5 * s3p == +1:
                    dim_Vp += mult
                else:
                    dim_Vm += mult

    L_parity = (-1) * (+1) * (-1)  # ρ_2 ⊗ ρ_1 ⊗ ρ_2 reflection char
    return {
        "dim_V_plus":  dim_Vp,
        "dim_V_minus": dim_Vm,
        "total":       dim_Vp + dim_Vm,
        "L_parity":    L_parity,
        "pass": (dim_Vp == 23 and dim_Vm == 22
                 and dim_Vp + dim_Vm == 45
                 and L_parity == +1),
    }


def truncated_icosahedron_vertices() -> Array:
    """Return the 60 vertex coordinates of the truncated icosahedron (TI).

    [ZS-M8 v1.0 §4.1, ZS-M11 v1.0 §9.5.6]

    Standard golden-ratio coordinates with edge length 2.
    Three types: even cyclic permutations of (0, ±1, ±3φ),
    (±1, ±(2+φ), ±2φ), and (±2, ±(1+2φ), ±φ).
    Yields 12 + 24 + 24 = 60 vertices.
    """
    coords = []
    # Type A: cyclic perms of (0, ±1, ±3φ) — 12 vertices
    for perm in [(0, 1, 2), (1, 2, 0), (2, 0, 1)]:
        for s1 in (+1, -1):
            for s2 in (+1, -1):
                v = [0.0, 0.0, 0.0]
                v[perm[1]] = s1 * 1.0
                v[perm[2]] = s2 * 3.0 * _PHI
                coords.append(v)
    # Type B: cyclic perms of (±1, ±(2+φ), ±2φ) — 24 vertices
    for perm in [(0, 1, 2), (1, 2, 0), (2, 0, 1)]:
        for s1 in (+1, -1):
            for s2 in (+1, -1):
                for s3 in (+1, -1):
                    v = [0.0, 0.0, 0.0]
                    v[perm[0]] = s1 * 1.0
                    v[perm[1]] = s2 * (2.0 + _PHI)
                    v[perm[2]] = s3 * 2.0 * _PHI
                    coords.append(v)
    # Type C: cyclic perms of (±2, ±(1+2φ), ±φ) — 24 vertices
    for perm in [(0, 1, 2), (1, 2, 0), (2, 0, 1)]:
        for s1 in (+1, -1):
            for s2 in (+1, -1):
                for s3 in (+1, -1):
                    v = [0.0, 0.0, 0.0]
                    v[perm[0]] = s1 * 2.0
                    v[perm[1]] = s2 * (1.0 + 2.0 * _PHI)
                    v[perm[2]] = s3 * _PHI
                    coords.append(v)
    return np.array(coords)


def truncated_icosahedron_laplacian() -> tuple[Array, Array]:
    """Build the graph adjacency and Laplacian L_Y = D - A on the TI.

    Edge length = 2 in standard coordinates → |edge|² = 4.
    Returns (A, L) where A is 60×60 adjacency, L is 60×60 Laplacian.
    The graph is 3-regular with 90 edges.
    """
    coords = truncated_icosahedron_vertices()
    n = len(coords)
    A_mat = np.zeros((n, n))
    for i in range(n):
        for j in range(i + 1, n):
            d2 = float(np.sum((coords[i] - coords[j]) ** 2))
            if abs(d2 - 4.0) < 1e-6:
                A_mat[i, j] = 1.0
                A_mat[j, i] = 1.0
    deg = A_mat.sum(axis=1)
    L_mat = np.diag(deg) - A_mat
    return A_mat, L_mat


def tilattice_rho2_spectrum() -> dict[str, object]:
    """Verify the ρ₂-sector golden-ratio spectral quantization on TI.

    [ZS-M11 v1.0 §9.5.6 Theorem 9.5.6, COMPUTED on the explicit 60-vertex
     TI lattice]

    Constructs the 60-vertex truncated icosahedron, builds L_Y = D - A,
    and verifies that the four golden-ratio-quantized eigenvalues
    {4 - φ, 5 - φ, 3 + φ, 4 + φ} are present in the spectrum, with
    Fiedler eigenvalue matching ZS-M8 v1.0 §4.2 reference 0.243402.

    The four target eigenvalues are exactly the ρ₂-isotype eigenvalues
    of L_Y under an explicit D₅ ⊂ I_h embedding (proof in ZS-M11 §9.5.6);
    here we verify their presence in the full spectrum as a necessary
    condition.

    Returns
    -------
    dict with keys:
      n_vertices   : int          — 60
      n_edges      : int          — 90
      regular_3    : bool         — True if all degrees == 3
      fiedler      : float        — second-smallest eigenvalue (≈ 0.243402)
      target_evs   : list[tuple]  — [(name, value, found_in_spectrum), ...]
      all_present  : bool         — True if all 4 φ-eigenvalues found
      pass         : bool         — full structural check
    """
    A_mat, L_mat = truncated_icosahedron_laplacian()
    n = L_mat.shape[0]
    n_edges = int(A_mat.sum() / 2)
    deg = A_mat.sum(axis=1)
    eigs = np.sort(np.linalg.eigvalsh(L_mat))
    fiedler = float(eigs[1])

    targets = [
        ("4-φ", 4.0 - _PHI),
        ("5-φ", 5.0 - _PHI),
        ("3+φ", 3.0 + _PHI),
        ("4+φ", 4.0 + _PHI),
    ]
    target_status = []
    all_present = True
    for name, val in targets:
        found = bool(any(abs(float(e) - val) < 1e-8 for e in eigs))
        target_status.append((name, val, found))
        if not found:
            all_present = False

    return {
        "n_vertices":  n,
        "n_edges":     n_edges,
        "regular_3":   bool(int(deg.min()) == 3 and int(deg.max()) == 3),
        "fiedler":     fiedler,
        "target_evs":  target_status,
        "all_present": all_present,
        "pass": (n == 60 and n_edges == 90
                 and int(deg.min()) == 3 and int(deg.max()) == 3
                 and abs(fiedler - 0.243402) < 1e-5
                 and all_present),
    }
