# 11. Explicit Non-Goals and Boundaries

---

This section defines **what Zeta will not build**. Clear boundaries prevent scope creep, focus engineering investment, and avoid accidental competition with partners. Being explicit about non-goals is as important as being clear about goals.

---

## 11.1 What Zeta Will Not Build

### Foundation Models

| Non-Goal | Rationale |
|----------|-----------|
| **Training foundation models** | Massive capital requirement; not Zeta's competitive advantage; CSPs do this well |
| **Fine-tuning infrastructure** | CSPs provide this; Zeta can use it through abstraction |
| **Model hosting/serving** | CSPs do this at scale; Zeta focuses on orchestration layer |
| **Model optimization (quantization, etc.)** | Model providers handle this; Zeta consumes optimized models |

**Position:** Zeta is a **consumer of models**, not a producer. Foundation model development requires billions in capital and specialized expertise. Zeta's value is in the layers above.

**What Zeta does do:**
- Abstract model access through portable interfaces
- Manage model selection and failover
- Handle model-specific configuration

### General-Purpose AI Platforms

| Non-Goal | Rationale |
|----------|-----------|
| **General ML training platform** | SageMaker, Azure ML, Vertex AI exist; not differentiated |
| **General data science workbench** | Not Zeta's focus; banks have existing tools |
| **General chatbot platform** | Zeta builds agents, not chatbots; distinction matters |
| **General RAG platform** | RAG is a component, not the product |

**Position:** Zeta builds **banking-specific agentic products**, not horizontal AI infrastructure.

### Infrastructure Services

| Non-Goal | Rationale |
|----------|-----------|
| **Cloud infrastructure** | CSPs provide compute, storage, networking; Zeta uses it |
| **Container orchestration** | Kubernetes exists; Zeta deploys to it |
| **Observability infrastructure** | Datadog, CloudWatch, etc. exist; Zeta integrates |
| **Identity provider** | Banks have identity systems; Zeta integrates |
| **Secret management** | Vault, CSP secrets exist; Zeta uses them |

**Position:** Zeta **uses infrastructure**, not replaces it. Every infrastructure layer Zeta builds is one more thing to maintain.

### CSP-Specific Optimizations

| Non-Goal | Rationale |
|----------|-----------|
| **Deep CSP-native integration** | Creates lock-in; conflicts with portability principle |
| **CSP-specific agent formats** | Portability requires abstraction |
| **CSP marketplace offerings** | Zeta distributes through own channels |

**Position:** Zeta maintains **arm's-length relationship** with CSP-specific features. Deep integration is a trap.

---

## 11.2 What Zeta Will Deliberately Rely on CSPs For

### Compute and Orchestration

| Capability | CSP Dependency | Zeta's Role |
|------------|----------------|-------------|
| **Container orchestration** | EKS, AKS, GKE | Deploy agents to Kubernetes |
| **Serverless functions** | Lambda, Azure Functions, Cloud Functions | Invoke for lightweight tasks |
| **Batch processing** | CSP batch services | Use for async processing |

### Model Inference

| Capability | CSP Dependency | Zeta's Role |
|------------|----------------|-------------|
| **Foundation model APIs** | Bedrock, Azure OpenAI, Vertex AI | Consume through abstraction layer |
| **Embedding generation** | CSP embedding models | Use through model interface |
| **Model fine-tuning** | CSP fine-tuning services | Configure; results portable |

### Storage

| Capability | CSP Dependency | Zeta's Role |
|------------|----------------|-------------|
| **Object storage** | S3, Blob, GCS | Store documents, artifacts |
| **Relational database** | RDS, Azure SQL, CloudSQL | Use PostgreSQL portably |
| **Vector storage** | OpenSearch, AI Search, pgvector | Abstract behind interface |

### Networking and Security

| Capability | CSP Dependency | Zeta's Role |
|------------|----------------|-------------|
| **VPC/VNET** | CSP networking | Deploy within customer network |
| **Load balancing** | CSP load balancers | Use for traffic distribution |
| **Certificate management** | CSP certificate services | Use for TLS |
| **DDoS protection** | CSP edge services | Rely on CSP protection |

### Observability Infrastructure

| Capability | CSP Dependency | Zeta's Role |
|------------|----------------|-------------|
| **Log collection** | CloudWatch, Azure Monitor, Cloud Logging | Send logs; integrate |
| **Metrics** | CSP metrics services | Emit metrics; integrate |
| **Tracing** | X-Ray, Application Insights, Cloud Trace | Use OpenTelemetry; integrate |

---

## 11.3 Avoiding Platform Sprawl

### The Platform Sprawl Anti-Pattern

Platform teams often fall into the trap of building too much:

```
Year 1: "We need an agent platform"
Year 2: "We need our own vector database"
Year 3: "We need our own model serving"
Year 4: "We need our own Kubernetes distribution"
Year 5: "We need our own cloud"
```

Each layer adds:
- Engineering headcount
- Maintenance burden
- Opportunity cost
- Customer integration complexity

### Zeta's Boundary Discipline

| When tempted to build... | Instead... |
|--------------------------|------------|
| Custom vector database | Abstract the interface; use existing DBs |
| Custom model serving | Use CSP model APIs; abstract the interface |
| Custom observability | Integrate with existing tools via OpenTelemetry |
| Custom identity | Integrate with bank identity systems |
| Custom Kubernetes | Use managed Kubernetes |

### Decision Framework

Before building any new capability, ask:

