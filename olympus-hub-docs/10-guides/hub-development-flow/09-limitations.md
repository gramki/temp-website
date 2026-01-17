# Limitations and Trade-offs

[← Previous: Merits](./08-merits.md) | [Back to Index](./README.md) | [Next: Best Practices →](./10-best-practices.md)

---

## Honest Assessment

Every design involves trade-offs. This document honestly describes the limitations of Hub's development model and who might find them challenging.

---

## 1. Different Integration Model (Not a Limitation, But a Paradigm Difference)

### What This Means

- You cannot create feature branches within a workbench's Git repository
- No git-flow, trunk-based development, or similar branching strategies
- Concurrent development requires separate workbenches
- Each subscription has a single Git repository with only a main branch

**Important:** This isn't about capability — both Git branches (with CI/CD) and Hub workbenches provide isolation. The difference is in the **integration model**:

| Aspect | Git + CI/CD | Hub |
|--------|-------------|-----|
| **Integration** | Merge-based (branches merge to main) | Promotion-based (artifacts promoted between environments) |
| **Environment** | Ephemeral (spin up for build/test, tear down) | Persistent (always-available, scale-to-zero when idle) |
| **Isolation** | ✅ Provided (via branches) | ✅ Provided (via workbenches) |

### Who This Affects

| Developer Profile | Impact |
|-------------------|--------|
| Solo developer | ✅ No impact |
| Small team (2-3) | ⚠️ Minor — workbenches provide similar isolation |
| Larger team (5+) | ⚠️ Moderate — more workbenches to manage |
| Coming from GitFlow | 🔴 Significant — different mental model (merge vs. promotion) |

### The Trade-off

```
What you give up:                 What you gain:
────────────────                  ──────────────
Merge-based integration           Promotion-based integration
Ephemeral environments            Persistent, always-available environments
Familiar branching workflow       No merge conflicts, simpler model
```

### Mitigation

- Use feature workbenches for isolation when needed
- Think of workbenches as "super-branches" with runtime capabilities
- Embrace the simpler model for small teams

---

## 2. Workbench Creation Overhead

### What This Means

Creating a new workbench is heavier than creating a Git branch:

| Creating a Branch | Creating a Workbench |
|-------------------|---------------------|
| `git checkout -b feature-x` | CRD creation |
| Instant | Provisioning time |
| No infrastructure | Workbench resources provisioned |
| No cost | Low cost (scale-to-zero when idle) |

**Important context:**
- Workbenches are **persistent** — state is preserved, making them always-available
- Infrastructure **scales to zero** when idle — low ongoing cost
- The overhead is **upfront creation**, not ongoing resource consumption
- For long-running work, the persistent nature pays off

### Who This Affects

| Scenario | Impact |
|----------|--------|
| Long-running features | ✅ Worth the overhead — persistent state is valuable |
| Quick experiments | ⚠️ Might be excessive — use primary DEV workbench instead |
| Frequent context switching | ⚠️ Can feel slow — but persistent workbenches help resume work quickly |

### Mitigation

- Use your primary DEV workbench for most work
- Only create feature workbenches when genuinely needed (long-running, breaking changes)
- Template workbenches can speed up creation
- Remember: workbenches are cost-efficient (scale-to-zero) and persistent (state preserved)

---

## 3. Less Familiar to Many Developers

### What This Means

Most developers are trained in Git branching workflows:

```
Developer expectation:
├── Create branch
├── Make changes
├── Create PR
├── Merge after review
└── CI/CD deploys

Hub reality:
├── Edit in workbench
├── Sync changes
├── Test locally
├── Request promotion
└── Admin approves → deployed
```

### Who This Affects

| Background | Impact |
|------------|--------|
| New developers | ✅ Easy to learn (no unlearning) |
| Git experts | ⚠️ Requires mindset shift |
| DevOps specialists | ⚠️ Less familiar tooling |

### Mitigation

- Invest in onboarding (this guide!)
- Focus on the benefits, not the differences
- Remember: simpler ≠ inferior

---

## 4. Promotion Approval Can Be a Bottleneck

### What This Means

Promotion requires explicit approval:

```
Developer                    Admin                    PROD
    │                          │                        │
    │  Request promotion       │                        │
    ├─────────────────────────▶│                        │
    │                          │                        │
    │  ⏳ Waiting...           │                        │
    │  ⏳ Still waiting...     │  (in a meeting)       │
    │  ⏳ ...                  │                        │
    │                          │                        │
```

### Who This Affects

| Situation | Impact |
|-----------|--------|
| Urgent hotfixes | 🔴 Can delay critical fixes |
| Frequent deployments | ⚠️ Approval overhead adds up |
| Single approver | 🔴 Single point of failure |

### Mitigation

- Designate multiple approvers
- Auto-approve for low-risk changes (if policy allows)
- Request promotions before EOD
- Emergency procedures for urgent cases

---

## 5. Main Branch Only — No History Branching

### What This Means

- Can't branch from a historical point
- Can't maintain multiple release lines
- Rolling back requires explicit rollback, not checkout

### Who This Affects

| Use Case | Impact |
|----------|--------|
| Single release line | ✅ No impact |
| Multiple maintained versions | 🔴 Not directly supported |
| Exploratory work from past state | ⚠️ Requires workbench copy |

### The Trade-off

```
What you give up:                 What you gain:
────────────────                  ──────────────
Multiple release branches         Simpler history
Hotfix branches                   Linear audit trail
Complex version trees             Clear promotion path
```

---

## 6. Physical Copy Adds Promotion Time

### What This Means

Cross-subscription promotion copies artifacts physically:

```
Promotion time:
├── Same subscription: Fast (references only)
└── Cross-subscription: Slower (physical copy)
    ├── Container image copy: 1-5 minutes
    └── CRD cloning: Usually fast
```

### Who This Affects

| Scenario | Impact |
|----------|--------|
| Large container images | ⚠️ Noticeable delay |
| Frequent cross-sub promotions | ⚠️ Adds up |
| Time-sensitive deployments | ⚠️ Plan for copy time |

### Mitigation

- Keep container images lean
- Pre-approve promotions for urgent cases
- Factor copy time into deployment planning

---

## 7. Stubbing is Your Responsibility

### What This Means

Hub doesn't provide built-in mocking/stubbing for external dependencies:

```
Testing with external dependencies:
├── Machine/Tool instances: You configure test versions
├── Mock services: You build/deploy them
└── Test data: You manage it
```

### Who This Affects

| Scenario | Impact |
|----------|--------|
| Simple Scenarios | ✅ Minimal external dependencies |
| Integration-heavy | ⚠️ More stub setup work |
| Complex external systems | 🔴 Significant test setup |

### Mitigation

- Use dedicated test environments with mock endpoints
- Create test-specific Machine/Tool instances
- Invest in good test data management

---

## When Hub Might Not Be the Right Fit

Be honest about fit. Hub may not be ideal for:

| Scenario | Why It's Challenging |
|----------|---------------------|
| **Large teams (10+)** | Workbench management overhead |
| **Rapid experimentation** | Workbench creation feels heavy (though scale-to-zero keeps cost low) |
| **Prefer merge-based integration** | Hub uses promotion-based integration — this is a paradigm difference, not a weakness |
| **Prefer local development** | Hub is cloud-based — developers work in cloud workspaces |
| **Multiple maintained versions** | Single version line assumed |
| **No approval authority** | Bottleneck on promotions |

---

## Summary: Know the Trade-offs

| Limitation | Trade-off For |
|------------|---------------|
| Different integration model (promotion vs. merge) | Persistent environments, no merge conflicts, simpler model |
| Workbench creation overhead | Persistent, always-available environments (scale-to-zero, low cost) |
| Unfamiliar model | Simpler mental model once learned, benefits for small teams |
| Approval bottleneck | Explicit, auditable gates (important for compliance when applicable) |
| Physical copy time | Complete subscription isolation |

---

> **Bottom line:** Hub's model is optimized for small teams prioritizing simplicity, especially those leveraging AI-assisted development or operating in regulated environments. The paradigm differences (promotion vs. merge, persistent vs. ephemeral) are trade-offs, not inherent weaknesses. If this context fits you, the trade-offs are worth it. If not, evaluate carefully.

---

[← Previous: Merits](./08-merits.md) | [Back to Index](./README.md) | [Next: Best Practices →](./10-best-practices.md)

