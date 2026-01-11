# Guide: Building a Scenario from BlueprintSpec

> **Status:** 🟡 Draft
> **Audience:** Process Architect, Developer
> **Last Updated:** 2026-01-11

Complete guide to building a fully functional scenario using a ScenarioBlueprintSpec from the Marketplace.

---

## Table of Contents

1. [Overview](#overview)
2. [Prerequisites](#prerequisites)
3. [Step 1: Browse Available BlueprintSpecs](#step-1-browse-available-blueprintspecs)
4. [Step 2: Create ScenarioNormativeSpec from Blueprint](#step-2-create-scenarionormativespec-from-blueprint)
5. [Step 3: Customize Normative Specification](#step-3-customize-normative-specification)
6. [Step 4: Create ScenarioAutomationSpec](#step-4-create-scenarioautomationspec)
7. [Step 5: Create ScenarioDeploymentSpec](#step-5-create-scenariodeploymentspec)
8. [Step 6: Deploy the Scenario](#step-6-deploy-the-scenario)
9. [Blueprint Reference Tracking](#blueprint-reference-tracking)
10. [Handling Updates from Blueprint](#handling-updates-from-blueprint)
11. [Troubleshooting](#troubleshooting)
12. [Related Documentation](#related-documentation)

---

## Overview

Building a scenario from a BlueprintSpec follows the standard scenario development journey, but starts with a template from the Marketplace rather than from scratch.

### Journey

```
Subscribe to Package
         │
         ▼
Create ScenarioNormativeSpec ← from ScenarioBlueprintSpec
         │
         ▼
Create ScenarioAutomationSpec
         │
         ▼
Create ScenarioDeploymentSpec
         │
         ▼
Deploy Scenario
```

---

## Prerequisites

| Requirement | Description |
|-------------|-------------|
| **Package Subscription** | Active subscription to package |
| **Workbench Access** | DEV workbench for development |
| **Role** | Process Architect (normative) or Developer (automation) |
| **Prerequisites Met** | Required machines/tools configured |

---

## Step 1: Browse Available BlueprintSpecs

Confirm the ScenarioBlueprintSpec you need is available.

```bash
# List Scenario BlueprintSpecs
hub get scenarioblueprintspecs

# View details
hub describe scenarioblueprintspec dispute-triage
```

### Review Contents

Check what's included:
- Goals and SLAs
- Roles
- SOPs
- Tool dependencies
- Configuration

---

## Step 2: Create ScenarioNormativeSpec from Blueprint

### Create the Derived Resource

```bash
hub create scenario-normative --from-blueprint dispute-triage
```

Or via Marketplace Console:
1. Navigate to subscribed package
2. Find `dispute-triage` BlueprintSpec
3. Click **Create Derived Resource**

### Verify Creation

```bash
hub get scenario-normative dispute-triage
```

---

## Step 3: Customize Normative Specification

Adapt the normative spec to your organization.

### Open for Editing

```bash
hub edit scenario-normative dispute-triage
```

### Common Customizations

| Section | Customization |
|---------|---------------|
| **Goals** | Adjust SLAs to your requirements |
| **Roles** | Map to your organizational structure |
| **SOPs** | Adapt procedures to your policies |
| **Escalation** | Configure your escalation matrix |

### Example Customization

```yaml
spec:
  goals:
    - id: "resolve-dispute"
      description: "Resolve dispute within SLA"
      sla: "P7D"  # Changed from P10D to P7D
  
  roles:
    - id: "triage-agent"
      mapTo: "dispute-analysts"  # Map to your IAM group
```

### Validate

```bash
hub validate scenario-normative dispute-triage
```

---

## Step 4: Create ScenarioAutomationSpec

If the package includes automation components, create the automation spec.

### Create from Package Resources

```bash
hub create scenario-automation dispute-triage \
  --normative-ref dispute-triage
```

### Configure Hub Application

```yaml
spec:
  application:
    runtime: rhea
    container: dispute-triage-app:1.2.0
  
  triggers:
    - name: dispute-filed
      source: atropos
      topic: card-network.disputes
  
  tools:
    - ref: card-network-lookup
```

### Validate

```bash
hub validate scenario-automation dispute-triage
```

---

## Step 5: Create ScenarioDeploymentSpec

Create the deployment specification.

```bash
hub create scenario-deployment dispute-triage-sandbox \
  --scenario dispute-triage \
  --environment sandbox
```

### Configure Deployment

```yaml
spec:
  scenario: dispute-triage
  environment: sandbox
  
  scaling:
    replicas: 1
  
  resources:
    memory: 512Mi
    cpu: 500m
```

---

## Step 6: Deploy the Scenario

### Validate Everything

```bash
hub validate scenario dispute-triage
```

### Deploy

```bash
hub sync scenario dispute-triage-sandbox
```

### First Deployment Notes

On first deployment:
- Containers are cloned from Marketplace (lazy cloning)
- Signature verified during clone
- May take slightly longer than subsequent deployments

### Verify Deployment

```bash
hub get scenario-deployment dispute-triage-sandbox --show-status
```

---

## Blueprint Reference Tracking

Your derived resources maintain links to their source BlueprintSpecs.

### View Reference

```bash
hub describe scenario-normative dispute-triage --show-blueprint
```

### Reference Contents

```yaml
blueprintReference:
  packageSha: "sha256:abc123..."
  packageUri: "marketplace://packages/dispute-ops-v1.2.0"
  blueprintName: "dispute-triage"
  blueprintType: "ScenarioBlueprintSpec"
  packageVersion: "1.2.0"
```

### Status Tracking

| Status | Meaning |
|--------|---------|
| **Synced** | Matches current Blueprint |
| **Update Available** | Newer version exists |
| **Divergent** | Modified after creation |
| **Out-of-Sync** | Chose not to update |

Check status:

```bash
hub marketplace subscriptions status dispute-ops-sub
```

---

## Handling Updates from Blueprint

When the publisher releases a new version:

### Check for Updates

```bash
hub marketplace subscriptions list --show-updates
```

### Apply Update (Non-Divergent)

```bash
hub marketplace subscriptions update dispute-ops-sub --apply-to dispute-triage
```

### Apply Update (Divergent Resource)

For divergent resources, you need to merge:

1. View the diff:
   ```bash
   hub diff --blueprint dispute-triage
   ```

2. Apply selectively:
   ```bash
   hub merge --from-blueprint dispute-triage --interactive
   ```

---

## Troubleshooting

### Container Clone Failed

| Issue | Resolution |
|-------|------------|
| Signature verification failed | Contact package publisher |
| Network error | Retry deployment |
| Container not found | Check package version still available |

### Deployment Failed

```bash
# Check events
hub get scenario-deployment dispute-triage-sandbox --show-events

# Check logs
hub logs operator hub-operator --tail 100
```

### Blueprint Reference Missing

If you don't see Blueprint reference:
- Resource may have been created manually (not from Blueprint)
- Upgrade from older Hub version needed

---

## Related Documentation

- [Subscribing to Packages](./subscribing-to-packages.md) — Package subscription
- [Using BlueprintSpecs](./using-blueprintspecs.md) — BlueprintSpec basics
- [Managing Blueprint Updates](./managing-blueprint-updates.md) — Handle updates
- [Scenario Development Journey](../08-personas-and-journeys/journeys/scenario-development.md) — Standard workflow

