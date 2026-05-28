# Scenario Execution Journey

This document walks through the complete lifecycle of a Scenario from authoring to execution, demonstrating how Scenario Management coordinates with other services.

## Overview

A Scenario flows through the system from definition to execution:

```
Authored → PR Validated → Merged → Synced to Metadata → WO Created → Resolved → Agent Recommended → Executed
```

The journey involves multiple modules:
- **Scenario Management** — Schema, validation, recommendations
- **Workshop Validation Service** — PR gating
- **Workshop Sync Service** — Config propagation
- **Metadata Service** — Storage and queries
- **Orchestrator** — WO creation
- **WO Runtime** — Scenario resolution and execution

## The Journey

### Phase 1: Scenario Authoring

**Location:** Workshop Definition Repository  
**Actor:** Workshop or Workbench Admin

#### Step 1.1: Create Scenario File

The admin creates a new scenario definition in the Workshop Definition Repo:

```
workshop-definition-repo/
└── workbenches/
    └── checkout/
        └── workspaces/
            └── development/
                └── scenarios/
                    └── implement-feature.yaml  # New file
```

#### Step 1.2: Write Scenario YAML

Following the [scenario schema](scenario-schema.md):

```yaml
apiVersion: foundry/v1
kind: Scenario
metadata:
  name: implement-feature
  workspace: development
  labels:
    track: build
    category: implementation
spec:
  description: "Implement a feature from Product Specification"
  
  triggers:
    - manual
    - orchestrator: psd-approved
  
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
      dependencies:
        - analyze-requirements
  
  skilled_agent:
    ref: sa-full-stack-dev
    fallback: auto
```

#### Step 1.3: Create Pull Request

The admin commits and pushes:

```bash
git add scenarios/implement-feature.yaml
git commit -m "Add implement-feature scenario for Development workspace"
git push origin feature/add-implement-scenario
# Creates PR #42
```

---

### Phase 2: PR Validation

**Location:** GitHub / Workshop Validation Service  
**Actor:** Workshop Validation Service (automated)

#### Step 2.1: PR Check Triggered

GitHub webhook notifies Workshop Validation Service:

```json
{
  "action": "opened",
  "pull_request": {
    "number": 42,
    "head": { "sha": "abc123" }
  },
  "repository": {
    "full_name": "acme/workshop-definition"
  }
}
```

#### Step 2.2: Identify Changed Files

Workshop Validation Service fetches the PR diff:

```
Changed files:
  + workbenches/checkout/workspaces/development/scenarios/implement-feature.yaml
```

#### Step 2.3: Validate Scenario

For each changed scenario file, Workshop Validation calls Scenario Management:

```
POST /api/v1/scenarios/validate
Content-Type: application/json
{
  "scenario_yaml": "apiVersion: foundry/v1\nkind: Scenario\n...",
  "api_version": "foundry/v1"
}
```

Scenario Management validates:

```
┌─────────────────────────────────────────────────────────────────┐
│  Scenario Management Validation                                  │
│                                                                  │
│  1. Parse YAML ─────────────────────────────────────── ✓ Valid  │
│  2. Check API version ──────────────────────────────── ✓ v1     │
│  3. Validate against schema ────────────────────────── ✓ Pass   │
│  4. Check skill references:                                      │
│     • requirements-analysis ────────────────────────── ✓ Exists │
│     • code-implementation ──────────────────────────── ✓ Exists │
│     • test-writing ─────────────────────────────────── ✓ Exists │
│  5. Check Skilled Agent reference:                               │
│     • sa-full-stack-dev ────────────────────────────── ✓ Exists │
│  6. Check task dependencies (no cycles) ────────────── ✓ Pass   │
│                                                                  │
│  Result: Valid                                                   │
└─────────────────────────────────────────────────────────────────┘
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

Workshop Validation Service reports to GitHub:

```
POST /repos/acme/workshop-definition/check-runs
{
  "name": "foundry-workshop-validation",
  "head_sha": "abc123",
  "status": "completed",
  "conclusion": "success",
  "output": {
    "title": "Scenario validation passed",
    "summary": "1 scenario validated successfully"
  }
}
```

#### Step 2.5: Merge PR

With checks passing, Workshop Validation Service merges the PR:

```
PUT /repos/acme/workshop-definition/pulls/42/merge
{
  "merge_method": "squash"
}
```

---

### Phase 3: Sync to Metadata Service

**Location:** Workshop Sync Service  
**Actor:** Workshop Sync Service (automated)

#### Step 3.1: Receive Webhook

GitHub sends push webhook after merge:

```json
{
  "ref": "refs/heads/main",
  "after": "def456",
  "commits": [{
    "added": ["workbenches/checkout/workspaces/development/scenarios/implement-feature.yaml"]
  }]
}
```

#### Step 3.2: Process Changed Files

Workshop Sync Service processes each changed file:

```python
for file in commit.added + commit.modified:
    if is_scenario_file(file):
        content = fetch_file_content(repo, file, commit_sha)
        scenario = parse_scenario(content)
        metadata_service.upsert_scenario(
            scope="workbench",
            scope_id=extract_workbench_id(file),
            workspace=extract_workspace(file),
            scenario=scenario
        )
