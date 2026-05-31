# Repositories

Repositories are the 15 canonical storage types that persist what a Workshop knows, produces, and remembers — the knowledge infrastructure supporting both AI and human agents throughout the product lifecycle.

## What it is

ACE defines a taxonomy of repositories that every Workshop maintains. These repositories represent the workshop's accumulated state across four themes:

| Theme | Purpose | Repositories |
|-------|---------|--------------|
| **Knowledge** | Domain facts, ontology, standards | Domain, Ontology |
| **Skills** | Practitioner-grade methods and playbooks | Practices |
| **Artifacts** | Outputs the workshop produces | Intent, Design, Code, Quality, Operations |
| **History** | Decisions, feedback, evolution, audit | Work, Feedback, Evolution, Workforce, Stakeholders |

The 15 canonical repository types with UPIM alignment:

| Repository | Code | UPIM Mapping | Scope |
|------------|------|--------------|-------|
| **Product Intent** | PIR | Strategy & Intent | Workshop |

> **Naming:** In new Foundry Platform prose, prefer **Intent Repository**. The ACE code **PIR** means Product Intent Repository. **PIR** also abbreviates Post-Incident Review in Run Track — write that term in full in platform-facing docs. See [../../glossary.md](../../glossary.md#pir-term-overload).
| **Domain** | DKB | Domain Knowledge | Workshop |
| **Ontology** | POR | Structural Topology | Workbench |
| **Design** | DAR | Technical, Ecosystem, Operational (definitions) | Workshop |
| **Code** | CAR | Build + Run engineering code | Workshop |
| **Quality** | QVS | Build quality verification | Workshop |
| **Operations** | OPR | Run artifacts | Workshop |
| **Feedback** | PFR | Win, Run, Build feedback views | Workshop |
| **Work** | WR | All tracks work instances | Workshop |
| **Practices** | PPR | Operating Model + Evolve | Workshop |
| **Workforce** | WFR | Operating Model (internal workforce) | Foundry |
| **Stakeholders** | - | Cross-cutting (reference layer) | Foundry |
| **Evolution** | PEIR | Traceability | Workshop |
| **Skill** | ESR | Agent capabilities | Foundry |

**Scope distinction:** Most repositories are Workshop-scoped (one per Workshop). Some are Foundry-scoped (shared across all Workshops in a Foundry), like Workforce and Stakeholders. Ontology is Workbench-scoped (each product defines its own structure).

The Feedback repository has three partitions by Track affinity:
- **Feedback (Win)** — FIRs, Win Cases, customer communication
- **Feedback (Run)** — Incident mirrors, operational observations
- **Feedback (Build)** — Bug report mirrors, tech debt observations

**Repositories are services, not stores.** Each provides injection/access interfaces; Foundry Management exposes the access layer. Consumers query through APIs, not directly from Git.

## Where it lives in Foundry

| Module | Repository Responsibility |
|--------|---------------------------|
| **Management** | Provisions repositories; provides access APIs |
| **Work Catalog Management** | Uses repositories for scenario artifacts |
| **Knowledge Management** | Manages Domain, Practices, Ontology |
| **WO Runtime** | Reads/writes repositories during execution |
| **Evolution Repository** | Cross-repo lineage and knowledge graph |

Storage locations vary by repository type:

| Type | Storage |
|------|---------|
| **Git-backed** | Intent Repository, Design, Code repos (GitHub) |
| **Work Repository** | Work Items (Jira adapter in Phase 1); vendor-neutral `workRepo*` contract fields |
| **Service-backed** | Metadata Service, Ontology, Evolution |
| **Hybrid** | Quality (TestRail + Git) |

## ACE/UPIM alignment

| ACE Concept | Foundry Platform Realization |
|-------------|------------------------------|
| [Repository taxonomy](../../ace/repositories.md) | 15 types provisioned and managed |
| [Workshop repositories](../../ace/concepts.md#workshop) | Workshop-scoped by default |
| [Foundry-scoped repositories](../../ace/repositories.md) | Workforce, Stakeholders, Skill shared |

From ACE: "Repositories are how a Workshop persists what it knows, what it produces, and what it remembers."

The four-theme clustering (Knowledge, Skills, Artifacts, History) is for presentation. The formal taxonomy with codes and UPIM mappings is authoritative.

Phase 1 artifact URIs use Foundry containment scoping:

```text
artifact://{foundry-id}/{workshop-id}/{workbench-id}/{repo-type}/{artifact-type}/{artifact-id}@{revision}
```

See [../../foundry-work-plan/phase-1/repository-contracts.md](../../foundry-work-plan/phase-1/repository-contracts.md). ACE landscape-scoped URIs remain documented in [../../ace/repositories.md](../../ace/repositories.md).

## Related concepts

- [Containment Hierarchy](containment-hierarchy.md) — Repository scope (Foundry, Workshop, Workbench)
- [Knowledge Hierarchy](knowledge-hierarchy.md) — Domain, Practices, Ontology inheritance
- [Metadata Service](metadata-service.md) — Where repository configs are served
- [Track](track.md) — Work and Feedback organized by Track

## Further reading

- [../../foundry-work-plan/phase-1/repository-contracts.md](../../foundry-work-plan/phase-1/repository-contracts.md) — Phase 1 entity and URI SSOT
- [../../foundry-work-plan/phase-1/api-surface.md](../../foundry-work-plan/phase-1/api-surface.md) — repo vs track API routes
- [../../ace/repositories.md](../../ace/repositories.md) — Canonical repository taxonomy
- [../management/platform-developer-guide/git-infrastructure.md](../management/platform-developer-guide/git-infrastructure.md) — Git repository provisioning
- [../management/platform-developer-guide/workshop-repository.md](../management/platform-developer-guide/workshop-repository.md) — Workshop Definition Repository structure
- [../management/platform-developer-guide/foundry-definition-repository.md](../management/platform-developer-guide/foundry-definition-repository.md) — Foundry repo structure