1. **Does this directly serve agent product value?** If not, don't build.
2. **Does a good-enough alternative exist?** If yes, integrate.
3. **Does building this create customer value or engineering burden?** If burden > value, don't build.
4. **Does this require specialized expertise we don't have?** If yes, don't build.
5. **Will maintaining this distract from core platform?** If yes, don't build.

---

## 11.4 Avoiding Accidental Lock-In

### Lock-In Zeta Must Avoid Creating

Irony: A platform designed to avoid CSP lock-in could create Zeta lock-in.

| Potential Lock-In | Prevention |
|-------------------|------------|
| **Proprietary agent format** | Use declarative, well-documented schema; provide export tools |
| **Proprietary memory format** | Store in standard formats; provide export/import |
| **Proprietary protocol** | Adopt open standards (MCP, OpenTelemetry) where available |
| **Undocumented APIs** | Publish API specifications; version responsibly |
| **Non-portable state** | All state exportable; migration paths documented |

### Customer Exit Rights

Zeta should explicitly support:

| Exit Right | Implementation |
|------------|----------------|
| **Export agent definitions** | CLI/API for full export |
| **Export memory** | Bulk export in portable format |
| **Export audit logs** | Self-describing archive format |
| **Export configuration** | GitOps-compatible format |
| **Migration assistance** | Documented procedures; optional services |

**Why this matters:** Customers who know they can leave are more likely to stay. Lock-in creates customer anxiety, not loyalty.

---

## 11.5 What Zeta Might Build Later (But Not Now)

Some capabilities are out of scope for initial platform but may become relevant:

| Capability | Why Not Now | Potential Future Trigger |
|------------|-------------|--------------------------|
| **Agent marketplace** | Focus on platform first | Customer demand for pre-built agents |
| **Low-code agent builder** | Enterprise focus; code-first | Mid-market demand |
| **Model evaluation framework** | CSPs provide this | Differentiation opportunity |
| **Synthetic data generation** | Not core to agents | Training/testing demand |
| **Agent simulation/testing** | Build basic first | Enterprise testing demand |
| **Multi-agent coordination** | Complex; maturing field | Industry standards emerge |

### Evaluation Criteria for Future Additions

When considering expanding scope:

1. **Customer demand** — Are multiple customers asking for this?
2. **Strategic fit** — Does this reinforce or dilute platform value?
3. **Competitive necessity** — Is this becoming table stakes?
4. **Build vs. partner** — Can a partner do this better?
5. **Resource availability** — Do we have capacity without harming core?

---

## 11.6 Relationship with Banking Products

### Zeta Agent Platform vs. Zeta Banking Products

| Layer | Ownership | Examples |
|-------|-----------|----------|
| **Agent Platform** | Zeta Platform Team | Lifecycle, memory, audit, governance |
| **Agent Products** | Zeta Product Teams | Collections agent, Advisor agent, Compliance agent |
| **Customer Agents** | Banks | Custom agents built on platform |

### Platform's Role

The platform should:

- **Enable** Zeta product teams to build agents faster
- **Enable** banks to build custom agents
- **Not** dictate product-level decisions
- **Not** become a blocker for product innovation

### What Platform Provides to Products

| Platform Capability | Product Benefit |
|---------------------|-----------------|
| Agent lifecycle | Products deploy reliably |
| Memory system | Products have persistent state |
| Audit fabric | Products are compliance-ready |
| Governance | Products have built-in controls |
| Tool framework | Products can integrate with bank systems |

### What Platform Does Not Dictate

| Product Decision | Platform Role |
|------------------|---------------|
| Agent use case | Products define |
| Agent prompts and behavior | Products define |
| Customer-facing UX | Products define |
| Pricing | Products define |
| Industry-specific logic | Products define |

---

## 11.7 Summary: The Boundaries

### Zeta Will Build

✅ Agent lifecycle and versioning
✅ Agent identity and authority
✅ Context assembly and orchestration
✅ Persistent, portable memory
✅ Knowledge integration (RAG orchestration)
✅ Tool and action framework
✅ Audit and evidence fabric
✅ Governance and override layer
✅ Runtime abstraction
✅ Multi-cloud deployment capability

### Zeta Will Not Build

❌ Foundation models
❌ Model training infrastructure
❌ General ML platforms
❌ Container orchestration
❌ Database engines
❌ Observability infrastructure
❌ Identity providers
❌ Cloud infrastructure

### Zeta Will Use But Not Own

⚡ CSP compute (EKS, AKS, GKE)
⚡ CSP storage (S3, Blob, GCS, PostgreSQL)
⚡ CSP models (Bedrock, Azure OpenAI, Vertex AI)
⚡ CSP observability (CloudWatch, Azure Monitor, Cloud Logging)
⚡ Open standards (Kubernetes, OpenTelemetry, MCP)

---

## 11.8 Final Word on Boundaries

Discipline about boundaries is a strategic advantage:

1. **Focus** — Engineering effort goes to differentiated capabilities
2. **Speed** — Less to build means faster to market
3. **Reliability** — Using mature infrastructure reduces risk
4. **Partnerships** — Clear boundaries enable CSP and SI partnerships
5. **Customer confidence** — Clear scope reduces buyer uncertainty

> "What you choose not to build is as important as what you build."

---

*Previous: [Section 10: Product & Go-To-Market Implications](./10-gtm-implications.md)*

*Next: [Appendix A: Regulatory & Legal Considerations →](./appendix-a-regulatory.md)*

