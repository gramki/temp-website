# 4.1 The Three Cognitive Layers

Enterprise AI agents operate across three distinct cognitive layers, each serving a different purpose and governed differently. Understanding these layers is fundamental to designing agents that are both effective and compliant.

## Overview of the Three Layers

| Layer | What It Contains | Purpose | Governance |
|-------|------------------|---------|------------|
| **Enterprise Knowledge** | Authoritative facts, policies, procedures | Ground agent reasoning in organizational truth | Curated, versioned, formally approved |
| **Enterprise Memory** | Decision records, outcomes, learned patterns | Enable institutional learning and audit | Immutable, 7+ year retention, no PII |
| **Agent Memory** | Session state, conversation, working hypotheses | Support in-flight operations | Ephemeral, session-scoped, PII permitted |

## Enterprise Knowledge: What is True

Enterprise Knowledge represents the organization's codified, authoritative understanding of how things should work:

*   **Regulatory requirements** — What compliance mandates
*   **Business policies** — What the organization has decided
*   **Standard procedures** — How work should be done
*   **Reference data** — Product catalogs, pricing rules, entity definitions

**Key Characteristics:**
- **Normative:** Dictates correct behavior
- **Curated:** Undergoes formal review and approval
- **Versioned:** Changes are tracked with full history
- **PII-free:** Contains no personally identifiable information

**Agent Use:** Grounds reasoning in authoritative guidance, ensuring compliance and consistency.

## Enterprise Memory: What Happened

Enterprise Memory captures the organization's experiential record—what actually occurred and what was learned:

*   **Decision records** — What was decided and why
*   **Outcome records** — What happened as a result
*   **Override records** — When and why humans intervened
*   **Learned patterns** — Hypotheses derived from operational experience

**Key Characteristics:**
- **Experiential:** Records actual events and outcomes
- **Immutable:** Append-only, cannot be modified after creation
- **Long-retained:** 7+ years for regulatory compliance
- **PII-free:** Uses entity references, not direct PII

**Agent Use:** Precedent lookup, understanding historical context, informing risk assessment.

## Agent Memory: What the Agent is Working With Now

Agent Memory supports the agent's immediate operational needs within a session:

*   **Conversation history** — Recent turns in the current interaction
*   **Session state** — Extracted entities, working hypotheses, intermediate results
*   **Preferences** — User preferences for this session
*   **Tool results** — Outputs from recent tool invocations

**Key Characteristics:**
- **Ephemeral:** Session or request-scoped
- **Mutable:** Can be updated during session
- **PII-permitted:** Can contain PII within session boundaries
- **Framework-native:** Uses patterns natural to the agent framework

**Agent Use:** Maintaining conversational flow, tracking intermediate reasoning, personalizing responses.

## Relationship Between Layers

```
┌─────────────────────────────────────────────────────────────┐
│                   ENTERPRISE KNOWLEDGE                       │
│                                                              │
│   What is TRUE — Authoritative, Curated, Versioned          │
│                                                              │
│   Agents READ; only authorized humans/processes WRITE        │
└─────────────────────────────────────────────────────────────┘
                              ▲
                              │ Governed promotion
                              │ (with human approval)
┌─────────────────────────────────────────────────────────────┐
│                   ENTERPRISE MEMORY                          │
│                                                              │
│   What HAPPENED — Experiential, Immutable, Auditable        │
│                                                              │
│   Agents WRITE (decisions, outcomes); READ for precedent     │
└─────────────────────────────────────────────────────────────┘
                              ▲
                              │ Explicit write
                              │ (via Signal Exchange)
┌─────────────────────────────────────────────────────────────┐
│                     AGENT MEMORY                             │
│                                                              │
│   What agent is WORKING WITH — Ephemeral, Session-scoped    │
│                                                              │
│   Agents READ/WRITE freely within session                    │
└─────────────────────────────────────────────────────────────┘
```

## Governance Boundaries

| Boundary | Enterprise Knowledge | Enterprise Memory | Agent Memory |
|----------|---------------------|-------------------|--------------|
| **Write access** | Governance-controlled | Signal Exchange | Direct SDK |
| **Retention** | Indefinite (versioned) | 7+ years | Session + days |
| **PII policy** | Prohibited | Prohibited | Permitted (session) |
| **Cross-agent visibility** | Shared (workbench) | Shared (workbench) | Isolated (agent) |
| **Auditability** | Version history | CAF immutable records | Minimal |

These three layers work together to provide agents with the right information at the right time, under appropriate governance for each type of data.

---

**References:**
*   `olympus-hub-docs/04-subsystems/memory-services/README.md`
*   `olympus-seer-docs/agentic-ai-concepts/agent-memory/knowledge-memory-context-session.md`
*   `olympus-seer-docs/why-seer/part-1-background/03-memory-requirements/_section-overview.md`