```

#### Step 3.3: Store in Metadata Service

Scenario is stored with full context:

```json
{
  "id": "scenario-uuid-123",
  "scope": "workbench",
  "scope_id": "checkout",
  "workspace_type": "development",
  "name": "implement-feature",
  "api_version": "foundry/v1",
  "spec": { ... },
  "source_file": "workbenches/checkout/workspaces/development/scenarios/implement-feature.yaml",
  "commit_sha": "def456",
  "synced_at": "2026-05-28T10:30:00Z"
}
```

#### Step 3.4: Invalidate Caches

Scenario Management caches are invalidated:

```
Cache invalidations:
  - scenario:checkout:development:implement-feature
  - recommendations:checkout:development
```

---

### Phase 4: Work Order Creation

**Location:** Orchestrator  
**Actor:** Orchestrator Workflow Engine

#### Step 4.1: Workflow Triggers WO

When a PI is approved (per workflow definition):

```yaml
# pi-workflow.yaml
stages:
  - name: specification-approved
    handlers:
      - when:
          event: governance-verdict
          params:
            scenario: product-specification-review
            verdict: approved
        then:
          - action: transition-orchestration-item
            params:
              target-stage: ready-for-development
          - action: create-work-order
            params:
              wo-label: dev-wo
              workspace: development
              scenario: implement-feature  # ← References our scenario
```

#### Step 4.2: Orchestrator Creates WO

Orchestrator creates the Work Order in Jira:

```json
{
  "project": "CHECKOUT-WO",
  "issueType": "Work Order",
  "summary": "Implement: Add user preferences panel",
  "customFields": {
    "foundry-scenario": "implement-feature",
    "foundry-workspace": "development",
    "foundry-workbench": "checkout",
    "foundry-orchestration-item": "PI-456",
    "foundry-wo-label": "dev-wo"
  }
}
```

---

### Phase 5: Scenario Resolution

**Location:** WO Runtime (in Workspace Session)  
**Actor:** WO Runtime Daemon

#### Step 5.1: WO Assigned to Session

Developer Alice's Workspace Session receives the WO:

```
Jira Poll: WO-789 assigned to alice@acme.com
Scenario: implement-feature
Workspace: development
```

#### Step 5.2: Resolve Effective Scenario

WO Runtime queries Scenario Management for the effective scenario:

```
GET /api/v1/scenarios/effective?name=implement-feature&workspace=development&workbench=checkout
```

Resolution process:

```
┌─────────────────────────────────────────────────────────────────┐
│  Effective Scenario Resolution                                   │
│                                                                  │
│  1. Check Workbench-level (checkout/development):               │
│     └── Found: implement-feature.yaml ─────────────── ✓ Use    │
│                                                                  │
│  (If not found, would check Workshop-level)                     │
│                                                                  │
│  Result: Workbench scenario                                      │
└─────────────────────────────────────────────────────────────────┘
```

Response:

```json
{
  "scenario": {
    "name": "implement-feature",
    "spec": { ... },
    "skilled_agent": { "ref": "sa-full-stack-dev", "fallback": "auto" }
  },
  "source": "workbench",
  "source_id": "checkout"
}
```

---

### Phase 6: Agent Recommendation

**Location:** Scenario Management / WO Runtime  
**Actor:** WO Runtime Daemon

#### Step 6.1: Request Recommendations

If `fallback: auto` is set, WO Runtime asks for recommendations:

```
GET /api/v1/scenarios/scenario-uuid-123/recommendations?workspace_id=checkout-dev
```

#### Step 6.2: Score Available Agents

Scenario Management evaluates available Skilled Agents:

```
┌─────────────────────────────────────────────────────────────────┐
│  Agent Recommendation Scoring                                    │
│                                                                  │
│  Required skills: requirements-analysis, code-implementation,    │
│                   test-writing                                   │
│                                                                  │
│  Candidate: sa-full-stack-dev                                   │
│    Skills: requirements-analysis ✓, code-implementation ✓,      │
│            test-writing ✓, code-review ✓                        │
│    Coverage: 100%                                                │
│    Workspace: development ✓                                      │
│    Score: 0.95                                                   │
│                                                                  │
│  Candidate: sa-backend-dev                                       │
│    Skills: code-implementation ✓, test-writing ✓                │
│    Coverage: 67%                                                 │
│    Workspace: development ✓                                      │
│    Score: 0.70                                                   │
│                                                                  │
│  Recommendation: sa-full-stack-dev (0.95)                       │
└─────────────────────────────────────────────────────────────────┘
```

Response:

```json
{
  "recommendations": [
    {
      "skilled_agent_id": "sa-full-stack-dev",
      "score": 0.95,
      "reasons": ["Skill coverage: 100%", "Configured for development workspace"]
    },
    {
      "skilled_agent_id": "sa-backend-dev",
      "score": 0.70,
      "reasons": ["Skill coverage: 67%"]
    }
  ]
}
```

---

### Phase 7: Agent Execution

**Location:** Workspace Session  
**Actor:** WO Runtime + Employed Agent

#### Step 7.1: Spawn Agent

WO Runtime spawns the recommended agent:

```
Selected: sa-full-stack-dev
Capable Agent: cursor-agent
Model: claude-opus

