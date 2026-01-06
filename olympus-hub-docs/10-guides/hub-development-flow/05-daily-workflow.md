# Daily Workflow

[← Previous: Dev to Prod Flow](./04-development-to-production-flow.md) | [Back to Index](./README.md) | [Next: Collaboration Patterns →](./06-collaboration-patterns.md)

---

## A Day in the Life of a Hub Developer

This document describes typical day-to-day activities when developing on Hub.

---

## Morning: Starting Your Day

### 1. Check Workbench Status

```
Developer Console → Your Workbench → Status

What to check:
├── Any failed deployments overnight?
├── Test results from scheduled runs?
├── Notifications from team?
└── Pending promotion requests?
```

### 2. Sync Latest Changes (If Shared Workbench)

If working in a shared DEV workbench:

```bash
# Pull latest CRDs from Git
cd subscription-repo/workbenches/dispute-ops-dev
git pull

# Check what changed
git log --oneline -5
```

> **Terminology Clarification:**  
> - **Git pull/push** = Moving CRD files between your local machine and the Git repository  
> - **Workbench Sync** = Applying CRD changes from Git to the running workbench (via Developer Console or API)

---

## Working on a Feature

### The Development Loop

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    DEVELOPMENT LOOP                                          │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│       ┌──────────┐                                                          │
│       │  EDIT    │  1. Make changes to CRDs or code                         │
│       └────┬─────┘                                                          │
│            │                                                                 │
│            ▼                                                                 │
│       ┌──────────┐                                                          │
│       │  BUILD   │  2. Trigger Runtime CI (if code changes)                 │
│       └────┬─────┘                                                          │
│            │                                                                 │
│            ▼                                                                 │
│       ┌──────────┐                                                          │
│       │  SYNC    │  3. Sync changes to DEV workbench                        │
│       └────┬─────┘                                                          │
│            │                                                                 │
│            ▼                                                                 │
│       ┌──────────┐                                                          │
│       │  TEST    │  4. Test your changes                                    │
│       └────┬─────┘                                                          │
│            │                                                                 │
│            ├─── Works? ───▶ Continue or request promotion                   │
│            │                                                                 │
│            └─── Broken? ──▶ Back to EDIT                                    │
│                                                                              │
└──────────────────────────────────────────────────────────────────────────────┘
```

---

## Common Tasks

### Task: Modify a Scenario

**Scenario:** You need to add a new trigger condition.

```yaml
# 1. Edit the trigger definition
# File: scenarios/standard-dispute/triggers/dispute-submitted.yaml

apiVersion: hub.olympus.io/v1
kind: Trigger
metadata:
  name: dispute-submitted
spec:
  signal_type: dispute.submitted
  
  # NEW: Add condition for high-value disputes
  conditions:
    - field: "$.amount"
      operator: greater_than
      value: 1000
      action: route_to_tier2
```

```bash
# 2. Commit and push to Git
git add triggers/dispute-submitted.yaml
git commit -m "[dispute-ops-dev/standard-dispute] feat: add high-value routing"
git push

# 3. Sync to workbench (via UI or API)
# Developer Console → Sync → Confirm

# 4. Test the change
# Send a test signal with amount > 1000
```

### Task: Update Hub Application Code

**Scenario:** You need to fix a bug in your Hub Application.

```python
# 1. Edit the application code
# File: applications/dispute-handler/src/handler.py

def process_dispute(dispute):
    # FIX: Handle null customer name
    customer_name = dispute.get('customer_name', 'Unknown')
    ...
```

```bash
# 2. Trigger Runtime CI
# Developer Console → Applications → dispute-handler → Build

# 3. Wait for build completion
# Build logs available in console

# 4. Sync workbench (picks up new container version)
# Developer Console → Sync → Confirm

# 5. Test the fix
# Send test signal that previously failed
```

### Task: Add a New Tool Binding

**Scenario:** You need to connect to a new external service.

```yaml
# 1. Create tool instance
# File: tools/payment-validator.yaml

apiVersion: hub.olympus.io/v1
kind: ToolInstance
metadata:
  name: payment-validator
spec:
  definition_ref: payment-validator-def  # From _shared
  
  endpoint:
    type: http
    url: https://payment-api.internal.acme.com/validate
  
  auth:
    type: bearer
    token_ref: payment-api-token
```

```bash
# 2. Commit, push, sync (same pattern)
```

---

## Testing Your Changes

### Quick Manual Test

```bash
# Send a test signal via curl
curl -X POST https://io-gateway.hub.acme.com/api/v1/signals/dispute.submitted \
  -H "Authorization: Bearer $DEV_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "customer_id": "TEST-001",
    "amount": 500.00,
    "dispute_type": "unauthorized"
  }'
```

### Using Hub Test Runner

```yaml
# 1. Define a test
# File: scenarios/standard-dispute/tests/happy-path.yaml

apiVersion: hub.olympus.io/v1
kind: Test
metadata:
  name: create-dispute-happy-path
spec:
  type: scenario_integration
  target:
    scenario: standard-dispute
    signal_type: dispute.submitted
  request:
    payload:
      customer_id: "TEST-001"
      amount: 500.00
  expectations:
    response:
      status_code: 200
```

```bash
# 2. Run the test
# Developer Console → Test Runner → Run Test
```

---

## End of Day: Wrapping Up

### Before You Leave

| Action | Why |
|--------|-----|
| **Commit all changes** | Don't lose work |
| **Push to Git** | Team can see your progress |
| **Note any blockers** | For tomorrow or team |
| **Check pending items** | Any approvals you're waiting on? |

### If Promotion Ready

```
Request promotion before leaving:
├── Ensures admin can review overnight
├── Reduces your wait time tomorrow
└── Gets changes to production faster
```

---

## Quick Reference: Common Commands

### Git Operations

```bash
# Pull latest
git pull

# Check status
git status

# Commit changes
git add .
git commit -m "[workbench/scenario] type: description"

# Push
git push
```

### Developer Console Actions

| Action | Path |
|--------|------|
| Sync workbench | Workbench → Sync |
| Trigger build | Applications → [App] → Build |
| View logs | Workbench → Logs |
| Run tests | Test Runner → Run |
| Request promotion | Workbench → Promote |

---

## Troubleshooting Common Issues

### "Sync failed"

```
Possible causes:
├── CRD validation error → Check YAML syntax
├── Reference missing → Ensure referenced resources exist
├── Permission denied → Check your workbench access
└── Version conflict → Pull latest, resolve, retry
```

### "Build failed"

```
Possible causes:
├── Compilation error → Check build logs
├── Test failure → Fix failing tests
├── Dependency issue → Check package versions
└── Timeout → Check for infinite loops or slow operations
```

### "Test not finding my changes"

```
Possible causes:
├── Forgot to sync → Sync workbench first
├── Wrong workbench → Confirm you're testing the right one
├── Cached state → Clear test environment
└── Wrong version → Check deployed version matches expected
```

---

## Summary

| Time | Activity |
|------|----------|
| **Morning** | Check status, pull latest |
| **Development** | Edit → Build → Sync → Test loop |
| **Testing** | Manual tests, Hub Test Runner |
| **End of day** | Commit, push, request promotions |

---

[← Previous: Dev to Prod Flow](./04-development-to-production-flow.md) | [Back to Index](./README.md) | [Next: Collaboration Patterns →](./06-collaboration-patterns.md)

