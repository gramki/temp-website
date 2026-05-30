# Foundry Definition Repository

Foundry-level configuration is managed declaratively in a Git repository. Each Foundry has one definition repository containing organization-wide settings, knowledge, and defaults.

## Repository Structure

```
foundry-{id}/
├── foundry.yaml                     # Foundry metadata
├── domain/                          # Foundry-level domain knowledge
│   ├── universal/                   # Applies to all workspaces
│   │   ├── glossary.md
│   │   ├── business-rules.md
│   │   └── regulatory-frameworks/
│   ├── product-specification/       # Workspace-specific
│   ├── ux-design/
│   ├── development/
│   ├── qa/
│   ├── release/
│   └── governance/
├── practices/                       # Foundry-level practices
│   ├── universal/                   # Applies to all workspaces
│   │   ├── code-of-conduct.md
│   │   ├── security-standards.md
│   │   └── review-policies/
│   ├── product-specification/
│   │   └── spec-writing-guidelines.md
│   ├── ux-design/
│   │   └── design-system-principles.md
│   ├── development/
│   │   └── coding-standards.md
│   ├── qa/
│   │   └── testing-methodology.md
│   ├── release/
│   │   └── release-checklist-template.md
│   └── governance/
│       └── approval-workflows.md
├── capable-agents.yaml              # Foundry-level Capable Agent config
└── README.md
```

## Foundry Metadata

### `foundry.yaml`

```yaml
apiVersion: foundry/v1
kind: Foundry
metadata:
  id: foundry-zeta
  name: "Zeta Corporation"
  description: "Enterprise product development foundry"
  region: us-east-1
spec:
  owner: "@foundry-admin"
  created: 2026-01-01
  settings:
    governancePolicy: strict
    defaultWorkspaceImage: foundry.azurecr.io/workspaces/base:latest
```

---

## Domain Knowledge

Foundry-level domain knowledge provides organization-wide context shared across all Workshops and Workbenches.

### Structure

```
domain/
├── universal/           # Applies to ALL workspaces in ALL workshops
└── {workspace-type}/    # Applies to specific workspace type only
```

### Universal Domain

Content in `domain/universal/` is available to agents in any workspace:

| Content Type | Purpose |
|--------------|---------|
| **Glossary** | Organization-wide terminology, acronyms, definitions |
| **Business Rules** | Core business logic, constraints, policies |
| **Regulatory Frameworks** | Compliance requirements (GDPR, SOC2, etc.) |
| **Industry Standards** | Domain-specific standards (PCI-DSS, HIPAA, etc.) |

### Workspace-Specific Domain

Content in `domain/{workspace-type}/` applies only to that workspace type:

| Workspace Type | Example Content |
|----------------|-----------------|
| `product-specification/` | Product management terminology, requirement templates |
| `ux-design/` | Design language glossary, accessibility guidelines |
| `development/` | Technical domain models, API naming conventions |
| `qa/` | Quality terminology, defect classification |
| `release/` | Deployment terminology, environment definitions |
| `governance/` | Compliance terminology, audit frameworks |

---

## Practices

Foundry-level practices establish organization-wide standards, templates, and policies.

### Structure

```
practices/
├── universal/           # Applies to ALL workspaces
└── {workspace-type}/    # Applies to specific workspace type only
```

### Universal Practices

Content in `practices/universal/` applies across all workspaces:

| Content Type | Purpose |
|--------------|---------|
| **Code of Conduct** | Professional standards for all work |
| **Security Standards** | Organization-wide security requirements |
| **Review Policies** | General review and approval guidelines |
| **Communication Standards** | Documentation and communication guidelines |

### Workspace-Specific Practices

Content in `practices/{workspace-type}/` applies only to that workspace:

| Workspace Type | Example Practices |
|----------------|-------------------|
| `product-specification/` | Spec writing guidelines, PRD templates, acceptance criteria formats |
| `ux-design/` | Design system principles, mockup conventions, accessibility checklist |
| `development/` | Coding standards, PR conventions, architecture patterns, code review checklist |
| `qa/` | Testing methodology, test case templates, coverage thresholds, defect triage |
| `release/` | Release checklist, deployment runbooks, rollback procedures, change management |
| `governance/` | Approval workflows, evidence requirements, audit trail standards |

---

## Capable Agents Configuration

Foundry-level Capable Agent configuration establishes organization-wide agent defaults.

### `capable-agents.yaml`

