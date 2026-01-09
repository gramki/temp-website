# Seer Agents in Hub

Seer Raw Agent -> OCI Container + CRD that Seer Operator handles; It's an application using one of the many popular agentic frameworks. The raw agent would have externalized ability ingect tools, resources, and skills (prompts). The raw agent would have inbuilt capabilities for context compilation, conversation orchestration, and even some guardrails. But the scope of raw is not bounded by the definition here. Agent developers at liberty to define them as they deem right.

Hub doesn't deploy raw agents. The CI, CD of Seer Raw Agents is in the scope of Seer.

Seer as a Hub Application Runtime runs Employed Agents. An Employed agent has references to Trained Agent and Raw Agent Specifications. Seer runs the Raw Agent in Atlantis runtime using a deployment corresponding to each Employed Agent. 

A Seer Trained Agent corresponds to a Hub Application Specification (CRD) with Seer as a runtime. The trained agent specfications as with Hub Applicaton Specification can be reused across workbenches and scenarios.  

The CRD of a Seer Trained Agent as a Hub Application Specification contains - system prompts, and skill-prompts and labels for the agent. The CRD also refers to the required hub tool specifications, hub resource specifications. 

A Seer Employed Agent in Hub is a Deployed Hub Application. The Deployment CRD of the hub maps the referenced specifications to real instances/endpoints. 

ask for clarifications you may need
----
This is a great foundation. Let me ask clarifying questions before we proceed:

---

## Clarifying Questions

### 1. Raw Agent Scope

You mentioned "the scope of raw is not bounded by the definition here." 

**Question:** Is a Raw Agent:
- **Framework-agnostic** — Could be LangChain, Strands, custom Python, etc.?
- **Always containerized** — Or could it be serverless (Lambda, etc.)?
- **Single agent only** — Or could a Raw Agent container host multiple sub-agents internally (compound agent)?
> Yes, raw agent can be written in any framework. Hub doesn't prescribe or recommend anything; Seer also doesn't specify anything
> Always containerized in both Seer and Hub contexts
> Raw Agent can be a compound agent with any toplogy. However, as far as Hub is concerned the composite is one agent. Hub doesn't recognize and control sub-agents. The lifecycle, orchestration is all responsibility of the Orchestrator application that is acting as a Raw Agent. 
---

### 2. Trained Agent ↔ Raw Agent Relationship

**Question:** Is the relationship:
- **1:1** — Each Trained Agent references exactly one Raw Agent?
- **N:1** — Multiple Trained Agents can reference the same Raw Agent (different prompts/tools)?
- **1:N** — One Trained Agent could use multiple Raw Agents (unlikely, but clarifying)?
> A Trained agent can only refer to one raw agent. However, there can be many trained agents in one or multiple workbench specifications based on one raw agent.
---

### 3. Employed Agent ↔ Trained Agent Relationship

**Question:** Is the relationship:
- **1:1** — Each Employed Agent is a deployment of exactly one Trained Agent?
- **N:1** — Multiple Employed Agents can deploy the same Trained Agent (different workbenches)?

> It is N:1. Multiple Scenario Specifications can reference the same Seer Trained Agent spec in their Hub Application CRD.  
---

### 4. Tool and Resource Binding

Trained Agent references "hub tool specifications" and "hub resource specifications."

**Question:**
- Are these **abstract references** (tool type/capability) resolved at employment time?
- Or **concrete references** (specific tool endpoints) already in Trained Agent?
- How do **Knowledge Bank references** fit? (Part of resource specs?)
> Go through hub registry-services documentation. You will see the distinctiton between normative and operative/runtime resources.
> Knowlege Bank references can be used resources; Knowledge bank itself can be used as tool too

---

### 5. Atlantis Runtime

You mentioned Seer runs Raw Agents in "Atlantis runtime."

**Question:**
- Is Atlantis a **Kubernetes operator** that manages agent container lifecycle?
- Or is it a **serverless runtime** (like Lambda)?
- Does Atlantis handle **scaling, health checks, failover**?
> Olympus Atlantis is like AWS ECS - a serverless runtime to run containers.
> See https://academy.olympus.tech/
---

### 6. Hub Application Lifecycle Alignment

For a Seer agent deployed in Hub:

| Hub Concept | Seer Equivalent | Same CRD? |
|-------------|-----------------|-----------|
| Application Spec | Trained Agent Spec | ✅ Yes? |
| Deployed Application | Employed Agent | ✅ Yes? |
| Application Runtime | Seer (Atlantis) | Runtime selection? |

**Question:** Is the Trained Agent CRD literally a `HubApplicationSpec` with `runtime: seer`? Or is it a separate Seer-specific CRD that Hub recognizes?
To Hub it is a HubApplicationSpec with `runtime: seer`; However, that CRD refers to another Seer Training Spec CRD.  

---

### 7. Scenario Binding

When a Seer agent is bound to a Hub Scenario:

**Question:**
- Is binding at **Trained Agent level** (scenario references the app spec)?
- Or at **Employed Agent level** (scenario references the deployment)?
- Can one Employed Agent serve **multiple scenarios**?
> Scenario Specification to Trained Agent
> Scenario Deployment to Employed Agent
> Scenario Deployment/Instance to Employed Agent is 1:1
---

### 8. Agent Memory + Context Assembly

With Agent Memory Services now complete:

**Question:**
- Does the **Trained Agent spec** declare memory requirements (stores needed)?
- Is memory provisioned at **employment time** or **request time**?
- Does Context Assembly Engine (CAE) compile context **per request** or **per task**?
> yes, it can declare memory stores required, or may use memory as a tool
> memory is provisioned at employment time
> Per Request and Per Request Update recevied from hub; Each update to a Hub Request translates to an invocation of Seer Employed Agent Application over https with appropriate payload
---

### 9. Documentation Structure

You mentioned "house all seer-hub integration concepts in seer-docs in a dedicated folder."

**Question:** Suggested structure:

```
olympus-seer-docs/
  seer-design/
    hub-integration/           # NEW FOLDER
      README.md                # Overview of Seer-Hub integration
      raw-agent-spec.md        # Raw Agent container + CRD
      trained-agent-spec.md    # Hub Application Spec for Seer
      employed-agent-spec.md   # Deployment CRD
      atlantis-runtime.md      # Runtime details
      lifecycle.md             # Agent lifecycle in Hub context
```

Does this structure work, or would you prefer a different organization?
> this is fine

---
Let me check the registry-services documentation to understand the normative vs operative distinction, and then ask final clarifying questions:

[2 tools called]

Excellent! The existing documentation is comprehensive. I now understand:

1. **Registry Services**: Definitions (abstract, normative) → Instances (concrete, operative)
2. **Agent Lifecycle**: Raw → Trained → Employed model is well documented

A few remaining clarifications for the **Hub integration** specifically:

---

## Final Clarifying Questions

### 1. CRD Hierarchy

Based on your answers, I understand:

```
HubApplicationSpec (runtime: seer)
    └── references → Seer TrainingSpec CRD
                        └── references → Raw Agent (container image)
```

**Question:** Is the Seer TrainingSpec CRD:
- **Managed by Seer Operator** (Hub doesn't validate its contents)?
- Or **validated by Hub** as part of HubApplicationSpec validation?

> As of now only Seer operators handle those CRDs

---

### 2. Scenario ↔ Agent Binding

You said: "Scenario Deployment to Employed Agent is 1:1"

**Question:** When a Scenario is deployed:
- Does Hub create the Employed Agent (via Seer API)?
- Or does Hub reference an already-created Employed Agent?
- Who triggers the actual container deployment in Atlantis — Hub or Seer?

> Hub creates a deployment spec of the Seer Agent Application. As seer is the runtime for this, the Seer operator picks this spec and materializes the Employed Agent. So employed agent is created in the Scenario Deployment process through orchestration of operators.  
---

### 3. Request → Agent Invocation

You mentioned: "Each update to a Hub Request translates to an invocation of Seer Employed Agent Application over HTTPS"

**Question:** 
- Is this HTTPS call made by **Hub directly** to the agent container?
- Or routed through **Seer** (Seer as intermediary)?
- What's the payload structure — Hub Request Update + compiled context?

---

### 4. Agent Memory Provisioning

You said: "Memory is provisioned at employment time"

**Question:**
- Does the **EmploymentSpec** (or ScenarioDeployment) specify memory store requirements?
- Or does Hub infer them from the TrainingSpec's declarations?
- Are memory stores **shared across requests** for the same Employed Agent, or **isolated per request**?

---

### 5. Context Assembly Location

**Question:**
- Does **Seer's CAE** compile context before invoking the Raw Agent?
- Or does the **Raw Agent** pull context via Hub Memory Access Tools?
- Or both — CAE pre-compiles, agent augments?

---

### 6. Existing Seer Docs to Update

The `agent-lifecycle-service.md` is comprehensive but Hub-agnostic. 

**Question:** Should the new `hub-integration/` folder:
- **Reference** the existing `agent-lifecycle-service.md` for agent layer details?
- **Duplicate** some content with Hub-specific context?
- Or should we **update** `agent-lifecycle-service.md` to include Hub integration inline?

---

Once you clarify these, I'll proceed with creating the documentation structure.

----


Let me know your answers and I'll proceed with the documentation.


## Seer Agent as a Hub Application

A Seer Agent Can be deployed as a Hub Application.
Seer Trained Agents can be enrolled Hub Applications in a Workbench Specification.
When the Workbench is deployed and the Scenario is wired to an Environment and the IO Gateways, the Agent is an Employed Agent. The Scenario Deployment spec includes the Hub Application Deployment Spec. Because this Hub Application is a Seer Agent Applicaition, the deployment spec refer to the Agent Employment Spec.  The agent employment references the actual resources - maps the tools, memory, knowlwedge stores, etc specification referenced in the training spec to the actual instances.

## Seer Agent as an Agent in Task Queue
> This leverages the Scenario as an Agent Composite Pattern
> That is, 
1. To make a 'Seer Application' (A1) as an agent in the Task Queue of another scenario, the developer will create a Scenario and make A1 the automation of that Scenario
2. This Scenario is registered as an Agent using the composite pattern
3. This Agent now can be employed in a Task Queue in the Workbench
4. A1 just works like any other Seer Agent Application. 

    The application itself doesn't host 'Hub Agents'; 
    A Seer application have 'internal agents' that are not 'hub visible'
    A Seer Agent receives Task Assignment Webhook Call; This call is delivered to the Seer Hub Application representing the Seer Agent; 
    The Seer Hub Application then delegates the task to the Seer Agent Engine to complete the task.




=====

Not to be confused with:
# Seer Orchestration Application