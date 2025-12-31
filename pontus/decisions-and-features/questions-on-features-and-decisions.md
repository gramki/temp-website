# Questions on Features and Decisions

## Deliberation Points for Semantic Feature Infrastructure

---

## 1. Scope and Boundaries

### 1.1 What Problem Are We Solving First?

- Is the immediate problem **feature discoverability and reuse** (semantic layer)?
- Or is it **domain expert empowerment** (full decision stack)?
- Can we solve one without the other?

### 1.2 Where Does the Semantic Layer End?

| Component | In Scope? | Notes |
|-----------|-----------|-------|
| Entity Registry | ? | Core entities, relationships |
| Composite Entity Definitions | ? | User-defined and system-defined |
| Feature Catalog | ? | Business-language metadata |
| Rules Engine | ? | Production decision logic |
| Decision Service | ? | Runtime execution |
| ML Model Registry | ? | Models that consume features |
| Outcome Tracking | ? | Feedback loop for learning |

### 1.3 Build vs. Integrate

- Should we build a custom semantic layer?
- Or integrate existing components (DataHub + Feast + rules engine)?
- What's the differentiation if we build?

---

## 2. Entity Model Design

### 2.1 Core vs. Analytical Entities

| Question | Considerations |
|----------|----------------|
| What distinguishes a core entity from an analytical entity? | Core = system-of-record, stable. Analytical = derived, fluid. |
| Can analytical entities be promoted to core? | Lifecycle management |
| Who owns the distinction? | Governance model |

### 2.2 User-Defined Entities

- **Who can define entities?** Data scientists only? Domain experts? Anyone?
- **What's the approval process?** None for exploration? Review for production?
- **How do we prevent sprawl?** 50 variants of "value bucket" is chaos
- **What's the canonical definition process?** Aliases? Versioning?

### 2.3 Derived Entities

Some entities don't exist in source data but are derived:

| Entity | Derivation |
|--------|------------|
| CardBIN | `Transaction.card_number[0:6]` |
| MerchantCountry | `Merchant.address.country` or `Transaction.geo.country` |
| PaymentValueBucket | `CASE WHEN amount < 50 THEN 'small' ... END` |
| RiskTier | `CASE WHEN fraud_score > 0.8 THEN 'high' ... END` |

- **Where is the derivation logic stored?** Entity definition? Separate transform layer?
- **Is derivation computed on-demand or pre-materialized?**
- **How do we handle derivation ambiguity?** (MerchantCountry from merchant vs. transaction)

### 2.4 Entity Relationships

- **What relationship types do we support?** One-to-many, many-to-many, hierarchical?
- **Are relationships directional?** Customer → Account vs. Account → Customer
- **Can relationships have attributes?** (e.g., Customer-Account with role: primary/secondary)

---

## 3. Composite Entities

### 3.1 Definition and Semantics

- **What is a composite entity, formally?** Tuple of entities? Relationship? Join key?
- **How do we express ternary+ composites?** Customer × Merchant × TimeWindow
- **Are temporal dimensions (TimeWindow) first-class entities?** Or a special case?

### 3.2 Key Construction

- **How are composite keys constructed?** Concatenation? Hash? Structured key?
- **Is the key schema declared or inferred?**
- **How do we handle null constituents?** (Customer with no Merchant relationship)

### 3.3 Composite Lifecycle

- **Can users create composites on-demand?** Or must they be pre-registered?
- **Are composites materialized or virtual?** Performance vs. flexibility
- **When does an ad-hoc composite become a formal definition?**

---

## 4. Features and Business Logic

### 4.1 Feature Ownership

- **Who defines features?** Data scientists? Domain experts? Both?
- **Who owns production features?** Engineering? Data science? Business?
- **What's the handoff from exploration to production?**

### 4.2 Feature vs. Rule

