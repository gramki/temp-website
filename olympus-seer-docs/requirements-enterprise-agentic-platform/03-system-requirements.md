# 3. System & Infrastructure Requirements for Agentic Products

---

This section defines **what the platform must do and why**, independent of any specific CSP or implementation. These are the requirements that any bank-grade agent platform must satisfy.

---

## 3.1 Deterministic and Inspectable Agent Behavior

### The Reproducibility Imperative

When an agent makes a decision, the bank must be able to:

1. **Reconstruct the context** — What information was available to the agent at decision time?
2. **Replay the reasoning** — Given the same inputs, can we understand how the agent reached its conclusion?
3. **Audit the chain** — What policies, tools, and data sources contributed to the decision?

This is not optional in regulated environments. It is the foundation of accountability.

### Requirements

| Requirement ID | Requirement | Rationale |
|----------------|-------------|-----------|
| **REQ-DET-01** | All inputs to agent reasoning must be captured and retrievable | Enables post-hoc reconstruction of decision context |
| **REQ-DET-02** | Agent prompts must be versioned and immutable once deployed | Prevents silent drift; enables rollback |
| **REQ-DET-03** | Tool calls and their results must be logged with timestamps | Creates evidence trail for auditors |
| **REQ-DET-04** | Model inference requests and responses must be logged | Enables reasoning reconstruction; required for model validation |
| **REQ-DET-05** | Non-deterministic elements (e.g., temperature) must be documented per agent version | Explains variance in outputs |

### Context Assembly Discipline

The agent's **context window** is the only information available during reasoning. Context assembly must be:

| Property | Definition |
|----------|------------|
| **Explicit** | Every element in context is intentionally included |
| **Traceable** | Each element has a source and timestamp |
| **Bounded** | Context size is managed; truncation follows policy |
| **Reproducible** | Given the same inputs, context assembly produces the same result |

---

## 3.2 Identity, Authority, and Control

### Agent Identity Requirements

Agents are not anonymous functions. They are **identifiable actors** in the system:

| Requirement ID | Requirement | Rationale |
|----------------|-------------|-----------|
| **REQ-ID-01** | Each agent instance must have a unique, stable identifier | Enables tracking across sessions and logs |
| **REQ-ID-02** | Agent identity must be distinct from user identity and system identity | Prevents attribution confusion |
| **REQ-ID-03** | Agent identity must be cryptographically verifiable | Prevents impersonation; enables secure delegation |
| **REQ-ID-04** | Agent versions must be independently identifiable | Different versions may have different behaviors and authorities |

### Authority Model Requirements

Agents exercise **delegated authority**—they act on behalf of the institution within defined boundaries:

| Requirement ID | Requirement | Rationale |
|----------------|-------------|-----------|
| **REQ-AUTH-01** | Agent authority must be explicitly defined and bounded | Prevents unauthorized actions |
| **REQ-AUTH-02** | Authority must include ceiling limits (amounts, rates, counts) | Limits blast radius of errors or compromise |
| **REQ-AUTH-03** | Authority can be scoped by customer, product, or context | Enables fine-grained delegation |
| **REQ-AUTH-04** | Authority delegation must be auditable | Regulators require evidence of who authorized what |
| **REQ-AUTH-05** | Authority can be revoked instantly, affecting all instances | Kill switch capability is non-negotiable |

### Control Requirements

| Requirement ID | Requirement | Rationale |
|----------------|-------------|-----------|
| **REQ-CTL-01** | Humans must be able to override agent decisions in real-time | Regulatory expectation for human-in-the-loop |
| **REQ-CTL-02** | Overrides must be logged with reason and operator identity | Creates evidence trail |
| **REQ-CTL-03** | High-risk actions must require explicit approval (dual control) | Standard banking control pattern |
| **REQ-CTL-04** | Agent pause and resume must be possible without data loss | Enables incident response |
| **REQ-CTL-05** | Agents must fail safe—default to human escalation, not autonomous action | Reduces risk of uncontrolled automation |

---

