<!-- CO-MAINTAINED: Any new input must be evaluated for updates to this file, presentation-contents-discussion.md, and book-writing-backlog.md simultaneously. -->

# Corporate Payments by Design — Presentation Outline

**Subtitle:** The first-principles design to solve for corporate concerns  
**Platform:** Tachyon + Electron  
**Audience:** Bank prospects evaluating the platform for corporate payments  
**Tone:** Consultative, domain-authoritative — show how it works and how it translates into data  

---

## Act 1 — The Gap

### Slide 0: Title

**Corporate Payments by Design with Tachyon and Electron**

- The first-principles design to solve for corporate concerns
- Speaker context: what we are about to walk through and why it matters to a bank

---

### Slide 1: Possibilities vs Needs

**Banks describe possibilities with virtual cards — and they are genuinely promising. Corporates hear those possibilities and imagine answers to their real questions: budget, authority, attribution, reconciliation. The gap between the promise and the imagined answer is the required evolution.**

*Speaker Notes:*
- Lead with possibilities, not features: "Issue a card per PO." "Lock to a single merchant." "Set velocity limits." "Get L2/L3 data." Acknowledge them — they are genuinely promising.
- Then pivot: corporates hear those possibilities and imagine answers — "budget enforcement across three legal entities," "GL attribution per transaction," "policy cascades across 200 supplier cards," "automated reconciliation against AP." The imagination is natural. The product does not yet deliver what is imagined.
- Land the framing: the gap between the promise and the imagined answer is the required evolution. Not a criticism — a market reality. Neither side is wrong.
- Let the statement sit. Do not rush to the next slide. The audience should recognize this dynamic from their own client conversations before you move on.

---

### Slide 2: The Platform Reality

**The vision of corporate payments is compelling. The platform wasn’t built for it.**

*Speaker Notes:*
- This is not a vendor critique — it is an architectural observation. The audience will recognize these constraints from their own experience.
- Validate the vision: the bank sees the opportunity clearly. The gap is not in ambition or strategy — it is in the platform beneath the strategy.
- Do not name specific vendors on screen. Let the audience map the constraints to their own platform.
- Let this sit. The audience should feel the tension between what they want to build and what their platform can deliver. Slide 7 will close this loop with specifics.

---

### Slide 3: The Semantic Dissonance

**When corporates ask questions and banks answer with card capabilities, both sides are speaking accurately — from different frames.**

| Corporate's Question | Bank's Answer |
|---|---|
| "Our policy is to encourage local procurement. How can I specify my suppliers?" | "Please provide the MID and TID of all your suppliers." |
| "Our policy requires maker and checker for high-value department spends. How can we specify that?" | "You can issue a card for every transaction, after checking whatever needs to be checked." |
| "Every ticket purchased is subject to the project budget, the employee’s location, and their career level." | "You can set limits per card." |
| "Our marketing budget is shared across three regions operating with different currencies. Each region can spend up to their allocation, but the total must not exceed the consolidated budget." | "You can set credit sub-limits per account." |

- The pattern: the corporate asks about business rules, organizational context, and operational workflows. The bank answers with card-level primitives — limits, identifiers, individual cards.
- Neither side is wrong. They are organizing around different concerns.

---

### Slide 4: Five Dimensions of Corporate Need

**The semantic dissonance reveals a pattern. Corporate payment needs span five dimensions — and today's card products answer only the first.**

| Dimension | What the corporate needs | What card products typically provide |
|---|---|---|
| **Payment Execution** | Authorize, clear, settle reliably | Well-answered: networks, schemes, real-time auth |
| **Financial Architecture** | Credit facilities allocated as budgets, tied to organizational purpose, with hierarchical enforcement | Partially answered: credit limits and sub-limits exist, but without budget semantics or OU-awareness |
| **Control Architecture** | Policy cascades, eligibility rules, enrollment workflows, lifecycle governance across programs | Primitively answered: per-card controls exist, but no program-level policy, no inheritance, no lifecycle orchestration |
| **Accounting & Attribution** | Every transaction attributed to GL, cost center, project, client — structured, validated, pushed to ERP | Not answered: reference fields exist but lack structure, validation, and ERP integration |
| **Reconciliation & Settlement** | Automated matching against PO/invoice/booking/contract; consolidated settlement by program | Not answered: transaction data is available but matching, consolidation, and settlement management are left to the corporate |

- The first dimension is table stakes. The other four are where corporate payment programs succeed or fail.
- No corporate CFO evaluates a card program on authorization speed. They evaluate on reconciliation labor, policy leakage, and attribution accuracy.

---

### Slide 5: The Counterparty Multiplier

**The five dimensions do not present uniformly. They vary by the type of counterparty the corporate pays — and the AP landscape has at least seven distinct shapes.**

