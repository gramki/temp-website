# Evolution Fabric — Product Note

**An operational layer for banking domains — making work explicit, governed, and evolvable by any combination of humans and AI — so that changes in actors, systems, channels, and regulations do not require re-engineering.**

---

## The Architectural Problem

Banks do not lack systems. They lack the ability to change how their domains operate without re-engineering.

Over time, each business domain — payments, credit, servicing, compliance — accumulates its own systems, its own procedures, its own tribal knowledge, and its own integration surface. The operational intelligence of how work gets done is fused to the systems that do it: embedded in bespoke code, manual handoffs, spreadsheet reconciliations, and informal routines that keep things running. Nothing is explicit. Nothing is portable.

The consequences compound:

- **Every change in who does the work requires re-engineering.** A vendor replacement, a team reorganization, an AI agent taking over a step — each triggers a re-engineering project rather than a configuration change. The operational model is inseparable from its current implementors. Changing the actors means redesigning the operations.
- **Operational intelligence is locked in code.** How a dispute gets resolved, how a credit application progresses, how reconciliation catches exceptions — this knowledge lives in system-specific logic, undocumented procedures, and the experience of individuals. When a system is replaced, the intelligence must be reverse-engineered. When a person leaves, it walks out the door.
- **Most of the bank's real work is invisible.** The work that keeps the bank running — manual handoffs between systems, compensating routines for integration gaps, informal escalation paths, exception handling that no system covers — happens in the seams between what's stated. It cannot be governed because it cannot be seen. It cannot be improved because it was never modeled.
- **AI cannot participate without an operational model.** Every AI deployment becomes a bespoke project because there is no explicit model of the work for AI to participate in. There are no declared scenarios, no structured context, no governed delegation, no tool contracts. Each AI initiative must reverse-engineer the operational context from scratch — and the result is a point solution that doesn't compound with anything else.
- **Each domain is an island.** Cross-domain coordination — a customer onboarding that spans identity, credit, payments, and servicing — requires bespoke integration between domains that have no shared model of work, no common interaction surface, and no unified governance. The coordination logic is itself locked in code.
- **Investments don't compound.** Each technology investment adds its own integration surface, its own operational model, its own maintenance burden. Nothing builds on what came before. The cost of change grows with every system added, not because the systems are bad, but because the operational model that connects them is implicit.

The result: the bank's architecture punishes evolution. The more systems it has, the harder it becomes to change how any domain operates. Modernization produces more integration complexity, not less.

---

## What Evolution Fabric Is

Evolution Fabric is the operational layer for banking domains — an integrated platform comprising two systems that together make work explicit, governed, and evolvable:

- **Hub** provides the operational substrate — bounded business domains (Hubs), each with an explicit model of its commitments (Streams), internal discipline (Loops), interaction surfaces (Channels), collaborators (Teams), and system capabilities (Machines). All work resolves through goal-oriented Scenarios — not procedures — using whatever combination of humans and AI is appropriate.
- **Seer** provides the AI agent control plane and runtime — agent lifecycle management, identity and authority, context assembly, guardrails, and governance. Seer agents operate within Hub's operational context: Hub defines what needs to be resolved; Seer governs how AI agents participate in the resolution.

Together, these two systems provide a single operational fabric where:

- Work is modeled as **situations that need resolution** — not as tasks to execute or procedures to follow.
- The model of work is **independent of who does it**. The same Scenario can be resolved by humans today, AI agents tomorrow, and a different vendor next quarter — without changing the model.
- Each domain's operational intelligence is **explicit and declarative** — visible, governable, and portable across changes in systems, people, and organization.
- Human-AI collaboration is **structural** — governed by the same model, the same accountability, and the same audit surface — not bolted on as an afterthought.
- Each investment **compounds on the model** rather than adding to the maintenance burden. A new capability plugs into the domain model through a tool contract; the integration surface does not grow.

---

## Capability Domains

### 1. Domain Modeling

Bounded business domains — each with an explicit operational model that captures what the domain does, how its work is classified, and what systems, people, and AI participate.

