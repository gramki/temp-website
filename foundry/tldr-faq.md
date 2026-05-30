# Foundry tldr — FAQ

> Companion to [tldr.md](tldr.md). Captures the questions, clarifications, and decisions that shaped the tldr but didn't fit on one page. Read [tldr.md](tldr.md) first.

---

## On the model — Tracks, Workspaces, Scenarios

### What's the difference between a Track and a Workspace?

- **Track** = a value stream in the SDLC. The five Tracks come from UPIM's Work Model: Discovery, Build, Run, Win, Evolve. ACE adds Governance as a sixth.
- **Workspace** = a station where a specific function executes work — Product Specification, UX Design, Development, QA, Release, Governance.

Tracks describe **what work flows**. Workspaces describe **where the work is done**. The same Workspace participates in multiple Tracks; what changes between Tracks is the *kind* of work passing through it.

### Why "multiple assembly lines"?

Each Track is its own value stream — Discovery work and Build work are not the same flow. Foundry models each Track as its own assembly line. The same Workspaces are shared stations across multiple lines; it's the Work Orders, Scenarios, and context that change per Track.

### Are the six Workspaces fixed?

For now, yes. The set is defined in [ace/workspaces/README.md](ace/workspaces/README.md): Product Specification, UX Design, Development, QA, Release, Governance.

### What's a Scenario, formally?

A defined kind of work that a Workspace knows how to execute — the **ingress contract** that defines what work a Workspace accepts. Each Workspace owns a catalogue of Scenarios. A Scenario is automated by an agent with skills and decomposes into Tasks. Scenarios have a **scope**: `workspace-ingress` (external contract, invoked by Orchestrator) or `workspace-internal` (invoked only by Tasks within the Workspace).

---

## On Orchestration Items, Work Orders, and Context

### What is an orchestration item vs a Workspace Work Order?

An **orchestration item** is the Track-level token the Orchestrator routes: Discovery Case, Product Intent, Run Case, Customer Release Intent or Win Case, Evolve Case, Governance Ritual, or Governance Enforcement. A **Workspace Work Order** is a Scenario instance executing in one Workspace, anchored to that item's context graph.

Build Track work centers on Product Intent, but Product Intent is not the only orchestration item in Foundry.

### What is the orchestration-item graph?

For Build Track, the graph is rooted at **Product Intent** — the hybrid bridge entity describing what the product is meant to become or what evidence Build must produce. Other Tracks root their graphs at their primary orchestration item. Cross-track links connect graphs at handoffs.

The exact schema of these graphs (typed edges, cycles, DAG-only?) is a deeper-docs topic.

### What is "Context"?

Reader is expected to know. In short: the structured information a Work Order needs to do its job, drawn from the parent orchestration-item graph and the Workspace's repositories. The formal definition belongs to ACE concepts.

### What is a "Skill"?

Reader is expected to know. In short: a unit of agent capability. A Scenario is automated by an agent with one or more skills. Deeper formalization belongs to ACE concepts and the platform spec.

---

## On Tasks and Agents

### Agent Task vs Human Task — what's the rule?

A Task is the granular unit of work inside a Work Order. A Task assigned to a human, *or waiting on any human*, is a Human Task. Otherwise it's an Agent Task. The distinction is about who is on the hook for the next move, not a different kind of entity.

### How long does an Agent live?

Agents are **spun up per Scenario**. They are not long-lived identities; each Scenario invocation gets its own agent configured with the skills required for that Scenario.

---

## On the Interface

### Why VS Code? Fork or extension?

VS Code because builders already use it and it has a strong extensibility model. The exact incarnation (fork vs extension vs hosted instance) is a platform-spec topic — not yet decided.

### How does the Foundry Workspace relate to a VS Code "workspace"?

At runtime, when a builder logs in, the VS Code Workspace they see *is* the Foundry Workspace for that user. The 1:1 per-user mapping collapses the two concepts. A runtime "Workspace Session" name was considered to disambiguate the layers but was dropped from the tldr — at this level, the overload is theoretical, not real. Deeper specs may revisit the naming.

### Codespaces analogy — is it 1:1?

Spiritually yes — log in, get a pre-configured environment with the context you need. Lifecycle, cost model, and isolation specifics are not yet decided.

