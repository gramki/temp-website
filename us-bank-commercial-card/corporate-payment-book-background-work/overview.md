> **Terminology note (for the rewrite into `corporate-payments-concepts.md`):**
> This document uses "Spend Lane" and "Spend Mandate" throughout. In the final book-structured document, these terms are reframed:
>
> | Term in this document | Term in the rewrite | Role in the rewrite |
> |---|---|---|
> | Spend Lane | **Spend Archetype** | Conceptual tool (Part I narrative); realized as a classification attribute of Corporate Payment Product in Part II entity model |
> | Spend Mandate | **Spend Mandate** (unchanged, but repositioned) | Conceptual tool (Part I narrative); realized as the composition of Budget, Spend Policy, Booking Profile, and Card Profile sub-sections within a Corporate Payment Program — not a standalone entity |
>
> A bridge section ("From Concepts to Entities") between Part I and Part II makes this mapping explicit. See `suggested-outline-draft.md` for the full outline.

---

From a bank perspective, virtual card programs are usually packaged as product lines. From a corporate perspective, the same programs are better understood as payment operating models for different spend workflows.

So the mapping is not really:
	•	bank product A = corporate product A

It is more:
	•	bank program construct = corporate use case + control model + system integration point

Here is the clean mapping.

1. Accounts Payable / Supplier Payment virtual cards

Bank view:
A bank sees this as an AP automation / B2B virtual card program. It is usually sold with ERP/AP integration, supplier enablement, working-capital messaging, and single-use card controls. Visa and Amex both position this around invoice matching, ERP integration, reconciliation, and cash-flow optimization.  ￼

Corporate view:
A corporate sees this as a way to modernize the procure-to-pay or invoice-to-pay workflow.

What the enterprise is trying to achieve:
	•	pay suppliers without paper/check/ACH-only friction
	•	match one invoice / one payment / one card number
	•	improve reconciliation and auditability
	•	extend payables where useful
	•	centralize controls in AP rather than in employee expense systems

Typical corporate owners:
	•	AP
	•	Procurement
	•	Treasury
	•	CFO organization

Corporate label for the program:
More likely called:
	•	Supplier payments
	•	AP automation
	•	B2B payable cards
	•	invoice-linked payments

⸻

2. Employee spend / purchasing virtual cards

Bank view:
A bank sees this as a commercial card / purchasing card / expense card modernization program, with controls on merchant category, amount, period, and sometimes geography. Visa explicitly frames virtual cards as a way to assign cards to specific purchases and reduce admin effort.  ￼

Corporate view:
A corporate sees this as a way to govern decentralized business spend without handing out broadly usable plastic cards.

What the enterprise is trying to achieve:
	•	give employees or teams controlled buying power
	•	issue cards for a specific need, project, campaign, or approval
	•	avoid reimbursement-heavy workflows
	•	reduce policy leakage
	•	improve real-time spend visibility

Typical corporate owners:
	•	Finance
	•	Procurement
	•	department budget owners
	•	expense management / controllership

Corporate label for the program:
Usually described as:
	•	employee spend controls
	•	department purchasing
	•	project-based spend cards
	•	controlled purchasing

⸻

3. Travel virtual cards

Bank view:
Banks and networks often treat this as a dedicated travel payments or wholesale travel program. Mastercard highlights virtual cards for business travel, and travel-oriented programs emphasize controlled bookings and reconciliation.  ￼

Corporate view:
A corporate sees this as part of the travel booking and settlement model, not just as “a card.”

What the enterprise is trying to achieve:
	•	centrally pay for hotel, airline, or agency bookings
	•	separate traveler experience from settlement mechanics
	•	make each trip/booking auditable
	•	reconcile travel bookings to itinerary and policy
	•	reduce card sharing and fraud risk

Typical corporate owners:
	•	Travel desk / travel management
	•	Finance
	•	Procurement
	•	HR or workplace operations in some firms

Corporate label for the program:
Often understood as:
	•	central travel payment
	•	travel booking settlement
	•	T&E payment control
	•	lodge / booking payment

⸻

4. Lodge card / ghost card / centrally billed virtual account

Bank view:
The bank sees this as a central-bill account structure or persistent virtual account used for repeated, centrally managed spend. Amex references Business Travel Account and related virtual account structures alongside other business virtual-number programs.  ￼

Corporate view:
A corporate sees this as a shared but controlled payment rail for a recurring workflow.

What the enterprise is trying to achieve:
	•	centralize spend under finance rather than individual cardholders
	•	support recurring merchants or programmatic purchases
	•	avoid dependence on an employee’s physical card
	•	preserve reporting by business unit, supplier, or cost center

Typical corporate owners:
	•	Finance
	•	AP
	•	Travel operations
	•	shared services

Corporate label for the program:
Usually:
	•	central billed account
	•	shared payment account
	•	merchant-specific central card
	•	lodge card

⸻

5. Single-use virtual card programs

Bank view:
This is a program feature or operating mode. Issuers emphasize security, time/amount controls, and one-to-one reconciliation. Visa and Amex both explicitly highlight single-use controls.  ￼

Corporate view:
The enterprise sees this as the best fit where the payment should map to one approval, one invoice, one booking, or one exception case.

Where corporates use it:
	•	supplier invoice payments
	•	one-off purchases
	•	contractor or candidate travel
	•	exceptional or high-risk transactions

Corporate framing:
Not a separate “program” so much as a control archetype:
	•	one-time controlled payment
	•	payment per invoice
	•	payment per booking

⸻

6. Multi-use / merchant-locked virtual card programs

Bank view:
Again, this is often a program configuration, where a virtual number persists for repeat use with chosen controls.

Corporate view:
The enterprise sees this as suited to recurring spend lanes.

Where corporates use it:
	•	SaaS subscriptions
	•	media/advertising spend
	•	approved supplier relationships
	•	team-level recurring online purchases

Corporate framing:
This is usually thought of as:
	•	recurring vendor payment account
	•	subscription spend control
	•	merchant-bound budget card

⸻

7. Embedded/API virtual card issuance

Bank view:
Banks and networks increasingly see this as an embedded finance distribution model. Mastercard explicitly frames virtual cards as part of embedded finance and integration into business software.  ￼

Corporate view:
The enterprise sees this as “payments inside the workflow system we already use.”

What the enterprise is trying to achieve:
	•	generate a virtual card from ERP, T&E, procurement, OTA, or workflow tools
	•	avoid swivel-chair operations
	•	keep payment controls in business process context
	•	automate posting, reconciliation, and approval trails

Typical corporate owners:
	•	Finance systems
	•	ERP / enterprise applications
	•	digital transformation office
	•	treasury tech / shared services automation

Corporate label for the program:
Usually:
	•	embedded payments
	•	ERP-integrated virtual cards
	•	workflow-native card issuance

⸻

A more useful enterprise taxonomy

If you are designing from the corporate/enterprise side, the best categorization is usually this:

A. Supplier-payments model

For paying vendors and invoices.

Maps to bank offerings:
	•	AP virtual cards
	•	Buyer-initiated payments
	•	single-use supplier cards

B. Employee-spend model

For empowering employees or teams under policy.

Maps to bank offerings:
	•	purchasing cards
	•	virtual expense cards
	•	controlled employee virtual cards

C. Centralized recurring-spend model

For merchants, subscriptions, central billing, or repeating workflows.

Maps to bank offerings:
	•	lodge cards
	•	ghost cards
	•	multi-use merchant-bound virtual cards

D. Travel-settlement model

For bookings, itineraries, central travel payment, and T&E control.

Maps to bank offerings:
	•	travel virtual cards
	•	business travel account structures
	•	wholesale travel / central booking payment programs

Note: Embedded / ERP-native payment generation is a delivery mechanism, not a separate spend model. All four models above should support API-based and ERP-integrated card issuance as a capability

⸻

One-line bank-to-corporate mapping

Here is the concise translation:

| Bank perspective            | Corporate perspective                           |
|----------------------------|-------------------------------------------------|
| AP virtual card program    | Supplier payment operating model                |
| Purchasing / commercial card| Employee spend control model                   |
| Travel virtual card        | Travel booking and settlement model             |
| Lodge / ghost card         | Centralized recurring payment model             |
| Single-use card            | One-transaction / one-invoice control pattern   |
| Multi-use controlled card  | Recurring merchant / budget-bound control pattern|
| Embedded issuance          | Delivery mechanism (API/ERP integration) across all models |

This is the key idea:
banks sell virtual cards as payment products; corporates adopt them as workflow controls.

What changes when you think like the enterprise

