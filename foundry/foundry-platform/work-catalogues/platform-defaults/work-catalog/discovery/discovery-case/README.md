# Discovery Case

**Orchestration Item for the Discovery track.**

## Overview

A Discovery Case represents a discovery initiative — exploring unknowns, validating hypotheses, and generating insights that inform product decisions. Discovery Cases help teams understand user needs, market opportunities, and technical feasibility before committing to build. The Discovery Case is the coordination token that synchronizes research across multiple Workspaces and ends in a recorded Product Decision Record (PDR).

## Lifecycle

```
start → discovery-initiated → research-in-progress → insights-synthesized →
recommendations-ready → decision-made → end
```

### Stage Descriptions

> Stages are Discovery Case coordination points that **route Work Orders to functional [stations](../../../../../../ace/workspaces/README.md)** — they are not the stations themselves. `research-in-progress` fans a single stage out to several stations in parallel.

| Stage | Description | Work Orders Created |
|-------|-------------|---------------------|
| `start` | Initial state | — |
| `discovery-initiated` | Case created; framing in progress | Product Specification WO (frame) |
| `research-in-progress` | Parallel research across stations | UX + Development + QA + Release WOs (group) |
| `insights-synthesized` | Research consolidated into evidence | Product Specification + QA WOs (group) |
| `recommendations-ready` | PDR recorded; governance + decision gate | Product Specification WO + user task |
| `decision-made` | Outcome decided; case closing | — |
| `end` | Terminal state | — |

## OI Workflow

→ [workflow.yaml](workflow.yaml) — Complete workflow definition

Key features:
- Parallel research fan-out (`research-in-progress` WO Group across four stations)
- Governance invocations (`pdr-alignment-review`, `discovery-closure-review`)
- Human decision gate (build / park / drop)
- Cross-track handoff: a `proceed-to-build` decision creates a Build-track Product Intent
- Timeout handling and partial-completion paths

## Stations and Scenarios

Discovery reuses the canonical six [workspace stations](../../../../../../ace/workspaces/README.md) — functional teams, not stages. The items below are discovery-flavored ingress scenarios on those same teams; there are no new workspaces.

> **Indicative specs.** The scenario `*.yaml` files are worked examples. Their inputs, outputs, skills, and tasks are placeholders and do not capture the true detail or structure — they will be replaced with real definitions during specification. The `workflow.yaml` orchestration is the reliable part.

| Station | Scenarios | Purpose |
|---------|-----------|---------|
| [product-specification/](product-specification/) | `frame-discovery-case`, `synthesize-evidence`, `record-product-decision` | Frame the case, synthesize evidence, record the PDR |
| [ux-design/](ux-design/) | `conduct-user-research`, `run-usability-experiment`, `build-design-prototype` | User research, experiments, prototypes |
| [development/](development/) | `assess-technical-feasibility`, `run-discovery-spike` | Feasibility and proofs of concept |
| [qa/](qa/) | `assess-testability`, `validate-experiment-evidence` | Testability and evidence rigor |
| [release/](release/) | `assess-rollout-feasibility` | Operational / rollout feasibility |
| [governance/](governance/) | `pdr-alignment-review`, `discovery-closure-review` | Governance gates at recommendation and closure |

Discovery typically uses *some* stations heavily (Product Specification, UX Design, Development) and others lightly (Release). The workflow fans `research-in-progress` out to several stations at once.

## Handoff to the Build Track

When stakeholders close the decision gate with `proceed-to-build`, the workflow creates a **Product Intent** in the [Build track](../../build/product-intent/), seeded from this Discovery Case. The Discovery Case still proceeds to `decision-made` and closes; the new Product Intent runs its own Build lifecycle independently. `park` and `drop` decisions close the case without a handoff.

## Example Flow

1. **DC "Should we offer offline mode?" created** → `start` → `discovery-initiated`
2. **Framing WO completes** → transitions to `research-in-progress`
3. **Parallel research group runs** → UX research, technical feasibility, testability, rollout feasibility
4. **Research group completes** → transitions to `insights-synthesized`
5. **Synthesis group completes** (evidence synthesized + validated) → transitions to `recommendations-ready`
6. **PDR recorded** → `pdr-alignment-review` governance check, decision gate opened
7. **Product Owner chooses `proceed-to-build`** → creates a Build-track Product Intent, transitions to `decision-made`
8. **Closure** → `discovery-closure-review` governance check, transitions to `end`

## Customization

Organizations can override this workflow at Foundry / Workshop / Workbench levels. Common customizations:
- Add/remove research streams in the `research-in-progress` group
- Add scenarios on the existing stations (no new workspaces)
- Adjust governance gates and timeouts
- Change the decision-gate outcomes or handoff target

## Related

- [../../README.md](../../README.md) — Work Catalogs overview
- [../build/product-intent/](../build/product-intent/) — Build track (handoff target)
- [../../user-guide/authoring-oi-workflows.md](../../user-guide/authoring-oi-workflows.md) — How to customize workflows
- [../../user-guide/authoring-scenarios.md](../../user-guide/authoring-scenarios.md) — How to author scenarios
