# Collaboration Patterns

[← Previous: Daily Workflow](./05-daily-workflow.md) | [Back to Index](./README.md) | [Next: CI/CD Integration →](./07-ci-cd-integration.md)

---

## Working in Small Teams

Hub is designed for small teams (2-5 developers). This document describes collaboration patterns that work well in this context.

---

## Workbench Instance Model: One Instance Per Developer

**Critical Understanding**: A workbench instance can only have **one branch associated** and **one workspace**. Multiple developers working on the same Workbench Specification must create **separate workbench instances**, each mapped to their own branch.

### How It Works

| Scenario | Solution |
|----------|----------|
| **1 developer** working on `main` branch | 1 workbench instance (`dispute-ops-dev`) → `main` branch |
| **3 developers** working on same Workbench Specification | 3 workbench instances:<br>- `dispute-ops-dev-alice` → `feature/alice-trigger`<br>- `dispute-ops-dev-bob` → `feature/bob-ui`<br>- `dispute-ops-dev-charlie` → `main` |
| **Developer switches branches** | Must either:<br>- Switch workbench instance branch (admin/authorized dev)<br>- Use different workbench instance for new branch<br>- Switch to existing workbench instance for that branch |

### Creating Workbench Instances

**For New Developers**:
1. Contact Tenant Admin to request a workbench instance
2. Specify:
   - Workbench Specification name (e.g., `dispute-ops`)
   - Your branch name (e.g., `feature/my-feature`)
   - Your user identity

**For Branch Switching**:
- Option 1: Request new workbench instance for new branch
- Option 2: Have admin/authorized dev update existing instance's branch association
- Option 3: Use existing workbench instance if one exists for your branch

### Best Practices

- **One branch per workbench instance**: Never try to use one instance for multiple branches
- **Coordinate with team**: Check if workbench instance exists for your branch before requesting new one
- **Clean up**: Request deletion of unused workbench instances when done

---

## Pattern 1: Single Developer

**Scenario:** You're the only developer on a Hub project.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    SINGLE DEVELOPER SETUP                                    │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│   DEV SUBSCRIPTION                       PROD SUBSCRIPTION                   │
│   ┌─────────────────────────┐           ┌─────────────────────────┐         │
│   │                         │           │                         │         │
│   │  dispute-ops-dev  (YOU) │  ──────▶  │  dispute-ops-prod       │         │
│   │                         │  Promote  │                         │         │
│   │                         │           │                         │         │
│   └─────────────────────────┘           └─────────────────────────┘         │
│                                                                              │
└──────────────────────────────────────────────────────────────────────────────┘
```

**Workflow:**
1. Work directly in your DEV workbench
2. No coordination needed
3. Request promotion when ready
4. Admin (might be you) approves

**Advantages:**
- Simple, no coordination overhead
- Fast iteration
- One workbench to manage

---

## Pattern 2: Two Developers, Shared Workbench

**Scenario:** Two developers working on the same project, mostly on different Scenarios.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    SHARED WORKBENCH                                          │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│   DEV SUBSCRIPTION                                                           │
│   ┌─────────────────────────────────────────────────────────────────────┐   │
│   │                                                                      │   │
│   │   dispute-ops-dev (SHARED)                                           │   │
│   │   ┌────────────────────────────────────────────────────────────┐    │   │
│   │   │                                                             │    │   │
│   │   │   Scenario A          Scenario B          Scenario C        │    │   │
│   │   │   (Alice)             (Bob)               (Either)          │    │   │
│   │   │                                                             │    │   │
│   │   └────────────────────────────────────────────────────────────┘    │   │
│   │                                                                      │   │
│   └─────────────────────────────────────────────────────────────────────┘   │
│                                                                              │
│   COORDINATION:                                                              │
│   • Communicate: "I'm working on Scenario A"                                 │
│   • Pull before making changes                                               │
│   • Push frequently to avoid conflicts                                       │
│                                                                              │
└──────────────────────────────────────────────────────────────────────────────┘
```

**When to use:**
- Developers work on different Scenarios
- Changes don't overlap often
- Quick informal coordination is easy

**Coordination practices:**
| Practice | How |
|----------|-----|
| **Claim work** | "I'm working on Scenario X today" |
| **Pull often** | Before starting any work |
| **Push promptly** | After completing a logical unit |
| **Communicate blocks** | "Don't touch Scenario X until I'm done" |

---

## Pattern 3: Two Developers, Separate Workbenches

