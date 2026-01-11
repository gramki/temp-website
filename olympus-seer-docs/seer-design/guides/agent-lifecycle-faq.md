# Agent Development Lifecycle FAQ

> **Audience**: Architects, Developers, and Platform Engineers  
> **Purpose**: Clarify common questions about developing, training, and employing AI agents in Seer  
> **Last Updated**: 2026-01-11
> 
> **See Also**: [Agent Development Lifecycle Guide](./agent-development-lifecycle.md) for the complete walkthrough with examples.

---

## Quick Reference

### What You Create vs. What's Generated

| CRD | Created By | Your Responsibility? |
|-----|------------|---------------------|
| **ScenarioNormativeSpec** | Process Architect | ❌ You receive this |
| **TrainingSpec** | Agent Engineer | ✅ **You create this** |
| **HubApplicationSpec** | Developer | ✅ **You create this** |
| **ScenarioAutomationSpec** | Developer | ✅ **You create this** |
| **ScenarioDeploymentSpec** | Supervisor | ⚠️ You may create (sandbox) or request (production) |
| **HubApplicationDeployment** | Hub Operators | ❌ Auto-generated |
| **EmploymentSpec** | Seer Operator | ❌ Auto-generated |

### Essential CLI Commands

```bash
# Validate (optional, before committing)
hub validate scenario my-scenario-sandbox

# Commit to Git (GitOps requirement)
git add .
git commit -m "feat: update scenario"
git push

# Deploy (smallest unit = Scenario, reads from Git)
hub sync scenario my-scenario-sandbox

# Monitor
hub logs agent my-agent-emp-001 --follow
hub metrics agent my-agent-emp-001

# Validate & Publish
hub validate training-spec my-agent-v1 --workbench my-sandbox
hub publish training-spec my-agent-v1 --version 1.0.0
```

---

## Conceptual Questions

### Q1: Are Trained Agents always bound to a Scenario Definition?

**Short Answer**: No, but yes conceptually.

**Detailed Answer**: 

At the **artifact level**, a Training Specification (which defines a Trained Agent) is an independent, reusable artifact. Once published, it can be employed across multiple Scenarios.

However, at the **development level**, a Training Specification cannot be meaningful without being grounded in Scenario context:

1. **Conceived** for a specific Scenario (Genesis)
2. **Developed and validated** in a Sandbox Workbench with that Scenario (Training)
3. **Improved** based on feedback from Employed Agents in production Scenarios (Evolution)

A Training Specification created without Scenario context would be hypothetical and unproven.

---

### Q2: What's the relationship between "Deploying" and "Employing" an agent?

**Answer**: They are the same thing. In Seer terminology, **deploying an agent = employing an agent**.

We use "employ" because it accurately describes what happens: a Trained Agent is assigned to a specific work context (Workbench Instance) and granted authority to act—just like a skilled employee being assigned to a specific team or project.

| Action | What Happens |
|--------|--------------|
| **Deploy/Employ** | Trained Agent is bound to a Workbench Instance with a concrete environment, granted authority, and starts handling work |

**How to deploy**:
```bash
# 1. Create your ScenarioDeploymentSpec targeting a Workbench Instance
# Edit scenario-deployment-sandbox.yaml, then commit to Git (GitOps requirement)
git add scenario-deployment-sandbox.yaml
git commit -m "feat: sandbox deployment spec"
git push

# 2. Sync the Scenario (smallest unit of deployment, reads from Git)
hub sync scenario my-scenario-sandbox
```

---

### Q3: How does the agent lifecycle compare to human employment?

**Answer**: The analogy is intentional and direct:

| Human Employment | Seer Agent Lifecycle |
|------------------|----------------------|
| **Skilled Person** (educated, has competencies) | **Raw Agent** (base LLM capabilities) |
| **Trained Employee** (trained for role, knows procedures) | **Trained Agent** (TrainingSpec applied) |
| **Employed Worker** (assigned to team, authorized to act) | **Employed Agent** (EmploymentSpec created) |
| **Training Program** (develops skills for role) | **Training Specification** |
| **Job Assignment** (role in specific project/department) | **Employment Specification** |
| **Project/Department** (concrete work context) | **Workbench Instance + Environment** |
| **Training Facility** (safe environment to learn) | **Sandbox Workbench Instance** |

