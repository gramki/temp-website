# Delegation

Delegation is the authority transfer mechanism from human to agent — a system of tokens that grants Employed Agents specific, bounded, auditable permissions to act on behalf of users within Work Order execution.

## What it is

When an [Employed Agent](agent-model.md) is spawned in a [Workspace Session](workspace-session.md), it needs authority to:

- Access repositories (read, write, commit)
- Call external services (Jira, GitHub, CI systems)
- Create sub-tasks and invoke internal Scenarios
- Make LLM model calls through the gateway

Delegation tokens grant this authority with important properties:

| Property | Description |
|----------|-------------|
| **Scoped** | Bound to specific Work Order, Session, or Task |
| **Time-limited** | Expires after duration or on Session close |
| **Revocable** | Can be cancelled before expiration |
| **Auditable** | All actions logged with token identity |
| **Quota-bound** | Subject to Foundry/Workbench/User limits |

Delegation is **not** impersonation. The agent acts with delegated authority, but the audit trail shows the agent as the actor with the human as the delegator. This maintains accountability.

The delegation flow:

```
1. User is assigned Work Order
2. User activates Session (or auto-activates)
3. WO Runtime spawns Employed Agent
4. Agent receives delegation token from user's authority
5. Token scoped to (Work Order, Session, Scenario)
6. Agent uses token for all external actions
7. Gateway validates token on each call
8. Audit log records (agent, token, action, outcome)
9. Token expires on Session close or Task completion
```

Tokens flow through the Gateway Policy Layer in Agent Fabric:

```
┌────────────────────────────────────────────────────────────────────────┐
│                       Gateway Policy Layer                              │
│                                                                         │
│    Quota enforcement │ Delegation tokens │ Credential injection │ Audit│
└────────────────────────────────────────────────────────────────────────┘
                                │
                                ▼
                      ┌─────────────────────┐
                      │   OSS LLM Gateway   │
                      │  (LiteLLM/Portkey)  │
                      └─────────────────────┘
```

## Where it lives in Foundry

| Module | Responsibility |
|--------|----------------|
| **Agent Fabric** | Token infrastructure, policy configuration |
| **WO Runtime** | Issues tokens when spawning agents |
| **Gateway Policy** | Validates tokens on each call |
| **Audit System** | Records all delegated actions |
| **Workforce Repository** | Stores delegation rules per role |

Delegation rules are configured at multiple levels:

| Level | Configuration |
|-------|---------------|
| **Foundry** | Maximum delegation scope, global limits |
| **Workbench** | Product-specific delegation policies |
| **Workspace** | Workspace-type restrictions |
| **User** | Personal delegation preferences |

## ACE/UPIM alignment

| ACE Concept | Foundry Platform Realization |
|-------------|------------------------------|
| [Delegation](../../ace/concepts.md) | Token-based authority transfer |
| Human–Agent Team | Delegation enables agent action on human's behalf |
| [Governance](governance.md) | Delegation is auditable and policy-bound |

From the Workforce Repository (UPIM): delegation rules, escalation chains, and approval authorities are part of the Responsibility Allocation Ledger.

Delegation connects the Operating Model's authority structure to runtime agent execution. UPIM defines who can delegate what; Foundry Platform's delegation system enforces those rules.

## Related concepts

- [Agent Model](agent-model.md) — Employed Agents receive delegation tokens
- [Workspace Session](workspace-session.md) — Tokens are scoped to Sessions
- [Work Order](work-order.md) — Tokens are scoped to Work Orders
- [Governance](governance.md) — Delegated actions are auditable
- [Skill](skill.md) — Skills operate within delegated authority

## Further reading

- [../agent-fabric/README.md](../agent-fabric/README.md) — Gateway Policy Layer
- [../agent-fabric/platform-developer-guide/gateway-policy.md](../agent-fabric/platform-developer-guide/gateway-policy.md) — Policy implementation
- [../work-order-runtime/README.md](../work-order-runtime/README.md) — Token issuance on spawn
- [../../ace/repositories.md#workforce-repository](../../ace/repositories.md#workforce-repository) — Delegation rules storage
