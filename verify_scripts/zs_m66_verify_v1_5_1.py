#!/usr/bin/env python3
"""ZS-M66 v1.5.1 — consolidated verification companion, FREEZE PENDING.

This single file is the registered companion of `ZS-M66_v1_5_1.md`.  It replaces
six earlier artifacts and carries their content, nothing deleted:

    zs_m66_split_construction_v0_1.py   -> blocks A, B
    zs_m66_general_and_K2_v0_1.py       -> blocks A, B, C
    zs_m66_fermion_boundary_v0_1.py     -> block  D
    zs_m66_cheshire_gate_v0_1.py        -> block  E
    ZS-M66_v1_0_supplement.md           -> block  R  (declaration rows)
    zs_m66_verify_v1_0.py               -> all blocks, superseded

The supplement is folded in here rather than into the paper body, because the
standing rule for this corpus line is that correction history, guard lineage
and release metadata do not go into a manuscript; they go into a registered
companion.  A verifier is a registered companion.  See row R14.

WHAT CHANGED IN v1.5.1, and why
  Correction only.  No new mathematics, no retyping, three repairs and one
  guard strengthened.  (1) v1.5 recorded the freeze and the user approval for
  it as accomplished facts while the audit that the freeze was conditional on
  had not yet run.  That is a release-metadata defect, not a wording one: a
  conditional approval was written into the record as a past decision.  The
  label is now PROPOSED-FOR-FREEZE and the approval line is withdrawn.
  (2) Two places still used the retired gate F-M66.13 in the present tense
  while the gate table called it retired; guard G14 passed them because it
  looked for the literal word OPEN and nothing else, which is a semantic false
  negative.  G14 now also catches present-tense gate usage, and both places
  are re-typed as historical.  (3) Paper 1 announced five statements and
  printed six; guard G18 is added to count them.

WHAT CHANGED IN v1.5, and why
  Round 5 found one scope overclaim and five stale internal references.  The
  overclaim: block Q was written as though moving to the cone of positive
  semidefinite operators removed a choice, when what it did was replace a
  basis choice by a CARRIER choice.  The cone is canonical once the carrier is
  fixed, and the carrier is not derived from anything.  Rows Q11 to Q13 make
  that exact rather than rhetorical, and in particular row Q12 shows where the
  strict bound of Theorem 3.7 actually comes from: faithfulness, which no pure
  state has, so the bound is bought with the mixing the vector model does not
  carry.  The stale references were dangling gates, a retired gate still
  quoted as ordering, a scope sentence that did not cover the section added in
  v1.4, and a printed conclusion contradicting the paper.  Guards G14 to G17
  are added so that a future edit cannot reintroduce any of them: they check
  the manuscript against itself and against this run.  This version is the
  freeze; no further version of this line is planned.

WHAT CHANGED IN v1.4, and why
  Block Q is added.  Round 4 observed that the generating basis of the cone,
  declared as a choice in v1.3, is not natural on a spinor boundary space, and
  pointed at the density-matrix cone instead.  Carried out, that move removes
  the choice rather than declaring it: the cone of positive semidefinite
  operators is canonical, kappa = Tr(rho J) is unitarily covariant, and the
  strict bound |kappa| < 1 follows from faithfulness alone with no alignment
  hypothesis.  Block Q also certifies the new no-go: if the boundary map
  commutes with the grading flip, its unique fixed point has kappa = 0
  exactly, so phase capability requires the action to break that symmetry, and
  the breaking needed is bounded below.

WHAT CHANGED IN v1.3, and why
  Round 3 found that this file's own header, usage line and release-metadata
  row still described v1.1 while every executable constant said v1.2, and that
  guard G09 passed anyway because it read only the manuscript.  A version-
  coherence guard that cannot see its own version string is a surface-form
  guard.  G09 now checks this source as well, and row F14 injects a stale
  version string to prove it fires.  Round 3 also found that the scalar
  closure of paper 4 was quantified over a term list that does not fix the
  scalar potential, so rows C07 and C08 are retyped C -> W and the closure is
  restated for the explicit boundary-term route only.

WHAT CHANGED IN v1.1, and why
  The v1.0 companion returned 74/74 PASS while the manuscript it accompanied
  carried a false universal statement.  Row D16 checked ONE positivity-
  improving matrix, found 0 < |kappa| < 1 there, and the manuscript read that
  witness as a property of every positivity-improving transfer operator.  It is
  not.  The exact counterexample

      P = [[2, 1], [1, 2]],   J = diag(-1, +1)

  is entrywise positive, has Perron-Frobenius eigenvalue 3 with ray (1, 1),
  has [P, J] != 0 and Delta != 0 and seam asymmetry T = 1 at its MAXIMUM, and
  yet kappa = 0, so the multiplier a(theta) = cos theta is real at every angle
  and the boundary carries no phase at all.  Block N locks this in as a
  negative control, row D16 is retyped from C to W, and guard G08 fails if the
  manuscript ever reasserts the withdrawn implication.  A witness passing is
  not a universal statement holding; that is the failure this file now guards.

Discipline
  * exact arithmetic only: Fraction and Gaussian rational.  No floating point
    appears in any evidence row.
  * class P (a row that discharges a theorem) is EMPTY by construction.  The
    proofs are the human arguments of the paper; these rows are computations,
    witnesses, controls, guards and declarations.
  * evidence rows (C, W, X) are subject to an AST audit forbidding constant
    folding and self-comparison.  D and G rows are exempt by declaration.
  * every guard carries a live-fire test (row G08).
  * locked project constants are excluded from the construction layer by a
    token scan over this source (row G01).

Usage
    python3 zs_m66_verify_v1_5_1.py               # full, manuscript required
    python3 zs_m66_verify_v1_5_1.py --no-manuscript # records that G04-G06 and
                                                  # G08-G09 were not run; still
                                                  # fail-closed on the rest
"""

from fractions import Fraction as F
import argparse
import ast
import hashlib
import inspect
import os
import random
import re
import sys

VERSION = "1.5.1"
PAPER = "ZS-M66_v1_5_1.md"
PREDECESSOR_PAPER = "ZS-M66_v1_5.md"
EXPECTED_ROWS = 132

# Files this artifact supersedes.  The paper was released naming them; the
# guard G05 resolves the paper's companion references through this map so that
# consolidation does not silently break a published reference (row R14).
LEGACY_FILE_MAP = {
    "zs_m66_split_construction_v0_1.py": "blocks A, B of this file",
    "zs_m66_general_and_K2_v0_1.py": "blocks A, B, C of this file",
    "zs_m66_fermion_boundary_v0_1.py": "block D of this file",
    "zs_m66_cheshire_gate_v0_1.py": "block E of this file",
    "ZS-M66_v1_0_supplement.md": "block R of this file",
    "zs_m66_verify_v1_0.py": "superseded by this file; see rows R17-R19",
    "ZS-M66_v1_0.md": "superseded manuscript; see rows R17-R18",
    "zs_m66_verify_v1_1.py": "superseded by this file; see rows R21, G10",
    "ZS-M66_v1_1.md": "superseded manuscript; see rows R21-R22",
    "zs_m66_verify_v1_2.py": "superseded by this file; see rows R25, G10",
    "ZS-M66_v1_2.md": "superseded manuscript; see rows R25-R26",
    "zs_m66_verify_v1_3.py": "superseded by this file; see rows R27, G10",
    "ZS-M66_v1_3.md": "superseded manuscript; see rows R27-R28",
    "zs_m66_verify_v1_4.py": "superseded by this file; see rows R29, G10",
    "ZS-M66_v1_4.md": "superseded manuscript; see rows R29-R30",
    "zs_m66_verify_v1_5.py": "superseded by this file; see rows R31, G10",
    "ZS-M66_v1_5.md": "superseded manuscript; see row R31",
}

# The v1.0 ledger, frozen here so that row provenance is MEASURED and not
# asserted (VERIFY 11).  id -> class, as actually emitted by the v1.0 run.
V10_LEDGER = {
    "A01": "C", "A02": "C", "A03": "C", "A04": "C", "A05": "C", "A06": "C",
    "A07": "C", "A08": "W",
    "B01": "C", "B02": "C", "B03": "C", "B04": "C",
    "C01": "C", "C02": "C", "C03": "X", "C04": "C", "C05": "C", "C06": "C",
    "C07": "C", "C08": "C",
    "D01": "C", "D02": "C", "D03": "C", "D04": "C", "D05": "C", "D06": "C",
    "D07": "C", "D08": "C", "D09": "C", "D10": "C", "D11": "C", "D12": "C",
    "D13": "C", "D14": "C", "D15": "C", "D16": "C", "D17": "W", "D18": "C",
    "D19": "C",
    "E01": "C", "E02": "C", "E03": "C", "E04": "C", "E05": "C", "E06": "C",
    "E07": "C", "E08": "C",
    "S01": "C", "S02": "X", "S03": "X", "S04": "D",
    "G01": "G", "G02": "G", "G03": "G", "G04": "G", "G05": "G", "G06": "G",
    "G07": "G",
    "R01": "D", "R02": "D", "R03": "D", "R04": "D", "R05": "D", "R06": "D",
    "R07": "D", "R08": "D", "R09": "D", "R10": "D", "R11": "D", "R12": "D",
    "R13": "D", "R14": "D", "R15": "D", "R16": "D",
}

V11_LEDGER = {
    "A01": "C", "A02": "C", "A03": "C", "A04": "C", "A05": "C", "A06": "C",
    "A07": "C", "A08": "W", "A09": "C", "B01": "C", "B02": "C", "B03": "C",
    "B04": "C", "C01": "C", "C02": "C", "C03": "X", "C04": "C", "C05": "C",
    "C06": "C", "C07": "C", "C08": "C", "C09": "C", "D01": "C", "D02": "C",
    "D03": "C", "D04": "C", "D05": "C", "D06": "C", "D07": "C", "D08": "C",
    "D09": "C", "D10": "C", "D11": "C", "D12": "C", "D13": "C", "D14": "C",
    "D15": "C", "D16": "W", "D17": "W", "D18": "C", "D19": "C", "E01": "C",
    "E02": "C", "E03": "C", "E04": "C", "E05": "C", "E06": "C", "E07": "C",
    "E08": "C", "G01": "G", "G02": "G", "G03": "G", "G04": "G", "G05": "G",
    "G06": "G", "G07": "G", "G08": "G", "G09": "G", "G10": "G", "N01": "W",
    "N02": "W", "N03": "R", "N04": "C", "N05": "C", "N06": "C", "N07": "X",
    "R01": "D", "R02": "D", "R03": "D", "R04": "D", "R05": "D", "R06": "D",
    "R07": "D", "R08": "D", "R09": "D", "R10": "D", "R11": "D", "R12": "D",
    "R13": "D", "R14": "D", "R15": "D", "R16": "D", "R17": "D", "R18": "D",
    "R19": "D", "R20": "D", "S01": "C", "S02": "X", "S03": "X", "S04": "D"
}

# Rows whose class changed in v1.1.  A silent reclassification invalidates a
# census (VERIFY 2.2), so the change is declared here and row R19 measures it.
RETYPED_IN_V11 = {
    "D16": ("C", "W", "the row checks one matrix; the manuscript read it as "
                      "universal. The computation is unchanged, its class is "
                      "not: a witness is class W"),
}

V12_LEDGER = {
    "A01": "C", "A02": "C", "A03": "C", "A04": "C", "A05": "C", "A06": "C",
    "A07": "C", "A08": "W", "A09": "C", "A10": "C", "B01": "C", "B02": "C",
    "B03": "C", "B04": "C", "C01": "C", "C02": "C", "C03": "X", "C04": "C",
    "C05": "C", "C06": "C", "C07": "C", "C08": "C", "C09": "C", "D01": "C",
    "D02": "C", "D03": "C", "D04": "C", "D05": "C", "D06": "C", "D07": "C",
    "D08": "C", "D09": "C", "D10": "C", "D11": "C", "D12": "C", "D13": "C",
    "D14": "C", "D15": "C", "D16": "W", "D17": "W", "D18": "C", "D19": "C",
    "D20": "D", "E01": "C", "E02": "C", "E03": "C", "E04": "C", "E05": "C",
    "E06": "C", "E07": "C", "E08": "C", "G01": "G", "G02": "G", "G03": "G",
    "G04": "G", "G05": "G", "G06": "G", "G07": "G", "G08": "G", "G09": "G",
    "G10": "G", "G11": "G", "N01": "W", "N02": "W", "N03": "R", "N04": "C",
    "N05": "W", "N06": "C", "N07": "X", "N08": "W", "N09": "R", "N10": "C",
    "N11": "C", "N12": "C", "N13": "X", "R01": "D", "R02": "D", "R03": "D",
    "R04": "D", "R05": "D", "R06": "D", "R07": "D", "R08": "D", "R09": "D",
    "R10": "D", "R11": "D", "R12": "D", "R13": "D", "R14": "D", "R15": "D",
    "R16": "D", "R17": "D", "R18": "D", "R19": "D", "R20": "D", "R21": "D",
    "R22": "D", "R23": "D", "R24": "D", "S01": "C", "S02": "X", "S03": "X",
    "S04": "D"
}

# Rows whose class changed in v1.2.  Same discipline, one row: N05 computed a
# finite rational family and was cited for a surjectivity statement.  The
# statement is now a theorem (3.6) proved by an explicit construction, and the
# row is what it always was, a witness.
RETYPED_IN_V12 = {
    "N05": ("C", "W", "the row enumerates rational (p,q); the manuscript read "
                      "it as the whole open interval. Rationals are dense, not "
                      "onto. The universal statement is now Theorem 3.6, "
                      "certified by rows N10-N12; this row is a witness"),
}

V13_LEDGER = {
    "A01": "C", "A02": "C", "A03": "C", "A04": "C", "A05": "C", "A06": "C",
    "A07": "C", "A08": "W", "A09": "C", "A10": "C", "B01": "C", "B02": "C",
    "B03": "C", "B04": "C", "C01": "C", "C02": "C", "C03": "X", "C04": "C",
    "C05": "C", "C06": "C", "C07": "W", "C08": "W", "C09": "C", "C10": "D",
    "C11": "X", "D01": "C", "D02": "C", "D03": "C", "D04": "C", "D05": "C",
    "D06": "C", "D07": "C", "D08": "C", "D09": "C", "D10": "C", "D11": "C",
    "D12": "C", "D13": "C", "D14": "C", "D15": "C", "D16": "W", "D17": "W",
    "D18": "C", "D19": "C", "D20": "D", "E01": "C", "E02": "C", "E03": "C",
    "E04": "C", "E05": "C", "E06": "C", "E07": "C", "E08": "C", "G01": "G",
    "G02": "G", "G03": "G", "G04": "G", "G05": "G", "G06": "G", "G07": "G",
    "G08": "G", "G09": "G", "G10": "G", "G11": "G", "G12": "G", "N01": "W",
    "N02": "W", "N03": "R", "N04": "C", "N05": "W", "N06": "C", "N07": "X",
    "N08": "W", "N09": "R", "N10": "C", "N11": "C", "N12": "C", "N13": "X",
    "R01": "D", "R02": "D", "R03": "D", "R04": "D", "R05": "D", "R06": "D",
    "R07": "D", "R08": "D", "R09": "D", "R10": "D", "R11": "D", "R12": "D",
    "R13": "D", "R14": "D", "R15": "D", "R16": "D", "R17": "D", "R18": "D",
    "R19": "D", "R20": "D", "R21": "D", "R22": "D", "R23": "D", "R24": "D",
    "R25": "D", "R26": "D", "S01": "C", "S02": "X", "S03": "X", "S04": "D"
}

# Rows whose class changed in v1.3.  Both are the same defect: a computation
# over the terms we could write down was cited for a sentence quantified over
# the whole term list, and the list does not fix the scalar potential.
RETYPED_IN_V13 = {
    "C07": ("C", "W", "the row checks that |H_5|^2 and |dH_5|^2 structures are "
                      "reflection-even. It does not check the scalar "
                      "potential, whose symmetry the upstream action leaves "
                      "unspecified, so it is a witness over the terms we can "
                      "write, not a statement about every term"),
    "C08": ("C", "W", "the Yukawa is C-linear and that computation stands. "
                      "'The only term that can carry odd content' quantifies "
                      "over the same unfixed list, so the row is a witness"),
}

# No row changes class in v1.4.  The four defects round 4 found are statement
# defects, not computation defects, which is exactly why a passing run did not
# see them; row R27 records that and G13 guards the one that is a live claim.
V14_LEDGER = {
    "A01": "C", "A02": "C", "A03": "C", "A04": "C", "A05": "C", "A06": "C",
    "A07": "C", "A08": "W", "A09": "C", "A10": "C", "B01": "C", "B02": "C",
    "B03": "C", "B04": "C", "C01": "C", "C02": "C", "C03": "X", "C04": "C",
    "C05": "C", "C06": "C", "C07": "W", "C08": "W", "C09": "C", "C10": "D",
    "C11": "X", "D01": "C", "D02": "C", "D03": "C", "D04": "C", "D05": "C",
    "D06": "C", "D07": "C", "D08": "C", "D09": "C", "D10": "C", "D11": "C",
    "D12": "C", "D13": "C", "D14": "C", "D15": "C", "D16": "W", "D17": "W",
    "D18": "C", "D19": "C", "D20": "D", "E01": "C", "E02": "C", "E03": "C",
    "E04": "C", "E05": "C", "E06": "C", "E07": "C", "E08": "C", "G01": "G",
    "G02": "G", "G03": "G", "G04": "G", "G05": "G", "G06": "G", "G07": "G",
    "G08": "G", "G09": "G", "G10": "G", "G11": "G", "G12": "G", "G13": "G",
    "N01": "W", "N02": "W", "N03": "R", "N04": "C", "N05": "W", "N06": "C",
    "N07": "X", "N08": "W", "N09": "R", "N10": "C", "N11": "C", "N12": "C",
    "N13": "X", "Q01": "C", "Q02": "C", "Q03": "C", "Q04": "W", "Q05": "C",
    "Q06": "C", "Q07": "X", "Q08": "C", "Q09": "D", "Q10": "X", "R01": "D",
    "R02": "D", "R03": "D", "R04": "D", "R05": "D", "R06": "D", "R07": "D",
    "R08": "D", "R09": "D", "R10": "D", "R11": "D", "R12": "D", "R13": "D",
    "R14": "D", "R15": "D", "R16": "D", "R17": "D", "R18": "D", "R19": "D",
    "R20": "D", "R21": "D", "R22": "D", "R23": "D", "R24": "D", "R25": "D",
    "R26": "D", "R27": "D", "R28": "D", "S01": "C", "S02": "X", "S03": "X",
    "S04": "D"
}

RETYPED_IN_V14 = {}

# No row changes class in v1.5 either.  Round 5 found a scope overclaim in
# prose and five stale internal references; none of them is a computation.
V15_LEDGER = {
    "A01": "C", "A02": "C", "A03": "C", "A04": "C", "A05": "C", "A06": "C",
    "A07": "C", "A08": "W", "A09": "C", "A10": "C", "B01": "C", "B02": "C",
    "B03": "C", "B04": "C", "C01": "C", "C02": "C", "C03": "X", "C04": "C",
    "C05": "C", "C06": "C", "C07": "W", "C08": "W", "C09": "C", "C10": "D",
    "C11": "X", "D01": "C", "D02": "C", "D03": "C", "D04": "C", "D05": "C",
    "D06": "C", "D07": "C", "D08": "C", "D09": "C", "D10": "C", "D11": "C",
    "D12": "C", "D13": "C", "D14": "C", "D15": "C", "D16": "W", "D17": "W",
    "D18": "C", "D19": "C", "D20": "D", "E01": "C", "E02": "C", "E03": "C",
    "E04": "C", "E05": "C", "E06": "C", "E07": "C", "E08": "C", "G01": "G",
    "G02": "G", "G03": "G", "G04": "G", "G05": "G", "G06": "G", "G07": "G",
    "G08": "G", "G09": "G", "G10": "G", "G11": "G", "G12": "G", "G13": "G",
    "G14": "G", "G15": "G", "G16": "G", "G17": "G", "N01": "W", "N02": "W",
    "N03": "R", "N04": "C", "N05": "W", "N06": "C", "N07": "X", "N08": "W",
    "N09": "R", "N10": "C", "N11": "C", "N12": "C", "N13": "X", "Q01": "C",
    "Q02": "C", "Q03": "C", "Q04": "W", "Q05": "C", "Q06": "C", "Q07": "X",
    "Q08": "C", "Q09": "D", "Q10": "X", "Q11": "D", "Q12": "C", "Q13": "X",
    "R01": "D", "R02": "D", "R03": "D", "R04": "D", "R05": "D", "R06": "D",
    "R07": "D", "R08": "D", "R09": "D", "R10": "D", "R11": "D", "R12": "D",
    "R13": "D", "R14": "D", "R15": "D", "R16": "D", "R17": "D", "R18": "D",
    "R19": "D", "R20": "D", "R21": "D", "R22": "D", "R23": "D", "R24": "D",
    "R25": "D", "R26": "D", "R27": "D", "R28": "D", "R29": "D", "R30": "D",
    "S01": "C", "S02": "X", "S03": "X", "S04": "D"
}

# No row changes class in v1.5.1 either.  It is a correction-only version.
RETYPED_IN_V15 = {}
RETYPED_IN_V151 = {}


# ---------------------------------------------------------------- arithmetic
class G:
    """Gaussian rational a+ib, exact."""

    __slots__ = ("re", "im")

    def __init__(self, re, im=0):
        self.re, self.im = F(re), F(im)

    def __add__(self, o):
        o = o if isinstance(o, G) else G(o)
        return G(self.re + o.re, self.im + o.im)

    __radd__ = __add__

    def __sub__(self, o):
        o = o if isinstance(o, G) else G(o)
        return G(self.re - o.re, self.im - o.im)

    def __neg__(self):
        return G(-self.re, -self.im)

    def __mul__(self, o):
        o = o if isinstance(o, G) else G(o)
        return G(self.re * o.re - self.im * o.im, self.re * o.im + self.im * o.re)

    __rmul__ = __mul__

    def __eq__(self, o):
        o = o if isinstance(o, G) else G(o)
        return self.re == o.re and self.im == o.im

    def conj(self):
        return G(self.re, -self.im)

    def abs2(self):
        return self.re * self.re + self.im * self.im

    def __repr__(self):
        s = "+" if self.im >= 0 else "-"
        return f"{self.re}{s}{abs(self.im)}i"


Z, ONE, I_ = G(0), G(1), G(0, 1)


def eye(n):
    return [[ONE if i == j else Z for j in range(n)] for i in range(n)]


def zero(n, m=None):
    m = m or n
    return [[Z] * m for _ in range(n)]


def mm(a, b):
    n, p, m = len(a), len(b), len(b[0])
    return [[sum((a[i][t] * b[t][j] for t in range(p)), Z) for j in range(m)]
            for i in range(n)]


def pl(a, b):
    return [[a[i][j] + b[i][j] for j in range(len(a[0]))] for i in range(len(a))]


def mi(a, b):
    return [[a[i][j] - b[i][j] for j in range(len(a[0]))] for i in range(len(a))]


def sc(a, z):
    z = z if isinstance(z, G) else G(z)
    return [[z * x for x in r] for r in a]


def ad(a):
    return [[a[j][i].conj() for j in range(len(a))] for i in range(len(a[0]))]


def mv(a, v):
    return [sum((a[i][k] * v[k] for k in range(len(v))), Z) for i in range(len(a))]


def tr(a):
    return sum((a[i][i] for i in range(len(a))), Z)


def re_of(u):
    return [[x.re for x in r] for r in u]


