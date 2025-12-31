# Features as Data Products: From Feature Builders to Self-Service Decisions

## A Practical Assessment and Path Forward

---

## TL;DR

**The Problem:**
Features serve their builders well. They don't serve their users.

The feature engineer who builds a feature can navigate, explain, and consume it. Everyone else — product managers, risk analysts, compliance teams — is locked out. Discovery is tribal. Reuse is rare. Semantic context lives in the builder's head, not in the infrastructure.

This isn't a feature store problem. Storage and serving are solved. **Features lack the semantic infrastructure to function as data products.**

**Why It Matters:**
Features power critical decisions: fraud detection, credit scoring, personalization, rewards. But today, they're internal implementation details — invisible, undocumented, and inaccessible to their rightful users. And tomorrow, when AI agents become the builders, the lack of semantic structure will make their work incomprehensible and ungovernable.

**The Argument:**
Build the semantic layer — Entity Registry, Feature Catalog, business-language metadata — so features become discoverable, understandable, and usable by the people (and agents) who need them. This is the foundation for self-service decisions where domain experts can author, test, and deploy logic without engineering as a permanent bottleneck.

---

## Scope of This Document

### What This Is About

**Features are enterprise data products.** They represent curated, computed knowledge about business entities — customers, accounts, transactions, merchants. Features power decisions: fraud detection, credit scoring, personalization, rewards optimization.

This document addresses a fundamental gap: **the current state of feature infrastructure doesn't serve the rightful users of features.**

| From (Today) | To (Target State) |
|--------------|-------------------|
| Features are columns in tables | Features are properties of business entities |
| Entities are implicit row keys | Entities are defined concepts with relationships |
| Composite entities don't exist | Composites (Customer × Merchant) are first-class |
| Discovery requires tribal knowledge | Discovery is self-service, business-language browsable |
| Only feature engineers can navigate | Product managers, analysts, developers can participate |
| Decision logic requires engineering | Domain experts author rules using self-service tools |
| Lineage is buried in code | Lineage is structural and auditable |

**The target state includes:**
- An **Entity Registry** that defines what things mean (Customer, Account, Merchant, CardBIN)
- A **Feature Catalog** with business-language descriptions, ownership, and governance
- **Composite Entity Definitions** that formalize relationships (Customer × Merchant × TimeWindow)
- **Self-service discovery** for non-engineers
- **Self-service decision authoring** with appropriate guardrails
- Features treated as **governed, versioned, auditable data products**
- Decisions that meet production **NFRs** (latency, availability, auditability)

Those users include:
- **Product managers** who need to understand what features exist and what they mean
- **Risk analysts** who need to define rules using features without data science intermediation
- **Fraud operations** who need to author and update detection rules in real-time
- **Rewards strategists** who need to configure offer eligibility and tier logic
- **Compliance / AML teams** who need to define monitoring rules and audit decisions
- **Application developers** who need to consume features in decision applications
- **Data scientists** who need to discover, reuse, and trust features built by others

Today, feature stores serve one persona well: **the feature engineer who built the feature.** Everyone else is locked out.

### What This Is NOT About

This document is **not** about:

- **Physical storage technologies.** S3, DynamoDB, Redis, Parquet — these are solved problems. We're not proposing changes to storage or serving infrastructure.

- **A universal, monolithic enterprise feature store.** We are not advocating for one canonical feature store to rule all domains. Different domains may have different feature stores, and that's fine.

- **Replacing existing feature stores.** Feast, Tecton, Databricks Feature Store, SageMaker Feature Store — these are useful infrastructure. The problem isn't the feature store itself.

### What This IS About

Within any given **scope or domain** for which a feature store is defined:

1. The **primitives are inadequate.** Entities are reduced to row keys. Composites don't exist. Relationships are implicit.

2. The **rightful users are unserved.** Only feature engineers can navigate the feature store. Everyone else waits for them.

3. **Features are inaccessible as products.** They're internal implementation details, not discoverable, governed data assets.

This document articulates the problem and explores directions toward semantic infrastructure that makes features usable as enterprise data products.

---

## 1. The Problem as We Experience It

### 1.1 Features Exist, But Nobody Uses Them

We have a feature store. It contains hundreds of features. Yet:

- **Adoption is limited.** Most teams don't use the feature store at all.
- **Reuse is non-existent.** Features are built for one model and never used again.
- **Engineers are gatekeepers.** You cannot use a feature without talking to the person who built it.
- **Discovery is broken.** Finding relevant features requires Slack, tribal knowledge, or luck.

The feature store is technically functional. It is practically inaccessible.

---

### 1.2 The Language Gap

When a data scientist describes a feature:

> `avg_txn_amt_30d_v2` — float, keyed by `customer_id`, refreshed daily

When a product manager asks:

> "What do we know about customer spending behavior that could help with churn intervention?"

These are the same question. But the feature store cannot bridge them.

**Features are described in technical terms.** Product teams think in business terms. The impedance mismatch blocks adoption.

---

### 1.3 The Composite Entity Disaster

Consider these features:

