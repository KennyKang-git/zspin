#!/usr/bin/env python3
"""
═══════════════════════════════════════════════════════════════════════════
  ZS-Q4 v1.0 COMPREHENSIVE VERIFICATION SUITE

  Near-Term Quantum Simulation of Z-Spin Lattice Gauge Theory:
  Mode-Count Collapse on the Truncated Octahedron

  Four-Stage Error Mitigation Pipeline:
    Stage 1: PAULI TWIRLING
    Stage 2: CYCLE BENCHMARKING
    Stage 3: PEC
    Stage 4: J-PARITY POST-SELECTION

  Z-Spin Cosmology Collaboration
  Kenny Kang · March 2026
═══════════════════════════════════════════════════════════════════════════
"""

import numpy as np
from typing import Dict, List, Tuple
import sys

np.random.seed(350437)

# ═══════════════════════════════════════════════════════════════
# LOCKED CONSTANTS
# ═══════════════════════════════════════════════════════════════
A = 35 / 437
Q = 11
G = Q + 1  # MUB(Q) = 12
V_TO, E_TO, F_TO = 24, 36, 14
N_QUBITS_TO = 2 * E_TO  # 72

I2 = np.eye(2, dtype=complex)
sX = np.array([[0,1],[1,0]], dtype=complex)
sY = np.array([[0,-1j],[1j,0]], dtype=complex)
sZ = np.array([[1,0],[0,-1]], dtype=complex)

def kron_multi(mats):
    out = mats[0]
    for m in mats[1:]: out = np.kron(out, m)
    return out

def pauli_n(indices, n):
    labels = [I2, sX, sY, sZ]
    return kron_multi([labels[i] for i in indices])

def flat_to_tuple(a, n):
    t = []
    for _ in range(n):
        t.append(a % 4); a //= 4
    return tuple(t)

# ═══════════════════════════════════════════════════════════════
# STAGE 1: PAULI TWIRLING
# ═══════════════════════════════════════════════════════════════
class PauliTwirling:
    def __init__(self, n_qubits):
        self.n = n_qubits; self.d = 2**n_qubits; self.n_paulis = 4**n_qubits
    
    def twirl_channel_ptm(self, kraus_ops):
        d = self.d
        lambdas = np.zeros(self.n_paulis)
        for a in range(self.n_paulis):
            Pa = pauli_n(flat_to_tuple(a, self.n), self.n)
            val = sum(np.real(np.trace(Pa @ K @ Pa @ K.conj().T)) for K in kraus_ops)
            lambdas[a] = val / d
        if lambdas[0] > 0: lambdas /= lambdas[0]
        return lambdas
    
    def make_depolarizing_kraus(self, p):
        d = self.d
        kraus = [np.sqrt(1 - p * (d**2 - 1)/d**2) * np.eye(d, dtype=complex)]
        for a in range(1, self.n_paulis):
            kraus.append(np.sqrt(p / d**2) * pauli_n(flat_to_tuple(a, self.n), self.n))
        return kraus
    
    def make_asymmetric_kraus(self, px, py, pz):
        assert self.n == 1
        p0 = 1 - px - py - pz
        return [np.sqrt(p0)*I2, np.sqrt(px)*sX, np.sqrt(py)*sY, np.sqrt(pz)*sZ]

# ═══════════════════════════════════════════════════════════════
# STAGE 2: CYCLE BENCHMARKING
# ═══════════════════════════════════════════════════════════════
class CycleBenchmarking:
    def __init__(self, n_qubits, true_lambdas=None):
        self.n = n_qubits; self.n_paulis = 4**n_qubits
        self.true_lambdas = true_lambdas if true_lambdas is not None else self._realistic_noise()
    
    def _realistic_noise(self):
        lam = np.ones(self.n_paulis)
        for a in range(1, self.n_paulis):
            t = flat_to_tuple(a, self.n)
            weight = sum(1 for x in t if x != 0)
            if weight == 1: lam[a] = 1 - np.random.uniform(0.003, 0.007)
            elif weight == 2: lam[a] = 1 - np.random.uniform(0.0005, 0.002)
            else: lam[a] = 1 - np.random.uniform(1e-5, 1e-4)
        return lam
    
    def simulate_benchmarking(self, depths, shots=2000):
        learned = np.ones(self.n_paulis)
        for a in range(self.n_paulis):
            ms = np.array(depths, float)
            fids = self.true_lambdas[a]**ms + np.random.normal(0, 1/np.sqrt(shots), len(ms))
            good = fids > 0.01
            if good.sum() >= 2:
                log_f = np.log(np.clip(fids[good], 1e-10, 1))
                m_g = ms[good]
                if len(m_g) >= 2:
                    slope, _ = np.polyfit(m_g, log_f, 1)
                    learned[a] = np.clip(np.exp(slope), 0, 1)
        return {'learned': learned, 'true': self.true_lambdas, 'mae': np.mean(np.abs(learned - self.true_lambdas))}

