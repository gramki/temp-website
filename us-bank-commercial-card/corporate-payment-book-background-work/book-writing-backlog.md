<!-- CO-MAINTAINED: Any new input must be evaluated for updates to this file, presentation-outline.md, and presentation-contents-discussion.md simultaneously. -->

# Book Writing Backlog

**Source:** Presentation planning discussions for "Corporate Payments by Design"  
**Context:** While designing a bank-prospect presentation, several concepts were discussed in depth that go beyond what the book currently covers. The book treats entities and relationships but does not detail the underlying systems, data flows, integration architecture, or stakeholder economics at the level needed to convince a bank prospect. These items should be incorporated into the book to make it complete.

---

## 1. Tachyon Customer Entity Types (HAH, LAH, RAH)

**Currently in the book:** The book references "Legal Entity" and uses it for KYB and Credit Facility anchoring. It does not define the Tachyon CLM entity types.

**What needs to be added:**

- **HAH (Headless Account Holder):** A quasi-customer in the bank's CLM system. Represents logical entities that may not require KYB or KYC. Used for entities that need account-level representation without full regulatory onboarding.
- **LAH (Legal Account Holder):** Represents a legal person (organization) subject to KYB obligations. This is the entity the book currently calls "Legal Entity" in the context of Credit Facilities. The Tachyon-specific term should be introduced and mapped.
- **RAH (Real Account Holder):** Represents a real person subject to KYC obligations. Relevant for individual cardholders who have direct bank relationships or for Member entities that require KYC as part of enrollment.

**Where it fits:** Chapter 7 (*Account Product and Virtual Card Product*) and Chapter 19 (*Onboarding — ESP and Corporate Legal Entities*) should introduce these terms and explain how they map to the book's existing "Legal Entity" and "Member" concepts. Chapter 6 (*Corporate, Legal Entity, Organizational Unit, and Members*) should cross-reference.

**Running example impact:** Commonwealth onboards Meridian's three legal entities as three LAHs. Individual employees enrolled in programs may be represented as RAHs where KYC is required. HAHs may be used for logical groupings or entities that don't require regulatory onboarding.

---

## 2. VBO (Virtual Bank Officer)

**Currently in the book:** The book describes the ESP's relationship to the bank as a "partner" but does not use the Tachyon term VBO or explain the partner model formally.

**What needs to be added:**

- **VBO (Virtual Bank Officer):** A specific kind of bank partner authorized by the bank to resell or distribute the bank's products, typically through value-added services. In the corporate payments scope, every ESP is a VBO of the bank. The ESP provides corporate payments-specific value-added services on top of the bank's products.
- The VBO concept establishes the formal relationship: the bank authorizes the VBO to access its product catalog (Account Products, Virtual Card Products), create Variants, and distribute Corporate Payment Products to corporates.
- VBO is a Tachyon (bank-side) entity — the bank manages VBO relationships, grants catalog access, and defines what the VBO can and cannot modify.

