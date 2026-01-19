---
name: Content Audit and Inconsistency Fix
overview: Fix inconsistencies in Hub application development and agent development documentation based on clarifications: no namespace concept in Hub resources, workbench instance to Kubernetes namespace is n:1 mapping, all hub commands scoped to workbench instance.
todos:
  - id: audit-1
    content: Document all Hub application development content files
    status: completed
  - id: audit-2
    content: Document all Agent development content files
    status: completed
  - id: audit-3
    content: Identify namespace vs workbench instance scoping inconsistency
    status: completed
  - id: audit-4
    content: Identify remaining hub apply reference in hub-cli-setup.md
    status: completed
  - id: fix-1
    content: Remove all -n (namespace) flags from CLI command examples in agent development docs
    status: pending
  - id: fix-2
    content: Remove hub apply reference from hub-cli-setup.md
    status: pending
  - id: fix-3
    content: Remove namespace: fields from CRD examples (not a Hub concept)
    status: pending
  - id: fix-4
    content: Add clarification on workbench instance to Kubernetes namespace mapping (n:1, configured by tenant admin)
    status: pending
---

# Content Audit: Hub Application Development and Agent Development

## All Content Related to Hub Application Development and Agent Development

### Hub Application Development Content

1. **CLI Channels for Developers** (`olympus-hub-docs/06-ux-architecture/tenant-domain/cli-channels-for-developers.md`)
   - Primary CLI reference for developers
   - Covers `hubdev` and `hub` commands
   - GitOps pattern documentation
   - Scenario-based deployment
   - **Status**: ✅ Correctly shows workbench instance scoping (no `-n` flags)

2. **Hub Development Flow Guide** (`olympus-hub-docs/10-guides/hub-development-flow/`)
   - README.md - Overview and Day 1 setup
   - 01-why-different-model.md - Rationale
   - 02-two-subscription-model.md - DEV vs PROD
   - 03-workbench-based-development.md - Development model
   - 04-development-to-production-flow.md - Deployment flow
   - 05-daily-workflow.md - Daily tasks
   - 06-collaboration-patterns.md - Team collaboration
   - 07-ci-cd-integration.md - CI/CD workflows
   - 08-merits.md - Benefits
   - 09-limitations.md - Trade-offs
   - 10-best-practices.md - Best practices
   - **Status**: ✅ Consistent (no namespace references)

3. **Hub CLI Setup** (`olympus-hub-docs/10-guides/hub-cli-setup.md`)
   - Installation guide
   - Configuration instructions
   - **Status**: ❌ Contains `hub apply` reference (line 115)

4. **Hub Application Concept** (`olympus-hub-docs/02-system-design/implementation-concepts/hub-application.md`)
   - CRD definition and structure
   - Application types and runtime selection
   - **Status**: ⚠️ Contains `namespace:` field in CRD examples (line 95)

5. **Hub Application Deployment** (`olympus-hub-docs/02-system-design/implementation-concepts/hub-application-deployment.md`)
   - Deployment CRD definition
   - Lifecycle and state transitions
   - **Status**: ⚠️ Contains `namespace:` fields in CRD examples (multiple locations)

6. **Automation Development Desk** (`olympus-hub-docs/06-ux-architecture/tenant-domain/automation-development-desk.md`)
   - Web UI alternative to CLI
   - **Status**: ✅ No namespace references

### Agent Development Content

1. **Agent Development Lifecycle Guide** (`olympus-seer-docs/seer-design/guides/agent-development-lifecycle.md`)
   - Complete lifecycle walkthrough
   - Human employment analogy
   - Training and employment flow
   - **Status**: ❌ Uses `-n acme-disputes` flag extensively (19 occurrences)
   - **Status**: ⚠️ Contains `namespace:` fields in CRD examples

2. **Agent Lifecycle FAQ** (`olympus-seer-docs/seer-design/guides/agent-lifecycle-faq.md`)
   - Common questions and answers
   - CRD relationships
   - Naming conventions
   - **Status**: ❌ Uses `-n my-namespace` in examples

3. **Seer Design Guides README** (`olympus-seer-docs/seer-design/guides/README.md`)
   - Guide index and quick reference
   - **Status**: ✅ No namespace references

