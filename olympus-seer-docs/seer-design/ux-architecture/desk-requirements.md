# Seer UX Architecture: Desk Requirements

> **Status:** 🟡 Draft — Requirements captured, detailed specs in desk folders  
> **Last Updated:** 2026-01-13  
> **Related:** [Role Definitions](../personas-and-needs/roles.md) | [Hub UX Architecture](../../../olympus-hub-docs/06-ux-architecture/README.md)

---

## Overview

This document provides a requirements overview for Seer persona desks. **Detailed specifications for each desk are now in the `desks/` folder.**

Each persona requires:
- **Desk** — Primary operational console
- **Consoles** — Functional views within the desk
- **Journeys** — Key workflows the persona must complete
- **Channels** — Access methods (Web, CLI, MCP, REST)

Seer UX follows the same (Persona, Channel, Use Case) meta approach as Hub.

---

## Persona-to-Desk Mapping

| Persona | Desk | Primary Focus | Detailed Spec |
|---------|------|---------------|---------------|
| Automation Product Owner (APO) | **Agent Portfolio Desk** | Business outcomes, autonomy management | [View](./desks/agent-portfolio-desk/README.md) |
| Cognitive Systems Architect (CSA) | **Agent Design Desk** | Architecture, patterns, validation | [View](./desks/agent-design-desk/README.md) |
| Agent Engineer (AE) | **Agent Development Desk** | Build, test, deploy | [View](./desks/agent-development-desk/README.md) |
| Knowledge & Memory Owner (KMO) | **Knowledge Governance Desk** | Curate, govern, promote | [View](./desks/knowledge-governance-desk/README.md) |
| Agent Reliability Engineer (ARE) | **Agent Operations Desk** | Observe, control, recover | [View](./desks/agent-operations-desk/README.md) |
| Cognitive Operations Steward (COS) | **Cognitive Health Desk** | Monitor, detect, route | [View](./desks/cognitive-health-desk/README.md) |
| AI Risk & Audit Owner (ARAO) | **Agent Compliance Desk** | Approve, audit, enforce | [View](./desks/agent-compliance-desk/README.md) |

---

## Desk Summary

### 1. Agent Portfolio Desk (APO)

**Purpose:** Manage agent portfolio, track business outcomes, and govern autonomy requests.

**Consoles:**
| Console | Purpose | Spec |
|---------|---------|------|
| Portfolio Console | Agent catalog, ownership, status, roadmap | [View](./desks/agent-portfolio-desk/portfolio-console.md) |
| Outcomes Console | Business KPIs, value tracking, ROI | [View](./desks/agent-portfolio-desk/outcomes-console.md) |
| Autonomy Console | Proposals, approvals, policy management | [View](./desks/agent-portfolio-desk/autonomy-console.md) |

**REST Channel:** [APO Channel](./rest-channels/apo-channel.md)

---

### 2. Agent Design Desk (CSA)

**Purpose:** Design agent architectures, define patterns, validate implementations.

**Consoles:**
| Console | Purpose | Spec |
|---------|---------|------|
| Design Console | Architecture, patterns, failure modes | [View](./desks/agent-design-desk/design-console.md) |
| Topology Console | Multi-agent interactions and coordination | [View](./desks/agent-design-desk/topology-console.md) |
| Validation Console | Implementation review and sign-off | [View](./desks/agent-design-desk/validation-console.md) |

**REST Channel:** [CSA Channel](./rest-channels/csa-channel.md)

---

### 3. Agent Development Desk (AE)

**Purpose:** Build, test, and deploy agents with proper operability contracts.

**Consoles:**
| Console | Purpose | Spec |
|---------|---------|------|
| Development Console | Code, prompts, workflows, tool bindings, telemetry | [View](./desks/agent-development-desk/development-console.md) |
| Test Console | Behavioral, integration, and stress testing | [View](./desks/agent-development-desk/test-console.md) |
| Release Console | Versioning, deployment, ARE handoff | [View](./desks/agent-development-desk/release-console.md) |

**REST Channel:** [AE Channel](./rest-channels/ae-channel.md)

---

### 4. Knowledge Governance Desk (KMO)

**Purpose:** Curate knowledge, govern memory, manage enterprise learning.

**Consoles:**
| Console | Purpose | Spec |
|---------|---------|------|
| Knowledge Console | Sources, catalog, quality | [View](./desks/knowledge-governance-desk/knowledge-console.md) |
| Memory Console | Policies, retention, access | [View](./desks/knowledge-governance-desk/memory-console.md) |
| Learning Console | Promotion queue, enterprise learning | [View](./desks/knowledge-governance-desk/learning-console.md) |

