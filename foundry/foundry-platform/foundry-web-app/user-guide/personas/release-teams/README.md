# Release Teams — Jobs to be Done

**Primary Workspace:** Release

**Role:** Manage and produce Product Delivery — build, verify, package, and publish artifacts to distribution stores.

## Prerequisites

- Access to a Workbench with Release Workspace membership
- Familiarity with CI/CD pipelines and artifact management
- Understanding of [Evidence Packs](../../../../release-tools/platform-developer-guide/ci/ci.TODO) and release readiness criteria

---

## Primary Jobs

### J1. View release pipeline status and Work Orders
**When** I need to understand release state  
**I want to** see all release-related Work Orders and pipeline status  
**So that** I can manage the release process

**Acceptance Criteria:**
- Release Work Orders with status
- CI/CD pipeline status (running, passed, failed)
- Artifacts in progress
- Release timeline/schedule

---

### J2. Monitor CI/CD job progress
**When** builds and pipelines are running  
**I want to** see real-time progress and logs  
**So that** I can detect and address failures quickly

**Acceptance Criteria:**
- Pipeline visualization (stages, jobs)
- Real-time log streaming
- Failure alerts
- Retry/restart actions
- Link to full CI system

---

### J3. Review release evidence packs
**When** preparing for release  
**I want to** review the evidence pack (test results, quality metrics, approvals)  
**So that** I can confirm release readiness

**Acceptance Criteria:**
- Evidence pack summary
- Test results summary
- Quality gate status
- Approval status
- Missing evidence alerts

---

### J4. Publish verified artifacts to distribution stores
**When** artifacts are ready  
**I want to** publish them to the appropriate distribution store  
**So that** they are available for deployment

**Acceptance Criteria:**
- Artifact selection
- Target store selection
- Version/tag assignment
- Signing and provenance
- Publish confirmation

---

### J5. Trigger release scenarios
**When** I need to initiate a build, package, or publish  
**I want to** trigger the appropriate scenario  
**So that** the release process starts

**Acceptance Criteria:**
- Scenario selection (build, package, publish)
- Input parameters
- Trigger confirmation
- Progress tracking

---

### J6. Track artifact versions and provenance
**When** I need to understand what's released  
**I want to** see artifact history, versions, and provenance  
**So that** I can trace any release

**Acceptance Criteria:**
- Artifact inventory
- Version history
- Provenance chain (source commit, build, tests)
- Deployment destinations

---

## Supporting Jobs

### J7. Access Operations repository
**When** I need deployment descriptors or records  
**I want to** browse the Operations repository  
**So that** I can find release artifacts

---

### J8. View agent-embedded CI results
**When** agents participate in CI  
**I want to** see their outputs and decisions  
**So that** I can verify their work

---

### J9. Monitor release blockers
**When** a release is blocked  
**I want to** see what's blocking and why  
**So that** I can unblock it

**Acceptance Criteria:**
- Blocker list with reasons
- Link to blocking Work Order/gate
- Suggested resolution

---

### J10. Review release-related defects
**When** defects block release  
**I want to** see open defects affecting the release  
**So that** I can assess risk

---

### J11. Track release history by Workbench
**When** reviewing past releases  
**I want to** see release history for a Workbench  
**So that** I can understand release patterns

**Acceptance Criteria:**
- Release history by Product Intent and Customer Release Intent
- Filter by Delivery and Release Renewal Product Intent purposes
- Do not treat non-Delivery Build work as customer release scope
- Release Renewal Map in PI Console showing Delivered Product Intent → Release Evidence → Feedback / Learnings → Renewed Product Intent
- Links to evidence packs and renewed intent records

---

### J12. Coordinate with Governance on release approvals
**When** release requires governance sign-off  
**I want to** see approval status and request approval  
**So that** release proceeds

---

## Related

- [CI Console](../../../platform-developer-guide/pages/consoles/build/ci-console.md) — Pipeline monitoring
- [Release Artifacts console](../../../platform-developer-guide/pages/consoles/build/release-artifacts.md) — Artifact management
- [Quality Status console](../../../platform-developer-guide/pages/consoles/build/quality-status.md) — Build quality indicators
- [Release Workspace console](../../../platform-developer-guide/pages/consoles/workspaces/workspace-release.md) — Release Workspace view
- [Release Tools user guide](../../../../release-tools/user-guide/README.md) — CI/CD documentation index

## Open Questions

- What's the boundary between Release (Build Track) and Deployment (Run Track)?
- How do agent-embedded CI jobs differ from traditional CI?
- What artifact signing and provenance standards apply?
