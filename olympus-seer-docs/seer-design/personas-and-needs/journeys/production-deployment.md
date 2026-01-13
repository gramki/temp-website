# Journey: Production Deployment

> **Status:** 🟡 Draft  
> **Last Updated:** 2026-01-13  
> **Priority:** High  
> **Frequency:** High  
> **Personas Involved:** AE, ARE, CSA

---

## Overview

This journey covers the process of deploying an agent version to production, including the handoff from AE to ARE, staged rollout, and verification. This is a high-frequency journey that occurs for every agent update.

---

## Journey Flow

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                       PRODUCTION DEPLOYMENT JOURNEY                          │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  ┌─────────────┐    ┌─────────────┐    ┌─────────────┐    ┌─────────────┐  │
│  │  PREPARE    │───▶│  VALIDATE   │───▶│   SUBMIT    │───▶│   REVIEW    │  │
│  │   (AE)      │    │  (AE/CSA)   │    │   (AE)      │    │   (ARE)     │  │
│  └─────────────┘    └─────────────┘    └─────────────┘    └─────────────┘  │
│         │                 │                  │                  │          │
│         │ Version         │ Tests &          │ Checklist        │ Gate     │
│         │ Created         │ Design           │ Complete         │ Review   │
│         ▼                 ▼                  ▼                  ▼          │
│  ┌─────────────┐    ┌─────────────┐    ┌─────────────┐    ┌─────────────┐  │
│  │   STAGE     │───▶│   CANARY    │───▶│  PROMOTE    │───▶│   VERIFY    │  │
│  │   (AE)      │    │ (AE/ARE)    │    │(AE/ARE)     │    │(ARE/COS)    │  │
│  └─────────────┘    └─────────────┘    └─────────────┘    └─────────────┘  │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## Phase 1: Prepare Release (AE)

**Desk:** [Agent Development Desk](../../ux-architecture/desks/agent-development-desk/README.md)  
**Console:** [Release Console](../../ux-architecture/desks/agent-development-desk/release-console.md)

### Activities

| Step | Action | Artifact |
|------|--------|----------|
| 1.1 | Finalize code/prompt changes | Code Changes |
| 1.2 | Update changelog | Changelog |
| 1.3 | Create version | Version Tag |
| 1.4 | Build release artifact | Build Artifact |

### Version Naming

```
v{major}.{minor}.{patch}
- major: Breaking changes or major features
- minor: New features, backward compatible
- patch: Bug fixes, minor improvements
```

---

## Phase 2: Validate (AE, CSA)

**Desks:** [Agent Development Desk](../../ux-architecture/desks/agent-development-desk/README.md), [Agent Design Desk](../../ux-architecture/desks/agent-design-desk/README.md)

### Test Validation (AE)

| Test Type | Requirement | Console |
|-----------|-------------|---------|
| Unit Tests | 100% passing | Test Console |
| Behavioral Tests | 100% passing | Test Console |
| Integration Tests | 100% passing | Test Console |
| Regression Tests | 100% passing | Test Console |

### Design Validation (CSA)

Required for:
- Pattern changes
- New tool bindings
- Significant prompt changes

| Check | Status | Console |
|-------|--------|---------|
| Pattern compliance | Required | Validation Console |
| Constraint adherence | Required | Validation Console |
| Failure mode coverage | Required | Validation Console |

---

## Phase 3: Production Readiness Checklist (AE)

**Desk:** [Agent Development Desk](../../ux-architecture/desks/agent-development-desk/README.md)  
**Console:** [Release Console](../../ux-architecture/desks/agent-development-desk/release-console.md)

### Checklist Items

| Category | Item | Verified |
|----------|------|----------|
| **Contract** | Agent contract complete | ☐ |
| **Safety** | Safety controls implemented | ☐ |
| **Safety** | Kill switch tested | ☐ |
| **Safety** | Execution bounds defined | ☐ |
| **Telemetry** | Required events implemented | ☐ |
| **Telemetry** | Trace sampling configured | ☐ |
| **Cost** | Cost attribution configured | ☐ |
| **Cost** | Cost ceiling defined | ☐ |
| **Testing** | All tests passing | ☐ |
| **Testing** | Coverage acceptable | ☐ |
| **Rollback** | Previous version available | ☐ |
| **Design** | CSA validation (if required) | ☐ |

---

## Phase 4: Submit for ARE Review (AE)

**Desk:** [Agent Development Desk](../../ux-architecture/desks/agent-development-desk/README.md)  
**Console:** [Release Console](../../ux-architecture/desks/agent-development-desk/release-console.md)

### Submission Package

