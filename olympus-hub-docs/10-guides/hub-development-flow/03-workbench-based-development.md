# Workbench-Based Development

[← Previous: Two-Subscription Model](./02-two-subscription-model.md) | [Back to Index](./README.md) | [Next: Development to Production →](./04-development-to-production-flow.md)

---

## What Is a Workbench?

A **Workbench** is a complete, isolated context for developing and running Hub Scenarios. Each workbench is tagged with a **Dev-Lifecycle-Stage** (DEV, STAGING, or PROD) indicating its purpose — distinct from **Hub Environment**, which is a business/operations domain concept for runtime configuration.

Think of it as:

| Analogy | Explanation |
|---------|-------------|
| **A development environment** | Has its own configurations, tools, machines |
| **A runtime container** | Scenarios actually run here for testing |
| **A promotion unit** | Can be promoted as a whole |
| **Your workspace** | Where you do your daily work |

---

## Remote Development Model

> **Important**: Hub development is entirely **remote**. There is no local development environment on your laptop.

You access your workbench via a **remote workspace** managed by Hub:

```bash
# On your laptop — open a remote workspace
hubdev login
hubdev workspace open dispute-ops-dev

# VS Code opens connected to remote workspace
# All hub commands run inside this workspace
```

| Where | CLI | What You Do |
|-------|-----|-------------|
| **Your laptop** | `hubdev` | Login, open/close workspaces, list instances |
| **Remote workspace** | `hub` | Validate, sync scenarios, view logs, monitor requests |

**Key Points:**
- All resources (specs, scripts, configs) live in a Hub-managed remote workspace backed by Git
- VS Code connects to this remote workspace (not local files)
- All `hub` CLI commands execute within the remote workspace context
- No "works on my machine" issues — everyone has the same environment

---

## Workbench vs Branch: The Key Difference

In Git, a branch is just a pointer to a set of commits. In Hub, a workbench is much more:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    BRANCH vs WORKBENCH                                       │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│   GIT BRANCH                           HUB WORKBENCH                         │
│   ──────────                           ─────────────                         │
│                                                                              │
│   ┌─────────────────┐                 ┌─────────────────────────────────┐   │
│   │                 │                 │                                 │   │
│   │  Pointer to     │                 │  Complete Environment           │   │
│   │  commits        │                 │  ├── Scenarios (running)        │   │
│   │                 │                 │  ├── Hub Applications           │   │
│   │  Just code      │                 │  ├── Tool instances             │   │
│   │  history        │                 │  ├── Machine connections        │   │
│   │                 │                 │  ├── Task queues                │   │
│   │                 │                 │  ├── Environment configs        │   │
│   │                 │                 │  └── Test data                  │   │
│   │                 │                 │                                 │   │
│   └─────────────────┘                 └─────────────────────────────────┘   │
│                                                                              │
│   Can't run code                      Can run and test scenarios            │
│   (needs CI/CD)                       (immediately)                         │
│                                                                              │
└──────────────────────────────────────────────────────────────────────────────┘
```

---

## Your DEV Workbench

When you join a Hub project, you'll typically have access to a DEV workbench:

### Workbench Structure

```
dispute-ops-dev/
├── workbench.yaml              # Workbench configuration
├── environments/
│   └── default.yaml            # Runtime environment settings
├── scenarios/
│   ├── standard-dispute/       # Your Scenario
│   │   ├── normative.yaml
│   │   ├── automation.yaml
│   │   └── deployment.yaml
│   └── fraud-detection/        # Another Scenario
├── applications/
│   └── dispute-handler/        # Hub Application code reference
├── task-queues/
│   └── tier-1-queue.yaml       # Task queue configuration
├── machines/
│   └── banking-core.yaml       # Machine instance binding
└── tools/
    └── email-sender.yaml       # Tool instance binding
```

### What You Can Do in Your Workbench

| Action | How |
|--------|-----|
| **Edit Scenarios** | Modify YAML files, commit to Git, sync scenario |
| **Build applications** | Trigger Runtime CI |
| **Run Scenarios** | Send signals via I/O Gateway |
| **Test end-to-end** | Use Hub Test Runner |
| **Debug** | Check logs in Olympus Watch |
| **Iterate quickly** | Commit → Sync → Test → Fix → Repeat |

---

## When to Create Additional Workbenches

Most of the time, **one DEV workbench is enough** for a small team. But sometimes you need more:

### Scenarios for Additional Workbenches

| Scenario | Solution |
|----------|----------|
| **Feature isolation** | Create a temporary feature workbench |
| **Parallel development** | Each developer gets their own workbench |
| **Experimental changes** | Create a sandbox workbench |
| **Long-running feature** | Dedicated workbench to avoid blocking others |

### Creating a Feature Workbench

```yaml
apiVersion: hub.olympus.io/v1
kind: Workbench
metadata:
  name: dispute-ops-dev-feature-x
  namespace: acme-bank
spec:
  display_name: "Dispute Ops - Feature X"
  dev_lifecycle_stage: DEV
  
  # Clone from existing workbench
  clone_from: dispute-ops-dev
  
  # Optionally limit who can access
  access:
    users:
      - developer-alice@acme.com