| Counterparty Type | Payment Pattern | Data Needs | Compliance | Card Acceptance |
|---|---|---|---|---|
| Goods suppliers | PO/invoice-driven, deterministic | L2/L3, three-way match | Trade compliance, tax | Generally high |
| Service providers | Milestone or deliverable-based | SOW reference, project attribution | Contract compliance | Variable |
| Employees | Reimbursable expenses or pre-approved budget-based spend; the actual merchant is not a direct party to the transaction | Receipt, expense category, project/cost center | Expense policy, delegation of authority | High — employee transacts at merchant |
| Contractors | Time/expense-based, recurring | Timesheet linkage, project codes | Labor compliance, 1099 | Low — often ACH preferred |
| SaaS / software vendors | Subscription, renewal-driven | Contract ID, license count | Procurement policy | High — most accept cards |
| Intermediaries / agencies | Pass-through, consolidated | Booking reference, itinerary | Agency agreements, duty of care | High — travel, logistics |
| Government / regulatory | Fee schedules, non-negotiable | Mandate reference, filing ID | Regulatory deadlines | Low — often requires wire/ACH; May move to RTP, FedNow rails |

- Today's card products abstract all of these as "merchants" — a single MCC-classified entity. The corporate sees seven fundamentally different relationships, each with distinct governance requirements. For employees, the merchant isn't even the counterparty — the governance is between the corporate and its employee, not the corporate and the merchant.
- This diversity multiplies the five dimensions: financial architecture for a goods supplier (PO-locked budget) looks nothing like financial architecture for a SaaS vendor (contract-locked renewal budget).
- The archetype discussion (next act) addresses this directly. For now: the problem is not just multi-dimensional — it is multi-dimensional per counterparty type.

---

### Slide 6: The Two-Lens Gap

**Banks organize around financial risk. Corporates organize around operational governance. Both worldviews are coherent. The friction is in the translation.**

- Bank's organizing principle: credit facility → account → card → MCC/amount/velocity controls → interchange → lifecycle
- Corporate's organizing principle: department → project → cost center → budget/policy/approval → GL/project/client codes → reconciliation → DPO
- The structural mismatches: org structure ≠ account structure; budget ≠ credit limit; GL fields ≠ transaction data; workflow ≠ card controls; reconciliation ≠ data availability
- This is not a criticism. Banks optimize for what they must: credit risk, regulatory compliance, network settlement. Corporates optimize for what they must: operational governance, financial attribution, audit readiness.
- The gap is architectural — not a missing feature, not a configuration oversight. It requires a design that respects both organizing principles without collapsing one into the other.

---

### Slide 7: The Challenge of the Promise

**The promise is captive to the platform that delivers it:**

| Constraint | What It Means |
|---|---|
| **Batch-native** | Real-time authorization events, lifecycle notifications, and cooperative callbacks require middleware the platform wasn’t designed for |
| **Rigid hierarchies** | Per-card limits exist; hierarchical budgets with programmable policy cascade and ancestor-chain enforcement do not |
| **Limiting data structures** | Rigid data fields that cannot carry corporate context through the transaction lifecycle; refunds and credits not attributed back to original booking profile |
| **Closed authorization** | The processor decides alone; no hook for ESP or corporate participation within network timeouts; no posting enrichment at clearing |
| **Lack of token awareness** | Token lifecycle not coordinated with card lifecycle across renewals and replacements; authentication limited across CNP/CP scenarios; PIN delivery confined to legacy channels; FRM has credential lifecycle blind spots |
| **Throughput constraints** | Not designed for high-frequency, API-triggered, single-use issuance at scale; card lifecycle operations designed for call-center workflows, not programmatic bulk operations |
| **Inaccessible for extension** | No event subscriptions, no webhook-driven integration, no API-driven lifecycle customization; the platform is closed to the ecosystem that needs to build on it |

*Speaker Notes:*
- Callback to Slide 2: “We said the promise is captive to the platform that delivers it. Now that you’ve seen what the corporate actually needs — five dimensions, seven counterparty types, two organizing principles — here’s specifically what that captivity looks like.”
- Walk through each row. Each constraint now maps to something the audience understands — they’ve just seen the five dimensions and the counterparty diversity. The constraints aren’t abstract anymore.
- Batch-native: “When was the last time your processor pushed an authorization event in real time without middleware?”
- Rigid hierarchies: “Can your processor enforce a budget hierarchy where a $25K card transaction checks the card limit, the program budget, and the legal entity credit facility — all at authorization?”
- Limiting data structures: “Can you attach a PO number to a card at issuance and have it travel through authorization, clearing, and settlement? When a refund arrives, does it attribute back to the original booking?”
- Closed authorization: “Can your corporate client participate in the authorization decision before the processor responds to the network? Can external data enrich the posting at clearing?”
- Lack of token awareness: “When a virtual card is renewed, do the tokens migrate automatically? Does your FRM system see the full credential lifecycle — or just the card?”
- Throughput: “How many single-use cards can your processor issue per minute via API? What happens to lifecycle operations at scale?”
- Inaccessible for extension: “Can your ESP subscribe to card events in real time? Can a corporate system trigger a lifecycle operation via API?”
- Let each question sit. The audience’s silence is the evidence.

---

### Slide 8: The Foundation and The Bridge

