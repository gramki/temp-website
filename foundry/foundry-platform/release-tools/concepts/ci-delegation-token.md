# CI Delegation Token

A CI Delegation Token is a pipeline-identity-scoped authority token that grants CI agents bounded, auditable permissions to act within pipeline execution — distinct from session-scoped tokens used in Work Order execution.

## What it is

When a CI agent runs in a pipeline, it needs authority to:

- Access repositories (read, write, commit)
- Call external services (GitHub, build tools)
- Make LLM model calls through the gateway
- Produce artifacts and evidence

CI Delegation Tokens grant this authority with CI-appropriate constraints:

| Property | WO Runtime Token | CI Token |
|----------|------------------|----------|
| **Identity** | Session owner (human) | Pipeline identity (service account) |
| **Scope** | Session-scoped tools and models | CI-scoped tools and models (limited) |
| **Lifetime** | Session duration | Pipeline job duration |
| **Quota pool** | Session owner's allocation | Workbench CI allocation |
| **Attribution** | Charged to session owner | Charged to Workbench CI budget |

CI tokens intentionally exclude:

| Excluded Scope | Reason |
|----------------|--------|
| Jira MCP | CI does not interact with Jira WOs directly |
| User-specific tools | CI runs as pipeline, not human |
| Session-scoped credentials | No human session owner to delegate from |
| Full MCP connector set | CI has limited, auditable integration surface |

Token generation flow:

```
Pipeline step starts
    │
    ├── Release Tools CI requests token from Agent Fabric
    │   ├── Workbench ID
    │   ├── Pipeline identity
    │   ├── Job ID
    │   └── Requested scopes (model, limited tools)
    │
    ├── Agent Fabric validates
    │   ├── Pipeline identity authorized for Workbench
    │   ├── CI quota available
    │   └── Requested scopes permitted
    │
    └── Agent Fabric issues CI-scoped token
        ├── Short expiry (job duration)
        ├── Limited scope (no Jira, no user tools)
        └── CI quota attribution
```

The token carries the same delegation properties as WO Runtime tokens:

| Property | Description |
|----------|-------------|
| **Scoped** | Bound to specific pipeline, job, and step |
| **Time-limited** | Expires after job duration |
| **Revocable** | Can be cancelled if pipeline is aborted |
| **Auditable** | All actions logged with token identity |
| **Quota-bound** | Subject to Workbench CI limits |

CI Delegation is **not** impersonation. The agent acts with delegated authority from the pipeline identity, and the audit trail shows the agent as actor with the pipeline as delegator.

## Where it lives in Foundry

| Module | Responsibility |
|--------|----------------|
| **Agent Fabric** | Token infrastructure; issues and validates CI tokens |
| **Release Tools** | Requests tokens when spawning CI agents |
| **Gateway Policy** | Validates tokens on each call |
| **Audit System** | Records all actions taken with CI tokens |
| **Workbench config** | Defines CI quota pool and permitted scopes |

Token configuration hierarchy:

| Level | Configuration |
|-------|---------------|
| **Foundry** | Maximum CI delegation scope, global limits |
| **Workshop** | Workshop-wide CI policies |
| **Workbench** | Workbench CI budget, permitted agents |
| **Pipeline** | Per-pipeline scope restrictions |

## ACE/UPIM alignment

| ACE Concept | Foundry Platform Realization |
|-------------|------------------------------|
| [Delegation](../../concepts/delegation.md) | CI Token is the delegation mechanism for CI |
| [Governance](../../concepts/governance.md) | CI actions are auditable via token attribution |
| Pipeline identity | Not an ACE concept; operational detail |

From UPIM's Workforce Repository: delegation rules apply to both human and service identities. CI tokens operationalize delegation for service accounts within the same policy framework.

The CI Delegation Token adapts the platform's delegation pattern for CI's identity model — pipeline identity rather than human session owner.

## Related concepts

- [CI Agent Harness](ci-agent-harness.md) — Execution environment that uses CI tokens
- [Delegation](../../concepts/delegation.md) — Platform-wide delegation pattern
- [Governance](../../concepts/governance.md) — Audit trail for delegated actions
- [Quality Gates](quality-gates.md) — May invoke governance with CI tokens

## Further reading

- [../platform-developer-guide/ci-agent-architecture.md](../platform-developer-guide/ci-agent-architecture.md) — Token generation details
- [../../agent-fabric/platform-developer-guide/gateway-policy.md](../../agent-fabric/platform-developer-guide/gateway-policy.md) — Token validation
- [../../concepts/delegation.md](../../concepts/delegation.md) — Platform delegation model
