# 1. Executive Summary

## Zeta Agent Platform Guidance for Bank-Grade, Cloud-Portable AI Agents

---

## The Imperative

Agentic AI is no longer speculative. Every major cloud provider—AWS, Azure, and Google Cloud—has shipped agent frameworks, and banks are actively piloting autonomous decision systems for fraud detection, customer service, underwriting, and compliance. **The question is not whether banks will deploy AI agents, but how they will do so without creating existential dependencies on single vendors or opaque systems that regulators cannot inspect.**

Zeta's opportunity is not to build another chatbot orchestrator. It is to build **the platform layer that makes AI agents deployable as regulated banking products** — auditable, explainable, portable, and resilient.

---

## Why Direct CSP Adoption Is Strategically Risky

Cloud Service Providers (AWS, Azure, GCP) offer compelling building blocks: elastic compute, foundation models, vector databases, and agent orchestration frameworks. These are valuable execution substrates. However, they are **not product platforms for regulated industries**.

The risks of treating CSP agent frameworks as the product layer include:

| Risk | Consequence |
|------|-------------|
| **Vendor lock-in** | Agent definitions, memory stores, and orchestration logic become non-portable. Switching costs compound over time. |
| **Opacity** | CSP-managed services optimize for convenience, not explainability. Regulators will demand evidence that CSPs cannot provide. |
| **Portability gaps** | Banks expect software to run in *their* cloud accounts, across regions, and potentially across CSPs. Native CSP agent runtimes are optimized for CSP-managed environments. |
| **Accountability ambiguity** | When an agent makes a decision, who is accountable? CSP frameworks do not model delegated authority or dual control. |
| **Business continuity exposure** | Multi-region and multi-cloud failover is a Zeta responsibility, not a CSP guarantee. |

---

## Zeta's Platform Stance

Zeta must own the **semantic layer** of agentic products:

1. **Agent identity, authority, and lifecycle** — Who the agent is, what it may do, and how it evolves.
2. **Memory and state portability** — Long-lived agent memory that survives CSP changes.
3. **Context assembly discipline** — Reproducible, inspectable reasoning inputs.
4. **Audit, evidence, and explainability** — Regulator-grade records of what happened and why.
5. **Governance and override capability** — Human-in-the-loop controls that are not optional.

CSPs provide:
- Compute, storage, and networking
- Foundation model inference
- Vector search and RAG primitives
- Observability infrastructure

**Zeta provides the control plane. CSPs provide the execution substrate.**

---

## Strategic Implications

| Dimension | Implication |
|-----------|-------------|
| **For Banks** | Agents are deployed as inspectable, compliant products with full audit visibility. Portability reduces concentration risk. |
| **For Regulators** | Clear accountability models, evidence chains, and override capabilities satisfy supervisory expectations. |
| **For Zeta** | Platform ownership creates defensibility. Agents become durable assets, not ephemeral experiments. |

---

## The Product IP Dimension

Zeta's model is **not just platform**—it is **platform plus products**:

| Element | Description |
|---------|-------------|
| **Zeta owns agent IP** | Collections Agent, Fraud Agent, Advisor Agent are Zeta products |
| **Multi-bank distribution** | Same agent product is licensed to multiple banks |
| **Banks have different CSPs** | Bank A is AWS, Bank B is Azure, Bank C is GCP |
| **Zeta manages lifecycle** | Updates, patches, and versions controlled by Zeta |
| **Bank owns data** | Memory and customer data stay in bank's environment |

This creates a **market access requirement**: if Zeta cannot deploy the same agent product to any bank regardless of their cloud, Zeta loses deals.

**Multi-CSP capability is not optional—it is a prerequisite for Zeta's product distribution model.**

---

## What This Document Provides

This guidance document details:

1. **System requirements** for bank-grade agentic products, independent of any CSP
2. **Comparative analysis** of AWS, Azure, and GCP offerings—capabilities, strengths, and lock-in risks
3. **Structural gaps** that no CSP platform addresses
4. **Zeta's platform architecture** — control plane, components, and design rationale
5. **Product and go-to-market implications** of this platform stance

The goal is to make it **self-evident** why:

> *A cloud-portable, bank-grade agent platform must exist above CSP offerings — and Zeta is positioned to build it.*

---

## Key Principles (Preview)

| Principle | Statement |
|-----------|-----------|
| **Agent Ownership** | Zeta owns agent semantics—identity, authority, memory, lifecycle. |
| **Product IP** | Zeta builds agent products and distributes to banks on any CSP. |
| **Substrate Neutrality** | CSPs are interchangeable execution layers; no CSP owns the control plane. |
| **State Portability** | All persistent state (memory, audit, configuration) is portable across regions and clouds. |
| **Failure-First Design** | Resilience is designed, not assumed. Multi-region and multi-cloud failover is default. |
| **Products First** | Agents are products with SLAs, not experiments. Same version works on any CSP. |

---

## One-Page Summary for Board

**The Situation:**
Banks want AI agents. CSPs want lock-in. Regulators want evidence. Banks use different CSPs. Zeta must thread the needle.

**The Risk:**
Building on CSP-native agent frameworks creates switching costs, opacity, and accountability gaps that banks and regulators will not tolerate. Worse: CSP-specific agents limit Zeta's market to banks on that single CSP.

**The Opportunity:**
Zeta builds the platform layer that makes agents deployable as regulated products—portable, explainable, and resilient. This creates:
- **Customer stickiness** through agent memory and lifecycle ownership
- **Regulatory defensibility** through evidence and override capabilities
- **Multi-cloud flexibility** that reduces bank concentration risk
- **Full market access** — Zeta can sell to any bank regardless of their CSP

**The Product Model:**
Zeta owns the IP of agent products (Collections, Fraud, Advisory). These products are sold to multiple banks. Banks are on AWS, Azure, or GCP. **Same agent, same version, any cloud.**

**The Ask:**
Invest in a control plane that owns agent semantics while leveraging CSP infrastructure. This is not about building models—it's about building the system that makes agent-based products viable for banking and deployable to any bank.

---

*Next: [Section 2: Problem Statement & Strategic Context →](./02-problem-statement.md)*