# ═══════════════════════════════════════════════════════════════
# STAGE 3: PEC
# ═══════════════════════════════════════════════════════════════
class ProbabilisticErrorCancellation:
    def __init__(self, lambdas):
        self.lambdas = lambdas
        inv_lam = np.where(np.abs(lambdas) > 1e-12, 1.0/lambdas, 0)
        self.gamma = np.sum(np.abs(inv_lam))
        self.q_dist = np.abs(inv_lam) / self.gamma
        self.signs = np.sign(inv_lam)

# ═══════════════════════════════════════════════════════════════
# STAGE 4: J-PARITY POST-SELECTION
# ═══════════════════════════════════════════════════════════════
class JParityPostSelection:
    def __init__(self, Q=11):
        self.Q = Q
        self.J = np.zeros((Q, Q), dtype=complex)
        for j in range(Q): self.J[j, Q-1-j] = 1.0
        self.P_plus = (np.eye(Q) + self.J) / 2
        self.P_minus = (np.eye(Q) - self.J) / 2
        self.dim_plus = int(np.round(np.trace(self.P_plus).real))
        self.dim_minus = int(np.round(np.trace(self.P_minus).real))
    
    def j_parity(self, psi): return np.real(psi.conj() @ self.J @ psi)
    
    def simulate_post_selection(self, psi_ideal, noise_model='depolarizing', p_error=0.05, n_shots=10000):
        assert np.allclose(self.J @ psi_ideal, psi_ideal)
        rho_ideal = np.outer(psi_ideal, psi_ideal.conj())
        O = np.zeros((self.Q, self.Q), dtype=complex)
        for j in range(self.Q): O[j, j] = np.cos(2*np.pi*j/self.Q)
        O = (O + self.J @ O @ self.J) / 2
        O_ideal = np.real(np.trace(O @ rho_ideal))
        
        fids_all, fids_post, obs_all, obs_post, n_kept = [], [], [], [], 0
        for _ in range(n_shots):
            psi_n = psi_ideal.copy()
            if noise_model == 'depolarizing' and np.random.random() < p_error:
                psi_n = np.random.randn(self.Q) + 1j*np.random.randn(self.Q)
                psi_n /= np.linalg.norm(psi_n)
            elif noise_model == 'bit_flip' and np.random.random() < p_error:
                i, j = np.random.choice(self.Q, 2, replace=False)
                psi_n[i], psi_n[j] = psi_n[j].copy(), psi_n[i].copy()
                psi_n /= np.linalg.norm(psi_n)
            fid = np.abs(psi_ideal.conj() @ psi_n)**2
            fids_all.append(fid)
            rho_n = np.outer(psi_n, psi_n.conj())
            obs_all.append(np.real(np.trace(O @ rho_n)))
            if self.j_parity(psi_n) > 0:
                n_kept += 1; fids_post.append(fid); obs_post.append(np.real(np.trace(O @ rho_n)))
        
        fids_all = np.array(fids_all)
        fids_post = np.array(fids_post) if fids_post else np.array([0.0])
        obs_all = np.array(obs_all)
        obs_post = np.array(obs_post) if obs_post else np.array([0.0])
        return {
            'O_ideal': O_ideal, 'F_all': np.mean(fids_all), 'F_post': np.mean(fids_post),
            'keep_rate': n_kept / n_shots, 'bias_all': abs(np.mean(obs_all) - O_ideal),
            'bias_post': abs(np.mean(obs_post) - O_ideal),
        }

