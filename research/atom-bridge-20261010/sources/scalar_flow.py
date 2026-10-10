#!/usr/bin/env python3
"""Prepared neutral Gauss-admissible split-flow integration QA; .69 only."""
import argparse
import hashlib
import importlib
import json
import os
from pathlib import Path
import platform
import resource
import signal
import sys
import time

for key in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS",
            "NUMEXPR_NUM_THREADS", "BLIS_NUM_THREADS", "VECLIB_MAXIMUM_THREADS"):
    os.environ[key] = "1"
sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
PREVIOUS = HERE.parent/"scalar-current-0"
DEPENDENCIES = ("pm.py", "rv.py", "ew.py", "tp.py", "danzer_naeherung.py", "licht_netz.py")
PARAMETERS = {"seed": 20261011, "e": 0.3, "dt": [.001, .0005, .00025],
    "T": .2, "phi_component_sigma": .05, "momentum_over_M_sigma": .02,
    "A_sigma": .02, "chi_sigma": .7, "gauss_tolerance": 1e-9,
    "charge_tolerance": 1e-10, "gauge_tolerance": 1e-9,
    "energy_relative_tolerance": .01, "convergence_floor_relative": 1e-10,
    "finest_difference_relative_tolerance": 1e-3, "order_ratio_interval": [2.5, 5.5],
    "mutant_detection_floor": 1e-6, "cpu_soft_seconds": 55,
    "cpu_hard_seconds": 58, "wall_seconds": 57}


def publish(path, obj):
    temporary = path.with_suffix(".tmp")
    temporary.write_text(json.dumps(obj, indent=2, allow_nan=False)+"\n")
    os.replace(temporary, path)


def timeout(signum, frame):
    raise TimeoutError("Predeclared budget exhausted")


def maximum(x):
    return float(np.max(np.abs(x)))


def initial_state(model):
    rng = np.random.default_rng(PARAMETERS["seed"])
    x, y = rng.normal(0., PARAMETERS["phi_component_sigma"], (2, model.n))
    px, py = model.M*rng.normal(0., PARAMETERS["momentum_over_M_sigma"], (2, model.n))
    A = rng.normal(0., PARAMETERS["A_sigma"], model.m)
    # Euclidean minimal momentum correction along the total-charge functional.
    p = np.concatenate((px, py))
    charge_functional = model.e*np.concatenate((y, -x))
    original_total = float(charge_functional@p)
    norm2 = float(charge_functional@charge_functional)
    if norm2 <= 1e-20:
        raise ValueError("Degenerate charge projection")
    correction = charge_functional*(original_total/norm2)
    p = p-correction
    z = np.concatenate((x, y, p, A, np.zeros(model.m)))
    rho = model.rho(z)
    # No background is added: neutrality is enforced through matter momenta.
    if abs(float(rho.sum())) > PARAMETERS["charge_tolerance"]:
        raise ValueError("Neutrality projection failed")
    lap = model.D.T@(model.W[:, None]*model.D)
    values, vectors = np.linalg.eigh(lap)
    cut = 1e-12*max(1., float(values.max()))
    small = np.abs(values) <= cut
    if int(small.sum()) != 1 or np.any(values < -cut):
        raise ValueError("Expected one constant gauge zero mode")
    coefficients = vectors.T@rho
    inverse = np.zeros_like(values)
    np.divide(1., values, out=inverse, where=~small)
    a0 = vectors@(inverse*coefficients)
    Pi = model.W*(model.D@a0)
    z[4*model.n+model.m:] = Pi
    residual = maximum(model.gauss(z))
    if residual > PARAMETERS["gauss_tolerance"]:
        raise ValueError("Gauss initial solve failed")
    chi = rng.normal(0., PARAMETERS["chi_sigma"], model.n)
    return z, chi, {"original_total_charge": original_total,
        "momentum_correction_norm": float(np.linalg.norm(correction)),
        "momentum_correction_subtracted": correction.tolist(),
        "total_charge_after": float(rho.sum()), "gauss_max": residual,
        "laplacian_zero_modes": int(small.sum()), "potential_mean": float(a0.mean()),
        "rho": rho.tolist(), "a0": a0.tolist(), "background_charge": False,
        "Pi_convention": "Pi=+W D a0; canonical electric momentum",
        "state": z.tolist(), "chi": chi.tolist()}