def im_of(u):
    return [[x.im for x in r] for r in u]


def symm(m_):
    n = len(m_)
    return [[(m_[i][j] + m_[j][i]) / 2 for j in range(n)] for i in range(n)]


def rquad(m_, v):
    n = len(v)
    return sum(v[i] * m_[i][j] * v[j] for i in range(n) for j in range(n))


def expJ(c, s, Jm, n):
    """exp(i theta J) = cos I + i sin J, valid because J is an involution."""
    return pl(sc(eye(n), G(c)), sc(Jm, G(0, s)))


def su2(al, be):
    return [[al, be], [-be.conj(), al.conj()]]


def perm(p):
    n = len(p)
    M = zero(n)
    for i, pi in enumerate(p):
        M[pi][i] = ONE
    return M


def build_P(w):
    """P = I + w w^T : entrywise positive, PF ray w, top eigenvalue 1+|w|^2."""
    n = len(w)
    return [[(F(1) if i == j else F(0)) + w[i] * w[j] for j in range(n)]
            for i in range(n)]


def multiplier(U, w):
    n = len(w)
    num = sum((G(w[i]) * U[i][j] * G(w[j]) for i in range(n) for j in range(n)), Z)
    den = sum(x * x for x in w)
    return G(num.re / den, num.im / den)


# -------------------------------------------------------------- row ledger
ROWS = []


def row(rid, cls, name, cond, detail):
    ROWS.append({"id": rid, "class": cls, "name": name,
                 "ok": bool(cond), "detail": detail})


# =========================================================== BLOCK A : split
WS = {2: [F(1), F(1)], 3: [F(1), F(2), F(3)], 4: [F(1), F(1), F(2), F(3)],
      5: [F(2), F(1), F(3), F(1), F(2)], 6: [F(1), F(2), F(3), F(1), F(2), F(1)]}
SU = [su2(G(F(-3, 5)), G(F(12, 25), F(16, 25))),
      su2(G(F(5, 13)), G(F(36, 65), F(48, 65))),
      su2(G(F(0), F(3, 5)), G(F(4, 5)))]


def make_U(n, k):
    blocks, size = [], 0
    while size + 2 <= n:
        blocks.append(SU[(len(blocks) + k) % 3])
        size += 2
    M = zero(n)
    r = 0
    for B in blocks:
        for i in range(2):
            for j in range(2):
                M[r + i][r + j] = B[i][j]
        r += 2
    if size < n:
        M[n - 1][n - 1] = G(-1) if k % 2 else ONE
    return mm(perm([(i + 1) % n for i in range(n)]), M)


ok_pf = ok_uni = ok_id = True
for n in (2, 3, 4, 5, 6):
    w, P = WS[n], build_P(WS[n])
    nrm = sum(x * x for x in w)
    ok_pf &= all(P[i][j] > 0 for i in range(n) for j in range(n))
    ok_pf &= all(sum(P[i][j] * w[j] for j in range(n)) == (1 + nrm) * w[i]
                 for i in range(n))
    U = make_U(n, n)
    ok_uni &= mm(ad(U), U) == eye(n)
    a = multiplier(U, w)
    ok_id &= a.re == rquad(symm(re_of(U)), w) / nrm
    ok_id &= a.im == rquad(symm(im_of(U)), w) / nrm

row("A01", "C", "P = I + ww^T is entrywise positive with PF ray w", ok_pf,
    "dimensions 2,3,4,5,6; top eigenvalue 1+|w|^2, simple")
row("A02", "C", "test unitaries are exactly unitary", ok_uni,
    "cyclic permutation composed with SU(2) blocks; not block diagonal")
row("A03", "C", "paper 3.1 TWO-FORM IDENTITY in every tested dimension", ok_id,
    "Re a = w^T Sym(Re U) w / |w|^2 and Im a = w^T Sym(Im U) w / |w|^2")

n = 4
w = WS[n]
U = make_U(n, 4)
CUC = [[x.conj() for x in r] for r in U]
half = G(F(0), F(-1, 2))
num = sum((G(w[i]) * (half * (U[i][j] - CUC[i][j])) * G(w[j])
           for i in range(n) for j in range(n)), Z)
a4 = multiplier(U, w)
row("A04", "C", "operator form Im a = (1/2i)<psi|(U - CUC)|psi>",
    num.re == a4.im * sum(x * x for x in w) and num.im == 0,
    f"C is the conjugation fixing the cone basis; n=4, Im a = {a4.im}")

ok_real = True
for n in (3, 4, 5):
    w = WS[n]
    R1 = perm([(i + 1) % n for i in range(n)])
    ok_real &= multiplier(R1, w).im == 0
    ok_real &= multiplier(mm(R1, sc(eye(n), -1)), w).im == 0
row("A05", "C", "reality lock: U real orthogonal gives Im a = 0", ok_real,
    "arg a in {0, pi}; IMPORTED, see rows R03/R04")

ok_qd = True
for n in (3, 4, 5):
    w = WS[n]
    Uq = [[G(F(1, n)) for _ in range(n)] for _ in range(n)]
    ok_qd &= multiplier(Uq, w).re > 0
row("A06", "C", "quadrant: Sym(Re U) entrywise nonnegative and nonzero gives Re a > 0",
    ok_qd, "the PF ray has strictly positive entries so the form cannot cancel; IMPORTED")

ok_c1 = ok_c2 = True
for n in (2, 3, 4, 5, 6):
    w = WS[n]
    U = make_U(n, n)
    Uw = mv(U, [G(x) for x in w])
    par = all(Uw[i] * G(w[0]) == Uw[0] * G(w[i]) for i in range(n))
    a = multiplier(U, w)
    ok_c1 &= (a.abs2() == 1) if par else True
    ok_c2 &= (a.abs2() < 1) if not par else True
row("A07", "C", "contraction: |a| = 1 exactly when U psi0 is parallel to psi0",
    ok_c1 and ok_c2, "checked in every tested dimension; Cauchy-Schwarz")

al, be = G(F(-3, 5)), G(F(12, 25), F(16, 25))
Uw2 = su2(al, be)
aw2 = multiplier(Uw2, [F(1), F(1)])
row("A08", "W", "SU(2) witness closed form a = Re(alpha) + i Im(beta)",
    mm(ad(Uw2), Uw2) == eye(2) and aw2.re == al.re and aw2.im == be.im
    and aw2.abs2() == 1 - al.im * al.im - be.re * be.re,
    f"a = {aw2}, |a|^2 = {aw2.abs2()}; the multiplier reads two of the four "
    "real parameters and the deficit reads the other two")

# v1.1, audit finding P3.  The manuscript's paper-2 setting introduced psi0
# without fixing its length, then used sigma0 = |psi0><psi0| and
# kappa = <psi0|J|psi0| and Tr(Delta^2) = 2(1 - kappa^2), which are the
# NORMALISED formulas, while this file's multiplier() and kappa() divide by the
# squared norm.  The arithmetic agreed; the statements did not.  The manuscript
# now declares ||psi0|| = 1 throughout, and this row checks that the declaration
# is the only thing that was missing: both quantities are scale invariant, so
# the normalised formula and the divided form agree on every representative.
ok_n1 = ok_n2 = True
for n in (2, 3, 4, 5, 6):
    w = WS[n]
    U = make_U(n, n)
    base = multiplier(U, w)
    for c in (F(2), F(1, 3), F(7, 5)):
        scaled = [c * x for x in w]
        ok_n1 &= multiplier(U, scaled) == base
    nrm2 = sum(x * x for x in w)
    unit_form = sum(w[i] * w[i] for i in range(n)) / nrm2
    ok_n2 &= unit_form == 1
row("A09", "C", "normalisation: the multiplier is invariant under psi0 -> c "
    "psi0, so the normalised statement and the divided form agree",
    ok_n1 and ok_n2,
    "audit P3. Dimensions 2-6, three rational rescalings each. The manuscript "
    "declares ||psi0|| = 1 in its setting section; this row shows the "
    "declaration fixes a statement, not a number")

# ==================================================== BLOCK B : the dichotomy
ok_b, wit_b = True, None
for n in (2, 3, 4, 5, 6):
    P = build_P(WS[n])
    for pat in range(1, 2 ** n - 1):
        eps = [1 if (pat >> i) & 1 else -1 for i in range(n)]
        bad = [(i, j) for i in range(n) for j in range(n)
               if eps[i] != eps[j] and P[i][j] != 0]
        ok_b &= len(bad) > 0
        if wit_b is None:
            wit_b = (n, eps, bad[0])
row("B01", "C", "paper 3.2(b): J diagonal in the cone basis forces [P, J] != 0",
    ok_b, f"every non-central sign pattern, n = 2..6; e.g. {wit_b}")

ok_a = True
for n in (4, 6):
    w = [F(1)] * n
    Pg = [[G(x) for x in r] for r in build_P(w)]
    Jp = perm([n - 1 - i for i in range(n)])
    ok_a &= mm(Pg, Jp) == mm(Jp, Pg)
    ok_a &= [w[n - 1 - i] for i in range(n)] == w
row("B02", "C", "paper 3.2(a): J cone-preserving and commuting gives J psi0 = psi0",
    ok_a, "reversal permutation; the seam asymmetry of the selected state vanishes")

ok_k, ks = True, []
for n in (3, 4, 5):
    w = WS[n]
    nrm = sum(x * x for x in w)
    for pat in (1, 2, 5):
        eps = [1 if (pat >> i) & 1 else -1 for i in range(n)]
        kap = sum(eps[i] * w[i] * w[i] for i in range(n)) / nrm
        D = [[(1 - eps[i] * eps[j]) * w[i] * w[j] / nrm for j in range(n)]
             for i in range(n)]
        ok_k &= sum(D[i][j] * D[j][i] for i in range(n) for j in range(n)) \
            == 2 * (1 - kap * kap)
        ks.append(str(kap))
row("B03", "C", "paper 3.3 asymmetry budget Tr(Delta^2) = 2(1 - kappa^2)", ok_k,
    f"so T = sqrt(1 - kappa^2); kappa samples {ks[:4]}")
row("B04", "C", "maximal asymmetry exactly when the ray splits its mass evenly",
    sum([1, 1, -1, -1][i] * [F(1), F(2), F(2), F(1)][i] ** 2 for i in range(4)) == 0,
    "kappa = 0 iff sum_j eps_j psi_j^2 = 0")

# ============================================ BLOCK C : the scalar route dies
N6 = 6
circ = [F(7), F(3), F(2), F(1), F(2), F(3)]
Pc = [[circ[(j - i) % N6] for j in range(N6)] for i in range(N6)]
refl = [(-i) % N6 for i in range(N6)]
Jr = perm(refl)
Pcg = [[G(x) for x in r] for r in Pc]

row("C01", "C", "circle transfer: symmetric positive circulant is entrywise positive",
    all(Pc[i][j] > 0 for i in range(N6) for j in range(N6)),
    "positivity improving on the cone of positive functions")
row("C02", "C", "paper 4: the reflection preserves the cone, so 3.2(a) fires",
    mm(Pcg, Jr) == mm(Jr, Pcg)
    and all(sum(Pc[i][j] for j in range(N6)) == sum(circ) for i in range(N6)),
    "[P, J] = 0 and the PF ray is the constant function: J psi0 = psi0, Delta = 0")


def iterate(Pm, x, steps):
    out = [x]
    for _ in range(steps):
        x = [sum(Pm[i][j] * x[j] for j in range(len(x))) for i in range(len(x))]
        out.append(x)
    return out


def jsym(x):
    return all(x[i] == x[refl[i]] for i in range(len(x)))


v_even = [F(5), F(3), F(2), F(4), F(2), F(3)]
Pe = [[v_even[i] * Pc[i][j] * v_even[j] for j in range(N6)] for i in range(N6)]
it_e = iterate(Pe, [F(1)] * N6, 4)
row("C03", "X", "an EVEN boundary weight does not open the lock",
    mm([[G(x) for x in r] for r in Pe], Jr) == mm(Jr, [[G(x) for x in r] for r in Pe])
    and all(jsym(x) for x in it_e),
    "every power iterate stays reflection symmetric, so the PF ray is invariant")

v_odd = [F(5), F(3), F(2), F(4), F(2), F(7)]
Po = [[v_odd[i] * Pc[i][j] * v_odd[j] for j in range(N6)] for i in range(N6)]
it_o = iterate(Po, [F(1)] * N6, 4)
row("C04", "C", "a REFLECTION-BREAKING boundary weight is exactly what opens it",
    mm([[G(x) for x in r] for r in Po], Jr) != mm(Jr, [[G(x) for x in r] for r in Po])
    and not any(jsym(x) for x in it_o[1:]),
    "[P, J] != 0 and no power iterate is reflection symmetric. Audit P4: the "
    "row name said ODD, which is a type error. v_odd is a POSITIVE weight and "
    "cannot satisfy Jv = -v; what it has is a nonzero odd component. The "
    "manuscript and this row now say reflection-breaking")

xe, xo = it_e[-1], it_o[-1]
ke = sum(xe[i] * xe[refl[i]] for i in range(N6)) / sum(x * x for x in xe)
ko = sum(xo[i] * xo[refl[i]] for i in range(N6)) / sum(x * x for x in xo)
row("C05", "C", "the asymmetry budget separates the two cases",
    ke == 1 and ko < 1, f"kappa_even = {ke} (Delta = 0), kappa_odd < 1")

ph_a = G(F(3, 5), F(4, 5))
SAMP = [G(F(2, 3), F(1, 5)), G(F(-1, 4), F(7, 8)), G(F(1)), G(F(0), F(3, 2))]
row("C06", "C", "the field-plane reflection is an exact involution on the unit circle",
    ph_a.abs2() == 1, "J_alpha : Phi -> e^{2i alpha} conj(Phi)")
row("C07", "W", "WITNESS: the |H_5|^2 and |dH_5|^2 structures of the printed "
    "list are J_alpha-EVEN. RETYPED IN v1.3 FROM CLASS C",
    all((ph_a * z.conj()).abs2() == z.abs2() for z in SAMP),
    "the curvature coupling, the two kinetic terms and the "
    "Gibbons-Hawking-York term forced on a manifold with boundary depend "
    "on H_5 only through |H_5|^2 or |dH_5|^2 and are therefore even. THE "
    "SCALAR POTENTIAL IS NOT COVERED: v1.2 listed it here, but the "
    "upstream action does not specify V(H_5, H), and the same manuscript "
    "registers the CP^4 direction of the H_5 vacuum as an unfixed debt, "
    "which is only meaningful if V is unspecified. See row C10")
row("C08", "W", "WITNESS: the Yukawa term is C-linear, hence not J_alpha-"
    "covariant. RETYPED IN v1.3 FROM CLASS C",
    any((ph_a * z.conj()) != z and (ph_a * z.conj()) != -z for z in SAMP),
    "it has no derivative of H_5, so it contributes no scalar boundary "
    "term. v1.2 also called it the only term that can carry odd content; "
    "that quantifier ranges over a list whose potential is unspecified, "
    "so it is withdrawn. See row C10 and gate F-M66.14")

# v1.1, audit finding P4.  The weight that opens the lock is not an odd vector.
# It is a strictly positive vector whose decomposition into the +1 and -1
# eigenspaces of the reflection has a nonzero -1 part.  A strictly positive
# vector can never satisfy Jv = -v, so the v1.0 phrasing named a class that is
# empty.  This row exhibits the correct type and shows the empty one is empty.
v_odd_part = [(v_odd[i] - v_odd[refl[i]]) / 2 for i in range(N6)]
v_even_part = [(v_even[i] - v_even[refl[i]]) / 2 for i in range(N6)]
row("C09", "C", "TYPE CORRECTION: the opening weight is positive with a "
    "nonzero odd component, and is NOT an odd vector",
    all(x > 0 for x in v_odd)
    and any(x != 0 for x in v_odd_part)
    and any(v_odd[i] != -v_odd[i] for i in range(N6))
    and all(x == 0 for x in v_even_part),
    f"odd component of the opening weight = {v_odd_part}, nonzero; odd "
    f"component of the even weight = {v_even_part}, zero. No strictly "
    "positive vector satisfies Jv = -v, so 'only an odd weight opens the lock' "
    "quantified over an empty class")

# ================================================ BLOCK D : fermion boundary
I2 = eye(2)
S1_ = [[Z, ONE], [ONE, Z]]
S2_ = [[Z, G(0, -1)], [I_, Z]]
S3_ = [[ONE, Z], [Z, G(-1)]]
O2 = zero(2)


def blk(A, B, C_, D_):
    return [[A[0][0], A[0][1], B[0][0], B[0][1]],
            [A[1][0], A[1][1], B[1][0], B[1][1]],
            [C_[0][0], C_[0][1], D_[0][0], D_[0][1]],
            [C_[1][0], C_[1][1], D_[1][0], D_[1][1]]]


g0 = blk(O2, I2, I2, O2)
g1 = blk(O2, S1_, sc(S1_, -1), O2)
g2 = blk(O2, S2_, sc(S2_, -1), O2)
g3 = blk(O2, S3_, sc(S3_, -1), O2)
gam, metric = [g0, g1, g2, g3], [1, -1, -1, -1]
g5 = sc(mm(mm(g0, g1), mm(g2, g3)), I_)

row("D01", "C", "Clifford algebra {gamma^mu, gamma^nu} = 2 g^{mu nu}",
    all(pl(mm(gam[m], gam[k]), mm(gam[k], gam[m]))
        == sc(eye(4), 2 * metric[m] if m == k else 0)
        for m in range(4) for k in range(4))
    and ad(g0) == g0 and ad(g3) == sc(g3, -1),
    "chiral representation, signature (+,-,-,-)")
row("D02", "C", "gamma5 = i g0 g1 g2 g3 = diag(-1,-1,+1,+1), an involution "
    "anticommuting with every gamma^mu",
    mm(g5, g5) == eye(4)
    and all(pl(mm(g5, gam[m]), mm(gam[m], g5)) == zero(4) for m in range(4))
    and [g5[i][i] for i in range(4)] == [G(-1), G(-1), ONE, ONE], "chirality")

N4 = mm(g0, g3)
row("D03", "C", "boundary form psi^dag N chi, N = gamma0 gamma3: Hermitian, "
    "N^2 = I, tr N = 0, signature (2,2)",
    ad(N4) == N4 and mm(N4, N4) == eye(4) and tr(N4) == Z,
    f"N = diag{[N4[i][i] for i in range(4)]}")
row("D04", "C", "CORRECTION: [N, gamma5] = 0 - the boundary form is chirality "
    "DIAGONAL", mi(mm(N4, g5), mm(g5, N4)) == zero(4),
    "it is the normal vector current, which preserves chirality; the "
    "chirality-flipping bilinear is the mass term. Our earlier expectation was "
    "the opposite and this row refuted it. See row R05 item C1")

Ep = [i for i in range(4) if N4[i][i] == ONE]
Em = [i for i in range(4) if N4[i][i] == G(-1)]
JE = [[g5[i][j] for j in Ep] for i in Ep]
row("D05", "C", "paper 5.1: E+ is 2-dimensional and mixes chirality, so "
    "J_E = gamma5|_{E+} = diag(-1,+1) is a NON-CENTRAL involution",
    len(Ep) == 2 and len(Em) == 2 and JE == [[G(-1), Z], [Z, ONE]]
    and mm(JE, JE) == eye(2) and JE != eye(2) and JE != sc(eye(2), -1),
    f"E+ basis {Ep}: one left-handed and one right-handed component. This one "
    "object meets the three environment requirements at once: dimension two, "
    "non-central involution, outside the register. IMPORTED - see R03/R04")

c_t, s_t = F(-3, 5), F(4, 5)
E5 = expJ(c_t, s_t, g5, 4)
Mth = mm(sc(g3, G(0, -1)), E5)
Pi = sc(pl(eye(4), Mth), F(1, 2))

row("D06", "C", "exp(i theta gamma5) = cos I + i sin gamma5 is exactly unitary",
    mm(ad(E5), E5) == eye(4) and c_t * c_t + s_t * s_t == 1,
    f"rational (cos, sin) = ({c_t}, {s_t})")
row("D07", "C", "M_theta = -i gamma3 exp(i theta gamma5) is a Hermitian "
    "involution with vanishing trace",
    ad(Mth) == Mth and mm(Mth, Mth) == eye(4) and tr(Mth) == Z,
    "the chiral-bag condition psi = M_theta psi; IMPORTED verbatim, see R03")
row("D08", "C", "{N, M_theta} = 0, so range(Pi) is maximal isotropic: the "
    "boundary condition is self-adjoint",
    pl(mm(N4, Mth), mm(Mth, N4)) == zero(4)
    and mm(mm(Pi, N4), Pi) == zero(4) and mm(Pi, Pi) == Pi and tr(Pi) == G(2),
    "the full moduli space is U(2); the chiral-bag family is a U(1) inside it")

phth = G(c_t, s_t)
Wth = [[Z, G(0, -1) * phth], [G(0, -1) * phth.conj(), Z]]
graph_ok = True
for k in range(2):
    x = [ONE if j == k else Z for j in range(2)]
    wx = [sum((Wth[i][j] * x[j] for j in range(2)), Z) for i in range(2)]
    v = [Z] * 4
    for aa, ii in zip(x, Ep):
        v[ii] = aa
    for aa, ii in zip(wx, Em):
        v[ii] = aa
    graph_ok &= mv(Mth, v) == v
row("D09", "C", "the boundary condition is the graph of a unitary E+ -> E-",
    graph_ok and mm(ad(Wth), Wth) == eye(2),
    "W_theta = [[0, -i e^{i t}], [-i e^{-i t}, 0]], checked on a basis of E+")

g0r = [[g0[i][j] for j in Ep] for i in Em]
Uth = sc(mm(g0r, Wth), I_)
row("D10", "C", "paper 5.2: after the declared normalisation the boundary "
    "unitary is exactly U_theta = exp(i theta J_E)",
    g0r == [[Z, ONE], [ONE, Z]] and Uth == expJ(c_t, s_t, JE, 2)
    and mm(ad(Uth), Uth) == eye(2),
    "the phase is generated by the grading itself")


def kappa(psi):
    d = sum(x * x for x in psi)
    return sum(psi[i] * JE[i][i].re * psi[i] for i in range(2)) / d


PSIS = [[F(1), F(2)], [F(3), F(1)], [F(2), F(5)], [F(1), F(1)], [F(7), F(4)]]
ok_m1 = ok_m2 = ok_m3 = True
det_m = []
imU = [[x.im for x in r] for r in Uth]
for psi in PSIS:
    a = multiplier(Uth, psi)
    k = kappa(psi)
    ok_m1 &= a.re == c_t and a.im == k * s_t
    ok_m2 &= 1 - a.abs2() == (1 - k * k) * s_t * s_t
    ok_m3 &= rquad(imU, psi) / sum(x * x for x in psi) == a.im
    det_m.append(f"kappa={k}, a={a}")
row("D11", "C", "paper 5.3 multiplier a(theta) = cos theta + i kappa sin theta",
    ok_m1, "; ".join(det_m[:3]))
row("D12", "C", "paper 5.3 THE FACTORISATION 1 - |a|^2 = (1 - kappa^2) sin^2 "
    "theta = T^2 sin^2 theta", ok_m2,
    "the contraction deficit splits into the state's contribution and the "
    "boundary condition's contribution")
row("D13", "C", "the two-form identity realised on the actual boundary unitary",
    ok_m3, "Im(U) entrywise is sin(theta) J_E, real symmetric, so "
           "Im a = psi^T Sym(Im U) psi = kappa sin theta")
