# 8. Platform Components & Design Rationale

---

This section details **each major component** of the Zeta Agent Platform. For each component:

- **Requirements** — What the platform must provide
- **Why It Matters** — Regulatory, operational, and strategic drivers
- **Solution Approach** — How Zeta addresses these requirements
- **Portability Approach** — How we avoid CSP lock-in

---

## 8.1 Agent Definition & Lifecycle Service

### Requirements

The platform must manage agents as **versioned, deployable products** with full lifecycle control.

| Requirement | Description |
|-------------|-------------|
| **Agent Schema** | Define agent structure: identity, capabilities, constraints, configuration |
| **Version Management** | Semantic versioning (major.minor.patch) with change tracking |
| **Multi-Stage Lifecycle** | Support distinct stages: definition → training → employment |
| **Training Immutability** | Guardrails and constraints defined at training cannot be relaxed at employment |
| **Deployment Orchestration** | Deploy agents to target environments (dev, staging, prod) |
| **Promotion Workflows** | Controlled progression with approval gates |
| **Rollback** | Instant reversion to previous version with state consistency |
| **Retirement** | Graceful end-of-life with deprecation warnings |
| **Registry** | Central catalog of all agents and versions |

### Why It Matters

| Driver | Requirement Source |
|--------|-------------------|
| **Regulatory** | Banks require change management processes for all production software (OCC SR 11-7) |
| **Operational** | Agents must be treated as managed products, not ad-hoc scripts |
| **Accountability** | Training constraints create audit-defensible behavioral boundaries |
| **Business Continuity** | Rollback capability is essential for production reliability |

### Solution Approach

| If CSP Owns | If Zeta Owns |
|-------------|--------------|
| Agent definitions are CSP-specific formats | Agent definitions are portable |
| Versioning is implicit or basic | Full semantic versioning with lifecycle stages |
| No promotion workflows | Bank-compliant change management |
| Rollback may lose state | Rollback maintains state consistency |
| No retirement model | Controlled deprecation and migration |
| Training and employment conflated | Clear separation with immutability guarantees |

**Zeta's approach:**

- Agent definitions stored in **Zeta-owned format** (YAML/JSON schema)
- Definitions are **version-controlled** in Git (customer-managed or Zeta-hosted)
- **Three-layer model**: Raw Agent (container) → Trained Agent (configured) → Employed Agent (delegated)
- Training guardrails are **immutable**; employment can narrow scope but never expand authority

### Portability Approach

- Agent definitions are CSP-independent
- Deployment handled by Zeta orchestration, not CSP agent deployment APIs
- CSP-specific elements (model references, tool endpoints) are **parameterized**, not embedded

### Data Model (Conceptual)

```yaml
agent:
  id: "collections-agent-v2"
  version: "2.4.1"
  status: "active"
  
  identity:
    name: "Collections Agent"
    description: "Handles overdue account communications"
    owner: "collections-team@bank.com"
  
  capabilities:
    - send_communication
    - query_account
    - propose_payment_plan
  
  authority:
    ceiling: 
      max_commitment_amount: 5000
      requires_approval_above: 1000
    scope:
      - customer_segment: "retail"
      - product_types: ["credit_card", "personal_loan"]
  
  configuration:
    primary_model: "claude-3-sonnet"
    fallback_model: "gpt-4o-mini"
    memory_scope: "customer"
    session_timeout: "30m"
```

---

## 8.2 Agent Identity & Authority Framework

### Requirements

The platform must provide **verifiable identity** and **explicit authority** for agents.

| Requirement | Description |
|-------------|-------------|
| **Agent Identity** | Unique, cryptographically verifiable agent identifiers |
| **Identity Lifecycle** | Create, rotate, revoke agent credentials |
| **Authority Definition** | Explicit statement of what agent can do (not implicit from code) |
| **Delegation Chain** | Traceable chain: who delegated authority to this agent? |
| **Ceiling Enforcement** | Hard limits on agent actions (amount, scope, rate) |
| **Kill Switch** | Instant, global authority revocation (not just process termination) |
| **Authority Audit** | Immutable log of all delegation changes |
| **Layered Authority** | Policy hierarchy: Bank → Agent Class → Agent Instance → Request |

### Why It Matters

| Driver | Requirement Source |
|--------|-------------------|
| **Regulatory** | Banking regulations require clear accountability for automated decisions |
| **Accountability** | "The system did it" is not acceptable to regulators |
| **Safety** | Authority ceilings prevent runaway agent actions |
| **Incident Response** | Kill switch enables rapid containment |

### Solution Approach

