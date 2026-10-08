# Reproduce a result

Start with [V Maxwell weights](reproducibility/maxwell-v/README.md). This compact package tests the negative-weight
limitation of [RESULTS, finding 3](RESULTS.md#3-compact-u1-on-the-tent-network-massless-isotropic-photon-and-a-phase-transition).
It contains fixed parameters, a standalone implementation, pinned dependencies, expected values, a pre-run plan and
recorded output. Follow its README for the exact installation and single rerun command. CUDA is required for this
implementation; there is no silent CPU fallback. It does not require access to the original project hosts or missing
historical binary files.

This is a focused numerical reproduction using source-derived geometry and a rewritten implementation. It is not an
independent human reproduction and does not reproduce the Monte Carlo photon or transition measurements. Agreement
with historical values can reveal implementation mistakes but cannot validate the physical assumptions shared by both
implementations. Sampled positivity is not a proof for all momenta or for the interacting measure.

## Coverage and error meanings

[CLAIMS.md](CLAIMS.md) lists all eight findings and their present evidence. The other seven findings do not yet have
complete compact packages here. Historical code and reports remain available through that register; some original
binary data are excluded as documented in [AUSSCHLUESSE.md](AUSSCHLUESSE.md).

Keep these errors separate:

- **Solver/roundoff error:** residuals and precision sensitivity in the implemented equations.
- **Model-reduction error:** a reduced model versus the full model at the same discretization, as in the Higgs tests.
- **Discretization error:** change with lattice spacing at fixed physical volume and matched model parameters.
- **Finite-volume error:** change with physical box size at fixed spacing.
- **Statistical error:** sampling/autocorrelation uncertainty, with systematic fit choices reported separately.
- **Experimental error:** uncertainty of actual measured data; none of the eight findings is an experimental validation.

## Acceptance and independence

A passing run must satisfy the package's frozen numerical checks and preserve the actual environment and output.
File hashes establish artifact identity, not physical correctness. If a run fails, retain its output and investigate
before changing code or criteria; publish changes as a new version. New parameter or momentum scans need separate
predeclared tests, rather than reusing evaluation points to tune the model.

No repository-wide continuous numerical integration or independent external reproduction is claimed. The recorded
checks were run on the project's compute host. The next packaging targets should follow the foundational priority
order in [the review response](coordination/review-response-20261008/RESPONSE.md), not the ease of obtaining more digits.
