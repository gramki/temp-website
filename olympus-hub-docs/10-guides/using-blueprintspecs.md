# Guide: Using BlueprintSpecs

> **Status:** 🟡 Draft
> **Audience:** Developer, Process Architect
> **Last Updated:** 2026-01-11

This guide explains how to use BlueprintSpecs from subscribed packages to create derived resources in your workbench.

---

## Table of Contents

1. [Overview](#overview)
2. [Understanding BlueprintSpecs](#understanding-blueprintspecs)
3. [Step 1: Browse Available BlueprintSpecs](#step-1-browse-available-blueprintspecs)
4. [Step 2: Review BlueprintSpec Details](#step-2-review-blueprintspec-details)
5. [Step 3: Create Derived Resource](#step-3-create-derived-resource)
6. [Step 4: Customize Derived Resource](#step-4-customize-derived-resource)
7. [Blueprint Reference Tracking](#blueprint-reference-tracking)
8. [Best Practices](#best-practices)
9. [Related Documentation](#related-documentation)

---

## Overview

**BlueprintSpecs** are specifications from Marketplace packages that serve as templates. To use them, you create **derived resources** — regular workbench specifications based on the BlueprintSpec.

```
BlueprintSpec (from Marketplace)
         │
         │ Create derived resource
         ▼
Regular Specification (your workbench)
         │
         │ Deploy
         ▼
Running Automation
```

---

## Understanding BlueprintSpecs

### Key Concepts

| Term | Description |
|------|-------------|
| **BlueprintSpec** | Template specification from a Marketplace package |
| **Derived Resource** | Regular specification created from a BlueprintSpec |
| **Blueprint Reference** | Link in derived resource to source BlueprintSpec |

### BlueprintSpec Types

| BlueprintSpec Type | Creates |
|--------------------|---------|
| `ScenarioBlueprintSpec` | `ScenarioNormativeSpec` |
| `WorkbenchBlueprintSpec` | Workbench resources |
| `MachineBlueprintSpec` | `MachineDefinitionSpec` |
| `ToolBlueprintSpec` | `ToolDefinitionSpec` |
| `RawAgentBlueprintSpec` | `RawAgentSpec` |

### Why Derived Resources?

- BlueprintSpecs are **not** directly deployable
- BlueprintSpecs remain separate from workbench definition
- Derived resources can be customized
- Update tracking is maintained

---

## Step 1: Browse Available BlueprintSpecs

### Via CLI

```bash
# List all BlueprintSpecs in current workbench
hub get blueprintspecs

# List by type
hub get scenarioblueprintspecs
hub get toolblueprintspecs
hub get machineblueprintspecs

# Filter by package
hub get blueprintspecs --package dispute-ops
```

### Via Marketplace Console

1. Navigate to **Subscriptions**
2. Select a subscribed package
3. View **Available BlueprintSpecs**

---

## Step 2: Review BlueprintSpec Details

Before creating a derived resource, understand what's in the BlueprintSpec.

### Via CLI

```bash
hub describe scenarioblueprintspec dispute-triage
```

### What to Review

| Aspect | Description |
|--------|-------------|
| **Goals** | What the scenario aims to achieve |
| **Roles** | What roles are defined |
| **SOPs** | Included procedures |
| **Dependencies** | Required tools, machines |
| **Configuration** | Default settings |

---

## Step 3: Create Derived Resource

### From ScenarioBlueprintSpec

```bash
# Create ScenarioNormativeSpec from ScenarioBlueprintSpec
hub create scenario-normative --from-blueprint dispute-triage
```

This creates:
- `dispute-triage` ScenarioNormativeSpec
- With Blueprint reference section

### Via Marketplace Console

1. Navigate to subscribed package
2. Find the BlueprintSpec
3. Click **Create Derived Resource**
4. Confirm resource name

### What's Created

```yaml
apiVersion: hub.olympus.tech/v1
kind: ScenarioNormativeSpec
metadata:
  name: dispute-triage
  namespace: dispute-ops-dev
spec:
  # ... content from BlueprintSpec ...

  # Blueprint reference added automatically
  blueprintReference:
    packageSha: "sha256:abc123..."
    packageUri: "marketplace://packages/dispute-ops-v1.2.0"
    blueprintName: "dispute-triage"
    blueprintType: "ScenarioBlueprintSpec"
    packageVersion: "1.2.0"
```

---

## Step 4: Customize Derived Resource

After creating, you can customize the derived resource for your needs.

### Edit the Resource

```bash
hub edit scenario-normative dispute-triage
```

### Common Customizations

| Aspect | Example Customization |
|--------|----------------------|
| **Goals** | Adjust SLAs for your organization |
| **Roles** | Map to your organizational roles |
| **SOPs** | Adapt procedures to your policies |
| **Escalation** | Configure your escalation matrix |
| **Environment** | Set environment-specific values |

### Divergence

When you modify a derived resource:
- It becomes **divergent** from the BlueprintSpec
- Blueprint reference is preserved
- Manual merge required for future updates

---

## Blueprint Reference Tracking

Every derived resource maintains a link to its source BlueprintSpec.

### Reference Section

```yaml
blueprintReference:
  packageSha: "sha256:abc123..."      # Package integrity
  packageUri: "marketplace://..."      # Package location
  blueprintName: "dispute-triage"      # Source BlueprintSpec
  blueprintType: "ScenarioBlueprintSpec"
  packageVersion: "1.2.0"              # Source version
```

### View Reference

```bash
hub describe scenario-normative dispute-triage --show-blueprint
```

### Why It Matters

- **Update Tracking** — Know when updates are available
- **Provenance** — Trace origin of resources
- **Merge Capability** — Apply updates from newer versions

---

## Best Practices

### 1. Review Before Creating

Always review BlueprintSpec contents before creating derived resources.

### 2. Minimize Customization Initially

Start with minimal changes to maintain sync with Blueprint.

### 3. Document Your Customizations

Keep notes on what you changed and why.

### 4. Track Updates

Regularly check for BlueprintSpec updates:

```bash
hub marketplace subscriptions list --show-updates
```

### 5. Use Version Ranges

Subscribe with version ranges to get compatible updates:

```bash
hub marketplace subscribe dispute-ops "^1.2.0" my-workbench
```

---

## Related Documentation

- [Subscribing to Packages](./subscribing-to-packages.md) — Get packages
- [Building Scenario from Blueprint](./building-scenario-from-blueprint.md) — Complete workflow
- [Managing Blueprint Updates](./managing-blueprint-updates.md) — Handle updates
- [Blueprints and Packages](../04-subsystems/marketplace/blueprints-and-packages.md) — System docs