**This is what we set out to solve. The foundation: a processing platform purpose-built for corporate spend governance, designed for the possibilities of this decade. The bridge: an architecture that answers the corporate's actual questions across all five dimensions, across all counterparty types, while preserving the bank's risk and compliance model.**

- The foundation requires a platform that is event-native, hierarchy-aware, contextually rich, on-demand, cooperatively authorized, token-aware, throughput-ready, and extensible — the inverse of every constraint we just identified
- It must also be architected for the evolving payment landscape: credentials beyond cards, authentication beyond static mechanisms, rails and clearing beyond card networks, and digital currencies — without re-platforming for each
- The bridge requires three things: (1) a product model that encodes corporate governance patterns, not just payment capabilities; (2) a clean separation between the bank's domain (risk, credit, compliance) and the corporate's domain (governance, attribution, reconciliation); (3) an intermediary that translates between them without blurring boundaries
- That is the three-domain model — Bank, ESP, Corporate, each owning what it understands best — running on a processing platform designed from the ground up for these requirements
- What follows: the foundation — the payment platform, its capabilities, and how it resolves the constraints we identified. Then the bridge — the three-domain architecture, Spend Archetypes that organize the counterparty diversity into actionable product patterns, a Spend Mandate framework that captures all five dimensions, and the entity architecture that connects them

---

## Act 2 — The Framework

### Slide 9: Spend Archetypes

**Corporate payments organize into Spend Archetypes — each with a distinct control model, card lifecycle, enrollment pattern, and reconciliation approach.**

| Dimension | Supplier Payments | Employee & Dept Spend | Travel & Booking | Central Recurring |
|---|---|---|---|---|
| Control model | Tight, deterministic, PO/invoice match | Policy-bounded, discretionary within limits | Booking-locked or agency-managed | Contract-aligned, merchant-locked |
| Card lifecycle | Single-use per invoice | Persistent, renewable | Per-booking or lodge (long-lived) | Long-lived, merchant-locked |
| Enrollment | Payee (supplier) | Payer (employee) | Traveler or travel desk | Central administrator |
| Reconciliation | PO/invoice match (L2/L3) | Expense report, receipt matching | Itinerary/booking match | Contract/subscription match |

- Archetypes are not product names — they are the organizing principle for how corporates govern spend. Each defines a distinct pattern of control, lifecycle, enrollment, and reconciliation.
- Supplier: single-use card issued per approved invoice/PO, locked to exact amount and merchant, closed after clearing; ERP triggers issuance; L2/L3 data critical for three-way match
- Employee: persistent card per employee, MCC allowlists, per-transaction and monthly velocity limits; self-enrollment or manager-initiated; expense reports drive reconciliation
- Travel: lodge card to travel agency (long-lived, shared) or per-booking virtual card; booking system triggers issuance; itinerary data for reconciliation
- Central Recurring: one card per merchant/contract, merchant-locked, renewal-aligned lifecycle; centrally administered; contract terms drive reconciliation
- "Embedded" (API-triggered issuance) is a delivery mechanism, not an archetype — it can serve any of the four

---

### Slide 10: Spend Mandates — The Authorization Envelope

**Every corporate payment must answer a chain of questions: Why was this allowed? Who authorized it? Whose budget? Which rules? How is it booked? Who is accountable? The Spend Mandate is the framework that holds those answers.**

| Component | What it governs | Example (Meridian) |
|---|---|---|
| Purpose | Why this spend exists | "Client Implementation Travel" for Bank X |
| Authority | Who may authorize | Engineering VP for department spend |
| Budget Source | Which budget funds it | Procurement Operations — $30M |
| Policy Scope | What categories are allowed | AMC-Logistics, AMC-Cloud only |
| Limits | Per-transaction, velocity, aggregate | $5,000 per booking, $35,000/quarter |
| Attribution | How spend is booked | Project BNK-X-2026, GL 6200-Travel |
| Validity | When the mandate is active | Apr–Jun 2026 |
| Exceptions | What happens outside bounds | Escalation to CFO, manual review |

- No single system entity called "Spend Mandate" — it is realized across Budget, Spend Policy, Booking Profile, Card Profile, and Program configuration

---

### Slide 11: Governance: Constraints and Decisions

**Governance is not enforcement alone. It requires constraints that the platform enforces automatically, and decisions — structured and unstructured.**

- **Constraints** — evaluated at authorization in real time:
  - Budget capacity (hierarchy-aware)
  - Spend Policy (MCC/AMC, amount, currency, geography, velocity)
  - Limits (per-transaction, daily, monthly, lifetime)
  - The bank evaluates these on every transaction — no exception

- **Structured Decisions** — representable as rules, enforced through configuration:
  - Purpose: which program the card belongs to
  - Attribution: booking profile rules determine GL/cost center/project assignment
  - Validity: program and card validity windows

- **Unstructured Decisions** — require human deliberation; the platform provides deliberation control:
  - Authority: who approved the enrollment and card issuance; escalation when authority is contested or delegated
  - Exceptions: escalation workflows, approval chains, post-facto justification

- The design challenge: enforce constraints automatically, enforce structured decision rules through configuration, and provide deliberation control for unstructured decisions

---

