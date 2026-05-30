# Release Artifacts Console

**URL pattern:** `/workbenches/{workbenchId}/consoles/release-artifacts`

**Group:** Build

**Purpose:** Deployment status, release history, versions, and Olympus Weave integration.

---

## Page Sections

### 1. Deployment Overview

| Element | Description |
|---------|-------------|
| **Systems** | All Systems in this Workbench |
| **Latest versions** | Most recent deployed version per System |
| **Deployment regions** | Where deployments exist |
| **Pending releases** | Awaiting deployment |
| **EoS/Deprecation alerts** | Flagged versions |

### 2. System Deployment Cards

| Element | Description |
|---------|-------------|
| **System name** | Identity |
| **Olympus Product Module code** | Weave identifier |
| **Current version** | Latest deployed |
| **Regions** | Where it's deployed |
| **Health** | From Weave |
| **EoS warning** | If approaching end-of-support |

### 3. Deployment Matrix

| System | Dev | Staging | Prod-US | Prod-EU | Prod-APAC |
|--------|-----|---------|---------|---------|-----------|
| System A | v2.3 | v2.2 | v2.1 | v2.1 | v2.0 |
| System B | v1.5 | v1.5 | v1.4 | v1.4 | v1.4 |

Shows which version is deployed where.

### 4. Release History

| Column | Description |
|--------|-------------|
| Version | Release version |
| System | Which System |
| Released | Timestamp |
| Regions | Deployed to |
| Released by | Who triggered |
| Status | Active, EoS, deprecated |

### 5. Pending Releases

| Element | Description |
|---------|-------------|
| **Awaiting approval** | Releases pending Governance gate |
| **Awaiting deployment** | Approved but not deployed |
| **Scheduled** | Future deployments |

### 6. Version Detail View

| Element | Description |
|---------|-------------|
| **Version info** | Number, release notes |
| **Build** | Source CI build |
| **Artifacts** | Deployed artifacts |
| **Deployment history** | When/where deployed |
| **Rollback info** | Previous version to roll back to |

---

## Actions

| Action | Who | Description |
|--------|-----|-------------|
| Create release | Manager | Package version for deployment |
| Deploy | Manager | Trigger deployment to region |
| Rollback | Manager | Revert to previous version |
| Schedule deployment | Manager | Set future deployment time |
| View in Weave | All | Open Olympus Weave console |

---

## Filters

- By System
- By region
- By version status (active, EoS, deprecated)
- By date range

---

## Integrations

- **Olympus Weave** — Deployment platform, version tracking, EoS metadata
- **CI Console** — Builds that produce releases
- **Governance** — Release gates

---

## Related Consoles

- **CI Console** — Builds producing artifacts
- **Components Console** — System definitions
- **Quality Status** — Quality gates for release
- **Governance Overview** — Release governance status
- **Registers** — Release-related risks, debt, and exceptions
