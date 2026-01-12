# AE Need: Full Development Lifecycle Coverage

> **Status:** Reference Document  
> **Last Updated:** 2026-01-13  
> **Related:** [AE Role Definition](../ae.md) | [Roles Overview](../roles.md#3-agent-engineer-ae)

---

## Overview

The **Agent Engineer (AE)** ([role definition](../roles.md#3-agent-engineer-ae)) requires platform support for the **complete agent development lifecycle** — from receiving feedback on existing agents to implementing improvements and releasing new versions.

This document details the lifecycle stages and platform requirements for AE to effectively develop and evolve agents.

---

## The Agent Development Lifecycle

### Lifecycle Stages

```
┌─────────────────────────────────────────────────────────────────────────┐
│                                                                         │
│   Feedback → Issue → Design → Implement → Test → Release → Monitor     │
│       ↑                                                         │       │
│       └─────────────────────────────────────────────────────────┘       │
│                         Continuous Improvement                          │
└─────────────────────────────────────────────────────────────────────────┘
```

| Stage | Owner | AE Role |
|-------|-------|---------|
| **Feedback** | COS, ARE, APO | Receive feedback |
| **Issue** | APO (prioritize), AE (triage) | Investigate root cause |
| **Design** | CSA | Review and validate feasibility |
| **Implement** | AE | Build the solution |
| **Test** | AE | Validate correctness |
| **Release** | AE → ARE | Deploy to production |
| **Monitor** | ARE, COS | Observe in production |

---

## Stage 1: Feedback Reception

### Feedback Sources

AE receives feedback from multiple sources:

| Source | Type of Feedback | Example |
|--------|------------------|---------|
| **COS** | Behavioral issues | "Agent inconsistent on edge cases" |
| **ARE** | Operational issues | "Agent exceeds cost bounds on retries" |
| **APO** | Business issues | "Agent not meeting outcome targets" |
| **Users** | Experience issues | "Agent responses too slow" |
| **CSA** | Design issues | "Implementation drifted from design" |

### Platform Requirements

AE needs:
- **Unified Feedback Inbox** — All feedback in one view
- **Feedback Classification** — Categorize by type (bug, enhancement, optimization)
- **Priority Visibility** — See APO-assigned priorities
- **Feedback Context** — Access related traces, logs, and decisions

### OPDA Support

| Dimension | Need |
|-----------|------|
| **Observable** | See all feedback with context |
| **Directable** | AE can request more information |

---

## Stage 2: Issue Investigation

### Investigation Workflow

```
Feedback received
       ↓
Reproduce issue (Scenario Replay)
       ↓
Analyze traces and decisions
       ↓
Classify root cause:
├── Prompt issue → Fix prompt
├── Logic issue → Fix code
├── Tool issue → Fix binding
├── Design issue → Escalate to CSA
└── Knowledge issue → Escalate to KMO
```

### Platform Requirements

AE needs:
- **Scenario Replay** — Re-run production scenarios in sandbox
- **Trace Analysis** — Inspect reasoning steps, tool calls, decisions
- **Diff View** — Compare expected vs. actual behavior
- **Root Cause Classification** — Structured categorization

### OPDA Support

| Dimension | Need |
|-----------|------|
| **Observable** | Full trace visibility for debugging |
| **Predictable** | Replay produces consistent results |

---

## Stage 3: Design Review

### CSA Collaboration

For significant changes, AE collaborates with CSA:

| Change Type | CSA Involvement |
|-------------|-----------------|
| Prompt adjustment | Inform CSA |
| Logic change within design | Inform CSA |
| New tool integration | CSA review required |
| Reasoning pattern change | CSA approval required |
| Escalation modification | CSA approval required |

### Platform Requirements

AE needs:
- **Design Spec Access** — View CSA's design documents
- **Change Request Workflow** — Request design changes from CSA
- **Design Validation** — Automated checks against design constraints

### OPDA Support

| Dimension | Need |
|-----------|------|
| **Predictable** | Implementation matches design |
| **Authority Enforceable** | Design constraints are checked |

---

## Stage 4: Implementation

### Implementation Artifacts

AE produces and manages:

| Artifact | Description | Version Controlled |
|----------|-------------|-------------------|
| **Agent Code** | Core logic, workflows, orchestration | Yes |
| **Prompts** | System, task, and tool prompts | Yes |
| **Tool Bindings** | External tool integrations | Yes |
| **Configuration** | Runtime parameters, feature flags | Yes |
| **Telemetry Config** | Events, traces, metrics definitions | Yes |

### Implementation Standards

AE must follow standards for:

1. **Prompt Engineering**
   - Version all prompts
   - Document prompt rationale
   - Include test cases with prompts

2. **Code Quality**
   - Follow agent framework best practices
   - Implement required safety hooks
   - Emit required telemetry events

3. **Tool Integration**
   - Validate input schemas
   - Handle tool failures gracefully
   - Respect access permissions

4. **Observability**
   - Emit lifecycle events
   - Include decision context in traces
   - Classify failures with structured errors

### Platform Requirements

AE needs:
- **Development Console** — IDE-like environment for agent development
- **Prompt Editor** — Specialized editor with versioning
- **Tool Binding Manager** — Configure and test tool integrations
- **Telemetry Validator** — Verify observability contracts

### OPDA Support

| Dimension | Need |
|-----------|------|
| **Observable** | Telemetry is implemented correctly |
| **Directable** | Safety hooks enable runtime control |
| **Authority Enforceable** | Bounds are implemented |

---

## Stage 5: Testing

### Test Types

| Test Type | Purpose | When Run |
|-----------|---------|----------|
| **Unit Tests** | Component correctness | Every commit |
| **Behavioral Tests** | Reasoning validation | Every commit |
| **Integration Tests** | Tool binding validation | Every commit |
| **Regression Tests** | Prompt stability | Every prompt change |
| **Stress Tests** | Bound enforcement | Before release |
| **Scenario Replay** | Production parity | Before release |

### Test Strategies for Agents

Agent testing differs from traditional software:

| Traditional Testing | Agent Testing |
|---------------------|---------------|
| Assert exact output | Assert acceptable output range |
| Mock dependencies | Mock with realistic responses |
| Test edge cases | Test reasoning edge cases |
| Coverage = lines | Coverage = scenarios |

### Platform Requirements

AE needs:
- **Test Console** — Test suite management and execution
- **Expected/Actual Comparison** — Behavior comparison tools
- **Coverage Reporting** — Scenario coverage metrics
- **CI Integration** — Automated test runs

### OPDA Support

| Dimension | Need |
|-----------|------|
| **Predictable** | Tests validate predictable behavior |
| **Observable** | Test results are detailed and traceable |

---

## Stage 6: Release

### Release Workflow

```
AE prepares release
       ↓
Production Readiness Checklist
       ↓
Submit to ARE for review
       ↓
ARE validates operability
       ↓
Staged deployment:
├── Stage → Validate
├── Canary → Validate
└── Production → Monitor
       ↓
Post-deployment verification
```

### Production Readiness Checklist

Before release, AE must verify:

- [ ] Agent contract complete (see [AE Deliverables to ARE](./ae-deliverables-to-are.md))
- [ ] Safety controls implemented (kill switch, bounds)
- [ ] Telemetry validated (all required events emitting)
- [ ] Cost attribution configured
- [ ] All tests passing
- [ ] CSA design validation complete
- [ ] Rollback tested

### Platform Requirements

AE needs:
- **Release Console** — Version and deployment management
- **Checklist Automation** — Automated verification of readiness
- **Deployment Pipeline** — Staged rollout with validation gates
- **Rollback Capability** — Quick revert to previous version

### OPDA Support

| Dimension | Need |
|-----------|------|
| **Directable** | Rollback available |
| **Authority Enforceable** | Release gates enforced |

---

## Stage 7: Post-Release Monitoring

### AE's Post-Release Role

After release, AE:
- Monitors for issues during stabilization period
- Responds to ARE/COS escalations
- Investigates bugs that emerge in production
- Plans next iteration based on feedback

### Platform Requirements

AE needs:
- **Production Visibility** — See agent behavior in production
- **Alert Subscription** — Receive relevant alerts
- **Quick Debug Access** — Fast path to traces and logs

### OPDA Support

| Dimension | Need |
|-----------|------|
| **Observable** | Production behavior visible |
| **Directable** | Can respond to issues quickly |

---

## Feedback-to-Implementation Flow

### Complete Flow Example

```
1. COS detects: "Agent inconsistent on invoices > $5000"
       ↓
2. COS routes to AE with evidence
       ↓
3. AE receives in Feedback Inbox
       ↓
4. AE uses Scenario Replay to reproduce
       ↓
5. AE traces reasoning: finds prompt ambiguity
       ↓
6. AE classifies: Prompt Issue (no CSA review needed)
       ↓
7. AE edits prompt in Development Console
       ↓
8. AE creates regression test for this scenario
       ↓
9. AE runs full test suite in Test Console
       ↓
10. AE prepares release in Release Console
       ↓
11. AE submits for ARE production gate
       ↓
12. ARE approves, staged deployment begins
       ↓
13. AE monitors post-deployment
       ↓
14. COS verifies issue resolved
       ↓
15. Feedback closed
```

---

## Integration with Other Personas

### AE ↔ CSA

- CSA provides design; AE implements
- AE validates feasibility during design
- AE requests design changes when needed
- CSA validates implementation matches design

### AE ↔ ARE

- AE delivers operability contracts to ARE
- ARE validates production readiness
- ARE operates what AE builds
- ARE escalates issues back to AE

### AE ↔ COS

- COS detects behavioral issues
- AE investigates and fixes
- COS validates fixes work

### AE ↔ KMO

- AE integrates knowledge access
- KMO ensures knowledge is available
- AE escalates knowledge issues to KMO

---

## Desk Support

These needs are supported through the **Agent Development Desk**:

| Console | Lifecycle Stages Supported |
|---------|---------------------------|
| **Development Console** | Implement |
| **Test Console** | Test |
| **Release Console** | Release |

Additional features needed across all consoles:
- **Feedback Inbox** — Visible in Development Console
- **Scenario Replay** — Available in Development and Test Consoles
- **Production View** — Available in all consoles

See [Agent Development Desk](../../ux-architecture/desks/agent-development-desk/README.md) for detailed specifications.

---

## Anti-Patterns

| Pattern | Why It's Problematic |
|---------|---------------------|
| "Ship and forget" | Feedback requires attention |
| "Works in test, ship it" | Production differs from test |
| "Prompt works, no need to version" | Prompt changes need history |
| "We'll add tests later" | Untested agents break in production |
| "ARE can figure out limits" | AE implements, ARE enforces |

---

## Success Criteria

AE lifecycle needs are met when:

- [ ] All feedback is visible in one place
- [ ] Scenario replay enables reliable reproduction
- [ ] Traces provide full debugging context
- [ ] Tests validate behavior, not just outputs
- [ ] Release process has automated checks
- [ ] Rollback is one-click
- [ ] Post-release monitoring is accessible

---

*End of document*