### Slide 12: The Three Domains

**The bank organizes around risk. The corporate organizes around governance. Neither can collapse into the other. The ESP exists to translate between them.**

- Why three domains: Slide 6 established that banks optimize for credit risk, regulatory compliance, and network settlement — while corporates optimize for operational governance, financial attribution, and audit readiness. These are not overlapping concerns — they are structurally different organizing principles. Attempting to serve both from one domain model forces one side to adopt the other's vocabulary, violating its own obligations.
- **Bank**: underwrites risk, authorizes transactions, enforces compliance, settles with networks — owns Credit Facilities and Payment Capabilities
- **ESP (Enterprise Service Provider)**: creates products per archetype, onboards corporates, manages billing, provides the operating layer — translates bank capabilities into corporate solutions without blurring either domain
- **Corporate**: configures programs, defines budgets and policies, enrolls members, operates day-to-day spend governance — owns the mandate and organizational context

- Each domain owns what it understands best; the platform enforces clean separation
- The bank does not see departments or cost centers; the corporate does not touch underwriting; the ESP mediates without owning either worldview

---

### Slide 13: Value Added and Value Realized

**Each domain contributes distinct value — and each captures distinct value in return.**

- **Bank** contributes: Credit Facilities, payment authorization, compliance enforcement, network settlement
- **ESP** contributes: product design per archetype, corporate onboarding, billing, operational layer
- **Corporate** contributes: program configuration, budget and policy definition, member enrollment, day-to-day governance

| Stakeholder | Value Realized |
|---|---|
| **Bank** | Float income, customer retention, network incentives, network interchange, account/card fees, regulatory compliance |
| **ESP** | Revenue share from bank (float, interchange, fees), fees and charges from corporate, portfolio scale across 40+ corporates |
| **Corporate** | Control and governance (mandate enforcement), AP automation story, rebates, rewards, DPO extension, reconciliation labor reduction |
| **Members** (of various types) | Cashflow benefits, negotiated MDRs (supplier), AR story (supplier), expense simplification (employee), travel convenience |

- Value is not zero-sum — the three-domain model creates incremental value at each layer

---

## Act 3 — The System Design

### Slide 14: Systems and Bounded Contexts

**Each domain operates through purpose-built systems. Understanding what runs where is essential to understanding the architecture.**

**Tachyon (Bank) — 14 subsystems of relevance:**
- Customer Lifecycle Management — HAH (Headless Account Holder: quasi-customer, no KYB/KYC), LAH (Legal Account Holder: legal person, KYB), RAH (Real Account Holder: real person, KYC)
- Product Lifecycle Management — Account Product Families, Virtual Card Product Families; catalog creation, versioning, redistributability
- BaaS Management — manages Virtual Banking Operators (VBOs); ESP onboarding, catalog access grants, partner agreements
- Credit Management — Credit Facilities, Limit Hierarchy, Revolving and Non-revolving Credit Accounts, Secured Credit Accounts
- Accounting System — Accounting, Fees, Interest, Billing, Statements (account-level financial operations)
- Payments Switch — real-time authorization routing, network connectivity, scheme message processing
- Payments Hub — clearing, settlement, posting; end-to-end payment lifecycle orchestration
- Rewards System — Reward Programs, Rebate Programs at Account and Statement level (product-level rewards)
- FRM (Fraud and Risk Management) — real-time fraud scoring, transaction monitoring, risk decisioning
- Disputes Management — chargeback processing, representment, dispute case lifecycle
- Consumer IAM — cardholder/member authentication, credential management
- Enterprise IAM — bank staff, ESP staff, corporate admin authentication and access control
- Notification — bank-originated notifications (regulatory, fraud, lifecycle events); non-suppressible alerts
- Operations Hub — bank operations console for monitoring, exception handling, servicing
- Data Mart — bank-side analytical data store for reporting, risk analytics, regulatory reporting

**Electron (ESP) — 7 subsystems of relevance:**
- Client Contract Management — Corporate and Contract lifecycle; relationship-level terms, scope, duration, renewal
- Payment Product Management System — Account Variants, Virtual Card Variants, CPP assembly; component programs (fees, interest, rewards, rebates, notifications, spend, auth, tokenization, 3DS, card fees)
- Payment Program Management System — Program configuration, Spend Policy, Booking/Settlement Profiles, eligibility rules, enrollment workflows, member and card management
- Billing and Collections System — Consolidated Invoices, Relationship-level Rebates, Rewards, Volume Commitments, Auto Debit
- Bank Gateway — Anti-corruption and Translation layer between Electron and Tachyon; maps ESP domain concepts to bank domain entities and vice versa
- Corporate Data Mart — comprehensive data regarding all programs, invoices, transactions, members; Data Extracts and Reports for corporates
- ESP Data Mart — analytics on Contracts, Products, and Programs for the ESP's own portfolio management