Just as skilled humans are *employable* but only become *employed* when assigned to a specific job, Trained Agents are *deployable* but only become *Employed Agents* when bound to a specific Workbench Instance.

---

## CRD and Specification Questions

### Q4: What is the relationship between Hub and Seer CRDs?

**Answer**: There are two parallel hierarchies that connect at specific points:

```
HUB CRDs                                    SEER CRDs
────────                                    ─────────
ScenarioNormativeSpec
        │
        ▼
ScenarioAutomationSpec ──refs──► HubApplicationSpec ──refs──► TrainingSpec
        │                              │
        ▼                              │
ScenarioDeploymentSpec                 │
        │                              │
        ▼ (Hub Operators)              │
HubApplicationDeployment ◄─────────────┘
        │
        ▼ (Seer Operator)
                                        EmploymentSpec
```

---

### Q5: Is there a separate "TrainedAgentSpec" CRD?

**Answer**: No. The "Trained Agent" is represented by **two CRDs together**:

| Perspective | CRD |
|-------------|-----|
| **Hub sees** | `HubApplicationSpec` with `runtime: seer` |
| **Seer sees** | `TrainingSpec` (referenced via `seerTrainingRef`) |

The `HubApplicationSpec` is the Hub-facing representation, while `TrainingSpec` contains the actual training configuration (prompts, knowledge, guardrails, etc.).

---

### Q6: What is `HubApplicationDeployment` and when is it created?

**Answer**: `HubApplicationDeployment` is a CRD that represents a running instance of a Hub Application. It is:

- **Generated by Hub Operators** when you run `hub sync scenario` on a `ScenarioDeploymentSpec`
- The **parent resource** for runtime-specific child resources
- Contains application identity and runtime-specific extensions

For Seer agents, the Seer Operator watches for `HubApplicationDeployment` resources and creates the corresponding `EmploymentSpec` and Atlantis resources (Service, Deployment, etc.).

**The deployment chain**:
```
ScenarioDeploymentSpec (you create)
        │
        ▼ hub sync triggers
HubApplicationDeployment (generated by Hub Operators)
        │
        ▼ Seer Operator processes
EmploymentSpec (generated)
        │
        ▼ Seer Operator creates
Atlantis Resources (Service, Deployment)
```

---

### Q7: What is the canonical way to reference a Training Spec from Hub?

**Answer**: Use `seerTrainingRef` in the `HubApplicationSpec`:

```yaml
apiVersion: hub.olympus.io/v1
kind: HubApplicationSpec
metadata:
  name: dispute-triage-agent
  labels:
    seer.olympus.io/resource-type: trained-agent
spec:
  runtime:
    type: seer
  
  # CANONICAL: seerTrainingRef
  seerTrainingRef:
    name: dispute-triage-agent-v1
    version: "1.0.0"
```

Do **not** use inline `seer_config` with embedded prompts—that pattern is for simpler use cases without formal training management.

---

### Q8: How are EmploymentSpecs created?

**Answer**: EmploymentSpecs are **not created manually** by developers. They are:

1. **Generated by Seer Operator** when it processes a `HubApplicationDeployment`
2. Created with an `ownerReference` pointing to the parent `HubApplicationDeployment`
3. Populated with resolved bindings (tools, knowledge, memory stores)

**Your workflow**:
```bash
# 1. Create the ScenarioDeploymentSpec (declares deployment intent)
# Edit scenario-deployment-sandbox.yaml, then commit to Git (GitOps requirement)
git add scenario-deployment-sandbox.yaml
git commit -m "feat: sandbox deployment spec"
git push

# 2. Sync to trigger operator chain (reads from Git)
hub sync scenario my-scenario-sandbox

# 3. Operators generate HubApplicationDeployment → EmploymentSpec → Resources
```

**Key insight**: When you update `TrainingSpec` and `HubApplicationSpec` and re-sync, the operators reconcile automatically—you don't manually recreate the `EmploymentSpec`.

---

## Sandbox and Training Questions

### Q9: How is a Sandbox Workbench different from Production?

