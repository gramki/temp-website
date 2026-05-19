# Processing Capability Template

**Type:** Capability Template
**Model:** Definition Model — Dimension 1 (PSD)
**Applies to:** Capabilities realized through background computation — triggered by events, schedules, or conditions; no synchronous human or system consumer awaiting a direct response.
**Used by:** Product Manager (PM-authored zone of the PSD — Product Draft phase)

---

## Purpose

This template guides a PM in specifying a **Processing Capability** within a PSD. A Processing Capability is one where the primary work happens asynchronously — the system reacts to a trigger, processes data, and produces an output without a consumer waiting for a synchronous response.

The PM specifies the business intent — what triggers the processing, what it produces, and what the reliability expectations are. The Architect maps to Systems and Components in the Technical Review phase.

---

## Capability Specification Fields (PM-authored)

### Capability Identity

| Field | Type | Guidance |
|---|---|---|
| Capability Name | String | What background processing does this capability perform? e.g., "Nightly Settlement Reconciliation" |
| Capability Template | Enum | `Processing` (selected) |
| Maturity (target) | Enum | `Alpha` / `Beta` / `Gamma` |
| Lifecycle Stage (target) | Enum | `Planned → Available` or `Available → Deprecated` |

### Processing Specification

| Field | Type | Guidance |
|---|---|---|
| Trigger | Text | What initiates this processing? (e.g., "Kafka event: payment.settled", "Cron: daily at 02:00 UTC", "Webhook from bank: file available on SFTP", "API call that dispatches to background queue") |
| Input Data | Text | What data is consumed? (business terms, not field names) e.g., "All settled payments for the business day from the payment ledger, matched against bank statement entries" |
| Processing Intent | Text | What does the processing do? (business description, not algorithm) e.g., "Matches each settled payment against the corresponding bank confirmation. Flags discrepancies for manual review. Marks matched payments as reconciled." |
| Output / Side Effects | Text | What does the processing produce or change? e.g., "Updated reconciliation status on each payment. Discrepancy report written to audit trail. Notification triggered for unmatched items." |
| Data Produced | Text | What new data records or events does this processing create? |
| SLA | Text | Processing time SLA: e.g., "Must complete within 2 hours of trigger," "Must process 100K payments within 4 hours" |
| Error Handling | Text | What happens when processing fails partially or fully? Retry behaviour, dead-letter handling, alerting expectations. |
| Idempotency | Text | What is the expected behaviour if this processing runs twice for the same input? |

### Capability Acceptance Criteria (PM-authored)

| Criterion | Type | Guidance |
|---|---|---|
| Trigger Response | Text | Processing starts within X seconds/minutes of the trigger |
| Completion SLA | Text | Processing completes within the specified SLA window |
| Data Accuracy | Text | Output data matches expected business rules (specify test cases) |
| Error Handling | Text | Partial failures are handled correctly; discrepancies are surfaced for review |
| Idempotency | Text | Re-running for the same input produces the same result without duplication |

---

## Notes for the Architect (Technical Review phase)

The Architect maps this Processing Capability to Systems and Components in Section 5 of the PSD. Common System contributions for Processing Capabilities:

- A **Batch Job** Component implements scheduled or triggered bulk processing
- An **Event-Driven Worker** Component handles event-stream processing
- An **Integration Adapter** Component connects to external data sources (SFTP, partner APIs)
- A **Data Store** Component holds intermediate or output state

---

## Example

**Capability:** "Nightly Settlement Reconciliation"
**Module:** Settlement Module (Record)
**Template:** Processing

| Field | Value |
|---|---|
| Trigger | Cron: daily at 02:00 UTC, after SWIFT MT940 file available on SFTP |
| Input Data | All payments with status "Cleared" for the settlement date; corresponding SWIFT MT940 entries |
| Processing Intent | Match each cleared payment against a SWIFT MT940 entry by reference number. Mark matched payments as "Reconciled." Flag unmatched payments as "Reconciliation Failed" with reason code. |
| Output | Payment status updates (Cleared → Reconciled or Reconciliation Failed); reconciliation summary report; Kafka event: `settlement.reconciliation.complete` with summary counts |
| SLA | Must complete within 3 hours of SWIFT file availability; process up to 500K transactions |
| Error Handling | Per-item failures are logged and flagged; overall job failure triggers PagerDuty alert and retries up to 3 times |