row("D14", "C", "the two axes are carried by different objects",
    multiplier(Uth, [F(1), F(1)]).im == 0
    and multiplier(Uth, [F(1), F(1)]).re == c_t
    and multiplier(expJ(F(1), F(0), JE, 2), [F(1), F(2)]).im == 0,
    "Re a = cos theta is the boundary condition alone; Im a = kappa sin theta "
    "dies if either factor dies")

wpf = [F(1), F(2)]
Ppf = build_P(wpf)
comm = mi(mm([[G(x) for x in r] for r in Ppf], JE),
          mm(JE, [[G(x) for x in r] for r in Ppf]))
kpf = kappa(wpf)
row("D15", "C", "paper 5.3: J_E is diagonal in the boundary basis, so 3.2(b) "
    "fires and [P, J_E] != 0 is forced",
    comm != zero(2) and all(Ppf[i][j] > 0 for i in range(2) for j in range(2)),
    "the aligned case (b) fires here, whereas case (a) fired on the "
    "vacuum circle. ALIGNMENT-CLASS-3: the two cases are sufficient "
    "conditions and are not exhaustive")
row("D16", "W", "WITNESS ONLY: for THIS transfer operator the PF ray lands in "
    "the usable window 0 < |kappa| < 1",
    0 < abs(kpf) < 1 and (1 - kpf * kpf) > 0
    and all(Ppf[i][j] > 0 for i in range(2) for j in range(2)),
    f"kappa = {kpf} for P built from w = {wpf}. RETYPED IN v1.1 FROM CLASS C. "
    "The computation is unchanged and correct. What changed is its class and "
    "what may be read off it: v1.0 read this single witness as a property of "
    "every positivity-improving P and printed that reading in the abstract, "
    "the introduction and paper 5.3. It is false. See rows N01-N04 for the "
    "exact counterexample and for the half of the statement that survives")
wit = multiplier(Uth, wpf)
row("D17", "W", "second-quadrant strictly contractive instance",
    wit.re < 0 and wit.im > 0 and 0 < wit.abs2() < 1 and comm != zero(2),
    f"a = {wit}, |a|^2 = {wit.abs2()}; no locked constant is used. What this "
    "shows is nonemptiness only - see row S04")

cb, sb = F(3, 5), F(4, 5)
c2b, s2b = cb * cb - sb * sb, 2 * cb * sb
Eb, Ebi = expJ(cb, sb, g5, 4), expJ(cb, -sb, g5, 4)
cs, ss = c_t * c2b + s_t * s2b, s_t * c2b - c_t * s2b
row("D18", "C", "a chiral rotation maps M_theta to M_{theta - 2 beta}",
    mm(mm(Eb, Mth), Ebi) == mm(sc(g3, G(0, -1)), expJ(cs, ss, g5, 4))
    and cs * cs + ss * ss == 1, f"exact double angle ({c2b}, {s2b})")
row("D19", "C", "paper 6: the same rotation shifts the mass phase by +2 beta, "
    "so only Delta = theta + theta_m is invariant",
    mm(mm(Eb, expJ(F(0), F(1), g5, 4)), Eb) == expJ(-s2b, c2b, g5, 4),
    "psibar picks up the same sign as psi, so the mass phase adds while the "
    "boundary angle subtracts")

# ============================================= BLOCK E : the Cheshire gate
Nd = [G(-1), ONE, ONE, G(-1)]
G5d = [G(-1), G(-1), ONE, ONE]
NG5 = [Nd[i] * G5d[i] for i in range(4)]
ANGLES = [(F(1), F(0)), (F(-1), F(0)), (F(3, 5), F(4, 5)), (F(-3, 5), F(4, 5)),
          (F(5, 13), F(12, 13)), (F(-12, 13), F(5, 13)), (F(-7, 25), F(24, 25))]


def sesq(diag, a, b):
    return sum((a[i].conj() * diag[i] * b[i] for i in range(4)), Z)


def basis_V(c, s):
    ph = G(c, s)
    return ([Z, ONE, Z, G(0, -1) * ph.conj()], [G(0, -1) * ph, Z, ONE, Z])


row("E01", "C", "seven exact rational angles including theta = 0 (MIT) and pi",
    all(c * c + s * s == 1 for c, s in ANGLES) and len(ANGLES) == 7,
    "N and gamma5 are diagonal involutions in this representation")
ok_bc = True
for c, s in ANGLES:
    ph = G(c, s)
    for p in basis_V(c, s):
        ok_bc &= p[0] == G(0, -1) * ph * p[2] and p[3] == G(0, -1) * ph.conj() * p[1]
row("E02", "C", "the two vectors satisfy the chiral-bag condition", ok_bc,
    "u1 = -i e^{it} v1 and v2 = -i e^{-it} u2 at every angle")
row("E03", "C", "they are orthogonal with squared norm 2",
    all(sum((p1[i].conj() * p2[i] for i in range(4)), Z) == Z
        and all(sum((p[i].conj() * p[i] for i in range(4)), Z) == G(2)
                for p in (p1, p2))
        for p1, p2 in (basis_V(c, s) for c, s in ANGLES)),
    "explicit orthogonal basis of the 2-dimensional boundary subspace")

ok_vec = all(sesq(Nd, a, b) == Z
             for c, s in ANGLES for a in basis_V(c, s) for b in basis_V(c, s))
row("E04", "C", "paper 5.4: THE VECTOR FLUX VANISHES IDENTICALLY", ok_vec,
    "psi^dag N chi = 0 - this IS the isotropy condition. Nothing charged "
    "leaks; the boundary confines and needs no exterior to absorb it")

axmats = []
for c, s in ANGLES:
    p1, p2 = basis_V(c, s)
    A = [[sesq(NG5, a, b) for b in (p1, p2)] for a in (p1, p2)]
    axmats.append([[G(x.re / 2, x.im / 2) for x in r] for r in A])
row("E05", "C", "paper 5.4: THE AXIAL FLUX DOES NOT VANISH",
    all(A[0][0] == G(-1) and A[1][1] == ONE and A[0][1] == Z and A[1][0] == Z
        for A in axmats),
    "N gamma5 restricts, in the graph basis, to diag(-1, +1)")
row("E06", "C", "and it leaks at EVERY angle, including theta = 0 and pi",
    all(A == axmats[0] for A in axmats),
    "bag boundary conditions break the axial symmetry for every member of the "
    "family; IMPORTED, recomputed here")
row("E07", "C", "THE AXIAL BOUNDARY FLUX IS THE GRADING",
    axmats[0] == [[G(-1), Z], [Z, ONE]],
    "the odd resource the programme demands is the axial boundary flux of the "
    "confined fermion")
row("E08", "C", "the two fluxes are different objects on the same subspace, "
    "although [N, gamma5] = 0",
    ok_vec and any(sesq(NG5, p, p) != Z for c, s in ANGLES for p in basis_V(c, s)),
    "vector current confined, axial current leaking")

# ================================================== BLOCK S : adversarial
random.seed(66)
sweep_bad = []
TRIS = [(F(3, 5), F(4, 5)), (F(-3, 5), F(4, 5)), (F(5, 13), F(12, 13)),
        (F(-12, 13), F(5, 13)), (F(-7, 25), F(24, 25)), (F(20, 29), F(21, 29)),
        (F(1), F(0)), (F(-1), F(0)), (F(0), F(1))]
for c, s in TRIS:
    for _ in range(200):
        p = [F(random.randint(1, 40)), F(random.randint(1, 40))]
        k = (-p[0] * p[0] + p[1] * p[1]) / (p[0] * p[0] + p[1] * p[1])
        re_, im_ = c, k * s
        if 1 - (re_ * re_ + im_ * im_) != (1 - k * k) * s * s:
            sweep_bad.append(("identity", c, s))
        if (re_ < 0 and im_ > 0) != (c < 0 and k * s > 0):
            sweep_bad.append(("quadrant", c, s))
        if ((re_ * re_ + im_ * im_) < 1) != (s != 0 and abs(k) < 1):
            sweep_bad.append(("contraction", c, s))
row("S01", "C", "adversarial sweep: nine exact angles x 200 rational states",
    len(sweep_bad) == 0,
    "the factorisation and the two equivalences hold with zero counterexamples")
row("S02", "X", "a seam-balanced state kills the phase at every angle",
    all(F(0) * s == 0 for c, s in TRIS), "kappa = 0 forces Im a = 0")
row("S03", "X", "a fully polarised state kills the contraction at every angle",
    all(c * c + F(1) * s * F(1) * s == 1 for c, s in TRIS),
    "|kappa| = 1 forces |a| = 1")
row("S04", "D", "IDENTIFIABILITY DECLARATION",
    True is not False,
    "Re a = cos theta covers (-1,1) and Im a = kappa sin theta covers "
    "(-|sin|,|sin|), so the pair (theta, kappa) reaches every point of the "
    "open unit disc. The witness of row D17 shows the class is nonempty and "
    "shows nothing about selection. Matching a two-real-parameter target with "
    "two free real parameters is identification, not derivation. This is the "
    "failure a previous line of this corpus was withdrawn for")

# ======================================== BLOCK N : the counterexample, v1.1
# Audit finding P1, severity S3.  v1.0 asserted, from the grading-cone
# dichotomy plus positivity, that the Perron-Frobenius ray automatically
# carries 0 < |kappa| < 1.  Only |kappa| < 1 follows.  kappa != 0 does not.

JN = [[F(-1), F(0)], [F(0), F(1)]]


def commutes(Pm, Jm):
    n = len(Pm)
    PJ = [[sum(Pm[i][k] * Jm[k][j] for k in range(n)) for j in range(n)]
          for i in range(n)]
    JP = [[sum(Jm[i][k] * Pm[k][j] for k in range(n)) for j in range(n)]
          for i in range(n)]
    return PJ == JP, [[PJ[i][j] - JP[i][j] for j in range(n)] for i in range(n)]


def kap(psi, Jm):
    return (sum(psi[i] * Jm[i][i] * psi[i] for i in range(len(psi)))
            / sum(x * x for x in psi))


def build_with_ray(p, q, lam):
    """Symmetric 2x2, entrywise positive, with (p, q) as its PF ray."""
    return [[lam - q / p, F(1)], [F(1), lam - p / q]]


PX = [[F(2), F(1)], [F(1), F(2)]]
psiX = [F(1), F(1)]
PX_psi = [sum(PX[i][j] * psiX[j] for j in range(2)) for i in range(2)]
comm_ok, comm_X = commutes(PX, JN)
kapX = kap(psiX, JN)
JpsiX = [JN[i][i] * psiX[i] for i in range(2)]
TX2 = 1 - kapX * kapX

row("N01", "W", "COUNTEREXAMPLE to the withdrawn implication: a positivity-"
    "improving P whose PF ray has kappa = 0",
    all(PX[i][j] > 0 for i in range(2) for j in range(2))
    and PX_psi == [3 * x for x in psiX]
    and (not comm_ok)
    and JpsiX != psiX and JpsiX != [-x for x in psiX]
    and kapX == 0,
    f"P = {[[str(x) for x in r] for r in PX]}, J = diag(-1,+1). Entrywise "
    f"positive; P psi = {[str(x) for x in PX_psi]} = 3 psi so the PF ray is "
    f"(1,1); [P,J] = {[[str(x) for x in r] for r in comm_X]} != 0; J psi != "
    f"+-psi so Delta != 0; and yet kappa = {kapX}")

phase_dead = [kapX * s == 0 for c, s in ANGLES]
deficit = [(1 - (c * c + (kapX * s) * (kapX * s)), TX2 * s * s)
           for c, s in ANGLES]
row("N02", "W", "on that same operator the seam asymmetry is MAXIMAL and the "
    "phase is zero at every angle",
    TX2 == 1 and all(phase_dead)
    and all(lhs == rhs for lhs, rhs in deficit)
    and any(lhs != 0 for lhs, rhs in deficit),
    f"T^2 = 1 - kappa^2 = {TX2}, its maximum, so the contraction deficit "
    "1 - |a|^2 = T^2 sin^2 theta is as large as the model allows; but "
    "a(theta) = cos theta + i kappa sin theta = cos theta is REAL at all "
    f"{len(ANGLES)} exact angles. Delta != 0 does not give Im a != 0")

equal_diag = [(F(a), F(b)) for a in range(1, 9) for b in range(1, 9) if a > b]
locus_ok = True
for a, b in equal_diag:
    Pl = [[a, b], [b, a]]
    ray = [F(1), F(1)]
    Pr = [sum(Pl[i][j] * ray[j] for j in range(2)) for i in range(2)]
    locus_ok &= Pr == [(a + b) * x for x in ray] and kap(ray, JN) == 0
    locus_ok &= all(Pl[i][j] > 0 for i in range(2) for j in range(2))
    locus_ok &= not commutes(Pl, JN)[0]
row("N03", "R", "REGRESSION: the failure is a whole locus, not one accident - "
    "every positivity-improving symmetric P with equal diagonal has kappa = 0",
    locus_ok and len(equal_diag) == 28,
    f"{len(equal_diag)} exact rational instances P = [[a,b],[b,a]], a > b > 0. "
    "In each, P is entrywise positive, [P,J] != 0 fires, the PF ray is (1,1) "
    "with eigenvalue a+b, and kappa = 0. This row exists so that the "
    "withdrawn implication cannot be reintroduced by a later edit without a "
    "failing row")

surv_ok = True
surv_min, surv_max = None, None
random.seed(1166)
for n in (2, 3, 4, 5, 6):
    Jd = [[F(0)] * n for _ in range(n)]
    for i in range(n):
        Jd[i][i] = F(-1) if i % 2 == 0 else F(1)
    for _ in range(60):
        ray = [F(random.randint(1, 30)) for _ in range(n)]
        lam = F(sum(ray) * 40)
        Pm = [[F(1)] * n for _ in range(n)]
        for i in range(n):
            Pm[i][i] = (lam * ray[i] - sum(ray) + ray[i]) / ray[i]
        chk = [sum(Pm[i][j] * ray[j] for j in range(n)) for i in range(n)]
        surv_ok &= all(Pm[i][j] > 0 for i in range(n) for j in range(n))
        surv_ok &= chk == [lam * x for x in ray]
        k = kap(ray, Jd)
        surv_ok &= abs(k) < 1
        surv_min = k if surv_min is None or k < surv_min else surv_min
        surv_max = k if surv_max is None or k > surv_max else surv_max
row("N04", "C", "THE HALF THAT SURVIVES: |kappa| < 1 strictly, for every "
    "positivity-improving P with a non-central diagonal grading",
    surv_ok,
    f"300 exact rational operators, dimensions 2-6, each built to have a "
    f"prescribed strictly positive PF ray and verified entrywise positive. "
    f"kappa ranged over [{surv_min}, {surv_max}], always strictly inside "
    "(-1,1). Strict positivity of every component in both eigenspaces gives "
    "|kappa| < 1 and hence Delta != 0 and T > 0. It gives nothing more")

reach, reach_ok = [], True
for p in range(1, 13):
    for q in range(1, 13):
        pp, qq = F(p), F(q)
        lam = F(2) * (pp / qq + qq / pp) + 2
        Pm = build_with_ray(pp, qq, lam)
        chk = [sum(Pm[i][j] * [pp, qq][j] for j in range(2)) for i in range(2)]
        reach_ok &= all(Pm[i][j] > 0 for i in range(2) for j in range(2))
        reach_ok &= chk == [lam * pp, lam * qq]
        k = kap([pp, qq], JN)
        reach_ok &= k == (qq * qq - pp * pp) / (qq * qq + pp * pp)
        reach.append(k)
row("N05", "W", "WITNESS ONLY: a rational family realising kappa = (q^2-p^2)/"
    "(q^2+p^2). RETYPED IN v1.2 FROM CLASS C; rationals are dense, not onto",
    reach_ok and F(0) in reach and min(reach) < F(-9, 10)
    and max(reach) > F(9, 10) and len(set(reach)) > 40,
    f"{len(reach)} exact instances from p,q in 1..12. P = [[lam - q/p, 1], "
    "[1, lam - p/q]] is entrywise positive with PF ray (p,q) for lam large "
    f"enough. Realised kappa includes 0 and reaches [{min(reach)}, "
    f"{max(reach)}]. Surjectivity onto the whole open interval is the "
    "manuscript's one-line continuity argument, not this row: t -> "
    "(1-t^2)/(1+t^2) is a continuous bijection (0,inf) -> (-1,1)")

# kappa = 0 means the PF ray splits its mass evenly, which for J = diag(-1,+1)
# means the ray is (1,1) up to scale, which by uniqueness of the PF ray means
# (1,1) is an eigenvector, which for a symmetric P is a + b = b + c.  Every
# step is rational, so no square root enters and the check stays exact.
iff_ok, iff_n, iff_zero = True, 0, 0
for a in range(1, 9):
    for b in range(1, 9):
        for c in range(1, 9):
            Pm = [[F(a), F(b)], [F(b), F(c)]]
            img = [sum(Pm[i][j] for j in range(2)) for i in range(2)]
            ray_is_flat = (img[0] == img[1])
            iff_ok &= (ray_is_flat == (a == c))
            iff_ok &= all(Pm[i][j] > 0 for i in range(2) for j in range(2))
            if ray_is_flat:
                iff_zero += 1
                iff_ok &= kap([F(1), F(1)], JN) == 0
                iff_ok &= img == [F(a + b), F(a + b)]
            else:
                iff_ok &= img[0] * F(1) != img[1] * F(1)
            iff_n += 1
row("N06", "C", "the kappa = 0 locus for symmetric 2x2 positivity-improving "
    "operators is exactly the equal-diagonal locus",
    iff_ok and iff_n == 512 and iff_zero == 64,
    f"{iff_n} exact instances P = [[a,b],[b,c]], a,b,c in 1..8; {iff_zero} of "
    "them lie on the locus. kappa = 0 iff the PF ray splits evenly iff (1,1) "
    "is an eigenvector iff a = c. The locus is codimension one in the "
    "parameter space, which is why one sampled witness misses it, and why a "
    "sampled sweep never establishes a universal statement")

row("N07", "X", "the two survival properties come apart precisely at the "
    "maximally asymmetric point",
    kapX == 0 and TX2 == 1
    and all(kap([F(1), F(t)], JN) != 0 for t in (2, 3, 5))
    and all(abs(kap([F(1), F(t)], JN)) < 1 for t in (2, 3, 5)),
    "Delta != 0 (equivalently T > 0) holds on the whole dichotomy branch. "
    "Im a != 0 requires kappa != 0, which fails exactly where T is largest. "
    "Seam-asymmetry survival and phase survival are different questions")

# ====================================================== BLOCK G : guards
SRC = inspect.getsource(sys.modules[__name__])
FORBIDDEN_TOKENS = ["688" + "453227", "566" + "417330", "763" + "362818",
                    "891" + "513565", "225" + "9249553", "49" + "/625"]
row("G01", "G", "locked-constant token scan over this source",
    not any(t in SRC for t in FORBIDDEN_TOKENS),
    f"{len(FORBIDDEN_TOKENS)} decimal fragments of locked project values and "
    "inherited thresholds are excluded from the construction layer")


def ast_defects(source):
    """Evidence rows must compute.  Returns (row_id, defect) pairs."""
    out = []
    tree = ast.parse(source)
    for nd in ast.walk(tree):
        if isinstance(nd, ast.Call) and getattr(nd.func, "id", "") == "row" \
                and len(nd.args) >= 4:
            try:
                rid = ast.literal_eval(nd.args[0])
                cls = ast.literal_eval(nd.args[1])
            except Exception:
                continue
            if cls not in ("C", "W", "X"):
                continue
            cond = nd.args[3]
            nodes = [x for x in ast.walk(cond)
                     if isinstance(x, (ast.Name, ast.Call, ast.Attribute,
                                       ast.Subscript, ast.comprehension))]
            if not nodes:
                out.append((rid, "constant fold"))
            if isinstance(cond, ast.Compare) and len(cond.comparators) == 1 \
                    and ast.dump(cond.left) == ast.dump(cond.comparators[0]):
                out.append((rid, "self-comparison"))
    return out


defects = ast_defects(SRC)
row("G02", "G", "AST self-audit: no evidence row is a constant fold or a "
    "self-comparison", len(defects) == 0,
    f"defects found: {defects if defects else 'none'}; D and G rows are "
    "declarations and are exempt by class, not by exception")

# Two sentences of the released manuscript are non-claiming uses whose clause
# structure separates the token from the negation that governs it: a colon in
# the first, an em dash in the second.  The manuscript is released, so rather
# than reword it we pin the exemption to the EXACT sentences.  An exemption
# pinned to a full string cannot grow to cover anything else, and row G06 fails
# if a pinned sentence is no longer present, so the list cannot outlive its
# target.  See row R05 item C8.
DECLARED_NONCLAIM = [
    "What it does not do: derive anything from an action, select anything, "
    "or introduce new mathematics.",
    "the boundary structure of the Dirac operator and its chirality "
    "decomposition are standard, and the corpus gate that asks whether any "
    "two-dimensional factor carries a non-central involution is therefore "
    "answered by a borrowed object rather than a new one.",
]

CLAIM_RE = re.compile(r"\bfirst\b(?!-)|\bnew\b|\bnovel\b|\bunique\b|action-derived",
                      re.I)
NEG_RE = re.compile(r"\bno\b|\bnot\b|\bneither\b|\bnever\b|\bcannot\b|\bnone\b",
                    re.I)


def claim_hits(text):
    """Clause-level, negation-aware scan.  A hit inside a clause that carries a
    negation is a non-claiming mention and is exempt.  Clause, not line: a
    marker in one clause must not shield a claim in the next."""
    hits = []
    for clause in re.split(r"[.;:!?]|\s—\s|\s-\s|\|", text):
        for m in CLAIM_RE.finditer(clause):
            if not NEG_RE.search(clause):
                hits.append((m.group(0), clause.strip()[:90]))
    return hits


# live fire: the two scanners must actually fire on injected defects
lf_ast = ast_defects("def row(a,b,c,d,e):\n    pass\n"
                     "row('ZZ1','C','x', 1 == 1, 'd')\n"
                     "row('ZZ2','C','x', True is not False, 'd')\n")
lf_claim_pos = claim_hits("This construction is the first of its kind")
lf_claim_neg = claim_hits("This paper claims no new external mathematics")
lf_claim_hyphen = claim_hits("it is what the first-order term leaves behind")
lf_pin = DECLARED_NONCLAIM[0].replace("does not do", "does")
row("G03", "G", "LIVE FIRE: every scanner fires on an injected defect and "
    "stays silent on the legitimate case",
    sorted({d[1] for d in lf_ast}) == ["constant fold", "self-comparison"]
    and len(lf_ast) == 3
    and len(lf_claim_pos) == 1 and len(lf_claim_neg) == 0
    and len(lf_claim_hyphen) == 0 and len(claim_hits(lf_pin)) == 1,
    "AST: the injected `1 == 1` is BOTH a constant fold and a self-comparison, "
    "so three defects from two injected rows - the first expectation written "
    "here said two and this row failed until it was corrected. Claim scanner: "
    "fires on an asserted superlative, silent on a negated mention, does not "
    "match first-order, and fires on a pinned sentence with its negation "
    "removed, so the pinning in G06 cannot shield a real claim")

# ------------------------------------------------- manuscript-facing guards
ap = argparse.ArgumentParser(add_help=True)
ap.add_argument("--no-manuscript", action="store_true")
ARGS, _ = ap.parse_known_args()
here = os.path.dirname(os.path.abspath(__file__))
paper_path = os.path.join(here, PAPER)
paper_present = os.path.isfile(paper_path)
paper_text = open(paper_path, encoding="utf-8").read() if paper_present else ""
paper_sha = hashlib.sha256(paper_text.encode()).hexdigest() if paper_present else ""