A corporate usually does not start with “which virtual card product do I want?” It starts with:
	•	which spend workflow is broken
	•	who owns that workflow
	•	whether the payment should be centralized or delegated
	•	whether the card should be single-use or persistent
	•	what system should generate it
	•	what controls and reconciliation evidence are needed

That is why Visa emphasizes ERP/AP integration, invoice matching, and employee purchase controls, while Mastercard emphasizes B2B, travel, and purchases on the go, and Amex emphasizes buyer-initiated AP flows and transaction-level controls.  ￼

Practical conclusion

If you are mapping a bank product portfolio to enterprise demand, the enterprise-facing packaging should probably be:
	1.	Supplier Payments
	2.	Employee & Department Spend
	3.	Travel & Booking Payments
	4.	Central Recurring Merchant Payments

Each should support embedded / ERP-native / API-based card issuance as a delivery mechanism

Then under each, offer the control variants:
	•	single-use
	•	multi-use
	•	merchant-locked
	•	amount/time/MCC constrained
	•	centrally billed vs individually delegated


----
Yes.

A Spend Mandate should represent the governing authorization envelope for a payment or spend action.

In short:

Lane says what kind of payment flow this is.
Mandate says why it is allowed, who owns it, which budget it uses, what rules govern it, and how it must be accounted for.

What Spend Mandate should represent

A Spend Mandate should capture these elements:

1. Business purpose

Why this spend exists.
Examples:
	•	project delivery
	•	department operations
	•	client implementation
	•	travel for sales
	•	recurring software for engineering

2. Authority

Who is allowed to initiate, approve, or own this spend.
Examples:
	•	project manager
	•	cost center owner
	•	procurement
	•	finance controller
	•	travel desk

3. Budget source

Which budget or funding bucket absorbs the spend.
Examples:
	•	department budget
	•	project budget
	•	client-billable budget
	•	capex
	•	opex
	•	discretionary pool

4. Policy scope

What policy regime applies.
Examples:
	•	procurement policy
	•	travel policy
	•	project spend policy
	•	approval thresholds
	•	supplier restrictions
	•	geography restrictions

5. Accountability and attribution

How the spend is tagged, tracked, and later justified.
Examples:
	•	cost center
	•	project code
	•	program code
	•	client code
	•	GL mapping
	•	tax treatment
	•	owner of record

6. Validity boundaries

When and for how long the authority is valid.
Examples:
	•	valid for a quarter
	•	valid for project phase 1
	•	valid until contract signature
	•	one-time only
	•	recurring until revoked

7. Financial limits

The ceilings and guardrails.
Examples:
	•	per transaction limit
	•	cumulative monthly limit
	•	total budget cap
	•	merchant/category cap
	•	supplier-specific cap

8. Exceptions and escalation

What happens when spend falls outside the norm.
Examples:
	•	approval reroute
	•	finance review
	•	procurement override
	•	temporary extension
	•	post-facto justification

Good definition

A Spend Mandate is the governing authorization envelope for spend, defining its purpose, ownership, funding source, policy, limits, attribution, validity, risk/compliance treatment, and eligible supplier boundaries.

What it should enable

A good Spend Mandate should let an enterprise answer, for any payment:
	•	why was this allowed
	•	who authorized it
	•	whose budget paid for it
	•	which rules applied
	•	how it should be booked
	•	whether it is still valid
	•	who is accountable
	•	who is eligible to receive payments
	•	who is eligible to authorize payments
    

Simple template

A Spend Mandate can be modeled as:
	•	Purpose
	•	Owner
	•	Approver(s)
	•	Budget / funding source
	•	Attribution tags
	•	Policy set
	•	Limits
	•	Validity period
	•	Exception path

Example

Lane: Travel & Booking Payments
Mandate: Client Implementation Travel

Mandate contains:
	•	purpose: travel for Bank X implementation
	•	owner: engagement manager
	•	approver: delivery head
	•	budget: client implementation budget
	•	attribution: client code + project code
	•	policy: implementation travel policy
	•	limits: airfare/hotel caps
	•	validity: Apr–Jun 2026
	•	exception path: CFO delegate for overages

That is what gives enterprise control.


-----
## Spend Lane

A Spend Lane is the operational path through which a payment is initiated, processed, and reconciled, defined by the nature of the spend workflow, the actors involved, and the payment-specific controls inherent to that workflow.

A Spend Lane defines the type of payment flow.

What it should represent:
	•	spend/workflow type
	•	initiating actor or system
	•	merchant/supplier/payment context
	•	processing pattern
	•	reconciliation pattern
	•	lane-native controls

Examples of lanes:
	•	Supplier Payments
	•	Employee & Department Spend
	•	Travel & Booking Payments
	•	Central Recurring Merchant Payments

Note: "Embedded / ERP-native Payments" is a delivery mechanism, not a Lane. Every lane should have relevant embedding capabilities through APIs and events. Lanes are extensible — ESPs define new Lanes with help from Zeta; the bank need not be involved.

Good paired definition:

Spend Lane defines how the payment flows operationally.
Spend Mandate defines why it is allowed and under what business, financial, and policy authority.

Cleaner enterprise version:

A Spend Lane is the operational category of spend flow, grouping payments that share a common initiation model, processing path, merchant or supplier context, reconciliation pattern, and natural control surfaces.

the best short pair is:
	•	Lane = operational payment flow
	•	Mandate = governing authorization envelope




====
## Credit Facility and Budget

The bank extends a Credit Facility to the corporate and makes it accessible through the ESP. A corporate can have any number of Credit Facilities. Each Credit Facility can be sub-divided into multiple Budgets by the corporate. While the issuer domain speaks in terms of limits, the corporate domain reflects the same constructs as Credit Facility and Budget.

⸻

### Bank perspective

Credit Facility:

A Credit Facility is a credit exposure the bank underwrites against a legal entity. It represents the bank's risk position.

	•	always tied to a single legal entity
	•	every account created under it inherits that legal entity association
	•	the bank manages it as a credit line with utilization tracking, covenant monitoring, and regulatory capital treatment
	•	sub-limits, if any, are internal risk controls — they do not represent corporate organizational structure
	•	the bank does not see or care about the corporate's internal department, project, or cost-center hierarchy

Budget (bank view):

A Budget, from the bank's perspective, is an administrative subdivision of a Credit Facility. It may be associated with any organizational unit within the corporate, but it does not change the legal ownership or the credit risk position.

	•	the bank sees a Budget as a spend partition, not a separate credit exposure
	•	Budgets do not introduce new legal entities — the Credit Facility's legal entity governs
	•	the bank treats Budget-level limits as soft allocations within the facility ceiling
	•	reporting at Budget level is optional from the bank's standpoint; what matters is facility-level utilization

What the bank tracks:

	•	facility-level credit exposure
	•	utilization against underwritten limit
	•	legal entity for regulatory, KYC, and covenant purposes
	•	account-to-facility mapping for settlement and billing

What the bank does not track:

	•	which department or project a Budget represents
	•	why the corporate chose to split Budgets in a particular way
	•	internal corporate approval chains tied to Budgets

⸻

### Corporate perspective

Credit Facility:

A Credit Facility is the total credit capacity the corporate has available from the bank for commercial card spend. The corporate treats it as a financial resource to be allocated across business needs.

	•	tied to the corporate's legal entity for contractual and treasury purposes
	•	managed by treasury or finance as part of overall credit and liquidity planning
	•	the corporate may hold multiple Credit Facilities — from the same bank or across banks — for different programs, geographies, or business units
	•	the facility ceiling is a constraint the corporate plans around, not just a bank-imposed cap

Budget (corporate view):

A Budget is the corporate's way of carving a Credit Facility into purposeful, governed allocations that map to its own organizational and operational structure.

	•	each Budget can represent a department, project, cost center, region, spend category, or business initiative
	•	Budgets are the unit at which the corporate assigns ownership, approval authority, and spend policy
	•	the corporate uses Budgets to enforce its own governance — who can spend, how much, for what purpose, and under which policy
	•	Budget allocation is a corporate finance decision, not a bank decision
	•	Budget is hierarchical — a Budget can have sub-Budgets (e.g., a department budget with project-level sub-budgets underneath)
	•	a Budget can be shared across Programs; collectively the Programs sharing a Budget cannot exceed it
	•	Budget sharing across Programs is constrained by the Budget-OU association — since Budgets are associated with OUs and Programs are owned by OUs, a Budget is visible to Programs owned by the OU to which the Budget belongs
	•	over-allocation of sub-Budgets is allowed (sub-Budget sum may exceed parent), but enforcement is through the hierarchy — all ancestors are consulted at authorization time and overuse of any ancestor is not allowed

