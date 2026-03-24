# Why Hierarchy Is Not the Answer

**The structural gap between card limits and corporate controls — and what it takes to close it.**

---

## 1. The Hierarchy of Limits — A Sound Credit Construct

Credit risk management is inherently hierarchical. A bank extends a credit facility to a legal entity. That facility is subdivided into accounts. Each account issues cards. At every level, limits govern exposure: per-transaction caps, daily and monthly aggregates, lifetime ceilings. Each level can only tighten what the level above permits — never loosen.

This is the hierarchy of limits:

**Credit Facility → Account → Card**

The hierarchy evaluates sequentially along a single path. When a card is presented for payment, the processor checks: Is the card active? Is the account in good standing? Does the facility have capacity? Does the budget have capacity? Does the spend policy permit this merchant, this amount, this currency, this geography? Each check narrows. The transaction either survives every gate or is declined.

In practice, the hierarchy extends further. A card processing platform typically enforces a policy cascade across multiple configuration layers — from the bank's base controls through intermediary product-level policies down to card-level restrictions. Each layer inherits the layer above and may only add restrictions. The result is a strictly narrowing funnel: the effective policy at authorization is the intersection of all applicable layers.

This model is sound. It manages credit exposure precisely. It enforces regulatory and compliance controls at the issuer level without downstream actors being able to circumvent them. It scales across millions of cards. For its purpose — credit risk management — the hierarchy is the right structure.

The question is whether credit risk management is the only governance a corporate payment must satisfy.

---

## 2. How Corporations Actually Govern Spend

A corporate's control model is not a hierarchy. It is a coordinate system of multiple independent dimensions evaluated simultaneously.

### Multi-Segment Budget Structures

Every major enterprise resource planning system models budgets as multi-dimensional. SAP's Controlling module (CO) assigns costs across company code, cost center, profit center, internal order, and WBS element — independently. Oracle's chart of accounts uses multi-segment keys where each segment (entity, department, account, project, location) is a separate axis. Workday uses worktags — flexible, stackable dimensions that can be combined without predefined hierarchy.

A single expenditure in a corporate ERP is not recorded against "a budget." It is recorded at the intersection of entity, department, cost center, project, GL account, and potentially client code, activity code, and fund. This intersection is a coordinate — a point in multi-dimensional space. The same department may have separate budget allocations per project. The same project may span multiple departments. The budget structure is a matrix, not a tree.

### Delegation of Authority Matrices

Public companies operating under SOX Section 404 must maintain documented internal controls over financial reporting. A central instrument is the Delegation of Authority (DoA) matrix. A DoA matrix maps transaction categories (capital expenditure, professional services, travel, office supplies, software subscriptions) against amount thresholds against organizational roles — producing a three-dimensional lookup: *for this category, at this amount, who must approve?*

Capital expenditure above $50,000 requires VP approval. Professional services above $10,000 requires Procurement sign-off. Travel above $5,000 requires Director approval. The approval path is not determined by amount alone — it depends on what is being purchased. A $10,000 flight and a $10,000 consulting engagement follow different approval chains even though the amount is identical. The COSO Internal Control Framework, which underpins SOX compliance, explicitly requires that authorization controls be designed around the nature of the transaction, not just its magnitude.

### Category-Dependent Policy Sets

Corporations maintain distinct policy regimes for different categories of spend. A travel policy governs fare class, per-diem rates, advance booking requirements, and duty-of-care obligations. A procurement policy governs preferred supplier lists, competitive bidding thresholds, and contract compliance. An expense policy governs reimbursement limits, receipt requirements, and entertainment caps. These are separate rule sets — maintained by different functions (travel desk, procurement office, finance), enforced through different workflows, and audited against different standards.

Which policy applies to a given transaction depends on its purpose and category, not its position in a limit hierarchy. A $2,000 flight is governed by the travel policy. A $2,000 software license is governed by the procurement policy. A $2,000 client dinner is governed by the entertainment expense policy. Same amount, same cardholder, three different policy regimes — three different sets of rules, approvers, and documentation requirements.

