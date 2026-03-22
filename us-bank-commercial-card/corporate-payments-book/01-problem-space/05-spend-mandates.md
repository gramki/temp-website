# Chapter 5: Spend Mandates — The Authorization Envelope

Every corporate payment carries an implicit set of assertions. Someone decided this payment was allowed. Someone's authority backs it. A budget absorbs it. A policy governs it. A cost center claims it. A time window bounds it. An exception path exists if something goes wrong.

In most enterprises, these assertions are scattered — partly in approval emails, partly in ERP configurations, partly in policy documents, partly in the head of the person who signed off. The Spend Mandate makes them explicit.

**A Spend Mandate is the governing authorization envelope for spend. It defines why a payment is allowed, who authorized it, whose budget pays for it, which rules apply, how it must be booked, and who is accountable.**

The Spend Mandate is a thinking tool. It is not a system entity, not a database record, not an API object. It is a framework for reasoning about the governance requirements that every corporate payment must satisfy — and for understanding how those requirements distribute across the entities in the product ontology.

---

## Why the Mandate Exists

For any payment made on behalf of an enterprise, the finance function must be able to answer a chain of questions:

- **Why was this allowed?** Every payment exists for a business purpose — project delivery, department operations, client engagement, vendor obligation. A payment without a stated purpose is a payment that cannot be justified in audit.
- **Who authorized it?** Spend authority flows through an organizational hierarchy. Someone — a project manager, a cost center owner, a procurement head, a finance controller — holds the authority that permits this payment.
- **Whose budget paid for it?** Every payment draws from a financial allocation. That allocation belongs to a department, a project, a client engagement, or a functional budget. The payment must decrement the correct allocation.
- **Which rules applied?** The payment operated under a policy regime — procurement policy, travel policy, project spend policy, departmental approval thresholds. The applicable rules determine what was permissible.
- **How should it be booked?** The payment must be recorded in the enterprise's financial system — attributed to a cost center, coded to a GL account, classified as capex or opex, tagged with a project or client code.
- **Who is accountable?** An individual or role bears responsibility for this payment. If it is questioned, disputed, or audited, the accountable party must be identifiable.

These questions are not optional. They are the governance requirements that separate controlled corporate spend from uncontrolled disbursement. The Spend Mandate is the structure that holds the answers.

---

## The Eight Components

A Spend Mandate comprises eight components. Together, they form the complete authorization envelope for a category of spend.

### 1. Purpose

Why this spend exists. The business justification that makes the payment legitimate.

A purpose is not a transaction description. It is the organizational reason the spend category was created. "Project delivery for Bank X implementation." "Department operations for Q3 Engineering." "Client entertainment for the APAC sales pipeline." "Recurring infrastructure for production systems."

Purpose connects the financial event to the business activity it serves.

### 2. Authority

Who is allowed to initiate, approve, or own this spend. Authority defines the chain of permission.

Authority is organizational, not personal. It attaches to roles — project manager, cost center owner, procurement head, travel desk administrator, finance controller. A person holds authority by virtue of their role, not their identity. When the person changes roles, the authority transfers.

Authority may be layered: an employee initiates, a manager approves, a finance controller oversees. The layers and their thresholds are part of the mandate.

### 3. Budget Source

Which budget or funding allocation absorbs the spend. The financial container that this payment decrements.

Budget source connects the payment to the enterprise's financial planning structure. A department budget. A project budget. A client-billable allocation. A capex pool. A discretionary fund. The budget source determines where the financial impact lands and who monitors utilization.

A single budget may fund multiple programs across different Spend Archetypes (see *Spend Archetypes — Four Workflow Patterns*). The budget is the financial container; the program's mandate configuration is the authorization envelope; the archetype determines the operational flow.

### 4. Policy Scope

What policy regime applies to this spend. The rules, restrictions, and thresholds that govern permissible behavior.

Policy scope may include procurement policies (approved vendor lists, competitive bidding thresholds), travel policies (fare class restrictions, per-diem caps, advance booking requirements), project spend policies (phase-gated approvals, client-billable constraints), and general corporate policies (approval thresholds by amount, geography restrictions, time-of-day limits).

Policy scope is not a single policy. It is the set of policies that collectively govern the spend category.

### 5. Limits

The financial ceilings and guardrails. Limits bound the magnitude and velocity of spend.

Limits operate at multiple levels: per-transaction amount, cumulative daily or monthly amount, total budget cap, merchant-specific or category-specific caps, supplier-specific ceilings. Limits may be absolute (hard decline at threshold) or advisory (flag for review at threshold).