## 3.3 State, Memory, and Continuity

### Memory Type Requirements

Agent memory is **not a single concept**. The platform must support distinct memory types:

| Memory Type | Purpose | Retention | Portability |
|-------------|---------|-----------|-------------|
| **Episodic** | What happened (events, interactions) | Long-term, immutable | Must be portable |
| **Semantic** | What is known (facts, relationships) | Long-term, updateable | Must be portable |
| **Preference** | What is preferred (user/customer settings) | Long-term, updateable | Must be portable |
| **Procedural** | How to do things (learned workflows) | Long-term, versioned | Must be portable |
| **Working** | Current task state | Short-term, ephemeral | Session-scoped |

### Memory System Requirements

| Requirement ID | Requirement | Rationale |
|----------------|-------------|-----------|
| **REQ-MEM-01** | Memory must persist across sessions and agent restarts | Continuity is the value proposition |
| **REQ-MEM-02** | Memory must be scoped by tenant, customer, and jurisdiction | Data isolation is non-negotiable |
| **REQ-MEM-03** | Memory must be exportable and importable | Enables cloud portability |
| **REQ-MEM-04** | Memory writes must be durable before acknowledgment | Prevents data loss |
| **REQ-MEM-05** | Memory must support versioning and rollback | Enables recovery from corruption |
| **REQ-MEM-06** | Memory access must be auditable | Regulators may require evidence of what agent remembered |
| **REQ-MEM-07** | Memory must support deletion (right to be forgotten) | Regulatory requirement (GDPR, CCPA) |

### Session Requirements

| Requirement ID | Requirement | Rationale |
|----------------|-------------|-----------|
| **REQ-SES-01** | Sessions must have explicit start and end boundaries | Enables billing, audit, and lifecycle management |
| **REQ-SES-02** | Session state must be recoverable after transient failures | Prevents user experience disruption |
| **REQ-SES-03** | Sessions must be associated with agent instance and user/customer | Enables context reconstruction |
| **REQ-SES-04** | Session timeout and cleanup policies must be configurable | Different use cases have different needs |

---

## 3.4 Explainability, Auditability, and Evidence

### Explainability Requirements

Explainability is not "nice to have" in banking—it is a regulatory expectation:

| Requirement ID | Requirement | Rationale |
|----------------|-------------|-----------|
| **REQ-EXP-01** | Agent must provide natural language explanation for significant decisions | Enables human understanding |
| **REQ-EXP-02** | Explanations must reference the inputs that influenced the decision | Enables validation |
| **REQ-EXP-03** | Explanations must be generated at decision time, not reconstructed later | Ensures accuracy |
| **REQ-EXP-04** | Explanation generation must not alter the decision itself | Prevents post-hoc rationalization |
| **REQ-EXP-05** | Explanations must be stored with the decision record | Enables audit trail |

### Auditability Requirements

| Requirement ID | Requirement | Rationale |
|----------------|-------------|-----------|
| **REQ-AUD-01** | All agent actions must be logged with timestamp, agent ID, and context | Creates evidence chain |
| **REQ-AUD-02** | Logs must be immutable once written | Prevents tampering |
| **REQ-AUD-03** | Logs must be retained per jurisdictional requirements (typically 7+ years) | Regulatory mandate |
| **REQ-AUD-04** | Logs must be searchable and exportable | Enables investigation |
| **REQ-AUD-05** | Log integrity must be cryptographically verifiable | Detects tampering |

### Evidence Requirements

Evidence is the subset of audit data that can be presented to regulators:

| Requirement ID | Requirement | Rationale |
|----------------|-------------|-----------|
| **REQ-EVD-01** | Evidence must be complete—no material facts omitted | Regulators expect full picture |
| **REQ-EVD-02** | Evidence must be self-describing—interpretable without proprietary tools | Enables independent review |
| **REQ-EVD-03** | Evidence must be chain-of-custody aware | Proves authenticity |
| **REQ-EVD-04** | Evidence generation must be automated, not ad-hoc | Ensures consistency |

