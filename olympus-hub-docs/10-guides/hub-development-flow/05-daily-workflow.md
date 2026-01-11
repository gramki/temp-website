# Daily Workflow

[← Previous: Dev to Prod Flow](./04-development-to-production-flow.md) | [Back to Index](./README.md) | [Next: Collaboration Patterns →](./06-collaboration-patterns.md)

---

## A Day in the Life of a Hub Developer

This document describes typical day-to-day activities when developing on Hub.

---

## Morning: Starting Your Day

### 1. Open Your Workspace

```bash
# On your laptop
hubdev login                          # If not already logged in
hubdev workspace open dispute-ops-dev  # Opens VS Code to remote workspace
```

### 2. Check Status (In Workspace Terminal)

```bash
# Check recent deployments
hub get scenario-deployment

# Check any agent issues
hub health --all

# View recent events
hub events --all

# Check current context
hub context
```

### 3. Sync Latest Changes (If Shared Workbench)

If working in a shared DEV workbench:

```bash
# In remote workspace — pull latest from Git
hub branch                    # Check current branch
git pull                     # Pull latest (standard git)

# Check what changed
git log --oneline -5
```

> **Terminology Clarification:**  
> - **Git pull/push** = Moving CRD files in the remote workspace Git repository  
> - **hub sync scenario** = Deploying scenario from committed Git files to the running workbench instance
> 
> **GitOps Pattern**: All `hub` commands read from **committed Git files**, not the local filesystem. Always `git commit` and `git push` before `hub sync scenario`.

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
│       │  COMMIT  │  2. Commit and push to Git (GitOps requirement)         │
│       └────┬─────┘                                                          │
│            │                                                                 │
│            ▼                                                                 │
│       ┌──────────┐                                                          │
│       │  BUILD   │  3. Trigger Runtime CI (if code changes)                 │
│       └────┬─────┘                                                          │
│            │                                                                 │
│            ▼                                                                 │
│       ┌──────────┐                                                          │
│       │  SYNC    │  4. Sync scenario to DEV workbench                       │
│       └────┬─────┘                                                          │
│            │                                                                 │
│            ▼                                                                 │
│       ┌──────────┐                                                          │
│       │  TEST    │  5. Test your changes                                    │
│       └────┬─────┘                                                          │
│            │                                                                 │
│            ├─── Works? ───▶ Continue or request promotion                   │
│            │                                                                 │
│            └─── Broken? ──▶ Back to EDIT                                    │
│                                                                              │
└──────────────────────────────────────────────────────────────────────────────┘
```

> **Understanding GitOps: Why Commit First?**
> 
> Hub commands operate on **committed Git files only**, not your local filesystem. This ensures:
> - Complete audit trail in Git history
> - Branch-based isolation
> - Reproducible deployments
> - 100% GitOps compliance
> 
> **Workflow**: Always `git commit` and `git push` before `hub sync scenario`.

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
# 2. Commit and push to Git (GitOps requirement)
git add triggers/dispute-submitted.yaml
git commit -m "[dispute-ops-dev/standard-dispute] feat: add high-value routing"
git push

# 3. Sync scenario (reads from Git)
hub sync scenario standard-dispute

# 4. Test the change
hub watch scenario-deployment standard-dispute-dev
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
# 2. Commit and push code changes (GitOps requirement)
git add applications/dispute-handler/
git commit -m "[dispute-ops-dev] fix: handle null customer name"
git push

# 3. Trigger Runtime CI (in remote workspace)
hub build application dispute-handler
hub get build dispute-handler --watch

# 4. Sync scenario (picks up new container version from Git)
hub sync scenario standard-dispute

# 5. Test the fix
hub watch request REQ-2026-01-11-00042
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

### Workspace Access (hubdev — on your laptop)

```bash
hubdev login                              # Authenticate
hubdev workspace list                     # List available instances
hubdev workspace open dispute-ops-dev     # Open workspace
hubdev workspace open dispute-ops-dev --branch feature/x  # Specific branch
```

### Development (hub — in remote workspace)

```bash
# Validate (optional, before committing)
hub validate scenario standard-dispute
hub validate -f scenarios/standard-dispute/automation.yaml

# Commit and push (GitOps requirement)
git add .
git commit -m "[workbench/scenario] type: description"
git push

# Deploy (reads from Git)
hub sync scenario standard-dispute        # Deploy scenario
hub sync scenario standard-dispute --wait # Wait for completion

# Monitor
hub logs agent my-agent-emp-001 --follow
hub metrics agent my-agent-emp-001
hub watch request REQ-2026-01-11-00042    # Watch specific request
hub watch scenario-deployment standard-dispute-dev  # Watch all requests

# Validate & Publish
hub validate training-spec my-agent-v1 --workbench dispute-ops-dev
hub publish training-spec my-agent-v1 --version 1.0.0
```

### Git Operations (in remote workspace)

```bash
hub branch                     # List/switch branches
hub branch feature/new --new   # Create new branch
git pull                       # Pull latest
git status                     # Check status
git add .                      # Stage changes
git commit -m "[workbench/scenario] type: description"
git push                       # Push to remote
```

### Developer Console Actions (Alternative to CLI)

| Action | Console Path | CLI Equivalent |
|--------|--------------|----------------|
| Validate scenario | — | `hub validate scenario <name>` |
| Sync workbench | Workbench → Sync | `hub sync scenario <name>` |
| View logs | Workbench → Logs | `hub logs agent <name>` |
| Run tests | Test Runner → Run | `hub validate training-spec <name>` |
| Request promotion | Workbench → Promote | `hub request-approval scenario-deployment <name>` |

> **Note**: All changes must be committed to Git before syncing. Use `git commit` and `git push` in the workspace terminal, then sync via console or CLI.

---

## Troubleshooting Common Issues

### "Sync failed"

```
Possible causes:
├── Branch mismatch → Check hub context, switch to workbench branch
├── Dirty files → Commit or stash uncommitted changes
├── CRD validation error → Check YAML syntax
├── Reference missing → Ensure referenced resources exist
├── Permission denied → Check your workbench access
└── Version conflict → Pull latest, resolve, retry
```

### "Branch Mismatch Error"

```
❌ ERROR: Branch Mismatch
   Current git branch: feature/new-trigger
   Workbench instance branch: main

To fix:
├── Switch to workbench branch: hub branch main && git pull
├── Request new workbench instance for your branch (contact Tenant Admin)
└── Update workbench instance branch (requires admin/authorized dev)
```

### "Dirty Files Error"

```
❌ ERROR: Dirty Files Detected
   Scenario files have uncommitted local changes

To fix:
├── Commit changes: git add . && git commit -m "message" && git push
├── Stash changes: git stash && hub sync scenario <name> && git stash pop
└── Discard changes: git checkout <files>
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

## Related Documentation

- [CLI Channels for Developers](../../06-ux-architecture/tenant-domain/cli-channels-for-developers.md) — Full CLI command reference
- [Hub CLI Setup](../hub-cli-setup.md) — Installation guide

---

[← Previous: Dev to Prod Flow](./04-development-to-production-flow.md) | [Back to Index](./README.md) | [Next: Collaboration Patterns →](./06-collaboration-patterns.md)