| If CSP Owns | If Zeta Owns |
|-------------|--------------|
| No distinct agent identity (uses caller identity) | Agent has own identity |
| No delegation concept | Explicit delegation with audit trail |
| No ceilings (all-or-nothing access) | Fine-grained limits |
| No kill switch (disable agent process) | Instant authority revocation |
| No authority audit | Full delegation history |

**Zeta's approach:**

- Agent identities are **Zeta-issued**, not CSP IAM principals
- Authority policies stored in **portable format**
- Kill switch operates at **authority level**, not infrastructure level
- Delegation chain stored in **Zeta-owned audit store**

### Portability Approach

- Agent identities are platform-owned, not CSP-specific
- Authority policies are portable (Rego, YAML, or custom DSL)
- Kill switch is platform-controlled, independent of CSP

### Authority Hierarchy Model

```
┌─────────────────────────────────────────────────────────────────────┐
│                      AUTHORITY HIERARCHY                            │
│                                                                     │
│  ┌─────────────────────────────────────────────────────────────┐   │
│  │ BANK POLICY                                                  │   │
│  │ "No agent may commit more than $50,000 without human"        │   │
│  └─────────────────────────────────────────────────────────────┘   │
│                              │                                      │
│                              ▼                                      │
│  ┌─────────────────────────────────────────────────────────────┐   │
│  │ AGENT CLASS POLICY                                           │   │
│  │ "Collections agents may commit up to $10,000"                │   │
│  └─────────────────────────────────────────────────────────────┘   │
│                              │                                      │
│                              ▼                                      │
│  ┌─────────────────────────────────────────────────────────────┐   │
│  │ AGENT INSTANCE POLICY                                        │   │
│  │ "This agent may commit up to $5,000 for retail customers"    │   │
│  └─────────────────────────────────────────────────────────────┘   │
│                              │                                      │
│                              ▼                                      │
│  ┌─────────────────────────────────────────────────────────────┐   │
│  │ REQUEST CONTEXT                                              │   │
│  │ "This request is for a $3,000 commitment"                    │   │
│  └─────────────────────────────────────────────────────────────┘   │
│                              │                                      │
│                              ▼                                      │
│                       ✓ AUTHORIZED                                  │
└─────────────────────────────────────────────────────────────────────┘
```

---

## 8.3 Context Assembly Engine

### Requirements

The platform must construct the **complete context** for each agent reasoning step in a reproducible, auditable manner.

| Requirement | Description |
|-------------|-------------|
| **Context Sources** | Define what sources contribute to context (memory, knowledge, session, APIs) |
| **Retrieval Orchestration** | Coordinate retrieval from multiple sources with configurable strategies |
| **Context Ranking** | Prioritize information by relevance, recency, authority |
| **Context Truncation** | Manage context size within model limits with intelligent truncation |
| **Context Logging** | Record assembled context for audit and reproducibility |
| **Reproducibility** | Same inputs must produce same context (deterministic assembly) |
| **Separation of Concerns** | Context assembly is platform responsibility, not agent code |

### Why It Matters

| Driver | Requirement Source |
|--------|-------------------|
| **Regulatory** | Regulators may ask "what information was available when this decision was made?" |
| **Explainability** | Decisions cannot be explained without knowing the input context |
| **Debugging** | Context issues are the #1 cause of agent misbehavior |
| **Reproducibility** | Audit requires ability to reproduce decision conditions |

### Solution Approach

| If CSP Owns | If Zeta Owns |
|-------------|--------------|
| Context assembly is opaque | Context assembly is inspectable |
| Retrieval logic is CSP-determined | Retrieval logic is configurable |
| No context logging | Full context audit trail |
| Cannot reproduce decision context | Decisions are reproducible |

**Zeta's approach:**

- Context sources defined in **Zeta configuration**, not CSP agent settings
- Retrieval uses **abstraction layer** for memory and knowledge
- Context logs stored in **audit store**, not CSP logs
- Context assembly logic is **platform-owned**, not CSP orchestration

### Portability Approach

- Context sources are platform-defined abstractions
- Storage backends are swappable (different DBs, vector stores)
- Context snapshots are stored in portable format

### Context Assembly Flow

