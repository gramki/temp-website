# Workshop Definition Repository

Workshop and Workbench definitions are managed declaratively in a Git repository. Each Workshop has one definition repository containing the Workshop configuration and all its Workbenches.

## Repository Structure

```
workshop-{id}/
├── workshop.yaml                     # Workshop metadata
├── domain/                           # Workshop-level domain knowledge
│   ├── universal/                    # Applies to all workspaces
│   │   ├── glossary.md
│   │   └── business-rules/
│   ├── product-specification/        # Workspace-specific
│   ├── development/
│   ├── qa/
│   └── ...
├── practices/                        # Workshop-level practices
│   ├── universal/
│   │   ├── review-policies.md
│   │   └── communication-standards.md
│   ├── product-specification/
│   ├── development/
│   │   └── coding-standards.md
│   ├── qa/
│   │   └── testing-methodology.md
│   └── ...
├── shared/
│   ├── domain.yaml                   # Domain repo config
│   ├── practices.yaml                # Practices repo config
│   └── stakeholders.yaml             # Stakeholders registry config
├── capable-agents.yaml               # Workshop-level Capable Agent overrides (optional)
├── workspaces/                       # Workshop-level workspaces (BASE - all 6 required)
│   ├── product-specification/
│   │   ├── workspace.yaml
│   │   ├── .devcontainer/
│   │   │   └── devcontainer.json
│   │   ├── scenarios/
│   │   │   ├── catalog.yaml
│   │   │   ├── {scenario}.yaml
│   │   │   └── {scenario}/           # Optional Skilled Agent for scenario
│   │   │       └── skilled-agent/
│   │   │           ├── agent.yaml    # Skilled Agent definition
│   │   │           └── skills/       # Skills this agent uses
│   │   ├── skills/
│   │   │   ├── skills.yaml
│   │   │   └── {skill}/
│   │   └── hooks/
│   ├── ux-design/
│   ├── development/
│   ├── qa/
│   ├── release/
│   └── governance/
├── workbenches/
│   └── {product-code}/
│       ├── workbench.yaml            # Workbench metadata
│       ├── repositories.yaml         # Repo links (Intent, Design, Code)
│       ├── integrations.yaml         # External tools (includes Jira WO project)
│       ├── team.yaml                 # Team references
│       ├── capable-agents.yaml       # Workbench-level Capable Agent overrides (optional)
│       ├── ontology/                 # Product structure, capabilities, features
│       │   ├── capabilities.yaml
│       │   ├── features.yaml
│       │   └── modules.yaml
│       ├── domain/                   # Workbench-level domain knowledge
│       │   ├── universal/
│       │   │   └── product-glossary.md
│       │   └── {workspace-type}/
│       ├── practices/                # Workbench-level practices
│       │   ├── universal/
│       │   │   └── architecture-conventions.md
│       │   └── {workspace-type}/
│       └── workspaces/               # OVERRIDES (sparse - only files that differ)
│           ├── development/
│           │   ├── scenarios/
│           │   │   ├── custom-scenario.yaml   # Added scenario
│           │   │   └── custom-scenario/       # Skilled Agent for custom scenario
│           │   │       └── skilled-agent/
│           │   │           └── agent.yaml
│           │   └── skills/
│           │       └── product-specific-skill/  # Added skill
│           └── ...                   # Only workspaces with overrides
└── README.md
```

## Workspace Inheritance Model

Workshop-level `workspaces/` provides the **base configuration** for all Workbenches. Workbench-level `workspaces/` provides **overrides**.

### Inheritance Rules

| Rule | Behavior |
|------|----------|
| **Base** | Workshop `workspaces/` has all 6 Workspace folders (required) |
| **Override granularity** | File-level — individual files can be overridden |
| **Index merging** | `skills.yaml` and `catalog.yaml` are **merged** (Workbench entries added to Workshop entries) |
| **Sparse overrides** | Workbench only needs folders/files where overrides exist |

### Merge Process (at Session Launch)

