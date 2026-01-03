# 9. Summary Table: Required Platform Services

---

This section provides a **consolidated reference table** mapping platform services to ownership, CSP involvement, portability risk, and rationale.

---

## 9.1 Platform Services Overview

| Platform Service | Owned By | Uses CSP | Portability Risk | Rationale |
|------------------|----------|----------|------------------|-----------|
| **Agent Definition & Schema** | Zeta | No | None | Agent semantics must be CSP-independent |
| **Agent Version Management** | Zeta | No | None | Lifecycle is product concern, not infra |
| **Agent Deployment Orchestration** | Zeta | Container Platforms | Low | Kubernetes is portable; Zeta owns orchestration logic |
| **Agent Promotion Workflows** | Zeta | No | None | Change management is bank requirement |
| **Agent Rollback** | Zeta | No | None | State-aware rollback is Zeta responsibility |
| **Agent Retirement** | Zeta | No | None | Product lifecycle is Zeta owned |

---

## 9.2 Identity & Authority Services

| Platform Service | Owned By | Uses CSP | Portability Risk | Rationale |
|------------------|----------|----------|------------------|-----------|
| **Agent Identity Issuance** | Zeta | No | None | Agents have Zeta identity, not CSP IAM |
| **Agent Credential Management** | Zeta | Secrets Managers | Low | Abstracted; Vault or CSP secrets |
| **Authority Definition** | Zeta | No | None | Banking authority model is unique |
| **Delegation Chain Tracking** | Zeta | No | None | Required for regulatory accountability |
| **Ceiling Enforcement** | Zeta | No | None | Action limits are Zeta enforced |
| **Kill Switch** | Zeta | No | None | Instant revocation is non-negotiable |
| **Authority Audit** | Zeta | Storage | Low | Stored portably; CSP is storage only |

---

## 9.3 Context & Reasoning Services

| Platform Service | Owned By | Uses CSP | Portability Risk | Rationale |
|------------------|----------|----------|------------------|-----------|
| **Context Assembly Engine** | Zeta | No | None | Reproducibility requires Zeta control |
| **Retrieval Orchestration** | Zeta | Vector DBs | Medium | Abstracted; interface owned by Zeta |
| **Context Truncation Policy** | Zeta | No | None | Model-aware truncation is Zeta logic |
| **Context Logging** | Zeta | Storage | Low | Stored portably |
| **Model Inference** | CSP | Yes (Bedrock, Azure OpenAI, Vertex) | Medium | Abstracted via model interface |
| **Model Failover** | Zeta | Multiple CSPs | Low | Zeta decides failover; CSPs provide models |

---

## 9.4 Memory Services

| Platform Service | Owned By | Uses CSP | Portability Risk | Rationale |
|------------------|----------|----------|------------------|-----------|
| **Episodic Memory Store** | Zeta | Database | Low | Schema and lifecycle are Zeta owned |
| **Semantic Memory Store** | Zeta | Database | Low | Schema and lifecycle are Zeta owned |
| **Preference Memory Store** | Zeta | Database | Low | Schema and lifecycle are Zeta owned |
| **Memory Scoping (Tenant/Customer)** | Zeta | No | None | Isolation is Zeta responsibility |
| **Memory Replication** | Zeta | No | None | Cross-region sync is Zeta managed |
| **Memory Export/Import** | Zeta | No | None | Portability feature is Zeta owned |
| **Memory Deletion (GDPR/CCPA)** | Zeta | No | None | Compliance requires Zeta control |

---

## 9.5 Knowledge & RAG Services

| Platform Service | Owned By | Uses CSP | Portability Risk | Rationale |
|------------------|----------|----------|------------------|-----------|
| **Knowledge Source Registry** | Zeta | No | None | Source definitions are Zeta owned |
| **Document Ingestion** | Zeta | Storage, Compute | Low | Processing logic is Zeta; infra is CSP |
| **Chunking & Indexing** | Zeta | No | None | Chunking strategy is Zeta decision |
| **Embedding Generation** | CSP | Yes (Titan, ada-002, Gecko) | Medium | Abstracted; embeddings may need regeneration on switch |
| **Vector Storage** | CSP | Yes (OpenSearch, AI Search, Vector Search) | Medium-High | Use pgvector where possible for portability |
| **Semantic Search** | Zeta | Vector DBs | Medium | Query logic is Zeta; vector DB is swappable |
| **Source Attribution** | Zeta | No | None | Provenance is Zeta responsibility |

---

## 9.6 Tool & Action Services

| Platform Service | Owned By | Uses CSP | Portability Risk | Rationale |
|------------------|----------|----------|------------------|-----------|
| **Tool Registry** | Zeta | No | None | Tool definitions are Zeta owned |
| **Tool Permission Model** | Zeta | No | None | Authority enforcement is Zeta |
| **Tool Execution Sandbox** | Zeta | Compute | Low | Sandbox logic is Zeta; containers are CSP |
| **Tool Invocation Logging** | Zeta | Storage | Low | Audit is Zeta responsibility |
| **MCP Compatibility** | Zeta | No | None | Open standard support |
| **Tool Retry & Timeout** | Zeta | No | None | Resilience logic is Zeta owned |

