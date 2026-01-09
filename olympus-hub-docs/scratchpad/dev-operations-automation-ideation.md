# Dev Operations Automation

> **Status:** Ideation → Formalized  
> **Date:** 2026-01-09  
> **Formal Documentation:** 
> - [DevOps Workbench Pattern](../09-composite-systems-and-patterns/devops-workbench/README.md)
> - [DevOps Workbench Reference](../09-composite-systems-and-patterns/devops-workbench/devops-workbench-reference.md)
> - [Implementation Concept](../02-system-design/implementation-concepts/devops-workbench-reference.md)

---

## The Vision

**Use Hub to automate the automation development process itself.**

Instead of APO, PA, and Developer manually performing their activities, their workflows are modeled as Scenarios within a **DevOps Workbench** that:

1. Responds to events from development subsystems
2. Automates routine decisions with human-agent collaboration
3. Accelerates the Intent → Charter → Scenario → Deployment lifecycle

---

## Key Insight

Hub already has the primitives:
- **Scenarios** — can model any operational workflow
- **Signals** — can come from any source (including dev subsystems)
- **Human-AI Collaboration** — agents + human oversight
- **Task Management** — assign work to the right persona

The solution: **A DevOps Workbench (D) that is optionally associated with a Business Workbench (A), receiving development signals and automating development activities.**

---

## Decisions Made

| Question | Decision |
|----------|----------|
| **Workbench Scope** | Separate workbench. A can optionally tag D. Signals from A route to D. |
| **Platform Provision** | Default DevOps WB per subscription + DevOps Workbench Blueprint |
| **Agent Identity** | Assistant Agents reside in D, belong to D's IAM domain |
| **Ownership** | Tenant owns D and all scenarios. A and D can be in different subscriptions |
| **Bootstrapping** | No chicken-egg. D is optional. D doesn't need D' to create it |
| **Customization** | Yes, tenants can fully customize DevOps scenarios |
| **Visibility** | Separate workbench = clean domain separation |
| **Autonomy** | Configurable by personas within D scope |

---

## Refined Conceptual Model

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    DEVOPS WORKBENCH ASSOCIATION MODEL                        │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  SUBSCRIPTION SCOPE                                                         │
│                                                                              │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │                                                                      │   │
│  │  BUSINESS WORKBENCHES                    DEVOPS WORKBENCHES         │   │
│  │                                                                      │   │
│  │  ┌─────────────────┐                    ┌─────────────────┐         │   │
│  │  │ Dispute-Ops     │───── devops_ref ──▶│ Dispute-DevOps  │         │   │
│  │  │ (A1)            │                    │ (D1)            │         │   │
│  │  └─────────────────┘                    │                 │         │   │
│  │                                          │ APO Scenarios  │         │   │
│  │  ┌─────────────────┐                    │ PA Scenarios   │         │   │
│  │  │ Payments-Ops    │───── devops_ref ──▶│ Dev Scenarios  │         │   │
│  │  │ (A2)            │                    │                 │         │   │
│  │  └─────────────────┘                    └─────────────────┘         │   │
│  │                                                                      │   │
│  │  ┌─────────────────┐                    ┌─────────────────┐         │   │
│  │  │ Credit-Risk-Ops │───── devops_ref ──▶│ Risk-DevOps     │         │   │
│  │  │ (A3)            │                    │ (D2)            │         │   │
│  │  └─────────────────┘                    │                 │         │   │
│  │                                          │ Custom scenarios│         │   │
│  │  ┌─────────────────┐                    │ for regulated   │         │   │
│  │  │ HR-Ops          │───── devops_ref ───│ domains         │         │   │
│  │  │ (A4)            │                    │                 │         │   │
│  │  └─────────────────┘                    └─────────────────┘         │   │
│  │                                                                      │   │
│  │                                          ┌─────────────────┐         │   │
│  │  (Workbenches without devops_ref         │ Default-DevOps  │         │   │
│  │   use the default DevOps WB) ───────────▶│ (Platform)      │         │   │
│  │                                          │                 │         │   │
│  │                                          │ Standard        │         │   │
│  │                                          │ scenarios       │         │   │
│  │                                          └─────────────────┘         │   │
│  │                                                                      │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Key Relationships