---

## 3.5 Knowledge Integration and Retrieval

### Knowledge vs. Memory Distinction

| Dimension | Knowledge | Memory |
|-----------|-----------|--------|
| **Ownership** | External (bank systems, documents, APIs) | Agent-owned |
| **Freshness** | Updated independently; agent retrieves on demand | Updated by agent actions |
| **Scope** | Shared across agents and systems | Scoped to specific agent/tenant |
| **Example** | Product catalog, customer profile, policy documents | Prior interactions, learned preferences |

### Knowledge Integration Requirements

| Requirement ID | Requirement | Rationale |
|----------------|-------------|-----------|
| **REQ-KNW-01** | Knowledge retrieval must be traceable (what was retrieved, when, from where) | Enables context reconstruction |
| **REQ-KNW-02** | Retrieved knowledge must be timestamped and versioned | Prevents reasoning on stale data |
| **REQ-KNW-03** | Knowledge sources must be authenticated and authorized | Prevents data poisoning |
| **REQ-KNW-04** | Knowledge retrieval latency must be bounded | Prevents agent timeouts |
| **REQ-KNW-05** | Knowledge retrieval failures must be handled gracefully | Agent should not fail silently |
| **REQ-KNW-06** | Knowledge access must respect data classification and entitlements | Prevents unauthorized disclosure |

---

## 3.6 Tool and Action Framework

### Tool Requirements

Tools are the mechanisms through which agents take action:

| Requirement ID | Requirement | Rationale |
|----------------|-------------|-----------|
| **REQ-TOOL-01** | Tools must be explicitly registered and versioned | Prevents unauthorized tool use |
| **REQ-TOOL-02** | Tool invocations must be logged with inputs and outputs | Enables audit and debugging |
| **REQ-TOOL-03** | Tools must have defined failure modes and timeouts | Prevents agent hangs |
| **REQ-TOOL-04** | Tool permissions must be scoped to agent authority | Agent cannot exceed its delegation |
| **REQ-TOOL-05** | Tool execution must be sandboxed | Prevents lateral movement |
| **REQ-TOOL-06** | Tools must support idempotency where possible | Enables safe retries |

### Action Classification

Not all actions are equal:

| Action Class | Definition | Control Required |
|--------------|------------|------------------|
| **Read** | Retrieves information; no side effects | Audit logging |
| **Notify** | Sends information; low-stakes side effect | Audit logging + rate limiting |
| **Propose** | Suggests action for human approval | Audit logging + workflow routing |
| **Execute** | Takes action with consequences | Authority check + dual control (if required) + audit |
| **Irreversible** | Cannot be undone | Pre-approval + explicit confirmation |

---

## 3.7 Availability, Resilience, and Business Continuity

### Availability Requirements

| Requirement ID | Requirement | Rationale |
|----------------|-------------|-----------|
| **REQ-AVL-01** | Agent platform must target 99.9% availability or higher | Banking SLA expectations |
| **REQ-AVL-02** | Single-region failure must not cause platform outage | Multi-region is mandatory |
| **REQ-AVL-03** | Planned maintenance must be zero-downtime | 24x7 banking operations |
| **REQ-AVL-04** | Availability must be measurable and reportable | Enables SLA tracking |

### Resilience Requirements

| Requirement ID | Requirement | Rationale |
|----------------|-------------|-----------|
| **REQ-RES-01** | Agent state must survive process restarts | Prevents work loss |
| **REQ-RES-02** | Agent must handle tool failures gracefully | Prevents cascade failures |
| **REQ-RES-03** | Agent must handle model inference failures | Must degrade gracefully |
| **REQ-RES-04** | Retry policies must be configurable per tool/action | Different actions have different tolerance |
| **REQ-RES-05** | Circuit breakers must prevent runaway failures | Standard resilience pattern |

### Business Continuity Requirements