| Feature | What It Describes |
|---------|-------------------|
| `user_merchant_spend_30d` | A customer's spend at a specific merchant |
| `user_city_txn_count` | A customer's transaction frequency in a city |
| `customer_channel_preference` | A customer's preferred interaction channel |

Each describes a **relationship between entities**, not a single entity.

But in the feature store, the key looks like:

```
cust_123::merch_456
```

Or:

```
user_id_merchant_id_hash
```

**The composite entity is never defined.** It exists only in the engineer's code. Six months later:

- What does `cust_123::merch_456` mean?
- How do I construct this key?
- Is the merchant ID a MID, a name hash, or something else?
- Does null mean "no data" or "no relationship"?

The feature is technically accessible. It is semantically opaque.

---

### 1.4 The Explosion in Fraud and Rewards

#### Core Entities in Banking and Payments

A typical banking/payments domain has hierarchical entity relationships:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                           CORE ENTITY HIERARCHY                             │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│                              ┌──────────┐                                   │
│                              │ Customer │                                   │
│                              └────┬─────┘                                   │
│                                   │                                         │
│                    ┌──────────────┼──────────────┐                          │
│                    │              │              │                          │
│                    ▼              ▼              ▼                          │
│              ┌─────────┐   ┌──────────┐   ┌──────────┐                      │
│              │ Account │   │  Device  │   │ Address  │                      │
│              └────┬────┘   └──────────┘   └──────────┘                      │
│                   │                                                         │
│                   ▼                                                         │
│            ┌─────────────┐                                                  │
│            │ Transaction │                                                  │
│            └──────┬──────┘                                                  │
│                   │                                                         │
│        ┌──────────┼──────────┬──────────┐                                   │
│        ▼          ▼          ▼          ▼                                   │
│   ┌────────┐ ┌────────┐ ┌────────┐ ┌─────────┐                              │
│   │Merchant│ │  MCC   │ │Location│ │ Channel │                              │
│   └────────┘ └────────┘ └────────┘ └─────────┘                              │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

#### Composite Entities in Fraud Detection

Fraud features require reasoning across entity combinations. Each line represents a composite entity:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                     FRAUD DETECTION COMPOSITES                              │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│    ┌──────────┐                                                             │
│    │ Customer │───────────────┬────────────────┬────────────────┐           │
│    └──────────┘               │                │                │           │
│         │                     │                │                │           │
│         │ ×                   │ ×              │ ×              │ ×         │
│         ▼                     ▼                ▼                ▼           │
│    ┌──────────┐         ┌──────────┐     ┌──────────┐     ┌──────────┐      │
│    │ Merchant │         │  Device  │     │ Location │     │   MCC    │      │
│    └──────────┘         └──────────┘     └──────────┘     └──────────┘      │
│         │                     │                │                            │
│         │                     │ ×              │                            │
│         │                     ▼                │                            │
│         │               ┌──────────┐           │                            │
│         │               │ Location │◄──────────┘                            │
│         │               └──────────┘                                        │
│         │                                                                   │
│         │ ×                                                                 │
│         ▼                                                                   │
│    ┌────────────┐                                                           │
│    │ TimeWindow │   (7d, 30d, 90d, lifetime)                                │
│    └────────────┘                                                           │
│                                                                             │
│    Binary Composites:          Ternary Composites:                          │
│    • Customer × Merchant       • Customer × Merchant × TimeWindow           │
│    • Customer × Device         • Customer × MCC × TimeWindow                │
│    • Customer × Location       • Device × Location × TimeWindow             │
│    • Customer × MCC            • Account × Merchant × Channel               │
│    • Device × Location                                                      │
│    • Account × Merchant                                                     │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

#### Adding Rewards: The Complexity Multiplies

Rewards programs introduce a new dimension that cross-cuts the fraud entities:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                       REWARDS PROGRAM COMPOSITES                            │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│    ┌──────────┐         ┌─────────┐         ┌───────┐                       │
│    │ Customer │────×────│ Program │────×────│ Tier  │                       │
│    └──────────┘         └─────────┘         └───────┘                       │
│         │                    │                                              │
│         │ ×                  │ ×                                            │
│         ▼                    ▼                                              │
│    ┌─────────┐          ┌─────────┐                                         │
│    │  Offer  │          │ Partner │                                         │
│    └─────────┘          └─────────┘                                         │
│         │                    │                                              │
│         │ ×                  │ ×                                            │
│         ▼                    ▼                                              │
│    ┌──────────┐         ┌──────────┐                                        │
│    │ Campaign │         │ Category │                                        │
│    └──────────┘         └──────────┘                                        │
│         │                                                                   │
│         │ ×                                                                 │
│         ▼                                                                   │
│    ┌─────────┐                                                              │
│    │ Channel │                                                              │
│    └─────────┘                                                              │
│                                                                             │
│    Binary Composites:          Ternary Composites:                          │
│    • Customer × Program        • Customer × Program × Tier                  │
│    • Customer × Offer          • Customer × Category × Program              │
│    • Customer × Partner        • Customer × Partner × Program               │
│    • Program × Category        • Customer × Offer × TimeWindow              │
│    • Offer × Campaign          • Customer × Campaign × Channel              │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

