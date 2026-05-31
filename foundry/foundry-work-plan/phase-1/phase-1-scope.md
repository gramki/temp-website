# Phase 1 Scope

Explicit inclusions, exclusions, assumptions, and success criteria for the first shippable slice of the Foundry Platform.

## Build question

Phase 1 must demonstrate:

> Can Foundry take a product-relevant discovery question, form Product Intent, refine it into buildable work, execute Workspace Work Orders, govern transitions, and publish Product Delivery with traceability?

## Tracks in scope

| Track | Phase 1 status |
|-------|----------------|
| **Discovery** | Full orchestration for Discovery Case → PDR → Build handoff |
| **Build** | Full orchestration for Product Intent → specification → UX → development → QA → release |
| **Governance** | Transition gates on Discovery and Build OI workflows (not the full Governance Ritual catalog) |
| **Release** | In scope as a **Build-track activity** (Release station / workspace), not as a separate track |
| **Run** | Out of scope — deployment and operational response deferred |
| **Win** | Out of scope — customer outcomes and Win orchestration deferred |
| **Evolve** | Out of scope — practice and model evolution deferred |

See [../../tldr.md](../../tldr.md) and [../../tldr-faq.md](../../tldr-faq.md) for track framing.

## Orchestration items

| OI | Phase 1 status |
|----|----------------|
| **Discovery Case** | Fully supported — platform default workflow in [../../foundry-platform/work-catalogues/platform-defaults/work-catalog/discovery/discovery-case/](../../foundry-platform/work-catalogues/platform-defaults/work-catalog/discovery/discovery-case/) |
| **Product Intent** | Fully supported — platform default workflow in [../../foundry-platform/work-catalogues/platform-defaults/work-catalog/build/product-intent/](../../foundry-platform/work-catalogues/platform-defaults/work-catalog/build/product-intent/) |
| **Governance Ritual** | Deferred — cadence-based rituals (sprint review, SLA review, etc.) not in Phase 1 |
| **Governance Enforcement** | Partial — transition governance scenarios invoked by Orchestrator at Build/Discovery gates only |
| **Customer Release Intent** | Read-only context — may be manually seeded; no Win-track orchestration |
| **Run Case, Evolve Case, Win Case** | Named for compatibility only — no workflows |

## Workspaces

All six canonical [workspace stations](../../ace/workspaces/README.md) participate in Phase 1, but not every station runs scenarios on every track:

| Station | Discovery | Build |
|---------|-----------|-------|
| Product Specification | Frame, synthesize, record PDR | Create specification |
| UX Design | User research, experiments, prototypes | Design user experience |
| Development | Feasibility, spikes | Implement |
| QA | Testability, evidence validation | Test suite prep, test execution |
| Release | Rollout feasibility | Accept, prepare customer release |
| Governance | PDR alignment, closure review | Spec, UX, test plan, coverage, release package review |

## Platform modules

| Module | Phase 1 expectation |
|--------|---------------------|
| **Foundry Management** | Workbench provisioning, repository metadata, Work Catalog resolution, Validation gate on config repos |
| **Foundry Orchestrator** | OI workflow engine, WO creation, governance invocation, cross-track handoff (Discovery → Build) |
| **Work Order Runtime** | In-session execution, task graph, agent employment, Personal Work, management-plane interface |
| **Workspace Session Infrastructure** | K8s pod provisioning, Coder URLs, extension packaging |
| **Workspace Session Management** | Session lifecycle control plane |
| **Foundry IDE** | Builder entry — work orders, tasks, agent panel, scenario authoring (user catalog) |
| **Agent Fabric** | Skill registry, capable agent routing, quota (minimal) |
| **Foundry Web App** | PI Console, Workspaces Console, basic governance views |
| **Release Tools** | Foundry CI for product repos (build/test); not full CD pipeline |
| **Platform Admin Web App** | Foundry-level admin only — minimal |
| **Platform Ops** | Deferred |