WO Runtime merges Workshop + Workbench workspace content:

```
1. Start with Workshop workspaces/{workspace}/ as base
2. For each file in Workbench workspaces/{workspace}/:
   - If index file (skills.yaml, catalog.yaml): MERGE entries
   - If other file: REPLACE Workshop version
3. Re-prepare indexes with merged content
4. Copy merged workspace into Session container
```

### Example: Development Workspace Merge

```
Workshop workspaces/development/
├── scenarios/
│   ├── catalog.yaml          # Lists: create-feature, fix-bug
│   └── create-feature.yaml
│   └── fix-bug.yaml
└── skills/
    ├── skills.yaml           # Lists: code-generator, test-writer
    └── code-generator/
    └── test-writer/

Workbench workspaces/development/
├── scenarios/
│   ├── catalog.yaml          # Lists: custom-deploy (MERGED with Workshop)
│   └── custom-deploy.yaml    # Added
└── skills/
    ├── skills.yaml           # Lists: product-analyzer (MERGED with Workshop)
    └── product-analyzer/     # Added

Result in Session:
├── scenarios/
│   ├── catalog.yaml          # Lists: create-feature, fix-bug, custom-deploy
│   └── create-feature.yaml   # From Workshop
│   └── fix-bug.yaml          # From Workshop
│   └── custom-deploy.yaml    # From Workbench
└── skills/
    ├── skills.yaml           # Lists: code-generator, test-writer, product-analyzer
    └── code-generator/       # From Workshop
    └── test-writer/          # From Workshop
    └── product-analyzer/     # From Workbench
```

---

## Workshop Level

### `workshop.yaml`

```yaml
apiVersion: foundry/v1
kind: Workshop
metadata:
  id: workshop-abc
  name: "Payments Platform"
  description: "All payment-related products"
  foundry: foundry-zeta
spec:
  owner: "@alice"
  created: 2026-01-15
  settings:
    governancePolicy: strict
```

### Workshop Knowledge

Workshop-level knowledge is shared across all Workbenches in the Workshop. Knowledge is organized into Domain and Practices repositories, each with universal and workspace-specific scopes.

#### Domain

```
domain/
├── universal/                    # Applies to ALL workspaces
│   ├── glossary.md              # Division terminology
│   ├── business-rules/          # Business logic, constraints
│   └── regulatory/              # Division-specific compliance
├── product-specification/        # Product Specification workspace only
├── ux-design/
├── development/
│   └── api-naming-conventions.md
├── qa/
│   └── defect-classification.md
├── release/
└── governance/
```

#### Practices

```
practices/
├── universal/                    # Applies to ALL workspaces
│   ├── review-policies.md       # Division review standards
│   ├── communication.md         # Documentation standards
│   └── security/                # Security practices
├── product-specification/
│   └── spec-writing-guidelines.md
├── ux-design/
│   └── design-system.md
├── development/
│   └── coding-standards.md
├── qa/
│   └── testing-methodology.md
├── release/
│   └── release-checklist.md
└── governance/
    └── approval-workflows.md
```

→ [knowledge-management/README.md](knowledge-management/README.md) for knowledge inheritance details

---

## Workbench Level

### `workbenches/{product-code}/workbench.yaml`

```yaml
apiVersion: foundry/v1
kind: Workbench
metadata:
  id: wb-checkout
  name: "Checkout Service"
  productCode: CHKOUT-001
  workshop: workshop-abc
spec:
  description: "Core checkout flow"
  created: 2026-02-01
```

### `workbenches/{product-code}/repositories.yaml`

```yaml
apiVersion: foundry/v1
kind: WorkbenchRepositories
metadata:
  workbench: wb-checkout
spec:
  github:
    org: zeta-payments
    appInstalled: true
  intent:
    repo: zeta-payments/checkout-intent
  design:
    repo: zeta-payments/checkout-design
  code:
    - repo: zeta-payments/checkout-api
      component: checkout-api-system
    - repo: zeta-payments/checkout-ui
      component: checkout-ui-system
  qualityAutomation:
    repo: zeta-payments/checkout-tests
```