row("G04", "G", "the manuscript is present and its digest is recorded",
    paper_present or ARGS.no_manuscript,
    (f"{PAPER} sha256={paper_sha[:16]}..., {len(paper_text.splitlines())} lines"
     if paper_present else
     "MANUSCRIPT ABSENT and --no-manuscript was passed: rows G04-G06 did not "
     "run. This run is not a release check"))

named = set(re.findall(r"[A-Za-z0-9_\-]+\.(?:py|md)", paper_text))
self_name = os.path.basename(__file__)
unresolved = sorted(f for f in named
                    if f not in LEGACY_FILE_MAP and f not in (PAPER, self_name))
row("G05", "G", "every companion the manuscript names resolves, through the "
    "legacy map, to this file",
    (not paper_present and ARGS.no_manuscript) or not unresolved,
    (f"{len(named)} filenames named; {len([f for f in named if f in LEGACY_FILE_MAP])}"
     f" carried by LEGACY_FILE_MAP; unresolved={unresolved or 'none'}"
     if paper_present else "not run"))

missing_pins = [d for d in DECLARED_NONCLAIM if d not in paper_text] \
    if paper_present else []
scrubbed = paper_text
for d in DECLARED_NONCLAIM:
    scrubbed = scrubbed.replace(d, " ")
hits = claim_hits(scrubbed) if paper_present else []
row("G06", "G", "manuscript claim scan: no unnegated novelty or derivation "
    "claim, and no stale exemption",
    (not paper_present and ARGS.no_manuscript)
    or (len(hits) == 0 and not missing_pins),
    (f"hits={hits if hits else 'none'}; "
     f"{len(DECLARED_NONCLAIM)} exactly-pinned non-claiming sentences, "
     f"stale pins={missing_pins or 'none'}" if paper_present else "not run"))

census = {}
for r in ROWS:
    census[r["class"]] = census.get(r["class"], 0) + 1
row("G07", "G", "class census: P is empty by construction and T is empty",
    census.get("P", 0) == 0 and census.get("T", 0) == 0,
    "this file discharges no theorem. The proofs are the human arguments of "
    "the paper; these rows are computations, witnesses, controls, guards and "
    "declarations")

# --------------------------------------------------- v1.1 guards
# G08.  The withdrawn implication must not come back.  The relation is declared
# by an explicit token rather than inferred from wording (VERIFY 7.2 S4): any
# sentence of the manuscript that asserts the window as a CONSEQUENCE of
# positivity must carry the token below, and the token is only legitimate in a
# sentence that is describing the retraction.
RETRACT_TOKEN = "WITHDRAWN-V1.1"
# a sentence claims the implication if it mentions positivity-improving (or the
# dichotomy branch) AND the window, in the same sentence, as an entailment.
IMPL_RE = re.compile(
    r"(positivity[- ]improving|case \(b\)|3\.2\(b\)|dichotomy)"
    r"[^.]*?(automatic|follows|forced|guarantee|hence|therefore|so that|so )"
    r"[^.]*?(0 ?< ?\|?(kappa|κ)\|? ?< ?1|usable window)",
    re.I | re.S)


def retraction_defects(text):
    """Sentences asserting the withdrawn implication without the token."""
    out = []
    for sent in re.split(r"(?<=[.!?])\s+|\n\n", text):
        if IMPL_RE.search(sent) and RETRACT_TOKEN not in sent:
            out.append(sent.strip()[:110])
    return out


retract_hits = retraction_defects(paper_text) if paper_present else []
# LIVE FIRE, VERIFY 7.1: the guard must be shown to fire on the exact sentence
# it exists to catch, and to stay silent on the sentence that reports the
# retraction.  A guard never seen to fail is not evidence that it works.
LF_INJECT = ("Because J_E is diagonal in the boundary basis, case (b) applies "
             "to any positivity-improving P there, so 0 < |kappa| < 1 holds "
             "automatically.")
LF_LEGIT = ("The v1.0 sentence which read that case (b) plus positivity-"
            "improving transfer forces 0 < |kappa| < 1 automatically is "
            "WITHDRAWN-V1.1.")
lf_ret_pos = retraction_defects(LF_INJECT)
lf_ret_neg = retraction_defects(LF_LEGIT)
row("G08", "G", "RETRACTION GUARD, live-fired: the manuscript nowhere asserts "
    "that positivity entails the phase window, except where marked withdrawn",
    len(lf_ret_pos) == 1 and len(lf_ret_neg) == 0
    and ((not paper_present and ARGS.no_manuscript) or not retract_hits),
    (f"live fire: the injected v1.0 sentence produced {len(lf_ret_pos)} hit "
     f"and the retraction-reporting sentence produced {len(lf_ret_neg)}. "
     f"Manuscript scan: offending sentences = "
     f"{retract_hits if retract_hits else 'none'}. The token {RETRACT_TOKEN} "
     "exempts a sentence that reports the retraction rather than making the "
     "claim" if paper_present else
     f"live fire {len(lf_ret_pos)}/{len(lf_ret_neg)}; manuscript scan not run"))

# G09, G10 and R19 measure the completed ledger, and cannot be emitted here: at
# this point the R block has not run, so ROWS is incomplete and any count taken
# now would be wrong.  They are emitted at the end of the file instead.  The
# v1.0 file computed its census twice for the same reason.

# ================================================ BLOCK R : the registries
row("R01", "D", "RELEASE METADATA",
    True is not False,
    "ZS-M66 v1.5.1, 2026-08-31 KST. NON-SSOT. Release label "
    "PROPOSED-FOR-FREEZE, FREEZE-PENDING-AUDIT. Output role SUPPORT / METHOD. "
    "TERMINAL-IN-SCOPE is PROPOSED for the scope stated in paper 7 and is NOT "
    "recorded as granted; see row R30 and row R31. v1.5 stated the freeze and "
    "its approval as accomplished facts before the audit they were "
    "conditional on had run, and that is withdrawn here. CORE not claimed. "
    "Programme movement: the measurement-selector frontier OPEN -> OPEN "
    "across every version. Predecessor manuscript and companion SUPERSEDED "
    "and retained, not deleted. Independence: six audit rounds. Rounds 1 and "
    "2 shared a model lineage with the generator. Round 3 reached corpus "
    "material the build could not read but did not replay the companion. "
    "Rounds 4, 5 and 6 replayed the companion under the registered names and "
    "reproduced its counts and digests. Every round returned substantive "
    "findings and five of the six returned findings no passing run could "
    "catch. Qualified-human anchor: NONE. REVIEW READY is NOT claimed and "
    "would require a qualified human or a deterministic formalisation. Paper "
    "identity: the code ZS-M66 is retained by user decision, gate F-M66.12 "
    "CLOSED; see row R26")
row("R02", "D", "DECLARED CONVENTIONS AND HIDDEN-FREEDOM AUDIT",
    True is not False,
    "None of these is derived: (1) signature (+,-,-,-) and the chiral "
    "representation; (2) outward normal along the third spatial direction; "
    "(3) the chiral-bag U(1) as a subfamily of the full U(2) of self-adjoint "
    "boundary conditions; (4) gamma0 as the identification E+ -> E-; (5) the "
    "overall factor -i divided out so theta = 0 gives the identity. Declared "
    "instances: cos theta = -3/5, sin theta = 4/5, psi0 = (1,2) giving "
    "kappa = 3/5; and an SU(2) witness alpha = -3/5, beta = 12/25 + 16i/25. "
    "These are Pythagorean rationals chosen for exactness, instances of the "
    "model and not project constants")
row("R03", "D", "PRIOR-ART EVIDENCE LEDGER",
    True is not False,
    "E-1 self-adjoint-extension literature: extensions are the maximal "
    "isotropic subspaces of the boundary structure, in bijection with "
    "unitaries by Cayley transform -> paper 5.2 classification is IMPORTED, "
    "and this corpus had already cited that source once. "
    "E-2 chiral-bag / Cheshire-Cat literature: the boundary condition is the "
    "same equation as paper 5.2, and the angle is written there as an EXTERNAL "
    "meson field value at the surface -> IMPORTED verbatim, and the angle is "
    "sourced, which is gate F-M66.9. "
    "E-3 bag gauge-theory literature: quarks change chirality on reflection and "
    "bag conditions break the axial symmetry -> paper 5.4's leak is IMPORTED. "
    "E-4 heat-kernel literature: the theta-dependence of chiral-bag invariants "
    "is an established programme -> the U(1) family as moduli is IMPORTED. "
    "E-5 sign-problem literature: a non-negative transfer matrix carries an "
    "antiunitary symmetry whose spontaneous breaking is CONJECTURED impossible "
    "and proved in two cases, and the proof's first step is the "
    "Perron-Frobenius positivity used here -> paper 3.1's reality lock is "
    "IMPORTED, and the general version is open externally too, so our "
    "finite-dimensional statement is not the hard part. "
    "E-6 standard chiral-rotation results: a chiral rotation shifts the mass "
    "phase and the vacuum angle shifts anomalously -> paper 6's physics is "
    "IMPORTED, textbook")
row("R04", "D", "NOVELTY CLASSIFICATION - OPEN-NOVELTY COUNT IS ZERO",
    True is not False,
    "IMPORTED or elementary: the reality lock, the quadrant bound, the "
    "two-form identity, the contraction criterion, both branches of the "
    "grading-cone dichotomy, the asymmetry budget, the boundary grading, the "
    "boundary-condition classification, the chiral-bag family and its "
    "boundary unitary, and the chiral-rotation shift. SPECIALIZED, and these "
    "are the only surviving contributions: identifying the grading imbalance "
    "with the seam-asymmetry demand so that the deficit factorises, and "
    "identifying the mass-phase summand with the registered vacuum-direction "
    "debt. Corpus-internal only: a standing corpus gate on a two-dimensional "
    "non-central involution is answered by an imported object, which is "
    "programme progress with zero external mathematical value. "
    "Search limits: four query families; lattice boundary terms, boundary "
    "conformal field theory and topological-insulator boundary theories were "
    "NOT searched; correction histories of E-1, E-2 and E-5 were NOT checked. "
    "NOT_FOUND is not ABSENT")
row("R05", "D", "CORRECTIONS MADE DURING PRODUCTION",
    True is not False,
    "C1 an earlier draft predicted that the Dirac boundary form pairs left "
    "against right and is intrinsically chirality-mixing. FALSE: it is the "
    "normal vector current and commutes with chirality; row D04 caught it. "
    "Do-not-repeat: do not give the boundary flux and the mass term the same "
    "name. "
    "C2 the first minimal test used a transfer convention whose selected state "
    "was the minimum eigenvector, and whose operator was not entrywise "
    "positive in the grading basis; a transfer operator's ground state is its "
    "Perron-Frobenius top eigenvector. Corrected; the selected state is "
    "unchanged. "
    "C3 a negative control in that file compared a probability with itself, a "
    "tautology passing as evidence; replaced by a real zero-rotation blindness "
    "test and a commuting-transfer control. "
    "C4 the Cheshire-gate file's first version contained a generator "
    "expression in a truth test, always true - the same guard-surface defect "
    "this line wrote a standing rule against after reporting it upstream. The "
    "self-audit caught it in the same minute. "
    "C5 EXPECTED_ROWS was wrong on the initial execution of three of the four "
    "predecessor files; recorded because a fail-closed count that never fires "
    "is not evidence that it works. "
    "C6 a release scan of the finished paper found a false priority claim - "
    "that the anomaly gate is the earliest point in this line at which a real "
    "observable is in reach. FALSE: the corpus already carries observational "
    "falsifiers. The superlative was retracted. "
    "C7 the finished paper described the upstream invariant tensor with a word "
    "this line forbids in unverified-novelty contexts; replaced by the "
    "upstream's own wording, multiplicity-one. "
    "C8 this file's own claim scanner then failed against the released paper "
    "on two non-claiming sentences whose clause structure - a colon in one, an "
    "em dash in the other - separated the token from the negation governing "
    "it. The scanner was right to flag them and the clause splitter was right "
    "not to reach across the separator, since a marker in one clause must not "
    "shield the next. Because the paper is released the two sentences are "
    "exempted by EXACT string rather than reworded, and G06 fails if either "
    "pin goes stale, so the exemption cannot outlive its target. "
    "C9 this file's own live-fire row failed on its first run: it expected two "
    "AST defects from two injected rows, but the injected `1 == 1` is both a "
    "constant fold and a self-comparison, so three. The expectation was wrong, "
    "not the scanner. "
    "C10 v1.1, SEVERITY S3, MATHEMATICAL CORRECTION. v1.0 stated in its "
    "abstract, its introduction and paper 5.3 that a positivity-improving "
    "transfer operator with a diagonal non-central grading selects a ray with "
    "0 < |kappa| < 1. Only |kappa| < 1 follows. Rows N01-N03 carry the exact "
    "counterexample and show the failure is a codimension-one locus. Row D16, "
    "which was the only computational support for the claim, tested one "
    "matrix; v1.0 read a witness as a universal statement. Retyped C -> W. "
    "Do-not-repeat: a row that checks one object may not be cited for a "
    "sentence containing the word every, any, or automatically. "
    "C11 v1.1, audit P3. The theorem setting introduced psi0 without fixing "
    "its length while using the normalised expressions for sigma0, kappa and "
    "Tr(Delta^2); this file divided by the norm instead. The numbers agreed "
    "and the statements did not. Normalisation is now declared; row A09. "
    "C12 v1.1, audit P4. Row C04 and paper 4 called the opening weight ODD. A "
    "strictly positive vector cannot satisfy Jv = -v, so the sentence "
    "quantified over an empty class. The correct type is a positive weight "
    "with a nonzero odd component, that is, a reflection-breaking weight; "
    "row C09. "
    "C13 v1.1, audit P5. Paper 6 called theta + theta_m the physical datum. "
    "Within the reduced free-Dirac boundary model it is the invariant of the "
    "declared classical reparametrisation; in the full theory the chiral "
    "rotation is anomalous and moves the vacuum angle too, so the identity of "
    "the invariant is exactly what gate F-M66.5 leaves open. Scope narrowed. "
    "C14 v1.1, audit P6. Paper 5.4 concluded that the angle is observable. "
    "The exact flux computation supports the narrower statement that the "
    "printed term list contains no explicit exterior sector implementing the "
    "standard compensation. Whether the angle survives in the full quantum "
    "theory is separated out and left OPEN. "
    "C15 v1.1, audit P7. The cover, paper 9 and Appendix A described four "
    "verifiers and a separate supplement; since v1.0 there has been one "
    "companion. Guard G09 now fails on that wording rather than recording it "
    "as known-stale")
row("R06", "D", "DEBTS TOUCHED AND NOT CLOSED",
    True is not False,
    "The boundary-phase-law debt is REDUCED from an infinite-dimensional law "
    "to a single angle Delta = theta + theta_m; not closed. The "
    "vacuum-direction debt is IDENTIFIED as one summand of that angle; not "
    "closed, and now load-bearing for the phase. The physical seam-environment "
    "debt sees its three requirements met by an imported object, but the "
    "construction is not derived from an action, so the debt does not close. "
    "The action-to-instrument debt is untouched: no parameter of the model is "
    "derived here. The exact-slab / reflection-positive identification is "
    "untouched")
row("R07", "D", "NO-GO EMISSION RECORD for the scalar closure of paper 4",
    True is not False,
    "SIGN: the gate asked whether the corrected action supplies odd boundary "
    "content, and the computation answers that gate's positive form. "
    "QUANTIFIER: an enumeration over a printed finite term list, so universal "
    "over that list and over nothing else. "
    "SOURCE: the obstruction comes from the upstream term list, not from a "
    "failure of our own construction. "
    "VALUE: it erases the scalar sector from the search space")
row("R08", "D", "GATES",
    True is not False,
    "F-M66.2 the quadrant bound's actual hypotheses, read from the upstream "
    "verifier rather than a summary table - OPEN, armed. "
    "F-M66.5 the anomaly relating the bulk vacuum angle to the boundary angle "
    "- OPEN, load-bearing: paper 5.3 wants a large angle while the bulk angle "
    "is severely bounded by experiment; if the two are the same object this is "
    "an immediate kill, and our typing says they are not. "
    "F-M66.6 a symmetry reduction of the U(2) moduli fixing Delta - OPEN. "
    "F-M66.7 a negative real part with a large seam asymmetry pushes theta "
    "toward pi - OPEN. "
    "F-M66.8 the uncompensated axial boundary flux is absorbed, or declared as "
    "explicit breaking - OPEN, re-typed; see R09. "
    "F-M66.9 the angle is sourced by a field the action actually contains - "
    "OPEN, both branches currently fail. "
    "F-M66.10 a curved boundary, a gauge background or several generations "
    "breaks the factorisation - OPEN")
row("R09", "D", "F-M66.8 ADJUDICATION IN FULL",
    True is not False,
    "The objection was that the boundary angle might be unobservable because "
    "interior theta-dependence is compensated by an exterior field. "
    "Compensation is anomaly inflow and needs something to leave the interior. "
    "Rows E04-E08: the vector flux vanishes identically on the boundary "
    "subspace - that is the isotropy condition - while the axial flux "
    "restricts to diag(-1,+1) in the graph basis, the same at every angle "
    "including the MIT one, and equal to the grading. Since the printed term "
    "list declares no exterior field there is nothing to compensate with and "
    "the cancellation has no mechanism. The gate is DEFUSED as a kill and "
    "RE-TYPED as an upstream consistency obligation: the boundary carries an "
    "uncompensated axial flux. Either the action supplies an absorber, and "
    "then the angle is imported from it, or the axial symmetry is explicitly "
    "broken at the boundary as a declared input. Neither branch produces a "
    "derived phase")
row("R10", "D", "MISSION POSITION, STOP, REVERSAL",
    True is not False,
    "Founding question: the origin of measurement. Frontier: the physical "
    "measurement selector and record. The paper advances the frontier's "
    "residue, not its state. Value separation - mission value: a route closed, "
    "a residue reduced to one angle, a standing gate answered, two kill tests "
    "registered; external mathematical value: NONE; reliability value: a false "
    "prediction of our own caught by computation, a tautological control "
    "removed, a guard-surface defect caught by the audit this line wrote for "
    "that class. STOP: the route budget is spent, the strongest route survived "
    "its minimal construction, the missing object is fixed as a signature, and "
    "further search does not change the novelty verdict. REVERSAL: a "
    "counterexample to the dichotomy above dimension two; a narrower reading "
    "of the imported quadrant bound; an exterior field found in the corrected "
    "action; recovery of the predecessor version under this code; a "
    "computation of the anomaly relating the bulk and boundary angles")
row("R11", "D", "DO-NOT-REPEAT, added by this work",
    True is not False,
    "1 Do not give the boundary flux and the mass term the same name; they are "
    "different bilinears and confusing them is a layer crossing, which "
    "produces no failing row. "
    "2 A gate that is automatically satisfied under one alignment and "
    "automatically violated under another is not a gate; ask the alignment "
    "question instead. "
    "3 When a witness family has as many free real parameters as the target has "
    "real components, say so in the artifact, not only in the prose. "
    "4 A rule this line wrote against a class of defect does not prevent this "
    "line from committing that defect; keep the audit that catches it")
row("R12", "D", "PROCESS LIMITS",
    True is not False,
    "The predecessor under this paper code was not recovered: five query "
    "families across the repositories returned nothing and two locators remain "
    "unexhausted, so no non-loss comparison against a predecessor was "
    "possible. The upstream quadrant bound's body was not read: two versions "
    "of the upstream paper were retrieved, one carrying a different theorem "
    "series and the other only a summary table; the next locator is the "
    "upstream verifier's row definitions, and gate F-M66.2 stays armed. "
    "Correction histories of the external sources were not checked. Scope: "
    "flat boundary, free Dirac operator, single chiral angle, one generation, "
    "no gauge background, no curvature in the boundary term. The "
    "general-dimension arguments are human proofs; these rows confirm them at "
    "dimensions two through six")
row("R13", "D", "HISTORY ROWS to append after those already recorded",
    True is not False,
    "The corpus history file in the working set ends at H-0240, so the rows "
    "this build generates are numbered from H-0241. "
    "H-0241 CLAIM STATE CHANGE, [verified] -> withdrawn: the implication "
    "'positivity improving plus diagonal non-central grading entails "
    "0 < |kappa| < 1' is retracted. Exact counterexample P = [[2,1],[1,2]], "
    "J = diag(-1,+1): PF ray (1,1), [P,J] != 0, Delta != 0, T = 1 maximal, "
    "kappa = 0, phase identically zero at every angle. Replacement statement: "
    "|kappa| < 1 is automatic, kappa != 0 is not, and the reachable set of "
    "kappa is the whole open interval. "
    "H-0242 CRITICAL VERIFIER DEFECT: the v1.0 companion returned 74/74 PASS "
    "on a manuscript carrying that false universal statement, because row D16 "
    "checked a single witness. Witness PASS does not entail a universal "
    "statement. Rows N01-N07 and guard G08 added; D16 retyped C -> W. "
    "H-0243 SSOT/ARTIFACT REPLACEMENT: ZS-M66 v1.0 and zs_m66_verify_v1_0.py "
    "SUPERSEDED by ZS-M66 v1.1 and zs_m66_verify_v1_1.py. Predecessor retained "
    "under the legacy map; nothing deleted. "
    "H-0244 SCOPE CORRECTIONS: theta + theta_m limited to the reduced "
    "free-Dirac sector pending the anomaly gate; the Cheshire-Cat adjudication "
    "split into a certified local flux result and an OPEN observability "
    "question; the boundary weight retyped from odd to reflection-breaking. "
    "H-0245 STRUCTURAL CONFLICT, UNRESOLVED: the paper code ZS-M66 is occupied "
    "by two different papers - the collision-class record paper cited by the "
    "research mission as ZS-M66 v0.1, and this positivity-phase line. The "
    "conflict is registered, not silently merged, and awaits a user decision; "
    "see R17. "
    "H-0246 gate F-M66.11 opened: the action must separately select a state "
    "with kappa != 0, which is a load-bearing requirement that did not exist "
    "before H-0241 because it was believed to be automatic")
row("R14", "D", "SUPERSESSION AND THE LEGACY MAP",
    True is not False,
    "This file replaces four verifiers and the supplement, listed in "
    "LEGACY_FILE_MAP. Nothing is deleted: their evidence rows are blocks A-E "
    "and their prose is blocks R01-R13. The supplement is folded into a "
    "verifier rather than into the paper because the standing rule for this "
    "line is that correction history, guard lineage and release metadata do "
    "not enter a manuscript body; a verifier is a registered companion and "
    "satisfies that rule. REPAIRED IN v1.1: v1.0's cover, section 9 and "
    "Appendix A named five companions and spoke of four verifiers, and v1.0 "
    "recorded that staleness rather than fixing it. The v1.1 manuscript names "
    "one companion, and guard G09 now FAILS on the old wording instead of "
    "filing it. Recording a defect is not repairing it, which is why the "
    "record has been replaced by a guard")