Limits are the most directly enforceable component of the mandate. They translate into card-level controls and budget-level enforcement at authorization time.

### 6. Attribution

How the spend is tagged, tracked, and classified for internal accounting. Attribution is the bridge between the payment event and the enterprise's financial reporting structure.

Attribution includes cost center assignment, GL account coding, project or client code tagging, capex/opex classification, tax treatment designation, and any other internal identifier the finance function uses to organize spend data.

Attribution determines where the payment appears in management reports, how it flows into the general ledger, and whether the finance team can close the books without manual reclassification.

### 7. Validity

When and for how long the authorization is in effect. Validity bounds the mandate in time.

A mandate may be valid for a quarter, a project phase, a contract period, a fiscal year, or until explicitly revoked. A one-time mandate expires after a single use. A recurring mandate persists until its validity window closes or the authorizing party revokes it.

Validity prevents stale authorizations from persisting beyond their intended scope. A project mandate that outlives the project creates uncontrolled spend exposure.

### 8. Exceptions

What happens when spend falls outside the norm. The escalation path for non-standard situations.

Exceptions include approval rerouting (who reviews when the normal approver is unavailable), finance review triggers (what amount or category thresholds escalate to finance), procurement overrides (how exceptions to vendor restrictions are handled), temporary extensions (how budget or limit overages are managed), and post-facto justification requirements (what documentation is required after an exception is used).

Exceptions acknowledge that not every payment fits the standard path. A well-defined exception process is part of governance, not a bypass of it.

---

## The Enforceable / Auditable Divide

The eight components of a Spend Mandate fall into two categories based on when and how they can be evaluated.

### Enforceable at authorization time

Three components can be evaluated and enforced at the moment a card transaction is authorized — in real time, inline with the payment:

- **Limits** — Budget limits are enforced through the budget hierarchy. When a transaction is authorized, all ancestor budgets are consulted. If any ancestor is exhausted, the transaction is declined. Spend policies — MCC restrictions, amount limits, velocity limits, merchant locks, geography restrictions — are evaluated at authorization. Card-level controls enforce restrictions placed on the card at issuance.
- **Policy scope** (partially) — Policies that translate into card controls or authorization rules are enforced at swipe. MCC restrictions, amount limits, merchant locks, and velocity controls are evaluated before the authorization response is returned.
- **Budget source** — The budget is utilized at authorization time. The transaction decrements the budget immediately. Adjustments are made at clearing if the final amount differs from the authorized amount.

These components are not advisory. They are enforced by the issuer at the point of authorization. A transaction that violates a budget limit, a spend policy, or a card control is declined in real time. The mandate's enforceable components translate into concrete platform controls — card-level restrictions set at issuance and policy-layer rules evaluated at authorization.

### Auditable but not enforceable at authorization

Five components cannot be evaluated at the point of transaction authorization. They are governance metadata — essential for post-transaction audit, reporting, and justification, but not reducible to a real-time authorization decision:

- **Purpose** — The business justification cannot be verified at swipe. It is captured in program configuration and validated through audit.
- **Authority** — The authorization chain is established at enrollment and approval time, not re-evaluated at each transaction (except for transactions that trigger pre-authorization approval workflows).
- **Attribution** — Cost center and GL coding may be provided by the cardholder after the transaction or derived from program-level defaults. It is not part of the authorization decision.
- **Validity** — Temporal validity is partially enforceable through card expiration dates, but the business-level validity (project phase, contract period) is an audit concern.
- **Exceptions** — Exception handling occurs after the fact or through separate approval workflows, not at the point of authorization.

```mermaid
graph TB
    subgraph Mandate["Spend Mandate — Eight Components"]
        subgraph Enforceable["Enforceable at Authorization"]
            EN1["Limits<br/><i>Budget ceilings, per-txn caps,<br/>velocity controls</i>"]
            EN2["Policy Scope<br/><i>MCC restrictions, merchant locks,<br/>geography limits</i>"]
            EN3["Budget Source<br/><i>Budget utilization,<br/>hierarchy enforcement</i>"]
        end
        subgraph Auditable["Auditable — Post-Transaction"]
            AU1["Purpose<br/><i>Business justification</i>"]
            AU2["Authority<br/><i>Authorization chain,<br/>role-based ownership</i>"]
            AU3["Attribution<br/><i>Cost center, GL code,<br/>project code</i>"]
            AU4["Validity<br/><i>Time window,<br/>project phase</i>"]
            AU5["Exceptions<br/><i>Escalation path,<br/>override protocol</i>"]
        end
    end

    Enforceable -->|"Evaluated inline<br/>at authorization"| AUTH["Authorization<br/>Decision"]
    Auditable -->|"Captured for<br/>audit and reporting"| AUDIT["Post-Transaction<br/>Governance"]

    style Enforceable fill:#e8f5e9,stroke:#2e7d32
    style Auditable fill:#fff3e0,stroke:#e65100
    style AUTH fill:#c8e6c9,stroke:#1b5e20
    style AUDIT fill:#ffe0b2,stroke:#bf360c
    style Mandate fill:#fafafa,stroke:#616161
```

