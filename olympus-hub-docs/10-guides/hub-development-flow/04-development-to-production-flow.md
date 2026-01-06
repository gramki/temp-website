# Development to Production Flow

[← Previous: Workbench-Based Development](./03-workbench-based-development.md) | [Back to Index](./README.md) | [Next: Daily Workflow →](./05-daily-workflow.md)

---

## The Complete Journey

This document walks through the full lifecycle of a change from development to production.

---

## Overview Diagram

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    DEVELOPMENT TO PRODUCTION FLOW                            │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│   DEV SUBSCRIPTION                                                           │
│   ┌─────────────────────────────────────────────────────────────────────┐   │
│   │                                                                      │   │
│   │   1. DEVELOP                    2. BUILD                            │   │
│   │   ┌────────────┐               ┌────────────┐                       │   │
│   │   │ Edit CRDs  │──────────────▶│ Runtime CI │                       │   │
│   │   │ & Code     │               │ Build+Test │                       │   │
│   │   └────────────┘               └─────┬──────┘                       │   │
│   │                                      │                               │   │
│   │                                      ▼                               │   │
│   │   3. SYNC                       4. TEST                              │   │
│   │   ┌────────────┐               ┌────────────┐                       │   │
│   │   │ Sync to    │◀──────────────│ Snapshot   │                       │   │
│   │   │ DEV WB     │               │ Registry   │                       │   │
│   │   └─────┬──────┘               └────────────┘                       │   │
│   │         │                                                            │   │
│   │         ▼                                                            │   │
│   │   ┌────────────┐                                                    │   │
│   │   │ Test in    │                                                    │   │
│   │   │ DEV WB     │                                                    │   │
│   │   └─────┬──────┘                                                    │   │
│   │         │                                                            │   │
│   └─────────┼────────────────────────────────────────────────────────────┘   │
│             │                                                                │
│             │  5. REQUEST PROMOTION                                          │
│             ▼                                                                │
│   ┌─────────────────────────────────────────────────────────────────────┐   │
│   │                         PROMOTION GATE                               │   │
│   │                                                                      │   │
│   │   ┌────────────┐    ┌────────────┐    ┌────────────┐               │   │
│   │   │ Request    │───▶│ Admin      │───▶│ Approved   │               │   │
│   │   │ Submitted  │    │ Reviews    │    │            │               │   │
│   │   └────────────┘    └────────────┘    └─────┬──────┘               │   │
│   │                                             │                        │   │
│   └─────────────────────────────────────────────┼────────────────────────┘   │
│                                                 │                            │
│                                                 │  6. ARTIFACTS COPIED       │
│                                                 ▼                            │
│   PROD SUBSCRIPTION                                                          │
│   ┌─────────────────────────────────────────────────────────────────────┐   │
│   │                                                                      │   │
│   │   7. DEPLOY                     8. LIVE                              │   │
│   │   ┌────────────┐               ┌────────────┐                       │   │
│   │   │ CRDs sync  │──────────────▶│ Running in │                       │   │
│   │   │ to PROD WB │               │ Production │                       │   │
│   │   └────────────┘               └────────────┘                       │   │
│   │                                                                      │   │
│   └─────────────────────────────────────────────────────────────────────┘   │
│                                                                              │
└──────────────────────────────────────────────────────────────────────────────┘
```

---

## Step-by-Step Walkthrough

### Step 1: Develop

**What you do:** Edit Scenario CRDs and Hub Application code.

```bash
# Your local development
vim scenarios/standard-dispute/automation.yaml
vim applications/dispute-handler/src/main.py
```

**What changes:**
- YAML files for Scenario specifications
- Source code for Hub Applications
- Trigger definitions
- Notification templates

### Step 2: Build

**What you do:** Trigger Runtime CI to build your Hub Application.

```
Runtime CI Pipeline:
├── Checkout source
├── Build container
├── Run unit tests
└── Push to Snapshot Registry
```

**Result:** Container image tagged with version:
```
registry.hub.acme.com/dev-sub/dispute-ops-dev/dispute-handler:1.2.3-beta.1+abc123
```

### Step 3: Sync

**What you do:** Sync CRD changes to your DEV workbench.

| What Gets Synced | Where It Goes |
|------------------|---------------|
| Scenario specs | Workbench runtime |
| Trigger definitions | Signal Exchange |
| Task queue configs | Task Management |
| Application references | Runtime deployment |

**How:**
- Via Developer Console UI: "Sync" button
- Via API: POST to sync endpoint
- Automatic: On CI completion (if configured)

### Step 4: Test

**What you do:** Test your changes in the DEV workbench.

| Test Type | How |
|-----------|-----|
| **Manual testing** | Send signals via I/O Gateway |
| **Integration tests** | Hub Test Runner with Test CRDs |
| **End-to-end** | Complete Scenario execution |

```yaml
# Example: Invoke Scenario via I/O Gateway
POST /api/v1/signals/dispute.submitted
{
  "customer_id": "CUST-001",
  "amount": 500.00,
  "dispute_type": "unauthorized"
}
```

### Step 5: Request Promotion

**What you do:** Request promotion of your Scenario to production.

```yaml
apiVersion: hub.olympus.io/v1
kind: PromotionRequest
metadata:
  name: pr-dispute-v1.2.3
