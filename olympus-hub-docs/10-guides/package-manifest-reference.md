# Package Manifest Reference

> **Status:** 🟡 Draft
> **Audience:** Developer
> **Last Updated:** 2026-01-11

Complete reference for the Package Manifest CRD used to define Marketplace packages.

---

## Overview

The Package Manifest CRD defines what's included in a Marketplace package and how it should be presented in the catalog.

---

## CRD Structure

```yaml
apiVersion: marketplace.hub.olympus/v1
kind: PackageManifest
metadata:
  name: <manifest-name>
  namespace: <workbench-namespace>

spec:
  # Required Fields
  packageName: <string>
  version: <semver>
  shortDescription: <string>
  blueprints: <object>
  
  # Optional Fields
  longDescription: <string>
  categories: [<string>]
  industryTags: [<string>]
  keywords: [<string>]
  visibility: <object>
  deploymentInstructions: <string>
  systemRequirements: [<string>]
  prerequisites: [<string>]
  documentationUri: <uri>
  supportInfo: <object>
```

---

## Required Fields

### packageName

Display name for the package in the catalog.

```yaml
packageName: "Dispute Operations Suite"
```

| Attribute | Value |
|-----------|-------|
| **Type** | string |
| **Length** | 3-100 characters |
| **Allowed** | Alphanumeric, spaces, hyphens |

### version

Semantic version of the package.

```yaml
version: "1.2.3"
```

| Attribute | Value |
|-----------|-------|
| **Type** | string |
| **Format** | SemVer (MAJOR.MINOR.PATCH) |
| **Pre-release** | Supported (e.g., "1.0.0-beta.1") |

### shortDescription

Brief description shown in search results.

```yaml
shortDescription: "Complete dispute resolution automation with AI-powered triage"
```

| Attribute | Value |
|-----------|-------|
| **Type** | string |
| **Length** | 10-200 characters |

### blueprints

Contents of the package.

```yaml
blueprints:
  scenarios:
    - name: dispute-triage
    - name: dispute-resolution
  workbenches:
    - name: payment-operations
  tools:
    - name: card-network-lookup
  machines:
    - name: core-banking-adapter
  rawAgents:
    - name: document-analyzer
```

| Field | Description |
|-------|-------------|
| `scenarios` | List of scenario names |
| `workbenches` | List of workbench names |
| `tools` | List of standalone tool names |
| `machines` | List of machine definition names |
| `rawAgents` | List of raw agent names |

---

## Optional Fields

### longDescription

Detailed description with markdown support.

```yaml
longDescription: |
  # Dispute Operations Suite
  
  This package includes two complete scenarios for dispute resolution:
  
  ## Included Scenarios
  - **Dispute Triage**: AI-powered initial assessment
  - **Dispute Resolution**: End-to-end resolution workflow
  
  ## Features
  - Pre-trained agents
  - Complete SOPs
  - Tool integrations
```

### categories

Classification tags for browsing.

```yaml
categories:
  - "dispute-resolution"
  - "customer-service"
  - "fraud-detection"
```

### industryTags

Industry-specific tags.

```yaml
industryTags:
  - "financial-services"
  - "banking"
  - "insurance"
```

### keywords

Search optimization keywords.

```yaml
keywords:
  - "disputes"
  - "chargebacks"
  - "card-not-present"
  - "fraud"
```

### visibility

Access controls for the package.

```yaml
visibility:
  mode: "public"  # public | restricted | private
  
  # For restricted/private mode
  tenantAllowList:
    - "tenant-partner-bank"
    - "tenant-subsidiary"
  
  # Block specific tenants (public mode)
  tenantDisallowList:
    - "tenant-competitor"
  
  # Regional restrictions
  regionAllowList:
    - "us-east-1"
    - "eu-west-1"
  
  regionDisallowList:
    - "cn-north-1"
```

### deploymentInstructions

Post-subscription deployment guidance.

