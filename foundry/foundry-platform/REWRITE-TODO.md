# Foundry Platform — Documentation Rewrite Backlog

Substantive content rewrites deferred from the [three-track restructure plan](.cursor/plans/docs_three-track_restructure_891f8129.plan.md). The restructure handles **moves, index files, link fixes, and light normalization** (section headers, doc index tables). Items below need **new prose, splits, deduplication, or spec hardening**.

---

## Cross-cutting

| ID | Item | Observation |
|----|------|-------------|
| X-1 | Module README routers | After restructure, READMEs should be thin routers. Any remaining long conceptual paragraphs duplicated from ACE should be trimmed and replaced with links to `foundry/ace/`. |
| X-2 | ACE/UPIM citation blocks | Platform developer guide docs should open with a standard ACE + UPIM alignment section; many specs jump straight to architecture without citing entities. |
| X-3 | Requirements ID coverage | `management/requirements.md`, subsystem requirements, and several module specs lack consistent FR-/NFR- numbering. Normalization does not add IDs. |
| X-4 | Stale terminology sweep | Post-restructure grep for: "Scenario Management", "CI validation" (Foundry config context), old path patterns, "Workshop Validation Service" without Validation module context. |
| X-5 | `platform.TODO` / `ci.TODO` | Backlog files are not audience-organized; consider splitting into user vs platform-dev work items when those modules are rewritten. |

---

## work-catalogues

| ID | File | Rewrite needed |
|----|------|----------------|
| WC-1 | `user-guide/how-work-flows.md` | Strong conceptual doc; could merge UPIM explanation with ACE `concepts.md` linkage rather than restating Work Model overview. |
| WC-2 | `user-guide/authoring-oi-workflows.md` vs `orchestrator/…` | Duplicate authoring surface with orchestrator `orchestration-item-workflow.md` (~559 lines). Consolidate to single canonical authoring guide; orchestrator should only document consumption. |
| WC-3 | `user-guide/troubleshooting.md` | Expand with Validation-module-specific error codes once FR IDs exist in validation-rules. |
| WC-4 | `platform-defaults/` stubs | Non-Build tracks are README stubs only; need lifecycle diagrams, workspace lists, and workflow.yaml content. |

---

## management

| ID | File | Rewrite needed |
|----|------|----------------|
| M-1 | `user-guide/foundry-onboarding.md` (from journey) | Journey format is narrative; rewrite to user-guide template with explicit Prerequisites, numbered Steps, Expected outcome. |
| M-2 | `user-guide/workbench-provisioning.md` | Same as M-1; add admin persona and decision points (when to create workbench vs workshop). |
| M-3 | `user-guide/foundry-settings.md` | Align with Foundry Web App settings pages; currently doc may drift from UI spec. |
| M-4 | `user-guide/workbench-architecture.md` | Split: admin-facing "what is a workbench" (user) vs logical architecture spec (platform-dev if not already in foundry-management). |
| M-5 | `platform-developer-guide/work-catalog-management/requirements.md` | Architecture diagram still says "Validate PRs" on Validation Service inside WCM; align with Validation module boundary. |
| M-6 | `platform-developer-guide/foundry-management/README.md` | Subsystem README may duplicate management module README; consolidate scope statements. |
| M-7 | `git-infrastructure.md` | Long ops doc; consider splitting user-facing "what repos exist" from operator runbook. |

---

## orchestrator

| ID | File | Rewrite needed |
|----|------|----------------|
| O-1 | `orchestration-item-workflow.md` → user-guide | **High priority dedupe** with `work-catalogues/user-guide/authoring-oi-workflows.md`. Either delete orchestrator copy or reduce to "how Orchestrator consumes resolved workflows" (events, WO creation) without schema tables. |
| O-2 | `pi-journey.md` → user-guide | Good narrative; rewrite for Program Manager persona with journey map and links to Web App orchestration console. |
| O-3 | `platform-developer-guide/requirements.md` | Verify against current Work Catalog resolution paths and Validation module integration. |
| O-4 | Module README | "Scenario Management" phrase in boundaries may still be stale; align with Work Catalog Management terminology. |

---

## work-order-runtime