**REST Channel:** [KMO Channel](./rest-channels/kmo-channel.md)

---

### 5. Agent Operations Desk (ARE)

**Purpose:** Operate agents safely, monitor health, respond to incidents.

**Consoles:**
| Console | Purpose | Spec |
|---------|---------|------|
| Health Console | AHS, metrics, SLOs | [View](./desks/agent-operations-desk/health-console.md) |
| Control Console | Levers, kill switches, bounds | [View](./desks/agent-operations-desk/control-console.md) |
| Incident Console | Triage, contain, recover, postmortem | [View](./desks/agent-operations-desk/incident-console.md) |

**REST Channel:** [ARE Channel](./rest-channels/are-channel.md)

---

### 6. Cognitive Health Desk (COS)

**Purpose:** Monitor agent behavior, detect drift, route issues to owners.

**Consoles:**
| Console | Purpose | Spec |
|---------|---------|------|
| Behavior Console | Quality signals, consistency, confidence | [View](./desks/cognitive-health-desk/behavior-console.md) |
| Patterns Console | Drift, anomalies, learning candidates | [View](./desks/cognitive-health-desk/patterns-console.md) |
| Issues Console | Issue triage and handoff | [View](./desks/cognitive-health-desk/issues-console.md) |

**REST Channel:** [COS Channel](./rest-channels/cos-channel.md)

---

### 7. Agent Compliance Desk (ARAO)

**Purpose:** Approve autonomy, ensure compliance, maintain audit readiness.

**Consoles:**
| Console | Purpose | Spec |
|---------|---------|------|
| Autonomy Console | Approval queue, policy review | [View](./desks/agent-compliance-desk/autonomy-console.md) |
| Compliance Console | Violations, investigations, evidence | [View](./desks/agent-compliance-desk/compliance-console.md) |
| Security Console | AI security posture, risk register | [View](./desks/agent-compliance-desk/security-console.md) |

**REST Channel:** [ARAO Channel](./rest-channels/arao-channel.md)

---

## Shared Components

### Common Consoles

Consoles that appear in multiple desks with appropriate permissions:

| Console | Description | Spec |
|---------|-------------|------|
| Agent Behavior Console | Cross-persona behavior analysis (COS, ARE, AE) | [View](./common-consoles/agent-behavior-console.md) |

See [Common Consoles Overview](./common-consoles/README.md) for details.

### Common Channels

| Channel | Description |
|---------|-------------|
| **Seer Web Portal** | Primary web access for all desks |
| **Seer CLI** | Command-line tools for AE, ARE |
| **Seer MCP Server** | AI assistant access |
| **Seer REST API** | Programmatic access — see [REST Channels](./rest-channels/README.md) |
| **Watch Integration** | Observability dashboards |

---

## OPDA Coverage

Each desk contributes to the OPDA framework:

| Desk | Observable | Predictable | Directable | Authority Enforceable |
|------|------------|-------------|------------|----------------------|
| Agent Portfolio | Agent visibility | Outcome targets | Priority changes | Autonomy governance |
| Agent Design | Design patterns | Pattern constraints | Design validation | Authority boundaries |
| Agent Development | Telemetry implementation | Test validation | Feedback handling | Bound implementation |
| Knowledge Governance | Knowledge quality | Promotion criteria | Source controls | Memory governance |
| Agent Operations | Fleet health | SLA guarantees | Kill/throttle/rollback | N/A |
| Cognitive Health | Reasoning traces | Quality baselines | Issue routing | N/A |
| Agent Compliance | Audit trails | Policy enforcement | Permission management | Core authority enforcement |

---

## Integration with Hub

Seer desks integrate with Hub desks where responsibilities overlap:

| Seer Persona | Hub Integration Point |
|--------------|----------------------|
| ARE | Hub SRE Ops Center (infrastructure layer) |
| AE | Workbench Studio (scenario binding) |
| KMO | Knowledge Base Console (content sync) |
| COS | Steward Desk (behavior alerts) |

See [Seer and Hub UX Integration](./seer-and-hub-ux-integration.md) for details.

---

## Next Steps

Detailed specifications for each desk are complete. Remaining work:
1. ~~Console wireframes~~ ✅ Indicative wireframes included in console docs
2. ~~API contracts~~ ✅ REST channels documented
3. Permission model implementation
4. Alert definitions
5. Integration specifications

---

*Status: 🟡 Draft — Requirements captured, detailed specs in desk folders*
