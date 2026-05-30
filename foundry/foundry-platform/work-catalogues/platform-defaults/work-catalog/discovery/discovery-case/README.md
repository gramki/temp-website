# Discovery Case

**Orchestration Item for the Discovery track.**

> **Status:** Stub — workflow and scenarios to be defined.

## Overview

A Discovery Case represents a discovery initiative — exploring unknowns, validating hypotheses, and generating insights that inform product decisions. Discovery Cases help teams understand user needs, market opportunities, and technical feasibility before committing to build.

## UPIM Alignment

| UPIM Concept | Discovery Track Realization |
|--------------|----------------------------|
| Discovery Track | This folder |
| Discovery Case | OI coordinating discovery activities |
| Insights, Hypotheses | Work entities processed by scenarios |

## Lifecycle (Proposed)

```
start → discovery-initiated → research-in-progress → insights-synthesized → 
recommendations-ready → decision-made → end
```

### Stage Descriptions (Proposed)

| Stage | Description |
|-------|-------------|
| `discovery-initiated` | Discovery case created, scope defined |
| `research-in-progress` | Active research and investigation |
| `insights-synthesized` | Research complete, insights being compiled |
| `recommendations-ready` | Recommendations prepared for decision |
| `decision-made` | Stakeholders have decided next steps |

## Stations and scenarios (Proposed)

Discovery reuses the canonical six [workspace stations](../../../../../../ace/workspaces/README.md) — functional teams, not stages. Discovery work is discovery-flavored ingress scenarios on those same teams; the items below are scenarios, not new workspaces.

| Station | Discovery scenarios (activities) |
|---------|----------------------------------|
| Product Specification | Frame the case, market/product research, deliberation, evidence synthesis, record the PDR, Definition-Model updates |
| UX Design | User research, usability experiments, design prototypes |
| Development | Technical feasibility, spikes, proofs of concept |
| QA | Testability assessment, experiment-evidence validation |
| Release | Operational/rollout feasibility assessment |
| Governance | PDR alignment review, discovery closure review (cross-cutting) |

Discovery typically uses *some* stations heavily (Product Specification, UX Design, Development) and others lightly. The Discovery Case workflow may fan one stage out to several stations in parallel.

## TODO

- [ ] Define `workflow.yaml` for Discovery Case lifecycle
- [ ] Add discovery scenario files under the relevant station folders (no new workspaces)
- [ ] Document governance checkpoints
- [ ] Define handoff to Build track (when discovery leads to Product Intent)

## Related

- [../../README.md](../../README.md) — Work Catalogs overview
- [../build/product-intent/](../build/product-intent/) — Build track example (fully defined)
