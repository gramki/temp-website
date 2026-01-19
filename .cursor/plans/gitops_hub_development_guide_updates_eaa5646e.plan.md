---
name: GitOps Hub Development Guide Updates
overview: "Update Hub development documentation to clarify GitOps pattern: all hub commands operate on Git-committed files from the current branch, not filesystem. Remove hub apply command (not aligned with GitOps). Standardize on hub sync scenario as primary deployment command. Add hub validate for validation-only operations. Add Day 1 setup, Git vs Hub clarification, and ensure all workflows follow GitOps pattern (edit → commit → sync scenario)."
todos: []
---

# GitOps Hub Development Guide Updates

## Overview

This plan updates the Hub development documentation to:

1. **Remove `hub apply` command**: Not aligned with GitOps model where smallest unit of deployment is Scenario. Standardize on `hub sync scenario` as primary deployment command.
2. **Add `hub validate` commands**: For validation-only operations (validate file, validate scenario) without deploying.
3. **Clarify GitOps pattern**: All `hub` commands operate on Git-committed files from the current branch, not the local filesystem
4. **Fix workflow order**: Change to "edit → git commit → git push → hub sync scenario" (scenario is smallest unit of deployment)
5. **Add Day 1 setup**: Create onboarding section for new developers (contact Tenant Admin for access)
6. **Clarify Git vs Hub**: Explicit distinction throughout all documents
7. **Add Git context emission**: Document that all hub commands show git repo, branch, commit SHA, and tags
8. **Document validation errors**: Branch mismatch and dirty file errors for `hub sync` (commands fail by default)
9. **Document audit logging**: All hub CLI commands maintain detailed audit logs with git SHA references for non-repudiation
10. **Clarify workbench instance model**: One workbench instance = one workspace = one branch. Multiple developers = multiple instances
11. **Document `hub context` output**: Includes whoami, last synced status, git info, and branch alignment

---

## Major Change: Removal of `hub apply` Command

**Decision**: Remove `hub apply -f <file>` command entirely. It is not aligned with GitOps model where the smallest unit of deployment is a Scenario.

**Rationale**:

- GitOps principle: sync states (scenarios/workbenches), not individual files
- Smallest unit of deployment is **Scenario**, not individual files
- File-level applies encourage anti-patterns and incomplete deployments
- Scenario-based sync ensures atomic deployments and proper dependency management

**Replacement**:

- **Primary deployment**: `hub sync scenario <name>` - sync entire scenario
- **Full sync**: `hub sync workbench` - sync entire workbench state
- **Validation-only**: `hub validate -f <file>` or `hub validate scenario <name>` - validate without deploying

---

## Key Clarifications Incorporated

Based on user feedback, the following clarifications have been incorporated into this plan:

1. **Removal of `hub apply` Command**:

            - `hub apply -f <file>` removed - not aligned with GitOps model
            - Smallest unit of deployment is **Scenario**, not individual files
            - Primary deployment command: `hub sync scenario <name>`
            - Alternative: `hub sync workbench` for syncing entire workbench
            - Validation-only: `hub validate -f <file>` and `hub validate scenario <name>`

2. **Validation Errors (Not Warnings)**: `hub sync` **fails immediately** if:

            - Branch mismatch detected (current branch ≠ workbench instance branch)
            - Dirty files detected (scenario files have uncommitted changes)
            - No "continue anyway" options - commands fail by default

3. **Workbench Instance Model**: 

            - One workbench instance = one workspace = one branch
            - Multiple developers = multiple workbench instances (not same instance)
            - Each developer working on same Workbench Specification gets their own instance

4. **hub sync Behavior**:

            - Reads committed scenario definitions from Git
            - **Errors out** if scenario files are dirty (uncommitted changes)
            - Developer must stash or commit before sync can proceed
            - Syncs entire scenario (smallest unit of deployment)

5. **hub context Output**:

            - Includes whoami (current user)
            - Shows last synced status (running status) of workbench instance
            - Shows branch alignment status (MATCH/MISMATCH)

6. **Audit Log Access**:

            - Everyone with access can view **all audit logs** for the subscription
            - No per-user filtering by default (refined access may come later)
            - Stored in Hub control plane

7. **Day 1 Setup**:

            - Contact **Tenant Admin** for access (not team lead)
            - Request workbench instance with branch association

8. **No Git Workflow Guidance**:

            - Guide should not include git branching strategies, merge/rebase workflows
            - Focus on Hub-specific workflows only

---

## Files to Update

### 1. CLI Channels Documentation

**File**: `olympus-hub-docs/06-ux-architecture/tenant-domain/cli-channels-for-developers.md`

