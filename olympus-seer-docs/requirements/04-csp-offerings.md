# 4. State of the World: CSP Offerings for Agentic AI

---

This section provides a **factual comparison** of what AWS, Azure, and Google Cloud offer for building agentic AI systems. For each capability area, we assess:

- **What the CSP provides**
- **Where it excels**
- **Lock-in risk** (Low / Medium / High) and why

This is not marketing—it is an honest assessment to inform Zeta's platform strategy.

---

## 4.1 Overview of CSP Agentic AI Stacks

### AWS

| Layer | Services |
|-------|----------|
| **Foundation Models** | [Amazon Bedrock](https://aws.amazon.com/bedrock/) (Claude, Llama, Titan, Mistral, Cohere) |
| **Agent Framework** | [Bedrock Agents](https://docs.aws.amazon.com/bedrock/latest/userguide/agents.html), [Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/) |
| **Knowledge/RAG** | [Bedrock Knowledge Bases](https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base.html), OpenSearch Serverless |
| **ML Ops** | [SageMaker](https://aws.amazon.com/sagemaker/) |
| **Vector Search** | OpenSearch Serverless, Aurora pgvector, Neptune Analytics |
| **Guardrails** | [Bedrock Guardrails](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails.html) |
| **Observability** | CloudWatch, X-Ray, Bedrock Model Invocation Logging |

### Azure

| Layer | Services |
|-------|----------|
| **Foundation Models** | [Azure OpenAI Service](https://azure.microsoft.com/en-us/products/ai-services/openai-service) (GPT-4, GPT-4o, o1, o3), Azure AI Model Catalog |
| **Agent Framework** | [Azure AI Agent Service](https://azure.microsoft.com/en-us/products/ai-services/ai-agent-service/), [Azure AI Foundry](https://azure.microsoft.com/en-us/products/ai-foundry/) |
| **Knowledge/RAG** | [Azure AI Search](https://azure.microsoft.com/en-us/products/ai-services/ai-search/), Cosmos DB Vector Search |
| **ML Ops** | [Azure Machine Learning](https://azure.microsoft.com/en-us/products/machine-learning/) |
| **Vector Search** | Azure AI Search, Cosmos DB for MongoDB vCore, PostgreSQL Flexible Server (pgvector) |
| **Guardrails** | Azure AI Content Safety, Azure OpenAI content filtering |
| **Observability** | Azure Monitor, Application Insights, Azure AI Evaluation |

### Google Cloud

| Layer | Services |
|-------|----------|
| **Foundation Models** | [Vertex AI](https://cloud.google.com/vertex-ai) (Gemini, PaLM, Claude, Llama) |
| **Agent Framework** | [Vertex AI Agent Builder](https://cloud.google.com/products/agent-builder), [Agent Development Kit (ADK)](https://google.github.io/adk-docs/) |
| **Knowledge/RAG** | Vertex AI Search, Vertex AI Grounding |
| **ML Ops** | Vertex AI Pipelines, Model Registry, Feature Store |
| **Vector Search** | [Vertex AI Vector Search](https://cloud.google.com/vertex-ai/docs/vector-search/overview), AlloyDB with pgvector |
| **Guardrails** | Vertex AI Safety Settings, Model Armor |
| **Observability** | Cloud Logging, Cloud Trace, Vertex AI Model Monitoring |

---

## 4.2 Data & Knowledge Stack Comparison

### Object Storage and Data Lakes

| Capability | AWS | Azure | GCP | Lock-in Risk |
|------------|-----|-------|-----|--------------|
| **Object Storage** | S3 | Blob Storage | Cloud Storage | **Low** — S3 API is de facto standard |
| **Data Lake Format** | Lake Formation, Iceberg support | Azure Data Lake Gen2, Delta Lake | BigLake, Iceberg support | **Medium** — Metadata formats differ |
| **Cross-region Replication** | Native | Native | Native | **Low** — Standard feature |

**Assessment:** Object storage is commoditized. S3-compatible APIs make portability feasible. **Lock-in risk is Low** for raw storage.

### Feature Stores

| Capability | AWS | Azure | GCP | Lock-in Risk |
|------------|-----|-------|-----|--------------|
| **Service** | SageMaker Feature Store | Azure ML Feature Store | Vertex AI Feature Store | **High** |
| **Format** | Proprietary | Proprietary | Proprietary | |
| **Portability** | Export to Parquet | Export to Parquet | Export to Parquet | |

**Assessment:** Feature store metadata and pipelines are deeply CSP-specific. The data is portable (Parquet), but the **operational logic is not**. **Lock-in risk is High.**

### Vector Databases and Semantic Search

| Capability | AWS | Azure | GCP | Lock-in Risk |
|------------|-----|-------|-----|--------------|
| **Managed Vector DB** | OpenSearch Serverless | Azure AI Search | Vertex AI Vector Search | **Medium-High** |
| **Open-source Option** | Aurora pgvector | PostgreSQL Flex pgvector | AlloyDB pgvector | **Low** |
| **Embedding Generation** | Bedrock (Titan Embeddings) | Azure OpenAI (ada-002) | Vertex AI (Gecko, etc.) | **Medium** |

**Assessment:** 
- **Managed vector DBs** have CSP-specific APIs and operational models. Lock-in risk is **Medium-High**.
- **pgvector on PostgreSQL** is portable and open-source. Lock-in risk is **Low**.
- **Embedding models** produce CSP-specific vectors that may not be interchangeable. Consider embedding portability in architecture.

### RAG / Knowledge Base Services

| Capability | AWS | Azure | GCP | Lock-in Risk |
|------------|-----|-------|-----|--------------|
| **Service** | Bedrock Knowledge Bases | Azure AI Search + OpenAI | Vertex AI Search, Grounding | **High** |
| **Connectors** | S3, Web, Confluence | Blob, SharePoint, SQL | GCS, BigQuery, web | **High** |
| **Chunking/Indexing** | Managed | Managed | Managed | **High** |

**Assessment:** RAG services are **tightly coupled** to CSP storage, indexing, and model inference. Chunking strategies, metadata schemas, and retrieval configurations are CSP-specific. **Lock-in risk is High.**

**Recommendation:** Zeta should own the RAG orchestration layer, using CSP vector DBs as swappable backends.

---

## 4.3 ML Ops & Model Lifecycle Comparison

### Training and Fine-tuning

| Capability | AWS | Azure | GCP | Lock-in Risk |
|------------|-----|-------|-----|--------------|
| **Fine-tuning Support** | Bedrock Custom Models, SageMaker | Azure OpenAI Fine-tuning, Azure ML | Vertex AI Tuning | **High** |
| **Training Infrastructure** | SageMaker, EC2 (P5, Trainium) | Azure ML, ND-series VMs | Vertex AI, TPUs, A3 VMs | **Medium** |
| **BYOM (Bring Your Own Model)** | SageMaker, Bedrock Custom Import | Azure ML | Vertex AI Model Garden | **Medium** |

**Assessment:** Fine-tuning configurations and checkpoints are CSP-specific. Training infrastructure is portable at the container level (CUDA/PyTorch), but managed services add friction. **Lock-in risk is High for fine-tuning, Medium for training.**

### Model Registry and Promotion

| Capability | AWS | Azure | GCP | Lock-in Risk |
|------------|-----|-------|-----|--------------|
| **Registry** | SageMaker Model Registry | Azure ML Model Registry | Vertex AI Model Registry | **High** |
| **Versioning** | Native | Native | Native | |
| **Promotion Workflows** | SageMaker Pipelines | Azure ML Pipelines | Vertex AI Pipelines | **High** |

**Assessment:** Model registries are CSP-specific. Metadata, lineage, and promotion rules do not transfer. **Lock-in risk is High.**

### Monitoring and Drift Detection

| Capability | AWS | Azure | GCP | Lock-in Risk |
|------------|-----|-------|-----|--------------|
| **Model Monitoring** | SageMaker Model Monitor | Azure ML Data Drift | Vertex AI Model Monitoring | **High** |
| **Metrics** | CSP-specific | CSP-specific | CSP-specific | |
| **Alerts** | CloudWatch | Azure Monitor | Cloud Monitoring | **Low** |

**Assessment:** Drift detection baselines and thresholds are CSP-specific. Alerting infrastructure is more portable. **Lock-in risk is High for monitoring logic, Low for alerting.**

---

## 4.4 Agent Build & Composition Capabilities

### Native Agent Builders

| Capability | AWS | Azure | GCP | Lock-in Risk |
|------------|-----|-------|-----|--------------|
| **Service** | Bedrock Agents | Azure AI Agent Service | Vertex AI Agent Builder | **Very High** |
| **Definition Format** | AWS-specific JSON/API | Azure-specific API | Google-specific API | **Very High** |
| **State Management** | Session-scoped | Session-scoped | Session-scoped | |
| **Memory** | Limited (session memory) | Limited (conversation history) | Limited (context) | |

**Assessment:** Native agent builders are the **highest lock-in services**. Agent definitions, orchestration logic, and state management are entirely CSP-specific. There is **no portability path** between CSP agent frameworks.

### Tool/Function Integration

| Capability | AWS | Azure | GCP | Lock-in Risk |
|------------|-----|-------|-----|--------------|
| **Tool Definition** | Action Groups (Lambda/API) | Function Calling + Azure Functions | Extensions, Function Calling | **Medium** |
| **API Gateway Integration** | Native | Native | Native | **Low** |
| **MCP Support** | Via AgentCore | Limited | Via ADK | **Low** (MCP is open) |

**Assessment:** Tool integration is more portable than agent definition. [Model Context Protocol (MCP)](https://modelcontextprotocol.io/) offers an open standard. Lambda/Functions are interchangeable at the conceptual level. **Lock-in risk is Medium**, reducible with abstraction.

### Planning and Orchestration

| Capability | AWS | Azure | GCP | Lock-in Risk |
|------------|-----|-------|-----|--------------|
| **Orchestration** | Bedrock Agent runtime | Azure AI Agent Service | Agent Engine | **Very High** |
| **Multi-agent** | Limited | Preview (multi-agent) | Preview (multi-agent) | **Very High** |
| **Workflow Integration** | Step Functions | Logic Apps, Durable Functions | Workflows | **High** |

**Assessment:** Agent orchestration is deeply coupled to CSP runtimes. Multi-agent coordination is nascent and entirely CSP-specific. **Lock-in risk is Very High.**

### Memory Primitives

| Capability | AWS | Azure | GCP | Lock-in Risk |
|------------|-----|-------|-----|--------------|
| **What's Called "Memory"** | Session memory, Knowledge Bases | Conversation history | Context, Search | **Very High** |
| **Persistence** | Session-scoped | Session-scoped | Session-scoped | |
| **Long-term Memory** | Not native; requires custom | Not native; requires custom | Not native; requires custom | |

**Assessment:** CSP "memory" is **not agent memory** in the product sense. It is session-scoped context or retrieval. **True persistent memory must be Zeta-owned.** Lock-in risk is **Very High** if you rely on CSP memory semantics.

---

## 4.5 Agent Runtime & Deployment Capabilities

### Managed Agent Runtimes

| Capability | AWS | Azure | GCP | Lock-in Risk |
|------------|-----|-------|-----|--------------|
| **Service** | Bedrock Agent Runtime | Azure AI Agent Service | Agent Engine | **Very High** |
| **Deployment Model** | Managed (opaque) | Managed (opaque) | Managed (opaque) | |
| **Customization** | Limited | Limited | Limited | |
| **Self-hosted Option** | Not for Bedrock Agents | Not for Agent Service | ADK can self-host | **Low for ADK** |

**Assessment:** Managed agent runtimes offer limited visibility into internal orchestration. Customization is constrained to provider-defined options, and migration paths to other platforms are not supported. **Lock-in risk is Very High**, except for GCP's ADK which can run outside GCP.

### Serverless vs. Container-based Execution

| Capability | AWS | Azure | GCP | Lock-in Risk |
|------------|-----|-------|-----|--------------|
| **Serverless Compute** | Lambda | Azure Functions | Cloud Functions, Cloud Run | **Low** (conceptually portable) |
| **Container Orchestration** | EKS, ECS, Fargate | AKS | GKE, Cloud Run | **Low** (Kubernetes is portable) |
| **Agent Workloads** | Mix of managed + Lambda | Mix of managed + Functions | Mix of managed + Cloud Run | |

**Assessment:** Container-based execution (Kubernetes) is portable. Serverless functions are conceptually similar but require adaptation. **Lock-in risk is Low** for compute, separate from agent framework lock-in.

### Regional and Cross-Region Behavior

| Capability | AWS | Azure | GCP | Lock-in Risk |
|------------|-----|-------|-----|--------------|
| **Multi-region Agents** | Manual (deploy per region) | Manual (deploy per region) | Manual (deploy per region) | **Low** |
| **Global Model Availability** | Varies by model | Varies by model | Varies by model | **Medium** |
| **State Replication** | Customer responsibility | Customer responsibility | Customer responsibility | |

**Assessment:** CSPs do not provide multi-region agent orchestration. State replication across regions is customer-owned. **Lock-in risk is Low**, but effort is high.

---

## 4.6 Safety, Guardrails, and Policy Tooling

### Content Safety APIs

| Capability | AWS | Azure | GCP | Lock-in Risk |
|------------|-----|-------|-----|--------------|
| **Service** | [Bedrock Guardrails](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails.html) | [Azure AI Content Safety](https://azure.microsoft.com/en-us/products/ai-services/ai-content-safety) | Vertex AI Safety Settings | **Medium** |
| **Customization** | Policy-based | Category-based | Safety thresholds | **Medium** |
| **PII Detection** | Native | Native | Native | **Low** |

**Assessment:** Content safety capabilities are similar across CSPs. Policy definitions are somewhat portable at the conceptual level. **Lock-in risk is Medium.**

### Prompt and Output Controls

| Capability | AWS | Azure | GCP | Lock-in Risk |
|------------|-----|-------|-----|--------------|
| **Input Filtering** | Guardrails | Content filtering | Safety Settings | **Medium** |
| **Output Filtering** | Guardrails | Content filtering | Safety Settings | **Medium** |
| **Grounding Checks** | Limited | Azure AI Groundedness | Vertex Grounding | **High** |
| **Topic Blocking** | Guardrails (denied topics) | Content filtering | Limited | **Medium** |

**Assessment:** Guardrail configurations are CSP-specific. However, the concepts (topic blocking, PII filtering, grounding) are portable. **Lock-in risk is Medium** if you abstract the policy layer.

### Policy Portability

| Aspect | Status |
|--------|--------|
| **Policy Definition Format** | CSP-specific; no standard |
| **Policy Evaluation Logs** | CSP-specific formats |
| **Custom Policy Logic** | Requires CSP-specific integration |

**Recommendation:** Zeta should define its own policy framework that compiles to CSP-native guardrails. This preserves portability while leveraging CSP enforcement.

---

## 4.7 Observability, Logging, and Evaluation Tooling

### Logs, Metrics, Traces

| Capability | AWS | Azure | GCP | Lock-in Risk |
|------------|-----|-------|-----|--------------|
| **Logging** | CloudWatch Logs | Azure Monitor Logs | Cloud Logging | **Medium** |
| **Metrics** | CloudWatch Metrics | Azure Monitor Metrics | Cloud Monitoring | **Medium** |
| **Distributed Tracing** | X-Ray | Application Insights | Cloud Trace | **Medium** |
| **OpenTelemetry Support** | Growing | Growing | Native | **Low** |

**Assessment:** [OpenTelemetry](https://opentelemetry.io/) is emerging as the portable observability standard. CSP-native solutions are more integrated but less portable. **Lock-in risk is Medium**, reducible with OpenTelemetry adoption.

### GenAI Evaluation and Testing

| Capability | AWS | Azure | GCP | Lock-in Risk |
|------------|-----|-------|-----|--------------|
| **Model Evaluation** | Bedrock Model Evaluation | Azure AI Evaluation | Vertex AI Evaluation Service | **High** |
| **Benchmark Datasets** | CSP-provided | CSP-provided | CSP-provided | **Low** |
| **Custom Evaluation** | Supported | Supported | Supported | **Medium** |
| **A/B Testing** | Customer-built | Customer-built | Customer-built | |

**Assessment:** Evaluation frameworks are CSP-specific. Metrics definitions, scoring logic, and baseline comparisons do not transfer. **Lock-in risk is High** for evaluation tooling.

### Limitations for Audit-Grade Explainability

| Limitation | Impact |
|------------|--------|
| **No decision-time explanation capture** | Must be built by Zeta |
| **No chain-of-reasoning logging** | Must be built by Zeta |
| **No evidence generation** | Must be built by Zeta |
| **Logs are operational, not evidentiary** | Not suitable for regulatory response |

**Assessment:** CSP observability is **operational**, not **evidentiary**. It answers "did the system work?" not "why did the agent decide this?" Zeta must build the audit/evidence layer.

---

## 4.8 Summary: Where CSP Platforms Excel

| Strength | Description |
|----------|-------------|
| **Elastic Compute** | On-demand scaling for inference and processing workloads |
| **Global Infrastructure** | Multi-region presence, edge locations, low-latency access |
| **Model Innovation** | Access to latest foundation models (Claude, GPT, Gemini, Llama) |
| **Managed Scale** | Automatic scaling, high availability for individual services |
| **Integration Depth** | Deep integration with CSP ecosystem (IAM, networking, storage) |
| **Security Certifications** | SOC2, ISO, FedRAMP, PCI-DSS compliance for infrastructure |

**CSPs are excellent execution substrates.** They provide the infrastructure on which agent products can run. However, they do not provide the **product layer** that makes agents deployable as regulated banking products.

---

## 4.9 Lock-in Risk Summary Table

| Capability | AWS Lock-in | Azure Lock-in | GCP Lock-in | Mitigation |
|------------|-------------|---------------|-------------|------------|
| **Object Storage** | Low | Low | Low | S3-compatible APIs |
| **Feature Stores** | High | High | High | Export to Parquet; own metadata |
| **Vector DB (Managed)** | Medium-High | Medium-High | Medium-High | Use pgvector; abstract interface |
| **Vector DB (pgvector)** | Low | Low | Low | Standard PostgreSQL |
| **RAG Services** | High | High | High | Own orchestration layer |
| **Fine-tuning** | High | High | High | Store checkpoints portably |
| **Model Registry** | High | High | High | Own registry abstraction |
| **Agent Builders** | Very High | Very High | High* | Own agent definition format |
| **Agent Runtime** | Very High | Very High | High* | Own runtime layer |
| **Tool Integration** | Medium | Medium | Medium | Use MCP; abstract interface |
| **Guardrails** | Medium | Medium | Medium | Own policy framework |
| **Observability** | Medium | Medium | Medium | Use OpenTelemetry |
| **Evaluation** | High | High | High | Own evaluation framework |

*GCP's ADK offers some portability via self-hosting.

---

## Key Takeaways

1. **Agent frameworks are the highest lock-in risk.** Bedrock Agents, Azure AI Agent Service, and Vertex Agent Builder have no portability path.

2. **"Memory" in CSP terms is not agent memory.** It is session-scoped context. True persistent memory must be owned by Zeta.

3. **RAG services are tightly coupled** to CSP storage and models. Zeta should own RAG orchestration.

4. **Observability is operational, not evidentiary.** Audit-grade explainability must be built by Zeta.

5. **Compute and storage are commodities.** Focus portability efforts on the layers above.

6. **MCP and OpenTelemetry offer portable standards.** Adopt these where possible.

7. **CSPs are substrates, not product platforms.** Zeta's value is in the layers they cannot provide.

---

*Previous: [Section 3: System & Infrastructure Requirements](./03-system-requirements.md)*

*Next: [Section 5: What CSP Offerings Cannot Address →](./05-csp-gaps.md)*

