# Troubleshooting

This guide covers common issues with Work Catalogs and how to resolve them.

## "Why isn't my scenario being used?"

### Symptom
You published a scenario but Work Orders are using a different version.

### Diagnosis

Check which version is active:

```bash
foundry catalog resolve \
  --workspace development \
  --scenario implement-feature
```

Output shows the resolution chain:

```
Resolving: development/scenarios/implement-feature

Level      | Found | Path
-----------|-------|---------------------------------------------
User       | No    | -
Workbench  | No    | -
Workshop   | Yes   | workshop-{id}/work-catalog/build/.../implement-feature.yaml
Foundry    | Yes   | foundry-{id}/work-catalog/build/.../implement-feature.yaml
Platform   | Yes   | platform-defaults/work-catalog/build/.../implement-feature.yaml

Active: Workshop level
```

### Common Causes

| Cause | Solution |
|-------|----------|
| Published to wrong level | Publish to a higher-priority level (e.g., Workbench instead of Workshop) |
| User catalog not activated | Enable "Use my Work Catalog" in settings, or use `--user-catalog` flag |
| Sync not complete | Wait for sync, or trigger manual refresh |
| Cache stale | Clear catalog cache: `foundry catalog refresh` |

### Fix: Enable User Catalog

If testing a User catalog scenario:

```bash
# Per Work Order
foundry wo create --scenario implement-feature --user-catalog

# Or enable globally
foundry config set user_catalog_enabled true
```

## "Scenario validation failed"

### Symptom
Validation reports errors when you try to publish or test.

### Common Errors and Fixes

#### `Unknown skill: xyz`

```
Error: Unknown skill reference: custom-code-skill
```

**Cause:** The skill doesn't exist in the registry.

**Fix:**
1. Check spelling: `foundry skills list | grep code`
2. Use an existing skill: `foundry skills list`
3. If skill should exist, contact your Foundry Admin

#### `Missing required field`

```
Error: Missing required field: scope
```

**Cause:** A required field is not present.

**Fix:** Add the missing field:
```yaml
scope: workspace-ingress  # or workspace-internal
```

#### `Invalid input type`

```
Error: Invalid input type 'text' for input 'description'
```

**Cause:** Using an unsupported type.

**Fix:** Use a supported type:
- `string`, `number`, `boolean`, `enum`, `object`, `array`

#### `Circular dependency`

```
Error: Circular task dependency detected: task-a → task-b → task-a
```

**Cause:** Tasks depend on each other in a cycle.

**Fix:** Review `depends-on` fields and break the cycle.

## "OI Workflow transition not happening"

### Symptom
An OI is stuck in a stage and not transitioning even though conditions seem met.

### Diagnosis

Check OI status:

```bash
foundry oi status <oi-id>
```

Output:

```
OI: pi-12345
Stage: in-specification
Time in stage: 5d 3h

Pending Work Orders:
  - spec-wo (in-progress)

Pending User Tasks:
  - (none)

Matched handlers awaiting:
  - (none - no matching events)

Recent events (Atropos paths):
  - /foundry-zeta/foundry.wo-runtime.work-order-progress (spec-wo at 80%)
  - /foundry-zeta/foundry.orchestrator.work-order-assigned (spec-wo)
```

### Common Causes

| Cause | Solution |
|-------|----------|
| Work Order not completed | Wait for WO to complete, or check WO status |
| Event handler mismatch | Verify handler `when` clause matches actual event |
| Missing `wo-label` | Ensure handler references correct `wo-label` |
| Governance blocked | Check governance status: `foundry oi governance <oi-id>` |

### Fix: Check Event Matching

Ensure your handler matches the event:

```yaml
# Wrong: generic event without params
- when:
    event: work-order-completed
  then: ...

# Right: specific to the labeled WO
- when:
    event: work-order-completed
    params:
      wo-label: spec-wo
      status: success
  then: ...
```

## "Work Order failed to create"

### Symptom
OI Workflow action `create-work-order` failed.