**Changes**:

- **Remove `hub apply` command entirely** - not aligned with GitOps model
- Add "GitOps Pattern" section explaining that hub commands only read from Git
- Update `hub sync scenario` as primary deployment command (smallest unit of deployment)
- **Document `hub sync scenario` detailed behavior**:
        - Reads all 3 scenario spec files from Git (ScenarioNormativeSpec, ScenarioAutomationSpec, ScenarioDeploymentSpec)
        - Reads all referenced resource files from Git (HubApplicationSpec, etc.)
        - Syncs **all resources** in the scenario (atomic deployment)
        - Checks for uncommitted changes in: scenario spec files + directly referenced resource files only
- Add `hub validate` commands for validation-only operations
- Document git context emission in all hub commands (repo, branch, commit SHA, tags)
- Document validation errors: branch mismatch and dirty file errors for `hub sync` (commands fail by default)
- **Document uncommitted changes detection scope**: scenario files + referenced resources only (not all repo files)
- Document audit logging: all hub commands maintain detailed audit logs with git SHA references
- Update all workflow examples to show correct order: edit → commit → push → sync scenario
- Add `hub context` output showing whoami, workbench, branch, git info, and last synced status
- Add troubleshooting section for branch mismatch and dirty file errors
- Add section on audit log access and non-repudiation guarantees
- Add section explaining why `hub apply` was removed (GitOps rationale)

**Key Sections to Update**:

- Line ~217: Add "GitOps Pattern" section after "hub Command Reference" header
- Line ~217: Add "Why No `hub apply`? GitOps and Scenario-Based Deployment" section
- Line ~217: Add "Audit Logging and Non-Repudiation" section after GitOps Pattern
- **Remove** `hub apply` section entirely (Line ~272-306)
- Line ~368-395: Update `hub sync scenario` section to be primary deployment command with:
        - Detailed behavior explanation (reads all 3 spec files from Git)
        - Clarification that it syncs ALL resources in scenario (atomic)
        - What files are checked for uncommitted changes (scenario files + referenced resources only)
        - Example showing what gets synced
- Add new subsection: "What Gets Synced: All Resources in Scenario"
- Add new subsection: "Uncommitted Changes Detection: Scenario-Specific Scope"
- Add new `hub validate` command section (validate file, validate scenario)
- Line ~219: Update "Context is inherited automatically" to mention git branch
- Add git context examples to command outputs throughout
- Add error message examples for branch mismatch and dirty files (with scenario file listing)
- Add troubleshooting section for these errors
- Add `hub audit log` command documentation in Utility Commands section
- Update all command examples to show audit log entry creation
- Update all workflow examples to use `hub sync scenario` instead of `hub apply`

---

### 2. Hub Development Flow Guide - README

**File**: `olympus-hub-docs/10-guides/hub-development-flow/README.md`

**Changes**:

- Add "Day 1: Quick Start" section before "Start Here"
- Add "Prerequisites Checklist" section
- Update "Key Concepts" to include GitOps pattern
- Add "Git vs Hub Commands" clarification table
- Update "Start Here" to point to Day 1 setup

**Key Sections to Add**:

- New section: "Day 1: Quick Start (5 Minutes)"
- New section: "Prerequisites Checklist"
- Update "Key Concepts" table with GitOps entries
- New section: "Git vs Hub: When to Use What"

---

### 3. Daily Workflow

**File**: `olympus-hub-docs/10-guides/hub-development-flow/05-daily-workflow.md`

**Changes**:

- Remove all references to `hub apply`
- Fix workflow order in all examples: edit → git commit → git push → hub sync scenario
- Add "GitOps Requirement" callout explaining why commit is required
- Update "Common Tasks" to show correct GitOps flow (sync scenario, not apply file)
- Add git context verification steps
- Add branch alignment check before sync
- Add troubleshooting for branch mismatch and dirty file errors
- Clarify that `hub sync` reads from Git, not filesystem
- Add `hub validate` commands for validation before sync

**Key Sections to Update**:

- Line ~120-133: Fix "Modify a Scenario" task workflow order (use `hub sync scenario`)
- Line ~149-160: Fix "Update Hub Application Code" task workflow (use `hub sync scenario`)
- Add new section: "Understanding GitOps: Why Commit First?"
- Add new section: "Checking Branch Alignment Before Sync"
- Update "Development Loop" diagram to show: edit → commit → push → sync scenario
- Update "Troubleshooting Common Issues" with branch mismatch and dirty file errors
- Remove all `hub apply` examples and replace with `hub sync scenario`

---

### 4. Workbench-Based Development