| Concept | Definition | Owner |
|---------|------------|-------|
| Feature | A property of an entity (e.g., `fraud_score`) | Data science |
| Rule | A decision condition over features (e.g., `IF fraud_score > 0.8 THEN decline`) | Domain expert |

- **Is this distinction useful?** Or should rules and features be unified?
- **Can a rule output become a feature input?** (e.g., `was_declined_24h`)

### 4.3 Domain Expert Authoring

- **What language do domain experts use to define rules?**
  - SQL-like? Natural language? Visual builder? DSL?
- **How do we validate rules before production?**
- **How do we version and audit rule changes?**

---

## 5. Technical Architecture

### 5.1 Substrate

- **Which feature store(s) do we wrap?** Feast? Databricks? Custom? Multiple?
- **Do we support multiple substrates simultaneously?**
- **What's the abstraction boundary?** (Semantic layer shouldn't know about DynamoDB)

### 5.2 Compute Model

| Mode | Use Case | Tradeoffs |
|------|----------|-----------|
| Pre-materialized | Production serving, low latency | Storage cost, staleness |
| Virtual / on-demand | Exploration, ad-hoc analysis | Compute cost, latency |
| Hybrid | Materialized for hot paths, virtual for long tail | Complexity |

- **Which mode(s) do we support?**
- **How do we decide what to materialize?**

### 5.3 Integration Points

- **How does the semantic layer integrate with:**
  - Feature store (Feast, Databricks, etc.)
  - Data catalog (DataHub, etc.)
  - Rules engine (if separate)
  - ML platform (model registry, training pipelines)
  - Decision service (runtime execution)
  - BI tools (for analysis)

### 5.4 API Design

- **What does the API look like for:**
  - Defining an entity?
  - Defining a composite?
  - Defining a feature?
  - Querying features by entity?
  - Discovering features by business domain?

---

## 6. Governance and Compliance

### 6.1 Lineage

- **What lineage do we track?**
  - Feature → source data
  - Feature → upstream features
  - Rule → features used
  - Model → features used
  - Decision → rule applied

- **Is lineage structural (declared) or inferred (observed)?**

### 6.2 Ownership

- **How do we assign ownership to:**
  - Core entities?
  - Analytical entities?
  - Features?
  - Rules?
  - Composites?

### 6.3 PII and Sensitivity

