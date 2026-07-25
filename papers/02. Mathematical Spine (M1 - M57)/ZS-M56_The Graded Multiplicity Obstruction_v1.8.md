**ZS-M56**  
**The Graded Multiplicity Obstruction**

*Why the **Q** \= 11 register admits no seam-Z₂-preserving tensor subsystem, and what that leaves for the environment*  
   
Kenny Kang · Z-Spin Cosmology Collaboration  
March 2026 · Theme: Mathematical Spine · Paper code: ZS-M56 · Version 1.8 — FINAL  
Supersedes ZS-M56 v1.7. Seven external audit rounds; sixty-one findings upheld, none contested. The central theorem of this version was supplied by audit round 7 and is verified here.  
Parent: ZS-M54 v2.2 FINAL. Reserved and untouched: ZS-M55. Successors: ZS-M57, ZS-Q19.  
   
**Verification: 101/101 PASS \+ 20 declarations | 0 FAIL | proof-bearing (R+A) \= 76, controls (X) \= 25, proxies (P) \= 0 | ledger classes now genuinely synchronised with the body | all figures from one seeded run of zs\_m56\_verify\_v1\_8.py | (A, Q, dim Z) \= (35/437, 11, 2\) LOCKED | Zero Free Parameters**  
 

# **§0. Abstract**

Audit round 7 found that v1.7's central theorem did not prove its own conclusion, supplied the theorem that does, and asked that it be verified. All eight findings are upheld, the replacement is verified, and ZS-M56 closes here.  
   
The refutation first. v1.7 argued that because every Z₂-odd operator in the register straddles the one-dimensional odd slot, and because a Z₂-even Hamiltonian cannot touch that slot, no odd partner B can exist internally. That reasoning confuses an odd factor with an even composite, which is the very distinction the paper's own selection rule rests on. The audit's counterexample is reproduced here: A \= |0⟩⟨1| \+ |1⟩⟨0| and B \= |1⟩⟨2| \+ |2⟩⟨1| are both odd, yet AB \+ BA \= |0⟩⟨2| \+ |2⟩⟨0| is even and therefore allowed. Two further findings are also reproduced: v1.7's “exhaustive” sector scan was not exhaustive, since span{|1⟩, |2⟩} carries restricted grading diag(−1, \+1) and two odd operators; and v1.7's check C3 verified only that Z\_path is odd while printing “admissible in-register B: none” as an unverified string.  
   
The replacement theorem, supplied by the audit and verified here, is shorter and stronger. The register grading J\_R \= I₁₁ − 2|1⟩⟨1| has multiplicities (n₊, n₋) \= (10, 1), so its odd subspace is one-dimensional. The pointer system in the seam basis has (p\_S, q\_S) \= (1, 1). An environment admitting a nonzero odd operator must have both eigenspaces occupied, p\_E ≥ 1 and q\_E ≥ 1, and then the odd subspace of the product grading has dimension  
**q(J\_S ⊗ J\_E) \= p\_S q\_E \+ q\_S p\_E \= q\_E \+ p\_E \= dim E ≥ 2 .**  
A grading-preserving isometry W : ℋ\_S ⊗ ℋ\_E ↪ ℂ¹¹ with W(J\_S ⊗ J\_E) \= J\_R W maps that odd subspace injectively into a one-dimensional one. Since 2 \> 1, no such isometry exists. Verified over seven (p\_E, q\_E) profiles, with the degenerate uniform gradings excluded a priori because they carry no odd operator at all.  
   
**The theorem also reconciles this paper's own history.** The v1.1 counterexample embedded ℂ²\_Z ⊗ ℂ²\_E into ℂ¹¹ and stands: on the code block the register grading is diag(+1, −1, \+1, \+1) with one negative, while every J\_S ⊗ J\_E on ℂ⁴ has two. One is not two, so the embedding cannot intertwine the gradings. Embedding the channel is possible; a seam-Z₂-preserving action-level tensor subsystem is not. That is the exact final statement, and it explains in one line why v1.0 was wrong and why its conclusion nevertheless keeps reappearing.  
   
Two further corrections go against this paper. The spinor candidate's “charge match” is WITHDRAWN: operator parity is defined by conjugation, and D^{1/2}(2π) \= −I is central, so (−I)B(−I) \= B for every B and the odd-operator count on that grading is zero. What the spinor supplies is a dimension and a state sign, not the required non-central involution. And v1.7's claim that the whole ZS-Q16 ghost route fails is WITHDRAWN as overreach: what was excluded is the isolated one-dimensional z₋-only carrier, and a full BRST ghost–antighost or cohomological graded factor was never analysed.  
   
