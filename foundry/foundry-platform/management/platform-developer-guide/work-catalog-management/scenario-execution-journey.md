# Scenario Execution Journey

This document walks through the complete lifecycle of a Scenario from authoring to execution, demonstrating how Work Catalog Management coordinates with other services in the context of the full Work Catalog hierarchy.

## Overview

A Scenario flows through the system from definition to execution:

```
Authored → PR Validated → Merged → Synced to Registry → OI Workflow References → WO Created → Resolved → Agent Recommended → Executed
```

The journey involves multiple modules:
- **Work Catalog Management** — Schema, validation, resolution, recommendations
- **Validation module** — PR gating for catalogs at each level
- **Work Catalog Sync Service** — Config propagation to registry
- **Metadata Service** — Storage and queries
- **Orchestrator** — OI Workflow execution, WO creation
- **WO Runtime** — Scenario resolution and execution

## The Journey

### Phase 1: Scenario Authoring

**Location:** Work Catalog Repository (at appropriate hierarchy level)  
**Actor:** Admin or Developer

#### Step 1.1: Choose Catalog Level

The author decides where to define the Scenario based on intended scope:

| Level | When to Use | Who Can Author |
|-------|-------------|----------------|
| Platform | Universal defaults for all Foundries | Platform team |
| Foundry | Foundry-wide standards | Foundry Admin |
| Workshop | Workshop-specific variations | Workshop Admin |
| Workbench | Team-specific customizations | Workbench Admin |
| User | Personal experiments | Developer |

For this example, a Workbench Admin creates a custom `implement-feature` scenario for the `checkout` team.

#### Step 1.2: Create Scenario File

The admin creates the scenario in the Workshop Definition Repo (Workbench section):

```
workshop-ecommerce/
└── workbenches/
    └── checkout/
        └── work-catalog/
            └── build/
                └── product-intent/
                    └── development/
                        └── scenarios/
                            └── implement-feature.yaml  # New file
```

#### Step 1.3: Write Scenario YAML

Following the [scenario schema](scenario-schema.md), including the `scope` field:

```yaml
apiVersion: foundry/v1
kind: Scenario
metadata:
  name: implement-feature
  workspace: development
  scope: workspace-ingress         # Can be invoked by Orchestrator
  labels:
    track: build
    category: implementation
spec:
  description: "Implement a feature from Product Specification (checkout team variant)"
  
  triggers:
    - manual
    - orchestrator: psd-approved   # Allowed because scope is workspace-ingress
  
  inputs:
    - name: psdRef
      type: reference
      required: true
  
  outputs:
    - name: pullRequest
      type: reference
  
  tasks:
    - name: analyze-requirements
      type: agent
      skills:
        - requirements-analysis
    - name: implement-code
      type: agent
      skills:
        - code-implementation
        - test-writing
        - checkout-domain-knowledge   # Team-specific skill
      dependencies:
        - analyze-requirements
  
  skilled_agent:
    ref: sa-checkout-dev             # Team-specific Skilled Agent
    fallback: auto
```

#### Step 1.4: Create Pull Request

```bash
git add workbenches/checkout/work-catalog/build/product-intent/development/scenarios/implement-feature.yaml
git commit -m "Add checkout-specific implement-feature scenario"
git push origin feature/checkout-implement-scenario
# Creates PR #42
```

---

### Phase 2: PR Validation

**Location:** GitHub / Validation module  
**Actor:** Validation module (automated)

#### Step 2.1: PR Check Triggered

GitHub webhook notifies the Validation module:

```json
{
  "action": "opened",
  "pull_request": {
    "number": 42,
    "head": { "sha": "abc123" }
  },
  "repository": {
    "full_name": "acme/ecommerce-workshop-definition"
  }
}
```

#### Step 2.2: Identify Changed Files

The Validation module identifies work catalog files:

```
Changed files:
  + workbenches/checkout/work-catalog/build/product-intent/development/scenarios/implement-feature.yaml
```

#### Step 2.3: Validate Scenario

The Validation module calls Work Catalog Management:

```
POST /api/v1/work-catalog/validate
Content-Type: application/json
{
  "type": "scenario",
  "yaml": "apiVersion: foundry/v1\nkind: Scenario\n...",
  "context": {
    "foundry_id": "acme",
    "workshop_id": "ecommerce",
    "workbench_id": "checkout"
  }
}
```

Work Catalog Management validates:

```
┌─────────────────────────────────────────────────────────────────────┐
│  Work Catalog Management Validation                                  │
│                                                                      │
│  1. Parse YAML ──────────────────────────────────────────── ✓ Valid │
│  2. Check API version ───────────────────────────────────── ✓ v1    │
│  3. Validate against Scenario schema ────────────────────── ✓ Pass  │
│  4. Check scope field ───────────────────────────────────── ✓ workspace-ingress │
│  5. Validate scope/trigger compatibility:                           │
│     • orchestrator trigger with workspace-ingress ───────── ✓ Valid │
│  6. Check skill references:                                         │
│     • requirements-analysis ─────────────────────────────── ✓ Exists│
│     • code-implementation ───────────────────────────────── ✓ Exists│
│     • test-writing ──────────────────────────────────────── ✓ Exists│
│     • checkout-domain-knowledge ─────────────────────────── ✓ Exists│
│  7. Check Skilled Agent reference:                                  │
│     • sa-checkout-dev ───────────────────────────────────── ✓ Exists│
│  8. Check task dependencies (no cycles) ─────────────────── ✓ Pass  │
│                                                                      │
│  Result: Valid                                                       │
└─────────────────────────────────────────────────────────────────────┘
```

Response:

```json
{
  "valid": true,
  "errors": [],
  "warnings": [
    "Optional field 'guardrails' not specified - using workspace defaults"
  ]
}
```

#### Step 2.4: Report Check Status

The Validation module reports to GitHub:

```
POST /repos/acme/ecommerce-workshop-definition/check-runs
{
  "name": "foundry-validation",
  "head_sha": "abc123",
  "status": "completed",
  "conclusion": "success",
  "output": {
    "title": "Work Catalog validation passed",
    "summary": "1 scenario validated successfully"
  }
}
```

#### Step 2.5: Merge PR

With checks passing, the PR is merged:

```
PUT /repos/acme/ecommerce-workshop-definition/pulls/42/merge
{
  "merge_method": "squash"
}
```

---

### Phase 3: Sync to Metadata Service

**Location:** Work Catalog Sync Service  
**Actor:** Work Catalog Sync Service (automated)

#### Step 3.1: Receive Webhook

GitHub sends push webhook after merge:

```json
{
  "ref": "refs/heads/main",
  "after": "def456",
  "commits": [{
    "added": ["workbenches/checkout/work-catalog/build/product-intent/development/scenarios/implement-feature.yaml"]
  }]
}
```

#### Step 3.2: Process Changed Files

Sync Service processes work catalog files:

```python
for file in commit.added + commit.modified:
    if is_scenario_file(file):
        content = fetch_file_content(repo, file, commit_sha)
        scenario = parse_scenario(content)
        
        # Determine hierarchy level from path
        catalog_level = determine_catalog_level(file)  # "workbench"
        
        metadata_service.upsert_scenario(
            catalog_level="workbench",
            foundry_id="acme",
            workshop_id="ecommerce",
            workbench_id="checkout",
            workspace_type=scenario.metadata.workspace,
            name=scenario.metadata.name,
            scope=scenario.metadata.scope,
            spec=scenario.spec,
            source={
                "repository": repo.full_name,
                "path": file.path,
                "commit_sha": commit_sha
            }
        )
```

#### Step 3.3: Store in Registry

Scenario is stored with full hierarchy context:

```json
{
  "id": "scenario-uuid-123",
  "name": "implement-feature",
  "workspace_type": "development",
  "scope": "workspace-ingress",
  "api_version": "foundry/v1",
  "spec": { ... },
  "catalog_level": "workbench",
  "foundry_id": "acme",
  "workshop_id": "ecommerce",
  "workbench_id": "checkout",
  "user_id": null,
  "source_repository": "acme/ecommerce-workshop-definition",
  "source_path": "workbenches/checkout/work-catalog/build/product-intent/development/scenarios/implement-feature.yaml",
  "source_commit_sha": "def456",
  "synced_at": "2026-05-28T10:30:00Z"
}
```

#### Step 3.4: Publish Event and Invalidate Caches

```python
# Publish to Atropos: /{foundry-id}/foundry.management.scenario-created
await publish_event(
    event_type="scenario-created",
    foundry_id="acme",
    workshop_id="ecommerce",
    workbench_id="checkout",
    data={
        "name": "implement-feature",
        "workspace": "development",
        "scope": "workspace-ingress",
        "catalog_level": "workbench"
    }
)

# Invalidate affected caches
await cache.invalidate_pattern("effective-catalog:acme:ecommerce:checkout:*")
await cache.invalidate_pattern("resolve:scenario:implement-feature:acme:ecommerce:checkout:*")
```

---

### Phase 4: OI Workflow References Scenario

**Location:** Work Catalog (OI Workflow definition)  
**Context:** The OI Workflow at Foundry level already references `implement-feature`

The Product Intent workflow (defined at Foundry level) includes:

```yaml
# work-catalog/build/product-intent/workflow.yaml (at Foundry level)
stages:
  - name: ready-for-development
    handlers:
      - when:
          event: release-intent-milestone-reached
          params:
            milestone: development-start
        then:
          - action: create-work-order
            params:
              wo-label: dev-wo
              workspace: development
              scenario: implement-feature  # Resolved from effective catalog
```

When validating this OI Workflow, Work Catalog Management:
1. Resolves `implement-feature` from the effective catalog at the workflow's scope
2. Verifies the resolved scenario has `scope: workspace-ingress`
3. Verifies workspace match (`development`)

---

### Phase 5: Work Order Creation

**Location:** Orchestrator  
**Actor:** Orchestrator Workflow Engine

#### Step 5.1: OI Workflow Triggers WO

When a Product Intent reaches the `ready-for-development` stage:

```
Orchestrator receives: release-intent-milestone-reached (development-start)
PI: PI-456
Workbench: checkout
```

#### Step 5.2: Resolve Effective Scenario

Before creating the WO, Orchestrator resolves the scenario:

```
GET /api/v1/work-catalog/resolve
  ?type=scenario
  &name=implement-feature
  &foundry_id=acme
  &workshop_id=ecommerce
  &workbench_id=checkout
```

Resolution walks the hierarchy:

```
┌─────────────────────────────────────────────────────────────────────┐
│  Effective Scenario Resolution                                       │
│                                                                      │
│  1. Check User level ──────────────────────────── Not active        │
│  2. Check Workbench level (checkout/development):                   │
│     └── Found: implement-feature.yaml ──────────── ✓ Use           │
│                                                                      │
│  (Workbench version overrides Workshop/Foundry/Platform)            │
│                                                                      │
│  Result: Workbench scenario (checkout-specific version)             │
└─────────────────────────────────────────────────────────────────────┘
```

#### Step 5.3: Verify Scope

Orchestrator confirms `scope: workspace-ingress`:

```
Scenario: implement-feature
Scope: workspace-ingress ✓
Can be invoked by Orchestrator
```

#### Step 5.4: Create Work Order

Orchestrator creates the Work Order in Jira:

```json
{
  "project": "CHECKOUT-WO",
  "issueType": "Work Order",
  "summary": "Implement: Add user preferences panel",
  "customFields": {
    "foundry-scenario": "implement-feature",
    "foundry-scenario-source": "workbench:checkout",
    "foundry-workspace": "development",
    "foundry-workbench": "checkout",
    "foundry-orchestration-item": "PI-456",
    "foundry-wo-label": "dev-wo"
  }
}
```

---

### Phase 6: Scenario Resolution at Execution

**Location:** WO Runtime (in Workspace Session)  
**Actor:** WO Runtime Daemon

#### Step 6.1: WO Assigned to Session

Developer Alice's Workspace Session receives the WO:

```
Jira Poll: WO-789 assigned to alice@acme.com
Scenario: implement-feature
Workspace: development
Workbench: checkout
```

#### Step 6.2: Check User Catalog Activation

WO Runtime checks if Alice has her personal catalog active:

```
GET /api/v1/sessions/{session_id}/user-catalog
Response: { "active": false, "source": "profile" }
```

Alice hasn't activated her user catalog, so user level is skipped.

#### Step 6.3: Resolve Effective Scenario

WO Runtime queries for the effective scenario:

```
GET /api/v1/work-catalog/resolve
  ?type=scenario
  &name=implement-feature
  &foundry_id=acme
  &workshop_id=ecommerce
  &workbench_id=checkout
  &user_id=alice
```

Since user catalog is not active, resolution returns the Workbench version:

```json
{
  "artifact": {
    "name": "implement-feature",
    "metadata": {
      "workspace": "development",
      "scope": "workspace-ingress"
    },
    "spec": { ... }
  },
  "source": {
    "level": "workbench",
    "id": "checkout",
    "repository": "acme/ecommerce-workshop-definition",
    "path": "workbenches/checkout/work-catalog/build/product-intent/development/scenarios/implement-feature.yaml",
    "commit_sha": "def456"
  }
}
```

---

### Phase 7: Agent Recommendation

**Location:** Work Catalog Management / WO Runtime  
**Actor:** WO Runtime Daemon

#### Step 7.1: Request Recommendations

Since `fallback: auto` is set, WO Runtime asks for recommendations:

```
GET /api/v1/scenarios/scenario-uuid-123/recommendations?workspace_id=checkout-dev
```

#### Step 7.2: Score Available Agents

Work Catalog Management evaluates Skilled Agents:

```
┌─────────────────────────────────────────────────────────────────────┐
│  Agent Recommendation Scoring                                        │
│                                                                      │
│  Required skills: requirements-analysis, code-implementation,        │
│                   test-writing, checkout-domain-knowledge            │
│                                                                      │
│  Candidate: sa-checkout-dev (preferred in scenario)                  │
│    Skills: requirements-analysis ✓, code-implementation ✓,          │
│            test-writing ✓, checkout-domain-knowledge ✓              │
│    Coverage: 100%                                                    │
│    Workspace: development ✓                                          │
│    Score: 0.98                                                       │
│                                                                      │
│  Candidate: sa-full-stack-dev                                        │
│    Skills: requirements-analysis ✓, code-implementation ✓,          │
│            test-writing ✓                                           │
│    Missing: checkout-domain-knowledge                                │
│    Coverage: 75%                                                     │
│    Workspace: development ✓                                          │
│    Score: 0.72                                                       │
│                                                                      │
│  Recommendation: sa-checkout-dev (0.98)                             │
└─────────────────────────────────────────────────────────────────────┘
```

---

### Phase 8: Agent Execution

**Location:** Workspace Session  
**Actor:** WO Runtime + Employed Agent

#### Step 8.1: Spawn Agent

WO Runtime spawns the recommended agent:

```
Selected: sa-checkout-dev
Capable Agent: cursor-agent
Model: claude-opus

Harness prepared:
  - Environment: FOUNDRY_SCENARIO=implement-feature, FOUNDRY_TASK_KEY=TASK-890
  - Skills: requirements-analysis@1.2.0, code-implementation@2.1.0, 
            test-writing@1.5.0, checkout-domain-knowledge@1.0.0
  - Context: PI-456 product specification, checkout-specific conventions
  - Delegation Token: <jwt>
```

#### Step 8.2: Execute Tasks

Agent executes tasks per scenario definition:

```
Task 1: analyze-requirements
  └── Reads PSD reference
  └── Creates implementation plan (using checkout domain knowledge)
  └── Marks complete

Task 2: implement-code (depends on Task 1)
  └── Reads implementation plan
  └── Writes code following checkout conventions
  └── Writes tests
  └── Creates PR
  └── Marks complete
```

#### Step 8.3: WO Completion

When all tasks complete:

```
WO-789: All tasks complete
  └── WO Runtime notifies Orchestrator
  └── Orchestrator advances PI-456 workflow
```

---

## Alternative: User Catalog Active

If Alice had activated her personal Work Catalog, the resolution would include her customizations:

```
Alice activates user catalog:
POST /api/v1/sessions/{session_id}/user-catalog
Body: { "action": "activate" }

Alice has custom implement-feature in her user catalog.

Resolution now returns:
{
  "source": {
    "level": "user",
    "id": "alice"
  }
}
```

This allows Alice to experiment with scenario changes without affecting other team members.

---

## Summary

| Phase | Location | Actor | Key Output |
|-------|----------|-------|------------|
| 1. Authoring | Work Catalog Repo | Admin | Scenario YAML file |
| 2. Validation | Validation module | Automated | PR check status (schema + scope) |
| 3. Sync | Sync Service | Automated | Scenario in registry with hierarchy |
| 4. OI Reference | OI Workflow | Orchestrator | Validated scenario reference |
| 5. WO Creation | Orchestrator | Workflow Engine | Work Order with resolved scenario |
| 6. Resolution | WO Runtime | Daemon | Effective scenario (hierarchy walk) |
| 7. Recommendation | Work Catalog Mgmt | API | Ranked agent list |
| 8. Execution | Workspace Session | Agent | Task outputs |

## Key Integration Points

```
┌──────────────────┐     ┌──────────────────┐     ┌──────────────────┐
│   Work Catalog   │────▶│   Validation     │────▶│    Metadata      │
│      Repos       │ PR  │     module       │sync │    Service       │
│  (5 levels)      │     │    + Sync        │     │   (registry)     │
└──────────────────┘     └──────────────────┘     └──────────────────┘
                                │                         │
                         calls  │                         │ queries
                                ▼                         ▼
                         ┌──────────────────┐     ┌──────────────────┐
                         │   Work Catalog   │◀────│  Orchestrator    │
                         │   Management     │     │  + WO Runtime    │
                         │  (resolution)    │     │                  │
                         └──────────────────┘     └──────────────────┘
```

## Read Next

- [README.md](README.md) — Work Catalog Management overview
- [resolution-algorithm.md](resolution-algorithm.md) — Hierarchy resolution details
- [scenario-schema.md](scenario-schema.md) — Full YAML schema
- [validation-rules.md](validation-rules.md) — Validation specification
- [../../orchestrator/README.md](../../../orchestrator/README.md) — How Orchestrator uses OI Workflows
- [../../work-order-runtime/README.md](../../../work-order-runtime/README.md) — WO execution details