| Relationship | Description |
|--------------|-------------|
| **A → D** | Business workbench (A) optionally references DevOps workbench (D) |
| **N:1** | Multiple business workbenches can share one DevOps workbench |
| **1:1** | Or each business workbench can have its own DevOps workbench |
| **Default** | Workbenches without explicit `devops_ref` use subscription's default DevOps WB |

---

## Questions to Explore

### Q1: Where Does the Dev Ops Workbench Live?

| Option | Description | Pros | Cons |
|--------|-------------|------|------|
| **A. Separate Workbench** | A dedicated "Dev Ops Workbench" per subscription | Clear separation | Another workbench to manage |
| **B. Workbench Extension** | Extension/module attached to each business workbench | Co-located with context | Pollutes business workbench |
| **C. Platform Workbench** | Publisher-provided platform workbench | Shared, maintained by Zeta | Less customizable |

**Leaning:** Option A — Separate Workbench scoped to subscription or workbench.

---

### Q2: What Are the Personas in Dev Ops Context?

In the Dev Ops Workbench, the same personas (APO, PA, Developer) are both:
- **Designers** of the Dev Ops automation (meta-level)
- **Operators** who benefit from the automation (operational level)

| Persona | As Designer | As Operator |
|---------|-------------|-------------|
| **APO** | Designs APO automation scenarios | Benefits from automated idea triage |
| **PA** | Designs PA automation scenarios | Benefits from automated scenario generation |
| **Developer** | Designs Dev automation scenarios | Benefits from automated testing, deployment |

---

### Q3: What Signals Exist in Development Subsystems?

#### From Automation Ideation

| Event | Description | Potential Automation |
|-------|-------------|---------------------|
| `idea.submitted` | New idea received | Auto-categorize, estimate value |
| `idea.promoted` | Idea promoted to intent | Draft intent template |
| `intent.completed` | Intent ready for PA | Notify PA, schedule review |
| `intent.accepted` | PA accepted, charter created | Generate scenario skeleton |

#### From CI Subsystem

| Event | Description | Potential Automation |
|-------|-------------|---------------------|
| `test.failed` | Test failure | Diagnose, suggest fix, assign to developer |
| `test.passed` | All tests pass | Notify PA, suggest promotion |
| `build.failed` | Build failure | Parse error, suggest resolution |

#### From Artifact Registry

| Event | Description | Potential Automation |
|-------|-------------|---------------------|
| `artifact.published` | New version published | Notify stakeholders, update changelog |
| `promotion.requested` | Promotion requested | Validate, auto-approve if criteria met |
| `promotion.approved` | Promotion approved | Trigger deployment |

#### From Feedback Services

| Event | Description | Potential Automation |
|-------|-------------|---------------------|
| `feedback.promoted` | New feedback from production | Triage, categorize, route |
| `feedback.accepted` | APO accepted feedback | Create task, assign to PA/Dev |

---

### Q4: What Scenarios Would Exist?

#### APO Scenarios

| Scenario | Trigger | Automation |
|----------|---------|------------|
| **Idea Triage** | `idea.submitted` | AI categorizes, estimates value, suggests action |
| **Intent Drafting** | `idea.promoted` | AI drafts intent from idea, APO refines |
| **Feedback Triage** | `feedback.promoted` | AI categorizes, prioritizes, suggests routing |
| **Outcome Review** | `outcome.updated` | AI summarizes performance, flags concerns |

#### PA Scenarios

| Scenario | Trigger | Automation |
|----------|---------|------------|
| **Intent Review** | `intent.completed` | AI summarizes intent, suggests design approach |
| **Scenario Drafting** | `charter.created` | AI generates scenario skeleton from charter |
| **SOP Generation** | `scenario.created` | AI drafts SOP from scenario definition |
| **Normative Validation** | `scenario.updated` | AI validates against governance policies |

