# ARAO Need: Audit Readiness and Evidence Requirements

> **Status:** Reference Document  
> **Last Updated:** 2026-01-13  
> **Related:** [ARAO Role Definition](../arao.md) | [Roles Overview](../roles.md#7-ai-risk--audit-owner-arao)

---

## Overview

The **AI Risk & Audit Owner (ARAO)** ([role definition](../roles.md#7-ai-risk--audit-owner-arao)) must ensure that agents are **defensible** to regulators, auditors, and stakeholders. This requires maintaining **continuous audit readiness** — the ability to explain and justify agent decisions at any time.

This document details the audit readiness and evidence requirements for platform developers building ARAO capabilities.

---

## Why Audit Readiness Matters

### Traditional Software vs. AI Agents

| Traditional Software | AI Agents |
|---------------------|-----------|
| Deterministic logic | Probabilistic reasoning |
| Code explains behavior | Model behavior is emergent |
| Same input → same output | Same input → possibly different output |
| Debug with stack traces | Debug with reasoning traces |
| Audit code | Audit decisions |

### Audit Scenarios

ARAO must be prepared for:

| Scenario | Trigger | Time Pressure |
|----------|---------|---------------|
| **Regulatory Audit** | Scheduled or surprise | Days to weeks |
| **Internal Audit** | Risk committee request | Weeks |
| **Incident Investigation** | Agent made a bad decision | Hours |
| **Customer Complaint** | "Why did the agent do this?" | Hours to days |
| **Legal Discovery** | Litigation | Days |

---

## Evidence Requirements

### Types of Evidence

ARAO requires access to multiple evidence types:

| Evidence Type | What It Contains | Retention |
|---------------|------------------|-----------|
| **Decision Records** | What the agent decided and why | 7 years |
| **Evidence Bundles** | Supporting data for decisions | 7 years |
| **Outcome Records** | What happened as a result | 7 years |
| **Override Records** | Human interventions | 7 years |
| **Control Evidence** | Guardrails that fired | 7 years |
| **Configuration Records** | Agent config at time of decision | 7 years |

### Decision Records

Every significant agent decision must be recorded:

```yaml
decision_record:
  id: "dec-2026-01-13-abc123"
  timestamp: "2026-01-13T14:30:00Z"
  
  agent:
    id: "invoice-processor-v2"
    version: "2.3.1"
    employment_id: "emp-xyz789"
  
  task:
    id: "task-456"
    request_id: "req-789"
    type: "invoice_approval"
  
  decision:
    action: "approve_invoice"
    confidence: 0.92
    autonomy_level: "full"
  
  reasoning:
    steps:
      - "Extracted invoice amount: $750"
      - "Found matching PO: PO-12345"
      - "Vendor status: approved"
      - "All criteria met for auto-approval"
    context_used:
      - "invoice_data"
      - "po_database"
      - "vendor_registry"
  
  outcome:
    status: "completed"
    result: "invoice_paid"
    timestamp: "2026-01-13T14:35:00Z"
```

### Evidence Bundles

Evidence bundles contain the supporting data for decisions:

| Bundle Component | Purpose | Example |
|------------------|---------|---------|
| **Input Data** | What the agent received | Invoice document |
| **Context Data** | What context was available | Vendor history |
| **Retrieved Knowledge** | What knowledge was used | Approval policy |
| **Tool Outputs** | What tools returned | PO lookup result |
| **Intermediate Decisions** | Sub-decisions made | Amount validation |

### Override Records

When humans intervene, records must capture:

```yaml
override_record:
  id: "ovr-2026-01-13-def456"
  timestamp: "2026-01-13T15:00:00Z"
  
  decision_id: "dec-2026-01-13-abc123"
  original_decision: "approve_invoice"
  override_decision: "reject_invoice"
  
  overriding_user:
    id: "user-jane-smith"
    role: "Finance Manager"
  
  reason: "Vendor under investigation"
  
  context:
    - "Verbal instruction from compliance"
    - "Pending vendor audit"
```

---

## Audit Trail Requirements

### Completeness

Every agent interaction must have:

- [ ] Unique identifier (traceable)
- [ ] Timestamp (when did it happen)
- [ ] Agent identity (which agent, which version)
- [ ] Task context (what was the task)
- [ ] Decision (what was decided)
- [ ] Reasoning (why was it decided)
- [ ] Outcome (what happened)
- [ ] Overrides (did humans intervene)

### Integrity

Audit trails must be:

| Property | Requirement | Implementation |
|----------|-------------|----------------|
| **Immutable** | Cannot be modified | Write-once storage |
| **Tamper-Evident** | Changes detectable | Cryptographic hashing |
| **Complete** | No gaps | Continuous logging |
| **Accessible** | Retrievable when needed | Indexed storage |

### Query Capabilities

ARAO must be able to query:

| Query Type | Example | Use Case |
|------------|---------|----------|
| **By Agent** | "All decisions by invoice-processor" | Agent-specific audit |
| **By Time Range** | "Decisions from Q1 2026" | Period-based audit |
| **By Decision Type** | "All approval decisions" | Process audit |
| **By Outcome** | "Decisions that were overridden" | Quality audit |
| **By User** | "Decisions affecting customer X" | Customer inquiry |
| **By Risk Level** | "High-confidence rejections" | Risk audit |

---

## Explainability Requirements

### What Must Be Explainable

| Question | Who Asks | Evidence Needed |
|----------|----------|-----------------|
| "Why did the agent decide X?" | Regulators | Decision record + reasoning |
| "What data influenced the decision?" | Auditors | Evidence bundle |
| "Was this decision within policy?" | Compliance | Policy mapping + control evidence |
| "Who approved this autonomy?" | Executives | Autonomy approval record |
| "Were controls in place?" | Security | Control evidence |

### Explanation Levels

ARAO must support multiple explanation levels:

| Level | Audience | Content |
|-------|----------|---------|
| **Executive Summary** | Leadership | High-level outcome and compliance |
| **Regulatory Detail** | Regulators | Policy mapping, controls, evidence |
| **Technical Detail** | Auditors | Full reasoning trace, data lineage |
| **Customer Facing** | Customers | Plain-language explanation |

### Platform Requirements

ARAO needs:
- **Explanation Generator** — Produce explanations at different levels
- **Policy Mapper** — Link decisions to policies
- **Evidence Assembler** — Compile evidence packages
- **Export Tools** — Export for external auditors

---

## Policy Compliance Tracking

### Policy Framework

ARAO maintains a policy framework that maps:

```
Policy Domain → Policy Requirements → Agent Behaviors → Compliance Checks
```

### Policy Domains

| Domain | Example Policies | Compliance Evidence |
|--------|------------------|---------------------|
| **Data Privacy** | PII handling, consent, retention | Data access logs |
| **Financial** | Authorization limits, segregation | Decision records |
| **Customer** | Fair treatment, disclosure, accuracy | Interaction logs |
| **Employment** | Bias prevention, equity | Decision analysis |
| **Industry** | Sector-specific regulations | Compliance reports |

### Continuous Compliance Monitoring

ARAO needs real-time compliance monitoring:

| Monitoring Type | Method | Alert Threshold |
|-----------------|--------|-----------------|
| **Policy Violations** | Rule-based detection | Any violation |
| **Policy Drift** | Statistical analysis | Trend change |
| **Near-Misses** | Guardrail fires | Increasing frequency |
| **Audit Gaps** | Coverage analysis | Missing evidence |

### Platform Requirements

ARAO needs:
- **Policy Catalog** — All policies affecting agents
- **Compliance Rules** — Automated compliance checks
- **Violation Dashboard** — Real-time violation tracking
- **Compliance Reports** — Scheduled compliance reporting

---

## Security Evidence

### AI Security Posture

ARAO must validate security controls:

| Control Area | Evidence Required | Validation Method |
|--------------|-------------------|-------------------|
| **Prompt Injection Defense** | Block logs, attack attempts | Penetration testing |
| **Data Exfiltration Prevention** | Access logs, denied requests | Audit logs |
| **Tool Access Control** | Permission grants, denials | Access reviews |
| **Model Security** | Version integrity, unauthorized changes | Change logs |
| **Authentication** | Login records, failed attempts | Auth logs |

### Security Metrics

| Metric | What It Measures | Target |
|--------|------------------|--------|
| **Attack Detection Rate** | % of attacks detected | > 99% |
| **False Positive Rate** | % of legitimate requests blocked | < 1% |
| **Time to Detect** | How fast attacks are detected | < 1 minute |
| **Time to Block** | How fast attacks are blocked | < 5 minutes |
| **Control Coverage** | % of agents with controls | 100% |

### Platform Requirements

ARAO needs:
- **Security Dashboard** — Real-time security posture
- **Attack Logs** — All security events
- **Penetration Test Results** — Regular security testing
- **Risk Register** — Track and manage risks

---

## Autonomy Approval Evidence

### Approval Records

Every autonomy approval must be recorded:

```yaml
autonomy_approval:
  id: "apv-2026-01-13-ghi789"
  timestamp: "2026-01-13T10:00:00Z"
  
  agent_id: "invoice-processor-v2"
  
  proposal:
    proposed_by: "user-john-doe"
    proposed_by_role: "APO"
    proposed_level: "full"
    scope:
      - "Approve invoices < $1000"
      - "Matching PO required"
    justification: "80% time reduction expected"
  
  review:
    reviewed_by: "user-sarah-audit"
    reviewed_by_role: "ARAO"
    review_date: "2026-01-12"
    risk_assessment: "Low"
    required_controls:
      - "Daily transaction limit: $50,000"
      - "Single transaction limit: $1,000"
      - "Override logging required"
  
  decision:
    status: "approved"
    effective_date: "2026-01-15"
    expiration_date: "2026-07-15"
    re_review_date: "2026-07-01"
  
  conditions:
    - "Monthly compliance review required"
    - "Immediate revocation if error rate > 2%"
```

### Approval Lifecycle Tracking

ARAO must track the full autonomy lifecycle:

```
Proposal submitted
       ↓
ARAO review begins
       ↓
Risk assessment completed
       ↓
Control requirements defined
       ↓
Decision: Approved / Rejected
       ↓
If approved: Implementation validated
       ↓
Ongoing compliance monitoring
       ↓
Periodic re-review
       ↓
Renewal / Revocation
```

### Platform Requirements

ARAO needs:
- **Approval Workflow** — Structured approval process
- **Risk Assessment Tools** — Standardized risk evaluation
- **Approval History** — Complete approval records
- **Re-Review Scheduler** — Automatic re-review reminders

---

## OPDA Requirements Summary

| OPDA Dimension | ARAO Need |
|----------------|-----------|
| **Observable** | Full visibility into agent decisions and evidence |
| **Predictable** | Consistent compliance with approved policies |
| **Directable** | Autonomy approval and revocation authority |
| **Authority Enforceable** | Policy enforcement and violation detection |

---

## Desk Support

These needs are supported through the **Agent Compliance Desk**:

| Console | Capabilities |
|---------|--------------|
| **Autonomy Console** | Approval queue, proposal review, decision history |
| **Compliance Console** | Violation dashboard, investigation queue, evidence browser |
| **Security Console** | Security dashboard, control inventory, risk register |

See [Agent Compliance Desk](../../ux-architecture/desks/agent-compliance-desk/README.md) for detailed specifications.

---

## Audit Preparation Checklist

Before any audit, ARAO should verify:

### Evidence Availability
- [ ] Decision records complete for audit period
- [ ] Evidence bundles accessible
- [ ] Override records captured
- [ ] Control evidence logged

### Policy Documentation
- [ ] Policy catalog up to date
- [ ] Agent-to-policy mapping complete
- [ ] Compliance rules documented
- [ ] Violation history available

### Security Posture
- [ ] Security controls documented
- [ ] Penetration test results current
- [ ] Risk register updated
- [ ] Incident history available

### Autonomy Documentation
- [ ] All autonomy approvals documented
- [ ] Current autonomy levels accurate
- [ ] Control implementation validated
- [ ] Re-reviews completed on schedule

---

## Anti-Patterns

| Pattern | Why It's Problematic |
|---------|---------------------|
| "We can explain it if asked" | Explanations must be ready now |
| "Audit evidence can be assembled later" | Evidence must be captured continuously |
| "Controls are in place, trust me" | Controls must be evidenced |
| "The model is safe" | Safety must be demonstrated |
| "Compliance is a checklist" | Compliance is continuous |

---

## Success Criteria

ARAO audit readiness needs are met when:

- [ ] Every decision has a complete audit trail
- [ ] Evidence is accessible within minutes
- [ ] Explanations can be generated at multiple levels
- [ ] Policy compliance is monitored continuously
- [ ] Violations are detected and reported automatically
- [ ] Security posture is validated regularly
- [ ] Autonomy approvals have complete documentation
- [ ] Audits are non-events (evidence is ready)

---

*End of document*
