# Journey: New Agent Development

> **Status:** 🟡 Draft  
> **Last Updated:** 2026-01-13  
> **Priority:** Critical  
> **Frequency:** High  
> **Personas Involved:** APO, CSA, AE, ARE, ARAO

---

## Overview

This journey covers the end-to-end process of developing a new AI agent from initial chartering through production deployment. It is the most fundamental journey in Seer and involves nearly all personas.

---

## Journey Flow

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                        NEW AGENT DEVELOPMENT JOURNEY                         │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  ┌─────────────┐    ┌─────────────┐    ┌─────────────┐    ┌─────────────┐  │
│  │   CHARTER   │───▶│   DESIGN    │───▶│   BUILD     │───▶│  VALIDATE   │  │
│  │    (APO)    │    │   (CSA)     │    │   (AE)      │    │  (CSA/AE)   │  │
│  └─────────────┘    └─────────────┘    └─────────────┘    └─────────────┘  │
│         │                 │                  │                  │          │
│         │ Autonomy        │ Pattern          │ Test             │ Design   │
│         │ Ceiling         │ Selection        │ Suites           │ Comp.    │
│         ▼                 ▼                  ▼                  ▼          │
│  ┌─────────────┐    ┌─────────────┐    ┌─────────────┐    ┌─────────────┐  │
│  │  APPROVE    │───▶│  RELEASE    │───▶│  OPERATE    │───▶│   MONITOR   │  │
│  │   (ARAO)    │    │  (AE/ARE)   │    │   (ARE)     │    │   (COS)     │  │
│  └─────────────┘    └─────────────┘    └─────────────┘    └─────────────┘  │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## Phase 1: Charter (APO)

**Desk:** [Agent Portfolio Desk](../../ux-architecture/desks/agent-portfolio-desk/README.md)  
**Console:** [Portfolio Console](../../ux-architecture/desks/agent-portfolio-desk/portfolio-console.md)

### Activities

| Step | Action | Artifact |
|------|--------|----------|
| 1.1 | Define agent purpose and scope | Agent Charter |
| 1.2 | Identify business outcomes | Success Criteria |
| 1.3 | Propose initial autonomy ceiling | Autonomy Proposal |
| 1.4 | Assign ownership | Owner Assignment |

### Outputs

- Agent Charter document
- Proposed autonomy ceiling
- Business outcome definitions

---

## Phase 2: Autonomy Approval (ARAO)

**Desk:** [Agent Compliance Desk](../../ux-architecture/desks/agent-compliance-desk/README.md)  
**Console:** [Autonomy Console](../../ux-architecture/desks/agent-compliance-desk/autonomy-console.md)

### Activities

| Step | Action | Artifact |
|------|--------|----------|
| 2.1 | Review autonomy ceiling request | Review Record |
| 2.2 | Assess risk level | Risk Assessment |
| 2.3 | Define initial escalation rules | Escalation Config |
| 2.4 | Approve or request changes | Approval Decision |

### Outputs

- Approved autonomy ceiling
- Initial escalation rules
- Risk assessment record

---

## Phase 3: Design (CSA)

**Desk:** [Agent Design Desk](../../ux-architecture/desks/agent-design-desk/README.md)  
**Console:** [Design Console](../../ux-architecture/desks/agent-design-desk/design-console.md)

### Activities

| Step | Action | Artifact |
|------|--------|----------|
| 3.1 | Select cognitive pattern | Pattern Selection |
| 3.2 | Design agent architecture | Architecture Doc |
| 3.3 | Define failure modes | Failure Catalog |
| 3.4 | Specify design constraints | Constraint Spec |
| 3.5 | Define observability requirements | Trace Spec |

### Outputs

- Cognitive architecture design
- Pattern selection rationale
- Failure mode catalog
- Observability contract

---

## Phase 4: Build (AE)

**Desk:** [Agent Development Desk](../../ux-architecture/desks/agent-development-desk/README.md)  
**Console:** [Development Console](../../ux-architecture/desks/agent-development-desk/development-console.md)

### Activities

