# 9. Summary Table: Required Platform Services

---

This section provides a **consolidated reference table** mapping platform services to ownership, CSP involvement, portability risk, and regulatory drivers.

---

## 9.1 Agent Lifecycle Services

| Platform Service | Requirement | Owned By | Uses CSP | Portability Risk |
|------------------|-------------|----------|----------|------------------|
| **Agent Definition & Schema** | Portable, versioned agent definitions | Platform | No | None |
| **Agent Version Management** | Semantic versioning with lifecycle stages | Platform | No | None |
| **Training Specification** | Immutable configuration of capabilities and guardrails | Platform | No | None |
| **Employment Specification** | Delegated authority for specific context | Platform | No | None |
| **Agent Deployment Orchestration** | Automated, controlled deployment | Platform | Container Platforms | Low |
| **Agent Promotion Workflows** | Bank-compliant change management | Platform | No | None |
| **Agent Rollback** | State-aware version reversion | Platform | No | None |
| **Agent Retirement** | Graceful end-of-life with migration | Platform | No | None |

**Rationale:** Agent semantics must be CSP-independent. Banks require change management processes (OCC SR 11-7). Training immutability creates audit-defensible boundaries.

---

## 9.2 Identity & Authority Services

| Platform Service | Requirement | Owned By | Uses CSP | Portability Risk |
|------------------|-------------|----------|----------|------------------|
| **Agent Identity Issuance** | Unique, verifiable agent identifiers | Platform | No | None |
| **Agent Credential Management** | Secure credential lifecycle | Platform | Secrets Managers | Low |
| **Authority Definition** | Explicit statement of agent capabilities | Platform | No | None |
| **Delegation Chain Tracking** | Traceable authority provenance | Platform | No | None |
| **Ceiling Enforcement** | Hard limits on agent actions | Platform | No | None |
| **Kill Switch** | Instant authority revocation | Platform | No | None |
| **Authority Audit** | Immutable log of delegation changes | Platform | Storage | Low |
| **Layered Policy Hierarchy** | Bank → Class → Instance → Request | Platform | No | None |

**Rationale:** Banking regulations require clear accountability. "The system did it" is not acceptable. Authority ceilings prevent runaway actions.

---

## 9.3 Context & Reasoning Services

| Platform Service | Requirement | Owned By | Uses CSP | Portability Risk |
|------------------|-------------|----------|----------|------------------|
| **Context Assembly Engine** | Reproducible context compilation | Platform | No | None |
| **Retrieval Orchestration** | Coordinated multi-source retrieval | Platform | Vector DBs | Medium |
| **Context Ranking & Truncation** | Intelligent context prioritization | Platform | No | None |
| **Context Logging** | Captured context for reproducibility | Platform | Storage | Low |
| **Model Inference** | LLM reasoning | CSP | Yes (Bedrock, Azure OpenAI, Vertex) | Medium |
| **Model Failover** | Multi-provider resilience | Platform | Multiple CSPs | Low |

**Rationale:** Regulators may ask "what information was available when this decision was made?" Decisions must be reproducible.

---

## 9.4 Memory Services

| Platform Service | Requirement | Owned By | Uses CSP | Portability Risk |
|------------------|-------------|----------|----------|------------------|
| **Memory Type System** | Episodic, Semantic, Procedural, Preference | Platform | No | None |
| **Organizational Memory Store** | Long-lived, cross-agent memory | Platform | Database | Low |
| **Operational Memory Store** | Session/request-scoped memory | Platform | Database | Low |
| **Memory Scoping** | Tenant/customer/agent isolation | Platform | No | None |
| **Memory Lifecycle** | TTL, archival, deletion policies | Platform | No | None |
| **Memory Replication** | Cross-region sync | Platform | No | None |
| **Memory Export/Import** | Portability across environments | Platform | No | None |
| **Right to Erasure** | GDPR/CCPA compliant deletion | Platform | No | None |

**Rationale:** Right to be forgotten requires demonstrable deletion. Banks must control customer data lifecycle. Typed memory enables appropriate governance per class.

---

## 9.5 Knowledge & RAG Services