What the corporate tracks at Budget level:

	•	allocated amount and remaining balance
	•	owning department or cost center
	•	authorized spenders and approvers
	•	applicable spend policy
	•	GL coding and attribution tags
	•	utilization against plan

How Budget connects to Spend Mandate and Spend Lane:

	•	a Corporate Payment Program draws its financial allocation from a Budget
	•	a Budget may fund multiple Programs across different Spend Lanes
	•	the Budget is the financial container; the Program’s mandate configuration is the authorization envelope; the Lane is the operational flow

Example:

Credit Facility: $10M commercial card facility from Bank X, tied to Acme Corp (legal entity).

Budgets carved from it:

	•	Engineering Operations — $2M, owned by VP Engineering, funding SaaS subscriptions and cloud spend
	•	Client Delivery Travel — $1.5M, owned by Delivery Head, funding implementation travel
	•	Marketing Programs — $500K, owned by CMO, funding campaign and event spend
	•	AP Supplier Payments — $6M, owned by AP Director, funding vendor invoice payments

Each Budget then supports one or more Mandates, each operating through the appropriate Lane.

⸻

### One-line mapping

| Bank domain       | Corporate domain                                  |
|-------------------|---------------------------------------------------|
| Credit limit      | Credit Facility — total capacity from the bank    |
| Sub-limit         | Budget — purposeful allocation to a business need |
| Legal entity      | Legal entity (same — this is the anchor)          |
| Account           | Financial container carrying Credit Facility and Budget |
| Utilization       | Spend against Budget allocation                   |

The key distinction: the bank structures limits around credit risk and legal entity. The corporate structures Budgets around business purpose, ownership, and policy. The Credit Facility is the shared anchor between the two views.


-----

## Booking Profile

A Booking Profile defines how an approved spend is recorded inside the enterprise’s financial and management systems, including the accounting, attribution, and reporting treatment that should be applied.

A Booking Profile is not necessarily static per Program. It can contain rules. Based on those rules, individual transactions can be attributed to the appropriate Cost Centers and Cost Heads dynamically. The profile acts as a template with runtime resolution — static defaults plus rule-driven overrides based on transaction, card, or payer-provided attributes.

The Booking Profile may also define a default allocation for unmatched credits (e.g., refunds that cannot be matched to an original posting).

What it covers:
	•	legal entity
	•	cost center / department
	•	project / program / client code
	•	GL / ERP account
	•	capex vs opex
	•	tax treatment
	•	accrual / reporting classification
	•	internal chargeback or allocation rules

In plain words:
	•	Booking Profile = where and how the spend is accounted for internally

⸻

## Settlement Profile

A Settlement Profile defines how the enterprise settles invoices received from the ESP, including the repayment source, account structure, and settlement responsibility.

The system supports only one Settlement Account in a Settlement Profile per Program. If a corporate needs different settlement accounts (e.g., by region or Legal Entity), it needs separate Programs.

What it covers:
	•	repayment bank account or virtual account
	•	billing entity / liable entity
	•	credit line / facility used
	•	central vs local settlement
	•	auto-debit or manual repayment method
	•	treasury ownership

In plain words:
	•	Settlement Profile = how the enterprise settles invoices received from the ESP

⸻

Clean distinction
	•	Spend Mandate = should this spend be allowed
	•	Booking Profile = how should this spend be recorded
	•	Settlement Profile = how should this spend be repaid

⸻

One-line versions
	•	Booking Profile: internal accounting and attribution instructions for the spend
	•	Settlement Profile: external repayment and liability-settlement instructions for the spend

⸻

Example

A travel payment may have:
	•	Mandate: Client implementation travel for Project Apollo
	•	Booking Profile: Expense GL 6210, Cost Center 4402, Client Code HDFC-01, Opex
	•	Settlement Profile: repay from India HQ current account via central corporate card facility


## Commercial Terms from ESP to Corporate
Beyond the credit facility itself, ESPs (or banks acting as ESPs) package a commercial terms stack around corporate card / virtual card / payables programs. In the Corporate Payment Product, what is relevant is the ESP terms extended to the Corporate. The terms extended by the Bank to the ESP are not modeled in the current scope.

Commercial terms are per Corporate Payment Product, not per Program. A Program represents an operational requirement in the corporate realm, not a commercial contract between ESP and Corporate.

A clean enumeration is this:

1. Core financing terms

These govern the credit itself.
	•	credit limit / sub-limits
	•	revolving vs charge-style repayment
	•	interest rate / finance charge
	•	interest-free period / grace period
	•	overlimit charges
	•	late payment charges
	•	delinquency / default charges
	•	cash-advance or equivalent financing charges, where relevant

2. Program fees

These are for running the program.
	•	program setup / onboarding fee
	•	implementation / integration fee
	•	annual program fee
	•	account maintenance fee
	•	card issuance fee
	•	virtual card generation fee
	•	replacement / reissuance fee
	•	statement fee
	•	portal / platform fee
	•	API access fee
	•	reporting / file delivery fee

3. Transaction fees

These apply per payment or payment type.
	•	domestic transaction fee
	•	international / cross-border transaction fee
	•	FX markup / currency conversion fee
	•	MCC-specific surcharge, where applicable
	•	authorization / switching fee
	•	declined transaction fee
	•	reversal / chargeback handling fee
	•	dispute processing fee
	•	refund handling fee
	•	ATM / cash withdrawal fee, if the program allows it

4. Supplier-payment / AP program charges

Common in virtual card and B2B payable programs.
	•	supplier enablement fee
	•	supplier onboarding fee
	•	remittance delivery fee
	•	payment instruction / file processing fee
	•	ERP / AP connector fee
	•	straight-through processing fee
	•	exception handling fee
	•	reconciliation / enriched data fee

5. Travel-program commercial terms

Common in lodge / travel / T&E setups.
	•	booking channel fee
	•	travel account / lodge account fee
	•	central-bill fee
	•	travel data / reconciliation fee
	•	travel-management-company integration fee
	•	unused ticket / travel exception handling fee

6. Settlement-related charges

These govern how the corporate repays the bank.
	•	auto-debit setup fee
	•	billing-account / settlement-account maintenance fee
	•	virtual account fee
	•	collection fee
	•	failed debit / failed repayment fee
	•	multi-entity settlement fee
	•	cross-border settlement fee
	•	treasury sweep / pooling-related fee, if offered

7. Controls / risk / compliance service fees

For advanced enterprise controls.
	•	custom control configuration fee
	•	spend-control rule fee
	•	fraud-monitoring fee
	•	alerting / monitoring fee
	•	compliance screening fee
	•	audit / evidence pack fee
	•	enhanced due diligence / KYC refresh fee
	•	tokenization / security service fee

8. Data / reporting / platform feature fees

For premium program capabilities.
	•	advanced analytics fee
	•	custom reporting fee
	•	real-time data feed fee
	•	ERP export / host-to-host fee
	•	API usage fee
	•	webhooks / event stream fee
	•	data retention / archive fee
	•	premium support fee

9. Rebates

These are the main economic give-backs from the bank.
	•	spend-based rebate
	•	interchange-sharing rebate, where permitted
	•	supplier-payment rebate
	•	volume-tier rebate
	•	annual threshold rebate
	•	category-specific rebate
	•	growth incentive rebate
	•	prompt-payment / disciplined repayment incentive, occasionally

10. Rewards

Usually more relevant in T&E and employee card programs.
	•	points
	•	airline miles
	•	hotel rewards
	•	cashback
	•	statement credits
	•	catalog rewards
	•	premium travel benefits
	•	lounge / insurance / concierge style bundled value

11. Commercial incentives / deal terms

These are negotiated more than published.
	•	introductory fee waiver
	•	first-year fee waiver
	•	migration incentive
	•	implementation subsidy
	•	minimum-volume commitment discount
	•	exclusivity pricing
	•	multi-product bundle discount
	•	co-investment for rollout
	•	marketing development funds, in partner-led programs
	•	custom rebate floors / tiers
	•	guaranteed service credits tied to SLA

12. Penalty / exception commercial terms

Often negotiated in enterprise contracts.
	•	minimum commitment shortfall charge
	•	contract break / early termination fee
	•	custom development abandonment fee
	•	non-standard support charges
	•	manual exception handling fee

A useful enterprise grouping is:
	•	Cost of credit
	•	Cost of operating the program
	•	Cost of transacting
	•	Cost of settling
	•	Economic upside from rebates/rewards/incentives
	•	Penalty / exception economics

One important distinction:
	•	fees and charges = explicit economics charged to the corporate
	•	rebates and rewards = economics shared back with the corporate or cardholders
	•	commercial terms = both of the above, plus thresholds, waivers, commitments, and SLA-linked provisions