#### Developer Scenarios

| Scenario | Trigger | Automation |
|----------|---------|------------|
| **Application Scaffolding** | `scenario.created` | AI generates app skeleton from scenario |
| **Test Failure Diagnosis** | `test.failed` | AI analyzes failure, suggests fix |
| **Build Error Resolution** | `build.failed` | AI parses error, suggests resolution |
| **Deployment Readiness** | `test.passed` | AI validates, suggests promotion |

---

### Q5: How Does This Differ from Business Workbench?

| Aspect | Business Workbench | Dev Ops Workbench |
|--------|-------------------|-------------------|
| **Purpose** | Business operations automation | Development operations automation |
| **Signals** | Business events (disputes, orders) | Dev events (ideas, builds, tests) |
| **Versioning** | Versioned, promoted through stages | Not versioned in business spec |
| **Personas** | Agents, Supervisors process work | APO, PA, Dev are the "agents" |
| **Scope** | One domain (Disputes, Payments) | One subscription or tenant |

---

### Q6: What Is the "Dev Operations Automation Bundle"?

A **Dev Ops Bundle** is a package of:
1. **Dev Ops Scenarios** — Scenarios that automate APO/PA/Dev activities
2. **Dev Ops Applications** — Hub Applications that implement automation
3. **Dev Ops Triggers** — Bindings from dev subsystem events to scenarios
4. **Dev Ops Agents** — AI agents trained for development activities

This bundle is:
- **NOT part of the business workbench spec**
- **Managed separately** from business scenarios
- **Potentially shared** across workbenches in a subscription

---

## Refined Architecture

### Platform Provision

| Asset | Description |
|-------|-------------|
| **Default DevOps Workbench** | Platform-provided DevOps WB per subscription with standard scenarios |
| **DevOps Workbench Blueprint** | Template for creating custom DevOps workbenches |
| **Standard Scenarios** | Platform-provided scenarios for common DevOps activities |
| **Assistant Agent Templates** | AI agent templates for APO, PA, Developer assistance |

### Signal Routing Model

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    SIGNAL ROUTING: A → D                                     │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  BUSINESS WORKBENCH (A)                    DEVOPS WORKBENCH (D)             │
│                                                                              │
│  ┌─────────────────────────────┐          ┌─────────────────────────────┐  │
│  │                             │          │                             │  │
│  │  automation-ideation        │          │  Signal Exchange (D)        │  │
│  │  ├── idea.submitted ───────────────────▶ Trigger: IdeaTriageScenario │  │
│  │  ├── intent.completed ─────────────────▶ Trigger: IntentReviewScenario│ │
│  │  └── charter.created ──────────────────▶ Trigger: ScenarioDraft...   │  │
│  │                             │          │                             │  │
│  │  ci-subsystem               │          │                             │  │
│  │  ├── test.failed ──────────────────────▶ Trigger: TestDiagnosis...   │  │
│  │  ├── test.passed ──────────────────────▶ Trigger: DeploymentReady... │  │
│  │  └── build.failed ─────────────────────▶ Trigger: BuildErrorRes...   │  │
│  │                             │          │                             │  │
│  │  artifact-registry          │          │                             │  │
│  │  ├── promotion.requested ──────────────▶ Trigger: PromotionReview... │  │
│  │  └── artifact.published ───────────────▶ Trigger: ReleaseNotify...   │  │
│  │                             │          │                             │  │
│  │  feedback-services          │          │                             │  │
│  │  ├── feedback.promoted ────────────────▶ Trigger: FeedbackTriage...  │  │
│  │  └── feedback.accepted ────────────────▶ Trigger: FeedbackAction...  │  │
│  │                             │          │                             │  │
│  └─────────────────────────────┘          └─────────────────────────────┘  │
│                                                                              │
│  Signal routing is based on:                                                │
│  • workbench.devops_ref configuration                                       │
│  • Signal provider (Atropos) routes to D's Signal Exchange                  │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