| Platform Service | Requirement | Owned By | Uses CSP | Portability Risk |
|------------------|-------------|----------|----------|------------------|
| **Knowledge Source Registry** | Catalog of authoritative sources | Platform | No | None |
| **Document Ingestion** | Content processing pipeline | Platform | Storage, Compute | Low |
| **Chunking & Indexing** | Retrieval-optimized segmentation | Platform | No | None |
| **Embedding Generation** | Semantic vectorization | CSP | Yes (Titan, ada-002, Gecko) | Medium |
| **Vector Storage** | Semantic search index | CSP | Yes (OpenSearch, AI Search) | Medium-High |
| **Semantic Search** | Query and retrieval | Platform | Vector DBs | Medium |
| **Source Attribution** | Provenance tracking | Platform | No | None |
| **Freshness Tracking** | Content currency indicators | Platform | No | None |

**Rationale:** Banks must know where information came from when defending decisions. Use pgvector where possible for portability.

---

## 9.6 Tool & Action Services

| Platform Service | Requirement | Owned By | Uses CSP | Portability Risk |
|------------------|-------------|----------|----------|------------------|
| **Tool Registry** | Catalog with schemas and versions | Platform | No | None |
| **Tool Permission Model** | Agent-tool entitlements | Platform | No | None |
| **Action Classification** | Read/Notify/Propose/Execute/Irreversible | Platform | No | None |
| **Execution Sandbox** | Isolated tool execution | Platform | Compute | Low |
| **Tool Invocation Logging** | Full audit trail | Platform | Storage | Low |
| **Rate Limiting** | Runaway prevention | Platform | No | None |
| **MCP Compatibility** | Open standard support | Platform | No | None |
| **Retry & Timeout** | Resilience handling | Platform | No | None |

**Rationale:** Banks must control and audit all actions. Irreversible actions require additional controls.

---

## 9.7 Cognitive Audit Fabric (CAF) Services

### 9.7.1 Decision Audit Services

| Platform Service | Requirement | Owned By | Uses CSP | Portability Risk |
|------------------|-------------|----------|----------|------------------|
| **Decision Record Creation** | Structured audit of every decision | Platform | No | None |
| **Context Snapshot Capture** | Preserved decision context | Platform | Storage | Low |
| **Outcome Tracking** | Decision-to-outcome linkage | Platform | No | None |
| **Causal Linking** | Record relationship management | Platform | No | None |
| **Immutability Enforcement** | Append-only, tamper-evident | Platform | No | None |
| **Content Hashing** | Cryptographic integrity verification | Platform | No | None |

### 9.7.2 Explanation Services

| Platform Service | Requirement | Owned By | Uses CSP | Portability Risk |
|------------------|-------------|----------|----------|------------------|
| **Real-Time Explanation Generation** | Explanation at decision time | Platform | No | None |
| **Factor Attribution** | Input impact analysis | Platform | No | None |
| **Multi-Audience Formatting** | Customer/operator/regulator views | Platform | No | None |
| **Counterfactual Support** | What-if analysis capability | Platform | No | None |
| **Natural Language Explanations** | Human-readable rationale | Platform | No | None |

### 9.7.3 Evidence Packaging Services

| Platform Service | Requirement | Owned By | Uses CSP | Portability Risk |
|------------------|-------------|----------|----------|------------------|
| **Evidence Bundle Creation** | Self-contained regulatory packages | Platform | No | None |
| **Context Reproduction** | Decision environment recreation | Platform | No | None |
| **Chain of Custody** | Traceable evidence handling | Platform | No | None |
| **Selective Export** | Subset disclosure capability | Platform | No | None |
| **Self-Describing Format** | Portable, interpretable packages | Platform | No | None |

### 9.7.4 Memory Governance Services

| Platform Service | Requirement | Owned By | Uses CSP | Portability Risk |
|------------------|-------------|----------|----------|------------------|
| **Memory Type Registry** | ESPP taxonomy management | Platform | No | None |
| **Retention Policy Enforcement** | Type-specific retention rules | Platform | No | None |
| **PII Exclusion Enforcement** | No PII in audit records | Platform | No | None |
| **Legal Hold Management** | Deletion suspension for litigation | Platform | No | None |
| **Long-Term Retention** | 7+ year storage with accessibility | Platform | Storage | Low |