A compact definition:

The commercial terms of a Corporate Payment Product are the full set of pricing, incentives, penalties, and economic-sharing arrangements that govern the use of the bank’s credit, payment rails, controls, and settlement services.


## Bank's Products and Corporate's Programs
Core entities

Corporate Payment Product

A Corporate Payment Product is the ESP-offered payment construct made available to corporates, built using the capabilities of the bank.

It encapsulates:
	•	one Spend Lane (a Product is tagged to a single Lane to simplify operations at both Corporate and ESP ends; multi-lane coverage requires multiple Products)
	•	supported control capabilities
	•	settlement mechanics
	•	commercial terms
	•	counterparty or partner specializations, where applicable

It is the thing the ESP designs, prices, contracts, and markets, using bank capabilities.

In short:
A Product is what the ESP offers.

⸻

Corporate Payment Program

A Corporate Payment Program is the enterprise-configured operating construct through which a corporate uses a Corporate Payment Product for a specific spend use case.

It encapsulates:
	•	Lane
	•	Mandate
	•	Booking Profile
	•	Settlement Profile

and binds them to:
	•	one Corporate Payment Product
	•	one Credit Facility

It is the thing the corporate configures and operates.

In short:
A Program is how the corporate puts a Product to use.

⸻

Supporting entities

Spend Lane

The operational payment flow.

It defines the nature of the spend workflow: how payments are initiated, processed, and reconciled.

Examples:
	•	Supplier Payments
	•	Employee & Department Spend
	•	Travel & Booking Payments
	•	Central Recurring Merchant Payments

⸻

Spend Mandate

The governing authorization envelope for spend.

It defines:
	•	purpose
	•	authority
	•	budget source
	•	policy scope
	•	limits
	•	attribution
	•	validity
	•	risk/compliance qualifiers
	•	supplier eligibility, where relevant

⸻

Booking Profile

The internal accounting treatment for the spend.

It defines how the transaction is recorded inside the enterprise:
	•	legal entity
	•	cost center
	•	project/client code
	•	GL account
	•	capex/opex
	•	tax/reporting treatment

⸻

Settlement Profile

The repayment and liability settlement treatment for the spend.

It defines how the corporate settles with the bank:
	•	repayment account / virtual account
	•	liable entity
	•	facility usage
	•	central vs local settlement
	•	treasury ownership
	•	billing/statement treatment

⸻

Relationship between Product and Program

Product → supplied by ESP

The ESP defines:
	•	payment capabilities
	•	supported lane behavior
	•	controls
	•	pricing
	•	rebates / fees
	•	settlement model
	•	partner/counterparty specialization

Program → configured by corporate

The corporate defines:
	•	the use case
	•	who can spend
	•	why they can spend
	•	how it is booked
	•	how it is settled
	•	how the product is operationalized internally

⸻

Clean usage principle

A Corporate Payment Program should use one Corporate Payment Product and one Credit Facility.

If the corporate needs combined or hybrid behavior, the ESP should create a new hybrid Corporate Payment Product, rather than the corporate stitching products together ad hoc.

⸻

Examples

Example 1: Supplier invoice payments

Product:
Supplier Payments Product

Program:
IT Vendor Invoice Payments Program

Program details:
	•	Lane: Supplier Payments
	•	Mandate: approved IT operations vendor spend
	•	Booking Profile: IT cost center, software services GL
	•	Settlement Profile: repay through central treasury current account
	•	Credit Facility: Corporate AP credit line

⸻

Example 2: Travel for a client implementation

Product:
Travel Payments Product

Program:
Client Rollout Travel Program

Program details:
	•	Lane: Travel & Booking Payments
	•	Mandate: travel for Bank X implementation team
	•	Booking Profile: client code + project code + travel expense GL
	•	Settlement Profile: billed to India entity, repaid from HQ settlement account
	•	Credit Facility: Travel credit facility

⸻

Example 3: Recurring SaaS subscriptions

Product:
Recurring Merchant Payments Product

Program:
Engineering SaaS Subscriptions Program

Program details:
	•	Lane: Central Recurring Merchant Payments
	•	Mandate: approved engineering tools and subscriptions
	•	Booking Profile: engineering budget, SaaS opex GL
	•	Settlement Profile: repay through centralized virtual account
	•	Credit Facility: central operating credit line

⸻

Example 4: Co-branded specialization

Product:
Travel Payments Product – Airline Co-branded Variant

Program:
Sales Team Air Travel Program

Program details:
	•	Lane: Travel & Booking Payments
	•	Mandate: approved domestic and international sales travel
	•	Booking Profile: sales cost center, travel GL
	•	Settlement Profile: settled through regional treasury account
	•	Credit Facility: sales travel line

Here, the co-branded airline terms belong to the Product, while the team-specific usage belongs to the Program.

⸻

Short final formulation

A Corporate Payment Product is the ESP’s payment offering for enterprise use.
A Corporate Payment Program is the corporate’s configured usage of that offering for a specific spend use case.

Or even shorter:

Product = what the ESP offers.
Program = how the corporate uses it.


====

## Writing Instructions for Restructure

> The sections below capture additional context, constraints, and clarifications for the rewrite into `corporate-payments-concepts.md`. Each numbered section corresponds to a concept area. Writing instructions are noted inline where relevant.

> **Structural notes for rewrite:**
> - The ontology entities should follow a logical containment/dependency order, not the order they were originally discussed.
> - Control archetypes should be explained in the context of each Spend Lane first (what controls are natural to that lane), then summarized in a dedicated section referencing the per-lane treatment.
> - Commercial Terms should be discussed before Corporate Payment Product is introduced (as input to what a Product encapsulates) or treated as a sub-section within Product. Commercial terms are per Corporate Payment Product, not per Program.
> - Reconciliation should be detailed per lane, since each lane's workflow determines what information is available and at what level.
> - Lifecycle should be detailed per lane.
> - "Embedded / ERP-native Payments" is a delivery mechanism, not a Lane. Drop it as a lane. Ensure every lane has relevant embedding capabilities through APIs and events. The document should describe four lanes: Supplier Payments, Employee & Department Spend, Travel & Booking Payments, Central Recurring Merchant Payments.
> - The document scope should focus on ESP and Corporate. Bank internals are out of scope except where needed to explain the Credit Facility, Account, and Merchant/AMC constructs.
> - Electron is the ESP-facing product (Zeta). Tachyon is the bank-facing product (Zeta). This context should be stated once.
> - Configuration authority should be described for ESP and Corporate only (who creates, modifies, views each entity).

⸻

### 1. Corporate, Legal Entity, and Organizational Units

A Corporate is a first-class logical entity in the system. It is not a Legal Entity itself — it is the top-level container that hosts the rest of the organizational structure. The Corporate entity is associated with a Client Contract (and thus to a Legal Entity) for legal provenance.

A Corporate is a collection of Legal Entities that are KYB'd by the Bank. Legal Entity is the legally accountable party to the bank. All credit, billing, and regulatory relationships anchor to Legal Entity.

The Corporate may create any number of OU (Organizational Unit) hierarchies as it needs. There can be multiple independent OU trees under a single Corporate. These are logical entities encapsulating various parties to payment — payers (employees, departments), payees (suppliers, contractors, clients/customers), and administrative roles.

All Legal Entities are by default represented as a flat OU hierarchy — one OU per Legal Entity — under a "Legal Entities" OU root node. Additional OU trees (by department, by geography, by project, etc.) can be created alongside this default structure.

OUs can span multiple Legal Entities. A "Global Engineering" OU may contain employees from three different Legal Entities. The OU is an organizational grouping; it does not determine legal ownership, which is always anchored to Legal Entity through Credit Facility.

OU hierarchies are created and maintained by the Corporate, with or without the ESP's assistance. The ESP may also create OUs on behalf of the Corporate.

If the corporate restructures, a Program's Credit Facility cannot move across Legal Entities, but Budgets can change and OU associations can change. All subsequent transactions are governed by the new Budget and reported to the new OU as required. Card assignments are not impacted — cards are associated to a Program, which in turn carries OU association.

Budget is a sub-entity of Credit Facility and is hierarchical. A Budget can have sub-Budgets. This allows the corporate to model nested allocation structures (e.g., a department budget with project-level sub-budgets underneath).

> **Writing instruction:** In the rewrite, Corporate → Legal Entity → OU hierarchy should be established as foundational context before Credit Facility, Budget, Account, or Program are introduced. The reader must understand the organizational scaffolding first.

⸻

### 2. Account, Credit Facility, Card, and Budget association

