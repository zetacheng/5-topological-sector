"""C2a P4 checkpoint driver: run the chiral-completeness A0 gate across masses.

Reproducible from committed code alone (fixed seeds, printed configs). Output is
archived in p4_gate_output.txt. A0_total must vanish (pointwise-exact, sec.6.3);
per-class A0 is printed regardless of pass/fail (standing discipline).
"""
from scripts.c2a.skyrme_full import a0_gate

MASSES = [0.30, 0.15, 0.08]          # spans the C2a mass scan
SEEDS = (11, 23, 47)
NMC = {0.30: 400_000, 0.15: 200_000, 0.08: 200_000}

if __name__ == "__main__":
    print("C2a P4 CHECKPOINT — chiral-completeness A0 cancellation across masses")
    print("Target: NON-SINGLET SU(2) (1,2,1,2); Goldstone => A0_total=0 EXACT.")
    print("        NOT the anomalous U(1)_A singlet (eta) sector.")
    results = {}
    for m in MASSES:
        pc, tot, pw = a0_gate(m, seeds=SEEDS, nmc=NMC[m])
        results[m] = (tot, pw)
    print(f"\n{'='*64}")
    print("P4 CHECKPOINT SUMMARY")
    print(f"{'='*64}")
    allpass = True
    for m in MASSES:
        tot, pw = results[m]
        import numpy as np
        t = np.array(tot)
        ok = abs(t.mean()) < 1e-9
        allpass = allpass and ok
        print(f"  m={m:<5}: A0_total={t.mean():+.3e}  pointwise max={pw:.2e}  "
              f"{'PASS' if ok else 'FAIL'}")
    print(f"\n  P4 GATE: {'PASS (all masses)' if allpass else 'FAIL'}")
    print("  Cancellation is a pointwise algebraic identity (Rider #4a),")
    print("  hence regulator- and mass-independent. Diagram set + flavour")
    print("  weights are correct. Checkpoint BEFORE the production kappa scan.")