### 9.7.5 Human Intervention Audit Services

| Platform Service | Requirement | Owned By | Uses CSP | Portability Risk |
|------------------|-------------|----------|----------|------------------|
| **Override Record Creation** | Document human overrides | Platform | No | None |
| **Intervention Context Capture** | Why and what was changed | Platform | No | None |
| **Directive Lifecycle Tracking** | Human directive resolution | Platform | No | None |
| **Escalation Audit** | Agent-to-human escalation records | Platform | No | None |
| **Handoff Context Preservation** | State transfer documentation | Platform | No | None |

### 9.7.6 Learning & Promotion Services

| Platform Service | Requirement | Owned By | Uses CSP | Portability Risk |
|------------------|-------------|----------|----------|------------------|
| **Pattern Detection** | Recurring pattern identification | Platform | No | None |
| **Hypothesis Formation** | Testable belief creation | Platform | No | None |
| **Knowledge Promotion Workflow** | Human-approved promotion | Platform | No | None |
| **Outcome Feedback Integration** | Decision-outcome learning | Platform | No | None |

**CAF Rationale:**
- **OCC SR 11-7:** Model Risk Management requires decision documentation
- **EU AI Act:** Explainability requirements for high-risk AI
- **Fair Lending:** Adverse action notices require decision explanations
- **Incident Response:** Understanding failures requires preserved context
- **Human Oversight:** Demonstrating humans remain in control

---

## 9.8 Governance & Control Services

| Platform Service | Requirement | Owned By | Uses CSP | Portability Risk |
|------------------|-------------|----------|----------|------------------|
| **Policy Definition** | Declarative governance rules | Platform | No | None |
| **Policy Enforcement** | Runtime policy application | Platform | Safety APIs (optional) | Low |
| **Guardrail Configuration** | Input/output safety rules | Platform | No | None |
| **Guardrail Immutability** | Training guardrails cannot be bypassed | Platform | No | None |
| **Approval Workflow Engine** | Human-in-loop routing | Platform | No | None |
| **Override Mechanism** | Surgical intervention with audit | Platform | No | None |
| **Dual Control Enforcement** | Multi-approval for sensitive actions | Platform | No | None |
| **Risk Scoring** | Dynamic risk assessment | Platform | No | None |
| **Kill Switch Execution** | Instant capability revocation | Platform | No | None |

**Rationale:** Human oversight is a regulatory expectation. Banks cannot delegate final authority for consequential decisions. Training guardrails create enforceable boundaries.

---

## 9.9 Runtime & Deployment Services

| Platform Service | Requirement | Owned By | Uses CSP | Portability Risk |
|------------------|-------------|----------|----------|------------------|
| **Container Orchestration** | Agent execution platform | CSP | Yes (EKS, AKS, GKE) | Low |
| **Deployment Orchestration** | Automated agent deployment | Platform | Container Platforms | Low |
| **Configuration Management** | Environment-specific config | Platform | No | None |
| **Scaling** | Load-based horizontal scaling | Platform | Container Platforms | Low |
| **Health Management** | Liveness, readiness checks | Platform | No | None |
| **Secrets Management** | Secure credential handling | Platform/CSP | Yes | Low |
| **Multi-Region Coordination** | Active-active deployment | Platform | No | None |
| **Graceful Degradation** | Predictable failure behavior | Platform | No | None |

**Rationale:** Kubernetes is portable standard. Zeta owns orchestration logic; CSPs provide compute.

---

## 9.10 Observability Services

| Platform Service | Requirement | Owned By | Uses CSP | Portability Risk |
|------------------|-------------|----------|----------|------------------|
| **Runtime Metrics** | Latency, throughput, errors | Platform | Metrics Backends | Low |
| **Cost Metrics** | Token and inference costs | Platform | No | None |
| **Health Indicators** | Agent health scores (AHS) | Platform | No | None |
| **Distributed Tracing** | End-to-end request traces | Platform | Tracing Backends | Low |
| **Log Aggregation** | Centralized, searchable logs | Platform | Log Backends | Low |
| **Alerting** | Threshold and anomaly alerts | Platform | Alert Managers | Low |
| **Dashboards** | Role-specific views | Platform | Dashboard Tools | Low |
| **OpenTelemetry Instrumentation** | Standard telemetry format | Platform | No | None |

