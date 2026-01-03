# 8. Platform Components & Design Rationale

---

This section details **each major component** of the Zeta Agent Platform. For each component:

- **What it does** — Functional description
- **Why Zeta must own it** — Strategic rationale
- **How it avoids CSP lock-in** — Portability approach

---

## 8.1 Agent Definition & Lifecycle Service

### What It Does

The Agent Definition & Lifecycle Service manages agents as **versioned, deployable products**.

| Capability | Description |
|------------|-------------|
| **Agent Schema** | Defines agent structure: identity, capabilities, constraints, configuration |
| **Version Management** | Semantic versioning (major.minor.patch) with change tracking |
| **Deployment** | Deploys agents to target environments (dev, staging, prod) |
| **Promotion Workflows** | Controlled progression with approval gates |
| **Rollback** | Instant reversion to previous version with state consistency |
| **Retirement** | Graceful end-of-life with deprecation warnings |
| **Registry** | Central catalog of all agents and versions |

### Why Zeta Must Own It

| If CSP Owns | If Zeta Owns |
|-------------|--------------|
| Agent definitions are CSP-specific formats | Agent definitions are portable |
| Versioning is implicit or basic | Full semantic versioning |
| No promotion workflows | Bank-compliant change management |
| Rollback may lose state | Rollback maintains state consistency |
| No retirement model | Controlled deprecation and migration |

**Regulatory driver:** Banks require change management processes for all production software. CSP agent frameworks provide basic versioning but lack the promotion workflows, approval gates, and rollback semantics that regulated environments require.

### How It Avoids CSP Lock-in

- Agent definitions are stored in **Zeta-owned format** (JSON/YAML schema)
- Definitions are **version-controlled** in Git (customer-managed or Zeta-hosted)
- Deployment is handled by **Zeta's deployment service**, not CSP agent deployment APIs
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

### What It Does

The Identity & Authority Framework provides **verifiable identity** and **explicit authority** for agents.

| Capability | Description |
|------------|-------------|
| **Agent Identity** | Unique, cryptographically verifiable agent identifiers |
| **Identity Lifecycle** | Create, rotate, revoke agent credentials |
| **Authority Definition** | Explicit statement of what agent can do |
| **Delegation Chain** | Who delegated authority to this agent? |
| **Ceiling Enforcement** | Hard limits on agent actions |
| **Kill Switch** | Instant, global authority revocation |
| **Authority Audit** | Immutable log of all delegation changes |

### Why Zeta Must Own It

| If CSP Owns | If Zeta Owns |
|-------------|--------------|
| No distinct agent identity (uses caller identity) | Agent has own identity |
| No delegation concept | Explicit delegation with audit trail |
| No ceilings (all-or-nothing access) | Fine-grained limits |
| No kill switch (disable agent process) | Instant authority revocation |
| No authority audit | Full delegation history |

**Regulatory driver:** Banking regulations require clear accountability for automated decisions. "The system did it" is not acceptable.

### How It Avoids CSP Lock-in

- Agent identities are **Zeta-issued**, not CSP IAM principals
- Authority policies are stored in **portable format**
- Kill switch operates at **Zeta control plane level**, independent of CSP
- Delegation chain is stored in **Zeta-owned audit store**

### Authority Model

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

### What It Does

The Context Assembly Engine constructs the **complete context** for each agent reasoning step.

| Capability | Description |
|------------|-------------|
| **Context Sources** | Defines what sources contribute to context |
| **Retrieval Orchestration** | Coordinates retrieval from memory, knowledge, APIs |
| **Context Ranking** | Prioritizes information by relevance |
| **Context Truncation** | Manages context size within model limits |
| **Context Logging** | Records assembled context for audit |
| **Reproducibility** | Same inputs produce same context |

### Why Zeta Must Own It

| If CSP Owns | If Zeta Owns |
|-------------|--------------|
| Context assembly is opaque | Context assembly is inspectable |
| Retrieval logic is CSP-determined | Retrieval logic is configurable |
| No context logging | Full context audit trail |
| Cannot reproduce decision context | Decisions are reproducible |

**Regulatory driver:** Regulators may ask "what information was available when this decision was made?" Zeta must be able to answer.

### How It Avoids CSP Lock-in

- Context sources are defined in **Zeta configuration**, not CSP agent settings
- Retrieval uses **abstraction layer** for memory and knowledge
- Context logs are stored in **Zeta audit store**, not CSP logs
- Context assembly logic is **Zeta code**, not CSP orchestration

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

### What It Does

The Memory System provides **persistent, typed, portable memory** for agents.

