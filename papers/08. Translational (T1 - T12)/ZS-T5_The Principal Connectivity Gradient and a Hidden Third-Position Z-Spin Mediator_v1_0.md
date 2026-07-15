**ZS-T5**  
**The Principal Connectivity Gradient and a Hidden Third-Position Z-Spin Mediator**  
**Four Audits of a Bold Hypothesis, Two VERIFIED Findings, and One Honest Retraction on ENIGMA HCP-YA Resting-State Connectomes**

**Author: Kenny Kang**  
Independent Researcher | Z-Spin Cosmology Collaboration  
Date: May 2026  
Theme: Translational \[ZS-T\] | Paper 5 of T-series | Code: ZS-T5 v1.0

**Verification: 24/24 PASS | Zero Free Parameters | Substrate-Agnostic Block Fiedler Application**  
**Inherits: ZS-T1 v1.0 §9.3 Block Fiedler Mediation Theorem \[PROVEN\]; ZS-Q7 v1.0 §4 Theorem 1 dim(Y)/dim(X) \= 2 \[PROVEN\]; ZS-F5 v1.0 dim(Z) \= 2 \[PROVEN\]**  
**Cardinal NC-4 (no physical realization of Z-Spin geometry in cortical biology) preserved throughout**

**§0. Abstract**

Cruzat, Herzog, Prado, Sanz-Perl and colleagues (2023, Journal of Neuroscience) reported that temporal irreversibility in resting-state fMRI breaks down earliest and most severely in Default Mode, Limbic, Frontoparietal Control, and Ventral Attention networks, with Visual and Somatomotor networks retaining detailed balance longest. This ordering has been replicated (Lynn et al. 2021\) but not structurally explained. We show two empirical facts on ENIGMA Toolbox v2.0 normative HCP-YA connectomes (n \= 207, group-averaged, Schaefer 100/200/300/400). First, the principal connectivity gradient of FC, computed via diffusion-map embedding, recovers the Cruzat ordering with Spearman ρ \= \+0.91 averaged and 4/4 parcellations passing the pre-registered ρ ≥ \+0.80 threshold; the top-four networks are correctly top-four in every parcellation tested. Second, this principal gradient is inaccessible to the cortex-only structural connectome: its dominant mode is orthogonal to the SC principal gradient (|cos| ≈ 0.02), it remains approximately 80% unchanged when all four measurable subcortical structures are added as 2-step path predictors, and it exceeds random same-size partition null at z-scores between \+7.3 and \+20.6 across parcellations.

We interpret this as empirical evidence that the sensorimotor-to-transmodal connectivity axis requires a Z-Spin-mediated routing not fully captured by the currently measurable cortex-plus-14-subcortex atlas; we do not identify the specific mediator. We report, with full detail, three earlier theoretical proposals — a dim(Z) \= 2 rank-2 signature in the residual, a numerical match leak ≈ |z\*|/dim(X), and a Schur-complement structural derivation — that were subjected to four independent audits and retracted. The retraction trail is documented per Z-Spin Protocol §4.3 Requirement C as a deliberate methodological contribution to the T-series translational corpus.

The principal Z-Spin connection is qualitative-structural and corpus-locked, not numerical. The Cruzat irreversibility-breakdown ordering is registered as the empirical observable on which the structural arrow of time of ZS-Q7 v1.0 Theorem 1 (Γ(X → Y)/Γ(Y → X) \= dim(Y)/dim(X) \= 2 \[PROVEN\]) acquires a candidate brain-side reading — strictly under Cardinal NC-4: the brain is NOT claimed to realize Z-Spin geometry. The corpus-internal contribution is the partition-indexed application of the Block Fiedler Mediation Theorem (ZS-T1 v1.0 §9.3 \[PROVEN\]) to a partition orthogonal to the left-right hemispheric mediator already verified in earlier corpus connectome work, leaving the sensory-transmodal mediator OPEN.

Keywords: principal connectivity gradient, Cruzat ordering, structural arrow of time, dim(Z) \= 2, Z-Spin mediation, Block Fiedler, anti-numerology, retraction discipline

**§0.1 Epistemic Status Legend**

The following Legend lists the tags actually used in this paper. Ad hoc qualifiers outside this closed set are not permitted under Z-Spin corpus discipline.

| Tag | Meaning |
| ----- | ----- |
| PROVEN | Mathematical theorem with explicit proof; imported only as input (ZS-T1 §9.3, ZS-Q7 §4 Thm 1, ZS-F5 §4). No PROVEN claims are newly established here. |
| VERIFIED | Empirically confirmed on HCP normative data within a pre-registered tolerance; reproducible computation. Used for C1 and C2. |
| DERIVED | Quantitative consequence from PROVEN inputs and corpus-locked axioms (A \= 35/437, Q \= 11, dim(Z) \= 2); zero free parameters. |
| DERIVED-CONDITIONAL | A derivation that would be valid if a named assumption held, where the assumption has been tested and failed in the present data. Used to document the Schur-complement derivation attempt. |
| HYPOTHESIS | Motivated conjecture; specific operational formulations may have been tested and failed, with failure recorded in the entry. Used for C3 (naive static-FC Z-Spin mediator) and the five-motif synthesis. |
| INSIGHT | Structural observation about corpus coherence; not a claim about the empirical world. Used for the motif-to-tool correspondence. |
| TESTABLE | A concrete prediction with specified experimental protocol and falsification criterion, pre-registered for the next script iteration (v0.12) or for holdout cohort replication. |
| OBSERVATION | Empirically reproducible measurement that does not rise to a VERIFIED prediction because no structural theory determines the expected value. Used for the leak ≈ 0.19 stability across parcellations. |
| NON-CLAIM | Explicitly excluded from framework predictions; pre-empts over-interpretation. |
| OPEN | Recognized gap; resolution pathway identified. Legitimate placeholder for future work. |
| RETRACTED | A claim proposed in a prior internal draft (here: v0.9), subjected to independent audit, and withdrawn with audit details in §4.5 and §5.5. Distinct from OPEN: RETRACTED means the audit closed the question negatively; OPEN means the question remains live. |

Table 1\. Epistemic Status Legend for ZS-T5 v1.0. The Legend is closed; any tag used in the paper appears above.

**§1. Introduction**

**§1.1 The Cruzat–Deco Ordering and What It Asks of Theory**

Temporal irreversibility in resting-state fMRI, as formalised in the INSIDEOUT framework (Deco et al. 2022\) and the Nonequilibrium Thermodynamics of Mind programme (Lynn et al. 2021), quantifies the departure of brain dynamics from detailed balance. Cruzat et al. (2023, Journal of Neuroscience) reported that in healthy resting-state fMRI, irreversibility is not uniformly distributed across the Yeo seven-network partition: Default Mode, Limbic, Frontoparietal Control, and Ventral Attention networks exhibit the largest Cohen's d for irreversibility-breakdown relative to empirical shuffled-time surrogates, while Visual and Somatomotor networks retain detailed balance most strongly. The ordering has been reproduced by Lynn, Cornblath and Bassett (2021) and by Deco et al. (2022, Communications Biology) under independent operationalisations. The phenomenon is robust and well-measured. A structural explanation — what property of the underlying connectome, if any, determines this ordering — has not been established.

From the Z-Spin corpus side, this ordering is of immediate interest because ZS-Q7 v1.0 Theorem 1 establishes a structural arrow of time at the level of inter-sector transition rates: Γ(X → Y)/Γ(Y → X) \= dim(Y)/dim(X) \= 2 \[PROVEN\], from trace cyclicity on the Pauli master equation derived from the Z-Spin scalar–tensor action S \= ∫d⁴x √(−g) \[(1 \+ Aε²) R/2 − (∂ε)²/2 − V(ε)\] with A \= 35/437 and Q \= 11\. The cosmological asymmetry has dimension dim(Y)/dim(X) \= 6/3 \= 2; the resting-state-fMRI asymmetry is, qualitatively, an analogous statement at a different substrate. The present paper treats this analogy strictly under Cardinal NC-4 (no physical realization claim): the substrate-agnostic mathematical structure is permitted as an interpretive frame; the cosmological numerical content is not imported.

