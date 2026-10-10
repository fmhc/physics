#!/usr/bin/env python3
"""Prepared fixed-V gauged scalar Hamiltonian checks. No trajectory or atom.

Run only after root review/coordination, on .69 with prebound provenance.
"""
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
SOURCES = HERE.parent / "atom-kernel-0/inputs-source"
DEPENDENCIES = ("pm.py", "rv.py", "ew.py", "tp.py", "danzer_naeherung.py", "licht_netz.py")
PARAMETERS = {"e": 0.3, "seed": 20261010, "fd_steps": [1e-5, 5e-6],
              "fd_tolerance": 2e-7, "algebra_tolerance": 1e-10,
              "spatial_dimension": 3, "primitive_periodic_cells": 1,
              "state_count": 3, "gauss_projection": False,
              "mutant_detection_floor": 1e-6,
              "cpu_soft_seconds": 55, "cpu_hard_seconds": 58, "wall_seconds": 57}


def publish(path, value):
    temporary = path.with_suffix(".tmp")
    temporary.write_text(json.dumps(value, indent=2, allow_nan=False) + "\n")
    os.replace(temporary, path)


def timeout(signum, frame):
    raise TimeoutError("Predeclared budget exhausted")


class Hamiltonian:
    def __init__(self, geometry):
        self.n, self.m = geometry["nV"], geometry["nE"]
        self.M = np.asarray(geometry["s0"])
        self.W = np.asarray(geometry["s1"])
        self.S2 = np.asarray(geometry["s2"])
        if min(self.M.min(), self.W.min(), self.S2.min()) <= 0:
            raise ValueError("Positive star0/star1/star2 required for this completion")
        self.D = np.zeros((self.m, self.n))
        self.C = np.zeros((geometry["nF"], self.m))
        self.tail = np.full(self.m, -1, int)
        self.head = np.full(self.m, -1, int)
        # N=1 torus: every integer cell translation is periodic identity.
        for edge, vertex, coefficient, shift in geometry["d0"]:
            self.D[edge, vertex] += coefficient
            if coefficient == -1:
                if self.tail[edge] != -1:
                    raise ValueError("Unexpected multiple edge tails")
                self.tail[edge] = vertex
            elif coefficient == 1:
                if self.head[edge] != -1:
                    raise ValueError("Unexpected multiple edge heads")
                self.head[edge] = vertex
            else:
                raise ValueError("Expected oriented incidence coefficients +/-1")
        if np.any(self.tail < 0) or np.any(self.head < 0):
            raise ValueError("Missing edge endpoint")
        for face, edge, coefficient, shift in geometry["d1"]:
            self.C[face, edge] += coefficient
        self.e = PARAMETERS["e"]
        self.variant = "original"

    def unpack(self, z):
        n, m = self.n, self.m
        return z[:n], z[n:2*n], z[2*n:3*n], z[3*n:4*n], z[4*n:4*n+m], z[4*n+m:]

    def evaluate(self, z):
        x, y, px, py, A, Pi = self.unpack(z)
        phi = x + 1j*y
        S = x*x + y*y
        phase = np.exp(-1j*self.e*A)
        if self.variant == "ungauged_gradient":
            phase = np.ones_like(phase)
        b = phase*phi[self.head] - phi[self.tail]
        curl = self.C @ A
        parts = {
            "kinetic": float(np.sum((px*px + py*py)/(4*self.M))),
            "gradient": float(np.sum(self.W*abs(b)**2)),
            "potential": float(np.sum(self.M*(S-S*S+S*S*S/2))),
            "electric": float(np.sum(Pi*Pi/(2*self.W))),
            "magnetic": float(np.sum(self.S2*curl*curl/2)),
        }
        grad_phi = 2*self.M*(1-2*S+1.5*S*S)*phi
        np.add.at(grad_phi, self.tail, -2*self.W*b)
        np.add.at(grad_phi, self.head, 2*self.W*phase.conj()*b)
        current = -2*self.e*self.W*np.imag(phi[self.tail].conj()*phase*phi[self.head])
        if self.variant == "reversed_current":
            current = -current
        elif self.variant == "ungauged_gradient":
            current = np.zeros_like(current)
        gradient = np.concatenate((grad_phi.real, grad_phi.imag, px/(2*self.M), py/(2*self.M),
                                   current + self.C.T @ (self.S2*curl), Pi/self.W))
        return sum(parts.values()), gradient, current, parts

    def rho(self, z):
        x, y, px, py, _, _ = self.unpack(z)
        return self.e*(y*px-x*py)

    def gauss(self, z):
        return self.D.T @ self.unpack(z)[5] - self.rho(z)

    def flow(self, gradient):
        hx, hy, hpx, hpy, hA, hPi = self.unpack(gradient)
        return np.concatenate((hpx, hpy, -hx, -hy, hPi, -hA))

    def rho_dot(self, z, gradient):
        x, y, px, py, _, _ = self.unpack(z)
        dx, dy, dpx, dpy, _, _ = self.unpack(self.flow(gradient))
        return self.e*(dy*px+y*dpx-dx*py-x*dpy)

    def gauge(self, z, chi):
        x, y, px, py, A, Pi = self.unpack(z)
        phase = np.exp(1j*self.e*chi)
        phi, p = phase*(x+1j*y), phase*(px+1j*py)
        return np.concatenate((phi.real, phi.imag, p.real, p.imag, A+self.D@chi, Pi))


