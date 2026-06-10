# Agent Swarms: Terminology and Architectural Position

**Status:** Proposed  
**Type:** Terminology Standard and Architectural Position Paper  
**Discussion transcript:** [swarm-terminology-discussion-transcript.md](swarm-terminology-discussion-transcript.md)

## Position Statement

Organizations adopting AI agent ecosystems require organizational constructs analogous to those used for humans. **Swarm** serves as the persistent, governed organizational unit for agent populations—deliberately distinct from the term's traditional association with runtime coordination patterns.

Under this model:

- **Swarms** govern agents (management plane)
- **Teams** execute work (runtime plane)
- The two must never be conflated

This separation is the central architectural decision.

## The Problem with Current Terminology

### Terminology Overload

The AI agent ecosystem suffers from overloaded vocabulary:

| Term | Conflicting meanings |
|------|---------------------|
| Agent | Code artifact, runtime instance, persona, assistant |
| Swarm | Population of agents, coordination topology, emergent behavior |
| Team | Humans, agents, or both; persistent or ephemeral |
| Workforce | People, automation, organizational capacity |

When architects say "create a fraud swarm," they may mean an organizational boundary, a runtime assembly, or a coordination pattern. This ambiguity compounds as agent populations grow.

### Why Terminology Matters

Without clear organizational constructs:

- **Discovery** becomes difficult—where do fraud-related agents live?
- **Governance** becomes unclear—who owns this agent population?
- **Accountability** fragments—which team is responsible when things go wrong?
- **Scalability** suffers—runtime and organizational concepts intertwine in ways that don't scale

Organizations do not manage people as an undifferentiated collection. They create teams, departments, business units, and organizational units. Agent ecosystems require equivalent structures.

## The Architectural Decision

### Governance vs Execution: The Core Separation

The model establishes a strict separation between management-plane and runtime constructs:

| Plane | Construct | Characteristics |
|-------|-----------|-----------------|
| Management | Swarm | Persistent, governed, domain-scoped, chartered |
| Management | Workforce | Combined human and agent population |
| Runtime | Team | Ephemeral, mission-specific, assembled for a Work Order |
| Runtime | Work Order | Instance of work to be completed |

**Why this separation matters:**

Governance boundaries are persistent. A "Fraud Swarm" exists whether or not any fraud investigation is currently active. It has ownership, a charter, policies, and stable membership.

Execution assemblies are ephemeral. A "Fraud Investigation Team" exists only for the duration of a specific Work Order. It may draw agents from multiple Swarms. It dissolves when the work completes.

Conflating these—as most current terminology does—creates confusion about ownership, lifecycle, and accountability.

### Why "Swarm" Despite the Semantic Baggage

The term "Swarm" carries connotations from swarm intelligence research:

| Traditional "Swarm" meaning | This document's meaning |
|-----------------------------|-------------------------|
| Runtime coordination pattern | Persistent organizational unit |
| Emergent, decentralized behavior | Governed, chartered domain boundary |
| Dynamic task assembly | Stable membership with defined lifecycle |
| Many simple agents self-organizing | Domain-complete population under human governance |

**Why override the traditional meaning?**

Alternatives considered:

| Term | Why rejected |
|------|--------------|
| Collection | Implies static inventory, not active participants |
| Catalog | Describes artifacts, not organizational identity |
| Guild | Uncommon in enterprise; implies community of practice |
| Workforce | More valuable as the human+agent umbrella term |
| Team | Better reserved for ephemeral execution assemblies |

"Swarm" was selected because it:

- Provides a natural collective noun for autonomous agent populations
- Implies agency, population, and collective capability
- Does not imply fixed hierarchy or specific mission
- Scales naturally from tens to thousands of agents
- Is distinct from "Team" (which enterprises already associate with mission execution)

**The rule to prevent confusion:**

> The term "Swarm" by itself always refers to the organizational construct. When referring to a runtime coordination pattern, say "Swarm Topology" explicitly.

This rule is non-negotiable. Violating it reintroduces the ambiguity this standard eliminates.

## The Model

### Organizational Hierarchy

```
Workforce
├── Human Organizational Units
│   ├── Engineering Team
│   ├── QA Team
│   └── ...
│
└── Agent Swarms
    ├── Build Swarm
    │   ├── feature-implementer (Trained Agent)
    │   ├── code-refactorer (Trained Agent)
    │   └── test-writer (Trained Agent)
    │
    ├── Review Swarm
    │   ├── code-reviewer (Trained Agent)
    │   ├── security-reviewer (Trained Agent)
    │   └── style-checker (Trained Agent)
    │
    └── Test Swarm
        └── ...
```

