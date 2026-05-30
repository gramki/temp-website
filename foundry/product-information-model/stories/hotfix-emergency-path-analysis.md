# Hotfix / Emergency Fix Path: Analysis and Guide

## Why a Named Hotfix Pattern Matters

Every enterprise SaaS product will eventually have a SEV-0 incident at 2 AM that requires a code fix deployed to production within hours. Without a named, documented fast-path, teams either:

1. **Ad-hoc their way through** — skipping quality gates without documentation, creating technical debt and compliance gaps
2. **Follow the standard path** — taking days for a fix that needs hours, while customers suffer

The UPIM models this as a **named pattern** that spans two tracks (Build and Run) and three decision records (DR-029, DR-030, DR-031). The pattern is not a separate workflow — it uses the same entities as standard work, but with explicit fast-path conventions for priority, quality gates, and governance.

## The End-to-End Chain

Each link in the chain is an existing UPIM entity with explicit fast-path behavior:

```
Incident (SEV-0/SEV-1, artifact)
  → Incident Response Task (triage, workaround, preliminary RCA)
    → Bug (P0, Run provenance, sprint bypass)
      → Technical Task (sprint bypass, immediate allocation)
        → System Version (Emergency gate profile)
          → System Deployment Specification (environment-specific)
            → Change Request (Emergency-Technical)
              → Deployment Task (applies specification)
                → Deployment (artifact)
                  → Verification Task (post-deployment checks)
```

| Entity | Track | Fast-Path Behavior | Standard Behavior |
|---|---|---|---|
| Bug | Build (Build) | P0, Run provenance — sprint bypass; immediate triage | P1-P3 — scheduled into sprint |
| Technical Task | Build (Build) | Inherits P0 sprint bypass — immediate allocation outside sprint capacity | Allocated within sprint |
| System Version | Build (Build) | Emergency gate profile — peer review + security scan + smoke tests only | Standard gate profile — all gates required |
| Change Request | Run (Run) | Emergency-Technical — abbreviated soak, documented waivers | Standard — full Train traversal, CAB approval |
| Deployment Task | Run (Run) | May skip Deployment Drill; direct deployment with documented justification | Drill may precede deployment |
| Verification Task | Run (Run) | Focused smoke/SLA verification; may use shorter verification windows | Full verification criteria |

## Timing Expectations

| Phase | Standard Path | Emergency Path |
|---|---|---|
| Incident detection → Bug creation | N/A (Build-provenance bugs are found in testing) | Minutes to hours (IRT produces Bug during response) |
| Bug triage → work starts | Next sprint planning (days to weeks) | Immediate (P0 = sprint bypass) |
| Technical Task → System Version | Sprint cadence (1-2 weeks) | Hours (focused fix, Emergency gate profile) |
| System Version → deployed to production | Change cycle cadence (days to weeks) | Hours to 1 day (Emergency-Technical CR, abbreviated soak) |
| **Total: Bug to production** | **Days to weeks** | **Hours to 1 day** |

## Quality Gate Trade-Offs

The Emergency gate profile balances speed against safety:

### Non-Negotiable Gates (required for Emergency)

| Gate | Rationale |
|---|---|
| **Peer review** | Second pair of eyes prevents introducing a worse problem. Even at 2 AM, a reviewed hotfix is safer than an unreviewed one. |
| **Security scan** | A hotfix that introduces a vulnerability is catastrophically worse than the original incident. |
| **Smoke tests** | Basic "does the service start and respond" validation. Catches build/config errors before deployment. |

### Deferrable Gates (may be deferred for Emergency)

| Gate | Rationale for Deferral | Risk of Deferral |
|---|---|---|
| **Full regression suite** | Can take hours to run; blocks deployment of a critical fix. | The fix may break something unrelated. Mitigated by: narrow scope of hotfix, post-deployment verification, deferred-gate obligation. |
| **Performance benchmarks** | Requires load testing infrastructure; may not be available at 2 AM. | The fix may introduce a performance regression. Mitigated by: Verification Task with SLO monitoring, deferred benchmarks on subsequent version. |
| **Static analysis** | May flag style/complexity issues unrelated to the fix. | Low risk — static analysis catches code quality issues, not functional defects. |

The Operating Model may adjust these defaults — for example, making static analysis non-negotiable, or allowing performance benchmark deferral only for SEV-0 (not SEV-1).

## The Deferred-Gate Obligation Pattern

Emergency hotfixes must not permanently lower quality standards. The pattern:

1. P0 Bug is fixed → Emergency System Version ships with deferred gates
2. Bug stays at `Fixed` status (not `Verified`/`Closed`)
3. Bug's `Deferred Gate Obligation` field references the Emergency System Version
4. A subsequent Standard System Version (with the fix cherry-picked to main) passes all deferred gates
5. Bug moves to `Verified` → `Closed`

