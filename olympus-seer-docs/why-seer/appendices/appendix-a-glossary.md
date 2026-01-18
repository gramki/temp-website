# Appendix A: Glossary

This glossary provides definitions for key terms used throughout this book.

---

## Agent Lifecycle

| Term | Definition |
|------|------------|
| **Raw Agent** | A deployable container image containing agent capabilities (model bindings, tool integrations, framework code) but no enterprise configuration. |
| **Trained Agent** | A Raw Agent configured with knowledge, skills, and guardrails via a TrainingSpec. Represents what the agent *can* do. |
| **Employed Agent** | A Trained Agent granted delegated authority for a specific context via an EmploymentSpec. Represents what the agent *is authorized* to do. |
| **TrainingSpec** | The specification that transforms a Raw Agent into a Trained Agent, defining knowledge bindings, skill configurations, and immutable guardrails. |
| **EmploymentSpec** | The specification that transforms a Trained Agent into an Employed Agent, granting delegated authority within defined ceilings. |

## Memory & Knowledge

| Term | Definition |
|------|------------|
| **Enterprise Knowledge** | Curated, approved, versioned facts that the organization recognizes as authoritative (policies, SOPs, regulations). |
| **Enterprise Memory** | Organizational-level memory of what happened and why (decisions, outcomes, learnings). Immutable, PII-prohibited, long-retained. |
| **Agent Memory** | Session-scoped operational memory for individual agent use. Ephemeral, PII-allowed, not authoritative. |
| **ESPP** | Episodic-Semantic-Procedural-Preference. A taxonomy for classifying memory by cognitive function. |
| **Episodic Memory** | Event-based, time-ordered memory of what happened (decisions, outcomes, handoffs). |
| **Semantic Memory** | Learned beliefs, patterns, and inferences about entities and relationships. |
| **Procedural Memory** | Learned skills, procedures, and action sequences for how to do things. |
| **Preference Memory** | Learned preferences for users and agents—how to personalize interactions. |

## Audit & Governance

| Term | Definition |
|------|------------|
| **CAF** | Cognitive Audit Fabric. The enterprise memory control plane that governs how memory is captured, linked, explained, and audited. |
| **Decision Record** | A structured audit record capturing what was decided, by whom, why, and with what evidence. |
| **Evidence Bundle** | A self-contained package of context, inputs, and outputs for a decision, suitable for regulatory response. |
| **Context Snapshot** | A record of what the agent knew at the time of a decision, enabling reproducibility. |
| **Override Record** | Documentation of a human intervention that changed or corrected an agent's decision. |
| **Handoff Context** | State transfer record when work moves from one agent to another. |

## Metrics & Observability

| Term | Definition |
|------|------------|
| **AHS** | Agent Health Score. A composite metric measuring agent operational health (quality, efficiency, reliability). |
| **CHR** | Cost-to-Health Ratio. The ratio of operational cost to agent health—a value to stabilize, not minimize. |
| **OPD** | Observability, Predictability, Directability. The three properties that distinguish enterprise-ready agents. |

## Agent Collaboration

| Term | Definition |
|------|------------|
| **HAT** | Human-AI Team. A paradigm for coordinated collaboration between human and AI agents within shared operational contexts. |
| **Thinker** | Agent archetype focused on reasoning and decision-making. |
| **Doer** | Agent archetype focused on executing actions and producing results. |
| **Orchestrator** | Agent archetype focused on assigning work and coordinating agents. |
| **Governor** | Agent archetype focused on observing, auditing, and flagging issues. |

## AOSM Concepts

| Term | Definition |
|------|------------|
| **AOSM** | Agent-Oriented Systems Modeling. Zeta's meta-model for designing agent-oriented enterprise systems. |
| **KSA** | Knowledge, Skills, Abilities. What agents know and can do—the components of agent competence. |
| **PIDA** | Perceive, Interpret, Decide, Act. The cycle of agent behavior in responding to situations. |
| **RASCI** | Responsible, Accountable, Supporting, Consulted, Informed. The accountability model where humans are always Accountable. |
| **Controlled Autonomy** | The principle that agent autonomy is always bounded by limits set by accountable humans. |

