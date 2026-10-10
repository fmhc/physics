#!/usr/bin/env python3
"""ATOM-KERNEL-0. Prepared source, not evidence of execution. CPU on .69 only.

After coordination/review: python atom_kernel.py --output NEW_DIRECTORY
No NPZ, protected experiment inputs, services, fitting or atomic dynamics.
"""
import argparse
import hashlib
import importlib
import itertools
import json
import math
import os
from pathlib import Path
import platform
import resource
import signal
import subprocess
import sys
import time

# Must precede scientific imports. One process, one allowed logical CPU.
for _key in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS",
             "NUMEXPR_NUM_THREADS", "BLIS_NUM_THREADS", "VECLIB_MAXIMUM_THREADS"):
    os.environ[_key] = "1"
sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
SOURCE = ROOT / "coordination/runden-v3/RUNDE-52/prisma-maxwell-1/code"
INPUTS = ("pm.py", "rv.py", "ew.py", "tp.py", "danzer_naeherung.py", "licht_netz.py")
PARAMETERS = {
    "boxes": [4, 6], "charge_e": 1.0, "source_vertex": 0,
    "source": "integrated vertex delta; common sublattice; no star0 multiplier",
    "hand_x": -23.0 / 7.0, "hand_y": -32.0 / 7.0,
    "directions": [[1, 0, 0], [0, 1, 0], [0, 0, 1], [1, -1, 0]],
    "steps": [1, 2], "ewald_cutoffs": [4, 6],
    "algebra_tolerance": 1e-9, "eigen_relative_cutoff": 1e-12,
    "reference_absolute_tolerance": 1e-8,
    "cpu_soft_seconds": 55, "cpu_hard_seconds": 58, "wall_seconds": 57,
}


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def git(*args):
    return subprocess.check_output(["git", "-C", str(ROOT), *args], text=True,
                                   timeout=3).strip()


def publish(path, obj):
    temporary = path.with_suffix(".tmp")
    temporary.write_text(json.dumps(obj, indent=2, allow_nan=False) + "\n")
    os.replace(temporary, path)


def expired(signum, frame):
    raise TimeoutError("Predeclared wall/CPU budget exhausted")


def matrices(pm, geometry, size):
    # Exactly pm's Bloch d0 convention; avoid constructing unrelated d1 action.
    shifts, blocks = pm.koeff(geometry["d0"], geometry["nE"], geometry["nV"])
    q = np.array(list(itertools.product(2 * np.pi * np.fft.fftfreq(size), repeat=3)))
    d = np.einsum("qn,nev->qev", np.exp(1j * (q @ shifts.T)), blocks)
    lap = np.einsum("qev,e,qew->qvw", d.conj(), geometry["s1"], d)
    return q, d, lap


def continuum_green(displacement, box, cutoff):
    """Zero-mean periodic -Delta Green function in rationalized 3D units.

    Point-source Ewald cross term only. No continuum point selfenergy exists.
    Rows of box are primitive translations; k = 2pi m @ inv(box).T.
    """
    volume = abs(np.linalg.det(box))
    eta = 2.0 / min(np.linalg.norm(box, axis=1))
    indices = np.array(list(itertools.product(range(-cutoff, cutoff + 1), repeat=3)))
    distances = np.linalg.norm(displacement + indices @ box, axis=1)
    if np.any(distances < 1e-12):
        raise ValueError("Coincident periodic sources have divergent continuum selfenergy")
    real = sum(math.erfc(eta * float(r)) / (4 * math.pi * float(r)) for r in distances)
    modes = indices[np.any(indices != 0, axis=1)]
    k = 2 * np.pi * modes @ np.linalg.inv(box).T
    k2 = np.sum(k * k, axis=1)
    reciprocal = np.sum(np.exp(-k2 / (4 * eta * eta)) * np.cos(k @ displacement) / k2) / volume
    return float(real + reciprocal - 1 / (4 * eta * eta * volume))


