# Why a Different Development Model?

[← Back to Index](./README.md) | [Next: Two-Subscription Model →](./02-two-subscription-model.md)

---

## The Question You're Probably Asking

*"Why doesn't Hub just use Git branches like everything else?"*

It's a fair question. Git branching is the industry standard. GitFlow, trunk-based development, feature branches — these are well-understood patterns. So why does Hub do things differently?

The short answer: **Hub is designed for small teams in regulated enterprises**, and that context changes everything.

---

## The Context: Small Teams, Big Compliance

Hub's target users are:

| Characteristic | Implication |
|----------------|-------------|
| **Small teams** | 2-5 developers, not 50 |
| **Regulated industries** | Banks, financial services, healthcare |
| **Compliance requirements** | Audit trails, separation of duties, approval workflows |
| **Enterprise infrastructure** | Security boundaries, access control, change management |

In this context, the traditional Git branching model creates friction:

### The Problem with Branches in Regulated Environments

```
Traditional Branch Workflow in Regulated Enterprise:

Developer                     Git                        Production
    │                          │                              │
    │  Create feature branch   │                              │
    ├─────────────────────────▶│                              │
    │                          │                              │
    │  Make changes            │                              │
    ├─────────────────────────▶│                              │
    │                          │                              │
    │  Create PR               │                              │
    ├─────────────────────────▶│                              │
    │                          │                              │
    │  Wait for review         │  ← Who approved?             │
    │  ...                     │  ← When?                     │
    │  ...                     │  ← What exactly changed?     │
    │                          │                              │
    │  Merge to main           │                              │
    ├─────────────────────────▶│                              │
    │                          │                              │
    │                          │  CI/CD deploys               │
    │                          ├─────────────────────────────▶│
    │                          │                              │
    │                          │  ← Audit: was this approved? │
    │                          │  ← By whom? For what env?    │
```

**The compliance challenges:**

| Challenge | Description |
|-----------|-------------|
| **Merge complexity** | Merge conflicts require resolution; who approved the resolution? |
| **Audit trail gaps** | Git history shows code changes, not deployment approvals |
| **Environment ambiguity** | Which branch maps to which environment? |
| **Approval attribution** | PR approval ≠ production deployment approval |

---

## Hub's Approach: Workbenches as Isolated Contexts

Hub replaces branches with **workbenches** — complete, isolated development and runtime contexts:

```
Hub Workbench Workflow:

Developer                    DEV Workbench                 PROD Workbench
    │                             │                              │
    │  Edit Scenario CRDs         │                              │
    ├────────────────────────────▶│                              │
    │                             │                              │
    │  Sync changes               │                              │
    ├────────────────────────────▶│                              │
    │                             │                              │
    │  Test in DEV                │                              │
    ├────────────────────────────▶│                              │
    │                             │                              │
    │  Request Promotion          │                              │
    ├─────────────────────────────┼─────────────────────────────▶│
    │                             │                              │
    │                             │  Admin approves              │
    │                             │  ← Explicit approval         │
    │                             │  ← Recorded with timestamp   │
    │                             │  ← Tied to specific artifacts│
    │                             │                              │
    │                             │  Artifacts promoted          │
    │                             ├─────────────────────────────▶│
    │                             │                              │
```

**Why this works better for compliance:**

| Benefit | How It Helps |
|---------|--------------|
| **No merge conflicts** | Each workbench is isolated; no code merging required |
| **Explicit promotion** | Promotion is a first-class operation, not a side effect of merge |
| **Clear approval** | Promotion requires explicit approval with recorded attribution |
| **Atomic artifacts** | Scenarios are promoted as complete units, not diff patches |
| **Audit-friendly** | Every promotion is logged with who, what, when, and why |

---

## What This Means for You

### Things That Stay the Same

| Familiar Concept | Hub Equivalent |
|-----------------|----------------|
| Writing code | Editing Scenario CRDs, Hub Application code |
| Local testing | Testing in your DEV workbench |
| Code review | Promotion approval process |
| CI/CD | Runtime CI + Hub Test Runner |
| Deployment | Promotion to STAGING/PROD |

### Things That Are Different

| Traditional | Hub |
|-------------|-----|
| Create a feature branch | Use your DEV workbench (or create a feature workbench) |
| Push to remote | Sync CRDs to workbench |
| Create PR | Request promotion |
| Merge to main | Promotion approved and executed |
| Branch cleanup | Workbench cleanup (if feature workbench) |

---

## The Mental Model Shift

Think of it this way:

| Git World | Hub World |
|-----------|-----------|
| Repository | Subscription |
| Branch | Workbench |
| Commit | CRD version in Git |
| Merge | Promotion |
| Main branch | PROD workbench |

The key insight: **In Hub, a workbench isn't just a Git branch — it's a complete, running environment where you can test your changes before promoting them.**

---

## Is This Right for Everyone?

No. Hub's model is optimized for:

✅ Small teams (2-5 developers)  
✅ Regulated industries with compliance requirements  
✅ Enterprise environments with security boundaries  
✅ Scenarios where audit trails are non-negotiable  

It may feel constraining for:

❌ Large teams with many parallel features  
❌ Open-source or startup-style rapid iteration  
❌ Organizations without compliance requirements  

---

## Summary

| Question | Answer |
|----------|--------|
| **Why no branches?** | Workbenches provide better isolation and audit trails |
| **Is this limiting?** | For small teams in regulated environments, it's actually simpler |
| **Do I lose anything?** | Branch flexibility is traded for compliance clarity |
| **Should I fight it?** | No — embrace the model and it works well |

---

[← Back to Index](./README.md) | [Next: Two-Subscription Model →](./02-two-subscription-model.md)