### DevOps Workbench Internal Architecture

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    DEVOPS WORKBENCH (D) INTERNALS                            │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │                         SIGNAL EXCHANGE (D)                          │   │
│  │                                                                      │   │
│  │  Receives signals from linked Business Workbenches (A1, A2, ...)    │   │
│  │  Each signal includes source_workbench_id for context               │   │
│  └──────────────────────────────┬───────────────────────────────────────┘   │
│                                 │                                            │
│                                 ▼                                            │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │                         DEVOPS SCENARIOS                             │   │
│  │                                                                      │   │
│  │  ┌───────────────────────────────────────────────────────────────┐  │   │
│  │  │ APO SCENARIOS                                                  │  │   │
│  │  │ • Idea Triage       — Categorize, estimate, suggest action    │  │   │
│  │  │ • Intent Drafting   — Draft intent from idea, APO refines     │  │   │
│  │  │ • Feedback Triage   — Categorize, prioritize, route           │  │   │
│  │  │ • Outcome Review    — Summarize performance, flag concerns    │  │   │
│  │  └───────────────────────────────────────────────────────────────┘  │   │
│  │                                                                      │   │
│  │  ┌───────────────────────────────────────────────────────────────┐  │   │
│  │  │ PA SCENARIOS                                                   │  │   │
│  │  │ • Intent Review     — Summarize, suggest design approach      │  │   │
│  │  │ • Scenario Draft    — Generate skeleton from charter          │  │   │
│  │  │ • SOP Generation    — Draft SOP from scenario definition      │  │   │
│  │  │ • Normative Valid   — Validate against governance policies    │  │   │
│  │  └───────────────────────────────────────────────────────────────┘  │   │
│  │                                                                      │   │
│  │  ┌───────────────────────────────────────────────────────────────┐  │   │
│  │  │ DEVELOPER SCENARIOS                                            │  │   │
│  │  │ • App Scaffolding   — Generate app skeleton from scenario     │  │   │
│  │  │ • Test Diagnosis    — Analyze failure, suggest fix            │  │   │
│  │  │ • Build Resolution  — Parse error, suggest resolution         │  │   │
│  │  │ • Deploy Readiness  — Validate, suggest promotion             │  │   │
│  │  └───────────────────────────────────────────────────────────────┘  │   │
│  │                                                                      │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                 │                                            │
│                                 ▼                                            │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │                         TASK QUEUES (D)                              │   │
│  │                                                                      │   │
│  │  ┌───────────────┐  ┌───────────────┐  ┌───────────────┐            │   │
│  │  │ APO Queue     │  │ PA Queue      │  │ Dev Queue     │            │   │
│  │  │               │  │               │  │               │            │   │
│  │  │ Enrolled:     │  │ Enrolled:     │  │ Enrolled:     │            │   │
│  │  │ • APO (human) │  │ • PA (human)  │  │ • Dev (human) │            │   │
│  │  │ • APO Agent   │  │ • PA Agent    │  │ • Dev Agent   │            │   │
│  │  │   (AI)        │  │   (AI)        │  │   (AI)        │            │   │
│  │  └───────────────┘  └───────────────┘  └───────────────┘            │   │
│  │                                                                      │   │
│  │  Escalation: AI Agent → Human (configurable per scenario)           │   │
│  │                                                                      │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

---

## Workbench Configuration

### Business Workbench (A) Configuration

```yaml
apiVersion: hub.olympus.io/v1
kind: Workbench
metadata:
  name: dispute-ops-dev
  namespace: acme-bank
spec:
  # ... standard workbench config ...
  
  # DevOps Workbench Association (optional)
  devops:
    # Reference to DevOps workbench
    workbench_ref: dispute-devops    # If null, uses subscription default
    
    # Signal routing configuration
    signal_routing:
      # Which subsystems' events to route to D
      sources:
        - automation-ideation      # Ideas, intents, charters
        - ci-subsystem             # Tests, builds
        - artifact-registry        # Promotions, publications
        - feedback-services        # Feedback from production
      
      # Filter (optional) - route only certain events
      filters:
        - source: ci-subsystem
          events: [test.failed, build.failed]  # Only failures
```

