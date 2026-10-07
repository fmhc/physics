"""Small CPU-only linear model; run on ubuntu-auto (.69), never locally."""
import os
for key in ('OMP_NUM_THREADS', 'OPENBLAS_NUM_THREADS', 'MKL_NUM_THREADS',
            'NUMEXPR_NUM_THREADS', 'VECLIB_MAXIMUM_THREADS'):
    os.environ[key] = '1'
import csv
import hashlib
import json
from itertools import combinations
from pathlib import Path
import resource
import socket
import time

if socket.gethostname().split('.')[0] != 'ubuntu-auto':
    raise SystemExit('Execution permitted only on ubuntu-auto (.69).')
resource.setrlimit(resource.RLIMIT_CPU, (60, 60))
START = time.process_time()
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

HERE = Path(__file__).resolve().parent
SOURCE = HERE.parent / 'RESULT.json'
NORMAL = np.array([1., .37, .23])
NORMAL /= np.linalg.norm(NORMAL)
AXIS_U = np.cross(NORMAL, [0., 0., 1.])
AXIS_U /= np.linalg.norm(AXIS_U)
AXIS_V = np.cross(NORMAL, AXIS_U)
AMPLITUDE = .001


def csv_out(name, header, rows):
    with (HERE / name).open('w', newline='') as handle:
        writer = csv.writer(handle)
        writer.writerow(header)
        writer.writerows(rows)


def rigidity(vertices, edges):
    r = np.zeros((len(edges), vertices.size))
    for row, (i, j) in enumerate(edges):
        direction = vertices[i] - vertices[j]
        length = np.linalg.norm(direction)
        assert length > 1e-12
        direction /= length
        r[row, 3*i:3*i+3] = direction
        r[row, 3*j:3*j+3] = -direction
    return r


def section(vertices, edges, cells):
    """Transverse crossings only; abort if a vertex lies on the plane."""
    signed = vertices @ NORMAL
    assert np.min(np.abs(signed)) > 1e-10, 'Nontransverse vertex-plane event'
    p = sum(signed[i] * signed[j] < 0 for i, j in edges)
    area = 0.
    for cell in cells:
        points = []
        for i, j in combinations(cell, 2):
            if signed[i] * signed[j] < 0:
                fraction = signed[i] / (signed[i] - signed[j])
                points.append(vertices[i] + fraction * (vertices[j] - vertices[i]))
        if len(points) < 3:
            continue
        points = np.array(points)
        xy = np.column_stack((points @ AXIS_U, points @ AXIS_V))
        centered = xy - xy.mean(axis=0)
        xy = xy[np.argsort(np.arctan2(centered[:, 1], centered[:, 0]))]
        area += .5 * abs(np.dot(xy[:, 0], np.roll(xy[:, 1], -1))
                        - np.dot(xy[:, 1], np.roll(xy[:, 0], -1)))
    return int(p), float(area)


def spectral_groups(eigenvalues, eigenvectors, vector, tolerance):
    groups = []
    begin = 0
    while begin < len(eigenvalues):
        end = begin + 1
        while end < len(eigenvalues) and abs(eigenvalues[end] - eigenvalues[begin]) <= tolerance:
            end += 1
        weight = np.linalg.norm(eigenvectors[:, begin:end].T @ vector)**2
        groups.append({'first_mode_0based': begin, 'multiplicity': end-begin,
                       'omega_squared': float(eigenvalues[begin:end].mean()),
                       'weight': float(weight)})
        begin = end
    return groups


