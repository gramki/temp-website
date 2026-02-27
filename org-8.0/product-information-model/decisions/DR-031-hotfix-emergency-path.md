# DR-031: Hotfix / Emergency Fix Path — P0 Sprint Bypass and Emergency Gate Profile

**Status:** Accepted
**Date:** 2026-02-25

## Context

DR-029 established the Emergency-Technical Change Request type for incident-driven deployments with abbreviated soak and documented waivers. DR-030 established the Incident Response Task that produces Bugs (provenance: Run) and triggers Emergency-Technical Change Requests. The missing piece was the **Build Track's fast-path**: how a P0 Bug bypasses sprint boundaries, how the resulting System Version uses a reduced quality gate profile, and how deferred gates are tracked to prevent permanent quality erosion.

The alternative considered was adding a separate `Urgency` field (Normal/Expedited) on Bug. This was rejected because P0 already carries "drop everything" semantics in standard engineering practice. Adding Urgency would create a redundant dimension alongside Severity and Priority without meaningful additional signal.

## Decisions

### D1: P0 Bug implies sprint bypass

**Decision:** Run-provenance Bugs from SEV-0/SEV-1 Incidents default to P0 at triage. P0 signals sprint-boundary bypass and eligibility for Emergency quality gate profile on the resulting System Version.

**Rationale:** Bug already has both `Severity` (how bad the defect is) and `Priority` (how soon to fix it). These are independent: a Critical bug found in testing can wait for the next sprint (P1/P2); a Critical bug from a SEV-0 production incident cannot (P0). Rather than adding a third dimension (`Urgency`), we document that P0 = sprint bypass. The Work Model states the default; the Operating Model determines the exact sprint-bypass mechanism (interrupt capacity, dedicated on-call, etc.).

**Alternative rejected:** Separate `Urgency` field. Rejected because P0 already carries the semantics and adding a third dimension would create confusion about which field governs sprint bypass.

### D2: System Version supports Standard and Emergency quality gate profiles

**Decision:** System Version gains a `Gate Profile` field with two values: `Standard` and `Emergency`.

| Profile | Non-Negotiable Gates | Deferrable Gates |
|---|---|---|
| **Standard** | All gates required: test coverage, tests passed, security scan, performance benchmark, static analysis, dependency audit | None |
| **Emergency** | Peer review, security scan, smoke tests | Full regression suite, performance benchmarks, static analysis (may be deferred) |

**Rationale:** Emergency hotfixes need to ship within hours, not days. Full regression suites and performance benchmarks can take hours and may block critical fixes. However, peer review (second pair of eyes on the change), security scan (no new vulnerabilities introduced), and smoke tests (basic functionality works) are non-negotiable — they prevent a hotfix from introducing a worse problem.

The distinction between non-negotiable and deferrable is based on **risk of harm**: peer review and security scan prevent introducing new defects; smoke tests confirm the fix works. Full regression and performance benchmarks confirm the fix doesn't break anything else — important, but the risk is lower for a narrowly scoped hotfix and the verification cost is higher.

### D3: Deferred-gate obligation

**Decision:** Emergency System Versions carry deferred gates. The originating Bug remains at status `Fixed` (not `Verified`/`Closed`) until a subsequent Standard System Version passes all deferred gates. A `Deferred Gate Obligation` field on Bug tracks this obligation.

**Rationale:** Without this mechanism, emergency hotfixes permanently lower quality standards — "we shipped it as an emergency, full tests never ran." The deferred-gate pattern ensures that every emergency fix eventually passes full quality gates. The Bug entity is the natural tracker because it is already the work item that stays open until the defect is fully resolved and verified.

### D4: Hotfix branch strategy is Operating Model territory

**Decision:** The Work Model captures `Git Reference` (commit SHA or tag) on System Version but does not prescribe branching strategy. Hotfix branch patterns (branch from release tag, cherry-pick to main, etc.) are Operating Model concerns.

**Rationale:** Branching strategy varies by team maturity, repository structure (monorepo vs. polyrepo), and release model (trunk-based vs. gitflow). The Work Model is tool-agnostic and process-agnostic — it captures *what was produced* (the System Version with its git reference), not *how the code was organized*. The story file documents common patterns as Operating Model guidance.

## Consequences

**Positive:**
- No new fields on Bug beyond the tracking obligation — P0 carries the semantics
- Emergency gate profile is explicit and auditable on System Version — not a verbal "we skipped tests"
- Deferred-gate pattern prevents permanent quality erosion
- Branching strategy stays in Operating Model where it belongs

**Negative:**
- Organizations must discipline themselves to follow through on deferred-gate obligations — the Bug staying at `Fixed` is a nudge, not enforcement
- The non-negotiable vs. deferrable gate split is a default that may need calibration per organization (e.g., some may make static analysis non-negotiable)
- P0 as sprint-bypass signal is a convention, not a structural constraint — teams unfamiliar with the convention may not act on it

---