```
┌─────────────────────────────────────────────────────────────────────┐
│                    CONTEXT ASSEMBLY FLOW                            │
│                                                                     │
│  Input Request ───►  ┌──────────────────────────────────────────┐  │
│                      │           Context Assembler              │  │
│                      │                                          │  │
│  ┌─────────────┐     │   ┌─────────────────────────────────┐   │  │
│  │   Memory    │────►│   │  1. Retrieve from memory        │   │  │
│  └─────────────┘     │   │  2. Retrieve from knowledge     │   │  │
│                      │   │  3. Retrieve from session       │   │  │
│  ┌─────────────┐     │   │  4. Add system context          │   │  │
│  │  Knowledge  │────►│   │  5. Rank by relevance           │   │  │
│  └─────────────┘     │   │  6. Truncate to fit             │   │  │
│                      │   │  7. Log assembled context       │   │  │
│  ┌─────────────┐     │   └─────────────────────────────────┘   │  │
│  │   Session   │────►│                                          │  │
│  └─────────────┘     └───────────────────┬──────────────────────┘  │
│                                          │                          │
│                                          ▼                          │
│                           Assembled Context (to Model)              │
└─────────────────────────────────────────────────────────────────────┘
```

---

## 8.4 Memory System

### Requirements

The platform must provide **persistent, typed, scoped memory** for agents with clear lifecycle and governance.

| Requirement | Description |
|-------------|-------------|
| **Memory Types** | Distinguish episodic (events), semantic (facts), procedural (how-to), preference (settings) |
| **Memory Scopes** | Support organizational, workbench, customer, agent, and session scopes |
| **Organizational Memory** | Long-lived, cross-agent memory for institutional learning |
| **Operational Memory** | Session/request-scoped memory for in-flight operations |
| **Memory Isolation** | Tenant, customer, agent isolation with no cross-contamination |
| **Memory Lifecycle** | TTL, archival, deletion with clear policies |
| **Memory Export/Import** | Portability across environments |
| **Memory Versioning** | Point-in-time recovery capability |
| **Right to Forget** | Demonstrable deletion for GDPR/CCPA compliance |

### Why It Matters

| Driver | Requirement Source |
|--------|-------------------|
| **Regulatory** | Right to be forgotten (GDPR, CCPA) requires demonstrable deletion |
| **Operational** | Banks must control customer data lifecycle |
| **Learning** | Institutional memory enables continuous improvement |
| **Isolation** | Multi-tenant environments require strict memory boundaries |

### Solution Approach

| If CSP Owns | If Zeta Owns |
|-------------|--------------|
| "Memory" is session context only | True persistent memory with types |
| Memory is CSP-specific format | Memory is portable |
| No memory types (undifferentiated) | Typed memory with different semantics |
| No memory export | Full export/import capability |
| Memory deletion unclear | Clear deletion with evidence |

**Zeta's approach:**

- Memory schema is **Zeta-defined**, using portable formats
- Memory storage uses **abstraction layer** (PostgreSQL, Cosmos, AlloyDB)
- Memory replication is **Zeta-managed**, not CSP-managed
- Memory export produces **self-describing format** (JSON + schema)
- Clear separation: **Organizational Memory** (audit, learning) vs. **Operational Memory** (session, request)

### Portability Approach

- Memory schema is CSP-independent
- Storage backends are abstracted and swappable
- Export format is self-describing

### Memory Architecture

```
┌─────────────────────────────────────────────────────────────────────┐
│                       MEMORY SYSTEM                                 │
│                                                                     │
│  ┌─────────────────────────────────────────────────────────────┐   │
│  │                    Memory Manager                            │   │
│  │   - Scoping (tenant/customer/agent)                          │   │
│  │   - Lifecycle (TTL, archival)                                │   │
│  │   - Access control                                           │   │
│  └─────────────────────────────────────────────────────────────┘   │
│                              │                                      │
│       ┌──────────────────────┼──────────────────────┐              │
│       ▼                      ▼                      ▼              │
│  ┌─────────────┐      ┌─────────────┐      ┌─────────────┐         │
│  │  Episodic   │      │  Semantic   │      │ Preference  │         │
│  │   Store     │      │   Store     │      │   Store     │         │
│  │ (Events)    │      │ (Facts)     │      │ (Settings)  │         │
│  └─────────────┘      └─────────────┘      └─────────────┘         │
│       │                      │                      │               │
│       └──────────────────────┼──────────────────────┘               │
│                              ▼                                      │
│  ┌─────────────────────────────────────────────────────────────┐   │
│  │              Storage Abstraction Layer                       │   │
│  │   PostgreSQL  │  Cosmos DB  │  AlloyDB  │  ...               │   │
│  └─────────────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────────────┘
```

---

## 8.5 Knowledge Integration Layer (RAG)

### Requirements

The platform must connect agents to **external, authoritative knowledge sources** with provenance tracking.

