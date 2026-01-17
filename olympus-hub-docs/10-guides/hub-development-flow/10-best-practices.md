# Best Practices

[← Previous: Limitations](./09-limitations.md) | [Back to Index](./README.md)

---

## Overview

This document collects best practices for working effectively within Hub's development model.

---

## Workbench Management

### Naming Conventions

| Workbench Type | Naming Pattern | Example |
|----------------|----------------|---------|
| Primary DEV | `{project}-dev` | `dispute-ops-dev` |
| Developer-specific | `{project}-dev-{name}` | `dispute-ops-dev-alice` |
| Feature | `{project}-dev-{feature}` | `dispute-ops-dev-fraud-v2` |
| STAGING | `{project}-staging` | `dispute-ops-staging` |
| PROD | `{project}-prod` | `dispute-ops-prod` |

### When to Create a Feature Workbench

✅ **Create one when:**
- Feature will take > 1 week
- Changes will break existing functionality temporarily
- Multiple developers collaborating on same feature
- Experimental/uncertain direction

❌ **Don't create one when:**
- Quick bug fix (use primary DEV)
- Small enhancement (use primary DEV)
- You just want isolation "just in case"

> **Note:** Workbenches are cost-efficient (infrastructure scales to zero when idle) and persistent (state preserved), but there's still upfront creation overhead. Default to your primary DEV workbench unless you genuinely need isolation or persistent state for a feature.

### Workbench Lifecycle

```
1. Create       Keep it minimal — clone from existing
2. Develop      Do your work, sync frequently
3. Test         Validate before promoting
4. Promote      Move to STAGING/PROD
5. Clean up     Delete feature workbenches when done
```

---

## CLI Workflow Best Practices

### Use hubdev for Workspace Management

```bash
# Good: Use hubdev to open workspace
hubdev workspace open dispute-ops-dev --branch feature/x

# Bad: Trying to clone repo locally (not supported)
git clone https://... # ❌ This won't work — all development is remote
```

### Use hub for All Development Operations

```bash
# Good: Use hub commands in workspace (after committing to Git)
git add .
git commit -m "feat: update scenario"
git push
hub sync scenario my-scenario
hub watch request REQ-2026-01-11-00042

# Avoid: Using raw kubectl or API calls (unless advanced use case)
# The hub CLI provides the right abstractions
```

### Monitor with hub watch

```bash
# Watch a specific request through its lifecycle
hub watch request REQ-2026-01-11-00042

# Watch all requests in a scenario
hub watch scenario-deployment my-scenario-dev

# Append to log file for analysis
hub watch scenario-deployment my-scenario-dev >> scenario-monitor.log
```

### Context Awareness

```bash
# Always verify your context before operations
hub context

# Output shows:
# Workbench: dispute-ops
# Instance: dispute-ops-dev
# Branch: main
# User: developer@acme.bank
```

---

## GitOps Best Practices

### Always Commit Before Sync

**Critical Rule**: All `hub` commands operate on **committed Git files**, not the local filesystem. This ensures:
- Complete audit trail in Git history
- Branch-based isolation
- Reproducible deployments
- 100% GitOps compliance

**Workflow**:
```bash
# 1. Edit files in VS Code
# 2. Commit to Git (required)
git add .
git commit -m "feat: update scenario"
git push

# 3. Then sync (reads from Git)
hub sync scenario my-scenario
```

### Branch Alignment: Always Verify Before Sync

```bash
# Always check branch alignment before sync
hub context  # Shows current branch, workbench branch, and alignment status

# If branch mismatch, fix before syncing:
hub branch main  # Switch to workbench branch
git pull
hub sync scenario my-scenario
```

### Scenario-Based Deployment: Smallest Unit of Change

- **Smallest unit of deployment is Scenario**, not individual files
- Always sync entire scenarios: `hub sync scenario <name>`
- Use `hub validate scenario <name>` for validation-only operations
- Keep scenario files and referenced resources committed together

## Git Practices

### Commit Messages

Use meaningful, structured messages:

```
Format:
[{workbench}/{scenario}] {type}: {description}

Types:
├── feat:     New feature
├── fix:      Bug fix
├── refactor: Code restructuring
├── docs:     Documentation
├── test:     Test additions
└── chore:    Maintenance tasks

Examples:
[dispute-ops-dev/standard-dispute] feat: add tier-2 routing for high-value
[dispute-ops-dev/fraud-detection] fix: handle null customer name
[_shared/tool-definitions] add: payment validation tool
```

### Push Frequency

| Situation | Recommendation |
|-----------|----------------|
| Active development | Push after each logical unit |
| Shared workbench | Push frequently (avoid stale conflicts) |
| End of day | Always push (don't lose work) |
| **Before sync** | **Always commit and push first (GitOps requirement)** |

### Pull Before Work

```bash
# Start of every work session
git pull

# Before any sync operation
git pull
```

### Handling Validation Errors

**Branch Mismatch Error**:
```bash
# Check alignment
hub context

# Fix: Switch to workbench branch
hub branch main
git pull
hub sync scenario my-scenario
```

**Dirty Files Error**:
```bash
# Check for uncommitted changes
git status

# Fix: Commit changes
git add .
git commit -m "feat: my changes"
git push
hub sync scenario my-scenario
```

### Audit Log Awareness: All Actions Are Logged

- All `hub` commands create audit log entries with Git SHA references
- View audit logs: `hub audit log`
- Every change is traceable to a specific Git commit
- Non-repudiation guaranteed through Git SHA in audit logs

---

## Scenario Development

### Structure Your Scenarios Well

```
scenarios/
└── standard-dispute/
    ├── normative.yaml       # WHAT should happen
    ├── automation.yaml      # HOW it's automated
    ├── deployment.yaml      # WHERE it runs
    ├── triggers/
    │   └── dispute-*.yaml   # Signal triggers
    ├── notifications/
    │   └── templates.yaml   # Notification templates
    ├── tests/
    │   ├── happy-path.yaml  # Happy path tests
    │   └── edge-cases.yaml  # Edge case tests
    └── migrations/
        └── v*.yaml          # Data migrations
```

### Version Your Specifications

```yaml
# In each specification
metadata:
  name: standard-dispute
  labels:
    version: "1.2.3"
spec:
  version: "1.2.3"  # Explicit version
  # ...
```

---

## Testing

### Minimum Test Coverage

| Scenario Complexity | Recommended Tests |
|--------------------|-------------------|
| Simple | 1 happy path, 1 error case |
| Medium | 3-5 tests covering main paths |
| Complex | 10+ tests with edge cases |

### Test Independence

Each test should:
- Set up its own data (or use pre-flight)
- Not depend on side effects from other tests
- Clean up after itself (or use post-flight)

```yaml
spec:
  setup:
    reset_environment: true
    seed_data:
      enabled: true
  # ...
  teardown:
    cleanup_test_data: true
```

### Test Naming

```yaml
# Good: Descriptive, action-oriented
name: create-dispute-high-value-routes-to-tier2

# Bad: Vague
name: test1
name: dispute-test
```

---

## Promotion Practices

### Before Requesting Promotion

| Checklist | Status |
|-----------|--------|
| All tests passing | ☐ |
| Synced to workbench | ☐ |
| Manually tested key flows | ☐ |
| Version updated | ☐ |
| Meaningful promotion notes | ☐ |

### Promotion Notes

Write useful notes for the approver:

```yaml
# Good
notes: |
  - Added fraud detection for disputes > $5000
  - Tested with 50 sample disputes
  - Related ticket: JIRA-1234

# Bad
notes: "Ready"
```

### Timing Promotions

| Situation | Recommendation |
|-----------|----------------|
| Normal changes | Request before EOD for next-day review |
| Urgent fixes | Contact approver directly |
| Friday afternoon | Consider waiting until Monday |
| Blocking someone | Communicate urgency |

---

## Collaboration

### Communication

| Event | Who to Notify |
|-------|---------------|
| Starting work on Scenario | Team (if shared workbench) |
| Breaking change incoming | All affected developers |
| Promotion requested | Approver(s) |
| Promotion completed | Stakeholders |

### Shared Workbench Etiquette

```
DO:
├── Pull before starting work
├── Push frequently
├── Communicate what you're working on
├── Keep changes focused
└── Don't break shared resources

DON'T:
├── Leave uncommitted changes overnight
├── Make sweeping changes without warning
├── Assume no one else is working
└── Sync without testing first
```

---

## Performance

### Keep Containers Lean

```dockerfile
# Good: Multi-stage build, minimal final image
FROM maven:3.8 AS build
COPY . .
RUN mvn package

FROM eclipse-temurin:17-jre-alpine
COPY --from=build /app/target/app.jar /app/
CMD ["java", "-jar", "/app/app.jar"]

# Bad: Everything in one layer
FROM ubuntu:latest
RUN apt-get update && apt-get install -y maven openjdk-17-jdk
COPY . .
RUN mvn package
CMD ["java", "-jar", "target/app.jar"]
```

### Sync Efficiently

- Don't sync after every tiny change
- Batch related changes into logical units
- **Always commit and push before syncing** (GitOps requirement)
- Sync when ready to test
- Understand what gets synced: all resources in scenario (atomic deployment)

---

## Troubleshooting Tips

### Common Issues and Fixes

| Issue | Likely Cause | Fix |
|-------|--------------|-----|
| Sync fails - Branch mismatch | Current branch ≠ workbench branch | `hub branch main && git pull` |
| Sync fails - Dirty files | Uncommitted changes | `git add . && git commit && git push` |
| Sync fails | CRD validation error | Check YAML syntax, references |
| Build fails | Code error | Check build logs |
| Test fails unexpectedly | Stale state | Reset test environment |
| Promotion stuck | Awaiting approval | Contact approver |
| Can't access workbench | Permissions | Check with Admin |

### Getting Help

```
1. Check error messages carefully
2. Review logs with hub commands:
   - hub logs agent <name> --tail 100
   - hub events --all
   - hub watch scenario-deployment <name>
3. Check documentation (this guide!)
4. Ask team members
5. Contact support with specifics
```

---

## Quick Reference Card

### Daily Checklist

```
[ ] Pull latest changes
[ ] Check workbench status (hub context)
[ ] Edit → Commit → Push → Sync → Test
[ ] Commit with meaningful message (before sync)
[ ] Push before leaving
[ ] Request pending promotions
```

### Key Commands

#### Workspace Access (hubdev — on laptop)
| Action | Command |
|--------|---------|
| Login | `hubdev login` |
| List workspaces | `hubdev workspace list` |
| Open workspace | `hubdev workspace open <instance>` |

#### Development (hub — in workspace)
| Action | Command |
|--------|---------|
| Validate scenario | `hub validate scenario <name>` |
| Validate file | `hub validate -f <file>` |
| Sync scenario | `hub sync scenario <name>` |
| View logs | `hub logs agent <name> --follow` |
| Watch request | `hub watch request <id>` |
| Watch scenario | `hub watch scenario-deployment <name>` |
| View audit log | `hub audit log` |
| Request approval | `hub request-approval scenario-deployment <name>` |

#### Git (in workspace)
| Action | Command |
|--------|---------|
| Pull | `git pull` |
| Push | `git push` |
| Branch | `hub branch` |

---

## Summary

| Area | Key Practice |
|------|--------------|
| **Workbenches** | Name clearly, create sparingly, clean up |
| **GitOps** | Always commit before sync, verify branch alignment |
| **Git** | Pull first, push often, meaningful commits |
| **Scenarios** | Structure well, version explicitly, sync entire scenario |
| **Testing** | Cover key paths, independent tests |
| **Promotion** | Check everything, write good notes |
| **Collaboration** | Communicate, respect shared spaces |
| **Audit Logs** | All actions logged with Git SHA for non-repudiation |

---

## Related Documentation

- [CLI Channels for Developers](../../06-ux-architecture/tenant-domain/cli-channels-for-developers.md) — Full CLI command reference
- [Hub CLI Setup](../hub-cli-setup.md) — Installation guide

---

[← Previous: Limitations](./09-limitations.md) | [Back to Index](./README.md)