| ID | File | Rewrite needed |
|----|------|----------------|
| W-1 | `ide-integration.md` | **Split required:** builder-visible IDE experience (user-guide) vs VS Code extension/plugin contract (platform-dev). Currently single architecture doc (~340 lines). |
| W-2 | `end-to-end-work-order-flow.md` | Rewrite for builder audience: less internal daemon detail, more observable states in IDE/Web App. |
| W-3 | `design-discussions/control-plane-and-agent-interfaces.md` | Design discussion — either promote to ADR/requirements or trim to decided outcomes only. |
| W-4 | `design-discussions/agent-harness-comparison.md` | Consolidate harness comparison; extract decision record for Symphony vs custom vs OpenHands. |
| W-5 | `agent-spawning.md` vs `agent-fabric/employed-agents.md` | Overlap on agent lifecycle; clarify WO Runtime vs Agent Fabric boundary in prose. |
| W-6 | `implementation-todos.md` | Convert to tracked issues or phase plan; not durable doc. |

---

## agent-fabric

| ID | File | Rewrite needed |
|----|------|----------------|
| A-1 | `skilled-agents.md` | **Split required:** "what is a Skilled Agent" (user-guide for admins) vs manifest schema/registry (platform-dev). Conceptual opening is good; registry sections belong in platform-dev. |
| A-2 | `agent-lifecycle-journey.md` | Rewrite for Foundry Admin configuring agents; link to Web App agent console. |
| A-3 | `capable-agents.md` | Registry YAML evolves rapidly; ensure interface types match WO Runtime design discussion outcomes. |
| A-4 | `gateway-policy.md` | Needs worked examples (allow/deny paths) for platform implementers. |
| A-5 | Module README | Mixed scope and skilled-agent explanation; after move, README should route only. |

---

## ide

| ID | File | Rewrite needed |
|----|------|----------------|
| I-1 | `README.md` | **Split required** into user-guide (builder sessions, WO panel, Scenario Editor usage) and platform-dev (extension architecture, Publish CLI). Currently single file mixes both. |
| I-2 | Scenario Editor section | Expand user-guide with task steps matching `work-catalogues/user-guide/authoring-scenarios.md`. |
| I-3 | Publish CLI | Document CLI commands in user-guide; implementation/protocol in platform-dev (may not exist yet). |

---

## release-tools

| ID | File | Rewrite needed |
|----|------|----------------|
| R-1 | Module README | Thin; needs user-guide index cross-linking to `foundry-web-app/user-guide/personas/release-teams/`. |
| R-2 | `platform-developer-guide/ci/` | `ci.TODO` is a bullet list; expand into phased CI spec aligned with Release Tools boundaries (no Validation module coupling). |
| R-3 | Agent-embedded CI | Open question in README; needs design doc when WO Runtime vs Release Tools agent lifecycle is finalized. |

---

## foundry-web-app

| ID | File | Rewrite needed |
|----|------|----------------|
| WA-1 | `user-guide/personas/*` | JTBD format is good; add Prerequisites and Related sections consistently; dedupe overlapping jobs across personas. |
| WA-2 | `platform-developer-guide/pages/**` | Page specs vary in depth; normalize wireframe/section template across consoles. |
| WA-3 | `CONSOLE-GUIDE.md` | May need update after Work Catalog console pages mature. |
| WA-4 | Work Catalog settings pages | Ensure parity with `work-catalogues/user-guide/` flows (browse, publish, effective catalog). |

---

## foundry-platform-admin-web-app

| ID | File | Rewrite needed |
|----|------|----------------|
| AD-1 | `user-guide/personas/platform-admin/` | Only one persona; expand jobs or merge into foundry-web-app foundry-admins if overlap exists. |
| AD-2 | `platform-developer-guide/pages/` | Page specs are stubs compared to foundry-web-app; flesh out platform-settings, infrastructure, foundry-detail. |

---

## Priority order (suggested)

1. **O-1 / WC-2** — OI Workflow authoring dedupe (highest duplication)
2. **W-1 / I-1** — IDE + WO Runtime split (mixed audience)
3. **A-1** — Skilled Agents split
4. **M-1 / M-2** — Admin journeys to task format
5. **W-3 / W-4** — WO Runtime design discussions → decisions
6. **WC-4** — Platform default track content

---

## Related

- Restructure plan: `.cursor/plans/docs_three-track_restructure_891f8129.plan.md`
- Style templates (normalization only): `foundry/foundry-platform/_templates/` (created during restructure)
