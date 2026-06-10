# Agent Recommender

The Agent Recommender is a service that suggests Trained Agents for Scenario execution based on required skills, Swarm membership, workspace fit, and historical success — providing advisory recommendations that WO Runtime can use or override.

## What it is

When WO Runtime needs to spawn an agent for a Scenario, it can ask the Agent Recommender: *Which Trained Agent from the referenced Swarms is best suited for this work?*

The recommender scores available Trained Agents within the Scenario's referenced Swarms against the requirements:

| Factor | Weight | Description |
|--------|--------|-------------|
| **Swarm membership** | Required | Agent must belong to a Swarm referenced by the Scenario |
| **Skill match** | High | Agent has skills the Scenario requires |
| **Workspace fit** | Medium | Agent is configured for this Workspace type |
| **Success history** | Low | Past success rate on similar Scenarios |

The recommendation API:

```
GET /api/v1/scenarios/{id}/recommendations

Response:
{
  "scenario_id": "implement-feature",
  "referenced_swarms": ["build-swarm", "review-swarm"],
  "recommendations": [
    {
      "trained_agent_jid": "feature-implementer@build-swarm.agents.acme.foundry.io",
      "swarm": "build-swarm",
      "score": 0.95,
      "reason": "Has all required skills; designated coordinator"
    },
    {
      "trained_agent_jid": "code-refactorer@build-swarm.agents.acme.foundry.io",
      "swarm": "build-swarm",
      "score": 0.78,
      "reason": "Strong skill match but not coordinator"
    }
  ]
}
```

Recommendations are **advisory, not prescriptive**. WO Runtime can override recommendations based on:

- Coordinator agent specification (always explicit in Scenario)
- User preference (if configured)
- Explicit agent specification in the Work Order
- Fallback due to unavailability

This keeps humans in control of agent selection while providing intelligent defaults.

The recommender operates on Swarm-scoped candidates — it only considers Trained Agents from Swarms referenced by the Scenario, visible at the current scope. Swarm visibility follows the hierarchy: Workspace → Workbench → Workshop → Foundry.

## Where it lives in Foundry

| Component | Responsibility |
|-----------|----------------|
| **Agent Recommender** (WCM) | Scoring and recommendation logic |
| **Swarm Registry** (Agent Fabric) | Source of Trained Agent membership and metadata |
| **Skill Registry** (Agent Fabric) | Source of skill metadata for matching |
| **WO Runtime** | Consumer of recommendations |

Recommendation flow:

```
Scenario Trigger → WO Runtime → Agent Recommender
                                      │
                    ┌─────────────────┼─────────────────┐
                    │                 │                 │
                    ▼                 ▼                 ▼
             Swarm Scope      Skill Match       Success History
             (filter by       (score within    (weight by past
              referenced       candidates)      performance)
              Swarms)
                    │                 │                 │
                    └─────────────────┼─────────────────┘
                                      │
                                      ▼
                              Scored Recommendations
                                      │
                                      ▼
                    WO Runtime → Select → Spawn Employed Agent
```

## Swarm-Aware Resolution

The recommender resolves candidates through Swarm membership:

1. **Identify referenced Swarms** — Read the Scenario's `swarms:` field
2. **Resolve Swarm visibility** — Apply scope hierarchy (Workspace/Workbench/Workshop/Foundry)
3. **Enumerate Trained Agents** — List all Trained Agents in referenced Swarms (including tenant extensions of platform Swarms)
4. **Score candidates** — Apply skill match, workspace fit, and history factors
5. **Return ranked list** — Ordered by composite score

For Scenarios with an explicit `coordinator-agent` field (`{swarm}/{agent}` notation), the coordinator is always returned as the top recommendation.

## ACE/UPIM alignment

| ACE Concept | Foundry Platform Realization |
|-------------|------------------------------|
| [Skill](../../concepts/skill.md) | Skills drive agent matching |
| [Scenario](../../concepts/scenario.md) | Scenario requirements and Swarm references drive recommendations |
| Human–Agent Team | Recommendations support human oversight of agent selection |

The Agent Recommender operationalizes the ACE principle that agents should be matched to work based on capabilities. Rather than requiring admins to manually specify agents for every Scenario, the system can suggest appropriate matches while preserving human control.

## Related concepts

- [Skill](../../concepts/skill.md) — Primary matching criterion
- [Scenario](../../concepts/scenario.md) — Work that references Swarms
- [Trained Agent](../../agent-fabric/concepts/trained-agent.md) — What the recommender suggests
- [Swarm](../../agent-fabric/concepts/swarm.md) — Organizational unit that scopes candidates
- [Work Catalog Resolution](work-catalog-resolution.md) — Provides context for scope

## Further reading

- [../platform-developer-guide/work-catalog-management/README.md](../platform-developer-guide/work-catalog-management/README.md) — Agent Recommender section
- [../../agent-fabric/platform-developer-guide/swarm-registry.md](../../agent-fabric/platform-developer-guide/swarm-registry.md) — Swarm Registry API
- [../../agent-fabric/platform-developer-guide/trained-agents.md](../../agent-fabric/platform-developer-guide/trained-agents.md) — Trained Agent manifest reference
- [../../agent-fabric/concepts/trained-agent.md](../../agent-fabric/concepts/trained-agent.md) — Trained Agent concept