Harness prepared:
  - Environment: FOUNDRY_SCENARIO=implement-feature, FOUNDRY_TASK_KEY=TASK-890
  - Skills: requirements-analysis@1.2.0, code-implementation@2.1.0, test-writing@1.5.0
  - Context: PI-456 product specification, workbench conventions
  - Delegation Token: <jwt>
```

#### Step 7.2: Execute Tasks

Agent executes tasks per scenario definition:

```
Task 1: analyze-requirements
  └── Reads PSD reference
  └── Creates implementation plan
  └── Marks complete

Task 2: implement-code (depends on Task 1)
  └── Reads implementation plan
  └── Writes code changes
  └── Writes tests
  └── Creates PR
  └── Marks complete
```

#### Step 7.3: WO Completion

When all tasks complete:

```
WO-789: All tasks complete
  └── WO Runtime notifies Orchestrator
  └── Orchestrator advances PI-456 to next stage
```

---

## Summary

| Phase | Location | Actor | Key Output |
|-------|----------|-------|------------|
| 1. Authoring | Workshop Repo | Admin | Scenario YAML file |
| 2. Validation | Validation Service | Automated | PR check status |
| 3. Sync | Sync Service | Automated | Scenario in Metadata Service |
| 4. WO Creation | Orchestrator | Workflow Engine | Work Order in Jira |
| 5. Resolution | WO Runtime | Daemon | Effective scenario definition |
| 6. Recommendation | Scenario Management | API | Ranked agent list |
| 7. Execution | Workspace Session | Employed Agent | Task outputs |

## Key Integration Points

```
┌──────────────┐     ┌──────────────┐     ┌──────────────┐
│   Workshop   │────▶│   Workshop   │────▶│   Metadata   │
│     Repo     │ PR  │  Validation  │sync │   Service    │
└──────────────┘     └──────────────┘     └──────────────┘
                            │                    │
                     calls  │                    │ queries
                            ▼                    ▼
                     ┌──────────────┐     ┌──────────────┐
                     │   Scenario   │◀────│  WO Runtime  │
                     │  Management  │     │              │
                     └──────────────┘     └──────────────┘
```

## Read Next

- [README.md](README.md) — Scenario Management overview
- [requirements.md](requirements.md) — Implementation requirements
- [scenario-schema.md](scenario-schema.md) — Full YAML schema
- [../services/workshop-validation.md](../services/workshop-validation.md) — Validation service details
- [../../orchestrator/pi-journey.md](../../orchestrator/pi-journey.md) — How scenarios fit in PI flow
- [../../work-order-runtime/end-to-end-work-order-flow.md](../../work-order-runtime/end-to-end-work-order-flow.md) — WO execution details