### `workbenches/{product-code}/integrations.yaml`

```yaml
apiVersion: foundry/v1
kind: WorkbenchIntegrations
metadata:
  workbench: wb-checkout
spec:
  figma:
    connected: true
    projects:
      - id: figma-proj-123
        name: "Checkout Designs"
  testRail:
    connected: true
    projects:
      - id: tr-456
        name: "Checkout Tests"
  jira:
    connected: true
    labels:
      tenant: "foundry-tenant-foundry-zeta"
      workshop: "foundry-workshop-workshop-abc"
      operations: "foundry-workbench-wb-checkout"
      feedback: "foundry-workbench-wb-checkout"
      work: "foundry-workbench-wb-checkout"
    projects:
      operations: JSM-OPS
      feedback: JIRA-FB
      work: JIRA-WORK
      workRepoWorkOrders: CHKOUT-WO  # workRepoProject in contract; Jira project key in adapter
  weave:
    connected: true
    productCode: CHKOUT-001
  additionalTools:
    - name: "Architecture Wiki"
      url: "https://wiki.internal/checkout-arch"
      category: documentation
    - name: "Datadog Dashboard"
      url: "https://datadog.internal/checkout"
      category: monitoring
```

**Note:** Shared Jira projects filter by `foundry-workbench-{workbenchId}`. The dedicated `workRepoWorkOrders` project maps to contract field `workRepoProject`. See [../../../foundry-work-plan/phase-1/repository-contracts.md](../../../foundry-work-plan/phase-1/repository-contracts.md).

### `workbenches/{product-code}/team.yaml`

```yaml
apiVersion: foundry/v1
kind: WorkbenchTeam
metadata:
  workbench: wb-checkout
spec:
  members:
    - id: user-alice
      role: manager
    - id: user-bob
      role: manager
    - id: user-carol
      role: member
    - id: user-dave
      role: member
```

### Workbench Knowledge

Workbench-level knowledge is specific to the Product. It includes Ontology (product structure), Domain knowledge, and Practices.

#### Ontology

Product structure, capabilities, and features (Workbench-only, no inheritance):

```
ontology/
├── capabilities.yaml    # What the product can do
├── features.yaml        # Features organized by capability
├── modules.yaml         # System/component structure
└── maturity.yaml        # Feature maturity states (beta, ga, deprecated)
```

#### Domain

```
domain/
├── universal/                    # Applies to ALL workspaces
│   └── product-glossary.md      # Product-specific terminology
├── product-specification/
├── development/
│   └── api-conventions.md       # Product API naming
├── qa/
└── ...
```

#### Practices

```
practices/
├── universal/
│   └── architecture-conventions.md   # Product architecture guidelines
├── development/
│   └── pr-template.md               # Product-specific PR template
├── qa/
│   └── test-coverage-thresholds.md  # Product-specific quality gates
└── ...
```

→ [knowledge-management/knowledge-hierarchy.md](knowledge-management/knowledge-hierarchy.md) for resolution rules

---

## Workspace Level

Workspaces exist at two levels:
1. **Workshop `workspaces/`** — Base configuration (all 6 required)
2. **Workbench `workspaces/`** — Overrides (sparse, only files that differ)

### Workspace Folder Structure

```
workspaces/{workspace}/
├── workspace.yaml           # Workspace metadata
├── .devcontainer/
│   ├── devcontainer.json    # Container config
│   └── Dockerfile           # Optional custom image
├── scenarios/
│   ├── catalog.yaml         # Enabled scenarios (merged if at both levels)
│   └── {scenario}.yaml      # Scenario definitions
├── skills/
│   ├── skills.yaml          # Skill index (merged if at both levels)
│   └── {skill}/
│       ├── skill.yaml       # Skill definition
│       ├── prompts/         # Prompt templates
│       └── tools/           # Skill-specific tools
└── hooks/
    ├── on-wo-start.sh
    └── on-wo-complete.sh
```

