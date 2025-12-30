# ETSL and Temporal Ordering
## Handling Out-of-Order Assertions and Corrections

**Audience:** Platform Architects, Data Engineers, ETSL Architects  
**Status:** Architectural Guidance Document

---

## 1. Purpose of This Document

This document provides conceptual guidance on how ETSL handles **out-of-order assertions** and **corrections**—two realities that arise regardless of whether assertions are ingested via batch or streaming.

It addresses:
- Why out-of-order is unavoidable
- How ETSL processes out-of-order assertions internally
- What ETSL delivers to consumers
- What consumers must expect and handle

This document is **technology-agnostic**. It does not prescribe streaming platforms, batch frameworks, or implementation patterns. Those are platform engineering concerns.

---

## 2. The Unavoidable Reality: Out-of-Order Assertions

### Why Out-of-Order Happens

Assertions rarely arrive in effective-time order. Causes include:

- **Multi-source federation:** Different Assertion Sources have different latencies
- **System retries and recovery:** Failed deliveries are re-sent later
- **Batch processing windows:** Batch jobs run on schedules, not real-time
- **Backdated corrections:** Legitimate business actions with past effective dates
- **Network and infrastructure variance:** Distributed systems have variable latency

> **Out-of-order is not a bug. It is a structural property of federated enterprise data.**

### The Three Times

ETSL distinguishes three time concepts:

| Time Concept | Definition | ETSL Usage |
|--------------|------------|------------|
| **Event Time** | When the business event occurred | Operational context |
| **Effective Time** | When the assertion becomes true | ETSL's primary time dimension |
| **Processing Time** | When ETSL processes the assertion | Internal operations only |

**ETSL operates on effective time.** Processing time is irrelevant to semantic truth. An assertion with effective time T is true as of T, regardless of when it was processed.

---

## 3. How ETSL Handles Out-of-Order Internally

### Ingress Processing

When an assertion arrives at the ETSL ingress boundary:

1. **Validation:** Authority, semantic type, temporal validity checks
2. **Effective time extraction:** The assertion's effective time is captured
3. **State impact assessment:** Does this assertion change current or past state?
4. **Reconciliation:** If conflicts exist, apply reconciliation patterns (see *Reconciliation Failure and Error Handling*)

### When Out-of-Order Changes State

If an assertion with effective time T₁ arrives after an assertion with effective time T₂ (where T₁ < T₂), and T₁ would have affected the state that was emitted based on T₂:

1. ETSL recomputes the affected state
2. ETSL emits a **correction** to the previously emitted state
3. The correction is **explicitly annotated** (see Section 5)
4. All **derived artifacts** within ETSL realm are also annotated

### Unhandled Out-of-Order

Not all out-of-order assertions can be automatically processed. When an out-of-order assertion cannot be resolved:

- The assertion is **side-channeled/quarantined** with full lineage
- **Alerts** are raised to Data Engineering and Operations
- **Resolution SLAs** apply (as defined in the Semantic Artifact)
- The assertion is held for manual or policy-based intervention

This is consistent with the error handling principle: **don't right-shift problems**.

---

## 4. What ETSL Delivers to Consumers

### Truth-as-Known

ETSL delivers **truth as it knows it at the time of emission**.

- Consumers never see "pending reconciliation" or "speculative" states
- If ETSL emits state, it is truth (until corrected)
- Reconciliation is an **internal ETSL concern**, not exposed to consumers

### Corrections Are Expected

Consumers must expect corrections. A correction is not an error—it is normal operation in a federated enterprise.

Corrections occur when:
- A late-arriving assertion changes previously emitted state
- A reconciliation conflict is resolved
- A backdated assertion legitimately alters past state

### Consumer Delivery is Source-Agnostic

ETSL may deliver updates via:
- Streaming interfaces (push-based)
- Query interfaces (pull-based)
- Materialized views (pre-computed)

**Consumer guidance is agnostic of source processing mode.** Whether the underlying ingress was batch or streaming is invisible to consumers. Consumers must handle corrections regardless of how ETSL received the original assertions.

---

## 5. Correction Semantics

### Corrections Are First-Class

A correction is not merely a new version of state. It is an **explicitly qualified** update that indicates:

- This update **replaces** a previously emitted state
- The reason is an assertion that arrived out of effective-time order
- The consumer should take appropriate action

### Correction Annotation

Every correction carries:

| Field | Purpose |
|-------|---------|
| `is_correction` | Boolean flag: this is a correction |
| `corrects_state_version` | Which prior state version is being corrected |
| `correction_reason` | Why the correction occurred (e.g., late_arrival, reconciliation_resolution) |
| `triggering_assertion_id` | The assertion that caused the correction |

### Lineage Propagation

When an out-of-order assertion changes an ETSL artifact:

1. The changed artifact is annotated as corrected
2. All **derived artifacts** in the ETSL realm that depend on it are also annotated
3. This propagation ensures consumers of derived artifacts know the upstream truth changed

