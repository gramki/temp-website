# Quota Management

Quota Management is the system of configurable usage limits at Foundry, Workbench, and User levels that controls agent resource consumption — with the effective quota calculated as the minimum of all applicable limits.

## What it is

Quotas prevent runaway costs and ensure fair resource distribution across teams and users. Every model call from an Employed Agent passes through quota checks before execution.

Quotas are configured at three levels, creating a hierarchy of constraints:

| Level | Scope | Example |
|-------|-------|---------|
| **Foundry** | Organization-wide | $50K/month total |
| **Workbench** | Product-specific | $2K/month for Checkout |
| **(Foundry, User)** | User's global limit | Alice: $500/month org-wide |
| **(Workbench, User)** | User's product limit | Alice on Checkout: $200/month |

The **effective quota** is calculated as the minimum of all applicable limits:

```
Effective Quota = min(Foundry, Workbench, (Foundry,User), (Workbench,User))
```

This ensures that no user can exceed their personal limit even if the product has budget remaining, and no product can exceed its allocation even if the org has budget remaining.

When quota is exhausted:

1. Gateway returns 429 with `X-Quota-Reset: <timestamp>`
2. Task enters **recoverable failure** state
3. Task metadata records: `blocked_reason: quota_exhausted`
4. Task resumes automatically when quota refreshes or is increased

Quota types include:

- **Monthly budget (USD)** — Total spend per period
- **Daily token limit** — Tokens consumed per day
- **Per-request cost cap** — Maximum cost for a single request

## Where it lives in Foundry

| Component | Responsibility |
|-----------|----------------|
| **Quota Manager** (Agent Fabric) | Tracks usage, computes effective quota |
| **Gateway Policy Layer** | Enforces quota on each request |
| **Foundry Definition Repo** | Foundry-level quota policy |
| **Workshop Definition Repo** | Workbench and user-level overrides |
| **Redis** | Real-time usage counters |
| **PostgreSQL** | Usage history for reporting |

Quota policy schema:

```yaml
quota:
  foundry:
    monthly_budget_usd: 50000
    daily_token_limit: 100000000
  workbenches:
    checkout:
      monthly_budget_usd: 2000
  user_defaults:
    monthly_budget_usd: 500
  user_overrides:
    alice@example.com:
      monthly_budget_usd: 1000
```

## ACE/UPIM alignment

| ACE Concept | Foundry Platform Realization |
|-------------|------------------------------|
| [Governance](../../concepts/governance.md) | Quota enforcement is a governance control |
| Resource Allocation | Quotas implement resource governance policy |
| Workspace | Quota enforcement scoped to Workbench context |

Quota Management operationalizes the ACE principle that automation must be governed. It provides the mechanism for organizations to control agent resource consumption while maintaining operational flexibility.

## Related concepts

- [Delegation](../../concepts/delegation.md) — Quota is bound to delegation tokens
- [Governance](../../concepts/governance.md) — Quota as a governance control
- [Employed Agent](employed-agent.md) — Agents that consume quota
- [Usage Analytics](usage-analytics.md) — Reporting on quota consumption

## Further reading

- [../platform-developer-guide/gateway-policy.md](../platform-developer-guide/gateway-policy.md) — Quota policy configuration and enforcement
- [../platform-developer-guide/requirements.md](../platform-developer-guide/requirements.md) — Quota Manager implementation details