### Why "Builder" instead of "Engineer"?

"Builder" is the term for Foundry IDE users — the humans who work inside Workspaces. "Engineer" remains valid in broader contexts (e.g., "engineers at Zeta"), but when referring to someone using the Foundry IDE, "builder" is preferred.

---

## On Phase 1

### Why these four Tracks?

Discovery, Build, Release, Governance is a focused subset that exercises the platform end-to-end:

- Discovery opens Discovery Cases and turns evidence into PDRs/Product Intent or other routing outcomes
- Build executes Product Intent, which may be delivery-oriented or discovery-supporting
- Release publishes those artifacts
- Governance validates every transition

Run, Win, and Evolve are out of Phase 1 scope.

### Why is "Release" not the Run Track?

In both UPIM and ACE, **Release is a Build-Track activity** — specifically, publishing verified artifacts. Deployment (applying those artifacts to environments) is Run-Track work and explicitly out of Phase 1 scope.

### Why is Governance a Track if UPIM defines only five?

ACE extends UPIM's track set by introducing Governance as a first-class Track — capturing transition validation, evidence capture, policy application, and audit-trail production as a flow with its own work entities. The Governance **Track** is logically distinct from the Governance **Workspace** (the station that executes Governance work). This formalization is captured as a TODO in [ace/governance.md](ace/governance.md).

### Which Scenarios per Workspace are in Phase 1?

Not yet decided. All Workspaces are in scope; only a subset of each Workspace's Scenarios will ship in Phase 1.

---

## On UPIM, ACE, and Foundry

### Are UPIM and ACE frozen specs?

No. UPIM and ACE are **co-evolving with Foundry**. Building Foundry will teach us what UPIM and ACE need to be; engineers building Foundry are expected to feed corrections and refinements back into the model docs.

### How does Foundry "implement" ACE?

ACE specifies the execution model — Workspaces, Scenarios, Work Orders, Agents, Tasks, Repositories, transitions, governance. Foundry is the running platform that realizes those abstractions: the runtime, the IDE-based interface, the data substrate, the agent layer. The concrete mapping between ACE specifications and Foundry code is deeper-doc territory.

### What does UPIM mean by "specific model of products"?

UPIM today is shaped for the products Zeta builds — banking software with the operating realities those products imply. UPIM can be specialized further for specific product types; Foundry is generic with respect to UPIM, and any UPIM-shaped Product can run on it.

---

## On Platform Modules

### What are the Foundry Platform modules?

| Module | Scope |
|--------|-------|
| **Foundry Management** | Admin plane — Workbenches for Products, repositories (as services), teams, agents, knowledge, tenancy |
| **Foundry IDE** | Builder-facing interface — workspace-specific views |
| **Work Order Runtime** | Execution engine — context compilation, agent lifecycle (for WO execution), agent delegation, human-task surfacing |
| **Foundry Orchestrator** | Coordination — route orchestration items across workspaces, create Workspace Work Orders, invoke Governance Scenarios, enforce gates |
| **Scenario Authoring (per Track, Workspace)** | Scenario discovery & definition; Skills, Knowledge, and Tools; agent recommendations |
| **Release Tools** | CI/CD pipelines with embedded agents, CD integrations, distribution stores, tool integrations |
| **Platform Ops** | Plumbing — observability dashboards, standard tooling, infrastructure |

### Where does agent lifecycle live?

**Agent lifecycle is context-dependent.** Work Order Runtime owns agent lifecycle for Work Order execution. Release Tools (CI) owns agent lifecycle for pipeline-embedded agents. There is no horizontal "agent layer" module.

### Where does Governance live?

**Governance is distributed across the model:**
- **Definition** → Scenarios (Scenario Authoring defines Governance Scenarios)
- **Enforcement** → Orchestrator invokes Governance Scenarios at gates
- **Evidence/Audit** → Governance Scenarios write to repositories

### What are "repositories as services"?

Each repository is a service, not just a store. It provides interfaces to inject and access contents, and manages its own organization, layout, and knowledge management. Foundry Management exposes the access layer; content evolves via Work Order execution (or independently for Domain, Practices repositories).

### How does Workbench repository architecture work?