The **Workforce** is the combined population of humans and agents available to perform organizational work. It is the umbrella construct.

A **Swarm** is a governed subset of the Workforce, scoped to a functional domain, containing only Trained Agents.

### Execution Hierarchy

```
Scenario (normative definition of work)
    │
    └── Work Order (runtime instance)
            │
            └── Team (ephemeral assembly)
                    ├── Human Developer
                    ├── feature-implementer (Employed Agent from Build Swarm)
                    ├── test-writer (Employed Agent from Build Swarm)
                    ├── code-reviewer (Employed Agent from Review Swarm)
                    └── Coordinator: build-swarm/feature-implementer (always explicit)
```

A **Scenario** defines a category of work: "Chargeback Investigation," "KYC Refresh," "Loan Underwriting."

A **Work Order** is a runtime instance: "Chargeback Investigation #12834."

A **Team** is assembled to execute a Work Order. It is ephemeral—it exists only for the duration of the work.

### Key Relationships

| Relationship | Rule |
|--------------|------|
| Trained Agent → Swarm | Each Trained Agent belongs to exactly one Swarm |
| Team → Swarm | A Team may recruit Employed Agents from multiple Swarms |
| Swarm boundary | Governance boundary, not execution boundary |
| Topology | How a Team coordinates; orthogonal to Swarm membership |
| Identity | Each Trained Agent has a JID: `{agent}@{swarm}.agents.{tenant}.foundry.io` |

Cross-Swarm participation is expected and normal. A feature implementation Team might include Employed Agents from the Build Swarm and Review Swarm. The Swarm boundaries define governance and ownership, not execution scope.

## Core Concepts

### Workforce

The combined population of humans and agents available to perform organizational work.

- Includes both human organizational units and agent Swarms
- The umbrella construct for productive capacity
- Should not be used for agent-only populations

**Example:** "Engineering Workforce" encompasses the Engineering Team (humans) and the Build, Review, and Test Swarms (Trained Agents).

### Swarm

A persistent, governed organizational unit of Trained Agents belonging to a bounded functional domain.

- Domain-scoped (Build, Review, Test, Documentation, Release, Governance)
- Exists in the management plane
- Possesses charter, ownership, membership rules, and policies
- Contains Trained Agents; does not execute work
- Governance boundary, not execution boundary
- Scoped at Foundry, Workshop, Workbench, or Workspace level

**Example:** "Build Swarm" contains all Trained Agents specialized for feature implementation, code refactoring, and test writing.

### Agent

An active entity exercising agency on behalf of a mission, team, or organization.

This definition is intentionally strict:

- A code artifact is not an Agent
- A template is not an Agent
- A skill definition is not an Agent
- Only active entities are Agents

This aligns with the three-tier agent model defined elsewhere in Agent Fabric: Raw Agent (the OCI-packaged agent system), Trained Agent (the configured manifest with Swarm membership and identity), Employed Agent (the active runtime instance with JID + Delegation Token). Only Employed Agents are "Agents" in the sense used by this document.

### Scenario

The normative definition of a category of work.

- Defines expected work patterns, inputs, outputs, and success criteria
- Not a runtime object
- Multiple Work Orders may instantiate the same Scenario

Scenarios reference Swarms and specify a coordinator agent explicitly. The coordinator is always a `{swarm}/{trained-agent}` reference.

**Examples:** implement-feature, code-review, execute-test-suite, deploy-release

### Work Order

A runtime instance of a Scenario—actual work to be completed.

- The operational representation of work
- Has a lifecycle: created, assigned, in-progress, completed
- Triggers Team assembly

**Examples:** implement-feature WO-567, code-review WO-890

### Team

A temporary assembly of participants formed to execute a Work Order.

- Ephemeral—exists only for the Work Order's duration
- May contain humans, agents, or both
- May draw Employed Agents from multiple Swarms
- One or more Coordinators manage execution

**Example:** The Team for implement-feature WO-567 includes a human developer, a feature-implementer Employed Agent and test-writer Employed Agent (both from the Build Swarm), and a code-reviewer Employed Agent (from the Review Swarm).

### Coordinator

A participant responsible for coordinating execution within a Team.

- May be human or agent
- Is part of the Team, not external to it
- Multiple Coordinators may coexist
- Coordination is a responsibility, not a separate organizational construct