```yaml
apiVersion: foundry/v1
kind: CapableAgentsConfig
metadata:
  foundry: foundry-zeta
spec:
  agents:
    cursor-agent:
      enabled: true
      models:
        claude-opus:
          enabled: true
          credentials:
            api-key: ${FOUNDRY_ANTHROPIC_API_KEY}
        claude-sonnet:
          enabled: true
          credentials:
            api-key: ${FOUNDRY_ANTHROPIC_API_KEY}
      fallback:
        enabled: true
        order: [claude-opus, claude-sonnet]
        
    copilot:
      enabled: true
      credentials:
        api-key: ${FOUNDRY_GITHUB_COPILOT_KEY}
        
    claude-code:
      enabled: false  # Disabled org-wide
      
  defaults:
    fallback-behavior: auto
    quota-exceeded-behavior: pause
```

### Inheritance

Capable Agent configuration cascades down:
- **Foundry** → Workshop → Workbench
- Disabled at Foundry = disabled everywhere
- Credentials resolve upward (Workbench → Workshop → Foundry)

See [../agent-fabric/capable-agents.md](../agent-fabric/capable-agents.md) for full configuration details.

---

## Knowledge Inheritance

Foundry-level knowledge serves as the base layer in the knowledge hierarchy:

```
┌─────────────────────────────────────────┐
│  Workbench Knowledge                    │  ← Most specific (overrides)
│  (product-context, architecture)        │
├─────────────────────────────────────────┤
│  Workshop Knowledge                     │  ← Division-specific
│  (domain, practices)                    │
├─────────────────────────────────────────┤
│  Foundry Knowledge                      │  ← Organization-wide (base)
│  (domain, practices)                    │
└─────────────────────────────────────────┘
```

### Resolution Rules

1. **Closest wins** — Workbench overrides Workshop overrides Foundry
2. **Workspace-specific overrides universal** — At each level, `{workspace-type}/` content overrides `universal/` content
3. **File-level granularity** — Individual files can be overridden; no partial file merging

See [knowledge-management/knowledge-hierarchy.md](knowledge-management/knowledge-hierarchy.md) for detailed resolution rules.

---

## Synchronization

The Foundry Definition Repository is the source of truth for Foundry-level configuration.

### Sync Process

```
Foundry Repo (Git)
       │
       │ PR opened
       ▼
Workshop Validation Service ──── validates Foundry config
       │
       │ merge to main (webhook)
       ▼
Workshop Sync Service
       │
       │ writes
       ▼
Metadata Service ◄──── queries ──── All platform consumers
```

### What Gets Synced

| Content | Sync Behavior |
|---------|---------------|
| `foundry.yaml` | Parsed and stored in Metadata Service |
| `domain/**` | Indexed for agent context assembly |
| `practices/**` | Indexed for agent context assembly |
| `capable-agents.yaml` | Parsed and stored; cascades to Workshops/Workbenches |

---

## Validation Rules

The Workshop Validation Service validates Foundry repository PRs:

| Rule | Validation |
|------|------------|
| **Schema** | `foundry.yaml` conforms to Foundry schema |
| **Folder Structure** | `domain/` and `practices/` use valid workspace-type names |
| **No Secrets** | No hardcoded credentials in any files |
| **Valid YAML** | All `.yaml` files are syntactically valid |
| **Markdown Lint** | Markdown files pass linting rules |

---

## Example Content

### `domain/universal/glossary.md`

```markdown
# Organization Glossary

## Business Terms

| Term | Definition |
|------|------------|
| **Customer** | End-user of our products |
| **Partner** | Third-party integration provider |
| **Tenant** | Organization using our platform |

## Technical Terms

| Term | Definition |
|------|------------|
| **API** | Application Programming Interface |
| **SLA** | Service Level Agreement |
| **RPO** | Recovery Point Objective |
```

### `practices/development/coding-standards.md`

```markdown
# Coding Standards

## General Principles

1. **Readability over cleverness** — Code is read more than written
2. **Single responsibility** — Each function/class does one thing
3. **Explicit over implicit** — Make behavior obvious

## Language-Specific

### Java
- Follow Google Java Style Guide
- Use constructor injection for dependencies
- Prefer immutable objects

### TypeScript
- Use strict mode
- Prefer interfaces over type aliases for object shapes
- Use async/await over raw Promises
```

---

## Open Questions

- Versioning strategy for Foundry repo (tags, branches?)
- Rollback mechanism for Foundry configuration changes
- Cross-Foundry knowledge sharing (if ever needed)
- Foundry repo template for new Foundry onboarding

## Read Next

- [knowledge-management/README.md](knowledge-management/README.md) — Knowledge Management subsystem
- [knowledge-management/knowledge-hierarchy.md](knowledge-management/knowledge-hierarchy.md) — Inheritance model
- [workshop-repository.md](workshop-repository.md) — Workshop Definition Repository (Workshop/Workbench levels)
- [foundry-management/README.md](foundry-management/README.md) — Foundry lifecycle management