**Git-based repositories:**
- **Intent, Design, Code** are stored in GitHub (associated GitHub Org)
- All repos created through Workbench interfaces (ensures tagging)
- Tags: FoundryID, Workshop, Workbench, Product Code

**Workbench Metadata Service:**
- Single service per Workbench
- Provides PI IDs before creating Intent
- Tracks all commits to Intent/Design/Code repos
- Manages code repo references

**Ontology Service:**
- Auto-provisioned on Workbench creation
- Independent of Metadata Service (in Management module)

**Quality Repository (hybrid):**
- **TestRail** — source of truth for test case definitions
- **Git** — automation code linked to TestRail test cases
- **Quality Service** — unified access wrapper over both

**Jira-based repositories:**
- **Operations** — Jira Service Management (JSM) for problems/incidents
- **Feedback** — Jira issues (FIRs, bugs, relevant JSM problems)
- **Work** — Jira issues (Work Model entities)
- Jira projects not exclusive to Workbench; configured via **simple label filter**
- Linked manually at Workbench setup

**Evolution Repository:**
- Deferred (not Phase 1)

**GitHub integration:**
- Workbench installs as GitHub App on org
- Workbench = org manager; team members = repo-level access only
- Multiple Workbenches can share one GitHub Org

### What external tools does Foundry integrate with?

**Phase 1 integrations:**
- **GitHub** — GitHub App (org management, commit tracking)
- **Figma** — OAuth (design assets)
- **TestRail** — OAuth (Quality repo SoT for test cases)
- **Jira** — OAuth (Operations/JSM, Feedback, Work repositories)
- **Olympus Weave** — OAuth (Publisher; deploy, track versions, EoS)
- **Others** — URL reference only

Workbench ID is used as OAuth client ID for all integrations.

### What is Olympus Weave integration?

Olympus Weave is the deployment platform. Workbench acts as **Publisher**:
- **Product Code** — assigned by Weave when Workbench created
- **Olympus Product Module code** — assigned by Weave per System (when registered in Ontology)
- **Deployment tracking** — Weave → Foundry webhook + Foundry polls Weave
- **Multi-region** — tracks which version deployed where
- **EoS/Deprecation** — Weave owns metadata; Foundry surfaces it

### Where do integrations live?

Integrations are owned by the module that needs them. Release Tools owns CI/CD/distribution integrations. There is no horizontal "Integrations" module.

### Where does multi-tenancy live?

Foundry Management handles tenancy — tenant provisioning, isolation, configuration.

### Where does observability live?

Foundry relies on standard observability tools. Platform Ops owns the plumbing and dashboards.

---

## On the audience

### Who uses Foundry day-to-day?

Builders at Zeta, and builders at the customer banks Zeta delivers software to. Foundry is **multi-tenant by design** from Phase 1. (See tldr.)

### Where does it run?

Internal audience knows the deployment model; deliberately not stated in the tldr.

### What's the tech stack?

Internal audience knows the stack; deliberately not stated in the tldr. New joiners pick this up during onboarding.

### Who is "we"?

Internal Zeta recruitment piece. "We" = the team building Foundry at Zeta; understood from context.

---

## Decisions and framing notes

Choices made during the tldr's iteration, recorded so the rationale doesn't get lost.

- **"First-class workers"** was chosen over "AI assistants" or "co-pilots". Agents in Foundry *do* the work, not suggest it.
- **"Builder"** was chosen over "Engineer" for Foundry IDE users. "Engineer" remains valid in broader contexts.
- **"Assembly line"** was kept as a metaphor, with the clarification that there's *one assembly line per Track*, not one for the whole platform.
- **"Repository"** is overloaded for a software-engineer audience (UPIM repo vs git repo). Left as-is in the tldr; readers will absorb the UPIM meaning from context. Clarified as "repositories as services" in the module list.
- **"Workspace Session"** was considered as a runtime-layer term to disambiguate ACE Workspace from VS Code Workspace, but dropped from the tldr because the per-user 1:1 mapping makes the disambiguation unnecessary at this level.
- **The Tracks list and Phase 1 Tracks list** were reconciled — the tldr now states the full UPIM five-Track set and notes Governance as an ACE extension, so the Phase 1 four-Track commitment doesn't contradict it.
- **CTA** is intentionally soft ("we should talk"). A concrete contact path will be added once the recruitment process firms up.
- **"Skill" and "Context"** are deliberately undefined in the tldr. The internal audience knows them well enough; defining them inline would bloat the one-pager.
- **Agent lifecycle is context-dependent** — Work Order Runtime owns it for WO execution; Release Tools (CI) owns it for pipeline-embedded agents. No horizontal "agent layer."
- **Governance is distributed** — definition via Scenarios, enforcement via Orchestrator, evidence via repositories. No standalone "Governance module."
- **Integrations are owned by modules** — no horizontal "Integrations" module. Release Tools owns CI/CD integrations.
- **Scenario Authoring is scoped to (Track, Workspace) pairs** — not a global authoring layer.