#### The Combined Picture

When fraud and rewards coexist, the entity graph explodes:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    COMBINED FRAUD + REWARDS ENTITY GRAPH                    │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│                              ┌──────────┐                                   │
│              ┌───────────────│ Customer │───────────────┐                   │
│              │               └────┬─────┘               │                   │
│              │                    │                     │                   │
│    ┌─────────┴─────────┬──────────┼──────────┬─────────┴─────────┐          │
│    │                   │          │          │                   │          │
│    ▼                   ▼          ▼          ▼                   ▼          │
│ ┌───────┐         ┌────────┐ ┌────────┐ ┌────────┐         ┌─────────┐      │
│ │Account│         │ Device │ │Location│ │Merchant│         │ Program │      │
│ └───┬───┘         └────────┘ └────────┘ └───┬────┘         └────┬────┘      │
│     │                  ╲          ╱         │                   │           │
│     │                   ╲        ╱          │                   │           │
│     ▼                    ╲      ╱           ▼                   ▼           │
│ ┌───────────┐             ╲    ╱        ┌───────┐          ┌────────┐       │
│ │Transaction│──────────────╳───────────│  MCC  │          │  Tier  │       │
│ └───────────┘             ╱    ╲        └───────┘          └────────┘       │
│                          ╱      ╲                               │           │
│                         ╱        ╲                              │           │
│                    ┌───────┐  ┌─────────┐                  ┌────────┐       │
│                    │Channel│  │TimeWindow│                 │ Offer  │       │
│                    └───────┘  └─────────┘                  └────────┘       │
│                                                                 │           │
│                                                            ┌────────┐       │
│                                                            │Campaign│       │
│                                                            └────────┘       │
│                                                                             │
│    Every line = potential composite entity                                  │
│    Every composite × TimeWindow = temporal variant                          │
│    Total: 200+ distinct entity-feature anchors                              │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

#### Feature Requirements by Composite

In transaction fraud detection, features must reason across:

| Composite Entity | Purpose |
|------------------|---------|
| Customer × Merchant | Is this a new merchant for the customer? |
| Customer × Location | Is this transaction geographically anomalous? |
| Customer × Device | Is this a trusted device? |
| Customer × MCC | Is this category unusual for the customer? |
| Device × Location | Is the device traveling impossibly fast? |
| Customer × Merchant × TimeWindow | What's the recent spend velocity at this merchant? |

In rewards programs, add:

| Composite Entity | Purpose |
|------------------|---------|
| Customer × Program | Points earned, current tier |
| Customer × Program × Tier | Days until tier expiry, spend to next tier |
| Customer × Offer | Offer eligibility, redemption count |
| Customer × Category × Program | Category-specific earn rates |
| Customer × Partner × Program | Partner affinity |

A mature fraud + rewards system requires:

- **5-10 core entities** (Customer, Account, Transaction, Merchant, Device, Program, Offer, etc.)
- **50+ binary composites** (Customer × Merchant, Account × MCC, etc.)
- **20+ ternary composites** (Customer × Merchant × TimeWindow, etc.)
- **Temporal variants** of each (7d, 30d, 90d, lifetime)

**That's 200+ distinct entity-feature anchors.** Without formal definitions, you get:

- `cust_merch_spend_30d_v2_final_FIXED`
- `customer_merchant_30day_spend`
- `usr_mcht_spend_month`

All describing the same thing. Or not. Who knows.

---

### 1.5 What Is an Entity, and Why Should You Care?

Before proposing solutions, we need to agree on what "entity" means — and why the distinction matters. This section is for the skeptical data engineer who thinks this is "just metadata" and the skeptical product manager who wonders why we're discussing ontology instead of shipping features.

#### The Practical Test

A **dimension** is a value you group by.
An **entity** is a thing that multiple facts reference, and about which you need to know more.

The test:

| Question | If Yes → |
|----------|----------|
| Do multiple transactions/events reference the same value? | Probably an entity |
| Do you need to look up attributes about this value? | Definitely an entity |
| Do you need to aggregate features at this level? | Definitely an entity |
| Is it just a grouping key for a report? | Dimension (for now) |

#### Concrete Example: CardBIN

A CardBIN is the first 6 digits of a card number. It identifies the issuing bank.

**As a dimension:**
```sql
SELECT card_bin, COUNT(*) as txn_count, SUM(is_fraud) as fraud_count
FROM transactions
GROUP BY card_bin
```

You're grouping by CardBIN. It's a column. Nothing more.

**As an entity:**

A fraud analyst asks: "What's the fraud rate for BINs from Russian banks on cards issued by neobanks?"

Now you need:
- `card_bin → issuing_bank`
- `card_bin → country`
- `card_bin → bank_type`

These attributes live in a BIN table (master data). The CardBIN is no longer just a grouping key — it's a **thing with properties**.

**As an entity with features:**