| Capability | What It Delivers |
|---|---|
| Hub as bounded domain | Each business domain (payments, credit, servicing, compliance) is modeled as a Hub — an encapsulated operational unit with its own Streams, Loops, Teams, Channels, and Machines. Domain boundaries are explicit, not implicit in system topology |
| Domain-by-domain adoption | Each Hub is independently deployable and independently valuable. A bank can start with one domain, prove value, and expand — without an enterprise-wide transformation. The model grows domain by domain, not all at once |
| Cross-domain coordination | When a commitment spans multiple domains — customer onboarding that touches identity, credit, payments, and servicing — cross-hub Streams coordinate the work through a shared model rather than bespoke point-to-point integration |
| Workbench encapsulation | Each Hub maps to a Workbench — the platform's unit of domain isolation — with its own configuration, enrollment, and governance. Domains operate independently while sharing the same infrastructure |

The Hub is not a replacement for existing systems. It is the operational layer that makes them work together — organized around the bank's business domains, not around vendor product boundaries.

### 2. Work Architecture

The complete classification of all operational work into two categories — external commitments and internal discipline — with no third category and no unmodeled gaps.

| Capability | What It Delivers |
|---|---|
| Streams (external commitments) | Work triggered by an external event — a customer applies, a partner submits, a regulator requests. Each Stream represents a commitment to the outside world that the domain must fulfill. Streams are episodic: they begin, progress through coordinated Scenarios, and resolve |
| Loops (internal discipline) | Work that originates within the domain — reconciliation, compliance verification, fraud detection, analytical routines, operational health monitoring. Loops are the domain's internal discipline: the rituals and routines that keep it healthy, honest, and improving |
| Complete partition | Every piece of work in a domain is either a Stream or a Loop. External trigger → Stream. Internal trigger → Loop. This classification is exhaustive. There is no category of work that falls outside the model |
| Feedback system | Streams generate data. Loops consume it — detecting patterns, verifying compliance, generating intelligence. Loops may trigger new Streams when internal discipline reveals something requiring an external commitment. The domain improves because it operates |

The Stream/Loop partition makes the invisible visible. Work that previously lived in the seams — informal routines, manual compensations, undocumented reconciliations — must be classified as one or the other. Once classified, it is modeled, governed, and improvable.

### 3. Scenario Execution

Goal-oriented resolution of every piece of work — through Scenarios that define what needs to be achieved, not step-by-step procedures that prescribe how.

| Capability | What It Delivers |
|---|---|
| Scenario as universal execution unit | Both Streams and Loops execute through Scenarios. One execution infrastructure for all work — no separate engines for different work types, no fragmentation of the runtime |
| Goal-oriented, not procedure-oriented | A Scenario defines a goal and the conditions for resolution — not a fixed sequence of steps. The path to resolution may vary based on context, available actors, and emerging information. This accommodates the reality that most operational work is not fully predetermined |
| Work pattern vocabulary | Seven recognized patterns — Queue-Based, Case-Based, Event-Driven, Conversation-Based, Artifact-Centric, Review-Based, and Generative — that differentiate how Scenarios execute. Real work composes these patterns: a loan application starts in a queue, involves artifact review, may escalate to a case, and ends with a review decision |
| Resolution spectrum | The same Scenario can be resolved through Pure Automation, Automation with Escalation, Human-AI Teaming, AI-Autonomous (within governance), or Pure Human collaboration. The model does not change when the resolution model changes — only who resolves the work changes |
| Signal-Trigger-Scenario chain | Signals arrive from the environment. Triggers match them to Scenarios. Requests become collaboration surfaces. Resolution happens through the appropriate mix of actors. Outcomes feed organizational learning |

The universal execution model means there is one way to model, execute, govern, and audit all work in a domain. When the bank decides to automate a manual Scenario or add AI to a human-led one, the Scenario definition persists — the resolution model shifts.

### 4. Human-AI Collaboration

Structured collaboration between humans and AI agents — governed by the same model, the same accountability, and the same domain context — across the full resolution spectrum.