| Requirement | Description |
|-------------|-------------|
| **Knowledge Sources** | Register and configure knowledge sources (documents, APIs, databases) |
| **Retrieval Orchestration** | Coordinate search across multiple sources |
| **Embedding Management** | Generate and manage embeddings for semantic search |
| **Result Ranking** | Combine and rank results from multiple sources |
| **Source Attribution** | Track what knowledge came from where (provenance) |
| **Freshness Tracking** | Know when knowledge was last updated |
| **Access Control** | Enforce entitlements on knowledge access |
| **Knowledge vs. Memory** | Clear distinction: Knowledge is curated truth; Memory is learned experience |

### Why It Matters

| Driver | Requirement Source |
|--------|-------------------|
| **Regulatory** | Banks must know where information came from when defending decisions |
| **Accuracy** | Agents must use authoritative, up-to-date information |
| **Explainability** | Decisions must cite sources |
| **Governance** | Knowledge sources must be controlled and versioned |

### Solution Approach

| If CSP Owns | If Zeta Owns |
|-------------|--------------|
| RAG is tightly coupled to CSP vector DB | RAG uses portable vector backends |
| Knowledge sources are CSP-specific | Knowledge sources are abstracted |
| No source attribution in results | Full provenance tracking |
| Embedding generation locked to CSP | Embedding model is swappable |

**Zeta's approach:**

- Knowledge source configuration is **Zeta-owned**
- Vector storage uses **abstraction layer** (OpenSearch, Azure AI Search, pgvector)
- Embedding generation uses **model abstraction** (can switch providers)
- Retrieval logic is **Zeta code**, not CSP orchestration
- Source attribution stored in **Zeta audit records**

### Portability Approach

- Knowledge source definitions are CSP-independent
- Vector storage is abstracted (prefer pgvector for portability)
- Embeddings may need regeneration on provider switch (acceptable tradeoff)

### RAG Flow

```
┌─────────────────────────────────────────────────────────────────────┐
│                      KNOWLEDGE RETRIEVAL                            │
│                                                                     │
│  Query ─────►  ┌────────────────────────────────────────────────┐  │
│                │           Retrieval Orchestrator               │  │
│                │                                                │  │
│                │  1. Parse query intent                         │  │
│                │  2. Determine relevant sources                 │  │
│                │  3. Check access entitlements                  │  │
│                │  4. Execute parallel retrieval                 │  │
│                │  5. Rank and merge results                     │  │
│                │  6. Attach provenance                          │  │
│                └─────────────────┬──────────────────────────────┘  │
│                                  │                                  │
│         ┌────────────────────────┼────────────────────────┐        │
│         ▼                        ▼                        ▼        │
│  ┌─────────────┐         ┌─────────────┐         ┌─────────────┐  │
│  │  Vector DB  │         │   Graph DB  │         │   Live API  │  │
│  │ (Documents) │         │(Relationships)│       │ (Real-time) │  │
│  └─────────────┘         └─────────────┘         └─────────────┘  │
│                                                                     │
│                                  │                                  │
│                                  ▼                                  │
│                    Retrieved Knowledge + Provenance                 │
└─────────────────────────────────────────────────────────────────────┘
```

---

## 8.6 Tool & Action Framework

### Requirements

The platform must enable agents to **take actions** in the world with appropriate controls.

| Requirement | Description |
|-------------|-------------|
| **Tool Registry** | Catalog of available tools with schemas |
| **Tool Versioning** | Track tool versions for compatibility |
| **Permission Model** | Define which agents can use which tools |
| **Execution Sandbox** | Isolated execution environment for tools |
| **Retry & Timeout** | Configurable failure handling |
| **Result Validation** | Validate tool outputs before returning |
| **Tool Logging** | Full audit of tool invocations |
| **Action Classification** | Distinguish read/notify/propose/execute/irreversible actions |
| **Rate Limiting** | Prevent runaway tool usage |
| **Open Standards** | Support for Model Context Protocol (MCP) and similar |

### Why It Matters

| Driver | Requirement Source |
|--------|-------------------|
| **Regulatory** | Banks must control and audit all actions taken on their behalf |
| **Safety** | Irreversible actions require additional controls |
| **Reliability** | Tools must have predictable failure handling |
| **Interoperability** | Open standards reduce integration effort |

### Solution Approach

| If CSP Owns | If Zeta Owns |
|-------------|--------------|
| Tool definitions are CSP-specific | Tool definitions are portable |
| Tool execution is CSP-managed | Tool execution is Zeta-controlled |
| Limited execution controls | Full sandbox and policy enforcement |
| Tool logs in CSP format | Tool logs in portable audit format |

**Zeta's approach:**

- Tool definitions use **open schema** (MCP-compatible where possible)
- Tool execution uses **Zeta runtime**, not CSP-specific executors
- Tool credentials managed by **Zeta secrets management**
- Tool logs written to **Zeta audit store**