```

### Workbench Lifecycle

```
┌─────────────┐     ┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│   Create    │────▶│   Develop   │────▶│   Promote   │────▶│   Delete    │
│   Workbench │     │   & Test    │     │   Scenario  │     │   (if temp) │
└─────────────┘     └─────────────┘     └─────────────┘     └─────────────┘
```

---

## Single Workbench vs Multiple: Decision Guide

| Question | Single Workbench | Multiple Workbenches |
|----------|------------------|---------------------|
| Team size? | 1-2 developers | 3+ developers |
| Parallel features? | No | Yes |
| Blocking concerns? | Low | High |
| Duration of features? | Short (days) | Long (weeks) |
| Complexity preference? | Simple | Can handle more |

### Recommendation for Small Teams

```
RECOMMENDED SETUP:

DEV Subscription
├── dispute-ops-dev           ← Primary development (shared)
├── dispute-ops-dev-feature   ← Feature workbench (when needed)
└── dispute-ops-staging       ← Pre-prod validation
```

---

## Working in Your Workbench

### The Edit-Sync-Test Cycle

```bash
# 1. Open your workspace (on laptop)
hubdev workspace open dispute-ops-dev

# 2. In VS Code (remote workspace terminal)
# Edit files in the editor, then:

# 3. Commit and push to Git (GitOps requirement)
git add scenarios/standard-dispute/
git commit -m "feat: update standard-dispute scenario"
git push

# 4. Deploy to workbench instance (reads from Git)
hub sync scenario standard-dispute

# 5. Test and monitor
hub watch scenario-deployment standard-dispute-dev
hub logs agent my-agent-emp-001 --follow
hub metrics agent my-agent-emp-001
```

> **Note**: All `hub` commands operate on **committed Git files**, not the local filesystem. The workspace branch is associated with the workbench instance. The smallest unit of deployment is a **Scenario**.

**The Complete Cycle:**

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    DEVELOPMENT CYCLE                                         │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│   LAPTOP: hubdev workspace open ──▶ VS Code opens remote workspace           │
│                                                                              │
│   WORKSPACE:                                                                 │
│       ┌──────────┐                                                          │
│       │          │                                                          │
│       │  EDIT    │◀────────────────────────────────────────────┐            │
│       │  CRDs    │  (in VS Code editor)                        │            │
│       │          │                                             │            │
│       └────┬─────┘                                             │            │
│            │                                                   │            │
│            ▼                                                   │            │
│       ┌──────────┐                                             │            │
│       │          │                                             │            │
│       │  COMMIT  │  git add . && git commit && git push       │            │
│       │          │  (GitOps requirement)                      │            │
│       │          │                                             │            │
│       └────┬─────┘                                             │            │
│            │                                                   │            │
│            ▼                                                   │            │
│       ┌──────────┐                                             │            │
│       │          │                                             │            │
│       │  SYNC    │  hub sync scenario <name>                  │            │
│       │          │  (reads from Git)                           │            │
│       │          │                                             │            │
│       └────┬─────┘                                             │            │
│            │                                                   │            │
│            ▼                                                   │            │
│       ┌──────────┐         ┌──────────┐                        │            │
│       │          │ pass    │          │                        │            │
│       │  TEST    │────────▶│ PROMOTE  │  hub request-approval │            │
│       │          │         │          │  to STAGING/PROD       │            │
│       │  hub watch│        │          │                        │            │
│       │  hub logs │        │          │                        │            │
│       └────┬─────┘         └──────────┘                        │            │
│            │                                                   │            │
│            │ fail                                              │            │
│            └───────────────────────────────────────────────────┘            │
│                                                                              │
└──────────────────────────────────────────────────────────────────────────────┘
```

### Sync Permissions

| Workbench Stage | Can You Sync? |
|-----------------|---------------|
| **DEV** | ✅ Yes (by default) |
| **STAGING** | ❌ No (admin only) |
| **PROD** | ❌ No (via promotion only) |

---

## Workbench Isolation

Each workbench is isolated:

| Aspect | Isolation Level |
|--------|-----------------|
| **CRDs** | Separate folder in Git |
| **Running Scenarios** | Separate runtime |
| **Tool/Machine instances** | Workbench-specific bindings |
| **Environment variables** | Workbench-specific |
| **Task queues** | Workbench-specific |
| **Test data** | Workbench-specific |

### Why This Matters

- Changes in one workbench don't affect others
- You can break your DEV workbench without affecting the team
- Multiple developers can work in parallel workbenches
- Feature workbenches can be deleted without cleanup

---

## Summary

| Concept | Key Point |
|---------|-----------|
| **Workbench** | Complete environment, not just code |
| **DEV workbench** | Your primary development context |
| **Feature workbench** | Created when isolation is needed |
| **Sync** | Deploy scenario from committed Git files to workbench |
| **Isolation** | Workbenches don't affect each other |
| **GitOps** | All hub commands read from committed Git files |
| **Scenario** | Smallest unit of deployment |

---

## Related Documentation

- [CLI Channels for Developers](../../06-ux-architecture/tenant-domain/cli-channels-for-developers.md) — Full CLI command reference
- [Hub CLI Setup](../hub-cli-setup.md) — Installation guide

---

[← Previous: Two-Subscription Model](./02-two-subscription-model.md) | [Back to Index](./README.md) | [Next: Development to Production →](./04-development-to-production-flow.md)