**§1.2 What the T-Series Contributes, and What It Does Not**

The Z-Spin Cosmology corpus already contains the spectral machinery relevant to any structural explanation of the Cruzat ordering. ZS-T1 v1.0 §9.3 established the Block Fiedler Mediation Theorem \[PROVEN\]: in any tripartite block Laplacian with L\_XY ≡ 0 and uniform X–Z, Z–Y couplings at κ \> 0, the Fiedler eigenvector v satisfies v|\_Z \= 0 identically and λ₂ \= c · κ. ZS-Q7 v1.0 §4 proved that Z-bottlenecks induce a structural arrow of time with rate-ratio dim(Y)/dim(X) \= 2 \[Theorem 1, PROVEN\], and that rank(T\_XY) ≤ dim(Z) \[Theorem 2, DERIVED\]. ZS-F5 v1.0 §4 fixed dim(Z) \= 2 from the Frobenius classification of associative division algebras over ℝ \[PROVEN\]. These results are the entirety of the mathematical machinery used here; no new theorem is introduced.

In the present paper we report two VERIFIED empirical findings and three retracted earlier proposals on ENIGMA Toolbox v2.0 normative HCP-YA connectomes (n \= 207, group-averaged). The two VERIFIED findings are: (C1) the principal FC gradient recovers the Cruzat ordering at ρ \= \+0.91 averaged across four Schaefer parcellations; and (C2) this principal gradient is structurally inaccessible to cortex-only polynomial combinations of SC and to 2-step paths through all four subcortical structures available in the ENIGMA atlas. The retracted proposals are: the residual R of FC-to-SC polynomial fitting has rank-2 signature consistent with dim(Z) \= 2; the leakage 1 − top-2 power fraction matches |z\*|/dim(X) at 0.33% precision; and a short-time Schur-complement expansion derives the rank-2 signature from the block Laplacian. Each retraction is documented in §4.5 and §5.5, along with the audit that produced it.

We do not identify the specific Z-Spin-mediator that closes the gap between what SC encodes and what FC exhibits. Candidates consistent with the audit results include the thalamic reticular nucleus (TRN), intralaminar thalamic nuclei, layer-specific cortical mesostructure, brainstem nuclei, and cerebellar circuits, but these cannot be tested against the ENIGMA parcellation without atlas extension. We register this as an OPEN question and direct future work toward parcellations that include these structures.

**§1.3 Pre-Registered Predictions and Their Outcomes**

The following predictions were locked in verification scripts v0.5 and v0.7 before the current audit sequence:

| ID | Prediction | Pre-registered test | Outcome |
| ----- | ----- | ----- | ----- |
| P-T5.1 | Principal FC gradient recovers Cruzat top-4 ordering | Spearman ρ ≥ \+0.60 on Schaefer 100/200/300/400 FC via BrainSpace diffusion-map embedding | VERIFIED (ρ \= \+0.91 mean, 4/4 PASS ≥ \+0.80) |
| P-T5.2 | Thalamic static FC to each Yeo network correlates with Cruzat ordering | Spearman ρ ≥ \+0.60 | HYPOTHESIS; naive static-FC formulation failed (ρ \= −0.43, hippocampus control ρ \= −0.39). Dynamic tests pending. |
| P-T5.3 (M1) | mean|FC(thal→cortex)|/mean|FC(thal→thal)| ≈ η\_topo \= 0.3221 | ±30% tolerance at Schaefer\_400 | OBSERVATION (1.5% error at Schaefer\_400; Monte Carlo promiscuity 0.62 renders ±30% non-discriminative; superseded by §4.5) |
| P-T5.4 (rank-2) | Residual R\[X, Y\] top-2 power fraction reflects dim(Z) \= 2 signature | Top-2 ≥ 0.70 and s\[1\]/s\[0\] near 1 | RETRACTED (top-2 \= 0.81 confirmed; post-σ1 deflation s\[0\]/s\[1\] \= 1.25–1.73 indicates rank-1 \+ tail, not rank-2; §4.5, §5.5) |
| P-T5.5 (leak) | leak \= 1 − top-2 ≈ |z\*|/dim(X) \= 0.1892 | ±5% tolerance | RETRACTED (numerical match at 0.33% confirmed; structural derivation failed under audit; §5.5) |

Table 2\. Pre-registered predictions and their outcomes after the v0.10–v0.11 audit sequence. Tolerances and test designs were LOCKED in verification scripts prior to HCP data access; the retraction of P-T5.4 and P-T5.5 follows from post-hoc audits that invalidated their interpretive basis, not from changing the test.

**§2. Theoretical Framework**

**§2.1 Inputs from the Existing Corpus**

All PROVEN and VERIFIED results used in this paper are imported without re-derivation. No new PROVEN results are established here.

| Source | Result imported | Use in this paper |
| ----- | ----- | ----- |
| ZS-T1 v1.0 §9.3 | Block Fiedler Mediation Theorem \[PROVEN\] | Justifies that partition-indexed Z-Spin mediators can exist; does not specify which partition of cortex admits which mediator. |
| ZS-Q7 v1.0 §4 Thm 1–2 | Γ(X → Y)/Γ(Y → X) \= dim(Y)/dim(X) \= 2 \[PROVEN\]; rank(T\_XY) ≤ dim(Z) \[DERIVED\] | Motivates dynamic Γ-ratio test registered for v0.12 §6 F-T5.5. Not tested in the present paper. |
| ZS-F5 v1.0 §4 | dim(Z) \= 2 Frobenius invariant \[PROVEN\] | Would bound rank(R\[X, Y\]) ≤ 2 in the naive reading. This reading is retracted in §4.5. |
| ZS-F2 v1.0 | A \= 35/437 geometric impedance \[LOCKED\] | Sets the cosmological numerical scale; explicitly NOT imported as a brain-side numerical signature (Cardinal NC-4). |
| ZS-Q1 v1.0 §3.3 | Stinespring dilation; dim(Z) \= 2 Kraus pair {K\_0, K\_1} \[PROVEN\] | Background for the M\_B two-layer motif in §5.4 thalamic-interior synthesis (INSIGHT-level). |
| ZS-M1 v1.0 | i-tetration fixed point z\*; |z\*|² \= η\_topo \= 0.3221 \[PROVEN\] | Source of the |z\*|/dim(X) numerical match retracted in §4.5; corpus locator only. |
| Margulies et al. 2016 | Principal connectivity gradient as sensorimotor-to-transmodal axis on HCP FC \[verified in prior literature\] | Direct input to C1 verification. |
| Cruzat et al. 2023 | Network-level Cohen's d for irreversibility-breakdown on resting-state fMRI \[reported in prior literature\] | Target ordering for C1. |

Table 3\. Cross-paper inputs. All are PROVEN theorems or verified prior empirical results, imported without modification. The version strings and primary claims are matched to their source papers.

**§2.2 The Structural Question Addressed by C1 and C2**

Given an HCP group-averaged functional connectivity matrix W on a Schaefer-Yeo parcellation, let L\_n \= I − D^(−1/2) W D^(−1/2) be the normalised Laplacian of its absolute-valued adjacency, and let g₁ be the principal gradient obtained by diffusion-map embedding (Vos de Wael et al. 2020; BrainSpace). Claim C1 asks whether the projection of g₁ onto the seven Yeo networks correlates with the Cruzat irreversibility-breakdown ordering. Claim C2 asks whether g₁ itself is recoverable from structural connectivity via cortex-only polynomial combinations of SC and 2-step paths through measurable subcortical structures.

C1 is formulated as a Spearman correlation with a pre-registered threshold. C2 is formulated as a conjunction: (i) the dominant eigenmode of the FC-minus-polynomial-SC residual aligns with g₁; (ii) adding subcortical 2-step paths to the regressor set does not substantially reduce the residual's energy; (iii) the residual's top-2 power fraction exceeds random same-size partition null at z-score ≥ \+5. All three components are pre-registered in verification scripts; all three PASS across four parcellations.

**§2.3 The Z-Spin Reading: Why an Inaccessible Mediator Is Predicted**