| Capability | Description |
|------------|-------------|
| **Episodic Memory** | What happened (interactions, events) |
| **Semantic Memory** | What is known (facts, relationships) |
| **Preference Memory** | What is preferred (user settings, learned preferences) |
| **Procedural Memory** | How to do things (learned workflows) |
| **Memory Scoping** | Tenant, customer, agent isolation |
| **Memory Lifecycle** | TTL, archival, deletion (right to forget) |
| **Memory Export/Import** | Portability across environments |
| **Memory Versioning** | Point-in-time recovery |

### Why Zeta Must Own It

| If CSP Owns | If Zeta Owns |
|-------------|--------------|
| "Memory" is session context only | True persistent memory |
| Memory is CSP-specific format | Memory is portable |
| No memory types (undifferentiated) | Typed memory with different semantics |
| No memory export | Full export/import capability |
| Memory deletion unclear | Clear deletion with evidence |

**Regulatory driver:** Right to be forgotten (GDPR, CCPA) requires demonstrable deletion. Banks must control customer data lifecycle.

### How It Avoids CSP Lock-in

- Memory schema is **Zeta-defined**, using portable formats
- Memory storage uses **abstraction layer** (PostgreSQL, Cosmos, AlloyDB)
- Memory replication is **Zeta-managed**, not CSP-managed
- Memory export produces **self-describing format** (JSON + schema)

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

### What It Does

The Knowledge Integration Layer connects agents to **external, authoritative knowledge sources**.

| Capability | Description |
|------------|-------------|
| **Knowledge Sources** | Register and configure knowledge sources (documents, APIs, databases) |
| **Retrieval Orchestration** | Coordinate search across multiple sources |
| **Embedding Management** | Generate and manage embeddings for semantic search |
| **Result Ranking** | Combine and rank results from multiple sources |
| **Source Attribution** | Track what knowledge came from where |
| **Freshness Tracking** | Know when knowledge was last updated |
| **Access Control** | Enforce entitlements on knowledge access |

### Why Zeta Must Own It

| If CSP Owns | If Zeta Owns |
|-------------|--------------|
| RAG is tightly coupled to CSP vector DB | RAG uses portable vector backends |
| Knowledge sources are CSP-specific | Knowledge sources are abstracted |
| No source attribution in results | Full provenance tracking |
| Embedding generation locked to CSP | Embedding model is swappable |

**Regulatory driver:** Banks must know where information came from when defending decisions to regulators.

### How It Avoids CSP Lock-in

- Knowledge source configuration is **Zeta-owned**
- Vector storage uses **abstraction layer** (OpenSearch, Azure AI Search, pgvector)
- Embedding generation uses **model abstraction** (can switch providers)
- Retrieval logic is **Zeta code**, not CSP orchestration
- Source attribution is stored in **Zeta audit records**

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

### What It Does

The Tool & Action Framework enables agents to **take actions** in the world.

