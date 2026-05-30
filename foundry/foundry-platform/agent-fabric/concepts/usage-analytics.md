# Usage Analytics

Usage Analytics is the system that aggregates and reports on agent and skill usage — tracking invocation metrics, cost attribution, and automation coverage across the Foundry.

## What it is

Usage Analytics answers the questions: How much are agents being used? What does it cost? Where is automation working well?

Every model call from an Employed Agent generates a usage event that flows through the Gateway Policy Layer. These events are enriched with context from the Delegation Token and stored for analysis:

| Dimension | Source | Purpose |
|-----------|--------|---------|
| **Session Owner** | Delegation Token | Who is responsible |
| **Work Order** | Delegation Token | Which orchestration item |
| **Task** | Delegation Token | Which specific work |
| **Workbench** | Delegation Token | Which product |
| **Skilled Agent** | Request metadata | Which agent definition |
| **Capable Agent** | Request metadata | Which agent system |
| **Model** | Request/response | Which LLM |
| **Tokens** | Response | Input/output token counts |
| **Cost** | Computed | USD based on model pricing |
| **Latency** | Measured | Request duration |

The Usage Analytics Service aggregates these events into reports:

| Report | Content |
|--------|---------|
| **By User** | Monthly cost per session owner |
| **By Workbench** | Monthly cost per product |
| **By Work Order** | Cost per orchestration item |
| **By Model** | Usage distribution across models |
| **By Skill** | Invocation counts and success rates |

Beyond cost tracking, Usage Analytics provides automation coverage metrics:

- **Automation rate** — Percentage of tasks handled by agents vs humans
- **Success rate** — Percentage of agent tasks completing without intervention
- **Fallback frequency** — How often agents fall back to alternative models
- **Failure patterns** — Common causes of agent task failures

## Where it lives in Foundry

| Component | Responsibility |
|-----------|----------------|
| **Usage Analytics Service** (Agent Fabric) | Aggregation, reporting, dashboards |
| **Gateway Policy Layer** | Emits usage events |
| **ClickHouse / TimescaleDB** | Analytics data store |
| **Audit System** | Long-term usage record retention |
| **Admin Dashboard** | Visualization and exploration |

Data flow:

```
Employed Agent → Gateway Policy Layer → Usage Event
                                              │
                                              ▼
                                      Usage Analytics Service
                                              │
                        ┌─────────────────────┼─────────────────────┐
                        │                     │                     │
                        ▼                     ▼                     ▼
                   Real-time            Batch Analytics       Billing Reports
                   Dashboards           (cost by WO)          (monthly rollup)
```

## ACE/UPIM alignment

| ACE Concept | Foundry Platform Realization |
|-------------|------------------------------|
| [Governance](../../concepts/governance.md) | Usage visibility enables governance oversight |
| Audit Trail | Usage events form the audit record for agent activity |
| Metrics | ACE emphasizes measurability; Usage Analytics implements it |

Usage Analytics operationalizes ACE's emphasis on transparency and measurability. By tracking every agent action with full attribution, organizations can govern automation effectively and demonstrate compliance.

## Related concepts

- [Quota Management](quota-management.md) — Quotas consume usage data
- [Delegation](../../concepts/delegation.md) — Tokens provide attribution context
- [Governance](../../concepts/governance.md) — Analytics enable governance oversight
- [Employed Agent](employed-agent.md) — Agents whose activity is tracked

## Further reading

- [../platform-developer-guide/requirements.md](../platform-developer-guide/requirements.md) — Usage Analytics Service specification
- [../platform-developer-guide/gateway-policy.md](../platform-developer-guide/gateway-policy.md) — How usage events are generated
- [../README.md](../README.md) — Agent Fabric module overview
