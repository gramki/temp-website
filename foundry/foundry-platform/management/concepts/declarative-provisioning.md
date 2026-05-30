# Declarative Provisioning

Declarative Provisioning is the infrastructure-as-configuration model where admins describe what they want (a Workshop, Workbench, or repository) and the Management module creates and connects all the required pieces automatically.

## What it is

Foundry Management treats infrastructure as configuration. A Workbench is not just a database entry — it's a GitHub org, a Jira project, a TestRail instance, a Figma workspace, all wired together. Declarative Provisioning handles this complexity by translating high-level intent into concrete infrastructure.

When an admin provisions a Workbench, they specify:

```yaml
name: Checkout
product_code: checkout
workshop: ecommerce
integrations:
  github:
    org_name: acme-checkout
  jira:
    project_key: CHK
  testrail:
    project_id: checkout-qa
```

The Management module then:

1. Creates the Workbench record
2. Creates or links the GitHub organization
3. Creates Intent and Design repositories
4. Creates the Jira project with Foundry-specific fields
5. Provisions Metadata Service and Ontology Service instances
6. Initializes the Workshop Definition Repo with Workbench scaffold
7. Configures webhooks across all integrations

This approach provides:

- **Consistency** — Every Workbench has the same structure
- **Completeness** — No manual setup steps forgotten
- **Repeatability** — Provisioning can be automated in CI/CD
- **Auditability** — Provisioning state is tracked and versioned

The same pattern applies at Workshop level (creating the Workshop Definition Repository, setting up defaults) and Foundry level (creating the Foundry Definition Repository, configuring platform-wide settings).

## Where it lives in Foundry

| Component | Responsibility |
|-----------|----------------|
| **Workshop Service** | Provisions Workshops and their definition repos |
| **Workbench Service** | Provisions Workbenches and all integrations |
| **Repository Service** | Manages repository lifecycle |
| **Integration Service** | Connects external tools (GitHub, Jira, etc.) |
| **Management API** | REST interface for provisioning operations |

Provisioning workflow:

```
Admin Request → Management API → Workbench Service
                                      │
        ┌─────────────────────────────┼─────────────────────────────┐
        │                             │                             │
        ▼                             ▼                             ▼
   GitHub App              Jira Integration              Other Integrations
   (create org,            (create project,             (TestRail, Figma,
    create repos)           configure fields)            Olympus Weave)
        │                             │                             │
        └─────────────────────────────┼─────────────────────────────┘
                                      │
                                      ▼
                              Workbench Active
```

## ACE/UPIM alignment

| ACE Concept | Foundry Platform Realization |
|-------------|------------------------------|
| [Workshop](../../../ace/concepts.md) | Declaratively provisioned divisions/units |
| [Workbench](../../../ace/concepts.md) | Declaratively provisioned Product containers |
| [Repositories](../../concepts/repositories.md) | Auto-created and connected during provisioning |

Declarative Provisioning operationalizes ACE's containment hierarchy. ACE defines the *what* (Workshops contain Workbenches); Declarative Provisioning implements the *how* (automated, configuration-driven setup).

## Related concepts

- [Containment Hierarchy](../../concepts/containment-hierarchy.md) — Structure that provisioning creates
- [Repositories](../../concepts/repositories.md) — Repos created during provisioning
- [Integration Service](integration-service.md) — External tools connected during provisioning
- [Workshop Sync](workshop-sync.md) — Propagates provisioned config to Metadata Service

## Further reading

- [../README.md](../README.md) — Management module overview
- [../platform-developer-guide/requirements.md](../platform-developer-guide/requirements.md) — Provisioning service specifications
- [../user-guide/workbench-provisioning.md](../user-guide/workbench-provisioning.md) — How to provision Workbenches