This divide is a first-class design principle. The platform enforces what it can enforce — budgets, policies, card controls — at the speed of authorization. It captures what it cannot enforce — purpose, attribution, accountability — as metadata for governance, reporting, and audit. The two categories are complementary, not competing. A mandate without enforceable controls is advisory. A mandate without auditable metadata is opaque.

---

## The Mandate as a Thinking Tool

The Spend Mandate is not an entity in the product ontology. There is no "Mandate" record that a corporate creates and attaches to a program. The mandate is a thinking tool — a way of reasoning about the governance requirements of a spend category before those requirements are distributed across concrete system entities.

In the product ontology:

- **Budget source** is realized through the Budget entity and its hierarchical relationship to Credit Facility.
- **Limits** and **policy scope** are realized through Spend Policy and card-level controls within a Corporate Payment Program.
- **Attribution** is realized through the Booking Profile — the internal accounting treatment configured per program.
- **Authority**, **purpose**, **validity**, and **exceptions** are realized through program configuration, enrollment settings, and approval workflows.

No single entity contains the complete mandate. The mandate's components are distributed across the sub-sections of a Corporate Payment Program — Budget, Spend Policy, Booking Profile, and Card Profile. Understanding the mandate as a whole is necessary for understanding why these sub-sections exist and how they compose.

---

## A Mandate in Practice

To make the abstraction concrete, consider a specific mandate within Meridian Industries.

**Archetype:** Travel & Booking Payments
**Mandate:** Client Implementation Travel

| Component | Specification |
|-----------|--------------|
| Purpose | Travel for Bank X implementation project |
| Authority | Engagement manager initiates; delivery head approves |
| Budget source | Client implementation budget (project-level sub-budget under Professional Services) |
| Policy scope | Implementation travel policy — economy class for flights under 6 hours, per-diem caps by city tier, advance booking required for air |
| Limits | $5,000 per booking, $35,000 cumulative per quarter |
| Attribution | Client code: BNK-X-2026. Project code: IMPL-PHASE-2. Cost center: Professional Services — Delivery. GL: 6200-Travel |
| Validity | April – June 2026 (Phase 2 deployment window) |
| Exceptions | CFO delegate approves overages. Post-trip justification required for any booking exceeding per-diem by more than 20% |

This mandate is not entered as a single form or stored as a single record. Its components are distributed: the budget is a Budget entity linked to the Professional Services OU. The limits and policy scope are Spend Policy rules configured in the Corporate Payment Program. The attribution is a Booking Profile. The authority and approval chain are enrollment and workflow configurations. The validity is enforced through card expiration dates and program-level temporal controls.

The mandate is the whole. The system entities are the parts. Understanding the whole is necessary for configuring the parts correctly.

---

## Mandates Across Archetypes

Each Spend Archetype (see *Spend Archetypes — Four Workflow Patterns*) produces mandates with characteristic profiles. Supplier payment mandates emphasize budget source and limits with tight merchant-level controls. Employee spend mandates emphasize attribution and policy scope with distributed authority. Travel mandates emphasize purpose and validity with booking-level controls. Recurring merchant mandates emphasize budget source and limits with long-validity, merchant-locked controls.

The archetype shapes the mandate's emphasis. The mandate shapes the program's configuration. The program's configuration distributes the mandate's components across system entities. This chain — archetype → mandate → program configuration → system entities — is the conceptual path from business need to platform implementation.

The bridge from these conceptual tools to the product ontology's concrete entities is the subject of *From Concepts to Entities*.

---

*See *ESP Variants and Corporate Payment Product* for how archetype-specific mandates inform Product design. See *Corporate Payment Program* for how mandate components are configured within a Program. See *Spend Policy and Controls* for the detailed treatment of enforceable mandate components.*
