# Scenario-Oriented Thinking: Examples

> **Status**: 🟢 Design Complete  
> **Target Audience**: All (APOs, PAs, Developers)  
> **Purpose**: Concrete use cases illustrating scenario-oriented thinking

---

## Example 1: Dispute Resolution Domain

### Domain Overview

**Domain:** Dispute Resolution  
**Business Context:** Financial services organization handling customer disputes on transactions

### Scenarios

#### Scenario: Standard Dispute

**Situation:** Routine dispute case with clear rules and automated decision capability.

**Signal:** `dispute-filed` with `amount < $1000`

**Normative Specification:**
```yaml
scenario: standard-dispute
normative:
  roles:
    - dispute-analyst
    - supervisor (escalation only)
  goals:
    - Resolve within 24 hours
    - Document decision with rationale
  decision_criteria:
    - Amount < $1000: Auto-approve if merchant history clean
    - Amount >= $1000: Analyst review required
  escalation:
    - If unresolved after 20h: Escalate to supervisor
```

**Automation Specification:**
```yaml
scenario: standard-dispute
automation:
  application: dispute-handler
  runtime: chronoshift  # Long-running case management
  triggers:
    - signal_type: dispute-filed
      conditions:
        amount: { lt: 1000 }  # Routes to this scenario
  tools:
    - core-banking
    - merchant-gateway
    - notification-service
```

**Deployment Specification:**
```yaml
scenario: standard-dispute
deployment:
  task_queue: dispute-analyst-queue
  sla:
    response_time: 4h
    resolution_time: 24h
  agents:
    - dispute-analyst-team
    - dispute-ai-assistant (support role)
  activation:
    enabled: true
    rollout_percentage: 100
```

#### Scenario: High-Value Dispute

**Situation:** Dispute involving significant amount, requiring analyst review and evidence gathering.

**Signal:** `dispute-filed` with `amount >= $1000`

**Key Differences from Standard Dispute:**
- Different roles (senior analyst, compliance officer)
- Different goals (48-hour resolution, regulatory documentation)
- Different automation (human-in-the-loop workflow)
- Different deployment (senior analyst queue, higher SLA)

#### Scenario: Fraud Dispute

**Situation:** Dispute flagged for potential fraud, requiring security team involvement.

**Signal:** `dispute-filed` with `fraud-indicator: true`

**Key Differences:**
- Different roles (security analyst, fraud investigator)
- Different goals (investigation, regulatory reporting)
- Different automation (investigation workflow, evidence collection)
- Different deployment (security queue, extended SLA)

### Why These Are Separate Scenarios

These represent **fundamentally different situations**:
- Different roles and responsibilities
- Different compliance requirements
- Different SLAs and goals
- Different signals (amount threshold, fraud indicator)

**Note:** Decision rules within Standard Dispute (e.g., "auto-approve if merchant history clean") are NOT separate scenarios — they're rules within the scenario's normative specification.

---

## Example 2: Payment Processing Domain

### Domain Overview

**Domain:** Payment Processing  
**Business Context:** Financial services organization processing various types of payments

### Scenarios

#### Scenario: Domestic Payment

**Situation:** Standard domestic payment within the same country.

**Signal:** `payment-request` with `origin_country == destination_country`

**Key Characteristics:**
- Standard compliance requirements
- Fast processing (real-time or near-real-time)
- Automated approval for low-risk transactions

#### Scenario: International Transfer

**Situation:** Cross-border payment requiring additional compliance checks.

**Signal:** `payment-request` with `origin_country != destination_country`

**Key Differences:**
- Additional compliance checks (AML, sanctions screening)
- Different processing time (may require manual review)
- Different roles (compliance officer, international payments specialist)
- Different regulatory requirements

#### Scenario: High-Risk Payment

**Situation:** Payment flagged as high-risk based on amount, destination, or customer profile.

**Signal:** `payment-request` with `risk_score > threshold` OR `amount > threshold`

**Key Differences:**
- Enhanced due diligence required
- Manual review mandatory
- Different roles (risk analyst, compliance officer)
- Extended processing time

### Why These Are Separate Scenarios

These represent **fundamentally different situations**:
- Different compliance requirements (domestic vs. international)
- Different risk profiles (standard vs. high-risk)
- Different signals (country match, risk score)
- Different roles and approval workflows

---

