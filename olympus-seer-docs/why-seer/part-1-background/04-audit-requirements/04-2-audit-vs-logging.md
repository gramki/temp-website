# 4.2 Audit Is Not Logging

*Understanding why extending logging infrastructure does not satisfy enterprise audit requirements.*

---

## Purpose

This subsection establishes the fundamental distinction between operational logging and enterprise audit. Many organizations approach audit requirements by extending their existing logging infrastructure—adding more fields, increasing retention periods, building better dashboards. This approach fails because logging and audit serve different purposes, have different consumers, and require different guarantees.

---

## Core Distinction

| Dimension | Operational Logging | Enterprise Audit |
|-----------|---------------------|------------------|
| **Purpose** | Debug and monitor systems | Defend and reconstruct decisions |
| **Primary consumer** | Engineers and operators | Regulators, auditors, legal |
| **Time horizon** | Days to weeks | Years to decades |
| **Mutability** | Mutable, rotated | Immutable, retained |
| **Content** | What happened | What happened AND why |
| **Integrity** | Best effort | Cryptographically verified |
| **Legal status** | Operational artifact | Evidentiary record |

---

## What Logging Provides

Operational logging is essential infrastructure for running systems. Good logging tells you:

| Question | Log Answer |
|----------|------------|
| *"Did the API call succeed?"* | HTTP status 200 |
| *"How long did it take?"* | Latency: 145ms |
| *"What error occurred?"* | NullPointerException at line 42 |
| *"When did the service restart?"* | Timestamp: 2024-01-15T14:30:00Z |

Logging is optimized for:

- **Debugging**: Finding what went wrong in code
- **Monitoring**: Tracking system health
- **Alerting**: Detecting anomalies
- **Performance**: Identifying bottlenecks

### Logging Characteristics

| Characteristic | Description |
|----------------|-------------|
| **High volume** | Thousands to millions of events per second |
| **Structured but flexible** | JSON, log lines, varied schemas |
| **Rotated** | Old logs deleted to manage storage |
| **Mutable** | Logs can be corrected or redacted |
| **System-focused** | What the system did, not why |

---

## What Audit Requires

Enterprise audit is fundamentally different. Audit tells you:

| Question | Audit Answer |
|----------|--------------|
| *"Why was this application denied?"* | Decision record with factors, evidence, reasoning |
| *"What did the agent know when it decided?"* | Context snapshot at decision time |
| *"Who approved this exception?"* | Override record with authority, justification |
| *"What happened to this case?"* | Complete timeline with outcomes |
| *"Can you prove this was reasonable?"* | Evidence bundle with all inputs |

Audit is optimized for:

- **Reconstruction**: Reproducing the decision context exactly
- **Explanation**: Providing human-understandable rationale
- **Defense**: Demonstrating reasonableness to regulators
- **Accountability**: Tracing decisions to responsible parties

### Audit Characteristics

| Characteristic | Description |
|----------------|-------------|
| **Lower volume** | Audit-relevant events only (decisions, overrides) |
| **Strictly structured** | Schema-validated records |
| **Retained** | 7+ years for regulatory compliance |
| **Immutable** | Records cannot be modified after creation |
| **Decision-focused** | Why decisions were made, not just what happened |

---

## Why Logging Cannot Become Audit

### 1. Reconstruction Problem

Logs capture system events. Audit requires reconstructing what an agent *knew* and *believed* at decision time.

**Log entry**:
```json
{
  "timestamp": "2024-01-15T14:30:00Z",
  "event": "credit_decision",
  "customer_id": "cust-12345",
  "result": "denied",
  "model_score": 0.42
}
```

**Audit record**:
```json
{
  "decision_id": "dec-67890",
  "timestamp": "2024-01-15T14:30:00Z",
  "decision": "deny_credit",
  "customer_ref": "cust-12345",
  "confidence": 0.42,
  "factors": [
    {"factor": "income_to_debt_ratio", "value": 0.62, "weight": 0.35},
    {"factor": "account_age", "value": "2_months", "weight": 0.25},
    {"factor": "payment_history", "value": "insufficient_data", "weight": 0.40}
  ],
  "evidence_bundle_ref": "evd-11111",
  "policy_ref": "credit-policy-v2.3",
  "alternatives_considered": ["conditional_approval", "manual_review"],
  "rationale": "Debt-to-income ratio exceeds threshold; insufficient payment history"
}
```