### Multi-Dimensional Cost Attribution

When a transaction posts, the corporate's finance function must attribute it to a coordinate in the accounting structure: cost center, project code, GL account, client code, capex/opex classification. This attribution determines where the payment appears in management reports, how it flows into the general ledger, and whether month-end close can proceed without manual reclassification.

Attribution is not a label applied after the fact. It is a governance requirement that shapes budget consumption, project profitability, client billing, and tax treatment. A payment attributed to the wrong cost center distorts departmental budgets. A payment miscoded between capex and opex affects financial statements. The corporate treats attribution as a control — not a reporting convenience.

### The Structural Point

Corporate spend governance operates across multiple dimensions simultaneously: budget (multi-segment), policy (category-dependent), authority (DoA matrix), attribution (multi-dimensional coordinate), purpose (business justification), and validity (time-bounded). These dimensions are independent — they cannot be collapsed into a single hierarchy without losing the information each carries. A transaction must satisfy all applicable dimensions concurrently. This is a coordinate system, not a tree.

### Why Hierarchy Cannot Represent This

A hierarchy forces a fixed ordering of its dimensions. If the tree is structured as Region → Department → Project, then "Department" is always subordinate to "Region" and "Project" is always subordinate to "Department." Three properties of corporate governance make this ordering structurally untenable:

**The dimensions are enterprise-specific.** Company A organizes governance by region → business unit → project. Company B organizes by department → client → cost center. Company C organizes by legal entity → function → product line. There is no universal ordering. A platform that encodes one ordering cannot serve the others without restructuring — not reconfiguring — its hierarchy.

**The dimensions are not static.** Enterprises restructure. A company that organized by geography last year reorganizes by product line this year. A new regulatory requirement adds a compliance dimension that did not previously exist. A merger introduces a second legal entity hierarchy that must coexist with the first. Each change would require rebuilding the hierarchy from scratch — the ordering itself has changed, not just the values within it.

**Different governance questions require different traversal orders simultaneously.** "What did Department X spend across all projects?" traverses Department first. "What did Project Alpha cost across all departments?" traverses Project first. "What is our total exposure in Region Y across all departments and projects?" traverses Region first. A hierarchy answers one of these efficiently — the one aligned with its fixed ordering. The others require full scans. A coordinate system of independent dimensions answers all of them without structural bias, because the dimensions are not nested.

The result: a hierarchy can enforce limits along a single path with precision. But it cannot represent the corporate's governance model — where dimensions are enterprise-specific, non-static, and queried in multiple orders simultaneously — without forcing a fixed ordering that no enterprise can universally commit to.

---

## 3. The Dissonance — Side by Side

The card processing model and the corporate governance model evaluate the same transaction through fundamentally different structures.

| Aspect | Card Processing Model | Corporate Governance Model |
|---|---|---|
| **Budget** | Single credit limit per hierarchy level (facility, account, card) | Multi-segment coordinate: entity × department × project × cost center × GL account |
| **Policy** | Flat merchant category and geography filters, applied uniformly per card | Category-dependent rule sets — travel, procurement, expense — each with distinct rules, thresholds, and approvers |
| **Approval** | Limit threshold per hierarchy level — amount-only | DoA matrix: category × amount × organizational role |
| **Attribution** | Not modeled in authorization | Multi-dimensional: cost center × project × activity × GL × client code |
| **Evaluation** | Sequential, single-path (facility → account → card) | Simultaneous, multi-dimensional (all applicable dimensions at once) |

The comparison is structural. The hierarchy evaluates depth — parent constrains child, each level narrows. The corporate model evaluates breadth — multiple independent dimensions intersect at a single point. No amount of depth resolves a dimensional mismatch.

### Scenario 1: Travel booking — three dimensions at once

An engineer in Bangalore books a $1,200 hotel for a client implementation project. The corporate's control requirement: the booking must satisfy (a) the travel policy for the engineer's career level and geography (per-diem cap for Tier-2 Indian cities), (b) the project budget for the client engagement (remaining allocation in the Q2 implementation phase), and (c) the department's travel approval threshold (bookings above $1,000 require manager sign-off for junior engineers).