### DevOps Workbench (D) Configuration

```yaml
apiVersion: hub.olympus.io/v1
kind: Workbench
metadata:
  name: dispute-devops
  namespace: acme-bank
spec:
  # Standard workbench config
  domain: devops
  description: "DevOps automation for Dispute workbenches"
  
  # Mark as DevOps workbench
  workbench_type: devops    # "business" (default) | "devops"
  
  # Scenarios defined as usual
  scenarios:
    - name: idea-triage
      # ...
    - name: intent-drafting
      # ...
  
  # Task Queues with AI agents enrolled
  task_queues:
    - name: apo-queue
      enrolled_agents:
        - type: human
          role: automation_product_owner
        - type: ai
          agent_id: apo-assistant-agent
          autonomy_level: medium    # low | medium | high
      escalation:
        from_ai_to_human: true
        timeout: 30m
    
    - name: pa-queue
      enrolled_agents:
        - type: human
          role: process_architect
        - type: ai
          agent_id: pa-assistant-agent
          autonomy_level: medium
    
    - name: dev-queue
      enrolled_agents:
        - type: human
          role: developer
        - type: ai
          agent_id: dev-assistant-agent
          autonomy_level: high      # Developer tasks often automatable
```

### DevOps Workbench Blueprint

```yaml
apiVersion: hub.olympus.io/v1
kind: Blueprint
metadata:
  name: devops-workbench-blueprint
  namespace: olympus-platform    # Platform-provided
spec:
  description: "Standard DevOps Workbench for automation development"
  
  # Pre-configured scenarios
  scenarios:
    # APO Scenarios
    - name: idea-triage
      type: cognitive
      triggers:
        - event: idea.submitted
      tasks:
        - type: decision
          description: "Categorize and estimate idea value"
          queue: apo-queue
    
    - name: intent-drafting
      type: cognitive
      triggers:
        - event: idea.promoted
      tasks:
        - type: action
          description: "Draft intent from idea"
          queue: apo-queue
    
    # PA Scenarios
    - name: scenario-drafting
      type: cognitive
      triggers:
        - event: charter.created
      tasks:
        - type: action
          description: "Generate scenario skeleton"
          queue: pa-queue
    
    # Developer Scenarios
    - name: test-diagnosis
      type: cognitive
      triggers:
        - event: test.failed
      tasks:
        - type: decision
          description: "Diagnose failure and suggest fix"
          queue: dev-queue
  
  # Pre-configured agents
  agents:
    - id: apo-assistant-agent
      name: "APO Assistant"
      capabilities: [idea-triage, intent-drafting, feedback-triage]
    
    - id: pa-assistant-agent
      name: "PA Assistant"
      capabilities: [intent-review, scenario-drafting, sop-generation]
    
    - id: dev-assistant-agent
      name: "Developer Assistant"
      capabilities: [scaffolding, test-diagnosis, build-resolution]
```

---

## Resolved Questions

1. **Workbench Scope** — Is the Dev Ops Workbench per-subscription or per-business-workbench?

> Let's go with 'Dev Ops Workbench' as a separate Workbench. A Workbench instance (A) can have a Dev Ops workbench instance (D) associated with it. The relevant signals from A are routed to D.

> Under a single Hub Subscription there is a 'Default' DevOps Workbench shipped with platform. The Platform also gives 'DevOps Workbench Blueprint'. A Tenant Admin can create as many Dev Ops Workbench instances as they please.

> Tenants can customize Scenarios in any of their DevOps workbenches as they please. This should allow for different treatment for various scenarios in different workbenches. Workbenches meant to automate HR processes and Credit Risk Process may need different level of DevOps proceses.

2. **Agent Identity** — Are APO/PA/Dev Agents the same as business agents, or separate?
> The Assistant Agents of each of these roles can now reside in relevant DevOps Workbenches. They of course then reside in the IAM domains associated with the DevOps Workbench.


