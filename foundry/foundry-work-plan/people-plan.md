# People Plan — Phase 1

Team structure for building Phase 1 of the Foundry Platform. Headcount and names are templates — fill when staffing is committed.

## Organizing principle

> **Platform squads build the engine; track experts write the catalog; Release Engineering builds and owns CI pipelines.**

- **Delivery** is organized around [milestones](milestones.md) (M0–M5), not module-complete releases.
- **Ownership** is organized around five streams plus a thin program layer.
- **Workspace stations** (Product Specification, Development, etc.) are catalog/scenario concerns — not org units.

## Program layer

Cross-squad roles. Not a fifth engineering squad.

| Role | Responsibility |
|------|----------------|
| **Program lead** | Scope, milestone sequencing, dependency arbitration, demo readiness, stakeholder reporting |
| **Platform architect** | Module boundaries, contract-gate approval, ACE/UPIM alignment enforcement |
| **Integration lead** | Golden-path E2E, tracer bullets, cross-stream definition of done at each milestone |

### Program roster

| Role | Name | Notes |
|------|------|-------|
| Program lead | TBD | |
| Platform architect | TBD | |
| Integration lead | TBD | May be tech lead from Control Plane or Execution Plane |

## Five delivery streams

| Stream | Charter | Primary modules |
|--------|---------|-----------------|
| **Control Plane** | [squad-charters/control-plane.md](squad-charters/control-plane.md) | Management, Orchestrator, WCM engine |
| **Execution Plane** | [squad-charters/execution-plane.md](squad-charters/execution-plane.md) | WSI, WSSM, WO Runtime, Agent Fabric (minimal) |
| **Builder Experience** | [squad-charters/builder-experience.md](squad-charters/builder-experience.md) | IDE, Foundry Web App |
| **Release Engineering** | [squad-charters/release-engineering.md](squad-charters/release-engineering.md) | Release Tools, Foundry CI |
| **Work Catalog Authoring** | [squad-charters/work-catalog-authoring.md](squad-charters/work-catalog-authoring.md) | Work Catalog **content** (workflows, scenarios) |

### Stream summaries

**Control Plane** — Workbench provisioning, entity APIs, Work Catalog resolution engine, Orchestrator workflow execution. Without this stream, nothing coordinates.

**Execution Plane** — Sessions (K8s/Coder), WO Runtime, minimal Agent Fabric. Where builders run work.

**Builder Experience** — IDE and Web App surfaces. Consumes Control Plane and Execution Plane APIs.

**Release Engineering** — Builds and owns Foundry CI and product-repo pipelines; release artifacts. Separate from catalog authoring; pipelines run when Development/Release WOs complete.

**Work Catalog Authoring** — Track experts who write authoritative OI workflows and scenarios. Requires SDLC domain knowledge per track (Discovery, Build, Governance transitions). Does not implement WCM engine or Orchestrator.

## Illustrative sizing (guidance only)

Not committed headcount. Adjust to actual staffing.

| Stream | Typical size | Start priority |
|--------|--------------|----------------|
| Control Plane | 4–6 | First — critical path |
| Execution Plane | 4–5 | First — critical path |
| Builder Experience | 3–4 | M1 (can mock APIs earlier) |
| Release Engineering | 1–2 | M2+ |
| Work Catalog Authoring | 3 track owners + 1 steward (part-time OK) | M0 steward; track owners ramp per milestone |
| Program layer | 1–2 | From day one |

## Skills profile

| Stream | Primary skills |
|--------|----------------|
| Control Plane | Backend services, workflow/state machines, Postgres, API design, multi-tenant config |
| Execution Plane | Kubernetes, container runtime, session lifecycle, task orchestration, Git automation |
| Builder Experience | VS Code extension, React/web app, UX for builders and PMs |
| Release Engineering | CI/CD, GitHub Actions, artifact packaging, pipeline agents |
| Work Catalog Authoring | ACE/UPIM Work Model, SDLC practice, scenario design, YAML workflow authoring |
| Integration lead | E2E testing, demo scripting, cross-module debugging |

## Squad lead roster

| Stream | Squad lead | Tech lead |
|--------|------------|-----------|
| Control Plane | TBD | TBD |
| Execution Plane | TBD | TBD |
| Builder Experience | TBD | TBD |
| Release Engineering | TBD | TBD |

## Work Catalog track owner roster

Part-time or dotted-line is acceptable. Accountability is per track, not per module.

| Track | Owner role | Name | Catalog path |
|-------|------------|------|--------------|
| Discovery | Discovery track owner | TBD | [discovery/discovery-case/](../foundry-platform/work-catalogues/platform-defaults/work-catalog/discovery/discovery-case/) |
| Build | Build track owner | TBD | [build/product-intent/](../foundry-platform/work-catalogues/platform-defaults/work-catalog/build/product-intent/) |
| Governance (transitions) | Governance track owner | TBD | Governance scenarios under Discovery + Build OI folders |
| Cross-track | Catalog steward | TBD | Schema compliance, naming, handoffs, publish via WCM |

## Read next

- [milestones.md](milestones.md) — when each stream delivers
- [integration/dependency-graph.md](integration/dependency-graph.md) — who blocks whom
- [phase-1/phase-1-scope.md](phase-1/phase-1-scope.md) — Phase 1 scope anchor