The log tells you what happened. The audit record tells you why.

### 2. Immutability Problem

Logs are routinely rotated, corrected, and redacted. This is appropriate for operational purposes but fatal for audit.

**Acceptable for logs**:
- Delete logs older than 30 days to manage storage
- Correct a log entry that contained an error
- Redact PII that was inadvertently logged

**Unacceptable for audit**:
- Any modification to historical records
- Deletion before retention period expires
- Correction without creating a new correction record

### 3. Schema Problem

Logs evolve over time. Fields are added, formats change, parsers update. This is normal for operational systems but creates audit liability.

**Log reality**:
- 2023: Logged `score`
- 2024: Changed to `model_score`
- 2025: Added `model_version`

**Audit requirement**:
- Every record must be interpretable using the schema that was current when it was created
- Schema changes must be versioned
- Historical records must remain readable

### 4. Evidence Chain Problem

Audit requires linking related records into evidence chains. Logs are typically independent events.

**Log approach**:
- Search logs for customer ID
- Manually correlate events
- Reconstruct timeline

**Audit approach**:
- Decision record links to evidence bundle
- Evidence bundle links to context snapshot
- Outcome record links back to decision
- Override record references original decision

The evidence chain must be explicit and traversable.

---

## The Reconstructed Explanation Problem

A common failure mode: organizations try to generate explanations after the fact from logs and current model state.

**Why this fails**:

| Issue | Problem |
|-------|---------|
| **Model drift** | Current model may behave differently than decision-time model |
| **Context loss** | What was in the prompt? What was retrieved? |
| **Policy changes** | Current policies may not reflect decision-time rules |
| **Evidence absence** | Some information may not have been logged |

Reconstructed explanations are suspect because they may not reflect the actual decision basis. Real-time capture is preferred because it documents what actually happened.

---

## Common Misconceptions

### Misconception 1: "We Just Need Longer Retention"

**The error**: Keep logs for 7 years instead of 30 days.

**Why it fails**: Longer retention of inadequate records does not make them adequate. If the log doesn't capture rationale at decision time, retaining it forever doesn't create rationale.

**The fix**: Capture audit records with appropriate structure at decision time.

### Misconception 2: "We Can Reconstruct from Data"

**The error**: If we have the transaction data, we can replay the decision.

**Why it fails**: The decision was made with a specific model version, specific retrieved context, specific policies, and specific agent state. Reconstructing exactly that state is often impossible.

**The fix**: Capture context snapshots at decision time.

### Misconception 3: "Our SIEM Is Our Audit System"

**The error**: Security Information and Event Management systems are designed for audit.

**Why it fails**: SIEMs are optimized for security monitoring, threat detection, and compliance reporting. They are not optimized for decision reconstruction, explanation generation, or evidence bundling.

**The fix**: Implement purpose-built audit infrastructure for cognitive systems.

---

## Practical Implications

### Logging vs. Audit: When to Use Each

| Use Case | System | Why |
|----------|--------|-----|
| Debug a failed API call | Logging | System behavior, not decision |
| Explain why credit was denied | Audit | Decision rationale for customer |
| Track request latency | Logging | Operational monitoring |
| Respond to regulator inquiry | Audit | Evidence package |
| Alert on error spike | Logging | Operational health |
| Link decision to outcome | Audit | Model performance |

### Building Both Systems

Enterprise agent platforms need both:

1. **Logging infrastructure** for operations, debugging, and monitoring
2. **Audit infrastructure** for decision capture, explanation, and evidence management

These systems have different requirements and should be designed separately, though they may share some underlying infrastructure.

---

## Cross-References

- **Section 4.3**: The Cognitive Audit Fabric provides the audit infrastructure
- **Section 4.4**: Immutability and tamper evidence mechanisms
- **Section 3.4**: Memory governance imperatives (immutability, retention)
- **Part 2, Section 7**: Runtime and observability in Seer

For implementation patterns, see:
- `olympus-hub-docs/04-subsystems/cognitive-audit-fabric/README.md`

---

*Audit is not logging with longer retention. It is a distinct discipline with different purposes, different consumers, and different guarantees. Extending logging does not satisfy audit requirements.*