Accounts are associated with a Credit Facility and thus are owned by the Legal Entity associated with that Credit Facility. The Legal Entity is the legally liable party to the bank.

Any number of cards can be associated with an account. Typically, a card is associated with only one account.

An Account is always specific to a Corporate Payment Program. The number of accounts per Program depends on the Spend Lane:
- Employee spend lanes (travel, reimbursements) → one account per employee
- P-Card-like programs where cards are issued to suppliers → typically one account per program
- The corporate can create programs as per its billing/booking requirements

Because a card is tied to one account and an account is tied to one Program, a card cannot be used across programs. An employee who participates in both a travel program and a department spend program will carry two separate cards.

A corporate can assign a Budget to the account. Because Budget is a child of Credit Facility, the Account's Credit Facility and Legal Entity are unambiguous — there is no conflict or ambiguity in ownership. A Budget of a Program can be shared by multiple accounts within the Program (many accounts : one Budget).

The issuer cares about the Credit Facility associated with the account (credit exposure, utilization, risk). The corporate cares about the Budget associated with the account (governance, allocation, policy). Both objectives are achieved through the same account structure without contradiction.

> **Writing instruction:** Account should be defined as a first-class entity in the ontology. Its dual role — carrier of Credit Facility (bank concern) and carrier of Budget (corporate concern) — is a key design insight. Establish this before discussing Programs.

⸻

### 3. Roles in a Corporate Payment Program

An OU, or members within an OU, can play various roles in a Corporate Payment Program.

**Program Admin:** Manages the program, approves enrollments. Depending on the program, people with this role generate payment instruments (cards) to give to intended payers or payees (in the case of cards issued to suppliers). They own all controls of the program from a corporate perspective.

**Payers and Payees:** Where relevant, can also be captured under OU. A program defines eligible members (not enrolled members — enrollment is always explicit) using rules based on OUs, member type, and member attributes.

Whether the program should specify eligibility by Payer or Payee depends on the Lane (workflow) being optimized:
- Supplier Payments lane → eligibility is defined by Payee (which suppliers are eligible to receive card payments)
- Employee Spend lane → eligibility is defined by Payer (which employees are eligible to spend)
- Travel lane → eligibility depends on archetype: Payer (which travelers are eligible) for per-booking cards; Payee (which agencies are enrolled) for lodge-style persistent agency cards
- Central Recurring Merchant Payments → eligibility is defined by Payee (which merchants are approved for recurring charges)

**Cardholder assignment for supplier-issued cards:**

When a card is issued to a supplier (in the Supplier Payments lane), the Program Admin is the cardholder by default. The Card Profile carries specific tags about the Supplier the card is issued to.

If the card is enabled for ACS and second-factor authentication for transactions, then an authorized user from the Supplier should be the cardholder so that they can respond to the second-factor challenge.

In both cases, the Supplier information is tagged to the Card, irrespective of what goes in the Cardholder Profile.

> **Writing instruction:** Roles should be introduced after Program is defined. The payer-vs-payee eligibility logic per lane is an important insight — it should appear in the per-lane treatment, not only in the roles section.

⸻

### 4. Transaction posting, statements, and account-level attribution

The issuer posts all transactions to accounts. A statement is generated per account. An Account is always specific to a Corporate Payment Program.

Each posting to the account captures:
- the card used
- card-specific attributes set by the corporate
- payee-provided information (L1 and L2 data)
- all fees associated with the transaction, attributed to that transaction

L1 data (always present in every transaction):
	•	transaction amount
	•	MCC
	•	date/time
	•	merchant name / merchant identifier
	•	currency

L2 data (provided by the merchant, where supported):
	•	tax amount
	•	tax indicator / tax rate
	•	PO number
	•	invoice number
	•	customer code / corporate reference
	•	order/reference IDs passed by the merchant or gateway

L3 data (line-item detail, provided by the merchant where supported):
	•	individual line items with description, quantity, unit price
	•	item-level tax and discount
	•	product/commodity codes
	•	particularly relevant in the Supplier Payments lane for tax compliance and detailed reconciliation
	•	if provided, made available to the corporate through data extracts

Because the account is associated with a Corporate Payment Program, the Booking Profile and Settlement Profile for that program are known at posting time.

In cases like cards issued to employees, the employee may need to provide additional information about each posting (e.g., purpose, project code, client code). The Booking Profile can pick up these attributes to appropriately book transactions to the correct cost centers and cost heads.

> **Writing instruction:** This is the transaction-to-booking bridge. It should be discussed after Account, Program, Booking Profile, and Settlement Profile are established. The three sources of data on a posting must be made explicit: (1) L1 data from the network/merchant — always present, (2) L2 data from the merchant — where supported, (3) payer-provided data — added by the cardholder during or after the transaction (e.g., expense coding by an employee). The card itself also carries corporate-set attributes (supplier tags, program metadata).

⸻

### 5. Mandate enforcement

All mandates — Budget limits, Spend Policies — are enforced inline to the transaction by the bank. The bank only accepts mandates it can enforce. The capabilities are quite rich.

The elements of a Spend Mandate fall into two categories:

**Enforceable at authorization time** (by the issuer):
- Budget limits — enforced through the Budget hierarchy; all ancestors are consulted
- Spend policies — MCC restrictions, amount limits, velocity limits, merchant locks, geography restrictions
- Card-level controls — restrictions placed on the card may accomplish controls pertaining to purpose (e.g., limiting where and with whom a card can be used)

**Auditable but not enforceable at swipe:**
- Business purpose
- Accountability and attribution
- These are governance metadata — they enable post-transaction audit, reporting, and justification, but cannot be evaluated at the point of authorization

Mandate controls translate into card-level controls at issuance time and also exist as a separate policy layer evaluated at authorization. Both enforcement points are used, with relevant controls enforced at the appropriate time.

Budget is utilized at the time of authorization. Adjustments are made at the time of clearing. There is no concept of "pending spend" at Budget level. "Uncleared" transactions are only a concern at the Account level.

> **Writing instruction:** State the enforcement principle clearly in the Spend Mandate section: mandates are not advisory; they are enforced at authorization time by the issuer. The auditable-vs-enforceable distinction is important — the rewrite should make this a first-class concept within the Mandate definition. Detail of enforcement capabilities is out of scope for this document — note that and point to a future controls/policy document.

⸻

### 6. Reconciliation per lane

The reconciliation process varies by each Spend Lane. Each lane's workflow determines whether the relevant information for reconciliation is available at:
- card level
- account level
- posting level

And if at posting level, whether that information comes from the payee (merchant data, L1/L2) or from the payer (during or after the transaction, e.g., expense coding by an employee).

Supplier/Merchant entities are not directly mappable across domains (see section 7). The corporate reconciles Supplier association using:
- Card Data — supplier tags set by the corporate on the card at issuance
- L1 Data from the posting — transaction amount, MCC, date/time, merchant name/identifier, currency
- L2 Data from the merchant — tax amount, PO number, invoice number, customer code/corporate reference, order/reference IDs

The combination of card-level supplier tags and posting-level merchant data provides the reconciliation bridge between the corporate's Supplier and the bank's Merchant.

> **Writing instruction:** Reconciliation should be detailed per lane with typical examples. Do not treat reconciliation as a single generic process — each lane has a different information availability profile. Include this in the per-lane treatment in the rewrite. Research and document typical reconciliation patterns for each of the four lanes (Embedded is now a delivery mechanism, not a lane).

⸻

### 7. Supplier / Merchant duality

These are not mappable entities. They represent different concepts and serve different purposes in their respective domains.

**Bank side — Merchant:**
A supplier, to the bank, is either:
- a directly affiliated merchant
- a merchant discovered through the card networks

The authentic bank-side term is **Merchant** — which may be Direct, Aggregated, or Discovered.

In Zeta's context, a group of merchants is recognized through an "Authorized Merchant Category (AMC)." In all commercial terms, AMCs are used as opposed to individual merchants. The bank may define AMCs using MIDs, TIDs, MCCs, names, locations, or patterns based on such attributes.

The bank uses Merchant/AMC information for: commercial terms, controls, and authorization decisions.

AMCs are also usable in Spend Policy rules by ESPs and Corporates — not only for commercial terms. A Spend Policy can reference AMCs for allow/block rules (e.g., "allow transactions only at merchants in AMC-Travel"). ESPs and Corporates may also request custom AMCs to be defined.

**Corporate side — Supplier:**
A Supplier is a type of member in an OU. The corporate defines Suppliers in its own organizational terms.

The corporate uses Supplier information for: card issuance, spend governance, and reconciliation.