---

## On platform structure

### How does configuration flow?

**Configuration flows through Metadata Service.** Consumers query Foundry Management, not git directly. Management exposes resolved configuration to runtime modules.

### What gates Foundry-scope configuration?

**Validation gates Foundry configuration.** The Validation module validates all Foundry-scope repos before merge. Release Tools CI handles product-repo build/test only — no cross-module dependency between Validation and Release Tools.

### Are Workspaces lifecycle stages?

No. **Workspaces are functional teams, not lifecycle stages.** The same six stations (Product Specification, UX Design, Development, QA, Release, Governance) serve every Track. OI workflow stages route Work Orders to stations; a single stage may fan out to multiple stations in parallel, and a station may be engaged across multiple stages. See [ace/workspaces/README.md](ace/workspaces/README.md).

### How are Workspace Sessions hosted?

**Sessions are Kubernetes pods.** Workspace Session Infrastructure spawns pods on a Foundry-admin-provided K8s cluster; URLs are generated via Coder's wildcard proxy.

### Who owns session lifecycle?

**Session lifecycle is a control-plane concern.** Workspace Session Management owns lifecycle state; WO Runtime is the in-session worker that acknowledges state transitions.

### Does the platform provision clusters?

No. **Foundry admin provides cluster endpoints.** The platform does not provision Kubernetes clusters — it consumes them via Foundry settings.

---

## Deferred / open questions

The tldr does not commit to these. Each will be addressed in deeper docs — ACE concepts, the platform spec, or onboarding material.

- **Work Order graph schema** — DAG or cyclic? typed edges? how is context resolution implemented?
- **Scenario decomposition** — deterministic (declared upfront) or dynamic (agent-decided)? how are skills mapped to Scenarios?
- **Agent runtime topology** — process model, isolation, observability, where agents physically run (within Work Order Runtime and Release Tools contexts).
- **Per-user vs shared agent infrastructure** — multiple users invoking the same Scenario: shared agent pool or independent spin-up?
- **Identity & access model** — Workspace permissions, agent permissions, repository ACLs, multi-tenant isolation specifics.
- **Phase 1 Scenario subset** per Workspace.
- **ACE-level reconciliation** — Governance Track and Governance Workspace dual framing. TODO in [ace/governance.md](ace/governance.md).
- **"Release" formalization** — should it also be introduced as a separate ACE-level Track, or remain framed as the publishing slice of Build? Open.
- **CTA mechanic** for the tldr's closing.
- **Foundry IDE specifics** — VS Code fork vs extension vs hosted, workspace-specific view customization.
- **Orchestrator implementation** — how Product Intent movement is triggered, Work Order creation API, gate enforcement mechanics.
- **Evolution repository** — storage model deferred (not Phase 1).
- **Scenario Catalog storage** — how are Scenario Catalogs stored, versioned, and distributed to Workbenches?
- **Workbench archival/deletion** — workflow for deprecating a Workbench and its repositories.
- **Cross-Workbench repository sharing** — how do Workbenches share code/design repos within a Workshop?
- **Jira label naming convention** — standard label format for Workbench filtering.

**Resolved (documented elsewhere):**
- ~~Foundry Management specifics~~ — Workbench architecture now documented in [foundry-platform/management/user-guide/workbench-architecture.md](foundry-platform/management/user-guide/workbench-architecture.md).
- ~~Repository storage model~~ — Quality (TestRail + Git), Operations/Feedback/Work (Jira/JSM) now documented. Evolution deferred.