**Corporate Domain** — spans multiple system types interacting with the Electron Corporate Portal:
- Electron Corporate Portal — Organization Management (OU hierarchy, legal entities), Program Administration (Programs, Spend Policy, Booking/Settlement Profiles), Member & Enrollment Management (members, eligibility, card issuance), Financial Control (budgets, settlement accounts), Operations (reconciliation, disputes)
- AP Systems (e.g., SAP Ariba, Oracle AP, Coupa) — supplier payment automation, PO/invoice matching, card issuance triggers
- AR Systems — receivables matching, payment application, customer payment tracking
- Expense Management Systems (e.g., Concur, Navan, Brex) — employee spend capture, receipt matching, policy compliance
- Travel Booking Systems (e.g., Amex GBT, CWT, Navan) — lodge card integration, booking-linked card issuance
- ERP / GL Systems (e.g., SAP, Oracle, NetSuite) — GL posting, cost center attribution, financial consolidation
- Treasury Systems (e.g., Kyriba, FIS) — settlement account management, cash positioning, FX management
- IAM / Directory Services (e.g., Okta, Azure AD, Ping) — member and user provisioning, role assignment, authentication for ESP and bank portal access, SSO and MFA enforcement
- LoB Applications — department-specific or vertical-specific applications that consume card data or trigger spend events

---

### Slide 15: Context Boundaries and Integration Points

**The systems communicate across well-defined boundaries. No domain reaches into another's internals.**