### Error Messages

#### `Scenario not found`

```
Error: Scenario 'implement-feature' not found in workspace 'development'
```

**Cause:** The scenario doesn't exist or isn't `workspace-ingress`.

**Fix:**
1. Verify scenario exists: `foundry catalog resolve --workspace development --scenario implement-feature`
2. Check scenario scope is `workspace-ingress`
3. Ensure scenario is published to an active catalog level

#### `Invalid workspace`

```
Error: Workspace 'dev' is not defined
```

**Cause:** Typo in workspace name.

**Fix:** Use correct workspace name:
```yaml
- action: create-work-order
  params:
    workspace: development  # Not 'dev'
```

## "Effective catalog looks wrong"

### Symptom
The catalog browser shows unexpected content or missing scenarios.

### Diagnosis

View effective catalog with source info:

```bash
foundry catalog list --workspace development --show-sources
```

### Common Causes

| Cause | Solution |
|-------|----------|
| Override at unexpected level | Check inheritance chain in catalog browser |
| Sync delay | Trigger sync: `foundry catalog sync` |
| Stale cache | Refresh: `foundry catalog refresh` |
| Permissions | Ensure you have access to the source repositories |

### Fix: Force Refresh

```bash
# Clear local cache
foundry catalog refresh --force

# Check sync status
foundry catalog sync-status
```

## "Skill not available"

### Symptom
Scenario requires a skill that doesn't exist or isn't accessible.

### Diagnosis

```bash
foundry skills check code-generation
```

Output:

```
Skill: code-generation
Status: Available
Registry: platform-registry
Versions: 1.0, 1.1, 1.2 (latest)
Required by your scenario: any
```

Or:

```
Skill: custom-skill
Status: Not found
Searched: platform-registry, foundry-registry
```

### Common Causes

| Cause | Solution |
|-------|----------|
| Typo in skill name | Check spelling against registry |
| Skill in different registry | Ensure correct registry is accessible |
| Skill not approved | Contact Foundry Admin for approval |

## "Governance check blocked transition"

### Symptom
OI can't transition due to governance rejection.

### Diagnosis

```bash
foundry oi governance <oi-id>
```

Output:

```
OI: pi-12345
Current stage: in-specification
Pending governance: code-review-gate

Governance status: BLOCKED
Reason: Required reviewers have not approved
Details:
  - Missing approval from: @senior-dev
  - PR: https://github.com/...

Actions available:
  - Request review from required approvers
  - (Admin) Override with justification
```

### Resolution

For `soft-block`:
- Address the concern or get manager override

For `hard-block`:
- Must resolve the underlying issue (e.g., get code review approval)
- Admin can override with documented justification

## "PR validation failed"

### Symptom
The Validation module rejects catalog changes when trying to merge a PR to a shared catalog (Workbench, Workshop, or Foundry). User catalog pushes are validated on push but are not gated by PR approval.

### Common Failures

#### Schema Validation

```
❌ Schema validation failed
   scenarios/implement-feature.yaml: line 15: invalid field 'timeout'
```

**Fix:** Remove or correct the invalid field.

#### Cross-Reference Validation

```
❌ Cross-reference validation failed
   workflow.yaml: references scenario 'process-feature' which does not exist
```

**Fix:** Either create the missing scenario or fix the reference.

#### Duplicate Name

```
❌ Duplicate scenario name
   'implement-feature' already exists at Workshop level
```

**Fix:** Use a different name, or explicitly intend to override (document in PR).

## Getting Help

If these steps don't resolve your issue:

1. **Check logs:** `foundry logs catalog-sync --recent`
2. **Search knowledge base:** [Internal wiki link]
3. **Contact support:**
   - Workbench issues → Workbench Manager
   - Workshop issues → Workshop Admin
   - Platform issues → Foundry Admin

Include in your support request:
- Scenario/workflow name and path
- Target catalog level
- Error message or unexpected behavior
- Steps you've already tried
