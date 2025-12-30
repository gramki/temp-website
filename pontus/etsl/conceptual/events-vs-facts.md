## Fact Modeling vs Event Modeling  
### For ETSL Engineers and Enterprise Data Architects

---

## 1. Purpose of This Guidance

This note provides **clear, operational guidance** on how to model **Facts** and **Events** within the Enterprise Truth & Semantics Layer (ETSL).

Misunderstanding or conflating these two units is one of the **most common and damaging failures** in enterprise-scale data architectures. This guidance exists to ensure:

- Semantic clarity
- Durable enterprise truth
- Explainability and auditability
- Stable state derivation
- Long-term scalability of data engineering

---

## 2. Core Definitions (Non-Negotiable)

### Fact
A **Fact** is a *semantically asserted truth* about the enterprise, valid from a point in time, and attributable to an explicit authority.

> Facts define **what is (or became) true** in enterprise reality.

---

### Event
An **Event** is a *temporal occurrence* that represents **what happened**, explaining **why or how** one or more facts came into existence or changed.

> Events explain **how reality changed**.

> **Clarification:** An Event is an **assertion** in the ETSL realm. Like all ETSL assertions, it must carry source, authority, and time. Events are not external system logs or application telemetry—they are governed semantic constructs subject to ETSL's authority and lineage requirements.

---

## 3. The Fundamental Distinction

| Dimension | Fact | Event |
|---------|------|-------|
| Primary question | What is true? | What happened? |
| Nature | Declarative | Narrative |
| Semantic role | Truth | Explanation |
| Time semantics | Effective time | Occurrence time |
| Authority | Explicit (asserted) | Explicit (derived or induced) |
| Mutability | Immutable | Immutable |

**Key rule:**  
> **Events cause facts. Facts define reality.**

> **Note on Authority:** Both Facts and Events are ETSL artifacts and must have authority attributed. For Facts, authority is explicitly asserted. For Events, authority is derived or induced from the event context (see Section 8). Source (who emitted) is distinct from authority (who has the mandate).

---

## 4. How Facts and Events Relate

### Enterprise Reality Flow

Event  →  Fact(s)  →  State

- **Event**: A meaningful occurrence
- **Fact**: An authoritative assertion derived from it
- **State**: Current enterprise reality derived from facts

### Example

Event: CreditLimitChanged
occurred_at = T1
initiated_by = SystemX

Fact: CreditLimit = 20,000
effective_from = T1
authority = CreditPolicy

The fact exists *because of* the event, but is modeled independently.

---

## 5. Fact Modeling Guidance

### 5.1 What Qualifies as a Fact

A fact must:
- Assert something that is true
- Be attributable to an authority
- Have an effective time
- Persist until superseded or contradicted

**Examples**
- Account A is OPEN as of T
- Obligation O exists between Party P and Bank B
- RiskRating of Party P is HIGH as of T

---

### 5.2 Fact Modeling DOs

✅ Model facts as **assertions**, not operations  
✅ Include:
- Subject
- Predicate
- Object / Value
- Effective time
- Authority  
✅ Make facts **append-only**  
✅ Allow **multiple facts over time** for the same subject  

---

### 5.3 Fact Modeling DON’Ts

❌ Do not encode workflow or process logic  
❌ Do not embed system behavior  
❌ Do not overwrite or delete facts  
❌ Do not assume facts are always numeric or scalar  

---

## 6. Event Modeling Guidance

### 6.1 What Qualifies as an Event

An event must:
- Represent something that occurred
- Have an occurrence time
- Reference affected entities
- Be semantically meaningful at the business level

**Examples**
- AccountOpened
- ObligationCreated
- LimitAdjusted
- DecisionOverridden

---

### 6.2 Event Modeling DOs

✅ Use **past tense** naming  
✅ Keep payloads **minimal and referential**  
✅ Include:
- Occurred_at
- Actor / Source
- Correlation identifiers  
✅ Version event schemas explicitly  

---

### 6.3 Event Modeling DON’Ts

❌ Do not model DB operations or API calls as events  
❌ Do not embed full entity snapshots  
❌ Do not overload events with inferred meaning  
❌ Do not treat events as state  