| Capability | What It Delivers |
|---|---|
| Teams as first-class collaborators | Each Hub enrolls Teams — combinations of human and AI agents — to resolve its Scenarios. Teams are not ad-hoc assignments; they are modeled, governed, and auditable participants in domain operations |
| Resolution model independence | The same Scenario model supports any point on the resolution spectrum. A dispute resolution Scenario works whether resolved by a human analyst, an AI agent with human oversight, or a fully automated process. The model survives the transition |
| Shared context | Humans and AI agents operating on the same Scenario share the same domain context — the same customer data, the same history, the same applicable rules, the same tool contracts. No separate data pipeline for AI |
| Seamless handoff | Work can move between human and AI agents within a Scenario without losing context, state, or governance. An AI agent can escalate to a human; a human can delegate a sub-task to AI. The collaboration surface is continuous |
| Organizational learning | Outcomes feed back into the domain model. The organization learns from how Scenarios are resolved — across both human and AI resolution — accumulating memory that makes future resolution better |

The shift is structural: instead of asking "how do we add AI to this process?", the bank asks "what resolution model fits this Scenario?" The model accommodates any answer — and accommodates changing the answer later.

### 5. Interaction Surfaces

Multi-modal collaboration channels through which humans and AI agents participate in a domain's Scenarios — each channel a complete interaction system, not just a UI.

| Capability | What It Delivers |
|---|---|
| Channel as interaction system | Each Channel embodies identity, authentication, access control, and the interaction model appropriate to its collaborators. A Channel is not a screen — it is a governed collaboration surface |
| Multi-modal coverage | Web applications (persona-specific desks), chat and collaboration platforms (MS Teams), voice and telephony, API channels (REST), AI agent channels (MCP — Model Context Protocol), and CLI. Each modality takes its native form while connected to the same domain model |
| Hub-scoped configuration | Each Hub configures which Channels are available for its Scenarios. A Payments Hub may expose REST APIs and an Agent Desk. A Customer Servicing Hub may expose web portals, voice, chat, and MCP channels. Channel selection is a domain modeling decision |
| Composable components | Channels are built from composable, paradigm-specific components — the same capability takes a native form in each Channel type (cards on a desk, bot messages in Teams, webhooks on REST, tool listings on MCP). New channels compose from existing components |
| Channel Products | Organization-scoped experiences that recompose components from multiple Hubs — a customer's mobile banking app draws from Payments, Servicing, and Credit Hubs through a unified Channel Product, not through separate integrations |

When the bank adds a new interaction modality — voice AI, a new collaboration platform, an MCP-enabled agent interface — it adds a Channel. The Streams, Loops, Scenarios, Teams, and Machines don't change. The channel is new; the operational model is stable.

### 6. System Integration

Existing systems registered as capability providers — with declared tool contracts that survive changes in which system provides the capability.

| Capability | What It Delivers |
|---|---|
| Machines as capability providers | Core banking systems, payment switches, fraud engines, ML services, credit bureaus — all registered as Machines. What matters is the Tools they provide, not their internal architecture |
| Tool contracts | Each Machine declares its capabilities as Tools — Prediction Applications (observe/predict), Decision Applications (decide), and Commands/Actuators (act). The contract is the stable interface between the domain model and the system landscape |
| System-agnostic modeling | The domain model references Tool contracts, not specific systems. Replacing a Machine — swapping a fraud engine, upgrading a core banking system, moving to a new vendor — does not change Streams, Loops, Teams, or Channels. The Tool contract is honored by the replacement |
| Native and third-party parity | Zeta product lines and third-party systems are equally valid Machines. The integration model is the same regardless of vendor. A domain is not locked to a specific technology provider |
| Hub Applications | Orchestration logic for how Scenarios are resolved — invoking Tools from Machines, coordinating Team activities, managing state. When the runtime is Seer, the Application is an AI Agent: simultaneously orchestrating and participating |

The tool contract is what makes evolution possible at the system level. When the bank replaces a system, it replaces the Machine — not the domain model. The new Machine honors the same tool contracts; the Scenarios that use those tools continue without modification.

### 7. AI Agent Governance

Enterprise-grade governance for AI agents participating in domain operations — lifecycle, identity, authority, guardrails, and memory — so that AI deployment is governed by design, not constrained by fear.