## Product Intent purposes (Phase 1)

Only **Delivery** purpose Product Intents on the golden path. Other purposes are defined in ACE but deferred:

| Purpose | Phase 1 |
|---------|---------|
| Delivery | In scope (golden path) |
| Discovery Support | Deferred — no Discovery Support PI before PDR |
| Technical Validation | Deferred |
| Internal / Enabling | Deferred |
| Operational Enablement | Deferred |
| Release Renewal | Deferred |

## Discovery origins (Phase 1)

Golden path assumes a **Product Manager–initiated Discovery Case** with a manually entered question. PMs MAY attach optional typed `sourceRefs[]` (e.g. `manual`, `fir`, `signal`) when creating the case; automated signal clustering remains deferred:

- Signal clustering → Objectives / Initiatives
- Customer Requirement → Product Intent (direct)
- Customer Release Intent → Discovery Case
- Agent/monitor-originated cases

## Integrations

| Integration | Phase 1 |
|-------------|---------|
| **GitHub** (Intent, Design, Code repos) | Required — clone, branch, PR on WO completion |
| **Jira** (Work repository) | Partial — WO sync; manual seed acceptable for demo |
| **Metadata Service** | Required — IDs, config resolution |
| **TestRail, Figma, Olympus Weave** | Deferred or mocked |
| **Confluence** | Doc sync only; not runtime dependency |

## Explicitly out of scope

- Run-track deployment and operational response
- Win-track outcomes, Customer Release Intent orchestration
- Evolve-track practice evolution
- Full Governance Ritual catalog (cadence rituals, registers, debt/catch-up lifecycle)
- Signal → Objective → Initiative automation
- Multi-Foundry / multi-tenant production hardening
- Full traceability maps (Executive Strategy Map, etc.) — basic parent/child links only
- Scenario YAML as authoritative contracts (platform defaults are indicative; see [../../foundry-platform/work-catalogues/platform-defaults/README.md](../../foundry-platform/work-catalogues/platform-defaults/README.md))
- Platform Ops observability dashboards (basic audit logs only)

## Assumptions

- One Workshop, one Workbench, one Product for the golden-path demo
- Foundry admin has provisioned a K8s cluster endpoint
- Platform default Work Catalog is used without Foundry/Workshop overrides
- Builders authenticate via existing identity provider
- English-only UI

## Success criteria

Phase 1 is complete when a builder can run the [golden path](golden-path.md) end-to-end on a provisioned Workbench:

1. Create a Discovery Case with a product question
2. Execute research WOs across stations (at least UX + Development + Product Specification)
3. Record a PDR and decide `proceed-to-build`
4. Receive a Product Intent created from the Discovery Case
5. Approve the PI draft, trigger specification work
6. Complete specification → UX → development → QA → release WOs
7. Pass governance gates at each transition
8. Publish a customer release package with traceable links back to Discovery Case and Product Intent

## Real vs mocked

| Capability | Phase 1 |
|------------|---------|
| OI workflow execution (Orchestrator) | Real |
| WO creation and assignment | Real |
| Workspace Session provisioning | Real |
| WO Runtime task execution (agent + human tasks) | Real — agent may use stub skills |
| Work Catalog resolution | Real |
| Git operations per WO | Real |
| Governance scenario invocation + verdict | Real (soft/hard block as defined) |
| Jira bidirectional sync | Mock or partial |
| TestRail / Figma | Mock |
| Full governance admin (CO/COI, registers) | Mock / manual |
| Metrics / KPIs (Say/Do, velocity) | Deferred |

## Read next

- [golden-path.md](golden-path.md) — step-by-step demo path
- [scenario-catalog.md](scenario-catalog.md) — Phase 1 scenarios
- [module-boundaries.md](module-boundaries.md) — ownership
- [governance-mvp.md](governance-mvp.md) — transition gates
- [open-questions.md](open-questions.md) — remaining decisions