---

## 7. Temporal Semantics (Critical Distinction)

| Aspect | Fact | Event |
|------|------|-------|
| Time dimension | Effective time | Occurrence time |
| Corrections | New fact | New event |
| Backdating | Allowed (controlled) | Rare |
| As-of queries | Natural | Derived |

**Rule of thumb**
- Facts answer: *What was true as of T?*
- Events answer: *What happened at T?*

---

## 8. Authority and Governance

Both Facts and Events are ETSL artifacts and **must have authority attributed**. However, the nature and derivation of authority differs.

### Fact Authority
- **Explicitly asserted** at the time of assertion
- Business- or policy-owned
- Stable over time
- Directly modeled in the Authority Registry

### Event Authority
- **Derived or induced** from event context
- Authority is determined from the event's domain, type, or originating function
- May be derived from the Assertion Source's registered authority
- Still explicit once derived—not optional or implicit

### Source vs Authority (Critical Distinction)

| Concept | Definition | Example |
|---------|------------|---------|
| **Source** | The system, application, or process that emitted the event | Core Banking System |
| **Authority** | The enterprise function with the mandate to assert this type of truth | Account Operations |

Source and authority are **not the same**. A single source may emit events on behalf of multiple authorities. Authority must be explicitly resolved, not inferred from source alone.

### Derivation Patterns for Event Authority

| Pattern | Description | When to Use |
|---------|-------------|-------------|
| **Source-registered** | Source is registered in Authority Registry with explicit authority mappings | Well-governed, stable sources |
| **Event-type-based** | Authority is determined by event type (e.g., all `CreditLimitChanged` events → Credit Policy authority) | When event types map cleanly to functional authority |
| **Domain-induced** | Authority is induced from the domain that owns the event stream | Domain-aligned architectures |

Regardless of derivation method, the resulting authority must be **explicit and auditable**.

### Governance Implication

> Both Facts and Events require authority governance. Facts typically have stricter assertion-time governance; Events require clear derivation rules that are governed at design time.

---

## 9. Storage Implications (ETSL-Aligned)

| Aspect | Facts | Events |
|------|-------|--------|
| Mutability | Append-only | Append-only |
| Volume | Moderate | High |
| Retention | Long-term | Long-term |
| Query pattern | State derivation | Causal analysis |
| Consumers | Broad | Selective |

Events optimize **flow and causality**.  
Facts optimize **truth and reconstruction**.

---

## 10. Common Anti-Patterns (Avoid at All Costs)

❌ Treating events as current state  
❌ Treating facts as transactional logs  
❌ Using “Updated” events with large payloads  
❌ Persisting derived facts only inside projections  
❌ Encoding semantic meaning inside pipelines  

---

## 11. Validation Tests (Use These)

### Test 1 – Truth Reconstruction
> If all projections are deleted, can enterprise reality be reconstructed from facts **without replaying code**?

If no → facts are insufficient.

---

### Test 2 – Explainability
> If all events are deleted, can you still explain **why** a fact exists?

If no → events are insufficient.

---

## 12. Canonical Principle for ETSL Engineers

> **Facts establish enterprise truth. Events explain how that truth came to be.  
They must be modeled explicitly, governed independently, and never conflated.**

---

## 13. Summary

- Events are about **happening**
- Facts are about **being true**
- State is derived from facts
- Explainability comes from events
- ETSL requires **both**, modeled with discipline

Failure to respect this separation leads to fragile systems, unexplainable decisions, and escalating data engineering costs.

---

---

# Appendix A  
## Event Provenance and Fact Justification  

---

## A.1 Purpose of This Appendix

This appendix extends the **Fact vs Event Modeling Guidance** by addressing a subtle but critical question:

> **Should a fact refer to the event that caused it?**

At enterprise scale, the answer is **yes, but only with discipline**.  
Incorrect modeling of provenance creates brittle schemas, semantic coupling, and audit fragility.  
This appendix defines the **correct ETSL pattern** for preserving causality and explainability **without compromising semantic independence**.

---

## A.2 Executive Summary