An ML model needs: "What's the historical fraud rate for this BIN?"

Now you need:
- `card_bin → fraud_rate_30d`
- `card_bin → avg_txn_amount`
- `card_bin → velocity_7d`

These are computed features, aggregated at the BIN level. The CardBIN is now a first-class entity in your feature store.

#### Why This Matters to the Data Engineer

If you don't model CardBIN as an entity:

1. **Key chaos.** Different pipelines encode BIN differently (`bin`, `card_bin`, `issuer_bin`, `bin_6`).
2. **Attribute lookup is ad-hoc.** Every team writes their own join to the BIN table.
3. **Features are orphaned.** `bin_fraud_rate_30d` exists, but nobody knows what "bin" means or where to find it.
4. **Lineage is broken.** You can't trace from a model's fraud score back to "because this BIN is from a high-risk country."

If you model CardBIN as an entity:

1. **Canonical key.** `CardBIN.id` is the standard.
2. **Attributes are declared.** `CardBIN.country`, `CardBIN.issuing_bank` — everyone uses the same lookup.
3. **Features are anchored.** `CardBIN.fraud_rate_30d` is discoverable under the CardBIN entity.
4. **Lineage is structural.** Feature → Entity → Attributes → Source.

#### Why This Matters to the Product Manager

If you don't model CardBIN as an entity:

- "Find me all features related to card issuers" → manual search, ask data science, wait.
- "Can we segment by bank type?" → "We'd need to build that join."
- "Why did this transaction get flagged?" → "Let me look at the notebook."

If you model CardBIN as an entity:

- "Find me all features related to card issuers" → browse CardBIN in the catalog.
- "Can we segment by bank type?" → `CardBIN.bank_type` is already defined.
- "Why did this transaction get flagged?" → trace to `CardBIN.fraud_rate_30d` → "this BIN has high fraud."

**The entity model makes the feature store usable by people who aren't feature engineers.**

#### The Same Pattern Repeats

| Value | As Dimension | As Entity (with attributes) | As Entity (with features) |
|-------|--------------|----------------------------|---------------------------|
| CardBIN | Group by BIN | BIN → issuing_bank, country | BIN → fraud_rate, velocity |
| IP Address | Count by IP | IP → geolocation, ISP, VPN flag | IP → reputation_score, login_count |
| City | Sum by city | City → country, timezone, risk_tier | City → avg_spend, fraud_rate |
| MCC | Group by MCC | MCC → category_name, risk_tier | MCC → avg_ticket, dispute_rate |
| Device | Filter by device | Device → type, OS, browser | Device → trust_score, first_seen |

The pattern:
1. You start with a value (dimension).
2. You need attributes → it becomes an entity.
3. You need features → it becomes an entity with features.

**This progression is use-case driven.** What's a dimension today may need to be an entity tomorrow. The semantic layer must support this evolution without re-architecting.

#### What Remains a Scalar?

Not everything becomes an entity. Some values are measurements, not things:

| Scalar | Why It Stays Scalar |
|--------|---------------------|
| Transaction amount | No shared identity; `$47.32` in two transactions is coincidental, not referential |
| Timestamp | A measurement of when, not a thing |
| Boolean flags | A classification, not a thing |
| Counts and ratios | Computed values, not things |

The test: **Do multiple facts point to the same instance of this value?**
- `customer_id = 12345` in 1000 transactions → same customer → entity
- `amount = 47.32` in 1000 transactions → different purchases → scalar

#### The Role of Master Data

When a dimension becomes an entity, its attributes come from **master data**:

| Entity | Master Data Source |
|--------|-------------------|
| CardBIN | BIN table (from card networks) |
| IP Address | IP geolocation database (MaxMind, etc.) |
| MCC | MCC code list (ISO 18245) |
| City | Geographic reference data |
| Device | Device fingerprint database |

Master data is:
- Externally sourced or curated
- Slowly changing
- The source of truth for entity attributes

Features are different:
- Computed from events
- Constantly changing
- Aggregated at the entity level

An entity may have both master data attributes and computed features. The semantic layer must distinguish them.

#### Bottom Line for Skeptics

**To the data engineer:** Entities aren't academic abstractions. They're the reason your feature keys are chaos, your joins are duplicated across teams, and your lineage is broken. Modeling entities explicitly fixes the plumbing.

**To the product manager:** Entities are how you find and understand features without asking data science. "What do we know about this card's issuer?" is a question about an entity. The answer should be browsable, not buried in code.

---

### 1.6 The Entity Type vs. Instance Conflation

There's a deeper confusion in feature stores: the conflation of **entity type** (the abstract definition — "Customer" as a concept with schema, constraints, relationships) and **entity instance** (a specific occurrence — Customer 12345).

Feature stores handle instance-level data well. Type-level semantics — relationships, constraints, governance — have no infrastructure. This isn't just vocabulary confusion; it's a structural gap.

For a detailed analysis of how current feature stores handle (or fail to handle) this distinction, see [Entity Type vs. Instance in Feature Store Systems](./entity-type-vs-instance-analysis.md) — covering Feast, Tecton, SageMaker, Databricks, Hopsworks, and alternative approaches.

