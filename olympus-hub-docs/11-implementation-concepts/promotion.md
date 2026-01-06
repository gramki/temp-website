# Promotion

> **Category:** Platform Foundation

---

## Overview

**Promotion** is the controlled movement of artifacts from one Workbench or Subscription to another. Unlike Git merges or CI/CD deployments, Promotion is a first-class Hub operation with explicit approval, complete artifact copying, and comprehensive audit trails. Promotion is how work moves from development to production in Hub.

---

## Ontology Context

### Relationship to Ontology

The ontology doesn't address how automations move between environments or how changes are deployed. Promotion is an implementation concept that fills this gap for regulated environments.

| Ontology Concept | Implementation | Relationship |
|------------------|----------------|--------------|
| Automation | Hub Application | Promotion moves applications |
| (not covered) | Promotion | Controlled artifact movement |

### Gap This Fills

The ontology focuses on runtime operations. Promotion addresses:
1. **Change management**: How do changes move to production?
2. **Approval workflow**: Who authorizes changes?
3. **Artifact integrity**: What exactly is being deployed?
4. **Audit trail**: What was promoted, when, by whom?

---

## Definition

**Promotion** is a controlled artifact movement operation that:
- Moves a Scenario (with all associated artifacts) from source to target
- Requires explicit approval (configurable per destination)
- Physically copies artifacts (not references)
- Creates complete audit trail
- Supports cross-subscription movement

### Characteristics

| Characteristic | Description |
|----------------|-------------|
| **Scope** | Subscription or Workbench level |
| **Lifecycle** | Requested by Developer; approved by Admin/Supervisor |
| **Ownership** | Admin defines paths; Developer requests; Admin approves |
| **Multiplicity** | Many promotions; one per request |

---

## Rationale

### Why This Design?

Explicit promotion enables:
1. **Compliance**: Clear approval and audit trail
2. **Isolation**: PROD never pulls from DEV registry
3. **Rollback**: Known good versions to revert to
4. **Visibility**: Everyone knows what's in production

### Alternatives Considered

| Alternative | Why Not Chosen |
|-------------|----------------|
| **Git merge + auto-deploy** | No explicit approval; audit gaps |
| **Reference-based deployment** | PROD depends on DEV availability |
| **Manual artifact copy** | Error-prone; no audit trail |

### Related ADRs

| ADR | Decision |
|-----|----------|
| [ADR-0046](../decision-logs/0046-semver-promotion-compatibility.md) | Semantic version compatibility for promotion |
| [ADR-0047](../decision-logs/0047-scenario-atomic-promotion-unit.md) | Scenario as atomic promotion unit |
| [ADR-0048](../decision-logs/0048-physical-copy-cross-subscription.md) | Physical copy for cross-subscription promotion |

---

## Structure

### Promotion Unit Hierarchy

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    PROMOTION UNITS                                           │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│   SMALLEST ◀─────────────────────────────────────────────────▶ LARGEST      │
│                                                                              │
│   ┌───────────────┐    ┌───────────────┐    ┌───────────────┐              │
│   │   SCENARIO    │    │   WORKBENCH   │    │ SUBSCRIPTION  │              │
│   │   ─────────   │    │   ─────────   │    │ ────────────  │              │
│   │               │    │               │    │               │              │
│   │ • Hub App     │    │ • Scenarios   │    │ • Workbenches │              │
│   │ • Triggers    │    │ • Resources   │    │ • Resources   │              │
│   │ • Specs (3)   │    │ • Configs     │    │ • Configs     │              │
│   │ • Templates   │    │               │    │               │              │
│   │               │    │               │    │               │              │
│   │ ATOMIC UNIT   │    │ All Scenarios │    │ All WBs       │              │
│   └───────────────┘    └───────────────┘    └───────────────┘              │
│                                                                              │
└──────────────────────────────────────────────────────────────────────────────┘
```

### Promotion Destination

```yaml
apiVersion: hub.olympus.io/v1
kind: PromotionDestination
metadata:
  name: dev-to-prod
  namespace: acme-bank