**Scenario:** Two developers who need isolation, or work on overlapping code.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    SEPARATE WORKBENCHES                                      │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│   DEV SUBSCRIPTION                                                           │
│   ┌─────────────────────────────────────────────────────────────────────┐   │
│   │                                                                      │   │
│   │   dispute-ops-dev-alice        dispute-ops-dev-bob                   │   │
│   │   ┌─────────────────────┐     ┌─────────────────────┐               │   │
│   │   │                     │     │                     │               │   │
│   │   │  Alice's changes    │     │  Bob's changes      │               │   │
│   │   │                     │     │                     │               │   │
│   │   └──────────┬──────────┘     └──────────┬──────────┘               │   │
│   │              │                           │                           │   │
│   │              │     ┌─────────────────────┘                           │   │
│   │              │     │                                                 │   │
│   │              ▼     ▼                                                 │   │
│   │         dispute-ops-staging                                          │   │
│   │         (Integration point)                                          │   │
│   │                                                                      │   │
│   └─────────────────────────────────────────────────────────────────────┘   │
│                                                                              │
└──────────────────────────────────────────────────────────────────────────────┘
```

**When to use:**
- Developers modify the same Scenario
- Need to experiment without affecting others
- Longer-running features
- Prefer isolation over coordination

**Workflow:**
1. Each developer has their own DEV workbench
2. Develop independently
3. Promote to STAGING for integration
4. Resolve any issues in STAGING
5. Promote from STAGING to PROD

---

## Pattern 4: Feature Workbench

**Scenario:** A significant feature that needs isolation, regardless of team size.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    FEATURE WORKBENCH                                         │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│   DEV SUBSCRIPTION                                                           │
│   ┌─────────────────────────────────────────────────────────────────────┐   │
│   │                                                                      │   │
│   │   dispute-ops-dev (main)       dispute-ops-dev-feature-x             │   │
│   │   ┌─────────────────────┐     ┌─────────────────────────────────┐   │   │
│   │   │                     │     │                                  │   │   │
│   │   │  Stable development │     │  Feature X development          │   │   │
│   │   │  Bug fixes          │     │  ├── May break things           │   │   │
│   │   │  Small changes      │     │  ├── Experimental               │   │   │
│   │   │                     │     │  └── Isolated from main         │   │   │
│   │   │                     │     │                                  │   │   │
│   │   └─────────────────────┘     └───────────────┬─────────────────┘   │   │
│   │              │                                │                      │   │
│   │              │                                │ When feature complete│   │
│   │              │                                │                      │   │
│   │              │                    ┌───────────┘                      │   │
│   │              ▼                    ▼                                  │   │
│   │         dispute-ops-staging                                          │   │
│   │                                                                      │   │
│   └─────────────────────────────────────────────────────────────────────┘   │
│                                                                              │
└──────────────────────────────────────────────────────────────────────────────┘
```

**When to create a feature workbench:**

| Criterion | Create Feature Workbench |
|-----------|-------------------------|
| Duration > 1 week | ✅ Yes |
| Breaks existing functionality | ✅ Yes |
| Experimental/uncertain | ✅ Yes |
| Multiple developers on feature | ✅ Yes |
| Quick bug fix | ❌ No |
| Small enhancement | ❌ No |

**Feature workbench lifecycle:**
1. **Create** — Clone from main DEV workbench
2. **Develop** — Work in isolation
3. **Test** — Validate in feature workbench
4. **Integrate** — Promote to STAGING
5. **Delete** — Remove feature workbench (optional)

---

## Coordination Mechanisms

### Communication

| Tool | Use For |
|------|---------|
| **Slack/Teams** | Quick coordination, "working on X" |
| **Promotion notes** | Documenting what changed |
| **Workbench naming** | Indicates purpose: `-feature-x`, `-alice` |

### Git Practices

```bash
# Meaningful commit messages
git commit -m "[dispute-ops-dev/standard-dispute] feat: add tier-2 routing"

# Frequent pushes (GitOps requirement)
git push  # After each logical unit, before syncing

# Pull before work
git pull  # Start of each session

# Always commit before sync (GitOps pattern)
git add .
git commit -m "feat: update scenario"
git push
hub sync scenario standard-dispute  # Reads from Git
```

### Hub CLI Commands for Coordination

```bash
# Check your context (branch, workbench, alignment)
hub context

# Verify branch alignment before syncing
hub context  # Shows branch alignment status

# View recent changes
hub get scenario-deployment --watch

# Monitor team's work
hub watch scenario-deployment standard-dispute-dev
```

### Scenario Ownership

For larger teams, consider informal ownership:

| Scenario | Owner |
|----------|-------|
| standard-dispute | Alice |
| fraud-detection | Bob |
| chargeback | Alice (backup: Bob) |

---

## Handling Conflicts

### Conflict Type 1: Same Scenario, Different Changes

**Situation:** Alice and Bob both changed the same Scenario.

**Resolution:**
```
Option A: Sequential
├── Alice promotes first
├── Bob reviews Alice's changes
└── Bob adapts and promotes second

Option B: Separate workbenches
├── Alice in dispute-ops-dev-alice
├── Bob in dispute-ops-dev-bob
└── Both promote to STAGING for integration
```

### Conflict Type 2: Shared Resources

**Situation:** Both need to modify a shared tool binding.

**Resolution:**
```
Coordination required:
├── Discuss the change
├── One person makes the change
└── Both verify it works for their Scenarios
```

---

## Choosing a Pattern

| Team Size | Overlap | Recommended Pattern |
|-----------|---------|---------------------|
| 1 | N/A | Single developer, one workbench |
| 2 | Low | Shared workbench |
| 2 | High | Separate workbenches |
| 3-5 | Low | Shared workbench + occasional feature workbenches |
| 3-5 | High | Developer workbenches + STAGING integration |

---

## Summary

| Pattern | Best For |
|---------|----------|
| **Single developer** | Solo projects |
| **Shared workbench** | Small teams, low overlap |
| **Separate workbenches** | Parallel development, high overlap |
| **Feature workbench** | Large features, experiments |

---

[← Previous: Daily Workflow](./05-daily-workflow.md) | [Back to Index](./README.md) | [Next: CI/CD Integration →](./07-ci-cd-integration.md)

