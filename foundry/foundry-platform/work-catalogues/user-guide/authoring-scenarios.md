# Authoring Scenarios

This guide covers how to create and edit Scenarios using the Scenario Editor.

## Prerequisites

- IDE with Foundry extensions installed
- Access to a Work Catalog repository (Workbench, Workshop, or your User catalog)
- Understanding of [how work flows](how-work-flows.md)

## Scenario Basics

A Scenario is a YAML file that defines:

```yaml
apiVersion: scenario/v1
name: implement-feature
description: Implement a feature from product specification
workspace: development
scope: workspace-ingress

inputs:
  - name: specification_id
    type: string
    required: true
    description: ID of the product specification to implement
  - name: priority
    type: enum
    values: [low, normal, high, critical]
    default: normal

outputs:
  - name: implementation_pr_url
    type: string
    description: URL of the pull request with implementation
  - name: test_coverage_percentage
    type: number

required-skills:
  - code-generation
  - test-writing
  - git-operations

tasks:
  - id: analyze-specification
    type: agent
    description: Analyze the specification and plan implementation
    
  - id: implement-changes
    type: agent
    description: Implement the code changes
    depends-on: [analyze-specification]
    
  - id: review-implementation
    type: human
    description: Review the implementation
    depends-on: [implement-changes]
```

## Creating a New Scenario

### Using the IDE

1. **Open Work Catalog Explorer** (Cmd/Ctrl+Shift+W)

2. **Navigate to the target folder:**
   - For Workbench scenarios: `workshop-{id}/workbenches/{wb}/work-catalog/{track}/{oi}/{workspace}/scenarios/`
   - For User catalog: `user-work-catalog-{userId}/work-catalog/<track>/<oi>/<workspace>/scenarios/`

3. **Create new file:** Right-click > "New Scenario"

4. **Choose a template or start blank**

The Scenario Editor opens with schema-aware editing enabled.

### Using the Command Line

```bash
# Create scenario file
foundry scenario create \
  --workspace development \
  --name implement-feature \
  --output ./scenarios/implement-feature.yaml
```

## Scenario Editor Features

### Schema-Aware Editing

The editor provides:

- **Autocomplete** for all schema fields
- **Type validation** as you type
- **Hover documentation** for each field
- **Quick fixes** for common errors

### Field Descriptions

| Field | Required | Description |
|-------|----------|-------------|
| `apiVersion` | Yes | Schema version (currently `scenario/v1`) |
| `name` | Yes | Unique identifier within the workspace |
| `description` | Yes | Human-readable description |
| `workspace` | Yes | Which workspace type this scenario belongs to |
| `scope` | Yes | `workspace-ingress` or `workspace-internal` |
| `inputs` | No | Input parameters the scenario accepts |
| `outputs` | No | Output values the scenario produces |
| `required-skills` | No | Skills needed to execute this scenario |
| `tasks` | No | Task definitions (can be generated from skills) |

### Scope Selection

Choose the appropriate scope:

**`workspace-ingress`** — Use when:
- The Orchestrator should be able to invoke this scenario
- Other Workspaces need to trigger this work
- This represents a capability the Workspace offers externally

**`workspace-internal`** — Use when:
- This is a helper scenario used by tasks within a Work Order
- You don't want external invocation
- This is an implementation detail, not a contract

### Input Definition

Inputs define what data the scenario needs:

```yaml
inputs:
  - name: specification_id
    type: string
    required: true
    description: The specification to implement
    
  - name: target_branch
    type: string
    required: false
    default: main
    description: Branch to create PR against
    
  - name: complexity
    type: enum
    values: [simple, moderate, complex]
    required: true
```

Supported types:
- `string` — Text value
- `number` — Numeric value
- `boolean` — True/false
- `enum` — One of specified values
- `object` — Structured data (specify schema)
- `array` — List of values (specify item type)

### Output Definition

Outputs define what the scenario produces:

```yaml
outputs:
  - name: implementation_pr_url
    type: string
    description: URL of the implementation PR
    
  - name: files_changed
    type: array
    items: string
    description: List of files modified
```

Outputs are captured by the Work Order and can be:
- Used by subsequent scenarios in the OI Workflow
- Recorded in the OI's completion data
- Referenced in notifications and reports

### Skill Requirements

List skills the scenario needs:

```yaml
required-skills:
  - code-generation      # Generate code from specifications
  - test-writing         # Write unit and integration tests
  - git-operations       # Commit, branch, create PRs
  - jira-integration     # Optional: update tickets
```

The Agent Recommender uses this to suggest appropriate Skilled Agents.

Browse available skills:
- **Web App:** Resources > Skill Registry
- **IDE:** Command Palette > "Skills: Browse Registry"

### Task Definition

Tasks are optional in the scenario definition. You can:

**Option A: Define tasks explicitly**
```yaml
tasks:
  - id: analyze
    type: agent
    description: Analyze requirements
    
  - id: implement
    type: agent
    depends-on: [analyze]
    
  - id: review
    type: human
    depends-on: [implement]
```

**Option B: Let the Skilled Agent determine tasks**
Omit the `tasks` section; the assigned Skilled Agent creates tasks based on its skills and the inputs provided.

**Option C: Hybrid**
Define key milestones as tasks; let the agent fill in details.

## Validation

### Real-Time Validation

The editor validates as you type:

| Check | Description |
|-------|-------------|
| Schema conformance | YAML matches scenario schema |
| Required fields | All required fields present |
| Type correctness | Values match declared types |
| Skill references | Referenced skills exist in registry |
| Name uniqueness | No duplicate scenario name in workspace |

### Manual Validation

Run full validation:

**IDE:** Command Palette > "Scenario: Validate"

**CLI:**
```bash
foundry scenario validate ./scenarios/implement-feature.yaml
```

Validation checks:
- Schema conformance
- Skill existence
- Input/output consistency
- Cross-reference validity

## Best Practices

### Naming Conventions

- Use kebab-case: `implement-feature`, not `implementFeature`
- Be specific: `implement-product-specification`, not `implement`
- Include the action: `create-`, `review-`, `test-`, `deploy-`

### Scope Decisions

Default to `workspace-internal` unless you specifically need external invocation. This keeps the Workspace's public contract minimal and intentional.

### Input Design

- Make inputs as specific as needed, no more
- Use `required: true` sparingly — prefer sensible defaults
- Document each input with `description`
- Use enums for constrained values

### Output Design

- Only declare outputs that consumers need
- Don't expose implementation details as outputs
- Use consistent naming across scenarios

### Skill Requirements

- List only skills the scenario actually needs
- Don't over-specify — let the Agent Recommender do its job
- Check skill availability before publishing

## Next Steps

After creating a scenario:

1. **Test it** — See [testing-scenarios.md](testing-scenarios.md)
2. **Publish it** — See [publishing-workflow.md](publishing-workflow.md)
3. **Monitor usage** — See the effective catalog in Web App