> **Corrections propagate through lineage.** A consumer of a derived artifact must know when upstream truth changed, even if their direct artifact wasn't the one corrected.

---

## 6. Consumer Responsibilities

### No Guarantees on Arrival Order

ETSL provides **no guarantee** that state updates arrive in effective-time order. Consumers must handle this reality.

### Consumer Strategies

Consumers may adopt different strategies based on their use case:

| Strategy | Description | Use Case |
|----------|-------------|----------|
| **Accept** | Apply all updates including corrections | Dashboards, analytics, non-critical systems |
| **Ignore** | Discard corrections for past states | Point-in-time snapshots already committed |
| **Escalate** | Trigger intervention when corrections exceed threshold | Audit-sensitive systems |
| **Compensate** | Apply compensating actions for corrections | Transactional systems that acted on prior state |

The choice is **consumer-specific**. ETSL does not prescribe consumer behavior.

### Correction Handling is Mandatory

All consumers must be capable of receiving corrections. A consumer that cannot handle corrections cannot consume ETSL state reliably.

This is a **design requirement** for any system consuming ETSL.

---

## 7. Patterns for Reducing Out-of-Order Impact

Out-of-order cannot be eliminated, but its impact can be reduced through assertion-specific and source-specific patterns.

### At Ingress

| Pattern | Description | When to Use |
|---------|-------------|-------------|
| **Buffering window** | Hold assertions for a short period to absorb out-of-order arrivals | When source latency is predictable |
| **Reordering by effective time** | Sort assertions before processing | When ordering is feasible within SLA |
| **Source-specific tolerance** | Different sources have different allowed lateness | When source characteristics are well-understood |

These patterns are declared per-assertion or per-source, not globally.

### At State Derivation

| Pattern | Description | When to Use |
|---------|-------------|-------------|
| **Idempotent state computation** | State can be recomputed without side effects | Always recommended |
| **Versioned state** | Every state emission carries a version | Always required |
| **Correction batching** | Aggregate multiple corrections before emission | When correction frequency is high |

---

## 8. Banking Examples

### Example 1: Credit Limit Change Arrives Late

**Scenario:**
- At T₁ (10:00 AM), Risk reduces customer credit limit from $50,000 to $30,000
- At T₂ (10:05 AM), customer makes a $40,000 purchase, approved based on $50,000 limit
- At T₃ (10:10 AM), ETSL receives the T₁ assertion (delayed due to system issue)

**ETSL Behavior:**
1. ETSL processes the T₁ assertion
2. State as-of T₁ is corrected: credit limit was $30,000, not $50,000
3. A correction is emitted with explicit annotation
4. Downstream artifacts (e.g., available credit calculations) are also annotated

**Consumer Responsibility:**
- The fraud system consuming available credit must handle the correction
- It may trigger a review of the T₂ transaction that was approved on stale data

---

### Example 2: Batch Reconciliation Creates Corrections

**Scenario:**
- Throughout the day, streaming assertions update customer address
- Nightly batch from the master customer system arrives with authoritative address
- The batch assertion has effective time earlier than some streaming assertions

**ETSL Behavior:**
1. Batch assertion is processed like any other assertion
2. If it changes state that was emitted based on streaming assertions, corrections are emitted
3. Corrections are annotated with `correction_reason: late_arrival`

**Consumer Responsibility:**
- Consumers see corrections the next morning
- Downstream systems (e.g., address verification) handle corrections per their strategy

---

### Example 3: Regulatory Reporting with Corrections

**Scenario:**
- A regulatory report was generated at T based on ETSL state
- A correction arrives at T+2 hours for data in the reporting window

**ETSL Behavior:**
1. Correction is emitted with full annotation
2. The regulatory reporting system (a consumer) receives the correction

**Consumer Responsibility:**
- The regulatory system must decide: re-file, note for next filing, or escalate
- This is a **consumer policy decision**, not ETSL's concern

---

## 9. Relationship to Other ETSL Guidance

| Topic | Document |
|-------|----------|
| Reconciliation failure handling | *Building ETSL Data Artifacts*, Section 11 |
| Authority modeling | *ETSL Authority Modeling Guidance for Architects* |
| State derivation | *State Modeling* and *State Engineering* |
| Error lineage | *Building ETSL Data Artifacts*, Section 11.7 |

---

## 10. Summary Principles

1. **Out-of-order is unavoidable.** It is a structural property, not a bug.

2. **ETSL operates on effective time.** Processing time is irrelevant to truth.

3. **ETSL delivers truth-as-known.** No reconciliation states exposed to consumers.

4. **Corrections are first-class and explicit.** Not just versions — explicitly qualified.

5. **Corrections propagate through lineage.** Derived artifacts are also annotated.

6. **Consumers must handle corrections.** This is mandatory, not optional.

7. **No guarantees on arrival order.** Consumers must deal with this reality.

8. **Patterns are assertion/source-specific.** No global solution to out-of-order.

9. **Unhandled out-of-order is quarantined.** With alerts and SLAs, not silent failures.

---