---

## 2. The Agentic Future: When AI Becomes the Builder

The problems described so far are today's problems — or yesterday's. Tomorrow brings a more severe challenge.

#### The Shift

| Today | Tomorrow |
|-------|----------|
| Humans build features | AI agents build features |
| Humans do analysis | AI agents do analysis |
| Humans define rules | AI agents suggest and create rules |
| Artifacts are human-authored | Artifacts are agent-generated |

When humans build features, the chaos is at least **traceable to a person** who can explain their work (even if poorly documented). When AI agents become the builders, the stakes change fundamentally.

#### The Risks

**1. Agent-generated artifacts become non-comprehensible.**

An agent creates `txn_velocity_composite_7d_v2_agg`. What is this? No human authored it. No one can explain it. The feature exists, but its meaning is locked in the agent's ephemeral reasoning.

**2. Redundancy explodes.**

Without access to well-organized metadata:
- Agent A creates `customer_spend_30d`
- Agent B creates `cust_avg_txn_amt_month`
- Same feature, different names, no deduplication
- Agents can't know what already exists if there's no queryable catalog

**3. Lineage breaks.**

Agent creates feature → uses in model → produces decision. "Why was this customer flagged?" The answer requires tracing through agent-generated artifacts with no semantic grounding.

**4. Explainability collapses.**

Banking regulators require explainable AI. If the features powering decisions are opaque agent-generated columns, the explanation chain is broken.

#### The Explainability Chain

```
Raw Data → Feature → Model → Decision → Outcome
    │          │        │        │          │
    ▼          ▼        ▼        ▼          ▼
Auditable  Interpretable  Explainable  Documented  Traceable
```

For an auditor, analyst, or product manager to explain a decision, every link must be comprehensible. **If features are opaque, the chain breaks at the second link.**

| Question | What It Requires |
|----------|------------------|
| "What data was used?" | Data lineage |
| "What features were computed?" | Feature definitions with business meaning |
| "What does this feature mean?" | Interpretable feature semantics |
| "What model used this feature?" | Model-feature lineage |
| "Why did the model output this?" | Model explainability |
| "What rule was applied?" | Rule definitions |
| "Who approved this logic?" | Governance trail |

#### What AI Agents Need

For agents to operate without creating chaos, they need the same semantic infrastructure humans need — but agents can't fall back to tribal knowledge.

| Capability | Why Agents Need It |
|------------|-------------------|
| **Queryable Entity Registry** | "What entities exist?" — before creating features |
| **Feature Catalog** | "Does this feature already exist?" — before creating duplicates |
| **Semantic Metadata** | "What does this feature mean?" — to create interpretable features |
| **Relationship Awareness** | "How does Customer relate to Account?" — for valid composites |
| **Governance Constraints** | "Is this PII? What's the retention policy?" — for compliant creation |
| **Artifact Creation Standards** | How to create features with proper metadata — not just values |

#### The Proactive vs. Reactive Choice

| Path | Description | Outcome |
|------|-------------|---------|
| **Proactive** | Build semantic infrastructure now | Agents inherit structure; explainability preserved |
| **Reactive** | Let agents generate artifacts; retrofit later | Chaos; painful remediation; regulatory risk |

Banking cannot afford the reactive path. Unexplainable decisions carry:
- Regulatory penalties
- Audit failures
- Customer harm
- Reputational damage

#### The Compound Problem

| Layer | Today's Problem | Tomorrow's Problem |
|-------|-----------------|-------------------|
| **Entity Semantics** | Entities are key schemas | Agents can't understand entities to build on them |
| **Feature Definitions** | Features lack business meaning | Agent-created features are opaque by default |
| **Relationships** | Not modeled | Agents can't reason about entity relationships |
| **Composites** | Ad-hoc key concatenation | Agents create meaningless composite keys |
| **Governance** | Spreadsheets and wikis | Agent-created features have no governance metadata |
| **Discoverability** | Tribal knowledge | Agents can't discover existing features; create duplicates |
| **Lineage** | Buried in code | Agent work has no traceable lineage |
| **Explainability** | Hard but possible | Impossible without semantic foundation |

**The semantic layer is not optional for the agentic future. It's the foundation for explainable, auditable, agent-assisted decision systems.**

For a detailed analysis of the AI-readiness gap and what's required, see [The AI-Readiness Cliff: Features in the Agentic Era](./ai-readiness-cliff.md).

---

## 3. The Self-Service Imperative: From Data to Decision

Features don't exist in isolation. They power **decisions** — and those decisions are owned by operations teams, not data scientists.

#### The Teams Who Own Decisions

| Team | Decision Types |
|------|---------------|
| **Fraud Operations** | Transaction approval/decline, account blocks, investigation triggers |
| **Credit Risk** | Limit assignments, application approvals, risk-based pricing |
| **Compliance / AML** | SAR filing triggers, transaction monitoring alerts, sanctions screening |
| **Rewards / Loyalty** | Offer eligibility, tier assignments, points calculations |
| **Collections** | Contact strategies, settlement offers, legal escalation |
| **Customer Service** | Escalation triggers, retention offers, case prioritization |

