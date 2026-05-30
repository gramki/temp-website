# Agent Recommender

The Agent Recommender is a service that suggests Skilled Agents for Scenario execution based on required skills, workspace fit, and historical success — providing advisory recommendations that WO Runtime can use or override.

## What it is

When WO Runtime needs to spawn an agent for a Scenario, it can ask the Agent Recommender: *Which Skilled Agent is best suited for this work?*

The recommender scores available Skilled Agents against the Scenario's requirements:

| Factor | Weight | Description |
|--------|--------|-------------|
| **Skill match** | High | Agent has skills the Scenario requires |
| **Workspace fit** | Medium | Agent is configured for this Workspace type |
| **Success history** | Low | Past success rate on similar Scenarios |

The recommendation API:

```
GET /api/v1/scenarios/{id}/recommendations

Response:
{
  "recommendations": [
    { "skilled_agent_id": "sa-code-impl", "score": 0.95, "reason": "Has all required skills" },
    { "skilled_agent_id": "sa-general", "score": 0.72, "reason": "Missing test-writer skill" }
  ]
}
```

Recommendations are **advisory, not prescriptive**. WO Runtime can override recommendations based on:

- User preference (if configured)
- Explicit agent specification in the Work Order
- Fallback due to unavailability

This keeps humans in control of agent selection while providing intelligent defaults.

The recommender operates on the effective Work Catalog — it only considers Skilled Agents that are visible at the current resolution scope. A Skilled Agent defined only at the Workshop level won't be recommended if a Workbench has overridden it with a different definition.

## Where it lives in Foundry

| Component | Responsibility |
|-----------|----------------|
| **Agent Recommender** (WCM) | Scoring and recommendation logic |
| **Skill Registry** (Agent Fabric) | Source of skill metadata for matching |
| **Resolution Engine** (WCM) | Provides effective Skilled Agent list |
| **WO Runtime** | Consumer of recommendations |

Recommendation flow:

```
Scenario Trigger → WO Runtime → Agent Recommender
                                      │
                    ┌─────────────────┼─────────────────┐
                    │                 │                 │
                    ▼                 ▼                 ▼
             Skill Match      Workspace Fit     Success History
                    │                 │                 │
                    └─────────────────┼─────────────────┘
                                      │
                                      ▼
                              Scored Recommendations
                                      │
                                      ▼
                    WO Runtime → Select → Spawn Employed Agent
```

## ACE/UPIM alignment

| ACE Concept | Foundry Platform Realization |
|-------------|------------------------------|
| [Skill](../../concepts/skill.md) | Skills drive agent matching |
| [Scenario](../../concepts/scenario.md) | Scenario requirements drive recommendations |
| Human–Agent Team | Recommendations support human oversight of agent selection |

The Agent Recommender operationalizes the ACE principle that agents should be matched to work based on capabilities. Rather than requiring admins to manually specify agents for every Scenario, the system can suggest appropriate matches while preserving human control.

## Related concepts

- [Skill](../../concepts/skill.md) — Primary matching criterion
- [Scenario](../../concepts/scenario.md) — Work that needs an agent
- [Skilled Agent](../../agent-fabric/concepts/skilled-agent.md) — What the recommender suggests
- [Work Catalog Resolution](work-catalog-resolution.md) — Provides the candidate pool

## Further reading

- [../platform-developer-guide/work-catalog-management/README.md](../platform-developer-guide/work-catalog-management/README.md) — Agent Recommender section
- [../../agent-fabric/platform-developer-guide/skilled-agents.md](../../agent-fabric/platform-developer-guide/skilled-agents.md) — Skilled Agent manifest reference
- [../../agent-fabric/concepts/skilled-agent.md](../../agent-fabric/concepts/skilled-agent.md) — Skilled Agent concept
