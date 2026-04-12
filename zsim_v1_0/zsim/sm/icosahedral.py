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
