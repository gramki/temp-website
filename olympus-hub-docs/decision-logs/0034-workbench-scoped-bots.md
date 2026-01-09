# ADR-0034: One Bot of Each Kind per Workbench

| Property       | Value                                           |
|----------------|-------------------------------------------------|
| **Status**     | Accepted                                        |
| **Date**       | 2026-01-06                                      |
| **Category**   | Integration                                     |
| **Deciders**   | Architecture Team                               |
| **Supersedes** | -                                               |

---

## Context

With the decision to have persona copilot bots (Me_Bot, Ask_Bot) and a Group Orchestration Bot, we need to determine the scope at which bots are created:

1. **Tenant-scoped**: One set of bots per Hub tenant
2. **Subscription-scoped**: One set per tenant subscription
3. **Workbench-scoped**: One set per workbench

Additionally, we need to consider:
- Azure AD/Entra ID registration requirements
- Bot naming constraints
- User experience when accessing multiple workbenches

---

## Decision

**One bot of each kind (Me_Bot, Ask_Bot, Group Orchestration Bot) is registered per workbench on MS Teams. All bots are scoped to their workbench only.**

### Key Constraints

| Aspect | Constraint |
|--------|------------|
| **Bot Naming** | Must be unique across workbenches within a tenant |
| **Azure Tenant** | Each workbench corresponds to exactly one Azure/MS Teams tenant |
| **Employee Scope** | Tenant's employees and bots belong to the same Azure tenant |
| **Cross-Tenant** | Not supported (employees must be in same tenant as bots) |

### Example Configuration

```
Tenant Subscription: acme-bank-prod
├── Workbench: Dispute Operations
│   ├── dispute-ops-me (Me_Bot)
│   ├── dispute-ops-ask (Ask_Bot)
│   └── dispute-ops-hub (Group Orchestration Bot)
│
└── Workbench: Fraud Investigation
    ├── fraud-inv-me (Me_Bot)
    ├── fraud-inv-ask (Ask_Bot)
    └── fraud-inv-hub (Group Orchestration Bot)
```

---

## Alternatives Considered

### 1. Tenant-Scoped Bots

Single set of bots for entire tenant, with workbench context in conversation.

**Rejected because:**
- Users would need to specify workbench context repeatedly
- Bot capabilities would need to span all workbenches
- Permission model becomes complex
- Harder to customize per workbench

### 2. Subscription-Scoped Bots

One set of bots per subscription, shared across workbenches in that subscription.

**Rejected because:**
- Same issues as tenant-scoped
- Workbench-specific customization still needed
- Subscription is an operational boundary, not a user-facing one

### 3. Scenario-Scoped Bots

Different bots per scenario within a workbench.

**Rejected because:**
- Too many bots (dozens per workbench)
- Users would need to know which bot for which scenario
- Fragmented experience
- Complex provisioning

---

## Consequences

### Positive

1. **Clear scope** — Each bot knows its workbench context
2. **Customizable** — Process Architects can name and configure bots per workbench
3. **Permission alignment** — Bot access matches workbench permissions
4. **Simpler provisioning** — Known set of bots per workbench
5. **User clarity** — Bot name indicates which workbench it serves

### Negative

1. **Bot proliferation** — Many workbenches = many bots
2. **Naming coordination** — Must ensure unique names across workbenches
3. **Multi-workbench users** — Need to interact with multiple bots
4. **Azure registration** — Each bot needs Azure AD app registration

### Risks

1. **Azure AD limits** — May hit app registration limits in large deployments
2. **User confusion** — Similar bot names across workbenches
3. **Management overhead** — More bots to monitor and maintain

---

## Implementation Notes

### Bot Provisioning Process

1. **Tenant Admin** provisions bots on Azure AD/Entra ID
2. **Tenant Admin** configures bot identity and credentials
3. **Deployment** associates bot to Bot Profile in Cipher IAM
4. **Workbench** bots become active for the workbench

### Bot Naming Convention

Suggested: Include workbench identifier in bot name for clarity:
- `dispute-ops-agent` (Agent Copilot)
- `dispute-ops-assist` (Business Employee Copilot)
- `dispute-ops-hub` (Group Orchestration Bot)

### Multi-Workbench Access

A user can have access to any number of workbenches' bots:
- Each bot appears in their Teams as a separate contact/app
- Context is maintained per bot conversation
- User chooses which bot for which workbench need

---

## Related Decisions

- [ADR-0032: Bots as Persona Copilots](./0032-bots-as-persona-copilots.md)
- [ADR-0030: Workbench-Scoped Data Stores](./0030-workbench-scoped-data-stores.md)
- [ADR-0015: Persona-Based Operator Grouping](./0015-persona-based-operator-grouping.md)