### Portability Approach

- Tool definitions are CSP-independent
- Execution is containerized (portable)
- Credentials use abstracted secrets management

### Action Classification and Controls

| Action Type | Example | Required Controls |
|-------------|---------|-------------------|
| **Read** | Query customer balance | Audit log |
| **Notify** | Send SMS notification | Audit log + rate limit |
| **Propose** | Suggest payment plan | Audit log + route to approval |
| **Execute** | Submit payment | Authority check + audit log |
| **Irreversible** | Close account | Pre-approval + confirmation + audit |

### Tool Definition Example

```yaml
tool:
  id: "send-sms"
  version: "1.2.0"
  
  description: "Send SMS to customer phone number"
  
  action_type: "notify"
  
  permissions:
    required_capabilities:
      - "send_communication"
    rate_limit:
      max_per_hour: 10
      max_per_customer_per_day: 3
  
  input_schema:
    type: object
    properties:
      customer_id:
        type: string
      message:
        type: string
        maxLength: 160
  
  output_schema:
    type: object
    properties:
      message_id:
        type: string
      status:
        type: string
        enum: ["sent", "queued", "failed"]
  
  timeout: 10s
  retry:
    max_attempts: 2
    backoff: exponential
```

---

## 8.7 Cognitive Audit Fabric (CAF)

### Overview

The Cognitive Audit Fabric (CAF) is the most critical component for regulated industries. It provides **regulator-grade evidence** for all agent activity, enabling enterprises to explain, defend, and learn from agent decisions.

CAF is not merely logging—it is the **cognitive memory control plane** that governs how decisions are captured, linked, explained, and audited.

### Requirements

#### 8.7.1 Decision Audit Requirements

| Requirement | Description |
|-------------|-------------|
| **Decision Records** | Structured record of every agent decision with rationale |
| **Context Snapshots** | Captured context at decision time (what the agent knew) |
| **Outcome Tracking** | Link decisions to their outcomes for learning |
| **Immutability** | Records cannot be modified after creation (append-only) |
| **Tamper Evidence** | Cryptographic hashing to detect tampering |
| **Causal Linking** | Decisions linked to triggers, evidence, and outcomes |

#### 8.7.2 Explanation Requirements

| Requirement | Description |
|-------------|-------------|
| **Real-Time Explanation** | Explanation generated at decision time, not reconstructed |
| **Multi-Audience Formatting** | Explanations tailored for customers, operators, regulators |
| **Factor Attribution** | Which inputs influenced the decision, and how |
| **Counterfactual Support** | What would have changed the decision? |
| **Natural Language** | Human-readable explanations, not just structured data |

#### 8.7.3 Evidence Packaging Requirements

| Requirement | Description |
|-------------|-------------|
| **Evidence Bundles** | Self-contained packages for regulatory response |
| **Context Reproduction** | Ability to reproduce the decision environment |
| **Chain of Custody** | Traceable handling of evidence |
| **Export Formats** | Self-describing, portable formats |
| **Selective Disclosure** | Export subsets without exposing unrelated data |

#### 8.7.4 Memory Taxonomy Requirements

The platform must support **distinct memory classes** with different semantics:

| Memory Class | Purpose | Characteristics |
|--------------|---------|-----------------|
| **Episodic** | What happened (events, decisions, interactions) | Time-ordered, immutable, case-bound |
| **Semantic** | What is believed (learned facts, patterns) | Entity-anchored, probabilistic, updatable |
| **Procedural** | How to do things (learned workflows, skills) | Skill-anchored, executable, refinable |
| **Preference** | What is preferred (settings, behaviors) | Subject-anchored, context-sensitive |

Each memory class has distinct:
- Retention policies
- Update semantics (immutable vs. refinable)
- Governance requirements
- Query patterns

#### 8.7.5 Human Intervention Audit Requirements

| Requirement | Description |
|-------------|-------------|
| **Override Records** | Document when humans override agent decisions |
| **Intervention Context** | Why the intervention occurred, what was changed |
| **Directive Tracking** | Track lifecycle of human directives to agents |
| **Escalation Audit** | Record when and why agents escalated to humans |
| **Handoff Context** | Preserve state when work transfers between agents or to humans |

#### 8.7.6 Data Governance Requirements

| Requirement | Description |
|-------------|-------------|
| **No PII in Audit Records** | Audit records use entity references, not personal data |
| **PII Resolution at Runtime** | Personal data retrieved when needed via controlled tools |
| **Long-Term Retention** | 7+ year retention for regulatory compliance |
| **Legal Hold** | Suspend deletion for litigation or investigation |
| **Right to Erasure** | Controlled deletion with evidence of compliance |

