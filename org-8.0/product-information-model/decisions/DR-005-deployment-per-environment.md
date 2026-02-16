# DR-005: Deployment Tracked Per-Environment, Not as Version Status

**Status:** Accepted
**Date:** 2026-02-15
**Related FAQ:** Q15

---

## Context

The model needed to represent how Module Versions move from "quality-gated artifact" to "running in production." Initially, "Deployed" was considered as a status on the Module Version entity (e.g., `Building → Released → Deployed`). However, this was challenged:

A single Module Version (e.g., `payments-service v2.3.3`) may need to be deployed to **multiple environments** — staging, production-us, production-eu, production-ap, disaster recovery — at different times, with different strategies, and potentially with different outcomes. "Deployed" is not a binary attribute of the version; it is a per-environment event.

## Decision

Model **Deployment** as a standalone Run Track entity with per-environment tracking, rather than as a status on Module Version.

Module Version status lifecycle: `Building → Released` (only two states).

Deployment entity tracks:
- Which Module Version
- Which Environment (Dim 7)
- Deployment strategy (Canary / Blue-Green / Rolling / Direct)
- Per-environment status (`Planned → In Progress → Succeeded / Failed / Rolled Back`)
- Timestamp

## Rationale

1. **Reality is per-environment.** A Module Version may be deployed to production-us on Tuesday and production-eu on Thursday. Modeling "Deployed" as a version status cannot represent this.
2. **Deployment status is multi-valued.** The same version can be `Succeeded` in one environment and `Failed` in another. A single status field cannot capture this.
3. **Decouples release from deployment.** A Module Version can be `Released` (quality gates passed) without being deployed anywhere. Once deployed (even to production), it may still be behind a feature flag — not yet part of an activated Customer Release. This supports dark launches and canary strategies.
4. **Run Track ownership.** Deployment is an operational activity owned by DevOps/SRE. Making it a standalone entity in the Run Track (alongside Incident, Change Request, Maintenance Task) correctly places it under operational ownership.

## Consequences

- **Positive:** Accurate representation of multi-environment deployment reality.
- **Positive:** Clean separation: Module Version status = quality gate, Deployment status = operational state.
- **Positive:** Supports advanced deployment strategies (canary, blue-green, phased rollout) natively.
- **Positive:** Deployment Planning Task (Run Track) plans deployments, creating a natural workflow.
- **Negative:** Querying "is v2.3.3 fully deployed?" requires checking deployment records across all target environments rather than reading a single status field. Tooling must support this aggregation.