**Answer**: Sandbox Workbench Instances are distinguished by:

1. **Lifecycle Stage Labels** (on WorkbenchInstance): `hub.olympus.io/lifecycle-stage: dev` or `build`
2. **Naming Conventions**: e.g., `acme-disputes-sandbox`, `acme-disputes-dev`
3. **Tags**: Optional `hub.olympus.io/workbench-type: sandbox`

Note: The `lifecycle-stage` label is defined on the **WorkbenchInstance** resource. Child resources (HubApplicationDeployment, EmploymentSpec) inherit this label.

Functionally, sandbox and production Workbench Instances work **identically**—the same operators process them, the same CRDs are created. The difference is in:
- Data sources (synthetic/anonymized vs. production)
- Network isolation
- Approval workflows

---

### Q10: How do I train an agent in a sandbox before production?

**Answer**: Follow the same deployment flow, but target a sandbox Workbench Instance:

```bash
# 1. Create your specs (edit files in VS Code)
# Edit: training-spec.yaml, hub-application-spec.yaml, scenario-automation-spec.yaml

# 2. Commit to Git (GitOps requirement)
git add training-spec.yaml hub-application-spec.yaml scenario-automation-spec.yaml
git commit -m "feat: initial agent specs (version 0.1.0)"
git push

# 3. Create ScenarioDeploymentSpec targeting sandbox
# Edit scenario-deployment-sandbox.yaml, then commit
git add scenario-deployment-sandbox.yaml
git commit -m "feat: sandbox deployment spec"
git push

# 4. Deploy to sandbox (syncs entire scenario from Git)
hub sync scenario my-scenario-sandbox

# 5. Monitor and iterate
hub logs agent my-agent-emp-001 --follow
hub metrics agent my-agent-emp-001

# 6. Update TrainingSpec based on observations
# Edit training-spec.yaml (version: 0.2.0), then commit
git add training-spec.yaml
git commit -m "feat: update to version 0.2.0"
git push

# 7. Re-sync to propagate changes (reads from Git)
hub sync scenario my-scenario-sandbox

# 8. When satisfied, validate and publish
hub validate training-spec my-agent-v1 --workbench my-sandbox
hub publish training-spec my-agent-v1 --version 1.0.0

# 9. Deploy to production
# Edit scenario-deployment-prod.yaml, then commit
git add scenario-deployment-prod.yaml
git commit -m "feat: production deployment spec"
git push
hub sync scenario my-scenario-prod
```

Note: The `lifecycle-stage` label is on the **WorkbenchInstance**, not the `ScenarioDeploymentSpec`. Child resources inherit it.

---

### Q11: How do learnings from production agents get back into Training Specs?

**Answer**: Through a **governed feedback loop**:

```
Employed Agent (production) 
    │
    └── Suggests learnings ──► Cognitive Operations Steward
                                      │
                                      └── Reviews ──► Change Management
                                                            │
                                                            └── Approved changes ──► Training Spec v(n+1)
```

Key governance principles:
- Learnings are **suggestions**, not automatic updates
- Different governance levels for different change types (prompt tweaks vs. guardrail changes)
- Changes are validated in sandbox before production

---

## Development Environment Questions

### Q12: Is there a local development environment for Hub applications?

**Answer**: No. There is no "local development" for Hub applications. All development happens within Hub Workbench Instances:

| Environment | Lifecycle Stage | Use Case |
|-------------|-----------------|----------|
| **Dev Workbench Instance** | `dev` | Rapid iteration, debugging, experimentation |
| **DevOps Workbench** | `dev` or `build` | CI/CD pipelines, automated testing, observability |
| **Sandbox Workbench Instance** | `build` | Pre-production validation, formal testing |

See [DevOps Workbench Pattern](../../../../olympus-hub-docs/09-composite-systems-and-patterns/devops-workbench.md) for setup details.

---

### Q13: What is the smallest unit of deployment?

**Answer**: **Scenario**. You deploy Scenarios, not individual agents or applications.

```bash
# Deploy a Scenario (includes all its applications/agents)
hub sync scenario my-scenario-sandbox

# NOT: hub deploy agent my-agent (this doesn't exist)
```