spec:
  # Target
  target:
    type: subscription  # subscription | workbench
    subscription_id: acme-prod
    workbench_id: dispute-ops-prod  # if type is workbench
  
  # Approval configuration
  approval:
    required: true
    approver_roles:
      - tenant-admin
      - supervisor
    
  # Notifications
  notifications:
    on_request: [requester, admin]
    on_approval: [requester, admin, ops-team]
    on_completion: [requester, admin, ops-team]
    on_failure: [requester, admin]
```

### Promotion Request

```yaml
apiVersion: hub.olympus.io/v1
kind: PromotionRequest
metadata:
  name: promo-req-001
  namespace: acme-bank
spec:
  # What to promote
  unit:
    type: scenario
    scenario_id: standard-dispute
    version: "1.3.0"
  
  # Source
  source:
    subscription_id: acme-dev
    workbench_id: dispute-ops-dev
    
  # Target (references destination)
  destination_ref: dev-to-prod
  
  # Request details
  reason: "New fraud detection rules - JIRA-1234"
  requested_by: developer-alice
  requested_at: "2026-01-06T10:00:00Z"

status:
  phase: PENDING_APPROVAL  # PENDING | APPROVED | REJECTED | IN_PROGRESS | COMPLETED | FAILED
  approvals:
    - approver: admin-bob
      decision: APPROVED
      timestamp: "2026-01-06T11:00:00Z"
      comment: "Reviewed and approved for production"
```

---

## Behavior

### Promotion Flow

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    PROMOTION WORKFLOW                                        │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│   1. REQUEST                           2. REVIEW                             │
│   ┌─────────────────────┐             ┌─────────────────────┐               │
│   │ Developer requests  │────────────▶│ Admin reviews       │               │
│   │ promotion           │             │ ├── Scenario specs  │               │
│   │ ├── Scenario        │             │ ├── Hub Application │               │
│   │ ├── Version         │             │ ├── Test results    │               │
│   │ └── Reason          │             │ └── Dependencies    │               │
│   └─────────────────────┘             └──────────┬──────────┘               │
│                                                  │                           │
│                          ┌───────────────────────┼───────────────────────┐  │
│                          │                       │                       │  │
│                          ▼                       ▼                       ▼  │
│   3a. APPROVED          3b. REJECTED            3c. MORE INFO            │  │
│   ┌────────────┐        ┌────────────┐          ┌────────────┐           │  │
│   │ Proceed    │        │ Closed     │          │ Back to    │           │  │
│   │ to copy    │        │ with reason│          │ requester  │           │  │
│   └─────┬──────┘        └────────────┘          └────────────┘           │  │
│         │                                                                   │
│         ▼                                                                   │
│   4. COPY ARTIFACTS                                                         │
│   ┌─────────────────────────────────────────────────────────────────────┐  │
│   │                                                                      │  │
│   │   Container Images ───────────────▶ Target Registry                 │  │
│   │   CRDs (all 3 specs) ─────────────▶ Target Git Repository           │  │
│   │   Notification Templates ─────────▶ Target Git Repository           │  │
│   │   Migration CRDs ─────────────────▶ Target Git Repository           │  │
│   │                                                                      │  │
│   └─────────────────────────────────────────────────────────────────────┘  │
│         │                                                                   │
│         ▼                                                                   │
│   5. SYNC & DEPLOY                                                          │
│   ┌────────────────────┐                                                   │
│   │ Target workbench   │                                                   │
│   │ syncs from Git     │                                                   │
│   │ ├── CRDs applied   │                                                   │
│   │ ├── Migrations run │                                                   │
│   │ └── App deployed   │                                                   │
│   └────────────────────┘                                                   │
│         │                                                                   │
│         ▼                                                                   │
│   6. COMPLETE                                                               │
│   ┌────────────────────┐                                                   │
│   │ Notifications sent │                                                   │
│   │ Audit trail closed │                                                   │
│   └────────────────────┘                                                   │
│                                                                              │
└──────────────────────────────────────────────────────────────────────────────┘
```

### What Gets Promoted (Scenario)

