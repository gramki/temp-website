# Release Console

> **Status:** 🟡 Draft  
> **Last Updated:** 2026-01-13  
> **Desk:** [Agent Development Desk](./README.md)  
> **Primary Persona:** [Agent Engineer (AE)](../../../personas-and-needs/roles.md#3-agent-engineer-ae)

---

## Purpose

The Release Console enables the **Agent Engineer (AE)** ([role definition](../../../personas-and-needs/roles.md#3-agent-engineer-ae)) to manage versioning, deployment pipelines, and production handoff to the **Agent Reliability Engineer (ARE)** ([role definition](../../../personas-and-needs/roles.md#5-agent-reliability-engineer-are)).

---

## Sections

### Version Manager

Create and manage agent versions.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│ VERSION MANAGER: invoice-processor                                          │
├─────────────────────────────────────────────────────────────────────────────┤
│ [+ Create Version]                                                          │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│ Version  │ Status      │ Created      │ Deployed      │ Actions            │
│ ───────────────────────────────────────────────────────────────────────────│
│ v2.3.1   │ 🟢 Prod     │ Jan 10, 2026 │ Jan 11, 2026  │ [View] [Rollback] │
│ v2.3.0   │ ⚫ Previous │ Jan 5, 2026  │ Jan 6, 2026   │ [View] [Compare]  │
│ v2.2.0   │ ⚫ Previous │ Dec 20, 2025 │ Dec 21, 2025  │ [View] [Compare]  │
│ v2.4.0   │ 🟡 Staging  │ Jan 12, 2026 │ —             │ [View] [Deploy]   │
│ v2.5.0   │ 📝 Draft    │ Jan 13, 2026 │ —             │ [View] [Build]    │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Deployment Pipeline

Staged deployment with validation gates.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│ DEPLOYMENT PIPELINE: invoice-processor v2.4.0                               │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│ ┌────────────┐    ┌────────────┐    ┌────────────┐    ┌────────────┐       │
│ │   BUILD    │───▶│  STAGING   │───▶│  CANARY    │───▶│ PRODUCTION │       │
│ │     ✅     │    │     ✅     │    │    🔄     │    │     ⬜     │       │
│ └────────────┘    └────────────┘    └────────────┘    └────────────┘       │
│                                                                             │
│ CURRENT STAGE: Canary                                                       │
│ ──────────────────────────────────────────────────────────────────────────  │
│ Progress: 10% of traffic │ Duration: 2 hours                                │
│ Health: AHS 0.91 (target: 0.85) ✅                                          │
│ Errors: 0.2% (target: <1%) ✅                                               │
│                                                                             │
│ [Pause] [Abort] [Promote to 50%] [Promote to Production]                    │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### ARE Handoff

Production readiness checklist and submission.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│ PRODUCTION READINESS: invoice-processor v2.4.0                              │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│ CHECKLIST                                                   Progress: 5/7   │
│ ──────────────────────────────────────────────────────────────────────────  │
│ ☑ Agent contract complete                                   ✅ Verified     │
│ ☑ Safety controls implemented                               ✅ Verified     │
│ ☑ Telemetry validated                                       ✅ Verified     │
│ ☑ Cost attribution configured                               ✅ Verified     │
│ ☑ All tests passing                                         ✅ 97/97        │
│ ⬜ CSA design validation                                    🔄 Pending      │
│ ⬜ ARE sign-off                                             ⬜ Not started  │
│                                                                             │
│ OPERABILITY CONTRACT                                                        │
│ ──────────────────────────────────────────────────────────────────────────  │
│ Kill Switch: ✅ Implemented and tested                                      │
│ Execution Bounds: ✅ 10 iterations, 60s timeout                             │
│ Cost Ceiling: ✅ $5.00 per request                                          │
│ Rollback: ✅ One-click to v2.3.1                                            │
│                                                                             │
│ [Submit to ARE for Review]                                                  │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Rollback

Quick rollback to previous versions.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│ ROLLBACK: invoice-processor                                                 │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│ Current Production: v2.3.1                                                  │
│ Rollback Target: v2.3.0                                                     │
│                                                                             │
│ ⚠️ This will replace v2.3.1 with v2.3.0 in production                      │
│                                                                             │
│ CHANGES BEING REVERTED                                                      │
│ ──────────────────────────────────────────────────────────────────────────  │
│ • Prompt update: confidence threshold 0.85 → 0.80                           │
│ • New tool: receipt_ocr                                                     │
│ • Bug fix: retry logic improvement                                          │
│                                                                             │
│ Rollback Validation:                                                        │
│ ☑ v2.3.0 image available                                                    │
│ ☑ Configuration compatible                                                  │
│ ☑ No database migrations to revert                                          │
│                                                                             │
│ [Cancel]                                      [Execute Rollback]            │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## Key Features

- **Semantic versioning**
- **Staged deployment (Stage → Canary → Production)**
- **Production readiness checklist**
- **One-click rollback**
- **ARE integration for sign-off**

---

## OPDA Contribution

| OPDA | Console Contribution |
|------|---------------------|
| **Observable** | Deployment status visibility |
| **Predictable** | Staged rollout reduces risk |
| **Directable** | Rollback capability |
| **Authority Enforceable** | Release gates |

---

*Status: 🟡 Draft — Specification complete, implementation TBD*