Four ledger entries that the v1.7 body had corrected but the v1.7 script had not are resynchronised, so the cover's claim of synchronisation is now true. The successor question is unchanged in substance and sharper in form: the environment must have dimension 2, a non-central Z₂ involution, and no grading-preserving embedding into the register — that is, it must be genuinely external.  
 

# **Epistemic Status Legend**

| Tag | Meaning |
| ----- | ----- |
| PROVEN / DERIVED / DERIVED-CONDITIONAL | As in v1.7; the conditional form displays its hypothesis in the theorem line. |
| VERIFIED-REGRESSION | Reproduces corpus numbers from corpus inputs. Guards drift; not independent evidence. Carried in the control class. |
| ALGEBRAIC | An identity about a reconstructed operator, with no claim about the microscopic slab. |
| HYPOTHESIS / OPEN / CLOSED-NEGATIVE / NON-CLAIM / RETRACTED | As in v1.7. |
| TAUTOLOGY | A check whose two sides share their premise. Never evidence. |

 

# **§1. Audit round 7**

Table 1.1. All eight findings upheld. Findings G1–G3 are reproduced computationally in §2.1.

| \# | Finding | Disposition |
| ----- | ----- | ----- |
| G1 | M56.21's argument confuses an odd factor with an even composite. Two odd operators can multiply to an allowed even one. | UPHELD and reproduced (C9). The v1.7 argument is RETRACTED; the conclusion survives on the replacement theorem. |
| G2 | C2's “exhaustive sub-block scan” is not exhaustive: span{|1⟩, |2⟩} has grading diag(−1, \+1) and two odd operators. | UPHELD and reproduced (C10). C2 is DEMOTED to a sector control. |
| G3 | The audit supplies the correct theorem: a graded tensor-factor multiplicity obstruction. | UPHELD and ADOPTED as Theorem M56.21′, verified in §2.2 (C3, C3b). |
| G4 | C3 verified only that Z\_path is odd, while printing its conclusion as an unverified string. | UPHELD. C3 is rewritten as an actual multiplicity test over seven (p\_E, q\_E) profiles. |
| G5 | The spinor “charge match” is invalid: −I is central, so it induces no operator grading. | UPHELD and reproduced (C6, C8). The claim is WITHDRAWN. |
| G6 | The ZS-Q16 verdict is too broad; only the one-dimensional z₋-only carrier was excluded. | UPHELD. C4 is NARROWED; the general BRST route is explicitly not analysed. |
| G7 | Ledger entries B3–B6 retain pre-correction wording and classes. | UPHELD. B3, B4 reclassified to controls; B5 and B6 texts synchronised with the v1.7 body. |
| G8 | The cover's “ledger classes resynchronised” was not yet true. | UPHELD. It is true in this version, and the four specific diffs are printed in the ledger itself. |

 

# **§2. The closure, correctly proved**

**2.1 What was wrong, reproduced**  
Table 2.1. The audit's three counterexamples, recomputed (C9, C10, C6).

| Claim in v1.7 | Counterexample | Verdict |
| ----- | ----- | ----- |
| “An odd partner is itself forbidden in an even Hamiltonian.” | A \= |0⟩⟨1| \+ |1⟩⟨0| and B \= |1⟩⟨2| \+ |2⟩⟨1| are both odd; AB \+ BA \= |0⟩⟨2| \+ |2⟩⟨0| is even. | Inference invalid. RETRACTED. |
| “Exhaustive scan of register sub-blocks.” | span{|1⟩, |2⟩} has grading diag(−1, \+1) and 2 odd operators. | Not exhaustive. C2 demoted to control. |
| “The spinor factor is a charge match.” | J\_E \= −I is central: (−I)B(−I) \= B for all B, so odd operators \= 0\. | WITHDRAWN. Dimension and state sign only. |

   
The first of these is the same error this paper made in v1.6 and corrected in v1.7 — conflating what a grading forbids as a lone term with what it forbids in a product — committed once more in the argument that replaced it.  
   
