# Agent Compliance Desk

> **Status:** 🟡 Draft  
> **Last Updated:** 2026-01-13  
> **Primary Persona:** [AI Risk & Audit Owner (ARAO)](../../../personas-and-needs/roles.md#7-ai-risk--audit-owner-arao)  
> **Related:** [ARAO Reference](../../../personas-and-needs/arao.md) | [ARAO Needs](../../../personas-and-needs/needs/arao-audit-readiness.md)

---

## Purpose

The Agent Compliance Desk is the primary workspace for the **AI Risk & Audit Owner (ARAO)** ([role definition](../../../personas-and-needs/roles.md#7-ai-risk--audit-owner-arao)). It provides capabilities to:

- Review and approve autonomy proposals
- Monitor compliance and investigate violations
- Maintain AI security posture
- Ensure audit readiness

---

## Consoles

| Console | Purpose | Documentation |
|---------|---------|---------------|
| **Autonomy Console** | Approval queue, proposal review | [autonomy-console.md](./autonomy-console.md) |
| **Compliance Console** | Violations, investigations, evidence | [compliance-console.md](./compliance-console.md) |
| **Security Console** | AI security posture, risk register | [security-console.md](./security-console.md) |

---

## Key Journeys

| Journey | Description | Consoles Used |
|---------|-------------|---------------|
| **Autonomy Review** | Evaluate APO proposal, approve or reject | Autonomy Console |
| **Compliance Investigation** | Investigate COS-flagged compliance concern | Compliance Console |
| **Audit Preparation** | Gather evidence, prepare for external audit | Compliance Console |
| **Security Assessment** | Validate AI security controls | Security Console |
| **Risk Management** | Track and manage agent-related risks | Security Console |

---

## OPDA Integration

The Agent Compliance Desk demonstrates OPDA capabilities for ARAO:

| OPDA | Capability | Console |
|------|------------|---------|
| **Observable** | Compliance status, audit trail completeness | Compliance Console |
| **Predictable** | Risk assessment, compliance forecasting | Security Console |
| **Directable** | Approval decisions, security control adjustment | Autonomy Console |
| **Authority Enforceable** | Autonomy approvals, policy enforcement | Autonomy Console, Compliance Console |

### How ARAO Actions, Assesses, and Evidences OPDA

| OPDA | ARAO Actions | ARAO Assesses | ARAO Evidences |
|------|--------------|---------------|----------------|
| **Observable** | Define audit requirements | Review evidence completeness | Audit trail reports |
| **Predictable** | Set compliance requirements | Monitor compliance trends | Compliance dashboards |
| **Directable** | Approve/reject autonomy | Verify control implementation | Approval records |
| **Authority Enforceable** | Define authority limits | Validate enforcement | Enforcement evidence |

---

## Channel Access

| Channel | Capabilities |
|---------|--------------|
| **Web UI** | Full desk access via Seer Portal |
| **REST API** | `/api/seer/arao/v1` — [API Documentation](../../rest-channels/arao-rest-channel.md) |
| **MCP** | `seer-arao-mcp` server for AI assistant integration |
| **Email** | Approval notifications |

---

## Integration Points

### Receives From

| Source | Data |
|--------|------|
| **APO** | Autonomy proposals |
| **COS** | Compliance concern issues |
| **KMO** | Sensitive knowledge promotion requests |
| **ARE** | Runtime compliance evidence |

### Sends To

| Destination | Data |
|-------------|------|
| **APO** | Approval decisions, control requirements |
| **ARE** | Approved autonomy for enforcement |
| **External Auditors** | Evidence packages |

---

## Indicative Layout

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  AGENT COMPLIANCE DESK                                     ARAO: Jordan P.  │
├─────────────────────────────────────────────────────────────────────────────┤
│  [Autonomy] [Compliance] [Security]                             🔔 🔍 ⚙️    │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  ┌──────────────────────────────────────────────────────────────────────┐   │
│  │ COMPLIANCE OVERVIEW                              Last Updated: 1h    │   │
│  ├──────────────────────────────────────────────────────────────────────┤   │
│  │                                                                       │   │
│  │  Policy Compliance │  Audit Readiness  │  Security Score │ Risk Level│   │
│  │   █████████░       │   ██████████      │   ████████░░    │  ███░░░░░░│   │
│  │      96%           │      100%         │      87%        │    Low    │   │
│  │   [Good]           │   [Ready]         │   [Good]        │  [Accept] │   │
│  │                                                                       │   │
│  └──────────────────────────────────────────────────────────────────────┘   │
│                                                                             │
│  ┌─────────────────────────────────────┐  ┌──────────────────────────────┐  │
│  │ APPROVAL QUEUE                [3]   │  │ OPEN INVESTIGATIONS    [2]   │  │
│  │                                     │  │                              │  │
│  │ 📋 invoice-processor               │  │ 🔍 Potential PII exposure    │  │
│  │    Autonomy: Suggest → Full        │  │    Agent: customer-service   │  │
│  │    Risk: Low │ From: APO (Jane)    │  │    Status: In Progress       │  │
│  │    [Review →]                       │  │                              │  │
│  │                                     │  │ 🔍 Unauthorized tool access  │  │
│  │ 📋 order-validator                 │  │    Agent: data-enricher      │  │
│  │    Autonomy: Ask → Suggest         │  │    Status: Evidence Review   │  │
│  │    Risk: Medium │ From: APO (Jane) │  │                              │  │
│  │    [Review →]                       │  │ [View All →]                 │  │
│  └─────────────────────────────────────┘  └──────────────────────────────┘  │
│                                                                             │
│  ┌──────────────────────────────────────────────────────────────────────┐   │
│  │ RECENT DECISIONS                                                      │   │
│  ├──────────────────────────────────────────────────────────────────────┤   │
│  │ ✅ APPROVED │ expense-approver │ Suggest → Full │ 2 conditions │ 2d  │   │
│  │ ❌ REJECTED │ data-enricher    │ Watch → Full   │ Risk too high │ 3d │   │
│  │ ✅ APPROVED │ customer-service │ Ask → Suggest  │ 1 condition  │ 5d  │   │
│  └──────────────────────────────────────────────────────────────────────┘   │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## Console Summaries

### Autonomy Console

Review and approve autonomy proposals.

**Sections:**
- **Approval Queue** — Pending autonomy proposals from APO
- **Proposal Detail** — Justification, risk analysis, controls
- **Decision Actions** — Approve, reject, request changes
- **Approval History** — All past decisions with rationale

**Key Features:**
- Risk scoring for proposals
- Control requirement checklist
- Conditional approval (with requirements)
- Expiration and re-review scheduling

[Full specification →](./autonomy-console.md)

---

### Compliance Console

Monitor and investigate compliance.

**Sections:**
- **Violation Dashboard** — Active and resolved violations
- **Investigation Queue** — COS-flagged compliance concerns
- **Evidence Browser** — Decision records, evidence bundles
- **Policy Mapping** — Agent behavior → policy requirements

**Key Features:**
- Violation severity classification
- Investigation workflow
- Evidence export for audits
- Remediation tracking

[Full specification →](./compliance-console.md)

---

### Security Console

AI security posture and risk management.

**Sections:**
- **Security Dashboard** — Overall AI security posture
- **Control Inventory** — Prompt injection, exfiltration, access controls
- **Penetration Test Results** — AI-specific security testing
- **Risk Register** — Track and manage agent-related risks

**Key Features:**
- Security control status
- Vulnerability tracking
- Risk scoring and prioritization
- Remediation timelines

[Full specification →](./security-console.md)

---

## REST API Overview

The ARAO REST channel provides programmatic access:

```
Base: /api/seer/arao/v1

Autonomy:
  GET    /proposals                - List proposals
  GET    /proposals/{id}           - Proposal details
  POST   /proposals/{id}/approve   - Approve proposal
  POST   /proposals/{id}/reject    - Reject proposal
  POST   /proposals/{id}/conditions - Add conditions
  GET    /approvals                - Approval history

Compliance:
  GET    /violations               - List violations
  GET    /violations/{id}          - Violation details
  POST   /investigations           - Start investigation
  GET    /investigations/{id}      - Investigation details
  PUT    /investigations/{id}      - Update investigation
  GET    /evidence                 - Browse evidence
  GET    /evidence/export          - Export for audit
  GET    /policies                 - Policy mappings

Security:
  GET    /security/posture         - Security posture
  GET    /security/controls        - Control inventory
  GET    /security/tests           - Penetration tests
  GET    /risks                    - Risk register
  POST   /risks                    - Add risk
  PUT    /risks/{id}               - Update risk
```

[Full API documentation →](../../rest-channels/arao-rest-channel.md)

---

*Status: 🟡 Draft — Overview and console specifications complete*