**File**: `olympus-hub-docs/10-guides/hub-development-flow/03-workbench-based-development.md`

**Changes**:

- Remove all references to `hub apply`
- Update "Edit-Sync-Test Cycle" to show: edit → commit → push → hub sync scenario
- Add explanation that hub commands operate on current git branch
- Clarify that workspace branch is associated with workbench instance
- Emphasize that scenario is smallest unit of deployment

**Key Sections to Update**:

- Line ~165-197: Update "Edit-Sync-Test Cycle" with correct GitOps flow (sync scenario)
- Add note about branch association with workbench instance
- Remove `hub apply` examples, replace with `hub sync scenario`

---

### 5. Development to Production Flow

**File**: `olympus-hub-docs/10-guides/hub-development-flow/04-development-to-production-flow.md`

**Changes**:

- Remove all references to `hub apply`
- Update Step 1 (Develop) to show: edit → commit → push
- Update Step 3 (Sync) to use `hub sync scenario` (primary deployment command)
- Add git context information to deployment outputs
- Clarify that scenario is smallest unit of deployment

**Key Sections to Update**:

- Line ~76-92: Update Step 1 to show git commit and push
- Line ~109-125: Update Step 3 to use `hub sync scenario` (not `hub apply`)
- Remove `hub apply` examples, replace with `hub sync scenario`

---

### 6. CI/CD Integration

**File**: `olympus-hub-docs/10-guides/hub-development-flow/07-ci-cd-integration.md`

**Changes**:

- Remove all references to `hub apply`
- Update workflow to show: git commit → git push → hub sync scenario
- Clarify that CI/CD operates on git commits, not filesystem
- Use `hub sync scenario` as deployment command in CI/CD pipelines

**Key Sections to Update**:

- Line ~209-247: Update "Recommended Workflow" to show git commit → push → sync scenario
- Remove `hub apply` examples, replace with `hub sync scenario`

---

### 7. Best Practices

**File**: `olympus-hub-docs/10-guides/hub-development-flow/10-best-practices.md`

**Changes**:

- Remove all references to `hub apply`
- Add "GitOps Best Practices" section
- Update "Git Practices" to emphasize commit-before-sync requirement
- Add git context verification practices
- Add branch alignment best practices
- Add guidance on handling validation errors
- Emphasize scenario-based deployment (smallest unit)

**Key Sections to Add**:

- New section: "GitOps Best Practices"
- Update "Git Practices" section with GitOps requirements (commit before sync)
- New subsection: "Branch Alignment: Always Verify Before Sync"
- New subsection: "Handling Validation Errors"
- New subsection: "Audit Log Awareness: All Actions Are Logged"
- New subsection: "Scenario-Based Deployment: Smallest Unit of Change"
- Remove all `hub apply` best practices, replace with `hub sync scenario`

---

### 8. Collaboration Patterns

**File**: `olympus-hub-docs/10-guides/hub-development-flow/06-collaboration-patterns.md`

**Changes**:

- Add section on workbench instance model (multiple developers = multiple instances)
- Add hub CLI commands for coordination
- Update git workflow examples to show GitOps pattern
- Add git context examples
- Clarify that multiple developers work on same Workbench Specification but different instances

**Key Sections to Update**:

- Line ~199-210: Add hub commands for coordination
- Add new section: "Workbench Instance Model: Multiple Developers"
- Add git context examples
- Remove git workflow guidance (branching strategies, merge/rebase workflows)

---

## New Content to Add

### Why No `hub apply`? GitOps and Scenario-Based Deployment

Add to CLI Channels doc (new section explaining removal of hub apply):

````markdown
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
````

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
````

### GitOps Pattern Explanation

Add to CLI Channels doc and README:

```markdown
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
````


Git Context:

Repository: https://git.hub.acme.com/acme-dev-subscription

Branch: feature/new-trigger

Commit: abc123def456

Tags: []

````
```

### Day 1 Setup Section

Add to README:

```markdown
## Day 1: Quick Start (5 Minutes)

1. **Install hubdev CLI**
   ```bash
   brew install hubdev  # or see [Installation Guide](../hub-cli-setup.md)
   ```

2. **Contact Tenant Admin for access**
   - Tenant name
   - Workbench instance name (or request new instance for your branch)
   - Access permissions
   - Branch association for workbench instance

3. **Login and open workspace**
   ```bash
   hubdev login
   hubdev workspace list
   hubdev workspace open <your-workbench>
   ```

4. **Verify context**
   ```bash
   hub context  # Shows whoami, workbench, branch, git info, last synced status
   ```

5. **Make your first change**
   ```bash
   # Edit scenario files in VS Code
   # Then:
   git add .
   git commit -m "feat: my first change"
   git push
   hub sync scenario <scenario-name>  # Deploy scenario (smallest unit)
   ```
```