The card processor evaluates: Does $1,200 exceed the card's per-transaction limit? Is the hotel's MCC in the allowed category list? Is India in the permitted geography? These are single-path checks. The processor cannot evaluate whether the booking fits the project budget (a different budget segment than the card's credit limit), whether the career-level policy applies (not a card attribute), or whether the manager has signed off (not representable as a limit).

### Scenario 2: Supplier payment — contract terms and PO match

The AP team issues a single-use virtual card for $25,000 to pay a logistics provider against an approved purchase order. The corporate's control requirement: the payment amount must match the PO amount, the supplier must be on the approved vendor list for this commodity category, and the payment must draw from the procurement operations budget (not the project budget, even though the goods are for a project).

The card processor evaluates: Is $25,000 within the card limit? Is the logistics provider's MCC in the allowed category? These checks pass. But the processor cannot verify PO match (no PO data in the authorization message), cannot distinguish the procurement operations budget from the project budget (both are the same credit facility), and cannot enforce the approved vendor list (MCC is a category, not a supplier identity).

### Scenario 3: Department expense — DoA matrix and budget intersection

A marketing director purchases $8,000 of event sponsorship materials. The corporate's control requirement: (a) the DoA matrix requires VP approval for marketing spend above $5,000, (b) the expenditure must be charged to the Events cost center under the Q2 brand campaign project, and (c) the combined spend on this cost center × project intersection must not exceed the $50,000 quarterly allocation.

The card processor evaluates: Is $8,000 within the card's per-transaction limit? Is the merchant's MCC permitted? The card limit is $10,000 — the transaction passes. But the processor cannot evaluate the DoA matrix (the approval requirement depends on category × amount × role, not just amount), cannot enforce the budget at the cost center × project intersection (it sees only the account-level credit limit), and cannot verify that VP approval was obtained.

### Scenario 4: Reimbursable expense — budget depends on purpose

An employee uses a persistent department card for a $400 dinner. The corporate's control requirement: if the dinner is client entertainment, it must be charged to the client engagement budget and coded to the entertainment GL account with the client code attached. If the dinner is a team event, it must be charged to the department operations budget and coded to the team activities GL account. The budget source, the GL coding, and the approval threshold all depend on the purpose — which is known to the employee but not to the card processor.

The card processor evaluates: Is $400 within the limit? Is the restaurant MCC permitted? The transaction is authorized. The purpose-dependent budget routing, GL coding, and approval threshold are invisible to the authorization decision.

### The Pattern

Every scenario requires evaluating multiple independent dimensions simultaneously. The hierarchy evaluates one path. The corporate's dimensional controls — budget segment, policy regime, authority matrix, attribution coordinate, purpose — are structurally absent from the authorization decision.

---

## 4. The Market Already Recognizes the Gap

An entire industry exists to compensate for the structural gap between card processing hierarchies and corporate governance dimensions.

SAP Concur manages travel and expense policy enforcement. Coupa manages procurement policy and supplier compliance. Emburse manages expense approval workflows and GL coding. BILL (Divvy) and Brex manage budget enforcement and spend categorization. Each platform sits between the card processor and the corporate's ERP — adding multi-dimensional control logic that the processor does not provide.

These platforms are not extensions of the card processor. They are compensating layers. Their customer base and their continued investment in feature depth are empirical evidence that the market has priced in the insufficiency of hierarchical card limits for corporate governance.

But evidence that the gap is recognized is not evidence that the gap is resolved.

---

## 5. What Middleware Cannot Solve

Middleware platforms operate in two time horizons: **pre-transaction** and **post-transaction**. Neither is the authorization moment.

**Pre-transaction**, the middleware enforces approval workflows before a card is issued or a payment is initiated. A procurement manager submits a purchase request. The middleware evaluates the DoA matrix, checks the budget, applies the procurement policy, and — if everything passes — triggers card issuance. The multi-dimensional controls are applied before the card exists.

**Post-transaction**, the middleware reviews completed transactions. An expense management platform flags a restaurant charge that exceeds the entertainment policy, routes it for manager review, and updates the GL coding. The multi-dimensional controls are applied after the money has moved.

**At the moment of authorization** — when the card is presented and the payment network requests a decision from the issuing bank — the middleware is not in the path. The processor evaluates its hierarchical limits: card limit, account limit, facility capacity, MCC filter, geographic restriction. The corporate's budget segments, DoA matrix, category-dependent policies, and attribution requirements are absent from this decision.

This creates a structural fracture in corporate governance. Controls are split across three time horizons:

- **Pre**: approval workflows and budget checks enforce multi-dimensional controls before card issuance — but only for transactions that originate through the workflow. An employee with a persistent card who makes an unplanned purchase bypasses the pre-transaction layer entirely.
- **During**: the processor evaluates hierarchical limits alone. The corporate's dimensional controls are not evaluated.
- **Post**: expense review catches violations after the transaction has settled. The middleware flags, the manager reviews, the finance team corrects. The violation was not prevented — it was detected.

The corporate's governance is never evaluated as a unified, multi-dimensional decision at the authorization moment. Pre-transaction workflows approximate it for planned spend. Post-transaction review compensates for unplanned spend. But neither is governance at the point of decision.

Post-facto correction is not governance. It is damage assessment. The money moved. The merchant was paid. The budget was consumed. The GL was miscoded. The correction is labor — reconciliation labor, exception-handling labor, audit-response labor. The corporate's finance team exists partly to clean up what the platform could not prevent.

---

## 6. What the Gap Costs

### To the Corporate

**Fragmented governance.** Controls that should be a single, unified evaluation at authorization are scattered across three systems and three time horizons. The procurement platform enforces pre-transaction. The card processor enforces during-transaction (limits only). The expense platform enforces post-transaction. No single system holds the complete governance picture.

**Reconciliation labor.** Every transaction that passes the processor's limits but violates a corporate policy generates manual work. A charge at a permitted MCC that should have been declined because the project budget was exhausted. A transaction that posted to the wrong cost center because the processor has no attribution model. A payment that cleared against a card limit but exceeded the DoA threshold for that category. Each violation requires human review, correction, and documentation. For large corporates with thousands of transactions per month, this is a material operational cost.

**Audit exposure.** Controls that are detective rather than preventive create audit risk. An auditor reviewing SOX compliance asks: "Was this $45,000 purchase approved by a VP as required by your DoA matrix?" If the answer is "the card processor authorized it within the card limit, and the expense platform flagged it for review afterward" — that is a weaker control than "the authorization system evaluated the DoA matrix and required VP approval before the transaction completed." Preventive controls are stronger evidence of compliance than detective controls. The hierarchy provides the former only for limits; for everything else, the corporate relies on the latter.

**Policy leakage.** When controls are advisory rather than enforced, compliance depends on human diligence. An employee who knows the expense platform will flag a policy violation after the fact may proceed anyway — the dinner is already eaten, the purchase already made. The middleware can report the violation, but it cannot prevent it. Over time, advisory controls erode. Enforced controls do not.

### To the Bank

**Disintermediation.** The middleware platform — Concur, Coupa, Emburse — becomes the corporate's operating relationship. The corporate's finance team logs into the middleware platform daily. They configure policies there, review transactions there, generate reports there. The bank's portal is where they check credit facility utilization. The bank is the infrastructure; the middleware is the experience. The corporate's loyalty attaches to the platform they operate in, not the one that issues the cards.

**Commoditization.** When every bank offers the same hierarchical limits through the same legacy processors, the card product is a commodity. Differentiation is impossible at the authorization layer. The only competitive surface is pricing — interchange share, rebate structure, facility terms. The bank cannot compete on governance capability because the processor does not support it.

**Revenue leakage.** Corporates will pay for governance capabilities — budget enforcement, policy compliance, attribution automation, approval workflows. They are already paying: to Concur, to Coupa, to Emburse, to Brex. That revenue accrues to middleware providers who fill the gap the bank's platform leaves open. When the platform can evaluate multi-dimensional controls at authorization, governance value and the corporate's operating relationship shift from the middleware layer to the issuing bank.

---

## 7. From Hierarchy to Dimensions — The Shift Required

The hierarchy is not wrong. It remains essential for credit risk management. Dismantling it would be reckless. The shift is not from hierarchy to dimensions — it is from hierarchy alone to hierarchy plus dimensions.

### What Is Missing

The authorization decision currently evaluates one structure: the credit risk hierarchy. What corporate governance requires is a second, concurrent evaluation: multi-dimensional controls drawn from the corporate's own governance model.

The dimensions are:

- **Budget** — evaluated not as a single credit limit but as a multi-segment coordinate: does this transaction fit within the remaining allocation at the intersection of department, project, cost center, and fund?
- **Policy** — evaluated not as a flat MCC filter but as a category-dependent rule set: which policy regime applies (travel, procurement, expense), and does this transaction satisfy its rules?
- **Authority** — evaluated not as a limit threshold but as a DoA matrix lookup: for this category, at this amount, has the required organizational role approved?
- **Attribution** — evaluated not after the fact but at authorization: to which cost center × project × GL account × client code should this transaction be booked?
- **Purpose** — evaluated by archetype: is this transaction consistent with the business justification of the spend channel through which it flows?
- **Validity** — evaluated temporally: is the authorization still within its defined window (project phase, fiscal quarter, contract period)?

### How They Interact

These dimensions are not sequential gates. They are concurrent constraints. A single transaction must satisfy all applicable dimensions simultaneously — budget capacity at the right segment, policy compliance under the right rule set, authority from the right organizational role, attribution to the right coordinate, purpose consistent with the right archetype, validity within the right time window.

The credit risk hierarchy remains. The facility limit still applies. The account limit still applies. The card limit still applies. The bank's non-overridable controls — AML, sanctions, fraud, delinquency — still execute. None of this changes.

What changes is that the authorization decision also evaluates the corporate's dimensional controls — in the same real-time window, before the response goes to the network. The result is a single, unified governance decision that satisfies both the bank's credit risk model and the corporate's operational governance model.

But stating what the authorization must evaluate is not the same as explaining how. The corporate's control matrix lives in the corporate's vocabulary. The bank's authorization engine speaks its own. Bridging the two is the architectural problem at the center of the platform.

---

## 8. The Translation Problem

The corporate's control matrix — budget segments, DoA thresholds, category-dependent policies, attribution coordinates — is expressed in corporate vocabulary: cost centers, project codes, GL accounts, organizational roles. The bank's authorization engine evaluates bank vocabulary: credit facility, account, card, MCC, amount, geography. These vocabularies are native to different domains, optimized for different obligations. They are not interchangeable.

Evaluating the corporate's multi-dimensional controls at authorization requires projecting the control matrix into each authorization request's evaluation context — without either domain abandoning its native semantics. This projection is the hard architectural problem. Three mechanisms accomplish it.

### An Anti-Corruption Layer Between Domains

The bank's authorization engine does not learn what a "cost center" is. The corporate's governance model does not learn what a "credit facility" is. The translation between them is explicit, maintained at a dedicated architectural boundary, and bidirectional.

Without this layer, domain integrity erodes in one of two directions. Either the bank's model absorbs corporate concepts — adding cost centers, project codes, and DoA matrices to its authorization logic — which violates the regulatory simplicity the bank requires and couples the bank's platform to every corporate's organizational idiosyncrasies. Or the corporate's governance is forced into bank vocabulary — expressing project budgets as card limits, DoA thresholds as amount caps, policy regimes as MCC filters — which loses the dimensional fidelity that makes corporate governance meaningful.

The anti-corruption layer prevents both. Each domain operates in its native semantics. The layer translates between them at well-defined integration points — at configuration time, at card issuance, at authorization, at posting — without leaking one domain's model into the other.

### Structured Entities That Pre-Encode Dimensional Controls

The corporate's multi-dimensional governance must be encoded into structured entities that the authorization engine can evaluate at transaction time — without the engine needing to understand the corporate's organizational model.

Budget hierarchies carry segment coordinates and enforce capacity at each ancestor in the chain. Spend policies carry category-dependent rules and cascade through configuration layers — each layer tightening within the envelope the layer above permits. Booking profiles carry attribution coordinates — cost center, GL account, project code, client code — so that every authorized transaction is attributed at the moment of decision, not corrected after the fact. Card profiles carry validity constraints, purpose markers, and merchant restrictions that encode the spend channel's governance intent.

These entities are the mechanism by which the corporate's multi-dimensional governance is projected into forms the authorization engine evaluates. The design of these entities — what they carry, how they compose, how they cascade, what they inherit — determines how much of the corporate's control matrix is evaluable at authorization. The more of the matrix that can be pre-encoded in structured entities, the less reliance on post-transaction correction.

### Cooperative Authorization for On-Demand Context

When pre-encoded structures do not carry sufficient information — a purpose-dependent routing decision, a cross-organizational budget query, an authority chain that depends on context not present in the card profile — the platform invokes external systems during the authorization window for additional context or decisions.

This is not only a recourse for edge cases. It is a first-class projection mechanism. A corporate's policy engine may hold governance logic too complex or too frequently changing to pre-encode in the platform's structured entities. Invoking that engine during authorization extends the platform's evaluative reach into the corporate's full control matrix — in real time, within the network timeout.

### The Constraint Triangle

These three mechanisms — anti-corruption layer, structured entities, cooperative authorization — must simultaneously satisfy three classes of constraints:

**Technical.** Sub-second latency. High throughput. Deterministic evaluation. The authorization engine evaluates hierarchical limits and multi-dimensional controls, aggregates cooperative authorization responses, and returns a decision within the network timeout — every time, at scale.

**Security.** Domain isolation. The bank's risk data and the corporate's organizational data do not cross boundaries without explicit, controlled translation at the anti-corruption layer. Access control and data minimization are enforced architecturally, not delegated to application logic.

**Regulatory.** The bank remains the issuer of record. The bank retains final authorization authority. Compliance controls — AML, sanctions, fraud, delinquency — are non-overridable regardless of what the corporate's dimensional evaluation produces or what a cooperative authorization participant returns. The corporate's governance enriches the authorization decision. It does not supersede the bank's obligations.

Designing the right combination of data structures, algorithms, and processes that meet all three constraints simultaneously — while faithfully projecting the corporate's multi-dimensional governance into every authorization decision — is the core value architecture of the platform. Not a feature list. Not a configuration surface. The hard problem that determines whether multi-dimensional corporate governance at authorization is achievable or remains aspirational.

---

## 9. When Structure Reaches Its Boundary

Even with structured entities that pre-encode dimensional controls and cooperative authorization that extends the platform's evaluative reach, some governance requirements resist representation as rules evaluable in real time.

### What Cannot Be Pre-Configured

- **Novel spend categories** where no policy has been established — a new project type, a new vendor category, a newly entered geography
- **Contested authority** where the delegation chain is ambiguous — an interim appointment, a cross-functional initiative, a matrix-reporting situation where two managers have overlapping jurisdiction
- **Exceptional circumstances** that fall outside configured rule sets — an emergency procurement, a force majeure event, a one-time engagement that doesn't fit any existing archetype
- **Organizations in transition** — mergers, restructurings, policy rewrites in progress — where the governance model itself is changing and rules are temporarily indeterminate

For these cases, the authorization system needs recourse beyond its configured rules.

### Three Modes of Deliberation

The authorization window — 2 to 5 seconds, imposed by the payment network — constrains what is feasible during a transaction decision. Three modes of deliberation address different governance needs within and around this constraint:

**Pre-authorization deliberation.** Human judgment is captured as policy, rules, and configuration before any transaction occurs. At program setup, budget allocation, enrollment approval, and card issuance, humans make governance decisions that the system then enforces mechanically at authorization time. The human decided in advance. The system enforces in real time. This is the dominant mode for structured governance — and the right one. The more governance that can be expressed as pre-configured rules and dimensional parameters, the stronger the real-time enforcement.

**Cooperative authorization.** The authorization system invokes an external decision-maker — another system, a policy engine, or an AI agent — during the authorization window. The platform holds the authorization decision open while the external system evaluates and returns a decision within the network timeout. This is system-to-system, sub-second. Human participation during the authorization window is generally infeasible at 2-5 seconds — limited to specific protocol-supported flows such as 3D Secure or credit pull requests, where the transaction protocol explicitly accommodates an extended interaction. For the general case, cooperative authorization is a machine-to-machine capability.

**Post-authorization review.** The transaction is provisionally authorized. Review, hold, or reversal follows. This is the appropriate recourse when neither pre-configured rules nor cooperative authorization can resolve the governance question. It is the weakest mode — the money has moved — but it is honest about its limitations and provides a structured path for correction rather than silent policy leakage.

### The Expanding Boundary

Agentic AI changes the calculus of cooperative authorization. Capabilities that previously required human pre-configuration — policy interpretation, pattern recognition, precedent-based judgment, contextual evaluation of ambiguous situations — can increasingly be performed by AI agents operating within the authorization window. An agent can evaluate whether a transaction matches the pattern of a novel spend category that hasn't been formally configured. It can assess whether an approval chain covers a cross-functional situation. It can apply judgment-like reasoning to edge cases that rigid rules would either over-block or under-block.

The significance is not that AI replaces human governance. It is that AI expands what can be evaluated during the authorization window — the moment where governance has the most force. Decisions that previously had to be either pre-configured (losing flexibility) or post-reviewed (losing prevention) can increasingly be evaluated in real time through cooperative authorization with an AI agent.

The residual set of decisions requiring human deliberation shrinks — not to zero, but substantially. And the architecture must support all three modes from the start. The trajectory is toward shifting more governance decisions into cooperative authorization as agent capabilities mature — but the platform cannot be redesigned each time that boundary moves. It must be designed for all three modes on day one.

---

## 10. Implications for Platform Design

The analysis implies specific architectural requirements.

**Concurrent evaluation.** Authorization must evaluate the credit risk hierarchy and the corporate governance dimensions in a single real-time decision. These are not separate workflows — they are concurrent evaluations that produce a unified approve/decline response within the network timeout. The platform cannot evaluate limits first and dimensions later; both must be resolved before the response goes to the network.

**Domain-separated configuration.** The corporate's dimensional model — budget segments, policy regimes, DoA thresholds, attribution coordinates — must be configurable by the corporate without altering the bank's credit model. The bank's facility limits, compliance controls, and risk parameters must be enforceable without awareness of the corporate's internal governance structure. Neither domain's configuration should require the other's permission or vocabulary — the anti-corruption layer maintains the boundary.

**Three-domain separation.** The bank owns the credit risk hierarchy. The corporate owns the governance dimensions. An intermediary — whether an ESP, a fintech, or a managed service provider — translates between the two domains through the anti-corruption layer, creating products that express corporate governance patterns using bank capabilities without blurring either domain's boundaries. The platform must enforce this separation architecturally, not just organizationally.

**Extensibility for evolving deliberation.** The platform must support pre-authorization configuration, cooperative authorization with external systems (including AI agents), and post-authorization review workflows — as first-class capabilities, not as integration workarounds. As the boundary between what can be pre-configured and what requires real-time deliberation shifts — driven by AI maturity, corporate governance evolution, and regulatory change — the platform must accommodate the shift without re-architecture.

---

The hierarchy of limits is a sound credit construct. It will remain. But corporate payment governance requires more than credit risk management. It requires concurrent evaluation of multiple independent dimensions — budget, policy, authority, attribution, purpose, validity — at the authorization moment. The gap between these two structures is not a configuration shortfall. It is a structural dissonance. Closing it requires a platform that evaluates both — and an architecture designed for the governance complexity that corporate payments demand.