Each of these teams has **domain experts** who understand the business logic better than any data scientist or engineer. A fraud analyst knows what patterns indicate account takeover. A rewards strategist knows what behaviors should trigger a bonus offer.

#### The Current State: Engineering as Gatekeeper

Today, any change to decision logic requires engineering:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                     CURRENT DECISION CHANGE FLOW                            │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│   1. Domain expert identifies need                                          │
│      "We need to flag transactions where velocity exceeds X"                │
│                                                                             │
│   2. Request goes to engineering                                            │
│      JIRA ticket, prioritization, wait in queue                             │
│                                                                             │
│   3. Engineer interprets the request                                        │
│      "What exactly is velocity? Which features? What threshold?"            │
│                                                                             │
│   4. Back-and-forth clarification                                           │
│      Multiple meetings, Slack threads, misunderstandings                    │
│                                                                             │
│   5. Engineer implements                                                    │
│      Writes code, deploys, monitors                                         │
│                                                                             │
│   6. Domain expert validates                                                │
│      "That's not quite what I meant..."                                     │
│                                                                             │
│   7. Iterate (repeat steps 3-6)                                             │
│                                                                             │
│   Timeline: Days to weeks                                                   │
│   Bottleneck: Engineering capacity                                          │
│   Knowledge loss: Domain expertise doesn't transfer to code                 │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

This isn't efficient. More importantly, it isn't scalable. As decision complexity grows, engineering becomes a permanent bottleneck.

#### What Self-Service Means

Self-service doesn't mean "no governance." It means the right people can do the right things without unnecessary intermediation.

| Layer | Self-Service Capability | Who Does It | Guardrails |
|-------|------------------------|-------------|------------|
| **Feature Discovery** | Browse, search, understand available features | Analysts, PMs, domain experts | Read-only access to catalog |
| **Feature Request** | Request new features with business context | Domain experts | Request workflow, prioritization |
| **Rule Authoring** | Define decision rules using available features | Domain experts | Syntax validation, sandbox testing |
| **Rule Testing** | Test rules against historical data | Domain experts | No production impact |
| **Rule Deployment** | Promote tested rules to production | Reviewers/approvers | Approval workflows, staged rollout |
| **Monitoring** | Track decision outcomes, alert on anomalies | Ops teams | Dashboards, alerts |
| **Rollback** | Revert to previous rule version | Ops teams with authority | Audit trail, instant rollback |

#### The Full Pipeline Must Be Addressable

Self-service isn't just about one layer. The **entire pipeline from data to decision** must be accessible with appropriate controls:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                     DATA TO DECISION PIPELINE                               │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│   ┌─────────┐    ┌──────────┐    ┌───────┐    ┌──────────┐    ┌──────────┐  │
│   │  Data   │───▶│ Features │───▶│ Rules │───▶│ Decision │───▶│ Outcome  │  │
│   └─────────┘    └──────────┘    └───────┘    └──────────┘    └──────────┘  │
│        │              │              │              │               │       │
│        ▼              ▼              ▼              ▼               ▼       │
│   ┌─────────┐    ┌──────────┐    ┌───────┐    ┌──────────┐    ┌──────────┐  │
│   │ Lineage │    │ Catalog  │    │ Editor│    │  Engine  │    │ Monitor  │  │
│   └─────────┘    └──────────┘    └───────┘    └──────────┘    └──────────┘  │
│                                                                             │
│   Who can do what at each stage?                                            │
│   What safeguards exist?                                                    │
│   What NFRs must be met?                                                    │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

#### Non-Functional Requirements (NFRs)

Self-service for decisions isn't just about UI. The underlying infrastructure must meet production requirements:

| NFR | Requirement | Why It Matters |
|-----|-------------|----------------|
| **Latency** | Rule evaluation < 50ms (typical), < 10ms (critical) | Real-time transaction decisions can't wait |
| **Availability** | 99.9%+ uptime for decision services | Decisions are on the critical path |
| **Throughput** | Handle peak transaction volumes | Black Friday, month-end, etc. |
| **Consistency** | Same input → same output (for a given rule version) | Auditability, reproducibility |
| **Auditability** | Every decision traceable: inputs, rule version, output | Regulatory requirement |
| **Versioning** | Rules are versioned, with history | Rollback, comparison, audit |
| **Testing** | Sandbox environment for rule testing | Don't break production |
| **Staged Rollout** | Canary, A/B, percentage-based deployment | Limit blast radius |
| **Rollback** | Instant revert to previous version | Recover from mistakes |

#### The Organizational Shift

Self-service changes who does what:

| Role | Before | After |
|------|--------|-------|
| **Domain Expert (Fraud, Risk, etc.)** | Writes requirements, waits for engineering | Authors rules, tests, requests deployment |
| **Data Scientist** | Builds features and models | Builds features and models; domain experts consume |
| **Feature Engineer** | Builds features, supports consumers | Builds features, documents in catalog |
| **Platform Engineer** | Implements decision logic | Maintains self-service platform, guardrails |
| **Reviewer / Approver** | Reviews code PRs | Reviews rule changes in business terms |