**Where it fits:** Chapter 18 (*Account Products and Virtual Card Products — The Bank's Building Blocks*) should define VBO as a bank-side entity. Chapter 19 (*Onboarding*) should describe ESP onboarding as VBO registration. Chapter 21 (*ESP-Wide Concerns*) should reference it from the ESP's perspective.

**Running example impact:** Apex Payments is a VBO of Commonwealth National Bank. Commonwealth's product catalog is "redistributable" to Apex (and other VBOs). Apex's authorization to create Variants and CPPs derives from its VBO status.

---

## 3. Product Family Hierarchy in the Bank Domain

**Currently in the book:** The book defines Account Product and Virtual Card Product as individual entities. It does not describe the Product Family → Product hierarchy that exists in Tachyon.

**What needs to be added:**

- **Product Family → Product** hierarchy for both Account Products and Virtual Card Products. A Product Family groups related products (e.g., all USD 30-day billing cycle Account Products). Products within a family share structural characteristics.
- The bank's product catalog is organized as: Product Family → Product. ESPs create Variants from individual Products, not from Product Families.
- Credit Facilities also have a hierarchy: Product, Program, Variant — parallel to the Account and Virtual Card structures.
- Account and Virtual Card entities in Tachyon follow a **Product Family → Product → Program → Variant** hierarchy. This is the bank's internal organizational structure — the book currently shows only the Product level and above (from the ESP perspective).

**Where it fits:** Chapter 7 (*Account Product and Virtual Card Product*) should be expanded to describe the Product Family grouping. Chapter 18 (*Account Products and Virtual Card Products — The Bank's Building Blocks*) should describe the full hierarchy from the bank's perspective.

**Running example impact:** Commonwealth's AP-US-30 and AP-US-45 might belong to the same "US Dollar Commercial" Product Family. VCP-Visa-US and VCP-MC-Global might belong to different Product Families (scheme-specific).

---

## 4. DDD-Style Bounded Contexts / Systems View

**Currently in the book:** The book separates entities into three domains (Bank, ESP, Corporate) and assigns ownership. It does not describe the systems or subsystems within each domain, nor does it use DDD-style bounded context thinking.

**What needs to be added:**

A new section or chapter describing the bounded contexts (subsystems) within each domain:

**Tachyon (Bank) — 14 subsystems of relevance:**
1. Customer Lifecycle Management — manages HAH, LAH, RAH; handles KYB/KYC workflows
2. Product Lifecycle Management — Account Product Families, Virtual Card Product Families; catalog creation, versioning, redistributability
3. BaaS Management — manages Virtual Banking Operators (VBOs); ESP onboarding, catalog access grants, partner agreements
4. Credit Management — Credit Facilities, Limit Hierarchy, Revolving and Non-revolving Credit Accounts, Secured Credit Accounts
5. Accounting System — Accounting, Fees, Interest, Billing, Statements (account-level financial operations)
6. Payments Switch — real-time authorization routing, network connectivity, scheme message processing
7. Payments Hub — clearing, settlement, posting; end-to-end payment lifecycle orchestration
8. Rewards System — Reward Programs, Rebate Programs at Account and Statement level (product-level rewards)
9. FRM (Fraud and Risk Management) — real-time fraud scoring, transaction monitoring, risk decisioning
10. Disputes Management — chargeback processing, representment, dispute case lifecycle
11. Consumer IAM — cardholder/member authentication, credential management
12. Enterprise IAM — bank staff, ESP staff, corporate admin authentication and access control
13. Notification — bank-originated notifications (regulatory, fraud, lifecycle events); non-suppressible alerts
14. Operations Hub — bank operations console for monitoring, exception handling, servicing
15. Data Mart — bank-side analytical data store for reporting, risk analytics, regulatory reporting

**Electron (ESP) — 7 subsystems of relevance:**
1. Client Contract Management — Corporate and Contract lifecycle; relationship-level terms, scope, duration, renewal
2. Payment Product Management System — Account Variants, Virtual Card Variants, CPP assembly; component programs (fees, interest, rewards, rebates, notifications, spend, auth, tokenization, 3DS, card fees)
3. Payment Program Management System — Program configuration, Spend Policy, Booking/Settlement Profiles, eligibility rules, enrollment workflows, member and card management
4. Billing and Collections System — Consolidated Invoices, Relationship-level Rebates, Rewards, Volume Commitments, Auto Debit
5. Bank Gateway — Anti-corruption and Translation layer between Electron and Tachyon; maps ESP domain concepts to bank domain entities and vice versa
6. Corporate Data Mart — comprehensive data regarding all programs, invoices, transactions, members; Data Extracts and Reports for corporates
7. ESP Data Mart — analytics on Contracts, Products, and Programs for the ESP's own portfolio management

**Electron Corporate Portal bounded contexts** (these are capabilities within the Payment Program Management System and related subsystems):
- Organization Management — manages OU hierarchies, legal entity associations
- Program Administration — manages Programs, Spend Policy configuration, Booking Profiles, Settlement Profiles
- Member & Enrollment Management — manages members, eligibility rules, enrollment workflows, card issuance
- Financial Control — manages budgets (hierarchical), settlement accounts
- Operations — reconciliation workflows, dispute management

**Key architectural elements not in the book:**
- **BaaS Management** is the Tachyon subsystem through which ESP/VBO relationships are formally managed — the book describes the relationship conceptually but does not name the system
- **Bank Gateway** is Electron's anti-corruption and translation layer to Tachyon — this is architecturally critical and entirely absent from the book. It is the seam through which all Electron↔Tachyon communication flows, mapping ESP domain concepts (variants, CPPs, programs) to bank domain entities (products, accounts, CFs) and vice versa
- **Payments Switch vs Payments Hub** — the book conflates authorization and clearing/settlement into "Transaction Processing"; these are distinct Tachyon subsystems with different responsibilities
- **Accounting System** — the book does not distinguish the accounting/fees/interest/billing/statements subsystem from credit management or transaction processing
- **Two IAM subsystems** — Consumer IAM (for cardholders/members) and Enterprise IAM (for bank/ESP/corporate staff) serve different populations; the book does not distinguish them
- **Two Data Marts in Electron** — Corporate Data Mart (for corporate reporting and extracts) and ESP Data Mart (for ESP portfolio analytics) serve different audiences; the book does not describe either
- **Tachyon Data Mart** — bank-side analytical data; absent from the book
- **Operations Hub** — bank operations console; absent from the book

**Where it fits:** This should be a new chapter in Part II (*The Ontology*) or as expanded introductions to Parts III and IV. The Bank Gateway specifically deserves mention in any chapter that discusses Electron↔Tachyon communication (Ch 7, 8, 18, 19, 20, 21). The two Data Marts and the Billing and Collections System should be reflected in the financial/operational chapters.

**Running example impact:** Each subsystem can be illustrated with Commonwealth/Apex/Meridian responsibilities. Commonwealth's BaaS Management onboards Apex as a VBO. Apex's Bank Gateway translates Apex's variant configurations into Commonwealth's Tachyon product model. Commonwealth's Payments Switch routes Meridian's authorization requests; Payments Hub handles clearing and settlement. Tachyon's Rewards System computes product-level rewards; Electron's Billing and Collections computes relationship-level rebates. Corporate Data Mart provides Meridian with program-level reporting and data extracts.

---

## 5. Corporate Domain Systems Landscape

**Currently in the book:** The book describes the Electron Corporate Portal's capabilities (programs, budgets, members, enrollment, reconciliation) but does not describe the broader corporate systems ecosystem that interacts with it.

**What needs to be added:**

The corporate domain is not a single system — it is a constellation of purpose-built systems that integrate through the Electron Corporate Portal:

- **AP Systems** (e.g., SAP Ariba, Oracle AP, Coupa) — supplier payment automation, PO/invoice matching, card issuance triggers. For supplier payment archetypes, the AP system is the trigger: an approved PO/invoice initiates card issuance via API.
- **AR Systems** — receivables matching, payment application, customer payment tracking. Relevant for corporates that use virtual cards in a buyer-supplier context where the supplier's AR needs to match card payments.
- **Expense Management Systems** (e.g., Concur, Navan, Brex) — employee spend capture, receipt matching, policy compliance. For employee spend archetypes, these systems receive transaction data and manage expense report workflows.
- **Travel Booking Systems** (e.g., Amex GBT, CWT, Navan) — lodge card integration, booking-linked card issuance. For travel archetypes, booking systems trigger card issuance (per-booking virtual card or lodge card to agency).
- **ERP / GL Systems** (e.g., SAP, Oracle, NetSuite) — GL posting, cost center attribution, financial consolidation. Transaction posting data flows from the Electron portal to the ERP for journal entry creation.
- **Treasury Systems** (e.g., Kyriba, FIS) — settlement account management, cash positioning, FX management. Treasury manages the corporate's settlement accounts and funding for auto-sweep or manual settlement.
- **IAM / Directory Services** (e.g., Okta, Azure AD, Ping) — member and user provisioning, role assignment, authentication for ESP and bank portal access, SSO and MFA enforcement. Corporate IAM contributes the member base, user identities, and role assignments that the Electron portal consumes.
- **LoB Applications** — department-specific or vertical-specific applications that consume card data or trigger spend events. These are custom or industry-specific systems that participate in the spend lifecycle.

**Where it fits:** This should be added to Chapter 26 (*Corporate-Wide Concerns*) as a section on "Corporate Systems Integration" or as a new chapter in Part V. It could also be reflected in Chapter 14 (*Users and Roles*) for the IAM/Directory Services aspect, and in the per-archetype program chapters (27-30) for archetype-specific system interactions.

**Running example impact:** Meridian's AP system (SAP Ariba) triggers single-use card issuance for approved POs; Meridian's expense management system (Concur) receives transaction data for employee spend; Meridian's ERP (SAP) receives posting data for GL entries; Meridian's IAM (Azure AD) provisions users and members and provides SSO to the Electron portal.

---

## 6. Context Boundaries and Integration Points

**Currently in the book:** The book describes entity relationships across domains and data flows (posting, authorization, onboarding) but does not systematically catalog the integration boundaries and what crosses each boundary.

**What needs to be added:**

A systematic description of the four integration boundaries:

**Bank ↔ ESP (mediated through the Bank Gateway):**
- Product redistribution: Product Lifecycle Management (Tachyon) → Bank Gateway → Payment Product Management (Electron); catalog access granted via BaaS Management (VBO relationship)
- Authorization callbacks: Payments Switch (Tachyon) → Bank Gateway → ESP/Corporate participation
- Rewards/rebate split: Rewards System (account/statement level, Tachyon) vs Billing and Collections (relationship-level rebates, Electron)
- Data flow: Tachyon Data Mart → Bank Gateway → Corporate Data Mart / ESP Data Mart
- The Bank Gateway is the anti-corruption layer — it ensures Tachyon's model (accounts, products, CFs) and Electron's model (variants, CPPs, programs, contracts) stay clean; the gateway translates between them
- What does NOT cross this boundary: corporate OUs, members, budgets, booking profiles — the bank does not see these

**ESP ↔ Corporate Portal:**
- Program provisioning: ESP creates and publishes CPPs; corporate selects and configures programs
- Enrollment workflows: eligibility rules defined by corporate; enrollment processed through ESP; card issuance involves both Electron and Tachyon
- Billing and master statements: ESP-generated per billing cycle, per legal entity; master statement aggregates multi-account programs
- Notification customization: ESP defines templates; corporate customizes thresholds, channels, preferences; card-level overrides

**Bank ↔ Corporate (indirect, mediated through ESP):**
- CF utilization and budget enforcement at authorization: the bank checks budget hierarchy (even though budgets are corporate-defined) as part of the authorization cascade
- Posting data flow: L1/L2/L3 transaction data flows from bank through ESP to corporate systems
- Regulatory and fraud notifications: non-suppressible, bank-originated; corporate receives for member communication and compliance

**Corporate Portal ↔ Corporate Systems:**
- AP: card issuance triggered from approved PO/invoice
- ERP/GL: posting data pushed for automated journal entries
- AP/AR: reconciliation matching
- Expense Management: transaction data for policy compliance and expense reports
- Travel Booking: lodge card or per-booking card issuance triggers
- Treasury: settlement account management, funding, cash positioning
- IAM/Directory: member/user provisioning, role assignment, authentication (SSO/MFA)
- LoB Applications: card data consumption, spend event triggers

**Where it fits:** This could be a new section in the Bridge chapter (*From Concepts to Entities*) or a new chapter in Part II. It provides the "how systems talk" view that complements the "what entities exist" view already in the book.

---

## 7. Stakeholder Value Realization (Detailed Breakdown)

**Currently in the book:** The book mentions value propositions implicitly (e.g., ESP earns revenue, corporate gains control) but does not systematically catalog the value each stakeholder captures.

**What needs to be added:**

A structured breakdown of value per stakeholder:

- **Bank:** Float income (credit facility utilization), customer retention (sticky multi-program relationships), network incentives (volume-based), network interchange (per-transaction), account and card fees (base fees from Account Products), regulatory compliance as competitive moat
- **ESP:** Revenue share from bank (portion of float, interchange, other fees as negotiated in VBO terms), direct fees and charges from corporate (per Client Contract), portfolio scale (one ESP serves 40+ corporates, amortizing product design costs), branding and market positioning
- **Corporate:** Control and governance benefits (mandate enforcement reduces policy leakage), AP automation story (DPO extension, e.g., ~12 days on $50M annual payables), rebates (product-level and relationship-level), rewards, reconciliation labor reduction (e.g., 95%+ auto-match for supplier programs)
- **Members (of various types):** Cashflow benefits (supplier: faster payment improves DSO; employee: simplified expense flow), negotiated MDRs (supplier), AR story (supplier: payment certainty), expense simplification (employee), travel convenience (employee/traveler)

**Where it fits:** This could be a new section in Chapter 1 (*The Corporate Payments Problem*) or Chapter 3 (*Two Lenses — Why the Gap Exists*), or as a standalone section in the front matter. It provides the economic rationale for the three-domain model.

**Running example impact:** Apex earns 1.5% interchange rebate on supplier pay (product-level, Tachyon) + 50 bps on aggregate spend > $10M/quarter (relationship-level, Electron). Meridian's CFO evaluates on reconciliation labor saved, DPO extension, and policy leakage prevention. Commonwealth earns from facility (interest/float), accounts (fees), and network (interchange).

---

## 8. Three Interlocking Hierarchies

**Currently in the book:** The book describes Credit Facility → Budget → Account hierarchy and OU → Program hierarchy separately. It does not present them as three parallel, interlocking hierarchies that are correlated at the Program level, each answering a distinct question.

**What needs to be added:**

Three parallel hierarchies visible from the corporate's and ESP's perspective:

- **Credit hierarchy:** Corporate → LAH → Credit Facility → Budget/Limit Hierarchy → Program → Account → Cards  
  Answers: "How much can we spend?" (risk-anchored, bank-enforced)

- **Organizational hierarchy:** Corporate → OU → Program → Account → Cards  
  Answers: "Who owns this spend?" (governance-anchored, corporate-defined)

- **Settlement hierarchy:** Corporate → Settlement Accounts → Programs → Account → Cards  
  Answers: "How do we pay for it?" (treasury-anchored, corporate-operated)

These hierarchies are independent but correlated at the Program level. Each entity has a system-of-residence: Credit Facility in Tachyon, Budget in Electron, OU in Electron, Settlement Account external.

Contrast with the **bank's view** — a single, simpler hierarchy: LAH → CF → Limit Hierarchy → Account → Cards. The bank does not see OUs, cost centers, project codes, budget allocations, settlement preferences, or member roles. This is by design.

**Where it fits:** Chapter 9 (*Credit Facility, Budget, and Account*) should present the three hierarchies explicitly and name them. Chapter 26 (*Corporate-Wide Concerns*) touches on this but should cross-reference the formal hierarchy model.

---

## 9. Program's Reflection on Bank Entities

**Currently in the book:** Chapter 10 (*Corporate Payment Program*) defines the program and its components. It does not explicitly map a program's "footprint" in the bank's entity model.

**What needs to be added:**

A section describing how a single program creates or references entities across both domains:

- One Credit Facility (via the legal entity / LAH)
- One or more Budget nodes (hierarchical allocation from CF)
- One Account (for supplier/recurring archetypes: one account per program) or one Account per member (for employee/travel archetypes) — **account cardinality depends on archetype**
- One or more Virtual Cards (issued per enrollment, per transaction, or per merchant — archetype-dependent)
- An effective Spend Policy (product baseline → program tightening → card-level overrides — the intersection of all four cascade levels)
- A Booking Profile (GL, cost center, project attribution rules)
- A Settlement Profile (settlement account, auto-sweep or manual, billing timing)

The bank sees account + card + CF utilization. The corporate sees program + budget + enrollment + attribution. Both views are consistent because they share the same underlying entities.

**Where it fits:** Chapter 10 (*Corporate Payment Program*) should add a section "Program's Footprint in the Bank Entity Model" that maps each program component to its bank-side counterpart.

---

## 10. Comprehensive Manifestation at Every Transaction

**Currently in the book:** Chapter 16 (*Transaction Posting and Data*) and Chapter 20 (*Processing, Authorization, and Controls*) describe transaction data and authorization. They do not present a single comprehensive view of all entities touched per transaction across all three domains.

**What needs to be added:**

A "transaction entity association" view showing that a single authorized and cleared transaction updates or associates with entities in all three domains:

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

The bank sees a transaction on an account. The corporate sees a governed spend event with full attribution. Both are the same event viewed through different lenses.

**Where it fits:** This could be added to Chapter 16 (*Transaction Posting and Data*) as a section "Entity Association per Transaction" or as a summary diagram. It could also serve as a synthesis section in the Bridge chapter.

---

## 11. Cooperative Authorization (Detailed)

**Currently in the book:** Chapter 20 (*Processing, Authorization, and Controls*) mentions optional ESP and corporate callbacks during authorization. It does not detail the two distinct capabilities: Authorization Decision and Posting Enrichment.

**What needs to be added:**

Two distinct extension points:

- **Authorization Decision:** ESP and/or corporate participate in real-time authorization via callbacks. They can approve, decline, or add conditions. The bank retains final authority and non-overridable controls. Timeout fallback behavior should be defined (typically: proceed with bank decision if callback times out).
  - Example: Meridian's AP system receives a callback, verifies the PO is still open and unfulfilled, confirms authorization — all within network timeout.

- **Posting Enrichment:** At clearing (not authorization), corporate systems can enrich the posting data with additional attribution before final booking. This allows project code updates, GL routing adjustments, and cost center overrides based on current organizational data (which may have changed since card issuance).
  - Example: At clearing, Meridian's system updates the project code from the original (set at card issuance) to the current project phase, and adjusts GL routing based on a recent OU restructuring.

**Where it fits:** Chapter 20 (*Processing, Authorization, and Controls*) should expand the callback section into two named capabilities. Chapter 26 (*Corporate-Wide Concerns*) should reference these from the corporate operations perspective.

---

## 12. ERP Embedding through ESP APIs (Detailed Integration Patterns)

**Currently in the book:** The book mentions ERP integration in passing (e.g., "ERP triggers card issuance") but does not describe the integration patterns systematically.

**What needs to be added:**

Per-system integration patterns:

- **AP → Electron:** Approved PO/invoice → API call → card issued with exact amount, merchant lock, and tags (PO number, invoice number, cost center) → card credentials delivered to supplier or used directly by AP system
- **ERP/GL ← Electron:** Transaction posting data (L1/L2/L3 + card tags + booking profile attribution) → pushed to GL for automated journal entry creation. Includes: GL account, cost center, project code, tax allocation, capex/opex classification.
- **AP/AR ← Electron:** Reconciliation data exported for three-way match (PO, invoice, card payment). Auto-match rate target: 95%+ for supplier programs.
- **Expense Management ↔ Electron:** Transaction data → expense system for receipt matching and policy compliance. Expense approvals may feed back for posting enrichment.
- **Travel Booking → Electron:** Booking confirmation → card issued with itinerary tags, traveler info, booking reference. Lodge card: long-lived card shared with agency. Per-booking: individual virtual card per trip.
- **Treasury ↔ Electron:** Settlement account management, auto-sweep configuration, funding status, cash positioning for upcoming settlement dates.
- **IAM/Directory → Electron:** User and member provisioning (SCIM or similar), role assignment synchronization, SSO authentication (SAML/OIDC), MFA enforcement policies.

**Where it fits:** A new section in Chapter 26 (*Corporate-Wide Concerns*) on "Corporate Systems Integration Patterns" or a dedicated new chapter in Part V. Per-archetype program chapters (27-30) should reference the archetype-specific integration patterns.

**Running example impact:** Meridian uses SAP Ariba for AP (triggers supplier card issuance), Concur for expense management (receives employee transaction data), SAP for ERP/GL (receives posting data for journal entries), Azure AD for IAM (provisions users and members, provides SSO to Electron portal).

---

## 13. "Promise → Imagined Answer → Required Evolution" Framing

**Currently in the book:** The book's Chapter 1 (*The Corporate Payments Problem*) and Chapter 2 (*Existing Solutions*) describe the problem space directly — what corporates need and what current solutions lack. The framing is factual but flat. It lists problems and shortcomings without naming the *psychological and commercial mechanism* that creates the gap: the dynamic between what banks promise, what corporates imagine those promises deliver, and the distance between the two.

**What needs to be added:**

The opening narrative should be rewritten to adopt the "promise → imagine → required evolution" framing. This is not just a rhetorical structure — it captures a specific insight about why corporate payment programs stall:

1. **Banks describe possibilities** — and they are genuinely promising. API issuance, single-use cards, MCC restrictions, velocity limits, L2/L3 data, real-time authorization notifications. These are real innovations. They invite interest.

2. **Corporates hear those possibilities and imagine answers** to their real questions: budget enforcement across legal entities, authority chains, GL attribution per transaction, policy cascades across programs, automated reconciliation against AP/ERP. The imagining is natural and reasonable — "single-use cards" sounds like it should mean "PO-matched, budget-aware, auto-reconciled cards." But it does not.

3. **The gap lives between the promise and the imagined answer.** Neither side is wrong. Banks are not overselling. Corporates are not being unreasonable. The imagination fills a space that the product does not yet fill. That distance is the required evolution — not a criticism, but a market imperative.

The balance is critical: acknowledge the promise (banks are right), honor the imagination (corporates are right), and name the gap without blame. "Required evolution" frames the gap as forward-looking and respectful of what exists — not disruption, not transformation, but evolution.

**Action required:** Chapters 1 and 2 should be rewritten to align with this framing. The current problem description reads as a critique of existing products. It should instead read as a diagnosis of a structural dynamic — the promise-to-imagination gap — that no product on the market fully closes. Chapter 2's critique of existing solutions should be restructured to show how each solution answers the promise but not the imagined answer.

**Where it fits:** Chapter 1 (*The Corporate Payments Problem*) should open with this framing. Chapter 2 (*Existing Solutions*) should use it to structure its analysis. The framing should echo through the rest of the book — every architectural decision the platform makes exists to close the gap between the promise and the imagined answer.

**Running example impact:** Meridian's CFO evaluates on reconciliation labor saved, policy leakage prevented, and DPO extended — not on card issuance speed or MCC control granularity. When Commonwealth describes its virtual card capabilities, Meridian's team *imagines* those capabilities answering their budget, attribution, and reconciliation questions. The book should make this dynamic explicit and name it.

---

## 14. Semantic Dissonance Table

**Currently in the book:** Chapter 3 (*Two Lenses — Why the Gap Exists*) describes the bank/corporate worldview mismatch conceptually. It does not present a structured table showing specific corporate questions, bank answers, and the resulting gaps.

**What needs to be added:**

A structured table (6-8 rows) showing the semantic dissonance between corporate questions and bank answers:

| Corporate's Question | Bank's Answer | The Gap |
|---|---|---|
| "Can I issue a card per PO and close it after payment?" | "Single-use virtual cards with amount locks" | No PO-to-card linkage, no three-way match, no auto-close to AP |
| "Can I enforce department budgets, not just credit limits?" | "Credit facilities with sub-limits" | Sub-limits are risk tools, not budget governance; no OU hierarchy |
| "Can I attribute every transaction to a GL account and project code?" | "Card-level reference fields" | Fields are unstructured, unvalidated, not pushed to ERP |
| "Can I cascade a policy change to all cards in a program?" | "Per-card spend controls" | No program-level policy, no inheritance, no tighten-only cascade |
| "Can I reconcile card transactions against invoices?" | "L2/L3 transaction data" | Data available but not matched; no PO linkage, no automated recon |
| "Can I onboard a supplier through my procurement system?" | "APIs for card issuance" | Enrollment, eligibility, merchant validation unsupported |

The pattern: every answer addresses payment execution. None address governance, financial architecture, or operational dimensions. This is a semantic gap, not a feature gap.

**Where it fits:** Chapter 2 (*Existing Solutions*) or Chapter 3 (*Two Lenses*) as a structured artifact that makes the abstract gap concrete and visceral.

**Running example impact:** Each row can be illustrated with Commonwealth/Meridian examples — e.g., Commonwealth offers AP Virtual Card Products; Meridian asks "can I enforce PO matching and route GL entries per supplier category?"

---

## 15. Five Dimensions of Corporate Need

**Currently in the book:** The book discusses control, attribution, reconciliation, and compliance as aspects of the problem (Chapter 1) and introduces the Spend Mandate's eight components (Chapter 5). It does not present a unified, named framework of the five dimensions that corporate payment needs span.

**What needs to be added:**

A five-dimension framework for analyzing corporate payment needs:

1. **Payment Execution** — authorize, clear, settle reliably. Well-answered by current card products: networks, schemes, real-time auth.
2. **Financial Architecture** — credit facilities allocated as budgets, tied to organizational purpose, with hierarchical enforcement. Partially answered: credit limits and sub-limits exist, but without budget semantics or OU-awareness.
3. **Control Architecture** — policy cascades, eligibility rules, enrollment workflows, lifecycle governance across programs. Primitively answered: per-card controls exist, but no program-level policy, no inheritance, no lifecycle orchestration.
4. **Accounting & Attribution** — every transaction attributed to GL, cost center, project, client — structured, validated, pushed to ERP. Not answered: reference fields exist but lack structure, validation, and ERP integration.
5. **Reconciliation & Settlement** — automated matching against PO/invoice/booking/contract; consolidated settlement by program. Not answered: data available but matching, consolidation, and settlement management left to the corporate.

The first dimension is table stakes. The other four are where corporate payment programs succeed or fail. No corporate CFO evaluates a card program on authorization speed — they evaluate on reconciliation labor, policy leakage, and attribution accuracy.

**Where it fits:** Chapter 1 (*The Corporate Payments Problem*) or Chapter 3 (*Two Lenses*) as the analytical framework that structures the rest of the book. The Spend Mandate (Chapter 5) can be shown to map onto these five dimensions. Each archetype chapter (Chapters 22-25, 27-30) can reference how the archetype addresses each dimension.

**Running example impact:** Meridian's evaluation criteria map directly to dimensions 2-5. Dimension 1 (payment execution) is assumed.

---

## 16. Counterparty Diversity in AP Landscape

**Currently in the book:** Chapter 4 (*Spend Archetypes*) organizes corporate payments into four workflow patterns. It does not explicitly discuss the diversity of counterparty types within the AP landscape and how this diversity multiplies the governance challenge.

**What needs to be added:**

The corporate AP landscape includes at least six distinct counterparty types, each with different payment patterns, data needs, compliance requirements, and card acceptance realities:

| Counterparty Type | Payment Pattern | Data Needs | Compliance | Card Acceptance |
|---|---|---|---|---|
| Goods suppliers | PO/invoice-driven, deterministic | L2/L3, three-way match | Trade compliance, tax | Generally high |
| Service providers | Milestone or deliverable-based | SOW reference, project attribution | Contract compliance | Variable |
| Contractors | Time/expense-based, recurring | Timesheet linkage, project codes | Labor compliance, 1099 | Low — often ACH preferred |
| SaaS / software vendors | Subscription, renewal-driven | Contract ID, license count | Procurement policy | High |
| Intermediaries / agencies | Pass-through, consolidated | Booking reference, itinerary | Agency agreements, duty of care | High |
| Government / regulatory | Fee schedules, non-negotiable | Mandate reference, filing ID | Regulatory deadlines | Low — often wire/ACH |

Today's card products abstract all of these as "merchants" — a single MCC-classified entity. The corporate sees six fundamentally different relationships. This diversity multiplies the five dimensions: financial architecture for a goods supplier (PO-locked budget) looks nothing like financial architecture for a SaaS vendor (contract-locked renewal budget).

**Where it fits:** Chapter 1 (*The Corporate Payments Problem*) as context for why the problem is multi-dimensional. Chapter 4 (*Spend Archetypes*) should reference how archetypes map to or organize counterparty types. Per-archetype chapters (22-25, 27-30) should reference the specific counterparty types each archetype serves.

**Running example impact:** Meridian's AP landscape includes goods suppliers (LogiCorp), SaaS vendors (Datadog, SaaSGrid), travel intermediaries (TravelRight), and others — each with distinct governance requirements that the archetype model addresses.

---

## 17. Legacy Platform Constraints — The Promise Has Its Own Limits

**Currently in the book:** The book treats bank capabilities (Tachyon) as a given — describing what the platform provides without contrasting it against the architectural limitations of legacy processors that most banks currently operate. The implicit assumption is that the "possibilities" banks describe are fully deliverable. They are not. The processing platforms behind today's card programs were not architected for the capabilities they now promise.

**What needs to be added:**

A new section or chapter that names the architectural constraints of legacy card processing platforms (TSYS/Global Payments, Fiserv, FIS, and similar processors) — not as a competitive teardown, but as an honest assessment of the infrastructure reality that bounds what banks can deliver today. This is essential context for why the "required evolution" is architectural, not incremental.

**The constraint catalog, organized by architectural pattern:**

**1. Batch-native, not event-native:**
- Authorization notifications, clearing confirmations, and lifecycle events designed for batch file exchange, not real-time push
- No native webhook/event-driven architecture; real-time event streaming requires custom middleware
- Settlement and posting on batch cycles; real-time balance and utilization queries are difficult or unavailable

**2. Flat hierarchies, not programmable:**
- Limits and controls are per-card or per-account; no hierarchical budgets with ancestor-chain enforcement at authorization
- No program-level policy inheritance or tighten-only cascade
- Spend controls are static MCC blocks and flat amount limits; no dynamic, context-aware controls (evaluate budget hierarchy, custom merchant categories, velocity across programs)
- No custom merchant categorization (AMCs) — only static MCC codes from the network

**3. Static data fields, not contextual:**
- Transaction data carries what the network provides; no mechanism to attach, persist, or enrich with corporate context (PO number, project code, cost center, GL account) at issuance
- Reference fields exist but are unstructured, unvalidated, and not pushed to ERP
- Refunds attribution — when a credit is issued, attributing it back to the original booking profile (GL, cost center, project) is manual
- No clearing enrichment hooks — no mechanism for external systems to enrich posting data at clearing time

**4. Pre-allocated inventory, not on-demand:**
- Card numbers and BINs managed as static pools, pre-allocated in ranges
- Not designed for high-frequency, API-triggered, single-use card issuance at the scale corporate supplier programs require (hundreds or thousands per day)
- Card lifecycle management designed for call-center workflows (suspend, reactivate, close, replace), not programmatic bulk operations with per-card differentiation
- Card state granularity is coarse (active, suspended, closed); no distinction between "suspended by program admin" vs. "suspended by fraud" vs. "suspended by corporate policy"

**5. Closed authorization path, not cooperative:**
- The processor makes the authorization decision alone; no architectural hook for external participation (ESP or corporate) within network timeout windows
- No posting enrichment capability — transaction data cannot be augmented by corporate systems at clearing time
- Authorization decision and posting enrichment are the two cooperative capabilities absent from legacy architectures

**6. Token and authentication rigidity:**
- Token lifecycle not coordinated with card lifecycle events (renewal, reissuance, replacement); token-to-card mapping breaks on card replacement
- Token lifecycle, authentication lifecycle not visible to FRM — fraud systems cannot see the full credential lifecycle, creating blind spots in risk decisioning
- Authentication versatility limited — rigid handling of card-not-present vs. card-present scenarios; limited support for modern authentication methods (3DS 2.x, FIDO, biometric)
- PIN delivery and management limited to legacy channels (mail, IVR); no digital-first PIN delivery (in-app reveal, push notification, QR-based)

**7. Billing and statement rigidity:**
- Fixed billing cycles; no configurable billing periods per program or per archetype
- No master statement capability — multi-account programs (e.g., 200+ employee accounts) cannot be consolidated into a single program-level statement
- No program-level rebate/reward computation; rewards computed per account, not across a relationship

**8. Multi-currency constraints:**
- Accounts tied to a single currency; multi-currency requires separate accounts, separate reconciliation, separate reporting
- No consolidated cross-currency exposure view without manual aggregation
- FX management at transaction time is limited; no native support for corporate treasury FX policies

**Why this matters for the book's argument:** The book currently positions Tachyon's capabilities as the "right way" to build corporate payment infrastructure. Without naming what legacy platforms *cannot do*, the reader has no baseline for comparison. The architectural constraints are not bugs — they reflect the era, technology stack, and use cases these platforms were designed for. Naming them honestly establishes why the evolution is architectural, not incremental, and why it cannot be achieved by adding features to existing processors.

**Where it fits:** This should be a section in Chapter 2 (*Existing Solutions — Why Current Approaches Fall Short*) or as a new section in Chapter 3 (*Two Lenses*). It provides the infrastructure context that grounds the "required evolution" argument. Each constraint category can be cross-referenced later when the book shows how Tachyon addresses it.

**Running example impact:** Commonwealth's choice of Tachyon is not just a vendor preference — it is an architectural decision. The book should show that legacy processors could not deliver what Commonwealth's corporate payment program requires: real-time cooperative authorization, hierarchical budget enforcement, programmable spend controls, on-demand card issuance, and event-driven lifecycle management.

---

## 18. Hierarchy vs. Coordinate System — Structural Dissonance

**Currently in the book:** Chapter 3 (*Two Lenses — Why the Gap Exists*) describes the bank/corporate worldview mismatch conceptually — bank optimizes for credit risk, corporate optimizes for governance. It does not name the specific structural reason the bank's control model cannot represent the corporate's: the hierarchy-vs-coordinate-system dissonance.

**What needs to be added:**

A section that makes three structural arguments for why the bank's hierarchy of limits cannot represent corporate governance dimensions:

1. **Enterprise-specific ordering.** A hierarchy forces a fixed nesting of dimensions. Company A organizes by region → business unit → project. Company B organizes by department → client → cost center. No universal ordering exists. A platform that encodes one ordering cannot serve the others without restructuring — not reconfiguring — its hierarchy.

2. **Non-static dimensions.** Enterprises restructure. A company that organized by geography last year reorganizes by product line this year. New regulatory or compliance dimensions emerge. Each change would require rebuilding the hierarchy from scratch — the ordering itself has changed.

3. **Simultaneous multi-axis traversal.** Different governance questions require different primary axes. "What did Department X spend across all projects?" and "What did Project Alpha cost across all departments?" need different traversal orders. A hierarchy answers one efficiently — the one aligned with its fixed ordering. A coordinate system of independent dimensions answers all without structural bias.

The conclusion: a hierarchy can enforce limits along a single path with precision. But it cannot represent a governance model where dimensions are enterprise-specific, non-static, and queried in multiple orders simultaneously — without forcing a fixed ordering that no enterprise can universally commit to. The corporate's governance requires a coordinate system of concurrent dimensions, not a deeper tree.

**Existing reference:** The detailed analysis — including ERP evidence, DoA matrices, four scenario walkthroughs, middleware gap analysis, the translation problem, and cooperative authorization — is in `why-hierarchy-is-not-the-answer.md`.

**Where it fits:** Chapter 3 (*Two Lenses — Why the Gap Exists*) should add a section "Hierarchy Is Not the Answer" that presents the three structural arguments. This becomes the sharpest articulation of *why* the gap exists — not just that it exists. The section should cross-reference `why-hierarchy-is-not-the-answer.md` for the full analysis.

**Running example impact:** Commonwealth's product team has been adding deeper hierarchy — more granular limits, more sub-accounts, more MCC groups — each time Meridian requests more control. This section names why that instinct fails: Meridian's governance dimensions (department, project, cost center, client code, compliance category) cannot be nested in any single order. Meridian's CFO restructured from geography-based to product-line-based organization last year; the hierarchy would need to be rebuilt, not reconfigured.

---

## Summary: Proposed Book Changes

| # | Topic | Estimated Scope | Priority |
|---|---|---|---|
| 1 | HAH, LAH, RAH customer types | Additions to Ch 7, 19, 6 | High — fundamental to bank audience |
| 2 | VBO partner model | Additions to Ch 18, 19, 21 | High — defines ESP-bank relationship |
| 3 | Product Family hierarchy | Expansion of Ch 7, 18 | Medium — organizational detail |
| 4 | Bounded contexts / systems view (now with actual subsystem names) | New chapter or major section in Part II or III | High — essential for bank prospects |
| 4a | Bank Gateway (anti-corruption layer) | Additions to Ch 7, 8, 18, 19, 20, 21 | High — architecturally critical seam |
| 4b | Payments Switch vs Payments Hub distinction | Expansion of Ch 20 | Medium — replaces generic "Transaction Processing" |
| 4c | Accounting System (fees, interest, billing, statements) | Expansion of Ch 18, new content | Medium — distinct from credit and payments |
| 4d | Two IAM subsystems (Consumer vs Enterprise) | Additions to Ch 14, 19 | Medium — distinct populations |
| 4e | Two Electron Data Marts (Corporate vs ESP) | New content in Ch 26, 21 | Medium — reporting and analytics |
| 4f | Tachyon Data Mart | New content in Ch 18 or 20 | Medium — bank-side analytics |
| 4g | BaaS Management subsystem | Additions to Ch 18, 19 | High — formal VBO management |
| 4h | Operations Hub | New content in Ch 20 | Low — bank operations detail |
| 5 | Corporate systems landscape | New section in Ch 26 or new chapter in Part V | High — shows real-world integration |
| 6 | Context boundaries / integration points (now with subsystem-to-subsystem mapping) | New section in Bridge or Part II | Medium — complements bounded contexts |
| 7 | Stakeholder value realization | New section in Ch 1 or Ch 3 | Medium — business case support |
| 8 | Three interlocking hierarchies | Expansion of Ch 9, cross-ref in Ch 26 | High — key conceptual model |
| 9 | Program reflection on bank entities | Expansion of Ch 10 | Medium — deepens program chapter |
| 10 | Transaction entity association | Addition to Ch 16 or Bridge | Medium — comprehensive data view |
| 11 | Cooperative authorization (detailed) | Expansion of Ch 20 | Medium — extension point detail |
| 12 | ERP embedding patterns | New section in Ch 26 or new chapter | High — critical for bank adoption |
| 13 | "Promise → Imagined Answer → Required Evolution" framing | Rewrite of Ch 1, Ch 2 opening narrative | High — structural insight; rewrite problem phrasing to align |
| 14 | Semantic dissonance table | New artifact in Ch 2 or Ch 3 | High — makes the abstract gap concrete and visceral |
| 15 | Five dimensions of corporate need | New framework in Ch 1 or Ch 3 | High — analytical structure for the entire book |
| 16 | Counterparty diversity in AP landscape | Additions to Ch 1, Ch 4, archetype chapters | High — multiplier on governance complexity |
| 17 | Legacy platform constraints catalog | New section in Ch 2 or Ch 3 | High — infrastructure reality that bounds the promise |
| 18 | Hierarchy vs. Coordinate System — structural dissonance | New section in Ch 3 or standalone appendix; incorporate `why-hierarchy-is-not-the-answer.md` analysis | High — names the architectural gap; explains why hierarchy cannot represent corporate governance dimensions (enterprise-specific ordering, non-static, simultaneous multi-axis traversal) |