3. **Scenario Ownership** — Who owns Dev Ops Scenarios? Platform team? Each tenant?
> Every Workbench is owned by the 'tenant' who subscribed to the Hub. Consequently, all the Scenarios within the workbench are also owned by the same tenant. However, workbench A and D can belong to different subscription of the same real-world tenant, if the tenant so wants to isolate them. However this is not an imposition from Hub platform.

4. **Bootstrapping** — How is the Dev Ops Workbench itself created? (Chicken-egg problem)
> Hub doesn't require existence of Dev Ops Workbench. It is optionally to tag a DevOps Workbench (D) to a Workbench (A). So there is not check-and-egg here. D is optional. D could have been created without existence of another D' that is serving as a DevOps workbench for D. 

5. **Customization** — Can tenants customize Dev Ops Scenarios, or are they platform-provided?
> Yes

6. **Visibility** — Do Dev Ops activities appear in the same desk as business activities?
> The Workbench is different. This gives clean separation from the domains of A and D.

7. **Agentic Boundary** — How autonomous should Dev Ops agents be? Full autonomy or human-in-loop?
> This is tuned by the relevant personas in the D scope.

---

## Implementation Roadmap

### Phase 1: Foundation

| Task | Description | Output |
|------|-------------|--------|
| Define `workbench_type` | Add "devops" workbench type to Workbench CRD | CRD update |
| Define `devops_ref` | Add DevOps workbench reference to Business WB | CRD update |
| Signal Routing | Route signals from A to D based on configuration | Signal Exchange update |
| Default DevOps WB | Create subscription default DevOps workbench | Platform feature |
| Blueprint | Create DevOps Workbench Blueprint | Blueprint CRD |

### Phase 2: Core Scenarios

| Scenario | Persona | Trigger | Priority |
|----------|---------|---------|----------|
| **Idea Triage** | APO | `idea.submitted` | High |
| **Test Diagnosis** | Developer | `test.failed` | High |
| **Intent Review** | PA | `intent.completed` | Medium |
| **Feedback Triage** | APO | `feedback.promoted` | Medium |
| **Scenario Drafting** | PA | `charter.created` | Medium |
| **App Scaffolding** | Developer | `scenario.created` | Low |

### Phase 3: AI Agents

| Agent | Capabilities | Autonomy |
|-------|--------------|----------|
| APO Assistant | Idea triage, intent drafting, feedback triage | Medium |
| PA Assistant | Intent review, scenario drafting, SOP generation | Medium |
| Dev Assistant | Test diagnosis, build resolution, scaffolding | High |

---

## Key Design Decisions

| Decision | Choice | Rationale |
|----------|--------|-----------|
| **Workbench Type** | Explicit `devops` type | Clear distinction from business workbenches |
| **Signal Routing** | Configuration-based | Flexible, tenant-controlled |
| **Platform Default** | Provided per subscription | Baseline for tenants, can be customized |
| **Blueprint** | Platform-provided | Template for custom DevOps workbenches |
| **Agent Enrollment** | AI + Human in same queue | Seamless escalation |
| **Autonomy Control** | Per-scenario and per-agent | Fine-grained tuning |

---

## End-to-End Example Flow

