# Corporate Payments Concepts — Suggested Outline

> Hybrid book structure: narrative sections build concepts progressively for first-time readers; reference sections stand alone for lookup. The two styles are clearly demarcated and never mixed within a single section.

---

## Writing Style and Preferences — Practitioner-Authoritative

> This section defines the writing style and authoring preferences for the entire book. It is an instruction to the author, not content for the reader. Follow these principles throughout.

**File structure**: Each chapter is a separate markdown file in `us-bank-commercial-card/corporate-payments-book/`. Filenames follow `NN-name.md` where NN is zero-padded digits (00, 01, 02, ...).

**Diagrams**: Use mermaid diagrams extensively to explain concepts, entity relationships, domain boundaries, control cascades, and program journeys. Every chapter should have at least one diagram where applicable.

**Examples**: Use Meridian Industries, Apex Payments, and Commonwealth National Bank as detailed, concrete examples throughout. Not just name-drops — show specific configurations, numbers, and decisions.

**Research**: For commentary on existing solutions and industry practices (particularly Chapter 2), research current market offerings and frame them accurately.

**Style**: Practitioner-authoritative. Declarative, precise, but not formal. Short sentences. Active voice. Concepts introduced with a one-line definition, then unpacked with purpose and relationships. Running examples woven in as illustration, not as the primary vehicle.

**Voice**: Third person, active voice. No "we" or "you." The book states facts, not instructions.

**Sentence length**: Short and declarative for definitions. Medium for explanations. Never compound-complex.

**Definitions**: Every entity gets a one-sentence definition on first mention, set apart (bold or callout). Subsequent text unpacks purpose, relationships, and constraints.

**Examples**: Meridian/Apex/Commonwealth used as illustration after the concept, not as the vehicle for introducing it. Pattern: state the rule, then show the example.

**Domain precision**: Always name the domain when it matters: "bank-domain entity," "corporate-configured," "ESP-defined." Never let the reader guess which actor owns what.

**Cross-references**: Explicit chapter references for forward and backward dependencies. No "as discussed earlier."

**Terminology discipline**: Use the ontology's terms consistently. Never use a synonym for a defined term. If the term is "Credit Facility," never say "credit line" or "credit limit" casually.

**Tone**: Confident, not hedging. "X is Y" not "X can be thought of as Y." Authoritative without being rigid.

**What to avoid**: Marketing language, superlatives, meta-narration ("In this chapter we will..."), rhetorical questions, filler transitions.

**Per-part calibration**:

- **Part I (Problem Space)**: Most narrative. Sets up the "why" with industry context and dissonance examples. Meridian's pain points drive the story. Still practitioner-grade — no hand-holding.
- **Part II (Ontology)**: Most reference-like. Each chapter opens with a crisp definition block, then unpacks relationships and rules. Examples are short and illustrative.
- **Part III (Bank's Foundation)**: Narrative + reference hybrid. Declarative statements about what the bank provides, how onboarding works, what the bank retains. Examples illustrate Commonwealth's operations.
- **Parts IV–V (ESP and Corporate Playbooks)**: Hybrid. Each chapter has a reference section (control archetype, eligibility model) and a narrative section (journey steps). The journey is told in numbered steps with Meridian/Apex/Commonwealth — each step is a declarative statement, not a story.

---

## Front Matter

### Part 0: Purpose, Audience, and Scope

- Who this is for (Zeta PMs building the platform)
- Why this document exists (two-lens problem: bank sees products, corporate sees workflow controls)
- Zeta's role: Tachyon (bank) + Electron (ESP/Corporate) — stated once
- Four-party network model: assumed knowledge
- Out of scope: Bank-to-ESP P&L, network protocol internals, regulatory specifics, fraud management, AML/sanctions, dispute resolution procedures

### The Running Example

> All entities below are fictitious. They are designed to exercise every concept in this book — multiple legal entities, complex OU hierarchies, all four spend archetypes, cross-border operations, and multi-currency credit facilities.

**Meridian Industries** — the Corporate

A multinational industrial manufacturer headquartered in the US with operations across North America, Europe, and Asia.

- Legal Entities:
  - Meridian Industries Inc. (US — Delaware)
  - Meridian UK Ltd (United Kingdom)
  - Meridian India Pvt Ltd (India)
- Organizational structure:
  - OU tree by function: Engineering, Sales, Operations, Finance, Procurement, Marketing
  - OU tree by geography: Americas, EMEA, APAC
  - OU tree by Legal Entity (default): one flat OU per Legal Entity
- 18,000 employees across 12 countries
- Spend needs: supplier payments for raw materials and logistics, employee spend for department purchasing, travel for client implementation teams, recurring SaaS subscriptions for engineering tools
- Treasury manages three Credit Facilities (one per Legal Entity, each in local currency)

**Apex Payments** — the ESP

A fintech company specializing in corporate payment solutions for mid-market and enterprise clients.

- Operates on Electron (Zeta's ESP platform)
- Creates Corporate Payment Products across all four Spend Archetypes
- Serves 40+ corporates including Meridian Industries
- Manages the commercial relationship with corporates: product packaging, onboarding, billing, support
- Has defined AMCs for common supplier categories (AMC-Logistics, AMC-Cloud, AMC-Travel-Agencies, AMC-SaaS)

**Commonwealth National Bank** — the Bank

A large US-based issuing bank with international capabilities.

- Operates on Tachyon (Zeta's bank platform)
- Creates Account Products and Virtual Card Products used by ESPs to build Corporate Payment Products
- Underwrites Credit Facilities for Meridian's three Legal Entities
- Provides accounts, card issuance, payments infrastructure, and authorization/clearing services
- Partners with Apex Payments as its ESP for corporate payment distribution

**How they interact:**

| Actor | Role | Platform |
|-------|------|----------|
| Commonwealth National Bank | Creates Account/Card Products, underwrites credit, provides payments infrastructure | Tachyon |
| Apex Payments | Creates products, onboards corporates, manages billing | Electron |
| Meridian Industries | Configures programs, enrolls members, operates spend workflows | Electron (corporate portal) |

> Subsequent chapters reference Meridian, Apex, and Commonwealth by name when illustrating concepts. Each chapter's examples are drawn from this shared scenario.

---

## Part I: The Problem Space — Narrative

> Part I establishes the payments problem corporates face, surveys existing solutions and their shortcomings, and introduces two conceptual tools — **Spend Archetypes** and **Spend Mandates** — to build the thinking paradigm. It also introduces the three key actors (Bank, ESP, Corporate). These conceptual tools are not system entities. Part II maps them to the actual product ontology.

### Chapter 1: The Corporate Payments Problem

- What corporates actually need to accomplish with commercial payments:
  - Pay suppliers, fund employee purchases, settle travel bookings, manage recurring subscriptions — all under governance
  - Control who can spend, how much, with whom, for what purpose, against which budget
  - Attribute every payment to a cost center, project, client, or GL account
  - Reconcile card transactions against internal records (invoices, POs, itineraries, expense reports)
  - Comply with internal policy, tax requirements, and audit obligations
- Why this is hard:
  - Payment authority is distributed across departments, geographies, and legal entities
  - Different spend workflows need different controls, different card lifecycles, different reconciliation patterns
  - The corporate's organizational structure (departments, projects, cost centers) does not map to the bank's account and credit structure
  - Finance teams need spend data in their language (cost centers, GL codes, project codes) — not in the bank's language (accounts, MCCs, transaction IDs)
- Illustrated with Meridian: AP team paying 200 suppliers, Engineering team managing SaaS subscriptions, Travel desk booking agency travel, Marketing running campaign spend — each with different control, attribution, and reconciliation needs

### Chapter 2: Existing Solutions and Their Limitations

- How banks package commercial card products today (research-backed):
  - AP / Supplier Payment virtual card programs — positioned around invoice matching, ERP integration, working-capital optimization
  - Commercial / Purchasing cards — positioned around employee spend controls, MCC restrictions, amount limits
  - Travel virtual cards — positioned around booking settlement, itinerary reconciliation, central travel payment
  - Lodge / Ghost cards — positioned around centralized recurring spend, persistent virtual account numbers
  - Single-use and multi-use card programs — as control variants across the above
  - Embedded / API-based issuance — as a distribution mechanism
- How networks (Visa, Mastercard, Amex) frame virtual card capabilities — each emphasizes different facets (ERP integration, B2B payments, travel, embedded finance)
- What works: card controls are rich, authorization is real-time, data flows are improving
- What doesn't work:
  - Bank products are organized by bank concerns (credit risk, interchange economics, account structure) — not by corporate workflow
  - A corporate buying a "virtual card program" must translate it into an operating model for supplier payments, a different one for employee spend, a different one for travel
  - Reconciliation, attribution, and policy enforcement are afterthoughts in the bank's packaging
  - The gap between what the bank sells and what the corporate needs to operate is where friction, adoption failure, and value leakage live

> This chapter absorbs and synthesizes the bank-vs-corporate product mapping from the original research. It grounds the reader in real-world context before introducing the conceptual framework.

### Chapter 3: Two Lenses — Why the Gap Exists

- The core insight: banks sell virtual cards as payment products; corporates adopt them as workflow controls
- The gap between these two views is where the ontology lives — and where Zeta's platform creates value
- Concrete dissonance examples:
  - Commonwealth packages an "AP Virtual Card Program" with interchange economics and single-use controls. Meridian's AP team asks: "How do I stop writing checks, match every payment to an invoice in my ERP, and get my team to actually use it?"
  - Commonwealth offers "commercial card with MCC restrictions." Meridian's Marketing VP asks: "How do I give my campaign team purchasing power without giving them a blank check, and how does each charge land on the right cost center?"
  - Commonwealth prices by interchange spread and transaction fees. Meridian's treasury evaluates by reconciliation labor saved, policy leakage reduced, and DPO extended.
- The three actors that bridge the gap: Bank (credit and payments infrastructure), ESP (product packaging and corporate servicing), Corporate (program operations and governance)
  - Brief introduction of Bank, ESP, Corporate roles — Tachyon vs Electron
  - Division of responsibility stated once; detailed treatment in Parts III, IV, and V
- What's needed: an ontology that bridges both lenses — giving the bank what it needs (credit exposure, legal entity, utilization) while giving the corporate what it needs (workflow control, attribution, reconciliation, governance)

### Chapter 4: Spend Archetypes — Four Workflow Patterns

- What a Spend Archetype is: a recognized pattern of how corporate payments work, defined by its control model, card lifecycle, enrollment model, and reconciliation approach
- The names are indicative; the definitions are the operational patterns
- The four archetypes, each with a short narrative sketch:
  - Supplier Payments
  - Employee & Department Spend
  - Travel & Booking Payments
  - Central Recurring Merchant Payments
- Embedded/ERP-native as a delivery mechanism across all archetypes, not an archetype itself
- Archetypes are extensible (ESP defines new ones with Zeta; bank not involved)

> This chapter introduces the archetypes narratively. Part IV details how the ESP designs Products for each; Part V details how the Corporate operates Programs for each.

### Chapter 5: Spend Mandates — The Authorization Envelope

- What a Spend Mandate is: the governing authorization envelope for spend
- Why it exists: for any payment, the enterprise must be able to answer — why was this allowed, who authorized it, whose budget paid for it, which rules applied, how it should be booked, who is accountable
- The eight components: purpose, authority, budget source, policy scope, limits, attribution, validity, exceptions
- Enforceable at authorization (budget limits, spend policies, card controls) vs auditable only (business purpose, accountability)

> Mandate is a thinking tool, not a system entity. Chapter 8 (Corporate Payment Product), Chapter 10 (Corporate Payment Program), and Chapter 12 (Spend Policy) show how its components are distributed across Program sub-sections.

---

### Bridge: From Concepts to Entities

> The theoretical framing in Part I uses Spend Archetypes and Spend Mandates to build intuition. In the product ontology (Part II), these map as follows:
>
> - A **Spend Archetype** is realized as a classification attribute of a **Corporate Payment Product**. Each Product is designed for one Archetype. One Archetype, one Product. Multi-archetype coverage requires multiple Products.
> - A **Spend Mandate** is realized as the composition of **Budget**, **Spend Policy**, **Booking Profile**, and **Card Profile** sub-sections within a **Corporate Payment Program**. There is no standalone "Mandate" entity.
>
> Neither is a standalone entity in the system. Both are essential for understanding *why* the entities are structured the way they are.

---

## Part II: The Ontology — Reference

> Entity model structured for lookup. Each entity gets: definition, key relationships, configuration authority (Bank vs ESP vs Corporate), and state model. Chapters are ordered by domain: corporate foundation → bank products → ESP constructs → financial hierarchy → corporate operations → controls → profiles → people → data → cross-cutting.

### Chapter 6: Corporate, Legal Entity, Organizational Units, and Members

- Corporate: logical container, not a legal entity; associated to Client Contract
- Client Contract: ESP-domain entity, creates the Corporate
- Legal Entity: KYB'd by bank, anchor for credit and regulatory relationships
- Organizational Unit (OU): hierarchical, can span Legal Entities, corporate-administered
- Default OU structure (Legal Entities root node)
- Member: first-class entity of a Corporate, affiliated to zero or more OUs
  - Types: Employee, Supplier, Contractor, Client (custom types supported)
  - Supplier as a Member type: the corporate-domain entity representing a vendor/payee; distinct from Merchant, which is the bank-domain entity (see Chapter 12)
  - Custom attributes per member type for enterprise system mapping

### Chapter 7: Account Product and Virtual Card Product

- Account Product (Tachyon entity, bank-defined):
  - Redistributable — usable by multiple ESPs
  - Defines: supported billing cycles, delinquency controls, base fees and charges
  - Currency constraint: must match Credit Facility currency; but Account Product itself does not recognize Credit Facility — CF is associated per Account at creation time
  - Bank maintains a catalog (browsable + request-based); ESP can request new Account Products
  - State model: out of scope (bank-internal)
- Virtual Card Product (Tachyon entity, bank-defined):
  - Redistributable — usable by multiple ESPs
  - May support multi-network and multi-clearing-house arrangements
  - Bank chooses which card schemes to make available and which scheme card to issue
  - Transactions may be presented through multiple payment networks if the bank has such relationships
  - Settlement to networks and dispute resolution: bank's obligation
  - State model: out of scope (bank-internal)

### Chapter 8: ESP Variants and Corporate Payment Product

- ESP Account Variant (Electron entity, ESP-defined):
  - Customizes a Bank Account Product (Chapter 7) via component programs:
    - Fee Programs, Interest Programs, Statement Program, Reward Programs, Rebate Programs, Notification Program
  - Override model: bank's base programs are fallback; ESP can make all commercial choices (including reducing fees); bank retains credit risk, AML, and compliance parameters exclusively
  - Notification Program: account-level notifications (billing alerts, utilization thresholds, delinquency, statement availability); recipients are Program Admins and (for CF-related) Legal Entity contacts
  - Reusable across multiple Corporate Payment Products; ESP may create dedicated variants for large customers
  - Branding options: cards, statements, notifications
  - State model: in scope (to be defined)
- ESP Virtual Card Variant (Electron entity, ESP-defined):
  - Customizes a Bank Virtual Card Product (Chapter 7) via component programs:
    - Embossing Program, Spend Program (Payment Usage Program), Authentication Program, Tokenisation Program, 3DS Program, Card Fee Programs, Notification Program
  - Override model: same as Account Variant — all commercial and operational parameters available; compliance and fraud risk exclusively bank-managed; limited User-Managed-Risk parameters shared (FRM scope)
  - Notification Program: card-level notifications (transaction alerts, declines, expiry); delivered per Cardholder Profile (email, phone); includes SMS/email OTP for 2FA
  - Notification customization: ESP customizes templates per Variant (branding, language, content); Corporate can further customize at Program/card level; all channels (email, SMS, push, webhook/API); all template changes reviewed by bank executives; bank-originated notifications (regulatory, fraud) non-suppressible by ESP
  - Reusable across multiple Corporate Payment Products
  - State model: in scope (to be defined)
- Rewards/Rebates split: account-level computation by Tachyon (per ESP Account Variant programs); relationship-level computation by Electron
- Corporate Payment Product: ESP-offered construct, tagged to one Spend Archetype
  - Assembly rule: one ESP Account Variant + one ESP Virtual Card Variant = one Corporate Payment Product
  - Product is the "blueprint" — what the ESP designs, prices, contracts, and markets
  - What the ESP defines at Product level:
    - Baseline Spend Policy (maximum control envelope)
    - Card Profile template (default structure, tag schema)
    - Settlement mechanics
    - Control capabilities available to Corporates
    - Data and reporting capabilities
  - Product-level commercial terms:
    - Fees: core financing (interest, overlimit, late payment), program fees (setup, annual, card issuance), transaction fees (domestic, cross-border, FX markup), archetype-specific fees (supplier enablement, travel data, reconciliation enrichment), settlement fees, controls/risk fees, data/reporting fees
    - Rebates: spend-based, volume-tier, category-specific, growth incentive
    - Rewards: points, cashback, miles, statement credits
  - Relationship-level commercial terms: scoped to Client Contract, not to Product (see Chapter 21)

### Chapter 9: Credit Facility, Budget, and Account

- Credit Facility: bank perspective (credit exposure, legal entity) and corporate perspective (total capacity, financial resource)
- Budget: hierarchical subdivision of Credit Facility, corporate governance construct
  - Over-allocation allowed, overuse not
  - Shared across Programs (constrained by OU association)
  - Budget-OU visibility
- Account: the bridging entity
  - Created under an Account Product (see Chapter 7); inherits billing cycles, delinquency controls, base fees from the Account Product
  - Carries Credit Facility (bank concern) and Budget (corporate concern)
  - Always specific to one Program
  - Account-per-archetype patterns (one per employee vs one per program)
- Card: associated with one Account
  - Issued using a Virtual Card Product (via the CPP's ESP Virtual Card Variant — see Chapters 7 and 8)
  - "Virtual" = decoupled from financial obligation (not a form-factor statement)
  - Physical and digital forms
- One-line mapping table (bank domain ↔ corporate domain)
- State models: Credit Facility, Budget, Account, Card

### Chapter 10: Corporate Payment Program

- Corporate Payment Program: corporate-configured operating construct
  - The Spend Mandate concept (from Chapter 5) is realized here as the composition of: Budget assignment, Spend Policy, Booking Profile, Settlement Profile, card controls
  - Bound to one Product (Chapter 8) and one Credit Facility (Chapter 9)
  - Owned by an OU
  - Program is the "instance" — how the corporate puts the Product to use
  - What the Corporate configures at Program level:
    - Spend Policy (can only tighten from Product-level baseline)
    - Booking Profile (cost-center attribution rules)
    - Settlement Profile (settlement account, auto-pay config)
    - Eligibility rules (which Members can participate)
    - Budget assignment
- Relationship: Product = blueprint offered by ESP (Chapter 8); Program = instance configured by corporate
- State model: Program (Draft → Active → Suspended → Closed)

### Chapter 11: Card Profile

- Card Profile as the full configuration attached to a card at issuance
- Cardholder Profile:
  - Name on card, address, contact info (email, phone for ACS and notifications)
  - Custom attributes mapping cardholder to corporate domain (CorporateMemberType, CorporateMemberID)
- Spend Policy / Payment Usage Policy (card-level):
  - Velocity and volume limits (tumbling windows: daily, weekly, monthly, quarterly, annually)
  - Limits scoped to merchant category, AMC, time-slices
  - Life-to-date limits
  - Allow/disallow rules based on authorization request attributes
  - Cascading restriction: can only tighten, never loosen (inherits from Program-level policy)
- Fee Overrides:
  - Per-card overrides for various assessed fees
- Tags:
  - Structured object extensions at card level (serialized as URI format per tag type)
  - Use cases: Corporate Program Information (Corporate ID, Program ID, Member ID, Membership ID), Intended Supplier Information, Reconciliation Tracking Information
  - Tag data can be referenced in Payment Usage Policy rules
- Card Profile as the bridge between corporate domain context and card behavior at point of sale

### Chapter 12: Spend Policy and Controls

- How the Spend Mandate's components are distributed across the Program (cross-reference Chapter 5)
- Spend Policy: cascading restriction model (ESP Product → Corporate Program → Card; tighten only, never loosen)
- Enforceable controls vs auditable governance (the two halves of the Mandate)
- Merchant (bank-domain entity): Direct, Aggregated, or Discovered; grouped as Authorized Merchant Categories (AMCs)
  - AMCs usable in Spend Policy rules by ESPs and Corporates; custom AMCs supported
  - Merchant is not the same entity as Supplier (a Member type in the corporate domain — see Chapter 6); each belongs to its own domain and serves different purposes
  - Authorization enforcement by bank (see Chapter 20)

### Chapter 13: Booking Profile and Settlement Profile

- Booking Profile: internal accounting and attribution
  - Rules-based, runtime resolution (static defaults + dynamic overrides)
  - Default allocation for unmatched credits
- Settlement Profile: how the corporate settles ESP invoices
  - One Settlement Account per Program
  - Auto-pay, payment-date config
- Disputes and refunds: attributed to original postings, inherit profiles

### Chapter 14: Users and Roles

- Users: people entitled to create and operate Programs, Products, Budgets, and other corporate entities
- Roles define scope of access: which OUs, Programs, Products, and Budgets a User can administer
- Users are not Members; they belong to different domains (a person can hold both, as separate entity instances)

### Chapter 15: Members, Eligibility, and Enrollment

- Members (including Suppliers) as participants in Programs
- Eligibility: rules-based, scoped by OU, member type, and member attributes — defined per Program
- Enrollment: always explicit, performed by Program Admin (UI, Files, APIs)
- Enrollment → card issuance; multiple enrollments per Member per Program (supports single-use card patterns)
- Conditional KYC steps during enrollment
- Approval engine: configurable at program setup (approving authority per member, nominated approval groups)

### Chapter 16: Transaction Posting and Data

- L1, L2, L3 data
- Three sources on a posting: network/merchant, merchant-provided, payer-provided
- Card-level corporate attributes (tags)
- Near real-time availability; CSV data extracts
- Master statement (Electron-compiled for multi-account programs)

### Chapter 17: Multi-Currency, Residency, and Cross-Border

- Account base currency = Credit Facility currency
- FX conversion at network level; corporate bears risk
- Settlement currency can differ from account currency
- Program residency pinned by Credit Facility; members can span entities/geographies
- Multiple Credit Facilities in different currencies
- Private Label card support

---

## Part III: The Bank's Foundation — Narrative + Reference

> How the bank underpins the entire corporate payments ecosystem: the products it creates, the onboarding it performs, and the processing and controls it enforces. All illustrated with Commonwealth National Bank.

### Chapter 18: Account Products and Virtual Card Products

> Entity definitions are in Chapter 7 (reference). This chapter provides the narrative context: why the bank creates these products, how the catalog works, and what the bank retains.

- What the bank makes available to ESPs and why
  - Account Products: the bank's account-level product construct (billing cycles, delinquency controls, base fees)
  - Virtual Card Products: the bank's card-level product construct (card scheme selection, multi-network, multi-clearing-house)
- Product catalogs: bank maintains a browsable catalog; ESPs can also request custom products
- Redistributable: a single Account Product or Virtual Card Product can serve multiple ESPs
- Currency constraint: Account Product currency must match Credit Facility currency
- What the bank retains vs what it exposes to the ESP
- Illustrated with Commonwealth creating Account Products and Virtual Card Products for its corporate payments business

### Chapter 19: Onboarding — ESP and Corporate Legal Entities

- ESP onboarding:
  - Bank onboards the ESP as a partner
  - Makes Account Products and Virtual Card Products available to the ESP
  - ESP begins creating Variants and assembling Corporate Payment Products (detailed in Part IV)
- Legal Entity onboarding (KYB):
  - Bank performs KYB on Corporate Legal Entities
  - Legal Entity registration in Tachyon
- Credit Facility extension:
  - Bank underwrites and extends Credit Facilities to Legal Entities
  - One Credit Facility per Legal Entity per currency (multiple CFs possible)
  - CF as the bank's credit exposure and the corporate's financial resource
- Illustrated with Commonwealth onboarding Apex Payments, KYB'ing Meridian's three Legal Entities, extending Credit Facilities

### Chapter 20: Processing, Authorization, and Controls

- Payment processing and posting:
  - Bank processes all transactions and posts them to accounts
  - All policies applicable to card and account honored inline at authorization
- Authorization enforcement:
  - Bank enforces all Spend Policies (ESP-level and Corporate-level) at authorization time
  - ESP and Corporate can optionally participate in authorization processing if bank controls are inadequate
- Account-level Rewards and Rebates:
  - Computed by Tachyon based on ESP Account Variant programs
  - This is the mechanism ESP relies on for product-level rewards/rebates
  - Relationship-level rewards/rebates computed separately by Electron
- Bank-side non-overridable controls:
  - Regulatory checks, bank-defined fraud checks, Credit Facility restrictions, delinquency controls, NPA tracking, customer servicing compliance
  - These are enforced at Account Product level; ESP cannot override
- Notification boundary:
  - Bank-originated notifications (regulatory disclosures, fraud alerts) cannot be suppressed by ESP
  - ESP can suggest templates for bank-originated notifications
- Illustrated with Commonwealth processing transactions for Meridian's programs, enforcing controls, computing rewards

---

## Part IV: The ESP's Playbook — Narrative + Reference

> How the ESP operates: from customizing bank products into Variants, assembling Corporate Payment Products, contracting with corporates, to designing Products for each Spend Archetype. All illustrated with Apex Payments. Builds on the bank foundation established in Part III.

### Chapter 21: ESP-Wide Concerns

- Client Contract initiation and management
  - Engaging with the corporate, signing contract with one or more Legal Entities
  - Corporate entity creation in Electron, associated to Client Contract
- ESP Account Variant and ESP Virtual Card Variant creation
  - How the ESP selects bank Account Products and Virtual Card Products from the catalog
  - Creating Account Variants: configuring Fee, Interest, Statement, Reward, Rebate, Notification Programs to override bank defaults
  - Creating Virtual Card Variants: configuring Embossing, Spend, Authentication, Tokenisation, 3DS, Card Fee, Notification Programs
  - Variant reuse strategy: shared variants vs dedicated variants for large customers
  - Branding: card design, statement format, notification templates
- Corporate Payment Product assembly
  - Selecting one ESP Account Variant + one ESP Virtual Card Variant
  - Tagging to a Spend Archetype (1:1 relationship)
  - Defining product-level Spend Policy baseline, Card Profile template, settlement mechanics
  - Setting product-level commercial terms (fees, rebates, rewards)
- Relationship-level commercial terms
  - Negotiated per Corporate: custom pricing, volume commitments, waivers, SLA credits, migration incentives
  - Distinguished from product-level terms (which are per Product, not per Corporate)
  - Relationship-level rewards and rebates computed by Electron (distinct from account-level computation by Tachyon)
- Credit Facility configuration
  - ESP facilitates Legal Entity registration and KYB (via Tachyon — see Chapter 19)
  - Bank extends Credit Facilities to Legal Entities; ESP configures access in Electron
- Corporate onboarding
  - OU hierarchy setup, Member population, User provisioning
  - Product selection — Corporate selects from ESP's catalog
- Billing
  - Billing is ESP-performed, account-level, Legal Entity as payer
  - Billing configuration: cycle, due date, interest-free period, penalties
  - Master statement compilation for multi-account programs

### Chapter 22: Supplier Payments Product

- Design decisions for this archetype:
  - Baseline Spend Policy: single-use or PO-based multi-use, merchant-locked controls
  - Card Profile template: supplier tags (supplier ID, PO/invoice reference), tag schema for reconciliation tracking
  - Product-level fees: supplier enablement fee, remittance delivery fee, ERP/AP connector fee, exception handling fee
  - Settlement mechanics: central billing, single-account-per-program settlement
  - Control capabilities exposed: per-card merchant lock, amount lock, validity window, single-use enforcement
  - Data/reporting: L2 data emphasis (invoice number, PO, tax), L3 where available
- Illustrated with Apex building a Supplier Payments Product for Commonwealth's platform

### Chapter 23: Employee Spend Product

- Design decisions for this archetype:
  - Baseline Spend Policy: MCC restrictions, velocity/volume limits (daily, weekly, monthly), amount caps
  - Card Profile template: employee tags (employee ID, department, cost center), configurable data-capture form schema
  - Product-level fees: card issuance fee, platform/portal fee, reporting fee
  - Settlement mechanics: per-employee account billing, master statement aggregation
  - Control capabilities exposed: MCC allow/block lists, approval workflow configuration, data-capture form definition
  - Data/reporting: employee-provided data alongside L1/L2, approval status in posting
- Illustrated with Apex building an Employee Spend Product

### Chapter 24: Travel Payments Product

- Design decisions for this archetype:
  - Baseline Spend Policy: AMC-Travel-Agencies whitelist, lodge-style persistent or per-booking single-use variants
  - Card Profile template: agency tags (agency ID, booking channel), itinerary reference tag schema
  - Product-level fees: travel account fee, booking channel fee, travel data/reconciliation fee, TMC integration fee
  - Settlement mechanics: lodge-style persistent account, agency-level billing
  - Control capabilities exposed: agency enrollment, per-booking or persistent card lifecycle selection
  - Data/reporting: L2 emphasis (itinerary reference, booking ID, traveler name)
- Illustrated with Apex building a Travel Payments Product

### Chapter 25: Central Recurring Payments Product

- Design decisions for this archetype:
  - Baseline Spend Policy: AMC whitelists/blacklists, persistent card with recurring authorization
  - Card Profile template: vendor/subscription tags (vendor ID, subscription reference, contract period)
  - Product-level fees: card maintenance fee, platform fee
  - Settlement mechanics: standard account-level billing
  - Control capabilities exposed: whitelist/blacklist merchant controls, per-card amount caps, validity periods
  - Data/reporting: subscription ID, invoice period in L2
- Illustrated with Apex building a Central Recurring Payments Product

---

## Part V: The Corporate's Playbook — Narrative + Reference

> How the Corporate operates: from managing its organizational foundation to running Programs for each Spend Archetype. All illustrated with Meridian Industries.

### Chapter 26: Corporate-Wide Concerns

- Managing Organizational Units
  - Creating and maintaining OU hierarchies (by function, geography, project)
  - Restructuring impact: Programs' Credit Facilities stay, Budgets and OU associations can change, cards unaffected
- Managing Budgets
  - Carving Credit Facilities into Budgets, creating sub-Budget hierarchies
  - Budget-OU association: which Budgets are visible to which Programs
  - Cross-program Budget sharing and its constraints
  - Over-allocation allowed, overuse enforcement through hierarchy
- Managing Settlement Accounts
  - Setting up settlement accounts per Program
  - Single Settlement Account per Program constraint; separate Programs for separate accounts
  - Settlement currency flexibility
- Managing Members
  - Loading and maintaining Members across OUs (employees, suppliers, contractors, clients)
  - Custom attributes per member type for enterprise system mapping
  - Member lifecycle: creation, OU affiliation changes, deactivation
- User Provisioning and Role Management
  - Designating Users with roles scoped to OUs, Programs, Products, Budgets
  - Users vs Members: different domains, different purposes
- Notification Customization
  - Customizing notification templates at Program and card level (within ESP Variant boundaries)
  - Configuring notification recipients for program-level events
- Settlement Operations
  - Settling against ESP invoices per Settlement Profile
  - Auto-pay configuration, payment-date settings
  - Settlement currency may differ from account currency

### Chapter 27: Supplier Payments Program

**Reference:**
- Control archetype: single-use per invoice/PO (multi-use if PO-based), single account per program
- Eligibility: Payee (which suppliers)
- Cardholder: Program Admin (or supplier authorized user for ACS)
- Supplier info tagged to Card via Card Profile Tags, irrespective of Cardholder Profile

**Program Journey:**
1. Program creation — Meridian's AP Director creates a Supplier Payments Program, selects Apex's Supplier Payments Product, assigns Credit Facility and Budget from Procurement OU
2. Program configuration — sets Spend Policy (AMC-Logistics whitelist), Booking Profile (AP cost center, vendor GL), Settlement Profile (central treasury account, auto-pay)
3. Supplier enrollment — Program Admin enrolls eligible suppliers; each enrollment generates a card tagged with supplier ID, PO/invoice reference
4. Card issuance — single-use card issued per invoice (or multi-use per PO); Card Profile carries supplier tags and payment usage restrictions
5. Transaction — supplier processes payment against the card; authorization checks Budget hierarchy, Spend Policy, card-level controls
6. Clearing and posting — transaction clears; L1 data (amount, MCC, merchant) + L2 data (invoice number, PO, tax) posted to account
7. Billing — Apex generates account-level bill; Meridian receives invoice with Legal Entity as payer
8. Settlement — Meridian settles against Apex invoice per Settlement Profile (auto-debit from treasury account)
9. Booking — Booking Profile rules attribute transaction to AP cost center and vendor GL in ERP
10. Reconciliation — card tags (supplier ID) + L2 posting data (invoice number, PO) matched against AP invoice in ERP

### Chapter 28: Employee & Department Spend Program

**Reference:**
- Control archetype: multi-use card, one account per employee, MCC-restricted
- Eligibility: Payer (which employees)
- Data-capture form: configurable at program setup, feeds Booking Profile rules
- Approval workflow: per-employee approver + nominated approval group

**Program Journey:**
1. Program creation — Meridian's Engineering VP creates a Department Spend Program, selects Apex's Employee Spend Product, assigns Credit Facility and Budget from Engineering OU
2. Program configuration — sets Spend Policy (MCC restrictions for office supplies and SaaS), Booking Profile (with rules for dynamic cost-center attribution based on employee-provided data), Settlement Profile, approval workflow (manager as approver per employee)
3. Employee enrollment — Program Admin enrolls eligible employees from Engineering OU; each enrollment generates a multi-use card with employee-specific Card Profile
4. Card issuance — card issued to employee; Card Profile carries employee member ID, department tags, MCC restrictions
5. Transaction — employee makes a purchase; authorization checks Budget hierarchy, MCC restrictions, velocity limits
6. Data capture — employee provides additional info (project code, expense category) via Electron UI or API; data attached to posting
7. Clearing and posting — transaction clears; L1 + L2 data posted; employee-provided data attached
8. Approval — if configured, transaction routed through approval workflow before booking
9. Billing — Apex generates per-employee account statements + master statement for the program
10. Settlement — Meridian settles against Apex invoice per Settlement Profile
11. Booking — Booking Profile rules use employee-provided project code to attribute to correct cost center and cost head in ERP
12. Reconciliation — program-level cost head (if single-purpose program) or employee-provided expense code matched against budget/cost center

### Chapter 29: Travel & Booking Payments Program

**Reference:**
- Control archetype: dual — single-use per booking or lodge-style persistent per agency
- Eligibility: Payer (travelers) for per-booking cards; Payee (agencies) for lodge-style cards
- Reconciliation: itinerary/booking reference from agency in L2 data

**Program Journey:**
1. Program creation — Meridian's Travel Desk creates a Travel Payments Program, selects Apex's Travel Product, assigns Credit Facility and Budget from the Travel OU
2. Program configuration — sets Spend Policy (AMC-Travel-Agencies whitelist), Booking Profile (travel expense GL, client code attribution rules), Settlement Profile
3. Agency enrollment (lodge model) — travel agency enrolled as payee; persistent card issued to agency with agency-specific Card Profile tags
4. Transaction — agency charges booking to the lodge card; authorization checks Budget, AMC restrictions
5. Clearing and posting — L1 data + L2 data (itinerary reference, booking ID, traveler name) posted to account
6. Billing — Apex generates account-level bill; master statement compiled if multiple accounts
7. Settlement — Meridian settles per Settlement Profile
8. Booking — Booking Profile rules use L2 data (client code, project code from itinerary) to attribute to correct cost center
9. Reconciliation — posting matched against itinerary/booking reference provided by agency in L2 data; cross-referenced with travel management system

### Chapter 30: Central Recurring Merchant Payments Program

**Reference:**
- Control archetype: one card per project or cost head, whitelist/blacklist restrictions, persistent
- Eligibility: Payee (which merchants are approved for recurring charges)
- Reconciliation: posting matched against subscription/contract record

**Program Journey:**
1. Program creation — Meridian's Engineering Ops Manager creates a SaaS Subscriptions Program, selects Apex's Recurring Payments Product, assigns Credit Facility and Budget from Engineering OU
2. Program configuration — sets Spend Policy (AMC-SaaS whitelist + named vendor blacklist), Booking Profile (SaaS opex GL, per-tool cost attribution), Settlement Profile
3. Vendor enrollment — each SaaS vendor enrolled; one persistent card issued per project or cost head, with Card Profile tags carrying vendor ID and subscription reference
4. Transaction — recurring charge processed by SaaS vendor; authorization checks Budget, AMC, velocity limits
5. Clearing and posting — L1 data + L2 data (subscription ID, invoice period) posted to account
6. Billing — Apex generates account-level bill
7. Settlement — Meridian settles per Settlement Profile
8. Booking — Booking Profile attributes to engineering opex GL and specific tool cost head
9. Reconciliation — posting matched against subscription/contract record in procurement system

---

## Open Questions for Discussion

1. ~~**Commercial terms placement**~~ — Resolved: product-level terms live in Chapter 8 (per Product); relationship-level terms live in Chapter 21 (per Client Contract). No duplication.

2. **State models** — Defined alongside entity definitions in Part II. Additionally collected into a consolidated reference table as an appendix for quick lookup.
