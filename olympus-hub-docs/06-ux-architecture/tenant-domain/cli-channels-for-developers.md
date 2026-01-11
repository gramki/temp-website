# CLI Channels for Developers

> **Audience**: Developers, Agent Engineers  
> **Scope**: Hub CLI commands for application development and deployment  
> **Last Updated**: 2026-01-11

---

## Overview

Hub provides **two command-line interfaces** for developers, each operating in a different context:

| CLI | Purpose | Runs Where | Auth Context |
|-----|---------|------------|--------------|
| **`hubdev`** | Open and manage workspaces | Your local machine | Tenant subscription (control plane) |
| **`hub`** | Build, deploy, monitor | Inside remote workspace | Workbench instance (data plane) |

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  YOUR LAPTOP                           │  REMOTE WORKSPACE                   │
│                                        │                                     │
│  hubdev login                          │                                     │
│  hubdev workspace list                 │                                     │
│  hubdev workspace open ─────────────────▶  VS Code opens here               │
│                                        │                                     │
│                                        │  hub sync scenario ...             │
│                                        │  hub validate scenario ...          │
│                                        │  hub logs agent ...                │
│                                        │  hub watch request ...             │
│                                        │                                     │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Remote Development Model

> **Important**: Hub development is entirely **remote**. There is no local development environment on your laptop.

All resources (specs, scripts, configs) live in a **Hub-managed remote workspace** backed by Git. When you run `hubdev workspace open`, VS Code connects to this remote workspace. All `hub` commands execute within this remote context. This ensures:

- Consistent environments across all developers
- Direct access to Hub services and runtimes
- Git-based version control with branch workflows
- No "works on my machine" issues

This document covers both CLIs. For installation, see [Hub CLI Installation Guide](../../10-guides/hub-cli-setup.md).

---

## Getting Started

### Prerequisites

- `hubdev` and `hub` CLIs installed (see [Installation Guide](../../10-guides/hub-cli-setup.md))
- Tenant subscription credentials (for `hubdev`)
- Network access to Hub control plane

### Step 1: Login to Hub (Control Plane)

On your **local machine**, authenticate to your tenant subscription:

```bash
# Login (opens browser for OAuth)
hubdev login

# Verify authentication
hubdev whoami
```

### Step 2: List and Open a Workspace

```bash
# List available workbench instances
hubdev workspace list

# Open a workspace (launches VS Code connected to remote workspace)
hubdev workspace open acme-disputes-sandbox

# Open at a specific branch
hubdev workspace open acme-disputes-sandbox --branch feature/new-agent

# Create a new branch and open
hubdev workspace open acme-disputes-sandbox --branch feature/refund-logic --new
```

When the workspace opens:
- VS Code connects to the Hub-managed remote environment
- Terminal is pre-configured with workbench context
- `hub` commands are ready to use (no additional auth needed)

### Step 3: Work Inside the Workspace

Once inside the workspace, all `hub` commands are automatically scoped to that Workbench Instance:

```bash
# No additional configuration needed — context is inherited from workspace

# Verify workspace context
hub context

# Start working
hub get scenario-normative
# Edit files, then commit and sync
git add .
git commit -m "feat: my changes"
git push
hub sync scenario my-scenario-sandbox
```

### hubdev Configuration (Local Machine)

The `hubdev` CLI stores configuration locally:

```yaml
# ~/.hubdev/config.yaml
tenant: acme-bank
api-endpoint: https://hub.olympus.acme.bank/api/v1
auth:
  type: oidc
  issuer: https://auth.acme.bank
  client-id: hubdev-cli

# Recently used workspaces (auto-populated)
recent-workspaces:
  - acme-disputes-sandbox
  - acme-disputes-prod
```

### hub Context (Inside Workspace)

Inside the workspace, context is automatic. You can verify with:

```bash
# View current context
hub context

# Output:
# Workbench: acme-disputes
# Instance: acme-disputes-sandbox
# Branch: main
# User: developer@acme.bank
```

### Workbench Instance and Kubernetes Namespace Mapping

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

---

## hubdev Command Reference (Control Plane)

These commands run on your **local machine** before entering a workspace.

### `hubdev login`

**Purpose**: Authenticate to your tenant subscription. Opens a browser for OAuth/OIDC flow.

```bash
# Login (opens browser)
hubdev login

# Login to specific tenant
hubdev login --tenant acme-bank

# Verify authentication
hubdev whoami
```

### `hubdev workspace`

**Purpose**: Manage and open remote workspaces.

| Command | Description |
|---------|-------------|
| `hubdev workspace list` | List available workbench instances |
| `hubdev workspace open <instance>` | Open workspace in VS Code |
| `hubdev workspace open <instance> --branch <name>` | Open at specific branch |
| `hubdev workspace open <instance> --branch <name> --new` | Create branch and open |
| `hubdev workspace status <instance>` | Check workspace status |
| `hubdev workspace close <instance>` | Close remote workspace |

```bash
# List all workbench instances you have access to
hubdev workspace list

# Output:
# INSTANCE                  WORKBENCH        LIFECYCLE    STATUS
# acme-disputes-sandbox     acme-disputes    dev          ready
# acme-disputes-prod        acme-disputes    production   ready
# acme-cards-sandbox        acme-cards       dev          ready

# Open a workspace
hubdev workspace open acme-disputes-sandbox

# Open at a specific branch
hubdev workspace open acme-disputes-sandbox --branch feature/new-agent

# Create a new branch and open
hubdev workspace open acme-disputes-sandbox --branch feature/refund-logic --new

# Check workspace status
hubdev workspace status acme-disputes-sandbox

# Close workspace (free resources)
hubdev workspace close acme-disputes-sandbox
```

