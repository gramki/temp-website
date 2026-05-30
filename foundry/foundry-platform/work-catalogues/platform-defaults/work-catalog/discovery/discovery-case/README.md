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

## Workspaces (Proposed)

| Workspace | Purpose |
|-----------|---------|
| User Research | Conduct user interviews, surveys, analysis |
| Market Analysis | Competitive and market research |
| Technical Discovery | Feasibility and architecture exploration |
| Synthesis | Compile insights and recommendations |

## TODO

- [ ] Define `workflow.yaml` for Discovery Case lifecycle
- [ ] Create workspace folders with scenario placeholders
- [ ] Document governance checkpoints
- [ ] Define handoff to Build track (when discovery leads to Product Intent)

## Related

- [../../README.md](../../README.md) — Work Catalogs overview
- [../build/product-intent/](../build/product-intent/) — Build track example (fully defined)