| Requirement ID | Requirement | Rationale |
|----------------|-------------|-----------|
| **REQ-BC-01** | Platform must support active-active multi-region deployment | Enables regional failover |
| **REQ-BC-02** | Platform must support multi-cloud deployment | Enables CSP independence |
| **REQ-BC-03** | State synchronization across regions must have defined RPO/RTO | Banks require defined recovery objectives |
| **REQ-BC-04** | Failover must be automated with manual override capability | Reduces recovery time |
| **REQ-BC-05** | DR testing must be executable without production impact | Enables confidence in failover |

---

## 3.8 Security and Isolation

### Tenancy Requirements

| Requirement ID | Requirement | Rationale |
|----------------|-------------|-----------|
| **REQ-TEN-01** | Tenant data must be logically isolated | Prevents cross-tenant leakage |
| **REQ-TEN-02** | Tenant isolation must be enforced at multiple layers (app, data, network) | Defense in depth |
| **REQ-TEN-03** | Tenant-specific encryption keys must be supported | Enables bank-controlled encryption |
| **REQ-TEN-04** | Tenant onboarding/offboarding must be auditable | Enables compliance tracking |

### Security Requirements

| Requirement ID | Requirement | Rationale |
|----------------|-------------|-----------|
| **REQ-SEC-01** | All data at rest must be encrypted | Standard security practice |
| **REQ-SEC-02** | All data in transit must be encrypted (TLS 1.3+) | Standard security practice |
| **REQ-SEC-03** | Authentication must support bank identity providers | Enables SSO integration |
| **REQ-SEC-04** | Authorization must be fine-grained and auditable | Enables least-privilege |
| **REQ-SEC-05** | Secrets must be managed via vault, not embedded | Standard secret management |
| **REQ-SEC-06** | Vulnerability scanning must be continuous | Reduces exposure window |

---

## 3.9 Portability and Deployment

### Portability Requirements

| Requirement ID | Requirement | Rationale |
|----------------|-------------|-----------|
| **REQ-PORT-01** | Agent definitions must be CSP-agnostic | Enables multi-cloud |
| **REQ-PORT-02** | Agent memory must be exportable to standard formats | Prevents CSP lock-in |
| **REQ-PORT-03** | Agent configurations must be declarative and version-controlled | Enables GitOps |
| **REQ-PORT-04** | Platform must abstract CSP-specific services behind portable interfaces | Enables swappable backends |

### Deployment Requirements

| Requirement ID | Requirement | Rationale |
|----------------|-------------|-----------|
| **REQ-DEP-01** | Platform must support deployment in customer cloud accounts | Bank landing zone requirement |
| **REQ-DEP-02** | Deployment must be automated and repeatable | Reduces deployment risk |
| **REQ-DEP-03** | Deployment must support blue-green and canary patterns | Enables safe rollouts |
| **REQ-DEP-04** | Rollback must be instant and automated | Reduces incident duration |
| **REQ-DEP-05** | Deployment must work across AWS, Azure, and GCP | Multi-cloud mandate |

---

## Summary: Non-Negotiable Requirements

The following requirements are **non-negotiable** for a bank-grade agent platform:

| Category | Non-Negotiable Requirements |
|----------|-----------------------------|
| **Determinism** | Context reproducibility, prompt versioning, full logging |
| **Authority** | Explicit delegation, ceilings, kill switches, dual control |
| **Memory** | Persistence, portability, versioning, deletion |
| **Audit** | Immutable logs, evidence generation, 7+ year retention |
| **Explainability** | Decision-time explanations, input referencing |
| **Resilience** | Multi-region, graceful degradation, defined RTO/RPO |
| **Portability** | CSP-agnostic definitions, exportable state, customer-cloud deployment |
| **Security** | Encryption, tenant isolation, fine-grained authorization |

These requirements define the **minimum bar** for Zeta's agent platform. They are derived from banking regulations, enterprise expectations, and sound engineering principles—not from CSP marketing.

---

*Previous: [Section 2: Problem Statement & Strategic Context](./02-problem-statement.md)*

*Next: [Section 4: State of the World: CSP Offerings →](./04-csp-offerings.md)*