**These two are not the same entity and cannot be directly mapped.** The correlation between Supplier-as-recognized-by-the-corporate and Merchant-as-recognized-by-the-bank may not be identical. Each relies on the relevant entities in its own domain. One should not be confused for the other, although the word "Supplier" may be used interchangeably in conversation.

The corporate reconciles Supplier identity from transaction data using Card Data (supplier tags set at issuance) and Posting Data (L1 and L2 data from the merchant — see section 4 and section 6 for details).

> **Writing instruction:** This duality must be stated clearly in the ontology. Define Merchant as a bank-domain entity and Supplier as a corporate-domain entity. Introduce AMC as the Zeta-specific grouping mechanism on the bank side. Warn explicitly against conflating the two. The reconciliation bridge (card tags + L1/L2 posting data) should be cross-referenced from the per-lane reconciliation treatment.

⸻

### 8. Program residency, multi-entity, multi-currency, billing, and settlement

**Residency:**
To the bank, a Corporate Payment Program's residency is the same as the residency of the Account(s) backing it, which is determined by the Credit Facility associated to the Program by the Corporate.

However, the members of the program — whether payers or payees — can be from any entity of the corporate, any OU, any location, as the corporate deems fit, as long as the bank's jurisdiction and product terms are not violated.

**Billing:**
Billing is performed by the ESP. Billing is at account level and is submitted to the corporate with the Legal Entity (to which the corresponding Credit Facility is extended) as the payer. The billing configuration at the ESP end determines the billing cycle, payment due date, interest-free period, and subsequent penalties.

**Settlement:**
Settlement is performed by the corporate against the bills/invoices received from the ESP, as per the Settlement Profile in the Payment Program created by the corporate. The Settlement Profile indicates how invoices from the program are settled, including auto-pay configuration and payment-date-related settings. The system supports only one Settlement Account in a Settlement Profile per Program. As good practice, the corporate may use a bank account associated with the same Legal Entity to which the account's Credit Facility belongs, but this is not a bank enforcement — it is a corporate-administered control. Invoices are paid using the settlement account configured in the Settlement Profile of the Program to which the account belongs.

**Multi-currency:**
Transactions are always posted to the account in the account's base currency. This currency is the same as the Credit Facility's currency. Settlements are also performed in the same currency. However, the settlement account could be in any currency as the corporate may choose. A bank may have extended multiple Credit Facilities in different currencies to the corporate.

**Disputes and refunds:**
Disputes are settled by the bank against the Account associated with the Program. Reversal/credits issued are attributed to the original postings, so reconciliation and adjustments can be handled without ambiguity.

Refunds inherit the Booking Profile and Settlement Profile of the original transaction. Settlement Profile is scoped to the account, so unmatched refunds are not a problem for settlement. The Booking Profile may have a default allocation for unmatched credits.

> **Writing instruction:** Residency, billing, and settlement mechanics should be covered after Account, Credit Facility, Program, and Settlement Profile are all defined. Multi-currency is a property of Credit Facility and should be noted there, with settlement-currency flexibility noted under Settlement Profile. The key insight — members can span entities and geographies even though residency is pinned by Credit Facility — should be stated clearly. The single-settlement-account-per-Program constraint is important — if a corporate needs different settlement accounts by region, it needs separate Programs.

⸻

### 9. ESP — Enterprise Service Provider

An ESP (Enterprise Service Provider) is the partner of the bank conducting the corporate payments business for the bank. ESPs may specialize in one or more Spend Lanes and bring variants of value to corporates. It is possible that the bank itself acts as an ESP.

The ESP has its own entity model and database. It is an independent persona with an independent product called **Electron** providing the required capabilities to ESPs and Corporates. **Tachyon** provides capabilities to the Bank to support ESPs and Corporates for pure bank-scope functions — Payments, Accounts, KYB, KYC, Credit Facilities, etc.

Wherever the document mentions the bank creating Corporate Payment Products, it should be understood that it is the ESP creating such tailored products using the capabilities of the bank.

Division of responsibility:
- **ESP:** sources corporates, creates and packages Corporate Payment Products, supports corporates operationally
- **Bank:** handles underwriting, extends Credit Facilities, provides accounts and payments infrastructure

The commercial terms of a Corporate Payment Product are defined by the ESP without violating the regulatory and policy enforcements of the bank. In the Corporate Payment Product, what is relevant is the ESP terms extended to the Corporate. The terms extended by the Bank to the ESP are not modeled in the current scope.

Commercial terms are per Corporate Payment Product, not per Program. A Program represents an operational requirement in the corporate realm, not a commercial contract between ESP and Corporate.

The system supports a Legal Entity being a customer of multiple ESPs. Whether a corporate works with multiple ESPs under the same bank is a business arrangement question, outside the product and system realm.

If an ESP is replaced while the corporate stays with the same bank:
- Credit Facilities survive (they are bank-scoped)
- Programs do not survive (they are ESP-scoped and must be recreated under the new ESP)

The Bank-to-ESP commercial relationship (P&L) is not in scope for this document.

**Spend Lanes are extensible.** ESPs define new Lanes with help from Zeta. The bank need not be involved in Lane definition.

> **Writing instruction:** ESP should be introduced early — after the two-lens problem (bank vs corporate), before Products are discussed. It reframes who the product creator is. Every subsequent reference to "the bank creates a Product" should be understood as "the ESP creates a Product using bank capabilities." Zeta provides the technology for both Bank and ESP. The Electron/Tachyon split is important context for PMs — Electron is the ESP-facing product, Tachyon is the bank-facing product. The document scope should focus on ESP and Corporate, not Bank internals.

⸻

### 10. Program lifecycle per lane and entity state models

The lifecycle of a Corporate Payment Program should be defined for each Spend Lane. Steps include setup, configuration, member enrollment, card issuance, operation, review, amendment, and wind-down.

**Entity state models:**

The following entities should have explicit state models defined in the rewrite:

Corporate Payment Program:
	•	Draft → Active → Suspended → Closed

Credit Facility:
	•	Active → Under Review → Terminated

Budget:
	•	Open → Exhausted → Frozen → Closed

Account:
	•	Active → Suspended → Closed

Card:
	•	Issued → Active → Suspended → Cancelled → Expired

> **Writing instruction:** Research and document the typical lifecycle steps for each of the four lanes (Embedded is a delivery mechanism, not a lane). Each lane will have variations — e.g., supplier enablement is a lifecycle step in the Supplier Payments lane but not in Employee Spend. Include in the per-lane treatment. State models should appear alongside each entity's definition in the ontology section, showing what operations are possible in each state.

⸻

### 11. Data and reporting

All posting data is made available as and when transactions are cleared (near real-time). Statements are shared in data-extract format of the corporate's choosing — usually CSV.

Every posting in a statement or in a real-time event contains all the data:
- account-level attributes
- card-level attributes
- posting-level attributes (as discussed in section 4 above)

> **Writing instruction:** Data and reporting should be a short section after transaction posting is explained. The key point is: no separate "reporting" entity — reporting is a view over posting data, enriched by account, card, and program context.

⸻

### 12. Zeta's role

Zeta provides the complete technology for both Bank and ESP.

> **Writing instruction:** State once, clearly, in the Purpose/Audience section. Zeta is building the platform that powers the bank's issuing and payments infrastructure and the ESP's product-creation and corporate-servicing capabilities. This frames why a Zeta PM needs to understand both lenses.

⸻

### 13. Card Profile

A Card Profile is the full configuration attached to a card at issuance. It comprises four sub-structures:

**Cardholder Profile:**
	•	name on card
	•	address
	•	email and phone number (used for ACS second-factor authentication and notification delivery)
	•	custom attributes mapping the cardholder to the corporate domain: CorporateMemberType, CorporateMemberID

**Spend Policy / Payment Usage Policy:**
	•	velocity and volume limits using tumbling windows (daily, weekly, monthly, quarterly, annually)
	•	limits scoped to merchant category, AMC, time-slices
	•	life-to-date limits
	•	restrictions on allowed/disallowed transactions based on various attributes in the authorization request

**Fee Overrides:**
	•	overrides for various fees assessed on the card

**Tags:**
	•	structured object extensions to capture data at card level (serialized as URI format for each tag type)
	•	use cases: Corporate Program Information (Corporate ID, Program ID, Member ID, Membership ID), Intended Supplier Information, Reconciliation Tracking Information
	•	tag data can be referenced in the Payment Usage Policy rules

> **Writing instruction:** Card Profile should be defined as a sub-entity of Card in the ontology. The Tags sub-structure is the mechanism by which corporate domain context (supplier identity, reconciliation references, program metadata) is carried on the card. This is the bridge between the corporate's world and the card's behavior at point of sale.

⸻

