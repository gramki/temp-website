# 3. FFOS Vision & Design Principles

## 3.1 Vision Statement
FFOS becomes the trusted, always-on operating fabric for households inside the bank's perimeter—sensing events across products and channels, reasoning over obligations, risk, and goals via governed state vectors, and executing through multi-agent workflows that honour consent, privacy, and regulatory mandates. It expands the bank's strategic surface area by enabling programmable, agentic experiences while maintaining institutional control, auditability, and resilience.

## 3.2 Core Design Principles

### 3.2.1 Family-First, Individual-Personalized
The family entity is the anchor record for data, workflows, and telemetry. Each member retains personalized views, preferences, and responsibilities enforced through role definitions, consent scopes, and channel policies. Journeys must simultaneously optimize for household objectives (e.g., cashflow stability) and individual needs (e.g., a teen card limit) without duplicating data or violating lineage.

### 3.2.2 Agentic-Native by Design
Every capability is delivered through orchestrated agents. IPC/IAC contracts, shared context envelopes, and guardrail hooks are defined upfront so agents can be onboarded, versioned, and retired predictably. Agents are stateless regarding raw data—they consume authoritative snapshots from core memory, graph memory, and feature stores to avoid divergence and simplify explainability.

### 3.2.3 Consent-First and Privacy-Respecting
All reads, writes, and recommendations must carry explicit consent references, policy versions, and expiry metadata. Consent lifecycle workflows integrate with IAM, document services, and audit archives. Privacy-by-design measures—data minimization, purpose binding, masking, and subject-right automation—are embedded throughout system services and agent contracts.

### 3.2.4 Bank-Resident, Bank-Governed
Compute, storage, and IPC operate within bank-controlled infrastructure or regulator-approved sovereign clouds. Security tooling, key management, monitoring, and SRE runbooks are part of the bank's existing operational stack. Vendor contributions must ship as controlled components with observable behaviour; there are no opaque black boxes handling sensitive workloads.

### 3.2.5 Extensible, Composable, and Product-Agnostic
FFOS separates foundational capabilities (identity, consent, guardrails, workflow, memory, IPC) from product-specific logic. Product teams configure behaviours through declarative policies, feature schemas, and integration drivers. Extension points—agent templates, feature pipelines, channel adapters—follow strict certification, ensuring innovation does not compromise compliance or reliability.

## 3.3 In-Scope vs Out-of-Scope
**In scope:** Household identity graph, consent/access services, security guardrails, event/timeline processing, obligation lifecycle, workflow engine, document/evidence services, core memory, graph memory, feature store, IPC/IAC bus, external I/O adapters, foundation agents, application-level agents, integration contracts, channel abstraction, governance model, and roadmap.  
**Out of scope:** Replacement of core banking systems, generic CRM tooling, or direct-to-consumer apps unrelated to FFOS workflows. FFOS integrates with existing banking products, payment rails, data warehouses, and regulatory reporting solutions instead of rebuilding them. Implementation details such as vendor selection, resourcing, and market-specific localization are handled in downstream delivery plans.