The domain expert's time-to-decision shrinks from weeks to hours. The engineer's role shifts from implementation to enablement.

#### The Prerequisite: Semantic Infrastructure

Self-service decision authoring **requires** the semantic infrastructure discussed in this document:

| Capability | Why Self-Service Needs It |
|------------|--------------------------|
| **Entity Registry** | Rule authors need to understand what entities exist (Customer, Account, Transaction) |
| **Feature Catalog** | Rule authors need to discover and understand available features |
| **Business Descriptions** | Rule authors speak business language, not feature column names |
| **Relationships** | Rules often span entities (Customer's Account's recent transactions) |
| **Governance Metadata** | Which features are approved for which decision types? PII constraints? |
| **Lineage** | When a rule fires, trace back to the data that informed it |

**Without the semantic layer, self-service becomes a fiction.** You can give domain experts a rule editor, but if they can't discover or understand the features, they still depend on engineers.

#### The Danger of Skipping to Self-Service

Organizations sometimes jump to "let's build a rule editor" without addressing the foundation:

| What They Build | What Happens |
|-----------------|--------------|
| Rule editor without feature catalog | Users can't find features; ask engineers anyway |
| Rule editor without entity semantics | Users don't understand feature contexts; make mistakes |
| Rule editor without testing | Rules break production; trust evaporates |
| Rule editor without governance | Unapproved rules cause compliance issues |
| Rule editor without lineage | Auditors can't trace decisions; regulatory risk |

**The rule editor is the tip of the iceberg. The semantic and governance infrastructure is the 90% below the waterline.**

#### The Vision

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                     SELF-SERVICE DECISION WORKFLOW                          │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│   1. Domain expert opens decision studio                                    │
│      Sees available entities, features, existing rules                      │
│                                                                             │
│   2. Browses feature catalog                                                │
│      "What do we know about customer velocity?"                             │
│      → Finds: customer_velocity_7d, customer_velocity_30d, ...              │
│      → Reads: "Transaction count in last 7 days for this customer"          │
│                                                                             │
│   3. Authors rule in business terms                                         │
│      IF customer_velocity_7d > 50 AND is_new_merchant = true                │
│         THEN flag_for_review                                                │
│                                                                             │
│   4. Tests against historical data                                          │
│      "How many transactions would this have flagged last month?"            │
│      → Result: 1,247 flags, 89% precision on known fraud                    │
│                                                                             │
│   5. Submits for approval                                                   │
│      Reviewer sees rule in context, approves                                │
│                                                                             │
│   6. Staged rollout                                                         │
│      5% → 25% → 100%, with monitoring at each stage                         │
│                                                                             │
│   7. Production                                                             │
│      Rule is live, decisions are logged, outcomes tracked                   │
│                                                                             │
│   Timeline: Hours, not weeks                                                │
│   Bottleneck: None (domain expert is empowered)                             │
│   Knowledge: Domain expertise is captured in the rule itself                │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

#### What This Requires

| Requirement | Description |
|-------------|-------------|
| **Semantic Layer** | Entity Registry, Feature Catalog, relationships, business descriptions |
| **Rule Language** | Expressive enough for domain needs, simple enough for non-engineers |
| **Testing Infrastructure** | Sandbox execution, historical replay, outcome simulation |
| **Governance Workflows** | Approval chains, role-based access, audit logging |
| **Execution Engine** | Low-latency, high-availability rule evaluation |
| **Monitoring** | Decision dashboards, anomaly detection, outcome tracking |
| **Versioning** | Rule history, comparison, rollback |

**Self-service from data to decision is the end goal. The semantic layer for features is the first step.**

---

## 4. The Current Landscape

### 4.1 Why Feature Stores Look This Way

Feature stores emerged to solve ML engineering problems — training–serving skew, freshness, online/offline parity, scalable materialization. They were built from a data engineering worldview:

> A feature is a column in a table, keyed by an ID.

They were **not** built from domain-driven design, enterprise entity modeling, or semantic systems. As a result:

- **The entity disappears into the primary key.** In most feature stores, `customer` is a key resolution mechanism, not a defined concept with relationships and constraints.
- **Composite entities don't exist.** A key like `customer_id::merchant_id` is constructed in code with no formal definition, schema, or discoverability.

### 4.2 What Feature Stores Solve (and Don't)

| Solved | Not Solved |
|--------|------------|
| Storage (S3, DynamoDB, Redis) | Entity semantics (entities are implicit row keys) |
| Low-latency serving | Relationships (no modeling of Customer → Account) |
| Materialization pipelines | Composite entities (no formal definition) |
| Online/offline parity | Business language (features are columns, not properties) |
| Distributed scale | Discovery (search by column name, not by entity) |
| | Governance (ownership and lineage require external tooling) |