### Workbench Instance Model: Multiple Developers

Add to Collaboration Patterns and Workbench-Based Development docs:

```markdown
## Workbench Instance Model: One Instance Per Developer

**Critical Understanding**: A workbench instance can only have **one branch associated** and **one workspace**. Multiple developers working on the same Workbench Specification must create **separate workbench instances**, each mapped to their own branch.

### How It Works

| Scenario | Solution |
|----------|----------|
| **1 developer** working on `main` branch | 1 workbench instance (`dispute-ops-dev`) → `main` branch |
| **3 developers** working on same Workbench Specification | 3 workbench instances:<br>- `dispute-ops-dev-alice` → `feature/alice-trigger`<br>- `dispute-ops-dev-bob` → `feature/bob-ui`<br>- `dispute-ops-dev-charlie` → `main` |
| **Developer switches branches** | Must either:<br>- Switch workbench instance branch (admin/authorized dev)<br>- Use different workbench instance for new branch<br>- Switch to existing workbench instance for that branch |

### Creating Workbench Instances

**For New Developers**:
1. Contact Tenant Admin to request a workbench instance
2. Specify:
   - Workbench Specification name (e.g., `dispute-ops`)
   - Your branch name (e.g., `feature/my-feature`)
   - Your user identity

**For Branch Switching**:
- Option 1: Request new workbench instance for new branch
- Option 2: Have admin/authorized dev update existing instance's branch association
- Option 3: Use existing workbench instance if one exists for your branch

### Best Practices

- **One branch per workbench instance**: Never try to use one instance for multiple branches
- **Coordinate with team**: Check if workbench instance exists for your branch before requesting new one
- **Clean up**: Request deletion of unused workbench instances when done
````

### Git vs Hub Clarification Table

Add to multiple files:

```markdown
## Git vs Hub: When to Use What

| Purpose | Use | Command Example | When |
|---------|-----|-----------------|------|
| **Version control** | Git | `git commit`, `git push` | After editing files |
| **Validate** | Hub | `hub validate -f <file>` or `hub validate scenario <name>` | Before deploying (optional) |
| **Deploy** | Hub | `hub sync scenario <name>` | After committing to Git (primary deployment) |
| **Deploy (full)** | Hub | `hub sync workbench` | Sync entire workbench state |
| **Monitor** | Hub | `hub logs`, `hub watch` | Anytime |
| **Branch management** | Git/Hub | `hub branch` | When switching contexts |

**Key Rules**: 
- Always `git commit` and `git push` before `hub sync`. Hub commands only read from Git.
- Smallest unit of deployment is **Scenario**. Use `hub sync scenario` for deployments.
```

### Validation Errors Documentation

Add to CLI Channels doc (hub sync section) and Troubleshooting sections:

```markdown
## Validation Errors

`hub sync` performs validation checks and **fails immediately** if validation fails:

### Branch Mismatch Error

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

### Dirty File Error

**What it checks**: Files being applied have uncommitted local modifications (dirty files)

**When it fails**: If the local file corresponding to the committed file has uncommitted changes

**Error behavior**: Command fails immediately (no option to continue)

**Example error**:
```

❌ ERROR: Dirty Files Detected

Scenario files have uncommitted local changes:

            - scenarios/dispute-triage/automation.yaml (modified)
            - scenarios/dispute-triage/deployment.yaml (modified)

Hub commands operate on committed Git files only (GitOps pattern).

The scenario files have uncommitted changes that differ from the committed version.

To fix:

Option 1: Commit your changes first (recommended)

git add scenarios/dispute-triage/

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

````

### Best Practices for Avoiding Errors

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
````
````

### hub sync scenario: Detailed Behavior

Add to CLI Channels doc (update `hub sync` section):

```markdown
#### `hub sync scenario <name>`: What Gets Synced

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
````

**Key Points**:

- ✅ **Atomic**: All scenario resources deployed together
- ✅ **From Git**: All files read from committed Git state
- ✅ **Complete**: All resources in scenario, not partial
- ✅ **Dependencies**: All referenced resources must exist and be committed
````

### Uncommitted Changes Detection: Scenario-Specific Scope

Add to CLI Channels doc (update Validation Errors section):

```markdown
### Uncommitted Changes Detection: What Files Are Checked?

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

**Example Error**:
```bash
$ hub sync scenario dispute-triage

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
   
   Option 2: Stash your changes
     git stash
     hub sync scenario dispute-triage
     git stash pop