The `hub sync scenario` command:
1. Reads all 3 scenario spec files from Git (ScenarioNormativeSpec, ScenarioAutomationSpec, ScenarioDeploymentSpec)
2. Reads all referenced resource files from Git (HubApplicationSpec, etc.)
3. Processes the `ScenarioDeploymentSpec`
4. Generates `HubApplicationDeployment` for each application in the Scenario
5. Triggers runtime operators (e.g., Seer Operator) to create child resources
6. Syncs **all resources** in the scenario atomically

**Key Points**:
- ✅ Reads from committed Git files only (GitOps pattern)
- ✅ Syncs entire scenario (all resources), not partial
- ✅ Atomic deployment (all or nothing)
- ✅ Fails if branch mismatch or dirty files detected

---

### Q14: What files does hub check for uncommitted changes when syncing a scenario?

**Answer**: `hub sync scenario` checks for uncommitted changes in:

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

**Why This Scope?**
- Ensures scenario integrity (all scenario components are committed)
- Catches dependencies (referenced resources must be committed)
- Reasonable scope (not checking entire repo, which would be slow)
- Aligns with scenario as atomic unit

---

### Q15: Does hub sync scenario sync all resources or just some?

**Answer**: **All resources in the scenario**. When you run `hub sync scenario <name>`, Hub syncs everything in that scenario atomically.

**What Gets Synced**:
- All scenario spec files (normative, automation, deployment)
- All HubApplicationDeployment resources for the scenario
- All child resources (EmploymentSpec, Services, Deployments, etc.)

**Example**:
```bash
$ hub sync scenario dispute-triage

Syncing scenario: dispute-triage...
  ✓ ScenarioDeployment/dispute-triage-sandbox created
  ✓ HubApplicationDeployment/dispute-triage-agent-001 created
  ✓ EmploymentSpec/dispute-triage-emp-001 created (by Seer Operator)
  ✓ Service/dispute-triage-emp-001-svc created
  ✓ Deployment/dispute-triage-emp-001-deployment created

✓ Scenario synced successfully (all resources deployed atomically)
```

You don't specify individual resources—you specify the scenario, and everything in it gets synced.

---

### Q16: How do I get started if I'm new to the team?

**Answer**: Before Day 1, ensure you have:

| Prerequisite | Who Provides It | How to Get It |
|--------------|-----------------|---------------|
| Scenario Definition | Process Architect | Check Workbench Scenario registry or ask team lead |
| Cognitive Design Document | CSA | Linked in Scenario Definition or onboarding ticket |
| Sandbox Workbench Instance | Platform Team / Supervisor | Request via provisioning process |
| Knowledge Bases | KMO | Listed in Cognitive Design Document |
| `hub` CLI | Self-service | See [Hub CLI Installation Guide](../../../../olympus-hub-docs/10-guides/hub-cli-setup.md) |

---

## Naming and Convention Questions

### Q17: What naming conventions should I use?

**Answer**:

| Resource Type | Naming Pattern | Display Name Pattern |
|---------------|----------------|---------------------|
| **TrainingSpec** | `{agent-name}-v{version}` | `"{Name} (Training Spec)"` |
| **HubApplicationSpec** | `{agent-name}` | `"{Name} (Trained Agent)"` |
| **HubApplicationDeployment** | `{agent-name}-{instance}-{seq}` | `"{Name} (Employed) - {Instance}"` |
| **EmploymentSpec** | `{agent-name}-emp-{seq}` | Inherits from parent |

Labels for Seer resources:
```yaml
labels:
  seer.olympus.io/resource-type: trained-agent  # or: employed-agent
  seer.olympus.io/agent-type: case-worker       # or: orchestrator, specialist
  hub.olympus.io/runtime: seer
```

Note: `hub.olympus.io/lifecycle-stage` is inherited from WorkbenchInstance by deployment resources, not set on specification resources like TrainingSpec or HubApplicationSpec.

---

### Q18: What do version numbers mean for Training Specs?

**Answer**: Version semantics indicate publication status:

| Version | Meaning | State |
|---------|---------|-------|
| `0.x.x` | Draft/development | Pre-publication, guardrails modifiable |
| `1.0.0+` | Production-ready | Published, guardrails **immutable** |

```yaml
# During development
metadata:
  version: "0.1.0"  # Draft

# After validation and publication
metadata:
  version: "1.0.0"  # Production-ready
```

---

### Q19: How do I know if a HubApplicationSpec is a Seer Trained Agent?

**Answer**: Check for:

1. **Runtime type**: `spec.runtime.type: seer`
2. **Label**: `seer.olympus.io/resource-type: trained-agent`
3. **seerTrainingRef**: Presence of this field (canonical for trained agents)
4. **Display name**: Should include "(Trained Agent)" by convention

```yaml
metadata:
  labels:
    seer.olympus.io/resource-type: trained-agent
spec:
  runtime:
    type: seer
  seerTrainingRef:
    name: my-agent-training-v1
```

---

## Common Mistakes

### Q20: What are common anti-patterns to avoid?

| Anti-Pattern | Why It's Wrong | Correct Approach |
|--------------|----------------|------------------|
| **Creating TrainingSpec without Scenario context** | Training is hypothetical, not grounded | Start with Scenario, derive training from its needs |
| **Manually creating EmploymentSpec** | Bypasses operator workflow | Let Seer Operator create from HubApplicationDeployment |
| **Using inline `seer_config` for formal agents** | Bypasses training management | Use `seerTrainingRef` to TrainingSpec |
| **Deploying directly to production** | Agent behavior is unvalidated | Always train/validate in sandbox first |
| **Employing agent to unrelated Scenario** | Training doesn't match work | Match Scenario to training provenance |

---

### Q21: What's the difference between Scenario specs and agent specs?

**Answer**: 

**Scenario specs** define the business context (the "what"):
- NormativeSpec: Roles, Goals, SOPs (Process Architect)
- AutomationSpec: Triggers, Tool bindings (Developer)  
- DeploymentSpec: Queues, SLAs, Activation (Supervisor)

**Agent specs** define the AI agent (the "who"):
- TrainingSpec: Knowledge, Skills, Prompts, Guardrails (Agent Engineer)
- HubApplicationSpec: Hub-facing wrapper (Developer)
- EmploymentSpec: Runtime authority and bindings (Generated)

The connection point is `ScenarioAutomationSpec.application.ref` → `HubApplicationSpec`.

---

## Troubleshooting Questions

### Q22: What are common error messages and how do I fix them?

| Error | Likely Cause | Fix |
|-------|--------------|-----|
| `ScenarioNormativeSpec not found` | Missing prerequisite | `hub get scenario-normative {name}` |
| `TrainingSpec version mismatch` | HubApplicationSpec references wrong version | Update `seerTrainingRef.version` |
| `Workbench instance not found` | Sandbox doesn't exist | `hub get workbench-instances` |
| `Insufficient permissions for sync` | Not authorized | Request sync from Supervisor |
| `Guardrail validation failed` | Config violates constraints | Review guardrails; may require ARAO approval |

---

### Q23: How do I debug agent behavior in sandbox?

**Answer**: Use the monitoring commands:

```bash
# View agent decision logs (real-time)
hub logs agent my-agent-emp-001 --follow

# View agent metrics
hub metrics agent my-agent-emp-001

# Open Workbench dashboard
hub dashboard open my-workbench-sandbox

# Compare sandbox vs production configuration
hub diff scenario-deployment my-scenario-sandbox my-scenario-prod
```

---

## Related Documentation

- [Agent Development Lifecycle Guide](./agent-development-lifecycle.md)
- [Agentic Automation Lifecycle Journey](../personas-and-needs/journeys/agentic-automation-lifecycle.md)
- [Training Spec CRD](../hub-integration/training-spec-crd.md)
- [Employment Spec CRD](../hub-integration/employment-spec-crd.md)
- [HubApplicationDeployment](../../../../olympus-hub-docs/02-system-design/implementation-concepts/hub-application-deployment.md)
- [Scenario Specification Types](../../../../olympus-hub-docs/02-system-design/implementation-concepts/scenario-specification-types.md)

---

*Have more questions? Contact the Platform Architecture team.*