def main():
    source_bytes = SOURCE.read_bytes()
    data = json.loads(source_bytes)
    control_v = np.array([[1., 1., 1.], [1., -1., -1.],
                          [-1., 1., -1.], [-1., -1., 1.]]) / np.sqrt(8.)
    control_r = rigidity(control_v, list(combinations(range(4), 2)))
    control_values = np.linalg.eigvalsh(control_r.T @ control_r)
    expected = np.array([0.] * 6 + [1., 1., 2., 2., 2., 4.])
    assert np.allclose(control_values, expected, atol=1e-12, rtol=0)
    output = {'status': 'linear_central_spring_followup', 'host': socket.gethostname(),
              'compute': 'CPU, single thread; no CUDA', 'cpu_budget_seconds': 60,
              'source_sha256': hashlib.sha256(source_bytes).hexdigest(),
              'script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              'k': 1, 'mass_per_vertex': 1, 'prestress': False,
              'plane_normal': NORMAL.tolist(), 'plane_offset': 0,
              'area_definition': 'sum of tetrahedron section polygon areas, with multiplicity; not union',
              'single_tetra_control_eigenvalues': control_values.tolist(), 'models': {}}
    spectrum_fig, spectrum_axes = plt.subplots(2, 2, figsize=(11, 7))
    trace_fig, trace_axes = plt.subplots(2, 2, figsize=(11, 7))
    geometry_fig = plt.figure(figsize=(12, 5))
    assert len(data['models']) == 2
    for col, (label, model) in enumerate(data['models'].items()):
        vertices = np.array(model['vertices'], dtype=float)
        edges = sorted({tuple(sorted(e)) for e in model['edges']})
        assert len(edges) == len(model['edges']), 'Input has duplicate edges'
        cells = [list(range(i, i+4)) for i in range(len(vertices)-3)]
        assert set(edges) == {e for cell in cells for e in combinations(cell, 2)}
        r = rigidity(vertices, edges)
        h = r.T @ r
        values, vectors = np.linalg.eigh(h)
        tolerance = 1e-10 * max(1., float(values[-1]))
        assert np.min(values) > -tolerance
        assert np.count_nonzero(np.abs(values) <= tolerance) == 6
        assert np.max(np.abs(h @ vectors - vectors * values)) < 1e-11
        centered = vertices - vertices.mean(axis=0)
        rigid = np.column_stack([np.tile(axis, len(vertices)) for axis in np.eye(3)] +
                                [np.cross(axis, centered).ravel() for axis in np.eye(3)])
        rigid /= np.linalg.norm(rigid, axis=0)
        rigid_residuals = np.linalg.norm(h @ rigid, axis=0)
        assert np.max(rigid_residuals) < 1e-11
        rigid_q, _ = np.linalg.qr(rigid)
        null_projector_error = np.linalg.norm(vectors[:, :6] @ vectors[:, :6].T - rigid_q @ rigid_q.T)
        assert null_projector_error < 1e-8
        k4 = np.linalg.eigvalsh(4*h)
        assert np.allclose(k4, 4*values, atol=1e-11, rtol=1e-10)
        scale = centered.ravel()
        scale /= np.linalg.norm(scale)
        hs = h @ scale
        rayleigh = float(scale @ hs)
        groups = spectral_groups(values, vectors, scale, tolerance)
        assert abs(sum(g['weight'] for g in groups)-1.) < 1e-12
        mode_index = int(np.flatnonzero(values > tolerance)[0])
        mode = vectors[:, mode_index].reshape((-1, 3)).copy()
        mode *= np.sign(mode.ravel()[np.argmax(np.abs(mode))])
        mode /= np.max(np.linalg.norm(mode, axis=1))
        omega = float(np.sqrt(values[mode_index]))
        period = 2*np.pi/omega
        times = np.linspace(0., 2*period, 201)
        # Bound for the whole continuous path, not just sampled times.
        plane_margin = float(np.min(np.abs(vertices @ NORMAL) - AMPLITUDE * np.abs(mode @ NORMAL)))
        assert plane_margin > 1e-10
        trace = []
        for t in times:
            u = AMPLITUDE * np.cos(omega*t) * mode
            velocity = -AMPLITUDE * omega * np.sin(omega*t) * mode
            p, area = section(vertices + u, edges, cells)
            energy = .5 * (velocity.ravel() @ velocity.ravel() + u.ravel() @ h @ u.ravel())
            trace.append([float(t), float(t/period), float(np.cos(omega*t)), p, area, float(energy)])
        trace = np.array(trace)
        assert np.ptp(trace[:, 5]) < 1e-12
        homo = []
        for t in np.linspace(0., 4*np.pi, 201):
            a = 1 + .1*np.cos(t)
            p, area = section(a*vertices, edges, cells)
            homo.append([float(t), float(a), p, area, float(area/a**2)])
        homo = np.array(homo)
        assert np.ptp(homo[:, 2]) == 0
        assert np.ptp(homo[:, 4]) < 1e-11
        result = {'vertex_count': len(vertices), 'edge_count': len(edges),
                  'tetrahedra': cells, 'eigenvalues_omega_squared': values.tolist(),
                  'eigenvectors_columns_xyz_vertex_order': vectors.tolist(),
                  'zero_tolerance': tolerance, 'nullity': 6,
                  'rigid_residuals_Tx_Ty_Tz_Rx_Ry_Rz': rigid_residuals.tolist(),
                  'null_projector_error': float(null_projector_error),
                  'k4_eigenvalue_max_abs_error': float(np.max(np.abs(k4-4*values))),
                  'k4_positive_frequency_max_abs_error': float(np.max(np.abs(np.sqrt(k4[6:])-2*np.sqrt(values[6:])))),
                  'scale_rayleigh': rayleigh, 'scale_relative_eigen_residual_normHs': float(np.linalg.norm(hs-rayleigh*scale)/np.linalg.norm(hs)),
                  'scale_modal_groups': groups, 'first_positive_mode_0based': mode_index,
                  'mode_shape_max_vertex_norm_1': mode.tolist(), 'omega': omega, 'period': period,
                  'max_vertex_displacement': AMPLITUDE, 'continuous_plane_margin': plane_margin,
                  'linear_trace_P_range': [int(trace[:, 3].min()), int(trace[:, 3].max())],
                  'linear_trace_area_range': [float(trace[:, 4].min()), float(trace[:, 4].max())],
                  'linear_energy_peak_to_peak': float(np.ptp(trace[:, 5])),
                  'homothety_P_peak_to_peak': float(np.ptp(homo[:, 2])),
                  'homothety_A_over_a2_peak_to_peak': float(np.ptp(homo[:, 4]))}
        output['models'][label] = result
        csv_out(f'{label}-spectrum.csv', ['mode_0based', 'omega_squared', 'omega'],
                [[i, val, np.sqrt(max(0., val))] for i, val in enumerate(values)])
        csv_out(f'{label}-scale-groups.csv', list(groups[0]), [list(g.values()) for g in groups])
        csv_out(f'{label}-linear.csv', ['time', 'time_over_period', 'cos_phase', 'P', 'A_cell_sum', 'linear_energy'], trace)
        csv_out(f'{label}-homothety.csv', ['prescribed_phase', 'a', 'P', 'A_cell_sum', 'A_over_a_squared'], homo)
        spectrum_axes[0, col].plot(range(len(values)), values, '.-')
        spectrum_axes[0, col].set(title=f'{label}: spectrum, six rigid zeros', xlabel='mode (0-based)', ylabel='omega squared')
        spectrum_axes[1, col].stem([g['omega_squared'] for g in groups], [g['weight'] for g in groups])
        spectrum_axes[1, col].set(xlabel='omega squared (grouped)', ylabel='scaling-vector modal weight', title=f'Rayleigh={rayleigh:.4g}; relative residual={result["scale_relative_eigen_residual_normHs"]:.3g}')
        trace_axes[0, col].plot(trace[:, 1], trace[:, 4], color='tab:blue', label='cell-sum area A')
        twin = trace_axes[0, col].twinx()
        twin.plot(trace[:, 1], trace[:, 3], color='tab:orange', linestyle='--')
        twin.set_ylabel('P: crossed unique edges', color='tab:orange')
        trace_axes[0, col].set(title=f'{label}: linear mode; max displacement 0.001', xlabel='time / period', ylabel='section area A')
        trace_axes[1, col].plot(homo[:, 0], homo[:, 3]/homo[0, 4], label='A / A(reference)')
        trace_axes[1, col].plot(homo[:, 0], homo[:, 4]/homo[0, 4], '--', label='(A/a²) / A(reference)')
        trace_axes[1, col].set(title='Prescribed homothety: measurement control only', xlabel='prescribed phase', ylabel='relative area')
        trace_axes[1, col].legend(fontsize=8)
        ax = geometry_fig.add_subplot(1, 2, col+1, projection='3d')
        for edge_number, (i, j) in enumerate(edges):
            for sign, color, name in [(0, '0.55', 'equilibrium'), (1, 'tab:red', '+phase: display 100x'), (-1, 'tab:blue', '-phase: display 100x')]:
                points = vertices[[i, j]] + sign * 100 * AMPLITUDE * mode[[i, j]]
                ax.plot(*points.T, color=color, alpha=.7, linewidth=1,
                        label=name if edge_number == 0 else None)
        ax.set(title=f'{label}: first positive mode', xlabel='x', ylabel='y', zlabel='z')
        extent = np.ptp(vertices, axis=0) + .2
        ax.set_box_aspect(extent)
        ax.legend(fontsize=7)
    geometry_fig.suptitle('Geometry: max shown displacement 0.1; actual linear trace amplitude 0.001')
    for fig, filename in [(spectrum_fig, 'spectrum-scaling.png'), (trace_fig, 'section-traces.png'), (geometry_fig, 'mode-geometry.png')]:
        fig.tight_layout()
        fig.savefig(HERE / filename, dpi=150)
        plt.close(fig)
    output['cpu_seconds'] = time.process_time() - START
    output['limitations'] = ['Linearized mechanics only, no nonlinear dynamics validation.',
                             'Prescribed homothety is not a demonstrated breathing eigenmode.',
                             'Area is cell-additive; polygon union is not evaluated.']
    temporary = HERE / 'RESULT.json.tmp'
    temporary.write_text(json.dumps(output, indent=2) + '\n')
    temporary.replace(HERE / 'RESULT.json')
    print(json.dumps({key: {k: v for k, v in model.items() if k in ('nullity', 'omega', 'scale_rayleigh', 'scale_relative_eigen_residual_normHs', 'linear_trace_P_range', 'linear_trace_area_range')} for key, model in output['models'].items()}, indent=2))
    print(f'CPU seconds: {output["cpu_seconds"]:.3f}')


if __name__ == '__main__':
    main()
