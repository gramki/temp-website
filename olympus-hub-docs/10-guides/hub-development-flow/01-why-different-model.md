# Why a Different Development Model?

[← Back to Index](./README.md) | [Next: Two-Subscription Model →](./02-two-subscription-model.md)

---

## The Question You're Probably Asking

*"Why doesn't Hub just use Git branches like everything else?"*

It's a fair question. Git branching is the industry standard. GitFlow, trunk-based development, feature branches — these are well-understood patterns. So why does Hub do things differently?

The short answer: **Hub is designed for small teams prioritizing simplicity and sustainable development** — especially those leveraging AI-assisted development or operating in regulated environments. This context changes the development model.

---

## The Context: Small Teams, AI-Assisted Development, and Compliance

Hub's target users are:

| Characteristic | Implication |
|----------------|-------------|
| **Small teams** | 2-5 developers, not 50 |
| **AI-assisted development** | AI agents handle more coding tasks, reducing team sizes and increasing context-switching frequency |
| **Frequent context switching** | Small teams work across multiple projects; developers need to switch contexts without local setup overhead |
| **Regulated industries** | Banks, financial services, healthcare (when applicable) |
| **Compliance requirements** | Audit trails, separation of duties, approval workflows (when applicable) |
| **Enterprise infrastructure** | Security boundaries, access control, change management |

In this context, the traditional Git branching model creates friction:

### The Paradigm Difference: Merge vs. Promotion, Ephemeral vs. Persistent

The difference isn't about isolation — both Git branches (with CI/CD) and Hub workbenches provide isolation. The real differences are:

**Integration Model:**
- **Git:** Merge-based integration (branches merge to main, CI/CD deploys)
- **Hub:** Promotion-based integration (artifacts promoted between environments with explicit approval)

**Environment Model:**
- **Git + CI/CD:** Ephemeral environments (spin up for build/test, tear down)
- **Hub:** Persistent, always-available environments (scale-to-zero when idle, state preserved)

**Why this matters for small teams with AI-assisted development:**
- **No local workspace required** — developers work in cloud workspaces, eliminating "works on my machine" issues
- **Faster context switching** — no need to set up local environments when switching projects
- **AI agents benefit from consistent environments** — same environment for all developers and AI agents
- **Persistent state** — workbench state is preserved, making it easy to resume work

**Why this matters for compliance (when applicable):**
- **Explicit promotion** — Promotion is a first-class operation with recorded approval, not a side effect of merge
- **Clear audit trail** — Every promotion is logged with who, what, when, and why
- **Atomic artifacts** — Scenarios are promoted as complete units, not diff patches

---

## Hub's Approach: Workbenches as Persistent Contexts

Hub replaces branches with **workbenches** — persistent, always-available development and runtime contexts:

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

**Why this works better:**

| Benefit | How It Helps |
|---------|--------------|
| **No merge conflicts** | Each workbench is isolated; no code merging required |
| **Persistent environments** | Workbench state is preserved; infrastructure scales to zero when idle (low cost) |
| **Always available** | No need to spin up environments — they're ready when you need them |
| **No local setup** | Developers work in cloud workspaces, eliminating environment inconsistencies |
| **Explicit promotion** | Promotion is a first-class operation with recorded approval (important for compliance) |
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

The key insight: **In Hub, a workbench isn't just a Git branch — it's a persistent, always-available environment where you can test your changes before promoting them. The infrastructure scales to zero when idle, so it's cost-efficient while remaining always accessible.**

---

## Is This Right for Everyone?

No. Hub's model is optimized for:

✅ **Small teams (2-5 developers)** — especially those leveraging AI-assisted development  
✅ **Frequent context switching** — teams working across multiple projects  
✅ **No local workspace overhead** — developers who want consistent cloud environments  
✅ **Regulated industries** (when applicable) — compliance requirements, audit trails  
✅ **Enterprise environments** (when applicable) — security boundaries, access control  

It may feel constraining for:

❌ Large teams with many parallel features  
❌ Open-source or startup-style rapid iteration  
❌ Teams that prefer local development environments  

---

## Summary

| Question | Answer |
|----------|--------|
| **Why no branches?** | Workbenches provide persistent, always-available environments with a different integration model (promotion vs. merge) |
| **Is this limiting?** | For small teams, especially with AI-assisted development, it's actually simpler — no local setup, faster context switching |
| **Do I lose anything?** | Merge-based integration is traded for promotion-based integration with explicit approval gates |
| **Should I fight it?** | No — embrace the model and it works well for its target context |

---

[← Back to Index](./README.md) | [Next: Two-Subscription Model →](./02-two-subscription-model.md)