| Capability | Description |
|------------|-------------|
| **Tool Registry** | Catalog of available tools with schemas |
| **Tool Versioning** | Track tool versions for compatibility |
| **Permission Model** | Define which agents can use which tools |
| **Execution Sandbox** | Isolated execution environment for tools |
| **Retry & Timeout** | Configurable failure handling |
| **Result Validation** | Validate tool outputs before returning |
| **Tool Logging** | Full audit of tool invocations |
| **MCP Support** | [Model Context Protocol](https://modelcontextprotocol.io/) compatibility |

### Why Zeta Must Own It

| If CSP Owns | If Zeta Owns |
|-------------|--------------|
| Tool definitions are CSP-specific | Tool definitions are portable |
| Tool execution is CSP-managed | Tool execution is Zeta-controlled |
| Limited execution controls | Full sandbox and policy enforcement |
| Tool logs in CSP format | Tool logs in portable audit format |

**Regulatory driver:** Banks must control and audit all actions taken on their behalf, including automated tool usage.

### How It Avoids CSP Lock-in

- Tool definitions use **open schema** (MCP-compatible where possible)
- Tool execution uses **Zeta runtime**, not CSP-specific executors
- Tool credentials are managed by **Zeta secrets management**
- Tool logs are written to **Zeta audit store**

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

## 8.7 Audit, Explanation & Evidence Fabric

### What It Does

The Audit Fabric provides **regulator-grade evidence** for all agent activity.

| Capability | Description |
|------------|-------------|
| **Decision Records** | Structured log of every agent decision |
| **Explanation Generation** | Natural language explanations at decision time |
| **Evidence Packaging** | Bundle evidence for regulatory response |
| **Immutability** | Tamper-evident, append-only storage |
| **Long-term Retention** | 7+ year retention with lifecycle management |
| **Search & Query** | Find relevant records during investigations |
| **Export** | Self-describing format for external systems |

### Why Zeta Must Own It

| If CSP Owns | If Zeta Owns |
|-------------|--------------|
| Logs are operational telemetry | Logs are evidentiary records |
| No structured decision records | Full decision audit trail |
| Explanations are reconstructed | Explanations are captured at decision time |
| Evidence requires manual assembly | Evidence is auto-generated |
| Retention is log retention | Retention is regulatory-grade |

**Regulatory driver:** OCC SR 11-7 requires documentation of model decisions. EU AI Act requires explainability for high-risk AI systems.

### How It Avoids CSP Lock-in

- Audit records use **portable schema** (JSON + self-describing metadata)
- Storage uses **abstraction layer** with immutability enforcement
- Export produces **standalone evidence packages**
- Queries work across **all deployment environments**

### Decision Record Structure

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
    "customer_id": "cust-456"
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
    "signature": "sig:...",
    "previous_record_hash": "sha256:..."
  }
}
```

---

## 8.8 Governance, Risk & Override Layer

### What It Does

The Governance Layer enforces **policies, controls, and human oversight**.

| Capability | Description |
|------------|-------------|
| **Policy Engine** | Define and enforce governance policies |
| **Guardrails** | Input/output filtering, topic blocking, safety checks |
| **Approval Workflows** | Route high-risk decisions to humans |
| **Override Mechanism** | Allow humans to intervene and correct |
| **Kill Switches** | Instant agent capability revocation |
| **Dual Control** | Require multiple approvals for sensitive actions |
| **Risk Scoring** | Assess risk level of agent actions |

### Why Zeta Must Own It

| If CSP Owns | If Zeta Owns |
|-------------|--------------|
| Guardrails are CSP-defined categories | Guardrails are bank-customizable |
| No approval workflows | Full workflow integration |
| Override is "disable agent" | Override is surgical and logged |
| Kill switch is infrastructure-level | Kill switch is authority-level |
| No dual control | Dual control for banking |

**Regulatory driver:** Human oversight is a regulatory expectation. Banks cannot delegate final authority to machines for consequential decisions.

### How It Avoids CSP Lock-in

- Policies are defined in **portable format** (Rego, YAML, or custom DSL)
- Policy engine is **Zeta-owned** (can use OPA or custom)
- Guardrails compile to **CSP-native enforcement** but are defined portably
- Approval workflows use **Zeta workflow engine**

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

### What It Does

The Runtime Abstraction enables **consistent agent execution** across environments.

| Capability | Description |
|------------|-------------|
| **Runtime Abstraction** | Same agent code runs on any CSP |
| **Deployment Orchestration** | Automated deployment to target environments |
| **Configuration Management** | Environment-specific configuration without code changes |
| **Scaling** | Horizontal scaling based on load |
| **Health Management** | Liveness, readiness, and dependency checks |
| **Secret Management** | Secure credential handling across environments |
| **Multi-region Coordination** | Active-active deployment management |

### Why Zeta Must Own It

| If CSP Owns | If Zeta Owns |
|-------------|--------------|
| Runtime is CSP-specific (Bedrock, Azure AI) | Runtime is portable |
| Deployment uses CSP-specific tools | Deployment is standardized |
| Scaling depends on CSP service | Scaling is Zeta-controlled |
| Multi-region is manual | Multi-region is automated |

### How It Avoids CSP Lock-in

- Agents run in **containers** (Kubernetes), not CSP-specific runtimes
- Configuration uses **environment abstraction** (no CSP-specific config)
- Secrets use **portable secrets management** (Vault or abstracted CSP secrets)
- Deployment uses **Zeta orchestrator** (can target any CSP)

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

## Summary: Component Ownership

| Component | What Zeta Owns | What CSPs Provide |
|-----------|----------------|-------------------|
| **Lifecycle** | Version, deploy, promote, retire | Compute to run agents |
| **Identity** | Agent identity, authority, delegation | IAM for infrastructure |
| **Context** | Assembly, logging, reproducibility | — |
| **Memory** | Types, persistence, portability | Storage backends |
| **Knowledge** | Orchestration, provenance | Vector DBs, embeddings |
| **Tools** | Registry, permissions, sandbox | Execution compute |
| **Audit** | Decision records, evidence, retention | Storage |
| **Governance** | Policies, guardrails, overrides | Safety APIs (optional) |
| **Runtime** | Deployment, scaling, coordination | Container orchestration |

---

*Previous: [Section 7: Zeta Agent Platform: Conceptual Architecture](./07-conceptual-architecture.md)*

*Next: [Section 9: Summary Table: Required Platform Services →](./09-platform-services-table.md)*