- Event provenance is **relevant and valuable** for audit, explainability, and forensics
- Facts must **never depend** on the continued availability or structure of events
- Provenance must be modeled as **justification**, not causation
- Justification references are **optional, referential, and opaque**
- Facts remain authoritative even if events are archived or unavailable

---

## A.3 Why Event Provenance Matters

Event provenance enables:

1. **Auditability**  
   - Why does this fact exist?
   - What triggered the change?

2. **Explainability**  
   - Especially for decisions, overrides, and regulatory outcomes

3. **Operational Forensics**  
   - Tracing incorrect or disputed state changes

4. **Regulatory Reconstruction**  
   - Rebuilding causal chains for a given point in time

However, provenance must not become **semantic dependency**.

---

## A.4 Core Modeling Principle

> **Facts assert enterprise truth.  
> Events explain causality.  
> Provenance links the two without entangling them.**

A fact must remain:
- Semantically complete
- Independently queryable
- Valid without requiring access to event payloads

---

## A.5 What Not to Do (Anti-Patterns)

### ❌ Embedding Event Semantics Inside Facts

```text
Fact:
  credit_limit = 20000
  caused_by_event_type = CreditLimitChanged
  caused_by_event_payload = {...}

Why this fails:
	•	Couples fact schema to event schema
	•	Makes facts fragile under event evolution
	•	Breaks independence of enterprise truth

⸻

A.6 The Correct Pattern: Fact Justification References

Facts may carry lightweight, optional references to their justification.

A.6.1 Minimal Fact Schema (Illustrative)

Fact:
  subject_id
  predicate
  value
  effective_from
  authority
  justification_ref (optional)

A.6.2 Justification Reference Characteristics
	•	Referential, not semantic
	•	Opaque identifiers
	•	Nullable / optional
	•	No assumptions about event structure

Example:

justification_ref:
  - event_id: EVT-12345
  - decision_id: DEC-67890


⸻

A.7 One-to-Many and Non-Event Justifications

A fact may be justified by:
	•	A single event
	•	Multiple events
	•	A decision derived from many events
	•	A policy or regulatory rule
	•	A manual or supervisory override

Therefore:
	•	Do not assume 1:1 event-to-fact mapping
	•	Support 0 → N justification references

⸻

A.8 Preferred Pattern: Indirect Justification via Decision Records

For inferred or evaluated facts, enterprises prefer:

Decision:
  decision_id
  inputs: [event_ids]
  logic_version
  outcome

Fact:
  value
  justification_decision_id

Benefits:
	•	Preserves explainability
	•	Enables reproducibility
	•	Avoids overloading facts with derivation logic

⸻

A.9 External and Non-Event Justifications

Some facts are justified by:
	•	Regulations
	•	Policies
	•	Legal agreements
	•	Supervisory actions

Example:

Fact:
  authority = Compliance
  justification_ref = REG-2024-AML-17

This ensures:
	•	Audit clarity
	•	Legal defensibility
	•	Independence from system-generated events

⸻

A.10 Hard Rules for ETSL Engineers

❌ Do not require an event reference for a fact to be valid
❌ Do not assume every fact change is event-driven
❌ Do not embed event semantics or payloads inside facts
❌ Do not force facts to be queried through events

⸻

A.11 Storage and Query Guidance
	•	Operational queries
	•	Read facts and state directly
	•	Audit and explainability
	•	Join facts → justification → events/decisions
	•	Archival scenarios
	•	Facts remain authoritative even if events are cold-stored

⸻

A.12 Validation Test (Mandatory)

Ask:

If all events are archived or unavailable, does this fact still remain authoritative and meaningful?

If the answer is no, the model violates ETSL principles.

⸻

A.13 Canonical Rule to Codify

Facts may carry optional justification references to events or decisions for audit and explainability, but they must remain semantically complete and authoritative independent of those references.

⸻

A.14 Closing Note

Event provenance strengthens ETSL only when modeled with restraint.
Over-linking erodes semantic stability; under-linking erodes trust.

A well-designed ETSL preserves truth without dependency and explanation without entanglement.

⸻


