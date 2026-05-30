# CI Console

**URL pattern:** `/workbenches/{workbenchId}/consoles/ci`

**Group:** Build

**Purpose:** Build and pipeline status — view CI runs, build history, pipeline health.

---

## Page Sections

### 1. Pipeline Overview

| Element | Description |
|---------|-------------|
| **Active pipelines** | Currently running builds |
| **Recent builds** | Last N builds across all repos |
| **Success rate** | % of builds passing |
| **Average duration** | Mean build time |

### 2. Pipeline List

| Column | Description |
|--------|-------------|
| Pipeline | Name/identifier |
| Repository | Source code repo |
| Trigger | Manual, PR, commit, scheduled |
| Status | Running, passed, failed, cancelled |
| Duration | How long it took/is taking |
| Triggered by | User or automation |
| Started | Timestamp |

### 3. Build Detail View (Drill-down)

| Element | Description |
|---------|-------------|
| **Build info** | ID, trigger, commit, branch |
| **Stages** | Pipeline stages with status |
| **Logs** | Build output logs |
| **Artifacts** | Produced artifacts |
| **Test results** | If tests ran, summary |
| **Agent info** | Which agent executed (if applicable) |

### 4. Repository Pipelines

| Element | Description |
|---------|-------------|
| **Per-repo view** | Select a code repo |
| **Pipeline history** | Builds for that repo |
| **Branch status** | Main, feature branches |

---

## Actions

| Action | Who | Description |
|--------|-----|-------------|
| Trigger build | Manager, Member | Manual build trigger |
| Cancel build | Manager, Member | Stop running build |
| Retry build | Manager, Member | Re-run failed build |
| View logs | All | Access build output |
| Download artifacts | All | Get build artifacts |

---

## Filters

- By repository
- By status (running, passed, failed)
- By branch
- By date range
- By trigger type

---

## Integrations

- **GitHub** — Commit/PR triggers, status checks
- **Release Tools module** — Pipeline definitions

---

## Related Consoles

- **Release Artifacts** — Deployments from builds
- **Findings Console** — Scan findings from builds
- **Quality Status** — Test results from CI
- **Components Console** — Which System was built