```
Scenario Promotion Includes:
├── ScenarioNormativeSpec
├── ScenarioAutomationSpec
├── ScenarioDeploymentSpec
├── Hub Application container(s)
├── TriggerSpecs (referenced)
├── NotificationTemplateSpecs (referenced)
└── Migration CRDs (if data store changes)
```

### Version Compatibility

```
Promotion requires version compatibility:

Source Workbench Spec Version: 2.0.0
Target Workbench Spec Version: 2.0.0  ← Must match

If mismatch:
- Promote Workbench first
- Or update target to compatible version
```

### Interactions

| Interacts With | Direction | Description |
|----------------|-----------|-------------|
| Artifact Registry | → copies to | Container images copied to target |
| Git Repository | → copies to | CRDs copied to target |
| Notification Services | → notifies | Stakeholders notified |
| Workbench Management | → triggers sync | Target syncs promoted artifacts |

---

## Constraints and Invariants

| Constraint | Description |
|------------|-------------|
| **Atomic scenario** | Entire Scenario promotes together |
| **Version compatibility** | Source/target specs must be compatible |
| **Approval required** | Cross-subscription always requires approval |
| **Physical copy** | Artifacts are copied, not referenced |
| **Audit trail** | All actions logged |

---

## Pros and Cons

### Benefits

| Benefit | Description |
|---------|-------------|
| ✅ **Clear approval** | Explicit authorization for production |
| ✅ **Complete audit** | Full trail of who, what, when |
| ✅ **Isolation** | Target independent of source |
| ✅ **Rollback** | Previous version always available |
| ✅ **Compliance** | Meets regulated industry requirements |

### Trade-offs

| Trade-off | Mitigation |
|-----------|------------|
| ⚠️ **Copy time** | Efficient copy; lean containers |
| ⚠️ **Storage duplication** | Lifecycle policies; cleanup |
| ⚠️ **Approval delay** | Clear SLAs; escalation paths |

---

## Examples

### Example 1: Scenario Promotion

```bash
# Developer requests promotion
hub promote scenario standard-dispute \
  --version 1.3.0 \
  --from dispute-ops-dev \
  --to dispute-ops-prod \
  --reason "JIRA-1234: New fraud detection rules"

# Output:
Promotion request created: promo-req-001
Status: PENDING_APPROVAL
Awaiting approval from: tenant-admin
```

### Example 2: Cross-Subscription Promotion

```yaml
# Promotion from DEV subscription to PROD subscription
source:
  subscription: acme-dev
  workbench: dispute-ops-dev

target:
  subscription: acme-prod  # Different subscription!
  workbench: dispute-ops-prod

artifacts_copied:
  - Container: dispute-handler:1.3.0
    from: registry.../acme-dev/snapshot/dispute-handler:1.3.0
    to:   registry.../acme-prod/production/dispute-handler:1.3.0
    
  - CRDs: 3 scenario specs + 2 triggers
    from: git.../acme-dev/workbenches/dispute-ops-dev/
    to:   git.../acme-prod/workbenches/dispute-ops-prod/
```

---

## Implementation Notes

### For Developers

- Test thoroughly in DEV before requesting promotion
- Include meaningful reason/JIRA reference
- Ensure all dependencies are promotable
- Check version compatibility before requesting

### For Operators

- Configure approval workflows per destination
- Monitor promotion queue for backlogs
- Review failed promotions promptly
- Maintain promotion destination configurations

---

## Related Concepts

| Concept | Relationship |
|---------|--------------|
| [Subscription](./subscription.md) | Promotion crosses subscriptions |
| [Dev-Lifecycle-Stage](./dev-lifecycle-stage.md) | Stage determines promotion eligibility |
| [Artifact Registry](./artifact-registry.md) | Source and target for artifacts |
| [Scenario Specification Types](./scenario-specification-types.md) | What gets promoted |

---

## References

- [Promotion Model](../04-subsystems/artifact-registry/promotion-model.md)
- [Hub Development Flow Primer](../10-guides/hub-development-flow/README.md)
- [ADR-0047: Scenario as Atomic Promotion Unit](../decision-logs/0047-scenario-atomic-promotion-unit.md)
- [ADR-0048: Physical Copy Cross-Subscription](../decision-logs/0048-physical-copy-cross-subscription.md)