### `hubdev config`

**Purpose**: Manage hubdev configuration on your local machine.

```bash
# View current config
hubdev config view

# Set default tenant
hubdev config set-tenant acme-bank

# Clear credentials
hubdev logout
```

---

## hub Command Reference (Data Plane)

These commands run **inside the remote workspace**. Context (workbench, instance, branch) is inherited automatically.

---

## GitOps Pattern: Hub Commands Read from Git

**Critical**: All `hub` commands operate on files that are **committed to Git**, not the local filesystem. This ensures:

- 100% of Hub modifications follow GitOps pattern
- Complete audit trail in Git history
- Branch-based isolation
- Reproducible deployments

**Workflow**:
1. Edit files in VS Code
2. **Commit to Git** (`git add`, `git commit`, `git push`)
3. **Then** use hub commands (`hub sync scenario` or `hub sync workbench`)

**Why No `hub apply`?**
- Smallest unit of deployment is **Scenario**, not individual files
- GitOps principle: sync states (scenarios/workbenches), not files
- Ensures atomic deployments and proper dependency management
- Use `hub validate` for validation-only operations

**Git Context**: All hub commands emit:
- Git repository URL
- Current branch name
- Commit SHA
- Tags (if any)

Example output:
```
Git Context:
  Repository: https://git.hub.acme.com/acme-dev-subscription
  Branch: feature/new-trigger
  Commit: abc123def456
  Tags: []
```

---

## Why No `hub apply`? GitOps and Scenario-Based Deployment

**Important**: The `hub apply -f <file>` command has been removed. This section explains why.

### The GitOps Principle

In a true GitOps model:
- **Sync states, not files**: You sync entire application states (scenarios/workbenches), not individual files
- **Smallest unit of deployment**: The smallest unit of deployment in Hub is a **Scenario**, not an individual resource file
- **Atomic deployments**: Scenarios ensure all related resources are deployed together atomically
- **Dependency management**: Scenarios handle dependencies between resources automatically

### Why `hub apply` Doesn't Fit

`hub apply -f <file>` suggests a file-by-file workflow that conflicts with GitOps:

1. **File-level thinking**: Encourages applying individual files, not complete application states
2. **Dependency issues**: Individual files may have dependencies that aren't visible at file level
3. **Incomplete deployments**: Applying one file doesn't guarantee the scenario is complete
4. **Not atomic**: File-level applies don't ensure atomic deployments

### The Correct Approach

**Primary Deployment Command**: `hub sync scenario <name>`
- Syncs entire scenario (smallest unit of deployment)
- Ensures all scenario resources are deployed atomically
- Handles dependencies automatically
- Aligns with GitOps principles

**Alternative**: `hub sync workbench`
- Syncs entire workbench state
- Useful for full workbench synchronization

**Validation-Only**: `hub validate -f <file>` or `hub validate scenario <name>`
- Validates without deploying
- Useful for linting/validation before committing

### Workflow Comparison

**❌ Old (file-based)**:
```bash
hub apply -f training-spec.yaml
hub apply -f hub-application.yaml
hub apply -f scenario-deployment.yaml
```

**✅ New (scenario-based)**:
```bash
# Edit all scenario files
git add .
git commit -m "feat: update dispute-triage scenario"
git push
hub sync scenario dispute-triage  # One command syncs entire scenario
```

### Benefits

- ✅ **Atomic deployments**: Entire scenario deployed together
- ✅ **Dependency management**: All dependencies handled automatically
- ✅ **Simpler mental model**: One command per scenario
- ✅ **GitOps aligned**: Sync states, not files
- ✅ **Clear audit trail**: Scenario-level audit logs

---

## Audit Logging and Non-Repudiation

**Critical Design Requirement**: All `hub` CLI commands maintain detailed audit logs that ensure non-repudiation for compliance and security.

### What Gets Logged

Every `hub` command execution is logged with:

| Field | Purpose | Example |
|-------|---------|---------|
| **Timestamp** | When command executed | `2026-01-11T14:32:15.123Z` |
| **User Identity** | Who executed the command | `developer@acme.bank` |
| **Command** | Exact command with arguments | `hub sync scenario dispute-triage` |
| **Git Repository** | Source repository | `https://git.hub.acme.com/acme-dev-subscription` |
| **Git Branch** | Branch context | `feature/new-trigger` |
| **Git Commit SHA** | **Critical for non-repudiation** | `abc123def456789...` |
| **Git Tags** | Version tags if any | `v1.2.3` |
| **Workbench Instance** | Target workbench | `dispute-ops-dev` |
| **Resources Affected** | What was modified | `ScenarioDeployment/dispute-triage-dev` |
| **Result** | Success/failure | `SUCCESS` or `FAILED: reason` |

### Audit Log Format

Example audit log entry:

```
2026-01-11T14:32:15.123Z | developer@acme.bank | hub sync scenario dispute-triage
  git_repo: https://git.hub.acme.com/acme-dev-subscription
  git_branch: feature/new-trigger
  git_commit: abc123def4567890123456789012345678901234
  git_tags: []
  workbench_instance: dispute-ops-dev
  resources: [ScenarioDeployment/dispute-triage-dev, HubApplicationDeployment/dispute-triage-agent-001]
  result: SUCCESS
  git_sha: abc123def4567890123456789012345678901234
```

### Non-Repudiation Guarantee

The inclusion of **Git Commit SHA** in every audit log entry ensures:

1. **Immutable Record**: Git commits are cryptographically hashed and immutable
2. **Exact State**: The SHA identifies the exact version of code/resources that were applied
3. **Audit Trail**: Can trace any Hub modification back to specific Git commit
4. **Compliance**: Meets regulatory requirements for change tracking
5. **Accountability**: Cannot deny what was executed - the SHA proves the exact state