## Swarm Governance

Every Swarm must possess:

### Charter

Defines the Swarm's:

- **Purpose** — Why does this Swarm exist?
- **Scope** — What problem domain does it cover?
- **Authority** — What actions can its agents take?
- **Responsibilities** — What outcomes is it accountable for?

### Ownership

Defines:

- **Responsible organizational unit** — Which human team owns this Swarm?
- **Accountable leaders** — Who answers for its behavior?
- **Governance contacts** — Who approves changes to membership or policies?

### Membership

Defines:

- **Which Trained Agents belong** — Explicit roster; each belongs to exactly one Swarm
- **Eligibility requirements** — What qualifies a Trained Agent for membership?
- **Identity** — Each Trained Agent receives a JID within the Swarm's domain
- **Lifecycle expectations** — How are Trained Agents added, reviewed, and removed?

### Policies

Defines:

- **Operational controls** — Rate limits, resource quotas, escalation rules
- **Security controls** — Authentication, authorization, audit requirements
- **Compliance requirements** — Regulatory constraints, data handling rules
- **Behavioral constraints** — What agents must not do

## Execution Topologies

Topology describes *how* a Team coordinates during execution. It is orthogonal to Swarm membership.

| Topology | Description |
|----------|-------------|
| Hierarchical | Central coordinator delegates to specialists |
| Pipeline | Sequential handoff between agents |
| Mesh | Peer-to-peer collaboration |
| Federated | Distributed coordination across boundaries |
| Market | Agents bid for and negotiate tasks |
| **Swarm Topology** | Decentralized, emergent coordination |

**Critical distinction:**

- A Team drawn from the "Build Swarm" might use Pipeline Topology
- A Team using "Swarm Topology" might draw Employed Agents from multiple Swarms
- The organizational construct (Swarm) and the coordination pattern (Swarm Topology) are independent

When you mean the coordination pattern, always say "Swarm Topology." When you mean the organizational unit, say "Swarm" or "[Domain] Swarm."

## Organizational Lifecycle

### Swarm Lifecycle

| Phase | Activities |
|-------|------------|
| **Creation** | Define charter, establish ownership, set initial policies |
| **Staffing** | Configure Trained Agents, assign to Swarm, set membership rules |
| **Operation** | Trained Agents available for employment; governance enforced |
| **Evolution** | Charter amendments, policy updates, membership changes |
| **Dissolution** | Trained Agents reassigned or decommissioned; Swarm archived |

### Agent Employment Lifecycle

| Phase | Activities |
|-------|------------|
| **Raw Agent Registration** | OCI container registered in Raw Agent Registry |
| **Trained Agent Configuration** | Manifest created binding Raw Agent to Swarm with skills, guardrails, and JID |
| **Swarm Assignment** | Trained Agent assigned to exactly one Swarm |
| **Availability** | Trained Agent available for Team recruitment |
| **Employment** | Trained Agent instantiated as Employed Agent with JID + Delegation Token (OAuth Access Token) |
| **Delegation** | Workspace owner's authority delegated via OAuth Access Token |
| **Execution** | Employed Agent participates in Team work |
| **Return** | Work Order completes; Employed Agent terminates; Trained Agent remains in Swarm |
| **Reassignment** | Trained Agent may be moved to a different Swarm (governance event) |

### Team Lifecycle

| Phase | Activities |
|-------|------------|
| **Assembly** | Work Order triggers Team formation; Employed Agents spawned from Trained Agents in referenced Swarm(s) |
| **Coordination** | Coordinator(s) assigned; topology selected |
| **Execution** | Team executes Work Order |
| **Dissolution** | Work Order completes; Employed Agents terminate; Trained Agents remain in Swarms |

## Agent Fabric Responsibilities

The Agent Fabric is the platform responsible for managing agent ecosystems. Its responsibilities include:

| Responsibility | Description |
|----------------|-------------|
| Raw Agent Registry | Register OCI containers in the two-layer catalog |
| Swarm Registry | Create, update, archive Swarms; manage membership |
| Swarm discovery | Find Swarms by domain, capability, ownership, scope |
| Trained Agent management | Configure manifests with JID, skills, guardrails |
| Agent discovery | Find Trained Agents by capability, Swarm, availability |
| Governance enforcement | Enforce charter, policies, membership rules, quotas |

The Agent Fabric is **not** synonymous with runtime orchestration. It manages the organizational structures from which Teams are assembled, but the Work Order Runtime handles actual execution.