### `workspace.yaml`

Minimal metadata for the Workspace.

```yaml
apiVersion: foundry/v1
kind: Workspace
metadata:
  name: development
  workbench: wb-checkout
spec:
  description: "Development workspace for Checkout"
```

### `.devcontainer/devcontainer.json`

Standard devcontainer spec for Workspace Sessions.

```json
{
  "name": "Development Workspace",
  "image": "foundry.azurecr.io/workspaces/development:java21",
  "features": {
    "ghcr.io/devcontainers/features/java:1": { "version": "21" },
    "ghcr.io/devcontainers/features/docker-in-docker:2": {}
  },
  "customizations": {
    "vscode": {
      "extensions": [
        "redhat.java",
        "vscjava.vscode-spring-boot-dashboard"
      ]
    }
  },
  "postCreateCommand": "./setup.sh",
  "remoteUser": "developer"
}
```

### Scenarios

Scenario definitions for this Workspace.

```yaml
# scenarios/create-feature.yaml
apiVersion: foundry/v1
kind: Scenario
metadata:
  name: create-feature
  workspace: development
spec:
  description: "Implement a new feature from PSD"
  triggers:
    - manual
    - orchestrator: psd-approved
  inputs:
    - psdRef: required
    - designRef: optional
  tasks:
    - name: analyze-requirements
      title: "Analyze Requirements"
      description: "Analyze the incoming specification and identify implementation constraints."
      agentType: ai-agent
      skill: requirements-analyst
    - name: generate-code
      title: "Generate Code"
      description: "Implement the approved changes and produce code artifacts."
      agentType: ai-agent
      skill: code-generator
    - name: human-review
      title: "Human Review"
      description: "Review and refine generated code."
      agentType: human
  outputs:
    - codeCommit
    - testCommit
  governance:
    gate: development-complete
```

### Skills

Skills are defined per Workspace, alongside Scenarios. Workshop provides base skills; Workbench can add or override.

```
skills/
├── skills.yaml           # Skill index (merged across levels)
├── code-generator/
│   ├── skill.yaml        # Skill definition
│   ├── prompts/          # Prompt templates
│   └── tools/            # Skill-specific tools
├── test-writer/
└── ...
```

**Skill definition example (`skills/code-generator/skill.yaml`):**

```yaml
apiVersion: foundry/v1
kind: Skill
metadata:
  name: code-generator
  workspace: development
spec:
  description: "Generates code from specifications"
  model: claude-sonnet-4
  prompts:
    system: prompts/system.md
    task: prompts/task.md
  tools:
    - file-writer
    - code-search
    - test-runner
  constraints:
    maxTokens: 8000
    temperature: 0.2
```

**Inheritance:**
- Workshop `skills/skills.yaml` + Workbench `skills/skills.yaml` → **merged** index
- Individual skill folders: Workbench version **replaces** Workshop version if same name Current structure has skills at Workspace level only.

### Hooks

Shell scripts executed at Work Order lifecycle events.

```
hooks/
├── on-wo-start.sh       # Run when WO starts in this Workspace
└── on-wo-complete.sh    # Run when WO completes
```

---

## Knowledge Hierarchy (Agent Context)

WO Runtime builds agent context from the knowledge hierarchy. Knowledge resolves from three levels, with workspace-specific content overriding universal:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  Work Order Context                                                          │
│  (PI, WO-specific artifacts, current state)                                  │
├─────────────────────────────────────────────────────────────────────────────┤
│  Workbench Knowledge                                                         │
│  ├── Ontology (product structure, capabilities)                             │
│  ├── Domain (universal + {workspace-type})                                  │
│  └── Practices (universal + {workspace-type})                               │
├─────────────────────────────────────────────────────────────────────────────┤
│  Workshop Knowledge                                                          │
│  ├── Domain (universal + {workspace-type})                                  │
│  └── Practices (universal + {workspace-type})                               │
├─────────────────────────────────────────────────────────────────────────────┤
│  Foundry Knowledge                                                           │
│  ├── Domain (universal + {workspace-type})                                  │
│  └── Practices (universal + {workspace-type})                               │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Resolution Rules