---

## 9.7 Audit & Evidence Services

| Platform Service | Owned By | Uses CSP | Portability Risk | Rationale |
|------------------|----------|----------|------------------|-----------|
| **Decision Record Creation** | Zeta | No | None | Audit structure is Zeta defined |
| **Explanation Generation** | Zeta | No | None | Explainability is Zeta responsibility |
| **Evidence Packaging** | Zeta | No | None | Regulatory response is Zeta owned |
| **Immutable Log Storage** | Zeta | Storage | Low | Immutability enforced by Zeta; storage is CSP |
| **Long-term Retention** | Zeta | Storage | Low | Lifecycle is Zeta managed |
| **Audit Query & Search** | Zeta | No | None | Query logic is Zeta owned |
| **Audit Export** | Zeta | No | None | Self-describing format |

---

## 9.8 Governance & Control Services

| Platform Service | Owned By | Uses CSP | Portability Risk | Rationale |
|------------------|----------|----------|------------------|-----------|
| **Policy Definition** | Zeta | No | None | Policies are bank-specific, Zeta owned |
| **Policy Enforcement** | Zeta | Safety APIs (optional) | Low | Can use CSP guardrails as accelerators |
| **Guardrail Configuration** | Zeta | No | None | Guardrail rules are Zeta defined |
| **Approval Workflow Engine** | Zeta | No | None | Human-in-loop is banking requirement |
| **Override Mechanism** | Zeta | No | None | Human control is non-negotiable |
| **Dual Control Enforcement** | Zeta | No | None | Banking control pattern |
| **Risk Scoring** | Zeta | No | None | Risk assessment is Zeta logic |

---

## 9.9 Infrastructure Services

| Platform Service | Owned By | Uses CSP | Portability Risk | Rationale |
|------------------|----------|----------|------------------|-----------|
| **Container Orchestration** | CSP | Yes (EKS, AKS, GKE) | Low | Kubernetes is portable standard |
| **Object Storage** | CSP | Yes (S3, Blob, GCS) | Low | S3 API is de facto standard |
| **Relational Database** | CSP | Yes (RDS, Azure SQL, CloudSQL) | Low | PostgreSQL is portable |
| **Secrets Management** | CSP/Vault | Yes | Low | Abstracted via Vault or CSP |
| **Networking** | CSP | Yes | Low | Standard networking primitives |
| **Load Balancing** | CSP | Yes | Low | Standard load balancer APIs |
| **Observability Infrastructure** | CSP | Yes (CloudWatch, Azure Monitor, Cloud Logging) | Medium | OpenTelemetry reduces lock-in |

---

## 9.10 Summary Matrix

### Ownership Summary

| Ownership Category | Count | Examples |
|-------------------|-------|----------|
| **Zeta Only** | 35+ | Agent schema, authority, memory, audit, governance |
| **Zeta + CSP Infrastructure** | 15+ | Deployment (Zeta logic + Kubernetes), storage (Zeta schema + DB) |
| **CSP Primary** | 8-10 | Model inference, container orchestration, object storage |

### Portability Risk Summary

| Risk Level | Count | Mitigation |
|------------|-------|------------|
| **None** | 25+ | Zeta owns completely; no CSP dependency |
| **Low** | 15+ | Uses CSP infra through abstraction layer |
| **Medium** | 8-10 | Requires adapter development; some effort to switch |
| **Medium-High** | 3-5 | Vector DBs, embeddings; prefer portable options |
| **High** | 0 | No high-risk services if Zeta owns control plane |

### Strategic Insight

The table demonstrates that **Zeta ownership concentrates in the semantic layer**:

- Agent identity and authority
- Memory and state
- Audit and evidence
- Governance and policy

While **CSP dependency concentrates in the infrastructure layer**:

- Compute (containers, serverless)
- Storage (object, relational, vector)
- Models (inference APIs)

This separation validates the platform strategy: **Zeta owns the control plane; CSPs provide the substrate.**

---

## 9.11 Decision Framework

When evaluating whether to build, buy, or abstract a capability, use this framework:

| Question | If Yes → Zeta Owns | If No → CSP/Abstract |
|----------|-------------------|---------------------|
| Does it define agent behavior? | Build | — |
| Does it affect regulatory compliance? | Build | — |
| Does it create CSP lock-in if CSP-owned? | Build or Abstract | — |
| Is it commodity infrastructure? | — | Use CSP |
| Is there a portable standard? | Adopt standard | — |
| Does bank need to customize it? | Build | — |

---

*Previous: [Section 8: Platform Components & Design Rationale](./08-platform-components.md)*

*Next: [Section 10: Product & Go-To-Market Implications →](./10-gtm-implications.md)*