def box_result(pm, geometry, size):
    q, d, lap = matrices(pm, geometry, size)
    ev, vectors = np.linalg.eigh(lap)
    threshold = PARAMETERS["eigen_relative_cutoff"] * max(1.0, float(ev.max()))
    small = np.abs(ev) <= threshold
    if np.any(ev < -threshold) or int(small.sum()) != 1 or not small[0, 0]:
        raise ValueError("Expected exactly the constant gauge zero mode and positive complement")
    inverse_ev = np.zeros_like(ev)
    np.divide(1.0, ev, out=inverse_ev, where=~small)
    inverse = (vectors * inverse_ev[:, None, :]) @ vectors.conj().transpose(0, 2, 1)
    nv = geometry["nV"]
    shape = (size, size, size, nv)
    def solve(source):
        modes = np.fft.fftn(source, axes=(0, 1, 2)).reshape(-1, nv)
        potential_modes = np.einsum("qvw,qw->qv", inverse, modes)
        potential = np.fft.ifftn(potential_modes.reshape(shape), axes=(0, 1, 2))
        residual = np.einsum("qvw,qw->qv", lap, potential_modes) - modes
        return potential, float(np.linalg.norm(residual) / max(1.0, np.linalg.norm(modes)))
    def dot(a, b):
        return float(np.vdot(a, b).real)
    u = np.zeros(shape)
    u[0, 0, 0, 0] = 1
    # L+ always subtracts the same uniform integrated-charge background.
    background = 1.0 / u.size
    pu, gu = solve(u - background)
    self_u = 0.5 * dot(u, pu)
    constant = np.ones(nv)
    controls = {
        "gauss_relative_max": gu,
        "constant_d0_max": float(np.max(np.abs(d[0] @ constant))),
        "hermitian_max": float(np.max(np.abs(lap - lap.conj().transpose(0, 2, 1)))),
        "neutrality_max": 0.0, "gauge_energy_change_max": 0.0,
        "gauge_field_change_max": 0.0, "sign_reversal_max": 0.0,
        "reciprocity_max": 0.0, "decomposition_max": 0.0,
        "field_energy_identity_max": 0.0, "imaginary_potential_max": 0.0,
        "self_translation_max": 0.0, "continuum_convergence_max": 0.0,
    }
    rows = []
    for direction, step in itertools.product(PARAMETERS["directions"], PARAMETERS["steps"]):
        shift = np.array(direction) * step
        v = np.roll(u, tuple(shift), axis=(0, 1, 2))
        source = u - v
        potential, gauss = solve(source)
        pv, gv = solve(v - background)
        negative_potential, gn = solve(-source)
        energy = 0.5 * dot(source, potential)
        self_v = 0.5 * dot(v, pv)
        cross = -dot(u, pv)
        modes = np.fft.fftn(potential, axes=(0, 1, 2)).reshape(-1, nv)
        field = np.einsum("qev,qv->qe", d, modes)
        field_energy = float(np.sum(geometry["s1"][None, :] * abs(field) ** 2) / (2 * size ** 3))
        gauge_modes = np.fft.fftn(potential + 3.25, axes=(0, 1, 2)).reshape(-1, nv)
        gauge_field = np.einsum("qev,qv->qe", d, gauge_modes)
        displacement = shift @ geometry["A3"]
        refs = [continuum_green(displacement, size * geometry["A3"], cutoff)
                for cutoff in PARAMETERS["ewald_cutoffs"]]
        measured = {
            "gauss_relative_max": max(gauss, gv, gn),
            "neutrality_max": abs(float(source.sum())),
            "gauge_energy_change_max": abs(0.5 * dot(source, potential + 3.25) - energy),
            "gauge_field_change_max": float(np.max(abs(gauge_field - field))),
            "sign_reversal_max": abs(0.5 * dot(-source, negative_potential) - energy),
            "reciprocity_max": abs(dot(u, pv) - dot(v, pu)),
            "decomposition_max": abs(energy - self_u - self_v - cross),
            "field_energy_identity_max": abs(field_energy - energy),
            "imaginary_potential_max": float(np.max(abs(potential.imag))),
            "self_translation_max": abs(self_u - self_v),
            "continuum_convergence_max": abs(refs[1] - refs[0]),
        }
        for key, value in measured.items():
            controls[key] = max(controls[key], value)
        rows.append({"cell_shift": shift.tolist(), "displacement": displacement.tolist(),
                     "unwrapped_r": float(np.linalg.norm(displacement)),
                     "neutral_field_energy": energy, "self_u": self_u, "self_v": self_v,
                     "cross_after_same_source_self_subtraction": cross,
                     "continuum_cross_cutoff4": -refs[0], "continuum_cross_cutoff6": -refs[1],
                     "lattice_minus_continuum_cross": cross + refs[1],
                     "interpretation": "periodic finite-box; additive zero-mean convention"})
    # Same-sublattice separation differences remove a common potential offset.
    baseline = rows[0]
    for row in rows:
        row["delta_cross_vs_shift100"] = row["cross_after_same_source_self_subtraction"] - baseline["cross_after_same_source_self_subtraction"]
        row["delta_continuum_cross_vs_shift100"] = row["continuum_cross_cutoff6"] - baseline["continuum_cross_cutoff6"]
    tolerance = PARAMETERS["algebra_tolerance"]
    algebra_ok = all(value <= tolerance for key, value in controls.items()
                     if key != "continuum_convergence_max")
    return {"N": size, "vertices": nv * size ** 3, "primitive_box_rows": (size * geometry["A3"]).tolist(),
            "spectrum_min": float(ev.min()), "positive_min": float(ev[~small].min()),
            "zero_modes": int(small.sum()), "controls": controls,
            "algebra_pass": bool(algebra_ok and all(row["neutral_field_energy"] >= -tolerance for row in rows)),
            "continuum_reference_converged": controls["continuum_convergence_max"] <= PARAMETERS["reference_absolute_tolerance"],
            "coulomb_status": "UNRESOLVED: no a << r << L window asserted", "rows": rows}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--source-dir", type=Path, default=SOURCE)
    parser.add_argument("--provenance", type=Path,
                        help="Prebound JSON: git_commit, git_branch, sha256 mapping of eight input basenames")
    args = parser.parse_args()
    if platform.node().split(".")[0] != "ubuntu-auto":
        raise SystemExit("Refusing: this prepared computation is authorized only on .69 (ubuntu-auto)")
    output = args.output.resolve()
    if not output.is_relative_to(HERE) or output == HERE:
        raise SystemExit("Output must be a new subdirectory of the atom-kernel-0 task directory")
    output.mkdir(parents=False, exist_ok=False)
    started = time.monotonic()
    os.nice(max(0, 19 - os.getpriority(os.PRIO_PROCESS, 0)))
    os.sched_setaffinity(0, {min(os.sched_getaffinity(0))})
    resource.setrlimit(resource.RLIMIT_CPU, (55, 58))
    signal.signal(signal.SIGXCPU, expired)
    signal.signal(signal.SIGALRM, expired)
    signal.alarm(57)
    report = {"status": "STARTING", "parameters": PARAMETERS,
              "host": platform.node(), "execution": "CPU float64/complex128, one thread, no CUDA",
              "scope": "frozen-background fixed-V DEC subproblem; inserted external test charges",
              "coupling_caveat": "q=eQ is a normalization bridge; SRegge+SMaxwell+SSkalar alone does not establish charged scalar source coupling or a unified atomic action",
              "nice": os.getpriority(os.PRIO_PROCESS, 0),
              "cpu_affinity": sorted(os.sched_getaffinity(0)), "python": platform.python_version(),
              "utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
              "claims_excluded": ["hydrogen", "particle masses", "emergent Maxwell", "resolved 1/r"]}
    try:
        snapshot = output / "inputs"
        snapshot.mkdir()
        paths = [args.source_dir.resolve() / name for name in INPUTS] + [Path(__file__).resolve(), HERE / "PLAN.txt"]
        bound = None
        if args.provenance:
            provenance_bytes = args.provenance.read_bytes()
            bound = json.loads(provenance_bytes)
            if set(bound["sha256"]) != {path.name for path in paths}:
                raise ValueError("Prebound provenance must cover exactly all eight input files")
            report["git_commit"] = bound["git_commit"]
            report["git_branch"] = bound["git_branch"]
            (output / "provenance.json").write_bytes(provenance_bytes)
            report["provenance_sha256"] = hashlib.sha256(provenance_bytes).hexdigest()
        else:
            report["git_commit"] = git("rev-parse", "HEAD")
            report["git_branch"] = git("rev-parse", "--abbrev-ref", "HEAD")
        report["inputs"] = []
        for path in paths:
            content = path.read_bytes()
            content_sha = hashlib.sha256(content).hexdigest()
            if bound is not None and content_sha != bound["sha256"][path.name]:
                raise ValueError("Prebound input hash mismatch: " + path.name)
            saved = snapshot / path.name
            saved.write_bytes(content)
            report["inputs"].append({"path": str(path),
                                     "sha256": content_sha,
                                     "snapshot": str(saved.relative_to(output))})
        publish(output / "manifest.json", report)
        # Import only the archived, hashed sources, not mutable project originals.
        sys.path.insert(0, str(snapshot))
        global np
        np = importlib.import_module("numpy")
        scipy = importlib.import_module("scipy")
        pm = importlib.import_module("pm")
        report["numpy"] = np.__version__
        report["scipy"] = scipy.__version__
        geometry = pm.raum_V(PARAMETERS["hand_x"], PARAMETERS["hand_y"])
        if np.any(geometry["s1"] <= 0):
            raise ValueError("Nonpositive electric Hodge weight")
        report["geometry"] = {"nV": geometry["nV"], "nE": geometry["nE"],
                              "min_s1": float(np.min(geometry["s1"])), "vol3": geometry["vol3"]}
        # Independent exact scalar eigenvalue of nearest-neighbor cubic Laplacian.
        q, _, cubic = matrices(pm, pm.raum_Z3(), 4)
        reference_error = float(np.max(abs(cubic[:, 0, 0] - 4 * np.sum(np.sin(q / 2) ** 2, axis=1))))
        report["known_cubic_reference_error"] = reference_error
        report["boxes"] = []
        for size in PARAMETERS["boxes"]:
            report["boxes"].append(box_result(pm, geometry, size))
            publish(output / "partial.json", report)
        report["original_inputs_unchanged"] = all(digest(path) == item["sha256"]
            for path, item in zip(paths, report["inputs"]))
        passed = reference_error <= PARAMETERS["algebra_tolerance"] and report["original_inputs_unchanged"]
        passed = passed and all(b["algebra_pass"] and b["continuum_reference_converged"] for b in report["boxes"])
        report["status"] = "CONTROLS_PASS_FINITE_BOX_UNRESOLVED" if passed else "CONTROL_FAILURE"
    except Exception as error:
        report["status"] = "TIMEOUT" if isinstance(error, TimeoutError) else "ERROR"
        report["error"] = type(error).__name__ + ": " + str(error)
    finally:
        signal.alarm(0)
        report["wall_seconds"] = time.monotonic() - started
        report["process_cpu_seconds"] = time.process_time()
        publish(output / "result.json", report)
    return 0 if report["status"] == "CONTROLS_PASS_FINITE_BOX_UNRESOLVED" else 1


if __name__ == "__main__":
    raise SystemExit(main())