### Accessing Audit Logs

**Audit Log Access Model**: Everyone who has access to audit logs can view **all audit logs** for the subscription. There is no per-user filtering by default (refined access control may be added later).

**For Developers**:
```bash
# View all audit log entries (for subscription)
hub audit log

# View audit log for specific resource
hub audit log --resource TrainingSpec/dispute-triage-agent-v1

# View audit log for specific git commit
hub audit log --git-commit abc123def456789

# View audit log for time range
hub audit log --since 2026-01-11 --until 2026-01-12

# View audit log for specific user (if needed)
hub audit log --user developer@acme.bank

# Export audit logs for compliance
hub audit log --export --format json > audit-2026-01-11.json

# Search audit logs
hub audit log --search "dispute-triage-agent"
```

**Storage**: Audit logs are stored in the Hub control plane and are accessible to all authorized users for the subscription.

### Audit Log Retention

- **Retention Policy**: Configured per tenant (typically 7 years for regulated industries)
- **Immutable Storage**: Audit logs are write-once, append-only
- **Access Control**: Only authorized personnel can view audit logs
- **Export**: Audit logs can be exported for external compliance systems

### Compliance Benefits

The audit logging design ensures:

- ✅ **Non-repudiation**: Git SHA proves exact state of resources
- ✅ **Complete traceability**: Every change linked to Git commit
- ✅ **Regulatory compliance**: Meets SOX, PCI-DSS, HIPAA audit requirements
- ✅ **Forensic analysis**: Can reconstruct exact sequence of changes
- ✅ **Change attribution**: Know who changed what, when, and from which commit

---

### Phase 1: Explore and Understand

Before building, understand the Scenario you're implementing.

#### `hub get`

**Purpose**: Retrieve and inspect Hub resources. Use this to review Scenario definitions, understand requirements, and verify resource state.

| Usage | Description |
|-------|-------------|
| `hub get <resource-type>` | List all resources of a type |
| `hub get <resource-type> <name>` | Get specific resource |
| `hub get <resource-type> <name> -o yaml` | Output as YAML |
| `hub get <resource-type> <name> -o json` | Output as JSON |
| `hub get <resource-type> <name> -o wide` | Extended table view |
| `hub get <resource-type> --watch` | Watch for changes |

**Common Resources for Developers**:

```bash
# Review the Scenario you're implementing
hub get scenario-normative routine-dispute-triage -o yaml

# List all applications in your workbench
hub get hub-application-spec

# Check deployment status
hub get scenario-deployment

# View training specs
hub get training-spec

# List workbench instances
hub get workbench-instance
```

**Filtering**:
```bash
# Filter by label
hub get hub-application-spec -l "seer.olympus.io/resource-type=trained-agent"

# Filter by field
hub get scenario-deployment --field-selector "spec.workbenchInstance.name=acme-disputes-sandbox"
```

---

### Phase 2: Build and Configure

Create and modify your application specifications. Remember: all changes must be committed to Git before syncing.

#### `hub validate`

**Purpose**: Validate Hub resources without deploying. Use this for linting/validation before committing changes. Since `hub apply` was removed (not aligned with GitOps), `hub validate` provides validation-only operations.

##### `hub validate -f <file>`

**Purpose**: Validate a single file without deploying. Useful for linting/validation before committing.

**Usage**:
```bash
# Validate a single file
hub validate -f scenarios/dispute-triage/automation.yaml

# Validate multiple files
hub validate -f file1.yaml -f file2.yaml
```