- **Bank ↔ ESP** (mediated through the Bank Gateway — Electron's anti-corruption and translation layer)
  - Product redistribution: bank product catalog (Product Lifecycle Management) → ESP variants (Payment Product Management)
  - Authorization callbacks: Payments Switch → Bank Gateway → ESP/Corporate participation
  - Rewards/rebate split: Rewards System (account/statement level, Tachyon) vs Billing and Collections (relationship-level rebates, Electron)
  - Data flow: Tachyon Data Mart → Bank Gateway → Corporate Data Mart / ESP Data Mart

- **ESP ↔ Corporate Portal**
  - Program provisioning: ESP creates products, corporate configures programs
  - Enrollment workflows: eligibility rules, member enrollment, card issuance
  - Billing and master statements: ESP-generated, per legal entity
  - Notification customization: ESP templates, corporate overrides, card-level preferences

- **Bank ↔ Corporate (indirect, mediated through ESP)**
  - CF utilization and budget enforcement at authorization
  - Posting data flow: L1/L2/L3 transaction data
  - Regulatory and fraud notifications: non-suppressible, bank-originated

- **Corporate Portal ↔ Corporate Systems**
  - Card issuance triggered from PO/invoice (AP systems)
  - Posting data pushed to GL (ERP)
  - Reconciliation matching (AP/AR systems)
  - Expense report integration (Expense Management)
  - Booking-linked issuance (Travel Booking systems)
  - Settlement positioning (Treasury)
  - Member/user provisioning and authentication (IAM/Directory)
  - Spend event triggers (LoB Applications)

---

### Slide 16: Bank Domain Entities

**What exists in Tachyon — the bank's model of the world.**

| Entity | Context | Description |
|---|---|---|
| Customer — HAH | CLM | Headless Account Holder; quasi-customer, no KYB/KYC required |
| Customer — LAH | CLM | Legal Account Holder; legal person subject to KYB |
| Customer — RAH | CLM | Real Account Holder; real person subject to KYC |
| Credit Facility | Credit & Risk | Per legal entity, per currency; bank's risk exposure; one facility per LAH per currency |
| Account Product | Product Catalog | Billing cycle, delinquency controls, base fees, single currency; organized as Product Family → Product |
| Virtual Card Product | Product Catalog | Scheme, BIN ranges, settlement/dispute rules; organized as Product Family → Product |
| VBO | Partner Management | Virtual Bank Officer; partner authorized to resell/distribute bank products; every ESP is a VBO of the bank |

- Commonwealth's catalog: AP-US-30, AP-US-45, AP-UK-30, AP-IN-30 (Account Products); VCP-Visa-US, VCP-MC-Global, VCP-RuPay-IN (Virtual Card Products)
- Same products serve multiple ESPs — differentiation happens at the variant layer

---

### Slide 17: ESP Domain Entities

**What exists in Electron — the ESP's model of the world.**

| Entity | Context | Description |
|---|---|---|
| ESP Account Variant | Product Design | Customizes a bank Account Product with component programs: fees, interest, statement, rewards, rebates, notifications |
| ESP Virtual Card Variant | Product Design | Customizes a bank Virtual Card Product with component programs: embossing, spend policy, auth rules, tokenization, 3DS, card fees, notifications |
| Corporate Payment Product | Product Design | Exactly one Account Variant + one Virtual Card Variant = one CPP; tagged to one Spend Archetype; carries baseline spend policy, card profile template, product-level commercial terms |
| Client Contract | Client Management | ESP–corporate relationship: legal provenance, archetype scope, relationship-level commercial terms, duration/renewal |

- Apex's four CPPs for Meridian: Supplier Pay, Corporate Spend, Travel Pay, Subscription Manager
- Assembly rule: 1 Account Variant + 1 Virtual Card Variant = 1 Corporate Payment Product
- Product-level terms (e.g., 1.5% interchange rebate on supplier pay) are distinct from relationship-level terms (e.g., 50 bps on aggregate spend > $10M/quarter)

---

### Slide 18: Corporate Domain Entities

**What exists in the Corporate Portal — the corporate's model of the world.**

| Entity | Context | Description |
|---|---|---|
| Organizational Unit (OU) | Organization Management | Hierarchical trees: Legal Entities, Business Units, Geographic Units, Functional Units, Customer Segments |
| Corporate Payment Program | Program Administration | Operational instance of a CPP: authority, audience, governance, spend profile, booking profile, settlement profile |
| Budget | Financial Control | Hierarchical subdivision of Credit Facility; purposeful allocation; over-allocation allowed with hierarchical enforcement |
| Member | Member & Enrollment | Participant in a program: Employee, Supplier, Contractor, Client |
| Enrollment | Member & Enrollment | Association of member to program + card provisioning; includes virtual card assignment and card-level overrides |
| Settlement Account | Financial Control | External bank account for corporate settlement; one per program |

- Meridian's landscape: 3 legal entities, 18,000+ members, OU trees by function/geography/legal entity
- Programs: Meridian US Supplier Payments ($30M budget), Engineering Spend ($4M), Client Travel ($5M), SaaS Subscriptions ($5M)

---

### Slide 19: Entity Relationships Across Domains

**How bank products become ESP variants become corporate programs — the derivation chain.**

```
Bank Product Catalog          ESP Variant Layer           Corporate Program Layer
─────────────────────         ─────────────────           ──────────────────────
Account Product ──────────→ ESP Account Variant ──┐
                                                  ├──→ Corporate Payment Product ──→ Corporate Payment Program
Virtual Card Product ─────→ ESP Virtual Card Variant ┘
                                                            ↑
Credit Facility ──────────────────────────────────────────────┘ (program draws from CF via Budget)
```

- Bank retains: credit/AML/sanctions/compliance, delinquency, base fees, scheme obligations
- ESP adds: branding, component programs (fees, rewards, notifications), commercial terms, onboarding
- Corporate configures: budget allocation, spend policy tightening, booking rules, eligibility, enrollment, settlement

---

### Slide 20: Hierarchies — Corporate's and ESP's View

**The corporate sees multiple interlocking hierarchies. The ESP correlates them.**

- **Credit hierarchy:** Corporate → LAH → Credit Facility → Budget/Limit Hierarchy → Program → Account → Cards
- **Organizational hierarchy:** Corporate → OU → Program → Account → Cards
- **Settlement hierarchy:** Corporate → Settlement Accounts → Programs → Account → Cards

Each hierarchy answers a different question:
- Credit: "How much can we spend?" (risk-anchored, bank-enforced)
- Organizational: "Who owns this spend?" (governance-anchored, corporate-defined)
- Settlement: "How do we pay for it?" (treasury-anchored, corporate-operated)

Entity system-of-residence: Credit Facility in Tachyon, Budget in Electron, OU in Electron, Settlement Account external — correlated at the Program level

---

### Slide 21: Hierarchies — Bank's View

**The bank sees a simpler, risk-anchored hierarchy.**

- LAH → Credit Facility → Limit Hierarchy → Account → Cards

The bank does not see:
- Departments, cost centers, or project codes
- Budget allocations or OU trees
- Settlement account preferences
- Member roles or enrollment logic

The bank enforces:
- Credit Facility capacity
- Budget hierarchy (utilization at authorization, all ancestors checked)
- Spend Policy (as defined by the effective policy cascade)
- Non-overridable controls (AML, sanctions, fraud, delinquency, NPA)

This separation is by design — the bank focuses on risk and compliance; the corporate focuses on governance and operations

---

## Act 4 — How the Story Becomes Data

### Slide 22: Corporate Payment Program's Reflection on Bank's Entities

**Every corporate program has a precise footprint in the bank's entity model.**

A single program creates or references:
- One Credit Facility (via the legal entity)
- One or more Budget nodes (hierarchical allocation from CF)
- One Account (for supplier/recurring archetypes: one account per program; for employee/travel: one account per member)
- One or more Virtual Cards (issued per enrollment, per transaction, or per merchant — archetype-dependent)
- An effective Spend Policy (product baseline → program tightening → card-level overrides)
- A Booking Profile (GL, cost center, project attribution rules)
- A Settlement Profile (settlement account, auto-sweep or manual, billing timing)

The bank sees the account, card, and CF utilization. The corporate sees the program, budget, enrollment, and attribution. Both views are consistent because they share the same underlying entities.

---

### Slide 23: Policy Cascade — Tighten-Only, Bank-Enforced

**Controls narrow at each level. No level can widen what the level above has set.**

```
Level 1: Bank Base (Account Product)     — broadest: all MCCs, high limits, all currencies
    ↓ tighten only
Level 2: ESP Variant (Product Spend Policy)  — archetype-appropriate: AMC restrictions, category limits
    ↓ tighten only
Level 3: Corporate Program              — program-specific: budget, AMC subset, per-tx and velocity limits
    ↓ tighten only
Level 4: Card Profile                   — card-specific: single-use, exact amount, merchant-locked
```

- Example: Apex product allows per-tx $1,000,000 and 500 tx/month; Meridian Supplier Program tightens to $500,000 per-tx, AMC-Logistics + AMC-Cloud only, 50 tx/month; a specific supplier card tightens further to $25,000 single-use, AMC-Logistics only
- The bank evaluates the effective policy (the intersection of all four levels) at authorization — there is no "override" path

---

### Slide 24: Authorization Flow

**Every transaction follows the same path. The bank is the single enforcement point.**

```
Merchant → Payment Network → Commonwealth (Tachyon)
                                  │
                                  ├─ Card active?
                                  ├─ Account active?
                                  ├─ Credit Facility capacity?
                                  ├─ Budget capacity? (ancestor chain)
                                  ├─ Spend Policy? (AMC, amount, currency, geo, velocity)
                                  ├─ Non-overridable controls? (AML, sanctions, fraud, delinquency)
                                  │
                                  ├─ [Optional] Callback to Apex (ESP) → authorization input
                                  ├─ [Optional] Callback to Meridian (Corporate) → authorization input
                                  │
                                  ├─ Bank aggregates all inputs, makes final decision
                                  │
                                  └─ Response → Payment Network → Merchant
```

- Non-overridable controls cannot be relaxed by ESP or corporate: AML screening, sanctions, fraud scoring, regulatory holds, delinquency/NPA blocks, CF breaches
- Posting after clearing: updates balance, CF utilization, budget consumption, rewards/rebates computation

---

### Slide 25: Transaction Posting — L1/L2/L3 Data

**Every posted transaction carries data from three sources, enabling end-to-end attribution and reconciliation.**

| Data Level | Source | Content |
|---|---|---|
| L1 (Network core) | Payment Network | Amount, currency, MCC, merchant ID, date, authorization code |
| L2 (Tax and references) | Merchant | Tax amount, tax rate, customer reference, merchant order ID |
| L3 (Line items) | Merchant | Item descriptions, quantities, unit prices, commodity codes |

**Card tags** (set at issuance by corporate): PO number, invoice number, cost center, project code, GL account, client code — these ride alongside the transaction and enable booking/attribution

- Three sources: Network provides L1; Merchant enriches with L2/L3; Payer/Cardholder contributes via card tags set at issuance
- Archetype determines data richness: supplier transactions carry deep L2/L3 for three-way match; employee spend may have minimal L3
- Example: LogiCorp invoice — $47,250, MCC 5085, PO-2847, INV-9921, three L3 line items with quantities, unit prices, and commodity codes

---

### Slide 26: Comprehensive Manifestation at Every Spend/Transaction/Posting

**At every transaction, every entity across all three domains is touched. The posting attributes and their association with entities across domains.**

For a single authorized and cleared transaction, the following entities are associated:

| Domain | Entity | What is recorded/updated |
|---|---|---|
| Bank | Credit Facility | Utilization updated (authorized amount held, cleared amount settled) |
| Bank | Account | Balance updated, posting recorded |
| Bank | Virtual Card | Transaction count, lifecycle state (closed if single-use) |
| Bank | Spend Policy (effective) | Compliance verified at authorization |
| ESP | Corporate Payment Product | Product-level rebate/reward computed |
| ESP | Client Contract | Relationship-level aggregate tracked |
| Corporate | Program | Program-level reporting, budget utilization |
| Corporate | Budget | Hierarchy-aware consumption (all ancestors updated) |
| Corporate | Booking Profile | GL, cost center, project, client attribution applied |
| Corporate | Member/Enrollment | Cardholder activity recorded |
| Corporate | Settlement Profile | Transaction included in next billing cycle |

- The bank sees a transaction on an account. The corporate sees a governed spend event with full attribution. Both are the same event viewed through different lenses.

---

## Act 5 — Program Lifecycle and Extensibility

### Slide 27: Large-Scale Virtual Card Program Lifecycle — Overview

**A program's lifecycle spans setup, operations, and financial management — each with distinct system interactions.**

1. Credit Facility extended by bank to legal entity
2. Program created by corporate, linked to Corporate Payment Product and Credit Facility
3. Budget allocated from Credit Facility
4. Eligibility rules defined (who may be enrolled)
5. Members enrolled, cards issued (with or without second-factor verification)
6. Transactions authorized — interceptor callbacks for ESP/corporate participation
7. Notifications delivered — authorizations, clearances, card expiry, closure
8. Fraud notifications received (bank-originated, non-suppressible)
9. Program statement generated with rebates and rewards
10. Transactions reconciled against AP/AR/expense/booking systems
11. Statement auto-repaid or manually settled
12. Disputes initiated and resolved through bank dispute process

---

### Slide 28: Setup Phase

**From credit facility to first card issued.**

- Bank extends Credit Facility to legal entity (KYB completed, limit set, covenants defined)
- Corporate selects Corporate Payment Product from ESP's catalog
- Program created: budget allocated, spend policy configured, booking profile set, settlement profile defined
- Eligibility rules established: member type, OU affiliation, approval requirements
- Members enrolled: eligibility verified → optional approval → optional KYC → account provisioned → card issued
- Card issuance: with or without second-factor verification; card carries tags (PO, cost center, project code) set at issuance
- For supplier programs: card issuance is typically API-triggered from ERP/AP system per approved invoice

---

### Slide 29: Operational Phase

**Day-to-day transaction processing and monitoring.**

- Interceptor callbacks: ESP and/or corporate receive authorization requests for optional participation (approve, decline, enrich posting data)
- Authorization notifications: real-time alerts on approvals and declines
- Clearance notifications: confirmation of settled transactions with final amounts
- Card lifecycle events: expiry warnings, closure confirmations, renewal triggers
- Fraud notifications: bank-originated, non-suppressible; corporate receives alerts for member communication
- Budget monitoring: threshold-based alerts (e.g., 75%, 90% utilization) at budget and program level
- Card management: suspend, reactivate, close, replace, modify limits — within program policy bounds

---

### Slide 30: Financial Phase

**Billing, settlement, reconciliation, and dispute resolution.**

- Program statement: generated by ESP (Electron), aggregates all accounts in the program, includes rebates and rewards computation
- Master statement: for multi-account programs (e.g., employee spend with 200+ accounts), a single consolidated view
- Reconciliation: transaction data matched against corporate systems — PO/invoice match (supplier), expense reports (employee), itineraries (travel), contracts (recurring)
- Auto-repayment: settlement profile defines auto-sweep on due date from designated settlement account
- Manual settlement: corporate may choose manual payment for disputed or exception transactions
- Disputes: initiated through bank dispute process; credits follow original booking attribution; settlement follows program profile
- Rebates: product-level (e.g., 1.5% on interchange) via Tachyon; relationship-level (e.g., 50 bps on aggregate > $10M/quarter) via Electron

---

### Slide 31: Embedding and Extension

**The platform supports deep integration with corporate systems and cooperative authorization.**

**ERP Embedding through ESP APIs**
- AP systems trigger card issuance via API for approved invoices/POs
- Posting data pushed to GL systems for automated journal entries
- Reconciliation data exported for three-way match in AP systems
- Expense management systems receive transaction data for policy compliance checks
- Travel booking systems trigger lodge card or per-booking card issuance

**Cooperative Authorization**
- Authorization Decision: ESP and/or corporate participate in real-time authorization via callbacks — can approve, decline, or add conditions (bank retains final authority and non-overridable controls)
- Posting Enrichment: at clearing, corporate systems can enrich posting data with additional attribution (project codes, client codes, GL overrides) before final booking

---

## Act 6 — The Opportunity

### Slide 32: Meridian End-to-End

**One corporate, four archetypes, three legal entities, one platform — all running simultaneously.**

| Program | Archetype | Budget | Cards | Lifecycle | Reconciliation |
|---|---|---|---|---|---|
| US Supplier Payments | Supplier | $30M from $50M CF | Single-use per invoice | API-issued, closed after clearing | PO/invoice match, L2/L3 |
| Engineering Spend | Employee | $4M from $50M CF | Persistent per employee | Self-enrollment, renewable | Expense reports, MCC match |
| Client Travel | Travel | $5M from $50M CF | Per-booking or lodge | Booking-triggered | Itinerary match |
| SaaS Subscriptions | Central Recurring | $5M from $50M CF | One per merchant | Contract-aligned lifecycle | Contract/renewal match |

- UK and India legal entities run parallel programs with local currency CFs (£12M, ₹400M)
- All four archetypes share one Credit Facility hierarchy, one OU structure, one member base, one settlement infrastructure
- Apex manages all four Corporate Payment Products; Commonwealth authorizes all transactions through one policy cascade
- Finance sees consolidated exposure across all programs, all legal entities, all currencies

---

### Slide 33: Next Steps / Engagement Path

**Where to go from here.**

- Platform deep-dive: walk through a specific archetype end-to-end with your team's use case
- Product catalog design workshop: map your existing card products to the Account Product / Virtual Card Product model
- ESP partner discussion: how VBO partners would create variants and Corporate Payment Products on your platform
- Pilot scoping: identify a corporate client and archetype for proof-of-concept
- Technical architecture review: Tachyon + Electron integration, API capabilities, authorization flow

---

## Speaker Notes — General Guidance

- Use Meridian/Apex/Commonwealth as the running example throughout — they are fictitious but comprehensive (3 legal entities, 18,000 employees, 4 archetypes, multi-currency)
- Define Tachyon-specific terms (HAH, LAH, RAH, VBO) when they first appear — don't assume the audience knows them
- The three-domain separation is the central architectural argument — return to it whenever the audience asks "who owns this?"
- Avoid commercial voice — frame capabilities as architectural decisions, not product features
- The policy cascade (tighten-only, bank-enforced) is the key technical differentiator — spend time on Slide 23
- The bounded context slide (Slide 14) is where the audience will anchor their understanding of system scope — be prepared for deep questions here
- The value realized slide (Slide 13) is where commercial interest peaks — have specific numbers ready for each stakeholder