1. **Closest level wins** — Workbench overrides Workshop overrides Foundry
2. **Workspace-specific overrides universal** — At each level, `{workspace-type}/` content overrides `universal/`
3. **File-level override** — Individual files are replaced, not merged

The agent harness (WO Runtime) merges these layers to build the right context for each agent invocation.

→ [knowledge-management/knowledge-hierarchy.md](knowledge-management/knowledge-hierarchy.md) for detailed resolution algorithm
→ [knowledge-management/knowledge-apis.md](knowledge-management/knowledge-apis.md) for query APIs

---

## Synchronization

The Workshop Definition Repository is the source of truth. Foundry Management module:
- Watches for changes (webhooks or polling)
- Validates configurations
- Applies changes to the running platform

Changes to `workbench.yaml`, `integrations.yaml`, etc. are reflected in the Foundry Web App after sync.

---

## Capable Agents Configuration

Capable Agents are configured at three levels with inheritance (see [../agent-fabric/platform-developer-guide/capable-agents.md](..//agent-fabric/platform-developer-guide/capable-agents.md)):

### Hierarchy

```
Foundry (org-level) ← foundry.yaml
    │
    └── Workshop (team-level) ← capable-agents.yaml
            │
            └── Workbench (product-level) ← capable-agents.yaml
```

### Workshop Level (`capable-agents.yaml`)

```yaml
capable-agents:
  cursor-agent:
    enabled: true
    models:
      claude-opus:
        credentials:
          api-key: ${WORKSHOP_ANTHROPIC_API_KEY}
          
  copilot:
    enabled: false  # Disabled for this Workshop
```

### Workbench Level (`workbenches/{product-code}/capable-agents.yaml`)

```yaml
capable-agents:
  cursor-agent:
    models:
      claude-opus:
        credentials:
          api-key: ${PROJECT_ANTHROPIC_API_KEY}  # Project-specific key
```

### Resolution Rules

- **Disable cascades down** — disabled at Workshop = disabled for all Workbenches
- **Credentials resolve upward** — Workbench → Workshop → Foundry (first found wins)

---

## Skilled Agents

Skilled Agents are defined per (Workspace, Scenario). See [../agent-fabric/user-guide/skilled-agents.md](..//agent-fabric/user-guide/skilled-agents.md).

### Folder Structure

```
workspaces/{workspace}/scenarios/{scenario}/
├── {scenario}.yaml           # Scenario definition
└── skilled-agent/            # Optional - if scenario has agent automation
    ├── agent.yaml            # Skilled Agent definition
    └── skills/               # Skills this agent uses
        ├── skill-a/
        │   ├── SKILL.md
        │   └── ...
        └── skill-b/
```

### agent.yaml Example

```yaml
name: feature-implementation-agent
description: Implements features based on specifications

compatible-capable-agents:
  - agent: cursor-agent
    models:
      - claude-opus
      - claude-sonnet

skills:
  - code-generator
  - test-writer

guardrails:
  - no-force-push
  - require-tests-for-new-code
```

If a Scenario does not have a `skilled-agent/` folder, tasks for that Scenario are queued for human completion.

---

## Open Questions

- Versioning strategy for Workshop repo (tags, branches?)
- Rollback mechanism for configuration changes
- Validation rules and schema enforcement
- Secrets management (OAuth tokens referenced but stored separately)

## Read Next

- [foundry-definition-repository.md](foundry-definition-repository.md) — Foundry-level repo structure
- [knowledge-management/README.md](knowledge-management/README.md) — Knowledge Management subsystem
- [knowledge-management/knowledge-hierarchy.md](knowledge-management/knowledge-hierarchy.md) — Inheritance model