spec:
  source:
    workbench: dispute-ops-dev
    scenario: standard-dispute
    version: "1.2.3"
  
  destination:
    subscription: acme-prod
    workbench: dispute-ops-prod
  
  notes: "Added fraud detection logic for high-value disputes"
```

**What happens:**
- Request is logged with your identity
- Notifications sent to approvers
- Request enters pending state

### Step 6: Approval (Admin)

**What the admin does:** Reviews and approves your promotion request.

| Admin Checks | Questions |
|--------------|-----------|
| **Code review** | Has this been reviewed? |
| **Test results** | Did tests pass? |
| **Change description** | What's changing? |
| **Risk assessment** | Is this safe for production? |

**Result:** Approval recorded with:
- Who approved
- When approved
- Any comments

### Step 7: Artifacts Copied

**What happens automatically:**

```
ARTIFACT COPY PROCESS:

1. Container images
   Source: registry.hub.acme.com/dev-sub/.../dispute-handler:1.2.3
   Target: registry.hub.acme.com/prod-sub/.../dispute-handler:1.2.3
   Action: Physical copy

2. CRDs
   Source: dev-sub Git repo → scenarios/standard-dispute/
   Target: prod-sub Git repo → scenarios/standard-dispute/
   Action: Clone to target

3. Migrations (if any)
   Source: dev-sub Git repo → migrations/
   Target: prod-sub Git repo → migrations/
   Action: Clone and queue for execution
```

### Step 8: Live in Production

**What happens:**
- CRDs sync to PROD workbench
- Migrations execute (if any)
- New Scenario version is active
- Old version replaced

**Notifications sent to:**
- You (requester)
- Admin (approver)
- Ops team (stakeholders)

---

## Timing Expectations

| Step | Typical Duration |
|------|------------------|
| Develop | Variable (your work) |
| Build | 2-10 minutes |
| Sync to DEV | < 1 minute |
| Test | Variable (your testing) |
| Request promotion | Immediate |
| Approval | Minutes to hours (human) |
| Artifact copy | 1-5 minutes |
| PROD deployment | 1-5 minutes |

**Total from request to live:** Depends on approval speed (typically same-day for urgent changes).

---

## What If Something Goes Wrong?

### Build Failure

```
Symptom: Runtime CI fails
Action: Check build logs, fix code, rebuild
Impact: None — nothing has changed in workbench
```

### Test Failure

```
Symptom: Tests fail in DEV workbench
Action: Debug, fix, re-sync, re-test
Impact: Only DEV workbench affected
```

### Promotion Rejected

```
Symptom: Admin rejects promotion request
Action: Address feedback, make changes, re-request
Impact: PROD unchanged
```

### Production Issue

```
Symptom: Bug discovered in PROD after deployment
Action: Rollback to previous version
Impact: Reverts to last known good state
```

---

## Rollback

If issues are discovered in production:

```yaml
apiVersion: hub.olympus.io/v1
kind: RollbackRequest
metadata:
  name: rollback-dispute-001
spec:
  workbench: dispute-ops-prod
  scenario: standard-dispute
  target_version: "1.2.2"  # Previous version
  reason: "Critical bug in fraud detection logic"
```

**Rollback constraints:**
- Only to the **immediately previous version**
- Data store migrations are **not automatically reversed**
- Must be initiated by Admin

---

## Summary

| Phase | Actor | Action | Result |
|-------|-------|--------|--------|
| Develop | Developer | Edit CRDs, code | Changes in Git |
| Build | CI System | Compile, test | Container in snapshot registry |
| Sync | Developer | Push to workbench | Changes live in DEV |
| Test | Developer | Validate changes | Confidence in quality |
| Request | Developer | Submit promotion | Request in queue |
| Approve | Admin | Review, approve | Promotion authorized |
| Copy | System | Transfer artifacts | Artifacts in PROD subscription |
| Deploy | System | Sync to PROD | Changes live in PROD |

---

[← Previous: Workbench-Based Development](./03-workbench-based-development.md) | [Back to Index](./README.md) | [Next: Daily Workflow →](./05-daily-workflow.md)