> Feature stores solve **how to serve features**, but not **what those features mean**.

### 4.3 What Exists Today

| Category | Systems | Strengths | Limitations |
|----------|---------|-----------|-------------|
| **Feature Stores** | Tecton, Hopsworks, Feast, Databricks | Storage, serving, some entity support | Tecton: proprietary. Feast: primitive entity model. |
| **Data Catalogs** | DataHub, Atlan, Alation, Apache Atlas | Entity modeling, lineage | Not ML-native, requires integration |
| **Semantic Layers** | dbt Semantic Layer | Entities, dimensions, measures | BI-focused, not ML-focused |

**The gap:** No open-source, ML-native, entity-first feature catalog exists. Tecton and Hopsworks come closest but are proprietary or niche. DataHub has entity modeling but isn't feature-native. Feast is open-source but entity semantics are weak.

---

## 5. Solution Direction

### 5.1 Augment, Don't Replace

The feature store infrastructure is not the problem. The missing semantic layer is.

**Do not replace the feature store. Add the missing metadata layer.**

### 5.2 Separate Responsibilities

| Concern | Owner |
|---------|-------|
| Physical storage & serving | Feature Store (S3, DynamoDB, Redis) |
| Feature computation & materialization | ETL / streaming pipelines |
| Entity semantics & relationships | **Entity Registry** (new) |
| Feature meaning, ownership, constraints | **Feature Catalog** (new) |

### 5.3 Introduce an Entity Registry

A lightweight registry that captures:

```yaml
entity:
  name: Customer
  description: "An individual or business with an account relationship"
  primary_key: customer_id
  key_type: string
  relationships:
    - target: Account
      type: one-to-many
      description: "A customer may have multiple accounts"
    - target: Device
      type: many-to-many
      description: "A customer may use multiple devices"
```

### 5.4 Define Composite Entities Explicitly

```yaml
composite_entity:
  name: CustomerMerchantRelationship
  description: "A customer's transactional relationship with a specific merchant"
  constituents:
    - entity: Customer
      role: subject
    - entity: Merchant
      role: object
  key_schema:
    - customer_id: string
    - merchant_id: string
  relationship_type: many-to-many
  materialization: explicit
```

Now the composite is **defined, discoverable, and consumable**.

### 5.5 Anchor Features to Entities

```yaml
feature:
  name: spend_velocity_30d
  entity: CustomerMerchantRelationship
  description: "Average daily spend by this customer at this merchant over 30 days"
  business_domain: Behavioral Risk
  owner: risk-features-team
  granularity: daily
  freshness: T+1
  pii_derived: false
```

The feature explicitly declares:

- Which entity it describes
- What it means in business terms
- Who owns it
- Whether it touches sensitive data

### 5.6 Enable Business-Language Discovery

Instead of searching for `avg_txn_amt_30d`, product teams can:

- Browse by entity: "What features exist for Customer?"
- Browse by domain: "What features exist for Behavioral Risk?"
- Search by concept: "customer spending velocity"

**Features become accessible to people who aren't feature engineers.**

### 5.7 Keep the Feature Store Lean

Continue to use:

- S3 + columnar formats for offline features
- DynamoDB / Redis for online features
- Existing feature store tools

But treat them as **execution substrates**, not semantic authorities.

---

## 6. End State

The semantic layer transforms features from internal implementation details to enterprise data products:

- **Entities** become defined concepts with relationships, not just row keys
- **Composites** become first-class definitions, not ad-hoc key concatenations
- **Features** become discoverable, understandable, and reusable by their rightful users
- **Lineage** becomes structural and auditable, not buried in code
- **Domain experts** can discover, understand, and use features without engineering intermediation
- **Decisions** become self-serviceable with appropriate governance

---

## 7. Open Questions

1. **Build vs. integrate?** Should we build a custom Entity Registry, or integrate with DataHub / similar?
2. **Substrate first?** Which feature store(s) do we wrap first? (Feast? Custom? Databricks?)
3. **Bootstrap strategy?** How do we populate entity definitions and feature metadata? (Manual? LLM-assisted? Inferred?)
4. **Internal first?** Do we validate internally before considering this as a product?
5. **Connection to agents?** Can this semantic layer power agentic systems (Ibuki, Quark) that need to reason about features?

For a comprehensive list of deliberation points across all aspects (features, entities, decisions, governance, self-service prerequisites), see [Questions on Features and Decisions](./questions-on-features-and-decisions.md).

---

## 8. Recommended Next Steps

| Step | Description | Owner |
|------|-------------|-------|
| **1. Align on scope** | Semantic layer only, or full decision stack? What's Phase 1? | Leadership |
| **2. Identify internal pilot** | Which team, which use case validates the approach? | Product + Engineering |
| **3. Evaluate existing solutions** | Tecton, Hopsworks, DataHub + Feast — build vs. integrate? | Architecture |
| **4. Draft entity model schema** | Core entities, relationships, composite definitions for pilot domain | Data Architecture |
| **5. Prototype discovery experience** | What does self-service look like for a product manager? | Product |

---