| Step | Action | Artifact |
|------|--------|----------|
| 4.1 | Implement prompts | Prompt Files |
| 4.2 | Configure tool bindings | Tool Config |
| 4.3 | Implement workflows | Workflow Code |
| 4.4 | Configure telemetry | Telemetry Config |
| 4.5 | Implement safety controls | Safety Config |

### Outputs

- Agent implementation
- Tool bindings
- Telemetry configuration

---

## Phase 5: Test (AE)

**Desk:** [Agent Development Desk](../../ux-architecture/desks/agent-development-desk/README.md)  
**Console:** [Test Console](../../ux-architecture/desks/agent-development-desk/test-console.md)

### Activities

| Step | Action | Artifact |
|------|--------|----------|
| 5.1 | Create behavioral test suite | Test Suite |
| 5.2 | Create integration tests | Test Suite |
| 5.3 | Run all tests | Test Results |
| 5.4 | Fix issues | Bug Fixes |
| 5.5 | Achieve passing tests | Test Report |

### Outputs

- Test suites
- Test results
- Coverage report

---

## Phase 6: Design Validation (CSA)

**Desk:** [Agent Design Desk](../../ux-architecture/desks/agent-design-desk/README.md)  
**Console:** [Validation Console](../../ux-architecture/desks/agent-design-desk/validation-console.md)

### Activities

| Step | Action | Artifact |
|------|--------|----------|
| 6.1 | Review implementation vs design | Comparison Report |
| 6.2 | Verify pattern compliance | Checklist |
| 6.3 | Approve or request changes | Validation Decision |

### Outputs

- Design validation decision
- Change requests (if any)

---

## Phase 7: Release (AE → ARE)

**Desk:** [Agent Development Desk](../../ux-architecture/desks/agent-development-desk/README.md)  
**Console:** [Release Console](../../ux-architecture/desks/agent-development-desk/release-console.md)

### Activities

| Step | Action | Artifact |
|------|--------|----------|
| 7.1 | Create release version | Version Tag |
| 7.2 | Complete production readiness checklist | Checklist |
| 7.3 | Submit to ARE for review | Submission |
| 7.4 | ARE reviews and approves | Approval |
| 7.5 | Deploy to staging | Deployment |
| 7.6 | Canary deployment | Canary Config |
| 7.7 | Full production deployment | Deployment |

### Outputs

- Production deployment
- Operability contract

---

## Phase 8: Operate & Monitor (ARE, COS)

**Desks:** [Agent Operations Desk](../../ux-architecture/desks/agent-operations-desk/README.md), [Cognitive Health Desk](../../ux-architecture/desks/cognitive-health-desk/README.md)

### Activities

| Step | Action | Responsible |
|------|--------|-------------|
| 8.1 | Monitor health metrics | ARE |
| 8.2 | Monitor cognitive quality | COS |
| 8.3 | Respond to incidents | ARE |
| 8.4 | Route cognitive issues | COS |

### Outputs

- Operating agent
- Health baselines
- Behavioral baselines

---

## Key Handoffs

| From | To | Artifact | Validation |
|------|-----|----------|------------|
| APO | ARAO | Autonomy Proposal | Risk assessment |
| ARAO | CSA | Approved Ceiling | Authority confirmation |
| CSA | AE | Design Spec | Design review |
| AE | CSA | Implementation | Design validation |
| AE | ARE | Release Candidate | Production readiness |
| ARE | COS | Deployed Agent | Baseline establishment |

---

## OPDA Checkpoints

| Phase | Observable | Predictable | Directable | Authority |
|-------|------------|-------------|------------|-----------|
| Design | Trace requirements | Pattern constraints | Escalation paths | Authority boundaries |
| Build | Telemetry implemented | Tests defined | Safety hooks | Bounds implemented |
| Release | Deployment visible | SLA defined | Kill switch ready | Ceiling enforced |
| Operate | Health monitored | Baselines set | Controls available | Violations detected |

---

## Success Criteria

- [ ] Agent charter approved by APO
- [ ] Autonomy ceiling approved by ARAO
- [ ] Design validated by CSA
- [ ] All tests passing
- [ ] Production readiness checklist complete
- [ ] ARE sign-off obtained
- [ ] Agent deployed to production
- [ ] Baselines established

---

*This journey is the foundation for all agent development in Seer.*