### 14. Member

Member is a first-class entity of a Corporate, with a member-of affiliation to zero or more OUs.

**Default Member Types:**
	•	Employee
	•	Supplier
	•	Contractor
	•	Client

A Corporate can define custom attributes for every member type as needed for mapping members to its enterprise systems.

**Eligibility and enrollment:**
	•	a Member is eligible for enrollment into a Payment Program based on the program's eligibility rules
	•	an eligible Member can be enrolled by the Program Admin using various tools — UI, Files, APIs
	•	each enrollment results in a virtual card and optionally account-based program constructs (depending on the lane)
	•	an eligible Member can have multiple enrollments into the same program; each enrollment represents a new card (supporting one-time-use cards, ad-hoc/short-lived cards, etc.)
	•	in specific cases, enrollment may require steps to be fulfilled by the cardholder for KYC purposes; this may be conditional

> **Writing instruction:** Member should be defined as a first-class entity in the ontology, after Corporate and OU. The enrollment lifecycle (eligible → enrolled → card issued) is a key operational flow and should be described clearly. The ability to have multiple enrollments per Member per Program is important — it enables single-use card patterns within the same program.

⸻

### 15. Client Contract

A Client Contract is an entity in the ESP domain that represents the commercial relationship between the ESP and a real-world Corporate.

A Corporate comes into existence through a Client Contract. The contract may have been signed by one or more Legal Entities corresponding to that Corporate.

Example: Walmart could be a Corporate, but it may have multiple Legal Entities through which its business is conducted. The ESP initiates Corporate onboarding using a Client Contract signed by one or more of those Legal Entities.

A Client Contract may have extensions and renewals, but the system may not model all of that.

> **Writing instruction:** Client Contract should be mentioned briefly when introducing Corporate — it is the entity through which a Corporate is created. It belongs to the ESP domain. Do not over-elaborate; note that it establishes legal provenance and move on.

⸻

### 16. Spend Policy (cascading restriction model)

Spend Policy is a sub-entity of the Mandate (conceptually, a sub-section of the Corporate Payment Program).

The Spend Policy follows a cascading restriction model across three levels:

1. **ESP level** (in Corporate Payment Product): the ESP configures the baseline Spend Policy, defining the maximum envelope of what is permitted
2. **Corporate level** (in Corporate Payment Program): the Corporate configures a Spend Policy for the program; this can only be more restrictive than the ESP-defined policy — it cannot expand the restrictions or controls set by the ESP
3. **Card level**: the Corporate may define a per-card Spend Policy; this can only be more restrictive than the program-level policy

Each level can only tighten controls, never loosen them.

Spend Policy can also be overridden per Card (within the tightening-only constraint).

> **Writing instruction:** The cascading restriction model (Product → Program → Card, tighten-only) is a fundamental design principle. It should be stated prominently in the Spend Mandate / controls section. It explains how ESP governance, corporate governance, and card-level controls compose without conflict.

⸻

### 17. Spend Mandate is not a single entity

There is no single Mandate entity in the system. All relevant aspects of the Mandate are sub-sections of the Corporate Payment Program entity.

Entities referenced within or by the Payment Program:
	•	Credit Facility
	•	Budget
	•	Settlement Accounts
	•	OUs
	•	Members
	•	Users

**Users** are people entitled to create and operate Payment Programs in the Corporate, with relevant authorization controls limiting their scope to specific programs, products, budgets, and OUs. Users and Members are entities in different domains. The User entity is relevant only for administration and operational use cases. Members are the participants in programs. A person can be both a User (administering one program) and a Member (enrolled as a spender in another program) — these are separate entity instances in separate domains.

**Program ownership:** A Program is always owned by an OU, irrespective of the members who may be eligible. Budgets of the owning OU are visible during program setup.

**Budget-OU association:** Budgets are associated with OUs. This means the OU that owns the program determines which Budgets are available for that program.

> **Writing instruction:** The Mandate concept remains valuable as an explanatory framework, but the rewrite should make clear that it is realized as the composition of Program sub-sections — not as a standalone entity. Users should be introduced as actors who operate Programs, distinct from Members who are enrolled into Programs. Clarify that User and Member are entities in different domains — a person can hold both roles. The Program-owned-by-OU and Budget-associated-with-OU relationships are important structural constraints that affect program setup.

⸻

### 18. Per-lane control archetypes and reconciliation patterns

**Supplier Payments:**
	•	Controls: single-use card, one card per invoice or PO. If for a PO, the card may be multi-use. Single account per program.
	•	Reconciliation: card (supplier-tagged) + posting (invoice number and other L2 attributes) matched against AP invoice in ERP.

**Employee & Department Spend:**
	•	Controls: multi-use card, one account per employee, MCC-restricted. Optional data-capture form for each spend — configured at program setup, designed to capture sufficient information to meet the data needs of the Booking Profile. "Form" is a metaphor; the actual UI could be anywhere, including Electron's default UI. APIs are provided to add this additional information against each Posting. The captured data flows into the Booking Profile rules for cost-center attribution. Optional approval workflow involving an approving authority per employee (as defined in enrollment) and optionally a group of users nominated by the Program Admin.
	•	Reconciliation: if the program requires the employee to provide an expense code, that is used. If the program is for a single cost head and expense code, that information is available at the program level itself — no per-transaction input needed.

**Travel & Booking Payments:**
	•	Controls: both single-use per booking and lodge-style persistent per agency are possible. Mostly persistent per agency.
	•	Reconciliation: posting matched against itinerary/booking reference provided by the agency in L2 data.

**Central Recurring Merchant Payments:**
	•	Controls: one card per project or cost head. Can be used at various merchants/suppliers with whitelist- or blacklist-based restrictions. Persistent.
	•	Reconciliation: posting matched against subscription/contract record.

> **Writing instruction:** These per-lane archetypes should be woven into the per-lane treatment in the rewrite. Each lane section should cover: control archetype, account structure, card issuance pattern, reconciliation pattern, and eligibility model (payer vs payee). The optional approval workflow in Employee Spend is an important feature to highlight.

⸻

### 19. Card form factor, enrollment, approval, FX, billing, L3, and scope

**Card form factor:**
A "virtual card" can be either physical or digital in form factor. A card can be initiated as a digital card but converted to a physical card. The word "virtual" in the industry does not refer to form factor — it indicates that the card itself does not carry a financial obligation; the obligation comes from the Account. This is an industry term distinguishing from card systems where card and account are tightly coupled, and has no operational relevance in the system.

**Approval engine:**
Electron provides an in-platform approval workflow engine. At the time of program setup, the approval workflow can be configured — including approving authority per employee and nominated approval groups.

**FX mechanics:**
When a card is used cross-border in a different currency from the account base currency, FX conversion happens at the network level. The corporate bears the FX risk.

**Master statement:**
For programs with multiple accounts (e.g., employee-spend programs with one account per employee), a master statement for the program is provided. Electron generates this master statement by compiling the individual account-level statements received from the issuer.

**L3 data:**
Level 3 data (line-item detail) is relevant. If provided by the merchant, it is made available to the corporate through data extracts. L3 is particularly relevant in the Supplier Payments lane for tax compliance and detailed reconciliation.

**Network model:**
The four-party model (issuer, acquirer, network, merchant) is assumed knowledge for the target audience. Note: programs can also work on Private Label cards, where the acquirer and issuer may be the same entity.

**Out of scope for this document:**
	•	Bank-to-ESP P&L and commercial relationship
	•	Card network protocol internals
	•	Regulatory specifics per jurisdiction
	•	Fraud management
	•	AML/sanctions screening
	•	Dispute resolution procedures

> **Writing instruction:** Card form factor clarification should appear where Card is first defined — dispel the "virtual = digital-only" assumption immediately. The approval engine should be noted in the roles/enrollment section. FX belongs in the multi-currency treatment. Master statement belongs in data/reporting. L3 data should be added to the posting data description alongside L1 and L2. Out-of-scope items should be stated in the Purpose/Audience section of the rewrite.

⸻

### 20. Spend Lane as workflow archetype

Lanes should be treated as archetypes of workflows. The labels (Supplier Payments, Employee & Department Spend, Travel & Booking Payments, Central Recurring Merchant Payments) are indicative. The description for each lane should specify what the lane is meant for as a workflow pattern, not just a label.

> **Writing instruction:** When describing Spend Lanes, emphasize they are workflow archetypes. The names are suggestive, but the core definition is the operational pattern — control model, card lifecycle, enrollment model, reconciliation approach — not the name.

⸻

### 21. Document structure and tone