## Clarifications Received

1. **No namespace concept in Hub resources**: The word "namespace" is not relevant to any Hub resources and can be removed from Hub documentation.

2. **Workbench Instance to Kubernetes Namespace Mapping**: 
   - Workbench instance to Kubernetes namespace is **n:1** (one workbench instance maps to one Kubernetes namespace)
   - This mapping is configured by Tenant Admin
   - A workbench instance is tagged to a Kubernetes namespace under the tenant subscription at the time of deployment
   - This is a **one-time choice** made by Tenant Admin

3. **Hub Command Scoping**: All `hub` commands are scoped to a specific workbench instance (no `-n` flag needed).

## Identified Inconsistencies

### Critical Inconsistency 1: Namespace Flag (`-n`) in CLI Examples

**Problem**: Agent development docs use `-n` (namespace) flag, but Hub commands are scoped to workbench instance (no flag needed).

**Evidence**:
- **CLI Channels doc**: Correctly shows workbench instance scoping (no `-n` flags)
- **Agent Development Lifecycle Guide**: Uses `-n acme-disputes` in 19 places
- **Agent Lifecycle FAQ**: Uses `-n my-namespace` in examples

**Files Affected**:
- `olympus-seer-docs/seer-design/guides/agent-development-lifecycle.md` (19 instances of `-n acme-disputes`)
- `olympus-seer-docs/seer-design/guides/agent-lifecycle-faq.md` (uses `-n my-namespace`)

**Fix Required**: Remove all `-n` flags from CLI command examples. Commands are auto-scoped to workbench instance.

### Critical Inconsistency 2: Remaining `hub apply` Reference

**Problem**: `hub apply` still referenced in installation guide.

**Evidence**:
- `olympus-hub-docs/10-guides/hub-cli-setup.md` line 115: `hub apply -f my-spec.yaml`

**Fix Required**: Replace with `hub validate` or `hub sync scenario` example.

### Critical Inconsistency 3: `namespace:` Field in CRD Examples

**Problem**: CRD examples show `namespace:` field, but namespace is not a Hub concept.

**Evidence**:
- `olympus-hub-docs/02-system-design/implementation-concepts/hub-application.md` line 95: `namespace: acme-bank`
- `olympus-hub-docs/02-system-design/implementation-concepts/hub-application-deployment.md` (multiple `namespace:` fields)
- `olympus-seer-docs/seer-design/guides/agent-development-lifecycle.md` (CRD examples with `namespace:`)

**Fix Required**: Remove `namespace:` fields from all Hub CRD examples. If Kubernetes namespace is needed for implementation, it should be handled by the platform (mapped from workbench instance), not specified in Hub CRDs.

## Implementation Plan

### Fix 1: Remove `-n` Flags from Agent Development Docs

**File**: `olympus-seer-docs/seer-design/guides/agent-development-lifecycle.md`

**Changes**:
- Remove `-n acme-disputes` from all CLI command examples (19 instances)
- Update examples to show workbench instance scoping (commands auto-scoped)

**Examples to Fix**:
```bash
# Before:
hub get scenario-normative routine-dispute-triage -n acme-disputes
hub sync scenario routine-dispute-triage-sandbox -n acme-disputes
hub logs agent dispute-triage-emp-001 -n acme-disputes --follow

# After:
hub get scenario-normative routine-dispute-triage
hub sync scenario routine-dispute-triage-sandbox
hub logs agent dispute-triage-emp-001 --follow
```

**File**: `olympus-seer-docs/seer-design/guides/agent-lifecycle-faq.md`

**Changes**:
- Remove `-n my-namespace` from CLI command examples
- Update examples to show workbench instance scoping

**Examples to Fix**:
```bash
# Before:
hub sync scenario my-scenario-sandbox -n my-namespace
hub logs agent my-agent-emp-001 -n my-namespace --follow

# After:
hub sync scenario my-scenario-sandbox
hub logs agent my-agent-emp-001 --follow
```

### Fix 2: Remove `hub apply` from Installation Guide

**File**: `olympus-hub-docs/10-guides/hub-cli-setup.md`

**Changes**:
- Line 115: Replace `hub apply -f my-spec.yaml` with appropriate command

