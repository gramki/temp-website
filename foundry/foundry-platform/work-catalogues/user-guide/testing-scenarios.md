# Testing Scenarios

This guide covers how to test scenarios before publishing them to shared catalogs.

## Why Test?

Before publishing a scenario to Workbench, Workshop, or Foundry levels, you should verify:

- The scenario is valid (passes schema and reference checks)
- Inputs and outputs are correctly defined
- Required skills are available
- The scenario executes as expected with sample data

## Testing Approaches

| Approach | What It Tests | When to Use |
|----------|---------------|-------------|
| Validation | Schema conformance, references | Always, before any other testing |
| Dry-run | Execution flow without side effects | Testing logic and task structure |
| User catalog | Real execution in isolated scope | Full end-to-end testing |
| Preview effective | Resolution behavior | Testing override scenarios |

## Validation

### IDE Validation

The Scenario Editor validates continuously as you type. Look for:

- 🔴 Red squiggles — Errors that must be fixed
- 🟡 Yellow squiggles — Warnings to review
- ℹ️ Blue hints — Suggestions

Run explicit validation:
**Command Palette:** "Scenario: Validate Current File"

### CLI Validation

```bash
# Validate a single scenario
foundry scenario validate ./scenarios/implement-feature.yaml

# Validate all scenarios in a directory
foundry scenario validate ./scenarios/

# Validate with verbose output
foundry scenario validate --verbose ./scenarios/implement-feature.yaml
```

Validation output:

```
✓ Schema conformance
✓ Required fields present
✓ Input types valid
✓ Output types valid
✓ Skills exist in registry: code-generation, test-writing, git-operations
✓ No circular dependencies in tasks

Validation passed: implement-feature.yaml
```

### Common Validation Errors

| Error | Cause | Fix |
|-------|-------|-----|
| `Unknown skill: xyz` | Skill not in registry | Check skill name spelling, or use existing skill |
| `Missing required field: scope` | Scope not specified | Add `scope: workspace-ingress` or `scope: workspace-internal` |
| `Invalid input type: foo` | Unsupported type | Use string, number, boolean, enum, object, or array |
| `Circular task dependency` | Tasks depend on each other | Review `depends-on` relationships |

## Dry-Run Testing

Dry-run executes the scenario logic without creating actual Work Orders or tasks.

### IDE Dry-Run

1. Open the scenario file
2. **Command Palette:** "Scenario: Dry Run"
3. Enter mock input values when prompted
4. Review the execution trace

### CLI Dry-Run

```bash
# Basic dry-run
foundry scenario dry-run ./scenarios/implement-feature.yaml

# With mock inputs
foundry scenario dry-run ./scenarios/implement-feature.yaml \
  --input specification_id=spec-123 \
  --input priority=high

# With mock inputs from file
foundry scenario dry-run ./scenarios/implement-feature.yaml \
  --inputs ./test-inputs.json
```

### Dry-Run Output

```
Dry-run: implement-feature
─────────────────────────────────────
Inputs received:
  specification_id: spec-123
  priority: high
  target_branch: main (default)

Task execution plan:
  1. [agent] analyze-specification
  2. [agent] implement-changes (depends: analyze-specification)
  3. [human] review-implementation (depends: implement-changes)

Skill requirements:
  ✓ code-generation — available
  ✓ test-writing — available
  ✓ git-operations — available

Expected outputs:
  - implementation_pr_url: string
  - test_coverage_percentage: number

Dry-run complete. No Work Orders created.
```

### What Dry-Run Tests

| Aspect | Tested | Not Tested |
|--------|--------|------------|
| Input validation | ✓ | — |
| Task dependency order | ✓ | — |
| Skill availability | ✓ | — |
| Output declarations | ✓ | — |
| Actual execution | — | ✗ |
| Real skill behavior | — | ✗ |
| Integration with other systems | — | ✗ |

## User Catalog Testing

For full end-to-end testing, publish to your User catalog and execute with real Work Orders.

### Step 1: Publish to User Catalog

```bash
# Publish scenario to your user catalog
foundry scenario publish ./scenarios/implement-feature.yaml --to user
```

This creates/updates the scenario in `user-work-catalog-{userId}/work-catalog/`.

### Step 2: Enable User Catalog

Enable your user catalog for testing:

**Option A: Per-session**
```bash
# When creating a Work Order
foundry wo create \
  --scenario implement-feature \
  --input specification_id=spec-123 \
  --user-catalog
```

**Option B: Profile setting**
In Web App: Settings > Preferences > "Use my Work Catalog" = On

### Step 3: Execute and Observe

Create a Work Order using your scenario:

```bash
foundry wo create \
  --workspace development \
  --scenario implement-feature \
  --input specification_id=spec-123 \
  --user-catalog
```

Monitor execution:
- **Web App:** Workspace Session > Work Orders > [your WO]
- **IDE:** Work Order panel shows status and tasks

### Step 4: Iterate

If the scenario doesn't behave as expected:

1. Update the scenario file locally
2. Re-publish to user catalog: `foundry scenario publish --to user`
3. Create a new test Work Order
4. Repeat until satisfied

### Cleanup

After testing, you can:
- Remove test scenarios from user catalog: `foundry scenario delete --from user --name implement-feature`
- Leave them for future experimentation
- Disable user catalog in profile settings

## Preview Effective Catalog

Test how your scenario will appear after resolution.

### Preview Command

```bash
# See effective catalog with your changes
foundry catalog preview \
  --workspace development \
  --include-user
```

Output shows:

```
Effective Catalog: development workspace
─────────────────────────────────────────
build/product-intent/development/scenarios/
  implement-feature.yaml
    Source: User (you) ← Workbench ← Workshop ← Platform
    Your version will override Workbench version

  implement-bugfix.yaml
    Source: Workbench
    (no user override)
```

### Preview at Specific Level

```bash
# Preview as if publishing to Workbench
foundry catalog preview \
  --workspace development \
  --at-level workbench \
  --include ./scenarios/implement-feature.yaml
```

## Testing OI Workflows

OI Workflows can also be tested:

### Workflow Validation

```bash
foundry workflow validate ./workflow.yaml
```

### Workflow Dry-Run

Simulate OI progression:

```bash
foundry workflow dry-run ./workflow.yaml \
  --from-stage draft-ready \
  --event user-task-completed \
  --event-params task-label=draft-approval
```

Output:

```
Dry-run: product-intent workflow
─────────────────────────────────
Current stage: draft-ready
Event: user-task-completed (task-label: draft-approval)

Handler matched:
  when: user-task-completed
  then:
    - transition-orchestration-item to: ready-for-specification

Resulting stage: ready-for-specification

On-enter actions for ready-for-specification:
  - notify: channel=author, template=pi-ready-for-specification
```

## Best Practices

### Test Incrementally

1. **Validate first** — Fix all schema errors
2. **Dry-run second** — Verify logic without execution
3. **User catalog third** — Full execution in isolation
4. **Publish last** — Only after testing passes

### Use Realistic Inputs

Create test input files that mirror production data:

```json
// test-inputs.json
{
  "specification_id": "spec-real-example",
  "priority": "high",
  "target_branch": "feature/dark-mode"
}
```

### Document Test Cases

Keep test inputs alongside scenarios:

```
scenarios/
├── implement-feature.yaml
└── tests/
    ├── implement-feature-basic.json
    ├── implement-feature-high-priority.json
    └── implement-feature-edge-case.json
```

### Clean Up Test Artifacts

After testing:
- Remove test Work Orders if they clutter your workspace
- Disable user catalog if you don't need it
- Document any issues found for follow-up