````


**Why This Scope?**

- Ensures scenario integrity (all scenario components are committed)
- Catches dependencies (referenced resources must be committed)
- Reasonable scope (not checking entire repo, which would be slow)
- Aligns with scenario as atomic unit
````

### hub validate Commands

Add to CLI Channels doc (new section after Validation Errors):

```markdown
## hub validate: Validation-Only Operations

Since `hub apply` was removed (not aligned with GitOps), use `hub validate` for validation-only operations that don't deploy.

### `hub validate -f <file>`

**Purpose**: Validate a single file without deploying. Useful for linting/validation before committing.

**Usage**:
```bash
# Validate a single file
hub validate -f scenarios/dispute-triage/automation.yaml

# Validate multiple files
hub validate -f file1.yaml -f file2.yaml
````


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

### `hub validate scenario <name>`

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
````

### Audit Logging and Non-Repudiation

Add to CLI Channels doc (new section after GitOps Pattern):

```markdown
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
| **Resources Affected** | What was modified | `TrainingSpec/dispute-triage-agent-v1` |
| **Result** | Success/failure | `SUCCESS` or `FAILED: reason` |

### Audit Log Format

Example audit log entry:

````


2026-01-11T14:32:15.123Z | developer@acme.bank | hub sync scenario dispute-triage

git_repo: https://git.hub.acme.com/acme-dev-subscription

git_branch: feature/new-trigger

git_commit: abc123def4567890123456789012345678901234

git_tags: []

workbench_instance: dispute-ops-dev

resources: [ScenarioDeployment/dispute-triage-dev, HubApplicationDeployment/dispute-triage-agent-001]

result: SUCCESS

git_sha: abc123def4567890123456789012345678901234

````

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
````

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
````

### hub audit log Command

Add to CLI Channels doc (Utility Commands section):

```markdown
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
````


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
````

---

## Implementation Details

### Git Context Emission

All hub commands should show git context in their output. Update command examples to include:

```bash
$ hub sync scenario dispute-triage

Git Context:
  Repository: https://git.hub.acme.com/acme-dev-subscription
  Branch: main
  Commit: abc123def456789
  Tags: []

Syncing scenario: dispute-triage...
✓ Scenario synced successfully
  - ScenarioDeployment/dispute-triage-dev created
  - HubApplicationDeployment/dispute-triage-agent-001 created

Audit Log Entry:
  Command: hub sync scenario dispute-triage
  User: developer@acme.bank
  Git SHA: abc123def4567890123456789012345678901234
  Timestamp: 2026-01-11T14:32:15.123Z
  Result: SUCCESS
````

### hub context Command Output

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

### Audit Logging Implementation

**Design Requirements**:

- Every `hub` command execution creates an audit log entry
- Audit log entries are immutable (write-once, append-only)
- Git SHA is included in every entry for non-repudiation
- Audit logs are accessible via `hub audit log` command
- Audit logs can be exported for compliance systems
- Retention policy is configurable per tenant

**Audit Log Fields** (all required):

- Timestamp (ISO 8601)
- User identity (from authentication)
- Full command with arguments
- Git repository URL
- Git branch name
- Git commit SHA (full 40-character SHA)
- Git tags (if any)
- Workbench instance
- Resources affected
- Result (SUCCESS/FAILED with reason)

### Validation Errors for hub sync

`hub sync` detects and **fails immediately** if validation fails:

**1. Branch Mismatch Error**

When current git branch differs from workbench instance's associated branch:

```bash
$ hub sync scenario dispute-triage

❌ ERROR: Branch Mismatch
   Current git branch: feature/new-trigger
   Workbench instance branch: main
   Workbench: dispute-ops-dev
   
   A workbench instance can only be associated with one branch.
   The workbench instance 'dispute-ops-dev' is configured to use branch 
   'main', but you're currently on 'feature/new-trigger'.
   
   To fix:
   - Switch to the workbench's branch: hub branch main && git pull
   - Or request new workbench instance for your branch (contact Tenant Admin)
   - Or update workbench instance branch (requires admin/authorized dev)
```

**2. Dirty Files Error**

When scenario files have uncommitted local changes:

```bash
$ hub sync scenario dispute-triage

❌ ERROR: Dirty Files Detected
   Scenario files have uncommitted local changes:
   - scenarios/dispute-triage/automation.yaml (modified)
   - scenarios/dispute-triage/deployment.yaml (modified)
   
   Hub commands operate on committed Git files only (GitOps pattern).
   The scenario files have uncommitted changes that differ from the committed version.
   
   To fix:
   - Commit changes: git add scenarios/dispute-triage/ && git commit -m "message" && git push
   - Or stash changes: git stash && hub sync scenario dispute-triage && git stash pop
   - Or discard changes: git checkout scenarios/dispute-triage/