#### 8.7.7 Learning & Promotion Requirements

| Requirement | Description |
|-------------|-------------|
| **Pattern Detection** | Identify recurring patterns from episodic memory |
| **Hypothesis Formation** | Form testable beliefs from observations |
| **Knowledge Promotion** | Promote validated learnings to authoritative knowledge |
| **Feedback Loops** | Outcomes inform future decisions |
| **Controlled Promotion** | Human approval for knowledge promotion |

### Why It Matters

| Driver | Requirement Source |
|--------|-------------------|
| **OCC SR 11-7** | Model Risk Management requires documentation of model decisions |
| **EU AI Act** | Explainability requirements for high-risk AI systems |
| **Fair Lending** | Adverse action notices require decision explanations |
| **Incident Response** | Understanding what happened when things go wrong |
| **Continuous Improvement** | Learning from past decisions to improve future ones |
| **Human Oversight** | Demonstrating that humans remain in control |

### Solution Approach

| If CSP Owns | If Zeta Owns |
|-------------|--------------|
| Logs are operational telemetry | Logs are evidentiary records |
| No structured decision records | Full decision audit trail |
| Explanations are reconstructed | Explanations are captured at decision time |
| Evidence requires manual assembly | Evidence is auto-generated |
| Retention is log retention | Retention is regulatory-grade |
| No memory taxonomy | Typed memory with distinct semantics |
| Override is undocumented | Override has full audit trail |
| No learning from experience | Structured learning and promotion |

**Zeta's approach:**

- Audit records use **portable schema** (JSON + self-describing metadata)
- Storage uses **abstraction layer** with immutability enforcement
- Export produces **standalone evidence packages**
- Queries work across **all deployment environments**
- Memory is **typed** with class-specific retention and governance
- Human interventions are **first-class audit events**
- Learning is **controlled** with human-in-the-loop promotion

### Portability Approach

- Audit schema is CSP-independent
- Storage backends are abstracted
- Export format is self-describing
- No dependency on CSP-specific logging services

### Decision Record Structure (Conceptual)

```json
{
  "record_id": "dec-2025-01-02-abc123",
  "timestamp": "2025-01-02T14:32:17.892Z",
  
  "agent": {
    "id": "collections-agent-v2",
    "version": "2.4.1"
  },
  
  "session": {
    "id": "ses-xyz789",
    "customer_ref": "cust-456"
  },
  
  "decision": {
    "type": "payment_plan_proposal",
    "outcome": "approved",
    "details": {
      "amount": 3000,
      "term_months": 12
    }
  },
  
  "context": {
    "hash": "sha256:abcdef...",
    "snapshot_ref": "ctx/2025/01/02/abc123.json"
  },
  
  "explanation": {
    "text": "Proposed 12-month payment plan based on customer's stated income and payment history. Amount is within authority ceiling.",
    "factors": [
      {"factor": "monthly_income", "value": 4500, "impact": "positive"},
      {"factor": "payment_history", "value": "good", "impact": "positive"},
      {"factor": "debt_to_income", "value": 0.35, "impact": "neutral"}
    ]
  },
  
  "authority": {
    "delegation_chain": ["bank-policy-001", "collections-policy-v2", "agent-collections-v2"],
    "ceiling_check": "passed",
    "approval_required": false
  },
  
  "integrity": {
    "content_hash": "sha256:...",
    "previous_record_hash": "sha256:..."
  }
}
```

---

## 8.8 Governance, Risk & Override Layer

### Requirements

The platform must enforce **policies, controls, and human oversight** at all times.

| Requirement | Description |
|-------------|-------------|
| **Policy Engine** | Define and enforce governance policies declaratively |
| **Guardrails** | Input/output filtering, topic blocking, safety checks |
| **Approval Workflows** | Route high-risk decisions to humans |
| **Override Mechanism** | Allow humans to intervene and correct (with full audit) |
| **Kill Switches** | Instant agent capability revocation |
| **Dual Control** | Require multiple approvals for sensitive actions |
| **Risk Scoring** | Assess risk level of agent actions dynamically |
| **Guardrail Immutability** | Training-time guardrails cannot be bypassed at runtime |

### Why It Matters

| Driver | Requirement Source |
|--------|-------------------|
| **Regulatory** | Human oversight is a regulatory expectation |
| **Accountability** | Banks cannot delegate final authority to machines for consequential decisions |
| **Safety** | Guardrails prevent harmful outputs |
| **Compliance** | Policies ensure regulatory adherence |

### Solution Approach