- **How do we track which features derive from PII?**
- **Is sensitivity inherited?** (Feature on Customer inherits Customer's sensitivity?)
- **What enforcement mechanisms exist?**

### 6.4 Audit and Change Control

- **What changes require approval?**
  - Core entity changes: always?
  - Feature changes: depends on production usage?
  - Rule changes: always for production rules?

---

## 7. Connection to ML and AI

### 7.1 ML Model Consumption

- **How do ML models consume features?**
  - By entity and feature name?
  - By composite and feature name?
  - By semantic query ("customer risk features")?

### 7.2 Training vs. Serving

- **Does the semantic layer provide point-in-time-correct features for training?**
- **How do we ensure training/serving consistency at the semantic level?**

### 7.3 AI Augmentation

- **Can AI/LLM systems:**
  - Discover features via natural language?
  - Suggest entity definitions based on data?
  - Recommend rules based on outcomes?
  - Detect entity/feature drift?

---

## 8. Connection to Agentic Systems

### 8.1 Agents and Features

- **Can agents query the feature catalog?** ("What features exist for this customer?")
- **Can agents request feature computation?** ("Compute fraud_score for this transaction")
- **Can agents invoke rules?** ("Apply fraud decision logic to this transaction")

### 8.2 Agents and Entity Understanding

- **Do agents need to understand entity semantics?**
  - To reason about relationships (Customer → Account → Transaction)
  - To navigate composites (Customer × Merchant)
  - To interpret feature meaning

### 8.3 Connection to Ibuki / Quark

- **Is this semantic layer the "feature substrate" for Ibuki agents?**
- **Is Quark the "decision execution" layer that consumes rules?**
- **How do they connect?**

---

## 9. Product and Market

### 9.1 Internal Validation

- **What internal use case validates the approach?**
- **What's the success metric?** (Feature reuse rate? Time to feature discovery? Rule deployment time?)
- **Who are the internal champions?**

### 9.2 External Product

- **Is this a standalone product or an enabler for other products?**
- **Who is the buyer?** ML platform team? CDO? Risk/fraud team?
- **What's the pricing model?** Per entity? Per feature? Per decision?

### 9.3 Competitive Positioning

- **How do we position against:**
  - Tecton (proprietary, strong entity model)
  - Feast + DataHub (open, requires integration)
  - dbt Semantic Layer (BI-focused)
  - Vertical SaaS (Featurespace, Feedzai for fraud)

---

## 10. Prioritization

### 10.1 What Must Be True for Phase 1?

| Capability | Must Have | Nice to Have | Later |
|------------|-----------|--------------|-------|
| Core entity registry | | | |
| Composite entity support | | | |
| User-defined entities | | | |
| Feature catalog with business language | | | |
| Self-service discovery UI | | | |
| Rules authoring by domain experts | | | |
| Production rules execution | | | |
| ML model integration | | | |
| AI/agent integration | | | |

### 10.2 What Can We Defer?

- Virtual/on-demand compute?
- Multi-substrate support?
- Full governance/audit trail?
- AI-assisted entity discovery?

---

---

## 11. Deferred Branches (To Discuss Later)

These topics emerged in discussion but are being deferred to maintain focus on the feature engineering problem first.

### 11.1 Domain Experts as Rule Authors

The insight that domain experts (fraud analysts, rewards PMs) should define operational rules — not just consume features — expands the scope significantly.

**Key points to revisit:**
- Fraud and rewards rules are best articulated by domain experts, not data scientists
- The decision lifecycle: Analysis → Hypothesis → Rule → Production → Outcomes → ML/AI refinement
- Rules use entities and features, but rule authoring is a separate capability from feature engineering
- This connects features to operational decisions, not just ML models

**Implication:** The semantic layer may need to extend beyond feature catalog to include rule definitions. But this is a larger scope.

### 11.2 User-Defined / Analytical Entities

Domain experts need to define entities that don't exist in the initial model:
- CardBIN (derived from card number)
- MerchantCountry (derived from merchant or transaction data)
- PaymentValueBucket (business-defined ranges)

**Key questions:**
- Should entity definition be self-service for domain experts?
- How do we distinguish core entities (stable, governed) from analytical entities (fluid, exploratory)?
- How do we prevent entity sprawl while enabling flexibility?

**Implication:** This is essential for full empowerment but may be Phase 2 after core entity registry is established.

### 11.3 Full Decision Stack

The complete architecture includes layers beyond feature engineering:

```
Domain Expert Layer → defines entities, rules, features
         ↓
Semantic Layer → entity registry, feature catalog
         ↓
Execution Layer → feature store, rules engine, decision service
         ↓
Learning Layer → ML models, outcome tracking, AI augmentation
```

**Implication:** Feature engineering is one layer. The full stack requires additional components. Defer full stack design until feature layer is validated.

### 11.4 Agentic System Integration

Can agents (Ibuki, Quark) consume the semantic layer?
- Query feature catalog
- Request feature computation
- Invoke decision logic

**Implication:** This is a consumption pattern, not a feature engineering concern. Defer until semantic layer API is defined.

---

## 12. Self-Service Decisions: Prerequisites by Aspect

For operations teams (Fraud, Credit Risk, Compliance/AML, Rewards, Collections, Customer Service) to self-service decisions from data to production, the following aspects must be addressed.

---

### 12.1 Feature Discovery & Understanding

- Can domain experts discover features without asking data science?
- Is there a browsable catalog with business-language descriptions?
- Can they search by business concept, not just column name?
- Can they see example values and distributions?
- Can they understand feature freshness and update frequency?
- Can they see which features are approved for their use case?
- Can they see feature quality metrics (coverage, drift)?

---

### 12.2 Entity & Relationship Understanding

- Can domain experts see what entities exist (Customer, Account, Merchant, etc.)?
- Can they understand relationships between entities?
- Can they navigate from one entity to related entities?
- Can they understand composite entities (Customer × Merchant)?
- Can they see which features are available for each entity?
- Is entity documentation accessible without technical background?

---

### 12.3 Rule Language & Authoring

- What language do domain experts use to author rules?
- Is it visual, text-based, or both?
- What level of expressiveness is needed? (Boolean? Arithmetic? Lookups? Loops?)
- Can they reference features by business name?
- Can they reference relationships (e.g., "customer's account's balance")?
- Can they express temporal conditions (e.g., "in the last 7 days")?
- Can they express aggregations (e.g., "count of transactions where...")?
- Is the language learnable without engineering background?
- Is there syntax validation and error guidance?
- Can they save drafts and iterate?

---

### 12.4 Testing Infrastructure

- Can domain experts test rules before production?
- Can they run rules against historical data?
- Can they see how many cases would be affected?
- Can they compare new rule behavior vs. current rule behavior?
- Can they see false positive / false negative estimates?
- Can they test on synthetic data if real data is restricted?
- Is testing isolated from production (sandbox)?
- Can they test with specific scenarios (edge cases)?
- Can they share test results with reviewers?

---

### 12.5 Deployment & Rollout

- How do rules get from test to production?
- Is there a staging environment?
- Can rules be deployed with percentage-based rollout (canary)?
- Can rules be A/B tested against alternatives?
- What's the latency from "approve" to "live"?
- Who has authority to deploy?
- Is deployment auditable (who deployed what, when)?
- Can deployment be scheduled (e.g., start Monday 9am)?

---

### 12.6 Governance & Approvals

- What changes require approval?
- Who can approve (by role, by domain, by risk level)?
- Is there a multi-level approval for high-risk changes?
- How are approvals documented?
- Can approvers see the full context (rule, test results, impact)?
- Is there an escalation path for urgent changes?
- How are approval workflows configured?
- Can governance requirements vary by team or rule type?

---

### 12.7 Monitoring & Observability

- Can domain experts see rule performance in production?
- Are there dashboards for decision volume, outcomes, latency?
- Can they see drift in rule firing rates?
- Are there alerts for anomalies (e.g., rule suddenly firing 10x more)?
- Can they correlate decisions with downstream outcomes?
- Can they see feature values at decision time (for debugging)?
- Is monitoring self-service or does it require engineering?

---

### 12.8 Rollback & Recovery

- Can a rule be rolled back instantly?
- Who has authority to rollback?
- Is rollback auditable?
- Can they rollback to any previous version, or just the last one?
- What's the latency from "rollback" to "effective"?
- Is there an automatic rollback trigger (e.g., if error rate spikes)?
- How is rollback communicated to downstream systems?

---

### 12.9 Version Control & History

- Are all rule versions preserved?
- Can domain experts see the history of changes?
- Can they compare two versions side-by-side?
- Can they see who changed what, when, and why?
- Can they restore a previous version without rollback (promote old version)?
- Is version history searchable?
- How long is history retained?

---

### 12.10 Training & Onboarding

- How do new domain experts learn the system?
- Is there documentation, tutorials, or training materials?
- Is there a sandbox for learning without production risk?
- Is there a community or support channel for questions?
- Are there templates or examples for common rule patterns?
- Is there role-specific onboarding (Fraud vs. Rewards vs. Compliance)?

---

### 12.11 Non-Functional Requirements (NFRs)

- What latency SLA must rule evaluation meet?
- What availability SLA must the decision service meet?
- What throughput must be supported (peak TPS)?
- Is there a consistency guarantee (same input → same output for a given rule version)?
- How are NFRs monitored and alerted?
- What happens if NFRs are breached (degradation, fallback)?
- Are NFR guarantees visible to domain experts or only to engineering?

---

### 12.12 Audit & Compliance

- Can every decision be traced to its inputs, rule version, and output?
- Is the audit trail immutable?
- Can auditors query decisions by time, rule, entity, outcome?
- Can auditors see feature values at decision time?
- Can auditors see who approved the rule?
- Is the audit trail exportable for regulatory review?
- How long is the audit trail retained?
- Does the system meet regulatory requirements (SR 11-7, ECOA, GDPR, CCPA, etc.)?

---

### 12.13 Integration with Existing Systems

- How does self-service integrate with existing decision systems?
- Can rules call external services or APIs?
- Can rules be consumed by existing applications?
- How is the transition from legacy rules to new rules managed?
- Is there a migration path for existing rules?
- How are dependencies between rules and features managed?
- Can the system integrate with existing identity/access management (SSO, RBAC)?

---

### 12.14 Data Freshness & Consistency

- How fresh are the features at decision time?
- Is freshness visible to rule authors?
- What happens if a feature is stale (error, fallback, proceed)?
- Is there consistency between features used in training vs. serving?
- Can domain experts see when features were last updated?
- Are there SLAs for feature freshness?

---

### 12.15 Access Control & Permissions

- Who can view rules (by team, by domain)?
- Who can author rules (by team, by domain)?
- Who can approve rules (by role, by risk level)?
- Who can deploy rules (by authority level)?
- Who can rollback rules (by authority level)?
- Who can view audit trails (by role)?
- Is access control integrated with corporate identity systems?
- Can permissions be delegated or inherited?

---

### 12.16 Feedback & Outcome Tracking

- Can domain experts see outcomes of decisions (fraud confirmed, customer retained, etc.)?
- Is outcome data linked back to the decision that was made?
- Can outcomes inform rule refinement (feedback loop)?
- Is outcome tracking automated or manual?
- Can outcomes be used for model training?
- Are outcome metrics visible in dashboards?
- How long does it take for outcomes to be visible?

---

### 12.17 Cross-Team Coordination

- How do multiple teams share entities and features?
- How are conflicts resolved (e.g., two teams want different definitions of "high risk")?
- Is there a central governance body or is it federated?
- Can one team's rule depend on another team's rule output?
- How are dependencies tracked and communicated?
- Is there visibility into cross-team usage of shared artifacts?

---

### 12.18 Edge Cases & Exceptions

- How are exceptions handled (customer escalation overrides rule)?
- Can domain experts define exception paths?
- Are exceptions auditable?
- Can rules handle missing or null feature values?
- Can rules handle unexpected values (out of range, new category)?
- What happens if the decision service is unavailable (fallback)?

---

### 12.19 Performance & Cost Visibility

- Can domain experts see the cost of their rules (compute, storage)?
- Are there guardrails to prevent expensive rules?
- Is rule complexity visible (e.g., this rule evaluates 50 features)?
- Can they see latency contribution of their rules?
- Is there a budget or quota per team?

---

### 12.20 AI/Agent Assistance

- Can AI suggest rules based on data patterns?
- Can AI explain why a rule fired?
- Can AI detect rule conflicts or redundancies?
- Can AI suggest feature improvements?
- Can agents invoke rules on behalf of users?
- Can agents be constrained by the same governance as humans?

---

## Next Steps

1. **Align on scope** — Semantic layer only, or full decision stack?
2. **Identify internal pilot** — Which team, which use case?
3. **Evaluate existing solutions** — Tecton, Hopsworks, DataHub integration
4. **Draft entity model schema** — For core, analytical, and composite entities
5. **Prototype discovery experience** — What does self-service look like?
6. **Map prerequisites by team** — Which aspects matter most to which ops team?
7. **Identify blockers** — Which prerequisites are hardest to satisfy?

---