def kick(model, z, h, broken=False):
    _, grad, current, _ = model.evaluate(z)
    hx, hy, _, _, hA, _ = model.unpack(grad)
    _, _, px, py, _, Pi = model.unpack(z)
    px -= h*hx
    py -= h*hy
    # Mutant changes only the electromagnetic matter-current kick.
    Pi -= h*(hA-2*current if broken else hA)


def drift(model, z, h):
    x, y, px, py, A, Pi = model.unpack(z)
    x += h*px/(2*model.M)
    y += h*py/(2*model.M)
    A += h*Pi/model.W


def step(model, z, dt, broken=False):
    kick(model, z, dt/2, broken)
    drift(model, z, dt)
    kick(model, z, dt/2, broken)


def trajectory(model, start, chi, dt, broken=False):
    z = start.copy()
    companion = model.gauge(start, chi)
    E0 = model.evaluate(start)[0]
    denominator = max(1., abs(E0))
    nsteps = round(PARAMETERS["T"]/dt)
    if abs(nsteps*dt-PARAMETERS["T"]) > 1e-14:
        raise ValueError("T not an integer multiple of dt")
    maxima = {"gauss": 0., "total_charge": 0., "energy_relative": 0.,
              "companion_gauss": 0., "companion_charge": 0.,
              "companion_energy_relative": 0., "gauge_state_relative": 0.}
    for index in range(nsteps+1):
        if index:
            step(model, z, dt, broken)
            step(model, companion, dt, broken)
        if not (np.all(np.isfinite(z)) and np.all(np.isfinite(companion))):
            raise ValueError("Nonfinite trajectory")
        expected = model.gauge(z, chi)
        measures = {
            "gauss": maximum(model.gauss(z)), "total_charge": abs(float(model.rho(z).sum())),
            "energy_relative": abs(model.evaluate(z)[0]-E0)/denominator,
            "companion_gauss": maximum(model.gauss(companion)),
            "companion_charge": abs(float(model.rho(companion).sum())),
            "companion_energy_relative": abs(model.evaluate(companion)[0]-E0)/denominator,
            "gauge_state_relative": maximum(companion-expected)/max(1., maximum(expected))}
        for key, value in measures.items():
            maxima[key] = max(maxima[key], value)
    passed = (max(maxima["gauss"], maxima["companion_gauss"]) <= PARAMETERS["gauss_tolerance"] and
        max(maxima["total_charge"], maxima["companion_charge"]) <= PARAMETERS["charge_tolerance"] and
        max(maxima["energy_relative"], maxima["companion_energy_relative"]) <= PARAMETERS["energy_relative_tolerance"] and
        maxima["gauge_state_relative"] <= PARAMETERS["gauge_tolerance"])
    return {"dt": dt, "steps": nsteps, "T": nsteps*dt, "broken_current_kick": broken,
        "initial_energy": E0, "final_energy": model.evaluate(z)[0], "maxima_all_steps": maxima,
        "trajectory_checks_passed": bool(passed), "final_state": z.tolist()}


