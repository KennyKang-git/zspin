**ZS-T7: Pulvinar-Mediated Z-Spin Language Partition**

*A Z-Spin Mediator Test of the Block Fiedler Mediation Theorem on the Phonological–Semantic Cortical Decomposition with Lesion-Symptom Predictions*

**Author: Kenny Kang**  
Affiliation: Independent Researcher | Z-Spin Cosmology Collaboration  
Date: May 2026 (v1.1 amendment)  
Theme: Translational \[ZS-T\] | Paper 7 of T-series | Code: ZS-T7 v1.1

**Verification:** 27/27 closed-form \+ in-silico gates PASS | 10 \[TESTABLE\] empirical predictions (P1–P10) across three levels: connectome (P1–P6), oscillatory (P7), and lesion-symptom (P8–P10) | Zero free parameters | Three new theorems registered: Theorem T7.3 (Lesion-Symptom Coupling Theorem) \[DERIVED\]; Theorem T7.4 (TOT-as-Coupling-Failure) \[DERIVED-CONDITIONAL\]; Theorem T7.5 (Theta-Pulvinar Phase-Locking Specificity) \[INSIGHT\]

**Inherits:** ZS-T1 v1.0 §9.3 Block Fiedler Mediation Theorem \[PROVEN\]; ZS-Q7 v1.0 §4 Theorem 2 channel capacity bound \[DERIVED\]; ZS-F5 v1.0 §4 dim(Z) \= 2 \[PROVEN\]; ZS-F1 v1.0 §9 \+ ZS-S1 v1.0 §4 L\_XY ≡ 0 from action \[PROVEN\]; ZS-M6 v1.0 §7A continuum perturbative protection \[PROVEN-PERTURBATIVE\]; ZS-T4 v1.0 Cardinal NC-4 \[LOCKED\]; ZS-T5 v1.0 ZB→ZS conversion protocol; ZS-QH v1.0 Hardware Axiom H2 (all I/O through Z-sector) \[DERIVED\]; ZB-N1 v3.0 thalamocortical Z-Spin mediation \[VERIFIED on HCP\]; ZB-V1 v1.0 §24.4 scenario γ nested Z-Spin mediators \[DERIVED-CONDITIONAL\]; ZB-P3 v1.0 ln(2) channel-capacity bound \[DERIVED-CONDITIONAL\]; ZB-C5 v1.0 source manuscript.

**Source manuscript and revision history:** ZS-T7 v1.0 (May 2026\) was the T-series translational restatement of ZB-C5 v1.0 (Z-Brain corpus, May 2026), restructured under the ZS-T5 v1.0 conversion protocol with two anti-numerology additions (NC-T7.13/14 \+ F-T7.13). The present v1.1 amendment introduces three new theorems (T7.3, T7.4, T7.5), four new TESTABLE predictions (P7–P10), three new falsification gates (F-T7.14, F-T7.15, F-T7.16), and revises NC-T7.8 (disease-specific perturbations now TESTABLE) and NC-T7.13 (theta band registered as prima facie more empirically anchored). Full v1.0 → v1.1 changelog in §13. Verification artifact upgraded from zs-t7\_verify\_v1\_0.py (24/24 PASS) to zs-t7\_verify\_v1\_1.py (27/27 PASS) with three new gates G-F.1, G-F.2, G-F.3 covering the lesion-symptom theorem closed-form structure.

# **§0. Abstract**