## Platform Components

| Term | Definition |
|------|------------|
| **Seer** | Zeta's agent control plane and runtime for enterprise AI agents. Governs agent identity, authority, lifecycle, and guardrails. |
| **Hub** | Zeta's operational substrate for enterprise automation. Provides memory, knowledge, tools, and audit infrastructure. |
| **Workbench** | A bounded business context in Hub containing signals, scenarios, operations, knowledge, memory, and agents. |
| **Scenario** | A defined business context within a Workbench that prescribes roles, goals, and procedures for handling work. |
| **Model Gateway** | Seer's unified interface to LLM/SLM providers, enabling model routing, fallback, and cost governance. |
| **Bifrost** | The open-source foundation for Seer's Model Gateway, adapted for enterprise requirements. |

## Coordination Patterns

| Term | Definition |
|------|------------|
| **Scenario-as-Tool** | Pattern where a Scenario is exposed as a callable tool for synchronous invocation. |
| **Scenario-as-Agent** | Pattern where a Scenario is enrolled as an agent to complete tasks in another Scenario's queue. |
| **Workbench-as-Machine** | Pattern where a Workbench is published as a machine for cross-workbench invocation. |
| **Parent-Child Request** | Nested request hierarchy enabling context inheritance and lifecycle coupling. |

## Identity & Authority

| Term | Definition |
|------|------------|
| **Delegation Chain** | The traceable path of authority from an accountable human through roles/users to an agent. |
| **Authority Ceiling** | A hard limit on what an agent can do, regardless of delegated permissions. |
| **Kill Switch** | Instant authority revocation mechanism, distinct from process termination. |
| **Cipher IAM** | Olympus's identity and access management system, providing identity infrastructure for agents. |
| **PEP** | Policy Enforcement Point. A component that evaluates and enforces policies at runtime. |
| **Request-Scoped Authority Delegation** | Delegation model enabling business users to grant temporary authority to agents for specific tasks, distinct from enterprise delegation. |
| **Delegation Template** | Defines a package of authority that can be delegated to agents. |
| **Delegation Certificate** | Represents a user's consent to delegate authority per a template. |
| **Delegation Access Token** | Request-scoped JWT that an agent uses to perform actions on behalf of the delegator. |
| **Agent Persona** | Scenario-derived business identity representing "who is accountable" in business terms. |
| **Deployment Identity** | SPIFFE-based infrastructure identity used for mTLS and service mesh authentication. |
| **Sub-Persona** | Distinct identity for each agent in a composite application, derived from base Agent Persona. |

## Collaboration Channels

| Term | Definition |
|------|------------|
| **MCP Server** | Workbench-scoped CRD that exposes Hub capabilities via Model Context Protocol. |
| **Template Kind** | CRD kind (e.g., `business-user-template`) that implies persona and capabilities without explicit persona field. |

## Governance & Oversight

| Term | Definition |
|------|------------|
| **COGW** | Cognitive Operations Governance Workbench — subscription-wide governance workbench type enabling cross-workbench oversight. |
| **COG Sentinel** | Request Sentinel with cross-workbench targeting via pattern-based matching. |

## Persona Twins

| Term | Definition |
|------|------------|
| **Persona Twin Blueprint** | Extension to Trained Agent Blueprints providing signal suggestions, filter templates, and schedule suggestions for non-developer twin creation. |
| **Signal Suggestions** | Common signals suggested by Persona Twin Blueprints (task assignment, platform notifications, schedules). |
| **Filter Suggestions** | OPA filter templates provided by Persona Twin Blueprints for signal filtering. |
| **Schedule Suggestions** | Common schedules suggested by Persona Twin Blueprints (daily summaries, weekly reviews). |

---