### Example: Idea to Scenario

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    IDEA TO SCENARIO (AGENTIC FLOW)                           │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  1. IDEA SUBMITTED                                                          │
│     Agent in dispute-ops-prod submits idea                                  │
│     Signal: idea.submitted (source: dispute-ops-dev)                        │
│                                                                              │
│     ┌────────────────────────────────────────────────────────────────────┐ │
│     │ Signal routed to dispute-devops (D)                                │ │
│     │ Trigger: IdeaTriageScenario                                        │ │
│     │ Task created → APO Queue                                           │ │
│     └────────────────────────────────────────────────────────────────────┘ │
│                                                                              │
│  2. IDEA TRIAGE (APO Agent)                                                 │
│     APO Assistant Agent picks task                                          │
│     AI analyzes idea, categorizes, estimates value                         │
│     AI recommends: "Promote to Intent - High Value"                        │
│                                                                              │
│     ┌────────────────────────────────────────────────────────────────────┐ │
│     │ If autonomy = high: Auto-promote                                   │ │
│     │ If autonomy = medium: APO (human) approves                         │ │
│     └────────────────────────────────────────────────────────────────────┘ │
│                                                                              │
│  3. INTENT DRAFTED (APO Agent)                                              │
│     Signal: idea.promoted                                                   │
│     Trigger: IntentDraftingScenario                                        │
│     APO Agent drafts intent from idea                                       │
│     APO (human) reviews and refines                                         │
│     APO marks intent complete                                               │
│                                                                              │
│  4. INTENT REVIEWED (PA Agent)                                              │
│     Signal: intent.completed                                                │
│     Trigger: IntentReviewScenario                                          │
│     PA Agent summarizes intent, suggests design approach                   │
│     PA (human) accepts intent → Charter created                            │
│                                                                              │
│  5. SCENARIO DRAFTED (PA Agent)                                             │
│     Signal: charter.created                                                 │
│     Trigger: ScenarioDraftingScenario                                      │
│     PA Agent generates scenario skeleton from charter                      │
│     PA (human) refines scenario                                             │
│                                                                              │
│  6. APP SCAFFOLDED (Dev Agent)                                              │
│     Signal: scenario.created                                                │
│     Trigger: AppScaffoldingScenario                                        │
│     Dev Agent generates Hub Application skeleton                           │
│     Developer (human) implements business logic                            │
│                                                                              │
│  OUTCOME: Idea → Intent → Charter → Scenario → App                         │
│           Mostly automated, human-in-loop at key decisions                 │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## Open Items for Next Iteration

1. **Signal Schema** — Define event schemas for all dev subsystems
2. **AI Agent Specs** — Define capabilities, prompts, tools for each agent
3. **Autonomy Model** — Formalize low/medium/high autonomy behaviors
4. **Cross-Subscription** — Can A and D be in different subscriptions?
5. **Metrics & Observability** — How to measure DevOps automation effectiveness
6. **Security Model** — IAM boundaries between A and D

---

## Next Steps

1. ✅ **Define Model** — DevOps Workbench association model (this document)
2. ✅ **Implementation Concept** — Created `devops-workbench-reference.md`
3. ✅ **Composite Pattern** — Created `devops-workbench/` pattern folder
4. ✅ **Workbench Spec Update** — Added `devops` block to workbench anatomy
5. ✅ **Bidirectional Binding** — Created `devops-workbench-binding.md` with CRDs and operators
6. ✅ **Signal Catalog** — Created `signal-routing-via-atropos.md` with event catalog
7. ✅ **DevOps Scenarios** — Created `devops-scenarios.md` with all APO, PA, Dev scenarios
8. ✅ **ADRs** — Created ADR-0088, ADR-0089, ADR-0090 for DevOps Workbench decisions
9. ✅ **Operators** — Added devops-binding-operator, manifest-operator, crd-approval-operator to admin-operators.md and crd-reference.md
10. ✅ **CRD Publishing** — Added D → A Git-based write capabilities for specs and instances (PR-based approval)
11. ✅ **AI Agent Specifications** — Created `ai-agent-specifications.md` with RawAgentSpec + 3 TrainingSpecs (APO, PA, Dev assistants)
12. 🔲 **DevOps Blueprint** — Template for custom DevOps workbenches
13. ✅ **Idea-to-Deployment Guide** — Created `10-guides/idea-to-deployment-guide.md`


Planned Documents (Next Steps)
Document	Description	Priority

signal-routing-via-atropos.md	Detailed Atropos configuration for cross-workbench signals	High
devops-scenarios.md	Standard scenarios for APO, PA, Developer	High
ai-assistant-agents.md	AI agent specs per persona	Medium
devops-blueprint.md	Template for custom DevOps workbenches	Medium
ADR for DevOps Workbench	Decision record	Medium

Would you like me to continue with any of these next documents, or would you prefer to detail the composite system further in a specific direction?