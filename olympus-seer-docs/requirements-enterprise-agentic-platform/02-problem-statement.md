# 2. Problem Statement & Strategic Context

---

## 2.1 Why Banks Want Agentic Products Now

### The Pressure to Automate Beyond Rules

Banks face compounding pressures that traditional automation cannot address:

| Pressure | Traditional Response | Limitation |
|----------|---------------------|------------|
| **Cost reduction** | RPA, workflow automation | Brittle scripts; cannot handle exceptions |
| **Scale personalization** | Segment-based models | Cannot reason about individual context |
| **Faster decisions** | Pre-scored decisioning | Static models; cannot adapt in real-time |
| **Regulatory response** | Manual review, sampling | Cannot scale with transaction volume |
| **Customer experience** | Chatbots, IVR | Scripted responses; no genuine reasoning |

Agentic AI offers something qualitatively different: **systems that reason, plan, and act** — not just pattern-match or follow scripts.

### What Banks Actually Want

Based on observed demand from large and mid-sized banks:

1. **Autonomous exception handling** — Agents that can triage, investigate, and resolve operational exceptions without human escalation for routine cases.

2. **Personalized advisory at scale** — Customer-facing agents that remember context, understand preferences, and provide genuinely tailored guidance.

3. **Continuous compliance monitoring** — Agents that monitor transactions, detect anomalies, and generate evidence for regulatory reporting.

4. **Intelligent document processing** — Agents that extract, validate, and reason about unstructured documents (loan applications, KYC materials, contracts).

5. **Proactive risk detection** — Agents that identify emerging risks across portfolios and recommend interventions.

These are not chatbot use cases. They are **decision automation use cases** with regulatory, financial, and reputational consequences.

---

## 2.2 Why Agentic AI Is a Hard Systems Problem

### Agents Are Not Chatbots

The distinction matters profoundly:

| Property | Chatbot | Agent |
|----------|---------|-------|
| **State** | Stateless or session-scoped | Persistent memory across interactions |
| **Authority** | None; advisory only | Delegated; can take actions with consequences |
| **Lifecycle** | Ephemeral | Versioned, deployed, monitored, retired |
| **Failure mode** | Bad answer | Bad decision with financial/regulatory impact |
| **Accountability** | "The AI said..." | Must trace to policy, authority, and oversight |

An agent is a **software product with identity, authority, memory, and failure modes**. It operates within a regulated system and must be:

- **Auditable** — What did it do, when, and why?
- **Explainable** — Can a human understand the reasoning?
- **Overridable** — Can a human intervene, correct, or stop it?
- **Revocable** — Can its authority be withdrawn instantly?

### The Conceptual Precision Problem

One of the most common failure modes in agent systems is **conceptual slippage**—blurring distinctions that must remain sharp:

| Concept | Definition | Must Not Be Confused With |
|---------|------------|---------------------------|
| **Context** | Ephemeral working state for a single reasoning step | Session, Memory |
| **Session** | Interaction boundary and continuity handle | Context, Conversation |
| **Memory** | Agent-owned, long-lived recall (episodic, semantic, preference, procedural) | Knowledge, Logs |
| **Knowledge** | External, authoritative data accessed via retrieval | Memory, Context |

CSP platforms often blur these distinctions. For example:
- AWS Bedrock's "memory" is session-scoped, not persistent
- Azure AI's "knowledge base" is retrieval, not agent memory
- GCP's Agent Engine conflates context and session

**Zeta must maintain these distinctions rigorously** in platform design.

### The Authority Problem

In banking, actions have consequences:
- An agent that approves a wire transfer is exercising delegated authority
- An agent that flags a transaction for review is influencing human decisions
- An agent that responds to a customer is representing the institution

This creates requirements that chatbot frameworks never considered:

| Requirement | Why It Matters |
|-------------|----------------|
| **Delegation ceilings** | An agent cannot exceed the authority delegated to it |
| **Dual control** | High-risk actions require multiple approvals (human or agent) |
| **Separation of duties** | The agent that proposes an action should not be the one that approves it |
| **Kill switches** | Authority can be revoked instantly, across all instances |
| **Accountability chain** | Every action traces to a policy, a delegation, and an oversight mechanism |

No CSP agent framework provides these capabilities. They are Zeta's responsibility.

### The Portability Problem

Banks expect software to run in **their** cloud accounts:

- Regulatory requirements (data residency, sovereignty)
- Concentration risk management (not all eggs in one CSP)
- Existing cloud commitments (banks have negotiated enterprise agreements)
- Security and compliance posture (bank security controls, not CSP defaults)

This creates a fundamental tension:

| CSP Assumption | Bank Reality |
|----------------|--------------|
| Agent runs in CSP-managed environment | Agent must run in customer landing zone |
| State lives in CSP-managed stores | State must be portable and bank-controlled |
| Orchestration uses CSP control plane | Control plane must be CSP-agnostic |
| Failover within CSP regions | Failover may require cross-CSP capability |

**Zeta's platform must bridge this gap**—using CSP infrastructure while maintaining control plane portability.

### The Product Distribution Problem

There is a deeper strategic dimension: **Zeta builds and owns the IP of agent products**.

Unlike a platform-only play where banks build their own agents, Zeta's model includes:

- **Zeta-built agent products** — Collections Agent, Fraud Detection Agent, Advisor Agent, Compliance Monitor
- **Sold to multiple banks** — The same agent product is licensed to Bank A, Bank B, Bank C
- **Each bank has different CSP preferences** — Bank A is AWS-first, Bank B is Azure-first, Bank C uses GCP

This creates a **market access requirement**:

| Scenario | Consequence |
|----------|-------------|
| Agent only runs on AWS | Cannot sell to Azure-committed banks |
| Agent only runs on Azure | Cannot sell to AWS-committed banks |
| Agent is CSP-portable | Zeta can sell to any bank, regardless of their cloud |

**If Zeta cannot deploy the same agent product to banks on different CSPs, Zeta loses deals.**

This is not about bank-requested portability—it is about **Zeta's ability to distribute its products to the entire market**.

### Implications for Agent Product Design

| Requirement | Rationale |
|-------------|-----------|
| **Same code/logic across CSPs** | Version 2.4.1 of Collections Agent behaves identically on AWS, Azure, and GCP |
| **Same lifecycle** | Zeta manages updates and patches for all deployments |
| **Bank owns data** | Memory and customer data reside in the bank's environment |
| **Deployment flexibility** | Runs in Zeta's cloud or bank's cloud—bank chooses |

This means agent products must be designed from the ground up as **CSP-agnostic artifacts** that Zeta can deploy anywhere.

### The Resilience Problem

Agent systems fail. The question is how:

| Failure Mode | Consequence | Mitigation Requirement |
|--------------|-------------|------------------------|
| **Model unavailable** | Agent cannot reason | Graceful degradation; fallback to rules or human |
| **Memory corruption** | Agent behaves inconsistently | Versioned memory; rollback capability |
| **Tool failure** | Agent cannot act | Retry, timeout, and escalation policies |
| **Region outage** | Agent unavailable | Active-active multi-region deployment |
| **CSP outage** | Entire agent fleet down | Multi-cloud failover capability |

CSP platforms optimize for **availability within their environment**. Zeta must design for **survivability across environments**.

---

## 2.3 The Regulatory Context

Banking regulators have not yet issued comprehensive guidance on AI agents, but the direction is clear from existing frameworks:

### Relevant Regulatory Expectations

| Framework | Relevant Requirements |
|-----------|----------------------|
| **OCC SR 11-7** (Model Risk Management) | Models must be validated, documented, and monitored. Applies to ML models; will apply to agents. |
| **Fed SR 21-3** | Guidance on managing risks from third-party relationships, including technology providers. |
| **FFIEC Guidance on AI** | Emphasis on explainability, fairness, and governance. |
| **EU AI Act** | High-risk AI systems (which includes financial services) require conformity assessments, documentation, and human oversight. |
| **DORA** (EU) | Digital operational resilience requirements, including ICT third-party risk management. |

### What Regulators Will Ask

Based on these frameworks, regulators will expect banks to answer:

1. **Who made the decision?** — Agent identity and authority chain must be traceable.
2. **What information was used?** — Context assembly must be reproducible and logged.
3. **Why was this decision made?** — Reasoning must be explainable, not just probabilistic.
4. **Could a human have intervened?** — Override and escalation mechanisms must exist.
5. **What happens if the agent fails?** — Fallback and resilience design must be documented.
6. **How is the agent tested and monitored?** — Lifecycle management must include validation.

**CSP platforms do not provide these answers. Zeta's platform must.**

---

## 2.4 Zeta's Strategic Position

### What Zeta Must Own

| Capability | Why Zeta Must Own It |
|------------|---------------------|
| **Agent definition & lifecycle** | Agents are Zeta products; versioning, deployment, and retirement are Zeta responsibilities. |
| **Agent identity & authority** | Delegation, ceilings, and kill switches are banking requirements CSPs don't address. |
| **Memory system** | Portable, durable, compliant memory is a product differentiator. |
| **Audit & evidence** | Regulator-grade evidence is a Zeta responsibility, not a CSP log stream. |
| **Context assembly** | Reproducible reasoning inputs are foundational to explainability. |
| **Governance & override** | Human-in-the-loop controls are non-negotiable for banks. |

### What CSPs Provide

| Capability | Why CSPs Provide It Well |
|------------|-------------------------|
| **Compute** | Elastic, global, cost-optimized |
| **Model inference** | Foundation models with scale and optimization |
| **Vector search** | High-performance semantic retrieval |
| **Storage** | Durable, replicated, cost-tiered |
| **Observability infrastructure** | Logs, metrics, traces at scale |

### The Division of Responsibility

```
┌─────────────────────────────────────────────────────────────┐
│                     ZETA CONTROL PLANE                      │
│  Agent Lifecycle │ Identity │ Memory │ Audit │ Governance   │
├─────────────────────────────────────────────────────────────┤
│                     ZETA RUNTIME LAYER                      │
│  Context Assembly │ Tool Execution │ Orchestration          │
├─────────────────────────────────────────────────────────────┤
│                     CSP EXECUTION SUBSTRATE                 │
│  Compute │ Models │ Storage │ Vector DB │ Observability     │
└─────────────────────────────────────────────────────────────┘
```

**Zeta owns the product layer. CSPs own the infrastructure layer. The boundary is non-negotiable.**

---

## 2.5 The Strategic Question

This document addresses a single strategic question:

> **How should Zeta build an AI agent platform that enables bank-grade, cloud-portable agentic products—leveraging CSP infrastructure without creating CSP lock-in?**

The answer requires:
1. Understanding what CSPs provide (Section 4)
2. Understanding what they cannot provide (Section 5)
3. Defining Zeta's design principles (Section 6)
4. Specifying the platform architecture (Sections 7-9)
5. Articulating the product and market implications (Section 10)

---

*Previous: [Section 1: Executive Summary](./01-executive-summary.md)*

*Next: [Section 3: System & Infrastructure Requirements →](./03-system-requirements.md)*