**2.2 Theorem M56.21′ (Graded Tensor-Factor Multiplicity Obstruction). \[DERIVED\]**  
Let the seam Z₂ act on the register as J\_R \= I₁₁ − 2|1⟩⟨1| (ZS-F0 Def. 8.11), with eigenvalue multiplicities (n₊, n₋) \= (10, 1). Let the pointer system carry J\_S \= diag(+1, −1) in the seam basis, so (p\_S, q\_S) \= (1, 1\) and Z\_path is odd (‖J\_S Z\_path J\_S \+ Z\_path‖ \= 0.00×10⁰). Suppose an environment ℋ\_E with grading J\_E admits a nonzero Z₂-odd operator B. Then both eigenspaces of J\_E are occupied, p\_E ≥ 1 and q\_E ≥ 1, and  
**q(J\_S ⊗ J\_E) \= p\_S q\_E \+ q\_S p\_E \= q\_E \+ p\_E \= dim E ≥ 2 .**  
A grading-preserving isometry W : ℋ\_S ⊗ ℋ\_E ↪ ℂ¹¹ satisfying W(J\_S ⊗ J\_E) \= J\_R W restricts to an injection of the (−1)-eigenspace of J\_S ⊗ J\_E into the (−1)-eigenspace of J\_R. Injectivity requires q(J\_S ⊗ J\_E) ≤ q\_R \= 1, contradicting q(J\_S ⊗ J\_E) ≥ 2\. No such isometry exists. □  
Table 2.2. Verification over environment grading profiles (C3). The uniform cases (p\_E, 0\) and (0, q\_E) are excluded a priori: they carry no odd operator, so B \= 0\.

| (p\_E, q\_E) | dim E | odd operators on E | q(J\_S ⊗ J\_E) | \> q\_R \= 1? |
| ----- | ----- | ----- | ----- | ----- |
| (1, 1\) | 2 | 2 | 2 | yes |
| (2, 1\) | 3 | 4 | 3 | yes |
| (1, 2\) | 3 | 4 | 3 | yes |
| (2, 2\) | 4 | 8 | 4 | yes |
| (3, 1\) | 4 | 6 | 4 | yes |
| (1, 3\) | 4 | 6 | 4 | yes |
| (3, 2\) | 5 | 12 | 5 | yes |

   
The theorem excludes rotated code planes, sector mixing and Grassmannian embeddings in one step, because it constrains only the multiplicity of a grading and not the choice of basis.  
   
**2.3 Reconciliation with the v1.1 counterexample**  
ZS-M56 v1.1 exhibited an algebraic embedding of ℂ²\_Z ⊗ ℂ²\_E into ℂ¹¹, refuting v1.0's carrier no-go. That embedding stands. On the code block, however, the register grading is diag(+1, −1, \+1, \+1), with one negative eigenvalue, while every J\_S ⊗ J\_E on ℂ⁴ with both environment eigenspaces occupied has two (C3b). One ≠ two, so the embedding does not intertwine the gradings.  
**embedding the channel: possible.    seam-Z₂-preserving action-level tensor subsystem: impossible.**  
This is the final statement of ZS-M56, and it explains the whole eight-version history in one line: v1.0's conclusion was right about the graded structure and wrong about the algebra, and every intermediate version was an attempt to prove the right half with the wrong tool.  
 

# **§3. What the environment must be**

**Theorem M56.22′ (Non-Central Grading Requirement). \[DERIVED\]**  
An environment grading admits a nonzero odd operator only if it is non-central. A central grading ±I gives (±I)B(±I) \= B for every B, hence zero odd operators; a non-central involution diag(+1, −1) gives two (C8). Combining with Theorem M56.5, which fixed the minimal Stinespring environment dimension at 2 from Kraus rank alone, and with Theorem M56.21′:  
Table 3.1. The successor specification. Three constraints from three independent sources.

| Constraint | Source | Requirement on ℋ\_E |
| ----- | ----- | ----- |
| Kraus rank | M56.5 — Choi rank of Φ^QND\_λ for 0 \< |λ| \< 1 | dim E ≥ 2; the minimal realization has dim E \= 2 |
| Charge | M56.20, M56.22′ — the Z₂ selection rule | J\_E non-central, both eigenspaces occupied |
| Multiplicity | M56.21′ — q\_R \= 1 | no grading-preserving embedding into the register; ℋ\_E must be external |

   
**The spinor candidate, re-scored downward.** v1.7 claimed the j \= ½ factor of χ\_Z \= −1 satisfied both a dimension and a charge constraint. The charge half is withdrawn: D^{1/2}(2π) \= −I is central, and central gradings induce no operator parity at all. What the spinor supplies is dim E \= 2 and a sign on states. The non-central involution required by M56.22′ is not derived from it anywhere in the corpus. The candidate remains HYPOTHESIS on one satisfied constraint out of three, which is weaker than v1.7 recorded.  
   