```

**Documentation Updates Needed**:

- Add error examples to `hub sync scenario` section  
- Add troubleshooting section for branch mismatch errors
- Add troubleshooting section for dirty file errors
- Update best practices to include branch alignment checks
- Add `hub context` command output showing branch alignment status

### Workflow Diagram Updates

Update all workflow diagrams to show:

```
Edit → Git Commit → Git Push → Hub Sync Scenario
```

Or for validation before sync:

```
Edit → Git Commit → Git Push → Hub Validate Scenario → Hub Sync Scenario
```

Not:

```
Edit → Hub Apply → Git Commit (WRONG - hub apply removed)
Edit → Git Commit → Hub Apply (WRONG - file-level apply not aligned with GitOps)
```

**Key Principle**: Smallest unit of deployment is **Scenario**. Always sync scenarios, not individual files.

---

## Testing Checklist

After implementation, verify:

- [ ] **`hub apply` command is completely removed** from all documentation
- [ ] All workflow examples show: edit → commit → push → sync scenario
- [ ] `hub sync scenario` is documented as primary deployment command
- [ ] `hub validate` commands are documented (validate file, validate scenario)
- [ ] GitOps pattern is explained in CLI doc and README
- [ ] "Why No `hub apply`?" section explains GitOps rationale (scenario is smallest unit)
- [ ] Day 1 setup section is clear and actionable
- [ ] Git vs Hub table appears in relevant docs (no hub apply, includes hub validate)
- [ ] Git context emission is documented for all hub commands
- [ ] Branch mismatch validation errors are documented for `hub sync` (fail by default)
- [ ] Dirty files validation errors are documented for `hub sync` (fail by default)
- [ ] Error message examples are clear and actionable (no "continue anyway" options)
- [ ] Troubleshooting sections include solutions for branch mismatch errors
- [ ] Troubleshooting sections include solutions for dirty file errors
- [ ] Workbench instance model is documented (one instance = one branch = one workspace)
- [ ] Multiple developers = multiple instances pattern is explained
- [ ] Best practices include branch alignment checks
- [ ] Best practices emphasize scenario-based deployment (smallest unit)
- [ ] Audit logging section is documented with git SHA references
- [ ] Non-repudiation guarantee is explained
- [ ] `hub audit log` command is documented with examples
- [ ] Audit log format and fields are clearly explained
- [ ] Compliance benefits of audit logging are highlighted
- [ ] No references to hub reading from filesystem (only Git)
- [ ] Branch association with workbench instance is clear
- [ ] `hub context` command shows whoami, last synced status, branch alignment status
- [ ] Audit log access model is documented (all accessible to authorized users, no per-user filtering)
- [ ] Day 1 setup mentions contacting Tenant Admin for access
- [ ] No git workflow guidance included (as requested)
- [ ] All examples use `hub sync scenario` instead of `hub apply`
- [ ] `hub sync scenario` behavior is documented (reads all 3 spec files from Git)
- [ ] `hub sync scenario` behavior clarifies it syncs ALL resources in scenario (atomic)
- [ ] Uncommitted changes detection scope is documented (scenario files + referenced resources only)
- [ ] Error messages list which scenario files are dirty
- [ ] FAQ includes questions about what gets synced and what files are checked

---

## Items Parked for Later Discussion - Review

Given the latest decisions (removal of `hub apply`, scenario-based deployment), here's a review of the parked items:

### 1. Uncommitted Changes Detection Scope (Question 4)

**Original Question**: Which files does hub check for uncommitted changes when syncing a scenario?

**Analysis**:

- Since we're syncing scenarios (not individual files), the scope should be **scenario-specific**
- Checking all files in the repo would be too broad and slow
- Checking only scenario directory might miss referenced resources

**Proposed Answer** (needs confirmation):

`hub sync scenario <name>` should check for uncommitted changes in:

1. **Scenario definition files** (the three spec files):

            - `ScenarioNormativeSpec` file
            - `ScenarioAutomationSpec` file  
            - `ScenarioDeploymentSpec` file

2. **Directly referenced resource files** (files referenced in the scenario specs):

            - `HubApplicationSpec` files referenced in `ScenarioAutomationSpec`
            - Any other CRD files directly referenced by the scenario

3. **NOT** all files in the repo (too broad)
4. **NOT** files in other scenarios (out of scope)

**Rationale**:

- Ensures scenario integrity (all scenario components are committed)
- Catches dependencies (referenced resources must be committed)
- Reasonable scope (not checking entire repo)
- Aligns with scenario as atomic unit

**Status**: ✅ **CONFIRMED** - Update documentation accordingly

---

### 2. hub sync scenario Behavior (Question 9)

**Original Questions**:

- Does `hub sync scenario` read all scenario definitions from Git?
- What if scenario definition files have uncommitted changes?
- Does it sync all resources in the scenario, or only those specified?

**Analysis**:

- We've already decided: commands read from Git (GitOps pattern) ✅
- We've already decided: commands fail if files are dirty ✅
- The "all resources vs specified" question is now moot (we removed file-level applies)

**Proposed Answers** (needs confirmation):

**Q1: Does `hub sync scenario` read all scenario definitions from Git?**

- **Answer**: **Yes**. `hub sync scenario` reads all three scenario definition files from Git:
        - `ScenarioNormativeSpec` (business context)
        - `ScenarioAutomationSpec` (automation logic)
        - `ScenarioDeploymentSpec` (deployment settings)
- It also reads all referenced resource files from Git (HubApplicationSpec, etc.)

**Q2: What if scenario definition files have uncommitted changes?**

- **Answer**: **Command fails immediately** (already decided - dirty file error)
- Error message should list which scenario files are dirty
- Developer must commit or stash before sync can proceed

**Q3: Does it sync all resources in the scenario, or only those specified?**

- **Answer**: **All resources in the scenario** (this is what "sync scenario" means)
- When you run `hub sync scenario dispute-triage`, it:
        - Reads all three scenario spec files from Git
        - Processes all resources defined in those specs
        - Creates/updates all `HubApplicationDeployment` resources for the scenario
        - Triggers creation of all child resources (EmploymentSpec, Services, Deployments, etc.)
- You don't specify individual resources - you specify the scenario, and everything in it gets synced

**Rationale**:

- Scenario is atomic unit - all or nothing
- Ensures consistency (all scenario resources deployed together)
- Aligns with GitOps principle (sync state, not individual resources)
- Matches the "smallest unit of deployment is Scenario" principle

**Status**: ✅ **CONFIRMED** - Update documentation accordingly

---

## Summary

Both parked items are now **CONFIRMED** and ready for documentation updates:

1. **Uncommitted Changes Scope**: ✅ **CONFIRMED**

            - Check scenario definition files (all 3 spec files)
            - Check directly referenced resource files (HubApplicationSpec, etc.)
            - Do NOT check all files in repo or files in other scenarios

2. **hub sync scenario Behavior**: ✅ **CONFIRMED**

            - Reads all scenario definitions from Git ✅
            - Fails if files are dirty ✅
            - Syncs all resources in the scenario ✅ (atomic deployment)

**Documentation Updates Required**: See section below for specific updates needed.

---

## Additional Documentation Updates for Confirmed Behaviors

### Files That Need Updates for `hub sync scenario` Behavior Clarifications

Based on the confirmed answers, the following files need updates to explicitly document:

1. **What files are checked for uncommitted changes**
2. **What resources are synced (all resources in scenario)**
3. **How scenario sync works (reads all 3 spec files from Git)**

### Files to Update

#### 1. CLI Channels Documentation

**File**: `olympus-hub-docs/06-ux-architecture/tenant-domain/cli-channels-for-developers.md`

**Additional Changes** (beyond removing `hub apply`):

- Update `hub sync scenario` section to explicitly state:
        - Reads all 3 scenario spec files from Git (ScenarioNormativeSpec, ScenarioAutomationSpec, ScenarioDeploymentSpec)
        - Reads all referenced resource files from Git (HubApplicationSpec, etc.)
        - Syncs **all resources** in the scenario (atomic deployment)
        - Checks for uncommitted changes in: scenario spec files + directly referenced resource files
        - Does NOT check all files in repo or files in other scenarios
- Add example showing what gets synced when you run `hub sync scenario dispute-triage`
- Update error messages to list which scenario files are dirty

**Key Sections to Update**:

- Line ~368-395: `hub sync` section - add detailed behavior explanation
- Add subsection: "What Gets Synced: All Resources in Scenario"
- Add subsection: "Uncommitted Changes Detection: Scenario-Specific Scope"
- Update error examples to show scenario file listing

#### 2. Agent Development Lifecycle Guide

**File**: `olympus-seer-docs/seer-design/guides/agent-development-lifecycle.md`

**Additional Changes**:

- Update all `hub sync scenario` examples to clarify it syncs entire scenario
- Add note that scenario is atomic unit (all resources deployed together)
- Update Quick Start section to emphasize scenario-based deployment

#### 3. Agent Lifecycle FAQ

**File**: `olympus-seer-docs/seer-design/guides/agent-lifecycle-faq.md`

**Additional Changes**:

- Update Q13 (Smallest unit of deployment) to clarify what "sync scenario" means
- Add new Q: "What files does hub check for uncommitted changes when syncing a scenario?"
- Add new Q: "Does hub sync scenario sync all resources or just some?"

#### 4. Daily Workflow Guide

**File**: `olympus-hub-docs/10-guides/hub-development-flow/05-daily-workflow.md`

**Additional Changes**:

- Remove all `hub apply` references (already in plan)
- Update workflow examples to show scenario sync behavior
- Add troubleshooting for "which files are checked" questions

#### 5. Development to Production Flow

**File**: `olympus-hub-docs/10-guides/hub-development-flow/04-development-to-production-flow.md`

**Additional Changes**:

- Remove `hub apply` references (already in plan)
- Update Step 3 (Sync) to clarify scenario sync behavior
- Add explanation of what gets synced (all scenario resources)

#### 6. Workbench-Based Development

**File**: `olympus-hub-docs/10-guides/hub-development-flow/03-workbench-based-development.md`

**Additional Changes**:

- Update Edit-Sync-Test cycle to clarify scenario sync behavior
- Add note about atomic scenario deployment

#### 7. Best Practices

**File**: `olympus-hub-docs/10-guides/hub-development-flow/10-best-practices.md`

**Additional Changes**:

- Add best practice: "Understand what gets synced: all resources in scenario"
- Add best practice: "Keep scenario files and referenced resources committed together"

---

## Related Files

- [CLI Channels for Developers](../../06-ux-architecture/tenant-domain/cli-channels-for-developers.md) - Primary CLI reference
- [Hub CLI Setup](../hub-cli-setup.md) - Installation guide
- [Agent Development Lifecycle Guide](../../../../olympus-seer-docs/seer-design/guides/agent-development-lifecycle.md) - May need GitOps updates too

---

## Plan Coverage Confirmation

### ✅ All Related Files Included

The plan includes updates to **all files** that reference `hub apply` or need updates for GitOps/scenario-based deployment:

**Core Documentation**:

1. ✅ CLI Channels for Developers (`cli-channels-for-developers.md`) - Primary CLI reference
2. ✅ Hub Development Flow README (`hub-development-flow/README.md`) - Guide overview
3. ✅ Daily Workflow (`05-daily-workflow.md`) - Common workflows
4. ✅ Workbench-Based Development (`03-workbench-based-development.md`) - Development model
5. ✅ Development to Production Flow (`04-development-to-production-flow.md`) - Deployment flow
6. ✅ CI/CD Integration (`07-ci-cd-integration.md`) - CI/CD workflows
7. ✅ Best Practices (`10-best-practices.md`) - Best practices guide
8. ✅ Collaboration Patterns (`06-collaboration-patterns.md`) - Team collaboration

**Seer Documentation** (may need updates):

9. ✅ Agent Development Lifecycle Guide (`agent-development-lifecycle.md`) - Agent lifecycle
10. ✅ Agent Lifecycle FAQ (`agent-lifecycle-faq.md`) - Common questions

**Additional Files** (referenced but may need updates):

- Hub CLI Setup (`hub-cli-setup.md`) - Installation guide (may need workflow updates)

### ✅ All Key Changes Covered

1. ✅ Removal of `hub apply` command from all files
2. ✅ Standardization on `hub sync scenario` as primary deployment command
3. ✅ Addition of `hub validate` commands
4. ✅ GitOps pattern documentation (commit before sync)
5. ✅ Validation errors (branch mismatch, dirty files)
6. ✅ Audit logging with Git SHA references
7. ✅ **NEW**: `hub sync scenario` detailed behavior (reads all 3 spec files, syncs all resources)
8. ✅ **NEW**: Uncommitted changes detection scope (scenario files + referenced resources only)
9. ✅ Workbench instance model (one instance = one branch = one workspace)
10. ✅ `hub context` output (whoami, last synced, branch alignment)

### ✅ Content Sections Ready

All new content sections are defined in the plan:

- GitOps Pattern explanation
- Why No `hub apply`? section
- `hub sync scenario` detailed behavior
- Uncommitted changes detection scope
- `hub validate` commands
- Audit logging and non-repudiation
- Workbench instance model
- Day 1 setup
- Git vs Hub clarification table
- Validation errors documentation
- `hub context` command output

**Plan Status**: ✅ **COMPLETE** - All related files identified and all changes specified