```yaml
deploymentInstructions: |
  After subscribing to this package:
  
  1. Create derived resources from BlueprintSpecs
  2. Configure environment credentials
  3. Set up machine connections
  4. Deploy scenarios to your workbench
```

### systemRequirements

Platform requirements.

```yaml
systemRequirements:
  - "Rhea Runtime 2.0+"
  - "OpenAI-compatible LLM access"
  - "At least 2 workbench slots available"
```

### prerequisites

Dependencies not included in package.

```yaml
prerequisites:
  - "Card network machine configured"
  - "Core banking machine configured"
  - "Email notification channel enabled"
```

### documentationUri

Link to external documentation.

```yaml
documentationUri: "https://docs.acme.com/dispute-ops"
```

### supportInfo

Publisher support information.

```yaml
supportInfo:
  email: "support@acme.com"
  website: "https://support.acme.com"
  slackChannel: "#dispute-ops-support"
```

---

## Complete Example

```yaml
apiVersion: marketplace.hub.olympus/v1
kind: PackageManifest
metadata:
  name: dispute-ops-package
  namespace: acme-dev

spec:
  # Identity
  packageName: "Dispute Operations Suite"
  version: "1.2.0"
  
  # Descriptions
  shortDescription: "Complete dispute resolution automation with AI-powered triage"
  longDescription: |
    # Dispute Operations Suite
    
    Comprehensive dispute resolution suite including:
    - **Dispute Triage**: AI-powered initial assessment and categorization
    - **Dispute Resolution**: End-to-end resolution workflow
    
    ## Key Features
    - Pre-trained AI agents for dispute analysis
    - Complete SOPs for regulatory compliance
    - Integration with major card networks
    - Escalation and notification workflows
    
    ## What's Included
    - 2 complete scenarios
    - 5 trained agents
    - 8 SOPs
    - Card network lookup tool
  
  # Contents
  blueprints:
    scenarios:
      - name: dispute-triage
      - name: dispute-resolution
    tools:
      - name: card-network-lookup
  
  # Visibility
  visibility:
    mode: "public"
    regionDisallowList:
      - "cn-north-1"
  
  # Categorization
  categories:
    - "dispute-resolution"
    - "customer-service"
  industryTags:
    - "financial-services"
    - "banking"
  keywords:
    - "disputes"
    - "chargebacks"
    - "card-not-present"
    - "fraud"
  
  # Deployment
  deploymentInstructions: |
    After subscribing:
    1. Create derived ScenarioNormativeSpecs from BlueprintSpecs
    2. Configure your environment credentials
    3. Set up card network machine connection
    4. Deploy scenarios to your workbench
  
  systemRequirements:
    - "Rhea Runtime 2.0+"
    - "OpenAI-compatible LLM access"
  
  prerequisites:
    - "Card network machine configured"
    - "Email notification channel enabled"
  
  # Documentation
  documentationUri: "https://docs.acme.com/dispute-ops"
  
  # Support
  supportInfo:
    email: "marketplace-support@acme.com"
    website: "https://support.acme.com/hub-packages"
```

---

## Validation

Validate your manifest before publishing:

```bash
hub validate package-manifest dispute-ops-package --verbose
```

### Common Validation Errors

| Error | Resolution |
|-------|------------|
| `missing required field: packageName` | Add packageName field |
| `invalid version format` | Use SemVer format (X.Y.Z) |
| `shortDescription too long` | Keep under 200 characters |
| `blueprint not found: scenario/xyz` | Verify scenario exists in workbench |
| `credentials detected` | Remove secrets from contents |

---

## Related Documentation

- [Publishing Scenario Blueprints](./publishing-scenario-blueprints.md)
- [Publishing Workbench Blueprints](./publishing-workbench-blueprints.md)
- [Blueprints and Packages](../04-subsystems/marketplace/blueprints-and-packages.md)
- [Publishing Services](../04-subsystems/marketplace/publishing-services.md)

