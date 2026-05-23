# Track Console

**URL pattern:** `/workbenches/{workbenchId}/consoles/track`

**Group:** Work

**Purpose:** Per-Track work analytics — view work flow through Discovery, Build, Run, Win, Evolve, Governance.

---

## Page Sections

### 1. Track Overview

| Track | Workspaces | Indicators |
|-------|------------|------------|
| **Discovery** | Product Specification, UX Design | Active WOs, items in discovery |
| **Build** | Development, QA, Release | Active WOs, builds, tests, deployments |
| **Run** | (Operations-focused) | Incidents, operational items |
| **Win** | (Customer success-focused) | Feedback items, adoption metrics |
| **Evolve** | (Evolution-focused) | Technical debt, improvements |
| **Governance** | Governance | Gate reviews, compliance items |

### 2. Track Flow Visualization

```
Discovery ──→ Build ──→ Release ──→ Run
                ↑                    │
                └──── Evolve ←───────┘
                         ↑
                    Governance (gates)
```

| Element | Description |
|---------|-------------|
| **PI positions** | Where each PI currently sits |
| **Flow rates** | Items moving between Tracks |
| **Bottlenecks** | Tracks with accumulating items |

### 3. Track Detail View (Drill-down)

| Element | Description |
|---------|-------------|
| **Track header** | Name, description |
| **Active PIs** | PIs with work in this Track |
| **Work Orders** | WOs executing in this Track |
| **Scenarios** | Scenarios available for this Track |
| **Metrics** | Cycle time, throughput for this Track |

### 4. Track Metrics

| Metric | Description |
|--------|-------------|
| **Throughput** | Items completed per week |
| **Cycle time** | Average time in Track |
| **WIP** | Work in progress count |
| **Wait time** | Time items spend waiting |

---

## Filters

- By Track
- By PI
- By date range
- By status

---

## Phase 1 Tracks

Phase 1 focuses on: **Discovery, Build, Release, Governance**

Run, Win, Evolve are visible but may have limited Scenarios.

---

## Related Consoles

- **Workspaces Console** — Workspace-level view
- **Progress Console** — Overall completion metrics
- **PI Console** — See PI flow through Tracks