**Rationale:** OpenTelemetry reduces lock-in. Cannot operate what cannot be observed.

---

## 9.11 Infrastructure Services (CSP-Provided)

| Platform Service | Requirement | Provider | Portability Risk |
|------------------|-------------|----------|------------------|
| **Container Orchestration** | Kubernetes | CSP (EKS, AKS, GKE) | Low |
| **Object Storage** | Blob storage | CSP (S3, Blob, GCS) | Low |
| **Relational Database** | PostgreSQL | CSP (RDS, Azure SQL, CloudSQL) | Low |
| **Secrets Management** | Secure secrets | CSP/Vault | Low |
| **Networking** | VPC, Load Balancing | CSP | Low |
| **Observability Infrastructure** | Metrics, Logs, Traces | CSP (CloudWatch, Azure Monitor) | Medium |

**Rationale:** These are commodity services with portable standards (Kubernetes, S3 API, PostgreSQL).

---

## 9.12 Summary Matrix

### Ownership Summary

| Ownership Category | Count | Examples |
|-------------------|-------|----------|
| **Platform Only** | 50+ | Agent schema, authority, CAF records, governance |
| **Platform + CSP Infrastructure** | 15+ | Deployment, storage, observability |
| **CSP Primary** | 8-10 | Model inference, container orchestration, object storage |

### Portability Risk Summary

| Risk Level | Count | Mitigation |
|------------|-------|------------|
| **None** | 45+ | Platform owns completely; no CSP dependency |
| **Low** | 20+ | Uses CSP infra through abstraction layer |
| **Medium** | 8-10 | Requires adapter development; manageable effort |
| **Medium-High** | 3-5 | Vector DBs, embeddings; prefer portable options |
| **High** | 0 | No high-risk services if platform owns control plane |

### CAF-Specific Summary

| CAF Capability | Services | Risk Level |
|----------------|----------|------------|
| **Decision Audit** | 6 services | None |
| **Explanation** | 5 services | None |
| **Evidence Packaging** | 5 services | None |
| **Memory Governance** | 5 services | None (storage: Low) |
| **Human Intervention Audit** | 5 services | None |
| **Learning & Promotion** | 4 services | None |

---

## 9.13 Strategic Insight

The tables demonstrate that **platform ownership concentrates in the semantic layer**:

- Agent identity and authority
- Memory types and governance
- Audit records and evidence
- Governance and policy
- Explanation and learning

While **CSP dependency concentrates in the infrastructure layer**:

- Compute (containers, serverless)
- Storage (object, relational, vector)
- Models (inference APIs)

This separation validates the platform strategy:

> **Platform owns the control plane; CSPs provide the substrate.**

### CAF as Strategic Differentiator

The Cognitive Audit Fabric represents the **highest concentration of platform-owned services**:

| CAF Services | Ownership |
|--------------|-----------|
| 30 services | Platform-only |
| 1 service | Low-risk CSP dependency (storage) |

CAF is the component where CSP offerings are **most deficient** and where **regulatory requirements are most stringent**. This makes CAF a key differentiator and a non-negotiable platform investment.

---

## 9.14 Decision Framework

When evaluating whether to build, buy, or abstract a capability:

| Question | If Yes → Platform Owns | If No → CSP/Abstract |
|----------|------------------------|---------------------|
| Does it define agent behavior? | Build | — |
| Does it affect regulatory compliance? | Build | — |
| Does it create CSP lock-in if CSP-owned? | Build or Abstract | — |
| Is it commodity infrastructure? | — | Use CSP |
| Is there a portable standard? | Adopt standard | — |
| Does bank need to customize it? | Build | — |
| Is it part of CAF? | Build | — |

---

*Previous: [Section 8: Platform Components & Design Rationale](./08-platform-components.md)*

*Next: [Section 10: Product & Go-To-Market Implications →](./10-gtm-implications.md)*