```
## Production Deployment Request

### Version Information
- Agent: [name]
- Version: [version]
- Previous: [previous version]

### Changes
[summary of changes]

### Test Results
- Unit: [X/X passing]
- Behavioral: [X/X passing]
- Integration: [X/X passing]
- Regression: [X/X passing]

### Checklist
[completed checklist]

### Rollback Plan
[rollback instructions]
```

---

## Phase 5: ARE Review (ARE)

**Desk:** [Agent Operations Desk](../../ux-architecture/desks/agent-operations-desk/README.md)  
**Console:** [Control Console](../../ux-architecture/desks/agent-operations-desk/control-console.md)

### Review Criteria

| Criterion | Check |
|-----------|-------|
| Checklist complete | All items verified |
| Test coverage adequate | Coverage meets standards |
| Rollback available | Previous version accessible |
| Operational impact acceptable | No major concerns |

### Decision

| Decision | Outcome |
|----------|---------|
| **Approve** | Proceed to deployment |
| **Request Changes** | Return to AE |
| **Deny** | Document reason |

---

## Phase 6: Staged Deployment

### Stage 1: Staging Environment (AE)

**Console:** [Release Console](../../ux-architecture/desks/agent-development-desk/release-console.md)

| Step | Action | Duration |
|------|--------|----------|
| 6.1 | Deploy to staging | Immediate |
| 6.2 | Run smoke tests | 15 minutes |
| 6.3 | Verify metrics | 30 minutes |
| 6.4 | Approve for canary | Manual gate |

### Stage 2: Canary Deployment (AE, ARE)

| Step | Action | Duration |
|------|--------|----------|
| 6.5 | Deploy to 10% of traffic | Immediate |
| 6.6 | Monitor health | 30 minutes |
| 6.7 | Compare to baseline | Ongoing |
| 6.8 | Decision: continue or abort | Manual gate |

### Canary Criteria

| Metric | Threshold | Action if Exceeded |
|--------|-----------|-------------------|
| Error rate | < 2% | Abort |
| Latency P95 | < baseline + 10% | Investigate |
| AHS | > 0.85 | Required |

### Stage 3: Progressive Rollout

| Step | Traffic | Duration | Gate |
|------|---------|----------|------|
| 6.9 | 25% | 1 hour | Auto if healthy |
| 6.10 | 50% | 2 hours | Auto if healthy |
| 6.11 | 100% | Full deployment | Manual approval |

---

## Phase 7: Verify (ARE, COS)

**Desks:** [Agent Operations Desk](../../ux-architecture/desks/agent-operations-desk/README.md), [Cognitive Health Desk](../../ux-architecture/desks/cognitive-health-desk/README.md)

### Post-Deployment Monitoring

| Metric | Duration | Owner |
|--------|----------|-------|
| Health metrics | 24 hours | ARE |
| Cognitive quality | 24 hours | COS |
| Error rate | 24 hours | ARE |
| User feedback | 48 hours | APO |

### Activities

| Step | Action | Responsible |
|------|--------|-------------|
| 7.1 | Verify health metrics stable | ARE |
| 7.2 | Verify cognitive quality stable | COS |
| 7.3 | Update baselines if needed | COS |
| 7.4 | Close deployment ticket | AE |

---

## Rollback Process

If issues detected at any stage:

```
┌─────────────┐    ┌─────────────┐    ┌─────────────┐    ┌─────────────┐
│   DETECT    │───▶│   DECIDE    │───▶│  ROLLBACK   │───▶│   VERIFY    │
│   Issue     │    │   Action    │    │  Execute    │    │   Health    │
└─────────────┘    └─────────────┘    └─────────────┘    └─────────────┘
```

### Rollback Steps

| Step | Action | Console | Owner |
|------|--------|---------|-------|
| R.1 | Detect issue | Health Console | ARE |
| R.2 | Decide to rollback | Control Console | ARE |
| R.3 | Execute rollback | Control Console | ARE |
| R.4 | Verify health restored | Health Console | ARE |
| R.5 | Notify AE | Notification | ARE |
| R.6 | Investigate root cause | Test Console | AE |

---

## OPDA Alignment

| Property | Deployment Relevance |
|----------|---------------------|
| **Observable** | Deployment visible in health dashboard |
| **Predictable** | Staged rollout reduces risk |
| **Directable** | Rollback available at any stage |
| **Authority** | No authority changes in deployment |

---

## Success Criteria

- [ ] All tests passing
- [ ] Production readiness checklist complete
- [ ] ARE approval obtained
- [ ] Staging validation successful
- [ ] Canary metrics within threshold
- [ ] Full deployment complete
- [ ] 24-hour monitoring period stable
- [ ] No rollback required

---

*Production deployment is the critical path from development to value delivery.*