row("R16", "D", "FAULT-INJECTION RECORD",
    True is not False,
    "Six faults were injected into a copy of this file and the manuscript in "
    "an isolated directory; the clean baseline exits 0 and every injection "
    "exits non-zero. F1 the negation removed from a pinned non-claiming "
    "sentence, which makes the pin stale and the claim live at once. F2 an "
    "asserted superlative inserted into the manuscript. F3 an unregistered "
    "companion filename named in the manuscript. F4 the manuscript deleted; "
    "the same run with --no-manuscript exits 0 and prints that it is not a "
    "release check. F5 a tautological evidence row injected. F6 a locked "
    "project constant injected into the construction layer. A guard that has "
    "never been shown to fail is not evidence that it works. "
    "v1.1 ADDS FOUR INJECTIONS against the guards introduced here, run in an "
    "isolated directory with the clean baseline at exit 0. F7 the withdrawn "
    "implication reasserted in the manuscript without the retraction token -> "
    "exit 1, G08 fires. F8 the manuscript's census banner altered by one "
    "count -> exit 1, G09 fires. F9 the stale four-verifier package wording "
    "restored to the cover -> exit 1, G09 fires. F10 row D16 retyped back to "
    "class C without updating RETYPED_IN_V11 -> exit 1, G09 and G10 both "
    "fire. Clean-room: copied to an empty directory, one command, exit 0, and "
    "two consecutive runs byte-identical. v1.2 ADDS THREE INJECTIONS, run "
    "in an isolated directory with the clean baseline at exit 0. F11 the "
    "exhaustiveness disclaimer stripped from the dichotomy sentence -> exit "
    "1, G11 fires. F12 row N05 retyped back to class C without updating "
    "RETYPED_IN_V12 -> exit 1, G09 and G10 both fire. F13 the census banner "
    "in the manuscript altered by one count -> exit 1, G09 fires. "
    "GUARD-SURFACE NOTE: the initial form of G11 split on sentence ends, "
    "and its own F11 injection PASSED, because the exempting token sat "
    "later in the same sentence and shielded the assertion in front of it. "
    "That is the surface-form defect this line wrote a standing rule "
    "against, committed again in the same lineage and caught by live fire "
    "rather than by reading. The guard now splits at clause boundaries, and "
    "this sentence is the disclosure the rule requires when a defect class "
    "reported upstream is repeated here. v1.3 ADDS TWO INJECTIONS. F14 a stale "
    "version string planted in a live row of this source -> exit 1, G09 fires. "
    "F15 the scope token stripped from the manuscript's closure sentence -> "
    "exit 1, G12 fires. SECOND GUARD-SURFACE NOTE: F14 did NOT fire against the "
    "initial form of the extended G09, whose exemption was a flag switched on "
    "by a marker line and switched off by a line that looked like a terminator; "
    "it exempted the remainder of the file. That is the same surface-form "
    "defect as the G11 case, in the same version, so the exemption is now "
    "computed by brace matching over named assignments and by row span, the "
    "release-metadata row is declared never exempt because it is the row under "
    "audit, and both injections fire. A guard whose exemption is positional "
    "rather than structural is not a guard, and an exemption wide enough to "
    "swallow the statement being audited is not an exemption. v1.4 ADDS TWO "
    "INJECTIONS. F16 the open-question token stripped from the manuscript's "
    "same-object sentence -> exit 1, G13 fires. F17 a stale release string "
    "planted in the current release-metadata row -> exit 1, G09 fires, which "
    "re-confirms the v1.3 repair against the version it was written for. Both "
    "run in an isolated directory with the clean baseline at exit 0. v1.5 ADDS "
    "FIVE INJECTIONS for the four self-reference guards, all in an isolated "
    "directory with the clean baseline at exit 0. F18 a gate cited that the "
    "gate table does not define -> exit 1, G14 fires. F19 a retired gate "
    "called OPEN in running text -> exit 1, G14 fires. F20 a non-claim cited "
    "with no definition -> exit 1, G15 fires. F21 a certificate row cited that "
    "is absent from this run -> exit 1, G16 fires. F22 a theorem cited that is "
    "not stated -> exit 1, G17 fires. THIRD GUARD-SURFACE NOTE, and the "
    "reason this row keeps growing: F19 did NOT fire against the first form of "
    "G14, whose clause splitter split on the period and therefore cut the "
    "identifier F-M66.13 into two fragments, so the retired-gate arm could "
    "never see a gate and a status in one clause. That is the same family as "
    "the G11 and G09 cases, the third occurrence in this line, and it was "
    "caught by live fire rather than by reading, again. Identifiers are now "
    "protected before splitting. The standing lesson, recorded at the freeze: "
    "in this codebase every new guard has been wrong on its first form, and "
    "the injection test is the only thing that has ever found it. v1.5.1 ADDS "
    "TWO INJECTIONS, isolated directory, clean baseline exit 0. F23 a retired "
    "gate restored to present-tense use in paper 2.1 -> exit 1, the "
    "STRENGTHENED G14 fires, where the unstrengthened form passed the same "
    "text. F24 the announced count in paper 1 set back to five over six items "
    "-> exit 1, G18 fires. FOURTH GUARD-SURFACE NOTE, and the one that "
    "generalises the other three: G14 was wrong TWICE. Its first form split "
    "identifiers, which its injection caught. Its second form searched for the "
    "literal word OPEN, and its injection used that same word, so the test "
    "confirmed the implementation and not the property; a human reader found "
    "it instead. The standing rule this line ends with: an injection that "
    "reuses the guard's own vocabulary tests the code, and every guard needs "
    "at least one injection phrased the way a careless author would phrase "
    "it, not the way the guard is written")
row("R15", "D", "WHAT THIS FILE IS NOT",
    True is not False,
    "It proves no theorem: class P is empty and row G07 checks that. A passing "
    "run certifies exactly the range these rows examine and nothing beyond it. "
    "It is not an independent audit, because it shares a lineage with what it "
    "checks. It does not derive any parameter from an action, and it does not "
    "show selection. Specific to v1.1: a passing run of this file did not "
    "catch the v1.0 defect and would not have; what catches it is row N01, "
    "which exists because an audit supplied the counterexample")
row("R17", "D", "AUDIT ROUND 1 - v1.0 audit, 8 findings, P1-P8, response "
    "version 1.1",
    True is not False,
    "P1 S3 MATHEMATICAL. Abstract, paper 1, paper 5.3: positivity does not "
    "entail 0 < |kappa| < 1. ACCEPTED IN FULL. Retracted; replacement theorem "
    "with both halves separated; rows N01-N07; guard G08; row D16 retyped. "
    "P2 S3/S2 IDENTITY. The paper code ZS-M66 is occupied by an earlier and "
    "unrelated paper, cited by the research mission as ZS-M66 v0.1 on the "
    "collision class and record measures. ACCEPTED AS A FINDING, NOT RESOLVED. "
    "The two candidate remedies - issue this line under an unused code, or "
    "declare a formal supersession of v0.1 - are not equivalent and the second "
    "is not reversible, so neither is executed here. Registered as an open "
    "identity gate F-M66.12 and escalated for a user decision. "
    "P3 S2. psi0 normalisation absent from the theorem setting. ACCEPTED; "
    "declared in the manuscript, row A09. "
    "P4 S2. The opening boundary weight is not an odd vector. ACCEPTED; type "
    "corrected in paper 4, rows C04 and C09. "
    "P5 S2. theta + theta_m over-claimed as the physical datum. ACCEPTED; "
    "restricted to the reduced free-Dirac sector, anomaly gate retained. "
    "P6 S2. The Cheshire-Cat verdict over-strong. ACCEPTED; split into a "
    "certified local statement and an OPEN observability question. "
    "P7 S1/S2. Stale four-verifier package wording. ACCEPTED; repaired and "
    "converted into guard G09. "
    "P8 S2. Paper 8 carried no bibliography with locators. ACCEPTED; see R20. "
    "Not accepted as stated: none. Findings deferred: none")
row("R18", "D", "RETRACTION RECORD - the exact statement withdrawn",
    True is not False,
    "WITHDRAWN, ZS-M66 v1.0, abstract sentence 3, paper 1 item 2, paper 5.3 "
    "final paragraph: 'Because J_E is diagonal in the boundary basis, case (b) "
    "of 3.2 applies to any positivity-improving P there ... so 0 < |kappa| < 1 "
    "holds automatically.' WHY IT IS FALSE: strict positivity of every "
    "component of the PF ray in both eigenspaces bounds |kappa| away from 1 "
    "but says nothing about kappa = 0, and the kappa = 0 locus is nonempty. "
    "DOWNSTREAM: the abstract's 'nonzero but incomplete grading imbalance' and "
    "paper 1's 'the same dichotomy opens another route' both fall with it; "
    "both are rewritten. The factorisation 1 - |a|^2 = T^2 sin^2 theta, the "
    "asymmetry budget, both branches of the dichotomy, the boundary grading "
    "and the flux computation are UNAFFECTED and are re-verified here. "
    "REPLACEMENT: theorem 3.4 of the v1.1 manuscript, with claim ID CL-M66.4, "
    "status DERIVED for the surviving half and the counterexample CERTIFIED. "
    "No external release of v1.0 was made, so no erratum is owed outside this "
    "corpus; the version is retained rather than deleted")
row("R20", "D", "BIBLIOGRAPHY LEDGER with locators, answering finding P8",
    True is not False,
    "B-1 A. Chodos and C. B. Thorn, Chiral invariance in a bag theory, Phys. "
    "Rev. D 12 (1975) 2733-2743, doi 10.1103/PhysRevD.12.2733 - the chiral-bag "
    "boundary condition and its angle. B-2 A. Chodos, R. L. Jaffe, K. Johnson, "
    "C. B. Thorn and V. F. Weisskopf, Phys. Rev. D 9 (1974) 3471 - the MIT bag "
    "boundary condition, the theta = 0 member. B-3 C. G. Beneventano, P. B. "
    "Gilkey, K. Kirsten and E. M. Santangelo, Strong ellipticity and spectral "
    "properties of chiral bag boundary conditions, J. Phys. A 36 (2003) "
    "11533-11543, arXiv hep-th/0306156 - the angle as a one-parameter family "
    "and its spectral role. B-4 C. G. Beneventano, E. M. Santangelo and A. "
    "Wipf, Spectral asymmetry for bag boundary conditions, J. Phys. A 35 "
    "(2002) 9343-9354. B-5 P. Hrasko and J. Balog, The fermion boundary "
    "condition and the theta angle in QED in two dimensions, Nucl. Phys. B245 "
    "(1984) 118-126 - the closest external precedent for gate F-M66.5, in two "
    "dimensions. B-6 S. Nadkarni, H. B. Nielsen and I. Zahed, Bosonization "
    "relations as bag boundary conditions, Nucl. Phys. B253 (1985) 308-322, "
    "and M. Rho, Cheshire Cat Hadrons, Phys. Rep. 240 (1994) 1-142 - the "
    "compensation mechanism adjudicated in paper 5.4. B-7 M. Asorey, A. Ibort "
    "and G. Marmo, Global theory of quantum boundary conditions and topology "
    "change, arXiv hep-th/0403048, and the same authors, The topology and "
    "geometry of self-adjoint and elliptic boundary conditions for Dirac and "
    "Laplace operators, Int. J. Geom. Methods Mod. Phys. 12 (2015) 1561007, "
    "arXiv 1510.08136, section 4.3 - boundary conditions as unitaries via the "
    "Cayley transform. B-8 Z. Ringel and D. L. Kovrizhin, Quantized "
    "gravitational responses, the sign problem, and quantum complexity, Sci. "
    "Adv. 3 (2017) e1701758, arXiv 1704.03880 - the non-negative transfer "
    "matrix carries a complex-conjugation antiunitary symmetry, whose "
    "spontaneous breaking is conjectured impossible and proved in two cases. "
    "EESF STATUS: Existence and Scope confirmed for all eight from publisher "
    "or arXiv records. Entailment confirmed at abstract level for B-3, B-5 and "
    "B-8; for B-1, B-2, B-4, B-6 and B-7 the mapping to the exact equations "
    "used here rests on secondary sources, so gate F-M66.2 stays armed and "
    "these are IMPORTED-OPEN rather than IMPORTED-PROVEN. Correction histories "
    "were not checked for any of the eight")



# =========================================== BLOCK V12 : audit round 2, v1.2
# Round 2 targeted v1.1.  Same lineage as the generator, so low independence
# again (L1), raised only by exact arithmetic and execution (L5).  Its two
# substantive findings are certified here before the manuscript states them.

# ---- A10 / N08 / N09 / N13 : the branch that fires is a property of the CONE
# v1.1 called 3.2 a dichotomy.  It is two sufficient conditions on how the
# involution sits relative to the cone, and they are not exhaustive.  Take the
# SAME involution and the SAME transfer operator and rotate the generating
# basis: neither branch applies, and the conclusion of branch (b) FAILS.
J_ROT = [[F(0), F(-1)], [F(-1), F(0)]]          # non-central, self-adjoint
P_ROT = [[F(2), F(1)], [F(1), F(2)]]            # entrywise positive
psi_ROT = [F(1), F(1)]                           # PF ray, eigenvalue 3


def mat2(A, B):
    return [[sum(A[i][k] * B[k][j] for k in range(2)) for j in range(2)]
            for i in range(2)]


def vec2(M, v):
    return [sum(M[i][j] * v[j] for j in range(2)) for i in range(2)]


rot_sa = J_ROT == [[J_ROT[j][i] for j in range(2)] for i in range(2)]
rot_inv = mat2(J_ROT, J_ROT) == [[F(1), F(0)], [F(0), F(1)]]
rot_noncentral = J_ROT != [[F(1), F(0)], [F(0), F(1)]] and \
    J_ROT != [[F(-1), F(0)], [F(0), F(-1)]]
rot_pos = all(P_ROT[i][j] > 0 for i in range(2) for j in range(2))
rot_pf = vec2(P_ROT, psi_ROT) == [3 * x for x in psi_ROT]
rot_comm = mat2(P_ROT, J_ROT) == mat2(J_ROT, P_ROT)
rot_Jpsi = vec2(J_ROT, psi_ROT)
rot_diag = J_ROT[0][1] == 0 and J_ROT[1][0] == 0
rot_cone = all(x >= 0 for x in vec2(J_ROT, [F(1), F(0)])) and \
    all(x >= 0 for x in vec2(J_ROT, [F(0), F(1)]))
rot_kappa = sum(psi_ROT[i] * rot_Jpsi[i] for i in range(2)) / \
    sum(x * x for x in psi_ROT)
rot_T2 = 1 - rot_kappa * rot_kappa

row("A10", "C", "the branch of 3.2 that fires is a property of the CONE, not "
    "of the pair (P, J): rotating the generating basis changes it",
    rot_sa and rot_inv and rot_noncentral and rot_pos and rot_pf
    and (not rot_diag) and (not rot_cone),
    "J = [[0,-1],[-1,0]] is a non-central self-adjoint involution; P = "
    "[[2,1],[1,2]] is entrywise positive with PF ray (1,1). J is NOT diagonal "
    "in the generating basis, so branch (b) does not apply, and J does NOT "
    "preserve the cone, so branch (a) does not apply either. The same J is "
    "diagonal in a rotated orthonormal basis. Which branch fires is therefore "
    "fixed by the choice of cone, and that choice is not derived anywhere in "
    "this paper: see row D20")

row("N08", "W", "COUNTEREXAMPLE 2, new in v1.2: outside branch (b) the "
    "surviving half FAILS - positivity improving does not give |kappa| < 1",
    rot_pos and rot_pf and rot_noncentral and rot_comm
    and rot_Jpsi == [-x for x in psi_ROT]
    and rot_kappa == -1 and rot_T2 == 0,
    f"[P,J] = 0 although J does not preserve the cone, J psi0 = -psi0, so "
    f"kappa = {rot_kappa} and T^2 = {rot_T2}. The seam asymmetry is DEAD. "
    "Theorem 3.4(i) is therefore conditional on 'diagonal in the generating "
    "basis' and the hypothesis is not removable. v1.1's abstract, section 1 "
    "and section 5.3 read the surviving half more broadly than the theorem "
    "supports; v1.2 restates it with the hypothesis carried")

rot_family = []
for a in range(1, 9):
    for b in range(1, 9):
        Q = [[F(a), F(b)], [F(b), F(a)]]
        if not all(Q[i][j] > 0 for i in range(2) for j in range(2)):
            continue
        if vec2(Q, psi_ROT) != [(a + b) * x for x in psi_ROT]:
            continue
        k = sum(psi_ROT[i] * vec2(J_ROT, psi_ROT)[i] for i in range(2)) / 2
        rot_family.append(k)
row("N09", "R", "REGRESSION: counterexample 2 is a whole family - every "
    "symmetric entrywise-positive P with PF ray (1,1) kills the asymmetry "
    "against the rotated grading",
    len(rot_family) == 64 and all(k == -1 for k in rot_family),
    f"{len(rot_family)} exact instances P = [[a,b],[b,a]], a,b in 1..8. In "
    "every one kappa = -1 and T = 0. This row is locked so that the "
    "unconditional reading of the surviving half cannot return without a "
    "failing row, exactly as N03 locks the withdrawn implication")

row("N13", "X", "the two branches of 3.2 are not exhaustive: a third "
    "alignment class exists and is covered by neither",
    (not rot_diag) and (not rot_cone) and rot_comm
    and rot_Jpsi == [-x for x in psi_ROT],
    "Branch (a) assumes J(K) subset K; branch (b) assumes J diagonal in the "
    "generating basis. The instance above satisfies neither, and its "
    "conclusion Jpsi0 = -psi0 contradicts branch (a)'s Jpsi0 = +psi0 while "
    "violating branch (b)'s |kappa| < 1. The word 'dichotomy' is therefore "
    "retired in v1.2 in favour of 'two aligned cases'")

row("D20", "D", "CONE DECLARATION, answering the round-2 finding: the "
    "generating basis of the cone on the boundary space is a CHOICE",
    True is not False,
    "Section 3 requires a cone generated by an orthonormal basis and, for "
    "branch (b), an involution diagonal in that basis. On the two-dimensional "
    "fermion boundary space the paper uses the chirality eigenbasis as the "
    "generating basis. Nothing derives that identification: the corrected "
    "action supplies no transfer operator on the boundary space, hence no "
    "cone. v1.1's own hidden-freedom audit (row R02) listed five undeclared "
    "choices and missed this one. It is declared here as choice (6) and gated "
    "as F-M66.13. Consequence, from rows N08-N09 and A10: if the action ever "
    "does supply a positive structure whose cone is not the chirality "
    "eigenbasis, the surviving half fails too and T can be 0")

# ---- N10 / N11 / N12 : Theorem 3.6, the reachable set, in EVERY dimension
# v1.1 proved surjectivity only in dimension two and only over rational (p,q),
# so the certified statement was a dense subset while the manuscript printed
# the whole interval.  The rank-one construction P = psi psi^T settles it in
# every dimension in two lines, and psi psi^T + eps I makes P invertible and
# positive definite for readers who want a nondegenerate transfer operator.
def rank_one(v):
    n = len(v)
    return [[v[i] * v[j] for j in range(n)] for i in range(n)]


def plus_eps(M, eps):
    n = len(M)
    return [[M[i][j] + (eps if i == j else F(0)) for j in range(n)]
            for i in range(n)]


SIGNS = {2: [(-1, 1)], 3: [(-1, 1, 1), (-1, -1, 1)],
         4: [(-1, 1, 1, 1), (-1, -1, 1, 1)], 5: [(-1, 1, -1, 1, 1)],
         6: [(-1, 1, 1, -1, 1, 1)]}
VS = {2: [F(1), F(3)], 3: [F(2), F(1), F(5)], 4: [F(1), F(2), F(3), F(1)],
      5: [F(3), F(1), F(1), F(2), F(5)],
      6: [F(1), F(4), F(1), F(2), F(1), F(3)]}

r1_ok = r1_eps_ok = True
r1_seen = 0
for n in (2, 3, 4, 5, 6):
    v = VS[n]
    P1 = rank_one(v)
    nrm = sum(x * x for x in v)
    r1_ok &= all(P1[i][j] > 0 for i in range(n) for j in range(n))
    r1_ok &= all(sum(P1[i][j] * v[j] for j in range(n)) == nrm * v[i]
                 for i in range(n))
    # rank one: every 2x2 minor vanishes, so the top eigenvalue is simple
    r1_ok &= all(P1[i][j] * P1[k][l] == P1[i][l] * P1[k][j]
                 for i in range(n) for j in range(n)
                 for k in range(n) for l in range(n))
    P2 = plus_eps(P1, F(1, 7))
    r1_eps_ok &= all(P2[i][j] > 0 for i in range(n) for j in range(n))
    r1_eps_ok &= all(sum(P2[i][j] * v[j] for j in range(n))
                     == (nrm + F(1, 7)) * v[i] for i in range(n))
    for eps in SIGNS[n]:
        k = sum(F(eps[j]) * v[j] * v[j] for j in range(n)) / nrm
        r1_ok &= -1 < k < 1
        r1_seen += 1

row("N10", "C", "Theorem 3.6 construction: P = psi psi^T is entrywise "
    "positive, has psi as a simple PF ray, in every tested dimension",
    r1_ok and r1_seen == 7,
    f"dimensions 2-6, {r1_seen} non-central sign patterns. P psi = |psi|^2 "
    "psi; every 2x2 minor vanishes so the rank is one and the top eigenvalue "
    "is simple; every entry is strictly positive so P is positivity "
    "improving. This is the whole proof of surjectivity and it does not use "
    "dimension two, symmetry of a special form, or rationality")

row("N11", "C", "the invertible variant P = psi psi^T + eps I is entrywise "
    "positive, positive definite, and has the same PF ray",
    r1_eps_ok,
    "eps = 1/7, dimensions 2-6. Spectrum {|psi|^2 + eps, eps, ..., eps}, so "
    "the operator is nonsingular and its top eigenvalue is still simple. A "
    "reader who objects that a rank-one transfer operator is degenerate gets "
    "the same conclusion from a nondegenerate one")

targets = [F(0), F(1, 2), F(-1, 2), F(3, 5), F(-3, 5), F(99, 100),
           F(-99, 100), F(1, 1000), F(-7, 9), F(5, 13), F(-12, 13), F(2, 3)]
reach12 = []
hit12 = True
for t in targets:
    # J = diag(-1, 1);  kappa = (v2^2 - v1^2)/(v1^2 + v2^2) = t
    # take v1^2 = 1 - t, v2^2 = 1 + t as rational SQUARES via scaling:
    # choose v = (1, s) with s^2 = (1+t)/(1-t) when that is a rational square,
    # otherwise realise t exactly by weighting a third component.
    num, den = (1 + t), (1 - t)
    v = [F(1), F(1)]
    # exact realisation with a two-component weight vector w on squares
    w1, w2 = den, num          # w1 + w2 = 2, (w2 - w1)/(w1 + w2) = t
    k = (w2 - w1) / (w1 + w2)
    hit12 &= (k == t) and w1 > 0 and w2 > 0
    reach12.append(k)
row("N12", "C", "Theorem 3.6 surjectivity: every exact rational target in "
    "(-1,1) is realised, kappa = 0 included",
    hit12 and reach12 == targets and len(set(reach12)) == len(targets),
    f"{len(targets)} exact targets from -99/100 to 99/100. Writing the PF "
    "ray's squared components as the weights (1-t, 1+t) gives kappa = t "
    "identically; the weights are strictly positive exactly when |t| < 1, and "
    "the rank-one construction of row N10 turns any strictly positive weight "
    "vector into an admissible P. Over the reals this is onto (-1,1); v1.1 "
    "certified only the rational subfamily and printed the whole interval, "
    "which is why row N05 is retyped")

# ---------------------------------------------------- G11 : alignment guard
G11_BAD = "The pair is a dichotomy on the cone of positive functions."
G11_OK = ("The predecessor called it a dichotomy (ALIGNMENT-CLASS-3) and the "
          "two cases are not exhaustive")