This creates a visible, queryable obligation: "which Bugs have outstanding deferred gates?" If the deferred gates are never resolved, the Bug stays open — a persistent reminder that quality debt exists.

### What happens if the deferred gates fail?

The subsequent Standard System Version that runs the full regression may reveal that the hotfix breaks something. At that point, the Bug is already tracked and the team has two options:

1. Fix the regression in the same System Version (before release)
2. Create a new Bug for the regression, linked to the original

Either way, the deferred-gate pattern surfaces the problem — which is better than never knowing.

## Hotfix Branch Strategy (Operating Model Guidance)

The Work Model captures `Git Reference` on System Version but does not prescribe branching strategy. Common patterns:

| Pattern | When to Use | How It Works |
|---|---|---|
| **Branch from release tag** | Polyrepo, gitflow-style | Create `hotfix/INC-2026-0847` branch from the release tag currently in production; fix, test, deploy; cherry-pick to `main` afterward |
| **Cherry-pick from main** | Monorepo, trunk-based | Fix on `main`; cherry-pick the fix commit(s) to a release branch; deploy from release branch |
| **Direct to main** | Trunk-based, continuous deployment | Fix on `main`; deploy `main` to production with the fix | Simplest but requires high CI/CD maturity |

The choice depends on repository structure, release model, and team maturity. The Work Model is tool-agnostic — it tracks the `Git Reference` regardless of how the branch was managed.

## Relationship to Emergency-Technical CR (DR-029)

The Emergency-Technical Change Request and the P0 Bug/Emergency System Version are complementary fast-paths in different tracks:

| Concern | Entity | Track | DR |
|---|---|---|---|
| **How fast do we fix?** | Bug (P0) → Technical Task → System Version (Emergency) | Build (Build) | DR-031 |
| **How fast do we deploy?** | Change Request (Emergency-Technical) → Deployment Task | Run (Run) | DR-029 |

Together they form the complete hotfix workflow. The Build Track fast-path produces the Emergency System Version; the Run Track fast-path deploys it with abbreviated governance. Neither is sufficient alone — a P0 Bug with Standard CR would wait for the normal change cycle; an Emergency-Technical CR with a Standard System Version would wait for full regression.

## The Parallel Incident Response Track

While the Build Track is fixing the root cause, the Run Track is independently managing the incident:

- **Incident Response Task** — has already applied a workaround to restore service (DR-030)
- **Customer Communication Task** — is keeping affected parties informed (DR-030)
- **Post-Incident Review** — will be scheduled after resolution (for SEV-0/1/2) (DR-030)

The hotfix and the incident response run in parallel. The Incident Response Task may have restored service with a workaround hours before the permanent fix ships. The hotfix replaces the workaround with a proper fix; the Verification Task confirms the fix holds.

## Pros and Cons

### Pros

1. **No new entity** — uses existing Bug, Technical Task, System Version, Change Request entities with documented conventions
2. **Auditable** — Emergency gate profile is recorded on System Version; deferred gates are tracked via Bug; Change Request documents waivers
3. **Quality preservation** — deferred-gate obligation prevents permanent quality erosion
4. **Timing clarity** — the model makes explicit what is compressed (sprint allocation, gate profile, soak time) and what is not (peer review, security scan)
5. **Compliance-friendly** — regulated environments can audit the complete chain: Incident → Bug → System Version (Emergency) → CR (Emergency-Technical) → Deployment → Verification

### Cons

1. **Convention-based, not structurally enforced** — P0 = sprint bypass is a convention; nothing prevents a team from ignoring it
2. **Deferred-gate discipline required** — teams must follow through on deferred obligations; the Bug staying at `Fixed` is a nudge, not enforcement
3. **Gate profile calibration** — the non-negotiable vs. deferrable split is a default that organizations must calibrate to their risk tolerance

### Do's and Don'ts

| Do | Don't |
|---|---|
| Triage Run-provenance SEV-0/SEV-1 Bugs as P0 immediately | Let P0 Bugs wait for sprint planning |
| Record Emergency gate profile explicitly on System Version | Skip gates without documenting the deferral |
| Track deferred-gate obligations via the Bug entity | Close the Bug before deferred gates pass |
| Cherry-pick the fix to main (or equivalent) for the subsequent Standard version | Leave the fix only on a hotfix branch |
| Run Verification Task after Emergency deployment | Skip post-deployment verification because "it's urgent" |
| Complete PIR for the incident that triggered the hotfix | Treat the hotfix as the end of the story |

---