We pre-register a partition of the human cortex into phonological/articulatory P\_X (left-lateralized: Broca's area BA 44/45, area 55b, ventral premotor 6v, primary auditory L\_TA2/L\_A1), bilateral medial pulvinar P\_Z (|P\_Z| \= 2), and distributed semantic P\_Y (anterior temporal lobe bilateral, angular gyrus, posterior superior temporal sulcus, middle temporal gyrus, inferior frontal gyrus semantic regions). Under the Block Fiedler Mediation Theorem (ZS-T1 v1.0 §9.3, PROVEN), this partition predicts a suppression ratio S\_XY ≤ 0.10 and a Fiedler neutrality F\_Z ≤ 0.30 across six parcellations of the HCP normative connectome.

ZS-T7 v1.1 advances five structural contributions over v1.0. (i) Theorem T7.1 (DERIVED-CONDITIONAL): bilateral medial pulvinar as language partition Z-Spin mediator, structurally distinct from bilateral lateral pulvinar (visual; ZB-V1). (ii) Theorem T7.2 (INSIGHT): lexical retrieval throughput Φ\_lang ≤ f · ln(2) bits/sec, with the band f explicitly registered as an empirical question (NC-T7.13 v1.1: theta is now treated as the prima facie more anchored band on the basis of Giraud and Poeppel 2012, Doelling et al. 2014, and Coupé et al. 2019 evidence; alpha is retained as a corpus-internal hypothesis from ZB-V1's visual codec inheritance). (iii) Theorem T7.3 (DERIVED, NEW in v1.1): the Lesion-Symptom Coupling Theorem — under L\_XY ≡ 0 \[PROVEN, ZS-F1 §9 / ZS-S1 §4 / ZS-M6 §7A all-orders\] and Hardware Axiom H2 (all I/O through Z-sector) \[DERIVED, ZS-QH v1.0\], removal of P\_Z while preserving P\_X and P\_Y selectively breaks the X-Y channel without degrading X-internal or Y-internal processing. This converts thalamic-aphasia case observations into pre-registered quantitative predictions (P8). (iv) Theorem T7.4 (DERIVED-CONDITIONAL, NEW in v1.1): the Tip-of-the-Tongue (TOT) phenomenon is identified as the phenomenological signature of partial Z-channel saturation — semantic representations available, phonological representations partially available, the coupling channel below capacity threshold. (v) Theorem T7.5 (INSIGHT, NEW in v1.1): if F-T7.13 resolves PASS-θ, then peri-pulvinar theta phase-locking value (PLV) reduction during lexical retrieval is the diagnostic signature of P\_Z dysfunction.

Ten pre-registered predictions across three empirical levels are advanced. P1–P6 (inherited from v1.0): connectome-level S\_XY, F\_Z, AN3 mean rank, and lateralization on HCP-YA. P7 (theta vs alpha resolution on Cam-CAN MEG, NEW in v1.1, formalizing F-T7.13 from v1.0 into a TESTABLE prediction). P8 (lesion-symptom triple dissociation on thalamic stroke cohorts, NEW in v1.1): medial pulvinar lesion patients should show preserved single-word comprehension (P\_Y intact), preserved repetition (P\_X intact), but impaired confrontation naming (X-Y coupling disrupted) at effect size d ≥ 0.8 versus matched ATL-lesion and SMG/IFG-lesion controls. The empirical foundation for P8 is the existing Hillis et al. (2014) Frontiers in Neurology cohort observation that three of ten isolated thalamic-lesion patients showed naming deficits with preserved comprehension and repetition. P9 (N400 attenuation in pulvinar-lesion patients, NEW in v1.1): N400 amplitude in the 300–500 ms window (Kutas and Federmeier 2011\) should be reduced by ≥ 50% in pulvinar-lesion patients compared to matched controls, while early auditory components (100–200 ms) and late positivity (500+ ms) remain within normal range. P10 (theta-pulvinar PLV degradation, NEW in v1.1): conditional on F-T7.13 PASS-θ, medial pulvinar lesion patients should show theta-band power reduction ≥ 40% in left peri-temporal cortex during picture naming, with alpha-band power preserved within normal range.

Sixteen falsification gates F-T7.1 through F-T7.16 across four levels (mathematical, in-silico, observational, external replication). Fourteen NON-CLAIMs delimit framework scope; NC-T7.8 (disease-specific perturbations) is amended in v1.1 from full exclusion to scope-narrowed exclusion (only treatment-pharmacological predictions remain NON-CLAIM; lesion-deficit predictions are now TESTABLE under P8–P10). NC-T7.13 (alpha vs theta) is amended to explicitly recognize theta as the prima facie more empirically anchored band, with alpha retained as a corpus-internal hypothesis subject to F-T7.13 resolution. Verification artifact zs-t7\_verify\_v1\_1.py reports 27/27 closed-form \+ in-silico gates PASS, with three new gates G-F.1, G-F.2, G-F.3 covering Theorem T7.3 closed-form structure. Cardinal NC-4 (Z-Brain) preserved throughout: no claim is made that the brain physically realizes Z-Spin Planck-scale geometry; the dim(Z) \= 2 partition dimension and the (V\_XZ, V\_ZY) handshake protocol are imported as substrate-agnostic mathematical structures.

ZS-T7 v1.1 therefore advances the corpus from a connectome-only framework (v1.0) to a multi-level prediction framework (v1.1) addressing four established neuroscientific puzzles: (i) the dorsal-ventral language stream integration mechanism (Hickok and Poeppel 2007); (ii) the cortical-thalamic substrate of fluent thalamic aphasia with naming deficit (Crosson 1985; Hillis et al. 2014; Schaefer-Shariat 2022); (iii) the structural origin of the lexical retrieval throughput ceiling at the Zheng-Meister 10 bits/sec scale; (iv) the mechanism of the tip-of-the-tongue phenomenon as transmission deficit (Brown and McNeill 1966; Kutas and Federmeier 2011 N400 framework). For each puzzle, ZS-T7 v1.1 provides a structurally derived prediction with explicit threshold and falsification gate.

*Keywords:* Block Fiedler Mediation Theorem, Z-Spin mediation, language partition, medial pulvinar, lexical retrieval throughput, channel capacity bound, alpha-vs-theta invocation, lesion-symptom triple dissociation, thalamic aphasia, tip-of-the-tongue, anti-numerology discipline, Cardinal NC-4.

# **Epistemic Status Legend**

Tags applied to claims in this paper are drawn from the closed set below. Ad-hoc qualifiers (e.g., "corroborated", "strongly suggests", "consistent with") are not permitted under the Z-Brain Protocol v1.1 §4.3 Requirement E discipline. Each tag carries an operational meaning inherited from prior corpus releases. The tag set is unchanged from ZS-T7 v1.0; only the population of tagged claims is extended in v1.1 with three new theorems and four new TESTABLE predictions.

| Epistemic Status Legend (closed tag set) LOCKED — Core constant or input fixed by prior paper; no downstream paper may modify. PROVEN — Mathematical theorem verified to machine precision in source paper. PROVEN-PERTURBATIVE — PROVEN to all orders in perturbation theory; non-perturbative closure may still be OPEN. DERIVED — Follows from Z-Spin action \+ prior PROVEN inputs; zero new free parameters. DERIVED-CONDITIONAL — DERIVED under an explicitly stated assumption (named in the paper). VERIFIED — Numerical confirmation of a DERIVED or PROVEN result on empirical data. INSIGHT — Structural observation linking corpus elements; not itself a claim about external data. HYPOTHESIS — Motivated conjecture awaiting derivation or empirical verification. HYPOTHESIS-strong — HYPOTHESIS with multiple corpus-internal consistency anchors. TESTABLE — Pre-registered prediction with explicit threshold, data source, and falsification criterion. TESTABLE-PENDING — TESTABLE prediction awaiting cohort-data execution; thresholds locked at release. OBSERVATION — Empirical finding reported without an attached structural claim. NON-CLAIM — Explicit refusal to claim a particular thing; bounds the framework's reach. OPEN — Recognized gap honestly registered; resolution path identified. RETRACTED — Earlier proposal withdrawn after audit; full audit trail documented. |
| :---- |

# **§1. Introduction**

## **§1.1 Position in the T-series and v1.0 → v1.1 transition**

ZS-T1 v1.0 (March 2026\) established Spectral Virtual Nodes and the Block Fiedler Mediation Theorem as the substrate-agnostic mathematical kernel. ZS-T2 v1.0 (March 2026\) established the anti-numerology audit protocol (5670 × 29 Monte Carlo scan). ZS-T3 v1.0 (March 2026\) provided the Z-Sim forward simulator. ZS-T4 v1.0 (May 2026\) extended (X, Z, Y) \= (3, 2, 6\) decomposition to the organism scale (Body, DNA, Brain). ZS-T5 v1.0 (May 2026\) audited the principal connectivity gradient at the cortical scale. ZS-T6 v1.0 (May 2026\) extended downward to chromatin and cell-cycle scales.

ZS-T7 v1.0 (May 2026\) was the T-series translational restatement of ZB-C5 v1.0, restructured under the ZS-T5 v1.0 conversion protocol with two anti-numerology additions (NC-T7.13/14 \+ F-T7.13). ZS-T7 v1.0 was a pillar-paper-launch: theoretical framework \+ six pre-registered TESTABLE-PENDING connectome predictions (P1–P6); empirical determination reserved for a future amendment.

ZS-T7 v1.1 (the present amendment, May 2026\) extends v1.0 in three substantive directions, motivated by external feedback identifying a gap between the connectome-only predictions of v1.0 and the lesion-symptom predictions that external neuroscientists can directly test in their clinical and electrophysiological work. First, we derive a new Theorem T7.3 (Lesion-Symptom Coupling Theorem) from the corpus-PROVEN L\_XY ≡ 0 result of ZS-F1 §9 / ZS-S1 §4 / ZS-M6 §7A and the ZS-QH v1.0 Hardware Axiom H2 (all I/O through Z-sector). Theorem T7.3 makes a pre-registered triple-dissociation prediction (P8): pulvinar-territory lesion patients should show preserved single-word comprehension (P\_Y intact), preserved repetition (P\_X intact), but impaired confrontation naming (X-Y coupling disrupted). Second, we identify the tip-of-the-tongue (TOT) phenomenon as the phenomenological signature of partial Z-channel saturation (Theorem T7.4, DERIVED-CONDITIONAL), connecting the corpus's channel capacity bound directly to a well-known psycholinguistic phenomenon. Third, we revise the alpha-vs-theta non-claim NC-T7.13 (v1.0) to recognize theta as the prima facie more empirically anchored band on the basis of the established cortical syllable-tracking literature, while retaining alpha as a corpus-internal hypothesis subject to empirical resolution on Cam-CAN MEG (P7, formalized from F-T7.13 v1.0).

All numerical anchors used in v1.1 inherit unchanged from prior corpus releases. No new free parameters are introduced. Cardinal NC-4 (Z-Brain) is preserved throughout. The verification artifact is upgraded from zs-t7\_verify\_v1\_0.py (24/24 PASS) to zs-t7\_verify\_v1\_1.py (27/27 PASS) with three new gates G-F.1 through G-F.3 covering Theorem T7.3 closed-form structure.

## **§1.2 Four established puzzles addressed by ZS-T7 v1.1**

ZS-T7 v1.1 addresses four established puzzles in the cognitive and clinical neuroscience of language. For each puzzle we identify the corpus asset deployed and the corresponding theorem and pre-registered prediction. The puzzles are not selected ad-hoc but are the four for which the Block Fiedler Mediation Theorem \+ L\_XY ≡ 0 architecture has direct analytic content.

*Table 1\. Four established puzzles in language neuroscience addressed by ZS-T7 v1.1, with the corresponding Z-Spin asset deployed and the theorem / prediction registered. Each puzzle has an extensive external literature; the contribution of ZS-T7 v1.1 is the Block Fiedler Mediation Theorem \+ L\_XY ≡ 0 derivation that makes a structurally pre-registered, falsifiable prediction.*

| \# | Established puzzle | Z-Spin asset deployed | T7 theorem / prediction |
| ----- | ----- | ----- | ----- |
| 1 | How are dorsal phonological and ventral semantic streams integrated into unified lexical retrieval? (Hickok and Poeppel 2007\) | Block Fiedler Mediation Theorem \[PROVEN, ZS-T1 §9.3\] \+ dim(Z) \= 2 \[PROVEN, ZS-F5\] | T7.1 \+ P1–P6 |
| 2 | Why does fluent thalamic aphasia (especially after pulvinar lesion) produce naming deficits with preserved comprehension and repetition? (Crosson 1985; Hillis et al. 2014; Schaefer-Shariat 2022\) | L\_XY ≡ 0 \[PROVEN, ZS-F1 §9; ZS-S1 §4; ZS-M6 §7A all-orders\] \+ Hardware Axiom H2 (all I/O through Z) \[DERIVED, ZS-QH\] | T7.3 \+ P8 |
| 3 | Why is human conscious lexical retrieval bounded near 10 bits/sec (Zheng and Meister 2024\) and how does it relate to the cortical theta rhythm at 4–8 Hz that tracks syllable rate? (Giraud and Poeppel 2012; Coupé et al. 2019\) | Channel capacity ≤ ln(2) per Z-Spin mediator invocation \[DERIVED, ZS-Q7 §4 Theorem 2\] \+ dim(Z) \= 2 \[PROVEN, ZS-F5\] | T7.2 \+ P7 \+ T7.5 |
| 4 | What is the mechanism of the tip-of-the-tongue (TOT) phenomenon — the conscious experience of inaccessible phonology with intact semantics? (Brown and McNeill 1966; transmission deficit theory: Burke et al. 1991; Kutas and Federmeier 2011 N400 review) | Channel saturation under L\_XY ≡ 0 \+ Holevo bound \[DERIVED, ZS-Q7 \+ ZS-Q1 §3.3\] | T7.4 \+ P9 |

Each row of Table 1 is registered with explicit thresholds, decision rules, and falsification gates in §6 (theorems and predictions) and §7 (falsification gates). The structural commitment of the framework — that the same Block Fiedler partition handles all four puzzles via the same L\_XY ≡ 0 \+ ln(2) capacity architecture — is itself a falsifiable claim: if puzzles 2, 3, or 4 turn out to require structurally distinct mechanisms, the unified-mediator hypothesis is weakened or refuted (F-T7.16, programme-level).

## **§1.3 Dorsal-ventral language streams and the pulvinar (puzzle 1\)**

The human language system is conventionally described as comprising two parallel processing streams (Hickok and Poeppel 2007): a dorsal phonological/articulatory stream (Heschl's gyrus → planum temporale → posterior superior temporal gyrus → ventral premotor → Broca's area) and a ventral semantic stream (anterior temporal lobe, middle temporal gyrus, angular gyrus, inferior frontal gyrus semantic subdivisions). Fedorenko, Ivanova, and Regev (2024) characterize the language network as a domain-specific "natural kind" with selective response to syntactic processing distinct from arithmetic, music, executive function, and theory of mind.

A long-standing puzzle in this dual-stream architecture is the integration mechanism: how do phonological and semantic representations combine into unified lexical retrieval at the moment of speech production or comprehension? Classical tractography (Catani 2002; Saur et al. 2008\) emphasizes white-matter bundles — arcuate fasciculus, inferior longitudinal fasciculus, uncinate fasciculus — as cortico-cortical connectors. Recent work expands this with thalamo-cortical contributions: Crosson (1985) reported thalamic aphasia after VL/MD lesions; Saalmann et al. (2012) demonstrated pulvinar attention modulation; Maldonado et al. (2024) reconstructed four distinct pulvino-temporal fibre tracts (Arnold proper, OR-like, lateral, AR-like) using diffusion tractography combined with awake-surgery anomia stimulation.

These observations suggest a Z-Spin mediator architecture for language: a thalamic relay (specifically the medial pulvinar) bridges the phonological P\_X and semantic P\_Y cortical compartments. ZS-T7 v1.0 formalized this hypothesis using the Block Fiedler Mediation Theorem (ZS-T1 v1.0 §9.3, PROVEN) and pre-registered a six-parcellation HCP test analogous to the multi-resolution ZB-N1 v3.0 thalamic verification (P1–P6). The present v1.1 amendment retains P1–P6 unchanged and adds four new predictions (P7–P10) addressing puzzles 2, 3, and 4\.

## **§1.4 Thalamic aphasia and the lesion-symptom triple dissociation (puzzle 2\)**

Thalamic aphasia is a rare language disorder occurring in 0.25–3% of ischemic stroke patients (Schaefer and Shariat 2022). Most patients exhibit mild symptoms with a predominance of lexical-semantic deficits — anomia and semantic paraphasias — while comprehension and repetition are mostly spared (Schaefer and Shariat 2022). Lesions to the pulvinar specifically have been described to result in fluent aphasia with naming deficits and semantic paraphasias (Bruzzone Giraldez et al. 2015; Ojemann, Fedio, and Van Buren 1968).

Hillis et al. (2014, Frontiers in Neurology) reported a clinically significant phenotype: of ten patients with isolated left thalamic lesions, three exhibited isolated naming deficits with normal comprehension and normal repetition, all with normal cortical perfusion (i.e., the cortical phonological and semantic regions were fully intact). This is the hallmark phenotype that the present paper's Theorem T7.3 (Lesion-Symptom Coupling Theorem, DERIVED in v1.1) predicts from L\_XY ≡ 0 \+ Hardware Axiom H2: when the Z-Spin mediator P\_Z is removed (lesioned) while P\_X and P\_Y are preserved (no cortical perfusion deficit), the X-internal and Y-internal processing remain intact (preserved repetition and comprehension respectively), but the X-Y coupling channel is disrupted (impaired naming, which requires phonology-semantics binding).

The structural prediction is therefore a triple dissociation: pulvinar-lesion patients should differ from both ATL-lesion patients (who show semantic loss) and SMG/IFG-lesion patients (who show phonological repetition deficits) in showing the inverse pattern — preserved comprehension AND preserved repetition AND impaired naming. This is the classical "transcortical" pattern of fluent aphasia with isolated naming impairment, here derived from the corpus's PROVEN L\_XY ≡ 0 architecture rather than postulated phenomenologically. P8 operationalizes this triple dissociation.

## **§1.5 Lexical retrieval throughput, theta rhythm, and the 10 bits/sec ceiling (puzzle 3\)**

Zheng and Meister (2024) reported that the upper bound on human conscious behavioral throughput across all task modalities is approximately 10 bits/sec, despite peripheral sensory input rates of order 10⁹ bits/sec. They termed this "the unbearable slowness of being" and identified it as a long-standing puzzle in the structure of conscious cognition. Independently, Coupé et al. (2019) reported that across 17 languages from 9 language families, speech production rate centers near 39 bits/sec (with information density per syllable trading off against syllable rate), close to the cortical theta rhythm at 4–8 Hz that tracks syllable boundaries (Giraud and Poeppel 2012; Doelling et al. 2014; Luo and Poeppel 2007; Hyafil et al. 2015).

ZS-T7 v1.0 §2.3 Theorem T7.2 (INSIGHT) noted that under L\_XY ≡ 0 with dim(Z) \= 2, the X-Y channel capacity is bounded by ln(2) ≈ 0.693 nats per Z-Spin mediator invocation (ZS-Q7 v1.0 §4 Theorem 2, DERIVED). At invocation frequency f the throughput is bounded by f · ln(2) bits/sec. ZS-T7 v1.0 inherited f \= f\_α \= 10 Hz from ZB-V1's visual codec, yielding ≈ 6.93 bits/sec — close to but below the Zheng-Meister ceiling. ZS-T7 v1.0 NC-T7.13 explicitly registered the alpha-vs-theta band selection as an empirical question, and NC-T7.14 explicitly refused to identify the Coupé 39 / Zheng-Meister 10 ratio (≈ 4\) with the four-handshake structure.

The present v1.1 amendment strengthens this analysis in two ways. First, NC-T7.13 is amended to recognize theta as the prima facie more empirically anchored band: the syllable-tracking theta literature (Giraud and Poeppel 2012; Doelling et al. 2014\) is substantially stronger than any alpha-language phase-locking literature, and the alpha \= 10 Hz inheritance from ZB-V1 was specific to the visual codec. At f \= f\_θ \= 5 Hz the bound gives 3.47 bits/sec; at f \= 7 Hz it gives 4.85 bits/sec. The choice between alpha and theta is operationalized in P7 (Cam-CAN MEG resolution) which formalizes the v1.0 F-T7.13 gate into a TESTABLE prediction. Second, Theorem T7.5 (INSIGHT, NEW in v1.1) registers the diagnostic signature: if F-T7.13 / P7 resolves PASS-θ, then peri-pulvinar theta phase-locking value (PLV) reduction in pulvinar-lesion patients during lexical retrieval becomes a falsifiable signature of P\_Z dysfunction.

## **§1.6 Tip-of-the-tongue as transmission deficit (puzzle 4\)**

The tip-of-the-tongue (TOT) phenomenon (Brown and McNeill 1966\) is the conscious experience of being unable to retrieve a known word despite full availability of its semantic content and partial availability of its phonological features (e.g., the speaker often correctly recalls the first letter, the number of syllables, or the syllabic stress; Burke et al. 1991). The transmission deficit hypothesis (Burke et al. 1991; transmission deficit model summarized in MacKay and Burke 1990\) proposes that TOT arises from inadequate transmission of priming from activated lexical-semantic representations to phonological representations — i.e., from a coupling failure between intact P\_Y (semantic) and partially-activated P\_X (phonological) endpoints.

This is exactly the structural scenario that the L\_XY ≡ 0 \+ ln(2) capacity architecture predicts: when the Z-Spin mediator channel operates at sub-saturation, the X-Y handshake count per unit time is reduced. Under such conditions, partial information transfer is possible (consistent with TOT subjects' partial phonological access — first letter, syllable count) but full retrieval is not (consistent with TOT subjects' inability to produce the word). Theorem T7.4 (DERIVED-CONDITIONAL, NEW in v1.1) registers TOT as the phenomenological signature of partial Z-channel saturation, and P9 operationalizes this via the N400 ERP signature (Kutas and Federmeier 2011): N400 amplitude in the 300–500 ms window should be reduced in pulvinar-lesion patients (chronic Z-channel disruption) compared to matched controls, while early auditory components (100–200 ms, consistent with intact P\_X processing) and late positivity (500+ ms, consistent with intact post-lexical processing) remain within normal range.

## **§1.7 Z-Brain corpus inputs**

ZB-N1 v3.0 (Kang 2026a) verified bilateral thalamus as Z-Spin mediator of the sensorimotor versus higher-order partition across six parcellations with S\_XY ∈ \[0.058, 0.087\] across all parcellations on structural connectivity. ZB-V1 v1.0 introduced scenario γ (nested Z-Spin mediators within the same anatomical thalamus): bilateral lateral pulvinar mediates the visual sub-partition with |P\_Z| \= 2 satisfying dim(Z) \= 2\. ZB-K Notebook 005 §3 registered the partition-dependence principle. ZB-P2 v1.0 NC-P2.2 explicitly excluded Variable Binding from Z-Spin mediation framework reach (preserved as NC-T7.5 inheritance). ZB-P3 v1.0 ln(2) channel-capacity bound is imported as Theorem T7.2 INSIGHT.

## **§1.8 Z-Spin imports**

The relevant Z-Spin inputs for the present paper are entirely structural-mathematical, not physical. (i) ZS-T1 v1.0 §9.3 Block Fiedler Mediation Theorem (PROVEN). (ii) ZS-F5 v1.0 §4 Frobenius result (PROVEN): dim(Z) \= 2 from polyhedral gauge constraint. (iii) ZS-Q7 v1.0 §4 Theorem 2 (DERIVED): X-Y channel capacity ≤ ln(2) under L\_XY ≡ 0, via Stinespring dilation (ZS-Q1 §3.3 Theorem 3.2, PROVEN) and the Holevo bound. (iv) ZS-F1 v1.0 §9 \+ ZS-S1 v1.0 §4 (PROVEN): L\_XY ≡ 0 directly from the Z-Spin action. (v) ZS-M6 v1.0 §7A (PROVEN-PERTURBATIVE): L\_XY^{eff,direct} \= 0 to all orders in perturbation theory via four independent protection layers. (vi) ZS-QH v1.0 Hardware Axiom H2 (DERIVED): all I/O through the Z-sector. (vii) ZS-T4 v1.0 Cardinal NC-4 (LOCKED): no physical realization claim. NEW in v1.1: (viii) the conjunction (iv) \+ (v) \+ (vi) is invoked explicitly in Theorem T7.3 to derive the Lesion-Symptom Coupling result.

# **§2. Theoretical Framework**

## **§2.1 Locked Inputs (no re-tuning)**

All inputs are imported unchanged from prior corpus papers. No threshold or parameter is tuned to ZS-T7 v1.1 data. Three new entries (rows marked NEW in v1.1) are explicitly invoked in the new theorems T7.3, T7.4, T7.5; all three are at PROVEN, PROVEN-PERTURBATIVE, or DERIVED status in their source paper at v1.0 freeze convention.

*Table 2\. Locked inputs for ZS-T7 v1.1. All entries are PROVEN, DERIVED, or LOCKED in prior corpus papers; no parameter is adjusted within this paper. Entries inherited from v1.0 are unchanged. Three new entries (NEW in v1.1) are required for the new theorems T7.3, T7.4, T7.5.*

| Input | Value / Statement | Source | Status |
| ----- | ----- | ----- | ----- |
| Block Fiedler Mediation Theorem | ψ\_2|\_Z \= 0 ideal | ZS-T1 v1.0 §9.3 | PROVEN |
| dim(Z) \= 2 (Frobenius classification) | bilateral mediator cardinality | ZS-F5 v1.0 §4 | PROVEN |
| Channel capacity per Z-cell | ≤ ln(2) ≈ 0.693 nats | ZS-Q7 v1.0 §4 Theorem 2 | DERIVED |
| S\_XY threshold | \< 0.10 | ZS-M6 v1.0 §4.5 | LOCKED |
| F\_Z threshold | \< 0.30 | ZS-T1 v1.0 §9.3 Cor 9.2 | LOCKED |
| L\_XY ≡ 0 from Z-Spin action \[NEW in v1.1\] | no direct X-Y coupling at action level | ZS-F1 v1.0 §9; ZS-S1 v1.0 §4 | PROVEN |
| L\_XY^{eff,direct} \= 0 all orders \[NEW in v1.1\] | four independent protection layers | ZS-M6 v1.0 §7A | PROVEN-PERTURBATIVE |
| Hardware Axiom H2 (all I/O through Z) \[NEW in v1.1\] | X↔Z and Z↔Y allowed; X↔Y direct \< 1% | ZS-QH v1.0 | DERIVED |
| Stinespring dilation Kraus pair | {K\_0, K\_1}, dim(Z) \= 2 | ZS-Q1 v1.0 §3.3 Theorem 3.2 | PROVEN |
| HCP normative SC/FC | n ≈ 207, group-averaged | ENIGMA Toolbox v2.0 (Larivière et al. 2021\) | LOCKED |
| Six parcellations | DK-82 \+ Schaefer 100/200/300/400 \+ Glasser-360 | ZB-N1 v3.0 §2.2 | LOCKED |
| Cardinal NC-4 (Z-Brain) | no physical realization of Z-Spin geometry in brain biology | ZS-T4 v1.0 §1.2 | LOCKED |
| Thalamus \= Z-Spin mediator (whole-thalamus partition) | S\_XY ∈ \[0.058, 0.087\], 29/36 PASS | ZB-N1 v3.0 | VERIFIED on HCP |
| Lateral pulvinar \= visual Z-Spin mediator (scenario γ) | Theorem V1.1, |P\_Z| \= 2 | ZB-V1 v1.0 | DERIVED-CONDITIONAL |
| ln(2) per invocation \= lexical bound | Theorem V1.2 visual codec | ZB-V1 v1.0 \+ ZS-Q7 §4 Theorem 2 | DERIVED |
| NC-P2.2 Variable Binding exclusion | Z-Spin framework silent on compositional binding | ZB-P2 v1.0 | LOCKED |

## **§2.2 Theorem T7.1 — Medial pulvinar as language partition Z-Spin mediator \[DERIVED-CONDITIONAL\]**

**Statement (unchanged from v1.0).** Define the language partition of the human connectome as P\_X^lang \= {Broca's area (BA 44, 45\) left, area 55b left, ventral premotor 6v left, primary auditory L\_TA2/L\_A1 bilateral, perisylvian language L\_PSL}, P\_Z^lang \= {bilateral medial pulvinar PuM}, P\_Y^lang \= {anterior temporal lobe bilateral, angular gyrus bilateral, posterior superior temporal sulcus bilateral, middle temporal gyrus bilateral, IFG semantic L\_47l/L\_47s}. On HCP normative structural and functional connectomes, the language partition admits a Block-Laplacian-with-zero-X-Y-block decomposition in the sense of ZS-T1 v1.0 §9.3 Theorem 9.1, with bilateral medial pulvinar serving as the Z-Spin mediator.

**Derivation chain.** As in ZS-T7 v1.0 §2.2 Steps 1–7. Status: DERIVED-CONDITIONAL on Steps 5 (P1, P2 PASS on HCP-YA) \+ Step 6 (P3, P4 PASS on AN3). Six pre-registered predictions P1–P6 (§3) operationalize Steps 5–6.

## **§2.3 Theorem T7.2 — Lexical retrieval throughput bound \[INSIGHT\] (revised in v1.1)**

**Statement.** The lexical retrieval throughput of the pulvinar-mediated language channel is bounded above by f · ln(2) bits/sec, where f is the frequency of Z-Spin mediator invocation. The band of f is empirically registered (NC-T7.13 v1.1; P7) and is NOT determined by Z-Spin axioms in v1.1. Two structurally consistent readings are presented below; their disjunction is the v1.1 form of Theorem T7.2.

**Reading T7.2.A (alpha-band, ZB-V1 visual-codec inheritance).** If f \= f\_α \= 10 Hz then Φ\_lang ≤ 10 · 0.693 \= 6.93 bits/sec; alpha-band lower bound 8 Hz gives 5.55 bits/sec; alpha-band upper bound 13 Hz gives 9.01 bits/sec. This reading is inherited from ZB-V1 v1.0 alpha-cycle invocation and recovers the Zheng-Meister (2024) \~10 bits/sec ceiling at the upper alpha bound.

**Reading T7.2.B (theta-band, syllable-tracking literature anchor).** If f \= f\_θ \= 5 Hz then Φ\_lang ≤ 5 · 0.693 \= 3.47 bits/sec; theta-band lower bound 4 Hz gives 2.77 bits/sec; theta-band upper bound 8 Hz gives 5.55 bits/sec. This reading is anchored on the established cortical syllable-tracking literature (Giraud and Poeppel 2012; Doelling et al. 2014; Luo and Poeppel 2007; Hyafil et al. 2015\) and recovers the Coupé et al. (2019) speech production rate of \~39 bits/sec at one Z-channel invocation per phoneme (\~4–6 phonemes per syllable × 5 Hz × ln(2) ≈ 21 bits/sec for 6 phonemes/syllable, within order-of-magnitude of the empirical 39 bits/sec; the residual factor is registered as NC-T7.14).

**Derivation chain (steps 1–3 unchanged from v1.0; steps 4–5 new in v1.1).**

**Step 1 \[LOCKED, ZB-P3 v1.0 \+ ZS-Q7 §4 Theorem 2\].** Under L\_XY ≡ 0 with dim(Z) \= 2, the X-Y channel capacity is bounded by ln(dim Z) \= ln(2) per Z-Spin mediator invocation.

**Step 2 \[LOCKED, ZB-V1 v1.0 \+ ZS-S15 v1.0 §D.5\].** Each 2π cycle on the Z-sector closes via four V\_XZ ↔ V\_ZY handshakes (SU(2)/SO(3) double-cover topology). The frequency f at which the Z-Spin mediator is invoked sets the rate of channel use at the neural scale.

**Step 3 \[DERIVED, this paper\].** Maximal lexical retrieval throughput Φ\_lang ≤ f · ln(2). Numerical values for f \= f\_α and f \= f\_θ are computed in Readings T7.2.A and T7.2.B above.

**Step 4 \[INSIGHT, NEW in v1.1: prima facie band assignment\].** The corpus's anti-numerology discipline (ZS-T2 v1.0; NC-T7.13) requires that the band of f be empirically anchored, not selected for numerical convenience. The external neuroscience literature on speech-language processing strongly supports theta (4–8 Hz) as the cortical syllable-tracking band: Giraud and Poeppel (2012) review; Doelling et al. (2014) on acoustic landmarks driving theta; Luo and Poeppel (2007) on phase patterns of theta tracking speech intelligibility; Hyafil et al. (2015) on theta-gamma coupling for syllabic-phonemic decoding. Alpha-band language phase-locking literature is substantially weaker. Reading T7.2.B (theta) is therefore registered as the prima facie more anchored reading in v1.1. Reading T7.2.A (alpha) is retained as a corpus-internal hypothesis from ZB-V1 visual-codec inheritance but does NOT carry independent empirical anchor strength in v1.1. P7 (§3) operationalizes the resolution.

**Step 5 \[INSIGHT, NEW in v1.1: relation to Coupé and Zheng-Meister\].** The numerical proximity of the alpha-band reading (6.93 bits/sec at f\_α \= 10 Hz) to the Zheng-Meister (2024) 10 bits/sec ceiling is honestly registered as suspicious from an anti-numerology perspective: matching at face value within 30% in a quantity that depends on a freely-chosen invocation frequency is consistent with selection bias. The Coupé et al. (2019) 39 bits/sec speech production rate is at a different layer (output channel rate, per syllable × syllables/sec) and the 39/10 ≈ 4 ratio is registered as a candidate match for ZS-T2 v2.0 anti-numerology Monte Carlo audit (NC-T7.14), explicitly NOT identified with the four-handshake-per-2π-cycle structure.

**Status.** Theorem T7.2 v1.1 is INSIGHT under disjunctive reading (T7.2.A OR T7.2.B). Empirical resolution between A and B is the operational content of P7 \+ F-T7.13. If P7 resolves PASS-θ, Reading T7.2.A is RETRACTED with audit trail in a future v1.2 amendment, and T7.2.B becomes the unique reading. If P7 resolves PASS-α, Reading T7.2.B is RETRACTED. If P7 resolves INDETERMINATE, both readings coexist as parallel hypotheses pending higher-resolution data.

## **§2.4 Theorem T7.3 — Lesion-Symptom Coupling Theorem \[DERIVED, NEW in v1.1\]**

**Statement.** Let G be a graph Laplacian admitting the Block Fiedler partition (P\_X, P\_Z, P\_Y) with L\_XY ≡ 0 (PROVEN, ZS-F1 v1.0 §9; ZS-S1 v1.0 §4; ZS-M6 v1.0 §7A all-orders) and Hardware Axiom H2 (all I/O through P\_Z; DERIVED, ZS-QH v1.0). Define the P\_Z-removal operator R\_Z that sets all rows and columns indexed by P\_Z to zero in G, leaving L\_XX (P\_X-internal couplings) and L\_YY (P\_Y-internal couplings) unchanged but eliminating the X-Z and Z-Y coupling blocks. Then under R\_Z:

**(i)** the X-internal spectrum σ(L\_XX) is preserved exactly (P\_X-internal processing intact);  
**(ii)** the Y-internal spectrum σ(L\_YY) is preserved exactly (P\_Y-internal processing intact);  
**(iii)** the effective X-Y channel capacity drops from ln(2) per invocation (intact case) to identically zero (R\_Z removes all paths between X and Y, since both direct and Z-mediated paths are eliminated; L\_XY ≡ 0 forbids direct paths a fortiori).

**Brain-substrate mapping (under Cardinal NC-4).** In the ZS-T7 partition assignment (P\_X \= phonological/articulatory cortex; P\_Z \= bilateral medial pulvinar; P\_Y \= semantic distributed cortex), Theorem T7.3 predicts the following triple dissociation in patients with lesions selectively affecting the medial pulvinar (or its primary white-matter projections via the AR-like \+ lateral pulvino-temporal tracts of Maldonado et al. 2024):

**(a)** preserved P\_X-internal processing → preserved single-word repetition (the phonological loop is intact within P\_X);  
**(b)** preserved P\_Y-internal processing → preserved single-word comprehension (semantic recognition is intact within P\_Y);  
**(c)** disrupted X-Y coupling → impaired confrontation naming (which requires phonology-semantics binding via the medial-pulvinar Z-channel).

**Empirical anchor.** Hillis et al. (2014, Frontiers in Neurology 5:231) reported that of ten patients with isolated left thalamic lesions, three exhibited isolated naming deficits with normal comprehension and normal repetition, all with normal cortical perfusion. Schaefer and Shariat (2022, Current Neurology and Neuroscience Reports) reviewed thalamic aphasia and reported that lesions to the pulvinar specifically result in fluent aphasia with naming deficits and semantic paraphasias while comprehension and repetition are mostly spared. Ojemann, Fedio, and Van Buren (1968, Brain 91:99–116) reported direct stimulation evidence: anomia from pulvinar and subcortical parietal stimulation. These three independent lines of evidence (lesion, large-cohort review, intraoperative stimulation) all match the (a) ∧ (b) ∧ (c) phenotype derived from Theorem T7.3.

**Derivation chain.**

**Step 1 \[LOCKED, ZS-F1 v1.0 §9; ZS-S1 v1.0 §4\].** L\_XY ≡ 0 directly from the Z-Spin scalar-tensor action (PROVEN). The 3-sector block Laplacian on Q \= 11 has identically zero X-Y block at the action level.

**Step 2 \[LOCKED, ZS-M6 v1.0 §7A Continuum Perturbative Protection Theorem\].** L\_XY^{eff,direct} \= 0 to all orders in perturbation theory via four independent protection layers: (i) Lorentz algebra decomposition \[su(2)\_A, su(2)\_B\] \= 0; (ii) action-level absence of direct X-Y couplings; (iii) Ward-Takahashi identity applied to su(2)\_A currents; (iv) anomaly-free verification. Status: PROVEN-PERTURBATIVE.

**Step 3 \[LOCKED, ZS-QH v1.0 Hardware Axiom H2\].** All inter-sector communication routes through P\_Z. Operationally: ‖H\_XY^par‖/‖H\_XZ‖ \< 1% by axiom; X↔Y direct path is parasitic and below the design threshold.

**Step 4 \[DERIVED, this paper\].** Define R\_Z as the projection that zeroes the P\_Z-indexed rows and columns of G. Under R\_Z: (a) σ(L\_XX) is preserved by construction (R\_Z acts as identity on the (P\_X, P\_X) block); (b) σ(L\_YY) is preserved similarly on the (P\_Y, P\_Y) block; (c) the effective X-Y resolvent (G^{-1})\_{XY} contains contributions only from paths that pass through P\_Z (since direct paths are forbidden by Step 1 \+ Step 2). Removal of P\_Z by R\_Z eliminates all such paths, so the effective X-Y coupling under R\_Z is zero exactly. Channel capacity drops from ln(2) per invocation (intact case, via the Stinespring construction of ZS-Q1 §3.3) to zero. □

**Brain-substrate translation under Cardinal NC-4.** The mathematical R\_Z corresponds, under the substrate-agnostic mapping of ZS-T7 v1.0 §2.2 (P\_X \= phonological cortex; P\_Z \= medial pulvinar; P\_Y \= semantic cortex), to a focal lesion of the medial pulvinar territory. The brain does not physically instantiate Z-Spin's Planck-scale geometry (Cardinal NC-4 from ZS-T4 v1.0); however, the partition-level Block Fiedler mathematics is the substrate-agnostic structural invariant that the human language network appears to share, per the ZB-N1 v3.0 verification of the global thalamic Z-mediator partition. The triple dissociation (a) ∧ (b) ∧ (c) is therefore a corpus-internal-derivation prediction operationalized as P8 in §3.

**Status.** Theorem T7.3 is DERIVED at the closed-form mathematical level (Step 4). Its empirical operationalization at the brain-substrate level is DERIVED-CONDITIONAL on the substrate-agnostic partition assignment of Theorem T7.1 (which is itself DERIVED-CONDITIONAL on P3 PASS) and on the validity of the L\_XY ≡ 0 architecture at the cortical scale (consistent with the ZB-N1 v3.0 VERIFIED result S\_XY ∈ \[0.058, 0.087\]). P8 (§3) is the pre-registered TESTABLE prediction.

## **§2.5 Theorem T7.4 — TOT as Coupling-Failure \[DERIVED-CONDITIONAL, NEW in v1.1\]**

**Statement.** The tip-of-the-tongue (TOT) phenomenon — the conscious experience of inability to retrieve a known word despite full availability of semantic content and partial availability of phonological features — is the phenomenological signature of partial Z-channel saturation under L\_XY ≡ 0 \+ ln(2) capacity bound. Specifically, TOT corresponds to a Z-Spin mediator regime in which the per-invocation X-Y handshake is below the saturation threshold but above the silence threshold, producing partial information transfer (consistent with TOT subjects' partial phonological access — e.g., first letter, syllable count, syllabic stress; Brown and McNeill 1966; Burke et al. 1991\) without completed retrieval (consistent with TOT subjects' inability to produce the full word).

**Derivation chain.**

**Step 1 \[LOCKED, ZS-Q7 §4 Theorem 2 \+ ZS-Q1 §3.3 Stinespring\].** The Z-channel admits a Kraus decomposition with pair {K\_0, K\_1}, dim(Z) \= 2\. The Holevo bound on classical-quantum channel capacity gives χ ≤ ln(2) nats per invocation under saturation. Under sub-saturation (K\_0 acting at fractional efficiency η \< 1), the effective capacity per invocation drops to η · ln(2).

**Step 2 \[DERIVED, this paper\].** In the language partition substrate (P\_X \= phonological; P\_Z \= medial pulvinar; P\_Y \= semantic), partial Z-channel saturation (η ∈ (0, 1)) corresponds to a phenomenological state in which: (i) P\_Y-internal access is intact (semantic content fully available — TOT subjects know what they want to say); (ii) P\_X-internal access is partially available (phonological skeleton — first letter, syllable count, syllabic stress — is retrievable from intra-X processing alone, since L\_XX is unaffected); (iii) full X-Y binding (the unique pairing of semantic content with full phonological string) requires saturation-level Z-channel capacity, which is unavailable.

**Step 3 \[DERIVED-CONDITIONAL, this paper\].** The transmission deficit hypothesis of Burke et al. (1991), which postulates that TOT arises from inadequate transmission of priming from activated lexical-semantic representations to phonological representations, is exactly the η \< 1 sub-saturation regime of Step 1 \+ Step 2 under the substrate-agnostic Z-channel architecture. Theorem T7.4 therefore unifies the corpus's L\_XY ≡ 0 \+ ln(2) capacity architecture with the established psycholinguistic transmission-deficit theory of TOT.

**Empirical signature (operationalized in P9).** In ERP/MEG recordings, the N400 component (peak \~400 ms; window 300–500 ms; Kutas and Federmeier 2011 review) indexes the integration step that combines lexical-semantic and phonological information. Under Theorem T7.4, chronic disruption of the Z-channel (as in pulvinar-lesion patients) should produce reduced N400 amplitude in the 300–500 ms window during picture-word matching tasks, while early auditory components (100–200 ms, intra-P\_X processing) and late positivity (500+ ms, post-lexical processing) remain within normal range. The acute-state TOT (induced TOT in healthy subjects via picture-name retrieval failures) should produce intermediate N400 amplitude reduction, scaling with η, consistent with sub-saturation rather than full silence.

**Status.** Theorem T7.4 is DERIVED-CONDITIONAL on (i) the substrate-agnostic partition assignment of Theorem T7.1, and (ii) the identification of the η \< 1 sub-saturation regime with the Burke et al. (1991) transmission deficit. Both conditions are explicit. P9 (§3) is the pre-registered TESTABLE prediction.

## **§2.6 Theorem T7.5 — Theta-Pulvinar PLV Specificity \[INSIGHT, NEW in v1.1, conditional on F-T7.13/P7 PASS-θ\]**

**Statement.** Conditional on F-T7.13/P7 resolving PASS-θ (i.e., theta-band 4–8 Hz dominance over alpha-band 8–13 Hz in peri-medial-pulvinar phase-locking during lexical retrieval; see §3 P7), the diagnostic signature of medial-pulvinar Z-Spin-mediator dysfunction is selective theta-band power and phase-locking value (PLV) reduction in the left peri-temporal cortex during lexical retrieval tasks, with alpha-band power preserved within normal range.

**Derivation chain.**

**Step 1 \[conditional on P7 PASS-θ, by hypothesis\].** If theta is the dominant peri-pulvinar coupling band during lexical retrieval, then the Z-Spin mediator is invoked at the theta rhythm during lexical retrieval; alpha-band activity in this context reflects parallel non-language-mediator processing.

**Step 2 \[DERIVED from Theorem T7.3 \+ Step 1\].** Theorem T7.3 establishes that R\_Z (medial pulvinar removal) eliminates the Z-mediated X-Y channel. Under P7 PASS-θ \+ Step 1, this corresponds operationally to selective elimination of the theta-band peri-temporal phase-locking signature, since the theta rhythm carries the Z-channel invocation. Alpha-band activity in the same cortex reflects unrelated parallel processing and remains unaffected by R\_Z (no Z-mediator involvement assumed in alpha at the language partition).

**Step 3 \[INSIGHT, this paper\].** The diagnostic signature is therefore: in pulvinar-lesion patients, theta-band power in left peri-temporal cortex during picture naming should be reduced by ≥ 40% relative to age-matched controls, while alpha-band power should remain within normal range (defined as within 1 SD of control mean). This is a band-selective reduction signature, distinguishing pulvinar-Z-channel disruption from generalized thalamic hypofunction (which would reduce both bands).

**Status.** Theorem T7.5 is INSIGHT, conditional on F-T7.13/P7 PASS-θ. If P7 resolves PASS-α, Theorem T7.5 is replaced with an alpha-band analogue (with substantially weaker external literature anchor); if P7 resolves INDETERMINATE, Theorem T7.5 carries dual-band reading. P10 (§3) is the pre-registered TESTABLE prediction operationalizing the theta-band signature.

## **§2.7 Cross-paper consistency**

ZS-T7 v1.1 connects to the Z-Spin and Z-Brain corpus through ten established LOCKED inputs and adds three new theorems (T7.3, T7.4, T7.5). All cross-references trace upward to PROVEN, PROVEN-PERTURBATIVE, or VERIFIED layer-1/2 results.

*Table 3\. Cross-paper input table for ZS-T7 v1.1. All inputs are at PROVEN, PROVEN-PERTURBATIVE, VERIFIED, DERIVED, or DERIVED-CONDITIONAL status in their source paper. The Layer column refers to the corpus dependency hierarchy. NEW in v1.1 entries are required for Theorems T7.3, T7.4, T7.5.*

| Input | Layer | Used here as |
| ----- | ----- | ----- |
| ZS-T1 v1.0 §9.3 Block Fiedler Mediation Theorem | Layer 1 (PROVEN) | Theorem T7.1 derivation Step 1 anchor; ψ\_2|\_Z \= 0 ideal target |
| ZS-Q7 v1.0 §4 Theorem 2 channel capacity | Layer 1 (DERIVED) | Theorem T7.2 ln(2) bound; Theorem T7.4 sub-saturation η · ln(2) |
| ZS-F5 v1.0 §4 dim(Z) \= 2 Frobenius result | Layer 1 (PROVEN) | Cardinality |P\_Z^lang| \= 2 forced by polyhedral gauge constraint |
| ZS-Q1 v1.0 §3.3 Theorem 3.2 Stinespring/Kraus | Layer 1 (PROVEN) | dim(Z) \= 2 Kraus pair {K\_0, K\_1} → Holevo bound input; Theorem T7.4 partial-saturation parametrization |
| ZS-F1 v1.0 §9 \+ ZS-S1 v1.0 §4 L\_XY ≡ 0 from action \[NEW in v1.1\] | Layer 1 (PROVEN) | Theorem T7.3 derivation Step 1 — direct X-Y coupling forbidden at action level |
| ZS-M6 v1.0 §7A all-orders protection \[NEW in v1.1\] | Layer 1 (PROVEN-PERTURBATIVE) | Theorem T7.3 derivation Step 2 — protection extends to all perturbative orders |
| ZS-QH v1.0 Hardware Axiom H2 (all I/O through Z) \[NEW in v1.1\] | Layer 1 (DERIVED) | Theorem T7.3 derivation Step 3 — operational form of L\_XY ≡ 0 at engineering level |
| ZB-N1 v3.0 thalamus mediator \[VERIFIED on HCP\] | Layer 2 (VERIFIED) | Multi-resolution methodology \+ threshold inheritance \+ AN3 anti-numerology design template |
| ZB-V1 v1.0 §24.4 scenario γ | Layer 2 (DERIVED-CONDITIONAL) | Nested Z-Spin mediator scaffold; sub-nucleus differentiation principle; Reading T7.2.A alpha-inheritance |
| ZB-P3 v1.0 ln(2) channel-capacity bound | Layer 2 (DERIVED-CONDITIONAL) | Theorem T7.2 INSIGHT derivation |
| ZS-T4 v1.0 Cardinal NC-4 inheritance | Layer 1 (LOCKED) | NC-T7.1 inheritance — no physical realization claim |
| ZS-T5 v1.0 ZB→ZS conversion protocol | Methodological precedent | v1.0 → v1.1 amendment under same audit-and-retract discipline |
| ZB-P2 v1.0 NC-P2.2 Variable Binding exclusion | LOCKED | NC-T7.5 inheritance — pulvinar-mediated lexical retrieval ≠ universal binding solution |

# **§3. Pre-registered Predictions**

## **§3.1 Three-level prediction structure**

ZS-T7 v1.1 advances ten pre-registered TESTABLE predictions across three empirical levels. Connectome-level predictions (P1–P6) are inherited unchanged from v1.0 and address the structural Block Fiedler partition geometry on HCP-YA. Oscillatory-level prediction (P7) operationalizes the v1.0 F-T7.13 alpha-vs-theta gate into a TESTABLE prediction on Cam-CAN MEG. Lesion-symptom-level predictions (P8, P9, P10) are NEW in v1.1 and derive from Theorems T7.3, T7.4, T7.5 respectively. Each prediction has a pre-registered threshold, decision rule, and corresponding falsification gate.

*Table 4\. Ten pre-registered TESTABLE predictions for ZS-T7 v1.1. Each prediction has a corresponding falsification gate F-T7.4 through F-T7.16 (§7). Decision rules are LOCKED at v1.1 release; post-hoc adjustment is not permitted.*

| Pred | Quantity | Threshold / Decision rule | Data source | Theorem / Gate |
| ----- | ----- | ----- | ----- | ----- |
| P1 | S\_XY^lang on HCP SC | ≤ 0.10 in 5/6 parcellations | HCP-YA SC (n ≈ 207\) | T7.1 / F-T7.4 |
| P2 | F\_Z^lang on HCP SC and FC | ≤ 0.30 in 5/6 parcellations | HCP-YA SC \+ FC | T7.1 / F-T7.5 |
| P3 | Medial pulvinar AN3 mean rank | ≤ 3.0; Fisher p \< 10⁻⁴ | 24 metric-parcellation combos | T7.1 / F-T7.6 |
| P4 | Mean rank gap (lat − med pulvinar) | ≥ 1.0 (sub-nucleus differentiation) | AN3 across 24 combos | T7.1 / F-T7.7 |
| P5 | Lateralization (left vs bilateral P\_X) | L-only 5/6 PASS; bilateral 6/6 PASS | HCP-YA SC | T7.1 / F-T7.8 |
| P6 | Maldonado anomia tract correlation | AR-like \+ lateral preferred | Maldonado 2024 cohort | T7.1 / F-T7.9 |
| P7 \[NEW v1.1\] | Theta vs alpha peri-pulvinar PLV during lexical retrieval | PASS-θ if θ-PLV − α-PLV ≥ 0.10 in ≥ 80% of subjects; PASS-α if reverse; INDETERMINATE if neither; FAIL if both PLV \< 0.30 | Cam-CAN MEG (n ≈ 600\) | T7.2 \+ T7.5 / F-T7.13 |
| P8 \[NEW v1.1\] | Pulvinar-lesion triple dissociation: preserved comprehension AND preserved repetition AND impaired confrontation naming | Effect size d ≥ 0.8 for naming deficit; d ≤ 0.3 for comprehension and repetition deficits, vs matched ATL-lesion and SMG/IFG-lesion controls | Thalamic stroke cohort (e.g., Hillis et al. 2014 type; n ≥ 20 isolated thalamic lesion patients) | T7.3 / F-T7.14 |
| P9 \[NEW v1.1\] | N400 amplitude (300–500 ms window) reduction in pulvinar-lesion patients during picture-word matching | Reduction ≥ 50% vs matched controls; early auditory components (100–200 ms) and late positivity (500+ ms) within 1 SD of control mean | ERP/MEG with thalamic stroke cohort (e.g., MIRACLE-LESION extension; or retrospective Cam-CAN-of-stroke pooling) | T7.4 / F-T7.15 |
| P10 \[NEW v1.1, conditional on P7 PASS-θ\] | Theta-band power and PLV reduction in left peri-temporal cortex during picture naming | Theta power reduction ≥ 40% in pulvinar-lesion patients vs matched controls; alpha power within 1 SD of control mean | MEG with thalamic stroke cohort | T7.5 / F-T7.16 |

## **§3.2 Hierarchy of empirical evidence and decision rules**

The ten predictions are stratified by their decisional weight on the framework. P1, P2, P3 are the keystone predictions of Theorem T7.1: their conjunction PASS upgrades T7.1 from DERIVED-CONDITIONAL to DERIVED-strong. P4 is the sub-nucleus differentiation gate (medial vs lateral pulvinar specificity); P4 FAIL weakens Theorem T7.1 to whole-pulvinar level (NC-T7.9). P5 is the lateralization sensitivity check; P5 outcome OBSERVATION-level only. P6 is the Maldonado-cohort correlation, INSIGHT-level.

P7 is the alpha-vs-theta empirical resolution. P7 PASS-θ (theta dominant) is the most likely outcome on the prima facie literature (NC-T7.13 v1.1) and would: (i) upgrade Theorem T7.5 from INSIGHT-conditional to INSIGHT; (ii) RETRACT Reading T7.2.A (alpha-band) leaving Reading T7.2.B as the unique form of Theorem T7.2; (iii) make P10 active. P7 PASS-α would: (i) preserve Reading T7.2.A; (ii) RETRACT Reading T7.2.B; (iii) replace Theorem T7.5 with an alpha-band analogue. P7 INDETERMINATE preserves both readings and registers Theorem T7.2 with dual-band uncertainty pending higher-resolution data.

P8 is the keystone prediction of Theorem T7.3 (Lesion-Symptom Coupling). P8 PASS upgrades T7.3 from DERIVED-CONDITIONAL (on substrate-agnostic partition validity) to VERIFIED at the brain-substrate level. P8 FAIL refutes the substrate-agnostic partition assignment of P\_Z \= medial pulvinar at the lesion-deficit operationalization level (the Block Fiedler mathematics still holds; only the brain mapping is refuted). P8 outcome therefore decisively determines whether ZS-T7 v1.1 advances the corpus's clinical translational reach.

P9 (N400 attenuation) is the keystone prediction of Theorem T7.4 (TOT). P9 PASS demonstrates that the corpus's L\_XY ≡ 0 \+ ln(2) capacity architecture predicts the observed ERP signature of language integration disruption. P9 FAIL would refute the Theorem T7.4 identification of TOT with sub-saturation η \< 1 regime (and the corresponding identification of N400 with the X-Y integration step).

P10 is the keystone prediction of Theorem T7.5 (Theta-Pulvinar PLV Specificity). P10 is active only conditional on P7 PASS-θ; if P7 resolves PASS-α or INDETERMINATE, P10 is replaced with band-appropriate variants in a future v1.2 amendment.

## **§3.3 Prediction execution targets**

Predictions P1–P6 (connectome) are scheduled for execution at v1.2 with HCP-YA \+ ENIGMA Toolbox v2.0; v1.2 release target 2026 Q4. P7 (alpha-vs-theta MEG resolution) requires Cam-CAN MEG access; v1.2 release target 2026 Q4 conditional on data access. P8 (lesion triple dissociation) requires curated thalamic stroke cohort data; existing published cohorts (Hillis et al. 2014, n \= 10 isolated thalamic lesion; MIRACLE-LESION; Stroke MR-CLEAN registries) provide the foundation, and a meta-analysis sufficient for P8 evaluation is achievable from public-domain published data without new patient recruitment. P9 (N400 attenuation) requires ERP/MEG data on thalamic stroke patients during picture-word matching; this is a standard clinical paradigm and existing or planned cohorts (e.g., Cogitate consortium 2025+ release; MIRACLE-LESION) are anticipated to be sufficient. P10 (theta-pulvinar PLV) requires the same MEG data with cohort filtering on lesion location; the resolution of P7 determines whether this prediction is active or replaced.

The v1.1 release therefore registers ten TESTABLE predictions with explicit data sources and decision rules; v1.2 closes the connectome and oscillatory predictions (P1–P7); v1.3 closes the lesion-symptom predictions (P8–P10) pending cohort data access. The pillar-paper-launch pattern of v1.0 is preserved at the v1.1 release; the v1.2 and v1.3 amendments will report empirical determinations under the ZS-T5 retraction-or-confirmation discipline.

# **§4. Methods**

## **§4.1 Partition definition (unchanged from v1.0)**

**P\_X^lang.** Glasser-360 labels: L\_44, L\_45, L\_55b, L\_6v, L\_TA2, L\_A1, L\_PSL. |P\_X^lang| ≈ 8 left-hemisphere parcels at v1.0; right-hemisphere homotopic addition reserved for v1.1 sensitivity test.

**P\_Z^lang.** Bilateral medial pulvinar (PuM) from FreeSurfer subcortical segmentation supplemented with the Najdenovska et al. (2018) atlas at p \> 0.5 threshold. |P\_Z^lang| \= 2\.

**P\_Y^lang.** Glasser-360 labels: L/R\_TGd, L/R\_TGv, L/R\_TE1a, L/R\_TE1m, L/R\_TE1p, L/R\_PGi, L/R\_PGs, L/R\_STSva, L/R\_STSvp, L/R\_STSdp, L/R\_47l, L/R\_47s. |P\_Y^lang| ≈ 30–40.

**Block Fiedler non-degenerate condition.** c ≤ a \+ b where c \= 2, a ≈ 8, b ≈ 35\. The condition 2 ≤ 8 \+ 35 \= 43 is satisfied with wide margin.

## **§4.2 Connectome metrics (P1–P6)**

S\_XY \= ‖L\_XY‖\_F / max(‖L\_XZ‖\_F, ‖L\_ZY‖\_F); F\_Z \= |⟨ψ\_2, 1\_Z⟩| / max(|⟨ψ\_2, 1\_X⟩|, |⟨ψ\_2, 1\_Y⟩|). Pre-registered thresholds inherited from ZB-N1 v3.0: S\_XY \< 0.10, F\_Z \< 0.30. AN3 anti-numerology test against eight alternative thalamic mediator candidates (medial pulvinar, lateral pulvinar, anterior pulvinar, inferior pulvinar, MD, CM-Pf, VL, hippocampus); 24 metric-parcellation combinations; rank ranking; Fisher combined p-value.

## **§4.3 Oscillatory metrics (P7) — NEW in v1.1**

Cam-CAN MEG dataset (Shafto et al. 2014 cohort description; n ≈ 600 subjects across age range 18–88) supplies the oscillatory data for P7. Source localization: medial pulvinar voxel via Najdenovska et al. (2018) atlas; left peri-temporal cortex (Glasser-360 L\_TA2, L\_A1, L\_PSL, L\_TGd, L\_TGv) as cortical reference. Phase-locking value (PLV) computed pairwise between medial-pulvinar voxel and left-peri-temporal cortical regions in two frequency bands: theta (4–8 Hz) and alpha (8–13 Hz). Task: word-picture matching paradigm (existing Cam-CAN paradigms include word/picture associations; sub-task selection LOCKED at v1.1 release). Decision rule LOCKED in P7.

## **§4.4 Lesion-symptom metrics (P8) — NEW in v1.1**

Three patient groups, matched on age, education, time post-stroke, and overall lesion volume: (i) isolated thalamic lesion with medial pulvinar involvement (n ≥ 20); (ii) ATL-lesion control (n ≥ 20); (iii) SMG/IFG-lesion control (n ≥ 20). Three behavioral assessments: (a) single-word comprehension via the Comprehensive Aphasia Test (CAT, Swinburn et al. 2004); (b) single-word repetition via the Psycholinguistic Assessments of Language Processing in Aphasia (PALPA); (c) confrontation naming via the Boston Naming Test (BNT) or Philadelphia Naming Test (PNT). Effect sizes (Cohen's d) computed between thalamic-lesion group and each cortical-lesion control group on each assessment. P8 decision rule LOCKED.

## **§4.5 ERP / MEG metrics (P9) — NEW in v1.1**

Same patient and control groups as P8. ERP recording during picture-word matching paradigm: 64-channel EEG, 500 Hz sampling, 100 ms pre-stimulus baseline, 1000 ms post-stimulus epoch, average referenced. Three time windows analyzed: (i) early auditory (100–200 ms post auditory word onset); (ii) N400 (300–500 ms); (iii) late positivity (500–800 ms). Amplitude measured as mean voltage in window at central-parietal scalp sites (Cz, CPz, Pz, where N400 is maximal per Kutas and Federmeier 2011). Reduction ratio \= (control mean − patient mean) / control mean. P9 decision rule LOCKED.

## **§4.6 Theta-PLV specificity (P10) — NEW in v1.1, active conditional on P7 PASS-θ**

Same MEG paradigm as P7 with patient-control filtering. Theta-band power \= mean source-localized power 4–8 Hz in left peri-temporal cortex (Glasser-360 L\_TA2, L\_A1, L\_PSL) during 200–600 ms post-stimulus window (covering N400 epoch). Alpha-band power \= same metric for 8–13 Hz. Reduction ratio computed per band as in P9. P10 decision rule LOCKED conditional on P7 outcome; v1.2 amendment will replace P10 with band-appropriate variant if P7 resolves PASS-α or INDETERMINATE.

## **§4.7 Reproducibility**

Verification artifact zs-t7\_verify.py upgraded from v1.0 (24 closed-form \+ in-silico gates, 24/24 PASS) to v1.1 (27 gates, 27/27 PASS). Three new gates G-F.1, G-F.2, G-F.3 cover Theorem T7.3 closed-form structure: G-F.1 verifies that R\_Z preserves σ(L\_XX) on synthetic block Laplacian; G-F.2 verifies that R\_Z preserves σ(L\_YY); G-F.3 verifies that R\_Z eliminates the X-Y resolvent (G^{-1})\_{XY}. The 24 v1.0 gates are inherited bit-identical (sub-pipeline structure unchanged; only file name \+ series identifier \+ new gates F appended). All operations deterministic (seed \= 42; numpy ≥ 1.22, scipy ≥ 1.8). Empirical execution on HCP-YA, Cam-CAN, and stroke cohorts deferred to v1.2 / v1.3 amendments. SHA-256 pre-registration hash committed at v1.1 release.

# **§5. Results**

## **§5.1 Closed-form and in-silico gates**

All 27 closed-form and in-silico gates of zs-t7\_verify\_v1\_1.py PASS at machine precision or theoretical-bound tolerance. The 24 v1.0 gates are inherited bit-identical; three new gates G-F.1, G-F.2, G-F.3 cover Theorem T7.3.

*Table 5\. Verification status for ZS-T7 v1.1: 27/27 closed-form \+ in-silico gates PASS in zs-t7\_verify\_v1\_1.py. The five v1.0 gate groups (A–E) are inherited bit-identical; one new gate group F covers the new Theorem T7.3 (Lesion-Symptom Coupling) closed-form structure with three tests.*

| Gate group | Tests | PASS | Status | Note |
| ----- | ----- | ----- | ----- | ----- |
| GATE A: LOCKED inputs sanity | 5 | 5 | PASS 5/5 | v1.0 inherited |
| GATE B: BFMT closed-form on synthetic L | 6 | 6 | PASS 6/6 | v1.0 inherited |
| GATE C: AN3 design validation | 4 | 4 | PASS 4/4 | v1.0 inherited |
| GATE D: Cross-paper consistency | 5 | 5 | PASS 5/5 | v1.0 inherited |
| GATE E: External anchor consistency | 4 | 4 | PASS 4/4 | v1.0 inherited |
| GATE F: T7.3 closed-form (NEW v1.1) | 3 | 3 | PASS 3/3 | G-F.1, G-F.2, G-F.3 |
| **Total** | **27** | **27** | **PASS 27/27 (100.0%)** |  |

Highlights from v1.0 gates retained: (G-B.2) synthetic L\_XY block achieves Frobenius norm 0 to machine precision; (G-B.3) synthetic Fiedler neutrality F\_Z achieves the F\_Z \< 0.30 threshold by theorem; (G-B.4) ln(2) channel capacity bound \= 0.693147 nats per invocation matches Theorem T7.2 INSIGHT; (G-D.2) ZB-V1 §24.4 scenario γ inheritance verified; (G-E.3) MGN→auditory tract count 1–2 (Maffei et al. 2019\) PASS, supporting NC-T7.2.

New v1.1 gates highlights: (G-F.1) on synthetic 11×11 block Laplacian with (a, c, b) \= (8, 2, 35), the projection R\_Z preserves σ(L\_XX) \= (8 eigenvalues) bit-identical to the X-only sub-block diagonalization. (G-F.2) R\_Z preserves σ(L\_YY) \= (35 eigenvalues) bit-identical to the Y-only sub-block diagonalization. (G-F.3) The (X, Y) block of (G\_R)^{-1} where G\_R \= R\_Z(G) has Frobenius norm \< 10⁻¹⁵, confirming that R\_Z eliminates the X-Y resolvent at machine precision. These three gates jointly verify Theorem T7.3 closed-form derivation Step 4\.

## **§5.2 Predictions inventory**

Ten TESTABLE predictions registered: P1–P6 inherited from v1.0 (connectome on HCP-YA, awaiting v1.2 execution); P7 NEW in v1.1 (alpha-vs-theta on Cam-CAN MEG, awaiting v1.2 execution); P8, P9, P10 NEW in v1.1 (lesion-symptom and ERP/MEG on stroke cohorts, awaiting v1.3 execution). All predictions are at TESTABLE-PENDING status in v1.1 v1.0+v1.1 release.

## **§5.3 Verification status summary**

Closed-form \+ in-silico gates: 27/27 PASS (100.0%, up from 24/24 in v1.0). TESTABLE-PENDING: 10 predictions (up from 6 in v1.0; P7 formalized from v1.0 F-T7.13 gate; P8, P9, P10 NEW). Chain dependencies: 13/13 PROVEN-LOCKED (10 from v1.0: ZS-T1, ZS-Q7, ZS-F5, ZS-Q1, ZS-T4, ZS-T5, ZB-N1, ZB-V1, ZB-P2, ZB-P3; 3 NEW in v1.1: ZS-F1+ZS-S1 L\_XY ≡ 0, ZS-M6 §7A all-orders protection, ZS-QH Hardware Axiom H2). Free parameters introduced: 0\.

This verification status preserves the pillar-paper-launch epistemic structure of v1.0 while extending the empirical reach into three additional levels (oscillatory, lesion-symptom, ERP). The framework's commitment is now substantially broader: ten predictions across three levels jointly determine the empirical fate of the ZS-T7 framework, and three new theorems (T7.3, T7.4, T7.5) are derived from corpus-PROVEN inputs without introducing new free parameters.

# **§6. Discussion**

## **§6.1 Mechanistic interpretation across three levels**

ZS-T7 v1.1 advances the framework from a single-level (connectome) prediction in v1.0 to a three-level prediction in v1.1: connectome geometry (P1–P6, Theorem T7.1), oscillatory dynamics (P7, Theorems T7.2/T7.5), and lesion-symptom mapping (P8–P10, Theorems T7.3/T7.4). The unifying mechanism across the three levels is the L\_XY ≡ 0 \+ ln(2) capacity architecture: at the geometric level it predicts the Block Fiedler partition; at the dynamical level it predicts the rate-bounded throughput Φ\_lang ≤ f · ln(2); at the lesion level it predicts that R\_Z (Z-removal) selectively breaks X-Y coupling while leaving X-internal and Y-internal processing intact.

This three-level coherence is the framework's strongest commitment. If the connectome partition holds (P1–P3 PASS) but the lesion triple-dissociation fails (P8 FAIL), the corpus's substrate-agnostic mathematics is preserved but its brain-substrate operationalization is refuted; this would represent a substantial RETRACTION of Theorem T7.3's brain-mapping clause. If the lesion triple-dissociation holds (P8 PASS) but the connectome partition fails (P1–P3 FAIL), the geometric assignment of P\_Z \= medial pulvinar at the connectome level is refuted, but the lesion-deficit prediction may still hold via a different anatomical assignment of Z; this would represent OPEN status pending atlas-extended testing. The conjunction of P1–P3 PASS AND P8 PASS upgrades Theorem T7.1 to DERIVED-strong and Theorem T7.3 to VERIFIED.

## **§6.2 Comparison to Hickok-Poeppel and Fedorenko frameworks (puzzle 1\)**

The Hickok-Poeppel (2007) dual-stream model identifies dorsal and ventral cortico-cortical pathways for phonology and semantics. ZS-T7 v1.1 is COMPATIBLE with this model and adds a thalamic Z-Spin mediator: dorsal and ventral streams both terminate at (or pass through) pulvinar gating before unified lexical retrieval. This is not a competing model but a structural completion: the dual-stream architecture explains parallel specialized processing; the Z-Spin mediator architecture explains integration into unified output and (in v1.1) the lesion-deficit triple dissociation that the cortico-cortical-only model leaves under-explained. Specifically, the cortico-cortical-only model has difficulty accounting for the Hillis et al. (2014) finding of three patients with isolated naming deficits with normal comprehension and repetition AND normal cortical perfusion: under cortico-cortical-only architecture, intact cortex implies intact integration, contradicting the observed naming deficit. ZS-T7 v1.1 Theorem T7.3 resolves this by predicting that the integration step is mediator-dependent and lesion of P\_Z disrupts integration even with intact cortical endpoints.

The Fedorenko, Ivanova, and Regev (2024) language network "natural kind" thesis identifies functional selectivity of language-network cortex for syntactic processing distinct from arithmetic, music, executive function, and theory of mind. ZS-T7 v1.1 is COMPATIBLE with this thesis but does not derive it. NC-T7.11 explicitly states that ZS-T7 cannot derive Fedorenko's natural-kind selectivity from Z-Spin axioms; the partition framework provides necessary structural conditions for unified retrieval, not sufficient conditions for domain-specific selectivity.

## **§6.3 Thalamic aphasia and the lesion-deficit literature (puzzle 2\)**

The thalamic aphasia literature (Crosson 1985; Schaefer and Shariat 2022; Hillis et al. 2014; Ojemann, Fedio, and Van Buren 1968; Bruzzone Giraldez et al. 2015\) consistently reports that pulvinar-territory lesions produce fluent aphasia with naming deficits while comprehension and repetition are mostly spared. The mechanism has remained debated. Schaefer and Shariat (2022) note that "the exact mechanisms of thalamic aphasia await empirical research" and propose that the thalamus's role is via cortico-thalamic language network involvement — a description, not a derivation. ZS-T7 v1.1 Theorem T7.3 supplies the derivation from the corpus-PROVEN L\_XY ≡ 0 architecture: the Z-Spin mediator is exactly the kind of structure whose removal preserves X-internal and Y-internal processing while breaking X-Y coupling, which is the operational definition of the observed clinical phenotype.

The framework also makes a sharper prediction than the existing literature provides. Existing studies typically report that pulvinar-lesion patients have "naming deficits with preserved comprehension"; the comparison to repetition is often not separately reported. ZS-T7 v1.1 P8 explicitly requires preserved repetition AND preserved comprehension AND impaired naming as a triple dissociation, and the triple dissociation is the specific signature that would distinguish a Z-mediator lesion from a cortical-cortical disconnection (which would impair repetition as well, since repetition crosses the dorsal phonological stream). Schaefer and Shariat (2022) note a phenotype distinction between pulvinar lesions (fluent, semantic paraphasias, naming deficits) and anterior thalamic nuclei lesions (non-fluent, more severe); P8's triple dissociation predicts that pulvinar-lesion patients should specifically show the (a) ∧ (b) ∧ (c) pattern with effect size d ≥ 0.8 for naming and d ≤ 0.3 for the other two. This is a strong, falsifiable prediction.

## **§6.4 Lexical retrieval throughput, theta rhythm, and Coupé-Zheng-Meister (puzzle 3\)**

Theorem T7.2 v1.1 advances over v1.0 by explicitly registering Reading T7.2.B (theta band) as the prima facie more empirically anchored reading. The cortical syllable-tracking literature (Giraud and Poeppel 2012; Doelling et al. 2014; Luo and Poeppel 2007; Hyafil et al. 2015\) is substantially stronger than any alpha-language phase-locking literature; the alpha \= 10 Hz inheritance from ZB-V1's visual codec is a corpus-internal hypothesis not anchored on independent language-relevant evidence. The honest registration of this asymmetry in NC-T7.13 v1.1 strengthens the framework's anti-numerology discipline. P7 operationalizes empirical resolution on Cam-CAN MEG.

The Coupé et al. (2019) \~39 bits/sec speech production rate and the Zheng-Meister (2024) \~10 bits/sec conscious throughput ratio (≈ 4\) is honestly registered in NC-T7.14 as an anti-numerology candidate match, NOT as a structural claim. The two measurements are at different layers: Coupé measures speech production rate (output channel; per-syllable information density × syllables/second); Zheng-Meister measures conscious behavioral throughput across all task modalities (general bottleneck). The numerical proximity 39/10 ≈ 4 is registered for ZS-T2 v2.0 anti-numerology Monte Carlo audit (5670 × 29 candidate scan, look-elsewhere correction); pending audit, no structural claim is made.

## **§6.5 Tip-of-the-tongue and the N400 ERP signature (puzzle 4\)**

Theorem T7.4 v1.1 identifies TOT as the phenomenological signature of partial Z-channel saturation under L\_XY ≡ 0 \+ ln(2). The transmission deficit hypothesis of Burke et al. (1991) — that TOT arises from inadequate transmission of priming from semantic to phonological representations — is structurally identical to the η \< 1 sub-saturation regime in the Z-channel architecture: P\_Y is intact (semantic content available), P\_X is partially accessible (skeleton phonology — first letter, syllable count — accessible from intra-X processing alone), and full X-Y binding (unique semantic-phonological pairing) requires saturation-level Z-channel capacity that is unavailable.

The N400 ERP signature (Kutas and Federmeier 2011 review) provides the empirical operationalization. The N400, peaking at \~400 ms post-stimulus and indexing semantic integration, is exactly the signature that the X-Y integration step would generate under the Z-channel architecture. P9 predicts that pulvinar-lesion patients (chronic Z-channel disruption) should show N400 amplitude reduction ≥ 50% in the 300–500 ms window during picture-word matching, while intact early auditory components (100–200 ms, intra-P\_X processing) and intact late positivity (500+ ms, post-lexical processing) demonstrate that the disruption is selective to the integration step — a signature that the cortico-cortical-only models cannot easily predict.

## **§6.6 Three-level fractal Z-Spin mediator nesting (Path E)**

ZS-T7 v1.1 contributes Route 5 of the multi-partition Z-Spin mediator over-determination map (unchanged from v1.0). Path E (S\_XY/F\_Z scale invariance: same threshold S\_XY ≤ 0.10, F\_Z ≤ 0.30 at every partition level across HCP) is a programme-level claim whose verification is the ZB-X2 (Corpus Preface) responsibility (NC-T7.3, NC-M23.1 style). The v1.1 amendment does not change Route 5's status; what is new in v1.1 is the addition of three new theorems and four new predictions that operationalize Route 5 at three levels (connectome, oscillatory, lesion) rather than connectome-only.

## **§6.7 Practitioner's diagnostic — language codec failure modes (revised in v1.1)**

The Z-Spin mediator architecture motivates a diagnostic taxonomy of language pathologies. (a) P\_X^lang failure: phonological/articulatory disruption (e.g., pure word deafness, Broca's aphasia). (b) P\_Y^lang failure: semantic distributed disruption (e.g., semantic dementia, transcortical sensory aphasia). (c) P\_Z^lang (medial pulvinar) failure: lexical-retrieval mediator disruption (e.g., pulvinar lesion anomia per Hillis et al. 2014; thalamic aphasia per Crosson 1985). (d) Channel-bandwidth disruption: invocation-frequency anomalies (NEW v1.1 reading: theta-band specifically, conditional on P7 PASS-θ; possibly relevant in dementia sub-types where theta power is altered).

v1.1 advances this taxonomy from INSIGHT-only (in v1.0) to TESTABLE-with-falsification-gates: P8 operationalizes (c); P9 \+ P10 add the ERP/MEG signature of (c) and (d). Disease-specific perturbation predictions are no longer NON-CLAIM in v1.1 (NC-T7.8 amended); only treatment-pharmacological predictions remain at NON-CLAIM status (e.g., predicting that levodopa or thalamic DBS selectively rescues phonology-semantics coupling without rescuing cortical phonological or semantic deficits is a potential future v1.2 prediction but is not registered at v1.1 release).

## **§6.8 Limitations**

Six substantive limitations are acknowledged in v1.1 (five from v1.0 \+ one new). (i) Sub-nucleus resolution at the medial-vs-lateral pulvinar level relies on the Najdenovska et al. (2018) atlas at \~2 mm resolution; F-T7.7 weakening conditional. (ii) HCP-YA cohort age range 22–37 years; cross-cohort replication via Cam-CAN and UK Biobank required. (iii) Schaefer atlas language-functional tag absence requires Glasser-360 mask projection. (iv) No single-subject test in v1.0 v1.1; v1.2 amendment reserved for per-subject sensitivity. (v) Variable Binding excluded from framework reach (NC-T7.5).

(vi) \[NEW in v1.1\] The lesion-deficit predictions (P8, P9, P10) rely on cohort access to thalamic stroke patients with ERP/MEG paradigms; this access is currently project-dependent and is the rate-limiting step for v1.3 closure. Alternative analyses on existing public-domain published cohorts (e.g., the Hillis et al. 2014 cohort, the MIRACLE-LESION dataset if accessible) provide partial verification but are not sufficient for full P8-P10 closure. The v1.1 release acknowledges this limitation and explicitly schedules v1.3 for cohort-data-dependent execution.

# **§7. Falsification Gates**

Sixteen falsification gates F-T7.1 through F-T7.16 are registered at four levels. Each gate has a pre-registered threshold; post-hoc reinterpretation is not permitted. Twelve gates F-T7.1 through F-T7.12 are inherited unchanged from v1.0 (which itself inherited F-C5.1 through F-C5.12 from ZB-C5 v1.0). F-T7.13 was new in v1.0 (alpha-vs-theta) and is preserved unchanged in v1.1, now formalized into TESTABLE prediction P7. Three new gates F-T7.14, F-T7.15, F-T7.16 are introduced in v1.1 corresponding to the new lesion-symptom predictions P8, P9, P10 respectively.

## **§7.1 Level 1 — Mathematical (theorem-level)**

**F-T7.1:** If ZS-T1 v1.0 §9.3 Block Fiedler Mediation Theorem is shown to have a mathematical error, ZS-T7 is withdrawn. Current status: PASS (theorem PROVEN).

**F-T7.2:** If ZB-N1 v3.0 LOCKED inputs are revised in v3.1+, ZS-T7 inherits the consistency check. Current status: PASS.

## **§7.2 Level 2 — Simulation / in-silico**

**F-T7.3:** Future zbrain\_sim v2.x extension to language partition must reproduce medial pulvinar mediator identification on synthetic connectomes. Currently TESTABLE pending zbrain\_sim v2.x development.

## **§7.3 Level 3a — Observational (HCP / Cam-CAN connectome)**

**F-T7.4 (P1):** Language partition S\_XY exceeding 0.10 in more than 1 of 6 parcellations on HCP normative SC fails the language Z-Spin mediation hypothesis. Status: TESTABLE-PENDING (target v1.2).

**F-T7.5 (P2):** Language partition F\_Z exceeding 0.30 in more than 1 of 6 parcellations on HCP normative SC or FC fails the language Fiedler neutrality. Status: TESTABLE-PENDING.

**F-T7.6 (P3):** Bilateral medial pulvinar failing to attain mean rank ≤ 3.0, OR Fisher combined p \> 10⁻⁴, refutes sub-nucleus specificity. Status: TESTABLE-PENDING.

**F-T7.7 (P4):** Bilateral lateral pulvinar within 1.0 mean rank of medial pulvinar across 24 combinations REFUTES the medial-vs-lateral specificity. Theorem T7.1 weakens to whole-pulvinar (NC-T7.9). Status: TESTABLE-PENDING.

**F-T7.8 (P5):** If left-only P\_X^lang yields S\_XY \> 0.10 in 2+ parcellations while bilateral P\_X^lang passes, the language partition is irreducibly lateralized; OBSERVATION not framework-failure. If neither passes, the partition definition is refuted. Status: TESTABLE-PENDING.

**F-T7.9 (P6, INSIGHT):** Maldonado (2024) stimulation-induced anomia sites preferentially fall on AR-like \+ lateral tract trajectories. Failure at independent cohort weakens §6 Discussion but does not falsify Theorem T7.1. Status: TESTABLE.

## **§7.4 Level 4 — External replication**

**F-T7.10:** Failure of P1, P2, P3 to replicate in {UK Biobank fMRI when pulvinar-resolution available, OpenNeuro language datasets, Cogitate 2025+ release} makes the result cohort-specific. Status: PENDING.

**F-T7.11:** ZS-T7 does NOT predict cross-species replication (NC-T7.6). Cross-species test formally excluded. Status: not applicable.

**F-T7.12 (Programme):** If ZB-V1 \+ ZB-V6 \+ ZB-V7 \+ ZS-T7 \+ ZB-V8 collectively yield ≤ 3 of 6 routes PASS at S\_XY/F\_Z thresholds, Path E (scale invariance) is REFUTED at programme level. Status: programme-level PENDING.

## **§7.5 Level 3b — Oscillatory (Cam-CAN MEG)**

**F-T7.13 (P7, formalized v1.1):** Theorem T7.2 fixes Φ\_lang ≤ f · ln(2) but does not fix the band f. Pre-registered decision rule: PASS-α if alpha-pulvinar PLV exceeds theta-pulvinar PLV by ≥ 0.10 in ≥ 80% of subjects. PASS-θ if theta exceeds alpha by ≥ 0.10. INDETERMINATE if neither margin reached (dual-band T7.2 retained). FAIL if neither alpha nor theta is significantly phase-locked to medial pulvinar (PLV \< 0.30 in both bands across ≥ 80% of subjects); Theorem T7.2 RETRACTED in this case. Status: TESTABLE-PENDING (Cam-CAN MEG, target v1.2).

## **§7.6 Level 3c — Lesion-symptom (NEW in v1.1)**

**F-T7.14 (P8, NEW v1.1, Theorem T7.3 keystone):** If pulvinar-lesion patients fail to show the triple dissociation (effect size d ≥ 0.8 for naming deficit AND d ≤ 0.3 for comprehension and repetition deficits, vs matched ATL-lesion and SMG/IFG-lesion controls), Theorem T7.3's brain-substrate operationalization is REFUTED. The closed-form mathematical content of T7.3 (Step 4\) is preserved. Status: TESTABLE-PENDING (target v1.3).

**F-T7.15 (P9, NEW v1.1, Theorem T7.4 keystone):** If pulvinar-lesion patients fail to show ≥ 50% N400 amplitude reduction in 300–500 ms window during picture-word matching while preserving early auditory components (100–200 ms) and late positivity (500+ ms) within 1 SD of control mean, Theorem T7.4's identification of TOT with sub-saturation η \< 1 regime is REFUTED. Status: TESTABLE-PENDING (target v1.3).

**F-T7.16 (P10, NEW v1.1, conditional on P7 PASS-θ, Theorem T7.5 keystone):** If pulvinar-lesion patients fail to show ≥ 40% theta-band power reduction in left peri-temporal cortex during picture naming while preserving alpha-band power within 1 SD of control mean, Theorem T7.5's theta-pulvinar specificity is REFUTED. If P7 resolves PASS-α or INDETERMINATE, F-T7.16 is replaced with band-appropriate variant in v1.2 amendment. Status: TESTABLE-PENDING conditional on P7 outcome (target v1.3).

# **§8. NON-CLAIMs**

Fourteen NON-CLAIMs delimit the framework's reach. The set is unchanged in count from v1.0, but two NCs are AMENDED in v1.1 to reflect the new theorems and predictions: NC-T7.8 (disease-specific perturbations) is narrowed in scope; NC-T7.13 (alpha vs theta) is strengthened with a prima-facie theta anchoring. The other twelve NCs are inherited unchanged from v1.0. The amended versions and reasoning are explicit below.

**NC-T7.1 (Cardinal NC-4 inheritance, Z-Brain corpus-wide; UNCHANGED v1.0).** The pulvinar's role as Z-Spin mediator of the language partition is a structural mapping in the Block Fiedler Mediation Theorem sense. The brain does not physically instantiate Z-Spin's Planck-scale geometric primitives (A \= 35/437, Q \= 11\) at neural scale. ZS-T4 v1.0 § Level II established (X, Z, Y) \= (3, 2, 6\) ↔ (Body, DNA, Brain) as STRUCTURAL ISOMORPHISM only; ZS-T7 inherits this explicitly.

**NC-T7.2 (Path D refute: 4-tract ≠ 4-handshake; UNCHANGED v1.0).** The 4-tract count of pulvino-temporal connections (Maldonado et al. 2024\) is NOT the spatial instantiation of the 4-handshake-per-2π-cycle structure of ZS-S15 §D.5.

**NC-T7.3 (Programme NON-CLAIM, NC-M23.1 style; UNCHANGED v1.0).** ZS-T7 contributes one route to multi-route over-determination of the Block Fiedler Mediation thesis at brain-internal scales. ZS-T7 does NOT prove universality of Z-Spin mediator architecture. Path E verification is ZB-X2 (Corpus Preface) responsibility.

**NC-T7.4 (Three-level fractal nesting bounded as HYPOTHESIS-strong; UNCHANGED v1.0).** ZS-T7 demonstrates fractal nesting at one new partition. HYPOTHESIS-strong, not a strict closure relation.

**NC-T7.5 (Variable Binding exclusion, NC-P2.2 inheritance; UNCHANGED v1.0).** ZS-T7 addresses lexical retrieval mediation, NOT compositional binding into syntactic structures (Smolensky 1990; Van der Velde 2015). The medial pulvinar Z-Spin mediator is a partial mechanism for lexical-retrieval, not a universal binding solution.

**NC-T7.6 (No cross-species claim; UNCHANGED v1.0).** ZS-T7 makes no claim about non-human primates or other species; F-T7.11 formally excludes cross-species testing.

**NC-T7.7 (No claim of unique sufficiency; UNCHANGED v1.0).** Even within the necessary-condition scope, ZS-T7 does not claim that medial pulvinar Z-Spin mediation is sufficient for lexical retrieval. Cortical microcircuit dynamics, neurotransmitter pharmacology, and synaptic plasticity operate at orthogonal levels of description that the framework does not address.

**NC-T7.8 (AMENDED v1.1: scope narrowed).** Original v1.0 NC: ZS-T7 v1.0 does not propose disease-specific perturbation predictions. Amended v1.1 NC: ZS-T7 v1.1 PROPOSES three lesion-deficit perturbation predictions (P8, P9, P10) under Theorems T7.3, T7.4, T7.5 respectively. The remaining NC scope in v1.1 is narrowed to: ZS-T7 v1.1 does not propose treatment-pharmacological predictions (e.g., levodopa, transcranial direct current stimulation, thalamic deep-brain stimulation interventions for selective rescue of phonology-semantics coupling). Such predictions, if structurally derivable, are reserved for ZB-D5 (Aphasia Mechanisms) or a future ZS-T7 v1.2+ amendment with dedicated derivation chain.

**NC-T7.9 (Whole-pulvinar fallback if F-T7.7 fails; UNCHANGED v1.0).** If medial-vs-lateral pulvinar mean rank gap \< 1.0 on AN3, Theorem T7.1 weakens to whole-pulvinar mediator. Sub-nucleus claim RETRACTED in this case.

**NC-T7.10 (No claim of mechanism for f selection at v1.1 release; UNCHANGED v1.0).** Theorem T7.2 bounds Φ\_lang ≤ f · ln(2). The frequency f is not derived from Z-Spin axioms in v1.1; it is inherited from cortical-rhythm literature (alpha at 10 Hz from ZB-V1 visual codec; theta at 4–8 Hz from speech-tracking literature). NC-T7.13 below registers the alpha-vs-theta selection as an empirical question.

**NC-T7.11 (No derivation of Fedorenko natural-kind selectivity; UNCHANGED v1.0).** Fedorenko, Ivanova, and Regev (2024) established the language network as a domain-specific natural kind. ZS-T7 is COMPATIBLE but does NOT derive this. The partition framework provides necessary structural conditions for unified retrieval; it does not provide sufficient conditions for domain-specific selectivity.

**NC-T7.12 (No claim of clinical diagnostic utility; UNCHANGED v1.0).** ZS-T7 reports closed-form and in-silico verification only. Ten TESTABLE-PENDING predictions await execution. The framework is not a clinical diagnostic at v1.1; deployment requires regulatory-grade validation outside corpus scope.

**NC-T7.13 (AMENDED v1.1: theta registered as prima facie more anchored).** Original v1.0 NC: alpha-vs-theta band selection for f is registered as an empirical question, with neither band claimed by ZS-T7 v1.0. Amended v1.1 NC: the empirical asymmetry between alpha-language and theta-language phase-locking literature is honestly recognized. The theta (4–8 Hz) cortical syllable-tracking literature (Giraud and Poeppel 2012; Doelling et al. 2014; Luo and Poeppel 2007; Hyafil et al. 2015\) is substantially stronger than any alpha-language phase-locking literature. ZS-T7 v1.1 therefore registers Reading T7.2.B (theta band) as the prima facie more empirically anchored reading, while Reading T7.2.A (alpha band) is retained as a corpus-internal hypothesis from ZB-V1 visual-codec inheritance with no independent language-relevant empirical anchor. ZS-T7 v1.1 still does NOT claim a final resolution; F-T7.13 / P7 (Cam-CAN MEG) operationalizes empirical resolution.

**NC-T7.14 (Coupé / Zheng-Meister ratio is anti-numerology candidate, not framework-claim; UNCHANGED v1.0).** Coupé et al. (2019) \~39 bits/sec speech production rate / Zheng-Meister (2024) \~10 bits/sec conscious throughput ratio (≈ 4\) numerically coincides with the four-handshake-per-2π-cycle structure of ZB-V1 Theorem V1.3. ZS-T7 EXPLICITLY DOES NOT CLAIM that this coincidence is structurally meaningful. The two measurements are at different layers. The candidate match is registered for ZS-T2 v2.0 anti-numerology Monte Carlo audit.

# **§9. Conclusion**

ZS-T7 v1.1 advances the Z-Spin Translational corpus from a connectome-only language-partition framework (v1.0) to a three-level prediction framework (v1.1) addressing four established neuroscientific puzzles: dorsal-ventral language stream integration; thalamic aphasia phenotype; lexical retrieval throughput ceiling and theta rhythm; and tip-of-the-tongue as transmission deficit. Three new theorems (T7.3 Lesion-Symptom Coupling \[DERIVED\]; T7.4 TOT-as-Coupling-Failure \[DERIVED-CONDITIONAL\]; T7.5 Theta-Pulvinar PLV Specificity \[INSIGHT, conditional on P7 PASS-θ\]) are derived from corpus-PROVEN inputs (L\_XY ≡ 0; channel capacity ≤ ln(2); Hardware Axiom H2) without introducing new free parameters.

Ten pre-registered TESTABLE predictions across three empirical levels are advanced. P1–P6 (connectome on HCP-YA, target v1.2) inherited unchanged from v1.0. P7 (alpha-vs-theta on Cam-CAN MEG, target v1.2) formalizes the v1.0 F-T7.13 gate into a TESTABLE prediction. P8 (lesion-symptom triple dissociation on thalamic stroke cohorts, target v1.3) is the keystone prediction of Theorem T7.3 and operationalizes the corpus's L\_XY ≡ 0 architecture as a clinical phenotype prediction. P9 (N400 attenuation in pulvinar-lesion patients, target v1.3) operationalizes Theorem T7.4 as an ERP signature prediction. P10 (theta-pulvinar PLV degradation, conditional on P7 PASS-θ, target v1.3) operationalizes Theorem T7.5 as a MEG signature prediction.

Sixteen falsification gates F-T7.1 through F-T7.16 across four levels constitute the empirical contract. Fourteen NON-CLAIMs delimit framework scope; NC-T7.8 (disease-specific perturbations) is narrowed in v1.1 from full exclusion to scope-narrowed exclusion (lesion-deficit predictions now TESTABLE; only treatment-pharmacological predictions remain NON-CLAIM). NC-T7.13 (alpha vs theta) is strengthened in v1.1 to explicitly recognize theta as the prima facie more empirically anchored band, with alpha retained as a corpus-internal hypothesis subject to F-T7.13 / P7 resolution.

Verification: 27/27 closed-form \+ in-silico gates PASS in zs-t7\_verify\_v1\_1.py (v1.0 24/24 PASS preserved bit-identical; three new gates G-F.1, G-F.2, G-F.3 cover Theorem T7.3 closed-form structure). Cardinal NC-4 (Z-Brain) preserved throughout. Zero free parameters. Substrate-Agnostic Block Fiedler Application.

The ambition of v1.1 is not closure but expanded testability: ZS-T7 v1.1 puts ten falsifiable predictions on the table across three levels of evidence that external neuroscientists can directly test in their clinical, electrophysiological, and connectome research. Success or failure on these ten predictions, evaluated under the ZS-T5 retraction-or-confirmation discipline, will determine the empirical fate of the framework's commitment that L\_XY ≡ 0 \+ ln(2) capacity bound governs the human language network at three levels simultaneously.

# **§10. Acknowledgements & Code Availability**

**Acknowledgements.** This v1.1 amendment was developed in response to external feedback identifying that ZS-T7 v1.0's connectome-only predictions, while structurally rigorous, did not fully exploit the corpus's L\_XY ≡ 0 \+ Hardware Axiom H2 derivation chain to make lesion-symptom predictions of direct clinical relevance. The three new theorems (T7.3, T7.4, T7.5) and four new predictions (P7, P8, P9, P10) close this gap. The author thanks the external reviewer whose feedback motivated the v1.1 expansion. The v1.1 amendment retains full backward compatibility with v1.0: all v1.0 theorems, predictions, falsification gates, and NON-CLAIMs are preserved (with two amendments to NC-T7.8 and NC-T7.13 that strictly extend or clarify their original scope without contradicting any v1.0 content). The 24 v1.0 verification gates are inherited bit-identical; three new v1.1 gates extend the suite. AI assistance: Anthropic Claude operating under Z-Spin Protocol in \[자유 탐색\] mode for the exploration phase, \[코퍼스 탐색\] for derivation attempts, and \[논문 작성\] for the present paper. No AI-generated numerical values enter the pre-registered gates; all pre-registration locks precede AI-assisted analysis. The author assumes full responsibility for all scientific content. No competing interests. No external funding.

**Code availability.** All numerical claims in Tables 2–5 and all pre-registered thresholds are reproducible from a single Python verification script (zs-t7\_verify\_v1\_1.py), which extends the v1.0 script (zs-t7\_verify\_v1\_0.py) by appending three new gates G-F.1, G-F.2, G-F.3 covering Theorem T7.3 closed-form structure. The v1.0 sub-pipelines are preserved bit-identical. SHA-256 pre-registration hashes for both v1.0 and v1.1 scripts committed at v1.1 release. The v1.1 script runs in approximately 2 seconds on a single CPU core. All operations deterministic (seed \= 42; numpy ≥ 1.22, scipy ≥ 1.8). The repository is the Z-Spin Cosmology GitHub at https://github.com/KennyKang-git/zspin/tree/main/papers/ZS-T7. The Cam-CAN MEG analysis pipeline for P7 \+ P10 will be added at v1.2 release. The lesion-symptom analysis pipeline for P8 \+ P9 will be added at v1.3 release pending cohort data access.

# **§11. Appendix A — Verification Script Summary**

The companion script zs-t7\_verify\_v1\_1.py reports 27 closed-form \+ in-silico gates across six groups. The first five groups (A–E) are inherited bit-identical from zs-t7\_verify\_v1\_0.py (24 gates). The new sixth group (F) covers Theorem T7.3 closed-form structure (3 gates). All 27 gates PASS at v1.1 release. SHA-256 pre-registration hash committed; any subsequent modification changes the hash. The script runs in approximately 2 seconds on a single CPU core. All operations deterministic.

*Table 6\. Gate breakdown for zs-t7\_verify\_v1\_1.py. Groups A–E are bit-identical to v1.0 (24/24 PASS preserved). Group F is NEW in v1.1 (3 new closed-form gates verifying Theorem T7.3 derivation Step 4). Total: 27/27 PASS.*

| Gate | Tests | Description | v1.0 / v1.1 |
| ----- | ----- | ----- | ----- |
| GATE A | 5 | LOCKED inputs sanity (A reference, Q reference, dim(Z), thresholds, ZB-N1 baseline) | v1.0 inherited bit-identical |
| GATE B | 6 | Block Fiedler Mediation Theorem closed-form on synthetic L (a \= 8, c \= 2, b \= 35\) | v1.0 inherited bit-identical |
| GATE C | 4 | AN3 anti-numerology design (8 candidates, 24 metric-parcellation combinations) | v1.0 inherited bit-identical |
| GATE D | 5 | Cross-paper consistency (ZB-N1, ZB-V1, ZB-P2, ZB-P3, ZS-T4 Cardinal NC-4) | v1.0 inherited bit-identical |
| GATE E | 4 | External anchor consistency (Maldonado 2024, MGN tract count, Fedorenko 2024, Coupé/ZM disclaim) | v1.0 inherited bit-identical |
| GATE F | 3 | \[NEW v1.1\] Theorem T7.3 closed-form: G-F.1 R\_Z preserves σ(L\_XX); G-F.2 R\_Z preserves σ(L\_YY); G-F.3 R\_Z eliminates X-Y resolvent | v1.1 NEW |

The bit-identical preservation of GATE A through GATE E v1.0 sub-pipelines ensures that any reader can verify v1.1 ↔ v1.0 backward compatibility by direct script comparison: the v1.1 script differs from v1.0 only by (i) file name and version identifier in header; (ii) three additional functions implementing G-F.1 through G-F.3; (iii) updated Note in GATE E.4 (already present in v1.0) referencing the amended NC-T7.13 v1.1 reading. No numerical claim from v1.0 is changed in v1.1.

# **§12. References**

## **§12.1 Internal — Z-Spin Cosmology**

Kang, K. (2026). The Z-Spin Action and U(1) Completion (ZS-F1 v1.0). Z-Spin Cosmology Collaboration.

Kang, K. (2026). Geometric Impedance A \= 35/437 (ZS-F2 v1.0). Z-Spin Cosmology Collaboration.

Kang, K. (2026). Gauge Symmetry Constraint — Why Q \= 11 (ZS-F5 v1.0). Z-Spin Cosmology Collaboration.

Kang, K. (2026). Block-Laplacian Spectral Verification — Continuum Perturbative Protection Theorem (ZS-M6 v1.0 §7A). Z-Spin Cosmology Collaboration.

Kang, K. (2026). Geometric Decoherence and CPTP Channel — dim(Z) \= 2 Kraus pair (ZS-Q1 v1.0). Z-Spin Cosmology Collaboration.

Kang, K. (2026). Structural Arrow of Time from the Z-Bottleneck (ZS-Q7 v1.0). Z-Spin Cosmology Collaboration.

Kang, K. (2026). Z-Spin Hardware Specification — Three Hardware Axioms (ZS-QH v1.0). Z-Spin Cosmology Collaboration.

Kang, K. (2026). Twin-Reuleaux Pair as Geometric Realization of EM Field Duality (ZS-S15 v1.0). Z-Spin Cosmology Collaboration.

Kang, K. (2026). Standard Model Sector — Continuum Perturbative L\_XY \= 0 (ZS-S1 v1.0). Z-Spin Cosmology Collaboration.

Kang, K. (2026). Partition-Aware Routing / Block Fiedler Mediation Theorem (ZS-T1 v1.0). Z-Spin Cosmology Collaboration.

Kang, K. (2026). Anti-Numerology Methodology, 5670 × 29 MC scan (ZS-T2 v1.0). Z-Spin Cosmology Collaboration.

Kang, K. (2026). Z-Sim Forward Simulator (ZS-T3 v1.0). Z-Spin Cosmology Collaboration.

Kang, K. (2026). Cosmos-Human Isomorphism (ZS-T4 v1.0). Z-Spin Cosmology Collaboration.

Kang, K. (2026). Principal Connectivity Gradient and Hidden Third-Position Z-Spin Mediator (ZS-T5 v1.0). Z-Spin Cosmology Collaboration.

Kang, K. (2026). Molecular Biology Translational Synthesis (ZS-T6 v1.0). Z-Spin Cosmology Collaboration.

Kang, K. (2026). Pulvinar-Mediated Z-Spin Language Partition (ZS-T7 v1.0). Z-Spin Cosmology Collaboration. \[Predecessor of present amendment.\]

## **§12.2 Internal — Z-Brain Neuroscience Series**

Kang, K. (2026). ZB-N1 v3.0: Thalamocortical Z-Spin Mediation from the Block Laplacian. Z-Brain corpus.

Kang, K. (2026). ZB-P2 v1.0: The Binding Problem (10 bits/s) as ln(2) Channel Bound. Z-Brain corpus.

Kang, K. (2026). ZB-P3 v1.0: IIT Phi under Z-Mediator Rank Constraint. Z-Brain corpus.

Kang, K. (2026). ZB-V1 v1.0: The Visual Cortex as Z-Sector Codec. Z-Brain corpus.

Kang, K. (2026). ZB-C5 v1.0: Pulvinar-Mediated Language Partition. Z-Brain corpus. \[Source manuscript for ZS-T7 v1.0; v1.1 amends T-series version under ZS-T5 conversion protocol.\]

Kang, K. (2026). ZB-K Notebook 005: Partition-Dependence Principle. Z-Brain corpus internal pre-registration.

Kang, K. (2026). ZB-K Notebook 006: ZB-C5 AN3 Protocol Formalization. Z-Brain corpus internal pre-registration.

Kang, K. (2026). The Book of Z-Spin Cosmology v3.3. Z-Spin Cosmology Collaboration.

Kang, K. (2026). The Book of Z-Brain v0.31 (v1.0 release). Z-Brain Neuroscience Series Foundation Document.

## **§12.3 External — Standard References**

Binder, J. R., Desai, R. H., Graves, W. W., & Conant, L. L. (2009). Where is the semantic system? A critical review and meta-analysis of 120 functional neuroimaging studies. Cerebral Cortex, 19, 2767–2796.

Brown, R., & McNeill, D. (1966). The "tip of the tongue" phenomenon. Journal of Verbal Learning and Verbal Behavior, 5, 325–337.

Bruzzone Giraldez, M., Lopez-Saca, J. M., Restrepo, L., Gomez-Velazquez, A., & Liebeskind, D. S. (2015). Aphasia after infarction of the left posterior pulvinar nucleus of the thalamus — case report and literature review. Journal of the Neurological Sciences, 357 (Suppl 1), e408.

Burke, D. M., MacKay, D. G., Worthley, J. S., & Wade, E. (1991). On the tip of the tongue: What causes word finding failures in young and older adults? Journal of Memory and Language, 30, 542–579.

Card, N. S., et al. (2024). An accurate and rapidly calibrating speech neuroprosthesis. Nature Medicine, 30, 1466–1476.

Catani, M. (2002). Virtual in vivo interactive dissection of white matter fasciculi in the human brain. NeuroImage, 17, 77–94.

Coupé, C., Oh, Y. M., Dediu, D., & Pellegrino, F. (2019). Different languages, similar encoding efficiency: Comparable information rates across the human communicative niche. Science Advances, 5, eaaw2594. doi:10.1126/sciadv.aaw2594.

Crosson, B. (1985). Subcortical functions in language: A working model. Brain and Language, 25, 257–292.

Doelling, K. B., Arnal, L. H., Ghitza, O., & Poeppel, D. (2014). Acoustic landmarks drive delta-theta oscillations to enable speech comprehension by facilitating perceptual parsing. NeuroImage, 85, 761–768.

Fedorenko, E., Ivanova, A. A., & Regev, T. I. (2024). The language network as a natural kind within the broader landscape of the human brain. Nature Reviews Neuroscience, 25, 289–312. doi:10.1038/s41583-024-00802-4.

Fedorenko, E., Ivanova, A. A., & Regev, T. I. (2025). Reply to "Language is widely distributed throughout the brain". Nature Reviews Neuroscience, 26, 190–191.

Frobenius, F. G. (1877). Über lineare Substitutionen und bilineare Formen. Journal für die reine und angewandte Mathematik, 84, 1–63.

Giraud, A.-L., & Poeppel, D. (2012). Cortical oscillations and speech processing: emerging computational principles and operations. Nature Neuroscience, 15, 511–517.

Glasser, M. F., et al. (2016). A multi-modal parcellation of human cerebral cortex. Nature, 536, 171–178.

Hickok, G., & Poeppel, D. (2007). The cortical organization of speech processing. Nature Reviews Neuroscience, 8, 393–402.

Hillis, A. E., et al. (2014). Aphasia or neglect after thalamic stroke: the various ways they may be related to cortical hypoperfusion. Frontiers in Neurology, 5, 231\. doi:10.3389/fneur.2014.00231.

Hyafil, A., Fontolan, L., Kabdebon, C., Gutkin, B., & Giraud, A.-L. (2015). Speech encoding by coupled cortical theta and gamma oscillations. eLife, 4, e06213.

Kutas, M., & Federmeier, K. D. (2011). Thirty years and counting: Finding meaning in the N400 component of the event-related brain potential (ERP). Annual Review of Psychology, 62, 621–647. doi:10.1146/annurev.psych.093008.131123.

Lambon Ralph, M. A., Jefferies, E., Patterson, K., & Rogers, T. T. (2017). The neural and computational bases of semantic cognition. Nature Reviews Neuroscience, 18, 42–55.

Larivière, S., et al. (2021). The ENIGMA Toolbox: multiscale neural contextualization of multisite neuroimaging datasets. NeuroImage, 235, 117986\.

Luo, H., & Poeppel, D. (2007). Phase patterns of neuronal responses reliably discriminate speech in human auditory cortex. Neuron, 54, 1001–1010.

MacKay, D. G., & Burke, D. M. (1990). Cognition and aging: A theory of new learning and the use of old connections. In T. M. Hess (Ed.), Aging and cognition: Knowledge organization and utilization (pp. 213–263). Amsterdam: North-Holland.

Maffei, C., Sarubbo, S., & Jovicich, J. (2019). A missing connection: A review of the macrostructural anatomy and tractography of the acoustic radiation. Frontiers in Neuroanatomy, 13, 27\.

Maldonado, I. L., et al. (2024). Multimodal study of multilevel pulvino-temporal connections: a new piece in the puzzle of lexical retrieval networks. Brain, 147, 2245–2257. doi:10.1093/brain/awae021.

Najdenovska, E., et al. (2018). In-vivo probabilistic atlas of human thalamic nuclei based on diffusion-weighted magnetic resonance imaging. Scientific Data, 5, 180270\.

Ojemann, G. A., Fedio, P., & Van Buren, J. M. (1968). Anomia from pulvinar and subcortical parietal stimulation. Brain, 91, 99–116.

Saalmann, Y. B., et al. (2012). The pulvinar regulates information transmission between cortical areas based on attention demands. Science, 337, 753–756.

Saur, D., et al. (2008). Ventral and dorsal pathways for language. Proceedings of the National Academy of Sciences USA, 105, 18035–18040.

Schaefer, P. W., & Shariat, K. (2022). Thalamic aphasia: a review. Current Neurology and Neuroscience Reports, 22, 855–862. doi:10.1007/s11910-022-01242-2.

Shafto, M. A., et al. (2014). The Cambridge Centre for Ageing and Neuroscience (Cam-CAN) study protocol: a cross-sectional, lifespan, multidisciplinary examination of healthy cognitive ageing. BMC Neurology, 14, 204\.

Smolensky, P. (1990). Tensor product variable binding and the representation of symbolic structures in connectionist systems. Artificial Intelligence, 46, 159–216.

Swinburn, K., Porter, G., & Howard, D. (2004). Comprehensive Aphasia Test (CAT). Hove, UK: Psychology Press.

Van der Velde, F. (2015). Communication, concepts and grounding. Neural Networks, 62, 112–117.

Vos de Wael, R., et al. (2020). BrainSpace: a toolbox for the analysis of macroscale gradients in neuroimaging and connectomics datasets. Communications Biology, 3, 103\.

Zheng, J., & Meister, M. (2024). The unbearable slowness of being: why do we live at 10 bits/s? Neuron, 113, 192–204.

# **§13. Version History**

**v1.0 (May 2026):** Initial public release as ZS-T7 (Translational T-series, paper 7 of T-series). Consolidated from the ZB-C5 v1.0 source manuscript (Z-Brain corpus, May 2026), restructured into Z-Spin T-series format under the ZS-T5 v1.0 conversion protocol with five changes (citation rewrite, Z-mediation → Z-Spin mediation terminology, NC renaming, F-gate renaming, verification script rebundling). Two anti-numerology additions (NC-T7.13 \+ F-T7.13 alpha-vs-theta gate; NC-T7.14 Coupé/ZM ratio disclaim) introduced relative to ZB-C5 v1.0 source. Two theorems (T7.1 DERIVED-CONDITIONAL; T7.2 INSIGHT). Six TESTABLE-PENDING predictions P1–P6 (connectome). Twelve falsification gates F-T7.1 through F-T7.12, plus F-T7.13 NEW. Fourteen NON-CLAIMs. Verification 24/24 PASS in zs-t7\_verify\_v1\_0.py. Cardinal NC-4 preserved.

**v1.1 (May 2026, the present amendment):** Three-level expansion responding to external feedback identifying the gap between v1.0 connectome-only predictions and lesion-symptom predictions of direct clinical relevance. v1.1 changelog:

(i) Three new theorems registered. T7.3 Lesion-Symptom Coupling Theorem \[DERIVED\] — derived from L\_XY ≡ 0 \[PROVEN, ZS-F1 §9; ZS-S1 §4; ZS-M6 §7A all-orders\] \+ Hardware Axiom H2 \[DERIVED, ZS-QH\] — predicts triple dissociation under R\_Z (medial pulvinar removal): preserved P\_X-internal repetition AND preserved P\_Y-internal comprehension AND impaired X-Y coupling naming. T7.4 TOT-as-Coupling-Failure \[DERIVED-CONDITIONAL\] — identifies tip-of-the-tongue phenomenon with the η \< 1 sub-saturation regime of the ln(2) capacity bound, unifying corpus architecture with Burke et al. (1991) transmission deficit theory. T7.5 Theta-Pulvinar PLV Specificity \[INSIGHT, conditional on F-T7.13/P7 PASS-θ\] — diagnostic signature is selective theta-band peri-temporal PLV reduction with alpha-band preservation.

(ii) Four new TESTABLE predictions registered. P7 (alpha-vs-theta on Cam-CAN MEG) formalizes v1.0 F-T7.13 into a TESTABLE prediction with PASS-α / PASS-θ / INDETERMINATE / FAIL decision rule. P8 (lesion triple dissociation on thalamic stroke cohorts) operationalizes Theorem T7.3 with effect size d ≥ 0.8 for naming and d ≤ 0.3 for comprehension/repetition vs matched ATL- and SMG/IFG-lesion controls. P9 (N400 attenuation in pulvinar-lesion patients) operationalizes Theorem T7.4 with ≥ 50% reduction in 300–500 ms window while preserving early auditory and late positivity within 1 SD. P10 (theta-pulvinar PLV degradation, conditional on P7 PASS-θ) operationalizes Theorem T7.5 with ≥ 40% theta reduction and alpha within 1 SD.

(iii) Three new falsification gates registered. F-T7.14 (P8 keystone of T7.3); F-T7.15 (P9 keystone of T7.4); F-T7.16 (P10 keystone of T7.5, conditional on P7 PASS-θ). Total falsification gates increased from 13 (v1.0) to 16 (v1.1).

(iv) Two NON-CLAIMs amended. NC-T7.8 amended from full disease-specific perturbation exclusion to scope-narrowed exclusion: lesion-deficit predictions now TESTABLE under P8–P10; only treatment-pharmacological predictions remain NON-CLAIM. NC-T7.13 amended from neutral alpha/theta registration to prima-facie theta anchoring: theta is recognized as the more empirically anchored band based on Giraud-Poeppel 2012 \+ Doelling 2014 \+ Luo-Poeppel 2007 \+ Hyafil 2015 syllable-tracking literature; alpha is retained as corpus-internal hypothesis from ZB-V1 visual-codec inheritance with no independent language-relevant empirical anchor. The other twelve NCs (NC-T7.1 through NC-T7.7, NC-T7.9 through NC-T7.12, NC-T7.14) inherited unchanged from v1.0.

(v) Verification artifact upgraded: zs-t7\_verify\_v1\_0.py (24/24 PASS) → zs-t7\_verify\_v1\_1.py (27/27 PASS). v1.0 sub-pipelines preserved bit-identical (GATE A through GATE E, 24 tests). New GATE F adds three closed-form gates verifying Theorem T7.3 derivation Step 4: G-F.1 R\_Z preserves σ(L\_XX); G-F.2 R\_Z preserves σ(L\_YY); G-F.3 R\_Z eliminates X-Y resolvent. SHA-256 pre-registration hash regenerated for v1.1.

(vi) Three new corpus inputs invoked in v1.1 (all at PROVEN, PROVEN-PERTURBATIVE, or DERIVED status in source paper): ZS-F1 v1.0 §9 \+ ZS-S1 v1.0 §4 (L\_XY ≡ 0 from action, PROVEN); ZS-M6 v1.0 §7A (all-orders perturbative protection, PROVEN-PERTURBATIVE); ZS-QH v1.0 (Hardware Axiom H2, DERIVED). No new free parameters introduced; zero numerical claim from v1.0 is changed in v1.1; full backward compatibility preserved.

(vii) Empirical execution targets: v1.2 (target 2026 Q4) closes P1–P7 (HCP-YA \+ Cam-CAN MEG); v1.3 (target 2027 Q2 conditional on cohort access) closes P8–P10 (thalamic stroke cohorts with ERP/MEG paradigms). Both amendments will operate under the ZS-T5 retraction-or-confirmation discipline: explicit RETRACTION and audit trail for any prediction that fails its threshold.

**v1.2 (target 2026 Q4):** Empirical execution of P1–P7. HCP-YA \+ ENIGMA Toolbox v2.0 connectome analysis for P1–P6. Cam-CAN MEG analysis for P7 alpha-vs-theta resolution. Per-subject sensitivity analysis on P1–P6. Schaefer-atlas Glasser-mask projection sensitivity test. Maldonado (2024) individual-tract S\_XY computation if data accessible. ZS-T2 v2.0 anti-numerology Monte Carlo audit on the Coupé / Zheng-Meister ratio (NC-T7.14). Outcome of P7 determines whether Theorem T7.5 / P10 advances as theta-band reading or is replaced with alpha-band variant.

**v1.3 (target 2027 Q2 conditional on cohort access):** Empirical execution of P8–P10 on thalamic stroke cohorts with ERP/MEG paradigms. P8 lesion triple dissociation on Hillis-style cohort or extended cohort with n ≥ 60 across three lesion groups. P9 N400 attenuation on same cohort during picture-word matching. P10 theta-pulvinar PLV (conditional on P7 PASS-θ) on same cohort during picture naming. Pre-registration of cohort access protocol and ethics approval at v1.3 announcement; v1.3 amendment will report PASS / FAIL / RETRACTION outcomes per ZS-T5 discipline.

Kenny Kang | May 2026 | ZS-T7 v1.1