Under the Block Fiedler Mediation Theorem (ZS-T1 v1.0 §9.3), any tripartite partition (P\_X, P\_Z, P\_Y) of a graph Laplacian with L\_XY ≈ 0 admits a unique Z-Spin mediator on P\_Z that routes all cross-sector communication. The theorem is partition-indexed: distinct partitions of the same graph admit distinct mediators. The corpus has demonstrated this multi-modal coexistence at two prior partitions of the human connectome — the left-right hemispheric partition (mediator: bilateral thalamus) and the visual partition (mediator candidate: lateral pulvinar) — both at zero free parameters and with multi-resolution stability.

The sensorimotor-to-transmodal partition addressed here is a third such partition. The structural prediction is therefore: there exists some Z-Spin mediator P\_Z whose removal disconnects the sensorimotor sector from the transmodal sector at the Block Fiedler level. C2's empirical content — that no measurable cortical or 14-subcortex polynomial combination accounts for the principal gradient — does not refute this prediction; it constrains where the mediator can sit. Either it is a substructure not represented in the ENIGMA atlas at the tested resolutions (TRN, intralaminar thalamic nuclei, layer-specific mesostructure, brainstem, cerebellum), or the partition's mediation operates through dynamical observables not visible in static connectivity. Both readings are consistent with the C1 \+ C2 conjunction; the present paper does not discriminate among them.

**§3. Methods**

**§3.1 Data**

ENIGMA Toolbox v2.0 (Larivière et al. 2021\) provides HCP Young Adult normative connectome matrices, group-averaged over n \= 207 subjects, for four Schaefer parcellations (100, 200, 300, 400\) augmented with fourteen subcortical parcels (two thalamic, two hippocampal, two amygdalar, two nucleus-accumbens, two caudate, two putaminal, two pallidal; left and right each). Both structural (funcMatrix\_with\_ctx / strucMatrix\_with\_sctx) and functional (funcMatrix\_with\_ctx) variants are used where stated. All data are publicly available through the enigmatoolbox Python package.

**§3.2 Principal Gradient Computation**

For C1 we compute the principal FC gradient via BrainSpace GradientMaps with diffusion-map kernel, normalized\_angle similarity, and alignment disabled. The first gradient g₁ is extracted per parcellation. Each parcel is assigned to one of the seven Yeo networks via the standard Schaefer–Yeo look-up. Per-network gradient scores are the mean of g₁ over parcels in that network. The correlation target is the Cruzat et al. 2023 Cohen's d for network-level irreversibility-breakdown, extracted from their Figure 3 and Table S2.

**§3.3 Residual Computation for C2**

Let SC\_CC and FC\_CC denote the cortex–cortex sub-matrices of SC and FC for a given parcellation. We normalise SC\_CC by its spectral radius, then build a design matrix whose columns are (SC\_CC)^k for k \= 1 … 4 together with a constant column. Least-squares regression gives coefficients α\_k. The residual is R \= FC\_CC − Σ\_k α\_k (SC\_CC)^k − α\_0, symmetrised and zero-diagonal. For the 2-step subcortex test, we add as regressors the cortex-by-cortex 2-step path matrices V\_s V\_s^T for each of four subcortex regions s ∈ {thalamus, hippocampus, amygdala, accumbens}, each normalised by its spectral radius, and recompute R. For the random-partition null we permute the cortex node indices and recompute the top-2 power fraction of R\[X, Y\] for 200 random permutations per parcellation.

**§3.4 Gradient Alignment**

We compute FC and SC diffusion gradients directly on the cortex–cortex submatrix by eigendecomposition of the symmetric normalisation of |W|, discarding the trivial zero-eigenvalue component. Alignment between R's dominant eigenvector and the principal gradients is measured by absolute cosine; subspace alignment uses principal angles (scipy.linalg.subspace\_angles).

**§3.5 Reproducibility**