| If CSP Owns | If Zeta Owns |
|-------------|--------------|
| Guardrails are CSP-defined categories | Guardrails are bank-customizable |
| No approval workflows | Full workflow integration |
| Override is "disable agent" | Override is surgical and logged |
| Kill switch is infrastructure-level | Kill switch is authority-level |
| No dual control | Dual control for banking |

**Zeta's approach:**

- Policies defined in **portable format** (Rego, YAML, or custom DSL)
- Policy engine is **Zeta-owned** (can use OPA or custom)
- Guardrails compile to **CSP-native enforcement** but are defined portably
- Approval workflows use **Zeta workflow engine**
- Training guardrails are **immutable**—employment can add but never remove

### Portability Approach

- Policy definitions are CSP-independent
- Enforcement uses portable policy engines (OPA)
- Approval workflows are platform-managed

### Policy Types

| Policy Type | Purpose | Example |
|-------------|---------|---------|
| **Authority Policy** | What can agent do? | "Max commitment $5000" |
| **Safety Policy** | What must agent avoid? | "Never disclose other customer data" |
| **Escalation Policy** | When to involve humans? | "Escalate if customer expresses distress" |
| **Rate Policy** | How often can agent act? | "Max 100 SMS per hour" |
| **Content Policy** | What can agent say? | "No discussion of competitor products" |

### Override Flow

```
┌─────────────────────────────────────────────────────────────────────┐
│                       OVERRIDE MECHANISM                            │
│                                                                     │
│  Agent proposes action ──► Policy Check ──► Risk Assessment         │
│                                                │                    │
│                              ┌─────────────────┼─────────────────┐  │
│                              │                 │                 │  │
│                              ▼                 ▼                 ▼  │
│                        ┌─────────┐       ┌──────────┐     ┌────────┐│
│                        │  Allow  │       │  Review  │     │ Block  ││
│                        └────┬────┘       └────┬─────┘     └───┬────┘│
│                             │                 │               │     │
│                             ▼                 ▼               ▼     │
│                        Execute           Route to          Log and │
│                                          Human             Reject  │
│                                             │                       │
│                              ┌──────────────┼──────────────┐       │
│                              │              │              │       │
│                              ▼              ▼              ▼       │
│                         ┌────────┐    ┌──────────┐   ┌──────────┐  │
│                         │Approve │    │ Modify   │   │  Reject  │  │
│                         │        │    │          │   │          │  │
│                         └───┬────┘    └────┬─────┘   └────┬─────┘  │
│                             │              │              │        │
│                             ▼              ▼              ▼        │
│                         Execute        Execute       Log and      │
│                         Original       Modified      Escalate     │
│                                                                     │
│  All paths logged with operator identity and reason                │
└─────────────────────────────────────────────────────────────────────┘
```

---

## 8.9 Runtime & Deployment Abstraction

### Requirements

The platform must enable **consistent agent execution** across environments.

| Requirement | Description |
|-------------|-------------|
| **Runtime Abstraction** | Same agent code runs on any CSP |
| **Deployment Orchestration** | Automated deployment to target environments |
| **Configuration Management** | Environment-specific configuration without code changes |
| **Scaling** | Horizontal scaling based on load |
| **Health Management** | Liveness, readiness, and dependency checks |
| **Secret Management** | Secure credential handling across environments |
| **Multi-Region Coordination** | Active-active deployment management |
| **Graceful Degradation** | Predictable behavior when dependencies fail |

### Why It Matters

| Driver | Requirement Source |
|--------|-------------------|
| **Business Continuity** | Multi-region deployment for disaster recovery |
| **Portability** | Avoid CSP lock-in at runtime level |
| **Operations** | Consistent deployment across environments |
| **Reliability** | Graceful degradation prevents cascading failures |

### Solution Approach

| If CSP Owns | If Zeta Owns |
|-------------|--------------|
| Runtime is CSP-specific (Bedrock, Azure AI) | Runtime is portable |
| Deployment uses CSP-specific tools | Deployment is standardized |
| Scaling depends on CSP service | Scaling is Zeta-controlled |
| Multi-region is manual | Multi-region is automated |

**Zeta's approach:**

- Agents run in **containers** (Kubernetes), not CSP-specific runtimes
- Configuration uses **environment abstraction** (no CSP-specific config)
- Secrets use **portable secrets management** (Vault or abstracted CSP secrets)
- Deployment uses **Zeta orchestrator** (can target any CSP)

### Portability Approach

- Container-based (Kubernetes is the portability layer)
- Configuration is environment-abstracted
- Secrets management is abstracted

### Deployment Model