def dichotomy_hits(text):
    out = []
    # CLAUSE-level, not sentence-level.  The first form of this guard split on
    # sentence ends and was defeated by its own injection test: the exempting
    # token sat later in the same sentence and shielded the assertion in front
    # of it.  That is the surface-form failure this line wrote a standing rule
    # against, committed once more and caught by live fire rather than by
    # reading.  Split on clause boundaries, newlines and table pipes.
    for sent in re.split(r"[.;:!?]|\n|\||,", text):
        if re.search(r"\bdichotom", sent, re.I) and \
                "ALIGNMENT-CLASS-3" not in sent:
            out.append(sent.strip()[:70])
    return out


g11_fire = len(dichotomy_hits(G11_BAD)) == 1
g11_quiet = len(dichotomy_hits(G11_OK)) == 0
g11_hits = dichotomy_hits(paper_text) if paper_present else []
row("G11", "G", "ALIGNMENT GUARD, live-fired: the manuscript does not call "
    "3.2 a dichotomy unless the same clause carries the exhaustiveness "
    "token",
    (not paper_present and ARGS.no_manuscript)
    or (g11_fire and g11_quiet and not g11_hits),
    f"live fire: the injected v1.1 wording produced "
    f"{len(dichotomy_hits(G11_BAD))} hit and the disclaimed wording produced "
    f"{len(dichotomy_hits(G11_OK))}. Manuscript scan: offending sentences = "
    f"{g11_hits or 'none'}. The token ALIGNMENT-CLASS-3 exempts a sentence "
    "that reports the non-exhaustiveness rather than assuming exhaustiveness"
    if paper_present else "not run")

# ------------------------------------------------- R21-R24 : round-2 record
row("R21", "D", "AUDIT ROUND 2 - v1.1 audit, 8 findings A1-A8, response "
    "version 1.2", True is not False,
    "A1 S2 SCOPE. 3.2 was called a dichotomy; the two branches are not "
    "exhaustive. ACCEPTED. Renamed to two aligned cases, third class "
    "certified in N13, guard G11 added. A2 S2 ASSUMPTION. The generating "
    "basis of the cone on the fermion boundary space was never declared, and "
    "outside branch (b) the surviving half fails outright (N08, N09). "
    "ACCEPTED. Declared as construction choice (6) in row D20 and in the "
    "manuscript's setting section; gate F-M66.13 opened; non-claim NC-M66.8 "
    "added. A3 S1 PROOF/STATEMENT. Theorem 3.4(iii) claimed the whole open "
    "interval in dimension two but proved it over positive rationals only. "
    "ACCEPTED AND STRENGTHENED: Theorem 3.6 gives every dimension and every "
    "non-central diagonal grading by the rank-one construction (N10-N12); row "
    "N05 retyped C -> W. A4 S1 FRONT MATTER. The abstract stated reachability "
    "without the dimension-two qualifier that the theorem carried. RESOLVED "
    "by A3: the statement is now true as printed. A5 S1 SCOPE. The window "
    "sentence of 5.3 omitted sin theta != 0. ACCEPTED; both factors now "
    "carried. A6 S1 REGISTRY. Section 10.2 and gate F-M66.12 cite the "
    "research mission as the source of the ZS-M66 v0.1 collision, but the "
    "ACTIVE mission version no longer records paper codes at all, so the "
    "citation is stale and the collision evidence must be re-anchored to the "
    "repository catalogue. ACCEPTED AS A FINDING, NOT RESOLVED; see R23. "
    "A7 S1 PACKAGE. Row R13 projected history rows from H-0241 on the basis "
    "that the corpus history ended at H-0240; the corpus head has since "
    "moved. ACCEPTED; renumbered in R22. A8 S0 BIBLIOGRAPHY. B-1's page range "
    "is printed differently by different secondary sources. ACCEPTED as an "
    "open bibliographic discrepancy; see R24. Not accepted as stated: none. "
    "Findings deferred: A6 to a user decision")

row("R22", "D", "HISTORY ROWS, renumbered against the current corpus head",
    True is not False,
    "The rows this build generates continue from the corpus head, which has "
    "moved since v1.1 was written: the v1.1 build projected H-0241 onward and "
    "those rows now exist, and two further rows were appended after them. The "
    "v1.2 rows therefore start at H-0249 and no v1.2 row may reuse an "
    "identifier already present in the history file. H-0249 CLAIM SCOPE "
    "CHANGE: the surviving half of Theorem 3.4 is conditional on the grading "
    "being diagonal in the cone's generating basis; counterexample 2 (rows "
    "N08, N09) shows |kappa| < 1 fails otherwise, with kappa = -1 and T = 0. "
    "H-0250 NEW THEOREM: Theorem 3.6, the reachable set of kappa is the whole "
    "open interval in every dimension, by the rank-one construction; row N05 "
    "retyped C -> W because a rational family was cited for a surjectivity "
    "statement. H-0251 STRUCTURAL: the two cases of 3.2 are not exhaustive; "
    "the name dichotomy is retired and guard G11 locks the change. H-0252 "
    "GATE OPENED: F-M66.13, the action must supply the positive structure "
    "AND its cone on the boundary space, not only a transfer operator. "
    "H-0253 REGISTRY CONFLICT: the mission citation supporting F-M66.12 is "
    "stale under the active mission version; the collision itself is "
    "unresolved and awaits a user decision. H-0254 ARTIFACT REPLACEMENT: "
    "ZS-M66 v1.1 and its companion superseded by v1.2 and this file; "
    "predecessors retained under the legacy map. The exact identifiers and "
    "timestamps are assigned when the rows are appended, not here")

row("R23", "D", "F-M66.12 EVIDENCE RE-ANCHORING, unresolved", True is not False,
    "v1.1 justified the paper-code collision by saying the research mission "
    "cites ZS-M66 v0.1. The active mission version records no paper, section "
    "or seed codes at all by an explicit long-horizon invariant, so that "
    "citation no longer resolves. Three consequences. First, the collision is "
    "not thereby dissolved: the earlier paper either exists in the repository "
    "catalogue or it does not, and this build could not read the catalogue. "
    "Second, the mission-facing cost of remedy 2, retiring a result the "
    "mission relies on, is no longer demonstrated and may be zero. Third, "
    "until the catalogue is read, the collision is [OPEN] on evidence rather "
    "than [VERIFIED] as v1.1 implied. The two remedies are unchanged and "
    "neither is executed here")

row("R24", "D", "BIBLIOGRAPHY, round-2 delta", True is not False,
    "B-1 Existence and Scope were re-confirmed this round directly against "
    "the publisher record at doi 10.1103/PhysRevD.12.2733, which gives the "
    "title as printed here and a 1975 Phys. Rev. D volume 12 article on a "
    "chirally symmetric bag with surface pion and sigma fields - the source "
    "of the angle as an external field value at the surface, which is what "
    "row R03 item E-2 says. Open discrepancy: secondary bibliographies print "
    "the closing page as 2743 and as 2745, and one prints a different title "
    "for the same volume and starting page. The manuscript keeps 2743 and "
    "records the conflict rather than resolving it from secondary sources. "
    "Entailment for B-1 remains at abstract level, so its IMPORTED-OPEN "
    "typing and gate F-M66.2 are unchanged. No other reference was re-checked "
    "this round")




# ============================================ BLOCK V13 : audit round 3, v1.3
# Round 3 targeted v1.2.  Two substantive findings, both accepted: the scalar
# closure was quantified over a term list that does not fix the potential, and
# this file's own release metadata was stale while the guard that exists to
# catch that read only the manuscript.

# ---- C10 / C11 : the scalar potential is not fixed, so the closure narrows
# The upstream action does not specify V(H_5, H).  This paper's own section on
# the residue registers the CP^4 direction of the H_5 vacuum as an unfixed
# debt, and that registration is only coherent if V is unspecified: a potential
# that fixed the direction would close the debt.  So the two statements cannot
# both stand, and the one that must go is the claim that every bosonic term is
# reflection-even.
row("C10", "D", "THE SCALAR POTENTIAL IS UNSPECIFIED UPSTREAM, so its "
    "reflection type is UNKNOWN and the closure of paper 4 narrows",
    True is not False,
    "v1.2 asserted that every bosonic term of the printed list depends on H_5 "
    "only through |H_5|^2 or |dH_5|^2, and listed the potential among them. "
    "The upstream action leaves V(H_5, H) unspecified and carries that as an "
    "open debt; the same manuscript relies on exactly that debt when it says "
    "the CP^4 direction of the H_5 vacuum is unfixed and supplies the mass "
    "phase. Both cannot hold. What survives is a closure of the EXPLICIT "
    "boundary-term route: the derivative-generated scalar boundary terms that "
    "the list does write down are reflection-even, and the Yukawa contributes "
    "no scalar boundary term because it carries no derivative of H_5. What "
    "does not survive is the closure of the scalar route as such, because an "
    "unspecified potential may select a reflection-breaking vacuum whose "
    "effective boundary weight or transfer structure is asymmetric. That is "
    "an indirect route and it is OPEN, gated at F-M66.14")

# The indirect route is not hypothetical arithmetic: a reflection-breaking
# weight exists on this very cone, and section 4 already exhibits one.  The
# only question the printed list leaves open is whether the potential's vacuum
# supplies it.  This control shows the two answers are not equivalent.
row("C11", "X", "NEGATIVE CONTROL: an unspecified potential is not the same as "
    "an even one - a reflection-breaking weight on this cone already exists",
    any(x != 0 for x in v_odd_part) and all(x > 0 for x in v_odd)
    and all(x == 0 for x in v_even_part),
    "row C04 exhibits a strictly positive weight with a nonzero odd component "
    "which opens the commutation lock, and row C03 exhibits an even one which "
    "does not. The question the upstream action leaves open is which of the "
    "two an unspecified V selects, and the answer is not derivable from the "
    "absence of a term. Absence of specification is not evenness")

# ---------------------------------------------- G12 : scalar scope guard
G12_BAD = "The scalar route closes negatively over the corrected action."
G12_OK = ("The explicit boundary-term route closes negatively "
          "(SCALAR-SCOPE-V13) and the indirect route stays open")


def scalar_scope_hits(text):
    """Clause-level.  A closure sentence about the scalar route must carry the
    scope token in the SAME clause; a token in a later clause must not shield
    an unqualified closure in front of it."""
    out = []
    for clause in re.split(r"[.;:!?]|\n|\||,", text):
        if re.search(r"scalar route", clause, re.I) and \
                re.search(r"clos", clause, re.I) and \
                "SCALAR-SCOPE-V13" not in clause:
            out.append(clause.strip()[:70])
    return out


g12_fire = len(scalar_scope_hits(G12_BAD)) == 1
g12_quiet = len(scalar_scope_hits(G12_OK)) == 0
g12_hits = scalar_scope_hits(paper_text) if paper_present else []
row("G12", "G", "SCALAR SCOPE GUARD, live-fired: the manuscript does not "
    "close the scalar route as such unless the clause carries the scope token",
    (not paper_present and ARGS.no_manuscript)
    or (g12_fire and g12_quiet and not g12_hits),
    f"live fire: the unqualified closure produced {len(scalar_scope_hits(G12_BAD))} "
    f"hit and the scoped wording produced {len(scalar_scope_hits(G12_OK))}. "
    f"Manuscript scan: offending clauses = {g12_hits or 'none'}. The token "
    "SCALAR-SCOPE-V13 marks a clause that states the narrowed closure rather "
    "than the withdrawn one" if paper_present else "not run")

# ------------------------------------------------- R25 / R26 : round-3 record
row("R25", "D", "AUDIT ROUND 3 - v1.2 audit, 5 required repairs B1-B5, "
    "response version 1.3", True is not False,
    "B1 S2 SCOPE, paper 4. The negative closure was quantified over a term "
    "list that does not fix the scalar potential. ACCEPTED IN FULL. Rows C07 "
    "and C08 retyped C -> W, row C10 added, gate F-M66.14 opened, non-claim "
    "NC-M66.9 added, guard G12 added, and the manuscript's title, abstract and "
    "section 4 now say explicit boundary-term route. B2 S2 PACKAGE. This "
    "file's header, usage line and release-metadata row still said v1.1 while "
    "the executable constants said v1.2, and one row detail still used the "
    "retired word for the aligned cases. ACCEPTED IN FULL; all four repaired, "
    "and G09 extended below so that the guard reads this source and not only "
    "the manuscript. B3 IDENTITY. The auditor recommended reissuing this line "
    "under an unused paper code. NOT ACCEPTED, on an explicit user decision: "
    "the earlier code-issuance event in the history log was a reservation "
    "made without prior approval, which the project has since forbidden, so "
    "it does not bind this line. The code ZS-M66 stays. Gate F-M66.12 is "
    "CLOSED by decision; see row R26. B4 INDEPENDENCE. The two-round "
    "same-lineage limit stands and the release label stays MANUSCRIPT DRAFT. "
    "ACCEPTED. B5 VALUE. External mathematical value low, Z-Spin mission "
    "value SUPPORT, reliability value high. ACCEPTED and unchanged from the "
    "manuscript's own typing. Auditor limitation recorded: round 3 did not "
    "replay this companion, so its package finding was confirmed against the "
    "artifact by this build rather than by the auditor")

row("R26", "D", "PAPER IDENTITY, CLOSED BY DECISION, and the history "
    "admission policy", True is not False,
    "DECISION, user-approved: the paper code ZS-M66 is retained by this line "
    "and no reissue is made. REASON: the earlier issuance recorded in the "
    "history log reserved a code for a paper that was never released and "
    "never recovered; the project now requires prior approval before a code "
    "is assigned, precisely so that a log entry cannot reserve identifiers, "
    "and a reservation made before that rule does not bind work after it. "
    "CONSEQUENCE: gate F-M66.12 is CLOSED, the two remedies of the previous "
    "version are withdrawn, and no cross-reference churn is incurred. The "
    "earlier history event is neither deleted nor edited; it is simply not "
    "read as an allocation. SECOND DECISION, applied here: under the "
    "project's history admission gate this build emits ONE consolidated "
    "history row rather than one per finding, because the findings share a "
    "single audit-repair cycle and a single disposition. Version-level detail, "
    "row counts, hashes, guard lineage and the change list live in this "
    "companion and in the manuscript's correction record, which is where the "
    "gate directs them")




# ================================ BLOCK Q : the canonical cone, round 4 upgrade
# The classical statements of block A/B/N live on a cone generated by a chosen
# orthonormal basis, and v1.3 had to DECLARE that choice on the fermion
# boundary space because nothing derives it.  On a two-dimensional spinor space
# the natural positive structure is not a coordinate cone at all: it is the
# cone of positive semidefinite operators, and the natural transfer object is a
# positive trace-preserving map rather than a matrix acting on coordinates.
# Rewritten there, the choice disappears instead of being declared.
#
# Conventions for this block.  rho = (I + r . sigma)/2 with r rational, so a
# state is a rational Bloch vector with |r| <= 1 and is faithful iff |r| < 1.
# A trace-preserving map is (M, t) with r -> M r + t.  The grading is
# J = diag(-1, +1) = -sigma_z, so kappa = Tr(rho J) = -r_z.  The grading flip
# is X = sigma_x, whose Bloch action is SGN = diag(1, -1, -1); XJX = -J.
SGN = (1, -1, -1)


def bl_apply(M, t, r):
    return [sum(M[i][j] * r[j] for j in range(3)) + t[i] for i in range(3)]


def bl_conj(M, t):
    """Ad_X . Phi . Ad_X in Bloch coordinates."""
    return ([[F(SGN[i]) * M[i][j] * F(SGN[j]) for j in range(3)]
             for i in range(3)],
            [F(SGN[i]) * t[i] for i in range(3)])


def bl_fixed(M, t):
    """Exact solution of (I - M) r = t, or None if not unique."""
    A = [[F(1 if i == j else 0) - M[i][j] for j in range(3)] + [t[i]]
         for i in range(3)]
    for c in range(3):
        p = next((k for k in range(c, 3) if A[k][c] != 0), None)
        if p is None:
            return None
        A[c], A[p] = A[p], A[c]
        pv = A[c][c]
        A[c] = [x / pv for x in A[c]]
        for k in range(3):
            if k != c and A[k][c] != 0:
                f0 = A[k][c]
                A[k] = [x - f0 * y for x, y in zip(A[k], A[c])]
    return [A[i][3] for i in range(3)]


def sqrt_ub(f):
    """A rational u with u >= sqrt(f), by AM-GM around a float seed.  The seed
    is only a seed: the returned bound is certified by the exact inequality
    u^2 - f = ((f/s - s)/2)^2 >= 0, which row Q06 checks."""
    if f == 0:
        return F(0)
    s = F(float(f) ** 0.5).limit_denominator(10 ** 6)
    if s <= 0:
        s = F(1)
    return (f / s + s) / 2


def diag3(d):
    return [[F(d[i]) if i == j else F(0) for j in range(3)] for i in range(3)]


ZERO3 = [F(0), F(0), F(0)]
ZEROM = [[F(0)] * 3 for _ in range(3)]

# The witness channel of row Q04, given by its action on matrix entries:
#   p' = (1-a) p + b q,   q' = a p + (1-b) q,   c' = g c
# with a = 4/5, b = 1/5, g = 2/5.  Bloch form follows by substitution.
A_RATE, B_RATE, G_COH = F(4, 5), F(1, 5), F(2, 5)
M_CL = diag3([G_COH, G_COH, 1 - A_RATE - B_RATE])
T_CL = [F(0), F(0), B_RATE - A_RATE]


def principal_minors_nonneg(Mx):
    """Exact PSD test for a rational symmetric matrix: every principal minor
    is non-negative.  Used on the Choi matrix, so complete positivity is
    certified rather than asserted."""
    n = len(Mx)

    def det(sub):
        k = len(sub)
        if k == 0:
            return F(1)
        Awork = [[Mx[i][j] for j in sub] for i in sub]
        d = F(1)
        for c in range(k):
            p = next((r0 for r0 in range(c, k) if Awork[r0][c] != 0), None)
            if p is None:
                return F(0)
            if p != c:
                Awork[c], Awork[p] = Awork[p], Awork[c]
                d = -d
            d *= Awork[c][c]
            pv = Awork[c][c]
            for r0 in range(c + 1, k):
                f0 = Awork[r0][c] / pv
                Awork[r0] = [x - f0 * y for x, y in zip(Awork[r0], Awork[c])]
        return d
    for k in range(1, n + 1):
        for sub in __import__("itertools").combinations(range(n), k):
            if det(list(sub)) < 0:
                return False
    return True


# Choi matrix of the witness channel, ordering |0>,|1> tensor basis.
CHOI_CL = [[F(1, 5), F(0), F(0), G_COH],
           [F(0), F(4, 5), F(0), F(0)],
           [F(0), F(0), F(1, 5), F(0)],
           [G_COH, F(0), F(0), F(4, 5)]]

XM = [[G(0), ONE], [ONE, G(0)]]
JM = [[G(-1), G(0)], [G(0), ONE]]
row("Q01", "C", "the grading flip X = sigma_x is a self-adjoint unitary "
    "involution with X J X = -J, and its Bloch action is diag(1, -1, -1)",
    mm(XM, XM) == eye(2) and ad(XM) == XM
    and mm(mm(XM, JM), XM) == [[-JM[i][j] for j in range(2)] for i in range(2)],
    "checked as exact matrices. Ad_X preserves the cone of positive "
    "semidefinite operators because X is unitary, so unlike the coordinate "
    "cone of block A there is nothing left to choose: the cone is canonical "
    "and the flip acts on it")

# Q02.  |kappa| < 1 from FAITHFULNESS ALONE - no alignment hypothesis.
faith_ok, faith_n, faith_max = True, 0, F(0)
for zn in range(-9, 10):
    for xn in range(-9, 10, 3):
        r = [F(xn, 10), F(0), F(zn, 10)]
        if sum(x * x for x in r) >= 1:
            continue
        faith_n += 1
        kap = -r[2]
        faith_ok &= (-1 < kap < 1)
        faith_max = max(faith_max, abs(kap))
row("Q02", "C", "THEOREM 3.7: a faithful fixed state gives |kappa| < 1 with no "
    "alignment hypothesis at all",
    faith_ok and faith_n > 40 and faith_max > F(4, 5),
    f"{faith_n} exact rational faithful states, |kappa| up to {faith_max}. "
    "The proof is one line: in the eigenbasis of J the diagonal entries of a "
    "faithful state are strictly positive and sum to one, so kappa is a "
    "strict convex combination of +1 and -1. Compare Theorem 3.4(i), which "
    "needed the grading to be diagonal in the cone's generating basis and "
    "which fails without it, row N08. Here the hypothesis is intrinsic to the "
    "state and no basis is chosen")

# ---- the sampled family of exactly rational positive trace-preserving maps
BASIS_CH = [(diag3([1, 1, 1]), ZERO3), (diag3([1, -1, -1]), ZERO3),
            (diag3([-1, 1, -1]), ZERO3), (diag3([-1, -1, 1]), ZERO3),
            (M_CL, T_CL)]
rng = random.Random(20260831)


def mix_ch(parts):
    return ([[sum(w * P[0][i][j] for w, P in parts) for j in range(3)]
             for i in range(3)],
            [sum(w * P[1][i] for w, P in parts) for i in range(3)])


def rand_ch():
    ws = [F(rng.randint(0, 4)) for _ in range(len(BASIS_CH) + 1)]
    tot = sum(ws)
    if tot == 0:
        return None
    r0 = [F(rng.randint(-3, 3), 8) for _ in range(3)]
    if sum(x * x for x in r0) > 1:
        r0 = [x / 2 for x in r0]
    cand = BASIS_CH + [(ZEROM, r0)]
    return mix_ch([(w / tot, P) for w, P in zip(ws, cand) if w])


def symmetrise(M, t):
    Mx, tx = bl_conj(M, t)
    return ([[(M[i][j] + Mx[i][j]) / 2 for j in range(3)] for i in range(3)],
            [(t[i] + tx[i]) / 2 for i in range(3)])


sym_ok, sym_n = True, 0
bud_ok, bud_n = True, 0
con_ok, con_n, con_live = True, 0, 0
for _ in range(400):
    ch = rand_ch()
    if ch is None:
        continue
    M, t = ch
    Ms, ts = symmetrise(M, t)
    rs = bl_fixed(Ms, ts)
    if rs is not None:
        sym_n += 1
        sym_ok &= (rs[1] == 0 and rs[2] == 0 and -rs[2] == 0)
    r = bl_fixed(M, t)
    if r is None:
        continue
    bud_n += 1
    kap = -r[2]
    bud_ok &= (kap * kap <= r[1] * r[1] + r[2] * r[2])
    Mx, tx = bl_conj(M, t)
    sg = [F(SGN[i]) * r[i] for i in range(3)]
    dv = [r[i] - sg[i] for i in range(3)]
    dif = [sum((M[i][j] - Mx[i][j]) * sg[j] for j in range(3))
           + (t[i] - tx[i]) for i in range(3)]
    fro2 = sum(M[i][j] ** 2 for i in range(3) for j in range(3))
    u = sqrt_ub(fro2)
    if u >= 1 or u * u < fro2:
        continue
    con_n += 1
    if sum(x * x for x in dv) > 0:
        con_live += 1
    con_ok &= ((1 - u) ** 2 * sum(x * x for x in dv)
               <= sum(x * x for x in dif))

row("Q03", "C", "THEOREM 3.8, THE NO-GO: a grading-flip covariant map with a "
    "unique fixed state has kappa = 0 exactly",
    sym_ok and sym_n > 300,
    f"{sym_n} exact rational maps, each obtained by symmetrising a sampled "
    "positive trace-preserving map over the flip, so each is covariant by "
    "construction and still positive and trace preserving. In every one the "
    "unique fixed state satisfies kappa = 0 exactly, not approximately. The "
    "proof is three lines: covariance sends the fixed state to a fixed state, "
    "uniqueness makes it the same state, and X J X = -J then forces kappa = "
    "-kappa. Consequence: phase capability is not a matter of finding a "
    "better positive map. It requires the action to BREAK the sector-exchange "
    "symmetry, which is gate F-M66.16")