## Guidance for Architects

### Terminology Usage

| When describing... | Use this term |
|--------------------|---------------|
| OCI-packaged agent system | Raw Agent |
| Configured manifest with skills, guardrails, and identity | Trained Agent |
| Running instance with delegated authority | Employed Agent |
| Persistent Trained Agent population scoped to a domain | Swarm |
| Combined human and agent productive capacity | Workforce |
| Ephemeral assembly executing a Work Order | Team |
| Normative definition of a work category | Scenario |
| Runtime instance of work | Work Order |
| Decentralized coordination pattern | Swarm Topology |

### Common Anti-Patterns

**Anti-Pattern: Conflating Swarm and Team**

❌ "The Build Swarm is implementing feature #123"

✓ "The Feature Implementation Team (assembled for Work Order #123) includes Employed Agents from the Build Swarm"

**Anti-Pattern: Using Swarm for Runtime Coordination**

❌ "Create a swarm to handle this request"

✓ "Assemble a Team to handle this Work Order" (or "Use Swarm Topology for decentralized coordination")

**Anti-Pattern: Using Workforce for Agents Only**

❌ "The Build Workforce contains our implementation agents"

✓ "The Build Swarm contains our implementation Trained Agents"

**Anti-Pattern: Assuming Swarm Implies Swarm Topology**

❌ "Trained Agents in the Build Swarm coordinate through emergent behavior"

✓ Swarm membership says nothing about coordination topology. The Build Swarm's Trained Agents might execute in Pipeline Topology, Hierarchical Topology, or Swarm Topology depending on the Scenario.

**Anti-Pattern: Confusing Trained and Employed Agents**

❌ "The Trained Agent is running the code review"

✓ "The Employed Agent (instantiated from the code-reviewer Trained Agent) is running the code review"

## Conclusion

The introduction of persistent agent populations requires organizational constructs analogous to those used for humans. **Swarm** is the organizational unit for agents because it conveys agency, population, and collective capability—while deliberately separating it from the runtime coordination pattern that shares its name.

The model established here:

| Construct | Role |
|-----------|------|
| Workforce | Combined human and agent population |
| Swarm | Governed organizational unit for agents |
| Scenario | Normative work definition |
| Work Order | Runtime work instance |
| Team | Ephemeral execution assembly |
| Coordinator | Execution coordination responsibility |
| Topology | How a Team coordinates (including Swarm Topology) |

Under this model, Swarms govern Trained Agents, Teams execute work through Employed Agents (Trained Agents instantiated with JID + Delegation Token), Work Orders represent missions, and the Agent Fabric provides the mechanisms — Raw Agent Registry, Swarm Registry, Skill Registry — through which these structures are defined, discovered, and managed.

The separation of governance from execution—and the explicit distinction between Swarm (organizational unit) and Swarm Topology (coordination pattern)—is the central contribution of this terminology standard.

## Glossary

| Term | Definition |
|------|------------|
| Agent | Active entity exercising agency on behalf of a mission, team, or organization |
| Agent Fabric | Platform responsible for managing agent ecosystems via Raw Agent Registry, Swarm Registry, and Skill Registry |
| Charter | Document defining a Swarm's purpose, scope, authority, and responsibilities |
| Coordinator | Team participant responsible for coordinating execution; always explicitly specified in Scenario definition |
| Delegation Token | OAuth Access Token from workspace owner granting scoped authority to an Employed Agent |
| Employed Agent | Runtime instantiation of a Trained Agent, bound to JID + Delegation Token + Workspace Session |
| JID | Jabber ID; Service Principal identity for a Trained Agent: `{agent}@{swarm}.agents.{tenant}.foundry.io` |
| Raw Agent | OCI-packaged agent system (e.g., Codex, Cursor Agent, Claude Code); the packaging layer |
| Scenario | Normative definition of a category of work; references Swarms and a coordinator agent |
| Swarm | Persistent, governed organizational unit of Trained Agents scoped to a functional domain |
| Swarm Topology | Runtime coordination pattern featuring decentralized, emergent behavior |
| Team | Temporary assembly of participants (Employed Agents + humans) formed to execute a Work Order |
| Topology | The coordination pattern a Team employs during execution |
| Trained Agent | Declarative manifest binding a Raw Agent to a Swarm with skills, guardrails, and JID; the configuration layer |
| Work Order | Runtime instance of a Scenario |
| Workforce | Combined population of humans and agents available for organizational work |