```
┌─────────────────────────────────────────────────────────────────────┐
│                   DEPLOYMENT ABSTRACTION                            │
│                                                                     │
│  ┌─────────────────────────────────────────────────────────────┐   │
│  │              Zeta Deployment Orchestrator                    │   │
│  │   - Agent version resolution                                 │   │
│  │   - Environment configuration                                │   │
│  │   - Rollout strategy (blue-green, canary)                    │   │
│  │   - Health verification                                      │   │
│  └─────────────────────────────────────────────────────────────┘   │
│                              │                                      │
│              ┌───────────────┼───────────────┐                     │
│              ▼               ▼               ▼                     │
│  ┌───────────────────┐┌───────────────────┐┌───────────────────┐  │
│  │    AWS Target     ││   Azure Target    ││    GCP Target     │  │
│  │  ┌─────────────┐  ││  ┌─────────────┐  ││  ┌─────────────┐  │  │
│  │  │     EKS     │  ││  │     AKS     │  ││  │     GKE     │  │  │
│  │  └─────────────┘  ││  └─────────────┘  ││  └─────────────┘  │  │
│  │  ┌─────────────┐  ││  ┌─────────────┐  ││  ┌─────────────┐  │  │
│  │  │   Bedrock   │  ││  │ Azure OpenAI│  ││  │  Vertex AI  │  │  │
│  │  └─────────────┘  ││  └─────────────┘  ││  └─────────────┘  │  │
│  └───────────────────┘└───────────────────┘└───────────────────┘  │
└─────────────────────────────────────────────────────────────────────┘
```

---

## 8.10 Observability & Monitoring

### Requirements

The platform must provide **comprehensive visibility** into agent behavior and health.

| Requirement | Description |
|-------------|-------------|
| **Runtime Metrics** | Latency, throughput, error rates, token usage |
| **Cost Metrics** | Token costs, inference costs, storage costs |
| **Health Indicators** | Agent health scores, degradation detection |
| **Distributed Tracing** | End-to-end request traces across services |
| **Log Aggregation** | Centralized, searchable logs |
| **Alerting** | Threshold-based and anomaly-based alerts |
| **Dashboards** | Role-specific views (operator, SRE, executive) |
| **Open Standards** | OpenTelemetry compatibility |

### Why It Matters

| Driver | Requirement Source |
|--------|-------------------|
| **Operations** | Cannot operate what you cannot observe |
| **Cost Control** | LLM costs can spiral without visibility |
| **Incident Response** | Distributed tracing essential for debugging |
| **SLAs** | Health indicators support SLA management |

### Solution Approach

| If CSP Owns | If Zeta Owns |
|-------------|--------------|
| Observability in CSP-specific tools | Unified observability layer |
| Metrics in CSP formats | OpenTelemetry standard |
| Dashboards are CSP-specific | Portable dashboards |

**Zeta's approach:**

- Observability built on **OpenTelemetry** for portability
- Metrics, logs, traces exported to **platform observability layer**
- Dashboards are **portable** (Grafana or similar)
- Agent-specific metrics (AHS, CHR) are **platform-defined**

### Portability Approach

- OpenTelemetry is the instrumentation standard
- Backends are swappable (Prometheus, CloudWatch, Azure Monitor)
- Dashboards are exportable

---

## Summary: Component Ownership

| Component | Requirements Focus | Solution Focus |
|-----------|-------------------|----------------|
| **Lifecycle** | Version, deploy, promote, retire with change management | Zeta-owned lifecycle; CSPs provide compute |
| **Identity** | Agent identity, authority, delegation with audit | Zeta-issued identity; Zeta-owned policies |
| **Context** | Assembly, logging, reproducibility | Zeta-owned assembly; abstracted storage |
| **Memory** | Types, persistence, portability, right-to-forget | Zeta-defined schema; abstracted storage |
| **Knowledge** | Orchestration, provenance, freshness | Zeta-owned orchestration; CSP vector DBs |
| **Tools** | Registry, permissions, sandbox, audit | Zeta-owned registry; containerized execution |
| **CAF** | Decision records, explanations, evidence, memory taxonomy | Zeta-owned schemas; abstracted storage |
| **Governance** | Policies, guardrails, overrides, human oversight | Zeta-owned policies; portable enforcement |
| **Runtime** | Deployment, scaling, coordination | Zeta orchestration; Kubernetes portability |
| **Observability** | Metrics, traces, dashboards, alerting | OpenTelemetry; portable backends |

---

*Previous: [Section 7: Zeta Agent Platform: Conceptual Architecture](./07-conceptual-architecture.md)*

*Next: [Section 9: Summary Table: Required Platform Services →](./09-platform-services-table.md)*