cl_fix = bl_fixed(M_CL, T_CL)
cl_conj = bl_conj(M_CL, T_CL)
row("Q04", "W", "WITNESS in the surviving complement: an explicitly completely "
    "positive channel, not flip covariant, whose unique faithful fixed state "
    "has kappa = 3/5",
    principal_minors_nonneg(CHOI_CL)
    and cl_fix == [F(0), F(0), F(-3, 5)]
    and -cl_fix[2] == F(3, 5)
    and sum(x * x for x in cl_fix) < 1
    and (cl_conj[1] != T_CL),
    "the channel is p' = (1-a)p + bq, q' = ap + (1-b)q, c' = gc with a = 4/5, "
    "b = 1/5, g = 2/5. Complete positivity is CERTIFIED, not asserted: every "
    "principal minor of its exact rational Choi matrix is non-negative. Its "
    f"unique fixed state is diag(1/5, 4/5), faithful, with kappa = 3/5 and "
    "no coherence. It is not flip covariant, as Theorem 3.8 requires of any "
    "map with nonzero kappa. This is the whole content of the surviving "
    "complement: the class the no-go leaves alive is nonempty")

row("Q05", "C", "THE FLIP BUDGET: |kappa| is at most half the trace distance "
    "between the fixed state and its flip",
    bud_ok and bud_n > 300,
    f"{bud_n} exact cases. 2|kappa| = |Tr((rho - X rho X) J)| <= "
    "||rho - X rho X||_1 because ||J|| = 1. This is the exact analogue of the "
    "seam budget T = sqrt(1 - kappa^2) of paper 3.3, one level up: there the "
    "budget bounded the asymmetry of a ray against a grading, here it bounds "
    "the phase capability by the asymmetry of a state against the flip")

row("Q06", "C", "THEOREM 3.9, THE QUANTITATIVE FORM: the flip breaking of the "
    "map bounds kappa from above, with a certified rational contraction bound",
    con_ok and con_n > 300 and con_live > 250,
    f"{con_n} exact cases, {con_live} of them with a nonzero flip defect. The "
    "inequality checked is (1 - u)^2 ||rho - X rho X||_1^2 <= "
    "||(Phi - Phi^X)(X rho X)||_1^2, where u is a rational number certified "
    "in the same row to satisfy u^2 >= ||M||_F^2 >= ||M||_2^2, and ||M||_2 is "
    "the contraction coefficient of the map on traceless differences. "
    "Rearranged, |kappa| <= ||Phi - Phi^X|| / (2(1 - u)). A map that is "
    "nearly flip covariant cannot select a usefully phase-capable state, so "
    "the action needs not merely some symmetry breaking but a quantified "
    "amount of it")

ONE_DIR = (ZEROM, [F(3, 10), F(4, 10), F(0)])
od_fix = bl_fixed(*ONE_DIR)
od_conj = bl_conj(*ONE_DIR)
row("Q07", "X", "NEGATIVE CONTROL: the no-go runs one way only - kappa = 0 "
    "does not imply flip covariance",
    od_fix is not None and od_fix[2] == 0 and -od_fix[2] == 0
    and od_conj[1] != ONE_DIR[1]
    and sum(x * x for x in od_fix) < 1,
    "the replacement channel onto the faithful state with Bloch vector "
    "(3/10, 4/10, 0) has kappa = 0 and is NOT flip covariant, since the flip "
    "reverses the y component. So Theorem 3.8 excludes a class, it does not "
    "characterise one, and an action that breaks the symmetry still has to be "
    "checked for kappa rather than assumed to supply it")

reach_t = [F(0), F(1, 2), F(-1, 2), F(3, 5), F(-3, 5), F(9, 10), F(-9, 10),
           F(1, 100), F(-7, 9), F(5, 13)]
reach_ok = True
for tt in reach_t:
    ch = (ZEROM, [F(0), F(0), -tt])
    rr = bl_fixed(*ch)
    reach_ok &= (rr is not None and -rr[2] == tt and sum(x * x for x in rr) < 1)
row("Q08", "C", "reachability survives the move to the canonical cone: every "
    "exact rational target in (-1, 1) is realised by a channel",
    reach_ok and len(reach_t) == 10,
    f"{len(reach_t)} exact targets. The replacement channel rho -> "
    "Tr(rho) sigma_t onto the state diag((1-t)/2, (1+t)/2) is completely "
    "positive and trace preserving, its fixed state is sigma_t, which is "
    "faithful exactly when |t| < 1, and kappa = t. Theorem 3.6 therefore "
    "carries over unchanged, and together with Theorem 3.7 it says that on "
    "the canonical cone positivity constrains kappa by |kappa| < 1 and by "
    "nothing else, now with no hypothesis about a basis")

row("Q09", "D", "WHAT THE OPERATOR-STATE ROUTE REMOVES, WHAT IT BUYS THAT "
    "WITH, and what it leaves standing",
    True is not False,
    "CORRECTED IN v1.5 after round 5. The predecessor's wording said the "
    "generating-basis choice does not exist here and that nothing is lost in "
    "the move. Both are one layer too strong. REMOVED: the arbitrary "
    "generating basis. Once the carrier is B(H_boundary) the cone of positive "
    "semidefinite elements is canonical and kappa = Tr(rho J) is unchanged by "
    "conjugating the map and the grading together, row Q10, so no alignment "
    "remains to choose and the third alignment class of paper 3.2.1 has no "
    "analogue. BOUGHT WITH: a carrier choice. Passing from a vector psi_0 to "
    "a state rho and from a matrix P to a positive trace-preserving map Phi "
    "is not a change of coordinates but a lift from a vector-state model to "
    "an operator-state model, and nothing in this paper derives that lift "
    "from the action. Row Q11 declares it as construction choice (7) and row "
    "Q12 shows the price is not notional: the strict bound of Theorem 3.7 "
    "rests on faithfulness, no pure state is faithful in dimension two or "
    "more, and on pure states the two multipliers agree exactly, so the bound "
    "is bought precisely with the mixing the vector model does not have. LEFT "
    "STANDING: the action must supply the boundary map AND the lift, which is "
    "gate F-M66.15, and that map must break the sector exchange by a "
    "quantified amount, which is gate F-M66.16. NOT CLAIMED: that the lift is "
    "physically equivalent to the vector model, that the fixed state is a "
    "boundary state rather than an effective description, that the lift "
    "introduces no coarse graining, or that any of this is external "
    "mathematics; see rows R03, R28 and R29")

rot_ok, rot_n = True, 0
for perm in ((0, 1, 2), (1, 2, 0), (2, 0, 1)):
    for sgn in ((1, 1, 1), (1, -1, -1), (-1, 1, -1), (-1, -1, 1)):
        ch = rand_ch()
        if ch is None:
            continue
        M, t = ch
        r = bl_fixed(M, t)
        if r is None:
            continue
        Rm = [[F(sgn[i]) if perm[i] == j else F(0) for j in range(3)]
              for i in range(3)]
        Mr = [[sum(Rm[i][k] * M[k][l] * Rm[j][l]
                   for k in range(3) for l in range(3)) for j in range(3)]
              for i in range(3)]
        tr_ = [sum(Rm[i][k] * t[k] for k in range(3)) for i in range(3)]
        rr = bl_fixed(Mr, tr_)
        Jr = [sum(Rm[2][k] * (F(1) if k == 2 else F(0)) for k in range(3))]
        rot_n += 1
        # kappa computed against the rotated grading equals the original kappa
        kap_new = -sum(Rm[2][k] * r[k] for k in range(3)) * (F(1))
        kap_rot = -rr[2] if rr is not None else None
        rot_ok &= (rr is not None and kap_rot == kap_new)
row("Q10", "X", "NO RESIDUAL ALIGNMENT FREEDOM: rotating the map and the "
    "grading together leaves kappa unchanged",
    rot_ok and rot_n >= 9,
    f"{rot_n} exact cases over signed coordinate rotations. kappa is a "
    "function of the pair (map, grading) and not of any chosen frame, so the "
    "freedom that produced counterexample 2 in the coordinate formulation "
    "does not exist here. That is what makes gate F-M66.13 dissolve rather "
    "than merely narrow")

# ------------------------------------------------- G13 : same-object guard
G13_BAD = "The attenuation axis and the phase axis cannot be carried by the "\
          "same object."
G13_OK = "In this factorisation the two axes are represented by distinct "\
         "structures (SAME-OBJECT-OPEN)"


def same_object_hits(text):
    out = []
    for clause in re.split(r"[.;:!?]|\n|\||,", text):
        if re.search(r"same object", clause, re.I) and \
                "SAME-OBJECT-OPEN" not in clause:
            out.append(clause.strip()[:70])
    return out


g13_hits = same_object_hits(paper_text) if paper_present else []
row("G13", "G", "SAME-OBJECT GUARD, live-fired: the manuscript does not assert "
    "that one object cannot carry both axes unless the clause marks it open",
    (not paper_present and ARGS.no_manuscript)
    or (len(same_object_hits(G13_BAD)) == 1
        and len(same_object_hits(G13_OK)) == 0 and not g13_hits),
    f"live fire: the round-4 target sentence produced "
    f"{len(same_object_hits(G13_BAD))} hit and the corrected wording produced "
    f"{len(same_object_hits(G13_OK))}. Manuscript scan: offending clauses = "
    f"{g13_hits or 'none'}. Nothing in this line proves that a single "
    "action-derived generator or dilation cannot carry attenuation and phase "
    "at once; what is shown is that in the present factorisation they are "
    "carried by different structures" if paper_present else "not run")

row("R27", "D", "AUDIT ROUND 4 - v1.3 audit, response version 1.4",
    True is not False,
    "C1 S2. Paper 1 asserted that the two axes cannot be carried by the same "
    "object. ACCEPTED: not proved anywhere in this line, and the same U and "
    "the same ray enter both parts of the multiplier. Replaced by a statement "
    "about the present factorisation; guard G13 added. C2 S2. The reduction "
    "to one angle was stated as a reduction of the boundary-condition debt, "
    "but the full moduli space is U(2) and the chiral-bag U(1) was selected "
    "from outside. ACCEPTED: restated as a conditional parametrisation within "
    "an externally selected subfamily, and the missing first arrow registered "
    "as a gate. C3 S2. Corollary 3.5 said the two survival properties come "
    "apart exactly at T = 1, omitting sin theta != 0. ACCEPTED: phase capable "
    "is now defined as producing a nonzero imaginary part at SOME "
    "nondegenerate angle, under which the corollary is true as stated. C4 S2. "
    "The type of the transfer operator was under-specified. ACCEPTED: P is "
    "now declared real-linear on the real form fixed by the conjugation, with "
    "top eigenvalue meaning spectral radius, and the complex-linear case "
    "required to commute with the conjugation. C5 local. arg a is undefined "
    "at a = 0; the counterexample ray was written unnormalised while the "
    "setting fixes unit norm; the phase is generated by the CHOSEN "
    "parametrisation rather than by the grading as such. All three accepted "
    "and corrected. C6 RECOMMENDATION. Do not iterate a fifth correction-only "
    "version. ACCEPTED IN SUBSTANCE: this version is not correction-only, it "
    "carries block Q, and the line is proposed for freeze after it. C7 "
    "RECOMMENDATION. Move to a density-matrix cone and a positive map. "
    "ACCEPTED AND EXECUTED; see block Q and row R28. C8 PACKAGE. A downloaded "
    "copy renamed with a suffix breaks the release check. ACCEPTED as a "
    "packaging note: the registered names are load-bearing and a run under "
    "any other name is not a release check. Not accepted as stated: none. "
    "AUDITOR CREDIT: round 4 replayed this package independently and reported "
    "matching counts and digests, and it correctly noted that a passing run "
    "cannot see any of C1 to C5, which are statement defects")

row("R28", "D", "DEEP SEARCH AND BREAKTHROUGH RECORD for block Q",
    True is not False,
    "ROUTE CARD. Transformed question: the coordinate cone was a declared "
    "choice on a spinor boundary space; is there a positive structure there "
    "that is canonical? Minimal construction: replace the coordinate cone by "
    "the cone of positive semidefinite operators, the transfer matrix by a "
    "positive trace-preserving map, and the Perron ray by the fixed state; "
    "define kappa = Tr(rho J). Operators used: LAYER SPLIT, separating the "
    "positive structure from the coordinates that expressed it, and "
    "OBSTRUCTION TO OBJECT, turning the alignment obstruction into a symmetry "
    "requirement on the map. WHAT WAS GAINED. The declared choice is removed "
    "rather than declared; the strict bound follows from faithfulness alone; "
    "the third alignment class disappears; and the missing requirement "
    "becomes a symmetry statement with a quantitative floor. WHAT WAS NOT "
    "GAINED. No boundary map is derived from the action, so the frontier does "
    "not move. KILL TEST, pre-registered: if the action-derived boundary map "
    "turns out to commute with the sector exchange, Theorem 3.8 forces "
    "kappa = 0 and this entire route to a boundary phase dies, with no repair "
    "available short of an explicit symmetry-breaking term. That is a real "
    "kill test because it can be evaluated as soon as any candidate map "
    "exists, before any angle is computed. PRIOR ART, external. The "
    "Perron-Frobenius theory of positive and completely positive maps, "
    "including uniqueness and faithfulness of the fixed state for primitive "
    "maps, is established: Evans and Hoegh-Krohn, Albeverio and Hoegh-Krohn, "
    "and the finite-dimensional ergodic and mixing classification of Burgarth "
    "and coauthors. The symmetry argument is the standard uniqueness plus "
    "covariance implies invariance argument. The contraction bound is the "
    "standard fixed-point perturbation estimate with the Dobrushin "
    "coefficient. NOVELTY VERDICT UNCHANGED: external mathematical novelty is "
    "ZERO, and the contribution is the mapping onto this programme's "
    "requirement, which is corpus-internal. SEARCH LIMITS: four query "
    "families on quantum Perron-Frobenius and primitive channels; the "
    "boundary-map literature for bag models was NOT searched from the "
    "originals; NOT_FOUND would not have been ABSENT and no such claim is made")




# ================== BLOCK Q, v1.5 addendum : the lift is a choice, and its price
# Round 5's single substantive finding: block Q was written as though the move
# to the canonical cone removed a choice.  It replaced a BASIS choice with a
# CARRIER choice.  These three rows make that exact.

row("Q11", "D", "DECLARED CONSTRUCTION CHOICE (7): the operator-state lift",
    True is not False,
    "Paper 2.1 declares six construction choices for the coordinate route. "
    "This is the seventh and it belongs to the operator-state route: the "
    "carrier of the boundary positive structure is taken to be the algebra "
    "B(H_boundary) with its cone of positive semidefinite elements, the "
    "boundary state is taken to be a density operator rather than a vector, "
    "and the boundary transfer is taken to be a positive trace-preserving "
    "map. NOT DERIVED, any of it. Four questions stay open and are named here "
    "so that no later reader mistakes silence for settlement. Does the "
    "boundary action select a density-operator carrier at all? Does the "
    "boundary dynamics induce a positive or completely positive "
    "trace-preserving map? Is Tr(rho U) the right multiplier for the record "
    "interpretation, given that the coordinate route used a vector "
    "expectation? Is the faithful fixed state a boundary state, or an "
    "effective description whose mixing comes from a coarse graining the "
    "action has not been shown to contain? All four are folded into gate "
    "F-M66.15")

# Q12.  Where the strict bound actually comes from.  On pure states the two
# multipliers agree exactly, so the lift is faithful to the vector model there;
# but no pure state is faithful, so Theorem 3.7's hypothesis excludes exactly
# the states the vector model is made of.  The bound is bought with mixing.
pure_agree, pure_n = True, 0
pure_kappa_extreme = []
for xn in range(-4, 5):
    for zn in range(-4, 5):
        n2 = xn * xn + zn * zn
        if n2 == 0:
            continue
        # unit Bloch vector <=> pure state; use exact rational points on the
        # cone by comparing kappa computed both ways on the SAME state
        r = [F(xn, 5), F(0), F(zn, 5)]
        if sum(v * v for v in r) > 1:
            continue
        pure_n += 1
        # rho = (I + r.sigma)/2 ; Tr(rho J) with J = -sigma_z is -r_z
        kap_state = -r[2]
        # the coordinate reading of the same diagonal data: psi with
        # |psi_1|^2 = (1+r_z)/2, |psi_2|^2 = (1-r_z)/2 gives <psi|J|psi>
        p1, p2 = (1 + r[2]) / 2, (1 - r[2]) / 2
        kap_vec = -p1 + p2
        pure_agree &= (kap_state == kap_vec)
        if sum(v * v for v in r) == 1:
            pure_kappa_extreme.append(kap_state)
row("Q12", "C", "THE PRICE OF THE LIFT: the two multipliers agree on the "
    "diagonal data, and the strict bound is bought with faithfulness, which "
    "no pure state has",
    pure_agree and pure_n > 40,
    f"{pure_n} exact rational states. Tr(rho J) and the vector expectation "
    "<psi|J|psi> return the same number on the same diagonal data, so the "
    "lift does not change the quantity being bounded. What changes is the "
    "hypothesis available. A pure state has Bloch norm one and is never "
    "faithful in dimension two, so Theorem 3.7 says nothing about it, while "
    "the coordinate route of paper 3.4 lives entirely on such states. The "
    "strict bound |kappa| < 1 is therefore not obtained for free by changing "
    "carrier; it is obtained from mixing, and where that mixing comes from is "
    "part of gate F-M66.15 rather than a result of this paper")

pure_pole = [F(0), F(0), F(1)]
row("Q13", "X", "NEGATIVE CONTROL: without faithfulness the strict bound "
    "fails in the operator-state route as well",
    sum(v * v for v in pure_pole) == 1
    and -pure_pole[2] == -1
    and abs(-pure_pole[2]) == 1,
    "the pure state with Bloch vector (0, 0, 1) is a fixed state of the "
    "replacement channel onto itself, it is not faithful, and its kappa is "
    "-1 exactly, so T = 0. Theorem 3.7 is conditional on faithfulness in the "
    "same way that Theorem 3.4(i) was conditional on alignment. The "
    "difference is where the condition sits: alignment was a property of a "
    "frame nobody had chosen on physical grounds, faithfulness is a property "
    "of the state the dynamics selects. That is an improvement in the KIND of "
    "open question, not the closing of one")

# ============================ BLOCK G, v1.5 : the manuscript against itself
# Round 5 found five stale internal references that every previous run passed
# over, because no row read the manuscript as a cross-referenced document.
# These four guards do that.  Each is live-fired on injected text.

GATE_DEF_RE = re.compile(r"^\|\s*\*{0,2}(F-M66\.\d+)\*{0,2}\s*\|", re.M)
GATE_USE_RE = re.compile(r"F-M66\.\d+")
NC_DEF_RE = re.compile(r"^-\s*\*\*(NC-M66\.\d+)\*\*", re.M)
NC_USE_RE = re.compile(r"NC-M66\.\d+")
ROW_RE = re.compile(r"(?<![A-Za-z0-9-])([ABCDESNQGR])(\d{2})(?![0-9])")
THM_DEF_RE = re.compile(r"\*\*(?:Theorem|Corollary) (\d+\.\d+)")
THM_USE_RE = re.compile(r"\b(?:Theorem|Corollary) (\d+\.\d+)")
SEC_DEF_RE = re.compile(r"^#{2,3} (?:§)?(\d+(?:\.\d+)*[a-z]?)[.\s]", re.M)
SEC_USE_RE = re.compile(r"§(\d+(?:\.\d+)*[a-z]?)")


def gate_defects(text):
    defs = GATE_DEF_RE.findall(text)
    uses = set(GATE_USE_RE.findall(text))
    bad = []
    for g in sorted(uses - set(defs)):
        bad.append(f"{g} used but not defined in the gate table")
    for g in sorted(set(defs)):
        if defs.count(g) > 1:
            bad.append(f"{g} defined {defs.count(g)} times")
    # a gate whose table entry retires it must not be called OPEN elsewhere
    retired = set()
    for ln in text.splitlines():
        m = GATE_DEF_RE.match(ln)
        if m and re.search(r"RETIRED|CLOSED", ln):
            retired.add(m.group(1))
    # The clause splitter must not split INSIDE a gate identifier.  The first
    # form of this arm split on "." and therefore cut "F-M66.13" into "F-M66"
    # and "13 ...", so the arm never fired and its injection passed.  Same
    # surface-form family as the G11 and G09 cases; disclosed in row R16.
    # STRENGTHENED IN v1.5.1.  The first form looked for the literal word
    # OPEN and nothing else, so two places that used a retired gate in the
    # PRESENT TENSE - "it is gated at", "the alignment it presupposes is
    # gate" - passed the guard while contradicting the gate table.  A guard
    # that checks one word is checking a word, not the property.  The cue set
    # below covers present-tense usage; a clause that marks the reference as
    # historical in the SAME clause is exempt, and the marker must be in that
    # clause rather than nearby.
    LIVE_CUE = re.compile(r"\bOPEN\b|gated at|\bis gate\b|presupposes"
                          r"|is answered|\bremains\b|\bcurrent gate\b")
    HIST_MARK = re.compile(r"retired|historical|superseded|withdrawn",
                           re.I)
    for ln in text.splitlines():
        if GATE_DEF_RE.match(ln):
            continue
        safe = re.sub(r"F-M66\.(\d+)", r"F-M66_\1", ln)
        for clause in re.split(r"[.;:!?]|\||,", safe):
            if HIST_MARK.search(clause):
                continue
            for g in retired:
                if g.replace(".", "_") in clause and LIVE_CUE.search(clause):
                    bad.append(f"{g} is retired but used as a live gate")
    return sorted(set(bad))


def nc_defects(text):
    defs = NC_DEF_RE.findall(text)
    uses = set(NC_USE_RE.findall(text))
    bad = [f"{c} used but not defined" for c in sorted(uses - set(defs))]
    bad += [f"{c} defined twice" for c in sorted(set(defs))
            if defs.count(c) > 1]
    return bad


def row_ref_defects(text, ids):
    bad = []
    for a, b in set(ROW_RE.findall(text)):
        if a + b not in ids:
            bad.append(f"row {a}{b} cited but absent from this run")
    return sorted(bad)


def structure_defects(text):
    bad = []
    defs = set(THM_DEF_RE.findall(text))
    for u in sorted(set(THM_USE_RE.findall(text))):
        if u not in defs:
            bad.append(f"Theorem/Corollary {u} cited but not stated")
    secs = SEC_DEF_RE.findall(text)
    known = set(secs)
    for s in secs:                       # a parent section counts as defined
        parts = s.split(".")
        for k in range(1, len(parts)):
            known.add(".".join(parts[:k]))
    for ln in text.splitlines():
        if ln.startswith("- **[B-"):     # external locators are not our refs
            continue
        for u in SEC_USE_RE.findall(ln):
            if u.rstrip(".") not in known:
                bad.append(f"section {u} cited but no such heading")
    order = []
    for s in secs:
        parts = s.split(".")
        if len(parts) < 2 or not parts[0].isdigit():
            continue
        minor = parts[1].rstrip("abcd")
        if not minor.isdigit():
            continue
        order.append((int(parts[0]), int(minor)))
    for x, y in zip(order, order[1:]):
        if x[0] == y[0] and y[1] < x[1]:
            bad.append(f"subsections out of order: {x} then {y}")
    return sorted(set(bad))


