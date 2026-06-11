# PI Artifacts Reference

[← Back to ERE Guide](../README.md)

Program Increment (PI) artifacts follow SAFe terminology. This reference defines each artifact and its purpose.

---

## Overview

Each PI folder in `ENG-{CODE}-project/pi/PI-{N}/` contains these artifacts:

| Artifact | SAFe Concept | When Created | Owner |
|----------|--------------|--------------|-------|
| `README.md` | PI Summary | PI Planning | EPM |
| `pi-objectives.md` | PI Objectives | PI Planning | EPM + EPO |
| `pi-backlog.md` | Program Backlog (PI slice) | PI Planning | EPO |
| `program-board.md` | Program Board | PI Planning | EPM + EA |
| `pi-risks.md` | ROAM Board | PI Planning, updated continuously | EPM |
| `confidence-vote.md` | Confidence Vote | End of PI Planning | ELs |
| `staffing.md` | PI Staffing | PI Planning | EPM |
| `iterations/` | Iteration Plans | Each iteration | ELs |
| `decisions/` | PI Decisions | As needed | Various |
| `pi-retrospective.md` | Inspect & Adapt | End of PI | EPM |

---

## Artifact Definitions

### pi-objectives.md — PI Objectives

**SAFe Concept:** PI Objectives

Committed business and technical objectives for the PI. Written in SMART format.

**Content:**

| Section | Description |
|---------|-------------|
| Business Objectives | Customer-facing outcomes; value delivered |
| Technical Objectives | Enablers, infrastructure, architecture work |
| Uncommitted Objectives | Stretch goals if capacity allows |

**Format:**

```markdown
## Business Objectives

| # | Objective | Business Value | Confidence |
|---|-----------|----------------|------------|
| 1 | Complete payment integration | Enables transactions | 4/5 |
| 2 | Launch customer portal MVP | Customer visibility | 5/5 |

## Technical Objectives

| # | Objective | Enabler For | Confidence |
|---|-----------|-------------|------------|
| 1 | Establish CI/CD pipeline | All future work | 5/5 |
| 2 | Performance baseline | Performance tracking | 4/5 |

## Uncommitted Objectives

| # | Objective | Notes |
|---|-----------|-------|
| 1 | Additional payment methods | If capacity allows |
```

---

### pi-backlog.md — Program Backlog (PI slice)

**SAFe Concept:** Program Backlog (sliced to this PI)

Features, enablers, and stories planned for this PI.

**Content:**

| Section | Description |
|---------|-------------|
| Features | Large capabilities broken into stories |
| Enablers | Technical foundation work |
| Stories | User stories assigned to iterations |

**Format:**

```markdown
## Features

| ID | Feature | Status | Iterations | Owner |
|----|---------|--------|------------|-------|
| F1 | Payment Processing | 🟢 On Track | I1-I3 | Squad A |
| F2 | Customer Dashboard | 🟡 At Risk | I2-I4 | Squad B |

## Enablers

| ID | Enabler | Status | Iteration | Owner |
|----|---------|--------|-----------|-------|
| E1 | CI/CD Setup | ✅ Complete | I1 | Platform |
| E2 | Monitoring | 🟢 On Track | I2 | SRE |

## Stories by Iteration

### Iteration 1
- [ ] Story 1.1 — Payment gateway integration
- [ ] Story 1.2 — Basic transaction flow
...
```

---

### program-board.md — Program Board

**SAFe Concept:** Program Board

Visualizes delivery timeline, cross-team dependencies, and milestones.

**Content:**

| Section | Description |
|---------|-------------|
| Timeline | PI iterations with key dates |
| Dependencies | Cross-squad and external dependencies |
| Milestones | Major delivery milestones |

**Format:**

```markdown
## Timeline

| Iteration | Dates | Theme |
|-----------|-------|-------|
| I1 | 2024-03-01 to 2024-03-14 | Foundation |
| I2 | 2024-03-15 to 2024-03-28 | Core Features |
| I3 | 2024-03-29 to 2024-04-11 | Integration |
| I4 | 2024-04-12 to 2024-04-25 | Stabilization |

## Dependencies

| ID | From | To | Item | Status | Due |
|----|------|-----|------|--------|-----|
| D1 | Squad A | Squad B | Payment API | 🟢 On Track | I2 |
| D2 | External | Squad A | Vendor SDK | 🟡 At Risk | I1 |

## Milestones

| Milestone | Date | Status |
|-----------|------|--------|
| Feature Complete | 2024-04-11 | 🟢 On Track |
| UAT Start | 2024-04-15 | 🟢 On Track |
| Go-Live | 2024-04-30 | 🟢 On Track |
```

