# Workshop Definition Repository

Workshop and Workbench definitions are managed declaratively in a Git repository. Each Workshop has one definition repository containing the Workshop configuration and all its Workbenches.

## Repository Structure

```
workshop-{id}/
├── workshop.yaml                     # Workshop metadata
├── knowledge/                        # Workshop-level knowledge (shared)
│   ├── domain/
│   ├── practices/
│   └── standards/
├── shared/
│   ├── domain.yaml                   # Domain repo config
│   ├── practices.yaml                # Practices repo config
│   └── stakeholders.yaml             # Stakeholders registry config
├── workspaces/                       # Workshop-level workspaces (BASE - all 6 required)
│   ├── product-specification/
│   │   ├── workspace.yaml
│   │   ├── .devcontainer/
│   │   │   └── devcontainer.json
│   │   ├── scenarios/
│   │   │   ├── catalog.yaml
│   │   │   └── *.yaml
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
│       ├── integrations.yaml         # External tools
│       ├── team.yaml                 # Team references
│       ├── knowledge/                # Workbench-level knowledge
│       │   ├── product-context/
│       │   ├── architecture/
│       │   ├── conventions/
│       │   └── templates/
│       └── workspaces/               # OVERRIDES (sparse - only files that differ)
│           ├── development/
│           │   ├── scenarios/
│           │   │   └── custom-scenario.yaml   # Added scenario
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

Workshop-level knowledge is shared across all Workbenches in the Workshop.

```
knowledge/
├── domain/           # Domain knowledge, glossaries, business rules
├── practices/        # Standards, templates, policies
└── standards/        # Coding standards, conventions
```

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
      operations: "workbench:wb-checkout"
      feedback: "workbench:wb-checkout"
      work: "workbench:wb-checkout"
    projects:
      operations: JSM-OPS
      feedback: JIRA-FB
      work: JIRA-WORK
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

Workbench-level knowledge is specific to the Product.

```
knowledge/
├── product-context/      # Product-specific context
├── architecture/         # Architecture docs, diagrams
├── conventions/          # Product-specific conventions
└── templates/            # Product-specific templates
```

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
      type: agent
      skill: requirements-analyst
    - name: generate-code
      type: agent
      skill: code-generator
    - name: human-review
      type: human
      description: "Review and refine generated code"
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

WO Runtime builds agent context from the knowledge hierarchy:

```
┌─────────────────────────────────────────┐
│  Work Order Context                     │
│  (PI, WO-specific artifacts, state)     │
├─────────────────────────────────────────┤
│  Workbench Knowledge                    │
│  (product-context, architecture, etc.)  │
├─────────────────────────────────────────┤
│  Workshop Knowledge                     │
│  (domain, practices, standards)         │
└─────────────────────────────────────────┘
```

The agent harness (WO Runtime) merges these layers to build the right context for each agent invocation.

---

## Synchronization

The Workshop Definition Repository is the source of truth. Foundry Management module:
- Watches for changes (webhooks or polling)
- Validates configurations
- Applies changes to the running platform

Changes to `workbench.yaml`, `integrations.yaml`, etc. are reflected in the Foundry Web App after sync.

---

## Open Questions

- Versioning strategy for Workshop repo (tags, branches?)
- Rollback mechanism for configuration changes
- Validation rules and schema enforcement
- Secrets management (OAuth tokens referenced but stored separately)