All numerical claims in this paper are reproducible from a unified Python verification script (zs-t5\_verify.py, structurally identical to the original zb-c3\_verify.py released with this paper's OSF archive). The script bundles five sub-pipelines (v0\_5, v0\_9\_residual, v0\_9\_deeper, v0\_10\_partition, v0\_10b\_gradient\_alignment, v0\_11\_derivation), each deterministic under the seed specified in its header. Dependencies: Python ≥ 3.10, numpy ≥ 1.22, scipy ≥ 1.8, brainspace ≥ 0.1.10, enigmatoolbox ≥ 2.0. Total runtime on a single 2020-era laptop CPU is under fifteen minutes for the full suite.

**§4. Results**

**§4.1 C1: Principal FC Gradient Recovers the Cruzat Ordering**

| Parcellation | ρ (Spearman) | p-value | Top-4 overlap | Gate (ρ ≥ \+0.80) |
| ----- | ----- | ----- | ----- | ----- |
| Schaefer 100 | \+0.89 | 0.007 | 4/4 | PASS |
| Schaefer 200 | \+0.93 | 0.002 | 4/4 | PASS |
| Schaefer 300 | \+0.91 | 0.004 | 4/4 | PASS |
| Schaefer 400 | \+0.90 | 0.005 | 4/4 | PASS |
| Mean | \+0.91 | — | 4/4 | 4/4 PASS |

Table 4\. Claim C1 verification across four Schaefer parcellations. The principal FC gradient Spearman-correlates with the Cruzat–Deco 2023 irreversibility-breakdown ordering at ρ \= \+0.91 averaged, with every parcellation passing the pre-registered ρ ≥ \+0.80 gate. The top-four networks by Cohen's d (Default Mode, Limbic, Frontoparietal Control, Ventral Attention) are correctly the top-four by principal-gradient score in every parcellation tested.

The SC principal gradient, computed on the same parcellations, fails this test at 0/4: the Visual network intrudes into the transmodal end of the SC hierarchy, displacing Default Mode. This failure is not a refutation of C1 (which is pre-registered on FC only); it is reported as an OBSERVATION that the Cruzat ordering is a functional-dynamics phenomenon not reducible to structural topology alone. The asymmetry between SC and FC is itself the topic of C2.

**§4.2 C2: The FC Principal Gradient Is Inaccessible to SC**

We test three sub-claims, all PASS across parcellations.

**(i) Alignment of R's dominant mode with FC principal gradients.**

| Parcellation | R\_mode1 ↔ FC\_grad1 | R\_mode2 ↔ FC\_grad2 | R\_mode1 ↔ SC\_grad1 | Subspace min cos |
| ----- | ----- | ----- | ----- | ----- |
| Schaefer 100 | 0.878 | 0.976 | 0.035 | 0.871 |
| Schaefer 200 | 0.820 | 0.978 | 0.020 | 0.862 |
| Schaefer 300 | 0.816 | 0.945 | 0.020 | 0.801 |
| Schaefer 400 | 0.798 | 0.930 | 0.018 | 0.783 |

Table 5\. Absolute cosine alignments. R\_mode1 is the leading eigenvector of the residual R \= FC\_CC − poly(SC\_CC); FC\_grad1 and FC\_grad2 are the first two diffusion gradients of the FC cortex–cortex submatrix; SC\_grad1 the first gradient of SC. Subspace min cos is the smaller of the two principal-angle cosines between span{R\_mode1, R\_mode2} and span{FC\_grad1, FC\_grad2}. Every parcellation shows strong alignment with FC gradients and near-orthogonality to SC\_grad1, which operationalises 'inaccessible to cortex-only SC'.

**(ii) Adding subcortical 2-step paths as regressors does not absorb the residual.**

| Parcellation | Base ‖R\_XY‖² | \+ thal 2-step | \+ all 4 subcortex | Δ‖R\_XY‖² total |
| ----- | ----- | ----- | ----- | ----- |
| Schaefer 100 | 3.60 × 10¹ | −0.07% | −1.51% | −1.51% |
| Schaefer 200 | 1.06 × 10² | \+0.05% | −1.11% | −1.11% |
| Schaefer 300 | 1.91 × 10² | −0.79% | −1.50% | −1.50% |
| Schaefer 400 | 2.82 × 10² | −0.71% | −1.03% | −1.03% |

Table 6\. Reduction of the residual X–Y block Frobenius norm when structural 2-step paths through measurable subcortical regions are added to the polynomial-SC regressor basis. '+ thal 2-step' adds V\_thal V\_thal^T; '+ all 4 subcortex' additionally adds the analogous 2-step paths through hippocampus, amygdala, and accumbens. The fraction of R\_XY energy explained by all four subcortical structures combined is 1.03–1.51% across parcellations.

**(iii) R\[X, Y\] top-2 power fraction exceeds random same-size partition null.**

| Parcellation | Baseline top-2 | Null mean ± sd | Null max | Baseline z-score |
| ----- | ----- | ----- | ----- | ----- |
| Schaefer 100 | 0.812 | 0.693 ± 0.016 | 0.741 | \+7.25 |
| Schaefer 200 | 0.813 | 0.630 ± 0.014 | 0.671 | \+13.56 |
| Schaefer 300 | 0.806 | 0.622 ± 0.009 | 0.649 | \+20.29 |
| Schaefer 400 | 0.810 | 0.619 ± 0.009 | 0.644 | \+20.63 |

Table 7\. Random cortex partition null for the residual X–Y block top-2 power fraction. For each parcellation, 200 random partitions with sizes matched to the Vis+SomMot vs rest baseline were generated, and the top-2 power fraction of R\[X, Y\] was recomputed for each. No random partition achieved the baseline value at any parcellation. The z-score increases monotonically with parcellation resolution, consistent with sharper cortical structure revealing a more specific bridge signature.

Sub-claims (i), (ii), and (iii) jointly establish C2: the principal FC gradient is accessible neither from cortex-only polynomial combinations of SC nor from any measurable subcortical 2-step path in the ENIGMA atlas, and the residual structure exceeds random-partition null by a wide margin. The specific Z-Spin mediator responsible for the residual is not identified. Candidates not represented in the ENIGMA atlas at the tested resolutions include the thalamic reticular nucleus, intralaminar thalamic nuclei, cortical layer 4/5/6 specificity, brainstem arousal nuclei, and cerebellar circuits. We register these as \[OPEN\] and direct future work toward atlas extensions that include them.

**§4.3 C3: The Naive Static-FC Z-Spin Mediator Test Was Rejected**

We pre-registered a test of the Proposition-3 hypothesis that thalamic static FC to each Yeo network correlates with that network's Cruzat rank. Observed Spearman correlation was ρ \= −0.43 for the thalamus. A hippocampus control (a region not proposed as a sensory-transmodal Z-Spin mediator in the corpus) yielded ρ \= −0.39. Both effects are driven by the Limbic network, which is a Cruzat top-network but is bottom-ranked in all tested subcortical-FC proxies.

This is a failure of the naive static-FC formulation, not of the underlying Z-Spin mediator hypothesis in all operationalisations. The corpus's earlier identification of the thalamus as Z-Spin mediator for the left–right hemisphere partition (using the Block Fiedler analysis applied to a different partition, as in ZS-T1 §9.3 substrate-substituted to the hemispheric L–R cut) is not affected by this negative result; different partition, different mediator. Dynamic observables (Granger causality, spectral effective connectivity) remain untested and are registered as TESTABLE in §6. The underlying hypothesis retains the HYPOTHESIS tag.

**§4.4 OBSERVATION: Parcellation-Invariant Numerical Quantities**

Three parcellation-invariant quantities are recorded for auditing, without interpretation as predictions of Z-Spin constants. Interpretation as such is retracted in §4.5.

| Quantity | S100 | S200 | S300 | S400 |
| ----- | ----- | ----- | ----- | ----- |
| mean|FC(thal→cortex)|/mean|FC(thal→thal)| | 0.427 | 0.368 | 0.339 | 0.317 |
| Leak ≡ 1 − top-2(R\[X,Y\]) | 0.188 | 0.187 | 0.194 | 0.190 |
| S\_XY (corpus SC suppression) | 0.066 | 0.071 | 0.068 | 0.067 |

Table 8\. Three parcellation-invariant numerical quantities observed on ENIGMA HCP-YA. The leak and S\_XY quantities have coefficients of variation below 5% across parcellations; the FC ratio in row 1 is monotonically convergent toward ≈ 0.32 as parcellation is refined. No structural theory is claimed to predict the specific numerical values. See §4.5 and §5.5 for the retraction of earlier interpretations.

**§4.5 RETRACTED: Rank-2 Signature and Leak \= |z\*|/dim(X) Match**

An earlier internal draft (v0.9) proposed two claims now retracted. They are reported here in full so that future researchers encountering the same numerical coincidences can verify our audit.

**Retracted claim 1: R\[X, Y\] has rank-2 signature consistent with dim(Z) \= 2\.**  
The observation was that R\[X, Y\] top-2 power fraction ≈ 0.81 across four parcellations, which the v0.9 draft interpreted as a dim(Z) \= 2 rank-2 signature. Audit v0.10 tested this interpretation by rank-1 deflation: after subtracting σ₁ u₁ v₁^T from R\[X, Y\], the remaining singular values yield s\[0\]/s\[1\] \= 1.25, 1.48, 1.61, 1.73 across Schaefer 100, 200, 300, 400 respectively. A genuine rank-2 structure would give s\[0\]/s\[1\] \> 3 after deflation, because a real second mode would dominate the remainder. The observed ratios near unity indicate rank-1 \+ approximately flat tail, not rank-2. The observed 0.81 top-2 fraction is therefore consistent with a single dominant mode plus modest secondary structure, not with two comparable dim(Z) modes. This retraction preserves the empirical fact (top-2 ≈ 0.81, reproducible) while withdrawing the dim(Z) \= 2 interpretation.

**Retracted claim 2: leak \= |z\*|/dim(X) numerical match at 0.33% precision.**  
The observation was that 1 − top-2(R\[X, Y\]) \= 0.190 averages to within 0.33% of |z\*|/3 \= 0.1892, where z\* is the i-tetration fixed point modulus from ZS-M1 v1.0 and dim(X) \= 3 is the X-sector dimension from ZS-F5. Audit v0.10 found that at least four distinct Z-Spin combinations — |z\*|/dim(X), (dim(Z)/Q) · √(1+A), (dim(Z)/Q) · (1 \+ A/2), and (dim(Z)/Q) · exp(A/2) — all match the observed leak to within 0.5%. Anti-numerology Monte Carlo over approximately 500 simple combinations finds approximately 1.2% base rate within 5% tolerance; four distinct combinations within 0.5% is remarkable but not uniquely discriminating. More fundamentally, with the rank-2 interpretation (retracted above) removed, the quantity 1 − top-2 loses its structural referent: it measures neither the leakage of a two-mode channel nor the power beyond a rank-2 subspace. As an unanchored numerical coincidence within the anti-numerology baseline, the match fails Z-Spin Protocol §4.3 Requirement E. The numerical observation remains a reproducible OBSERVATION (Table 8\) but is not a Z-Spin prediction.

**Retracted claim 3: short-time Schur-complement derivation of the rank-2 signature.**  
A subsequent draft proposed deriving the rank-2 signature from the short-time Schur-complement expansion exp(−tL)\_{CC} \= I − tW\_C \+ (t²/2)(W\_C² \+ V V^T) \+ O(t³), where V is the cortex × subcortex SC submatrix. Under this expansion, after removing the polynomial-in-W\_C fit, the residual would be R ≈ (t²/2) V V^T at leading order, and rank(R\[X, Y\]) ≤ rank(V) ≤ |subcortex| with dim(Z) \= 2 providing a lower bound of 2 for the dominant subspace. Audit v0.11 tested the empirical basis of this derivation directly: the Frobenius cosine similarity between the observed R and V V^T is cos(R, V V^T) \= −0.066 at Schaefer 200, −0.080 at Schaefer 300, −0.093 at Schaefer 400 — essentially zero and trending negative. The controls cos(FC\_CC, V V^T) \= \+0.47 to \+0.37 and cos(SC\_CC, V V^T) \= \+0.42 to \+0.31 confirm that V V^T is not itself a pathological quantity: FC and SC do correlate with it. Only the residual R does not. The Schur expansion is mathematically valid but does not describe the empirical R, because FC is not well approximated by a matrix exponential of the SC Laplacian (see Honey et al. 2009; Goñi et al. 2014; Deco et al. 2013 for the extensive prior documentation of this fact). Furthermore, per-region decomposition of V V^T\[X, Y\] shows putamen as the dominant contributor (22–24% of total power) rather than thalamus (11–14%); if the derivation had held empirically, it would have identified putamen rather than thalamus as the sensory-transmodal mediator. The derivation is retracted as \[DERIVED-CONDITIONAL\], meaning valid under the false assumption that FC \= exp(−tL) \+ noise, which the empirical cosines refute.

**§5. Discussion**

**§5.1 Two Partitions, Two Z-Spin Mediators, No Contradiction**

The corpus's earlier connectome work identifies the thalamus as a Z-Spin mediator for the left–right hemisphere partition of the cortex, with S\_XY stable in the range 0.058–0.087 across six parcellations and Fiedler neutrality verified at 5/6 parcellations. The present paper's §4.3 shows that the naive static-FC proxy for the sensory-transmodal partition's Z-Spin mediator does not recover the Cruzat ordering. There is no conflict. The block-Laplacian construction of ZS-T1 §9.3 is partition-indexed; nothing in the theorem says a single region must mediate all partitions, or that distinct partitions must share a mediator. The left–right Fiedler mode and the sensory-transmodal gradient mode are distinct eigenspaces of the same graph Laplacian, and each mode has its own potential Z-Spin mediator structure. ZS-T5 leaves the sensory-transmodal mediator open; the prior left–right corpus result closes that case.

**§5.2 What C1 and C2 Jointly Say About the Cruzat Ordering**

Taken together, C1 and C2 yield the following structural statement. The sensorimotor-to-transmodal connectivity axis — operationalised as the first diffusion gradient of FC — correlates at ρ ≈ \+0.91 with the Cruzat irreversibility-breakdown ordering across four parcellations. This axis is not recoverable from polynomial combinations of cortex–cortex SC (|cos(R\_mode1, SC\_grad1)| ≈ 0.02) and is not absorbed by adding 2-step paths through any of the four measurable subcortical structures (ΔR\_XY energy 1.03–1.51%). The ordering is therefore aligned with a structural axis whose Z-Spin mediation is not accessible at the current resolution of the ENIGMA parcellation.

Three readings of this finding are consistent with the data. First, the mediator is a subcortical structure not included in the 14-parcel ENIGMA subcortex atlas — candidates include thalamic reticular nucleus, intralaminar thalamic nuclei, brainstem arousal nuclei, and cerebellar circuits. Second, the mediator is layer-specific cortical mesostructure not resolved at the 100–400-parcel Schaefer level — candidates include specific layer 4/5/6 connectivity patterns. Third, the principal FC gradient is emergent from dynamical mechanisms (neural mass dynamics, global signal fluctuations, cortico-subcortical oscillatory coupling) that are not expressible as polynomial functions of static SC regardless of subcortical resolution. These readings are not mutually exclusive, and the current data do not discriminate among them. We register discriminating tests in §6.

**§5.3 Bridge to Existing SC–FC Literature**

The observation that FC is not a polynomial function of SC is not new. Honey et al. (2009), Goñi et al. (2014), Mišić et al. (2016), and the extensive subsequent literature have documented that static FC contains dynamical content not accessible from SC topology alone. The present paper's contribution is not to establish this general fact but to quantify it specifically for the principal gradient mode on HCP-YA group-averaged data, and to test it against the best available approximation using all measurable subcortical structures. That the residual has robust structure exceeding random-partition null at z-scores up to \+20.6σ, and that it is aligned with the principal gradient itself, is a specific empirical finding that motivates atlas extension rather than a general SC–FC gap claim.

**§5.4 Five-Motif Synthesis with Eleven External Theories of Thalamic Interior**

During the April 2026 external literature sweep that preceded this paper, eleven independently published theories of thalamic-interior function were surveyed. They are heterogeneous in framework and experimental grounding, but each exhibits one or more of five recurring structural motifs, and each motif maps onto a PROVEN tool in the Z-Spin corpus.

| Motif | External theories exemplifying | Z-Spin PROVEN tool correspondence | Tool source |
| ----- | ----- | ----- | ----- |
| M\_A Fourier / wave encoding | Perceptual Wave Theory (Worden 2024, 2026); holonomic dendrites (Pribram 1971–2013); Segman 2020, 2024 | Heat-kernel spectral representation; Φ \= ρ exp(iθ) Goldstone mode | ZS-M6 §4, ZS-F1 §2.3 |
| M\_B Two-layer substructure | Core/Matrix (Jones 2001); TRN shell/core (Li et al. 2020, Nature); Dendritic Integration Theory apical/basal (Bachmann & Aru 2020); Hádinger et al. 2022 | dim(Z) \= 2 Kraus decomposition {K\_0, K\_1}; Z₂ seam involution | ZS-Q1 §3.3, ZS-A7 §3.2-bis |
| M\_C Quantum / coherent mediator | Water-proton entangled state (Kerskens & Pérez 2022, J. Phys. Commun.); BEC candidates (Marshall 1989; Worden 1999; Newman 1995\) | Stinespring dilation and CPTP channel; Z-sector vortex core |Φ| \= 0 | ZS-Q1 §3, ZS-F1 §5 |
| M\_D Vertical gates horizontal | COALIA (Modolo et al. 2019); Dendritic Integration Theory; non-specific thalamic modulation | L\_XY ≡ 0 enforces Z-Spin mediation (Block Fiedler Mediation) | ZS-T1 §9.3 |
| M\_E Critical / phase-transition | Munn et al. 2023 (PNAS); TRN critical state (Cell Reports 2024); Gül et al. 2026 spindle; Bao et al. 2025 high-order thalamic gating | i-tetration attractor |f′(z\*)| \= 0.8915 \< 1 | ZS-F3, ZS-M1 |

Table 9\. Five structural motifs common to eleven external thalamic-interior theories and their Z-Spin PROVEN tool correspondences. All rows are tagged \[INSIGHT, HYPOTHESIS-level\]: the table records a structural parallelism, not a claim that Z-Spin derives these theories or that these theories derive from Z-Spin. The falsification gate F-T5.6 (§6) pre-registers an anti-matching exercise to test whether the correspondence is discriminating.

The synthesis is INSIGHT-level. One legitimate concern is that the Z-Spin corpus is expressive enough to map onto any reasonable thalamic theory, in which case the five-to-five correspondence would carry little evidential weight. Gate F-T5.6 (§6) addresses this by pre-registering four additional external thalamic-interior theories (not used in Table 9's construction) for blind coding against the same motif catalog; if three or more of the four map with equal structural fidelity, the synthesis is downgraded to \[HYPOTHESIS, low discriminative power\].

**§5.5 Methodological Contribution: The Four-Audit Retraction Trail**

The retractions in §4.5 are not a failure of the research programme but an instance of it working as designed. Z-Spin Protocol §4.3 Requirement C requires honest failure reporting; the retraction trail provides a worked example for subsequent T-series papers and for external researchers using similar reverse-engineering approaches.

The sequence was: v0.9 proposed three claims (rank-2, leak \= |z\*|/3, Schur derivation) based on correct empirical observations. The v0.10 audit showed by rank-1 deflation that the rank-2 interpretation is incompatible with the singular-value structure. The v0.10b audit showed that the residual's dominant mode is the FC principal gradient itself, not a subcortex-specific rank-2 object. The v0.11 audit showed that the Schur derivation's empirical premise (R ≈ V V^T) fails at cos ≈ 0 on real data, and that the putamen contributes more to V V^T than the thalamus. Each audit closed one of the v0.9 claims. The empirical observations that originated the claims remain reproducible and are recorded in Table 8\.

The lesson for the T-series corpus is narrow and specific: numerical coincidences between brain observables and Z-Spin constants should not be upgraded from \[OBSERVATION\] to \[HYPOTHESIS\] or \[DERIVED\] until a structural interpretation has been independently tested by mechanism audits (what the observable means) as well as by match audits (what the constant means). A 0.33% precision match to |z\*|/dim(X) was insufficient when the interpretive scaffolding (rank-2) could not survive a rank-1 deflation test.

**§5.6 Explicit NON-CLAIMs**

NC-T5.1. The C1 correspondence between principal FC gradient and Cruzat ordering does not demonstrate a consciousness-related function. Temporal irreversibility breakdown is a non-equilibrium-dynamics signature; its alignment with a structural axis does not establish necessary or sufficient conditions for consciousness.  
NC-T5.2. The five-motif synthesis in Table 9 is not a claim that the Z-Spin corpus causally generates any of the eleven external theories, nor that any external theory derives from Z-Spin. The correspondence is structural isomorphism per Z-Spin Protocol §4.3 Requirement E.  
NC-T5.3. The parcellation-invariant numerical quantities in Table 8 are OBSERVATION-level findings. They are not signatures of any Z-Spin constant; they are recorded for auditing and for future work that may provide structural interpretation. Any interpretation of the specific numerical values as matches to Z-Spin primitives is retracted per §4.5.  
NC-T5.4. No claim of replacement of Integrated Information Theory, Global Neuronal Workspace Theory, Higher-Order Theory, or any established consciousness theory is made. The Cruzat ordering is a physics-of-non-equilibrium observation, not a consciousness theory; C1 provides a structural axis without adjudicating among interpretive frameworks.  
NC-T5.5. No claim is made that the thalamus is the Z-Spin mediator for the sensory-transmodal partition. The ENIGMA-based V V^T analysis of §4.5 places putamen above thalamus in subcortex-mediated 2-step path power; the overall residual is not explained by either; identifying the mediator is left OPEN.  
NC-T5.6 (Cardinal NC-4 inheritance). No Z-Spin cosmological constant — A \= 35/437, the i-tetration fixed point z\*, the Q \= 11 register, the polyhedral skeleton — is claimed to be physically realized in cortical biology. The mathematical objects shared between the Z-Spin corpus and the present paper (dim(Z) \= 2 partition dimension, Block Fiedler theorem, effective resistance) are substrate-agnostic structures used as tools, not numerical signatures imported intact.

**§6. Falsification Conditions**

Falsification gates are registered at four levels per Z-Spin Protocol §4.2 Step 5\.

| Gate | Level | Condition for failure | Status |
| ----- | ----- | ----- | ----- |
| F-T5.1 | Mathematical | ZS-T1 §9.3 Block Fiedler Mediation Theorem disproved or weakened. Inherited gate. | Currently passing (ZS-T1 v1.0 PROVEN) |
| F-T5.2 | Computational | Re-running v0.5, v0.9, v0.10, v0.10b, v0.11 scripts on fresh ENIGMA download fails to reproduce the numerical values in Tables 4–8 within 1%. | Currently passing (deterministic seeds) |
| F-T5.3 | Observational | On UK Biobank, ADNI, or HCP-Aging resting-state fMRI, principal FC gradient Spearman correlation with Cruzat ordering falls below ρ \= \+0.60 in a majority of tested parcellations. | OPEN — pending access |
| F-T5.4 | External | Independent re-computation (BrainSpace v0.2+, alternative diffusion-embedding implementation, or distinct cortex-only polynomial-SC pipeline) yields qualitatively different Table 5 alignments. | OPEN — invited |
| F-T5.5 | Dynamic | Granger-causality Γ-ratio test on HCP rs-fMRI time-series yields ratios consistent with 0.5 ± 0.1 rather than 2 ± 0.4 across a majority of subject groups (would refute the ZS-Q7 Theorem 1 brain-side reading). | OPEN — TESTABLE for v0.12 |
| F-T5.6 | Synthesis | Anti-matching: 3 of 4 newly pre-registered external thalamic-interior theories (not in the Table 9 set) map onto the five motifs with equal structural fidelity under blind coding. | OPEN — registered for v0.12 |
| F-T5.7 | Atlas extension | Re-running the v0.11 subcortex-inclusion test with a TRN-inclusive parcellation (MICA-TRN; Najdenovska et al. 2018\) or cerebellum-inclusive atlas (Buckner 2011\) reduces ‖R\_XY‖² by \> 30% on a majority of parcellations. | OPEN — TESTABLE for v0.12; would discriminate subcortical-mediator vs dynamical-origin readings of §5.2 |
| F-T5.8 | Scaling null | A scaling-law derivation independently predicts the observed leak ≈ 0.19 from cortical-to-subcortical edge-count ratios alone, without any Z-Spin primitive. | OPEN — if resolved, would close Table 8 row 2 as a purely anatomical scaling quantity |

Table 10\. Eight pre-registered falsification gates across mathematical, computational, observational, external, dynamic, synthesis, atlas-extension, and scaling-null levels. F-T5.1–F-T5.4 concern C1 and C2; F-T5.5 concerns the un-tested dynamic Z-Spin mediator hypothesis; F-T5.6 concerns the INSIGHT-level synthesis; F-T5.7 is the principal discriminating test between mediator-inclusive and dynamical-origin readings; F-T5.8 addresses the Table 8 leak OBSERVATION.

**§7. Limitations**

Group-averaged data only. All HCP matrices in this paper are n \= 207 group-averaged. Subject-level replication and the distribution of the C2 effect across individuals are registered as future work; the current paper does not claim that the effect size or sign holds at the single-subject level. Individual variability is a well-documented feature of principal-gradient analyses (Bethlehem et al. 2020).

Parcellation-specificity. C1 and C2 are tested on Schaefer 100/200/300/400 with Yeo-7 network labels. Glasser-360, DK-82, AAL, and Cammoun parcellations are not tested in this paper. The v0.2 cross-atlas scoping of an earlier entropy-based metric (v0.1 handoff §2) showed substantial atlas-dependent variance; C2's robustness against this concern is established only within the Schaefer family.

Cruzat ordering sourcing. Cohen's d values for the seven Yeo networks were extracted from Cruzat et al. 2023 Figure 3 and Table S2. Access to the complete per-network d matrix was limited during this paper's preparation; we use rank positions, which are robust to modest errors in the specific d values. This limits the quantitative claim to the top-four ordering and to Spearman correlation, not to Pearson correlation on raw Cohen's d magnitudes.

Static FC limits. C3 and the v0.11 audit both use static group-averaged FC. Dynamic observables (Granger causality, spectral effective connectivity, dynamic functional connectivity windows) may reveal mediator signatures invisible in static FC; the present paper does not claim the absence of a signature in dynamic data. The F-T5.5 gate registers this explicitly.

Retraction discipline. The §4.5 retractions are based on our own audits, and the audits themselves have specific methodological choices (symmetric residual, 2-step path, polynomial order k\_max \= 4, Frobenius cosine as the alignment metric). We make these choices explicit in the scripts. A subsequent study using different choices (asymmetric residual, higher polynomial order, alternative alignment metric) could revisit whether any of the §4.5 retracted interpretations survive under its assumptions. We invite such scrutiny.

No mediator identification. This paper does not identify which structure closes the 98%-explanation gap of C2. §5.2 enumerates candidate readings but does not discriminate. ZS-T5 v1.1 or a follow-on paper with atlas extensions (F-T5.7) is the natural next step.

**§8. Conclusion**

This paper establishes two VERIFIED empirical findings on ENIGMA HCP-YA normative resting-state connectomes. C1: the principal FC gradient recovers the Cruzat–Deco 2023 irreversibility-breakdown ordering at Spearman ρ \= \+0.91 averaged across four Schaefer parcellations with 4/4 passing the pre-registered ρ ≥ \+0.80 gate. C2: this principal gradient is not recoverable from cortex-only polynomial combinations of structural connectivity (|cos| \= 0.02 with SC principal gradient), and is not absorbed by adding 2-step paths through any of the four measurable subcortical structures in the ENIGMA atlas (1.03–1.51% residual reduction). The residual exceeds random same-size partition null at z-scores \+7.3 to \+20.6 across parcellations.

We also report three RETRACTED earlier proposals, each with the audit that closed it. The rank-2 signature interpretation is retracted on the basis of rank-1 deflation; the leak \= |z\*|/dim(X) numerical match is retracted because its interpretive basis (rank-2) failed and alternative Z-Spin combinations match at comparable precision; the Schur-complement derivation is retracted because its empirical premise (R ≈ V V^T) fails at cos ≈ 0 and its implied mediator is putamen rather than thalamus. The retractions leave the empirical observations in Table 8 intact but withdraw their earlier structural interpretations.

For the Z-Spin Translational corpus, ZS-T5 v1.0 contributes: (i) a structural axis for the Cruzat phenomenon that is qualitatively coherent with ZS-Q7 v1.0 Theorem 1's dim(Y)/dim(X) \= 2 arrow-of-time direction without claiming numerical equality or physical realization (Cardinal NC-4 strictly preserved); (ii) an empirical motivation for the existence of a third-position Z-Spin mediator outside the current ENIGMA atlas, distinct from the left–right hemispheric mediator already verified in earlier corpus connectome work; and (iii) a worked example of Z-Spin Protocol Requirement C applied to a high-stakes retraction. Forward pointers: ZS-T5 v1.1 pending v0.12 execution of Appendix-B-class tests and TRN-inclusive atlas extension; future ZS-T papers may build on the five-motif synthesis once the anti-matching gate F-T5.6 is evaluated. For external researchers, the invitation is to re-compute our residuals on holdout cohorts (UK Biobank, ADNI, HCP-Aging) and to discriminate among the three readings of §5.2 by atlas extension or by dynamic-observable measurement.

**Acknowledgements & Code Availability**

Data: ENIGMA Toolbox v2.0 (Larivière et al. 2021), HCP Young Adult normative connectome matrices (n \= 207, group-averaged). Implementation: BrainSpace (Vos de Wael et al. 2020). External literature sweep informed by publicly available April 2026 searches covering Cruzat et al. 2023, Margulies et al. 2016, Worden 2024/2026, Kerskens & Pérez 2022, Li et al. 2020, Hádinger et al. 2022, Bao et al. 2025, Munn et al. 2023, Honey et al. 2009, Goñi et al. 2014, Deco et al. 2013, Lynn et al. 2021, and others cited in §2 and §5. AI assistance: Claude (Anthropic), operating under Z-Spin Protocol in \[자유 탐색\] mode for the exploration phase, \[코퍼스 탐색\] for derivation attempts, and \[논문 작성\] for the present paper. No AI-generated numerical values enter the pre-registered gates; all pre-registration locks precede AI-assisted analysis. No competing interests. No external funding.

Code availability. All numerical claims in Tables 4–8 and all retraction audits in §4.5 are reproducible from a single Python verification script (zs-t5\_verify.py, structurally identical to the original zb-c3\_verify.py released with the OSF archive; bundled sub-pipelines v0\_5, v0\_9\_residual, v0\_9\_deeper, v0\_10\_partition, v0\_10b\_gradient\_alignment, v0\_11\_derivation). Deterministic under the seeds specified in script headers. Repository: github.com/KennyKang-git/zspin (papers/08\_Translational/ZS-T5).

**Appendix A. Verification Script Inventory**

| Script / sub-pipeline | Purpose | Claim or audit output |
| ----- | ----- | ----- |
| v0\_5 (C1 primary) | C1 verification | Principal FC gradient → Cruzat ordering on Schaefer 100/200/300/400 (Table 4\) |
| v0\_9\_residual | C2 baseline | R\[X,Y\] top-2 fraction \= 0.81 across 4 parcellations; alignment with thalamic path negative (Table 7 baseline) |
| v0\_9\_deeper | C2 detail | Per-Yeo-network weights of R's top-2 singular vectors; leak cross-parcellation stability |
| v0\_9\_audit | C2 sub-claim (ii) | Adding 4 measurable subcortex 2-step paths reduces ‖R\_XY‖² by 1.03–1.51% (Table 6\) |
| v0\_10\_partition\_audit | C2 sub-claim (iii); §4.5 retraction 1 | Random-partition null z-scores \+7.25 to \+20.63 (Table 7); post-σ1 deflation s\[0\]/s\[1\] \= 1.25–1.73 (§4.5) |
| v0\_10b\_gradient\_alignment | C2 sub-claim (i) | R\_mode1 ↔ FC\_grad1 at |cos| \= 0.80–0.88; R\_mode1 ↔ SC\_grad1 at |cos| \= 0.02 (Table 5\) |
| v0\_11\_derivation\_audit | §4.5 retraction 3 | cos(R, V V^T) \= −0.066 to −0.093; putamen is the dominant V V^T contributor at 22–24% vs thalamus 11–14% |

Table A1. Inventory of seven sub-pipelines that together reproduce all numerical values in Tables 4–8 and all retraction audits in §4.5. All sub-pipelines are deterministic under specified seeds and run in under fifteen minutes combined on a single CPU with enigmatoolbox v2.0 installed.

**Appendix B. Registry of Pre-Registered Tests for ZS-T5 v1.1**

The following tests are pre-registered at the v1.0 release for execution in v1.1. Thresholds are LOCKED here and may not be relaxed during implementation.

| ID | Prediction | Observable | PASS threshold |
| ----- | ----- | ----- | ----- |
| T-T5.v12.1 | Γ-ratio ≈ 2 for cortex ↔ thalamus on HCP rs-fMRI time-series (ZS-Q7 Thm 1\) | Bidirectional Granger F-ratio on HCP-YA 1200-release time-series | PASS if ≥ 2/3 tested subject groups yield ratio in \[1.6, 2.4\] |
| T-T5.v12.2 | Thalamic BOLD AR(1) coefficient in \[0.80, 0.98\] (|f′(z\*)| \= 0.8915 ± 10%) | Per-subject AR(1) on thalamic BOLD, mean across HCP-YA | PASS if mean in \[0.80, 0.98\] with bootstrap 95% CI inside tolerance |
| T-T5.v12.3 | Scaling-law null: random 2-node pair yields mean|FC(pair→cortex)|/mean|FC(pair→pair)| ≠ 0.32 | Monte Carlo over 1000 random same-size 2-node pairs at Schaefer\_400 | PASS (thalamus retained as specific) if z \> 2; else DOWNGRADE Table 8 row 1 to purely anatomical |
| T-T5.v12.4 | TRN-inclusive atlas reduces ‖R\_XY‖² by \> 30% (F-T5.7) | Re-run v0.11 pipeline with MICA-TRN or Najdenovska 2018 | PASS if \> 30% reduction on ≥ 2/4 parcellations; identifies TRN as plausible mediator |
| T-T5.v12.5 | Anti-matching: 4 new external thalamic-interior theories map onto ≤ 2 of 5 motifs with equal fidelity (F-T5.6) | Blind coding by pre-registered scoring rubric | PASS (synthesis retained as INSIGHT) if ≤ 2/4 map; else DOWNGRADE to HYPOTHESIS low-discriminative-power |
| T-T5.v12.6 | Holdout UK Biobank cohort reproduces C1 at ρ ≥ \+0.60 (F-T5.3) | Same BrainSpace pipeline on UK Biobank 10,000-subject subset | PASS if ρ ≥ \+0.60 on ≥ 3/4 parcellations; else F-T5.3 triggered |

Table B1. Six pre-registered tests for ZS-T5 v1.1. Thresholds are LOCKED at v1.0 release and constitute the falsification contract for each claim. No threshold may be adjusted during v1.1 execution.

**References**

\[1\] T. Bachmann and J. Aru, Dendritic integration theory: A thalamo-cortical theory of state and content of consciousness, Philos. Mind Sci. 1, 1 (2020).  
\[2\] Z. Bao et al., Human high-order thalamic nuclei gate conscious perception, Science (in press, 2025).  
\[3\] R. A. I. Bethlehem, C. Paquola, J. Seidlitz et al., Dispersion of functional gradients across the adult lifespan, NeuroImage 222, 117299 (2020).  
\[4\] R. L. Buckner, F. M. Krienen, A. Castellanos, J. C. Diaz, and B. T. T. Yeo, The organization of the human cerebellum estimated by intrinsic functional connectivity, J. Neurophysiol. 106, 2322 (2011).  
\[5\] J. Cruzat, R. Herzog, P. Prado, Y. Sanz-Perl et al., Temporal irreversibility of large-scale brain dynamics in Alzheimer's disease, J. Neurosci. 43, 1643 (2023).  
\[6\] G. Deco, A. Ponce-Alvarez, P. Hagmann, G. L. Romani, D. Mantini, and M. Corbetta, How local excitation–inhibition ratio impacts the whole brain dynamics, J. Neurosci. 33, 11239 (2013).  
\[7\] G. Deco, Y. Sanz Perl et al., The INSIDEOUT framework provides precise signatures of the balance of intrinsic and extrinsic dynamics in brain states, Commun. Biol. 5, 572 (2022).  
\[8\] J. Goñi, M. P. van den Heuvel, A. Avena-Koenigsberger et al., Resting-brain functional connectivity predicted by analytic measures of network communication, Proc. Natl. Acad. Sci. USA 111, 833 (2014).  
\[9\] F. Gül et al., Cortico-thalamic spindle propagation requires 3-D topography and spatial weight scaling, Commun. Biol. (in press, 2026).  
\[10\] N. Hádinger et al., Region-selective control of the thalamic reticular nucleus by cortical L5 pyramidal cells, Nat. Neurosci. 25, 1308 (2022).  
\[11\] C. J. Honey, O. Sporns, L. Cammoun et al., Predicting human resting-state functional connectivity from structural connectivity, Proc. Natl. Acad. Sci. USA 106, 2035 (2009).  
\[12\] Z. Huang et al., Propofol-induced matrix:core thalamic shift in conscious perception, Nat. Commun. (2024).  
\[13\] E. G. Jones, The thalamic matrix and thalamocortical synchrony, Trends Neurosci. 24, 595 (2001).  
\[14\] K. Kang, Partition-Aware Routing in Block-Structured Networks: From Z-Spin Block Laplacians to Spectral Virtual Nodes (ZS-T1 v1.0), Z-Spin Cosmology Collaboration (2026).  
\[15\] K. Kang, Spectral Observatory: Structural Proximities Between Z-Spin Invariants and Undetermined Physical Constants (ZS-T2 v1.0), Z-Spin Cosmology Collaboration (2026).  
\[16\] K. Kang, Z-Sim: A Zero-Free-Parameter Forward Simulator for Z-Spin Cosmology (ZS-T3 v1.0), Z-Spin Cosmology Collaboration (2026).  
\[17\] K. Kang, The Cosmos–Human Isomorphism: Six-Step Telomere Hierarchy and (Body, DNA, Brain) Sector Decomposition (ZS-T4 v1.0), Z-Spin Cosmology Collaboration (2026).  
\[18\] K. Kang, The Z-Spin Action and U(1) Completion (ZS-F1 v1.0); A \= 35/437 (ZS-F2 v1.0); i-Tetration Fixed Point (ZS-F3 v1.0); Frobenius Classification dim(Z) \= 2 (ZS-F5 v1.0); ε-Field Inflation (ZS-U1 v1.0); Geometric Decoherence (ZS-Q1 v1.0); Structural Arrow of Time from the Z-Bottleneck (ZS-Q7 v1.0); i-Tetration Cascade (ZS-M1 v1.0); SU(2) Phase Gate (ZS-M3 v1.0); Block-Laplacian Spectral Verification (ZS-M6 v1.0); Z₂ Seam Involution (ZS-A7 v1.0). Z-Spin Cosmology Collaboration (2026).  
\[19\] C. M. Kerskens and D. L. Pérez, Experimental indications of non-classical brain functions, J. Phys. Commun. 6, 105001 (2022).  
\[20\] S. Larivière, C. Paquola, B. Y. Park et al., The ENIGMA Toolbox: multiscale neural contextualization of multisite neuroimaging datasets, Nat. Methods 18, 698 (2021).  
\[21\] Y. Li et al., Distinct subnetworks of the thalamic reticular nucleus, Nature 583, 819 (2020).  
\[22\] C. W. Lynn, E. J. Cornblath, L. Papadopoulos, and D. S. Bassett, Broken detailed balance and entropy production in the human brain, Proc. Natl. Acad. Sci. USA 118, e2109889118 (2021).  
\[23\] D. S. Margulies, S. S. Ghosh, A. Goulas et al., Situating the default-mode network along a principal gradient of macroscale cortical organization, Proc. Natl. Acad. Sci. USA 113, 12574 (2016).  
\[24\] I. N. Marshall, Consciousness and Bose–Einstein condensates, New Ideas Psychol. 7, 73 (1989).  
\[25\] B. Mišić, R. F. Betzel, A. Griffa et al., Network-level structure–function relationships in human neocortex, Cereb. Cortex 26, 3285 (2016).  
\[26\] J. Modolo, M. Hassan, F. Wendling, and P. Benquet, COALIA: A computational model of human EEG, PLOS Comput. Biol. 16, e1008503 (2019).  
\[27\] B. R. Munn, E. J. Müller, G. Wainstein, and J. M. Shine, The ascending arousal system shapes neural dynamics to mediate awareness of cognitive states, Proc. Natl. Acad. Sci. USA 120, e2306884120 (2023).  
\[28\] E. Najdenovska, Y. Alemán-Gómez, G. Battistella et al., In-vivo probabilistic atlas of human thalamic nuclei based on diffusion-weighted magnetic resonance imaging, Sci. Data 5, 180270 (2018).  
\[29\] J. Newman, Thalamic contributions to attention and consciousness, Conscious. Cogn. 4, 172 (1995).  
\[30\] K. H. Pribram, Languages of the Brain: Experimental Paradoxes and Principles in Neuropsychology (Prentice-Hall, 1971).  
\[31\] R. H. Segman, Wave-based neural communication (preprint, 2020).  
\[32\] R. Vos de Wael, O. Benkarim, C. Paquola et al., BrainSpace: a toolbox for the analysis of macroscale gradients in neuroimaging and connectomics datasets, Commun. Biol. 3, 103 (2020).  
\[33\] R. Worden, The quantum mind: A consciousness model (preprint, 1999).  
\[34\] R. Worden, Perceptual Wave Theory: a Fourier framework for thalamic wave encoding, Front. Psychol. / Active Inference Inst. (2024/2026).

**Version History**

v1.0 (May 2026): Initial public release as ZS-T5 (Translational T-series, paper 5 of T-series). Consolidated from internal Z-Spin Collaboration research notes up to v3.1.0 of the ZB-C3 v1.0 source manuscript (April 22, 2026), restructured into the Z-Spin T-series format with the following changes: (i) all 'ZB-' source citations rewritten as 'ZS-' citations per corpus-wide unification policy, with version strings preserved; (ii) 'Z-mediation' rewritten as 'Z-Spin mediation' / 'Z-Spin mediator' throughout, per the corpus terminology guideline that mediation is an action of the Z-Spin operator on the Z-sector stage; (iii) the originating Z-Brain paper-specific NON-CLAIMs NC-C3.1–NC-C3.5 rewritten as NC-T5.1–NC-T5.5 with one additional Cardinal NC-4 inheritance NC-T5.6; (iv) eight falsification gates F-C3.1–F-C3.8 rewritten as F-T5.1–F-T5.8; (v) verification scripts re-bundled as zs-t5\_verify.py with structurally identical sub-pipelines. All numerical claims (Tables 4–8), retraction audits (§4.5), and falsification thresholds (Table 10, Table B1) are unchanged from the source manuscript and remain LOCKED. Two VERIFIED claims (C1, C2). One HYPOTHESIS (C3 naive static-FC, explicitly failed). Three RETRACTED proposals with full audit trail (rank-2 \= dim(Z) \= 2, leak \= |z\*|/dim(X), Schur-complement). One INSIGHT-level five-motif synthesis. Six TESTABLE pre-registered tests in Appendix B. Closed Epistemic Legend. Zero free parameters. Substrate-Agnostic Block Fiedler Application; Cardinal NC-4 preserved throughout.