| Capability | What It Delivers |
|---|---|
| Agent lifecycle management | Three-stage lifecycle — Raw (base model capability), Trained (domain-specialized), Employed (assigned to a specific role and context in a Hub). Each stage carries different authority levels and governance requirements |
| Agent identity | Two-layer identity model — Business Identity (the agent's persona, role, and domain context) and Deployment Identity (the technical runtime identity). The business identity persists across deployment changes |
| Authority and delegation | Explicit delegation from a human or role to an agent, with inherited permissions and clear boundaries. Agent authority is always derived, never self-asserted. Every action traces back to an accountable human |
| Context assembly | Structured context compilation for each agent invocation — assembling the right domain knowledge, entity relationships, applicable rules, and tool contracts from the Hub's operational model. Agents operate with full domain context, not generic prompts |
| Guardrails | Input validation, output filtering, behavioral boundaries, and policy enforcement — applied consistently across all agent interactions. Guardrails are structural properties of the agent's employment, not per-invocation configurations |
| OPD governance | Every agent is assessed across three dimensions: Observability (can we see what it's doing?), Predictability (does it behave within expected bounds?), and Directability (can we steer or stop it?). All three must be satisfied for enterprise deployment |
| Memory governance | Agent memory classified by type — Episodic (what happened), Semantic (what things mean), Procedural (how to do things), Preference (what's preferred) — with lifecycle management, retention policies, and governance appropriate to each type |

Seer answers the question the CIO asks before deploying AI at scale: "How do I know this agent is doing what it should, only what it should, and that someone is accountable?" The answer is structural — identity, delegation, guardrails, and audit are built into the agent's employment, not layered on after deployment.

---

## Architectural Position

Evolution Fabric occupies two layers in the banking technology stack:

| Layer | Evolution Fabric Role |
|---|---|
| **Operational Substrate** | Hub provides the explicit, governed model for each business domain — Hubs, Streams, Loops, Scenarios, Teams, Channels, Machines — making operational intelligence declarative and portable rather than locked in code. This is the stable layer on which everything else can change |
| **Agent Control Plane** | Seer provides the governance infrastructure for AI agents operating within Hub's domains — lifecycle, identity, authority, context, guardrails, and memory. This is what makes human-AI collaboration governed by design rather than constrained by caution |

These two layers have historically been addressed — when they've been addressed at all — by separate categories of tooling: BPM and workflow engines for process execution, case management systems for unstructured resolution, integration middleware for system coordination, and custom AI deployments for each use case. Each has its own model, its own data, and its own governance surface. Evolution Fabric replaces this fragmentation with a single operational layer organized around the bank's business domains.

---

## Relationship to Other Fabrics

Evolution Fabric consumes and depends on the other fabrics in the product family:

| Fabric | Relationship |
|---|---|
| **Trust Fabric** | Provides the identity, authentication, consent, and delegation infrastructure that Evolution Fabric requires for both human and AI agent participation. Agent identity in Seer is governed through Trust Fabric's identity model |
| **Truth Fabric** | Provides the semantic layer that grounds Evolution Fabric's domain models in shared, authority-aware definitions. When a Scenario references "available credit" or "dispute resolution," Truth Fabric ensures everyone — human and AI — means the same thing |
| **Cognitive Audit Fabric** | Provides the auditability layer for decisions made within Evolution Fabric's Scenarios. Every judgment call — by human or AI — is reconstructable, explainable, and defensible through CAF's decision memory |
| **Cloud Fabric** | Provides the infrastructure on which Evolution Fabric runs — managed estate, customer-centric observability, and agentic site operations. Evolution Fabric's operational health is monitored through Cloud Fabric's outside-in observability model |

The fabrics are complementary, not competitive. Each governs a distinct concern. Together, they provide the full enterprise infrastructure for a bank that wants to evolve its operations domain by domain — with trust, truth, accountability, and operational reliability built in.

---

## References

- [Olympus Hub Documentation](../../../../olympus-hub-docs/README.md) — The operational substrate for information-centric work
- [Olympus Seer Documentation](../../../../olympus-seer-docs/README.md) — Enterprise AI agent platform: control plane and runtime
- [The Hub Way](../../the-hub-way/README.md) — The framework for modeling work in enterprise banking domains
- [The Thesis](../../the-thesis/README.md) — The structural argument: problems, systems gap, governing principles, and benefits
- [Finding the Fabric for Hub](../finding-the-fabric-for-hub.md) — The naming deliberation that led to "Evolution Fabric"

> **Evolution Fabric makes the bank's operational model the stable layer — so that everything else can change.**
