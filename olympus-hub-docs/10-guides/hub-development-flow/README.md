# Hub Development Flow: A Developer's Primer

> **Audience:** Developers building on Hub  
> **Goal:** Understand Hub's development model and work effectively within it

---

## Why This Guide Exists

If you're coming from a traditional software development background, Hub's development model may feel different. This guide explains:

- **Why** Hub uses workbenches instead of Git branches
- **How** the two-subscription model works
- **What** your daily workflow looks like
- **When** to create additional workbenches

By the end, you'll understand not just the mechanics, but the rationale behind Hub's approach.

---

## Quick Summary

| Traditional Approach | Hub Approach |
|---------------------|--------------|
| Feature branches in Git | Separate DEV workbenches |
| Merge to main | Promote Scenario to target |
| CI/CD pipeline per branch | Runtime CI + Promotion |
| Environment = deployment target | Workbench = isolated context |

---

## The Hub Development Model at a Glance

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    HUB DEVELOPMENT FLOW                                      │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│   DEV SUBSCRIPTION                       PROD SUBSCRIPTION                   │
│   ┌─────────────────────────┐           ┌─────────────────────────┐         │
│   │                         │           │                         │         │
│   │  ┌─────────────────┐    │           │    ┌─────────────────┐  │         │
│   │  │  DEV Workbench  │    │           │    │ PROD Workbench  │  │         │
│   │  │                 │    │           │    │                 │  │         │
│   │  │  You work here  │    │  Promote  │    │  Production     │  │         │
│   │  │  ────────────── │────┼──────────▶│    │                 │  │         │
│   │  │  • Edit CRDs    │    │           │    │                 │  │         │
│   │  │  • Build apps   │    │           │    │                 │  │         │
│   │  │  • Run tests    │    │           │    │                 │  │         │
│   │  └─────────────────┘    │           │    └─────────────────┘  │         │
│   │           │             │           │                         │         │
│   │           ▼             │           │                         │         │
│   │  ┌─────────────────┐    │           │                         │         │
│   │  │STAGING Workbench│    │           │                         │         │
│   │  │  (validation)   │    │           │                         │         │
│   │  └─────────────────┘    │           │                         │         │
│   │                         │           │                         │         │
│   └─────────────────────────┘           └─────────────────────────┘         │
│                                                                              │
└──────────────────────────────────────────────────────────────────────────────┘
```

---

## Guide Contents

| # | Section | Description |
|---|---------|-------------|
| 1 | [Why a Different Model?](./01-why-different-model.md) | The rationale behind Hub's approach |
| 2 | [Two-Subscription Model](./02-two-subscription-model.md) | DEV vs PROD subscription separation |
| 3 | [Workbench-Based Development](./03-workbench-based-development.md) | Using workbenches instead of branches |
| 4 | [Development to Production](./04-development-to-production-flow.md) | Step-by-step promotion walkthrough |
| 5 | [Daily Workflow](./05-daily-workflow.md) | Day-to-day developer activities |
| 6 | [Collaboration Patterns](./06-collaboration-patterns.md) | Working effectively in small teams |
| 7 | [CI/CD Integration](./07-ci-cd-integration.md) | Build, test, and deploy with Hub |
| 8 | [Merits of This Approach](./08-merits.md) | Why this model works well |
| 9 | [Limitations & Trade-offs](./09-limitations.md) | Honest assessment of constraints |
| 10 | [Best Practices](./10-best-practices.md) | Tips for effective Hub development |

---

## Key Concepts

Before diving in, familiarize yourself with these terms:

| Concept | Definition |
|---------|------------|
| **Workbench** | Isolated development/runtime context with its own configurations |
| **Scenario** | A business process automation; the atomic unit of promotion |
| **Dev-Lifecycle-Stage** | Tag (DEV/STAGING/PROD) indicating workbench purpose — not to be confused with "Hub Environment" |
| **Hub Environment** | Business/operations domain entity for runtime configuration (different from dev-lifecycle-stage) |
| **Promotion** | Moving artifacts from one workbench to another |
| **Subscription** | Isolated tenant environment with dedicated registries and Git repo |

---

## Start Here

1. **New to Hub?** Start with [Why a Different Model?](./01-why-different-model.md)
2. **Setting up?** Jump to [Two-Subscription Model](./02-two-subscription-model.md)
3. **Ready to code?** See [Daily Workflow](./05-daily-workflow.md)
4. **Evaluating Hub?** Read [Merits](./08-merits.md) and [Limitations](./09-limitations.md)

---

## Related Documentation

- [Artifact Registry](../../04-subsystems/artifact-registry/README.md) — Technical details on registries and promotion
- [Dev-Lifecycle-Stages](../../04-subsystems/artifact-registry/dev-lifecycle-stages.md) — Stage definitions and registry access
- [CI Subsystem](../../04-subsystems/ci-subsystem/README.md) — Build and test infrastructure
- [Workbench Management](../../04-subsystems/workbench-management/README.md) — Workbench lifecycle and configuration
- [Developer Operators](../../04-subsystems/operators/developer-operators.md) — CRD specifications