def convergence(rows):
    finals = [np.array(row["final_state"]) for row in rows]
    scale = max(1., float(np.linalg.norm(finals[-1])))
    coarse = float(np.linalg.norm(finals[0]-finals[1]))/scale
    fine = float(np.linalg.norm(finals[1]-finals[2]))/scale
    floor = PARAMETERS["convergence_floor_relative"]
    ratio = coarse/fine if coarse > floor and fine > floor else None
    if coarse <= floor or fine <= floor:
        status = "ROUNDING_FLOOR_UNRESOLVED"
    elif PARAMETERS["order_ratio_interval"][0] <= ratio <= PARAMETERS["order_ratio_interval"][1]:
        status = "SECOND_ORDER_COMPATIBLE_ON_THIS_INTERVAL"
    else:
        status = "ORDER_UNRESOLVED"
    return {"coarse_difference_relative_l2": coarse, "fine_difference_relative_l2": fine,
        "coarse_over_fine": ratio, "status": status,
        "refinement_gate_passed": bool(fine <= coarse+floor and fine <= PARAMETERS["finest_difference_relative_tolerance"]),
        "meaning": "same gauge and canonical coordinates; self-convergence, not exact-solution error"}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--source-dir", type=Path, default=PREVIOUS/"inputs-source")
    parser.add_argument("--model-source", type=Path, default=PREVIOUS/"run-a/inputs/scalar_current.py")
    parser.add_argument("--provenance", type=Path, required=True)
    args = parser.parse_args()
    if platform.node().split(".")[0] != "ubuntu-auto":
        raise SystemExit("Only .69 / ubuntu-auto may execute this QA")
    output = args.output.resolve()
    if output == HERE or not output.is_relative_to(HERE):
        raise SystemExit("Output must be a new task subdirectory")
    output.mkdir(exist_ok=False)
    started = time.monotonic()
    os.nice(max(0, 19-os.getpriority(os.PRIO_PROCESS, 0)))
    os.sched_setaffinity(0, {min(os.sched_getaffinity(0))})
    resource.setrlimit(resource.RLIMIT_CPU, (55, 58))
    signal.signal(signal.SIGXCPU, timeout)
    signal.signal(signal.SIGALRM, timeout)
    signal.alarm(57)
    report = {"status": "STARTING", "parameters": PARAMETERS, "host": platform.node(),
        "utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "python": platform.python_version(), "nice": os.getpriority(os.PRIO_PROCESS, 0),
        "cpu_affinity": sorted(os.sched_getaffinity(0)), "execution": "CPU float64/complex128 one thread; no CUDA",
        "scope": "short integration QA of new minimally gauged scalar on frozen fixed-V",
        "claims_excluded": ["binding", "long-time stability", "fermions", "atoms", "full core with flips"]}
    try:
        paths = [args.source_dir.resolve()/name for name in DEPENDENCIES]
        paths += [args.model_source.resolve(), HERE/"scalar_flow.py", HERE/"PLAN.txt", HERE/"DERIVATION.txt"]
        bound_bytes = args.provenance.read_bytes()
        bound = json.loads(bound_bytes)
        if set(bound["sha256"]) != {path.name for path in paths} or len(paths) != 10:
            raise ValueError("Provenance must bind exactly all ten inputs")
        report["git_commit"], report["git_branch"] = bound["git_commit"], bound["git_branch"]
        (output/"provenance.json").write_bytes(bound_bytes)
        report["provenance_sha256"] = hashlib.sha256(bound_bytes).hexdigest()
        snapshot = output/"inputs"
        snapshot.mkdir()
        report["inputs"] = []
        for path in paths:
            content = path.read_bytes()
            sha = hashlib.sha256(content).hexdigest()
            if sha != bound["sha256"][path.name]:
                raise ValueError("Hash mismatch: "+path.name)
            (snapshot/path.name).write_bytes(content)
            report["inputs"].append({"path": str(path), "sha256": sha, "snapshot": "inputs/"+path.name})
        publish(output/"manifest.json", report)
        sys.path.insert(0, str(snapshot))
        global np
        np = importlib.import_module("numpy")
        scipy = importlib.import_module("scipy")
        pm = importlib.import_module("pm")
        scalar = importlib.import_module("scalar_current")
        scalar.np = np  # Frozen module binds np only in its own CLI; do not run that CLI.
        model = scalar.Hamiltonian(pm.raum_V())
        if model.e != PARAMETERS["e"] or model.variant != "original":
            raise ValueError("Frozen model convention differs from predeclared plan")
        report["numpy"], report["scipy"] = np.__version__, scipy.__version__
        z0, chi, report["initialization"] = initial_state(model)
        report["trajectories"] = []
        for dt in PARAMETERS["dt"]:
            report["trajectories"].append(trajectory(model, z0, chi, dt))
            publish(output/"partial.json", report)
        report["convergence"] = convergence(report["trajectories"])
        report["mutant"] = trajectory(model, z0, chi, PARAMETERS["dt"][0], broken=True)
        report["mutant_detected"] = (not report["mutant"]["trajectory_checks_passed"] and
            report["mutant"]["maxima_all_steps"]["gauss"] > PARAMETERS["mutant_detection_floor"])
        report["original_inputs_unchanged"] = all(hashlib.sha256(path.read_bytes()).hexdigest() == item["sha256"] for path, item in zip(paths, report["inputs"]))
        passed = all(row["trajectory_checks_passed"] for row in report["trajectories"])
        passed = passed and report["convergence"]["refinement_gate_passed"] and report["mutant_detected"] and report["original_inputs_unchanged"]
        report["status"] = "SHORT_INTEGRATION_QA_PASS" if passed else "CONTROL_FAILURE"
    except Exception as error:
        report["status"] = "TIMEOUT" if isinstance(error, TimeoutError) else "ERROR"
        report["error"] = type(error).__name__+": "+str(error)
    finally:
        signal.alarm(0)
        report["wall_seconds"] = time.monotonic()-started
        report["process_cpu_seconds"] = time.process_time()
        publish(output/"result.json", report)
    return 0 if report["status"] == "SHORT_INTEGRATION_QA_PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