The final `corporate-payments-concepts.md` should be a **hybrid** document — structured as a book rather than a single flat document. It should have:
- **Authoritative reference sections** — precise definitions, structured for lookup, independent of surrounding narrative.
- **Narrative sections** — progressive narrative that builds concepts for first-time readers.

The two types of sections should be clearly distinguishable. A PM should be able to read it cover-to-cover on first encounter, then use the reference sections for subsequent lookup.

> **Writing instruction:** Structure the rewrite as a hybrid book. Use narrative prose to introduce and connect concepts progressively. Use clearly demarcated reference sections (entity definitions, state models, control archetypes) that stand on their own for lookup. Avoid mixing the two styles within a single section.

⸻

### 22. Bank's Role — Account Products, Virtual Card Products, and ESP Variants

The Bank (on Tachyon) makes redistributable **Account Products** and **Virtual Card Products** accessible to ESPs. These are redistributable — a single Account Product or Virtual Card Product can be used by multiple ESPs. The ESP creates Corporate Payment Products using these bank-provided products as building blocks. The bank also maintains a catalog that ESPs can browse and select from; ESPs may additionally request custom products from the bank.

**Account Products (Bank-defined, Tachyon entity):**

When an Account is created for a Program using a Corporate Payment Product, the bank creates the Account under the corresponding Account Product. An ESP may request new Account Products from the Bank.

A Bank's Account Product defines:
- Supported billing cycles
- Delinquency controls
- Base fees and charges applicable to the account

Currency: Account Product currency must match Credit Facility currency. However, the Account Product itself does not recognize Credit Facility — the Credit Facility is associated per Account at account-creation time.

State model for Account Products is out of scope for this document (bank-internal).

**ESP Account Variant (ESP-defined, Electron entity, overrides Bank defaults):**

An ESP may define specific programs to customise and override the Bank's Account Product parameters:
- Fee Programs
- Interest Programs
- Statement Program
- Reward Programs
- Rebate Programs
- Notification Program

These are collectively referred to as an **ESP Account Variant**. Such an ESP Account Variant can be used while creating an ESP Corporate Payment Product.

Override model: Bank's base programs serve as fallback for any parameters the ESP has not overridden. ESP can make all commercial choices within the scope of programs accessible to the ESP — including reducing fees and charges. The charges made to the bank may or may not represent revenue to the bank; this depends on the Bank-ESP arrangement (out of scope).

What the bank retains exclusively: credit risk parameters, AML controls, and other compliance-related parameters are not accessible to the ESP.

Variants can be reused across multiple Corporate Payment Products. An ESP may also create dedicated variants for large customers. Variants provide branding options for cards, statements, and notifications.

Notification Program (Account Variant): Configures account-level notifications — billing alerts, credit utilization thresholds, delinquency warnings, statement availability. Recipients are typically the Corporate Users configured as Program Admins for the Corporate Payment Program to which the Account is mapped. Credit Facility-related notifications are delivered to the configured contacts for the Legal Entity, over and above the program-level contacts.

State model for ESP Account Variants: to be defined (in scope for this document).

**Virtual Card Products (Bank-defined, Tachyon entity):**

The Bank provides Virtual Card Products to an ESP. An ESP can request custom products from the bank.

A Virtual Card Product could support multi-network and multi-clearing-house arrangements. The bank chooses which card schemes to make available and which scheme card to issue when a card is requested. Irrespective of the scheme to which a card belongs, transactions may be presented through multiple payment networks if the bank has such relationships.

A Card Product provides all the details for a specific product arrangement. Settlement to various networks is the bank's obligation. Dispute resolution is also the bank's obligation.

State model for Virtual Card Products is out of scope for this document (bank-internal).

**ESP Virtual Card Variant (ESP-defined, Electron entity, customises Bank's Virtual Card Product):**

An ESP may create an ESP Virtual Card Variant using:
- Embossing Program
- Spend Program (also known as Payment Usage Program)
- Authentication Program
- Tokenisation Program
- 3DS Program
- Card Fee Programs
- Notification Program

Such an ESP Virtual Card Variant can be used while creating an ESP Corporate Payment Product.

Override model: same as Account Variant — all commercial and operational parameters are available for the ESP. Compliance and fraud risk parameters are not accessible and are exclusively managed by the bank. However, for a limited scope, the bank provides User-Managed-Risk parameters to ESP and the cardholder (discussed in FRM documentation — out of scope for this document).

Variants can be reused across multiple Corporate Payment Products.

Notification Program (Virtual Card Variant): Configures card-level notifications — transaction alerts, authorization declines, card expiry reminders. Delivered based on Cardholder Profile information (email, phone). Also includes SMS and email OTP notification for second-factor authentication.

Notification customization: ESP can customize notification templates per Variant (branding, language, content). Corporate can further customize at the Program or card level. All notification channels supported: email, SMS, push, webhook/API callback. All notification template changes go through review from bank executives.

Bank-originated notifications (regulatory disclosures, fraud alerts): ESP cannot suppress these but can suggest templates.

State model for ESP Virtual Card Variants: to be defined (in scope for this document).

**Corporate Payment Product Assembly:**

A Corporate Payment Product references exactly one ESP Account Variant and exactly one ESP Virtual Card Variant. Multiple CPPs can share the same Variant.

**Processing and Policy Enforcement:**

The Bank is responsible for processing payments and posting them to accounts. All processing honours all policies applicable to the card and account — the bank enforces all Spend Policies (including ESP-level and Corporate-level policies) at authorization time.

ESP and Corporate both have an option to participate in authorization processing if the controls provided by the bank are inadequate to meet their needs.

The Bank provides account-level Rewards and Rebate computations based on the programs configured (ESP Account Variant). This is the mechanism the ESP relies on for product-level rewards and rebates. The ESP system (Electron) provides its own mechanism for relationship-level rewards and rebates.

**Bank-side controls beyond Spend Policy:**

Beyond the Spend Policy cascade (Product → Program → Card), the bank enforces controls at the Account Product level that the ESP cannot override: all regulatory checks, bank-defined fraud checks, credit facility related restrictions, delinquency related controls, NPA tracking, and compliances related to customer servicing.

**Bank's journey:**

The Bank part in the book should cover:
- ESP onboarding
- Corporate's Legal Entities' onboarding (KYB)
- Making Account Products and Virtual Card Products available to ESPs
- Extending Credit Facilities to Legal Entities

> **Writing instruction:** A dedicated Part for the Bank should be added to the book structure, placed before the ESP part. The Bank's role is foundational — it creates the Account Products and Virtual Card Products that the ESP customises into Variants, which are then assembled into Corporate Payment Products. The flow is: Bank creates base products → ESP customises via Variants → ESP assembles into Corporate Payment Products → Corporate configures Programs.
>
> Key entities to define:
> - Account Product (Tachyon entity) — redistributable, multi-ESP
> - Virtual Card Product (Tachyon entity) — redistributable, multi-ESP, multi-network, multi-clearing-house
> - ESP Account Variant (Electron entity, composed of Fee/Interest/Statement/Reward/Rebate/Notification Programs)
> - ESP Virtual Card Variant (Electron entity, composed of Embossing/Spend/Authentication/Tokenisation/3DS/Card Fee/Notification Programs)
>
> The relationship chain: Account Product → ESP Account Variant → Corporate Payment Product → Corporate Payment Program should be made explicit.
> Similarly: Virtual Card Product → ESP Virtual Card Variant → Corporate Payment Product → Corporate Payment Program.
>
> Assembly rule: one ESP Account Variant + one ESP Virtual Card Variant = one Corporate Payment Product. Variants reusable across CPPs.
>
> Control boundary: Bank retains credit risk, AML, compliance, fraud, delinquency, NPA, regulatory, and customer servicing controls. ESP gets all commercial and operational parameters. Limited User-Managed-Risk parameters shared with ESP and cardholder (FRM scope).
>
> Authorization: Bank enforces all policies inline. ESP and Corporate can optionally participate.
>
> Rewards/Rebates: Account-level computation by Tachyon (per ESP Account Variant programs). Relationship-level computation by Electron.

⸻

====
## FAQ

Why do enterprises often buy virtual card capability through separate AP, T&E, and spend-management tracks instead of under one finance transformation program?

What else, besides control and reconciliation, determines whether a virtual card program gets adopted by procurement, treasury, or travel teams?

What would happen if an enterprise standardized on only single-use cards and refused persistent multi-use virtual accounts altogether?

One more why: why must the mandate exist at issuance time rather than be inferred later during reconciliation?

One more what else: what else should a mandate carry in your world — risk classification, regulatory treatment, or pre-approved supplier set?

One more what would happen if: what would happen if the mandate were editable after spend without a controlled audit trail?