## Example 3: Customer Onboarding Domain

### Domain Overview

**Domain:** Customer Onboarding  
**Business Context:** Financial services organization onboarding new customers

### Scenarios

#### Scenario: Individual Account Onboarding

**Situation:** Standard individual customer account opening.

**Signal:** `onboarding-request` with `customer_type == individual`

**Key Characteristics:**
- Standard KYC verification
- Document collection (ID, proof of address)
- Automated verification where possible
- Standard approval workflow

#### Scenario: Business Account Onboarding

**Situation:** Business entity account opening requiring additional verification.

**Signal:** `onboarding-request` with `customer_type == business`

**Key Differences:**
- Additional documentation (business registration, ownership structure)
- Different roles (business onboarding specialist, compliance officer)
- Enhanced due diligence (UBO verification)
- Different approval workflow (may require multiple approvers)

#### Scenario: Regulated Entity Onboarding

**Situation:** Onboarding of regulated entity (e.g., financial institution) with strict compliance requirements.

**Signal:** `onboarding-request` with `entity_type == regulated`

**Key Differences:**
- Extensive documentation requirements
- Regulatory approval may be required
- Different roles (regulatory specialist, legal counsel)
- Extended onboarding timeline
- Different compliance checks

### Why These Are Separate Scenarios

These represent **fundamentally different situations**:
- Different verification requirements (individual vs. business vs. regulated)
- Different documentation needs
- Different roles and expertise required
- Different compliance contexts
- Different signals (customer type, entity type)

---

## Example 4: Customer Support Domain

### Domain Overview

**Domain:** Customer Support  
**Business Context:** Organization providing customer support across multiple channels

### Scenarios

#### Scenario: Simple Inquiry

**Situation:** Routine customer question that can be answered directly.

**Signal:** `support-request` with `complexity == low` AND `type == inquiry`

**Key Characteristics:**
- Automated response possible (chatbot, knowledge base)
- Fast resolution (minutes)
- Standard support agent can handle
- No escalation required

#### Scenario: Technical Issue

**Situation:** Technical problem requiring investigation and resolution.

**Signal:** `support-request` with `type == technical-issue`

**Key Differences:**
- Technical expertise required
- Investigation workflow
- Different roles (technical support specialist, engineering team)
- Extended resolution time
- May require escalation to engineering

#### Scenario: Formal Complaint

**Situation:** Formal customer complaint requiring structured handling and documentation.

**Signal:** `support-request` with `type == complaint` OR `severity == high`

**Key Differences:**
- Structured complaint handling process
- Regulatory documentation required
- Different roles (complaint handler, supervisor, compliance)
- Extended resolution time
- Escalation matrix required
- Customer communication protocol

### Why These Are Separate Scenarios

These represent **fundamentally different situations**:
- Different nature of problem (inquiry vs. technical vs. complaint)
- Different expertise required
- Different compliance requirements (complaints require regulatory handling)
- Different signals (complexity, type, severity)
- Different goals and SLAs

---

## Common Patterns Across Examples

### Pattern 1: Signal-Based Routing

All examples show how **signals** route to the appropriate scenario:
- Dispute: Amount threshold, fraud indicator
- Payment: Country match, risk score
- Onboarding: Customer type, entity type
- Support: Complexity, type, severity

### Pattern 2: Distinct Situations

Each scenario represents a **fundamentally different situation** that business stakeholders recognize:
- Different roles required
- Different goals and SLAs
- Different compliance requirements
- Different handling approaches

### Pattern 3: Three Specifications

Each scenario has three complementary specifications:
- **Normative:** What should happen (roles, goals, rules)
- **Automation:** How it's automated (application, runtime, triggers)
- **Deployment:** How it's operated (queues, agents, SLAs)

### Pattern 4: Decision Rules Within Scenarios

Decision rules (e.g., "auto-approve if merchant history clean") belong **within** a scenario's normative specification, not as separate scenarios.

---

## Related Documentation

- [Entry Point](./scenario-oriented-thinking.md) — Overview and reading guide
- [Core Concepts](./scenario-oriented-thinking-core.md) — Foundations and specifications
- [The Core Argument](./scenario-oriented-thinking-argument.md) — Why this matters
- [Adoption Guide](./scenario-oriented-thinking-adoption.md) — How to get started

---

[← Back to Entry Point](./scenario-oriented-thinking.md)