def finite_gradient(function, z, h):
    result = np.empty_like(z)
    for index in range(len(z)):
        left, right = z.copy(), z.copy()
        left[index] -= h
        right[index] += h
        result[index] = (function(right)-function(left))/(2*h)
    return result


def maximum(values):
    return float(np.max(np.abs(values)))


def check_state(model, z, chi, include_mutants=True):
    H, gradient, current, parts = model.evaluate(z)
    x, y, px, py, A, Pi = model.unpack(z)
    gauged = model.gauge(z, chi)
    H_g, gradient_g, current_g, parts_g = model.evaluate(gauged)
    # Tangent canonical gauge transformation, not the affine A-shift.
    flow = model.flow(gradient)
    dx, dy, dpx, dpy, dA, dPi = model.unpack(flow)
    phase = np.exp(1j*model.e*chi)
    dphi, dp = phase*(dx+1j*dy), phase*(dpx+1j*dpy)
    transformed_flow = np.concatenate((dphi.real, dphi.imag, dp.real, dp.imag, dA, dPi))
    drho = model.rho_dot(z, gradient)
    algebra = {
        "gauge_energy_relative": abs(H_g-H)/max(1., abs(H)),
        "gauge_current_absolute": maximum(current_g-current),
        "gauge_rho_absolute": maximum(model.rho(gauged)-model.rho(z)),
        "gauge_gauss_absolute": maximum(model.gauss(gauged)-model.gauss(z)),
        "gauge_flow_absolute": maximum(model.flow(gradient_g)-transformed_flow),
        "continuity_absolute": maximum(drho+model.D.T@current),
        "total_charge_derivative_absolute": abs(float(drho.sum())),
        "gauss_derivative_absolute": maximum(model.D.T@model.unpack(flow)[5]-drho),
    }
    finite = []
    for step in PARAMETERS["fd_steps"]:
        fd = finite_gradient(lambda state: model.evaluate(state)[0], z, step)
        fd_drho = model.rho_dot(z, fd)
        # Independent numerical H derivatives, subtract analytic pure magnetic term.
        fd_current = model.unpack(fd)[4] - model.C.T@(model.S2*(model.C@A))
        gen_fd = finite_gradient(lambda state: float(chi@model.gauss(state)), z, step)
        gen_flow = model.flow(gen_fd)
        expected_generator = np.concatenate((-model.e*chi*y, model.e*chi*x,
                    -model.e*chi*py, model.e*chi*px, model.D@chi, np.zeros(model.m)))
        directional_rho = (model.rho(z+step*flow)-model.rho(z-step*flow))/(2*step)
        finite.append({"step": step,
            "hamiltonian_gradient_relative": maximum(fd-gradient)/max(1., maximum(gradient)),
            "current_absolute": maximum(fd_current-current),
            "continuity_absolute": maximum(fd_drho+model.D.T@fd_current),
            "gauss_derivative_absolute": maximum(model.D.T@model.unpack(model.flow(fd))[5]-fd_drho),
            "generator_absolute": maximum(gen_flow-expected_generator),
            "directional_rho_absolute": maximum(directional_rho-drho)})
    mutants = {}
    if include_mutants:
        for variant in ("reversed_current", "ungauged_gradient"):
            model.variant = variant
            try:
                mutant = check_state(model, z, chi, include_mutants=False)
            finally:
                model.variant = "original"
            mutants[variant] = {"algebra": mutant["algebra"],
                "finite_difference": mutant["finite_difference"],
                "same_checks_passed": mutant["passed"]}
    passed = max(algebra.values()) <= PARAMETERS["algebra_tolerance"]
    passed = passed and all(max(v for k, v in row.items() if k != "step") <= PARAMETERS["fd_tolerance"] for row in finite)
    return {"H": H, "parts": parts, "total_charge": float(model.rho(z).sum()),
            "gauss_norm": float(np.linalg.norm(model.gauss(z))),
            "off_constraint_state": True, "algebra": algebra, "finite_difference": finite,
            "mutants": mutants, "passed": bool(passed)}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--source-dir", type=Path, default=SOURCES)
    parser.add_argument("--provenance", type=Path, required=True)
    args = parser.parse_args()
    if platform.node().split(".")[0] != "ubuntu-auto":
        raise SystemExit("Computation is restricted to .69 / ubuntu-auto")
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
        "scope": "NEW explicit minimal-coupling completion; frozen fixed-V scalar Hamiltonian",
        "not_established": ["already accepted unified core coupling", "fermions", "electron", "proton", "atom", "trajectory", "physical Gauss initial state"]}
    try:
        paths = [args.source_dir.resolve()/name for name in DEPENDENCIES]
        paths += [HERE/"scalar_current.py", HERE/"PLAN.txt", HERE/"DERIVATION.txt"]
        bound_bytes = args.provenance.read_bytes()
        bound = json.loads(bound_bytes)
        if set(bound["sha256"]) != {path.name for path in paths}:
            raise ValueError("Provenance must bind exactly all nine input files")
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
                raise ValueError("Input hash mismatch: "+path.name)
            (snapshot/path.name).write_bytes(content)
            report["inputs"].append({"path": str(path), "sha256": sha, "snapshot": "inputs/"+path.name})
        publish(output/"manifest.json", report)
        sys.path.insert(0, str(snapshot))
        global np
        np = importlib.import_module("numpy")
        scipy = importlib.import_module("scipy")
        pm = importlib.import_module("pm")
        report["numpy"], report["scipy"] = np.__version__, scipy.__version__
        model = Hamiltonian(pm.raum_V())
        report["geometry"] = {"nV": model.n, "nE": model.m, "nF": len(model.S2),
            "min_star0": float(model.M.min()), "min_star1": float(model.W.min()),
            "min_star2": float(model.S2.min()), "chain_complex_error": maximum(model.C@model.D),
            "constant_incidence_error": maximum(model.D@np.ones(model.n))}
        # Known convention control: phi=exp(-i omega t)f => rho=2e M omega f².
        f, omega = .4, .7
        rotating = np.concatenate((np.full(model.n, f), np.zeros(model.n),
            np.zeros(model.n), -2*model.M*omega*f, np.zeros(2*model.m)))
        report["qball_charge_sign_error"] = maximum(model.rho(rotating)-2*model.e*model.M*omega*f*f)
        rng = np.random.default_rng(PARAMETERS["seed"])
        report["states"] = []
        for index in range(PARAMETERS["state_count"]):
            z = rng.normal(0., .2, 4*model.n+2*model.m)
            chi = rng.normal(0., .7, model.n)
            report["states"].append(check_state(model, z, chi))
            publish(output/"partial.json", report)
        report["original_inputs_unchanged"] = all(hashlib.sha256(path.read_bytes()).hexdigest() == item["sha256"] for path, item in zip(paths, report["inputs"]))
        passed = all(row["passed"] for row in report["states"]) and report["original_inputs_unchanged"]
        report["mutants_detected"] = {
            "reversed_current": any(not row["mutants"]["reversed_current"]["same_checks_passed"] and
                max(fd["current_absolute"] for fd in row["mutants"]["reversed_current"]["finite_difference"]) > PARAMETERS["mutant_detection_floor"] for row in report["states"]),
            "ungauged_gradient": any(not row["mutants"]["ungauged_gradient"]["same_checks_passed"] and
                row["mutants"]["ungauged_gradient"]["algebra"]["gauge_energy_relative"] > PARAMETERS["mutant_detection_floor"] for row in report["states"])}
        passed = passed and all(report["mutants_detected"].values())
        passed = passed and max(report["qball_charge_sign_error"], report["geometry"]["chain_complex_error"], report["geometry"]["constant_incidence_error"]) <= PARAMETERS["algebra_tolerance"]
        report["status"] = "STATIC_HAMILTONIAN_CHECKS_PASS" if passed else "CONTROL_FAILURE"
    except Exception as error:
        report["status"] = "TIMEOUT" if isinstance(error, TimeoutError) else "ERROR"
        report["error"] = type(error).__name__+": "+str(error)
    finally:
        signal.alarm(0)
        report["wall_seconds"] = time.monotonic()-started
        report["process_cpu_seconds"] = time.process_time()
        publish(output/"result.json", report)
    return 0 if report["status"] == "STATIC_HAMILTONIAN_CHECKS_PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