**3.2 The ghost route, narrowed**  
v1.7 rejected the ZS-Q16 reading of z₋ as a traced-out environment. What that computation actually excluded is the isolated one-dimensional z₋-only carrier: a one-dimensional space carries only scalars, scalars are even, and B \= 0\. ZS-Q16's construction quotients the exact content and builds a physical pointer algebra by cohomological means, which is a different object and is not analysed here — ZS-Q16 is not among the loaded corpus files. v1.7's broader claim is WITHDRAWN. A full BRST ghost–antighost pair would have (p\_E, q\_E) \= (1, 1\) and would satisfy M56.22′; whether it can evade M56.21′ by living outside the register is exactly the successor question.  
 

# **§4. Status board at closing**

| Item | Status |
| ----- | ----- |
| M56.1, M56.2, M56.3 and M56.3a′, M56.4 and M56.4a, M56.5, M56.7, M56.10a, M56.10b, M56.11, M56.13′, M56.14a–c, M56.15′, M56.15a, M56.15b, M56.16′, M56.17 | Unchanged through seven audit rounds. The paper's durable content. |
| M56.18 Z₂-Odd Forbiddance | DERIVED at the symmetric quadratic background; DERIVED-CONDITIONAL to all orders. |
| M56.19 Spectral reproduction | VERIFIED-REGRESSION, control class in body and ledger alike \[v1.8 ledger sync\]. |
| M56.19a | No lone Z\_path term in the Z-only block \[text synced in the ledger, v1.8\]. |
| M56.20 Z₂ Selection Rule | DERIVED, premise (G) explicit; the “register cannot supply B” clause removed from body and ledger alike. |
| M56.21 Odd-Charge Exhaustion (v1.7) | RETRACTED. The argument confused an odd factor with an even composite. |
| M56.21′ Graded Multiplicity Obstruction | NEW, DERIVED. Supplied by audit round 7, verified here. Closes the action layer. |
| M56.22′ Non-Central Grading Requirement | NEW, DERIVED. |
| M56.8 spinor candidate | HYPOTHESIS on one of three constraints \[downgraded from v1.7's two of two\]. |
| C2 sector scan | Control, explicitly not exhaustive. |
| C4 ghost verdict | Narrowed to the one-dimensional z₋-only carrier. |

 

# **§5. Gates at closing**

| Gate | Status |
| ----- | ----- |
| F-M56.18a, F-M56.18b, F-M56.22 | CLOSED (v1.6, v1.7). |
| F-M56.A | ANSWERED IN FORM by M56.20, M56.21′ and M56.22′: the environment requires dimension at least 2, with a minimal candidate of dimension 2, a non-central Z₂ involution, and genuine externality. Construction is the successor question. |
| F-M56.19 | OPEN: exactness of the grading beyond quadratic order, symmetry-preserving regulator, Z₂-invariant background. |
| F-M56.20 | OPEN, principal successor question: exhibit an external factor meeting all three constraints of Table 3.1, together with the vertex Z\_path ⊗ B. → ZS-M57. |
| F-M56.21 | OPEN. Option B is excluded only in its one-dimensional form; options A and C, and the full BRST route, remain. → ZS-M57. |
| F-M56.23 (NEW) | Does the corpus derive a NON-CENTRAL Z₂ involution on any two-dimensional factor? Without one, M56.22′ has no realisation. This replaces the withdrawn spinor charge match. |
| F-M56.B / C | OPEN, load-bearing: does the action fix τ\_Z and ρ\_E? → ZS-Q19. |
| F-M56.13 | OPEN and never analysed, in eight consecutive versions. Φ^QND is mixed-unitary with p \= 0.9457568, so a classical two-outcome phase noise may reproduce it with no quantum tensor factor at all — and such a realisation would sit outside the reach of M56.21′ entirely. Handed on unpaid, and it should be ZS-M57's first item. |
| F-M56.11 / 12 / 14 / 15 / 16 / 17 | Unchanged. |
| F-M56.1–F-M56.5, F-M56.7–F-M56.10 | Stand. F-M56.6 FIRED (v1.1). |

 

# **§6. What is not closed**

•  F-M54-16′ is NOT closed. ZS-M56 closes the action-layer half of sub-condition (A) and specifies the environment; it does not construct one.  
•  No factor satisfying all three constraints of Table 3.1 is exhibited. The spinor satisfies one.  
•  The BRST ghost–antighost route satisfies the charge constraint on paper and was not analysed. → ZS-M57.  
•  The stochastic / mixed-unitary route has never been analysed in eight versions, and it is the one route M56.21′ does not reach.  
•  Exactness of the grading beyond quadratic order and Z₂-invariance of the background are assumed.  
•  τ\_Z and ρ\_E remain undetermined; by M56.7 the multiplier carries no evidential content while they are free.  
•  F-M54-12 and F-M54-13 untouched. The three-metric remains forbidden by ZS-A16 Thm F. No continuum limit, no phenomenology.

# **§7. Conclusion**

Eight versions, seven audit rounds, sixty-one upheld findings and not one contested. Six of the eight central theorems this paper advanced were refuted from outside it, and the seventh was refuted and then replaced by the audit that refuted it. What survives is worth stating plainly, because it took all eight versions to reach a form that no round has broken.  
   
The seam Z₂ of ZS-S1 §5.2 has a one-dimensional odd eigenspace in the Q \= 11 register. A pointer system carrying an odd observable, tensored with any environment able to carry an odd partner, has an odd eigenspace of dimension at least two. Two does not embed in one. Therefore no seam-Z₂-preserving tensor subsystem exists inside the register, and the QND vertex that ZS-M54 needs cannot be written there — not for want of dimensions, which v1.0 wrongly claimed, and not for want of an odd operator, which v1.7 wrongly claimed, but because a grading has a multiplicity and this one is too small.  
   
The same theorem explains why the counterexample that destroyed v1.0 was never a refutation of its instinct. The channel embeds; the grading does not. Everything between v1.1 and v1.7 was an attempt to say that without the right invariant.  
   
What is handed on is a specification rather than a prohibition:minimal dimension two, a non-central Z₂ involution, and genuine externality — three constraints from three independent sources, of which the corpus currently satisfies one. The spinor factor is no longer a charge match; the BRST route has not been looked at; and the oldest debt, the stochastic realisation that would sidestep this theorem altogether, has gone unpaid for eight versions and should be the successor's first item, not its last.  
   
Stated at exact strength: q\_R \= 1 \< 2 ≤ dim E, and that is the whole obstruction.  
 

# **Acknowledgements & Code Availability**

The central theorem of this version was written by audit round 7, not by this paper. It is adopted with attribution rather than paraphrased, because the alternative — restating a supplied proof as one's own construction — is the kind of quiet inaccuracy this line has spent eight versions learning to avoid. Every load-bearing error across those versions was caught externally; none by drafting. The last one lived inside the correction to the previous one, which is the strongest argument in this record for external review.  
   
All figures come from one seeded run of zs\_m56\_verify\_v1\_8.py (seed 56), filed as ledger\_v18.txt. Cover: 101/101 PASS, 0 FAIL, 20 declarations; proof-bearing (R+A) \= 76, controls (X) \= 25, proxies (P) \= 0\. The proof-bearing count fell from v1.7 despite four new checks, because C2, B3 and B4 moved to the control class.  
 

# **Appendix A. Verification ledger — v1.8 additions and resynchronisations**

| Check | Class | Result |
| ----- | ----- | ----- |
| C3 | R | Multiplicity obstruction: q\_R \= 1; for (p\_E,q\_E) \= (1,1), (2,1), (1,2), (2,2), (3,1), (1,3), (3,2) the odd-operator counts are 2, 4, 4, 8, 6, 6, 12 and q(J\_S ⊗ J\_E) \= 2, 3, 3, 4, 4, 4, 5, all exceeding q\_R. |
| C3b | R | Reconciliation: register negatives on the code block \= 1; J\_S ⊗ J\_E negatives \= 2\. |
| C8 | R | Non-central requirement: central −I gives 0 odd operators; diag(+1,−1) gives 2\. |
| C9 | X | Audit counterexample: A odd, B odd, AB \+ BA even — the v1.7 inference is invalid. |
| C10 | X | Audit counterexample: odd operators on span{|1⟩,|2⟩} \= 2 — the v1.7 scan was not exhaustive. |
| C2 | X | DEMOTED R → X: sector control only, explicitly not exhaustive. |
| C4 | X | NARROWED: excludes the isolated one-dimensional z₋-only carrier; the general BRST route is not analysed. |
| C6 | X | Spinor re-scored: −I is central, odd-operator count 0; “charge match” withdrawn. |
| B3, B4 | X | RECLASSIFIED R → X, matching the v1.7 body demotion to VERIFIED-REGRESSION. |
| B5, B6 | A, R | Texts synchronised: “no pointer component anywhere” → “no lone Z\_path term”; the “register cannot supply B” clause deleted. |
| C1, C5, C7, B1, B2, B7, Z1–Z12, Y1–Y9, X1–X8, W1–W7, V1–V46 | R, A, X | v1.0–v1.7 groups retained with their v1.8 classes and figures. |
| D0–D17, B8 | D | Twenty declarations, including D16 (final closure) and D17 (spinor charge-match retraction). |

 

# **Appendix B. Referee correction log (complete)**

| \# | Item | Origin |
| ----- | ----- | ----- |
| C1–C6 | Internal scans: Track II, Koenigs tautology, literal-True, norm convention, T\_XY layers, τ\_Z restored. | v1.0 |
| C7–C15 | Carrier no-go retracted after 11 \= 2·2 \+ 7\. | round 1 |
| C16–C24 | M56.9 rebuilt, M56.10 split, moduli 28 → 2, W1 rebuilt on the actual pointer slots. | round 2 |
| C25–C29 | M56.9 retracted as a channel obstruction; X5 retracted; route returned to OPEN. | round 3 |
| C30–C35 | Layer separation enforced; Y8 reclassified; M56.12 split; M56.13 narrowed. | round 4 |
| C36–C42 | Gram versus self-energy; double counting; sector versus datum; rank-one rigidity; one-unknown reduction. | round 5 |
| C43–C46 | F-M56.18a closed by two routes; Z₂ selection rule; gates F-M56.19–22. | v1.6 |
| C47–C55 | “Register cannot supply B” deleted; “no pointer anywhere” narrowed; M56.19 demoted; ghost route tested; F-M56.22 closed by quotation. | round 6 |
| C56 | M56.21 RETRACTED: an odd factor is not the same as an even composite. Counterexample reproduced. | round 7, G1 |
| C57 | C2 demoted to control; the sector scan is not exhaustive. Counterexample reproduced. | round 7, G2 |
| C58 | Theorem M56.21′ ADOPTED from the audit and verified over seven grading profiles. | round 7, G3 |
| C59 | C3 rewritten as an actual multiplicity test; the v1.7 string conclusion removed. | round 7, G4 |
| C60 | Spinor “charge match” WITHDRAWN: −I is central and induces no operator grading. | round 7, G5 |
| C61 | ZS-Q16 verdict narrowed to the one-dimensional carrier; the general BRST route explicitly not analysed. | round 7, G6 |
| C62 | Ledger entries B3–B6 reclassified and resynchronised; the cover claim is now true. | round 7, G7–G8 |

 

# **References**

\[1\] W. F. Stinespring, Proc. Am. Math. Soc. 6, 211 (1955); M.-D. Choi, Linear Algebra Appl. 10, 285 (1975).  
\[2\] K. Kraus, States, Effects, and Operations, LNP 190 (Springer, Berlin, 1983).  
\[3\] E. Knill, R. Laflamme, and L. Viola, Phys. Rev. Lett. 84, 2525 (2000).  
\[4\] P. Zanardi, D. A. Lidar, and S. Lloyd, Phys. Rev. Lett. 92, 060402 (2004).  
\[5\] D. Kribs, R. Laflamme, and D. Poulin, Phys. Rev. Lett. 94, 180501 (2005).  
\[6\] C. Becchi, A. Rouet, and R. Stora, Ann. Phys. (N.Y.) 98, 287 (1976); I. V. Tyutin, Lebedev Inst. preprint (1975).  
\[7\] H. Feshbach, Ann. Phys. (N.Y.) 5, 357 (1958); P.-O. Löwdin, J. Math. Phys. 3, 969 (1962).  
\[8\] S. Nakajima, Prog. Theor. Phys. 20, 948 (1958); R. Zwanzig, J. Chem. Phys. 33, 1338 (1960).  
\[9\] A. Björck and G. H. Golub, Math. Comput. 27, 579 (1973); C. C. Paige and M. A. Saunders, SIAM J. Numer. Anal. 18, 398 (1981).  
\[10\] F. J. Dyson, Phys. Rev. 75, 486 (1949).  
\[11\] M. A. Nielsen and I. L. Chuang, Quantum Computation and Quantum Information (Cambridge Univ. Press, Cambridge, 2010), Ch. 8\.  
\[12\] J. Watrous, The Theory of Quantum Information (Cambridge Univ. Press, Cambridge, 2018), Ch. 2\.  
\[13\] R. P. Feynman and F. L. Vernon, Jr., Ann. Phys. (N.Y.) 24, 118 (1963).  
\[14\] J. Schwinger, J. Math. Phys. 2, 407 (1961); L. V. Keldysh, Sov. Phys. JETP 20, 1018 (1965).  
\[15\] V. B. Braginsky, Y. I. Vorontsov, and K. S. Thorne, Science 209, 547 (1980).  
\[16\] W. H. Zurek, Rev. Mod. Phys. 75, 715 (2003).  
\[17\] G. Koenigs, Ann. Sci. Éc. Norm. Supér. (3) 1, 3 (1884); J. Milnor, Dynamics in One Complex Variable, 3rd ed. (Princeton Univ. Press, Princeton, 2006), §8.  
\[18\] A. S. Cattaneo, P. Mnev, and N. Reshetikhin, Commun. Math. Phys. 332, 535 (2014).  
\[19\] R. M. Corless et al., Adv. Comput. Math. 5, 329 (1996).  
   
Corpus: ZS-F0, ZS-F2, ZS-F5, ZS-M1, ZS-M2, ZS-M6, ZS-M43, ZS-M53 v1.5, ZS-M54 v2.2, ZS-Q11 and ZS-Q16 (cited, not loaded), ZS-Q18 v1.7, ZS-S1, ZS-S14, ZS-S20 v2.2, ZS-S24 v1.9, ZS-S27, ZS-A16, ZS-A17, ZS-A30 (cited, not loaded), ZS-T1, ZS-U7.  
 

# **Version History**

v1.0–v1.7 (March 2026): see the version history of ZS-M56 v1.7. In summary: a carrier no-go refuted by 11 \= 2·2 \+ 7; a seam-grading obstruction refuted for testing one coupling; a coupling-free rebuild refuted because its universal test imposed its premise; a mixed-generator route refuted for gluing two ZS-M54 layers; a misnamed self-energy and a double count; a rank-one rigidity that reduced everything to one parameter; that parameter closed at d \= 0 with a Z₂ selection rule; and an odd-charge exhaustion argument that did not follow.  
   
v1.8 (March 2026\) — FINAL. Audit round 7, all eight findings upheld. RETRACTED: Theorem M56.21 of v1.7, whose argument confused an odd factor with an even composite; the audit's counterexample A \= |0⟩⟨1|+|1⟩⟨0|, B \= |1⟩⟨2|+|2⟩⟨1|, AB+BA even, is reproduced. RETRACTED: the spinor “charge match” — D^{1/2}(2π) \= −I is central and induces no operator grading, so the odd-operator count on it is zero. NARROWED: the ZS-Q16 verdict, to the isolated one-dimensional z₋-only carrier. DEMOTED: C2 to a sector control, since span{|1⟩,|2⟩} carries two odd operators. ADOPTED from the audit and VERIFIED: Theorem M56.21′, the graded tensor-factor multiplicity obstruction — q\_R \= 1 while q(J\_S ⊗ J\_E) \= dim E ≥ 2, so no grading-preserving isometry ℋ\_S ⊗ ℋ\_E ↪ ℂ¹¹ exists; verified over seven (p\_E, q\_E) profiles and reconciled with the v1.1 code counterexample (1 negative versus 2). NEW: Theorem M56.22′, the non-central grading requirement. C3 rewritten as an actual multiplicity test. Ledger entries B3–B6 reclassified and resynchronised, so the cover's synchronisation claim is now true. New gate F-M56.23: does the corpus derive a non-central Z₂ involution on any two-dimensional factor? 101/101 PASS \+ 20 declarations, 0 FAIL. (A, Q, dim Z) \= (35/437, 11, 2\) LOCKED; no new constant introduced. ZS-M56 CLOSES at v1.8; the successor question passes to ZS-M57 and ZS-Q19, with the stochastic route as first item.