---

### pi-risks.md — ROAM Board

**SAFe Concept:** ROAM (Resolved, Owned, Accepted, Mitigated)

Tracks PI-level risks with ROAM status.

**Content:**

| Column | Description |
|--------|-------------|
| ID | Risk identifier |
| Risk | Description of the risk |
| Status | ROAM status with indicator |
| Owner | Who is responsible |
| Mitigation | Actions taken or planned |
| Last Updated | When status last changed |

**Format:**

```markdown
## Active Risks

| ID | Risk | Status | Owner | Mitigation |
|----|------|--------|-------|------------|
| R1 | Vendor API stability | 🔶 [O] | @ea | Circuit breaker; fallback mode |
| R2 | Resource availability | 🛡️ [M] | @epm | Cross-training complete |
| R3 | Scope expansion | 🤝 [A] | @epm | Change control enforced |

## Resolved Risks

| ID | Risk | Resolution | Date |
|----|------|------------|------|
| R0 | Initial access provisioning | ✅ [R] Access granted | 2024-03-05 |
```

See [Markdown Style Guide](markdown-style-guide.md#roam-risk-status-safe) for ROAM transition rules.

---

### confidence-vote.md — Confidence Vote

**SAFe Concept:** Confidence Vote

Squad-by-squad confidence in achieving PI objectives. Captured at the end of PI Planning.

**Content:**

| Column | Description |
|--------|-------------|
| Squad | Squad name |
| Confidence | Score 1-5 (fingers) |
| Concerns | Any issues affecting confidence |

**Format:**

```markdown
## Confidence Vote Results

| Squad | Confidence | Concerns |
|-------|------------|----------|
| Squad A | 4 | Vendor dependency timing |
| Squad B | 5 | None |
| Squad C | 3 | Resource availability |
| Verification | 4 | Environment readiness |

**Overall:** 4.0 average

### Actions from Low Confidence

- Squad C: Cross-training scheduled with Platform team
- Environment readiness: SRE escalation in progress
```

---

### iterations/ — Iteration Plans

**SAFe Concept:** Iteration Plans

Per-sprint planning artifacts.

**Structure:**

```
iterations/
├── iteration-1.md
├── iteration-2.md
├── iteration-3.md
└── iteration-4.md
```

**Content per iteration:**

```markdown
# Iteration 1

**Dates:** 2024-03-01 to 2024-03-14
**Theme:** Foundation

## Goals
1. Establish CI/CD pipeline
2. Complete payment gateway integration

## Capacity

| Squad | Available | Allocated | Buffer |
|-------|-----------|-----------|--------|
| Squad A | 80 pts | 72 pts | 10% |

## Stories

| ID | Story | Points | Status | Owner |
|----|-------|--------|--------|-------|
| S1 | Gateway connection | 8 | ✅ Complete | @dev1 |
| S2 | Transaction flow | 13 | 🟢 On Track | @dev2 |

## Iteration Review Notes
(Completed at iteration end)
```

---

### pi-retrospective.md — Inspect & Adapt

**SAFe Concept:** Inspect & Adapt

What worked, what didn't, and improvements for future PIs.

**Format:**

```markdown
# PI-1 Retrospective

**Date:** 2024-04-26
**Facilitator:** @epm

## What Worked Well
- Early risk identification prevented major issues
- Cross-squad collaboration improved
- Customer feedback loop effective

## What Didn't Work
- Environment provisioning delays
- Unclear acceptance criteria on some stories
- Knowledge documentation fell behind

## Improvement Actions

| Action | Owner | Due | Status |
|--------|-------|-----|--------|
| Earlier environment requests | @sre | PI-2 I1 | 🟢 On Track |
| AC review checklist | @epo | PI-2 Planning | ✅ Complete |
| Knowledge capture checkpoints | @epm | Ongoing | 🟢 On Track |

## Metrics

| Metric | Target | Actual |
|--------|--------|--------|
| Velocity | 200 pts | 185 pts |
| Defect escape rate | <5% | 3% |
| Objective achievement | 100% | 90% |
```

---

## Related Content

- [Engagement Repos](../05-document-governance/engagement-repos.md) — where PI artifacts live
- [Markdown Style Guide](markdown-style-guide.md) — formatting conventions
- [Gates and Checkpoints](../06-governance-enforcement/gates-checkpoints.md) — PI-related gates