**Fix**:
```bash
# Before:
hub apply -f my-spec.yaml      # Apply resources

# After:
hub validate -f my-spec.yaml   # Validate resources
# Or:
hub sync scenario my-scenario   # Deploy scenario (after committing to Git)
```

### Fix 3: Remove `namespace:` Fields from CRD Examples

**Files to Update**:

1. **`olympus-hub-docs/02-system-design/implementation-concepts/hub-application.md`**
   - Line 95: Remove `namespace: acme-bank` from HubApplicationSpec example
   - Add note explaining that Kubernetes namespace mapping is handled by platform

2. **`olympus-hub-docs/02-system-design/implementation-concepts/hub-application-deployment.md`**
   - Remove all `namespace:` fields from CRD examples
   - Update references to namespace in spec fields (e.g., `applicationSpecRef.namespace`, `scenarioDeploymentRef.namespace`)
   - Add clarification about workbench instance to Kubernetes namespace mapping

3. **`olympus-seer-docs/seer-design/guides/agent-development-lifecycle.md`**
   - Remove `namespace:` fields from all CRD examples
   - Update any references to namespace in CRD structures

**Note**: If CRDs need to reference resources in other workbenches, use workbench instance references instead of namespace.

### Fix 4: Add Workbench Instance to Kubernetes Namespace Mapping Clarification

**Where to Add**:
- CLI Channels doc: Add section explaining workbench instance scoping and Kubernetes namespace mapping
- Hub Application Deployment doc: Add note about Kubernetes namespace mapping
- Agent Development Lifecycle Guide: Add note in prerequisites or getting started section

**Content to Add**:

```markdown
## Workbench Instance and Kubernetes Namespace Mapping

**Important**: Hub resources do not use "namespace" as a concept. All `hub` commands are scoped to a **workbench instance**.

**Kubernetes Namespace Mapping**:
- Each workbench instance is mapped to exactly one Kubernetes namespace (n:1 relationship)
- This mapping is configured by the Tenant Admin at workbench instance creation time
- The mapping is a one-time choice and cannot be changed after deployment
- Developers do not need to specify namespace—commands are automatically scoped to the workbench instance

**Example**:
- Workbench Instance: `acme-disputes-sandbox`
- Mapped to Kubernetes Namespace: `acme-disputes-sandbox-ns` (configured by Tenant Admin)
- CLI Command: `hub sync scenario my-scenario` (no `-n` flag needed)
```

## Files to Update

### Priority 1: Critical Fixes

1. ✅ `olympus-seer-docs/seer-design/guides/agent-development-lifecycle.md`
   - Remove all `-n` flags (19 instances)
   - Remove `namespace:` fields from CRD examples

2. ✅ `olympus-seer-docs/seer-design/guides/agent-lifecycle-faq.md`
   - Remove `-n` flags from examples

3. ✅ `olympus-hub-docs/10-guides/hub-cli-setup.md`
   - Remove `hub apply` reference

### Priority 2: CRD Examples

4. ✅ `olympus-hub-docs/02-system-design/implementation-concepts/hub-application.md`
   - Remove `namespace:` field from CRD example
   - Add note about Kubernetes namespace mapping

5. ✅ `olympus-hub-docs/02-system-design/implementation-concepts/hub-application-deployment.md`
   - Remove `namespace:` fields from CRD examples
   - Update spec references (may need to use workbench instance references instead)
   - Add clarification about Kubernetes namespace mapping

### Priority 3: Documentation Clarifications

6. ✅ `olympus-hub-docs/06-ux-architecture/tenant-domain/cli-channels-for-developers.md`
   - Add section explaining workbench instance to Kubernetes namespace mapping (if not already clear)

## Verification Checklist

After fixes:
- [ ] All `-n` flags removed from CLI command examples
- [ ] All `namespace:` fields removed from Hub CRD examples
- [ ] `hub apply` reference removed from hub-cli-setup.md
- [ ] Workbench instance scoping clearly explained
- [ ] Kubernetes namespace mapping (n:1) documented
- [ ] All workflow examples show: edit → commit → push → sync scenario
- [ ] All examples use `hub sync scenario` (not `hub apply`)
- [ ] GitOps pattern consistently explained
- [ ] Workbench instance model consistently explained