**What it checks**:
- File syntax and structure
- CRD schema validation
- References to other resources
- Does NOT check branch alignment or dirty files (since it's read-only)

**Example output**:
```
Validating scenarios/dispute-triage/automation.yaml...

✓ File syntax valid
✓ CRD schema valid
✓ References valid:
  - HubApplicationSpec/dispute-triage-agent (exists)
  - WorkbenchInstance/dispute-ops-dev (exists)
✓ Validation passed
```

##### `hub validate scenario <name>`

**Purpose**: Validate an entire scenario without deploying. Useful for comprehensive validation before sync.

**Usage**:
```bash
# Validate a scenario
hub validate scenario dispute-triage

# Validate with verbose output
hub validate scenario dispute-triage --verbose
```

**What it checks**:
- All scenario files (normative, automation, deployment specs)
- All referenced resources (HubApplicationSpec, WorkbenchInstance, etc.)
- Scenario consistency and completeness
- Does NOT check branch alignment or dirty files (since it's read-only)

**Example output**:
```
Validating scenario: dispute-triage

✓ ScenarioNormativeSpec valid
✓ ScenarioAutomationSpec valid
✓ ScenarioDeploymentSpec valid
✓ All referenced resources exist:
  - HubApplicationSpec/dispute-triage-agent
  - WorkbenchInstance/dispute-ops-dev
✓ Scenario validation passed
```

**When to use**:
- Before committing changes (quick validation)
- In CI/CD pipelines (validate before merge)
- When debugging scenario issues (isolate validation from deployment)

#### `hub delete`

**Purpose**: Remove Hub resources. Use with caution—deletion of specifications may affect running deployments.

| Usage | Description |
|-------|-------------|
| `hub delete <resource-type> <name>` | Delete by name |
| `hub delete -f <file>` | Delete resources defined in file |
| `hub delete <resource-type> <name> --force` | Force delete (skip confirmation) |

```bash
# Delete a training spec (will prompt for confirmation)
hub delete training-spec dispute-triage-agent-v1

# Delete without confirmation
hub delete training-spec dispute-triage-agent-v1 --force
```

#### `hub branch` (Git Operations)

**Purpose**: Manage Git branches within the workspace. Since all resources are Git-backed, you can use standard branch workflows.

> **Note**: To open a workspace at a different branch, use `hubdev workspace open` from your local machine. Once inside a workspace, use `hub branch` for branch operations.

| Usage | Description |
|-------|-------------|
| `hub branch` | List branches |
| `hub branch <name>` | Switch to branch |
| `hub branch <name> --new` | Create and switch to new branch |
| `hub branch --current` | Show current branch |

```bash
# List branches
hub branch

# Switch to existing branch
hub branch feature/new-escalation-logic

# Create and switch to new branch
hub branch feature/refund-guardrails --new

# Show current branch
hub branch --current
```

**Committing Changes**:
```bash
# Stage and commit (standard Git via hub wrapper)
hub commit -m "Add refund guardrails to training spec"

# Push to remote
hub push
```

---

### Phase 3: Deploy to Sandbox

Deploy your application to a sandbox Workbench Instance for testing.

#### `hub sync`

**Purpose**: Trigger deployment of a Scenario to a Workbench Instance. This is the **primary deployment command**—it initiates the operator chain that generates `HubApplicationDeployment` and runtime resources. The smallest unit of deployment is a **Scenario**.

| Usage | Description |
|-------|-------------|
| `hub sync scenario <name>` | Deploy scenario |
| `hub sync scenario <name> --wait` | Wait for deployment to complete |
| `hub sync scenario <name> --timeout 5m` | Set timeout for --wait |
| `hub sync workbench` | Sync entire workbench state |

**Typical Flow**:

```bash
# Deploy to sandbox
hub sync scenario routine-dispute-triage-sandbox

# Deploy and wait for completion
hub sync scenario routine-dispute-triage-sandbox --wait

# Deploy with custom timeout
hub sync scenario routine-dispute-triage-sandbox --wait --timeout 10m
```

##### `hub sync scenario <name>`: What Gets Synced

**Critical Understanding**: When you run `hub sync scenario <name>`, Hub syncs **all resources** in that scenario atomically. This is not a partial sync—it's an all-or-nothing deployment of the entire scenario.

**What Gets Read from Git**:

1. **All three scenario definition files**:
   - `ScenarioNormativeSpec` (business context)
   - `ScenarioAutomationSpec` (automation logic)
   - `ScenarioDeploymentSpec` (deployment settings)

2. **All directly referenced resource files**:
   - `HubApplicationSpec` files referenced in `ScenarioAutomationSpec`
   - Any other CRD files directly referenced by the scenario specs

**What Gets Synced (All Resources in Scenario)**:

When you run `hub sync scenario dispute-triage`, Hub:

1. **Reads all scenario specs from Git** (committed versions only)
2. **Processes ScenarioDeploymentSpec** to determine deployment targets
3. **Generates HubApplicationDeployment** for each application in the scenario
4. **Triggers runtime operators** (Seer, Rhea, etc.) to create child resources:
   - `EmploymentSpec` (for Seer agents)
   - Kubernetes `Service` resources
   - Kubernetes `Deployment` resources
   - Any other runtime-specific resources

**Example**:
```bash
$ hub sync scenario dispute-triage

Git Context:
  Repository: https://git.hub.acme.com/acme-dev-subscription
  Branch: main
  Commit: abc123def4567890123456789012345678901234

Reading scenario definitions from Git...
  ✓ ScenarioNormativeSpec/dispute-triage (from Git)
  ✓ ScenarioAutomationSpec/dispute-triage (from Git)
  ✓ ScenarioDeploymentSpec/dispute-triage-sandbox (from Git)
  ✓ HubApplicationSpec/dispute-triage-agent (referenced, from Git)

Syncing scenario: dispute-triage...
  ✓ ScenarioDeployment/dispute-triage-sandbox created
  ✓ HubApplicationDeployment/dispute-triage-agent-001 created
  ✓ EmploymentSpec/dispute-triage-emp-001 created (by Seer Operator)
  ✓ Service/dispute-triage-emp-001-svc created
  ✓ Deployment/dispute-triage-emp-001-deployment created

✓ Scenario synced successfully (all resources deployed atomically)
```

**Key Points**:
- ✅ **Atomic**: All scenario resources deployed together
- ✅ **From Git**: All files read from committed Git state
- ✅ **Complete**: All resources in scenario, not partial
- ✅ **Dependencies**: All referenced resources must exist and be committed

**Why Scenario?**: You don't deploy individual agents or applications directly. A Scenario bundles the normative spec, automation spec, and deployment spec together. When you sync a Scenario, Hub processes all three specs and deploys everything atomically.

#### `hub rollback`

**Purpose**: Revert a Scenario deployment to a previous version. Use when a new deployment causes issues.

```bash
# Rollback to previous version
hub rollback scenario routine-dispute-triage-sandbox

# Rollback to specific version
hub rollback scenario routine-dispute-triage-sandbox --to-revision 3
```

#### Validation Errors

`hub sync` performs validation checks and **fails immediately** if validation fails:

##### Branch Mismatch Error

**What it checks**: Current git branch vs workbench instance's associated branch

**When it fails**: If you're on a different branch than the workbench instance expects

**Error behavior**: Command fails immediately (no option to continue)

**Example error**:
```
❌ ERROR: Branch Mismatch
   Current git branch: feature/new-trigger
   Workbench instance branch: main
   Workbench: dispute-ops-dev
   
   The workbench instance 'dispute-ops-dev' is configured to use branch 
   'main', but you're currently on 'feature/new-trigger'.
   
   A workbench instance can only be associated with one branch. To fix:
   
   Option 1: Switch to the workbench's branch
     hub branch main
     git pull
     hub sync scenario my-scenario
   
   Option 2: Request a new workbench instance for your branch
     (Contact Tenant Admin to create new workbench instance for 'feature/new-trigger')
   
   Option 3: Update workbench instance to use your branch (requires admin/authorized dev)
     (Contact Tenant Admin or authorized developer to change workbench instance branch association)
```

##### Dirty Files Error

**What it checks**: Scenario files have uncommitted local modifications (dirty files)

**When it fails**: If scenario files or referenced resource files have uncommitted changes

**Error behavior**: Command fails immediately (no option to continue)

**Uncommitted Changes Detection: What Files Are Checked?**

When you run `hub sync scenario <name>`, Hub checks for uncommitted changes in:

**✅ Checked Files**:
1. **Scenario definition files** (all 3 spec files):
   - `ScenarioNormativeSpec` file for the scenario
   - `ScenarioAutomationSpec` file for the scenario
   - `ScenarioDeploymentSpec` file for the scenario

2. **Directly referenced resource files**:
   - `HubApplicationSpec` files referenced in `ScenarioAutomationSpec`
   - Any other CRD files directly referenced by the scenario specs

**❌ NOT Checked**:
- Files in other scenarios
- All files in the repository
- Files not referenced by the scenario

**Example error**:
```
❌ ERROR: Dirty Files Detected
   
   Scenario files have uncommitted local changes:
   - scenarios/dispute-triage/normative.yaml (modified, 3 lines changed)
   - scenarios/dispute-triage/automation.yaml (modified, 1 line added)
   - specs/hub-applications/dispute-triage-agent.yaml (referenced, modified, 2 lines changed)
   
   Hub commands operate on committed Git files only (GitOps pattern).
   The scenario files and referenced resources have uncommitted changes.
   
   To fix:
   Option 1: Commit your changes first (recommended)
     git add scenarios/dispute-triage/ specs/hub-applications/dispute-triage-agent.yaml
     git commit -m "feat: update dispute-triage scenario"
     git push
     hub sync scenario dispute-triage
   
   Option 2: Stash your changes (if you want to sync committed version)
     git stash
     hub sync scenario dispute-triage
     git stash pop  # Restore your changes after sync
   
   Option 3: Discard changes (if accidental)
     git checkout scenarios/dispute-triage/
     hub sync scenario dispute-triage
```

**Why This Scope?**
- Ensures scenario integrity (all scenario components are committed)
- Catches dependencies (referenced resources must be committed)
- Reasonable scope (not checking entire repo, which would be slow)
- Aligns with scenario as atomic unit

##### Best Practices for Avoiding Errors

```bash
# 1. Always check branch alignment before sync
hub context  # Shows current branch, workbench branch, and alignment status

# 2. Always commit and push before sync
git status   # Check for uncommitted changes
git add .
git commit -m "feat: my changes"
git push
hub sync scenario my-scenario  # Now safe

# 3. Validate before sync (optional)
hub validate scenario my-scenario  # Validate without deploying

# 4. Verify before sync
hub context  # Double-check branch alignment
hub sync scenario my-scenario  # Will fail if branch mismatch or dirty files
```

---

### Phase 4: Monitor and Debug

Observe your deployed agents and applications.

#### `hub logs`

**Purpose**: View logs from running agents and operators. Essential for debugging behavior, understanding decision-making, and diagnosing issues.

| Usage | Description |
|-------|-------------|
| `hub logs agent <name>` | View agent logs |
| `hub logs agent <name> --follow` | Stream logs in real-time |
| `hub logs agent <name> --tail 100` | Last N log lines |
| `hub logs agent <name> --since 1h` | Logs from last hour |
| `hub logs operator <name>` | View operator logs |

**Agent Logs**:
```bash
# Stream agent logs
hub logs agent dispute-triage-emp-001 --follow

# Last 100 lines
hub logs agent dispute-triage-emp-001 --tail 100

# Logs from last 30 minutes
hub logs agent dispute-triage-emp-001 --since 30m

# Filter by log level
hub logs agent dispute-triage-emp-001 --level error
```

**Operator Logs** (for debugging deployment issues):
```bash
# Hub operator logs (system-level)
hub logs operator hub-operator --tail 100

# Seer operator logs (system-level)
hub logs operator seer-operator --tail 100
```

#### `hub metrics`

**Purpose**: View performance metrics for agents and applications. Use to understand response times, throughput, escalation rates, and resource usage.

| Usage | Description |
|-------|-------------|
| `hub metrics agent <name>` | Agent metrics summary |
| `hub metrics agent <name> --period 24h` | Metrics for time period |
| `hub metrics agent <name> -o json` | JSON output for parsing |

```bash
# View agent metrics
hub metrics agent dispute-triage-emp-001

# Metrics for last 24 hours
hub metrics agent dispute-triage-emp-001 --period 24h

# Specific metrics
hub metrics agent dispute-triage-emp-001 --metric response-time,escalation-rate
```

**Sample Output**:
```
Agent: dispute-triage-emp-001
Period: Last 1 hour

┌─────────────────────────────────────────────────────────┐
│ Metric                  │ Value   │ Trend   │ Threshold │
├─────────────────────────────────────────────────────────┤
│ Tasks Completed         │ 47      │ ↑ +12%  │ -         │
│ Avg Response Time       │ 2.3s    │ ↓ -5%   │ < 5s ✓    │
│ Escalation Rate         │ 8.5%    │ → 0%    │ < 15% ✓   │
│ Autonomous Decisions    │ 91.5%   │ ↑ +2%   │ > 80% ✓   │
│ Token Usage (hourly)    │ 12,450  │ → -1%   │ < 50,000  │
└─────────────────────────────────────────────────────────┘
```

#### `hub health`

**Purpose**: Check the health status of agents, applications, and infrastructure. Returns status, readiness, and any error conditions.

```bash
# Agent health
hub health agent dispute-triage-emp-001

# Application health
hub health application dispute-triage-agent

# All resources in workbench
hub health --all
```

#### `hub dashboard`

**Purpose**: Open the web-based Workbench dashboard for visual monitoring and debugging.

```bash
# Open sandbox dashboard
hub dashboard open acme-disputes-sandbox

# Open specific view
hub dashboard open acme-disputes-sandbox --view agents
hub dashboard open acme-disputes-sandbox --view requests
```

#### `hub events`

**Purpose**: View events related to a resource. Useful for understanding what happened during deployment or execution.

```bash
# View events for a deployment
hub get scenario-deployment routine-dispute-triage-sandbox --show-events

# View all events in workbench
hub events --all
```

#### `hub watch`

**Purpose**: Stream real-time updates for requests or scenario deployments. Unlike `hub logs` which shows agent internal logs, `hub watch` shows **Signal Exchange updates**—the business-level events flowing through the system.

##### Watch a Request

Stream all Signal Exchange updates for a specific Hub Request. Useful for debugging request flow and understanding how a request progresses through tasks.

| Usage | Description |
|-------|-------------|
| `hub watch request <request-id>` | Stream updates to stdout |
| `hub watch request <request-id> -o json` | JSON format output |
| `hub watch request <request-id> >> file.log` | Append to file |
| `hub watch request <request-id> --since 1h` | Include history from last hour |

```bash
# Watch a specific request
hub watch request REQ-2026-01-11-00042

# Watch and append to log file
hub watch request REQ-2026-01-11-00042 >> request-debug.log

# JSON output for parsing
hub watch request REQ-2026-01-11-00042 -o json

# Include recent history
hub watch request REQ-2026-01-11-00042 --since 30m
```

**Sample Output**:
```
[2026-01-11T14:32:05Z] REQ-2026-01-11-00042 | signal: dispute-filed | source: card-network
[2026-01-11T14:32:06Z] REQ-2026-01-11-00042 | task-created: triage-001 | assigned: dispute-triage-emp-001
[2026-01-11T14:32:08Z] REQ-2026-01-11-00042 | task-started: triage-001 | agent: dispute-triage-emp-001
[2026-01-11T14:32:12Z] REQ-2026-01-11-00042 | decision: classify-as-unauthorized | confidence: 0.94
[2026-01-11T14:32:13Z] REQ-2026-01-11-00042 | task-completed: triage-001 | outcome: escalate-to-investigation
[2026-01-11T14:32:14Z] REQ-2026-01-11-00042 | task-created: investigation-001 | assigned: fraud-analyst-emp-003
```

##### Watch a Scenario Deployment

Stream all Signal Exchange updates for **all requests** within a Scenario deployment. Useful for monitoring scenario health, observing traffic patterns, and debugging systemic issues.

| Usage | Description |
|-------|-------------|
| `hub watch scenario-deployment <name>` | Stream all request updates |
| `hub watch scenario-deployment <name> --filter status=error` | Filter by condition |
| `hub watch scenario-deployment <name> -o json` | JSON format |
| `hub watch scenario-deployment <name> >> file.log` | Append to file |

```bash
# Watch all requests in a scenario deployment
hub watch scenario-deployment routine-dispute-triage-sandbox

# Filter to only errors/escalations
hub watch scenario-deployment routine-dispute-triage-sandbox --filter status=error
hub watch scenario-deployment routine-dispute-triage-sandbox --filter event=escalation

# Append to monitoring log
hub watch scenario-deployment routine-dispute-triage-sandbox >> scenario-monitor.log

# JSON for log aggregation pipelines
hub watch scenario-deployment routine-dispute-triage-sandbox -o json | tee scenario-events.jsonl
```

**Sample Output**:
```
[2026-01-11T14:35:01Z] routine-dispute-triage-sandbox | REQ-00042 | task-completed: triage-001
[2026-01-11T14:35:03Z] routine-dispute-triage-sandbox | REQ-00043 | signal: dispute-filed
[2026-01-11T14:35:05Z] routine-dispute-triage-sandbox | REQ-00043 | task-created: triage-002
[2026-01-11T14:35:07Z] routine-dispute-triage-sandbox | REQ-00041 | escalation: human-review-required
[2026-01-11T14:35:09Z] routine-dispute-triage-sandbox | REQ-00044 | signal: dispute-filed
[2026-01-11T14:35:11Z] routine-dispute-triage-sandbox | REQ-00043 | decision: auto-approve-refund
```

---

### Phase 5: Validate and Test

Formally validate agent behavior before publication.

#### `hub validate`

**Purpose**: Run validation tests against a deployed agent. Validation tests the agent against Scenario-derived test cases including functional accuracy, procedural compliance, safety (guardrail adherence), and performance.

| Usage | Description |
|-------|-------------|
| `hub validate training-spec <name>` | Run validation |
| `hub validate training-spec <name> --workbench <wb>` | Specify workbench |
| `hub validate training-spec <name> -f <config>` | Use config file |
| `hub validate training-spec <name> --test-suites <list>` | Run specific suites |

```bash
# Basic validation
hub validate training-spec dispute-triage-agent-v1 --workbench acme-disputes-sandbox

# With specific test suites
hub validate training-spec dispute-triage-agent-v1 \
  --workbench acme-disputes-sandbox \
  --scenario routine-dispute-triage \
  --test-suites golden-set-disputes,edge-case-disputes,adversarial-prompts

# Using validation config file
hub validate training-spec dispute-triage-agent-v1 -f validation-config.yaml

# Output results to file
hub validate training-spec dispute-triage-agent-v1 \
  --workbench acme-disputes-sandbox \
  -o json > validation-results.json
```

**Validation Config Example**:
```yaml
# validation-config.yaml
employmentContext:
  workbench: acme-disputes-sandbox
  scenario: routine-dispute-triage
testSuites:
  - golden-set-disputes
  - edge-case-disputes
  - compliance-scenarios
evaluationCriteria:
  functionalAccuracy: 0.95
  slaCompliance: 0.99
  guardrailAdherence: 1.0
```

#### `hub diff`

**Purpose**: Compare two resources or deployments. Useful for understanding differences between sandbox and production configurations, or between spec versions.

```bash
# Compare sandbox vs production deployments
hub diff scenario-deployment routine-dispute-triage-sandbox routine-dispute-triage-prod

# Compare training spec versions
hub diff training-spec dispute-triage-agent-v1:0.1.0 dispute-triage-agent-v1:0.2.0

# Compare file to deployed resource
hub diff -f training-spec.yaml training-spec/dispute-triage-agent-v1
```

---

### Phase 6: Publish and Release

Graduate validated specifications for production use.

#### `hub publish`

**Purpose**: Publish a validated Training Specification, making it available for production employment. Publication:
- Bumps version from `0.x.x` to `1.0.0+`
- Locks guardrails (immutable after publication)
- Makes the spec available organization-wide

| Usage | Description |
|-------|-------------|
| `hub publish training-spec <name>` | Publish with auto-version |
| `hub publish training-spec <name> --version <v>` | Specify version |
| `hub publish training-spec <name> --approver <email>` | Record approver |
| `hub publish training-spec <name> --validation-ref <id>` | Link to validation |

```bash
# Publish with all metadata
hub publish training-spec dispute-triage-agent-v1 \
  --version 1.0.0 \
  --approver domain-steward@acme.bank \
  --validation-ref val-dispute-triage-2026-01-11 \
  --notes "Validated in acme-disputes-sandbox. Ready for production."

# Verify publication
hub get training-spec dispute-triage-agent-v1
```

---

### Phase 7: Production Deployment

Deploy to production (typically requires Supervisor approval).

#### `hub request-approval`

**Purpose**: Request approval for a production deployment. Creates an approval request that must be approved by authorized personnel (typically Supervisor or ARAO) before deployment can proceed.

```bash
# Request production deployment approval
hub request-approval scenario-deployment routine-dispute-triage-prod \
  --approver supervisor@acme.bank \
  --production-readiness-ref prc-dispute-triage-2026-01-11 \
  --notes "Approved for production employment"

# Check approval status
hub get approval-requests

# View specific approval request
hub get approval-request ar-routine-dispute-triage-prod-001
```

**Note**: Production sync often requires Supervisor permissions. As a Developer, you typically:
1. Create and apply the `ScenarioDeploymentSpec` for production
2. Request approval via `hub request-approval`
3. Supervisor executes `hub sync scenario` after approval

---

## Utility Commands

### Resource Inspection

```bash
# Describe resource with full details
hub describe training-spec dispute-triage-agent-v1

# Get specific fields (using JSONPath)
hub get training-spec dispute-triage-agent-v1 -o jsonpath='{.spec.guardrails}'

# List employed agents
hub get employed-agents
```

### Context and Configuration

Inside the workspace, context is inherited automatically. Use these commands to inspect:

```bash
# View current workspace context
hub context

# View current config (output preferences, etc.)
hub config view

# Set default output format
hub config set-output yaml
```

**`hub context` Output**:

The `hub context` command shows complete workspace context:

```bash
$ hub context

Workspace Context:
  User: developer@acme.bank
  Workbench Instance: dispute-ops-dev
  Workbench Branch: main
  Current Git Branch: main
  Branch Alignment: ✓ MATCH
  
Git Context:
  Repository: https://git.hub.acme.com/acme-dev-subscription
  Branch: main
  Commit: abc123def4567890123456789012345678901234
  Tags: []
  
Workbench Status:
  Last Synced: 2026-01-11T14:30:00Z
  Status: Running
  Scenarios Active: 2
```

**Key Fields**:
- **User**: Current authenticated user (whoami)
- **Workbench Instance**: Current workbench instance name
- **Workbench Branch**: Branch associated with workbench instance
- **Current Git Branch**: Current git branch in workspace
- **Branch Alignment**: Shows if branches match (MATCH/MISMATCH)
- **Last Synced**: Timestamp of last successful sync operation
- **Status**: Workbench instance running status

#### `hub audit log`

**Purpose**: View audit logs of hub command executions. All hub commands automatically create audit log entries with git SHA references for non-repudiation.

| Usage | Description |
|-------|-------------|
| `hub audit log` | View all audit log entries for the subscription |
| `hub audit log --user <email>` | View audit log for specific user |
| `hub audit log --resource <type>/<name>` | View audit log for specific resource |
| `hub audit log --git-commit <sha>` | View audit log entries for specific git commit |
| `hub audit log --since <date>` | View audit log since date |
| `hub audit log --until <date>` | View audit log until date |
| `hub audit log --export --format json` | Export audit logs for compliance |

**Examples**:

```bash
# View all recent audit log entries (for subscription)
hub audit log --since 2026-01-11

# View audit log for a specific resource
hub audit log --resource TrainingSpec/dispute-triage-agent-v1

# View audit log for a specific git commit
hub audit log --git-commit abc123def4567890123456789012345678901234

# View audit log for a specific user
hub audit log --user developer@acme.bank

# Export audit logs for compliance reporting
hub audit log --since 2026-01-01 --export --format json > audit-report.json
```

**Sample Output**:
```
AUDIT LOG ENTRIES (Last 10)

2026-01-11T14:32:15.123Z | developer@acme.bank | hub sync scenario dispute-triage
  git_repo: https://git.hub.acme.com/acme-dev-subscription
  git_branch: feature/new-trigger
  git_commit: abc123def4567890123456789012345678901234
  git_tags: []
  workbench_instance: dispute-ops-dev
  resources: [ScenarioDeployment/dispute-triage-dev, HubApplicationDeployment/dispute-triage-agent-001]
  result: SUCCESS

2026-01-11T14:30:22.456Z | developer@acme.bank | hub sync scenario standard-dispute
  git_repo: https://git.hub.acme.com/acme-dev-subscription
  git_branch: feature/new-trigger
  git_commit: abc123def4567890123456789012345678901234
  git_tags: []
  workbench_instance: dispute-ops-dev
  resources: [ScenarioDeployment/standard-dispute-dev]
  result: SUCCESS
```

> **Note**: Authentication and workspace switching are handled by `hubdev` on your local machine. Inside the workspace, you're already authenticated to the workbench instance.

---

## Command Flags Reference

### Global Flags (hub)

These flags work with all `hub` commands inside the workspace:

| Flag | Short | Description |
|------|-------|-------------|
| `--output` | `-o` | Output format: yaml, json, table, wide |
| `--verbose` | `-v` | Verbose output |
| `--quiet` | `-q` | Minimal output |
| `--help` | `-h` | Show help |

> **Note**: Workbench and instance context is inherited from the workspace. Use `hubdev workspace open` to switch workspaces.

### Output Formats

| Format | Description | Use Case |
|--------|-------------|----------|
| `table` | Human-readable table (default) | Interactive use |
| `wide` | Extended table with more columns | Detailed inspection |
| `yaml` | YAML format | Editing, piping to files |
| `json` | JSON format | Scripting, parsing |
| `jsonpath` | Extract specific fields | Automation |

---

## Common Workflows

> **Prerequisite**: Open your workspace first with `hubdev workspace open <instance>`. All commands below run inside the workspace.

### Develop → Test → Deploy (Sandbox)

```bash
# 1. Review scenario requirements
hub get scenario-normative routine-dispute-triage -o yaml

# 2. Edit scenario files in VS Code
# (Edit training-spec.yaml, hub-application-spec.yaml, scenario-automation-spec.yaml, scenario-deployment-sandbox.yaml)

# 3. Commit and push changes
git add .
git commit -m "feat: update dispute-triage scenario"
git push

# 4. Deploy to sandbox (syncs entire scenario)
hub sync scenario routine-dispute-triage-sandbox --wait

# 5. Monitor
hub logs agent dispute-triage-emp-001 --follow

# 6. Iterate (update specs, commit, re-sync)
# Edit files, then:
git add .
git commit -m "feat: update to version 0.2.0"
git push
hub sync scenario routine-dispute-triage-sandbox
```

### Validate → Publish → Production

```bash
# 1. Run validation (optional, before committing)
hub validate scenario routine-dispute-triage

# 2. Commit and push changes
git add .
git commit -m "feat: production deployment spec"
git push

# 3. Publish training spec
hub publish training-spec dispute-triage-agent-v1 --version 1.0.0

# 4. Request approval
hub request-approval scenario-deployment routine-dispute-triage-prod \
  --approver supervisor@acme.bank

# 5. (After approval) Supervisor deploys
# hub sync scenario routine-dispute-triage-prod
```

### Debug a Failing Agent

```bash
# 1. Check agent health
hub health agent dispute-triage-emp-001

# 2. View recent logs
hub logs agent dispute-triage-emp-001 --tail 200 --level error

# 3. Check events
hub get scenario-deployment routine-dispute-triage-sandbox --show-events

# 4. View metrics
hub metrics agent dispute-triage-emp-001 --period 1h

# 5. Compare configs
hub diff scenario-deployment routine-dispute-triage-sandbox routine-dispute-triage-prod
```

---

## Error Handling

### Common Errors

| Error | Cause | Resolution |
|-------|-------|------------|
| `resource not found` | Resource doesn't exist | Verify name and workbench instance |
| `unauthorized` | Invalid or expired credentials | Run `hub auth login` |
| `forbidden` | Insufficient permissions | Contact Supervisor for access |
| `validation failed` | Invalid resource specification | Check YAML syntax and schema |
| `sync timeout` | Deployment taking too long | Check operator logs |
| `version mismatch` | Reference to non-existent version | Update version references |

### Debugging Tips

```bash
# Validate before syncing (verbose output)
hub validate scenario routine-dispute-triage --verbose

# Check operator logs
hub logs operator hub-operator --tail 100
hub logs operator seer-operator --tail 100

# Verify resource state
hub describe scenario-deployment routine-dispute-triage-sandbox

# Check audit logs for recent changes
hub audit log --since 1h
```

---

## Related Documentation

- [Hub CLI Installation Guide](../../10-guides/hub-cli-setup.md) — Installation and initial setup
- [Automation Development Desk](./automation-development-desk.md) — Web UI for developers
- [Agent Development Lifecycle Guide](../../../../olympus-seer-docs/seer-design/guides/agent-development-lifecycle.md) — Complete agent development workflow
- [Agent Lifecycle FAQ](../../../../olympus-seer-docs/seer-design/guides/agent-lifecycle-faq.md) — Common questions

---

*All commands operate within your configured Workbench Instance scope. Use `hub config view` to verify your current context.*
