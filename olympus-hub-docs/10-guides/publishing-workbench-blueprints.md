# Guide: Publishing Workbench Blueprints

> **Status:** 🟡 Draft
> **Audience:** Developer, Tenant Admin
> **Last Updated:** 2026-01-11

This guide walks through publishing Workbench Blueprints to the Marketplace, allowing subscribers to deploy complete workbench templates.

---

## Table of Contents

1. [Overview](#overview)
2. [Prerequisites](#prerequisites)
3. [Step 1: Prepare Your Workbench](#step-1-prepare-your-workbench)
4. [Step 2: Create Package Manifest](#step-2-create-package-manifest)
5. [Step 3: Configure Workbench Blueprint](#step-3-configure-workbench-blueprint)
6. [Step 4: Add Visibility and Metadata](#step-4-add-visibility-and-metadata)
7. [Step 5: Publish](#step-5-publish)
8. [Workbench Blueprint vs Scenario Blueprint](#workbench-blueprint-vs-scenario-blueprint)
9. [Troubleshooting](#troubleshooting)
10. [Related Documentation](#related-documentation)

---

## Overview

A **Workbench Blueprint** packages an entire workbench template, including:
- All scenarios within the workbench
- Workbench-level configurations
- Environment templates
- Knowledge structures

This is ideal for sharing complete solutions or starter templates.

---

## Prerequisites

| Requirement | Description |
|-------------|-------------|
| **Publisher Registration** | Tenant must be a registered publisher |
| **Workbench** | Complete, tested workbench |
| **Role** | Developer (for creation) + Tenant Admin (for approval) |

---

## Step 1: Prepare Your Workbench

Before publishing, ensure your workbench is complete:

| Checklist | Description |
|-----------|-------------|
| ✅ **All Scenarios Complete** | Each scenario tested and working |
| ✅ **Workbench Configuration** | Settings, policies configured |
| ✅ **Environment Templates** | Environment definitions ready |
| ✅ **No Credentials** | All secrets removed |
| ✅ **Documentation** | README for each scenario |

---

## Step 2: Create Package Manifest

```bash
hub create package-manifest payment-ops-workbench
```

Or via Marketplace Console → Package Creation.

---

## Step 3: Configure Workbench Blueprint

```yaml
apiVersion: marketplace.hub.olympus/v1
kind: PackageManifest
metadata:
  name: payment-ops-workbench
  namespace: acme-dev

spec:
  packageName: "Payment Operations Workbench"
  version: "1.0.0"
  
  shortDescription: "Complete payment operations workbench with 4 scenarios"
  longDescription: |
    A full-featured payment operations workbench including:
    - Payment Processing
    - Payment Reconciliation
    - Exception Handling
    - Fraud Detection
    
    Includes all scenarios, SOPs, knowledge structures, and 
    environment templates for quick deployment.
  
  # Package Contents - Workbench Blueprint
  blueprints:
    workbenches:
      - name: payment-operations
    # Individual scenarios included automatically
  
  # Categorization
  categories:
    - "payment-processing"
    - "banking-operations"
  industryTags:
    - "financial-services"
    - "payments"
```

### What's Included

When you include a workbench, these are automatically packaged:

| Content | Included |
|---------|----------|
| All Scenarios | ✅ |
| Hub Applications | ✅ |
| Triggers | ✅ |
| SOPs | ✅ |
| Knowledge Structures | ✅ |
| Environment Templates | ✅ |
| Workbench Policies | ✅ |

---

## Step 4: Add Visibility and Metadata

```yaml
spec:
  # Visibility
  visibility:
    mode: "public"
  
  # Additional Metadata
  deploymentInstructions: |
    After subscription:
    1. Create derived workbench from blueprint
    2. Configure environment credentials
    3. Set up machine connections
    4. Deploy scenarios
  
  systemRequirements:
    - "Rhea Runtime 2.0+"
    - "At least 2 workbench slots"
  
  prerequisites:
    - "Payment gateway machine configured"
    - "Core banking machine configured"
```

---

## Step 5: Publish

Same process as Scenario Blueprints:

```bash
# Validate
hub validate package-manifest payment-ops-workbench

# Publish
hub marketplace publish payment-ops-workbench
```

Then:
1. Admin approval
2. Security scanning
3. Catalog availability

---

## Workbench Blueprint vs Scenario Blueprint

| Aspect | Workbench Blueprint | Scenario Blueprint |
|--------|--------------------|--------------------|
| **Scope** | Complete workbench | One or more scenarios |
| **Use Case** | Full solution templates | Reusable scenario patterns |
| **Deployment** | Creates new workbench | Adds to existing workbench |
| **Size** | Larger (multiple scenarios) | Smaller (focused) |
| **Customization** | Subscriber adapts workbench | Subscriber adapts scenarios |

### When to Use Which

| Use Case | Recommendation |
|----------|----------------|
| Complete business solution | Workbench Blueprint |
| Reusable scenario pattern | Scenario Blueprint |
| Tool/Machine definitions | Scenario Blueprint with tools |
| Starter template | Workbench Blueprint |

---

## Troubleshooting

### Common Issues

| Issue | Resolution |
|-------|------------|
| Workbench not found | Verify workbench name in manifest |
| Incomplete scenarios | Complete all scenarios before publishing |
| Missing dependencies | Include required tools in package |

### Validation Errors

```bash
hub validate package-manifest payment-ops-workbench --verbose
```

---

## Related Documentation

- [Publisher Registration](./marketplace-publisher-registration.md)
- [Publishing Scenario Blueprints](./publishing-scenario-blueprints.md)
- [Package Manifest Reference](./package-manifest-reference.md)
- [Blueprints and Packages](../04-subsystems/marketplace/blueprints-and-packages.md)