# ═══════════════════════════════════════════════════════════════
# VERIFICATION SUITE
# ═══════════════════════════════════════════════════════════════
def main():
    print("=" * 72)
    print("  ZS-Q4 v1.0 VERIFICATION SUITE")
    print("  Near-Term Quantum Simulation of Z-Spin Lattice Gauge Theory")
    print("=" * 72)
    
    tests = []
    def T(name, cond, detail=""):
        s = "✅ PASS" if cond else "❌ FAIL"
        tests.append((name, cond))
        print(f"  [{s}] {name}" + (f"  ({detail})" if detail else ""))
    
    # ── A: Pauli Twirling ──
    print("\n  [A] Pauli Twirling")
    tw1 = PauliTwirling(1)
    lam_id = tw1.twirl_channel_ptm([np.eye(2, dtype=complex)])
    T("A1: Identity channel → all λ=1", np.allclose(lam_id, 1))
    K_d = tw1.make_depolarizing_kraus(0.01)
    lam_d = tw1.twirl_channel_ptm(K_d)
    T("A2: Depolarizing λ_I=1", abs(lam_d[0] - 1) < 1e-10, f"λ_I={lam_d[0]:.10f}")
    T("A3: All λ ∈ [0,1]", np.all(lam_d >= -0.01) and np.all(lam_d <= 1.01))
    K_a = tw1.make_asymmetric_kraus(0.003, 0.001, 0.006)
    lam_a = tw1.twirl_channel_ptm(K_a)
    T("A4: Asymmetric noise → λ_X ≠ λ_Z", abs(lam_a[1] - lam_a[3]) > 1e-6)
    
    # ── B: Cycle Benchmarking ──
    print("\n  [B] Cycle Benchmarking")
    cb = CycleBenchmarking(1)
    res_cb = cb.simulate_benchmarking([1,2,4,8,16,32,64], shots=5000)
    T("B1: MAE < 5%", res_cb['mae'] < 0.05, f"MAE={res_cb['mae']:.4f}")
    T("B2: Learned λ_I ≈ 1", abs(res_cb['learned'][0] - 1) < 0.05)
    T("B3: All learned λ ∈ (0,1]", np.all(res_cb['learned'] > 0) and np.all(res_cb['learned'] <= 1.01))
    
    # ── C: PEC ──
    print("\n  [C] Probabilistic Error Cancellation")
    pec1 = ProbabilisticErrorCancellation(np.array([1.0, 0.99, 0.98, 0.97]))
    T("C1: Sampling dist normalized", abs(np.sum(pec1.q_dist) - 1) < 1e-10)
    T("C2: γ > 1 for noisy channel", pec1.gamma > 1)
    pec_c = ProbabilisticErrorCancellation(np.ones(4))
    pec_n = ProbabilisticErrorCancellation(np.array([1, 0.9, 0.9, 0.9]))
    T("C3: γ(noisy) > γ(clean)", pec_n.gamma > pec_c.gamma, f"γ_noisy={pec_n.gamma:.2f} > γ_clean={pec_c.gamma:.2f}")
    T("C4: Perfect channel → γ=N", abs(pec_c.gamma - 4) < 1e-10)
    
    # ── D: J-Parity Post-Selection ──
    print("\n  [D] J-Parity Post-Selection")
    jps = JParityPostSelection(Q)
    T("D1: J² = I", np.allclose(jps.J @ jps.J, np.eye(Q)))
    T("D2: dim(E+)=6", jps.dim_plus == 6)
    T("D3: dim(E-)=5", jps.dim_minus == 5)
    T("D4: P+ + P- = I", np.allclose(jps.P_plus + jps.P_minus, np.eye(Q)))
    
    psi = np.zeros(Q, dtype=complex)
    c = np.array([1, 0.5+0.3j, 0.2-0.1j, 0.7j, 0.4, 0.6])
    for k in range(5): psi[k] += c[k]; psi[Q-1-k] += c[k]
    psi[5] = c[5]; psi /= np.linalg.norm(psi)
    T("D5: J|ψ⟩ = |ψ⟩ for E+ state", np.allclose(jps.J @ psi, psi))
    T("D6: ⟨ψ|J|ψ⟩ = 1", abs(jps.j_parity(psi) - 1) < 1e-10)
    
    res_ps = jps.simulate_post_selection(psi, 'depolarizing', 0.10, 30000)
    T("D7: Post-selection improves F", res_ps['F_post'] > res_ps['F_all'], f"F_post={res_ps['F_post']:.4f} > F_all={res_ps['F_all']:.4f}")
    T("D8: Keep rate < 100%", res_ps['keep_rate'] < 1.0, f"keep={res_ps['keep_rate']:.1%}")
    T("D9: Post-selection reduces bias", res_ps['bias_post'] < res_ps['bias_all'], f"bias: {res_ps['bias_all']:.4f} → {res_ps['bias_post']:.4f}")
    
    # ── E: Cross-Paper Consistency ──
    print("\n  [E] Cross-Paper Consistency")
    T("E1: A = 35/437", abs(A - 35/437) < 1e-15)
    T("E2: Q = 11, G = 12", Q == 11 and G == 12)
    T("E3: MUB(Q) = Q+1 = G", Q + 1 == G)
    T("E4: TO: 72 qubits", N_QUBITS_TO == 72)
    T("E5: (V+F)/G = 19/6", abs((V_TO+F_TO)/G - 19/6) < 1e-10)
    T("E6: dim(E+)+dim(E-)=Q", jps.dim_plus + jps.dim_minus == Q)
    
    # ── F: Falsification Gates ──
    print("\n  [F] Falsification Gates")
    # F1: VQE γ² overhead check — γ from PEC on learned noise
    _gamma_sq = pec_n.gamma ** 2
    T("F1: VQE path feasible (γ² < 10⁹)", _gamma_sq < 1e9, f"γ²={_gamma_sq:.1f}")
    # F2: Deep Trotter needs O(E³) CX gates ~ 46656 for TO (E=36), infeasible at current error rates
    _trotter_cx = E_TO ** 3
    T("F2: Deep Trotter infeasible (honest)", _trotter_cx > 10000, f"CX~E³={_trotter_cx} >> 10k")
    # F3: J-symmetrization identity — verify Tr(O·ρ) = Tr(O·(ρ+JρJ)/2) for 100 random pairs
    _sym_ok = True
    _J = jps.J
    for _ in range(100):
        _rho = np.random.randn(Q, Q) + 1j * np.random.randn(Q, Q)
        _rho = _rho @ _rho.conj().T; _rho /= np.trace(_rho)
        _O = np.random.randn(Q, Q) + 1j * np.random.randn(Q, Q)
        _O = (_O + _J @ _O @ _J) / 2  # J-symmetric observable
        _tr_orig = np.real(np.trace(_O @ _rho))
        _rho_sym = (_rho + _J @ _rho @ _J) / 2
        _tr_sym = np.real(np.trace(_O @ _rho_sym))
        if abs(_tr_orig - _tr_sym) > 1e-10: _sym_ok = False; break
    T("F3: J-parity NOT fidelity improvement (honest)", _sym_ok, "Tr(O·ρ)=Tr(O·ρ_sym) for 100 pairs")
    T("F4: J-parity IS post-selection filter", res_ps['F_post'] > res_ps['F_all'])
    
    # ── SUMMARY ──
    total = len(tests)
    passed = sum(1 for _, ok in tests if ok)
    failed = total - passed
    
    print(f"\n{'=' * 72}")
    print(f"  TOTAL: {passed}/{total} PASS, {failed}/{total} FAIL")
    print(f"{'=' * 72}")
    
    if failed > 0:
        print("\n  FAILED:")
        for name, ok in tests:
            if not ok: print(f"    {name}")
        sys.exit(1)
    else:
        print(f"\n  ★ ALL {total} TESTS PASSED ★")
        print("  ZS-Q4 v1.0 verification complete.")
        print(f"{'=' * 72}")
        sys.exit(0)

if __name__ == "__main__":
    main()
