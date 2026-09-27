#!/usr/bin/env python3
"""ZS-M73 v2.2.1 verification driver (correction-only release).
Full profile: extracts the byte-identical v2.2 release into a temporary directory and runs its unchanged
driver (89 rows, which reruns the v2.1 and v2.0 verifiers), reports V22-SQ-TAIL with its effective class V
(audit finding F32-01), then runs the eight v2.2.1 correction rows.
No row certifies Hypothesis EG-C, external novelty, significance or a research grade."""
import argparse, collections, hashlib, json, os, platform, subprocess, sys, tempfile, time, zipfile
from pathlib import Path
HERE = Path(__file__).resolve().parent
V22_SHA = '80a13ed602f3c4e194c3709e10289fb7391e8b26d73133384c4b253cc3b42f08'
N_NEW_HISTORY = 2


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--delta-only', action='store_true')
    ap.add_argument('--output', default='zs_m73_verify_v2_2_1.json')
    args = ap.parse_args(); start = time.time(); rows = []
    archive = HERE / 'provenance/ZS-M73_v2_2_release.zip'
    assert hashlib.sha256(archive.read_bytes()).hexdigest() == V22_SHA, 'Frozen v2.2 ZIP changed'
    inherited = None
    if not args.delta_only:
        with tempfile.TemporaryDirectory(prefix='m73-v221-') as td:
            root = Path(td)
            with zipfile.ZipFile(archive) as z:
                for info in z.infolist():
                    p = Path(info.filename)
                    assert not p.is_absolute() and '..' not in p.parts, 'Unsafe archive path'
                    assert (info.external_attr >> 16) & 0o170000 != 0o120000, 'Symlink in archive'
                z.extractall(root)
            d = root / 'ZS-M73_v2_2'
            run = subprocess.run([sys.executable, str(d / 'zs_m73_verify_v2_2.py'), '--output', str(root / 'v22.json')],
                                 cwd=d, capture_output=True, text=True)
            if run.returncode:
                raise RuntimeError('Frozen v2.2 driver failed:\n' + run.stdout[-3000:] + '\n' + run.stderr[-3000:])
            inherited = json.loads((root / 'v22.json').read_text())
            for r in inherited['rows']:
                if r['id'] == 'V22-SQ-TAIL':
                    r['class_emitted_by_v22'] = r['class']; r['class'] = 'V'
                    r['reclassification'] = 'F32-01: a six-point monotonicity check is a diagnostic, not a certificate of the infinite tail'
                if r['id'] == 'V22-SQ-CERT':
                    r['note_v221'] = 'F32-02: acceptance gate .9885; the stated .98853 is certified by V221-SQ-CERT-98853'
            rows.extend(inherited['rows'])
            print('Inherited v2.2 profile:', inherited['census'], flush=True)
    sys.path.insert(0, str(HERE / 'v221'))
    import checks as c

    def row(name, kind, ok, detail):
        rows.append({'id': name, 'class': kind, 'result': 'PASS' if ok else 'FAIL', 'detail': detail})
        print(name, rows[-1]['result'], flush=True)
    x = c.sq_cert_98853(); row('V221-SQ-CERT-98853', 'C', x['ok'], x)
    x = c.gate_fault(); row('V221-SQ-GATE-FAULT', 'R', x['ok'], x)
    x = c.branch_jump(); row('V221-BRANCH-JUMP', 'R', x['ok'], x)
    x = c.tail_scope(); row('V221-TAIL-SCOPE', 'V', x['ok'], x)
    x = c.tail_audit_repro(); row('V221-TAIL-AUDIT-REPRO', 'V', x['ok'], x)
    x = c.preservation(str(archive), str(HERE / 'ZS-M73_v2_2_1.md'), str(HERE / 'v221/edit_register.json'))
    row('V221-PRESERVATION', 'G', x['ok'], x)
    x = c.history_check(str(HERE / 'history_h0001-h0416.md'), str(archive), N_NEW_HISTORY); row('V221-HISTORY', 'G', x['ok'], x)
    x = c.provenance(str(archive), str(HERE / 'provenance/ZS-M73_v2_2_audit_evidence.zip')); row('V221-PROVENANCE', 'G', x['ok'], x)
    counts = collections.Counter(r['result'] for r in rows); classes = collections.Counter(r['class'] for r in rows)
    import numpy, scipy, mpmath, sympy
    record = dict(artifact='zs_m73_verify_v2_2_1', profile='V221-DELTA-8' if args.delta_only else 'PORTABLE-M73-97',
        rows=rows, census={'total': len(rows), 'PASS': counts['PASS'], 'FAIL': counts['FAIL'], 'SKIPPED': counts['SKIPPED'],
                           'classes': dict(sorted(classes.items()))},
        inherited_census_as_emitted=None if inherited is None else inherited['census'], v22_archive_sha256=V22_SHA,
        runtime={'python': platform.python_version(), 'numpy': numpy.__version__, 'scipy': scipy.__version__,
                 'mpmath': mpmath.__version__, 'sympy': sympy.__version__},
        seconds=round(time.time() - start, 2), limitations=[
            'Inherited rows concern the frozen v2.2, v2.1 and v2.0 manuscripts and code; the v2.2 code is not modified.',
            'Classes are effective classes: V22-SQ-TAIL is counted as V (emitted as C by the v2.2 driver).',
            'V221-SQ-CERT-98853 certifies the stated formulas on [1+log2,1e15]; the tail beyond is the analytic argument of Section 8.17.5.',
            'V221-TAIL-AUDIT-REPRO checks constants of the audit\'s tail reconstruction, not its inequalities.',
            'No row certifies EG-C, novelty, significance or a research grade.'])
    Path(args.output).write_text(json.dumps(record, indent=1, default=float) + '\n')
    print(json.dumps(record['census']))
    return int(counts['FAIL'] > 0)


if __name__ == '__main__':
    sys.exit(main())