G14_BAD = "| **F-M66.99** | a gate nobody defined | OPEN |"
G14_OK = "the gate table is the single place a gate is defined"
g14_hits = gate_defects(paper_text) if paper_present else []
row("G14", "G", "GATE REGISTRY GUARD, live-fired: every gate cited is defined "
    "exactly once, and no retired gate is called open elsewhere",
    (not paper_present and ARGS.no_manuscript)
    or (len(gate_defects("F-M66.99 is discussed here")) == 1
        and len(gate_defects("| **F-M66.13** | x | RETIRED |\nit is gated at "
                             "F-M66.13 here")) == 1
        and not gate_defects("| **F-M66.13** | x | RETIRED |\nF-M66.13 was "
                             "retired and is gated at nothing")
        and not gate_defects(G14_OK) and not g14_hits),
    f"live fire: a citation with no table entry produced "
    f"{len(gate_defects('F-M66.99 is discussed here'))} defect, a retired gate "
    "used in the present tense produced 1, and the same sentence marked "
    f"historical produced 0; clean text produced {len(gate_defects(G14_OK))}. Manuscript scan: "
    f"{g14_hits or 'no defects'}. Round 5 found a retired gate still quoted "
    "as an ordering constraint in the seed-fidelity section; this guard is "
    "what makes that class of drift fail the run instead of surviving it"
    if paper_present else "not run")

G15_BAD = "as NC-M66.99 already records"
g15_hits = nc_defects(paper_text) if paper_present else []
row("G15", "G", "NON-CLAIM REGISTRY GUARD, live-fired: every non-claim cited "
    "is defined exactly once",
    (not paper_present and ARGS.no_manuscript)
    or (len(nc_defects(G15_BAD)) == 1 and not g15_hits),
    f"live fire: a citation with no definition produced "
    f"{len(nc_defects(G15_BAD))} defect. Manuscript scan: "
    f"{g15_hits or 'no defects'}. Non-claims are the load-bearing part of a "
    "paper that claims nothing external, so a dangling one is worse here than "
    "a dangling result would be" if paper_present else "not run")

# the ledger so far; block Q and G14-G15 are already registered above,
# and the rows registered after this one are named explicitly below.
LATE_IDS = {"G09", "G10", "G16", "G17", "G18", "R19", "R29", "R30", "R31"}
ids_so_far = {r["id"] for r in ROWS} | LATE_IDS
G16_BAD = "certified in row Z99 and row A01"
g16_hits = row_ref_defects(paper_text, ids_so_far) if paper_present else []
row("G16", "G", "ROW REFERENCE GUARD, live-fired: every certificate row the "
    "manuscript cites exists in THIS run",
    (not paper_present and ARGS.no_manuscript)
    or (not row_ref_defects("row A01 and row Q04", ids_so_far)
        and len(row_ref_defects("row N99 was checked", ids_so_far)) == 1
        and not g16_hits),
    f"live fire: a citation of a row absent from the ledger produced "
    f"{len(row_ref_defects('row N99 was checked', ids_so_far))} defect and two "
    "live citations produced none. Manuscript scan over "
    f"{len(set(a + b for a, b in ROW_RE.findall(paper_text)))} distinct row "
    f"citations: {g16_hits or 'no defects'}. This is the guard that ties the "
    "paper to the ledger in the direction that was never checked: previous "
    "versions verified that the ledger's counts matched the paper's banner, "
    "not that the paper's citations matched the ledger's rows"
    if paper_present else "not run")

G17_BAD = "as Theorem 9.9 shows, and see §99.9"
g17_hits = structure_defects(paper_text) if paper_present else []
row("G17", "G", "STRUCTURE GUARD, live-fired: every theorem and section the "
    "manuscript cites exists, and subsections are in order",
    (not paper_present and ARGS.no_manuscript)
    or (len(structure_defects(G17_BAD)) == 2 and not g17_hits),
    f"live fire: a citation of an absent theorem and an absent section "
    f"produced {len(structure_defects(G17_BAD))} defects. Manuscript scan: "
    f"{g17_hits or 'no defects'}. Round 5 found the version-history "
    "subsections printed out of order, which is the kind of defect a reader "
    "notices and a run never did" if paper_present else "not run")

row("R29", "D", "AUDIT ROUND 5 - v1.4 audit, response version 1.5, and the "
    "close of the correction sequence", True is not False,
    "D1 S2, release blocking. Block Q and paper 3.7 were written as though "
    "the move to the cone of positive semidefinite operators removed a "
    "choice. ACCEPTED IN FULL: it replaced a basis choice with a carrier "
    "choice. The wording that the choice does not exist and that nothing is "
    "lost is withdrawn; row Q09 is rewritten, row Q11 declares the lift as "
    "construction choice (7), row Q12 shows the strict bound is bought with "
    "faithfulness that no pure state has, row Q13 is the matching negative "
    "control, and gate F-M66.15 now asks for the lift as well as the map. "
    "D2. Non-claim NC-M66.8 contradicted the retirement of gate F-M66.13. "
    "ACCEPTED: re-typed as historical and scoped to the coordinate route. D3. "
    "The seed-fidelity section still ordered a retired gate before F-M66.11. "
    "ACCEPTED: re-ordered as F-M66.15, then F-M66.16, then F-M66.11. D4. The "
    "scope sentence claimed every statement of paper 3 is relative to a "
    "declared cone, which paper 3.7 is not. ACCEPTED: split. D5. A reversal "
    "trigger still named the retired alignment problem. ACCEPTED: replaced by "
    "the operator-state failure modes. D6. This file's final printed line "
    "still concluded that the action must supply the cone. ACCEPTED: "
    "rewritten, and guard G14 now fails the run if a retired gate is called "
    "open anywhere in the manuscript. D7 packaging. The version-history "
    "subsections were printed out of order; guard G17 now checks that. Not "
    "accepted as stated: none. AUDITOR CREDIT: round 5 replayed this package "
    "under the registered names and reproduced 121/121 and the census, and "
    "its central finding is a layer confusion that four previous rounds and "
    "every passing run missed")

row("R30", "D", "FREEZE PROPOSAL and HANDOFF", True is not False,
    "PROPOSAL, not a decision, and CORRECTED IN v1.5.1: the predecessor row "
    "recorded this as a decision already taken and marked it user-approved, "
    "which pre-dated the approval it described. The approval standing behind "
    "this line was conditional on the paper being free of the defects an "
    "audit would find, and rounds 5 and 6 both found some. STATE: ZS-M66 is "
    "PROPOSED for freeze at v1.5.1 as a SUPPORT / METHOD technical note, "
    "TERMINAL-IN-SCOPE for the scope stated in paper 7, pending a delta "
    "re-audit and an explicit approval after it. No further substantive "
    "version of this line is planned. WHAT TERMINAL-IN-SCOPE WOULD NOT "
    "MEAN, once granted: it is not REVIEW READY, it is not externally reviewed, and it is "
    "not a claim that the paper is free of defects. Five audit rounds each "
    "found substantive defects, four of the five found defects that a passing "
    "run could not see, and the honest prior is that a sixth round would find "
    "more. Freezing is a decision to stop spending on this artifact, not a "
    "certificate about it, and it is not yet taken. Qualified-human anchor: "
    "still NONE. WHAT CARRIES "
    "FORWARD, and it is the whole point of the freeze: positivity does not "
    "select a phase-capable state; the coordinate formulation has an "
    "alignment freedom that no action fixes; in the operator-state route the "
    "sector-exchange symmetry forces kappa = 0 exactly, so the requirement is "
    "symmetry breaking with a quantified floor; and the open objects are the "
    "boundary map, the lift that gives it a carrier, and the selection of the "
    "chiral-bag subfamily from the full moduli. HANDOFF, no code assigned: "
    "the successor is a construction paper that builds a boundary positive or "
    "completely positive trace-preserving map from the Z-Spin boundary "
    "action, together with the operator-state lift that carries it, and then "
    "applies the pre-registered kill test. If the constructed map commutes "
    "with the sector exchange, Theorem 3.8 gives kappa = 0 and the boundary "
    "phase route ends there. If it does not commute, Theorem 3.9 converts the "
    "programme's required imbalance into a lower bound on the flip defect. If "
    "no map follows from the action at all, the construction has failed and "
    "that is also a result. A successor identifier is assigned when its "
    "release is approved, not here")




# ============================== BLOCK G, v1.5.1 : declared counts must be true
# Round 6 found paper 1 announcing five statements and printing six.  G17
# checks that cited theorems and sections exist and that subsections are in
# order; it does not read an announced count.  This one does.
COUNT_WORDS = {"two": 2, "three": 3, "four": 4, "five": 5, "six": 6,
               "seven": 7, "eight": 8, "nine": 9, "ten": 10}
COUNT_RE = re.compile(r"^(Two|Three|Four|Five|Six|Seven|Eight|Nine|Ten) "
                      r"(sentences|statements|items|points|reasons)\.$",
                      re.M)


def count_defects(text):
    bad = []
    lines = text.splitlines()
    for i, ln in enumerate(lines):
        m = COUNT_RE.match(ln.strip())
        if not m:
            continue
        declared = COUNT_WORDS[m.group(1).lower()]
        seen, j = 0, i + 1
        while j < len(lines):
            s = lines[j].strip()
            if re.match(r"^\d+\.\s", s):
                seen += 1
            elif s and seen:
                break
            j += 1
        if seen != declared:
            bad.append(f"declares {declared} {m.group(2)} but prints {seen}")
    return bad


G18_BAD = "Five statements.\n\n1. a\n2. b\n3. c\n4. d\n5. e\n6. f\n"
G18_OK = "Six statements.\n\n1. a\n2. b\n3. c\n4. d\n5. e\n6. f\n"
g18_hits = count_defects(paper_text) if paper_present else []
row("G18", "G", "ENUMERATION GUARD, live-fired: an announced count of "
    "statements matches the number printed",
    (not paper_present and ARGS.no_manuscript)
    or (len(count_defects(G18_BAD)) == 1 and not count_defects(G18_OK)
        and not g18_hits),
    f"live fire: an announcement of five over a list of six produced "
    f"{len(count_defects(G18_BAD))} defect and the corrected announcement "
    f"produced {len(count_defects(G18_OK))}. Manuscript scan: "
    f"{g18_hits or 'no defects'}. This is the smallest defect any round has "
    "reported and it survived five audits and 130 passing rows, which is the "
    "argument for the guard rather than for a proofread"
    if paper_present else "not run")

row("R31", "D", "AUDIT ROUND 6, DELTA - v1.5 audit, response version 1.5.1, "
    "correction only", True is not False,
    "E1 S2, release blocking. v1.5 recorded the freeze and the user approval "
    "for it as accomplished facts, in the manuscript cover, in paper 10.7, in "
    "row R30 and in this file's final printed line, while the audit the "
    "freeze was conditional on had not run. ACCEPTED IN FULL. This is a "
    "release-metadata defect and not a wording one: a conditional approval "
    "was written into the record as a past decision, and a row PASSing on it "
    "certified nothing except that the sentence was present. The label is now "
    "PROPOSED-FOR-FREEZE, the approval line is withdrawn, and the final "
    "freeze record is to be created only after a delta re-audit passes. "
    "E2 S1, internal coherence. Paper 2.1 said the choice is gated at "
    "F-M66.13 and paper 3.4 said the alignment it presupposes is gate "
    "F-M66.13, while the gate table calls that gate retired. ACCEPTED: both "
    "are re-typed as historical coordinate-route limitations superseded by "
    "F-M66.15 and F-M66.16. The guard's PASS on this was a SEMANTIC FALSE "
    "NEGATIVE: G14 searched for the literal word OPEN, and present-tense use "
    "of a retired gate does not contain it. G14 is strengthened here with a "
    "present-tense cue set and a same-clause historical exemption, and the "
    "strengthened form is live-fired both ways. E3 S1, structure. Paper 1 "
    "announced five statements and printed six. ACCEPTED; guard G18 added. "
    "Not accepted as stated: none. AUDITOR CREDIT: round 6 replayed the "
    "package, reproduced 130/130 and the digests of manuscript, companion and "
    "log, and then found that a guard added in the same version to prevent "
    "exactly this class of drift had a hole in it. THE STANDING LESSON OF "
    "THIS LINE, now at its fourth instance: every guard this package has "
    "added was wrong on its first form, and G14 is the first that was wrong "
    "in a way its own injection could not reveal, because the injection "
    "tested the word the guard looked for. An injection that reuses the "
    "guard's own vocabulary tests the implementation and not the property")


# ------------------------------------------- provenance, over the full ledger
# These two rows are emitted last because they measure the ledger, and a
# measurement taken mid-file would count only the rows written so far.  The two
# rows are pre-registered so that they count themselves.
cur_ids = {r["id"]: r["class"] for r in ROWS}
cur_ids["G09"], cur_ids["G10"], cur_ids["R19"] = "G", "G", "D"

# G09.  Internal version coherence, CPN11.  Not a token-existence check: the
# manuscript's own printed self-description must AGREE with this run.  The
# projected census counts the three rows still to be emitted, which is why they
# are registered above rather than inferred.
final_census = {}
for cls in cur_ids.values():
    final_census[cls] = final_census.get(cls, 0) + 1
BANNER = " ".join(f"{k}={final_census[k]}" for k in sorted(final_census))
coh = []
if paper_present:
    if f"rows={len(cur_ids)}" not in paper_text:
        coh.append(f"manuscript does not print rows={len(cur_ids)}")
    if os.path.basename(__file__) not in paper_text:
        coh.append("manuscript does not name this companion")
    if PREDECESSOR_PAPER in paper_text and "SUPERSEDED" not in paper_text:
        coh.append("predecessor named without a supersession statement")
    if BANNER not in paper_text:
        coh.append(f"manuscript census banner does not match '{BANNER}'")
    for stale in ("four verifiers", "Companion verifiers:"):
        if stale in paper_text:
            coh.append(f"stale package wording present: {stale!r}")
# CPN11 extended in v1.3.  Round 3 found this file's own header, usage line and
# release-metadata row still describing v1.1 while every executable constant
# said v1.2, and this guard passed because it read only the manuscript.  A
# version-coherence guard that cannot see its own version string checks the
# surface and not the property.  The scan below is over THIS source, with the
# legacy map, the frozen predecessor ledgers and the correction prose exempt,
# since those must name older versions to do their job.
# Frozen-data regions are exempt because the legacy map and the predecessor
# ledgers must name older versions to do their job.  The exemption is computed
# by brace matching over the named assignments, NOT by "a marker line turns
# exemption on until some line looks like a terminator": the first form of this
# scan used that shape and silently exempted the whole rest of the file, so the
# stale-version injection F14 passed.  Same surface-form failure, third
# occurrence in this line; recorded in row R16.
FROZEN_NAMES = ("LEGACY_FILE_MAP", "V10_LEDGER", "V11_LEDGER", "V12_LEDGER",
                "V13_LEDGER", "V14_LEDGER", "RETYPED_IN_V11",
                "RETYPED_IN_V12", "RETYPED_IN_V13", "RETYPED_IN_V14",
                "RETYPED_IN_V15", "V15_LEDGER", "RETYPED_IN_V151")
src_lines = SRC.splitlines()
exempt_lines = set()
for name in FROZEN_NAMES:
    m = re.search(rf"^{name} = " + r"\{", SRC, re.M)
    if not m:
        continue
    depth, k = 0, m.start()
    while k < len(SRC):
        if SRC[k] == "{":
            depth += 1
        elif SRC[k] == "}":
            depth -= 1
            if depth == 0:
                break
        k += 1
    first = SRC.count("\n", 0, m.start()) + 1
    last = SRC.count("\n", 0, k) + 1
    exempt_lines.update(range(first, last + 1))
# Prose that declares a predecessor AS a predecessor is also not stale.  The
# unit of exemption is the ROW CALL, not the physical line: a declaration row
# is one logical statement wrapped across many lines, and marking only the
# line that happens to carry the word "superseded" splits a record in half.
SUPERSESSION_MARK = ("superseded", "SUPERSEDED", "PREDECESSOR_PAPER",
                     "-> block", "-> all blocks", "predecessor", "H-02")
row_starts = [SRC.count("\n", 0, m.start()) + 1
              for m in re.finditer(r'^row\("', SRC, re.M)]
row_starts.append(len(src_lines) + 1)
# One row is NEVER exempt: R01 carries the CURRENT release metadata, and it is
# the row round 3 found stale.  Exempting it because its own prose contains the
# word "superseded" would exempt precisely the statement under audit.
NEVER_EXEMPT = ('row("R01"',)
for a, b in zip(row_starts, row_starts[1:]):
    body = "\n".join(src_lines[a - 1:b - 1])
    if any(tok in body for tok in NEVER_EXEMPT):
        continue
    if any(tok in body for tok in SUPERSESSION_MARK):
        exempt_lines.update(range(a, b))
# The docstring's legacy inventory is one logical block as well.  Lines inside
# a never-exempt row are excluded from this per-line pass too.
never_span = set()
for a, b in zip(row_starts, row_starts[1:]):
    if any(tok in "\n".join(src_lines[a - 1:b - 1]) for tok in NEVER_EXEMPT):
        never_span.update(range(a, b))
for ln_no, ln in enumerate(src_lines, 1):
    if ln_no not in never_span and any(tok in ln for tok in SUPERSESSION_MARK):
        exempt_lines.add(ln_no)
self_stale = []
for ln_no, ln in enumerate(src_lines, 1):
    if ln_no in exempt_lines:
        continue
    if re.search(r"zs_m66_verify_v1_[0-5]\.py|ZS-M66_v1_[0-5]\.md", ln):
        self_stale.append(f"line {ln_no}: stale artifact name")
    if re.search(r"ZS-M66 v1\.[0-5]\b", ln) and "v1.5.1" not in ln \
            and "v1.0" not in ln:
        self_stale.append(f"line {ln_no}: stale release string")
coh += self_stale
row("G09", "G", "internal version coherence, CPN11: the manuscript AND this "
    "source agree with this run on version, companion name and census",
    (not paper_present and ARGS.no_manuscript) or not coh,
    (f"expected rows={len(cur_ids)} and census '{BANNER}'; self-scan over "
     f"{len(SRC.splitlines())} source lines; mismatches: "
     f"{coh if coh else 'none'}" if paper_present else "not run"))

carried = sorted(i for i in cur_ids
                 if i in V15_LEDGER and V15_LEDGER[i] == cur_ids[i])
retyped = sorted(i for i in cur_ids
                 if i in V15_LEDGER and V15_LEDGER[i] != cur_ids[i])
added = sorted(i for i in cur_ids if i not in V15_LEDGER)
removed = sorted(i for i in V15_LEDGER if i not in cur_ids)
lineage_ok = (len(V10_LEDGER) == 74 and len(V11_LEDGER) == 90
              and len(V12_LEDGER) == 103 and len(V13_LEDGER) == 108
              and len(V14_LEDGER) == 121 and len(V15_LEDGER) == 130
              and set(RETYPED_IN_V11) == {"D16"}
              and set(RETYPED_IN_V12) == {"N05"}
              and set(RETYPED_IN_V13) == {"C07", "C08"}
              and not RETYPED_IN_V14 and not RETYPED_IN_V15
              and not RETYPED_IN_V151)
PROVENANCE = {"carried_unchanged": len(carried), "retyped": len(retyped),
              "added": len(added), "removed": len(removed)}
row("G10", "G", "ledger provenance against the v1.5 run is computed, and every "
    "reclassification is declared in advance",
    lineage_ok
    and set(retyped) == set(RETYPED_IN_V151)
    and not removed
    and len(carried) + len(retyped) + len(added) == len(cur_ids),
    f"carried_unchanged={len(carried)}, retyped={len(retyped)} {retyped}, "
    f"added={len(added)} {added}, removed={len(removed)}. Nothing from the "
    "v1.5 ledger is deleted, and no row changes class in this version: "
    "RETYPED_IN_V151 is empty, as the two before it were. Rounds 4, 5 and 6 "
    "all returned major revisions against runs that passed every row, because "
    "their defects were statement, cross-reference and release-metadata "
    "defects. Lineage: 74 rows at v1.0, 90 at v1.1, 103 at v1.2, 108 at v1.3, "
    "121 at v1.4, 130 at v1.5, and all six ledgers are retained above so that "
    "provenance stays auditable")
row("R19", "D", "LEDGER PROVENANCE, v1.5 -> v1.5.1, measured by row G10",
    True is not False,
    f"carried_unchanged={PROVENANCE['carried_unchanged']}, "
    f"retyped={PROVENANCE['retyped']}, added={PROVENANCE['added']}, "
    f"removed={PROVENANCE['removed']}. No row is retyped in this "
    "version and none is deleted; the v1.5 evidence is carried whole and "
    "two rows are added on top of it. Residual drift on carried "
    "rows is zero by construction, since every carried row recomputes the same "
    "exact rational quantity from the same inputs and this file was not "
    "re-tuned")

# ============================================================== summary
# G16 had to whitelist the rows registered after it; this closes that
# hole from the other side, fail-closed, once the ledger is complete.
assert LATE_IDS <= {r["id"] for r in ROWS}, \
    sorted(LATE_IDS - {r["id"] for r in ROWS})
assert len(ROWS) == EXPECTED_ROWS, f"row count {len(ROWS)} != {EXPECTED_ROWS}"

fails = [r for r in ROWS if not r["ok"]]
width = max(len(r["id"]) for r in ROWS)
for r in ROWS:
    print(f"{r['id']:<{width}} [{r['class']}] {r['name']}: "
          f"{'PASS' if r['ok'] else 'FAIL'}")
    print(f"{'':<{width}}      | {r['detail']}")

cen = {}
for r in ROWS:
    cen[r["class"]] = cen.get(r["class"], 0) + 1
print()
print("CENSUS " + " ".join(f"{k}={cen[k]}" for k in sorted(cen)))
print(f"       evidence C={cen.get('C',0)} V={cen.get('V',0)} "
      f"W={cen.get('W',0)} P={cen.get('P',0)} | controls R={cen.get('R',0)} "
      f"G={cen.get('G',0)} | non-evidence X={cen.get('X',0)} "
      f"D={cen.get('D',0)} T={cen.get('T',0)}")
print(f"SUMMARY rows={len(ROWS)} PASS={len(ROWS)-len(fails)} FAIL={len(fails)}")
print(f"PROVENANCE v1.5 -> v1.5.1 "
      + " ".join(f"{k}={v}" for k, v in PROVENANCE.items()))
print(f"SELF {os.path.basename(__file__)} "
      f"sha256={hashlib.sha256(SRC.encode()).hexdigest()[:16]}...")
if paper_present:
    print(f"PAPER {PAPER} sha256={paper_sha[:16]}...")
else:
    print("PAPER absent; this run is not a release check")
print("SCOPE flat boundary, free Dirac, single chiral angle | no derivation "
      "from an action | selection NOT shown | frontier OPEN -> OPEN")
print("WITHDRAWN-V1.1 positivity improving does NOT entail a phase-capable "
      "PF state; the action must separately select kappa != 0")
print("ALIGNMENT-CLASS-3 in the coordinate formulation the cone remains a "
      "choice: the two cases of 3.2 are not exhaustive and outside branch (b) "
      "even |kappa| < 1 fails")
print("OPERATOR-STATE the PSD route removes the basis alignment CONDITIONALLY "
      "on a declared operator-state lift which is not derived; the "
      "action-derived boundary map, its lift, and its symmetry breaking all "
      "remain OPEN")
print("FREEZE-PENDING-AUDIT ZS-M66 v1.5.1 is PROPOSED for freeze as terminal "
      "in scope; the freeze is NOT recorded as taken and requires a delta "
      "re-audit and an explicit approval after it")
sys.exit(0 if not fails else 1)
