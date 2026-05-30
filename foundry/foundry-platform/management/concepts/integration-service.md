# Integration Service

The Integration Service manages connections to external tools — GitHub, Jira, TestRail, Figma, and Olympus Weave — handling OAuth flows, webhook configuration, and credential management for each Workbench.

## What it is

Foundry doesn't operate in isolation. Real product work requires GitHub for code, Jira for tracking, TestRail for QA, Figma for design, and potentially other tools. The Integration Service is the module that connects Workbenches to these external systems.

For each integration type, the service handles:

- **Authentication** — OAuth flows, token storage (encrypted), refresh
- **Provisioning** — Creating projects/orgs or linking existing ones
- **Webhooks** — Configuring event notifications from external tools
- **Health monitoring** — Detecting disconnections, token expiry

Supported integrations:

| Integration | What It Connects | Setup Process |
|-------------|------------------|---------------|
| **GitHub** | Code repos, PRs, commits | Install Foundry GitHub App on org |
| **Jira** | Work Orders, Operations, Feedback | OAuth authorization + project selection |
| **TestRail** | Quality Repository | OAuth authorization + project link |
| **Figma** | Design assets | OAuth authorization + team link |
| **Olympus Weave** | Portfolio integration | API key + webhook configuration |

Each integration follows a standard lifecycle:

```
Configure → Authorize (OAuth) → Provision → Active → [Disconnect]
```

Status tracking:

```yaml
JiraIntegration:
  type: jira
  site_url: "https://acme.atlassian.net"
  project_keys:
    work_orders: CHK
    operations: CHK-OPS
    feedback: CHK-FB
  oauth_token: <encrypted>
  status: active | disconnected
```

When an integration disconnects (token expired, permissions revoked), the service:
1. Marks status as `disconnected`
2. Alerts Workbench admins
3. Queues reconnection attempts
4. Gracefully degrades dependent features

## Where it lives in Foundry

| Component | Responsibility |
|-----------|----------------|
| **Integration Service** | OAuth flows, credential management, status tracking |
| **Workbench Service** | Stores integration config per Workbench |
| **Webhook handlers** | Process events from external tools |
| **Secrets store** | Encrypted credential storage (Vault/KMS) |

Integration architecture:

```
┌───────────────────────────────────────────────────────────────┐
│                      Integration Service                       │
│                                                               │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐          │
│  │   GitHub    │  │    Jira     │  │  TestRail   │          │
│  │ Integration │  │ Integration │  │ Integration │          │
│  └──────┬──────┘  └──────┬──────┘  └──────┬──────┘          │
│         │                │                │                   │
│  ┌──────┴──────┐  ┌──────┴──────┐  ┌──────┴──────┐          │
│  │   Figma     │  │   Olympus   │  │   Future    │          │
│  │ Integration │  │    Weave    │  │ Integrations│          │
│  └─────────────┘  └─────────────┘  └─────────────┘          │
│                                                               │
│                    ┌─────────────────┐                       │
│                    │  Secrets Store  │                       │
│                    │  (Vault/KMS)    │                       │
│                    └─────────────────┘                       │
└───────────────────────────────────────────────────────────────┘
         │                   │                   │
         ▼                   ▼                   ▼
    GitHub API          Jira API           Other APIs
```

## ACE/UPIM alignment

| ACE Concept | Foundry Platform Realization |
|-------------|------------------------------|
| [Repositories](../../concepts/repositories.md) | Integrations connect to repository storage |
| External Tools | ACE assumes tool integration; this service implements it |
| Workbench | Integrations are scoped to Workbenches |

The Integration Service operationalizes ACE's assumption that work happens in connected tooling. Rather than building clones of GitHub or Jira, Foundry integrates with best-of-breed tools and provides the orchestration layer.

## Related concepts

- [Declarative Provisioning](declarative-provisioning.md) — Integrations configured during provisioning
- [Repositories](../../concepts/repositories.md) — Integrations connect to repository storage
- [Containment Hierarchy](../../concepts/containment-hierarchy.md) — Integrations scoped to Workbenches

## Further reading

- [../platform-developer-guide/requirements.md](../platform-developer-guide/requirements.md) — Integration Service specification
- [../user-guide/workbench-provisioning.md](../user-guide/workbench-provisioning.md) — Setting up integrations
- [../README.md](../README.md) — Management module overview
