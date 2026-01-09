# Raw, Trained, Employed Agents: Zeta's Extension to AOSM

> **Concept Note — Zeta's Extension to AOSM**  
> **Audience:** Enterprise Architects, Product Managers, AI Engineers  
> **Status:** Draft for Review — Seeking Feedback  
> **Last Updated:** January 2026  
> **Document Type:** Conceptual Framework (not implementation-ready technical design)  
> **Relationship to AOSM:** This document extends the Agent-Oriented Systems Modeling (AOSM) meta-model with terminology specific to enterprise agent lifecycle and governance.

### Prerequisite Reading

This document assumes familiarity with **Agent-Oriented Systems Modeling (AOSM)** concepts. Before proceeding, readers should review:

- **[Book Summary: Integrating Artificial and Human Intelligence through Agent-Oriented Systems Design](./book-ref/book-summary.md)** — Essential pre-read covering AOSM meta-model, KSA, PIDA, OPD, RASCI, and HAT patterns
- For deeper understanding, the complete book is recommended: *Integrating Artificial and Human Intelligence through Agent-Oriented Systems Design* (Systems Innovation Book Series)

---

## Table of Contents

1. [Executive Summary](#executive-summary)
2. [Scope and Applicability](#scope-and-applicability)
3. [Origins and Influences](#origins-and-influences)
4. [Alternative Framings](#alternative-framings)
5. [The Problem: Terminology Ambiguity](#1-the-problem-terminology-ambiguity-in-agent-discourse)
6. [Where Terminology Clarity Adds Value](#2-where-terminology-clarity-adds-value)
7. [Zeta's Proposed Terminology](#3-zetas-proposed-terminology-agents-by-deployment-nature) — **Core content**
   - [3.1 Raw Agents](#31-raw-agents-the-deployable-artifact)
   - [3.2 Trained Agents](#32-trained-agents-tenant-configured-with-knowledge-and-skills)
   - [3.3 Employed Agents](#33-employed-agents-delegated-authority)
   - [3.4 OPD Across Agent Layers](#34-opd-across-agent-layers)
8. [Composition and Relationships](#4-composition-and-relationships)
9. [Lifecycle Implications](#5-lifecycle-implications)
10. [Governance Implications](#6-governance-implications)
11. [Open Questions](#7-open-questions-for-discussion)
12. [Summary](#8-summary-what-zeta-hopes-to-achieve)
13. [Appendices](#appendix-a-glossary)

---

## Executive Summary

The term "agent" in Agentic AI is used to describe many different things—from foundation models to orchestration code to authorization scopes. In many contexts, this ambiguity is harmless; teams develop shared understanding and context disambiguates meaning.

However, when building **agent-based products for regulated industries**—where audit, accountability, and delegated authority matter—this conflation can create real friction. Different stakeholders (platform engineers, security teams, compliance officers, domain experts) may use "agent" to mean different things, leading to miscommunication about ownership, change management, and liability.

**This document proposes a terminology framework that Zeta is considering for its agent platform.** The framework distinguishes three layers:

1. **Raw Agents** — Deployable application artifacts with technical capabilities
2. **Trained Agents** — Tenant-configured agents with domain knowledge, procedures, and skills
3. **Employed Agents** — Agents with delegated authority to act in specific contexts

This is not presented as *the* universal answer to agent terminology. It is *a* decomposition that we believe fits Zeta's context: building bank-grade agent products where delegation, multi-tenancy, and governance are first-class concerns.

---

## Scope and Applicability

### Conceptual Foundation: Human-AI Teams (HAT) and AOSM

This framework limits the scope and realm of "agent" to **Enterprise Information Systems** that are modeled as **Human-AI Teams (HAT)** conforming to the **Agent-Oriented Systems Modeling (AOSM)** meta-model.

In this context:
- **Agents** are entities that sense, interpret, decide, and act (PIDA activities)
- Agents operate within **Goal hierarchies** with defined **Roles** and **Responsibilities**
- Agents possess **Capabilities** (Knowledge, Skills, Abilities—KSA) appropriate to their Responsibilities
- AI agents operate under **Controlled Autonomy**—acting autonomously only to the extent beneficial to, and within bounds set by, responsible humans
- Humans remain **Accountable** for outcomes; AI agents may be Responsible but never Accountable
- All agents must satisfy **OPD requirements**: Observability, Predictability, Directability (see [Section 3.4](#34-opd-across-agent-layers))
- Agent authority derives from the **Four Components of Autonomy**: Authority, Availability, Capability, Capacity

This framing explicitly excludes:
- Fully autonomous physical systems (robotics, self-driving vehicles)
- General-purpose AI or AGI without defined organizational roles
- Research/experimental agents not subject to enterprise governance

**Where this framework is most relevant:**
- Enterprises shipping agents as products (not just internal tools)
- Regulated industries with audit and accountability requirements
- Multi-tenant platforms where the same code serves multiple customers
- Systems where agents act with delegated authority (on behalf of users or roles)
- Architectures where multiple agents collaborate or delegate to each other

**Where simpler models may suffice:**
- Internal experimentation and prototyping
- Single-tenant deployments with informal governance
- Chatbots and assistants without tool-calling or delegation
- Teams with strong shared context who can disambiguate organically
- Personal assistants outside workplace/enterprise context (consumer use)

*Note: Single-user, private agents within an enterprise context ARE in scope—the exclusion applies only to consumer personal assistants outside organizational governance.*

The intensity of the framework should match the stakes of the deployment.

---

## Origins and Influences

This proposal draws on several sources:

- **Agent-Oriented Systems Modeling (AOSM)**: The meta-model for Human-AI Teams developed by Systems Innovation, which provides a rigorous framework for designing systems where humans and AI agents collaborate. Key concepts adopted:
  - Capabilities as Knowledge, Skills, and Abilities (KSA)
  - PIDA Responsibilities (Perception, Interpretation, Decision, Action)
  - Four Components of Autonomy (Authority, Availability, Capability, Capacity)
  - Controlled Autonomy and OPD (Observability, Predictability, Directability)
  - RASCI allocation (Responsible, Accountable, Supporting, Consulted, Informed)

- **Practical experience** building multi-tenant agent systems
- **Enterprise identity patterns** (SPIFFE, OAuth delegation, workforce IAM)
- **Software supply chain thinking** (distinguishing build-time, deploy-time, and runtime)
- **Regulatory frameworks** that require tracing actions to accountable principals
- **Agent memory research** (Reflexion, MemGPT) informing the distinction between procedural, semantic, and episodic memory

**References:**
- Sterling, L., & Taveter, K. (2009). *The Art of Agent-Oriented Modeling*
- Stevenson et al. (2023). Four Components of Autonomy
- Johnson, M., et al. (2018). OPD framework for human-machine teaming
- Shinn, N., et al. (2023). Reflexion: Language Agents with Verbal Reinforcement Learning

We acknowledge that the AI agent ecosystem is evolving rapidly, and vocabulary is emerging organically. Frameworks like LangGraph, CrewAI, AutoGen, and others are developing their own concepts. This proposal aims to complement—not replace—that evolution, providing a lens specifically suited to Zeta's enterprise context.

---

## Alternative Framings

The three-layer model proposed here is not the only valid decomposition. Other framings may be more suitable for different concerns:

| Alternative Framing | Focus | When It Fits |
|---------------------|-------|--------------|
| **By lifecycle stage** (dev / deploy / runtime / interaction) | When the question is "what phase are we in?" | CI/CD and DevOps discussions |
| **By ownership** (platform / application / user) | When the question is "who is responsible?" | Organizational design |
| **By scope** (model / runtime / session / action) | When the question is "what granularity?" | Debugging and observability |
| **By capability** (reasoning / acting / learning) | When the question is "what can it do?" | Capability assessment |

The Raw/Trained/Employed model optimizes for the **delegation and governance** dimension, which is central to Zeta's use case. Teams with different priorities may prefer different decompositions.

---

## 1. The Problem: Terminology Ambiguity in Agent Discourse

### 1.1 The Ambiguity in Practice

In contemporary discourse about AI agents, the word "agent" is applied to many different artifacts. This is natural for an emerging field—vocabulary takes time to stabilize. However, when precision matters (for contracts, security reviews, or incident response), the ambiguity can become friction:

| What People Call "Agent" | What It Actually Is | Example |
|--------------------------|---------------------|---------|
| The LLM | A foundation model that provides reasoning capability | "We're using GPT-4 as our agent" |
| The orchestration code | Application logic that manages conversation flow, tool calls, and memory | "Our agent is built on LangGraph" |
| A prompt collection | A set of system prompts, few-shot examples, and guardrails | "We have a compliance agent and a sales agent" |
| A RAG pipeline | A retrieval-augmented generation system over documents | "The agent searches our knowledge base" |
| A chatbot interface | A conversational UI backed by an LLM | "The agent is available on Slack" |
| A tool-calling wrapper | A system that invokes APIs based on LLM decisions | "The agent can book meetings and send emails" |
| An autonomous process | A long-running system that acts without user prompts | "The agent monitors our infrastructure" |
| A persona | A configured identity with specific behaviors | "Ask the legal agent about this contract" |
| An employee substitute | An autonomous system performing job functions | "The agent handles tier-1 support tickets" |

In many contexts, this ambiguity resolves itself through shared understanding. However, when agents cross organizational boundaries—or when accountability must be formal—each interpretation implies different:

- **Ownership boundaries** (platform team vs. product team vs. business owner)
- **Change management processes** (code deployment vs. prompt update vs. credential rotation)
- **Security models** (infrastructure identity vs. user delegation vs. service account)
- **Audit requirements** (model logs vs. decision trails vs. action records)
- **Lifecycle states** (deployed vs. active vs. suspended vs. revoked)

### 1.2 Extended Examples of Conflation

**Example 1: "We deployed the agent to production"**
- Does this mean a container was deployed to Kubernetes?
- Or that a prompt configuration was published to a registry?
- Or that an agent identity was provisioned in the IAM system?
- All three might be true, but they are governed by different processes.

**Example 2: "The agent has access to customer data"**
- Is this because the underlying LLM was trained on customer data?
- Or because the RAG pipeline indexes customer documents?
- Or because the agent holds credentials to a customer database?
- Each has radically different privacy and compliance implications.

**Example 3: "We need to update the agent"**
- Update the foundation model version?
- Patch the orchestration code for a security vulnerability?
- Revise the system prompts based on user feedback?
- Rotate the agent's credentials?
- These have different blast radii, rollback strategies, and approval gates.

**Example 4: "The agent made an unauthorized transaction"**
- Was this a model hallucination that the orchestration layer failed to catch?
- A prompt injection that bypassed guardrails?
- A legitimate tool call that the agent was authorized to make but shouldn't have been?
- A credential compromise?
- Root cause analysis requires understanding which layer failed.

**Example 5: "Give the agent more authority"**
- Expand the tools available in the orchestration layer?
- Broaden the scope in the system prompts?
- Grant additional IAM permissions to the agent identity?
- Delegate authority from a higher-privilege user?
- Each requires different approvals and has different risk profiles.

---

## 2. Where Terminology Clarity Adds Value

*The following challenges are most acute when agents are deployed as products in regulated environments. Teams building internal tools or prototypes may not encounter these friction points.*

### 2.1 Governance and Compliance Considerations

**Accountability Questions:**
When an agent acts, regulators and auditors may ask: Who authorized this? If "agent" conflates "the code" and "the authorization scope," accountability can become unclear. The code author, the prompt author, the identity administrator, and the delegating user may all be different parties—and none may feel they own "the agent."

A layered terminology helps assign accountability to specific layers.

**Change Management Trade-offs:**
Enterprise change management typically distinguishes between infrastructure changes, application changes, configuration changes, and access changes. Agents can blur all four. Organizations often:
- Treat all agent changes as code deployments (which slows prompt iteration)
- Treat all agent changes as configuration updates (which may be too permissive for code changes)
- Develop ad-hoc processes for each team

A shared vocabulary can help standardize these processes where standardization is valuable.

**Audit Trail Correlation:**
Effective audit may require correlating:
- What the agent did (action logs)
- Why it decided to do it (reasoning traces)
- Under whose authority it acted (identity and delegation)
- What policies constrained it (prompt and guardrail versions)

Layer boundaries make this correlation more tractable.

### 2.2 Architecture and Design Considerations

**Composition Boundaries:**
When building agent systems, architects often ask:
- What can be shared across tenants?
- What can be updated without redeployment?
- What requires security review?

The proposed layers provide one way to answer these questions consistently:
- Raw Agent: shareable infrastructure
- Trained Agent: tenant-specific but without external access
- Employed Agent: holds credentials, never shared

**Multi-Agent Architectures:**
When multiple agents collaborate, the layer model helps clarify what is being composed:
- Multiple personas (Trained Agents) sharing a single runtime (Raw Agent)?
- Independent runtimes (Raw Agents) coordinated by an orchestrator?
- Delegation chains where one Employed Agent authorizes another?

Each pattern has different failure modes and governance implications.

### 2.3 Lifecycle Management Considerations

**Versioning:**
What does "agent version 2.3.1" mean? The layer model suggests versioning each layer independently:
- Raw Agent version (container/code)
- Trained Agent version (training configuration)
- Employed Agent version (delegation policy)

This allows teams to be precise about what changed.

**State Management:**
An agent can be in various states that span layers:
- Deployed but not trained (Raw but not Trained)
- Trained but not authorized (Trained but not Employed)
- Authorized but suspended (Employed but inactive)
- Running but with revoked delegation (Active but unauthorized)

Layer boundaries help define which state transitions are valid and who can trigger them.

### 2.4 Operational Considerations

**Incident Response:**
When an agent misbehaves, the response may depend on which layer is at fault:
- Raw Agent issue → Platform team, deployment rollback
- Trained Agent issue → Domain team, training configuration revert
- Employed Agent issue → Security team, delegation revocation

Layer clarity can help route incidents to the right responders.

**Cost Attribution:**
For chargeback or capacity planning, costs can be attributed by layer:
- Raw Agent: infrastructure costs (compute, memory, network)
- Trained Agent: knowledge storage and model inference
- Employed Agent: attributed to the delegating user/team, bounded by quota/budget

---

## 3. Zeta's Proposed Terminology: Agents by Deployment Nature

The following three-layer model is what Zeta proposes to adopt for its agent platform. It reflects the progressive development and authorization of agents as they move from deployable artifact to trained configuration to delegated authority.

This model is designed for Zeta's specific context: multi-tenant, bank-grade agent products where delegation and governance are primary concerns. Other decompositions may be more appropriate for other contexts.

The terminology is grounded in the **AOSM meta-model** for Human-AI Teams, where agents are defined by their Capabilities (Knowledge, Skills, Abilities), Roles, Responsibilities (PIDA), and Authority.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                         EMPLOYED AGENT                                       │
│  Delegated authority to act in a specific work context                      │
│  - Has identity in Workforce/Customer IAM                                    │
│  - Holds credentials and access tokens                                       │
│  - Scoped to specific work (team, project, customer)                        │
│  - Subject to delegation constraints and resource quotas                     │
│  - Operates under Controlled Autonomy with Accountable human                │
├─────────────────────────────────────────────────────────────────────────────┤
│                         TRAINED AGENT                                        │
│  Tenant-configured agent with domain knowledge and skills                   │
│  - Knowledge: organizational memory, domain facts, procedures               │
│  - Skills: task-specific behaviors, tool usage, problem-solving patterns    │
│  - Prompts: organization style, guardrails, role definitions                │
│  - Tools: specifications, usage training, sandbox validation                │
│  - Identity: application identity (no external access)                       │
├─────────────────────────────────────────────────────────────────────────────┤
│                         RAW AGENT                                            │
│  Deployable application artifact with technical capabilities                │
│  - Container/Lambda/Service deployment                                       │
│  - LLM integration and model routing                                         │
│  - Memory, context, and knowledge management                                 │
│  - Multi-agent patterns and protocols                                        │
│  - Infrastructure identity (SPIFFE/workload identity)                        │
│  - Capacity constraints and availability characteristics                     │
└─────────────────────────────────────────────────────────────────────────────┘
```

### 3.1 Raw Agents: The Deployable Artifact

**Definition (AOSM-aligned):** A Raw Agent is the deployable technical artifact—the software application or container—that implements the foundational mechanisms for agent behavior: sensing (Perception), reasoning (Interpretation/Decision), and acting (Action execution).

In AOSM terms, a Raw Agent possesses **Abilities** (technical execution capabilities) but has not yet been assigned **Knowledge** (organizational/domain), **Skills** (task-specific behaviors), **Role**, or **Responsibilities**.

**Characteristics:**

| Dimension | Description |
|-----------|-------------|
| **Deployment Artifact** | Container image, serverless function, Kubernetes deployment |
| **Identity** | Infrastructure identity (SPIFFE SVID, cloud workload identity) |
| **Ownership** | Platform engineering team |
| **Change Process** | Standard software deployment (CI/CD, staging, canary) |
| **Versioning** | Semantic versioning of the codebase |
| **Multi-tenancy** | Designed for multi-tenant operation |
| **Availability** | Critical characteristic—capacity constraints, scaling limits, SLAs |
| **OPD (as Property)** | Observable by System Operators: metrics, health, availability, orchestration traces |

**Capabilities (Abilities) a Raw Agent Provides:**

1. **Modality Support**
   - Text, voice, vision, multimodal input/output
   - Streaming and batch processing modes

2. **Orchestration Capabilities**
   - Agent loop implementation (observe → think → act → reflect)
   - Context window management and summarization
   - Memory integration infrastructure (episodic, semantic, procedural)
   - Knowledge retrieval (RAG) orchestration

3. **Multi-Agent Patterns**
   - Supervisor/worker topologies
   - Peer collaboration protocols
   - Handoff and escalation patterns
   - State sharing and coordination

4. **Interaction Channels**
   - HTTP/REST, gRPC, WebSocket
   - Message queues (Kafka, SQS)
   - Event-driven invocation

5. **Model Integration**
   - Model routing and failover
   - Whitelisted/blacklisted model providers
   - Token management and rate limiting

6. **Role Optimization** (optional specialization)
   - Some Raw Agents optimize for specific PIDA responsibilities:
     - **Thinker:** Deep reasoning, analysis, planning (Interpretation-heavy)
     - **Doer:** Action execution, tool invocation (Action-heavy)
     - **Governor:** Policy enforcement, safety checks (Decision-heavy)
     - **Orchestrator:** Workflow coordination, delegation (Coordination-heavy)

**Optional: Industry/Domain Pre-Training**

A Raw Agent *may* have specialized knowledge about an industry domain that it was fine-tuned for (e.g., banking terminology, healthcare protocols). This is:
- **Public or proprietary** to the agent developer
- **Industry-level**, not organization-specific
- **Optional**—many Raw Agents are domain-agnostic

This allows Zeta to ship Raw Agents with baseline domain understanding while remaining organization-unaware.

**What a Raw Agent Does NOT Have:**

| AOSM Concept | Raw Agent Status |
|--------------|------------------|
| **Knowledge** (organizational) | None—unaware of tenant, policies, or procedures |
| **Skills** (task-specific) | None—no task-specific training |
| **Role** | None assigned—not part of any Goal hierarchy |
| **Responsibilities (PIDA)** | None bound—no specific duties |
| **Goals** | None—not pursuing any organizational objectives |
| **Authority** | None—cannot act on behalf of any principal |
| **Mental Model** | None—no understanding of team, task, or context |

> **Design Note: Sub-Layer Consideration**
> 
> The Raw Agent layer bundles several concerns with potentially different lifecycles (orchestration code, container artifact, model integration, infrastructure identity). A finer sub-layer decomposition has been considered and is **parked for future iterations** of this framework. The current single-layer model will be validated through adoption; if governance friction emerges due to the bundling, sub-layer separation will be revisited in subsequent versions.

**Capacity and Availability:**

Raw Agents have inherent **capacity constraints** that must be managed:
- Concurrent request limits
- Token throughput bounds
- Memory and compute resource limits
- Cold start latency (for serverless)

**Availability** is a critical characteristic scoped to the Raw Agent—it determines whether the agent can participate in a HAT at any given time.

---

### 3.2 Trained Agents: Tenant-Configured with Knowledge and Skills

**Definition (AOSM-aligned):** A Trained Agent is a Raw Agent that has been configured with organizational **Knowledge**, domain-specific **Skills**, defined **Responsibilities**, and a **Role** within a tenant's Goal hierarchy—but has not yet been granted **Authority** to act.

In AOSM terms, a Trained Agent represents the outcome of *Training*—the development of Knowledge, Skills, and Abilities appropriate to an assigned Role. Its capabilities are **latent**—ready but not activated.

**Characteristics:**

| Dimension | Description |
|-----------|-------------|
| **Configuration Artifact** | Training Spec (declarative configuration) |
| **Identity** | Application identity within tenant domain |
| **Ownership** | Domain/product team within the tenant |
| **Change Process** | Configuration management (version control, approval workflows) |
| **Versioning** | Training Spec version (independent of Raw Agent version) |
| **Multi-tenancy** | Always scoped to a single tenant |

**Capabilities (KSA) Added Through Training:**

| KSA Component | What is Added |
|---------------|---------------|
| **Knowledge** | Domain facts, organizational memory, relevant context, industry regulations |
| **Skills** | Task-specific behaviors, problem-solving patterns, tool usage proficiency |
| **Abilities** | Inherited from Raw Agent, now directed toward specific Responsibilities |

**Training Spec Components:**

The Training Spec is a composite that **references** several independent artifacts. Each referenced artifact has its own lifecycle, versioning, and governance. The Training Spec does not own these artifacts—it binds them together for a specific agent configuration.

1. **Context Definitions** *(integral to Training Spec)*
   - Tenant identity and organizational context
   - Business domain and function
   - Role and responsibility definitions (PIDA mapping)
   - Operating constraints and expectations

2. **Behavioral Configuration** *(integral to Training Spec)*
   - System prompts and instructions
   - Organization style and tone guidelines
   - Response format specifications
   - Procedures encoding (organizational protocols, escalation paths)

3. **Guardrails** *(independent artifact, referenced)*
   - Prohibited behaviors and safety constraints
   - **Cannot be overridden at Employment**
   - May evolve independently based on controlling authority (security, compliance)
   - Training Spec references guardrail version (semantic versioning)

4. **Tool Specifications** *(independent artifact, referenced)*
   - Tool schemas, descriptions, usage patterns
   - Tool usage policies and constraints
   - Evolve based on tool provider lifecycle
   - Training Spec references tool spec version (semantic versioning)
   - **Sandbox validation**—training may involve role-playing exercises

5. **Knowledge Bases** *(independent artifact, accessed by reference)*
   - Accessible knowledge bases and indices
   - Retrieval strategies and ranking
   - Knowledge refresh policies
   - Training Spec references knowledge base version (semantic versioning)

6. **Memory Training** *(integral to Training Spec)*
   Training enhances multiple memory types (ref: Reflexion):
   - **Tool memory**: How to use specific tools, past tool interactions
   - **Procedural memory**: Step-by-step processes, workflows, decision trees
   - **Semantic memory**: Domain concepts, organizational knowledge, facts

> **Versioning Model**: All referenced artifacts (Guardrails, Tool Specifications, Knowledge Bases) follow **semantic versioning** compatibility rules. The Training Spec specifies compatible version ranges (e.g., `guardrails: ^2.1.0`, `tools/ticket-system: ~3.0`). Incompatible updates to referenced artifacts require explicit Training Spec updates.

**Trained Agent Spec = Training Spec + Tenant Identity**

The Trained Agent Spec binds a Training Spec to a tenant's identity system:
- Application registration in tenant's identity provider
- Service principal or managed identity
- Audit trail correlation identifiers

**AOSM Status of a Trained Agent:**

| AOSM Concept | Trained Agent Status |
|--------------|----------------------|
| **Knowledge** | ✓ Domain and organizational knowledge acquired |
| **Skills** | ✓ Task-specific skills developed through training |
| **Abilities** | ✓ Inherited from Raw Agent |
| **Role** | ✓ Assigned—set of Responsibilities necessary to fulfill Goals |
| **Responsibilities (PIDA)** | ✓ Defined—what to Perceive, Interpret, Decide, Act |
| **Goals** | ✓ Assigned—part of tenant's Goal hierarchy |
| **Authority** | ✗ None—knows *what* to do but not authorized *to* do it |
| **Mental Model** | Partial—understands task and domain, not operational context |
| **Procedures** | ✓ Organizational protocols encoded |

**What a Trained Agent Does NOT Have:**
- Credentials to access external systems
- Authority to act on behalf of users
- Access tokens or delegated permissions
- Scope to specific work contexts

**Training Approaches:**

Training can be achieved through various methods:
- Prompt engineering and system instruction configuration
- Fine-tuning on domain-specific data
- Role-playing exercises in sandbox environments
- Feedback loops from evaluation and correction
- Knowledge base population and retrieval tuning

**Layering of Training:**
Training can be composed and refined:
- Base training for general organizational behavior
- Domain training for specific business function
- Role training for particular responsibilities

```
Organization Base Training
    └── Customer Support Domain Training
            └── Tier-1 Resolution Role Training
            └── Escalation Handler Role Training
```

**Trained Agent Blueprints (Zeta Product Concept):**

Zeta may ship **Trained Agent Blueprints**—pre-configured Training Specs for domains where Zeta has requisite understanding of potential tenant environments. These are "nearly trained" agents that require minimal tenant-specific customization:

- Banking compliance domain blueprints
- Customer service domain blueprints
- Document processing domain blueprints

Blueprints accelerate deployment while allowing tenants to layer additional training.

---

### 3.3 Employed Agents: Delegated Authority

**Definition (AOSM-aligned):** An Employed Agent is a Trained Agent that has been granted delegated **Authority**, allocated to a specific **team context**, and assigned **RASCI responsibilities**—operating under **Controlled Autonomy** with a designated **Accountable** human.

In AOSM terms, an Employed Agent is a full participant in a Human-AI Team, with all Four Components of Autonomy present: Authority, Availability, Capability, and Capacity.

**Characteristics:**

| Dimension | Description |
|-----------|-------------|
| **Authorization Artifact** | Employment Spec (delegation configuration) |
| **Identity** | Identity in Workforce IAM or Customer IAM |
| **Ownership** | Delegating principal (user, role, or manager) |
| **Change Process** | Access management (PAM, just-in-time, approval workflows) |
| **Versioning** | Employment Spec version |
| **Scope** | Specific work context (team, project, customer) |
| **Capacity** | Resource quota/budget allocated for this employment |
| **OPD (as Property)** | Observable/Directable by HAT team members per role; observers/directors specified in Employment Spec |

**Employment Spec Components:**

1. **Work Scope**
   - Project or team boundaries
   - Temporal scope (duration, schedule)
   - Functional scope (what types of work)

2. **Operational Environment** (AOSM Environment)
   
   > **Note**: "Operational Environment" is distinct from "deployment stage" (dev/staging/production). Deployment stage is a software lifecycle concept. Operational Environment is the AOSM concept—the concrete machines, tools, and endpoints the agent interacts with.
   
   The **Environment** in AOSM terms is the concrete context in which the Employed Agent operates—the machines, sensors, tools, and actuators that constitute the HAT's operational reality:
   
   - **Connection strings** to databases, APIs, message queues
   - **Credentials** for accessing external systems (encrypted, rotated)
   - **Tool endpoints** with their specific configurations
   - **Machine/sensor bindings** if applicable
   - **Knowledge base locations** (vector stores, document indices)
   - **Communication channels** (Slack workspace, email server, etc.)
   
   > **Note**: The Operational Environment makes a Trained Agent's abstract tool specifications concrete. Training says "can use a ticket system"; Employment says "connect to Zendesk at api.zendesk.com with these credentials."

3. **Capacity and Resources**
   - **Resource quota/budget** allocated for this employment
   - Token limits, API call budgets, compute allocation
   - Cost attribution and chargeback identifiers
   - Throttling and rate limiting policies

5. **Authority Delegation Model**

   **A. User Delegation (Customer or Employee)**
   - The Employed Agent acts as a delegate of a specific user
   - Identity is derived from the delegating user's identity
   - Similar to OAuth client credentials with user consent
   - Authority is always a subset of delegator's current authority
   
   ```
   Delegating User (Alice, has permissions A, B, C, D)
       └── Employed Agent (Alice's Delegate, granted A, B only)
   ```

   **B. Role Delegation (Organizational)**
   - The Employed Agent represents an organizational role, not a user
   - Primary identity in Workforce IAM (like an autonomous employee)
   - Can participate in IAM groups and assume IAM roles
   - Must have a designated **Manager** (user, role, or group)—the Accountable human
   
   ```
   Organizational Role (Compliance Reviewer)
       └── Employed Agent (Compliance Agent, has role's permissions)
           └── Manager: Compliance Team Lead (Accountable)
   ```

6. **Constraints and Policies**
   - Action limits (rate, volume, value)
   - Approval requirements (dual control for high-risk actions)
   - Prohibition lists (explicit denials)
   - Escalation triggers

7. **Delegator Preferences** (expressed as prompts)
   - Communication style preferences
   - Decision-making guidelines
   - Notification and reporting expectations

**Critical Constraint: Training Guardrails Are Immutable**

> An Employed Agent may **never override the guardrails** set during Training.

Employment can **specialize** the Trained Agent's behavior (narrow scope, add constraints, express preferences) but can **never expand** beyond what Training permits:

| Employment Can Do | Employment Cannot Do |
|-------------------|----------------------|
| Restrict tool access | Enable tools not in Training |
| Narrow scope of actions | Expand action authority beyond Training |
| Add delegator preferences | Override Training guardrails |
| Set resource quotas | Remove safety constraints |
| Specify work context | Grant capabilities not trained |

**AOSM Status of an Employed Agent:**

| AOSM Concept | Employed Agent Status |
|--------------|----------------------|
| **Authority** | ✓ Delegated—right to act within defined scope |
| **Autonomy** | ✓ Controlled Autonomy—acts within bounds set by Accountable human |
| **Allocation** | ✓ Assigned to a specific Human-AI Team |
| **RASCI** | ✓ Responsible for specific activities, with human Accountable |
| **OPD** | ✓ Observable/Directable by HAT team members; authorized observers/directors per Employment Spec |
| **Mental Model** | ✓ Complete—shared understanding with team members |
| **Coordination** | ✓ Active participant in team coordination |

**Learning and Feedback Loop:**

An Employed Agent operates within its Training bounds but can **suggest learnings** to be incorporated into future Training versions:

```
Employed Agent (runtime)
    │
    ├── Operates within Training guardrails
    │
    └── Suggests learnings ──→ Trainer (human or agent)
                                    │
                                    └── Reviews with change management controls
                                        │
                                        └── Incorporates into Trained Agent v(n+1)
```

This preserves the integrity of the Training layer while enabling continuous improvement.

> **Governance Note**: The "Trainer" is not necessarily a single individual or agent, and the update is not a straight-through process. Learning suggestions are subject to **change management controls** appropriate to the Training artifact being modified. Guardrail changes require elevated review; prompt tweaks may have lighter governance. The review process must include controls to prevent malicious updates from compromised Employed Agents.

**Authority Inheritance Rule:**

> The delegated authority at any time is always a subset of what the delegator is currently authorized to do, irrespective of what authority was available at the time of delegation.

This means:
- If Alice delegates permissions A and B to an agent
- And Alice later loses permission B
- The agent immediately loses access to B as well
- The agent's authority shrinks in real-time with the delegator's authority

**Implementation Note:** Real-time authority synchronization requires infrastructure support. In Zeta's context, the **Cipher IAM** system with its Policy Enforcement Points (PEPs) provides this capability. Third-party systems can implement PEPs using Cipher SDKs and sidecars. Specific implementation patterns will be detailed in platform technical design documents. (See [Appendix C: Feasibility and Implementation Considerations](#appendix-c-feasibility-and-implementation-considerations))

---

### 3.4 OPD Across Agent Layers

The term **OPD** (Observability, Predictability, Directability) is used in two distinct but related senses in this framework. This section clarifies the distinction and how OPD applies differently at each agent layer.

#### OPD as Agent Capability (Agent → Environment)

Every agent in an AOS has OPD **capabilities** to interact with its environment:

| Element | Meaning | Relation to PIDA |
|---------|---------|------------------|
| **Observe** | Agent senses machine/environment state | Perception |
| **Predict** | Agent anticipates next state of environment | Interpretation |
| **Direct** | Agent decides if action is required and triggers it | Decision + Action |

This is part of the agent's PIDA responsibilities—its ability to observe, predict, and direct actions toward machines and other entities in the AOS.

#### OPD as Agent Property (Others → Agent)

The agent itself must be **observable, predictable, and directable BY** other agents, supervisors, and operators. This has two distinct layers:

| Layer | Subject (Who Observes) | Object | What They See | Purpose |
|-------|------------------------|--------|---------------|---------|
| **System/Infrastructure** | System Operators | Raw Agent | Metrics, resources, cost, availability, health, orchestration traces | Operational management |
| **AOS/Data Plane** | HAT Team Members | Employed Agent | Activities, decisions, state, behavior | Team coordination, oversight |

#### Role-Based Visibility in HAT

Within the Human-AI Team, different roles have different OPD scopes:

| HAT Role | Observability Scope | Directability Scope |
|----------|---------------------|---------------------|
| **Delegator** | All activities of agents they delegated to | Full direction within delegation scope |
| **Team Member** | Relevant activities to coordinate | Based on coordination needs |
| **Supervisor/Overwatch** | All activity, deviations, failures | Review, intervention, correction |
| **Accountable Human** | All activity with explanations | Kill-switch, revocation, override |

#### The Observer's PIDA Loop

When we say an agent must be "observable, predictable, directable," we are enabling the **observer's own PIDA cycle**:

```
Observer (Human or Agent in HAT)
    │
    ├── Observes the target agent (O)
    │
    ├── Predicts what the agent will do next (P)
    │       └── Based on agent's known behavior, state, context
    │
    └── Directs the agent if intervention needed (D)
            └── Includes deciding whether to direct
```

**Key insight:** "Predictability" is not a passive property ("the agent is predictable"). It is the **observer's ability** to predict the agent's behavior, which feeds into the observer's own decision-making.

#### OPD by Agent Layer

| Layer | OPD Capability (→ Environment) | OPD Property (← Observers) |
|-------|-------------------------------|---------------------------|
| **Raw Agent** | Technical ability to observe/predict/direct machines | Observable by System Operators (metrics, health, traces) |
| **Trained Agent** | Domain-directed observation and action patterns | Minimal — may be probed for info on Employed Agents it supports |
| **Employed Agent** | Contextualized OPD within delegated scope | Observable/Directable by HAT team members per role |

#### Specifying OPD in Employment Spec

The Employment Spec should explicitly define authorized observers and directors:

```yaml
opd_authorization:
  observers:
    - role: delegator
      agent: alice@workforce.corp
      scope: all_activities
    - role: supervisor
      agent: compliance-team
      scope: all_activities_with_review
    - role: team_member
      agent: bob@workforce.corp
      scope: relevant_activities
  directors:
    - role: delegator
      agent: alice@workforce.corp
      scope: full_within_delegation
    - role: supervisor
      agent: compliance-lead@workforce.corp
      scope: intervention_override
    - role: accountable
      agent: manager@workforce.corp
      scope: kill_switch_revocation
```

This may be derived from the AOS specification that the HAT is part of, or explicitly stated in the Employment Spec.

---

## 4. Composition and Relationships

### 4.1 The Composition Model

```
┌─────────────────────────────────────────────────────────────────┐
│                    EMPLOYED AGENT SPEC                           │
│  ┌───────────────────────────────────────────────────────────┐  │
│  │ Employment Spec                                            │  │
│  │  - Work scope, delegation model, credentials, policies    │  │
│  │  - Capacity/quota, delegator preferences                   │  │
│  └───────────────────────────────────────────────────────────┘  │
│                              ▼                                   │
│                         references (cannot expand)               │
│                              ▼                                   │
│  ┌───────────────────────────────────────────────────────────┐  │
│  │ TRAINED AGENT SPEC                                         │  │
│  │  ┌─────────────────────────────────────────────────────┐  │  │
│  │  │ Training Spec                                        │  │  │
│  │  │  - Knowledge, skills, prompts, tools, guardrails     │  │  │
│  │  └─────────────────────────────────────────────────────┘  │  │
│  │                          + Tenant Identity                 │  │
│  └───────────────────────────────────────────────────────────┘  │
│                              ▼                                   │
│                         deployed on                              │
│                              ▼                                   │
│  ┌───────────────────────────────────────────────────────────┐  │
│  │ RAW AGENT                                                  │  │
│  │  - Orchestration code, runtime, infrastructure identity   │  │
│  │  - Capacity constraints, availability characteristics     │  │
│  └───────────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────────┘
```

### 4.2 Many-to-Many Relationships

- **One Raw Agent** can host **many Trained Agents** (multi-tenant deployment)
- **One Trained Agent** can have **many Employed instances** (multiple delegations)
- **One User** can delegate to **many Employed Agents** (multiple helpers)
- **One Employed Agent** references **one Trained Agent** (fixed training per employment)

### 4.3 Versioning Independence

Each layer is versioned independently:

| Layer | Version Example | What Changes |
|-------|-----------------|--------------|
| Raw Agent | `v2.4.1` | Orchestration code, model integrations, capacity |
| Training Spec | `v1.7.0` | Knowledge, skills, prompts, tool training, guardrails |
| Employment Spec | `v3.2.0` | Delegation scope, credentials, policies, quotas |

An Employed Agent's complete version might be expressed as:
```
raw:v2.4.1/trained:v1.7.0/employed:v3.2.0
```

**Cross-Layer Version Compatibility:**

Dependencies between layers follow **semantic versioning** rules:
- **Trained Agent → Raw Agent**: Training Spec declares compatible Raw Agent version range (e.g., `raw: ^2.0.0`)
- **Employed Agent → Trained Agent**: Employment Spec declares compatible Training Spec version (e.g., `trained: ~1.7.0`)

When a Raw Agent is upgraded, Trained Agents specifying compatible version ranges continue to function. Incompatible upgrades require explicit Training Spec updates and re-validation.

### 4.4 Multi-Agent Delegation

In multi-agent architectures, delegation semantics and patterns are **defined by each Raw Agent** based on its delegation capabilities:

- Some Raw Agents support supervisor/worker patterns with internal delegation
- Some support peer-to-peer coordination protocols
- Some support handoff patterns between agents

The specifics of how authority flows between collaborating agents are determined by the Raw Agent's architecture and documented in its specifications. This framework defines the layers; the Raw Agent defines the composition patterns.

---

## 5. Lifecycle Implications

### 5.1 State Transitions

```
        ┌─────────────────────────────────────────────────────────────┐
        │                        RAW AGENT                             │
        │   [Developed] → [Built] → [Deployed] → [Running] → [Retired]│
        └─────────────────────────────────────────────────────────────┘
                                      │
                                      ▼ trained with
        ┌─────────────────────────────────────────────────────────────┐
        │                        TRAINED AGENT                         │
        │   [Drafted] → [Validated] → [Published] → [Active] → [Archived]│
        └─────────────────────────────────────────────────────────────┘
                                      │
                                      ▼ employed as
        ┌─────────────────────────────────────────────────────────────┐
        │                       EMPLOYED AGENT                         │
        │   [Requested] → [Approved] → [Active] → [Suspended] → [Revoked]│
        └─────────────────────────────────────────────────────────────┘
```

### 5.2 Ownership and Responsibility (RASCI Aligned)

| Layer | Owner (Responsible) | Approver | Auditor | Accountable |
|-------|---------------------|----------|---------|-------------|
| Raw Agent | Platform Team | Platform Lead + Security | Platform Audit | Platform Lead |
| Trained Agent | Domain Team | Domain Lead + Compliance | Domain Audit | Domain Lead |
| Employed Agent | Delegating Principal | Manager + Security | Access Audit | Manager (human) |

### 5.3 Incident Response by Layer

| Issue Type | Layer | First Responder | Action |
|------------|-------|-----------------|--------|
| Crash/OOM | Raw | Platform SRE | Restart/Scale |
| Hallucination | Raw/Trained | AI Engineering | Prompt/Guard update |
| Wrong domain behavior | Trained | Domain Team | Training Spec revision |
| Unauthorized action | Employed | Security | Delegation revocation |
| Guardrail violation | Trained | Domain + Security | Training review |
| Data breach | All | Security + Legal | Full investigation |

---

## 6. Governance Implications

### 6.1 Change Management Matrix

| Change Type | Layer | Review Required | Approval Gate | Rollback |
|-------------|-------|-----------------|---------------|----------|
| Code patch | Raw | Code review | Platform lead | Redeploy previous |
| Model upgrade | Raw | Eval + security | Platform + AI lead | Revert config |
| Capacity change | Raw | Ops review | Platform lead | Previous config |
| Knowledge update | Trained | Content review | Domain lead | Re-index previous |
| Prompt update | Trained | Domain review | Domain lead | Version rollback |
| Tool training | Trained | Security review | Domain + security | Remove from spec |
| Guardrail change | Trained | Security + compliance | Domain + security lead | Version rollback |
| Scope expansion | Employed | Risk assessment | Delegator + security | Reduce scope |
| Quota change | Employed | Budget review | Delegator | Previous quota |
| Credential rotation | Employed | Automated | None (standard) | N/A |
| Delegation revocation | Employed | None | Security (emergency) | Re-delegate |

### 6.2 Audit Trail Requirements

**Raw Agent Audit:**
- Deployment events (who, when, what version)
- Configuration changes
- Error and crash logs
- Resource utilization and capacity metrics
- Availability events

**Trained Agent Audit:**
- Training Spec version history
- Prompt, knowledge, and tool changes
- Guardrail modifications (requires elevated review)
- Sandbox validation results
- Activation/deactivation events

**Employed Agent Audit:**
- Delegation events (who delegated, what scope, when)
- Authority exercises (what actions, under whose authority)
- Credential usage
- Resource quota consumption
- Learning suggestions submitted
- Revocation events

**Correlation Requirement:**
Every agent action must be traceable to:
1. The Raw Agent version executing
2. The Training Spec version in effect
3. The Employment Spec governing authority
4. The delegating principal (Accountable human)

---

## 7. Open Questions for Discussion

### 7.1 Identity and Authority

**Q1: Real-time Authority Synchronization**
When a delegator's permissions change, how quickly must the Employed Agent's authority reflect this change?
- Immediate (synchronous policy check)?
- Near-real-time (event-driven propagation)?
- At refresh (token expiration boundary)?

**Q2: Manager Role for Autonomous Agents**
For Employed Agents with role-based (not user-based) delegation:
- Is the "manager" a technical construct (system account) or organizational (named person)?
- What are the manager's responsibilities and liabilities?
- Can the manager role be delegated?

**Q3: Delegation Chains**
Can an Employed Agent delegate to another Employed Agent?
- If yes, what is the authority inheritance model?
- If no, how do we handle legitimate multi-hop workflows?

### 7.2 Lifecycle and Operations

**Q4: Raw Agent Updates**
When a Raw Agent is patched:
- Must all Trained Agents be re-validated?
- Must all Employed Agents be re-authorized?

*Partial Answer:* Cross-layer version compatibility follows semantic versioning (see Section 4.3). Trained Agents specify compatible Raw Agent version ranges. Incompatible upgrades require explicit re-validation.

**Q5: Training Spec Portability**
Can a Training Spec be migrated to a different Raw Agent?
- What is the compatibility surface?
- Who approves such migrations?

**Q6: Employment Inheritance**
When a Trained Agent is updated:
- Do existing Employed Agent instances automatically inherit the changes?
- Or must they be explicitly upgraded?
- How are guardrail changes propagated?

**Q7: Learning Incorporation**
When an Employed Agent suggests learnings:
- What is the review process for incorporating into Training?
- Who approves Training updates based on runtime learnings?
- How is the feedback loop audited?

### 7.3 Multi-Agent Architectures

**Q8: Cross-Layer Orchestration**
In a multi-agent system:
- Can a Raw Agent (orchestrator) coordinate Employed Agents directly?
- Or must orchestration happen at the Employed Agent layer?
- How is authority delegation managed across agent boundaries?

*Partial Answer:* Multi-agent delegation semantics are defined by each Raw Agent based on its delegation capabilities (see Section 4.4). The framework defines layers; Raw Agents define composition patterns.

**Q9: Shared Training**
Can two Employed Agents share the same Training Spec but have different Employment Specs?
- If yes, how is isolation ensured?
- If no, what is the duplication cost?

### 7.4 Security and Compliance

**Q10: Credential Isolation**
How are Employed Agent credentials isolated when the same Raw Agent hosts multiple Employed Agents?
- Process isolation?
- Memory isolation?
- Hardware security modules?

**Q11: Audit Correlation**
In high-volume scenarios, how do we efficiently correlate:
- LLM inference logs (model provider)
- Orchestration logs (Raw Agent)
- Training context (Trained Agent)
- Action logs (Employed Agent)
- Without excessive performance overhead?

**Q12: Guardrail Enforcement**
How do we ensure that Training guardrails cannot be bypassed at Employment?
- Runtime enforcement mechanisms?
- Cryptographic binding of Training constraints?
- Audit detection of guardrail violations?

*Partial Answer:* One potential approach is sidecar-based enforcement, where guardrails are evaluated independently from the primary reasoning loop. Guardrails are intended to block and alert. Specific enforcement mechanisms will be detailed in platform technical design. (See Appendix C)

---

## 8. Summary: What Zeta Hopes to Achieve

For Zeta's context—building bank-grade agent products with multi-tenant deployment and delegated authority within the Human-AI Team paradigm—the three-layer model offers several potential benefits:

| Intended Benefit | Mechanism |
|------------------|-----------|
| **Clearer ownership** | Each layer has a distinct owner and change process |
| **Proportionate governance** | Change management scales to the risk of each layer |
| **Traceable audit** | Actions can be correlated through all three layers to Accountable human |
| **Faster incident routing** | Issues are routed based on which layer is at fault |
| **Explicit delegation** | Authority is bounded, constrained by Training, and revocable |
| **Multi-tenant isolation** | Infrastructure is shared; Training and Employment are isolated |
| **Independent evolution** | Layers can be versioned and updated separately |
| **Guardrail integrity** | Training guardrails cannot be overridden at Employment |
| **Continuous improvement** | Employed Agents can suggest learnings for Training |
| **Product distribution** | Trained Agent Blueprints enable productized agent delivery |

This framework is a proposal, not a prescription. We expect it to evolve as we implement and learn.

For teams in different contexts—internal tools, single-tenant deployments, or domains without stringent delegation requirements—simpler models may be more appropriate. The value of any terminology is proportional to the coordination challenges it addresses.

**Grounding in AOSM:** This terminology is explicitly designed for Enterprise Information Systems modeled as Human-AI Teams conforming to the AOSM meta-model, where Controlled Autonomy, RASCI accountability, and OPD requirements are foundational.

---

## Appendix A: Glossary

### Agent Terminology

| Term | Definition |
|------|------------|
| **Raw Agent** | Deployable application artifact with technical capabilities (Abilities) but no organizational Knowledge, Skills, Role, or Authority |
| **Trained Agent** | Raw Agent configured with organizational Knowledge, domain Skills, defined Role, Responsibilities, and Procedures—but no Authority |
| **Employed Agent** | Trained Agent with delegated Authority, allocated to a Human-AI Team, operating under Controlled Autonomy |
| **Training Spec** | Declarative configuration of knowledge, skills, prompts, tools, guardrails, and procedures |
| **Employment Spec** | Delegation scope, credentials, authority constraints, capacity quotas, and delegator preferences |
| **Trained Agent Blueprint** | Pre-configured Training Spec for a domain, shipped by Zeta as part of agent products |

### AOSM Terms

| Term | Definition |
|------|------------|
| **Capabilities (KSA)** | Knowledge, Skills, and Abilities—what an agent can do |
| **PIDA** | Perception, Interpretation, Decision, Action—the four types of Responsibilities |
| **Role** | Set of Responsibilities necessary to fulfill a Goal |
| **Controlled Autonomy** | Acting autonomously only within bounds set by responsible human |
| **OPD** | Observability, Predictability, Directability—bidirectional: (1) Agent's capability to OPD environment, (2) Agent's property of being OPD'd by others |
| **OPD as Capability** | Agent's ability to observe/predict/direct machines and environment (relates to PIDA) |
| **OPD as Property** | Agent being observable/predictable/directable BY System Operators (infrastructure) or HAT team members (data plane) |
| **RASCI** | Responsible, Accountable, Supporting, Consulted, Informed—responsibility assignment |
| **Four Components of Autonomy** | Authority, Availability, Capability, Capacity |
| **Human-AI Team (HAT)** | Two or more agents (humans and/or AI) working interdependently |

### Authority Terms

| Term | Definition |
|------|------------|
| **Delegator** | Principal (user or role) that grants authority to an Employed Agent |
| **Manager** | Human with Accountable role for role-delegated Employed Agents |
| **Authority Inheritance** | Rule that agent authority ≤ delegator's current authority |
| **Guardrail** | Constraint set during Training that cannot be overridden at Employment |

### Operational Terms

| Term | Definition |
|------|------------|
| **Operational Environment** | The concrete AOSM Environment in which an Employed Agent operates—connection strings, credentials, tool endpoints, machine bindings, and other parameters that make abstract Training specifications concrete |
| **Deployment Stage** | The software lifecycle phase (dev, staging, production)—distinct from Operational Environment |

## Appendix B: Example Scenarios

### Scenario 1: Customer Support Agent

```
RAW AGENT: "Atlas Orchestrator v2.1"
  - Multi-turn conversation management
  - RAG integration, tool calling
  - Deployed as Kubernetes service
  - SPIFFE identity: spiffe://platform/atlas
  - Capacity: 1000 concurrent sessions, 50 req/sec
  - Availability: 99.9% SLA

    ↓ trained with

TRAINED AGENT: "Acme Corp Support Agent"
  - Training Spec v1.4
  - Knowledge: Acme product catalog, support procedures
  - Skills: ticket triage, FAQ response, escalation detection
  - System prompts for Acme's brand voice
  - Tools: ticket lookup (trained), knowledge base search (trained)
  - Guardrails: no refund authority, escalate complaints, no PII disclosure
  - Application identity: support-agent@acme.corp

    ↓ employed as

EMPLOYED AGENT: "Tier-1 Support Bot"
  - Employment Spec v2.0
  - Delegated by: Support Team Lead role
  - Work Scope: Tier-1 tickets in NA region
  - Deployment Stage: production
  - Operational Environment:
      - Zendesk: api.zendesk.com (API key: vault://zendesk-prod)
      - Customer DB: customers.acme.internal:5432 (read-only)
      - Knowledge Base: kb-vectors.acme.internal
  - Quota: 500 sessions/day, $50/day inference budget
  - Manager (Accountable): @sarah.chen (Support Manager)
  - Workforce identity: tier1-bot@workforce.acme.corp
  - OPD Authorization:
      - Observers:
          - @sarah.chen (delegator): all_activities
          - support-leads (role): all_activities_with_review
      - Directors:
          - @sarah.chen: full_within_delegation
          - support-leads: intervention, kill-switch
```

### Scenario 2: Enterprise Personal Assistant

```
RAW AGENT: "Hermes Assistant v3.0"
  - Calendar, email, task management
  - Voice and text modalities
  - Deployed as AWS Lambda
  - Workload identity: arn:aws:iam::hermes-prod
  - Capacity: 100 concurrent users, cold start <2s

    ↓ trained with

TRAINED AGENT: "Executive Assistant"
  - Training Spec v2.1
  - Knowledge: company directory, meeting policies, org chart
  - Skills: scheduling, email drafting, meeting prep
  - Tone: professional, concise
  - Tools: calendar (trained), email draft (trained), task creation (trained)
  - Guardrails: cannot send emails (only draft), cannot access HR systems
  - Application identity: exec-assistant@tenant

    ↓ employed as

EMPLOYED AGENT: "Alice's Assistant"
  - Employment Spec v1.0
  - Delegated by: Alice (VP Engineering)
  - Work Scope: Alice's calendar, Alice's email drafts
  - Deployment Stage: production
  - Operational Environment:
      - Calendar: graph.microsoft.com/calendar (OAuth: alice-delegate)
      - Email: graph.microsoft.com/mail (OAuth: alice-delegate, draft-only)
      - Directory: graph.microsoft.com/users (read-only)
  - Authority: Cannot send emails (inherits Training guardrail)
  - Quota: Unlimited within Alice's budget allocation
  - Preferences: Prefer 30-min meetings, block focus time 9-11am
  - Customer identity: alice-assistant@alice.user.id
  - Accountable: Alice (self-managed delegation)
```

### Scenario 3: Compliance Monitoring Agent (Role Delegation)

```
RAW AGENT: "Sentinel Monitor v1.5"
  - Continuous monitoring, anomaly detection
  - Multi-source data integration
  - Deployed as Kubernetes StatefulSet
  - SPIFFE identity: spiffe://platform/sentinel
  - Capacity: 10K events/sec, 1TB memory

    ↓ trained with (from Zeta Blueprint)

TRAINED AGENT: "Banking Compliance Monitor"
  - Training Spec v3.0 (based on Zeta Trained Agent Blueprint)
  - Knowledge: Banking regulations, internal policies, violation patterns
  - Skills: Transaction monitoring, SAR detection, risk scoring
  - Guardrails: read-only access, no customer contact, mandatory escalation
  - Application identity: compliance-monitor@bank.corp

    ↓ employed as

EMPLOYED AGENT: "AML Transaction Monitor"
  - Employment Spec v1.2
  - Delegated by: Compliance Officer role (not individual user)
  - Work Scope: All wire transfers >$10K
  - Deployment Stage: production
  - Operational Environment:
      - Transaction DB: txn-db.bank.internal:5432 (read-only, encrypted)
      - Alert System: alerts.bank.internal/api (write)
      - Case Management: cases.bank.internal/api (create-only)
      - SAR Filing: fincen-gateway.bank.internal (via approval workflow)
  - Quota: Unlimited (critical function)
  - Manager (Accountable): Chief Compliance Officer
  - Workforce identity: aml-monitor@workforce.bank.corp
  - OPD Authorization:
      - Observers:
          - Chief Compliance Officer (accountable): all_activities_with_explanations
          - compliance-team (role): all_activities_with_review
          - audit-team (role): read-only audit trail
      - Directors:
          - Chief Compliance Officer: kill-switch, revocation, override
          - compliance-leads: intervention, parameter adjustment
```

---

## Appendix C: Feasibility and Implementation Considerations

> **Document Scope Clarification**
> 
> This document is a **conceptual framework**, not an implementation-ready technical design. It establishes terminology, layer boundaries, and governance principles. The platform technical design phase will address implementation details, and may introduce trade-offs or limitations against this conceptual design.

### Areas Requiring Platform Technical Design Attention

The following aspects of this framework require detailed technical design and may involve implementation trade-offs:

| Aspect | Conceptual Intent | Technical Design Consideration |
|--------|-------------------|-------------------------------|
| **Guardrail Enforcement** | Training guardrails cannot be overridden at Employment | Implementation options include sidecar-based evaluation (separate from primary reasoning loop), policy engines, or code-level constraints. Guardrails are intended to **block and alert**. |
| **Authority Inheritance** | Delegated authority shrinks in real-time with delegator's authority | Requires IAM infrastructure support (e.g., Cipher with Policy Enforcement Points). Token refresh strategies, policy evaluation timing, and revocation propagation need design. |
| **Cross-Layer Version Compatibility** | Semantic versioning governs dependencies | Compatibility testing automation, migration tooling, and rollback procedures need specification. |
| **Multi-Agent Authority Flow** | Delegation patterns defined per Raw Agent | Each Raw Agent architecture must document its delegation model. Framework-agnostic patterns may emerge. |
| **OPD Implementation** | Agents must be Observable, Predictable, Directable | Specific OPD mechanisms (dashboards, kill-switches, intervention protocols) require platform support. |
| **Credential Isolation** | Employed Agent credentials isolated in shared Raw Agent | Process isolation, memory protection, or HSM integration options need evaluation. |
| **Audit Correlation** | Actions traceable through all layers | Log aggregation, correlation ID propagation, and performance overhead need design. |

### Implementation Trade-offs to Document

The platform technical design should explicitly document any trade-offs against this conceptual framework:

- If guardrail enforcement has latency implications, document the trade-off
- If authority inheritance is eventually consistent rather than immediate, document the consistency model
- If certain Raw Agents cannot support all Training Spec features, document the compatibility constraints

### Zeta Infrastructure Assumptions

This framework assumes availability of:

- **Cipher IAM**: Identity and access management with Policy Enforcement Points
- **Semantic versioning infrastructure**: Artifact registries with version compatibility checking
- **Audit infrastructure**: Centralized logging with correlation support
- **Deployment infrastructure**: Container orchestration with sidecar support

Third-party or customer environments may require Cipher SDKs or sidecar deployment for equivalent capabilities.

---

## Invitation for Feedback

This document represents a proposed conceptual framework, not a final decision. We are seeking input on:

1. **Terminology clarity** — Are the terms Raw/Trained/Employed intuitive? Do they communicate the progression clearly?
2. **AOSM alignment** — Does the mapping to AOSM concepts (KSA, PIDA, RASCI, OPD) add value or complexity?
3. **Layer boundaries** — Are the boundaries between layers in the right places for our use cases?
4. **Guardrail model** — Is the constraint that Training guardrails cannot be overridden at Employment the right design?
5. **Learning loop** — Is the "suggest learnings" model for continuous improvement workable?
6. **Blueprint concept** — Does the Trained Agent Blueprint model support our product distribution goals?
7. **Missing concerns** — What dimensions does this framework fail to address?
8. **Implementation feasibility** — Can our platform and tooling support these distinctions?

The goal is to arrive at a shared vocabulary that serves Zeta's engineering, product, and security teams—not to impose a framework for its own sake.

---

*This is a concept proposal for internal discussion. It will evolve based on feedback and implementation experience.*

*Grounded in the Agent-Oriented Systems Modeling (AOSM) meta-model for Human-AI Teams.*
