# Chapter 03.02.36: Influence Fabric — Product Note

**The enterprise loyalty and incentivization System of Record (SOR) and rules engine — owning incentive constructs, reward balance ledgers, vouchers, and the query logic that resolves eligible and availed benefits for identified users.**

---

## What It Governs

Influence Fabric is the authoritative domain-specific Banking Fabric for customer incentivization, loyalty, and behavioral motivation. Rather than operating as a disconnected infrastructure layer or separate marketing campaign tools, Influence Fabric serves as the transaction and rules engine that houses the system of record for all incentive constructs (such as vouchers, reward points, cashback limits, discount templates, and dynamic pricing rules) that are orchestrator-agnostic. 

Out of scope: direct channel messaging and delivery mechanics (delegated to Engagement Fabric), direct customer event detection and processing (delegated to Cognition Fabric), and front-end campaign content authoring (delegated to Hubs).

---

## Source of Truth

- **Entities owned:** Incentive constructs (voucher definitions, points models, cashback thresholds, dynamic fee-waiver configurations), active voucher instances, customer reward balance ledgers, customer cashback accumulation limits, dynamic pricing policies.
- **Key invariants:** 
  - Reward ledger transactions are immutable and double-entry balanced.
  - Active vouchers must map to a valid, unexpired incentive construct.
  - Cashback accumulations cannot exceed defined campaign limits.
  - Query APIs require verified/identifiable user tokens and are strictly blocked/not applicable for anonymous or unidentifiable prospects.
- **Configurable vs. compliance floor:** Incentive values, point conversion ratios, cashback caps, eligibility rules, and expiry dates are configurable per campaign. Compliance floor: Strict accounting controls for points/ledger balances, secure cryptographic signing of issued vouchers, and GDPR/CCPA data-deletion compliance.

---

## Scope Highlights

- **Incentive Constructs:** Defining, versioning, and managing vouchers, rewards, cashback limits, and dynamic fee templates.
- **Rules Engine & Ledgers:** Evaluating eligibility and keeping track of points, cashback balances, and redemption states in a double-entry reward ledger.
- **Query/Read Capability Model:** Providing high-performance APIs to resolve 'Eligible' and 'Availed' incentives for an identified user across three distinct scopes:
  - **Global Scope:** Across all relationships (evaluating the complete customer profile and relationship space at the bank via Party_ID).
  - **Relationship Scope:** Bounded to a specific relationship (e.g., within a particular credit card account or deposit account scope).
  - **Journey Scope:** Bounded within an active application journey (e.g., an ongoing loan or credit card application before the applicant becomes a full customer).
- **Campaign Orchestration Division:** Partitioning orchestration context across specialized Hubs to keep the core rules engine clean:
  - **Distribution Hub:** Leads, prospecting, and referral campaigns before a customer relationship is established.
  - **Relationship Hub:** Relationship context, lifecycle nudges, and cross-sell rewards.
  - **Operations Hub:** Back-office exceptions, waivers, and settlement discount offers.

---

## Capability Domains

### 1. Incentive Constructs & Systems of Record

The authoritative system for defining and maintaining the lifecycle of vouchers, points models, cashback limits, and dynamic fee templates.

| Capability | What It Delivers |
|---|---|
| Construct taxonomy | All incentive types modeled in a common framework — rewards (points, miles), cashbacks (post-transaction rebates), promotions, and vouchers. Each type has defined attributes, constraints, and lifecycle rules. |
| Reward points ledger | Double-entry accounting system that tracks reward points, miles, or loyalty balances. Ensures immutable, auditable credit and debit transactions. |
| Voucher lifecycle manager | Issues, activates, suspends, and redeems distinct voucher instances, preventing double-redemption or fraudulent use. |
| Cashback & limit tracking | Maintains real-time accumulation trackers against defined campaign caps to prevent over-allocation of marketing funds. |

### 2. Query & Resolution Engine

Provides high-performance, secure read APIs that evaluate eligibility and fetch historical incentive states.

| Capability | What It Delivers |
|---|---|
| Eligible benefits resolution | Resolves which reward points, vouchers, cashbacks, or dynamic pricing models are currently active and available to the user based on evaluated rules. |
| Availed benefits tracking | Provides historical lookup of all incentives that have already been claimed or redeemed by the user. |
| Multi-scope query evaluation | Supports queries at three distinct boundaries: Global Scope (via Party_ID), Relationship Scope (via Account_ID), and Journey Scope (via Journey_ID). |
| Secure identity constraint | Enforces a strict identity requirement: query APIs are blocked/not applicable for anonymous or unidentifiable prospects, ensuring data privacy and preventing fraudulent eligibility mining. |

### 3. Campaign Orchestration Division

The structural partitioning of campaign execution across the bank's operational hubs, separating policy design and delivery from the core rules engine.

| Capability | What It Delivers |
|---|---|
| Distribution Hub orchestration | Manages top-of-funnel campaigns, prospect referrals, and pre-relationship acquisitions, where users are partially identified or referred. |
| Relationship Hub orchestration | Manages deep customer engagement, loyalty programs, cross-selling, and lifecycle milestones for fully authenticated and onboarded customers. |
| Operations Hub orchestration | Manages back-office exception workflows, fee waivers, goodwill gestures, and settlement discount offers. |

---

## Relationship to Other Fabrics

Influence Fabric serves as a core Banking Fabric that relies heavily on our Infrastructure Fabrics:

| Fabric | Relationship |
|---|---|
| **Trust Fabric** | Enforces consent and communication preferences during any marketing/loyalty interactions. |
| **Truth Fabric** | Standardizes semantic definitions of "customer," "account," and "transaction" that feed into eligibility rule evaluations. |
| **Engagement Fabric** | Delivers the generated vouchers, reward summaries, and promotional notifications to the end customer. |
| **Intelligence Fabric** | Provides the behavioral segmentation and propensity scores that determine which rules and incentive structures to apply. |
| **Cognition Fabric** | Publishes real-time customer event streams (e.g., transaction swiped, loan application started) that trigger incentive evaluations. |
| **Memory Fabric** | Maintains the historical trail of all issued, expired, and redeemed incentives for auditing and analytical purposes. |

---

## References

- [Engagement Fabric](../01-infra-fabrics/09-engagement-fabric.md) — Multi-channel interaction infrastructure
- [Modeling Channels](../../../../02-the-thesis/07-the-hub-way/03-enablement/05-modeling-channels.md) — Closed-loop telemetry and attribution
- [The Thesis](../../../../02-the-thesis/README.md) — Architectural principles and structural argument
